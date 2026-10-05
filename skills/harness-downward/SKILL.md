---
name: harness-downward
description: Act toward your children in an Agent Workstream Harness — issue tasks, review approaches, answer questions, integrate by fast-forward, mediate conflicts, relay document requests upward. Load only when the harness skill's whoami reports harness-downward for this session. Covers T1, T4-integrate, T5-relay, T7, T8, T11-review and T12-answer.
---

# Downward — what you do toward your children

Spec, on demand only: `~/.claude/skills/harness/ref/spec.md`.

## `T1` — issuing a task: the brief

A task carries id, lane, path scope, intent, checks, band, and the seams you hold for it. Write all of it down at once, as one brief, before the child starts. Planning is your work; a stub followed by answers is the failure.

```bash
harness brief <task> --for <child> --write "..."   # write or rewrite (stdin: --write -)
harness brief <task>                               # read it back, with suggestions
harness brief <task> --resolve N                   # mark suggestion N addressed
harness brief <task> --history                     # last five revisions
```

- No scope, no task. No two open tasks anywhere in the tree may claim the same path (`I3`); overlap is refused at issue time.
- No intent, no task. `src/parse/**` is a scope; "widen the parser signature for encoding support" is an intent.
- `harness mark` refuses a task with no brief, with no override. `spawn` skips a node with nothing briefed and names the remedies: write the brief, or pass `--empty`. A lead with open tasks below it counts as briefed.
- `spawn` starts only your own children. Naming another lead's child is refused.
- You cannot write a grandchild's brief. Tell its lead what you want.
- `--after <task>` (repeatable; `--after none` clears) holds a brief until that task is signed off: `mark` refuses it, sign-off and `recycle` skip it, and the closing task names what it releases. Use it instead of "DEPENDS ON" prose. `harness brief <segment> --close-after <task>` holds a segment's close the same way: `mark --close` refuses and orientation stops offering it. A "closes only after X" note does not. `--not-before 00:05Z` (UTC; `none` clears) holds a start on a clock the same way. `--requires <ref>` makes "X must be in your tree" a check at `mark --done`, not at the lane's first commit, so a ruling landing while you hold your tree still for a check stops nobody.
- Rewriting a brief replaces it. The append-only channel is `harness note`.
- Pick a distinct name for each brief. Hyphens and underscores are the same character, so `a_b` and `a-b` are one record. Writing onto an existing brief prints `REPLACED`; moving one to another node needs `--force`. If you suspect an overwrite, check `--history` at once.

The spawned or recycled child claims its node and works its queue until blocked. It needs no start message.

## Bands (`I8`, `I10`)

| band | new tokens | shape |
| --- | --- | --- |
| S | ≤ 40k | one file, approach known |
| M | 40k – 120k | several files, some exploration |
| L | 120k – 300k | needs design, more than one seam |
| XL | > 300k | not a task; split it or escalate |

Set it on the brief: `harness brief <task> --for <node> --write - --band M`. `--band XL` is refused. A member may pass `--band` at `harness mark` to disagree; both letters are kept, and a disagreement means your estimate may be wrong. New tokens are up + down, excluding resent context. When estimate and measurement differ, the estimate was wrong.

Tell the child to run `harness mark <task-id>` first, or no measured actual exists at `T10`. Do not recycle mid-task to get a number; the mark stops subtracting across transcripts.

## Facts, not pasted figures

```bash
harness brief <task> --for <child> --fact <name> --write "..."
```

`--fact` resolves when the brief is read, showing current value, age and source command. Citing an unrecorded fact is refused; measuring it is a task.

## Splitting a brief handed to you

A brief written for you is a segment to split or start. `whoami` says `handed N brief(s) to split or start` until you open a mark on it or derive from it:

```bash
harness brief <sub-task> --for <child> --from <the-brief-you-were-handed> --write "..."
```

`--from` records the split; without it your children never learn the work exists. Give each part `--covers N,N` for the parent's numbered CHECKS it delivers: the split then names any clause no part covers, and the segment cannot read settled or close (without `--force`) while one is uncovered. You can only split a brief written for you. Moving an existing part to another segment needs `--move`, and prints both segments' settled counts. Each child gets a whole specification, rewritten, not your brief forwarded or sent in pieces. Read `harness charter` before splitting; a part that traces to no feature is worth querying upward. If brief and charter disagree, ask your lead.

A split segment leaves your queue but is not done. Orientation says when every part is signed off (`close   N segment(s) you split are finished`); then run `harness mark <segment> --close`. It refuses while any part is open, and an abandoned part blocks it too, so a segment with an abandoned part closes only with `--force`. Closing a segment recycles nothing.

## Withdrawing and parking

```bash
harness brief <task> --supersede "what overtook it" --by <replacing-task>
harness mark <task> --abandon "why it stopped, and what was left"
harness mark <task> --abandon "why" --requeue-after <task>   # defer it: back in the queue after <task>
```

Withdraw structurally, never by writing SUPERSEDED in the text: queue, recycle and spawn read state, not prose. A superseded brief stays readable, is never offered again, and `mark` refuses it. Supersede refuses while a mark is open.

