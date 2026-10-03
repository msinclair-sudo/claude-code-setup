"""Liveness and nag rules. Run: python3 -m unittest discover harness/tests"""
import importlib.machinery
import importlib.util
import json
import socket
import tempfile
import time
import unittest
from pathlib import Path
from unittest import mock

_SRC = Path(__file__).resolve().parents[1] / "bin" / "harness"
_ld = importlib.machinery.SourceFileLoader("harness_cli", str(_SRC))
hz = importlib.util.module_from_spec(importlib.util.spec_from_loader("harness_cli", _ld))
_ld.exec_module(hz)

HOST = socket.gethostname()
OLD = time.strftime("%Y-%m-%dT%H:%M:%S%z", time.localtime(time.time() - 3 * 3600))


class FakeCtx:
    """Just enough of Ctx: a tree, a state dir, locks."""

    def __init__(self, parents):
        self.dir = Path(tempfile.mkdtemp())
        self.state = self.dir
        self.tree = {"nodes": {n: {"parent": p} for n, p in parents.items()}}

    def children(self, name):
        return sorted(n for n, s in self.tree["nodes"].items() if s.get("parent") == name)

    def rank(self, node):
        return 0 if not self.tree["nodes"][node].get("parent") else 1

    me = "main"

    def require_enrolled(self):
        pass

    def node(self):
        return self.me, self.tree["nodes"][self.me]

    def lock_path(self, node):
        return self.dir / "locks" / f"{node}.lock"

    def state_file(self, kind, name, ext):
        return self.dir / kind / f"{name}{ext}"

    def lock(self, node, pid, ref="ref-" + "x" * 8):
        p = self.lock_path(node)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(json.dumps({"node": node, "ref": ref, "pid": pid, "host": HOST}))


class Liveness(unittest.TestCase):
    def test_other_host_is_unknown(self):
        self.assertIsNone(hz.holder_alive({"host": "elsewhere", "pid": 1}))

    def test_dead_pid_with_ghost_roster_row_is_dead(self):
        # obs 1, 16: the roster row outlives the process and has no pid.
        ghost = [{"sessionId": "r", "state": "working"}]
        with mock.patch.object(hz, "pid_alive", return_value=False), \
             mock.patch.object(hz, "live_sessions", return_value=[]):
            self.assertFalse(hz.holder_alive({"host": HOST, "pid": 99, "ref": "r"}, ghost))

    def test_resumed_session_keeps_id_and_is_alive(self):
        with mock.patch.object(hz, "pid_alive", side_effect=lambda p: p == 7), \
             mock.patch.object(hz, "live_sessions",
                               return_value=[{"sessionId": "r", "pid": 7}]):
            self.assertTrue(hz.holder_alive({"host": HOST, "pid": 99, "ref": "r"}))

    def test_bad_pids(self):
        self.assertFalse(hz.pid_alive(0))
        self.assertFalse(hz.pid_alive(None))
        self.assertFalse(hz.pid_alive(2 ** 22 + 12345))


class IdleNag(unittest.TestCase):
    def setUp(self):
        self.ctx = FakeCtx({"main": None, "dev": "main", "dev_1": "dev"})
        self.q = [{"task": "s3", "written_at": OLD}]

    def owes(self, marks, alive):
        with mock.patch.object(hz, "open_marks", return_value=marks), \
             mock.patch.object(hz, "queue", return_value=self.q), \
             mock.patch.object(hz, "holder_alive", return_value=alive), \
             mock.patch.object(hz, "last_write", return_value=None):
            return hz.lead_owes(self.ctx, "main")

    def test_lead_waiting_on_its_lane_is_not_idle(self):
        self.ctx.lock("dev", 1)
        self.assertEqual(self.owes({"s1a": {"_node": "dev_1"}}, True), [])

    def test_quiet_live_lead_is_told_by_message_not_recycle(self):
        self.ctx.lock("dev", 1)
        (kind, child, task, _), = self.owes({}, True)
        self.assertEqual((kind, child, task), ("start", "dev", "s3"))
        self.assertNotIn("recycle", hz.owed_line(kind, child, task, 0))

    def test_dead_lead_is_down_not_idle(self):
        self.ctx.lock("dev", 1)
        (kind, *_), = self.owes({}, False)
        self.assertEqual(kind, "down")


