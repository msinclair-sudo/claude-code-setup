## rarefying.10 (claim)

Rarefaction curves display sampling completeness (ecology) and were not benchmarked as a comparison method in the sources found.

- conf: not stated
- class: not stated
- holds: the review's summary by approach
- src: none (the review's summary)
- trail: MB-01 §5.6

From the note:

> MB-01:B-0320 [5.6 Summary by approach] | Approach | Shown to correct | Not shown to correct, or shown to fail | Measure (alpha / beta / DA) |
>
> MB-01:B-0325 [5.6 Summary by approach] | Rarefaction curves | Display of sampling completeness (ecology) | Not benchmarked as a comparison method in the sources found | Alpha |
>

Not found in the cited text (where to look, not what is wrong): holds: review

## rarefying.11 (claim)

Simulation results on rarefying and its alternatives flip with design choices, as Weiss 2017 and Schloss 2024a both say.

- conf: not stated
- class: not stated
- holds: simulation benchmarks
- src: weissNormalizationMicrobialDifferential2017, schlossWasteNotWant2024, hongRarefyNotRarefy2022
- trail: MB-01 §answers, §Adversarial

From the note:

> MB-01:A-284 [quote: Answers as delivered] Simulation results flip with design choices; Weiss 2017 and Schloss 2024a both say so.
>
> MB-01:C-142 [warning: Adversarial critique, full findings] - Overview: 'Simulations disagree mainly because they build different data-generating processes into the truth'. This is partly supported (Weiss 2017, Hong 2022 and Schloss 2024a each say results depend on data-generating assumptions) but is phrased as the review's own causal diagnosis.
>

## scaling-normalisation.1 (claim)

In RNA-seq, total-count scaling can bias differential-expression estimates.

- conf: not stated
- class: not stated
- holds: RNA-seq, indirect
- src: bullardEvaluationStatisticalMethods2010 (AB; INDIRECT)
- trail: MB-01 §5.1

From the note:

> MB-01:B-0264 [5.1 Origins of the approaches] **Scaling normalisation.** Total-count scaling can bias differential-expression estimates in RNA-seq (Bullard 2010) [AB; INDIRECT].
>

## scaling-normalisation.2 (claim)

TMM and DESeq's negative binomial model also come from RNA-seq, and both assume most features are unchanged between conditions.

- conf: not stated
- class: not stated
- holds: RNA-seq, indirect
- src: robinsonScalingNormalizationMethod2010 (AB; INDIRECT), andersDifferentialExpressionAnalysis2010 (AB; INDIRECT), weissNormalizationMicrobialDifferential2017
- trail: MB-01 §5.1

From the note:

> MB-01:B-0265 [5.1 Origins of the approaches] TMM (Robinson and Oshlack 2010) and DESeq's negative binomial model (Anders and Huber 2010) also come from RNA-seq [AB; INDIRECT].
>
> MB-01:B-0266 [5.1 Origins of the approaches] Weiss 2017 notes that both assume most features are unchanged between conditions.
>

## scaling-normalisation.3 (claim)

In shotgun gene-abundance data, TMM and RLE performed best.

- conf: not stated
- class: not stated
- holds: shotgun gene-abundance data, indirect
- src: pereiraComparisonNormalizationMethods2018 (AB; INDIRECT, shotgun)
- trail: MB-01 §5.1

From the note:

> MB-01:B-0267 [5.1 Origins of the approaches] In shotgun gene-abundance data, TMM and RLE performed best (Buongermino Pereira 2018) [AB; INDIRECT, shotgun].
>

## scaling-normalisation.4 (claim)

Scaling normalisations used on microbiome data (TMM, RLE, CSS, VST, SRS, Wrench) come from RNA-seq and assume most features do not change, and under Schloss's null model they did not remove depth effects.

- conf: not stated
- class: not stated
- holds: Schloss's null model
- src: bullardEvaluationStatisticalMethods2010, robinsonScalingNormalizationMethod2010, andersDifferentialExpressionAnalysis2010, schlossRarefactionCurrentlyBest2024
- trail: MB-01 §answers

From the note:

> MB-01:A-270 [quote: Answers as delivered] Scaling normalisations (TMM, RLE, CSS, VST, SRS, Wrench) come from RNA-seq (Bullard 2010; Robinson and Oshlack 2010; Anders and Huber 2010, indirect) and assume most features do not change.
>
> MB-01:A-271 [quote: Answers as delivered] Under Schloss's null they did not remove depth effects.
>

Not found in the cited text (where to look, not what is wrong): holds: model

## scaling-normalisation.5 (claim)

In a simulation, RLE and VST came close to quantitative methods for association tests in a dysbiosis scenario.

- conf: not stated
- class: not stated
- holds: a simulation, dysbiosis scenario
- src: llorensricoBenchmarkingMicrobiomeTransformations2021
- trail: MB-01 §answers

From the note:

> MB-01:A-272 [quote: Answers as delivered] In the Llorens-Rico 2021 simulation, RLE and VST came close to quantitative methods for association tests in a dysbiosis scenario.
>

## scaling-normalisation.6 (claim)

Wrench's makers state that library-size scaling and rarefaction cannot correct compositional bias that is uncorrelated with library size.

- conf: not stated
- class: not stated
- holds: a makers' claim
- src: kumarAnalysisCorrectionCompositional2018 (AB; makers' claim)
- trail: MB-01 §5.4

From the note:

> MB-01:B-0307 [5.4 Tests of which taxa differ in abundance] Wrench's makers state that library-size scaling and rarefaction cannot correct compositional bias that is uncorrelated with library size (Kumar 2018) [AB; makers' claim].
>

## scaling-normalisation.7 (claim)

SRS's makers claim better reproducibility than rarefying.

- conf: not stated
- class: not stated
- holds: a makers' claim
- src: beuleImprovedNormalizationSpecies2020 (AB)
- trail: MB-01 §5.4

From the note:

> MB-01:B-0308 [5.4 Tests of which taxa differ in abundance] SRS's makers claim better reproducibility than rarefying (Beule 2020) [AB].
>

## scaling-normalisation.8 (claim)

In the review's summary, scaling methods (TMM, RLE, CSS, VST, SRS, Wrench) show some FDR and power benefits at small n (DESeq2) and come close to quantitative methods in a dysbiosis simulation, but are depth-sensitive for beta and alpha diversity under the null, assume most taxa unchanged, and DESeq2's FDR rises with n and uneven libraries; the summary table mixes evidence classes without a per-cell label.

- conf: not stated
- class: not stated
- holds: the review's summary by approach; differential abundance and beta diversity
- src: weissNormalizationMicrobialDifferential2017, schlossRarefactionCurrentlyBest2024, llorensricoBenchmarkingMicrobiomeTransformations2021
- trail: MB-01 §5.6, §Adversarial

From the note:

> MB-01:B-0320 [5.6 Summary by approach] | Approach | Shown to correct | Not shown to correct, or shown to fail | Measure (alpha / beta / DA) |
>
> MB-01:B-0328 [5.6 Summary by approach] | Scaling (TMM, RLE, CSS, VST, SRS, Wrench) | Some FDR and power benefits at small n (DESeq2); close to quantitative methods in a dysbiosis simulation | Depth-sensitive beta and alpha under null; assume most taxa unchanged; DESeq2 FDR rises with n and uneven libraries | DA; beta |
>
> MB-01:C-143 [warning: Adversarial critique, full findings] - Section 5.6 summary table: 'Shown to correct' cells mix makers' claims and simulation results with measured results without per-cell evidence class, so it reads closer to a method recommendation than the brief allows.
>

Not found in the cited text (where to look, not what is wrong): holds: review

## compositional-data.1 (claim)

A review argues that 16S data are compositions "at all stages" and should be analysed with log-ratios.

- conf: cont (marker)
- class: assert (marker)
- holds: a review
- src: gloorMicrobiomeDatasetsCompositional2017 (AB; assert; cont)
- trail: MB-01 §5.1

From the note:

> MB-01:I-0110 [5.1 Origins of the approaches] **Compositional data analysis.** A review argues that 16S data are compositions "at all stages" and should be analysed with log-ratios (Gloor 2017) [AB; assert; cont].
>

## compositional-data.2 (claim)

In the review's summary, compositional (log-ratio) approaches give ratio fold changes invariant to load and to multiplicative bias, and ANCOM and ALDEx2 are conservative, but Aitchison distances are depth-sensitive under the null, ANCOM-BC shows type I inflation in some settings, and results are sensitive to pseudocounts; the summary table mixes evidence classes without a per-cell label.

- conf: not stated
- class: not stated
- holds: the review's summary by approach; differential abundance and beta diversity
- src: mclarenConsistentCorrectableBias2019, nearingMicrobiomeDifferentialAbundance2022, schlossRarefactionCurrentlyBest2024, yangComprehensiveEvaluationMicrobial2022, kaulAnalysisMicrobiomeData2017
- trail: MB-01 §5.6, §Adversarial

From the note:

> MB-01:B-0320 [5.6 Summary by approach] | Approach | Shown to correct | Not shown to correct, or shown to fail | Measure (alpha / beta / DA) |
>
> MB-01:B-0323 [5.6 Summary by approach] | Compositional (log-ratio) | Ratio fold changes invariant to load and to multiplicative bias; ANCOM and ALDEx2 conservative | Aitchison distances depth-sensitive under null; ANCOM-BC type I inflation in some settings; pseudocount sensitivity | DA; beta |
>
> MB-01:C-143 [warning: Adversarial critique, full findings] - Section 5.6 summary table: 'Shown to correct' cells mix makers' claims and simulation results with measured results without per-cell evidence class, so it reads closer to a method recommendation than the brief allows.
>

Not found in the cited text (where to look, not what is wrong): holds: review

## richness.1 (claim)

Chao1, ACE, CatchAll, Shannon and Simpson all varied with library size in pyrosequencing data.

- conf: repl (marker)
- class: meas (marker)
- holds: pyrosequencing data
- src: gihringMassivelyParallelRRNA2012 (AB; meas; repl)
- trail: MB-01 §5.2

From the note:

> MB-01:I-0112 [5.2 Richness and other alpha diversity measures] **Depth dependence is replicated.** Chao1, ACE, CatchAll, Shannon and Simpson all varied with library size in pyrosequencing data (Gihring 2012) [AB; meas; repl].
>

## richness.2 (claim)

In Schloss's null models built from 12 V4 datasets, observed richness, Chao1, ACE, breakaway and SRS-normalised richness all correlated with depth.

- conf: cont (marker)
- class: model (marker)
- holds: null models from 12 V4 datasets
- src: schlossRarefactionCurrentlyBest2024 (FT, re-opened; model; cont)
- trail: MB-01 §5.2, §answers

From the note:

> MB-01:I-0113 [5.2 Richness and other alpha diversity measures] In Schloss's null models built from 12 V4 datasets, observed richness, Chao1, ACE, breakaway and SRS-normalised richness all correlated with depth (Schloss 2024b) [FT, re-opened; model; cont].
>
> MB-01:A-237 [quote: Answers as delivered] Richness estimators and extrapolation: Chao1, ACE and breakaway stayed correlated with depth, and breakaway intervals were too wide to be useful (Schloss 2024b).
>

## richness.3 (claim)

Shannon was less depth-sensitive and inverse Simpson was not depth-sensitive; Simpson-type indices are robust.

- conf: not stated
- class: not stated
- holds: Schloss 2024b's null models; Haegeman 2013
- src: schlossRarefactionCurrentlyBest2024, haegemanRobustEstimationMicrobial2013
- trail: MB-01 §5.2, §answers

From the note:

> MB-01:B-0268 [5.2 Richness and other alpha diversity measures] Shannon was less depth-sensitive and inverse Simpson was not depth-sensitive.
>
> MB-01:A-242 [quote: Answers as delivered] Shannon is less sensitive to depth and Simpson-type indices are robust (Schloss 2024b; Haegeman 2013).
>

Not found in the cited text (where to look, not what is wrong): holds: models

## richness.4 (claim)

The depth dependence of raw and estimator richness is replicated.

- conf: repl (note: "the depth dependence of raw and estimator richness is replicated")
- class: not stated
- holds: the three studies named
- src: gihringMassivelyParallelRRNA2012, schlossRarefactionCurrentlyBest2024, haegemanRobustEstimationMicrobial2013
- trail: MB-01 §answers

From the note:

> MB-01:A-274 [quote: Answers as delivered] Richness: the depth dependence of raw and estimator richness is replicated (Gihring 2012; Schloss 2024b; Haegeman 2013).
>

## richness.5 (claim)

In the synthesis agent's re-reading of the full text, coverage-based iNEXT estimates were among those that "showed a strong correlation between richness and the number of sequences", and the text exempts only "rarefaction and possibly the size-based iNEXT estimates"; this is the only microbial amplicon test of coverage-based standardisation found, and beyond it the evidence is non-microbial.

- conf: single (critic: MB-01:C-049)
- class: not stated
- holds: Schloss 2024b's null models
- src: schlossRarefactionCurrentlyBest2024
- trail: MB-01 §5.2, §answers, §critic, §Search record, §8. Answers

From the note:

> MB-01:B-0276 [5.2 Richness and other alpha diversity measures] - **Coverage-based iNEXT.** In the synthesis agent's re-reading of the full text, coverage-based iNEXT estimates were among those that "showed a strong correlation between richness and the number of sequences".
>
> MB-01:B-0277 [5.2 Richness and other alpha diversity measures] The text exempts "rarefaction and possibly the size-based iNEXT estimates".
>
> MB-01:B-0278 [5.2 Richness and other alpha diversity measures] This is the only microbial amplicon test of coverage-based standardisation found.
>
> MB-01:A-236 [quote: Answers as delivered] In Schloss 2024b's null models the coverage-based iNEXT estimates stayed correlated with depth (the synthesis agent's reading of the full text).
>
> MB-01:C-049 [danger: Critic: answers partly supported] Coverage-based standardisation has one microbial test (the Schloss 2024b null model, verified: all approaches 'except for rarefaction and possibly the size-based iNEXT estimates' remained depth-correlated).
>
> MB-01:C-050 [danger: Critic: answers partly supported] Beyond that, the evidence is non-microbial.
>
> MB-01:B-0374 [Search record] One correction resulted: the Schloss 2024b passage shows coverage-based iNEXT estimates remained correlated with depth.
>
> MB-01:A-313 [8. Answers in brief] Coverage-based standardisation has almost no microbial benchmark.
>

