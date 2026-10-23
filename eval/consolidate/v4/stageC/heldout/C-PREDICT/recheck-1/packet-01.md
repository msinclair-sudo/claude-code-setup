## hold-out-design.6 (claim)

Microbial held-out studies mostly used random splits: random, not site-blocked, splits in Liu 2023, Faure 2021 and Frémont 2022, and random splits of whole sites, not spatially blocked, in Mod 2021; Fuhrman et al. 2006 evaluated in-sample; and Werbin's functional-versus-taxonomic contrast is a within-site temporal test.

- conf: not stated
- class: not stated
- holds: microbial held-out prediction studies
- src: liuPredictingMicrobialCommunity2023, faureTowardsOmicsbasedPredictions2021, fremontRestructuringPlanktonGenomic2022, modPredictingSpatialPatterns2021, fuhrmanAnnuallyReoccurringBacterial2006, werbinForecastingSoilMicrobiome2024
- trail: C-PREDICT §Transferability, bounds, §Answers as delivered

From the note:

> C-PREDICT:B-0080 [2. One profile type at held-out units] **Taxonomic profiles.** Mod et al. 2021 [8] (full text via search agents) modelled soil bacterial OTU abundances at 255 Swiss Alpine sites with ten random 80/20 splits of whole sites (random, not spatially blocked).
>
> C-PREDICT:B-0124 [5. Transferability, bounds and failure modes] Microbial held-out studies mostly used random splits [3, 4, 5, 8], and Werbin's functional-versus-taxonomic contrast is a within-site temporal test.
>
> C-PREDICT:A-063 [quote: Answers as delivered] Several microbial held-out studies used random, not site-blocked, splits (Faure 2021; Liu 2023; Frémont 2022) or evaluated in-sample (Fuhrman et al. 2006).
>
> C-PREDICT:R-0113 [References] [8] Mod, Heidi K.; Buri, Aline; Yashiro, Erika; Guex, Nicolas; Malard, Lucie; Pinto-Figueroa, Eric; Pagni, Marco; Niculita-Hirzel, Hélène; van der Meer, Jan Roelof; Guisan, Antoine (2021).
>

## hold-out-design.7 (claim)

The clearest microbial failure bounds found are the one spatial transfer result in Werbin (bacteria losing 65% of CRPS skill at new sites) and the zero median site-scale 1:1 R2 in Averill's cross-study test, where that median is 0 for every group except fungal functional groups, though about 21 of 130 groups have a positive 1:1 R2.

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

## averill.7 (claim)

In the reviewer's recomputation of Averill et al.'s site-scale medians, bacteria peak at order (0.51) with phylum lowest (0.23 to 0.30 depending on how duplicated rows are handled), and fungal medians do not rise cleanly with rank (phylum 0.12, class 0.01, order 0.11, family 0.13, genus 0.08), whereas Averill et al. state fungal predictability rises with taxonomic scale; the authors' claim may rest on a different summary in the unread main text.

- conf: single (note: "Each rank finding is single-study")
- class: not stated
- holds: site scale, best-fit R2
- src: averillSoilMicrobiomePredictability2021 (supplement)
- trail: C-PREDICT §What the direct evidence, §Answers as delivered

From the note:

> C-PREDICT:B-0037 [1. What the direct evidence consists of] | Group (site scale) | n groups | median best-fit R2 | median R2 (1:1) |
>
> C-PREDICT:B-0040 [1. What the direct evidence consists of] | Bacteria order | 10 | 0.51 | 0.00 |
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
> C-PREDICT:B-0053 [1. What the direct evidence consists of] The fungal rank medians do not rise cleanly with rank.
>
> C-PREDICT:A-035 [quote: Answers as delivered] Averill et al. 2021 state fungal predictability rises with taxonomic scale; in the reviewer's recomputation of their site-scale supplementary R2 medians, bacteria peak at order (0.51) with phylum lowest (0.23 to 0.30 depending on how duplicated rows are handled), and fungal medians do not rise cleanly with rank (phylum 0.12, class 0.01, order 0.11, family 0.13, genus 0.08); the authors' claim may rest on a different summary in the unread main text.
>
> C-PREDICT:A-044 [quote: Answers as delivered] Each rank finding is single-study, the microbial studies disagree on shape, rank is confounded with abundance, and the functional-hierarchy side has no held-out evidence at all..
>

