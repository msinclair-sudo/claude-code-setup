---
name: explain
description: Make a research report or technical explanation at the lowest level of effort that carries the message, from a one-page note through a figure report, stepped slides (optionally narrated with local text to speech) and an interactive page with reactive graphs, up to a narrated Manim animation. Plans first (storyboard and a claims ledger), checks every number against its source with a reader that never sees the render, renders, measures the result in a browser or the video, and always leaves a static version that can be published as plain HTML. Use when the user invokes /explain or asks to explain, present, report on, visualise, animate or narrate a method, result or system.
allowed-tools: Bash, Read, Write, Edit, Agent
---

# explain

Pick the lowest tier that carries the message. Most explanations are tier 0 or 1. A tier is earned: write in `storyboard.yaml: tier_reason` why the tier below would not do.

| Tier | Make it when | Output |
|---|---|---|
| 0 note | the answer is a fact, a number or a decision | `index.html` |
| 1 figure report | something has to be seen; the reader goes at their own pace | page + 1-5 figures |
| 2 stepped slides | the explanation builds in order; add `--voice` when each step is mainly a picture | reveal deck, narration, captions |
| 3 interactive page | the reader must explore one parameter, many series, or uncertainty, **and** the default view already carries the message | Plotly page |
| 4 narrated animation | what must be understood is a **change** (a process, a transformation), watched narrated and system-paced, under 6 minutes | mp4, captions, player page |

Why the ladder: animation beats static pictures only for change, only when system-paced, and the gain vanishes when the reader controls the pace; few readers touch interactive controls; polish raises how well people *think* they understood, not how well they did. `references/design-rules.md` has the effects and their strength.

## Workflow

Run everything through `x` (`~/.claude/skills/explain/scripts/x`). Check the machine first: `bash ~/.claude/skills/explain/scripts/check.sh --tier N`.

1. **Brief.** `x new <dir> --tier N --title "…" [--voice]`, then fill `brief.md`: audience, the one-sentence message, delivery (`read` or `presented`), sources. **Sources come first, not memory:** when the explanation is not built from the user's own data or documents, run `/research-brief` on the subject and write the storyboard from its result note. A fact-check only tests the claims you wrote down; it cannot find the steps you left out.
2. **Storyboard, before any code.** Fill `storyboard.yaml` (schema and an example: `references/storyboard.md`). Do the token pass now: edit `tokens.json` (4-6 colours, one accent, the typefaces, a one-line layout concept); for anything beyond the defaults, read the frontend-design skill first. `x lint <dir>` must pass.
3. **Claims before rendering.** Every number and factual statement goes in `claims.yaml` with its source and kind. Then run the blind fact-check in `references/accuracy.md`: a fresh subagent sees only the claims and the sources, never the render.
4. **Build.** Write `src/` for the tier (starters are already there), using that tier's guide. Read `/dataviz` before any chart code. `x build <dir> [--draft]`.
5. **Render, check, fix: at most 3 rounds.** `x stills <dir>`, `x check <dir> --round N`, then one fresh-reader review of the contact sheet (`references/review.md`). Fix blocking faults, rebuild, next round. Stop when the checks pass and the reader has nothing blocking, or after round 3; report what is left.
6. **Deliver.** `x fallback <dir>` writes `static/`, which passes the harness's publish check. Hand over `build/` and `static/`, say the tier and why, and list open warnings.

## Which reference to read

- Every tier: `references/storyboard.md`, `references/accuracy.md`, `references/review.md`.
- Tier 1: `references/t1-figures.md`. Tier 2: `references/t2-slides.md` (+ `narration.md` with `--voice`). Tier 3: `references/t3-interactive.md`. Tier 4: `references/t4-animation.md` and `references/narration.md`.
- The evidence behind the rules: `references/design-rules.md`. Installing or repairing the tools: `references/install.md`.

## Hard rules

- **Every number shown or spoken is in `claims.yaml`.** `x check` fails on orphans. Illustrative numbers are labelled illustrative on the page.
- **Captions always on** for narration; the transcript ships with it. Never speed narration above the voice's normal rate.
- **No decoration that stays on screen.** Every visual element carries information or goes.
- **Say whether a depiction is the actual data, a simulation or an illustration**, with a visible label on every view (`<span class="x-label">data</span>`, `simulated`, `illustrative`). A truncated axis carries a visible note.
- **One idea per slide or segment**; at most 12 words on screen and 35 words of narration per segment.
- **Visible prose goes through humanizer** before the last round.
- **PPTX only when asked:** build it from the same storyboard with the pptx skill.
