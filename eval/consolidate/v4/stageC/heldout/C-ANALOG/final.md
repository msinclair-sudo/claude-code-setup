---
type: knowledge
title: Present-day analogues for changed climate and changed soil conditions
inputs:
  - C-ANALOG: PhD/Proposal/Research/Results/Do changed conditions at a location fall within the range present elsewhere Evidence on present-day analogues for changed climate and changed soil conditions.md
refs: PhD/Proposal/Refs/Refs.bib
built: 2026-10-24
status: draft
tags:
  - research
  - knowledge
---
# Present-day analogues for changed climate and changed soil conditions

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
| C-ANALOG | [[Do changed conditions at a location fall within the range present elsewhere Evidence on present-day analogues for changed climate and changed soil conditions]] | yes | labelled (access; class; standing) | no | no | exact (every labelled sentence, every answer sentence, and the critique) |

## Concepts

### emission-scenarios: the forcing scenarios the projections use
needs: none
- **emission-scenarios.bg1** The Representative Concentration Pathways (RCPs) are a set of four pathways that together span year-2100 radiative forcing values from 2.6 to 8.5 W/m2, with extensions that allow climate modelling experiments through the year 2300.
  kind: background · ref: vanvuurenRepresentativeConcentrationPathways2011 · check: DOI 10.1007/s10584-011-0148-z resolves on Crossref (Climatic Change 109(1-2): 5-31); the four pathways, the 2.6 to 8.5 W/m2 span and the extensions to 2300 are in the abstract (Semantic Scholar and OpenAlex)

