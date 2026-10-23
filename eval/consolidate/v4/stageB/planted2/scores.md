## Catch rates by condition (W: with the omission hint; N: without, B1's setup)

| Edit type | n | Hint-visible | W1 | W2 | W either | W both | N1 | N2 | N either | N both | Intended kind, W / N (either) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| scope | 16 | 4 | 13 | 12 | 13/16 = 81% (57% to 93%) | 12 | 12 | 12 | 12/16 = 75% (51% to 90%) | 12 | 11 / 9 |
| counter | 7 | 5 | 5 | 4 | 5/7 = 71% (36% to 92%) | 4 | 5 | 5 | 5/7 = 71% (36% to 92%) | 5 | 5 / 5 |
| hedge | 8 | 5 | 8 | 8 | 8/8 = 100% (68% to 100%) | 8 | 8 | 8 | 8/8 = 100% (68% to 100%) | 8 | 8 / 8 |
| setting | 4 |  | 1 | 4 | 4/4 = 100% (51% to 100%) | 1 | 3 | 4 | 4/4 = 100% (51% to 100%) | 3 | 4 / 4 |
| number | 4 |  | 4 | 4 | 4/4 = 100% (51% to 100%) | 4 | 4 | 4 | 4/4 = 100% (51% to 100%) | 4 | 4 / 4 |
| standing | 2 |  | 2 | 1 | 2/2 = 100% (34% to 100%) | 1 | 2 | 1 | 2/2 = 100% (34% to 100%) | 1 | 2 / 2 |
| **Omissions, pooled** | 31 | 14 | 26 | 24 | 26/31 = 84% (67% to 93%) | 24 | 25 | 25 | 25/31 = 81% (64% to 91%) | 25 | 24 / 22 |
| **Controls (unedited): faulted** | 45 |  | 2 | 3 | 3/45 = 7% (2% to 18%) | 2 | 3 | 3 | 4/45 = 9% (4% to 21%) | 2 |  |

## Paired, with versus without (judge-pair either)

| | Only W | Only N | Both | Neither | Exact McNemar p |
|---|---|---|---|---|---|
| Omission plants caught | 1 | 0 | 25 | 5 | 1.00 |
| Hint-visible omission plants caught | 0 | 0 | 12 | 2 | 1.00 |
| Controls faulted | 0 | 1 | 3 | 41 | 1.00 |

## Decision rule (fixed before drawing)

- Omission catches summed over each condition's two judges: W 50, N 50 (of 62).
- Control faults summed over two judges: W 5, N 6 (of 90); W per judge W1 2, W2 3 (5% of 45 is 2.25).
- **NOT ADOPTED, STOP: noticeably more false alarms.**

## Every claim

