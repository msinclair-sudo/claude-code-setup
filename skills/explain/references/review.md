# Review: render, check, fix (at most 3 rounds)

Tools first, eyes second. `x check` measures what a model judges poorly (overflow, overlap, small type, orphan numbers, network, timing). The fresh reader then judges what tools cannot: does the message come through, is anything misleading.

## A round
1. `x build <dir>` (narration clips are cached; for tier 4, `--only SceneA,SceneB` re-renders just those chapters and reuses the rest).
2. `x stills <dir>`: contact sheets in `checks/contact-*.png`.
3. `x check <dir> --round N`: faults block; warnings go to the reader.
4. The fresh reader: start a subagent with the Agent tool; give it the contact sheets, the one-sentence message, this file's checklist for the tier, and the round's warnings. Not the code, not the storyboard. Prompt:

   > These stills are an explanation meant to convey: "<message>". Say what you understand from them in one sentence. Then list problems as **blocking** (the message is wrong, unclear, or misleading; text unreadable; something overlaps or is cut off; a number contradicts another) or **minor**. Use the checklist. Be specific: which still, where.

5. The narrative reader (tiers 2 and 4, round 1, and again after the narration changes): a second fresh subagent gets only the narration in order, the audience and the message; no pictures. Prompt:

   > Read this narration as the audience. At every segment boundary, does the next step arrive with the question or reason that motivates it? List each gap (the question the viewer would have, and a bridging sentence of at most 20 words), then wording that is vague or awkward aloud, casual verbs where the field has a term, and terms used before they are explained.

   Stills cannot show these faults; the owner found them by watching (sixth exemplar: "the narrative still has too many gaps").
6. Fix the blocking items. Re-render only what changed. Next round.

A round is build, check **and** review. Rebuilding to clear `x check` faults before the reader sees anything is part of the same round; the count is of reviews. **Stop** when `x check` passes and the reader reports nothing blocking, or after round 3. Most of the gain is in round one; later rounds layer fixes on fixes. Report what is left.

## Checklists
**Every tier:** the reader's one-sentence summary matches the message; one idea per view; nothing decorative stays on screen; labels sit next to what they label; data vs illustrative is labelled.

**Charts:** the title states the point; ticks are sensible (no decimal years, no inverted axis by accident); axis titles are not cut off; bars start at zero or say why not; colour is not the only cue; the legend sits in the data where it can.

**Slides:** no text overflows or wraps unexpectedly (the commonest slide fault); a visual on every slide; no accent line under titles, no decorative stripes; nothing placeholder left in; the build order matches the narration.

**Interactive:** the default view carries the message without touching anything; each control changes something the text names; it still reads at 390 px.

**Text and terms:** every piece of on-screen text labels a thing, gives a number or term to keep, or names the step, in at most 4 words; no caption, legend or source card says in a sentence what the voice says (a frame that reads like a slide fails); new terms are defined in the subject's terms; a renamed thing keeps its old name in view; a chart's axes are said after its finding; each step of a method says why it is done (what it is for, how its setting is chosen, what the choice costs), not only that it is done.

**Animation:** a colour keeps one meaning from first frame to last (if blue is a taxon, it is never also a sample); every frame says whether it is schematic, simulated or data (`self.tag(...)`); every term the narration leans on appears on screen once; every object stays in frame; nothing overlaps unless it means to; each new element holds long enough to read; the narration names what is moving while it moves (stills cannot show this: read `checks/sync.json`, where each anchor and cue gives when the phrase is said and when its picture starts; `x check` faults a start later than the tolerance, a declared event never played, and events out of order, and the owner's viewing is the final check); nothing changes in silence for long.

**Narration:** pronunciation of technical terms (check against the lexicon in `narration.md`); no number read differently from how it is shown; captions match the speech.
