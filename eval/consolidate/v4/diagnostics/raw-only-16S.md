# Diagnostic: facts only in the 16S raw piece

One reader per topic (read-only), working from the raw piece, the view piece, the raw piece's fact-check, the
writer's view, the knowledge note and the raw notes. Each raw statement with factual content was matched against
the view piece. Each raw-only fact was traced: A unused (in the view, not used), B lost by the view (in the
knowledge note only in a field the view drops: holds, src, class, rating, trail), C correctly excluded
(do-not-say or a critic correction), D lost by consolidation (in a raw note, not in the knowledge note), E the
writer's own (in neither).

Rule here: "in both" when the view piece states the central finding. Minor figures inside a shared finding are
listed below the counts (all A).

| Class | Count | Rows |
|---|---|---|
| No fact | 4 | 2, 3, 66, 70 |
| In both | 56 | |
| A. Unused | 8 | 19, 25, 34, 35, 54, 57, 58, 60 |
| B. Lost by the view | 0 | |
| C. Correctly excluded | 1 | 38 (dns.14) |
| D. Lost by consolidation | 0 | |
| E. Writer's own | 1 | 47 |
| **Total** | **70** | |

| # | Raw-only fact | Class | Evidence | Fact-check |
|---|---|---|---|---|
| 19 | extraction distorted pair ratios up to 36.6-fold (mean 5.5), PCR less; 7-taxon vaginal mix | A | extraction.2 | supported |
| 25 | a cell holds 1 to hundreds of genomes in cultured species, by growth phase | A | ploidy.1, ploidy.5 | supported |
| 34 | chimeras 0.9% to 18.2% of reads at 30 cycles, by polymerase | A | chimeras.3 | supported |
| 35 | a fraction of a percent to several percent of reads misassigned, creating false presences | A | index-misassignment.3, .10 | supported |
| 38 | relative abundances varied far less between pipelines | C | dns.14 ("relative abundance is robust to the pipeline; counts of taxa are not") | dns |
| 47 | the counts carry no record of load | E | no entry; gap.6 lists the library-size and biomass relation as unknown; neither raw note says it | unsupported claim |
| 54 | a statistical argument that rarefied richness is biased (Willis) | A | rarefying.11 | supported |
| 57 | proportions and log-ratio distances stayed depth-sensitive | A | rarefying.3, compositional-analysis.2 | supported |
| 58 | RNA-seq scaling methods assume most taxa do not change | A | scaling-normalisation.1 | supported |
| 60 | Chao1 breaks when denoisers drop singletons | A | richness-estimators.3 | supported |

Raw-only details inside shared findings, all A: the 15% divergence threshold (row 28, copy-number-correction.3),
17.2% replicate overlap (40, technical-replicates.1), rarefying borrowed from ecology (51, rarefying.1), the 5%
false-positive result (52, rarefying.2-3), the disputed simulation design (53, rarefying.8), qPCR against flow
cytometry on mock and stool (64, absolute-quantification.12). Rows 26 and 39 are borderline; either would be A.

**Reading.** Nothing the raw writer used was lost by consolidation or hidden by the view. The view writer chose
other entries on the same points (a 22,000-word view of 410 claims). The one consolidation effect is row 38:
the raw piece repeats a wording the critic corrected, which dns.14 kept out of the view piece. 16S's raw piece
names few sources, so attribution did not separate the pieces here (neither has a reference list).
