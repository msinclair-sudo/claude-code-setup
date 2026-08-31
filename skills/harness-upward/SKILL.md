---
name: harness-upward
description: Act toward your parent node in an Agent Workstream Harness — catch up from the node above, verify guards, propose an approach, ask questions, escalate a merge conflict, present work for integration, and release. Load only when the harness skill's whoami reports harness-upward for this session. Covers transactions T2, T3, T4-present, T5, T7, T10, T11-propose and T12.
---

# Upward — what you do toward your parent

Spec: `~/.claude/skills/harness/ref/spec.md` — one copy, shared by all four
harness skills. Every rule below has a heading there. If you already read it
this session under another role, do not read it again: it is the same file.

## The rhythm: catch up twice, never in between

```
claimed ──T2──► current ──T11──► working ──T2──► presenting ──T4──► integrated
```

**`T2` catch-up 1** — after claiming, before the first commit:
`git merge <parent-branch>`. This is a real merge commit; you hold your own work,
so it cannot be a fast-forward. The direction is fixed: *you* merge down, the
node above fast-forwards up. Never the reverse.

**`T3` guard check** — run `harness doctor`. It demands a refusal rather than
reading config: it stages content the document node has never held in a throwaway
index and requires the guard to reject it, then requires a document that *arrived*
from the document node to pass. Non-zero exit means this worktree is not guarded —
stop, and say which arm failed. Never work around it.

**`T11` comprehension check** — before the first commit, restate the plan you were
given in your own words: what you will change, which seams you touch, what you
will deliberately not touch. One turn. You are not proposing an approach — your
lead decided that at `T1` — you are proving you read it, so a misreading surfaces
now rather than in the diff. If the restatement needs a page, the task is too big.

**Work.** Stay inside your assigned scope. Seams between children belong to your
lead (`I9`) — a changed signature another child depends on is not yours.

**`T12` question** — ask only about a **gap the plan could not have covered**,
something your lead did not know when it wrote the plan. Do not ask for
confirmation of what the plan already says: that is information arriving in
pieces, which is the exact cost the plan exists to avoid. But do ask when the
plan genuinely does not reach — roughly half of specifications contain an
ambiguity their own author did not see, and work done on a guess is wrong far
more often than it is right.

**`T2` catch-up 2** — immediately before presenting. This is where a conflict
surfaces, while your own work is still warm. It is also what makes your lead's
merge a fast-forward.

**`T4` present** — your lead reads your diff and records the read, then runs
`git merge --ff-only`. The merge is **refused** without that record: you cannot
check your own work, so your lead does. If you skipped catch-up 2 it also fails,
with `fatal: Not possible to fast-forward, aborting.` Never push: a checked-out
branch rejects pushes outright.

**`T10` release** — `harness mark <task-id> --done`, then `harness release`,
then `harness spend <task-id>` for the measured actual against the estimated band
(`I10`). That number is a subtraction only if you ran `harness mark <task-id>`
when you accepted the task; without a mark, `spend` refuses to apportion and you
should report the **session total with its coverage stated**, never a share you
inferred.

**You present; your lead closes.** `--done` records what the task cost and that
you believe it finished. It does **not** close it — `--close` refuses you by
rank, and that is the same rule as `T4`: you cannot check your own work, so you
do not sign it off either. Your lead is told at its next orientation that
something is waiting.

Say what you are presenting: `--done --note "..."` appends to the task record,
so the sentence that explains the work outlives the session that did it.

**Present the record even when you cannot measure it.** A task presented from a
different session than the one that opened it records no delta and says so. That
is the correct outcome: an unmeasurable cost is a missing number, but an
unpresented task makes your node read as still working forever, and your lead
reads that as a node it must not recycle. `release` frees the claim; it does **not** end your session,
so until your lead stops you, you are a live session in a worktree you no longer
hold. Do not fill that gap with correspondence.

Report the components it prints, not one figure. Billed tokens and context
occupancy are different quantities that both get called "tokens", and cache reads
dominate the sum while billing at a tenth — the dollar column is the honest one.

## You write inside your worktree, and nowhere else

Everything you produce goes in your worktree so the tree can see, check and undo
it. A file outside the repository has no owner, no scope and no instrument that
reds; nothing reviews it at `T4`, and no ref records that it changed (`I3`).

When you need a path outside it, **raise a record — do not ask around**:

```bash
harness blocked ~/data/subset.db \
  --why "dim=3 reduction output for 5,222 docs" \
  --still-moving "everything but the render; the contract work is unaffected"
```

