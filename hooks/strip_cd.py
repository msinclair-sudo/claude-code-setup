#!/usr/bin/env python3
"""PreToolUse(Bash): refuse `cd /absolute/path && ...`, so it never becomes a
permission prompt nobody is there to answer.

WHY THIS EXISTS, AND WHY IT REFUSES RATHER THAN STRIPS
-----------------------------------------------------
The global convention is already written down: never prefix a command with
`cd /absolute/path &&`. The tool already starts in the working directory, and
the prefix buys nothing.

What it costs is exact, and was measured on a live tree on 2026-09-08. A
background session ran

    cd "/mnt/.../apps/biblion2-dev" && ~/.claude/harness/bin/harness note ...

and stopped dead. Both halves were allowlisted — `Bash(cd:*)` and
`Bash(~/.claude/harness/bin/harness:*)` are both in the global rules — but an
allow rule matches a command, and this is one COMPOUND command matching neither
prefix. So it asked. It was a background session with no terminal on it, so
nobody answered, and a rank-1 lead sat halted for the best part of an hour
holding three briefs nobody could start.

The name is inherited and is now a misnomer, kept because the documentation
refers to it. A PreToolUse hook CANNOT rewrite tool input — checked against the
reference 2026-09-08, its only decision fields are `permissionDecision`
(allow/deny/ask) and `permissionDecisionReason`. So nothing can strip the `cd`.

Refusing is the better instrument anyway, and the reason is the whole point:

    an `ask` is answered by a HUMAN, and a `deny` is answered by the MODEL.

An unanswerable `ask` strands the session until somebody notices. A `deny`
comes straight back to the model with a reason, it reissues the command without
the prefix, and the lane keeps moving with nobody at a keyboard. The failure
mode this exists to remove is *waiting for a human who is not there*, so
converting the one into the other IS the fix.

WHAT IT DOES NOT DO
-------------------
It does not reimplement the permission matcher. Duplicating an allowlist in a
second place is how two matchers drift apart and a guard starts passing for the
wrong reason; this makes no judgement about what the rest of the command is
allowed to do and defers all of that to the real rules.

It only refuses an ABSOLUTE `cd`. `cd build && make` is ordinary and relative,
stays inside the tree, and is left alone.

FAILING SILENTLY IS PART OF THE CONTRACT
----------------------------------------
This runs before every Bash call in every session on the machine. Anything it
prints on the allow path is noise in every transcript forever, and anything it
raises is a broken Bash tool. So: no output unless it refuses, and every
unexpected condition exits 0 and allows.
"""
import json
import re
import sys

# `cd <absolute-or-~ path> &&` — or `;`, which is the same mistake with a worse
# failure mode, since the rest runs whether the cd succeeded or not.
#
# The path may be quoted (it usually is; these paths have spaces in them), and
# `\S` will not do for the unquoted form for the same reason.
CD_PREFIX = re.compile(
    r"""^\s*cd\s+(?:'(?P<sq>/[^']*|~[^']*)'|"(?P<dq>/[^"]*|~[^"]*)"|(?P<bare>(?:/|~)\S*))\s*(?:&&|;)""",
    re.VERBOSE,
)


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except Exception:
        return 0                      # unparseable input is not this hook's call
    if payload.get("tool_name") != "Bash":
        return 0
    cmd = (payload.get("tool_input") or {}).get("command")
    if not isinstance(cmd, str):
        return 0
    m = CD_PREFIX.match(cmd)
    if not m:
        return 0
    path = m.group("sq") or m.group("dq") or m.group("bare") or ""
    rest = cmd[m.end():].strip()
    print(json.dumps({"hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "permissionDecision": "deny",
        "permissionDecisionReason": (
            f"Drop the `cd {path} &&` prefix and run the command on its own:\n\n"
            f"    {rest[:400]}\n\n"
            "The tool already starts in the working directory, so the prefix "
            "changes nothing about where this runs. What it DOES change is "
            "whether it needs a human: an allow rule matches a command, and "
            "`cd X && Y` matches no rule for `cd` and no rule for `Y`, so the "
            "pair asks for permission even when both halves are allowed. In a "
            "background session there is nobody to ask, and it stops there "
            "until somebody notices — measured at the better part of an hour "
            "on a lead holding three briefs.\n\n"
            "If you genuinely need a different directory, pass it to the tool "
            "rather than to the shell: `git -C <path>`, `make -C <path>`, "
            "`python3 <path>/x.py`, or run from the right place to begin with."
        )}}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
