# Agent Workstream Harness

> [!abstract] Note Role
> **Contains**: the roles, git nodes, transactions and invariants of the multi-agent git harness. Every transaction carries an index (`T*`) referenced from the edges of `tree.canvas` beside this file; every invariant carries an index (`I*`).
> **Cannot contain**: implementation code, installation steps, or per-project scope assignments.
> **Lives here only**: this file is the spec. There is no other copy; edit it in the setup repo.

## Roles

| Role | Writes | Owns | Reports to |
| --- | --- | --- | --- |
| **Top lead** (rank 0) | documents, rulings, manifest | `main` and `dev` | the user |
| **Lead** (rank *n*) | nothing directly — authors by request | one integration node | the lead one rank above |
| **Member** (leaf) | code, within an assigned scope | one worktree | its lead |

A lead is a member of the rank above it. Its own node is its contribution upward. Only rank 0 is special; every other rank is relative, and the structure repeats without change.

A lead's children may be members, leads, or both, in any mix. Breadth and depth are independent — see [[#I7 — Fan-out is a dial]].

## Git nodes

| Node | Held by | Checked out | Contents |
| --- | --- | --- | --- |
| `main` | top lead | always | documents, rulings, manifest, guards |
| `dev` | top lead | always | code integration, rank 0 |
| `dev/<lead>` | that lead | always | code integration, rank *n* |
| `w/<member>` | that member | always | one task's work |

Every node is checked out in exactly one worktree held by exactly one session.

---

## Transactions

### T1 — Task assignment