## averill.9 (claim)

Individual bacterial functional groups in Averill et al. spanned the full range: Lignolytic 0.96 best-fit against 0 on the 1:1 line; Copiotroph 0.86 against 0; N fixation 0.01 against 0; Chitinolytic 0.33 against 0.26.

- conf: not stated
- class: not stated
- holds: Averill et al.'s bacterial functional groups, cross-study transfer
- src: averillSoilMicrobiomePredictability2021 (supplement)
- trail: C-PREDICT §What the direct evidence

From the note:

> C-PREDICT:B-0051 [1. What the direct evidence consists of] Setting: continental USA soils, cross-study transfer.
>
> C-PREDICT:B-0055 [1. What the direct evidence consists of] Individual bacterial functional groups spanned the full range: Lignolytic 0.96 best-fit against 0 on the 1:1 line; Copiotroph 0.86 against 0; N fixation 0.01 against 0; Chitinolytic 0.33 against 0.26.
>

Not found in the cited text (where to look, not what is wrong): holds: averill

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
> C-PREDICT:R-0119 [References] Existing climate change will lead to pronounced shifts in the diversity of soil prokaryotes.
>
> C-PREDICT:R-0121 [References] Access: full text (methods).
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
> C-PREDICT:R-0135 [References] Agricultural land use induces broader homogenization of soil microbial functional composition than taxonomic composition. bioRxiv preprint. https://doi.org/10.1101/2025.02.17.638669.
>

## explanatory-microbial.13 (claim)

Coles et al. 2017 reproduced ocean gradients regardless of which random species cohort seeded a trait-based model.

- conf: not stated
- class: model (note: "modelled, abstract only")
- holds: ocean biogeochemistry, a trait-based model
- src: colesOceanBiogeochemistryModeled2017 (abstract only)
- trail: C-PREDICT §Explanatory comparisons

From the note:

> C-PREDICT:B-0097 [3. Explanatory comparisons within one dataset] Coles et al. 2017 [23] (modelled, abstract only) reproduced ocean gradients regardless of which random species cohort seeded a trait-based model.
>
> C-PREDICT:R-0174 [References] Ocean biogeochemistry modeled with emergent trait-based genomics.
>

## explanatory-other.3 (claim)

Kruk et al. 2011 found morphology-based phytoplankton groups predicted better from environment than phylogenetic groups (a coarse taxonomic aggregate), in-sample, in one dataset of 211 lakes; the comparison also included Reynolds groups and single species, and the paper's title says composition "can be predicted best in terms of morphological groups".

- conf: not stated
- class: not stated
- holds: 211 lakes, in-sample, one dataset
- src: krukPhytoplanktonCommunityComposition2010 (abstract only)
- trail: C-PREDICT §Explanatory comparisons, §Adversarial critique

From the note:

> C-PREDICT:B-0100 [3. Explanatory comparisons within one dataset] Kruk et al. 2011 [26] found morphology-based phytoplankton groups predicted better from environment than phylogenetic groups in 211 lakes (in-sample).
>
> C-PREDICT:B-0105 [3. Explanatory comparisons within one dataset] All abstract only.
>
> C-PREDICT:C-067 [warning: Adversarial critique, full findings] - Section 3: Kruk et al. 2011 is used as support for 'functional groups more predictable than taxa'. Its comparison is morphology-based groups versus phylogenetic groups and Reynolds groups, in-sample, in one dataset.
>
> C-PREDICT:C-112 [warning: Adversarial critique, full findings] - Kruk 2011 compares morphology-based groups with phylogenetic groups (a coarse taxonomic aggregate) and single species. It is cited as trait versus species composition without keeping the aggregate-taxonomic case apart.
>
> C-PREDICT:R-0188 [References] Phytoplankton community composition can be predicted best in terms of morphological groups.
>

