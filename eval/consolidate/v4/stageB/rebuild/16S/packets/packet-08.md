## differential-abundance.12 (claim)

In implanted-signal benchmarks, only linear models, Wilcoxon, t-test, limma and fastANCOM controlled FDR at relatively high sensitivity; fitZig reached an observed FDR of 80%, and ANCOM and ANCOM-BC controlled FDR only at 200 or more samples per group.

- conf: repl (marker)
- class: model (marker)
- holds: implanted-signal benchmarks
- src: wirbelRealisticBenchmarkDifferential2024 (FT; model; repl)
- trail: MB-01 §5.4, §answers, §7. Bounds

From the note:

> MB-01:I-0132 [5.4 Tests of which taxa differ in abundance] **Implanted-signal benchmarks.** Only linear models, Wilcoxon, t-test, limma and fastANCOM controlled FDR at relatively high sensitivity. fitZig reached an observed FDR of 80%, and ANCOM and ANCOM-BC controlled FDR only at 200 or more samples per group (Wirbel 2024) [FT; model; repl].
>
> MB-01:A-260 [quote: Answers as delivered] ANCOM-BC showed type I inflation in some settings (Yang and Chen 2022) and controlled FDR only at 200 or more samples per group (Wirbel 2024).
>
> MB-01:A-263 [quote: Answers as delivered] Elementary tests on relative abundances (Wilcoxon, linear models) were among the most replicable (Pelto 2025, abstract) and controlled FDR in an implanted-signal benchmark (Wirbel 2024).
>
> MB-01:B-0364 [7. Bounds and negative results] - ANCOM-BC at small sample sizes (Wirbel 2024);
>
> MB-01:B-0365 [7. Bounds and negative results] - fitZig (Wirbel 2024).
>

## differential-abundance.13 (claim)

Elementary methods on relative abundances (Wilcoxon, linear models) were the most replicable across 53 studies.

- conf: single (marker)
- class: meas (marker)
- holds: 53 studies; an abstract
- src: peltoElementaryMethodsProvide2025 (AB; meas; single)
- trail: MB-01 §5.4, §answers

From the note:

> MB-01:I-0133 [5.4 Tests of which taxa differ in abundance] Elementary methods on relative abundances were the most replicable across 53 studies (Pelto 2025) [AB; meas; single].
>
> MB-01:A-263 [quote: Answers as delivered] Elementary tests on relative abundances (Wilcoxon, linear models) were among the most replicable (Pelto 2025, abstract) and controlled FDR in an implanted-signal benchmark (Wirbel 2024).
>

## differential-abundance.14 (claim)

Makers claim FDR control for ANCOM-BC and ANCOM, and independent benchmarks disagree in part.

- conf: not stated
- class: not stated
- holds: makers' claims against independent benchmarks
- src: linAnalysisCompositionsMicrobiomes2020 (AB; makers' claims), mandalAnalysisCompositionMicrobiomes2015 (AB; makers' claims), yangComprehensiveEvaluationMicrobial2022, wirbelRealisticBenchmarkDifferential2024
- trail: MB-01 §5.4, §answers

From the note:

