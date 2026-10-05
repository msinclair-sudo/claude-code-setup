"""Liveness and nag rules. Run: python3 -m unittest discover harness/tests"""
import importlib.machinery
import importlib.util
import io
import json
import os
import socket
import tempfile
import time
import unittest
from contextlib import redirect_stdout
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
        chk = [{"name": "arm", "command": command, "blindSpot": "-"}]
        base = hz.load_baseline(ctx)
        with mock.patch("sys.stdout"):
            rows, failed = hz.run_arms(ctx, "dev", "c" * 40, ctx.dir, chk, base, 30, "r")
        return hz.check_exit(hz.make_check_report("dev", "c" * 40, rows, failed, base))

    def test_known_reds_pass_and_a_new_red_refuses(self):
        self.assertEqual(self.run_check("echo 'failed: a.py(1)'; exit 1"), 0)
        self.assertEqual(self.run_check("echo 'failed: a.py(1) b.py(1)'; exit 1"), hz.REFUSED)


class CheckVisible(unittest.TestCase):
    """obs 68, 69: a running check shows progress, and a timed-out arm keeps its output."""

    def setUp(self):
        self.ctx = FakeCtx({"main": None, "dev": "main"})
        self.ctx.me, self.ctx.branch, self.ctx.worktree = "dev", "dev", self.ctx.dir
        (self.ctx.dir / "checks").mkdir()

    def check(self, command, timeout=30, out=None, progress=None):
        chk = [{"name": "arm", "command": command, "blindSpot": "-"}]
        with mock.patch("sys.stdout", out or io.StringIO()):
            rows, _ = hz.run_arms(self.ctx, "dev", "c" * 40, self.ctx.dir, chk, None, timeout,
                                  "r", progress=progress)
        return rows[0]

    def test_timeout_keeps_what_it_printed(self):
        row = self.check("echo first; echo second; sleep 5", timeout=1)
        self.assertTrue(row["timedOut"])
        self.assertIn("second", row["stdout"])
        self.assertEqual(row["lastLine"], "second")
        self.assertIn("timed out after 1s", row["stderr"])
        self.assertIn("second", (self.ctx.dir / "checks" / "dev-arm.out").read_text())

    def test_progress_is_reported_before_each_arm(self):
        seen = []
        self.check("true", progress=lambda i, arm: seen.append((i, arm)))
        self.assertEqual(seen, [(0, "arm")])

    def test_clip_says_it_cut(self):
        self.assertEqual(hz.clip("x" * 105), "x" * 100 + "…(+5 chars)")
        self.assertEqual(hz.clip("short"), "short")


class WaitChain(unittest.TestCase):
    """obs 68: one reading of what a node is doing, and a stalled wait reaches the rank above."""

    def setUp(self):
        self.ctx = FakeCtx({"main": None, "dev": "main", "dev_2": "dev"})
        for d in ("waiting", "checks"):
            (self.ctx.dir / d).mkdir()

    def wait(self, since):
        hz.waiting_path(self.ctx, "dev_2").write_text(json.dumps(
            {"node": "dev_2", "parent": "dev", "asked": "ruling on X", "since": since}))

    def checking(self, pid):
        hz.testq_save(self.ctx, {"id": "j1", "kind": "check", "sha": "c" * 40, "state": "running",
                                 "requested_by": [{"node": "dev"}], "pid": pid, "total": 23,
                                 "done_arms": 6, "arm": "pytest-all", "started": OLD, "at": OLD})

    def test_activity(self):
        self.wait(OLD)
        self.assertTrue(hz.node_activity(self.ctx, "dev_2").startswith("waiting on dev 3h"))
        self.checking(os.getpid())
        self.assertEqual(hz.node_activity(self.ctx, "dev"), "check running arm 7/23, 3h00")
        with mock.patch.object(hz, "runner_alive", return_value=False):
            self.assertIn("check runner died", hz.node_activity(self.ctx, "dev"))

    def items(self, node):
        with mock.patch.object(hz, "lead_owes", return_value=[]), \
             mock.patch.object(hz, "rank0_owes", return_value=[]), \
             mock.patch.object(hz, "focus_family", return_value=None), \
             mock.patch.object(hz, "unread_brief_comments", return_value={}), \
             mock.patch.object(hz, "unactioned_briefs", return_value=[]), \
             mock.patch.object(hz, "open_marks", return_value={}), \
             mock.patch.object(hz, "queue", return_value=[]):
            return hz.queue_items(self.ctx, node)

    def test_stalled_wait_reaches_the_rank_above(self):
        self.wait(OLD)
        self.checking(os.getpid())
        main = self.items("main")
        self.assertIn("stuck:dev_2", main)
        self.assertIn("dev: check running arm 7/23", main["stuck:dev_2"])
        dev = self.items("dev")
        self.assertIn("asked:dev_2", dev)
        self.assertNotIn("stuck:dev_2", dev)
        self.wait(time.strftime("%Y-%m-%dT%H:%M:%S%z"))
        self.assertNotIn("stuck:dev_2", self.items("main"))


class CloseAfter(unittest.TestCase):
    """obs 67: a segment's close waits on a task, structurally."""

    def setUp(self):
        self.ctx = FakeCtx({"main": None, "dev": "main", "dev_1": "dev", "dev_2": "dev"})
        for d in ("briefs", "marks"):
            (self.ctx.dir / d).mkdir()
        self.w = lambda p, o: (self.ctx.dir / p).write_text(json.dumps(o))
        self.w("briefs/seg.json", {"task": "seg", "node": "dev", "close_after": ["later"],
                                   "close_after_by": "main"})
        self.w("briefs/p1.json", {"task": "p1", "node": "dev_1", "from": "seg"})
        self.w("marks/p1.json", {"_node": "dev_1", "_closed_at": "2026"})
        self.w("briefs/later.json", {"task": "later", "node": "dev_2"})

    def test_settled_parts_do_not_make_it_ready(self):
        (x,) = hz.delegated(self.ctx, "dev")
        self.assertFalse(x["ready"])
        self.assertTrue(x["held"][0].startswith("after later"))
        self.w("marks/later.json", {"_node": "dev_2", "_closed_at": "2026"})
        self.assertTrue(hz.delegated(self.ctx, "dev")[0]["ready"])

    def test_close_refuses_while_held(self):
        import argparse
        a = argparse.Namespace(task="seg", done=False, abandon=None, requeue_after=None,
                               close=True, force=False)
        with mock.patch.object(hz, "Ctx", return_value=self.ctx), \
             mock.patch.dict(os.environ, {"CLAUDE_CODE_SESSION_ID": "s"}), \
             mock.patch("sys.stderr", io.StringIO()) as err:
            with self.assertRaises(SystemExit) as e:
                hz.cmd_mark(a)
        self.assertEqual(e.exception.code, hz.REFUSED)
        self.assertIn("closes only after", err.getvalue())


class Hold(unittest.TestCase):
    """obs 66: a held resource stops the checks that read it."""

    def setUp(self):
        self.ctx = FakeCtx({"main": None, "dev": "main"})
        self.ctx.me, self.ctx.branch, self.ctx.worktree = "dev", "dev", self.ctx.dir
        for d in ("holds", "checks", "marks", "briefs"):
            (self.ctx.dir / d).mkdir()

    def test_matching(self):
        db = [{"path": "~/data/subset.db"}]
        self.assertTrue(hz.hold_catching({"command": "py t.py $HOME/data/subset.db"}, db))
        self.assertIsNone(hz.hold_catching({"command": "py t.py other.db"}, db))
        self.assertTrue(hz.hold_catching({"command": "x", "reads": ["~/data"]}, db))
        self.assertIsNone(hz.hold_catching({"command": "~/data/subset.db", "reads": ["/elsewhere"]}, db))

    def test_until_lifts_it(self):
        (self.ctx.dir / "holds" / "h.json").write_text(json.dumps(
            {"path": "/x", "why": "job", "by": "dev", "until": "job"}))
        (self.ctx.dir / "briefs" / "job.json").write_text(json.dumps({"task": "job", "node": "dev"}))
        self.assertEqual(len(hz.live_holds(self.ctx)), 1)
        (self.ctx.dir / "marks" / "job.json").write_text(json.dumps({"_node": "dev", "_closed_at": "x"}))
        self.assertEqual(hz.live_holds(self.ctx), [])

    def test_check_skips_a_held_arm(self):
        (self.ctx.dir / "holds" / "h.json").write_text(json.dumps(
            {"path": str(self.ctx.dir / "db"), "why": "live merge", "by": "dev", "until": ""}))
        touched = self.ctx.dir / "ran"
        chk = [{"name": "arm", "command": f"touch {touched}; cat {self.ctx.dir}/db", "blindSpot": "-"}]
        with mock.patch("sys.stdout", io.StringIO()):
            rows, failed = hz.run_arms(self.ctx, "dev", "c" * 40, self.ctx.dir, chk, None, 30, "r")
        rep = hz.make_check_report("dev", "c" * 40, rows, failed, None)
        self.assertFalse(touched.exists())
        self.assertEqual((rep["passed"], rep["held"]), (False, 1))
        self.assertIn("live merge", rep["checks"][0]["held"])


class ResetCeiling(unittest.TestCase):
    """obs 66 addendum: a pending reset fires past its ceiling even when never quiet."""

    def setUp(self):
        self.ctx = FakeCtx({"main": None, "dev": "main"})
        self.ctx.lock("dev", 1, ref="sid-dev")
        (self.ctx.dir / "resets").mkdir()

    def step(self, size, deadline):
        hz.reset_path(self.ctx, "dev").write_text(json.dumps(
            {"by": "main", "flushed": True, "by_tokens": 400_000, "deadline": deadline}))
        with mock.patch.object(hz, "reset_quiet", return_value=False), \
             mock.patch.object(hz, "context_size", return_value=size), \
             mock.patch.object(hz, "launch_reset") as launch:
            hz.reset_step(self.ctx, "dev")
        return launch.called

    def test_ceiling(self):
        later = time.time() + 3600
        self.assertFalse(self.step(300_000, later))
        self.assertTrue(self.step(410_000, later))
        self.assertTrue(self.step(300_000, time.time() - 1))

    def test_a_busy_lead_keeps_the_reset_pending(self):
        """obs 73: the record outlives a launch; a skip leaves it to retry."""
        self.assertTrue(self.step(410_000, time.time() + 3600))
        p = hz.reset_path(self.ctx, "dev")
        self.assertTrue(p.exists())
        with mock.patch.object(hz, "reset_quiet", return_value=False), \
             mock.patch.object(hz, "context_size", return_value=410_000), \
             mock.patch.object(hz, "launch_reset") as launch:
            self.assertFalse(hz.reset_step(self.ctx, "dev"))      # in flight: once
            hz.reset_outcome(self.ctx, "dev", "busy")
            self.assertTrue(json.loads(p.read_text())["skipped_at"])
            self.assertTrue(hz.reset_step(self.ctx, "dev"))       # retried
            self.assertEqual(launch.call_count, 1)
        hz.reset_outcome(self.ctx, "dev")
        self.assertFalse(p.exists())                              # gone on success

    def test_dry_run_writes_nothing_and_cancel_is_a_command(self):
        """obs 72."""
        p = hz.reset_path(self.ctx, "dev")
        self.ctx.branch = "main"
        self.ctx.tree["nodes"]["main"]["branch"] = "main"
        with mock.patch.object(hz, "context_limits", return_value=(300_000, None)), \
             redirect_stdout(io.StringIO()):
            hz.request_reset(self.ctx, ["dev"], dry_run=True)
            self.assertFalse(p.exists())
            hz.request_reset(self.ctx, ["dev"])
            self.assertTrue(p.exists())
            hz.request_reset(self.ctx, ["dev"], dry_run=True, cancel=True)
            self.assertTrue(p.exists())
            hz.request_reset(self.ctx, ["dev"], cancel=True)
            self.assertFalse(p.exists())


class Cited(unittest.TestCase):
    """obs 74: does an open record still need a path, before the owner deletes it."""

    def test_open_records_only_and_every_form(self):
        ctx = FakeCtx({"main": None})
        ctx.repo = Path("/r")
        home = str(Path.home())
        texts = [("brief open", f'{{"text": "replay from ~/data/backup-2026.db"}}'),
                 ("fact f", '{"command": "ls scratch/run.py"}')]
        with mock.patch.object(hz, "open_record_texts", return_value=texts), \
             mock.patch.object(hz, "load_index", return_value={"byWorktree": {"/r-dev": "dev"}}):
            got = hz.cited(ctx, [f"{home}/data/backup-2026.db", "/r-dev/scratch/run.py",
                                 "/elsewhere/backup-2026.db", f"{home}/data/other.bin"])
        self.assertEqual(got[f"{home}/data/backup-2026.db"], [("brief open", "names it")])
        self.assertEqual(got["/r-dev/scratch/run.py"], [("fact f", "names it")])
        self.assertEqual(got["/elsewhere/backup-2026.db"],
                         [("brief open", "names backup-2026.db")])     # by name: careful
        self.assertEqual(got[f"{home}/data/other.bin"], [])


class TimeGate(unittest.TestCase):
    """obs 70: a task can wait on a clock, read by every start path."""

    def setUp(self):
        self.ctx = FakeCtx({"main": None, "dev": "main", "dev_1": "dev"})
        (self.ctx.dir / "briefs").mkdir()

    def test_parse(self):
        import datetime as dt
        now = dt.datetime(2026, 10, 4, 23, 0, tzinfo=dt.timezone.utc).timestamp()
        self.assertEqual(hz.utc_label(hz.parse_utc("00:05Z", now)), "2026-10-05 00:05Z")
        self.assertEqual(hz.utc_label(hz.parse_utc("22:00Z", now)), "2026-10-05 22:00Z")
        self.assertEqual(hz.utc_label(hz.parse_utc("2026-10-06T01:30Z", now)), "2026-10-06 01:30Z")

    def test_waits_until_then_starts(self):
        b = {"task": "job", "node": "dev_1", "not_before": time.time() + 3600}
        (self.ctx.dir / "briefs" / "job.json").write_text(json.dumps(b))
        self.assertTrue(hz.waits_on(self.ctx, b)[0].startswith("until "))
        self.assertEqual(hz.startable(self.ctx, "dev_1"), [])
        b["not_before"] = time.time() - 1
        (self.ctx.dir / "briefs" / "job.json").write_text(json.dumps(b))
        self.assertEqual([x["task"] for x in hz.startable(self.ctx, "dev_1")], ["job"])


