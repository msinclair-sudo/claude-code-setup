---
name: harness-downward
description: Act toward your children in an Agent Workstream Harness — issue scoped tasks with recorded intent, review approaches, answer questions, integrate work by fast-forward, mediate merge conflicts, and relay document requests upward. Load only when the harness skill's whoami reports harness-downward for this session. Covers transactions T1, T4-integrate, T5-relay, T7, T8, T11-review and T12-answer.
---

# Downward — what you do toward your children

Spec: `~/.claude/skills/harness/ref/spec.md` — one copy, shared by all four
harness skills. Every rule below has a heading there. If you already read it
this session under another role, do not read it again: it is the same file.

## `T1` — issuing a task

A task record carries: **id, lane, path scope, intent, checks, estimated band,
and the seams you are holding for it.**

- **No scope, no task.** Check it against the global registry first — no two open
  tasks anywhere in the tree may claim the same path (`I3`). Overlap is refused
  at issue time, not resolved later.
- **No intent, no task.** `src/parse/**` is a scope. *"widen the parser signature
  for encoding support"* is an intent. Without the second you will later be asked
  why a conflict happened and will have nothing but a guess — and a confident
  invented cause is worse than none.
- **Band, not a number** (`I10`). `XL` is a refusal: if you cannot bring a task
  under `L`, split it or escalate.

## `T11` — reviewing an approach

Before the child's first commit. It sends a few lines; you approve or redirect.
This is where your model of the subtree gets built — cheaply, while it is small.
Reconstructing it later during a conflict costs several times more.

## `T12` — answering

Answer from scope, intent and seams. **"I don't know, escalating" is a correct
answer.** Do not guess; escalate under `T5`/`T9` instead.

## `I9` — you own the seams

Interfaces between your children are yours. Insides are theirs. This is what
keeps your context shallow: *k* interfaces, not *k* implementations.

## Verifying before you integrate

Fan out one subagent per child, in parallel, each **read only**:

- is it caught up? `git merge-base --is-ancestor <your-branch> <child-branch>`
- run every check in the manifest, including after one fails, and report each
  one's declared blind spot verbatim

Then integrate sequentially, yourself. Do not parallelise the merges: one node is
one branch and one index.

Do not reach for a workflow. The fan-out is a few read-only checks and the merge
half is a loop — a script would be a layer to maintain for no property you need.
And never try to give a subagent a node: it shares your session id, pid and
working directory, so it cannot hold a lock or be attached to.

## `T4` — integrating

```bash
git merge --ff-only <child-branch>
```

Performed in **your** worktree, because you own the node. Nobody pushes — a
checked-out branch rejects pushes. If it is not a fast-forward the child skipped
catch-up 2; hand it back rather than merging manually.

Because every integration is a fast-forward, `pre-merge-commit` never fires on
this path. `reference-transaction` is the primary guard here, not a backstop.

## `T7` / `T8` — mediating a conflict

The child hits the conflict during its catch-up 2 and sends you the stages and
authors. **Which transaction this is depends on authorship, not tree position:**

```bash
git log --merge --format='%(trailers:key=Task,valueonly)' -- FILE
```

| the trailers name tasks | transaction | what you do |
| --- | --- | --- |
| **you issued** | `T7` | you hold both intents — state the cause, then propose |
| **you did not issue** | `T8` | read the retained ledger rows; fetch down only if that is insufficient |

Two sibling lead nodes conflict under `T8`, because the work was authored ranks
below you.

Then, in order:

1. State the **cause** before the resolution. The cause is the part only the
   assigner has.
2. Require the child to re-run its own checks and state the effect — a claim, not
   agreement. There is a rank gradient here: asked *does this look right?* a
   member says yes. Do not ask that question.
3. Run the **absent** member's checks. Their code is being changed and they are
   not here; their tests stand in for a signature nobody can verify.

**Two escalations, both rare.** No recorded intent → say so and raise a ruling
request rather than invent a cause. The same file conflicting twice under you →
that is a scope defect, not a merge. Re-cut the scopes.

