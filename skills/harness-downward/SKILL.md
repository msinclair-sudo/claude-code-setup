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
harness recycle --idle               # only children with no OPEN task record
```

**`--idle` is the sweep at subtree close, and it is the one that matters.** A
claimed node with no open task is not idle, it is capacity with no object, and
capacity with no object gets spent on elective correspondence — messages nobody
can terminate, because no transaction ends them and `SendMessage` passes through
no instrument that could count them. Recycling ends such a thread mechanically:
not by anyone deciding to stop, but by the counterparty no longer existing in
that context. Close the task record first (`harness mark <task> --close`), or
`--idle` will read the node as still working.

`harness status` shows you which is which — an open task by name, or
`unassigned`. Take `unassigned` on a live node as a standing prompt.

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

## You write your children's briefs

```bash
harness brief <task> --for <child> --write "..."   # write it, or rewrite it
harness brief <task>                               # read it back, with suggestions
harness brief <task> --resolve N                   # a suggestion you have addressed
```

The brief is the `T1` plan in a file: scope, the approach **you** decided, the
check set, the seams, what done means. Write it before the child starts, not in
pieces afterwards — the same information delivered in pieces costs 39%, and the
penalty lands at two pieces.

**This is a gate, not advice.** `harness mark` refuses a task with no brief and
has no override, so a child you have not briefed cannot open one. `spawn` and
`recycle` warn you when a node has nothing briefed, which is your cue to write
it rather than let a fresh session start and ask.

**A brief is a plan, not a record.** Rewriting it replaces the earlier text and
that is correct; a working document that behaves like provenance is one nobody
dares to correct. The append-only half is `harness note`, and comments there
survive the recycle that ends the session you are answering.

You cannot write a grandchild's brief. `dev_1`'s lead is `dev`, so `dev` writes
it — if you are above that, tell the lead what you want and let it write.

## Findings come up to you, and become work only with approval

`whoami` tells you when a child has handed one up:

```
findings 1 handed up to you: pixel-depth
         potential work nobody has scoped — brief it (--from-finding) or
         decline it. harness finding --list
```

Two outcomes, and both are first class:

```bash
harness brief pixel-size-fix --for dev_1 --from-finding pixel-depth --write "..."
harness finding pixel-depth --drop "why it is not worth a session"
```

**A brief written from a finding is gated on the operator.** It is written in
full, everyone can read it, and it is in no queue — `harness mark` refuses it and
`recycle` will not start on it — until the operator approves. **You cannot
approve it yourself, and neither can rank 0**: a lead approving the brief it just
wrote is the gate approving itself.

Nobody is idle over it. The lane that raised the finding carried on with its
queue, which is what makes gating safe.

**Do not gate everything.** The operator's queue is their attention and it is
finite. A finding you would not spend a session on is one you decline, in a line,
on the record — and the record is the point: the next lead to notice the same
thing gets your answer instead of the silence.

`--needs-approval` puts the same gate on any brief, finding or not, when you want
work written up but not started.

## Bands are token counts, and XL is a refusal

| band | new tokens | shape |
| --- | --- | --- |
| S | ≤ 40k | one file, approach already known |
| M | 40k – 120k | several files, some exploration |
| L | 120k – 300k | needs design, touches more than one seam |
| XL | > 300k | **not a task** — a decomposition you have not done yet |

`harness mark <task> --band XL` is refused outright. If you cannot bring a piece
under L, split it or escalate; that is the whole of `I8`.

**New tokens means up + down** — what was sent for the first time plus what was
generated. It excludes resent context, which is the conversation handed back
every turn: count that and every band is blown by the second turn, and you are
measuring how long the session talked instead of how big the job was.

The estimate is yours and the measurement is the member's. When they come back
apart, that is your estimate that was wrong. It is the only thing that makes the
next one better, so ask for it plainly rather than treating an over-band as the
member's problem.

## Cite figures, do not paste them

```bash
harness brief <task> --for <child> --fact endpoint-reach --write "..."
```

A number typed into a brief is true on the day you write it and silently wrong
after that. The honest thing to write beside one is the date it was taken and an
instruction to re-derive — which is a lot of longhand for something the record
can carry.

`--fact` resolves when the brief is **read**, so your member sees the current
value, its age, and the command that produced it:

```
fact      todo-count = 3  [the tree has moved since]
          2d ago · grep -c TODO notes.txt
```

Citing a fact nobody has recorded is refused, which is what keeps a citation from
being a promise. If you need a figure that does not exist yet, that is a task:
brief someone to measure it and record it.

## The queue, and the boundary between tasks

```bash
harness queue                       # every node in the tree
harness queue dev_1                 # one node, in the order you set
harness queue dev_1 --order a,b,c   # set it; unnamed keep their place behind
```

Briefs queue in the order you write them. **Order them deliberately** — a member
holding four briefs and no order does not have a backlog, it has a choice, and
a member choosing which task to do first is choosing its own work. It is also
where "shall I start?" comes from: an ambiguity at the top of a session gets
resolved by asking.

**Recycle between tasks.** When you sign off, you are told which it is and given
the command:

```
signed off doi-index for dev_1
  next for dev_1: ingest-2024  — recycle it first, do not hand it on:
    harness recycle dev_1
