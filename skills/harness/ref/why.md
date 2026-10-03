# Why each harness rule exists

Read on demand, when a skill's rule needs its reason. One section per skill.

---

## Why the harness skill's rules exist

### Enrolment takes two keys

`.harness/tree.json` says the project defines a role tree; `binding.json` says this machine has joined it. Both are deliberate, so one alone never enrols a session by accident.

### Position is derived, not declared

The CLI reads position from `git rev-parse`. You cannot claim a role, only stand in one. It calls `claude agents --json` itself, which lists every live session including this one, so it learns its own name and every peer's liveness without being told.

### Work after claiming

Spawned sessions used to claim their node and stop. The launch prompt and the skill now both say to work the queue until blocked on the lead or the operator.

### Prose on stdin

Written in double quotes, backticks and `$()` are expanded by the shell before the CLI runs. The argument just arrives shorter, the command prints success, and what is stored is grammatical and wrong. It has turned an instruction into one that named nothing, and a defect report into one with no location. The quoted heredoc delimiter is what makes the text literal. `--write "$(cat file)"` strips every trailing newline, so a round trip never matches; `-` removes only the one the delimiter adds.

### Exit 2 versus exit 6

`C1`–`C5` assert the undocumented Claude state the harness reads. A failure means refuse, not degrade: a mis-identified session is how two sessions end up holding one node. `doctor` failures used to share exit 2, which told sessions not to work around them and read as a ban on `harness scaffold`, the one fix. They now exit 6. `scaffold` rewrites the hooks every node runs, so only rank 0 may run it.

### The auto-mode classifier

A classifier block means no harness process started: no exit code, no output, nothing decided. It keys on command text and is non-deterministic, so the same call may pass twice and fail the third time. The fix is a Bash permission rule (`permissions.example.json` carries the harness ones). Asking another session to run a denied command launders a decision the operator made about you.

### Liveness and `--force`

A roster row outlives its process, and a session id and pid are reissued on resume, so `claim` checks the lock's pid on this host, then a live session file for the same id, then a live roster row. Exited sessions linger in `claude agents --json` with a null pid; they no longer count as occupancy. Absence from a local roster says nothing about another host, so a lock claimed elsewhere still needs `--force`. Never pass a hand-edited roster to `--roster`: that lets a session choose what its own guard sees.

### Model and effort per node

Defaults: `opus[1m]` at `high` for rank 0 and `medium` for a lead, because context follows the view and a lead is where reports, conflicts and documents accumulate. A leaf gets plain `opus` at `medium`: coding is where the effort curve is steep, and a leaf holds one task and is then recycled.

### Subagents hold nothing

A subagent has no session id, no lock and no row in the session table, so it cannot hold a node, a claim or a transaction.

### Ledger rows are closed, not deleted

An ancestor resolving a deep conflict (`T8`) reads closed rows.

### Facts need `--from`

A value with no way to reproduce it is a rumour with a figure attached: the reader either trusts it or pays the whole derivation again. With the command recorded, checking costs one `--recheck`. Paraphrased values ("about two") can never match a recheck. Two lanes once ran the same check honestly and got 1 and 9, because an install directory `git status` cannot see changed what the check counted; that is why another worktree's figure is a different measurement. A measurement tells nobody what to do; if it should change what someone does, that is a brief, and only a lead writes one.

### The charter is optional

A complete brief is enough to work from, and loading the project's purpose into a scoped task hands back context the task was scoped to exclude. It exists so the answer no longer depends on the lead being awake. If it is wrong, raise a `--suggest` on your brief or tell your lead.

---

## Why — harness-root rules

The reasons behind the rules in `harness-root/SKILL.md`, under the same headings. Read only when you need the reason.

### The charter

