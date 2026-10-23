## profile-types.1 (claim)

The comparison the research asked for predicts both a taxonomic profile and a gene or trait profile from environment and scores both at units not used in fitting; a measured gene profile is metagenomic genes, pathways or categories, while a derived functional profile is obtained from taxonomy by assigning genera to functions (genus-to-function lookup).

- conf: not stated
- class: not stated
- holds: the review's terms
- src: none (the review's definitions)
- trail: C-PREDICT §What the direct evidence

From the note:

> C-PREDICT:B-0025 [1. What the direct evidence consists of] The brief asks for studies that predict both a taxonomic profile and a gene or trait profile from environment and score both at units not used in fitting.
>
> C-PREDICT:B-0026 [1. What the direct evidence consists of] Across three independent search angles (microbial ecology; species distribution and bioassessment transferability; trait-based community ecology), no study was found that does this with a **measured** gene profile (metagenomic genes, pathways or categories).
>
> C-PREDICT:B-0027 [1. What the direct evidence consists of] Every same-study held-out comparison located uses a functional profile **derived** from taxonomy by assigning genera to functions.
>
> C-PREDICT:A-006 [quote: Answers as delivered] The three same-study held-out comparisons found all use functional profiles derived from taxonomy (genus-to-function lookup): Averill et al. 2021 (cross-study hold-out, independent NEON survey), Werbin et al. 2024 (later-period temporal hold-out at calibration sites, plus 13 held-out sites), and Liu et al. 2023 (random sample hold-out, not blocked by plant).
>

Not found in the cited text (where to look, not what is wrong): holds: review

## hold-out-design.1 (claim)

Hold-out design changes apparent skill: Norberg et al., benchmarking 33 stacked and joint SDMs on five plant and animal datasets, found extrapolation much harder than interpolation, and the prediction task explained 29% of variance in performance, model variant 33% and data properties 38%.

- conf: not stated
- class: not stated
- holds: five plant and animal datasets, 33 stacked and joint species distribution models
- src: norbergComprehensiveEvaluationPredictive2019 (full text via search agents, not re-opened by the synthesis)
- trail: C-PREDICT §Transferability, bounds, §Adversarial critique

From the note:

> C-PREDICT:B-0119 [5. Transferability, bounds and failure modes] Hold-out design changes apparent skill.
>
> C-PREDICT:B-0120 [5. Transferability, bounds and failure modes] Norberg et al. 2019 [44] (full text via search agents), benchmarking 33 stacked and joint SDMs on five plant and animal datasets, found extrapolation much harder than interpolation.
>
> C-PREDICT:B-0121 [5. Transferability, bounds and failure modes] Prediction task explained 29% of variance in performance, model variant 33% and data properties 38%.
>
> C-PREDICT:C-058 [warning: Adversarial critique, full findings] - Werbin et al. 2024 [2], Liu 2023 [3], Hawkins 2010 [38], Norberg 2019 [44], Frémont preprint [5], Fuhrman 2006 [11], Ladau 2018 [9]: 'full text' labels rest on search agents and were not re-opened by the synthesis.
>

## hold-out-design.2 (claim)

Wenger and Olden found machine-learning models with excellent in-sample fit transferred poorly under blocked cross-validation.

- conf: not stated
- class: not stated
- holds: machine-learning ecological models under blocked cross-validation
- src: wengerAssessingTransferabilityEcological2012 (abstract only)
- trail: C-PREDICT §Transferability, bounds

From the note:

> C-PREDICT:B-0122 [5. Transferability, bounds and failure modes] Wenger and Olden 2012 [45] (abstract only) found machine-learning models with excellent in-sample fit transferred poorly under blocked cross-validation.
>
> C-PREDICT:R-0271 [References] Assessing transferability of ecological models: an underappreciated aspect of statistical validation.
>

## hold-out-design.3 (claim)

Random splits overstate transfer relative to blocked or extrapolative splits; in Norberg et al. the prediction task explained 29% of variance in performance.

- conf: repl (note: "replicated in SDM work")
- class: not stated
- holds: the species distribution model literature
- src: wengerAssessingTransferabilityEcological2012, norbergComprehensiveEvaluationPredictive2019
- trail: C-PREDICT §Answers as delivered, §critic
- rating: "Moderate"

From the note:

> C-PREDICT:A-062 [quote: Answers as delivered] Hold-out design: random splits overstate transfer relative to blocked or extrapolative splits (Wenger and Olden 2012; Norberg et al. 2019, where the prediction task explained 29% of variance in performance), and flexible models overfit (Mod 2021: GBM in-sample correlation about 0.97, held-out about 0.21).
>
> C-PREDICT:A-064 [quote: Answers as delivered] *Strength:* Moderate for abundance or prevalence as a driver of taxonomic skill (three microbial studies plus SDM literature) and for random-versus-blocked design effects (replicated in SDM work).
>
> C-PREDICT:C-030 [danger: Critic: answers partly supported] Random splits flatter transfer relative to blocked or extrapolative splits (SDM literature).
>

## hold-out-design.4 (claim)

Maguire et al. 2016 found both species and community models failed across distant, climatically novel periods; its abstract also reports that community-level models generally outperformed SDMs in novel climates (transferring better than species models) and did not overfit.

- conf: not stated
- class: not stated
- holds: distant, climatically novel periods; taxonomic profiles only
- src: maguireControlledComparisonSpecies2016 (abstract only; verified by the critic)
- trail: C-PREDICT §Transferability, bounds, §Adversarial critique

From the note:

> C-PREDICT:B-0123 [5. Transferability, bounds and failure modes] Maguire et al. 2016 [46] found both species and community models failed across distant, climatically novel periods.
>
> C-PREDICT:C-099 [warning: Adversarial critique, full findings] - Maguire et al. 2016 appears in body section 5 only as a failure bound ('both species and community models failed').
>
> C-PREDICT:C-100 [warning: Adversarial critique, full findings] The abstract (verified) also reports that community-level models generally outperformed SDMs in novel climates and did not overfit.
>
> C-PREDICT:C-101 [warning: Adversarial critique, full findings] That finding appears only in the D3 conflicts field, not in the body.
>
> C-PREDICT:A-068 [quote: Answers as delivered] Maguire et al. 2016 found community-level models transferred better than species models across novel climates, while Zurell et al. 2020 found stacking choices mattered more than model type; these concern taxonomic profiles only..
>
> C-PREDICT:R-0277 [References] Access: abstract only.
>

## hold-out-design.5 (claim)

Zurell et al. 2020 found stacking choices mattered more than model type.

- conf: not stated
- class: not stated
- holds: stacking choices; taxonomic profiles only
- src: zurell2020
- trail: C-PREDICT §Answers as delivered

From the note:

> C-PREDICT:A-068 [quote: Answers as delivered] Maguire et al. 2016 found community-level models transferred better than species models across novel climates, while Zurell et al. 2020 found stacking choices mattered more than model type; these concern taxonomic profiles only..
>

## hold-out-design.6 (claim)

Microbial held-out studies mostly used random, not site-blocked, splits (Liu 2023, Faure 2021, Frémont 2022, Mod 2021) or evaluated in-sample (Fuhrman et al. 2006), and Werbin's functional-versus-taxonomic contrast is a within-site temporal test.

- conf: not stated
- class: not stated
- holds: microbial held-out prediction studies
- src: liuPredictingMicrobialCommunity2023, faureTowardsOmicsbasedPredictions2021, fremontRestructuringPlanktonGenomic2022, modPredictingSpatialPatterns2021, fuhrmanAnnuallyReoccurringBacterial2006, werbinForecastingSoilMicrobiome2024
- trail: C-PREDICT §Transferability, bounds, §Answers as delivered

From the note:

> C-PREDICT:B-0124 [5. Transferability, bounds and failure modes] Microbial held-out studies mostly used random splits [3, 4, 5, 8], and Werbin's functional-versus-taxonomic contrast is a within-site temporal test.
>
> C-PREDICT:A-063 [quote: Answers as delivered] Several microbial held-out studies used random, not site-blocked, splits (Faure 2021; Liu 2023; Frémont 2022) or evaluated in-sample (Fuhrman et al. 2006).
>
> C-PREDICT:R-0113 [References] [8] Mod, Heidi K.; Buri, Aline; Yashiro, Erika; Guex, Nicolas; Malard, Lucie; Pinto-Figueroa, Eric; Pagni, Marco; Niculita-Hirzel, Hélène; van der Meer, Jan Roelof; Guisan, Antoine (2021).
>

## hold-out-design.7 (claim)

The clearest microbial failure bounds found are the one spatial transfer result in Werbin (bacteria losing 65% of CRPS skill at new sites) and the zero median 1:1 R2 in Averill's cross-study test, where the median is 0 for every group except fungal functional groups, though about 21 of 130 groups have a positive 1:1 R2.

- conf: not stated
- class: not stated
- holds: soil microbes, NEON; new-site transfer (Werbin) and cross-study transfer (Averill)
- src: werbinForecastingSoilMicrobiome2024, averillSoilMicrobiomePredictability2021
- trail: C-PREDICT §Transferability, bounds, §critic, §Adversarial critique
- limit: access (critic: C-059)

From the note:

> C-PREDICT:B-0031 [1. What the direct evidence consists of] **Averill et al. 2021** [1] calibrated Bayesian models of soil bacterial (16S) and fungal (ITS) group abundances on global surveys, using climate, soil and vegetation predictors, and validated them on the independent NEON survey across the continental USA at core, plot and site scales.
>
> C-PREDICT:B-0057 [1. What the direct evidence consists of] **Werbin et al. 2024** [2] (Research Square preprint, not peer reviewed; full text via search agents) forecast 170 soil groups (135 taxonomic, phylum to genus; 35 derived functional) at 43 NEON sites with hierarchical Bayesian state-space models.
>
> C-PREDICT:B-0125 [5. Transferability, bounds and failure modes] The one spatial transfer result in Werbin (bacteria losing 65% of CRPS skill at new sites) and the near-universal zero 1:1 R2 in Averill's cross-study test are the clearest microbial failure bounds found.
>
> C-PREDICT:C-031 [danger: Critic: answers partly supported] Measure dependence rests on Averill alone: the critic confirmed that median site-scale 1:1 R2 is 0 for every group except fungal functional groups, but about 21 of 130 groups have a positive 1:1 R2 (for example Bacteroidetes 0.50), so 'almost every group had no skill' is a median-level statement.
>
> C-PREDICT:C-059 [warning: Adversarial critique, full findings] Several load-bearing Werbin specifics (fungal functional groups more environment-sensitive, 65% vs 8% CRPS, 'evaluated at 30 sites included within calibration models') are therefore second-hand within the pipeline, and the answers do not flag this.
>

## skill-measures.1 (claim)

Averill et al.'s supplementary table reports two measures of out-of-sample skill: R2 of the best-fit line between predicted and observed, and R2 against the 1:1 line.

- conf: not stated
- class: not stated
- holds: Averill et al. 2021 Supplementary Data 1
- src: averillSoilMicrobiomePredictability2021 (supplement full text)
- trail: C-PREDICT §What the direct evidence

From the note:

> C-PREDICT:B-0034 [1. What the direct evidence consists of] The reviewer re-opened their Supplementary Data 1 (full text) and recomputed medians of out-of-sample R2 at site scale.
>
> C-PREDICT:B-0035 [1. What the direct evidence consists of] The table reports two measures: R2 of the best-fit line between predicted and observed, and R2 against the 1:1 line.
>

Not found in the cited text (where to look, not what is wrong): holds: averill; holds: 2021

## skill-measures.2 (claim)

Skill measure and baseline can reverse or erase apparent skill: under the two measures in Averill et al. the orderings change, with high correlation alongside zero 1:1 skill; in microbes this measure-reversal finding rests on Averill et al. 2021 alone.

- conf: single (note: "Weak (single study) for every property shown on derived functional profiles and for the measure-dependent verdict in microbes")
- class: not stated
- holds: soil microbes, cross-study transfer (Averill)
- src: averillSoilMicrobiomePredictability2021
- trail: C-PREDICT §Answers as delivered, §Properties that raise, §critic
- rating: "Weak (single study)"

From the note:

> C-PREDICT:A-054 [quote: Answers as delivered] Both: skill measure and baseline can reverse or erase apparent skill; random versus blocked hold-outs inflate skill.**: Properties shown to raise held-out skill of taxonomic profiles: higher relative abundance and occurrence frequency (Mod et al. 2021, soil OTUs; Liu et al. 2023, activated sludge ASVs; Werbin et al. 2024 across all groups); restricting to common taxa in O/E models (Mykrä et al. 2008).
>
> C-PREDICT:A-065 [quote: Answers as delivered] Weak (single study) for every property shown on derived functional profiles and for the measure-dependent verdict in microbes.
>
> C-PREDICT:A-072 [quote: Answers as delivered] The measure-reversal finding in microbes rests on Averill et al. 2021 alone; the definition-rule and autocorrelation findings rest on Werbin et al. 2024 alone; the negligible trait gain over a mean baseline rests on Statzner et al. 2005 alone..
>
> C-PREDICT:B-0031 [1. What the direct evidence consists of] **Averill et al. 2021** [1] calibrated Bayesian models of soil bacterial (16S) and fungal (ITS) group abundances on global surveys, using climate, soil and vegetation predictors, and validated them on the independent NEON survey across the continental USA at core, plot and site scales.
>
> C-PREDICT:B-0141 [6. Properties that raise or lower held-out skill] | Skill measure (best-fit versus 1:1 R2) | Both, microbial | High correlation with zero 1:1 skill; changes orderings | [1] supplement full |
>
> C-PREDICT:C-031 [danger: Critic: answers partly supported] Measure dependence rests on Averill alone: the critic confirmed that median site-scale 1:1 R2 is 0 for every group except fungal functional groups, but about 21 of 130 groups have a positive 1:1 R2 (for example Bacteroidetes 0.50), so 'almost every group had no skill' is a median-level statement.
>

Not found in the cited text (where to look, not what is wrong): holds: cross-study

## skill-measures.3 (claim)

No microbial study reported skill over a mean-profile or persistence baseline for both profile types.

- conf: not stated
- class: search (note: "no microbial study reported skill over a mean-profile baseline for both profile types")
- holds: microbial held-out prediction
- src: none (the review's search)
- trail: C-PREDICT §Answers as delivered
- search: not stated

From the note:

> C-PREDICT:A-061 [quote: Answers as delivered] Because trait profiles vary little across reference sites, low raw error and low skill over baseline can coexist; no microbial study reported skill over a mean-profile baseline for both profile types.
>
> C-PREDICT:A-069 [quote: Answers as delivered] *Not measured:* Properties of measured gene profiles (gene length, copy number, annotation completeness, genome-size normalisation, compositional closure) tested against held-out skill; any microbial comparison of both profile types against a mean-profile or persistence baseline; spatially blocked hold-outs in microbial function prediction..
>

## direct-evidence.1 (claim)

No study was found that predicts a measured metagenomic gene or trait profile and a measured taxonomic profile from environment and compares their skill at held-out sites, habitats, studies or times (Case A: no evidence found).

- conf: not stated
- class: search (note: "None of the three found, by these routes")
- holds: three blind search angles (microbial ecology; species distribution and bioassessment transferability; trait-based community ecology); routes that worked: Europe PMC REST, Crossref REST, Unpaywall, publisher, preprint and repository PDFs, Research Square, UNIL repositories, the USGS Pubs Warehouse and the biblion SQL corpus; all three angles reported WebSearch exhausted, a Scholar Gateway identity error, rate-limited Semantic Scholar and OpenAlex and a failed biblion semantic search
- src: none (the review's search)
- trail: C-PREDICT §What the direct evidence, §Search record, §Provenance, §critic
- search: searched, not found (note: "None of the three found, by these routes")

From the note:

> C-PREDICT:A-002 [quote: Answers as delivered] Case A (same-study, measured gene profiles, held-out units): no evidence found.
>
> C-PREDICT:A-005 [quote: Answers as delivered] Case D (explanatory, same-data, microbial and other groups): trait or functional profiles usually track environment more closely, with contrary microbial results.**: No study was found that predicts a measured metagenomic gene or trait profile and a measured taxonomic profile from environment and compares their skill at held-out sites, habitats, studies or times.
>
> C-PREDICT:C-001 [danger: Critic: answers partly supported] - **D1**: The body supports the headline: no same-study held-out comparison of a measured metagenomic gene or pathway profile against a measured taxonomic profile was found by the review's routes.
>
> C-PREDICT:B-0009 [info: Provenance] **Search record:** Synthesis inputs: three blind search angles (microbial; transferability, meaning SDM and bioassessment; traits).
>
> C-PREDICT:B-0010 [info: Provenance] All three reported WebSearch exhausted, a Scholar Gateway identity error, rate-limited Semantic Scholar and OpenAlex, and a failed biblion semantic search.
>
> C-PREDICT:B-0011 [info: Provenance] The working routes were Europe PMC REST, Crossref REST, Unpaywall, publisher, preprint and repository PDFs, the USGS Pubs Warehouse and the biblion SQL corpus.
>
> C-PREDICT:B-0012 [info: Provenance] None of the three found, by these routes, a same-study held-out comparison of measured metagenomic gene profiles against taxonomic profiles, or any held-out comparison across functional hierarchy levels.
>
> C-PREDICT:B-0026 [1. What the direct evidence consists of] Across three independent search angles (microbial ecology; species distribution and bioassessment transferability; trait-based community ecology), no study was found that does this with a **measured** gene profile (metagenomic genes, pathways or categories).
>
> C-PREDICT:B-0144 [Search record] The synthesis draws on three blind search angles: microbial, transferability (SDM and bioassessment) and traits.
>
> C-PREDICT:B-0145 [Search record] All three reported WebSearch exhausted before they started, a Scholar Gateway identity error, rate-limited Semantic Scholar and OpenAlex, and a failed biblion semantic search.
>
> C-PREDICT:B-0146 [Search record] The routes that worked were Europe PMC REST, Crossref REST, Unpaywall, publisher and repository PDFs, Research Square, UNIL repositories, the USGS Pubs Warehouse and a local biblion SQL corpus.
>
> C-PREDICT:B-0147 [Search record] Each agent's query terms are in its own search record.
>
> C-PREDICT:B-0148 [Search record] By these routes, none of the three found a same-study held-out comparison of measured gene profiles against taxonomic profiles, or a held-out comparison across functional hierarchy levels.
>

## direct-evidence.2 (claim)

Not measured: spatially blocked or habitat-held-out comparisons, and any comparison referenced to a null or mean-profile baseline for both profile types in one study.

- conf: not stated
- class: search (note: "Not measured")
- holds: taxonomic versus gene or trait profiles at held-out units
- src: none (the review's search)
- trail: C-PREDICT §Answers as delivered
- search: not stated

From the note:

> C-PREDICT:A-021 [quote: Answers as delivered] *Not measured:* Measured metagenomic gene or pathway profiles versus measured taxonomic profiles at held-out units in any system; spatially blocked or habitat-held-out comparisons; earlier-period (hindcast) and interleaved temporal designs for either comparison; any comparison referenced to a null or mean-profile baseline for both profile types in one study; marine, freshwater, sediment and host-free engineered systems beyond activated sludge; any same-study held-out trait versus taxon comparison in plants or animals located..
>

## direct-evidence.3 (claim)

Not measured: earlier-period (hindcast) and interleaved temporal hold-out designs for either comparison; these designs, and long-term microbial time series predicted out of period, were not searched for either profile type.

- conf: not stated
- class: search (note: "Not measured")
- holds: temporal hold-out designs
- src: none (the review's search)
- trail: C-PREDICT §Answers as delivered, §Adversarial critique
- search: not searched (critic: C-095)

From the note:

> C-PREDICT:A-021 [quote: Answers as delivered] *Not measured:* Measured metagenomic gene or pathway profiles versus measured taxonomic profiles at held-out units in any system; spatially blocked or habitat-held-out comparisons; earlier-period (hindcast) and interleaved temporal designs for either comparison; any comparison referenced to a null or mean-profile baseline for both profile types in one study; marine, freshwater, sediment and host-free engineered systems beyond activated sludge; any same-study held-out trait versus taxon comparison in plants or animals located..
>
> C-PREDICT:C-095 [warning: Adversarial critique, full findings] - gap: Temporal hold-outs in the earlier-period (hindcast) and interleaved designs, and long-term microbial time series (e.g. SPOT, BATS, the Western Channel Observatory beyond Larsen 2012, Helgoland) predicted out of period, are not searched for either profile type.; setting_or_class: Temporal hold-out designs, marine time series; direction: D1, D3
>

## direct-evidence.4 (claim)

Not measured: freshwater, sediment and host-free engineered systems beyond activated sludge; the search record does not name the query routes used for these settings.

- conf: not stated
- class: search (note: "Not measured")
- holds: freshwater, sediment and engineered microbial systems
- src: none (the review's search)
- trail: C-PREDICT §Answers as delivered, §Adversarial critique
- search: not stated (critic: C-092)

From the note:

> C-PREDICT:A-021 [quote: Answers as delivered] *Not measured:* Measured metagenomic gene or pathway profiles versus measured taxonomic profiles at held-out units in any system; spatially blocked or habitat-held-out comparisons; earlier-period (hindcast) and interleaved temporal designs for either comparison; any comparison referenced to a null or mean-profile baseline for both profile types in one study; marine, freshwater, sediment and host-free engineered systems beyond activated sludge; any same-study held-out trait versus taxon comparison in plants or animals located..
>
> C-PREDICT:C-092 [warning: Adversarial critique, full findings] - gap: No freshwater, sediment, groundwater or lake microbial held-out prediction studies for either profile type, and no host-free engineered systems other than activated sludge. The not_measured lists state this, but the Search record does not name the query routes used for these settings.; setting_or_class: Freshwater and sediment microbial communities; direction: D1, D2
>

## direct-evidence.5 (claim)

Not measured: marine systems; marine measured metagenomic and metatranscriptomic prediction beyond Faure 2021 was not searched as held-out prediction of gene profiles.

- conf: not stated
- class: search (note: "Not measured")
- holds: marine microbial measured gene profiles
- src: none (the review's search)
- trail: C-PREDICT §Answers as delivered, §Adversarial critique
- search: not searched (critic: C-091)

From the note:

> C-PREDICT:A-021 [quote: Answers as delivered] *Not measured:* Measured metagenomic gene or pathway profiles versus measured taxonomic profiles at held-out units in any system; spatially blocked or habitat-held-out comparisons; earlier-period (hindcast) and interleaved temporal designs for either comparison; any comparison referenced to a null or mean-profile baseline for both profile types in one study; marine, freshwater, sediment and host-free engineered systems beyond activated sludge; any same-study held-out trait versus taxon comparison in plants or animals located..
>
> C-PREDICT:C-091 [warning: Adversarial critique, full findings] - gap: Marine measured metagenomic and metatranscriptomic prediction beyond Faure 2021 (e.g. Tara Oceans gene-abundance models by depth and temperature, the Salazar et al. 2019 Tara metatranscriptome, BioGEOTRACES gene-based niche models) is not searched as held-out prediction of gene profiles. The microbial measured-gene case rests on one study.; setting_or_class: Marine microbial measured gene profiles, held-out stations or cruises; direction: D1, D3
>

## direct-evidence.6 (claim)

Not measured: any same-study held-out trait versus taxon comparison in plants or animals; the trait-based SDM transferability literature and the fourth-corner and HMSC trait-environment prediction work were not searched.

- conf: not stated
- class: search (note: "Not measured")
- holds: plant and animal community ecology
- src: none (the review's search)
- trail: C-PREDICT §Answers as delivered, §Adversarial critique
- search: not searched (critic: C-089)

From the note:

> C-PREDICT:A-021 [quote: Answers as delivered] *Not measured:* Measured metagenomic gene or pathway profiles versus measured taxonomic profiles at held-out units in any system; spatially blocked or habitat-held-out comparisons; earlier-period (hindcast) and interleaved temporal designs for either comparison; any comparison referenced to a null or mean-profile baseline for both profile types in one study; marine, freshwater, sediment and host-free engineered systems beyond activated sludge; any same-study held-out trait versus taxon comparison in plants or animals located..
>
> C-PREDICT:C-089 [warning: Adversarial critique, full findings] - gap: The trait-based SDM transferability literature (e.g. Vesk et al. 2021, Ecography, on the transferability of trait-based SDMs; Pollock et al. 2012 on trait-based species distribution models) and the fourth-corner / HMSC trait-environment prediction work are not searched. These are the plant and animal counterparts that compare trait-based with taxon-based prediction at held-out units.; setting_or_class: Plant and animal community ecology, trait-based versus taxon-based prediction at held-out sites; direction: D1, D3
>

## averill.1 (claim)

Averill et al. 2021 calibrated Bayesian models of soil bacterial (16S) and fungal (ITS) group abundances on global surveys, using climate, soil and vegetation predictors, and validated them on the independent NEON survey across the continental USA at core, plot and site scales: a cross-study hold-out.

- conf: single (note: "Standing: SINGLE SOURCE")
- class: meas (note: "Evidence class: measured")
- holds: continental USA soils, cross-study transfer
- src: averillSoilMicrobiomePredictability2021 (abstract plus supplementary data table; main text not read)
- trail: C-PREDICT §What the direct evidence, §Answers as delivered

From the note:

> C-PREDICT:B-0031 [1. What the direct evidence consists of] **Averill et al. 2021** [1] calibrated Bayesian models of soil bacterial (16S) and fungal (ITS) group abundances on global surveys, using climate, soil and vegetation predictors, and validated them on the independent NEON survey across the continental USA at core, plot and site scales.
>
> C-PREDICT:B-0032 [1. What the direct evidence consists of] This is a cross-study hold-out.
>
> C-PREDICT:B-0050 [1. What the direct evidence consists of] *Evidence class: measured.
>
> C-PREDICT:B-0051 [1. What the direct evidence consists of] Setting: continental USA soils, cross-study transfer.
>
> C-PREDICT:B-0052 [1. What the direct evidence consists of] Standing: SINGLE SOURCE.* Reviewer's reading, labelled as such: bacterial derived functional groups were the least predictable bacterial category by best-fit R2, fungal functional groups the most predictable fungal category, and under the 1:1 measure almost every group of both types had no skill in cross-study transfer.
>
> C-PREDICT:A-022 [quote: Answers as delivered] *Access:* Averill 2021: abstract plus supplementary data table (full text of supplement, re-opened and recomputed by the reviewer); main text not read.
>

## averill.2 (claim)

Averill et al. conclude that "biogeochemical functional groups and high-level taxonomic groups of microorganisms were equally predictable", that predictability rose with spatial scale, and that fungal predictability rose with taxonomic scale; the equal-predictability claim compares functional groups with high-level taxonomic groups, not with all ranks.

- conf: not stated
- class: not stated
- holds: soil microbes, NEON validation; the authors' abstract (main text paywalled, not read by any agent; quote verified verbatim by the critic)
- src: averillSoilMicrobiomePredictability2021 (abstract only)
- trail: C-PREDICT §What the direct evidence, §critic

From the note:

> C-PREDICT:B-0031 [1. What the direct evidence consists of] **Averill et al. 2021** [1] calibrated Bayesian models of soil bacterial (16S) and fungal (ITS) group abundances on global surveys, using climate, soil and vegetation predictors, and validated them on the independent NEON survey across the continental USA at core, plot and site scales.
>
> C-PREDICT:B-0033 [1. What the direct evidence consists of] The authors conclude that "biogeochemical functional groups and high-level taxonomic groups of microorganisms were equally predictable", that predictability rose with spatial scale, and that fungal predictability rose with taxonomic scale (abstract only; the main text is paywalled and was not read by any agent).
>
> C-PREDICT:A-008 [quote: Answers as delivered] Averill et al. state that functional groups and high-level taxonomic groups were 'equally predictable'.
>
> C-PREDICT:A-035 [quote: Answers as delivered] Averill et al. 2021 state fungal predictability rises with taxonomic scale; in the reviewer's recomputation of their site-scale supplementary R2 medians, bacteria peak at order (0.51) with phylum lowest (0.23 to 0.30 depending on how duplicated rows are handled), and fungal medians do not rise cleanly with rank (phylum 0.12, class 0.01, order 0.11, family 0.13, genus 0.08); the authors' claim may rest on a different summary in the unread main text.
>
> C-PREDICT:C-004 [danger: Critic: answers partly supported] The authors' 'equally predictable' claim (abstract, verified verbatim by the critic) compares functional groups with HIGH-LEVEL taxonomic groups, not with all ranks.
>
> C-PREDICT:C-045 [danger: Critic: answers partly supported] The Averill 'equally predictable' quote is verbatim.
>

## averill.3 (claim)

From Averill et al.'s Supplementary Data 1, median site-scale out-of-sample R2 (best-fit; 1:1) by group: bacteria phylum (10 groups) 0.23 to 0.30; 0.00, class (10) 0.30 to 0.35; 0.00, order (10) 0.51; 0.00, family (10) 0.32; 0.00, genus (10) 0.35; 0.00, bacterial derived functional (13) 0.15; 0.00; fungi phylum (4) 0.12; 0.00, class (9) 0.01; 0.00, order (19) 0.11; 0.00, family (20) 0.13; 0.00, genus (15) 0.08; 0.00, fungal derived functional (5) 0.23; 0.11. The ranges cover both ways of resolving duplicate rows for taxa whose names occur at two ranks; the derived functional medians were unaffected. The critic's recomputation matches (bacterial phylum 0.27, class 0.33, order 0.51, family 0.315, genus 0.355, functional 0.15; fungal functional 0.23 best-fit and 0.11 on the 1:1 line; all other 1:1 medians 0).

- conf: single (note: "Standing: SINGLE SOURCE")
- class: meas (note: "Evidence class: measured")
- holds: continental USA soils, site scale, cross-study transfer; recomputed by the reviewer from the supplement
- src: averillSoilMicrobiomePredictability2021 (supplement full text, re-opened by the reviewer)
- trail: C-PREDICT §What the direct evidence, §Provenance, §critic

From the note:

> C-PREDICT:B-0013 [info: Provenance] The synthesis agent downloaded Averill et al. 2021 Supplementary Data 1 from Springer static content, parsed it with the Python standard library, and recomputed per-group medians of best-fit and 1:1 R2 at site scale.
>
> C-PREDICT:B-0014 [info: Provenance] Duplicate cross-joined rows for names shared across ranks were handled both ways (minimum and maximum), and the medians for derived functional groups were unaffected.
>
> C-PREDICT:B-0034 [1. What the direct evidence consists of] The reviewer re-opened their Supplementary Data 1 (full text) and recomputed medians of out-of-sample R2 at site scale.
>
> C-PREDICT:B-0036 [1. What the direct evidence consists of] Taxa whose names occur at two ranks (for example Actinobacteria) appear in cross-joined duplicate rows, so medians for those ranks shift slightly with how duplicates are resolved; the ranges below cover both choices.
>
> C-PREDICT:B-0037 [1. What the direct evidence consists of] | Group (site scale) | n groups | median best-fit R2 | median R2 (1:1) |
>
> C-PREDICT:B-0038 [1. What the direct evidence consists of] | Bacteria phylum | 10 | 0.23 to 0.30 | 0.00 |
>
> C-PREDICT:B-0039 [1. What the direct evidence consists of] | Bacteria class | 10 | 0.30 to 0.35 | 0.00 |
>
> C-PREDICT:B-0040 [1. What the direct evidence consists of] | Bacteria order | 10 | 0.51 | 0.00 |
>
> C-PREDICT:B-0041 [1. What the direct evidence consists of] | Bacteria family | 10 | 0.32 | 0.00 |
>
> C-PREDICT:B-0042 [1. What the direct evidence consists of] | Bacteria genus | 10 | 0.35 | 0.00 |
>
> C-PREDICT:B-0043 [1. What the direct evidence consists of] | Bacteria functional (derived) | 13 | 0.15 | 0.00 |
>
> C-PREDICT:B-0044 [1. What the direct evidence consists of] | Fungi phylum | 4 | 0.12 | 0.00 |
>
> C-PREDICT:B-0045 [1. What the direct evidence consists of] | Fungi class | 9 | 0.01 | 0.00 |
>
> C-PREDICT:B-0046 [1. What the direct evidence consists of] | Fungi order | 19 | 0.11 | 0.00 |
>
> C-PREDICT:B-0047 [1. What the direct evidence consists of] | Fungi family | 20 | 0.13 | 0.00 |
>
> C-PREDICT:B-0048 [1. What the direct evidence consists of] | Fungi genus | 15 | 0.08 | 0.00 |
>
> C-PREDICT:B-0049 [1. What the direct evidence consists of] | Fungi functional (derived) | 5 | 0.23 | 0.11 |
>
> C-PREDICT:B-0050 [1. What the direct evidence consists of] *Evidence class: measured.
>
> C-PREDICT:B-0051 [1. What the direct evidence consists of] Setting: continental USA soils, cross-study transfer.
>
> C-PREDICT:B-0052 [1. What the direct evidence consists of] Standing: SINGLE SOURCE.* Reviewer's reading, labelled as such: bacterial derived functional groups were the least predictable bacterial category by best-fit R2, fungal functional groups the most predictable fungal category, and under the 1:1 measure almost every group of both types had no skill in cross-study transfer.
>
> C-PREDICT:C-042 [danger: Critic: answers partly supported] I recomputed the Averill supplement medians from Supplementary Data 1 and they match (bacterial phylum 0.27, class 0.33, order 0.51, family 0.315, genus 0.355, functional 0.15; fungal functional 0.23 best-fit and 0.11 on the 1:1 line; all other 1:1 medians 0).
>

## averill.4 (claim)

Against phylum at site scale, Averill et al.'s supplement gives a split by kingdom: bacterial functional median best-fit R2 is 0.15 against 0.27 for phyla, and fungal functional 0.23 against 0.12 for phyla; so the reviewer's reading departs from the authors for bacteria only, not for both kingdoms.

- conf: not stated
- class: not stated
- holds: site scale, recomputed by the critic, matching the review's numbers
- src: averillSoilMicrobiomePredictability2021 (supplement)
- trail: C-PREDICT §critic

From the note:

> C-PREDICT:C-005 [danger: Critic: answers partly supported] Against phylum at site scale, the supplement (recomputed by the critic, matching the review's numbers) gives a split by kingdom: bacterial functional median best-fit R2 is 0.15 against 0.27 for phyla, fungal functional is 0.23 against 0.12 for phyla.
>
> C-PREDICT:C-006 [danger: Critic: answers partly supported] So the reviewer's reading departs from the authors for bacteria only, not for both kingdoms.
>
> C-PREDICT:C-047 [danger: Critic: answers partly supported] (1) Averill's 'equally predictable' claim is set against all taxonomic ranks, when the authors compared functional groups with high-level taxonomic groups; against phyla the result splits by kingdom.
>

## averill.5 (claim)

Reviewer's reading, labelled as such: bacterial derived functional groups were the least predictable bacterial category by best-fit R2 (0.15 against 0.23 to 0.51 for ranks), and fungal functional groups the most predictable fungal category (0.23 against 0.01 to 0.13); this reading sets the functional groups against all taxonomic ranks, not the high-level groups the authors named.

- conf: not stated
- class: reading (note: "Reviewer's reading, labelled as such")
- holds: site scale, best-fit R2
- src: averillSoilMicrobiomePredictability2021 (supplement)
- trail: C-PREDICT §What the direct evidence, §Answers as delivered, §critic

From the note:

> C-PREDICT:B-0052 [1. What the direct evidence consists of] Standing: SINGLE SOURCE.* Reviewer's reading, labelled as such: bacterial derived functional groups were the least predictable bacterial category by best-fit R2, fungal functional groups the most predictable fungal category, and under the 1:1 measure almost every group of both types had no skill in cross-study transfer.
>
> C-PREDICT:A-009 [quote: Answers as delivered] In the reviewer's own computation from their Supplementary Data 1, bacterial derived functional groups had the lowest median site-scale best-fit R2 of any bacterial group (0.15 against 0.23 to 0.51 for ranks), fungal functional groups the highest among fungi (0.23 against 0.01 to 0.13), and median R2 against the 1:1 line was 0 for everything except fungal functional groups (0.11).
>
> C-PREDICT:C-047 [danger: Critic: answers partly supported] (1) Averill's 'equally predictable' claim is set against all taxonomic ranks, when the authors compared functional groups with high-level taxonomic groups; against phyla the result splits by kingdom.
>

## averill.6 (claim)

Under the 1:1 measure in Averill et al.'s cross-study transfer, median site-scale R2 is 0 for every group except fungal functional groups (0.11), but about 21 of 130 groups have a positive 1:1 R2 (for example Bacteroidetes 0.50).

- conf: not stated
- class: not stated
- holds: site scale, R2 against the 1:1 line; confirmed by the critic
- src: averillSoilMicrobiomePredictability2021 (supplement)
- trail: C-PREDICT §Answers as delivered, §critic

From the note:

> C-PREDICT:A-009 [quote: Answers as delivered] In the reviewer's own computation from their Supplementary Data 1, bacterial derived functional groups had the lowest median site-scale best-fit R2 of any bacterial group (0.15 against 0.23 to 0.51 for ranks), fungal functional groups the highest among fungi (0.23 against 0.01 to 0.13), and median R2 against the 1:1 line was 0 for everything except fungal functional groups (0.11).
>
> C-PREDICT:C-031 [danger: Critic: answers partly supported] Measure dependence rests on Averill alone: the critic confirmed that median site-scale 1:1 R2 is 0 for every group except fungal functional groups, but about 21 of 130 groups have a positive 1:1 R2 (for example Bacteroidetes 0.50), so 'almost every group had no skill' is a median-level statement.
>

## averill.7 (claim)

In the reviewer's recomputation of Averill et al.'s site-scale medians, bacteria peak at order (0.51) with phylum lowest (0.23 to 0.30 depending on how duplicated rows are handled), and fungal medians do not rise cleanly with rank (phylum 0.12, class 0.01, order 0.11, family 0.13, genus 0.08).

- conf: single (note: "Each rank finding is single-study")
- class: not stated
- holds: site scale, best-fit R2
- src: averillSoilMicrobiomePredictability2021 (supplement)
- trail: C-PREDICT §What the direct evidence, §Answers as delivered

From the note:

> C-PREDICT:B-0053 [1. What the direct evidence consists of] The fungal rank medians do not rise cleanly with rank.
>
> C-PREDICT:A-035 [quote: Answers as delivered] Averill et al. 2021 state fungal predictability rises with taxonomic scale; in the reviewer's recomputation of their site-scale supplementary R2 medians, bacteria peak at order (0.51) with phylum lowest (0.23 to 0.30 depending on how duplicated rows are handled), and fungal medians do not rise cleanly with rank (phylum 0.12, class 0.01, order 0.11, family 0.13, genus 0.08); the authors' claim may rest on a different summary in the unread main text.
>
> C-PREDICT:A-044 [quote: Answers as delivered] Each rank finding is single-study, the microbial studies disagree on shape, rank is confounded with abundance, and the functional-hierarchy side has no held-out evidence at all..
>

Not found in the cited text (where to look, not what is wrong): holds: best-fit

## averill.8 (claim)

The reviewer's reading of Averill et al.'s supplement sits beside, not in place of, the authors' conclusion of equal predictability and rising fungal predictability with rank, which may rest on a figure-level or model-based summary in the unread main text.

- conf: not stated
- class: not stated
- holds: Averill et al. 2021; main text not read
- src: averillSoilMicrobiomePredictability2021
- trail: C-PREDICT §What the direct evidence

From the note:

> C-PREDICT:B-0054 [1. What the direct evidence consists of] This sits beside, not in place of, the authors' conclusion of equal predictability and rising fungal predictability with rank, which may rest on a figure-level or model-based summary in the unread main text.
>

Not found in the cited text (where to look, not what is wrong): holds: averill; holds: 2021

## averill.9 (claim)

Individual bacterial functional groups in Averill et al. spanned the full range: Lignolytic 0.96 best-fit against 0 on the 1:1 line; Copiotroph 0.86 against 0; N fixation 0.01 against 0; Chitinolytic 0.33 against 0.26.

- conf: not stated
- class: not stated
- holds: Averill et al.'s bacterial functional groups, site scale, cross-study transfer
- src: averillSoilMicrobiomePredictability2021 (supplement)
- trail: C-PREDICT §What the direct evidence

From the note:

> C-PREDICT:B-0051 [1. What the direct evidence consists of] Setting: continental USA soils, cross-study transfer.
>
> C-PREDICT:B-0055 [1. What the direct evidence consists of] Individual bacterial functional groups spanned the full range: Lignolytic 0.96 best-fit against 0 on the 1:1 line; Copiotroph 0.86 against 0; N fixation 0.01 against 0; Chitinolytic 0.33 against 0.26.
>

Not found in the cited text (where to look, not what is wrong): holds: averill; holds: site

## averill.10 (claim)

In Averill et al. many groups with high correlation-type R2 had zero R2 against the 1:1 line in cross-study transfer, the authors link bias partly to compositional data, and the fungal-over-bacterial and functional-versus-taxonomic orderings differ under the two measures.

- conf: not stated
- class: not stated
- holds: soil microbes, cross-study transfer, both profile types
- src: averillSoilMicrobiomePredictability2021 (supplement full text)
- trail: C-PREDICT §Answers as delivered, §Properties that raise

From the note:

> C-PREDICT:A-059 [quote: Answers as delivered] On measures and baselines: in Averill et al. many groups with high correlation-type R2 had zero R2 against the 1:1 line in cross-study transfer (for example Copiotroph 0.86 against 0; Lignolytic 0.96 against 0), and the authors link bias partly to compositional data; the fungal-over-bacterial and functional-versus-taxonomic orderings differ under the two measures.
>
> C-PREDICT:B-0031 [1. What the direct evidence consists of] **Averill et al. 2021** [1] calibrated Bayesian models of soil bacterial (16S) and fungal (ITS) group abundances on global surveys, using climate, soil and vegetation predictors, and validated them on the independent NEON survey across the continental USA at core, plot and site scales.
>
> C-PREDICT:B-0141 [6. Properties that raise or lower held-out skill] | Skill measure (best-fit versus 1:1 R2) | Both, microbial | High correlation with zero 1:1 skill; changes orderings | [1] supplement full |
>

## averill.11 (claim)

A peer reviewer of Averill et al. (review file, full text via a search agent) noted that predictive ability "was still quite low across bacteria and fungi".

- conf: not stated
- class: not stated
- holds: Averill et al. 2021 peer-review file
- src: averillSoilMicrobiomePredictability2021 (peer-review file, full text via search agent)
- trail: C-PREDICT §What the direct evidence

From the note:

> C-PREDICT:B-0056 [1. What the direct evidence consists of] A peer reviewer (review file, full text via search agent) noted that predictive ability "was still quite low across bacteria and fungi".
>

Not found in the cited text (where to look, not what is wrong): holds: averill; holds: 2021

## averill.12 (claim)

Removing Averill et al. 2021 removes the only cross-study held-out comparison and the only evidence that the verdict flips with skill measure.

- conf: not stated
- class: not stated
- holds: the review's D1 single-source sensitivity
- src: averillSoilMicrobiomePredictability2021
- trail: C-PREDICT §Answers as delivered

From the note:

> C-PREDICT:A-026 [quote: Answers as delivered] *Single-source sensitivity:* Yes.
>
> C-PREDICT:A-027 [quote: Answers as delivered] Removing Averill et al. 2021 removes the only cross-study held-out comparison and the only evidence that the verdict flips with skill measure.
>

Not found in the cited text (where to look, not what is wrong): holds: review; holds: d1

## werbin.1 (claim)

Werbin et al. 2024 forecast 170 soil groups (135 taxonomic, phylum to genus; 35 derived functional) at 43 NEON sites with hierarchical Bayesian state-space models; calibration ran from November 2015 to January 2018 at 30 sites, the hold-outs were a later period (February 2018 to January 2020) and 13 new sites, and skill measures were nRMSE, CRPS and forecast R2, with the historical site mean as the null for forecast horizon.

- conf: single (note: "SINGLE SOURCE; preprint")
- class: model/meas (note: "Modelled/measured")
- holds: soil microbes at 43 NEON sites; the design as the review labels it stands (critic)
- src: werbinForecastingSoilMicrobiome2024 (Research Square preprint, not peer reviewed; full text via search agents)
- trail: C-PREDICT §What the direct evidence, §critic

From the note:

> C-PREDICT:B-0057 [1. What the direct evidence consists of] **Werbin et al. 2024** [2] (Research Square preprint, not peer reviewed; full text via search agents) forecast 170 soil groups (135 taxonomic, phylum to genus; 35 derived functional) at 43 NEON sites with hierarchical Bayesian state-space models.
>
> C-PREDICT:B-0058 [1. What the direct evidence consists of] Calibration ran from November 2015 to January 2018 at 30 sites; the hold-outs were a **later** period (February 2018 to January 2020) and 13 new sites.
>
> C-PREDICT:B-0059 [1. What the direct evidence consists of] Skill measures were nRMSE, CRPS and forecast R2, with the historical site mean as the null for forecast horizon.
>
> C-PREDICT:B-0065 [1. What the direct evidence consists of] *Modelled/measured; SINGLE SOURCE; preprint.*
>
> C-PREDICT:C-008 [danger: Critic: answers partly supported] Werbin et al. 2024 (preprint) and Liu et al. 2023 stand as described, with their designs as the review labels them.
>

## werbin.2 (claim)

Werbin et al. report "functional groups of microorganisms ... were more predictable than most taxonomic groups", but that comparison is "evaluated at 30 sites included within calibration models", that is, on later dates at the fitted sites, where temporal autocorrelation contributes.

- conf: single (note: "SINGLE SOURCE; preprint")
- class: not stated
- holds: later dates at the 30 calibration sites; established by one search agent from a figure caption
- src: werbinForecastingSoilMicrobiome2024 (full text via search agents)
- trail: C-PREDICT §What the direct evidence, §Answers as delivered, §Adversarial critique
- limit: access (critic: C-059)

From the note:

> C-PREDICT:B-0060 [1. What the direct evidence consists of] The authors report "functional groups of microorganisms ... were more predictable than most taxonomic groups", but one search agent established from the figure caption that this comparison is "evaluated at 30 sites included within calibration models", that is, on later dates at the fitted sites.
>
> C-PREDICT:B-0065 [1. What the direct evidence consists of] *Modelled/measured; SINGLE SOURCE; preprint.*
>
> C-PREDICT:A-010 [quote: Answers as delivered] Werbin et al. report functional groups more predictable than most taxonomic groups, but that comparison is evaluated at calibration sites on later dates, where temporal autocorrelation contributes, and bacterial functional groups were less sensitive to environment than bacterial taxa.
>
> C-PREDICT:C-059 [warning: Adversarial critique, full findings] Several load-bearing Werbin specifics (fungal functional groups more environment-sensitive, 65% vs 8% CRPS, 'evaluated at 30 sites included within calibration models') are therefore second-hand within the pipeline, and the answers do not flag this.
>

## werbin.3 (claim)

In Werbin et al., new-site transfer is reported for bacteria versus fungi, not split by profile type: bacteria had much lower error than fungi at calibration sites (mean nRMSE 0.68 against 1.94) but transferred far worse to new sites (mean CRPS worse by 65% against 8%).

- conf: single (note: "SINGLE SOURCE; preprint")
- class: not stated
- holds: 13 new NEON sites against the 30 calibration sites
- src: werbinForecastingSoilMicrobiome2024 (full text via search agents)
- trail: C-PREDICT §What the direct evidence, §Adversarial critique
- limit: access (critic: C-059)

From the note:

> C-PREDICT:B-0058 [1. What the direct evidence consists of] Calibration ran from November 2015 to January 2018 at 30 sites; the hold-outs were a **later** period (February 2018 to January 2020) and 13 new sites.
>
> C-PREDICT:B-0061 [1. What the direct evidence consists of] New-site transfer is reported for bacteria versus fungi, not split by profile type.
>
> C-PREDICT:B-0062 [1. What the direct evidence consists of] Bacteria had much lower error than fungi at calibration sites (mean nRMSE 0.68 against 1.94) but transferred far worse to new sites (mean CRPS worse by 65% against 8%).
>
> C-PREDICT:B-0065 [1. What the direct evidence consists of] *Modelled/measured; SINGLE SOURCE; preprint.*
>
> C-PREDICT:C-059 [warning: Adversarial critique, full findings] Several load-bearing Werbin specifics (fungal functional groups more environment-sensitive, 65% vs 8% CRPS, 'evaluated at 30 sites included within calibration models') are therefore second-hand within the pipeline, and the answers do not flag this.
>

Not found in the cited text (where to look, not what is wrong): holds: neon

## werbin.4 (claim)

In Werbin et al. the mechanism differs by kingdom: bacterial functional groups were less sensitive to environmental predictors than bacterial taxa and gained skill through stronger temporal autocorrelation, while fungal functional groups were more environment-sensitive than fungal taxa; whether functional grouping raises skill therefore depends on organism group and mechanism.

- conf: single (note: "SINGLE SOURCE; preprint")
- class: not stated
- holds: soil microbes at NEON
- src: werbinForecastingSoilMicrobiome2024 (full text via search agents)
- trail: C-PREDICT §What the direct evidence, §Answers as delivered, §Adversarial critique
- limit: access (critic: C-059)

From the note:

> C-PREDICT:B-0057 [1. What the direct evidence consists of] **Werbin et al. 2024** [2] (Research Square preprint, not peer reviewed; full text via search agents) forecast 170 soil groups (135 taxonomic, phylum to genus; 35 derived functional) at 43 NEON sites with hierarchical Bayesian state-space models.
>
> C-PREDICT:B-0063 [1. What the direct evidence consists of] The mechanism differs by kingdom: bacterial functional groups were *less* sensitive to environmental predictors than bacterial taxa and gained skill through stronger temporal autocorrelation, while fungal functional groups were more environment-sensitive than fungal taxa.
>
> C-PREDICT:B-0065 [1. What the direct evidence consists of] *Modelled/measured; SINGLE SOURCE; preprint.*
>
> C-PREDICT:A-010 [quote: Answers as delivered] Werbin et al. report functional groups more predictable than most taxonomic groups, but that comparison is evaluated at calibration sites on later dates, where temporal autocorrelation contributes, and bacterial functional groups were less sensitive to environment than bacterial taxa.
>
> C-PREDICT:A-067 [quote: Answers as delivered] *Conflicts:* Whether functional grouping raises skill depends on organism group and mechanism in Werbin (environmental sensitivity for fungi, autocorrelation for bacteria).
>
> C-PREDICT:C-059 [warning: Adversarial critique, full findings] Several load-bearing Werbin specifics (fungal functional groups more environment-sensitive, 65% vs 8% CRPS, 'evaluated at 30 sites included within calibration models') are therefore second-hand within the pipeline, and the answers do not flag this.
>

## werbin.5 (claim)

In Werbin et al., seasonality-only models matched or beat six-predictor environmental models for most groups.

- conf: single (note: "SINGLE SOURCE; preprint")
- class: not stated
- holds: soil microbes at NEON
- src: werbinForecastingSoilMicrobiome2024 (full text via search agents)
- trail: C-PREDICT §What the direct evidence

From the note:

> C-PREDICT:B-0057 [1. What the direct evidence consists of] **Werbin et al. 2024** [2] (Research Square preprint, not peer reviewed; full text via search agents) forecast 170 soil groups (135 taxonomic, phylum to genus; 35 derived functional) at 43 NEON sites with hierarchical Bayesian state-space models.
>
> C-PREDICT:B-0064 [1. What the direct evidence consists of] Seasonality-only models matched or beat six-predictor environmental models for most groups.
>
> C-PREDICT:B-0065 [1. What the direct evidence consists of] *Modelled/measured; SINGLE SOURCE; preprint.*
>

## werbin.6 (claim)

The Werbin et al. abstract reports "91% and 50% accuracy" and "Forecasts perform best for microbes grouped at broad taxonomic ranks or by ecological groups".

- conf: not stated
- class: not stated
- holds: the Werbin et al. 2024 abstract, the only part the critic confirmed
- src: werbinForecastingSoilMicrobiome2024 (abstract, read by the critic)
- trail: C-PREDICT §Adversarial critique

From the note:

> C-PREDICT:C-060 [warning: Adversarial critique, full findings] The critic confirmed only the Werbin abstract: '91% and 50% accuracy' and 'Forecasts perform best for microbes grouped at broad taxonomic ranks or by ecological groups'.
>

Not found in the cited text (where to look, not what is wrong): holds: 2024

## werbin.7 (claim)

Removing Werbin et al. 2024 removes the only temporal (later) hold-out comparison.

- conf: not stated
- class: not stated
- holds: the review's D1 single-source sensitivity
- src: werbinForecastingSoilMicrobiome2024
- trail: C-PREDICT §Answers as delivered

From the note:

> C-PREDICT:A-028 [quote: Answers as delivered] Removing Werbin et al. 2024 removes the only temporal (later) hold-out comparison.
>

Not found in the cited text (where to look, not what is wrong): holds: review; holds: d1; holds: single-source

## liu-sludge.1 (claim)

Liu et al. 2023 trained neural networks on 777 activated-sludge samples from 269 plants in 23 countries to predict ASV relative abundances from operational and environmental variables; mean 1:1 R2 was 35.1% for ASVs present in at least 10% of samples, 33 to 42% across taxonomic levels, and 32.6 to 56.8% (33 to 57% in the answers) for five derived functional groups (nitrifiers, denitrifiers, PAOs, GAOs, filamentous organisms).

- conf: single (note: "Measured; SINGLE SOURCE")
- class: meas (note: "Measured; SINGLE SOURCE")
- holds: activated sludge, 269 plants in 23 countries
- src: liuPredictingMicrobialCommunity2023 (full text via search agent)
- trail: C-PREDICT §What the direct evidence, §Answers as delivered, §critic

From the note:

> C-PREDICT:B-0066 [1. What the direct evidence consists of] **Liu et al. 2023** [3] (full text via search agent) trained neural networks on 777 activated-sludge samples from 269 plants in 23 countries to predict ASV relative abundances from operational and environmental variables.
>
> C-PREDICT:B-0067 [1. What the direct evidence consists of] Mean 1:1 R2 was 35.1% for ASVs present in at least 10% of samples, 33 to 42% across taxonomic levels, and 32.6 to 56.8% for five derived functional groups (nitrifiers, denitrifiers, PAOs, GAOs, filamentous organisms).
>
> C-PREDICT:B-0069 [1. What the direct evidence consists of] *Measured; SINGLE SOURCE.*
>
> C-PREDICT:A-011 [quote: Answers as delivered] Liu et al. give 1:1 R2 of 33 to 57% for derived functional groups against 33 to 42% mean across taxonomic levels.
>
> C-PREDICT:C-008 [danger: Critic: answers partly supported] Werbin et al. 2024 (preprint) and Liu et al. 2023 stand as described, with their designs as the review labels them.
>

## liu-sludge.2 (claim)

Liu et al.'s hold-out was a random 20% of samples, not blocked by plant, so the same plant could appear in training and test sets.

- conf: single (note: "Measured; SINGLE SOURCE")
- class: not stated
- holds: activated sludge; noted by a search agent
- src: liuPredictingMicrobialCommunity2023 (full text via search agent)
- trail: C-PREDICT §What the direct evidence

From the note:

> C-PREDICT:B-0068 [1. What the direct evidence consists of] The hold-out was a random 20% of samples; a search agent notes it was not blocked by plant, so the same plant could appear in training and test sets.
>
> C-PREDICT:B-0069 [1. What the direct evidence consists of] *Measured; SINGLE SOURCE.*
>

Not found in the cited text (where to look, not what is wrong): holds: sludge

## derived-comparison.1 (claim)

The three same-study held-out comparisons found, all microbial, all use functional profiles derived from taxonomy, and their results do not agree: Averill et al. 2021 (cross-study hold-out, independent NEON survey), Werbin et al. 2024 (later-period temporal hold-out at calibration sites, plus 13 held-out sites) and Liu et al. 2023 (random sample hold-out, not blocked by plant). Case B is mixed, dependent on hold-out design and skill measure.

- conf: not stated
- class: not stated
- holds: soil microbes and activated sludge; three single studies, one a non-peer-reviewed preprint, disagreeing among themselves and with the reviewer's reading of the one cross-study test
- src: averillSoilMicrobiomePredictability2021, werbinForecastingSoilMicrobiome2024, liuPredictingMicrobialCommunity2023
- trail: C-PREDICT §What the direct evidence, §Answers as delivered, §critic, §Adversarial critique
- rating: "Weak for held-out comparisons"
- contrary: one-sided (critic: C-098)

From the note:

> C-PREDICT:B-0027 [1. What the direct evidence consists of] Every same-study held-out comparison located uses a functional profile **derived** from taxonomy by assigning genera to functions.
>
> C-PREDICT:B-0030 [1. What the direct evidence consists of] Three such studies exist, all microbial.
>
> C-PREDICT:B-0031 [1. What the direct evidence consists of] **Averill et al. 2021** [1] calibrated Bayesian models of soil bacterial (16S) and fungal (ITS) group abundances on global surveys, using climate, soil and vegetation predictors, and validated them on the independent NEON survey across the continental USA at core, plot and site scales.
>
> C-PREDICT:B-0057 [1. What the direct evidence consists of] **Werbin et al. 2024** [2] (Research Square preprint, not peer reviewed; full text via search agents) forecast 170 soil groups (135 taxonomic, phylum to genus; 35 derived functional) at 43 NEON sites with hierarchical Bayesian state-space models.
>
> C-PREDICT:B-0066 [1. What the direct evidence consists of] **Liu et al. 2023** [3] (full text via search agent) trained neural networks on 777 activated-sludge samples from 269 plants in 23 countries to predict ASV relative abundances from operational and environmental variables.
>
> C-PREDICT:B-0070 [1. What the direct evidence consists of] The three disagree.
>
> C-PREDICT:A-003 [quote: Answers as delivered] Case B (same-study, held-out, functional profile derived from taxonomy): mixed, dependent on hold-out design and skill measure.
>
> C-PREDICT:A-006 [quote: Answers as delivered] The three same-study held-out comparisons found all use functional profiles derived from taxonomy (genus-to-function lookup): Averill et al. 2021 (cross-study hold-out, independent NEON survey), Werbin et al. 2024 (later-period temporal hold-out at calibration sites, plus 13 held-out sites), and Liu et al. 2023 (random sample hold-out, not blocked by plant).
>
> C-PREDICT:A-007 [quote: Answers as delivered] Their results do not agree.
>
> C-PREDICT:A-016 [quote: Answers as delivered] *Strength:* Weak for held-out comparisons: three single studies, all with derived functional profiles, one a non-peer-reviewed preprint, disagreeing among themselves and with the reviewer's reading of the one cross-study test.
>
> C-PREDICT:C-002 [danger: Critic: answers partly supported] The three same-study held-out comparisons all use functional profiles derived from taxonomy, and they disagree.
>
> C-PREDICT:C-096 [warning: Adversarial critique, full findings] - Averill's authors' conclusion is scrutinised by re-analysing the raw supplement, but the reanalysis tests 'equally predictable' against all ranks rather than against the high-level groups the authors named.
>
> C-PREDICT:C-097 [warning: Adversarial critique, full findings] The Werbin authors' claims received no comparable re-analysis of their figures.
>
> C-PREDICT:C-098 [warning: Adversarial critique, full findings] That asymmetry does favour the review's 'no agreement' reading, although the review does flag the Werbin calibration-site caveat.
>
> C-PREDICT:C-098 [warning: Adversarial critique, full findings] That asymmetry does favour the review's 'no agreement' reading, although the review does flag the Werbin calibration-site caveat.
>

## derived-comparison.2 (claim)

Averill's supplement puts bacterial derived function below all bacterial ranks; Werbin puts derived function above most taxa (for a within-site temporal test); Liu puts derived function at or above the taxonomic average (for a random-sample test). The hold-out designs differ in every case (cross-study; later period at the same sites; random samples), so these results cannot be pooled and the disagreement cannot be attributed to any one factor.

- conf: not stated
- class: not stated
- holds: the three derived-profile studies
- src: averillSoilMicrobiomePredictability2021, werbinForecastingSoilMicrobiome2024, liuPredictingMicrobialCommunity2023
- trail: C-PREDICT §What the direct evidence, §Answers as delivered

From the note:

> C-PREDICT:B-0071 [1. What the direct evidence consists of] Averill's supplement puts bacterial derived function below all bacterial ranks; Werbin puts derived function above most taxa (for a within-site temporal test); Liu puts derived function at or above the taxonomic average (for a random-sample test).
>
> C-PREDICT:B-0072 [1. What the direct evidence consists of] The hold-out designs differ in every case (cross-study; later period at the same sites; random samples), so these results cannot be pooled and the disagreement cannot be attributed to any one factor.
>
> C-PREDICT:A-018 [quote: Answers as delivered] *Conflicts:* Averill authors' 'equally predictable' versus the reviewer's reading of their supplement; Averill (bacterial functional lower than taxa) versus Werbin (functional higher than most taxa) versus Liu (functional similar to or higher than taxa).
>

Not found in the cited text (where to look, not what is wrong): holds: derived-profile

## derived-comparison.3 (claim)

A 2026 reanalysis the review missed (Aouabed, Therrien, Bouaoune, Bakhtyari, Hijri and Makarenkov, Scientific Reports) fits several ML models predicting bacterial and fungal composition at functional-group and phylum-to-genus levels from environmental factors on the Averill and NEON datasets; it reports that bacterial functional groups failed under every model on Averill's data and that fungal functional groups reached R2 0.45 on NEON. This is further derived-profile, same-data evidence, and its hold-out design is unverified.

- conf: not stated
- class: not stated
- holds: soil microbes, machine-learning reanalysis of the same continental datasets
- src: aouabedSoilMicrobiomePrediction2026 (abstract only, read by the critic)
- trail: C-PREDICT §critic, §Adversarial critique

From the note:

> C-PREDICT:C-009 [danger: Critic: answers partly supported] A 2026 reanalysis the review missed (Aouabed et al., Scientific Reports, abstract read by the critic only) fits several ML models to the Averill and NEON data.
>
> C-PREDICT:C-010 [danger: Critic: answers partly supported] It reports that bacterial functional groups failed under every model on Averill's data, and that fungal functional groups reached R2 0.45 on NEON.
>
> C-PREDICT:C-011 [danger: Critic: answers partly supported] This is further derived-profile, same-data evidence, and its hold-out design is unverified.
>
> C-PREDICT:C-083 [warning: Adversarial critique, full findings] - gap: Aouabed, Therrien, Bouaoune, Bakhtyari, Hijri and Makarenkov (2026), 'Soil microbiome prediction using traditional machine learning and deep learning models', Scientific Reports, doi 10.1038/s41598-026-39537-w.
>
> C-PREDICT:C-084 [warning: Adversarial critique, full findings] It predicts bacterial and fungal composition at functional-group and phylum-to-genus levels from environmental factors on the Averill and NEON datasets.
>
> C-PREDICT:C-085 [warning: Adversarial critique, full findings] It reports predictability rising with taxonomic scale and all models failing for bacterial functional groups on Averill's data.
>
> C-PREDICT:C-086 [warning: Adversarial critique, full findings] This is a same-study derived-profile comparison bearing on D1 and D2 that the review does not include.; setting_or_class: Soil microbes, derived functional versus taxonomic, machine-learning reanalysis of the same continental datasets; direction: D1, D2
>

## one-profile-studies.1 (claim)

Faure et al. 2021 fitted random forests for 228,914 protein clusters mapped from marine MAGs to 93 Tara Oceans metagenomes using 52 environmental variables: mean test-set R2 was 0.28, 55.9% of models exceeded 0.25 and 6.4% exceeded 0.5, and Longhurst province, a habitat category, was the top predictor in 43% of models.

- conf: not stated
- class: not stated
- holds: marine measured gene content, 93 Tara Oceans metagenomes; numbers matched to the full text by the critic
- src: faureTowardsOmicsbasedPredictions2021 (full text via search agent)
- trail: C-PREDICT §One profile type, §critic

From the note:

> C-PREDICT:B-0073 [2. One profile type at held-out units] **Measured gene content.** Faure et al. 2021 [4] (full text via search agent) fitted random forests for 228,914 protein clusters mapped from marine MAGs to 93 Tara Oceans metagenomes using 52 environmental variables.
>
> C-PREDICT:B-0074 [2. One profile type at held-out units] Mean test-set R2 was 0.28; 55.9% of models exceeded 0.25 and 6.4% exceeded 0.5.
>
> C-PREDICT:B-0075 [2. One profile type at held-out units] Longhurst province, a habitat category, was the top predictor in 43% of models.
>
> C-PREDICT:C-043 [danger: Critic: answers partly supported] Mod 2021 (0.53/0.26; GBM 0.97/0.21; random 80/20 site splits) and Faure 2021 (mean test R2 0.28; 55.9%; 6.4%; Longhurst top predictor in 43.0%; 75% training splits of 93 samples) match the full text.
>

## one-profile-studies.2 (claim)

Faure et al.'s test sets were random 25% splits of samples, not blocked by station or region, with no baseline; it is the only measured-gene held-out study found, and it has no taxonomic comparison.

- conf: not stated
- class: not stated
- holds: 75% training splits of 93 samples
- src: faureTowardsOmicsbasedPredictions2021 (full text via search agent)
- trail: C-PREDICT §One profile type, §critic

From the note:

> C-PREDICT:B-0076 [2. One profile type at held-out units] Test sets were random 25% splits of samples, not blocked by station or region; no baseline.
>
> C-PREDICT:B-0077 [2. One profile type at held-out units] This is the only measured-gene held-out study found, and it has no taxonomic comparison.
>
> C-PREDICT:C-043 [danger: Critic: answers partly supported] Mod 2021 (0.53/0.26; GBM 0.97/0.21; random 80/20 site splits) and Faure 2021 (mean test R2 0.28; 55.9%; 6.4%; Longhurst top predictor in 43.0%; 75% training splits of 93 samples) match the full text.
>

## one-profile-studies.3 (claim)

Frémont et al. 2022 built niche models for metagenomic "genomic provinces", which are neither purely taxonomic nor functional: 27 of 38 provinces passed an AUC threshold under random splits, and the 11 rejected had few stations (few training units).

- conf: not stated
- class: not stated
- holds: surface-ocean plankton genomic provinces, random splits
- src: fremontRestructuringPlanktonGenomic2022 (bioRxiv preprint read by a search agent)
- trail: C-PREDICT §One profile type, §Properties that raise, §Answers as delivered

From the note:

> C-PREDICT:B-0078 [2. One profile type at held-out units] Frémont et al. 2022 [5] (bioRxiv preprint read by a search agent) built niche models for metagenomic "genomic provinces", which are neither purely taxonomic nor functional; 27 of 38 provinces passed an AUC threshold under random splits, and those rejected had few stations.
>
> C-PREDICT:B-0136 [6. Properties that raise or lower held-out skill] | Few training units | Genomic provinces | Model rejection | [5] preprint full |
>
> C-PREDICT:A-055 [quote: Answers as delivered] Lowering it: high neutral-model migration rate (Liu et al. 2023); rarity (Mod 2021; Norberg et al. 2019 for plants and animals); few training units, which led to rejection of 11 of 38 metagenomic province niche models (Frémont et al. 2022).
>
> C-PREDICT:R-0101 [References] Restructuring of plankton genomic biogeography in the surface ocean under climate change.
>

## one-profile-studies.4 (claim)

Single-gene abundance models exist (nifH groups, Tang and Cassar 2019; pmoA and mcrA, Ou et al. 2024), but hold-out skill was not visible in their abstracts.

- conf: not stated
- class: not stated
- holds: nifH in the global ocean; pmoA and mcrA in soil
- src: tangDataDrivenModelingDistribution2019 (abstract only), ouGlobalAtlasMethane2024 (abstract only)
- trail: C-PREDICT §One profile type

From the note:

> C-PREDICT:B-0079 [2. One profile type at held-out units] Single-gene abundance models exist (nifH groups, Tang and Cassar 2019 [6]; pmoA and mcrA, Ou et al. 2024 [7]) but hold-out skill was not visible in their abstracts.
>
> C-PREDICT:R-0105 [References] Data-driven modeling of the distribution of diazotrophs in the global ocean.
>
> C-PREDICT:R-0109 [References] Global atlas of methane metabolism marker genes in soil.
>

## one-profile-studies.5 (claim)

Mod et al. 2021 modelled soil bacterial OTU abundances at 255 Swiss Alpine sites with ten random 80/20 splits of whole sites (random, not spatially blocked); the best model (GAMnb) reached a median correlation of about 0.53 in fitting and about 0.26 at held-out sites.

- conf: not stated
- class: not stated
- holds: 255 Swiss Alpine sites, soil bacterial OTUs; verified by the critic in full text
- src: modPredictingSpatialPatterns2021 (full text via search agents)
- trail: C-PREDICT §One profile type, §critic

From the note:

> C-PREDICT:B-0080 [2. One profile type at held-out units] **Taxonomic profiles.** Mod et al. 2021 [8] (full text via search agents) modelled soil bacterial OTU abundances at 255 Swiss Alpine sites with ten random 80/20 splits of whole sites (random, not spatially blocked).
>
> C-PREDICT:B-0081 [2. One profile type at held-out units] The best model reached a median correlation of about 0.53 in fitting and about 0.26 at held-out sites; more flexible models overfitted (GBM about 0.97 in fitting, about 0.21 held out).
>
> C-PREDICT:C-029 [danger: Critic: answers partly supported] - **D3**: Supported: higher abundance and occurrence frequency go with higher held-out skill for taxonomic profiles in three microbial studies (Mod 2021 verified by the critic in full text: GAMnb median correlation about 0.53 in calibration and 0.26 in prediction, GBM about 0.97 and 0.21).
>
> C-PREDICT:C-043 [danger: Critic: answers partly supported] Mod 2021 (0.53/0.26; GBM 0.97/0.21; random 80/20 site splits) and Faure 2021 (mean test R2 0.28; 55.9%; 6.4%; Longhurst top predictor in 43.0%; 75% training splits of 93 samples) match the full text.
>

## one-profile-studies.6 (claim)

In Mod et al. more flexible models overfitted: GBM correlation about 0.97 in fitting and about 0.21 held out.

- conf: not stated
- class: not stated
- holds: 255 Swiss Alpine sites, soil bacterial OTUs
- src: modPredictingSpatialPatterns2021 (full text via search agents), wengerAssessingTransferabilityEcological2012 (abstract only)
- trail: C-PREDICT §One profile type, §Properties that raise, §Answers as delivered

From the note:

> C-PREDICT:B-0080 [2. One profile type at held-out units] **Taxonomic profiles.** Mod et al. 2021 [8] (full text via search agents) modelled soil bacterial OTU abundances at 255 Swiss Alpine sites with ten random 80/20 splits of whole sites (random, not spatially blocked).
>
> C-PREDICT:B-0081 [2. One profile type at held-out units] The best model reached a median correlation of about 0.53 in fitting and about 0.26 at held-out sites; more flexible models overfitted (GBM about 0.97 in fitting, about 0.21 held out).
>
> C-PREDICT:B-0137 [6. Properties that raise or lower held-out skill] | Model flexibility | Taxonomic (OTU) | Overfitting at held-out sites | [8] full, [45] abstract |
>
> C-PREDICT:A-062 [quote: Answers as delivered] Hold-out design: random splits overstate transfer relative to blocked or extrapolative splits (Wenger and Olden 2012; Norberg et al. 2019, where the prediction task explained 29% of variance in performance), and flexible models overfit (Mod 2021: GBM in-sample correlation about 0.97, held-out about 0.21).
>

## one-profile-studies.7 (claim)

Ladau et al. 2018 used leave-one-out cross-validation for families and OTUs on the Tibetan Plateau, where samples came three per location, so leave-one-sample-out is not whole-site hold-out unless done by location (not verified).

- conf: not stated
- class: not stated
- holds: Tibetan Plateau soil prokaryotes
- src: ladauExistingClimateChange2018 (full text, methods)
- trail: C-PREDICT §One profile type

From the note:

> C-PREDICT:B-0082 [2. One profile type at held-out units] Ladau et al. 2018 [9] used leave-one-out cross-validation for families and OTUs on the Tibetan Plateau, where samples came three per location, so leave-one-sample-out is not whole-site hold-out unless done by location (not verified).
>

Not found in the cited text (where to look, not what is wrong): holds: soil

## one-profile-studies.8 (claim)

Larsen et al. 2012 reported average Bray-Curtis similarity of 89.7 between predicted and observed communities over time at a Channel time series, with no baseline and an unstated temporal design.

- conf: not stated
- class: not stated
- holds: a Channel time series
- src: larsenPredictingBacterialCommunity2012 (abstract only)
- trail: C-PREDICT §One profile type

From the note:

> C-PREDICT:B-0083 [2. One profile type at held-out units] Larsen et al. 2012 [10] (abstract only) reported average Bray-Curtis similarity of 89.7 between predicted and observed communities over time at a Channel time series, with no baseline and an unstated temporal design.
>

## one-profile-studies.9 (claim)

Fuhrman et al. 2006, often cited for predictability, evaluated in-sample: the regression was fitted and assessed on the same 48 monthly samples.

- conf: not stated
- class: not stated
- holds: 48 monthly samples, ocean conditions
- src: fuhrmanAnnuallyReoccurringBacterial2006 (full text via search agents)
- trail: C-PREDICT §One profile type, §Answers as delivered

From the note:

> C-PREDICT:B-0084 [2. One profile type at held-out units] Fuhrman et al. 2006 [11] (full text via search agents), often cited for predictability, evaluated in-sample: the regression was fitted and assessed on the same 48 monthly samples.
>
> C-PREDICT:A-063 [quote: Answers as delivered] Several microbial held-out studies used random, not site-blocked, splits (Faure 2021; Liu 2023; Frémont 2022) or evaluated in-sample (Fuhrman et al. 2006).
>
> C-PREDICT:R-0127 [References] Annually reoccurring bacterial communities are predictable from ocean conditions.
>

## one-profile-studies.10 (claim)

One-profile-only held-out studies (Faure et al. 2021 measured gene clusters, mean test R2 0.28; Mod et al. 2021 bacterial OTUs, median held-out correlation 0.26) use different measures and cannot be set against each other: comparisons assembled across studies (Case C) are not commensurable.

- conf: not stated
- class: not stated
- holds: held-out studies of one profile type
- src: faureTowardsOmicsbasedPredictions2021, modPredictingSpatialPatterns2021
- trail: C-PREDICT §Answers as delivered

From the note:

> C-PREDICT:A-004 [quote: Answers as delivered] Case C (assembled across studies): not commensurable.
>
> C-PREDICT:A-012 [quote: Answers as delivered] One-profile-only held-out studies (Faure et al. 2021 measured gene clusters, mean test R2 0.28; Mod et al. 2021 bacterial OTUs, median held-out correlation 0.26) use different measures and cannot be set against each other.
>

## explanatory-microbial.1 (claim)

Explanatory comparisons within one dataset do not measure held-out skill; they bear on how much environment accounts for each profile type.

- conf: not stated
- class: not stated
- holds: within-dataset comparisons
- src: none (the reviewer's framing)
- trail: C-PREDICT §Explanatory comparisons

From the note:

> C-PREDICT:B-0085 [3. Explanatory comparisons within one dataset] These do not measure held-out skill.
>
> C-PREDICT:B-0086 [3. Explanatory comparisons within one dataset] They bear on how much environment accounts for each profile type.
>

Not found in the cited text (where to look, not what is wrong): holds: within-dataset

## explanatory-microbial.2 (claim)

Louca et al. 2016 found environment strongly structured the distribution of FAPROTAX functional groups in the global ocean but only weakly structured taxonomy within groups.

- conf: not stated
- class: not stated
- holds: global ocean, derived function
- src: loucaDecouplingFunctionTaxonomy2016 (abstract only)
- trail: C-PREDICT §Explanatory comparisons

From the note:

> C-PREDICT:B-0087 [3. Explanatory comparisons within one dataset] *Microbial, derived function.* Louca et al. 2016 [12] (abstract only) found environment strongly structured the distribution of FAPROTAX functional groups in the global ocean but only weakly structured taxonomy within groups.
>

## explanatory-microbial.3 (claim)

Ohigashi et al. 2025 found predicted functional composition homogenised over broader scales than taxonomy in farmland.

- conf: not stated
- class: not stated
- holds: farmland soils, derived function
- src: ohigashiAgriculturalLandUse2025 (preprint, abstract only)
- trail: C-PREDICT §Explanatory comparisons

From the note:

> C-PREDICT:B-0088 [3. Explanatory comparisons within one dataset] Ohigashi et al. 2025 [13] (preprint, abstract only) found predicted functional composition homogenised over broader scales than taxonomy in farmland.
>

Not found in the cited text (where to look, not what is wrong): holds: soils

## explanatory-microbial.4 (claim)

Nelson et al. 2016 found habitat and soil C and N largely explained soil N-pathway frequency, but could not identify drivers of taxonomy within N groups.

- conf: not stated
- class: not stated
- holds: soils, measured genes
- src: nelsonGlobalBiogeographyMicrobial2016 (abstract only)
- trail: C-PREDICT §Explanatory comparisons

From the note:

> C-PREDICT:B-0089 [3. Explanatory comparisons within one dataset] *Microbial, measured genes.* Nelson et al. 2016 [14] (abstract only) found habitat and soil C and N largely explained soil N-pathway frequency, but could not identify drivers of taxonomy within N groups.
>

## explanatory-microbial.5 (claim)

Bahram et al. 2018 found gene composition varied more with environment than with distance.

- conf: not stated
- class: not stated
- holds: measured genes
- src: bahramStructureFunctionGlobal2018
- trail: C-PREDICT §Explanatory comparisons

From the note:

> C-PREDICT:B-0089 [3. Explanatory comparisons within one dataset] *Microbial, measured genes.* Nelson et al. 2016 [14] (abstract only) found habitat and soil C and N largely explained soil N-pathway frequency, but could not identify drivers of taxonomy within N groups.
>
> C-PREDICT:B-0090 [3. Explanatory comparisons within one dataset] Bahram et al. 2018 [15] found gene composition varied more with environment than with distance.
>

## explanatory-microbial.6 (claim)

Fierer et al. 2012 found functional beta diversity strongly correlated with taxonomic beta diversity.

- conf: not stated
- class: not stated
- holds: 16 soils, measured genes
- src: fiererCrossbiomeMetagenomicAnalyses2012 (abstract only)
- trail: C-PREDICT §Explanatory comparisons

From the note:

> C-PREDICT:B-0089 [3. Explanatory comparisons within one dataset] *Microbial, measured genes.* Nelson et al. 2016 [14] (abstract only) found habitat and soil C and N largely explained soil N-pathway frequency, but could not identify drivers of taxonomy within N groups.
>
> C-PREDICT:B-0091 [3. Explanatory comparisons within one dataset] Fierer et al. 2012 [16] (abstract only, 16 soils) found functional beta diversity strongly correlated with taxonomic beta diversity.
>

## explanatory-microbial.7 (claim)

Galand et al. 2018 found that at a Mediterranean coastal site taxonomic shifts altered function, and that this link appeared only when all reads were used rather than annotated genes: annotation coverage changes the apparent coupling of function to taxonomy.

- conf: not stated
- class: not stated
- holds: a Mediterranean coastal site, measured genes, explanatory
- src: galandStrongLinkMarine2018 (abstract only)
- trail: C-PREDICT §Explanatory comparisons, §Properties that raise, §Answers as delivered

From the note:

> C-PREDICT:B-0092 [3. Explanatory comparisons within one dataset] Galand et al. 2018 [17] (abstract only) found that at a Mediterranean coastal site taxonomic shifts altered function, and that this link appeared only when all reads were used rather than annotated genes.
>
> C-PREDICT:B-0140 [6. Properties that raise or lower held-out skill] | Annotation coverage (all reads versus annotated genes) | Measured functional, explanatory | Changes apparent coupling to taxonomy | [17] abstract |
>
> C-PREDICT:A-058 [quote: Answers as delivered] Measured-versus-derived: 16S-derived function matched enzyme patterns qualitatively, not quantitatively (Breitkreuz et al. 2021); explanatory coupling of taxonomy and function appeared only when all reads rather than annotated genes were used (Galand et al. 2018).
>

## explanatory-microbial.8 (claim)

Liu et al. 2021 found function stable while taxonomy tracked temperature and nitrate upstream in a river, but both changed together under strong anthropogenic pressure downstream.

- conf: not stated
- class: not stated
- holds: a river, upstream and downstream; measured genes
- src: liuAnthropogenicActivitiesChange2021 (abstract only)
- trail: C-PREDICT §Explanatory comparisons

From the note:

> C-PREDICT:B-0089 [3. Explanatory comparisons within one dataset] *Microbial, measured genes.* Nelson et al. 2016 [14] (abstract only) found habitat and soil C and N largely explained soil N-pathway frequency, but could not identify drivers of taxonomy within N groups.
>
> C-PREDICT:B-0093 [3. Explanatory comparisons within one dataset] Liu et al. 2021 [18] (abstract only) found function stable while taxonomy tracked temperature and nitrate upstream in a river, but both changed together under strong anthropogenic pressure downstream.
>

## explanatory-microbial.9 (claim)

Liang et al. 2024 found 16S and qPCR N-gene dissimilarity responded to different predictors on the Tibetan Plateau.

- conf: not stated
- class: not stated
- holds: Tibetan Plateau soils
- src: qingqingTaxonomicFunctionalBiogeography2024 (preprint, abstract only)
- trail: C-PREDICT §Explanatory comparisons

From the note:

> C-PREDICT:B-0094 [3. Explanatory comparisons within one dataset] Liang et al. 2024 [19] (preprint, abstract only) found 16S and qPCR N-gene dissimilarity responded to different predictors on the Tibetan Plateau.
>
> C-PREDICT:R-0158 [References] Taxonomic and functional biogeography of soil bacteria: importance of environmental filtering and dispersal depends on scale.
>

