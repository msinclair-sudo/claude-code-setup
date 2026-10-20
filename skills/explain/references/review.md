# Review: render, check, fix (at most 3 rounds)

Tools first, eyes second. `x check` measures what a model judges poorly (overflow, overlap, small type, orphan numbers, network, timing). The fresh reader then judges what tools cannot: does the message come through, is anything misleading.

## A round
1. `x build <dir>` (only what changed rebuilds quickly: narration clips are cached).
2. `x stills <dir>`: contact sheets in `checks/contact-*.png`.
3. `x check <dir> --round N`: faults block; warnings go to the reader.
4. The fresh reader: start a subagent with the Agent tool; give it the contact sheets, the one-sentence message, this file's checklist for the tier, and the round's warnings. Not the code, not the storyboard. Prompt:

   > These stills are an explanation meant to convey: "<message>". Say what you understand from them in one sentence. Then list problems as **blocking** (the message is wrong, unclear, or misleading; text unreadable; something overlaps or is cut off; a number contradicts another) or **minor**. Use the checklist. Be specific: which still, where.

5. Fix the blocking items. Re-render only what changed. Next round.

A round is build, check **and** review. Rebuilding to clear `x check` faults before the reader sees anything is part of the same round; the count is of reviews. **Stop** when `x check` passes and the reader reports nothing blocking, or after round 3. Most of the gain is in round one; later rounds layer fixes on fixes. Report what is left.

## Checklists
**Every tier:** the reader's one-sentence summary matches the message; one idea per view; nothing decorative stays on screen; labels sit next to what they label; data vs illustrative is labelled.

**Charts:** the title states the point; ticks are sensible (no decimal years, no inverted axis by accident); axis titles are not cut off; bars start at zero or say why not; colour is not the only cue; the legend sits in the data where it can.

**Slides:** no text overflows or wraps unexpectedly (the commonest slide fault); a visual on every slide; no accent line under titles, no decorative stripes; nothing placeholder left in; the build order matches the narration.

**Interactive:** the default view carries the message without touching anything; each control changes something the text names; it still reads at 390 px.

**Animation:** every object stays in frame; nothing overlaps unless it means to; each new element holds long enough to read; the narration names what is moving while it moves; nothing changes in silence for long.

**Narration:** pronunciation of technical terms (check against the lexicon in `narration.md`); no number read differently from how it is shown; captions match the speech.
