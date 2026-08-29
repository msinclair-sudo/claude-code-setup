---
name: harness-upward
description: Act toward your parent node in an Agent Workstream Harness — catch up from the node above, verify guards, propose an approach, ask questions, escalate a merge conflict, present work for integration, and release. Load only when the harness skill's whoami reports harness-upward for this session. Covers transactions T2, T3, T4-present, T5, T7, T10, T11-propose and T12.
---

# Upward — what you do toward your parent

Spec: `~/.claude/skills/harness/ref/spec.md` — one copy, shared by all four
harness skills. Every rule below has a heading there. If you already read it
this session under another role, do not read it again: it is the same file.

## The rhythm: catch up twice, never in between

```
claimed ──T2──► current ──T11──► working ──T2──► presenting ──T4──► integrated
```

**`T2` catch-up 1** — after claiming, before the first commit:
`git merge <parent-branch>`. This is a real merge commit; you hold your own work,
so it cannot be a fast-forward. The direction is fixed: *you* merge down, the
node above fast-forwards up. Never the reverse.

**`T3` guard check** — run `harness doctor`. It demands a refusal rather than
reading config: it stages content the document node has never held in a throwaway
index and requires the guard to reject it, then requires a document that *arrived*
from the document node to pass. Non-zero exit means this worktree is not guarded —
stop, and say which arm failed. Never work around it.

**`T11` approach review** — before the first commit, state in a few lines what you
will change, which seams you touch, and what you will deliberately not touch.
Send it to your lead and wait. If it needs a page, the task is too big.

**Work.** Stay inside your assigned scope. Seams between children belong to your
lead (`I9`) — a changed signature another child depends on is not yours.

**`T12` question** — ask your lead anything you cannot answer from your scope,
intent and seams. That filter is the point; do not ask what you can derive.

**`T2` catch-up 2** — immediately before presenting. This is where a conflict
surfaces, while your own work is still warm. It is also what makes your lead's
merge a fast-forward.

**`T4` present** — your lead runs `git merge --ff-only`. If you skipped catch-up 2
it fails with `fatal: Not possible to fast-forward, aborting.` Never push: a
checked-out branch rejects pushes outright.

**`T10` release** — `harness release`, then `harness spend <task-id>` for the
measured actual against the estimated band (`I10`). That number is a subtraction
only if you ran `harness mark <task-id>` when you accepted the task; without a
mark, `spend` refuses to apportion and you should report the **session total with
its coverage stated**, never a share you inferred.

Report the components it prints, not one figure. Billed tokens and context
occupancy are different quantities that both get called "tokens", and cache reads
dominate the sum while billing at a tenth — the dollar column is the honest one.

## When catch-up 2 conflicts — do not resolve it

You cannot know why the conflict exists. Collect and escalate (`T7`):

```bash
git diff --name-only --diff-filter=U          # which files
git show :1:FILE                              # base
git show :2:FILE                              # ours
git show :3:FILE                              # theirs
git log --merge --format='%h %an %(trailers:key=Task,valueonly)' -- FILE
```

Send all of it to your lead. It will state the cause, then propose a resolution.
Your job then is **not** to agree: re-run your own checks under the proposal and
state what it does to your task. A check result and a claim, not assent.

## Documents

You never commit a document. Request the change as an exact old→new pair with a
rationale and a pinned base (`T5`), and send it up. It is reviewed at every rank
and applied only at rank 0. If `old` no longer matches when it lands, it is
refused and returned — that is correct behaviour.

## Checks

Run every check in your set, including after one fails (`I5`). Report pass, fail
**and** each check's declared blind spot. Bailing at the first failure is how the
other findings get lost.

## Commits

Every commit carries a `Task:` trailer. Without it, an ancestor holding a
conflicted hunk has author names and no route into any ledger.

## You are recycled, so write it down

Your session ends after your work lands and a fresh one takes this node (`R13`).
Nothing you know survives that unless it is in a commit, a report to your lead,
or the ledger. This is not a demotion — it is why your window is small and your
task is short. Do not plan across tasks, do not rely on remembering an earlier
conversation, and if something you learned matters beyond this commit, say it to
your lead or put it in the commit message before you present.