## `T5` — relaying documents

You write no documents. A request from below is reviewed *by you* — that review
is the reason the chain exists — then passed up. Batch and deduplicate before
relaying: two children asking for the same change should become one request for
every ancestor above you.

## Seeing your subtree

One **ListAgents** call shows which children are live and which are busy. Send a
`T2` behind-mark when it will actually be read.

## Mark the task when you issue it

A `T1` without a mark cannot produce a measured actual at `T10` — the child can
only guess its share, and a guess recorded as a measurement is worse than no
figure. Tell the child to run `harness mark <task-id>` as its first act.

Do not force a mid-task recycle if you want the number: a recycled session starts
a new transcript and the mark no longer subtracts (`R13` against `I10`). Recycle
at the end of commits, which is where it belongs anyway.

## Issue a plan, not a task

Everything you know goes down at once (`T1`): scope, intent, the approach *you*
have decided, the check set, the seams you are holding, and what done looks like.
The same information delivered in pieces instead of up front costs a measured 39%
across 15 models, and the penalty appears at **two** pieces — so a single
follow-up detail is already the failure. Planning is your work. A lead that issues
a stub and answers questions afterwards has chosen the 39%.

Your child will restate the plan back to you once (`T11`). Read it and correct
only a misreading; there is nothing to approve. It exists because models are
unreliable at noticing they need to ask — one model in a published benchmark
never asked at all — so a forced restatement is the cheapest detector for a
misunderstanding that would otherwise stay silent.

## Read the diff before you integrate — this is now a gate

```bash
harness review <node> --record   # reads it AND records the read
harness review --children        # every child: commits, diffstat, seams
harness review <node> --diff     # plus the full patch
```

**`git merge --ff-only` will be refused without a recorded review.** A member
cannot verify its own work: measured, a model revisiting its own output without
an external check gets worse in every configuration tested, and improves only
when an oracle is present. You are the oracle.

The record is keyed to the child's exact commit, so a new commit invalidates it
automatically. If you meet the refusal, note that git checks out the fast-forward
before the ref update it aborts: the branch is unmoved and safe, the working tree
is not, and `git reset --hard HEAD` restores it.

Attend to two lines in particular. **`SEAM with <sibling>`** means two of your
children changed the same file: that is yours to judge under `I9`, neither of
them can, and both may be individually fast-forwardable right up until the first
one lands. **`document check UNAVAILABLE`** means the guard could not be asked —
treat that as unknown, not as clean, and find out why before merging.

## Recycle a child once its work has landed

A member holds nothing that is not written down, so its context is transcript
rather than knowledge once its commits are in (`R13`). After you integrate a
child, end its session and start a fresh one on the same node:

```bash
harness recycle <node> --dry-run     # see what it would do, and what it refuses
harness recycle --children           # every child of this node
```

It refuses by itself on a dirty worktree, on commits not yet in you, on a busy
session, and on rank 0. Take those refusals at face value — each one means work
would be stranded.

**When a child's checks fail, retry it higher before you reason about it.**

```bash
harness recycle <node> --escalate --dry-run   # shows the level it would move to
harness recycle <node> --escalate             # one level above that node's own setting
```

**This is available, not recommended by default.** The figures behind the
retry-cheap-then-escalate pattern are an unreproduced vendor claim, and a
published study undercut its own retry method: a longer *first* attempt beat
selective recovery on accuracy and total tokens together, by 28%. Prefer raising
a node's starting effort in `tree.json` over retrying it higher. Reach for
`--escalate` when you want the failure and the retry both on the record, not as
the routine recovery. If it fails a second time, that is a finding, not a budget
problem — read it.

The one it cannot judge is whether you owe that child an answer. A member idling
on an unanswered `T12` question looks exactly like a member idling with nothing
to do. You are the only one who knows, which is why this is your call and not a
timer's. Answer first, then recycle.

Never `claude rm` — it deletes the worktree, and the worktree is the node.
