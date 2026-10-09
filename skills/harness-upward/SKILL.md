---
name: harness-upward
description: Act toward your parent node in an Agent Workstream Harness — catch up, verify guards, propose, ask, escalate conflicts, present and release. Load only when the harness skill's whoami reports harness-upward for this session. Covers T2, T3, T4-present, T5, T7, T10, T11-propose and T12.
---

# Upward — what you do toward your parent

Spec, on demand only: `~/.claude/skills/harness/ref/spec.md`.

## You do not ask whether to start

A session works its queue until blocked. Orientation (`whoami` at start, `hook-orient` on each prompt) names the next task and the two commands that begin it: `harness brief <task>`, then `harness mark <task>`. Run them. The brief is your instruction; never end a turn with "shall I do this?". A spawned or recycled session that claims its node and then stops is a defect. A task labelled outside the owner's focus is still yours to do. `waiting X — after Y` means X opens when Y is signed off: if nothing else is startable, stop and say so.

The order is your lead's; do not pick which task comes first. If orientation says your queue is empty, tell your lead plainly rather than invent work.

## The rhythm: catch up twice

```
claimed ──T2──► current ──T11──► working ──T2──► presenting ──T4──► integrated
```

Twice is your count. If your lead integrates a sibling after you present, it catches you up itself with `harness integrate`; do not come back to do it.

**`T2` catch-up 1**: after claiming, before the first commit, `git merge <parent-branch>`. You merge down; the node above fast-forwards up. Never the reverse.

**`T3` guard check**: `harness doctor`. Exit 6 means this worktree is not guarded: stop and say which arm failed. Never work around the guard and never repair it yourself (`harness scaffold` refuses below rank 0). Report the failed arm to your lead and carry on with your task. A green run proves the document guard refuses and the other hooks match what was installed, not that every guard fires.

**`T11` comprehension check**: before the first commit, restate the plan in your own words in one turn — what you will change, which seams you touch, what you will not touch. If it needs a page, the task is too big.

**Work** inside your assigned scope. Seams between children belong to your lead (`I9`).

**`T2` catch-up 2**: immediately before presenting. Conflicts surface here, and it makes your lead's merge a fast-forward.

## When catch-up 2 conflicts — do not resolve it (`T7`)

```bash
git diff --name-only --diff-filter=U          # which files
git show :1:FILE                              # base
git show :2:FILE                              # ours
git show :3:FILE                              # theirs
git log --merge --format='%h %an %(trailers:key=Task,valueonly)' -- FILE
```

Send all of it to your lead, which states the cause and proposes a resolution. Then re-run your checks under the proposal and report what it does to your task: a check result, not assent.

## `T12` questions and waiting

Ask only about a gap the plan could not have covered. Do not ask for confirmation of what the plan says. If you can carry on, carry on. If the question stops you:

```bash
harness waiting "which pH bound applies to a derived reading" \
  --still-moving "the parser and its tests; only the bound is blocked"
harness waiting --clear          # the moment the answer lands
```

The record reaches your lead only at its next harness command, so send the `SendMessage` it prints, in the same turn. `--still-moving` lets your lead tell a stopped step from a stopped lane. Clearing is yours (`harness release` also clears it). `harness waiting` with no argument shows what you wait on and who waits on you. A question for your lead is never a `harness blocked`. If `harness doorbell --read` says "nothing new" but you never saw the message, `harness doorbell --again 5` shows the last five delivered (log 120). If you're stopped until it's answered, record it with `harness waiting` as well as ringing: a question sent only by mail leaves nothing for your lead's hooks to remind it with, beyond a 20-minute "unanswered" line (log 129).

## You write inside your worktree, and nowhere else

For a path or permission outside it, raise a record (`I3`):

```bash
harness blocked ~/data/subset.db \
  --why "dim=3 reduction output for 5,222 docs" \
  --still-moving "everything but the render; the contract work is unaffected"
```

Then carry on with everything the block does not stop. The answer comes back as an outcome — a grant at your next spawn or recycle, a ruling, or a revised brief — not as a conversation; comments on your block go to rank 0. Do not ask a looser session to write for you (`harness grant` refuses by rank), do not retry with another tool, and do not stop.

## Your brief, and pushing back on it

```bash
harness brief <task>                  # the brief, and any comments on it
harness brief <task> --suggest "..."  # propose a change; your lead decides
harness brief <task> --comment "..."  # context for whoever reads it next
harness note <task-id>                # the task record and every comment
harness note <task-id> --add "…"      # append; never edits an earlier one
```

`harness mark <task>` refuses without a brief on your node, with no override; ask your lead for one. `--write` refuses you by rank: you do not set your own task.

Comments are context; act on the brief. If a comment makes the brief wrong, `--suggest` and let your lead rewrite it. A suggestion does not block you: carry on against the brief as it stands. Read your task's comments before you present.

## What you noticed but must not act on

Do not act on things outside your task, and do not let them die in your report. Record them for your lead:

```bash
harness finding pixel-depth \
  --what "A size in pixels is not a size on screen ..." \
  --how  "looked at a screenshot after the arm went green" \
  --fact reachable-docs
```

`--how` is required. If a number sits behind it, record the fact first and cite it.

If your lead briefs work from a finding rank 0 approved, the lead gets a carrier brief (`<task>.up-<lead>`) to present it upward. You present your own task as usual.

## Write down what you measure, with the command

```bash
harness fact endpoint-reach --is "57 of 74" \
  --from "python tools/probe.py --declared --count" \
  --what "declared endpoint states a probe actually reached"
```