A head lead with no charter divides the only thing it can see. It reads the repository, finds failing checks, stale docstrings and artefacts that disagree, and writes careful work items that are really a maintenance backlog dressed as a plan. That backlog can't be prioritised, because nothing in it says what matters, and it can't say what is out of scope, because being out of scope is not a property a failing check has. On 2026-08-31, four of five work items came from the state of the instruments; the one that came from a feature was the one where the operator had said what they wanted. A charter drafted from the repository reproduces the backlog in prose, more confidently, and everything then checks out against it. The operator's correction is the deliverable, not your draft. Deleted features leave no tombstone because a charter that only grows is one nobody rereads; what was decided *not* to build belongs in the description as prose. Two levels at most: a charter with a table of contents has stopped being prose.

### Briefs (`T1`)

Reaching past a lead into a grandchild's brief skips the translation the lead exists to perform, and is how a standing rule and a late exception end up in the same tree. Briefs and notes live in separate files so a brief can be corrected freely and a comment trusted absolutely. Writing everything at once matters because splitting it carries the same 39% penalty whether the pieces arrive as three briefs or one brief and two comments.

### Approving briefs

Approval was once refused to every session including rank 0, because a lead approving its own brief is the gate approving itself. The cost was a tree that stopped: `harness needs` named approvals nobody present could move, and the subtree waited on an absent human. Since 2026-09-07 rank 0 may act. The CLI cannot tell you from the operator except in the record, so `self_approved` is shown on the line for later readers to find decisions nothing outside this node saw.

### Priority

Reordering changes no brief's text; it says which matters first, and that belongs to the node that holds the charter and talks to the operator. That is why your reach over queues is wider than over briefs. A reorder with no `--why` reads as noise and gets changed back. A lead may know a dependency you don't; the harness can't tell a correction from an override, so it records both and shows you.

### Asking the operator for a ruling (`T17`)

What is waiting on the answer is the one thing the operator cannot work out from the question, and it is how your question is ordered against everything else asking for them; hence `--turns` is the CLI's only required prose argument. A shortlist of options costs them a word where an open question costs a paragraph. A block renders to the operator as a grant, so a question filed as a block asks them to answer a different question. Before `decision` existed, rank 0 wrote its questions into its own away-summary, where nobody read them. Self-answering is allowed because a queue that waits on an absent operator is the overnight stall.

### Blocks: comments and closing them

A block leaves the tree; what comes back is usually reasoning, not an instruction. Sent straight to the lane, it is contextual noise in a task scoped to avoid exactly that. An answered block sits in a record leads don't read and a transcript that ends at your next recycle, and a decision nobody is tasked with does not move: a task is the only thing that travels. With no memory across a respawn, an answered block with nothing linked looks like a decision nobody acted on, which is how the same brief gets written twice. Answered blocks stay out of `harness needs` because asking the operator to decide twice is how a queue stops being read. `--no-task` is often right (a reach grant usually removes an obstacle without adding work), but it carries a reason because an unexplained silence and a forgotten decision look identical afterwards. You close blocks anywhere because you held the conversation; leaving the close to the lane hands the decision to the one party not in it. The work a ruling releases may span lanes that raised nothing, which is why you brief the whole of it to the lead and let `--from-block` leave the lineage readable (`answers the block '<need>'`).

### Applying a document request (`T5`)

Refusing a stale `old` is the feature: the alternative is a three-way merge of a document nobody read. The pair has been reviewed once per rank on the way up; you are the last reviewer, not the first.

### Rulings (`T9`) and the scope registry (`I3`)

A ruling is a document change, so it uses the same channel; there is no second mechanism. A single tree-wide scope registry makes textual conflicts rare rather than routine and is cheaper than any resolution protocol. What remains is semantic conflict, which produces no merge conflict and is caught by checks at integration, not by git.

### The manifest and the guards

The required "what it cannot see" field is what makes "report all three" enforceable. Every upward integration is a fast-forward by design, so `pre-merge-commit` is silent on the path documents actually take; `reference-transaction` is primary. A crashing guard is worse than no guard: a non-zero exit stops every ref update. A relative `core.hooksPath` missing on a branch runs no hook, exits 0 and warns nobody. A check comparing `core.hooksPath` to an expected value goes red because the harness is correctly installed, and its printed remedy disarms every worktree while reporting success. Guards don't travel: one absolute copy means no branch runs unguarded while waiting for a merge, at the cost that you can't trial a change on one node and a broken manifest stops every worktree at once.