class Requires(unittest.TestCase):
    """obs 68/70: "X must be an ancestor" is checked at presenting, not at commit."""

    def setUp(self):
        import subprocess
        self.env = mock.patch.dict(os.environ, {
            "GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": "t@t",
            "GIT_COMMITTER_NAME": "t", "GIT_COMMITTER_EMAIL": "t@t",
            "CLAUDE_CODE_SESSION_ID": "sess"})
        self.env.start()
        self.addCleanup(self.env.stop)
        self.ctx = FakeCtx({"main": None, "dev": "main"})
        self.ctx.me = "dev"
        repo = self.ctx.dir / "repo"
        repo.mkdir()
        g = lambda *a: subprocess.run(["git", *a], cwd=repo, capture_output=True, text=True).stdout.strip()
        g("init", "-q", "-b", "dev")
        g("commit", "-q", "--allow-empty", "-m", "a")
        g("checkout", "-q", "-b", "main")
        g("commit", "-q", "--allow-empty", "-m", "ruling")
        self.ruling = g("rev-parse", "HEAD")
        g("checkout", "-q", "dev")
        self.g = g
        self.ctx.repo = self.ctx.worktree = repo
        for d in ("briefs", "marks"):
            (self.ctx.dir / d).mkdir()
        (self.ctx.dir / "briefs" / "t.json").write_text(json.dumps(
            {"task": "t", "node": "dev", "requires": [{"ref": "main", "sha": self.ruling}]}))
        (self.ctx.dir / "marks" / "t.json").write_text(json.dumps({"_node": "dev"}))

    def present(self):
        import argparse
        a = argparse.Namespace(task="t", done=True)
        err = io.StringIO()
        with mock.patch.object(hz, "Ctx", return_value=self.ctx), \
             mock.patch("sys.stderr", err), mock.patch("sys.stdout", io.StringIO()):
            try:
                hz.cmd_mark(a)
            except (SystemExit, AttributeError, Exception):
                pass
        return err.getvalue()

    def test_refused_until_head_contains_it(self):
        self.assertIn("requires main", self.present())
        self.g("merge", "-q", "--ff-only", "main")
        self.assertNotIn("requires main", self.present())


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
        self.assertTrue(p.exists())             # kept until the recycle succeeds (obs 73)
        hz.reset_outcome(self.ctx, "dev")
        self.assertFalse(p.exists())


class Sweep(unittest.TestCase):
    """The harness cleans up a completed unit, on rank 0's recorded decision."""

    A, B, L = "a" * 36, "b" * 36, "c" * 36

    def setUp(self):
        import gzip as gz
        self.gz = gz
        self.ctx = FakeCtx({"main": None, "dev": "main", "dev_1": "dev"})
        d = self.ctx.dir
        for k in ("briefs", "marks", "facts", "seen"):
            (d / k).mkdir()
        w = lambda p, o: (d / p).write_text(json.dumps(o))
        w("briefs/s1.json", {"task": "s1", "node": "dev"})
        w("briefs/s1a.json", {"task": "s1a", "node": "dev_1", "from": "s1", "history": [1]})
        w("briefs/s1b.json", {"task": "s1b", "node": "dev_1", "from": "s1"})
        w("marks/s1a.json", {"_node": "dev_1", "_session": self.A, "_closed_at": "x"})
        w("marks/s1b.json", {"_node": "dev_1", "_session": self.B, "_closed_at": "x"})
        w("marks/s1.json", {"_node": "dev", "_session": self.L, "_closed_at": "x"})
        self.proj = Path(tempfile.mkdtemp())
        (self.proj / "p").mkdir()
        for sid in (self.A, self.B, self.L):
            (self.proj / "p" / f"{sid}.jsonl").write_text('{"x": 1}\n' * 50)
        self.jobs = Path(tempfile.mkdtemp()) / ".claude" / "jobs"
        for sid in (self.A, self.B):
            jd = self.jobs / sid[:8]
            (jd / "tmp").mkdir(parents=True)
            (jd / "tmp" / "scratch.db").write_bytes(b"0" * 1000)
            (jd / "tmp" / "cd3.py").write_text("print(1)")
            (jd / "state.json").write_text(json.dumps({"sessionId": sid}))
        w("facts/r9.json", {"name": "r9", "observations": [
            {"value": "3", "command": f"ls {self.jobs / self.B[:8] / 'tmp'}", "by": "dev_1 (session x)"}]})
        (d / "seen" / "dead-session.json").write_text("{}")
        self.rm = mock.MagicMock(return_value=(True, ""))
        self.p = [mock.patch.object(hz, "PROJECTS", self.proj),
                  mock.patch.object(hz, "JOBS", self.jobs),
                  mock.patch.object(hz, "live_sessions", return_value=[]),
                  mock.patch.object(hz, "claude_rm", self.rm)]
        for x in self.p:
            x.start(); self.addCleanup(x.stop)

    def unit(self):
        units = hz.completed_units(self.ctx)
        self.assertEqual([u["name"] for u in units], ["s1"])
        return units[0]

    def test_only_a_closed_segment_is_a_unit(self):
        (self.ctx.dir / "marks" / "s1.json").write_text(json.dumps({"_node": "dev"}))
        self.assertEqual(hz.completed_units(self.ctx), [])

    def test_dry_run_selects_lanes_keeps_cited_and_changes_nothing(self):
        plan = hz.sweep_plan(self.ctx, self.unit())
        self.assertEqual(len(plan["transcripts"]), 2)                 # lanes, not the lead
        self.assertIn((self.L[:8], "a lead or rank 0"), plan["skipped"])
        self.assertEqual([Path(p).parent.name for p, _ in plan["tmp"]], [self.A[:8]])
        self.assertIn("cited by facts/r9", plan["kept"][0][1])         # B's tmp is cited whole
        self.assertTrue((self.proj / "p" / f"{self.A}.jsonl").exists())

    def test_sweep_archives_deletes_folds_and_ledgers(self):
        u = self.unit()
        plan = hz.sweep_plan(self.ctx, u)
        e = hz.run_sweep(self.ctx, u, plan, "s1 shipped", "main")
        src = self.proj / "p" / f"{self.A}.jsonl"
        self.assertFalse(src.exists())
        gzf = self.ctx.dir / "archive" / "s1" / "transcripts" / f"{self.A}.jsonl.gz"
        self.assertEqual(self.gz.decompress(gzf.read_bytes()), b'{"x": 1}\n' * 50)
        self.assertFalse((self.jobs / self.A[:8] / "tmp").exists())
        self.assertTrue((self.jobs / self.B[:8] / "tmp").exists())     # cited, kept
        self.assertFalse((self.ctx.dir / "briefs" / "s1a.json").exists())
        recs = json.loads((self.ctx.dir / "archive" / "s1" / "records.json").read_text())
        self.assertNotIn("history", recs["tasks"]["s1a"]["brief"])
        self.assertEqual(hz.task_state(self.ctx, "s1a"), "closed")     # still resolves
        self.assertEqual(hz.waits_on(self.ctx, {"after": ["s1a"]}), [])
        self.assertFalse((self.ctx.dir / "seen" / "dead-session.json").exists())
        self.assertEqual(hz.ledger(self.ctx)[0]["why"], "s1 shipped")
        self.assertEqual(e["counts"]["kept"], 1)
        self.assertEqual(hz.completed_units(self.ctx), [])              # not offered again
        # Off the session list: A, not B, whose job folder a fact cites.
        self.assertEqual([c.args[0] for c in self.rm.call_args_list], [self.A])
        self.assertEqual(e["sessions_removed"], [self.A[:8]])


class Findings(unittest.TestCase):
    """obs 57: a finding can be handed down, and closed as ruled."""

    def setUp(self):
        self.ctx = FakeCtx({"main": None, "dev": "main", "dev_1": "dev"})
        (self.ctx.dir / "findings").mkdir()
        self.f = self.ctx.dir / "findings" / "daily_cap.json"
        self.f.write_text(json.dumps({"name": "daily-cap", "to": "main", "from": "dev"}))

    def route(self, node, **kw):
        a = mock.Mock(name="daily-cap", to=kw.get("to"), ruled=kw.get("ruled"))
        a.name = "daily-cap"
        r = json.loads(self.f.read_text())
        with mock.patch("sys.stdout"):
            return hz.finding_route(self.ctx, node, node, a, r, self.f)

    def rec(self):
        return json.loads(self.f.read_text())

    def test_hand_down_only_to_own_child_by_the_addressee(self):
        with self.assertRaises(SystemExit):
            self.route("dev", to="dev_1")            # not the addressee
        with self.assertRaises(SystemExit):
            self.route("main", to="dev_1")           # not main's child
        self.route("main", to="dev")
        r = self.rec()
        self.assertEqual((r["to"], r["approved_by"]), ("dev", "main"))
        self.assertIn("daily_cap", hz.open_findings(self.ctx, "dev"))

    def test_ruled_closes_as_answered_not_declined(self):
        self.route("main", ruled="ENRICH-DESIGN 3fabdcb")
        r = self.rec()
        self.assertEqual(r["ruled_ref"], "ENRICH-DESIGN 3fabdcb")
        self.assertNotIn("dropped_at", r)
        self.assertEqual(hz.open_findings(self.ctx, "main"), {})
        with self.assertRaises(SystemExit):
            self.route("main", ruled="again")         # already closed


class Covers(unittest.TestCase):
    """obs 58: parts say which of the segment's numbered checks they cover."""

    TEXT = ("INTENT. Fetch references (2026 plan).\n"
            "CHECKS. (1) stubs have edges (2) idempotent (3) yardstick\n"
            "SEAMS. none (4) is not a clause here\n"
            "DONE. Presented with the three checks.")

    def setUp(self):
        self.ctx = FakeCtx({"main": None, "dev": "main", "dev_1": "dev"})
        for d in ("briefs", "marks"):
            (self.ctx.dir / d).mkdir()
        self.w = lambda t, o: (self.ctx.dir / "briefs" / f"{t}.json").write_text(json.dumps(o))
        self.w("s6", {"task": "s6", "node": "dev", "text": self.TEXT})

    def test_clauses_come_from_the_checks_paragraph(self):
        self.assertEqual(hz.brief_clauses(self.TEXT), {1, 2, 3})
        self.assertEqual(hz.brief_clauses("no numbers here"), set())
        # obs 71: markdown headings and list markers, as rank 0 writes them.
        self.assertEqual(hz.brief_clauses("## Done means\n1. a\n2) b\n## Notes\n3. no"),
                         {1, 2})

    def test_settled_parts_with_an_uncovered_clause_are_not_ready(self):
        self.w("s6a", {"task": "s6a", "node": "dev_1", "from": "s6", "covers": [2]})
        self.w("s6b", {"task": "s6b", "node": "dev_1", "from": "s6", "covers": [3]})
        for t in ("s6a", "s6b"):
            (self.ctx.dir / "marks" / f"{t}.json").write_text(json.dumps({"_closed_at": "x"}))
        x = hz.delegated(self.ctx, "dev")[0]
        self.assertEqual((x["done"], x["uncovered"], x["ready"]), (2, [1], False))
        self.w("s6c", {"task": "s6c", "node": "dev_1", "from": "s6", "covers": [1]})
        (self.ctx.dir / "marks" / "s6c.json").write_text(json.dumps({"_closed_at": "x"}))
        self.assertTrue(hz.delegated(self.ctx, "dev")[0]["ready"])

    def run_brief(self, *argv):
        import os
        (self.ctx.dir / "findings").mkdir(exist_ok=True)
        self.ctx.me, self.ctx.branch = "dev", "dev"
        self.ctx.worktree = self.ctx.repo = self.ctx.dir
        with mock.patch.object(hz, "Ctx", return_value=self.ctx), \
             mock.patch.dict(os.environ, {"CLAUDE_CODE_SESSION_ID": "s" * 36}), \
             mock.patch("sys.argv", ["harness", "brief", *argv]), \
             mock.patch("sys.stdout"), mock.patch("sys.stderr"):
            try:
                hz.main(); return 0
            except SystemExit as e:
                return e.code

    def test_brief_checks_covers_and_inherits_a_handed_down_approval(self):
        self.assertEqual(self.run_brief("s6a", "--for", "dev_1", "--from", "s6",
                                        "--covers", "9", "--write", "x"), hz.REFUSED)
        self.assertEqual(self.run_brief("s6a", "--for", "dev_1", "--from", "s6",
                                        "--covers", "1,3", "--write", "x"), 0)
        self.assertEqual(json.loads((self.ctx.dir / "briefs" / "s6a.json").read_text())["covers"],
                         [1, 3])
        (self.ctx.dir / "findings" / "cap.json").write_text(
            json.dumps({"name": "cap", "to": "dev", "from": "dev_1", "approved_by": "main"}))
        self.assertEqual(self.run_brief("capwork", "--for", "dev_1", "--from-finding", "cap",
                                        "--write", "x"), 0)
        ap = json.loads((self.ctx.dir / "briefs" / "capwork.json").read_text())["approval"]
        self.assertEqual((ap["state"], ap["decided_by"]), ("approved", "main"))

    def test_parts_without_covers_behave_as_before(self):
        self.w("s6a", {"task": "s6a", "node": "dev_1", "from": "s6"})
        (self.ctx.dir / "marks" / "s6a.json").write_text(json.dumps({"_closed_at": "x"}))
        x = hz.delegated(self.ctx, "dev")[0]
        self.assertEqual((x["uncovered"], x["ready"]), ([], True))


class Protection(Sweep):
    """obs 61: a sweep deleted a script a fact's --from ran; only paths protect,
    resolved through the author, and kept file by file."""

    def test_job_dir_var_resolves_through_the_author_and_keeps_one_file(self):
        (self.ctx.dir / "facts" / "nested.json").write_text(json.dumps({"name": "nested",
            "observations": [{"value": "1", "command": "python3 $CLAUDE_JOB_DIR/tmp/cd3.py",
                              "by": f"dev_1 (session {self.A[:8]})"}]}))
        u = self.unit()
        plan = hz.sweep_plan(self.ctx, u)
        tmp = str(self.jobs / self.A[:8] / "tmp")
        self.assertEqual(plan["tmp_keep"][tmp], ["cd3.py"])
        hz.run_sweep(self.ctx, u, plan, "w", "main")
        self.assertTrue((self.jobs / self.A[:8] / "tmp" / "cd3.py").exists())
        self.assertFalse((self.jobs / self.A[:8] / "tmp" / "scratch.db").exists())

    def test_the_units_own_note_protects_a_named_file(self):
        m = self.ctx.dir / "marks" / "s1a.json"
        r = json.loads(m.read_text())
        r["_comments"] = [{"by": f"dev_1 (session {self.A[:8]})", "text": "kept scratch.db for S2"}]
        m.write_text(json.dumps(r))
        plan = hz.sweep_plan(self.ctx, self.unit())
        self.assertEqual(plan["tmp_keep"][str(self.jobs / self.A[:8] / "tmp")], ["scratch.db"])

    def test_authorship_alone_protects_nothing(self):
        (self.ctx.dir / "findings").mkdir()
        (self.ctx.dir / "findings" / "x.json").write_text(json.dumps(
            {"name": "x", "by": f"dev_1 (session {self.A[:8]})", "what": "noticed a thing"}))
        plan = hz.sweep_plan(self.ctx, self.unit())
        self.assertEqual(plan["tmp_keep"][str(self.jobs / self.A[:8] / "tmp")], [])

    def test_gone_job_file_is_reported(self):
        o = {"command": "python3 $CLAUDE_JOB_DIR/tmp/gone.py", "by": f"x (session {self.A[:8]})"}
        with mock.patch.object(hz, "job_dirs", return_value={self.A[:8]: self.jobs / self.A[:8]}):
            self.assertEqual(len(hz.gone_job_files(o)), 1)
            o["command"] = "python3 $CLAUDE_JOB_DIR/tmp/cd3.py"
            self.assertEqual(hz.gone_job_files(o), [])