class Orientation(unittest.TestCase):
    def setUp(self):
        self.ctx = FakeCtx({"main": None, "dev": "main"})

    def items(self, fam=None, unread=None, unactioned=(), marks=None):
        with mock.patch.object(hz, "lead_owes", return_value=[]), \
             mock.patch.object(hz, "rank0_owes", return_value=[]), \
             mock.patch.object(hz, "open_waits", return_value={}), \
             mock.patch.object(hz, "focus_family", return_value=fam), \
             mock.patch.object(hz, "unread_brief_comments", return_value=unread or {}), \
             mock.patch.object(hz, "unactioned_briefs", return_value=list(unactioned)), \
             mock.patch.object(hz, "open_marks", return_value=marks or {}), \
             mock.patch.object(hz, "queue",
                               return_value=[{"task": t} for t in unactioned]):
            return hz.queue_items(self.ctx, "main")

    def test_comments_collapse_to_one_line(self):
        out = self.items(unread={"a": [{}], "b": [{}, {}]})
        self.assertEqual(list(out), ["comment:3"])

    def test_focus_drops_comments_outside_it(self):
        self.assertEqual(self.items(fam={"a"}, unread={"b": [{}]}), {})

    def test_handed_only_when_nothing_in_flight(self):
        self.assertEqual(self.items(unactioned=["x"], marks={"t": {"_node": "dev"}}), {})
        self.assertIn("handed:x", self.items(unactioned=["x", "y"]))
        self.assertNotIn("handed:y", self.items(unactioned=["x", "y"]))

    def test_handed_skips_a_brief_that_waits(self):
        with mock.patch.object(hz, "waits_on",
                               side_effect=lambda c, b: ["after z"] if b["task"] == "x" else []):
            self.assertIn("handed:y", self.items(unactioned=["x", "y"]))


class Focus(unittest.TestCase):
    def setUp(self):
        self.ctx = FakeCtx({"main": None})
        d = self.ctx.dir / "briefs"
        d.mkdir()
        for stem, frm in {"enrich_citations": None, "enrich_fulltext": None,
                          "s7_pmc_core": "enrich-fulltext", "surface_polish": None}.items():
            (d / f"{stem}.json").write_text(json.dumps({"from": frm} if frm else {}))

    def focus(self, rec):
        (self.ctx.dir / "focus.json").write_text(json.dumps(rec))
        return hz.focus_family(self.ctx)

    def test_glob_covers_several_segments_and_their_parts(self):
        # obs 53: the owner's priority spans segments with no common parent.
        fam = self.focus({"tasks": ["enrich*"]})
        self.assertEqual(fam, {"enrich_citations", "enrich_fulltext", "s7_pmc_core"})

    def test_several_names(self):
        fam = self.focus({"tasks": ["enrich-citations", "surface-polish"]})
        self.assertEqual(fam, {"enrich_citations", "surface_polish"})

    def test_old_single_task_record_still_reads(self):
        self.assertEqual(self.focus({"task": "enrich-fulltext"}),
                         {"enrich_fulltext", "s7_pmc_core"})

    def test_unset_is_none(self):
        self.assertIsNone(hz.focus_family(self.ctx))

    def test_replacement_inherits_focus(self):
        # obs 56: --supersede --by dropped the replacement out of focus.
        d = self.ctx.dir / "briefs"
        (d / "chrome_over_canvas.json").write_text(json.dumps(
            {"superseded_for": "chrome-over-canvas-resumed"}))
        (d / "chrome_over_canvas_resumed.json").write_text(json.dumps({}))
        fam = self.focus({"tasks": ["chrome-over-canvas"]})
        self.assertIn("chrome_over_canvas_resumed", fam)

    def test_add_and_remove_edit_the_list(self):
        self.focus({"tasks": ["enrich*"], "why": "owner"})
        self.ctx.tree = {"nodes": {"main": {}}}
        args = dict(task=[], add=None, remove=None, clear=False, why=None)
        with mock.patch.object(hz, "Ctx", return_value=self.ctx), \
             mock.patch.object(hz, "queue", return_value=[]), mock.patch("sys.stdout"):
            hz.cmd_focus(mock.Mock(**{**args, "add": ["surface-polish"]}))
            self.assertEqual(hz.focus_tasks(self.ctx), ["enrich*", "surface-polish"])
            hz.cmd_focus(mock.Mock(**{**args, "remove": ["enrich*"]}))
            self.assertEqual(hz.focus_tasks(self.ctx), ["surface-polish"])
        self.assertEqual(json.loads((self.ctx.dir / "focus.json").read_text())["why"], "owner")


