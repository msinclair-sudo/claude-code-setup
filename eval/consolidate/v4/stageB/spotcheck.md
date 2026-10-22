# The owner's spot-check against the first-pass checker (B0)

The 20 entries of `../../v3/spot-check-16S.md` were drawn with seed 20261021 from the 16S note as built. The owner
judged them blind to the checker. The checker's first-pass verdicts were sealed in `spot-check-16S.checker.md` and
opened after the owner's verdicts were filed (2ce0b39). The owner's labels are mapped to fault kinds as the owner
gave them (2026-10-22). The owner had seen comments on entry 5 beforehand.

| # | Entry | Owner | Checker | Which way |
|---|---|---|---|---|
| 1 to 3, 7 to 9, 11 to 17, 19 | | ok | ok | agree (11 and 16: language, a readability point, not a fault) |
| 4 | primers.5 | ok | `absent`: "abstract only" not in the text | checker stricter: an addition |
| 5 | copy-number-correction.8 | `stronger`: drops "but not DNA mocks or most mock tests in one preprint" | ok | checker missed an omission (a counter-clause present in the cited A-141) |
| 6 | copy-number-correction.15 | `conf`/`critic`: `src` shows `repl` while `conf` is `single` | ok | checker missed fields that contradict each other |
| 10 | bias-consistency.1 | ok | `holds`: a setting not in the text | checker stricter: an addition |
| 18 | compositional-analysis.3 | `holds`: omits McLaren 2022 | `holds`: "model" not in the text | both fault it, for opposite reasons: the owner an omission, the checker an addition |
| 20 | dns.27 | ok for faithfulness; unreadable as a do-not-say entry | ok | agree on faithfulness; readability went to change 2 |

- **Agreement:** 16 of 20 (ok or fault). Each found 3 faults, and only entry 18 is shared, faulted for opposite
  reasons.
- **Reading:** the checker catches additions and misses omissions (dropped hedges and counter-evidence, fields
  that contradict each other), the riskier kind. That is the reason for B1's planted-fault test, weighted towards
  omissions, and for the omission hint as the first fix if B1 shows poor catch rates.
- **Effect on v4:**
  - `checker.md` now says that dropping a "but not …" or contrary finding is `stronger`, and that a `src` label
    contradicting `conf` is `conf`;
  - do-not-say entries are full sentences (format.md, change 2).