class Stale(unittest.TestCase):
    """Closed findings and old uncited facts fold into the archive on a decision."""

    def setUp(self):
        self.ctx = FakeCtx({"main": None, "dev": "main"})
        for d in ("facts", "findings", "briefs", "marks"):
            (self.ctx.dir / d).mkdir()
        w = lambda p, o: (self.ctx.dir / p).write_text(json.dumps(o))
        w("facts/old.json", {"name": "old", "observations": [{"at": "2026-09-01T00:00:00+1000", "value": 1}]})
        w("facts/cited.json", {"name": "cited", "observations": [{"at": "2026-09-01T00:00:00+1000", "value": 1}]})
        w("facts/fresh.json", {"name": "fresh", "observations": [{"at": time.strftime("%Y-%m-%dT%H:%M:%S%z"), "value": 1}]})
        w("briefs/t.json", {"task": "t", "node": "dev", "facts": ["cited"]})
        w("findings/dropped.json", {"name": "dropped", "to": "dev", "dropped_at": "x"})
        w("findings/open.json", {"name": "open", "to": "dev"})

    def test_rule(self):
        facts, finds = hz.stale_records(self.ctx, days=14)
        self.assertEqual(sorted(facts), ["old"])
        self.assertEqual(finds, {"dropped": "dropped"})

    def test_fold_keeps_them_readable(self):
        facts, finds = hz.stale_records(self.ctx, days=14)
        hz.fold_stale(self.ctx, facts, finds, "tidy", "main")
        self.assertFalse((self.ctx.dir / "facts" / "old.json").exists())
        self.assertEqual(hz.load_fact(self.ctx, "old")[1]["name"], "old")
        self.assertEqual(hz.archived_knowledge(self.ctx, "findings", "dropped")["name"], "dropped")
        self.assertEqual(hz.ledger(self.ctx)[-1]["counts"], {"facts": 1, "findings": 1})

    def test_nag_names_the_command_that_clears_it(self):
        """obs 65: the stale nag pointed at `sweep`, which only lists units."""
        rows = [r for r in hz.rank0_owes(self.ctx, "main") if r[0] == "sweep"]
        self.assertEqual([r[1:3] for r in rows], [("stale", "2 stale record(s)")])
        a = mock.Mock(stale=False, sessions=False, unit=None, all=True)
        out = io.StringIO()
        with mock.patch.object(hz, "Ctx", return_value=self.ctx), redirect_stdout(out):
            hz.cmd_sweep(a)
        self.assertIn("2 stale record(s) — harness sweep --stale", out.getvalue())


class Orphan(unittest.TestCase):
    """obs 63, 64: a session that died holding its task is work to resume, and
    its parent is told at once."""

    def setUp(self):
        self.ctx = FakeCtx({"main": None, "dev": "main", "dev_1": "dev"})
        for d in ("briefs", "marks"):
            (self.ctx.dir / d).mkdir()
        w = lambda p, o: (self.ctx.dir / p).write_text(json.dumps(o))
        w("marks/merge.json", {"_node": "dev_1"})                       # open, unpresented
        w("briefs/merge.json", {"task": "merge", "node": "dev_1"})
        w("briefs/runs.json", {"task": "runs", "node": "dev_1", "after": ["merge"]})

    def test_open_mark_is_resume_not_waiting(self):
        st = hz.next_start(self.ctx, "dev_1")
        self.assertEqual((st["skip"], st["line"].split()[:2]), (None, ["resumes", "merge"]))
        (self.ctx.dir / "marks" / "merge.json").write_text(
            json.dumps({"_node": "dev_1", "_presented_at": "x"}))
        self.assertIn("waits", hz.next_start(self.ctx, "dev_1")["skip"])

    def test_parent_is_told_when_the_holder_dies(self):
        self.ctx.lock("dev_1", 1)
        with mock.patch.object(hz, "holder_alive", return_value=False), \
             mock.patch.object(hz, "last_write", return_value=time.time() - 600):
            rows = hz.lead_owes(self.ctx, "dev")
            self.assertEqual([r[:3] for r in rows if r[0] == "orphan"], [("orphan", "dev_1", "merge")])
            self.ctx.lock("dev", 1)
            down = [r for r in hz.lead_owes(self.ctx, "main") if r[0] == "down"]
            self.assertEqual(down[0][1], "dev")                           # a dead lead too
        with mock.patch.object(hz, "holder_alive", return_value=False), \
             mock.patch.object(hz, "last_write", return_value=time.time() - 30):
            self.assertEqual([r for r in hz.lead_owes(self.ctx, "dev") if r[0] == "orphan"], [])


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


class Ask(unittest.TestCase):
    """T17: asks are opened by leads, briefed by the intermediary, signed by the owner."""

    BRIEF = ("## Question\nShip X or Y?\n## Background\nX ships the map.\n\nY waits a cycle.\n## Why yours\nintent: scope is the owner's\n"
             "## Checked\nbriefs/s1.json\n## Options\n- X: faster\n- Y: safer\n"
             "## Recommendation\nX (dev)\n## Waiting\nnothing")


    def test_id_not_reused_after_accept(self):
        d = Path(tempfile.mkdtemp())
        (d / "asks").mkdir(); (d / "briefs").mkdir()
        (d / "briefs" / "t.json").write_text(json.dumps({"task": "t", "rulings": [{"id": "t-1"}]}))
        self.assertEqual(hz.ask_next_id(d, "t"), "t-2")
    def setUp(self):
        self.ctx = FakeCtx({"main": None, "dev": "main", "dev_1": "dev"})
        (self.ctx.dir / "briefs").mkdir()
        self.bf = self.ctx.dir / "briefs" / "s1.json"
        self.bf.write_text(json.dumps({"task": "s1", "node": "dev_1", "text": "do it"}))
        self.err = mock.patch("sys.stderr", new_callable=io.StringIO)
        self.err.start()
        self.addCleanup(self.err.stop)

    def open(self, me="dev", sid="s" * 36, task="s1"):
        return hz.ask_open(self.ctx, task, "intent", "Ship X or Y?", me, sid)

    def path(self, rec):
        return self.ctx.dir / "asks" / f"{rec['id']}.json"

    def test_lead_opens_member_refused_brief_required(self):
        r = self.open()
        self.assertEqual((r["id"], r["state"], r["node"]), ("s1-1", "asked", "dev_1"))
        self.assertEqual(self.open(me="main")["id"], "s1-2")
        with self.assertRaises(SystemExit):
            self.open(me="dev_1")                       # a lane, in a session
        self.assertEqual(self.open(me="dev_1", sid="")["asked_by"], "dev_1 (operator)")
        with self.assertRaises(SystemExit):
            self.open(task="nope")                      # no brief
        with self.assertRaises(SystemExit):
            hz.ask_open(self.ctx, "s1", "intent", "x" * 201, "dev", "")

    def test_brief_validation_names_every_section(self):
        b, errs = hz.parse_ask_brief(self.BRIEF)
        self.assertEqual(errs, [])
        self.assertEqual(b["options"], ["X: faster", "Y: safer"])
        _, errs = hz.parse_ask_brief(self.BRIEF.replace("## Waiting\nnothing", ""))
        self.assertEqual(errs, ["waiting: missing"])
        self.assertEqual(b["background"], "X ships the map.\n\nY waits a cycle.")
        bad = (self.BRIEF.replace("Ship X or Y?", "q" * 350)
               .replace("- Y: safer", "")
               .replace("briefs/s1.json", "\n".join("l" * 3 for _ in range(13))))
        _, errs = hz.parse_ask_brief(bad)
        self.assertIn("question: 350 chars, cap 300", errs)
        self.assertIn("checked: 13 lines, cap 12", errs)
        self.assertIn("options: 1 item(s), need 2–5", errs)
        _, errs = hz.parse_ask_brief(self.BRIEF.replace("X: faster", "x" * 501))
        self.assertEqual(errs, ["options #1: 501 chars, cap 500"])

    def test_draft_needs_ready_and_accept_attaches(self):
        r = self.open()
        with self.assertRaises(SystemExit):
            hz.ask_draft(self.path(r), r, "Ship X")
        with self.assertRaises(SystemExit):
            hz.ask_accept(self.ctx.dir, self.path(r), r)
        hz.ask_set_brief(self.path(r), r, self.BRIEF)
        hz.ask_draft(self.path(r), r, "Ship X")
        out = hz.ask_accept(self.ctx.dir, self.path(r), r)
        self.assertFalse(self.path(r).exists())
        rs = json.loads(self.bf.read_text())["rulings"]
        self.assertEqual((rs[0]["id"], rs[0]["answer"], rs[0]["asker_node"]),
                         ("s1-1", "Ship X", "dev"))
        self.assertEqual(out["question"], "Ship X or Y?")

    def run_cli(self, argv, env):
        import os
        with mock.patch.object(hz, "HOME_STATE", self.home), \
             mock.patch.dict(os.environ, env), \
             mock.patch("sys.argv", ["harness", *argv]), \
             redirect_stdout(io.StringIO()) as out:
            try:
                hz.main(); code = 0
            except SystemExit as e:
                code = e.code
        return code, out.getvalue()

    def two_projects(self):
        self.home = Path(tempfile.mkdtemp())
        for name in ("p1", "p2"):
            d = self.home / f"-x-{name}"
            (d / "asks").mkdir(parents=True)
            (d / "binding.json").write_text(json.dumps({"repo": f"/x/{name}"}))
            (d / "asks" / "t-1.json").write_text(json.dumps(
                {"id": "t-1", "task": "t", "state": "ready", "asked_at": OLD,
                 "question": f"q {name}"}))
        (self.home / "-x-p2" / "asks" / "u-1.json").write_text(json.dumps(
            {"id": "u-1", "task": "u", "state": "rejected", "at": OLD}))

    def test_list_json_across_projects_and_accept_refused_in_session(self):
        self.two_projects()
        code, out = self.run_cli(["ask", "--list", "--json"], {})
        rows = json.loads(out)
        self.assertEqual(code, 0)
        self.assertEqual(sorted((r["project"], r["slug"]) for r in rows),
                         [("p1", "-x-p1"), ("p2", "-x-p2")])
        code, _ = self.run_cli(["ask", "t-1", "--accept"], {"CLAUDE_CODE_SESSION_ID": "s" * 36})
        self.assertEqual(code, hz.REFUSED)
        code, _ = self.run_cli(["ask", "t-1", "--draft", "x"], {"HARNESS_INTERMEDIARY": "0"})
        self.assertEqual(code, hz.REFUSED)
        import os
        env = {k: v for k, v in os.environ.items() if k != "CLAUDE_CODE_SESSION_ID"}
        with mock.patch.dict(os.environ, env, clear=True):
            code, _ = self.run_cli(["ask", "t-1", "--reject"], {})
        self.assertEqual(code, hz.REFUSED)                          # ambiguous id
        with mock.patch.dict(os.environ, env, clear=True):
            code, _ = self.run_cli(["ask", "t-1", "--reject", "--project", "p1"], {})
        self.assertEqual(code, 0)
        self.assertEqual(json.loads((self.home / "-x-p1" / "asks" / "t-1.json")
                                    .read_text())["state"], "rejected")

    def items(self, node):
        with mock.patch.object(hz, "lead_owes", return_value=[]), \
             mock.patch.object(hz, "rank0_owes", return_value=[]), \
             mock.patch.object(hz, "open_waits", return_value={}), \
             mock.patch.object(hz, "focus_family", return_value=None), \
             mock.patch.object(hz, "unread_brief_comments", return_value={}), \
             mock.patch.object(hz, "unactioned_briefs", return_value=[]), \
             mock.patch.object(hz, "open_marks", return_value={}), \
             mock.patch.object(hz, "queue", return_value=[]):
            return hz.queue_items(self.ctx, node), hz.delta(self.ctx, node, "sid-" + node)

    def test_reject_is_told_once_to_the_asker(self):
        r = self.open()
        hz.ask_reject(self.path(r), r)
        self.assertNotIn("rejected:s1-1", self.items("main")[0])
        now, (lines, ids) = self.items("dev")
        self.assertIn("rejected:s1-1", now)
        self.assertIn("rejected:s1-1", ids)
        self.assertFalse(self.path(r).exists())          # told, so gone
        self.assertNotIn("rejected:s1-1", self.items("dev")[0])

    def test_ruled_reaches_lead_and_asker_until_read(self):
        r = self.open(me="main")
        hz.ask_set_brief(self.path(r), r, self.BRIEF)
        hz.ask_draft(self.path(r), r, "Ship X")
        hz.ask_accept(self.ctx.dir, self.path(r), r)
        self.assertIn("ruled:s1:s1-1", self.items("dev")[0])       # the task's lead
        self.assertIn("ruled:s1:s1-1", self.items("main")[0])      # the asker
        self.assertNotIn("ruled:s1:s1-1", self.items("dev_1")[0])
        b = json.loads(self.bf.read_text())
        b["read"] = {"dev": time.strftime("%Y-%m-%dT%H:%M:%S%z",
                                          time.localtime(time.time() + 5))}
        self.bf.write_text(json.dumps(b))
        self.assertNotIn("ruled:s1:s1-1", self.items("dev")[0])

    def test_rewrite_keeps_rulings_and_read(self):
        import os
        self.bf.write_text(json.dumps({"task": "s1", "node": "dev_1", "text": "do it",
                                       "revision": 1, "rulings": [{"id": "s1-1"}],
                                       "read": {"dev": OLD}}))
        self.ctx.me, self.ctx.branch = "dev", "dev"
        self.ctx.worktree = self.ctx.repo = self.ctx.dir
        with mock.patch.object(hz, "Ctx", return_value=self.ctx), \
             mock.patch.dict(os.environ, {"CLAUDE_CODE_SESSION_ID": "s" * 36}), \
             mock.patch("sys.argv", ["harness", "brief", "s1", "--write", "redo it"]), \
             mock.patch("sys.stdout"):
            hz.main()
        b = json.loads(self.bf.read_text())
        self.assertEqual((b["text"], b["rulings"], b["read"]),
                         ("redo it", [{"id": "s1-1"}], {"dev": OLD}))