class FactStaleness(unittest.TestCase):
    """obs 54: a reader on another branch is not evidence the tree moved."""

    def setUp(self):
        import subprocess
        self.repo = Path(tempfile.mkdtemp())
        g = lambda *a: subprocess.run(["git", *a], cwd=self.repo, check=True,
                                      capture_output=True, text=True).stdout.strip()
        g("init", "-q", "-b", "main")
        g("-c", "user.name=t", "-c", "user.email=t@t", "commit", "-q", "--allow-empty", "-m", "a")
        self.a = g("rev-parse", "HEAD")
        g("-c", "user.name=t", "-c", "user.email=t@t", "commit", "-q", "--allow-empty", "-m", "b")
        self.b = g("rev-parse", "HEAD")
        self.ctx = FakeCtx({"main": None})
        self.ctx.worktree = self.repo

    def test_relation_words(self):
        rel = lambda sha, head: hz.sha_relation(self.ctx, sha, head)
        self.assertEqual(rel(self.b, self.a), "is behind the measured commit")
        self.assertEqual(rel(self.a, self.b), "contains the measured commit")
        self.assertEqual(rel(self.a, self.a), "is the measured commit")

    def test_other_worktree_unmoved_is_fresh(self):
        o = {"sha": self.b, "worktree": str(self.repo)}
        reader = FakeCtx({"main": None})
        reader.worktree = Path(tempfile.mkdtemp())     # somewhere else, not a repo
        with mock.patch.object(hz, "sha_relation", return_value="x"):
            fresh, same_wt, _, _ = hz.fact_state(reader, o)
        self.assertTrue(fresh)
        self.assertFalse(same_wt)

    def test_measuring_tree_moved_is_stale(self):
        o = {"sha": self.a, "worktree": str(self.repo)}
        fresh, same_wt, _, _ = hz.fact_state(self.ctx, o)
        self.assertEqual((fresh, same_wt), (False, True))


class Occupancy(unittest.TestCase):
    def test_interactive_session_in_worktree_is_seen(self):
        # obs 4: the roster lists background sessions only.
        rows = [{"kind": "interactive", "sessionId": "i1", "cwd": "/w/sub", "pid": 1},
                {"kind": "interactive", "sessionId": "i2", "cwd": "/w2", "pid": 2},
                {"kind": "bg", "sessionId": "b1", "cwd": "/w", "pid": 3},
                {"kind": "interactive", "sessionId": "me", "cwd": "/w", "pid": 4}]
        with mock.patch.object(hz, "live_sessions", return_value=rows):
            self.assertEqual([r["sessionId"] for r in hz.interactive_in("/w", {"me"})],
                             ["i1"])


class QueueShape(unittest.TestCase):
    def test_preview_skips_shared_preamble(self):
        # obs 14: seven briefs opening alike previewed alike.
        pre = "ENRICH SEGMENT. Read plans/enrich first.\n"
        a = {"text": pre + "S1 identity table"}
        b = {"text": pre + "S2 status and memory"}
        self.assertEqual(hz.brief_preview(a, [a, b]), "S1 identity table")
        self.assertEqual(hz.brief_preview({"text": "only"}, []), "only")

    def test_new_brief_joins_the_back_of_an_ordered_queue(self):
        ctx = FakeCtx({"main": None})
        with mock.patch.object(hz, "queue", return_value=[{"seq": 0}, {"seq": 3}, {}]):
            self.assertEqual(hz.next_seq(ctx, "dev"), {"seq": 4})
        with mock.patch.object(hz, "queue", return_value=[{}, {}]):
            self.assertEqual(hz.next_seq(ctx, "dev"), {})


