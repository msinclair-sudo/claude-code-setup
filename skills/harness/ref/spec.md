---
tags:
  - Decision
---

# Agent Workstream Harness

> [!abstract] Note Role
> **Contains**: the roles, git nodes, transactions and invariants of the multi-agent git harness. Every transaction carries an index (`T*`) referenced from the edges of [[Agent Workstream Harness.canvas]]; every invariant carries an index (`I*`).
> **Cannot contain**: implementation code, installation steps, or per-project scope assignments.

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

### T2 — Catch-up (merge down)

**Direction** downward, node into worktree.
**Performed by** the worktree's own session, never by the node.
**Rule** Twice per task, and only twice: once after claiming, before the first commit; once immediately before presenting. Never between.
**Enforcement** `git merge <parent>`. This produces a real merge commit, because the worktree holds its own work.
**Fails when** Attempted from outside. Merging into a worktree that is in use aborts with `error: Your local changes to the following files would be overwritten by merge` when the incoming change touches dirty files, and succeeds silently when it does not — so it lands in the harmless cases and refuses in the colliding ones. A node therefore publishes `git rev-list --count <child>..<node>` and lets the recipient act at its own boundary.

### T3 — Guard verification

**Direction** internal to a worktree, after [[#T2 — Catch-up (merge down)]].
**Rule** A worktree proves it is guarded before it commits. Config that *looks*
right and hooks that *are* right are different claims.
**Enforcement** `harness doctor`. It demands the behaviour rather than reading
settings: it synthesises content the document node has never held, stages it in a
**throwaway index** so the real one is untouched, and requires the guard to refuse
it. It also requires the guard to *allow* a document that arrived from the
document node, so a guard that refuses everything fails too.

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
**Enforcement** `git merge --ff-only <child>`. A contributor that has not completed T2 is refused with `fatal: Not possible to fast-forward, aborting.`
**Fails when** Treated as a push. Pushing to a checked-out branch is rejected: `! [remote rejected] … (branch is currently checked out)`.

**A review is required, and it is enforced.** `harness review <node> --record` reads the diff and records the read against the child's exact commit; `reference-transaction` refuses the parent's fast-forward without that record. A new commit on the child invalidates it automatically, so there is nothing to expire.

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

**Reading is optional; being able to read is not.** A lead may integrate without
reading the diff — that is a judgement about pace, and the harness does not gate
the merge on a review. But the view must never be unavailable, and there is a
sharp reason it was: **a fast-forward leaves no boundary.** After `T4`, parent
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
**Enforcement** `harness mark <task> --close` writes the record: the closing sha, the closing session, and the delta if it is subtractable. `harness release` frees the node. `harness stop <node>` ends the session that held it: `claude stop` is a full teardown — the process dies, the session file is removed, and it leaves `claude agents --json`. A lead can reap its whole layer with `harness stop --children`, and no session may stop itself.
**The close is the point, and it had no record until 2026-08-31.** "Released" was a claim in a message rather than a fact in a store, so nothing could tell a node still working from a node finished and still standing there. `harness status` now names the difference — an open task, or `unassigned` — and `harness recycle --idle` sweeps exactly the children that have none. Closing is always permitted even when the measurement is not: a task closed in a different session than it opened records `_delta: null` and says why, because refusing the close over an unmeasurable cost would leave the task open forever and destroy the one signal this exists to give.
**Fails when** The row is deleted rather than closed — [[#T8 — Deep conflict]] depends on closed rows staying readable. Or the session is left running after its node is released: a lane nobody can shut down is not a lane, it is a leak. `release` drops the claim and **does not end the session**, so that leak has a shape — a live session standing in a worktree it no longer claims, constrained by no rule in the tree. `status` reports it as `OCCUPIED but unclaimed`.

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

---

## Invariants

### I1 — One session per branch

Enforced by git, not by agreement. `git worktree add` refuses a branch another worktree holds: `fatal: 'dev' is already used by worktree at …`

### I2 — Nobody pushes

The owner of a node integrates contributors into it. Pushing to a checked-out branch is rejected outright, so the invariant costs nothing to maintain while every node stays checked out.

### I3 — Scopes are globally disjoint

No two open tasks anywhere in the tree may claim the same path, checked against a single registry. This makes textual conflicts rare rather than routine, and leaves semantic conflicts — a changed signature that a caller elsewhere depends on — which produce no merge conflict and are caught by checks at integration.

**A member writes only inside its own worktree.** An artefact outside the repository has no owner, no path scope and no instrument that can go red on it: nothing reviews it at [[#T4 — Integration (fast-forward up)]], no guard refuses it, and no ref records that it changed. A member producing one is producing something the tree cannot see, check or undo. Outputs outside the repository are rank 0's or the operator's, unless the machine's owner declared otherwise — see [[#I11 — Reach beyond the worktree is granted at enrolment]]. This is not a restriction added on top of the permission system; it is the same rule I3 already states, applied to the one direction it had not been.

**A record anyone may correct must be a document inside the tree.** Code has an owner, a scope and an instrument that goes red. A note kept outside the repository has none of the three, so a disagreement about it cannot be settled by a check, a diff or a ref — only by argument, and argument between two parties who both value catching errors alternates instead of converging. Inside the tree the same correction is a [[#T5 — Document request (upward)]] pair: applied once by the owner, no reply expected, terminal on an artefact. Outside it, the exchange has no terminal state at all, and nothing in the protocol can ever say which round is the last. Measured 2026-08-31: four rounds of mutual correction over records held outside any scope, each finding something genuine, each smaller than the last, no ref moving after the first.

### I4 — `reference-transaction` is the primary guard

| operation | `pre-commit` | `pre-merge-commit` | `reference-transaction` |
| --- | --- | --- | --- |
| commit in a worktree | fires | n/a | fires |
| fast-forward up (T4) | silent | **silent** | fires |
| merge down (T2) | silent | fires | fires |
| `reset --hard` | silent | silent | fires |
| `push` | silent | silent | fires |
| `branch -f` | silent | silent | fires |

Every T4 is a fast-forward by design, so `pre-merge-commit` is silent on the path documents would take. `reference-transaction` alone covers it. It must be POSIX `sh` with an explicit `exit 0`: a non-zero exit gives `fatal: ref updates aborted by hook` and the repository stops accepting any ref update.


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

### I6 — The ledger is append-only

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

Grants become two documented, additive `claude` flags at the next spawn or recycle — `--settings` with a `permissions.allow` list, and `--add-dir` for reach — so a running session keeps exactly what it started with and a grant never takes effect mid-task.

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

**XL is a refusal, not a size.** It is the operational definition of [[#I8 — Tasks are short]]: if a lead cannot bring a task under L, it splits it or escalates. This is the only number in the harness that decides whether work may be issued at all.

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
([[#R13 — Members are recycled, not accumulated]]) starts a new transcript, so a
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
figure, and states its unit every time. Cache reads dominate the sum and bill at
0.1×, which makes the token total actively misleading as a proxy for cost — for
this session, 261.7M tokens is ~$194.50, and reading the token column instead of
the dollar column would overstate it by an order of magnitude.

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
### R3 — State is split by whether it travels

| in the repository, versioned | on the machine, never committed |
| --- | --- |
| logical tree (node → parent) | worktree → node binding |
| ledger, rulings, manifest, guards | locks, session ids, enrolment |

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

Measured 2026-08-31: rank 0 told a lead to hold a member so it could carry its context into the next task; the lead had already recycled it, correctly, on the standing rule. The lead could not have avoided receiving that message. It could have avoided trying to satisfy it, and the attempt is where the tokens went. The instruction was also **wrong on its merits** — [[#R13 — Members are recycled, not accumulated]] says nothing a member knows survives unless it is in a commit, a report or the ledger, so a request to preserve a session for its context is a request to skip writing a document. The coordination failure was downstream of a documentation one, and [[#T10 — Release]]'s close record is where that document belongs.

**Transport is the agent's, which sets a hard limit on what can be guarded.** `SendMessage` does not pass through the CLI, so no instrument here can count exchanges, notice that a thread has stopped producing artefacts, or decline to send. A rule of the form "stop replying after n rounds with no ref moved" is therefore a *rule with a diagnostic*, never a guard — and a guard that depends on a participant staying alert is the thing this design exists to remove. Only two mechanisms actually terminate an exchange, and neither is a tripwire: making the artefact a document, so the correction becomes a [[#T5 — Document request (upward)]] pair with a terminal state; and [[#R13 — Members are recycled, not accumulated]], which ends it by the counterparty no longer existing in that context. The diagnostic half is real and worth having — `harness status` marks a live node with no open task as `unassigned`, and `harness spend` prices the exchange — but it informs a decision rather than making one.

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

Refusing is the correct response because the failure is silent otherwise: a harness that mis-identifies a session can let two of them hold one node, and that is the one failure the lock exists to prevent. The check runs at claim time, not once at install.

### R10 — Propagation spawns sessions, and can stop them

One human starts the rank-0 session. It builds the tree and launches the rest:

```
harness spawn [--dry-run]        one `claude --bg -n <project>-<node>` per
                                 unoccupied node, in that node's worktree
harness stop  <node> ...         end those sessions
harness stop  --children         reap a whole layer
```

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

`SessionStart` is one of three events whose **plain stdout is added to the model's
context**, so no JSON envelope is needed; `whoami` output is the payload.
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
a member runs its own checks and presents the report, and the only checks a lead
re-runs are the absent member's during [[#T7 — Conflict escalation]].

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
| member (leaf) | `opus` | `medium` | one task, one worktree, then recycled — but coding is the one steep effort curve |

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
([[#R13 — Members are recycled, not accumulated]]) so it never accumulates one.
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

**The split has a cost, and it is not zero.** `opus[1m]` and `opus` are separate
cache namespaces — measured: a request on one immediately after the other rewrote
12,521 tokens rather than reading them, while a repeat on the same model read all
22,491 and wrote none. Sessions in one repo share a static prefix, so running two
models across the ranks caches that prefix twice. The wide window is still worth
it for a lead; this is the bill for it, stated rather than hidden.

Re-measure all of this from closed ledger rows under
[[#I10 — Cost is estimated, then measured]] rather than trusting the table.
Anthropic's own guidance is that the curve is per-workload *and* per-model, and
that a sweep should be re-run after any model migration or workload shift.

A misspelt effort is refused when the tree is validated, not when `claude`
rejects it — by then the session is already spawned and detached.

### R14 — The operator is told, and does not have to look

**The platform cannot tell you which session wants you.** Measured 2026-08-31: `claude agents --json` carries `status` (busy/idle) and `state` (working/done) and nothing else. A session stopped dead on a refused permission is `busy`, indistinguishable from one that is working. So the harness has to say so itself, and the mechanism is constrained by [[#R4 — No arbiter process]]: nothing polls, because nothing is running to poll. **The event notifies at the moment it is recorded**, or not at all.

| surface | reaches the operator when |
| --- | --- |
| `~/.claude/harness/notify` | immediately, if they installed one — run with `HARNESS_SUMMARY`, `HARNESS_COUNT`, `HARNESS_JSON` in the environment |
| the statusline badge | next prompt, in **any** session, enrolled or not |
| `harness needs` | when they ask, from anywhere |

**The harness does not choose the channel.** `notify-send` is wrong over ssh, wrong on a Mac and wrong in WSL, which is three of three on the machines this has run on. The hook is absent by default and the record is written either way; a notifier that fails, hangs or is missing must never take the block record down with it.

**Everything a decision needs is in one place, with the command already written.** `harness needs` scans every enrolled project on the machine, deliberately building no `Ctx` — the operator is usually not standing in the repository that wants them, and often not in a repository at all. A command that only works from the right directory is one that does not get run. Each entry prints what is needed, what it is for, **what is still moving without it** (which is how urgency gets judged rather than guessed), and the exact `harness grant` and `harness recycle` lines, `cd`-wrapped and shell-quoted.

Granting closes the block it answers. A queue that keeps naming something already dealt with is a queue nobody reads, so the two records are kept in step rather than left to a member to tidy up after the fact.

`needs.json` beside the project directories is a derived cache, rebuilt on every raise, grant and resolve, and it exists for exactly one reader: the statusline renders on every prompt and cannot walk every project's block directory. The per-project block records are the truth; `inbox.jsonl` is the append-only history of both raising and clearing ([[#I6 — The ledger is append-only]]).

### R13 — Members are recycled, not accumulated

A member's session is ended and a fresh one started on the same node once its
work has landed. `harness recycle <node>` or `--children` does it; a lead drives
it for its own children.

It is a teardown and relaunch, not a clear. A background session cannot clear
itself, and a session that stopped itself could not start its replacement — so
the parent does both. **Never `claude rm`:** that deletes the session *and its
worktree*, and on a node the worktree is the node.

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

