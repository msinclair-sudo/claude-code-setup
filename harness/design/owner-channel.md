# Owner channel — scope

Agreed with the owner 2026-10-05. Not built. This file is not installed, so it costs no session
context; the spec's `T17` points here.

## What it is for

The owner is asked only what nobody in the tree can answer. Each question arrives briefed well enough
to rule on without reconstructing its history, and the ruling is kept with the question, so the
record is a log of decisions made. Four kinds of question qualify:

- **Intent.** Is this what you meant? Is X in scope?
- **Judgement or taste.** A design direction whose options lead to different work.
- **Only the owner can do it.** Look at a render, add a permission rule, log in somewhere.
- **Risk.** A live or destructive write the owner has to accept.

It is not for path access, task approvals or stalled sessions. Blocks, grants and approvals handle
those between sessions, and they stay as they are. Sessions should settle most questions
themselves; an item here is the exception.

## Who is involved

- **Askers:** rank 0 and leads. A lane goes through its lead.
- **The intermediary:** one persistent session outside the work tree, standing between the askers
  and the owner.
  - **Input:** a raw ask from an asker.
  - **Investigation:** it reads code, worktrees and harness records (briefs, facts, findings,
    notes), so it understands the problem directly rather than through the asker's account. It is
    read-only and runs nothing. It can query the asker for missing information or clarification.
  - **Filtering:** it can send an ask back as not the owner's, or merge it with one already open.
  - **Output:** it writes every briefing in one fixed form, for the owner to read, not for the
    record.
  - **Limits:** it does not decide, edit or create tasks.
  - **Life:** it persists across items. The GUI shows its context and can restart or compact it.
- **The owner:** discusses an item with the intermediary. The intermediary answers follow-ups
  itself from its own reading, and goes back to the asker only when it has to.

## What gets recorded

A ruling is written only when the owner and the intermediary both agree it is right. The record is
the question, amended with anything the discussion showed it was missing, and the answer. The
discussion itself is not kept.

The asker carries on with other work while it waits, if it can. The ruling returns to it.

## Why the previous attempt failed

The failures of `harness needs` and `harness decision`, removed 2026-10-05. Do not repeat them.

1. Four populations in one list: grants, approvals, stalled sessions and real questions. Most were
   not the owner's, so the list was noise.
2. The asker wrote the item to justify itself, so the question was buried in an essay.
3. The only way to reply was a quoted shell argument.
4. Nothing closed an item. Nothing waited on it, nothing expired, nothing followed up.
5. Nothing told the owner an item existed. Three were raised and none was ever answered.

## Still to discuss

- The visual form: the briefing layout and the reply box.
- Notification: how the owner learns something is waiting.
- The briefing's fixed sections.
- How a ruling reaches the asker, and where rulings are stored so tasks and facts can cite them.
- What happens to an item nobody answers.