| Claim | Type | Old hint | Omission line | Visible | W1 | W2 | N1 | N2 |
|---|---|---|---|---|---|---|---|---|
| 16S/beta-diversity.1 | control |  | yes |  | ok | ok | ok | ok |
| 16S/coverage-standardisation.3 | control |  | yes |  | ok | ok | ok | ok |
| 16S/denoising-clustering.7 | control |  | yes |  | ok | ok | ok | ok |
| 16S/denoising-clustering.8 | control |  | yes |  | ok | ok | ok | ok |
| 16S/overdispersion.1 | control |  |  |  | ok | ok | ok | ok |
| 16S/pcr.14 | control |  |  |  | ok | ok | ok | ok |
| 16S/pcr.15 | control |  |  |  | ok | ok | ok | ok |
| 16S/quality-filtering.6 | control |  |  |  | ok | ok | ok | ok |
| 16S/rare-biosphere.8 | control | yes | yes |  | ok | ok | ok | ok |
| 16S/sequencing-platform.1 | control |  |  |  | ok | ok | ok | ok |
| 16S/technical-variation.6 | control |  | yes |  | ok | ok | ok | ok |
| CB1/soil-carbon.2 | control |  |  |  | ok | ok | ok | ok |
| CB2/targeted-reconstruction.1 | control | yes |  |  | holds | holds | holds | holds |
| CB2/targeted-reconstruction.5 | control | yes |  |  | ok | ok | ok | ok |
| CB3/food-system.1 | control | yes |  |  | ok | ok | ok | ok |
| CB3/n2o.2 | control |  | yes |  | ok | ok | ok | ok |
| CB3/soils.6 | control |  | yes |  | ok | ok | ok | ok |
| H1-02/chimerism.1 | control |  |  |  | ok | ok | ok | ok |
| H1-02/core-genome-inference.3 | control | yes |  |  | ok | holds | ok | holds |
| H1-02/sequencing-depth.5 | control |  |  |  | ok | ok | ok | ok |
| H1-02/sequencing-depth.6 | control | yes |  |  | ok | ok | ok | ok |
| H1-05/contrast-size.1 | control | yes |  |  | ok | ok | ok | ok |
| H1-05/measurement-artefacts.2 | control |  | yes |  | ok | ok | ok | ok |
| H1-05/redundancy.1 | control | yes | yes |  | ok | ok | ok | ok |
| H1-06/metabolic-depth.8 | control |  | yes |  | ok | ok | ok | ok |
| H1-06/tau-d.1 | control | yes |  |  | ok | ok | ok | ok |
| H1-RES/accessory-function.20 | control |  |  |  | ok | ok | ok | ok |
| H1-RES/pangenome.2 | control |  |  |  | ok | ok | ok | ok |
| H1-RES/taxonomy-function.1 | control | yes |  |  | ok | ok | ok | ok |
| H2-01/gene-set-aggregation.9 | control | yes | yes |  | ok | ok | ok | ok |
| H2-01/levels-across.9 | control |  | yes |  | ok | ok | ok | ok |
| H2-01/levels-within.12 | control |  | yes |  | ok | ok | ok | ok |
| H2-01/other-field-transfer.5 | control |  | yes |  | ok | ok | ok | ok |
| H2-04/association-networks.12 | control |  | yes |  | ok | ok | ok | ok |
| H2-04/axis-agreement.4 | control |  | yes |  | conf | conf | conf | conf |
| H2-04/covariation-sources.2 | control |  | yes |  | ok | ok | ok | ok |
| H2-04/genome-linkage.2 | control |  | yes |  | ok | ok | ok | ok |
| H2-04/shared-ancestry.1 | control |  | yes |  | ok | ok | ok | ok |
| H2-04/shared-environment.5 | control | yes |  |  | ok | ok | holds | ok |
| H2-04/shared-environment.6 | control |  |  |  | ok | ok | ok | ok |
| NFERT/manufacturing-energy.1 | control |  |  |  | ok | ok | ok | ok |
| NFERT/symbiotic-fixation.4 | control |  |  |  | ok | ok | ok | ok |
| TAXRES/cross-kingdom-backbone.3 | control | yes | yes |  | ok | ok | ok | ok |
| TAXRES/gtdb-ncbi-divergence.3 | control |  | yes |  | ok | ok | ok | ok |
| TSL/altitude-ordering.3 | control | yes | yes |  | ok | ok | ok | ok |
| 16S/copy-number-correction.9 | counter |  | yes | yes | stronger | stronger | stronger | stronger |
| 16S/ploidy.11 | counter | yes | yes |  | ok | ok | ok | ok |
| 16S/relic-dna.2 | counter |  | yes | yes | stronger | stronger | stronger | stronger |
| 16S/sampling-storage.5 | counter |  | yes | yes | stronger | stronger | stronger | stronger |
| CB1/scarcity-claim.7 | counter |  | yes | yes | stronger | stronger | stronger | stronger |
| H2-01/levels-within.4 | counter |  |  |  | stronger | ok | stronger | stronger |
| H2-01/other-field-transfer.1 | counter |  | yes | yes | ok | ok | ok | ok |
| 16S/abundance-occupancy.2 | hedge |  | yes | yes | stronger | stronger | stronger | stronger |
| 16S/scaling-normalisation.1 | hedge |  | yes |  | stronger | stronger | stronger | stronger |
| GHOST/benchmark-regime.3 | hedge | yes | yes |  | stronger | stronger | stronger | stronger |
| H1-02/same-sample-isolate.5 | hedge | yes | yes | yes | stronger | stronger | stronger | stronger |
| H1-RES/n-cycle-hgt.13 | hedge |  | yes | yes | stronger | stronger | stronger | stronger |
| H1-RES/n-cycle-hgt.8 | hedge |  | yes | yes | stronger | stronger | stronger | stronger |
| H1-RES/redundancy.16 | hedge | yes | yes | yes | stronger | stronger | stronger | stronger |
| NFERT/mineralisation.2 | hedge | yes |  |  | stronger | stronger | stronger | stronger |
| 16S/abundance-distribution.2 | number | yes | yes |  | numbers | numbers | numbers | numbers |
| H1-06/depth-dependence.1 | number | yes |  |  | numbers | numbers | numbers | numbers |
| H1-06/genome-incompleteness.7 | number | yes | yes |  | numbers | numbers | numbers | numbers |
| TSL/c-tf-idf.1 | number | yes |  |  | numbers | numbers | numbers | numbers |
| 16S/copy-number-correction.5 | scope | yes | yes |  | stronger | stronger | stronger | stronger |
| 16S/core-microbiome.5 | scope |  | yes |  | numbers | numbers | numbers | numbers |
| 16S/differential-abundance.1 | scope |  | yes | yes | stronger | stronger | stronger | stronger |
| 16S/ploidy.21 | scope | yes | yes |  | stronger | stronger | stronger | stronger |
| 16S/technical-variation.3 | scope | yes |  |  | stronger | stronger | stronger | stronger |
| CB1/ghg-balance.4 | scope | yes |  |  | stronger | stronger | stronger | stronger |
| CB2/depth-axis.2 | scope | yes | yes | yes | stronger | stronger | stronger | stronger |
| CB2/marker-gap.4 | scope |  |  |  | numbers | numbers | numbers | numbers |
| H1-02/mobile-region-loss.5 | scope |  |  |  | stronger | ok | ok | ok |
| H1-02/sample-dependence.7 | scope |  | yes |  | ok | ok | ok | ok |
| H1-05/ordering.24 | scope | yes | yes | yes | stronger | stronger | stronger | stronger |
| H1-06/perturbation-response.9 | scope | yes | yes | yes | ok | ok | ok | ok |
| H1-06/uncontrolled-rank-studies.1 | scope |  | yes |  | stronger | absent | absent | absent |
| H1-RES/pangenome.11 | scope |  |  |  | ok | ok | ok | ok |
| H2-01/covariation-stability.12 | scope |  | yes |  | stronger | stronger | stronger | stronger |
| NFERT/symbiotic-fixation.2 | scope |  |  |  | stronger | stronger | stronger | stronger |
| CB2/marker-gap.1 | setting | yes |  |  | ok | holds | holds | holds |
| CB3/gwp-metric.4 | setting | yes |  |  | ok | holds | ok | holds |
| GHOST/feature-propagation.3 | setting | yes | yes |  | ok | holds | holds | holds |
| TSL/altitude-ordering.6 | setting | yes |  |  | holds | holds | holds | holds |
| 16S/compositional-analysis.4 | standing |  | yes |  | conf | conf | conf | conf |
| H1-RES/redundancy.11 | standing |  |  |  | stronger | ok | stronger | ok |

## Controls faulted by any judge: the adjudicator's reading (information only)

| Control | Faulted by | Adjudicator |
|---|---|---|
| H2-04/shared-environment.5 | N1 | holds |
| CB2/targeted-reconstruction.1 | W1, W2, N1, N2 | holds |
| H1-02/core-genome-inference.3 | W2, N2 | holds |
| H2-04/axis-agreement.4 | W1, W2, N1, N2 | conf |