`harness doctor` is the only thing that demands a real refusal and a real allow, and only for the document guard. A tree once held a `reference-transaction` calling a `_guard` without `--gate`; every functional arm passed while the gate permitted everything, which is why the drift arm exists. `scaffold` refuses below rank 0 because the absolute `core.hooksPath` means a scaffold from any worktree rewrites the hooks every node runs, instantly, with no commit or review. Uncommitted hooks are the worse resting state: every node runs what `HEAD` doesn't contain, and one `git reset` anywhere silently disarms the tree. Scaffold's change to `.claude/settings.json` alters how every session terminates.

### Grants (`I11`)

Grants are never in `tree.json` because the tree is a document you edit: permissions there would be ones you could widen for yourself, and they would travel by merge to machines whose owner never agreed. They apply only at spawn or recycle (as `--settings` and `--add-dir`), so a grant or revoke never changes a lane mid-task. Your grants and a human's differ only in `granted_by`. A grant made for one task persists for everything that node does afterwards, and once nobody remembers why it exists nobody removes it. Nothing polls because nothing is running to poll (`R4`), so notification happens at record time or not at all. The notify hook is the operator's because what it does depends on a machine you are not on.

### Shrinking the tree (`R3`)

A node lives in three stores: `tree.json` (travels), `index.json` (derived), and `locks/*.lock` (claims, closed rather than deleted). Adding touches one; removing touches all three, and only the first announces itself. A trim that removed three of six nodes and stopped would leave a state no store describes, hence collect-all-refusals first. It is yours because `tree.json` is a document in your worktree. The tree edit is staged so the commit is a deliberate document change. Undeclared worktrees are left because deleting one nobody declared is a guess. `--force` prints the orphaned sha because it is the only route back. Unattributable task records are closed rather than assigned because a number invented into the ledger is worse than a record closed without a cost.

### Recycling the lead

You persist only because you hold the one thing no record reconstructs: the conversation with the operator. Everything else is in records on purpose. A lead waiting on its children accumulates context for nothing; replacing it costs one orientation, keeping it costs everything it carries at full rate the moment you speak after an hour's gap, on Opus with its own weekly reset.

### Seeing it all

`gui` defaults to 8791 because 8787 is RStudio Server's and 8888 is Jupyter's. An explicit `--port` never wanders because being quietly moved is worse than being told. It serves the page loaded at startup, so a browser reload after an update changes nothing. It is a viewer so killing it changes nothing (`R4`), and it binds loopback because it has no authentication and shows paths, session names and every open block. Comments append to the mark record, so they survive the recycle that ends the session you are answering.

---

## Why — harness-downward

The reasons behind the rules in `harness-downward/SKILL.md`, under the same headings. Read only when you need one.

### T1 — issuing a task: the brief

Intent is required because a lead later asked why a conflict happened has nothing but a guess without it, and a confident invented cause is worse than none. A plan goes down whole because the same information delivered in pieces cost a measured 39% across 15 models, with the penalty already present at two pieces; a single follow-up detail is the failure.

`mark` and `spawn` gate on a brief because `spawn` used to warn and start the node in the same output, and a warning read after launch is a caption. `spawn` is scoped to your own children because bare `spawn` once took every node with a worktree, and a lead started a member under a sibling lead with nothing briefed. The operator, not being a node, still drives the whole tree.

A brief is a plan, not provenance: a working document that behaves like a record is one nobody dares correct. The naming refusals exist because writing `properties-hide-empty` onto `properties_hide_empty` once took the parent's text, moved the brief to the child, and recorded it as splitting itself, destroying the brief. `--history` exists because otherwise the only copy is in a session one recycle from gone.

### Bands

The band used to be entered at `harness mark`, which the member runs, so the XL refusal landed on the one party that may not split the task and could dissolve it by typing `L`. Resent context is excluded because counting it blows every band by the second turn and measures how long the session talked, not how big the job was. The member's disagreeing band is the earliest signal of a mis-sized brief.

