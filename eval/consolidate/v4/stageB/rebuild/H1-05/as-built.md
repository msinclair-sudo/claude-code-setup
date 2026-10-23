---
type: knowledge
title: Functional and taxonomic turnover in soil microbial communities
inputs:
  - H1-05: PhD/Proposal/Research/Results/Functional versus taxonomic turnover in soil microbial communities comparisons, dependence on functional unit and metric, and what null models conclude.md
refs: PhD/Proposal/Refs/Refs.bib
built: 2026-10-23
status: draft
tags:
  - research
  - knowledge
---
# Functional and taxonomic turnover in soil microbial communities

> [!abstract] Note Role
> **Contains**: what the research in the inputs found, one claim per finding, organised by concept, with the
> standing, conditions and sources the notes give, and links back to where each was verified.
> **Cannot contain**: anything not in the inputs (except background entries, marked), verification (it stays
> in the result notes), or guidance on writing, story or order of telling.
> **Order**: the concepts are listed in one valid ordering of the `needs` graph. It has no narrative meaning;
> other valid orderings are equally correct.

## Inputs
| id | note | critique | citations | standing labels | run record | omission check |
|---|---|---|---|---|---|---|
| H1-05 | [[Functional versus taxonomic turnover in soil microbial communities comparisons, dependence on functional unit and metric, and what null models conclude]] | yes | labelled (access; class; standing) | no | no | exact |

## Concepts

### functional-profile: what turnover and "function" mean in these comparisons
needs: none

- **functional-profile.bg1** The distance-based test of homogeneity of multivariate dispersions (PERMDISP) compares the spread of groups of samples, measured with any dissimilarity measure, as distances to the group centroid or spatial median; it is a multivariate extension of Levene's test.
  kind: background · ref: andersonDistancebasedTestsHomogeneity2006 · check: DOI 10.1111/j.1541-0420.2005.00440.x resolves on Crossref (Biometrics 62(1):245-253); stated in the abstract (Europe PMC record: "Distance-based tests of homogeneity of multivariate dispersions, which can be based on any dissimilarity measure of choice"; "straightforward multivariate extensions of Levene's test")
- **functional-profile.1** Turnover here means between-sample dissimilarity. "Function" in the soil literature means several different things: shotgun reads annotated to SEED, KEGG or eggNOG; GeoChip probe arrays; gene-family counts from assemblies or MAGs; profiles inferred from 16S (PICRUSt, FAPROTAX); and, in two cases, measured enzyme activity or protein.
  conf: not stated · class: not stated · holds: the soil literature reviewed · src: none (the reviewer's definitions) · trail: H1-05 §Functional versus taxonomic turnover · from: H1-05:B-0029, H1-05:B-0030

### covariation: covariation of functional and taxonomic dissimilarity
needs: functional-profile

- **covariation.1** Across 16 soils from cold desert, hot desert, forest, grassland and tundra, Bray-Curtis dissimilarity of MG-RAST/SEED gene profiles correlated with 16S Bray-Curtis (Mantel r = 0.76) and with unweighted UniFrac (r = 0.82); only 13 to 23% of reads were annotatable, and desert and non-desert samples separated almost completely (ANOSIM R about 0.97 to 0.98).
  conf: not stated · class: meas (marker) · holds: 16 soils at a strong cross-biome contrast; figures confirmed against full text by the critic · src: fiererCrossbiomeMetagenomicAnalyses2012 (FT; measured; critic: C-053 was "FT, via search agents; measured") · trail: H1-05 §Covariation at strong contrasts, §answers, §critic, §Adversarial critique · from: H1-05:I-0001, H1-05:B-0035, H1-05:A-006, H1-05:C-001, H1-05:C-033, H1-05:C-052, H1-05:C-053
- **covariation.2** On the reviewer's reading, not the authors', a single dominant desert/non-desert split drives both matrices in the 16-soil study, so the correlation may say more about that split than about fine-scale coupling; the critic adds that the authors made a parallel caveat for alpha diversity (the correlations were not significant without the cold-desert soils).
  conf: not stated · class: reading (note: "My reading, not the authors'") · holds: 16 soils, dominated by a desert/non-desert split · src: fiererCrossbiomeMetagenomicAnalyses2012 · trail: H1-05 §Covariation at strong contrasts, §answers, §Adversarial critique · from: H1-05:B-0036, H1-05:A-016, H1-05:C-054
- **covariation.3** The authors of Fierer 2012 conclude that functional redundancy 'is not so pervasive as to obscure' the taxonomy-function relationship.
  conf: not stated · class: not stated · holds: Fierer 2012 · src: fiererCrossbiomeMetagenomicAnalyses2012 · trail: H1-05 §Adversarial critique · from: H1-05:C-097
- **covariation.4** Across six NutNet grassland sites, functional-gene and bacterial dissimilarity correlated with rho = 0.87, mostly between sites; within-site N and P additions shifted both.
  conf: not stated · class: meas (marker) · holds: six NutNet grassland sites; figures confirmed against full text by the critic · src: leffConsistentResponsesSoil2015 (FT; measured; critic: C-053 was "FT, measured") · trail: H1-05 §Covariation at strong contrasts, §answers, §critic · from: H1-05:B-0037, H1-05:I-0002, H1-05:A-006, H1-05:C-001, H1-05:C-033, H1-05:C-053
- **covariation.5** In 845 pooled public soil metagenomes (356,090 pairs), pairwise functional and taxonomic Bray-Curtis similarities correlated (r2 = 0.2831).
  conf: not stated · class: meas (marker) · holds: 845 pooled MG-RAST soil metagenomes; rechecked against full text by the reviewer and the critic · src: chenFunctionalRedundancySoil2022 (FT, rechecked by this reviewer; measured) · trail: H1-05 §Covariation at strong contrasts, §answers, §critic · from: H1-05:I-0003, H1-05:A-006, H1-05:C-001, H1-05:C-033
- **covariation.6** At one site under coal-fire heating, metagenome and amplicon ordinations were concordant (Procrustes 0.802, m2 = 0.357), alongside stable functional similarity, so 'stable function' and 'covariation' coexist in one dataset.
  conf: not stated · class: not stated · holds: one site; a preprint read via a fetch summary · src: barnettDisturbanceIncreasesSoil2025 (secondary or abstract-level; preprint; critic: C-048 was "FT via fetch summary; preprint") · trail: H1-05 §Covariation at strong contrasts, §answers · from: H1-05:B-0038, H1-05:A-024, H1-05:C-047, H1-05:C-048
- **covariation.7** Across soils, functional and taxonomic dissimilarity are usually positively correlated; the clearest cases come from strong cross-biome or between-site contrasts (Mantel r 0.76 to 0.82 across 16 soils; Spearman rho 0.87 across 6 NutNet sites; r2 0.28 across 845 pooled metagenomes), and strong contrasts give covariation.
  conf: not stated · class: meas (marker) · holds: three soil datasets at strong contrasts, all using Bray-Curtis on annotated profiles and correlation-type tests; none used a null model; the critic: not independent in lineage, as two come from one group and the third pools MG-RAST submissions that may include the first · src: fiererCrossbiomeMetagenomicAnalyses2012, leffConsistentResponsesSoil2015, chenFunctionalRedundancySoil2022 · rating: "Moderate for covariation at strong contrasts" (critic: C-002: these datasets are not independent in lineage) · trail: H1-05 §answers, §Covariation at strong contrasts, §Contrast size, §critic · from: H1-05:A-001, H1-05:A-002, H1-05:A-005, H1-05:A-006, H1-05:A-010, H1-05:A-016, H1-05:B-0034, H1-05:B-0039, H1-05:B-0040, H1-05:B-0070, H1-05:C-001, H1-05:C-002, H1-05:C-038, H1-05:I-0001

### turnover-ordering: which turnover is larger, functional or taxonomic
needs: covariation

- **turnover-ordering.1** Covariation and "function less variable" are compatible: covariation says nothing about which turnover is larger, because a correlation between dissimilarity matrices says nothing about their relative magnitudes; two soil datasets report both.
  conf: not stated · class: not stated · holds: the 845 pooled soil metagenomes and the coal-fire site · src: chenFunctionalRedundancySoil2022, barnettDisturbanceIncreasesSoil2025 · trail: H1-05 §How the cases relate, §critic · from: H1-05:B-0146, H1-05:B-0147, H1-05:C-003, H1-05:C-037, H1-05:I-0003, H1-05:B-0038
- **turnover-ordering.2** In the global pooled dataset, functional Bray-Curtis similarity ranged 44 to 99% and taxonomic 9 to 100% (paired t = 67.5); climate plus soil explained 16.3% of taxonomic and 13.5% of functional variation (DistLM). The authors call this strong evidence for functional redundancy. It is the one large soil magnitude comparison, and it finds functional similarity higher than taxonomic at a strong (global) contrast; removing it would leave the 'function lower' ordering resting on small single-site studies and significance contrasts.
  conf: single (note: "SINGLE SOURCE for this sample size") · class: not stated · holds: 845 pooled public soil metagenomes; the profiles pool assembled and unassembled MG-RAST submissions from many studies; SEED level 3 (1,135 functions) compared with RefSeq genus (1,113 taxa); nothing tests whether a lower functional dissimilarity is expected from aggregation alone; figures checked against full text by the reviewer and the critic · src: chenFunctionalRedundancySoil2022 (FT, rechecked) · trail: H1-05 §Functional turnover reported lower, §answers, §critic · from: H1-05:B-0041, H1-05:B-0042, H1-05:B-0043, H1-05:B-0044, H1-05:B-0045, H1-05:B-0046, H1-05:A-007, H1-05:A-008, H1-05:A-019, H1-05:A-032, H1-05:A-033, H1-05:C-004, H1-05:C-033
- **turnover-ordering.3** Between serpentine and non-serpentine site pairs, bacterial composition differed (PERMANOVA R2 = 0.061, P = 0.004) while eggNOG functional composition did not (R2 = 0.027, P = 0.391); the authors conclude redundancy, and note that specialized functions such as siderophore biosynthesis did differ.
  conf: not stated · class: meas (marker) · holds: serpentine and non-serpentine soil pairs; residual df 19 against 16; figures rechecked by the reviewer and the critic · src: igweRedundancyMaintainsMicrobial2026 (FT, rechecked; measured) · trail: H1-05 §Functional turnover reported lower, §answers, §critic · from: H1-05:I-0004, H1-05:B-0048, H1-05:A-008, H1-05:C-033
- **turnover-ordering.4** On the reviewer's reading, the serpentine result is a significant test set against a non-significant one, on datasets of different size after QC (the functional dataset is smaller): site pairs explained about 56% of variation in both functional (non-significant, F(19,16)) and bacterial (significant) composition, which suggests limited power on the functional side rather than an absence of structure.
  conf: not stated · class: reading (note: "My reading") · holds: serpentine and non-serpentine soil pairs · src: igweRedundancyMaintainsMicrobial2026 · trail: H1-05 §Functional turnover reported lower, §answers · from: H1-05:B-0049, H1-05:B-0050, H1-05:A-020
- **turnover-ordering.5** Along a latitudinal forest gradient in China, bacterial Bray-Curtis showed strong distance decay, while GeoChip function (summarized as DCA axes, not pairwise dissimilarity) was "highly convergent"; the two turnovers are not on a common basis.
  conf: not stated · class: not stated · holds: natural broadleaf forest along a latitudinal gradient in China; GeoChip against 16S · src: zhangSoilBacterialEndemism2016 (FT via agents) · trail: H1-05 §Functional turnover reported lower · from: H1-05:B-0051, H1-05:B-0052, H1-05:R-0045
- **turnover-ordering.6** Under coal-fire disturbance, OTU similarity to reference rose as soils cooled, while KO similarity stayed high throughout (stable KO similarity during fire-disturbance recovery); MAG-based redundancy rose with disturbance, which the authors attribute to lower diversity and smaller genomes.
  conf: not stated · class: not stated · holds: one coal-fire site; a preprint with no published version found, read via a fetch summary · src: barnettDisturbanceIncreasesSoil2025 (secondary or abstract-level; preprint, no published version found; critic: C-048 was "FT via fetch summary; preprint, no published version found") · trail: H1-05 §Functional turnover reported lower, §answers · from: H1-05:B-0053, H1-05:B-0054, H1-05:A-008, H1-05:C-048
- **turnover-ordering.7** No fertilizer effect on functional profiles after 54 years, despite taxonomic shifts.
  conf: not stated · class: not stated · holds: long-term N, P, K and NPK fertilization of grassland soil, 54 years; abstract only · src: panImpactLongtermN2014 (AB) · trail: H1-05 §Functional turnover reported lower · from: H1-05:B-0055, H1-05:R-0057
- **turnover-ordering.8** Stable functional potential across a 1 to 30 C peat incubation while taxonomy changed.
  conf: not stated · class: not stated · holds: peat incubation; abstract only · src: yangDecouplingMicrobialCommunity2021 (AB) · trail: H1-05 §Functional turnover reported lower · from: H1-05:B-0055
- **turnover-ordering.9** Taxonomic differences "far greater" than SEED functional differences under tillage and rotation, with the two measured in different papers.
  conf: not stated · class: not stated · holds: a soil under different tillage and crop-management (rotation) regimes; abstract only; a cross-paper comparison · src: souzaMetagenomicAnalysisReveals2015 (AB) · trail: H1-05 §Functional turnover reported lower · from: H1-05:B-0055, H1-05:R-0067
- **turnover-ordering.10** Similar functional capacities in arid and hyperarid saline drylands despite structural differences.
  conf: not stated · class: not stated · holds: arid and hyperarid saline drylands; only the abstract and methods closely read, so abstract-level for its result claim · src: saumasanchezFunctionalRedundancyBuffers2024 (AB for its result claim; critic: C-051 was "FT via agents, abstract and methods only closely read") · trail: H1-05 §Functional turnover reported lower, §Adversarial critique · from: H1-05:B-0055, H1-05:C-051
- **turnover-ordering.11** Under high Hg, little change in C and N genes but a significant shift in predicted-gene beta diversity.
  conf: not stated · class: not stated · holds: long-term mercury contamination of soils (high Hg); abstract only · src: freyLongtermMercuryContamination2022 (AB) · trail: H1-05 §Functional turnover reported lower · from: H1-05:B-0055, H1-05:R-0063
- **turnover-ordering.12** After aromatic pollution in a microcosm, taxonomic diversity fell and gene-pool diversity rose (alpha diversity, not turnover).
  conf: not stated · class: not stated · holds: a microcosm; alpha, not turnover; abstract only · src: katoTimeseriesMetagenomicAnalysis2015 (AB) · trail: H1-05 §Functional turnover reported lower · from: H1-05:B-0055
- **turnover-ordering.13** Fungal endemism with convergent enzyme activity across North America: a non-DNA case, indirect for DNA profiles.
  conf: not stated · class: not stated · holds: soil fungi across North America; measured enzyme activity, not DNA; abstract only · src: talbotEndemismFunctionalConvergence2014 (AB) · trail: H1-05 §Functional turnover reported lower · from: H1-05:B-0056, H1-05:B-0057
- **turnover-ordering.14** With marker-inferred function, ZnO dose separated taxa but not PICRUSt-type predicted functions.
  conf: not stated · class: deriv (marker) · holds: soil polluted with nano ZnO, by dose; function inferred from the same 16S data, so not independent of taxonomy; abstract only · src: dineshSoilPollutedNano2023 (AB; derived) · trail: H1-05 §Functional turnover reported lower, §answers · from: H1-05:I-0005, H1-05:A-045, H1-05:B-0058, H1-05:R-0084
- **turnover-ordering.15** Along an alpine gradient, PICRUSt2 function was redundant and tracked phylogenetic more than taxonomic dissimilarity.
  conf: not stated · class: deriv (marker) · holds: an alpine altitudinal gradient; function inferred from the same 16S data, so not independent of taxonomy · src: liAsynchronousPatternsSoil2024 (FT via agents; derived) · trail: H1-05 §Functional turnover reported lower, §answers · from: H1-05:I-0006, H1-05:A-045, H1-05:B-0058, H1-05:R-0086
- **turnover-ordering.16** After 14 years of moderate warming (0.8 to 2.0 C), 16S composition did not differ while GeoChip functional-gene composition did (Adonis, ANOSIM, MRPP, P < 0.05), with n = 4 per treatment; the authors conclude that functional potential is more sensitive than taxonomy. Plant and abiotic variables were unchanged, so the contrast was weak.
  conf: not stated · class: meas (marker) · holds: one long-term warming site in a Mediterranean-type grassland, n = 4 per treatment, GeoChip against 16S; n and the three tests checked by the critic · src: gaoLongtermWarmingMediterraneantype2021 (FT, rechecked; measured) · trail: H1-05 §Functional turnover reported higher, §answers, §critic · from: H1-05:I-0007, H1-05:B-0059, H1-05:B-0060, H1-05:A-009, H1-05:A-021, H1-05:C-033, H1-05:R-0042
- **turnover-ordering.17** Under aeolian erosion and deposition, soil nutrients correlated with functional but not taxonomic structure (Mantel).
  conf: not stated · class: not stated · holds: field simulation of aeolian soil erosion and deposition; GeoChip; abstract only · src: maDivergentTaxonomicFunctional2017 (AB) · trail: H1-05 §Functional turnover reported higher, §answers · from: H1-05:B-0061, H1-05:A-009, H1-05:R-0061
- **turnover-ordering.18** Along the Changbai elevation gradient, functional-gene distance decay (r = 0.708) was stronger than bacterial (r = 0.409) on the reviewer's reading; the authors describe the patterns as similar, with different drivers (pH for taxa, DOC for genes), and the two r values come from different platforms (16S against GeoChip) and are not on a common scale.
  conf: not stated · class: reading (note: "This is my reading") · holds: Changbai elevation gradient · src: shenDramaticIncreasesSoil2016 (FT via agents) · trail: H1-05 §Functional turnover reported higher, §answers · from: H1-05:B-0062, H1-05:B-0063, H1-05:B-0064, H1-05:B-0065, H1-05:A-009
- **turnover-ordering.19** Lower functional than taxonomic turnover is the most common reported ordering in soil but rests on weak comparisons: none of the 'function lower' soil studies compares the two turnovers on a common test with a null, and the single-site 'function lower' results mostly set a significant test against a non-significant one.
  conf: not stated · class: not stated · holds: soil, DNA-measured functional profiles · src: chenFunctionalRedundancySoil2022, igweRedundancyMaintainsMicrobial2026, panImpactLongtermN2014, yangDecouplingMicrobialCommunity2021, souzaMetagenomicAnalysisReveals2015, saumasanchezFunctionalRedundancyBuffers2024 · rating: "Weak for the ordering" · trail: H1-05 §answers, §critic · from: H1-05:A-003, H1-05:A-017, H1-05:A-018, H1-05:C-006
- **turnover-ordering.20** The reverse ordering (function responds where taxonomy does not) is reported under weak contrasts and rests on two GeoChip studies from one group (one abstract only) plus a reviewer's reading of a third; removing the warming study would leave only the abstract-only study and that reading.
  conf: not stated · class: not stated · holds: 14 years of moderate warming (n = 4 per treatment), erosion and deposition, and possibly an elevation gradient; platforms differ; the critic: the power-asymmetry critique made against the serpentine study is not applied to the warming study (n = 4, significant functional against non-significant taxonomic) · src: gaoLongtermWarmingMediterraneantype2021, maDivergentTaxonomicFunctional2017, shenDramaticIncreasesSoil2016 · rating: "Weak for the reverse ordering" · contrary: one-sided (critic: C-093) · trail: H1-05 §answers, §critic, §Adversarial critique · from: H1-05:A-004, H1-05:A-009, H1-05:A-021, H1-05:A-034, H1-05:C-007, H1-05:C-093, H1-05:C-094, H1-05:C-095, H1-05:I-0004
- **turnover-ordering.21** In soil, function more responsive (the 14-year warming and erosion studies) is in conflict with function less responsive (the serpentine, fertilizer, peat, tillage and dryland studies), all at single sites or weak or moderate contrasts.
  conf: cont (note: "Conflicts: Soil: [5] and [15] (function more responsive) against") · class: not stated · holds: single sites or weak or moderate contrasts · src: gaoLongtermWarmingMediterraneantype2021, maDivergentTaxonomicFunctional2017, igweRedundancyMaintainsMicrobial2026, panImpactLongtermN2014, yangDecouplingMicrobialCommunity2021, souzaMetagenomicAnalysisReveals2015, saumasanchezFunctionalRedundancyBuffers2024 · trail: H1-05 §answers · from: H1-05:A-022, H1-05:I-0007, H1-05:B-0061, H1-05:I-0004, H1-05:B-0055

### contrast-size: dependence of the comparison on the size of the environmental contrast
needs: covariation, turnover-ordering

- **contrast-size.1** No soil study was found that tests (or plots) how the functional-taxonomic gap scales with environmental distance; systematic comparisons across a graded range of environmental distances were not measured.
  conf: not stated · class: search (note: "No soil study was found that tests how the functional-taxonomic gap scales with environmental distance") · holds: soil · src: none (a search result) · search: searched, not found (note: "No soil study was found that tests how the functional-taxonomic gap scales with environmental distance") · trail: H1-05 §answers, §Contrast size · from: H1-05:A-013, H1-05:A-026, H1-05:B-0066
- **contrast-size.2** In a single-site precipitation experiment, ±30% precipitation slightly decreased and ±60% strongly increased within-treatment dispersion (PERMDISP) of taxa, genes, proteins and enzyme activities alike; gene, protein and enzyme dissimilarities were Mantel-correlated with taxonomic dissimilarity, and neither taxonomy nor function showed a directional PERMANOVA shift. The authors conclude that "taxonomic stochasticity translated into functional stochasticity", not redundancy.
  conf: not stated · class: meas (marker) · holds: one Eurasian steppe site under two magnitudes of precipitation change; within-treatment dispersion, not a comparison of the two turnovers' magnitudes, so indirect for the ordering question; the ±30% decrease in function confirmed by the critic · src: xuDistinctivePatternMechanism2022 (FT, rechecked; measured) · trail: H1-05 §Contrast size, §answers, §critic, §Adversarial critique · from: H1-05:I-0008, H1-05:B-0067, H1-05:B-0068, H1-05:B-0069, H1-05:A-012, H1-05:A-023, H1-05:A-025, H1-05:C-009, H1-05:C-010, H1-05:C-033, H1-05:C-040, H1-05:R-0075
- **contrast-size.3** At weak single-site contrasts the ordering has gone both ways (function lower in the serpentine, 54-year fertilizer and tillage studies; function higher in the 14-year warming and erosion studies); cross-study comparison of contrast size is confounded by platform (GeoChip against shotgun), group, sample size and test, so no dependence on contrast size can be read off.
  conf: not stated · class: not stated · holds: soil; strong contrasts give covariation, weak single-site contrasts give both orderings · src: igweRedundancyMaintainsMicrobial2026, panImpactLongtermN2014, souzaMetagenomicAnalysisReveals2015, gaoLongtermWarmingMediterraneantype2021, maDivergentTaxonomicFunctional2017 · trail: H1-05 §answers, §Contrast size, §critic · from: H1-05:A-005, H1-05:A-011, H1-05:B-0071, H1-05:B-0072, H1-05:C-008, H1-05:I-0004, H1-05:B-0055, H1-05:I-0007, H1-05:B-0061
- **contrast-size.4** On the reviewer's synthesis, the reverse ordering appears only in GeoChip or single-site weak-contrast studies, so platform, contrast size and sample size are entangled; the magnitude comparison is the claim that most needs a null, and in soil it has none.
  conf: not stated · class: reading (critic: C-103) · holds: soil; mostly labelled as the reviewer's reading · src: none (the reviewer's synthesis) · trail: H1-05 §How the cases relate, §Adversarial critique · from: H1-05:B-0148, H1-05:B-0149, H1-05:C-103, H1-05:C-104, H1-05:C-105
