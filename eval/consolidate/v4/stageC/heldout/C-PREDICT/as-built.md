---
type: knowledge
title: Held-out prediction of taxonomic versus gene or trait profiles from environment
inputs:
  - C-PREDICT: PhD/Proposal/Research/Results/Held-out prediction of taxonomic versus gene or trait community profiles from environment a literature review.md
refs: PhD/Proposal/Refs/Refs.bib
built: 2026-10-24
status: draft
tags:
  - research
  - knowledge
---
# Held-out prediction of taxonomic versus gene or trait profiles from environment

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
| C-PREDICT | [[Held-out prediction of taxonomic versus gene or trait community profiles from environment a literature review]] | yes | narrative author-year | no | no | fallback |

## Concepts

### profile-types: taxonomic, measured gene and derived functional profiles
needs: none
- **profile-types.1** The comparison the research asked for predicts both a taxonomic profile and a gene or trait profile from environment and scores both at units not used in fitting; a measured gene profile is metagenomic genes, pathways or categories, while a derived functional profile is obtained from taxonomy by assigning genera to functions (genus-to-function lookup).
  conf: not stated · class: not stated · holds: the review's terms · src: none (the review's definitions) · trail: C-PREDICT §What the direct evidence · from: C-PREDICT:B-0025..0027, C-PREDICT:A-006

### hold-out-design: hold-out design and transferability
needs: none
- **hold-out-design.1** Hold-out design changes apparent skill: Norberg et al., benchmarking 33 stacked and joint SDMs on five plant and animal datasets, found extrapolation much harder than interpolation, and the prediction task explained 29% of variance in performance, model variant 33% and data properties 38%.
  conf: not stated · class: not stated · holds: five plant and animal datasets, 33 stacked and joint species distribution models · src: norbergComprehensiveEvaluationPredictive2019 (full text via search agents, not re-opened by the synthesis) · trail: C-PREDICT §Transferability, bounds, §Adversarial critique · from: C-PREDICT:B-0119..0121, C-PREDICT:C-058
- **hold-out-design.2** Wenger and Olden found machine-learning models with excellent in-sample fit transferred poorly under blocked cross-validation.
  conf: not stated · class: not stated · holds: machine-learning ecological models under blocked cross-validation · src: wengerAssessingTransferabilityEcological2012 (abstract only) · trail: C-PREDICT §Transferability, bounds · from: C-PREDICT:B-0122, C-PREDICT:R-0271
- **hold-out-design.3** Random splits overstate transfer relative to blocked or extrapolative splits; in Norberg et al. the prediction task explained 29% of variance in performance.
  conf: repl (note: "replicated in SDM work") · class: not stated · holds: the species distribution model literature · src: wengerAssessingTransferabilityEcological2012, norbergComprehensiveEvaluationPredictive2019 · trail: C-PREDICT §Answers as delivered, §critic · rating: "Moderate" · from: C-PREDICT:A-062, C-PREDICT:A-064, C-PREDICT:C-030
- **hold-out-design.4** Maguire et al. 2016 found both species and community models failed across distant, climatically novel periods; its abstract also reports that community-level models generally outperformed SDMs in novel climates (transferring better than species models) and did not overfit.
  conf: not stated · class: not stated · holds: distant, climatically novel periods; taxonomic profiles only · src: maguireControlledComparisonSpecies2016 (abstract only; verified by the critic) · trail: C-PREDICT §Transferability, bounds, §Adversarial critique · from: C-PREDICT:B-0123, C-PREDICT:C-099..101, C-PREDICT:A-068, C-PREDICT:R-0277
- **hold-out-design.5** Zurell et al. 2020 found stacking choices mattered more than model type.
  conf: not stated · class: not stated · holds: stacking choices; taxonomic profiles only · src: zurell2020 · trail: C-PREDICT §Answers as delivered · from: C-PREDICT:A-068
- **hold-out-design.6** Microbial held-out studies mostly used random, not site-blocked, splits (Liu 2023, Faure 2021, Frémont 2022, Mod 2021) or evaluated in-sample (Fuhrman et al. 2006), and Werbin's functional-versus-taxonomic contrast is a within-site temporal test.
  conf: not stated · class: not stated · holds: microbial held-out prediction studies · src: liuPredictingMicrobialCommunity2023, faureTowardsOmicsbasedPredictions2021, fremontRestructuringPlanktonGenomic2022, modPredictingSpatialPatterns2021, fuhrmanAnnuallyReoccurringBacterial2006, werbinForecastingSoilMicrobiome2024 · trail: C-PREDICT §Transferability, bounds, §Answers as delivered · from: C-PREDICT:B-0124, C-PREDICT:A-063, C-PREDICT:R-0113
- **hold-out-design.7** The clearest microbial failure bounds found are the one spatial transfer result in Werbin (bacteria losing 65% of CRPS skill at new sites) and the zero median 1:1 R2 in Averill's cross-study test, where the median is 0 for every group except fungal functional groups, though about 21 of 130 groups have a positive 1:1 R2.
  conf: not stated · class: not stated · holds: soil microbes, NEON; new-site transfer (Werbin) and cross-study transfer (Averill) · src: werbinForecastingSoilMicrobiome2024, averillSoilMicrobiomePredictability2021 · trail: C-PREDICT §Transferability, bounds, §critic, §Adversarial critique · limit: access (critic: C-059) · from: C-PREDICT:B-0031, C-PREDICT:B-0057, C-PREDICT:B-0125, C-PREDICT:C-031, C-PREDICT:C-059

### skill-measures: skill measures and baselines
needs: none
- **skill-measures.bg1** The continuous ranked probability score (CRPS) is a proper scoring rule for probabilistic forecasts that take the form of predictive cumulative distribution functions; it generalises the absolute error.
  kind: background · ref: gneitingStrictlyProperScoring2007 · check: DOI 10.1198/016214506000001437 resolves on Crossref (JASA 102(477):359-378); stated in the abstract
- **skill-measures.1** Averill et al.'s supplementary table reports two measures of out-of-sample skill: R2 of the best-fit line between predicted and observed, and R2 against the 1:1 line.
  conf: not stated · class: not stated · holds: Averill et al. 2021 Supplementary Data 1 · src: averillSoilMicrobiomePredictability2021 (supplement full text) · trail: C-PREDICT §What the direct evidence · from: C-PREDICT:B-0034, C-PREDICT:B-0035
- **skill-measures.2** Skill measure and baseline can reverse or erase apparent skill: under the two measures in Averill et al. the orderings change, with high correlation alongside zero 1:1 skill; in microbes this measure-reversal finding rests on Averill et al. 2021 alone.
  conf: single (note: "Weak (single study) for every property shown on derived functional profiles and for the measure-dependent verdict in microbes") · class: not stated · holds: soil microbes, cross-study transfer (Averill) · src: averillSoilMicrobiomePredictability2021 · trail: C-PREDICT §Answers as delivered, §Properties that raise, §critic · rating: "Weak (single study)" · from: C-PREDICT:A-054, C-PREDICT:A-065, C-PREDICT:A-072, C-PREDICT:B-0031, C-PREDICT:B-0141, C-PREDICT:C-031