## richness.6 (claim)

Chao and Jost argue that standardising by sample completeness rather than size gives less biased richness ratios.

- conf: not stated
- class: model (marker)
- holds: indirect evidence
- src: chaoCoveragebasedRarefactionExtrapolation2012 (FT; model; INDIRECT)
- trail: MB-01 §5.1, §answers

From the note:

> MB-01:I-0107 [5.1 Origins of the approaches] **Coverage-based standardisation.** Chao and Jost argue that standardising by sample completeness rather than size gives less biased richness ratios (Chao and Jost 2012) [FT; model; INDIRECT].
>
> MB-01:A-234 [quote: Answers as delivered] Coverage-based standardisation: in ecology it is argued to give less biased richness ratios (Chao and Jost 2012, indirect).
>

## richness.7 (claim)

Hill-number extrapolation is reliable only to about 2 to 3 times the reference sample size for richness.

- conf: not stated
- class: model (marker)
- holds: indirect evidence
- src: chaoRarefactionExtrapolationHill2014 (FT; model; INDIRECT)
- trail: MB-01 §5.1, §answers

From the note:

> MB-01:I-0108 [5.1 Origins of the approaches] Hill-number extrapolation is reliable only to about 2 to 3 times the reference sample size for richness (Chao 2014) [FT; model; INDIRECT].
>
> MB-01:A-239 [quote: Answers as delivered] Extrapolation is reliable only to about 2-3 times the sample size (Chao 2014, indirect).
>