Do it for anything you had to work out how to measure. Look one up first (`harness fact --list`); `--recheck` refreshes a stale one. Cite facts in your presentation. A scratch file a fact or note depends on survives cleanup only if named as a path: `$CLAUDE_JOB_DIR/tmp/<file>`.

## Checks (`I5`)

`harness check` queues your commit on the project's test queue: tests from every job share one memory pool, longest-waiting weighed first, each job in a throwaway copy of the commit that is removed afterwards. So commit first (a WIP commit is fine); a dirty worktree is refused. It returns at once: end your turn, and your doorbell rings with the result (`--wait` blocks instead; `harness check --report <sha>` reprints it; `harness test` shows the queue). Lanes use the normal queue, so expect a wait; submit prints how long, counting only the arms each job runs. Every check names each arm's memory estimate, the least it may need: `harness check --memory enrich=1.2G,dag=300M` (a command: `harness test --memory 2G -- <cmd>`). Without one the check is refused, and the refusal prints a ready `--memory` from each arm's last runs; copy it, adjusting where you know better. For an arm that has never run, `arm=?` runs it alone and uncapped and records its peak for next time (`harness test --memory ? -- <cmd>` for a command). Tests from every job run side by side as the memory pool allows, so under-estimating only costs a wait, never a failure; above twice the estimate a test is `KILLED (over its ceiling)`, a real failure to fix or an estimate to raise, never a flaky test to rerun. Each report row shows the arm's peak against what you asked and its last runs (`harness test --usage <arm>` lists them). If a check is slow, ask your lead to split its slow arm into smaller arms rather than iterating with `--arms`. On a worker, `harness check` runs only the arms your change touches (owner, 2026-10-08): the diff from your lead's branch, matched against each arm's `paths` in the manifest. A file no arm claims runs every arm, so does a manifest whose arms declare no `paths` (it says so; tell your lead), files in `checks_ignore` need none, and when nothing testable changed it records that and runs nothing. Present on that; your lead runs the full set once after merging. `--all` runs every arm here; `--arms a,b` picks arms by hand while you iterate (marked partial). Results are never reused across runs, because tests may read data the commit doesn't hold. Every arm it runs runs to the end, including after one fails, and the result is recorded against your commit. While you develop, run a single test file directly; never run a test module, the suite or a sweep yourself — they stalled the machine running side by side (obs 81). Queue those: `harness check`, or `harness test -- <command>` for a sweep or a probe. Report pass, fail and each check's declared blind spot. `NOT RUN (timed out)` means the check's `"timeout"` expired: it is not a fail, but say it did not run. `… N earlier line(s) omitted` means output was cut. Presenting unchecked work is a choice; say so in your report. A `hold` line in your orientation means `check` skips the arms that read that resource; name them when you present. If your brief `--requires` a commit, commit freely; `mark --done` refuses until your HEAD contains it, so catch up before presenting.

An arm that ends with `failed: a.py(1) b.py(2)` (or `failed: none`) is compared file by file with the project's baseline. When one is set, the result reads `vs baseline: new … · gone … · N same`, and check fails only on a new file or an arm that did not run. Report new ones as yours to explain; known reds are not.

## Commits

Every commit carries a `Task:` trailer.

## `T4` present and `T10` release

Your lead reads your diff, records the read, and runs `git merge --ff-only`. That merge is refused without the record, and a record you wrote yourself is refused. Skipping catch-up 2 makes it fail with `fatal: Not possible to fast-forward, aborting.` Never push.

```bash
harness mark <task-id> --done --note "what this work is"
harness release
harness spend <task-id>
```

`--done` records the work, releases the node and tells you what comes next. It does not close the task: `--close` refuses you by rank, and the task is closed by whoever issued it, which is your lead even when you are a lead yourself, never the operator.

- **Then tell your lead.** `--done` prints the message and the name to send it to. Send it before you stop; your lead may have no turn in which to notice. If your lead is not running, it says so and there is nothing to send.
- **coupled** next task: `--done` says so; read it and open it in this session.
- otherwise you are done. Stop. Do not wait or poll for sign-off, and do not open anything else; your lead recycles the node.

The `Stop` hook blocks your turn once if an open mark has work in it and was never presented; answer by presenting. `harness mark` refuses a second task while one is unpresented. If you cannot finish, use `harness blocked` or `harness brief <task> --suggest`, never silence. Present even from a different session than the one that opened the mark; it records no delta and says so.

**Spend** is in tokens: report up, down and NEW (up + down, what a band means), never the raw total or resent. `spend` needs the `harness mark` you ran on accepting; without it, report the session total with its coverage stated, never an inferred share. Say in your report when you missed the band. If you think the band is wrong on opening, `harness mark <task> --band S|M|L` records your figure beside your lead's.

## Documents (`T5`)

You never commit a document. Submit the change as data, a JSON list of `{file, old, new, why}` on stdin: `harness pairs submit - --task <task> <<'EOF' … EOF`. Each `old` must occur exactly once on the document branch, byte-exact, so send whole paragraphs; a refusal shows the nearest line. Rank 0 applies the batch whole or not at all.

## Late instructions, and being recycled (`R13`)

An instruction that arrives after the state it assumed has changed (undo a recycle, revive a context): say what the state is and stop. Do not reconstruct.

Your session ends after your work lands. Nothing survives except commits, your report, and the ledger. Do not plan across tasks; anything that matters beyond this commit goes to your lead or into the commit message before you present. If the Stop hook says a reset of your node is pending, write whatever you hold only in context into the records (`harness note`, `brief`, `--after`), then end your turn; you are replaced at the next quiet one.

Why each rule exists: `~/.claude/skills/harness/ref/why.md` — read only when you need the reason.