- **contrast-size.5** Along a latitudinal gradient, taxonomic dissimilarity explains almost none of functional variation, while in the precipitation experiment function tracks taxonomy under both contrast sizes: the review lists these as in conflict.
  conf: cont (note: "Conflicts:") · class: not stated · holds: a latitudinal forest gradient against one precipitation experiment · src: zhangSoilBacterialEndemism2016, xuDistinctivePatternMechanism2022 · trail: H1-05 §answers · from: H1-05:A-023, H1-05:A-022, H1-05:I-0008, H1-05:B-0051

### chronosequence-precedents: chronosequences and drivers, the nearest precedents
needs: functional-profile

- **chronosequence-precedents.1** Over 143 years of grassland restoration, bacterial richness falls while SEED functional richness expands (alpha diversity; no paired turnover comparison).
  conf: not stated · class: not stated · holds: grassland restoration chronosequence; alpha, not turnover; the preprint's "profound functional decoupling" was softened to "a decoupling" in the published version · src: goodallTaxonomicFilteringAccompanies2026 (FT via agents) · trail: H1-05 §Nearest precedents, §answers, §Preprints and published versions · from: H1-05:B-0073, H1-05:B-0074, H1-05:A-027, H1-05:B-0142
- **chronosequence-precedents.2** Along Swedish succession, taxonomic diversity falls while C, N and P gene diversity rises, with PICRUSt2 used for the redundancy analyses (alpha diversity; no paired turnover comparison).
  conf: not stated · class: not stated · holds: Swedish successional chronosequence; alpha, not turnover; the preprint's "causal link" was softened to "the link" in the published version · src: sveenFunctionalDiversitySoil2025 (FT via agents) · trail: H1-05 §Nearest precedents, §answers, §Preprints and published versions · from: H1-05:B-0073, H1-05:B-0074, H1-05:A-027, H1-05:B-0143
- **chronosequence-precedents.3** Global N-cycling pathway frequencies track habitat and soil C and N much better than the genera that encode them; this contrasts drivers, not turnovers, so it is indirect.
  conf: not stated · class: not stated · holds: global soils; N-cycling traits · src: nelsonGlobalBiogeographyMicrobial2016 (FT via agents) · trail: H1-05 §Nearest precedents · from: H1-05:B-0075, H1-05:B-0076

### other-habitats: functional against taxonomic turnover outside soil
needs: covariation, turnover-ordering

- **other-habitats.1** On algal surfaces, taxonomic similarity was 15% against 70% COG similarity.
  conf: not stated · class: not stated · holds: algal surfaces; read via a fetch summary · src: burkeBacterialCommunityAssembly2011 (secondary or abstract-level; critic: C-048 was "FT via fetch summary") · trail: H1-05 §Other habitats, §answers · from: H1-05:B-0080, H1-05:A-014
- **other-habitats.2** In the Ulva microbiome across a 2000 km, 5 to 35 PSU salinity gradient, salinity explained R2 = 0.70 of taxonomic and 0.17 of KO-based functional variation (envfit), although 23 KEGG modules still shifted: function stays lower under a strong contrast.
  conf: single (critic: C-062) · class: not stated · holds: Ulva microbiome; one study, MAG-based taxonomy; envfit figures checked by the critic; the only strong-contrast case outside soil; soil has not tested function lower at a strong contrast with a common metric · src: vanderloosLowFunctionalChange2025 (FT, rechecked) · trail: H1-05 §Other habitats, §answers, §critic, §Adversarial critique, §How the cases relate · from: H1-05:B-0081, H1-05:A-014, H1-05:C-033, H1-05:C-062, H1-05:B-0150
- **other-habitats.3** In a coastal Mediterranean time series, all-gene similarity tracked 16S similarity closely (R2 = 0.77); the authors reject strict redundancy.
  conf: not stated · class: not stated · holds: one marine time series; its full-text XML returned empty to the reviewer, so it rests on the agents' reading · src: galandStrongLinkMarine2018 (FT via agents) · trail: H1-05 §Other habitats, §answers, §Provenance · from: H1-05:B-0083, H1-05:B-0084, H1-05:A-014, H1-05:B-0019
- **other-habitats.4** In subsurface sediments, taxa CVs were about 10 times those of gene groups of similar mean abundance: taxa were about an order of magnitude more variable than gene groups at every KEGG level and EC, after abundance matching.
  conf: not stated · class: not stated · holds: Oregon coastal subsurface sediments · src: soufiTaxonomicVariabilityFunctional2024 (FT via agents) · trail: H1-05 §Other habitats, §answers · from: H1-05:B-0085, H1-05:A-049, H1-05:R-0106
- **other-habitats.5** In bromeliads, functional-group structure was stable while within-group taxonomy varied.
  conf: not stated · class: not stated · holds: bromeliad communities; abstract only · src: loucaHighTaxonomicVariability2016 (AB) · trail: H1-05 §Other habitats · from: H1-05:B-0086
- **other-habitats.6** In the global ocean, with FAPROTAX (derived) functional groups, environment strongly shapes functional groups but weakly shapes within-group taxonomy.
  conf: not stated · class: deriv (note: "Global ocean, FAPROTAX (derived)") · holds: global ocean; FAPROTAX-derived function; abstract only · src: loucaDecouplingFunctionTaxonomy2016 (AB) · trail: H1-05 §Other habitats · from: H1-05:B-0087
- **other-habitats.7** During vermicomposting, PICRUSt2 turnover was about 12 times slower than taxonomic turnover.
  conf: not stated · class: deriv (marker) · holds: vermicomposting; PICRUSt2-inferred function · src: airaFasterTurnoverTaxonomic2026 (FT via agents; derived) · trail: H1-05 §Other habitats · from: H1-05:I-0009
