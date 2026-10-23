# B2: the hint effect

100 of the 300 baseline entries (60 with a hint line, 40 without), seeds subset 20261034, order 20261035, adjudication order 20261036. W1 is the baseline checker's verdict; W2 a fresh checker with hints; N1 and N2 fresh checkers without hints, packets identical apart from the hint lines. Agreement is on ok against fault.

## Agreement

| Pair | All 100 | Hinted | Not hinted |
|---|---|---|---|
| W1 and W2 | 78 | 42/60 | 36/40 |
| N1 and N2 | 81 | 47/60 | 34/40 |
| W1 and N1 | 89 | 51/60 | 38/40 |
| W1 and N2 | 78 | 44/60 | 34/40 |
| W2 and N1 | 83 | 47/60 | 36/40 |
| W2 and N2 | 88 | 50/60 | 38/40 |

## Fault rates by run

| Run | All | Hinted | Not hinted | Kinds |
|---|---|---|---|---|
| W1 | 45/100 | 39/60 | 6/40 | holds 30, absent 13, conf 1, stronger 1 |
| W2 | 23/100 | 21/60 | 2/40 | holds 18, stronger 2, absent 2, conf 1 |
| N1 | 36/100 | 30/60 | 6/40 | holds 27, absent 5, stronger 3, conf 1 |
| N2 | 25/100 | 23/60 | 2/40 | holds 13, absent 8, stronger 2, numbers 1, critic 1 |

## Discordant entries (30), with the adjudicator's reading (no hints, blind to condition)

| Entry | Hint | W1 | W2 | N1 | N2 | Adjudicator |
|---|---|---|---|---|---|---|
| 16S/denoising-clustering.4 |  | holds | holds | holds | ok | holds |
| 16S/dns.20 | yes | absent | ok | absent | absent | absent |
| 16S/ploidy.8 | yes | holds | ok | holds | critic | critic |
| CB1/lime-requirement.13 |  | ok | ok | ok | numbers | stronger |
| CB2/dns.3 | yes | absent | ok | absent | absent | absent |
| CB3/farm-gate.1 | yes | holds | ok | holds | ok | holds |
| CB3/food-system.12 |  | absent | ok | absent | ok | absent |
| GHOST/benchmark-regime.2 | yes | absent | ok | holds | holds | absent |
| GHOST/low-variance-defect.2 | yes | holds | ok | ok | absent | absent |
| H1-02/bounding-comparisons.7 | yes | absent | ok | ok | ok | ok |
| H1-02/chimerism.2 | yes | absent | ok | ok | ok | absent |
| H1-02/core-genome-inference.1 | yes | absent | ok | ok | absent | absent |
| H1-05/annotation.3 | yes | absent | holds | ok | holds | absent |
| H1-05/ordering.7 | yes | holds | holds | holds | ok | holds |
| H1-06/perturbation-response.6 | yes | holds | ok | holds | ok | holds |
| H1-06/taxonomies.1 | yes | holds | ok | ok | ok | ok |
| H1-RES/taxonomy-function.7 | yes | holds | ok | ok | ok | ok |
| H2-01/covariation-stability.8 | yes | holds | holds | holds | ok | holds |
| H2-01/direct-dimension.5 |  | ok | ok | stronger | ok | absent |
| H2-01/expression-dimension.3 | yes | conf | conf | conf | ok | conf |
| H2-01/levels-within.14 | yes | holds | holds | ok | ok | absent |
| H2-04/aggregation-artefacts.3 |  | holds | ok | holds | ok | holds |
| H2-04/covariance-partition.4 | yes | holds | ok | ok | ok | ok |
| NFERT/manufacturing-energy.3 |  | absent | ok | ok | ok | absent |
| TAXRES/cross-kingdom-backbone.1 | yes | holds | ok | holds | ok | holds |
| TAXRES/gtdb.1 | yes | holds | ok | holds | ok | holds |
| TAXRES/name-resolution.1 | yes | holds | ok | holds | ok | holds |
| TAXRES/name-resolution.3 |  | holds | ok | holds | ok | holds |
| TAXRES/ncbi-lpsn.1 | yes | holds | ok | holds | ok | holds |
| TSL/altitude-ordering.4 | yes | holds | ok | holds | ok | holds |

## On the discordant entries, runs against the adjudicator (summed over each condition's two runs)

| | With hints (W1, W2) | Without (N1, N2) |
|---|---|---|
| faulted, adjudicator ok | 4 | 0 |
| passed, adjudicator fault | 22 | 25 |