## richness.8 (claim)

A 2026 test on terrestrial inventories finds coverage-based rarefaction "does not respond predictably" to richness.

- conf: single (marker)
- class: model (marker)
- holds: terrestrial inventories, non-microbial, abstract only
- src: alroyCoveragebasedRarefactionFails2026 (AB; model; single; INDIRECT)
- trail: MB-01 §5.1, §answers

From the note:

> MB-01:I-0109 [5.1 Origins of the approaches] A 2026 test on terrestrial inventories finds coverage-based rarefaction "does not respond predictably" to richness (Alroy 2026) [AB; model; single; INDIRECT].
>
> MB-01:A-235 [quote: Answers as delivered] Alroy 2026 (abstract, non-microbial) finds it fails on terrestrial inventories.
>

## richness.9 (claim)

Coverage-based standardisation is disputed: Chao and Jost 2012 against Alroy 2026 (both non-microbial) and the microbial null model in Schloss 2024b.

- conf: not stated
- class: not stated
- holds: two non-microbial studies and one microbial null model
- src: chaoCoveragebasedRarefactionExtrapolation2012, alroyCoveragebasedRarefactionFails2026, schlossRarefactionCurrentlyBest2024
- trail: MB-01 §answers

From the note:

> MB-01:A-282 [quote: Answers as delivered] Coverage-based standardisation: Chao and Jost 2012 versus Alroy 2026 (both non-microbial) and the microbial null model in Schloss 2024b.
>

## richness.10 (claim)

In the review's summary, coverage-based standardisation compresses richness ratios less than size-based rarefaction (ecology, modelled) but fails on terrestrial inventories and is depth-correlated in a microbial null model.

- conf: not stated
- class: not stated
- holds: the review's summary by approach; alpha diversity
- src: chaoCoveragebasedRarefactionExtrapolation2012, alroyCoveragebasedRarefactionFails2026, schlossRarefactionCurrentlyBest2024
- trail: MB-01 §5.6

From the note:

> MB-01:B-0320 [5.6 Summary by approach] | Approach | Shown to correct | Not shown to correct, or shown to fail | Measure (alpha / beta / DA) |
>
> MB-01:B-0322 [5.6 Summary by approach] | Coverage-based standardisation | Compresses richness ratios less than size-based rarefaction (ecology, modelled) | Fails on terrestrial inventories (Alroy 2026); depth-correlated in a microbial null model (Schloss 2024b) | Alpha |
>

Not found in the cited text (where to look, not what is wrong): holds: review

## richness.11 (claim)