class Intermediary(unittest.TestCase):
    """T17: one intermediary per project, its reach that project only."""

    def setUp(self):
        self.err = mock.patch("sys.stderr", new_callable=io.StringIO)
        self.stderr = self.err.start()
        self.addCleanup(self.err.stop)
        self.home = Path(tempfile.mkdtemp())
        self.root = Path(tempfile.mkdtemp())
        self.pd = {}
        for name in ("alpha", "beta"):
            repo, wt, grant = (self.root / name, self.root / f"{name}-dev",
                               self.root / f"{name}-data")
            for d in (repo, wt, grant):
                d.mkdir()
            pdir = self.home / hz.slug(repo)
            (pdir / "asks").mkdir(parents=True)
            (pdir / "binding.json").write_text(json.dumps({"repo": str(repo)}))
            (pdir / "index.json").write_text(json.dumps(
                {"nodes": {"dev": {"worktree": str(wt)}}}))
            (pdir / "grants.json").write_text(json.dumps(
                {"nodes": {"dev": [{"path": str(grant)}]}}))
            (pdir / "asks" / "t-1.json").write_text(json.dumps(
                {"id": "t-1", "task": "t", "state": "ready", "asked_at": OLD}))
            self.pd[name] = (pdir, repo)
        (self.pd["beta"][0] / "asks" / "u-1.json").write_text(json.dumps(
            {"id": "u-1", "task": "u", "state": "ready", "asked_at": OLD}))
        for m in (mock.patch.object(hz, "HOME_STATE", self.home),
                  mock.patch.object(hz, "intermediary_prompt",
                                    side_effect=lambda pd: Path(pd) / "intermediary" / "prompt.md")):
            m.start()
            self.addCleanup(m.stop)

    def test_name_is_per_project(self):
        self.assertEqual(hz.intermediary_name("/x/y/biblion2"), "harness-intermediary-biblion2")
        self.assertEqual(hz.intermediary_name(Path("/x/y/biblion2/")),
                         "harness-intermediary-biblion2")

    def test_cmd_reaches_its_project_only(self):
        pdir, repo = self.pd["alpha"]
        cmd = hz.intermediary_cmd(pdir, str(repo))
        line = " ".join(cmd)
        dirs = cmd[cmd.index("--add-dir") + 1:cmd.index("--tools")]
        self.assertEqual(cmd[cmd.index("-n") + 1], "harness-intermediary-alpha")
        self.assertEqual(dirs[:4], [str(pdir), str(repo), str(self.root / "alpha-dev"),
                                    str(self.root / "alpha-data")])
        self.assertNotIn(str(self.home), dirs)                 # not every project's state
        self.assertNotIn("beta", line)
        self.assertIn(f"Bash(git -C {repo} log *)", cmd)
        self.assertNotIn(f"Bash(git -C {self.root / 'alpha-data'} log *)", cmd)  # grant: read only
        self.assertIn("intermediary for alpha", cmd[-1])

    def test_project_resolves_by_name_or_slug_and_refuses_otherwise(self):
        pdir, repo = self.pd["beta"]
        self.assertEqual(hz.intermediary_project("beta"), (pdir, str(repo)))
        self.assertEqual(hz.intermediary_project(pdir.name), (pdir, str(repo)))
        with self.assertRaises(SystemExit):
            hz.intermediary_project("gamma")
        with mock.patch.object(hz, "git", return_value=(128, "", "not a git repo")):
            with self.assertRaises(SystemExit):
                hz.intermediary_project()
        with mock.patch.object(hz, "git", return_value=(0, str(repo / ".git"), "")):
            self.assertEqual(hz.intermediary_project(), (pdir, str(repo)))

    def test_bound_intermediary_finds_and_lists_its_project_only(self):
        a, b = self.pd["alpha"][0], self.pd["beta"][0]
        with mock.patch.dict(os.environ, {"HARNESS_PROJECT": a.name}):
            self.assertEqual(hz.ask_find("t-1")[0], a)            # no longer ambiguous
            with self.assertRaises(SystemExit):
                hz.ask_find("u-1")                                # beta's
            self.assertIn("not in alpha", self.stderr.getvalue())
            self.assertEqual({r["project"] for r in hz.ask_list()}, {"alpha"})
            self.assertEqual({r["project"] for r in hz.ask_list(True)}, {"alpha", "beta"})
        with mock.patch.dict(os.environ, {"HARNESS_PROJECT": "-nowhere"}):
            with self.assertRaises(SystemExit):
                hz.ask_list()
        env = {k: v for k, v in os.environ.items() if k != "HARNESS_PROJECT"}
        with mock.patch.dict(os.environ, env, clear=True):
            self.assertEqual(hz.ask_find("u-1")[0], b)
            with self.assertRaises(SystemExit):
                hz.ask_find("t-1")                                # in both

    def test_gui_reports_each_projects_own(self):
        gp = Path(__file__).resolve().parents[1] / "bin" / "harness-gui"
        ld = importlib.machinery.SourceFileLoader("harness_gui", str(gp))
        gui = importlib.util.module_from_spec(importlib.util.spec_from_loader("harness_gui", ld))
        ld.exec_module(gui)
        self.assertIsNone(gui.intermediary(None, "/x/alpha")["running"])
        rows = [{"name": "harness-intermediary-alpha-t-1", "status": "idle", "sessionId": "s" * 36}]
        asks = [{"id": "t-1"}, {"id": "t-2"}]
        pdir = Path(tempfile.mkdtemp())
        (pdir / "intermediary" / "t-2").mkdir(parents=True)
        (pdir / "intermediary" / "t-2" / "inbox.jsonl").write_text("{}\n")
        with mock.patch.object(gui.CLI, "last_turn", return_value=(120, 5000)):
            a = gui.intermediary(rows, "/x/alpha", asks, pdir)
        self.assertEqual((a["running"], a["items"]), (1, ["t-1"]))
        self.assertEqual((asks[0]["session"]["state"], asks[0]["session"]["idle"],
                          asks[1]["session"]["state"]), ("idle", 120, "queued"))
        self.assertEqual(gui.intermediary(rows, "/x/beta", [])["running"], 0)


class AskEvidence(unittest.TestCase):
    """T17: evidence attached to an ask is copied in, served whitelisted, and
    goes when the ask does."""

    def setUp(self):
        self.ctx = FakeCtx({"main": None, "dev": "main", "dev_1": "dev"})
        (self.ctx.dir / "briefs").mkdir()
        (self.ctx.dir / "briefs" / "s1.json").write_text(
            json.dumps({"task": "s1", "node": "dev_1", "text": "do it"}))
        self.err = mock.patch("sys.stderr", new_callable=io.StringIO)
        self.err.start()
        self.addCleanup(self.err.stop)
        self.src = Path(tempfile.mkdtemp())
        self.png = self.src / "shot one.PNG"
        self.png.write_bytes(b"\x89PNG\r\n\x1a\n" + b"x" * 100)
        self.diff = self.src / "route.diff"
        self.diff.write_text("--- a\n+++ b\n")

    def open(self):
        r = hz.ask_open(self.ctx, "s1", "intent", "Ship X or Y?", "dev", "")
        return self.ctx.dir / "asks" / f"{r['id']}.json", r

    def test_attach_copies_and_records(self):
        p, r = self.open()
        e = hz.ask_attach(p, r, str(self.png), "the overlap")
        self.assertEqual((e["file"], e["name"], e["kind"], e["bytes"], e["caption"]),
                         ("1-shot_one.png", "shot one.PNG", "image", 108, "the overlap"))
        f = self.ctx.dir / "asks" / "evidence" / r["id"] / "1-shot_one.png"
        self.assertEqual(f.read_bytes(), self.png.read_bytes())
        self.assertTrue(self.png.exists())                    # copied, not moved
        hz.ask_attach(p, r, str(self.diff))
        rec = json.loads(p.read_text())
        self.assertEqual([x["kind"] for x in rec["evidence"]], ["image", "text"])
        self.assertIn("attached route.diff", rec["history"][-1]["what"])

    def test_bad_extension_missing_dir_and_caption_refused(self):
        p, r = self.open()
        bad = self.src / "x.exe"; bad.write_bytes(b"MZ")
        for args in ((str(bad),), (str(self.src / "nope.png"),), (str(self.src),),
                     (str(self.png), "c" * 301)):
            with self.assertRaises(SystemExit):
                hz.ask_attach(p, r, *args)
        self.assertFalse((self.ctx.dir / "asks" / "evidence").exists())

    def test_oversize_refused(self):
        p, r = self.open()
        with mock.patch.dict(hz.EVIDENCE_CAP, {"image": 50}):
            with self.assertRaises(SystemExit):
                hz.ask_attach(p, r, str(self.png))
        with mock.patch.object(hz, "EVIDENCE_MAX", 1):
            hz.ask_attach(p, r, str(self.diff))
            with self.assertRaises(SystemExit):
                hz.ask_attach(p, r, str(self.diff))

    def test_drop_removes_file_and_never_reuses_a_name(self):
        p, r = self.open()
        hz.ask_attach(p, r, str(self.png)); hz.ask_attach(p, r, str(self.diff))
        d = self.ctx.dir / "asks" / "evidence" / r["id"]
        hz.ask_drop_evidence(p, r, 2)
        self.assertFalse((d / "2-route.diff").exists())
        with self.assertRaises(SystemExit):
            hz.ask_drop_evidence(p, r, 2)
        self.assertEqual(hz.ask_attach(p, r, str(self.diff))["file"], "3-route.diff")
        self.assertEqual([e["file"] for e in json.loads(p.read_text())["evidence"]],
                         ["1-shot_one.png", "3-route.diff"])

    def test_accept_reject_return_delete_the_evidence(self):
        for end in ("accept", "reject", "return"):
            p, r = self.open()
            hz.ask_attach(p, r, str(self.png))
            d = self.ctx.dir / "asks" / "evidence" / r["id"]
            self.assertTrue(d.is_dir())
            if end == "accept":
                hz.ask_set_brief(p, r, Ask.BRIEF)
                hz.ask_draft(p, r, "Ship X")
                hz.ask_accept(self.ctx.dir, p, r)
            elif end == "reject":
                hz.ask_reject(p, r)
            else:
                hz.ask_return(p, r, "a lead's call")
            self.assertFalse(d.exists(), end)

    def test_merge_moves_evidence_renumbered(self):
        p1, r1 = self.open()
        p2, r2 = self.open()
        hz.ask_attach(p2, r2, str(self.diff))
        hz.ask_attach(p1, r1, str(self.png), "cap")
        hz.ask_attach(p1, r1, str(self.diff))
        o = hz.ask_merge(p1, r1, r2["id"])
        ev = self.ctx.dir / "asks" / "evidence"
        self.assertEqual([(e["file"], e["caption"]) for e in o["evidence"]],
                         [("1-route.diff", None), ("2-shot_one.png", "cap"),
                          ("3-route.diff", None)])
        self.assertEqual(sorted(f.name for f in (ev / r2["id"]).iterdir()),
                         ["1-route.diff", "2-shot_one.png", "3-route.diff"])
        self.assertFalse((ev / r1["id"]).exists())

    def test_gui_serves_only_whitelisted_files(self):
        gp = Path(__file__).resolve().parents[1] / "bin" / "harness-gui"
        ld = importlib.machinery.SourceFileLoader("harness_gui", str(gp))
        gui = importlib.util.module_from_spec(importlib.util.spec_from_loader("harness_gui", ld))
        ld.exec_module(gui)
        home = Path(tempfile.mkdtemp())
        pdir = home / "-x-p"
        (pdir / "asks").mkdir(parents=True)
        (pdir / "binding.json").write_text("{}")
        (home / "secret.png").write_bytes(b"secret")
        p = pdir / "asks" / "t-1.json"
        r = {"id": "t-1", "state": "ready"}
        hz.ask_attach(p, r, str(self.png)); hz.ask_attach(p, r, str(self.diff))
        r["evidence"].append(dict(r["evidence"][0], file="../../../secret.png"))
        hz._save(p, r)
        with mock.patch.object(gui.CLI, "HOME_STATE", home):
            self.assertEqual(gui.ask_evidence("-x-p", "t-1", "1"),
                             (self.png.read_bytes(), "image/png"))
            self.assertEqual(gui.ask_evidence("-x-p", "t-1", "2", "2-route.diff")[1],
                             "text/plain; charset=utf-8")
            for args in (("-x-p", "t-1", "3"), ("-x-p", "t-1", "0"), ("-x-p", "t-1", "x"),
                         ("-x-p", "t-1", "1", "2-route.diff"), ("..", "t-1", "1"),
                         ("-x-p", "../t-1", "1"), ("-x-p", "t-2", "1")):
                self.assertIsNone(gui.ask_evidence(*args), args)


class StopKind(unittest.TestCase):
    """A stopped session is either at a permission prompt or waiting on a reply."""
    def setUp(self):
        self.proj = Path(tempfile.mkdtemp())
        (self.proj / "p").mkdir()
        self.p = mock.patch.object(hz, "PROJECTS", self.proj); self.p.start()

    def tearDown(self):
        self.p.stop()

    def run_(self, *entries, rows=None, state="blocked"):
        (self.proj / "p" / "s.jsonl").write_text("\n".join(json.dumps(e) for e in entries))
        return hz.stop_detail({"state": state, "sessionId": "s"}, rows)

    U = staticmethod(lambda c, **k: dict({"type": "user", "message": {"content": c}}, **k))
    A = staticmethod(lambda *c: {"type": "assistant", "message": {"content": list(c)}})
    END = {"type": "system", "subtype": "turn_duration"}
    TXT = {"type": "text", "text": "done"}

    def test_permission_prompt(self):
        call = {"type": "tool_use", "name": "Bash", "input": {"command": "cd /x && ls"}}
        self.assertEqual(self.run_(self.U("go"), self.A(self.TXT, call), {"type": "attachment"}),
                         {"kind": "permission", "tool": "Bash", "what": "cd /x && ls"})

    def test_reply_to_operator(self):
        self.assertEqual(self.run_(self.U("go"), self.A(self.TXT), self.END),
                         {"kind": "reply", "on": "", "said": ""})

    def test_reply_to_the_session_that_prompted_it(self):
        msg = '<cross-session-message from="uds:/r/9.sock" from-name="proj-dev">hi'
        r = self.run_(self.U("go"), self.A(self.TXT), self.END,
                      self.U(msg, isMeta=True), self.U("skill text", isMeta=True),
                      self.A(self.TXT), self.END)
        self.assertEqual(r["on"], "proj-dev")

    def test_last_message_sent_wins(self):
        send = {"type": "tool_use", "name": "SendMessage",
                "input": {"to": "proj-main", "summary": "presented"}}
        res = self.U([{"type": "tool_result", "content": "ok"}])
        r = self.run_(self.U("go"), self.A(send), res, self.A(self.TXT), self.END)
        self.assertEqual((r["on"], r["said"]), ("proj-main", "presented"))

    def test_socket_resolved_by_pid(self):
        send = {"type": "tool_use", "name": "SendMessage", "input": {"to": "uds:/r/42.sock"}}
        res = self.U([{"type": "tool_result", "content": "ok"}])
        e = (self.U("go"), self.A(send), res, self.A(self.TXT), self.END)
        self.assertEqual(self.run_(*e, rows=[{"pid": 42, "name": "proj-main"}])["on"],
                         "proj-main")
        self.assertEqual(self.run_(*e)["on"], "an exited session")

    def test_the_harness_launch_prompt_is_not_the_owner(self):
        jobs = Path(tempfile.mkdtemp())
        (jobs / "j1").mkdir()
        (jobs / "j1" / "state.json").write_text(json.dumps({"intent": "Use the harness skill."}))
        (self.proj / "p" / "s.jsonl").write_text("\n".join(json.dumps(e) for e in (
            self.U("Use the harness skill."), self.A(self.TXT), self.END)))
        with mock.patch.object(hz, "JOBS", jobs):
            r = hz.stop_detail({"state": "blocked", "sessionId": "s", "id": "j1"})
            self.assertEqual(r["on"], hz.LAUNCHED)
            # Its prompt beyond the tail: a whole queue worked in one long turn.
            self.assertEqual(hz.stop_detail({"state": "blocked", "sessionId": "s", "id": "j1"},
                                            tail=60)["on"], hz.LAUNCHED)
            (self.proj / "p" / "s.jsonl").write_text("\n".join(json.dumps(e) for e in (
                self.U("owner typed this"), self.A(self.TXT), self.END)))
            self.assertEqual(hz.stop_detail({"state": "blocked", "sessionId": "s", "id": "j1"})["on"], "")

    def test_neither(self):
        self.assertIsNone(self.run_(self.A(self.TXT), self.END, self.U("again")))
        self.assertIsNone(self.run_(self.U("go"), self.A(self.TXT), self.END,
                                    state="working"))


