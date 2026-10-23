# Faithfulness check: 30 entries

## H1-02/bounding-comparisons.7 (claim)

These bounds are coarse (genome size, ANI, per-OTU annotation overlap) and do not contradict the gene-level losses in Meziti et al., which fall on variable and mobile genes that length and ANI do not register.

- conf: not stated
- class: reading (note: "Reviewer's reading")
- holds: the bounding comparisons above; the critic: correctly labelled, but used to discount the bounding evidence in favour of Meziti et al. without a source saying so
- src: none (the reviewer's synthesis)
- trail: H1-02 §2.6, §Adversarial critique

From the note:

> Reviewer's reading: these bounds are coarse (genome size, ANI, per-OTU annotation overlap) and do not contradict the gene-level losses in [1], which fall on variable and mobile genes that length and ANI do not register.
>
> - 'Reviewer's reading: these bounds are coarse ... and do not contradict the gene-level losses' is correctly labelled. But it is used to discount the bounding evidence in favour of [1] without a source saying so.
>

## H2-01/covariation-stability.8 (claim)

Co-abundance and co-expression of ocean OGs predicted shared KEGG membership.

- conf: not stated
- class: not stated
- holds: global ocean, pooled; fitted and scored on the same samples; partly circular
- src: salazarGeneExpressionChanges2019 (FT; fitted and scored on the same samples; partly circular)
- trail: H2-01 §4.4

From the note:

> **Microbial, pooled only.** Covariation among functions has otherwise been fitted on pooled cross-habitat data, not compared between habitats: N-pathway frequencies "overwhelmingly positively correlated" across 365 soils from 10 habitat types [Nelson2016]; co-abundance and co-expression of ocean OGs predicting shared KEGG membership [Salazar2019; fitted and scored on the same samples; partly circular]; covariation of amino-acid transport and cofactor synthesis in GOS [Gianoulis2009; AB]; covariation among community genomic traits, some possibly technical in origin [Barberan2012; AB].
>

## 16S/ploidy.8 (claim)

Copy number does not always fall in stationary phase: Azotobacter vinelandii is reported to rise from about 4 copies in exponential phase to about 80 in stationary phase, and M. acetivorans from 2.5 to 5 (Bruck 2023 full text, secondary via the critic); Pecoraro 2011 Table 5 gives A. vinelandii as 1 (up to 8) copies in slow growth and 40 in fast growth, attributed to another laboratory.

- conf: not stated
- class: not stated
- holds: cultures; reported by the critic from full texts the review did not use (Bruck 2023 labelled AB, Pecoraro Table 5 not reported)
- src: bruckOneAdvantageBeing2023 (AB), pecoraroQuantificationPloidyProteobacteria2011 (FT)
- trail: MB-02 §critic, §Adversarial

From the note:

> Most Soppa-group species fall in stationary phase or starvation.
>
> The soil diazotroph Azotobacter vinelandii, however, is reported to rise from about 4 copies in exponential phase to about 80 in stationary phase (SECONDARY, via Bruck et al. 2023 full text).
>
> Pecoraro et al. 2011 Table 5 [FT] gives A. vinelandii as 1 (up to 8) copies in slow growth and 40 in fast growth, attributed to another laboratory.
>
> Bruck 2023, open in PMC but labelled abstract only, reports A. vinelandii rising from 4 to 80 copies from exponential to stationary phase, against the review's 'copies usually fall' framing.
>
> - Bruck et al. 2023 [18] is open in PMC (PMC10536925) but labelled AB.
>
> Its full text reports that A. vinelandii and M. acetivorans carry more chromosomes in stationary than in exponential phase (4 versus 80; 2.5 versus 5).
>
> That contradicts the review's framing and was missed.
>
> - D1(b): the review reports down-regulation of ploidy in stationary phase and starvation in detail.
>
> Contrary cases, ploidy rising in stationary phase (A. vinelandii; M. acetivorans in slow growth), are omitted, though they appear in a source read in full (Pecoraro Table 5) and in an open full text (Bruck 2023).
>

## H1-05/annotation.3 (claim)

The marine time series finds restricting to annotated genes weakens the coupling, while the soil precipitation experiment finds all-read and annotated dissimilarity behave alike; the two use different measures (regression of similarities vs within-treatment dispersion) and habitats, so they do not directly contradict.

- conf: not stated
- class: not stated
- holds: [31] (marine) and [22] (soil)
- src: galandStrongLinkMarine2018, xuDistinctivePatternMechanism2022
- trail: H1-05 §answers, §2

From the note:

> *Conflicts:* [31] finds that restricting to annotated genes weakens the coupling (all-read coupling is strongest), while [22] finds all-read and annotated dissimilarity behave alike in soil.
>
> The two use different measures (regression of similarities vs within-treatment dispersion) and habitats, so they do not directly contradict.
>
> The two measure different things (dispersion vs a similarity regression).
>

## TSL/altitude-ordering.4 (claim)

The same pattern is independently corroborated by Caraballo & Charniak (1999): ~86% at lower levels, 45.5% at upper levels.

- conf: repl (note: "Independently corroborated")
- class: not stated
- holds: specificity of nouns, lower vs upper levels; each figure belongs to its own study
- src: caraballoDeterminingSpecificityNouns1999, johoDocumentFrequencyTerm2007
- trail: TSL §Verdict

From the note:

> The qualification is decisive and comes from the only direct empirical test: **collection df reliably orders terms by specificity only at the specific end** (~74–83% accuracy at the bottom two WordNet levels) and **degrades to ~55–68% — near-random — for general terms** [S4].
>
> Independently corroborated by Caraballo & Charniak (1999): ~86% at lower levels, 45.5% at upper levels.
>

## 16S/dns.20 (do not say)

"Spike-in totals agreed poorly with flow cytometry (r2 0.19)" (Lin 2019) as a failure without the authors' conclusion.

- why: the authors conclude the internal-standard method is quantitative and consistent with flow cytometry; the review omits this (Common rule 6), and the r2 figure could not be verified
- instead: absolute-quantification.14
- trail: MB-01 §critic, §Adversarial

From the note:

> (3) Lin 2019: the authors conclude that the internal-standard method is quantitative and consistent with flow cytometry.
>
> The review reports only r2 = 0.19 before correction and does not give the authors' conclusion (Common rule 6).
>
> - Lin 2019: the review reports the internal-standard method's poor initial agreement with flow cytometry (r2 0.19) without the authors' conclusion that the method 'provided results consistent with ... total bacterial counts by flow cytometry' and 'is quantitative' (abstract). This breaches Common rule 6.
>
> - D5 absolute quantification: Lin 2019 is listed among failure modes (r2 0.19 before correction, four outliers removed) without the authors' conclusion that the method is quantitative and consistent with flow cytometry. Jian 2020's 'near-perfect' correlation is given at face value, although it is also a comparison of methods that share an upstream (qPCR versus qPCR-anchored sequencing).
>

## GHOST/benchmark-regime.2 (claim)

High feature sparsity provably bounds the information loss from missingness, "making all models appear robust and preventing a meaningful comparison": on standard benchmarks the models cannot be distinguished.

- conf: not stated
- class: deriv (note: "provably bounds")
- holds: standard sparse-feature benchmarks; R7 is a January 2026 arXiv preprint, under review
- src: ferriniRethinkingGNNsMissing2026 (under review)
- trail: GHOST §Verdict, §5. Bounding

From the note:

> **A 2026 result proves the benchmark itself hides the differences.** High feature sparsity provably bounds the information loss from missingness, "making all models appear robust and preventing a meaningful comparison" — so the dominance of propagation on standard benchmarks may be an artifact, not a regime-general property [R7].
>
> - **Benchmark artifact (proven).** High sparsity bounds missingness-induced information loss, so all models look robust and cannot be distinguished on standard benchmarks; dense-feature and non-MCAR (MNAR) regimes are under-evaluated [R7].
>
> Several key sources are 2025–2026 preprints / under-review (R5, R6, R7) — high-quality venues but not all finalized.
>

## H1-05/ordering.7 (claim)

Single-site "function lower" results [4][13][14][18][24] mostly set a significant test against a non-significant one.

- conf: not stated
- class: not stated
- holds: single-site soil studies; the critic's reading of them
- src: igweRedundancyMaintainsMicrobial2026, panImpactLongtermN2014, yangDecouplingMicrobialCommunity2021, souzaMetagenomicAnalysisReveals2015, saumasanchezFunctionalRedundancyBuffers2024
- trail: H1-05 §critic

From the note:

> Single-site 'function lower' results [4][13][14][18][24] mostly set a significant test against a non-significant one.
>

## TAXRES/name-resolution.3 (claim)

Grenié et al. (2023) is a review of tools, databases and best practices for harmonising taxon names.

- conf: not stated
- class: not stated
- holds: biodiversity data
- src: grenieHarmonizingTaxonNames2023
- trail: TAXRES §Taxon-name resolution

From the note:

> Grenié et al. (2023) is a **review of tools, databases, and best practices** for harmonising taxon names.
>

## H1-02/chimerism.2 (claim)

In the multi-habitat GMGC set, GUNC flagged 9.4% of MIMAG high-quality MAGs and 20.5% of genomes passing CheckM's contamination threshold of under 5%.

- conf: not stated
- class: not stated
- holds: the multi-habitat GMGC set; the study measures chimerism, not called gene content
- src: orakovGUNCDetectionChimerism2021
- trail: H1-02 §2.2

From the note:

> In the multi-habitat GMGC set, 9.4% of MIMAG high-quality MAGs were flagged, and so were 20.5% of genomes passing CheckM's contamination threshold of under 5%.
>
> The study measures chimerism, not called gene content.
>

## H2-01/expression-dimension.3 (claim)

In large heterogeneous compendia (5,372 and 7,100 samples), the first three PCs explained about 36% of variance, components beyond the third were unstable between datasets, and the residual space carried most tissue-specific signal.

- conf: single (critic: H2-01:C-122)
- class: not stated
- holds: heterogeneous expression compendia (other field); the critic's spot check confirmed n = 5,372 and 7,100 and that the fourth component was unstable
- src: lenzPrincipalComponentsAnalysis2016 (FT)
- trail: H2-01 §2.4, §critic

From the note:

> Against this, in large heterogeneous compendia (5,372 and 7,100 samples), the first three PCs explained about 36% of variance, components beyond the third were unstable between datasets, and the residual space carried most tissue-specific signal.
>
> A spot check of Lenz2016 (PMC4890592) confirmed n = 5,372 and 7,100 and that the fourth component was unstable.
>
> Lenz2016 (higher dimension) and Bruelheide2018 (covariation stable) are flagged.
>

## H2-04/aggregation-artefacts.3 (claim)

The fourth-corner approach is proposed as a remedy for the inflated community-weighted mean tests.

- conf: not stated
- class: not stated
- holds: trait ecology
- src: peresnetoLinkingTraitVariation2017 (AB)
- trail: H2-04 §Artefacts of aggregation

From the note:

> Standard tests of community-weighted mean versus environment have inflated Type I error that rises as beta diversity falls [35, AB; modelled]; the fourth-corner approach is proposed as a remedy [23a, AB].
>

## H2-01/levels-within.14 (claim)

Whether the greater stability of function levels is biological rather than processing-driven is weakly supported: none of the studies controls for normalisation, aggregation and granularity together.

- conf: not stated
- class: not stated
- holds: same-habitat studies of case A
- src: none (the reviewer's synthesis)
- trail: H2-01 §answers
- rating: "weak for the claim that the stability is biological rather than processing-driven"

From the note:

> *Strength:* Moderate for the direction as reported, weak for the claim that the stability is biological rather than processing-driven.
>
> Several independent studies agree, but none controls for normalisation, aggregation and granularity together..
>

## H2-04/covariance-partition.4 (claim)

Every microbial partition found is a single study with its own denominator, so the shares cannot be pooled.

- conf: single (note: "single study")
- class: not stated
- holds: the microbial partitions of case D1(b)
- src: none (the review's assessment of its sources)
- trail: H2-04 §answers, §critic
- rating: "Weak"

From the note:

> *Strength:* Weak.
>
> Every microbial partition is a single study with a different denominator, so the shares cannot be pooled.
>
> Strength weak; every microbial share is a single study with its own denominator.
>

## CB1/lime-requirement.13 (claim)

At a bulk density of 1 g/cm³ and 20 cm depth, 0.2–23.9 cmolc/kg converts one-for-one to t CaCO₃/ha: a two-order-of-magnitude range, which the reviewer calls the honest answer to "what is a typical rate."

- conf: not stated
- class: deriv (note: "converts one-for-one")
- holds: the reviewer's conversion at an assumed bulk density of 1 g/cm³ and 20 cm depth
- src: none (the reviewer's conversion of lime-requirement.12)
- trail: CB1-LIMING §1. Application rates

From the note:

> Their compiled incubation datasets span lime requirements of 0.2–23.9 cmolc/kg, which at a bulk density of 1 g/cm³ and 20 cm depth converts one-for-one to t CaCO₃/ha.
>
> That is a two-order-of-magnitude range, and it is the honest answer to "what is a typical rate."
>

## TAXRES/gtdb.1 (claim)

GTDB classifies by relative evolutionary divergence (RED) from genome similarity, rank-normalised.

- conf: not stated
- class: not stated
- holds: GTDB as found by a single-pass web search on 2026-06-19
- src: anonHarmonizingProkaryoticNomenclature2022, parksGTDBOngoingCensus2022
- trail: TAXRES §The NCBI-vs-GTDB divergence

From the note:

> - **GTDB** classifies by **relative evolutionary divergence (RED)** from genome similarity, rank-normalised; **NCBI Taxonomy and LPSN** follow the International Code of Nomenclature of Prokaryotes (ICNP).
>
> Searched 2026-06-19 across four angles: NCBI-vs-GTDB divergence, taxon-name resolution tools, GTDB structure/identifiers, and the GBIF/Catalogue-of-Life cross-kingdom backbone.
>

## 16S/denoising-clustering.4 (claim)

mothur and QIIME1 returned 10 to 200 times the expected number of sequences, and Faith's PD was overestimated 1.3 to 2.7-fold by QIIME2, 2 to 18-fold by QIIME1 and 3.5 to 29-fold by mothur; the authors report pipeline-dependent interpretations.

- conf: repl (marker)
- class: meas (marker)
- holds: environmental and mock data; the authors also built nf-core/ampliseq
- src: straubInterpretationsEnvironmentalMicrobial2020 (FT; meas; repl; authors also built nf-core/ampliseq)
- trail: MB-01 §2.10, §answers, §Adversarial

From the note:

> - mothur and QIIME1 returned 10 to 200 times the expected number of sequences. Faith's PD was overestimated 1.3 to 2.7-fold by QIIME2, 2 to 18-fold by QIIME1 and 3.5 to 29-fold by mothur (Straub 2020) [FT; meas; repl; authors also built nf-core/ampliseq].
>
> Taxa: mothur and QIIME1 produced 10-200 times the expected number of sequences (Straub 2020).
>
> - Section 2.10 heading: 'Relative abundance is robust to the pipeline; counts of taxa are not' generalises from Nearing 2018 (with Marizzoni 2020). Nearing 2018 itself reports that all pipelines 'markedly differed' from expected composition on the Zymo mock, and Straub 2020 reports pipeline-dependent interpretations.
>

## H1-02/core-genome-inference.1 (claim)

Simulations of core-genome inference give larger numbers than real comparisons because they strip sequence at random.

- conf: not stated
- class: not stated
- holds: simulated incompleteness
- src: none (the reviewer's synthesis)
- trail: H1-02 §2.5

From the note:

> Simulations of core-genome inference give larger numbers because they strip sequence at random.
>

## TAXRES/cross-kingdom-backbone.1 (claim)

The GBIF Backbone Taxonomy is a single synthetic cross-kingdom classification (eight kingdoms; Linnaean ranks Kingdom to Species plus subspecies, variety and forma), built by starting from the Catalogue of Life and merging other authorities in priority order.

- conf: not stated
- class: not stated
- holds: the GBIF Backbone Taxonomy as found by a single-pass web search on 2026-06-19
- src: gbifGBIFBackboneTaxonomy, gbifSixQuestionsAnswered, silvaPytaxonPythonSoftware2025, ropensciGnrResolveGlobal
- trail: TAXRES §The cross-kingdom backbone

From the note:

> The **GBIF Backbone Taxonomy** is a single synthetic cross-kingdom classification (eight kingdoms; Linnaean ranks Kingdom to Species plus subspecies/variety/forma) built by starting from the **Catalogue of Life** and merging other authorities in priority order, and it explicitly **cross-walks names between sources**.
>
> Searched 2026-06-19 across four angles: NCBI-vs-GTDB divergence, taxon-name resolution tools, GTDB structure/identifiers, and the GBIF/Catalogue-of-Life cross-kingdom backbone.
>

## GHOST/low-variance-defect.2 (claim)

The low-variance defect bounds, but does not refute, propagation: the high-variance channels do the work.

- conf: not stated
- class: not stated
- holds: the review's reading of R5 and R6
- src: none (the reviewer's synthesis)
- trail: GHOST §5. Bounding

From the note:

> Bounds, does not refute, the strategy: the high-variance channels do the work.
>

## TAXRES/name-resolution.1 (claim)

Unlike microbial gene normalisation, taxonomic name resolution is a mature, dedicated tooling area (TNRS, GNverifier / Global Names, GBIF fuzzy matching, taxize, Taxamatch, Pytaxon) with a best-practices review: documented tooling exists, likely stronger than in the gene case.

- conf: not stated
- class: not stated
- holds: the review's provisional, single-pass verdict; the gene case is a separate research result
- src: none (the verdict cites nothing; the tools are cited under the findings)
- trail: TAXRES §Provisional verdicts

From the note:

> **(b) Evaluated standard for resolving free-text taxon names? — DOCUMENTED TOOLING EXISTS (likely stronger than the gene case).** Unlike microbial gene normalisation, taxonomic name resolution is a **mature, dedicated tooling area** (TNRS, GNverifier/Global Names, GBIF fuzzy matching, `taxize`, Taxamatch, Pytaxon) with a best-practices review.
>

## TAXRES/ncbi-lpsn.1 (claim)

NCBI Taxonomy and LPSN follow the International Code of Nomenclature of Prokaryotes (ICNP).

- conf: not stated
- class: not stated
- holds: NCBI Taxonomy and LPSN as found by a single-pass web search on 2026-06-19
- src: anonHarmonizingProkaryoticNomenclature2022, parksGTDBOngoingCensus2022
- trail: TAXRES §The NCBI-vs-GTDB divergence

From the note:

> - **GTDB** classifies by **relative evolutionary divergence (RED)** from genome similarity, rank-normalised; **NCBI Taxonomy and LPSN** follow the International Code of Nomenclature of Prokaryotes (ICNP).
>
> Searched 2026-06-19 across four angles: NCBI-vs-GTDB divergence, taxon-name resolution tools, GTDB structure/identifiers, and the GBIF/Catalogue-of-Life cross-kingdom backbone.
>

## CB3/farm-gate.1 (claim)

AR6 WGIII Ch. 7: "Average non-CO2 emission (aggregated using GWP100 IPCC AR6 values) from agriculture have risen from 5.2 ± 1.4 GtCO2-eq yr−1 for the period 1990 to 1999, to 6.0 ± 1.7 GtCO2-eq yr−1 for the period 2010 to 2019 (Crippa et al. 2021)".

- conf: not stated
- class: not stated
- holds: agricultural non-CO2 (CH4 + N2O); AR6 GWP100; §7.2.1
- src: nabuursAgricultureForestryOther2022
- trail: CB3-AG-EMISSIONS §Boundary C

From the note:

> **AR6 WGIII Ch. 7**: "Average non-CO2 emission (aggregated using GWP100 IPCC AR6 values) from agriculture have risen from 5.2 ± 1.4 GtCO2-eq yr−1 for the period 1990 to 1999, to **6.0 ± 1.7 GtCO2-eq yr−1** for the period 2010 to 2019 (Crippa et al. 2021)" [1, §7.2.1].
>

## CB3/food-system.12 (claim)

Poore & Nemecek 2018 sit lower because the boundary is narrower: "Today's food supply chain creates ~13.7 billion metric tons of carbon dioxide equivalents (CO2eq), 26% of anthropogenic GHG emissions"; their accounting stops at retail and excludes consumer cooking and waste.

- conf: not stated
- class: not stated
- holds: food supply chain to retail, food only; ~2010 baseline; CO2, CH4, N2O
- src: pooreReducingFoodS2018 (accepted manuscript, headline results)
- trail: CB3-AG-EMISSIONS §Boundary A

From the note:

> **Poore & Nemecek 2018** sit deliberately lower because the boundary is narrower: "Today's food supply chain creates ~13.7 billion metric tons of carbon dioxide equivalents (CO2eq), **26%** of anthropogenic GHG emissions.
>
> Their accounting stops at retail and excludes consumer cooking and waste.
>
> | 7 | Food supply chain to retail, food only | 26% | 13.7 Gt CO2eq | ~2010 baseline | CO2, CH4, N2O | Poore & Nemecek 2018 [10] | not stated in headline |
>

## CB2/dns.3 (do not say)

"MAG-only clusters share 93% 16S identity against 99.8% for RefSeq" (Hiseni et al.) as an established figure.

- why: the note: the same caveat applies (no methods section)
- instead: catalogue-recovery.7
- trail: CB2-RRNA §1. Measured recovery

From the note:

> Hiseni et al. also report that 97.5%-ANI clusters composed purely of MAGs share on average 93% 16S identity, while clusters of complete RefSeq genomes share 99.8% — an anomaly for a gene that conserved, and their argument that the 16S sequences MAGs *do* carry are often wrong.
>
> Same caveat applies.
>

## H1-06/taxonomies.1 (claim)

Rank-wise analyses of community composition use taxonomies, not trees, and the taxonomy differs between studies: Greengenes, SILVA or RDP, GTDB, a curated gyrB taxonomy, or no ranks at all, only sequence-identity thresholds.

- conf: not stated
- class: not stated
- holds: the studies the review read: Greengenes (Lu 2016); SILVA or RDP (Ramoneda 2023, Lennon 2012, Isobe 2019); GTDB (López-Mondéjar 2022, Royalty and Steen 2019, Hoffert 2026, Barnum 2024); gyrB (Mayjonade 2024); identity thresholds only (Bay 2020, Quiroga 2022, Schmidt 2014)
- src: luEvaluatingCommunityenvironmentRelationships2016, ramonedaBuildingGenomebasedUnderstanding2023, lennonMappingNicheSpace2012, isobePhylogeneticConservationBacterial2019, lopezmondejarGlobalDistributionCarbohydrate2022, royaltyQuantitativelyPartitioningMicrobial2019, hoffertConstructingPeriodicTable2026, barnumPredictingMicrobialGrowth2024, mayjonadeRelativeEffectsAbiotic2024, baySoilBacterialCommunities2020, quirogaEcologicalAssemblyBacterial2022, schmidtEcologicalConsistencySSU2014
- trail: H1-06 §1. What is being compared

From the note:

> Rank-wise analyses of community composition use taxonomies, not trees, and the taxonomy differs between studies: Greengenes [23], SILVA or RDP [13, 14, 19], GTDB [5, 6, 8, 12], a curated gyrB taxonomy [24], or no ranks at all, only sequence-identity thresholds [25, 26, 27].
>

## NFERT/manufacturing-energy.3 (claim)

Energy requirements fell from about 55 GJ per tonne of ammonia in the 1950s to the high-20s today.

- conf: not stated
- class: not stated
- holds: the 1950s to the present
- src: tunaTechnoEconomicAssessment2014
- trail: NFERT §Energy per unit

From the note:

> The historical trajectory is steep: requirements fell from about 55 GJ per tonne in the 1950s to the high-20s today (Tunå et al. 2014).
>

## H2-01/direct-dimension.5 (claim)

In 128 soil metagenomes, the first four multiple co-inertia axes captured 29%, 21%, 16% and 10% of variation; this is the only variance-explained figure for a microbial functional profile.

- conf: single (critic: H2-01:C-009)
- class: not stated
- holds: global topsoil set; KEGG, eggNOG, SEED, CAZy and genomic-trait tables, relative abundance normalised by annotated bacterial reads, log(x+1), z-scored
- src: pitonLifeHistoryStrategies2023 (FT per trait-ecology angle, not re-checked by the reviewer, critic: H2-01:C-064)
- trail: H2-01 §2.1, §answers

From the note:

> - **Soil, community-aggregated traits, co-inertia.** In 128 soil metagenomes (global topsoil set) with KEGG, eggNOG, SEED, CAZy and genomic-trait tables (relative abundance normalised by annotated bacterial reads, log(x+1), z-scored), the first four multiple co-inertia axes captured 29%, 21%, 16% and 10% of variation.
>
> In 128 soils, two co-inertia axes carried 29% and 21% of variation and the next two 16% and 10% [Piton2023].
>
> Removing Piton2023 leaves no variance-explained figure for a microbial functional profile.
>
> All three direct microbial estimates (Jiang2012, Piton2023, Flinkstrom2024) are single studies fitted and scored on the same samples.
>
> - D1 access_basis says 'Mostly full text', but the synthesis re-opened only Chen2020 and Manor2017. Piton2023 (the only variance-explained figure), Mouillot2021 (the only measured dependence of dimension on feature and sample count), Nayfach2015, HMP2012 and Tian2020 are full text 'per angle' and were not re-checked, even though they are named as single points of failure.
>

## H1-06/perturbation-response.6 (claim)

Warming, drought, elevated CO2, P addition and liming gave tau_D 0.016 to 0.024, with little difference among perturbations.

- conf: not stated
- class: not stated
- holds: soil perturbation experiments
- src: isobePhylogeneticConservationSoil2020
- trail: H1-06 §2. Part A1

From the note:

> Warming, drought, elevated CO2, P addition and liming gave tau_D 0.016 to 0.024, with little difference among perturbations; clades responding to one perturbation rarely responded to another [20].
>

## H1-RES/taxonomy-function.7 (claim)

Whether taxonomy predicts nitrogen-cycle functions depends on the gene and clade: for nosZ, particularly in nirK-harbouring organisms, taxonomy is a reasonable proxy for gene presence and phylogenetic relationships; for core nif genes (NifHDKEN) in clades with conserved operons and congruent phylogenies it is a strong predictor of nitrogen-fixation capacity; for nirK and norB it is a poor predictor because of extensive HGT and habitat-based clustering; and in *Paenibacillus* and free-living *Bradyrhizobium*, horizontal acquisition of functional modules decouples nitrogen-fixation capacity from core genome phylogeny.

- conf: not stated
- class: not stated
- holds: the Sub-claim 3 genes and clades
- src: jones2008, hirsch1995, heylen2006, garbeva2007, heylen2007, tao2021, xie2014
- trail: H1-RES §Gene-Specific

From the note:

> The implications for using taxonomy to predict nitrogen-cycle functions depend on the specific gene and clade.
>
> For nosZ, particularly in nirK-harboring organisms, taxonomy provides a reasonable proxy for gene presence and phylogenetic relationships [13].
>
> For core nif genes (NifHDKEN) in clades with conserved operons and congruent phylogenies, taxonomy is a strong predictor of nitrogen-fixation capacity [18].
>
> However, for nirK and norB, taxonomy is a poor predictor due to extensive HGT and habitat-based clustering [2] [7] [16].
>
> For nif genes in taxa like *Paenibacillus* and free-living *Bradyrhizobium*, horizontal acquisition of functional modules means that nitrogen-fixation capacity is decoupled from core genome phylogeny [6] [9].
>

