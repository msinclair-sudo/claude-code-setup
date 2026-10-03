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
             mock.patch.object(hz, "queue", return_value=[]):
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