class EndedSessions(unittest.TestCase):
    """`sweep --sessions`: which ended sessions are this project's to remove."""

    def test_selection(self):
        base = Path(tempfile.mkdtemp())
        repo, wt = base / "proj", base / "proj-dev_1"
        repo.mkdir(); wt.mkdir()
        ctx = FakeCtx({"main": None})
        ctx.repo = repo
        row = lambda sid, name, cwd, **k: dict({"sessionId": sid, "name": name,
                                                "cwd": str(cwd)}, **k)
        rows = [row("live", "proj-dev_1", wt, pid=1),
                row("ended", "proj-dev_1", wt),
                row("cited", "proj-dev_1", wt),
                row("trimmed", "proj-panel", base / "proj-panel"),     # worktree gone
                row("owners", "my own session", wt),                  # not spawn's name
                row("elsewhere", "proj-x", base),                     # not a node's
                row("me", "proj-main", repo)]
        with mock.patch.object(hz, "live_rows", lambda rs: [r for r in rs if r.get("pid")]), \
             mock.patch.object(hz, "load_index", return_value={"byWorktree": {str(wt): "dev_1"}}), \
             mock.patch.object(hz, "job_dirs", return_value={"cited": base / "j"}), \
             mock.patch.object(hz, "job_refs", return_value={base / "j": {"all": "facts/x",
                                                                          "files": {}}}), \
             mock.patch.dict(os.environ, {"CLAUDE_CODE_SESSION_ID": "me"}):
            got = {r["sessionId"]: why for r, why in hz.ended_sessions(ctx, rows)}
        self.assertEqual(got, {"ended": None, "cited": "facts/x", "trimmed": None})

    def test_orientation_count_reads_job_folders(self):
        jobs = Path(tempfile.mkdtemp())
        ctx = FakeCtx({"main": None})
        ctx.repo = Path("/r")
        other = tempfile.mkdtemp()                       # exists: not a trimmed node
        for i, (cwd, st, nm) in enumerate([("/r-dev", "done", "r-dev"),
                                           ("/r-dev", "stopped", "r-dev"),
                                           ("/r-dev", "stopped", "r-dev"),     # cited
                                           ("/r-dev", "working", "r-dev"),
                                           ("/r-dev", "done", "mine"),
                                           (other, "done", "r-x")]):
            (jobs / str(i)).mkdir()
            (jobs / str(i) / "state.json").write_text(
                json.dumps({"cwd": cwd, "state": st, "name": nm}))
        with mock.patch.object(hz, "JOBS", jobs), \
             mock.patch.object(hz, "job_refs", return_value={jobs / "2": {}}), \
             mock.patch.object(hz, "load_index", return_value={"byWorktree": {"/r-dev": "dev"}}), \
             mock.patch.object(hz, "ENDED_NAG", 1):
            self.assertEqual(hz.ended_count(ctx), 2)
            with mock.patch.object(hz, "job_refs", side_effect=AssertionError):
                self.assertEqual(hz.ended_count(ctx), 2)          # cached


class Wake(unittest.TestCase):
    """obs 70: a time gate starts its node when the time comes, if nothing else will."""
    AT = 1000.0

    def plan(self, rows=(), brief=None, state="briefed", waits=(), role="member", marks=None):
        ctx = FakeCtx({"main": None, "dev": "main", "dev_1": "dev"})
        b = dict({"task": "run", "node": "dev_1", "not_before": self.AT}, **(brief or {}))
        with mock.patch.object(hz, "load_brief", return_value=(None, b)), \
             mock.patch.object(hz, "task_state", return_value=state), \
             mock.patch.object(hz, "waits_on", return_value=list(waits)), \
             mock.patch.object(hz, "role_of", return_value=role), \
             mock.patch.object(hz, "open_marks", return_value=marks or {}), \
             mock.patch.object(hz, "load_index",
                               return_value={"nodes": {"dev_1": {"worktree": "/w1"}}}):
            return hz.wake_plan(ctx, "run", self.AT, list(rows))

    def test_starts_a_free_or_idle_lane(self):
        self.assertEqual(self.plan()[0], "start")
        self.assertEqual(self.plan([{"cwd": "/w1", "status": "idle"}])[0], "start")

    def test_leaves_what_will_reach_it_anyway(self):
        idle = [{"cwd": "/w1", "status": "idle"}]
        self.assertIsNone(self.plan([{"cwd": "/w1", "status": "busy"}])[0])
        self.assertIsNone(self.plan(idle, marks={"x": {"_node": "dev_1"}})[0])
        self.assertIsNone(self.plan(idle, role="lead")[0])          # never a live lead
        self.assertIsNone(self.plan(state="open")[0])                # already started
        self.assertIsNone(self.plan(waits=["after x (open on dev)"])[0])
        self.assertIn("moved", self.plan(brief={"not_before": self.AT + 60})[1])

    def test_alarm_recycles_the_node_once_due(self):
        ctx = FakeCtx({"main": None, "dev_1": "main"})
        ctx.repo = Path("/r")
        with mock.patch.object(hz, "Ctx", return_value=ctx), \
             mock.patch.object(hz, "agents_json", return_value=[]), \
             mock.patch.object(hz, "wake_plan", return_value=("start", "free")), \
             mock.patch.object(hz, "load_brief", return_value=(None, {"node": "dev_1"})), \
             mock.patch.object(hz, "append_inbox"), \
             mock.patch.object(hz.subprocess, "run") as run, \
             redirect_stdout(io.StringIO()):
            hz.cmd_wake(mock.Mock(task="run", at=str(time.time() - 1)))
        self.assertEqual(run.call_args.args[0][-3:], ["recycle", "dev_1", "--when-idle"])


class DocPairs(unittest.TestCase):
    """T18: pairs that create, move and delete, and the CLAUDE.md budget."""

    def report(self, pairs, files, check=None):
        return hz.pair_report(pairs, lambda f: files.get(f), check)

    def test_ops(self):
        files = {"CLAUDE.md": "intro\n## History\nlong story\n## Rules\nr\n", "old.md": "x"}
        rows, texts = self.report([
            {"op": "move", "file": "CLAUDE.md", "old": "## History\nlong story\n",
             "to": "provenance/CLAUDE/history.md", "pointer": "History: provenance/CLAUDE/history.md\n"},
            {"op": "create", "file": "new.md", "new": "hello\n"},
            {"op": "delete", "file": "old.md"}], files)
        self.assertTrue(all(r[2] == 1 for r in rows))
        self.assertEqual(texts["CLAUDE.md"], "intro\nHistory: provenance/CLAUDE/history.md\n## Rules\nr\n")
        self.assertEqual(texts["provenance/CLAUDE/history.md"], "## History\nlong story\n")
        self.assertEqual(texts["new.md"], "hello\n")
        self.assertIsNone(texts["old.md"])

    def test_refusals(self):
        files = {"a.md": "x"}
        self.assertEqual(self.report([{"op": "create", "file": "a.md", "new": "y"}], files)[0][0][2], 0)
        self.assertEqual(self.report([{"op": "delete", "file": "b.md"}], files)[0][0][2], 0)
        rows, _ = self.report([{"op": "delete", "file": "a.md"}], files,
                              check=lambda x: "an open record names it: brief t")
        self.assertEqual((rows[0][2], rows[0][4]), (0, "an open record names it: brief t"))
        with self.assertRaises(SystemExit):
            hz.parse_pairs('[{"op": "move", "file": "a.md", "old": "x"}]')   # no to/pointer

    def test_budget_refuses_growth_only(self):
        ctx = FakeCtx({"main": None})
        ctx.repo = Path(tempfile.mkdtemp())
        (ctx.repo / ".harness").mkdir()
        (ctx.repo / ".harness" / "manifest.json").write_text('{"claude_md_words": 5}')
        read = lambda f: "one two three four five six seven" if f == "CLAUDE.md" else None
        self.assertIsNone(hz.budget_verdict(ctx, read, {"CLAUDE.md": "one two three"}))
        self.assertIsNone(hz.budget_verdict(ctx, read, {"CLAUDE.md": "a b c d e f"}))  # shrinks
        self.assertIn("over its budget", hz.budget_verdict(
            ctx, read, {"CLAUDE.md": "a b c d e f g h"}))
        self.assertIsNone(hz.budget_verdict(ctx, read, {"other.md": "a " * 50}))

    def test_apply_commits_a_move_and_a_delete(self):
        import subprocess
        repo = Path(tempfile.mkdtemp())
        g = lambda *a: subprocess.run(["git", "-C", str(repo), *a], capture_output=True, text=True)
        g("init", "-q"); g("config", "user.email", "t@t"); g("config", "user.name", "t")
        (repo / "CLAUDE.md").write_text("intro\n## History\nstory\n")
        (repo / "old.md").write_text("gone\n")
        g("add", "-A"); g("commit", "-qm", "init")
        ctx = FakeCtx({"main": None})
        ctx.repo = ctx.worktree = repo
        rec = {"task": "docs-1", "by": "documenter", "auto": True, "job": "budget", "model": "opus",
               "pairs": [{"op": "move", "file": "CLAUDE.md", "old": "## History\nstory\n",
                          "to": "provenance/CLAUDE/history.md", "pointer": "History: provenance/CLAUDE/history.md\n"},
                         {"op": "delete", "file": "old.md"}]}
        f = ctx.dir / "docs-1.json"
        with mock.patch.object(hz, "cited", return_value={}), \
             mock.patch.object(hz, "guard_classify", return_value={}), \
             mock.patch.object(hz, "docs_decided") as chain, redirect_stdout(io.StringIO()):
            with self.assertRaises(SystemExit):                       # not reviewed yet
                hz.pairs_apply(ctx, "main", {"kind": "doc"}, "docs-1", rec, f)
            rec.update(reviewed_by="main", reviewed_at="t")
            hz.pairs_apply(ctx, "main", {"kind": "doc"}, "docs-1", rec, f)
        self.assertFalse((repo / "old.md").exists())
        self.assertEqual((repo / "provenance/CLAUDE/history.md").read_text(), "## History\nstory\n")
        msg = g("log", "-1", "--format=%B").stdout
        self.assertTrue(msg.startswith("Documenter (budget): move “History” CLAUDE.md → "
                                       "provenance/CLAUDE/history.md (3 words) (+1 more); CLAUDE.md 4 → 3"))
        for line in ("Documenter: budget", "Reviewed-by: main", "CLAUDE.md: 4 -> 3 words",
                     "Co-Authored-By: Claude (harness documenter, opus) <noreply@anthropic.com>"):
            self.assertIn(line, msg)
        self.assertEqual(g("status", "--porcelain").stdout, "")
        self.assertEqual(json.loads(f.read_text())["claude_md"], [4, 3])
        self.assertEqual(chain.call_args[0][0], ctx)               # the run ends at review

    def test_the_documenter_cannot_apply(self):
        with mock.patch.dict(os.environ, {"HARNESS_DOCUMENTER": "1"}), \
             self.assertRaises(SystemExit):
            hz.pairs_apply(FakeCtx({"main": None}), "main", {"kind": "doc"}, "t", {}, Path("/x"))


class DocMeasure(unittest.TestCase):
    """T18: what a run measures, from transcripts and records."""

    def lines(self, *tools):
        return "\n".join(json.dumps({"message": {"content": [
            {"type": "tool_use", "name": n, "input": i} for n, i in tools]}}) for _ in [0]) + "\n"

    def test_transcript_reads_and_edits_plain_and_gz(self):
        import gzip as gz
        d = Path(tempfile.mkdtemp())
        body = self.lines(("Read", {"file_path": "/r/proj-dev/schema/SCHEMA.md"}),
                          ("Bash", {"command": "sed -n 1,40p design/API.md | head"}),
                          ("Edit", {"file_path": "/r/proj-dev/schema/schema.sql"}))
        (d / "a.jsonl").write_text(body)
        with gz.open(d / "b.jsonl.gz", "wt") as fh:
            fh.write(body)
        for f in ("a.jsonl", "b.jsonl.gz"):
            got = hz._transcript_facts(d / f)
            self.assertEqual(got["reads"], ["/r/proj-dev/schema/SCHEMA.md", "design/API.md"])
            self.assertEqual(got["edits"], ["/r/proj-dev/schema/schema.sql"])

    def test_cache_parses_only_what_changed(self):
        ctx = FakeCtx({"main": None})
        ctx.repo = Path("/r/proj")
        proj = Path(tempfile.mkdtemp())
        (proj / "-r-proj-dev").mkdir()
        (proj / "-r-proj-dev" / "s.jsonl").write_text(self.lines(("Read", {"file_path": "x.md"})))
        with mock.patch.object(hz, "PROJECTS", proj):
            self.assertEqual(len(hz.doc_transcripts(ctx)), 1)
            with mock.patch.object(hz, "_transcript_facts", side_effect=AssertionError):
                self.assertEqual(list(hz.doc_transcripts(ctx).values())[0]["reads"], ["x.md"])

    def test_rel_strips_any_worktree_of_the_repo(self):
        ctx = FakeCtx({"main": None})
        ctx.repo = Path("/a/proj")
        self.assertEqual(hz._rel(ctx, "/a/proj-dev_1/schema/x.sql"), "schema/x.sql")
        self.assertEqual(hz._rel(ctx, "/a/proj/CLAUDE.md"), "CLAUDE.md")

    def test_gaps(self):
        snap = {"budget": 100, "claude_md": 400,
                "reach": {"schema/**": {"doc": "S.md", "editors": 4, "read": 1}},
                "docs": {"old.md": {"words": 900, "reads": 0, "writes": 0, "pointers_in": 0,
                                    "cited": 0, "idle_days": 30},
                         "used.md": {"words": 900, "reads": 3, "writes": 0, "pointers_in": 2,
                                     "cited": 1, "idle_days": 30}}}
        jobs = [(j, t) for j, t, _ in hz.docs_gaps(snap)]
        self.assertIn(("budget", "CLAUDE.md"), jobs)
        self.assertIn(("reach", "schema/**"), jobs)
        self.assertIn(("stale", "old.md"), jobs)
        self.assertNotIn(("stale", "used.md"), jobs)