Mark at the start because a T1 with no mark cannot produce a measured actual at T10; a guess recorded as a measurement is worse than no figure. A mid-task recycle starts a new transcript and the mark no longer subtracts (`R13` against `I10`).

### Facts, not pasted figures

A number typed into a brief is true the day it is written and silently wrong afterwards. Refusing an unrecorded fact keeps a citation from being a promise.

### Splitting a brief handed to you

Without `--from` a brief written for you sits where nobody is asked to look, and nothing reports that the cascade stopped at you. Lineage you could invent for work never handed to you would not be worth reading. Splitting is where the general becomes technical, which is where invented tasks get in; hence the charter check.

You close your own split segments because "nobody closes their own" is about checking your own work, and you did none: you split it and signed off each part. An unclosed segment sits on your card looking like ignored work; one lead appeared to hold thirteen tasks when seven were real. An abandoned part blocks closure because "all parts settled" would otherwise be satisfied by work nobody finished.

### Withdrawing and parking

The things that choose what to run (queue, the recycle after `--close`, `spawn --dry-run`) are not readers, so SUPERSEDED in prose was offered and started without anything unusual printed. Supersede refuses under an open mark because withdrawing work beneath a session doing it throws that work away silently.

A mark from a dead session survives every recycle and is named as the work in front of each fresh session. `--done` and `--close` would both be false. Leaving it open puts a figure in the ledger no transcript measured.

### Comments and suggestions

A member acting on a comment rather than a brief is drip-feeding by another route, and the 39% penalty does not care which channel the pieces came through. Rewriting rather than forwarding keeps the argument upstream, on record next to the revision it produced. An unanswered suggestion is a lane working around a gap in silence.

### The queue

A member holding four unordered briefs has a choice, not a backlog, and choosing which task comes first is choosing its own work; it is also where "shall I start?" comes from. Rank 0 may reorder because ordering changes no brief's text and rank 0 holds the charter and the operator conversation. You may reverse it because you may know a dependency it does not, but silent reversal is refused.

Coupling keeps a session alive across a boundary the evidence says to reset at, so the reason must be real: context expensive to rebuild, not "both are about the UI".

### Focus

Focus exists so a lead working one thing is not pulled sideways by nags about everything else, while still seeing a one-line count of what it is setting aside.

### Orientation and your todo list

A lead learned it owed a sign-off, held a long exchange with its own lead about something else, and the debt was gone from its head long before it left the ledger. This happened repeatedly on a live tree. The todo list is the only structure in a session that survives that conversation. Signing off starts the child's next task, so a carried debt is a lane standing still.

Nags print only at orientation because printing them after every command made them noise. A lead with lanes holding open marks used to be reported idle and told to recycle, which was wrong: it is waiting. Ghost roster rows and ad hoc `/proc` checks were replaced by one liveness reading so that `claim`, `status` and the hooks agree.

### T11 — reviewing an approach

Models are unreliable at noticing they need to ask; one model in a published benchmark never asked at all. A forced restatement is the cheapest detector for a silent misunderstanding, and building your model of the subtree here is cheaper than reconstructing it during a conflict.

### T12 — answering

Age alone misleads: a child waiting three hours while working costs less than one that stopped forty minutes ago. Recycling a child that is waiting on you throws away the question with the session. If the answer did not arrive, it was put somewhere the child does not read; the brief is what it reads.

### I9 — you own the seams

Owning interfaces rather than implementations keeps your context at k interfaces, not k implementations.

### Reviewing — a gate

A member cannot verify its own work: a model revisiting its own output without an external check got worse in every configuration tested, and improved only with an oracle present. You are the oracle. The gate's first version tested only that a record file existed, so a member could write the record that unblocked its own integration; the record now names the reader and the guard checks it. Git checks out the fast-forward before the ref update it aborts, hence the reset.

The check report sits in the review because before it existed you integrated on the member's word that the suite was green. A blind spot prints beside a pass because the moment it matters is the moment you decide what a pass means.

Subagents cannot hold a node because they share your session id, pid and working directory. A workflow script would be a layer to maintain for no property you need.

### T4 — integrating

