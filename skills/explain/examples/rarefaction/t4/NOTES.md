# Tier 4 narrated animation: what the loop did
- Round 1 (draft): the counter's digits ran into "taxa" (Integer() lays out once, in Manim's serif), and the axis numbers were serif beside Lato labels. Counters are now `always_redraw` Lato text pinned to a slot; axis numbers are Text labels. Integer() start values no longer trip the number check.
- Fresh reader: nothing blocking. Minor items fixed in round 3: `simulated` in a corner of both chapters, "67 fewer than the deep sample" on screen, the curve and the dot labelled, the cut marked "2,000 reads", "average" in the value label, narration "rises steeply, then slowly" (it had said "keeps climbing" over a curve that flattens).
- ExplainScene gained `track(obj, name)` for objects placed by axis coordinates, so order and overlap checks see them.
- Final: 51.5 s at 1080p60, two chapters, five narrated segments, captions merged from manim-voiceover's SRT.
- Noise to ignore: "/bin/sh: sox: Permission denied" (see references/install.md).