- **other-habitats.8** Across 148 trait datasets, mean Mantel r along space was 0.254 taxonomic against 0.115 functional, with about 31 of 148 datasets reversed.
  conf: not stated · class: not stated · holds: 148 datasets including diatoms and fungi but no bacteria, so not 'non-microbial'; Mantel values checked by the critic · src: gracorozaDistanceDecay22022 (FT via agents) · trail: H1-05 §Other habitats, §critic, §Adversarial critique · from: H1-05:B-0088, H1-05:C-011, H1-05:C-033, H1-05:C-055, H1-05:C-101
- **other-habitats.9** In European fish, functional beta diversity is below taxonomic, driven by turnover.
  conf: not stated · class: not stated · holds: European fish assemblages; abstract only · src: villegerDecomposingFunctionalDiversity2013 (AB) · trail: H1-05 §Other habitats · from: H1-05:B-0089
- **other-habitats.10** Yet in European fish, functional homogenization over time exceeded taxonomic homogenization six-fold.
  conf: not stated · class: not stated · holds: European fish assemblages; abstract only · src: villegerFunctionalHomogenizationExceeds2014 (AB) · trail: H1-05 §Other habitats · from: H1-05:B-0090
- **other-habitats.11** Outside soil, marine and host-associated studies report lower functional turnover, including under a strong 2000 km salinity contrast and on algal surfaces, while a marine time series finds tight coupling; this mixes FAPROTAX-derived, abstract-only and single-time-series evidence, and the only strong-contrast case is the Ulva study across 2000 km of salinity.
  conf: not stated · class: not stated · holds: marine and host-associated systems, kept separate from soil · src: vanderloosLowFunctionalChange2025, burkeBacterialCommunityAssembly2011, galandStrongLinkMarine2018, loucaDecouplingFunctionTaxonomy2016, loucaHighTaxonomicVariability2016 · trail: H1-05 §answers, §Adversarial critique · from: H1-05:A-014, H1-05:C-062, H1-05:B-0081
- **other-habitats.12** Non-bacterial communities (148 datasets including diatoms and fungi; European fish) show lower functional decay on average, but with many reversals.
  conf: not stated · class: not stated · holds: non-bacterial communities · src: gracorozaDistanceDecay22022, villegerDecomposingFunctionalDiversity2013, villegerFunctionalHomogenizationExceeds2014 · trail: H1-05 §answers, §critic · from: H1-05:A-015, H1-05:C-011, H1-05:B-0088, H1-05:B-0089

### unit-annotation-metric: dependence of the comparison on functional unit, annotation, platform and metric
needs: turnover-ordering, functional-profile

- **unit-annotation-metric.1** In the 845 pooled soil metagenomes, functional similarity exceeded taxonomic similarity at SEED levels 1 and 2 against all five taxonomic ranks, so the ordering did not reverse at any combination tested; the authors say coarser levels are more conserved, and state only that the ordering held at all levels. It is the only soil evidence on annotation level.
  conf: single (critic: C-012) · class: not stated · holds: 845 metagenomes (Chen 2022); SEED levels; rechecked by the reviewer · src: chenFunctionalRedundancySoil2022 (FT, rechecked) · trail: H1-05 §Dependence on unit, §answers, §critic · from: H1-05:B-0092, H1-05:B-0093, H1-05:A-037, H1-05:A-038, H1-05:A-063, H1-05:C-013, H1-05:C-014, H1-05:C-045, H1-05:C-033, H1-05:I-0003
- **unit-annotation-metric.2** Finer functional units (KO, gene clusters) were not tested in that study, which explicitly chose SEED over KO, COG and NOG, so whether the ordering can reverse at fine resolution is open.
  conf: not stated · class: not stated · holds: the global pooled soil metagenomes · src: chenFunctionalRedundancySoil2022 · trail: H1-05 §Dependence on unit, §answers, §critic · from: H1-05:A-039, H1-05:B-0094, H1-05:C-016
- **unit-annotation-metric.3** In one soil experiment, dissimilarity from all reads including unannotated ones (Mash) and from assembled genes gave within-treatment patterns similar to annotated-read dissimilarity, so in that case the annotation did not change the result.
  conf: single (critic: C-012) · class: not stated · holds: one Eurasian steppe precipitation experiment; within-treatment dispersion; rechecked by the reviewer · src: xuDistinctivePatternMechanism2022 (FT, rechecked) · trail: H1-05 §Dependence on unit, §answers, §critic, §Provenance · from: H1-05:B-0095, H1-05:A-040, H1-05:C-017, H1-05:B-0018, H1-05:R-0075
- **unit-annotation-metric.4** In a marine time series, the functional-taxonomic correlation fell from R2 0.77 (all genes) to 0.58 (KEGG) to 0.16 (FAPROTAX/PICRUSt, taxonomy-inferred functions): coupling strength depends on the annotation scheme. Removing this study removes the main direct evidence for that.
  conf: single (note: "single study") · class: not stated · holds: marine, one time series · src: galandStrongLinkMarine2018 (full text, single study, marine) · rating: "Moderate for the general point, outside soil, that annotation scheme changes the strength of coupling" · trail: H1-05 §answers, §Dependence on unit, §critic · from: H1-05:A-048, H1-05:A-054, H1-05:A-064, H1-05:B-0096, H1-05:C-021
- **unit-annotation-metric.5** The marine time series finds that restricting to annotated genes weakens the coupling (all-read coupling is strongest), while the soil precipitation experiment finds all-read and annotated dissimilarity behave alike; the two use different measures (regression of similarities against within-treatment dispersion) and habitats, so they do not directly contradict.
  conf: not stated · class: not stated · holds: marine water against one soil experiment · src: galandStrongLinkMarine2018, xuDistinctivePatternMechanism2022 · trail: H1-05 §answers, §Dependence on unit · from: H1-05:A-055, H1-05:A-056, H1-05:B-0097, H1-05:I-0008
- **unit-annotation-metric.6** Unknown-function genes are prevalent in fine-textured, higher-pH soils and are often mobile-element associated, so the unannotated fraction can vary along soil gradients (with soil properties): indirect support for an annotation-bias critique, not a demonstration of its effect on turnover.
  conf: not stated · class: not stated · holds: soils; a preprint, abstract only · src: hollandmoritzEcologicalPerspectiveMicrobial2021 (AB; preprint) · trail: H1-05 §Dependence on unit, §answers · from: H1-05:B-0098, H1-05:B-0099, H1-05:A-047
- **unit-annotation-metric.7** On the same 27 paired steppe and cropland soils, the dispersion-based analysis found KEGG gene assemblages homogenized in cropland at local and regional scales while bacterial taxa were homogenized only locally, whereas an earlier distance-decay-slope analysis of the same data had found greater KEGG functional turnover in cropland: the choice of turnover statistic changed the functional conclusion.
  conf: single (critic: C-063) · class: not stated · holds: 27 paired steppe and cropland soils; the only soil case where metric choice reversed a conclusion; rechecked by the reviewer · src: guLandConversionCropland2025 (FT, rechecked) · trail: H1-05 §Nearest precedents, §Dependence on unit, §answers, §critic · from: H1-05:B-0077, H1-05:B-0078, H1-05:B-0100, H1-05:A-041, H1-05:A-042, H1-05:A-065, H1-05:C-018, H1-05:C-063
- **unit-annotation-metric.8** No soil study compared Bray-Curtis with Aitchison or Jaccard (dissimilarity measures or transforms) for the functional-taxonomic ordering.
  conf: not stated · class: search (note: "No soil study compared Bray-Curtis with Aitchison or Jaccard") · holds: soil; searches by both agents (soil agent queries); the critic: compositional comparisons reported as not found without naming the routes · src: none (a search result) · search: searched, not found (note: "No soil study compared Bray-Curtis with Aitchison or Jaccard for the functional-taxonomic ordering (searches by both agents)") · trail: H1-05 §Dependence on unit, §critic, §Provenance · from: H1-05:B-0101, H1-05:C-020, H1-05:B-0020, H1-05:C-084
- **unit-annotation-metric.9** For ectomycorrhizal fungi, turnover appeared at the level of gene sequence variants but not gene-family abundance.
  conf: not stated · class: not stated · holds: ectomycorrhizal fungal communities across a precipitation gradient; targeted gene families; abstract only · src: pellitierPotentialFunctionalDivergence2024 (AB) · trail: H1-05 §Dependence on unit, §answers · from: H1-05:B-0103, H1-05:A-043, H1-05:A-028, H1-05:R-0071
- **unit-annotation-metric.10** Within one grazing and P-addition grassland site, species-level resolution within functional groups gave strong taxon-function consistency (Procrustes) and removed an apparent decoupling; the authors attribute stable function to reciprocal changes in two dominant species rather than redundancy.
  conf: not stated · class: not stated · holds: one grassland site under grazing and P addition · src: liuReciprocalChangesDominant2023 (FT via agents) · trail: H1-05 §Nearest precedents, §Dependence on unit, §answers · from: H1-05:B-0079, H1-05:B-0102, H1-05:A-044, H1-05:A-071
- **unit-annotation-metric.11** In anaerobic digesters, taxonomic convergence depended on taxonomic rank: inoculum identity was recoverable at genus but less at phylum level.
  conf: not stated · class: not stated · holds: anaerobic digestion communities, outside soil; abstract only · src: jourdainEnvironmentalSelectionConstrains2026 (AB) · trail: H1-05 §answers, §Dependence on unit · from: H1-05:A-051, H1-05:B-0104
- **unit-annotation-metric.12** In lake enrichments, redundancy was higher with EC grouping than with KO.
  conf: not stated · class: not stated · holds: lake enrichments, outside soil · src: lemoigneLinkingStochasticAssembly2026 (FT via agents) · trail: H1-05 §answers, §Dependence on unit · from: H1-05:A-050, H1-05:B-0104
- **unit-annotation-metric.13** The 845 pooled soil metagenomes and the subsurface sediments both find functional variability lower at every annotation level tested, so no reversal of ordering by unit was found in either.
  conf: not stated · class: not stated · holds: soil SEED levels; sediment KEGG levels and EC · src: chenFunctionalRedundancySoil2022, soufiTaxonomicVariabilityFunctional2024 · trail: H1-05 §answers, §Dependence on unit · from: H1-05:A-057, H1-05:B-0105, H1-05:I-0003, H1-05:B-0085
- **unit-annotation-metric.14** The taxonomic side is also measured differently across studies (16S amplicon in the 16-soil, NutNet and 14-year warming studies; read-based RefSeq in the 845 pooled metagenomes; MAG in the Ulva study), and this is not kept apart.
  conf: not stated · class: not stated · holds: the soil and Ulva studies named · src: fiererCrossbiomeMetagenomicAnalyses2012, leffConsistentResponsesSoil2015, gaoLongtermWarmingMediterraneantype2021, chenFunctionalRedundancySoil2022, vanderloosLowFunctionalChange2025 · trail: H1-05 §critic · from: H1-05:C-019, H1-05:I-0001, H1-05:B-0037, H1-05:I-0007, H1-05:I-0003, H1-05:B-0081
- **unit-annotation-metric.15** Platform differs across studies: GeoChip probes a few thousand preselected known genes, whose detection depends on hybridisation thresholds, while shotgun annotation typically covers a minority of reads (13 to 23% in the 16-soil study).
  conf: not stated · class: not stated · holds: GeoChip against shotgun platforms · src: fiererCrossbiomeMetagenomicAnalyses2012 · trail: H1-05 §answers, §Adversarial critique · from: H1-05:A-046, H1-05:C-094, H1-05:I-0001
- **unit-annotation-metric.16** On the reviewer's observation, GeoChip underlies the three soil studies where function was as or more responsive and shotgun annotation underlies most "function lower" results; no study ran both on the same soils for this comparison, so platform and result are confounded across the literature. This is not a tested result; it is drawn from three papers, two of them from one group (Zhou/Yang), and the answer on soil ordering leans on it.
  conf: not stated · class: reading (note: "This is the reviewer's observation, not a tested result") · holds: soil · src: gaoLongtermWarmingMediterraneantype2021, shenDramaticIncreasesSoil2016, maDivergentTaxonomicFunctional2017 · trail: H1-05 §Dependence on unit, §Adversarial critique · from: H1-05:B-0106, H1-05:B-0107, H1-05:B-0108, H1-05:B-0109, H1-05:C-061
- **unit-annotation-metric.17** Average genome size biases gene-abundance comparisons; it shifts with N and P addition and with heating in soil.
  conf: not stated · class: not stated · holds: the bias shown in human gut only; abstract only; in soil, shifts with N and P addition (NutNet) and with heating (coal fire) · src: nayfachAverageGenomeSize2015 (AB; human gut), leffConsistentResponsesSoil2015, barnettDisturbanceIncreasesSoil2025 · trail: H1-05 §Dependence on unit, §answers · from: H1-05:B-0110, H1-05:B-0111, H1-05:A-058, H1-05:B-0037, H1-05:B-0038
- **unit-annotation-metric.18** The effect of genome size on the functional-taxonomic turnover comparison was not tested in any study found.
  conf: not stated · class: search (note: "was not tested in any study found") · holds: soil · src: none (a search result) · search: searched, not found (note: "its effect on the functional-taxonomic turnover comparison was not tested in any study found") · trail: H1-05 §Dependence on unit · from: H1-05:B-0111
- **unit-annotation-metric.19** In soil, the comparison depends on functional unit, annotation and metric, but soil evidence for ordering reversals is thin: single-study evidence only, each soil claim resting on one study.
  conf: single (critic: C-012) · class: not stated · holds: soil · src: chenFunctionalRedundancySoil2022, xuDistinctivePatternMechanism2022, guLandConversionCropland2025 · rating: "Weak for soil" (critic: C-012: single-study evidence only) · trail: H1-05 §answers, §Dependence on unit, §critic · from: H1-05:A-036, H1-05:A-052, H1-05:A-053, H1-05:B-0091, H1-05:C-012
- **unit-annotation-metric.20** Not measured in soil: the ordering across dissimilarity measures, compositional (log-ratio) transforms, KO vs COG vs pangenome clusters vs MAG-resolved traits, rarefaction depth, relic-DNA removal and genome-size normalization; no reversal of ordering by any of these factors was found in soil because none was tested.
  conf: not stated · class: search (note: "Not measured:") · holds: soil · src: none (a search result) · search: not stated · trail: H1-05 §answers · from: H1-05:A-058, H1-05:A-059

### averaging-null: Ho and Huang's averaging argument and label-shuffling null
needs: turnover-ordering