## resolution.4 (claim)

Liu et al. 2023 report 33 to 42% mean skill across taxonomic levels without a clear stated trend.

- conf: single (note: "Each rank finding is single-study")
- class: not stated
- holds: activated sludge
- src: liuPredictingMicrobialCommunity2023 (full text via search agents)
- trail: C-PREDICT §Answers as delivered, §What the direct evidence

From the note:

> C-PREDICT:A-037 [quote: Answers as delivered] Liu et al. 2023 report 33 to 42% mean skill across taxonomic levels without a clear stated trend.
>
> C-PREDICT:A-044 [quote: Answers as delivered] Each rank finding is single-study, the microbial studies disagree on shape, rank is confounded with abundance, and the functional-hierarchy side has no held-out evidence at all..
>
> C-PREDICT:B-0066 [1. What the direct evidence consists of] **Liu et al. 2023** [3] (full text via search agent) trained neural networks on 777 activated-sludge samples from 269 plants in 23 countries to predict ASV relative abundances from operational and environmental variables.
>

## resolution.6 (claim)

Aouabed et al. 2026, missed by the review, say predictability rises with taxonomic scale across several ML models fitted to the Averill and NEON data.

- conf: not stated
- class: not stated
- holds: soil microbes, reanalysis of the Averill and NEON datasets
- src: aouabedSoilMicrobiomePrediction2026 (abstract only)
- trail: C-PREDICT §critic, §Adversarial critique

From the note:

> C-PREDICT:C-019 [danger: Critic: answers partly supported] The review missed two reports.
>
> C-PREDICT:C-020 [danger: Critic: answers partly supported] Aouabed et al. 2026 (abstract only) say predictability rises with taxonomic scale across several ML models fitted to the Averill and NEON data.
>
> C-PREDICT:C-083 [warning: Adversarial critique, full findings] - gap: Aouabed, Therrien, Bouaoune, Bakhtyari, Hijri and Makarenkov (2026), 'Soil microbiome prediction using traditional machine learning and deep learning models', Scientific Reports, doi 10.1038/s41598-026-39537-w.
>
> C-PREDICT:C-085 [warning: Adversarial critique, full findings] It reports predictability rising with taxonomic scale and all models failing for bacterial functional groups on Averill's data.
>

Not found in the cited text (where to look, not what is wrong): holds: datasets

## resolution.8 (claim)

The two missed 2026 reports both lean towards broader ranks predicting better and weaken the review's 'no direction' reading; neither separates rank from abundance.

- conf: not stated
- class: not stated
- holds: soil microbes at NEON
- src: aouabedSoilMicrobiomePrediction2026, anon2026
- trail: C-PREDICT §critic

From the note:

> C-PREDICT:C-019 [danger: Critic: answers partly supported] The review missed two reports.
>
> C-PREDICT:C-020 [danger: Critic: answers partly supported] Aouabed et al. 2026 (abstract only) say predictability rises with taxonomic scale across several ML models fitted to the Averill and NEON data.
>
> C-PREDICT:C-021 [danger: Critic: answers partly supported] A 2026 New Phytologist study predicting soil microbes at NEON from airborne canopy reflectance (abstract only; its predictors are remote sensing, not direct environmental measures) found broad microbial groups predicted best.
>
> C-PREDICT:C-022 [danger: Critic: answers partly supported] Both lean towards broader ranks predicting better and weaken the review's 'no direction' reading.
>
> C-PREDICT:C-023 [danger: Critic: answers partly supported] Neither separates rank from abundance.
>

## resolution.10 (claim)

Nearest precedents for the trait hierarchy: invertebrate trait profiles computed from species, genus or family data are very similar (Gayraud et al. 2003, descriptive), and narrow soil functions are less redundant than broad ones (Chen et al. 2022, explanatory, about redundancy not predictability).