class DocRuns(unittest.TestCase):
    """T18: batches land at rank 0's quiet turn end; runs start when due."""

    def setUp(self):
        self.ctx = FakeCtx({"main": None, "dev": "main"})
        self.ctx.repo = self.ctx.worktree = Path(tempfile.mkdtemp())

    def test_trigger_at_most_once_a_day(self):
        with mock.patch.object(hz, "docs_due", return_value="over budget"), \
             mock.patch.object(hz, "_detached") as go:
            self.assertTrue(hz.docs_trigger(self.ctx))
            self.assertFalse(hz.docs_trigger(self.ctx))
        self.assertEqual(go.call_count, 1)
        self.assertEqual(go.call_args.args[1][:3], ["documenter", "--job", "auto"])

    def test_launch_is_restricted_and_carries_its_identity(self):
        pdir = self.ctx.dir
        (pdir / "index.json").write_text(json.dumps({"nodes": {}}))
        home = Path(tempfile.mkdtemp())
        (home / ".claude" / "skills" / "harness-documenter").mkdir(parents=True)
        (home / ".claude" / "skills" / "harness-documenter" / "SKILL.md").write_text("skill")
        with mock.patch.object(hz.Path, "home", return_value=home):
            cmd = hz.documenter_cmd(pdir, str(self.ctx.repo), "stale")
        self.assertEqual(cmd[:4], ["claude", "--bg", "-n", f"harness-documenter-{self.ctx.repo.name}"])
        self.assertIn("--restricted", cmd)
        env = json.loads(cmd[cmd.index("--settings") + 1])["env"]
        self.assertEqual((env["HARNESS_DOCUMENTER"], env["HARNESS_DOCUMENTER_JOB"]), ("1", "stale"))
        allow = cmd[cmd.index("--allowedTools") + 1:cmd.index("--permission-mode")]
        self.assertIn("Bash(harness pairs submit *)", allow)
        self.assertNotIn("Bash(harness pairs *)", allow)                 # never apply
        # Writes only its own batch files: a heredoc'd batch was denied live.
        bd = home / ".local" / "state" / "harness" / pdir.name / "batches"
        self.assertEqual([a for a in allow if a.startswith(("Write", "Edit"))],
                         [f"Write(/{bd}/**)", f"Edit(/{bd}/**)"])            # outside ~/.claude
        self.assertEqual(cmd[cmd.index("--model") + 1], "sonnet")        # stale: the cheap one

    def test_the_documenter_asks_on_docs_and_the_ruling_lands_in_its_file(self):
        with mock.patch.object(hz, "load_brief", return_value=(None, None)):
            with self.assertRaises(SystemExit):
                hz.ask_open(self.ctx, "other", "intent", "q?", "documenter", "s")
            rec = hz.ask_open(self.ctx, "docs", "intent", "Which is right?", "documenter", "s")
        rec.update(state="drafted", draft="the code")
        p = self.ctx.dir / "asks" / f"{rec['id']}.json"
        with mock.patch.object(hz, "evidence_clear"):
            hz.ask_accept(self.ctx.dir, p, rec)
        r = json.loads((self.ctx.dir / "docs" / "rulings.json").read_text())
        self.assertEqual((r[0]["question"], r[0]["answer"]), ("Which is right?", "the code"))


class DocNoteStops(unittest.TestCase):
    """A run's closing note stops its session, so a finished run doesn't read as running."""

    def test_note_schedules_the_stop(self):
        ctx = FakeCtx({"main": None})
        ctx.repo = Path("/r")
        env = {"HARNESS_DOCUMENTER": "1", "CLAUDE_CODE_SESSION_ID": "abcdef12-0000"}
        with mock.patch.object(hz, "Ctx", return_value=ctx), \
             mock.patch.dict(os.environ, env), \
             mock.patch.object(hz.subprocess, "Popen") as po, \
             redirect_stdout(io.StringIO()):
            hz.cmd_docs(mock.Mock(verb="note", args=["moved a section"]))
        self.assertIn("claude stop abcdef12", po.call_args.args[0][2])
        self.assertIn("moved a section", (ctx.dir / "docs" / "ledger.jsonl").read_text())


class DocChain(unittest.TestCase):
    """`documenter --runs N`: runs follow one another once the last batches apply."""

    def setUp(self):
        self.pdir = Path(tempfile.mkdtemp())
        self.a = lambda **k: mock.Mock(**dict({"project": None, "print_cmd": False, "stop": False,
                                               "wake": None, "finish": False,
                                               "next": False, "runs": 1, "job": "auto",
                                               "model": None, "effort": None, "why": None}, **k))
        self.p = [mock.patch.object(hz, "intermediary_project", return_value=(self.pdir, "/r/proj"))]
        for x in self.p:
            x.start(); self.addCleanup(x.stop)

    def run_(self, **k):
        out = io.StringIO()
        with redirect_stdout(out):
            hz.cmd_documenter(self.a(**k))
        return out.getvalue()

    def test_runs_set_the_chain_and_stop_ends_it(self):
        with mock.patch.object(hz, "documenter_launch", return_value=(True, "started")):
            self.assertIn("2 more run(s)", self.run_(runs=3))
        self.assertEqual(hz.docs_queue(self.pdir)["remaining"], 2)
        self.assertIn("2 cancelled", self.run_(stop=True))
        self.assertEqual(hz.docs_queue(self.pdir)["remaining"], 0)

    def test_runs_asked_during_a_run_queue_behind_it(self):
        with mock.patch.object(hz, "documenter_launch", return_value=(False, "x is working; one run")):
            self.assertIn("3 more run(s) will follow", self.run_(runs=3))
        self.assertEqual(hz.docs_queue(self.pdir)["remaining"], 3)

    def test_a_busy_run_refuses_an_idle_one_is_replaced(self):
        row = lambda st: [{"name": "harness-documenter-proj", "status": st, "sessionId": "s" * 36,
                           "pid": 1}]
        with mock.patch.object(hz, "live_rows", lambda r: r), \
             mock.patch.object(hz, "documenter_cmd", return_value=["claude"]), \
             mock.patch.object(hz, "claude_rm") as rm, \
             mock.patch.object(hz.subprocess, "run", return_value=mock.Mock(returncode=0)):
            with mock.patch.object(hz, "agents_json", return_value=row("busy")):
                self.assertFalse(hz.documenter_launch(self.pdir, "/r/proj", "auto")[0])
            with mock.patch.object(hz, "agents_json", return_value=row("idle")):
                self.assertTrue(hz.documenter_launch(self.pdir, "/r/proj", "auto")[0])
        rm.assert_called_once()

    def test_gui_action_validates(self):
        gp = Path(__file__).resolve().parents[1] / "bin" / "harness-gui"
        ld = importlib.machinery.SourceFileLoader("harness_gui", str(gp))
        gui = importlib.util.module_from_spec(importlib.util.spec_from_loader("harness_gui", ld))
        ld.exec_module(gui)
        (self.pdir / "binding.json").write_text('{"repo": "/r/proj"}')
        with mock.patch.object(gui, "_project_dir", return_value=self.pdir), \
             mock.patch.object(gui.subprocess, "run",
                               return_value=mock.Mock(returncode=0, stdout="started", stderr="")) as r:
            self.assertEqual(gui.documenter_action("x", "start", 99)[0], True)
            self.assertIn("20", r.call_args.args[0])                 # capped
            # A state slug starts with "-": a bare "--project <slug>" read it as a flag.
            self.assertIn(f"--project={self.pdir.name}", r.call_args.args[0])
            self.assertEqual(gui.documenter_action("x", "start", "lots"), (False, "runs must be a number"))
            self.assertEqual(gui.documenter_action("x", "drop", 1), (False, "unknown action"))


class Held(unittest.TestCase):
    """A node whose next task is gated on another's task or a clock is held."""

    def test_mark_held(self):
        gp = Path(__file__).resolve().parents[1] / "bin" / "harness-gui"
        ld = importlib.machinery.SourceFileLoader("harness_gui", str(gp))
        gui = importlib.util.module_from_spec(importlib.util.spec_from_loader("harness_gui", ld))
        ld.exec_module(gui)
        nodes = [{"name": "a", "tasks": []}, {"name": "b", "tasks": [{"presented": False}]},
                 {"name": "c", "tasks": []}, {"name": "d", "tasks": []}]
        q = {"a": [{"task": "ta"}], "b": [{"task": "tb"}], "c": [{"task": "tc"}], "d": []}
        why = {"ta": ["after x (open on b)"], "tc": ["until 00:05Z (in 3h)"]}
        with mock.patch.object(gui.CLI, "queue", lambda c, n: q[n]), \
             mock.patch.object(gui.CLI, "startable", lambda c, n: []), \
             mock.patch.object(gui.CLI, "waits_on", lambda c, b: why.get(b["task"], [])):
            gui.mark_held(None, nodes)
        a, b, c, d = nodes
        self.assertEqual(a["held"], [{"task": "ta", "after": "x", "state": "open", "by": "b"}])
        self.assertEqual(b["holding"], [{"node": "a", "after": "x"}])
        self.assertEqual(b["held"], [])                   # mid-task: working, not held
        self.assertEqual(c["held"], [{"task": "tc", "until": "00:05Z (in 3h)"}])
        self.assertEqual(d["held"], [])                   # nothing queued


class SessionModel(unittest.TestCase):
    def test_last_real_model(self):
        d = Path(tempfile.mkdtemp())
        f = d / "s.jsonl"
        f.write_text("\n".join(json.dumps(e) for e in (
            {"type": "assistant", "message": {"model": "claude-sonnet-5-5", "content": []}},
            {"type": "assistant", "message": {"model": "claude-opus-5-5", "content": []}},
            {"type": "assistant", "message": {"model": "<synthetic>", "content": []}},
            {"type": "user", "message": {"content": "x"}})) + "\n")
        self.assertEqual(hz.session_model("s", f), "claude-opus-5-5")
        self.assertIsNone(hz.session_model("", None))


class DocReview(unittest.TestCase):
    """Rank 0 reviews every documenter batch (owner, 2026-10-05; obs 76, 77)."""

    def setUp(self):
        self.ctx = FakeCtx({"main": None, "dev": "main"})
        self.ctx.repo = self.ctx.worktree = Path(tempfile.mkdtemp())
        (self.ctx.dir / "pairs").mkdir()
        self.rec = {"task": "docs-1", "by": "documenter", "auto": True, "job": "budget",
                    "at": time.strftime("%Y-%m-%dT%H:%M:%S%z", time.localtime(time.time() - 600)),
                    "pairs": [{"op": "move", "file": "CLAUDE.md", "old": "## Old\nx\n",
                               "to": "provenance/C/old.md", "pointer": "Old: provenance/C/old.md\n"}]}
        (self.ctx.dir / "pairs" / "docs-1.json").write_text(json.dumps(self.rec))

    def test_the_stop_hook_never_applies_and_rank_0_is_told(self):
        with mock.patch.object(hz, "_detached") as go:
            self.assertFalse(hz.docs_apply_step(self.ctx, "main"))   # pending: no apply, no new run
        go.assert_not_called()
        rows = [r for r in hz.rank0_owes(self.ctx, "main") if r[0] == "review"]
        self.assertEqual(rows[0][1], "docs-1")
        self.assertIn("move “Old” CLAUDE.md → provenance/C/old.md", rows[0][2])

    def test_reading_stamps_the_review_and_decline_records_why(self):
        texts = {"CLAUDE.md": "a\n## Old\nx\n"}
        a = lambda **k: mock.Mock(**dict({"verb": "docs-1", "target": None, "task": None,
                                          "decline": None, "full": False, "auto": False}, **k))
        self.ctx.tree["nodes"]["main"].update(kind="doc", branch="main")
        self.ctx.branch = "main"
        out = io.StringIO()
        with mock.patch.object(hz, "Ctx", return_value=self.ctx), \
             mock.patch.object(hz, "git", side_effect=lambda *x, **k: (0, texts.get(x[1].split(":", 1)[-1], "").rstrip("\n"), "")
                               if x[0] == "show" else (0, "", "")), \
             mock.patch.dict(os.environ, {"CLAUDE_CODE_SESSION_ID": "sess"}), \
             mock.patch.object(hz, "docs_decided") as chain, redirect_stdout(out):
            hz.cmd_pairs(a())
            r = json.loads((self.ctx.dir / "pairs" / "docs-1.json").read_text())
            self.assertEqual(r["reviewed_by"], "main")
            self.assertIn("+Old: provenance/C/old.md", out.getvalue())   # the diff
            hz.cmd_pairs(a(decline="moves a rule sessions need"))
        r = json.loads((self.ctx.dir / "pairs" / "docs-1.json").read_text())
        self.assertEqual(r["refused"], "declined by main: moves a rule sessions need")
        chain.assert_called_once()

    def test_a_new_file_must_be_a_document(self):
        check = hz.pair_guard(self.ctx)
        with mock.patch.object(hz, "guard_classify", side_effect=lambda c, ps: {ps[0]: "code"}):
            self.assertIn("as code", check({"op": "create", "file": "provenance/x.md", "new": "y"}))
            self.assertIn("provenance/**/*.md", check(self.rec["pairs"][0]))
        with mock.patch.object(hz, "guard_classify", side_effect=lambda c, ps: {ps[0]: "doc"}):
            self.assertIsNone(check(self.rec["pairs"][0]))

    def test_a_decision_ends_the_run_or_wakes_it_to_fix(self):
        rec = dict(self.rec, session="S" * 36, applied="abc")
        (self.ctx.dir / "pairs" / "docs-1.json").write_text(json.dumps(rec))
        with mock.patch.object(hz, "_detached") as go:
            hz.docs_decided(self.ctx, rec)
        self.assertEqual(go.call_args.args[1][-1], "--finish")      # applied: the run is over
        rec = dict(self.rec, session="S" * 36, refused="declined by main: wrong heading")
        (self.ctx.dir / "pairs" / "docs-1.json").write_text(json.dumps(rec))
        with mock.patch.object(hz, "_detached") as go:
            hz.docs_decided(self.ctx, rec)
        self.assertEqual(go.call_args.args[1][-2], "--wake")         # declined: fix it
        self.assertIn("wrong heading", go.call_args.args[1][-1])
        (self.ctx.dir / "pairs" / "docs-2.json").write_text(json.dumps(dict(rec, task="docs-2")))
        with mock.patch.object(hz, "_detached") as go:
            hz.docs_decided(self.ctx, dict(rec, task="docs-2"))
        self.assertEqual(go.call_args.args[1][-1], "--finish")      # second decline: over

    def test_note_waits_while_its_batch_is_reviewed(self):
        env = {"HARNESS_DOCUMENTER": "1", "CLAUDE_CODE_SESSION_ID": "S" * 36}
        rec = dict(self.rec, session="S" * 36)
        (self.ctx.dir / "pairs" / "docs-1.json").write_text(json.dumps(rec))
        with mock.patch.object(hz, "Ctx", return_value=self.ctx), \
             mock.patch.dict(os.environ, env), \
             mock.patch.object(hz.subprocess, "Popen") as po, \
             redirect_stdout(io.StringIO()) as out:
            hz.cmd_docs(mock.Mock(verb="note", args=["moved", "history"], json=False))
        po.assert_not_called()                                       # no stop: it waits
        self.assertIn("waits on rank 0's review", out.getvalue())

    def test_moved_text_reach_counts_only_later_sessions(self):
        r = dict(self.rec, applied="abc", applied_at="2026-10-05T16:00:00+1100")
        t0 = hz._epoch(r["applied_at"])
        trs = {"a": {"reads": ["/x/proj/provenance/C/old.md"], "edits": [], "mtime": t0 + 60},
               "b": {"reads": ["/x/proj/provenance/C/old.md"], "edits": [], "mtime": t0 - 60},
               "c": {"reads": [], "edits": [], "mtime": t0 + 90}}
        self.ctx.repo = Path("/x/proj")
        with mock.patch.object(hz, "docs_batches", return_value=[(None, r)]), \
             mock.patch.object(hz, "doc_files", return_value=[]), \
             mock.patch.object(hz, "doc_transcripts", return_value=trs), \
             mock.patch.object(hz, "git", return_value=(0, "", "")), \
             mock.patch.object(hz, "all_briefs", return_value={}), \
             mock.patch.object(hz, "cited", return_value={}):
            snap = hz.docs_measure(self.ctx)
        self.assertEqual((snap["moved"][0]["read"], snap["moved"][0]["sessions"]), (1, 2))


class ProjectArg(unittest.TestCase):
    def test_a_dash_led_slug_parses(self):
        import argparse
        ap = argparse.ArgumentParser(); ap.add_argument("--project")
        arg = hz.project_arg(Path("/s/-mnt-a-proj"))
        self.assertEqual(ap.parse_args([arg]).project, "-mnt-a-proj")