- **averaging-null.1** Converting taxon abundances to function abundances through a gene-content matrix sums over many taxa, so functional variability falls by statistical averaging even without any selection; the published abstract keeps this conclusion. 'Function lower than taxonomy' is therefore not by itself evidence of redundancy or selection.
  conf: single (critic: C-027) · class: model (marker) · holds: functions inferred through a gene-content matrix (FAPROTAX-style groups or genome annotations), not shotgun-measured profiles; the preprint read only as a fetch summary and the published body not read · src: hoChallengesQuantifyingFunctional2024 (secondary or abstract-level; modelled; critic: C-048 was "FT preprint via fetch summary; modelled"), hoChallengesInterpretingFunctional2025 (AB) · limit: access (critic: C-050) · rating: "Moderate as a methodological point, but single source" (critic: C-050: that firmness rests on a summary of the preprint) · trail: H1-05 §The averaging problem, §answers, §critic, §Adversarial critique · from: H1-05:I-0012, H1-05:B-0117, H1-05:B-0118, H1-05:A-084, H1-05:B-0127, H1-05:C-024, H1-05:C-027, H1-05:C-028, H1-05:C-050, H1-05:C-060, H1-05:C-119, H1-05:C-122
- **averaging-null.2** Their null permutes taxon labels across the gene-content matrix, which keeps function prevalences and scrambles taxon-function links.
  conf: not stated · class: not stated · holds: functions inferred through a gene-content matrix · src: hoChallengesQuantifyingFunctional2024 · trail: H1-05 §The averaging problem · from: H1-05:B-0119
- **averaging-null.3** For soil- and leaf-derived communities grown in vitro on glucose (Goldford data), functional distance was significantly below the shuffles (functional variability lower than expected), which the authors read as selection for metabolic function.
  conf: not stated · class: not stated · holds: in vitro, a single glucose medium; variability around a mean community within one environment; functions inferred through a gene-content matrix, so indirect for field soil and belonging to the marker-inferred case · src: hoChallengesQuantifyingFunctional2024, hoChallengesInterpretingFunctional2025, goldfordEmergentSimplicityMicrobial2018 (AB) · trail: H1-05 §The averaging problem, §answers, §critic · from: H1-05:B-0120, H1-05:B-0122, H1-05:A-072, H1-05:C-025, H1-05:C-026
- **averaging-null.4** The same null found no evidence of functional selection in bromeliad data (reanalysing the bromeliad study of stable functional-group structure), and found apparent selection in HMP stool to be artifactual: it disappeared under restricted shuffles.
  conf: not stated · class: not stated · holds: bromeliad communities and HMP stool · src: hoChallengesQuantifyingFunctional2024, hoChallengesInterpretingFunctional2025, loucaHighTaxonomicVariability2016 · trail: H1-05 §The averaging problem, §answers · from: H1-05:B-0121, H1-05:B-0124, H1-05:A-073, H1-05:B-0086
- **averaging-null.5** In gut communities in vitro, the null found selection with metabolomics-based groupings.
  conf: not stated · class: not stated · holds: gut communities in vitro · src: hoChallengesQuantifyingFunctional2024 · trail: H1-05 §The averaging problem · from: H1-05:B-0123
- **averaging-null.6** Ho and Huang's label-shuffling null is the only direct microbial test of the functional-taxonomic difference, and the only soil-derived (in vitro) null result; it operates on functions inferred from taxa through a gene-content matrix (the logic of PICRUSt/FAPROTAX), not on shotgun-measured profiles, and tests variability around a mean community within one environment, not turnover across environments. Without it, the answer would rest on non-microbial and indirect microbial nulls.
  conf: single (critic: C-027) · class: not stated · holds: microbial data; marker-inferred function; within-environment dispersion · src: hoChallengesQuantifyingFunctional2024, hoChallengesInterpretingFunctional2025 · contrary: one-sided (critic: C-096) · trail: H1-05 §critic, §Adversarial critique, §answers · from: H1-05:C-023, H1-05:C-041, H1-05:C-042, H1-05:C-096, H1-05:C-098, H1-05:C-099, H1-05:A-099, H1-05:A-100, H1-05:A-101
- **averaging-null.7** Between the preprint and the published version, the second confound was renamed from "bias toward environment-independent beneficial functions" to correlations between functions and taxonomic abundances handled by an "extended null model"; the title changed and the abstract conclusions are otherwise consistent; the published body, and so how the extended null model differs in body text, was not reached.
  conf: not stated · class: not stated · holds: bioRxiv 2024 against Cell Systems 2025 · src: hoChallengesQuantifyingFunctional2024, hoChallengesInterpretingFunctional2025 (AB) · limit: access (note: "The published body was not reached") · trail: H1-05 §The averaging problem, §Preprints and published versions, §answers · from: H1-05:B-0125, H1-05:B-0126, H1-05:B-0141, H1-05:A-094
