# Diagnostic: facts only in the NFERT raw piece

Method and classes as in `raw-only-16S.md`. A row whose sourced content is only partly in the view piece is
classed by the missing part ("partial"). A qualifier the raw writer added without support stays "in both".

| Class | Count | Rows |
|---|---|---|
| No fact | 2 | 3, 37 |
| In both | 64 | |
| A. Unused | 2 | 14 (partial), 43 |
| B. Lost by the view | 2 | 11, 50 (partial) |
| C. Correctly excluded | 0 | |
| D. Lost by consolidation | 0 | |
| E. Writer's own | 2 | 33, 34 |
| **Total** | **72** | |

| # | Raw-only fact | Class | Evidence | Fact-check |
|---|---|---|---|---|
| 11 | the per-N figures are arithmetic, not separate measurements | B | manufacturing-energy.4: `class: deriv`, `holds: "not a separately measured quantity"`; the view keeps only "therefore" | supported |
| 14 | ecoinvent's 1.92 t CO₂e comes with 41 GJ primary energy | A (partial) | manufacturing-co2.2 statement | supported |
| 33 | average synthetic N carries about 12 t CO₂e/t N over its life "by their accounting" | E | the writer's division 23/1.9, attributed to the sources | unsupported claim |
| 34 | several times the factory figure | E | a comparison across system boundaries | number |
| 43 | legumes are the largest biological N input; effect on fertiliser demand documented (Ladha) | A | symbiotic-fixation.1 statement | supported |
| 50 | **in one system** (Ladha), 125-250 kg N cut fixation 81-86% | B (partial) | symbiotic-fixation.5 `holds: "one system reviewed by Ladha et al. (2022)"`; the view piece states it as general | supported |

**Citations the view piece drops** (counted "in both"; the finding is there, the source is not, because the
view drops `src`): rows 24 (IFA via Menegat), 25 (the process studies), 48 (Anglade; Ladha), 57 (Ladha); and
per-figure citations in rows 5, 7, 13, 14, 16, 17, folded into one collective citation.

**Reading.** Nothing was lost by consolidation. Both B losses are caveats held in fields the view drops: that a
figure is derived (`class`), and that a result comes from one system (`holds`). Without them the view piece
reads firmer than the evidence: the 81-86% suppression is stated as general, and the per-N figures are called
"the firmest numbers in this piece". The view tags manufacturing-co2.6 `(repl)` although its statement carries
the reviewer's per-N conversion: a standing shown for a claim that mixes a measured figure with a derived one.
The E items are the raw writer's own arithmetic; their absence from the view piece is a gain.
