# Documenter — scope

Agreed with the owner 2026-10-05. Not built. This file is not installed, so it costs no session
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

1. It submits a batch of pairs. The harness adds three new operations to the pair format: create a
   file, delete a file, and move a section to a file and leave a pointer.
2. The batch is queued.
3. The harness applies it at root's next turn end, from root's Stop hook. A pending reset is
   handled at the same point. It applies only when root's worktree is clean, because a commit in
   the middle of root's turn could collide with root's own edits.
4. Application is all or nothing, as `pairs apply` is now. It re-runs `harness cited` for every
   deletion and move. The result is one commit with a `Documenter:` trailer.
5. A pair that no longer matches goes back to the ledger, and the next pass picks it up.
6. Root sees one line in its orientation.

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