class Reorder(unittest.TestCase):
    def test_every_reorder_needs_a_reason(self):
        # obs 21: a lead reordering its own child gave no reason, and the
        # record could not take one afterwards.
        ctx = FakeCtx({"main": None, "dev": "main", "dev_1": "dev"})
        ctx.me = "dev"
        a = mock.Mock(order="b,a", node="dev_1", why=None)
        with mock.patch.object(hz, "Ctx", return_value=ctx), \
             self.assertRaises(SystemExit) as e:
            hz.cmd_queue(a)
        self.assertEqual(e.exception.code, hz.REFUSED)


class Reparent(unittest.TestCase):
    def test_moving_a_part_needs_move(self):
        # obs 45: --from on a revision silently moved the brief's lineage.
        ctx = FakeCtx({"main": None})
        b = {"from": "enrich-import-bib"}
        with self.assertRaises(SystemExit) as e:
            hz.reparent_check(ctx, "s5-live", b, "enrich-keyed-via-cli", False)
        self.assertEqual(e.exception.code, hz.REFUSED)
        # same parent, spelled differently: not a move
        hz.reparent_check(ctx, "s5-live", b, "enrich_import_bib", False)
        with mock.patch.object(hz, "segment_count", return_value=(3, 4)), \
             mock.patch.object(hz, "task_state", return_value="open"):
            hz.reparent_check(ctx, "s5-live", b, "enrich-keyed-via-cli", True)


class Requeue(unittest.TestCase):
    def test_abandoned_task_returns_after_the_named_one(self):
        # obs 52: abandoning to put another task first dropped it from the queue.
        ctx = FakeCtx({"main": None, "dev": "main"})
        (ctx.dir / "briefs").mkdir()
        for i, t in enumerate(["a", "b", "c"]):
            (ctx.dir / "briefs" / f"{t}.json").write_text(json.dumps(
                {"task": t, "node": "dev", "seq": i}))
        (ctx.dir / "marks").mkdir()
        mf = ctx.dir / "marks" / "b.json"
        mf.write_text(json.dumps({"_node": "dev", "_abandoned_at": "x", "_closed_at": "x"}))
        self.assertEqual([b["task"] for b in hz.queue(ctx, "dev")], ["a", "c"])
        hz.requeue_after(ctx, mf, "dev", "b", "c", "dev", "pmc first")
        self.assertEqual([b["task"] for b in hz.queue(ctx, "dev")], ["a", "c", "b"])
        self.assertFalse(mf.exists())
        self.assertEqual(len(list((ctx.dir / "marks" / "parked").glob("b-*.json"))), 1)


class Baseline(unittest.TestCase):
    """obs 42: a check red at every commit says nothing; compare with a baseline."""

    def test_failed_files(self):
        self.assertEqual(hz.failed_files("x\nfailed: b.py(1) a.py(2)\nran 3"), ["a.py", "b.py"])
        self.assertEqual(hz.failed_files("failed: none\n"), [])
        self.assertIsNone(hz.failed_files("FAIL somewhere\n"))
        self.assertEqual(hz.failed_files("failed: a.py\n...\nfailed: c.py(1)"), ["c.py"])

    def test_diff_new_gone_same_whole_arm_and_not_run(self):
        base = {"arms": {"a": {"failed": True, "files": ["x.py", "y.py"]},
                         "b": {"failed": True, "files": None},
                         "c": {"failed": False, "files": []}}}
        rows = [{"name": "a", "exit": 1, "failedFiles": ["y.py", "z.py"]},
                {"name": "b", "exit": 1, "failedFiles": None},
                {"name": "c", "exit": 124, "timedOut": True},
                {"name": "d", "exit": 1, "failedFiles": ["q.py"]}]
        d = hz.baseline_diff(rows, base)
        self.assertEqual((d["a"]["new"], d["a"]["gone"], d["a"]["same"]), (["z.py"], ["x.py"], 1))
        self.assertEqual((d["b"]["new"], d["b"]["same"]), ([], 1))
        self.assertTrue(d["c"]["notrun"])
        self.assertEqual(d["d"]["new"], ["q.py"])

    def run_check(self, command):
        ctx = FakeCtx({"main": None, "dev": "main"})
        ctx.me, ctx.branch, ctx.worktree = "dev", "dev", ctx.dir
        (ctx.dir / "checks").mkdir()
        hz.baseline_path(ctx).write_text(json.dumps(
            {"sha": "b" * 40, "arms": {"arm": {"failed": True, "files": ["a.py"]}}}))
        a = mock.Mock(set_baseline=False, timeout=30)
        chk = [{"name": "arm", "command": command, "blindSpot": "-"}]
        with mock.patch.object(hz, "Ctx", return_value=ctx), \
             mock.patch.object(hz, "load_checks", return_value=chk), \
             mock.patch("sys.stdout"):
            return hz.cmd_check(a)

    def test_known_reds_pass_and_a_new_red_refuses(self):
        self.assertIsNone(self.run_check("echo 'failed: a.py(1)'; exit 1"))
        with self.assertRaises(SystemExit) as e:
            self.run_check("echo 'failed: a.py(1) b.py(1)'; exit 1")
        self.assertEqual(e.exception.code, hz.REFUSED)