```

Do it. Handing a second task to a session that just finished one is the pattern
with the best evidence against it in this whole design: a persistent worker
compounds its own earlier mistakes, scale does not fix it, and explicitly
clearing history does. The fresh session costs less than the errors you keep.

**Couple two tasks only when the context is the point:**

```bash
harness brief doi-verify --for dev_1 --with doi-index \
        --why "it checks the index the previous task just built; a fresh
               session would re-read the same 40 files to know what it is
               checking" --write "..."
```

`--why` is required and an empty one is refused. Coupling keeps a session alive
across a boundary the evidence says to reset at, so the reason has to be real:
shared context expensive to rebuild, not "they're both about the UI". A coupled
task has no queue position of its own — it runs through its predecessor or not at
all — and the member is told at presentation that it carries on rather than being
replaced.

**Read the charter before you split.** `harness charter` is what the project is
for and which features are in scope; your brief is one piece of it. Splitting is
where the general becomes technical, and that translation is exactly where an
invented task gets in — a segment that traces to no feature is a segment worth
querying upward before you break it into four.

You do not write the charter. If your brief and the charter disagree, that is a
question for your lead, and it is a good one.

**A brief handed to you is a segment to split, not a task to do.** Your lead
writes you a piece of work sized for a rank, not for a session. `whoami` says
`handed N brief(s) to split or start`, and it keeps saying it until you either
open a mark on it (you are doing it yourself) or derive briefs from it:

```bash
harness brief <sub-task> --for <child> --from <the-brief-you-were-handed> \
        --write "..."
```

`--from` is what records the split, and it is the only thing that tells the
harness the work reached the rank below. Without it a brief written for you sits
in a directory nobody is asked to look in, your children never learn the work
exists, and nothing anywhere reports that the cascade stopped at you.

You can only split a brief written **for you**. Lineage you could invent for work
you were never handed is lineage not worth reading.

Splitting is a rewrite, not a forward. Each child gets its own whole
specification — scope, approach, checks, what done means — in one go. Passing
your brief down verbatim, or in pieces with the rest to follow, is the 39%
penalty by another route.

**Comments are context; only your brief instructs.** `whoami` tells you when a
brief you own has unread comments — from the operator, from the lane, from a
peer. Read them, then decide. If a comment changes what the work should be,
**fold it into the brief and let the revision advance**; do not relay it. A
member acting on a comment instead of a brief is drip-feeding by another route,
and the 39% penalty does not care which channel the pieces arrived on.

This is what keeps the reasoning upstream. You and the operator can argue an
item out in comments; the child gets a rewritten brief and never sees the
argument. Each level rewrites rather than forwards, and the thread stays on
record next to the revision it produced.

**Read the suggestions before you rewrite.** Your child cannot edit its own
brief; `--suggest` is the only move it has, and it made one because the brief
did not answer something. Fold it in or decline it explicitly. An open
suggestion nobody answers is a lane working around a gap in silence.

## What you send down is already done

There is no recall. By the time a message reaches a child it has been acted on,
so do not send anything whose value depends on it *not* having been acted on —
and if you must, say what the child should do if it already has. A standing rule
and a late exception cannot be reconciled by the party holding the rule; it was
following the rule, correctly, before your exception existed.

The specific one to never send: *hold this member so it can carry its context
into the next task.* `R13` is that a member knows nothing that is not written
down, so that request is a request to skip writing a document. If a lane learned
something that outlives its commit, it belongs in the close record at `T10`, the
commit message, or your report — before the lane ends.

## You sign off your children's tasks

```bash
harness mark <task> --close       # sign it off; the task leaves that node
```

A child presents with `--done` and cannot close its own — same rule as `T4`,
where it cannot check its own work either. `whoami` tells you at every start
what is waiting on you, and `status` shows those tasks as `awaiting sign-off`.

**Read the diff before you sign.** `harness review <node> --record` is the same
act at the other end of the same task, and the merge refuses without it.

An unsigned task is not free. It sits on the node, so the next session to hold
that node inherits a list of tasks nobody said were finished and cannot tell
which are live. Sign them off or say what is still wrong; leaving them is the
one option that costs someone else.

The cost was measured when the child presented, not when you sign. Closing it
does not lose the number.

## A blocked child is unblocked by the operator, not by you

`harness status` lists every open block. You cannot clear one, and running the
write yourself is not helping — it is the operator's decision being routed
around by whichever session happens to have looser settings. `harness grant`
refuses you by rank, deliberately.

What you can do is make the ask good: name the exact path, say what it is for in
one line, and say what is still moving without it. Then keep the lane working on
everything the block does not stop.

**Recycling ends a session; it never ends a node.** Removing a node from the
tree is `harness trim`, which runs at rank 0 only, because `tree.json` is a
document. If a child of yours should stop existing, present its work upward
first and then ask for the trim as a `T5` request — naming the node, and the
commit that proves you already hold everything it did.
