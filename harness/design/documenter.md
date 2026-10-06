# Documenter — scope

Agreed with the owner 2026-10-05. v1 built 2026-10-05 (`harness docs`, `harness documenter`, spec `T18`). This file is not installed, so it costs no session
context.

## What it is for

Keeping a project's markdown small, current and clear, so rank 0 can spend its context on
orchestration instead of document upkeep.

The cost it exists to cut, measured on biblion2 on 2026-10-05:

- `CLAUDE.md` is 16,212 words, about 21k tokens. Every session loads it at start, including every
  lane recycle. Most of it is provenance: dated measurements, incident write-ups, and the history of
  how each rule came about.
- Another 409k words of markdown sits in `plans/` (186k), `design/` (134k), `spine/` (56k) and
  `schema/` (33k). Most of `plans/` likely describes finished work.
- `CLAUDE.md` was committed 28 times in the last month, and no pass has ever taken anything out.

## Revised 2026-10-06: current and true, one whole doc per run

The owner, after watching runs: they were very quick, only trimmed words and moved text, and
nothing checked whether the content was true. "Its job is to document what things currently look
like, and move provenance out of current docs, so documentation is current." And: "if the scope
starts to drift then issues will pile up and the project will become very difficult to recover."

What changed:

1. **The job is truth first.** The docs describe the project as it is now, and what they say holds.
   Size comes last.
2. **A run is one document, whole.** "One change per run is a bit light: it means the documenter
   has to relearn every time." It reads every section, checks each concrete claim against the code
   at HEAD, fixes what the code plainly contradicts (citing `file:line` or a commit in the pair's
   `why`), moves history to provenance, trims last, and sends one batch. A declined batch may be
   fixed twice.
3. **Mechanical content checks** (`harness docs check`): paths, links and anchors, and functions a
   doc names that are not there; lines that read as history. The manifest's `doc_sources` lists
   other repositories the docs may describe (biblion2 cites its inherited biblion codebase: without
   it, 2,155 path hits, 334 with it and suffix matching, most of them real).
4. **Checked against the code, and when.** `harness docs verified <doc>` records the commit a doc
   was checked at; it is due again when the code it names changes.
5. **Docs are ranked, not changes:** importance (reads, pointers; every session for `CLAUDE.md`)
   times trouble (missing names, never or outdated check, history lines, size, budget). A 47k-word
   log nobody reads no longer outranks the spine everyone reads.
6. **Scope conflicts go to the owner** as a new ask kind, `scope`, through an intermediary to the
   Issues tab. The sections involved stay untouched until ruled.
7. **No automatic runs** until the design is good enough (`DOC_AUTO_RUN = False`). Runs start
   from the GUI card or `harness documenter [--doc <path>] [--runs N]`.

The sections below describe v1, kept for the reasoning; where they disagree with this list, this
list holds.

## What it does

Each pass does one of four jobs:

1. **Budget.** Holds `CLAUDE.md` to 2,500 words. That is what a worker needs at every start, plus
   one-line pointers to where everything else lives, so a lead or worker can still find it in one
   read.
2. **Provenance.** Moves the why (dated measurements, incident stories, superseded observations)
   to `provenance/<doc>/<section>.md`. The rule and a pointer stay behind.
3. **Stale docs.** Deletes docs nothing needs; git history keeps them. A doc is stale when it
   describes only closed tasks, names paths that no longer exist, or has been superseded by another
   doc. It is deleted only if no open record cites it (`harness cited`, obs 74), and only if every
   kept doc that links to it is fixed in the same batch.
4. **Clarity.** Rewrites with `schimel-science-writing` and `google-devdocs-style`. Like the
   intermediary's writing skills, these are passed in at launch.

It never orchestrates, touches code, decides intent, or writes briefs.

**Out of scope:**
- the harness's own skills and spec;
- `.harness/` and `.claude/`;
- the manifest: root owns it, so a bloated `blindSpot` is reported, not edited.

## Each run: measure, pick one improvement, make it

It doesn't try to fix the corpus at once, and it never reads it whole. Every run starts by
measuring, picks the one improvement the measurements point to, makes it carefully, and leaves the
numbers for the next run to compare against.

### What it measures

The harness takes the measurements, mostly with no model, and stores a snapshot per run:

- **Per doc:** its length in words; how often it is written to (commits since the last run); and
  how often it is read (sessions that opened it, counted from transcripts, archived ones included).
- **Pointers:** the links into each doc (from `CLAUDE.md`, other docs and briefs) and the links out
  of it.
- **Reach, per code area:** of the sessions that edited files in an area, how many read the doc
  that governs it. A low read count is ambiguous: either the doc isn't needed, or sessions that
  should read it don't.

  Measured roughly on biblion2 (2026-10-05):
  - 3 of 4 sessions that edited `schema/` read `schema/SCHEMA.md`;
  - 3 of 6 that edited `loader/` read `spine/MODEL.md`.

  A worker changing the schema without having read the schema doc is a documentation failure: the
  doc was too hard to find or too big to read.