class Pairs(unittest.TestCase):
    """obs 25, 47: document pairs travel as data and apply all-or-nothing."""

    DOC = "# Schema\n\nFive serve the record object.\nindex position_cluster_by_level ddl=92a\nend\n"

    def setUp(self):
        import os
        import subprocess
        self.env = mock.patch.dict(os.environ, {
            "GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": "t@t",
            "GIT_COMMITTER_NAME": "t", "GIT_COMMITTER_EMAIL": "t@t"})
        self.env.start()
        self.addCleanup(self.env.stop)
        self.repo = Path(tempfile.mkdtemp())
        self.g = lambda *a: subprocess.run(["git", *a], cwd=self.repo, check=True,
                                           capture_output=True, text=True).stdout.strip()
        self.g("init", "-q", "-b", "main")
        (self.repo / "SCHEMA.md").write_text(self.DOC)
        self.g("add", ".")
        self.g("commit", "-q", "-m", "doc")
        self.ctx = FakeCtx({"main": None, "dev": "main"})
        self.ctx.tree["nodes"]["main"].update(kind="doc", branch="main")
        self.ctx.repo = self.ctx.worktree = self.repo

    def run_cmd(self, verb, target=None, task=None, me="dev"):
        self.ctx.me = me
        with mock.patch.object(hz, "Ctx", return_value=self.ctx), mock.patch("sys.stdout"):
            return hz.cmd_pairs(mock.Mock(verb=verb, target=target, task=task))

    def pairs(self, *p):
        return json.dumps([{"file": "SCHEMA.md", "old": o, "new": n, "why": "w"} for o, n in p])

    def test_submit_refuses_zero_and_two(self):
        rows, _ = hz.pair_report(json.loads(self.pairs(
            ("index position_cluster_by_level\n", "x\n"))), lambda f: self.DOC)
        self.assertEqual(rows[0][2], 0)          # obs 25: the decayed anchor
        self.assertIn("ddl=92a", rows[0][3])     # nearest line names the real one
        with self.assertRaises(SystemExit):
            self.run_cmd("submit", self.pairs(("e", "E")), task="t")   # 'e' occurs many times

    def test_apply_is_all_or_nothing_and_one_commit(self):
        self.run_cmd("submit", self.pairs(("Five serve", "Six serve"), ("end\n", "fin\n")), task="t")
        before = self.g("rev-list", "--count", "HEAD")
        self.run_cmd("apply", "t", me="main")
        self.assertEqual(int(self.g("rev-list", "--count", "HEAD")), int(before) + 1)
        self.assertIn("Task: t", self.g("log", "-1", "--format=%B"))
        self.assertIn("Six serve", (self.repo / "SCHEMA.md").read_text())

    def test_decayed_batch_applies_nothing(self):
        self.run_cmd("submit", self.pairs(("Five serve", "Six serve"), ("end\n", "fin\n")), task="t")
        (self.repo / "SCHEMA.md").write_text(self.DOC.replace("end\n", "END\n"))
        self.g("commit", "-qam", "moved")
        with self.assertRaises(SystemExit):
            self.run_cmd("apply", "t", me="main")
        self.assertIn("Five serve", (self.repo / "SCHEMA.md").read_text())

    def test_only_the_document_node_applies(self):
        self.run_cmd("submit", self.pairs(("Five serve", "Six serve")), task="t")
        with self.assertRaises(SystemExit):
            self.run_cmd("apply", "t", me="dev")


