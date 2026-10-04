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
  - **Life:** a live session, in a terminal the owner keeps open beside the GUI (decided
    2026-10-05). A quick back-and-forth stays on a warm cache, and askers reach it with
    `SendMessage`, the transport sessions already use, and it reaches them the same way. It starts
    outside any enrolled repo, so it carries no project CLAUDE.md, hooks or MCP servers, and with
    read-only permissions enforced by its settings. The owner compacts or restarts it in the
    terminal; the GUI only shows its context, read from its transcript.
- **The owner:** discusses an item with the intermediary in its terminal. The intermediary
  answers follow-ups itself from its own reading, and goes back to the asker only when it has to.

## What gets recorded

A ruling is written only when the owner and the intermediary both agree it is right: the
intermediary writes a draft ruling to the item, and the owner's **accept** button in the GUI signs
it. The intermediary cannot accept on the owner's behalf. The record is
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

## The GUI page (decided 2026-10-05)

`harness gui` gets a page of its own; the tree page is for watching sessions, this one is for
ruling.

- **The list:** one row per item, with its kind, the question in one line, the asker, its age and
  whose move it is (being briefed, waiting on the asker, waiting on the owner). Rulings sit below
  as a searchable log of question and answer.
- **An item:** the briefing in fixed, capped sections, then the draft ruling with **accept** and
  **edit**. The conversation is in the terminal, not on the page.
- **The header:** the intermediary's context, with how full it is.
- **Notification:** inside the GUI only, as the page's count and the tab title. Nothing outside it
  for now. An item counts once it is briefed and it is the owner's move, not when the ask
  arrives, since the intermediary may send it back or merge it.

Proposed briefing sections, each capped: question (one answerable sentence), why it's the
owner's, what the intermediary checked, the options with each one's consequence, the asker's
recommendation (attributed; the intermediary does not decide), and what waits on the answer.

## Still to discuss

- The briefing's sections: confirm the proposal above, and the caps.
- How an asker hands an ask over, and the record the intermediary writes (a `harness` command,
  so the GUI and the askers read the same record).
- How a ruling reaches the asker, and where rulings are stored so tasks and facts can cite them.
- What happens to an item nobody answers.
- The intermediary's own instructions: what it reads first, how it decides an ask isn't the
  owner's, and when it compacts.
