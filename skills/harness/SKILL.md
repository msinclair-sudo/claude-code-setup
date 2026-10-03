---
name: harness
description: Resolve this session's position in an Agent Workstream Harness role tree, claim or release its git node, and load the role-appropriate harness skills. Applies ONLY in repositories enrolled in the harness — a committed .harness/tree.json plus a local binding. Use when starting work in an enrolled worktree, when claiming or releasing a node, or when the user mentions the harness, the role tree, ranks, leads and members, or workstream nodes. In a project that is not enrolled it establishes that in one step and stops.
---

# Harness — position and occupancy

CLI: `~/.claude/harness/bin/harness`. Spec, on demand only: `ref/spec.md`. Diagram: `ref/tree.canvas`.

## First: are we even in this?

Run `~/.claude/harness/bin/harness whoami`. **Exit 3 means not enrolled:** say so in one line and stop. Do not offer to enrol unless asked. Enrolment takes two keys: `.harness/tree.json` committed in the repo, and `~/.claude/harness/<slug>/binding.json` on this machine.

## Then: prove position, then take it

Position is derived from git, never declared. The CLI queries `claude agents --json` itself; do not gather a roster (`--roster FILE` is for tests only).

1. `harness whoami` — derives the node, checks the platform contract, asserts the session name against the branch.
2. `harness claim` — then work your queue until you are blocked on your lead or the operator. Claiming is not the end of the job.
3. `harness doctor` — demands a refusal from the document guard. Exit 6: stop and report which arm failed. Green means the guard fires and the other hooks match what was installed; it does not prove the integration gate fires.
4. Load exactly the skills `whoami` lists under `skills`. Nothing else.

```
leaf      → harness + harness-upward
mid-lead  → harness + harness-upward + harness-downward
top lead  → harness + harness-downward + harness-root
```

`harness focus [task|'glob*'...|--clear]` holds the owner's priority; nags outside it fold into one line. Nags appear only at orientation (session start and each prompt), not after every command.

## Prose goes in on stdin, not in quotes

The shell eats backticks and `$()` before the CLI runs, silently. Any long argument may be `-` (one per command), read from a quoted heredoc:

```bash
harness brief x --for y --write - <<'EOF'
the `continue` stays, and $(anything) survives
EOF
```

`<<'EOF'`, not `<<EOF`. Avoid `"$(cat file)"`; it strips trailing newlines. Quotes are fine for a short phrase with no backticks.

## Exit codes are the contract

| code | meaning | what to do |
| --- | --- | --- |
| 2 | platform contract failed (`C1`–`C5`) | **Stop.** Report which check failed. Claude's internals have changed; do not work around it. |
| 3 | not enrolled | one line, stop |
| 4 | refused | the harness declined: a live session holds the node, a recycle would strand work, or a measurement was asked for that cannot be derived. Not a fault — read the line and do what it says |
| 5 | name/position mismatch | the session is misnamed — rename it, never rename the node |
| 6 | `doctor` says this worktree is not guarded as configured | **Stop working** and read which arm failed. Below rank 0, report it upward and carry on (`harness scaffold` is refused to you). At rank 0 it is yours, after reading the diff it prints. |

No exit code at all, with the tool call *blocked by the auto-mode classifier*, means the harness never ran. Say the command did not run; hand the operator the exact command. Never ask another session to run something you were denied.

## Claiming a held node

`claim` judges liveness itself (the lock's pid on this host, then the session file, then a live roster row) and takes a dead holder's lock without help. `--force` is needed only for a lock claimed on another host, after you have checked it is not running there.

## Propagating a tree (rank 0)

`harness spawn --dry-run`, then `harness spawn` (one `claude --bg` per node; occupied nodes skipped). Each node runs at the model and effort `whoami` prints under `run as`; override in `tree.json` or with `--model`/`--effort`. A subagent cannot hold a node, claim or transaction; use one only for bounded lookups.

## Releasing

`harness release` at the end of a task. The ledger row is closed, never deleted.

## Before you derive a number, look it up

`harness fact --list`, `harness fact <name>`, `harness fact <name> --recheck`. Record with `harness fact <name> --is "..." --from "<command>" --what "..."`: `--from` is required, and the value goes in the command's own words. *Tree has moved since* means re-run; *measured in another worktree* is a different measurement, not a disagreement. A fact is not a brief.

## If you need to ask why

`harness charter [--feature <name>]` — optional; read it when a brief seems to point away from the project's purpose. Only rank 0 and the operator write it.

Why each rule exists: `ref/why.md` — read only when you need the reason.
