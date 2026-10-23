# Claims to edit, one edit each, of the type named

**Edit type: hedge**

## 16S/scaling-normalisation.1

Total-count scaling can bias differential-expression estimates in RNA-seq; TMM and DESeq's negative binomial model also come from RNA-seq, and both assume most features are unchanged between conditions.

- conf: not stated
- class: not stated
- holds: RNA-seq, labelled INDIRECT; abstracts only
- src: bullardEvaluationStatisticalMethods2010 (AB; INDIRECT), robinsonScalingNormalizationMethod2010 (AB; INDIRECT), andersDifferentialExpressionAnalysis2010 (AB; INDIRECT), weissNormalizationMicrobialDifferential2017
- trail: MB-01 §5.1, §answers

From the note:

> **Scaling normalisation.** Total-count scaling can bias differential-expression estimates in RNA-seq (Bullard 2010) [AB; INDIRECT].
>
> TMM (Robinson and Oshlack 2010) and DESeq's negative binomial model (Anders and Huber 2010) also come from RNA-seq [AB; INDIRECT].
>
> Weiss 2017 notes that both assume most features are unchanged between conditions.
>
> Scaling normalisations (TMM, RLE, CSS, VST, SRS, Wrench) come from RNA-seq (Bullard 2010; Robinson and Oshlack 2010; Anders and Huber 2010, indirect) and assume most features do not change.
>

**Edit type: hedge**

## GHOST/benchmark-regime.3

The dominance of propagation on standard benchmarks may be an artefact of the benchmarks, not a regime-general property.

- conf: not stated
- class: reading (note: "so the dominance of propagation on standard benchmarks may be an artifact")
- holds: the review's inference from R7's result on sparse benchmarks
- src: ferriniRethinkingGNNsMissing2026
- trail: GHOST §Verdict

From the note:

> **A 2026 result proves the benchmark itself hides the differences.** High feature sparsity provably bounds the information loss from missingness, "making all models appear robust and preventing a meaningful comparison" — so the dominance of propagation on standard benchmarks may be an artifact, not a regime-general property [R7].
>

**Edit type: hedge**

## 16S/abundance-occupancy.2

Nemergut's authors note that abundant taxa may simply be easier to detect, and that undersampling could hide intermediate distributions.

- conf: not stated
- class: not stated
- holds: the same study
- src: nemergutGlobalPatternsBiogeography2011
- trail: MB-02 §D3.2, §answers

From the note:

> - The authors note that abundant taxa may simply be easier to detect, and that undersampling could hide intermediate distributions.
>
> Sampling and detection: the authors of [62] note abundant taxa may simply be easier to detect.
>

**Edit type: hedge**

## H1-RES/redundancy.16

The counter-evidence bounds soil redundancy rather than overturning it: function and taxonomy are reported to covary closely where environments differ most strongly (across biomes, precipitation extremes and contamination gradients), so redundancy is real within moderate environmental ranges but appears to weaken as environmental contrast grows, with selection then shaping taxa and functions together.

- conf: not stated
- class: reading (note: "Synthesis written from the eleven studies tabulated above")
- holds: the eleven soil studies; the synthesis was written manually, not by the research round
- src: fiererCrossbiomeMetagenomicAnalyses2012, tripathiTrendsTaxonomicFunctional2017, renComparisonMicrobialTaxonomic2016
- trail: H1-RES §Assessment: redundancy

From the note:

> *(Synthesis written from the eleven studies tabulated above; the round did not reach this synthesis itself.)*
>
> The counter-evidence does not overturn this but bounds it, and the bound matters for this project specifically.
>
> Function and taxonomy are reported to covary closely precisely where environments differ most strongly: across whole biomes (Fierer et al., 2012 [8]), across precipitation extremes (Tripathi et al., 2017 [9]), and along contamination gradients (Ren et al., 2016 [11]).
>
> In other words, redundancy is real within moderate environmental ranges but appears to weaken as the environmental contrast grows, with selection then shaping taxa and functions together.
>

**Edit type: hedge**

## H1-RES/n-cycle-hgt.13

Anand & Chanway (2013), in *Paenibacillus polymyxa* strain P2b-2R, found phylogenetic analyses suggesting nifH was transmitted horizontally and nifD vertically, a gene-specific pattern within the same operon.

- conf: not stated
- class: not stated
- holds: one strain
- src: anand2013
- trail: H1-RES §Counter-Evidence: Vertical

From the note:

> Anand & Chanway (2013) analyzed *Paenibacillus polymyxa* strain P2b-2R and found that phylogenetic analyses suggested nifH was transmitted horizontally while nifD was transmitted vertically, indicating gene-specific evolutionary patterns within the same operon [20].
>

**Edit type: hedge**

## H1-02/same-sample-isolate.5

The paper attributes the low-identity share of missed genes to sequence divergence from the isolate or to assembly errors, so part of the loss may be biology and not recovery.

- conf: not stated
- class: not stated
- holds: the critic's reading of the full text of Meziti et al.
- src: mezitiReliabilityMetagenomeassembledGenomes2021
- trail: H1-02 §critic, §Adversarial critique

From the note:

> The low-identity share of missed genes is attributed to sequence divergence from the isolate or to assembly errors.
>
> [1] attributes low-identity missed genes to sequence differences from the isolate or to assembly errors, so part of the 'loss' may be biology and not recovery.
>

**Edit type: hedge**

## NFERT/mineralisation.2

Quantifying soil nitrogen supply can improve fertiliser-use efficiency and trim rates, but the lever is the measured soil supply, not a demonstrated property of microbial-community efficiency.

- conf: not stated
- class: not stated
- holds: stated by the reviewer after St. Luce et al.
- src: stluceNitrogenDynamicsIndices2011
- trail: NFERT §The weak channel

From the note:

> Quantifying soil nitrogen supply can improve fertiliser-use efficiency and trim rates, but the lever is the measured soil supply, not a demonstrated property of microbial-community efficiency.
>

**Edit type: hedge**

## H1-RES/n-cycle-hgt.8

Garbeva et al. (2007) detected nirK and norB in *Nitrosospira* species, with phylogenetic analysis suggesting lateral transfer of these denitrification genes into ammonia-oxidising bacteria; in some strains they were not phylogenetically distinct from classical denitrifiers and appeared less conserved than 16S rRNA or amoA genes.

