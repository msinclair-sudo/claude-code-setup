---
name: harness
description: Resolve this session's position in an Agent Workstream Harness role tree, claim or release its git node, and load the role-appropriate harness skills. Applies ONLY in repositories enrolled in the harness — both a committed .harness/tree.json and a local binding. Use when starting work in an enrolled worktree, when claiming or releasing a node, or when the user mentions the harness, the role tree, ranks, leads and members, or workstream nodes. In any project that is not enrolled this skill establishes that in one step and stops.
---

# Harness — position and occupancy

Spec: `ref/spec.md` (`R1`–`R11`) — the single copy. The role skills carry no
spec of their own and point back here, so read it at most once per session.
Diagram: `ref/tree.canvas`.
CLI: `~/.claude/harness/bin/harness` — stdlib Python, no daemon, no server.

## First: are we even in this?

```bash
~/.claude/harness/bin/harness whoami
```

**Exit 3 means not enrolled.** Say so in one line and stop. Do not offer to enrol
unless asked. Enrolment takes two keys (`R9`) and both are deliberate:

| key | where | meaning |
| --- | --- | --- |
| `.harness/tree.json` | in the repo, committed | this project defines a role tree |
| `binding.json` | `~/.claude/harness/<slug>/` | *and this machine has joined it* |

## Then: prove position, then take it

Position is derived, never declared (`R1`). The CLI reads it from
`git rev-parse` — you cannot claim a role, only stand in one.

1. `harness whoami` — derives the node from git, checks the platform contract,
   and asserts the session name against the branch.
2. `harness claim`
3. `harness doctor` — proves this worktree is actually guarded by demanding a
   refusal, rather than reading config and trusting it. Exit 6 means unguarded;
   stop and report which arm failed. It proves the DOCUMENT guard fires, and
   only checks that the other hooks are present and match what was installed —
   a green run is not a demonstration that the integration gate fires.
4. Load exactly the skills `whoami` names under `skills`. Nothing else.

You do **not** gather a roster. The CLI calls `claude agents --json` itself, which
lists every live session including this one, so it learns its own name and every
peer's liveness without being told. `--roster FILE` exists only to feed it a
recorded roster for testing.

```
leaf      → harness + harness-upward
mid-lead  → harness + harness-upward + harness-downward
top lead  → harness + harness-downward + harness-root
```

## Prose goes in on stdin, not in quotes

Every long argument here is prose — a brief, a finding, a reason — and prose
about code contains backticks and `$()`. Written the obvious way, a shell eats
them **before this program runs**:

```bash
harness brief x --for y --write "the `continue` stays"   # arrives as "the  stays"
```

The argument is simply shorter. Nothing can detect that, the command prints its
success line, and what is stored is grammatical and wrong. It has already turned
an instruction into one that named nothing and a defect report into one with no
location. Both would have been acted on.

Any long argument may be `-`, which reads it from stdin instead:

```bash
harness brief x --for y --write - <<'EOF'
the `continue` stays, and $(anything) survives
EOF
```

**The quoted delimiter is what makes it literal** — `<<'EOF'`, not `<<EOF`. One
`-` per command. Use it for anything naming code; for a short phrase with no
backticks, quotes are still fine.

## Exit codes are the contract

| code | meaning | what to do |
| --- | --- | --- |
| 2 | platform contract failed (`C1`–`C5`) | **Stop.** Report which check failed. Claude's internals have changed; do not work around it. |
| 3 | not enrolled | one line, stop |
| 4 | refused | the harness declined: a live session holds the node, a recycle would strand work, or a measurement was asked for that cannot be derived. Not a fault — read the line and do what it says |
| 5 | name/position mismatch | the session is misnamed — rename it, never rename the node |
| 6 | `doctor` says this worktree is not guarded as configured | **Stop working.** A hook is missing, inert, or no longer the one that was installed. Nothing about Claude has changed and this is not a code you work around: read which arm failed. **Who repairs it depends on your rank, and the message says which you are** — below rank 0, report it upward and carry on, because `harness scaffold` rewrites the hooks every node in the tree runs and the CLI refuses it. At rank 0 it is yours, after reading the diff it prints. |

`C1`–`C5` assert the undocumented Claude state this harness reads (`R8`). A
failure means refuse, not degrade: a mis-identified session is how two of them
end up holding one node, which is the failure the lock exists to prevent.

## Forcing a stale claim

`harness claim --force` is allowed only when the holder's ref is **absent from
ListAgents**. It records who forced it. It refuses outright if the stale claim
was made on another host — absence from a local roster does not prove death.

## Propagating a tree

From the rank-0 session, once the tree and worktrees exist:

```bash
harness spawn --dry-run     # check what it would launch, where, and as what
harness spawn               # claude --bg -n <project>-<node>, one per node
```

Each node carries the model and effort it should be run as (`R12`). By default
`opus[1m]` at `high` for rank 0 and `medium` for a lead — context follows the
view, and a lead is where reports, conflicts and climbing documents accumulate —
and plain `opus` at `medium` for a leaf — coding is the one workload where the
effort curve is steep, and a leaf holds one task and is then recycled (`R13`). Set `model`/`effort` on a node in `tree.json` to override, or
`--model`/`--effort` to override every node in one launch. `whoami` prints the
pair under `run as`, so a session can see what it was meant to be.

Each is a real session that derives its own position and claims it. Occupied
nodes are skipped. View with `claude agents`, join with `claude attach <id>`.

A subagent cannot hold a node — no session id, no lock, no row in the session
table (`R6`). You may still spawn one for a bounded lookup and use its answer;
what you cannot do is give it a node, a claim or a transaction.

## Releasing

`harness release` at the end of a task. The ledger row is closed, never deleted:
an ancestor resolving a deep conflict (`T8`) reads closed rows.

## Before you derive a number, look it up

```bash
harness fact --list                      # everything measured here
harness fact <name>                      # the value, and the command that made it
harness fact <name> --recheck            # run that command again, here, now
harness fact <name> --is "..." --from "<command>" --what "..."
```

**`--from` is required.** A value with no way to reproduce it is a rumour with a
figure attached: whoever reads it either believes you or pays the entire
derivation again, and the second cost is the one that keeps being paid. Record
the command and checking costs one `--recheck`.

**Record the value in the command's own words**, not in yours. `2` and not
"about two". A value you paraphrased is one `--recheck` can never compare
against, and it will report a difference that is only your phrasing.

**Read what it tells you about where it came from.** Two different things go
stale, and they are not the same:

- *the tree has moved since* — the figure is old at this commit. Re-run it.
- *measured in another worktree* — it is a **different measurement**, not a
  disagreement. Two lanes ran the same check honestly and got 1 and 9, because
  an install directory that `git status` cannot see changes what a check counts.

Any node may record a fact. It is not authority: a measurement tells nobody what
to do. If it should change what someone does, that is a brief, and only a lead
writes one.

## If you need to ask why

```bash
harness charter                     # what this project is for, and its features
harness charter --feature <name>
```

You are not required to read it. A complete brief is enough to work from, and
loading the project's purpose into a scoped task hands back the context that
task was scoped to exclude.

It is there for the moment you need it: when a brief seems to point away from
what the project appears to be for, when you are choosing between two readings
of a scope, or when you simply want to know what any of this is in aid of. The
answer used to depend on your lead being awake.

Only rank 0 and the operator write it. If it is wrong, that is a `--suggest` on
your brief or a word to your lead, not an edit.