Abandon a mark whose session died rather than marking it `--done` or `--close`. Check what was left first: 0 commits ahead and a clean worktree means abandon.

## Comments and suggestions

Comments are context; only the brief instructs. If a comment changes the work, fold it into the brief and let the revision advance; do not relay it. A child's `--suggest` is its only way to edit its brief: fold it in or decline it explicitly, then `--resolve N`.

## The queue

```bash
harness queue                       # every node: occupancy, then queue in order
harness queue dev_1                 # one node
harness queue dev_1 --order a,b,c --why "..."   # --why always required; unnamed keep their place behind
```

Order briefs deliberately; an unordered backlog makes the member choose its own work. Rank 0 may reorder any queue, with a reason shown in `harness queue`. You may change it back, but must say why.

Couple two tasks into one session only when shared context is the point:

```bash
harness brief <task> --for <child> --with <previous-task> --why "..." --write "..."
```

`--why` is required. A coupled task has no queue position of its own.

## Focus

```bash
harness focus <task|'glob*'>... [--why "..."]   # set
harness focus                        # show
harness focus --add <task> | --remove <task>
harness focus --clear
```

While set, nags about work outside it fold into one line. Queues are never filtered: a lead sees in-focus work first, and a lane's out-of-focus task is labelled, not hidden. A `--supersede --by` replacement inherits its predecessor's place.

## Orientation and your todo list

Nags print only at orientation (SessionStart `whoami`, UserPromptSubmit `hook-orient`). When one says a child presented or needs something, record it with `TaskCreate` before replying to anything else. An owed sign-off re-nags every ten minutes; everything else fires once.

Children: a lead whose lanes hold open marks is waiting, not idle. A quiet live child gets "message it to start (SendMessage)". A child with no running session gets `harness spawn <child>`. A child with an empty queue means you owe a brief. One `ListAgents` call shows which children are live and busy.

`harness status` decides liveness for you (lock pid on this host, then the session file, then a live roster row) and shows `gone (last write HH:MM)` for a dead holder. Ghost roster rows do not block `claim`. Do not check `/proc` or `claude stop` anything before claiming or spawning.

## `T11` — reviewing an approach

Before the first commit the child restates your plan in a few lines. Correct only a misreading; there is nothing to approve.

## `T12` — answering

Answer from scope, intent and seams. "I don't know, escalating" is correct; escalate under `T5`/`T9` rather than guess. Orientation lists children waiting on you (`harness waiting --list`), oldest first, with what is still moving. Answer the halted one before the one still working. Answer, then recycle, never the reverse. If a name stays on the list after you answered, the answer did not arrive; put it in the brief. A `stuck` line means a grandchild has waited over ten minutes on a child of yours that is busy (often on a long `harness check`, shown with its progress): message that child, or answer the grandchild yourself.

## `I9` — you own the seams

Interfaces between your children are yours; insides are theirs.

## Reviewing — a gate

```bash
harness review <node> --record   # read it and record the read
harness review --children        # every child: commits, diffstat, seams
harness review <node> --diff     # plus the full patch
```

The fast-forward is refused without a recorded review by you, from your own worktree, at the child's exact commit. Recording a review of your own node is refused. A new commit invalidates the record, except a clean catch-up by `harness integrate`, which carries it. If the ref update is refused, the branch is unmoved but the working tree is not: `git reset --hard HEAD`.

The review prints the child's `harness check` report at that commit and what each check cannot see. Absent reads as `NOT RUN`; a timed-out check reads `NOT RUN (timed out)`; a cut tail reads `… N earlier line(s) omitted`. With a baseline set, review shows each failing arm as new / gone / same: new blocks sign-off until explained, gone is news. When the known set really changes, re-record it from your node's report at HEAD: `harness check --set-baseline --why "..."`. Do not re-run a child's suite. `SEAM with <sibling>` means two children changed one file, yours to judge. `document check UNAVAILABLE` means unknown, not clean; find out why before merging. `harness hold <path> --why "..." [--until <task>]` stops every arm that reads a shared resource while a job holds it; they read `NOT RUN (held: …)`, and the report is not a pass.

Still worth a read-only subagent per child, in parallel: is it caught up (`git merge-base --is-ancestor <your-branch> <child-branch>`), and does the diff do what the brief said and stop where it stopped. Merge sequentially yourself. No workflow script, and never give a subagent a node: it shares your session id, pid and cwd.

## `T4` — integrating

```bash
harness integrate <child> --dry-run
harness integrate <child> ...          # one or several, in the order named
harness integrate --children           # every child that has presented
```

Runs in your worktree; underneath is `git merge --ff-only <child-branch>`. Use the command once you have two children to take, because the first fast-forward leaves the rest behind. It refuses an occupied child worktree (nothing overrides that), a dirty one, and work never presented or grown since. It catches the child up in its own worktree, then fast-forwards you. On conflict it aborts and hands back: that is `T7`/`T8`. It does not run checks.

`pre-merge-commit` never fires on this path; `reference-transaction` is the guard. `pre-push` refuses every node branch. Nobody pushes.

## Signing off

