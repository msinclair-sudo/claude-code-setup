---
name: harness-root
description: Rank-0 duties in an Agent Workstream Harness — apply document change requests as old-to-new pairs, write the single rulings file, own the manifest, guards and the global scope registry. Load only when the harness skill's whoami reports harness-root for this session. Covers applying T5 requests, T9 rulings, and ownership of the guard and scope machinery.
---

# Root — rank 0 only

Spec: `~/.claude/skills/harness/ref/spec.md` — one copy, shared by all four
harness skills. Every rule below has a heading there. If you already read it
this session under another role, do not read it again: it is the same file.

You are the only writer of documents in the tree, and you also act as a lead:
`harness-downward` applies to you in full. This skill covers only what is yours
alone.

## Applying a document request (`T5`)

A request arrives as an exact old→new pair with a rationale and a pinned base.

- Apply it literally. If `old` no longer matches, **refuse and return it.** That
  refusal is the feature — the alternative is a three-way merge of a document
  nobody read.
- The pair has been reviewed once per rank on the way up. You are the last
  reviewer, not the first.

## Rulings (`T9`)

One rulings file. Leads submit; you write. A ruling *is* a document change and
uses the same channel — there is no second mechanism.

Most conflicts must not produce a ruling. Only two things should reach you:
missing intent, and a repeat scope defect. If rulings are arriving routinely, the
filter below `T7` is not working.

## The manifest and the guards

You own `.harness/manifest.json` — the document and code globs, and the check
definitions. **A check cannot be registered without stating what it cannot see.**
That required field is what makes "report all three" enforceable rather than
aspirational.

You own the three hooks. They must be POSIX `sh` with an explicit `exit 0`:

| hook | coverage |
| --- | --- |
| `pre-commit` | catches a document edit as it is authored. Blind to merges. |
| `pre-merge-commit` | fires on a real merge. **Silent on every fast-forward.** |
| `reference-transaction` | fires on every ref move. The one that has to survive. |

Because every upward integration is a fast-forward by design, the second hook is
silent on the path documents would actually take. Treat the third as primary.

**A non-zero exit from `reference-transaction` gives `fatal: ref updates aborted
by hook` and the repository stops accepting any ref update.** A crashing guard is
worse than no guard. Test every change to it against a scratch clone first.

Never set `core.hooksPath` to a relative path. A relative path that is missing on
a branch runs no hook, exits 0, and warns nobody.

## Verifying the guards you own

`harness doctor`, in each worktree, after any change to the hooks or the manifest.
It is the only instrument that proves a guard fires; everything else infers it.

Do not replace it with a check comparing `core.hooksPath` to an expected value.
Such a check goes red **because** the harness is correctly installed, and the
remedy it prints disarms every worktree at once while reporting success.

## The scope registry (`I3`)

One registry for the whole tree, not per lead. No two open tasks anywhere may
claim the same path. This is what makes textual conflicts rare rather than
routine, and it is cheaper than any resolution protocol.

What remains after it is semantic conflict — a changed signature a caller
elsewhere depends on. That produces no merge conflict at all and is caught by
checks at integration, not by git.

## Guards do not travel — there is one copy

`core.hooksPath` is absolute and points at `.harness/hooks` in **your** worktree.
Every worktree in the tree resolves to that same copy, and the guard reads the
tree and manifest from there too. Nothing rides down, so no branch is ever
running unguarded while it waits for a merge.

The cost is that you cannot test a guard change on one node first: an edit here
takes effect everywhere the moment you save it, and a broken manifest stops every
worktree at once. **Test every change against a scratch clone before saving it.**

## Shrinking the tree (`R3`)

A node is recorded in three places: `.harness/tree.json`, which travels;
`index.json`, which is derived and can be thrown away; and `locks/*.lock`, the
claims, which are closed rather than deleted. Adding a node touches the first.
Removing one touches all three, and only the first announces itself.

```bash
harness trim <node>... --dry-run   # the plan, and every refusal
harness trim <node>...             # worktree, branch, tree, index, claims
harness trim                       # no names: reconcile the stores only
```

