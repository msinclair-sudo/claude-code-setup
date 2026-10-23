# B2: the re-scored v3 baseline

Checking procedure (frozen): checker.md and hints as at 7b5a0b3; 60-entry packets; two fresh checkers per packet, a fault from either counted. 300 entries, seeds draw 20261032, order 20261033, bootstrap 20261037 (10,000 resamples within note and stratum).

## First-pass fault rate

- **Re-scored v3, whole-note estimate (strata weighted): 38.6% (bootstrap 95% 33.4% to 43.9%).**
- In the sample, unweighted: 118/300 = 39.3% (Wilson 34.0% to 45.0%).
- v3 as reported (its own first-pass checkers, all 1697 entries): 206/1697 = 12.1%.

- Each checker set alone (whole-note estimate): first 35.9%, second 35.6%. In the sample: first 108, second 110, either 118, both 100.
- The two checkers agree (ok against fault) on 282 of 300 entries.

| Packet | First checker | Second checker | Either | Agree |
|---|---|---|---|---|
| 1 | 15 | 19 | 19 | 56 |
| 2 | 19 | 19 | 21 | 56 |
| 3 | 24 | 25 | 25 | 59 |
| 4 | 22 | 22 | 22 | 60 |
| 5 | 28 | 25 | 31 | 51 |

## Per 100 entries, by fault kind (whole-note estimate, bootstrap 95%)

| Kinds | Per 100 | 95% interval | In the sample |
|---|---|---|---|
| holds + absent | 36.1 | 31.1 to 41.3 | 111 |
| stronger + numbers | 1.9 | 0.5 to 3.6 | 6 |
| conf | 0.4 | 0.0 to 1.2 | 1 |
| critic | 1.0 | 0.0 to 2.5 | 2 |
| merged | 0.0 | 0.0 to 0.0 | 0 |

## By note and stratum

| Note | Entries | Passed by v3: full, drawn, faulted | Rest: full, drawn, faulted | Note estimate |
|---|---|---|---|---|
| 16S | 460 | 327, 39, 8 | 133, 17, 12 | 35% |
| CB1 | 107 | 90, 16, 2 | 17, 4, 2 | 18% |
| CB2 | 64 | 54, 12, 3 | 10, 3, 2 | 32% |
| CB3 | 85 | 75, 15, 8 | 10, 3, 2 | 55% |
| GHOST | 37 | 29, 10, 2 | 8, 3, 1 | 23% |
| H1-02 | 126 | 96, 16, 6 | 30, 6, 6 | 52% |
| H1-05 | 142 | 94, 15, 6 | 48, 8, 6 | 52% |
| H1-06 | 138 | 118, 19, 6 | 20, 4, 3 | 38% |
| H1-RES | 122 | 114, 19, 3 | 8, 2, 1 | 18% |
| H2-01 | 182 | 155, 23, 14 | 27, 5, 3 | 61% |
| H2-04 | 127 | 81, 14, 4 | 46, 8, 2 | 27% |
| NFERT | 45 | 40, 12, 2 | 5, 2, 1 | 20% |
| TAXRES | 27 | 25, 11, 7 | 2, 1, 1 | 66% |
| TSL | 35 | 26, 9, 2 | 9, 4, 3 | 36% |

## Faults on entries the v3 checker passed, and on those it faulted

- v3 passed: 73/230 faulted now
- the rest (do-not-say and v3-faulted): 45/70 faulted now
- of v3-faulted entries in the sample, faulted again: 40/44

## Every `stronger` and `numbers` fault (gate B, criterion 3)

| Entry | Kinds | Checker's reason |
|---|---|---|
| 16S/ploidy.15 | stronger | stronger: the text says "No source I found measured 16S copies per cell", and the entry drops "I found" to "No source measured". / stronger: the entry says "No source measured 16S copies per cell directly", dropping the text's hedge "No source I found measured". |
| CB3/dns.2 | numbers | numbers: the why gives "published estimates range from about 1.5% to 4.1%" for agricultural soils, dropping the text's definition "estimates of N₂O from agricultural soils as a share of global GHG". |
| H1-06/dns.6 | absent, numbers | absent: the quoted statement's "about otu94" and "tau_D about 0.017 to 0.02" are not in the text, which gives "otu97-to-genus rise" and "tau_D ~0.017". / numbers: the quoted phrasing gives "tau_D about 0.017 to 0.02" and "otu94", while the text gives only "tau_D ~0.017" and an "otu97-to-genus rise". |
| H1-06/metabolic-depth.12 | stronger | stronger: the entry gives absolute depths under "replicates across independent datasets" but drops the text's "the absolute depths are not" [consistent] and "inconsistent in absolute depth between datasets and trees". / stronger: the entry gives absolute depths (e.g. "sulfate reduction 0.039") as part of the replicating pattern but drops the text's "the absolute depths are not" consistent between datasets. |
| H1-RES/accessory-function.23 | stronger | stronger: the text says "This pattern suggests that a large fraction of accessory content represents ...", and the entry drops "suggests" to state it as fact. / stronger: the text says "This pattern suggests that a large fraction...", and the entry drops "suggests" to state it flatly. |
| TSL/information-content.1 | stronger | stronger: the entry drops the caveat that comes with the confidence rating, "Caveat: needs a unified root; WordNet has none naturally." / stronger: the entry drops the text's condition "Caveat: needs a unified root; WordNet has none naturally." |

## Kinds in the sample

holds 85, absent 32, stronger 4, numbers 2, critic 2, conf 1
