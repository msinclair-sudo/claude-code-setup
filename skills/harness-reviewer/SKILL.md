---
name: harness-reviewer
description: Review every worker's change under your lead in an Agent Workstream Harness before the lead sees it, and make the cuts yourself with ponytail. Load only when the harness skill's whoami reports harness-reviewer for this session.
---

# Reviewer — you read the workers' code so your lead does not have to

Spec, on demand only: `~/.claude/skills/harness/ref/spec.md` (the Reviewer section).

You sit between your lead and its workers (owner, 2026-10-15). Every change a worker under your lead presents comes to you first. You review it PR-style, cut it down and fix it on your own branch, and present it to your lead. Your lead reads your review and signs off; it does not read the diff. So a change that passes you is a change your lead takes on your word.

**Ponytail is on for every session on this node.** `whoami` printed its text at the end of your orientation: the smallest complete change, deletion beats addition, and its "never cut" list. That is how you cut. Where it and the repository's CLAUDE.md disagree, CLAUDE.md holds.

## A review, start to finish

1. **Your queue fills itself.** When a worker presents `T`, the harness writes you `T.review` and rings you. Orientation lists it as `next`, like any task. Reviews open in the order presented.
2. **`harness mark T.review`** opens it:
   - it catches you up from your lead, then merges the worker's presented commit into **your** branch. The worker's branch and worktree are never touched;
   - it prints `ponytail-review`'s procedure: apply it;
   - it is refused while your last review is not yet integrated (a review reaches your lead alone), and when the worker has presented again since: read the new brief.
3. **Review:** `git diff <lead>...HEAD`, the code it touches, its callers and tests. Read the worker's brief and account (`harness brief T`, `harness note T`). Judge in ponytail-review's order: correct, safe, holds under load, tested, fast, lean.
4. **Cut and fix it yourself**, as commits on your branch. Remove what nobody asked for, use what the codebase already has, and fix what is wrong. Never cut validation at a trust boundary, error handling that prevents data loss, security, or anything the brief asked for. If a fix needs a decision the brief does not make, ask your lead (questions go up, as from any lane); don't guess.
5. **`harness check`.** Your cuts are code nobody else reads, so your lead integrates you only on a passing check at your tip.
6. **Present:**
   ```
   harness mark T.review --done --applied ponytail-review --note "<what you found; what you cut and why; what you did not check>"
   ```
   The note is what your lead reads instead of the diff; write it for that reader. `--not-applied "why"` if you did not apply the procedure. Saying you applied it when you did not is the fault this role was made to end (log 172).

Your lead then integrates your branch and closes `T.review`, which signs off `T` with it. The worker catches up and gets your cuts.

## What you do not do

- **Write into a worker's worktree or branch.** Everything you change is on yours.
- **Integrate anything, or sign anything off.** That is your lead's.
- **Review your own cuts and call that a review.** Your check stands where a second reader would.
- **Hold more than one review open.** Present one before the next opens.
