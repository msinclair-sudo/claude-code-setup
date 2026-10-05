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

## The briefing (second version, 2026-10-05)

Seven sections, in this order. The CLI refuses a briefing that is over a cap or missing a section.

| section | holds | cap |
| --- | --- | --- |
| question | one sentence the owner can answer, in plain words | 300 chars |
| background | what is going on, what the owner would see, how it came up, why it matters; prose | 2000 chars |
| why yours | which of the four kinds, and why the tree can't settle it | 400 chars |
| checked | what was read and opened, what was verified, what couldn't be seen | 12 lines |
| options | 2–5 options: what changes, what it costs and risks, what it rules out | 500 chars each |
| recommendation | the asker's, credited to the asker; may be "none" | 500 chars |
| waiting | what is held back until the ruling, or "nothing" | 300 chars |

**Why it changed.** The first real briefing (`hover_mark_above_edges-1`) was accurate and
unreadable. With six sections at 120–200 characters it had no room to say what was going on, and
it used the tree's internal labels ("(b)", "the two-layer no-halo test", "7 of 13 sampled papers").
The fix adds a background section, raises the caps so an option can carry its consequence, and
gives the intermediary writing guidance: the owner's Voice section in its prompt, and four writing
skills (humanizer, de-densify, sentence-prose, google-devdocs-style) it reads before briefing. It
can also read the folders lanes hold live grants on, where the screenshots and diffs it couldn't
open were.

## Evidence (2026-10-05)

The intermediary attaches files the owner should see: `harness ask <id> --evidence PATH
--caption "..."`. The CLI copies each into `<state>/asks/evidence/<id>/`, because scratch folders
get swept and the GUI should never serve an arbitrary path. The Issues tab shows images inline
(click for full size) and text files (diffs, logs) as links. Evidence is deleted with the ask on
accept or reject; the ruling is the record.

## The record and the commands

An ask is a record in `~/.claude/harness/<slug>/asks/<id>.json`. It is always attached to a task:
the ruling has to land where a lead will read it. If no task exists yet, the asker writes the brief
first.

States: `asked` → `briefing` → `ready` (the owner's move) → `drafted` → removed by **accept** or
**reject**. `returned` (sent back to the asker) and `merged` (folded into another ask) end it
early.

| who | command | does |
| --- | --- | --- |
| rank 0 or a lead | `harness ask <task> --kind intent\|judgement\|action\|risk --question "..."` | opens an ask and prints the intermediary's address for a `SendMessage` nudge. Lanes are refused. |
| intermediary | `harness ask <id> --brief FILE` | sets the seven sections, checked against the caps; the state becomes `ready` |
| intermediary | `harness ask <id> --amend "..."` | rewrites the question with what the discussion added |
| intermediary | `harness ask <id> --draft "..."` | writes the draft ruling; the state becomes `drafted` |
| intermediary | `harness ask <id> --return "why"` / `--merge <other>` | sends the ask back, or folds it into another |
| owner (GUI) | `harness ask <id> --accept` / `--reject` | refused from inside any session, as `sweep` is, so only the owner's GUI or shell can sign |
| anyone | `harness ask --list` | the open asks; the GUI reads the same thing |

**Accept** attaches the (amended) question and the ruling to the task's brief as a `rulings` entry,
then removes the ask. `harness brief <task>` shows the rulings, and the task's lead gets one
orientation line when one lands. Rulings travel with the brief, so a swept task keeps them in the
archive.

**Reject** removes the ask. The asker gets one orientation line saying the owner rejected it, so it
doesn't ask again. Nothing else is kept.

## The intermediary's session and skill

- `harness intermediary` starts it, run in the project's repo (or with `--project NAME`): `claude`
  in that project's state directory, named `harness-intermediary-<project>`, with read access to
  that project only (repo, worktrees, state, live-grant folders) and read-only permissions.
  **One per project** (changed 2026-10-05 from one per machine): each sees only its own asks, and
  the Agents tab shows it beside that project's tree.
- Its own skill, `harness-intermediary`, says:
  - what to read first for an ask: the task's brief, the asker's notes, then the code;
  - when to send an ask back (the tree can settle it, or it's access, approval or a stalled session);
  - how to merge duplicates;
  - how to write the seven sections, for the owner rather than for the tree;
  - how to query the asker;
  - that it never decides, and never accepts.
- Askers learn `harness ask` from one line each in the root and downward skills.

## Commands for the owner, and waking on demand (2026-10-05)

The owner's ask: "if main wants to provide me with something it needs to go through the
intermediary … these actions won't need me to respond, I just need to click a button that confirms
the action was completed. OR I can directly type something to request further information."

- **Action asks with commands.** `harness ask owner --kind action --question "…" --run "cmd"`
  (up to 10 commands, 500 chars each). `owner` is rank 0's standing task: no brief needed, and no
  one else may use it. A lead's action ask on its own task may carry `--run` too.
- **Shown at once.** The Issues tab shows each command with a Copy button, **Done** (with an
  optional note), **Won't do** (reject), and a box to ask the intermediary about it. The commands
  are the point, so they don't wait for a briefing; the intermediary adds two or three lines on
  what they do with `--reply`.
- **Done** logs the action to `owner/done.jsonl`, leaves a stub the asker is told of once, and
  rings the asker's doorbell (`harness ring`), which wakes an idle rank 0 with no model in between.
- **A question** (`ask <id> --query`, owner only) goes into the ask's `thread` and wakes the
  intermediary. It answers with `--reply`, after asking the asker by `SendMessage` if it must.
- **The intermediary sleeps.** It now runs in the background. A new ask or an owner question wakes
  it. A stopped session is resumed with `claude --bg --resume <id> "<why>"` (no other flags: a
  background session keeps its saved options, and any flag starts a copy; measured 2026-10-05). It
  keeps its context across wakes. A busy one gets the reason through `intermediary/inbox.jsonl`.
  Every wake ends with `harness ask --idle`. That hands over the inbox, or, with nothing `asked`
  and no question open, stops the session 90s later. `harness intermediary` wakes it by hand, and
  `--fg` runs it in a terminal as before. The GUI's intermediary card and Issues header carry a
  **Start** button that does the same; once it is up they show `claude attach <id>` with Copy, so
  the owner can open it at once.

## Still to discuss

- Nothing blocks building the first version. Revisit the caps and sections after the first few
  real items.