**Direction** downward, lead to member.
**Rule** A task record is a **plan**, complete at the moment it is issued. It carries an id, a lane, a path scope, an intent, the approach the lead has decided, an acceptance check set, the seams the lead is holding for this task, the definition of done, and an estimated cost band — see [[#I9 — The lead owns the seams]]. No scope, no task. No intent, no task — see [[#T7 — Conflict escalation]].
**Everything the lead knows goes down at once.** Measured: the same information delivered in pieces instead of up front costs 39% of performance across 15 models and roughly 200,000 conversations, and concatenating the pieces back into one instruction recovers 95.1% — so the loss is caused by incremental arrival, not by anything missing. Degradation appears at **two** pieces, which makes a single follow-up detail already the failure. Restating everything on later turns recovers only 15 to 20%. This is the largest measured lever in the design and no model or effort setting recovers it.
**The lead does the thinking.** Planning is the lead's work, not a negotiation held afterwards. A lead that issues a stub and answers questions has chosen the 39%.
**Enforcement** The scope is checked against the global registry ([[#I3 — Scopes are globally disjoint]]) before the task is issued. Overlap is refused at issue time.
**Fails when** Intent is recorded as a restatement of the scope. `src/parse/**` is a scope; *widen the parser signature for encoding support* is an intent.
**Applies at every rank.** A brief written for a lead is a segment that lead breaks up, under the same rule — see [[#T14 — A brief handed to a lead is split, not done]]. Work that arrives at rank 0 as an operator decision enters this path through [[#T13 — Unblocking is a task]].

**Every task traces to a charter feature** (owner, 2026-10-06: issues far outside scope meant agents were looping and making tasks out of nothing). `harness brief` requires `--feature` on a new brief once the charter has features; parts split `--from` a segment inherit it; rewrites keep it; `--feature` alone maps an existing brief (rank 0 or a lead). Open briefs without one are rank 0's re-reported `untraced:` debt until mapped or dropped. A task that serves no feature is out of scope, and `whoami` shows each node the feature its open task serves.

### T2 — Catch-up (merge down)

**Direction** downward, node into worktree.
**Performed by** the worktree's own session, never by the node — while the worktree is occupied. See below.
**Rule** Twice per task, and only twice: once after claiming, before the first commit; once immediately before presenting. Never between.
**Enforcement** `git merge <parent>`. This produces a real merge commit, because the worktree holds its own work.
**Fails when** Attempted from outside. Merging into a worktree that is in use aborts with `error: Your local changes to the following files would be overwritten by merge` when the incoming change touches dirty files, and succeeds silently when it does not — so it lands in the harmless cases and refuses in the colliding ones. A node therefore publishes `git rev-list --count <child>..<node>` and lets the recipient act at its own boundary.

**Two catch-ups is the MEMBER's count, and reading it as the worktree's count made the two rules here unsatisfiable together.** [[#T4 — Integration (fast-forward up)]] is `--ff-only`, which succeeds only while the child is an ancestor of the parent. Integrate the first child and the parent moves: every sibling that caught up before presenting — exactly as this rule instructs — is now behind, cannot be fast-forwarded, and needs a third catch-up this rule forbids. With *k* children at most one per round can satisfy both. It is not a rare race; it is what happens the second time a lead integrates anything.

**The prohibition protects the worktree, not the ref, so it ends where occupancy ends.** Everything in the *Fails when* line above is about a tree somebody is working in. A member that has presented and released is not working in it, the roster says so, and the merge that was dangerous a minute earlier is now ordinary. So: **the member catches up twice; a third catch-up into an unoccupied worktree belongs to the lead, and is part of T4 rather than an exception here.** `harness integrate` is that act and refuses an occupied worktree outright — occupancy is the one thing nothing overrides.

**Found three times in one night, and worked around in the wrong place first.** `harness recycle` was taught to release a presented child that had been left behind, which is correct — the member has genuinely finished — but it clears the *node* and leaves the *work* precisely where it was. Both are needed and they are different jobs.

### T3 — Guard verification

**Direction** internal to a worktree, after [[#T2 — Catch-up (merge down)]].
**Rule** A worktree proves it is guarded before it commits. Config that *looks*
right and hooks that *are* right are different claims.
**Enforcement** `harness doctor`. It demands the behaviour rather than reading
settings: it synthesises content the document node has never held, stages it in a
**throwaway index** so the real one is untouched, and requires the guard to refuse
it. It also requires the guard to *allow* a document that arrived from the
document node, so a guard that refuses everything fails too.

**It demands that behaviour of the document guard, and only that.** Every other hook is checked for presence, mode and agreement with the installed template — the weaker claim, and one that has to be stated wherever the stronger one is, or a reader takes "proves a guard fires" for all of them. The integration gate in particular has no watched refusal: a `reference-transaction` calling a `_guard` that does not implement `--gate` passed every functional arm while permitting every ref update, which is what the template-agreement arm was added to catch. Agreement is not demonstration; it is the nearest thing available without a second live tree to integrate into.

It checks the wiring as well — hooksPath set and absolute, all three hooks present
and executable, and their mode as **git records it**, since `core.fileMode=false`
on a Windows-backed mount lets a `chmod` succeed on disk while git stores 100644
and the hooks ship inert in every clone.

**Fails when** an instrument compares config to an expected string instead. Such a
check goes red when the harness is correctly installed and prints a remedy that
disarms it — a correct instrument with a stale expected value, which nothing about
its construction warns you about.

### T4 — Integration (fast-forward up)

**Direction** upward, worktree into the node above.
**Performed by** the owner of the target node, in the owner's own worktree.
**Rule** The node is fast-forwarded to the worktree. The worktree is never fast-forwarded to the node — that direction is T2.
**Enforcement** `git merge --ff-only <child>`, or `harness integrate <child> | --children`, which is that merge with the catch-up and the ordering around it. A contributor that has not caught up is refused with `fatal: Not possible to fast-forward, aborting.`
**Fails when** Treated as a push. Pushing to a checked-out branch is rejected: `! [remote rejected] … (branch is currently checked out)`.

**Presenting rings the lead.** `harness mark <task> --done` rings the lead's doorbell at once, and orientation never folds a "presented, unsigned" line away under the owner's focus (obs 91: a lane presented, its session ended without a message, and the lead learned 2h43m later from a nag its focus had folded).

**A lead with more than one child should use the command**, because serialising is the part that was left to be remembered and [[#T2 — Catch-up (merge down)]] is where that bill came due. It refuses an occupied or dirty child worktree, refuses work that was never presented, aborts and hands a conflict back rather than resolving one, and does not run the child's checks — nothing in this CLI executes a manifest command, and the one place the design has a lead run a member's checks is [[#T7 — Conflict escalation]], where a conflict has already made it necessary. It is a merge with the bookkeeping, not a reviewer.

**A review is required, and it is enforced.** `harness review <node> --record` reads the diff and records the read against the child's exact commit; `reference-transaction` refuses the parent's fast-forward without that record. A new commit on the child invalidates it automatically, so there is nothing to expire.

**The record says who read it, and for a long time nothing asked.** The gate's whole test was that a file existed. `harness review --record` defaults its target to the node you are standing in and asked nobody's rank, so a member could write the record that unblocked its own integration — and the gate justified by *a member cannot verify its own work* was satisfiable by that member, silently, with a green result. The record had carried `reviewed_by` and `session` from the start. **Provenance nobody reads is provenance nobody corrects**, which is the same sentence [[#T16 — A finding crosses one rank, and becomes work only with approval]] wrote about `decided_by`, arriving a second time in a place nobody thought to look. The guard now reads `reviewed_by_node` — derived from git in the recording session under [[#R1 — Position is derived, never declared]], so it cannot be claimed — and refuses unless it is the node being integrated into. Refused in the CLI too, but the guard's is the one that holds: a check in the CLI is bypassed by writing the file.

**A clean catch-up carries the review; a conflicted one does not.** The record is keyed on the child's sha, so the lead's own catch-up under T2 invalidates the read it just did — and a lead integrating *k* children would re-read every one of them, *k* times, for merges git performed mechanically. So `integrate` carries the record across a clean merge, recording `carried_from`, because the child's side was read, the parent's side is the lead's own integrated history, and nobody decided anything in between. A conflict never reaches that path: somebody chose something, and it is read.

**Detection is by ancestry, not by shape.** The first gate asked whether the parent's new sha *is* a child's tip, which is true of the fast-forward this design uses and false of every other way the same work arrives — `git merge --no-ff <child>` produces a merge commit that is nobody's tip and walked past the gate untouched. The question that holds is whether a child's tip became reachable when it was not reachable before, which costs the same to ask. It also checks **every** child that newly arrived rather than the first match: two children can sit on the same sha, and a review recorded for one satisfied the gate for the other.

Why enforced rather than expected: a member cannot verify its own work. Measured, a model revisiting its own output without an external check gets **worse** in every configuration tested, one case falling from 75.8 to 38.1, while the same procedure improves results when an oracle is available. The lead is that oracle. This reverses an earlier decision in this note that left the read optional.

One consequence to know before meeting it: git checks out the fast-forward *before* the ref update the hook aborts, and no earlier hook fires on that path. A refused integration leaves the branch unmoved and correct, and the working tree already updated to the child's content. `git reset --hard HEAD` restores it, and the refusal says so.

**What it shows.** `harness review <node>` / `--children` builds what a pull
request would show, from local git: the commits ahead with their `Task:` trailers
(and a warning for any that lack one), the diffstat, whether the child is caught
up so the fast-forward will actually succeed, any document touched by a code node
— and the thing no pull request can report, **which files a sibling also
changed**. Seams belong to the lead under [[#I9 — The lead owns the seams]], so an
overlap is the lead's business by definition and neither child is positioned to
see it. Two children can each be individually fast-forwardable while colliding
with each other; the review surfaces that before either merge, rather than as a
conflict after the first one lands.

The document check calls `_guard --classify` rather than matching paths itself,
and reports `document check UNAVAILABLE` when the guard is missing or too old.
An unavailable check must never render as a clean one — the first draft of this
command returned an empty result in that case and silently read as "no
violations".

**Being able to read it is a separate requirement, and it survives the gate.**
This paragraph used to open *reading is optional* and say the harness does not
gate the merge on a review, which stopped being true when the gate was built and
sat here for weeks afterwards contradicting the section above it — the expensive
direction, because a lead that believes it meets the refusal *after* git has
already checked out the fast-forward. What the paragraph is actually about is
unchanged and is not about pace: **a fast-forward leaves no boundary.** After `T4`, parent
and child point at the same commit, no merge commit records where the
contribution began, and `parent..child` is empty. Measured in a live tree, five
of six children sat at zero ahead and `review` said *nothing to present* for
every one — the diff a lead had chosen not to read had become unreachable.

So an integrated child falls back to a window of its own history, labelled as a
window rather than as the integrated set, because the exact set is genuinely
unrecoverable from git alone. `--since <ref>` reads any explicit range. The
window is `N` **first-parent steps**, and the commit count printed is the number
of commits in the resulting range, which is routinely larger — a header reading
"last 4 commits" above a list of thirteen is exactly the kind of figure that
gets quoted later, so the two are named differently.

**Why not actual pull requests.** The suggestion is sound and the gap it aims at
is real: nothing else in the tree reads a member's diff. But a PR merged on a
server runs none of this repository's hooks, and every guarantee in
[[#I4 — `reference-transaction` is the primary guard]] is a local hook. Enforcing
the authorship rule server-side would mean a second implementation of the
matcher, which is the exact defect that made `doctor` pass for the wrong reason.
A merged PR is also not a fast-forward, so it discards the catch-up discipline
that makes a conflict surface at the member while its work is still warm. What a
lead actually needed was the artefact, not the platform. A real PR earns its cost
when work must leave the machine — an outside reviewer, CI that cannot run
locally, an audit trail for people outside the tree — and none of those are
true of a local tree today.

### T5 — Document request (upward)

**Direction** upward, one rank at a time, to rank 0.
**Rule** Documents are never committed below rank 0. A change is requested as an exact old→new pair with a rationale and a pinned base.
**Enforcement** The guards refuse a document path committed on any node below `main`.
**Fails when** The pair goes stale in transit. If `old` no longer matches, the application is refused and the pair returns. Risk grows with the number of ranks crossed.

### T6 — Propagation (downward)

**Direction** downward, rank by rank.
**Rule** Documents travel down by merge. Guards and the manifest do not travel at
all — every worktree reads one shared copy.
**Enforcement** The guard tests **authorship, not path**. A document is refused
when it was *edited here* and allowed when it *arrived* from the document node.
Those are told apart by blob identity against the document node's history: if this
exact blob was ever that node's content at that path, it came from there.

**Not the document node's current blob.** That rule is wrong and was measured
wrong: the document node moves while a change traverses the tree — one commit per
105 seconds against a three-hop journey — so a legitimately merged copy routinely
fails to match the tip. The history form is correct, and is affordable only when
cached against the document node's tip and extended incrementally (measured: 9.3s
for a full pass, 0.25s incremental, microseconds per lookup).

**Fails closed.** A missing or unreadable tree or manifest is a defect, not
permission — this guard only runs where the harness is configured. Only a branch
that is no node in the tree is passed over.

**`never_travels` is empty by default and should usually stay so.** A path listed
there is refused even when it *arrives* by merge — and since a hook can only allow
or abort, that aborts the entire merge rather than skipping the path. Six edges in
one project were sealed this way, the refusal merely changing its reason.

It is **not** needed to protect `.harness/`. Measured: a code node given its own
`manifest.json` declaring nothing to be a document was still refused, using the
document node's copy. Hooks resolve through an absolute `core.hooksPath` and the
guard resolves config through `--git-common-dir`, so both always read the document
node's checkout. A copy on any other branch is never read and never executed — it
is inert by construction, not by convention.

**Fails when** Globs are written assuming `*` crosses `/`. It does not; `**` does.
`design/*.md` is depth-1 only, `design/**/*.md` is any depth.

### T7 — Conflict escalation

**Direction** upward one hop, to the node that issued the work.
**Applies when** this node issued the tasks named in the conflicting commits' `Task:` trailers, so it already holds both intents. Otherwise [[#T8 — Deep conflict]].
**Rule** A conflict surfaces during the second T2, while the author's own work is current. The member collects and does not resolve.

1. Collect: `git diff --name-only --diff-filter=U`; stages `:1:` base, `:2:` ours, `:3:` theirs; `git log --merge` for both author names.
2. Ask the lead. The member cannot know why the conflict exists.
3. The lead reads the recorded intent of both tasks.
4. The lead states the cause, then proposes a resolution.
5. The member re-runs its own checks and states the effect on its task — a check result and a claim, not agreement.
6. The lead runs the absent member's checks. Their tests stand in for a signature nobody can verify.
7. The member presents; the lead performs T4.

**Fails when** No intent was recorded. The correct output is then *the cause is not known*, escalated as a ruling request — not an invented cause. Also when the same file conflicts twice under one lead: that is a scope defect, not a merge, and the scopes are re-cut.

### T8 — Deep conflict

**Direction** at the node where the two lines of work meet.
**Applies when** the conflicting commits name tasks this node did not issue. That is a property of authorship, not of tree position: two sibling lead nodes conflict under T8, because the work was authored ranks below them.
**Rule** The node frames the collision from its own coarse assignment — which is the right altitude, since at that level the honest output is often a ruling rather than a merge — and resolves it from the ledger.
**Enforcement** Every commit carries a `Task:` trailer, so a conflicted hunk resolves to ledger ids without asking anyone:
`git log --merge --format='%(trailers:key=Task,valueonly)' -- <file>`
**Fails when** The ledger has been cleared. By the time work aggregates two ranks up, the originating task is usually closed and its worktree released — see [[#I6 — The ledger is append-only]].

### T9 — Ruling

**Direction** upward as a request, applied at rank 0.
**Rule** One rulings file. Leads submit; the top lead writes. A ruling is a document change and uses T5 — there is no second mechanism.
**Fails when** Every conflict produces one. Mechanical conflicts resolve under T7 and produce no ruling; only missing intent and repeat scope defects escalate.

### T10 — Release

**Direction** terminal, member to lead.
**Rule** Commit, integrate by [[#T4 — Integration (fast-forward up)]], close the
ledger row, drop the worktree, and stop the session.
**A task has three states, and the member owns only the first transition.** `--done` presents it; the **lead** closes it, on the same rule as the brief — the node above sets the task and the node above says it is finished. A member closing its own task is a member marking its own homework, which [[#T4 — Integration (fast-forward up)]] already refuses in the other direction.

| | who | what it records |
| --- | --- | --- |
| open | the member, at `mark` | the starting position |
| **presented** | the member, at `--done` | the **cost**, and that it believes the work finished |
| **signed off** | the lead, at `--close` | that the work is accepted, and the task leaves the node |

**The measurement is taken at presentation, not at sign-off, and that is why the split works.** A lead closing a member's task is by definition a different session, so a subtraction there would be across two transcripts and mean nothing ([[#I10 — Cost is estimated, then measured]]). Taking it when the member presents keeps the one number that was ever real.

Presented work does **not** hold the node: `recycle --idle` sweeps it, because the member has finished and measured, and only the lead's sign-off is outstanding. Waiting for that would idle a session with nothing left to do. `status` shows the task as `awaiting sign-off` rather than merely open, because those are different facts about who is holding things up.

**Presenting does not reach the lead, and the member must. This is T10's last step, not a courtesy.** The claim that the lead is told at orientation was written here and was false in the only case that matters. Every mechanism that tells a lead anything — the Stop hook, edge-triggered orientation — fires when the *lead* takes a turn, and a member presenting gives it no reason to take one. Worse, the thresholds guarantee the miss: a presentation is only owed after `STALLED_SIGNOFF`, by which point the lead has been standing still at least that long, so the condition becomes true strictly after the last moment anything could have tested it. Measured on a live tree 2026-09-08 — a lead stopped at 11:21:10, its members presented at 11:25:47 and 11:44:14, and neither hook could fire for either; both sat unsigned until the operator prompted rank 0 by hand twenty-eight minutes later, for the third time that evening. It was read every time as a lead that forgot, and it was never that.

No command can close this from below: checked against the CLI 2026-09-08, `claude` offers attach, logs, stop, rm and respawn and nothing that delivers a prompt into a running session. The only transport is a message from another session, so it must be sent by somebody mid-turn — and the member that has just presented is the only party that qualifies. `harness mark <task> --done` resolves the lead's live session from its claim and prints the message and the address; if the lead is not running it says so instead, because sending a member after a dead session is worse than the record it already wrote. The push is the member's; the record remains the fallback the lead reads at orientation.

**Enforcement** `harness mark <task> --close` writes the record: the closing sha, the closing session, and the delta if it is subtractable. `harness release` frees the node. `harness stop <node>` ends the session that held it: `claude stop` is a full teardown — the process dies, the session file is removed, and it leaves `claude agents --json`. A lead can reap its whole layer with `harness stop --children`, and no session may stop itself. A stop is recorded per node (`stopped/<node>.json`, with `--why`, the owner's words when it is theirs), so the hooks don't read a deliberate stop as an outage: `lead_owes` raises no "down" or "orphan" row for it and orientation says it was stopped on purpose, until a claim or spawn clears it (log 115: after the owner's "stop all work", main's Stop hook told it to spawn dev). Halting the tree stays the owner's. **A released node is not a running one** (log 128): a child with no claim and no session in its worktree, while its own task, its lanes' tasks or its unread rings wait, is `down` in its lead's hooks, with the unread count. **A question owed** (log 129): a child's ring to its lead that asks (a `?`, "block…", "question"), older than 20 minutes, with no ring back since and the child's turn ended, is an `unanswered` row. `integrate --dry-run` only says it would end a presented child's lingering session (log 117). A mid-lead's `mark --close` on a segment its lead wrote presents it upward and keeps the claim (log 127); only the writer of a brief closes it. A pending `--at-quiet` reset names the session it was set for, and a different session drops it and rings the requester; `recycle` decides what the fresh session opens before it stops anything, and a launched recycle is checked 3 minutes later: if no session claimed, rank 0 and the lead are rung (log 123).
**The close is the point, and it had no record until 2026-08-31.** "Released" was a claim in a message rather than a fact in a store, so nothing could tell a node still working from a node finished and still standing there. `harness status` now names the difference — an open task, or `unassigned` — and `harness recycle --idle` sweeps exactly the children that have none. Closing is always permitted even when the measurement is not: a task closed in a different session than it opened records `_delta: null` and says why, because refusing the close over an unmeasurable cost would leave the task open forever and destroy the one signal this exists to give.
**Fails when** The row is deleted rather than closed — [[#T8 — Deep conflict]] depends on closed rows staying readable. Or the session is left running after its node is released: a lane nobody can shut down is not a lane, it is a leak. `release` drops the claim and **does not end the session**, so that leak has a shape — a live session standing in a worktree it no longer claims, constrained by no rule in the tree. `status` reports it as `OCCUPIED but unclaimed`.

**No brief, no task. `harness mark` refuses, and there is no `--force`.** This was a convention until 2026-08-31 and conventions do not survive a busy night. A task opened without a brief is a task whose scope will arrive in pieces, and the measured penalty for that is 39% against delivering the same information at once — appearing at **two** pieces, so the first follow-up detail is already the failure. The remedy is one command, and it is the command that makes the work go better; a bypass flag would only let the expensive path stay open.

Three arms, each refusing for its own reason: **no brief at all** (with the remedy addressed to whoever is standing there — write it, if rank 0; ask your lead, if not); **a brief for another node**, since a task belongs to one node; and **an empty brief**, because a task nobody can describe is not ready to issue.

The gate sits at `mark` rather than at `spawn`, because the requirement is on the *task*, not on the session — a node may legitimately be occupied with nothing to do. But a node with nothing briefed is not started: `spawn` **skips** it and names both remedies, and `--empty` stands one up on purpose. **Rank 0 is exempt**, because the refusal exists to stop a node starting with nothing to open and then asking its lead what to do — rank 0 has no lead, and writing the queue is its job rather than a precondition of it. `spawn main` into an empty tree is the ordinary way to start a project, and gating it asks the operator to do rank 0's work before rank 0 exists to do it. It warned and started it anyway until 2026-09-08, which is a caption rather than a warning — the session is already launching by the time the line is read. Standing up an empty node stays legitimate; what it stopped being is the silent outcome of a bare `spawn` that meant *start my lanes on their work*.

**The brief is written by the lead, and `harness brief` enforces that.** A lead writes the briefs of its **children**; rank 0 writes its **own**, because there is nobody above it; and no node writes its own anywhere else. A node that sets its own task is the failure the tree exists to prevent, and it is also this transaction — everything the lead knows goes down at once, *from the lead*.

| act | who | |
| --- | --- | --- |
| `harness brief <task> --for <node> --write` | that node's parent | writes or rewrites it |
| `harness brief <task> --write` | rank 0, for itself | the only self-write in the tree |
| `harness brief <task> --suggest` | the node the brief is **for** | proposes; does not change it |
| `harness brief <task> --resolve N` | that node's lead | marks a suggestion addressed |

**A brief is a plan, not provenance, and the two are kept in different files on purpose.** It is rewritten in place, the revision counter advances, and the previous text is gone — because a working document that behaves like a record is one people become afraid to correct. `harness note` is the append-only half: comments are never edited, and they survive the recycle that ends the session they answer. Both attach to the same task and neither is allowed to become the other.

**Comments inform; only the brief instructs.** `harness brief <task> --comment` appends context from anyone — the operator, a lead, a peer — and changes nothing about what the work is. If it *should* change the work, the lead folds it in and the revision advances. Two channels of instruction would rebuild the drip-feed this whole design exists to close, one piece at a time, so the separation is enforced by which command can write the text.

That is what lets the reasoning stay upstream. The operator and rank 0 can argue an item out in comments on `dev`'s brief; rank 0 then **rewrites** `dev`'s brief, `dev` writes `dev_1`'s from scratch, and the member downstream receives a clean instruction and never sees the argument. Each level rewrites rather than forwards, and the thread that produced revision 3 stays readable next to it — the append-only half doing the job the mutable half cannot.

**Nothing can push to a running session, and that limit is stated rather than worked around.** A comment is surfaced by the next harness command the session happens to run: `whoami` prints an unread count at every start, resume and compact, and reading the brief marks it read **for that reader only**, so a lead reading a child's brief does not clear the child's flag. A comment therefore reaches a lane at its next harness call or its next recycle, not the instant it is written; a member deep in an edit-test loop will not see it for a while. [[#R4 — No arbiter process]] is why, and inventing a poller to hide it would cost more than the delay does.

The assignee is not silent, and that is what stops "no questions asked" collapsing into the 39%-wrong result at [[#T12 — Question]]. It reads the brief, and `--suggest` records a proposed change against the revision it read, for the lead to fold in or decline. **A suggestion is not an edit**, and the work continues against the brief as it stands while the lead decides.

A brief exists **before** its mark: the lead writes it, then the member accepts. So `harness gui` shows briefed-but-unmarked work on the child's card as a dashed chip — handed down and not yet picked up, which is a window a lead otherwise cannot see.

### T11 — Comprehension check

**Direction** upward, one turn. Not a negotiation.
**When** After the first T2, before the first commit.
**Rule** The member restates the plan in its own words: what it will change, which seams it touches, what it will deliberately not touch. The lead reads it and corrects only a misreading. There is nothing to approve, because the approach was decided at [[#T1 — Task assignment]].
**Why it survives at all.** An earlier draft made this a proposal the lead approved, which is a round trip and therefore the 39% penalty in miniature. It is kept, inverted, because models are unreliable at noticing they need to ask: on a benchmark built by stripping detail from real issues, interaction recovered up to 74% of lost performance, but detection swung wildly with prompt phrasing and one model never asked at all, a 100% false-negative rate. A forced restatement is the cheapest available detector for a misunderstanding the member would not otherwise raise.
**Fails when** It becomes a proposal again, or a plan document. If the restatement needs a page, the task is too large — see [[#I8 — Tasks are short]].

### T12 — Question

**Direction** upward during work, answered downward.
**Rule** A member may ask its lead about a **gap the plan could not have covered** — something the lead did not know at [[#T1 — Task assignment]]. It may not ask for confirmation of what the plan already says; that is the incremental-arrival penalty arriving through a side door.
**Why it is not removed.** Workers given ambiguous instructions with no channel to ask were correct about 39% of the time, so roughly 61% of submitted work was wrong. And specifications are incomplete more often than their authors believe: 46.7% of flagged ambiguities in freshly written specifications were confirmed by the authors themselves, about 2.6 per specification, and 38.3% of a curated software benchmark was judged underspecified. A complete plan is the goal; a channel for the gaps is the admission that the goal is missed about half the time.
**Enforcement** The lead answers, or escalates under [[#T5 — Document request (upward)]] and [[#T9 — Ruling]].
**Fails when** The lead answers from guesswork. *I don't know, escalating* is a correct answer, on the same principle as an unrecorded intent under T7.

### T13 — Unblocking is a task

**Direction** the operator's answer arrives at rank 0; work leaves rank 0 downward.
**Rule** A block that has been answered is **half-finished**. Closing it requires naming what work the answer produced: a brief, or an explicit `none` with its reason. `--resolve` refuses an operator-answered block that names neither, and `--no-task` refuses an empty reason.

**Why the gap existed.** [[#T9 — Ruling]] said the outcome reaches the lane rewritten, and [[#R14 — The operator is told, and does not have to look]] routed the conversation to rank 0 so the lane would not receive reasoning as though it were instruction. Both were right and neither closed the loop. The operator answered, `grant` closed the block as a side effect, rank 0 read the thread — and then the decision lived in a record no lead reads and in a transcript that ends at the next recycle. The lane was unblocked and still working to the brief it had. **Being told is not being tasked, and a task is the only thing in this design that travels.**

**Rank 0 closes any block in the tree**, not only its own. It held the conversation; leaving the close to the lane that raised it hands the decision to the one party that was not in it.

**Look at what the answer released, not at the block.** A ruling on one lane's question routinely unblocks work spread across lanes that raised nothing. Rank 0 writes one brief for the whole of it, addressed to its lead, and the lead splits it — which is [[#T1 — Task assignment]] applied a rank higher, with the same rule that everything known goes down in one go.

**Lineage, not forwarding.** `--from-block` stamps the block with the task it produced, so the block stops appearing in rank 0's queue by the act of being answered rather than by being dismissed. The brief records which block it answers and the lane can read the operator's reasoning one hop away — but the brief itself is rank 0's rewriting, never a relay of the thread ([[#T9 — Ruling]]).

**Answered is the test, not closed.** A block the operator replied to and nobody closed is the commonest shape of this, and it appeared in nobody's queue: not the operator's as a decision, because they had made it, and not rank 0's as work, because it was not resolved. It now sits in rank 0's queue, and the operator's shows one summary count instead of asking them to decide twice.

**Answered means their word is the LAST word, not that they once spoke.** The first reading of this rule made the operator's own reply the thing that hid the block: it left every surface they read, permanently, and any comment appended afterwards — including a measurement refuting the answer they had just given — reached a thread they had no reason to open again. A block returns to the operator's queue the moment anything is said after their last comment, and leaves it again the moment theirs is the last. It comes back as *what came back*: the replies since their answer, not the request they already read. **A block that was GRANTED never returns** — there the operator did the thing rather than said something, and the reach exists whatever is said about it afterwards. Recording what it produced closes it, because that is the second half of the same act.

**A task written before anyone linked it still counts.** `harness blocked <need> --task <task>` attaches an existing task to an answered block, repeatably, and closes it. Without that, a decision acted on and never linked stayed in the queue forever and **every respawn re-reported it** — a fresh rank 0 has no memory, so an unlinked decision looks exactly like an unmade one, and the second session writes the brief again.

**A respawn needs the state, not just the link.** `--decided` prints answered blocks whose tasks are `briefed`, `open`, `presented` or `gated`, one line each, and goes silent once every task has closed. All four states are read off the mark and brief records that already exist, so there is no second store to fall out of step. A queue that keeps naming finished work stops being read, which is the same rule that keeps a self-closed block out of it.

**A block the raiser closed itself is not in the queue.** No operator comment, no grant: it found another way, there is nothing to hand down, and a queue that names work which does not exist is a queue that stops being read.

**`none` is a real answer.** A reach grant usually removes an obstacle without adding work. It is recorded with its reason because an unexplained silence and a forgotten decision are indistinguishable afterwards.

**Enforcement** `harness blocked --decided` is rank 0's queue and `whoami` prints its count at orientation. The consequence is a field on the block record, so it survives the recycle that ends the session which wrote it.
**Fails when** Rank 0 answers the operator in the block thread and stops, satisfied that the exchange happened. The exchange is not the deliverable.

### T14 — A brief handed to a lead is split, not done

**Direction** downward, one rank at a time.
**Rule** A brief written for a lead is a **segment sized for a rank**, not a task sized for a session. The lead discharges it by opening a mark on it (it is doing the work itself) or by deriving briefs from it for its children (`--from`). Until one of those, the brief is **unactioned** and `whoami` says so at every orientation.

**Why it needs a record.** Nothing else in the harness notices a cascade that stops. `spawn` and `recycle` warn that a node has nothing briefed; nothing warned that a node had a brief and had passed none of it on. A brief written for a lead then sat in a directory nobody was asked to look in, and the rank below never learned the work existed.

**`--from` is what makes the split visible.** A lead may only split a brief written **for it** — lineage that can be invented for work never handed down is lineage not worth reading. The derived brief is a rewrite carrying its own complete specification, never the parent forwarded or the parent in pieces: the 39% penalty of [[#T1 — Task assignment]] does not care whether the pieces arrived as three briefs or as one brief and two comments.

**Task ids are compared after sanitising.** A brief is stored under the filename its id becomes, so `corpus-ingest` and `corpus_ingest` are one brief; comparing lineage on what was typed made a recorded split fail to count and left the lead nagged for work it had already passed down.

**Enforcement** `handed N brief(s) to split or start` at orientation, cleared only by a mark or a derived brief.
**Fails when** A lead treats its segment as its own task list and works it directly with children idle. That is legitimate only when it is genuinely one session's work; the mark is the declaration that it is.

### T15 — Acceptance is not a decision

**Direction** none. This is the absence of a transaction, stated so it stops being invented.
**Rule** A brief at the head of a node's queue is an **instruction already given**. The member opens the mark and begins. It does not ask whether to start, and there is nobody waiting to be asked.

**What it is not.** [[#T12 — Question]] stays exactly as it is: a member may ask about a gap the plan could not have covered. *Shall I do this?* is not a gap. T12 already forbids asking for confirmation of what the plan says, and the behaviour happened anyway — which means the rule was true and was not reaching the member at the moment it mattered.

**That moment is orientation.** A session that starts, reads its brief and ends its turn with a question has spent a session to request something it already held, and the node it is standing on is now idle with a live counterparty — the condition [[#R2 — Occupancy is the worktree, not the session]] exists to prevent, arrived at by politeness rather than by drift.

**Ambiguity is what produces the question, and the queue is what removes it.** A member holding four briefs and no order does not have a backlog, it has a choice — and a member choosing which of its tasks to do first is choosing its own work, one notch smaller than choosing its own task and refused on the same grounds. So orientation names **one** task, prints the two commands that begin it, and says plainly that the brief is the instruction. What follows it is listed and marked *not yours to start*.

**It is not a members-only rule, and treating it as one caused the same failure one rank up.** A lead used to be told `handed 3 brief(s)` — a list with no first item and no instruction to begin. So it asked what to do; and having nobody obvious in the tree to ask, it asked the **operator**, which routes around the rank that owns the answer. Orientation now names one task and whose order it sits in at every rank, and only the verb changes: a member opens it, a lead splits it or opens it.

**The one case where asking is right has a correct target, and it is never the operator.** A node with an empty queue and nothing open says so to its **lead** and stops. The lead is told the same gap from its own side at its next orientation, so it is already a record before anyone speaks. The operator could not answer it without going through the lead in any case.

**Enforcement** None, and there cannot be. A CLI cannot make a session begin. What it can do is remove every ambiguity the question could be about, and say the thing at the moment the question would otherwise be asked. If it is still asked, that is a prompt failure and not a design gap.
**Fails when** The queue is empty and orientation says so. A node with nothing briefed asking what to do is correct; that question belongs to its lead, and `spawn` does not start the node that would ask it.

### T16 — A finding crosses one rank, and becomes work only with approval

**Direction** upward one rank, then downward as a gated brief.
**Rule** Potential work noticed while doing something else is recorded as a **finding**, addressed to the **lead of the node that made the claim**. The lead either writes a brief from it or declines it on the record. A brief written from a finding is **not staffable until the operator approves it**.

**The channel was missing and its absence had a shape.** A lane learns something real — that a size in pixels is not a size on screen, because the layer adds the point offset before the perspective divide, so nothing at two depths is painted alike — and there is nowhere for it to go. Not a block: it asks the operator for nothing. Not a suggestion: it is not about this task's brief. Not a fact: no command produces it. So it goes in a report, and a report is read once by one session and then ends. The most expensive thing the session produced is the thing with the shortest life.

**It goes up exactly one rank, and to the lead.** The claimant may not act on it — a member doing what it noticed is choosing its own task ([[#T15 — Acceptance is not a decision]]) — and the lead is the only party that may turn it into one. Reaching past that lead is refused.

**It carries how it was found**, on the same rule as [[#I13 — A measurement travels with the command that produced it]]. *Found by looking at a screenshot after the arm went green* is the difference between a claim a lead can weigh and one it can only believe, and `--how` is required. The same lane caught a regression by **use rather than review** — a 2px floor cut reachable documents from 20 to 6 while every check it had written stayed green — which is the case for the channel in one sentence: the finding was invisible to every instrument that existed, and existed only in a session that was about to end.

**Approval is the operator's, and rank 0 decides on their behalf.** Every rank *below* rank 0 is refused, because a lead approving the brief it just wrote is the gate approving itself. This remains stricter than [[#I11 — Reach beyond the worktree is granted at enrolment]] in what it means, if no longer in who may act: a grant is a capability rank 0 already holds, so making one gives it nothing, while an approval is a *decision* about whether unrequested work is worth a session. The CLI still cannot authenticate an operator and does not pretend to — it records who decided.

**Changed 2026-09-07, on the operator's instruction, and the reasoning it replaces is kept rather than deleted.** The rule was *no session, rank 0 included*. What it cost was concrete: rank 0's orientation printed pending approvals, and rank 0 could read every one of them and act on none — so the queue named the operator's attention as the only thing that could move, and the tree waited for a human who was not at the keyboard. That is [[#R13 — Everything below rank 0 starts cold]]'s overnight stall by another route. The risk the old rule named did not go away; it was traded, knowingly, for a tree that runs.

**So the case it existed for is recorded rather than refused.** When rank 0 approves a brief rank 0 itself asked for, the approval carries `self_approved: true` and the command says so on the line. Carving that case out would have been the old gate back under a narrower name. `decided_by` now names the deciding session instead of asserting `"operator"` — nothing ever read that field, which is exactly how it could have gone on claiming a human decided long after that stopped being true. **Provenance nobody reads is provenance nobody corrects**, and it is worse wrong than absent.

**The wait pool** (log 109, owner 2026-10-08). A ruling can say a task waits on something no verb names ("unstaffed until a design session produces a design"); approve would break it and decline would end it, and the Stop hook blocked rank 0 on every turn for it. `harness brief <task> --wait "<condition>"`, by rank 0 or the task's lead, parks it for 12 hours: it leaves every queue, the approval nag skips it, and the GUI shows it on its node with the condition. It is never renewed by itself. When the 12 hours run out the harness moves it back to the normal pool and the Stop hook of the node that parked it blocks once to say so; keeping it waiting takes a new `--wait`, so a wait can't fade into a footnote. `--wait none` takes it out early.

**Gated means gated.** The brief is written in full and readable by everyone; it is in no queue, `harness mark` refuses it, and `spawn` and `recycle` will not start a session on it. A declined brief is never offered again but is never deleted: what a project decided against is part of what it is, and the next lead to notice the same thing deserves the answer.

**Nobody waits.** The lane that raised the finding carried on with its queue, and the gate holds no session idle. That is what makes it safe to gate at all.

**It has a way up** (2026-10-08, log 106: dev_tests briefed its worker from a finding rank 0 approved, nobody had briefed dev_tests or dev for that work, and `integrate dev_tests` refused "no PRESENTED task record"). A node presents only a task it was briefed. So when rank 0 approves a finding-born brief, either by handing the finding down or by `--approve`, the harness writes a **carrier** brief, `<task>.up-<node>`, for each node from the brief's writer up to, not including, rank 0. Each carrier is approved, carries `carries: <task>`, and waits (`after`) on the task one rank below, so it opens once that is signed off. Its node then marks it and presents it with `--done` like any other task, and its lead integrates. Each carrier's node is rung when it is written. A brief that is already a part of a segment (`from`) has its way up and gets none.

**Enforcement** `--how` required; the addressed lead only; every rank below 0 refused at `--approve`, with rank 0's own approval recorded `self_approved` and said on the line; `mark` and the queue both exclude a gated or declined brief. Rank 0 sees it at orientation and reads it with `harness brief <task>` — deciding whether a task is worth a session means reading the task.
**Fails when** A lead turns every finding into a gated brief. The queue is the operator's attention and it is finite; declining on the record is a first-class outcome and costs one line.

### T17 — Rank 0 and leads ask the owner, through the intermediary

**A hand-off to the owner is an ask, and only an ask** (log 97, 2026-10-06: a lead "handed to the operator" in a note and its own todo list, and every lane went idle on it). The Stop hook blocks, once, a turn of rank 0 or a lead whose messages close by handing something to the owner or operator (below rank 0, also "leave … to you") while none of its asks is open and the turn names no open ask; measured on a day's biblion2 turns, it fired 4 times in about 640, each a real hand-off. The asker can take an ask back: `harness ask <id> --withdraw "why"` (the asking node, rank 0, or the owner from a shell), logged to `owner/withdrawn.jsonl`. A note on the `owner` task is refused with the route that reaches the item (`--msg`), since nothing reads one there.

**Scope frames every ask, and every ask carries its chain** (owner, 2026-10-06, after owner-7 reached them as two `harness stop` commands and "run them, then click Done"). The harness reads the chain off the transcripts at `ask_open` (`ask_chain`): the asker's turn, what opened it (the owner's words, a launch, a cross-session message, doorbell mail, which now records the sending session), and upstream through each sender's turn, up to six hops; each hop records the node, its task and feature (untraced when none), what reached it and what it concluded. `ask --show` prints it first and the Issues card shows it. The brief has thirteen sections, scope first (question, scope, situation, chain, cause, harness, tried, why you, options, commands for actions, consequence, checked, unknown, recommendation), or the short form ending `## Out of scope`, a complete answer. `ask_verify` refuses a brief whose `path:line`, sha, log entry or quote can't be found (quotes must be what a chain session said or what the intermediary read, never its own writing), with fewer than two verified Checked lines, a `Harness: yes` without a place, or a multi-session chain none of whose sessions it asked (`--to`). Every ask runs on Opus; an action's commands and Done are hidden until it is briefed, and a reply no longer readies it. An out-of-scope item offers the owner Drop it (`ask --drop`: the ask closes and the untraced task on its chain is marked `out_of_scope`, leaving every queue, its node and lead told to close it), Halt the tree, or It's in scope.

**Direction** upward, out of the tree, to the owner; the ruling returns on the task.
**Rule** A question only the owner can answer (intent, judgement, something only they can do, risk they must accept) is opened with `harness ask <task>`. The intermediary, one read-only session outside the tree, investigates it, may question the asker, returns what isn't the owner's, and briefs the rest in seven capped sections written for the owner, not the tree. The owner discusses it with the intermediary in a terminal; the intermediary drafts the ruling; only the owner's **accept** in the GUI writes it to the task's brief (`rulings`), and **reject** removes the question. This holds for rank 0 even when the owner is in its session (owner, 2026-10-06: main put a live delete for approval in chat, where the owner might not see it): a command, an approval or a question for the owner is an ask, so it shows in the Issues tab; chat may only point at it.

**Why this shape.** `harness decision` (removed 2026-10-05) let the asker write the question to justify itself, gave the owner no way to reply but a quoted shell argument, closed nothing and told nobody; three were raised and none was answered. The intermediary writes for the owner, checks the asker's claims against the code, and the accept button is the signature no session can forge: `--accept` and `--reject` refuse inside any session.

**Commands for the owner.** Rank 0 hands the owner commands as an action ask on its standing task `owner`, with `--run "cmd"` per command. A command learned after filing is added with `harness ask <id> --run "cmd"` by the asker or rank 0 (log 113); an item already briefed goes back to its intermediary to re-brief, so the owner never sees a command it hasn't vetted. They show in the Issues tab at once; the owner clicks **Done** (the asker's doorbell rings) or asks about them (`--query`, answered by the intermediary's `--reply`). The owner can also open a conversation (`--kind note` on `owner`).

**A ruling rings** (2026-10-08, log 108: two rulings sat unread while rank 0 waited on its doorbell). Accepting a ruling rings the asker and the lead of the brief's node, once each, with its first line and `harness brief <task>`; the orientation line stays until they read the brief. The documenter's rulings go to its next run instead.

**One intermediary per item** (owner, 2026-10-05: one project-wide session grew too large to keep). Each open ask gets its own session, `harness-intermediary-<project>-<id>`, removed when the ask closes; at most 3 run at once and the rest queue. Sonnet takes action items and notes, Opus intent, judgement and risk. A session sleeps after 55 quiet minutes, inside the one-hour prompt cache, and a message resumes it. Messages are addressed to the ask, never a session: `harness ask <id> --msg` in from anyone (the owner's chat box under the item does the same), `--reply` out to the owner, `--to <node>` out to a node, whose doorbell rings. Everything lands in the ask's thread. The intermediary has no `SendMessage`, which loses a message to a sleeping session. **It writes in one place** (log 114: owner-8's intermediary wrote a brief it couldn't submit): an item session has Write and Edit with a single `Edit(//<scratch>/**)` allow rule, its scratch folder `~/.cache/harness/asks/<project>/<id>/`, removed when the item closes. Its brief and any long `--reply`, `--text` or `--draft` go there as a file, passed by path; a heredoc is a redirection and inline text with backticks reads as command substitution, both refused under dontAsk. The folder is outside `~/.claude`, which Claude Code protects whatever the allow rules say (measured: the same rule there was refused). Long stdin is refused too, whatever it holds (measured: a 3-line heredoc passed, an 11k-character brief did not), so the file is the only route. A resumed session keeps the tools it started with, so each fresh start stamps the item's folder with its permission profile (a hash of `intermediary_cmd`'s source and the tool lists); a wake finding the stamp missing or different starts a fresh session with the inbox and a pointer to `--show`, instead of resuming (log 114, follow-up).

**Enforcement** `harness ask` refuses a lane, a task with no brief (except `owner`, rank 0's only), and `--run` off an action ask; the intermediary's verbs (and `--reply`, `--to`, `--idle`) need `HARNESS_INTERMEDIARY=1` and act only on its own ask (`HARNESS_ASK`), which only `harness intermediary` sets; `--accept`, `--reject` and `--done` refuse inside any session; briefs over a cap are refused by section. Design: `harness/design/owner-channel.md` in the setup repo.

### T18 — The documenter keeps the documents

**Direction** sideways, outside the tree, into rank 0's worktree by `T5` pairs.
**Rule** A fresh background session per run (`harness documenter`) keeps the project's documentation current and true. **A run is one document, whole** (owner, 2026-10-06: one change per run made each run relearn the doc, and runs trimmed words without checking content): it reads every section, checks each concrete claim against the code at HEAD, fixes what the code plainly contradicts (each pair's `why` cites `file:line` or a commit), moves history verbatim to `provenance/<doc>/<section>.md` with a `Why:` pointer, raises scope conflicts with the owner, trims last, and submits one batch. `harness docs measure` lists the docs that need a run by trouble: paths, links and functions it names that are not there (`harness docs check`, against the repo and the manifest's `doc_sources`), a check against the code never made or outdated by commits to the code it names (`harness docs verified` records the commit), lines that read as history, size, and `CLAUDE.md` over budget. **An auto run draws its doc at random** (owner, 2026-10-09: ranking by reads took `CLAUDE.md` 21 times in 32, because every session loads it, and the rest went unread because they went unfixed): every doc that needs a run is in the draw, weighted gently by trouble (1 + log2(1 + trouble)), reads play no part, and the last five docs run (`docs begin` keeps the history) sit out unless nothing else is left. The launch names the drawn doc in the run's opening prompt. **A run may find its doc needs nothing** (owner, 2026-10-09): `harness docs skip "<why>"` records the doc as checked against the code at HEAD with the reason, logs the skip, rests the doc and draws another for the same run, three skips at most before the run ends with its note. Stale docs (no reads, pointers or citing record, idle 14 days) are listed apart and may be deleted in any run's batch. `harness docs begin <doc>` records the run's doc, which the GUI card shows. **Scope conflicts go to the owner** as `harness ask docs --kind scope`, through an intermediary to the Issues tab: something the charter does not cover, a doc against the charter or a ruling, two docs disagreeing about what the project is, or an intent the code doesn't meet; the sections stay untouched until ruled, and the same open question is refused twice. Pairs may `create`, `move` (text leaves for the end of another file, a pointer takes its place) and `delete` as well as replace. Rank 0 reviews every batch before it applies (owner, 2026-10-05, reversing auto-apply after obs 77): `harness pairs <task>` shows the diff and stamps the review, then rank 0 applies it or declines it with a reason. A move is checked verbatim on disk before the commit, and a created file or move destination must be a path the manifest classes as a document (obs 76). **Runs start only by hand** (owner, 2026-10-06: not automatically until the design is good enough; `DOC_AUTO_RUN`): the GUI card's start button, or `harness documenter [--doc <path>] [--runs N]`; each run of a chain draws its own doc. A run is not over until rank 0 has decided its batch (owner, 2026-10-05): its `docs note` leaves the session waiting; an apply closes it and starts the next run of a chain; a decline resumes it with the reason to fix and resend the batch, twice at most, and a third decline ends it. A run that submits nothing stops at its note; `--stop` lets the current run finish and starts no more.

**Plans are not the documenter's** (owner, 2026-10-11: plans are not documentation in the normal sense; of biblion2's last five runs, four were on files under `plans/`). A plan says what was intended, so checking it against the code and trimming it is wrong. The manifest's `documenter_skip` lists globs the documenter leaves alone, `["plans/**"]` when the key is absent and nothing when it is `[]`. A skipped document is never drawn for a run or listed as needing one, `docs begin` refuses it, and `pairs submit` from the documenter refuses a batch that edits, moves out of or deletes one. It stays a document to the guard, and stays in every session's scope index.

**Why this shape.** biblion2's `CLAUDE.md` reached 16,212 words, about 21k tokens loaded by every session at start, with 409k more words of markdown behind it, and rank 0 is the only writer: upkeep competed with orchestration and lost. A fresh session per run keeps no context to manage; pairs keep rank 0 the only committer.

**Enforcement** `pairs apply` refuses any batch (from anyone) that leaves `CLAUDE.md` over the manifest's `claude_md_words` and larger than before, and any `delete` of a path an open record names. The documenter runs `--restricted` with read tools; its identity (`HARNESS_DOCUMENTER`) comes through `--settings`, a background session not inheriting the launcher's environment, and `pairs apply` refuses it. Design: `harness/design/documenter.md` in the setup repo.

### T19 — A design session stands beside rank 0

**Direction** sideways, outside the tree. Nothing is handed on by the harness: the owner talks to it and passes the design to rank 0.
**Rule** `harness design <topic>` (the owner's, from a shell; refused inside a session) starts a session for design work on one topic, beside rank 0 (owner, 2026-10-10: "another session onto main, for design work for new complex features"). It is not a node: it holds no claim, has no lead and no children, and I1 stands, because it works in a worktree of its own, `<repo>-design-<topic>`, on a branch `design/<topic>` cut from rank 0's. It reads every node's worktree and the tree's records, writes design documents in its own worktree, and directs nothing. The same command again resumes the topic's last conversation (`--fresh` starts a new one, `--here` runs it in the terminal); `--list` shows every design with its commits ahead of rank 0; `--end` stops the session and removes the worktree, keeping the branch, and refuses uncommitted work; `--drop` deletes the branch too and lists what is lost.

**Why this shape.** A second session in rank 0's own worktree is the breach I1 exists to prevent, and a second rank 0 would be two sessions holding one authority with separate contexts. Design is reading and writing documents, so it needs neither: rank 0 stays the only session that briefs.

**Enforcement** Three layers, none resting on the session's good behaviour. Permissions: it runs `--restricted` in `manual` mode, so the machine's own allow rules do not apply; it is allowed `Edit` under its worktree only, read-only git (`log`, `show`, `diff`, `status`) on the other worktrees, ordinary git in its own, and `harness`; anything else asks the owner. The CLI: with `HARNESS_DESIGN` set (through `--settings`, as a background session does not inherit the launcher's environment), `design_gate` allows a list of read verbs and their reading arguments, which answer as rank 0 would see them, and refuses the rest, a verb added later included; the session hooks say nothing, so it never takes rank 0's mail. The guards: `design/<topic>` is not a node, so the document guard passes over it and its documents commit freely; merging it into rank 0 is an ordinary merge, since the integration gate fires only for a child node's tip. Measured 2026-10-10 in a scratch project with the guards live: a document committed on the design branch and merged into the document node, while the same document authored on a code node was refused; in print mode with the session's flags, a write and an edit in other worktrees, a commit there and `git push` were refused, and a write and commit in its own worktree went through. Rank 0's orientation names each design and its commits ahead; the tree's reconcile (run by `harness trim`) labels its branch and worktree instead of calling them strays. A halt does not stop it: it starts nothing of the tree's. Claude Code starts a background session only in a repository it trusts, which every enrolled project with running nodes already is.

## Invariants

### I1 — One session per branch

Enforced by git, not by agreement. `git worktree add` refuses a branch another worktree holds: `fatal: 'dev' is already used by worktree at …`

**That sentence covers only half of it, and the uncovered half is the dangerous half.** Git refuses one *branch* in two *worktrees*. It has nothing to say about two *sessions* in one *worktree* — that is the claim lock's job, and the lock is a file, so it binds only the tools that consult it. Anything that starts a session without one can produce the state git is being credited with preventing.

**And that failure is silent by construction.** Two sessions in one tree are both writing it, so one's `reset`, `checkout` or `stash` reaches the other's uncommitted work — and a destroyed uncommitted edit leaves no artefact at all: no error, no diff, and a clean `git status` that positively asserts there was never a change. This is not hypothetical and it is not the harness's own history: biblion2 added per-session worktrees on 2026-08-26 after edits vanished twice from one shared checkout, which is why that repository's CLAUDE.md leads with it.

**Measured 2026-09-07: `harness recycle` could manufacture it.** Every refusal in its holder loop ended in `continue`, which continued the HOLDER loop rather than the node — so with a busy holder and no `--force` it printed `skip dev  busy`, then `recycled dev`, then `recycled 1`, and started a session beside the one it had just declined to stop. The command that maintains the lock was the one able to break it, and had the two sessions then collided the evidence would have been a clean tree. It was findable only because it printed the refusal and the contradiction in the same breath. Fixed — a refusal now abandons the node — but the general rule is the durable part: **any path that spawns must treat a doubt about a node as fatal to that node, never as a note.**

**Stated once for the holder check, and left unapplied everywhere else in the same command.** `spawn` went on printing *nothing briefed — it will have no task to open* in the same output as the spawn it described, which is the identical shape one refusal to the left. A warning emitted in the same breath as the action it warns about is read afterwards, and by then the only question left is what to do about it. Three instances were found in one evening — this one, a `--close` prompt claiming *every part settled* for a segment whose parts were superseded rather than done, and an `unsigned` line offering `harness recycle <lead>` without looking at whether that lead held an unpresented mark. The test is mechanical: if a line describes a reason not to do something, the something must not already be happening on the next line.

**And that rule needs two qualifications, both found by biblion2-main reading the fix rather than the code.** First, *"I stopped the holder"* has to be **measured, not requested**: `claude stop` exiting 0 says it asked, and whether the process died is a separate fact that only the roster reports. A session that ignores the signal or shuts down slowly left the caller free to start a second one beside it, with a clean exit code certifying the result. `recycle` now waits for the holder to leave the roster and treats exit 0 with a surviving session as a failed stop. Second, **the caller is a holder too**: recycling the node you are standing in printed *that is this session*, correctly declined to stop itself, and then spawned — so the one participant guaranteed to still be there was the one exempted from the check. `--force` changed nothing there, because the thing being forced was never the obstacle.

The shape is worth naming because all three instances share it: **an arm that correctly declines to act, followed by code that proceeds as though the action had happened.** The decline is visible and looks like the safe outcome, which is exactly why nobody reads the next line.

**It is the acting half of a pair this project has already paid for on the checking half**, and the two are worth reading together because a reviewer who knows one will recognise the other. The checking half is a guard that passes because it met *something* rather than the right thing: `doctor`'s code-path arm reimplemented `_guard`'s matcher, drifted, and selected a **document** — passing for the wrong reason — and the same arm drew its code sample from a node that may track no code at all, so it could never fail. biblion2's CLAUDE.md states the general form after nine instances in one build: *a guard that has never failed is not yet a guard*, and *a verification offered as evidence is a check* — a digest said to prove a schema had not moved covered two lines of a block and none of its rows, and would have matched however much the schema changed.

So: **a check that cannot fail, and a refusal that does not stop anything.** Both read as green, both are load-bearing, and neither is visible from the line that carries it. The test for the first is to break the thing it protects and watch it go red. The test for the second is to force the refusal and check what ran afterwards — which is how all three instances above were found, and none of them by reading the code.

### I2 — Nobody pushes

The owner of a node integrates contributors into it. Pushing to a checked-out branch is rejected outright, so the invariant costs nothing to maintain *between the branches of this tree*, while every node stays checked out.

**That covers the direction nobody was going to take, and for a while nothing covered the other one.** git's refusal is about a local branch that a worktree holds. It says nothing whatever about a remote, so `git push origin w_m1` was unguarded — and [[#I4 — `reference-transaction` is the primary guard]]'s table said that hook fired on a push, which is true and useless: on a push it sees `refs/remotes/*`, which is exactly what a **fetch** updates, so it cannot tell the two apart and a refusal there would break every fetch in the repository. A row reading *fires* over a hook that cannot act is a check that cannot fail, which is the shape this note tells its own readers to hunt.

**`pre-push` is the one hook that runs on the sending side knowing it is a push**, so the rule lives there. It asks `_guard --publish <branch>`: a branch outside the tree is not the guard's business, a branch named in the manifest's `publish` list is allowed, and a node branch is refused. `publish` is empty by default, which is this invariant stated exactly. It is a document, so widening it is rank 0's deliberate act and every node reads the same answer.

What is at stake is not tidiness. Every guarantee here is a **local** hook and a remote runs none of them, so a pushed node branch is work no rank has integrated, sitting somewhere the guard cannot reach and cannot undo. `git push --no-verify` skips this exactly as it skips `pre-commit`; nothing local is proof against it, which is why this is an invariant with a guard rather than a property of git.

### I3 — Scopes are globally disjoint

No two open tasks anywhere in the tree may claim the same path, checked against a single registry. This makes textual conflicts rare rather than routine, and leaves semantic conflicts — a changed signature that a caller elsewhere depends on — which produce no merge conflict and are caught by checks at integration.

**A member writes only inside its own worktree.** An artefact outside the repository has no owner, no path scope and no instrument that can go red on it: nothing reviews it at [[#T4 — Integration (fast-forward up)]], no guard refuses it, and no ref records that it changed. A member producing one is producing something the tree cannot see, check or undo. Outputs outside the repository are rank 0's or the operator's, unless the machine's owner declared otherwise — see [[#I11 — Reach beyond the worktree is granted at enrolment]]. This is not a restriction added on top of the permission system; it is the same rule I3 already states, applied to the one direction it had not been.

**A record anyone may correct must be a document inside the tree.** Code has an owner, a scope and an instrument that goes red. A note kept outside the repository has none of the three, so a disagreement about it cannot be settled by a check, a diff or a ref — only by argument, and argument between two parties who both value catching errors alternates instead of converging. Inside the tree the same correction is a [[#T5 — Document request (upward)]] pair: applied once by the owner, no reply expected, terminal on an artefact. Outside it, the exchange has no terminal state at all, and nothing in the protocol can ever say which round is the last. Measured 2026-08-31: four rounds of mutual correction over records held outside any scope, each finding something genuine, each smaller than the last, no ref moving after the first.

### I4 — `reference-transaction` is the primary guard

| operation | `pre-commit` | `pre-merge-commit` | `pre-push` | `reference-transaction` |
| --- | --- | --- | --- | --- |
| commit in a worktree | fires | n/a | silent | fires |
| fast-forward up (T4) | silent | **silent** | silent | fires |
| merge down (T2) | silent | fires | silent | fires |
| `reset --hard` | silent | silent | silent | fires |
| `branch -f` | silent | silent | silent | fires |
| `branch <new>` | silent | silent | silent | fires — see below |
| `push` | silent | silent | **fires** | fires on `refs/remotes/*`, and cannot act |

Every T4 is a fast-forward by design, so `pre-merge-commit` is silent on the path documents would take. `reference-transaction` alone covers it. It must be POSIX `sh` with an explicit `exit 0`: a non-zero exit gives `fatal: ref updates aborted by hook` and the repository stops accepting any ref update.

**The last two rows are each a hole that was closed, and they close differently.** A push reaches `reference-transaction` only as a remote-tracking ref update, indistinguishable from a fetch, so that hook cannot refuse it and [[#I2 — Nobody pushes]] moved to `pre-push`. **Branch creation** is the other: there is no `old` to diff from, so the document arm was skipped and the ref update passed — a branch outside the tree may author documents freely, and `git worktree add` of a new *node* branch at that commit was then the whole bypass, in two ordinary commands. With no diff to take, the guard classifies the whole tree instead; only paths matching `docs` are read at all, so it costs the size of the document set rather than of the repository, and branch creation is rare.


#### Trust model — what the guard does not cover

An audit of the runtime found no command injection (every `subprocess` call
passes an argument list; nothing uses a shell) and no secrets in the tree. The
real exposure is structural, and worth stating because it is easy to mistake the
guard for more than it is.

**Propagation is a code-execution channel.** Three documents travel down under
[[#T6 — Propagation (downward)]] and every one of them executes:

| document | executed by | when |
| --- | --- | --- |
| `.harness/hooks/*` | git | every commit and every ref update |
| `.claude/settings.json` | Claude Code | every session start on that node |
| `manifest.json` → `checks[].command` | the session | every check run |

So **rank 0 holds arbitrary code execution on every node in the tree.** That is
inherent — a guard that cannot travel cannot be repaired — but it means the
document node is the only trust boundary that matters, and "documents are
reviewed at every rank before rank 0 applies them"
([[#T5 — Document request (upward)]]) is a security control, not only an
editorial one.

`core.hooksPath` is absolute and shared by every worktree, so a change to the
main worktree's `.harness/hooks/` takes effect on all nodes at once, without a
merge and without review. Convenient for repair; the same property in the other
direction.

**The guard's own availability is part of its threat model.** Three fail-opens
were found and closed in one day, in three files, the third written immediately
after the first two were fixed. The generalisation, which is `biblion2-main`'s
and better than mine: *a guard whose absence is indistinguishable from its
consent is the default shape unless someone writes against it.* The reviewable
question is not "did I check" but **"does this code have a path where
not-checking and checking-clean render the same?"** Two more were found by asking
exactly that: `_guard --classify` returned nothing on the document branch and on
any branch outside the tree, which a caller could not tell from "no documents
here"; and a hostile glob in `manifest.json` could hang the matcher indefinitely
— eight `**/` segments did not finish in five seconds — which on
`reference-transaction` stalls every git operation on the node with no message
at all. A guard that hangs is indistinguishable from a guard that is thinking.
### I5 — Checks run to completion

Every check in a task's set runs, including after one fails. Each check declares what it cannot see, as a required field of its definition, and the report carries pass, fail and blind spot for all of them.

**A finished lane never deadlocks its lead** (log 105, 2026-10-06). One answer for "running" (`node_running`: the claim lock, then a live session in the worktree) feeds orientation, spawn and integrate, so a lead is never told to spawn a child spawn refuses. A child that released its node with nothing unpresented but whose session stayed is "lingering": `integrate` ends that session itself before merging. **The queue** (logs 103, 104): a command job is estimated only from runs of the same command, and a running job past its estimate says by how much; `harness slot` commands are listed in `harness test` and on the GUI card while they wait and hold, take the slot first in, first out, and go before queued jobs.

**One full run per change, at the lead** (owner, 2026-10-08: a worker ran the full set, then its lead ran it again after merging; one lane's change cost up to three full runs, about 2.5 hours of the one test slot). On a member `harness check` runs only the arms its change touches: the diff from the merge-base with its lead's branch, matched against each arm's `paths` globs in the manifest. A changed file no scoped arm claims runs every arm, because an unmapped change is the one nobody has said is safe; files matching the manifest's `checks_ignore` need no check; an arm without `paths` runs whenever anything testable changed; when nothing testable changed the report records that and nothing runs. When no arm declares `paths`, nothing is compared and `check` says so, naming the fix; `harness doctor` notes it once, without failing (log 110). The report says `scoped`, not partial. A lead's `harness check` runs every arm by default, and `mark --done` tells a lead presenting on a scoped report to run `--all`. `--changed` and `--all` override either default. Results are still never reused.

**This was an invariant with no implementation until 2026-09-08.** Nothing in the CLI read `manifest["checks"]` — grep found one hit, the template that writes it. So the manifest declared checks, briefs said *done means green*, and no command ran them or recorded that anyone had. A lead integrated on a member's **word** that they passed, which is the self-verification [[#T4 — Integration (fast-forward up)]]'s gate exists to refuse, arriving through the other door. It was found by driving a sandbox through a full lifecycle and noticing that running the checks by hand left no trace.

**The harness has no tests of its own** (owner, 2026-10-06). It manages worktrees and task order, and gives a project a safe way to run its tests when there are many worktrees: it schedules runs, isolates them and delivers the results. The project owns what runs, its setup, where its scratch goes, which arms a change needs, and whether an old result still holds.

**Enforcement** `harness check` queues the commit (2026-10-06, after obs 81: sessions running checks side by side stalled the machine). Jobs wait in two queues, each in the order asked, and their tests are packed into the memory ledger (below): **priority** for integration (a lead's or rank 0's check) and **normal** for lanes and `harness test -- <cmd>`; a running job is never pre-empted. Submit prints the expected wait, from each arm's recent run times (the median of its last five; a running check counts down arm by arm), or from finished jobs like it when an arm has none (log 111: a one-arm job was estimated as a full check). One job still runs at a time; the owner chose true estimates over a second slot. A job runs in a fresh `git worktree add --detach` copy of the commit on the Linux disk, not where the worktree was (obs 84), and the project is told so: `HARNESS_TEST_ORIGIN` (the requesting worktree), `HARNESS_TEST_SHA`, `HARNESS_TEST_JOB`, `HARNESS_TEST_SCRATCH` and `TMPDIR`, the last two inside the run folder and deleted with it (obs 86: anything a project writes elsewhere stays). A request joins an identical job still queued or running; a finished report is never reused, because a project's tests may read data the commit doesn't hold (obs 83). `--arms a,b` runs only the arms the caller names, and the report says it is partial. The harness chooses arms in one case only, a member's default: the arms whose `paths` its diff touches, with every arm for an unclaimed file (see *One full run per change, at the lead* above; obs 82). There is no harness setup step: setup belongs in the project's own commands (obs 85). `harness slot -- <cmd>` takes the same slot for a project's own runner. The runner (`harness testd`) is a plain process, not a session, and kills each arm's whole process tree on timeout or cancel (obs 80). It records the result against the exact commit, like the review record, so a new commit invalidates it by construction. `blindSpot` is refused when absent rather than defaulted — a check that does not say what it cannot see is read as proof of more than it is — and it is printed **beside each result**, because the moment it matters is the moment somebody is deciding what a pass means.

**Tests share a memory ledger** (owner, 2026-10-09: a full check spent 43 minutes running single-threaded arms one after another; this replaces the same day's per-job pool, fcdbd64). The unit is a test: each check arm and each `harness test` command. Every submission carries each test's memory estimate, the least it may need (`--memory`), and is refused without one; the refusal suggests the median peak of its last runs. A test reserves estimate × 1.2 (`TEST_NEED`) in a pool of `test_pool_share` (0.8) × `MemTotal`, which on WSL2 is the memory the VM is given. The pool is soft: the ledger only counts reservations and never kills, so actual use may spill over while reservations keep the total in bounds. The runner keeps adding tests from every queued and running job while they fit the pool and `test_cores`; a test larger than the pool, an `exclusive` arm, or a job queued before estimates runs alone. Which goes next is weighed (owner, 2026-10-09): each queued test scores 1 + wait / `TEST_STARVE` (600 s), wait counted from its job's submission and an integration job starting 600 s ahead, and a test that fits now scores `TEST_FIT_BONUS` (2) times that; ties go to the best fit (the largest need), then the longest-running. The highest score starts. When the highest is a test that doesn't fit, nothing passes it and the pool drains for it. So a fresh test that fits goes ahead of an old one that doesn't, until the old one has waited about 600 s more than twice the newcomer's wait, and then the newcomer waits even though it fits. A test blocked only by its own earlier run of the same name holds nothing. This replaces a hard rule (backfill freely, then stop everything once the oldest unfitting test had been blocked 600 s). A waiting `harness slot` command starts nothing new and is let in when the running tests end (log 104). Each test runs in a transient cgroup scope (`systemd-run --user --scope`, `MemoryMax` = estimate × 2, no swap, `OOMPolicy=continue`); a wrapper inside writes the scope's `memory.peak` and `oom_kill` before it exits, because systemd removes a scope at once (measured). Over its ceiling a test is `KILLED`, a failure, and the rest carry on. **A test is capped one of two ways, and the harness proves which** (log 142, owner 2026-10-11: after a WSL restart the user's systemd manager was down and 246 tests ran with no ceiling and no measurement for four hours, with nothing to say so). `system`: its own cgroup scope with `MemoryMax`, exact, where `systemd-run --user` works. `watch`: where it does not, the harness adds up the memory of the test's whole process tree (`Pss`, so shared pages count once; a child that detaches itself stays counted) every 0.5 s and kills the tree above the ceiling. Close, not exact: a spike shorter than the gap can overshoot (measured: a 300 MB allocation under a 128 MB ceiling reached 304 MB before the kill). Each report row records which (`capBy`). The proof (`caps_selftest`) runs two real processes: one that takes 96 MB under a 32 MB ceiling must be killed, one that takes 16 MB under 64 MB must finish and be measured; a system cap that makes a scope but fails the proof is set aside for the watch. It runs at every runner start, hourly, as soon as the system's answer changes (a "no" is re-asked each minute), in `harness doctor`, and on demand with `harness test --caps`; the result is `testq/meta/caps.json`. Nothing is said while the system cap is proved. Otherwise one line names the way and the fix (`sudo loginctl enable-linger <user>`), or says `MEMORY CAPS OFF`: first in every check report, at the top of `harness test`, in `harness doctor` (which also checks lingering), as a badge on the viewer's test panel, and once to rank 0 when it changes (an FYI when the system cap is back). A row with no peak says "peak not recorded"; a timed-out test keeps its peak, read from the scope before the kill (2026-10-11: the kill took the wrapper that writes it), and the highest sample stands in whenever the scope's own figure cannot be read. A test that fails only because the manager vanished mid-run is run again under the watch. **The runner picks up an install:** when the CLI is replaced it starts nothing new, lets what runs finish, and re-execs; nothing is cancelled. **The history keeps the last five runs that have a peak** as well as the last five of any kind, so an outage cannot push the measured runs out. Each test gets its own `HARNESS_TEST_SCRATCH` and `TMPDIR`. A job's copy is made when its first test starts and torn down after its last, when its report is written and its requesters rung, as before. The last five runs per test (peak, seconds, estimate, killed) are kept in `testq/meta/usage.json`; reports show them, estimates are simulated from them, `harness test --usage` lists them. Cancelling a job flags it: the runner kills that job's tests only. Measured in a sandbox with the real runner: six 3-second tests from two jobs ran in 3.49 s; a test asking 64M and allocating 200M was killed at its 128M ceiling; three 6G tests (7.2G reserved each) against the 18.8G pool ran two then one; the estimate for that job was 6.2 s against 7.0 s measured, copy and teardown included.

**Where it surfaces is the point.** `harness mark <task> --done` says whether the set ran at this commit and what it said, so a member presenting unchecked work is told before its lead is. `harness review` prints the same for the child being integrated, and an absent report renders as **NOT RUN**, never as clean — the rule the document check on that command already follows.

**A partial report says so first** (log 92, 2026-10-06: a hold skipped 8 of 9 arms for three hours, and the report looked whole). A report with arms that did not run (held, timed out, exit 125) leads with `PARTIAL: 1 of 9 arms ran; 8 NOT RUN (held: …)`, in the printed report, the queue's mail and the presenting line; `--set-baseline` refuses it, since a held arm used to be recorded as a known failure. A hold older than 30 minutes is an obligation in its placer's and rank 0's orientation, re-reported until it is released. **Rank 0 or a lead moves a job forward:** `harness test --promote <id> --why` puts a queued job at the front of the priority queue and rings its requesters (log 98: the critical-path arm waited two hours behind full checks); one slot still, per log 89. A lane cancels only jobs it asked for.

**Nothing runs it implicitly.** `manifest.json` is a document that travels to every node and `checks[].command` is executed by the session, which [[#I4 — `reference-transaction` is the primary guard]]'s trust model names as one of three code-execution channels rank 0 holds over the tree. A hook or an orientation path that ran it would make that channel automatic. It runs when someone submits it. The manifest is read from the document node's checkout via `--git-common-dir`, the same resolution `_guard` uses, so every node runs the same set.

### I5b — A claim is required against a live holder, not against an empty node

Nothing consulted the lock before writing to the ledger. Measured on the sandbox 2026-09-08: an entire lifecycle — briefs, marks, presentation, review, integration, sign-off — ran through with `harness status` reporting `no nodes claimed` throughout. The claim is the only mutual-exclusion primitive in the design and no write path read it.

The rule is deliberately narrower than *you must hold the claim*, and the difference is where the hazard actually is. An **unclaimed** node is the operator working by hand, a scripted walkthrough, or a session between claims — untidy, not dangerous, and refusing it would break every by-hand path including this project's own tests. A node claimed by **somebody else who is still running** is the real thing: two sessions writing one node's ledger, which is [[#I1 — One session per branch]]'s failure reached through the records instead of through the worktree.

So `mark` refuses a live foreign holder, warns on an unclaimed or stale one, and names which it met. An unreadable roster warns rather than refuses — the opposite call from `harness integrate`, which is writing into another node's worktree and must not guess. **Absence of a claim is a gap in the record; presence of the wrong one is a collision.**

### I6 — The ledger is append-only

**Facts** (log 101, 2026-10-06): a `--recheck` whose command exits non-zero or prints nothing is recorded as a failed observation beside the value, which stands; `latest` skips failed ones. `--from` must parse as shell (`bash -n`) to be recorded. **`harness cited`** (log 102, obs 78) matches the full path or its last two parts, never the file name alone: a fact naming one `live-copy.db` no longer protects every other.

Rows are closed, never removed. Every commit carries a `Task:` trailer so any ancestor can resolve a conflicted hunk to a ledger entry without reaching down the tree.

### I7 — Fan-out is a dial

Conflict pairs at a node are *k(k−1)/2*; depth is *log_k(W)*. Narrow fan-out lowers conflict load and raises latency, agent count and the distance to a common ancestor.

| fan-out | depth at 8 members | agents | conflict pairs |
| --- | --- | --- | --- |
| 8 | 1 | 9 | 28 |
| 4 | 2 | 11 | ~13 |
| 2 | 3 | 15 | 7 |

Under I3 conflict rate stops driving the choice, and fan-out is set by what a lead can hold in context.

Integration load is not the constraint: every T4 is `--ff-only`, which cannot conflict and costs nothing. The load that scales with subtree size is T5 — every document request from anywhere below climbs through this node and is reviewed here. That cost is not overhead; it is the review the hierarchy exists to perform. The one lever against it is batching: a lead that collects requests before passing them up also deduplicates them, and two members asking for the same document change become one request for every ancestor above.

Leads write no code, so their context stays shallow — a ledger, a set of intents, and a request queue — however wide it gets.

### I11 — Reach beyond the worktree is granted at enrolment

A node that must touch a path outside the repository gets it from `grants.json` in `~/.claude/harness/<slug>/`, beside `binding.json`. **Not from `tree.json`.** The tree is a document and rank 0 edits documents, so a permission set living there is one the tree can widen for itself; and it would travel by merge to machines whose owner never agreed to it. Enrolment is where a machine consents to participate ([[#R9 — Enrolment takes two keys]]), so it is where its owner says how far. Same key, same scope, never committed.

| act | who | what it is |
| --- | --- | --- |
| `harness blocked <need> --why` | the member | a **record**, not a message: it survives the recycle that ends the session which raised it, and `status` prints every open one together |
| `harness grant <node> <path>` | rank 0, or a shell with no session | append-only; carries the reason and who made it |
| `harness grant … --revoke` | same | sets `revoked_at`; the record stays readable ([[#I6 — The ledger is append-only]]) |

Grants become two documented, additive `claude` flags at the next spawn or recycle — `--settings` with a `permissions.allow` list, and `--add-dir` for reach — so a running session keeps exactly what it started with and a grant never takes effect mid-task. **A path grant is not a pass through the classifier** (log 112: dev_1's granted fixture write was refused as "Modify Shared Resources"). Under auto mode Claude Code's classifier decides each write by itself, so `harness grant` says so when it records a path, and `grant --list` marks live path grants: a lead plans a write outside the worktree as an owner action ask from the start, or the owner adds a project permission rule.

**Two things this deliberately does not do.** It cannot authenticate an operator: `harness grant` from rank 0 and from a human shell are indistinguishable except in the record, which is why every grant carries `granted_by`. And it does not let a lead unblock a member. A session with looser settings performing a write another session was refused is the operator's decision being routed around rather than implemented, and it is refused by rank, not by trust.

**Why a grant is not automatic.** A grant made under time pressure for one task persists for every later task on that node, and once nobody can reconstruct why it exists, nobody removes it. So a grant names a **path**, not a node, and records what asked for it. Being blocked and being unblocked are different acts by different parties, on purpose.

### I10 — Cost is estimated, then measured

Every task carries an estimated cost band at [[#T1 — Task assignment]] and a measured actual at [[#T10 — Release]]. Bands, not numbers — a guess to five significant figures is a lie.

| band | tokens | shape |
| --- | --- | --- |
| **S** | ≤ 40k | one file, approach already known |
| **M** | 40k – 120k | several files, some exploration |
| **L** | 120k – 300k | needs design, touches more than one seam |
| **XL** | > 300k | not a task — a decomposition that has not happened yet |

**A finished session's own record is readable.** `harness spend <task>` from another session, or from a shell, reads the marking session's transcript within the task's window (mark to presentation) and splits its NEW tokens by tool, Bash command class, after-compaction and past-warning turns (obs 88). That is one session's record, not a subtraction across sessions, which stays refused.

**The band counts NEW tokens** (up + down), not billed total. Resent context is excluded, or every band would be exceeded by the second turn and the estimate would measure conversation length instead of work.

**Opening a task is not blocked by an unmeasurable cost.** `mark` called `read_spend` directly, which exits `CONTRACT` when the transcript is missing or its shape has moved — so a transcript-format change would have made it impossible to open a task **anywhere, in any tree**. Position-recording is what the ledger is for; the cost is the second thing it carries. It now records a null baseline and says so, which is the judgement [[#T10 — Release]] already makes at the other end: refusing a close over an unmeasurable cost would leave the task open forever and destroy the one signal the record exists to give, and refusing the *open* is worse, because there is no record at all to be imperfect. Presenting is decoupled for the same reason — a member that cannot present is a member whose finished work is invisible to everyone above it. `harness spend` still refuses outright, and should: there the number **is** the output.

**XL is a refusal, not a size, and is now enforced.** It is the operational definition of [[#I8 — Tasks are short]]: `--band XL` is refused outright, so a lead that cannot bring a task under L splits it or escalates. This is the only number in the harness that decides whether work may be issued at all.

**The estimate goes in with the brief, because that is whose it is.** `harness brief <task> --for <node> --write - --band S|M|L`. The only place to enter it used to be `harness mark`, which the **member** runs — so a lead's XL was refused at the member's keyboard: the one party that may not split the task ([[#T15 — Acceptance is not a decision]]) and can make the refusal disappear by typing a smaller letter. An enforcement pointed at the wrong actor is not an enforcement, and this one had the additional property that obeying it required disobeying something else. [[#T1 — Task assignment]] always said a task record carries an estimated band *at issue*; the number simply had nowhere to live until the brief did.

**The band is read from the brief at the mark, and checked at presentation.** `--done` prints the measured band beside the estimated one. A member may still pass `--band` to disagree, and the disagreement is recorded as one — both letters are kept, with `_band_source` naming who set which. That is the earliest possible signal that a brief was mis-sized, and it is worth nothing if it silently overwrites the estimate it disagrees with. A band that was wrong is the only thing that improves the next estimate, and it is the lead's estimate that was wrong rather than the member's work — which is why the member is told to report it rather than to explain it.

Rough per-transaction cost, for budgeting a task's overhead:

| transaction | member | lead |
| --- | --- | --- |
| T1 assignment | — | 2k – 5k |
| T2 catch-up (×2) | 1k – 3k each | — |
| T3 guard check | ~1k | — |
| T4 integration | — | < 1k |
| T11 approach review | 2k – 4k | 4k – 8k |
| T12 question | 2k – 5k each | 2k – 5k each |
| T10 release | ~1k | — |
| **fixed overhead** | **~10k – 15k** | **~8k – 15k per child** |
| T7 conflict | 8k – 15k | 12k – 20k |
| T8 deep conflict | 8k – 15k | 25k – 45k |
| T5 document request | 2k – 4k | 3k – 8k **per rank crossed** |

Two consequences worth reading off the table. A conflict costs more than the fixed overhead of the task that caused it, which is what pays for [[#I3 — Scopes are globally disjoint]] and [[#T11 — Approach review]]. And T5 is the only line that multiplies by depth, which is the concrete form of the latency that [[#I7 — Fan-out is a dial]] trades away.

Because [[#I6 — The ledger is append-only]] retains closed rows with both estimate and actual, a lead's own history is its calibration set, and its estimates should improve without anyone tuning them. A lead can also sum the open bands across its subtree to see its committed load — which is the only thing in the harness that makes load, rather than structure, visible.

> [!warning] These figures are guesses, not measurements
> They are placeholders based on the general shape of agent sessions, with no data from this harness behind them. Replace each range with observed values from closed ledger rows as soon as there are enough of them, and delete this callout when you do.

#### The denominator, and why it was missing

`dev_ui_1` refused to apportion its session total across its tasks, and was
right to: nothing marked where a task began, so a share could only be guessed,
and *"a guess dressed as a measurement is the thing this lane has spent the night
arguing against."* A band can be estimated at `T1` while the actual is
unmeasurable at `T10` — the asymmetry was the defect, not the lane.

It is measurable. Every `assistant` record in a session's own transcript
(`~/.claude/projects/<slug>/<session-id>.jsonl`, already asserted by `C1`/`C2`)
carries a `usage` object. Summing them gives billed spend at any point, so the
actual becomes a subtraction:

```bash
harness mark <task-id>     # at T1, records the position
harness spend <task-id>    # at T10, the delta in components
harness spend              # no task: the session total, labelled as such
```

Without a mark it **refuses** rather than apportioning. Marked in a different
session it **refuses** rather than subtracting — a recycled member
([[#R13 — Everything below rank 0 starts cold]]) starts a new transcript, so a
mark taken before the recycle measures nothing afterwards.

**That second refusal is the mechanism working, and it will look like a bug.** A
forced mid-task recycle does not merely lose the denominator; it leaves a mark
that still exists and now points at a different session. Whoever meets the
refusal will have a file on disk that looks valid and a tool declining to use it.
It is declining because the subtraction would produce a number, and the number
would be meaningless. Recycle at the end of commits — where `R13` already puts it
— and a task lives inside one session and the subtraction holds.

Both refusals exit **4**, not 2. Exit 2 is reserved for `C1`–`C5`, meaning
Claude's internals have changed and you must not work around it; a refusal to
measure is not platform drift, and reporting it as such would send the reader
hunting a fault that is not there. The first draft used 2 for the cross-session
case and was wrong.

#### Two quantities, one word — the more dangerous defect

`dev_ui_1` reported **339,295 tokens** for its session. Measured the same night,
this session's billed total was **261,717,226**. Both are honest; they are not the
same quantity. Context occupancy is what a window holds at a moment; billed
tokens accumulate across turns, because every turn resends the conversation.

Recording both under the word "tokens" is precisely how *a number restated once
acquires an owner it never had*. So `spend` prints components and never a single
figure, and states its unit every time.

**Up, down, and resent — three quantities, and the third is never added in.**
*Up* is what was newly sent: the prompt, plus whatever entered the cache for the
first time. *Down* is what was generated. *Resent* is cache reads, which is the
conversation handed back on every turn, and it grows with the square of the turns
rather than with the size of the job. **New** is up plus down, and it is the only
one of them comparable to a band: the 261.7M above sat inside a task banded at
40k, because almost all of it was the same conversation counted again. A total
including resent measures the shape of the exchange, not the work.

**The unit is tokens and not money.** A dollar figure is a token count multiplied
by a price table the harness would have to hold, per model, and keep correct —
and every node may run a different model. A rate that has drifted produces a
figure that looks authoritative, cannot be checked from the record it sits in,
and is wrong in a ledger whose whole purpose is to be trusted. Tokens are what
was measured; the price is somebody else's table and is not this file's to
assert.

Until enough rows are closed, `dev_ui_1`'s interim stands and is now the rule
rather than a workaround: **session total plus stated coverage, no per-task
estimate.** The bands above remain guesses; `harness spend` is what will replace
them, one closed row at a time.

### I9 — The lead owns the seams

The interfaces between a lead's children belong to the lead. The insides belong to the members. A member changes anything within its scope freely; anything on a boundary another child depends on is the lead's decision, taken at [[#T1 — Task assignment]] or [[#T11 — Approach review]].

This bounds a lead's knowledge to *k* interfaces rather than *k* implementations, which is what makes wide fan-out survivable — and it is precisely the knowledge that predicts a conflict before it happens. Where [[#I3 — Scopes are globally disjoint]] prevents textual conflicts, this prevents semantic ones: a changed signature is a seam, and seams are not a member's to change.

Understanding gained here also travels upward. A lead that reviewed its children's approaches can answer for its subtree at the rank above, which is what makes a [[#T8 — Deep conflict]] resolvable from a ledger read instead of a fetch down the tree.

**Not adopted, deliberately.** Progress reporting: it costs the member real effort and returns fluent summaries that conceal problems, and a lead that cannot act on a report should not receive one. Diff review at integration: it scales with code volume rather than with interfaces, and a lead that writes no code is a poor reviewer of code. T4 stays mechanical.

### I8 — Tasks are short

The ground moves only at task boundaries, so two catch-ups is frequent only if boundaries are close together. A lead's boundary is *between integrations*, a narrower window than a member's, and it narrows with depth.

### I12 — The project says what it is before it is divided

**Rule** A **charter** holds what the project is for and which features are in scope, in prose, and every node can read it. It sits beside the briefs as its own object: a project description and, nested but separate, one description per major feature. It is written by rank 0 or by the operator directly, and by nobody else.

**What goes wrong without it, observed.** A head lead with no charter divides the only thing it can see. Reading a repository it finds failing checks, stale docstrings and disagreements between artefacts, and produces work items that are faithful, well specified, and **the maintenance backlog wearing a plan's clothes**. Of five work items written on 2026-08-31, four were derived from the state of the instrument suite and the documentation, and one from a feature — and the one was the only one where the operator had supplied a purpose in their own words. Given a feature it wrote a feature; given a test suite it wrote test-suite work.

**A backlog cannot be prioritised or bounded.** Nothing in it says what matters, because it was derived from what happens to be broken; and nothing in it can say what is **out** of scope, because being out of scope is not a property a failing check has. Both of those are the charter's job, and neither is any brief's.

**Prose, and deliberately not a specification.** Written to be understood, not implemented from. The reader who has to check it is a person, and a technical document is the format a person will not read closely enough to notice that it describes the wrong project. This is the one artefact in the system whose purpose is to be argued with by the operator, which is why it is also the one thing the viewer lets them **edit** rather than comment on.

**Read by all, required of none.** A member does not need the project's purpose to execute a complete brief, and pushing one at it would hand back the context its task was scoped to exclude ([[#T1 — Task assignment]]). But *why are we doing this* now has an answer that does not depend on a lead being awake. Orientation prints one line and a pointer, never a demand to go and read; the exception is rank 0 with no charter, which is told plainly.

**It does not reintroduce the drip feed.** The 39% penalty is about a **task's specification** arriving in pieces. The charter is not part of any task's specification; it is the standing frame that makes a brief interpretable, and it is available whole before the first brief exists. The failure mode to watch is the charter absorbing implementation detail while briefs shrink into pointers at it — which is the drip feed reassembled through a side door. The line: **the charter says what and why, a brief says how and done.** If a sentence would change when the code changes, it is in the wrong document.

**The charter is an outline, and deletion is absolute.** Features carry the order the operator put them in and may sit under one another, two levels deep — which features are facets of one thing is information, and an alphabetical list threw it away. `--move`, `--promote` and `--demote` shape it; `--delete` removes a feature outright, taking any sub-features with it, and keeps no record of what was there.

This replaced retiring, which kept a struck-through feature on the charter with the reason it left scope. The argument for retiring was that what a project decided not to build is part of what it is — which is true, and belongs in the description, written as prose by the person who decided it. What retiring actually produced was a charter that grew monotonically and was read less each time it did. **The operator owns this document; a document that remembers everything ever proposed is one they curate twice and reread never.**

### I13 — A measurement travels with the command that produced it

**Rule** A value one session hands to another is recorded as a **fact**: the value, and the command that produced it. `--from` is required and an empty one is refused. Facts are observations, appended, never edited.

**What it costs not to have this.** Sessions were re-deriving figures another session had already measured, and — the expensive half — re-deriving *how* to measure them. A number written into prose ages silently and carries no way to check it, so the honest thing to write beside one is the date it was taken and an instruction to re-derive. A head lead ended up doing exactly that by hand: *"22 endpoints, 74 declared pairs, 57 reached, 17 not reached at all, 220 requests, exit 1 — RECORDED 2026-08-30 and deliberately not re-measured since. Re-derive before acting; it is cheap for you and the figure is two days old."* Every part of that is provenance the record should have carried, written out longhand because there was nowhere to put it.

**A value with no way to reproduce it is a rumour with a figure attached.** The next session either believes it or pays the whole derivation again, and both are wrong. With the command stored, checking costs one `--recheck`.

**Record the value in the command's own words.** A figure the recorder paraphrased is one `--recheck` can never compare against, so the mechanism itself sets the convention.

**Any node may record one, and that is not a widening of authority.** A measurement is not an instruction; it tells nobody what to do. The member that ran the command is the one holding the number, and routing it up to be retyped by a lead is how a digit changes.

**Two things can have moved, and conflating them is how a stale figure passes as current.** The **commit** may have moved, which makes a figure old. The **worktree** may be a different one, which makes it a different measurement — two lanes ran the same check honestly and got 1 and 9, because `npm ci` leaves `node_modules/` and `surface/build/` behind, both gitignored and both invisible to `git status`. A tree that has ever run an install is not the tree the next reader holds. The record carries both, and the reader is told which applies.

**Briefs cite rather than paste.** `harness brief <task> --fact <name>` resolves at **read** time, so a member opening its brief sees the current value, its age, and the command — not the figure that happened to be true when the brief was written. Citing a fact that does not exist is refused, which is what stops a citation being a promise.

**A recheck is never automatic.** It runs a command another session recorded, so it happens only when typed. Nothing in the harness re-runs one on a schedule, at orientation, or as a side effect.

**Fails when** a fact becomes a channel for instruction. It carries a value and a command and nothing else; if it needs to change what someone does, that is a brief revision ([[#T1 — Task assignment]]), on the same rule as a comment.

**Fails when** rank 0 drafts a charter by reading the repository. It will describe the backlog in prose, more confidently than before, and every brief will then pass any check made against it. The operator's correction is the deliverable, not the draft.

---

## Runtime

The harness is global, opt-in, and anchored per project — the same shape as Claude's project memory. A session that has not enrolled has no role and behaves normally.

### R1 — Position is derived, never declared

A session does not look itself up by name. It asks git where it is standing:

```
git rev-parse --show-toplevel      → worktree path → node
git rev-parse --abbrev-ref HEAD    → branch
```

The worktree it occupies determines its node, its node determines its rank, and its rank determines which skills load. A session cannot claim a role; it can only be standing in one. This is [[#T3 — Guard verification]]'s principle applied to identity: behaviour, not configuration.

### R2 — Occupancy is the worktree, not the session

**A session id does not survive a resume.** Measured: resuming a conversation
from the agents panel reissues `CLAUDE_CODE_SESSION_ID`, `CLAUDE_PID`, the name
and even `kind` — the same conversation came back as a different session by every
identifier it carries.

What survives is the worktree. So occupancy is derived from it:

| question | answer |
| --- | --- |
| who is in this node? | live rows in `claude agents --json` whose `cwd` is its worktree |
| is a claim stale? | its recorded id is gone **and** nobody else is standing there |
| is this a conflict? | two or more live sessions share one `cwd` |

`claude agents --json` is the oracle: a supported command returning `cwd`, `kind`,
`name`, `pid`, `sessionId` and `status` for every live session including the
caller's own. The CLI queries it directly; nothing is handed in.

The lock file records the observed holder as metadata and is refreshed on each
claim. A claim that finds a different id recorded, with nobody else in the
worktree, is a **resume** rather than a takeover, and says so.

Prefer this over reading `~/.claude/sessions/` wherever correctness matters — that
directory is internal. It is used only on the statusline's hot path, where 0.02s
against 0.57s justifies it.


**A declared node is not a filled position.** `tree.json` names the tree; a
position exists only when a live session stands in it and derives it from git
([[#R1 — Position is derived, never declared]]). The statusline therefore renders
only occupied nodes — a lead with no children running shows no children, which is
the true statement, and `harness index` is where the declared tree is listed.
Rendering an empty node with a marker asserted a position that nobody held.

**The fast occupancy read is an approximation, and it raised a false alarm.**
`claude agents --json` is authoritative but costs ~0.6s, which a statusline
rendering every turn cannot pay, so it reads `~/.claude/sessions/*.json` and
filters by live pid. The daemon parks a warm spare process which also writes a
session file with the repo as its cwd — so it was counted as a second occupant
of the document node and displayed `!2`, the I1-violation marker, with no
violation behind it. A false alarm on the invariant the marker exists to report
is worse than no marker. Spares are auto-named after their own job id while every
harness session is named `<project>-<node>` by `spawn`, so they are filtered on
that; after filtering the two sources agree exactly. `harness status` remains
authoritative and the statusline says nothing it cannot support.

A live session in a worktree that is **not** a declared node — a branch someone
created outside the tree — maps to nothing and stays invisible to both. That is
the inverse gap and it is not currently reported.

**`claude agents --json` is not a list of live sessions**, despite what the
harness's own docstring claimed for most of its life. Exited sessions are
retained with `pid` null. Counting them meant a node whose session had ended read
as permanently occupied: `spawn` skipped it as *"occupied by"* a session that no
longer existed, so it could never be refilled, and `status` reported its lock
`live` — exactly backwards, since surfacing a stale lock so it can be forced is
what that command is for. Every occupancy question now passes rows through
`live_rows()`, which requires an integer pid belonging to a running process.
Controlled against a real pid, a null pid, a dead pid and a row missing the key;
only the first survives.
**"This session" must mean a session, not a directory.** `spawn` derived it from the branch of the working directory, so an operator standing in a node's worktree in a plain shell was told `skip main — this session` about a node whose session they had just stopped, and could not start its replacement from the one place it is natural to try. It is keyed on the session id now: where there is no session, there is no this-session, and only the occupancy check applies.

**A stale claim from another host is refused, and for a while nothing checked.** `claim` returned before its own `--force` branch, which made the remaining test unreachable: a lock recorded on a different machine was taken silently. Absence from a **local** roster is not evidence about a remote process, and taking a node a live session holds elsewhere is precisely the two-sessions-one-branch failure the lock exists to prevent. The message also stopped calling it a resume — a resumed conversation and a fresh session replacing a stopped one are indistinguishable from there, so it now reports what was observed rather than choosing between them.

### R3 — State is split by whether it travels

| in the repository, versioned | on the machine, never committed |
| --- | --- |
| logical tree (node → parent) | worktree → node binding |
| rulings, manifest, guards | **the ledger**, locks, session ids, enrolment |

**The ledger was in the wrong column until 2026-09-08, and had been all along.** This table said `ledger` was versioned. It is not: marks, briefs, blocks, findings, facts, checks and reviews all live under `~/.claude/harness/<slug>/`, and an enrolled repository's committed `.harness/` holds exactly three things — `hooks`, `manifest.json`, `tree.json`. Checked against biblion2.

Two consequences follow, and the first is why it went unnoticed. [[#I6 — The ledger is append-only]] says any ancestor can resolve a conflicted hunk to a ledger entry, and [[#T8 — Deep conflict]] resolves from the ledger — but both actually work through the `Task:` trailers **in the commits**, which are in git and do travel. The ledger files are a convenience over the top of that. The second is real and unfixed: a second machine joining the tree gets the structure and none of the history, and nothing says so at enrolment.

Worktree paths are machine-specific, so the physical binding cannot live in the repo; the logical tree must, because it has to merge. Machine-local state lives at `~/.claude/harness/<slug>/`, where `<slug>` is the project root with every non-alphanumeric character replaced by `-`. Keep it on a native filesystem — atomic claims are not dependable on a mounted Windows drive.

**The machine-local column is two stores, not one, and they have different status.** `index.json` is *derived*: a pure function of the tree and `git worktree list`, safe to delete and rebuild at any moment. `locks/*.lock` are *claims*, and by [[#I6 — The ledger is append-only]] a claim is closed rather than destroyed. So node state lives in three places, and only the first travels.

**Adding a node touches one store; removing one touches all three, and nothing announces the second and third.** Measured 2026-08-31: a session asked to remove six nodes proved containment by hand, removed six worktrees and six branches, hand-edited `tree.json`, rebuilt the index on a guess, and then found `harness status` still naming all six — from the third store, which it had no reason to know existed. It ended by hand-archiving six `.lock` files into a directory it invented. Every step was correct. The cost was that each one had to be discovered.

`harness trim <node>…` is that sequence, in order, as one instruction:

| it does | because |
| --- | --- |
| collects **every** refusal before deleting anything | a trim that removes three of six nodes and stops leaves a state no store describes |
| proves containment against each node's own parent | deleting the branch destroys the only reference to a commit the parent never took |
| refuses an occupied node, a dirty worktree, an orphaned child, rank 0, and its own node | each is work or structure that a removal would silently take with it |
| refuses when the roster is unreadable | every other reader of the roster can shrug and carry on with a worse answer; this one would delete a worktree somebody is standing in |
| removes worktree, then branch, printing the sha it deleted | the sha is the only handle left, and under `--force` the only route back |
| rewrites `tree.json`, **stages** it, and prints the commit line | the tree is a document, so the commit is rank 0's to make deliberately |
| rebuilds the index and closes orphan claims | the two derived stores, in the order that leaves neither ahead of the tree |
| reports stray worktrees and branches without touching them | deleting one nobody declared is a guess |

Pre-flight refusals are the easy half. Git can still fail mid-way — a worktree on a mount that went away, a ref another process holds — and there the rule is that **partial is acceptable, partial and unrecorded is not**: the loop stops at the first failure, then writes the tree for what did go and reconciles anyway, so no store is left describing a node that no longer exists. It exits refused, naming where it stopped and how many went.

Only rank 0 may run it, because `tree.json` is a document living in rank 0's worktree: editing it from a dev-side branch writes into another node's checkout, and the guard would refuse the commit a moment later anyway. Called with **no node names it only reconciles**, which is the repair path for a tree already trimmed by hand. `--force` overrides the dirty and containment refusals and prints what it is about to lose; nothing overrides occupancy.

### R4 — No arbiter process

There is no daemon and no server. `ListAgents` supplies liveness and `SendMessage` supplies transport, which leaves only atomic claim — and that is a lock file.

| concern | mechanism |
| --- | --- |
| position | `git rev-parse`, by the session itself |
| liveness | `claude agents --json` |
| transport | `SendMessage`, by the agent |
| propagation | `claude --bg -n <project>-<node>` |
| mutual exclusion | `O_EXCL` lock file |
| ledger, tree, bindings | plain JSON |

A single small CLI performs atomic file operations and the checks in [[#R8 — The platform contract fails loud]]. It performs no reasoning: the agent gathers liveness and decides, the CLI only writes. Nothing here starts, supervises or recovers a process.

**A downward message is executed on receipt, and there is no recall.** Two rules follow, and the second is the one that costs money when it is missing. *Sender*: by the time you send, assume it is done — do not send anything whose value depends on it not yet having been acted on, unless you also say what to do if it has. *Recipient*: an instruction that arrives after the state it depended on has changed is **reported, not reconstructed**. Say what the state is and stop.

Measured 2026-08-31: rank 0 told a lead to hold a member so it could carry its context into the next task; the lead had already recycled it, correctly, on the standing rule. The lead could not have avoided receiving that message. It could have avoided trying to satisfy it, and the attempt is where the tokens went. The instruction was also **wrong on its merits** — [[#R13 — Everything below rank 0 starts cold]] says nothing a member knows survives unless it is in a commit, a report or the ledger, so a request to preserve a session for its context is a request to skip writing a document. The coordination failure was downstream of a documentation one, and [[#T10 — Release]]'s close record is where that document belongs.

**Transport is the agent's, which sets a hard limit on what can be guarded.** `SendMessage` does not pass through the CLI, so no instrument here can count exchanges, notice that a thread has stopped producing artefacts, or decline to send. A rule of the form "stop replying after n rounds with no ref moved" is therefore a *rule with a diagnostic*, never a guard — and a guard that depends on a participant staying alert is the thing this design exists to remove. Only two mechanisms actually terminate an exchange, and neither is a tripwire: making the artefact a document, so the correction becomes a [[#T5 — Document request (upward)]] pair with a terminal state; and [[#R13 — Everything below rank 0 starts cold]], which ends it by the counterparty no longer existing in that context. The diagnostic half is real and worth having — `harness status` marks a live node with no open task as `unassigned`, and `harness spend` prices the exchange — but it informs a decision rather than making one.

### R7 — The name is cosmetic

Sessions are conventionally named `<project>-<node>`, and `harness spawn` sets that
at launch with `claude --bg -n`. It is a convenience for reading `claude agents`,
nothing more.

**Do not gate on it.** Claude Code owns the name: it derives one from the working
directory (`biblion2-2d`), auto-titles others from session content
(`verify-handover-refs`), leaves most sessions unnamed, and reissues the name on
resume. A mismatch is a warning; `--strict-name` restores the refusal for anyone
who wants it.

Position comes from git under [[#R1 — Position is derived, never declared]] and
occupancy from the worktree under [[#R2 — Occupancy is the worktree, not the session]].
Neither needs the name, which is exactly why it can be allowed to drift.

**No node branch may be a path prefix of another.** Git refs are files, so
`refs/heads/dev` blocks `refs/heads/dev/ui` from existing at all — in either
order. Separate node names with anything but `/`: `dev`, `dev_ui`, `w_m1`.
`harness whoami` refuses a tree that breaks this rather than letting it fail at
the first `git worktree add`.

### R8 — The platform contract fails loud

The harness reads Claude's own state. It never writes it. Those files and variables are internal and may change without notice, so every dependency is asserted before anything else runs, and a failed assertion **refuses to operate** rather than degrading.

| id | asserted | why it matters |
| --- | --- | --- |
| `C1` | `CLAUDE_CODE_SESSION_ID` is set and is a UUID | identifies this session *now*; it is reissued on resume |
| `C2` | `~/.claude/projects/<slug>/<id>.jsonl` exists | proves the id is the real session, not a bridge artefact |
| `C3` | `CLAUDE_PID` is set and live | second liveness source, independent of `ListAgents` |
| `C4` | `slug(cwd)` resolves to an existing project directory | the anchoring rule still holds |
| `C5` | `claude agents --json` returns an array listing this session, with the expected fields | the liveness oracle is readable |
| `C6` | those rows carry `state` | a session **stopped** at a prompt is distinguishable from an idle one |

`C6` is its own id and not part of `C5` on purpose. `C5` failing means the harness cannot identify a session at all and must stop; `C6` failing means it can, but has gone blind to the one condition only a human can clear. That is a different fault, not a smaller one, and sending its reader after `C5`'s cause would waste the trip — the same *one word, two contracts* rule this note applies to exit codes.

Refusing is the correct response because the failure is silent otherwise: a harness that mis-identifies a session can let two of them hold one node, and that is the one failure the lock exists to prevent. The check runs at claim time, not once at install.

### R10 — Propagation spawns sessions, and can stop them

One human starts the rank-0 session. It builds the tree and launches the rest:

```
harness spawn [--dry-run]        one `claude --bg -n <project>-<node>` per
                                 unoccupied CHILD of the caller
harness spawn <node> --empty     start a node that has nothing briefed
harness stop  <node> ...         end those sessions
harness stop  --children         reap a whole layer
```

**A node starts its own children and nobody else's, and until 2026-09-08 it
could start anything.** Bare `spawn` targeted every node in the tree with a
worktree, with no test of who was asking — so a rank-1 lead ran it and started a
member two ranks away under a sibling lead. Measured: `dev` ran bare `spawn` and
started `panel_1`, which is `panel`'s child, has never been `dev`'s business,
and had nothing briefed for it. Every other downward command was already gated
this way — `brief --for` refuses a node that is not yours — and `spawn` is the
one that starts a *session*, so it is where the gate mattered most and it was
the one that had none. The operator is not a node, legitimately drives the whole
tree, and is exactly the caller with no session id; that is the one case that
keeps the old reach.

Each spawned session is a real session with its own id, lock and row in the
session table. It is told nothing about where it is: it derives its position from
git under [[#R1 — Position is derived, never declared]] and claims it.

**Names set at launch are stable.** A session named with `-n` records
`nameSource: peer`, and it survives being attached to and worked in — verified.
Names the system chose for itself do not: `derived` names come from the directory
and `auto` names are titled from content, and a resumed conversation can return
under a new id with a new name. That is why the check in
[[#R7 — The name is cosmetic]] warns by default, and why `--strict-name` is
reasonable for a tree the harness spawned itself.

They are attachable: `claude agents` to view, `claude attach <id>` to open one in
a terminal, Ctrl+Z to leave it running.

**Background sessions can stall on permission prompts** with nobody to answer.
Expect the first propagation to need attaching to each session once.

### R11 — Orientation is a hook in the enrolled repo, not a global one

`harness scaffold` writes this into the target repository's own
`.claude/settings.json`, alongside `.harness/`:

```json
"SessionStart": [{
  "matcher": "startup|resume|compact",
  "hooks": [{ "type": "command", "timeout": 10,
              "command": "~/.claude/harness/bin/harness whoami --quiet --no-check" }]
}]
```

**Scope is the whole point.** Claude Code offers three: `~/.claude/settings.json`
is every project on the machine, `.claude/settings.json` is this project and is
committable, `.claude/settings.local.json` is this project and gitignored. A
harness hook has no business existing outside an enrolled repository, so it goes
in the second and travels with `.harness/tree.json`. In every other project the
command is never spawned at all — not run-and-silent, simply absent.

`SessionStart` is one of **four** events whose plain stdout on exit 0 is added to
the model's context — the others are `UserPromptSubmit`, `UserPromptExpansion`
and `PostModelSwitch` — so no JSON envelope is needed; `whoami` output is the
payload. Everywhere else, including `Stop`, exit-0 stdout goes to the debug log.
Checked against the reference 2026-09-08; this note said *three* and did not say
which, which is a count nobody can act on.
`--no-check` skips the cosmetic name warning, which would otherwise cost a
`claude agents --json` call at every session start.

**The `resume` matcher is not decorative.** A resumed conversation is issued a new
`CLAUDE_CODE_SESSION_ID`, which would orphan its own lock; re-running `whoami`
lets it reclaim under [[#R2 — Occupancy is the worktree, not the session]].
`compact` is included because a compacted session may have lost its position.

**Do not reach for the `if` field to scope a global hook.** It is evaluated only
on tool events — on any other event, a hook with `if` set never runs at all.

`SessionStart` cannot block: exit 2 shows stderr to the user and startup proceeds.
That is the right shape — orientation should never be able to stop a session.

### R9 — Enrolment takes two keys

Nothing is enrolled by default. A session participates only when **both** are present:

| key | where | meaning |
| --- | --- | --- |
| logical tree | `.harness/tree.json`, in the repo | this project defines a role tree |
| local binding | `~/.claude/harness/<slug>/binding.json` | *and this machine has joined it* |

Cloning a harness repository does not enrol you; adding a binding to a project with no tree means nothing. Opting out is deleting the local binding — immediate, machine-local, and it touches no shared state.

Outside an enrolled project the `harness` skill establishes that in one step and stops. Claude everywhere else is unaffected.

### R5 — Four skills, composed by direction

Role content is not disjoint — a middle lead is a member upward and a lead downward — so the split follows direction of travel, not role name.

| skill | loaded when | covers |
| --- | --- | --- |
| `harness` | always | R1, R2, enrolment, invariants, routing |
| `harness-upward` | the node has a parent | T2, T3, T4 present, T5, T7, T10, T11 propose, T12 ask |
| `harness-downward` | the node has children | T1, T4 integrate, T5 relay, T7, T8, T11 review, T12 answer |
| `harness-root` | rank 0 only | applying pairs, T9, manifest, guards, the scope registry |

```
··leaf·······→··harness + upward
··mid-lead···→··harness + upward + downward
··top lead···→··harness + downward + root
```

A leaf never loads lead instructions, which is what keeps a lead's context shallow under [[#I9 — The lead owns the seams]].

### R6 — Only full sessions hold nodes

Only a full session participates in the tree. A node is owned by a session with
its own id, its own lock and its own row in `claude agents --json`.

**A subagent cannot hold a node.** Measured: it reports its parent's
`CLAUDE_CODE_SESSION_ID`, its parent's `CLAUDE_PID` and its parent's working
directory. It takes no distinct lock, appears in no session table, and cannot be
attached to. So it cannot be a member, cannot claim, and cannot present work.

**This is not a ban on subagents.** A session may still spawn one when asked, or
to answer a bounded question — a search across files, a quick lookup — and fold
the answer into its own work. That subagent is a tool the session used, not a
participant: the node, the lock and the commits stay with the session. What is
forbidden is *substitution* — handing a node, a claim or a transaction to
something that cannot be identified or attached to.

**Workflows are not used.** Deterministic scripting buys nothing here, and adds a
script to maintain and a layer to debug.

A lead integrates its children itself, sequentially — one node is one branch and
one index. It needs no fan-out to verify: under [[#I5 — Checks run to completion]]
a member runs the checks its change touches and presents the report, a lead
runs the full set once after merging, and the only other checks a lead runs are
the absent member's during [[#T7 — Conflict escalation]].

### R12 — Model and effort are attributes of the node, not the operator

A node records what it should be run as. `spawn` passes `--model` and `--effort`
to each session it launches; `whoami` prints the pair so a session can see what
it was meant to be, and a human can see when it is not.

```json
"dev_ui_1": {"branch": "dev_ui_1", "parent": "dev_ui", "kind": "code",
             "effort": "medium"}
```

Absent from the node, it falls to a default chosen by **role**, so a tree can
rename every node and still get them:

| role | model | effort | why |
| --- | --- | --- | --- |
| root (rank 0) | `opus` | `high` | applies every document change, writes rulings, holds the widest view |
| lead (parent *and* children) | `opus` | `medium` | holds every child's report and both sides of a conflict it did not create |
| member (leaf) | `sonnet` | `medium` | one task, one worktree, then recycled — see below; effort stays medium because coding is the one steep effort curve |

**A member runs Sonnet for a reason about the plan, not about the work.** On a subscription, Opus has its own weekly window that resets separately from the others. So a member on Opus is not spending *less* than its lead — it is spending the **same scarce pool** that the lead and rank 0 need, and the tree competes with itself for it. Moving members off does not reduce tokens by one; it moves them to a pool nothing else in the tree draws on.

That is a different claim from *Sonnet is good enough for coding*, which this note does not make and has no evidence for. The nearest measured result is dollar-matched rather than tier-matched, is **conditional on a strong verifier**, and gets its saving from sampling five times and selecting — not from running one cheaper worker once. What the design does supply is the verifier condition: a complete brief at [[#T1 — Task assignment]], acceptance that is a measurement rather than an assertion, the repo's own instrument suite, and a lead's read before integration at [[#T4 — Integration (fast-forward up)]].

**Leads and rank 0 stay on Opus.** A lead writes its children's briefs, and brief quality is where the 39% penalty lives: a bad split costs more than the tier saves, and it costs it downstream where it is hardest to see.

**The mark records what actually ran** (`_model`, `_effort`), because a per-node model change otherwise produces two numbers nobody can attribute. `--done` prints it beside the band verdict and `spend` puts it in the header, so the question this table answers by judgement — whether a cheaper member causes enough rework to cost more turns than it saves — becomes one the ledger answers by subtraction.

**No node uses a 1M window, and an earlier version of this note was wrong to.**
The argument was that context follows the view: a lead accumulates every child's
report ([[#I5 — Checks run to completion]]), both sides of a conflict it did not
create ([[#T7 — Conflict escalation]]), the seams between siblings
([[#I9 — The lead owns the seams]]), and every document climbing past it. That
accumulation is real and it is why documents travel rank by rank. It is not an
argument for a larger window.

The direct measurement is a null. Same model family at two window sizes, on
inputs that fit both, performed **"nearly identical"** — tested across three
pairs. A larger maximum *permits* higher occupancy; it does not improve
behaviour at a given occupancy. And occupancy itself is what costs: holding
retrieval perfect and masking irrelevant tokens still degraded performance 13.9
to 85% as input grew. The wide window buys headroom, and headroom is the thing
that hurts.

**A member is the opposite by construction.** One short task
([[#I8 — Tasks are short]]) in one worktree, ending at a commit. It is not given
a large window because it is not asked to hold anything; instead it is recycled
([[#R13 — Everything below rank 0 starts cold]]) so it never accumulates one.
`opus[1m]` resolves to `claude-opus-5[1m]`; plain `opus` to `claude-opus-5`. Both
were checked against the CLI rather than assumed.

**Effort does not simply fall with rank, and an earlier draft of this note had
it wrong.** The argument was that judgement falls with rank by design — a leaf is
handed its scope ([[#T1 — Task assignment]]), has its approach approved before the
first commit ([[#T11 — Approach review]]), does not own the seams
([[#I9 — The lead owns the seams]]), and escalates rather than resolves
([[#T7 — Conflict escalation]]) — so a leaf was set to `low`. The reasoning is
still sound; the conclusion was not, because effort does not track judgement. It
tracks *workload shape*, and Anthropic has measured those curves:

| workload | claimed |
| --- | --- |
| research / knowledge work | nearly flat: `low` gives up 1–3 points for a third to a half off; `medium` matches the default at 70–85% of its cost |
| long-horizon **coding** | steep: ~2 points at `medium` for half the cost, but ~8 points at `low` for a quarter |
| reasoning-ceiling work | every step buys ~2.4 rubric points; no free cut |

> [!warning] These figures are an unreproduced vendor claim, not a measurement
> They come from a guide bundled with the tooling, which is not publicly
> published and has never been independently reproduced. A literature search
> found **no** published accuracy-per-effort-level or tokens-per-level figures
> from any vendor or independent party. They may be correct; their status is a
> claim. Treat the direction as informative and the numbers as unverified, and
> replace them from closed ledger rows under
> [[#I10 — Cost is estimated, then measured]].

A member is a long-horizon coder. It sits on the one curve where `low` is
expensive, and it is the one role whose output nothing reviews — `T4` integrates
by fast-forward, which is mechanical; `T11` reviews the approach, not the diff;
the checks test behaviour, not quality. Paying eight points of pass rate at the
only unreviewed seam in the tree is the worst available trade, so members run at
`medium`. A lead's review and diagnosis is knowledge-shaped, where the curve is
flat and `medium` costs less for the same answer. Rank 0 stays at `high`, which
is also the platform default.

**The failure signal the harness already has.** Anthropic's cheapest measured
configuration is not a lower setting — it is *re-running failures* at a higher
one: everything at `low` with failures retried at the default solved ~93% for
~$0.70 per task, against 91.7% for $1.39 at the default throughout; starting at
`medium` solved ~94% for ~$0.95. That pattern needs a usable failure signal, and
the manifest's check set under [[#I5 — Checks run to completion]] is exactly one.
A lead whose child fails its checks can re-run the work harder without editing
the tree: `harness recycle <node> --escalate` restarts it one level above
whatever that node is set to, so the same command works at any baseline. It
saturates at `max` and says so rather than pretending a retry is available. Use
it for the saving, not the lift, and price in the doubled wall clock. A second
failure at a higher level is a finding — read it rather than escalating again.

**The split has a cost, and it is not zero.** Two models across the ranks are two
cache namespaces, and sessions in one repo share a static prefix, so that prefix
is cached twice. The measurement to hand is next door rather than on the nose:
`opus[1m]` against `opus` rewrote 12,521 tokens rather than reading them, while a
repeat on the same model read all 22,491 and wrote none. That was taken when this
note still put a lead on a wide window; the pairing it measured is gone and the
property it demonstrates — a change of model is a cold cache — is what applies to
`opus` against `sonnet`. Stated rather than hidden, and labelled as the near-miss
it is rather than passed off as the figure for the split actually in use.

Re-measure all of this from closed ledger rows under
[[#I10 — Cost is estimated, then measured]] rather than trusting the table.
Anthropic's own guidance is that the curve is per-workload *and* per-model, and
that a sweep should be re-run after any model migration or workload shift.

A misspelt effort is refused when the tree is validated, not when `claude`
rejects it — by then the session is already spawned and detached.

### R14 — A stopped session, and the viewer

**The platform could not tell you which session wants you, and now it can — the measurement expired and this note went on quoting it.** Measured 2026-08-31: `claude agents --json` carried `status` (busy/idle) and `state` (working/done) and nothing else, so a session stopped dead on a refused permission was indistinguishable from one that was working. Everything below was built on that.

Re-derived 2026-09-08: rows carry **`state: "blocked"`**. What it cost to keep the old reading is exact. `biblion2-dev` sat halted at a prompt for forty minutes holding three briefs written for it, while `status`, `idle`, `whoami` and the viewer all rendered it `idle` — the same word as free — because every occupancy call in the CLI read `status` and nothing anywhere read `state`. `recycle` would not even have refused it: the remedy was reachable the whole time and no instrument could see the condition.

This is [[#I13 — A measurement travels with the command that produced it]] landing in the worst available place. A figure written into prose ages silently; **this one aged into a premise**, and nothing re-derives a premise. So the assertion is now `C6` in [[#R8 — The platform contract fails loud]] — if the field ever goes away, the harness says so instead of quietly going blind again.

**One state, two situations, and the first reading of it prescribed the wrong remedy.** Measured 2026-09-08, an hour after the above: `biblion2-main` reported `blocked` because it had **ended its turn and was waiting for a reply** — prompting it cleared it at once, and attaching did nothing because there was nothing to approve. `biblion2-dev` reported the same value while genuinely **halted on a permission prompt**, for a compound `cd … && harness note …` command that matched no allow rule despite both of its halves being allowed.

The roster can't tell those apart; the session's transcript can (`stop_detail`, re-derived 2026-10-05, when every stopped session in the tree was the first kind). A turn that ended is a **wait** only when it messaged someone for an answer (owner, 2026-10-06: *waiting on* means the node has messaged another and is waiting for its response): its last `SendMessage` went to a session other than the one that opened the turn. It is drawn as one, inferred, on that session, with the wait colour on the branch — not as a fault. A turn that ended with no message, or whose last message answered whoever opened it, is **at rest**, not waiting (`stop_wait_on`); the old rule waited every finished turn on whoever spoke last, so a lane that woke for its doorbell and re-armed read as waiting.

**Held by is a different thing: another node has to act before this one can do anything.** A node is held when it has nothing in hand and its next task is gated `--after` a task that isn't closed (or `--not-before` a clock). The holder is always another node: a gate on the node's own task is followed to whatever holds that task, and dropped if nothing outside the node does; a gate on presented work names the worker's lead, whose sign-off is what's missing. Held is violet and dashed, a wait teal and solid, and neither is a fault. A tool call with nothing after it is a **permission prompt**, the only stop still shown as needing the keyboard, naming the tool and command. When the tail says neither, every surface says **waiting on you** and offers both remedies cheapest first. The first draft said *halted at a prompt* and told the operator to attach, which was wrong for the commoner of the two and sent them at the wrong action twice in a row. **A queue that confidently prescribes the wrong action is worse than one that says it does not know**, and it is the same failure as a check that passes for the wrong reason: the output looks like knowledge either way.

**It is `stopped` in the record and `waiting` on every surface, never `blocked`.** `harness blocked` is already a record asking the operator to widen a permission, raised deliberately by a session that is still running and often still working. A session the runtime has halted is a different fact about a different thing, and one word over two contracts is a fault this project has already paid for. The runtime's value is read at exactly one boundary.

**Traffic between nodes is drawn on the nodes, never as an owner's item.** A lane waiting on its lead, a lead asking for unrequested work to be staffed: rendering those as items for the owner asks them to adjudicate a conversation they are not in. The owner said what that looked like: *"it all looks like noise if these are the messages going between nodes."*

So node traffic is drawn **on the node it is directed at, naming the node it came from**, in the muted colour the tree already uses, never the warning colour, because it is not a fault:

```
dev_2   ← dev   APPROVAL     Read build/graph.dot back and assert its shape.   approve
dev_2   ← dev   UNANSWERED   asked dev and stopped — dev is not running        spawn
```

One line: direction, kind, the point, the verb. The full text is one click away. **Rich about what it is, short about saying it** — the reverse of the first attempt, which was long about why the category exists and silent about which item this was. The paragraph explaining what a grant *is* was identical on every grant; it is said once, in the viewer's rules panel, and never again per item.

**Recycling is not the remedy and looks exactly like it.** A replacement starts cold, walks the same path and stops at the same prompt, so the sweep costs a session and changes nothing — while discarding whatever the halted one was waiting to be told. `recycle` and `recycle --cold` now refuse a stopped node and name `claude attach` instead; `--force` still overrides, and says what it is throwing away.

**The owner queue this section once described is gone (2026-10-05).** `harness needs`, its cache, the `notify` hook and the viewer's "waiting on you" column held path grants, approvals and stalled sessions — none of them the owner's — and three questions nobody answered. Blocks, grants and approvals stay between sessions; the owner channel is being redesigned (`harness/design/owner-channel.md` in the setup repo).

**The viewer's header shows the account's 5h and 7d limits, with their reset times** (owner, 2026-10-09). Claude Code hands these only to a statusline (`rate_limits` on its stdin); no transcript or session file carries them. So the statusline saves the latest copy to `~/.cache/harness/usage.json` (write-then-rename), and the viewer reads it through `/api/usage`, apart from `/api/state` so a ticking percentage never redraws the tree. A window whose reset time has passed shows "—", because its saved figure is stale, and a copy more than ten minutes old says how old. 80% and above is coloured.

**The statusline used to carry a count and no longer does.** It was wrong in the one way a statusline cannot be: it rendered in **every** session on the machine, enrolled or not, so a block raised in one project shouted at every unrelated shell — and there is nothing to be done about it from where it appears. The statusline still shows tree **position**, which is a fact about the repository you are standing in and stops at its edge. The queue belongs where the commands that clear it are.

**The viewer does not seize the browser.** It prints its URL and opens nothing unless asked with `--open`. It starts often — from `harness gui`, from a restart after an edit, from a second port when the first is taken — and a viewer that takes the screen every time is one that interrupts whatever was on it.

Granting closes the block it answers. A queue that keeps naming something already dealt with is a queue nobody reads, so the two records are kept in step rather than left to a member to tidy up after the fact.

**The page does not redraw while there is something to lose.** A cursor in a comment box, or an unsent draft in one, outranks a fresher tree: the poll fetches, notices, and skips the render, saying so in the header. The identical-payload check does not cover this on its own — a session flipping between busy and idle is a *genuine* change and arrives every few seconds, so the panel would legitimately redraw and legitimately eat a half-typed sentence. Drafts are also held by box identity and restored after any render that does happen, which covers the case where the redraw was not the one you were in.

**A poll updates named elements; it does not repaint the page.** Everything volatile carries `data-live` with a stable key, and a poll may replace those and nothing else — comparing content first, so an unchanged region is not even touched. A textarea mid-sentence, an expanded item, a text selection and the scroll position all survive **by construction**, because nothing reaches them.

This replaced an exclude list, and the direction matters. The first attempt repainted everything and then tried to put back what it had destroyed: the open set, the drafts, a pause while the cursor was in a box. That fails the wrong way — forget to exempt something and it is eaten silently, which is what happened twice. An include list fails the *right* way: forget to tag a volatile field and it goes stale on screen, where it is visible. Only a change in the **shape** of the tree rebuilds — a node appearing, an item clearing — and that path restores drafts and expansions by key.

**Copies drift, and nothing announced it three times in one day.** The guard in a project repo, the running viewer, and every installed skill each fell behind their source silently. `install.sh` now stamps `~/.claude/harness/VERSION` with the source path and its commit; `harness doctor` compares them as its first arm, because a stale install makes every arm below it a measurement of the wrong thing; and the viewer raises it as an item owed to the operator.

**Comments on a brief prompt the lead who writes it, not the lane it is for**, by the same rule: only the party who can fold a comment in is asked to act on it. The lane still sees comments when it reads its brief — it is simply never prompted to act on one, because only the brief instructs.

The box is rendered inside the expanded item rather than behind a click on some other surface. An affordance one click away on a page the reader is not looking at is one that does not get found, which is what the first version was: one clickable chip on the whole page, and none on the four things actually waiting.

**Comments are the one thing the viewer writes, and the exception is deliberate.** Clicking a task opens its brief, when it was opened, which session opened it, and every comment on it, with a box beneath. A comment appends to the mark record and is never edited ([[#I6 — The ledger is append-only]]). It goes there and not into a message because **a message dies with the session that receives it**: the next occupant of that node starts with none of it, while the mark outlives a recycle by design.

The write is *delegated*, not implemented: the server shells out to `harness note --add` in the project, so the viewer gains no ability the CLI does not already grant and there is one definition of what a comment is. It strips `CLAUDE_CODE_SESSION_ID` before doing so, because a comment typed into a page was typed by a person, and a server launched from inside a session would otherwise sign it with that session's id — a false attribution in the one record that exists to be trusted.

Because the server has no authentication, a page merely *visited* in the same browser could otherwise POST to it. The write requires a custom header, which forces a CORS preflight cross-origin that is never answered, and the `Origin` is checked as well for anything not playing by browser rules. Reads whitelist rather than sanitise: a project slug must **be** a directory that exists and a task must **be** a file already in the listing, so nothing is ever joined from input and there is no path to traverse.

**Unclaimed task records reach rank 0 at orientation, not only on request.** `whoami` prints a line for them, and one for waiting blocks, at rank 0 only and only when the count is non-zero — the hook runs on every start, resume and compact, so a line that is usually absent costs nothing and a line that appears has earned its tokens.

**`harness gui` is a viewer, and holds no authority.** A prototype: one stdlib file, no build step, bound to `127.0.0.1` only, on port 8791 — not 8787 or 8888, which belong to RStudio Server and Jupyter, both long-running services someone starts once and forgets. The default walks upward when it is taken; an **explicit** `--port` is honoured exactly or refused, because being quietly moved off a port you named is worse than being told. It reads `tree.json` for structure, `index.json` for worktree paths, the locks, the open marks and the open blocks, and renders every project on the machine as one indented tree with busy/idle per node and a clickable attention panel. It never claims, writes or decides — so [[#R4 — No arbiter process]] is untouched, and it can be killed mid-render without anything in the harness noticing. It also has no authentication of any kind, which is why it never binds anything but loopback: it exposes worktree paths, session names and every open block.

**A node with a session and no mark is not idle, and must not be labelled as though it were.** The view said `unassigned`, which reads as *nothing is there*; what it means is that the session is working and the **harness has no record of on what**. It says `no task record` now, in the viewer and in `status`, because the distinction is the whole point of [[#I10 — Cost is estimated, then measured]]: an unmarked task is one whose cost can never be a subtraction.

**An open mark that names no node is reported, never guessed.** Marks gained a `_node` field on 2026-08-31, and the six written before that were silently dropped by every reader — so their nodes read as having no task while their sessions had one. Two kinds now, kept apart: a mark naming a **trimmed** node is stale and `harness trim` closes it; a mark naming **nothing at all** cannot be attributed, only reported and closed by hand. Inferring which node a pre-field mark belonged to would put a number in a ledger that exists to be trusted, on the strength of a guess.

**Occupancy has three states there, not two.** A failed roster read used to become an empty roster, so a tree of working sessions rendered as a tree of empty nodes — the same "couldn't check shown as clean" fault the `review` command had, in a second place. `null` now means *unknown*, distinct from `[]`, and the page says so in a banner rather than drawing conclusions. Two sessions in one worktree are also shown as two: keying occupancy on a dict of cwd silently kept the last one and reported the breach as ordinary occupancy.

**Depth runs down the page, not across it.** Root at the top, siblings side by side beneath their parent, connectors drawn in CSS. The roster is cached for one poll interval, because each read costs 0.55s of process spawn and the page polls every three seconds — without it, every open tab is a `claude` process every three seconds forever.

### R15 — Orientation is edge-triggered, and change is what travels

**The cost of telling a session something is not paid once.** A line printed at turn *k* of an *n*-turn conversation is resent on every turn after it, so it costs roughly *n − k* times. Periodic orientation is therefore **quadratic in session length**, and that one fact rules out the obvious design — print the queue every so often — before any other consideration. What is left is the only shape that works: **report a change, never a state.** A session already told about an item does not pay for it again, the bill is *O(changes)* rather than *O(turns)*, and a quiet tree costs nothing at all.

**The scope is injected, not looked up** (owner, 2026-10-06: scope comes first from the harness project description, then the full documentation). `scope_block` is the charter (description and every feature in full, in the owner's order) then the project's doc index; it opens every spawn, recycle and reset prompt, is appended to the intermediary's and documenter's system prompts (rebuilt at each start), and `whoami` prints it at start, resume and compact. **The owner can halt the tree:** `harness halt --why` (refused inside any session) stops spawn, recycle, new briefs, task opens and new checks and test jobs; the runner finishes its job and exits; every node is rung and its Stop hook says it once per halt; orientation and the GUI show it; `harness resume` ends it. Two nodes ringing each other four or more times each way in an hour show in rank 0's orientation as a loop.

This is [[#R11 — Orientation is a hook in the enrolled repo, not a global one]]'s existing rule — *a line that is usually absent costs nothing and a line that appears has earned its tokens* — applied to the whole surface instead of to one hook.

**Three channels, and each is chosen by what it can reach.**

| channel | reaches | costs |
| --- | --- | --- |
| `UserPromptSubmit` → `harness hook-orient` | the session, every turn | nothing unless something changed |
| the delta footer after any harness command | the session, while it works | nothing unless something changed |
| `Stop` → `harness hook-stop` | the session, by **blocking** it | a turn, so it is reserved for work that is owed |
| `PostToolUse` → `harness-mail` | the session, mid-turn | nothing unless it has doorbell mail |

**A block is top-level JSON: `{"decision": "block", "reason": "..."}`.** Until 2026-10-06 every block `hook-stop` printed was nested in `hookSpecificOutput`, which Claude Code ignores for `Stop`: main's transcript showed 359 turn ends, each `preventedContinuation: false`, so no nag in this table's third row ever reached anyone. Every block now goes through `stop_block`, and blocks speak only to the node's own session (the one in its lock), never to an intermediary, the documenter or another session in the same checkout.

**Doorbell mail is delivered by hooks, and the project's ringer wakes an idle session** (log 134, owner 2026-10-10; before that each session kept a background waiter armed and re-armed it after every wake). A `ring` (and everything that rings: a presentation, a hold, a finished check, `ask --to`) writes a file to `doorbell/<node>/inbox/`, with a priority. The node's own session gets it from a hook: after a tool call (`harness-mail`, a stdlib-only script, because it runs after every call; high mail only), at its turn end (`hook-stop` blocks with it, even right after another block; only when something in it asks for action), or at a prompt (`hook-orient`). Each message is claimed by an atomic rename, shown once and logged to `delivered.jsonl`.

**The ringer.** A hook cannot wake an idle session, so one `harness ringer` per project does (a lock file keeps it to one; `ensure_ringer` starts it wherever mail is written and from the prompt and Stop hooks, so no session has anything to arm; it exits after ten minutes with no node session alive). It needs no model: every Claude Code session binds an inbox socket (`messagingSocketPath` in `~/.claude/sessions/<pid>.json`), and the ringer posts one JSON line to it, `{"type":"user","message":{"role":"user","content":"harness ringer: N unread message(s) ..."}}`. An idle session starts a turn on that line and its prompt hook prints the mail; the ringer itself never takes mail. Measured 2026-10-11 on a throwaway session: a ring to an idle node woke it one second later with no waiter running; an FYI woke nothing in its first seconds; a low message sent as its turn ended woke it 60 s later. Each tick (1 s) it decides per node with `ringer_plan`:

| Receiver | high (default) | low | fyi |
|---|---|---|---|
| busy | left to its hooks: shown after its next tool call | held until its turn ends | held |
| idle | woken now | woken once idle 60 s (`LOW_IDLE`) | woken once idle 5 min (`FYI_IDLE`), so it is always read |
| stopped while idle (no process, claim held, last turn ended) | resumed with `claude --bg --resume`, not while halted | the same | no |
| no session | nothing; the "down" row (log 128) covers it | | |

A wake whose mail is still unread after 90 s is sent again at 1, 5 and 15 minutes, and then the node is `unwoken`: its lead gets a row and the viewer flags it, so a wake that fails does not fail quietly. The ringer also raises the nudge the waiter used to (a node that has waited on an idle one past `NUDGE_AFTER`). **Priorities:** `harness ring <node> [--low | --fyi]`. FYI mail and a note a session sent itself are shown without the demand to act; a ring signed with a node's name from a shell in its checkout is the owner speaking, not a note to self. `ring` says what will happen ("the ringer wakes it now", "held until its turn ends", "an FYI asks for nothing"). An FYI first never woke anyone; the owner pointed out the same day that one sent to a node nothing else prompts would never be read, so it now wakes an idle node after five minutes (2026-10-11). **Retired:** `harness doorbell` with no flags says so and starts nothing; the Stop hook's "doorbell not armed" block is gone; `--read`, `--again` and `--status` stay. main's eight points (log 134): re-arming, the wrong way to arm succeeding, silent failure, the contentless wake and stray waiter processes are gone with the waiter; two routes for one message is now one (hooks deliver, the ringer only wakes); obligation welded to delivery and the hidden cost of sending are answered by priorities and by `ring` naming a pending reset. Not known yet: whether Claude Code stops an idle background session after about an hour now that no waiter keeps a shell running in it; if it does, mail resumes it. The `PostToolUse` entry dates from 2026-10-06; a repo scaffolded before it lacks it until rank 0 runs `harness scaffold --force` and commits `.claude/settings.json`, and `harness doctor` says so.

**A waiting doorbell is not work.** Claude Code reports a session with a background command running as `busy`, so every idle node with an armed doorbell read as busy (true of any background command; the waiter itself is retired, log 134). `agents_json` corrects it: a `busy` row whose transcript ends in a `turn_duration` record (walking back past titles, queue bookkeeping and system notes, before any message) is idle, and keeps `reported_status: busy`. Every consumer (spawn, recycle, nudges, `ring`, the GUI) reads the corrected row.

`Stop` cannot do the first job. Exit-0 stdout becomes context for four events — `UserPromptSubmit`, `UserPromptExpansion`, `SessionStart`, `PostModelSwitch` — and goes to the debug log for everything else, `Stop` included. So a `Stop` hook reaches a session only by refusing to let it stop, which is the right instrument for a duty and the wrong one for news.

**The footer is the cheap half and it is nearly free.** A working session runs `mark`, `brief`, `review`, `integrate` all day and is already reading their output, so orientation rides along for the price of the lines it actually prints — none, unless the queue moved. It is deliberately silent after a refusal: the reader is dealing with the refusal, and a queue notice underneath it is noise at the worst moment.

**A debt is not news, and treating it as one caused exactly the failure this section was written to prevent.** The rule above — report a change, never a state — is right for something that *happened* and wrong for something you *owe*. An unsigned presentation does not stop being true because the lead has been told once, but the id is stable, so it was reported once and suppressed forever. Observed on a live tree: `dev` repeatedly failed to sign off its children, because it learned of the debt and then held a long exchange with `main`, and nothing said it again.

So obligations — an unsigned presentation, an idle child with work queued, a pending approval, an answered block with no task, a child stopped waiting on you, a brief handed to you and unactioned — **re-report every ten minutes while they persist**. Everything else still fires once. The cooldown is what keeps that from being a per-turn tax: a debt costs one line per ten minutes, not one line per turn.

**And the session is told to write it down, by name.** The harness cannot hold a thought for a session, and nothing it prints survives forty turns of somebody else's conversation. What does survive is the session's own todo list, so orientation and the delta both say `TaskCreate` explicitly at the moment the debt is learned, and the `Stop` hook repeats it when it blocks. A rule that depends on a participant staying alert is what this design exists to remove; naming the one structure that remembers for them is the nearest available substitute.

**Keyed on the session, not the node.** A recycled session has been told nothing, which is exactly right — [[#R13 — Everything below rank 0 starts cold]] means it starts cold by design and its orientation is where it learns the lot. `whoami` marks everything it printed as told, so the next command does not repeat it; a notice that arrives twice running is one a reader learns to skip, which is the failure this exists to prevent.

**An item that clears and returns reports again.** Only additions are printed — *X is gone* is not actionable — but the comparison is on a set, so something that comes back is news the second time too.

**Rank 0 is why this was needed.** It holds more queues than anyone — pending approvals, answered blocks that produced no task — and reads them least often, because orientation fires on startup, resume and compact and rank 0 is the one node [[#R13 — Everything below rank 0 starts cold]] never recycles. Measured on a live tree 2026-09-08: its lock had gone **37 hours** without a refresh, which is 37 hours of that queue read exactly once. `lead_owes` already gave it a per-turn heartbeat for what it owes *downward* and nothing for what it owes *outward*, so the queues only it could clear were the ones with no heartbeat at all. That is now a `Stop` row of its own, aged like the others.

**It reads local JSON and nothing else.** No roster, no `claude agents --json`. This runs on every prompt in an enrolled repository, and 0.55s there is a tax on typing.

### R13 — Everything below rank 0 starts cold

A session is ended and a fresh one started on the same node once its work has
landed. `harness recycle <node>`, `--children`, `--idle` or `--cold` does it; a
node drives it for its own children.

**"Landed" has no meaning across an edge that never integrates, and reading it
as unlanded work deadlocks the rule.** Code does not reach the document branch —
the guard refuses it there — so for the top of the code subtree the count of
commits its parent has not taken is not a backlog, it is the project, and it
only grows. Measured on biblion2 2026-09-07: `harness recycle dev` refused with
*576 commit(s) not yet in main — present them first*, a condition no action can
ever clear, while orientation went on recommending the recycle and `--idle`
swept nothing. The harness derives the exception from `kind` rather than asking
anyone to declare it: a **code** child of a **doc** parent proves no
containment; a doc child of a doc parent still does. It says so on the line
rather than passing quietly, because the number is large and rising and a
reader who checks by hand should not conclude the tool missed it.

**It applies to leads, not only to members, and that is a change of scope rather
than of mechanism.** A lead used to be worth keeping because it held what nobody
else did: which briefs it had written, which blocks had been answered and what
they produced, what its children were carrying, which figures it had measured.
All of that is a record now — the charter, briefs and their queue, marks with
derived state, findings, facts, block consequences — so a fresh lead **reads it
back instead of remembering it**, and the only thing lost by replacing one is
context it should never have been the sole holder of. A rank-1 lead should
therefore be recycled often, not exceptionally.

**Rank 0 is the single exception, and the reason is narrow.** It is not that it
holds more; it is that it holds the one thing no record reconstructs — the
conversation with the operator. Everything else rank 0 knows has been moved out
of its transcript deliberately, which is what makes the exception small rather
than a licence.

**The parent is the actor, so the parent is told.** A session cannot recycle
itself, so orientation prints the line on the node above: `recycle dev —
nothing in flight`. It fires only when no child holds an unpresented mark, so a
node mid-task is never offered up.

It is a teardown and relaunch, not a clear. A background session cannot clear
itself, and a session that stopped itself could not start its replacement — so
the parent does both. It stops, it does not `claude rm`: `rm` deletes the job
folder, whose `tmp/` may hold a file a record cites. It never deletes a worktree
made with `git worktree add` (measured 2026-10-05: list entry and job folder
gone, node worktree untouched), so `harness sweep` uses it — on each session it
archives, and with `--sessions` on every ended `<project>-<node>` session the
list still carries — skipping any whose job folder a record cites. `claude stop`
alone left 197 ended sessions listed on one tree in a month.

**Between tasks, not between sessions.** A member's queue is the ordered briefs written for it that no mark has opened. Its lead sets the order (`harness queue <node> --order`), because a member picking its own next task is picking its own work. When a task is signed off, the harness computes what happens to the node and prints it with the command already written: recycle, or carry on. Leaving that to be remembered is how one session ends up doing four tasks on one accumulating context, which is the thing this rule exists to prevent.

**Priority is rank 0's; authorship is not.** A lead orders any queue below it: its children's, a sub-lead's, and that sub-lead's lanes' (owner, 2026-10-09: dev had to be able to reorder dev_tests' lanes). **Rank 0 orders anywhere in the tree.** A lead that orders past a sub-lead rings it with the new order and the reason, so it never briefs or sequences on the old one. This is deliberately a wider reach than a lead has over briefs — writing a grandchild's brief is refused because it skips the translation a rank exists to perform and rebuilds the drip feed one level down, whereas reordering changes no brief's text at all. It says which of them matters first, and what matters is rank 0's: it holds the charter, and it is the one talking to the operator.

**Reaching past a rank needs a reason, in both directions.** A lead reordering a grandchild's queue must give `--why`; the lead wrote those and sequenced them for a reason, and a change with none reads as noise and gets changed back. The same rule applies downward: once a higher rank has ordered a queue, the lead cannot silently undo it — it must give a reason too. It is not refused, because the lead may know a dependency rank 0 does not, and the harness has no way to tell a correction from an override. Both are recorded, the stamp always names whoever ordered it **last**, and the other party reads the same queue.

**One ordering mechanism, not two.** There is no per-brief priority field beside the sequence. Two authorities setting order would fight, and the loser would be whichever ran second — an ordering that changes depending on who looked at it last is not a priority.

**Coupling is the exception, and is justified in writing.** Two tasks may be declared to run in one session (`harness brief <b> --with <a> --why "..."`) when the context the first built is worth more than the reset the second would get. The `--why` is required and refused when empty, because the default is the evidenced one and an exception with no stated reason is indistinguishable from forgetting. A coupled task holds no queue position of its own — it is reached through its predecessor or not at all, and ordering one directly is refused.

**A completion carries itself through.** Signing off a task recycles the node onto the next thing in its queue, in the same act. Leaving the recycle to be remembered is what stranded a finished hand-off: the member had presented and stopped, the next task was queued, and the only thing between them was a command nobody ran. `recycle`'s own guards still apply at that point — a dirty worktree or an open unpresented mark refuses exactly as it would on the command line — and `--no-recycle` opts out. Where nothing is queued, nothing starts; a fresh session with no task to open is the state [[#T15 — Acceptance is not a decision]] exists to prevent.

**Presenting is enforced at the only moment it can be.** A member that finishes and stops runs no harness command, so nothing the harness prints can reach it — every other surface here waits to be asked. The `Stop` hook fires exactly there. When a node below rank 0 holds an open mark that was never presented **and there is work to show for it**, the stop is blocked once with the command that ends it.

**Evidence is required, and one nudge is the whole of it.** A mark opened and not started is a lane that has not begun, and blocking that would trap a member waiting on something; so the test is that HEAD has moved since the mark was opened, or the worktree is dirty. `stop_hook_active` says a block already happened this turn, and the hook allows immediately when it is set — a member gets one nudge and may then stop, which is what keeps this a reminder rather than a trap.

**A hook that runs on every turn must fail silently, not loudly.** It prints nothing on the allow path — which turns out to be right for a better reason than the one given here. This note said exit-0 stdout becomes context in every turn; checked 2026-09-08, `Stop` is not one of the four events that happens for, so its allow-path stdout goes to the **debug log** and reaches nobody. A `Stop` hook can only reach a session by **blocking** it. That makes it the correct instrument for work that is owed and the wrong one for news, and it is why orientation-by-heartbeat lives on `UserPromptSubmit` instead — see [[#R15 — Orientation is edge-triggered, and change is what travels]]. It is silent outside a git worktree, outside an enrolled project, on a branch that is not a node, and on unparseable input. `Ctx()` raises `SystemExit` rather than an `Exception` when it refuses, which an ordinary guard does not catch and which would have written a notice into every transcript on the machine, forever.

**The same hook enforces the other direction, and it is the harder one.** Upward reporting is a single act by the party that just did the work. Downward, a lead owes two things it can easily never notice, because neither is visible to the child and neither can be done by it: a presentation it has not signed off, and a child standing idle with work already written for it. This applies to **rank 0 as well** — main is `dev`'s lead — which is why every row is aged past a threshold, so a conversation with the operator is not interrupted over a child idle for ninety seconds.

**Ageing is what separates "has not got to it" from "is not going to".** A presentation seconds old is a lead mid-review; a child idle for a moment is one being recycled. Idleness is measured from whichever is later, the child's last closed task or the moment the work was written for it — a queue nobody has started is not idle from the instant the brief is saved.

**A child with an empty queue is not this rule.** That is a lead owing a *brief*, which is a larger act than a command, and blocking a stop over it would trap a lead legitimately waiting on something above it. The rule fires only where a single named command clears it.

**The second chokepoint needs no hook.** `harness mark` refuses to open a task while this node holds unpresented work with evidence in it — opening a second task would leave the first invisible to everyone above. That one fires for anybody who does carry on working, including through a recycle.

**Presenting releases the node.** The claim is on the worktree, and a member that has presented has nothing left to write there, so holding it only stops the lead refilling the node. It was a separate command, and it was the one that got skipped.

**A presentation is a record with no delivery, and that is the one gap nothing else covers.** The lead learns of it at its next harness command, and a lead that is idle or absent runs none — so a finished hand-off sits unnoticed while the member that finished it stands in the node. Nothing can push ([[#R4 — No arbiter process]]). What can be done is tell the rank **above** the lead, which is running: a task presented and unsigned for more than twenty minutes appears at that node's orientation with the command that fixes it, because recycling the lead is what makes it orient and read the queue it owes. Twenty minutes rather than immediately, so a lead mid-review is not reported as absent.

**A cold session is the expensive one, and it does not look expensive.** An idle session costs nothing while it is idle. It costs when you speak to it: every turn resends the whole conversation, and the prompt cache holds that for **one hour on a subscription** — five minutes once usage credits are being drawn on. Past it, the next thing anyone says re-processes the entire context as new work rather than as a cache read. So a node walked away from three hours ago is not free to pick up; the first word costs its whole history at full rate, and nothing on screen said so.

`harness idle` lists every session holding a node, oldest first, with how long it has been quiet, whether it is past the cache lifetime, and how much context it would have to re-read. `harness recycle --cold` sweeps the ones that are, and the viewer marks the card. Both refuse a node with an **unpresented** open mark and a dirty worktree, so the sweep never destroys work in progress; where a session's transcript cannot be read the age is unknown and the node is kept, on the same rule that makes a failed roster read mean *unknown* rather than *empty*.

This is [[#R13 — Everything below rank 0 starts cold]] arriving at the same answer from cost that it already reached from quality. A member is stateless by design — position comes from git, orientation from the hook, scope from the task record — so replacing a cold session costs one orientation, while resuming it costs everything it was carrying **and** keeps the accumulated errors.

**Recycling is the best-evidenced thing in this design.** A persistent worker
accumulates its own errors: measured, per-step accuracy falls as steps grow, and
the cause is not only long context but self-conditioning on its own earlier
mistakes, which scale does not fix. What does fix it is explicitly removing prior
history. Separately, a worker revisiting its own output without an external check
degrades in every configuration tested, and improves only when an oracle is
present, which is the same finding that makes the lead's read at
[[#T4 — Integration (fast-forward up)]] a gate rather than a courtesy.

**Recycle rather than compact.** The alternative to ending a worker is summarising
it in place, and that is worse on the evidence available. Of 2,495 fixed-interval
summarisation calls in one measured run, 1,009 flipped a correct answer to wrong:
40.4% of transitions degraded. No compaction threshold is empirically grounded —
no study sweeps a trigger against quality with enough resolution to locate one,
the widely repeated "70 to 80% of the window" traces to blog posts, and deployed
defaults span 50% to 99% while all claiming the same benefit. A content-conditioned
rule beat a fixed trigger in 11 of 12 settings at 30 to 70% lower cost, and the
gain came from the rule rather than from compacting at all.

So this note sets **no fixed compaction threshold**. Where compaction happens
anyway, the plan issued at [[#T1 — Task assignment]] is pinned: summarisation is
measurably biased against the earliest material in its input, and in a
plan-then-delegate design the earliest thing in a worker's context is the plan it
is executing.

Nothing is lost, because a member holds nothing that is not written down. Its
position comes from git ([[#R1 — Position is derived, never declared]]), its
orientation from the SessionStart hook
([[#R11 — Orientation is a hook in the enrolled repo, not a global one]]), its
scope from the task record ([[#T1 — Task assignment]]) and its work from the
commits. A member that survives many tasks is carrying transcript, not knowledge.

**When.** At the end of commits — meaning once they have *landed*, not merely
been made. `recycle` refuses on its own if:

| refusal | why |
| --- | --- |
| rank 0 | it holds the rulings and the document state |
| worktree is dirty | uncommitted work would be stranded in a context nobody can read again |
| commits not yet in the parent | its author is about to be replaced; present them first ([[#T4 — Integration (fast-forward up)]]) |
| session is `busy` | it may be mid-task, or awaiting a reply to [[#T12 — Question]] or [[#T7 — Conflict escalation]] |

The last is the weak one and should be read as a courtesy, not a proof. `busy`
means mid-turn; a member idling on an unanswered question looks exactly like a
member idling with nothing to do. Only the lead knows whether it owes an answer,
which is why recycling is the lead's call and not a timer's. `--force` overrides
every row above, and every one of them exists because it was cheaper to refuse
than to explain afterwards.