A fast-forward works only while the child is an ancestor of you. Integrating the first child moves you, so every sibling that caught up before presenting is now behind and unmergeable, needs a third catch-up `T2` forbids, and has nobody in its worktree to run one because it presented and released per `T10`. That deadlock is common; `integrate` walks through it. Occupancy is what `T2` protects. A dirty worktree has nobody to explain it. A clean catch-up carries the review because the child's side is unchanged and git wrote the merge mechanically; a conflicted one does not, because somebody decided something. A remote runs none of these guards, so a pushed branch is unintegrated work out of reach.

### Signing off

The gap between "signed off" and "started the next thing" used to be a command nobody ran, so `--close` recycles itself. The member has already stopped and released, so until you close, the work sits finished and invisible and the node empty. The rank above is told because nothing pushes and an idle lead runs no commands. An unsigned task leaves the next holder a list it cannot sort into live and dead. The cost was measured at presentation, so closing loses no number.

### T7 / T8 — mediating a conflict

The cause is the part only the assigner has. Asked "does this look right?", a member says yes; that rank gradient is why you ask for a claim. The absent member's tests stand in for a signature nobody present can give.

### T5 — relaying documents

Your review is why the chain exists. Two children asking for the same change should become one request for every ancestor.

### Recycling

A member holds nothing not written down, so after integration its context is transcript, not knowledge (`R13`). A persistent worker compounds its earlier mistakes, scale does not fix it, and clearing history does. A claimed node with no open task is capacity with no object, which gets spent on correspondence no transaction ends; recycling ends that thread by removing the counterparty.

Idle sessions cost nothing until spoken to; then every turn resends the whole conversation, and the subscription prompt cache lasts one hour. A node quiet three hours carrying 349k is re-processed in full at the next hello, and keeps its accumulated errors. Replacing it costs one orientation.

Leads are recycled too because what a lead once held alone (briefs, answered blocks, measurements) is now on record. Rank 0 is exempt because it holds the operator conversation, which no record reconstructs.

`--escalate` is not the default because the retry-cheap-then-escalate figures are an unreproduced vendor claim, and a published study found a longer first attempt beat selective recovery by 28% on accuracy and tokens together. `tree.json` is a document, so trim is rank 0's.

### Findings

A lead approving the brief it just wrote is the gate approving itself. Gating is safe because the lane that raised the finding carries on with its queue. The operator's queue is finite attention, so decline on the record; the next lead to notice the same thing gets your answer instead of silence. Rank 0 may approve on the operator's behalf since 2026-09-07.

### You are also somebody's child

The operator approves unrequested work before it starts; finishing requested work is not theirs, and routing it to them stalls the lane. An empty queue is reported to your own lead at its next orientation, and the operator could not answer without going through that lead anyway.

### Sending down and blocks

A standing rule and a late exception cannot be reconciled by the party holding the rule; it was following the rule correctly before the exception existed. Holding a member to carry context is a request to skip writing a document (`R13`). Running a blocked write yourself routes around the operator's decision via whichever session has looser settings.

---

## Why — harness-upward

The reasons behind the rules in `harness-upward/SKILL.md`, under the same headings. Read only when you need the reason.

### You do not ask whether to start

You already hold the authorisation, so the answer to "shall I do this?" is always yes, and asking costs a whole session. Worse, the node sits occupied and idle while your lead waits on work, which is exactly what the tree is built to avoid. Choosing which of your tasks to do first is choosing your own work, one notch smaller than setting your own task.

### The rhythm: catch up twice

Your lead can catch you up after you present because you have released and nobody is standing in the worktree. If you went back to fix your position while still holding it, your lead could not. Catch-up 1 is a real merge commit because you hold your own work, so it cannot be a fast-forward.

`harness doctor` demands a refusal rather than reading config: it stages content the document node never held in a throwaway index and requires the guard to reject it, then requires a document that arrived from the document node to pass. Repair is rank 0's because `core.hooksPath` points absolutely into the document node's checkout, so `harness scaffold` from any worktree rewrites the hooks every node executes the instant the files land, with no commit or review, and sessions mid-task never learn of it.

