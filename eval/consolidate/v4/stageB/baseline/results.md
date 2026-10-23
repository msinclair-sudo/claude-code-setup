# B2: the re-scored v3 baseline

Checker: frozen B1 setup (checker.md as at 7b5a0b3, with hints). 300 entries, five fresh checkers, seeds draw 20261032, order 20261033, bootstrap 20261037 (10,000 resamples within note and stratum).

## First-pass fault rate

- **Re-scored v3, whole-note estimate (strata weighted): 35.9% (bootstrap 95% 30.8% to 41.2%).**
- In the sample, unweighted: 108/300 = 36.0% (Wilson 30.8% to 41.6%).
- v3 as reported (its own first-pass checkers, all 1697 entries): 206/1697 = 12.1%.

## Per 100 entries, by fault kind (whole-note estimate, bootstrap 95%)

| Kinds | Per 100 | 95% interval | In the sample |
|---|---|---|---|
| holds + absent | 33.6 | 28.7 to 38.7 | 102 |
| stronger + numbers | 1.4 | 0.2 to 3.0 | 4 |
| conf | 0.4 | 0.0 to 1.2 | 1 |
| critic | 0.5 | 0.0 to 1.5 | 1 |
| merged | 0.0 | 0.0 to 0.0 | 0 |

## By note and stratum

| Note | Entries | Passed by v3: full, drawn, faulted | Rest: full, drawn, faulted | Note estimate |
|---|---|---|---|---|
| 16S | 460 | 327, 39, 8 | 133, 17, 12 | 35% |
| CB1 | 107 | 90, 16, 2 | 17, 4, 2 | 18% |
| CB2 | 64 | 54, 12, 2 | 10, 3, 2 | 24% |
| CB3 | 85 | 75, 15, 7 | 10, 3, 1 | 45% |
| GHOST | 37 | 29, 10, 1 | 8, 3, 1 | 15% |
| H1-02 | 126 | 96, 16, 5 | 30, 6, 6 | 48% |
| H1-05 | 142 | 94, 15, 6 | 48, 8, 6 | 52% |
| H1-06 | 138 | 118, 19, 6 | 20, 4, 3 | 38% |
| H1-RES | 122 | 114, 19, 3 | 8, 2, 1 | 18% |
| H2-01 | 182 | 155, 23, 12 | 27, 5, 3 | 53% |
| H2-04 | 127 | 81, 14, 3 | 46, 8, 2 | 23% |
| NFERT | 45 | 40, 12, 2 | 5, 2, 0 | 15% |
| TAXRES | 27 | 25, 11, 6 | 2, 1, 1 | 58% |
| TSL | 35 | 26, 9, 2 | 9, 4, 3 | 36% |

## Faults on entries the v3 checker passed, and on those it faulted

- v3 passed: 65/230 faulted now
- the rest (do-not-say and v3-faulted): 43/70 faulted now
- of v3-faulted entries in the sample, faulted again: 40/44

## Every `stronger` and `numbers` fault (gate B, criterion 3)

| Entry | Kinds | Checker's reason |
|---|---|---|
| 16S/ploidy.15 | stronger | stronger: the text says "No source I found measured 16S copies per cell", and the entry drops "I found" to "No source measured". |
| H1-06/metabolic-depth.12 | stronger | stronger: the entry gives absolute depths under "replicates across independent datasets" but drops the text's "the absolute depths are not" [consistent] and "inconsistent in absolute depth between datasets and trees". |
| H1-RES/accessory-function.23 | stronger | stronger: the text says "This pattern suggests that a large fraction of accessory content represents ...", and the entry drops "suggests" to state it as fact. |
| TSL/information-content.1 | stronger | stronger: the entry drops the caveat that comes with the confidence rating, "Caveat: needs a unified root; WordNet has none naturally." |

## Kinds in the sample

holds 79, absent 23, stronger 4, conf 1, critic 1