- **The area map:** which doc governs which code area. Nothing records this today. The documenter
  builds it and keeps it, and `CLAUDE.md`'s pointer lines are its readable form ("working in
  `schema/`? read `schema/SCHEMA.md` first").
- **`CLAUDE.md`:** its length against the 2,500-word budget, and its pointers.

### What it picks

It picks the largest gap the numbers show. One target per run:

| gap | its usual move |
| --- | --- |
| `CLAUDE.md` over budget | Move sections out to the doc that owns them, and leave pointers. |
| Low reach: a governing doc that editors don't read | Add or sharpen the pointer. Or split the doc so its part can be read on its own: a 33k-word doc gets skipped. |
| Written often, read rarely | Consolidate it into the doc that is read. |
| The same content in several docs | Consolidate to one, and point the others at it. |
| History in a reference doc | Move it to provenance. |
| A stale doc (uncited, unlinked, about closed tasks) | Delete it; git history keeps it. |

Trimming and consolidating are its main work, but it can't remove what someone needs.

**Critical content** is rules and invariants, commands, paths, rulings and decisions, and anything
an open record, a check or the manifest refers to. That content is never deleted outright. It moves,
either into the doc that owns it or to provenance, with a pointer left behind. The harness checks
that moved text arrives verbatim before it applies a batch. Text is deleted only when it is a
duplicate kept elsewhere or history nothing needs, and the evidence goes in the ledger.

**The next run checks the last one.** If a doc's reach drops after a change, or a session goes
looking for something that was moved, that change is flagged first.

Each run is capped at about 80k tokens read. Being a fresh session, it never accumulates context.

## Doc and code disagreeing

- **The code is right and the doc is stale** (a passing check or a commit shows what the code
  does): it fixes the doc without asking.
- **It can't tell which is the bug** (the doc states an intent the code doesn't meet): it asks the
  owner through the intermediary (`T17`). The ask attaches to a standing docs task. It leaves that
  section alone and goes on with the rest of the pass.
- **Something root owns is wrong** (a brief, the manifest, the tree): it raises a finding.

## Life

- **A fresh session per pass.** Each session does one job and ends. What it did goes to a docs
  ledger, so nothing has to survive in context and nobody manages compaction.
- **Started by the harness, not by root.** Passes are launched detached, the same way resets and
  wakes are, when a trigger fires: `CLAUDE.md` is over budget, units have been swept since the last
  pass, or the owner asks from the GUI or the CLI.
- **One pass at a time per project.** Each pass has a file set and a token cap, because nobody
  can read 409k words in one sitting.
- **Read-only, like the intermediary.** It runs restricted with read tools only. The one write path
  is `harness pairs` submissions, plus `harness cited`, `harness ask` and read-only git.

## How its edits land

Only rank 0 commits documents (`T5`); the documenter doesn't change that.

1. It submits a batch of pairs. Pairs can create a file, delete one, or move a section to a file
   and leave a pointer, as well as replace. A created file or a move's destination must be a path
   the manifest classes as a document (obs 76).
2. **Rank 0 reviews every batch** (`harness pairs <task>` shows the diff and stamps the review),
   then applies it or declines it with a reason. This reverses the original auto-apply: the owner
   decided on 2026-10-05, after rank 0's assessment of the first three runs (obs 77), that slower
   now is better in the long run. Orientation and rank 0's Stop hook name a batch that has waited
   five minutes.
3. Application is all or nothing. A move is checked verbatim on disk before the commit. The
   commit's subject says what moved, and it carries `Documenter:`, `Reviewed-by:` and a
   co-author trailer.
4. A declined or refused batch shows in the next run's measurements with its reason.
5. A chain of runs (`--runs N`) starts its next run when rank 0 decides the last batch.

## The budget is the harness's, not the documenter's

`claude_md_words: 2500` goes in the manifest. `pairs apply` refuses any batch that would take
`CLAUDE.md` over it, whoever sent the batch: a lane's T5 or the documenter's. Root's own hand edits
are reported in orientation and by `doctor`, not refused. A refusal is also a trigger for a budget
pass.

## In the GUI

A side card beside the intermediary's shows:

- `CLAUDE.md` words against the budget;
- the last pass, and what it did;
- any queued or refused batch;
- open asks it is waiting on.

## Open

- Trigger frequency, and the per-pass token cap.
- Model and effort per job. Clarity likely needs the strongest model; the stale-doc job probably
  doesn't.
- Whether to bring the harness's own docs (`michaels_setup`) into scope later.
- Whether orientation should name the governing doc from the area map when a lane's task touches
  that area. This fixes reach directly, instead of relying on someone reading `CLAUDE.md` closely.