- conf: not stated
- class: not stated
- holds: *Nitrosospira* species
- src: garbeva2007
- trail: H1-RES §Multi-Level HGT

From the note:

> Garbeva et al. (2007) detected nirK and norB in *Nitrosospira* species, with phylogenetic analysis suggesting lateral transfer of these denitrification genes into ammonia-oxidizing bacteria [7].
>
> The nirK and norB sequences from some *Nitrosospira* strains were not phylogenetically distinct from classical denitrifiers, and these genes appeared less conserved than 16S rRNA or amoA genes [7].
>

**Edit type: counter**

## 16S/copy-number-correction.9

Correction changed the identity of the most abundant OTU in about 20% of Human Microbiome Project and 31% of Earth Microbiome Project communities, but against predicted, not measured, truth; in simulations it reduced sample shifts in ordinations but left PERMANOVA variance explained essentially unchanged (5.27 to 19.65% true versus 5.27 to 19.82% uncorrected).

- conf: not stated
- class: not stated
- holds: HMP and EMP communities and simulations; the only figures on how often correction changes the dominant taxon in real communities
- src: gaoAccounting16SRRNA2023 (FT)
- trail: MB-02 §D1.4, §answers, §critic

From the note:

> - **Dominant taxa and ordinations.** Correction changed the most abundant OTU in about 20% of Human Microbiome Project communities and 31% of Earth Microbiome Project communities [33, FT].
>
> In simulations it reduced sample shifts in ordinations but left PERMANOVA variance explained essentially unchanged (5.27 to 19.65% true versus 5.27 to 19.82% uncorrected).
>
> Effects on ecological conclusions are mixed: correction changed the most abundant OTU in about 20% (human) and 31% (Earth Microbiome Project) of communities but left PERMANOVA variance explained essentially unchanged [33]; it changed human body-site clustering but not ocean clustering [28]; it changed enterotype number from two to three [29]; in a forest soil example Acidobacteria rose from 50.1% of sequences to an estimated 66.0% of genomes [6].
>
> Gao and Wu also report that correction changes dominant taxa but not beta-diversity test results, so both camps' observations can hold together.
>
> The only figures on how often correction changes the dominant taxon in real communities rest on Gao and Wu 2023 [33].
>
> It changes dominant taxa often (20 to 31%) but rarely changes beta-diversity test results [33].
>
> Correction changes the identity of the dominant OTU in about 20 to 31% of HMP and EMP communities, but against predicted, not measured, truth.
>
> It barely changes PERMANOVA in simulations [33].
>

**Edit type: counter**

## CB2/linking-tools.1

Linking tools recover part but not most of the gap: MarkerMAG, on benchmark datasets at 100% linking accuracy, recovered 88.2% (15/17 MAGs, low-complexity MBARC-26), 53.5% (23/43, medium) and 46.7% (14/30, high complexity); on real data the improvement over baseline ranged from 1.1-fold (macroalgae) to 14.2-fold (pig gut).

- conf: not stated
- class: not stated
- holds: benchmark datasets of three complexities; real data from macroalgae to pig gut
- src: songMarkerMAGLinkingMetagenomeassembled2022 (single-pass extraction of the article HTML)
- trail: CB2-RRNA §4. Bounding facts

From the note:

> **Linking tools recover part but not most of the gap.** MarkerMAG, on benchmark datasets at 100% linking accuracy, recovered 88.2% (15/17 MAGs, low-complexity MBARC-26), 53.5% (23/43, medium) and 46.7% (14/30, high complexity); on real data the improvement over baseline ranged from 1.1-fold (macroalgae) to 14.2-fold (pig gut).
>
> These figures come from a single-pass extraction of the article HTML.
>

**Edit type: counter**

## 16S/ploidy.11

Single-cell measurements in H. salinarum showed wide cell-to-cell variation in genome copy number, larger in exponential than in stationary phase; the review read only the abstract, which gives no per-cell shares, although the open full text reports single-cell CLSM and FACS distributions.

- conf: not stated
- class: not stated
- holds: H. salinarum cultures
- limit: access (critic: MB-02:C-071)
- src: breuertRegulatedPolyploidyHalophilic2006 (AB)
- trail: MB-02 §D1.3, §Adversarial

From the note:

> Single-cell measurements in H. salinarum showed wide cell-to-cell variation in copy number, larger in exponential than in stationary phase [14, AB]; the abstract gives no per-cell shares.
>
> - Breuert et al. 2006 [14] is open in PMC (PMC1762399; Europe PMC fullTextXML works) but labelled AB.
>
> Its full text reports single-cell CLSM and FACS distributions of genome copy number in H. salinarum, which bear directly on the brief's 'share of cells' question.
>
> The review states that 'the abstract gives no per-cell shares' without trying the full text.
>

**Edit type: counter**

## H2-04/within-between-partition.9

The plant partitions are measured and partly replicated, but concern species traits, not gene content.

