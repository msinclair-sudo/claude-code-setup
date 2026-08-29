"""Harness segment for a Claude Code statusline — paste-ready, zero-dependency.

Contract: returns "" for ANY reason it cannot produce a segment — not a repo, not
enrolled, no index yet, branch is not a node, malformed state. A statusline runs
in every session regardless of harness enrolment, so absence must cost nothing
and must never raise.

Cost: one `git rev-parse` (common-dir and branch in a single call) plus two file
reads. The session table is ~100 small files and reads in about 30ms.

    seg = harness_segment(cdir)          # cdir = the statusline's project dir
    if seg: print(seg)                   # else print nothing at all

Renders, e.g.:   ↑dev·  [ui]  ⇄ api!6 m1◦  ↓ ui1· ui2·
    •  busy      ◦ idle      ·  nobody      !N  N sessions sharing ONE worktree
"""
import json, os, re, glob, subprocess

_MARK = {"busy": "•", "idle": "◦"}


def harness_segment(cdir):
    try:
        r = subprocess.run(
            ["git", "-C", cdir, "rev-parse", "--path-format=absolute",
             "--git-common-dir", "--abbrev-ref", "HEAD"],
            capture_output=True, text=True, timeout=2)
        if r.returncode:
            return ""
        common, branch = r.stdout.split("\n")[0].strip(), r.stdout.split("\n")[1].strip()
        repo = os.path.dirname(common.rstrip("/"))
        slug = re.sub(r"[^A-Za-z0-9]", "-", repo)
        idx_path = os.path.expanduser(f"~/.claude/harness/{slug}/index.json")
        if not os.path.isfile(idx_path):
            return ""                      # not enrolled — stay silent
        idx = json.load(open(idx_path))
        node = idx.get("byBranch", {}).get(branch)
        if not node:
            return ""
        me = idx["nodes"][node]

        # Occupancy: ~/.claude/sessions/<pid>.json carries cwd, status and name.
        # Most files are dead sessions, so every pid is checked.
        occ = {}
        by_wt = idx.get("byWorktree", {})
        for f in glob.glob(os.path.expanduser("~/.claude/sessions/*.json")):
            try:
                d = json.load(open(f))
                os.kill(d["pid"], 0)
            except Exception:
                continue
            n = by_wt.get(d.get("cwd", ""))
            if n:
                occ.setdefault(n, []).append(d)

        def mark(n):
            ss = occ.get(n, [])
            if not ss:
                return f"{n}·"
            if len(ss) > 1:
                return f"{n}!{len(ss)}"     # more than one session in one worktree
            return n + _MARK.get(ss[0].get("status"), "?")

        bits = []
        if me.get("parent"):
            bits.append("↑" + mark(me["parent"]))
        bits.append(f"[{node}]")
        if me.get("siblings"):
            bits.append("⇄ " + " ".join(mark(s) for s in me["siblings"]))
        if me.get("children"):
            bits.append("↓ " + " ".join(mark(c) for c in me["children"]))
        return "  ".join(bits)
    except Exception:
        return ""


if __name__ == "__main__":
    import sys
    print(harness_segment(sys.argv[1] if len(sys.argv) > 1 else os.getcwd()))