class DocPing(unittest.TestCase):
    """A documenter batch tells rank 0 to review it: an idle rank 0 hears nothing else."""

    def test_submit_prints_the_message_to_rank_0(self):
        ctx = FakeCtx({"main": None, "dev": "main"})
        ctx.repo = ctx.worktree = Path(tempfile.mkdtemp())
        ctx.tree["nodes"]["main"].update(kind="doc", branch="main")
        ctx.tree["project"] = "proj"
        pairs = '[{"op": "create", "file": "provenance/a.md", "new": "x"}]'
        out = io.StringIO()
        with mock.patch.object(hz, "Ctx", return_value=ctx), \
             mock.patch.object(hz, "git", side_effect=lambda *a, **k: (1, "", "") if a[0] == "show"
                               else (0, "", "")), \
             mock.patch.object(hz, "guard_classify", return_value={}), \
             mock.patch.object(hz, "load_index", return_value={"nodes": {"main": {"worktree": "/w"}}}), \
             mock.patch.object(hz, "live_rows", lambda r: r), \
             mock.patch.object(hz, "agents_json", return_value=[{"cwd": "/w", "name": "proj-main"}]), \
             mock.patch.dict(os.environ, {"HARNESS_DOCUMENTER": "1", "HARNESS_DOCUMENTER_JOB": "stale"}), \
             redirect_stdout(out):
            hz.cmd_pairs(mock.Mock(verb="submit", target=pairs, task=None))
        line = next(l for l in out.getvalue().splitlines() if "SendMessage" in l)
        self.assertIn("SendMessage to 'proj-main'", line)
        self.assertIn("awaits your review: create provenance/a.md", line)
        self.assertNotIn("\\", line)
        with mock.patch.object(hz, "load_index", side_effect=Exception):
            self.assertEqual(hz.root_session_name(ctx, "main"), "proj-main")   # the spawn name


class Doorbell(unittest.TestCase):
    """Waking an idle session: its background `harness doorbell` exits."""

    def setUp(self):
        self.ctx = FakeCtx({"main": None, "dev": "main"})
        self.ctx.me = "main"
        self.env = mock.patch.dict(os.environ, {"CLAUDE_CODE_SESSION_ID": "sess-main"})
        self.env.start(); self.addCleanup(self.env.stop)
        self.c = mock.patch.object(hz, "Ctx", return_value=self.ctx)
        self.c.start(); self.addCleanup(self.c.stop)

    def out(self, f, a):
        o = io.StringIO()
        with redirect_stdout(o):
            f(a)
        return o.getvalue()

    def test_ring_wakes_and_read_says_why(self):
        self.ctx.me = "dev"
        self.out(hz.cmd_ring, mock.Mock(node="main", text=["dev", "needs", "a", "ruling"]))
        self.ctx.me = "main"
        with mock.patch.object(hz, "bell_nudge", return_value=None):
            o = self.out(hz.cmd_doorbell, mock.Mock(read=False, status=False))
        self.assertIn("rang: 1 message", o)
        self.assertFalse((hz.bell_dir(self.ctx, "main") / "armed.json").exists())
        o = self.out(hz.cmd_doorbell, mock.Mock(read=True, status=False))
        self.assertIn("from dev: dev needs a ruling", o)
        self.assertIn("nothing has rung", self.out(hz.cmd_doorbell, mock.Mock(read=True, status=False)))

    def test_a_newer_doorbell_replaces_the_old(self):
        d = hz.bell_dir(self.ctx, "main")
        def sleep(_):
            (d / "armed.json").write_text(json.dumps({"pid": -1}))
        with mock.patch.object(hz, "bell_nudge", return_value=None), \
             mock.patch.object(hz.time, "sleep", side_effect=sleep):
            self.assertIn("replaced", self.out(hz.cmd_doorbell, mock.Mock(read=False, status=False)))

    def test_nudge_once_per_wait_and_only_when_idle(self):
        rows = [{"sessionId": "sess-main", "status": "idle", "cwd": "/m"}]
        w = [("dev", 900, "carry rebuilt", "inf:dev:1")]
        with mock.patch.object(hz, "cached_roster", return_value=rows), \
             mock.patch.object(hz, "waiters_on", return_value=w), \
             mock.patch.object(hz, "load_index", return_value={"byWorktree": {}}):
            with mock.patch.object(hz, "last_turn", return_value=(60, 0)):
                self.assertIsNone(hz.bell_nudge(self.ctx, "main", "sess-main"))   # just spoke
            with mock.patch.object(hz, "last_turn", return_value=(900, 0)):
                self.assertIn("dev has been waiting on you for 15m: carry rebuilt",
                              hz.bell_nudge(self.ctx, "main", "sess-main"))
                self.assertIsNone(hz.bell_nudge(self.ctx, "main", "sess-main"))   # told once
            rows[0]["status"] = "busy"
            with mock.patch.object(hz, "waiters_on", return_value=[("dev", 900, "", "inf:dev:2")]), \
                 mock.patch.object(hz, "last_turn", return_value=(900, 0)):
                self.assertIsNone(hz.bell_nudge(self.ctx, "main", "sess-main"))   # working


class OwnerActions(unittest.TestCase):
    """Commands rank 0 hands the owner: an action ask with runs, through the
    intermediary to the Issues tab; Done rings the asker, a question wakes it."""

    def setUp(self):
        self.ctx = FakeCtx({"main": None, "dev": "main", "dev_1": "dev"})
        (self.ctx.dir / "briefs").mkdir()
        (self.ctx.dir / "briefs" / "s1.json").write_text(json.dumps({"task": "s1", "node": "dev_1"}))
        self.err = mock.patch("sys.stderr", new_callable=io.StringIO)
        self.err.start()
        self.addCleanup(self.err.stop)

    def open(self, me="main", sid="s" * 36, task="owner", runs=("pip install x",), kind="action"):
        return hz.ask_open(self.ctx, task, kind, "Install x?", me, sid, list(runs))

    def path(self, rec):
        return self.ctx.dir / "asks" / f"{rec['id']}.json"

    def test_rank0_opens_on_owner_without_a_brief(self):
        r = self.open()
        self.assertEqual((r["id"], r["task"], r["runs"], r["thread"]),
                         ("owner-1", "owner", ["pip install x"], []))
        with self.assertRaises(SystemExit):
            self.open(me="dev")                              # a lead: its own task
        self.assertEqual(self.open(me="dev", task="s1")["runs"], ["pip install x"])
        with self.assertRaises(SystemExit):
            self.open(runs=())                               # owner carries commands
        with self.assertRaises(SystemExit):
            self.open(runs=["x"] * 11)
        with self.assertRaises(SystemExit):
            self.open(runs=["x" * 501])
        with self.assertRaises(SystemExit):
            self.open(task="s1", kind="intent")              # --run needs action

    def test_done_logs_stubs_rings_and_is_told_once(self):
        r = self.open()
        hz.ask_done(self.ctx.dir, self.path(r), r, "ran fine")
        stub = json.loads(self.path(r).read_text())
        self.assertEqual((stub["state"], stub["note"]), ("done", "ran fine"))
        self.assertEqual(hz.owner_done(self.ctx.dir)[0]["runs"], ["pip install x"])
        rung = list((self.ctx.dir / "doorbell" / "main" / "inbox").glob("*.json"))
        self.assertEqual(len(rung), 1)
        msg = json.loads(rung[0].read_text())
        self.assertEqual(msg["from"], "owner")
        self.assertIn("pip install x", msg["text"])
        self.assertIn("ran fine", msg["text"])
        self.assertIn("done:owner-1", hz.ask_notices(self.ctx, "main"))
        hz.ask_consume(self.ctx, ["done:owner-1"])
        self.assertFalse(self.path(r).exists())
        self.assertEqual(self.open()["id"], "owner-2")       # the log keeps the id
        with self.assertRaises(SystemExit):
            hz.ask_done(self.ctx.dir, self.path(r), dict(r, kind="intent"))

    def test_msg_and_reply_thread(self):
        r = self.open()
        hz.ask_msg(self.path(r), r, "owner", "is x the pinned one?")
        self.assertTrue(r["query_open"])
        hz.ask_reply(self.path(r), r, "yes, 1.2")
        saved = json.loads(self.path(r).read_text())
        self.assertEqual([t["by"] for t in saved["thread"]], ["owner", "intermediary"])
        self.assertFalse(saved["query_open"])
        self.assertEqual(saved["state"], "ready")            # looked at

    def test_note_is_the_owners_alone(self):
        with self.assertRaises(SystemExit):
            hz.ask_open(self.ctx, "owner", "note", "hi", "main", "s" * 36)
        r = hz.ask_open(self.ctx, "owner", "note", "hi", "owner", "")
        self.assertEqual((r["kind"], r["asker_node"]), ("note", "owner"))
        hz.ask_done(self.ctx.dir, self.path(r), r)           # Close: nobody to ring
        self.assertFalse((self.ctx.dir / "doorbell" / "owner").exists())


class ItemSessions(unittest.TestCase):
    """One intermediary session per open ask: resumed, never copied; capped."""

    def setUp(self):
        self.pdir = Path(tempfile.mkdtemp())
        (self.pdir / "asks").mkdir()
        for i, kind in ((1, "action"), (2, "intent")):
            (self.pdir / "asks" / f"t-{i}.json").write_text(json.dumps(
                {"id": f"t-{i}", "kind": kind, "state": "asked", "question": "q"}))
        self.err = mock.patch("sys.stderr", new_callable=io.StringIO)
        self.err.start()
        self.addCleanup(self.err.stop)

    def row(self, ask, status="idle", sid=None, kind="background", t=1):
        return {"name": f"harness-intermediary-proj-{ask}", "sessionId": sid or ask * 12,
                "status": status, "kind": kind, "startedAt": t, "pid": 1}

    def wake(self, rows, ask="t-1", why="hello", rc=0):
        calls = []
        def run(cmd, **kw):
            calls.append(cmd)
            return mock.Mock(returncode=rc, stdout="", stderr="")
        with mock.patch.object(hz, "roster_all", return_value=rows), \
             mock.patch.object(hz, "live_rows", side_effect=lambda rs: [r for r in rs if r.get("pid")]), \
             mock.patch.object(hz, "intermediary_cmd", side_effect=lambda *a, **k:
                               ["claude", "--bg", "FRESH", a[2], k.get("ask_id"), k.get("start")]), \
             mock.patch.object(hz.subprocess, "run", side_effect=run):
            ok, msg = hz.item_wake(self.pdir, "/r/proj", ask, why)
        return ok, msg, calls

    def test_names_are_per_ask(self):
        self.assertEqual(hz.item_name("/x/proj", "owner-3"), "harness-intermediary-proj-owner-3")
        rows = [self.row("t-1", sid="a" * 36, t=1), dict(self.row("t-1", sid="b" * 36, t=2), pid=None)]
        with mock.patch.object(hz, "live_rows", side_effect=lambda rs: [r for r in rs if r.get("pid")]):
            live, sid = hz.item_sessions("/x/proj", rows)["t-1"]
        self.assertEqual((live["sessionId"], sid), ("a" * 36, "b" * 36))   # newest id wins

    def test_busy_or_terminal_queues(self):
        for r in (self.row("t-1", "busy"), self.row("t-1", kind="interactive")):
            ok, _, calls = self.wake([r])
            self.assertEqual(calls, [])
            self.assertEqual(hz.item_inbox(self.pdir, "t-1", take=True), ["hello"])

    def test_idle_is_stopped_then_resumed_without_flags(self):
        sid = "abcd1234" + "x" * 28
        ok, _, calls = self.wake([self.row("t-1", sid=sid)])
        self.assertEqual(calls[0], ["claude", "stop", "abcd1234"])
        self.assertEqual(calls[1][:4], ["claude", "--bg", "--resume", sid])
        self.assertEqual(len(calls[1]), 5)                   # flags would start a copy
        self.assertIn("harness ask --idle", calls[1][4])

    def test_fresh_start_takes_the_model_for_its_kind(self):
        ok, _, calls = self.wake([], ask="t-2")
        self.assertEqual(calls[0][:5], ["claude", "--bg", "FRESH", "opus", "t-2"])
        ok, _, calls = self.wake([], ask="t-1")
        self.assertEqual(calls[0][3], "sonnet")

    def test_cap_queues_the_fourth(self):
        rows = [self.row(f"x-{i}") for i in range(3)]
        ok, msg, calls = self.wake(rows)
        self.assertTrue(msg.startswith("queued"))
        self.assertEqual(calls, [])
        self.assertEqual(hz.item_inbox(self.pdir, "t-1", take=True), ["hello"])

    def test_closed_ask_is_not_woken(self):
        ok, _, calls = self.wake([], ask="t-9")
        self.assertFalse(ok)

    def test_bg_cmd_carries_its_ask(self):
        repo = Path(tempfile.mkdtemp())
        with mock.patch.object(hz, "intermediary_prompt", return_value=self.pdir / "p.md"):
            cmd = hz.intermediary_cmd(self.pdir, str(repo), "sonnet", "medium", bg=True,
                                      start="go", ask_id="t-1")
        env = json.loads(cmd[cmd.index("--settings") + 1])["env"]
        self.assertEqual(env["HARNESS_ASK"], "t-1")
        self.assertEqual(cmd[cmd.index("-n") + 1], f"harness-intermediary-{repo.name}-t-1")
        tools = cmd[cmd.index("--tools") + 1:cmd.index("--allowedTools")]
        self.assertNotIn("SendMessage", tools)               # lost on a sleeping session
        self.assertEqual(cmd[-1], "go")

    def test_idle_prints_inbox_else_schedules_settle(self):
        hz.item_inbox(self.pdir, "t-1", "owner asks")
        with mock.patch.object(hz, "_intermediary_bg") as bg, redirect_stdout(io.StringIO()) as out:
            hz.ask_idle(self.pdir, "t-1")
        self.assertIn("owner asks", out.getvalue())
        bg.assert_not_called()
        with mock.patch.object(hz, "_intermediary_bg") as bg, redirect_stdout(io.StringIO()):
            hz.ask_idle(self.pdir, "t-1")
        self.assertEqual(bg.call_args[0][1], ["--ask", "t-1", "--settle"])

    def test_settle_waits_out_the_cache_window(self):
        live = self.row("t-1", sid="abcd1234" + "x" * 28)
        turns = iter([(30, 0), (hz.INTERMEDIARY_QUIET + 1, 0)])
        with mock.patch.object(hz, "roster_all", return_value=[live]), \
             mock.patch.object(hz, "live_rows", side_effect=lambda rs: rs), \
             mock.patch.object(hz, "last_turn", side_effect=lambda sid: next(turns)), \
             mock.patch.object(hz.time, "sleep") as sl, \
             mock.patch.object(hz, "items_next"), \
             mock.patch.object(hz.subprocess, "run") as run, \
             redirect_stdout(io.StringIO()):
            hz.item_settle(self.pdir, "/r/proj", "t-1")
        sl.assert_called_once_with(hz.INTERMEDIARY_QUIET - 30 + 5)
        self.assertEqual(run.call_args[0][0], ["claude", "stop", "abcd1234"])
        self.assertGreaterEqual(hz.INTERMEDIARY_QUIET, 50 * 60)