No independent microbial benchmark of coverage-based standardisation was found.

- conf: not stated
- class: search (note: "An independent microbial benchmark of coverage-based standardisation (statistics angle)")
- holds: the statistics angle's search
- src: none (a search result)
- trail: MB-01 §Search record, §Provenance
- search: searched, not found (note: "An independent microbial benchmark of coverage-based standardisation (statistics angle)")

From the note:

> MB-01:B-0383 [Search record] - An independent microbial benchmark of coverage-based standardisation (statistics angle).
>
> MB-01:B-0377 [Search record] Not found, with the routes used:
>
> MB-01:B-0017 [info: Provenance] Not found by any route: within-run CV of reads per sample; absolute per-cycle 16S efficiencies; measured (not predicted) community copy number by environment; 16S-specific index hopping on patterned flow cells; overdispersion fitted to 16S technical replicates; an independent microbial benchmark of coverage-based standardisation; abundance-distribution shapes reported separately for water and host.
>

## richness.12 (claim)

Willis argues that plug-in and rarefied richness are both negatively biased, and that rarefying can create false differences between environments with equal richness but different abundance structures; she recommends estimators with variance estimates compared through measurement-error models, and presents statistical argument plus a worked simulated example.

- conf: cont (marker)
- class: not stated (critic: MB-01:C-043)
- holds: a perspective
- src: willisRarefactionAlphaDiversity2019 (FT; cont; critic: MB-01:C-043 was "FT; assert; cont")
- trail: MB-01 §5.2, §answers, §critic, §Adversarial
- contrary: one-sided (critic: MB-01:C-126)

From the note:

> MB-01:B-0279 [5.2 Richness and other alpha diversity measures] **Arguments against rarefying for richness.** Willis argues that plug-in and rarefied richness are both negatively biased, and that rarefying can create false differences between environments with equal richness but different abundance structures.
>
> MB-01:I-0114 [5.2 Richness and other alpha diversity measures] She recommends estimators with variance estimates compared through measurement-error models (Willis 2019) [FT; assert; cont].
>
> MB-01:A-233 [quote: Answers as delivered] Willis 2019 (asserted) argues that rarefied and plug-in richness are both biased and that rarefying can create false differences.
>
> MB-01:C-043 [danger: Critic: answers partly supported] (1) Willis 2019 is labelled 'asserted', but it presents statistical argument plus a worked simulated example.
>
> MB-01:C-124 [warning: Adversarial critique, full findings] - D5: Willis 2019 (against rarefying for richness) is classed 'asserted' and described as 'contested by an assertion', but the paper gives statistical argument plus a worked simulated example.
>
> MB-01:C-125 [warning: Adversarial critique, full findings] Schloss's simulations are classed 'modelled'.
>
> MB-01:C-126 [warning: Adversarial critique, full findings] The evidence class is applied unevenly between the two sides.
>

## richness.13 (claim)

Breakaway and betta are offered by their makers as estimators with variance estimates.

- conf: not stated
- class: not stated
- holds: makers' claims
- src: willisEstimatingDiversityFrequency2015 (AB; makers' claims), willisImprovedDetectionChanges2017 (AB; makers' claims)
- trail: MB-01 §5.2

From the note:

