# Storyboard

The plan is written before any code, and `x lint` checks it. A plan that cannot say what each segment draws and says is not ready to build.

## Fields
- `title`, `message` (one sentence the reader can repeat), `audience`, `delivery` (`read` or `presented`).
- `tier`, `tier_reason` (why the tier below would not carry the message; required above 0).
- `voice` (tier 2), `default_view` and `controls` (tier 3), `numbers_ok` (incidental numbers needing no claim).
- `segments[]`: `id`, `role` (setting, mechanism, problem, resolution, limits), `visual` (what is drawn), `onscreen` (the frame's labels, separated by `;`, each at most 4 words), `narration` (≤ 35 words, about 13 s), `claims` (ids in `claims.yaml`), and:
  - tier 2: `step` = `"h.v.f"`, the slide and fragment where it plays (`f` = -1 before any fragment);
  - tier 4: `scene` (the Manim class), `anchors` (`{name: cell}`, cells A1-F4 on a 6×4 grid, A1 top left), `verify` (`inside_frame: all`, `no_overlap: all | [a, b]`, `order: [a, b]`, `hold_min_s: 2`), `sync` (`{event: phrase}`: each event the narration names, by a phrase that occurs once in it; at least the one the first sentence names; the scene's `play(sync=...)` starts on it). Storyboard-level `sync_tolerance` (seconds, default 0.5).
  - tiers 2 and 4, optional: `pace` (`{2: {pause: 1.2, speed: 0.9}}`): per sentence, numbered from 1, the silence after it in seconds (not on the last sentence: `pause_after` sets that) and a multiplier on the voice's speed. Unset, a sentence gets the storyboard's sentence pause and the voice's speed.

## The token pass
Before any code, edit `tokens.json`: 4-6 colours with one accent, the typefaces, and a one-line layout concept. Data carries the colour; chrome stays quiet. Defaults read as generic; a deliberate choice of accent and type, made for this material, does not.

## The arc: setting first
Open with the **setting** before any problem: what the system is, what is really there, and how it is measured. A reader dropped straight into "two samples differ" has nothing to hang it on. Give each segment a `role`, in roughly this order:
- `setting`: the thing being studied, and what an ideal measurement would show;
- `mechanism`: how the measurement actually works, step by step;
- `problem`: where and how the measurement departs from the truth;
- `distil`: one plain sentence that restates what was just shown, said over a still picture, before the next idea;
- `resolution`: what the method being explained does about it;
- `limits`: what it does not fix, and what it costs.

From tier 2 up, `x lint` warns when the first segment is not `setting`, and when a chapter of three or more segments has no `distil`. (Owner reviews, 2026-10-20: the first exemplars "dive straight into it"; after a concept is taught "it needs to be distilled" before the next.) A distil line is the owner's rule: recaps in narrated video have not been tested (design-rules, NP).

## Chapters
Order the chapters as causes and consequences, a problem and its answer, or a comparison, not as a list of topics: the same content was recalled better in organised forms. Each chapter ends on a distil line and a visible boundary (the stage clears, the next title appears), then the chapter pause.

**Every step answers a question the viewer now has.** Write it on the chapter's first segment as `question:` (`x lint` warns when it is missing), and let the narration voice it or set it up: the last chapter's distil raises it, the new chapter's first sentence answers it. Owner review of the sixth exemplar: the soil chapter ended on "this is the truth an experiment sets out to measure" and the next began "First, we pull the DNA out of the cells": "there's no connection between counting taxa and extracting DNA. There's a question missing: how do we count the taxa in the first place?" The chain should read as want, obstacle, so: we want the cells of each taxon; we can't count them by eye; so we extract their DNA and read one gene. Check every segment boundary the same way, not only the chapters: a step that starts without its reason is a gap.

## Writing segments
- One idea per segment. If the narration needs "and then", split it.
- Spoken sentences of about 20 words at most; plain words; talk to the viewer ("you", "we"). `x lint` warns past 22 words.
- One new term per segment: say it, show it, use it again in the next segment.
- Come back to the subject in every segment: the soil, this sample, the gene, by name.
- Slow down on the facts the explanation rests on: give a key number its own segment, with what it means for the subject, rather than passing it in a clause.
- The narration says what the picture shows *while* it shows it; the on-screen text names the things in the picture, never the narration itself, reworded or not (text identical to the narration impaired learning; `x lint` warns).
- Order: the question, the thing that answers it, the consequence.
- Each number in `onscreen` or `narration` has a claim id beside it.

## On-screen text has a job
Not everything said is shown, and not everything shown is said (owner review of the third exemplar, 2026-10-21: "text on screen has to have purpose... they're kinda just floating text"). The aim is a 3Blue1Brown video, not a narrated slide deck: the picture carries the idea, the voice explains it, and text only names what is drawn. Owner review of the fifth exemplar: "we're doing the classic bad thing in presentations, and reading from the slides. Slides should complement the narration, not be the same." A piece of text earns its place by doing one of these, in at most 4 words (`x lint` and `x check` enforce it):
- **labels a thing**, beside it or on it (a region of a gene, a bar, a bin); never off to the side;
- **gives a number or a term** the viewer must keep (a key value, a word the next segment uses);
- **names the step**: one short heading per step at the top left (signalling helped, design-rules NP).

A caption, legend or source card that says in a sentence what the voice says does none of these; leave it out. When a frame needs a fact from the literature, draw it: "harder shaking gave up to 400% more Gram-positive DNA" is two bars and "+400%"; "2% of taxa hold 41% of reads" is one bar split at 41%; three pipelines' ASV counts are three bars. Mark it `data` in the corner tag, not in a sentence. Text pops in (0.3 s, `Appear`) when the voice reaches it and holds still; it is never written letter by letter.

## Explaining terms and charts
- **New terms are defined in the subject's own terms**: "conserved" is *almost the same in every bacterium, so one primer fits them all*; "variable" is *different from taxon to taxon, so it tells them apart*. Use the field's names ("variable region", "V4", "read pair"), not paraphrases.
- **A renamed thing keeps its old name in view**: when the 16S rRNA gene's variable region becomes "the barcode", say so and label it "barcode: a variable region of the 16S rRNA gene".
- **Introduce before use**: a term the viewer needs later (read pairs) is introduced at the step where it arises (sequencing), not where it is first needed.
- **A chart is explained in this order**: the finding first ("in one study, ..."), then how the picture shows it ("along the bottom is ..., up the side ..., each dot is one taxon").
- **A step is explained by its reason, not only named**: say what it is for, what goes wrong without it, how its setting is chosen, and what that choice costs. Owner review of the fourth exemplar: read filtering "should be stated why it's done, not just that it is done": the barcode has an expected length and taxa differ by a few bases; trimming low-quality ends and off-target copies make other lengths; the cut-offs are set by eye and judgement, the same for every sample, so there is always a trade-off.
- **Use the field's usual plot** for a quantity (read lengths: a histogram, length along the bottom, number of reads up the side, with the cut-off drawn on it).
- **Show a relative change directly**: when what matters is how two things changed against each other, take them out of the full chart and set them side by side, with the gap or ratio written between them, and let that value change as they change.

## Words that carry a field meaning
A word the audience's field uses technically means that, and only that; a word the field uses in two senses gets replaced by one that has one. Check each before the fact-check (`references/accuracy.md`). The rarefaction exemplar called the taxa with most cells in one sample "common" and the rest "rare". The owner read those as how widely a taxon is found, and a taxon dominant in one soil can be scarce across soils. The field is split: in 181 rare-biosphere articles, 37% gave no clear definition, and most of the rest meant low relative abundance in a sample (often under 0.1%), while "core" and "prevalent" mean occupancy across samples (MB-02 review, vault `Topics/Biology/Research/Results`). So say "abundant", "dominant", "low-abundance" for counts in one sample, and "widespread", "found in few samples" for occupancy. Other traps: "significant" (statistics), "diversity" (richness or evenness?), "copies" (per genome or per cell?), "sample" (a soil core or a draw of reads?).

## Example (tier 4, one segment)
```yaml
title: "How two samples get a distance"
message: "The distance between two samples is the number of steps up the ontology to their first shared parent."
audience: "ecologists who know the samples, not the ontology"
delivery: presented
tier: 4
tier_reason: "the walk up the tree is a process; a static tree shows the answer but not how it is reached"
segments:
  - id: s2
    scene: Walk
    visual: "soil's path climbs one parent at a time; sediment's climbs from the other side"
    onscreen: "first shared parent"
    narration: "Each sample climbs one parent at a time. The first parent they share is where the paths meet."
    claims: [c2]
    anchors: {tree: B1, soil: B4, sediment: E4, label: D1}
    verify: {inside_frame: all, no_overlap: [soil, sediment, label], order: [soil, sediment], hold_min_s: 2}
```