```bash
harness mark <task> --close        # sign off; recycles the child onto its next task
harness mark <task> --close --no-recycle
```

A child presents with `--done` and cannot close its own. `whoami` lists what waits on you; `status` shows `awaiting sign-off`. Review first. `--close` refuses on a dirty worktree or an open unpresented mark; with nothing queued, nothing starts. Sign off promptly: after twenty minutes the rank above you is told, and your `Stop` hook blocks once while a sign-off is owed.

## `T7` / `T8` — mediating a conflict

The child sends stages and authors from its catch-up. Authorship decides the transaction:

```bash
git log --merge --format='%(trailers:key=Task,valueonly)' -- FILE
```

| trailers name tasks | transaction | what you do |
| --- | --- | --- |
| you issued | `T7` | you hold both intents: state the cause, then propose |
| you did not issue | `T8` | read retained ledger rows; fetch down only if insufficient |

Two sibling leads conflict under `T8`. Then: state the cause before the resolution; have the child re-run its checks and state the effect (never ask "does this look right?"); run the absent member's checks yourself. No recorded intent means raise a ruling request. The same file conflicting twice under you is a scope defect: re-cut the scopes.

## `T5` — relaying documents

You write no documents. Read a child's batch with `harness pairs <task>` (it re-checks every count), and when two children touch one paragraph, submit one merged batch yourself.

## Recycling

```bash
harness recycle <node> --dry-run
harness recycle --children
harness recycle --idle          # children with no open task record
harness recycle --cold          # children past the cache lifetime
harness recycle <node> --escalate [--dry-run]   # one effort level up
harness recycle <node> --at-quiet               # a lead too big to keep: reset at its next quiet turn end
```

`status` shows each node's context (`ctx 442k`); a lead over its rank's threshold (300k unless `tree.json` sets `context_warn`) is named in your orientation. A busy lead is never idle, so `--at-quiet` is the reset for it: its own Stop hook first makes it write context-only state into the records, then replaces it at the next turn end with nothing owed. Leads launch with `--autocompact 350k` (`autocompact` in `tree.json`). A pending reset fires regardless at its ceiling (`--by`, default 400k for a lead; `--within`, default 60m). Until then hold non-urgent messages to that lead: each one restarts its quiet clock.

Recycle a child once its work has landed and after sign-off (`--close` does it for you), and replace a cold session rather than speaking to it. Leads too. Close the task record first or `--idle` reads the node as working. It refuses on a dirty worktree, unintegrated commits, a busy session, an unpresented mark and rank 0; take each refusal at face value. If a child asked only by message, answer before recycling.

`--escalate` is available, not the default; prefer raising the node's starting effort in `tree.json`. A second failure is a finding. Never `claude rm`: the worktree is the node. Removing a node is `harness trim`, rank 0 only; ask for it as a `T5` request naming the node and the commit proving you hold its work.

`orphan` in orientation means a child's session ended holding its task: `harness recycle <child>` resumes it (`--dry-run` shows the same). A requirement you send a child by message dies with its session; put it on the task too (`harness note <task> --add -`).

You are on the same rule. If being recycled would lose something, write it into a brief, fact or finding now. When rank 0 sweeps a finished unit, its briefs, marks and notes leave the board for the archive (`harness archive`); cite a `tmp/` path in a fact or finding if it must survive.

## Findings

`whoami` names findings handed up. Brief one or decline it:

```bash
harness brief <task> --for <child> --from-finding <name> --write "..."
harness finding <name> --drop "why it is not worth a session"
harness finding <name> --to <child>                  # hand it down a rank
harness finding <name> --ruled "<commit or doc ref>"  # answered by a document: closed, not declined
```

A brief from a finding is gated on approval, unless rank 0 handed the finding down (that was the approval): `mark` refuses it and `recycle` skips it until approved. You cannot approve it; rank 0 sees it at orientation. Decline what you would not spend a session on. `--needs-approval` puts the same gate on any brief.

## Asking the owner (`T17`)

Only for what the tree can't settle: intent, judgement, something only the owner can do, or risk they must accept. `harness ask <task> --kind intent|judgement|action|risk --question "..."` (the task needs a brief), then `SendMessage` the project's intermediary (`harness ask` names it) "new ask <id>" and carry on. It may question you; answer it. The ruling lands on the task's brief (`harness brief <task>`) and orientation tells you; a rejected or returned ask is said once. Lanes ask you, not the owner.

## You are also somebody's child

Your own task closes the same way: `harness mark <task> --done`, then your lead signs it off. Read your brief and act; it is an instruction, not a proposal (`T15`). An empty queue is your lead's to fix: say so in your report and stop. Do not ask the operator what to do next, and do not hand finished work to them.

## Sending down and blocks

There is no recall: a message has been acted on by the time it lands, so say what to do if it already was. Never ask to hold a member to carry context into its next task; what it learned goes in the `T10` close record, commit message or your report.

`harness status` lists open blocks. Only the operator clears one; `harness grant` refuses you by rank. Make the ask good (exact path, purpose in a line, what still moves) and keep the lane working around it.

Why each rule exists: `~/.claude/skills/harness/ref/why.md` — read only when you need the reason.