class After(unittest.TestCase):
    """obs 15, 59: a brief can wait on another task, and every path obeys it."""

    def setUp(self):
        self.ctx = FakeCtx({"main": None, "dev": "main", "dev_1": "dev", "dev_2": "dev"})
        for d in ("briefs", "marks", "blocks"):
            (self.ctx.dir / d).mkdir()

    def brief(self, task, node="dev_1", **kw):
        (self.ctx.dir / "briefs" / f"{hz.tkey(task)}.json").write_text(
            json.dumps({"task": task, "node": node, **kw}))

    def mark(self, task, node="dev_2", **kw):
        (self.ctx.dir / "marks" / f"{hz.tkey(task)}.json").write_text(
            json.dumps({"_node": node, **kw}))

    def test_waits_until_signed_off(self):
        self.brief("ledger", node="dev_2")
        self.brief("edges", after=["ledger"])
        self.mark("ledger")
        self.assertEqual(hz.waits_on(self.ctx, {"after": ["ledger"]}),
                         ["after ledger (open on dev_2)"])
        self.mark("ledger", _closed_at="x")
        self.assertEqual(hz.waits_on(self.ctx, {"after": ["ledger"]}), [])

    def test_abandoned_still_waits_and_superseded_follows_replacement(self):
        self.mark("ledger", _closed_at="x", _abandoned_at="x")
        self.assertTrue(hz.waits_on(self.ctx, {"after": ["ledger"]}))
        self.brief("old", superseded_at="x", superseded_for="new")
        self.brief("new")
        self.mark("new")
        self.assertIn("after new", hz.waits_on(self.ctx, {"after": ["old"]})[0])

    def test_open_decision_waits(self):
        (self.ctx.dir / "blocks" / "main_embed_model.json").write_text(json.dumps({"need": "q"}))
        self.assertEqual(hz.waits_on(self.ctx, {"gated_by": "embed-model"}),
                         ["decision embed-model is open"])

    def test_startable_and_next_after_skip_waiting(self):
        self.brief("ledger", node="dev_2")
        self.mark("ledger")
        self.brief("edges", after=["ledger"], seq=0)
        self.brief("polish", seq=1)
        self.assertEqual([b["task"] for b in hz.startable(self.ctx, "dev_1")], ["polish"])
        self.assertEqual(hz.next_after(self.ctx, "dev_1", "x")[0]["task"], "polish")
        self.mark("polish", node="dev_1")
        self.assertIsNone(hz.next_after(self.ctx, "dev_1", "x")[0])

    def test_cycle_refused(self):
        self.brief("a", after=["b"])
        self.brief("b", after=["c"])
        self.assertTrue(hz.after_cycle(self.ctx, "c", ["a"]))
        self.assertFalse(hz.after_cycle(self.ctx, "d", ["a"]))

    def test_mark_refuses_a_waiting_brief(self):
        import os
        self.brief("ledger", node="dev_2")
        self.mark("ledger")
        self.brief("edges", after=["ledger"])
        self.ctx.me = "dev_1"
        with mock.patch.object(hz, "Ctx", return_value=self.ctx), \
             mock.patch.object(hz, "unreported", return_value=[]), \
             mock.patch.dict(os.environ, {"CLAUDE_CODE_SESSION_ID": "s" * 36}), \
             mock.patch("sys.argv", ["harness", "mark", "edges"]), \
             mock.patch("sys.stderr"), self.assertRaises(SystemExit) as e:
            hz.main()
        self.assertEqual(e.exception.code, hz.REFUSED)
        self.assertFalse((self.ctx.dir / "marks" / "edges.json").exists())


