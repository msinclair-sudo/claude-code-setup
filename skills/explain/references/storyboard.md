# Storyboard

The plan is written before any code, and `x lint` checks it. A plan that cannot say what each segment draws and says is not ready to build.

## Fields
- `title`, `message` (one sentence the reader can repeat), `audience`, `delivery` (`read` or `presented`).
- `tier`, `tier_reason` (why the tier below would not carry the message; required above 0).
- `voice` (tier 2), `default_view` and `controls` (tier 3), `numbers_ok` (incidental numbers needing no claim).
- `segments[]`: `id`, `role` (setting, mechanism, problem, resolution, limits), `visual` (what is drawn), `onscreen` (≤ 12 words), `narration` (≤ 35 words, about 13 s), `claims` (ids in `claims.yaml`), and:
  - tier 2: `step` = `"h.v.f"`, the slide and fragment where it plays (`f` = -1 before any fragment);
  - tier 4: `scene` (the Manim class), `anchors` (`{name: cell}`, cells A1-F4 on a 6×4 grid, A1 top left), `verify` (`inside_frame: all`, `no_overlap: all | [a, b]`, `order: [a, b]`, `hold_min_s: 2`).

## The token pass
Before any code, edit `tokens.json`: 4-6 colours with one accent, the typefaces, and a one-line layout concept. Data carries the colour; chrome stays quiet. Defaults read as generic; a deliberate choice of accent and type, made for this material, does not.

## The arc: setting first
Open with the **setting** before any problem: what the system is, what is really there, and how it is measured. A reader dropped straight into "two samples differ" has nothing to hang it on. Give each segment a `role`, in roughly this order:
- `setting`: the thing being studied, and what an ideal measurement would show;
- `mechanism`: how the measurement actually works, step by step;
- `problem`: where and how the measurement departs from the truth;
- `resolution`: what the method being explained does about it;
- `limits`: what it does not fix, and what it costs.

From tier 2 up, `x lint` warns when the first segment is not `setting`. (Owner review, 2026-10-20: the first exemplars "dive straight into it"; the rebuilt tier 4 starts from a droplet of soil.)

## Writing segments
- One idea per segment. If the narration needs "and then", split it.
- The narration says what the picture shows *while* it shows it; the on-screen text is a label, not a sentence the voice also reads in full.
- Order: the question, the thing that answers it, the consequence.
- Each number in `onscreen` or `narration` has a claim id beside it.

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