- conf: not stated
- class: not stated
- holds: invertebrates of large European rivers (Gayraud); global soil metagenomes (Chen)
- src: gayraudInvertebrateTraitsBiomonitoring2003 (abstract only), chenLowerFunctionalRedundancy2022 (abstract only)
- trail: C-PREDICT §Answers as delivered, §Adversarial critique

From the note:

> C-PREDICT:A-041 [quote: Answers as delivered] Nearest precedents: plant community-weighted trait means are predicted better than trait diversity indices (Dubuis et al. 2013; Deschamps et al. 2023); invertebrate trait profiles computed from species, genus or family data are very similar (Gayraud et al. 2003, descriptive); narrow soil functions are less redundant than broad ones (Chen et al. 2022, explanatory).
>
> C-PREDICT:C-093 [warning: Adversarial critique, full findings] - gap: Functional-hierarchy resolution: there is no search for studies comparing KO, module, pathway and category (or CAZy family versus class) predictability or environmental fit, even explanatory ones such as metagenome-wide comparisons of KEGG level 1 to 3. Chen et al. 2022 is the only entry and is about redundancy, not predictability.; setting_or_class: Measured metagenomic gene hierarchy levels; direction: D2
>
> C-PREDICT:R-0297 [References] Invertebrate traits for the biomonitoring of large European rivers: an initial assessment of alternative metrics.
>
> C-PREDICT:R-0301 [References] Lower functional redundancy in 'narrow' than 'broad' functions in global soil metagenomics.
>

## resolution.13 (claim)