class LeadContext(unittest.TestCase):
    """obs 60: the harness meters a lead's context, sets compaction, and resets
    it at a quiet point."""

    def setUp(self):
        self.ctx = FakeCtx({"main": None, "dev": "main", "dev_1": "dev"})
        self.ctx.branch = "main"

    def test_context_size_reads_the_tail(self):
        t = self.ctx.dir / "t.jsonl"
        usage = lambda n: json.dumps({"message": {"usage": {
            "input_tokens": 1, "cache_read_input_tokens": n, "cache_creation_input_tokens": 9}}})
        t.write_text("\n".join([usage(5)] + ["x" * 200] * 50 + [usage(424000), "{}"]) + "\n")
        self.assertEqual(hz.context_size("s", t, tail=600), 424010)
        self.assertIsNone(hz.context_size("s", self.ctx.dir / "missing.jsonl"))

    def test_heavy_child_is_named_over_the_threshold_only(self):
        self.ctx.lock("dev", 1)
        def owes(size):
            with mock.patch.object(hz, "open_marks", return_value={}), \
                 mock.patch.object(hz, "queue", return_value=[]), \
                 mock.patch.object(hz, "holder_alive", return_value=True), \
                 mock.patch.object(hz, "context_size", return_value=size):
                return [o for o in hz.lead_owes(self.ctx, "main") if o[0] == "heavy"]
        self.assertEqual(owes(424000)[0][1:3], ("dev", "424k (warn 300k)"))
        self.assertEqual(owes(120000), [])

    def test_launch_sets_autocompact_by_rank_and_tree(self):
        cmd = hz.launch_cmd(self.ctx, "dev", "p-dev", [], "opus", "medium", "go")
        self.assertEqual(cmd[cmd.index("--autocompact") + 1], "350k")
        self.assertEqual(cmd[-1], "go")
        self.assertNotIn("--autocompact", hz.launch_cmd(self.ctx, "dev_1", "p", [], None, None, "go"))
        self.ctx.tree["nodes"]["dev"]["autocompact"] = "600k"
        cmd = hz.launch_cmd(self.ctx, "dev", "p-dev", [], None, None, "go")
        self.assertEqual(cmd[cmd.index("--autocompact") + 1], "600k")

    def test_reset_flushes_then_launches_at_a_quiet_turn_end(self):
        with mock.patch("sys.stdout"):
            hz.request_reset(self.ctx, ["dev"])
            with self.assertRaises(SystemExit):
                hz.request_reset(self.ctx, ["main"])          # rank 0 is never reset
        p = hz.reset_path(self.ctx, "dev")
        with mock.patch.object(hz, "launch_reset") as go, mock.patch("sys.stdout") as out:
            self.assertFalse(hz.reset_step(self.ctx, "dev", launch_only=True))  # no block yet
            self.assertTrue(hz.reset_step(self.ctx, "dev"))   # 1st turn end: flush
            self.assertIn("pending", "".join(c.args[0] for c in out.write.call_args_list))
            go.assert_not_called()
            with mock.patch.object(hz, "reset_quiet", return_value=False):
                self.assertFalse(hz.reset_step(self.ctx, "dev", launch_only=True))
            go.assert_not_called()
            with mock.patch.object(hz, "reset_quiet", return_value=True):
                self.assertTrue(hz.reset_step(self.ctx, "dev", launch_only=True))
            go.assert_called_once()
        self.assertFalse(p.exists())


class Records(unittest.TestCase):
    def test_author_is_not_told_of_own_comment(self):
        ctx = FakeCtx({"main": None, "dev": "main"})
        (ctx.dir / "briefs").mkdir()
        (ctx.dir / "briefs" / "t.json").write_text(json.dumps({
            "node": "dev", "comments": [{"at": "2026", "by": "main", "text": "x"}]}))
        self.assertEqual(hz.unread_brief_comments(ctx, "main"), {})

    def test_abandoned_part_is_not_settled(self):
        ctx = FakeCtx({"main": None})
        (ctx.dir / "marks").mkdir()
        (ctx.dir / "marks" / "p.json").write_text(json.dumps(
            {"_closed_at": "2026", "_abandoned_at": "2026"}))
        self.assertEqual(hz.task_state(ctx, "p"), "abandoned")


if __name__ == "__main__":
    unittest.main()