- conf: not stated
- class: meas (note: "The plant partitions are measured")
- holds: plant trait ecology
- src: none (the review's assessment of the plant sources)
- trail: H2-04 §answers

From the note:

> The plant partitions are measured and partly replicated but concern species traits, not gene content..
>

**Edit type: counter**

## H2-01/levels-within.4

On a macroalgal host, similarity was about 15% in species composition against 70% in COG composition; the contrast compares a species table with a coarser COG table, and the taxonomic figure is from an earlier study.

- conf: not stated
- class: meas (marker)
- holds: one macroalgal host
- src: burkeBacterialCommunityAssembly2011 (FT; measured)
- trail: H2-01 §4.1

From the note:

> - A macroalgal host: about 15% similarity in species composition against 70% in COG composition [Burke2011; FT; measured].
>
> The contrast compares a species table with a coarser COG table, and the taxonomic figure is from an earlier study.
>

**Edit type: counter**

## H2-01/taxonomy-fixed.2

Salazar2019 separate regulatory change (metatranscriptome) from community turnover in the ocean, and per the search agent's reading turnover dominated at global scale; this concerns expression, not gene content.

- conf: not stated
- class: not stated
- holds: global ocean, metatranscriptomes
- src: salazarGeneExpressionChanges2019 (FT)
- trail: H2-01 §4.3

From the note:

> Salazar et al. (2019) separate regulatory change (metatranscriptome) from community turnover in the ocean; per the search agent's reading, turnover dominated at global scale.
>
> That is the nearest item and concerns expression, not gene content.
>

**Edit type: counter**

## H1-02/filters-corrections.5

CELEBRIMBOR was validated on simulations, and the authors state that non-random loss violates its missing-at-random assumption.

- conf: not stated
- class: not stated
- holds: simulations
- src: hellewellCELEBRIMBORCoreAccessory2024
- trail: H1-02 §2.7

From the note:

> CELEBRIMBOR [19] was validated on simulations, and the authors state that non-random loss violates its missing-at-random assumption. mOTUpan [14] was checked against a few closed Prochlorococcus genomes plus bootstraps, and its authors state that genes hard to assemble or bin leave "an inevitable underestimate of the accessory genomes".
>

**Edit type: counter**

## 16S/sampling-storage.5

Storage of a single soil for 1 to 14 days at room temperature, 4 C or -20 C changed its community, most at 3 to 7 days and least when frozen; these changes were small relative to differences among more than 500 Earth Microbiome Project soils.

- conf: repl (marker)
- class: meas (marker)
- holds: one soil, 1 to 14 days, three temperatures, compared with more than 500 EMP soils; not shown for other soils
- src: rubinInvestigatingImpactStorage2013 (FT; meas; repl), lauberEffectStorageConditions2010 (SEC)
- trail: MB-01 §2.1, §answers, §7. Bounds

From the note:

> **Soil.** Storage for 1 to 14 days at room temperature, 4 C or -20 C changed a single soil's community, most at 3 to 7 days and least when frozen.
>
> These changes were small relative to differences among more than 500 Earth Microbiome Project soils (Rubin 2013) [FT; meas; repl].
>
> In soil, storage effects were small compared with differences between soils (Rubin 2013; single soil).
>
> - storage, relative to between-soil differences (Rubin 2013);
>
> Lauber et al. 2010 is known only through Rubin's description (SEC; see Sources not obtained).
>

**Edit type: counter**

## 16S/relic-dna.2

Relic DNA averaged 33% (over 80% in some samples) across soil, sediment, water and mammalian gut but had minimal effect on diversity estimates; models predict bias only when relic and intact abundance distributions differ.

- conf: cont (marker)
- class: meas (marker)
- holds: soil, sediment, water and mammalian gut
- src: lennonHowWhereRelic2018 (FT; meas; cont)
- trail: MB-01 §2.2, §7. Bounds, MB-02 §D3.3

From the note:

> - Relic DNA averaged 33% across soil, sediment, water and mammalian gut but had minimal effect on diversity estimates. Models predict bias only when relic and intact abundance distributions differ (Lennon 2018) [FT; meas; cont].
>
> - relic DNA in one multi-environment study (Lennon 2018);
>
> - Lennon et al. 2018 [78, AB]: across soil, sediment, water and gut, relic DNA averaged 33% (over 80% in some samples) but had minimal effect on diversity estimates.
>

**Edit type: counter**

## H2-01/other-field-transfer.1

Sparse module dictionaries learned on 5% of samples recovered expression of the same TCGA tumour type at about 87% (Spearman, SMAF), and a dictionary from a different tumour type gave 68% on average, related tumour types doing better; this is recovery of expression from 25 random composite measurements through a learned dictionary (compressed sensing), not a direct covariance-reproduction score.

- conf: single (marker)
- class: meas (marker)
- holds: TCGA tumour types (other field); simulated random composite measurements, m = 25, g = 5,000; the only other-field test found that withholds a biologically distinct group (the closest analogue of a habitat)
- src: clearyEfficientGenerationTranscriptomic2017 (FT; measured; SINGLE SOURCE)
- trail: H2-01 §3.4, §critic, §answers

From the note:

> - **Withheld tissue type (the closest analogue of a withheld habitat).** Sparse module dictionaries learned on 5% of samples recovered held-out profiles of the same TCGA tumour type at about 87% (Spearman, SMAF).
>
> A dictionary from a different tumour type gave 68% on average, and related tumour types did better [Cleary2017; FT; measured; SINGLE SOURCE].
>
> Module dictionaries went from about 87% recovery within a tumour type to 68% across types, better for related types [Cleary2017].
>
> Removing Cleary2017 leaves no other-field test that withholds a biologically distinct group (the closest analogue of a habitat)..
>
> Cleary2017's 87% to 68% is recovery of expression from 25 random composite measurements through a learned dictionary (compressed sensing).
>
> It is not a direct covariance-reproduction score, and the answer should say so.
>
> - Cleary2017: the 87% to 68% figures are correct, but the review describes them as dictionaries that 'recovered held-out profiles'.
>
> They are Spearman recovery from 25 simulated random composite measurements through the dictionary (compressed sensing, m = 25, g = 5,000).
>
> The answer states the transfer more directly than the full text supports.
>

**Edit type: counter**

## H2-01/transfer-dependencies.1

There is no direct conflict on the same quantity: reproduction is high in some tests (Subramanian 81%; Chen reductive TCA 94.7%) and low in others (Cleary cross-type drop; pooled networks in Pierson; sign reversals across scales in plant traits).

- conf: not stated
- class: not stated
- holds: tests of different quantities in different fields
- src: subramanianNextGenerationConnectivity2017 (FT), chenGutMicrobialCoabundance2020 (FT), clearyEfficientGenerationTranscriptomic2017 (FT), piersonSharingSpecificityCoexpression2015 (FT), andereggWithinspeciesPatternsChallenge2018 (AB)
- trail: H2-01 §answers

From the note:

> *Conflicts:* No direct conflict on the same quantity.
>
> Reproduction is high in some tests (Subramanian 81%; Chen reductive TCA 94.7%) and low in others (Cleary cross-type drop; pooled networks in Pierson; sign reversals across scales in plant traits [Anderegg2018]); the differences track how different the target is from the training data..
>

**Edit type: counter**

## CB1/scarcity-claim.7

Two observations could be read as consistent with scarcity but do not evidence it: USGS's urban shortages are planning and land-use pressure, and Beerling et al.'s reliance on existing crushed-limestone infrastructure implies a mature, large-scale extractive industry, which cuts against scarcity rather than for it.

- conf: not stated
- class: reading (note: "Indirect support, labelled as such")
- holds: indirect evidence
- src: willettStoneCrushed2025, beerlingPotentialLargescaleCO22020
- trail: CB1-LIMING §Verdict on the scarcity

From the note:

> **Indirect support, labelled as such.** Two observations could be read as *consistent with* scarcity but do not evidence it.
>
> USGS notes shortages in urban and industrialised areas driven by zoning and land-development competition, pushing quarries further from demand [3] — that is planning and land-use pressure, and USGS presents it as a price driver, not a reserve limitation.
>
> And Beerling et al.'s reliance on existing crushed-limestone infrastructure to argue enhanced weathering is deployable [9] implies a mature, large-scale extractive industry, which cuts against scarcity rather than for it.
>

**Edit type: setting**

## GHOST/feature-propagation.3

FP outperformed prior missing-feature methods on its seven benchmarks.

- conf: not stated
- class: not stated
- holds: seven benchmarks, 2022; homophilous + sparse + MCAR, and mostly author-reported
- src: rossiUnreasonableEffectivenessFeature2022
- trail: GHOST §2. Degradation

From the note:

> - FP: on average ~4% relative node-classification accuracy drop at **99% missing** across seven benchmarks; it outperformed prior missing-feature methods on those benchmarks [R1].
>
> **Caveat carried on every number above:** homophilous + sparse + MCAR, and mostly author-reported.
>

**Edit type: setting**

## TSL/altitude-ordering.6

One taxonomy-induction framework (Yang & Callan 2009) abandons a single fixed altitude signal and learns a separate information function per abstraction level: different feature sets win at different levels (co-occurrence alone for abstract L2–L3; contextual + co-occurrence + pattern + syntactic for concrete L4–L6), so no single fixed signal serves all altitudes.

- conf: not stated
- class: not stated
- holds: is-a taxonomy induction, not cluster-label ordering
- src: yangMetricbasedFrameworkAutomatic2009 (Indirect)
- trail: TSL §Verdict, §2. How multi-level
- rating: "Confidence: high (3-0)"

From the note:

> One taxonomy-induction framework [S5] abandons a single fixed altitude signal entirely, learning a separate information function per abstraction level.
>
> - **Learned, per-level information functions** [S5]: Yang & Callan (2009) found different feature sets win at different abstraction levels (co-occurrence alone for abstract L2–L3; contextual+co-occurrence+pattern+syntactic for concrete L4–L6) — i.e. no single fixed signal serves all altitudes.
>
> *Confidence: high (3-0).
>
> Indirect:* this is is-a taxonomy induction, not cluster-label ordering.
>

**Edit type: setting**

## CB2/marker-gap.1

In SMAG, 3,641 MAGs were high quality with rRNA, and a further 5,184 MAGs reached ≥90% completeness and <5% contamination but failed on "the absence of all rRNA genes or less than 18 tRNAs".

- conf: not stated
- class: not stated
- holds: soil (SMAG)
- src: maGenomicCatalogueSoil2023
- trail: CB2-RRNA §2. Side by side

From the note:

> - **Soil (SMAG).** 3,641 MAGs were high quality *with* rRNA; a further 5,184 MAGs reached ≥90% completeness and <5% contamination but failed on "the absence of all rRNA genes or less than 18 tRNAs".
>

**Edit type: setting**

## CB3/gwp-metric.4

Lynch et al. do not offer a replacement share; the criticism attacks the aggregation, not the inventory.

- conf: not stated
- class: not stated
- holds: Lynch et al. 2021 as the review read it
- src: lynchAgricultureSContribution2021
- trail: CB3-AG-EMISSIONS §Bounding and negative facts

From the note:

> They do not offer a replacement *share*; the criticism attacks the aggregation, not the inventory.
>

**Edit type: standing**

## H1-02/artefact-size.5

One natural biocrust soil shows systematic short-read assembly loss of variable regions, which is indirect support only for soil.

- conf: not stated
- class: not stated
- holds: one natural biocrust soil; assembly loss, not gene content of recovered genomes
- src: bergComparisonShortreadLongread2025
- trail: H1-02 §Verdict as delivered, §5. Verdicts

From the note:

> One natural biocrust soil shows systematic short-read assembly loss of variable regions [26], which is indirect support only.
>
> Berg et al. [26] is indirect support.
>

**Edit type: standing**

## 16S/compositional-analysis.4

Proportion-based differential-abundance results err when the community's mean efficiency is associated with the condition.

- conf: single (marker)
- class: model (marker)
- holds: preprint abstract
- src: mclarenImplicationsTaxonomicBias2022 (AB; PREPRINT; model; single)
- trail: MB-01 §5.4, §answers

From the note:

> Proportion-based differential-abundance results err when the community's mean efficiency is associated with the condition (McLaren 2022) [AB; PREPRINT; model; single].
>
> Ratio-based analyses are invariant to multiplicative bias, whereas proportion-based ones are biased when community mean efficiency tracks the condition (McLaren 2019; McLaren 2022 preprint).
>

**Edit type: standing**

## H1-RES/redundancy.11

Tripathi et al. (2017): distinct taxonomic and functional communities were observed across precipitation zones in Israel, with lower functional diversity in arid environments, showing coordinated taxonomic and functional shifts with climate.

- conf: not stated
- class: not stated
- holds: a precipitation gradient in Israel
- src: tripathiTrendsTaxonomicFunctional2017
- trail: H1-RES §Soil counter-evidence

From the note:

> |  Trends in taxonomic and functional composition of soil microbiome along a precipitation gradient in Israel, Binu M.
>
> Tripathi et al., 2017  | Distinct taxonomic and functional communities were observed across precipitation zones; functional diversity was lower in arid environments, demonstrating coordinated taxonomic and functional shifts with climate [9].  |
>

**Edit type: standing**

## H1-02/artefact-size.6

Removing Meziti et al. would leave Part A as measured and material on Majernik et al. and Orellana et al., but would remove the only natural same-sample isolate comparison and every figure for missed core and variable genes, since Li and Yin reuse its data.

- conf: not stated
- class: not stated
- holds: the review's sensitivity analysis
- src: mezitiReliabilityMetagenomeassembledGenomes2021, majernikSmallAmountsMisassembly2025, orellanaComparingGenomesRecovered2023, liCriticalAssessmentPangenomic2022
- trail: H1-02 §5. Verdicts

From the note:

> **Sensitivity to single sources.** Removing Meziti et al. [1] would leave Part A as "measured and material" on [22] and [12], but would remove the only natural same-sample isolate comparison and every figure for missed core and variable genes ([2] reuses [1]'s data).
>

**Edit type: number**

## H1-06/depth-dependence.1

In 2,730 marine genomes, chitinase tau_D was 0.0281 on a 16S tree and 0.0444 on a core-gene tree, three to five times Zimmerman's 0.008.

- conf: not stated
- class: not stated
- holds: marine genomes (Sun 2021) against Zimmerman's 3,058 genomes
- src: sunPhylogeneticDistributionPolysaccharideDegrading2021, zimmermanMicrodiversityExtracellularEnzyme2013
- trail: H1-06 §3. Part A2, §answers

From the note:

> **Dataset and tree dependence.** In 2,730 marine genomes, chitinase tau_D was 0.0281 on a 16S tree and 0.0444 on a core-gene tree [4], three to five times Zimmerman's 0.008 [2].
>
> Absolute depths for the same trait differ between datasets and trees: chitinase 0.008 (Zimmerman 2013) against 0.028 on a 16S tree and 0.044 on a core-gene tree (Sun 2021).
>

**Edit type: number**

## TSL/c-tf-idf.1

c-TF-IDF (BERTopic, Grootendorst 2022) treats each cluster as one document, L1-normalises tf for cluster size, and down-weights via log(1 + A/f_t).

- conf: not stated
- class: not stated
- holds: BERTopic's class-based TF-IDF procedure, as described in the paper and its documentation
- src: grootendorstBERTopicNeuralTopic2022, anonCTFIDFDocumentation
- trail: TSL §1. Specificity signals
- rating: "Confidence: high (3-0)"

From the note:

> - **Class/group df — c-TF-IDF** [S3] — BERTopic (Grootendorst 2022): treat each cluster as one document, L1-normalise tf for cluster size, down-weight via log(1 + A/f_t).
>
> *Confidence: high (3-0).*
>

**Edit type: number**

## H1-06/genome-incompleteness.7

For 116,884 MAGs against RefSeq, raw gene detection rates fell below model-corrected prevalences, and most KEGG orthologs were biased between culture-heavy and MAG references.

- conf: single (critic: C-034)
- class: not stated
- holds: MAGs against RefSeq
- src: albrightTraitBiasesMicrobial2023
- trail: H1-06 §3. Part A2, §critic

From the note:

> For 116,884 MAGs against RefSeq, raw gene detection rates fell below model-corrected prevalences, and most KEGG orthologs were biased between culture-heavy and MAG references [11].
>
> - 'Incompleteness pushes detected function down' (Section 5) is phrased generally. Each quantitative element is SINGLE SOURCE ([9] modules, [10] core genes, [11] reference bias), and none measures the effect on conservation depth, which the review does concede.
>

**Edit type: number**

## 16S/abundance-distribution.2

In one Brazilian soil, 26,079 reads and 2,880 observed species were fitted equally well by communities of 10^4, 10^5 and 10^6 species, so the tail cannot be identified from sample data.

- conf: repl (marker)
- class: model (marker)
- holds: one Brazilian soil; the full text was not openly retrievable and these figures could not be confirmed
- limit: access (critic: MB-01:C-028)
- src: haegemanRobustEstimationMicrobial2013 (FT; model; repl)
- trail: MB-01 §3.4, §answers, §critic

From the note:

> - In the Brazil soil, 26,079 reads and 2,880 observed species were fitted equally well by communities of 10^4, 10^5 and 10^6 species, so the tail cannot be identified from sample data (Haegeman 2013) [FT; model; repl].
>
> One Brazilian soil was fitted equally well by communities of 10^4, 10^5 and 10^6 species, so the tail cannot be identified from the data (Haegeman 2013).
>
> Haegeman 2013's Brazil-soil figures rest on a full text that was not openly retrievable.
>

**Edit type: scope**

## 16S/technical-variation.3

At 1:10^5 dilution of a staggered mock, 12 species appeared in only 2 of 4 PCR replicates.

- conf: not stated
- class: not stated
- holds: Dyrhovden's staggered mock
- src: dyrhovdenManagingContaminationDiverse2021
- trail: MB-01 §4.3

From the note:

> - At 1:10^5 dilution of a staggered mock, 12 species appeared in only 2 of 4 PCR replicates.
>

**Edit type: scope**

## H1-05/ordering.24

The reverse ordering (function responds where taxonomy does not) rests on two GeoChip studies from one group [5][15], one abstract only, plus a reviewer's reading of [6]; removing [5] would leave it supported only by the abstract-only [15] and the reading of [6].

- conf: not stated
- class: not stated
- holds: weak contrasts: 14 years of moderate warming [5], erosion and deposition [15], an elevation gradient [6]; n = 4 per treatment in [5]; platforms differ
- src: gaoLongtermWarmingMediterraneantype2021, maDivergentTaxonomicFunctional2017, shenDramaticIncreasesSoil2016
- trail: H1-05 §critic, §answers
- rating: "Weak for the reverse ordering"

From the note:

> The reverse ordering rests on two GeoChip studies from one group [5][15] (one abstract only) plus a reviewer's reading of [6].
>
> The reverse ordering is reported under weak contrasts.
>
> Weak for the reverse ordering (n = 4 per treatment in [5]; platforms differ)..
>
> Removing Gao et al. 2021 [5] would leave the reverse ordering supported only by an abstract-only study [15] and a reviewer's reading of [6].
>

**Edit type: scope**

## H1-06/perturbation-response.9

In situ growth measured by qSIP in one forest soil had Blomberg's K 0.38 to 0.54 and Pagel's lambda 0.96 to 0.98.

- conf: not stated
- class: not stated
- holds: one forest soil
- src: morrisseyPhylogeneticOrganizationBacterial2016
- trail: H1-06 §2. Part A1

From the note:

> In situ growth measured by qSIP in one forest soil had K 0.38 to 0.54 and lambda 0.96 to 0.98 [22].
>

**Edit type: scope**

## 16S/abundance-distribution.17

DNA reassociation kinetics, which measure whole-community DNA rather than reads or cells, were best fitted by a power law, implying over a million distinct genomes in a pristine soil; metal pollution cut diversity by over 99.9%. This is the main contrary result on the shape of the distribution, and removing it removes the power-law side of the conflict.

- conf: not stated
- class: not stated
- holds: whole-community DNA; abstract only
- src: gansComputationalImprovementsReveal2005 (AB)
- trail: MB-02 §D3.1, §answers

From the note:

> **DNA reassociation kinetics.** This measures whole-community DNA, neither reads nor cells.
>
> A power law fitted best, implying over a million distinct genomes in a pristine soil; metal pollution cut diversity by over 99.9% [66, AB].
>
> This is the main contrary result on the shape of the distribution.
>
> DNA reassociation kinetics (whole community DNA, not reads or cells): a power law best described the abundance distribution, with over one million genomes in a pristine soil [66].
>
> Removing Gans et al. 2005 [66] removes the power-law side of the functional-form conflict.
>

**Edit type: scope**

## CB2/marker-gap.4

In UHGG, 3,207 of 4,644 species representatives were >90% complete and <5% contaminated; 573 additionally had 5S/16S/23S plus ≥18 tRNAs, and only 38 of those 573 were MAGs. The paper attributes this to the rRNA operon being "a problematic region to assemble from short-read metagenomic datasets".

- conf: not stated
- class: not stated
- holds: human gut species representatives
- src: almeidaUnifiedCatalog2042020
- trail: CB2-RRNA §2. Side by side

From the note:

> - **Human gut (UHGG).** 3,207 of 4,644 species representatives were >90% complete and <5% contaminated; 573 additionally had 5S/16S/23S plus ≥18 tRNAs — and only 38 of those 573 were MAGs.
>
> The paper attributes this to the rRNA operon being "a problematic region to assemble from short-read metagenomic datasets".
>

**Edit type: scope**

## 16S/bias-consistency.10

Evidence on whether bias is consistent across samples is weak: it rests mainly on one reanalysis of 7 taxa, with contrary or limiting field evidence.

- conf: not stated
- class: not stated
- holds: the evidence above
- src: none (the review's and critic's rating of the evidence)
- trail: MB-01 §answers, §8. Answers, §critic
- rating: "weak for consistency"

From the note:

> Evidence on whether bias is consistent across samples is weak to moderate: it rests mainly on one reanalysis of 7 taxa, with contrary or limiting field evidence.
>
> Strong qualitatively, moderate for magnitudes, weak for consistency.
>
> Overall: strong qualitatively; moderate for the inflation of taxon counts; weak for per-step relative-abundance magnitudes and for consistency across samples.
>

**Edit type: scope**

## 16S/core-microbiome.5

In 4,866 maize rhizosphere samples, seven OTUs were present in all, five of them responsive to host genotype.

- conf: not stated
- class: not stated
- holds: maize rhizosphere; abstract only
- src: waltersLargescaleReplicatedField2018 (AB)
- trail: MB-02 §D3.2, §answers

From the note:

> - **Maize** [75, AB]: in 4,866 samples, seven OTUs were present in all, five of them responsive to host genotype.
>
> Rhizosphere: in common bean rhizospheres across four US regions plus Colombia, 48 bacterial and archaeal taxa occurred in all samples, and 13.7% of bacterial and archaeal taxa deviated from a neutral abundance-occupancy expectation [74]; in 4,866 maize rhizosphere samples, seven OTUs were present in all samples [75]; core assignments in an Arabidopsis root dataset varied 7-fold among methods [52].
>

**Edit type: scope**

## 16S/copy-number.13

The Acidobacteria mean of 1.0 rests on 4 genomes from 4 species, and the rrnDB v5.10 Acidobacteriota mean of 1.4 on 29 species; these soil-relevant low values are imprecise.

- conf: not stated
- class: not stated
- holds: Vetrovsky and Baldrian's Table 1 and rrnDB v5.10
- src: vetrovskyVariability16SRRNA2013, schmidtlaboratoryRrnDBReleaseFiles
- trail: MB-02 §critic, §Adversarial, §D1.1

From the note:

> (2) The 'Acidobacteria 1.0' mean from Vetrovsky and Baldrian [6, FT] rests on 4 genomes from 4 species (their Table 1).
>
> The rrnDB v5.10 figure of 1.4 rests on 29 species.
>
> These soil-relevant low values are imprecise, and the soil correction example (Acidobacteria 50.1% to 66.0%) depends on them.
>
> - D1(a): per-phylum means for Acidobacteria (1.0 from 4 genomes in [6]) are presented alongside large-n phyla without the n. The soil correction example rests on this.
>
> - Acidobacteriota 1.4 (29)
>

**Edit type: scope**

## H2-01/covariation-stability.12

Community-weighted plant traits across 1.1 million plots showed the same two covariation axes as species-level traits, "unexpected" per the authors, while climate and soil explained only 10.8 to 14.0% of CWM variation.

- conf: single (marker)
- class: meas (marker)
- holds: plant communities worldwide; removing it removes the only large-scale case of covariation more stable than levels
- src: bruelheideGlobalTraitenvironmentRelationships2018 (FT; measured; SINGLE SOURCE)
- trail: H2-01 §4.4, §answers

From the note:

> - Covariation more stable than levels: community-weighted plant traits across 1.1 million plots showed the same two covariation axes as species-level traits, "unexpected" per the authors, while climate and soil explained only 10.8 to 14.0% of CWM variation [Bruelheide2018; FT; measured; SINGLE SOURCE].
>
> In plant traits the evidence runs both ways: CWM covariation axes matched species-level axes worldwide while CWM levels varied under similar environments [Bruelheide2018]; trait networks and bivariate slopes changed with climate [FloresMoreno2019; Wright2005]; and along an aridity gradient a trait covariance changed more systematically than level-type diversity [DwyerLaughlin2017].
>
> Removing Bruelheide2018 removes the only large-scale case of covariation more stable than levels..
>
> Lenz2016 (higher dimension) and Bruelheide2018 (covariation stable) are flagged.
>

**Edit type: scope**

## H1-02/sample-dependence.7

In soil, dependence of the gene or pathway content of related recovered genomes on sample properties was not measured in this setting, and there is indirect recovery-quality evidence only; none of the soil evidence measures the gene or pathway content of related genomes recovered from different soil samples.

- conf: not stated
- class: search (critic: C-012)
- holds: natural soil
- src: none (a search result)
- trail: H1-02 §critic, §Verdict as delivered, §5. Verdicts, §3.3

From the note:

> Part B, soil and sediment: NOT MEASURED IN THIS SETTING, with indirect recovery-quality evidence only.
>
> Dependence on sample properties: soil (natural)**: NOT MEASURED IN THIS SETTING for gene or pathway content of related recovered genomes.
>
> - Soil: **not measured in this setting**.
>
> None of it measures the gene or pathway content of related genomes recovered from different soil samples.
>

**Edit type: scope**

## NFERT/symbiotic-fixation.2

In an organic legume-based rotation in Europe, 87% of total nitrogen inputs came from fixation, and the rotation matched conventional productivity at a surplus of only 21 kg N per hectare per year against 40 to 100 for fertilised systems.

- conf: not stated
- class: not stated
- holds: an organic legume-based rotation in Europe
- src: angladeRelationshipsEstimatingN22015
- trail: NFERT §The strong, direct channel

From the note:

> In an organic legume-based rotation in Europe, 87% of total nitrogen inputs came from fixation, and the rotation matched conventional productivity at a surplus of only 21 kg N per hectare per year against 40 to 100 for fertilised systems (Anglade et al. 2015).
>

**Edit type: scope**

## CB1/ghg-balance.4

The soil-carbon term, which drives much of the difference between these balances, is itself unsettled.

- conf: unclear (note: "is itself unsettled")
- class: not stated
- holds: the soil-carbon term of the whole-system balance
- src: hollandLimingImpactsSoils2018, paradeloNetEffectLiming2015
- trail: CB1-LIMING §5. Where the numbers

From the note:

> The soil-carbon term, which drives much of the difference, is itself unsettled.
>

**Edit type: scope**

## 16S/ploidy.21

Flow cytometric cell-cycle analyses of Prochlorococcus (and Synechococcus) in situ are by method taxon-specific measurements of the share of cells with replicated DNA (G1 versus S/G2), so the review's statement that no such share exists for any natural community is not established; nothing comparable was found for soil.

- conf: not stated
- class: not stated
- holds: marine picocyanobacteria in situ; read only at abstract level by the review
- limit: access (critic: MB-02:C-018)
- src: vaulotGrowthProchlorococcusPhotosynthetic1995 (AB)
- trail: MB-02 §critic, §Adversarial

From the note:

> Flow cytometric cell-cycle analyses of Prochlorococcus in situ [24] are by method taxon-specific measurements of the share of cells with replicated DNA.
>
> The review read only the abstract, so its statement that no such share exists for any natural community is not established.
>
> Nothing comparable was found for soil.
>
> - In situ cell-cycle analyses of Prochlorococcus and Synechococcus (Vaulot 1995 and successors) report the fraction of cells in G1 versus S/G2 by taxon in natural seawater.
>
> They were read only at abstract level, and the review asserts that no such share exists for any natural community.
>

**Edit type: scope**

## H1-02/mobile-region-loss.8

In a natural biocrust soil community, short-read assemblies were checked against a PacBio HiFi assembly of the same system: of 614 long-read bins, only 24 had at least half their 1 kb segments fully recovered by short reads, while 490 had at least half not recovered.

- conf: not stated
- class: not stated
- holds: one site; the reference is long-read bins, not isolates; concerns assembly, not the gene content of binned genomes compared across samples
- src: bergComparisonShortreadLongread2025
- trail: H1-02 §2.4

From the note:

> Berg et al. [26] provide the only natural soil evidence.
>
> In a biocrust community, short-read assemblies were checked against a PacBio HiFi assembly of the same system.
>
> Of 614 long-read bins, only 24 had at least half their 1 kb segments fully recovered by short reads, while 490 had at least half not recovered.
>
> The authors conclude that short-read metagenomes "can possibly underestimate the diversity of these genome regions" (measured; natural; one site; the reference is long-read bins, not isolates).
>
> This concerns assembly, not the gene content of binned genomes compared across samples.
>

**Edit type: scope**

## H1-06/uncontrolled-rank-studies.1

Studies across ranks that do not control group number and size agree in part and conflict in part with the controlled study.

- conf: not stated
- class: not stated
- holds: Mayjonade 2024 (preprint), Bay 2020, Chakraverti-Wuerthwein 2026 (preprint), Auladell 2022
- src: mayjonadeRelativeEffectsAbiotic2024, baySoilBacterialCommunities2020, chakravertiwuerthweinPhylogeneticCoherenceMicrobiome2026, auladellSeasonalNicheDifferentiation2021
- trail: H1-06 §answers

From the note:

> Uncontrolled studies agree in part and conflict in part: habitat R2 peaked at class and physicochemical associations were most frequent at phylum (Mayjonade 2024 preprint, gyrB taxonomy); 97% OTUs explained more composition variance than ASVs (Bay 2020); a pH-aligned composition axis stayed stable across ranks (Chakraverti-Wuerthwein 2026 preprint); seasonal niches were absent at class level (Auladell 2022, time series, not a spatial environment gradient).
>

**Edit type: scope**

## H2-01/covariation-stability.10

Community genomic traits covaried, some possibly for technical reasons.

- conf: not stated
- class: not stated
- holds: microbial metagenomes, pooled
- src: barberanExplorationCommunityTraits2011 (AB)
- trail: H2-01 §4.4

From the note:

> **Microbial, pooled only.** Covariation among functions has otherwise been fitted on pooled cross-habitat data, not compared between habitats: N-pathway frequencies "overwhelmingly positively correlated" across 365 soils from 10 habitat types [Nelson2016]; co-abundance and co-expression of ocean OGs predicting shared KEGG membership [Salazar2019; fitted and scored on the same samples; partly circular]; covariation of amino-acid transport and cofactor synthesis in GOS [Gianoulis2009; AB]; covariation among community genomic traits, some possibly technical in origin [Barberan2012; AB].
>

**Edit type: scope**

## H1-06/ph-preference.5

A phylum-level tendency in pH preference seen in one dataset (acidophilic Acidobacteria in freshwater) did not recur in the others.

- conf: not stated
- class: not stated
- holds: Ramoneda's five datasets
- src: ramonedaBuildingGenomebasedUnderstanding2023
- trail: H1-06 §2. Part A1

From the note:

> A phylum-level tendency seen in one dataset (acidophilic Acidobacteria in freshwater) did not recur.
>

**Edit type: scope**

## CB2/recovery-variation.1

Of the four axes of variation in rRNA recovery, direct evidence was found for three (read length and sequencing technology, assembler choice, sequencing depth) and none for the fourth (study of origin); the four have very different evidentiary status.

- conf: not stated
- class: not stated
- holds: the literature the reviewer searched
- src: none (the review's verdict over sections 2 to 5)
- trail: CB2-RRNA §Verdict, §5. What is measured, §Verdict on the second

From the note:

> **Direct evidence found for three of the four axes; for study of origin, NO EVIDENCE EXISTS.**
>
> **Direct evidence found — for three of the four axes; no evidence exists for the fourth.**
>
> This is the second target of the brief, and the four axes it names have very different evidentiary status.
>

**Edit type: scope**

## 16S/copy-number-correction.5

Phylogenetic copy-number prediction had a leave-one-out error of about one copy, and in 100 simulated communities correction raised the correlation with true organism abundance from r = 0.70 to 0.81.

- conf: cont (marker)
- class: model (marker)
- holds: simulated communities; figures checked by MB-02's critic
- src: kembelIncorporating16SGene2012 (FT; model; cont)
- trail: MB-01 §2.5, §answers, MB-02 §D1.4, §answers, §critic

From the note:

> - **Supportive (modelled).** In simulations, phylogenetically corrected abundances correlated better with true organism abundance (r = 0.81) than raw gene abundances did (r = 0.70) (Kembel 2012) [FT; model; cont].
>
> Simulation favours correction (Kembel 2012, modelled).
>
> - **Kembel et al. 2012** [28, FT]: leave-one-out error was about one copy.
>
> In 100 simulated communities, correction raised the correlation with true abundance from r = 0.70 to 0.81.
>
> Within that limit, phylogenetic predictions are informative: leave-one-out error about one copy [28], R2 high and precision about 0.96 at small distances with uncertainty growing with distance [33].
>
> Correction improved agreement with simulated truth (r from 0.70 to 0.81) [28], with mock communities and metagenomes [29], and the chance of identifying the true most abundant OTU (13% to 65% in simulations) [33].
>
> These all matched: Pecoraro 2011 (E. coli 6.8/2.5 origins, P. putida 20/14, Caulobacter 2.1, Wolinella 0.9), Louca 2018 (15%/30% autocorrelation, 49% of SILVA OTUs, 635 communities including soil), Gao and Wu 2023 (0.96 precision, 20%/31%, 13% to 65%), Kembel 2012 (r 0.70 to 0.81, K = 0.48), Vetrovsky 2013 (mean 4.2, 15%/21%, Acidobacteria 50.1% to 66.0%), Bickel and Or 2021 (0.4%, 0.019%, prevalence 0.3 vs 0.001), Jia 2022 (61.59/45.65/28.36%, ASV counts), Custer 2023 (1.21 to 9.42%), Pascoal 2025 (181 articles, 37%, 84%, V4V5 versus full-length reversal) and Stopnisek and Shade 2021 (48 taxa, 13.7%, rarefied to 31,255 reads).
>

**Edit type: scope**

## H1-02/mobile-region-loss.5

In a simulated 30-genome short-read metagenome, across 12 assembler and binner combinations, 82% to 94% of chromosomes were recovered, against 38% to 44% of genomic islands and 1% to 29% of plasmids.

- conf: not stated
- class: model (note: "simulated a 30-genome short-read metagenome")
- holds: one simulated 30-genome community
- src: maguireMetagenomeAssembledGenomeBinning2020
- trail: H1-02 §2.4

From the note:

> Maguire et al. [4] simulated a 30-genome short-read metagenome.
>
> Across 12 assembler and binner combinations, 82% to 94% of chromosomes were recovered, against 38% to 44% of genomic islands and 1% to 29% of plasmids.
>

**Edit type: scope**

## 16S/differential-abundance.1

Fourteen differential-abundance methods on 38 datasets gave 0.8% to 40.5% significant ASVs (unfiltered means); ALDEx2 and ANCOM-II were the most consistent, and edgeR and LEfSe produced many false positives on random splits.

- conf: single (marker)
- class: meas (marker)
- holds: 38 real datasets
- src: nearingMicrobiomeDifferentialAbundance2022 (FT; meas; single)
- trail: MB-01 §5.4, §answers

From the note:

> **Agreement among methods on real data.** Fourteen methods on 38 datasets gave 0.8% to 40.5% significant ASVs (unfiltered means).
>
> ALDEx2 and ANCOM-II were the most consistent. edgeR and LEfSe produced many false positives on random splits (Nearing 2022) [FT; meas; single].
>
> Differential abundance.
>
> ALDEx2 and ANCOM-II were the most consistent across 38 datasets (Nearing 2022).
>
> The 14 methods gave 0.8% to 40.5% significant ASVs on the same data (Nearing 2022).
>

**Edit type: scope**

## H1-RES/pangenome.11

The nitrogen-fixing *Rhizobiales* pangenome (12 symbionts) contained 37,364 total loci with only 700 core genes, representing 10.2% of single genomes.

- conf: not stated
- class: not stated
- holds: 12 *Rhizobiales* symbionts
- src: none (cited only as SC1 [7]; the note gives no reference list)
- trail: H1-RES §Confirming Evidence Across

From the note:

> The nitrogen-fixing *Rhizobiales* pangenome (12 symbionts) contained 37,364 total loci with only 700 core genes, representing 10.2% of single genomes [7].
>

**Edit type: scope**

## CB2/depth-axis.2

Philip et al. report a coverage floor: "we need more than 10 read pairs, and in most cases more then 40, to be able to reconstruct a 16S with some substantial length".

- conf: not stated
- class: not stated
- holds: METASEED reconstruction
- src: philipMETASEEDNovelApproach2024 (single-pass extraction)
- trail: CB2-RRNA §5. What is measured

From the note:

> Philip et al. report the coverage floor from the other side: "we need more than 10 read pairs, and in most cases more then 40, to be able to reconstruct a 16S with some substantial length" (single-pass extraction).
>

**Edit type: scope**

## H2-01/functional-profile.2

Trait ecology supplies community-weighted means (CWMs) and species-by-trait matrices, mostly from plants.

- conf: not stated
- class: not stated
- holds: the review's account of the three bodies of work that bear on the brief
- src: none (the reviewer's account of the literature)
- trail: H2-01 §1. What

From the note:

> Three bodies of work bear on the brief.
>
> Trait ecology supplies community-weighted means (CWMs) and species-by-trait matrices, mostly from plants.
>