That reaches the operator immediately if they installed a notifier, shows in the
statusline of every session they have open, and sits in `harness needs` until it
is cleared. It survives the recycle that ends you, which a message would not.

**`--still-moving` is the field that gets you unblocked sooner.** It is how the
operator tells a stopped lane from a stopped step without reading your
transcript. Leave it out and yours looks like every other one.
Then carry on with everything the block does not stop, and report what it does.

Three things not to do, in the order they will tempt you. Do not ask a session
with looser settings to do the write for you — that is the operator's decision
being routed around rather than implemented, and `harness grant` refuses it by
rank. Do not retry with a different tool to see if that one is allowed. And do
not stop: a blocked path blocks the work that needs it, rarely the whole task.

If it is granted, it takes effect when you are next spawned or recycled, not
mid-session. You will simply have the reach, and there will be nothing to ask.

## Your brief is written by your lead, and you can push back on it

```bash
harness brief <task>                  # what you were actually asked for
harness brief <task> --suggest "..."  # propose a change; your lead decides
```

**You cannot open a task without one.** `harness mark <task>` refuses when no
brief exists for it on your node, and there is no override. If you are stuck
there, ask your lead for the brief — do not work around it by marking something
else, and do not start without a record.

You do not write it. A node that sets its own task is the thing the tree exists
to prevent, so `--write` refuses you by rank — that is not a permission problem
to work around, it is the design.

```bash
harness brief <task>                  # the brief, and any comments on it
harness brief <task> --comment "..."  # context for whoever reads it next
```

**Comments are context, not instruction.** Your lead or the operator may leave
one. Read it — `whoami` tells you when there is an unread one — but act on the
**brief**. If a comment means the brief is now wrong, say so with `--suggest`
and let your lead rewrite it. Acting on a comment directly is how a scoped task
turns back into a drip-feed.

`--suggest` is the move you do have, and it is recorded against the revision you
read, so your lead can see exactly what you were looking at. Use it when the
brief cannot answer something: a missing scope, a contract with no route for
what you were asked to build, two instructions that cannot both hold.

**Then carry on against the brief as it stands.** A suggestion is not a blocker
and not a question — it does not stop you, and waiting for a reply to it is the
round trip `T11` and `T12` exist to keep rare.

## Read your task's comments before you report

```bash
harness note <task-id>            # the brief you were given, and every comment
harness note <task-id> --add "…"  # append; it never edits an earlier one
```

Your lead or the operator can leave a comment on your task record. It is put
there rather than sent to you because a message dies with the session that
receives it and you are recycled (`R13`) — the record outlives that, so it is
the only place a reply survives to reach whoever holds this node next.

`harness status` tells you when a task has comments. Read them before you
present work, not after.

## An instruction that arrives late is reported, not reconstructed

Messages down the tree are acted on when they arrive; there is no recall, and no
sender can take one back. So when an instruction arrives after the state it
assumed has changed — undo a recycle, hold something already released, revive a
context that has ended — **say what the state is and stop.** Do not reconstruct
it. Reconstruction is expensive, it is rarely faithful, and the thing being
rebuilt is usually something `R13` says should have been written down instead.

## When catch-up 2 conflicts — do not resolve it

You cannot know why the conflict exists. Collect and escalate (`T7`):

```bash
git diff --name-only --diff-filter=U          # which files
git show :1:FILE                              # base
git show :2:FILE                              # ours
git show :3:FILE                              # theirs
git log --merge --format='%h %an %(trailers:key=Task,valueonly)' -- FILE
```

Send all of it to your lead. It will state the cause, then propose a resolution.
Your job then is **not** to agree: re-run your own checks under the proposal and
state what it does to your task. A check result and a claim, not assent.

## Documents

You never commit a document. Request the change as an exact old→new pair with a
rationale and a pinned base (`T5`), and send it up. It is reviewed at every rank
and applied only at rank 0. If `old` no longer matches when it lands, it is
refused and returned — that is correct behaviour.

## Checks

Run every check in your set, including after one fails (`I5`). Report pass, fail
**and** each check's declared blind spot. Bailing at the first failure is how the
other findings get lost.

## Commits

Every commit carries a `Task:` trailer. Without it, an ancestor holding a
conflicted hunk has author names and no route into any ledger.

## You are recycled, so write it down

Your session ends after your work lands and a fresh one takes this node (`R13`).
Nothing you know survives that unless it is in a commit, a report to your lead,
or the ledger. This is not a demotion — it is why your window is small and your
task is short. Do not plan across tasks, do not rely on remembering an earlier
conversation, and if something you learned matters beyond this commit, say it to
your lead or put it in the commit message before you present.