- **averaging-null.8** The averaging null has not been applied to field soil; on the reviewer's application of it, it bears on every "function lower" soil result, none of which controls for averaging.
  conf: not stated · class: reading (critic: C-107) · holds: the soil 'redundancy' studies (the 845 pooled metagenomes, serpentine, latitudinal forest, coal-fire, fertilizer and dryland studies); acceptable if kept labelled · src: none (the reviewer's application of the null to other studies) · trail: H1-05 §The averaging problem, §answers, §Adversarial critique · from: H1-05:B-0127, H1-05:B-0128, H1-05:A-085, H1-05:C-106, H1-05:C-107, H1-05:C-108, H1-05:I-0003, H1-05:I-0004, H1-05:B-0051, H1-05:B-0053, H1-05:B-0055
- **averaging-null.9** The same null gives opposite answers in two systems: in vitro soil communities show selection, the bromeliad pattern is consistent with averaging.
  conf: cont (note: "Conflicts:") · class: not stated · holds: in vitro soil-derived communities against bromeliads · src: hoChallengesInterpretingFunctional2025 · trail: H1-05 §answers · from: H1-05:A-087, H1-05:A-088, H1-05:A-089

### null-models: null models of the functional-taxonomic comparison, in soil and elsewhere
needs: turnover-ordering, averaging-null

- **null-models.1** No field-soil study was found that applies a null model (taxon-label shuffling of a gene-content matrix, trait randomization, phylogenetic null) to the difference between functional and taxonomic turnover, in shotgun, GeoChip, RNA or protein profiles; nulls across environmental-contrast sizes in soil were not measured either.
  conf: not stated · class: search (note: "No field-soil study was found that applies a null model") · holds: field soil; both search agents looked, using Europe PMC boolean queries on soil, metagenome or GeoChip combined with null, shuffle, randomization, NST or betaNTI; the critic: appropriately worded as a search result · src: none (a search result) · rating: "Weak for soil, where the evidence is absent for field metagenomes and single-study for in vitro soil-derived communities" · search: searched, not found (note: "Both search agents looked") · trail: H1-05 §Soil, §answers, §critic, §Provenance · from: H1-05:A-066, H1-05:A-067, H1-05:A-083, H1-05:A-092, H1-05:A-093, H1-05:B-0112, H1-05:B-0113, H1-05:B-0020, H1-05:C-022, H1-05:C-046
- **null-models.2** Soil nulls found target taxonomic assembly only: SES of taxonomic beta in the precipitation experiment, iCAMP in the dryland study.
  conf: not stated · class: not stated · holds: soil · src: xuDistinctivePatternMechanism2022, saumasanchezFunctionalRedundancyBuffers2024 · trail: H1-05 §Soil, §answers · from: H1-05:A-068, H1-05:B-0114, H1-05:I-0008, H1-05:B-0055
- **null-models.3** In a Tibetan wetland spanning sediment, rhizosphere and bulk soils along salinity, separate null-model analyses put the deterministic share at 32.39% for taxonomy and 45.78%, 43.79% and 48.19% for methane, N and S gene composition (43.8 to 48.2% for function against 32.4%), which the authors read as the environment selecting function rather than taxa; the study does not test the difference itself, and removing it would remove the only soil-inclusive null comparison of functional and taxonomic determinism.
  conf: not stated · class: deriv (marker) · holds: a Tibetan plateau saline-alkaline wetland, sediment and soil pooled; separate nulls on taxonomy and gene sets; the null framework was not named in the text the agent read; a different class of null from Ho and Huang's · src: zhangEnvironmentSelectedMicrobial2025 (FT via agents; derived) · trail: H1-05 §Soil, §answers, §critic, §Adversarial critique · from: H1-05:I-0010, H1-05:A-069, H1-05:A-091, H1-05:A-102, H1-05:B-0115, H1-05:C-029, H1-05:C-030, H1-05:C-102, H1-05:R-0089
- **null-models.4** A simulated 72% species loss in global metagenomes produced limited change in functional categories; this is a resampling construction, not a field comparison.
  conf: not stated · class: model (marker) · holds: global soil metagenomes; resampling; abstract only · src: chenStableSoilMicrobial2021 (AB; modelled) · trail: H1-05 §Soil, §answers · from: H1-05:I-0011, H1-05:A-070, H1-05:B-0116
- **null-models.5** In lake enrichments, 80.2% of community pairs matched a taxon-shuffling null for between-community redundancy; communities were also less functionally dissimilar than random GTDB genome sets, read as selection plus shared pool origin.
  conf: not stated · class: not stated · holds: lake enrichments · src: lemoigneLinkingStochasticAssembly2026 (FT via agents) · trail: H1-05 §Other habitats, §answers · from: H1-05:B-0129, H1-05:B-0130, H1-05:A-074
- **null-models.6** In bioreactors, taxa and genes assembled differently under a null; the preprint said stochasticity was more important for genes, driven by rare genes, while the published abstract drops this and stresses determinism under disturbance.
  conf: not stated · class: not stated · holds: mesocosm-scale bioreactors under press disturbance; abstract only for both versions · src: santillanPressDisturbanceAlters2020 (AB), santillanPressDisturbanceAlters2019 (AB) · trail: H1-05 §Other habitats, §answers, §Preprints and published versions · from: H1-05:B-0131, H1-05:B-0132, H1-05:B-0133, H1-05:A-075, H1-05:B-0144, H1-05:R-0110
- **null-models.7** In contaminated sediments, functional and phylogenetic beta diversity correlated, with the null applied to taxonomy only.
  conf: not stated · class: not stated · holds: sediments along a contamination gradient; abstract only · src: renComparisonMicrobialTaxonomic2016 (AB) · trail: H1-05 §Other habitats · from: H1-05:B-0134, H1-05:R-0124
- **null-models.8** Network nulls on gut gene-content networks and gut proteome networks show redundancy arises from nested gene sharing; this bears only indirectly on between-sample turnover.
  conf: not stated · class: not stated · holds: human gut microbiome, DNA and protein (ultra-deep metaproteomics) · src: tianDecipheringFunctionalRedundancy2020 (FT via agents), liRevealingProteomelevelFunctional2023 (FT via agents) · trail: H1-05 §Other habitats, §answers · from: H1-05:B-0135, H1-05:B-0136, H1-05:A-076, H1-05:R-0111, H1-05:R-0113
- **null-models.9** Across 148 datasets, species-name randomization found functional decay "random given taxonomic decay" in most (13 deviated along space, 3 faster and 10 slower; 11 along environment, all but one faster); the authors note that hypervolume Sørensen gives lower taxonomic than functional similarity by construction for communities sharing no species. This gives independent support, outside bacteria, that most functional turnover is predictable from taxonomic turnover under a randomization null.
  conf: not stated · class: not stated · holds: 148 datasets including diatoms and fungi, no bacteria; deviating counts checked by the critic · src: gracorozaDistanceDecay22022 (FT via agents) · trail: H1-05 §Other habitats, §answers, §critic · from: H1-05:B-0137, H1-05:B-0138, H1-05:A-077, H1-05:A-086, H1-05:C-031, H1-05:C-033
- **null-models.10** Tropical trees along elevation turned over functionally faster than a trait-randomization null predicts.
  conf: not stated · class: not stated · holds: tropical trees along an elevational gradient; read via a fetch summary · src: swensonDeterministicTropicalTree2010 (secondary or abstract-level; critic: C-048 was "FT via fetch summary") · trail: H1-05 §Other habitats, §answers, §critic · from: H1-05:B-0139, H1-05:A-078, H1-05:C-032
- **null-models.11** The 148-dataset synthesis (mostly null-consistent) and the tropical trees (faster than null) disagree.
  conf: cont (note: "disagree in non-microbial systems") · class: not stated · holds: outside bacteria · src: gracorozaDistanceDecay22022, swensonDeterministicTropicalTree2010 · trail: H1-05 §answers · from: H1-05:A-090, H1-05:A-077, H1-05:A-078
- **null-models.12** Louca et al. conclude that non-neutral processes shape within-function taxonomy and redundancy, while Ho and Huang find the bromeliad pattern consistent with averaging; the Louca originals were not reached in full text, so what their tests controlled for is known only from abstracts and from Ho and Huang's description.
  conf: cont (note: "Conflicts: Louca et al. [33][34] conclude that non-neutral processes") · class: not stated · holds: bromeliad communities; the Louca studies known from abstracts · src: loucaHighTaxonomicVariability2016 (AB), loucaFunctionFunctionalRedundancy2018 (AB), hoChallengesInterpretingFunctional2025 (AB) · limit: access (note: "Louca et al. originals were not reached in full text") · trail: H1-05 §answers · from: H1-05:A-087, H1-05:A-088, H1-05:A-098
- **null-models.13** On the reviewer's synthesis, non-microbial syntheses show that lower average functional decay can coexist with most datasets being null-consistent, the same caution Ho and Huang raise for microbes.
  conf: not stated · class: reading (critic: C-103) · holds: the 148-dataset synthesis · src: gracorozaDistanceDecay22022 · trail: H1-05 §How the cases relate · from: H1-05:B-0151, H1-05:C-103, H1-05:A-077

### redundancy-arguments: functional redundancy as an explanation: for, against, critiques
needs: turnover-ordering, averaging-null, null-models

- **redundancy-arguments.1** Arguments for functional redundancy (asserted or measured without nulls) come, in soil, from the 845 pooled metagenomes and the serpentine, latitudinal forest, fertilizer, tillage and dryland studies, and elsewhere from the bromeliad, algal-surface, Ulva and sediment studies and a perspective.
  conf: not stated · class: not stated · holds: asserted or measured without nulls · src: chenFunctionalRedundancySoil2022, igweRedundancyMaintainsMicrobial2026, zhangSoilBacterialEndemism2016, panImpactLongtermN2014, souzaMetagenomicAnalysisReveals2015, saumasanchezFunctionalRedundancyBuffers2024, loucaHighTaxonomicVariability2016, burkeBacterialCommunityAssembly2011, vanderloosLowFunctionalChange2025, soufiTaxonomicVariabilityFunctional2024, loucaFunctionFunctionalRedundancy2018 · trail: H1-05 §Functional redundancy as an explanation, §answers · from: H1-05:C-112, H1-05:C-113, H1-05:A-079, H1-05:I-0003, H1-05:I-0004, H1-05:B-0051, H1-05:B-0055, H1-05:B-0086, H1-05:B-0080, H1-05:B-0081, H1-05:B-0085
- **redundancy-arguments.2** A perspective argues that redundancy and within-function variability are emergent properties of open systems, not drift.
  conf: not stated · class: assert (note: "AB, asserted") · holds: a perspective; abstract only · src: loucaFunctionFunctionalRedundancy2018 (AB, asserted) · trail: H1-05 §Functional redundancy as an explanation · from: H1-05:C-114
- **redundancy-arguments.3** Against or complicating redundancy: coupling holds when all genes are used (the marine time series); functional dispersion tracks taxonomic dispersion (the precipitation experiment); decoupling vanishes at species resolution within groups (one grassland site); averaging alone reproduces lower functional variability (Ho and Huang); function is more responsive under some weak contrasts (the 14-year warming and erosion studies). Fierer 2012, whose authors conclude that functional redundancy 'is not so pervasive as to obscure' the taxonomy-function relationship, is listed only as an annotation-fraction critique, not among these.
  conf: not stated · class: not stated · holds: soil and marine · src: galandStrongLinkMarine2018, xuDistinctivePatternMechanism2022, liuReciprocalChangesDominant2023, hoChallengesInterpretingFunctional2025, hoChallengesQuantifyingFunctional2024, gaoLongtermWarmingMediterraneantype2021, maDivergentTaxonomicFunctional2017 · contrary: one-sided (critic: C-097) · trail: H1-05 §Functional redundancy as an explanation, §answers, §Adversarial critique · from: H1-05:C-115, H1-05:C-116, H1-05:C-117, H1-05:C-118, H1-05:C-119, H1-05:C-120, H1-05:A-080, H1-05:C-097, H1-05:B-0083, H1-05:I-0008, H1-05:B-0079, H1-05:B-0117, H1-05:I-0007, H1-05:B-0061
- **redundancy-arguments.4** Critiques of redundancy readings are reported by ground: aggregation or averaging (Ho and Huang; modelled plus reanalysis); annotation fraction and bias (13 to 23% annotated in the 16-soil study; the marine time series); unannotated genes varying with soil (indirect); genome size (shown in human gut, with soil shifts under N and P addition and heating; indirect); asymmetric power or sample size between the functional and taxonomic tests (the serpentine study; the reviewer's reading); and marker-inferred function being circular (the ZnO, alpine PICRUSt2 and vermicomposting studies), with weak coupling of inferred to measured profiles in the marine time series.
  conf: not stated · class: not stated · holds: soil and other habitats · src: hoChallengesInterpretingFunctional2025, hoChallengesQuantifyingFunctional2024, fiererCrossbiomeMetagenomicAnalyses2012, galandStrongLinkMarine2018, hollandmoritzEcologicalPerspectiveMicrobial2021, nayfachAverageGenomeSize2015, leffConsistentResponsesSoil2015, barnettDisturbanceIncreasesSoil2025, igweRedundancyMaintainsMicrobial2026, dineshSoilPollutedNano2023, liAsynchronousPatternsSoil2024, airaFasterTurnoverTaxonomic2026 · trail: H1-05 §Functional redundancy as an explanation, §answers · from: H1-05:C-121, H1-05:C-122, H1-05:C-123, H1-05:C-124, H1-05:C-125, H1-05:C-126, H1-05:C-127, H1-05:A-081, H1-05:B-0117, H1-05:I-0001, H1-05:B-0083, H1-05:B-0110, H1-05:I-0004, H1-05:I-0005, H1-05:I-0006, H1-05:I-0009
- **redundancy-arguments.5** No study was found that examines relic DNA, compositionality or sequencing depth for this comparison; these were not searched in depth by either agent, so the absence is weakly established.
  conf: not stated · class: search (note: "not searched in depth by either agent") · holds: the functional-taxonomic comparison; the critic: soil studies exist on the effect of relic DNA on taxonomic beta diversity, and depth and annotation-rate effects were not searched · src: none (a search result) · search: not searched (note: "not searched in depth by either agent") · trail: H1-05 §Functional redundancy as an explanation, §answers, §Provenance, §Adversarial critique · from: H1-05:C-128, H1-05:A-082, H1-05:B-0020, H1-05:C-083, H1-05:C-084
- **redundancy-arguments.6** The review's lean towards 'function lower is not evidence of redundancy' rests on Ho and Huang (modelled, single source) and Graco-Roza (non-bacterial); it is not simply echoed from the brief.
  conf: single (critic: C-110) · class: not stated · holds: the review's overall reading · src: hoChallengesInterpretingFunctional2025, hoChallengesQuantifyingFunctional2024, gracorozaDistanceDecay22022 · trail: H1-05 §Adversarial critique · from: H1-05:C-110, H1-05:C-111

## Do not say

- **dns.1** "Unlike the soil cross-biome result, marine function stays lower even under a strong contrast."
  why: The soil cross-biome study made no magnitude comparison, and the 845 pooled soil metagenomes are themselves a strong-contrast soil case of function lower; the contrast treats a correlation result and a magnitude result as the same kind of finding. · instead: other-habitats.2, turnover-ordering.2 · trail: H1-05 §Other habitats, §critic, §Adversarial critique · from: H1-05:B-0082, H1-05:C-005, H1-05:C-035, H1-05:C-036, H1-05:C-100, H1-05:I-0003
- **dns.2** "Three independent soil datasets show that functional and taxonomic dissimilarity covary."
  why: The three datasets are not independent in lineage: two come from one group, and the third pools MG-RAST submissions that may include the first. · instead: covariation.7 · trail: H1-05 §Covariation at strong contrasts, §critic · from: H1-05:B-0039, H1-05:C-002, H1-05:C-038
- **dns.3** "Xu et al. 2022 is the only within-site test of how contrast size changes the functional-taxonomic comparison."
  why: It measures within-treatment dispersion with no directional shift in either community and does not compare the two turnovers' magnitudes, so it bears only indirectly on the question and should be labelled indirect. · instead: contrast-size.2 · trail: H1-05 §answers, §critic · from: H1-05:A-035, H1-05:C-039, H1-05:C-040
- **dns.4** "Ho and Huang's null is the direct microbial test of the functional-taxonomic difference."
  why: It works on functions inferred from taxonomy through a gene-content matrix and on variability within one environment; the review does not label it as marker-inferred or as dispersion rather than cross-environment turnover. · instead: averaging-null.6 · trail: H1-05 §critic, §Adversarial critique · from: H1-05:C-041, H1-05:C-042, H1-05:C-043, H1-05:C-098
- **dns.5** "In soil, the functional-taxonomic gap widens as functions are aggregated."
  why: This is the reviewer's inference from one study, phrased as a finding; the authors state only that functional similarity was higher at SEED levels 1 and 2 against all five taxonomic ranks. · instead: unit-annotation-metric.1 · trail: H1-05 §answers, §critic, §Adversarial critique · from: H1-05:A-038, H1-05:C-015, H1-05:C-044, H1-05:C-045, H1-05:C-059
- **dns.6** "Aggregation alone lowers functional variability, so in every soil study 'function lower' is not evidence of redundancy."
  why: This is framed as a methodological point bearing on every soil study, but it rests on Ho and Huang alone and is modelled. · instead: averaging-null.1, averaging-null.8 · trail: H1-05 §Adversarial critique · from: H1-05:C-060, H1-05:A-084
- **dns.7** "GeoChip underlies the soil studies where function was as or more responsive, so the reverse ordering is a platform effect."
  why: It is the reviewer's cross-study observation, drawn from three papers, two of them from one group (Zhou/Yang), and not a tested result. · instead: unit-annotation-metric.16 · trail: H1-05 §Adversarial critique, §Dependence on unit · from: H1-05:C-061, H1-05:B-0109
- **dns.8** "Marine and host-associated studies mostly report lower functional turnover."
  why: This mixes FAPROTAX-derived, abstract-only and single-time-series evidence; the only strong-contrast case is one study with MAG-based taxonomy. · instead: other-habitats.11 · trail: H1-05 §Adversarial critique · from: H1-05:C-062
- **dns.9** "The choice of metric reverses the functional-taxonomic conclusion."
  why: This rests on one study (27 paired steppe and cropland soils), flagged in the sensitivity note but stated generally in the review. · instead: unit-annotation-metric.7 · trail: H1-05 §Adversarial critique · from: H1-05:C-063, H1-05:B-0077
- **dns.10** "Graco-Roza et al. 2022 is a non-microbial synthesis."
  why: It includes diatoms and fungi (it lacks bacteria), so calling it non-microbial is wrong and blurs the microbial against non-microbial split. · instead: other-habitats.8 · trail: H1-05 §critic, §Adversarial critique · from: H1-05:C-011, H1-05:C-055, H1-05:C-101
- **dns.11** "In soil, separate assembly nulls show function is more deterministic than taxonomy."
  why: The wetland study pools sediment and soil, uses separate nulls on taxonomy and gene sets, and does not test the difference itself. · instead: null-models.3 · trail: H1-05 §Adversarial critique, §critic · from: H1-05:C-102, H1-05:C-029, H1-05:C-030
- **dns.12** "Ho and Huang's null shows selection for metabolic function in soil communities."
  why: The soil result comes from a single in vitro glucose medium, on functions inferred through a gene-content matrix and variability within one environment, so it is indirect for field soil. · instead: averaging-null.3 · trail: H1-05 §critic, §Adversarial critique · from: H1-05:C-026, H1-05:C-096
- **dns.13** "Ho and Huang's preprint, Barnett and Shade, Burke and Swenson were read in full text."
  why: They were read through fetch summaries, which are not a full-text reading, so they should be labelled secondary or abstract-level unless the text was read. · instead: none · trail: H1-05 §Adversarial critique · from: H1-05:C-047, H1-05:C-048
- **dns.14** "The dryland study's 'function lower' result was read in full text."
  why: Only its abstract and methods were read, so it is abstract-level for its result claim. · instead: turnover-ordering.10 · trail: H1-05 §Adversarial critique · from: H1-05:C-051, H1-05:B-0055
- **dns.15** "Between serpentine and non-serpentine soils, functional turnover is lower than taxonomic turnover."
  why: The result sets a significant test against a non-significant one on datasets of different size after QC, which suggests limited power on the functional side rather than an absence of structure. · instead: turnover-ordering.3, turnover-ordering.4 · trail: H1-05 §Functional turnover reported lower · from: H1-05:B-0049, H1-05:B-0050, H1-05:I-0004
- **dns.16** "Along the Changbai elevation gradient, functional turnover is stronger than taxonomic turnover."
  why: That is the reviewer's reading; the authors describe the patterns as similar, and the two r values come from different platforms and are not on a common scale. · instead: turnover-ordering.18 · trail: H1-05 §Functional turnover reported higher · from: H1-05:B-0063, H1-05:B-0064, H1-05:B-0065, H1-05:B-0062
- **dns.17** "The ZnO and alpine PICRUSt studies are two independent tests of soil functional redundancy."
  why: Both infer function from the same 16S data, so they are not independent tests. · instead: turnover-ordering.14, turnover-ordering.15 · trail: H1-05 §Functional turnover reported lower · from: H1-05:B-0058, H1-05:I-0005, H1-05:I-0006
- **dns.18** "Chronosequences show functional and taxonomic turnover diverging."
  why: The chronosequence papers report alpha diversity moving in opposite directions, but no paired turnover comparison. · instead: chronosequence-precedents.1, chronosequence-precedents.2 · trail: H1-05 §Nearest precedents · from: H1-05:B-0073
- **dns.19** "Within-treatment dispersion results answer how turnover across environments compares."
  why: The precipitation experiment's PERMDISP within treatments and Ho and Huang's distance from the mean community in one medium are within-environment dispersion, used without an indirect label to answer questions about turnover across environments. · instead: contrast-size.2, averaging-null.6 · trail: H1-05 §Adversarial critique · from: H1-05:C-099, H1-05:I-0008, H1-05:B-0117
- **dns.20** "In soil, the unannotated fraction biases functional turnover."
  why: That unknown-function genes vary with soil properties is indirect support for an annotation-bias critique, not a demonstration of its effect on turnover. · instead: unit-annotation-metric.6 · trail: H1-05 §Dependence on unit · from: H1-05:B-0099
- **dns.21** "Global N-cycling pathways turn over less than the genera that encode them."
  why: The study contrasts drivers, not turnovers, so it is indirect for the comparison. · instead: chronosequence-precedents.3 · trail: H1-05 §Nearest precedents · from: H1-05:B-0076, H1-05:B-0075
- **dns.22** "A marine time series and a soil experiment contradict each other on whether annotation matters."
  why: They use different measures (regression of similarities against within-treatment dispersion) and habitats, so in the review's words they do not directly contradict. · instead: unit-annotation-metric.5 · trail: H1-05 §answers · from: H1-05:A-056, H1-05:A-055

## Gaps

- **gap.1** Bahram et al. 2018 (Nature 560:233-237), the largest paired metabarcoding plus metagenome global topsoil set (shotgun plus amplicon on the same samples), was not read beyond an abstract; the publisher was not tried; the stage-2 check says it should be read in full by hand.
  blocks: covariation, turnover-ordering, unit-annotation-metric · origin: critic coverage gap; a source not obtained that matters · src: bahramStructureFunctionGlobal2018 · search: not stated · trail: H1-05 §Adversarial critique, §Stage 2 check · from: H1-05:C-082, H1-05:B-0028
- **gap.2** Relic DNA: soil studies exist on its effect on taxonomic beta diversity (Carini et al. 2016 Nat Microbiol; Lennon et al. 2018 mBio; mBio 2020), indirect evidence for the taxonomic side of the comparison that the review does not cite while reporting relic-DNA critiques as not found.
  blocks: unit-annotation-metric, null-models · origin: critic coverage gap; soil extracellular DNA · search: not searched (note: "not searched in depth by either agent") · trail: H1-05 §Adversarial critique, §Provenance · from: H1-05:C-083, H1-05:B-0020
- **gap.3** Sequencing depth and annotation-rate effects on functional-profile dissimilarity (for example the comparative-metagenomics normalization literature beyond Nayfach 2015); compositional (Aitchison, CLR) comparisons were reported as not found without naming the routes.
  blocks: unit-annotation-metric · origin: critic coverage gap; shotgun functional profiles, methodological · search: not searched (critic: C-084) · trail: H1-05 §Adversarial critique · from: H1-05:C-084
- **gap.4** Soil metatranscriptome (and protein) turnover compared with taxonomic turnover: no study reported, the only non-DNA soil case being the precipitation experiment's metaproteome dispersion; forest-soil and rhizosphere metatranscriptome studies were not searched specifically.
  blocks: turnover-ordering, unit-annotation-metric · origin: critic coverage gap; soil RNA · search: not searched (critic: C-087) · trail: H1-05 §Adversarial critique, §answers, §Provenance · from: H1-05:C-085, H1-05:C-086, H1-05:C-087, H1-05:A-025, H1-05:B-0021
- **gap.5** Recent soil chronosequence metagenome studies (Greenlandic glacial chronosequence, FEMS Microbiol Ecol 2026; ecosystem retrogression, mLife 2026; ISME Commun 2026) not assessed for paired turnover comparisons; chronosequences with a head-to-head beta comparison were not measured.
  blocks: chronosequence-precedents, contrast-size · origin: critic coverage gap · search: not stated · trail: H1-05 §Adversarial critique, §answers · from: H1-05:C-088, H1-05:A-027
- **gap.6** Chen et al. 2021a (water metagenomes, function-taxonomy similarity r2 0.3344, function lower), cited within the global soil study, is not reported under other habitats.
  blocks: other-habitats · origin: critic coverage gap; aquatic MG-RAST metagenomes · search: not stated · trail: H1-05 §Adversarial critique · from: H1-05:C-089
- **gap.7** The taxonomic side's measurement type (16S amplicon, read-based RefSeq, MAG) is not tabulated per study, although it plausibly affects the ordering.
  blocks: unit-annotation-metric · origin: critic coverage gap · search: not stated · trail: H1-05 §Adversarial critique · from: H1-05:C-090
- **gap.8** Fungal shotgun turnover comparisons beyond the ectomycorrhizal and mycobiome studies; archaeal and protist functional turnover in soil are not addressed.
  blocks: turnover-ordering · origin: critic coverage gap; soil fungi, archaea, protists · search: not stated · trail: H1-05 §Adversarial critique, §answers · from: H1-05:C-091, H1-05:A-028
- **gap.9** A per-study table giving measurement type, functional unit, annotation, dissimilarity measure and contrast, as the brief's evidence-to-gather bullet requires; these attributes are scattered through the text.
  blocks: unit-annotation-metric, contrast-size · origin: critic coverage gap · search: not stated · trail: H1-05 §Adversarial critique · from: H1-05:C-092
- **gap.10** The stage-2 check was triggered: write a follow-up brief, sized separately, on the habitat classes with shotgun results not assessed (soil chronosequence metagenomes, soil metatranscriptomes, fungal, archaeal and protist functional turnover, aquatic MG-RAST comparisons) and on the per-study measurement table, with methodological gaps on both sides (relic DNA on the taxonomic side; depth, annotation rate and compositional measures on the functional side); no new null-model family with direct soil results was named.
  blocks: turnover-ordering, unit-annotation-metric, chronosequence-precedents · origin: the note's stage-2 check (ROUTING condition) · search: not stated · trail: H1-05 §Stage 2 check · from: H1-05:B-0024, H1-05:B-0025, H1-05:B-0026, H1-05:B-0027, H1-05:B-0028
- **gap.11** The published Ho and Huang (Cell Systems 2025) body text was not read, and the preprint was read only as a fetch summary, although the bioRxiv full text is openly reachable; how the published 'extended null model' differs from the preprint is unknown.
  blocks: averaging-null · origin: critic access finding; a source not obtained · src: hoChallengesInterpretingFunctional2025, hoChallengesQuantifyingFunctional2024 · search: not stated · trail: H1-05 §Adversarial critique, §answers, §Sources not obtained · from: H1-05:C-049, H1-05:A-094, H1-05:R-0009
- **gap.12** A label-shuffling, trait or phylogenetic null applied to field-soil shotgun, GeoChip, RNA or protein profiles, testing whether functional turnover is lower than expected given taxonomic turnover, including across environmental-contrast sizes.
  blocks: null-models, averaging-null · origin: the review's not-found result · search: searched, not found (note: "Both search agents looked") · trail: H1-05 §answers, §Soil · from: H1-05:A-092, H1-05:A-093, H1-05:B-0113
- **gap.13** A soil test of how the functional-taxonomic gap scales with environmental distance.
  blocks: contrast-size · origin: the review's not-found result · search: searched, not found (note: "No soil study was found that tests how the functional-taxonomic gap scales with environmental distance") · trail: H1-05 §answers · from: H1-05:A-013
- **gap.14** Soil tests of the ordering across dissimilarity measures, compositional transforms, functional units (KO, COG, pangenome clusters, MAG-resolved traits), rarefaction depth, relic-DNA removal and genome-size normalization.
  blocks: unit-annotation-metric · origin: the review's not-measured result · search: not stated · trail: H1-05 §answers · from: H1-05:A-058, H1-05:A-059
- **gap.15** The Louca et al. originals (2016 Science; 2016/2017 and 2018 Nat Ecol Evol) and Villéger et al. 2013 were not reached in full text, so what the Louca tests controlled for is known only from abstracts and from Ho and Huang's description.
  blocks: null-models, other-habitats · origin: sources not obtained that matter · src: loucaDecouplingFunctionTaxonomy2016, loucaHighTaxonomicVariability2016, loucaFunctionFunctionalRedundancy2018, villegerDecomposingFunctionalDiversity2013 · search: not stated · trail: H1-05 §answers, §Sources not obtained · from: H1-05:A-098, H1-05:R-0019, H1-05:R-0023
- **gap.16** The marine time-series (Galand 2018) figures rest on the agents' reading: its full-text XML returned empty to the reviewer.
  blocks: unit-annotation-metric, other-habitats · origin: the note's synthesis-stage check · src: galandStrongLinkMarine2018 · search: not stated · trail: H1-05 §Provenance · from: H1-05:B-0019
- **gap.17** The note contradicts itself on its sources not obtained: the list says nothing beyond a citation was reachable for them and none supports any claim in the review, yet it records abstracts obtained or used for several of them (Bahram 2018, Fierer 2013, the Louca studies, Villéger 2013), and the Ho and Huang Cell Systems and Louca abstracts are cited in the review.
  blocks: none · origin: a note that contradicts itself · search: not stated · trail: H1-05 §Sources not obtained · from: H1-05:R-0001, H1-05:R-0005, H1-05:R-0022, H1-05:R-0024

## Out of scope

- H1-05:C-064..081: reference corrections and checks, applied in Sources
- H1-05:C-056..058: the Holland-Moritz registry caveat, corrected in Sources
- H1-05:C-034: the critic's count of over-reaches; each of the five is its own item (C-035..045)
- H1-05:C-109: the brief's wording in the expectation-echo check (provenance, kept in the result note)
- H1-05:A-029..031, H1-05:A-060..062, H1-05:A-095..097: access basis of the answers (provenance; each source's access is in Sources)

## Sources

```bibtex
@article{fiererCrossbiomeMetagenomicAnalyses2012,
  author = {Fierer, Noah and Leff, Jonathan W. and Adams, Byron J. and Nielsen, Uffe N. and Bates, Scott Thomas and Lauber, Christian L. and Owens, Sarah and Gilbert, Jack A. and Wall, Diana H. and Caporaso, J. Gregory},
  title = {Cross-biome metagenomic analyses of soil microbial communities and their functional attributes},
  journal = {Proceedings of the National Academy of Sciences},
  year = {2012},
  volume = {109},
  number = {52},
  pages = {21390--21395},
  doi = {10.1073/pnas.1215210110},
  note = {access: full_text (via search agents); cited as: H1-05 [1]; critic: H1-05:C-052, C-053 confirmed the figures in full text (PMC3535587), so the label can be upgraded}
}
@article{leffConsistentResponsesSoil2015,
  author = {Leff, Jonathan W. and Jones, Stuart E. and Prober, Suzanne M. and Barberán, Albert and Borer, Elizabeth T. and Firn, Jennifer L. and Harpole, W. Stanley and Hobbie, Sarah E. and Hofmockel, Kirsten S. and Knops, Johannes M. H. and McCulley, Rebecca L. and Pierre, Kimberly La and Risch, Anita C. and Seabloom, Eric W. and Schütz, Martin and Steenbock, Christopher and Stevens, Carly J. and Fierer, Noah},
  title = {Consistent responses of soil microbial communities to elevated nutrient inputs in grasslands across the globe},
  journal = {Proceedings of the National Academy of Sciences},
  year = {2015},
  volume = {112},
  number = {35},
  pages = {10967--10972},
  doi = {10.1073/pnas.1508382112},
  note = {access: full_text (via search agents); cited as: H1-05 [2]; critic: H1-05:C-052, C-053 confirmed the figures in full text (PMC4568213), so the label can be upgraded}
}
@article{chenFunctionalRedundancySoil2022,
  author = {Chen, Huaihai and Ma, Kayan and Lu, Caiyan and Fu, Qi and Qiu, Yingbo and Zhao, Jiayi and Huang, Yu and Yang, Yuchun and Schadt, Christopher W. and Chen, Hao},
  title = {Functional redundancy in soil microbial community based on metagenomics across the globe},
  journal = {Frontiers in Microbiology},
  year = {2022},
  volume = {13},
  pages = {878978},
  doi = {10.3389/fmicb.2022.878978},
  note = {access: full_text (rechecked by the reviewer); cited as: H1-05 [3]}
}
@article{igweRedundancyMaintainsMicrobial2026,
  author = {Igwe, Alexandria N. and Afkhami, Michelle E.},
  title = {Redundancy maintains microbial ecosystem functional potential despite taxonomic shifts between serpentine and nonserpentine soils},
  journal = {Microbial Genomics},
  year = {2026},
  volume = {12},
  number = {9},
  doi = {10.1099/mgen.0.001835},
  note = {access: full_text (rechecked by the reviewer); cited as: H1-05 [4]; article number not in the Crossref record (Crossref gives vol 12 issue 9 with no article number, critic: H1-05:C-080); incomplete: pages}
}
@article{gaoLongtermWarmingMediterraneantype2021,
  author = {Gao, Ying and Ding, Junjun and Yuan, Mengting and Chiariello, Nona and Docherty, Kathryn and Field, Chris and Gao, Qun and Gu, Baohua and Gutknecht, Jessica and Hungate, Bruce A. and Le Roux, Xavier and Niboyet, Audrey and Qi, Qi and Shi, Zhou and Zhou, Jizhong and Yang, Yunfeng},
  title = {Long-term warming in a Mediterranean-type grassland affects soil bacterial functional potential but not bacterial taxonomic composition},
  journal = {npj Biofilms and Microbiomes},
  year = {2021},
  volume = {7},
  number = {1},
  pages = {17},
  doi = {10.1038/s41522-021-00187-7},
  note = {access: full_text (rechecked by the reviewer); cited as: H1-05 [5]}
}
@article{shenDramaticIncreasesSoil2016,
  author = {Shen, Congcong and Shi, Yu and Ni, Yingying and Deng, Ye and Nostrand, Joy D. Van and He, Zhili and Zhou, Jizhong and Chu, Haiyan},
  title = {Dramatic increases of soil microbial functional gene diversity at the treeline ecotone of Changbai Mountain},
  journal = {Frontiers in Microbiology},
  year = {2016},
  volume = {7},
  pages = {1184},
  doi = {10.3389/fmicb.2016.01184},
  note = {access: full_text (via search agents); cited as: H1-05 [6]}
}
@article{zhangSoilBacterialEndemism2016,
  author = {Zhang, Yuguang and Cong, Jing and Lu, Hui and Deng, Ye and Liu, Xiao and Zhou, Jizhong and Li, Diqiang},
  title = {Soil bacterial endemism and potential functional redundancy in natural broadleaf forest along a latitudinal gradient},
  journal = {Scientific Reports},
  year = {2016},
  volume = {6},
  pages = {28819},
  doi = {10.1038/srep28819},
  note = {access: full_text (via search agents); cited as: H1-05 [7]}
}
@article{goodallTaxonomicFilteringAccompanies2026,
  author = {Goodall, Tim and Busi, Susheel Bhanu and Jones, Briony and Thorpe, Amy and Griffiths, Robert I and Redhead, John and Hulmes, Lucy and Hulmes, Sarah and Ridding, Lucy and Peyton, Jodey and Pereira, Gloria and Gweon, Hyun Soon and Read, Daniel S and Pywell, Richard},
  title = {Taxonomic filtering accompanies functional expansion during long-term soil restoration},
  journal = {The ISME Journal},
  year = {2026},
  volume = {20},
  number = {1},
  pages = {wrag131},
  doi = {10.1093/ismejo/wrag131},
  note = {access: full_text (via search agents); cited as: H1-05 [9]}
}
@article{sveenFunctionalDiversitySoil2025,
  author = {Sveen, Tord Ranheim and Viketoft, Maria and Bengtsson, Jan and Strengbom, Joachim and Lejoly, Justine and Buegger, Franz and Pritsch, Karin and Fritscher, Joachim and Hildebrand, Falk and Osburn, Ernest and Hannula, S. Emilia and Bahram, Mo},
  title = {Functional diversity of soil microbial communities increases with ecosystem development},
  journal = {Nature Communications},
  year = {2025},
  volume = {16},
  number = {1},
  pages = {10408},
  doi = {10.1038/s41467-025-66544-8},
  note = {access: full_text (via search agents); cited as: H1-05 [10]}
}
@article{liuReciprocalChangesDominant2023,
  author = {Liu, Huaiqiang and Li, Frank Yonghong and Liu, Jiayue and Shi, Chunjun and Tang, Kuanyan and Yang, Qianhui and Liu, Yu and Fu, Qiang and Gao, Xiaotian and Wang, Ning and Guo, Wei},
  title = {The reciprocal changes in dominant species with complete metabolic functions explain the decoupling phenomenon of microbial taxonomic and functional composition in a grassland},
  journal = {Frontiers in Microbiology},
  year = {2023},
  volume = {14},
  pages = {1113157},
  doi = {10.3389/fmicb.2023.1113157},
  note = {access: full_text (via search agents); cited as: H1-05 [11]}
}
@article{nelsonGlobalBiogeographyMicrobial2016,
  author = {Nelson, Michaeline B. and Martiny, Adam C. and Martiny, Jennifer B. H.},
  title = {Global biogeography of microbial nitrogen-cycling traits in soil},
  journal = {Proceedings of the National Academy of Sciences},
  year = {2016},
  volume = {113},
  number = {29},
  pages = {8033--8040},
  doi = {10.1073/pnas.1601070113},
  note = {access: full_text (via search agents); cited as: H1-05 [12]}
}
@article{panImpactLongtermN2014,
  author = {Pan, Yao and Cassman, Noriko and de Hollander, Mattias and Mendes, Lucas W. and Korevaar, Hein and Geerts, Rob H.E.M. and van Veen, Johannes A. and Kuramae, Eiko E.},
  title = {Impact of long-term N, P, K, and NPK fertilization on the composition and potential functions of the bacterial community in grassland soil},
  journal = {FEMS Microbiology Ecology},
  year = {2014},
  volume = {90},
  number = {1},
  pages = {195--205},
  doi = {10.1111/1574-6941.12384},
  note = {access: abstract_only; cited as: H1-05 [13]}
}
@article{yangDecouplingMicrobialCommunity2021,
  author = {Yang, Sizhong and Liebner, Susanne and Svenning, Mette Marianne and Tveit, Alexander Tøsdal},
  title = {Decoupling of microbial community dynamics and functions in Arctic peat soil exposed to short term warming},
  journal = {Molecular Ecology},
  year = {2021},
  volume = {30},
  number = {20},
  pages = {5094--5104},
  doi = {10.1111/mec.16118},
  note = {access: abstract_only; cited as: H1-05 [14]}
}
@article{maDivergentTaxonomicFunctional2017,
  author = {Ma, Xingyu and Zhao, Cancan and Gao, Ying and Liu, Bin and Wang, Tengxu and Yuan, Tong and Hale, Lauren and Nostrand, Joy D. Van and Wan, Shiqiang and Zhou, Jizhong and Yang, Yunfeng},
  title = {Divergent taxonomic and functional responses of microbial communities to field simulation of aeolian soil erosion and deposition},
  journal = {Molecular Ecology},
  year = {2017},
  volume = {26},
  number = {16},
  pages = {4186--4196},
  doi = {10.1111/mec.14194},
  note = {access: abstract_only; cited as: H1-05 [15]}
}
@article{freyLongtermMercuryContamination2022,
  author = {Frey, Beat and Rast, Basil M. and Qi, Weihong and Stierli, Beat and Brunner, Ivano},
  title = {Long-term mercury contamination does not affect the microbial gene potential for C and N cycling in soils but enhances detoxification gene abundance},
  journal = {Frontiers in Microbiology},
  year = {2022},
  volume = {13},
  pages = {1034138},
  doi = {10.3389/fmicb.2022.1034138},
  note = {access: abstract_only; cited as: H1-05 [16]}
}
@article{katoTimeseriesMetagenomicAnalysis2015,
  author = {Kato, Hiromi and Mori, Hiroshi and Maruyama, Fumito and Toyoda, Atsushi and Oshima, Kenshiro and Endo, Ryo and Fuchu, Genki and Miyakoshi, Masatoshi and Dozono, Ayumi and Ohtsubo, Yoshiyuki and Nagata, Yuji and Hattori, Masahira and Fujiyama, Asao and Kurokawa, Ken and Tsuda, Masataka},
  title = {Time-series metagenomic analysis reveals robustness of soil microbiome against chemical disturbance},
  journal = {DNA Research},
  year = {2015},
  volume = {22},
  number = {6},
  pages = {413--424},
  doi = {10.1093/dnares/dsv023},
  note = {access: abstract_only; cited as: H1-05 [17]}
}
@article{souzaMetagenomicAnalysisReveals2015,
  author = {Souza, Renata Carolini and Hungria, Mariangela and Cantão, Maurício Egídio and Vasconcelos, Ana Tereza Ribeiro and Nogueira, Marco Antonio and Vicente, Vânia Aparecida},
  title = {Metagenomic analysis reveals microbial functional redundancies and specificities in a soil under different tillage and crop-management regimes},
  journal = {Applied Soil Ecology},
  year = {2015},
  volume = {86},
  pages = {106--112},
  doi = {10.1016/j.apsoil.2014.10.010},
  note = {access: abstract_only; cited as: H1-05 [18]}
}
@article{chenStableSoilMicrobial2021,
  author = {Chen, Huaihai and Ma, Kayan and Huang, Yu and Yao, Zhiyuan and Chu, Chengjin},
  title = {Stable soil microbial functional structure responding to biodiversity loss based on metagenomic evidences},
  journal = {Frontiers in Microbiology},
  year = {2021},
  volume = {12},
  pages = {716764},
  doi = {10.3389/fmicb.2021.716764},
  note = {access: abstract_only; cited as: H1-05 [19]}
}
@article{pellitierPotentialFunctionalDivergence2024,
  author = {Pellitier, Peter T and Nuland, Michael Van and Salamov, Asaf and Grigoriev, Igor V and Peay, Kabir G},
  title = {Potential for functional divergence in ectomycorrhizal fungal communities across a precipitation gradient},
  journal = {ISME Communications},
  year = {2024},
  volume = {4},
  number = {1},
  pages = {ycae031},
  doi = {10.1093/ismeco/ycae031},
  note = {access: abstract_only; cited as: H1-05 [20]}
}
@article{talbotEndemismFunctionalConvergence2014,
  author = {Talbot, Jennifer M. and Bruns, Thomas D. and Taylor, John W. and Smith, Dylan P. and Branco, Sara and Glassman, Sydney I. and Erlandson, Sonya and Vilgalys, Rytas and Liao, Hui-Ling and Smith, Matthew E. and Peay, Kabir G.},
  title = {Endemism and functional convergence across the North American soil mycobiome},
  journal = {Proceedings of the National Academy of Sciences},
  year = {2014},
  volume = {111},
  number = {17},
  pages = {6341--6346},
  doi = {10.1073/pnas.1402584111},
  note = {access: abstract_only; cited as: H1-05 [21]}
}
@article{xuDistinctivePatternMechanism2022,
  author = {Xu, Minjie and Zhu, Xunzhi and Chen, Shiping and Pang, Shuang and Liu, Wei and Gao, Lili and Yang, Wei and Li, Tingting and Zhang, Yuhan and Luo, Chun and He, Dandan and Wang, Zhiping and Fan, Yi and Han, Xingguo and Zhang, Ximei},
  title = {Distinctive pattern and mechanism of precipitation changes affecting soil microbial assemblages in the Eurasian steppe},
  journal = {iScience},
  year = {2022},
  volume = {25},
  number = {3},
  pages = {103893},
  doi = {10.1016/j.isci.2022.103893},
  note = {access: full_text (rechecked by the reviewer); cited as: H1-05 [22]}
}
@article{guLandConversionCropland2025,
  author = {Gu, Haidong and Liu, Zhuxiu and Liu, Song and Hu, Xiaojing and Yu, Zhenhua and Li, Yansheng and Li, Lujun and Sui, Yueyu and Jin, Jian and Liu, Xiaobing and Jia, Zhongjun and Sun, Lei and Adams, Jonathan M and van der Heijden, Marcel G A and Liu, Junjie and Wang, Guanghua},
  title = {Land conversion to cropland homogenizes variation in soil biota, gene assemblages, and ecological strategies on local and regional scales},
  journal = {The ISME Journal},
  year = {2025},
  volume = {19},
  number = {1},
  pages = {wraf264},
  doi = {10.1093/ismejo/wraf264},
  note = {access: full_text (rechecked by the reviewer); cited as: H1-05 [23]}
}
@article{saumasanchezFunctionalRedundancyBuffers2024,
  author = {Sauma-Sánchez, Tomás and Alcorta, Jaime and Tamayo-Leiva, Javier and Díez, Beatriz and Bezuidenhout, Hugo and Cowan, Don A and Ramond, Jean-Baptiste},
  title = {Functional redundancy buffers the effect of poly-extreme environmental conditions on southern African dryland soil microbial communities},
  journal = {FEMS Microbiology Ecology},
  year = {2024},
  volume = {100},
  number = {12},
  pages = {fiae157},
  doi = {10.1093/femsec/fiae157},
  note = {access: abstract_only for its result claim (critic: H1-05:C-051; the note said FT via agents, partly read: abstract and methods only); cited as: H1-05 [24]}
}
@article{dineshSoilPollutedNano2023,
  author = {Dinesh, R. and Sreena, C.P. and Sheeja, T.E. and Kumar, I.P. Vijesh and Praveena, R. and Charles, Sona and Srinivasan, V. and Jayarajan, K. and Sajith, V. and Subila, K.P. and Haritha, P.},
  title = {Soil polluted with nano ZnO reveals unstable bacterial communities and decoupling of taxonomic and functional diversities},
  journal = {Science of the Total Environment},
  year = {2023},
  volume = {889},
  pages = {164285},
  doi = {10.1016/j.scitotenv.2023.164285},
  note = {access: abstract_only; cited as: H1-05 [25]}
}
@article{liAsynchronousPatternsSoil2024,
  author = {Li, Xianping and Li, Teng and Li, Huixin},
  title = {Asynchronous patterns in soil bacterial diversity and functional potentials along an alpine altitudinal gradient},
  journal = {Frontiers in Microbiology},
  year = {2024},
  volume = {15},
  pages = {1428815},
  doi = {10.3389/fmicb.2024.1428815},
  note = {access: full_text (via search agents); cited as: H1-05 [26]}
}
@article{zhangEnvironmentSelectedMicrobial2025,
  author = {Zhang, Hongjie and Zhao, Dayong and Wu, Qinglong L. and Zeng, Jin},
  title = {Environment selected microbial function rather than taxonomic species in a plateau saline-alkaline wetland},
  journal = {Applied and Environmental Microbiology},
  year = {2025},
  volume = {91},
  number = {7},
  pages = {e02206--24},
  doi = {10.1128/aem.02206-24},
  note = {access: full_text (via search agents); cited as: H1-05 [28]}
}
@article{hoChallengesInterpretingFunctional2025,
  author = {Ho, Po-Yi and Huang, Kerwyn Casey},
  title = {Challenges in interpreting functional redundancy and quantifying functional selection in microbial communities},
  journal = {Cell Systems},
  year = {2025},
  volume = {16},
  number = {8},
  pages = {101350},
  doi = {10.1016/j.cels.2025.101350},
  note = {access: abstract_only; cited as: H1-05 [29]; the published full text was not obtained (listed under Sources not obtained)}
}
@article{galandStrongLinkMarine2018,
  author = {Galand, Pierre E. and Pereira, Olivier and Hochart, Corentin and Auguet, Jean Christophe and Debroas, Didier},
  title = {A strong link between marine microbial community composition and function challenges the idea of functional redundancy},
  journal = {The ISME Journal},
  year = {2018},
  volume = {12},
  number = {10},
  pages = {2470--2478},
  doi = {10.1038/s41396-018-0158-1},
  note = {access: full_text (via search agents); cited as: H1-05 [31]}
}
@article{loucaDecouplingFunctionTaxonomy2016,
  author = {Louca, Stilianos and Parfrey, Laura Wegener and Doebeli, Michael},
  title = {Decoupling function and taxonomy in the global ocean microbiome},
  journal = {Science},
  year = {2016},
  volume = {353},
  number = {6305},
  pages = {1272--1277},
  doi = {10.1126/science.aaf4507},
  note = {access: abstract_only; cited as: H1-05 [32]; full text not obtained (listed under Sources not obtained)}
}
@article{loucaHighTaxonomicVariability2016,
  author = {Louca, Stilianos and Jacques, Saulo M. S. and Pires, Aliny P. F. and Leal, Juliana S. and Srivastava, Diane S. and Parfrey, Laura Wegener and Farjalla, Vinicius F. and Doebeli, Michael},
  title = {High taxonomic variability despite stable functional structure across microbial communities},
  journal = {Nature Ecology & Evolution},
  year = {2017},
  volume = {1},
  number = {1},
  pages = {1--12},
  doi = {10.1038/s41559-016-0015},
  note = {access: abstract_only; cited as: H1-05 [33]; online 5 December 2016; pages corrected to Crossref's 1-12 (critic: H1-05:C-074..076; the note gave the article number 0015); full text not obtained (listed under Sources not obtained)}
}
@article{loucaFunctionFunctionalRedundancy2018,
  author = {Louca, Stilianos and Polz, Martin F. and Mazel, Florent and Albright, Michaeline B. N. and Huber, Julie A. and O'Connor, Mary I. and Ackermann, Martin and Hahn, Aria S. and Srivastava, Diane S. and Crowe, Sean A. and Doebeli, Michael and Parfrey, Laura Wegener},
  title = {Function and functional redundancy in microbial systems},
  journal = {Nature Ecology & Evolution},
  year = {2018},
  volume = {2},
  number = {6},
  pages = {936--943},
  doi = {10.1038/s41559-018-0519-1},
  note = {access: abstract_only; cited as: H1-05 [34]; full text not obtained (listed under Sources not obtained)}
}
@article{burkeBacterialCommunityAssembly2011,
  author = {Burke, Catherine and Steinberg, Peter and Rusch, Doug and Kjelleberg, Staffan and Thomas, Torsten},
  title = {Bacterial community assembly based on functional genes rather than species},
  journal = {Proceedings of the National Academy of Sciences},
  year = {2011},
  volume = {108},
  number = {34},
  pages = {14288--14293},
  doi = {10.1073/pnas.1101591108},
  note = {access: secondary (critic: H1-05:C-047, C-048, a fetch summary is not a full-text reading, so secondary or abstract-level unless the text was read; the note said FT via fetch summary); cited as: H1-05 [35]}
}
@article{vanderloosLowFunctionalChange2025,
  author = {van der Loos, Luna M. and Steinhagen, Sophie and Stock, Willem and Weinberger, Florian and D'hondt, Sofie and Willems, Anne and De Clerck, Olivier},
  title = {Low functional change despite high taxonomic turnover characterizes the Ulva microbiome across a 2000-km salinity gradient},
  journal = {Science Advances},
  year = {2025},
  volume = {11},
  number = {3},
  pages = {eadr6070},
  doi = {10.1126/sciadv.adr6070},
  note = {access: full_text (rechecked by the reviewer); cited as: H1-05 [36]}
}
@article{soufiTaxonomicVariabilityFunctional2024,
  author = {Soufi, Hengameh H. and Porch, Robert and Korchagina, Masha V. and Abrams, Joseph A. and Schnider, Jared S. and Carr, Ben D. and Williams, Mark A. and Louca, Stilianos},
  title = {Taxonomic variability and functional stability across Oregon coastal subsurface microbiomes},
  journal = {Communications Biology},
  year = {2024},
  volume = {7},
  number = {1},
  pages = {1663},
  doi = {10.1038/s42003-024-07384-y},
  note = {access: full_text (via search agents); cited as: H1-05 [37]}
}
@article{lemoigneLinkingStochasticAssembly2026,
  author = {Le Moigne, Alizée and Andrei, Adrian-Ştefan and Pernthaler, Jakob},
  title = {Linking stochastic assembly to functional potential, redundancy, and trait patterns in bacterial communities},
  journal = {Microbiome},
  year = {2026},
  volume = {14},
  number = {1},
  pages = {201},
  doi = {10.1186/s40168-026-02442-5},
  note = {access: full_text (via one agent), abstract_only (via the other); cited as: H1-05 [38]}
}
@article{santillanPressDisturbanceAlters2020,
  author = {Santillan, Ezequiel and Constancias, Florentin and Wuertz, Stefan},
  title = {Press disturbance alters community structure and assembly mechanisms of bacterial taxa and functional genes in mesocosm-scale bioreactors},
  journal = {mSystems},
  year = {2020},
  volume = {5},
  number = {4},
  pages = {e00471--20},
  doi = {10.1128/mSystems.00471-20},
  note = {access: abstract_only; a preprint version (bioRxiv doi:10.1101/805788, abstract only) is a separate entry; cited as: H1-05 [39]}
}
@article{tianDecipheringFunctionalRedundancy2020,
  author = {Tian, Liang and Wang, Xu-Wen and Wu, Ang-Kun and Fan, Yuhang and Friedman, Jonathan and Dahlin, Amber and Waldor, Matthew K. and Weinstock, George M. and Weiss, Scott T. and Liu, Yang-Yu},
  title = {Deciphering functional redundancy in the human microbiome},
  journal = {Nature Communications},
  year = {2020},
  volume = {11},
  number = {1},
  pages = {6217},
  doi = {10.1038/s41467-020-19940-1},
  note = {access: full_text (via search agents); cited as: H1-05 [40]}
}
@article{liRevealingProteomelevelFunctional2023,
  author = {Li, Leyuan and Wang, Tong and Ning, Zhibin and Zhang, Xu and Butcher, James and Serrana, Joeselle M. and Simopoulos, Caitlin M. A. and Mayne, Janice and Stintzi, Alain and Mack, David R. and Liu, Yang-Yu and Figeys, Daniel},
  title = {Revealing proteome-level functional redundancy in the human gut microbiome using ultra-deep metaproteomics},
  journal = {Nature Communications},
  year = {2023},
  volume = {14},
  number = {1},
  pages = {3428},
  doi = {10.1038/s41467-023-39149-2},
  note = {access: full_text (via search agents); cited as: H1-05 [41]}
}
@article{goldfordEmergentSimplicityMicrobial2018,
  author = {Goldford, Joshua E. and Lu, Nanxi and Bajić, Djordje and Estrela, Sylvie and Tikhonov, Mikhail and Sanchez-Gorostiaga, Alicia and Segrè, Daniel and Mehta, Pankaj and Sanchez, Alvaro},
  title = {Emergent simplicity in microbial community assembly},
  journal = {Science},
  year = {2018},
  volume = {361},
  number = {6401},
  pages = {469--474},
  doi = {10.1126/science.aat1168},
  note = {access: abstract_only; cited as: H1-05 [42]}
}
@article{estrelaFunctionalAttractorsMicrobial2022,
  author = {Estrela, Sylvie and Vila, Jean C.C. and Lu, Nanxi and Bajić, Djordje and Rebolleda-Gómez, Maria and Chang, Chang-Yu and Goldford, Joshua E. and Sanchez-Gorostiaga, Alicia and Sánchez, Álvaro},
  title = {Functional attractors in microbial community assembly},
  journal = {Cell Systems},
  year = {2022},
  volume = {13},
  number = {1},
  pages = {29--42.e7},
  doi = {10.1016/j.cels.2021.09.011},
  note = {access: abstract_only; cited as: H1-05 [43]; listed only in the D3 answer's access line, not cited for any finding (not cited)}
}
@article{jourdainEnvironmentalSelectionConstrains2026,
  author = {Jourdain, Lisa and Leininger, Aaron and Pacheco, Alan R and Gu, Wenyu},
  title = {Environmental selection constrains metabolic network architecture despite taxonomic turnover in anaerobic digestion communities},
  journal = {The ISME Journal},
  year = {2026},
  volume = {20},
  number = {1},
  pages = {wrag145},
  doi = {10.1093/ismejo/wrag145},
  note = {access: abstract_only; cited as: H1-05 [44]}
}
@article{airaFasterTurnoverTaxonomic2026,
  author = {Aira, Manuel and Pérez-Losada, Marcos and Crandall, Keith A. and Domínguez, Jorge},
  title = {Faster turnover of taxonomic over functional bacterial composition during vermicomposting indicates increasing functional redundancy},
  journal = {PLOS One},
  year = {2026},
  volume = {21},
  number = {7},
  pages = {e0354276},
  doi = {10.1371/journal.pone.0354276},
  note = {access: full_text (via search agents); cited as: H1-05 [45]}
}
@article{renComparisonMicrobialTaxonomic2016,
  author = {Ren, Youhua and Niu, Jiaojiao and Huang, Wenkun and Peng, Deliang and Xiao, Yunhua and Zhang, Xian and Liang, Yili and Liu, Xueduan and Yin, Huaqun},
  title = {Comparison of microbial taxonomic and functional shift pattern along contamination gradient},
  journal = {BMC Microbiology},
  year = {2016},
  volume = {16},
  number = {1},
  pages = {110},
  doi = {10.1186/s12866-016-0731-6},
  note = {access: abstract_only; cited as: H1-05 [46]}
}
@article{nayfachAverageGenomeSize2015,
  author = {Nayfach, Stephen and Pollard, Katherine S},
  title = {Average genome size estimation improves comparative metagenomics and sheds light on the functional ecology of the human microbiome},
  journal = {Genome Biology},
  year = {2015},
  volume = {16},
  number = {1},
  pages = {51},
  doi = {10.1186/s13059-015-0611-7},
  note = {access: abstract_only; cited as: H1-05 [47]}
}
@article{gracorozaDistanceDecay22022,
  author = {Graco-Roza, Caio and Aarnio, Sonja and Abrego, Nerea and Acosta, Alicia T. R. and Alahuhta, Janne and Altman, Jan and Angiolini, Claudia and Aroviita, Jukka and Attorre, Fabio and Baastrup-Spohr, Lars and Barrera-Alba, José J. and Belmaker, Jonathan and Biurrun, Idoia and Bonari, Gianmaria and Bruelheide, Helge and Burrascano, Sabina and Carboni, Marta and Cardoso, Pedro and Carvalho, José C. and Castaldelli, Giuseppe and Christensen, Morten and Correa, Gilsineia and Dembicz, Iwona and Dengler, Jürgen and Dolezal, Jiri and Domingos, Patricia and Erös, Tibor and Ferreira, Carlos E. L. and Filibeck, Goffredo and Floeter, Sergio R. and Friedlander, Alan M. and Gammal, Johanna and Gavioli, Anna and Gossner, Martin M. and Granot, Itai and Guarino, Riccardo and Gustafsson, Camilla and Hayden, Brian and He, Siwen and Heilmann-Clausen, Jacob and Heino, Jani and Hunter, John T. and Huszar, Vera L. M. and Janišová, Monika and Jyrkänkallio-Mikkola, Jenny and Kahilainen, Kimmo K. and Kemppinen, Julia and Kozub, Łukasz and Kruk, Carla and Kulbiki, Michel and Kuzemko, Anna and le Roux, Peter Christiaan and Lehikoinen, Aleksi and de Lima, Domênica Teixeira and Lopez-Urrutia, Angel and Lukács, Balázs A. and Luoto, Miska and Mammola, Stefano and Marinho, Marcelo M. and Menezes, Luciana S. and Milardi, Marco and Miranda, Marcela and Moser, Gleyci A. O. and Mueller, Joerg and Niittynen, Pekka and Norkko, Alf and Nowak, Arkadiusz and Ometto, Jean P. and Ovaskainen, Otso and Overbeck, Gerhard E. and Pacheco, Felipe S. and Pajunen, Virpi and Palpurina, Salza and Picazo, Félix and Campos, Juan Antonio and Rodil, Iván F. and Sabatini, Francesco M. and Salingré, Shira and De Sanctis, Michele and Segura, Angel M. and da Silva, Lucia H. S. and Stevanovic, Zora D. and Swacha, Grzegorz and Teittinen, Anette and Tolonen, Kimmo T. and Tsiripidis, Ioannis and Virta, Leena and Wang, Beixin and Wang, Jianjun and Weisser, Wolfgang and Xu, Yuan and Soininen, Janne},
  title = {Distance decay 2.0: A global synthesis of taxonomic and functional turnover in ecological communities},
  journal = {Global Ecology and Biogeography},
  year = {2022},
  volume = {31},
  number = {7},
  pages = {1399--1421},
  doi = {10.1111/geb.13513},
  note = {access: full_text (via search agents); cited as: H1-05 [48]; openly available as PMC9322010 (critic: H1-05:C-055); the note says the published title separates '2.0' and 'A' with a dash; 92 authors match Crossref (critic: H1-05:C-077..079)}
}
@article{swensonDeterministicTropicalTree2010,
  author = {Swenson, Nathan G. and Anglada-Cordero, Pedro and Barone, John A.},
  title = {Deterministic tropical tree community turnover: evidence from patterns of functional beta diversity along an elevational gradient},
  journal = {Proceedings of the Royal Society B: Biological Sciences},
  year = {2011},
  volume = {278},
  number = {1707},
  pages = {877--884},
  doi = {10.1098/rspb.2010.1369},
  note = {access: secondary (critic: H1-05:C-047, C-048, a fetch summary is not a full-text reading, so secondary or abstract-level unless the text was read; the note said FT via fetch summary); cited as: H1-05 [49]}
}
@article{villegerDecomposingFunctionalDiversity2013,
  author = {Villéger, Sébastien and Grenouillet, Gaël and Brosse, Sébastien},
  title = {Decomposing functional β-diversity reveals that low functional β-diversity is driven by low functional turnover in European fish assemblages},
  journal = {Global Ecology and Biogeography},
  year = {2013},
  volume = {22},
  number = {6},
  pages = {671--681},
  doi = {10.1111/geb.12021},
  note = {access: abstract_only; cited as: H1-05 [50]; full text not obtained (listed under Sources not obtained; a Zenodo copy listed but not fetched)}
}
@article{villegerFunctionalHomogenizationExceeds2014,
  author = {Villéger, Sébastien and Grenouillet, Gaël and Brosse, Sébastien},
  title = {Functional homogenization exceeds taxonomic homogenization among European fish assemblages},
  journal = {Global Ecology and Biogeography},
  year = {2014},
  volume = {23},
  number = {12},
  pages = {1450--1460},
  doi = {10.1111/geb.12226},
  note = {access: abstract_only; cited as: H1-05 [51]}
}
@article{barnettDisturbanceIncreasesSoil2025,
  author = {Barnett, Samuel E. and Shade, Ashley},
  title = {Disturbance increases soil microbiome functional redundancy but decreases capacity for insurance via winnowed environmental responsiveness},
  journal = {bioRxiv},
  year = {2025},
  doi = {10.1101/2025.09.19.677300},
  note = {access: secondary (critic: H1-05:C-047, C-048, a fetch summary is not a full-text reading, so secondary or abstract-level unless the text was read; the note said FT via fetch summary); type: preprint, no published version found; cited as: H1-05 [8]; incomplete: volume, pages}
}
@article{hollandmoritzEcologicalPerspectiveMicrobial2021,
  author = {Holland-Moritz, Hannah and Vanni, Chiara and Fernandez-Guerra, Antonio and Bissett, Andrew and Fierer, Noah},
  title = {An ecological perspective on microbial genes of unknown function in soil},
  journal = {bioRxiv},
  year = {2021},
  doi = {10.1101/2021.12.02.470747},
  note = {access: abstract_only; type: preprint, no published version found; cited as: H1-05 [27]; the note's caveat that the given names are unverified because the DOI is not in Crossref is unnecessary: Crossref has the record with all five authors (critic: H1-05:C-056..058, C-073); incomplete: volume, pages}
}
@article{hoChallengesQuantifyingFunctional2024,
  author = {Ho, Po-Yi and Huang, Kerwyn Casey},
  title = {Challenges in quantifying functional redundancy and selection in microbial communities},
  journal = {bioRxiv},
  year = {2024},
  doi = {10.1101/2024.03.26.586891},
  note = {access: secondary (critic: H1-05:C-047, C-048, a fetch summary is not a full-text reading, so secondary or abstract-level unless the text was read; the note said FT via fetch summary; the critic retrieved the open bioRxiv full text, C-049); type: preprint v1, published as Cell Systems 2025; cited as: H1-05 [30]; incomplete: volume, pages}
}
@article{santillanPressDisturbanceAlters2019,
  author = {Santillan, Ezequiel and Constancias, Florentin and Wuertz, Stefan},
  title = {Press disturbance alters community structure and assembly mechanisms of bacterial taxa and functional genes in mesocosm-scale bioreactors},
  journal = {bioRxiv},
  year = {2019},
  doi = {10.1101/805788},
  note = {access: abstract_only; type: preprint of the mSystems 2020 paper, named in the same reference; cited as: H1-05 [39]; the note gives no title for the preprint, title and authors transcribed from the published version in the same reference; incomplete: title (as published in the preprint), volume, pages}
}
@article{ramirezflandesRedoxTraitsCharacterize2019,
  author = {Ramírez-Flandes, Salvador and González, Bernardo and Ulloa, Osvaldo},
  title = {Redox traits characterize the organization of global microbial communities},
  journal = {Proceedings of the National Academy of Sciences USA},
  year = {2019},
  volume = {116},
  number = {9},
  pages = {3630--3635},
  doi = {10.1073/pnas.1817554116},
  note = {access: not_obtained (known only as described in Chen et al. 2022, secondary); names and accents corrected and the DOI confirmed (critic: H1-05:C-065); listed under Sources not obtained; not cited}
}
@article{bahramStructureFunctionGlobal2018,
  author = {Bahram, Mohammad and Hildebrand, Falk and Forslund, S. K. and others},
  title = {Structure and function of the global topsoil microbiome},
  journal = {Nature},
  year = {2018},
  volume = {560},
  number = {7717},
  pages = {233--237},
  doi = {10.1038/s41586-018-0386-6},
  note = {access: not_obtained (Europe PMC abstract obtained; no PMC full text; publisher not tried); listed twice under Sources not obtained; first author's given name corrected to Mohammad (critic: H1-05:C-064, the note had Mayra; 21 authors, last author Peer Bork); not cited; incomplete: author}
}
@article{fiererReconstructingMicrobialDiversity2013,
  author = {Fierer, N. and Ladau, J. and Clemente, J. C. and Leff, J. W. and Owens, S. M. and Pollard, K. S. and Knight, R. and Gilbert, J. A. and McCulley, R. L.},
  title = {Reconstructing the microbial diversity and function of pre-agricultural tallgrass prairie soils in the United States},
  journal = {Science},
  year = {2013},
  volume = {342},
  number = {6158},
  pages = {621--624},
  doi = {10.1126/science.1243768},
  note = {access: not_obtained (Europe PMC abstract only; no PMC copy); listed twice under Sources not obtained, once with et al. only (critic: H1-05:C-066..069, an incomplete reference; Crossref lists 9 authors); not cited}
}
@article{jiaNewPerspectiveFunctional2020,
  author = {Jia, Yu and Whalen, Joann K.},
  title = {A new perspective on functional redundancy and phylogenetic niche conservatism in soil microbial communities},
  journal = {Pedosphere},
  year = {2020},
  volume = {30},
  number = {1},
  pages = {18--24},
  doi = {10.1016/S1002-0160(19)60826-X},
  note = {access: not_obtained (Crossref metadata only; not in Europe PMC; no open copy found); listed twice under Sources not obtained; names match Crossref in substance (critic: H1-05:C-070..072); not cited}
}
@article{andersonDistancebasedTestsHomogeneity2006,
  author = {Anderson, Marti J.},
  title = {Distance-Based Tests for Homogeneity of Multivariate Dispersions},
  journal = {Biometrics},
  year = {2006},
  volume = {62},
  number = {1},
  pages = {245--253},
  doi = {10.1111/j.1541-0420.2005.00440.x},
  note = {background; checked on Crossref and the Europe PMC abstract}
}
```