On rank, the studies conflict: Averill (bacterial peak at order, by the reviewer's reading) against Werbin (bacterial peak at class); the authors' 'fungal predictability increases with taxonomic scale' against non-monotonic supplementary medians; and a microbial broad-rank advantage for fungi against a species-over-family advantage in stream invertebrates (different organisms, different measures).

- conf: cont (note: "Conflicts")
- class: not stated
- holds: soil microbes and stream invertebrates
- src: averillSoilMicrobiomePredictability2021, werbinForecastingSoilMicrobiome2024, hawkinsDEVELOPMENTEVALUATIONPREDICTIVE2000
- trail: C-PREDICT §Answers as delivered, §What the direct evidence

From the note:

> C-PREDICT:A-045 [quote: Answers as delivered] *Conflicts:* Averill (bacterial peak at order by reviewer's reading) versus Werbin (bacterial peak at class); authors' 'fungal predictability increases with taxonomic scale' versus non-monotonic supplementary medians; microbial broad-rank advantage for fungi versus species-over-family advantage in stream invertebrates (different organisms, different measures)..
>
> C-PREDICT:B-0031 [1. What the direct evidence consists of] **Averill et al. 2021** [1] calibrated Bayesian models of soil bacterial (16S) and fungal (ITS) group abundances on global surveys, using climate, soil and vegetation predictors, and validated them on the independent NEON survey across the continental USA at core, plot and site scales.
>
> C-PREDICT:B-0057 [1. What the direct evidence consists of] **Werbin et al. 2024** [2] (Research Square preprint, not peer reviewed; full text via search agents) forecast 170 soil groups (135 taxonomic, phylum to genus; 35 derived functional) at 43 NEON sites with hierarchical Bayesian state-space models.
>

## skill-properties.2 (claim)

A high neutral-model migration rate lowers held-out skill of taxonomic profiles (Liu et al. 2023).

- conf: single (critic: C-066)
- class: not stated
- holds: activated-sludge ASVs
- src: liuPredictingMicrobialCommunity2023 (full text)
- trail: C-PREDICT §Properties that raise, §Answers as delivered, §Adversarial critique

From the note:

> C-PREDICT:B-0132 [6. Properties that raise or lower held-out skill] | Neutral-model migration rate | Taxonomic (ASV) | Higher migration, lower skill | [3] full |
>
> C-PREDICT:A-054 [quote: Answers as delivered] Both: skill measure and baseline can reverse or erase apparent skill; random versus blocked hold-outs inflate skill.**: Properties shown to raise held-out skill of taxonomic profiles: higher relative abundance and occurrence frequency (Mod et al. 2021, soil OTUs; Liu et al. 2023, activated sludge ASVs; Werbin et al. 2024 across all groups); restricting to common taxa in O/E models (Mykrä et al. 2008).
>
> C-PREDICT:A-055 [quote: Answers as delivered] Lowering it: high neutral-model migration rate (Liu et al. 2023); rarity (Mod 2021; Norberg et al. 2019 for plants and animals); few training units, which led to rejection of 11 of 38 metagenomic province niche models (Frémont et al. 2022).
>
> C-PREDICT:C-066 [warning: Adversarial critique, full findings] - D3: 'Neutral-model migration rate lowers skill' (Liu 2023) and 'restricting to common taxa improves O/E error' (Mykrä 2008, abstract only) are each single source.
>

## skill-properties.3 (claim)

Rarity lowers held-out skill (Mod 2021; Norberg et al. 2019 for plants and animals).

- conf: not stated
- class: not stated
- holds: soil OTUs; plants and animals
- src: modPredictingSpatialPatterns2021, norbergComprehensiveEvaluationPredictive2019
- trail: C-PREDICT §Answers as delivered

From the note:

> C-PREDICT:A-052 [quote: Answers as delivered] Taxonomic profiles: abundance and prevalence raise skill; rarity lowers it; migration rate lowers it.
>
> C-PREDICT:A-054 [quote: Answers as delivered] Both: skill measure and baseline can reverse or erase apparent skill; random versus blocked hold-outs inflate skill.**: Properties shown to raise held-out skill of taxonomic profiles: higher relative abundance and occurrence frequency (Mod et al. 2021, soil OTUs; Liu et al. 2023, activated sludge ASVs; Werbin et al. 2024 across all groups); restricting to common taxa in O/E models (Mykrä et al. 2008).
>
> C-PREDICT:A-055 [quote: Answers as delivered] Lowering it: high neutral-model migration rate (Liu et al. 2023); rarity (Mod 2021; Norberg et al. 2019 for plants and animals); few training units, which led to rejection of 11 of 38 metagenomic province niche models (Frémont et al. 2022).
>

## dns.1 (do not say)

"Averill et al.'s own supplement contradicts their conclusion that functional and taxonomic groups were equally predictable."

- why: The authors compared functional groups with high-level taxonomic groups, not with all ranks, and against phyla the result splits by kingdom, so the reviewer's reading departs from the authors for bacteria only.
- instead: averill.2, averill.4
- trail: C-PREDICT §critic, §Answers as delivered, §Adversarial critique

From the note:

> C-PREDICT:A-018 [quote: Answers as delivered] *Conflicts:* Averill authors' 'equally predictable' versus the reviewer's reading of their supplement; Averill (bacterial functional lower than taxa) versus Werbin (functional higher than most taxa) versus Liu (functional similar to or higher than taxa).
>
> C-PREDICT:C-003 [danger: Critic: answers partly supported] Averill et al. 2021 must be stated more exactly.
>
> C-PREDICT:C-006 [danger: Critic: answers partly supported] So the reviewer's reading departs from the authors for bacteria only, not for both kingdoms.
>
> C-PREDICT:C-047 [danger: Critic: answers partly supported] (1) Averill's 'equally predictable' claim is set against all taxonomic ranks, when the authors compared functional groups with high-level taxonomic groups; against phyla the result splits by kingdom.
>
> C-PREDICT:C-096 [warning: Adversarial critique, full findings] - Averill's authors' conclusion is scrutinised by re-analysing the raw supplement, but the reanalysis tests 'equally predictable' against all ranks rather than against the high-level groups the authors named.
>

Not found in the cited text (where to look, not what is wrong): "Averill et al. own supplement contradicts their conclusion that functional and taxonomic groups were equally predictable."

## dns.8 (do not say)

"Across stream macroinvertebrates, fish, macrophytes, diatoms and lake phytoplankton, trait composition is more closely tied to environment than species composition, a moderate and replicated pattern."

- why: The claim merges three measures (closeness of fit to environment, consistency of responses across regions, lower variability), every source behind it was read as abstract only, most come from one macroinvertebrate research network, and it is moderate at best and not replicated across organism groups.
- instead: explanatory-other.11, explanatory-other.1, explanatory-other.4, explanatory-other.7
- trail: C-PREDICT §Answers as delivered, §critic, §Adversarial critique

From the note:

> C-PREDICT:A-013 [quote: Answers as delivered] Explanatory within-dataset comparisons in stream macroinvertebrates, fish, macrophytes, diatoms and lake phytoplankton mostly find trait or functional-group composition more closely tied to environment than species composition (Göthe et al. 2017; Soininen et al. 2016; Kruk et al. 2011), and trait profiles vary less across sites, regions and seasons (Charvet et al. 2000; Bonada et al. 2007; Bêche et al. 2006).
>
> C-PREDICT:C-014 [danger: Critic: answers partly supported] It is moderate at best and should not be called replicated across organism groups.
>
> C-PREDICT:C-050 [danger: Critic: answers partly supported] (4) The explanatory freshwater 'trait advantage' is rated 'moderate and replicated' though every source behind it was read as abstract only and most come from one macroinvertebrate research network.
>
> C-PREDICT:C-108 [warning: Adversarial critique, full findings] - The D1 explanatory paragraph merges three distinct measures into one 'trait composition more closely tied to environment' claim: closeness of fit to environment (Göthe, Soininen, Kruk), consistency of responses across regions (Dolédec 2011, Hoeinghaus 2007, Pont 2006) and lower variability (Charvet, Bonada, Bêche).
>

Not found in the cited text (where to look, not what is wrong): "Across stream macroinvertebrates, fish, macrophytes, diatoms and lake phytoplankton, trait composition is more closely tied to environment than species composition, a moderate and replicated pattern."

## dns.12 (do not say)

"Taxonomic rank shows no consistent direction in how predictable microbial profiles are."

- why: The answer misses a 2026 reanalysis of the same Averill and NEON data (Aouabed et al.) that reports predictability rising with taxonomic scale, a 2026 New Phytologist study in which broad groups were predicted best, and the within-NEON cross-validation figure in Averill's own Extended Data; both missed reports lean towards broader ranks.
- instead: resolution.1, resolution.8
- trail: C-PREDICT §Answers as delivered, §critic

From the note:

> C-PREDICT:A-031 [quote: Answers as delivered] Taxonomic rank: no consistent direction across studies; fungi tend to be more predictable at broad ranks, bacteria peak at intermediate ranks, fine-resolution bacterial OTU clustering made no difference in one study, species beat family in one bioassessment study.
>
> C-PREDICT:C-020 [danger: Critic: answers partly supported] Aouabed et al. 2026 (abstract only) say predictability rises with taxonomic scale across several ML models fitted to the Averill and NEON data.
>
> C-PREDICT:C-021 [danger: Critic: answers partly supported] A 2026 New Phytologist study predicting soil microbes at NEON from airborne canopy reflectance (abstract only; its predictors are remote sensing, not direct environmental measures) found broad microbial groups predicted best.
>
> C-PREDICT:C-022 [danger: Critic: answers partly supported] Both lean towards broader ranks predicting better and weaken the review's 'no direction' reading.
>
> C-PREDICT:C-051 [danger: Critic: answers partly supported] (5) The D2 answer 'no consistent direction' misses a 2026 reanalysis of the same Averill/NEON data (Aouabed et al.) that reports predictability rising with taxonomic scale and bacterial functional groups failing, as well as the within-NEON cross-validation figure in Averill's own Extended Data (Extended Data Fig. 1), which the review says it obtained but does not report.
>

Not found in the cited text (where to look, not what is wrong): "Taxonomic rank shows no consistent direction in how predictable microbial profiles are."