> MB-01:B-0305 [5.4 Tests of which taxa differ in abundance] **Compositional methods.** Makers claim FDR control for ANCOM-BC and ANCOM (Lin and Peddada 2020; Mandal 2015) [AB; makers' claims].
>
> MB-01:B-0306 [5.4 Tests of which taxa differ in abundance] Independent benchmarks disagree in part (above).
>
> MB-01:A-283 [quote: Answers as delivered] ANCOM-BC: maker claims versus Yang and Chen 2022 and Wirbel 2024. qPCR versus flow cytometry: Jian 2020 versus Galazzo 2020.
>

## differential-abundance.15 (claim)

Reference frames make differential rankings invariant to load.

- conf: single (marker)
- class: meas (marker)
- holds: an abstract
- src: mortonEstablishingMicrobialComposition2019 (AB; meas; single)
- trail: MB-01 §5.4, §answers

From the note:

> MB-01:I-0134 [5.4 Tests of which taxa differ in abundance] Reference frames make differential rankings invariant to load (Morton 2019) [AB; meas; single].
>
> MB-01:A-261 [quote: Answers as delivered] Reference frames make differential rankings invariant to load (Morton 2019, abstract).
>

## differential-abundance.16 (claim)

Fold changes in taxon ratios are invariant to multiplicative bias; fold changes in proportions are not and can change sign; this bias-invariance of ratio-based methods rests on one source.

- conf: not stated
- class: not stated
- holds: McLaren et al.'s model
- src: mclarenConsistentCorrectableBias2019
- trail: MB-01 §5.4, §answers

From the note:

> MB-01:B-0309 [5.4 Tests of which taxa differ in abundance] **Taxonomic bias.** Fold changes in taxon ratios are invariant to multiplicative bias; fold changes in proportions are not and can change sign (McLaren 2019).
>
> MB-01:A-262 [quote: Answers as delivered] Ratio-based analyses are invariant to multiplicative bias, whereas proportion-based ones are biased when community mean efficiency tracks the condition (McLaren 2019; McLaren 2022 preprint).
>
> MB-01:A-293 [quote: Answers as delivered] The bias-invariance of ratio-based methods rests on McLaren 2019.
>

Not found in the cited text (where to look, not what is wrong): holds: model

## differential-abundance.17 (claim)

Proportion-based differential-abundance results err when the community's mean efficiency is associated with the condition.

- conf: single (marker)
- class: model (marker)
- holds: a preprint abstract
- src: mclarenImplicationsTaxonomicBias2022 (AB; PREPRINT; model; single)
- trail: MB-01 §5.4, §answers

From the note:

> MB-01:I-0135 [5.4 Tests of which taxa differ in abundance] Proportion-based differential-abundance results err when the community's mean efficiency is associated with the condition (McLaren 2022) [AB; PREPRINT; model; single].
>
> MB-01:A-262 [quote: Answers as delivered] Ratio-based analyses are invariant to multiplicative bias, whereas proportion-based ones are biased when community mean efficiency tracks the condition (McLaren 2019; McLaren 2022 preprint).
>

## differential-abundance.18 (claim)

Differential-abundance results show large disagreement between methods and frequent FDR failures, robustly; which method is best is contested.

- conf: cont (note: "Which method is best is contested")
- class: not stated
- holds: benchmarks on real and simulated data
- src: nearingMicrobiomeDifferentialAbundance2022, hawinkelBrokenPromiseMicrobiome2019, yangComprehensiveEvaluationMicrobial2022, wirbelRealisticBenchmarkDifferential2024
- trail: MB-01 §answers, §8. Answers, §critic

From the note:

> MB-01:A-277 [quote: Answers as delivered] Differential abundance: robust in showing large disagreement between methods and frequent FDR failures (Nearing 2022; Hawinkel 2019; Yang and Chen 2022; Wirbel 2024).
>
> MB-01:A-278 [quote: Answers as delivered] Which method is best is contested.
>
> MB-01:A-311 [8. Answers in brief] Differential-abundance methods disagree widely, and FDR failures are common.
>
> MB-01:C-041 [danger: Critic: answers partly supported] - **D5: comparing samples with unequal depth or load**: The body supports 'contested' for rarefying, proportions and differential-abundance methods.
>

Not found in the cited text (where to look, not what is wrong): holds: simulated

## differential-abundance.19 (claim)

In the review's summary, proportions are simple, and elementary tests on proportions were replicable and FDR-controlling in some benchmarks, but showed severe type I error with large depth differences, depth-sensitive beta diversity, and proportion error that varies with sample composition.

- conf: not stated
- class: not stated
- holds: the review's summary by approach; differential abundance and beta diversity
- src: peltoElementaryMethodsProvide2025, wirbelRealisticBenchmarkDifferential2024, yangComprehensiveEvaluationMicrobial2022, schlossRarefactionCurrentlyBest2024, mclarenConsistentCorrectableBias2019
- trail: MB-01 §5.6, §Adversarial

From the note:

> MB-01:B-0320 [5.6 Summary by approach] | Approach | Shown to correct | Not shown to correct, or shown to fail | Measure (alpha / beta / DA) |
>
> MB-01:B-0324 [5.6 Summary by approach] | Proportions | Simple; elementary tests on proportions replicable and FDR-controlling in some benchmarks | Severe type I error with large depth differences (Yang and Chen 2022); depth-sensitive beta (Schloss 2024b); proportion error varies with sample composition (McLaren 2019) | DA; beta |
>
> MB-01:C-143 [warning: Adversarial critique, full findings] - Section 5.6 summary table: 'Shown to correct' cells mix makers' claims and simulation results with measured results without per-cell evidence class, so it reads closer to a method recommendation than the brief allows.
>

Not found in the cited text (where to look, not what is wrong): holds: review

## absolute-quantification.1 (claim)

Load measurements (qPCR, flow cytometry, dPCR and spike-ins) change, and can reverse, conclusions drawn from relative data; this is replicated.

- conf: repl (note: "replicated that it changes conclusions")
- class: not stated
- holds: the four studies named
- src: vandeputteQuantitativeMicrobiomeProfiling2017, propsAbsoluteQuantificationMicrobial2016, barlowQuantitativeSequencingFramework2020, tkaczAbsoluteQuantitationMicrobiota2018
- trail: MB-01 §5.5, §answers, §critic

From the note:

> MB-01:B-0310 [5.5 Absolute quantification of total load] **What it corrects.** Load measurements change conclusions drawn from relative data.
>
> MB-01:A-266 [quote: Answers as delivered] Absolute quantification for differences in load. qPCR, flow cytometry, dPCR and spike-ins can reverse relative-abundance conclusions (Vandeputte 2017; Props 2017; Barlow 2020; Tkacz 2018).
>
> MB-01:A-279 [quote: Answers as delivered] Absolute quantification: replicated that it changes conclusions; weak on the agreement between quantification methods.
>
> MB-01:C-042 [danger: Critic: answers partly supported] It supports that absolute quantification changes conclusions but does not remove taxon-specific bias.
>

## absolute-quantification.2 (claim)

Flow-cytometry quantitative profiling showed the Bacteroides-Prevotella trade-off in relative data to be an artefact, and load drove Crohn's-associated differences.

- conf: not stated
- class: not stated
- holds: an abstract
- src: vandeputteQuantitativeMicrobiomeProfiling2017 (AB)
- trail: MB-01 §5.5

From the note:

> MB-01:B-0311 [5.5 Absolute quantification of total load] - Flow-cytometry quantitative profiling showed the Bacteroides-Prevotella trade-off in relative data to be an artefact, and load drove Crohn's-associated differences (Vandeputte 2017) [AB].
>

## absolute-quantification.3 (claim)

In engineered freshwater, relative enrichment did not imply absolute outgrowth.

- conf: not stated
- class: not stated
- holds: engineered freshwater; an abstract
- src: propsAbsoluteQuantificationMicrobial2016 (AB; engineered freshwater)
- trail: MB-01 §5.5

From the note:

> MB-01:B-0312 [5.5 Absolute quantification of total load] - Relative enrichment did not imply absolute outgrowth (Props 2017) [AB; engineered freshwater].
>

## absolute-quantification.4 (claim)

In soil, absolute abundance could hold steady or rise while relative abundance fell.

- conf: not stated
- class: not stated
- holds: soil
- src: tkaczAbsoluteQuantitationMicrobiota2018 (FT; soil)
- trail: MB-01 §5.5

From the note:

> MB-01:B-0313 [5.5 Absolute quantification of total load] - Absolute abundance could hold steady or rise while relative abundance fell (Tkacz 2018) [FT; soil].
>

## absolute-quantification.5 (claim)

Spike-in bacteria added before extraction recovered ratios of absolute abundances across mouse faecal dilutions, but the three spike-in species gave different read yields.

- conf: repl (marker)
- class: meas (marker)
- holds: mouse faecal dilutions
- src: stammlerAdjustingMicrobiomeProfiles2016 (FT; meas; repl)
- trail: MB-01 §5.5

From the note:

> MB-01:I-0136 [5.5 Absolute quantification of total load] - Spike-in bacteria added before extraction recovered ratios of absolute abundances across mouse faecal dilutions (Stammler 2016) [FT; meas; repl].
>
> MB-01:B-0314 [5.5 Absolute quantification of total load] The three spike-in species gave different read yields.
>

## absolute-quantification.6 (claim)

dPCR anchoring gave about 2x extraction accuracy above 8.3 x 10^4 input copies, and absolute but not relative analysis revealed diet effects.

- conf: single (marker)
- class: meas (marker)
- holds: one study
- src: barlowQuantitativeSequencingFramework2020 (FT; meas; single)
- trail: MB-01 §5.5

From the note:

> MB-01:I-0137 [5.5 Absolute quantification of total load] - dPCR anchoring gave about 2x extraction accuracy above 8.3 x 10^4 input copies, and absolute but not relative analysis revealed diet effects (Barlow 2020) [FT; meas; single].
>

## absolute-quantification.7 (claim)

Soil internal standards tracked PLFA and respiration biomass better than those two measures tracked each other.

- conf: single (marker)
- class: meas (marker)
- holds: soil; an abstract
- src: smetsMethodSimultaneousMeasurement2016 (AB; meas; single)
- trail: MB-01 §5.5

From the note:

> MB-01:I-0138 [5.5 Absolute quantification of total load] - Soil internal standards tracked PLFA and respiration biomass better than those two measures tracked each other (Smets 2016) [AB; meas; single].
>

## absolute-quantification.8 (claim)

Total 16S qPCR multiplied by relative abundance correlated near-perfectly with taxon-specific qPCR, a comparison of methods that share an upstream (qPCR against qPCR-anchored sequencing) for four taxa.

- conf: single (marker)
- class: meas (marker)
- holds: four taxa
- src: jianQuantitativePCRProvides2020 (FT; meas; single)
- trail: MB-01 §5.5, §Adversarial

From the note:

> MB-01:I-0139 [5.5 Absolute quantification of total load] - Total 16S qPCR multiplied by relative abundance correlated near-perfectly with taxon-specific qPCR (Jian 2020) [FT; meas; single].
>
> MB-01:C-127 [warning: Adversarial critique, full findings] - D5 absolute quantification: Lin 2019 is listed among failure modes (r2 0.19 before correction, four outliers removed) without the authors' conclusion that the method is quantitative and consistent with flow cytometry. Jian 2020's 'near-perfect' correlation is given at face value, although it is also a comparison of methods that share an upstream (qPCR versus qPCR-anchored sequencing).
>
> MB-01:C-106 [warning: Adversarial critique, full findings] There is no 16S-versus-shotgun comparison of the same samples, and no culture-based, microscopy/FISH or taxon-specific qPCR comparison beyond Jian 2020's four taxa.
>

## absolute-quantification.9 (claim)

In simulation, experimental quantitative profiling outperformed computational transformations for associations.

- conf: not stated
- class: not stated
- holds: simulation
- src: llorensricoBenchmarkingMicrobiomeTransformations2021
- trail: MB-01 §5.5

From the note:

> MB-01:B-0315 [5.5 Absolute quantification of total load] - In simulation, experimental quantitative profiling outperformed computational transformations for associations (Llorens-Rico 2021).
>

## absolute-quantification.10 (claim)

Absolute quantification addresses differences in load but does not remove taxon-specific extraction and PCR bias.

- conf: not stated
- class: not stated
- holds: as stated
- src: mclarenConsistentCorrectableBias2019, bonkPCRbasedQuantificationTaxaspecific2018
- trail: MB-01 §5.5, §answers, §critic, §8. Answers

From the note:

> MB-01:B-0316 [5.5 Absolute quantification of total load] **What it does not correct, and failure modes.**
>
> MB-01:B-0317 [5.5 Absolute quantification of total load] - Taxon-specific extraction and PCR bias remain (McLaren 2019; Bonk 2018).
>
> MB-01:A-267 [quote: Answers as delivered] They do not correct taxon-specific extraction and PCR bias. qPCR and flow cytometry diverged on faeces (Galazzo 2020, single source).
>
> MB-01:A-312 [8. Answers in brief] Absolute quantification addresses differences in load but not taxon-specific bias, and its methods disagree with each other.
>
> MB-01:C-042 [danger: Critic: answers partly supported] It supports that absolute quantification changes conclusions but does not remove taxon-specific bias.
>

## absolute-quantification.11 (claim)

qPCR and sequencing both count extracellular DNA, unlike cell counts.

- conf: not stated
- class: not stated
- holds: as stated
- src: jianQuantitativePCRProvides2020
- trail: MB-01 §5.5

From the note:

> MB-01:B-0318 [5.5 Absolute quantification of total load] - qPCR and sequencing both count extracellular DNA, unlike cell counts (Jian 2020).
>

## absolute-quantification.12 (claim)

qPCR and flow cytometry agreed on a whole-cell mock (|r| = 0.967) but gave "highly divergent" profiles for faeces, where qPCR and flow-cytometry enumeration correlated at Pearson r = -0.50; ddPCR correlated strongly with qPCR, and the authors used this to rule out qPCR imprecision as the cause of the divergence.

- conf: single (marker)
- class: meas (marker)
- holds: a whole-cell mock and faeces
- src: galazzoHowCountOur2020 (FT; meas; single)
- trail: MB-01 §5.5, §answers, §critic, §Adversarial

From the note:

> MB-01:I-0140 [5.5 Absolute quantification of total load] - qPCR and flow cytometry agreed on a whole-cell mock (|r| = 0.967) but gave "highly divergent" profiles for faeces. ddPCR versus flow correlated at only r = 0.50 (Galazzo 2020) [FT; meas; single].
>
> MB-01:A-267 [quote: Answers as delivered] They do not correct taxon-specific extraction and PCR bias. qPCR and flow cytometry diverged on faeces (Galazzo 2020, single source).
>
> MB-01:A-292 [quote: Answers as delivered] The divergence of absolute-quantification methods rests on Galazzo 2020.
>
> MB-01:C-045 [danger: Critic: answers partly supported] (2) Galazzo 2020: the r = -0.50 correlation on faeces is between qPCR and flow cytometry, not ddPCR and flow. ddPCR correlated strongly with qPCR, and the authors used this to rule out qPCR imprecision as the cause of the divergence.
>
> MB-01:C-057 [danger: Critic: answers partly supported] (c) The Galazzo 2020 r = 0.50 correlation is reported as ddPCR versus flow cytometry; it is qPCR versus flow (r = -0.50).
>
> MB-01:C-071 [warning: Adversarial critique, full findings] - Galazzo 2020 (FT): the review says 'ddPCR versus flow correlated at only r = 0.50'. The full text reports qPCR versus flow-cytometry enumeration on faeces (Pearson r = -0.50); ddPCR 'correlated strongly with qPCR'.
>

## absolute-quantification.13 (claim)

Synthetic spike-ins had differing detection efficiencies and small departures from linearity, and correlations were weaker with Taq than with KOD polymerase.

- conf: repl (marker)
- class: meas (marker)
- holds: synthetic spike-in standards
- src: tourlousseSyntheticSpikeinStandards2016 (FT; meas; repl)
- trail: MB-01 §5.5

From the note:

> MB-01:I-0141 [5.5 Absolute quantification of total load] - Synthetic spike-ins had differing detection efficiencies and small departures from linearity. Correlations were weaker with Taq than with KOD polymerase (Tourlousse 2017) [FT; meas; repl].
>

## absolute-quantification.14 (claim)

Seawater internal standards agreed with flow cytometry at r2 = 0.19 until corrections for copy number and particle association (with four outliers removed) raised it to 0.61, and the authors conclude that the internal-standard method is quantitative and consistent with flow cytometry; the r2 figures need the body and could not be verified.

- conf: single (marker)
- class: meas (marker)
- holds: seawater
- src: linTowardsQuantitativeMicrobiome2019 (FT; meas; single)
- trail: MB-01 §5.5, §answers, §critic, §Adversarial
- limit: access (critic: MB-01:C-076)
- contrary: one-sided (critic: MB-01:C-127)

From the note:

> MB-01:I-0142 [5.5 Absolute quantification of total load] - Seawater internal standards agreed with flow cytometry at r2 = 0.19 until corrections for copy number and particle association (with four outliers removed) raised it to 0.61 (Lin 2019) [FT; meas; single].
>
> MB-01:A-269 [quote: Answers as delivered] Spike-in totals agreed poorly with flow cytometry (r2 0.19) until corrected (Lin 2019).
>
> MB-01:B-0363 [7. Bounds and negative results] - internal standards before correction (Lin 2019);
>
> MB-01:C-046 [danger: Critic: answers partly supported] (3) Lin 2019: the authors conclude that the internal-standard method is quantitative and consistent with flow cytometry.
>
> MB-01:C-047 [danger: Critic: answers partly supported] The review reports only r2 = 0.19 before correction and does not give the authors' conclusion (Common rule 6).
>
> MB-01:C-048 [danger: Critic: answers partly supported] That figure could not be verified here.
>
> MB-01:C-076 [warning: Adversarial critique, full findings] Figures needing the body (Zhou 2011's 0.06 to 5.34% spike range and its 13.1%/5.9% discussion values; Kozich's 9,913 and 2,454 reads; Haegeman's 26,079 reads and 2,880 species; Lin 2019's r2 0.19 and 0.61) could not be confirmed, and the review shows no evidence of full-text reading beyond 'per angle'.
>
> MB-01:C-081 [warning: Adversarial critique, full findings] - Lin 2019: the review reports the internal-standard method's poor initial agreement with flow cytometry (r2 0.19) without the authors' conclusion that the method 'provided results consistent with ... total bacterial counts by flow cytometry' and 'is quantitative' (abstract). This breaches Common rule 6.
>
> MB-01:C-127 [warning: Adversarial critique, full findings] - D5 absolute quantification: Lin 2019 is listed among failure modes (r2 0.19 before correction, four outliers removed) without the authors' conclusion that the method is quantitative and consistent with flow cytometry. Jian 2020's 'near-perfect' correlation is given at face value, although it is also a comparison of methods that share an upstream (qPCR versus qPCR-anchored sequencing).
>

## absolute-quantification.15 (claim)

A review states that internal standards often underperform or fail.

- conf: not stated
- class: assert (marker)
- holds: a review
- src: harrisonQuestAbsoluteAbundance2020 (AB; assert)
- trail: MB-01 §5.5

From the note:

> MB-01:I-0143 [5.5 Absolute quantification of total load] - A review states that internal standards often underperform or fail (Harrison 2021) [AB; assert].
>

## absolute-quantification.16 (claim)

The agreement between absolute-quantification methods is weak: on qPCR against flow cytometry, Jian 2020 and Galazzo 2020 conflict, and the divergence of the methods rests on Galazzo 2020.

- conf: not stated
- class: not stated
- holds: the two studies named
- src: jianQuantitativePCRProvides2020, galazzoHowCountOur2020
- trail: MB-01 §answers, §6. Where
- rating: "weak on the agreement between quantification methods"

From the note:

> MB-01:A-279 [quote: Answers as delivered] Absolute quantification: replicated that it changes conclusions; weak on the agreement between quantification methods.
>
> MB-01:A-283 [quote: Answers as delivered] ANCOM-BC: maker claims versus Yang and Chen 2022 and Wirbel 2024. qPCR versus flow cytometry: Jian 2020 versus Galazzo 2020.
>
> MB-01:A-292 [quote: Answers as delivered] The divergence of absolute-quantification methods rests on Galazzo 2020.
>
> MB-01:B-0342 [6. Where the evidence conflicts] Absolute quantification: Jian 2020 versus Galazzo 2020.
>

## absolute-quantification.17 (claim)

In the review's summary, absolute load measurements correct differences in total load and reversals of relative trends, but not taxon-specific bias, extraction-yield variation, or disagreement between qPCR and flow cytometry; they apply to all three measures and are strongest for differential abundance and associations.

- conf: not stated
- class: not stated
- holds: the review's summary by approach
- src: none (the review's summary)
- trail: MB-01 §5.6, §Adversarial

From the note:

> MB-01:B-0320 [5.6 Summary by approach] | Approach | Shown to correct | Not shown to correct, or shown to fail | Measure (alpha / beta / DA) |
>
> MB-01:B-0321 [5.6 Summary by approach] | Absolute load (qPCR, flow, dPCR, spike-ins) | Differences in total load; reversals of relative trends | Taxon-specific bias; extraction-yield variation; disagreement between qPCR and flow | All three; strongest for DA and associations |
>
> MB-01:C-143 [warning: Adversarial critique, full findings] - Section 5.6 summary table: 'Shown to correct' cells mix makers' claims and simulation results with measured results without per-cell evidence class, so it reads closer to a method recommendation than the brief allows.
>

Not found in the cited text (where to look, not what is wrong): holds: review

## absolute-quantification.18 (claim)

No approach is shown to correct depth, load and taxon-specific bias together: no benchmark builds taxon-specific bias and differences in total load into the simulated truth together, apart from one that simulated faeces without taxon bias; no benchmark in soil or water used measured absolute loads as truth; and no richness correction was tested against known-richness mocks across depths.

- conf: not stated
- class: search (note: "Not found: an independent microbial amplicon benchmark of coverage-based standardisation with known truth")
- holds: the statistics angle's routes (Europe PMC, Crossref, publisher HTML, author PDFs, web search) and the lab and bioinformatics angles for spike-ins
- src: llorensricoBenchmarkingMicrobiomeTransformations2021
- trail: MB-01 §answers, §critic, §Adversarial
- search: searched, not found (note: "Not found: an independent microbial amplicon benchmark of coverage-based standardisation with known truth")

From the note:

> MB-01:A-230 [quote: Answers as delivered] **contested; no approach is shown to correct depth, load and taxon-specific bias together; per-measure details in answer**: Richness and alpha diversity.
>
> MB-01:A-285 [quote: Answers as delivered] *Not measured:* Not found: an independent microbial amplicon benchmark of coverage-based standardisation with known truth; any D5 benchmark that includes taxon-specific bias and differences in total load in the simulated truth together, apart from Llorens-Rico 2021 (simulated faeces, no taxon bias); benchmarks in soil or water with measured absolute loads used as truth; tests of richness corrections against known-richness mocks across depths.
>
> MB-01:A-286 [quote: Answers as delivered] Routes: statistics angle (Europe PMC, Crossref, publisher HTML, author PDFs, web search); lab and bioinformatics angles for spike-ins.
>
> MB-01:C-051 [danger: Critic: answers partly supported] Benchmarks that build taxon-specific bias and load differences into the simulated truth together are absent, apart from Llorens-Rico 2021, which simulated faeces without taxon bias.
>
> MB-01:C-118 [warning: Adversarial critique, full findings] - gap: No benchmark of any D5 approach in soil or water with measured absolute loads as truth, and no known-richness mock tested across depths.; setting_or_class: Soil and aquatic communities with measured load; known-richness mocks; direction: D5
>

## rarity-terms.1 (claim)

Three families of definition of abundance and distribution terms are in use and are not interchangeable: within-sample relative-abundance thresholds (0.1% most common for rare, 1% for abundant), occupancy (core, mostly occurrence-only, 30 to 100%), and regional or global classes defined on pooled data; usage is heterogeneous and often unstated, and the usage percentages rest on two surveys.

- conf: not stated
- class: not stated
- holds: microbial ecology literature; two systematic literature surveys plus reviews
- src: pascoalDefinitionMicrobialRare2025, neuDefiningQuantifyingCore2021
- trail: MB-02 §answers, §critic
- rating: "Strong on the fact of heterogeneity"

From the note:

> MB-02:A-060 [quote: Answers as delivered] **D2: definitions and usage of abundant, rare, dominant, common, prevalent, core and related terms**: Three families of definition are in use and are not interchangeable.
>
> MB-02:A-070 [quote: Answers as delivered] *Strength:* Strong on the fact of heterogeneity and on the dominance of fixed relative abundance thresholds and occupancy-only cores (two systematic literature surveys [42,51] plus reviews).
>
> MB-02:A-079 [quote: Answers as delivered] *Single-source sensitivity:* The usage percentages rest on two surveys: rare-biosphere usage on Pascoal et al. 2025 [42] and core usage on Neu et al. 2021 [51]; removing either removes the quantitative usage picture for that term.
>
> MB-02:A-144 [Answers] **D2.** Definitions fall into three families: within-sample thresholds (0.1% most common for rare, 1% for abundant), occupancy (core, mostly occurrence-only, 30 to 100%), and regional or global (dominant or common defined on pooled data).
>
> MB-02:A-145 [Answers] Usage is heterogeneous and often unstated [42,51].
>
> MB-02:C-028 [danger: Critic: answers partly supported] **D2 definitions and thresholds**: Supported in substance.
>
> MB-02:C-029 [danger: Critic: answers partly supported] Three families of definition are in use: within-sample thresholds (0.1% most common for rare), occupancy (core, mostly occurrence-only) and pooled or global classes.
>
> MB-02:C-030 [danger: Critic: answers partly supported] Usage is heterogeneous and often unstated (two surveys [42,51]).
>

## rarity-terms.2 (claim)

Within a sample, rare is most often defined as below 0.1% of reads, sometimes below 0.01% or 0.001%, and abundant usually as above 1%; one of the sources cited for these thresholds uses a single rare/common cutoff and does not support "abundant above 1%".

- conf: not stated
- class: not stated
- holds: within-sample relative abundance
- src: lynchEcologyExplorationRare2015, galandEcologyRareMicrobial2009, daiIdentifyingKeyTaxonomic2016, jiaUnravellingInterplayEcological2022
- trail: MB-02 §answers, §critic

From the note:

> MB-02:A-061 [quote: Answers as delivered] (1) Within-sample relative abundance: rare is most often below 0.1% of reads per sample, sometimes below 0.01% or 0.001%; abundant is usually above 1% [40,43,44,49].
>
> MB-02:C-031 [danger: Critic: answers partly supported] Three corrections.
>
> MB-02:C-032 [danger: Critic: answers partly supported] (1) Jia et al. 2022 [49] uses a single rare/common cutoff and does not support 'abundant above 1%'.
>
> MB-02:C-065 [danger: Critic: answers partly supported] (4) Small misreports: Starke 2021 computed its 7.1% on n = 10 mocks (one of 11 excluded); [49] cited for an 'abundant above 1%' threshold it does not use; Custer 'about 1%' is a derivation.
>

## rarity-terms.3 (claim)

The "rare biosphere" entered usage with deep-sea tag sequencing, which found thousands of low-abundance populations alongside a few dominants.

- conf: not stated
- class: not stated
- holds: deep sea
- src: soginMicrobialDiversityDeep2006 (AB)
- trail: MB-02 §D2.1

From the note:

> MB-02:B-0156 [D2.1 Within-sample relative abundance] The "rare biosphere" entered usage with deep-sea tag sequencing, which found thousands of low-abundance populations alongside a few dominants [38, AB].
>

## rarity-terms.4 (claim)

Reviews describe a few dominant taxa and many rare ones without fixing a threshold.

- conf: not stated
- class: not stated
- holds: reviews
- src: pedrosalioRareBacterialBiosphere2012 (AB), lynchEcologyExplorationRare2015 (AB), pascoalMicrobialRareBiosphere2021 (AB)
- trail: MB-02 §D2.1

From the note:

> MB-02:B-0157 [D2.1 Within-sample relative abundance] Reviews describe a few dominant taxa and many rare ones without fixing a threshold [39, AB; 40, AB; 41, AB].
>

## rarity-terms.5 (claim)

Rare has been defined as below 0.01% and abundant as above 1% per sample, a cutoff the authors called "much more severe than the <0.1% criteria proposed earlier" and tied to a singleton in the smallest library.

- conf: not stated
- class: not stated
- holds: per sample
- src: galandEcologyRareMicrobial2009 (FT)
- trail: MB-02 §D2.1

From the note:

> MB-02:B-0158 [D2.1 Within-sample relative abundance] Operational thresholds vary:
>
> MB-02:B-0159 [D2.1 Within-sample relative abundance] - **Galand et al. 2009** [43, FT]: rare below 0.01% and abundant above 1% per sample.
>
> MB-02:B-0160 [D2.1 Within-sample relative abundance] They called the 0.01% cutoff "much more severe than the <0.1% criteria proposed earlier" and tied it to a singleton in the smallest library.
>

## rarity-terms.6 (claim)

Rare below 0.1% and abundant above 1% were combined with behaviour across samples into six categories: always abundant, conditionally abundant, always rare, conditionally rare, moderate, and conditionally rare or abundant.

- conf: not stated
- class: not stated
- holds: one study
- src: daiIdentifyingKeyTaxonomic2016 (AB)
- trail: MB-02 §D2.1, §answers

From the note:

> MB-02:B-0161 [D2.1 Within-sample relative abundance] - **Dai et al. 2016** [44, AB]: rare below 0.1%, abundant above 1%.
>
> MB-02:B-0162 [D2.1 Within-sample relative abundance] Their six categories combine these thresholds with behaviour across samples: always abundant, conditionally abundant, always rare, conditionally rare, moderate, and conditionally rare or abundant.
>
> MB-02:A-063 [quote: Answers as delivered] Categories mixing thresholds with behaviour across samples exist: always or conditionally rare or abundant (thresholds 0.1% and 1% in [44]); conditionally rare taxa defined by bimodal abundance over time with a maximum above 1% [45]; permanently, transiently and conditionally rare [49].
>

## rarity-terms.7 (claim)

In a survey of 181 rare-biosphere articles from 2006 to 2024, about 37% gave no clear method or definition; of those with one, about 84% used relative abundance thresholds and about 60% of those a single threshold, about half used 0.1%, and about 70% applied it per sample rather than to the pooled dataset.

- conf: not stated
- class: not stated
- holds: 181 articles; the only survey of rare-biosphere usage
- src: pascoalDefinitionMicrobialRare2025 (FT)
- trail: MB-02 §D2.1, §answers

From the note:

> MB-02:B-0163 [D2.1 Within-sample relative abundance] The most systematic usage survey covers 181 rare-biosphere articles from 2006 to 2024 [42, FT]:
>
> MB-02:B-0164 [D2.1 Within-sample relative abundance] - About 37% gave no clear method.
>
> MB-02:B-0165 [D2.1 Within-sample relative abundance] - Of those with a method, about 84% used relative abundance thresholds.
>
> MB-02:B-0166 [D2.1 Within-sample relative abundance] - About 60% of those used a single threshold.
>
> MB-02:B-0167 [D2.1 Within-sample relative abundance] - About half used 0.1%, about 70% of them per sample rather than on the pooled dataset.
>
> MB-02:A-062 [quote: Answers as delivered] A survey of 181 rare-biosphere articles (2006 to 2024) found about 37% gave no clear definition; of those that did, about 84% used relative abundance thresholds, about half used 0.1%, and about 70% applied it per sample [42].
>
> MB-02:A-079 [quote: Answers as delivered] *Single-source sensitivity:* The usage percentages rest on two surveys: rare-biosphere usage on Pascoal et al. 2025 [42] and core usage on Neu et al. 2021 [51]; removing either removes the quantitative usage picture for that term.
>

## rarity-terms.8 (claim)

Conditionally rare taxa are defined by a bimodal abundance distribution over time (coefficient of bimodality) together with a maximum relative abundance above 1%; across 42 non-soil time series they made up 1.5 to 28% of membership.

- conf: not stated
- class: not stated
- holds: 42 non-soil time series
- src: shadeConditionallyRareTaxa2014 (FT, excerpts)
- trail: MB-02 §D2.2, §answers

From the note:

> MB-02:B-0179 [D2.2 Occupancy and prevalence across samples or time] Temporal rarity types add a second axis:
>
> MB-02:B-0180 [D2.2 Occupancy and prevalence across samples or time] - **Conditionally rare taxa** [45, FT]: a bimodal abundance distribution over time (coefficient of bimodality) together with a maximum relative abundance above 1%.
>
> MB-02:B-0181 [D2.2 Occupancy and prevalence across samples or time] Across 42 non-soil time series, these taxa made up 1.5 to 28% of membership [45, AB].
>
> MB-02:A-063 [quote: Answers as delivered] Categories mixing thresholds with behaviour across samples exist: always or conditionally rare or abundant (thresholds 0.1% and 1% in [44]); conditionally rare taxa defined by bimodal abundance over time with a maximum above 1% [45]; permanently, transiently and conditionally rare [49].
>

## rarity-terms.9 (claim)

A three-way split into permanently, transiently and conditionally rare taxa has been applied in soil.

- conf: not stated
- class: not stated
- holds: soil
- src: jiaUnravellingInterplayEcological2022 (FT)
- trail: MB-02 §D2.2, §answers

From the note:

> MB-02:B-0182 [D2.2 Occupancy and prevalence across samples or time] - **Permanently, transiently and conditionally rare taxa** [49, FT]: a three-way split applied in soil.
>
> MB-02:A-063 [quote: Answers as delivered] Categories mixing thresholds with behaviour across samples exist: always or conditionally rare or abundant (thresholds 0.1% and 1% in [44]); conditionally rare taxa defined by bimodal abundance over time with a maximum above 1% [45]; permanently, transiently and conditionally rare [49].
>

## rarity-terms.10 (claim)

Across 30 datasets (1,998 samples), rarer taxa better predicted soil community structure; this abstract-level source does not report abundance-occupancy and is not used in the answers.

- conf: not stated
- class: not stated
- holds: 30 soil datasets; an abstract
- src: ramirezDetectingMacroecologicalPatterns2017 (AB)
- trail: MB-02 §Search record

From the note:

> MB-02:B-0303 [Search record] Ramirez et al. 2018 (reference 65) was read at abstract level.
>
> MB-02:B-0304 [Search record] It reports that rarer taxa better predicted soil community structure across 30 datasets (1,998 samples), but it does not report abundance-occupancy and is not used in the answers.
>

## rarity-terms.11 (claim)

No survey was found that tallies definitions specifically within soil studies, or separately for bulk soil and rhizosphere.

- conf: not stated
- class: search (note: "No survey found that tallies definitions specifically within soil studies")
- holds: soil
- src: none (a search result)
- trail: MB-02 §answers
- search: searched, not found (note: "No survey found that tallies definitions specifically within soil studies")

From the note:

> MB-02:A-075 [quote: Answers as delivered] *Not measured:* No survey found that tallies definitions specifically within soil studies, or separately for bulk soil and rhizosphere.
>

## rarity-terms.12 (claim)

No study was found that compares threshold-based rarity classes between amplicon and metagenome data from the same soil samples; the ulrb comparison of amplicon and metagenome units used marine samples.

- conf: not stated
- class: search (note: "No study found that compares threshold-based rarity classes")
- holds: soil
- src: pascoalDefinitionMicrobialRare2025
- trail: MB-02 §answers
- search: searched, not found (note: "No study found that compares threshold-based rarity classes")

From the note:

> MB-02:A-076 [quote: Answers as delivered] No study found that compares threshold-based rarity classes between amplicon and metagenome data from the same soil samples (the ulrb comparison of amplicon and metagenome units used marine samples).
>

## rarity-terms.13 (claim)

Copy-number-corrected rarity thresholds were not found to have been tested.

- conf: not stated
- class: search (note: "Copy-number-corrected thresholds were not found to have been tested")
- holds: as stated
- src: none (a search result)
- trail: MB-02 §answers
- search: searched, not found (note: "Copy-number-corrected thresholds were not found to have been tested")

From the note:

> MB-02:A-077 [quote: Answers as delivered] Copy-number-corrected thresholds were not found to have been tested.
>

## core-microbiome.1 (claim)

"Core" is the main occupancy term; it was first framed as the members shared across samples, the overlap of Venn diagrams, with later calls to add persistence and connectivity.

- conf: not stated
- class: not stated
- holds: core-microbiome literature
- src: shadeBeyondVennDiagram2012 (AB)
- trail: MB-02 §D2.2

From the note:

> MB-02:B-0168 [D2.2 Occupancy and prevalence across samples or time] "Core" is the main occupancy term.
>
> MB-02:B-0169 [D2.2 Occupancy and prevalence across samples or time] It was first framed as the members shared across samples, the overlap of Venn diagrams, with later calls to add persistence and connectivity [50, AB].
>

Not found in the cited text (where to look, not what is wrong): holds: core-microbiome

## core-microbiome.2 (claim)

In a survey of 224 core-microbiome studies, 75.4% defined the core by occurrence only, 4% by relative abundance only and 11.6% by both, with over 18% not stating a method; occurrence cutoffs ran from 30% to 100% of samples (100% most common), and abundance cutoffs in combined methods from 0.1% to 4.5%.

- conf: not stated
- class: not stated
- holds: 224 studies; the only survey of core usage
- src: neuDefiningQuantifyingCore2021 (FT, first 100,000 characters)
- trail: MB-02 §D2.2, §answers

From the note:

> MB-02:B-0170 [D2.2 Occupancy and prevalence across samples or time] A survey of 224 core-microbiome studies [51, FT] found:
>
> MB-02:B-0171 [D2.2 Occupancy and prevalence across samples or time] - 75.4% used occurrence only.
>
> MB-02:B-0172 [D2.2 Occupancy and prevalence across samples or time] - 4% used relative abundance only.
>
> MB-02:B-0173 [D2.2 Occupancy and prevalence across samples or time] - 11.6% combined the two.
>
> MB-02:B-0174 [D2.2 Occupancy and prevalence across samples or time] - Over 18% did not state a method.
>
> MB-02:B-0175 [D2.2 Occupancy and prevalence across samples or time] - Occurrence cutoffs ranged from 30% to 100% of samples; 100% was the most common.
>
> MB-02:B-0176 [D2.2 Occupancy and prevalence across samples or time] - In combined methods, abundance cutoffs ran from 0.1% to 4.5%.
>
> MB-02:A-064 [quote: Answers as delivered] (2) Occupancy or prevalence across samples: the core microbiome is defined by occurrence alone in 75.4% of 224 studies, by abundance alone in 4%, and by both in 11.6%, with over 18% not stating a method; occurrence cutoffs run from 30% to 100% of samples (100% most common) and abundance cutoffs from 0.1% to 4.5% [51].
>
> MB-02:A-079 [quote: Answers as delivered] *Single-source sensitivity:* The usage percentages rest on two surveys: rare-biosphere usage on Pascoal et al. 2025 [42] and core usage on Neu et al. 2021 [51]; removing either removes the quantitative usage picture for that term.
>

## core-microbiome.3 (claim)

Citing other work, Neu et al. report that only two OTUs were shared by all of 24 soil locations and none across 51 wastewater plants.

- conf: not stated
- class: not stated
- holds: soil and wastewater; secondary
- src: neuDefiningQuantifyingCore2021
- trail: MB-02 §D2.2
- limit: access (note: "SECONDARY via [51]")

From the note:

> MB-02:B-0177 [D2.2 Occupancy and prevalence across samples or time] Neu et al. also report, citing other work, that only two OTUs were shared by all of 24 soil locations and none across 51 wastewater plants (SECONDARY via [51]).
>

## core-microbiome.4 (claim)

Risely distinguishes five kinds of core (common, temporal, ecological, functional, host-adapted) and argues that no one definition captures all.

- conf: not stated
- class: not stated
- holds: host-microbe systems
- src: riselyApplyingCoreMicrobiome2020 (AB)
- trail: MB-02 §D2.2

From the note:

> MB-02:B-0178 [D2.2 Occupancy and prevalence across samples or time] Risely distinguishes five kinds of core (common, temporal, ecological, functional, host-adapted) and argues that no one definition captures all [55, AB].
>

Not found in the cited text (where to look, not what is wrong): holds: host-microbe

## regional-terms.1 (claim)

In soil, "dominant" has been defined jointly: in the top 10% of phylotypes by share of 16S reads and present in more than half of 237 soils.

- conf: not stated
- class: not stated
- holds: 237 soils
- src: delgadobaquerizoGlobalAtlasDominant2018 (FT)
- trail: MB-02 §D2.3, §answers

From the note:

> MB-02:B-0183 [D2.3 Regional and global distribution] In soil, "dominant" has been defined jointly: in the top 10% of phylotypes by share of 16S reads and present in more than half of 237 soils [60, FT].
>
> MB-02:A-065 [quote: Answers as delivered] (3) Regional or global distribution: 'dominant' soil phylotypes were defined as both in the top 10% by reads and present in over half of 237 sites [60]; 'common' versus 'rare' was set by a data-driven global threshold (about 0.019% of pooled relative abundance) [61].
>

## regional-terms.2 (claim)

"Common" versus "rare" has also been set by a data-driven minimum cross-entropy threshold on the globally pooled rank-abundance distribution, about 0.019% of pooled relative abundance, with prevalence across samples reported separately.

- conf: not stated
- class: not stated
- holds: 844 global soils
- src: bickelChosenFewVariations2021 (FT)
- trail: MB-02 §D2.3, §answers

From the note:

> MB-02:B-0184 [D2.3 Regional and global distribution] "Common" versus "rare" has also been set by a data-driven minimum cross-entropy threshold on the globally pooled rank-abundance distribution, about 0.019% [61, FT].
>
> MB-02:B-0185 [D2.3 Regional and global distribution] Prevalence across samples was then reported separately.
>
> MB-02:A-065 [quote: Answers as delivered] (3) Regional or global distribution: 'dominant' soil phylotypes were defined as both in the top 10% by reads and present in over half of 237 sites [60]; 'common' versus 'rare' was set by a data-driven global threshold (about 0.019% of pooled relative abundance) [61].
>

Not found in the cited text (where to look, not what is wrong): holds: 844

## regional-terms.3 (claim)

Reviews treat habitat specificity and geographic range as microbial rarity axes alongside local abundance.

- conf: not stated
- class: not stated
- holds: reviews
- src: joussetWhereLessMay2017 (FT)
- trail: MB-02 §D2.3

From the note:

> MB-02:B-0186 [D2.3 Regional and global distribution] Reviews treat habitat specificity and geographic range as microbial rarity axes alongside local abundance [47, FT].
>

## regional-terms.4 (claim)

Terms are used inconsistently: "dominant" sometimes means abundant within a sample and sometimes abundant and ubiquitous, and "common" means high pooled abundance in one study and high occupancy elsewhere.

- conf: not stated
- class: not stated
- holds: microbial ecology literature
- src: delgadobaquerizoGlobalAtlasDominant2018, bickelChosenFewVariations2021
- trail: MB-02 §answers

From the note:

> MB-02:A-074 [quote: Answers as delivered] Terms are also used inconsistently: 'dominant' sometimes means abundant within a sample and sometimes abundant and ubiquitous [60]; 'common' means high pooled abundance in [61] and high occupancy elsewhere.
>

## ecology-frameworks.1 (claim)

Rabinowitz (1981) classifies rarity by geographic range, habitat specificity and local abundance; its microbial users state these concepts "can be easily transferred to microbial communities".

- conf: not stated
- class: not stated
- holds: general ecology; known only secondarily
- src: rabinowitzSevenFormsRarity1981 (SEC), joussetWhereLessMay2017
- trail: MB-02 §D2.4, §answers
- limit: access (note: "The original was not obtained")

From the note:

> MB-02:B-0187 [D2.4 Frameworks from general ecology] - **Rabinowitz (1981).** Classifies rarity by geographic range, habitat specificity and local abundance.
>
> MB-02:B-0188 [D2.4 Frameworks from general ecology] SECONDARY via [47], whose authors state these concepts "can be easily transferred to microbial communities".
>
> MB-02:B-0189 [D2.4 Frameworks from general ecology] The original was not obtained.
>
> MB-02:A-066 [quote: Answers as delivered] From general ecology, rarity is classed along local abundance, habitat specificity and geographic range (Rabinowitz 1981, secondary via [47]), core versus occasional species are separated by persistence [57], and abundance and occupancy are usually positively related [58].
>

## ecology-frameworks.2 (claim)

In a 21-year estuarine fish record, persistent and abundant "core" species fitted a lognormal, while infrequent "occasional" species fitted a log series.

- conf: not stated
- class: not stated
- holds: estuarine fish
- src: magurranExplainingExcessRare2003 (AB)
- trail: MB-02 §D2.4, §answers

From the note:

> MB-02:B-0190 [D2.4 Frameworks from general ecology] - **Magurran and Henderson (2003).** In a 21-year estuarine fish record, persistent and abundant "core" species fitted a lognormal, while infrequent "occasional" species fitted a log series [57, AB].
>
> MB-02:A-066 [quote: Answers as delivered] From general ecology, rarity is classed along local abundance, habitat specificity and geographic range (Rabinowitz 1981, secondary via [47]), core versus occasional species are separated by persistence [57], and abundance and occupancy are usually positively related [58].
>

## ecology-frameworks.3 (claim)

The same split is reported for rare against abundant Arctic Ocean prokaryotes: log series against lognormal.

- conf: not stated
- class: not stated
- holds: Arctic Ocean prokaryotes
- src: galandEcologyRareMicrobial2009 (FT)
- trail: MB-02 §D2.4

From the note:

> MB-02:B-0191 [D2.4 Frameworks from general ecology] Galand et al. report the same split for rare versus abundant Arctic Ocean prokaryotes (log series versus lognormal) [43, FT].
>

## ecology-frameworks.4 (claim)

Positive intraspecific and interspecific abundance-occupancy relationships are general in the British flora and fauna; in general macroecology positive relationships are common and multiple explanations have been tested.

- conf: not stated
- class: not stated
- holds: British flora and fauna; general macroecology
- src: gastonAbundanceoccupancyRelationships2000 (AB)
- trail: MB-02 §D2.4, §D3.3, §answers

From the note:

> MB-02:B-0192 [D2.4 Frameworks from general ecology] - **Gaston et al. (2000).** Positive intraspecific and interspecific abundance-occupancy relationships are general in the British flora and fauna [58, AB].
>
> MB-02:B-0279 [D3.3 Sampling effort, depth, detection and null models] - **General macroecology** [58, AB]: positive relationships are common and multiple explanations have been tested.
>
> MB-02:A-066 [quote: Answers as delivered] From general ecology, rarity is classed along local abundance, habitat specificity and geographic range (Rabinowitz 1981, secondary via [47]), core versus occasional species are separated by persistence [57], and abundance and occupancy are usually positively related [58].
>
> MB-02:A-113 [quote: Answers as delivered] General macroecology finds positive interspecific relationships common [58].
>

## threshold-sensitivity.1 (claim)

In a salt-marsh soil chronosequence (Schiermonnikoog, five stages over 110 years, amplicon ASVs), the rare fraction of reads was 61.6%, 45.7% and 28.4% at cutoffs of 0.2%, 0.1% and 0.05%.

- conf: not stated
- class: not stated
- holds: one salt-marsh chronosequence
- src: jiaUnravellingInterplayEcological2022 (FT)
- trail: MB-02 §D2.5, §answers

From the note:

> MB-02:B-0193 [D2.5 Do classifications and conclusions hold across thresholds?] Direct tests found:
>
> MB-02:B-0194 [D2.5 Do classifications and conclusions hold across thresholds?] - **Soil, Schiermonnikoog salt-marsh chronosequence** (five stages over 110 years, amplicon ASVs) [49, FT].
>
> MB-02:B-0195 [D2.5 Do classifications and conclusions hold across thresholds?] The rare fraction of reads was 61.6%, 45.7% and 28.4% at cutoffs of 0.2%, 0.1% and 0.05%.
>
> MB-02:A-067 [quote: Answers as delivered] Whether conclusions hold across thresholds varies: in a soil chronosequence, the rare share of reads changed from 61.6% to 45.7% to 28.4% at 0.2%, 0.1% and 0.05% cutoffs and the composition of rarity types shifted, yet beta-diversity patterns and assembly conclusions held [49]; in Arctic Ocean data biogeography of rare taxa persisted down to 0.001% [43]; in coastal sand data, ecological patterns held after removing up to 35 to 40% of rare sequences [46]; but the same 0.1% threshold reversed the rare versus abundant ASV count between V4V5 and full-length 16S in marine samples [42]; four core methods assigned 1.2% to 9.4% of taxa as core (nearly 10-fold) with only about 1% of taxa agreed by all, and in one dataset changed a PERMANOVA conclusion [52]; in sponges, core definitions changed alpha and beta diversity in some cases but not host-specificity or network conclusions [53]; in human gut, core size depended mainly on analysis depth and required prevalence [54].
>
> MB-02:A-084 [quote: Answers as delivered] In a salt-marsh soil chronosequence the rare (below 0.1%) fraction held 45.7% of reads [49].
>

## threshold-sensitivity.2 (claim)

As the cutoff tightened, permanently and transiently rare ASVs fell in proportion, conditionally rare ASVs rose, and the relative importance of selection rose, while beta-diversity patterns and the main assembly inference (homogeneous selection for the rare biosphere, variable selection for the common) were reported as similar across cutoffs: classification changed, the qualitative conclusion held; this is the only soil test of threshold sensitivity found.

- conf: single (critic: MB-02:C-037)
- class: not stated
- holds: one soil test
- src: jiaUnravellingInterplayEcological2022 (FT)
- trail: MB-02 §D2.5, §answers, §critic

From the note:

> MB-02:B-0196 [D2.5 Do classifications and conclusions hold across thresholds?] As the cutoff tightened, permanently and transiently rare ASVs fell in proportion and conditionally rare ASVs rose.
>
> MB-02:B-0197 [D2.5 Do classifications and conclusions hold across thresholds?] Beta-diversity patterns and the main assembly inference (homogeneous selection for the rare biosphere, variable selection for the common) were reported as similar across cutoffs.
>
> MB-02:B-0198 [D2.5 Do classifications and conclusions hold across thresholds?] Classification changed; the conclusion held.
>
> MB-02:A-067 [quote: Answers as delivered] Whether conclusions hold across thresholds varies: in a soil chronosequence, the rare share of reads changed from 61.6% to 45.7% to 28.4% at 0.2%, 0.1% and 0.05% cutoffs and the composition of rarity types shifted, yet beta-diversity patterns and assembly conclusions held [49]; in Arctic Ocean data biogeography of rare taxa persisted down to 0.001% [43]; in coastal sand data, ecological patterns held after removing up to 35 to 40% of rare sequences [46]; but the same 0.1% threshold reversed the rare versus abundant ASV count between V4V5 and full-length 16S in marine samples [42]; four core methods assigned 1.2% to 9.4% of taxa as core (nearly 10-fold) with only about 1% of taxa agreed by all, and in one dataset changed a PERMANOVA conclusion [52]; in sponges, core definitions changed alpha and beta diversity in some cases but not host-specificity or network conclusions [53]; in human gut, core size depended mainly on analysis depth and required prevalence [54].
>
> MB-02:A-080 [quote: Answers as delivered] The only soil test of threshold sensitivity found is Jia et al. 2022 [49].
>
> MB-02:C-037 [danger: Critic: answers partly supported] The single soil test (Jia 2022) found that classifications shift with the cutoff and that the relative importance of selection rose as the cutoff tightened, while the qualitative assembly conclusion held.
>
> MB-02:B-0300 [Search record] - **Systematic threshold-sensitivity tests in soil**: WebSearch (standard and extended) and a Europe PMC query on rare biosphere thresholds.
>

## threshold-sensitivity.3 (claim)

In Arctic Ocean data, the biogeography of rare taxa persisted at a 0.001% cutoff.

- conf: not stated
- class: not stated
- holds: Arctic Ocean
- src: galandEcologyRareMicrobial2009 (FT)
- trail: MB-02 §D2.5, §answers

From the note:

> MB-02:B-0199 [D2.5 Do classifications and conclusions hold across thresholds?] - **Arctic Ocean** [43, FT]: biogeography of rare taxa persisted at a 0.001% cutoff.
>
> MB-02:A-067 [quote: Answers as delivered] Whether conclusions hold across thresholds varies: in a soil chronosequence, the rare share of reads changed from 61.6% to 45.7% to 28.4% at 0.2%, 0.1% and 0.05% cutoffs and the composition of rarity types shifted, yet beta-diversity patterns and assembly conclusions held [49]; in Arctic Ocean data biogeography of rare taxa persisted down to 0.001% [43]; in coastal sand data, ecological patterns held after removing up to 35 to 40% of rare sequences [46]; but the same 0.1% threshold reversed the rare versus abundant ASV count between V4V5 and full-length 16S in marine samples [42]; four core methods assigned 1.2% to 9.4% of taxa as core (nearly 10-fold) with only about 1% of taxa agreed by all, and in one dataset changed a PERMANOVA conclusion [52]; in sponges, core definitions changed alpha and beta diversity in some cases but not host-specificity or network conclusions [53]; in human gut, core size depended mainly on analysis depth and required prevalence [54].
>

## threshold-sensitivity.4 (claim)

In coastal sand data, ecological patterns were maintained after removing up to 35 to 40% of rare sequences.

- conf: not stated
- class: not stated
- holds: coastal sands
- src: gobetMultivariateCutoffLevel2010 (AB)
- trail: MB-02 §D2.5, §answers

From the note:

> MB-02:B-0200 [D2.5 Do classifications and conclusions hold across thresholds?] - **Coastal sands** [46, AB]: patterns were maintained after removing up to 35 to 40% of rare sequences.
>
> MB-02:A-067 [quote: Answers as delivered] Whether conclusions hold across thresholds varies: in a soil chronosequence, the rare share of reads changed from 61.6% to 45.7% to 28.4% at 0.2%, 0.1% and 0.05% cutoffs and the composition of rarity types shifted, yet beta-diversity patterns and assembly conclusions held [49]; in Arctic Ocean data biogeography of rare taxa persisted down to 0.001% [43]; in coastal sand data, ecological patterns held after removing up to 35 to 40% of rare sequences [46]; but the same 0.1% threshold reversed the rare versus abundant ASV count between V4V5 and full-length 16S in marine samples [42]; four core methods assigned 1.2% to 9.4% of taxa as core (nearly 10-fold) with only about 1% of taxa agreed by all, and in one dataset changed a PERMANOVA conclusion [52]; in sponges, core definitions changed alpha and beta diversity in some cases but not host-specificity or network conclusions [53]; in human gut, core size depended mainly on analysis depth and required prevalence [54].
>

## threshold-sensitivity.5 (claim)

In marine samples, the 0.1% per-sample rule gave more rare than abundant ASVs with V4V5 amplicons and the reverse with full-length 16S, and threshold-based classes behaved differently across OTUs, ASVs and metagenomic OTUs, while the unsupervised method gave the same pattern across these.

- conf: not stated
- class: not stated
- holds: marine samples
- src: pascoalDefinitionMicrobialRare2025 (FT)
- trail: MB-02 §D2.5, §answers

From the note:

> MB-02:B-0201 [D2.5 Do classifications and conclusions hold across thresholds?] - **Marine samples, ulrb paper** [42, FT].
>
> MB-02:B-0202 [D2.5 Do classifications and conclusions hold across thresholds?] The 0.1% per-sample rule gave more rare than abundant ASVs with V4V5 amplicons and the reverse with full-length 16S, and threshold-based classes behaved differently across OTUs, ASVs and metagenomic OTUs.
>
> MB-02:B-0203 [D2.5 Do classifications and conclusions hold across thresholds?] The unsupervised method gave the same pattern across these.
>
> MB-02:A-067 [quote: Answers as delivered] Whether conclusions hold across thresholds varies: in a soil chronosequence, the rare share of reads changed from 61.6% to 45.7% to 28.4% at 0.2%, 0.1% and 0.05% cutoffs and the composition of rarity types shifted, yet beta-diversity patterns and assembly conclusions held [49]; in Arctic Ocean data biogeography of rare taxa persisted down to 0.001% [43]; in coastal sand data, ecological patterns held after removing up to 35 to 40% of rare sequences [46]; but the same 0.1% threshold reversed the rare versus abundant ASV count between V4V5 and full-length 16S in marine samples [42]; four core methods assigned 1.2% to 9.4% of taxa as core (nearly 10-fold) with only about 1% of taxa agreed by all, and in one dataset changed a PERMANOVA conclusion [52]; in sponges, core definitions changed alpha and beta diversity in some cases but not host-specificity or network conclusions [53]; in human gut, core size depended mainly on analysis depth and required prevalence [54].
>

## threshold-sensitivity.6 (claim)

Four core methods compared on human faecal (319 samples) and Arabidopsis root (288 samples) data assigned 1.2% to 9.4% of taxa as core, nearly 10-fold apart; 165 to 176 taxa were agreed by all four, which is 13 to 16% of core assignments.

- conf: not stated
- class: not stated
- holds: human faecal and Arabidopsis root data
- src: custerComparativeAnalysisCore2023 (FT, first 100,000 characters)
- trail: MB-02 §D2.5, §answers, §critic, §Adversarial

From the note:

> MB-02:B-0204 [D2.5 Do classifications and conclusions hold across thresholds?] - **Core methods** [52, FT].
>
> MB-02:B-0205 [D2.5 Do classifications and conclusions hold across thresholds?] Four methods were compared on human faecal (319 samples) and Arabidopsis root (288 samples) data.
>
> MB-02:B-0206 [D2.5 Do classifications and conclusions hold across thresholds?] They assigned 1.2% to 9.4% of taxa as core, and only 165 to 176 taxa (about 1%) were agreed by all four.
>
> MB-02:A-067 [quote: Answers as delivered] Whether conclusions hold across thresholds varies: in a soil chronosequence, the rare share of reads changed from 61.6% to 45.7% to 28.4% at 0.2%, 0.1% and 0.05% cutoffs and the composition of rarity types shifted, yet beta-diversity patterns and assembly conclusions held [49]; in Arctic Ocean data biogeography of rare taxa persisted down to 0.001% [43]; in coastal sand data, ecological patterns held after removing up to 35 to 40% of rare sequences [46]; but the same 0.1% threshold reversed the rare versus abundant ASV count between V4V5 and full-length 16S in marine samples [42]; four core methods assigned 1.2% to 9.4% of taxa as core (nearly 10-fold) with only about 1% of taxa agreed by all, and in one dataset changed a PERMANOVA conclusion [52]; in sponges, core definitions changed alpha and beta diversity in some cases but not host-specificity or network conclusions [53]; in human gut, core size depended mainly on analysis depth and required prevalence [54].
>
> MB-02:C-033 [danger: Critic: answers partly supported] (2) Custer et al. 2023 report that 165 to 176 taxa were agreed by all four methods, which is 13 to 16% of core assignments.
>
> MB-02:C-081 [warning: Adversarial critique, full findings] - Custer et al. 2023 [52]: 'about 1% of taxa agreed by all four' is not a figure in the source, which gives 165 and 176 taxa as 13% and 15.85% of core assignments. It should carry a 'derived' label.
>

## threshold-sensitivity.7 (claim)

In the human data, a temporal effect significant in the full dataset was reported as not significant in core-based analyses, but the source's text is internally inconsistent on whether core analyses gained or lost the temporal effect.

- conf: not stated
- class: not stated
- holds: human data
- src: custerComparativeAnalysisCore2023
- trail: MB-02 §D2.5, §answers, §critic

From the note:

> MB-02:B-0207 [D2.5 Do classifications and conclusions hold across thresholds?] In the human data, a temporal effect significant in the full dataset was not significant in core-based analyses.
>
> MB-02:A-067 [quote: Answers as delivered] Whether conclusions hold across thresholds varies: in a soil chronosequence, the rare share of reads changed from 61.6% to 45.7% to 28.4% at 0.2%, 0.1% and 0.05% cutoffs and the composition of rarity types shifted, yet beta-diversity patterns and assembly conclusions held [49]; in Arctic Ocean data biogeography of rare taxa persisted down to 0.001% [43]; in coastal sand data, ecological patterns held after removing up to 35 to 40% of rare sequences [46]; but the same 0.1% threshold reversed the rare versus abundant ASV count between V4V5 and full-length 16S in marine samples [42]; four core methods assigned 1.2% to 9.4% of taxa as core (nearly 10-fold) with only about 1% of taxa agreed by all, and in one dataset changed a PERMANOVA conclusion [52]; in sponges, core definitions changed alpha and beta diversity in some cases but not host-specificity or network conclusions [53]; in human gut, core size depended mainly on analysis depth and required prevalence [54].
>
> MB-02:C-035 [danger: Critic: answers partly supported] (3) Custer's text is internally inconsistent on whether core analyses gained or lost the temporal effect.
>

## threshold-sensitivity.8 (claim)

Occupancy-based core methods were most accurate in simulations, in one simulation study.

- conf: single (critic: MB-02:C-092)
- class: not stated
- holds: simulations
- src: custerComparativeAnalysisCore2023
- trail: MB-02 §D2.5, §answers, §Adversarial

From the note:

> MB-02:B-0208 [D2.5 Do classifications and conclusions hold across thresholds?] Occupancy-based methods were most accurate in simulations.
>
> MB-02:A-068 [quote: Answers as delivered] Proposed standards include unsupervised classification (ulrb) [42], multivariate cutoff analysis [46,48], abundance-occupancy ranking with neutral-model deviations for cores [56], explicit reporting and distinguishing spatial and temporal scales of core [51], and occupancy-based core methods, which performed best in simulations [52].
>
> MB-02:C-092 [warning: Adversarial critique, full findings] - D2: 'Occupancy-based core methods performed best' rests on one simulation study (Custer et al. 2023 [52]) and is listed among proposed standards as if established.
>

## threshold-sensitivity.9 (claim)

In sponges, core definitions changed alpha and beta diversity in some cases but not conclusions on host specificity, environmental quality or networks, and the authors call the approach "surprisingly robust".

- conf: not stated
- class: not stated
- holds: sponges
- src: astudillogarciaEvaluatingCoreMicrobiota2017 (AB)
- trail: MB-02 §D2.5, §answers

From the note:

> MB-02:B-0209 [D2.5 Do classifications and conclusions hold across thresholds?] - **Sponges** [53, AB]: core definitions changed alpha and beta diversity in some cases but not conclusions on host specificity, environmental quality or networks.
>
> MB-02:B-0210 [D2.5 Do classifications and conclusions hold across thresholds?] The authors call the approach "surprisingly robust".
>
> MB-02:A-067 [quote: Answers as delivered] Whether conclusions hold across thresholds varies: in a soil chronosequence, the rare share of reads changed from 61.6% to 45.7% to 28.4% at 0.2%, 0.1% and 0.05% cutoffs and the composition of rarity types shifted, yet beta-diversity patterns and assembly conclusions held [49]; in Arctic Ocean data biogeography of rare taxa persisted down to 0.001% [43]; in coastal sand data, ecological patterns held after removing up to 35 to 40% of rare sequences [46]; but the same 0.1% threshold reversed the rare versus abundant ASV count between V4V5 and full-length 16S in marine samples [42]; four core methods assigned 1.2% to 9.4% of taxa as core (nearly 10-fold) with only about 1% of taxa agreed by all, and in one dataset changed a PERMANOVA conclusion [52]; in sponges, core definitions changed alpha and beta diversity in some cases but not host-specificity or network conclusions [53]; in human gut, core size depended mainly on analysis depth and required prevalence [54].
>

