"""Liveness and nag rules. Run: python3 -m unittest discover harness/tests"""
import importlib.machinery
import importlib.util
import io
import json
import os
import re
import shutil
import socket
import subprocess
import sys
import tempfile
import threading
import time
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest import mock

# Every mail write starts the project's ringer when none runs (log 134). No
# test may start a real daemon.
os.environ["HARNESS_NO_RINGER"] = "1"

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

    def test_a_lead_orders_anywhere_below_it(self):
        # Owner, 2026-10-09: dev orders the lanes under its sub-lead dev_tests,
        # and dev_tests is rung, since its child's order changed under it. A
        # sibling lead may not.
        class Deep(FakeCtx):
            def rank(self, node):
                p = self.tree["nodes"][node]["parent"]
                return 0 if not p else 1 + self.rank(p)
        ctx = Deep({"main": None, "dev": "main", "dev_1": "dev",
                    "dev_tests": "dev", "dev_tests_1": "dev_tests"})
        (ctx.dir / "briefs").mkdir()
        for i, t in enumerate(["a", "b"]):
            (ctx.dir / "briefs" / f"{t}.json").write_text(json.dumps(
                {"task": t, "node": "dev_tests_1", "seq": i}))
        ctx.me = "dev"
        a = mock.Mock(order="b,a", node="dev_tests_1", why="b unblocks dev_1")
        with mock.patch.object(hz, "Ctx", return_value=ctx), \
             mock.patch.object(hz, "ring_report", return_value="r"), \
             mock.patch("sys.stdout", new_callable=io.StringIO):
            hz.cmd_queue(a)
        self.assertEqual([b["task"] for b in hz.queue(ctx, "dev_tests_1")], ["b", "a"])
        rung = list((ctx.dir / "doorbell" / "dev_tests" / "inbox").glob("*.json"))
        self.assertEqual(len(rung), 1)
        self.assertIn("b → a", json.loads(rung[0].read_text())["text"])
        ctx.me = "dev_1"
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
        self.check("true", progress=lambda i, arm, running, done: seen.append((i, arm, done)))
        self.assertEqual(seen[0], (0, "arm", []))                       # told before it runs
        self.assertEqual(seen[-1], (1, None, ["arm"]))                  # and when it ends

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
        # OLD is three hours before this file was loaded, so the minutes depend on
        # how long the suite has run: the hour is what is being checked.
        self.assertRegex(hz.node_activity(self.ctx, "dev"), r"^check running arm 7/23, 3h0\d$")
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

    def test_a_stalled_wait_is_its_lead_s_and_the_rank_above_sees_it_on_request(self):
        # Log 173 (owner, 2026-10-15): the rank above is not prompted with what a
        # lead below owes; that lead is nudged. `whoami --tree` shows it.
        self.wait(OLD)
        self.checking(os.getpid())
        self.assertNotIn("stuck:dev_2", self.items("main"))
        (line,) = hz.stuck_waits(self.ctx, "main")
        self.assertIn("dev: check running arm 7/23", line)
        dev = self.items("dev")
        self.assertIn("asked:dev_2", dev)
        self.assertEqual(hz.stuck_waits(self.ctx, "dev"), [])
        self.wait(time.strftime("%Y-%m-%dT%H:%M:%S%z"))
        self.assertEqual(hz.stuck_waits(self.ctx, "main"), [])


class OwedWake(unittest.TestCase):
    """Log 173 (owner, 2026-10-15): an action a node owes wakes that node, after
    five quiet minutes, and is not shown to the rank above at every prompt."""

    def setUp(self):
        self.ctx = FakeCtx({"main": None, "dev": "main", "dev_1": "dev"})
        (self.ctx.dir / "marks").mkdir()
        p = mock.patch.object(hz, "ensure_ringer", lambda s: None)
        p.start(); self.addCleanup(p.stop)

    def present(self, at=OLD, **more):
        (self.ctx.dir / "marks" / "t.json").write_text(json.dumps(dict(
            {"_node": "dev_1", "_task": "t", "_presented_at": at, "_presented_sha": "a" * 40},
            **more)))

    def inbox(self, n):
        return sorted((self.ctx.dir / "doorbell" / n / "inbox").glob("*.json"))

    def test_what_a_node_owes_is_its_own(self):
        self.present()
        (k, line), = hz.owed_now(self.ctx, "dev").items()
        self.assertTrue(k.startswith("sign off:dev_1:t:"))
        self.assertIn("harness mark t --close", line)
        self.assertEqual(hz.owed_now(self.ctx, "main"), {})      # not main's to sign
        self.present(_review_task="t.review")                    # the reviewer's (log 172)
        self.assertEqual(hz.owed_now(self.ctx, "dev"), {})
        self.present(at=time.strftime("%Y-%m-%dT%H:%M:%S%z"))     # just presented: mid-review
        self.assertEqual(hz.owed_now(self.ctx, "dev"), {})

    def test_a_parked_sign_off_is_owed_by_nobody_until_the_wait_ends(self):
        # Owner, 2026-10-15: dev's item waited on the owner, so dev parks it,
        # with a time, rather than being rung for it.
        self.assertEqual([hz.parse_span(x) for x in ("45m", "3h", "2d", "1h30m", "x", "")],
                         [2700, 10800, 172800, 5400, None, None])
        self.present()
        (self.ctx.dir / "briefs").mkdir()
        brief = self.ctx.dir / "briefs" / "t.json"
        brief.write_text(json.dumps({"task": "t", "node": "dev_1", "wait": {
            "why": "the owner runs the migration", "until": time.time() + 3600}}))
        self.assertEqual(hz.owed_now(self.ctx, "dev"), {})
        now = time.time()
        with mock.patch.object(hz, "turn_end_at", return_value=now - hz.OWED_IDLE - 1):
            self.assertIsNone(hz.owed_ring(self.ctx, "dev", "s", now))
            brief.write_text(json.dumps({"task": "t", "node": "dev_1", "wait": {
                "why": "x", "until": time.time() - 1}}))                  # the wait ran out
            self.assertIn("harness mark t --close", hz.owed_ring(self.ctx, "dev", "s", now))

    def test_it_rings_once_per_item_after_five_quiet_minutes(self):
        self.present()
        now = time.time()
        with mock.patch.object(hz, "turn_end_at", return_value=now - 100):
            self.assertIsNone(hz.owed_ring(self.ctx, "dev", "s", now))   # not quiet long enough
        with mock.patch.object(hz, "turn_end_at", return_value=now - hz.OWED_IDLE - 1):
            text = hz.owed_ring(self.ctx, "dev", "s", now)
            self.assertIn("harness mark t --close", text)
            (m,) = self.inbox("dev")
            self.assertEqual(json.loads(m.read_text())["priority"], "low")   # resumes a sleeper
            self.assertIsNone(hz.owed_ring(self.ctx, "dev", "s", now))       # once
            self.assertEqual(self.inbox("main"), [])
            self.present(_closed_at="2026")                                   # signed off
            self.assertIsNone(hz.owed_ring(self.ctx, "dev", "s", now))
            self.present()                                                    # owed again
            self.assertIsNotNone(hz.owed_ring(self.ctx, "dev", "s", now))
            self.assertEqual(len(self.inbox("dev")), 2)
        self.assertIsNone(hz.owed_ring(self.ctx, "dev", "", now))           # no session at all


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


class HandedSegment(unittest.TestCase):
    """Log 127: a mid-lead's `--close` of a segment its parent wrote presents it,
    so the parent's integrate finds a PRESENTED record."""

    def setUp(self):
        self.ctx = FakeCtx({"main": None, "dev": "main", "dev_tests": "dev",
                            "dev_tests_1": "dev_tests"})
        r = self.ctx.dir / "wt"
        r.mkdir()
        subprocess.run(["git", "init", "-q"], cwd=r, check=True)
        subprocess.run(["git", "-c", "user.name=t", "-c", "user.email=t@t", "commit", "-q",
                        "--allow-empty", "-m", "x"], cwd=r, check=True)
        self.ctx.worktree = self.ctx.repo = r
        for d in ("briefs", "marks"):
            (self.ctx.dir / d).mkdir()
        self.w = lambda p, o: (self.ctx.dir / p).write_text(json.dumps(o))

    def close(self, task, me):
        self.ctx.me, self.ctx.branch = me, me
        with mock.patch.object(hz, "Ctx", return_value=self.ctx), \
             mock.patch.dict(os.environ, {"CLAUDE_CODE_SESSION_ID": "s" * 36}), \
             mock.patch("sys.argv", ["harness", "mark", task, "--close"]), \
             mock.patch("sys.stderr", io.StringIO()) as err, redirect_stdout(io.StringIO()) as o:
            try:
                hz.main()
            except SystemExit:
                pass
        self.err = err.getvalue()
        return o.getvalue()

    def test_a_handed_segment_is_presented_not_closed(self):
        self.w("briefs/seg.json", {"task": "seg", "node": "dev_tests",
                                   "written_by": "dev (session abcd1234)"})
        self.w("briefs/p1.json", {"task": "p1", "node": "dev_tests_1", "from": "seg"})
        self.w("marks/p1.json", {"_node": "dev_tests_1", "_closed_at": "2026"})
        self.ctx.lock("dev_tests", os.getpid())
        out = self.close("seg", "dev_tests")
        self.assertIn("presented, not closed", out)
        rec = json.loads((self.ctx.dir / "marks" / "seg.json").read_text())
        self.assertTrue(rec.get("_presented_at"))
        self.assertFalse(rec.get("_closed_at"))
        self.assertTrue(self.ctx.lock_path("dev_tests").exists())        # still coordinating
        rung = list((self.ctx.dir / "doorbell" / "dev" / "inbox").glob("*.json"))
        self.assertTrue(rung)

    def test_rank_0_still_closes_its_own_segment(self):
        self.w("briefs/seg.json", {"task": "seg", "node": "main",
                                   "written_by": "main (session abcd1234)"})
        self.w("briefs/p1.json", {"task": "p1", "node": "dev", "from": "seg"})
        self.w("marks/p1.json", {"_node": "dev", "_closed_at": "2026"})
        self.close("seg", "main")
        rec = json.loads((self.ctx.dir / "marks" / "seg.json").read_text())
        self.assertTrue(rec.get("_closed_at"))


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

    def test_a_hold_never_blocks_its_own_tasks_check(self):
        # Log 132: a hold until layout-basis-marker skipped that task's own check,
        # which its sign-off (and so the hold's lifting) rested on.
        hold = {"path": "/fixture", "until": "layout-basis-marker"}
        (self.ctx.dir / "marks" / "layout-basis-marker.json").write_text(
            json.dumps({"_node": "dev_2"}))
        job = lambda who: {"kind": "check", "sha": "abc", "requested_by": [{"node": who}]}
        self.ctx.repo = self.ctx.dir
        with mock.patch.object(hz, "git", return_value=(0, "1a2b\tlayout-basis-marker", "")):
            self.assertIn("carries layout-basis-marker", hz.hold_exempt(self.ctx, job("dev"), hold))
        # A trailer that only starts with the name is another task.
        with mock.patch.object(hz, "git", return_value=(0, "1a2b\tlayout-basis-marker-2", "")):
            self.assertIn("dev_2 asked", hz.hold_exempt(self.ctx, job("dev_2"), hold))
            self.assertIsNone(hz.hold_exempt(self.ctx, job("dev_1"), hold))      # a sibling: held
            self.assertIsNone(hz.hold_exempt(self.ctx, job("dev_2"), {"path": "/f", "until": ""}))
            self.assertIsNone(hz.hold_exempt(self.ctx, dict(job("dev_2"), kind="cmd"), hold))

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
        self.launch = launch
        return launch.called

    def test_past_its_ceiling_the_recycle_is_told_so(self):
        # Log 133: the ceiling is a promise; the launched recycle must not skip.
        self.assertTrue(self.step(410_000, time.time() + 3600))
        self.assertEqual(self.launch.call_args.kwargs, {"past": True})
        hz.reset_path(self.ctx, "dev").write_text(json.dumps(
            {"by": "main", "flushed": True, "by_tokens": 400_000, "deadline": time.time() + 3600}))
        with mock.patch.object(hz, "reset_quiet", return_value=True), \
             mock.patch.object(hz, "context_size", return_value=300_000), \
             mock.patch.object(hz, "launch_reset") as launch:
            hz.reset_step(self.ctx, "dev")
        self.assertEqual(launch.call_args.kwargs, {"past": False})     # quiet, not due

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


class ResetBelongsToItsSession(unittest.TestCase):
    """Log 123: a pending reset outlived its session and stopped the next one."""

    def setUp(self):
        self.ctx = FakeCtx({"main": None, "dev": "main"})
        self.ctx.lock("dev", 1, ref="sid-old")
        (self.ctx.dir / "resets").mkdir()
        self.ctx.branch = "main"
        self.ctx.tree["nodes"]["main"]["branch"] = "main"

    def test_the_record_names_its_session_and_lapses_for_another(self):
        p = hz.reset_path(self.ctx, "dev")
        with mock.patch.object(hz, "context_limits", return_value=(300_000, None)), \
             mock.patch.object(hz, "node_running", return_value=("claimed", {"session_id": "sid-old"})), \
             redirect_stdout(io.StringIO()):
            hz.request_reset(self.ctx, ["dev"])
        self.assertEqual(json.loads(p.read_text())["session"], "sid-old")
        rec = dict(json.loads(p.read_text()), flushed=True, deadline=0)
        p.write_text(json.dumps(rec))
        with mock.patch.dict(os.environ, {"CLAUDE_CODE_SESSION_ID": "sid-new"}), \
             mock.patch.object(hz, "launch_reset") as launch:
            self.assertFalse(hz.reset_step(self.ctx, "dev"))
        launch.assert_not_called()
        self.assertFalse(p.exists())
        rung = list((self.ctx.dir / "doorbell" / "main" / "inbox").glob("*.json"))
        self.assertIn("lapsed", json.loads(rung[0].read_text())["text"])

    def test_its_own_session_still_resets(self):
        p = hz.reset_path(self.ctx, "dev")
        p.write_text(json.dumps({"by": "main", "flushed": True, "session": "sid-old",
                                 "deadline": 0}))
        with mock.patch.dict(os.environ, {"CLAUDE_CODE_SESSION_ID": "sid-old"}), \
             mock.patch.object(hz, "reset_quiet", return_value=True), \
             mock.patch.object(hz, "launch_reset") as launch:
            self.assertTrue(hz.reset_step(self.ctx, "dev"))
        launch.assert_called_once()


class Cited(unittest.TestCase):
    """obs 74: does an open record still need a path, before the owner deletes it."""

    def test_open_records_only_and_every_form(self):
        ctx = FakeCtx({"main": None})
        ctx.repo = Path("/r")
        home = str(Path.home())
        texts = [("brief open", f'{{"text": "replay from ~/data/backup-2026.db"}}'),
                 ("fact f", '{"command": "ls scratch/run.py"}'),
                 ("fact held", '{"command": "sqlite3 scratch/held-edge-cost/live-copy.db"}')]
        with mock.patch.object(hz, "open_record_texts", return_value=texts), \
             mock.patch.object(hz, "load_index", return_value={"byWorktree": {"/r-dev": "dev"}}):
            got = hz.cited(ctx, [f"{home}/data/backup-2026.db", "/r-dev/scratch/run.py",
                                 "/elsewhere/backup-2026.db", f"{home}/data/other.bin",
                                 "/r/scratch/test-modules/hec-reaim/live-copy.db",
                                 "/x/y/held-edge-cost/live-copy.db"])
        self.assertEqual(got[f"{home}/data/backup-2026.db"], [("brief open", "names it")])
        self.assertEqual(got["/r-dev/scratch/run.py"], [("fact f", "names it")])
        # Log 102 / obs 78: the same file name in another folder is another file.
        self.assertEqual(got["/elsewhere/backup-2026.db"], [])
        self.assertEqual(got["/r/scratch/test-modules/hec-reaim/live-copy.db"], [])
        self.assertEqual(got["/x/y/held-edge-cost/live-copy.db"],
                         [("fact held", "names held-edge-cost/live-copy.db")])
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

    def test_presenting_rings_the_lead(self):
        """obs 91: the lead heard 2h43m later, from a nag its focus folded away."""
        self.g("merge", "-q", "--ff-only", "main")
        class A:                                   # every other flag unset
            task, done = "t", True
            def __getattr__(self, k):
                return None
        with mock.patch.object(hz, "Ctx", return_value=self.ctx), \
             mock.patch("sys.stderr", io.StringIO()), mock.patch("sys.stdout", io.StringIO()):
            try:
                hz.cmd_mark(A())
            except SystemExit:
                pass
        rung = list((self.ctx.dir / "doorbell" / "main" / "inbox").glob("*.json"))
        self.assertEqual(len(rung), 1)
        msg = json.loads(rung[0].read_text())
        self.assertEqual(msg["from"], "dev")
        self.assertIn("presented 't'", msg["text"])


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
        # The first prompt carries the project's scope, then the start (owner, 2026-10-06).
        self.assertTrue(cmd[-1].startswith("# Project scope"))
        self.assertTrue(cmd[-1].endswith("# Your start\ngo"))
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

    def test_a_bold_label_numbers_its_bullets(self):
        # Log 116: main writes **DONE.** with "- (1)" bullets; nothing numbered.
        done = "INTENT. x\n\n**DONE.**\n- (1) a\n- (2) b\n- (3) c\n"
        self.assertEqual(hz.brief_clauses(done), {1, 2, 3})
        self.assertEqual(hz.brief_clauses("**CHECKS.** (1) a (2) b\n**NOTES.** (3) no"), {1, 2})
        self.assertEqual(hz.brief_clauses(self.TEXT), {1, 2, 3})        # plain, unchanged

    def test_writing_an_unnumbered_done_warns(self):
        def write(text):
            self.ctx.me, self.ctx.branch = "main", "main"
            with mock.patch.object(hz, "Ctx", return_value=self.ctx), \
                 mock.patch.dict(os.environ, {"CLAUDE_CODE_SESSION_ID": "s" * 36}), \
                 mock.patch("sys.argv", ["harness", "brief", "w1", "--for", "dev", "--write",
                                         text]), \
                 mock.patch("sys.stderr", io.StringIO()), redirect_stdout(io.StringIO()) as o:
                try:
                    hz.main()
                except SystemExit:
                    pass
            return o.getvalue()
        out = write("INTENT. x\n**DONE.** every check passes and it is presented.")
        self.assertIn("WROTE", out)
        self.assertIn("no clauses the harness can number", out)
        self.assertNotIn("can number", write("INTENT. x\n**DONE.**\n- (1) a\n- (2) b"))

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
        # Never counted at a prompt (2026-10-12: the count took 3 to 10 s on a
        # live tree): rank 0's rows come from the count the ringer keeps.
        slow = AssertionError("counted on the prompt path")
        with mock.patch.object(hz, "stale_records", side_effect=slow), \
             mock.patch.object(hz, "completed_units", side_effect=slow), \
             mock.patch.object(hz, "ended_count", side_effect=slow):
            self.assertEqual([r for r in hz.rank0_owes(self.ctx, "main") if r[0] == "sweep"], [])
        with mock.patch.object(hz, "ended_count", return_value=3):
            c = hz.sweep_counts(self.ctx, fresh=True)
        self.assertEqual((c["units"], c["stale"], c["sessions"]), (0, 2, 3))
        self.assertEqual(hz.sweep_counts(self.ctx)["stale"], 2)          # kept in a file
        with mock.patch.object(hz, "stale_records", side_effect=slow), \
             mock.patch.object(hz, "completed_units", side_effect=slow), \
             mock.patch.object(hz, "ended_count", side_effect=slow):
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

    def test_a_lead_with_a_lane_at_work_is_never_only_waiting(self):
        # Log 133: dev's one queued task was a carrier waiting on dev_1, so its
        # forced reset was skipped as "every queued task waits" for three hours.
        (self.ctx.dir / "briefs" / "up.json").write_text(json.dumps(
            {"task": "up", "node": "dev", "after": ["merge"]}))
        st = hz.next_start(self.ctx, "dev")
        self.assertIsNone(st["skip"])
        self.assertIn("leads 1 open task(s) below it", st["line"])
        (self.ctx.dir / "marks" / "merge.json").unlink()             # no lane at work
        self.assertIn("waits", hz.next_start(self.ctx, "dev")["skip"])

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


    def stop(self, *argv):
        """`harness stop` from main's session, with nobody live anywhere."""
        self.ctx.me, self.ctx.branch = "main", "main"
        idx = {"byWorktree": {}, "byBranch": {"main": "main"},
               "nodes": {n: {"children": self.ctx.children(n)} for n in ("main", "dev", "dev_1")}}
        with mock.patch.object(hz, "Ctx", return_value=self.ctx), \
             mock.patch.object(hz, "load_index", return_value=idx), \
             mock.patch.object(hz, "agents_json", return_value=[]), \
             mock.patch.dict(os.environ, {"CLAUDE_CODE_SESSION_ID": "s" * 36}), \
             mock.patch("sys.argv", ["harness", "stop", *argv]), \
             redirect_stdout(io.StringIO()) as o:
            hz.main()
        return o.getvalue()

    def test_a_deliberate_stop_is_not_an_outage(self):
        # Log 115: after "stop all work" the Stop hook told rank 0 to spawn dev.
        self.ctx.lock("dev_1", 1)
        self.ctx.lock("dev", 1)
        self.stop("dev", "--dry-run")
        self.assertIsNone(hz.stopped(self.ctx, "dev"))                  # a dry run records nothing
        out = self.stop("dev", "dev_1", "--why", "owner: stop all work for now")
        self.assertIn("stopped on purpose", out)
        self.assertEqual(hz.stopped(self.ctx, "dev")["by"], "main")
        with mock.patch.object(hz, "holder_alive", return_value=False), \
             mock.patch.object(hz, "last_write", return_value=time.time() - 600):
            self.assertEqual([r for r in hz.lead_owes(self.ctx, "dev") if r[0] == "orphan"], [])
            self.assertEqual([r for r in hz.lead_owes(self.ctx, "main") if r[0] == "down"], [])
            line = hz.stopped_line(self.ctx)
            self.assertIn("dev, dev_1", line)
            self.assertIn("owner: stop all work", line)
            hz.stopped_path(self.ctx, "dev_1").unlink()                 # as a claim does
            self.assertEqual([r[0] for r in hz.lead_owes(self.ctx, "dev") if r[0] == "orphan"],
                             ["orphan"])


class SilentNodes(unittest.TestCase):
    """Log 128: a lead that released with its lanes mid-work and mail unread is
    down; log 129: a child's unanswered question while it idles is owed."""

    def setUp(self):
        self.ctx = FakeCtx({"main": None, "dev": "main", "dev_tests": "dev",
                            "dev_tests_1": "dev_tests", "dev_2": "dev"})
        (self.ctx.dir / "marks").mkdir()
        (self.ctx.dir / "marks" / "lane.json").write_text(json.dumps({"_node": "dev_tests_1"}))
        self.stamp = lambda ago: time.strftime("%Y-%m-%dT%H:%M:%S%z",
                                               time.localtime(time.time() - ago))

    def ring(self, to, frm, text, ago, read=False):
        d = self.ctx.dir / "doorbell" / to
        if read:
            d.mkdir(parents=True, exist_ok=True)
            with open(d / "delivered.jsonl", "a") as fh:
                fh.write(json.dumps({"from": frm, "text": text, "at": self.stamp(ago)}) + "\n")
        else:
            (d / "inbox").mkdir(parents=True, exist_ok=True)
            (d / "inbox" / f"{time.time_ns()}.json").write_text(json.dumps(
                {"from": frm, "text": text, "at": self.stamp(ago)}))

    def owed(self, node, running=(None, None), ended=True):
        with mock.patch.object(hz, "node_running", return_value=running), \
             mock.patch.object(hz, "turn_ended", return_value=ended), \
             mock.patch.object(hz, "startable", return_value=[]):
            return [(k, c, t) for k, c, t, _ in hz.lead_owes(self.ctx, node) if k != "heavy"]

    def test_a_released_lead_with_lanes_at_work_and_mail_unread_is_down(self):
        self.ring("dev_tests", "dev", "present it, please", 600)
        rows = self.owed("dev")
        self.assertIn(("down", "dev_tests", "and its lanes still hold open work; 1 unread ring(s)"),
                      rows)
        self.assertEqual(self.owed("dev", running=("unclaimed", {"sessionId": "x"})), [])

    def test_nothing_that_would_start_a_session_is_owed_while_halted(self):
        # Log 135: under the owner's halt the Stop hook still blocked main with
        # "dev has no running session ... harness spawn dev".
        self.ring("dev_tests", "dev", "present it, please", 600)
        self.assertTrue([r for r in self.owed("dev") if r[0] == "down"])
        hp = hz.halt_path(self.ctx)
        hp.parent.mkdir(parents=True, exist_ok=True)
        hp.write_text(json.dumps({"at": "2026-10-09T23:20:00+1100", "why": "shutdown for today"}))
        self.assertEqual([r for r in self.owed("dev") if r[0] in hz.HALT_SILENT], [])
        hp.unlink()
        self.assertTrue([r for r in self.owed("dev") if r[0] == "down"])     # resumed: owed again

    def test_a_question_a_child_waits_on_is_owed_until_answered(self):
        self.ring("dev", "dev_2", "BLOCKER: (a) edit carve.py or (b) leave it to you?", 1800,
                  read=True)
        rows = self.owed("dev", running=("claimed", {"session_id": "s2"}))
        self.assertEqual([r[:2] for r in rows if r[0] == "unanswered"], [("unanswered", "dev_2")])
        self.assertEqual([r for r in self.owed("dev", ("claimed", {"session_id": "s2"}), ended=False)
                          if r[0] == "unanswered"], [])                 # still working
        self.ring("dev_2", "dev", "(a), go ahead", 60)
        self.assertEqual([r for r in self.owed("dev", ("claimed", {"session_id": "s2"}))
                          if r[0] == "unanswered"], [])                 # answered
        self.assertIn("harness ring dev_2 -", hz.owed_line("unanswered", "dev_2", "q", 1800))


class StopCause(unittest.TestCase):
    """Logs 122, 125: a usage limit and an API refusal leave a synthetic API error
    as the last assistant entry; the session's own Stop hook acts on it."""

    LIMIT = {"type": "assistant", "isApiErrorMessage": True, "error": "rate_limit",
             "message": {"model": "<synthetic>", "stop_reason": "stop_sequence", "content": [
                 {"type": "text", "text": "You've hit your session limit · resets 6:10pm (Australia/Sydney)"}]}}
    REFUSAL = [{"type": "system", "subtype": "model_refusal_no_fallback", "requestId": "req_1"},
               {"type": "assistant", "isApiErrorMessage": True, "error": "invalid_request",
                "message": {"model": "<synthetic>", "stop_reason": "refusal",
                            "content": [{"type": "text", "text": "API Error: safeguards"}]}}]
    END = {"type": "system", "subtype": "turn_duration"}

    def setUp(self):
        self.ctx = FakeCtx({"main": None, "dev": "main", "dev_1": "dev"})
        self.t = self.ctx.dir / "t.jsonl"
        m = mock.patch.object(hz, "transcript_for", return_value=self.t)
        m.start(); self.addCleanup(m.stop)

    def write(self, *recs):
        self.t.write_text("".join(json.dumps(r) + "\n" for r in recs))

    def test_a_limit_and_its_reset_time(self):
        self.write({"type": "user", "message": {"content": "go"}}, self.LIMIT, self.END)
        c = hz.stop_cause("s")
        self.assertEqual(c["cause"], "limit")
        self.assertEqual(time.strftime("%H:%M", time.localtime(c["until"])), "18:10")
        self.assertGreater(c["until"], time.time())

    def test_a_refusal_and_a_normal_end(self):
        self.write(*self.REFUSAL, self.END)
        self.assertEqual(hz.stop_cause("s")["cause"], "refusal")
        self.assertEqual(hz.stop_cause("s")["request"], "req_1")
        self.write({"type": "assistant", "message": {"stop_reason": "end_turn",
                                                     "content": [{"type": "text", "text": "done"}]}},
                   self.END)
        self.assertIsNone(hz.stop_cause("s"))
        self.write(self.LIMIT, {"type": "user", "message": {"content": "carry on"}})
        self.assertIsNone(hz.stop_cause("s"))                 # prompted since

    def test_a_reset_time_is_read_against_when_it_was_said(self):
        # Read against the clock, "resets 6:10pm" moved to tomorrow once it
        # passed, so a limit two days old still read as standing.
        said = dict(self.LIMIT, timestamp="2026-10-12T04:17:05.000Z")
        self.write({"type": "user", "message": {"content": "go"}}, said, self.END)
        c = hz.stop_cause("s")
        self.assertEqual(time.strftime("%Y-%m-%d %H:%M", time.localtime(c["until"]))[11:], "18:10")
        self.assertLess(c["until"], time.time())
        with mock.patch.object(hz, "holder_alive", return_value=False), \
             mock.patch.object(hz, "turn_end_at", return_value=1234.0):
            self.assertEqual(hz.holder_state({"session_id": "s"}), ("asleep", 1234.0))

    def test_no_process_is_asleep_limited_or_dead(self):
        held = {"session_id": "s"}
        with mock.patch.object(hz, "holder_alive", return_value=False):
            self.write({"type": "user", "message": {"content": "go"}}, self.LIMIT, self.END)
            st, until = hz.holder_state(held)
            self.assertEqual(st, "limited")
            self.assertGreater(until, time.time())
            self.write(*self.REFUSAL, self.END)
            self.assertEqual(hz.holder_state(held)[0], "dead")           # wedged: needs a fresh one
            self.write({"type": "assistant", "message": {"content": [{"type": "text", "text": "done"}]}},
                       dict(self.END, timestamp="2026-10-14T00:00:00.000Z"))
            self.assertEqual(hz.holder_state(held)[0], "asleep")
            self.write({"type": "assistant", "message": {"content": [{"type": "text", "text": "mid"}]}})
            self.assertEqual(hz.holder_state(held)[0], "dead")
        with mock.patch.object(hz, "holder_alive", return_value=True):
            self.assertEqual(hz.holder_state(held), ("live", None))
        with mock.patch.object(hz, "holder_alive", return_value=None):
            self.assertEqual(hz.holder_state(held), ("unknown", None))

    def test_a_refusal_rings_the_lead_not_the_owner(self):
        hz.stop_cause_step(self.ctx, "dev_1", {"cause": "refusal", "request": "req_1"})
        rung = list((self.ctx.dir / "doorbell" / "dev" / "inbox").glob("*.json"))
        self.assertIn("harness recycle dev_1 --force", json.loads(rung[0].read_text())["text"])

    def test_reset_times(self):
        noon = time.mktime((2026, 10, 9, 12, 0, 0, 0, 0, -1))
        for text, hm in (("resets 6:10pm", "18:10"), ("resets 9am", "09:00"), ("resets 12:30am", "00:30")):
            self.assertEqual(time.strftime("%H:%M", time.localtime(hz._reset_epoch(text, noon))), hm)
        self.assertIsNone(hz._reset_epoch("no time here"))


class MailShownThenLogged(unittest.TestCase):
    """Log 120: mail was logged as delivered before the hook printed it, and a
    hook killed at its timeout lost it."""

    def setUp(self):
        self.state = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.state, True)
        hz.ring_inbox(self.state, "dev", "main", "revoke dev_1's grant")

    def test_a_claim_that_dies_before_its_commit_is_read_again(self):
        got = hz.MAIL().claim(self.state, "dev")
        self.assertEqual(len(got), 1)
        self.assertEqual(hz.MAIL().pending(self.state, "dev"), 0)        # claimed
        c = got[0][0]
        c.rename(c.with_name(c.name.split(".taken-")[0] + ".taken-999999"))  # its process died
        self.assertEqual(hz.MAIL().pending(self.state, "dev"), 1)        # back in the inbox
        self.assertFalse((self.state / "doorbell" / "dev" / "delivered.jsonl").exists())

    def test_commit_logs_it_and_again_shows_it(self):
        got = hz.MAIL().claim(self.state, "dev")
        hz.MAIL().commit(self.state, "dev", got, "prompt")
        self.assertEqual(hz.MAIL().pending(self.state, "dev"), 0)
        (m,) = hz.MAIL().delivered(self.state, "dev", 5)
        self.assertEqual((m["text"], m["how"]), ("revoke dev_1's grant", "prompt"))


class ExitFlips(unittest.TestCase):
    """Log 119: the same file exiting 1 then -11 read as a new failure and a gone
    one; its logs died with the copy. Log 118: reviews read old reports against
    a baseline set since."""

    def test_a_signal_is_a_code_not_a_name(self):
        out = "failed: test_surface_samples.py(-11) test_dag.py(1)"
        self.assertEqual(hz.failed_files(out), ["test_dag.py", "test_surface_samples.py"])
        self.assertEqual(hz.failed_codes(out), {"test_surface_samples.py": -11, "test_dag.py": 1})

    def test_a_changed_code_is_a_flip_not_new(self):
        base = {"arms": {"surface": {"failed": True, "files": ["a.py", "b.py"],
                                     "codes": {"a.py": 1, "b.py": 1}}}}
        row = {"name": "surface", "exit": 1, "failedFiles": ["a.py", "b.py"],
               "failedCodes": {"a.py": -11, "b.py": 1}}
        d = hz.baseline_diff([row], base)["surface"]
        self.assertEqual((d["new"], d["gone"], d["same"]), ([], [], 1))
        self.assertEqual(d["flipped"], [("a.py", 1, -11)])
        self.assertIn("a.py exit 1 → signal 11", hz.baseline_line(d))
        self.assertIn("no new failures", hz.baseline_summary({"checks": [row]}, base))
        old = {"arms": {"surface": {"failed": True, "files": ["a.py", "b.py"]}}}   # no codes kept
        self.assertEqual(hz.baseline_diff([row], old)["surface"]["same"], 2)

    def test_a_known_red_file_with_a_new_fault_inside_is_new(self):
        # dev_tests, 2026-10-15: test_arm_paths.py was red in the baseline for
        # one fault, held two new ones, and every check read it "same".
        out = ("manifest: 3 fault(s), 5 warning(s); 9 arm(s) read\n"
               "reads: 0 fault(s), 251 read(s) exempt\n"
               "  audit outside control: removed, and faulted with 1 fault(s)\n"
               "FAIL: test_x (t.T.test_x)\nFAILED tests/a.py::test_y - boom\n")
        self.assertEqual(hz.fault_counts(out), {"manifest": 3, "test_x (t.T.test_x)": 1,
                                                "tests/a.py::test_y": 1})
        d = Path(tempfile.mkdtemp()); self.addCleanup(shutil.rmtree, d, True)
        (d / "runs__x__documents__test_arm_paths.py.out").write_text(out)
        row = {"name": "documents", "exit": 1, "failedFiles": ["test_arm_paths.py"],
               "failedCodes": {"test_arm_paths.py": 1}}
        row["failedFaults"] = hz.failed_faults(row, [str(p) for p in d.iterdir()])
        self.assertEqual(row["failedFaults"]["test_arm_paths.py"]["manifest"], 3)
        base = {"sha": "b" * 40, "arms": {"documents": {
            "failed": True, "files": ["test_arm_paths.py"], "codes": {"test_arm_paths.py": 1},
            "faults": {"test_arm_paths.py": {"manifest": 1}}}}}
        diff = hz.baseline_diff([row], base)["documents"]
        self.assertEqual(diff["same"], 0)
        self.assertEqual(diff["grew"][0][0], "test_arm_paths.py")
        self.assertIn("manifest 1 → 3", hz.baseline_line(diff))
        self.assertIn("NEW failure", hz.baseline_summary({"checks": [row]}, base))
        self.assertEqual(hz.make_check_report("dev_1", "s", [row], 1, base)["new"], 1)
        # Fewer faults, or a baseline from before faults were kept: same.
        base["arms"]["documents"]["faults"] = {"test_arm_paths.py": dict(
            row["failedFaults"]["test_arm_paths.py"], manifest=4)}
        self.assertEqual(hz.baseline_diff([row], base)["documents"]["same"], 1)
        base["arms"]["documents"].pop("faults")
        self.assertEqual(hz.baseline_diff([row], base)["documents"]["same"], 1)

    def test_a_review_reads_a_report_against_its_own_baseline(self):
        ctx = FakeCtx({"main": None})
        p = hz.baseline_path(ctx)
        p.parent.mkdir(parents=True)
        p.write_text(json.dumps({"sha": "new", "arms": {}, "history": [{"sha": "old", "arms": {"x": 1}}]}))
        self.assertEqual(hz.baseline_at(ctx, "old")["arms"], {"x": 1})
        self.assertEqual(hz.baseline_at(ctx, "new")["sha"], "new")

    def test_a_failed_arms_logs_are_kept_out_of_the_copy(self):
        ctx = FakeCtx({"main": None})
        wt = ctx.dir / "copy"
        (wt / "logs").mkdir(parents=True)
        (wt / "logs" / "test_x.log").write_text("x" * 100 + "segfault here")
        (wt / "logs" / "test_y.log").write_text("not failing")
        o = {"wt": wt, "env": None, "job": {"requested_by": [{"node": "dev"}]},
             "checks": {"surface": {"keep": ["logs/{file}.log"]}}}
        kept = hz.keep_logs(ctx, o, "surface", {"failedFiles": ["test_x.py"]})
        self.assertEqual(len(kept), 1)
        self.assertTrue(Path(kept[0]).read_text().endswith("segfault here"))


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


class SessionFiles(unittest.TestCase):
    """Log 167: a session file outlives its session, and after a restart its pid
    is taken by some other process. Only the process that wrote it counts."""

    def test_a_session_file_whose_pid_was_reused_is_not_a_live_session(self):
        d = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, d, True)
        me = os.getpid()
        start = Path(f"/proc/{me}/stat").read_text().rsplit(")", 1)[-1].split()[19]
        (d / "a.json").write_text(json.dumps({"pid": me, "sessionId": "real", "procStart": start}))
        (d / "b.json").write_text(json.dumps({"pid": me, "sessionId": "old", "procStart": "1"}))
        (d / "c.json").write_text(json.dumps({"pid": me, "sessionId": "nostart"}))   # not claude
        (d / "d.json").write_text(json.dumps({"pid": 2 ** 22 + 7, "sessionId": "gone"}))
        (d / "e.json").write_text("")
        with mock.patch.object(hz, "SESSIONS", d):
            self.assertEqual([x["sessionId"] for x in hz.live_sessions()], ["real"])


class Log161(unittest.TestCase):
    """Log 161: one session per node, however it was started. A start is
    recorded while it is in flight, occupancy is read from two sources, and a
    session that finds itself second in a worktree can write nothing."""

    def setUp(self):
        self.ctx = FakeCtx({"main": None, "dev": "main", "dev_1": "dev"})
        self.addCleanup(shutil.rmtree, self.ctx.dir, True)
        self.ctx.repo = self.ctx.dir / "p"
        self.ctx.tree["project"] = "p"
        (self.ctx.dir / "locks").mkdir()
        nodes = self.ctx.tree["nodes"]
        self.idx = {"project": "p", "byBranch": {n: n for n in nodes},
                    "byWorktree": {f"/w/{n}": n for n in nodes},
                    "nodes": {n: {"worktree": f"/w/{n}", "branch": n, "parent": s.get("parent"),
                                  "rank": self.ctx.rank(n), "children": self.ctx.children(n)}
                              for n, s in nodes.items()}}

    def own(self, node, sid, **more):
        self.ctx.lock_path(node).write_text(json.dumps(
            dict({"node": node, "session_id": sid, "ref": sid, "name": f"p-{node}", "pid": 4242,
                  "host": HOST}, **more)))

    def row(self, node, sid, **more):
        return dict({"sessionId": sid, "cwd": f"/w/{node}", "name": f"p-{node}", "pid": 1,
                     "status": "idle", "kind": "background"}, **more)

    def test_one_start_in_flight_and_what_ends_it(self):
        take, standing = hz.start_take, hz.start_standing
        self.assertIsNone(take(self.ctx, "dev", "spawn", "main"))
        st = take(self.ctx, "dev", "resume", "the ringer", "s-old")
        self.assertEqual((st["how"], st["by"]), ("spawn", "main"))
        self.assertRegex(hz.start_words(st), r"a start is in flight \(spawn by main, \S+ ago\)")
        self.assertIsNone(standing(self.ctx, "dev_1"))                  # one node's is not another's
        hz.start_clear(self.ctx, "dev")
        self.assertIsNone(standing(self.ctx, "dev"))
        take(self.ctx, "dev", "spawn", "main")
        self.assertIsNone(standing(self.ctx, "dev", now=time.time() + hz.START_GRACE + 1))
        self.assertIsNone(take(self.ctx, "dev", "recycle", "harness"))  # lapsed: free again
        hz.start_clear(self.ctx, "dev")
        # A resume has landed once the session it resumed holds the node and runs.
        take(self.ctx, "dev", "resume", "the ringer", "s-1")
        self.own("dev", "s-1")
        with mock.patch.object(hz, "holder_alive", return_value=False):
            self.assertIsNotNone(standing(self.ctx, "dev"))
        with mock.patch.object(hz, "holder_alive", return_value=True):
            self.assertIsNone(standing(self.ctx, "dev"))

    def test_a_claim_clears_the_start(self):
        hz.start_take(self.ctx, "dev", "spawn", "main")
        self.ctx.me, self.ctx.worktree = "dev", "/w/dev"
        me = {"sessionId": "s-new", "name": "p-dev"}
        with mock.patch.object(hz, "Ctx", return_value=self.ctx), \
             mock.patch.multiple(hz, read_roster=lambda p: None, require_contract=lambda r: None,
                                 agents_json=lambda r: [], self_row=lambda rows: me,
                                 interactive_in=lambda *a, **k: []), \
             redirect_stdout(io.StringIO()):
            hz.cmd_claim(mock.Mock(roster=None, strict_name=False, force=False))
        self.assertEqual(json.loads(self.ctx.lock_path("dev").read_text())["session_id"], "s-new")
        self.assertIsNone(hz.start_standing(self.ctx, "dev"))

    def spawn(self, node, rows=(), files=(), me="main", ok=True, sid="s" * 36, cmd="spawn", extra=()):
        self.ctx.me = self.ctx.branch = me
        started, out = [], io.StringIO()

        def launch(cmd_, cwd, env=None):
            started.append((cwd, (env or {}).get("HARNESS_NODE"), "CLAUDE_CODE_SESSION_ID" in (env or {})))
            return (True, "") if ok else (False, "Workspace not trusted")
        with mock.patch.object(hz, "Ctx", return_value=self.ctx), \
             mock.patch.dict(os.environ, {"CLAUDE_CODE_SESSION_ID": sid}), \
             mock.patch.multiple(
                 hz, load_index=lambda *a, **k: self.idx, agents_json=lambda *a: list(rows),
                 live_rows=lambda r: r, live_sessions=lambda: list(files), pid_alive=lambda p: True,
                 read_roster=lambda p: None, grants_for=lambda c, n: [],
                 launch_cmd=lambda *a: ["true"], assignment_for=lambda c, n: ("m", "e"),
                 launch_bg=launch, catch_up=lambda *a, **k: ("current", {}),
                 startable=lambda c, n: [{"task": "t"}], print_delta=lambda *a, **k: None,
                 next_start=lambda c, n: {"skip": None, "line": "starts on t"},
                 git=lambda *a, **k: (0, "", ""), launch_claim_check=lambda *a: None,
                 reset_outcome=lambda *a, **k: None, open_marks=lambda c: {}), \
             mock.patch("sys.argv", ["harness", cmd, node, *extra]), \
             redirect_stdout(out), mock.patch("sys.stderr", out):
            try:
                hz.main()
            except SystemExit:
                pass
        return started, out.getvalue()

    def test_a_second_spawn_stops_on_the_first_s_start(self):
        started, out = self.spawn("dev")
        self.assertEqual(started, [("/w/dev", "dev", False)])           # it knows whose node it is
        self.assertIn("spawned p-dev", out)
        started, out = self.spawn("dev")
        self.assertEqual(started, [])
        self.assertIn("skip dev", out)
        self.assertIn("a start is in flight (spawn by main", out)
        hz.start_clear(self.ctx, "dev")
        started, out = self.spawn("dev", ok=False)                      # refused: nothing stands
        self.assertIn("NOT started", out)
        self.assertIsNone(hz.start_standing(self.ctx, "dev"))

    def test_a_session_the_roster_does_not_list_still_occupies(self):
        # 2026-10-14: a second spawn of dev_migrate_1, a minute after the
        # first, printed "spawned" with the first's session running.
        started, out = self.spawn("dev", files=[self.row("dev", "s-1")])
        self.assertEqual(started, [])
        self.assertIn("occupied by p-dev", out)
        self.assertEqual(len(hz.sessions_in(self.ctx, self.idx, "dev", [self.row("dev", "s-1")],
                                            [self.row("dev", "s-1")])), 1)   # one session, two sources
        with mock.patch.object(hz, "pid_alive", return_value=True):
            for aux in ({"kind": "interactive"}, {"name": "p-design-x"}, {"name": "j1", "jobId": "j1"},
                        {"name": hz.documenter_name(self.ctx.repo)},
                        {"name": hz.intermediary_name(self.ctx.repo)}):
                self.assertEqual(hz.sessions_in(self.ctx, self.idx, "dev", [],
                                                [self.row("dev", "s-x", **aux)]), [], aux)
            self.assertEqual(hz.sessions_in(self.ctx, self.idx, "dev", [],
                                            [self.row("dev_1", "s-kid")]), [])   # the child's, not its

    def test_spawn_says_when_it_retires_a_session_that_was_only_asleep(self):
        self.own("dev", "s-old-1234")
        with mock.patch.object(hz, "holder_state", return_value=("asleep", 0.0)):
            started, out = self.spawn("dev")
        self.assertEqual(len(started), 1)
        self.assertIn("retiring s-old-12, which had only ended its turn", out)
        hz.start_clear(self.ctx, "dev")
        with mock.patch.object(hz, "holder_state", return_value=("dead", 0.0)):
            self.assertNotIn("retiring", self.spawn("dev")[1])

    def test_a_recycle_stops_on_a_start_in_flight_and_records_its_own(self):
        hz.start_take(self.ctx, "dev_1", "resume", "the ringer", "s-old")
        started, out = self.spawn("dev_1", me="dev", cmd="recycle")
        self.assertEqual(started, [])
        self.assertIn("a start is in flight (resume by the ringer", out)
        self.assertIn("nothing stopped", out)
        hz.start_clear(self.ctx, "dev_1")
        started, out = self.spawn("dev_1", me="dev", cmd="recycle")
        self.assertEqual(started, [("/w/dev_1", "dev_1", False)])
        self.assertEqual(hz.start_standing(self.ctx, "dev_1")["how"], "recycle")

    def second(self, sid="s-2", env=None, files=(), alive=True):
        with mock.patch.dict(os.environ, dict({"CLAUDE_CODE_SESSION_ID": sid}, **(env or {}))), \
             mock.patch.object(hz, "holder_alive", return_value=alive), \
             mock.patch.object(hz, "live_sessions", return_value=list(files)), \
             mock.patch.object(hz, "design_env", return_value=None):
            for k in ("HARNESS_INTERMEDIARY", "HARNESS_DOCUMENTER", "HARNESS_NODE"):
                if k not in (env or {}):
                    os.environ.pop(k, None)
            return hz.second_session(self.ctx, "dev")

    def test_who_is_a_second_session(self):
        self.own("dev", "s-1")
        started_here = {"HARNESS_NODE": "dev"}
        self.assertEqual(self.second(env=started_here)["session_id"], "s-1")
        self.assertIsNone(self.second(sid="s-1", env=started_here))               # the holder itself
        self.assertIsNone(self.second(env=started_here, alive=False))             # the holder has gone
        self.assertIsNone(self.second())                                          # the owner's own session
        self.assertIsNone(self.second(env={"HARNESS_NODE": "dev_1"}))             # another node's
        named = [self.row("dev", "s-2")]
        self.assertIsNotNone(self.second(files=named))                            # by the node's name
        self.assertIsNone(self.second(files=[self.row("dev", "s-2", name="something else")]))
        for aux in ("HARNESS_INTERMEDIARY", "HARNESS_DOCUMENTER"):
            self.assertIsNone(self.second(env=dict(started_here, **{aux: "1"})))
        line = hz.second_line("dev", json.loads(self.ctx.lock_path("dev").read_text()))
        self.assertIn("SECOND SESSION: dev is held by p-dev [s-1] (pid 4242)", line)
        self.assertIn("end your turn", line)

    def gate(self, cmd, **flags):
        a = mock.Mock(cmd=cmd, add=None, status=False)
        for k, v in flags.items():
            setattr(a, k, v)
        (self.ctx.dir / "tree.json").write_text(json.dumps(self.ctx.tree))
        self.ctx.binding_path = self.ctx.tree_path = self.ctx.dir / "tree.json"
        self.ctx.me = "dev"
        err = io.StringIO()
        with mock.patch.object(hz.Ctx, "from_files", return_value=self.ctx), \
             mock.patch.object(hz, "second_session", return_value={"session_id": "s-1", "name": "p-dev"}), \
             mock.patch.dict(os.environ, {"CLAUDE_CODE_SESSION_ID": "s-2"}), \
             mock.patch("sys.stderr", err):
            try:
                hz.second_gate(a)
            except SystemExit:
                return err.getvalue() or "refused"
        return None

    def test_a_second_session_s_writes_are_refused_and_its_questions_are_not(self):
        for cmd, flags in (("note", {"add": "x"}), ("spawn", {}), ("mark", {}), ("brief", {}),
                           ("ring", {}), ("doorbell", {"read": True}), ("release", {})):
            self.assertIn("SECOND SESSION", self.gate(cmd, **flags) or "", cmd)
        for cmd, flags in (("status", {}), ("whoami", {}), ("behind", {}), ("claim", {}),
                           ("note", {}), ("doorbell", {"status": True}), ("hook-stop", {}),
                           ("hook-orient", {})):
            self.assertIsNone(self.gate(cmd, **flags), cmd)

    def stop(self, rows, **flags):
        stopped = []
        self.ctx.me = self.ctx.branch = "main"
        a = mock.Mock(children=False, node=["dev"], dry_run=False, surplus=True, keep=None, why=None)
        for k, v in flags.items():
            setattr(a, k, v)
        with mock.patch.object(hz, "Ctx", return_value=self.ctx), \
             mock.patch.multiple(hz, load_index=lambda *a, **k: self.idx, agents_json=lambda *a: rows,
                                 live_rows=lambda r: r, live_sessions=lambda: [],
                                 stop_session_row=lambda c, n, r: (stopped.append(r["sessionId"]),
                                                                   (True, []))[1]), \
             mock.patch.dict(os.environ, {"CLAUDE_CODE_SESSION_ID": "x"}), \
             redirect_stdout(io.StringIO()) as out:
            hz.cmd_stop(a)
        return stopped, out.getvalue()

    def test_stop_surplus_stops_everyone_but_the_holder(self):
        rows = [self.row("dev", "s-a"), self.row("dev", "s-b"), self.row("dev", "s-c")]
        self.own("dev", "s-b")
        stopped, out = self.stop(rows)
        self.assertEqual(stopped, ["s-a", "s-c"])
        self.assertIn("keep dev", out)
        self.assertFalse(hz.stopped_path(self.ctx, "dev").exists())      # the node is not "stopped on purpose"
        self.own("dev", "s-gone")                                        # nobody there holds it
        stopped, out = self.stop(rows)
        self.assertEqual(stopped, [])
        self.assertIn("harness stop dev --surplus --keep <id>", out)
        stopped, out = self.stop(rows, keep="s-c")
        self.assertEqual(stopped, ["s-a", "s-b"])
        stopped, out = self.stop([self.row("dev", "s-b")], keep="s-b")
        self.assertEqual(stopped, [])
        self.assertIn("one session there", out)

    def test_in_rank_0_s_worktree_only_the_node_s_own_sessions_are_rivals(self):
        # The repository is rank 0's worktree, and the owner runs other things there.
        mine, twin = self.row("main", "s-main"), self.row("main", "s-twin")
        other = self.row("main", "s-job", name="fix the importer")
        self.assertEqual(hz.rivals(self.ctx, "main", [mine, other, twin]), [mine, twin])
        self.assertEqual(hz.rivals(self.ctx, "dev", [self.row("dev", "a", name="x")]),
                         [self.row("dev", "a", name="x")])       # a lane's worktree is its own
        self.own("main", "s-main")
        stopped, out = self.stop([mine, other, twin], node=["main"])
        self.assertEqual(stopped, ["s-twin"])

    def claimcheck(self, running, ended=True):
        with mock.patch.object(hz, "Ctx", return_value=self.ctx), \
             mock.patch.object(hz, "node_running", return_value=running), \
             mock.patch.object(hz, "turn_ended", return_value=ended), \
             mock.patch.object(hz.time, "sleep"), redirect_stdout(io.StringIO()):
            hz.cmd_claimcheck(mock.Mock(node="dev_1", within=180))
        return [m["text"] for m in hz.MAIL().unread(self.ctx.state, "main")]

    def test_the_unclaimed_ring_never_offers_a_spawn_beside_a_session(self):
        # 11:40 on 2026-10-14: rank 0 was told to spawn a lane that was working.
        self.assertEqual(self.claimcheck(("unclaimed", {"sessionId": "s-9abcdefg"}), ended=False), [])
        (text,) = self.claimcheck(("unclaimed", {"sessionId": "s-9abcdefg"}))
        self.assertIn("Do not spawn another", text)
        self.assertIn("harness ring dev_1 -", text)
        self.assertNotIn("harness spawn", text)
        self.assertTrue(any("harness spawn dev_1" in t for t in self.claimcheck((None, None))))

    def owes(self, state, marks=None, brief=None, gone=600, at=900):
        self.own("dev_1", "s-1")
        with mock.patch.multiple(
                hz, holder_state=lambda h, rows=None: (state, time.time() + at),
                last_write=lambda sid: time.time() - gone,
                open_marks=lambda c: marks if marks is not None else {"t": {"_node": "dev_1"}},
                load_brief=lambda c, t: (None, brief), startable=lambda c, k: [],
                node_running=lambda c, k, rows=None: (None, None),
                unanswered=lambda *a: None, unwoken=lambda *a: None,
                context_limits=lambda c, k: (None, None), stopped=lambda c, k: None,
                halted=lambda c: None):
            return [o[0] for o in hz.lead_owes(self.ctx, "dev")]

    def test_only_a_dead_session_is_an_orphan_and_a_parked_task_nags_nobody(self):
        self.assertEqual(self.owes("dead"), ["orphan"])
        self.assertEqual(self.owes("asleep", at=-60), [])    # a ring resumes it: nothing is owed
        long = -hz.ASLEEP_AFTER - 60
        self.assertEqual(self.owes("asleep", at=long), ["asleep"])      # but hours of it is said
        self.assertIn("harness ring dev_1 -", hz.owed_line("asleep", "dev_1", "t", 7200))
        self.assertEqual(self.owes("limited"), ["limit"])
        self.assertEqual(self.owes("live"), [])
        parked = {"wait": {"until": time.time() + 3600, "why": "until modules.py moves"}}
        self.assertEqual(self.owes("dead", brief=parked), [])           # log 162
        self.assertEqual(self.owes("asleep", at=long, brief=parked), [])
        self.assertEqual(self.owes("dead", brief={"wait": {"until": time.time() - 1}}), ["orphan"])
        line = hz.owed_line("orphan", "dev_1", "t", 600)
        self.assertIn("harness recycle dev_1", line)
        self.assertIn("add --force", line)
        self.assertIn('harness brief t --wait "<condition>"', line)
        self.assertIn("the ringer restarts it then", hz.owed_line("limit", "dev_1", "16:50", 0))

    def test_status_says_asleep_or_dead_and_shows_a_session_beside_a_stale_lock(self):
        self.own("dev", "s-dev")
        self.own("dev_1", "s-old")
        (self.ctx.dir / "locks" / "main.lock").write_text(json.dumps(
            {"node": "main", "session_id": "s-main", "ref": "s-main", "name": "p-main", "host": HOST}))
        states = {"s-dev": ("asleep", 0.0), "s-old": ("dead", 0.0), "s-main": ("live", None)}
        rows = [self.row("main", "s-main"), self.row("dev_1", "s-fresh"), self.row("main", "s-twin")]
        hz.start_take(self.ctx, "dev", "resume", "the ringer", "s-dev")
        out = io.StringIO()
        with mock.patch.object(hz, "Ctx", return_value=self.ctx), \
             mock.patch.multiple(
                 hz, read_roster=lambda p: None, agents_json=lambda *a: rows, live_rows=lambda r: r,
                 live_sessions=lambda: [], load_index=lambda *a, **k: self.idx,
                 holder_state=lambda h, rows=None: states[h["session_id"]],
                 is_stopped=lambda r: False, open_marks=lambda c: {}, open_waits=lambda c: {},
                 behind_seen=lambda *a, **k: None, context_size=lambda sid: 1000,
                 node_activity=lambda *a, **k: "", start_standing=lambda c, n, now=None: (
                     {"how": "resume", "by": "the ringer", "at": time.time()} if n == "dev" else None)), \
             redirect_stdout(out):
            try:
                hz.cmd_status(mock.Mock(roster=None))
            except Exception:
                pass                              # what follows the session table is not under test
        text = out.getvalue()
        line = lambda node: next(l for l in text.splitlines() if l.startswith(f"  {node} "))
        self.assertIn("asleep", line("dev"))
        self.assertIn("a ring resumes it", line("dev"))
        self.assertIn("DEAD", line("dev_1"))
        self.assertIn("stopped mid-turn", line("dev_1"))
        self.assertNotIn("gone", text)
        self.assertRegex(text, r"dev_1 +p-dev_1 +\[s-fresh\] +in the worktree, not claimed yet")
        self.assertRegex(text, r"main +p-main +\[s-twin\] +SECOND SESSION beside the holder "
                               r"— harness stop main --surplus")
        self.assertRegex(text, r"dev +a start is in flight \(resume by the ringer")

    def test_the_prompt_hook_tells_a_second_session_and_hands_it_nothing(self):
        self.own("dev", "s-1")
        hz.ring_inbox(self.ctx.state, "dev", "main", "for the holder only")
        (self.ctx.dir / "tree.json").write_text(json.dumps(self.ctx.tree))
        self.ctx.binding_path = self.ctx.tree_path = self.ctx.dir / "tree.json"
        self.ctx.me = "dev"
        out = io.StringIO()
        with mock.patch.object(hz, "hook_ctx", return_value=self.ctx), \
             mock.patch.object(hz, "QUIET", False), \
             mock.patch.object(hz, "holder_alive", return_value=True), \
             mock.patch.object(hz, "print_delta") as delta, \
             mock.patch.object(hz, "ensure_ringer"), \
             mock.patch.dict(os.environ, {"HARNESS_NODE": "dev", "CLAUDE_CODE_SESSION_ID": "s-2"}), \
             mock.patch("sys.stdin", io.StringIO(json.dumps({"session_id": "s-2"}))), \
             redirect_stdout(out), self.assertRaises(SystemExit):
            hz.cmd_hook_orient(mock.Mock())
        self.assertIn("harness: SECOND SESSION: dev is held by p-dev [s-1]", out.getvalue())
        self.assertNotIn("for the holder only", out.getvalue())
        delta.assert_not_called()
        self.assertEqual(len(hz.MAIL().unread(self.ctx.state, "dev")), 1)     # still the holder's

    def test_a_presented_task_with_no_note_says_so(self):
        # Log 165: a lead read "no comments" 17 s before the lane wrote its account.
        (self.ctx.dir / "marks").mkdir()
        (self.ctx.dir / "marks" / "t.json").write_text(json.dumps(
            {"_node": "dev_1", "_at": OLD, "_session": "s", "_presented_at": OLD}))
        out = io.StringIO()
        with mock.patch.object(hz, "Ctx", return_value=self.ctx), \
             mock.patch.object(hz, "load_brief", return_value=(None, None)), redirect_stdout(out):
            hz.cmd_note(mock.Mock(task="t", add=None))
        self.assertRegex(out.getvalue(), r"no comments: presented .* with no --note")

    def test_claude_is_named_claude_not_by_its_version_folder(self):
        kid = subprocess.Popen(["sleep", "30"])
        self.addCleanup(lambda: (kid.kill(), kid.wait()))
        real = Path.read_bytes

        def cmdline(self_):
            p = str(self_)
            if p == f"/proc/{kid.pid}/cmdline":
                return b"/home/u/.local/share/claude/versions/2.1.296\x00agents\x00--json"
            if p == "/proc/77/cmdline":
                return b"bash\x00-c\x00source /x/shell-snapshots/s.sh"
            return real(self_)
        with mock.patch.object(hz, "proc_children", return_value=({1: [77], 77: [kid.pid]}, {})), \
             mock.patch.object(Path, "read_bytes", cmdline), \
             mock.patch.object(Path, "read_text", lambda self_, *a, **k: (
                 "bash\n" if str(self_) == "/proc/77/comm" else "2.1.296\n")):
            self.assertEqual(hz.session_work({"pid": 1}), "claude")


if __name__ == "__main__":
    unittest.main()


class Ask(unittest.TestCase):
    """T17: asks are opened by leads, briefed by the intermediary, signed by the owner."""

    BRIEF = ("## Question\nShip X or Y?\n## Scope\nthe sample join: maps are its output.\n"
             "## Situation\nX ships the map.\n\nY waits a cycle.\n## Chain\nmain asked; owner set the cut.\n"
             "## Cause\nThe cut leaves room for one.\n## Harness\nno: the queue and briefs are clean.\n"
             "## Tried\nnothing; it is a choice.\n## Why you\nintent: scope is the owner's\n"
             "## Options\n- X: faster\n- Y: safer\n## Consequence\nthe map waits a cycle.\n"
             "## Checked\nbriefs/s1.json\nthe charter\nthe queue\nthe cut\n"
             "## Unknown\nnothing material\n## Recommendation\nX (dev)")


    def test_id_not_reused_after_accept(self):
        d = Path(tempfile.mkdtemp())
        (d / "asks").mkdir(); (d / "briefs").mkdir()
        (d / "briefs" / "t.json").write_text(json.dumps({"task": "t", "rulings": [{"id": "t-1"}]}))
        self.assertEqual(hz.ask_next_id(d, "t"), "t-2")
    def setUp(self):
        _v = mock.patch.object(hz, "ask_verify", return_value=[])
        _v.start(); self.addCleanup(_v.stop)
        self.ctx = FakeCtx({"main": None, "dev": "main", "dev_1": "dev"})
        (self.ctx.dir / "briefs").mkdir()
        self.bf = self.ctx.dir / "briefs" / "s1.json"
        self.bf.write_text(json.dumps({"task": "s1", "node": "dev_1", "text": "do it"}))
        self.err = mock.patch("sys.stderr", new_callable=io.StringIO)
        self.err.start()
        self.addCleanup(self.err.stop)

    def open(self, me="dev", sid="s" * 36, task="s1", q="Ship X or Y?"):
        return hz.ask_open(self.ctx, task, "intent", q, me, sid)

    def path(self, rec):
        return self.ctx.dir / "asks" / f"{rec['id']}.json"

    def test_lead_opens_member_refused_brief_required(self):
        r = self.open()
        self.assertEqual((r["id"], r["state"], r["node"]), ("s1-1", "asked", "dev_1"))
        self.assertEqual(self.open(me="main", q="Ship Z?")["id"], "s1-2")
        with self.assertRaises(SystemExit):
            self.open(me="dev_1", q="Ship W?")          # a lane, in a session
        self.assertEqual(self.open(me="dev_1", sid="", q="Ship V?")["asked_by"],
                         "dev_1 (operator)")

    def test_the_same_open_question_is_not_asked_twice(self):
        self.open()
        with self.assertRaises(SystemExit):
            self.open(me="main", q="ship x or y?")
        self.assertIn("already asked, and open: s1-1", sys.stderr.getvalue())
        with self.assertRaises(SystemExit):
            self.open(task="nope")                      # no brief
        with self.assertRaises(SystemExit):
            hz.ask_open(self.ctx, "s1", "intent", "x" * 201, "dev", "")

    def test_brief_validation_names_every_section(self):
        b, errs = hz.parse_ask_brief(self.BRIEF)
        self.assertEqual(errs, [])
        self.assertEqual(b["options"], ["X: faster", "Y: safer"])
        _, errs = hz.parse_ask_brief(self.BRIEF.replace("## Recommendation\nX (dev)", ""))
        self.assertEqual(errs, ["recommendation: missing"])
        self.assertEqual(b["situation"], "X ships the map.\n\nY waits a cycle.")
        self.assertIn("commands: missing", hz.parse_ask_brief(self.BRIEF, "action")[1])
        bad = (self.BRIEF.replace("Ship X or Y?", "q" * 350)
               .replace("- Y: safer", "")
               .replace("no: the queue", "the queue")
               .replace("the queue\nthe cut\n", ""))
        _, errs = hz.parse_ask_brief(bad)
        self.assertIn("question: 350 chars, cap 300", errs)
        self.assertTrue(any(e.startswith("checked: 2 line(s); at least 4") for e in errs))
        self.assertTrue(any(e.startswith("options: 1 item(s)") for e in errs))
        self.assertTrue(any(e.startswith("harness: start with yes or no") for e in errs))
        # out of scope is a complete answer in five sections
        oos = ("## Question\nStop two sessions?\n## Scope\nnone: harness upkeep, no feature.\n"
               "## Situation\nlanes stuck.\n## Chain\ndev to main to here.\n"
               "## Out of scope\nIt serves no charter feature; the loop is dev and main.")
        b, errs = hz.parse_ask_brief(oos, "action")
        self.assertEqual(errs, [])
        self.assertIn("out_of_scope", b)
        _, errs = hz.parse_ask_brief(self.BRIEF.replace("X: faster", "x" * 801))
        self.assertEqual(errs, ["options #1: 801 chars, cap 800"])

    def test_a_brief_may_carry_a_tldr_for_the_issues_list(self):
        self.assertNotIn("tldr", hz.parse_ask_brief(self.BRIEF)[0])      # optional
        with_it = self.BRIEF.replace("## Scope", "## TLDR\nShip the map now,\n  or wait?\n## Scope")
        b, errs = hz.parse_ask_brief(with_it)
        self.assertEqual((errs, b["tldr"]), ([], "Ship the map now, or wait?"))
        _, errs = hz.parse_ask_brief(self.BRIEF.replace("## Scope", "## TLDR\n" + "w" * 91 + "\n## Scope"))
        self.assertEqual(errs, ["tldr: 91 chars, cap 90"])
        _, errs = hz.parse_ask_brief(self.BRIEF.replace("## Scope", "## TLDR\n\n## Scope"))
        self.assertEqual(errs, ["tldr: empty (leave the section out instead)"])

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


class ScopeFrame(unittest.TestCase):
    """Owner, 2026-10-06: scope comes from the charter, then the docs, and is in
    every session's first prompt; every task traces to a charter feature."""

    CHARTER = {"description": {"text": "biblion joins papers to samples."},
               "features": {"the_sample_join": {"name": "the sample join", "text": "Follow each "
                                                "paper to its samples.", "seq": 1, "parent": None},
                            "sample_maps": {"name": "sample maps", "text": "Maps of them.",
                                            "seq": 1, "parent": "the_sample_join"}}}

    def setUp(self):
        self.ctx = FakeCtx({"main": None, "dev": "main", "dev_1": "dev"})
        self.ctx.repo = self.ctx.worktree = self.ctx.dir
        (self.ctx.dir / "charter.json").write_text(json.dumps(self.CHARTER))
        (self.ctx.dir / "briefs").mkdir()
        self.err = mock.patch("sys.stderr", new_callable=io.StringIO)
        self.err.start(); self.addCleanup(self.err.stop)

    def brief(self, *argv, me="dev"):
        self.ctx.me, self.ctx.branch = me, me
        with mock.patch.object(hz, "Ctx", return_value=self.ctx), \
             mock.patch.dict(os.environ, {"CLAUDE_CODE_SESSION_ID": "s" * 36}), \
             mock.patch("sys.argv", ["harness", "brief", *argv]), \
             redirect_stdout(io.StringIO()) as o:
            try:
                hz.main(); return 0, o.getvalue()
            except SystemExit as e:
                return e.code, o.getvalue()

    def test_the_scope_block_is_the_charter_in_full_then_the_docs(self):
        with mock.patch.object(hz, "doc_files", return_value=["README.md", "provenance/x/y.md"]):
            (self.ctx.dir / "README.md").write_text("# Read me first\nbody")
            b = hz.scope_block(self.ctx)
        self.assertIn("biblion joins papers to samples.", b)
        self.assertIn("1. **the sample join** — Follow each paper to its samples.", b)
        self.assertIn("   1.1 **sample maps** — Maps of them.", b)
        self.assertIn("- `README.md` — Read me first", b)
        self.assertNotIn("provenance/x/y.md", b)
        (self.ctx.dir / "charter.json").unlink()
        self.assertIn("No charter is written", hz.scope_block(self.ctx, docs=False))

    def test_every_first_prompt_carries_it(self):
        with mock.patch.object(hz, "context_limits", return_value=(None, None)):
            cmd = hz.launch_cmd(self.ctx, "dev_1", "p-dev_1", [], None, None, "go")
        self.assertIn("**the sample join**", cmd[-1])
        home = Path(tempfile.mkdtemp())
        (home / ".claude" / "skills" / "harness-intermediary").mkdir(parents=True)
        (home / ".claude" / "skills" / "harness-intermediary" / "SKILL.md").write_text("skill")
        (home / ".claude" / "skills" / "harness-documenter").mkdir(parents=True)
        (home / ".claude" / "skills" / "harness-documenter" / "SKILL.md").write_text("skill")
        with mock.patch.object(hz.Path, "home", return_value=home), \
             mock.patch.object(hz, "doc_files", return_value=[]):
            for f in (hz.intermediary_prompt(self.ctx.dir, str(self.ctx.repo)),
                      hz.documenter_prompt(self.ctx.dir, str(self.ctx.repo))):
                self.assertIn("**the sample join**", f.read_text())

    def test_a_new_brief_names_its_feature_or_is_refused(self):
        code, _ = self.brief("t1", "--for", "dev_1", "--write", "do it")
        self.assertNotEqual(code, 0)
        self.assertIn("names no charter feature", sys.stderr.getvalue())
        code, _ = self.brief("t1", "--for", "dev_1", "--feature", "nope", "--write", "do it")
        self.assertNotEqual(code, 0)
        code, _ = self.brief("t1", "--for", "dev_1", "--feature", "the sample join", "--write", "do it")
        self.assertEqual(code, 0)
        self.assertEqual(json.loads((self.ctx.dir / "briefs" / "t1.json").read_text())["feature"],
                         "the_sample_join")
        self.assertEqual(self.brief("t1", "--write", "redo it")[0], 0)        # a rewrite keeps it
        self.assertEqual(json.loads((self.ctx.dir / "briefs" / "t1.json").read_text())["feature"],
                         "the_sample_join")

    def test_a_stored_comment_ends_on_its_confirmation(self):
        """obs 107: a success that ended on the `--write` hint read as a refusal."""
        self.brief("t1", "--for", "dev_1", "--feature", "the sample join", "--write", "do it")
        code, out = self.brief("t1", "--comment", "kept scratch.db", me="dev_1")
        self.assertEqual(code, 0)
        lines = out.strip().splitlines()
        self.assertEqual(lines[-1], "added comment 1 to t1 (brief at revision 1)")
        self.assertFalse([l for l in lines if l.strip().startswith("harness brief")])
        rec = json.loads((self.ctx.dir / "briefs" / "t1.json").read_text())
        self.assertEqual(rec["comments"][0]["on_revision"], 1)

    def test_untraced_work_is_rank_0_s_until_mapped(self):
        (self.ctx.dir / "briefs" / "old.json").write_text(json.dumps(
            {"task": "old", "node": "dev_1", "text": "x"}))
        with mock.patch.object(hz, "task_state", return_value="briefed"), \
             mock.patch.object(hz, "lead_owes", return_value=[]), \
             mock.patch.object(hz, "rank0_owes", return_value=[]):
            items = hz.queue_items(self.ctx, "main")
            self.assertIn("untraced:old", items)
            self.assertTrue(hz.is_debt("untraced:old"))
            self.assertNotEqual(self.brief("old", "--feature", "sample maps", me="dev_1")[0], 0)
            self.assertEqual(self.brief("old", "--feature", "sample maps", me="main")[0], 0)
            self.assertNotIn("untraced:old", hz.queue_items(self.ctx, "main"))


class Halt(unittest.TestCase):
    """Owner, 2026-10-06: the owner can halt the whole tree when work leaves scope."""

    def setUp(self):
        self.ctx = FakeCtx({"main": None, "dev": "main", "dev_1": "dev"})
        self.ctx.require_enrolled = lambda: None
        self.err = mock.patch("sys.stderr", new_callable=io.StringIO)
        self.err.start(); self.addCleanup(self.err.stop)

    def halt(self, sid=None, resume=False, why="drifted"):
        env = {"CLAUDE_CODE_SESSION_ID": sid} if sid else {}
        with mock.patch.object(hz, "Ctx", return_value=self.ctx), \
             mock.patch.dict(os.environ, env, clear=False), redirect_stdout(io.StringIO()):
            if not sid:
                os.environ.pop("CLAUDE_CODE_SESSION_ID", None)
            hz.cmd_halt(mock.Mock(resume=resume, why=why, ask=None))

    def test_only_the_owner_halts_and_every_node_is_told(self):
        with self.assertRaises(SystemExit):
            self.halt(sid="s" * 36)
        self.halt()
        self.assertEqual(hz.halted(self.ctx)["why"], "drifted")
        for n in ("main", "dev", "dev_1"):
            self.assertTrue(list((self.ctx.dir / "doorbell" / n / "inbox").glob("*.json")))
        with self.assertRaises(SystemExit):
            hz.refuse_if_halted(self.ctx, "spawning")
        self.assertIn("halted the tree", sys.stderr.getvalue())
        self.assertIn("halt:", "".join(hz.queue_items(self.ctx, "dev_1")))
        with mock.patch.object(hz, "testq_jobs", return_value=[]):
            self.halt(resume=True)
        self.assertIsNone(hz.halted(self.ctx))
        hz.refuse_if_halted(self.ctx, "spawning")                     # no longer refused

    def test_the_runner_starts_nothing_while_halted(self):
        self.halt()
        c = hz.ProjCtx(self.ctx.dir, self.ctx.dir)
        with mock.patch.object(hz, "testq_recover"), \
             mock.patch.object(hz, "testq_jobs", side_effect=AssertionError("picked a job")), \
             mock.patch("signal.signal"), redirect_stdout(io.StringIO()) as o:
            hz._testd_loop(c)
        self.assertIn("halted; runner exits", o.getvalue())

    def test_the_stop_hook_says_it_once_per_halt(self):
        self.halt()
        self.ctx.tree_path = self.ctx.dir / "tree.json"; self.ctx.tree_path.write_text("{}")
        self.ctx.binding_path = self.ctx.dir / "binding.json"; self.ctx.binding_path.write_text("{}")
        self.ctx.tree_path.write_text(json.dumps(self.ctx.tree))
        def stop():
            o = io.StringIO()
            with mock.patch.object(hz, "Ctx", return_value=self.ctx), \
                 mock.patch.object(hz, "hook_ctx", return_value=self.ctx), \
                 mock.patch.object(hz, "git", return_value=(0, "", "")), \
                 mock.patch.object(hz, "docs_apply_step"), \
                 mock.patch.object(hz, "bell_armed", return_value={"pid": 1}), \
                 mock.patch.object(hz, "lead_owes", return_value=[]), \
                 mock.patch.object(hz, "unreported", return_value=[]), \
                 mock.patch.object(hz, "turn_texts", return_value=[]), \
                 mock.patch("sys.stdin", io.StringIO(json.dumps({"session_id": "s1"}))), \
                 redirect_stdout(o):
                for k in list(hz.MAIL().take(self.ctx.state, "dev_1", "t")):
                    pass
                hz.cmd_hook_stop(mock.Mock())
            return o.getvalue()
        self.ctx.me = "dev_1"
        self.assertIn("halted the tree", stop())
        self.assertEqual(stop(), "")

    def test_a_ping_pong_between_two_nodes_reads_as_a_loop(self):
        at = time.strftime("%Y-%m-%dT%H:%M:%S%z")
        for frm, to in (("dev", "main"), ("main", "dev")):
            d = self.ctx.dir / "doorbell" / to
            d.mkdir(parents=True, exist_ok=True)
            (d / "delivered.jsonl").write_text("\n".join(
                json.dumps({"from": frm, "text": "x", "at": at}) for _ in range(5)) + "\n")
        self.assertEqual(hz.drift_loops(self.ctx), [("dev", "main", 5, 5)])
        with mock.patch.object(hz, "lead_owes", return_value=[]), \
             mock.patch.object(hz, "rank0_owes", return_value=[]), \
             mock.patch.object(hz, "untraced_briefs", return_value=[]):
            self.assertTrue(any(k.startswith("loop:dev:main") for k in hz.queue_items(self.ctx, "main")))


class AskChain(unittest.TestCase):
    """Owner, 2026-10-06: every ask carries how it reached the owner, read off the
    transcripts back to the owner's own words."""

    def test_the_chain_runs_from_the_owner_through_each_session(self):
        ctx = FakeCtx({"main": None, "dev": "main"})
        proj = Path(tempfile.mkdtemp()) / "p"
        proj.mkdir(parents=True)
        A = lambda *c: {"type": "assistant", "timestamp": "2026-10-06T09:39:00Z",
                        "message": {"content": list(c)}}
        U = lambda t, ts="2026-10-06T09:37:00Z": {"type": "user", "timestamp": ts,
                                                   "message": {"content": t}}
        txt = lambda t: {"type": "text", "text": t}
        tool = lambda n, i: {"type": "tool_use", "name": n, "input": i}
        res = {"type": "user", "message": {"content": [{"type": "tool_result", "content": "ok"}]}}
        report = "dev: incident, the hook and spawn disagree about dev_1"
        (proj / "sa.jsonl").write_text("\n".join(json.dumps(r) for r in (
            U("always tell main about harness errors"),
            A(txt("Checking it."), tool("Bash", {"command": "harness spawn dev_1 --dry-run"})), res,
            A(txt("Reporting it to main."), tool("SendMessage", {"to": "p-main", "message": report})),
            res)))
        (proj / "sb.jsonl").write_text("\n".join(json.dumps(r) for r in (
            U('<cross-session-message from="uds:/r/1.sock" from-name="p-dev">' + report +
              '</cross-session-message>', "2026-10-06T09:39:30Z"),
            A(txt("Both clean. Filing it."), tool("Bash", {"command": "harness ask owner --kind action"})))))
        for n, sid in (("dev", "sa"), ("main", "sb")):
            ctx.lock_path(n).parent.mkdir(parents=True, exist_ok=True)
            ctx.lock_path(n).write_text(json.dumps({"node": n, "session_id": sid}))
        with mock.patch.object(hz, "PROJECTS", proj.parent), \
             mock.patch.object(hz, "agents_json", return_value=[]), \
             mock.patch.object(hz, "open_marks", return_value={"t1": {"_node": "dev"}}), \
             mock.patch.object(hz, "load_brief", return_value=(None, {"task": "t1"})):
            ch = hz.ask_chain(ctx, "sb")
        self.assertEqual([(h["node"], h["from"]) for h in ch], [("dev", "owner"), ("main", "p-dev")])
        self.assertEqual(ch[0]["received"], "always tell main about harness errors")
        self.assertIn("hook and spawn disagree", ch[1]["received"])
        self.assertEqual(ch[1]["concluded"], "Both clean. Filing it.")
        self.assertTrue(ch[0]["untraced"])                         # t1 serves no feature
        lines = "\n".join(hz.render_chain(ch))
        self.assertIn("UNTRACED", lines)
        self.assertIn('received from owner: "always tell main', lines)


class AskEvidence2(unittest.TestCase):
    """Owner, 2026-10-06: the brief's evidence is checked, so it can only be
    written by looking."""

    def setUp(self):
        import subprocess as sp
        self.root = Path(tempfile.mkdtemp())
        self.repo = self.root / "repo"; self.repo.mkdir()
        g = lambda *a: sp.run(["git", "-C", str(self.repo), *a], capture_output=True, text=True)
        g("init", "-q"); g("config", "user.email", "t@t"); g("config", "user.name", "t")
        (self.repo / "loader.py").write_text("a\nb\nc\n")
        g("add", "-A"); g("commit", "-qm", "x")
        self.sha = g("rev-parse", "--short", "HEAD").stdout.strip()
        self.pdir = self.root / "state"; (self.pdir / "asks").mkdir(parents=True)
        (self.pdir / "binding.json").write_text(json.dumps({"repo": str(self.repo)}))
        self.path = self.pdir / "asks" / "owner-7.json"
        self.rec = {"id": "owner-7", "kind": "action", "state": "asked",
                    "chain": [{"node": "dev", "received": "the hook and spawn disagree about dev_1"},
                              {"node": "main", "received": "x"}],
                    "thread": []}
        self.obs = mock.patch.object(hz, "HOME_STATE", self.root)
        self.obs.start(); self.addCleanup(self.obs.stop)
        (self.root / "OBSERVATIONS.md").write_text("### 105. Two predicates for running\n")
        e = mock.patch.dict(os.environ, {}); e.start(); self.addCleanup(e.stop)
        os.environ.pop("CLAUDE_CODE_SESSION_ID", None)     # the test runner's own session

    def brief(self, checked, harness="yes: obs 105", cause="x"):
        return {"scope": "s", "cause": cause, "harness": harness, "checked": checked}

    def test_references_must_exist(self):
        good = "\n".join(["loader.py:2 holds the reader", f"`{self.sha}` is the reviewed commit",
                          "obs 105 names it", "the queue"])
        self.rec["thread"] = [{"to": "dev", "text": "which commit?"}]
        self.assertEqual(hz.ask_verify(self.path, self.rec, self.brief(good)), [])
        bad = "\n".join(["loader.py:99 holds it", "`deadbee` is it", "obs 999", "x"])
        errs = hz.ask_verify(self.path, self.rec, self.brief(bad))
        self.assertTrue(any("loader.py:99 is not there" in e for e in errs))
        self.assertTrue(any("`deadbee` is no commit" in e for e in errs))
        self.assertTrue(any("log entry 999 doesn't exist" in e for e in errs))
        self.assertTrue(any(e.startswith("checked: 0 line(s)") for e in errs))

    def test_quotes_must_be_read_and_yes_needs_a_place(self):
        self.rec["thread"] = [{"to": "dev", "text": "?"}]
        b = self.brief("\n".join(['dev said "the hook and spawn disagree about dev_1"',
                                  "loader.py:1", "a", "b"]),
                       harness="yes, the harness is at fault",
                       cause='"spawn is never consulted by the orientation hook here"')
        errs = hz.ask_verify(self.path, self.rec, b)
        self.assertTrue(any("cause: the quote" in e for e in errs))           # invented
        self.assertFalse(any("checked: the quote" in e for e in errs))       # read on the chain
        self.assertTrue(any("harness: yes needs" in e for e in errs))

    def test_a_multi_session_chain_needs_a_question_first(self):
        b = self.brief("\n".join(["loader.py:1", "loader.py:2", "a", "b"]))
        self.assertTrue(any("asked none of them" in e for e in hz.ask_verify(self.path, self.rec, b)))
        self.rec["thread"] = [{"by": "intermediary", "to": "dev", "text": "why occupied?"}]
        self.assertEqual(hz.ask_verify(self.path, self.rec, b), [])

    def test_drop_marks_the_untraced_task_and_tells_its_node_and_lead(self):
        repo = self.repo
        (repo / ".harness").mkdir()
        (repo / ".harness" / "tree.json").write_text(json.dumps(
            {"nodes": {"main": {}, "dev": {"parent": "main"}, "dev_1": {"parent": "dev"}}}))
        (self.pdir / "briefs").mkdir()
        (self.pdir / "briefs" / "fix_it.json").write_text(json.dumps({"task": "fix-it", "node": "dev_1"}))
        self.rec.update(task="owner", chain=[{"node": "dev_1", "task": "fix-it", "untraced": True}])
        self.path.write_text(json.dumps(self.rec))
        task, told = hz.ask_drop(self.pdir, self.path, self.rec, "harness upkeep, no feature")
        self.assertEqual((task, told), ("fix-it", ["dev_1", "dev"]))
        b = json.loads((self.pdir / "briefs" / "fix_it.json").read_text())
        self.assertEqual(b["out_of_scope"]["ask"], "owner-7")
        self.assertEqual(json.loads(self.path.read_text())["state"], "rejected")


class Log106(unittest.TestCase):
    """Log 106: finding-born work approved at rank 0 gets a carrier brief at
    every level between the lane and rank 0, so each lead can present it."""

    def setUp(self):
        self.ctx = FakeCtx({"main": None, "dev": "main", "dev_tests": "dev",
                            "dev_tests_1": "dev_tests"})
        nodes = self.ctx.tree["nodes"]

        def rank(n, r=0):
            while nodes[n].get("parent"):
                n, r = nodes[n]["parent"], r + 1
            return r
        self.ctx.rank = rank
        (self.ctx.dir / "briefs").mkdir()

    def brief(self, task, **kw):
        b = {"task": task, "node": "dev_tests_1", "text": "t", "from_finding": "typing-gap"}
        b.update(kw)
        (self.ctx.dir / "briefs" / f"{task}.json").write_text(json.dumps(b))
        return b

    def load(self, task):
        p = self.ctx.dir / "briefs" / f"{task}.json"
        return json.loads(p.read_text()) if p.exists() else None

    def carriers(self, b, decider="main"):
        with mock.patch.object(hz, "queue", return_value=[]):
            return hz.finding_carriers(self.ctx, b["task"], b, decider)

    def test_each_level_below_rank_0_gets_a_carrier_that_waits_on_the_one_below(self):
        made = self.carriers(self.brief("dtf"))
        self.assertEqual(made, [("dtf.up-dev_tests", "dev_tests"), ("dtf.up-dev", "dev")])
        lo, hi = self.load("dtf.up-dev_tests"), self.load("dtf.up-dev")
        self.assertEqual((lo["node"], lo["after"], lo["carries"]), ("dev_tests", ["dtf"], "dtf"))
        self.assertEqual((hi["node"], hi["after"]), ("dev", ["dtf.up-dev_tests"]))
        self.assertEqual(hi["approval"]["state"], "approved")
        self.assertFalse(hz.awaiting(hi))
        rung = sorted(p.parent.parent.name for p in self.ctx.dir.glob("doorbell/*/inbox/*.json"))
        self.assertEqual(rung, ["dev", "dev_tests"])

    def test_running_again_writes_nothing_new(self):
        b = self.brief("dtf")
        self.carriers(b)
        self.assertEqual(self.carriers(b), [])

    def test_near_rank_0_one_carrier_at_rank_0_none(self):
        self.assertEqual(self.carriers(self.brief("a", node="dev_tests")),
                         [("a.up-dev", "dev")])
        self.assertEqual(self.carriers(self.brief("b", node="dev")), [])

    def test_a_carrier_opens_only_once_the_task_below_is_signed_off(self):
        self.carriers(self.brief("dtf"))
        lo = self.load("dtf.up-dev_tests")
        (self.ctx.dir / "marks").mkdir()
        m = self.ctx.dir / "marks" / "dtf.json"
        m.write_text(json.dumps({"_node": "dev_tests_1", "_task": "dtf",
                                 "_presented_at": "2026-10-08T13:00:00"}))
        self.assertTrue(hz.waits_on(self.ctx, lo))
        m.write_text(json.dumps({"_node": "dev_tests_1", "_task": "dtf",
                                 "_presented_at": "2026-10-08T13:00:00",
                                 "_closed_at": "2026-10-08T13:05:00"}))
        self.assertEqual(hz.waits_on(self.ctx, lo), [])

    def test_a_part_of_a_segment_or_a_plain_brief_gets_none(self):
        self.assertEqual(self.carriers(self.brief("p", **{"from": "seg"})), [])
        self.assertEqual(self.carriers(self.brief("q", from_finding="")), [])


class Log105(unittest.TestCase):
    """Log 105: one answer for "running", and a finished lane's lingering session
    never deadlocks its lead."""

    def setUp(self):
        self.ctx = FakeCtx({"main": None, "dev": "main", "dev_2": "dev"})
        self.row = {"cwd": "/w/dev_2", "sessionId": "s2", "name": "p-dev_2", "pid": 7}
        self.idx = {"nodes": {"dev_2": {"worktree": "/w/dev_2"}}}

    def test_node_running_reads_the_roster_when_nothing_is_claimed(self):
        with mock.patch.object(hz, "load_index", return_value=self.idx):
            self.assertEqual(hz.node_running(self.ctx, "dev_2", [self.row]), ("unclaimed", self.row))
            self.assertEqual(hz.node_running(self.ctx, "dev_2", []), (None, None))

    def test_finished_and_released_or_still_working(self):
        with mock.patch.object(hz, "open_marks", return_value={"t": {"_node": "dev_2", "_presented_at": "x"}}):
            self.assertTrue(hz.finished_released(self.ctx, "dev_2", [self.row]))
        with mock.patch.object(hz, "open_marks", return_value={"t": {"_node": "dev_2"}}):
            self.assertFalse(hz.finished_released(self.ctx, "dev_2", [self.row]))   # work in hand
        self.ctx.lock_path("dev_2").parent.mkdir(parents=True, exist_ok=True)
        self.ctx.lock_path("dev_2").write_text(json.dumps({"session_id": "s2"}))
        with mock.patch.object(hz, "open_marks", return_value={}):
            self.assertFalse(hz.finished_released(self.ctx, "dev_2", [self.row]))   # claimed

    def test_the_lead_is_never_told_to_spawn_an_occupied_child(self):
        q = [{"task": "next", "written_at": OLD}]
        with mock.patch.object(hz, "load_index", return_value=self.idx), \
             mock.patch.object(hz, "cached_roster", return_value=[self.row]), \
             mock.patch.object(hz, "startable", side_effect=lambda c, k: q if k == "dev_2" else []), \
             mock.patch.object(hz, "open_marks", return_value={}), \
             mock.patch.object(hz, "context_limits", return_value=(None, None)):
            owed = hz.lead_owes(self.ctx, "dev")
        self.assertIn("lingering", [o[0] for o in owed])
        self.assertNotIn("down", [o[0] for o in owed])
        line = hz.owed_line(*[o for o in owed if o[0] == "lingering"][0])
        self.assertIn("harness integrate dev_2 ends it", line)


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
                                    side_effect=lambda pd, *r: Path(pd) / "intermediary" / "prompt.md")):
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

    def test_the_issues_list_knows_when_each_item_last_moved_and_who_moved_it(self):
        gp = Path(__file__).resolve().parents[1] / "bin" / "harness-gui"
        ld = importlib.machinery.SourceFileLoader("harness_gui", str(gp))
        gui = importlib.util.module_from_spec(importlib.util.spec_from_loader("harness_gui", ld))
        ld.exec_module(gui)
        t = lambda m: time.strftime("%Y-%m-%dT%H:%M:%S%z", time.localtime(time.time() - m * 60))
        r = {"asked_at": t(300), "asker_node": "dev",
             "thread": [{"at": t(200), "by": "intermediary"}, {"at": t(30), "by": "owner"}],
             "history": [{"at": t(90), "by": "intermediary", "what": "briefed"}, "junk"]}
        a = gui.ask_activity(r)
        self.assertEqual((a["last_by"], a["active"]), ("owner", "30m"))
        self.assertAlmostEqual(a["active_at"], time.time() - 1800, delta=5)
        self.assertEqual(gui.ask_activity({"asked_at": t(5), "asked_by": "s1"})["last_by"], "s1")
        self.assertIsNone(gui.ask_activity({})["active_at"])

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
        _v = mock.patch.object(hz, "ask_verify", return_value=[])
        _v.start(); self.addCleanup(_v.stop)
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
        # A fresh question each time: the same open question is refused.
        self.n = getattr(self, "n", 0) + 1
        r = hz.ask_open(self.ctx, "s1", "intent", f"Ship X or Y ({self.n})?", "dev", "")
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
                         {"kind": "reply", "on": "", "said": "", "messaged": False,
                          "opener": ""})

    def test_waiting_means_it_messaged_someone_else(self):
        # Owner, 2026-10-06: waiting is having messaged a node for an answer.
        msg = '<cross-session-message from="uds:/r/9.sock" from-name="proj-dev">hi'
        send = lambda to: {"type": "tool_use", "name": "SendMessage",
                           "input": {"to": to, "summary": "q"}}
        res = {"type": "user", "message": {"content": [{"type": "tool_result"}]}}
        # a turn that ended without a message is at rest, whoever opened it
        self.assertIsNone(hz.stop_wait_on(self.run_(self.U(msg), self.A(self.TXT), self.END)))
        note = "<task-notification><status>completed</status></task-notification>"
        st = self.run_(self.U(note), self.A(self.TXT), self.END)
        self.assertIsNone(hz.stop_wait_on(st))
        self.assertEqual(st["on"], "")
        # answering whoever opened the turn is not waiting on them
        self.assertIsNone(hz.stop_wait_on(
            self.run_(self.U(msg), self.A(send("proj-dev")), res, self.A(self.TXT), self.END)))
        # asking someone else is
        self.assertEqual(hz.stop_wait_on(
            self.run_(self.U(msg), self.A(send("proj-dev_1")), res, self.A(self.TXT), self.END)),
            "proj-dev_1")

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
            got = {r["sessionId"]: why for r, why in hz.ended_sessions(ctx, rows, keep=0)}
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
             mock.patch.object(hz, "ENDED_NAG", 1), mock.patch.object(hz, "SESSIONS_KEEP", 0):
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

    def test_gaps_rank_whole_docs_by_importance_times_trouble(self):
        # Owner, 2026-10-06: a run is one whole doc, and the most-read doc with
        # something untrue in it comes before a big one nobody reads.
        clean = {"paths": [], "links": [], "functions": [], "history": []}
        d = lambda **k: dict({"words": 900, "reads": 0, "writes": 0, "pointers_in": 0,
                              "cited": 0, "idle_days": 30, "check": clean,
                              "verified": {"sha": "a", "changed": 0}}, **k)
        snap = {"budget": 100, "claude_md": 400, "transcripts": 50, "reach": {},
                "docs": {"CLAUDE.md": d(),
                         "old.md": d(verified=None),
                         "huge.md": d(words=47000, reads=2, verified=None),
                         "spine.md": d(reads=40, pointers_in=30,
                                       check=dict(clean, paths=[(3, "gone.py")])),
                         "fine.md": d(reads=9, pointers_in=1),
                         "provenance/x/y.md": d(verified=None)}}
        g = {x["doc"]: x for x in hz.docs_gaps(snap)}
        order = [x["doc"] for x in hz.docs_gaps(snap)]
        self.assertEqual(order[:2], ["CLAUDE.md", "spine.md"])     # read by all; broken path
        self.assertLess(order.index("spine.md"), order.index("huge.md"))
        self.assertIn("never checked against the code", g["huge.md"]["why"])
        self.assertIn("1 path(s) or link(s) not there", g["spine.md"]["why"])
        self.assertTrue(g["old.md"]["stale"]) and self.assertEqual(order[-1], "old.md")
        self.assertNotIn("fine.md", g)                            # checked, nothing wrong
        self.assertNotIn("provenance/x/y.md", g)                  # history is meant to be there


class DocTruth(unittest.TestCase):
    """The documenter checks that a doc's content is there and current, a run
    is one whole doc, and scope conflicts go to the owner (owner, 2026-10-06)."""

    def setUp(self):
        import subprocess as sp
        self.repo = Path(tempfile.mkdtemp())
        (self.repo / "src").mkdir()
        (self.repo / "src" / "app.py").write_text("def load_rows():\n    pass\n")
        (self.repo / "docs").mkdir()
        (self.repo / "docs" / "B.md").write_text("# Intro\n## Load path\ntext\n")
        (self.repo / "A.md").write_text(
            "# A\n"
            "Rows come from `src/app.py` via `load_rows()`.\n"           # 2: fine
            "The old `src/gone.py` and `parse_all()` did it.\n"          # 3: both missing
            "See [load](docs/B.md#load-path) and [x](docs/B.md#nope).\n"  # 4: one bad anchor
            "Branch `fix/writer-oa` and the bare `app.py` are fine.\n"    # 5: not paths / suffix
            "Measured 2026-09-01, superseded by the new loader.\n")      # 6: history
        for c in (["init", "-q"], ["add", "-A"],
                  ["-c", "user.email=t@t", "-c", "user.name=t", "commit", "-qm", "x"]):
            sp.run(["git", "-C", str(self.repo)] + c, check=True)
        hz._TRACKED.clear()
        self.ctx = FakeCtx({"main": None})
        self.ctx.repo = self.repo

    def check(self):
        texts = {"A.md": (self.repo / "A.md").read_text()}
        return hz.doc_check(self.ctx, "A.md", texts["A.md"], texts,
                            hz.doc_check_symbols(self.ctx, texts))

    def test_names_that_are_not_there(self):
        ck = self.check()
        self.assertEqual(ck["paths"], [(3, "src/gone.py")])
        self.assertEqual(ck["functions"], [(3, "parse_all()")])
        self.assertEqual(ck["links"], [(4, "docs/B.md#nope")])
        self.assertEqual(ck["history"], [6])

    def test_another_repo_the_docs_describe(self):
        other = Path(tempfile.mkdtemp())
        (other / "src").mkdir()
        (other / "src" / "gone.py").write_text("")
        import subprocess as sp
        for c in (["init", "-q"], ["add", "-A"],
                  ["-c", "user.email=t@t", "-c", "user.name=t", "commit", "-qm", "x"]):
            sp.run(["git", "-C", str(other)] + c, check=True)
        (self.repo / ".harness").mkdir()
        (self.repo / ".harness" / "manifest.json").write_text(
            json.dumps({"doc_sources": [str(other)]}))
        self.assertEqual(self.check()["paths"], [])

    def test_verified_records_the_commit_and_code_changes_make_it_due(self):
        with mock.patch.object(hz, "Ctx", return_value=self.ctx), \
             redirect_stdout(io.StringIO()) as out:
            hz.cmd_docs(mock.Mock(verb="verified", args=["A.md", "6 sections; 2 fixed"]))
        self.assertIn("checked against the code at", out.getvalue())
        v = hz.docs_verified(self.ctx)["A.md"]
        code = hz.doc_code_paths(self.ctx, (self.repo / "A.md").read_text())
        self.assertEqual(code, ["src/app.py"])
        self.assertEqual(hz.doc_changed_since(self.ctx, v["sha"], code), 0)
        (self.repo / "src" / "app.py").write_text("def load_rows():\n    return 1\n")
        import subprocess as sp
        sp.run(["git", "-C", str(self.repo), "-c", "user.email=t@t", "-c", "user.name=t",
                "commit", "-qam", "y"], check=True)
        self.assertEqual(hz.doc_changed_since(self.ctx, v["sha"], code), 1)
        with mock.patch.object(hz, "Ctx", return_value=self.ctx), \
             self.assertRaises(SystemExit), mock.patch("sys.stderr", new_callable=io.StringIO):
            hz.cmd_docs(mock.Mock(verb="verified", args=["A.md"]))         # says nothing

    def test_begin_takes_one_doc_and_names_it(self):
        with mock.patch.object(hz, "Ctx", return_value=self.ctx), \
             mock.patch.object(hz, "doc_files", return_value=["A.md", "docs/B.md"]), \
             redirect_stdout(io.StringIO()) as out:
            hz.cmd_docs(mock.Mock(verb="begin", args=["A.md"]))
        self.assertIn("line 3     path not there: src/gone.py", out.getvalue())
        self.assertIn("this run is A.md", out.getvalue())
        cur = json.loads((hz.docs_dir(self.ctx) / "current.json").read_text())
        self.assertEqual(cur["doc"], "A.md")
        with mock.patch.object(hz, "Ctx", return_value=self.ctx), \
             mock.patch.object(hz, "doc_files", return_value=["A.md", "docs/B.md"]), \
             self.assertRaises(SystemExit), mock.patch("sys.stderr", new_callable=io.StringIO):
            hz.cmd_docs(mock.Mock(verb="begin", args=["A.md", "docs/B.md"]))

    SNAP = {"gaps": [{"doc": "CLAUDE.md", "trouble": 50, "stale": False, "reads": 292},
                     {"doc": "A.md", "trouble": 5, "stale": False, "reads": 0},
                     {"doc": "docs/B.md", "trouble": 0, "stale": False, "reads": 0},
                     {"doc": "old.md", "trouble": 9, "stale": True, "reads": 0}]}

    def test_auto_draws_at_random_and_rests_recent_docs(self):
        # Owner, 2026-10-09: runs took CLAUDE.md 21 times in 32.
        rng = mock.Mock(choices=lambda pool, weights: (self.seen.append(
            ([g["doc"] for g in pool], weights)) or [pool[-1]]))
        self.seen = []
        self.assertEqual(hz.docs_pick(self.ctx, self.SNAP, rng), ("A.md", 2))
        pool, w = self.seen[-1]
        self.assertEqual(pool, ["CLAUDE.md", "A.md"])      # no stale, no trouble-free doc
        self.assertLess(w[0] / w[1], 3)                     # reads play no part; flat weights
        with open(hz.docs_dir(self.ctx) / "begun.jsonl", "a") as fh:
            fh.write(json.dumps({"doc": "CLAUDE.md"}) + "\n")
        self.assertEqual(hz.docs_pick(self.ctx, self.SNAP, rng), ("A.md", 1))
        with open(hz.docs_dir(self.ctx) / "begun.jsonl", "a") as fh:
            fh.write(json.dumps({"doc": "A.md"}) + "\n")
        self.assertEqual(hz.docs_pick(self.ctx, self.SNAP, rng)[1], 2)  # all rested: all back

    def test_plans_are_not_the_documenters(self):
        # Owner, 2026-10-11: plans aren't documentation in the normal sense.
        self.assertEqual(hz.documenter_skip(self.ctx), ["plans/**"])       # no manifest key
        self.assertEqual(hz.doc_skipped("plans/enrich/ENRICH-MAP.md", ["plans/**"]), "plans/**")
        self.assertEqual(hz.doc_skipped("plans/PLAN.md", ["plans/**"]), "plans/**")
        self.assertIsNone(hz.doc_skipped("design/plans.md", ["plans/**"]))
        self.assertIsNone(hz.doc_skipped("plans.md", ["plans/**"]))
        row = {"words": 10, "reads": 9, "pointers_in": 0, "pointers_out": 0, "cited": 0,
               "idle_days": 0, "check": {"paths": [(1, "x")]}, "verified": None}
        snap = {"docs": {"plans/PLAN.md": dict(row), "design/D.md": dict(row)},
                "skip": ["plans/**"]}
        self.assertEqual([g["doc"] for g in hz.docs_gaps(snap)], ["design/D.md"])
        # The project's own list replaces the default; an empty one skips nothing.
        man = self.repo / ".harness" / "manifest.json"
        man.parent.mkdir(exist_ok=True)
        old = man.read_text() if man.exists() else None
        self.addCleanup(lambda: man.write_text(old) if old is not None else man.unlink())
        man.write_text(json.dumps({"documenter_skip": []}))
        self.assertEqual(hz.documenter_skip(self.ctx), [])
        man.write_text(json.dumps({"documenter_skip": ["design/**", "NOTES.md"]}))
        self.assertEqual(hz.doc_skipped("NOTES.md", hz.documenter_skip(self.ctx)), "NOTES.md")

    def test_a_doc_that_needs_nothing_is_skipped_and_another_drawn(self):
        env = {"CLAUDE_CODE_SESSION_ID": "s" * 36}
        def skip(*why):
            with mock.patch.object(hz, "Ctx", return_value=self.ctx), \
                 mock.patch.object(hz, "docs_pick", return_value=("docs/B.md", 3)), \
                 mock.patch.dict(os.environ, env), redirect_stdout(io.StringIO()) as out:
                hz.cmd_docs(mock.Mock(verb="skip", args=list(why)))
            return out.getvalue()
        with mock.patch.object(hz, "Ctx", return_value=self.ctx), \
             mock.patch.dict(os.environ, env), \
             self.assertRaises(SystemExit), mock.patch("sys.stderr", new_callable=io.StringIO):
            hz.cmd_docs(mock.Mock(verb="skip", args=["fine"]))           # nothing begun
        for k in range(3):
            (hz.docs_dir(self.ctx) / "current.json").write_text(json.dumps({"doc": "A.md"}))
            out = skip("every section matches the code")
            self.assertIn("skipped A.md", out)
            if k < 2:
                self.assertIn("your next doc: docs/B.md", out)
        self.assertIn("end the run", out)                                 # three is the cap
        self.assertIn("nothing to change", hz.docs_verified(self.ctx)["A.md"]["note"])
        self.assertFalse((hz.docs_dir(self.ctx) / "current.json").exists())
        self.assertEqual(sum(1 for e in hz.docs_ledger(self.ctx) if e.get("skipped")), 3)

    def test_no_automatic_runs(self):
        with mock.patch.object(hz, "docs_trigger", return_value=True) as tr, \
             mock.patch.object(hz, "docs_pending", return_value=[]):
            self.assertFalse(hz.docs_apply_step(self.ctx, "main"))
        tr.assert_not_called()

    def test_scope_is_an_ask_kind_on_opus(self):
        self.assertIn("scope", hz.ASK_KINDS)
        self.assertEqual(hz.ITEM_MODEL["scope"], ("opus", "high"))


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
            cmd = hz.documenter_cmd(pdir, str(self.ctx.repo), "schema/SCHEMA.md")
        self.assertEqual(cmd[:4], ["claude", "--bg", "-n", f"harness-documenter-{self.ctx.repo.name}"])
        self.assertIn("--restricted", cmd)
        env = json.loads(cmd[cmd.index("--settings") + 1])["env"]
        self.assertEqual((env["HARNESS_DOCUMENTER"], env["HARNESS_DOCUMENTER_JOB"]),
                         ("1", "schema/SCHEMA.md"))
        self.assertIn("one document, whole: schema/SCHEMA.md", cmd[-1])
        allow = cmd[cmd.index("--allowedTools") + 1:cmd.index("--permission-mode")]
        self.assertIn("Bash(harness pairs submit *)", allow)
        self.assertNotIn("Bash(harness pairs *)", allow)                 # never apply
        # Writes only its own batch files: a heredoc'd batch was denied live.
        bd = home / ".local" / "state" / "harness" / pdir.name / "batches"
        self.assertEqual([a for a in allow if a.startswith(("Write", "Edit"))],
                         [f"Write(/{bd}/**)", f"Edit(/{bd}/**)"])            # outside ~/.claude
        self.assertEqual(cmd[cmd.index("--model") + 1], "opus")          # every run checks claims

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


class Design(unittest.TestCase):
    """Owner, 2026-10-10: a design session beside rank 0. It reads the tree,
    writes design documents in its own worktree, and directs nothing."""

    def setUp(self):
        self.root = Path(tempfile.mkdtemp())
        self.repo = self.root / "proj"
        self.repo.mkdir()
        g = lambda *a: subprocess.run(["git", "-c", "user.name=t", "-c", "user.email=t@t", *a],
                                      cwd=self.repo, check=True, capture_output=True)
        g("init", "-q", "-b", "main")
        (self.repo / "f").write_text("x")
        g("add", "f"); g("commit", "-q", "-m", "one")
        self.g = g
        self.ctx = FakeCtx({"main": None, "dev": "main"})
        self.ctx.repo, self.ctx.branch, self.ctx.worktree = self.repo, "main", self.repo
        self.ctx.tree["nodes"]["main"]["branch"] = "main"
        self.ctx.tree["nodes"]["dev"]["branch"] = "dev"

    def tearDown(self):
        shutil.rmtree(self.root, ignore_errors=True)

    def args(self, cmd, **kw):
        return hz.argparse.Namespace(cmd=cmd, fn=None, **kw)

    def test_the_worktree_and_branch_are_made_once_and_reused(self):
        self.assertEqual(hz.design_slug("Geo coverage, v2!"), "geo-coverage-v2")
        rec = hz.design_ensure(self.ctx, "geo", "Geo coverage")
        wt = self.root / "proj-design-geo"
        self.assertEqual((rec["branch"], rec["worktree"]), ("design/geo", str(wt)))
        self.assertTrue((wt / "f").exists())
        (wt / "d.md").write_text("design")
        again = hz.design_ensure(self.ctx, "geo")
        self.assertEqual(again["topic"], "Geo coverage")
        self.assertTrue((wt / "d.md").exists())                     # nothing remade
        self.assertEqual([r["slug"] for r in hz.design_records(self.ctx)], ["geo"])
        self.assertEqual(hz.design_ahead(self.ctx, rec), 0)

    def test_it_may_write_only_in_its_own_worktree(self):
        rec = hz.design_ensure(self.ctx, "geo")
        with mock.patch.object(hz, "load_index", return_value={
                "nodes": {"main": {"worktree": str(self.repo)}}}), \
             mock.patch.object(hz, "scope_block", return_value="# scope"):
            cmd = hz.design_cmd(self.ctx, rec, "opus", "high")
        allow = cmd[cmd.index("--allowedTools") + 1:cmd.index("--permission-mode")]
        self.assertEqual([r for r in allow if r.startswith(("Edit", "Write"))],
                         [f"Edit(/{rec['worktree']}/**)"])
        self.assertEqual(cmd[cmd.index("--permission-mode") + 1], "manual")
        self.assertIn("--restricted", cmd)
        dirs = cmd[cmd.index("--add-dir") + 1:cmd.index("--tools")]
        self.assertIn(str(self.repo), dirs)
        # Other worktrees: reading git only, never a commit or a merge.
        other = [r for r in allow if str(self.repo) in r]
        self.assertTrue(other and all(r.split('" ')[-1].split()[0] in hz.INTERMEDIARY_GIT
                                      for r in other if '"' in r))
        env = json.loads(cmd[cmd.index("--settings") + 1])["env"]
        self.assertEqual(env["HARNESS_DESIGN"], "geo")
        prompt = Path(cmd[cmd.index("--append-system-prompt-file") + 1]).read_text()
        self.assertIn("Never ring a node", prompt)
        self.assertIn("# scope", prompt)

    def test_it_reads_the_tree_as_rank_0_and_writes_nothing_to_it(self):
        self.addCleanup(setattr, hz, "DESIGN_VIEW", False)
        for a in (self.args("ring", node="main", text=["x"]),
                  self.args("mark", task="t", done=True),
                  self.args("queue", node="dev", order="b,a", why="w"),
                  self.args("brief", task="t", write="text"),
                  self.args("charter", write="new"),
                  self.args("hold", path="/x", why="w"),
                  self.args("test", command=["--", "pytest"]),
                  self.args("design", topic="another")):
            with self.assertRaises(SystemExit) as e:
                hz.design_gate(a)
            self.assertEqual(e.exception.code, hz.REFUSED, a.cmd)
            self.assertFalse(hz.DESIGN_VIEW)
        # The hooks say nothing: above all, they never take rank 0's mail.
        for h in ("hook-stop", "hook-orient"):
            with self.assertRaises(SystemExit) as e:
                hz.design_gate(self.args(h))
            self.assertEqual(e.exception.code, 0)
        hz.design_gate(self.args("check", report="abc", timeout=900),
                       {"timeout": 900}.get)
        hz.design_gate(self.args("queue", node="dev", order=None, why=None))
        self.assertTrue(hz.DESIGN_VIEW)
        c = hz.Ctx.__new__(hz.Ctx)
        c.tree, c.branch = self.ctx.tree, "design/geo"
        self.assertEqual(c.node()[0], "main")
        hz.DESIGN_VIEW = False
        with self.assertRaises(SystemExit) as e:
            c.node()
        self.assertEqual(e.exception.code, hz.NOT_ENROLLED)

    def test_ending_keeps_the_branch_and_refuses_uncommitted_work(self):
        rec = hz.design_ensure(self.ctx, "geo")
        wt = Path(rec["worktree"])
        (wt / "d.md").write_text("design")
        with mock.patch.object(hz, "agents_json", return_value=[]), \
             mock.patch("sys.stdout", io.StringIO()) as out:
            with self.assertRaises(SystemExit) as e:
                hz.design_end(self.ctx, "geo")
            self.assertEqual(e.exception.code, hz.REFUSED)
            self.assertTrue(wt.is_dir())
            subprocess.run(["git", "add", "d.md"], cwd=wt, check=True)
            subprocess.run(["git", "-c", "user.name=t", "-c", "user.email=t@t", "commit", "-q",
                            "-m", "design"], cwd=wt, check=True)
            hz.design_end(self.ctx, "geo")
            self.assertFalse(wt.exists())
            self.assertIn("1 commit(s) ahead of main", out.getvalue())
            self.assertEqual(hz.design_ahead(self.ctx, rec), 1)             # the branch is kept
            self.assertTrue(hz.design_records(self.ctx)[0]["ended"])
            # Rank 0 is told the branch is there to merge.
            with mock.patch.object(hz, "halted", return_value=None), \
                 mock.patch.object(hz, "drift_loops", return_value=[]), \
                 mock.patch.object(hz, "untraced_briefs", return_value=[]), \
                 mock.patch.object(hz, "live_holds", return_value=[]):
                items = hz.queue_items(self.ctx, "main")
                self.assertTrue(any(k.startswith("design:geo:1") for k in items))
                self.assertFalse(any(k.startswith("design:") for k in hz.queue_items(self.ctx, "dev")))
            hz.design_end(self.ctx, "geo", drop=True)
            self.assertIsNone(hz.design_ahead(self.ctx, rec))
            self.assertEqual(hz.design_records(self.ctx), [])


class Usage(unittest.TestCase):
    """The viewer shows the account's 5h and 7d limits the statusline saved."""

    def test_read_usage(self):
        gp = Path(__file__).resolve().parents[1] / "bin" / "harness-gui"
        ld = importlib.machinery.SourceFileLoader("harness_gui", str(gp))
        gui = importlib.util.module_from_spec(importlib.util.spec_from_loader("harness_gui", ld))
        ld.exec_module(gui)
        with tempfile.TemporaryDirectory() as td:
            f = Path(td) / "usage.json"
            with mock.patch.object(gui, "USAGE_FILE", f):
                self.assertIsNone(gui.read_usage())                  # no statusline yet
                f.write_text(json.dumps({"at": 1000, "rate_limits": {
                    "five_hour": {"used_percentage": 42.7, "resets_at": 1500},
                    "seven_day": {"used_percentage": 18, "resets_at": "1970-01-02T00:00:00Z"}}}))
                u = gui.read_usage(now=1300)
                self.assertEqual(u["age"], 300)
                self.assertEqual([(w["label"], w["pct"]) for w in u["windows"]],
                                 [("5h", 42), ("7d", 18)])
                # Past the 5h reset the saved figure is stale: shown as unknown.
                u = gui.read_usage(now=2000)
                self.assertEqual([w["pct"] for w in u["windows"]], [None, 18])


class Ringer(unittest.TestCase):
    """Log 134: one watcher per project wakes whoever has mail, by priority, by
    posting to the session's own inbox socket. No session runs a waiter."""

    def setUp(self):
        self.ctx = FakeCtx({"main": None, "dev": "main", "dev_1": "dev"})
        (self.ctx.dir / "locks").mkdir()
        self.ctx.repo = self.ctx.dir
        self.rows, self.sent = [], []

    def own(self, node, sid):
        (self.ctx.dir / "locks" / f"{node}.lock").write_text(json.dumps({"session_id": sid}))

    def tick(self, S, now, ended=None, ok=True, resumed=None, roster=()):
        def wake(row, text):
            self.sent.append((row["sessionId"], text)); return ok
        def resume(sid, text, cwd, node=None):
            (resumed if resumed is not None else self.sent).append((sid, text)); return ok
        with mock.patch.object(hz, "live_sessions", return_value=self.rows), \
             mock.patch.object(hz, "agents_json", return_value=list(roster)), \
             mock.patch.object(hz, "live_rows", side_effect=lambda r: r), \
             mock.patch.object(hz, "pid_alive", return_value=True), \
             mock.patch.object(hz, "load_index", return_value={"nodes": {
                 n: {"worktree": f"/w/{n}"} for n in self.ctx.tree["nodes"]}}), \
             mock.patch.object(hz, "bell_nudge", return_value=None), \
             mock.patch.object(hz, "turn_end_at", return_value=ended), \
             mock.patch.object(hz, "turn_ended", return_value=True), \
             mock.patch.object(hz, "wake_session", side_effect=wake), \
             mock.patch.object(hz, "resume_session", side_effect=resume), \
             mock.patch("sys.stdout", io.StringIO()):
            return hz.ringer_tick(self.ctx, S, now)

    def test_a_sleeping_lead_that_owes_a_sign_off_is_rung_and_resumed(self):
        # Log 173: dev slept for hours on presentations nobody rang it for again.
        p = mock.patch.object(hz, "ensure_ringer", lambda s: None)
        p.start(); self.addCleanup(p.stop)
        (self.ctx.dir / "marks").mkdir()
        (self.ctx.dir / "marks" / "t.json").write_text(json.dumps(
            {"_node": "dev_1", "_task": "t", "_presented_at": OLD, "_presented_sha": "a" * 40}))
        self.own("dev", "s-dev")
        self.own("main", "s-main")
        now, resumed = time.time(), []
        self.tick({}, now, ended=now - hz.OWED_IDLE - 1, resumed=resumed)
        self.assertEqual([s for s, _ in resumed], ["s-dev"])     # main owes nothing here
        mail = [json.loads(m.read_text()) for m in
                (self.ctx.dir / "doorbell" / "dev" / "inbox").glob("*.json")]
        self.assertIn("harness mark t --close", mail[0]["text"])

    def test_the_plan_for_every_kind_of_receiver_and_mail(self):
        hi, lo, fyi = ({"from": "dev", "priority": p, "text": "x"} for p in ("high", "low", "fyi"))
        plan = lambda st, mail, idle=0, last=None, now=1000: hz.ringer_plan(
            st, idle, mail, "main", last, now)[0]
        self.assertIsNone(plan("busy", [hi]))                # its hooks deliver
        self.assertIsNone(plan("busy", [lo]))
        self.assertEqual(plan("idle", [hi]), "wake")         # high: now
        self.assertIsNone(plan("idle", [lo], idle=10))       # low: not yet idle long enough
        self.assertEqual(plan("idle", [lo], idle=hz.LOW_IDLE), "wake")
        self.assertIsNone(plan("idle", [fyi], idle=hz.FYI_IDLE - 1))    # an FYI never interrupts
        self.assertEqual(plan("idle", [fyi], idle=hz.FYI_IDLE), "wake")  # but it is always read
        self.assertEqual(hz.ringer_plan("idle", hz.FYI_IDLE, [fyi], "main", None, 1000)[1], "fyi")
        mine = [{"from": "main", "session": "s-main", "text": "note to self"}]
        self.assertIsNone(hz.ringer_plan("idle", 0, mine, "main", None, 1000, "s-main")[0])
        # Signed "main" from a shell in main's checkout: the owner, not a note to self.
        self.assertEqual(plan("idle", [{"from": "main", "session": "", "text": "from a shell"}]),
                         "wake")
        self.assertEqual(plan("stopped", [hi]), "resume")
        self.assertEqual(plan("stopped", [lo]), "resume")
        self.assertIsNone(plan("stopped", [fyi]))
        self.assertIsNone(plan("none", [hi]))                # the "down" row covers it
        # Woken and still unread: wait the grace, then again at 1, 5 and 15 minutes.
        self.assertIsNone(plan("idle", [hi], last={"tries": 1, "at": 950}))
        self.assertEqual(plan("idle", [hi], last={"tries": 1, "at": 1000 - hz.WAKE_GRACE}), "wake")
        self.assertIsNone(plan("idle", [hi], last={"tries": 2, "at": 800}))
        self.assertEqual(plan("idle", [hi], last={"tries": 2, "at": 1000 - 300}), "wake")

    def test_the_wake_is_one_line_on_the_session_s_own_socket(self):
        d = Path(tempfile.mkdtemp())
        srv = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        srv.bind(str(d / "s.sock")); srv.listen(1)
        got = []
        def serve():
            c, _ = srv.accept()
            buf = b""
            while True:
                b = c.recv(4096)
                if not b:
                    break
                buf += b
            got.append(buf); c.close()
        th = threading.Thread(target=serve); th.start()
        self.assertTrue(hz.wake_session({"messagingSocketPath": str(d / "s.sock")}, "harness: mail"))
        th.join(5); srv.close()
        self.assertTrue(got[0].endswith(b"\n"))
        self.assertEqual(json.loads(got[0]), {"type": "user", "message": {
            "role": "user", "content": "harness: mail"}})
        self.assertFalse(hz.wake_session({"messagingSocketPath": str(d / "gone.sock")}, "x"))
        self.assertFalse(hz.wake_session({}, "x"))

    def test_an_idle_node_is_woken_a_busy_one_is_left_to_its_hooks(self):
        self.own("dev", "s-dev"); self.own("dev_1", "s-1")
        self.rows = [{"sessionId": "s-dev", "status": "idle", "messagingSocketPath": "/a"},
                     {"sessionId": "s-1", "status": "busy", "messagingSocketPath": "/b"}]
        hz.ring_inbox(self.ctx.state, "dev", "dev_1", "done, please review")
        hz.ring_inbox(self.ctx.state, "dev_1", "dev", "stop and read this")
        self.assertTrue(self.tick({}, 1000))
        self.assertEqual([s for s, _ in self.sent], ["s-dev"])
        self.assertIn("1 unread message(s) for dev (from dev_1)", self.sent[0][1])
        self.assertEqual(hz.MAIL().pending(self.ctx.state, "dev"), 1)    # it never takes mail

    def test_low_waits_for_idle_and_an_fyi_waits_longer_but_is_read(self):
        # Owner, 2026-10-11: an FYI that nothing ever prompts the session to read
        # is never read. It never interrupts, and after five idle minutes it wakes.
        self.own("dev", "s-dev")
        self.rows = [{"sessionId": "s-dev", "status": "idle", "messagingSocketPath": "/a"}]
        hz.ring_inbox(self.ctx.state, "dev", "main", "for information", "fyi")
        self.tick({}, 1000, ended=1000 - hz.LOW_IDLE - 5)    # idle a minute: not yet
        self.assertEqual(self.sent, [])
        self.tick({}, 1000, ended=1000 - hz.FYI_IDLE)
        self.assertEqual(len(self.sent), 1)
        self.sent.clear()
        hz.MAIL().take(self.ctx.state, "dev", "t")
        hz.ring_inbox(self.ctx.state, "dev", "main", "when you are free", "low")
        self.tick({}, 1000, ended=990)                       # idle 10 s
        self.assertEqual(self.sent, [])
        self.tick({}, 1000, ended=1000 - hz.LOW_IDLE)
        self.assertEqual(len(self.sent), 1)

    def test_a_wake_that_is_not_read_is_retried_then_flagged_to_its_lead(self):
        self.own("dev_1", "s-1")
        self.rows = [{"sessionId": "s-1", "status": "idle", "messagingSocketPath": "/b"}]
        hz.ring_inbox(self.ctx.state, "dev_1", "dev", "your check finished")
        S, t = {}, 1000
        self.tick(S, t); self.tick(S, t + 30)                # inside the grace: once
        self.assertEqual(len(self.sent), 1)
        for gap in (90, 300, 900):
            t += gap
            self.tick(S, t)
        self.assertEqual(len(self.sent), 4)
        self.assertEqual(hz.unwoken(self.ctx, "dev_1")["tries"], 4)
        with mock.patch.object(hz, "node_running", return_value=("claimed", {})), \
             mock.patch.object(hz, "cached_roster", return_value=[]):
            rows = [r for r in hz.lead_owes(self.ctx, "dev") if r[0] == "unwoken"]
        self.assertEqual([(r[1], r[2]) for r in rows], [("dev_1", "1 unread message(s)")])
        self.assertIn("harness recycle dev_1", hz.owed_line(*rows[0]))
        hz.MAIL().take(self.ctx.state, "dev_1", "t")         # read at last: the flag goes
        self.tick(S, t + 1)
        self.assertIsNone(hz.unwoken(self.ctx, "dev_1"))

    def test_a_session_stopped_while_idle_is_resumed_and_a_halt_resumes_nothing(self):
        self.own("dev_1", "s-1")                             # claimed, no live process
        hz.ring_inbox(self.ctx.state, "dev_1", "dev", "your check finished")
        resumed = []
        self.assertFalse(self.tick({}, 1000, resumed=resumed))
        self.assertEqual([s for s, _ in resumed], ["s-1"])
        hp = hz.halt_path(self.ctx)
        hp.parent.mkdir(parents=True, exist_ok=True)
        hp.write_text(json.dumps({"at": "2026-10-09T23:20:00+1100", "why": "x"}))
        resumed.clear()
        self.tick({}, 2000, resumed=resumed)
        self.assertEqual(resumed, [])

    def test_the_session_that_is_there_is_woken_not_the_holder_that_has_gone(self):
        # Log 161: a fresh spawn takes a minute to claim, the lock still named
        # the old session, and the ringer resumed that one beside it.
        self.own("dev_1", "s-old")
        self.rows = [{"sessionId": "s-new", "status": "idle", "cwd": "/w/dev_1",
                      "name": "p-dev_1", "messagingSocketPath": "/b"}]
        hz.ring_inbox(self.ctx.state, "dev_1", "dev", "go")
        resumed = []
        self.tick({}, 1000, resumed=resumed)
        self.assertEqual(resumed, [])
        self.assertEqual([s for s, _ in self.sent], ["s-new"])

    def test_nothing_is_resumed_while_a_start_is_in_flight(self):
        self.own("dev_1", "s-old")
        hz.ring_inbox(self.ctx.state, "dev_1", "dev", "go")
        self.assertIsNone(hz.start_take(self.ctx, "dev_1", "spawn", "dev"))
        resumed, S = [], {}
        self.tick(S, 1000, resumed=resumed)
        self.assertEqual(resumed, [])
        self.assertIn("a start is in flight (spawn by dev", S["_noresume"]["dev_1"])
        hz.start_clear(self.ctx, "dev_1")
        self.tick(S, 1001, resumed=resumed)
        self.assertEqual([s for s, _ in resumed], ["s-old"])
        st = hz.start_standing(self.ctx, "dev_1")                # the resume is a start too
        self.assertEqual((st["how"], st["by"], st["sid"]), ("resume", "the ringer", "s-old"))

    def test_nothing_is_resumed_beside_a_session_only_the_roster_knows(self):
        self.own("dev_1", "s-old")
        hz.ring_inbox(self.ctx.state, "dev_1", "dev", "go")
        resumed = []
        self.tick({}, 1000, resumed=resumed,
                  roster=[{"sessionId": "s-new", "cwd": "/w/dev_1", "name": "p-dev_1", "pid": 1}])
        self.assertEqual(resumed, [])
        self.assertIsNone(hz.start_standing(self.ctx, "dev_1"))

    def test_a_resume_that_fails_leaves_no_start_standing(self):
        self.own("dev_1", "s-old")
        hz.ring_inbox(self.ctx.state, "dev_1", "dev", "go")
        self.tick({}, 1000, ok=False, resumed=[])
        self.assertIsNone(hz.start_standing(self.ctx, "dev_1"))

    def owner_asks(self):
        d = Path(self.ctx.state) / "asks"
        return [hz._read_json(f) for f in sorted(d.glob("*.json"))] if d.is_dir() else []

    def test_two_sessions_in_one_worktree_are_the_owner_s_to_stop(self):
        # Log 174: rank 0 was told to stop one, and stopping a session is the
        # owner's call. The owner gets an action ask with the stop to run.
        self.own("dev_1", "s-a")
        self.rows = [{"sessionId": sid, "status": "busy", "cwd": "/w/dev_1", "name": "p-dev_1",
                      "pid": pid} for sid, pid in (("s-a", 11), ("s-b", 12))]
        S = {}
        self.tick(S, 1000)
        self.tick(S, 1001)
        (a,) = self.owner_asks()
        self.assertEqual((a["task"], a["kind"], a["asked_by"]), ("owner", "action", "harness (ringer)"))
        self.assertIn("[s-a] holds it", a["question"])
        (run,) = a["runs"]
        self.assertTrue(run.endswith("~/.claude/harness/bin/harness stop dev_1 --surplus"), run)
        self.assertTrue(run.startswith("cd "))
        self.assertFalse(hz.run_is_cd(run))
        self.assertIn("p-dev_1 [s-a] pid 11 holds the node", a["detail"])
        self.assertEqual(hz.MAIL().unread(self.ctx.state, "main"), [])     # not rank 0's
        (m,) = hz.MAIL().unread(self.ctx.state, "dev")                       # the lead: news
        self.assertEqual(m["priority"], "fyi")
        self.assertIn("The owner is asked to run: harness stop dev_1 --surplus", m["text"])
        self.assertEqual(hz.MAIL().unread(self.ctx.state, "dev_1"), [])
        # A new ringer does not ask again; a new pair replaces the ask.
        self.tick({}, 1002)
        self.assertEqual(len(self.owner_asks()), 1)
        self.own("dev_1", "s-gone")
        self.rows[1]["sessionId"] = "s-c"
        self.tick(S, 1003)
        (a2,) = self.owner_asks()
        self.assertIn("none holds it", a2["question"])
        self.assertEqual([r.split("--keep ")[1] for r in a2["runs"]], ["s-a", "s-c"])
        # One left: the ask is withdrawn, not left for the owner to run.
        self.rows = self.rows[:1]
        self.tick(S, 1004)
        self.assertEqual(self.owner_asks(), [])
        w = (Path(self.ctx.state) / "owner" / "withdrawn.jsonl").read_text().splitlines()
        self.assertEqual(json.loads(w[-1])["by"], "harness (ringer)")

    def limits(self, S, now, cause, start=None, recycled=None):
        with mock.patch.object(hz, "stop_cause", side_effect=lambda sid: cause if sid == "s-1" else None), \
             mock.patch.object(hz, "next_start", return_value=start or {"skip": None, "line": "t"}), \
             mock.patch.object(hz, "limit_recycle",
                               side_effect=lambda ctx, n: (recycled.append(n), "recycled 1")[1]), \
             mock.patch("sys.stdout", io.StringIO()) as out:
            return hz.ringer_limits(self.ctx, S, now), out.getvalue()

    def test_a_usage_limit_is_waited_out_by_the_ringer_then_the_node_is_started_once(self):
        # Log 122 again: the Stop hook that scheduled the restart never runs at
        # a limit stop, so nothing ever restarted.
        self.own("dev_1", "s-1")
        hz.ring_inbox(self.ctx.state, "dev_1", "dev", "go")
        now, S, rec = 10_000, {}, []
        cause = {"cause": "limit", "until": now + 600, "text": "resets soon"}
        for _ in range(2):
            waiting, _o = self.limits(S, now, cause, recycled=rec)
        self.assertTrue(waiting)                               # the ringer stays up for it
        self.assertEqual(rec, [])
        (m,) = hz.MAIL().unread(self.ctx.state, "main")        # rank 0 hears once
        self.assertIn("usage limit: dev_1 stopped until", m["text"])
        self.assertIn("the ringer restarts it then", m["text"])
        resumed = []
        self.tick(S, now + 1, resumed=resumed)                 # mail does not resume it into the limit
        self.assertEqual(resumed, [])
        self.assertIn("usage limit", S["_noresume"]["dev_1"])
        waiting, _o = self.limits(S, now + 600 + 130, cause, recycled=rec)
        self.assertEqual((waiting, rec), (False, ["dev_1"]))
        self.limits(S, now + 600 + 200, cause, recycled=rec)   # not again inside the retry gap
        self.assertEqual(rec, ["dev_1"])
        self.limits(S, now + 600 + 130 + hz.LIMIT_RETRY + 1, cause, recycled=rec)
        self.assertEqual(rec, ["dev_1", "dev_1"])
        self.limits(S, now + 2000, None, recycled=rec)         # going again: the record goes
        self.assertFalse(self.ctx.state_file("limits", "dev_1", ".json").exists())

    def test_a_limit_that_reset_long_ago_or_a_node_with_nothing_to_open_is_left(self):
        self.own("dev_1", "s-1")
        now, rec = 100_000, []
        late = {"cause": "limit", "until": now - 7200, "text": "x"}
        _w, out = self.limits({}, now, late, recycled=rec)
        self.assertEqual(rec, [])
        self.assertIn("not restarted", out)
        self.assertEqual(hz.MAIL().unread(self.ctx.state, "main"), [])   # no promise about the past
        self.assertEqual(hz._read_json(self.ctx.state_file("limits", "dev_1", ".json"))["left"], "late")
        self.ctx.state_file("limits", "dev_1", ".json").unlink()
        due = {"cause": "limit", "until": now - 200, "text": "x"}
        _w, out = self.limits({}, now, due, start={"skip": "every queued task waits", "line": ""},
                              recycled=rec)
        self.assertEqual(rec, [])
        self.assertIn("not restarted: every queued task waits", out)
        # An empty queue is worth a session only for a lead whose lanes hold work.
        self.ctx.state_file("limits", "dev_1", ".json").unlink()
        empty = {"skip": None, "line": "nothing queued", "empty": True}
        with mock.patch.object(hz, "open_marks", return_value={}):
            S = {}
            _w, out = self.limits(S, now, due, start=empty, recycled=rec)
        self.assertEqual(rec, [])
        self.assertIn("not restarted: nothing is queued for it", out)
        self.assertNotIn("dev_1", S["_limited"])              # so mail resumes it, as ever

    def test_rank_0_and_a_halted_tree_are_never_restarted_for_a_limit(self):
        self.own("main", "s-1")
        rec = []
        self.limits({}, 5000, {"cause": "limit", "until": 4000, "text": "x"}, recycled=rec)
        self.assertEqual(rec, [])
        self.own("dev_1", "s-1")
        hp = hz.halt_path(self.ctx)
        hp.parent.mkdir(parents=True, exist_ok=True)
        hp.write_text(json.dumps({"at": "2026-10-09T23:20:00+1100", "why": "x"}))
        self.limits({}, 4200, {"cause": "limit", "until": 4000, "text": "x"}, recycled=rec)
        self.assertEqual(rec, [])

    def test_ring_takes_a_priority_and_says_what_happens(self):
        self.ctx.me = "dev"
        o = io.StringIO()
        with mock.patch.object(hz, "Ctx", return_value=self.ctx), \
             mock.patch.object(hz, "cached_roster", return_value=[]), redirect_stdout(o):
            hz.cmd_ring(mock.Mock(node="main", text=["schema", "landed"], fyi=True, low=False))
        (m,) = hz.MAIL().unread(self.ctx.state, "main")
        self.assertEqual((m["priority"], m["from"]), ("fyi", "dev"))
        self.assertIn("rang main (fyi)", o.getvalue())

    def test_the_ringer_restarts_itself_when_the_harness_is_updated(self):
        # A daemon outlives an install: it must not run the old rules.
        self.ctx.require_enrolled = lambda: None
        with mock.patch.object(hz, "Ctx", return_value=self.ctx), \
             mock.patch.object(hz, "ringer_stamp", side_effect=[["old"], ["new"]]), \
             mock.patch.object(hz.os, "execv", side_effect=SystemExit) as ex, \
             mock.patch("sys.stdout", io.StringIO()), self.assertRaises(SystemExit):
            hz.cmd_ringer(mock.Mock())
        self.assertEqual(ex.call_args.args[1][-1], "ringer")
        # The lock was let go for the new process.
        again = hz._flock(hz.ringer_dir(self.ctx.state) / "ringer.lock", block=False)
        self.assertIsNotNone(again)
        again.close()

    def test_a_no_to_memory_caps_is_asked_again_and_a_yes_is_kept(self):
        # Log 142: a runner that asked once, while the user's systemd manager was
        # down, ran every test uncapped for hours after it came back.
        saved = list(hz._CGROUP)
        self.addCleanup(lambda: hz._CGROUP.__setitem__(slice(None), saved))
        no, yes = mock.Mock(returncode=1, stderr="Failed to connect to bus", stdout=""), \
            mock.Mock(returncode=0, stderr="", stdout="")
        hz._CGROUP[:] = [None, 0.0]
        with mock.patch.object(hz.subprocess, "run", side_effect=[no, yes]) as run, \
             mock.patch("sys.stdout", io.StringIO()) as out:
            self.assertFalse(hz.cgroup_caps()[0])
            self.assertFalse(hz.cgroup_caps()[0])            # inside the minute: not asked again
            self.assertEqual(run.call_count, 1)
            hz._CGROUP[1] -= hz.CGROUP_RETRY
            self.assertTrue(hz.cgroup_caps()[0])             # asked again: back
            self.assertIn("available again", out.getvalue())
            hz._CGROUP[1] -= 10 * hz.CGROUP_RETRY
            self.assertTrue(hz.cgroup_caps()[0])             # a yes is kept
            self.assertEqual(run.call_count, 2)

    def test_a_launch_claude_code_refuses_is_not_called_spawned(self):
        # 2026-10-11: `spawn` printed "spawned" after "Workspace not trusted".
        run = lambda rc, out: mock.patch.object(hz.subprocess, "run", return_value=mock.Mock(
            returncode=rc, stdout=out, stderr=""))
        with run(0, "backgrounded · c4959ad8 · proj-dev\n  claude agents ..."):
            self.assertEqual(hz.launch_bg(["claude", "--bg"], "/w"), (True, ""))
        with run(1, "Workspace not trusted. Run `claude` in /w once and accept the trust prompt."):
            ok, why = hz.launch_bg(["claude", "--bg"], "/w")
        self.assertFalse(ok)
        self.assertIn("Workspace not trusted", why)
        with run(0, "something else entirely"):
            self.assertFalse(hz.launch_bg(["claude", "--bg"], "/w")[0])

    def test_one_ringer_per_project_started_by_the_harness(self):
        (self.ctx.dir / "binding.json").write_text(json.dumps({"repo": str(self.ctx.dir)}))
        with mock.patch.object(hz.subprocess, "Popen") as po:
            hz.ensure_ringer(self.ctx.state)                 # the test switch: nothing starts
            self.assertFalse(po.called)
            with mock.patch.dict(os.environ):
                os.environ.pop("HARNESS_NO_RINGER")
                hz.ensure_ringer(self.ctx.state)
                self.assertEqual(po.call_args.args[0][-1], "ringer")
                self.assertNotIn("CLAUDE_CODE_SESSION_ID", po.call_args.kwargs["env"])
                po.reset_mock()
                with mock.patch.object(hz, "ringer_alive", return_value={"pid": 1}):
                    hz.ensure_ringer(self.ctx.state)         # one runs already
                self.assertFalse(po.called)
        # A second ringer finds the lock held and leaves at once.
        held = hz._flock(hz.ringer_dir(self.ctx.state) / "ringer.lock", block=False)
        self.addCleanup(held.close)
        self.ctx.require_enrolled = lambda: None
        with mock.patch.object(hz, "Ctx", return_value=self.ctx):
            hz.cmd_ringer(mock.Mock())
        self.assertFalse((hz.ringer_dir(self.ctx.state) / "ringer.json").exists())


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

    def test_held_by_is_always_another_node_that_must_act(self):
        # Owner, 2026-10-06: held by means another node must do something first.
        gp = Path(__file__).resolve().parents[1] / "bin" / "harness-gui"
        ld = importlib.machinery.SourceFileLoader("harness_gui", str(gp))
        gui = importlib.util.module_from_spec(importlib.util.spec_from_loader("harness_gui", ld))
        ld.exec_module(gui)
        cctx = mock.Mock(tree={"nodes": {"lead": {}, "a": {"parent": "lead"},
                                         "w": {"parent": "lead"}}})
        nodes = [{"name": "a", "tasks": []}, {"name": "lead", "tasks": []},
                 {"name": "w", "tasks": []}]
        why = {"ta": ["after own (briefed on a)"], "own": ["after x (open on w)"],
               "tb": ["after p (presented on w)"], "tc": ["after solo (briefed on a)"]}
        briefs = {"own": {"task": "own"}, "solo": {"task": "solo"}}
        q = {"a": [{"task": "ta"}], "lead": [], "w": []}
        with mock.patch.object(gui.CLI, "queue", lambda c, n: q[n]), \
             mock.patch.object(gui.CLI, "startable", lambda c, n: []), \
             mock.patch.object(gui.CLI, "load_brief", lambda c, t: (None, briefs.get(t))), \
             mock.patch.object(gui.CLI, "waits_on", lambda c, b: why.get((b or {}).get("task"), [])):
            gui.mark_held(cctx, nodes)
            self.assertEqual(nodes[0]["held"],                # its own task, followed
                             [{"task": "ta", "after": "x", "state": "open", "by": "w"}])
            q["a"] = [{"task": "tb"}]
            gui.mark_held(cctx, nodes)
            self.assertEqual(nodes[0]["held"], [{"task": "tb", "after": "p", "state": "presented",
                                                 "by": "lead", "worker": "w"}])
            self.assertEqual(nodes[1]["holding"], [{"node": "a", "after": "p", "signoff": "w"}])
            q["a"] = [{"task": "tc"}]
            gui.mark_held(cctx, nodes)
            self.assertEqual(nodes[0]["held"], [])        # only its own ordering: not held

    def test_a_lead_waiting_on_its_own_sign_off_is_not_held_by_the_child(self):
        # Owner, 2026-10-15: dev read as held by dev_dag, because dev's next task
        # waited on environment-dag, which dev_dag had presented and dev had not
        # signed off. The sign-off is dev's own: owed, not held.
        gp = Path(__file__).resolve().parents[1] / "bin" / "harness-gui"
        ld = importlib.machinery.SourceFileLoader("harness_gui", str(gp))
        gui = importlib.util.module_from_spec(importlib.util.spec_from_loader("harness_gui", ld))
        ld.exec_module(gui)
        cctx = mock.Mock(tree={"nodes": {"dev": {}, "dev_dag": {"parent": "dev"}}})
        nodes = [{"name": "dev", "tasks": []}, {"name": "dev_dag", "tasks": []}]
        q = {"dev": [{"task": "environment-dag.up-dev"}], "dev_dag": []}
        why = {"environment-dag.up-dev": ["after environment-dag (presented on dev_dag)"]}
        with mock.patch.object(gui.CLI, "queue", lambda c, n: q[n]), \
             mock.patch.object(gui.CLI, "startable", lambda c, n: []), \
             mock.patch.object(gui.CLI, "waits_on", lambda c, b: why.get(b["task"], [])):
            gui.mark_held(cctx, nodes)
        dev, dag = nodes
        self.assertEqual(dev["held"], [])
        self.assertEqual(dev["signoff"], [{"after": "environment-dag", "worker": "dev_dag",
                                           "task": "environment-dag.up-dev"}])
        self.assertEqual(dag["holding"], [])


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
        self.assertEqual(go.call_args.args[1][-2], "--wake")         # a whole doc: two fixes
        (self.ctx.dir / "pairs" / "docs-3.json").write_text(json.dumps(dict(rec, task="docs-3")))
        with mock.patch.object(hz, "_detached") as go:
            hz.docs_decided(self.ctx, dict(rec, task="docs-3"))
        self.assertEqual(go.call_args.args[1][-1], "--finish")      # third decline: over

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
    """Reading mail by hand. The waiter this command used to be is retired
    (log 134): the project's ringer wakes a session, and nothing is armed."""

    def setUp(self):
        self.ctx = FakeCtx({"main": None, "dev": "main"})
        self.ctx.me = "main"
        self.env = mock.patch.dict(os.environ, {"CLAUDE_CODE_SESSION_ID": "sess-main"})
        self.env.start(); self.addCleanup(self.env.stop)
        self.c = mock.patch.object(hz, "Ctx", return_value=self.ctx)
        self.c.start(); self.addCleanup(self.c.stop)
        self.r = mock.patch.object(hz, "cached_roster", return_value=[])
        self.r.start(); self.addCleanup(self.r.stop)

    def out(self, f, a):
        o = io.StringIO()
        with redirect_stdout(o):
            f(a)
        return o.getvalue()

    def test_ring_wakes_and_read_says_why(self):
        self.ctx.me = "dev"
        self.out(hz.cmd_ring, mock.Mock(node="main", text=["dev", "needs", "a", "ruling"]))
        self.ctx.me = "main"
        # The old way to arm it: says it is retired, starts nothing, takes nothing.
        o = self.out(hz.cmd_doorbell, mock.Mock(read=False, status=False))
        self.assertIn("retired", o)
        self.assertFalse((hz.bell_dir(self.ctx, "main") / "armed.json").exists())
        self.assertEqual(hz.MAIL().pending(self.ctx.state, "main"), 1)
        o = self.out(hz.cmd_doorbell, mock.Mock(read=True, status=False))
        self.assertIn("from dev: dev needs a ruling", o)
        self.assertIn("nothing new", self.out(hz.cmd_doorbell, mock.Mock(read=True, status=False)))

    def test_the_waiter_leaves_the_mail_for_whoever_reads_it(self):
        # It only wakes the session; a hook may have shown the mail first.
        hz.ring_inbox(self.ctx.state, "main", "dev", "hello")
        with mock.patch.object(hz, "bell_nudge", return_value=None):
            self.out(hz.cmd_doorbell, mock.Mock(read=False, status=False))
        self.assertEqual(hz.MAIL().pending(self.ctx.state, "main"), 1)
        self.assertEqual([m["text"] for m in hz.MAIL().take(self.ctx.state, "main", "t")], ["hello"])
        self.assertIn("nothing new", self.out(hz.cmd_doorbell, mock.Mock(read=True, status=False)))

    def test_nudge_once_per_wait_and_only_when_idle(self):
        rows = [{"sessionId": "sess-main", "status": "idle", "cwd": "/m"}]
        w = [("dev", 900, "carry rebuilt", "inf:dev:1")]
        with mock.patch.object(hz, "cached_roster", return_value=rows), \
             mock.patch.object(hz, "waiters_on", return_value=w), \
             mock.patch.object(hz, "load_index", return_value={"byWorktree": {}}):
            with mock.patch.object(hz, "turn_end_at", return_value=time.time() - 60):
                self.assertIsNone(hz.bell_nudge(self.ctx, "main", "sess-main"))   # just spoke
            with mock.patch.object(hz, "turn_end_at", return_value=time.time() - 900):
                self.assertIn("dev has been waiting on you for 15m: carry rebuilt",
                              hz.bell_nudge(self.ctx, "main", "sess-main"))
                self.assertIsNone(hz.bell_nudge(self.ctx, "main", "sess-main"))   # told once
            rows[0]["status"] = "busy"
            with mock.patch.object(hz, "waiters_on", return_value=[("dev", 900, "", "inf:dev:2")]), \
                 mock.patch.object(hz, "turn_end_at", return_value=time.time() - 900):
                self.assertIsNone(hz.bell_nudge(self.ctx, "main", "sess-main"))   # working

    def test_idle_is_counted_from_the_turn_end_not_a_later_note(self):
        # Claude Code's away_summary lands in an idle transcript; it restarted
        # the five minutes when idle was read off the file's mtime (2026-10-06).
        t = Path(tempfile.mkdtemp()) / "s.jsonl"
        t.write_text("\n".join(json.dumps(r) for r in (
            {"type": "assistant", "message": {"content": []}},
            {"type": "system", "subtype": "turn_duration", "timestamp": "2026-10-06T05:43:51.000Z"},
            {"type": "system", "subtype": "away_summary", "timestamp": "2026-10-06T05:46:49.000Z"})))
        with mock.patch.object(hz, "transcript_for", return_value=t):
            self.assertEqual(hz.turn_end_at("s"),
                             hz.datetime.datetime(2026, 10, 6, 5, 43, 51,
                                                  tzinfo=hz.datetime.timezone.utc).timestamp())
            t.write_text(t.read_text() + "\n" + json.dumps({"type": "user", "message": {"content": "go"}}))
            self.assertIsNone(hz.turn_end_at("s"))                       # a turn is running


class DoorbellHooks(unittest.TestCase):
    """Mail reaches the node's own session through hooks, with no arming: after
    a tool call, at a turn end, at a prompt. The Stop hook's blocks are
    top-level JSON, the only form Claude Code acts on (2026-10-06)."""

    def setUp(self):
        self.ctx = FakeCtx({"main": None, "dev": "main"})
        self.ctx.me = "main"
        self.ctx.tree_path = self.ctx.dir / "tree.json"
        self.ctx.binding_path = self.ctx.dir / "binding.json"
        self.ctx.tree_path.write_text(json.dumps(self.ctx.tree))
        self.ctx.binding_path.write_text("{}")
        self.ctx.lock_path("main").parent.mkdir(parents=True, exist_ok=True)
        self.ctx.lock_path("main").write_text(json.dumps({"node": "main", "session_id": "sess-main"}))
        for p in [mock.patch.object(hz, "Ctx", return_value=self.ctx),
                  mock.patch.object(hz, "hook_ctx", return_value=self.ctx),
                  mock.patch.object(hz, "git", return_value=(0, "", "")),
                  mock.patch.object(hz, "docs_apply_step", return_value=None),
                  mock.patch.object(hz, "reset_step", return_value=False),
                  mock.patch.object(hz, "lead_owes", return_value=[]),
                  mock.patch.object(hz, "rank0_owes", return_value=[]),
                  mock.patch.object(hz, "print_delta", return_value=None),
                  mock.patch.object(hz, "cached_roster", return_value=[]),
                  mock.patch.dict(os.environ, {}, clear=False)]:
            p.start(); self.addCleanup(p.stop)
        os.environ.pop("HARNESS_INTERMEDIARY", None)
        os.environ.pop("HARNESS_DOCUMENTER", None)

    def stop(self, sid="sess-main", again=False, armed=True):
        o = io.StringIO()
        payload = json.dumps({"session_id": sid, "stop_hook_active": again})
        with mock.patch.object(hz, "bell_armed", return_value={"pid": 1} if armed else None), \
             mock.patch("sys.stdin", io.StringIO(payload)), redirect_stdout(o):
            hz.cmd_hook_stop(mock.Mock())
        return json.loads(o.getvalue()) if o.getvalue().strip() else None

    def test_a_block_is_top_level_json(self):
        hz.ring_inbox(self.ctx.state, "main", "dev", "a ruling, please")
        out = self.stop()
        self.assertEqual(out["decision"], "block")
        self.assertNotIn("hookSpecificOutput", out)
        self.assertIn("from dev: a ruling, please", out["reason"])
        self.assertIsNone(self.stop())                       # taken as shown

    def test_only_the_node_s_own_session_gets_mail_or_nags(self):
        hz.ring_inbox(self.ctx.state, "main", "dev", "for main")
        self.assertIsNone(self.stop(sid="someone-else", armed=False))
        os.environ["HARNESS_INTERMEDIARY"] = "1"
        self.assertIsNone(self.stop(armed=False))
        del os.environ["HARNESS_INTERMEDIARY"]
        self.assertEqual(hz.MAIL().pending(self.ctx.state, "main"), 1)

    def test_mail_blocks_even_after_a_block_but_nags_do_not(self):
        self.assertIsNone(self.stop(again=True, armed=False))
        hz.ring_inbox(self.ctx.state, "main", "dev", "late news")
        self.assertIn("late news", self.stop(again=True)["reason"])

    def test_no_turn_end_is_blocked_for_want_of_a_waiter(self):
        # Log 134: "your doorbell is not armed" blocked every turn end, forty
        # re-arms a day on main. The ringer wakes an idle session; nothing to arm.
        for _ in range(2):
            self.assertIsNone(self.stop(armed=False))

    def test_only_mail_that_asks_for_something_holds_the_turn_open(self):
        hz.ring_inbox(self.ctx.state, "main", "dev", "thanks, all good", "fyi")
        with mock.patch.dict(os.environ, {"CLAUDE_CODE_SESSION_ID": "sess-main"}):
            hz.ring_inbox(self.ctx.state, "main", "main", "my own answer")
        self.assertIsNone(self.stop())                       # an FYI and an own note: no block
        self.assertEqual(hz.MAIL().pending(self.ctx.state, "main"), 2)
        hz.ring_inbox(self.ctx.state, "main", "dev", "when you are free", "low")
        out = self.stop()["reason"]                          # low: handed over at the turn end
        self.assertIn("Doorbell — 1 message(s) for you", out)
        self.assertIn("when you are free", out)
        self.assertIn("FYI, no action needed — 1", out)
        self.assertIn("you wrote: my own answer", out)
        self.assertEqual(out.count("act on them now"), 1)
        self.assertEqual(hz.MAIL().pending(self.ctx.state, "main"), 0)

    def test_the_prompt_hook_hands_over_mail(self):
        hz.ring_inbox(self.ctx.state, "main", "owner", "re-file the delete")
        self.addCleanup(setattr, hz, "QUIET", hz.QUIET)     # hook-orient sets it
        o = io.StringIO()
        with mock.patch("sys.stdin", io.StringIO(json.dumps({"session_id": "sess-main"}))), \
             redirect_stdout(o), self.assertRaises(SystemExit):
            hz.cmd_hook_orient(mock.Mock())
        self.assertIn("from owner: re-file the delete", o.getvalue())
        self.assertEqual(hz.MAIL().pending(self.ctx.state, "main"), 0)

    def test_a_slow_orientation_is_cut_short_and_the_mail_still_arrives(self):
        # 2026-10-12: rank 0's prompt took 3 to 10 s, the hook was killed at 5 s,
        # and the mail the ringer had woken the session for was never printed.
        hz.ring_inbox(self.ctx.state, "main", "owner", "re-file the delete")
        self.addCleanup(setattr, hz, "QUIET", hz.QUIET)
        o, t0 = io.StringIO(), time.time()
        with mock.patch.object(hz, "print_delta", side_effect=lambda *a: time.sleep(5)), \
             mock.patch.object(hz, "HOOK_BUDGET", 0.3), \
             mock.patch("sys.stdin", io.StringIO(json.dumps({"session_id": "sess-main"}))), \
             redirect_stdout(o), self.assertRaises(SystemExit):
            hz.cmd_hook_orient(mock.Mock())
        self.assertLess(time.time() - t0, 2)
        self.assertIn("skipped this prompt", o.getvalue())
        self.assertIn("from owner: re-file the delete", o.getvalue())
        self.assertEqual(hz.MAIL().pending(self.ctx.state, "main"), 0)
        self.assertIn("main hook-orient over 0.3s", (self.ctx.dir / "hook_slow.log").read_text())

    def test_the_budget_cuts_work_that_guards_against_every_exception(self):
        def stubborn():
            try:
                time.sleep(5)
            except Exception:                    # the guards inside the real work
                pass
        t0 = time.time()
        self.assertFalse(hz.within_budget(0.2, stubborn))
        self.assertLess(time.time() - t0, 2)
        self.assertTrue(hz.within_budget(0.5, lambda: None))
        t0 = time.time()
        time.sleep(0.6)                          # and its alarm does not outlive it
        self.assertGreater(time.time() - t0, 0.5)

    def test_the_tool_call_hook_finds_its_node_and_skips_subagents(self):
        M = hz.MAIL()
        home = Path(tempfile.mkdtemp())
        st = home / "proj"
        (st / "locks").mkdir(parents=True)
        (st / "locks" / "main.lock").write_text(json.dumps({"session_id": "s1"}))
        (st / "index.json").write_text(json.dumps({"byWorktree": {"/w/repo": "main",
                                                                  "/w/repo-dev": "dev"}}))
        hz.ring_inbox(st, "main", "dev", "not urgent", "low")
        hz.ring_inbox(st, "main", "dev", "for information", "fyi")
        hz.ring_inbox(st, "main", "dev", "mid-turn note")

        def run(payload):
            o = io.StringIO()
            with mock.patch.object(M, "HOME_STATE", home), \
                 mock.patch("sys.stdin", io.StringIO(json.dumps(payload))), redirect_stdout(o):
                M.main()
            return o.getvalue()
        self.assertEqual(run({"cwd": "/w/repo-dev", "session_id": "s1"}), "")   # not its node
        self.assertEqual(run({"cwd": "/w/repo", "session_id": "s2"}), "")       # not its owner
        self.assertEqual(run({"cwd": "/w/repo/sub", "session_id": "s1", "agent_id": "a"}), "")
        out = json.loads(run({"cwd": "/w/repo/sub", "session_id": "s1"}))
        self.assertEqual(out["hookSpecificOutput"]["hookEventName"], "PostToolUse")
        self.assertIn("mid-turn note", out["hookSpecificOutput"]["additionalContext"])
        # Mid-turn only what interrupts: the low and FYI messages stay (log 134).
        self.assertNotIn("not urgent", out["hookSpecificOutput"]["additionalContext"])
        self.assertEqual(run({"cwd": "/w/repo", "session_id": "s1"}), "")       # once
        log = (st / "doorbell" / "main" / "delivered.jsonl").read_text().splitlines()
        self.assertEqual(json.loads(log[0])["how"], "tool call")
        self.assertEqual(sorted(M.prio(m) for m in M.unread(st, "main")), ["fyi", "low"])

    def test_ring_says_when_it_will_be_read(self):
        rr = lambda pr="high": hz.ring_report(self.ctx, "main", pr)
        self.assertIn("no live session", rr())
        with mock.patch.object(hz, "cached_roster",
                               return_value=[{"sessionId": "sess-main", "status": "busy"}]):
            self.assertIn("next tool call", rr())
            self.assertIn("held until its turn ends", rr("low"))
        with mock.patch.object(hz, "cached_roster",
                               return_value=[{"sessionId": "sess-main", "status": "idle"}]):
            self.assertIn("the ringer wakes it now", rr())
            self.assertIn("idle a minute", rr("low"))
            self.assertIn("idle five minutes", rr("fyi"))
            hz.reset_path(self.ctx, "main").parent.mkdir(parents=True, exist_ok=True)
            hz.reset_path(self.ctx, "main").write_text("{}")
            self.assertIn("a reset of it is pending", rr())

    def test_ring_knows_a_session_that_has_not_claimed_yet(self):
        # Log 96 note: `ring` said "no live session" about a node `recycle` had
        # just started; it reads "running" as orientation does (log 105).
        with mock.patch.object(hz, "bell_armed", return_value=None), \
             mock.patch.object(hz, "cached_roster", return_value=[]), \
             mock.patch.object(hz, "node_running", return_value=("unclaimed", {"cwd": "/w"})):
            r = hz.ring_report(self.ctx, "main")
        self.assertNotIn("no live session", r)
        self.assertIn("hasn't claimed", r)

    def test_recycle_says_what_to_do_when_nothing_is_queued(self):
        with mock.patch.object(hz, "open_marks", return_value={}), \
             mock.patch.object(hz, "startable", return_value=[]), \
             mock.patch.object(hz, "queue", return_value=[]), \
             mock.patch.object(hz, "load_charter", return_value=(None, {"features": [{"name": "f"}]})):
            line = hz.next_start(self.ctx, "dev")["line"]
        self.assertIn("harness ring dev -", line)
        self.assertIn("--feature <f>", line)

    def test_a_waiting_doorbell_does_not_make_an_idle_session_busy(self):
        # Claude Code calls a session with a background command busy.
        t = self.ctx.dir / "t.jsonl"
        ended = [{"type": "assistant", "message": {"content": []}},
                 {"type": "system", "subtype": "stop_hook_summary"},
                 {"type": "system", "subtype": "turn_duration"},
                 {"type": "system", "subtype": "away_summary"},
                 {"type": "custom-title"}]
        running = ended + [{"type": "user", "message": {"content": "task done"}}]
        with mock.patch.object(hz, "transcript_for", return_value=t):
            t.write_text("\n".join(json.dumps(r) for r in ended))
            self.assertTrue(hz.turn_ended("s"))
            rows = hz.agents_json(json.dumps([{"sessionId": "s", "status": "busy"}]))
            self.assertEqual((rows[0]["status"], rows[0]["reported_status"]), ("idle", "busy"))
            t.write_text("\n".join(json.dumps(r) for r in running))
            self.assertFalse(hz.turn_ended("s"))
            self.assertEqual(hz.agents_json(json.dumps([{"sessionId": "s", "status": "busy"}]))[0]
                             ["status"], "busy")

    def test_doctor_names_a_missing_session_hook(self):
        repo = Path(tempfile.mkdtemp())
        (repo / ".claude").mkdir()
        conf = {"hooks": {ev: [json.loads(json.dumps(e))] for ev, e in hz.SESSION_HOOKS
                          if ev != "PostToolUse"}}
        (repo / ".claude" / "settings.json").write_text(json.dumps(conf))
        self.assertEqual(hz.session_hooks_missing(repo), ["PostToolUse (harness-mail)"])
        conf["hooks"]["PostToolUse"] = [dict(dict(hz.SESSION_HOOKS)["PostToolUse"])]
        (repo / ".claude" / "settings.json").write_text(json.dumps(conf))
        self.assertEqual(hz.session_hooks_missing(repo), [])
        # Log 172: SubagentStart is wanted only where a node has a skill on.
        del conf["hooks"]["SubagentStart"]
        (repo / ".claude" / "settings.json").write_text(json.dumps(conf))
        self.assertEqual(hz.session_hooks_missing(repo, {"nodes": {"a": {}}}), [])
        self.assertEqual(hz.session_hooks_missing(repo, {"nodes": {"a": {"role": "reviewer"}}}),
                         ["SubagentStart (harness hook-subagent)"])


class Log108(unittest.TestCase):
    """Log 108: a signed ruling rings the asker and the brief's lead now, not at
    their next prompt."""

    def setUp(self):
        self.ctx = FakeCtx({"main": None, "dev": "main", "dev_1": "dev"})
        (self.ctx.dir / "briefs").mkdir()
        (self.ctx.dir / "asks").mkdir()
        (self.ctx.dir / "briefs" / "s1.json").write_text(json.dumps({"task": "s1", "node": "dev_1"}))

    def accept(self, asker, answer="Use the local model.\nMore detail."):
        rec = {"id": "s1-1", "task": "s1", "node": "dev_1", "kind": "judgement",
               "question": "Which model?", "asker_node": asker, "state": "drafted",
               "draft": answer}
        path = self.ctx.dir / "asks" / "s1-1.json"
        path.write_text(json.dumps(rec))
        with mock.patch.object(hz, "ask_lead", return_value="dev"):
            return hz.ask_accept(self.ctx.dir, path, rec)

    def inbox(self, n):
        return [json.loads(p.read_text())
                for p in (self.ctx.dir / "doorbell" / n / "inbox").glob("*.json")]

    def test_ruling_rings_the_asker_and_the_lead_with_its_first_line(self):
        r = self.accept("main")
        self.assertEqual(r["rung"], ["main", "dev"])
        for n in ("main", "dev"):
            [m] = self.inbox(n)
            self.assertEqual(m["from"], "owner")
            self.assertIn("Use the local model.", m["text"])
            self.assertNotIn("More detail", m["text"])
            self.assertIn("harness brief s1", m["text"])
        # the orientation line stays as the backstop until the brief is read
        self.assertTrue(any(k.startswith("ruled:") for k in hz.ask_notices(self.ctx, "main")))

    def test_an_asker_that_is_the_lead_is_rung_once(self):
        self.assertEqual(self.accept("dev")["rung"], ["dev"])
        self.assertEqual(len(self.inbox("dev")), 1)

    def test_the_owner_and_operator_are_not_rung(self):
        self.assertEqual(self.accept("operator")["rung"], ["dev"])

    def test_a_node_the_ruling_names_is_rung_too(self):
        with mock.patch.object(hz, "ask_nodes", return_value=["main", "dev", "dev_1"]):
            r = self.accept("dev", answer="Authorised by a grant from main to dev_1.")
        self.assertEqual(r["rung"], ["dev", "main", "dev_1"])

    def test_a_documenter_ruling_rings_nobody(self):
        self.accept("documenter")
        self.assertEqual(list(self.ctx.dir.glob("doorbell/*/inbox/*.json")), [])
        self.assertTrue((self.ctx.dir / "docs" / "rulings.json").exists())


class ChangedArms(unittest.TestCase):
    """Owner, 2026-10-08: a worker checks only the arms its change touches; the
    lead runs the full set after merging."""

    def setUp(self):
        self.ctx = FakeCtx({"dev": None, "w": "dev"})
        self.ctx.tree["nodes"]["dev"]["branch"] = "dev"
        self.ctx.tree["nodes"]["w"]["branch"] = "w"
        r = self.ctx.dir / "repo"
        r.mkdir()
        self.ctx.repo = self.ctx.worktree = r
        g = lambda *a: subprocess.run(["git", "-c", "user.name=t", "-c", "user.email=t@t", *a],
                                      cwd=r, check=True, capture_output=True)
        self.g = g
        g("init", "-q", "-b", "dev")
        for f in ("src/surface/a.js", "src/enrich/b.py", "docs/x.md", "README.md"):
            (r / f).parent.mkdir(parents=True, exist_ok=True)
            (r / f).write_text("1")
        (r / ".harness").mkdir()
        self.man({})
        g("add", "-A"); g("commit", "-qm", "base"); g("checkout", "-qb", "w")
        self.checks = [{"name": "surface", "paths": ["src/surface/*"]},
                       {"name": "enrich", "paths": ["src/enrich/*"]}]

    def man(self, m):
        (self.ctx.repo / ".harness" / "manifest.json").write_text(json.dumps(m))

    def change(self, *files):
        for f in files:
            p = self.ctx.repo / f
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text("2")
        self.g("add", "-A"); self.g("commit", "-qm", "c")

    def arms(self, checks=None):
        return hz.changed_arms(self.ctx, "w", checks or self.checks)

    def test_only_the_arm_a_change_touches(self):
        self.change("src/enrich/b.py")
        sel, info = self.arms()
        self.assertEqual(sel, ["enrich"])
        self.assertEqual(info["base"], "dev")

    def test_an_unclaimed_file_runs_every_arm(self):
        self.change("src/enrich/b.py", "setup.cfg")
        sel, info = self.arms()
        self.assertIsNone(sel)
        self.assertIn("setup.cfg", info["why"])

    def test_ignored_files_need_no_check(self):
        self.man({"checks_ignore": ["docs/*", "*.md"]})
        self.g("add", "-A"); self.g("commit", "-qm", "m")
        self.change("docs/x.md", "README.md")
        sel, info = self.arms()
        self.assertIsNone(sel)                     # the manifest itself is unclaimed
        self.man({"checks_ignore": ["docs/*", "*.md", ".harness/*"]})
        self.g("add", "-A"); self.g("commit", "-qm", "m2")
        self.assertEqual(self.arms()[0], [])

    def test_an_arm_without_paths_always_runs(self):
        self.change("src/enrich/b.py")
        sel, _ = self.arms(self.checks + [{"name": "guard"}])
        self.assertEqual(sel, ["enrich", "guard"])

    def test_no_arm_with_paths_says_so(self):
        # Log 110: "the change touches every arm" hid that nothing was compared.
        self.change("src/enrich/b.py")
        sel, info = self.arms([{"name": "surface"}, {"name": "enrich"}])
        self.assertIsNone(sel)
        self.assertTrue(info.get("nopaths"))
        self.assertIn("no arm declares paths", info["why"])

    def test_no_paths_still_honours_checks_ignore(self):
        self.man({"checks_ignore": ["docs/*", "*.md", ".harness/*"]})
        self.g("add", "-A"); self.g("commit", "-qm", "m")
        self.change("docs/x.md")
        sel, info = self.arms([{"name": "surface"}])
        self.assertEqual(sel, [])
        self.assertNotIn("nopaths", info)


class GrantWording(unittest.TestCase):
    """Log 112: a granted path still meets Claude Code's classifier under auto
    mode, so the grant says so where it is made."""

    def setUp(self):
        self.ctx = FakeCtx({"main": None, "dev": "main"})
        self.ctx.tree_path = self.ctx.dir / "tree.json"

    def grant(self, *argv):
        with mock.patch.object(hz, "Ctx", return_value=self.ctx), \
             mock.patch.dict(os.environ, {}, clear=False), \
             mock.patch("sys.argv", ["harness", "grant", *argv]), \
             redirect_stdout(io.StringIO()) as o:
            os.environ.pop("CLAUDE_CODE_SESSION_ID", None)
            hz.main()
        return o.getvalue()

    def test_a_path_grant_names_the_classifier_and_the_action_ask(self):
        out = self.grant("dev", str(self.ctx.dir / "fixture"), "--reason", "x")
        self.assertIn("classifier", out)
        self.assertIn("--kind action", out)
        self.assertIn("writes still face the classifier", self.grant("--list"))

    def test_a_rule_grant_does_not(self):
        out = self.grant("dev", "Bash(make *)", "--reason", "x")
        self.assertNotIn("classifier", out)


class WaitPool(unittest.TestCase):
    """Log 109: a parked task starts nowhere and nags nobody for 12 hours, then
    returns to the normal pool by itself and its parker is told once."""

    def setUp(self):
        self.ctx = FakeCtx({"main": None, "dev": "main"})
        (self.ctx.dir / "briefs").mkdir()

    def brief(self, task, **kw):
        b = {"task": task, "node": "dev", "text": "t"}
        b.update(kw)
        (self.ctx.dir / "briefs" / f"{task}.json").write_text(json.dumps(b))

    def load(self, task):
        return json.loads((self.ctx.dir / "briefs" / f"{task}.json").read_text())

    def wait(self, left):
        return {"why": "until the design session", "by_node": "main", "at": "x",
                "until": time.time() + left}

    def test_parked_leaves_the_queue_and_the_approval_nag(self):
        old = time.strftime("%Y-%m-%dT%H:%M:%S%z", time.localtime(time.time() - 7200))
        self.brief("dag", approval={"state": "pending", "asked_at": old}, wait=self.wait(3600))
        self.brief("q", wait=self.wait(3600))
        self.assertEqual(hz.queue(self.ctx, "dev"), [])
        with mock.patch.object(hz, "docs_pending", return_value=[]), \
             mock.patch.object(hz, "decided_blocks", return_value={}), \
             mock.patch.object(hz, "completed_units", return_value=[]), \
             mock.patch.object(hz, "stale_records", return_value=([], [])), \
             mock.patch.object(hz, "ended_count", return_value=0):
            self.assertEqual([o for o in hz.rank0_owes(self.ctx, "main") if o[0] == "approve"], [])

    def test_an_expired_wait_returns_to_the_pool_and_is_told_once(self):
        self.brief("q", wait=self.wait(-1))
        self.assertFalse(hz.parked(self.load("q")))
        self.assertEqual(len(hz.expire_waits(self.ctx)), 1)
        b = self.load("q")
        self.assertNotIn("wait", b)
        self.assertEqual(b["returned"]["why"], "until the design session")
        self.assertEqual(b["wait_history"][0]["why"], "until the design session")
        self.assertEqual([x[1]["task"] for x in hz.returned_for(self.ctx, "main")], ["q"])
        self.assertEqual(hz.returned_for(self.ctx, "dev"), [])
        self.assertEqual([x["task"] for x in hz.queue(self.ctx, "dev")], ["q"])
        self.assertEqual(hz.expire_waits(self.ctx), [])        # nothing left to move

    def test_a_live_wait_is_left_alone(self):
        self.brief("q", wait=self.wait(600))
        self.assertTrue(hz.parked(self.load("q")))
        self.assertEqual(hz.expire_waits(self.ctx), [])


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
        self.assertEqual(saved["state"], "asked")            # a reply is not a brief

    def add(self, rec, *runs, me="main", sid="s" * 36):
        """`harness ask <id> --run ...` as `me` (log 113)."""
        self.ctx.me, self.ctx.branch = me, me
        env = {"CLAUDE_CODE_SESSION_ID": sid} if sid else {}
        argv = ["harness", "ask", rec["id"]] + [x for r in runs for x in ("--run", r)]
        with mock.patch.object(hz, "Ctx", return_value=self.ctx), \
             mock.patch.object(hz, "ask_find", side_effect=lambda *a: (
                 self.ctx.dir, "/r/proj", self.path(rec),
                 json.loads(self.path(rec).read_text()))), \
             mock.patch.object(hz, "item_wake_detached") as wake, \
             mock.patch.dict(os.environ, env), \
             mock.patch("sys.argv", argv), redirect_stdout(io.StringIO()) as o:
            if not sid:
                os.environ.pop("CLAUDE_CODE_SESSION_ID", None)
            try:
                hz.main(); code = 0
            except SystemExit as e:
                code = e.code
        return code, o.getvalue(), wake, json.loads(self.path(rec).read_text())

    def test_a_command_joins_a_filed_ask(self):
        r = self.open(me="dev", task="s1")
        code, out, wake, saved = self.add(r, "pip install y", me="dev")
        self.assertEqual(code, 0)
        self.assertEqual(saved["runs"], ["pip install x", "pip install y"])
        self.assertEqual(saved["state"], "asked")
        self.assertIn("added 1 command(s)", out)
        wake.assert_called_once()
        self.assertEqual(self.add(r, "z", me="main")[0], 0)        # rank 0 may too
        self.assertEqual(self.add(r, "w", sid="")[0], 0)           # and a shell
        self.assertNotEqual(self.add(r, "v", me="dev_1")[0], 0)    # a lane may not

    def test_a_briefed_ask_goes_back_to_be_rebriefed(self):
        r = self.open()
        rec = json.loads(self.path(r).read_text())
        rec.update(state="drafted", brief={"question": "q"}, draft="run it")
        self.path(r).write_text(json.dumps(rec))
        code, out, wake, saved = self.add(r, "pip install y")
        self.assertEqual((saved["state"], saved["draft"]), ("asked", None))
        self.assertEqual(saved["brief"], {"question": "q"})        # kept, to amend
        self.assertIn("re-brief", wake.call_args[0][2])
        self.assertIn("re-briefs", out)

    def test_adding_commands_is_refused_where_it_does_not_fit(self):
        q = hz.ask_open(self.ctx, "s1", "intent", "Which way?", "dev", "s" * 36)
        self.assertNotEqual(self.add(q, "x", me="dev")[0], 0)      # not an action ask
        r = self.open(runs=["x"] * 9)
        self.assertNotEqual(self.add(r, "y", "z")[0], 0)           # 11 > the cap of 10
        self.assertEqual(len(json.loads(self.path(r).read_text())["runs"]), 9)
        rec = json.loads(self.path(r).read_text())
        self.path(r).write_text(json.dumps(dict(rec, state="done")))
        self.assertNotEqual(self.add(r, "y")[0], 0)                # closed

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
        self.scratch_home()                    # never the real ~/.cache

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
             mock.patch.object(hz, "item_profile", return_value="P1"), \
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

    def stamp(self, ask="t-1", profile="P1"):
        home = hz.item_home(self.pdir, ask)
        home.mkdir(parents=True, exist_ok=True)
        (home / "profile").write_text(profile + "\n")

    def test_idle_is_stopped_then_resumed_without_flags(self):
        sid = "abcd1234" + "x" * 28
        self.stamp()
        ok, _, calls = self.wake([self.row("t-1", sid=sid)])
        self.assertEqual(calls[0], ["claude", "stop", "abcd1234"])
        self.assertEqual(calls[1][:4], ["claude", "--bg", "--resume", sid])
        self.assertEqual(len(calls[1]), 5)                   # flags would start a copy
        self.assertIn("harness ask --idle", calls[1][4])

    def test_a_session_from_an_older_profile_is_replaced_not_resumed(self):
        # Log 114 follow-up: a resumed session kept the tools it started with.
        sid = "abcd1234" + "x" * 28
        for stamp in (None, "OLD"):                  # unstamped, then a stale stamp
            if stamp:
                self.stamp(profile=stamp)
            hz.item_inbox(self.pdir, "t-1", f"queued before {stamp}")
            ok, msg, calls = self.wake([self.row("t-1", sid=sid)])
            self.assertEqual(calls[0], ["claude", "stop", "abcd1234"])
            self.assertEqual(calls[1][:3], ["claude", "--bg", "FRESH"])
            self.assertIn("older permissions", calls[1][5])
            self.assertIn(f"queued before {stamp}", calls[1][5])     # the inbox carries over
            self.assertTrue(msg.startswith("restarted"))
            self.assertEqual((hz.item_home(self.pdir, "t-1") / "profile").read_text().strip(),
                             "P1")

    def test_fresh_start_takes_the_model_for_its_kind(self):
        ok, _, calls = self.wake([], ask="t-2")
        self.assertEqual(calls[0][:5], ["claude", "--bg", "FRESH", "opus", "t-2"])
        ok, _, calls = self.wake([], ask="t-1")
        self.assertEqual(calls[0][3], "opus")               # an action is dug into too

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

    def test_item_writes_its_scratch_folder_only(self):
        # Log 114: it had no route to hand over a brief.
        repo = Path(tempfile.mkdtemp())
        with mock.patch.object(hz, "intermediary_prompt", return_value=self.pdir / "p.md"):
            cmd = hz.intermediary_cmd(self.pdir, str(repo), bg=True, ask_id="t-1")
            whole = hz.intermediary_cmd(self.pdir, str(repo))
        sc = hz.item_scratch(self.pdir, "t-1")
        self.assertTrue(sc.is_dir())
        tools = cmd[cmd.index("--tools") + 1:cmd.index("--allowedTools")]
        allow = cmd[cmd.index("--allowedTools") + 1:cmd.index("--permission-mode")]
        self.assertIn("Write", tools)
        self.assertIn("Edit", tools)
        self.assertEqual([r for r in allow if not r.startswith("Bash(")], [f"Edit(/{sc}/**)"])
        self.assertIn(str(sc), cmd[cmd.index("--add-dir") + 1:cmd.index("--tools")])
        self.assertNotIn(".claude", str(sc))           # Claude Code protects ~/.claude
        self.assertNotIn("Write", whole[whole.index("--tools"):whole.index("--allowedTools")])
        self.assertIn(str(sc / "brief.md"), hz.item_start(self.pdir, str(repo), {"id": "t-1"}))

    def scratch_home(self):
        d = Path(tempfile.mkdtemp())
        m = mock.patch.object(hz, "ASK_SCRATCH", d / "asks")
        m.start()
        self.addCleanup(m.stop)
        self.addCleanup(shutil.rmtree, d, True)

    def test_scratch_files_are_read_and_other_paths_stay_text(self):
        sc = hz.item_scratch(self.pdir, "t-1")
        sc.mkdir(parents=True)
        (sc / "r.md").write_text("long `reply` with $x")
        other = self.pdir / "asks" / "t-1.json"
        self.assertEqual(hz.scratch_text(self.pdir, "t-1", str(sc / "r.md")),
                         "long `reply` with $x")
        self.assertEqual(hz.scratch_text(self.pdir, "t-1", str(other)), str(other))
        self.assertEqual(hz.scratch_text(self.pdir, "t-2", str(sc / "r.md")), str(sc / "r.md"))
        self.assertEqual(hz.scratch_text(self.pdir, "t-1", "plain words"), "plain words")

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

    def test_a_command_run_through_the_harness_is_recorded_and_done_says_which_ran(self):
        # Log 166: three commands, one ran, and nothing could say which.
        self.rec.update(kind="action", asker_node="dev", runs=[
            "echo first-out; exit 3", "cd /tmp", "echo second-out", "echo never run"])
        self.path.write_text(json.dumps(self.rec))
        with mock.patch("sys.stdout", io.StringIO()):
            self.assertEqual(hz.ask_exec(self.pdir, self.path, self.rec, 1), 3)
            self.assertEqual(hz.ask_exec(self.pdir, self.path, self.rec, 3), 0)
        for n in (2, 0, 5):                                   # a cd; out of range
            with self.assertRaises(SystemExit):
                hz.ask_exec(self.pdir, self.path, self.rec, n)
        self.assertIn("changes your shell's directory", sys.stderr.getvalue())
        rec = json.loads(self.path.read_text())
        self.assertEqual([(e["n"], e["exit"]) for e in rec["run_log"]], [(1, 3), (3, 0)])
        self.assertIn("first-out", Path(rec["run_log"][0]["log"]).read_text())
        words = [hz.run_word(r) for r in hz.runs_status(rec)]
        self.assertTrue(words[0].startswith("exit 3 at "))
        self.assertIn("output: ", words[0])
        self.assertEqual(words[1], "a cd, typed by hand: not recorded")
        self.assertTrue(words[2].startswith("exit 0 at "))
        self.assertEqual(words[3], "no record of being run")
        self.assertEqual([r["n"] for r in hz.runs_unclean(rec)], [1, 4])
        self.assertEqual(len((hz.run_dir(self.pdir, "t-1") / "runs.jsonl").read_text().splitlines()), 2)
        d = hz.ask_done(self.pdir, self.path, rec, "ran them")
        self.assertEqual([r["n"] for r in d["unclean"]], [1, 4])
        (m,) = hz.MAIL().unread(self.pdir, "dev")
        self.assertIn("NOT every command is recorded as run cleanly (2 of 3)", m["text"])
        self.assertIn("4. echo never run — no record of being run", m["text"])
        line = json.loads((self.pdir / "owner" / "done.jsonl").read_text().splitlines()[-1])
        self.assertEqual(len(line["run_log"]), 2)
        self.assertEqual(json.loads(self.path.read_text())["state"], "done")

    def test_every_long_message_between_models_carries_a_tldr_and_the_owner_s_never(self):
        # Owner, 2026-10-14: the pane folds each model message to the line the
        # intermediary wrote, and never the owner's own.
        long = "dev checked the 791 depth cells against three labs' own sheets. " * 4
        with self.assertRaises(SystemExit):
            hz.ask_reply(self.path, self.rec, long)                     # needs one
        self.assertIn("needs a --tldr", sys.stderr.getvalue())
        with self.assertRaises(SystemExit):
            hz.ask_reply(self.path, self.rec, long, tldr="x" * 121)
        hz.ask_reply(self.path, self.rec, long, tldr="the depths are metres, checked")
        hz.ask_reply(self.path, self.rec, "yes.")                         # short: its own TLDR
        hz.ask_to(self.pdir, self.repo, self.path, self.rec, "dev", long, tldr="  check   the labs ")
        hz.ask_msg(self.path, self.rec, "dev", long)
        hz.ask_msg(self.path, self.rec, "owner", long)
        th = json.loads(self.path.read_text())["thread"]
        self.assertEqual([t.get("tldr") for t in th],
                         ["the depths are metres, checked", None, "check the labs", None, None])
        t = hz.ask_tldr(self.path, self.rec, 4, "dev: all 791 are metres")   # a node's, afterwards
        self.assertEqual(json.loads(self.path.read_text())["thread"][3]["tldr"], t["tldr"])
        for n in (5, 0, 9):                                               # the owner's; out of range
            with self.assertRaises(SystemExit):
                hz.ask_tldr(self.path, self.rec, n, "x")
        self.assertIn("never summarised", sys.stderr.getvalue())

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

    def test_msg_from_a_session_names_its_node(self):
        # obs 93: a bare Ctx() has no tree until require_enrolled(); --msg from
        # any session crashed, and it is the one answer route to an intermediary.
        class C:
            def require_enrolled(self):
                self.tree = {"nodes": {"main": {}}}
            def node(self):
                return "main", self.tree["nodes"]["main"]
        with mock.patch.object(hz, "Ctx", C):
            code, wake, _ = self.cli(["t-1", "--msg", "the answer"],
                                     {"CLAUDE_CODE_SESSION_ID": "s" * 36})
        self.assertEqual(code, 0)
        self.assertEqual(json.loads(self.path.read_text())["thread"][-1]["by"], "main")
        wake.assert_called_once()

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
        # The runner proves the memory caps when it starts (two real processes,
        # over a second). That has its own tests; every other runner test skips it.
        self.caps_watch = hz.caps_watch
        cw = mock.patch.object(hz, "caps_watch")
        cw.start(); self.addCleanup(cw.stop)
        self.runs = self.root / "runs"
        for m in (mock.patch.object(hz, "RUNS_HOME", self.runs),
                  mock.patch.object(hz, "TESTQ_IDLE", 0),
                  mock.patch.object(hz, "testq_ensure_runner")):
            m.start(); self.addCleanup(m.stop)

    def run_queue(self):
        with mock.patch("sys.stdout", io.StringIO()), mock.patch("signal.signal"):
            hz.testd(self.state, self.repo)

    def test_a_command_is_estimated_from_its_own_runs_and_says_when_it_overruns(self):
        # Log 103: a timing job read "done in under a minute" 27 minutes in.
        def done(cmd, secs):
            j, _ = hz.testq_submit(self.ctx, "cmd", self.sha, "dev", "s", command=cmd)
            j.update(state="done", started="2026-10-06T10:00:00+1100",
                     finished=time.strftime("%Y-%m-%dT%H:%M:%S%z",
                                            time.localtime(hz._epoch("2026-10-06T10:00:00+1100") + secs)))
            hz.testq_save(self.ctx, j)
        done("echo probe", 5)
        self.assertEqual(hz.testq_duration(self.ctx, "cmd", None, "echo probe"), 5)
        self.assertIsNone(hz.testq_duration(self.ctx, "cmd", None, "sh time-every-file"))
        done("sh time-every-file", 600)
        j, _ = hz.testq_submit(self.ctx, "cmd", self.sha, "dev", "s", command="sh time-every-file")
        j.update(state="running", started=time.strftime("%Y-%m-%dT%H:%M:%S%z",
                                                        time.localtime(time.time() - 1500)))
        hz.testq_save(self.ctx, j)
        self.assertAlmostEqual(hz.testq_overdue(self.ctx, j), 900, delta=5)

    def test_slot_commands_are_listed_in_order_and_go_before_the_queue(self):
        # Log 104: three of the owner's writes held the slot and showed nowhere.
        d = hz.testq_dir(self.ctx) / "slots"
        d.mkdir(parents=True, exist_ok=True)
        (d / "999999.json").write_text(json.dumps({"pid": 999999, "state": "waiting",
                                                   "since": "2026-10-06T10:00:00+1100"}))
        for pid, since in ((os.getpid(), "2026-10-06T10:02:00+1100"),
                           (os.getppid(), "2026-10-06T10:01:00+1100")):
            (d / f"{pid}.json").write_text(json.dumps({"pid": pid, "state": "waiting", "who": "owner",
                                                       "since": since, "command": "import"}))
        ts = hz.slot_tickets(self.ctx)
        self.assertEqual([t["pid"] for t in ts], [os.getppid(), os.getpid()])   # oldest first
        self.assertFalse((d / "999999.json").exists())                          # its process is gone
        hz.testq_submit(self.ctx, "cmd", self.sha, "dev", "s", command="echo queued")
        started = []
        with mock.patch.object(hz, "testd_start", side_effect=lambda *a, **k: started.append(1)), \
             mock.patch.object(hz.time, "sleep", side_effect=SystemExit), \
             mock.patch("sys.stdout", io.StringIO()), mock.patch("signal.signal"):
            with self.assertRaises(SystemExit):
                hz._testd_loop(self.ctx)
        self.assertEqual(started, [])                                          # waited for the slot

    def test_rank_0_or_a_lead_promotes_and_a_lane_touches_only_its_own(self):
        # Log 98: the critical-path job sat two hours behind full checks.
        tree = {"main": None, "dev": "main", "dev_1": "dev", "dev_2": "dev"}
        c = self.ctx
        c.require_enrolled = lambda: None
        c.children = lambda n: [k for k, p in tree.items() if p == n]
        c.rank = lambda n: 0 if n == "main" else 1 if n == "dev" else 2
        a, _ = hz.testq_submit(c, "cmd", self.sha, "dev_2", "s", command="echo a")
        b, _ = hz.testq_submit(c, "cmd", self.sha, "dev_1", "s", command="echo b")
        args = lambda **k: mock.Mock(**dict(dict(command=[], cancel=None, log=None,
                                                 promote=None, why=None), **k))
        def as_node(n, **k):
            c.node = lambda: (n, {})
            with mock.patch.object(hz, "Ctx", return_value=c), \
                 mock.patch.dict(os.environ, {"CLAUDE_CODE_SESSION_ID": "s" * 36}), \
                 redirect_stdout(io.StringIO()) as o:
                try:
                    hz.cmd_test(args(**k)); return 0, o.getvalue()
                except SystemExit as e:
                    return e.code, o.getvalue()
        self.assertNotEqual(as_node("dev_1", promote=b["id"], why="mine")[0], 0)   # a lane
        self.assertNotEqual(as_node("dev_1", cancel=a["id"])[0], 0)                # not its job
        self.assertEqual(as_node("dev", promote=b["id"], why="gates svi-ddl")[0], 0)
        q = hz.testq_order(hz.testq_jobs(c, ("queued",)))
        self.assertEqual([j["id"] for j in q], [b["id"], a["id"]])
        self.assertEqual(q[0]["queue"], "priority")
        rung = list((self.state / "doorbell" / "dev_1" / "inbox").glob("*.json"))
        self.assertIn("front of the queue", json.loads(rung[0].read_text())["text"])
        self.assertEqual(as_node("dev_1", cancel="all")[0], 0)                     # its own only
        self.assertEqual([j["id"] for j in hz.testq_jobs(c, ("queued",))], [a["id"]])

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

    def arm_reports(self):
        """good ran 10s, 20s, 30s; bad 100s (a timed-out bad row is a cap, not a time)."""
        hz._ARM_SECONDS.clear()
        d = self.state / "checks"
        d.mkdir(exist_ok=True)
        for k, (g, b) in enumerate(((10, 100), (20, 900), (30, 100))):
            (d / f"s{k}.json").write_text(json.dumps({"checks": [
                {"name": "good", "seconds": g},
                {"name": "bad", "seconds": b, "timedOut": b == 900}]}))
        self.addCleanup(hz._ARM_SECONDS.clear)

    def test_a_check_is_estimated_from_its_arms_own_times(self):
        # Log 111: a one-arm job read as a full check, "done in about 42m".
        self.arm_reports()
        self.assertEqual(hz.testq_duration(self.ctx, "check", ["good"]), 20)
        self.assertEqual(hz.testq_duration(self.ctx, "check", None), 120)
        self.assertIsNone(hz.testq_duration(self.ctx, "check", ["new-arm"]))

    def test_a_running_check_counts_down_by_arm(self):
        self.arm_reports()
        now = time.time()
        stamp = lambda t: time.strftime("%Y-%m-%dT%H:%M:%S%z", time.localtime(t))
        hz.testq_save(self.ctx, {"id": "r", "kind": "check", "sha": "y", "state": "running",
                                 "arms": None, "requested_by": [], "at": stamp(now - 100),
                                 "started": stamp(now - 90), "done_arms": 1, "arm": "bad",
                                 "arm_started": stamp(now - 40), "pid": os.getpid()})
        job = {"id": "new", "kind": "check", "arms": ["good"], "state": "queued",
               "at": stamp(now)}
        hz.testq_save(self.ctx, dict(job, requested_by=[]))
        self.assertAlmostEqual(hz.testq_wait_estimate(self.ctx, job), 60 + 20, delta=3)

    # ── the memory ledger (owner, 2026-10-09) ─────────────────────────────
    def ledger(self, arms, jobs, pool=None, cores=10, starve=None, during=None):
        """Run the real runner over ad-hoc arms. arms: [(name, body, estimate,
        exclusive)]; jobs: [[arm names], ...] submitted in order, a little apart.
        Each arm logs `name start end`. -> (spans, runner output, jobs)."""
        log = self.root / "arms.log"
        log.unlink(missing_ok=True)
        checks = [{"name": n, "blindSpot": "-",
                   "command": f"echo {n} $(date +%s.%N) >> {log}; {body}; "
                              f"echo {n} $(date +%s.%N) >> {log}"} for n, body, _, _ in arms]
        (self.repo / ".harness" / "manifest.json").write_text(json.dumps({"checks": checks}))
        spec = {n: (est, ex) for n, _, est, ex in arms}
        for k, names in enumerate(jobs):
            hz.testq_submit(self.ctx, "check", self.sha, f"n{k}", "s", arms=sorted(names),
                            tests={n: hz.test_spec(hz.parse_mem(spec[n][0]), 1, spec[n][1])
                                   for n in names})
            time.sleep(0.02)
        hz._ARM_SECONDS.clear()
        ps = [mock.patch.object(hz, "test_pool", return_value=(
            hz.parse_mem(pool) if pool else 16 * 2**30, cores))]
        if starve is not None:
            ps.append(mock.patch.object(hz, "TEST_STARVE", starve))
        for m in ps:
            m.start()
        try:
            with mock.patch("sys.stdout", io.StringIO()) as out, mock.patch("signal.signal"):
                if during:
                    th = threading.Thread(target=hz.testd, args=(self.state, self.repo))
                    th.start(); during(); th.join()
                else:
                    hz.testd(self.state, self.repo)
        finally:
            for m in ps:
                m.stop()
        span = {}
        for line in log.read_text().split("\n") if log.exists() else []:
            if line.strip():
                n, ts = line.split()
                span.setdefault(n, []).append(float(ts))
        return span, out.getvalue(), hz.testq_jobs(self.ctx)

    def needs_cgroups(self):
        if not hz.cgroup_caps()[0]:
            self.skipTest("systemd-run --user can't make capped scopes here")

    @staticmethod
    def overlap(span, a, b):
        return span[a][0] < span[b][1] and span[b][0] < span[a][1]

    def test_tests_from_two_jobs_pack_side_by_side_within_the_pool(self):
        self.needs_cgroups()
        t0 = time.time()
        span, out, jobs = self.ledger([(n, "sleep 2", "256M", False) for n in ("a1", "a2", "b1", "b2")],
                                      [["a1", "a2"], ["b1", "b2"]])
        self.assertLess(time.time() - t0, 5)
        self.assertTrue(self.overlap(span, "a1", "b1") and self.overlap(span, "a2", "b2"))
        self.assertEqual([j["state"] for j in jobs], ["done", "done"])
        for m in re.finditer(r"reserved (\S+) of (\S+),", out):
            self.assertLessEqual(hz.parse_mem(m.group(1)), hz.parse_mem(m.group(2)))

    def test_the_pool_holds_tests_back_and_one_bigger_than_it_runs_alone(self):
        self.needs_cgroups()
        # need = 256M x 1.2 = 307M: two fit a 700M pool, the third waits.
        span, _, _ = self.ledger([(f"t{i}", "sleep 1", "256M", False) for i in range(3)],
                                 [["t0", "t1", "t2"]], pool="700M")
        self.assertTrue(self.overlap(span, "t0", "t1"))
        self.assertFalse(self.overlap(span, "t2", "t0") and self.overlap(span, "t2", "t1"))
        span, _, jobs = self.ledger([("big", "sleep 0.5", "1G", False),
                                     ("s1", "sleep 0.5", "64M", False)], [["big"], ["s1"]],
                                    pool="700M")
        self.assertFalse(self.overlap(span, "big", "s1"))
        self.assertTrue(all(j["state"] == "done" for j in jobs))

    def test_an_exclusive_test_runs_alone(self):
        self.needs_cgroups()
        span, _, _ = self.ledger([("x", "sleep 0.5", "64M", True), ("y", "sleep 0.5", "64M", False),
                                  ("z", "sleep 0.5", "64M", False)], [["x"], ["y", "z"]])
        self.assertFalse(self.overlap(span, "x", "y") or self.overlap(span, "x", "z"))
        self.assertTrue(self.overlap(span, "y", "z"))

    def test_the_oldest_test_stops_backfill_once_it_has_waited_too_long(self):
        self.needs_cgroups()
        arms = [("s1", "sleep 1.5", "256M", False), ("big", "sleep 0.5", "500M", False),
                ("s2", "sleep 0.5", "256M", False)]
        span, _, _ = self.ledger(arms, [["s1"], ["big"], ["s2"]], pool="700M", starve=600)
        self.assertLess(span["s2"][0], span["big"][0])           # backfill while it is young
        span, out, _ = self.ledger(arms, [["s1"], ["big"], ["s2"]], pool="700M", starve=0)
        self.assertGreaterEqual(span["s2"][0], span["big"][0])   # it has waited: it goes first
        self.assertIn("nothing else starts until it does", out)

    def test_a_waiting_test_outweighs_a_fitting_one_only_once_it_has_waited_enough(self):
        # Owner, 2026-10-09: tests keep being added while they fit, weighted by
        # how long they've waited; sometimes the waiting one goes first even
        # though a newer one fits.
        M = 2**20
        running = {("r", "s1"): {"need": 307 * M, "threads": 1, "alone": False,
                                 "node": "x", "name": "s1",
                                 "thread": mock.Mock(is_alive=lambda: True)}}

        def pick(big_wait, small_wait):
            now = time.time()
            jobs = [{"id": "jb", "kind": "check", "t": now - big_wait, "requested_by": [],
                     "tests": {"big": hz.test_spec(500 * M)}},
                    {"id": "js", "kind": "check", "t": now - small_wait, "requested_by": [],
                     "tests": {"small": hz.test_spec(256 * M)}}]
            S = {"open": {}, "running": dict(running), "slot": object(), "said": ""}
            started = []
            with mock.patch.object(hz, "testq_jobs", return_value=jobs), \
                 mock.patch.object(hz, "test_pool", return_value=(700 * M, 8)), \
                 mock.patch.object(hz, "arm_seconds", return_value={}), \
                 mock.patch.object(hz, "test_seconds", return_value=None), \
                 mock.patch.object(hz, "slot_tickets", return_value=[]), \
                 mock.patch.object(hz, "halted", return_value=False), \
                 mock.patch.object(hz, "testd_ledger"), \
                 mock.patch.object(hz, "TEST_STARVE", 600), \
                 mock.patch.object(hz, "testd_start",
                                   side_effect=lambda c, S, j, n, *a: started.append(n)), \
                 mock.patch("sys.stdout", io.StringIO()) as out:
                hz.testd_tick(self.ctx, S)
            return started, out.getvalue()

        self.assertEqual(pick(300, 0)[0], ["small"])        # 1.5 against 2 x 1: it fits, it goes
        started, out = pick(900, 0)                         # 2.5 against 2 x 1: held for big
        self.assertEqual(started, [])
        self.assertIn("big (jb) has waited", out)
        self.assertEqual(pick(900, 300)[0], ["small"])      # 2.5 against 2 x 1.5: the small goes

    def test_a_never_run_test_runs_alone_uncapped_and_its_peak_is_kept(self):
        # Log 130: --memory arm=? for an arm with no history.
        self.needs_cgroups()
        alloc = "python3 -c 'import time; x = bytearray(80 * 2**20); time.sleep(0.3)'"
        span, _, jobs = self.ledger([("new", alloc, "?", False), ("old", "sleep 0.5", "64M", False)],
                                    [["new", "old"]])
        self.assertFalse(self.overlap(span, "new", "old"))
        self.assertTrue(all(j["state"] == "done" for j in jobs))
        rep = json.loads(hz.shared_report_path(self.ctx, self.sha).read_text())
        r = {x["name"]: x for x in rep["checks"]}
        self.assertFalse(r["new"]["memoryKilled"])
        self.assertGreater(r["new"]["peakMemory"], 80 * 2**20)
        self.assertGreater(hz.usage_for(self.ctx, "new")[-1]["peak"], 80 * 2**20)
        self.assertEqual(hz.usage_suggest(self.ctx, "new"), hz.fmt_mem(r["new"]["peakMemory"]))

    # ── memory caps: proven, visible, always on (log 142, owner 2026-10-11) ──
    def arm(self, body, cap, how, limit=20):
        d = Path(tempfile.mkdtemp())
        m = {}
        r = hz.run_arm(f"{sys.executable} -c {hz.shlex.quote(body)}", d, limit, d / "o", d / "e",
                       cap=cap, meter=m, how=how)
        return r, m

    def test_with_no_system_cap_the_harness_watches_and_kills(self):
        # After the 22:40 restart 246 tests ran with no ceiling. No systemd needed here.
        M = 2**20
        take = "import time; x = bytearray({} * 2**20); time.sleep({})"
        (code, _, _, timed_out), m = self.arm(take.format(200, 10), 64 * M, "watch")
        self.assertTrue(m["oom"])
        self.assertEqual((code, timed_out, m["how"]), (137, False, "watch"))
        self.assertGreater(m["peak"], 64 * M)
        (code, _, _, _), m = self.arm(take.format(40, 1.2), 64 * M, "watch")
        self.assertEqual((code, m.get("oom")), (0, None))                # under it: finishes
        self.assertTrue(30 * M <= m["peak"] <= 64 * M)
        self.assertTrue(m["sampled"])

    def test_the_watch_counts_a_child_that_left_the_tree(self):
        # A child that detaches itself (setsid, its parent gone) is still the arm's.
        M = 2**20
        hog = f"{sys.executable} -c 'import time; x = bytearray(150 * 2**20); time.sleep(20)'"
        body = ("import subprocess, time; "
                f"subprocess.Popen({hog!r}, shell=True, start_new_session=True); time.sleep(20)")
        t0 = time.time()
        (code, _, _, _), m = self.arm(body, 64 * M, "watch")
        self.assertTrue(m["oom"])
        self.assertLess(time.time() - t0, 10)

    def test_a_timed_out_test_keeps_its_peak(self):
        # 2026-10-11 12:56: killing a timed-out arm killed the wrapper that
        # writes the scope's peak, so the row had none.
        self.needs_cgroups()
        (code, _, _, timed_out), m = self.arm(
            "import time; x = bytearray(50 * 2**20); time.sleep(30)", None, "system", limit=2)
        self.assertEqual((code, timed_out), (124, True))
        self.assertGreater(m["peak"], 40 * 2**20)

    def test_the_proof_names_the_way_that_works_and_records_it(self):
        def proved(system_ok, proofs):
            it = iter(proofs)
            with mock.patch.object(hz, "cgroup_caps",
                                   return_value=(system_ok, "" if system_ok else "no bus")), \
                 mock.patch.object(hz, "caps_proof", side_effect=lambda how, tmp: next(it)):
                return hz.caps_selftest(self.state)
        c = proved(True, [(True, "")])
        self.assertEqual((c["how"], c["proved"]), ("system", True))
        self.assertIsNone(hz.caps_line(c))                               # the normal case is silent
        self.assertEqual(hz.caps_state(self.state)["how"], "system")
        c = proved(True, [(False, "not killed"), (True, "")])            # a scope, but no kill
        self.assertEqual((c["how"], c["proved"]), ("watch", True))
        self.assertIn("the proof failed: not killed", c["why"])
        self.assertEqual(hz._CGROUP_BAD[0], c["why"])
        hz._CGROUP_BAD[0] = None
        c = proved(False, [(True, "")])
        self.assertEqual((c["how"], c["why"]), ("watch", "no bus"))
        self.assertIn("capped by the harness's own watch", hz.caps_line(c))
        self.assertIn("loginctl enable-linger", hz.caps_line(c))
        c = proved(False, [(False, "nothing was killed")])
        self.assertEqual((c["how"], c["proved"]), ("none", False))
        self.assertIn("MEMORY CAPS OFF", hz.caps_line(c))

    def test_both_ways_of_capping_pass_the_real_proof(self):
        self.assertEqual(hz.caps_proof("watch", self.root / "pw"), (True, ""))
        if hz.cgroup_caps()[0]:
            self.assertEqual(hz.caps_proof("system", self.root / "ps"), (True, ""))

    def test_a_report_says_how_tests_were_capped_and_when_one_was_not_measured(self):
        rows = [{"name": "a", "exit": 0, "seconds": 1.0, "peakMemory": 5 * 2**20, "capBy": "watch"},
                {"name": "b", "exit": 0, "seconds": 1.0, "peakMemory": None, "capBy": "watch"},
                {"name": "old", "exit": 0, "seconds": 1.0, "peakMemory": None}]
        out = lambda caps: self.printed(hz.print_check_report, hz.make_check_report(
            "dev", "abc", rows, 0, None, **({"caps": caps} if caps else {})), None)
        o = out({"how": "watch", "proved": True, "why": "Failed to connect to bus"})
        self.assertIn("memory: capped by the harness's own watch", o.splitlines()[0] + o.splitlines()[1])
        self.assertIn("peak not recorded", [l for l in o.splitlines() if " b " in l][0])
        self.assertNotIn("peak not recorded", [l for l in o.splitlines() if " old " in l][0])
        self.assertIn("MEMORY CAPS OFF", out({"how": "none", "proved": False}))
        self.assertNotIn("memory:", out({"how": "system", "proved": True}))
        self.assertNotIn("memory:", out(None))

    def printed(self, f, *a):
        o = io.StringIO()
        with redirect_stdout(o):
            f(*a)
        return o.getvalue()

    def test_rank_0_is_told_once_when_the_caps_change(self):
        (self.repo / ".harness" / "tree.json").write_text(json.dumps(
            {"nodes": {"main": {"parent": None}, "dev": {"parent": "main"}}}))
        inbox = lambda: [json.loads(f.read_text()) for f in
                         sorted((self.state / "doorbell" / "main" / "inbox").glob("*.json"))]
        watch = {"how": "watch", "proved": True, "why": "no bus", "at": "x"}
        system = {"how": "system", "proved": True, "why": "", "at": "x"}

        def start(result):                       # a fresh runner each time, as when the queue empties
            def proof(state):
                hz._save(Path(state) / "testq" / "meta" / "caps.json", result)
                return result
            with mock.patch.object(hz, "caps_selftest", side_effect=proof), \
                 mock.patch("sys.stdout", io.StringIO()) as out:
                self.caps_watch(self.ctx, {})
            return out.getvalue()
        self.assertIn("memory caps proved", start(system))
        self.assertFalse((self.state / "doorbell" / "main").exists())    # the normal case: no mail
        self.assertIn("capped by the harness's own watch", start(watch))
        self.assertEqual([(m["priority"], m["from"]) for m in inbox()], [("high", "test queue")])
        start(watch)                                                     # the next runner: no repeat
        self.assertEqual(len(inbox()), 1)
        start(system)
        (back,) = [m for m in inbox() if m["priority"] == "fyi"]         # good news: an FYI
        self.assertIn("is back and proved", back["text"])
        self.assertEqual(len(inbox()), 2)

    def test_the_runner_finishes_what_runs_then_restarts_on_a_new_install(self):
        ticks = []

        def tick(ctx, S):
            ticks.append(bool(S.get("drain")))
            if len(ticks) == 1:
                S["running"]["x"] = object()     # something is running when the install lands
            elif len(ticks) == 3:
                S["running"].clear()
        stamps = iter([["old"], ["old"]] + [["new"]] * 9)   # the install lands after one pass
        with mock.patch.object(hz, "testq_recover"), mock.patch("signal.signal"), \
             mock.patch.object(hz, "testd_tick", side_effect=tick), \
             mock.patch.object(hz, "testq_jobs", return_value=[{"id": "queued-behind"}]), \
             mock.patch.object(hz, "ringer_stamp", side_effect=lambda p: next(stamps)), \
             mock.patch.object(hz.time, "sleep"), \
             mock.patch.object(hz.os, "execv", side_effect=SystemExit) as ex, \
             mock.patch("sys.stdout", io.StringIO()) as out, self.assertRaises(SystemExit):
            hz._testd_loop(self.ctx)
        self.assertEqual(ticks, [False, True, True])     # draining, and not restarted while it ran
        self.assertEqual(ex.call_args.args[1][2], "testd")
        self.assertIn("finishing what runs", out.getvalue())

    def test_a_draining_runner_opens_no_job_but_an_open_one_runs_out_its_arms(self):
        # Log 153: "start nothing" left an open job's last arm waiting for good,
        # so the job never closed and the restart never came: 45 minutes.
        jobs = [{"id": "j", "kind": "check", "t": time.time(), "requested_by": [],
                 "tests": {"a": hz.test_spec(2**20)}}]
        started = []

        def tick(is_open):
            with mock.patch.object(hz, "testq_jobs", return_value=jobs), \
                 mock.patch.object(hz, "test_pool", return_value=(2**30, 8)), \
                 mock.patch.object(hz, "arm_seconds", return_value={}), \
                 mock.patch.object(hz, "slot_tickets", return_value=[]), \
                 mock.patch.object(hz, "halted", return_value=False), \
                 mock.patch.object(hz, "testd_ledger"), \
                 mock.patch.object(hz, "testd_open", side_effect=AssertionError("opened a job")), \
                 mock.patch.object(hz, "testd_start",
                                   side_effect=lambda ctx, S, j, name, *a: (
                                       started.append(name),
                                       j["tests"][name].update(state="running"))):
                hz.testd_tick(self.ctx, {"open": {"j": {"job": jobs[0]}} if is_open else {},
                                         "running": {}, "slot": object(), "said": "",
                                         "drain": True})
        tick(False)
        self.assertEqual(started, [])                # a queued job is left for the new runner
        tick(True)
        self.assertEqual(started, ["a"])             # an open job's waiting arm still starts

    def test_an_outage_cannot_push_the_measured_runs_out_of_the_history(self):
        for i in range(5):
            hz.usage_append(self.ctx, "arm", {"peak": (i + 1) * 2**20, "seconds": 1})
        for _ in range(8):                                               # the outage: no peaks
            hz.usage_append(self.ctx, "arm", {"peak": None, "seconds": 2})
        h = hz.usage_for(self.ctx, "arm")
        self.assertEqual([r["peak"] // 2**20 for r in h if r["peak"]], [1, 2, 3, 4, 5])
        self.assertEqual(sum(1 for r in h if not r["peak"]), 5)
        self.assertEqual(hz.usage_suggest(self.ctx, "arm"), "3M")

    def test_twice_the_estimate_kills_and_spill_below_that_runs_on(self):
        self.needs_cgroups()
        alloc = "python3 -c 'import time; x = bytearray({} * 2**20); time.sleep(0.3)'"
        span, _, jobs = self.ledger([("hog", alloc.format(200), "32M", False),
                                     ("spill", alloc.format(60), "40M", False)], [["hog", "spill"]])
        rep = json.loads(hz.shared_report_path(self.ctx, self.sha).read_text())
        r = {x["name"]: x for x in rep["checks"]}
        self.assertTrue(r["hog"]["memoryKilled"])
        self.assertLessEqual(r["hog"]["peakMemory"], 64 * 2**20)
        self.assertFalse(r["spill"]["memoryKilled"])
        self.assertGreater(r["spill"]["peakMemory"], 40 * 2**20)    # over its estimate, under 2x
        self.assertEqual(r["spill"]["estimate"], 40 * 2**20)
        self.assertEqual(rep["failed"], 1)
        self.assertTrue(hz.usage_for(self.ctx, "hog")[-1]["killed"])
        self.assertEqual(r["spill"]["lastPeaks"], [r["spill"]["peakMemory"]])

    def test_cancelling_one_job_leaves_the_other_running(self):
        self.needs_cgroups()
        def cancel():
            time.sleep(1)
            (a,) = [j for j in hz.testq_jobs(self.ctx, ("running",)) if j["arms"] == ["c1"]]
            hz.testq_cancel(self.ctx, a)
        span, _, jobs = self.ledger([("c1", "sleep 3", "64M", False), ("c2", "sleep 2", "64M", False)],
                                    [["c1"], ["c2"]], during=cancel)
        st = {tuple(j["arms"]): j["state"] for j in jobs}
        self.assertEqual(st, {("c1",): "cancelled", ("c2",): "done"})
        self.assertEqual(len(span["c1"]), 1)                     # killed: it never logged its end

    def test_usage_keeps_the_last_five_runs_and_suggests_their_median(self):
        for i in range(7):
            hz.usage_append(self.ctx, "arm", {"peak": (i + 1) * 2**20})
        self.assertEqual([r["peak"] // 2**20 for r in hz.usage_for(self.ctx, "arm")], [3, 4, 5, 6, 7])
        self.assertEqual(hz.usage_suggest(self.ctx, "arm"), "5M")
        self.assertIsNone(hz.usage_suggest(self.ctx, "never"))

    def test_estimates_are_parsed_per_test(self):
        est, bad = hz.parse_estimates("a=2G, b=500M,c=x", ["a", "b", "c"])
        self.assertEqual((est, bad), ({"a": 2 * 2**30, "b": 500 * 2**20}, ["c=x"]))
        self.assertEqual(hz.parse_estimates("1G", ["only"])[0], {"only": 2**30})
        self.assertEqual(hz.parse_estimates("1G", ["a", "b"])[1], ["1G"])
        # Log 130: a written ? is a never-run arm: alone, uncapped, measured.
        self.assertEqual(hz.parse_estimates("a=?, b=1G", ["a", "b"]), ({"a": None, "b": 2**30}, []))
        self.assertEqual(hz.parse_estimates("z=?", ["a"])[1], ["z=?"])
        u = hz.test_spec(None, 2)
        self.assertEqual((u["need"], u["ceiling"], u["exclusive"], u["threads"]), (None, None, True, 2))
        t = hz.test_spec(2**30)
        self.assertEqual((t["need"], t["ceiling"]), (int(1.2 * 2**30), 2 * 2**30))

    def test_the_ledger_estimate_packs_what_fits(self):
        (self.repo / ".harness" / "manifest.json").write_text(json.dumps({"checks": [
            {"name": n, "command": "true", "blindSpot": "-"} for n in ("a", "b", "c")]}))
        sp = lambda m: hz.test_spec(m * 2**20)
        j1, _ = hz.testq_submit(self.ctx, "check", self.sha, "x", "s", arms=["a", "b"],
                                tests={"a": sp(256), "b": sp(256)})
        j2, _ = hz.testq_submit(self.ctx, "check", self.sha, "y", "s", arms=["c"],
                                tests={"c": sp(256)})
        with mock.patch.object(hz, "arm_seconds", return_value={"a": 30, "b": 20, "c": 10}):
            with mock.patch.object(hz, "test_pool", return_value=(2**30, 10)):
                self.assertEqual(hz.testq_wait_estimate(self.ctx, j1), 30)   # side by side
                self.assertEqual(hz.testq_wait_estimate(self.ctx, j2), 10)   # backfills now
            with mock.patch.object(hz, "test_pool", return_value=(400 * 2**20, 10)):
                self.assertEqual(hz.testq_wait_estimate(self.ctx, j2), 60)   # one at a time

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



class LogEntries92to102(unittest.TestCase):
    """Log 92-102 (2026-10-06): what should reach the owner or a node does, and
    nothing reads as more certain than it is."""

    def setUp(self):
        self.ctx = FakeCtx({"main": None, "dev": "main", "dev_1": "dev"})
        self.err = mock.patch("sys.stderr", new_callable=io.StringIO)
        self.err.start(); self.addCleanup(self.err.stop)

    def out(self, f, *args):
        o = io.StringIO()
        with redirect_stdout(o):
            f(*args)
        return o.getvalue()

    # 97: a hand-off to the owner with no ask is blocked once
    def test_a_handoff_with_no_ask_is_caught_for_leads_only(self):
        (self.ctx.dir / "asks").mkdir()
        said = ["Reviewed svi-ddl.", "Same as with dev_1, I'll record the review and leave "
                                     "landing to you."]
        self.assertTrue(hz.handoff_unasked(self.ctx, "dev", said))
        self.assertTrue(hz.handoff_unasked(self.ctx, "dev", ["Awaiting operator: integrate it."]))
        self.assertFalse(hz.handoff_unasked(self.ctx, "dev_1", said))          # a lane
        self.assertFalse(hz.handoff_unasked(self.ctx, "main", said))           # "you": rank 0
        self.assertFalse(hz.handoff_unasked(self.ctx, "dev", ["Signed off and integrated."]))
        # Log 177: the true negative is not a hand-off; a negation after it does not cancel one.
        for s in ("Nothing waits on the owner.", "Done. No owner action is needed.",
                  "The owner doesn't need to approve anything here.",
                  "Integrated dev_1; nobody needs the owner for it."):
            self.assertFalse(hz.handoff_unasked(self.ctx, "dev", [s]), s)
        self.assertTrue(hz.handoff_unasked(self.ctx, "dev", [
            "Nothing else is open. This waits on the owner, not on dev_1."]))
        # buried in a summary's body, not its closing words
        self.assertFalse(hz.handoff_unasked(self.ctx, "dev", [
            "The owner is waiting on nothing here.\n\nNext: tfm-store. The doorbell is armed."]))
        (self.ctx.dir / "asks" / "owner-4.json").write_text(json.dumps(
            {"id": "owner-4", "asker_node": "main", "state": "asked"}))
        self.assertFalse(hz.handoff_unasked(self.ctx, "dev", [
            "The rebuild is owner-4; I'll leave landing to you."]))                # names an open ask
        (self.ctx.dir / "asks" / "s-1.json").write_text(json.dumps(
            {"id": "s-1", "asker_node": "dev", "state": "ready"}))
        self.assertFalse(hz.handoff_unasked(self.ctx, "dev", said))            # its own ask is open

    def test_turn_texts_reads_the_whole_last_turn(self):
        f = Path(tempfile.mkdtemp()) / "s.jsonl"
        A = lambda t: {"type": "assistant", "message": {"content": [{"type": "text", "text": t}]}}
        f.write_text("\n".join(json.dumps(r) for r in (
            {"type": "user", "message": {"content": "old prompt"}}, A("old turn"),
            {"type": "user", "message": {"content": "go"}}, A("first"),
            {"type": "user", "message": {"content": [{"type": "tool_result"}]}}, A("second"),
            {"type": "system", "subtype": "turn_duration"})))
        with mock.patch.object(hz, "transcript_for", return_value=f):
            self.assertEqual(hz.turn_texts("s"), ["first", "second"])

    # 101b: the asker withdraws; the owner task takes no notes
    def test_withdraw_by_the_asker_and_rank_0_only(self):
        d = Path(tempfile.mkdtemp())
        (d / "asks").mkdir()
        p = d / "asks" / "owner-2.json"
        rec = {"id": "owner-2", "asker_node": "dev", "state": "asked", "kind": "action",
               "question": "Run x?", "runs": ["x"]}
        p.write_text(json.dumps(rec))
        class C:
            me = "dev_1"
            def require_enrolled(self): pass
            def node(self): return C.me, {}
            def rank(self, n): return {"main": 0, "dev": 1, "dev_1": 2}[n]
        with mock.patch.object(hz, "Ctx", C):
            with self.assertRaises(SystemExit):
                hz.ask_withdraw(d, p, rec, "replaced", "s" * 36)                # someone else's
            with self.assertRaises(SystemExit):
                hz.ask_withdraw(d, p, rec, "", None)                            # no why
            C.me = "main"
            hz.ask_withdraw(d, p, rec, "replaced by owner-4", "s" * 36)         # rank 0 may
        self.assertFalse(p.exists())
        log = json.loads((d / "owner" / "withdrawn.jsonl").read_text())
        self.assertEqual((log["id"], log["by"], log["why"]), ("owner-2", "main", "replaced by owner-4"))

    # 94: delivered mail says how old it is
    def test_mail_shows_its_age(self):
        at = time.strftime("%Y-%m-%dT%H:%M:%S%z", time.localtime(time.time() - 3900))
        self.assertIn("(1h05m ago)", hz.MAIL().render([{"at": at, "from": "main", "text": "x"}]))

    # 92: partial reports and old holds
    def test_a_partial_report_says_so_and_cannot_be_a_baseline(self):
        rows = [{"name": "a", "exit": 0}] + [{"name": f"h{i}", "exit": None, "held": "subset.db by dev"}
                                              for i in range(8)]
        rep = hz.make_check_report("dev", "abc", rows, 0, None)
        self.assertEqual(hz.partial_line(rep),
                         "PARTIAL: 1 of 9 arms ran; 8 NOT RUN (held: subset.db by dev x8)")
        self.assertIn("PARTIAL: 1 of 9", self.out(hz.print_check_report, rep, None))
        self.ctx.worktree = self.ctx.dir
        with mock.patch.object(hz, "git", return_value=(0, "abc", "")), \
             mock.patch.object(hz, "read_check_report", return_value=rep), \
             self.assertRaises(SystemExit):
            hz.set_baseline(self.ctx, "dev", "start")
        self.assertIn("A baseline needs every arm run", sys.stderr.getvalue())

    def test_the_code_root_under_a_document_main_sets_the_baseline(self):
        # Log 131: main is kind doc and never holds dev's code, so the 118 guard
        # (a commit the parent holds) left dev nowhere to set it.
        ctx = FakeCtx({"main": None, "dev": "main", "dev_1": "dev", "dev_1a": "dev_1"})
        ctx.tree["nodes"]["main"]["kind"] = "doc"
        ctx.worktree = ctx.dir
        self.assertIsNone(hz.code_ancestor(ctx, "dev"))
        self.assertEqual(hz.code_ancestor(ctx, "dev_1a"), "dev_1")
        rep = hz.make_check_report("dev", "abc", [{"name": "a", "exit": 0}], 0, None)
        calls = []

        def git(*args, **kw):
            calls.append(args[0])
            return (1, "", "") if args[0] == "merge-base" else (0, "abc", "")
        with mock.patch.object(hz, "git", side_effect=git), \
             mock.patch.object(hz, "read_check_report", return_value=rep), \
             mock.patch("sys.stdout", io.StringIO()):
            hz.set_baseline(ctx, "dev", "surface reds fixed")
            self.assertNotIn("merge-base", calls)                    # no guard at the code root
            self.assertEqual(hz.load_baseline(ctx)["sha"], "abc")
            with self.assertRaises(SystemExit):
                hz.set_baseline(ctx, "dev_1", "not in dev")          # 118 still holds below it
        self.assertIn("is not in dev yet", sys.stderr.getvalue())

    def test_an_old_hold_is_asked_about(self):
        (self.ctx.dir / "holds").mkdir()
        old = time.strftime("%Y-%m-%dT%H:%M:%S%z", time.localtime(time.time() - 2 * 3600))
        (self.ctx.dir / "holds" / "x.json").write_text(json.dumps(
            {"path": "subset.db", "why": "delete", "by": "dev", "until": "", "at": old}))
        with mock.patch.object(hz, "lead_owes", return_value=[]), \
             mock.patch.object(hz, "rank0_owes", return_value=[]):
            items = hz.queue_items(self.ctx, "dev")
            self.assertIn("hold old:subset.db", items)
            self.assertIn("harness hold subset.db --release", items["hold old:subset.db"])
            self.assertTrue(hz.is_debt("hold old:subset.db"))                   # re-reported
            self.assertNotIn("hold old:subset.db", hz.queue_items(self.ctx, "dev_1"))

    # 99: the documenter's new wording, flagged
    def test_new_wording_is_listed_and_risky_words_flagged(self):
        rec = {"pairs": [
            {"op": "move", "file": "M.md", "old": "The remedy is a guard. Measured 2026-10-01: 41 rows.",
             "to": "provenance/M/x.md", "pointer": "History: provenance/M/x.md. This is fixed by a guard."},
            {"file": "M.md", "old": "Loads take 3s.", "new": "Loads take 3s."}]}
        nw = hz.pairs_new_wording(rec)
        self.assertEqual([(s, bool(f)) for _, s, f in nw],
                         [("This is fixed by a guard.", True), ("History: provenance/M/x.md.", False)])

    def test_a_hardened_claim_is_flagged_with_its_reason(self):
        # Log 121: "cannot run today" became "cannot run".
        rec = {"pairs": [{"file": "API.md", "old": "The import cannot run today without the key.",
                          "new": "The import cannot run without the key."},
                         {"file": "API.md", "old": "An endpoint drops a state when it fails.",
                          "new": "An endpoint never drops a state when it fails."}]}
        why = {s: f for _, s, f in hz.pairs_new_wording(rec)}
        self.assertIn("dropped: today", why["The import cannot run without the key."])
        self.assertIn("added: never", why["An endpoint never drops a state when it fails."])

    # 101: a failed recheck leaves the value standing
    def test_a_failed_observation_is_never_the_latest(self):
        fact = {"observations": [{"value": "41", "at": "x"},
                                 {"failed": "exit 2", "command": "c", "at": "y"}]}
        self.assertEqual(hz.latest(fact)["value"], "41")

    def test_from_must_parse(self):
        self.ctx.worktree = self.ctx.dir
        a = mock.Mock(list=False, name="n", is_="41", from_="echo 'unclosed", what=None,
                      recheck=False, retire=None)
        with mock.patch.object(hz, "Ctx", return_value=self.ctx), \
             mock.patch.object(hz, "load_fact", return_value=(self.ctx.dir / "f.json", None)), \
             self.assertRaises(SystemExit):
            hz.cmd_fact(a)
        self.assertIn("--from is not valid shell", sys.stderr.getvalue())


class LogEntries88to91(unittest.TestCase):
    """obs 87, 88, 90 and 91."""

    def setUp(self):
        self.ctx = FakeCtx({"main": None, "dev": "main", "dev_1": "dev"})
        for d in ("briefs", "marks", "waiting", "holds"):
            (self.ctx.dir / d).mkdir()
        self.ctx.repo = self.ctx.dir
        self.err = mock.patch("sys.stderr", new_callable=io.StringIO)
        self.err.start()
        self.addCleanup(self.err.stop)

    def test_a_hold_for_a_task_rings_its_lane_and_answers_its_wait(self):
        (self.ctx.dir / "marks" / "t.json").write_text(json.dumps({"_node": "dev_1"}))
        hz.waiting_path(self.ctx, "dev_1").write_text(json.dumps(
            {"node": "dev_1", "parent": "dev", "asked": "hold subset.db", "since": OLD}))
        with mock.patch.object(hz, "open_marks", return_value={"t": {"_node": "dev_1"}}), \
             redirect_stdout(io.StringIO()):
            hz.hold_tell(self.ctx, "dev", "t", "/data/subset.db")
        rung = list((self.ctx.dir / "doorbell" / "dev_1" / "inbox").glob("*.json"))
        self.assertIn("/data/subset.db", json.loads(rung[0].read_text())["text"])
        w = json.loads(hz.waiting_path(self.ctx, "dev_1").read_text())
        self.assertIn("placed a hold", w["answered"])
        with mock.patch.object(hz, "open_marks", return_value={"u": {"_node": "dev"}}), \
             redirect_stdout(io.StringIO()):
            hz.hold_tell(self.ctx, "dev", "u", "/x")              # its own task: nobody to ring
        self.assertFalse((self.ctx.dir / "doorbell" / "dev").exists())

    def test_sign_off_is_never_folded(self):
        self.assertIn('"sign off:"', Path(hz.__file__).read_text().split("kept = {k: v")[1][:600])

    def transcript(self, recs):
        d = Path(tempfile.mkdtemp()) / "proj"
        d.mkdir()
        sid = "a" * 8 + "-0000-0000-0000-" + "b" * 12
        (d / f"{sid}.jsonl").write_text("\n".join(json.dumps(r) for r in recs) + "\n")
        return d.parent, sid

    def test_spend_window_splits_by_tool_and_window(self):
        u = lambda n, ctx=0: {"input_tokens": n, "output_tokens": 0, "cache_read_input_tokens": ctx,
                              "cache_creation_input_tokens": 0}
        tool = lambda name, **inp: {"type": "tool_use", "name": name, "input": inp}
        recs = [
            {"type": "assistant", "timestamp": "2026-10-06T01:00:00+0000",
             "message": {"usage": u(999), "content": [tool("Read")]}},               # before
            {"type": "assistant", "timestamp": "2026-10-06T02:00:00+0000",
             "message": {"usage": u(100), "content": [tool("Read")]}},
            {"type": "assistant", "timestamp": "2026-10-06T02:01:00+0000",
             "message": {"usage": u(40), "content": [tool("Bash", command="harness check"),
                                                     tool("Bash", command="ls")]}},
            {"type": "system", "subtype": "compact_boundary", "timestamp": "2026-10-06T02:02:00+0000"},
            {"type": "assistant", "timestamp": "2026-10-06T02:03:00+0000",
             "message": {"usage": u(10, ctx=500_000), "content": [{"type": "text", "text": "x"}]}}]
        root, sid = self.transcript(recs)
        with mock.patch.object(hz, "PROJECTS", root):
            w = hz.spend_window(sid, "2026-10-06T01:30:00+0000", None, warn=400_000)
        self.assertEqual(w["totals"]["input"], 150)
        self.assertEqual(w["by"], {"Read": 100, "Bash: test queue": 20, "Bash: other": 20, "talk": 10})
        self.assertEqual((w["after_compact"], w["past_warn"]), (10, 10))

    def test_teardown_removes_an_empty_project_folder_only(self):
        root = Path(tempfile.mkdtemp())
        a, b = root / "proj" / "j1", root / "proj" / "j2"
        a.mkdir(parents=True); b.mkdir()
        with mock.patch.object(hz, "git", return_value=(0, "", "")):
            hz.testq_teardown(self.ctx, {"dir": str(a)})
            self.assertTrue((root / "proj").exists())             # j2 still there
            hz.testq_teardown(self.ctx, {"dir": str(b)})
        self.assertFalse((root / "proj").exists())


class HookPosition(unittest.TestCase):
    """2026-10-12: a hook reads where it stands from the worktree's own files.
    `Ctx()` starts three git processes, and under load on a slow disk those were
    most of a prompt hook that has five seconds."""

    def setUp(self):
        self.root = Path(tempfile.mkdtemp()).resolve()
        self.addCleanup(shutil.rmtree, self.root, True)
        self.repo, self.wt = self.root / "proj", self.root / "proj-dev"
        self.g = lambda cwd, *a: subprocess.run(
            ["git", "-c", "user.name=t", "-c", "user.email=t@t", *a], cwd=cwd, check=True,
            capture_output=True)
        self.repo.mkdir()
        self.g(self.repo, "init", "-q", "-b", "main")
        self.g(self.repo, "commit", "-q", "--allow-empty", "-m", "a")
        self.g(self.repo, "worktree", "add", "-q", "-b", "dev", str(self.wt))
        (self.wt / "src").mkdir()

    def at(self, cwd):
        """What git says there, through the ordinary constructor."""
        was = os.getcwd()
        os.chdir(cwd)
        try:
            return hz.Ctx()
        finally:
            os.chdir(was)

    def test_it_agrees_with_git_in_a_checkout_a_worktree_and_a_folder_inside_one(self):
        for cwd in (self.repo, self.wt, self.wt / "src"):
            a, b = hz.Ctx.from_files(cwd), self.at(cwd)
            for k in ("repo", "worktree", "branch", "slug", "state", "binding_path", "tree_path"):
                self.assertEqual(getattr(a, k), getattr(b, k), (cwd, k))
        with mock.patch.object(hz, "git", side_effect=AssertionError("git was started")):
            self.assertEqual(hz.Ctx.from_files(self.wt).branch, "dev")

    def test_what_it_cannot_read_plainly_it_leaves_to_git(self):
        self.g(self.wt, "checkout", "-q", "--detach")
        self.assertIsNone(hz.Ctx.from_files(self.wt))
        outside = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, outside, True)
        self.assertIsNone(hz.Ctx.from_files(outside))
        # Not enrolled here: the hook asks git, as before.
        was = os.getcwd()
        os.chdir(self.repo)
        try:
            with mock.patch.object(hz, "HOME_STATE", self.root / "state"):
                self.assertEqual(hz.hook_ctx().branch, "main")
        finally:
            os.chdir(was)
        os.chdir(outside)
        try:
            self.assertIsNone(hz.hook_ctx())
        finally:
            os.chdir(was)


class Log152(unittest.TestCase):
    """Log 152 (owner, 2026-10-12): rank 0 writes a brief for any node. The
    leads between are told, and carry the work up one rank at a time."""

    def setUp(self):
        self.ctx = FakeCtx({"main": None, "dev": "main", "dev_dag": "dev", "dev_dag_1": "dev_dag"})
        nodes = self.ctx.tree["nodes"]

        def rank(n, r=0):
            while nodes[n].get("parent"):
                n, r = nodes[n]["parent"], r + 1
            return r
        self.ctx.rank = rank
        self.ctx.worktree = self.ctx.repo = self.ctx.dir
        self.ctx.tree_path = self.ctx.dir / "tree.json"
        for d in ("briefs", "findings"):
            (self.ctx.dir / d).mkdir()

    def brief(self, me, *argv):
        self.ctx.me = self.ctx.branch = me
        out = io.StringIO()
        with mock.patch.object(hz, "Ctx", return_value=self.ctx), \
             mock.patch.dict(os.environ, {"CLAUDE_CODE_SESSION_ID": "s" * 36}), \
             mock.patch.object(hz, "print_delta", lambda *a, **k: None), \
             mock.patch("sys.argv", ["harness", "brief", *argv]), \
             redirect_stdout(out), mock.patch("sys.stderr", out):
            try:
                hz.main(); code = 0
            except SystemExit as e:
                code = e.code or 0
        return code, out.getvalue()

    def load(self, task):
        return hz.load_brief(self.ctx, task)[1]

    def mail(self, node):
        return [json.loads(p.read_text())
                for p in sorted((self.ctx.dir / "doorbell" / node / "inbox").glob("*.json"))]

    def test_rank_0_briefs_a_node_two_ranks_down_and_its_lead_carries_it_up(self):
        code, out = self.brief("main", "environment-dag", "--for", "dev_dag", "--write", "build it")
        self.assertEqual(code, 0, out)
        b = self.load("environment-dag")
        self.assertEqual((b["node"], b["direct_by"], b["text"]), ("dev_dag", "main", "build it"))
        c = self.load("environment-dag.up-dev")
        self.assertEqual((c["node"], c["carries"], c["after"]), ("dev", "environment-dag",
                                                                 ["environment-dag"]))
        self.assertIn("carrier environment-dag.up-dev for dev", out)
        # The carrier opens once the task below it is signed off, and needs no approval.
        self.assertFalse(hz.awaiting(c))
        self.assertTrue(hz.waits_on(self.ctx, c)[0].startswith("after environment-dag"))
        (self.ctx.dir / "marks").mkdir()
        (self.ctx.dir / "marks" / "environment-dag.json").write_text(
            json.dumps({"_node": "dev_dag", "_closed_at": "2026"}))
        self.assertEqual(hz.waits_on(self.ctx, c), [])
        (m,) = self.mail("dev")
        self.assertEqual(m["priority"], "high")                    # it has a session to start
        self.assertIn("main briefed dev_dag directly: 'environment-dag'", m["text"])
        self.assertIn("harness spawn dev_dag", m["text"])
        self.assertIn("you do not hand it down", m["text"])
        # A rewrite by rank 0 tells nobody twice and writes no second carrier.
        code, out = self.brief("main", "environment-dag", "--write", "build it better")
        self.assertEqual(code, 0, out)
        self.assertEqual(len(self.mail("dev")), 1)
        self.assertEqual(self.load("environment-dag")["direct_by"], "main")

    def test_three_ranks_down_every_lead_between_holds_a_carrier(self):
        code, out = self.brief("main", "leaf", "--for", "dev_dag_1", "--write", "do it")
        self.assertEqual(code, 0, out)
        lo, hi = self.load("leaf.up-dev_dag"), self.load("leaf.up-dev")
        self.assertEqual((lo["after"], hi["after"]), (["leaf"], ["leaf.up-dev_dag"]))
        self.assertEqual(self.mail("dev_dag")[0]["priority"], "high")       # the node's own lead
        self.assertEqual(self.mail("dev")[0]["priority"], "low")            # further up: no act yet
        self.assertNotIn("harness spawn", self.mail("dev")[0]["text"])

    def test_a_child_of_rank_0_needs_no_carrier_and_nobody_else_gained_the_right(self):
        code, out = self.brief("main", "seg", "--for", "dev", "--write", "x")
        self.assertEqual(code, 0, out)
        self.assertNotIn("direct_by", self.load("seg"))
        self.assertIsNone(self.load("seg.up-dev"))
        # A lead still writes only for its children, and nobody writes their own.
        code, out = self.brief("dev", "far", "--for", "dev_dag_1", "--write", "x")
        self.assertEqual(code, hz.REFUSED)
        self.assertIn("'dev' does not write the brief for 'dev_dag_1'", out)
        self.assertEqual(self.brief("dev_dag", "own", "--for", "dev_dag", "--write", "x")[0],
                         hz.REFUSED)

    def spawn(self, me, node):
        self.ctx.me = self.ctx.branch = me
        nodes = self.ctx.tree["nodes"]
        idx = {"project": "p", "byBranch": {n: n for n in nodes}, "byWorktree": {},
               "nodes": {n: {"worktree": f"/w/{n}", "branch": n, "parent": s.get("parent"),
                             "rank": self.ctx.rank(n)} for n, s in nodes.items()}}
        started, out = [], io.StringIO()
        with mock.patch.object(hz, "Ctx", return_value=self.ctx), \
             mock.patch.dict(os.environ, {"CLAUDE_CODE_SESSION_ID": "s" * 36}), \
             mock.patch.multiple(
                 hz, load_index=lambda *a, **k: idx, agents_json=lambda *a: [],
                 read_roster=lambda p: None, grants_for=lambda c, n: [],
                 launch_cmd=lambda *a: ["true"], assignment_for=lambda c, n: ("m", "e"),
                 launch_bg=lambda cmd, cwd, env=None: (started.append(cwd), (True, ""))[1],
                 catch_up=lambda *a, **k: ("current", {}), print_delta=lambda *a, **k: None), \
             mock.patch("sys.argv", ["harness", "spawn", node]), \
             redirect_stdout(out), mock.patch("sys.stderr", out):
            try:
                hz.main()
            except SystemExit:
                pass
        return started, out.getvalue()

    def test_rank_0_starts_a_node_on_the_task_it_briefed_directly(self):
        self.brief("main", "environment-dag", "--for", "dev_dag", "--write", "build it")
        started, out = self.spawn("main", "dev_dag")
        self.assertEqual(started, ["/w/dev_dag"], out)
        self.assertIn("starts on environment-dag", out)
        (told,) = [m for m in self.mail("dev") if m["from"] == "main"]
        self.assertEqual(told["priority"], "low")
        self.assertIn("main started dev_dag on 'environment-dag'", told["text"])
        self.assertIn("Nothing for you to start", told["text"])

    def test_rank_0_does_not_start_a_node_on_someone_else_s_task(self):
        self.brief("dev", "devs-own", "--for", "dev_dag", "--write", "dev's work")
        started, out = self.spawn("main", "dev_dag")
        self.assertEqual(started, [])
        self.assertIn("not your child — dev starts it", out)
        # Its own direct brief, queued behind the lead's: said, with how to put it first.
        self.brief("main", "environment-dag", "--for", "dev_dag", "--write", "build it")
        started, out = self.spawn("main", "dev_dag")
        self.assertEqual(started, [])
        self.assertIn("'environment-dag', which you briefed for it, is queued behind 'devs-own'", out)
        self.assertIn("harness queue dev_dag --order environment-dag", out)
        # A lead gained nothing: it starts its own children only.
        self.brief("main", "leaf", "--for", "dev_dag_1", "--write", "x")
        started, out = self.spawn("dev", "dev_dag_1")
        self.assertEqual(started, [])
        self.assertIn("not your child — dev_dag starts it", out)

    def test_a_suggestion_against_it_reaches_rank_0_which_may_resolve_it(self):
        self.brief("main", "environment-dag", "--for", "dev_dag", "--write", "build it")
        code, out = self.brief("dev_dag", "environment-dag", "--suggest", "split the loader out")
        self.assertEqual(code, 0, out)
        self.assertIn("main wrote this brief and decides; it has been told", out)
        (m,) = self.mail("main")
        self.assertEqual((m["from"], m["priority"]), ("dev_dag", "low"))
        self.assertIn("split the loader out", m["text"])
        self.assertIn("harness brief environment-dag --resolve 1", m["text"])
        code, out = self.brief("main", "environment-dag", "--resolve", "1")
        self.assertEqual(code, 0, out)
        self.assertTrue(self.load("environment-dag")["suggestions"][0]["resolved_at"])
        # A node that is neither its lead nor rank 0 still may not.
        self.brief("dev_dag", "environment-dag", "--suggest", "another")
        code, out = self.brief("dev_dag_1", "environment-dag", "--resolve", "2")
        self.assertEqual(code, hz.REFUSED)

    def test_the_lead_may_rewrite_it_and_rank_0_hears(self):
        self.brief("main", "environment-dag", "--for", "dev_dag", "--write", "build it")
        code, out = self.brief("dev", "environment-dag", "--write", "build it my way")
        self.assertEqual(code, 0, out)
        self.assertIn("main wrote this brief for dev_dag; it has been told", out)
        (m,) = self.mail("main")
        self.assertEqual((m["from"], m["priority"]), ("dev", "low"))
        self.assertIn("dev replaced the brief you wrote for dev_dag", m["text"])
        self.assertEqual(self.load("environment-dag")["direct_by"], "main")  # still marked


class CatchUp(unittest.TestCase):
    """Log 139: the harness merges a node's parent in whenever nothing there can
    be disturbed by it, and says so, with the reason, when it cannot."""

    def setUp(self):
        self.env = mock.patch.dict(os.environ, {
            "GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": "t@t",
            "GIT_COMMITTER_NAME": "t", "GIT_COMMITTER_EMAIL": "t@t"})
        self.env.start()
        self.addCleanup(self.env.stop)
        self.ctx = FakeCtx({"main": None, "dev": "main", "dev_1": "dev"})
        self.root = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.root, True)
        self.addCleanup(shutil.rmtree, self.ctx.dir, True)
        repo = self.root / "proj"
        repo.mkdir()
        self.wt = {"main": repo, "dev": self.root / "wt-dev", "dev_1": self.root / "wt-dev_1"}
        self.git("main", "init", "-q", "-b", "main")
        (repo / "a.txt").write_text("a\n")
        self.git("main", "add", "-A"); self.git("main", "commit", "-qm", "base")
        self.git("main", "worktree", "add", "-q", "-b", "dev", str(self.wt["dev"]))
        self.git("dev", "worktree", "add", "-q", "-b", "dev_1", str(self.wt["dev_1"]))
        self.ctx.repo = self.ctx.worktree = repo
        self.ctx.branch = "main"
        for n in self.ctx.tree["nodes"]:
            self.ctx.tree["nodes"][n]["branch"] = n
        self.idx = {"nodes": {
            "main": {"branch": "main", "worktree": str(repo), "parent": None, "rank": 0},
            "dev": {"branch": "dev", "worktree": str(self.wt["dev"]), "parent": "main", "rank": 1},
            "dev_1": {"branch": "dev_1", "worktree": str(self.wt["dev_1"]), "parent": "dev",
                      "rank": 2}}}
        for p in (mock.patch.object(hz, "load_index", return_value=self.idx),
                  mock.patch.object(hz, "live_sessions", return_value=[]),
                  mock.patch.object(hz, "agents_json", return_value=[])):
            p.start()
            self.addCleanup(p.stop)

    def git(self, node, *a):
        r = subprocess.run(["git", *a], cwd=self.wt[node], capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stderr)
        return r.stdout.strip()

    def commit(self, node, name, text="x\n"):
        (self.wt[node] / name).write_text(text)
        self.git(node, "add", "-A"); self.git(node, "commit", "-qm", f"{node}: {name}")
        return self.git(node, "rev-parse", "HEAD")

    def has(self, node, sha):
        return subprocess.run(["git", "merge-base", "--is-ancestor", sha, node],
                              cwd=self.wt["main"]).returncode == 0

    def up(self, node, **kw):
        return hz.catch_up(self.ctx, self.idx, node, "harness", **kw)

    def test_the_count_and_since_when(self):
        self.assertEqual(hz.behind_of(self.ctx, self.idx, "dev")["n"], 0)
        self.assertIsNone(hz.behind_of(self.ctx, self.idx, "main"))        # rank 0 has no parent
        t0 = time.time()
        self.commit("main", "m1"); self.commit("main", "m2")
        b = hz.behind_of(self.ctx, self.idx, "dev")
        self.assertEqual((b["n"], b["parent"]), (2, "main"))
        # When the parent FIRST moved past it, from the reflog: not the last move.
        self.assertTrue(t0 - 2 <= b["since"] <= time.time() + 1)
        self.assertIn("2 commit(s) behind main since ", hz.behind_words(b))

    def test_a_clean_node_nobody_is_working_in_is_merged(self):
        sha = self.commit("main", "m1")
        st, info = self.up("dev")
        self.assertEqual((st, info["n"], info["files"]), ("caught", 1, ["m1"]))
        self.assertTrue(self.has("dev", sha))
        rec = hz._read_json(hz.behind_path(self.ctx, "dev"))
        self.assertEqual((rec["n"], rec["caught"]["n"], rec["caught"]["files"]), (0, 1, ["m1"]))
        self.assertEqual(self.up("dev")[0], "current")

    def test_each_thing_that_blocks_it_and_the_reason_is_recorded(self):
        self.commit("main", "m1")
        tip = self.git("dev", "rev-parse", "HEAD")
        row = lambda st: [{"cwd": str(self.wt["dev"]), "status": st, "sessionId": "s"}]
        with mock.patch.object(hz, "turn_ended", return_value=True):
            self.assertEqual(self.up("dev", rows=row("busy"))[1]["kind"], "busy")
            self.assertIn("running a command", self.up("dev", rows=row("shell"))[1]["why"])
            # Its own session, acting in its own worktree, is not in its own way.
            self.assertEqual(self.up("dev", rows=row("busy"), own=True, dry=True)[0], "would")
        with mock.patch.object(hz, "turn_ended", return_value=False):
            # Idle by the session file, but the transcript says a turn is running.
            st, info = self.up("dev", rows=row("idle"))
            self.assertEqual((st, info["kind"], info["occupied"]), ("blocked", "busy", True))
        # A session in a child's worktree is the child's, never its parent's.
        with mock.patch.object(hz, "turn_ended", return_value=False):
            self.assertEqual(self.up("dev", dry=True, rows=[
                {"cwd": str(self.wt["dev_1"]), "status": "busy", "sessionId": "c"}])[0], "would")
        (self.ctx.dir / "testq").mkdir(exist_ok=True)
        job = self.ctx.dir / "testq" / "j1.json"
        job.write_text(json.dumps({"id": "j1", "kind": "check", "sha": tip, "state": "queued"}))
        self.assertEqual(self.up("dev")[1]["kind"], "check")       # the commit under test stays put
        # Its own work of any kind, at any commit (log 154: a lane's runs were
        # queue copies of one commit, submitted as commands).
        job.write_text(json.dumps({"id": "j1", "kind": "cmd", "sha": "0" * 40, "state": "running",
                                   "requested_by": [{"node": "dev"}]}))
        st, info = self.up("dev")
        self.assertEqual((info["kind"], info["why"]), ("check", "it has work in the test queue"))
        job.write_text(json.dumps({"id": "j1", "kind": "cmd", "sha": "0" * 40, "state": "running",
                                   "requested_by": [{"node": "dev_1"}]}))
        self.assertEqual(self.up("dev", dry=True)[0], "would")     # someone else's is not its
        job.unlink()
        (self.ctx.dir / "halt.json").write_text(json.dumps({"at": hz._now(), "why": "stop"}))
        self.assertEqual(self.up("dev")[1]["kind"], "halt")
        (self.ctx.dir / "halt.json").unlink()
        (self.wt["dev"] / "a.txt").write_text("edited\n")
        st, info = self.up("dev")
        self.assertEqual((st, info["kind"], info["occupied"]), ("blocked", "dirty", False))
        self.assertEqual(self.up("dev", own=True)[1]["kind"], "dirty")     # own or not
        rec = hz._read_json(hz.behind_path(self.ctx, "dev"))
        self.assertEqual((rec["n"], rec["kind"]), (1, "dirty"))
        self.assertEqual(self.git("dev", "rev-parse", "HEAD"), tip)        # nothing moved
        gone = dict(self.idx["nodes"]["dev"], worktree=str(self.root / "nowhere"))
        with mock.patch.dict(self.idx["nodes"], {"dev": gone}):
            self.assertEqual(self.up("dev")[1]["kind"], "nowt")

    def test_a_conflict_is_aborted_and_the_node_left_as_it_was(self):
        self.commit("main", "a.txt", "main's\n")
        tip = self.commit("dev", "a.txt", "dev's\n")
        st, info = self.up("dev")
        self.assertEqual((st, info["kind"], info["conflict"]), ("conflict", "conflict", ["a.txt"]))
        self.assertEqual(self.git("dev", "rev-parse", "HEAD"), tip)
        self.assertEqual(self.git("dev", "status", "--porcelain"), "")
        self.assertIn("conflicts with main in a.txt",
                      hz._read_json(hz.behind_path(self.ctx, "dev"))["why"])
        # The node's own session keeps the conflict in place to collect it (T7).
        self.assertEqual(self.up("dev", own=True, keep_conflict=True)[0], "conflict")
        self.assertIn("UU a.txt", self.git("dev", "status", "--porcelain"))
        self.git("dev", "merge", "--abort")
        # Read from the record for as long as neither branch moves.
        now = hz.behind_now(self.ctx, self.idx, "dev")
        self.assertEqual((now["n"], now["kind"]), (1, "conflict"))

    def test_a_merge_git_refuses_is_recorded_in_its_words_and_tried_again(self):
        self.commit("main", "new.txt", "main's\n")
        (self.wt["dev"] / "new.txt").write_text("an untracked file in the way\n")
        tip = self.git("dev", "rev-parse", "HEAD")
        st, info = self.up("dev")
        self.assertEqual((st, info["kind"]), ("blocked", "refused"))
        self.assertIn("git refused the merge:", info["why"])
        self.assertIn("new.txt", info["why"])
        self.assertEqual(self.git("dev", "rev-parse", "HEAD"), tip)
        # Most refusals pass (dev: "fatal: stash failed", three times), so it is
        # tried again each pass, then every ten minutes; only a conflict waits
        # for a branch to move.
        skip = {}
        with mock.patch.object(hz, "catch_up", wraps=hz.catch_up) as cu:
            for _ in range(hz.REFUSED_TRIES + 3):
                res = hz.catchup_pass(self.ctx, idx=self.idx, rows=[], skip=skip, only={"dev"})
            self.assertEqual(cu.call_count, hz.REFUSED_TRIES)
            self.assertEqual((res[0][1], res[0][2]["kind"]), ("blocked", "refused"))
            skip["dev"]["at"] -= hz.REFUSED_EVERY + 1
            hz.catchup_pass(self.ctx, idx=self.idx, rows=[], skip=skip, only={"dev"})
            self.assertEqual(cu.call_count, hz.REFUSED_TRIES + 1)
            (self.wt["dev"] / "new.txt").unlink()            # the reason passes: it merges
            skip["dev"]["at"] -= hz.REFUSED_EVERY + 1
            res = hz.catchup_pass(self.ctx, idx=self.idx, rows=[], skip=skip, only={"dev"})
        self.assertEqual(res[0][1], "caught")
        self.assertNotIn("dev", skip)

    def test_a_presented_node_keeps_its_record_and_review(self):
        tip = self.commit("dev_1", "work")
        (self.ctx.dir / "marks").mkdir()
        (self.ctx.dir / "marks" / "t.json").write_text(json.dumps(
            {"_node": "dev_1", "_presented_at": hz._now(), "_presented_sha": tip}))
        hz.write_review(self.ctx, "dev_1", "dev_1", tip, "dev")
        self.commit("dev", "sibling")                      # the lead integrated someone else
        st, info = self.up("dev_1")
        self.assertEqual((st, info["carried"]), ("caught", tip))
        new = self.git("dev_1", "rev-parse", "HEAD")
        m = hz.open_marks(self.ctx)["t"]
        self.assertEqual((m["_presented_sha"], m["_caught_up_by"]), (new, "harness"))
        rv = hz.read_review(self.ctx, "dev_1", new)
        self.assertEqual((rv["reviewed_by_node"], rv["carried_from"]), ("dev", tip))
        # So the lead's fast-forward goes through.
        self.git("dev", "merge", "-q", "--ff-only", "dev_1")

    def test_one_pass_carries_a_change_down_every_rank(self):
        sha = self.commit("main", "m1")
        res = hz.catchup_pass(self.ctx, idx=self.idx, rows=[])
        self.assertEqual([(n, st) for n, st, _, _ in res], [("dev", "caught"), ("dev_1", "caught")])
        self.assertTrue(self.has("dev_1", sha))
        self.assertEqual([st for _, st, _, _ in hz.catchup_pass(self.ctx, idx=self.idx, rows=[])],
                         ["current", "current"])

    def test_the_ringer_passes_only_when_something_moved_and_tries_a_conflict_once(self):
        S = {}
        with mock.patch("sys.stdout", io.StringIO()) as out, \
             mock.patch.object(hz, "catchup_pass", wraps=hz.catchup_pass) as p:
            hz.ringer_catchup(self.ctx, S)
            hz.ringer_catchup(self.ctx, S)
            self.assertEqual(p.call_count, 1)              # nothing moved: one git call, no pass
            self.commit("main", "a.txt", "main's\n")
            self.commit("dev", "a.txt", "dev's\n")
            with mock.patch.object(hz, "catch_up", wraps=hz.catch_up) as cu:
                hz.ringer_catchup(self.ctx, S)
                hz.ringer_catchup(self.ctx, S)
                tried = [c.args[2] for c in cu.call_args_list]
        self.assertEqual(tried.count("dev"), 1)            # the same pair of tips: not again
        self.assertEqual(S["_behind"], ["dev"])
        self.assertEqual(out.getvalue().count("dev is 1 commit(s) behind main"), 1)
        self.assertIn("dev_1 caught up: 1 commit(s) from dev", out.getvalue())

    def test_a_background_shell_blocks_only_when_it_is_doing_something(self):
        d = self.root / "shell-snapshots"
        d.mkdir()
        (d / "s.sh").write_text("")
        def shell(cmd):
            p = subprocess.Popen(["bash", "-c", f"source '{d}/s.sh'; {cmd}; true"])
            self.addCleanup(p.wait)
            self.addCleanup(p.kill)
            return p
        me = {"pid": os.getpid(), "cwd": str(self.wt["dev"]), "status": "shell", "sessionId": "s"}
        self.assertEqual(hz.session_work(me), "a command")          # no tool shell: cannot tell
        self.assertEqual(hz.session_work({"pid": None}), "a command")
        w = shell("sleep 30")
        time.sleep(0.3)
        self.assertIsNone(hz.session_work(me))                      # a loop that only waits
        self.commit("main", "m1")
        with mock.patch.object(hz, "turn_ended", return_value=True):
            self.assertEqual(self.up("dev", rows=[me], dry=True)[0], "would")
            job = shell(f"'{sys.executable}' -c 'import time; time.sleep(30)'")
            time.sleep(0.3)
            st, info = self.up("dev", rows=[me], dry=True)
        self.assertEqual(st, "blocked")
        self.assertRegex(info["why"], r"its session is running python")
        w.kill(); job.kill()
        for p in hz.proc_tree(os.getpid())[1:]:                     # the sleeps under them
            try:
                os.kill(p, 9)
            except OSError:
                pass

    def test_since_when_is_the_first_move_it_lacks_however_many_followed(self):
        def at(t, name):
            with mock.patch.dict(os.environ, {"GIT_COMMITTER_DATE": f"{t} +0000"}):
                return self.commit("main", name)
        for i in range(3):
            at(1700000000 + i, f"old{i}")
        self.assertEqual(self.up("dev")[0], "caught")          # holds the first three moves
        for i in range(9):
            at(1700001000 + 100 * i, f"new{i}")
        b = hz.behind_of(self.ctx, self.idx, "dev")
        self.assertEqual((b["n"], b["since"]), (9, 1700001000))

    def test_a_quiet_pass_asks_git_once_and_a_pending_one_does_not_recount(self):
        S = {}
        calls = []
        real = hz.git
        def spy(*a, **kw):
            calls.append(a[0] if a[0] != "--no-optional-locks" else a[1])
            return real(*a, **kw)
        with mock.patch("sys.stdout", io.StringIO()), mock.patch.object(hz, "git", side_effect=spy):
            hz.ringer_catchup(self.ctx, S)
            calls.clear()
            hz.ringer_catchup(self.ctx, S)                      # nothing moved
            self.assertEqual(calls, ["for-each-ref"])
            self.commit("main", "m1")
            (self.wt["dev"] / "a.txt").write_text("edited\n")   # dev cannot be merged into
            hz.ringer_catchup(self.ctx, S)
            self.assertEqual(S["_behind"], ["dev"])
            calls.clear()
            hz.ringer_catchup(self.ctx, S)                      # still behind, nothing moved
            self.assertNotIn("rev-list", calls)                 # counted once, not again
            self.assertNotIn("reflog", calls)
            self.assertIn("status", calls)                      # but looked at again
        self.assertEqual(hz._read_json(hz.behind_path(self.ctx, "_pass"))["pid"], os.getpid())

    def test_a_node_the_ringer_just_woke_is_left_alone_this_pass(self):
        sha = self.commit("main", "m1")
        S = {"dev": {"at": time.time(), "tries": 1}}
        with mock.patch("sys.stdout", io.StringIO()):
            hz.ringer_catchup(self.ctx, S)
            self.assertFalse(self.has("dev", sha))
            self.assertEqual(S["_behind"], ["dev"])             # so the next pass comes back
            S["dev"]["at"] = time.time() - hz.WAKE_GRACE - 1
            hz.ringer_catchup(self.ctx, S)
        self.assertTrue(self.has("dev", sha))

    def test_status_reads_the_ringer_s_records_while_it_is_running(self):
        self.commit("main", "m1")
        (self.wt["dev"] / "a.txt").write_text("edited\n")
        with mock.patch("sys.stdout", io.StringIO()):
            hz.ringer_catchup(self.ctx, {})
        with mock.patch.object(hz, "ringer_alive", return_value={"pid": os.getpid()}), \
             mock.patch.object(hz, "git", side_effect=AssertionError("no git")):
            b = hz.behind_seen(self.ctx, self.idx, "dev")
            self.assertEqual((b["n"], b["kind"]), (1, "dirty"))
            self.assertEqual(hz.behind_seen(self.ctx, self.idx, "dev_1")["n"], 0)
        with mock.patch.object(hz, "ringer_alive", return_value=None):     # no ringer: measured
            self.assertEqual(hz.behind_seen(self.ctx, self.idx, "dev")["n"], 1)

    def test_integrate_repairs_a_presentation_a_merge_left_behind(self):
        tip = self.commit("dev_1", "work")
        (self.ctx.dir / "marks").mkdir()
        (self.ctx.dir / "marks" / "t.json").write_text(json.dumps(
            {"_node": "dev_1", "_task": "t", "_presented_at": hz._now(), "_presented_sha": tip}))
        hz.write_review(self.ctx, "dev_1", "dev_1", tip, "dev")
        self.commit("dev", "sibling")
        self.git("dev_1", "merge", "-q", "--no-edit", "dev")   # merged, and no record followed
        code, out = self.run_as("dev", "integrate", "dev_1", read_roster=lambda p: None)
        self.assertEqual(code, 0, out)
        self.assertEqual(self.git("dev", "rev-parse", "HEAD"), self.git("dev_1", "rev-parse", "HEAD"))
        # A commit of its own after presenting is still refused.
        self.commit("dev_1", "more")
        code, out = self.run_as("dev", "integrate", "dev_1", read_roster=lambda p: None)
        self.assertEqual(code, hz.REFUSED)
        self.assertIn("has committed since it presented", out)

    def test_a_check_is_found_through_a_catch_up_merge(self):
        tip = self.commit("dev_1", "work")
        f = hz.check_report_path(self.ctx, "dev_1", tip)
        f.parent.mkdir(parents=True, exist_ok=True)
        f.write_text(json.dumps({"sha": tip, "passed": True}))
        self.commit("dev", "sibling")
        self.assertEqual(self.up("dev_1")[0], "caught")
        head = self.git("dev_1", "rev-parse", "HEAD")
        self.ctx.worktree = self.wt["dev_1"]
        rep, at, hops = hz.check_through_catchup(self.ctx, "dev_1", head)
        self.assertEqual((rep["passed"], at, hops), (True, tip, 1))
        # A commit of its own on top is not a catch-up: that one is unchecked.
        mine = self.commit("dev_1", "more")
        self.assertEqual(hz.check_through_catchup(self.ctx, "dev_1", mine), (None, mine, 0))

    def test_the_session_s_own_commands_catch_up_first_and_say_so(self):
        sha = self.commit("main", "m1")
        out = io.StringIO()
        with redirect_stdout(out):
            st, _ = hz.own_catchup(self.ctx, "dev")
        self.assertEqual(st, "caught")
        self.assertTrue(self.has("dev", sha))
        self.assertIn("dev caught up: 1 commit(s) from main merged (1 file(s): m1)", out.getvalue())
        self.commit("main", "m2")
        (self.wt["dev"] / "a.txt").write_text("edited\n")
        out = io.StringIO()
        with redirect_stdout(out):
            st, info = hz.own_catchup(self.ctx, "dev")
        self.assertEqual((st, info["n"]), ("blocked", 1))
        self.assertIn("BEHIND   1 commit(s) behind main", out.getvalue())
        self.assertIn("uncommitted change(s)", out.getvalue())

    def items(self, node):
        with mock.patch.object(hz, "lead_owes", return_value=[]), \
             mock.patch.object(hz, "rank0_owes", return_value=[]), \
             mock.patch.object(hz, "open_waits", return_value={}), \
             mock.patch.object(hz, "focus_family", return_value=None), \
             mock.patch.object(hz, "unread_brief_comments", return_value={}), \
             mock.patch.object(hz, "unactioned_briefs", return_value=[]), \
             mock.patch.object(hz, "open_marks", return_value={}), \
             mock.patch.object(hz, "queue", return_value=[]):
            return hz.queue_items(self.ctx, node)

    def test_the_node_is_told_at_its_next_prompt_once(self):
        self.commit("main", "m1")
        self.up("dev")                                     # merged while it was between turns
        got = self.items("dev")
        key = next(k for k in got if k.startswith("caught:"))
        self.assertIn("caught up: 1 commit(s) from main were merged into your worktree", got[key])
        self.assertIn("(1 file(s): m1) — re-read any you had open", got[key])
        rows, ids = hz.delta(self.ctx, "dev", "sid-dev")
        self.assertIn(key, ids)
        self.assertEqual(hz.delta(self.ctx, "dev", "sid-dev"), ([], []))       # once
        # Its own command already printed it: not said again at the prompt.
        self.commit("main", "m2")
        with redirect_stdout(io.StringIO()):
            hz.own_catchup(self.ctx, "dev")
        self.assertFalse(any(k.startswith("caught:") for k in self.items("dev")))
        # Behind for a reason it can act on: said, with what to do.
        self.commit("main", "m3")
        (self.wt["dev"] / "a.txt").write_text("edited\n")
        self.up("dev")
        line = next(v for k, v in self.items("dev").items() if k.startswith("behind:"))
        self.assertIn("1 commit(s) behind main", line)
        self.assertIn("Commit what is there", line)
        # Mid-turn is not something to tell it: it merges when the turn ends.
        (self.wt["dev"] / "a.txt").write_text("a\n")
        with mock.patch.object(hz, "turn_ended", return_value=False):
            self.up("dev", rows=[{"cwd": str(self.wt["dev"]), "status": "busy", "sessionId": "s"}])
        self.assertFalse(any(k.startswith("behind:") for k in self.items("dev")))

    def test_the_lead_owes_only_what_only_it_can_clear(self):
        def rec(**kw):
            hz._save(hz.behind_path(self.ctx, "dev_1"),
                     dict({"n": 4, "parent": "dev", "since": time.time() - 3600}, **kw))
            with mock.patch.object(hz, "open_marks", return_value={}), \
                 mock.patch.object(hz, "startable", return_value=[]), \
                 mock.patch.object(hz, "unanswered", return_value=None), \
                 mock.patch.object(hz, "node_running", return_value=(None, None)), \
                 mock.patch.object(hz, "context_limits", return_value=(None, None)):
                return [o for o in hz.lead_owes(self.ctx, "dev") if o[0] == "stale"]
        owed = rec(kind="conflict", why="it conflicts with dev in a.txt", occupied=True)
        self.assertEqual([(o[1], o[2]) for o in owed],
                         [("dev_1", "4 commit(s) behind you: it conflicts with dev in a.txt")])
        self.assertIn("yours to mediate", hz.owed_line(*owed[0]))
        owed = rec(kind="dirty", why="2 uncommitted change(s) there", occupied=False)
        self.assertIn("harness catchup dev_1", hz.owed_line(*owed[0]))
        self.assertEqual(rec(kind="dirty", why="x", occupied=True), [])    # its session commits
        self.assertEqual(rec(kind="busy", why="its session is mid-turn"), [])
        self.assertEqual(rec(kind="conflict", why="x", since=time.time() - 60), [])   # not yet
        (self.ctx.dir / "halt.json").write_text(json.dumps({"at": hz._now(), "why": "stop"}))
        self.assertEqual(rec(kind="conflict", why="x"), [])                # nothing new in a halt

    def test_a_report_on_a_behind_tree_opens_by_saying_so(self):
        b = {"n": 42, "parent": "dev_tests", "since": time.time() - 60,
             "why": "it conflicts with dev_tests in schema.sql"}
        rep = hz.make_check_report("dev_1", "a" * 40, [], 0, None, behind=b)
        out = io.StringIO()
        with redirect_stdout(out):
            hz.print_check_report(rep, None)
        first = out.getvalue().splitlines()[0]
        self.assertTrue(first.startswith("STALE TREE: this commit is 42 commit(s) behind dev_tests"))
        self.assertIn("may be the difference, not your change", first)
        out = io.StringIO()
        with redirect_stdout(out):
            hz.print_check_report(hz.make_check_report("dev_1", "a" * 40, [], 0, None), None)
        self.assertNotIn("STALE", out.getvalue())

    def run_as(self, node, *argv, sid="s" * 36, **patches):
        """One `harness ...` command as `node`'s session (sid None: a shell)."""
        self.ctx.me, self.ctx.branch, self.ctx.worktree = node, node, self.wt[node]
        self.idx.update(project="proj", byBranch={n: n for n in self.idx["nodes"]},
                        byWorktree={sp["worktree"]: n for n, sp in self.idx["nodes"].items()})
        patches.setdefault("print_delta", lambda *a, **k: None)
        out, code = io.StringIO(), 0
        env = dict(os.environ, CLAUDE_CODE_SESSION_ID=sid or "")
        if not sid:
            env.pop("CLAUDE_CODE_SESSION_ID")
        with mock.patch.object(hz, "Ctx", return_value=self.ctx), \
             mock.patch.dict(os.environ, env, clear=True), \
             mock.patch.multiple(hz, **patches), \
             mock.patch("sys.argv", ["harness", *argv]), \
             redirect_stdout(out), mock.patch("sys.stderr", out):
            try:
                hz.main()
            except SystemExit as e:
                code = e.code or 0
        return code, out.getvalue()

    def test_behind_says_how_far_since_when_and_why(self):
        self.commit("main", "m1")
        (self.wt["dev"] / "a.txt").write_text("edited\n")
        code, out = self.run_as("dev", "behind")
        self.assertTrue(out.startswith("1  commits behind main (main) since "), out)
        self.assertIn("1 uncommitted change(s) there", out)
        code, out = self.run_as("main", "behind", "--all")
        self.assertIn("dev            1 commit(s) behind main", out)
        self.assertIn("dev_1          current with dev", out)
        self.assertIn("1 of 2 node(s) behind their parent", out)

    def test_catchup_by_hand_for_itself_and_for_the_nodes_below(self):
        sha = self.commit("main", "m1")
        code, out = self.run_as("dev", "catchup", "--dry-run")
        self.assertIn("dev would catch up 1 commit(s) from main", out)
        self.assertFalse(self.has("dev", sha))
        code, out = self.run_as("dev", "catchup")
        self.assertEqual(code, 0, out)
        self.assertTrue(self.has("dev", sha))
        self.assertIn("dev is current with main", self.run_as("dev", "catchup")[1])
        sha2 = self.commit("main", "m2")
        code, out = self.run_as("main", "catchup", "--all")
        self.assertTrue(self.has("dev_1", sha2), out)
        # Not a node below the caller: refused, by name.
        code, out = self.run_as("dev_1", "catchup", "dev")
        self.assertEqual(code, hz.REFUSED)
        self.assertIn("not below dev_1", out)
        # Its own conflict stays in place to be collected, and is not resolved.
        self.commit("main", "a.txt", "main's\n")
        self.commit("dev", "a.txt", "dev's\n")
        code, out = self.run_as("dev", "catchup")
        self.assertEqual(code, hz.REFUSED)
        self.assertIn("dev CONFLICTS with main in: a.txt", out)
        self.assertIn("UU a.txt", self.git("dev", "status", "--porcelain"))

    def check(self, node):
        sent = {}
        def submit(ctx, kind, sha, n, sid, **kw):
            sent.update(kw, sha=sha)
            return {"id": "j1", "queue": "priority"}, "queued"
        code, out = self.run_as(
            node, "check", "--memory", "x=100M",
            load_checks=lambda ctx: [{"name": "x", "command": "true", "blindSpot": "b"}],
            role_of=lambda ctx, n: "lead", testq_submit=submit,
            testq_wait_phrase=lambda ctx, job: "")
        return code, out, sent

    def test_a_check_merges_the_parent_in_first(self):
        sha = self.commit("main", "m1")
        code, out, sent = self.check("dev")
        self.assertEqual(code, 0, out)
        self.assertIn("dev caught up: 1 commit(s) from main", out)
        self.assertTrue(self.has("dev", sha))
        self.assertEqual(sent["sha"], self.git("dev", "rev-parse", "HEAD"))   # the merged commit
        self.assertIsNone(sent["behind"])

    def test_a_check_that_cannot_catch_up_still_runs_and_is_stamped(self):
        self.commit("main", "a.txt", "main's\n")
        tip = self.commit("dev", "a.txt", "dev's\n")
        code, out, sent = self.check("dev")
        self.assertEqual(code, 0, out)
        self.assertIn("BEHIND   1 commit(s) behind main", out)
        self.assertEqual((sent["sha"], sent["behind"]["n"], sent["behind"]["parent"]),
                         (tip, 1, "main"))
        self.assertIn("conflicts with main in a.txt", sent["behind"]["why"])
        self.assertEqual(self.git("dev", "status", "--porcelain"), "")     # aborted, not left

    def test_a_session_starts_on_its_lead_s_current_tree(self):
        sha = self.commit("main", "m1")
        started = []
        code, out = self.run_as(
            "main", "spawn", "dev", sid=None,
            read_roster=lambda p: None, startable=lambda ctx, n: [{"task": "t"}],
            grants_for=lambda ctx, n: [], launch_cmd=lambda *a: ["true"],
            assignment_for=lambda ctx, n: ("m", "e"),
            launch_bg=lambda cmd, cwd, env=None: (
                started.append((cwd, self.has("dev", sha))), (True, ""))[1])
        self.assertIn("dev caught up: 1 commit(s) from main", out)
        self.assertEqual(started, [(str(self.wt["dev"]), True)])           # merged BEFORE it starts

    def test_the_stop_hook_counts_a_catch_up_as_no_work_and_a_split_task_as_nothing_to_present(self):
        # Log 169: dev_dag was told at every turn end to present a segment it
        # had split, and the only moves of its HEAD were the harness's catch-ups.
        for d in ("marks", "briefs"):
            (self.ctx.dir / d).mkdir(exist_ok=True)
        self.ctx.me, self.ctx.branch, self.ctx.worktree = "dev_1", "dev_1", self.wt["dev_1"]
        (self.ctx.dir / "marks" / "t.json").write_text(json.dumps(
            {"_node": "dev_1", "_task": "t", "_sha": self.git("dev_1", "rev-parse", "HEAD")}))
        self.assertEqual(hz.unreported(self.ctx, "dev_1"), [])
        self.commit("dev", "from_the_lead.txt")
        self.git("dev_1", "merge", "-q", "--no-edit", "dev")          # a catch-up
        self.assertEqual(hz.unreported(self.ctx, "dev_1"), [])
        self.commit("dev_1", "own_work.txt")                        # work of its own
        self.assertEqual([(m, d) for _, m, d in hz.unreported(self.ctx, "dev_1")], [(True, False)])
        (self.ctx.dir / "briefs" / "t_a.json").write_text(json.dumps(
            {"task": "t-a", "node": "dev_1", "from": "t"}))           # now split into parts
        self.assertEqual(hz.unreported(self.ctx, "dev_1"), [])

    def test_a_re_mark_keeps_the_task_s_comments(self):
        # Log 159: the command a restarted session is offered rebuilt the record
        # from nothing: 34 comments became 8, and 10 became 0.
        (self.ctx.dir / "briefs").mkdir()
        (self.ctx.dir / "marks").mkdir()
        (self.ctx.dir / "briefs" / "t.json").write_text(json.dumps({"task": "t", "node": "dev_1"}))
        mf = self.ctx.dir / "marks" / "t.json"
        mf.write_text(json.dumps({
            "_node": "dev_1", "_session": "dead-session", "_at": "2026-10-12T09:00:00+1100",
            "_band": "S", "_band_source": "member", "_band_brief": "M", "_delegated": ["t.up-dev"],
            "_comments": [{"at": "x", "by": "dev", "text": "the handover"},
                          {"at": "y", "by": "main", "text": "a ruling"}]}))
        opened = dict(unreported=lambda *a: [], claim_conflict=lambda ctx, n: (None, "unclaimed"),
                      read_spend_or_none=lambda sid: (None, "no transcript"),
                      assignment_for=lambda ctx, n: ("m", "e"))
        code, out = self.run_as("dev_1", "mark", "t", **opened)
        self.assertNotEqual(code, 0)
        self.assertIn("the task's comments are kept", out)
        code, out = self.run_as("dev_1", "mark", "t", "--force", **opened)
        self.assertEqual(code, 0, out)
        self.assertIn("kept 2 comment(s) from the earlier mark", out)
        rec = json.loads(mf.read_text())
        self.assertEqual([c["text"] for c in rec["_comments"]], ["the handover", "a ruling"])
        self.assertEqual(rec["_delegated"], ["t.up-dev"])
        self.assertEqual((rec["_band"], rec["_band_source"], rec["_band_brief"]), ("S", "member", "M"))
        self.assertEqual(rec["_remarked_from"]["session"], "dead-session")
        self.assertEqual(rec["_session"], "s" * 36)

    def test_a_task_starts_on_the_lead_s_current_tree(self):
        (self.ctx.dir / "briefs").mkdir()
        (self.ctx.dir / "marks").mkdir()
        for t in ("t", "u"):
            (self.ctx.dir / "briefs" / f"{t}.json").write_text(
                json.dumps({"task": t, "node": "dev_1"}))
        opened = dict(unreported=lambda *a: [], claim_conflict=lambda ctx, n: (None, "unclaimed"),
                      read_spend_or_none=lambda sid: (None, "no transcript"),
                      assignment_for=lambda ctx, n: ("m", "e"))
        sha = self.commit("dev", "d1")
        code, out = self.run_as("dev_1", "mark", "t", **opened)
        self.assertEqual(code, 0, out)
        self.assertIn("dev_1 caught up: 1 commit(s) from dev", out)
        rec = json.loads((self.ctx.dir / "marks" / "t.json").read_text())
        self.assertTrue(self.has("dev_1", sha))
        self.assertEqual(rec["_sha"], self.git("dev_1", "rev-parse", "HEAD"))
        self.assertNotIn("_behind_at_open", rec)
        # It cannot be caught up: the task opens all the same, and keeps the count.
        self.commit("dev", "d2")
        (self.wt["dev_1"] / "a.txt").write_text("edited\n")
        code, out = self.run_as("dev_1", "mark", "u", **opened)
        self.assertEqual(code, 0, out)
        self.assertIn("BEHIND   1 commit(s) behind dev", out)
        rec = json.loads((self.ctx.dir / "marks" / "u.json").read_text())
        self.assertEqual((rec["_behind_at_open"]["n"], rec["_behind_at_open"]["parent"]), (1, "dev"))

    def test_integrate_catches_a_released_child_up_through_the_same_door(self):
        tip = self.commit("dev_1", "work")
        (self.ctx.dir / "marks").mkdir()
        (self.ctx.dir / "marks" / "t.json").write_text(json.dumps(
            {"_node": "dev_1", "_task": "t", "_presented_at": hz._now(), "_presented_sha": tip}))
        hz.write_review(self.ctx, "dev_1", "dev_1", tip, "dev")
        self.commit("dev", "sibling")
        code, out = self.run_as("dev", "integrate", "dev_1", read_roster=lambda p: None)
        self.assertEqual(code, 0, out)
        self.assertIn("caught up (1 behind)", out)
        self.assertIn("review carried from " + tip[:8], out)
        self.assertEqual(self.git("dev", "rev-parse", "HEAD"), self.git("dev_1", "rev-parse", "HEAD"))
        self.assertEqual(hz.open_marks(self.ctx)["t"]["_caught_up_by"], "dev")

    # Log 171: dev_tests' integrate ended dev_tests_1's session, which cancelled
    # its queued check, and then refused for want of a record, because the task
    # had been signed off a minute before it was integrated.
    def job(self, jid, kind, sha, node="dev_1"):
        j = {"id": jid, "kind": kind, "sha": sha, "state": "queued", "command": "x",
             "requested_by": [{"node": node}], "at": hz._now()}
        (hz.testq_dir(self.ctx) / f"{jid}.json").write_text(json.dumps(j))
        return lambda: hz._read_json(hz.testq_dir(self.ctx) / f"{jid}.json")

    def presented(self, tip, **more):
        (self.ctx.dir / "marks").mkdir(exist_ok=True)
        (self.ctx.dir / "marks" / "t.json").write_text(json.dumps(dict(
            {"_node": "dev_1", "_task": "t", "_presented_at": hz._now(), "_presented_sha": tip},
            **more)))

    def test_integrate_refuses_before_it_ends_a_lane_and_says_it_was_signed_off_early(self):
        tip = self.commit("dev_1", "work")
        self.presented(tip, _closed_at="2026-10-14T22:38:33+1100", _closed_by="dev (session a)")
        hz.write_review(self.ctx, "dev_1", "dev_1", tip, "dev")
        check = self.job("j1", "check", tip)
        row = [{"cwd": str(self.wt["dev_1"]), "sessionId": "c" * 36, "status": "idle"}]
        stopped = []
        code, out = self.run_as("dev", "integrate", "dev_1", read_roster=lambda p: None,
                                agents_json=lambda *a: row, live_rows=lambda r: r,
                                finished_released=lambda *a: True,
                                stop_session_row=lambda c, n, r: stopped.append(n) or (True, []))
        self.assertEqual(code, hz.REFUSED)
        self.assertIn("was signed off at 2026-10-14T22:38:33+1100 by dev (session a)", out)
        self.assertIn("git merge --ff-only dev_1", out)
        self.assertEqual(stopped, [])                       # nobody was ended for a refusal
        self.assertEqual(check()["state"], "queued")
        # Unreviewed is refused before the stop too.
        self.presented(tip)
        self.ctx.state_file("reviews", f"dev_1-{tip}", ".json").unlink()
        code, out = self.run_as("dev", "integrate", "dev_1", read_roster=lambda p: None,
                                agents_json=lambda *a: row, live_rows=lambda r: r,
                                finished_released=lambda *a: True,
                                stop_session_row=lambda c, n, r: stopped.append(n) or (True, []))
        self.assertIn("no review is recorded at this commit", out)
        self.assertEqual(stopped, [])

    def test_stopping_a_lane_keeps_its_check_and_records_why_it_cancels_the_rest(self):
        tip = self.commit("dev_1", "work")
        check, probe = self.job("j1", "check", tip), self.job("j2", "command", tip)
        other = self.job("j3", "command", tip, node="dev")
        ok = subprocess.CompletedProcess([], 0, "", "")
        with mock.patch.object(hz.subprocess, "run", return_value=ok), \
             mock.patch.object(hz.time, "sleep"):
            done, lines = hz.stop_session_row(self.ctx, "dev_1", {"sessionId": "c" * 36, "pid": None})
        self.assertTrue(done)
        self.assertEqual(check()["state"], "queued")
        self.assertIn(f"its queued check j1 stays: it checks {tip[:8]}, not the session",
                      "\n".join(lines))
        self.assertEqual((probe()["state"], probe()["why"]), ("cancelled", "dev_1's session was stopped"))
        self.assertEqual(other()["state"], "queued")

    def test_a_presented_commit_s_check_rings_the_lead_as_well(self):
        tip = self.commit("dev_1", "work")
        p = mock.patch.object(hz, "ensure_ringer", lambda s: None)
        p.start(); self.addCleanup(p.stop)
        (self.ctx.dir / "index.json").write_text(json.dumps(self.idx))
        self.presented(tip)
        inbox = lambda n: list((self.ctx.dir / "doorbell" / n / "inbox").glob("*.json"))
        job = {"id": "j1", "kind": "check", "sha": tip, "state": "done",
               "requested_by": [{"node": "dev_1"}]}
        rep = {"checks": [{}, {}], "failed": 0, "held": 0}
        hz.testq_ring(self.ctx, job, rep, 0)
        self.assertEqual((len(inbox("dev_1")), len(inbox("dev"))), (1, 1))
        self.assertIn("yours to read", hz._read_json(inbox("dev")[0])["text"])
        # A commit nobody presented rings only who asked.
        other = self.commit("dev_1", "more")
        hz.testq_ring(self.ctx, dict(job, sha=other), rep, 0)
        self.assertEqual((len(inbox("dev_1")), len(inbox("dev"))), (2, 1))

    def test_a_lead_signs_off_only_what_it_has_integrated_and_integrate_says_what_was_checked(self):
        tip = self.commit("dev_1", "work")
        self.presented(tip)
        hz.write_review(self.ctx, "dev_1", "dev_1", tip, "dev")
        code, out = self.run_as("dev", "mark", "t", "--close")
        self.assertEqual(code, hz.REFUSED)
        self.assertIn("1 commit(s) of it are not in dev yet", out)
        self.assertIn("harness integrate dev_1", out)
        self.job("j1", "check", tip)
        code, out = self.run_as("dev", "integrate", "dev_1", read_roster=lambda p: None)
        self.assertEqual(code, 0, out)
        self.assertIn(f"NOT CHECKED yet at {tip[:8]}: check j1 is queued", out)
        code, out = self.run_as("dev", "mark", "t", "--close")
        self.assertEqual(code, 0, out)
        self.assertIn("signed off t", out)
        # A reported check is named on the integrate line.
        tip2 = self.commit("dev_1", "more")
        self.presented(tip2)
        hz.write_review(self.ctx, "dev_1", "dev_1", tip2, "dev")
        f = hz.check_report_path(self.ctx, "dev_1", tip2)
        f.parent.mkdir(parents=True, exist_ok=True)
        f.write_text(json.dumps({"sha": tip2, "passed": True, "checks": [{}], "failed": 0}))
        code, out = self.run_as("dev", "integrate", "dev_1", read_roster=lambda p: None)
        self.assertIn(f"check at {tip2[:8]}: passed", out)
        # A document root signs off code it never merges: not held to it.
        self.ctx.tree["nodes"]["main"]["kind"] = "doc"
        mine = self.commit("dev", "lead's own")
        (self.ctx.dir / "marks" / "d.json").write_text(json.dumps(
            {"_node": "dev", "_task": "d", "_presented_at": hz._now(), "_presented_sha": mine}))
        code, out = self.run_as("main", "mark", "d", "--close")
        self.assertEqual(code, 0, out)

    def test_rank_0_is_not_shown_what_a_lead_below_owes_unless_it_asks(self):
        # Log 173: main's every prompt listed dev's unsigned presentations.
        tip = self.commit("dev_1", "work")
        (self.ctx.dir / "marks").mkdir(exist_ok=True)
        (self.ctx.dir / "marks" / "t.json").write_text(json.dumps(
            {"_node": "dev_1", "_task": "t", "_presented_at": OLD, "_presented_sha": tip}))
        code, out = self.run_as("main", "whoami", "--no-check", read_roster=lambda p: None)
        self.assertEqual(code, 0, out)
        self.assertNotIn("unsigned", out)
        code, out = self.run_as("main", "whoami", "--no-check", "--tree",
                                read_roster=lambda p: None)
        self.assertIn("unsigned t (dev_1, 3h", out)

    def test_a_lead_parks_a_presentation_it_cannot_sign_off_yet_for_a_time(self):
        # Owner, 2026-10-15: dev waited on the owner and was nagged for it.
        tip = self.commit("dev_1", "work")
        (self.ctx.dir / "marks").mkdir(exist_ok=True)
        (self.ctx.dir / "briefs").mkdir(exist_ok=True)
        (self.ctx.dir / "marks" / "t.json").write_text(json.dumps(
            {"_node": "dev_1", "_task": "t", "_presented_at": OLD, "_presented_sha": tip}))
        (self.ctx.dir / "briefs" / "t.json").write_text(json.dumps(
            {"task": "t", "node": "dev_1", "text": "x", "written_by": "dev (session s)"}))
        code, out = self.run_as("dev", "brief", "t", "--wait-for", "3h")
        self.assertEqual(code, hz.REFUSED)
        self.assertIn("--wait-for goes with --wait", out)
        code, out = self.run_as("dev", "brief", "t", "--wait", "x", "--wait-for", "9d")
        self.assertEqual(code, hz.REFUSED)
        code, out = self.run_as("dev", "brief", "t", "--wait", "the owner runs the migration",
                                "--wait-for", "3h")
        self.assertEqual(code, 0, out)
        self.assertIn("Nothing asks for its sign-off", out)
        self.assertIn("(3h", out)
        self.assertEqual([o for o in hz.lead_owes(self.ctx, "dev") if o[0] == "sign off"], [])
        code, out = self.run_as("dev", "whoami", "--no-check", read_roster=lambda p: None)
        self.assertIn("parked   t's sign-off, until", out)
        self.assertNotIn("sign off 1 presented", out)

    def test_a_hold_keeps_a_node_s_tree_still_until_it_presents(self):
        # Log 154 (owner, 2026-10-12): merging between turns stays the rule, and
        # a lane that needs one tree for a whole diagnosis says so.
        sha = self.commit("dev", "d1")
        code, out = self.run_as("dev_1", "catchup", "--hold", "one tree for the whole diagnosis")
        self.assertEqual(code, 0, out)
        self.assertIn("held: nothing merges into dev_1 until it presents", out)
        st, info = self.up("dev_1")                                  # the ringer
        self.assertEqual((st, info["kind"]), ("blocked", "held"))
        self.assertEqual(info["why"], "held by dev_1: one tree for the whole diagnosis")
        with redirect_stdout(io.StringIO()) as o:                    # its own check or task start
            self.assertEqual(hz.own_catchup(self.ctx, "dev_1")[0], "blocked")
        self.assertIn("held by dev_1", o.getvalue())
        code, out = self.run_as("dev_1", "catchup")
        self.assertEqual(code, hz.REFUSED)
        self.assertIn("harness catchup --release, then harness catchup", out)
        self.assertIn("held by dev_1: one tree", self.run_as("dev_1", "behind")[1])
        self.assertFalse(self.has("dev_1", sha))
        # Its lead's integrate, after it has presented, is not held back.
        self.assertEqual(self.up("dev_1", own=True, ignore_hold=True, dry=True)[0], "would")
        # A node above may release it or place one; a node that is not above may not.
        code, out = self.run_as("dev", "catchup", "--release", "dev_1")
        self.assertIn("released: dev_1 is merged with its parent again", out)
        self.assertEqual(self.up("dev_1")[0], "caught")
        code, out = self.run_as("dev_1", "catchup", "--hold", "x", "dev")
        self.assertEqual(code, hz.REFUSED)
        self.assertIn("'dev' is not below dev_1", out)
        self.assertEqual(self.run_as("dev", "catchup", "--hold", " ", "dev_1")[0], hz.REFUSED)
        code, out = self.run_as("dev", "catchup", "--hold", "bundle is being profiled", "dev_1")
        self.assertEqual(code, 0, out)
        (m,) = [json.loads(p.read_text())
                for p in (self.ctx.dir / "doorbell" / "dev_1" / "inbox").glob("*.json")]
        self.assertEqual((m["from"], m["priority"]), ("dev", "fyi"))
        self.assertEqual(hz.catchup_hold(self.ctx, "dev_1")["by"], "dev")

    def test_a_hold_ends_when_the_node_presents(self):
        (self.ctx.dir / "briefs").mkdir()
        (self.ctx.dir / "marks").mkdir()
        (self.ctx.dir / "briefs" / "t.json").write_text(json.dumps({"task": "t", "node": "dev_1"}))
        (self.ctx.dir / "marks" / "t.json").write_text(json.dumps({"_node": "dev_1"}))
        self.run_as("dev_1", "catchup", "--hold", "one tree")
        code, out = self.run_as("dev_1", "mark", "t", "--done",
                                read_spend_or_none=lambda sid: (None, "no transcript"),
                                lead_address=lambda ctx, p: (None, None),
                                next_after=lambda *a: (None, False))
        self.assertIn("presented t", out)
        self.assertIn("the hold on merging into dev_1 has ended (dev_1: one tree)", out)
        self.assertIsNone(hz.catchup_hold(self.ctx, "dev_1"))

    def test_many_files_are_told_by_the_folders_they_fall_under(self):
        self.assertEqual(hz.path_groups(["surface/client/src/a.js", "surface/client/b.js",
                                         "tests/test_x.py", "README.md", "loader/db/x/y.py"]),
                         ["surface/client/", "tests/", "README.md", "loader/db/"])
        for i in range(7):
            (self.wt["main"] / "surface" / "client").mkdir(parents=True, exist_ok=True)
            (self.wt["main"] / "surface" / "client" / f"f{i}.js").write_text("x")
        (self.wt["main"] / "tests").mkdir()
        (self.wt["main"] / "tests" / "t.py").write_text("x")
        self.git("main", "add", "-A"); self.git("main", "commit", "-qm", "many")
        self.up("dev")
        line = next(v for k, v in self.items("dev").items() if k.startswith("caught:"))
        self.assertIn("(8 file(s) under surface/client/, tests/)", line)
        self.assertIn("rebuild anything built from them", line)
        self.assertIn('harness catchup --hold "<why>"', line)

    def test_a_fact_measured_on_a_behind_tree_says_so(self):
        self.commit("main", "m1")
        code, out = self.run_as("dev", "fact", "peak", "--is", "3G", "--from", "echo 3G")
        self.assertEqual(code, 0, out)
        self.assertIn("STALE TREE: measured 1 commit(s) behind main", out)
        obs = hz.load_fact(self.ctx, "peak")[1]["observations"][-1]
        self.assertEqual((obs["behind"], obs["behind_of"]), (1, "main"))
        self.assertIn("STALE    measured on a tree 1 commit(s) behind main",
                      self.run_as("dev", "fact", "peak")[1])

    def test_a_retired_fact_keeps_its_figures_and_cites_nothing(self):
        # Log 176: two facts measured on build 9, which the owner deleted.
        gone = str(self.root / "build9.db")
        self.assertEqual(self.run_as("dev", "fact", "cells", "--is", "12",
                                     "--from", f"sqlite3 {gone} 'select 12'")[0], 0)
        self.run_as("dev", "fact", "cells-b10", "--is", "14", "--from", "echo 14")
        self.assertTrue(hz.cited(self.ctx, [gone])[gone])
        code, out = self.run_as("dev", "fact", "cells", "--retire", "")
        self.assertEqual(code, hz.REFUSED)
        code, out = self.run_as("dev", "fact", "cells", "--retire", "build 9 deleted",
                                "--by", "nope")
        self.assertEqual(code, hz.REFUSED)
        code, out = self.run_as("dev", "fact", "cells", "--retire", "build 9 deleted",
                                "--by", "cells-b10")
        self.assertEqual(code, 0, out)
        self.assertEqual(hz.cited(self.ctx, [gone])[gone], [])
        self.assertFalse(any(gone in t for _, t, _ in hz.record_texts(self.ctx, live_only=True)))
        code, out = self.run_as("dev", "fact", "cells", "--recheck")
        self.assertEqual(code, 0, out)
        self.assertIn("is retired, so nothing is re-run: build 9 deleted", out)
        out = self.run_as("dev", "fact", "cells")[1]
        self.assertIn("cells = 12", out)
        self.assertIn("RETIRED", out)
        self.assertIn("harness fact cells-b10", out)
        self.assertIn("retired: build 9 deleted", hz.stale_records(self.ctx)[0]["cells"])
        code, out = self.run_as("dev", "fact", "cells", "--is", "13", "--from", "echo 13")
        self.assertIn("this observation brings it back", out)
        self.assertNotIn("retired", hz.load_fact(self.ctx, "cells")[1])


SKILLS = Path(__file__).resolve().parents[1] / "skills"


class RoleSkills(unittest.TestCase):
    """Log 172: a node's role names the skills it works with, and the harness
    injects them for that node only."""

    def setUp(self):
        self.ctx = FakeCtx({"main": None, "dev": "main", "dev_1": "dev", "dev_r": "dev"})
        self.ctx.tree["nodes"]["dev_r"]["role"] = "reviewer"
        p = mock.patch.object(hz, "skill_dirs", lambda worktree=None: [SKILLS])
        p.start(); self.addCleanup(p.stop)

    def test_a_reviewer_has_ponytail_on_and_its_sibling_has_nothing(self):
        self.assertEqual(hz.on_words(self.ctx, "dev_r"), "ponytail (full)")
        text = hz.on_text(self.ctx, "dev_r")
        self.assertIn("PONYTAIL MODE ACTIVE — level: full", text)
        self.assertIn("You are a lazy senior developer.", text)
        self.assertIn("| **full** |", text)
        self.assertNotIn("| **lite** |", text)              # other levels' rows dropped
        self.assertNotIn("argument-hint", text)             # no frontmatter
        self.assertEqual(hz.on_words(self.ctx, "dev_1"), "")
        self.assertEqual(hz.role_of(self.ctx, "dev_r"), "reviewer")
        self.assertEqual(hz.assignment_for(self.ctx, "dev_r"), ("opus", "medium"))
        self.assertIn("harness-reviewer", hz.skills_for(self.ctx, "dev_r"))
        self.assertTrue(hz.is_lane(self.ctx, "dev_r"))
        self.assertEqual(hz.reviewer_of(self.ctx, "dev"), "dev_r")
        # A node's own skills, with a level, and a skill that cannot be found.
        self.ctx.tree["nodes"]["dev_1"]["skills"] = ["ponytail:ultra", "nope"]
        self.assertEqual(hz.on_words(self.ctx, "dev_1"), "ponytail (ultra), nope")
        text = hz.on_text(self.ctx, "dev_1")
        self.assertIn("level: ultra", text)
        self.assertIn("MISSING  skill 'nope'", text)

    def test_the_tree_refuses_what_the_harness_cannot_act_on(self):
        def bad(**nodes):
            with self.assertRaises(SystemExit), mock.patch("sys.stderr", io.StringIO()):
                hz.validate_tree({"nodes": nodes}, "tree.json")
        bad(a={}, b={"parent": "a", "role": "boss"})
        bad(a={}, b={"parent": "a", "skills": "ponytail"})
        bad(a={"role": "reviewer"})
        bad(a={}, b={"parent": "a", "role": "reviewer"}, c={"parent": "b"})
        bad(a={}, b={"parent": "a", "role": "reviewer"}, c={"parent": "a", "role": "reviewer"})
        hz.validate_tree({"nodes": {"a": {}, "b": {"parent": "a", "role": "reviewer",
                                                    "skills": ["ponytail-audit"]}}}, "tree.json")

    def test_a_subagent_gets_the_same_text(self):
        self.ctx.me = "dev_r"
        with mock.patch.object(hz, "Ctx", return_value=self.ctx), \
             redirect_stdout(io.StringIO()) as o:
            hz.cmd_hook_subagent(None)
        out = json.loads(o.getvalue())["hookSpecificOutput"]
        self.assertEqual(out["hookEventName"], "SubagentStart")
        self.assertIn("PONYTAIL MODE ACTIVE", out["additionalContext"])
        self.ctx.me = "dev_1"
        with mock.patch.object(hz, "Ctx", return_value=self.ctx), \
             redirect_stdout(io.StringIO()) as o:
            hz.cmd_hook_subagent(None)
        self.assertEqual(o.getvalue(), "")


class Reviewer(unittest.TestCase):
    """Log 172 (owner, 2026-10-15): a reviewer between a lead and its workers
    reads every worker's change before the lead sees it, and makes the cuts on
    its own branch; the lead reads the review and signs off."""

    # CatchUp's real repositories and helpers, without re-running its tests.
    git, commit, has, run_as, up = (CatchUp.git, CatchUp.commit, CatchUp.has, CatchUp.run_as,
                                    CatchUp.up)

    def setUp(self):
        CatchUp.setUp(self)
        self.ctx.tree["nodes"]["dev_r"] = {"parent": "dev", "branch": "dev_r", "role": "reviewer"}
        self.wt["dev_r"] = self.root / "wt-dev_r"
        self.git("dev", "worktree", "add", "-q", "-b", "dev_r", str(self.wt["dev_r"]))
        self.idx["nodes"]["dev_r"] = {"branch": "dev_r", "worktree": str(self.wt["dev_r"]),
                                      "parent": "dev", "rank": 2}
        for d in ("briefs", "marks"):
            (self.ctx.dir / d).mkdir(exist_ok=True)
        (self.ctx.dir / "briefs" / "t.json").write_text(json.dumps({"task": "t", "node": "dev_1"}))
        for p in (mock.patch.object(hz, "skill_dirs", lambda worktree=None: [SKILLS]),
                  mock.patch.object(hz, "ensure_ringer", lambda s: None)):
            p.start(); self.addCleanup(p.stop)
        self.op = dict(unreported=lambda *a: [], claim_conflict=lambda ctx, n: (None, "unclaimed"),
                       read_spend_or_none=lambda sid: (None, "no transcript"),
                       assignment_for=lambda ctx, n: ("m", "e"),
                       lead_address=lambda ctx, p: (None, None))

    def inbox(self, n):
        return [hz._read_json(f) for f in
                sorted((self.ctx.dir / "doorbell" / n / "inbox").glob("*.json"))]

    def mark(self, node, *argv):
        return self.run_as(node, "mark", *argv, **self.op)

    def present_t(self):
        self.assertEqual(self.mark("dev_1", "t")[0], 0)
        sha = self.commit("dev_1", "work.py", "a = 1\nb = 2\n")
        code, out = self.mark("dev_1", "t", "--done", "--note", "wrote work.py")
        self.assertEqual(code, 0, out)
        return sha, out

    def review_t(self):
        code, out = self.mark("dev_r", "t.review")
        self.assertEqual(code, 0, out)
        cut = self.commit("dev_r", "work.py", "a = 1\n")
        return cut, out

    def present_review(self):
        return self.mark("dev_r", "t.review", "--done", "--applied", "ponytail-review",
                         "--note", "b was unused; cut it")

    def checked(self, node, sha):
        f = hz.check_report_path(self.ctx, node, sha)
        f.parent.mkdir(parents=True, exist_ok=True)
        f.write_text(json.dumps({"sha": sha, "passed": True, "checks": [{}], "failed": 0}))

    def test_a_worker_s_change_goes_to_the_reviewer_and_never_straight_to_the_lead(self):
        sha, out = self.present_t()
        self.assertIn("It goes to dev_r, the reviewer under dev, as 't.review'", out)
        b = hz.load_brief(self.ctx, "t.review")[1]
        self.assertEqual((b["node"], b["uses"]), ("dev_r", ["ponytail-review"]))
        self.assertEqual(b["review_of"], {"task": "t", "node": "dev_1", "sha": sha, "lead": "dev"})
        self.assertEqual(hz.open_marks(self.ctx)["t"]["_review_task"], "t.review")
        self.assertTrue(any("review it before dev sees it" in m["text"] for m in self.inbox("dev_r")))
        self.assertEqual([m["priority"] for m in self.inbox("dev") if "in review by" in m["text"]], ["fyi"])
        self.assertEqual(hz.lead_owes(self.ctx, "dev"), [])     # nothing to sign off yet
        hz.write_review(self.ctx, "dev_1", "dev_1", sha, "dev")  # even with a read of its own
        code, out = self.run_as("dev", "integrate", "dev_1", read_roster=lambda p: None)
        self.assertEqual(code, hz.REFUSED)
        self.assertIn("is in review by dev_r", out)
        self.assertFalse(self.has("dev", sha))

    def test_the_review_from_opening_to_sign_off(self):
        sha, _ = self.present_t()
        cut, out = self.review_t()
        self.assertIn("took dev_1's 't' at " + sha[:8] + " into dev_r", out)
        self.assertIn("this task uses ponytail-review", out)     # the procedure, printed
        self.assertTrue(self.has("dev_r", sha))
        self.assertTrue(self.has("dev_1", sha) and not self.has("dev_1", cut))   # untouched
        code, out = self.mark("dev_r", "t.review", "--done", "--note", "x")
        self.assertEqual(code, hz.REFUSED)
        self.assertIn("--applied ponytail-review", out)
        code, out = self.mark("dev_r", "t.review", "--done", "--applied", "ponytail-review")
        self.assertEqual(code, hz.REFUSED)
        self.assertIn("is a review: its note is what the lead reads", out)
        code, out = self.present_review()
        self.assertEqual(code, 0, out)
        rev = hz.read_review(self.ctx, "dev_r", cut)
        self.assertEqual((rev["kind"], rev["reviewed_by_node"]), ("reviewer", "dev_r"))
        self.assertEqual(hz.open_marks(self.ctx)["t.review"]["_applied"], ["ponytail-review"])
        ring = next(m["text"] for m in self.inbox("dev") if "reviewed" in m["text"])
        self.assertIn("dev_r reviewed dev_1's 't'", ring)
        self.assertIn("b was unused; cut it", ring)
        # No passing check: the cuts are code nobody else read.
        code, out = self.run_as("dev", "integrate", "dev_r", read_roster=lambda p: None)
        self.assertEqual(code, hz.REFUSED)
        self.assertIn("integrates\n", out.replace("integrates on", "integrates\n"))
        self.assertIn("nothing has checked it", out)
        self.checked("dev_r", cut)
        code, out = self.run_as("dev", "integrate", "dev_r", read_roster=lambda p: None)
        self.assertEqual(code, 0, out)
        self.assertIn(f"check at {cut[:8]}: passed", out)
        self.assertTrue(self.has("dev", sha) and self.has("dev", cut))
        code, out = self.mark("dev", "t.review", "--close", "--no-recycle")
        self.assertEqual(code, 0, out)
        self.assertIn("signed off t for dev_1 with it", out)
        self.assertEqual(hz.open_marks(self.ctx), {})

    def test_one_review_at_a_time_and_on_the_commit_presented(self):
        sha, _ = self.present_t()
        self.review_t()
        self.assertEqual(self.present_review()[0], 0)
        (self.ctx.dir / "briefs" / "u.json").write_text(json.dumps({"task": "u", "node": "dev_1"}))
        hz.write_review_brief(self.ctx, "u", "dev_1", sha, "dev", "dev_r", {})
        code, out = self.mark("dev_r", "u.review")
        self.assertEqual(code, hz.REFUSED)
        self.assertIn("holds 2 commit(s) dev has not integrated: your last review", out)
        # A worker that presents again makes the brief stale until it is rewritten.
        (self.ctx.dir / "marks" / "u.json").write_text(json.dumps(
            {"_node": "dev_1", "_task": "u", "_presented_at": hz._now(), "_presented_sha": "f" * 40}))
        self.git("dev_r", "reset", "-q", "--hard", "dev")
        code, out = self.mark("dev_r", "u.review")
        self.assertEqual(code, hz.REFUSED)
        self.assertIn("presented 'u' again, at ffffffff", out)

    def test_the_gate_takes_the_reviewer_s_record_and_the_workers_inside_it(self):
        repo = self.wt["main"]
        (repo / ".harness").mkdir()
        (repo / ".harness" / "tree.json").write_text(json.dumps({"nodes": {
            "main": {"branch": "main", "kind": "doc"}, "dev": {"branch": "dev", "parent": "main"},
            "dev_1": {"branch": "dev_1", "parent": "dev"},
            "dev_r": {"branch": "dev_r", "parent": "dev", "role": "reviewer"}}}))
        (repo / ".harness" / "manifest.json").write_text(json.dumps({"docs": []}))
        home = self.root / "home"
        state = home / ".claude" / "harness" / re.sub(r"[^A-Za-z0-9]", "-", str(repo))
        guard = Path(__file__).resolve().parents[1] / "templates" / "hooks" / "_guard"
        old = self.git("dev", "rev-parse", "HEAD")

        def gate(new):
            r = subprocess.run([sys.executable, str(guard), "--gate", "dev", new, old],
                               cwd=self.wt["dev"], capture_output=True, text=True,
                               env=dict(os.environ, HOME=str(home)))
            return r.returncode, r.stderr

        def put(kind, node, sha, rec):
            f = state / kind / (re.sub(r"[^A-Za-z0-9]", "_", f"{node}-{sha}") + ".json")
            f.parent.mkdir(parents=True, exist_ok=True)
            f.write_text(json.dumps(rec))

        w = self.commit("dev_1", "work.py")
        self.git("dev_r", "merge", "-q", "--no-edit", w)
        cut = self.commit("dev_r", "work.py", "cut\n")
        (state / "marks").mkdir(parents=True)
        (state / "marks" / "t.json").write_text(json.dumps({"_node": "dev_1", "_review_task": "t.review"}))
        code, err = gate(w)                                # the worker, around its reviewer
        self.assertEqual(code, 1)
        self.assertIn("'dev_1' is in review by 'dev_r'", err)
        code, err = gate(cut)                              # the reviewer, unrecorded
        self.assertEqual(code, 1)
        put("reviews", "dev_r", cut, {"reviewed_by_node": "dev_r", "kind": "reviewer"})
        code, err = gate(cut)                              # recorded, unchecked
        self.assertEqual(code, 1)
        self.assertIn("nothing has passed a check", err)
        put("checks", "dev_r", cut, {"passed": False, "baseline": "b", "new": 2,
                                     "inherited": {"from": "dev_1", "own": 0}})
        self.assertEqual(gate(cut)[0], 1)                  # inherited from the wrong node
        put("checks", "dev_r", cut, {"passed": False, "baseline": "b", "new": 2,
                                     "inherited": {"from": "dev", "own": 0}})
        self.assertEqual(gate(cut)[0], 0, gate(cut)[1])    # the lead's own reds
        put("checks", "dev_r", cut, {"passed": True})
        code, err = gate(cut)                              # and dev_1 arrives inside it
        self.assertEqual(code, 0, err)
        put("reviews", "dev_r", cut, {"reviewed_by_node": "dev_r"})
        code, err = gate(cut)                              # a reviewer's record must say so
        self.assertEqual(code, 1)

    def test_a_presentation_from_before_the_reviewer_integrates_as_before(self):
        self.ctx.tree["nodes"]["dev_r"].pop("role")
        sha, out = self.present_t()
        self.assertNotIn("t.review", out)
        self.ctx.tree["nodes"]["dev_r"]["role"] = "reviewer"
        hz.write_review(self.ctx, "dev_1", "dev_1", sha, "dev")
        code, out = self.run_as("dev", "integrate", "dev_1", read_roster=lambda p: None)
        self.assertEqual(code, 0, out)
        self.assertTrue(self.has("dev", sha))

    def test_reds_the_lead_fails_the_same_are_inherited_not_the_review_s(self):
        # dev_dag, 2026-10-15 19:1x: two reds from the owner's fixture step
        # failed identically at the lead, and integrate had no way past them.
        sha, _ = self.present_t()
        cut, _ = self.review_t()
        self.assertEqual(self.present_review()[0], 0)
        bp = hz.baseline_path(self.ctx)
        bp.parent.mkdir(parents=True, exist_ok=True)
        bp.write_text(json.dumps({"sha": "b" * 40, "arms": {"docs": {
            "failed": False, "files": [], "codes": {}}}}))
        row = lambda *fs: {"name": "docs", "exit": 1, "failedFiles": list(fs)}
        def report(node, at, *fs):
            f = hz.check_report_path(self.ctx, node, at)
            f.parent.mkdir(parents=True, exist_ok=True)
            f.write_text(json.dumps({"sha": at, "passed": False, "baseline": "b" * 40,
                                     "new": len(fs), "checks": [row(*fs)]}))
        integrate = lambda: self.run_as("dev", "integrate", "dev_r", read_roster=lambda p: None)
        report("dev_r", cut, "test_keep.py", "test_route.py")
        code, out = integrate()
        self.assertEqual(code, hz.REFUSED)
        self.assertIn("check dev itself", out)
        lead = self.git("dev", "rev-parse", "HEAD")
        report("dev", lead, "test_keep.py")                     # one of the two is dev's
        code, out = integrate()
        self.assertEqual(code, hz.REFUSED)
        self.assertIn("1 of them fail the same at dev's", out)
        self.assertIn("still new: docs: test_route.py", out)
        report("dev", lead, "test_keep.py", "test_route.py")    # both are
        code, out = integrate()
        self.assertEqual(code, 0, out)
        self.assertIn("inherited, not the review's", out)
        self.assertTrue(self.has("dev", cut))
        inh = hz.read_check_report(self.ctx, "dev_r", cut)["inherited"]
        self.assertEqual((inh["from"], inh["at"], inh["own"]), ("dev", lead, 0))
        self.assertEqual(inh["failures"], ["docs: test_keep.py", "docs: test_route.py"])

    def test_a_catch_up_of_the_presented_worker_does_not_latch_the_review(self):
        # 2026-10-15, four times on dev_dag: the ringer caught a presented
        # worker up, the presentation followed the merge, and the review brief
        # refused to open because it named the commit before it.
        sha, _ = self.present_t()
        lead = self.commit("dev", "lead.py")
        self.assertEqual(self.up("dev_1")[0], "caught")
        self.assertNotEqual(hz.open_marks(self.ctx)["t"]["_presented_sha"], sha)
        code, out = self.mark("dev_r", "t.review")
        self.assertEqual(code, 0, out)
        self.assertIn("took dev_1's 't' at " + sha[:8], out)
        self.assertTrue(self.has("dev_r", sha) and self.has("dev_r", lead))
        # A worker commit after the presentation is still a new presentation.
        self.git("dev_r", "reset", "-q", "--hard", "dev")
        f =self.ctx.dir / "marks" / "t.json"
        rec = hz._read_json(f)
        rec["_presented_sha"] = self.commit("dev_1", "more.py")
        f.write_text(json.dumps(rec))
        (self.ctx.dir / "marks" / "t.review.json").unlink()
        code, out = self.mark("dev_r", "t.review")
        self.assertEqual(code, hz.REFUSED)
        self.assertIn("presented 't' again", out)

    def test_a_rewritten_review_brief_keeps_the_revision_before(self):
        hz.write_review_brief(self.ctx, "t", "dev_1", "a" * 40, "dev", "dev_r", {})
        hz.write_review_brief(self.ctx, "t", "dev_1", "b" * 40, "dev", "dev_r", {})
        b = hz.load_brief(self.ctx, "t.review")[1]
        self.assertEqual(b["revision"], 2)
        self.assertEqual([h["revision"] for h in b["history"]], [1])
        self.assertIn("a" * 12, b["history"][0]["text"])

    def test_integrate_takes_the_presentation_at_the_tip_past_a_parked_one(self):
        # 2026-10-15, dev and dev_migrate: the oldest presented record was the
        # one compared with the tip, so a parked one refused every newer one.
        self.ctx.tree["nodes"]["dev_r"].pop("role")
        old, _ = self.present_t()
        (self.ctx.dir / "briefs" / "u.json").write_text(json.dumps({"task": "u", "node": "dev_1"}))
        self.assertEqual(self.mark("dev_1", "u")[0], 0)
        new = self.commit("dev_1", "u.py")
        code, out = self.mark("dev_1", "u", "--done", "--note", "u")
        self.assertEqual(code, 0, out)
        hz.write_review(self.ctx, "dev_1", "dev_1", new, "dev")
        code, out = self.run_as("dev", "integrate", "dev_1", read_roster=lambda p: None)
        self.assertEqual(code, 0, out)
        self.assertNotIn("has committed since it presented", out)
        self.assertTrue(self.has("dev", new) and self.has("dev", old))

    def test_a_carrier_closes_without_its_lane_being_merged(self):
        # 2026-10-15, dev: the carrier's ring said never merge dev_tests for it,
        # and its --close refused until it was merged.
        self.ctx.tree["nodes"]["dev_r"].pop("role")
        (self.ctx.dir / "briefs" / "t.up-dev_1.json").write_text(json.dumps(
            {"task": "t.up-dev_1", "node": "dev_1", "carries": "t"}))
        self.assertEqual(self.mark("dev_1", "t.up-dev_1")[0], 0)
        sha = self.commit("dev_1", "c.py")
        self.assertEqual(self.mark("dev_1", "t.up-dev_1", "--done", "--note", "c")[0], 0)
        code, out = self.mark("dev", "t.up-dev_1", "--close", "--no-recycle")
        self.assertEqual(code, 0, out)
        self.assertFalse(self.has("dev", sha))
        self.assertIsNone(hz.closed_unmerged(self.ctx, "dev_1", "dev_1"))

    def test_an_fyi_alone_is_no_reason_to_start_a_gone_node(self):
        # 2026-10-15, dev_dag: an --fyi to a node with nothing queued made every
        # Stop hook demand a spawn of it.
        with mock.patch.object(hz, "node_running", lambda ctx, k: (None, None)):
            hz.ring_inbox(self.ctx.dir, "dev_r", "dev", "moot now", "fyi")
            self.assertEqual(hz.released_gone(self.ctx, "dev_r")[1], 0)
            hz.ring_inbox(self.ctx.dir, "dev_r", "dev", "a question?", "high")
            self.assertEqual(hz.released_gone(self.ctx, "dev_r")[1], 1)

    def test_close_after_adds_and_none_replaces(self):
        # Log 175: a sixth condition dropped the five before it.
        (self.ctx.dir / "briefs" / "u.json").write_text(json.dumps({"task": "u", "node": "dev_1"}))
        (self.ctx.dir / "briefs" / "v.json").write_text(json.dumps({"task": "v", "node": "dev_1"}))
        (self.ctx.dir / "briefs" / "seg.json").write_text(json.dumps({"task": "seg", "node": "dev"}))
        self.run_as("main", "brief", "seg", "--close-after", "t", "--close-after", "u")
        code, out = self.run_as("main", "brief", "seg", "--close-after", "v")
        self.assertEqual(code, 0, out)
        self.assertEqual(hz.load_brief(self.ctx, "seg")[1]["close_after"], ["t", "u", "v"])
        self.assertIn("closes only after t, u, v", out)
        code, out = self.run_as("main", "brief", "seg", "--close-after", "none",
                                "--close-after", "v")
        self.assertEqual(hz.load_brief(self.ctx, "seg")[1]["close_after"], ["v"])
        self.assertIn("replaced: t, u, v", out)

    def test_a_brief_s_uses_are_named_with_the_write(self):
        code, out = self.run_as("dev", "brief", "t", "--uses", "ponytail-review")
        self.assertEqual(code, hz.REFUSED)
        self.assertIn("--uses goes in with --write", out)


class SessionPrune(unittest.TestCase):
    """Owner, 2026-10-15: finished sessions are deleted, and a node keeps its
    last 3 as history. The sweep had run once by hand and 475 had piled up."""

    def setUp(self):
        base = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, base, True)
        self.repo, self.wt = base / "proj", base / "proj-dev_1"
        self.repo.mkdir(); self.wt.mkdir()
        self.ctx = FakeCtx({"main": None, "dev_1": "main"})
        self.ctx.repo = self.repo
        self.base = base
        self.real_job_refs = hz.job_refs
        for p in (mock.patch.object(hz, "load_index",
                                    return_value={"byWorktree": {str(self.wt): "dev_1"}}),
                  mock.patch.object(hz, "live_rows", lambda rs: [r for r in rs if r.get("pid")]),
                  mock.patch.object(hz, "job_dirs", return_value={}),
                  mock.patch.object(hz, "job_refs", return_value={}),
                  mock.patch.dict(os.environ, {"CLAUDE_CODE_SESSION_ID": ""})):
            p.start(); self.addCleanup(p.stop)

    def row(self, sid, t, name="proj-dev_1", cwd=None, **k):
        return dict({"sessionId": sid, "name": name, "cwd": str(cwd or self.wt),
                     "startedAt": t}, **k)

    def chosen(self, rows, keep=3):
        return {r["sessionId"]: why for r, why in hz.ended_sessions(self.ctx, rows, keep=keep)}

    def test_each_node_keeps_its_last_three_and_no_more(self):
        rows = [self.row(f"s{i}", i) for i in range(6)] + [self.row("live", 9, pid=1)]
        got = self.chosen(rows)
        self.assertEqual(sorted(s for s, w in got.items() if w is None), ["s0", "s1", "s2"])
        self.assertEqual(got["s5"], "one of dev_1's last 3")
        self.assertNotIn("live", got)                       # running: not finished
        self.assertEqual(sorted(s for s, w in self.chosen(rows, keep=0).items() if w is None),
                         ["s0", "s1", "s2", "s3", "s4", "s5"])

    def test_what_is_never_removed_however_old(self):
        hz._save(self.ctx.lock_path("dev_1"), {"session_id": "holder"})       # asleep holder
        hz._save(self.ctx.state_file("starts", "dev_1", ".json"), {"sid": "starting"})
        hz._save(self.ctx.state_file("limits", "dev_1", ".json"), {"sid": "limited"})
        hz._save(self.ctx.state_file("marks", "t", ".json"), {"_node": "dev_1", "_session": "opener"})
        hz._save(self.ctx.state_file("asks", "q1", ".json"), {"state": "asked"})
        hz._save(self.ctx.state_file("asks", "q2", ".json"), {"state": "done"})
        im = hz.intermediary_name(self.repo)
        rows = [self.row(s, i) for i, s in enumerate(("holder", "starting", "limited", "opener"))]
        rows += [self.row(f"new{i}", 10 + i) for i in range(3)]
        rows += [self.row("q1a", 1, name=f"{im}-q1", cwd=self.base),
                 self.row("q2a", 2, name=f"{im}-q2", cwd=self.base)]
        rows += [self.row(f"d{i}", i, name=hz.documenter_name(self.repo), cwd=self.base)
                 for i in range(5)]
        rows += [self.row("trimmed", 20, name="proj-panel", cwd=self.base / "gone"),
                 self.row("owner's", 1, name="my session"),
                 self.row("design", 1, name="proj-design-x", cwd=self.base)]
        got = self.chosen(rows, keep=3)
        self.assertEqual(got["holder"], "it holds dev_1")
        self.assertEqual(got["starting"], "a start in flight on dev_1")
        self.assertEqual(got["limited"], "it waits out a usage limit on dev_1")
        self.assertEqual(got["opener"], "it opened t, still open")
        self.assertEqual(got["q1a"], "item q1 is open")
        self.assertEqual(got["q2a"], "one of intermediary's last 3")
        self.assertEqual(sorted(s for s, w in got.items() if w is None), ["d0", "d1", "trimmed"])
        for s in ("new0", "new1", "new2"):                  # the protected do not use up the 3
            self.assertEqual(got[s], "one of dev_1's last 3")
        for s in ("owner's", "design"):
            self.assertNotIn(s, got)

    def test_the_ringer_s_run_needs_no_decision_and_is_ledgered(self):
        rows = [self.row(f"s{i}", i) for i in range(5)]
        gone = []
        import argparse
        a = argparse.Namespace(dry_run=False, why=None, auto=True, keep_last=None)
        with mock.patch.object(hz, "all_sessions", return_value=rows), \
             mock.patch.object(hz, "claude_rm", lambda sid: (gone.append(sid), (True, ""))[1]), \
             mock.patch.object(hz, "sweep_decider", side_effect=AssertionError("asked")), \
             redirect_stdout(io.StringIO()) as o:
            hz.sweep_sessions(self.ctx, a)
        self.assertEqual(sorted(gone), ["s0", "s1"])
        self.assertIn("removed 2 session(s)", o.getvalue())
        led = [json.loads(l) for l in (hz.archive_dir(self.ctx) / "ledger.jsonl").read_text().splitlines()]
        self.assertEqual((led[-1]["by"], sorted(led[-1]["removed"])), ("harness (ringer)", ["s0", "s1"]))
        # By hand it still waits on a decision.
        a = argparse.Namespace(dry_run=False, why=None, auto=False, keep_last=None)
        gone.clear()
        with mock.patch.object(hz, "all_sessions", return_value=rows), \
             mock.patch.object(hz, "claude_rm", lambda sid: (gone.append(sid), (True, ""))[1]), \
             redirect_stdout(io.StringIO()) as o:
            hz.sweep_sessions(self.ctx, a)
        self.assertEqual(gone, [])
        self.assertIn("Nothing done. Decide", o.getvalue())

    def test_the_ringer_launches_one_sweep_every_interval(self):
        (self.ctx.dir / "doorbell").mkdir()
        launched = []

        class P:
            pid = os.getpid()                               # alive while the test runs
        with mock.patch.object(hz.subprocess, "Popen", lambda *a, **k: launched.append(a) or P()):
            S = {}
            self.assertTrue(hz.prune_launch(self.ctx, S, now=10_000))
            self.assertFalse(hz.prune_launch(self.ctx, S, now=10_000 + 60))          # too soon
            self.assertFalse(hz.prune_launch(self.ctx, S, now=10_000 + hz.PRUNE_EVERY))  # still running
            (self.ctx.dir / "prune.pid").write_text("999999999")                     # it ended
            self.assertTrue(hz.prune_launch(self.ctx, S, now=10_000 + 2 * hz.PRUNE_EVERY))
        self.assertEqual(len(launched), 2)
        self.assertEqual(launched[0][0][-3:], ["sweep", "--sessions", "--auto"])

    def test_the_count_reads_job_folders_by_the_same_rule(self):
        jobs = self.base / "jobs"
        for i in range(5):
            (jobs / f"j{i}").mkdir(parents=True)
            (jobs / f"j{i}" / "state.json").write_text(json.dumps(
                {"sessionId": f"s{i}", "name": "proj-dev_1", "cwd": str(self.wt), "state": "done",
                 "createdAt": f"2026-10-1{i}T00:00:00.000Z"}))
        (jobs / "j9").mkdir()
        (jobs / "j9" / "state.json").write_text(json.dumps(
            {"sessionId": "s9", "name": "proj-dev_1", "cwd": str(self.wt), "state": "working"}))
        with mock.patch.object(hz, "JOBS", jobs):
            self.assertEqual(hz.ended_count(self.ctx), 2)    # s0, s1; s9 is working

    def test_a_citation_lapses_when_its_record_is_done_with_it(self):
        # A task record by an old session names a file in that session's tmp/:
        # it protects the session while open, and for CITE_GRACE after it closes.
        sid = "abcd1234-0000-4000-8000-000000000000"
        jd = self.base / "jobs" / "abcd1234"
        (jd / "tmp").mkdir(parents=True)
        (jd / "tmp" / "report-on-x.md").write_text("x")
        rows = [self.row(sid, 0)] + [self.row(f"new{i}", 10 + i) for i in range(3)]
        mark = self.ctx.state_file("marks", "t", ".json")
        text = {"_comments": [{"by": f"dev_1 (session {sid[:8]})", "text": "see report-on-x.md"}]}
        with mock.patch.object(hz, "job_dirs", return_value={sid: jd, sid[:8]: jd}), \
             mock.patch.object(hz, "job_refs", self.real_job_refs):
            hz._save(mark, dict(text, _node="dev_1", _closed_at="2026-10-01"))
            self.assertEqual(self.chosen(rows)[sid], "marks/t")               # just closed
            old = time.time() - hz.CITE_GRACE - 60
            os.utime(mark, (old, old))
            self.assertIsNone(self.chosen(rows)[sid])                         # stale: lapsed
            hz._save(mark, dict(text, _node="dev_1"))                         # open: needed
            os.utime(mark, (old, old))
            self.assertEqual(self.chosen(rows)[sid], "marks/t")