- **skill-measures.3** No microbial study reported skill over a mean-profile or persistence baseline for both profile types.
  conf: not stated · class: search (note: "no microbial study reported skill over a mean-profile baseline for both profile types") · holds: microbial held-out prediction · src: none (the review's search) · trail: C-PREDICT §Answers as delivered · search: not stated · from: C-PREDICT:A-061, C-PREDICT:A-069

### direct-evidence: same-study held-out comparisons with measured gene profiles
needs: profile-types, hold-out-design
- **direct-evidence.1** No study was found that predicts a measured metagenomic gene or trait profile and a measured taxonomic profile from environment and compares their skill at held-out sites, habitats, studies or times (Case A: no evidence found).
  conf: not stated · class: search (note: "None of the three found, by these routes") · holds: three blind search angles (microbial ecology; species distribution and bioassessment transferability; trait-based community ecology); routes that worked: Europe PMC REST, Crossref REST, Unpaywall, publisher, preprint and repository PDFs, Research Square, UNIL repositories, the USGS Pubs Warehouse and the biblion SQL corpus; all three angles reported WebSearch exhausted, a Scholar Gateway identity error, rate-limited Semantic Scholar and OpenAlex and a failed biblion semantic search · src: none (the review's search) · trail: C-PREDICT §What the direct evidence, §Search record, §Provenance, §critic · search: searched, not found (note: "None of the three found, by these routes") · from: C-PREDICT:A-002, C-PREDICT:A-005, C-PREDICT:C-001, C-PREDICT:B-0009..0012, C-PREDICT:B-0026, C-PREDICT:B-0144..0148
- **direct-evidence.2** Not measured: spatially blocked or habitat-held-out comparisons, and any comparison referenced to a null or mean-profile baseline for both profile types in one study.
  conf: not stated · class: search (note: "Not measured") · holds: taxonomic versus gene or trait profiles at held-out units · src: none (the review's search) · trail: C-PREDICT §Answers as delivered · search: not stated · from: C-PREDICT:A-021
- **direct-evidence.3** Not measured: earlier-period (hindcast) and interleaved temporal hold-out designs for either comparison; these designs, and long-term microbial time series predicted out of period, were not searched for either profile type.
  conf: not stated · class: search (note: "Not measured") · holds: temporal hold-out designs · src: none (the review's search) · trail: C-PREDICT §Answers as delivered, §Adversarial critique · search: not searched (critic: C-095) · from: C-PREDICT:A-021, C-PREDICT:C-095
- **direct-evidence.4** Not measured: freshwater, sediment and host-free engineered systems beyond activated sludge; the search record does not name the query routes used for these settings.
  conf: not stated · class: search (note: "Not measured") · holds: freshwater, sediment and engineered microbial systems · src: none (the review's search) · trail: C-PREDICT §Answers as delivered, §Adversarial critique · search: not stated (critic: C-092) · from: C-PREDICT:A-021, C-PREDICT:C-092
- **direct-evidence.5** Not measured: marine systems; marine measured metagenomic and metatranscriptomic prediction beyond Faure 2021 was not searched as held-out prediction of gene profiles.
  conf: not stated · class: search (note: "Not measured") · holds: marine microbial measured gene profiles · src: none (the review's search) · trail: C-PREDICT §Answers as delivered, §Adversarial critique · search: not searched (critic: C-091) · from: C-PREDICT:A-021, C-PREDICT:C-091
- **direct-evidence.6** Not measured: any same-study held-out trait versus taxon comparison in plants or animals; the trait-based SDM transferability literature and the fourth-corner and HMSC trait-environment prediction work were not searched.
  conf: not stated · class: search (note: "Not measured") · holds: plant and animal community ecology · src: none (the review's search) · trail: C-PREDICT §Answers as delivered, §Adversarial critique · search: not searched (critic: C-089) · from: C-PREDICT:A-021, C-PREDICT:C-089

### averill: Averill et al. 2021, a cross-study hold-out
needs: profile-types, hold-out-design, skill-measures
- **averill.1** Averill et al. 2021 calibrated Bayesian models of soil bacterial (16S) and fungal (ITS) group abundances on global surveys, using climate, soil and vegetation predictors, and validated them on the independent NEON survey across the continental USA at core, plot and site scales: a cross-study hold-out.
  conf: single (note: "Standing: SINGLE SOURCE") · class: meas (note: "Evidence class: measured") · holds: continental USA soils, cross-study transfer · src: averillSoilMicrobiomePredictability2021 (abstract plus supplementary data table; main text not read) · trail: C-PREDICT §What the direct evidence, §Answers as delivered · from: C-PREDICT:B-0031, C-PREDICT:B-0032, C-PREDICT:B-0050..0052, C-PREDICT:A-022
- **averill.2** Averill et al. conclude that "biogeochemical functional groups and high-level taxonomic groups of microorganisms were equally predictable", that predictability rose with spatial scale, and that fungal predictability rose with taxonomic scale; the equal-predictability claim compares functional groups with high-level taxonomic groups, not with all ranks.
  conf: not stated · class: not stated · holds: soil microbes, NEON validation; the authors' abstract (main text paywalled, not read by any agent; quote verified verbatim by the critic) · src: averillSoilMicrobiomePredictability2021 (abstract only) · trail: C-PREDICT §What the direct evidence, §critic · from: C-PREDICT:B-0031, C-PREDICT:B-0033, C-PREDICT:A-008, C-PREDICT:A-035, C-PREDICT:C-004, C-PREDICT:C-045
- **averill.3** From Averill et al.'s Supplementary Data 1, median site-scale out-of-sample R2 (best-fit; 1:1) by group: bacteria phylum (10 groups) 0.23 to 0.30; 0.00, class (10) 0.30 to 0.35; 0.00, order (10) 0.51; 0.00, family (10) 0.32; 0.00, genus (10) 0.35; 0.00, bacterial derived functional (13) 0.15; 0.00; fungi phylum (4) 0.12; 0.00, class (9) 0.01; 0.00, order (19) 0.11; 0.00, family (20) 0.13; 0.00, genus (15) 0.08; 0.00, fungal derived functional (5) 0.23; 0.11. The ranges cover both ways of resolving duplicate rows for taxa whose names occur at two ranks; the derived functional medians were unaffected. The critic's recomputation matches (bacterial phylum 0.27, class 0.33, order 0.51, family 0.315, genus 0.355, functional 0.15; fungal functional 0.23 best-fit and 0.11 on the 1:1 line; all other 1:1 medians 0).
  conf: single (note: "Standing: SINGLE SOURCE") · class: meas (note: "Evidence class: measured") · holds: continental USA soils, site scale, cross-study transfer; recomputed by the reviewer from the supplement · src: averillSoilMicrobiomePredictability2021 (supplement full text, re-opened by the reviewer) · trail: C-PREDICT §What the direct evidence, §Provenance, §critic · from: C-PREDICT:B-0013, C-PREDICT:B-0014, C-PREDICT:B-0034, C-PREDICT:B-0036..0052, C-PREDICT:C-042
- **averill.4** Against phylum at site scale, Averill et al.'s supplement gives a split by kingdom: bacterial functional median best-fit R2 is 0.15 against 0.27 for phyla, and fungal functional 0.23 against 0.12 for phyla; so the reviewer's reading departs from the authors for bacteria only, not for both kingdoms.
  conf: not stated · class: not stated · holds: site scale, recomputed by the critic, matching the review's numbers · src: averillSoilMicrobiomePredictability2021 (supplement) · trail: C-PREDICT §critic · from: C-PREDICT:C-005, C-PREDICT:C-006, C-PREDICT:C-047
- **averill.5** Reviewer's reading, labelled as such: bacterial derived functional groups were the least predictable bacterial category by best-fit R2 (0.15 against 0.23 to 0.51 for ranks), and fungal functional groups the most predictable fungal category (0.23 against 0.01 to 0.13); this reading sets the functional groups against all taxonomic ranks, not the high-level groups the authors named.
  conf: not stated · class: reading (note: "Reviewer's reading, labelled as such") · holds: site scale, best-fit R2 · src: averillSoilMicrobiomePredictability2021 (supplement) · trail: C-PREDICT §What the direct evidence, §Answers as delivered, §critic · from: C-PREDICT:B-0052, C-PREDICT:A-009, C-PREDICT:C-047
- **averill.6** Under the 1:1 measure in Averill et al.'s cross-study transfer, median site-scale R2 is 0 for every group except fungal functional groups (0.11), but about 21 of 130 groups have a positive 1:1 R2 (for example Bacteroidetes 0.50).
  conf: not stated · class: not stated · holds: site scale, R2 against the 1:1 line; confirmed by the critic · src: averillSoilMicrobiomePredictability2021 (supplement) · trail: C-PREDICT §Answers as delivered, §critic · from: C-PREDICT:A-009, C-PREDICT:C-031
- **averill.7** In the reviewer's recomputation of Averill et al.'s site-scale medians, bacteria peak at order (0.51) with phylum lowest (0.23 to 0.30 depending on how duplicated rows are handled), and fungal medians do not rise cleanly with rank (phylum 0.12, class 0.01, order 0.11, family 0.13, genus 0.08).
  conf: single (note: "Each rank finding is single-study") · class: not stated · holds: site scale, best-fit R2 · src: averillSoilMicrobiomePredictability2021 (supplement) · trail: C-PREDICT §What the direct evidence, §Answers as delivered · from: C-PREDICT:B-0053, C-PREDICT:A-035, C-PREDICT:A-044
- **averill.8** The reviewer's reading of Averill et al.'s supplement sits beside, not in place of, the authors' conclusion of equal predictability and rising fungal predictability with rank, which may rest on a figure-level or model-based summary in the unread main text.
  conf: not stated · class: not stated · holds: Averill et al. 2021; main text not read · src: averillSoilMicrobiomePredictability2021 · trail: C-PREDICT §What the direct evidence · from: C-PREDICT:B-0054
- **averill.9** Individual bacterial functional groups in Averill et al. spanned the full range: Lignolytic 0.96 best-fit against 0 on the 1:1 line; Copiotroph 0.86 against 0; N fixation 0.01 against 0; Chitinolytic 0.33 against 0.26.
  conf: not stated · class: not stated · holds: Averill et al.'s bacterial functional groups, site scale, cross-study transfer · src: averillSoilMicrobiomePredictability2021 (supplement) · trail: C-PREDICT §What the direct evidence · from: C-PREDICT:B-0051, C-PREDICT:B-0055
- **averill.10** In Averill et al. many groups with high correlation-type R2 had zero R2 against the 1:1 line in cross-study transfer, the authors link bias partly to compositional data, and the fungal-over-bacterial and functional-versus-taxonomic orderings differ under the two measures.
  conf: not stated · class: not stated · holds: soil microbes, cross-study transfer, both profile types · src: averillSoilMicrobiomePredictability2021 (supplement full text) · trail: C-PREDICT §Answers as delivered, §Properties that raise · from: C-PREDICT:A-059, C-PREDICT:B-0031, C-PREDICT:B-0141
- **averill.11** A peer reviewer of Averill et al. (review file, full text via a search agent) noted that predictive ability "was still quite low across bacteria and fungi".
  conf: not stated · class: not stated · holds: Averill et al. 2021 peer-review file · src: averillSoilMicrobiomePredictability2021 (peer-review file, full text via search agent) · trail: C-PREDICT §What the direct evidence · from: C-PREDICT:B-0056
- **averill.12** Removing Averill et al. 2021 removes the only cross-study held-out comparison and the only evidence that the verdict flips with skill measure.
  conf: not stated · class: not stated · holds: the review's D1 single-source sensitivity · src: averillSoilMicrobiomePredictability2021 · trail: C-PREDICT §Answers as delivered · from: C-PREDICT:A-026, C-PREDICT:A-027

### werbin: Werbin et al. 2024, a later-period and new-site hold-out
needs: profile-types, hold-out-design, skill-measures
- **werbin.1** Werbin et al. 2024 forecast 170 soil groups (135 taxonomic, phylum to genus; 35 derived functional) at 43 NEON sites with hierarchical Bayesian state-space models; calibration ran from November 2015 to January 2018 at 30 sites, the hold-outs were a later period (February 2018 to January 2020) and 13 new sites, and skill measures were nRMSE, CRPS and forecast R2, with the historical site mean as the null for forecast horizon.
  conf: single (note: "SINGLE SOURCE; preprint") · class: model/meas (note: "Modelled/measured") · holds: soil microbes at 43 NEON sites; the design as the review labels it stands (critic) · src: werbinForecastingSoilMicrobiome2024 (Research Square preprint, not peer reviewed; full text via search agents) · trail: C-PREDICT §What the direct evidence, §critic · from: C-PREDICT:B-0057..0059, C-PREDICT:B-0065, C-PREDICT:C-008
- **werbin.2** Werbin et al. report "functional groups of microorganisms ... were more predictable than most taxonomic groups", but that comparison is "evaluated at 30 sites included within calibration models", that is, on later dates at the fitted sites, where temporal autocorrelation contributes.
  conf: single (note: "SINGLE SOURCE; preprint") · class: not stated · holds: later dates at the 30 calibration sites; established by one search agent from a figure caption · src: werbinForecastingSoilMicrobiome2024 (full text via search agents) · trail: C-PREDICT §What the direct evidence, §Answers as delivered, §Adversarial critique · limit: access (critic: C-059) · from: C-PREDICT:B-0060, C-PREDICT:B-0065, C-PREDICT:A-010, C-PREDICT:C-059
- **werbin.3** In Werbin et al., new-site transfer is reported for bacteria versus fungi, not split by profile type: bacteria had much lower error than fungi at calibration sites (mean nRMSE 0.68 against 1.94) but transferred far worse to new sites (mean CRPS worse by 65% against 8%).
  conf: single (note: "SINGLE SOURCE; preprint") · class: not stated · holds: 13 new NEON sites against the 30 calibration sites · src: werbinForecastingSoilMicrobiome2024 (full text via search agents) · trail: C-PREDICT §What the direct evidence, §Adversarial critique · limit: access (critic: C-059) · from: C-PREDICT:B-0058, C-PREDICT:B-0061, C-PREDICT:B-0062, C-PREDICT:B-0065, C-PREDICT:C-059
- **werbin.4** In Werbin et al. the mechanism differs by kingdom: bacterial functional groups were less sensitive to environmental predictors than bacterial taxa and gained skill through stronger temporal autocorrelation, while fungal functional groups were more environment-sensitive than fungal taxa; whether functional grouping raises skill therefore depends on organism group and mechanism.
  conf: single (note: "SINGLE SOURCE; preprint") · class: not stated · holds: soil microbes at NEON · src: werbinForecastingSoilMicrobiome2024 (full text via search agents) · trail: C-PREDICT §What the direct evidence, §Answers as delivered, §Adversarial critique · limit: access (critic: C-059) · from: C-PREDICT:B-0057, C-PREDICT:B-0063, C-PREDICT:B-0065, C-PREDICT:A-010, C-PREDICT:A-067, C-PREDICT:C-059
- **werbin.5** In Werbin et al., seasonality-only models matched or beat six-predictor environmental models for most groups.
  conf: single (note: "SINGLE SOURCE; preprint") · class: not stated · holds: soil microbes at NEON · src: werbinForecastingSoilMicrobiome2024 (full text via search agents) · trail: C-PREDICT §What the direct evidence · from: C-PREDICT:B-0057, C-PREDICT:B-0064, C-PREDICT:B-0065
- **werbin.6** The Werbin et al. abstract reports "91% and 50% accuracy" and "Forecasts perform best for microbes grouped at broad taxonomic ranks or by ecological groups".
  conf: not stated · class: not stated · holds: the Werbin et al. 2024 abstract, the only part the critic confirmed · src: werbinForecastingSoilMicrobiome2024 (abstract, read by the critic) · trail: C-PREDICT §Adversarial critique · from: C-PREDICT:C-060
- **werbin.7** Removing Werbin et al. 2024 removes the only temporal (later) hold-out comparison.
  conf: not stated · class: not stated · holds: the review's D1 single-source sensitivity · src: werbinForecastingSoilMicrobiome2024 · trail: C-PREDICT §Answers as delivered · from: C-PREDICT:A-028

### liu-sludge: Liu et al. 2023, activated sludge
needs: profile-types, hold-out-design, skill-measures
- **liu-sludge.1** Liu et al. 2023 trained neural networks on 777 activated-sludge samples from 269 plants in 23 countries to predict ASV relative abundances from operational and environmental variables; mean 1:1 R2 was 35.1% for ASVs present in at least 10% of samples, 33 to 42% across taxonomic levels, and 32.6 to 56.8% (33 to 57% in the answers) for five derived functional groups (nitrifiers, denitrifiers, PAOs, GAOs, filamentous organisms).
  conf: single (note: "Measured; SINGLE SOURCE") · class: meas (note: "Measured; SINGLE SOURCE") · holds: activated sludge, 269 plants in 23 countries · src: liuPredictingMicrobialCommunity2023 (full text via search agent) · trail: C-PREDICT §What the direct evidence, §Answers as delivered, §critic · from: C-PREDICT:B-0066, C-PREDICT:B-0067, C-PREDICT:B-0069, C-PREDICT:A-011, C-PREDICT:C-008
- **liu-sludge.2** Liu et al.'s hold-out was a random 20% of samples, not blocked by plant, so the same plant could appear in training and test sets.
  conf: single (note: "Measured; SINGLE SOURCE") · class: not stated · holds: activated sludge; noted by a search agent · src: liuPredictingMicrobialCommunity2023 (full text via search agent) · trail: C-PREDICT §What the direct evidence · from: C-PREDICT:B-0068, C-PREDICT:B-0069

### derived-comparison: the same-study held-out comparisons with derived functional profiles
needs: averill, werbin, liu-sludge
- **derived-comparison.1** The three same-study held-out comparisons found, all microbial, all use functional profiles derived from taxonomy, and their results do not agree: Averill et al. 2021 (cross-study hold-out, independent NEON survey), Werbin et al. 2024 (later-period temporal hold-out at calibration sites, plus 13 held-out sites) and Liu et al. 2023 (random sample hold-out, not blocked by plant). Case B is mixed, dependent on hold-out design and skill measure.
  conf: not stated · class: not stated · holds: soil microbes and activated sludge; three single studies, one a non-peer-reviewed preprint, disagreeing among themselves and with the reviewer's reading of the one cross-study test · src: averillSoilMicrobiomePredictability2021, werbinForecastingSoilMicrobiome2024, liuPredictingMicrobialCommunity2023 · trail: C-PREDICT §What the direct evidence, §Answers as delivered, §critic, §Adversarial critique · rating: "Weak for held-out comparisons" · contrary: one-sided (critic: C-098) · from: C-PREDICT:B-0027, C-PREDICT:B-0030, C-PREDICT:B-0031, C-PREDICT:B-0057, C-PREDICT:B-0066, C-PREDICT:B-0070, C-PREDICT:A-003, C-PREDICT:A-006, C-PREDICT:A-007, C-PREDICT:A-016, C-PREDICT:C-002, C-PREDICT:C-096..098
- **derived-comparison.2** Averill's supplement puts bacterial derived function below all bacterial ranks; Werbin puts derived function above most taxa (for a within-site temporal test); Liu puts derived function at or above the taxonomic average (for a random-sample test). The hold-out designs differ in every case (cross-study; later period at the same sites; random samples), so these results cannot be pooled and the disagreement cannot be attributed to any one factor.
  conf: not stated · class: not stated · holds: the three derived-profile studies · src: averillSoilMicrobiomePredictability2021, werbinForecastingSoilMicrobiome2024, liuPredictingMicrobialCommunity2023 · trail: C-PREDICT §What the direct evidence, §Answers as delivered · from: C-PREDICT:B-0071, C-PREDICT:B-0072, C-PREDICT:A-018
- **derived-comparison.3** A 2026 reanalysis the review missed (Aouabed, Therrien, Bouaoune, Bakhtyari, Hijri and Makarenkov, Scientific Reports) fits several ML models predicting bacterial and fungal composition at functional-group and phylum-to-genus levels from environmental factors on the Averill and NEON datasets; it reports that bacterial functional groups failed under every model on Averill's data and that fungal functional groups reached R2 0.45 on NEON. This is further derived-profile, same-data evidence, and its hold-out design is unverified.
  conf: not stated · class: not stated · holds: soil microbes, machine-learning reanalysis of the same continental datasets · src: aouabedSoilMicrobiomePrediction2026 (abstract only, read by the critic) · trail: C-PREDICT §critic, §Adversarial critique · from: C-PREDICT:C-009..011, C-PREDICT:C-083..086

### one-profile-studies: one profile type at held-out units
needs: profile-types, hold-out-design, skill-measures
- **one-profile-studies.1** Faure et al. 2021 fitted random forests for 228,914 protein clusters mapped from marine MAGs to 93 Tara Oceans metagenomes using 52 environmental variables: mean test-set R2 was 0.28, 55.9% of models exceeded 0.25 and 6.4% exceeded 0.5, and Longhurst province, a habitat category, was the top predictor in 43% of models.
  conf: not stated · class: not stated · holds: marine measured gene content, 93 Tara Oceans metagenomes; numbers matched to the full text by the critic · src: faureTowardsOmicsbasedPredictions2021 (full text via search agent) · trail: C-PREDICT §One profile type, §critic · from: C-PREDICT:B-0073..0075, C-PREDICT:C-043
- **one-profile-studies.2** Faure et al.'s test sets were random 25% splits of samples, not blocked by station or region, with no baseline; it is the only measured-gene held-out study found, and it has no taxonomic comparison.
  conf: not stated · class: not stated · holds: 75% training splits of 93 samples · src: faureTowardsOmicsbasedPredictions2021 (full text via search agent) · trail: C-PREDICT §One profile type, §critic · from: C-PREDICT:B-0076, C-PREDICT:B-0077, C-PREDICT:C-043
- **one-profile-studies.3** Frémont et al. 2022 built niche models for metagenomic "genomic provinces", which are neither purely taxonomic nor functional: 27 of 38 provinces passed an AUC threshold under random splits, and the 11 rejected had few stations (few training units).
  conf: not stated · class: not stated · holds: surface-ocean plankton genomic provinces, random splits · src: fremontRestructuringPlanktonGenomic2022 (bioRxiv preprint read by a search agent) · trail: C-PREDICT §One profile type, §Properties that raise, §Answers as delivered · from: C-PREDICT:B-0078, C-PREDICT:B-0136, C-PREDICT:A-055, C-PREDICT:R-0101
- **one-profile-studies.4** Single-gene abundance models exist (nifH groups, Tang and Cassar 2019; pmoA and mcrA, Ou et al. 2024), but hold-out skill was not visible in their abstracts.
  conf: not stated · class: not stated · holds: nifH in the global ocean; pmoA and mcrA in soil · src: tangDataDrivenModelingDistribution2019 (abstract only), ouGlobalAtlasMethane2024 (abstract only) · trail: C-PREDICT §One profile type · from: C-PREDICT:B-0079, C-PREDICT:R-0105, C-PREDICT:R-0109
- **one-profile-studies.5** Mod et al. 2021 modelled soil bacterial OTU abundances at 255 Swiss Alpine sites with ten random 80/20 splits of whole sites (random, not spatially blocked); the best model (GAMnb) reached a median correlation of about 0.53 in fitting and about 0.26 at held-out sites.
  conf: not stated · class: not stated · holds: 255 Swiss Alpine sites, soil bacterial OTUs; verified by the critic in full text · src: modPredictingSpatialPatterns2021 (full text via search agents) · trail: C-PREDICT §One profile type, §critic · from: C-PREDICT:B-0080, C-PREDICT:B-0081, C-PREDICT:C-029, C-PREDICT:C-043
- **one-profile-studies.6** In Mod et al. more flexible models overfitted: GBM correlation about 0.97 in fitting and about 0.21 held out.
  conf: not stated · class: not stated · holds: 255 Swiss Alpine sites, soil bacterial OTUs · src: modPredictingSpatialPatterns2021 (full text via search agents), wengerAssessingTransferabilityEcological2012 (abstract only) · trail: C-PREDICT §One profile type, §Properties that raise, §Answers as delivered · from: C-PREDICT:B-0080, C-PREDICT:B-0081, C-PREDICT:B-0137, C-PREDICT:A-062
- **one-profile-studies.7** Ladau et al. 2018 used leave-one-out cross-validation for families and OTUs on the Tibetan Plateau, where samples came three per location, so leave-one-sample-out is not whole-site hold-out unless done by location (not verified).
  conf: not stated · class: not stated · holds: Tibetan Plateau soil prokaryotes · src: ladauExistingClimateChange2018 (full text, methods) · trail: C-PREDICT §One profile type · from: C-PREDICT:B-0082
- **one-profile-studies.8** Larsen et al. 2012 reported average Bray-Curtis similarity of 89.7 between predicted and observed communities over time at a Channel time series, with no baseline and an unstated temporal design.
  conf: not stated · class: not stated · holds: a Channel time series · src: larsenPredictingBacterialCommunity2012 (abstract only) · trail: C-PREDICT §One profile type · from: C-PREDICT:B-0083
- **one-profile-studies.9** Fuhrman et al. 2006, often cited for predictability, evaluated in-sample: the regression was fitted and assessed on the same 48 monthly samples.
  conf: not stated · class: not stated · holds: 48 monthly samples, ocean conditions · src: fuhrmanAnnuallyReoccurringBacterial2006 (full text via search agents) · trail: C-PREDICT §One profile type, §Answers as delivered · from: C-PREDICT:B-0084, C-PREDICT:A-063, C-PREDICT:R-0127
- **one-profile-studies.10** One-profile-only held-out studies (Faure et al. 2021 measured gene clusters, mean test R2 0.28; Mod et al. 2021 bacterial OTUs, median held-out correlation 0.26) use different measures and cannot be set against each other: comparisons assembled across studies (Case C) are not commensurable.
  conf: not stated · class: not stated · holds: held-out studies of one profile type · src: faureTowardsOmicsbasedPredictions2021, modPredictingSpatialPatterns2021 · trail: C-PREDICT §Answers as delivered · from: C-PREDICT:A-004, C-PREDICT:A-012

### explanatory-microbial: explanatory comparisons within one microbial dataset
needs: profile-types
- **explanatory-microbial.1** Explanatory comparisons within one dataset do not measure held-out skill; they bear on how much environment accounts for each profile type.
  conf: not stated · class: not stated · holds: within-dataset comparisons · src: none (the reviewer's framing) · trail: C-PREDICT §Explanatory comparisons · from: C-PREDICT:B-0085, C-PREDICT:B-0086
- **explanatory-microbial.2** Louca et al. 2016 found environment strongly structured the distribution of FAPROTAX functional groups in the global ocean but only weakly structured taxonomy within groups.
  conf: not stated · class: not stated · holds: global ocean, derived function · src: loucaDecouplingFunctionTaxonomy2016 (abstract only) · trail: C-PREDICT §Explanatory comparisons · from: C-PREDICT:B-0087
- **explanatory-microbial.3** Ohigashi et al. 2025 found predicted functional composition homogenised over broader scales than taxonomy in farmland.
  conf: not stated · class: not stated · holds: farmland soils, derived function · src: ohigashiAgriculturalLandUse2025 (preprint, abstract only) · trail: C-PREDICT §Explanatory comparisons · from: C-PREDICT:B-0088
- **explanatory-microbial.4** Nelson et al. 2016 found habitat and soil C and N largely explained soil N-pathway frequency, but could not identify drivers of taxonomy within N groups.
  conf: not stated · class: not stated · holds: soils, measured genes · src: nelsonGlobalBiogeographyMicrobial2016 (abstract only) · trail: C-PREDICT §Explanatory comparisons · from: C-PREDICT:B-0089
- **explanatory-microbial.5** Bahram et al. 2018 found gene composition varied more with environment than with distance.
  conf: not stated · class: not stated · holds: measured genes · src: bahramStructureFunctionGlobal2018 · trail: C-PREDICT §Explanatory comparisons · from: C-PREDICT:B-0089, C-PREDICT:B-0090
- **explanatory-microbial.6** Fierer et al. 2012 found functional beta diversity strongly correlated with taxonomic beta diversity.
  conf: not stated · class: not stated · holds: 16 soils, measured genes · src: fiererCrossbiomeMetagenomicAnalyses2012 (abstract only) · trail: C-PREDICT §Explanatory comparisons · from: C-PREDICT:B-0089, C-PREDICT:B-0091
- **explanatory-microbial.7** Galand et al. 2018 found that at a Mediterranean coastal site taxonomic shifts altered function, and that this link appeared only when all reads were used rather than annotated genes: annotation coverage changes the apparent coupling of function to taxonomy.
  conf: not stated · class: not stated · holds: a Mediterranean coastal site, measured genes, explanatory · src: galandStrongLinkMarine2018 (abstract only) · trail: C-PREDICT §Explanatory comparisons, §Properties that raise, §Answers as delivered · from: C-PREDICT:B-0092, C-PREDICT:B-0140, C-PREDICT:A-058
- **explanatory-microbial.8** Liu et al. 2021 found function stable while taxonomy tracked temperature and nitrate upstream in a river, but both changed together under strong anthropogenic pressure downstream.
  conf: not stated · class: not stated · holds: a river, upstream and downstream; measured genes · src: liuAnthropogenicActivitiesChange2021 (abstract only) · trail: C-PREDICT §Explanatory comparisons · from: C-PREDICT:B-0089, C-PREDICT:B-0093
- **explanatory-microbial.9** Liang et al. 2024 found 16S and qPCR N-gene dissimilarity responded to different predictors on the Tibetan Plateau.
  conf: not stated · class: not stated · holds: Tibetan Plateau soils · src: qingqingTaxonomicFunctionalBiogeography2024 (preprint, abstract only) · trail: C-PREDICT §Explanatory comparisons · from: C-PREDICT:B-0094, C-PREDICT:R-0158
- **explanatory-microbial.10** Measured gene profiles varied less than taxonomy among replicate units in bromeliad tanks (Louca et al. 2016b).
  conf: not stated · class: not stated · holds: bromeliad tanks, background variability · src: loucaHighTaxonomicVariability2016 (abstract only) · trail: C-PREDICT §Explanatory comparisons · from: C-PREDICT:B-0095, C-PREDICT:B-0096
- **explanatory-microbial.11** Measured gene profiles varied less than taxonomy on Ulva surfaces: about 15% species similarity against about 70% functional similarity (Burke et al. 2011).
  conf: not stated · class: not stated · holds: Ulva surfaces, background variability · src: burkeBacterialCommunityAssembly2011 (abstract only) · trail: C-PREDICT §Explanatory comparisons · from: C-PREDICT:B-0095, C-PREDICT:B-0096
- **explanatory-microbial.12** Measured gene profiles varied less than taxonomy among human body-site samples (HMP 2012, host-associated).
  conf: not stated · class: not stated · holds: human body sites, host-associated · src: theStructureFunctionDiversity2012 (abstract only) · trail: C-PREDICT §Explanatory comparisons · from: C-PREDICT:B-0095, C-PREDICT:B-0096
- **explanatory-microbial.13** Coles et al. 2017 reproduced ocean gradients regardless of which random species cohort seeded a trait-based model.
  conf: not stated · class: model (note: "modelled, abstract only") · holds: ocean biogeochemistry, a trait-based model · src: colesOceanBiogeochemistryModeled2017 (abstract only) · trail: C-PREDICT §Explanatory comparisons · from: C-PREDICT:B-0097
- **explanatory-microbial.14** In microbes the explanatory picture is split: Louca et al. 2016 (derived) and Nelson et al. 2016 (measured) find functional structure more environment-bound than taxonomy within functional groups, with Burke 2011 and HMP 2012 also on the decoupling side, while Fierer et al. 2012 find functional and taxonomic beta diversity strongly correlated and Galand et al. 2018 find function tracks taxonomy. These contrary results are abstract only, as is the freshwater pattern rated more strongly.
  conf: not stated · class: not stated · holds: explanatory microbial studies · src: loucaDecouplingFunctionTaxonomy2016, nelsonGlobalBiogeographyMicrobial2016, burkeBacterialCommunityAssembly2011, theStructureFunctionDiversity2012, fiererCrossbiomeMetagenomicAnalyses2012, galandStrongLinkMarine2018 · trail: C-PREDICT §Answers as delivered, §Adversarial critique · from: C-PREDICT:A-014, C-PREDICT:A-019, C-PREDICT:C-102

### explanatory-other: explanatory comparisons in other organism groups
needs: profile-types
- **explanatory-other.1** Göthe et al. 2017 found trait composition corresponded more closely to environment than species composition across macrophytes, macroinvertebrates and fish in Danish streams.
  conf: not stated · class: not stated · holds: Danish streams; closeness of fit to environment · src: gotheEnvironmentalSpatialControls2016 (abstract only) · trail: C-PREDICT §Explanatory comparisons, §Adversarial critique · from: C-PREDICT:B-0098, C-PREDICT:B-0105, C-PREDICT:C-108
- **explanatory-other.2** Soininen et al. 2016 found diatom guild composition better explained by environment than species composition across six regions.
  conf: not stated · class: not stated · holds: diatoms, six regions; closeness of fit to environment · src: soininenGlobalPatternsDrivers2016 (abstract only) · trail: C-PREDICT §Explanatory comparisons, §Adversarial critique · from: C-PREDICT:B-0099, C-PREDICT:B-0105, C-PREDICT:C-108
- **explanatory-other.3** Kruk et al. 2011 found morphology-based phytoplankton groups predicted better from environment than phylogenetic groups (a coarse taxonomic aggregate), Reynolds groups and single species, in-sample, in one dataset of 211 lakes.
  conf: not stated · class: not stated · holds: 211 lakes, in-sample, one dataset · src: krukPhytoplanktonCommunityComposition2010 (abstract only) · trail: C-PREDICT §Explanatory comparisons, §Adversarial critique · from: C-PREDICT:B-0100, C-PREDICT:B-0105, C-PREDICT:C-067, C-PREDICT:C-112
- **explanatory-other.4** Dolédec et al. 2011 found trait responses to land use consistent across New Zealand ecoregions while taxonomic responses differed: a result about how consistently responses hold across regions, not how closely a profile fits environment.
  conf: not stated · class: not stated · holds: New Zealand rivers and ecoregions, invertebrates, land use · src: doledecInvertebrateCommunityResponses2011 (abstract only) · trail: C-PREDICT §Explanatory comparisons, §critic · from: C-PREDICT:B-0101, C-PREDICT:B-0105, C-PREDICT:C-015, C-PREDICT:R-0193
- **explanatory-other.5** Hoeinghaus et al. 2007 found fish functional groups sorted by habitat regardless of region: a result about consistency across regions, not closeness of fit.
  conf: not stated · class: not stated · holds: stream fish · src: hoeinghausLocalRegionalDeterminants2006 (abstract only) · trail: C-PREDICT §Explanatory comparisons, §critic · from: C-PREDICT:B-0102, C-PREDICT:B-0105, C-PREDICT:C-015, C-PREDICT:R-0197
- **explanatory-other.6** Pont et al. 2006 found functional fish metrics less sensitive to biogeographic variation than species metrics.
  conf: not stated · class: not stated · holds: European rivers, fish · src: pontAssessingRiverBiotic2006 (abstract only) · trail: C-PREDICT §Freshwater bioassessment · from: C-PREDICT:B-0115, C-PREDICT:R-0249
- **explanatory-other.7** Trait profiles of benthic macroinvertebrates varied less than taxonomy across French reference streams (Charvet et al. 2000).
  conf: not stated · class: not stated · holds: French reference streams; stream macroinvertebrates · src: charvetTraitsBenthicMacroinvertebrates2000 (abstract only) · trail: C-PREDICT §Explanatory comparisons, §Adversarial critique · from: C-PREDICT:B-0103, C-PREDICT:B-0105, C-PREDICT:C-063, C-PREDICT:R-0201
- **explanatory-other.8** Trait profiles varied less than taxonomy between Mediterranean and temperate Europe (Bonada et al. 2007).
  conf: not stated · class: not stated · holds: stream macroinvertebrates, Mediterranean and temperate Europe · src: bonadaTaxonomicBiologicalTrait2007 (abstract only) · trail: C-PREDICT §Explanatory comparisons, §Adversarial critique · from: C-PREDICT:B-0103, C-PREDICT:B-0105, C-PREDICT:C-063
- **explanatory-other.9** Trait profiles varied less than taxonomy across seasons and years in California streams (Bêche et al. 2006); this and the two preceding variability results are three abstract-only stream-macroinvertebrate studies from overlapping author groups, two sharing Statzner and Dolédec with the Statzner 2005 and Gayraud 2003 papers, so they are not independent replicates across organism groups.
  conf: not stated · class: not stated · holds: California streams, stream macroinvertebrates · src: becheLongtermSeasonalVariation2005 (abstract only) · trail: C-PREDICT §Explanatory comparisons, §Adversarial critique · from: C-PREDICT:B-0103, C-PREDICT:B-0105, C-PREDICT:C-063
- **explanatory-other.10** Bruelheide et al. 2018 is bounding: across more than a million vegetation plots, community trait axes were only weakly associated with macroclimate and soil; it bounds the freshwater pattern in plants but is not weighed against it in the D1 answer.
  conf: not stated · class: not stated · holds: more than a million vegetation plots · src: bruelheideGlobalTraitenvironmentRelationships2018 (abstract only) · trail: C-PREDICT §Explanatory comparisons, §critic, §Adversarial critique · from: C-PREDICT:B-0104, C-PREDICT:C-013, C-PREDICT:C-106
- **explanatory-other.11** The explanatory freshwater pattern (trait composition more aligned with environment and less variable than taxonomic composition) rests entirely on abstracts, is concentrated in stream macroinvertebrates from a closely linked set of authors (Statzner, Dolédec, Usseglio-Polatera, Bonada), and is bounded in plants by Bruelheide et al. 2018; it is moderate at best and not replicated across organism groups, and it is explanatory, not held-out skill. For the explanatory freshwater pattern, no single removal changes it.
  conf: not stated · class: not stated · holds: freshwater explanatory studies; every supporting source (Göthe, Soininen, Kruk, Dolédec, Hoeinghaus, Charvet, Bonada, Bêche) abstract only · src: gotheEnvironmentalSpatialControls2016, soininenGlobalPatternsDrivers2016, krukPhytoplanktonCommunityComposition2010, doledecInvertebrateCommunityResponses2011, hoeinghausLocalRegionalDeterminants2006, charvetTraitsBenthicMacroinvertebrates2000, bonadaTaxonomicBiologicalTrait2007, becheLongtermSeasonalVariation2005 · trail: C-PREDICT §critic, §Adversarial critique, §Answers as delivered · rating: "Moderate and replicated" (critic: C-014: moderate at best, and should not be called replicated across organism groups) · limit: access (critic: C-056) · from: C-PREDICT:A-005, C-PREDICT:A-017, C-PREDICT:A-029, C-PREDICT:C-012..014, C-PREDICT:C-050, C-PREDICT:C-056

### bioassessment: freshwater bioassessment reference models
needs: hold-out-design, skill-measures
- **bioassessment.1** RIVPACS-type models predict expected taxa at held-out reference sites.
  conf: not stated · class: not stated · holds: freshwater bioassessment · src: none (the reviewer's description) · trail: C-PREDICT §Freshwater bioassessment · from: C-PREDICT:B-0106
- **bioassessment.2** Hawkins et al. 2000 report species-level RIVPACS models more accurate than family-level ones, evaluated by "how well models predicted the taxa found at unimpaired sites", which is not shown to be independent sites, and confounded with the Pc threshold choice (all taxa versus Pc ≥ 0.5) varied at the same time: it is not confirmed as a held-out species-versus-family result.
  conf: not stated · class: not stated · holds: freshwater bioassessment; hold-out design not confirmed · src: hawkinsDEVELOPMENTEVALUATIONPREDICTIVE2000 (abstract only; verified by the critic) · trail: C-PREDICT §Freshwater bioassessment, §critic, §Adversarial critique · from: C-PREDICT:B-0107, C-PREDICT:A-039, C-PREDICT:C-024, C-PREDICT:C-025, C-PREDICT:C-061, C-PREDICT:C-110
- **bioassessment.3** Moss et al. 1999 tested species and family systems on 101 independent sites; the abstract reports only that differences among methods were marginal and gives no comparison between levels.
  conf: not stated · class: not stated · holds: running-water sites in Great Britain, 101 independent sites · src: mossComparisonAlternativeTechniques1999 (abstract only) · trail: C-PREDICT §Freshwater bioassessment, §critic · from: C-PREDICT:B-0108, C-PREDICT:A-039, C-PREDICT:C-026, C-PREDICT:C-044, C-PREDICT:R-0222
- **bioassessment.4** Van Sickle et al. 2005 introduced a null model for O/E; the SDs of O/E (0.18 against 0.20; 0.13 against 0.28) were computed across the reference sites used to build the models, so they are calibration-site (in-sample) precision, ranging from negligible to large gains for taxonomic O/E, not held-out skill over a null.
  conf: not stated · class: not stated · holds: stream macroinvertebrates, taxonomic O/E, calibration (reference) sites; verified in the abstract by the critic · src: vansickleNullModelExpected2005 (abstract only) · trail: C-PREDICT §Freshwater bioassessment, §critic, §Adversarial critique · from: C-PREDICT:B-0109, C-PREDICT:C-032, C-PREDICT:C-033, C-PREDICT:C-052, C-PREDICT:C-104, C-PREDICT:R-0227
- **bioassessment.5** Mykrä et al. 2008 found restricting to common taxa improved O/E error but left only 8 to 13 expected taxa.
  conf: single (critic: C-066) · class: not stated · holds: invertebrate O/E models, stream macroinvertebrates across regional scales · src: mykraPredictingStreamMacroinvertebrate2008 (abstract only) · trail: C-PREDICT §Freshwater bioassessment, §Properties that raise, §Adversarial critique · from: C-PREDICT:B-0110, C-PREDICT:B-0133, C-PREDICT:A-054, C-PREDICT:C-066, C-PREDICT:R-0231
- **bioassessment.6** No study was found that fits separate reference models for trait and taxon profiles and compares their precision at held-out reference sites; the key trait-based bioassessment sources were not obtained and no alternative route was recorded.
  conf: not stated · class: search (note: "none found separate trait and taxon reference models compared at held-out reference sites") · holds: freshwater bioassessment · src: none (the review's search) · trail: C-PREDICT §Freshwater bioassessment, §Search record, §Adversarial critique · search: searched, not found (note: "none found separate trait and taxon reference models compared at held-out reference sites") · from: C-PREDICT:B-0116, C-PREDICT:B-0149, C-PREDICT:C-094
- **bioassessment.7** Feio and Dolédec 2012 derived expected trait profiles from predicted taxa.
  conf: not stated · class: not stated · holds: trait profiles expected from predicted taxa, a case study in Portugal · src: feioIntegrationInvertebrateTraits2012 (abstract only) · trail: C-PREDICT §Freshwater bioassessment · from: C-PREDICT:B-0114, C-PREDICT:R-0245

### trait-baseline: trait profiles against a mean-profile baseline
needs: bioassessment
- **trait-baseline.1** Statzner et al. 2005 predicted trait profiles of large European river reaches and found that landscape models gained negligibly over a mean-profile model; this is verified in the abstract, but whether the comparison was made at held-out test reaches is not stated there (the abstract mentions test-LIRRs only for the final assignment step), so its held-out framing rests on the secondary account in Hawkins et al. 2010. It is a trait-only result, with no taxonomic counterpart in the same study, and not a trait-versus-taxon comparison.
  conf: single (critic: C-064) · class: not stated · holds: large European river reaches, least impacted · src: statznerInvertebrateTraitsBiomonitoring2005 (abstract only), hawkinsReferenceConditionPredicting2010 (SECONDARY; read by a search agent, not re-opened by the synthesis; critic: C-055 was "full-text review") · trail: C-PREDICT §Freshwater bioassessment, §critic, §Adversarial critique · limit: access (critic: C-034) · from: C-PREDICT:B-0111, C-PREDICT:B-0112, C-PREDICT:A-025, C-PREDICT:A-072, C-PREDICT:C-016, C-PREDICT:C-017, C-PREDICT:C-034, C-PREDICT:C-053..055, C-PREDICT:R-0235
- **trait-baseline.2** The Statzner et al. 2005 abstract (point 3) reports that the relative abundance of many trait categories changed along 13 rivers.
  conf: not stated · class: not stated · holds: 13 large European rivers · src: statznerInvertebrateTraitsBiomonitoring2005 (abstract only) · trail: C-PREDICT §critic, §Adversarial critique · from: C-PREDICT:C-036, C-PREDICT:C-062, C-PREDICT:R-0235
- **trait-baseline.3** The reviewer's own inference, not the source's explanation: because trait profiles vary little across reference sites, a constant already predicts them, so low raw error and low skill over baseline can coexist. It rests on Statzner et al. 2005 (abstract only) plus that inference, is partly contradicted by the abstract's own point 3, and partly follows the brief's evidence bullet on background variability, though it is not an echo of a stated expectation.
  conf: not stated · class: reading (critic: C-035) · holds: trait profiles of reference reaches · src: statznerInvertebrateTraitsBiomonitoring2005 (abstract only) · trail: C-PREDICT §critic, §Adversarial critique · from: C-PREDICT:C-035, C-PREDICT:C-037, C-PREDICT:C-049, C-PREDICT:C-114, C-PREDICT:C-115, C-PREDICT:C-117..119

### plant-traits: plant trait prediction
needs: hold-out-design
- **plant-traits.1** In plants, community-weighted trait means were predicted better than trait diversity indices (Dubuis et al. 2013).
  conf: not stated · class: not stated · holds: plant functional traits · src: dubuisPredictingCurrentFuture2013 (abstract only) · trail: C-PREDICT §Freshwater bioassessment · from: C-PREDICT:B-0117, C-PREDICT:B-0118, C-PREDICT:R-0253
- **plant-traits.2** Modelling plant traits directly beat stacking species predictions for environmental extrapolation (R2 0.60 against 0.54 for plant height; Deschamps et al. 2023).
  conf: not stated · class: not stated · holds: plant height, environmental extrapolation; matched to the abstract by the critic · src: deschampsPredictFirstassembleLater2023 (abstract only) · trail: C-PREDICT §Freshwater bioassessment, §critic · from: C-PREDICT:B-0117, C-PREDICT:B-0118, C-PREDICT:C-044
- **plant-traits.3** Leaf nitrogen could not be predicted reliably at global scale, and data quality raised performance by 28% (Boonman et al. 2020).
  conf: not stated · class: not stated · holds: predicted plant trait distributions at global scale · src: boonmanAssessingReliabilityPredicted2020 (abstract only) · trail: C-PREDICT §Freshwater bioassessment, §Answers as delivered · from: C-PREDICT:B-0117, C-PREDICT:B-0118, C-PREDICT:A-057, C-PREDICT:R-0262
- **plant-traits.4** For plant trait profiles, skill differs by trait (leaf nitrogen unreliable) and by summary statistic (means better than diversity indices); the means-against-diversity-indices comparison concerns the choice of summary statistic, not the level of the trait hierarchy.
  conf: not stated · class: not stated · holds: plant traits · src: dubuisPredictingCurrentFuture2013, deschampsPredictFirstassembleLater2023, boonmanAssessingReliabilityPredicted2020 · trail: C-PREDICT §Properties that raise, §Answers as delivered, §Adversarial critique · from: C-PREDICT:B-0138, C-PREDICT:A-057, C-PREDICT:C-111

### resolution: taxonomic rank and functional hierarchy
needs: averill, werbin, liu-sludge, one-profile-studies, bioassessment, plant-traits
- **resolution.1** For microbial taxonomic rank, the held-out evidence shows no consistent monotonic shape across the studies reviewed, with caveats: each rank finding is single-study, the microbial studies disagree on shape, and rank is confounded with abundance.
  conf: single (note: "Each rank finding is single-study") · class: not stated · holds: held-out microbial studies reviewed · src: werbinForecastingSoilMicrobiome2024, averillSoilMicrobiomePredictability2021, modPredictingSpatialPatterns2021, liuPredictingMicrobialCommunity2023 · trail: C-PREDICT §critic, §Answers as delivered · rating: "Weak" · from: C-PREDICT:C-018, C-PREDICT:A-033, C-PREDICT:A-043, C-PREDICT:A-044
- **resolution.2** Werbin et al. 2024 report broad fungal ranks (phylum, class) more predictable than genus and family, and bacteria most predictable at class.
  conf: single (critic: C-065) · class: not stated · holds: soil microbes at NEON; a preprint; the review's recomputation of Averill contradicts the fungal pattern · src: werbinForecastingSoilMicrobiome2024 (full text via search agents) · trail: C-PREDICT §Answers as delivered, §Adversarial critique · from: C-PREDICT:A-034, C-PREDICT:B-0057, C-PREDICT:C-065
- **resolution.3** Mod et al. 2021 found that OTU clustering distance and closed-reference genera did not change held-out skill of soil bacterial models; removing it removes the only fine-resolution (OTU clustering) test.
  conf: single (note: "Each rank finding is single-study") · class: not stated · holds: soil bacterial models, Swiss Alpine sites · src: modPredictingSpatialPatterns2021 (full text via search agents) · trail: C-PREDICT §Answers as delivered · from: C-PREDICT:A-036, C-PREDICT:A-044, C-PREDICT:A-050, C-PREDICT:B-0080
- **resolution.4** Liu et al. 2023 report 33 to 42% mean skill across taxonomic levels without a clear stated trend.
  conf: single (note: "Each rank finding is single-study") · class: not stated · holds: activated sludge · src: liuPredictingMicrobialCommunity2023 (full text via search agents) · trail: C-PREDICT §Answers as delivered · from: C-PREDICT:A-037, C-PREDICT:A-044
- **resolution.5** Werbin et al. note that higher ranks are more abundant and abundance was the strongest correlate of predictability, so rank effects are confounded with abundance.
  conf: not stated · class: not stated · holds: soil microbes at NEON · src: werbinForecastingSoilMicrobiome2024 · trail: C-PREDICT §Answers as delivered, §Properties that raise · from: C-PREDICT:A-038, C-PREDICT:B-0057, C-PREDICT:B-0143
- **resolution.6** Aouabed et al. 2026, missed by the review, say predictability rises with taxonomic scale across several ML models fitted to the Averill and NEON data.
  conf: not stated · class: not stated · holds: soil microbes, reanalysis of the Averill and NEON datasets · src: aouabedSoilMicrobiomePrediction2026 (abstract only) · trail: C-PREDICT §critic, §Adversarial critique · from: C-PREDICT:C-019, C-PREDICT:C-020, C-PREDICT:C-085
- **resolution.7** A 2026 New Phytologist study, missed by the review, predicting soil microbes at 14 NEON domains from airborne canopy reflectance found validation R2 of 0.27 to 0.86 varying with taxonomic resolution, with broad microbial groups predicted best; its predictors are remote sensing, not direct environmental measures.
  conf: not stated · class: not stated · holds: soil microbes at 14 NEON domains; remote-sensing predictors · src: anon2026 (abstract only) · trail: C-PREDICT §critic, §Adversarial critique · from: C-PREDICT:C-021, C-PREDICT:C-088
- **resolution.8** The two missed 2026 reports both lean towards broader ranks predicting better and weaken the review's 'no direction' reading; neither separates rank from abundance.
  conf: not stated · class: not stated · holds: soil microbes at NEON · src: aouabedSoilMicrobiomePrediction2026, anon2026 · trail: C-PREDICT §critic · from: C-PREDICT:C-021, C-PREDICT:C-022, C-PREDICT:C-023
- **resolution.9** For gene or trait profiles, no held-out study comparing gene, pathway and category levels (the functional hierarchy) was found; studies comparing KO, module, pathway and category (or CAZy family versus class) predictability or environmental fit were not searched for.
  conf: not stated · class: search (note: "no held-out study comparing gene, pathway and category levels was found") · holds: measured metagenomic gene hierarchy levels; none of the three search angles found one by their routes · src: none (the review's search) · trail: C-PREDICT §Answers as delivered, §critic, §Adversarial critique · search: not searched (critic: C-093) · from: C-PREDICT:A-032, C-PREDICT:A-040, C-PREDICT:B-0012, C-PREDICT:C-027, C-PREDICT:C-093
- **resolution.10** Nearest precedents for the trait hierarchy: invertebrate trait profiles computed from species, genus or family data are very similar (Gayraud et al. 2003, descriptive), and narrow soil functions are less redundant than broad ones (Chen et al. 2022, explanatory, about redundancy not predictability).
  conf: not stated · class: not stated · holds: stream invertebrates (Gayraud); global soil metagenomes (Chen) · src: gayraudInvertebrateTraitsBiomonitoring2003 (abstract only), chenLowerFunctionalRedundancy2022 (abstract only) · trail: C-PREDICT §Answers as delivered, §Adversarial critique · from: C-PREDICT:A-041, C-PREDICT:C-093
- **resolution.11** No study compared the two profile types at matched levels of aggregation, or across several resolution levels on both sides; for the cross-level comparison there is no evidence beyond one derived-profile study.
  conf: not stated · class: search (note: "No study compared the two profile types across several resolution levels on both sides") · holds: taxonomic and gene or trait profiles · src: none (the review's search) · trail: C-PREDICT §Answers as delivered, §critic · search: not stated · from: C-PREDICT:A-033, C-PREDICT:A-042, C-PREDICT:C-028
- **resolution.12** Not measured: gene to pathway to broad-category held-out skill for measured metagenomic profiles; individual trait versus trait syndrome at held-out units; strain or ASV versus OTU versus genus comparisons with rank decoupled from abundance; any study comparing taxonomic and gene or trait profiles at matched levels of aggregation.
  conf: not stated · class: search (note: "Not measured") · holds: resolution comparisons · src: none (the review's search) · trail: C-PREDICT §Answers as delivered · search: not stated · from: C-PREDICT:A-046
- **resolution.13** On rank, the studies conflict: Averill (bacterial peak at order, by the reviewer's reading) against Werbin (bacterial peak at class); the authors' 'fungal predictability increases with taxonomic scale' against non-monotonic supplementary medians; and a microbial broad-rank advantage for fungi against a species-over-family advantage in stream invertebrates (different organisms, different measures).
  conf: cont (note: "Conflicts") · class: not stated · holds: soil microbes and stream invertebrates · src: averillSoilMicrobiomePredictability2021, werbinForecastingSoilMicrobiome2024, hawkinsDEVELOPMENTEVALUATIONPREDICTIVE2000 · trail: C-PREDICT §Answers as delivered · from: C-PREDICT:A-045
- **resolution.14** Removing Werbin et al. 2024 leaves only Averill's supplement for the microbial rank shape, and removing Hawkins et al. 2000 removes the only species-versus-family comparison in bioassessment, which is not confirmed as held-out.
  conf: not stated · class: not stated · holds: the review's D2 single-source sensitivity · src: werbinForecastingSoilMicrobiome2024, averillSoilMicrobiomePredictability2021, hawkinsDEVELOPMENTEVALUATIONPREDICTIVE2000 · trail: C-PREDICT §Answers as delivered, §Adversarial critique · from: C-PREDICT:A-050, C-PREDICT:C-061

### skill-properties: properties that raise or lower held-out skill
needs: averill, werbin, liu-sludge, one-profile-studies, bioassessment, trait-baseline, plant-traits, hold-out-design, skill-measures
- **skill-properties.1** Higher relative abundance and occurrence frequency go with higher held-out skill for taxonomic profiles in three microbial studies (Mod et al. 2021, soil OTUs; Liu et al. 2023, activated-sludge ASVs; Werbin et al. 2024, whose all-groups result includes derived functional as well as taxonomic groups), plus the SDM literature; the abundance effect survives removal of any one source.
  conf: not stated · class: not stated · holds: soil OTUs, activated-sludge ASVs, NEON soil groups · src: modPredictingSpatialPatterns2021, liuPredictingMicrobialCommunity2023, werbinForecastingSoilMicrobiome2024 · trail: C-PREDICT §Answers as delivered, §Properties that raise, §critic, §Adversarial critique · rating: "Moderate" · from: C-PREDICT:A-052, C-PREDICT:A-054, C-PREDICT:A-064, C-PREDICT:A-071, C-PREDICT:B-0057, C-PREDICT:B-0131, C-PREDICT:C-029, C-PREDICT:C-109
- **skill-properties.2** A high neutral-model migration rate lowers held-out skill of taxonomic profiles (Liu et al. 2023).
  conf: single (critic: C-066) · class: not stated · holds: activated-sludge ASVs · src: liuPredictingMicrobialCommunity2023 (full text) · trail: C-PREDICT §Properties that raise, §Answers as delivered, §Adversarial critique · from: C-PREDICT:B-0132, C-PREDICT:A-055, C-PREDICT:C-066
- **skill-properties.3** Rarity lowers held-out skill (Mod 2021; Norberg et al. 2019 for plants and animals).
  conf: not stated · class: not stated · holds: soil OTUs; plants and animals · src: modPredictingSpatialPatterns2021, norbergComprehensiveEvaluationPredictive2019 · trail: C-PREDICT §Answers as delivered · from: C-PREDICT:A-052, C-PREDICT:A-055
- **skill-properties.4** For derived functional profiles, groups defined from literature plus genomic pathway evidence were more predictable than those from literature alone or enrichment experiments (Werbin 2024).
  conf: single (critic: C-038) · class: not stated · holds: derived functional groups, bacteria, NEON · src: werbinForecastingSoilMicrobiome2024 (full text) · trail: C-PREDICT §Answers as delivered, §Properties that raise, §critic · rating: "Weak (single study)" · from: C-PREDICT:A-056, C-PREDICT:A-065, C-PREDICT:B-0057, C-PREDICT:B-0135, C-PREDICT:C-038
- **skill-properties.5** For derived functional profiles in temporal hold-outs, temporal autocorrelation raises skill but does not transfer to new sites: bacterial functional groups gained temporal skill from autocorrelation rather than environmental sensitivity, and bacteria lost much more skill at new sites (CRPS worse by 65% against 8% for fungi).
  conf: single (critic: C-038) · class: not stated · holds: derived functional and taxonomic bacterial groups, NEON · src: werbinForecastingSoilMicrobiome2024 (full text) · trail: C-PREDICT §Answers as delivered, §Properties that raise, §critic · rating: "Weak (single study)" · limit: access (critic: C-059) · from: C-PREDICT:A-053, C-PREDICT:A-056, C-PREDICT:A-065, C-PREDICT:B-0057, C-PREDICT:B-0134, C-PREDICT:C-038, C-PREDICT:C-059
- **skill-properties.6** No property affecting held-out skill has been shown on measured gene profiles at held-out units; not measured are properties of measured gene profiles (gene length, copy number, annotation completeness, genome-size normalisation, compositional closure), any microbial comparison of both profile types against a mean-profile or persistence baseline, and spatially blocked hold-outs in microbial function prediction.
  conf: not stated · class: search (note: "No property has been shown on measured gene profiles at held-out units") · holds: measured gene profiles · src: none (the review's search) · trail: C-PREDICT §Answers as delivered, §critic · search: not stated · from: C-PREDICT:A-066, C-PREDICT:A-069, C-PREDICT:C-039
- **skill-properties.7** 16S-derived function matched enzyme patterns qualitatively, not quantitatively (Breitkreuz et al. 2021).
  conf: not stated · class: not stated · holds: agricultural soils; derived versus measured function · src: breitkreuzCanWeEstimate2021 (abstract only) · trail: C-PREDICT §Properties that raise, §Answers as delivered · from: C-PREDICT:B-0139, C-PREDICT:A-058, C-PREDICT:R-0293

### reverse-direction: profiles predicting environment
needs: hold-out-design
- **reverse-direction.1** In the reverse direction, where profiles predict environment, cross-study transfer of gut disease classifiers was weaker than within-study validation (Pasolli et al. 2016).
  conf: not stated · class: not stated · holds: gut disease classifiers; a nearest precedent only · src: pasolliMachineLearningMetaanalysis2016 (abstract only) · trail: C-PREDICT §Transferability, bounds · from: C-PREDICT:B-0126, C-PREDICT:B-0128, C-PREDICT:B-0129
- **reverse-direction.2** Soil bacteria predicted land use and soil variables in New Zealand (Hermans et al. 2020).
  conf: not stated · class: not stated · holds: New Zealand soils; a nearest precedent only · src: hermansUsingSoilBacterial2020 (abstract only) · trail: C-PREDICT §Transferability, bounds · from: C-PREDICT:B-0127..0129
- **reverse-direction.3** Groundwater bacteria predicted geochemistry, with geographic generalisation untested (Smith et al. 2015).
  conf: not stated · class: not stated · holds: groundwater; a nearest precedent only · src: smithNaturalBacterialCommunities2015 (abstract only) · trail: C-PREDICT §Transferability, bounds · from: C-PREDICT:B-0127..0129

## Do not say
- **dns.1** "Averill et al.'s own supplement contradicts their conclusion that functional and taxonomic groups were equally predictable."
  why: The authors compared functional groups with high-level taxonomic groups, not with all ranks, and against phyla the result splits by kingdom, so the reviewer's reading departs from the authors for bacteria only. · instead: averill.2, averill.4 · trail: C-PREDICT §critic, §Answers as delivered, §Adversarial critique · from: C-PREDICT:A-018, C-PREDICT:C-003, C-PREDICT:C-047, C-PREDICT:C-096
- **dns.2** "Under the 1:1 measure, almost every group in Averill et al.'s cross-study test had no skill."
  why: That is a median-level statement: the median 1:1 R2 is 0 for every group except fungal functional groups, but about 21 of 130 groups have a positive 1:1 R2. · instead: averill.6 · trail: C-PREDICT §What the direct evidence, §critic · from: C-PREDICT:B-0052, C-PREDICT:C-031
- **dns.3** "In bioassessment, gains in held-out skill over a null model range from negligible to large (Van Sickle et al. 2005)."
  why: Van Sickle's SDs of O/E are precision across the reference sites used to build the models, calibration-site evidence, and were folded into held-out skill-over-baseline evidence alongside Statzner 2005. · instead: bioassessment.4 · trail: C-PREDICT §Answers as delivered, §Properties that raise, §critic, §Adversarial critique · from: C-PREDICT:A-060, C-PREDICT:B-0142, C-PREDICT:C-033, C-PREDICT:C-048, C-PREDICT:C-107
- **dns.4** "Statzner et al. 2005 found that landscape models gained negligibly over a mean-profile model at held-out reaches."
  why: The abstract, the only part read, does not state that the comparison was made at held-out reaches; that framing comes from Hawkins et al. 2010, so it should be cited to that review and labelled SECONDARY. · instead: trait-baseline.1 · trail: C-PREDICT §Freshwater bioassessment, §critic, §Adversarial critique · from: C-PREDICT:B-0112, C-PREDICT:C-049, C-PREDICT:C-053..055
- **dns.5** "Trait profiles barely vary among natural reaches, so a constant already predicts them."
  why: This is the reviewer's inference attached to Statzner 2005 as if it were the source's explanation, phrased as a general property of trait profiles, and the Statzner abstract itself reports that many trait categories changed along 13 rivers. · instead: trait-baseline.3, trait-baseline.2 · trail: C-PREDICT §Freshwater bioassessment, §critic, §Adversarial critique · from: C-PREDICT:B-0113, C-PREDICT:C-036, C-PREDICT:C-062, C-PREDICT:C-115
- **dns.6** "Because trait profiles vary little across reference sites, low raw error and low skill over baseline can coexist."
  why: It is the reviewer's own mechanistic argument, presented in the answer without a label, resting on Statzner 2005 (abstract only) plus inference. · instead: trait-baseline.3 · trail: C-PREDICT §Answers as delivered, §Adversarial critique · from: C-PREDICT:A-061, C-PREDICT:C-062, C-PREDICT:C-114
- **dns.7** "The one bioassessment result that bears on skill against a baseline cuts the other way from a naive traits-are-more-predictable reading."
  why: It uses a single trait-only study with no taxonomic counterpart as if it were a comparative result, frames the evidence against a hypothesis the literature reviewed does not state, and applies the baseline caution to the trait side only. · instead: trait-baseline.1 · trail: C-PREDICT §Answers as delivered, §critic, §Adversarial critique · from: C-PREDICT:A-015, C-PREDICT:A-020, C-PREDICT:C-016, C-PREDICT:C-064, C-PREDICT:C-103..105, C-PREDICT:C-113
- **dns.8** "Across stream macroinvertebrates, fish, macrophytes, diatoms and lake phytoplankton, trait composition is more closely tied to environment than species composition, a moderate and replicated pattern."
  why: The claim merges three measures (closeness of fit to environment, consistency of responses across regions, lower variability), every source behind it was read as abstract only, most come from one macroinvertebrate research network, and it is moderate at best and not replicated across organism groups. · instead: explanatory-other.11, explanatory-other.1, explanatory-other.4, explanatory-other.7 · trail: C-PREDICT §Answers as delivered, §critic, §Adversarial critique · from: C-PREDICT:A-013, C-PREDICT:C-050, C-PREDICT:C-108
- **dns.9** "Trait profiles vary less across sites, regions and seasons than taxonomic profiles."
  why: Phrased generally, it rests on three abstract-only stream-macroinvertebrate studies from overlapping author groups, which are not independent replicates across organism groups. · instead: explanatory-other.9 · trail: C-PREDICT §Answers as delivered, §Adversarial critique · from: C-PREDICT:A-013, C-PREDICT:C-063
- **dns.10** "Kruk et al. 2011 show that functional groups are more predictable than taxa."
  why: Its comparison is morphology-based groups against phylogenetic groups (a coarse taxonomic aggregate), Reynolds groups and single species, in-sample, in one dataset. · instead: explanatory-other.3 · trail: C-PREDICT §Explanatory comparisons, §Adversarial critique · from: C-PREDICT:B-0100, C-PREDICT:C-067, C-PREDICT:C-112
- **dns.11** "Fungi tend to be more predictable at broad taxonomic ranks."
  why: It rests on Werbin 2024 alone, a preprint, and the review's own recomputation of Averill contradicts it. · instead: resolution.2, averill.7 · trail: C-PREDICT §Answers as delivered, §Adversarial critique · from: C-PREDICT:A-031, C-PREDICT:C-065
- **dns.12** "Taxonomic rank shows no consistent direction in how predictable microbial profiles are."
  why: The answer misses a 2026 reanalysis of the same Averill and NEON data (Aouabed et al.) that reports predictability rising with taxonomic scale, a 2026 New Phytologist study in which broad groups were predicted best, and the within-NEON cross-validation figure in Averill's own Extended Data; both missed reports lean towards broader ranks. · instead: resolution.1, resolution.8 · trail: C-PREDICT §Answers as delivered, §critic · from: C-PREDICT:A-031, C-PREDICT:C-022, C-PREDICT:C-051
- **dns.13** "In freshwater bioassessment, species-level models predicted held-out sites better than family-level models (Hawkins et al. 2000)."
  why: The abstract does not show the evaluation sites were independent, and the comparison is confounded with the Pc threshold choice varied at the same time, so it is not a held-out species-versus-family result. · instead: bioassessment.2 · trail: C-PREDICT §Answers as delivered, §critic, §Adversarial critique · from: C-PREDICT:A-031, C-PREDICT:C-024, C-PREDICT:C-025, C-PREDICT:C-061, C-PREDICT:C-110
- **dns.14** "Higher abundance raises held-out skill of taxonomic profiles across all of Werbin et al.'s groups."
  why: Werbin's all-groups result merges derived functional groups with taxonomic groups under the taxonomic label. · instead: skill-properties.1 · trail: C-PREDICT §Properties that raise, §Adversarial critique · from: C-PREDICT:B-0131, C-PREDICT:C-109
- **dns.15** "Plant community-weighted means predicted better than trait diversity indices show how resolution in the trait hierarchy affects predictability."
  why: Means against diversity indices concern the choice of summary statistic, not the level of the trait hierarchy, though they sit in the resolution answer. · instead: plant-traits.4 · trail: C-PREDICT §Answers as delivered, §Adversarial critique · from: C-PREDICT:A-041, C-PREDICT:C-111
- **dns.16** "Maguire et al. 2016 found that species and community models both failed in novel climates."
  why: As the whole finding this is one-sided: the abstract also reports that community-level models generally outperformed SDMs in novel climates and did not overfit. · instead: hold-out-design.4 · trail: C-PREDICT §Transferability, bounds, §Adversarial critique · from: C-PREDICT:B-0123, C-PREDICT:C-099..101

## Gaps
- **gap.1** Aouabed et al. 2026 (Scientific Reports), a same-study derived-profile comparison on the Averill and NEON datasets, was read only in abstract by the critic; its hold-out design is unverified.
  blocks: derived-comparison.3, resolution.6 · origin: critic coverage gap · search: not stated · src: aouabedSoilMicrobiomePrediction2026 · from: C-PREDICT:C-011, C-PREDICT:C-083..086 · trail: C-PREDICT §Adversarial critique
- **gap.2** Averill et al. 2021's main text (Fig. 4, per-rank skill) was not obtained, and its Extended Data Fig. 1 (within-NEON 70/30 random cross-validation, 1:1 R2 across functional and taxonomic groups) and Extended Data Fig. 2 (coefficients of variation across groupings, in and out of sample) went unreported though the captions were obtained; the stage-2 check says the main text should be read in full by hand, since D1 and D2 lean on it.
  blocks: averill · origin: critic coverage gap; source not obtained; stage 2 check · search: not stated · src: averillSoilMicrobiomePredictability2021 · from: C-PREDICT:C-007, C-PREDICT:C-057, C-PREDICT:C-087, C-PREDICT:B-0024, C-PREDICT:R-0002, C-PREDICT:R-0003 · trail: C-PREDICT §critic, §Adversarial critique, §Stage 2 check, §Sources not obtained
- **gap.3** Remote-sensing-predictor studies of soil microbial composition at several resolutions (for example the 2026 New Phytologist canopy-reflectance study at 14 NEON domains) were not found or discussed.
  blocks: resolution · origin: critic coverage gap · search: not stated · src: anon2026 · from: C-PREDICT:C-088 · trail: C-PREDICT §Adversarial critique
- **gap.4** The trait-based SDM transferability literature (Vesk et al. 2021; Pollock et al. 2012) and fourth-corner and HMSC trait-environment prediction, the plant and animal counterparts comparing trait-based with taxon-based prediction at held-out units, were not searched; the stage-2 routing check was triggered and calls for a follow-up brief on the trait-based SDM and bioassessment transfer literature, sized separately.
  blocks: direct-evidence.6 · origin: critic coverage gap; stage 2 check (triggered) · search: not searched (critic: C-089) · src: vesk2021, pollock2012 · from: C-PREDICT:C-089, C-PREDICT:B-0020..0023 · trail: C-PREDICT §Adversarial critique, §Stage 2 check
- **gap.5** Community-level modelling benchmarks beyond Norberg 2019 and Zurell 2020 (Ferrier and Guisan 2006; Baselga and Araújo 2010; Yates et al. 2018) are not covered, so the joint-SDM transferability evidence rests on one benchmark.
  blocks: hold-out-design · origin: critic coverage gap · search: not stated · src: ferrier2006, baselga2010, yates2018 · from: C-PREDICT:C-090 · trail: C-PREDICT §Adversarial critique
- **gap.6** Marine measured metagenomic and metatranscriptomic prediction beyond Faure 2021 (Tara Oceans gene-abundance models, the Salazar et al. 2019 Tara metatranscriptome, BioGEOTRACES gene-based niche models) was not searched as held-out prediction of gene profiles; the microbial measured-gene case rests on one study.
  blocks: one-profile-studies, direct-evidence.5 · origin: critic coverage gap · search: not searched (critic: C-091) · src: salazar2019 · from: C-PREDICT:C-091 · trail: C-PREDICT §Adversarial critique
- **gap.7** No freshwater, sediment, groundwater or lake microbial held-out prediction studies were found for either profile type, and no host-free engineered systems other than activated sludge; the query routes used for these settings are not named.
  blocks: direct-evidence.4 · origin: critic coverage gap · search: not stated (critic: C-092) · from: C-PREDICT:C-092 · trail: C-PREDICT §Adversarial critique
- **gap.8** Functional-hierarchy resolution: no search for studies comparing KO, module, pathway and category (or CAZy family versus class) predictability or environmental fit, even explanatory ones such as metagenome-wide comparisons of KEGG level 1 to 3.
  blocks: resolution.9 · origin: critic coverage gap; stage 2 check · search: not searched (critic: C-093) · from: C-PREDICT:C-093 · trail: C-PREDICT §Adversarial critique
- **gap.9** Trait-based bioassessment reference models: sources central to D1 and D2 (Vander Laan and Hawkins 2014, Mondy et al. 2012, Van Sickle et al. 2007, Clarke et al. 2003) were not obtained, no alternative route is recorded, and the trait-profile O/E literature (Dolédec and Statzner 2008) is absent.
  blocks: bioassessment.6 · origin: critic coverage gap; sources not obtained · search: not stated · src: vanderlaanEnhancingPerformanceInterpretation2014, mondyNewMacroinvertebratebasedMultimetric2012, vansickleExclusionRareTaxa2007, clarkeRIVPACSModelsPredicting2003, doledec2008 · from: C-PREDICT:C-094, C-PREDICT:R-0010, C-PREDICT:R-0011, C-PREDICT:R-0015, C-PREDICT:R-0016, C-PREDICT:R-0025..0028, C-PREDICT:R-0060..0063 · trail: C-PREDICT §Adversarial critique, §Sources not obtained
- **gap.10** Temporal hold-outs in earlier-period (hindcast) and interleaved designs, and long-term microbial time series (SPOT, BATS, the Western Channel Observatory beyond Larsen 2012, Helgoland) predicted out of period, are not searched for either profile type.
  blocks: direct-evidence.3 · origin: critic coverage gap · search: not searched (critic: C-095) · from: C-PREDICT:C-095 · trail: C-PREDICT §Adversarial critique
- **gap.11** The full-text labels for Werbin et al. 2024, Liu 2023, Hawkins 2010, Norberg 2019, the Frémont preprint, Fuhrman 2006 and Ladau 2018 rest on search agents and were not re-opened by the synthesis, so load-bearing Werbin specifics (fungal functional groups more environment-sensitive, 65% against 8% CRPS, evaluation at calibration sites) are second-hand within the pipeline.
  blocks: werbin, skill-properties.5 · origin: critic access finding · search: not stated · src: werbinForecastingSoilMicrobiome2024, liuPredictingMicrobialCommunity2023, hawkinsReferenceConditionPredicting2010, norbergComprehensiveEvaluationPredictive2019, fremontRestructuringPlanktonGenomic2022, fuhrmanAnnuallyReoccurringBacterial2006, ladauExistingClimateChange2018 · from: C-PREDICT:C-058, C-PREDICT:C-059 · trail: C-PREDICT §Adversarial critique
- **gap.12** Bioassessment sources on taxonomic resolution and functional against taxonomic models were not obtained: Hawkins and Norris 2000 (taxonomic resolution and subsets of the fauna in RIVPACS-type models), Dolédec, Olivier and Statzner 2000 (taxonomic and spatial resolution of taxa and traits), Heino 2014 (taxonomic surrogacy and transferability among regions) and Di Maggio et al. 2016 (taxonomic against functional groups-based phytoplankton models).
  blocks: resolution, bioassessment · origin: sources not obtained · search: not stated · src: hawkinsEffectsTaxonomicResolution2000, doledecAccurateDescriptionAbundance2000, heinoTaxonomicSurrogacyNumerical2014, dimaggioModelingPhytoplanktonCommunity2016 · from: C-PREDICT:R-0037..0055, C-PREDICT:R-0064..0069 · trail: C-PREDICT §Sources not obtained
- **gap.13** Other sources listed as not obtained: Wilhelm, van Es and Buckley 2022 (predicting soil health from the microbiome), Chessman and Royal 2004 (bioassessment without reference sites) and Statzner et al. 2001 (functional composition of invertebrate communities in European running waters).
  blocks: none · origin: sources not obtained · search: not stated · src: wilhelmPredictingMeasuresSoil2021, chessmanBioassessmentReferenceSites2004, statznerPerspectivesBiomonitoringLarge2001 · from: C-PREDICT:R-0012, C-PREDICT:R-0013, C-PREDICT:R-0017, C-PREDICT:R-0033..0036, C-PREDICT:R-0056..0059 · trail: C-PREDICT §Sources not obtained
- **gap.14** The note contradicts itself on access: its Sources not obtained list says "Nothing beyond a citation was reachable for these; none supports any claim in the review", yet several sources on that list (Louca et al. 2016, Galand et al. 2018, Larsen et al. 2012, Feio and Dolédec 2012, Hawkins et al. 2000, Van Sickle et al. 2005, Frémont et al. 2022, Bruelheide et al. 2018) are cited in the review as read in abstract (or, for Frémont, as a preprint read in full).
  blocks: none · origin: the note contradicts itself · search: not stated · src: loucaDecouplingFunctionTaxonomy2016, galandStrongLinkMarine2018, larsenPredictingBacterialCommunity2012, feioIntegrationInvertebrateTraits2012, hawkinsDEVELOPMENTEVALUATIONPREDICTIVE2000, vansickleNullModelExpected2005, fremontRestructuringPlanktonGenomic2022, bruelheideGlobalTraitenvironmentRelationships2018 · from: C-PREDICT:R-0001, C-PREDICT:R-0004..0009, C-PREDICT:R-0014, C-PREDICT:R-0018..0024, C-PREDICT:R-0029..0032 · trail: C-PREDICT §Sources not obtained

## Out of scope
- C-PREDICT:A-001, C-PREDICT:A-030, C-PREDICT:A-051: question headings of the answers (routing, not findings)
- C-PREDICT:A-023, C-PREDICT:A-024, C-PREDICT:A-047..049, C-PREDICT:A-070: access basis of the answers (provenance, kept in the result note; applied in Sources)
- C-PREDICT:C-040, C-PREDICT:C-041, C-PREDICT:C-046: the critic's overall assessment and its framing of the over-reach list (verification, kept in the result note)
- C-PREDICT:C-068..082: reference corrections and the critic's Crossref check, applied in Sources
- C-PREDICT:C-116: the critic's check found no evaluation or endorsement of a research design (no finding)

## Sources
```bibtex
@article{averillSoilMicrobiomePredictability2021,
  author = {Averill, Colin and Werbin, Zoey R. and Atherton, Kathryn F. and Bhatnagar, Jennifer M. and Dietze, Michael C.},
  title = {Soil microbiome predictability increases with spatial and taxonomic scale},
  journal = {Nature Ecology \& Evolution},
  volume = {5},
  number = {6},
  pages = {747--756},
  year = {2021},
  doi = {10.1038/s41559-021-01445-9},
  note = {access: abstract_only (C-PREDICT; main text not read by any agent, paywalled), full_text (C-PREDICT; Supplementary Data 1, re-opened and recomputed by the reviewer; peer-review file via a search agent); main text body listed in Sources not obtained; cited as: C-PREDICT [1]}
}
@misc{werbinForecastingSoilMicrobiome2024,
  author = {Werbin, Zoey and Averill, Colin and Bhatnagar, Jennifer and Dietze, Michael},
  title = {Forecasting the soil microbiome at a continental scale},
  howpublished = {Research Square preprint, posted 13 November 2024},
  year = {2024},
  doi = {10.21203/rs.3.rs-5183308/v1},
  note = {access: full_text (C-PREDICT; preprint, via search agents, not re-opened by the synthesis, critic: C-PREDICT:C-058; the critic read the abstract); type: preprint, not peer reviewed; cited as: C-PREDICT [2]}
}
@article{liuPredictingMicrobialCommunity2023,
  author = {Liu, Xiaonan and Nie, Yong and Wu, Xiao-Lei},
  title = {Predicting microbial community compositions in wastewater treatment plants using artificial neural networks},
  journal = {Microbiome},
  volume = {11},
  number = {1},
  pages = {93},
  year = {2023},
  doi = {10.1186/s40168-023-01519-9},
  note = {access: full_text (C-PREDICT; via a search agent, not re-opened by the synthesis, critic: C-PREDICT:C-058); cited as: C-PREDICT [3]}
}
@article{faureTowardsOmicsbasedPredictions2021,
  author = {Faure, Emile and Ayata, Sakina-Dorothée and Bittner, Lucie},
  title = {Towards omics-based predictions of planktonic functional composition from environmental data},
  journal = {Nature Communications},
  volume = {12},
  number = {1},
  pages = {4361},
  year = {2021},
  doi = {10.1038/s41467-021-24547-1},
  note = {access: full_text (C-PREDICT; via a search agent; numbers matched to the full text by the critic); cited as: C-PREDICT [4]}
}
@article{fremontRestructuringPlanktonGenomic2022,
  author = {Frémont, Paul and Gehlen, Marion and Vrac, Mathieu and Leconte, Jade and Delmont, Tom O. and Wincker, Patrick and Iudicone, Daniele and Jaillon, Olivier},
  title = {Restructuring of plankton genomic biogeography in the surface ocean under climate change},
  journal = {Nature Climate Change},
  volume = {12},
  number = {4},
  pages = {393--401},
  year = {2022},
  doi = {10.1038/s41558-022-01314-8},
  note = {access: full_text (C-PREDICT; of the bioRxiv preprint 10.1101/2020.10.20.347237, read by a search agent, not re-opened by the synthesis; published version not read); the version read is the preprint (critic: C-PREDICT:C-077..079: cite the version read; the note cited the published version); conflict: also listed in Sources not obtained (Europe PMC preprint abstract only, bioRxiv API failed); cited as: C-PREDICT [5]}
}
@article{tangDataDrivenModelingDistribution2019,
  author = {Tang, Weiyi and Cassar, Nicolas},
  title = {Data-driven modeling of the distribution of diazotrophs in the global ocean},
  journal = {Geophysical Research Letters},
  volume = {46},
  number = {21},
  pages = {12258--12269},
  year = {2019},
  doi = {10.1029/2019GL084376},
  note = {access: abstract_only (C-PREDICT); cited as: C-PREDICT [6]}
}
@article{ouGlobalAtlasMethane2024,
  author = {Ou, Yafei and Ren, Zhongda and Chen, Xi and Jiang, Zhenran and Liu, Qiancai and Li, Xiaofei and Zheng, Yanling and Liang, Xia and Liu, Min and Hou, Lijun and Dong, Hongpo},
  title = {Global atlas of methane metabolism marker genes in soil},
  journal = {Environmental Science \& Technology},
  volume = {58},
  number = {21},
  pages = {9261--9271},
  year = {2024},
  doi = {10.1021/acs.est.4c02827},
  note = {access: abstract_only (C-PREDICT); given names from Crossref (critic: C-PREDICT:C-072..074; the note gave initials and called them unverified); cited as: C-PREDICT [7]}
}
@article{modPredictingSpatialPatterns2021,
  author = {Mod, Heidi K. and Buri, Aline and Yashiro, Erika and Guex, Nicolas and Malard, Lucie and Pinto-Figueroa, Eric and Pagni, Marco and Niculita-Hirzel, Hélène and van der Meer, Jan Roelof and Guisan, Antoine},
  title = {Predicting spatial patterns of soil bacteria under current and future environmental conditions},
  journal = {The ISME Journal},
  volume = {15},
  number = {9},
  pages = {2547--2560},
  year = {2021},
  doi = {10.1038/s41396-021-00947-5},
  note = {access: full_text (C-PREDICT; via search agents; verified by the critic in full text); cited as: C-PREDICT [8]}
}
@article{ladauExistingClimateChange2018,
  author = {Ladau, Joshua and Shi, Yu and Jing, Xin and He, Jin-Sheng and Chen, Litong and Lin, Xiangui and Fierer, Noah and Gilbert, Jack A. and Pollard, Katherine S. and Chu, Haiyan},
  title = {Existing climate change will lead to pronounced shifts in the diversity of soil prokaryotes},
  journal = {mSystems},
  volume = {3},
  number = {5},
  pages = {e00167-18},
  year = {2018},
  doi = {10.1128/mSystems.00167-18},
  note = {access: full_text (C-PREDICT; methods; via search agents, not re-opened by the synthesis, critic: C-PREDICT:C-058); cited as: C-PREDICT [9]}
}
@article{larsenPredictingBacterialCommunity2012,
  author = {Larsen, Peter E. and Field, Dawn and Gilbert, Jack A.},
  title = {Predicting bacterial community assemblages using an artificial neural network approach},
  journal = {Nature Methods},
  volume = {9},
  number = {6},
  pages = {621--625},
  year = {2012},
  doi = {10.1038/nmeth.1975},
  note = {access: abstract_only (C-PREDICT); conflict: full text listed in Sources not obtained, whose heading says nothing beyond a citation was reachable; cited as: C-PREDICT [10]}
}
@article{fuhrmanAnnuallyReoccurringBacterial2006,
  author = {Fuhrman, Jed A. and Hewson, Ian and Schwalbach, Michael S. and Steele, Joshua A. and Brown, Mark V. and Naeem, Shahid},
  title = {Annually reoccurring bacterial communities are predictable from ocean conditions},
  journal = {Proceedings of the National Academy of Sciences USA},
  volume = {103},
  number = {35},
  pages = {13104--13109},
  year = {2006},
  doi = {10.1073/pnas.0602399103},
  note = {access: full_text (C-PREDICT; via search agents, not re-opened by the synthesis, critic: C-PREDICT:C-058); cited as: C-PREDICT [11]}
}
@article{loucaDecouplingFunctionTaxonomy2016,
  author = {Louca, Stilianos and Parfrey, Laura Wegener and Doebeli, Michael},
  title = {Decoupling function and taxonomy in the global ocean microbiome},
  journal = {Science},
  volume = {353},
  number = {6305},
  pages = {1272--1277},
  year = {2016},
  doi = {10.1126/science.aaf4507},
  note = {access: abstract_only (C-PREDICT); conflict: full text listed in Sources not obtained, whose heading says nothing beyond a citation was reachable; cited as: C-PREDICT [12]}
}
@misc{ohigashiAgriculturalLandUse2025,
  author = {Ohigashi, Takamitsu and Madegwa, Yvonne M. and Karuku, George N. and Njira, Keston and Uchida, Yoshitaka},
  title = {Agricultural land use induces broader homogenization of soil microbial functional composition than taxonomic composition},
  howpublished = {bioRxiv preprint},
  year = {2025},
  doi = {10.1101/2025.02.17.638669},
  note = {access: abstract_only (C-PREDICT); type: preprint; given names from Crossref (critic: C-PREDICT:C-075; the note gave initials only); cited as: C-PREDICT [13]}
}
@article{nelsonGlobalBiogeographyMicrobial2016,
  author = {Nelson, Michaeline B. and Martiny, Adam C. and Martiny, Jennifer B. H.},
  title = {Global biogeography of microbial nitrogen-cycling traits in soil},
  journal = {Proceedings of the National Academy of Sciences USA},
  volume = {113},
  number = {29},
  pages = {8033--8040},
  year = {2016},
  doi = {10.1073/pnas.1601070113},
  note = {access: abstract_only (C-PREDICT); cited as: C-PREDICT [14]}
}
@article{bahramStructureFunctionGlobal2018,
  author = {Bahram, Mohammad and Hildebrand, Falk and Forslund, Sofia K. and Anderson, Jennifer L. and Soudzilovskaia, Nadejda A. and Bodegom, Peter M. and Bengtsson-Palme, Johan and Anslan, Sten and Coelho, Luis Pedro and Harend, Helery and Huerta-Cepas, Jaime and Medema, Marnix H. and Maltz, Mia R. and Mundra, Sunil and Olsson, Pål Axel and Pent, Mari and Põlme, Sergei and Sunagawa, Shinichi and Ryberg, Martin and Tedersoo, Leho and Bork, Peer},
  title = {Structure and function of the global topsoil microbiome},
  journal = {Nature},
  volume = {560},
  number = {7717},
  pages = {233--237},
  year = {2018},
  doi = {10.1038/s41586-018-0386-6},
  note = {access: abstract_only (C-PREDICT); cited as: C-PREDICT [15]}
}
@article{fiererCrossbiomeMetagenomicAnalyses2012,
  author = {Fierer, Noah and Leff, Jonathan W. and Adams, Byron J. and Nielsen, Uffe N. and Bates, Scott Thomas and Lauber, Christian L. and Owens, Sarah and Gilbert, Jack A. and Wall, Diana H. and Caporaso, J. Gregory},
  title = {Cross-biome metagenomic analyses of soil microbial communities and their functional attributes},
  journal = {Proceedings of the National Academy of Sciences USA},
  volume = {109},
  number = {52},
  pages = {21390--21395},
  year = {2012},
  doi = {10.1073/pnas.1215210110},
  note = {access: abstract_only (C-PREDICT); cited as: C-PREDICT [16]}
}
@article{galandStrongLinkMarine2018,
  author = {Galand, Pierre E. and Pereira, Olivier and Hochart, Corentin and Auguet, Jean Christophe and Debroas, Didier},
  title = {A strong link between marine microbial community composition and function challenges the idea of functional redundancy},
  journal = {The ISME Journal},
  volume = {12},
  number = {10},
  pages = {2470--2478},
  year = {2018},
  doi = {10.1038/s41396-018-0158-1},
  note = {access: abstract_only (C-PREDICT); conflict: full text listed in Sources not obtained, whose heading says nothing beyond a citation was reachable; cited as: C-PREDICT [17]}
}
@article{liuAnthropogenicActivitiesChange2021,
  author = {Liu, Lemian and Wang, Shanshan and Chen, Jianfeng},
  title = {Anthropogenic activities change the relationship between microbial community taxonomic composition and functional attributes},
  journal = {Environmental Microbiology},
  volume = {23},
  number = {11},
  pages = {6663--6675},
  year = {2021},
  doi = {10.1111/1462-2920.15702},
  note = {access: abstract_only (C-PREDICT); given names from Crossref (critic: C-PREDICT:C-076; the note gave initials only); cited as: C-PREDICT [18]}
}
@misc{qingqingTaxonomicFunctionalBiogeography2024,
  author = {Liang, Qingqing and Mod, Heidi K. and Luo, Shuaiwei and Ma, Beibei and Yang, Kena and Chen, Beibei and Qi, Wei and Zhao, Zhiguang and Du, Guozhen and Guisan, Antoine and Ma, Xiaojun and Le Roux, Xavier},
  title = {Taxonomic and functional biogeography of soil bacteria: importance of environmental filtering and dispersal depends on scale},
  howpublished = {Authorea preprint},
  year = {2024},
  doi = {10.22541/au.170666982.24064936/v1},
  note = {access: abstract_only (C-PREDICT); type: preprint; author list corrected to 12 authors ending with Xavier Le Roux (critic: C-PREDICT:C-068..070; the note added 'Liang, Qi' as a 13th; the Crossref record itself is garbled); cited as: C-PREDICT [19]}
}
@article{loucaHighTaxonomicVariability2016,
  author = {Louca, Stilianos and Jacques, Saulo M. S. and Pires, Aliny P. F. and Leal, Juliana S. and Srivastava, Diane S. and Parfrey, Laura Wegener and Farjalla, Vinicius F. and Doebeli, Michael},
  title = {High taxonomic variability despite stable functional structure across microbial communities},
  journal = {Nature Ecology \& Evolution},
  volume = {1},
  number = {1},
  pages = {0015},
  year = {2016},
  doi = {10.1038/s41559-016-0015},
  note = {access: abstract_only (C-PREDICT); Crossref records pages 1-12 for article 0015 (critic: C-PREDICT:C-081); cited as: C-PREDICT [20]}
}
@article{burkeBacterialCommunityAssembly2011,
  author = {Burke, Catherine and Steinberg, Peter and Rusch, Doug and Kjelleberg, Staffan and Thomas, Torsten},
  title = {Bacterial community assembly based on functional genes rather than species},
  journal = {Proceedings of the National Academy of Sciences USA},
  volume = {108},
  number = {34},
  pages = {14288--14293},
  year = {2011},
  doi = {10.1073/pnas.1101591108},
  note = {access: abstract_only (C-PREDICT); cited as: C-PREDICT [21]}
}
@article{theStructureFunctionDiversity2012,
  author = {{The Human Microbiome Project Consortium}},
  title = {Structure, function and diversity of the healthy human microbiome},
  journal = {Nature},
  volume = {486},
  number = {7402},
  pages = {207--214},
  year = {2012},
  doi = {10.1038/nature11234},
  note = {access: abstract_only (C-PREDICT); cited as: C-PREDICT [22]}
}
@article{colesOceanBiogeochemistryModeled2017,
  author = {Coles, V. J. and Stukel, M. R. and Brooks, M. T. and Burd, A. and Crump, B. C. and Moran, M. A. and Paul, J. H. and Satinsky, B. M. and Yager, P. L. and Zielinski, B. L. and Hood, R. R.},
  title = {Ocean biogeochemistry modeled with emergent trait-based genomics},
  journal = {Science},
  volume = {358},
  number = {6367},
  pages = {1149--1154},
  year = {2017},
  doi = {10.1126/science.aan5712},
  note = {access: abstract_only (C-PREDICT); given names not verified; incomplete: author given names; cited as: C-PREDICT [23]}
}
@article{gotheEnvironmentalSpatialControls2016,
  author = {Göthe, Emma and Baattrup-Pedersen, Annette and Wiberg-Larsen, Peter and Graeber, Daniel and Kristensen, Esben A. and Friberg, Nikolai},
  title = {Environmental and spatial controls of taxonomic versus trait composition of stream biota},
  journal = {Freshwater Biology},
  volume = {62},
  number = {2},
  pages = {397--413},
  year = {2017},
  doi = {10.1111/fwb.12875},
  note = {access: abstract_only (C-PREDICT); Crossref online 2016; cited as: C-PREDICT [24]}
}
@article{soininenGlobalPatternsDrivers2016,
  author = {Soininen, Janne and Jamoneau, Aurélien and Rosebery, Juliette and Passy, Sophia I.},
  title = {Global patterns and drivers of species and trait composition in diatoms},
  journal = {Global Ecology and Biogeography},
  volume = {25},
  number = {8},
  pages = {940--950},
  year = {2016},
  doi = {10.1111/geb.12452},
  note = {access: abstract_only (C-PREDICT); cited as: C-PREDICT [25]}
}
@article{krukPhytoplanktonCommunityComposition2010,
  author = {Kruk, C. and Peeters, E. T. H. M. and Van Nes, E. H. and Huszar, V. L. M. and Costa, L. S. and Scheffer, M.},
  title = {Phytoplankton community composition can be predicted best in terms of morphological groups},
  journal = {Limnology and Oceanography},
  volume = {56},
  number = {1},
  pages = {110--118},
  year = {2011},
  doi = {10.4319/lo.2011.56.1.0110},
  note = {access: abstract_only (C-PREDICT); cited as: C-PREDICT [26]}
}
@article{doledecInvertebrateCommunityResponses2011,
  author = {Dolédec, Sylvain and Phillips, Ngaire and Townsend, Colin},
  title = {Invertebrate community responses to land use at a broad spatial scale: trait and taxonomic measures compared in New Zealand rivers},
  journal = {Freshwater Biology},
  volume = {56},
  number = {8},
  pages = {1670--1688},
  year = {2011},
  doi = {10.1111/j.1365-2427.2011.02597.x},
  note = {access: abstract_only (C-PREDICT); cited as: C-PREDICT [27]}
}
@article{hoeinghausLocalRegionalDeterminants2006,
  author = {Hoeinghaus, David J. and Winemiller, Kirk O. and Birnbaum, Jenny S.},
  title = {Local and regional determinants of stream fish assemblage structure: inferences based on taxonomic vs. functional groups},
  journal = {Journal of Biogeography},
  volume = {34},
  number = {2},
  pages = {324--338},
  year = {2007},
  doi = {10.1111/j.1365-2699.2006.01587.x},
  note = {access: abstract_only (C-PREDICT); cited as: C-PREDICT [28]}
}
@article{charvetTraitsBenthicMacroinvertebrates2000,
  author = {Charvet, Stéphane and Statzner, Bernhard and Usseglio-Polatera, Philippe and Dumont, Bernard},
  title = {Traits of benthic macroinvertebrates in semi-natural French streams: an initial application to biomonitoring in Europe},
  journal = {Freshwater Biology},
  volume = {43},
  number = {2},
  pages = {277--296},
  year = {2000},
  doi = {10.1046/j.1365-2427.2000.00545.x},
  note = {access: abstract_only (C-PREDICT); cited as: C-PREDICT [29]}
}
@article{bonadaTaxonomicBiologicalTrait2007,
  author = {Bonada, Núria and Dolédec, Sylvain and Statzner, Bernhard},
  title = {Taxonomic and biological trait differences of stream macroinvertebrate communities between mediterranean and temperate regions: implications for future climatic scenarios},
  journal = {Global Change Biology},
  volume = {13},
  number = {8},
  pages = {1658--1671},
  year = {2007},
  doi = {10.1111/j.1365-2486.2007.01375.x},
  note = {access: abstract_only (C-PREDICT); cited as: C-PREDICT [30]}
}
@article{becheLongtermSeasonalVariation2005,
  author = {Bêche, Leah A. and McElravy, Eric P. and Resh, Vincent H.},
  title = {Long-term seasonal variation in the biological traits of benthic-macroinvertebrates in two Mediterranean-climate streams in California, U.S.A.},
  journal = {Freshwater Biology},
  volume = {51},
  number = {1},
  pages = {56--75},
  year = {2006},
  doi = {10.1111/j.1365-2427.2005.01473.x},
  note = {access: abstract_only (C-PREDICT); cited as: C-PREDICT [31]}
}
@article{bruelheideGlobalTraitenvironmentRelationships2018,
  author = {Bruelheide, Helge and Dengler, Jürgen and Purschke, Oliver and Lenoir, Jonathan and Jiménez-Alfaro, Borja and Hennekens, Stephan M. and Botta-Dukát, Zoltán and Chytrý, Milan and Field, Richard and Jansen, Florian and Kattge, Jens and Pillar, Valério D. and Schrodt, Franziska and Mahecha, Miguel D. and Peet, Robert K. and Sandel, Brody and van Bodegom, Peter and others},
  title = {Global trait-environment relationships of plant communities},
  journal = {Nature Ecology \& Evolution},
  volume = {2},
  number = {12},
  pages = {1906--1917},
  year = {2018},
  doi = {10.1038/s41559-018-0699-8},
  note = {access: abstract_only (C-PREDICT); incomplete: author (105 in Crossref, 17 transcribed; critic: C-PREDICT:C-071); conflict: also listed in Sources not obtained (OpenAlex no abstract); cited as: C-PREDICT [32]}
}
@article{hawkinsDEVELOPMENTEVALUATIONPREDICTIVE2000,
  author = {Hawkins, Charles P. and Norris, Richard H. and Hogue, James N. and Feminella, Jack W.},
  title = {Development and evaluation of predictive models for measuring the biological integrity of streams},
  journal = {Ecological Applications},
  volume = {10},
  number = {5},
  pages = {1456--1477},
  year = {2000},
  doi = {10.1890/1051-0761(2000)010[1456:DAEOPM]2.0.CO;2},
  note = {access: abstract_only (C-PREDICT; OpenAlex abstract; the critic verified the abstract and the Crossref record, C-PREDICT:C-080); conflict: full text listed in Sources not obtained, whose heading says nothing beyond a citation was reachable; cited as: C-PREDICT [33]}
}
@article{mossComparisonAlternativeTechniques1999,
  author = {Moss, D. and Wright, J. F. and Furse, M. T. and Clarke, R. T.},
  title = {A comparison of alternative techniques for prediction of the fauna of running-water sites in Great Britain},
  journal = {Freshwater Biology},
  volume = {41},
  number = {1},
  pages = {167--181},
  year = {1999},
  doi = {10.1046/j.1365-2427.1999.00376.x},
  note = {access: abstract_only (C-PREDICT); cited as: C-PREDICT [34]}
}
@article{vansickleNullModelExpected2005,
  author = {Van Sickle, John and Hawkins, Charles P. and Larsen, David P. and Herlihy, Alan T.},
  title = {A null model for the expected macroinvertebrate assemblage in streams},
  journal = {Journal of the North American Benthological Society},
  volume = {24},
  number = {1},
  pages = {178--191},
  year = {2005},
  doi = {10.1899/0887-3593(2005)024<0178:ANMFTE>2.0.CO;2},
  note = {access: abstract_only (C-PREDICT; OpenAlex; verified by the critic; one search agent could not reach it and knew it only through Hawkins et al. 2010); conflict: listed twice in Sources not obtained, once as known only via the Hawkins et al. 2010 description; cited as: C-PREDICT [35]}
}
@article{mykraPredictingStreamMacroinvertebrate2008,
  author = {Mykrä, Heikki and Aroviita, Jukka and Kotanen, Juho and Hämäläinen, Heikki and Muotka, Timo},
  title = {Predicting the stream macroinvertebrate fauna across regional scales: influence of geographical extent on model performance},
  journal = {Journal of the North American Benthological Society},
  volume = {27},
  number = {3},
  pages = {705--716},
  year = {2008},
  doi = {10.1899/07-074.1},
  note = {access: abstract_only (C-PREDICT); cited as: C-PREDICT [36]}
}
@article{statznerInvertebrateTraitsBiomonitoring2005,
  author = {Statzner, Bernhard and Bady, Pierre and Dolédec, Sylvain and Schöll, Franz},
  title = {Invertebrate traits for the biomonitoring of large European rivers: an initial assessment of trait patterns in least impacted river reaches},
  journal = {Freshwater Biology},
  volume = {50},
  number = {12},
  pages = {2136--2161},
  year = {2005},
  doi = {10.1111/j.1365-2427.2005.01447.x},
  note = {access: abstract_only (C-PREDICT; verified by the critic); its held-out framing known only through Hawkins et al. 2010 (critic: C-PREDICT:C-053..055); cited as: C-PREDICT [37]}
}
@article{hawkinsReferenceConditionPredicting2010,
  author = {Hawkins, Charles P. and Olson, John R. and Hill, Ryan A.},
  title = {The reference condition: predicting benchmarks for ecological and water-quality assessments},
  journal = {Journal of the North American Benthological Society},
  volume = {29},
  number = {1},
  pages = {312--343},
  year = {2010},
  doi = {10.1899/09-092.1},
  note = {access: full_text (C-PREDICT; read by a search agent, not re-opened by the synthesis, critic: C-PREDICT:C-055, C-058); type: review; cited as: C-PREDICT [38]}
}
@article{feioIntegrationInvertebrateTraits2012,
  author = {Feio, Maria João and Dolédec, Sylvain},
  title = {Integration of invertebrate traits into predictive models for indirect assessment of stream functional integrity: a case study in Portugal},
  journal = {Ecological Indicators},
  volume = {15},
  number = {1},
  pages = {236--247},
  year = {2012},
  doi = {10.1016/j.ecolind.2011.09.039},
  note = {access: abstract_only (C-PREDICT; one agent's Semantic Scholar automated summary not used); conflict: full text listed in Sources not obtained, whose heading says nothing beyond a citation was reachable; cited as: C-PREDICT [39]}
}
@article{pontAssessingRiverBiotic2006,
  author = {Pont, Didier and Hugueny, Bernard and Beier, Ulrika and Goffaux, Daniel and Melcher, Andreas and Noble, Richard and Rogers, Catriona and Roset, Nicolas and Schmutz, Stefan},
  title = {Assessing river biotic condition at a continental scale: a European approach using functional metrics and fish assemblages},
  journal = {Journal of Applied Ecology},
  volume = {43},
  number = {1},
  pages = {70--80},
  year = {2006},
  doi = {10.1111/j.1365-2664.2005.01126.x},
  note = {access: abstract_only (C-PREDICT); cited as: C-PREDICT [40]}
}
@article{dubuisPredictingCurrentFuture2013,
  author = {Dubuis, Anne and Rossier, Leila and Pottier, Julien and Pellissier, Loïc and Vittoz, Pascal and Guisan, Antoine},
  title = {Predicting current and future spatial community patterns of plant functional traits},
  journal = {Ecography},
  volume = {36},
  number = {11},
  pages = {1158--1168},
  year = {2013},
  doi = {10.1111/j.1600-0587.2013.00237.x},
  note = {access: abstract_only (C-PREDICT); cited as: C-PREDICT [41]}
}
@article{deschampsPredictFirstassembleLater2023,
  author = {Deschamps, Gabrielle and Poggiato, Giovanni and Brun, Philipp and Galiez, Clovis and Thuiller, Wilfried},
  title = {Predict first-assemble later versus assemble first-predict later: revisiting the dilemma for functional biogeography},
  journal = {Methods in Ecology and Evolution},
  volume = {14},
  number = {10},
  pages = {2680--2696},
  year = {2023},
  doi = {10.1111/2041-210X.14203},
  note = {access: abstract_only (C-PREDICT); cited as: C-PREDICT [42]}
}
@article{boonmanAssessingReliabilityPredicted2020,
  author = {Boonman, Coline C. F. and Benítez-López, Ana and Schipper, Aafke M. and Thuiller, Wilfried and Anand, Madhur and Cerabolini, Bruno E. L. and Cornelissen, Johannes H. C. and Gonzalez-Melo, Andres and Hattingh, Wesley N. and Higuchi, Pedro and Laughlin, Daniel C. and Onipchenko, Vladimir G. and Peñuelas, Josep and Poorter, Lourens and Soudzilovskaia, Nadejda A. and Huijbregts, Mark A. J. and Santini, Luca},
  title = {Assessing the reliability of predicted plant trait distributions at the global scale},
  journal = {Global Ecology and Biogeography},
  volume = {29},
  number = {6},
  pages = {1034--1051},
  year = {2020},
  doi = {10.1111/geb.13086},
  note = {access: abstract_only (C-PREDICT); cited as: C-PREDICT [43]}
}
@article{norbergComprehensiveEvaluationPredictive2019,
  author = {Norberg, Anna and Abrego, Nerea and Blanchet, F. Guillaume and Adler, Frederick R. and Anderson, Barbara J. and Anttila, Jani and Araújo, Miguel B. and Dallas, Tad and Dunson, David and Elith, Jane and Foster, Scott D. and Fox, Richard and Franklin, Janet and Godsoe, William and Guisan, Antoine and O'Hara, Bob and Hill, Nicole A. and Holt, Robert D. and Hui, Francis K. C. and Husby, Magne and Kålås, John Atle and Lehikoinen, Aleksi and Luoto, Miska and Mod, Heidi K. and Newell, Graeme and Renner, Ian and Roslin, Tomas and Soininen, Janne and Thuiller, Wilfried and Vanhatalo, Jarno and Warton, David and White, Matt and Zimmermann, Niklaus E. and Gravel, Dominique and Ovaskainen, Otso},
  title = {A comprehensive evaluation of predictive performance of 33 species distribution models at species and community levels},
  journal = {Ecological Monographs},
  volume = {89},
  number = {3},
  pages = {e01370},
  year = {2019},
  doi = {10.1002/ecm.1370},
  note = {access: full_text (C-PREDICT; via search agents, not re-opened by the synthesis, critic: C-PREDICT:C-058); cited as: C-PREDICT [44]}
}
@article{wengerAssessingTransferabilityEcological2012,
  author = {Wenger, Seth J. and Olden, Julian D.},
  title = {Assessing transferability of ecological models: an underappreciated aspect of statistical validation},
  journal = {Methods in Ecology and Evolution},
  volume = {3},
  number = {2},
  pages = {260--267},
  year = {2012},
  doi = {10.1111/j.2041-210X.2011.00170.x},
  note = {access: abstract_only (C-PREDICT); cited as: C-PREDICT [45]}
}
@article{maguireControlledComparisonSpecies2016,
  author = {Maguire, Kaitlin C. and Nieto-Lugilde, Diego and Blois, Jessica L. and Fitzpatrick, Matthew C. and Williams, John W. and Ferrier, Simon and Lorenz, David J.},
  title = {Controlled comparison of species- and community-level models across novel climates and communities},
  journal = {Proceedings of the Royal Society B},
  volume = {283},
  number = {1826},
  pages = {20152817},
  year = {2016},
  doi = {10.1098/rspb.2015.2817},
  note = {access: abstract_only (C-PREDICT; verified by the critic); cited as: C-PREDICT [46]}
}
@article{pasolliMachineLearningMetaanalysis2016,
  author = {Pasolli, Edoardo and Truong, Duy Tin and Malik, Faizan and Waldron, Levi and Segata, Nicola},
  title = {Machine learning meta-analysis of large metagenomic datasets: tools and biological insights},
  journal = {PLOS Computational Biology},
  volume = {12},
  number = {7},
  pages = {e1004977},
  year = {2016},
  doi = {10.1371/journal.pcbi.1004977},
  note = {access: abstract_only (C-PREDICT); cited as: C-PREDICT [47]}
}
@article{hermansUsingSoilBacterial2020,
  author = {Hermans, Syrie M. and Buckley, Hannah L. and Case, Bradley S. and Curran-Cournane, Fiona and Taylor, Matthew and Lear, Gavin},
  title = {Using soil bacterial communities to predict physico-chemical variables and soil quality},
  journal = {Microbiome},
  volume = {8},
  number = {1},
  pages = {79},
  year = {2020},
  doi = {10.1186/s40168-020-00858-1},
  note = {access: abstract_only (C-PREDICT); cited as: C-PREDICT [48]}
}
@article{smithNaturalBacterialCommunities2015,
  author = {Smith, Mark B. and Rocha, Andrea M. and Smillie, Chris S. and others},
  title = {Natural bacterial communities serve as quantitative geochemical biosensors},
  journal = {mBio},
  volume = {6},
  number = {3},
  pages = {e00326-15},
  year = {2015},
  doi = {10.1128/mBio.00326-15},
  note = {access: abstract_only (C-PREDICT); incomplete: author (32 in Crossref, 3 transcribed; critic: C-PREDICT:C-071); cited as: C-PREDICT [49]}
}
@article{breitkreuzCanWeEstimate2021,
  author = {Breitkreuz, Claudia and Heintz-Buschart, Anna and Buscot, François and Wahdan, Sara Fareed Mohamed and Tarkka, Mika and Reitz, Thomas},
  title = {Can we estimate functionality of soil microbial communities from structure-derived predictions? A reality test in agricultural soils},
  journal = {Microbiology Spectrum},
  volume = {9},
  number = {1},
  pages = {e00278-21},
  year = {2021},
  doi = {10.1128/Spectrum.00278-21},
  note = {access: abstract_only (C-PREDICT); cited as: C-PREDICT [50]}
}
@article{gayraudInvertebrateTraitsBiomonitoring2003,
  author = {Gayraud, Sébastien and Statzner, Bernhard and Bady, Pierre and Haybach, Arne and Schöll, Franz and Usseglio-Polatera, Philippe and Bacchi, Michel},
  title = {Invertebrate traits for the biomonitoring of large European rivers: an initial assessment of alternative metrics},
  journal = {Freshwater Biology},
  volume = {48},
  number = {11},
  pages = {2045--2064},
  year = {2003},
  doi = {10.1046/j.1365-2427.2003.01139.x},
  note = {access: abstract_only (C-PREDICT); cited in the answers only; cited as: C-PREDICT [51]}
}
@article{chenLowerFunctionalRedundancy2022,
  author = {Chen, Huaihai and Ma, Kayan and Huang, Yu and Fu, Qi and Qiu, Yingbo and Lin, Jiajiang and Schadt, Christopher W. and Chen, Hao},
  title = {Lower functional redundancy in 'narrow' than 'broad' functions in global soil metagenomics},
  journal = {SOIL},
  volume = {8},
  pages = {297--308},
  year = {2022},
  doi = {10.5194/soil-8-297-2022},
  note = {access: abstract_only (C-PREDICT); cited in the answers only; cited as: C-PREDICT [52]}
}
@article{vanderlaanEnhancingPerformanceInterpretation2014,
  author = {Vander Laan, J. J. and Hawkins, C. P.},
  title = {Enhancing the performance and interpretation of freshwater biological indices: an application in arid zone streams},
  journal = {Ecological Indicators},
  volume = {36},
  pages = {470--482},
  year = {2014},
  doi = {10.1016/j.ecolind.2013.09.006},
  note = {access: not_obtained (C-PREDICT); not cited; listed in Sources not obtained}
}
@article{wilhelmPredictingMeasuresSoil2021,
  author = {Wilhelm, R. C. and van Es, H. M. and Buckley, D. H.},
  title = {Predicting measures of soil health using the microbiome and supervised machine learning},
  journal = {Soil Biology and Biochemistry},
  volume = {164},
  pages = {108472},
  year = {2022},
  doi = {10.1016/j.soilbio.2021.108472},
  note = {access: not_obtained (C-PREDICT); not cited; listed in Sources not obtained}
}
@article{clarkeRIVPACSModelsPredicting2003,
  author = {Clarke, R. T. and Wright, J. F. and Furse, M. T.},
  title = {RIVPACS models for predicting the expected macroinvertebrate fauna and assessing the ecological quality of rivers},
  journal = {Ecological Modelling},
  volume = {160},
  pages = {219--233},
  year = {2003},
  doi = {10.1016/S0304-3800(02)00255-7},
  note = {access: not_obtained (C-PREDICT); not cited; listed in Sources not obtained}
}
@article{statznerPerspectivesBiomonitoringLarge2001,
  author = {Statzner, Bernhard and Bis, Barbara and Dolédec, Sylvain and Usseglio-Polatera, Philippe},
  title = {Perspectives for biomonitoring at large spatial scales: a unified measure for the functional composition of invertebrate communities in European running waters},
  journal = {Basic and Applied Ecology},
  volume = {2},
  number = {1},
  pages = {73--85},
  year = {2001},
  doi = {10.1078/1439-1791-00039},
  note = {access: not_obtained (C-PREDICT; Semantic Scholar summary only); not cited; listed in Sources not obtained}
}
@article{vansickleExclusionRareTaxa2007,
  author = {Van Sickle, John and Larsen, David P. and Hawkins, Charles P.},
  title = {Exclusion of rare taxa affects performance of the O/E index in bioassessments},
  journal = {Journal of the North American Benthological Society},
  volume = {26},
  number = {2},
  pages = {319--331},
  year = {2007},
  doi = {10.1899/0887-3593(2007)26[319:EORTAP]2.0.CO;2},
  note = {access: not_obtained (C-PREDICT; Semantic Scholar automated summary only); not cited; listed in Sources not obtained}
}
@article{chessmanBioassessmentReferenceSites2004,
  author = {Chessman, Bruce C. and Royal, Meredith J.},
  title = {Bioassessment without reference sites: use of environmental filters to predict natural assemblages of river macroinvertebrates},
  journal = {Journal of the North American Benthological Society},
  volume = {23},
  number = {3},
  pages = {599--615},
  year = {2004},
  doi = {10.1899/0887-3593(2004)023<0599:BWRSUO>2.0.CO;2},
  note = {access: not_obtained (C-PREDICT); not cited; listed in Sources not obtained}
}
@incollection{hawkinsEffectsTaxonomicResolution2000,
  author = {Hawkins, C. P. and Norris, R. H.},
  title = {Effects of taxonomic resolution and use of subsets of the fauna on the performance of RIVPACS-type models},
  booktitle = {Assessing the Biological Quality of Fresh Waters: RIVPACS and Other Techniques},
  editor = {Wright, J. F. and Sutcliffe, D. W. and Furse, M. T.},
  publisher = {Freshwater Biological Association},
  address = {Ambleside},
  pages = {217--228},
  year = {2000},
  note = {access: not_obtained (C-PREDICT); no DOI found; citation details from a search agent's recall, unverified; incomplete: doi; not cited; listed in Sources not obtained}
}
@article{dimaggioModelingPhytoplanktonCommunity2016,
  author = {Di Maggio, Jimena and Fernández, Carolina and Parodi, Elisa R. and Diaz, M. Soledad and Estrada, Vanina},
  title = {Modeling phytoplankton community in reservoirs. A comparison between taxonomic and functional groups-based models},
  journal = {Journal of Environmental Management},
  volume = {165},
  pages = {31--52},
  year = {2016},
  doi = {10.1016/j.jenvman.2015.08.027},
  note = {access: not_obtained (C-PREDICT); not cited; listed in Sources not obtained}
}
@article{doledecAccurateDescriptionAbundance2000,
  author = {Dolédec, S. and Olivier, J. M. and Statzner, B.},
  title = {Accurate description of the abundance of taxa and their biological traits in stream invertebrate communities: effects of taxonomic and spatial resolution},
  journal = {Archiv für Hydrobiologie},
  volume = {148},
  number = {1},
  pages = {25--43},
  year = {2000},
  doi = {10.1127/archiv-hydrobiol/148/2000/25},
  note = {access: not_obtained (C-PREDICT; Semantic Scholar summary only); not cited; listed in Sources not obtained}
}
@article{heinoTaxonomicSurrogacyNumerical2014,
  author = {Heino, Jani},
  title = {Taxonomic surrogacy, numerical resolution and responses of stream macroinvertebrate communities to ecological gradients: Are the inferences transferable among regions?},
  journal = {Ecological Indicators},
  volume = {36},
  pages = {186--194},
  year = {2014},
  doi = {10.1016/j.ecolind.2013.07.022},
  note = {access: not_obtained (C-PREDICT; Semantic Scholar automated summary only); not cited; listed in Sources not obtained}
}
@article{mondyNewMacroinvertebratebasedMultimetric2012,
  author = {Mondy, Cédric Pascal and Villeneuve, Bertrand and Archaimbault, Virginie and Usseglio-Polatera, Philippe},
  title = {A new macroinvertebrate-based multimetric index (I2M2) to evaluate ecological quality of French wadeable streams fulfilling the WFD demands: A taxonomical and trait approach},
  journal = {Ecological Indicators},
  volume = {18},
  pages = {452--467},
  year = {2012},
  doi = {10.1016/j.ecolind.2011.12.013},
  note = {access: not_obtained (C-PREDICT); not cited; listed in Sources not obtained}
}
@article{aouabedSoilMicrobiomePrediction2026,
  author = {Aouabed and Therrien and Bouaoune and Bakhtyari and Hijri and Makarenkov},
  title = {Soil microbiome prediction using traditional machine learning and deep learning models},
  journal = {Scientific Reports},
  year = {2026},
  doi = {10.1038/s41598-026-39537-w},
  note = {access: abstract_only (C-PREDICT; read by the critic only, critic: C-PREDICT:C-009, C-083); missed by the review; incomplete: author given names, volume, pages}
}
@article{anon2026,
  journal = {New Phytologist},
  year = {2026},
  doi = {10.1111/nph.70720},
  note = {access: abstract_only (C-PREDICT; read by the critic only, critic: C-PREDICT:C-021, C-088); a 2026 study predicting soil microbes at NEON from airborne canopy reflectance; missed by the review; incomplete: author, title, volume, pages}
}
@article{zurell2020,
  author = {Zurell and others},
  year = {2020},
  note = {access: not stated (C-PREDICT; cited in the D3 answer only, on stacking choices in species distribution models); not in the reference list; incomplete: author, title, journal, volume, pages, doi}
}
@article{vesk2021,
  author = {Vesk and others},
  journal = {Ecography},
  year = {2021},
  note = {access: not stated (C-PREDICT; named by the critic as a coverage-gap example on the transferability of trait-based SDMs); not cited; incomplete: author, title, volume, pages, doi}
}
@article{pollock2012,
  author = {Pollock and others},
  year = {2012},
  note = {access: not stated (C-PREDICT; named by the critic as a coverage-gap example on trait-based species distribution models); not cited; incomplete: author, title, journal, volume, pages, doi}
}
@article{ferrier2006,
  author = {Ferrier and Guisan},
  year = {2006},
  note = {access: not stated (C-PREDICT; named by the critic as a coverage-gap example on community-level modelling); not cited; incomplete: author, title, journal, volume, pages, doi}
}
@article{baselga2010,
  author = {Baselga and Araújo},
  year = {2010},
  note = {access: not stated (C-PREDICT; named by the critic as a coverage-gap example on community composition predictions); not cited; incomplete: author, title, journal, volume, pages, doi}
}
@article{yates2018,
  author = {Yates and others},
  journal = {Trends in Ecology \& Evolution},
  year = {2018},
  note = {access: not stated (C-PREDICT; named by the critic as a coverage-gap example, a review on model transferability); not cited; incomplete: author, title, volume, pages, doi}
}
@article{salazar2019,
  author = {Salazar and others},
  year = {2019},
  note = {access: not stated (C-PREDICT; named by the critic as a coverage-gap example, the Tara metatranscriptome); not cited; incomplete: author, title, journal, volume, pages, doi}
}
@article{doledec2008,
  author = {Dolédec, S. and Statzner, B.},
  year = {2008},
  note = {access: not stated (C-PREDICT; named by the critic and the stage-2 check as trait-profile O/E literature absent from the review); not cited; incomplete: title, journal, volume, pages, doi}
}
@article{gneitingStrictlyProperScoring2007,
  author = {Gneiting, Tilmann and Raftery, Adrian E.},
  title = {Strictly Proper Scoring Rules, Prediction, and Estimation},
  journal = {Journal of the American Statistical Association},
  volume = {102},
  number = {477},
  pages = {359--378},
  year = {2007},
  doi = {10.1198/016214506000001437},
  note = {background (skill-measures); access: full_text (checked in an author-hosted PDF)}
}
```
