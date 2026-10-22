# Unseen notes set aside for evaluating the writing stage (written before the draw)

Approved by the owner on 2026-10-22, at gate A (`../v4/stageA/results.md`). Six notes are drawn now, before stage
C draws its held-out set, and are excluded from stage C's frame and from every consolidation evaluation. Nobody
reads them until the writing stage is evaluated.

- **Frame.** The held-out frame (`../heldout/frame.tsv`, 75 notes, made from metadata only), minus every note
  excluded there (development or read) and the eight notes drawn in the v3 held-out evaluation. The vault had no
  new result notes on 2026-10-22, so the frame is current.
- **Categories.** Assigned by the same rule as `../heldout/draw.py`. The parts of one research set are one unit.
- **How many:** category 3, 2 units; category 6, 1; category 7, 2; category 8, 1. None from categories 1, 2 or 4,
  which are scarce.
- **Soil or microbiology preferred, by title only.** Within a category, the draw is from the units whose file name
  matches `soil|microb|bacteri|archae|fung|16s|metagenom|genom|gene|nitrogen|denitrif|taxonom|communit`
  (case-insensitive), if there are at least as many as are needed; otherwise from the whole category.
- **The draw.** `random.Random(20261024).sample` over the eligible units of each category, in path order,
  categories in ascending order. Written to `setaside.md` by `draw_setaside.py`.