> MB-01:B-0280 [5.2 Richness and other alpha diversity measures] Breakaway and betta are offered as such tools by their makers (Willis and Bunge 2015; Willis, Bunge and Whitman 2017) [AB; makers' claims].
>
> MB-01:I-0114 [5.2 Richness and other alpha diversity measures] She recommends estimators with variance estimates compared through measurement-error models (Willis 2019) [FT; assert; cont].
>

## richness.14 (claim)

Breakaway intervals were mostly too wide to be useful, and breakaway stayed correlated with depth.

- conf: not stated
- class: not stated
- holds: Schloss 2024b's null models
- src: schlossRarefactionCurrentlyBest2024
- trail: MB-01 §5.2, §answers

From the note:

> MB-01:B-0281 [5.2 Richness and other alpha diversity measures] Schloss 2024b found breakaway intervals mostly too wide to be useful.
>
> MB-01:A-237 [quote: Answers as delivered] Richness estimators and extrapolation: Chao1, ACE and breakaway stayed correlated with depth, and breakaway intervals were too wide to be useful (Schloss 2024b).
>

Not found in the cited text (where to look, not what is wrong): holds: models

## richness.15 (claim)

Sample data carry no information on the rare tail, and Chao's estimator ranked in silico communities wrongly: a community with 20 times fewer species was estimated to have 10 times more.

- conf: not stated
- class: not stated
- holds: in silico communities
- src: haegemanRobustEstimationMicrobial2013
- trail: MB-01 §5.2, §answers

From the note:

> MB-01:B-0282 [5.2 Richness and other alpha diversity measures] **Limits of richness estimators.**
>
> MB-01:B-0283 [5.2 Richness and other alpha diversity measures] - Sample data carry no information on the rare tail.
>
> MB-01:B-0284 [5.2 Richness and other alpha diversity measures] Chao's estimator ranked in silico communities wrongly: a community with 20 times fewer species was estimated to have 10 times more.
>
> MB-01:A-238 [quote: Answers as delivered] Tails are unidentifiable, and Chao's estimator mis-ranked communities (Haegeman 2013).
>

## richness.16 (claim)

Bounds for Hill numbers of order 2 and above nearly coincide, and the authors recommend Shannon and Simpson over richness.

- conf: repl (marker)
- class: model (marker)
- holds: Haegeman et al.'s analysis
- src: haegemanRobustEstimationMicrobial2013 (FT; model; repl)
- trail: MB-01 §5.2

From the note:

> MB-01:I-0115 [5.2 Richness and other alpha diversity measures] Bounds for Hill numbers of order 2 and above nearly coincide (Haegeman 2013) [FT; model; repl].
>
> MB-01:B-0285 [5.2 Richness and other alpha diversity measures] The authors recommend Shannon and Simpson over richness.
>

## richness.17 (claim)

Chao1 and ACE are invalid on ASV tables from algorithms that drop singletons, as DADA2 does by default.

- conf: single (marker)
- class: assert (marker)
- holds: ASV tables
- src: dengNonparametricRichnessEstimators2024 (FT; assert; single)
- trail: MB-01 §5.2, §answers

From the note:

> MB-01:I-0116 [5.2 Richness and other alpha diversity measures] - Chao1 and ACE are invalid on ASV tables from algorithms that drop singletons, as DADA2 does by default (Deng 2024) [FT; assert; single].
>
> MB-01:A-240 [quote: Answers as delivered] Chao1 and ACE are invalid on ASV tables with singletons removed (Deng 2024, asserted).
>

## richness.18 (claim)

Spurious OTUs severely inflated Chao1, and removing them severely underestimated Chao1 in uneven communities, while abundance-weighted metrics were little affected.

- conf: not stated
- class: not stated
- holds: Pinto and Raskin 2012
- src: pintoPCRBiasesDistort2012
- trail: MB-01 §5.2, §answers

From the note:

> MB-01:B-0286 [5.2 Richness and other alpha diversity measures] - Spurious OTUs severely inflated Chao1, and removing them severely underestimated Chao1 in uneven communities (Pinto and Raskin 2012).
>
> MB-01:A-079 [quote: Answers as delivered] Taxa: spurious OTUs severely inflated Chao1.
>
> MB-01:A-080 [quote: Answers as delivered] Abundance-weighted metrics were little affected (Pinto and Raskin 2012).
>
> MB-01:B-0071 [2. Steps from sample to table (D1) and departures from the sampled community (D2)] | Library prep, sequencing | Library prep and primers are the largest drivers of error profile | Spurious OTUs severely inflate Chao1 | Error rate rises with cluster density | Schirmer 2015; Kozich 2013; Pinto and Raskin 2012 |
>

## richness.19 (claim)

An abundance filter makes ACE and Chao1 inapplicable.

- conf: not stated
- class: not stated
- holds: Bokulich et al.'s quality filtering
- src: bokulichQualityfilteringVastlyImproves2013
- trail: MB-01 §5.2

From the note:

> MB-01:B-0287 [5.2 Richness and other alpha diversity measures] - An abundance filter makes ACE and Chao1 inapplicable (Bokulich 2013).
>

## richness.20 (claim)

Spurious singletons inflate richness estimators, and a singleton-replacement estimator for error-inflated data has been proposed.

- conf: single (marker)
- class: model (marker)
- holds: a proposed estimator
- src: chiuEstimatingComparingMicrobial2016 (AB; model; single), pintoPCRBiasesDistort2012
- trail: MB-01 §5.2, §answers

From the note:

> MB-01:I-0117 [5.2 Richness and other alpha diversity measures] - A singleton-replacement estimator for error-inflated data has been proposed (Chiu and Chao 2016) [AB; model; single].
>
> MB-01:A-241 [quote: Answers as delivered] Spurious singletons inflate them (Pinto and Raskin 2012; Chiu and Chao 2016).
>

## richness.21 (claim)

Multiplicative bias can make an uneven sample look more even, biasing Shannon and inverse Simpson.

- conf: not stated
- class: model (note: "(McLaren 2019) [model]")
- holds: McLaren et al.'s model
- src: mclarenConsistentCorrectableBias2019 (model)
- trail: MB-01 §5.2, §answers

From the note:

> MB-01:B-0288 [5.2 Richness and other alpha diversity measures] **Bias in the measurement.** Multiplicative bias can make an uneven sample look more even, biasing Shannon and inverse Simpson (McLaren 2019) [model].
>
> MB-01:A-252 [quote: Answers as delivered] Bias in measured relative abundance can make uneven samples look more even (McLaren 2019, modelled).
>

## richness.22 (claim)

PCR-bias calibration improved Shannon diversity in 7 of 10 mocks.

- conf: not stated
- class: not stated
- holds: 10 mocks
- src: silvermanMeasuringMitigatingPCR2021
- trail: MB-01 §5.2

From the note:

> MB-01:B-0289 [5.2 Richness and other alpha diversity measures] PCR-bias calibration improved Shannon in 7 of 10 mocks (Silverman 2021).
>

## richness.23 (claim)

In simulated faecal communities with load varying from 1.9 x 10^9 to 10^13 cells per gram, all 13 transformations reproduced Shannon and Simpson diversity.

- conf: not stated
- class: not stated
- holds: simulated faecal communities
- src: llorensricoBenchmarkingMicrobiomeTransformations2021
- trail: MB-01 §5.2

From the note:

> MB-01:B-0290 [5.2 Richness and other alpha diversity measures] **Absolute quantification.** In simulated faecal communities with load varying from 1.9 x 10^9 to 10^13 cells per gram, all 13 transformations reproduced Shannon and Simpson.
>

## richness.24 (claim)

In simulated faecal communities, richness was recovered reliably only by quantitative profiling in a bloom scenario.

- conf: single (marker)
- class: model (marker)
- holds: simulated faecal communities, bloom scenario
- src: llorensricoBenchmarkingMicrobiomeTransformations2021 (FT; model; single)
- trail: MB-01 §5.2, §answers

From the note:

> MB-01:I-0118 [5.2 Richness and other alpha diversity measures] Richness was recovered reliably only by quantitative profiling in a bloom scenario (Llorens-Rico 2021) [FT; model; single].
>
> MB-01:A-243 [quote: Answers as delivered] Absolute quantification: in a simulation, only quantitative profiling recovered richness in a bloom scenario (Llorens-Rico 2021, single source).
>
> MB-01:B-0290 [5.2 Richness and other alpha diversity measures] **Absolute quantification.** In simulated faecal communities with load varying from 1.9 x 10^9 to 10^13 cells per gram, all 13 transformations reproduced Shannon and Simpson.
>

## richness.25 (claim)

In freshwater and sediment 454 data, 5,000 sequences captured Shannon trends and over 80% of Chao1 trends.

- conf: single (marker)
- class: meas (marker)
- holds: freshwater and sediment, 454
- src: lundinWhichSequencingDepth2012 (AB; meas; single)
- trail: MB-01 §5.2

From the note:

> MB-01:I-0119 [5.2 Richness and other alpha diversity measures] **Bounding.** In freshwater and sediment 454 data, 5,000 sequences captured Shannon trends and over 80% of Chao1 trends (Lundin 2012) [AB; meas; single].
>

## richness.26 (claim)

In the review's summary, richness estimators give lower bounds and extrapolation to about 2 to 3 times sample size (ecology), but are depth-correlated, have unidentifiable tails, are invalid without singletons and are inflated by spurious singletons.

- conf: not stated
- class: not stated
- holds: the review's summary by approach; alpha diversity
- src: chaoRarefactionExtrapolationHill2014, haegemanRobustEstimationMicrobial2013, dengNonparametricRichnessEstimators2024, schlossRarefactionCurrentlyBest2024
- trail: MB-01 §5.6

From the note:

> MB-01:B-0320 [5.6 Summary by approach] | Approach | Shown to correct | Not shown to correct, or shown to fail | Measure (alpha / beta / DA) |
>
> MB-01:B-0327 [5.6 Summary by approach] | Richness estimators and extrapolation | Lower bounds; extrapolation to about 2 to 3x sample size (ecology) | Depth-correlated; tails unidentifiable; invalid without singletons; inflated by spurious singletons | Alpha |
>

Not found in the cited text (where to look, not what is wrong): 3; holds: review

## beta-diversity.1 (claim)

In Schloss's null models, Jaccard and Bray-Curtis computed from raw counts, relative abundances, CSS or SRS, Aitchison distances (four zero-handling variants) and DESeq2 VST Euclidean distances all correlated with depth differences; only rarefaction removed the correlation, and only rarefaction held 5% false positives in PERMANOVA under confounding.

- conf: not stated
- class: not stated
- holds: null models from 12 V4 datasets
- src: schlossRarefactionCurrentlyBest2024
- trail: MB-01 §5.3, §answers

From the note:

> MB-01:B-0291 [5.3 Beta diversity] **For rarefying.** In Schloss's null models, Jaccard and Bray-Curtis computed from raw counts, relative abundances, CSS or SRS, as well as Aitchison distances (four zero-handling variants) and DESeq2 VST Euclidean distances, all correlated with depth differences.
>
> MB-01:B-0292 [5.3 Beta diversity] Only rarefaction removed the correlation, and only rarefaction held 5% false positives in PERMANOVA under confounding (Schloss 2024b).
>
> MB-01:A-244 [quote: Answers as delivered] Beta diversity.
>
> MB-01:A-245 [quote: Answers as delivered] Rarefying: Schloss 2024b finds only rarefaction removed depth effects on Jaccard and Bray-Curtis; relative abundance, CSS, SRS, Aitchison and VST did not.
>
> MB-01:A-251 [quote: Answers as delivered] Log-ratio (Aitchison): depth-sensitive in Schloss 2024b.
>

Not found in the cited text (where to look, not what is wrong): holds: 12; holds: v4; holds: datasets

## beta-diversity.2 (claim)

Rarefying clustered samples better for presence/absence metrics, and other normalisations were vulnerable below about 1,000 reads per sample.

- conf: repl (marker)
- class: model (marker)
- holds: Weiss et al.'s simulations
- src: weissNormalizationMicrobialDifferential2017 (FT; model; repl)
- trail: MB-01 §5.3

From the note:

> MB-01:I-0120 [5.3 Beta diversity] In Weiss 2017, rarefying clustered samples better for presence/absence metrics, and other normalisations were vulnerable below about 1,000 reads per sample (Weiss 2017) [FT; model; repl].
>

Not found in the cited text (where to look, not what is wrong): holds: simulations

## beta-diversity.3 (claim)

In simulations from Global Patterns, rarefying to the 15th percentile and dropping samples below it reduced clustering accuracy.

- conf: cont (marker)
- class: model (marker)
- holds: simulations from Global Patterns
- src: mcmurdieWasteNotWant2014 (FT; model; cont)
- trail: MB-01 §5.3, §answers

From the note:

> MB-01:I-0121 [5.3 Beta diversity] **Against rarefying.** In simulations from Global Patterns, rarefying to the 15th percentile and dropping samples below it reduced clustering accuracy (McMurdie and Holmes 2014) [FT; model; cont].
>
> MB-01:A-246 [quote: Answers as delivered] McMurdie and Holmes 2014 found rarefying reduced clustering accuracy, and Schloss 2024a disputes their design.
>

## beta-diversity.4 (claim)

Schloss identified 11 design choices that disadvantaged rarefying in the McMurdie and Holmes study; notably, low-depth samples were removed only in the rarefied arm.

- conf: single (marker)
- class: model (marker)
- holds: a re-analysis of McMurdie and Holmes's simulations
- src: schlossWasteNotWant2024 (FT; model; single)
- trail: MB-01 §5.3, §answers

From the note:

> MB-01:B-0293 [5.3 Beta diversity] Schloss identified 11 design choices that disadvantaged rarefying in that study.
>
> MB-01:I-0122 [5.3 Beta diversity] Notably, low-depth samples were removed only in the rarefied arm (Schloss 2024a) [FT; model; single].
>
> MB-01:A-246 [quote: Answers as delivered] McMurdie and Holmes 2014 found rarefying reduced clustering accuracy, and Schloss 2024a disputes their design.
>

Not found in the cited text (where to look, not what is wrong): holds: re-analysis; holds: simulations

## beta-diversity.5 (claim)

Proportions and rarefying were the only methods that fully normalised depth, and scaling methods masked differences in common OTUs.

- conf: single (marker)
- class: model (marker)
- holds: an abstract
- src: mcknightMethodsNormalizingMicrobiome2019 (AB; model; single)
- trail: MB-01 §5.3, §answers

From the note:

> MB-01:I-0123 [5.3 Beta diversity] **Proportions.** Proportions and rarefying were the only methods that fully normalised depth; scaling methods masked differences in common OTUs (McKnight 2019) [AB; model; single].
>
> MB-01:A-249 [quote: Answers as delivered] Proportions: accurate for community comparisons according to McKnight 2019 (abstract), but still depth-sensitive under Schloss's null.
>

## beta-diversity.6 (claim)

Whether proportions normalise depth for beta diversity conflicts between studies: McKnight 2019 against Schloss 2024b, in which relative-abundance Bray-Curtis stayed depth-sensitive under the null.

- conf: cont (note: "This conflicts with Schloss 2024b")
- class: not stated
- holds: simulations
- src: mcknightMethodsNormalizingMicrobiome2019, schlossRarefactionCurrentlyBest2024
- trail: MB-01 §5.3, §answers, §6. Where

From the note:

> MB-01:B-0294 [5.3 Beta diversity] This conflicts with Schloss 2024b, in which relative-abundance Bray-Curtis stayed depth-sensitive.
>
> MB-01:A-249 [quote: Answers as delivered] Proportions: accurate for community comparisons according to McKnight 2019 (abstract), but still depth-sensitive under Schloss's null.
>
> MB-01:A-281 [quote: Answers as delivered] Proportions for beta: McKnight 2019 versus Schloss 2024b.
>
> MB-01:B-0341 [6. Where the evidence conflicts] Proportions for beta diversity: McKnight 2019 versus Schloss 2024b.
>

Not found in the cited text (where to look, not what is wrong): holds: simulations

## beta-diversity.7 (claim)

In real river data, rarefying barely changed Bray-Curtis or Jaccard (r > 0.9) and did not change weighted UniFrac.

- conf: not stated
- class: not stated
- holds: real river data
- src: chiarelloRankingBiasesChoice2022
- trail: MB-01 §5.3, §answers

From the note:

> MB-01:B-0295 [5.3 Beta diversity] **Real-data bounding results.**
>
> MB-01:B-0296 [5.3 Beta diversity] - Rarefying barely changed Bray-Curtis or Jaccard (r > 0.9) and did not change weighted UniFrac (Chiarello 2022).
>
> MB-01:A-247 [quote: Answers as delivered] Rarefying changed Bray-Curtis little (r > 0.9) in real river data (Chiarello 2022).
>

## beta-diversity.8 (claim)

Library-size normalisation had very little effect on beta-diversity separation compared with the choice of distance metric.

- conf: single (marker)
- class: meas (marker)
- holds: an abstract
- src: thorsenLargescaleBenchmarkingReveals2016 (AB; meas; single)
- trail: MB-01 §5.3, §answers

From the note:

> MB-01:I-0124 [5.3 Beta diversity] - Library-size normalisation had very little effect on beta-diversity separation compared with the choice of distance metric (Thorsen 2016) [AB; meas; single].
>
> MB-01:A-250 [quote: Answers as delivered] Library normalisation had very little effect on beta separation compared with the choice of metric (Thorsen 2016, abstract).
>

## beta-diversity.9 (claim)

1,000 denoised sequences explained 90% of the Bray-Curtis trends seen at 15,000 to 20,000 sequences.

- conf: not stated
- class: not stated
- holds: freshwater and sediment, 454
- src: lundinWhichSequencingDepth2012
- trail: MB-01 §5.3

From the note:

> MB-01:B-0297 [5.3 Beta diversity] - 1,000 denoised sequences explained 90% of the Bray-Curtis trends seen at 15,000 to 20,000 (Lundin 2012).
>
> MB-01:I-0119 [5.2 Richness and other alpha diversity measures] **Bounding.** In freshwater and sediment 454 data, 5,000 sequences captured Shannon trends and over 80% of Chao1 trends (Lundin 2012) [AB; meas; single].
>

## beta-diversity.10 (claim)

Bray-Curtis was usually the most powerful beta-diversity metric, and metric choice changes power.

- conf: single (marker)
- class: meas (marker)
- holds: an abstract
- src: kersPowerMicrobiomeStudies2022 (AB; meas; single)
- trail: MB-01 §5.3

From the note:

> MB-01:I-0126 [5.3 Beta diversity] Bray-Curtis was usually the most powerful metric, and metric choice changes power (Kers and Saccenti 2022) [AB; meas; single].
>

## beta-diversity.11 (claim)

Evidence on how to normalise for beta diversity is contested and simulation-based.

- conf: cont (note: "Beta: contested, simulation-based")
- class: not stated
- holds: simulations
- src: schlossRarefactionCurrentlyBest2024, mcmurdieWasteNotWant2014, weissNormalizationMicrobialDifferential2017
- trail: MB-01 §answers

From the note:

> MB-01:A-276 [quote: Answers as delivered] Beta: contested, simulation-based.
>

## differential-abundance.1 (claim)

Studies disagree on whether rarefying harms differential-abundance tests.

- conf: cont (note: "Studies disagree on whether rarefying harms differential-abundance tests")
- class: not stated
- holds: simulations and benchmarks
- src: mcmurdieWasteNotWant2014, weissNormalizationMicrobialDifferential2017, hongRarefyNotRarefy2022, yangComprehensiveEvaluationMicrobial2022
- trail: MB-01 §5.4, §answers

From the note:

> MB-01:B-0298 [5.4 Tests of which taxa differ in abundance] **Rarefying and proportions.** Studies disagree on whether rarefying harms differential-abundance tests.
>
> MB-01:A-253 [quote: Answers as delivered] Differential abundance.
>

Not found in the cited text (where to look, not what is wrong): holds: simulations

## differential-abundance.2 (claim)

Rarefied counts and proportions gave high false-positive rates, while DESeq2 and edgeR were near zero.

- conf: not stated
- class: not stated
- holds: McMurdie and Holmes's simulations
- src: mcmurdieWasteNotWant2014
- trail: MB-01 §5.4, §answers

From the note:

> MB-01:B-0299 [5.4 Tests of which taxa differ in abundance] - Rarefied counts and proportions gave high false-positive rates; DESeq2 and edgeR were near zero (McMurdie and Holmes 2014).
>
> MB-01:A-254 [quote: Answers as delivered] Rarefying versus proportions versus models: McMurdie and Holmes 2014 report high false-positive rates for both rarefying and proportions and near-zero rates for DESeq2 and edgeR.
>

Not found in the cited text (where to look, not what is wrong): holds: simulations

## differential-abundance.3 (claim)

Rarefying did not raise FDR for most methods, and lowered it at about 10x group differences in library size, at a cost in sensitivity.

- conf: not stated
- class: not stated
- holds: Weiss et al.'s simulations
- src: weissNormalizationMicrobialDifferential2017
- trail: MB-01 §5.4, §answers

From the note:

> MB-01:B-0300 [5.4 Tests of which taxa differ in abundance] - Rarefying did not raise FDR for most methods.
>
> MB-01:B-0301 [5.4 Tests of which taxa differ in abundance] It lowered FDR at about 10x group differences in library size, at a cost in sensitivity.
>
> MB-01:A-255 [quote: Answers as delivered] Weiss 2017 found rarefying did not raise FDR, and lowered it at about 10x library-size differences between groups, at a cost in sensitivity.
>

Not found in the cited text (where to look, not what is wrong): holds: simulations

## differential-abundance.4 (claim)

DESeq2's FDR rose with more samples or uneven libraries, and ANCOM alone controlled FDR well.

- conf: not stated
- class: not stated
- holds: Weiss et al.'s simulations
- src: weissNormalizationMicrobialDifferential2017
- trail: MB-01 §5.4, §answers

From the note:

> MB-01:B-0302 [5.4 Tests of which taxa differ in abundance] DESeq2's FDR rose with more samples or uneven libraries, and ANCOM alone controlled FDR well (Weiss 2017).
>
> MB-01:A-258 [quote: Answers as delivered] Compositional methods: ANCOM had the best FDR control in Weiss 2017.
>

Not found in the cited text (where to look, not what is wrong): holds: simulations

## differential-abundance.5 (claim)

Rarefying followed by permutation controls type I error; the sensitivity loss is negligible when overdispersion is high, and is summarised by a rarefaction efficiency index.

- conf: single (marker)
- class: model (marker)
- holds: Hong et al.'s analysis
- src: hongRarefyNotRarefy2022 (FT; model; single)
- trail: MB-01 §5.4, §answers

From the note:

> MB-01:I-0127 [5.4 Tests of which taxa differ in abundance] - Rarefying followed by permutation controls type I error. The sensitivity loss is negligible when overdispersion is high, and is summarised by a rarefaction efficiency index (Hong 2022) [FT; model; single].
>
> MB-01:A-256 [quote: Answers as delivered] Hong 2022 found rarefying plus permutation controls type I error, with a power cost that is negligible under high overdispersion.
>

## differential-abundance.6 (claim)

Tests on proportions at a tenfold depth difference had severe type I inflation, which rarefying controlled, and no method was "simultaneously robust, powerful, and flexible"; ANCOM-BC showed type I inflation in some settings.

- conf: repl (marker)
- class: model (marker)
- holds: Yang and Chen's simulations
- src: yangComprehensiveEvaluationMicrobial2022 (FT; model; repl)
- trail: MB-01 §5.4, §answers

From the note:

> MB-01:I-0128 [5.4 Tests of which taxa differ in abundance] - Tests on proportions at a tenfold depth difference had severe type I inflation, which rarefying controlled. No method was "simultaneously robust, powerful, and flexible" (Yang and Chen 2022) [FT; model; repl].
>
> MB-01:A-257 [quote: Answers as delivered] With a tenfold depth difference, tests on proportions had severe type I inflation that rarefying controlled (Yang and Chen 2022).
>
> MB-01:A-260 [quote: Answers as delivered] ANCOM-BC showed type I inflation in some settings (Yang and Chen 2022) and controlled FDR only at 200 or more samples per group (Wirbel 2024).
>

Not found in the cited text (where to look, not what is wrong): holds: simulations

## differential-abundance.7 (claim)

Fourteen differential-abundance methods on 38 datasets gave 0.8% to 40.5% significant ASVs (unfiltered means).

- conf: not stated
- class: not stated
- holds: 38 real datasets
- src: nearingMicrobiomeDifferentialAbundance2022
- trail: MB-01 §5.4, §answers

From the note:

> MB-01:B-0303 [5.4 Tests of which taxa differ in abundance] **Agreement among methods on real data.** Fourteen methods on 38 datasets gave 0.8% to 40.5% significant ASVs (unfiltered means).
>
> MB-01:A-264 [quote: Answers as delivered] The 14 methods gave 0.8% to 40.5% significant ASVs on the same data (Nearing 2022).
>

## differential-abundance.8 (claim)

ALDEx2 and ANCOM-II were the most consistent across 38 datasets, and edgeR and LEfSe produced many false positives on random splits.

- conf: single (marker)
- class: meas (marker)
- holds: 38 real datasets
- src: nearingMicrobiomeDifferentialAbundance2022 (FT; meas; single)
- trail: MB-01 §5.4, §answers

From the note:

> MB-01:I-0129 [5.4 Tests of which taxa differ in abundance] ALDEx2 and ANCOM-II were the most consistent. edgeR and LEfSe produced many false positives on random splits (Nearing 2022) [FT; meas; single].
>
> MB-01:A-259 [quote: Answers as delivered] ALDEx2 and ANCOM-II were the most consistent across 38 datasets (Nearing 2022).
>

## differential-abundance.9 (claim)

Excess false discoveries were widespread across differential-abundance methods.

- conf: repl (marker)
- class: model (marker)
- holds: an abstract
- src: hawinkelBrokenPromiseMicrobiome2019 (AB; model; repl)
- trail: MB-01 §5.4, §answers

From the note:

> MB-01:I-0130 [5.4 Tests of which taxa differ in abundance] Excess false discoveries were widespread across methods (Hawinkel 2019) [AB; model; repl].
>
> MB-01:A-265 [quote: Answers as delivered] Excess false discoveries are widespread (Hawinkel 2019, abstract).
>

## differential-abundance.10 (claim)

Methods with the highest false-positive rates had the most power.

- conf: not stated
- class: not stated
- holds: Thorsen et al.'s benchmark
- src: thorsenLargescaleBenchmarkingReveals2016
- trail: MB-01 §5.4

From the note:

> MB-01:B-0304 [5.4 Tests of which taxa differ in abundance] Methods with the highest false-positive rates had the most power (Thorsen 2016).
>

## differential-abundance.11 (claim)

Microbiome-specific methods did not beat RNA-seq methods.

- conf: single (marker)
- class: meas (marker)
- holds: an abstract
- src: calgaroAssessmentStatisticalMethods2020 (AB; meas; single)
- trail: MB-01 §5.4

From the note:

> MB-01:I-0131 [5.4 Tests of which taxa differ in abundance] Microbiome-specific methods did not beat RNA-seq methods (Calgaro 2020) [AB; meas; single].
>