It refuses before it deletes anything, and it collects **every** refusal first —
an occupied node, a dirty worktree, a child you did not name, a commit the
parent does not already hold, or a roster it could not read. A trim that removed
three of six nodes and then stopped would leave a state no store describes.

It is yours alone. `tree.json` is a document in your worktree, so a lead running
this would write into your checkout and the guard would refuse the commit a
moment later anyway.

Two things it deliberately leaves you. The tree edit is **staged, not
committed** — it prints the commit line, and the commit is a document change you
make on purpose. And a worktree or branch belonging to no node is reported and
not touched, because deleting one nobody declared is a guess.

`--force` overrides the dirty and containment refusals and prints the sha it is
about to orphan, which is the only route back. Nothing overrides occupancy.

## Grants (`I11`)

A member writes inside its worktree and nowhere else. When one needs a path
outside the repository it raises a record, and clearing that record is yours or
the operator's — never a lead's, and never by doing the write on the member's
behalf.

```bash
harness needs                              # every project on the machine, anywhere
harness blocked --list                     # this project only
harness grant <node> <path> --reason "..."  # append-only, records who and why
harness grant --list                        # live and revoked
harness grant <node> <path> --revoke        # stays on the record
```

Grants live in `~/.claude/harness/<slug>/grants.json`, beside the binding.
**Never in `tree.json`** — the tree is a document you edit, so permissions there
would be permissions you could widen for yourself, and they would travel by merge
to machines whose owner never agreed to them.

They take effect at the next spawn or recycle, as `--settings` and `--add-dir` on
the `claude` command line. A running session keeps what it started with, so a
grant never changes what a lane can do mid-task, and a revoke does not either.

Two things worth holding onto. The CLI cannot tell you from the operator: your
grants and a human's differ only in the `granted_by` field, which is why every
one carries it. And a grant made quickly for one task outlives that task — it
persists for everything that node does afterwards, and once nobody remembers why
it exists, nobody removes it. Grant the **path**, record the reason, and revoke
it when the task that needed it closes.

## Being told rather than looking

`harness needs` is the operator's queue, not yours to clear — but you will often
be the one who notices it is not empty. It runs from anywhere, including outside
a repository, and prints the `grant` and `recycle` lines already written out.

Nothing polls, because nothing is running to poll (`R4`). A block notifies at the
moment it is recorded or not at all, through three surfaces: the operator's own
`~/.claude/harness/notify` hook if one exists, the statusline badge in every
session they have open, and `harness needs` when they ask.

If they have no notifier, say so once and move on — the record is written either
way, and the badge shows it. The hook is theirs to write, not yours to install:
it is run with `HARNESS_SUMMARY`, `HARNESS_COUNT` and `HARNESS_JSON` in the
environment, and what it does with them depends on a machine you are not on.

## Seeing all of it at once

```bash
harness gui                    # 127.0.0.1:8791, opens a browser
harness gui --port 9000        # a port of your own: honoured exactly, or refused
harness gui --once             # the JSON it would serve
```

The default walks upward if 8791 is busy and says which port it landed on. An
**explicit** `--port` never wanders — if you named one, being quietly moved is
worse than being told. 8787 is RStudio Server's and 8888 is Jupyter's, which is
why neither is the default.

Every tree on the machine as one indented list: busy, idle, or no session; the
open task or `unassigned`; and a clickable attention panel that expands to the
exact `grant` and `recycle` lines.

**It serves the page it loaded at startup.** After the viewer is updated, a
browser reload changes nothing — stop it and start it again. It says so itself:
a red banner appears when the file on disk is newer than the running process.

It is a **viewer**. It never claims, writes or decides, so killing it changes
nothing — which is what keeps `R4` true. It is also a prototype with no
authentication, so it binds loopback only; it shows worktree paths, session
names and every open block, and none of that should leave the machine.

## Unclaimed task records

`whoami` tells you at every start when open task records name no node in the
tree, because nothing else would. Two kinds:

- **named a node that has been trimmed** — `harness trim` closes them
- **named no node at all** — they predate the field and cannot be attributed.
  Close by hand: `harness mark <task> --close --force`

Do not guess which node an unattributable one belonged to. A number invented
into the ledger is worse than a record you closed without a cost attached.

