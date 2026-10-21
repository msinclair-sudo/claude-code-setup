---
type: knowledge
title: Functional and taxonomic turnover in soil microbial communities
inputs:
  - H1-05: PhD/Proposal/Research/Results/Functional versus taxonomic turnover in soil microbial communities comparisons, dependence on functional unit and metric, and what null models conclude.md
refs: PhD/Proposal/Refs/Refs.bib
built: 2026-10-22
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

### turnover: functional and taxonomic turnover
needs: none
- **turnover.1** In the review, turnover means between-sample dissimilarity.
  conf: not stated · class: not stated · holds: the review's working definition, used throughout · src: none (the review's definition) · trail: H1-05 §Functional versus taxonomic turnover · from: H1-05:B-0029

### functional-profile: what "function" means in the soil literature
needs: none
- **functional-profile.1** "Function" in the soil literature means several different things: shotgun reads annotated to SEED, KEGG or eggNOG; GeoChip probe arrays; gene-family counts from assemblies or MAGs; profiles inferred from 16S (PICRUSt, FAPROTAX); and, in two cases, measured enzyme activity or protein.
  conf: not stated · class: not stated · holds: the soil studies the review covers; the review keeps these kinds apart · src: none (the reviewer's description of the literature) · trail: H1-05 §Functional versus taxonomic turnover · from: H1-05:B-0030

### platform: GeoChip and shotgun platforms
needs: functional-profile
- **platform.1** GeoChip probes a few thousand preselected known genes, whose detection depends on hybridisation thresholds, and its functional profiles are set against 16S taxonomy measured on a different platform.
  conf: not stated · class: not stated · holds: GeoChip studies in the review ([5], [6], [15]) · src: none (the reviewer's and the critic's description of the platform) · trail: H1-05 §2, §Adversarial critique · from: H1-05:A-046, H1-05:B-0106, H1-05:C-096
- **platform.2** Shotgun annotation typically covers a minority of reads: 13 to 23% of reads were annotatable in [1].
  conf: not stated · class: not stated · holds: the reads of [1]; "typically" is the review's generalisation · src: fiererCrossbiomeMetagenomicAnalyses2012 · trail: H1-05 §1.1, §answers · from: H1-05:A-046, H1-05:B-0035, H1-05:C-125
- **platform.3** No study was found that ran GeoChip and shotgun sequencing on the same soils for the functional-taxonomic comparison.
  conf: not stated · class: search (note: "I found no study that ran both on the same soils") · holds: the review's searches · src: none (a search result) · trail: H1-05 §2 · from: H1-05:B-0108

### covariation: covariation of functional and taxonomic dissimilarity
needs: turnover, functional-profile
- **covariation.1** Positive covariation of functional and taxonomic dissimilarity is shown in three soil datasets at strong contrasts [1][2][3]; the three are not independent in lineage, because [1] and [2] come from one group and [3] pools MG-RAST submissions that may include [1].
  conf: not stated · class: not stated · holds: DNA-measured functional profiles; strong cross-biome or between-site contrasts (Mantel r 0.76 to 0.82 across 16 soils [1]; rho 0.87 across 6 NutNet sites [2]; r2 0.28 across 845 pooled metagenomes [3]); covariation is shown mainly at strong contrasts · src: fiererCrossbiomeMetagenomicAnalyses2012, leffConsistentResponsesSoil2015, chenFunctionalRedundancySoil2022 · trail: H1-05 §critic, §answers, §1.1 · from: H1-05:C-001, H1-05:C-002, H1-05:A-002, H1-05:A-005, H1-05:A-006, H1-05:A-016, H1-05:B-0034 · rating: "Moderate for covariation at strong contrasts"
- **covariation.2** Across 16 soils from cold desert, hot desert, forest, grassland and tundra, Bray-Curtis dissimilarity of MG-RAST/SEED gene profiles correlated with 16S Bray-Curtis (Mantel r = 0.76) and with unweighted UniFrac (r = 0.82).
  conf: not stated · class: meas (marker) · holds: 16 soils; only 13 to 23% of reads annotatable; desert and non-desert samples separated almost completely (ANOSIM R about 0.97 to 0.98) · src: fiererCrossbiomeMetagenomicAnalyses2012 (FT, figures confirmed by the critic via PMC; measured; critic: H1-05:C-052, H1-05:C-053 was "FT, via search agents; measured") · trail: H1-05 §1.1, §Adversarial critique · from: H1-05:I-0001, H1-05:B-0035, H1-05:C-052, H1-05:C-053
- **covariation.3** In the reviewer's reading, not the authors', a single dominant desert/non-desert split drives both matrices in [1], so the correlation may say more about that split than about fine-scale coupling.
  conf: not stated · class: reading (note: "My reading, not the authors'") · holds: the 16 soils of [1], dominated by a desert/non-desert split · src: fiererCrossbiomeMetagenomicAnalyses2012 · trail: H1-05 §1.1 · from: H1-05:B-0036, H1-05:A-016
- **covariation.4** The authors of [1] made a caveat for alpha diversity parallel to the reviewer's reading: the correlations were not significant without the cold-desert soils.
  conf: not stated · class: not stated · holds: alpha diversity in [1]; reported by the critic · src: fiererCrossbiomeMetagenomicAnalyses2012 · trail: H1-05 §Adversarial critique · from: H1-05:C-054
- **covariation.5** Across six NutNet grassland sites, functional-gene and bacterial dissimilarity correlated with rho = 0.87, mostly between sites.
  conf: not stated · class: not stated · holds: six NutNet grassland sites [2] · src: leffConsistentResponsesSoil2015 · trail: H1-05 §1.1 · from: H1-05:B-0037
- **covariation.6** Across the six NutNet grassland sites, within-site N and P additions shifted both functional genes and bacteria.
  conf: not stated · class: meas (marker) · holds: within-site N and P additions [2] · src: leffConsistentResponsesSoil2015 (FT, measured) · trail: H1-05 §1.1 · from: H1-05:I-0002, H1-05:B-0037
- **covariation.7** In 845 pooled public soil metagenomes, pairwise functional and taxonomic Bray-Curtis similarities correlated (r2 = 0.2831, over 356,090 pairs).
  conf: not stated · class: meas (marker) · holds: 845 MG-RAST soil metagenomes pooled across studies [3] · src: chenFunctionalRedundancySoil2022 (FT, rechecked by this reviewer; measured) · trail: H1-05 §1.1, §critic · from: H1-05:I-0003, H1-05:C-001
- **covariation.8** At one site under coal-fire heating, metagenome and amplicon ordinations were concordant (Procrustes 0.802, m2 = 0.357).
  conf: not stated · class: not stated · holds: one coal-fire site [8], a preprint · src: barnettDisturbanceIncreasesSoil2025 (secondary or abstract-level; preprint; critic: H1-05:C-047, H1-05:C-048 was "FT via fetch summary; preprint") · trail: H1-05 §1.1 · from: H1-05:B-0038, H1-05:C-047, H1-05:C-048
- **covariation.9** The three covariation datasets all use Bray-Curtis on annotated profiles and correlation-type tests, and none used a null model.
  conf: not stated · class: not stated · holds: [1], [2], [3] · src: fiererCrossbiomeMetagenomicAnalyses2012, leffConsistentResponsesSoil2015, chenFunctionalRedundancySoil2022 · trail: H1-05 §1.1 · from: H1-05:B-0039, H1-05:B-0040
- **covariation.10** In soil, [22] finds that function tracks taxonomy under both contrast sizes, while [7] finds that taxonomic dissimilarity explains almost none of functional variation along a latitudinal gradient.
  conf: cont (note: "Conflicts") · class: not stated · holds: a single-site precipitation experiment [22]; a latitudinal gradient [7] · src: xuDistinctivePatternMechanism2022, zhangSoilBacterialEndemism2016 · trail: H1-05 §answers, §1.4 · from: H1-05:A-022, H1-05:A-023, H1-05:I-0008
- **covariation.11** In the precipitation experiment, gene, protein and enzyme dissimilarities were Mantel-correlated with taxonomic dissimilarity.
  conf: not stated · class: not stated · holds: a single-site precipitation experiment [22] · src: xuDistinctivePatternMechanism2022 · trail: H1-05 §1.4 · from: H1-05:B-0068, H1-05:I-0008

### ordering: which turnover is larger, functional or taxonomic
needs: turnover, functional-profile, covariation, platform
- **ordering.bg1** Anderson's non-parametric multivariate analysis of variance (PERMANOVA) tests for differences among groups from any symmetric distance or dissimilarity matrix, with P-values obtained by permutation.
  kind: background · ref: andersonNewMethodNonparametric2001 · check: DOI 10.1111/j.1442-9993.2001.01070.pp.x resolves on Crossref; stated in the abstract ("calculated directly from any symmetric distance or dissimilarity matrix"; "P-values are then obtained using permutations")
- **ordering.1** Covariation says nothing about which turnover is larger: a correlation between dissimilarity matrices says nothing about their relative magnitudes, so covariation and "function less variable" are compatible.
  conf: not stated · class: not stated · holds: the critic's and the reviewer's reasoning about correlation-type tests · src: none (the critic's and the reviewer's reasoning) · trail: H1-05 §critic, §5 · from: H1-05:C-003, H1-05:B-0146
- **ordering.2** [3] and [8] each report both covariation and "function less variable" in one dataset; in [8], stable functional similarity sits alongside a metagenome-amplicon Procrustes correlation of 0.80.
  conf: not stated · class: not stated · holds: [3]; [8] · src: chenFunctionalRedundancySoil2022, barnettDisturbanceIncreasesSoil2025 (secondary or abstract-level; critic: H1-05:C-047, H1-05:C-048 was "FT via fetch summary") · trail: H1-05 §5, §answers · from: H1-05:B-0146, H1-05:B-0147, H1-05:A-024, H1-05:C-047, H1-05:C-048
- **ordering.3** In the one large soil magnitude comparison, functional Bray-Curtis similarity ranged 44 to 99% and taxonomic 9 to 100% (paired t = 67.5): functional similarity was higher than taxonomic, at a strong (global) contrast.
  conf: single (note: "SINGLE SOURCE for this sample size") · class: not stated · holds: 845 pooled MG-RAST soil metagenomes; the profiles pool assembled and unassembled submissions from many studies; SEED level 3 (1,135 functions) is compared with RefSeq genus (1,113 taxa); nothing tests whether a lower functional dissimilarity is expected from aggregation alone; removing it would remove the only large-sample soil evidence on the same samples and metric · src: chenFunctionalRedundancySoil2022 (FT, rechecked) · trail: H1-05 §1.2, §critic, §answers · from: H1-05:B-0041, H1-05:B-0042, H1-05:B-0045, H1-05:B-0046, H1-05:A-007, H1-05:A-008, H1-05:A-019, H1-05:A-032, H1-05:C-004
- **ordering.4** In [3], climate plus soil explained 16.3% of taxonomic and 13.5% of functional variation (DistLM).
  conf: not stated · class: not stated · holds: [3] · src: chenFunctionalRedundancySoil2022 (FT, rechecked) · trail: H1-05 §1.2 · from: H1-05:B-0043
- **ordering.5** At serpentine vs non-serpentine site pairs, bacterial composition differed (PERMANOVA R2 = 0.061, P = 0.004) while eggNOG functional composition did not (R2 = 0.027, P = 0.391).
  conf: not stated · class: meas (marker) · holds: serpentine and non-serpentine soil pairs [4]; a significant taxonomic shift set against a non-significant functional one · src: igweRedundancyMaintainsMicrobial2026 (FT, rechecked; measured) · trail: H1-05 §1.2, §answers · from: H1-05:I-0004, H1-05:A-008
- **ordering.6** In the reviewer's reading of the serpentine study, the result sets a significant test against a non-significant one, on datasets of different size after QC; site pairs explained about 56% of variation in both functional (non-significant, F(19,16)) and bacterial (significant) composition, which suggests limited power on the functional side rather than an absence of structure.
  conf: not stated · class: reading (note: "My reading") · holds: [4]; the functional dataset is smaller · src: igweRedundancyMaintainsMicrobial2026 · trail: H1-05 §1.2, §answers · from: H1-05:B-0049, H1-05:B-0050, H1-05:A-020, H1-05:C-128
- **ordering.7** Single-site "function lower" results [4][13][14][18][24] mostly set a significant test against a non-significant one.
  conf: not stated · class: not stated · holds: single-site soil studies; the critic's reading of them · src: igweRedundancyMaintainsMicrobial2026, panImpactLongtermN2014, yangDecouplingMicrobialCommunity2021, souzaMetagenomicAnalysisReveals2015, saumasanchezFunctionalRedundancyBuffers2024 · trail: H1-05 §critic · from: H1-05:C-006
- **ordering.8** Along a latitudinal forest gradient in China, bacterial Bray-Curtis showed strong distance decay, while GeoChip function, summarised as DCA axes rather than pairwise dissimilarity, was "highly convergent"; the two turnovers are not on a common basis.
  conf: not stated · class: not stated · holds: a latitudinal forest gradient in China [7]; GeoChip · src: zhangSoilBacterialEndemism2016 (FT via agents) · trail: H1-05 §1.2 · from: H1-05:B-0051, H1-05:B-0052
- **ordering.9** Under coal-fire disturbance, OTU similarity to reference rose as soils cooled, while KO similarity stayed high throughout.
  conf: not stated · class: not stated · holds: coal-fire disturbance [8] · src: barnettDisturbanceIncreasesSoil2025 (secondary or abstract-level; critic: H1-05:C-047, H1-05:C-048 was "FT via fetch summary") · trail: H1-05 §1.2, §answers · from: H1-05:B-0053, H1-05:A-008, H1-05:C-047, H1-05:C-048
- **ordering.10** In [8], MAG-based redundancy rose with disturbance, which the authors attribute to lower diversity and smaller genomes.
  conf: not stated · class: not stated · holds: [8], a preprint · src: barnettDisturbanceIncreasesSoil2025 (secondary or abstract-level; preprint, no published version found; critic: H1-05:C-047, H1-05:C-048 was "FT via fetch summary; preprint, no published version found") · trail: H1-05 §1.2 · from: H1-05:B-0054, H1-05:C-047, H1-05:C-048
- **ordering.11** After 54 years of fertilization there was no effect on functional profiles despite taxonomic shifts.
  conf: not stated · class: not stated · holds: 54 years of fertilizer [13]; abstract only · src: panImpactLongtermN2014 (AB) · trail: H1-05 §1.2 · from: H1-05:B-0055
- **ordering.12** Functional potential stayed stable across a 1 to 30 C peat incubation while taxonomy changed.
  conf: not stated · class: not stated · holds: a 1 to 30 C peat incubation [14]; abstract only · src: yangDecouplingMicrobialCommunity2021 (AB) · trail: H1-05 §1.2 · from: H1-05:B-0055
- **ordering.13** Under tillage and rotation, taxonomic differences were "far greater" than SEED functional differences, with the two measured in different papers.
  conf: not stated · class: not stated · holds: one soil under tillage and crop-management regimes [18]; abstract only · src: souzaMetagenomicAnalysisReveals2015 (AB) · trail: H1-05 §1.2 · from: H1-05:B-0055
- **ordering.14** Arid and hyperarid saline drylands had similar functional capacities despite structural differences.
  conf: not stated · class: not stated · holds: arid and hyperarid saline drylands [24]; only the abstract and methods were closely read · src: saumasanchezFunctionalRedundancyBuffers2024 (abstract-level; critic: H1-05:C-051 was "FT via agents, abstract and methods only closely read") · trail: H1-05 §1.2, §Adversarial critique · from: H1-05:B-0055, H1-05:C-051
- **ordering.15** With high Hg, C and N genes changed little, while predicted-gene beta diversity shifted significantly.
  conf: not stated · class: not stated · holds: high Hg [16]; abstract only · src: freyLongtermMercuryContamination2022 (AB) · trail: H1-05 §1.2 · from: H1-05:B-0055
- **ordering.16** After aromatic pollution in a microcosm, taxonomic diversity fell and gene-pool diversity rose (alpha, not turnover).
  conf: not stated · class: not stated · holds: a soil microcosm [17]; alpha diversity; abstract only · src: katoTimeseriesMetagenomicAnalysis2015 (AB) · trail: H1-05 §1.2 · from: H1-05:B-0055
- **ordering.17** After 14 years of moderate warming (0.8 to 2.0 C), 16S composition did not differ, while GeoChip functional-gene composition did (Adonis, ANOSIM, MRPP, P < 0.05), with n = 4 per treatment.
  conf: not stated · class: meas (marker) · holds: 14 years of moderate warming [5]; GeoChip against 16S; n = 4 per treatment · src: gaoLongtermWarmingMediterraneantype2021 (FT, rechecked; measured) · trail: H1-05 §1.3, §answers · from: H1-05:I-0007, H1-05:A-009
- **ordering.18** The authors of the warming study conclude that functional potential is more sensitive than taxonomy.
  conf: not stated · class: not stated · holds: [5] · src: gaoLongtermWarmingMediterraneantype2021 · trail: H1-05 §1.3 · from: H1-05:B-0059
- **ordering.19** In the warming study, plant and abiotic variables were unchanged, so the contrast was weak.
  conf: not stated · class: not stated · holds: [5] · src: gaoLongtermWarmingMediterraneantype2021 · trail: H1-05 §1.3 · from: H1-05:B-0060
- **ordering.20** The power-asymmetry critique made against the serpentine study (a significant vs a non-significant test, differences in n) applies to the warming study too (n = 4, significant functional vs non-significant taxonomic), and the review does not apply to the "function higher" GeoChip results [5][15] the caution it applies to "function lower" studies for lacking an averaging null.
  conf: not stated · class: not stated · holds: [4], [5], [15]; the critic's finding on the review's handling · src: igweRedundancyMaintainsMicrobial2026, gaoLongtermWarmingMediterraneantype2021, maDivergentTaxonomicFunctional2017 · trail: H1-05 §Adversarial critique · from: H1-05:C-095, H1-05:C-097
- **ordering.21** Under aeolian erosion and deposition, soil nutrients correlated with functional but not with taxonomic structure (Mantel).
  conf: not stated · class: not stated · holds: aeolian erosion and deposition [15]; GeoChip; abstract only · src: maDivergentTaxonomicFunctional2017 (AB) · trail: H1-05 §1.3, §answers · from: H1-05:B-0061, H1-05:A-009
- **ordering.22** On the Changbai elevation gradient, functional-gene distance decay (r = 0.708) was stronger than bacterial (r = 0.409), in the reviewer's reading; the two r values come from different platforms (16S vs GeoChip) and are not on a common scale.
  conf: not stated · class: reading (note: "This is my reading") · holds: Changbai Mountain elevation gradient [6] · src: shenDramaticIncreasesSoil2016 (FT via agents) · trail: H1-05 §1.3, §answers · from: H1-05:B-0062, H1-05:B-0063, H1-05:B-0065, H1-05:A-009
- **ordering.23** The authors of the Changbai study describe the functional and bacterial patterns as similar, with different drivers (pH for taxa, DOC for genes).
  conf: not stated · class: not stated · holds: [6] · src: shenDramaticIncreasesSoil2016 · trail: H1-05 §1.3 · from: H1-05:B-0064
- **ordering.24** The reverse ordering (function responds where taxonomy does not) rests on two GeoChip studies from one group [5][15], one abstract only, plus a reviewer's reading of [6]; removing [5] would leave it supported only by the abstract-only [15] and the reading of [6].
  conf: not stated · class: not stated · holds: weak contrasts: 14 years of moderate warming [5], erosion and deposition [15], an elevation gradient [6]; n = 4 per treatment in [5]; platforms differ · src: gaoLongtermWarmingMediterraneantype2021, maDivergentTaxonomicFunctional2017, shenDramaticIncreasesSoil2016 · trail: H1-05 §critic, §answers · from: H1-05:C-007, H1-05:A-004, H1-05:A-021, H1-05:A-034 · rating: "Weak for the reverse ordering"
- **ordering.25** In soil, at single sites or weak or moderate contrasts, the ordering has gone both ways: function less responsive in [4][13][14][18][24], more responsive in [5][15].
  conf: cont (note: "Conflicts") · class: not stated · holds: single sites or weak or moderate contrasts · src: igweRedundancyMaintainsMicrobial2026, panImpactLongtermN2014, yangDecouplingMicrobialCommunity2021, souzaMetagenomicAnalysisReveals2015, saumasanchezFunctionalRedundancyBuffers2024, gaoLongtermWarmingMediterraneantype2021, maDivergentTaxonomicFunctional2017 · trail: H1-05 §answers, §1.4 · from: H1-05:A-001, H1-05:A-011, H1-05:A-022, H1-05:B-0071
- **ordering.26** Lower functional than taxonomic turnover is the most commonly reported ordering in soil but rests on weak comparisons: none of the "function lower" soil studies compares the two turnovers on a common test with a null, and without the global dataset [3] it would rest on small single-site studies and significance contrasts.
  conf: not stated · class: not stated · holds: DNA-measured soil functional profiles · src: none (the reviewer's synthesis) · trail: H1-05 §answers · from: H1-05:A-003, H1-05:A-017, H1-05:A-018, H1-05:A-033 · rating: "Weak for the ordering"
- **ordering.27** GeoChip underlies the three soil studies where function was as or more responsive [5][6][15], two of them from one group (Zhou/Yang), and shotgun annotation underlies most "function lower" results, so platform and result are confounded across the literature; this is the reviewer's cross-study observation, not a tested result.
  conf: not stated · class: reading (note: "This is the reviewer's observation, not a tested result") · holds: the soil studies in the review · src: gaoLongtermWarmingMediterraneantype2021, shenDramaticIncreasesSoil2016, maDivergentTaxonomicFunctional2017 · trail: H1-05 §2, §Adversarial critique · from: H1-05:B-0106, H1-05:B-0107, H1-05:B-0109, H1-05:C-061

### contrast-size: dependence on the size of the environmental contrast
needs: ordering, covariation
- **contrast-size.1** No soil study was found that tests or plots how the functional-taxonomic gap scales with environmental distance; systematic comparisons across a graded range of environmental distances were not measured.
  conf: not stated · class: search (note: "No soil study was found") · holds: the review's searches · src: none (a search result) · trail: H1-05 §1.4, §answers · from: H1-05:A-013, H1-05:A-026, H1-05:B-0066
- **contrast-size.2** In a single-site precipitation experiment, ±30% precipitation slightly decreased and ±60% strongly increased the within-treatment dispersion (PERMDISP) of taxa, genes, proteins and enzyme activities alike, and neither taxonomy nor function showed a directional PERMANOVA shift.
  conf: not stated · class: meas (marker) · holds: a single-site precipitation experiment, two magnitudes of precipitation change [22]; within-treatment dispersion, not turnover across environments; the study does not compare the two turnovers' magnitudes, so it bears only indirectly on the ordering · src: xuDistinctivePatternMechanism2022 (FT, rechecked; measured) · trail: H1-05 §1.4, §critic, §answers · from: H1-05:I-0008, H1-05:B-0067, H1-05:B-0068, H1-05:A-012, H1-05:C-009, H1-05:C-010, H1-05:C-040
- **contrast-size.3** Across studies, strong contrasts [1][2] give covariation, while weak single-site contrasts give both orderings.
  conf: not stated · class: not stated · holds: cross-study comparison of soil studies · src: fiererCrossbiomeMetagenomicAnalyses2012, leffConsistentResponsesSoil2015 · trail: H1-05 §1.4, §answers · from: H1-05:B-0070, H1-05:A-010
- **contrast-size.4** Platform (GeoChip vs shotgun), group, sample size, test and contrast size are confounded across studies, so no dependence on contrast size can be read off.
  conf: not stated · class: reading (critic: H1-05:C-105) · holds: cross-study comparison of the soil studies · src: none (the reviewer's and the critic's synthesis) · trail: H1-05 §critic, §1.4, §5 · from: H1-05:C-008, H1-05:A-005, H1-05:B-0072, H1-05:B-0149, H1-05:C-105, H1-05:C-106

### chronosequence: chronosequences and long-term restoration
needs: turnover, functional-profile
- **chronosequence.1** Chronosequence papers report alpha diversity moving in opposite directions for taxonomy and function, but no paired (head-to-head beta) turnover comparison.
  conf: not stated · class: not stated · holds: [9], [10] · src: goodallTaxonomicFilteringAccompanies2026, sveenFunctionalDiversitySoil2025 · trail: H1-05 §1.5, §answers · from: H1-05:B-0073, H1-05:A-027
- **chronosequence.2** Over 143 years of grassland restoration, bacterial richness falls while SEED functional richness expands.
  conf: not stated · class: not stated · holds: a grassland restoration chronosequence [9]; alpha diversity · src: goodallTaxonomicFilteringAccompanies2026 (FT via agents) · trail: H1-05 §1.5 · from: H1-05:B-0074
- **chronosequence.3** Along a Swedish succession, taxonomic diversity falls while C, N and P gene diversity rises, with PICRUSt2 used for the redundancy analyses.
  conf: not stated · class: not stated · holds: a Swedish successional gradient [10]; alpha diversity · src: sveenFunctionalDiversitySoil2025 (FT via agents) · trail: H1-05 §1.5 · from: H1-05:B-0074
- **chronosequence.4** Between the bioRxiv and ISME J 2026 versions of the restoration study, "profound functional decoupling" was softened to "a decoupling", and the driver taxa were named differently.
  conf: not stated · class: not stated · holds: [9] · src: goodallTaxonomicFilteringAccompanies2026 · trail: H1-05 §4 · from: H1-05:B-0142
- **chronosequence.5** Between the bioRxiv 2025 and Nat Commun 2025 versions of the succession study, "causal link" was softened to "the link".
  conf: not stated · class: not stated · holds: [10] · src: sveenFunctionalDiversitySoil2025 · trail: H1-05 §4 · from: H1-05:B-0143

### drivers: drivers of functional versus taxonomic composition
needs: functional-profile
- **drivers.1** Globally, N-cycling pathway frequencies in soil track habitat and soil C and N much better than the genera that encode them; this is indirect for turnover, because it contrasts drivers, not turnovers.
  conf: not stated · class: not stated · holds: global soil N-cycling traits [12] · src: nelsonGlobalBiogeographyMicrobial2016 (FT via agents) · trail: H1-05 §1.5 · from: H1-05:B-0075, H1-05:B-0076

### other-habitats: functional and taxonomic turnover outside soil
needs: ordering, covariation
- **other-habitats.1** On algal surfaces, taxonomic similarity was 15% and COG similarity 70%.
  conf: not stated · class: not stated · holds: algal surface bacterial communities [35] · src: burkeBacterialCommunityAssembly2011 (secondary or abstract-level; critic: H1-05:C-047, H1-05:C-048 was "FT via fetch summary") · trail: H1-05 §1.6 · from: H1-05:B-0080, H1-05:C-047, H1-05:C-048
- **other-habitats.2** Across a 2000 km, 5 to 35 PSU salinity gradient, salinity explained R2 = 0.70 of taxonomic and 0.17 of KO-based functional variation in the Ulva microbiome (envfit), although 23 KEGG modules still shifted.
  conf: single (critic: H1-05:C-062) · class: not stated · holds: Ulva microbiome [36]; MAG-based taxonomy · src: vanderloosLowFunctionalChange2025 (FT, rechecked) · trail: H1-05 §1.6, §Adversarial critique · from: H1-05:B-0081, H1-05:C-062
- **other-habitats.3** In a coastal Mediterranean time series, all-gene similarity tracked 16S similarity closely (R2 = 0.77), and the authors reject strict redundancy.
  conf: single (critic: H1-05:C-021) · class: not stated · holds: one marine time series [31] · src: galandStrongLinkMarine2018 (FT via agents) · trail: H1-05 §1.6 · from: H1-05:B-0083, H1-05:B-0084, H1-05:C-021
- **other-habitats.4** In subsurface sediments, taxa CVs were about 10 times those of gene groups of similar mean abundance.
  conf: not stated · class: not stated · holds: subsurface sediments [37] · src: soufiTaxonomicVariabilityFunctional2024 (FT via agents) · trail: H1-05 §1.6 · from: H1-05:B-0085
- **other-habitats.5** In bromeliads, functional-group structure was stable while within-group taxonomy varied.
  conf: not stated · class: not stated · holds: bromeliad tank communities [33] · src: loucaHighTaxonomicVariability2016 (AB) · trail: H1-05 §1.6 · from: H1-05:B-0086
- **other-habitats.6** In the global ocean, environment strongly shapes FAPROTAX functional groups but weakly shapes within-group taxonomy.
  conf: not stated · class: deriv (note: "FAPROTAX (derived)") · holds: global ocean microbiome [32]; FAPROTAX-inferred function · src: loucaDecouplingFunctionTaxonomy2016 (AB) · trail: H1-05 §1.6 · from: H1-05:B-0087
- **other-habitats.7** During vermicomposting, PICRUSt2 turnover was about 12 times slower than taxonomic turnover.
  conf: not stated · class: deriv (marker) · holds: vermicomposting [45]; PICRUSt2-inferred function · src: airaFasterTurnoverTaxonomic2026 (FT via agents; derived) · trail: H1-05 §1.6 · from: H1-05:I-0009
- **other-habitats.8** Outside soil, the only strong-contrast case of lower functional than taxonomic turnover is the 2000 km salinity contrast [36], a single study with MAG-based taxonomy; the generalisation that marine and host-associated studies mostly report lower functional turnover mixes FAPROTAX-derived [32], abstract-only [33] and a single time series [31], which finds tight coupling.
  conf: single (critic: H1-05:C-062) · class: not stated · holds: marine and host-associated systems · src: vanderloosLowFunctionalChange2025, loucaDecouplingFunctionTaxonomy2016, loucaHighTaxonomicVariability2016, galandStrongLinkMarine2018, burkeBacterialCommunityAssembly2011 · trail: H1-05 §Adversarial critique, §answers · from: H1-05:C-062, H1-05:A-014
- **other-habitats.9** Across 148 trait datasets, which include diatoms and fungi but no bacteria, mean Mantel r along space was 0.254 taxonomic vs 0.115 functional, with about 31 of 148 datasets reversed.
  conf: not stated · class: not stated · holds: [48]; datasets including diatoms and fungi, no bacteria · src: gracorozaDistanceDecay22022 (FT via agents) · trail: H1-05 §1.6, §critic · from: H1-05:B-0088, H1-05:C-011, H1-05:C-055, H1-05:C-103
- **other-habitats.10** In European fish, functional beta diversity was below taxonomic, driven by turnover.
  conf: not stated · class: not stated · holds: European fish assemblages [50] · src: villegerDecomposingFunctionalDiversity2013 (AB) · trail: H1-05 §1.6 · from: H1-05:B-0089
- **other-habitats.11** In European fish, functional homogenization over time exceeded taxonomic homogenization six-fold.
  conf: not stated · class: not stated · holds: European fish assemblages [51] · src: villegerFunctionalHomogenizationExceeds2014 (AB) · trail: H1-05 §1.6 · from: H1-05:B-0090
- **other-habitats.12** The trait-dataset synthesis [48] and the fish studies [50][51] show lower functional decay on average, but with many reversals.
  conf: not stated · class: not stated · holds: [48] (diatoms and fungi included, no bacteria), [50], [51] · src: gracorozaDistanceDecay22022, villegerDecomposingFunctionalDiversity2013, villegerFunctionalHomogenizationExceeds2014 · trail: H1-05 §answers, §critic · from: H1-05:A-015, H1-05:C-011

### marker-inferred: function inferred from 16S (PICRUSt, FAPROTAX)
needs: functional-profile, turnover
- **marker-inferred.1** ZnO dose separated taxa but not PICRUSt-type predicted functions.
  conf: not stated · class: deriv (marker) · holds: ZnO dose [25]; PICRUSt-type inferred function · src: dineshSoilPollutedNano2023 (AB; derived) · trail: H1-05 §1.2 · from: H1-05:I-0005
- **marker-inferred.2** Along an alpine gradient, PICRUSt2 function was redundant and tracked phylogenetic more than taxonomic dissimilarity.
  conf: not stated · class: deriv (marker) · holds: an alpine altitudinal gradient [26]; PICRUSt2-inferred function · src: liAsynchronousPatternsSoil2024 (FT via agents; derived) · trail: H1-05 §1.2 · from: H1-05:I-0006
- **marker-inferred.3** Soil PICRUSt2-inferred profiles are not independent of taxonomy: the ZnO and alpine studies infer function from the same 16S data, so they are not independent tests, and they report either decoupling [25] or functional dissimilarity closer to phylogenetic than to taxonomic dissimilarity [26].
  conf: not stated · class: not stated · holds: marker-inferred function in soil · src: dineshSoilPollutedNano2023, liAsynchronousPatternsSoil2024 · trail: H1-05 §1.2, §answers · from: H1-05:B-0058, H1-05:A-045

### functional-unit: functional unit and annotation level
needs: ordering, functional-profile
- **functional-unit.1** In soil, each finding on whether functional unit, annotation or metric changes the functional-taxonomic comparison rests on one study.
  conf: single (critic: H1-05:C-012) · class: not stated · holds: soil · src: none (the review's and the critic's summary) · trail: H1-05 §critic, §answers, §2 · from: H1-05:C-012, H1-05:A-036, H1-05:A-052, H1-05:A-053, H1-05:B-0091 · rating: "Weak for soil"
- **functional-unit.2** In the global soil metagenome comparison, functional similarity exceeded taxonomic similarity at SEED levels 1 and 2 against all five taxonomic ranks, so the ordering did not reverse at any combination tested.
  conf: single (critic: H1-05:C-012) · class: not stated · holds: [3], the only soil study reporting the comparison at several annotation levels; removing it leaves no soil evidence on annotation level · src: chenFunctionalRedundancySoil2022 (FT, rechecked) · trail: H1-05 §critic, §2, §answers · from: H1-05:C-013, H1-05:C-014, H1-05:B-0092, H1-05:A-037, H1-05:A-057, H1-05:A-063
- **functional-unit.3** The authors of the global comparison say coarser levels are more conserved.
  conf: not stated · class: not stated · holds: [3] · src: chenFunctionalRedundancySoil2022 · trail: H1-05 §2 · from: H1-05:B-0093
- **functional-unit.4** The global comparison explicitly chose SEED over KO, COG and NOG, so finer functional units (KO, gene clusters) were not tested, and whether the ordering can reverse at fine resolution is open.
  conf: not stated · class: not stated · holds: [3] · src: chenFunctionalRedundancySoil2022 · trail: H1-05 §critic, §2 · from: H1-05:C-016, H1-05:A-039, H1-05:B-0094
- **functional-unit.5** In subsurface sediments, taxa were about an order of magnitude more variable than gene groups at every KEGG level and EC, after abundance matching, so the ordering did not reverse by unit there.
  conf: not stated · class: not stated · holds: sediments [37]; after abundance matching · src: soufiTaxonomicVariabilityFunctional2024 · trail: H1-05 §2, §answers · from: H1-05:A-049, H1-05:B-0105, H1-05:A-057
- **functional-unit.6** In lake enrichments, redundancy was higher with EC grouping than with KO.
  conf: not stated · class: not stated · holds: lake enrichment communities [38] · src: lemoigneLinkingStochasticAssembly2026 (FT via agents) · trail: H1-05 §2, §answers · from: H1-05:A-050, H1-05:B-0104
- **functional-unit.7** For ectomycorrhizal fungi, turnover appeared at the level of gene sequence variants but not of gene-family abundance.
  conf: not stated · class: not stated · holds: ectomycorrhizal fungi [20]; abstract only · src: pellitierPotentialFunctionalDivergence2024 (AB) · trail: H1-05 §2, §answers · from: H1-05:A-043, H1-05:B-0103

### annotation: annotated versus all reads, and the unannotated fraction
needs: functional-profile, covariation, ordering, platform
- **annotation.1** In one soil experiment, within-treatment dissimilarity from all reads including unannotated ones (Mash) and from assembled genes patterned like annotated-read dissimilarity, so in that case the annotation did not change the result.
  conf: single (critic: H1-05:C-012) · class: not stated · holds: one soil experiment [22]; within-treatment dissimilarities · src: xuDistinctivePatternMechanism2022 (FT, rechecked) · trail: H1-05 §2, §critic, §answers · from: H1-05:A-040, H1-05:B-0095, H1-05:C-017
- **annotation.2** In a marine time series, the functional-taxonomic correlation fell from R2 0.77 (all genes) to 0.58 (KEGG) to 0.16 (FAPROTAX/PICRUSt), so coupling strength depends on the annotation scheme.
  conf: single (critic: H1-05:C-021) · class: not stated · holds: a marine time series [31]; removing it removes the main direct evidence that annotation scheme changes coupling strength · src: galandStrongLinkMarine2018 (full text) · trail: H1-05 §2, §critic, §answers · from: H1-05:A-048, H1-05:B-0096, H1-05:C-021, H1-05:A-054, H1-05:A-064, H1-05:C-118 · rating: "Moderate for the general point, outside soil, that annotation scheme changes the strength of coupling"
- **annotation.3** The marine time series finds restricting to annotated genes weakens the coupling, while the soil precipitation experiment finds all-read and annotated dissimilarity behave alike; the two use different measures (regression of similarities vs within-treatment dispersion) and habitats, so they do not directly contradict.
  conf: not stated · class: not stated · holds: [31] (marine) and [22] (soil) · src: galandStrongLinkMarine2018, xuDistinctivePatternMechanism2022 · trail: H1-05 §answers, §2 · from: H1-05:A-055, H1-05:A-056, H1-05:B-0097
- **annotation.4** Unknown-function genes are prevalent in fine-textured, higher-pH soils and are often mobile-element associated; the unannotated fraction varies with soil properties.
  conf: not stated · class: not stated · holds: soils in [27], a preprint · src: hollandmoritzEcologicalPerspectiveMicrobial2021 (AB; preprint) · trail: H1-05 §2, §answers · from: H1-05:B-0098, H1-05:A-047
- **annotation.5** So the unannotated fraction can vary along soil gradients: indirect support for an annotation-bias critique, not a demonstration of its effect on turnover.
  conf: not stated · class: not stated · holds: inference from [27] · src: hollandmoritzEcologicalPerspectiveMicrobial2021 · trail: H1-05 §2 · from: H1-05:B-0099, H1-05:C-126

### metric: dissimilarity measure and turnover statistic
needs: turnover, ordering
- **metric.1** On the same 27 paired steppe and cropland soils, the choice of turnover statistic changed the functional conclusion: an earlier distance-decay-slope analysis found greater KEGG functional turnover in cropland, while the dispersion-based analysis found KEGG gene assemblages homogenized in cropland at local and regional scales and bacterial taxa homogenized only locally.
  conf: single (critic: H1-05:C-012) · class: not stated · holds: 27 paired steppe and cropland soils [23]; the only soil case where metric choice reversed a conclusion · src: guLandConversionCropland2025 (FT, rechecked) · trail: H1-05 §critic, §1.5, §2, §answers · from: H1-05:C-018, H1-05:A-041, H1-05:A-042, H1-05:A-065, H1-05:B-0077, H1-05:B-0078, H1-05:B-0100
- **metric.2** No soil study was found that compares dissimilarity measures (Bray-Curtis vs Aitchison vs Jaccard) or transforms for the functional-taxonomic ordering.
  conf: not stated · class: search (note: "No soil study was found") · holds: searches by both agents · src: none (a search result) · trail: H1-05 §critic, §2 · from: H1-05:C-020, H1-05:B-0101

### taxonomic-resolution: taxonomic resolution and how the taxonomic side is measured
needs: ordering
- **taxonomic-resolution.1** In one grassland under grazing and P addition, resolving taxa within functional groups at species level gave strong taxon-function consistency (Procrustes) and removed an apparent decoupling.
  conf: single (critic: H1-05:C-012) · class: not stated · holds: one grazing and P-addition site [11] · src: liuReciprocalChangesDominant2023 (FT via agents) · trail: H1-05 §2, §1.5, §answers · from: H1-05:A-044, H1-05:B-0102, H1-05:B-0079
- **taxonomic-resolution.2** In anaerobic digesters, taxonomic convergence depended on taxonomic rank, and inoculum identity was recoverable at genus but less at phylum level.
  conf: not stated · class: not stated · holds: anaerobic digestion communities [44]; abstract only · src: jourdainEnvironmentalSelectionConstrains2026 (AB) · trail: H1-05 §2, §answers · from: H1-05:A-051, H1-05:B-0104
- **taxonomic-resolution.3** The taxonomic side is measured differently across studies (16S amplicon in [1][2][5]; read-based RefSeq in [3]; MAG in [36]), and the review does not keep this apart.
  conf: not stated · class: not stated · holds: the studies named · src: fiererCrossbiomeMetagenomicAnalyses2012, leffConsistentResponsesSoil2015, gaoLongtermWarmingMediterraneantype2021, chenFunctionalRedundancySoil2022, vanderloosLowFunctionalChange2025 · trail: H1-05 §critic · from: H1-05:C-019

### genome-size: average genome size
needs: functional-profile, ordering
- **genome-size.1** Average genome size biases gene-abundance comparisons.
  conf: not stated · class: not stated · holds: human gut only [47] · src: nayfachAverageGenomeSize2015 (AB; human gut) · trail: H1-05 §2 · from: H1-05:B-0110, H1-05:C-127
- **genome-size.2** In soil, average genome size shifts with N and P addition and with heating.
  conf: not stated · class: not stated · holds: soil; N and P addition [2]; heating [8] · src: leffConsistentResponsesSoil2015, barnettDisturbanceIncreasesSoil2025 · trail: H1-05 §2 · from: H1-05:B-0111, H1-05:B-0110
- **genome-size.3** The effect of genome size on the functional-taxonomic turnover comparison was not tested in any study found, and genome-size normalization was not measured in soil.
  conf: not stated · class: search (note: "not tested in any study found") · holds: the review's searches · src: none (a search result) · trail: H1-05 §2, §answers · from: H1-05:B-0111, H1-05:A-058

### measurement-artefacts: relic DNA, compositionality, sequencing depth and rarefaction
needs: ordering
- **measurement-artefacts.1** No study was found that examines relic DNA, compositionality or sequencing depth for the functional-taxonomic comparison; these were not searched in depth by either agent, so the absence is weakly established.
  conf: not stated · class: search (note: "not searched in depth by either agent") · holds: both agents' routes · src: none (a search result) · trail: H1-05 §3.4, §answers, §Provenance · from: H1-05:C-130, H1-05:A-082, H1-05:B-0020
- **measurement-artefacts.2** In soil, the ordering has not been measured across dissimilarity measures, compositional (log-ratio) transforms, KO vs COG vs pangenome clusters vs MAG-resolved traits, rarefaction depth, relic-DNA removal or genome-size normalization, so no reversal of ordering by any of these was found because none was tested.
  conf: not stated · class: search (note: "none was tested") · holds: soil · src: none (a search result) · trail: H1-05 §answers · from: H1-05:A-058, H1-05:A-059

### non-dna-function: function measured as RNA, protein or enzyme activity
needs: functional-profile, ordering
- **non-dna-function.1** Across North America, soil fungi showed endemism with convergent enzyme activity; this is a non-DNA case and indirect for DNA profiles.
  conf: not stated · class: not stated · holds: North American soil mycobiome [21]; enzyme activity · src: talbotEndemismFunctionalConvergence2014 (AB) · trail: H1-05 §1.2 · from: H1-05:B-0056, H1-05:B-0057
- **non-dna-function.2** Soil RNA (metatranscriptome) and protein (metaproteome) turnover comparisons were not measured, apart from metaproteome dispersion, which tracked taxonomy, in the precipitation experiment; the only non-DNA soil case is that metaproteome dispersion.
  conf: not stated · class: search (note: "Not measured") · holds: soil · src: xuDistinctivePatternMechanism2022 · trail: H1-05 §answers, §Adversarial critique · from: H1-05:A-025, H1-05:C-088

### null-model: null models for the functional-taxonomic difference
needs: turnover, ordering
- **null-model.1** No field-soil study was found that applies a null model (taxon-label shuffling of a gene-content matrix, trait randomization, phylogenetic null) to the difference between functional and taxonomic turnover.
  conf: not stated · class: search (note: "No field-soil study was found") · holds: both search agents' Europe PMC boolean queries on soil, metagenome or GeoChip combined with null, shuffle, randomization, NST or betaNTI; the critic finds the absence appropriately worded as a search result · src: none (a search result) · trail: H1-05 §3.1, §answers, §critic · from: H1-05:B-0112, H1-05:B-0113, H1-05:A-066, H1-05:A-067, H1-05:C-022, H1-05:C-046, H1-05:A-083 · rating: "Weak for soil"
- **null-model.2** Not measured: any label-shuffling, trait or phylogenetic null applied to field-soil shotgun, GeoChip, RNA or protein profiles to test whether functional turnover is lower than expected given taxonomic turnover, and nulls across environmental-contrast sizes in soil.
  conf: not stated · class: search (note: "Not measured") · holds: soil · src: none (a search result) · trail: H1-05 §answers · from: H1-05:A-092, H1-05:A-093
- **null-model.3** Soil nulls found target taxonomic assembly only: SES of taxonomic beta in the precipitation experiment, iCAMP in the dryland study.
  conf: not stated · class: not stated · holds: [22], [24] · src: xuDistinctivePatternMechanism2022, saumasanchezFunctionalRedundancyBuffers2024 · trail: H1-05 §3.1, §answers · from: H1-05:B-0114, H1-05:A-068
- **null-model.4** In a Tibetan wetland spanning sediment, rhizosphere and bulk soils along salinity, separate null-model analyses put the deterministic share at 32.39% for taxonomy and 45.78%, 43.79% and 48.19% for methane, N and S gene composition, which the authors read as the environment selecting function rather than taxa.
  conf: not stated · class: deriv (marker) · holds: wetland sediment and soil pooled [28]; separate assembly nulls on taxonomy and on gene sets, a different class of null from Ho and Huang's; it does not test the difference itself; the null framework was not named in the text the agent read; the only soil-inclusive null comparison of functional and taxonomic determinism · src: zhangEnvironmentSelectedMicrobial2025 (FT via agents; derived) · trail: H1-05 §3.1, §critic, §answers · from: H1-05:I-0010, H1-05:A-069, H1-05:B-0115, H1-05:C-029, H1-05:C-030, H1-05:A-091, H1-05:A-102
- **null-model.5** A simulated 72% species loss in global soil metagenomes produced limited change in functional categories; this is a resampling construction, not a field comparison.
  conf: not stated · class: model (marker) · holds: global soil metagenomes [19]; abstract only · src: chenStableSoilMicrobial2021 (AB; modelled) · trail: H1-05 §3.1, §answers · from: H1-05:I-0011, H1-05:A-070, H1-05:B-0116
- **null-model.6** In lake enrichments, 80.2% of community pairs matched a taxon-shuffling null for between-community redundancy, while communities were less functionally dissimilar than random GTDB genome sets, read as selection plus shared pool origin.
  conf: not stated · class: not stated · holds: lake enrichment communities [38] · src: lemoigneLinkingStochasticAssembly2026 (FT via agents) · trail: H1-05 §3.3, §answers · from: H1-05:B-0129, H1-05:B-0130, H1-05:A-074
- **null-model.7** In bioreactors, taxa and genes assembled differently under a null; the preprint said stochasticity was more important for genes, driven by rare genes, while the published abstract drops this and stresses determinism under disturbance.
  conf: not stated · class: not stated · holds: bioreactors [39]; abstract only, preprint and published version · src: santillanPressDisturbanceAlters2020 (AB), santillan2019 (AB) · trail: H1-05 §3.3, §4, §answers · from: H1-05:B-0131, H1-05:B-0132, H1-05:B-0133, H1-05:B-0144, H1-05:A-075
- **null-model.8** In contaminated sediments, functional and phylogenetic beta diversity correlated, with the null applied to taxonomy only.
  conf: not stated · class: not stated · holds: contaminated sediments [46]; abstract only · src: renComparisonMicrobialTaxonomic2016 (AB) · trail: H1-05 §3.3 · from: H1-05:B-0134
- **null-model.9** Network nulls on gut gene-content networks [40] and gut proteome networks [41] show that redundancy arises from nested gene sharing; this bears only indirectly on between-sample turnover.
  conf: not stated · class: not stated · holds: human gut DNA [40] and protein [41] · src: tianDecipheringFunctionalRedundancy2020 (FT via agents), liRevealingProteomelevelFunctional2023 (FT via agents) · trail: H1-05 §3.3, §answers · from: H1-05:B-0135, H1-05:B-0136, H1-05:A-076
- **null-model.10** Across 148 datasets, which include diatoms and fungi but no bacteria, a species-name randomization found functional decay "random given taxonomic decay" in most datasets: 13 deviated along space (3 faster, 10 slower) and 11 along environment (all but one faster).
  conf: not stated · class: not stated · holds: [48]; diatoms and fungi included, no bacteria · src: gracorozaDistanceDecay22022 · trail: H1-05 §3.3, §critic, §answers · from: H1-05:B-0137, H1-05:C-031, H1-05:A-077
- **null-model.11** The authors of [48] note that hypervolume Sørensen gives lower taxonomic than functional similarity by construction for communities sharing no species.
  conf: not stated · class: not stated · holds: [48] · src: gracorozaDistanceDecay22022 · trail: H1-05 §3.3 · from: H1-05:B-0138, H1-05:B-0137
- **null-model.12** The 148-dataset synthesis supports that most functional turnover is predictable from taxonomic turnover under a randomization null, from datasets that include diatoms and fungi but no bacteria.
  conf: not stated · class: not stated · holds: [48] · src: gracorozaDistanceDecay22022 · trail: H1-05 §answers, §Adversarial critique · from: H1-05:A-086, H1-05:C-055
- **null-model.13** Tropical trees along an elevation gradient turned over functionally faster than a trait-randomization null predicts.
  conf: not stated · class: not stated · holds: tropical trees [49] · src: swensonDeterministicTropicalTree2010 (secondary or abstract-level; critic: H1-05:C-047, H1-05:C-048 was "FT via fetch summary") · trail: H1-05 §3.3, §critic, §answers · from: H1-05:B-0139, H1-05:C-032, H1-05:A-078, H1-05:C-047, H1-05:C-048
- **null-model.14** [48] (mostly null-consistent) and [49] (faster than null, in trees) disagree.
  conf: cont (note: "disagree") · class: not stated · holds: [48] (includes diatoms and fungi, lacks bacteria); [49] (trees) · src: gracorozaDistanceDecay22022, swensonDeterministicTropicalTree2010 · trail: H1-05 §answers, §critic, §Adversarial critique · from: H1-05:A-090, H1-05:C-032, H1-05:C-055

### averaging: the averaging problem and Ho and Huang's label-shuffling null
needs: null-model, marker-inferred, functional-profile, redundancy
group: redundancy-averaging
- **averaging.1** Ho and Huang argue, in a modelled and single-source argument read only through a fetch summary of the preprint, that converting taxon abundances to function abundances through a gene-content matrix sums over many taxa, so functional variability falls by statistical averaging even without any selection; the published abstract keeps this conclusion.
  conf: single (critic: H1-05:C-027) · class: model (marker) · holds: functions inferred through a gene-content matrix (FAPROTAX-style groups or genome annotations), not shotgun-measured profiles; modelled; not applied to field soil · src: hoChallengesQuantifyingFunctional2024 (secondary or abstract-level; modelled; critic: H1-05:C-047, H1-05:C-048 was "FT preprint via fetch summary; modelled"), hoChallengesInterpretingFunctional2025 (AB) · trail: H1-05 §3.2, §critic, §answers · from: H1-05:B-0117, H1-05:I-0012, H1-05:B-0118, H1-05:B-0127, H1-05:C-024, H1-05:C-027, H1-05:C-028, H1-05:C-050, H1-05:A-084 · limit: access (critic: H1-05:C-050)
- **averaging.2** Ho and Huang's null permutes taxon labels across the gene-content matrix, which keeps function prevalences and scrambles taxon-function links; it tests variability around a mean community within one environment, not turnover across environments.
  conf: not stated · class: not stated · holds: [29], [30] · src: hoChallengesInterpretingFunctional2025, hoChallengesQuantifyingFunctional2024 · trail: H1-05 §3.2, §critic · from: H1-05:B-0119, H1-05:C-025
- **averaging.3** On bromeliad data, the label-shuffling null found no evidence of functional selection, so the bromeliad pattern is consistent with averaging.
  conf: not stated · class: not stated · holds: a reanalysis of the bromeliad communities of [33] · src: hoChallengesInterpretingFunctional2025, hoChallengesQuantifyingFunctional2024, loucaHighTaxonomicVariability2016 · trail: H1-05 §3.2, §answers · from: H1-05:B-0121, H1-05:A-073, H1-05:A-088
- **averaging.4** In soil- and leaf-derived communities grown in vitro on glucose (Goldford data), functional distance was significantly below the shuffles, read as selection for metabolic function; this soil-derived result is indirect for field soil and belongs to the marker-inferred case.
  conf: not stated · class: not stated · holds: in vitro communities on one glucose medium [42]; the only soil-derived (in vitro) null result · src: hoChallengesInterpretingFunctional2025, hoChallengesQuantifyingFunctional2024, goldfordEmergentSimplicityMicrobial2018 · trail: H1-05 §3.2, §answers, §critic · from: H1-05:B-0122, H1-05:A-072, H1-05:C-026, H1-05:A-100
- **averaging.5** In gut communities in vitro, the label-shuffling null found selection with metabolomics-based groupings.
  conf: not stated · class: not stated · holds: in vitro gut communities [29][30] · src: hoChallengesInterpretingFunctional2025, hoChallengesQuantifyingFunctional2024 · trail: H1-05 §3.2 · from: H1-05:B-0123
- **averaging.6** In HMP stool, apparent functional selection disappeared under restricted shuffles, so it was artifactual.
  conf: not stated · class: not stated · holds: HMP stool data [29][30] · src: hoChallengesInterpretingFunctional2025, hoChallengesQuantifyingFunctional2024 · trail: H1-05 §3.2, §answers · from: H1-05:B-0124, H1-05:A-073
- **averaging.7** Results of the label-shuffling null differed by system: it gives opposite answers for bromeliad communities (consistent with averaging) and for in vitro soil communities (selection).
  conf: not stated · class: not stated · holds: [29][30] · src: hoChallengesInterpretingFunctional2025, hoChallengesQuantifyingFunctional2024 · trail: H1-05 §3.2, §answers · from: H1-05:B-0120, H1-05:A-089
- **averaging.8** Ho and Huang's label-shuffling null is the only direct microbial test of the functional-taxonomic difference, but it works on functions inferred from taxonomy through a gene-content matrix, the logic of PICRUSt/FAPROTAX, and on variability within one environment rather than turnover across environments; without it the answer would rest on [48][49] and on indirect microbial nulls [38][40].
  conf: single (critic: H1-05:C-027) · class: not stated · holds: microbial data · src: hoChallengesInterpretingFunctional2025, hoChallengesQuantifyingFunctional2024 · trail: H1-05 §critic, §Adversarial critique, §answers · from: H1-05:C-023, H1-05:C-041, H1-05:C-042, H1-05:C-043, H1-05:C-100, H1-05:C-101, H1-05:A-099, H1-05:A-100, H1-05:A-101
- **averaging.9** Between the bioRxiv 2024 and Cell Systems 2025 versions, the title changed and the second confound was renamed from "bias toward environment-independent beneficial functions" to correlations between functions and taxonomic abundances handled by an "extended null model"; the abstract conclusions are otherwise consistent, and the published body was not reached.
  conf: not stated · class: not stated · holds: [29], [30]; abstracts and a fetch summary of the preprint · src: hoChallengesInterpretingFunctional2025, hoChallengesQuantifyingFunctional2024 · trail: H1-05 §3.2, §4, §answers · from: H1-05:B-0125, H1-05:B-0126, H1-05:B-0141, H1-05:A-094
- **averaging.10** None of the soil "redundancy" studies [3][4][7][8][13][24] controls for averaging; this is the reviewer's application of Ho and Huang to other studies, not a finding of those studies.
  conf: not stated · class: reading (critic: H1-05:C-109) · holds: the soil "function lower" results in the review · src: hoChallengesInterpretingFunctional2025, hoChallengesQuantifyingFunctional2024, chenFunctionalRedundancySoil2022, igweRedundancyMaintainsMicrobial2026, zhangSoilBacterialEndemism2016, barnettDisturbanceIncreasesSoil2025, panImpactLongtermN2014, saumasanchezFunctionalRedundancyBuffers2024 · trail: H1-05 §3.2, §answers, §Adversarial critique · from: H1-05:B-0128, H1-05:A-085, H1-05:C-108, H1-05:C-109, H1-05:C-110
- **averaging.11** Ho and Huang's null has limits the review does not examine: it runs on inferred functions and within-environment variability, and its soil result comes from a single in vitro medium.
  conf: not stated · class: not stated · holds: [29][30] · src: hoChallengesInterpretingFunctional2025, hoChallengesQuantifyingFunctional2024 · trail: H1-05 §Adversarial critique · from: H1-05:C-098
- **averaging.12** In the 148-dataset synthesis, lower average functional decay coexists with most datasets being null-consistent, the same caution Ho and Huang raise for microbes.
  conf: not stated · class: not stated · holds: [48] (diatoms and fungi included, no bacteria) · src: gracorozaDistanceDecay22022, hoChallengesInterpretingFunctional2025, hoChallengesQuantifyingFunctional2024 · trail: H1-05 §5 · from: H1-05:B-0151
- **averaging.13** The review's lean towards "function lower is not evidence of redundancy" rests on Ho and Huang (modelled, single source) and on the 148-dataset synthesis (non-bacterial), and is not simply echoed from the brief, which is phrased in both directions and does not state an expected answer.
  conf: not stated · class: not stated · holds: the critic's expectation-echo check · src: hoChallengesInterpretingFunctional2025, hoChallengesQuantifyingFunctional2024, gracorozaDistanceDecay22022 · trail: H1-05 §Adversarial critique · from: H1-05:C-111, H1-05:C-112, H1-05:C-113

### redundancy: functional redundancy as an explanation
needs: ordering, averaging
group: redundancy-averaging
- **redundancy.bg1** Allison and Martiny define functional redundancy as the ability of one microbial taxon to carry out a process at the same rate as another under the same environmental conditions.
  kind: background · ref: allisonResistanceResilienceRedundancy2008 · check: DOI 10.1073/pnas.0801925105 resolves on Crossref; the definition is in Table 1 ("Summary of definitions used in this article"), section "A Framework Within the Black Box" (PMC2556421 full text)
- **redundancy.1** The review counts as arguments for redundancy (asserted or measured without nulls) [3][4][7][13][18][24] in soil and [33][35][36][37] elsewhere; the answers list [3][4][7][33][34].
  conf: not stated · class: not stated · holds: the review's classification of its sources · src: chenFunctionalRedundancySoil2022, igweRedundancyMaintainsMicrobial2026, zhangSoilBacterialEndemism2016, panImpactLongtermN2014, souzaMetagenomicAnalysisReveals2015, saumasanchezFunctionalRedundancyBuffers2024, loucaHighTaxonomicVariability2016, burkeBacterialCommunityAssembly2011, vanderloosLowFunctionalChange2025, soufiTaxonomicVariabilityFunctional2024, loucaFunctionFunctionalRedundancy2018 · trail: H1-05 §3.4, §answers · from: H1-05:C-114, H1-05:C-115, H1-05:A-079
- **redundancy.2** The authors of the global metagenome comparison call its result strong evidence for functional redundancy.
  conf: not stated · class: not stated · holds: [3] · src: chenFunctionalRedundancySoil2022 · trail: H1-05 §1.2 · from: H1-05:B-0044
- **redundancy.3** The authors of the serpentine study conclude redundancy, and they note that specialized functions such as siderophore biosynthesis did differ.
  conf: not stated · class: not stated · holds: [4] · src: igweRedundancyMaintainsMicrobial2026 · trail: H1-05 §1.2 · from: H1-05:B-0048
- **redundancy.4** The perspective of Louca et al. 2018 argues that redundancy and within-function variability are emergent properties of open systems, not drift.
  conf: not stated · class: assert (marker) · holds: [34]; abstract only · src: loucaFunctionFunctionalRedundancy2018 (AB, asserted) · trail: H1-05 §3.4 · from: H1-05:C-116
- **redundancy.5** Louca et al. conclude that non-neutral processes shape within-function taxonomy and redundancy, while Ho and Huang find the bromeliad pattern consistent with averaging.
  conf: cont (note: "Conflicts") · class: not stated · holds: [33][34] against [29]; what the Louca tests controlled for is known only from abstracts and from Ho and Huang's description · src: loucaHighTaxonomicVariability2016 (AB), loucaFunctionFunctionalRedundancy2018 (AB), hoChallengesInterpretingFunctional2025 · trail: H1-05 §answers · from: H1-05:A-087, H1-05:A-088, H1-05:A-098 · limit: access (note: "Louca et al. originals were not reached in full text")
- **redundancy.6** The review counts as against or complicating redundancy: coupling holds when all genes are used [31]; functional dispersion tracks taxonomic dispersion [22]; decoupling vanishes at species resolution within groups [11]; averaging alone reproduces lower functional variability [29][30]; function is more responsive under some weak contrasts [5][15].
  conf: not stated · class: not stated · holds: the review's classification of its sources · src: galandStrongLinkMarine2018, xuDistinctivePatternMechanism2022, liuReciprocalChangesDominant2023, hoChallengesInterpretingFunctional2025, hoChallengesQuantifyingFunctional2024, gaoLongtermWarmingMediterraneantype2021, maDivergentTaxonomicFunctional2017 · trail: H1-05 §3.4, §answers · from: H1-05:C-117, H1-05:C-118, H1-05:C-119, H1-05:C-120, H1-05:C-121, H1-05:C-122, H1-05:A-080
- **redundancy.7** The authors of the precipitation experiment conclude that "taxonomic stochasticity translated into functional stochasticity", not redundancy.
  conf: not stated · class: not stated · holds: [22] · src: xuDistinctivePatternMechanism2022 · trail: H1-05 §1.4 · from: H1-05:B-0069
- **redundancy.8** One grassland study argues against redundancy, attributing apparent decoupling and stable function to reciprocal changes in two dominant species.
  conf: not stated · class: not stated · holds: one grazing and P-addition grassland site [11] · src: liuReciprocalChangesDominant2023 (FT via agents) · trail: H1-05 §answers, §1.5 · from: H1-05:A-071, H1-05:B-0079
- **redundancy.9** The cross-biome study [1] explicitly concludes that functional redundancy "is not so pervasive as to obscure" the taxonomy-function relationship; the review lists it only as an annotation-fraction critique.
  conf: not stated · class: not stated · holds: [1] · src: fiererCrossbiomeMetagenomicAnalyses2012 · trail: H1-05 §Adversarial critique · from: H1-05:C-099
- **redundancy.10** The review reports critiques of redundancy claims by ground: aggregation or averaging [29][30] (modelled plus reanalysis); annotation fraction and bias [1][31]; unannotated genes varying with soil [27] (indirect); genome size [47], with soil shifts in [2][8] (indirect); asymmetric power or sample size between the functional and taxonomic tests [4] (reviewer's reading); marker-inferred function being circular [25][26][45], with weak coupling of inferred to measured profiles in [31].
  conf: not stated · class: not stated · holds: the review's classification of its sources · src: hoChallengesInterpretingFunctional2025, hoChallengesQuantifyingFunctional2024, fiererCrossbiomeMetagenomicAnalyses2012, galandStrongLinkMarine2018, hollandmoritzEcologicalPerspectiveMicrobial2021, nayfachAverageGenomeSize2015, leffConsistentResponsesSoil2015, barnettDisturbanceIncreasesSoil2025, igweRedundancyMaintainsMicrobial2026, dineshSoilPollutedNano2023, liAsynchronousPatternsSoil2024, airaFasterTurnoverTaxonomic2026 · trail: H1-05 §3.4, §answers · from: H1-05:C-123, H1-05:C-124, H1-05:C-125, H1-05:C-126, H1-05:C-127, H1-05:C-128, H1-05:C-129, H1-05:A-081

## Do not say
- **dns.1** "In marine [36], function stays lower even under a strong contrast, unlike the soil cross-biome result [1]."
  why: [1] made no magnitude comparison, and [3] is itself a strong-contrast soil case of function lower; the sentence treats a correlation result and a magnitude result as the same kind of finding, and the body's own Section 5 concedes covariation and magnitude are separate · instead: ordering.1, ordering.3, other-habitats.2 · trail: H1-05 §critic, §Adversarial critique · from: H1-05:B-0082, H1-05:C-005, H1-05:C-035, H1-05:C-036, H1-05:C-037, H1-05:C-102
- **dns.2** "Covariation is replicated across three independent soil datasets."
  why: the datasets are not independent in lineage: [1] and [2] come from one group, and [3] pools MG-RAST submissions that may include [1]; the strength note concedes the shared lineage · instead: covariation.1 · trail: H1-05 §critic, §Adversarial critique · from: H1-05:B-0039, H1-05:A-016, H1-05:C-002, H1-05:C-038
- **dns.3** "The precipitation experiment [22] is the only within-site test of contrast size."
  why: it measures within-treatment dispersion with no directional shift in either community and does not compare the two turnovers' magnitudes, so it is indirect for turnover across environments · instead: contrast-size.2 · trail: H1-05 §Adversarial critique · from: H1-05:A-035, H1-05:C-039, H1-05:C-040, H1-05:C-101
- **dns.4** "Ho and Huang's null is the only null model that directly targets the functional-taxonomic difference in microbial data", without saying that it works on marker-inferred function and within-environment variability.
  why: it operates on functions inferred from taxa through a gene-content matrix, the same logic as PICRUSt/FAPROTAX, which the brief requires to be labelled separately, and on distance from the mean community in one medium, not turnover across environments · instead: averaging.8, averaging.2 · trail: H1-05 §Adversarial critique · from: H1-05:A-100, H1-05:C-041, H1-05:C-042, H1-05:C-043, H1-05:C-100, H1-05:C-101
- **dns.5** "Functional similarity exceeded taxonomic similarity at SEED levels 1 and 2, so the gap widens as functions are aggregated."
  why: that the gap widens is the reviewer's inference from [3] alone, phrased as a finding; Chen states only that the ordering held at all levels · instead: functional-unit.2 · trail: H1-05 §critic, §Adversarial critique · from: H1-05:A-038, H1-05:C-015, H1-05:C-044, H1-05:C-045, H1-05:C-059
- **dns.6** "Aggregation alone lowers functional variability, so 'function lower' is not by itself evidence of redundancy", as a methodological point bearing on every soil study, or "Ho and Huang show analytically and by simulation" with a 'Moderate' rating.
  why: it rests on Ho and Huang [29][30] only and is modelled; the 'Moderate' firmness rests on a summary of the preprint, the published version having been read as abstract only (access) · instead: averaging.1, averaging.10 · trail: H1-05 §Adversarial critique · from: H1-05:A-084, H1-05:C-050, H1-05:C-060
- **dns.7** "GeoChip underlies the studies where function was as or more responsive", stated as a finding.
  why: it is the reviewer's cross-study observation drawn from three papers, two from one group (Zhou/Yang), on which the D1 answer leans · instead: ordering.27 · trail: H1-05 §Adversarial critique · from: H1-05:B-0106, H1-05:C-061
- **dns.8** "Marine and host-associated studies mostly report lower functional turnover."
  why: it mixes FAPROTAX-derived [32], abstract-only [33] and a single time series [31]; the only strong-contrast case is [36], a single study with MAG-based taxonomy · instead: other-habitats.8 · trail: H1-05 §Adversarial critique · from: H1-05:A-014, H1-05:C-062
- **dns.9** "Metric choice reversed the conclusion", stated generally.
  why: it rests on [23] alone; it is flagged in the sensitivity note but stated generally in Section 2 · instead: metric.1 · trail: H1-05 §Adversarial critique · from: H1-05:C-063
- **dns.10** "The 148-dataset synthesis [48] is non-microbial" (or "non-microbial communities show lower functional decay on average").
  why: [48] includes diatoms and fungi (it lacks bacteria), which blurs the microbial vs non-microbial split the review uses · instead: other-habitats.9, other-habitats.12, null-model.10 · trail: H1-05 §critic, §Adversarial critique · from: H1-05:A-015, H1-05:A-077, H1-05:A-086, H1-05:A-101, H1-05:B-0088, H1-05:C-011, H1-05:C-055, H1-05:C-103
- **dns.11** "The wetland study [28] is a soil result" (as placed under Soil in D3).
  why: wetland sediment and soil are pooled in [28] without separating them · instead: null-model.4 · trail: H1-05 §Adversarial critique · from: H1-05:C-104
- **dns.12** "On the Changbai gradient, functional turnover was stronger than taxonomic turnover", as the study's result.
  why: the note says this is the reviewer's reading; the authors describe the patterns as similar, and the two r values come from different platforms and are not on a common scale · instead: ordering.22, ordering.23 · trail: H1-05 §1.3 · from: H1-05:B-0063, H1-05:B-0064, H1-05:B-0065
- **dns.13** "Unannotated genes are shown to bias soil turnover comparisons."
  why: the note says the varying unannotated fraction is indirect support for an annotation-bias critique, not a demonstration of its effect on turnover · instead: annotation.4, annotation.5 · trail: H1-05 §2 · from: H1-05:B-0099

## Gaps
- **gap.1** Bahram et al. 2018, the largest paired metabarcoding plus metagenome global topsoil set (shotgun plus amplicon on the same samples, global strong contrast), was not read beyond an abstract; the publisher was not tried, and the stage 2 check says it should be read in full by hand.
  blocks: ordering, covariation, functional-unit · origin: critic coverage gap; stage 2 check · src: bahramStructureFunctionGlobal2018 · from: H1-05:C-084, H1-05:B-0028
- **gap.2** Relic DNA on the taxonomic side: soil studies on its effect on taxonomic beta diversity exist and were not cited, while the review reports "not found" for relic-DNA critiques.
  blocks: measurement-artefacts · origin: critic coverage gap; stage 2 check · src: cariniRelicDNAAbundant2016, lennonHowWhereRelic2018, cariniEffectsSpatialVariability2020 · from: H1-05:C-085, H1-05:B-0026, H1-05:B-0007
- **gap.3** Sequencing depth and annotation-rate effects on functional-profile dissimilarity were not searched, and compositional (Aitchison, CLR) comparisons were reported as "not found" without naming the routes used.
  blocks: measurement-artefacts, metric · origin: critic coverage gap; stage 2 check · src: nayfachAverageGenomeSize2015 · from: H1-05:C-086, H1-05:B-0026
- **gap.4** Soil metatranscriptome turnover compared with taxonomic turnover: no study reported; forest-soil and rhizosphere metatranscriptome studies were not searched specifically, and soil metatranscriptome comparisons were not searched in depth.
  blocks: non-dna-function · origin: critic coverage gap; search record · from: H1-05:C-087, H1-05:C-089, H1-05:B-0021
- **gap.5** Recent soil chronosequence metagenome studies (a Greenlandic glacial chronosequence, ecosystem retrogression, and an ISME Communications 2026 study) are not assessed for paired turnover comparisons.
  blocks: chronosequence · origin: critic coverage gap; stage 2 check · src: anon2026, anon2026a, anon2026b · from: H1-05:C-090, H1-05:B-0025
- **gap.6** Chen et al. 2021a (water metagenomes, function-taxonomy similarity r2 0.3344, function lower), cited within [3], is not reported under other habitats.
  blocks: other-habitats · origin: critic coverage gap · src: chen2021 · from: H1-05:C-091
- **gap.7** The taxonomic side's measurement type (16S amplicon vs read-based RefSeq vs MAG) is not tabulated per study, although it plausibly affects the ordering.
  blocks: taxonomic-resolution, ordering · origin: critic coverage gap · from: H1-05:C-092
- **gap.8** Fungal shotgun turnover comparisons beyond [20] and [21], and archaeal and protist functional turnover in soil, are not addressed; fungi-specific shotgun comparisons were not measured.
  blocks: ordering, functional-unit · origin: critic coverage gap; answers (not measured) · src: pellitierPotentialFunctionalDivergence2024, talbotEndemismFunctionalConvergence2014 · from: H1-05:C-093, H1-05:A-028
- **gap.9** No per-study table gives measurement type, functional unit, annotation, dissimilarity measure and contrast, as the brief's Evidence-to-gather bullet requires.
  blocks: ordering, functional-unit, metric, contrast-size · origin: critic coverage gap; stage 2 check · from: H1-05:C-094, H1-05:B-0028
- **gap.10** The stage 2 check was triggered: write a follow-up brief, sized separately, on the habitat and data classes with shotgun results not assessed (soil chronosequence metagenomes, soil metatranscriptomes, fungal, archaeal and protist functional turnover in soil, aquatic MG-RAST comparisons) and on the per-study measurement table; no new null-model family with direct soil results was named.
  blocks: chronosequence, non-dna-function, other-habitats, ordering · origin: the note's stage 2 check · from: H1-05:B-0024, H1-05:B-0025, H1-05:B-0027, H1-05:B-0028
- **gap.11** Ho and Huang: the published Cell Systems body was not reached, so how its "extended null model" differs from the preprint is unknown; the preprint was read only as a fetch summary, although its bioRxiv full text is openly reachable.
  blocks: averaging · origin: answers (not measured); critic access finding · src: hoChallengesInterpretingFunctional2025, hoChallengesQuantifyingFunctional2024 · from: H1-05:A-094, H1-05:C-028, H1-05:C-049
- **gap.12** The Louca et al. originals were not reached in full text, so what their tests controlled for is known only from abstracts and from Ho and Huang's description.
  blocks: redundancy · origin: sources not obtained · src: loucaDecouplingFunctionTaxonomy2016, loucaHighTaxonomicVariability2016, loucaFunctionFunctionalRedundancy2018 · from: H1-05:A-098
- **gap.13** Sources read only as a fetch summary ([8], [30], [35], [49]) should be labelled secondary or abstract-level unless the text is read.
  blocks: covariation, ordering, other-habitats, null-model, averaging · origin: critic access errors · src: barnettDisturbanceIncreasesSoil2025, hoChallengesQuantifyingFunctional2024, burkeBacterialCommunityAssembly2011, swensonDeterministicTropicalTree2010 · from: H1-05:C-047, H1-05:C-048
- **gap.14** No field-soil null model on the functional-taxonomic difference, across any profile type or contrast size, was found.
  blocks: null-model, averaging · origin: "not found" in the answers and search record · from: H1-05:A-066, H1-05:A-092, H1-05:A-093, H1-05:B-0020
- **gap.15** In soil, no study compares dissimilarity measures, transforms or functional units finer than SEED (KO, COG, gene clusters) for the functional-taxonomic ordering.
  blocks: functional-unit, metric · origin: "not found" in the answers and search record · from: H1-05:A-053, H1-05:B-0094, H1-05:B-0020
- **gap.16** No soil study tests how the functional-taxonomic gap scales with environmental distance.
  blocks: contrast-size · origin: "not found" in the answers · from: H1-05:A-013, H1-05:A-026

## Out of scope
- H1-05:A-029..031: access basis of the D1 answer (provenance, kept in the result note)
- H1-05:A-060..062: access basis of the D2 answer (provenance, kept in the result note)
- H1-05:A-095..097: access basis of the D3 answer (provenance, kept in the result note)
- H1-05:C-033: the critic's check of figures against full text (verification, kept in the result note)
- H1-05:C-034: the critic's count of the over-reaches that follow (each is a do-not-say entry)
- H1-05:C-056..058: reference correction (Holland-Moritz in Crossref), applied in Sources
- H1-05:C-064..083: reference corrections, applied in Sources
- H1-05:C-107: the critic's note that the reviewer's synthesis does not evaluate a research design (scope check, not a finding)

## Sources

```bibtex
@article{fiererCrossbiomeMetagenomicAnalyses2012,
  author = {Fierer, Noah and Leff, Jonathan W. and Adams, Byron J. and Nielsen, Uffe N. and Bates, Scott Thomas and Lauber, Christian L. and Owens, Sarah and Gilbert, Jack A. and Wall, Diana H. and Caporaso, J. Gregory},
  title = {{Cross-biome metagenomic analyses of soil microbial communities and their functional attributes}},
  journal = {Proceedings of the National Academy of Sciences},
  year = {2012},
  volume = {109},
  number = {52},
  pages = {21390-21395},
  doi = {10.1073/pnas.1215210110},
  note = {access: full_text (via search agents; the critic confirmed the figures via PMC3535587, H1-05:C-052, C-053); cited as: H1-05 [1]}
}

@article{leffConsistentResponsesSoil2015,
  author = {Leff, Jonathan W. and Jones, Stuart E. and Prober, Suzanne M. and Barberán, Albert and Borer, Elizabeth T. and Firn, Jennifer L. and Harpole, W. Stanley and Hobbie, Sarah E. and Hofmockel, Kirsten S. and Knops, Johannes M. H. and McCulley, Rebecca L. and Pierre, Kimberly La and Risch, Anita C. and Seabloom, Eric W. and Schütz, Martin and Steenbock, Christopher and Stevens, Carly J. and Fierer, Noah},
  title = {{Consistent responses of soil microbial communities to elevated nutrient inputs in grasslands across the globe}},
  journal = {Proceedings of the National Academy of Sciences},
  year = {2015},
  volume = {112},
  number = {35},
  pages = {10967-10972},
  doi = {10.1073/pnas.1508382112},
  note = {access: full_text (via agents); the critic confirmed the figures via PMC4568213 (H1-05:C-052, C-053), the note said full_text (via agents); cited as: H1-05 [2]}
}

@article{chenFunctionalRedundancySoil2022,
  author = {Chen, Huaihai and Ma, Kayan and Lu, Caiyan and Fu, Qi and Qiu, Yingbo and Zhao, Jiayi and Huang, Yu and Yang, Yuchun and Schadt, Christopher W. and Chen, Hao},
  title = {{Functional redundancy in soil microbial community based on metagenomics across the globe}},
  journal = {Frontiers in Microbiology},
  year = {2022},
  volume = {13},
  pages = {878978},
  doi = {10.3389/fmicb.2022.878978},
  note = {access: full_text (rechecked by the reviewer); cited as: H1-05 [3]}
}

@article{igweRedundancyMaintainsMicrobial2026,
  author = {Igwe, Alexandria N. and Afkhami, Michelle E.},
  title = {{Redundancy maintains microbial ecosystem functional potential despite taxonomic shifts between serpentine and nonserpentine soils}},
  journal = {Microbial Genomics},
  year = {2026},
  volume = {12},
  number = {9},
  doi = {10.1099/mgen.0.001835},
  note = {access: full_text (rechecked by the reviewer); article number not in the Crossref record; Crossref gives vol 12 issue 9, published 2026-09-22, no article number (H1-05:C-082); cited as: H1-05 [4]}
}

@article{gaoLongtermWarmingMediterraneantype2021,
  author = {Gao, Ying and Ding, Junjun and Yuan, Mengting and Chiariello, Nona and Docherty, Kathryn and Field, Chris and Gao, Qun and Gu, Baohua and Gutknecht, Jessica and Hungate, Bruce A. and Roux, Xavier Le and Niboyet, Audrey and Qi, Qi and Shi, Zhou and Zhou, Jizhong and Yang, Yunfeng},
  title = {{Long-term warming in a Mediterranean-type grassland affects soil bacterial functional potential but not bacterial taxonomic composition}},
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
  title = {{Dramatic increases of soil microbial functional gene diversity at the treeline ecotone of Changbai Mountain}},
  journal = {Frontiers in Microbiology},
  year = {2016},
  volume = {7},
  pages = {1184},
  doi = {10.3389/fmicb.2016.01184},
  note = {access: full_text (via agents); cited as: H1-05 [6]}
}

@article{zhangSoilBacterialEndemism2016,
  author = {Zhang, Yuguang and Cong, Jing and Lu, Hui and Deng, Ye and Liu, Xiao and Zhou, Jizhong and Li, Diqiang},
  title = {{Soil bacterial endemism and potential functional redundancy in natural broadleaf forest along a latitudinal gradient}},
  journal = {Scientific Reports},
  year = {2016},
  volume = {6},
  pages = {28819},
  doi = {10.1038/srep28819},
  note = {access: full_text (via agents); cited as: H1-05 [7]}
}

@misc{barnettDisturbanceIncreasesSoil2025,
  author = {Barnett, Samuel E. and Shade, Ashley},
  title = {{Disturbance increases soil microbiome functional redundancy but decreases capacity for insurance via winnowed environmental responsiveness}},
  howpublished = {bioRxiv},
  year = {2025},
  doi = {10.1101/2025.09.19.677300},
  note = {access: secondary or abstract_only (critic: H1-05:C-047, C-048; the note said full_text (via fetch summary)); type: preprint (no published version found via Crossref or Europe PMC); cited as: H1-05 [8]}
}

@article{goodallTaxonomicFilteringAccompanies2026,
  author = {Goodall, Tim and Busi, Susheel Bhanu and Jones, Briony and Thorpe, Amy and Griffiths, Robert I and Redhead, John and Hulmes, Lucy and Hulmes, Sarah and Ridding, Lucy and Peyton, Jodey and Pereira, Gloria and Gweon, Hyun Soon and Read, Daniel S and Pywell, Richard},
  title = {{Taxonomic filtering accompanies functional expansion during long-term soil restoration}},
  journal = {The ISME Journal},
  year = {2026},
  volume = {20},
  number = {1},
  pages = {wrag131},
  doi = {10.1093/ismejo/wrag131},
  note = {access: full_text (via agents); cited as: H1-05 [9]}
}

@article{sveenFunctionalDiversitySoil2025,
  author = {Sveen, Tord Ranheim and Viketoft, Maria and Bengtsson, Jan and Strengbom, Joachim and Lejoly, Justine and Buegger, Franz and Pritsch, Karin and Fritscher, Joachim and Hildebrand, Falk and Osburn, Ernest and Hannula, S. Emilia and Bahram, Mo},
  title = {{Functional diversity of soil microbial communities increases with ecosystem development}},
  journal = {Nature Communications},
  year = {2025},
  volume = {16},
  number = {1},
  pages = {10408},
  doi = {10.1038/s41467-025-66544-8},
  note = {access: full_text (via agents); cited as: H1-05 [10]}
}

@article{liuReciprocalChangesDominant2023,
  author = {Liu, Huaiqiang and Li, Frank Yonghong and Liu, Jiayue and Shi, Chunjun and Tang, Kuanyan and Yang, Qianhui and Liu, Yu and Fu, Qiang and Gao, Xiaotian and Wang, Ning and Guo, Wei},
  title = {{The reciprocal changes in dominant species with complete metabolic functions explain the decoupling phenomenon of microbial taxonomic and functional composition in a grassland}},
  journal = {Frontiers in Microbiology},
  year = {2023},
  volume = {14},
  pages = {1113157},
  doi = {10.3389/fmicb.2023.1113157},
  note = {access: full_text (via agents); cited as: H1-05 [11]}
}

@article{nelsonGlobalBiogeographyMicrobial2016,
  author = {Nelson, Michaeline B. and Martiny, Adam C. and Martiny, Jennifer B. H.},
  title = {{Global biogeography of microbial nitrogen-cycling traits in soil}},
  journal = {Proceedings of the National Academy of Sciences},
  year = {2016},
  volume = {113},
  number = {29},
  pages = {8033-8040},
  doi = {10.1073/pnas.1601070113},
  note = {access: full_text (via agents); cited as: H1-05 [12]}
}

@article{panImpactLongtermN2014,
  author = {Pan, Yao and Cassman, Noriko and de Hollander, Mattias and Mendes, Lucas W. and Korevaar, Hein and Geerts, Rob H.E.M. and van Veen, Johannes A. and Kuramae, Eiko E.},
  title = {{Impact of long-term N, P, K, and NPK fertilization on the composition and potential functions of the bacterial community in grassland soil}},
  journal = {FEMS Microbiology Ecology},
  year = {2014},
  volume = {90},
  number = {1},
  pages = {195-205},
  doi = {10.1111/1574-6941.12384},
  note = {access: abstract_only; cited as: H1-05 [13]}
}

@article{yangDecouplingMicrobialCommunity2021,
  author = {Yang, Sizhong and Liebner, Susanne and Svenning, Mette Marianne and Tveit, Alexander Tøsdal},
  title = {{Decoupling of microbial community dynamics and functions in Arctic peat soil exposed to short term warming}},
  journal = {Molecular Ecology},
  year = {2021},
  volume = {30},
  number = {20},
  pages = {5094-5104},
  doi = {10.1111/mec.16118},
  note = {access: abstract_only; cited as: H1-05 [14]}
}

@article{maDivergentTaxonomicFunctional2017,
  author = {Ma, Xingyu and Zhao, Cancan and Gao, Ying and Liu, Bin and Wang, Tengxu and Yuan, Tong and Hale, Lauren and Nostrand, Joy D. Van and Wan, Shiqiang and Zhou, Jizhong and Yang, Yunfeng},
  title = {{Divergent taxonomic and functional responses of microbial communities to field simulation of aeolian soil erosion and deposition}},
  journal = {Molecular Ecology},
  year = {2017},
  volume = {26},
  number = {16},
  pages = {4186-4196},
  doi = {10.1111/mec.14194},
  note = {access: abstract_only; cited as: H1-05 [15]}
}

@article{freyLongtermMercuryContamination2022,
  author = {Frey, Beat and Rast, Basil M. and Qi, Weihong and Stierli, Beat and Brunner, Ivano},
  title = {{Long-term mercury contamination does not affect the microbial gene potential for C and N cycling in soils but enhances detoxification gene abundance}},
  journal = {Frontiers in Microbiology},
  year = {2022},
  volume = {13},
  pages = {1034138},
  doi = {10.3389/fmicb.2022.1034138},
  note = {access: abstract_only; cited as: H1-05 [16]}
}

@article{katoTimeseriesMetagenomicAnalysis2015,
  author = {Kato, Hiromi and Mori, Hiroshi and Maruyama, Fumito and Toyoda, Atsushi and Oshima, Kenshiro and Endo, Ryo and Fuchu, Genki and Miyakoshi, Masatoshi and Dozono, Ayumi and Ohtsubo, Yoshiyuki and Nagata, Yuji and Hattori, Masahira and Fujiyama, Asao and Kurokawa, Ken and Tsuda, Masataka},
  title = {{Time-series metagenomic analysis reveals robustness of soil microbiome against chemical disturbance}},
  journal = {DNA Research},
  year = {2015},
  volume = {22},
  number = {6},
  pages = {413-424},
  doi = {10.1093/dnares/dsv023},
  note = {access: abstract_only; cited as: H1-05 [17]}
}

@article{souzaMetagenomicAnalysisReveals2015,
  author = {Souza, Renata Carolini and Hungria, Mariangela and Cantão, Maurício Egídio and Vasconcelos, Ana Tereza Ribeiro and Nogueira, Marco Antonio and Vicente, Vânia Aparecida},
  title = {{Metagenomic analysis reveals microbial functional redundancies and specificities in a soil under different tillage and crop-management regimes}},
  journal = {Applied Soil Ecology},
  year = {2015},
  volume = {86},
  pages = {106-112},
  doi = {10.1016/j.apsoil.2014.10.010},
  note = {access: abstract_only; cited as: H1-05 [18]}
}

@article{chenStableSoilMicrobial2021,
  author = {Chen, Huaihai and Ma, Kayan and Huang, Yu and Yao, Zhiyuan and Chu, Chengjin},
  title = {{Stable soil microbial functional structure responding to biodiversity loss based on metagenomic evidences}},
  journal = {Frontiers in Microbiology},
  year = {2021},
  volume = {12},
  pages = {716764},
  doi = {10.3389/fmicb.2021.716764},
  note = {access: abstract_only; cited as: H1-05 [19]}
}

@article{pellitierPotentialFunctionalDivergence2024,
  author = {Pellitier, Peter T and Nuland, Michael Van and Salamov, Asaf and Grigoriev, Igor V and Peay, Kabir G},
  title = {{Potential for functional divergence in ectomycorrhizal fungal communities across a precipitation gradient}},
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
  title = {{Endemism and functional convergence across the North American soil mycobiome}},
  journal = {Proceedings of the National Academy of Sciences},
  year = {2014},
  volume = {111},
  number = {17},
  pages = {6341-6346},
  doi = {10.1073/pnas.1402584111},
  note = {access: abstract_only; cited as: H1-05 [21]}
}

@article{xuDistinctivePatternMechanism2022,
  author = {Xu, Minjie and Zhu, Xunzhi and Chen, Shiping and Pang, Shuang and Liu, Wei and Gao, Lili and Yang, Wei and Li, Tingting and Zhang, Yuhan and Luo, Chun and He, Dandan and Wang, Zhiping and Fan, Yi and Han, Xingguo and Zhang, Ximei},
  title = {{Distinctive pattern and mechanism of precipitation changes affecting soil microbial assemblages in the Eurasian steppe}},
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
  title = {{Land conversion to cropland homogenizes variation in soil biota, gene assemblages, and ecological strategies on local and regional scales}},
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
  title = {{Functional redundancy buffers the effect of poly-extreme environmental conditions on southern African dryland soil microbial communities}},
  journal = {FEMS Microbiology Ecology},
  year = {2024},
  volume = {100},
  number = {12},
  pages = {fiae157},
  doi = {10.1093/femsec/fiae157},
  note = {access: abstract_only for its result claim (critic: H1-05:C-051; the note said full_text (via agents, partly read)); cited as: H1-05 [24]}
}

@article{dineshSoilPollutedNano2023,
  author = {Dinesh, R. and Sreena, C.P. and Sheeja, T.E. and Kumar, I.P. Vijesh and Praveena, R. and Charles, Sona and Srinivasan, V. and Jayarajan, K. and Sajith, V. and Subila, K.P. and Haritha, P.},
  title = {{Soil polluted with nano ZnO reveals unstable bacterial communities and decoupling of taxonomic and functional diversities}},
  journal = {Science of the Total Environment},
  year = {2023},
  volume = {889},
  pages = {164285},
  doi = {10.1016/j.scitotenv.2023.164285},
  note = {access: abstract_only; cited as: H1-05 [25]}
}

@article{liAsynchronousPatternsSoil2024,
  author = {Li, Xianping and Li, Teng and Li, Huixin},
  title = {{Asynchronous patterns in soil bacterial diversity and functional potentials along an alpine altitudinal gradient}},
  journal = {Frontiers in Microbiology},
  year = {2024},
  volume = {15},
  pages = {1428815},
  doi = {10.3389/fmicb.2024.1428815},
  note = {access: full_text (via agents); cited as: H1-05 [26]}
}

@misc{hollandmoritzEcologicalPerspectiveMicrobial2021,
  author = {Holland-Moritz, Hannah and Vanni, Chiara and Fernandez-Guerra, Antonio and Bissett, Andrew and Fierer, Noah},
  title = {{An ecological perspective on microbial genes of unknown function in soil}},
  howpublished = {bioRxiv},
  year = {2021},
  doi = {10.1101/2021.12.02.470747},
  note = {access: abstract_only; type: preprint (no published version found via Crossref or Europe PMC); the note said the given names were not verified because the bioRxiv DOI is not in the Crossref works API; the critic (H1-05:C-056..058) found it is, with all five authors as listed; cited as: H1-05 [27]}
}

@article{zhangEnvironmentSelectedMicrobial2025,
  author = {Zhang, Hongjie and Zhao, Dayong and Wu, Qinglong L. and Zeng, Jin},
  title = {{Environment selected microbial function rather than taxonomic species in a plateau saline-alkaline wetland}},
  journal = {Applied and Environmental Microbiology},
  year = {2025},
  volume = {91},
  number = {7},
  pages = {e02206-24},
  doi = {10.1128/aem.02206-24},
  note = {access: full_text (via agents); cited as: H1-05 [28]}
}

@article{hoChallengesInterpretingFunctional2025,
  author = {Ho, Po-Yi and Huang, Kerwyn Casey},
  title = {{Challenges in interpreting functional redundancy and quantifying functional selection in microbial communities}},
  journal = {Cell Systems},
  year = {2025},
  volume = {16},
  number = {8},
  pages = {101350},
  doi = {10.1016/j.cels.2025.101350},
  note = {access: abstract_only; the published full text is listed under Sources not obtained (cell.com HTTP 403; not in PMC); cited as: H1-05 [29]}
}

@misc{hoChallengesQuantifyingFunctional2024,
  author = {Ho, Po-Yi and Huang, Kerwyn Casey},
  title = {{Challenges in quantifying functional redundancy and selection in microbial communities}},
  howpublished = {bioRxiv},
  year = {2024},
  doi = {10.1101/2024.03.26.586891},
  note = {access: secondary or abstract_only (critic: H1-05:C-047, C-048; the note said full_text (via fetch summary)); type: preprint (v1); the critic (H1-05:C-049) says the bioRxiv full text is openly reachable; cited as: H1-05 [30]}
}

@article{galandStrongLinkMarine2018,
  author = {Galand, Pierre E. and Pereira, Olivier and Hochart, Corentin and Auguet, Jean Christophe and Debroas, Didier},
  title = {{A strong link between marine microbial community composition and function challenges the idea of functional redundancy}},
  journal = {The ISME Journal},
  year = {2018},
  volume = {12},
  number = {10},
  pages = {2470-2478},
  doi = {10.1038/s41396-018-0158-1},
  note = {access: full_text (via agents); cited as: H1-05 [31]}
}

@article{loucaDecouplingFunctionTaxonomy2016,
  author = {Louca, Stilianos and Parfrey, Laura Wegener and Doebeli, Michael},
  title = {{Decoupling function and taxonomy in the global ocean microbiome}},
  journal = {Science},
  year = {2016},
  volume = {353},
  number = {6305},
  pages = {1272-1277},
  doi = {10.1126/science.aaf4507},
  note = {access: abstract_only; full text listed under Sources not obtained (nature.com paywall; abstracts used); cited as: H1-05 [32]}
}

@article{loucaHighTaxonomicVariability2016,
  author = {Louca, Stilianos and Jacques, Saulo M. S. and Pires, Aliny P. F. and Leal, Juliana S. and Srivastava, Diane S. and Parfrey, Laura Wegener and Farjalla, Vinicius F. and Doebeli, Michael},
  title = {{High taxonomic variability despite stable functional structure across microbial communities}},
  journal = {Nature Ecology \& Evolution},
  year = {2017},
  volume = {1},
  number = {1},
  pages = {0015},
  doi = {10.1038/s41559-016-0015},
  note = {access: abstract_only; online 5 December 2016; full text listed under Sources not obtained (abstracts used); the critic (H1-05:C-076..078) says Crossref gives pages 1-12, article number 0015; cited as: H1-05 [33]}
}

@article{loucaFunctionFunctionalRedundancy2018,
  author = {Louca, Stilianos and Polz, Martin F. and Mazel, Florent and Albright, Michaeline B. N. and Huber, Julie A. and O'Connor, Mary I. and Ackermann, Martin and Hahn, Aria S. and Srivastava, Diane S. and Crowe, Sean A. and Doebeli, Michael and Parfrey, Laura Wegener},
  title = {{Function and functional redundancy in microbial systems}},
  journal = {Nature Ecology \& Evolution},
  year = {2018},
  volume = {2},
  number = {6},
  pages = {936-943},
  doi = {10.1038/s41559-018-0519-1},
  note = {access: abstract_only; full text listed under Sources not obtained (abstracts used); cited as: H1-05 [34]}
}

@article{burkeBacterialCommunityAssembly2011,
  author = {Burke, Catherine and Steinberg, Peter and Rusch, Doug and Kjelleberg, Staffan and Thomas, Torsten},
  title = {{Bacterial community assembly based on functional genes rather than species}},
  journal = {Proceedings of the National Academy of Sciences},
  year = {2011},
  volume = {108},
  number = {34},
  pages = {14288-14293},
  doi = {10.1073/pnas.1101591108},
  note = {access: secondary or abstract_only (critic: H1-05:C-047, C-048; the note said full_text (via fetch summary)); cited as: H1-05 [35]}
}

@article{vanderloosLowFunctionalChange2025,
  author = {van der Loos, Luna M. and Steinhagen, Sophie and Stock, Willem and Weinberger, Florian and D'hondt, Sofie and Willems, Anne and De Clerck, Olivier},
  title = {{Low functional change despite high taxonomic turnover characterizes the Ulva microbiome across a 2000-km salinity gradient}},
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
  title = {{Taxonomic variability and functional stability across Oregon coastal subsurface microbiomes}},
  journal = {Communications Biology},
  year = {2024},
  volume = {7},
  number = {1},
  pages = {1663},
  doi = {10.1038/s42003-024-07384-y},
  note = {access: full_text (via agents); cited as: H1-05 [37]}
}

@article{lemoigneLinkingStochasticAssembly2026,
  author = {Moigne, Alizée Le and Andrei, Adrian-Ştefan and Pernthaler, Jakob},
  title = {{Linking stochastic assembly to functional potential, redundancy, and trait patterns in bacterial communities}},
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
  title = {{Press disturbance alters community structure and assembly mechanisms of bacterial taxa and functional genes in mesocosm-scale bioreactors}},
  journal = {mSystems},
  year = {2020},
  volume = {5},
  number = {4},
  pages = {e00471-20},
  doi = {10.1128/mSystems.00471-20},
  note = {access: abstract_only; the bioRxiv preprint is a separate entry; cited as: H1-05 [39]}
}

@article{tianDecipheringFunctionalRedundancy2020,
  author = {Tian, Liang and Wang, Xu-Wen and Wu, Ang-Kun and Fan, Yuhang and Friedman, Jonathan and Dahlin, Amber and Waldor, Matthew K. and Weinstock, George M. and Weiss, Scott T. and Liu, Yang-Yu},
  title = {{Deciphering functional redundancy in the human microbiome}},
  journal = {Nature Communications},
  year = {2020},
  volume = {11},
  number = {1},
  pages = {6217},
  doi = {10.1038/s41467-020-19940-1},
  note = {access: full_text (via agents); cited as: H1-05 [40]}
}

@article{liRevealingProteomelevelFunctional2023,
  author = {Li, Leyuan and Wang, Tong and Ning, Zhibin and Zhang, Xu and Butcher, James and Serrana, Joeselle M. and Simopoulos, Caitlin M. A. and Mayne, Janice and Stintzi, Alain and Mack, David R. and Liu, Yang-Yu and Figeys, Daniel},
  title = {{Revealing proteome-level functional redundancy in the human gut microbiome using ultra-deep metaproteomics}},
  journal = {Nature Communications},
  year = {2023},
  volume = {14},
  number = {1},
  pages = {3428},
  doi = {10.1038/s41467-023-39149-2},
  note = {access: full_text (via agents); cited as: H1-05 [41]}
}

@article{goldfordEmergentSimplicityMicrobial2018,
  author = {Goldford, Joshua E. and Lu, Nanxi and Bajić, Djordje and Estrela, Sylvie and Tikhonov, Mikhail and Sanchez-Gorostiaga, Alicia and Segrè, Daniel and Mehta, Pankaj and Sanchez, Alvaro},
  title = {{Emergent simplicity in microbial community assembly}},
  journal = {Science},
  year = {2018},
  volume = {361},
  number = {6401},
  pages = {469-474},
  doi = {10.1126/science.aat1168},
  note = {access: abstract_only; cited as: H1-05 [42]}
}

@article{estrelaFunctionalAttractorsMicrobial2022,
  author = {Estrela, Sylvie and Vila, Jean C.C. and Lu, Nanxi and Bajić, Djordje and Rebolleda-Gómez, Maria and Chang, Chang-Yu and Goldford, Joshua E. and Sanchez-Gorostiaga, Alicia and Sánchez, Álvaro},
  title = {{Functional attractors in microbial community assembly}},
  journal = {Cell Systems},
  year = {2022},
  volume = {13},
  number = {1},
  pages = {29-42.e7},
  doi = {10.1016/j.cels.2021.09.011},
  note = {access: abstract_only; not cited (listed in the D3 access line only); cited as: H1-05 [43]}
}

@article{jourdainEnvironmentalSelectionConstrains2026,
  author = {Jourdain, Lisa and Leininger, Aaron and Pacheco, Alan R and Gu, Wenyu},
  title = {{Environmental selection constrains metabolic network architecture despite taxonomic turnover in anaerobic digestion communities}},
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
  title = {{Faster turnover of taxonomic over functional bacterial composition during vermicomposting indicates increasing functional redundancy}},
  journal = {PLOS One},
  year = {2026},
  volume = {21},
  number = {7},
  pages = {e0354276},
  doi = {10.1371/journal.pone.0354276},
  note = {access: full_text (via agents); cited as: H1-05 [45]}
}

@article{renComparisonMicrobialTaxonomic2016,
  author = {Ren, Youhua and Niu, Jiaojiao and Huang, Wenkun and Peng, Deliang and Xiao, Yunhua and Zhang, Xian and Liang, Yili and Liu, Xueduan and Yin, Huaqun},
  title = {{Comparison of microbial taxonomic and functional shift pattern along contamination gradient}},
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
  title = {{Average genome size estimation improves comparative metagenomics and sheds light on the functional ecology of the human microbiome}},
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
  title = {{Distance decay 2.0: A global synthesis of taxonomic and functional turnover in ecological communities}},
  journal = {Global Ecology and Biogeography},
  year = {2022},
  volume = {31},
  number = {7},
  pages = {1399-1421},
  doi = {10.1111/geb.13513},
  note = {access: full_text (via agents); the critic (H1-05:C-055) says it is openly available (PMC9322010); Crossref lists 92 authors (C-079..081); published title separates "2.0" and "A" with a dash; cited as: H1-05 [48]}
}

@article{swensonDeterministicTropicalTree2010,
  author = {Swenson, Nathan G. and Anglada-Cordero, Pedro and Barone, John A.},
  title = {{Deterministic tropical tree community turnover: evidence from patterns of functional beta diversity along an elevational gradient}},
  journal = {Proceedings of the Royal Society B: Biological Sciences},
  year = {2011},
  volume = {278},
  number = {1707},
  pages = {877-884},
  doi = {10.1098/rspb.2010.1369},
  note = {access: secondary or abstract_only (critic: H1-05:C-047, C-048; the note said full_text (via fetch summary)); cited as: H1-05 [49]}
}

@article{villegerDecomposingFunctionalDiversity2013,
  author = {Villéger, Sébastien and Grenouillet, Gaël and Brosse, Sébastien},
  title = {{Decomposing functional β-diversity reveals that low functional β-diversity is driven by low functional turnover in European fish assemblages}},
  journal = {Global Ecology and Biogeography},
  year = {2013},
  volume = {22},
  number = {6},
  pages = {671-681},
  doi = {10.1111/geb.12021},
  note = {access: abstract_only; full text listed under Sources not obtained (a Zenodo copy listed by OpenAlex was not fetched; abstract used); cited as: H1-05 [50]}
}

@article{villegerFunctionalHomogenizationExceeds2014,
  author = {Villéger, Sébastien and Grenouillet, Gaël and Brosse, Sébastien},
  title = {{Functional homogenization exceeds taxonomic homogenization among European fish assemblages}},
  journal = {Global Ecology and Biogeography},
  year = {2014},
  volume = {23},
  number = {12},
  pages = {1450-1460},
  doi = {10.1111/geb.12226},
  note = {access: abstract_only; cited as: H1-05 [51]}
}

@article{ramirezflandesRedoxTraitsCharacterize2019,
  author = {Ram{\'i}rez-Flandes, Salvador and Gonz{\'a}lez, Bernardo and Ulloa, Osvaldo},
  title = {{Redox traits characterize the organization of global microbial communities}},
  journal = {Proceedings of the National Academy of Sciences USA},
  volume = {116},
  number = {9},
  pages = {3630-3635},
  year = {2019},
  doi = {10.1073/pnas.1817554116},
  note = {access: not_obtained (known only as described in Chen et al. 2022, secondary; no direct EPMC/Crossref lookup performed because of time budget); names and accents and the DOI as corrected by the critic (H1-05:C-065); not cited; listed under Sources not obtained}
}

@article{bahramStructureFunctionGlobal2018,
  author = {Bahram, Mohammad and Hildebrand, Falk and Forslund, S. K. and others},
  title = {{Structure and function of the global topsoil microbiome}},
  journal = {Nature},
  volume = {560},
  number = {7717},
  pages = {233-237},
  year = {2018},
  doi = {10.1038/s41586-018-0386-6},
  note = {access: not_obtained (Europe PMC abstract obtained; no PMC full text; publisher not tried); listed twice under Sources not obtained, once with the first author as 'Mayra'; the critic (H1-05:C-064) gives 'Mohammad', 21 authors, last author Peer Bork; incomplete: author; not cited}
}

@article{fiererReconstructingMicrobialDiversity2013,
  author = {Fierer, Noah and Ladau, Joshua and Clemente, Jose C. and Leff, J. W. and Owens, S. M. and Pollard, K. S. and Knight, R. and Gilbert, Jack A. and McCulley, Rebecca L.},
  title = {{Reconstructing the microbial diversity and function of pre-agricultural tallgrass prairie soils in the United States}},
  journal = {Science},
  volume = {342},
  number = {6158},
  pages = {621-624},
  year = {2013},
  doi = {10.1126/science.1243768},
  note = {access: not_obtained (Europe PMC abstract only; no PMC copy); listed twice under Sources not obtained, once as 'Noah Fierer et al.'; the critic (H1-05:C-066..071) lists 9 authors, given names partly given; not cited}
}

@article{jiaNewPerspectiveFunctional2020,
  author = {Jia, Yu and Whalen, Joann K.},
  title = {{A new perspective on functional redundancy and phylogenetic niche conservatism in soil microbial communities}},
  journal = {Pedosphere},
  volume = {30},
  number = {1},
  pages = {18-24},
  year = {2020},
  doi = {10.1016/S1002-0160(19)60826-X},
  note = {access: not_obtained (Crossref metadata only, no abstract; not in Europe PMC; no open copy found); listed twice under Sources not obtained; the critic (H1-05:C-072..074) finds no error; not cited}
}

@misc{santillan2019,
  author = {Santillan, Ezequiel and others},
  howpublished = {bioRxiv (preprint)},
  year = {2019},
  doi = {10.1101/805788},
  note = {access: abstract_only; type: preprint of H1-05 [39]; cited as: H1-05 [39]; incomplete: title, author}
}

@article{cariniRelicDNAAbundant2016,
  author = {Carini, P. and others},
  journal = {Nature Microbiology},
  year = {2016},
  doi = {10.1038/nmicrobiol.2016.242},
  note = {access: not stated (named by the critic in a coverage gap on relic DNA, H1-05:C-085; not read by the review); incomplete: author, title, volume, pages}
}

@article{lennonHowWhereRelic2018,
  author = {Lennon, J. T. and others},
  journal = {mBio},
  year = {2018},
  doi = {10.1128/mbio.00637-18},
  note = {access: not stated (named by the critic in a coverage gap on relic DNA, H1-05:C-085; not read by the review); incomplete: author, title, volume, pages}
}

@article{cariniEffectsSpatialVariability2020,
  journal = {mBio},
  year = {2020},
  doi = {10.1128/mbio.02776-19},
  note = {access: not stated (named by the critic in a coverage gap on relic DNA, H1-05:C-085; not read by the review); incomplete: author, title, volume, pages}
}

@article{anon2026,
  journal = {FEMS Microbiology Ecology},
  year = {2026},
  doi = {10.1093/femsec/fiag054},
  note = {access: not stated (named by the critic, H1-05:C-090, as a Greenlandic glacial chronosequence metagenome study not assessed); incomplete: author, title, volume, pages}
}

@article{anon2026a,
  journal = {mLife},
  year = {2026},
  doi = {10.1002/mlf2.70087},
  note = {access: not stated (named by the critic, H1-05:C-090, as an ecosystem retrogression metagenome study not assessed); incomplete: author, title, volume, pages}
}

@article{anon2026b,
  journal = {ISME Communications},
  year = {2026},
  doi = {10.1093/ismeco/ycag157},
  note = {access: not stated (named by the critic, H1-05:C-090, as a chronosequence metagenome study not assessed); incomplete: author, title, volume, pages}
}

@article{chen2021,
  author = {Chen, H. and others},
  year = {2021},
  note = {access: not stated (named by the critic, H1-05:C-091, as Chen et al. 2021a, water metagenomes, cited within H1-05 [3]); incomplete: author, title, journal, volume, pages, doi}
}

@article{allisonResistanceResilienceRedundancy2008,
  author = {Allison, Steven D. and Martiny, Jennifer B. H.},
  title = {{Resistance, resilience, and redundancy in microbial communities}},
  journal = {Proceedings of the National Academy of Sciences},
  volume = {105},
  number = {Supplement 1},
  pages = {11512-11519},
  year = {2008},
  doi = {10.1073/pnas.0801925105},
  note = {background; access: full_text (PMC2556421)}
}

@article{andersonNewMethodNonparametric2001,
  author = {Anderson, Marti J.},
  title = {{A new method for non-parametric multivariate analysis of variance}},
  journal = {Austral Ecology},
  volume = {26},
  number = {1},
  pages = {32-46},
  year = {2001},
  doi = {10.1111/j.1442-9993.2001.01070.pp.x},
  note = {background; access: abstract_only (Crossref record)}
}
```