### analogue-design: how a climate analogue study is built
needs: none
- **analogue-design.1** Every climate analogue study makes the same five choices: a set of variables; a way of scaling them, usually by interannual variability; a dissimilarity measure (standardised Euclidean distance, SED, or a Mahalanobis form such as "sigma dissimilarity"); a threshold separating "analogue" from "novel"; and a pool of candidate analogues, which is the reference domain.
  conf: not stated · class: not stated · holds: the climate analogue studies the review covers · src: none (the reviewer's synthesis) · trail: C-ANALOG §1.1 · from: C-ANALOG:B-0034..0039
- **analogue-design.2** The unit counted also varies (land area, grid cells, cities, counties or harvested crop area); because these choices differ from study to study, the reported shares are not one quantity measured with error, do not share a definition and cannot be pooled.
  conf: not stated · class: not stated · holds: the climate analogue studies the review covers; the figures differ in unit, metric, threshold, variable set, model generation and grid · src: none (the reviewer's synthesis) · trail: C-ANALOG §1.1, §critic, §answers, §4. Answers · rating: "Weak for any single 'share' figure" · from: C-ANALOG:B-0040, C-ANALOG:B-0041, C-ANALOG:C-002, C-ANALOG:A-003, C-ANALOG:A-026, C-ANALOG:A-098
- **analogue-design.3** Many modelling studies estimate the share of projected future climate with no present-day analogue; there is no single share, and the reported shares run from under 1% to over 97%.
  conf: not stated · class: not stated · holds: modelling studies; the top of the range is Ordonez 2024's unverified figure · src: none (the reviewer's synthesis) · trail: C-ANALOG §critic, §answers, §4. Answers · from: C-ANALOG:C-001, C-ANALOG:A-001, C-ANALOG:A-002, C-ANALOG:A-095, C-ANALOG:C-009, C-ANALOG:A-096
- **analogue-design.4** Estimates run from 0.3-2.2% of land novel in phytoclimate space (Conradi 2024) through 4-39% (Williams 2007) to 67-76% by 2100 and over 97% by 2300 (Ordonez 2024), with crop-restricted, county, city and hemisphere-pool figures in between.
  conf: not stated · class: not stated · holds: the range spans studies of different design; the Ordonez figures are unverified · src: conradiReassessmentRisksClimate2024, williamsProjectedDistributionsNovel2007, ordonezTowardsNovelBiosphere2024, fitzpatrickContemporaryClimaticAnalogs2019, bastinUnderstandingClimateChange2019, pughClimateAnaloguesSuggest2016, chaudharyClimateAnalogsCan2023 · trail: C-ANALOG §4. Answers, §critic · from: C-ANALOG:A-096, C-ANALOG:A-097, C-ANALOG:C-009
- **analogue-design.5** All of the climate analogue evidence is modelled; nothing is measured.
  conf: not stated · class: not stated · holds: the climate analogue studies the review covers · src: none (the reviewer's synthesis) · trail: C-ANALOG §critic, §answers, §4. Answers · from: C-ANALOG:C-019, C-ANALOG:A-028, C-ANALOG:A-111

### global-climate-shares: global land estimates of novel climate
needs: analogue-design, emission-scenarios
- **global-climate-shares.1** Williams, Jackson and Kutzbach compared 2080-2099 with 1980-1999 climate on a T42 grid, with four seasonal variables (JJA and DJF temperature and precipitation), SED scaled by interannual variability, a threshold of SEDt = 3.22 chosen as the value that best discriminates same-biome from different-biome climate pairs, and all 20th-century land as the candidate pool.
  conf: not stated · class: model (marker) · holds: global land, T42 grid · src: williamsProjectedDistributionsNovel2007 (FT-r, modelled) · trail: C-ANALOG §1.2 · from: C-ANALOG:I-0001, C-ANALOG:B-0042, C-ANALOG:B-0043, C-ANALOG:B-0044
- **global-climate-shares.2** Williams et al. give novel climates on 12-39% of land under A2 and 4-20% under B1, and disappearing climates on 10-48% (A2) and 4-20% (B1).
  conf: not stated · class: not stated · holds: 2080-2099 against 1980-1999; checked in full text by the reviewer and the critic · src: williamsProjectedDistributionsNovel2007 (FT-r) · trail: C-ANALOG §1.2, §critic, §Provenance · from: C-ANALOG:B-0045, C-ANALOG:B-0046, C-ANALOG:C-003, C-ANALOG:B-0017, C-ANALOG:I-0001
- **global-climate-shares.3** The authors call the biome-calibrated threshold "a conservative estimator", and report that the extent of novel and disappearing climates "scales linearly with the magnitude of mean global warming".
  conf: not stated · class: not stated · holds: Williams 2007 · src: williamsProjectedDistributionsNovel2007 (full text, re-read) · trail: C-ANALOG §1.2, §answers · from: C-ANALOG:B-0047, C-ANALOG:B-0048, C-ANALOG:A-006
- **global-climate-shares.4** The text of Williams 2007 re-read for the review does not say what sets the low and high ends of each range, so that remains unverified.
  conf: not stated · class: not stated · holds: the main text; the Supporting Information was not read · src: williamsProjectedDistributionsNovel2007 · trail: C-ANALOG §1.2, §Provenance · search: not stated · from: C-ANALOG:B-0050, C-ANALOG:B-0051, C-ANALOG:B-0018, C-ANALOG:B-0049
- **global-climate-shares.5** Ordonez, Riede, Normand and Svenning used Mahalanobis distance on seasonal temperature and precipitation, 50 km cells, 11 CMIP5 models and a 1970-2000 baseline, with the threshold set by ROC discrimination between biomes.
  conf: not stated · class: model (marker) · holds: global land, 50 km cells · src: ordonezTowardsNovelBiosphere2024 (FT-s, modelled) · trail: C-ANALOG §1.2, §References · from: C-ANALOG:I-0002, C-ANALOG:B-0052, C-ANALOG:B-0053, C-ANALOG:R-0078
- **global-climate-shares.6** The Ordonez 2024 abstract reports novel-ecosystem coverage from three combined metrics (new climate combinations, climate velocity and disaggregation): over 50% of land by 2100 and over 80% by 2300.
  conf: not stated · class: not stated · holds: novel ecosystems combined across three metrics, not a single-metric no-analogue share · src: ordonezTowardsNovelBiosphere2024 (abstract, checked by the critic) · trail: C-ANALOG §critic, §Adversarial · from: C-ANALOG:C-008, C-ANALOG:C-035, C-ANALOG:C-044, C-ANALOG:C-102
- **global-climate-shares.7** The review's figures for Ordonez 2024, 67% (RCP6.0) and 76% (RCP8.5) of land novel by 2100 and over 97% by 2300, rest on a search agent's full-text reading that was not re-opened, and they are unverified, as is whether they refer to the climate-combination metric alone.
  conf: single (note: "SINGLE SOURCE for the high figure") · class: not stated · holds: one study; the full text was blocked to the reviewer and the critic · src: ordonezTowardsNovelBiosphere2024 (FT-s, not re-opened) · trail: C-ANALOG §1.2, §critic, §Adversarial, §answers · limit: access (critic: C-045) · from: C-ANALOG:B-0053, C-ANALOG:B-0057, C-ANALOG:C-009, C-ANALOG:C-036, C-ANALOG:C-043, C-ANALOG:C-045, C-ANALOG:A-010, C-ANALOG:C-030
- **global-climate-shares.8** Ordonez et al. do not reconcile their figure with Williams; grid resolution, metric, variable scaling, CMIP generation and baseline all differ, so the review cannot assign the gap to any one factor.
  conf: not stated · class: not stated · holds: Williams 2007 against Ordonez 2024 · src: ordonezTowardsNovelBiosphere2024, williamsProjectedDistributionsNovel2007 · trail: C-ANALOG §1.2, §answers, §Adversarial · from: C-ANALOG:B-0055, C-ANALOG:B-0056, C-ANALOG:A-031, C-ANALOG:C-094
- **global-climate-shares.9** The land shares of Williams 2007 (12-39% of land novel by 2100 under A2), Ordonez 2024 (67-76% under RCP6.0/8.5) and Conradi 2024 (0.3-2.2% in phytoclimate space) are unreconciled in the sources, but the Williams-Ordonez conflict is not established as like for like, because the Ordonez figure appears, from its abstract, to combine three metrics, and the review's 67-76% and >97% figures for Ordonez are unverified.
  conf: not stated · class: not stated · holds: three studies of different design · src: williamsProjectedDistributionsNovel2007, ordonezTowardsNovelBiosphere2024, conradiReassessmentRisksClimate2024 · trail: C-ANALOG §answers, §4. Answers, §critic · from: C-ANALOG:A-030, C-ANALOG:A-110, C-ANALOG:C-010, C-ANALOG:C-102, C-ANALOG:C-009
- **global-climate-shares.10** Conradi et al. transformed climate into a "phytoclimate" space, the modelled suitability of 14 plant growth forms derived from ecophysiological models of 135,153 species, with the threshold at the 5th percentile of intercentroid distances between phytoclimatic zones.
  conf: not stated · class: model (marker) · holds: land, in phytoclimate space · src: conradiReassessmentRisksClimate2024 (FT-r, modelled) · trail: C-ANALOG §1.2 · from: C-ANALOG:I-0003, C-ANALOG:B-0058, C-ANALOG:B-0059
- **global-climate-shares.11** Conradi 2024 gives 33% to 68% of land with significant phytoclimate change by 2070, against only 0.3% (RCP2.6) to 2.2% (RCP8.5) of land with novel phytoclimates, and 0.1-1.3% of present phytoclimates disappearing.
  conf: not stated · class: not stated · holds: by 2070; the 33% is the source's figure, which the review misprints as 3% · src: conradiReassessmentRisksClimate2024 (FT-r) · trail: C-ANALOG §1.2, §critic, §answers · from: C-ANALOG:B-0059, C-ANALOG:B-0060, C-ANALOG:B-0061, C-ANALOG:C-004, C-ANALOG:C-032, C-ANALOG:C-054, C-ANALOG:C-070, C-ANALOG:A-018, C-ANALOG:A-104
- **global-climate-shares.12** The Conradi authors conclude that tropical climates that are novel in raw variables "are not functionally novel"; their example is the Sahara, novel in climate but still unsuitable for every growth form.
  conf: not stated · class: not stated · holds: phytoclimate space · src: conradiReassessmentRisksClimate2024 · trail: C-ANALOG §1.2, §answers · from: C-ANALOG:B-0062, C-ANALOG:B-0063, C-ANALOG:A-032
- **global-climate-shares.13** The space in which analogues are sought can move the answer by one to two orders of magnitude; the only evidence is Conradi 2024, and removing it removes the evidence that biologically transformed spaces give less novelty.
  conf: single (note: "SINGLE SOURCE") · class: not stated · holds: raw climate against phytoclimate space · src: conradiReassessmentRisksClimate2024 · trail: C-ANALOG §1.2, §critic, §Adversarial, §answers · from: C-ANALOG:B-0064, C-ANALOG:B-0065, C-ANALOG:C-014, C-ANALOG:C-062, C-ANALOG:A-046

### reference-domain: the candidate pool and search extent
needs: analogue-design, emission-scenarios
- **reference-domain.1** Limiting Williams' search to 500 km roughly doubles novel land, to 39-84% (A2) and 14-52% (B1), and disappearing land to 37-85% and 14-50%.
  conf: not stated · class: not stated · holds: global land, a within-study contrast · src: williamsProjectedDistributionsNovel2007 (FT-r) · trail: C-ANALOG §1.3, §critic, §answers · from: C-ANALOG:B-0068, C-ANALOG:C-003, C-ANALOG:A-011, C-ANALOG:A-101, C-ANALOG:C-012
- **reference-domain.2** Pugh et al. searched only within each crop's current harvested area (SED on growing degree days and precipitation, threshold 0.7, 2081-2099, RCP8.5) and found no analogue for 17.2% of maize, 17.6% of wheat and 60.5% of rice harvested area, counted only where at least 4 of 5 GCMs agree, against 8.0, 5.4 and 28.9% in 2041-2059.
  conf: not stated · class: model (marker) · holds: current global croplands; no unrestricted comparison · src: pughClimateAnaloguesSuggest2016 (FT-s, modelled) · trail: C-ANALOG §1.3, §critic, §answers · from: C-ANALOG:I-0004, C-ANALOG:B-0069, C-ANALOG:C-007, C-ANALOG:A-012, C-ANALOG:A-039, C-ANALOG:C-013
- **reference-domain.3** Chaudhary et al. searched among 3,001 US counties (five agroclimatic variables, sigma dissimilarity, 2040-2070); 80% (RCP8.5) and 84% (RCP4.5) of 680 specialty-crop counties had an acceptable analogue (<=2 sigma), so 16-20% had none.
  conf: not stated · class: model (marker) · holds: a US-only county pool; no unrestricted comparison · src: chaudharyClimateAnalogsCan2023 (FT-s, modelled) · trail: C-ANALOG §1.3, §answers, §critic · from: C-ANALOG:I-0005, C-ANALOG:A-013, C-ANALOG:C-013
- **reference-domain.4** Bastin et al. used as reference the convex hull of 520 current city climates (four principal components of 19 bioclimatic variables, 2050, RCP4.5); 22% of cities fell outside it, and 30% in the tropics.
  conf: not stated · class: model (marker) · holds: 520 city climates; no unrestricted comparison · src: bastinUnderstandingClimateChange2019 (FT-s, modelled) · trail: C-ANALOG §1.3, §answers, §critic · from: C-ANALOG:I-0006, C-ANALOG:A-014, C-ANALOG:C-013
- **reference-domain.5** The Bastin 2019 abstract says the climates are "not currently experienced by any existing major cities"; the 'on the planet today' phrase the review quotes is not in the abstract, so the reviewer's critique that the authors overstate their reference set rests on a misquote or on unverified body text.
  conf: not stated · class: not stated · holds: the Bastin 2019 abstract, checked by the critic · src: bastinUnderstandingClimateChange2019 (abstract) · trail: C-ANALOG §1.3, §critic, §Adversarial · contrary: one-sided (critic: C-096) · from: C-ANALOG:B-0070, C-ANALOG:B-0071, C-ANALOG:C-033, C-ANALOG:C-034, C-ANALOG:C-053, C-ANALOG:C-096, C-ANALOG:C-109
- **reference-domain.6** Burke et al. let analogues come from any location in six periods (Eocene, Pliocene, Last Interglacial, mid-Holocene, pre-industrial, historical), with a threshold at the 99th percentile of modern-to-preindustrial best-analogue distances.
  conf: not stated · class: model (marker) · holds: a pool reaching back into geological time · src: burkePlioceneEoceneProvide2018 (FT-s, modelled) · trail: C-ANALOG §1.3 · from: C-ANALOG:I-0007
- **reference-domain.7** Widening the pool into geological time lowers novelty: the Burke 2018 abstract gives under 1% of locations without an analogue under RCP4.5 and 8.7% under RCP8.5.
  conf: not stated · class: not stated · holds: a deep-time pool, a within-study contrast · src: burkePlioceneEoceneProvide2018 (abstract) · trail: C-ANALOG §critic, §Adversarial, §4. Answers · from: C-ANALOG:C-006, C-ANALOG:C-037, C-ANALOG:C-052, C-ANALOG:A-103, C-ANALOG:C-012, C-ANALOG:B-0072
- **reference-domain.8** The review's Burke 2018 figures under RCP8.5 are 2.1% of locations without an analogue by 2100 and 8.7% by 2280; they come from the search agent's full-text reading, which was not re-opened.
  conf: not stated · class: not stated · holds: a deep-time pool · src: burkePlioceneEoceneProvide2018 (FT-s, not re-opened) · trail: C-ANALOG §1.3, §answers, §Adversarial · limit: access (critic: C-052) · from: C-ANALOG:B-0073, C-ANALOG:A-010, C-ANALOG:C-052, C-ANALOG:B-0072
- **reference-domain.9** Fitzpatrick and Dunn used 12 seasonal variables, a 1960-1990 reference and a pool spanning the Western Hemisphere north of the equator: under RCP8.5, 42.7% of 540 North American urban areas were more than 4 sigma from their best contemporary analogue and only 17% were within 2 sigma; under RCP4.5, 69.6% of cities west of the Rockies had analogues within 2 sigma.
  conf: not stated · class: model (marker) · holds: 540 North American urban areas, a hemisphere-wide pool · src: fitzpatrickContemporaryClimaticAnalogs2019 (FT-r, modelled) · trail: C-ANALOG §1.3, §answers, §Provenance · from: C-ANALOG:I-0008, C-ANALOG:B-0074, C-ANALOG:B-0075, C-ANALOG:A-008, C-ANALOG:B-0018
- **reference-domain.10** Only two within-study contrasts isolate the candidate pool, Williams' 500 km restriction and Burke's deep-time pool; the crop, county and city figures (Pugh, Chaudhary, Bastin) have no unrestricted comparison and differ in variables, metric, unit and horizon, so they do not show that narrowing the pool raises novelty.
  conf: not stated · class: not stated · holds: within-study against between-study contrasts · src: williamsProjectedDistributionsNovel2007, burkePlioceneEoceneProvide2018, pughClimateAnaloguesSuggest2016, chaudharyClimateAnalogsCan2023, bastinUnderstandingClimateChange2019 · trail: C-ANALOG §critic, §Adversarial · contrary: one-sided (critic: C-093) · from: C-ANALOG:C-012, C-ANALOG:C-013, C-ANALOG:C-038, C-ANALOG:C-039, C-ANALOG:C-093, C-ANALOG:C-095, C-ANALOG:C-103
- **reference-domain.11** The qualitative dependence on reference domain and scenario survives the removal of any one source.
  conf: not stated · class: reading (note: "Single-source sensitivity") · holds: the D1 evidence base · src: none (the reviewer's sensitivity reading) · trail: C-ANALOG §answers · from: C-ANALOG:A-045

### scenario-horizon: forcing scenario and time horizon
needs: analogue-design, emission-scenarios
- **scenario-horizon.1** Every within-study contrast finds more novelty under higher forcing and at later horizons: A2 against B1 (Williams 2007), RCP4.5 against 8.5 across North America (Mahony 2017), cities (Fitzpatrick and Dunn 2019) and crops (Pugh 2016, qualitatively), and 2100 against 2300 (Ordonez 2024) and 2100 against 2280 (Burke 2018).
  conf: repl (note: "several independent modelling studies agree on the direction") · class: not stated · holds: modelling studies, each with a within-study contrast · src: williamsProjectedDistributionsNovel2007, mahonyCloserLookNovel2017 (AB), fitzpatrickContemporaryClimaticAnalogs2019, pughClimateAnaloguesSuggest2016, ordonezTowardsNovelBiosphere2024, burkePlioceneEoceneProvide2018 · trail: C-ANALOG §1.4, §critic, §answers, §4. Answers · rating: "Moderate to strong for the qualitative dependence on scenario, horizon and reference domain" (critic: C-039: the reference-domain part rests on two within-study contrasts) · from: C-ANALOG:B-0076..0080, C-ANALOG:C-011, C-ANALOG:C-041, C-ANALOG:A-004, C-ANALOG:A-005, C-ANALOG:A-025, C-ANALOG:A-099, C-ANALOG:A-100
- **scenario-horizon.2** Mahony et al. 2017 give 7% of North America with novel climate under RCP4.5 and 40% under RCP8.5.
  conf: not stated · class: not stated · holds: North America · src: mahonyCloserLookNovel2017 (abstract, re-read) · trail: C-ANALOG §1.4, §critic, §answers · from: C-ANALOG:B-0078, C-ANALOG:C-005, C-ANALOG:A-007
- **scenario-horizon.3** Lotterhos, Laruson and Jiang analysed the surface ocean on temperature, pH and aragonite saturation, with hemisphere-wide pools: from 1800 to 2000 there was moderate novelty on 3.7% of the ocean and no extreme novelty, and from 2000 to 2100 extreme novelty covered 10.3% (RCP4.5) and 81.9% (RCP8.5).
  conf: not stated · class: model (marker) · holds: the surface ocean, a marine chemical case, not terrestrial climate · src: lotterhosNovelDisappearingClimates2021 (FT-s, modelled) · trail: C-ANALOG §1.4, §answers, §Adversarial · from: C-ANALOG:I-0009, C-ANALOG:B-0081, C-ANALOG:B-0082, C-ANALOG:A-009, C-ANALOG:C-101
- **scenario-horizon.4** The ocean result is seawater carbonate chemistry, not soil, and bears on the soil question only as indirect evidence that a pervasive chemical forcing can push most locations beyond an earlier multi-site range.
  conf: not stated · class: not stated · holds: the surface ocean · src: lotterhosNovelDisappearingClimates2021 · trail: C-ANALOG §1.4 · from: C-ANALOG:B-0083, C-ANALOG:B-0084

### metric-threshold-resolution: dissimilarity measure, threshold and resolution
needs: analogue-design
- **metric-threshold-resolution.1** Burke et al. ran both Mahalanobis distance and SED and report results that are "generally similar", with SED giving a "greater prevalence of geologically novel climates".
  conf: single (note: "SINGLE SOURCE for a direct metric contrast") · class: not stated · holds: one direct comparison, with a deep-time pool · src: burkePlioceneEoceneProvide2018 · trail: C-ANALOG §1.5, §1.3, §answers, §4. Answers, §critic · from: C-ANALOG:I-0007, C-ANALOG:B-0085, C-ANALOG:B-0086, C-ANALOG:B-0087, C-ANALOG:A-016, C-ANALOG:A-035, C-ANALOG:A-047, C-ANALOG:A-105, C-ANALOG:C-014
- **metric-threshold-resolution.2** No study read reports the headline global share across a range of thresholds: Williams tested a higher threshold (5.33 against 3.22) only in its Supporting Information, which no one read, and Pugh et al. state robustness to threshold for projected yields, not for the no-analogue share.
  conf: not stated · class: not stated · holds: Williams 2007 and Pugh 2016 · src: williamsProjectedDistributionsNovel2007, pughClimateAnaloguesSuggest2016 · trail: C-ANALOG §1.5, §1.2, §answers, §4. Answers, §critic · limit: access (note: "which neither the search agent nor the reviewer read") · search: not stated · from: C-ANALOG:B-0088, C-ANALOG:B-0089, C-ANALOG:B-0090, C-ANALOG:B-0049, C-ANALOG:A-017, C-ANALOG:A-037, C-ANALOG:A-107, C-ANALOG:C-015
- **metric-threshold-resolution.3** Mahony et al. refined SED into sigma dissimilarity at high resolution for North America and found that novel climates emerge at low elevations in 80% (RCP4.5) and 99% (RCP8.5) of ecoregions, concluding that "novel climates can emerge in any landscape".
  conf: single (critic: C-014) · class: model (marker) · holds: North America at high resolution; local occurrence, not total share · src: mahonyCloserLookNovel2017 (AB, modelled) · trail: C-ANALOG §1.5, §answers, §critic · from: C-ANALOG:I-0010, C-ANALOG:B-0091, C-ANALOG:A-023, C-ANALOG:C-014, C-ANALOG:B-0093
- **metric-threshold-resolution.4** Ordonez et al. assert, without a test, that 1 km resolution could lower the differences; this conflicts in spirit with Mahony et al.'s localised low-elevation novelty, but the two address different quantities (total share against local presence), so they are not in direct contradiction.
  conf: not stated · class: not stated · holds: Ordonez 2024 against Mahony 2017 · src: ordonezTowardsNovelBiosphere2024, mahonyCloserLookNovel2017 · trail: C-ANALOG §1.5, §answers · from: C-ANALOG:B-0092, C-ANALOG:B-0093, C-ANALOG:A-024, C-ANALOG:A-033, C-ANALOG:A-034
- **metric-threshold-resolution.5** The effect of resolution on the total share is not measured in anything read; the resolution evidence is one abstract (Mahony 2017) plus one untested assertion (Ordonez 2024).
  conf: single (critic: C-014) · class: not stated · holds: the studies the review read · src: mahonyCloserLookNovel2017 (abstract only), ordonezTowardsNovelBiosphere2024 · trail: C-ANALOG §1.5, §4. Answers, §answers · search: not stated · from: C-ANALOG:B-0094, C-ANALOG:A-108, C-ANALOG:A-048
- **metric-threshold-resolution.6** The effects of threshold, resolution and the number of variables are poorly measured: nearest precedents, single studies, or unread supplements.
  conf: not stated · class: not stated · holds: the climate analogue studies the review covers · src: none (the reviewer's synthesis) · trail: C-ANALOG §4. Answers, §answers · rating: "Weak for the effects of the number of variables, of the threshold and of resolution" · from: C-ANALOG:A-106, C-ANALOG:A-027

### variable-count: the number of variables combined
needs: analogue-design
- **variable-count.1** No spatial-analogue study found varies the number of variables and reports the change in share; Veloz et al. 2012, which may test variable-set sensitivity, was not obtained, and only evidence that combinations reveal more novelty was sought.
  conf: not stated · class: search (note: "No spatial-analogue study found here varies the number of variables") · holds: the climate angle's queries (novel climates, no-analog climate, climate analogue, climatic novelty with Mahalanobis, sigma dissimilarity and SED, SDM extrapolation) · src: velozIdentifyingClimaticAnalogs2011 (not obtained) · trail: C-ANALOG §1.6, §critic, §answers, §Adversarial · search: searched, not found (note: "No spatial-analogue study found here varies the number of variables") · contrary: one-sided (critic: C-092) · from: C-ANALOG:B-0095, C-ANALOG:B-0105, C-ANALOG:C-016, C-ANALOG:A-019, C-ANALOG:A-036, C-ANALOG:C-092, C-ANALOG:B-0013
- **variable-count.2** Mesgaran, Cousens and Webber introduced ExDet, which separates novelty outside the univariate range (type 1) from novel correlations within it (type 2); for Acacia cyclops, 6,617 of 10,785 (61%) global projection points inside the univariate range of the native-range reference showed distorted correlations.
  conf: not stated · class: not stated · holds: an SDM geographic transfer, not change over time at a location; a nearest precedent · src: mesgaranHereBeDragons2014 (AB) · trail: C-ANALOG §1.6, §answers · from: C-ANALOG:B-0096, C-ANALOG:B-0097, C-ANALOG:B-0098, C-ANALOG:B-0099, C-ANALOG:B-0100, C-ANALOG:A-021
- **variable-count.3** Mahony and Cannon studied local departure from natural variability, not spatial analogues: the joint summer Tmax-precipitation regime departs at least 10 years before either variable alone on 16% (7-23%) of land; the paper's headline figure, 23% (9-34%) of land with pronounced departure intensification, is not reported in the review.
  conf: not stated · class: model (marker) · holds: global land, local time of emergence; a nearest precedent · src: mahonyWetterSummersCan2018 (FT-s, modelled) · trail: C-ANALOG §1.6, §answers, §Adversarial · from: C-ANALOG:I-0011, C-ANALOG:B-0101, C-ANALOG:B-0102, C-ANALOG:A-022, C-ANALOG:C-057
- **variable-count.4** The two nearest precedents show that joint judgement exposes novelty that single variables miss, but neither measures the share D1 asks about, and neither addresses how raw distance-based measures scale with dimension (how raw SED inflates with dimension compared with chi-distribution-scaled sigma dissimilarity), so 'more variables means more novelty' is not established for spatial analogue shares; remove both precedents and nothing remains.
  conf: not stated · class: not stated · holds: an SDM geographic transfer (Mesgaran 2014, abstract only) and local departure over time (Mahony and Cannon 2018) · src: mesgaranHereBeDragons2014, mahonyWetterSummersCan2018 · trail: C-ANALOG §1.6, §critic, §Adversarial, §answers, §4. Answers · contrary: one-sided (critic: C-092) · from: C-ANALOG:B-0103, C-ANALOG:B-0104, C-ANALOG:C-017, C-ANALOG:C-018, C-ANALOG:C-059, C-ANALOG:C-082, C-ANALOG:A-020, C-ANALOG:A-049, C-ANALOG:A-109

### palaeo-analogues: palaeoecological background
needs: analogue-design
- **palaeo-analogues.1** The modern analogue technique calibrates dissimilarity coefficients on modern pollen: in eastern North America, modern analogues existed for almost all Holocene samples but for none before about 9,300 to 11,000 years BP at two sites, and the choice of coefficient changed which samples counted as analogous.
  conf: not stated · class: meas (marker) · holds: fossil pollen at two sites in eastern North America · src: overpeckQuantitativeInterpretationFossil1985 (AB, measured) · trail: C-ANALOG §1.7 · from: C-ANALOG:I-0012, C-ANALOG:B-0106, C-ANALOG:B-0107
- **palaeo-analogues.2** Late-21st-century RCP8.5 climate novelty in North America is similar to or higher than peak novelty over the last 21,000 years, and forecast skill falls as novelty rises.
  conf: not stated · class: model (marker) · holds: North America · src: fitzpatrickHowWillClimate2018 (AB, modelled) · trail: C-ANALOG §1.7 · from: C-ANALOG:I-0013
- **palaeo-analogues.3** Climate novelty is the strongest predictor of vegetation novelty since the Last Glacial Maximum, but in Europe the relationship for transient novelty runs "opposite of expectation", a contrary result on how well climate novelty maps onto ecological novelty.
  conf: not stated · class: deriv (marker) · holds: Europe and eastern North America since the Last Glacial Maximum · src: burkeDifferingClimaticMechanisms2019 (AB, derived) · trail: C-ANALOG §1.7, §References · from: C-ANALOG:I-0014, C-ANALOG:B-0108, C-ANALOG:R-0125
- **palaeo-analogues.4** Six climate-change metrics give contrasting global patterns, so the answer to "where is change largest" depends on which dimension is measured.
  conf: not stated · class: model (marker) · holds: global · src: garciaMultipleDimensionsClimate2014 (AB, modelled) · trail: C-ANALOG §1.7 · from: C-ANALOG:I-0015

### soil-in-climate-analogues: soil in climate analogue studies
needs: analogue-design
- **soil-in-climate-analogues.1** In the agricultural analogue studies read in full, soil is excluded from matching, and the exclusion is named as a limitation.
  conf: not stated · class: assert (marker) · holds: Pugh 2016 and Chaudhary 2023 · src: pughClimateAnaloguesSuggest2016 (FT-s; asserted), chaudharyClimateAnalogsCan2023 (FT-s; asserted) · trail: C-ANALOG §1.8 · from: C-ANALOG:I-0016
- **soil-in-climate-analogues.2** Saxon et al. built 500 environmental domains from dynamic climate and static topography and soils; domains covering half the study area today disappear under the higher-emission scenario.
  conf: not stated · class: not stated · holds: soil as a static stratifier · src: saxonMappingEnvironmentsRisk2004 (AB) · trail: C-ANALOG §1.8 · from: C-ANALOG:B-0109, C-ANALOG:B-0110, C-ANALOG:B-0111
- **soil-in-climate-analogues.3** Keupp et al. admitted future climate analogues for Franconia only if texture and pH classes matched; by 2100 the analogues lie mostly in the northern Mediterranean.
  conf: not stated · class: not stated · holds: Franconia; soil as a static filter · src: keuppUndampedClimateChange2026 (FT-s) · trail: C-ANALOG §1.8 · from: C-ANALOG:B-0112, C-ANALOG:B-0113
- **soil-in-climate-analogues.4** Neither study that brings soil into a climate analogue search reports how much the soil criterion removes, and neither lets soil change; no analogue search that also matches soil was found beyond such static filters or strata.
  conf: not stated · class: not stated · holds: Saxon 2005 and Keupp 2026 · src: saxonMappingEnvironmentsRisk2004, keuppUndampedClimateChange2026 · trail: C-ANALOG §1.8, §answers · search: not stated · from: C-ANALOG:B-0114, C-ANALOG:A-040
- **soil-in-climate-analogues.5** Donmez et al. project 150 of 247 German long-term experiment sites to move into semi-arid aridity classes under SSP5-8.5; the abstract does not say whether those future conditions have present-day analogues.
  conf: not stated · class: not stated · holds: German long-term field experiments; read from the SSRN preprint record, not the published version cited · src: donmezClimateChangeImpacts (AB, the SSRN preprint record read), donmezClimateChangeImpacts2023 (the version cited) · trail: C-ANALOG §1.8, §Adversarial · from: C-ANALOG:B-0115, C-ANALOG:B-0116, C-ANALOG:C-051, C-ANALOG:C-068

### soil-direct-question: whether changed soil conditions fall within present-day ranges
needs: none
- **soil-direct-question.1** None of the three search angles (soil mapping, soil change, management) found a study that reports, for any soil variable and any driver, the share of changed soil conditions lying inside or outside the range or multivariate envelope of present-day sites, whether analogues are judged variable by variable or on combinations.
  conf: not stated · class: search (note: "None found a study that reports") · holds: Europe PMC, Crossref, Unpaywall, Semantic Scholar DOI lookups and publisher pages, with soil, digital soil mapping, soil ecology and management vocabularies; WebSearch unavailable · src: none (a search result) · trail: C-ANALOG §2.1, §critic, §answers, §4. Answers, §Provenance · rating: "moderate confidence" · search: searched, not found (note: "Every 'not found' in the review rests on these routes") · from: C-ANALOG:B-0117, C-ANALOG:B-0118, C-ANALOG:B-0119, C-ANALOG:B-0027, C-ANALOG:B-0024, C-ANALOG:B-0014, C-ANALOG:C-020, C-ANALOG:A-050, C-ANALOG:A-051, C-ANALOG:A-076, C-ANALOG:A-077, C-ANALOG:A-084, C-ANALOG:A-112, C-ANALOG:A-113
- **soil-direct-question.2** The absence is a claim about those searches, not a statement that the literature lacks such work; it is limited by WebSearch being unavailable to all agents, it does not depend on one source, and the critic finds it adequately framed as a claim about the search.
  conf: not stated · class: reading (note: "This is a claim about those searches") · holds: the three search angles · src: none (the reviewer's reading of its own search) · trail: C-ANALOG §2.1, §Provenance, §answers, §critic · from: C-ANALOG:B-0120, C-ANALOG:B-0007, C-ANALOG:B-0010, C-ANALOG:A-090, C-ANALOG:C-042
- **soil-direct-question.3** What exists falls into five groups: operational uses of the question without a reported share; coverage of present-day conditions by the reference sites themselves; driver-specific magnitudes that can be set against cross-site ranges only by the reviewer, not the authors; bounding results on inferring change from space; and methods (area of applicability, hypercube coverage, homosoils).
  conf: not stated · class: not stated · holds: the soil literature the review found · src: meyerPredictingUnknownSpace2020, meyerMachineLearningbasedGlobal2022, ludwigAssessingImprovingTransferability2023, carreEstimationPotentialImprovement2007, nenkamUsingHomosoilsQuantitative2022 · trail: C-ANALOG §answers, §2.1 · from: C-ANALOG:B-0121, C-ANALOG:A-052, C-ANALOG:A-053, C-ANALOG:A-056, C-ANALOG:A-058, C-ANALOG:A-063, C-ANALOG:A-068, C-ANALOG:A-114
- **soil-direct-question.4** On variable-by-variable against combination judgements there is no soil-change test, and the single-variable reviewer readings (managed pH mostly within cross-site pH ranges) do not answer the combination question.
  conf: not stated · class: search (note: "there is no soil-change test") · holds: the same searches · src: none (a search result) · trail: C-ANALOG §answers, §2.1 · search: searched, not found (note: "That holds whether analogues are judged variable by variable or on combinations") · from: C-ANALOG:A-069, C-ANALOG:A-072, C-ANALOG:B-0119
- **soil-direct-question.5** By driver, liming, N fertilisation, N deposition and land-use change have nearest precedents, and warming-driven carbon loss has only space-for-time analogue pairing.
  conf: not stated · class: not stated · holds: the soil drivers the review covers · src: none (the reviewer's synthesis) · trail: C-ANALOG §answers, §2.5 · from: C-ANALOG:A-073, C-ANALOG:A-074, C-ANALOG:B-0186
- **soil-direct-question.6** Drying (soil moisture), pollution and acid deposition as a standalone driver were not found or not searched in depth: the soil angle did not search soil moisture in depth, no angle searched pollutants, and drying, pollution and multivariate novelty of changed soil states have not been measured in anything found.
  conf: not stated · class: search (note: "No agent searched soil moisture change or soil pollution in depth") · holds: the three search angles · src: none (a search result) · trail: C-ANALOG §Provenance, §2.5, §answers, §4. Answers · search: not searched (note: "No agent searched soil moisture change or soil pollution in depth") · from: C-ANALOG:B-0015, C-ANALOG:B-0187, C-ANALOG:B-0188, C-ANALOG:A-075, C-ANALOG:A-120
- **soil-direct-question.7** Not measured, or not searched, for the direct question, for every driver: soil moisture or drying against the cross-site range; pollution (heavy metals, salinisation); soil temperature; acidification from deposition compared with regional pH ranges; long-term experiment plots compared quantitatively with regional survey distributions; multivariate novelty of changed soil states (pH, C, N, C/N jointly); any effect of the reference set of sites; and area shares outside the AOA for global soil maps (Ludwig 2023 and van den Hoogen 2019 were not obtained in full).
  conf: not stated · class: not stated · holds: the three search angles; some were not searched · src: none (the note's not-measured list) · trail: C-ANALOG §answers, §critic · search: not stated · from: C-ANALOG:A-085, C-ANALOG:C-028, C-ANALOG:A-084, C-ANALOG:B-0117
- **soil-direct-question.8** No conflict was found on the analogue-share question itself, because no study measures it.
  conf: not stated · class: not stated · holds: the soil question · src: none (a search result) · trail: C-ANALOG §answers · from: C-ANALOG:A-083

### soil-novelty-methods: methods for detecting analogues and novelty in soil space
needs: none
- **soil-novelty-methods.1** Meyer and Pebesma define the area of applicability (AOA) by a dissimilarity index, the minimum importance-weighted distance from a prediction point to the training data divided by the mean training-to-training distance, with the threshold at the outlier-removed maximum index of the training data under cross-validation; in simulations, error inside the AOA matched cross-validation error, and the AOA judges analogy on combinations of predictors.
  conf: not stated · class: model (marker) · holds: simulations · src: meyerPredictingUnknownSpace2020 (AB, modelled) · trail: C-ANALOG §2.2 · from: C-ANALOG:I-0017, C-ANALOG:B-0122, C-ANALOG:B-0123, C-ANALOG:B-0124
- **soil-novelty-methods.2** For WoSIS soil CEC profiles, distances from global prediction locations to the nearest profile far exceed the distances between profiles, and geographic gaps do not always imply feature-space gaps.
  conf: not stated · class: meas (marker) · holds: global maps from WoSIS profiles · src: meyerMachineLearningbasedGlobal2022 (FT-s, measured) · trail: C-ANALOG §2.2 · from: C-ANALOG:I-0018, C-ANALOG:B-0125
- **soil-novelty-methods.3** Ludwig et al. report that "reliable gap-free global predictions were not possible" even after predictor reduction; the shares outside the AOA were not obtained.
  conf: not stated · class: not stated · holds: current global spatial prediction models · src: ludwigAssessingImprovingTransferability2023 (AB) · trail: C-ANALOG §2.2, §References · limit: access (note: "the shares outside the AOA were not obtained") · from: C-ANALOG:B-0126, C-ANALOG:R-0142
- **soil-novelty-methods.4** The HELS hypercube method checks legacy soil samples against quantile strata of covariates, so it assesses coverage stratum by stratum rather than by distance.
  conf: not stated · class: meas (marker) · holds: legacy soil samples for digital soil mapping · src: carreEstimationPotentialImprovement2007 (AB, measured) · trail: C-ANALOG §2.2, §References · from: C-ANALOG:I-0019, C-ANALOG:R-0145
- **soil-novelty-methods.5** The homosoil approach searches the globe for places sharing soil-forming factors; homosoil-based extrapolation worked for Mali, but accuracy "dramatically improved" with local data, and homosoil maps beat global products for silt, sand and pH, not for clay, organic carbon or total N, so an analogue in soil-forming factors does not guarantee transferable soil relationships.
  conf: not stated · class: meas (marker) · holds: Mali; a bounding result; the original homosoil chapter is known only via this abstract · src: nenkamUsingHomosoilsQuantitative2022 (AB, measured), mallavanHomosoilMethodologyQuantitative2010 (SEC) · trail: C-ANALOG §2.2 · from: C-ANALOG:B-0127, C-ANALOG:I-0020, C-ANALOG:B-0128, C-ANALOG:B-0129

### soil-site-coverage: how well present-day sites cover soil space
needs: soil-novelty-methods
- **soil-site-coverage.1** Guerra et al. mapped 17,186 soil biodiversity and function sampling sites against SoilGrids and CHELSA layers: soil texture and pH are well represented "with the exception of extreme ranges (e.g., pH > 7.33 or silt content <19%)", and the authors write that 'most soil-related variables are well covered'.
  conf: not stated · class: meas (marker) · holds: soil biodiversity and function sampling sites; present-day conditions, not changed ones · src: guerraBlindSpotsGlobal2020 (FT-s, measured) · trail: C-ANALOG §2.3, §critic · from: C-ANALOG:I-0021, C-ANALOG:B-0130, C-ANALOG:B-0133, C-ANALOG:C-023, C-ANALOG:C-040
- **soil-site-coverage.2** 59.6% of global climate conditions are not covered by any study (Mahalanobis distance, chi-square 0.975 cut-off).
  conf: not stated · class: not stated · holds: climate variables, not soil variables · src: guerraBlindSpotsGlobal2020 · trail: C-ANALOG §2.3, §critic · from: C-ANALOG:B-0131, C-ANALOG:C-023
- **soil-site-coverage.3** Even in well-sampled Central and West Europe, combinations of high altitude, low pH and high carbon are uncovered; this is the only soil-combination statement, it is qualitative, and it rests on Guerra 2020 alone, so the review's contrast of combined against univariate coverage is not a like-for-like soil contrast.
  conf: single (critic: C-063) · class: not stated · holds: Central and West Europe; present-day sampling coverage · src: guerraBlindSpotsGlobal2020 · trail: C-ANALOG §2.3, §critic, §Adversarial · from: C-ANALOG:B-0132, C-ANALOG:B-0135, C-ANALOG:C-023, C-ANALOG:C-024, C-ANALOG:C-063, C-ANALOG:C-098, C-ANALOG:C-099
- **soil-site-coverage.4** SoilGrids 2.0 uncertainty is highest where observations are sparse, especially at high latitudes.
  conf: not stated · class: not stated · holds: SoilGrids 2.0 · src: poggioSoilGrids202021 (AB) · trail: C-ANALOG §2.3 · from: C-ANALOG:B-0136
- **soil-site-coverage.5** 205 German long-term field experiments broadly match the area shares of climatic water balance and soil quality classes of national agricultural area, with a bias toward high soil quality, and one grassland climate class (3% of grassland) has no experiment; this assesses the experiments' background conditions, not whether treated plots leave the regional range.
  conf: not stated · class: meas (marker) · holds: German national agricultural area · src: grosseLongtermFieldExperiments2020 (FT-s, measured) · trail: C-ANALOG §2.3, §Adversarial · from: C-ANALOG:I-0022, C-ANALOG:B-0137, C-ANALOG:B-0138, C-ANALOG:B-0139, C-ANALOG:C-079

### soil-analogue-uses: present-day sites used as analogues for changed soils
needs: soil-novelty-methods
- **soil-analogue-uses.bg1** Space-for-time substitution infers past or future trajectories of ecological systems from contemporary spatial patterns; its foundational assumption is that the drivers of spatial gradients also drive temporal change.
  kind: background · ref: bloisSpaceCanSubstitute2013 · check: DOI 10.1073/pnas.1220228110 resolves on Crossref (PNAS 110(23): 9374-9379); the definition and its assumption are in the abstract (Europe PMC, PMID 23690569)
- **soil-analogue-uses.1** Emde et al. predicted each German inventory site's SOC under the alternative land use from sites currently under that use, excluding sites outside the AOA (threshold 0.95) of the alternative-use training set; this is the closest operational use of the soil question found, with land-use change as the driver and national inventory sites as the reference, but the number of excluded sites appears only in a figure the search agent could not extract, so the share is unknown.
  conf: single (note: "SINGLE SOURCE") · class: model (marker) · holds: German agricultural and forest inventory sites · src: emdeSiteSpecificDriversLandUse2025 (FT-s, modelled) · trail: C-ANALOG §2.4, §critic, §answers, §3. How · from: C-ANALOG:I-0023, C-ANALOG:B-0140, C-ANALOG:B-0141, C-ANALOG:B-0142, C-ANALOG:B-0144, C-ANALOG:C-021, C-ANALOG:A-054, C-ANALOG:A-115, C-ANALOG:B-0193, C-ANALOG:R-0164
- **soil-analogue-uses.2** Removing Emde 2025 leaves no soil study that applies an analogue or AOA test to changed conditions.
  conf: not stated · class: reading (note: "Single-source sensitivity") · holds: the D2 evidence base · src: none (the reviewer's sensitivity reading) · trail: C-ANALOG §answers · from: C-ANALOG:A-090, C-ANALOG:A-091
- **soil-analogue-uses.3** The Emde authors' own conclusion concerns depth: about 30% of land-use-change-driven SOC change occurs at 30-90 cm.
  conf: not stated · class: not stated · holds: German soils · src: emdeSiteSpecificDriversLandUse2025 · trail: C-ANALOG §2.4 · from: C-ANALOG:B-0143, C-ANALOG:I-0023
- **soil-analogue-uses.4** Wang et al. paired 113,013 profiles into "ambient" and "warm" 1 degree C classes matched on landform, soil type and precipitation (difference <50 mm) and estimate 6.0 +/- 1.6% loss of topsoil SOC stock per degree; pairs were sparse in tundra (<100), but no share of conditions lacking a matched analogue is reported.
  conf: not stated · class: deriv (marker) · holds: 113,013 global soil profiles · src: wangGlobalSoilProfiles2022 (FT-s, derived) · trail: C-ANALOG §2.4, §critic, §answers, §4. Answers · from: C-ANALOG:I-0024, C-ANALOG:B-0145, C-ANALOG:B-0146, C-ANALOG:C-022, C-ANALOG:A-055, C-ANALOG:A-116, C-ANALOG:R-0167
- **soil-analogue-uses.5** The same paper compiled 85 warming experiments (261 observations) and found forest SOC change "on average neutral", against significant losses from space-for-time; the authors attribute the gap to short experiments, partial warming and the assumption of similar soil histories.
  conf: single (critic: C-027) · class: meas (note: "measured; BOUNDING") · holds: forests; one paper · src: wangGlobalSoilProfiles2022 · trail: C-ANALOG §2.4, §answers, §critic · from: C-ANALOG:B-0147, C-ANALOG:B-0148, C-ANALOG:A-064, C-ANALOG:A-079, C-ANALOG:A-080, C-ANALOG:C-027
- **soil-analogue-uses.6** Heuvelink et al. predicted only modest change in Argentinian SOC from 1982 to 2017, with substantial uncertainty that they attribute to the number and distribution of calibration data.
  conf: not stated · class: not stated · holds: Argentina, space-time mapping · src: heuvelinkMachineLearningSpace2020 (AB) · trail: C-ANALOG §2.4 · from: C-ANALOG:B-0149
- **soil-analogue-uses.7** Helfenstein et al. mapped 2050 soil organic matter in the Netherlands and name "predicting future trends based on historic data" as their main limitation; neither space-time mapping study reports whether future covariates fall inside the training space.
  conf: not stated · class: not stated · holds: the Netherlands, space-time mapping · src: helfensteinNatureinclusiveFutureHealthy2024 (AB), heuvelinkMachineLearningSpace2020 · trail: C-ANALOG §2.4 · from: C-ANALOG:B-0150, C-ANALOG:B-0151

### soil-driver-magnitudes: how far drivers move soil variables, against cross-site ranges
needs: soil-direct-question
- **soil-driver-magnitudes.1** None of the driver studies compares changed values with the range of other sites: the comparisons are the reviewer's readings, per-variable (almost all pH) and indirect, and most rest on abstracts or on a summarising tool (Leff 2015).
  conf: not stated · class: reading (note: "reviewer's readings") · holds: liming, N addition, long-term ammonium sulphate and Chinese cropland acidification · src: none (the reviewer's reading) · trail: C-ANALOG §2.5, §critic, §answers, §Adversarial · rating: "The indirect driver-specific readings are weak" · contrary: one-sided (critic: C-097) · from: C-ANALOG:B-0152, C-ANALOG:B-0153, C-ANALOG:C-025, C-ANALOG:C-026, C-ANALOG:C-097, C-ANALOG:A-058, C-ANALOG:A-078
- **soil-driver-magnitudes.2** On the Hoosfield acid strip at Rothamsted, a 19th-century chalk application left a pH gradient of 4.0-8.3 within about 200 m (the abstract says 180 m).
  conf: not stated · class: not stated · holds: one arable field · src: rouskSoilBacterialFungal2010 (FT-s) · trail: C-ANALOG §2.5, §Adversarial, §References · from: C-ANALOG:B-0154, C-ANALOG:C-050, C-ANALOG:R-0180
- **soil-driver-magnitudes.3** Bacterial community variation across the Hoosfield gradient matched that among 88 American soils spanning pH below 3.5 to nearly 9.0; the 88-soils range is Rousk's citation of another study (Lauber et al. 2009).
  conf: not stated · class: meas (marker) · holds: one field against a continental set of 88 American soils · src: rouskSoilBacterialFungal2010 (SEC, measured; critic: C-050 was "FT-s, measured"), lauber2009 · trail: C-ANALOG §2.5, §Adversarial · from: C-ANALOG:I-0025, C-ANALOG:C-050, C-ANALOG:B-0155
- **soil-driver-magnitudes.4** The reviewer reads the liming result as a management-generated pH range at one site that spans most of a continental cross-site pH range and sits inside it, not beyond it; the authors' conclusion concerns pH control of microbial communities, not analogues, and the reading rests on Rousk 2010.
  conf: not stated · class: reading (note: "Reviewer's reading") · holds: one field · src: rouskSoilBacterialFungal2010 · trail: C-ANALOG §2.5, §answers · from: C-ANALOG:B-0155, C-ANALOG:B-0156, C-ANALOG:B-0157, C-ANALOG:A-059, C-ANALOG:A-092
- **soil-driver-magnitudes.5** Goulding and Holland et al. describe liming as pulling pH toward agronomic targets (UK 6.5 arable, 6.0 grassland), report non-representative figures of about 40% of arable and 57% of grassland soils below target, and Holland et al. note that liming changes "all elements in soils" simultaneously, which bears on combinations, though no combination has been tested.
  conf: not stated · class: assert (marker) · holds: the UK · src: gouldingSoilAcidificationImportance2016 (FT-s, asserted), hollandLimingImpactsSoils2018 (AB, asserted) · trail: C-ANALOG §2.5, §answers · from: C-ANALOG:I-0026, C-ANALOG:B-0158, C-ANALOG:B-0159, C-ANALOG:B-0160, C-ANALOG:A-071
- **soil-driver-magnitudes.6** In 25 Nutrient Network grasslands, N addition lowered pH by 0.16 units against an among-site range of 4.5-8.4, and the authors conclude the pH change was too small to drive the microbial shifts; the two figures are not in the abstract.
  conf: not stated · class: meas (marker) · holds: a global grassland network (Nutrient Network) · src: leffConsistentResponsesSoil2015 (secondary, measured; critic: C-048 was "FT-s via a summarising fetch tool, measured") · trail: C-ANALOG §2.5, §Adversarial, §answers · limit: access (critic: C-049) · from: C-ANALOG:I-0027, C-ANALOG:B-0161, C-ANALOG:C-047, C-ANALOG:C-048, C-ANALOG:C-049, C-ANALOG:A-093, C-ANALOG:A-060
- **soil-driver-magnitudes.7** Tian and Niu's meta-analysis of 106 studies found a mean pH change of -0.26 (-0.49 in grasslands) under N addition, a response rising with N rate above about 5 g N m-2 yr-1, and no response where initial pH was 3-4 (initial pH range 3-7.7); the last detail is not in the abstract and was unverified.
  conf: not stated · class: meas (marker) · holds: 106 N-addition studies · src: tianGlobalAnalysisSoil2015 (FT-s, measured) · trail: C-ANALOG §2.5, §answers, §Adversarial · limit: access (critic: C-061) · from: C-ANALOG:I-0028, C-ANALOG:B-0162, C-ANALOG:B-0163, C-ANALOG:B-0164, C-ANALOG:A-060, C-ANALOG:C-055, C-ANALOG:C-061
- **soil-driver-magnitudes.8** The Tian and Niu abstract reports that N-addition effects on soil pH diminish in experiments longer than 20 years, a finding relevant to long-term plots that the review omitted.
  conf: not stated · class: not stated · holds: N-addition experiments by duration · src: tianGlobalAnalysisSoil2015 (abstract) · trail: C-ANALOG §Adversarial · from: C-ANALOG:C-055, C-ANALOG:I-0028, C-ANALOG:R-0170
- **soil-driver-magnitudes.9** N addition to an already very acid tropical forest soil (pH <4.0) did not change exchangeable Al3+.
  conf: not stated · class: meas (marker) · holds: a tropical forest soil · src: luNitrogenDepositionContributes2014 (AB, measured) · trail: C-ANALOG §2.5 · from: C-ANALOG:I-0029
- **soil-driver-magnitudes.10** The reviewer reads the acid end of the natural range as acting as a floor in the N-addition data; the reading rests on Tian and Niu 2015 (the initial pH 3-4 detail unverified) plus Lu 2014 (abstract only).
  conf: not stated · class: reading (note: "Reviewer's reading: the acid end of the natural range acts as a floor") · holds: N addition to acid soils · src: tianGlobalAnalysisSoil2015, luNitrogenDepositionContributes2014 · trail: C-ANALOG §2.5, §Adversarial · from: C-ANALOG:B-0165, C-ANALOG:C-061, C-ANALOG:I-0028, C-ANALOG:I-0029
- **soil-driver-magnitudes.11** Experimental N rates (0.93-60 g m-2 yr-1) mostly exceed the 5-35 kg ha-1 yr-1 (0.5-3.5 g m-2 yr-1) ambient deposition gradient across 68 British grasslands, so the driver itself is often applied outside the range of present-day deposition even where the resulting pH is not outside the range of present-day soils.
  conf: not stated · class: reading (note: "A second reviewer's reading, derived from two papers") · holds: experimental N rates against 68 British grasslands · src: stevensImpactNitrogenDeposition2004 (AB) · trail: C-ANALOG §2.5 · from: C-ANALOG:B-0166, C-ANALOG:B-0167
- **soil-driver-magnitudes.12** Park Grass plot pH spans about 3.3-7.4 or 3.6-7, and the plots reach pH 3.3-3.6 under long-term ammonium sulphate.
  conf: not stated · class: not stated · holds: the Park Grass Experiment · src: rouskFungalBacterialGrowth2011 (AB), zhalninaSoilPHDetermines2014 (AB) · trail: C-ANALOG §2.5, §answers · from: C-ANALOG:B-0168, C-ANALOG:B-0169, C-ANALOG:A-061
- **soil-driver-magnitudes.13** Ammonium sulphate also raises soil carbon and C/N at Park Grass.
  conf: not stated · class: assert (note: "asserted in the abstract") · holds: the Park Grass Experiment · src: zhalninaSoilPHDetermines2014 · trail: C-ANALOG §2.5 · from: C-ANALOG:B-0170, C-ANALOG:B-0168, C-ANALOG:B-0169
- **soil-driver-magnitudes.14** Grassland diversity recovered after N stopped, except "where there has been extreme acidification"; Crawley et al. report large pH decreases and richness from 3 to 44 species.
  conf: not stated · class: not stated · holds: the Park Grass Experiment · src: storkeyGrasslandBiodiversityBounces2015 (AB), crawleyDeterminantsSpeciesRichness2005 (AB) · trail: C-ANALOG §2.5 · from: C-ANALOG:B-0171, C-ANALOG:B-0172, C-ANALOG:B-0168
- **soil-driver-magnitudes.15** Ward et al. reproduce the Park Grass pattern in a 65-year South African experiment.
  conf: not stated · class: not stated · holds: Ukulinga, South Africa · src: wardAfricanGrasslandResponds2017 (AB) · trail: C-ANALOG §2.5 · from: C-ANALOG:B-0168, C-ANALOG:B-0173
- **soil-driver-magnitudes.16** Poulton et al. report Geescroft Wilderness pH falling from 7.1 (1883) to 4.4 (1999), and manure plots raising SOC toward new equilibria over 80-100 years.
  conf: not stated · class: not stated · holds: Rothamsted long-term experiments · src: poultonMajorLimitationsAchieving2018 (FT-s) · trail: C-ANALOG §2.5 · from: C-ANALOG:B-0174, C-ANALOG:B-0168
- **soil-driver-magnitudes.17** The reviewer reads the most acidified Park Grass plots as lying near the bottom of cross-site pH ranges, and the joint shift in pH, C and C/N as a candidate route to combinations not found elsewhere; no study found tests either against a regional reference set.
  conf: not stated · class: reading (note: "Reviewer's reading: the most acidified Park Grass plots") · holds: the Park Grass Experiment · src: none (the reviewer's reading) · trail: C-ANALOG §2.5, §Adversarial · search: not stated · from: C-ANALOG:B-0175, C-ANALOG:B-0176, C-ANALOG:C-113
- **soil-driver-magnitudes.18** Silvertown et al. state that comparisons among sites, nutrient inputs or soil acidity "may in general underestimate the threat" from long-term nutrient change.
  conf: single (note: "SINGLE SOURCE") · class: assert (marker) · holds: one abstract on the Park Grass Experiment, used as a bounding result · src: silvertownParkGrassExperiment2006 (AB, asserted) · trail: C-ANALOG §2.5, §answers, §Adversarial · from: C-ANALOG:I-0030, C-ANALOG:B-0177, C-ANALOG:A-065, C-ANALOG:C-064
- **soil-driver-magnitudes.19** Chinese cropland pH fell significantly from the 1980s to the 2000s.
  conf: not stated · class: meas (marker) · holds: major Chinese croplands · src: guoSignificantAcidificationMajor2010 (AB, measured) · trail: C-ANALOG §2.5, §References · from: C-ANALOG:I-0031, C-ANALOG:R-0214
- **soil-driver-magnitudes.20** Chinese national mean cropland pH went from 7.1 (1980) to 6.6 (2018), and about a quarter of neutral soils moved into acidic classes.
  conf: not stated · class: meas (marker) · holds: Chinese croplands, 1980 to 2018 · src: chenNationalScaleAssessmentSoil2025 (AB, measured) · trail: C-ANALOG §2.5, §answers · from: C-ANALOG:I-0032, C-ANALOG:A-062
- **soil-driver-magnitudes.21** A scenario of 1% annual growth in N input projects a further fall in Chinese cropland pH of about one unit by 2050.
  conf: not stated · class: model (marker) · holds: Chinese croplands · src: zhuCroplandAcidificationIncreases2020 (AB, modelled) · trail: C-ANALOG §2.5 · from: C-ANALOG:I-0033, C-ANALOG:I-0031
- **soil-driver-magnitudes.22** The reviewer reads the Chinese change as movement between classes already occupied nationally; whether any cells left the 1980 range was not tested in the abstract, and the full text was not obtained.
  conf: not stated · class: reading (note: "Reviewer's reading of [46]") · holds: Chinese croplands · src: chenNationalScaleAssessmentSoil2025 (abstract) · trail: C-ANALOG §2.5 · limit: access (note: "the full text was not obtained") · from: C-ANALOG:B-0178, C-ANALOG:B-0179, C-ANALOG:I-0031, C-ANALOG:I-0032
- **soil-driver-magnitudes.23** Soil pH in England and Wales rose under all land uses from 1978 to 2003, during recovery from acid deposition.
  conf: not stated · class: not stated · holds: the national inventory of England and Wales · src: kirkChangesSoilPH2009 (AB) · trail: C-ANALOG §2.5 · from: C-ANALOG:B-0180, C-ANALOG:B-0181
- **soil-driver-magnitudes.24** Topsoil carbon change in Great Britain is contested: the National Soil Inventory reported SOC loss of 0.6% per year, while the Countryside Survey found no net topsoil C change from 1978 to 2007 and calls the difference "unresolved".
  conf: cont (note: "contested") · class: not stated · holds: national resurveys of Great Britain · src: bellamyCarbonLossesAll2005 (AB), reynoldsCountrysideSurveyNational2013 (AB) · trail: C-ANALOG §2.5, §answers · from: C-ANALOG:B-0182, C-ANALOG:B-0183, C-ANALOG:A-081
- **soil-driver-magnitudes.25** The national resurveys report shifts in means by habitat, not shares of sites leaving the reference distribution.
  conf: not stated · class: not stated · holds: national resurveys · src: kirkChangesSoilPH2009, bellamyCarbonLossesAll2005, reynoldsCountrysideSurveyNational2013 · trail: C-ANALOG §2.5 · from: C-ANALOG:B-0184
- **soil-driver-magnitudes.26** Global soil pH shows an abrupt alkaline-to-acid transition where precipitation exceeds potential evapotranspiration, the shape of the present-day reference distribution any comparison would use.
  conf: not stated · class: meas (marker) · holds: global soils · src: slessarevWaterBalanceCreates2016 (AB, measured) · trail: C-ANALOG §2.5 · from: C-ANALOG:I-0034, C-ANALOG:B-0185
- **soil-driver-magnitudes.27** A machine-learning estimate puts P-fertilisation-driven increases in resin P at 37% and N-driven decreases at 10%, relative to unfertilised soil, not to the range across sites.
  conf: not stated · class: model (marker) · holds: global-scale, agricultural fertilisation against unfertilised soil · src: qiGlobalscalePatternsBioavailable2026 (AB, modelled) · trail: C-ANALOG §2.5, §References · from: C-ANALOG:I-0035, C-ANALOG:R-0244

### soil-failure-modes: limits on inferring soil change from space
needs: soil-analogue-uses
- **soil-failure-modes.1** Change that depends on the baseline value is partly regression to the mean; a published comment disputes aspects of the proposed correction, known only secondarily via the search agent.
  conf: cont (note: "a published comment disputes aspects") · class: deriv (marker) · holds: baseline-dependent change in soil monitoring · src: larkBaselineValuesChange2006 (AB, derived) · trail: C-ANALOG §2.6, §answers · from: C-ANALOG:I-0036, C-ANALOG:A-066, C-ANALOG:A-082, C-ANALOG:R-0235
- **soil-failure-modes.2** Monitoring networks may need about 10 years to detect some large SOC changes, which bounds any attempt to place measured change against spatial variability.
  conf: not stated · class: model (marker) · holds: European soil-monitoring networks · src: sabyWillEuropeanSoilmonitoring2008 (AB, modelled) · trail: C-ANALOG §2.6, §answers, §References · from: C-ANALOG:I-0037, C-ANALOG:A-067, C-ANALOG:R-0238
- **soil-failure-modes.3** Bounding results caution against inferring temporal change from spatial contrasts.
  conf: not stated · class: not stated · holds: Wang 2022, Silvertown 2006 and Lark 2006 · src: wangGlobalSoilProfiles2022, silvertownParkGrassExperiment2006, larkBaselineValuesChange2006 · trail: C-ANALOG §4. Answers, §answers · from: C-ANALOG:A-119, C-ANALOG:A-063

### climate-soil-relation: how the climate and soil cases relate
needs: global-climate-shares, soil-novelty-methods
- **climate-soil-relation.1** Two literatures answer the question very differently: the climate literature has a shared toolkit (scaled distance, a biome-calibrated or percentile threshold, an explicit candidate pool) that it has used to produce shares comparable within studies, while the soil literature has the equivalent toolkit (the AOA dissimilarity index, hypercube coverage, homosoils) and has used it to judge where maps can be trusted and, in one case (land-use change), to exclude changed states from prediction, but not to report how many changed states lack analogues.
  conf: not stated · class: not stated · holds: the climate and soil literatures the review covers · src: none (the reviewer's synthesis) · trail: C-ANALOG §3. How, §Present-day · from: C-ANALOG:B-0025, C-ANALOG:B-0026, C-ANALOG:B-0028, C-ANALOG:B-0029, C-ANALOG:B-0190..0193
- **climate-soil-relation.2** Evidence from climate does not answer the soil question, and nor does the ocean pH result, which is seawater chemistry under a globally uniform forcing.
  conf: not stated · class: not stated · holds: the climate and ocean studies against the soil question · src: lotterhosNovelDisappearingClimates2021 · trail: C-ANALOG §3. How · from: C-ANALOG:B-0194, C-ANALOG:B-0195
- **climate-soil-relation.3** The reviewer argues, without a source, that ocean pH evidence does not transfer because most soil drivers (liming, fertiliser) are local and imposed on already varied soils.
  conf: not stated · class: reading (critic: C-105) · holds: the reviewer's argument · src: none (the reviewer's argument) · trail: C-ANALOG §3. How, §Adversarial · from: C-ANALOG:B-0195, C-ANALOG:C-105

## Do not say
- **dns.1** "Projected climates are novel on 67-76% of land by 2100 and on over 97% by 2300."
  why: These are unverified figures from a search agent's reading of Ordonez 2024, and its abstract gives different headline figures, over 50% of land by 2100 and over 80% by 2300, for novel ecosystems combined across three metrics. · instead: global-climate-shares.6, global-climate-shares.7 · trail: C-ANALOG §critic, §Adversarial · from: C-ANALOG:C-035, C-ANALOG:C-036, C-ANALOG:C-044, C-ANALOG:A-010, C-ANALOG:A-096
- **dns.2** "Ordonez et al. 2024 find roughly double Williams et al.'s share of novel climate for comparable forcing, the largest conflict in the literature."
  why: The 'roughly double Williams' conflict is not established as like for like: the Ordonez abstract figure combines three metrics and the review compares it directly with Williams' single-metric no-analogue share, and the answer states the conflict firmly on unverified access. · instead: global-climate-shares.9, global-climate-shares.8 · trail: C-ANALOG §critic, §Adversarial, §1.2 · from: C-ANALOG:C-010, C-ANALOG:C-045, C-ANALOG:C-102, C-ANALOG:B-0054, C-ANALOG:A-029
- **dns.3** "3% to 68% of land shows significant phytoclimate change by 2070."
  why: The source says 33% to 68%; the review misprints it. · instead: global-climate-shares.11 · trail: C-ANALOG §critic, §Adversarial · from: C-ANALOG:C-032, C-ANALOG:C-054, C-ANALOG:C-070, C-ANALOG:B-0059
- **dns.4** "With a deep-time pool, fewer than 1.5% of locations lack an analogue under RCP4.5."
  why: The Burke 2018 abstract says under 1% for RCP4.5, and the review's full-text figures were not re-opened. · instead: reference-domain.7 · trail: C-ANALOG §critic, §Adversarial · from: C-ANALOG:C-037, C-ANALOG:C-052, C-ANALOG:B-0072, C-ANALOG:A-015
- **dns.5** "The candidate pool is the single most consistent control on the share of novel climate."
  why: As a controlled contrast this rests on two within-study contrasts only, Williams 2007 (500 km) and Burke 2018 (deep time); the crop, county and city studies are between-study comparisons. · instead: reference-domain.10 · trail: C-ANALOG §Adversarial, §critic · from: C-ANALOG:C-058, C-ANALOG:C-039, C-ANALOG:B-0066
- **dns.6** "Restricting the pool to a crop's own area, a national county set or a city hull raises novelty, as Pugh, Chaudhary and Bastin show."
  why: Those studies contain no unrestricted contrast, so they do not show that narrowing the pool raises novelty; the answer mixes them with within-study controlled contrasts. · instead: reference-domain.10 · trail: C-ANALOG §critic, §Adversarial, §4. Answers · from: C-ANALOG:C-013, C-ANALOG:C-038, C-ANALOG:C-103, C-ANALOG:A-102, C-ANALOG:B-0067
- **dns.7** "Bastin et al. overstate their reference set by claiming that these climates do not exist 'on the planet today'."
  why: That phrase is not in the abstract, which says 'not currently experienced by any existing major cities', so the critique of the authors rests on a misquote or on unverified body text. · instead: reference-domain.5 · trail: C-ANALOG §critic, §Adversarial · from: C-ANALOG:C-033, C-ANALOG:C-034, C-ANALOG:C-053, C-ANALOG:C-109, C-ANALOG:B-0070, C-ANALOG:B-0071
- **dns.8** "Judging climate variable by variable understates novelty."
  why: The claim is phrased generally but rests on two nearest precedents from different settings (Mesgaran 2014, abstract only; Mahony and Cannon 2018), neither of which addresses how distance measures scale with dimension. · instead: variable-count.4 · trail: C-ANALOG §Adversarial, §critic · from: C-ANALOG:C-059, C-ANALOG:C-018, C-ANALOG:B-0103
- **dns.9** "Recasting climate in a biological state space is the clearest demonstration that the state space moves the share by one to two orders of magnitude."
  why: The state-space effect rests on Conradi 2024 alone; the review flags this but still calls it the clearest demonstration in the set. · instead: global-climate-shares.13 · trail: C-ANALOG §Adversarial · from: C-ANALOG:C-062, C-ANALOG:B-0064
- **dns.10** "Present-day soil sampling covers combinations of soil variables worse than single soil variables."
  why: In Guerra 2020 the 59.6% uncovered figure is for climate combinations, and the authors write that most soil-related variables are well covered; the only soil-combination statement is qualitative, so the review's reading merges soil univariate with climate combination coverage and carries it into the D2 answer as a soil result. · instead: soil-site-coverage.3, soil-site-coverage.1 · trail: C-ANALOG §critic, §Adversarial, §4. Answers · from: C-ANALOG:C-040, C-ANALOG:C-098, C-ANALOG:C-100, C-ANALOG:A-057, C-ANALOG:A-070, C-ANALOG:A-094, C-ANALOG:A-117, C-ANALOG:B-0134
- **dns.11** "Space-for-time substitution and manipulative experiments disagree in sign for forest SOC."
  why: As a general failure mode this rests on Wang et al. 2022 alone. · instead: soil-analogue-uses.5 · trail: C-ANALOG §Adversarial, §2.6 · from: C-ANALOG:C-060, C-ANALOG:B-0189
- **dns.12** "N deposition, like liming and N addition, has a nearest precedent in the soil evidence."
  why: N-addition experiments and ambient N deposition sit under one bullet, and the D2 answer counts N deposition as having a nearest precedent when the precedent is mostly experimental addition. · instead: soil-driver-magnitudes.6, soil-driver-magnitudes.11 · trail: C-ANALOG §Adversarial · from: C-ANALOG:C-104, C-ANALOG:A-073
- **dns.13** "Lotterhos et al.'s result is evidence that climate novelty depends on the scenario."
  why: Lotterhos et al. analysed surface ocean temperature, pH and aragonite saturation, a marine chemical case that the D1 answer lists among climate scenario evidence without a label. · instead: scenario-horizon.3, scenario-horizon.4 · trail: C-ANALOG §Adversarial · from: C-ANALOG:C-101, C-ANALOG:A-009
- **dns.14** "Managed and fertiliser-driven changes in soil pH mostly stay within present-day cross-site pH ranges."
  why: That is the reviewer's own per-variable reading, built into the D2 answer; set against the absence finding, these readings stand in for the missing measurement, and the answer to a literature question should lead with what the sources report. · instead: soil-driver-magnitudes.1, soil-direct-question.1 · trail: C-ANALOG §Adversarial, §4. Answers · from: C-ANALOG:C-106, C-ANALOG:C-107, C-ANALOG:C-108, C-ANALOG:A-118
- **dns.15** "The climate analogue evidence rests mostly on full text."
  why: Several load-bearing full-text sources read by a search agent (Ordonez, Burke, Bastin, Chaudhary, Lotterhos) were not re-opened by the synthesis agent, as the synthesis role requires. · instead: analogue-design.5 · trail: C-ANALOG §Adversarial, §answers · from: C-ANALOG:C-056, C-ANALOG:A-041, C-ANALOG:A-111
- **dns.16** "Cross-site comparisons underestimate temporal soil change, as the Park Grass Experiment shows."
  why: This is Silvertown 2006's assertion, in one abstract, used as a bounding result in the D2 answer. · instead: soil-driver-magnitudes.18 · trail: C-ANALOG §Adversarial · from: C-ANALOG:C-064, C-ANALOG:A-065
- **dns.17** "One limed field spans pH 4.0-8.3 within about 200 m, most of the 3.5-9.0 range measured across 88 American soils in the same study."
  why: The 88-soils range is Rousk's citation of another study (Lauber et al. 2009), so it is secondary for that range, and the abstract says 180 m, not about 200 m. · instead: soil-driver-magnitudes.2, soil-driver-magnitudes.3 · trail: C-ANALOG §Adversarial · from: C-ANALOG:C-050, C-ANALOG:A-059
- **dns.18** "N addition causes no pH response where initial pH is 3-4, so the acid end of the natural range is a floor."
  why: The initial pH 3-4 detail is from a search agent's reading and not in the Tian and Niu abstract, and the floor reading rests on that unverified detail plus one abstract (Lu 2014). · instead: soil-driver-magnitudes.7, soil-driver-magnitudes.10 · trail: C-ANALOG §Adversarial · from: C-ANALOG:C-055, C-ANALOG:C-061, C-ANALOG:A-060

## Gaps
- **gap.1** Whether experimental drought treatments or drying fall outside the natural range of soil moisture or precipitation, the drying driver for D2; the distributed-experiment literature compares imposed drought with historical extremes (Knapp et al. 2017; Kröel-Dulay et al. 2022), named as candidate routes and not verified.
  blocks: soil-direct-question · origin: critic coverage gap; stage 2 check triggered a follow-up brief · search: not searched (critic: C-071) · src: knappPushingPrecipitationExtremes2017, kroeldulay2022 · from: C-ANALOG:C-071, C-ANALOG:C-072, C-ANALOG:C-073, C-ANALOG:C-074, C-ANALOG:B-0021
- **gap.2** Soil temperature, as a soil physical variable changed by warming: novel soil thermal regimes or permafrost-affected soils relative to present-day sites.
  blocks: soil-direct-question · origin: critic coverage gap; stage 2 check triggered a follow-up brief · search: not searched (critic: C-075) · from: C-ANALOG:C-075, C-ANALOG:B-0021
- **gap.3** Pollution drivers: heavy metals, salinisation from irrigation or sea-level rise, and sodicity, in the contaminated-land and salinity-mapping communities.
  blocks: soil-direct-question · origin: critic coverage gap; stage 2 check triggered a follow-up brief · search: not searched (critic: C-076) · from: C-ANALOG:C-076, C-ANALOG:B-0021
- **gap.4** Global or regional soil-map studies reporting the share of area outside the AOA or convex hull (Ludwig 2023 and van den Hoogen 2019 not obtained in full), digital soil mapping papers reporting dissimilarity-index shares for national pH or SOC maps, and SDMs with soil predictors reporting MESS or ExDet novelty for future projections.
  blocks: soil-novelty-methods, soil-direct-question · origin: critic coverage gap; the stage 2 follow-up brief is on area-of-applicability shares in digital soil mapping · search: not searched (critic: C-077) · src: ludwigAssessingImprovingTransferability2023, vandenhoogenSoilNematodeAbundance2019 · from: C-ANALOG:C-077, C-ANALOG:B-0021, C-ANALOG:B-0023
- **gap.5** Long-term experiment plots compared quantitatively with regional survey distributions; only Grosse 2020 (background conditions) was found, and networks such as NutNet, GLTEN or national long-term experiment databases were not searched for treated-plot soil values against national inventories.
  blocks: soil-driver-magnitudes · origin: critic coverage gap (the brief's Evidence bullet); the stage 2 follow-up brief covers experimental and managed soil conditions against survey ranges · search: not searched (critic: C-080) · src: grosseLongtermFieldExperiments2020 · from: C-ANALOG:C-078, C-ANALOG:C-080, C-ANALOG:B-0021, C-ANALOG:B-0023
- **gap.6** The number of variables in spatial climate analogues: Veloz 2012 and the Mahony 2017 PC-truncation analysis were not obtained, and nothing addresses how raw SED inflates with dimension compared with chi-distribution-scaled sigma dissimilarity, a scaling that could reverse or cancel the variable-count effect; no contrary evidence was sought.
  blocks: variable-count · origin: critic coverage gap and one-sided-handling finding; the stage 2 check lists the Mahony 2017 dimension analysis · search: not stated · contrary: one-sided (critic: C-092) · src: velozIdentifyingClimaticAnalogs2011, mahonyCloserLookNovel2017 · from: C-ANALOG:C-081, C-ANALOG:C-083, C-ANALOG:C-092, C-ANALOG:B-0022
- **gap.7** Threshold sensitivity of the global shares: the Williams 2007 Supporting Information (SEDt = 5.33, SI Figs. 5-7) is freely available with the PNAS article but was not retrieved, and Pugh's threshold robustness figure (Supplementary Fig. 19) concerns yields only.
  blocks: metric-threshold-resolution · origin: critic coverage gap; a source not obtained · search: not stated · src: williamsProjectedDistributionsNovel2007, pughClimateAnaloguesSuggest2016 · from: C-ANALOG:C-084, C-ANALOG:B-0022, C-ANALOG:R-0059, C-ANALOG:R-0060, C-ANALOG:R-0061
- **gap.8** Observed, as opposed to projected, climate change against present-day or historical analogues: the time-of-emergence and observed-departure literature and analogue analyses of observed 20th-century change on land.
  blocks: scenario-horizon · origin: critic coverage gap; the note's not-measured list · search: not searched (critic: C-085) · from: C-ANALOG:C-085, C-ANALOG:A-038, C-ANALOG:B-0022
- **gap.9** Regional analogue studies outside North America (European city-analogue work, agricultural climate-analogue tools used in Africa and South Asia such as the CCAFS Climate Analogues work) and CMIP6-based estimates; all reported shares come from CMIP3 or CMIP5.
  blocks: global-climate-shares, reference-domain · origin: critic coverage gap; the note's not-measured list · search: not stated · from: C-ANALOG:C-086, C-ANALOG:A-039, C-ANALOG:B-0022
- **gap.10** The SDM extrapolation community: MESS (Elith 2010) and Fitzpatrick and Hargrove 2009 were not obtained, and other extrapolation-visualisation and calibration-area constraint papers were not searched, so the SDM novelty background rests on one abstract (Mesgaran).
  blocks: variable-count · origin: critic coverage gap · search: not searched (critic: C-087) · src: elithArtModellingRangeshifting2010, fitzpatrickProjectionSpeciesDistribution2009, mesgaranHereBeDragons2014 · from: C-ANALOG:C-087
- **gap.11** The palaeo modern analogue technique: only Overpeck 1985 (abstract) and two Quaternary-novelty abstracts were read, Williams and Jackson 2007 was not obtained, and there is no evidence on how the choice of analogue threshold in pollen MAT shifts no-analogue shares.
  blocks: palaeo-analogues · origin: critic coverage gap · search: not stated · src: overpeckQuantitativeInterpretationFossil1985, williamsNovelClimatesNoanalog2007 · from: C-ANALOG:C-088, C-ANALOG:C-089, C-ANALOG:C-090
- **gap.12** How the choice of reference set of sites (national against global soil databases) changes whether changed soil values count as within range, which D2 asks about explicitly.
  blocks: soil-direct-question · origin: critic coverage gap; the note's not-measured list · search: not stated · from: C-ANALOG:C-091
- **gap.13** Any analogue search that also matches soil, beyond static soil filters or strata that do not report how much the soil criterion removes.
  blocks: soil-in-climate-analogues · origin: the note's not-measured list · search: not stated · src: saxonMappingEnvironmentsRisk2004, keuppUndampedClimateChange2026 · from: C-ANALOG:A-040
- **gap.14** The stage 2 check was triggered: the critic's gaps name soil variables and practices where analogue frequency is measured under other names, so a follow-up brief on area-of-applicability shares in digital soil mapping and on experimental and managed soil conditions against survey ranges is to be written, sized separately.
  blocks: none · origin: the note's stage 2 check (ROUTING condition met) · search: not stated · from: C-ANALOG:B-0020, C-ANALOG:B-0021, C-ANALOG:B-0022, C-ANALOG:B-0023
- **gap.15** What sets the low and high ends of each Williams 2007 range was not found in the main text and remains unverified.
  blocks: global-climate-shares.2 · origin: the reviewer's re-reading · search: not stated · src: williamsProjectedDistributionsNovel2007 · from: C-ANALOG:B-0050, C-ANALOG:B-0051, C-ANALOG:B-0018
- **gap.16** Load-bearing full-text sources read only by a search agent were not re-opened: Ordonez 2024 and Burke 2018 could not be re-opened (captcha page; Europe PMC XML error; for Ordonez also PMC HTML captcha, Royal Society block and no body in the eutils XML), and Bastin 2019, Chaudhary 2023 and Lotterhos 2021 were not re-opened.
  blocks: global-climate-shares, reference-domain, scenario-horizon · origin: critic access error; the reviewer's checks · search: not stated · src: ordonezTowardsNovelBiosphere2024, burkePlioceneEoceneProvide2018, bastinUnderstandingClimateChange2019, chaudharyClimateAnalogsCan2023, lotterhosNovelDisappearingClimates2021 · from: C-ANALOG:C-030, C-ANALOG:C-043, C-ANALOG:C-046, C-ANALOG:C-056, C-ANALOG:B-0018
- **gap.17** Climate sources not obtained: Veloz et al. 2012 (climatic analogs for Wisconsin), Ordonez and Williams 2013, Ordonez, Williams and Svenning 2016, the Mahony et al. 2017 full text, Williams and Jackson 2007, Fitzpatrick and Hargrove 2009 and Elith et al. 2010; the note says none supports any claim in the review.
  blocks: variable-count, palaeo-analogues · origin: sources not obtained · search: not stated · src: velozIdentifyingClimaticAnalogs2011, ordonezProjectedClimateReshuffling2013, ordonezMappingClimaticMechanisms2016, mahonyCloserLookNovel2017, williamsNovelClimatesNoanalog2007, fitzpatrickProjectionSpeciesDistribution2009, elithArtModellingRangeshifting2010 · from: C-ANALOG:R-0001..0021
- **gap.18** Soil sources not obtained: the full texts of Ludwig et al. 2023, Saby et al. 2008, Storkey et al. 2015, Chen et al. 2025 and Guo et al. 2010 (with its supplement), the homosoil chapter (Mallavan et al. 2010), Bertrand et al. 2012, van den Hoogen et al. 2019, Silvertown et al. 2006, Blake et al. 1999, Johnston et al. 1986, and Stevens et al. 2004 beyond an abstract with no pH figures.
  blocks: soil-novelty-methods, soil-driver-magnitudes, soil-failure-modes · origin: sources not obtained · search: not stated · src: ludwigAssessingImprovingTransferability2023, sabyWillEuropeanSoilmonitoring2008, storkeyGrasslandBiodiversityBounces2015, chenNationalScaleAssessmentSoil2025, guoSignificantAcidificationMajor2010, mallavanHomosoilMethodologyQuantitative2010, bertrandDisregardingEdaphicDimension2012, vandenhoogenSoilNematodeAbundance2019, silvertownParkGrassExperiment2006, blakeChangesSoilChemistry1999, johnstonSoilAcidificationMore1986, stevensImpactNitrogenDeposition2004 · from: C-ANALOG:R-0022..0058, C-ANALOG:R-0062..0073
- **gap.19** The note's lists contradict each other on Silvertown 2006: the reference list says "one search agent read the abstract; another reached only the record", while Sources not obtained gives "Europe PMC (record only, no abstract)".
  blocks: soil-driver-magnitudes.18 · origin: a note that contradicts itself · search: not stated · src: silvertownParkGrassExperiment2006 · from: C-ANALOG:I-0030, C-ANALOG:R-0041, C-ANALOG:R-0042, C-ANALOG:R-0043
- **gap.20** The published comment disputing Lark et al. 2006's regression-to-the-mean correction is known only secondarily, via the search agent, and is not identified.
  blocks: soil-failure-modes.1 · origin: a source known only second-hand · search: not stated · src: larkBaselineValuesChange2006 · from: C-ANALOG:A-082, C-ANALOG:I-0036

## Out of scope
- C-ANALOG:C-029, C-ANALOG:C-031: the critic's record of which sources it checked and which figures match (verification record, kept in the result note)
- C-ANALOG:C-065..067, C-ANALOG:C-069: reference checks (DOIs resolved, metadata matched, venue naming acceptable), applied in Sources
- C-ANALOG:C-110..114: expectation echo (the brief's presupposition and its absence from the review; provenance of the critique, not a finding)
- C-ANALOG:A-042..044: access basis of the D1 answer (provenance, applied in Sources)
- C-ANALOG:A-086..089: access basis of the D2 answer (provenance, applied in Sources)

## Sources
```bibtex
@article{williamsProjectedDistributionsNovel2007,
  author = {Williams, John W. and Jackson, Stephen T. and Kutzbach, John E.},
  title = {Projected distributions of novel and disappearing climates by 2100 AD},
  journal = {Proceedings of the National Academy of Sciences of the USA},
  year = {2007},
  volume = {104},
  number = {14},
  pages = {5738-5742},
  doi = {10.1073/pnas.0606292104},
  note = {access: full_text (FT-r, re-opened by the reviewer; Supporting Information with the SEDt = 5.33 sensitivity not retrieved); cited as: C-ANALOG [1] (FT-r)}
}

@article{ordonezTowardsNovelBiosphere2024,
  author = {Ordonez, Alejandro and Riede, Felix and Normand, Signe and Svenning, Jens-Christian},
  title = {Towards a novel biosphere in 2300: rapid and extensive global and biome-wide climatic novelty in the Anthropocene},
  journal = {Philosophical Transactions of the Royal Society B},
  year = {2024},
  volume = {379},
  number = {1902},
  pages = {20230022},
  doi = {10.1098/rstb.2023.0022},
  note = {access: full_text (FT-s, read by a search agent, not re-opened; the reviewer and the critic were blocked from the full text; the critic checked the abstract); cited as: C-ANALOG [2] (FT-s)}
}

@article{conradiReassessmentRisksClimate2024,
  author = {Conradi, Timo and Eggli, Urs and Kreft, Holger and Schweiger, Andreas H. and Weigelt, Patrick and Higgins, Steven I.},
  title = {Reassessment of the risks of climate change for terrestrial ecosystems},
  journal = {Nature Ecology & Evolution},
  year = {2024},
  volume = {8},
  number = {5},
  pages = {888-900},
  doi = {10.1038/s41559-024-02333-8},
  note = {access: full_text (FT-r, re-opened by the reviewer); cited as: C-ANALOG [3] (FT-r)}
}

@article{mahonyCloserLookNovel2017,
  author = {Mahony, Colin R. and Cannon, Alex J. and Wang, Tongli and Aitken, Sally N.},
  title = {A closer look at novel climates: new methods and insights at continental to landscape scales},
  journal = {Global Change Biology},
  year = {2017},
  volume = {23},
  number = {9},
  pages = {3934-3955},
  doi = {10.1111/gcb.13645},
  note = {access: abstract_only (re-read via OpenAlex; full text not obtained); cited as: C-ANALOG [4] (AB (re-read via OpenAlex))}
}

@article{mahonyWetterSummersCan2018,
  author = {Mahony, Colin R. and Cannon, Alex J.},
  title = {Wetter summers can intensify departures from natural variability in a warming climate},
  journal = {Nature Communications},
  year = {2018},
  volume = {9},
  pages = {783},
  doi = {10.1038/s41467-018-03132-z},
  note = {access: full_text (FT-s per the reference list; the critic checked the Nature full text); cited as: C-ANALOG [5] (FT-s)}
}

@article{fitzpatrickContemporaryClimaticAnalogs2019,
  author = {Fitzpatrick, Matthew C. and Dunn, Robert R.},
  title = {Contemporary climatic analogs for 540 North American urban areas in the late 21st century},
  journal = {Nature Communications},
  year = {2019},
  volume = {10},
  pages = {614},
  doi = {10.1038/s41467-019-08540-3},
  note = {access: full_text (FT-r, re-opened by the reviewer); cited as: C-ANALOG [6] (FT-r)}
}

@article{bastinUnderstandingClimateChange2019,
  author = {Bastin, Jean-Francois and Clark, Emily and Elliott, Thomas and Hart, Simon and van den Hoogen, Johan and Hordijk, Iris and Ma, Haozhi and Majumder, Sabiha and Manoli, Gabriele and Maschler, Julia and Mo, Lidong and Routh, Devin and Yu, Kailiang and Zohner, Constantin M. and Crowther, Thomas W.},
  title = {Understanding climate change from a global analysis of city analogues},
  journal = {PLOS ONE},
  year = {2019},
  volume = {14},
  number = {7},
  pages = {e0217592},
  doi = {10.1371/journal.pone.0217592},
  note = {access: full_text (FT-s, read by a search agent, not re-opened); cited as: C-ANALOG [7] (FT-s)}
}

@article{burkePlioceneEoceneProvide2018,
  author = {Burke, K. D. and Williams, J. W. and Chandler, M. A. and Haywood, A. M. and Lunt, D. J. and Otto-Bliesner, B. L.},
  title = {Pliocene and Eocene provide best analogs for near-future climates},
  journal = {Proceedings of the National Academy of Sciences of the USA},
  year = {2018},
  volume = {115},
  number = {52},
  pages = {13288-13293},
  doi = {10.1073/pnas.1809600115},
  note = {access: full_text (FT-s, read by a search agent, not re-opened); cited as: C-ANALOG [8] (FT-s)}
}

@article{pughClimateAnaloguesSuggest2016,
  author = {Pugh, T. A. M. and Müller, C. and Elliott, J. and Deryng, D. and Folberth, C. and Olin, S. and Schmid, E. and Arneth, A.},
  title = {Climate analogues suggest limited potential for intensification of production on current croplands under climate change},
  journal = {Nature Communications},
  year = {2016},
  volume = {7},
  pages = {12608},
  doi = {10.1038/ncomms12608},
  note = {access: full_text (FT-s per the reference list; the critic checked the PMC XML); cited as: C-ANALOG [9] (FT-s)}
}

@article{chaudharyClimateAnalogsCan2023,
  author = {Chaudhary, Siddharth and Rajagopalan, Kirti and Kruger, Chad E. and Brady, Michael P. and Fraisse, Clyde W. and Gustafson, David I. and Hall, Sonia A. and Hoogenboom, Gerrit and Melnick, Rachel L. and Reyes, Julian and Stöckle, Claudio O. and Sulser, Timothy B.},
  title = {Climate analogs can catalyze cross-regional dialogs for US specialty crop adaptation},
  journal = {Scientific Reports},
  year = {2023},
  volume = {13},
  pages = {9317},
  doi = {10.1038/s41598-023-35887-x},
  note = {access: full_text (FT-s, read by a search agent, not re-opened); cited as: C-ANALOG [10] (FT-s)}
}

@article{lotterhosNovelDisappearingClimates2021,
  author = {Lotterhos, Katie E. and Láruson, Áki J. and Jiang, Li-Qing},
  title = {Novel and disappearing climates in the global surface ocean from 1800 to 2100},
  journal = {Scientific Reports},
  year = {2021},
  volume = {11},
  pages = {15535},
  doi = {10.1038/s41598-021-94872-4},
  note = {access: full_text (FT-s, read by a search agent, not re-opened); cited as: C-ANALOG [11] (FT-s)}
}

@article{mesgaranHereBeDragons2014,
  author = {Mesgaran, Mohsen B. and Cousens, Roger D. and Webber, Bruce L.},
  title = {Here be dragons: a tool for quantifying novelty due to covariate range and correlation change when projecting species distribution models},
  journal = {Diversity and Distributions},
  year = {2014},
  volume = {20},
  number = {10},
  pages = {1147-1159},
  doi = {10.1111/ddi.12209},
  note = {access: abstract_only; cited as: C-ANALOG [12] (AB)}
}

@article{saxonMappingEnvironmentsRisk2004,
  author = {Saxon, Earl and Baker, Barry and Hargrove, William and Hoffman, Forrest and Zganjar, Chris},
  title = {Mapping environments at risk under different global climate change scenarios},
  journal = {Ecology Letters},
  year = {2005},
  volume = {8},
  number = {1},
  pages = {53-60},
  doi = {10.1111/j.1461-0248.2004.00694.x},
  note = {access: abstract_only; online-first 2004 per Crossref (the note's note on dates); cited as: C-ANALOG [13] (AB)}
}

@article{overpeckQuantitativeInterpretationFossil1985,
  author = {Overpeck, J. T. and Webb, III, T. and Prentice, I. C.},
  title = {Quantitative interpretation of fossil pollen spectra: dissimilarity coefficients and the method of modern analogs},
  journal = {Quaternary Research},
  year = {1985},
  volume = {23},
  number = {1},
  pages = {87-108},
  doi = {10.1016/0033-5894(85)90074-2},
  note = {access: abstract_only; cited as: C-ANALOG [14] (AB)}
}

@article{fitzpatrickHowWillClimate2018,
  author = {Fitzpatrick, Matthew C. and Blois, Jessica L. and Williams, John W. and Nieto-Lugilde, Diego and Maguire, Kaitlin C. and Lorenz, David J.},
  title = {How will climate novelty influence ecological forecasts? Using the Quaternary to assess future reliability},
  journal = {Global Change Biology},
  year = {2018},
  volume = {24},
  number = {8},
  pages = {3575-3586},
  doi = {10.1111/gcb.14138},
  note = {access: abstract_only; cited as: C-ANALOG [15] (AB)}
}

@article{garciaMultipleDimensionsClimate2014,
  author = {Garcia, Raquel A. and Cabeza, Mar and Rahbek, Carsten and Araújo, Miguel B.},
  title = {Multiple dimensions of climate change and their implications for biodiversity},
  journal = {Science},
  year = {2014},
  volume = {344},
  number = {6183},
  pages = {1247579},
  doi = {10.1126/science.1247579},
  note = {access: abstract_only; cited as: C-ANALOG [16] (AB)}
}

@article{burkeDifferingClimaticMechanisms2019,
  author = {Burke, Kevin D. and Williams, John W. and Brewer, Simon and Finsinger, Walter and Giesecke, Thomas and Lorenz, David J. and Ordonez, Alejandro},
  title = {Differing climatic mechanisms control transient and accumulated vegetation novelty in Europe and eastern North America},
  journal = {Philosophical Transactions of the Royal Society B},
  year = {2019},
  volume = {374},
  number = {1788},
  pages = {20190218},
  doi = {10.1098/rstb.2019.0218},
  note = {access: abstract_only; cited as: C-ANALOG [17] (AB)}
}

@article{keuppUndampedClimateChange2026,
  author = {Keupp, Luzia and Hotho, Andreas and Dech, Stefan and Paeth, Heiko},
  title = {Undamped climate change poses the need for substantial shifts in cultivated crop types in Germany},
  journal = {Scientific Reports},
  year = {2026},
  volume = {16},
  pages = {7945},
  doi = {10.1038/s41598-026-42040-x},
  note = {access: full_text (FT-s, read by a search agent); cited as: C-ANALOG [18] (FT-s)}
}

@article{donmezClimateChangeImpacts2023,
  author = {Donmez, Cenk and Schmidt, Marcus and Cilek, Ahmet and Grosse, Meike and Paul, Carsten and Hierold, Wilfried and Helming, Katharina},
  title = {Climate change impacts on long-term field experiments in Germany},
  journal = {Agricultural Systems},
  year = {2023},
  volume = {205},
  pages = {103578},
  doi = {10.1016/j.agsy.2022.103578},
  note = {access: abstract_only (read from the SSRN preprint record doi:10.2139/ssrn.4034620, not this published version; critic: C-ANALOG:C-051); cited as: C-ANALOG [19] (AB (read from SSRN preprint record doi:10.2139/ssrn.4034620))}
}

@article{meyerPredictingUnknownSpace2020,
  author = {Meyer, Hanna and Pebesma, Edzer},
  title = {Predicting into unknown space? Estimating the area of applicability of spatial prediction models},
  journal = {Methods in Ecology and Evolution},
  year = {2021},
  volume = {12},
  number = {9},
  pages = {1620-1633},
  doi = {10.1111/2041-210X.13650},
  note = {access: abstract_only; cited as: C-ANALOG [20] (AB)}
}

@article{meyerMachineLearningbasedGlobal2022,
  author = {Meyer, Hanna and Pebesma, Edzer},
  title = {Machine learning-based global maps of ecological variables and the challenge of assessing them},
  journal = {Nature Communications},
  year = {2022},
  volume = {13},
  pages = {2208},
  doi = {10.1038/s41467-022-29838-9},
  note = {access: full_text (FT-s, read by a search agent); cited as: C-ANALOG [21] (FT-s)}
}

@article{ludwigAssessingImprovingTransferability2023,
  author = {Ludwig, Marvin and Moreno-Martinez, Alvaro and Hölzel, Norbert and Pebesma, Edzer and Meyer, Hanna},
  title = {Assessing and improving the transferability of current global spatial prediction models},
  journal = {Global Ecology and Biogeography},
  year = {2023},
  volume = {32},
  number = {3},
  pages = {356-368},
  doi = {10.1111/geb.13635},
  note = {access: abstract_only (full text not obtained; abstract read via Crossref); cited as: C-ANALOG [22] (AB)}
}

@article{carreEstimationPotentialImprovement2007,
  author = {Carré, F. and McBratney, Alex B. and Minasny, B.},
  title = {Estimation and potential improvement of the quality of legacy soil samples for digital soil mapping},
  journal = {Geoderma},
  year = {2007},
  volume = {141},
  number = {1-2},
  pages = {1-14},
  doi = {10.1016/j.geoderma.2007.01.018},
  note = {access: abstract_only; cited as: C-ANALOG [23] (AB)}
}

@article{nenkamUsingHomosoilsQuantitative2022,
  author = {Nenkam, Andree M. and Wadoux, Alexandre M. J.-C. and Minasny, Budiman and McBratney, Alex B. and Traore, Pierre C. S. and Falconnier, Gatien N. and Whitbread, Anthony M.},
  title = {Using homosoils for quantitative extrapolation of soil mapping models},
  journal = {European Journal of Soil Science},
  year = {2022},
  volume = {73},
  number = {5},
  pages = {e13285},
  doi = {10.1111/ejss.13285},
  note = {access: abstract_only; cited as: C-ANALOG [24] (AB)}
}

@article{guerraBlindSpotsGlobal2020,
  author = {Guerra, Carlos A. and Heintz-Buschart, Anna and Sikorski, Johannes and Chatzinotas, Antonis and Guerrero-Ramírez, Nathaly and Cesarz, Simone and Beaumelle, Léa and Rillig, Matthias C. and Maestre, Fernando T. and Delgado-Baquerizo, Manuel and Buscot, François and Overmann, Jörg and Patoine, Guillaume and Phillips, Helen R. P. and Winter, Marten and Wubet, Tesfaye and Küsel, Kirsten and Bardgett, Richard D. and Cameron, Erin K. and Cowan, Don and Grebenc, Tine and Marín, César and Orgiazzi, Alberto and Singh, Brajesh K. and Wall, Diana H. and Eisenhauer, Nico},
  title = {Blind spots in global soil biodiversity and ecosystem function research},
  journal = {Nature Communications},
  year = {2020},
  volume = {11},
  pages = {3870},
  doi = {10.1038/s41467-020-17688-2},
  note = {access: full_text (FT-s per the reference list; the critic checked the PMC XML); cited as: C-ANALOG [25] (FT-s)}
}

@article{poggioSoilGrids202021,
  author = {Poggio, Laura and de Sousa, Luis M. and Batjes, Niels H. and Heuvelink, Gerard B. M. and Kempen, Bas and Ribeiro, Eloi and Rossiter, David},
  title = {SoilGrids 2.0: producing soil information for the globe with quantified spatial uncertainty},
  journal = {SOIL},
  year = {2021},
  volume = {7},
  number = {1},
  pages = {217-240},
  doi = {10.5194/soil-7-217-2021},
  note = {access: abstract_only; cited as: C-ANALOG [26] (AB)}
}

@article{heuvelinkMachineLearningSpace2020,
  author = {Heuvelink, Gerard B. M. and Angelini, Marcos E. and Poggio, Laura and Bai, Zhanguo and Batjes, Niels H. and van den Bosch, Rik and Bossio, Deborah and Estella, Sergio and Lehmann, Johannes and Olmedo, Guillermo F. and Sanderman, Jonathan},
  title = {Machine learning in space and time for modelling soil organic carbon change},
  journal = {European Journal of Soil Science},
  year = {2021},
  volume = {72},
  number = {4},
  pages = {1607-1623},
  doi = {10.1111/ejss.12998},
  note = {access: abstract_only; online-first 2020 per Crossref (the note's note on dates); cited as: C-ANALOG [27] (AB)}
}

@article{helfensteinNatureinclusiveFutureHealthy2024,
  author = {Helfenstein, Anatol and Mulder, Vera L. and Hack-ten Broeke, Mirjam J. D. and Breman, Bas C.},
  title = {A nature-inclusive future with healthy soils? Mapping soil organic matter in 2050 in the Netherlands},
  journal = {European Journal of Soil Science},
  year = {2024},
  volume = {75},
  number = {4},
  pages = {e13529},
  doi = {10.1111/ejss.13529},
  note = {access: abstract_only; cited as: C-ANALOG [28] (AB)}
}

@article{emdeSiteSpecificDriversLandUse2025,
  author = {Emde, David and Sakhaee, Ali and Poeplau, Christopher and Don, Axel and Scherstjanoi, Marc and Wellbrock, Nicole and Schneider, Florian},
  title = {Site-specific drivers of land-use change effects on organic carbon in German agriculture and forest soils},
  journal = {Global Change Biology},
  year = {2025},
  volume = {31},
  number = {10},
  pages = {e70576},
  doi = {10.1111/gcb.70576},
  note = {access: full_text (FT-s, read by a search agent); cited as: C-ANALOG [29] (FT-s)}
}

@article{wangGlobalSoilProfiles2022,
  author = {Wang, Mingming and Guo, Xiaowei and Zhang, Shuai and Xiao, Liujun and Mishra, Umakant and Yang, Yuanhe and Zhu, Biao and Wang, Guocheng and Mao, Xiali and Qian, Tian and Jiang, Tong and Shi, Zhou and Luo, Zhongkui},
  title = {Global soil profiles indicate depth-dependent soil carbon losses under a warmer climate},
  journal = {Nature Communications},
  year = {2022},
  volume = {13},
  pages = {5514},
  doi = {10.1038/s41467-022-33278-w},
  note = {access: full_text (FT-s, read by a search agent); cited as: C-ANALOG [30] (FT-s)}
}

@article{tianGlobalAnalysisSoil2015,
  author = {Tian, Dashuan and Niu, Shuli},
  title = {A global analysis of soil acidification caused by nitrogen addition},
  journal = {Environmental Research Letters},
  year = {2015},
  volume = {10},
  number = {2},
  pages = {024019},
  doi = {10.1088/1748-9326/10/2/024019},
  note = {access: full_text (FT-s, read by a search agent); cited as: C-ANALOG [31] (FT-s)}
}

@article{stevensImpactNitrogenDeposition2004,
  author = {Stevens, Carly J. and Dise, Nancy B. and Mountford, J. Owen and Gowing, David J.},
  title = {Impact of nitrogen deposition on the species richness of grasslands},
  journal = {Science},
  year = {2004},
  volume = {303},
  number = {5665},
  pages = {1876-1879},
  doi = {10.1126/science.1094678},
  note = {access: abstract_only (Europe PMC abstract read, no pH figures); cited as: C-ANALOG [32] (AB)}
}

@article{leffConsistentResponsesSoil2015,
  author = {Leff, Jonathan W. and Jones, Stuart E. and Prober, Suzanne M. and Barberán, Albert and Borer, Elizabeth T. and Firn, Jennifer L. and Harpole, W. Stanley and Hobbie, Sarah E. and Hofmockel, Kirsten S. and Knops, Johannes M. H. and McCulley, Rebecca L. and La Pierre, Kimberly and Risch, Anita C. and Seabloom, Eric W. and Schütz, Martin and Steenbock, Christopher and Stevens, Carly J. and Fierer, Noah},
  title = {Consistent responses of soil microbial communities to elevated nutrient inputs in grasslands across the globe},
  journal = {Proceedings of the National Academy of Sciences of the USA},
  year = {2015},
  volume = {112},
  number = {35},
  pages = {10967-10972},
  doi = {10.1073/pnas.1508382112},
  note = {access: secondary (critic: C-ANALOG:C-048; the note said FT-s via a page-summarising fetch tool); cited as: C-ANALOG [33] (FT-s (via a page-summarising fetch tool))}
}

@article{rouskSoilBacterialFungal2010,
  author = {Rousk, Johannes and Bååth, Erland and Brookes, Philip C. and Lauber, Christian L. and Lozupone, Catherine and Caporaso, J. Gregory and Knight, Rob and Fierer, Noah},
  title = {Soil bacterial and fungal communities across a pH gradient in an arable soil},
  journal = {The ISME Journal},
  year = {2010},
  volume = {4},
  number = {10},
  pages = {1340-1351},
  doi = {10.1038/ismej.2010.58},
  note = {access: full_text (FT-s, read by a search agent); secondary for the 88-soils pH range, which is Rousk's citation of Lauber et al. 2009 (critic: C-ANALOG:C-050); cited as: C-ANALOG [34] (FT-s)}
}

@article{rouskFungalBacterialGrowth2011,
  author = {Rousk, Johannes and Brookes, Philip C. and Bååth, Erland},
  title = {Fungal and bacterial growth responses to N fertilization and pH in the 150-year 'Park Grass' UK grassland experiment},
  journal = {FEMS Microbiology Ecology},
  year = {2011},
  volume = {76},
  number = {1},
  pages = {89-99},
  doi = {10.1111/j.1574-6941.2010.01032.x},
  note = {access: abstract_only; cited as: C-ANALOG [35] (AB)}
}

@article{zhalninaSoilPHDetermines2014,
  author = {Zhalnina, Kateryna and Dias, Raquel and de Quadros, Patricia Dörr and Davis-Richardson, Austin and Camargo, Flavio A. O. and Clark, Ian M. and McGrath, Steve P. and Hirsch, Penny R. and Triplett, Eric W.},
  title = {Soil pH determines microbial diversity and composition in the Park Grass Experiment},
  journal = {Microbial Ecology},
  year = {2015},
  volume = {69},
  number = {2},
  pages = {395-406},
  doi = {10.1007/s00248-014-0530-2},
  note = {access: abstract_only; online-first 2014 per Crossref (the note's note on dates); cited as: C-ANALOG [36] (AB)}
}

@article{crawleyDeterminantsSpeciesRichness2005,
  author = {Crawley, M. J. and Johnston, A. E. and Silvertown, J. and Dodd, M. and de Mazancourt, C. and Heard, M. S. and Henman, D. F. and Edwards, G. R.},
  title = {Determinants of species richness in the Park Grass Experiment},
  journal = {The American Naturalist},
  year = {2005},
  volume = {165},
  number = {2},
  pages = {179-192},
  doi = {10.1086/427270},
  note = {access: abstract_only; cited as: C-ANALOG [37] (AB)}
}

@article{storkeyGrasslandBiodiversityBounces2015,
  author = {Storkey, J. and Macdonald, A. J. and Poulton, P. R. and Scott, T. and Köhler, I. H. and Schnyder, H. and Goulding, K. W. T. and Crawley, M. J.},
  title = {Grassland biodiversity bounces back from long-term nitrogen addition},
  journal = {Nature},
  year = {2015},
  volume = {528},
  number = {7582},
  pages = {401-404},
  doi = {10.1038/nature16444},
  note = {access: abstract_only (full text not obtained; Nature pages redirect to login); cited as: C-ANALOG [38] (AB)}
}

@article{silvertownParkGrassExperiment2006,
  author = {Silvertown, Jonathan and Poulton, Paul and Johnston, Edward and Edwards, Grant and Heard, Matthew and Biss, Pamela M.},
  title = {The Park Grass Experiment 1856-2006: its contribution to ecology},
  journal = {Journal of Ecology},
  year = {2006},
  volume = {94},
  number = {4},
  pages = {801-814},
  doi = {10.1111/j.1365-2745.2006.01145.x},
  note = {access: abstract_only (one search agent read the abstract; another reached only the record); conflict: the note's Sources not obtained says record only, no abstract; cited as: C-ANALOG [39] (AB (one search agent read the abstract; another reached only the record))}
}

@article{wardAfricanGrasslandResponds2017,
  author = {Ward, David and Kirkman, Kevin and Tsvuura, Zivanai},
  title = {An African grassland responds similarly to long-term fertilization to the Park Grass experiment},
  journal = {PLOS ONE},
  year = {2017},
  volume = {12},
  number = {5},
  pages = {e0177208},
  doi = {10.1371/journal.pone.0177208},
  note = {access: abstract_only; cited as: C-ANALOG [40] (AB)}
}

@article{poultonMajorLimitationsAchieving2018,
  author = {Poulton, Paul and Johnston, Johnny and Macdonald, Andy and White, Rodger and Powlson, David},
  title = {Major limitations to achieving "4 per 1000" increases in soil organic carbon stock in temperate regions: evidence from long-term experiments at Rothamsted Research, United Kingdom},
  journal = {Global Change Biology},
  year = {2018},
  volume = {24},
  number = {6},
  pages = {2563-2584},
  doi = {10.1111/gcb.14066},
  note = {access: full_text (FT-s, read by a search agent); cited as: C-ANALOG [41] (FT-s)}
}

@article{gouldingSoilAcidificationImportance2016,
  author = {Goulding, K. W. T.},
  title = {Soil acidification and the importance of liming agricultural soils with particular reference to the United Kingdom},
  journal = {Soil Use and Management},
  year = {2016},
  volume = {32},
  number = {3},
  pages = {390-399},
  doi = {10.1111/sum.12270},
  note = {access: full_text (FT-s, read by a search agent); cited as: C-ANALOG [42] (FT-s)}
}

@article{hollandLimingImpactsSoils2018,
  author = {Holland, J. E. and Bennett, A. E. and Newton, A. C. and White, P. J. and McKenzie, B. M. and George, T. S. and Pakeman, R. J. and Bailey, J. S. and Fornara, D. A. and Hayes, R. C.},
  title = {Liming impacts on soils, crops and biodiversity in the UK: a review},
  journal = {Science of the Total Environment},
  year = {2018},
  volume = {610-611},
  pages = {316-332},
  doi = {10.1016/j.scitotenv.2017.08.020},
  note = {access: abstract_only; cited as: C-ANALOG [43] (AB)}
}

@article{luNitrogenDepositionContributes2014,
  author = {Lu, Xiankai and Mao, Qinggong and Gilliam, Frank S. and Luo, Yiqi and Mo, Jiangming},
  title = {Nitrogen deposition contributes to soil acidification in tropical ecosystems},
  journal = {Global Change Biology},
  year = {2014},
  volume = {20},
  number = {12},
  pages = {3790-3801},
  doi = {10.1111/gcb.12665},
  note = {access: abstract_only; cited as: C-ANALOG [44] (AB)}
}

@article{guoSignificantAcidificationMajor2010,
  author = {Guo, J. H. and Liu, X. J. and Zhang, Y. and Shen, J. L. and Han, W. X. and Zhang, W. F. and Christie, P. and Goulding, K. W. T. and Vitousek, P. M. and Zhang, F. S.},
  title = {Significant acidification in major Chinese croplands},
  journal = {Science},
  year = {2010},
  volume = {327},
  number = {5968},
  pages = {1008-1010},
  doi = {10.1126/science.1182570},
  note = {access: abstract_only (full text and supplement not obtained); cited as: C-ANALOG [45] (AB)}
}

@article{chenNationalScaleAssessmentSoil2025,
  author = {Chen, Zhong and Yin, Yulong and Gong, Haiqing and Wang, Hongye and Ying, Hao and Zhang, Hongyan and Cui, Zhenling},
  title = {National-scale assessment of soil pH change in Chinese croplands from 1980 to 2018},
  journal = {Agronomy},
  year = {2025},
  volume = {15},
  number = {12},
  pages = {2775},
  doi = {10.3390/agronomy15122775},
  note = {access: abstract_only (full text not obtained); cited as: C-ANALOG [46] (AB)}
}

@article{zhuCroplandAcidificationIncreases2020,
  author = {Zhu, Qichao and Liu, Xuejun and Hao, Tianxiang and Zeng, Mufan and Shen, Jianbo and Zhang, Fusuo and de Vries, Wim},
  title = {Cropland acidification increases risk of yield losses and food insecurity in China},
  journal = {Environmental Pollution},
  year = {2020},
  volume = {256},
  pages = {113145},
  doi = {10.1016/j.envpol.2019.113145},
  note = {access: abstract_only; cited as: C-ANALOG [47] (AB)}
}

@article{slessarevWaterBalanceCreates2016,
  author = {Slessarev, E. W. and Lin, Y. and Bingham, N. L. and Johnson, J. E. and Dai, Y. and Schimel, J. P. and Chadwick, O. A.},
  title = {Water balance creates a threshold in soil pH at the global scale},
  journal = {Nature},
  year = {2016},
  volume = {540},
  number = {7634},
  pages = {567-569},
  doi = {10.1038/nature20139},
  note = {access: abstract_only; cited as: C-ANALOG [48] (AB)}
}

@article{kirkChangesSoilPH2009,
  author = {Kirk, Guy J. D. and Bellamy, Pat H. and Lark, R. Murray},
  title = {Changes in soil pH across England and Wales in response to decreased acid deposition},
  journal = {Global Change Biology},
  year = {2010},
  volume = {16},
  number = {11},
  pages = {3111-3119},
  doi = {10.1111/j.1365-2486.2009.02135.x},
  note = {access: abstract_only; online-first 2009 per Crossref (the note's note on dates); cited as: C-ANALOG [49] (AB)}
}

@article{bellamyCarbonLossesAll2005,
  author = {Bellamy, Pat H. and Loveland, Peter J. and Bradley, R. Ian and Lark, R. Murray and Kirk, Guy J. D.},
  title = {Carbon losses from all soils across England and Wales 1978-2003},
  journal = {Nature},
  year = {2005},
  volume = {437},
  number = {7056},
  pages = {245-248},
  doi = {10.1038/nature04038},
  note = {access: abstract_only; cited as: C-ANALOG [50] (AB)}
}

@article{reynoldsCountrysideSurveyNational2013,
  author = {Reynolds, B. and Chamberlain, P. M. and Poskitt, J. and Woods, C. and Scott, W. A. and Rowe, E. C. and Robinson, D. A. and Frogbrook, Z. L. and Keith, A. M. and Henrys, P. A. and Black, H. I. J. and Emmett, B. A.},
  title = {Countryside Survey: National "Soil Change" 1978-2007 for topsoils in Great Britain: acidity, carbon, and total nitrogen status},
  journal = {Vadose Zone Journal},
  year = {2013},
  volume = {12},
  number = {2},
  pages = {1-15},
  doi = {10.2136/vzj2012.0114},
  note = {access: abstract_only; cited as: C-ANALOG [51] (AB)}
}

@article{larkBaselineValuesChange2006,
  author = {Lark, R. M. and Bellamy, P. H. and Kirk, G. J. D.},
  title = {Baseline values and change in the soil, and implications for monitoring},
  journal = {European Journal of Soil Science},
  year = {2006},
  volume = {57},
  number = {6},
  pages = {916-921},
  doi = {10.1111/j.1365-2389.2006.00875.x},
  note = {access: abstract_only; cited as: C-ANALOG [52] (AB)}
}

@article{sabyWillEuropeanSoilmonitoring2008,
  author = {Saby, Nicolas P. A. and Bellamy, Patricia H. and Morvan, Xavier and Arrouays, Dominique and Jones, Robert J. A. and Verheijen, Frank G. A. and Kibblewhite, Mark G. and Verdoodt, Ann and Berényi Üveges, Judit and Freudenschuß, Alexandra and Simota, Catalin},
  title = {Will European soil-monitoring networks be able to detect changes in topsoil organic carbon content?},
  journal = {Global Change Biology},
  year = {2008},
  volume = {14},
  number = {10},
  pages = {2432-2442},
  doi = {10.1111/j.1365-2486.2008.01658.x},
  note = {access: abstract_only (full text not obtained); cited as: C-ANALOG [53] (AB)}
}

@article{grosseLongtermFieldExperiments2020,
  author = {Grosse, Meike and Hierold, Wilfried and Ahlborn, Marlen C. and Piepho, Hans-Peter and Helming, Katharina},
  title = {Long-term field experiments in Germany: classification and spatial representation},
  journal = {SOIL},
  year = {2020},
  volume = {6},
  number = {2},
  pages = {579-596},
  doi = {10.5194/soil-6-579-2020},
  note = {access: full_text (FT-s, read by a search agent); cited as: C-ANALOG [54] (FT-s)}
}

@article{qiGlobalscalePatternsBioavailable2026,
  author = {Qi, Chongchong and Feng, Yuxin and Hu, Tao and Zhang, Ping and Chu, Chu and Chai, Liyuan},
  title = {Global-scale patterns of bioavailable soil phosphorus driven by agricultural fertilization},
  journal = {iScience},
  year = {2026},
  volume = {29},
  number = {7},
  pages = {116624},
  doi = {10.1016/j.isci.2026.116624},
  note = {access: abstract_only; cited as: C-ANALOG [55] (AB)}
}

@article{velozIdentifyingClimaticAnalogs2011,
  author = {Veloz, Samuel and Williams, John W. and Lorenz, David and Notaro, Michael and Vavrus, Steve and Vimont, Daniel J.},
  title = {Identifying climatic analogs for Wisconsin under 21st-century climate-change scenarios},
  journal = {Climatic Change},
  year = {2012},
  volume = {112},
  number = {3-4},
  pages = {1037-1058},
  doi = {10.1007/s10584-011-0261-z},
  note = {access: not_obtained (Springer HTML auth redirect and cookie wall; Unpaywall only a handle; abstract elided by publisher; Europe PMC); cited as: C-ANALOG Sources not obtained, and in the body as Veloz et al. (2012), which may test variable-set sensitivity}
}

@article{ordonezProjectedClimateReshuffling2013,
  author = {Ordonez, Alejandro and Williams, John W.},
  title = {Projected climate reshuffling based on multivariate climate-availability, climate-analog, and climate-velocity analyses: implications for community disaggregation},
  journal = {Climatic Change},
  year = {2013},
  volume = {119},
  number = {3-4},
  pages = {659-675},
  doi = {10.1007/s10584-013-0752-1},
  note = {access: not_obtained (Unpaywall closed; no abstract on Crossref or Semantic Scholar; Europe PMC); not cited; cited as: C-ANALOG Sources not obtained}
}

@article{ordonezMappingClimaticMechanisms2016,
  author = {Ordonez, Alejandro and Williams, John W. and Svenning, Jens-Christian},
  title = {Mapping climatic mechanisms likely to favour the emergence of novel communities},
  journal = {Nature Climate Change},
  year = {2016},
  volume = {6},
  number = {12},
  pages = {1104-1109},
  doi = {10.1038/nclimate3127},
  note = {access: not_obtained (Unpaywall closed; no abstract on Crossref or Semantic Scholar); not cited; cited as: C-ANALOG Sources not obtained}
}

@article{williamsNovelClimatesNoanalog2007,
  author = {Williams, John W. and Jackson, Stephen T.},
  title = {Novel climates, no-analog communities, and ecological surprises},
  journal = {Frontiers in Ecology and the Environment},
  year = {2007},
  volume = {5},
  number = {9},
  pages = {475-482},
  doi = {10.1890/070037},
  note = {access: not_obtained (Wiley pdfdirect 403; no abstract on Crossref); not cited; cited as: C-ANALOG Sources not obtained, and in a critic coverage gap}
}

@article{fitzpatrickProjectionSpeciesDistribution2009,
  author = {Fitzpatrick, Matthew C. and Hargrove, William W.},
  title = {The projection of species distribution models and the problem of non-analog climate},
  journal = {Biodiversity and Conservation},
  year = {2009},
  volume = {18},
  number = {8},
  pages = {2255-2261},
  doi = {10.1007/s10531-009-9584-8},
  note = {access: not_obtained (Unpaywall closed; no abstract on Crossref or Semantic Scholar); not cited; cited as: C-ANALOG Sources not obtained, and in a critic coverage gap}
}

@article{elithArtModellingRangeshifting2010,
  author = {Elith, Jane and Kearney, Michael and Phillips, Steven},
  title = {The art of modelling range-shifting species},
  journal = {Methods in Ecology and Evolution},
  year = {2010},
  volume = {1},
  number = {4},
  pages = {330-342},
  doi = {10.1111/j.2041-210X.2010.00036.x},
  note = {access: not_obtained (Crossref metadata only, no abstract); not cited; cited as: C-ANALOG Sources not obtained, and in a critic coverage gap (MESS)}
}

@incollection{mallavanHomosoilMethodologyQuantitative2010,
  author = {Mallavan, B. P. and Minasny, B. and McBratney, A. B.},
  title = {Homosoil, a methodology for quantitative extrapolation of soil information across the globe},
  booktitle = {Digital Soil Mapping},
  series = {Progress in Soil Science 2},
  publisher = {Springer},
  year = {2010},
  pages = {137-150},
  doi = {10.1007/978-90-481-8863-5_12},
  note = {access: not_obtained (Crossref no abstract; Semantic Scholar abstract elided, closed access); known only via the Nenkam et al. 2022 abstract (secondary); listed twice in Sources not obtained; not cited; cited as: C-ANALOG Sources not obtained}
}

@article{bertrandDisregardingEdaphicDimension2012,
  author = {Bertrand, R. and Perez, V. and Gegout, J.-C.},
  title = {Disregarding the edaphic dimension in species distribution models leads to the omission of crucial spatial information under climate change: the case of Quercus pubescens in France},
  journal = {Global Change Biology},
  year = {2012},
  volume = {18},
  pages = {2648-2660},
  doi = {10.1111/j.1365-2486.2012.02679.x},
  note = {access: not_obtained (Semantic Scholar abstract elided, closed; Crossref title search); not cited; incomplete: number; cited as: C-ANALOG Sources not obtained}
}

@article{vandenhoogenSoilNematodeAbundance2019,
  author = {van den Hoogen, Johan and others},
  title = {Soil nematode abundance and functional group composition at a global scale},
  journal = {Nature},
  year = {2019},
  volume = {572},
  pages = {194-198},
  doi = {10.1038/s41586-019-1418-6},
  note = {access: abstract_only (Europe PMC abstract only, no PMC full text; listed twice in Sources not obtained); not cited (named in the answers' not-measured list and a critic coverage gap); incomplete: authors, number; cited as: C-ANALOG Sources not obtained}
}

@article{blakeChangesSoilChemistry1999,
  author = {Blake, L. and Goulding, K. W. T. and Mott, C. J. B. and Johnston, A. E.},
  title = {Changes in soil chemistry accompanying acidification over more than 100 years under woodland and grass at Rothamsted Experimental Station, UK},
  journal = {European Journal of Soil Science},
  year = {1999},
  volume = {50},
  number = {3},
  pages = {401-412},
  doi = {10.1046/j.1365-2389.1999.00253.x},
  note = {access: not_obtained (Crossref metadata; Unpaywall no OA; no abstract retrieved); not cited; cited as: C-ANALOG Sources not obtained}
}

@article{johnstonSoilAcidificationMore1986,
  author = {Johnston, A. E. and Goulding, K. W. T. and Poulton, P. R.},
  title = {Soil acidification during more than 100 years under permanent grassland and woodland at Rothamsted},
  journal = {Soil Use and Management},
  year = {1986},
  volume = {2},
  number = {1},
  pages = {3-10},
  doi = {10.1111/j.1475-2743.1986.tb00669.x},
  note = {access: not_obtained (Crossref metadata; Unpaywall no OA); not cited; cited as: C-ANALOG Sources not obtained}
}

@misc{donmezClimateChangeImpacts,
  author = {Donmez, Cenk and others},
  title = {Climate change impacts on long-term field experiments in Germany},
  howpublished = {SSRN preprint},
  doi = {10.2139/ssrn.4034620},
  note = {access: abstract_only (the preprint record, the version actually read for reference [19]; critic: C-ANALOG:C-051, C-ANALOG:C-068, cite the version read); incomplete: year, authors beyond the first; cited as: C-ANALOG [19] access note}
}

@article{knappPushingPrecipitationExtremes2017,
  author = {Knapp, A. K. and others},
  title = {Pushing precipitation to the extremes in distributed experiments},
  journal = {Global Change Biology},
  year = {2017},
  note = {access: not stated (named by the critic as a candidate route, not verified); not cited; incomplete: authors, volume, pages, doi; cited as: C-ANALOG critique, coverage gaps}
}

@article{kroeldulay2022,
  author = {Kröel-Dulay, G. and others},
  journal = {Nature Ecology and Evolution},
  year = {2022},
  note = {access: not stated (named by the critic as a candidate route on field experiments against natural drought, not verified); not cited; incomplete: authors, title, volume, pages, doi; cited as: C-ANALOG critique, coverage gaps}
}

@article{lauber2009,
  author = {Lauber, C. L. and others},
  year = {2009},
  note = {access: not stated (known only as Rousk et al. 2010's citation for the 88 American soils pH range; critic: C-ANALOG:C-050); not cited; incomplete: authors, title, journal, volume, pages, doi; cited as: C-ANALOG critique}
}

@article{vanvuurenRepresentativeConcentrationPathways2011,
  author = {van Vuuren, D. and Edmonds, J. and Kainuma, M. and Riahi, K. and Thomson, Allison M. and Hibbard, K. and Hurtt, G. and Kram, T. and Krey, V. and Lamarque, J. and Masui, Toshihiko and Meinshausen, M. and Nakicenovic, N. and Smith, Steven J. and Rose, Steven K.},
  title = {The representative concentration pathways: an overview},
  journal = {Climatic Change},
  year = {2011},
  volume = {109},
  number = {1-2},
  pages = {5-31},
  doi = {10.1007/s10584-011-0148-z},
  note = {background; type: overview; access: abstract checked (Semantic Scholar and OpenAlex)}
}

@article{bloisSpaceCanSubstitute2013,
  author = {Blois, Jessica L. and Williams, John W. and Fitzpatrick, Matthew C. and Jackson, Stephen T. and Ferrier, Simon},
  title = {Space can substitute for time in predicting climate-change effects on biodiversity},
  journal = {Proceedings of the National Academy of Sciences},
  year = {2013},
  volume = {110},
  number = {23},
  pages = {9374-9379},
  doi = {10.1073/pnas.1220228110},
  note = {background; type: peer reviewed; access: abstract checked (Europe PMC, PMID 23690569)}
}
```