The comprehension check is not a proposal; your lead decided the approach at `T1`. It exists so a misreading surfaces before the diff.

### When catch-up 2 conflicts

You cannot know why the conflict exists; your lead holds the context of both sides. Re-running your checks under its proposal gives it evidence instead of agreement.

### `T12` questions and waiting

Confirming what the plan already says is information arriving in pieces, the cost the plan exists to avoid. But roughly half of specifications contain an ambiguity their author did not see, and work done on a guess is usually wrong, so real gaps are worth asking about. A question is a message, read late or not at all if your lead is mid-task; `harness waiting` is a record shown at the lead's next orientation, and the viewer draws the node as stopped rather than idle. A block is for things only the operator can widen; routing a lead's question there asks the operator to answer something they did not scope.

### You write inside your worktree, and nowhere else

A file outside the repository has no owner, no scope, no instrument that reds, no review at `T4` and no ref recording the change (`I3`). A block record reaches the operator's notifier and statusline, sits in `harness needs`, and survives your recycle, which a message would not. `--still-moving` lets the operator tell a stopped lane from a stopped step without reading your transcript. Comments on a block go to rank 0 because the operator's reasoning, delivered into a scoped task, is the noise the scope exists to keep out. Asking a looser session to do the write routes around the operator's decision instead of implementing it.

### Your brief, and pushing back on it

A node that sets its own task is what the tree exists to prevent, so `--write` refusing by rank is the design, not a permission problem. Acting on a comment directly turns a scoped task back into a drip-feed. A suggestion is recorded against the revision you read, so your lead sees exactly what you saw. Comments live on the record rather than in messages because a message dies with the session and you are recycled.

### What you noticed but must not act on

Acting on it is choosing your own task. Leaving it in your report loses it: the report is read once by one session. These observations are often the most expensive thing a session produced. `--how` separates a claim your lead can weigh from one it can only believe. The strongest findings come from use rather than review: a 2px floor once cut reachable documents from 20 to 6 while every check written for it stayed green.

### Write down what you measure, with the command

The expensive part is rarely running the command; it is working out which command answers the question. That is what a fact saves the next session, often you after a recycle. A figure with no command behind it must be taken on trust or redone.

### Checks

A suite that stops at the first failure reveals problems one per cycle, and each cycle costs a session. The blind spot is printed beside each result because a green suite is evidence only about what was tested. A timeout is reported as not run rather than failed so a slow check is not mistaken for a broken one.

### Commits

Without a `Task:` trailer, an ancestor holding a conflicted hunk has author names and no route into any ledger.

### `T4` present and `T10` release

You cannot check your own work, so the guard reads which node wrote the review record and refuses your own. A checked-out branch rejects a local push outright, and `pre-push` refuses a node branch to a remote.

Telling your lead is enforced because the failure kept happening. On 2026-09-08 a lead stopped at 11:21, its members presented at 11:25 and 11:44, and neither the Stop hook nor orientation could fire: the condition became true after the last moment anything could test it. Both sat unsigned for twenty-eight minutes until the operator intervened. You are mid-turn and your lead is not, so only you can make the record visible.

Waiting for sign-off holds a worktree and a context that costs its whole history the moment anyone speaks to you; sign-off may take hours. The operator approves unrequested work before it starts (`T16`) and has nothing to do with closing requested work; telling them to close it stalls your lane behind someone who cannot act. An unpresented task makes your node read as still working forever, which your lead reads as a node it must not recycle, so present even when the cost is unmeasurable.

Resent (cache reads) counts the whole conversation again every turn, so it grows with talk length rather than work; a task banded at 40k once measured 261.7M that way. NEW is the figure a band is set in. A missed band is the only thing that improves the next estimate, and it was your lead's estimate that missed, not your work.

### Documents

Documents are reviewed at every rank and applied only at rank 0; a refused `old` that no longer matches is correct behaviour.

### Late instructions, and being recycled

There is no recall down the tree. Reconstruction is expensive, rarely faithful, and usually rebuilds something `R13` says should have been written down. Recycling is why your window is small and your task short; it is not a demotion.