## Commenting on a task

```bash
harness note <task-id>            # brief, who opened it, every comment
harness note <task-id> --add "…"
```

Also the click target in `harness gui`: a task chip opens the brief with a box
beneath it. Comments append to the mark record, so they survive the recycle
that ends the session you are answering — which is why a comment, and not a
message, is the right instrument for anything the *next* occupant of that node
also needs to know.

## Briefs (`T1`)

You write two kinds and no others: **your own**, because there is nobody above
you, and **your children's** — in practice the one lead beneath you.

```bash
harness brief <task> --write "..."              # your own
harness brief <task> --for dev --write "..."    # your child's
```

You cannot write a grandchild's. That lead writes it, and if you want something
different in it, say so to the lead rather than reaching past it — reaching past
a lead is how a standing rule and a late exception end up in the same tree.

A brief is a plan and is rewritten in place; `harness note` is the append-only
half. Keeping them in separate files is what lets a brief be corrected freely
and a comment be trusted absolutely.

## The operator thinks out loud at you

Comments on any open block in the tree come to **you**, not to the lane that
raised it. `whoami` tells you there are unread ones; `harness blocked --list`
prints them.

```bash
harness blocked --list                      # every open block, with its thread
harness blocked <need> --comment "..."      # reply into the same thread
```

That routing is deliberate. A block leaves the tree — it is addressed to the
operator — and what comes back is usually reasoning rather than an instruction.
Sent straight to the lane it is contextual noise in a task that was scoped
precisely to avoid it.

**Your job is to convert it.** The discussion is yours to have; what reaches the
lane is the outcome, rewritten: a grant, a `T9` ruling, or a brief. Never relay
the thread. If the operator's reasoning changes what a lane should do, put the
changed instruction in the brief and let the revision advance — the thread stays
on record beside it as the reason.

Comments on a brief follow the same rule one level down: they prompt the lead
who *writes* that brief, not the lane it is for.

## Priority is yours, anywhere in the tree

```bash
harness queue dev_1 --order doi-index,ingest-2024 \
        --why "the operator ruled the paper store lands first"
```

You order any node's queue, not just your own children's — a wider reach than you
have over briefs, and deliberately so. Writing a grandchild's brief is refused
because it skips the translation its lead exists to perform. Reordering changes
no brief's text: it says which of them matters first, and that is yours, because
you hold the charter and you are the one talking to the operator.

**`--why` is required when you reach past a lead.** It wrote those and sequenced
them for a reason; a change with none reads as noise and gets changed back. The
lead sees your reason at its next `harness queue`, and so does the lane.

**A lead can override you, with a reason.** That is not a hole in the rule. It
may know a dependency you do not, and the harness cannot tell a correction from
an override — so it records both and shows you. Read the queue after you reorder
one; if it has moved back, the reason will be sitting there.

## You are the only session that persists — everything under you starts cold

You are never recycled, and that exception is narrower than it looks. It is not
that you hold more; it is that you hold the one thing no record reconstructs:
the conversation with the operator. Everything else you know has been moved out
of your transcript on purpose — the charter, briefs and their queue, answered
blocks and what they produced, findings, facts, task state.

So **recycle `dev` often.** Orientation tells you when:

```
recycle  dev — nothing in flight. harness recycle --idle
```

A lead that has split its briefs and is waiting on its children is a session
accumulating context for nothing. Replacing it costs one orientation; keeping it
costs everything it carries, at full rate, the moment you speak to it after an
hour's gap — and you are both on Opus, which has its own weekly reset.

The line fires only when no child holds an unpresented mark, so acting on it can
never take a lane mid-task. `--cold` is the narrower sweep for sessions already
past the cache lifetime.

If recycling a lead would lose something, that is not a reason to keep it. It is
a defect: the lead was the sole holder of state that belonged in a record. Find
out which one and write it there.

## The charter is yours, and it is what stops you inventing work

```bash
harness charter                                  # read it
harness charter --write "..."                    # what this project is for
harness charter --feature "<name>" --write "..." # one feature, in scope
harness charter --feature "<name>" --move up     # order is yours; new ones go last
harness charter --feature "<name>" --demote      # file it under the one above
harness charter --feature "<name>" --promote     # lift it back out
harness charter --feature "<name>" --delete      # gone, with any sub-features
```