class ItemMessages(unittest.TestCase):
    """Messages are addressed to an ask, logged in its thread, and wake its session."""

    def setUp(self):
        self.repo = Path(tempfile.mkdtemp())
        (self.repo / ".harness").mkdir()
        (self.repo / ".harness" / "tree.json").write_text(json.dumps(
            {"nodes": {"main": {}, "dev": {"parent": "main"}}}))
        self.pdir = Path(tempfile.mkdtemp())
        (self.pdir / "asks").mkdir()
        self.path = self.pdir / "asks" / "t-1.json"
        self.rec = {"id": "t-1", "kind": "intent", "state": "ready", "question": "Ship X?",
                    "asker_node": "main", "thread": []}
        self.path.write_text(json.dumps(self.rec))
        self.err = mock.patch("sys.stderr", new_callable=io.StringIO)
        self.err.start()
        self.addCleanup(self.err.stop)

    def test_to_rings_the_node_and_its_msg_clears_the_wait(self):
        hz.ask_to(self.pdir, self.repo, self.path, self.rec, "dev", "which test failed?")
        self.assertEqual(self.rec["waiting_on"], "dev")
        rung = list((self.pdir / "doorbell" / "dev" / "inbox").glob("*.json"))
        self.assertIn("harness ask t-1 --msg", json.loads(rung[0].read_text())["text"])
        with self.assertRaises(SystemExit):
            hz.ask_to(self.pdir, self.repo, self.path, self.rec, "nobody", "x")
        hz.ask_msg(self.path, self.rec, "dev", "the import one")
        saved = json.loads(self.path.read_text())
        self.assertIsNone(saved["waiting_on"])
        self.assertEqual([t["by"] for t in saved["thread"]], ["intermediary", "dev"])
        self.assertFalse(saved.get("query_open"))
        hz.ask_msg(self.path, self.rec, "owner", "why?")
        self.assertTrue(json.loads(self.path.read_text())["query_open"])

    def test_the_waited_on_node_is_told_at_orientation(self):
        ctx = FakeCtx({"main": None, "dev": "main"})
        (ctx.dir / "asks").mkdir()
        rec = dict(self.rec, waiting_on="dev",
                   thread=[{"by": "intermediary", "to": "dev", "text": "which test?"}])
        (ctx.dir / "asks" / "t-1.json").write_text(json.dumps(rec))
        n = hz.ask_notices(ctx, "dev")
        self.assertIn("imask:t-1:1", n)
        self.assertIn("which test?", n["imask:t-1:1"])

    def cli(self, argv, env):
        with mock.patch.object(hz, "ask_find",
                               return_value=(self.pdir, str(self.repo), self.path, self.rec)), \
             mock.patch.object(hz, "item_wake_detached") as wake, \
             mock.patch.object(hz, "item_close_detached") as close, \
             mock.patch.dict(os.environ, env), \
             mock.patch("sys.argv", ["harness", "ask", *argv]), \
             redirect_stdout(io.StringIO()):
            for k in ("CLAUDE_CODE_SESSION_ID", "HARNESS_ASK", "HARNESS_INTERMEDIARY"):
                if k not in env:
                    os.environ.pop(k, None)
            try:
                hz.main(); code = 0
            except SystemExit as e:
                code = e.code
        return code, wake, close

    def test_scoping_and_closing(self):
        im = {"HARNESS_INTERMEDIARY": "1", "HARNESS_ASK": "t-2"}
        code, _, _ = self.cli(["t-1", "--reply", "x"], im)           # not its ask
        self.assertEqual(code, hz.REFUSED)
        code, _, _ = self.cli(["t-1", "--msg", "x"], dict(im, HARNESS_ASK="t-1"))
        self.assertEqual(code, hz.REFUSED)                            # its own: --reply
        code, wake, _ = self.cli(["t-1", "--msg", "is X the map?"], {})
        self.assertEqual(code, 0)
        self.assertIn("--reply", wake.call_args[0][2])
        code, _, close = self.cli(["t-1", "--reject"], {})
        self.assertEqual(code, 0)
        close.assert_called_once()


class TestQueue(unittest.TestCase):
    """obs 81, owner 2026-10-05: checks run from a queue, one job per project, in a
    copy of the commit, torn down after."""

    def setUp(self):
        import subprocess as sp
        self.sp = sp
        self.root = Path(tempfile.mkdtemp())
        self.repo = self.root / "proj"
        self.repo.mkdir()
        g = lambda *a: sp.run(["git", "-C", str(self.repo), *a], capture_output=True, text=True)
        g("init", "-q"); g("config", "user.email", "t@t"); g("config", "user.name", "t")
        (self.repo / ".harness").mkdir()
        self.state = self.root / "state"
        self.state.mkdir()
        mark = self.state / "tmpdir.txt"
        (self.repo / ".harness" / "manifest.json").write_text(json.dumps({"checks": [
            {"name": "good", "command": f"echo $TMPDIR > {mark}; echo fine", "blindSpot": "-"},
            {"name": "bad", "command": "echo 'failed: x.py(1)'; exit 1", "blindSpot": "-"}]}))
        (self.repo / "a.txt").write_text("a")
        g("add", "-A"); g("commit", "-qm", "one")
        self.sha = g("rev-parse", "HEAD").stdout.strip()
        self.ctx = hz.ProjCtx(self.state, self.repo)
        self.runs = self.root / "runs"
        for m in (mock.patch.object(hz, "RUNS_HOME", self.runs),
                  mock.patch.object(hz, "TESTQ_IDLE", 0),
                  mock.patch.object(hz, "testq_ensure_runner")):
            m.start(); self.addCleanup(m.stop)

    def run_queue(self):
        with mock.patch("sys.stdout", io.StringIO()), mock.patch("signal.signal"):
            hz.testd(self.state, self.repo)

    def test_same_commit_joins_but_a_finished_one_is_never_reused(self):
        j1, how1 = hz.testq_submit(self.ctx, "check", self.sha, "dev_1", "s1")
        j2, how2 = hz.testq_submit(self.ctx, "check", self.sha, "dev", "s2")
        self.assertEqual((how1, how2, j1["id"]), ("queued", "joined", j2["id"]))
        self.assertEqual([r["node"] for r in hz.testq_jobs(self.ctx)[0]["requested_by"]],
                         ["dev_1", "dev"])
        self.run_queue()
        self.assertEqual(hz.testq_submit(self.ctx, "check", self.sha, "qa", "s3")[1], "queued")
        _, how = hz.testq_submit(self.ctx, "check", self.sha, "qa", "s3", arms=["good"])
        self.assertEqual(how, "queued")                         # another arm set: its own job

    def test_priority_goes_first_and_a_lead_promotes_a_lane_job(self):
        log = self.state / "order.txt"
        n1, _ = hz.testq_submit(self.ctx, "cmd", self.sha, "dev_1", "s", command=f"echo n1 >> {log}")
        time.sleep(1.1)
        n2, _ = hz.testq_submit(self.ctx, "cmd", self.sha, "dev_2", "s", command=f"echo n2 >> {log}")
        time.sleep(1.1)
        p1, _ = hz.testq_submit(self.ctx, "cmd", self.sha, "dev", "s", command=f"echo p1 >> {log}",
                                queue="priority")
        self.assertEqual([j["id"] for j in hz.testq_ahead(self.ctx, n1)], [p1["id"]])
        self.run_queue()
        self.assertEqual(log.read_text().split(), ["p1", "n1", "n2"])
        c, _ = hz.testq_submit(self.ctx, "check", self.sha, "dev_1", "s")
        hz.testq_submit(self.ctx, "check", self.sha, "dev", "s", queue="priority")
        self.assertEqual(hz._read_json(hz.testq_dir(self.ctx) / f"{c['id']}.json")["queue"],
                         "priority")

    def test_the_wait_is_estimated_from_finished_jobs(self):
        now = time.time()
        stamp = lambda t: time.strftime("%Y-%m-%dT%H:%M:%S%z", time.localtime(t))
        for k, d in enumerate((60, 120, 90)):
            hz.testq_save(self.ctx, {"id": f"d{k}", "kind": "check", "sha": "x", "state": "done",
                                     "arms": None, "requested_by": [], "at": stamp(now - 999),
                                     "started": stamp(now - 900 + k), "finished": stamp(now - 900 + k + d)})
        hz.testq_save(self.ctx, {"id": "r", "kind": "check", "sha": "y", "state": "running",
                                 "arms": None, "requested_by": [], "at": stamp(now - 40),
                                 "started": stamp(now - 30), "pid": os.getpid()})
        job = {"id": "new", "kind": "check", "arms": None, "state": "queued", "at": stamp(now)}
        hz.testq_save(self.ctx, dict(job, requested_by=[]))
        self.assertAlmostEqual(hz.testq_wait_estimate(self.ctx, job), 150, delta=3)

    def test_arms_run_only_the_named_and_the_report_says_partial(self):
        hz.testq_submit(self.ctx, "check", self.sha, "dev", "s", arms=["good"])
        self.run_queue()
        rep = json.loads(hz.check_report_path(self.ctx, "dev", self.sha).read_text())
        self.assertEqual(([r["name"] for r in rep["checks"]], rep["partial"], rep["arms"]),
                         (["good"], True, ["good"]))

    def test_the_project_is_told_where_it_runs_and_no_setup_is_run(self):
        out = self.state / "env.txt"
        marker = self.state / "setup-ran"
        (self.repo / ".harness" / "manifest.json").write_text(json.dumps({
            "test_setup": f"touch {marker}",
            "checks": [{"name": "env", "blindSpot": "-", "command":
                        f"echo $HARNESS_TEST_ORIGIN $HARNESS_TEST_SHA $HARNESS_TEST_SCRATCH > {out}; "
                        f"touch $HARNESS_TEST_SCRATCH/x"}]}))
        hz.testq_submit(self.ctx, "check", self.sha, "dev", "s", origin="/wt/dev")
        self.run_queue()
        origin, sha, scratch = out.read_text().split()
        self.assertEqual((origin, sha), ("/wt/dev", self.sha))
        self.assertTrue(scratch.startswith(str(self.runs)))
        self.assertFalse(Path(scratch).exists())                # torn down with the run
        self.assertFalse(marker.exists())                       # setup is the project's

    def test_a_run_reports_to_every_requester_rings_and_leaves_nothing(self):
        hz.testq_submit(self.ctx, "check", self.sha, "dev_1", "s1")
        hz.testq_submit(self.ctx, "check", self.sha, "dev", "s2")
        with mock.patch("sys.stdout", io.StringIO()), mock.patch("signal.signal"):
            hz.testd(self.state, self.repo)
        (job,) = hz.testq_jobs(self.ctx)
        self.assertEqual(job["state"], "done")
        for n in ("dev_1", "dev"):
            rep = json.loads(hz.check_report_path(self.ctx, n, self.sha).read_text())
            self.assertEqual((rep["failed"], rep["node"]), (1, n))
            rung = list((self.state / "doorbell" / n / "inbox").glob("*.json"))
            self.assertIn("1/2 passed", json.loads(rung[0].read_text())["text"])
        self.assertTrue((self.state / "tmpdir.txt").read_text().startswith(str(self.runs)))
        self.assertFalse(any(p.is_file() for p in self.runs.rglob("*")))   # nothing it built
        wl = self.sp.run(["git", "-C", str(self.repo), "worktree", "list"],
                         capture_output=True, text=True).stdout
        self.assertEqual(len(wl.strip().splitlines()), 1)              # only the repo itself

    def test_ids_are_unique_within_a_second(self):
        ids = {hz.testq_submit(self.ctx, "cmd", self.sha, "dev", "s", command="true")[0]["id"]
               for _ in range(5)}
        self.assertEqual(len(ids), 5)
        self.assertEqual(len(hz.testq_jobs(self.ctx)), 5)

    def test_one_runner(self):
        held = hz._flock(hz.testq_dir(self.ctx) / "runner.lock", block=False)
        try:
            with mock.patch("sys.stdout", io.StringIO()) as out:
                hz.testd(self.state, self.repo)
            self.assertIn("another runner", out.getvalue())
            self.assertTrue(hz.testq_runner_alive(self.ctx))
        finally:
            held.close()

    def test_a_dead_runners_job_is_failed_and_torn_down(self):
        d = self.runs / "x" / "j"
        d.mkdir(parents=True)
        hz.testq_save(self.ctx, {"id": "j", "kind": "check", "sha": self.sha, "state": "running",
                                 "pid": 999999, "dir": str(d), "requested_by": [], "at": "1"})
        hz.testq_recover(self.ctx)
        self.assertEqual(hz.testq_jobs(self.ctx)[0]["state"], "failed")
        self.assertFalse(d.exists())

    def test_kill_tree_reaches_a_setsid_grandchild(self):
        p = self.sp.Popen(["sh", "-c", "setsid sleep 60 & sleep 60"], start_new_session=True)
        time.sleep(0.5)
        pids = hz.proc_tree(p.pid)
        self.assertGreaterEqual(len(pids), 3)
        hz.kill_tree(p.pid)
        p.wait()
        time.sleep(0.3)
        alive = [x for x in pids if hz._pid_exists(x) and
                 "zombie" not in open(f"/proc/{x}/status").read().lower()]
        self.assertEqual(alive, [])

    def test_reads_from_widens_reads_so_a_hold_catches_the_arm(self):
        c = {"name": "arm", "command": "true", "blindSpot": "-", "reads": [],
             "reads_from": "echo /data/live.db"}
        self.assertEqual(hz.check_reads(c, self.repo), ["/data/live.db"])
        held = hz.hold_catching(dict(c, reads=hz.check_reads(c, self.repo)),
                                [{"path": "/data/live.db", "why": "rebuild", "by": "dev"}])
        self.assertIsNotNone(held)


class StopKillsWork(unittest.TestCase):
    """obs 80: `stop` ends the session's processes, not just the conversation."""

    def test_survivors_are_killed(self):
        import subprocess as sp
        ctx = FakeCtx({"main": None, "dev": "main"})
        ctx.branch = "main"
        sess = sp.Popen(["sh", "-c", "setsid sleep 519 & sleep 520"], start_new_session=True)
        time.sleep(0.4)
        tree = hz.proc_tree(sess.pid)
        idx = {"byWorktree": {"/wt/dev": "dev"}, "byBranch": {"main": "main"},
               "nodes": {"dev": {"children": []}, "main": {"children": ["dev"]}}}
        rows = [{"cwd": "/wt/dev", "sessionId": "d" * 36, "name": "p-dev", "pid": sess.pid}]
        def fake_stop(cmd, **kw):            # `claude stop` ends the session process only
            if cmd[:2] == ["claude", "stop"]:
                sess.kill(); sess.wait()
            return mock.Mock(returncode=0, stdout="", stderr="")
        with mock.patch.object(hz, "Ctx", return_value=ctx), \
             mock.patch.object(hz, "load_index", return_value=idx), \
             mock.patch.object(hz, "agents_json", return_value=rows), \
             mock.patch.object(hz, "live_rows", side_effect=lambda r: r), \
             mock.patch.object(hz.subprocess, "run", side_effect=fake_stop), \
             mock.patch.dict(os.environ, {"CLAUDE_CODE_SESSION_ID": "x"}), \
             redirect_stdout(io.StringIO()) as out:
            hz.cmd_stop(mock.Mock(children=False, node=["dev"], dry_run=False))
        time.sleep(0.3)
        self.assertIn("killed", out.getvalue())
        self.assertEqual([p for p in tree if p != sess.pid and hz._pid_exists(p)], [])