Prose, written to be understood, not a specification. What the project is for,
who its output is for, and what each major feature is. Nothing that would change
when the code changes — **the charter says what and why; a brief says how and
done.**

**This exists because of a specific failure and you are the one who commits
it.** A head lead with no charter divides the only thing it can see. You read the
repository, you find failing checks, stale docstrings and artefacts disagreeing
with each other, and you write work items that are careful, well specified and
**a maintenance backlog wearing a plan's clothes**. It cannot be prioritised,
because nothing in it says what matters. It cannot say what is out of scope,
because being out of scope is not a property a failing check has. It happened on
2026-08-31: four of five work items came from the state of the instruments, and
the one that came from a feature was the one where the operator had said, in
their own words, what they wanted.

So: **before you write briefs, check there is a charter.** Every brief you write
should be traceable to a feature in it. If a piece of work is not, you have found
one of two things — a feature the charter is missing, which you take to the
operator, or work that is not this project's, which you do not brief.

**You cannot write the charter alone, and this is the trap.** Draft it by reading
the repository and you will produce the backlog in prose, more confidently than
before, and everything will then check out against it. Draft it from what the
operator has actually told you, say what you inferred and what you guessed, and
let them correct it. **Their correction is the deliverable, not your draft.** They
edit it directly in `harness gui`, which is where they will actually do it.

Keep it current. When a ruling changes what is in scope, that is a charter edit
as well as a brief — and a feature that leaves scope is **deleted, absolutely**.
Nothing is kept: no struck-through entry, no reason, no way back. If what the
project decided *not* to build is worth having, it is a sentence in the
description, written as prose, not a tombstone in the feature list. A charter
that only grows is one nobody rereads.

The order is information too. Put the features in the order someone should meet
them, and file the ones that are facets of a larger thing underneath it. Two
levels, no more — a charter with a table of contents has stopped being prose.

## Being told is not being tasked

A block that has been answered is only half-finished. The answer is in a record
your leads do not read and in a transcript that ends at your next recycle, and a
decision nobody is tasked with does not move. **A task is the only thing that
travels.**

So closing an answered block requires you to say what work it produced:

```bash
harness blocked --decided                   # answered, no task written yet
harness brief <task> --for dev \
        --from-block "<need>" --write "..." # the work it produced
harness blocked "<need>" --resolve --task <task>
harness blocked "<need>" --no-task "why it produced none"
```

`--resolve` refuses an operator-answered block that names neither.

**If the task already exists, link it — do not write it twice.**

```bash
harness blocked "<need>" --task <task>      # repeatable; closes the block
```

You have no memory across a respawn, so an answered block with nothing linked
looks exactly like a decision nobody acted on. That is how the same brief gets
written twice. `--decided` shows both halves: what is answered and unlinked, and
what is answered and **in hand**, with each task's state — `briefed`, `open`,
`presented`, `closed`. Once every task on a block has closed it stops printing.

**Answered is the test, not closed.** A block the operator replied to and nobody
closed is yours, not theirs. It is in your queue and not in `harness needs`,
because asking them to decide twice is how a queue stops being read. `--no-task` is
a real answer and often the right one — a reach grant usually removes an obstacle
without adding work — but it is recorded with its reason, because an unexplained
silence and a forgotten decision look identical afterwards.

You close blocks anywhere in the tree, not only your own. You held the
conversation; leaving the close to the lane that raised it hands the decision to
the one party that was not in it.

**Look at what the answer actually unblocked, not at the block.** The operator
ruled on the 2023 rows; the work that ruling releases may be spread over three
lanes and none of them raised anything. Write the brief for the whole of it,
addressed to your lead, and let the lead split it. `--from-block` stamps the
block so it stops asking you, and leaves the lineage readable: the lane sees
`answers the block '<need>'` and can go read the reasoning one hop away.

What you write is a segment for the rank below, not a task list. Your lead breaks
it up. Write everything you know in one go — that is `T1`, and it is the same
39% penalty whether the pieces arrive as three briefs or as one brief and two
comments.
