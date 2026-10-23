# Faithfulness check: 100 entries

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

## CB2/catalogue-recovery.9 (claim)

Ma et al. state that "near full-complement rRNA genes sequences are challenging for assembling from metagenomes, especially for near-complete MAGs."

- conf: not stated
- class: not stated
- holds: a statement in a catalogue paper
- src: maGenomicCatalogueSoil2023
- trail: CB2-RRNA §4. Bounding facts

From the note:

> Ma et al.: "near full-complement rRNA genes sequences are challenging for assembling from metagenomes, especially for near-complete MAGs."
>

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

## 16S/taxonomic-assignment.6 (claim)

Estimated annotation error is about 10% for RDP and about 17% for SILVA v128 and Greengenes 13.5, judged from conflicting labels on identical sequences.

- conf: single (marker)
- class: deriv (marker)
- holds: three reference databases; one author
- src: edgarTaxonomyAnnotationGuide2018 (FT; deriv; single)
- trail: MB-01 §2.12, §answers, §Adversarial

From the note:

> **Databases.** Estimated annotation error is about 10% for RDP and about 17% for SILVA v128 and Greengenes 13.5, judged from conflicting labels on identical sequences (Edgar 2018c) [FT; deriv; single].
>
> Reference databases carry about 10-17% annotation error (Edgar 2018c).
>
> - Section 2.12: V4 genus accuracy of about 50% at 97% identity and 10 to 17% database annotation error rest on Edgar 2018b and 2018c, from one author who also develops competing classifiers. Flagged single in the text but used in the D2 answer without that qualifier.
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

## H1-02/contaminated-pangenome.1 (claim)

In a cirrhosis case-control gut cohort re-analysed with UHGG/MIDAS2 pangenomes, 33 (38%) of 86 Lachnospiraceae genes that differed in prevalence between cases and controls were probable contaminants from disease-associated genera; the differential calls come from read mapping to a partly contaminated reference pangenome, not from comparing recovered genomes.

- conf: single (critic: C-003)
- class: not stated
- holds: one cirrhosis cohort and one family, Lachnospiraceae (the critic); natural human gut; false differential prevalence, not content differences between genomes recovered from different samples
- src: majernikSmallAmountsMisassembly2025
- trail: H1-02 §2.2, §critic, §Adversarial critique

From the note:

> Majernik et al. [22] re-analysed a cirrhosis case-control gut cohort with UHGG/MIDAS2 pangenomes.
>
> Of 86 Lachnospiraceae genes that differed in prevalence between cases and controls, 33 (38%) were probable contaminants from disease-associated genera.
>
> Separately, contamination of a reference pangenome produced false differential gene prevalence between sample groups (SINGLE SOURCE [22]; the calls come from read mapping to UHGG, not from comparing recovered genomes).
>
> [22] measures false differential prevalence from reads mapped to a contaminated reference pangenome, not content differences between genomes recovered from different samples.
>
> - Contamination-driven false gene associations (38%, 33/86) come from one cirrhosis cohort and one family, Lachnospiraceae [22]. The quick re-run on Bacteroides thetaiotaomicron was 30 genes in the same data set.
>
> The differential calls come from MIDAS2 read mapping to a reference pangenome that was partly contaminated.
>

## GHOST/structure-only-embedding.1 (claim)

A distinct family of methods consumes only topology (LLE, Laplacian Eigenmaps, Graph Factorisation, GraRep, HOPE, DeepWalk, node2vec, SDNE, DNGR, LINE), operating on adjacency / similarity matrices; attribute-joint methods are treated as a separate, newer line.

- conf: not stated
- class: not stated
- holds: the taxonomy of a 2018 survey; the topology-only characterisation of those classical methods remains accurate, but the field has expanded since
- src: goyalGraphEmbeddingTechniques2018
- rating: "Confidence: high (3-0)"
- trail: GHOST §1. Strategies, §Standing caveats

From the note:

> - **Structure-only / positional embedding.** A distinct family consuming *only* topology — LLE, Laplacian Eigenmaps, Graph Factorisation, GraRep, HOPE, DeepWalk, node2vec, SDNE, DNGR, LINE — operating on adjacency/similarity matrices; attribute-joint methods are treated as a separate, newer line [R8].
>
> *Confidence: high (3-0).*
>
> The structure-only taxonomy rests on a 2018 survey (R8); the topology-only characterisation of those classical methods remains accurate, but the field has expanded since.
>

## H1-06/ab-relation.1 (claim)

No source tests a correspondence between the rise in composition-environment R2 from otu97 to genus (natural systems) and the depths at which perturbation responses cluster (engineered).

- conf: not stated
- class: not stated
- holds: the critic's assessment of the review's 'Relation to Part A' reading
- src: luEvaluatingCommunityenvironmentRelationships2016, isobePhylogeneticConservationBacterial2019, isobePhylogeneticConservationSoil2020
- trail: H1-06 §critic

From the note:

> - 'Relation to Part A (reviewer's reading)' links a natural-system composition result (Lu 2016, otu97-to-genus rise) to engineered perturbation-response depths (Isobe 2019, 2020, tau_D ~0.017, 'about genus'), which breaks Common rule 10's natural/engineered separation. It is labelled reviewer's reading, but it presents a correspondence the sources do not test.
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

## CB3/dns.6 (do not say)

"The 13–21% range for AFOLU reflects statistical uncertainty."

- why: the note: the spread is not statistical noise but two different CO2 accounting methods
- instead: afolu.2, co2-accounting.1
- trail: CB3-AG-EMISSIONS §Boundary B

From the note:

> The spread is not statistical noise — it is two different CO2 accounting methods: 11.9 ± 4.4 GtCO2eq of a total 55.9 ± 6.1 GtCO2eq gives 21% using bookkeeping models for the CO2 component, but "When using FAOSTAT/NGHGIs CO2 flux data, then the contribution of AFOLU to total emissions amounts to 13% of global emissions" [1, §7.2.1].
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

## H1-RES/redundancy.2 (claim)

Zhang et al. (2016): along a latitudinal gradient in natural broadleaf forest, strong biogeographic endemism in bacterial taxonomy contrasted with highly convergent potential functions, implying functional compensation across differing taxa.

- conf: not stated
- class: not stated
- holds: natural broadleaf forest soils along a latitudinal gradient
- src: zhangSoilBacterialEndemism2016
- trail: H1-RES §Soil redundancy evidence

From the note:

> |  Soil bacterial endemism and potential functional redundancy in natural broadleaf forest along a latitudinal gradient, Yuguang Zhang et al., 2016  | Strong biogeographic endemism in bacterial taxonomy contrasted with highly convergent potential functions along the latitudinal gradient, implying functional compensation across differing taxa [2].  |
>

## CB3/afolu.2 (claim)

The 13–21% spread is two different CO2 accounting methods, not statistical noise: 11.9 ± 4.4 GtCO2eq of a total 55.9 ± 6.1 GtCO2eq gives 21% using bookkeeping models for the CO2 component, and "When using FAOSTAT/NGHGIs CO2 flux data, then the contribution of AFOLU to total emissions amounts to 13% of global emissions".

- conf: not stated
- class: not stated
- holds: 2010–2019 mean; AR6 WGIII Ch. 7 §7.2.1
- src: nabuursAgricultureForestryOther2022
- trail: CB3-AG-EMISSIONS §Boundary B

From the note:

> The spread is not statistical noise — it is two different CO2 accounting methods: 11.9 ± 4.4 GtCO2eq of a total 55.9 ± 6.1 GtCO2eq gives 21% using bookkeeping models for the CO2 component, but "When using FAOSTAT/NGHGIs CO2 flux data, then the contribution of AFOLU to total emissions amounts to 13% of global emissions" [1, §7.2.1].
>
> | 11 | AFOLU, bookkeeping CO2 | 21% | 11.9 GtCO2-eq | 2010–2019 mean | CO2, CH4, N2O; AR6 GWP100 | AR6 WGIII Ch.7 [1] | ±4.4 Gt; *medium confidence* |
>
> | 12 | AFOLU, FAOSTAT/NGHGI CO2 | 13% | — | 2010–2019 mean | as above | AR6 WGIII Ch.7 [1] | *medium confidence* |
>

## CB2/depth-axis.4 (claim)

The closest work is Haryono et al., who show MAG quality tracking normalised coverage decile by decile, but their quality axis there is the completeness/contamination classification, not rRNA presence.

- conf: not stated
- class: not stated
- holds: tropical activated sludge; completeness/contamination, not rRNA
- src: haryonoRecoveryHighQuality2022
- trail: CB2-RRNA §5. What is measured

From the note:

> The closest is Haryono et al., who show MAG quality tracking normalised coverage decile by decile — but their quality axis there is the completeness/contamination classification, not rRNA presence.
>

## H2-01/covariation-stability.1 (claim)

No microbial study was found that compares the between-habitat stability of function-function covariation with that of function levels or taxonomic composition.

- conf: not stated
- class: search (note: "No microbial study was found that compares the between-habitat stability of function-function covariation")
- holds: search routes as for D2
- src: none (a search result)
- trail: H2-01 §answers, §1. What, §critic
- rating: "Absent for the microbial cross-habitat case"

From the note:

> **D3 case D: covariation among functions against function levels and taxonomic composition, across habitats (including temporal stability of covariation)**: No microbial study was found that compares the between-habitat stability of function-function covariation with that of function levels or taxonomic composition (search routes as for D2).
>
> *Strength:* Absent for the microbial cross-habitat case.
>
> No microbial cross-habitat comparison was found.
>
> No study was found that compared the between-habitat stability of function-function covariation with the stability of function levels and of taxonomic composition in microbial metagenomes.
>
> Not found by these routes: any microbial test withholding a habitat when scoring functional covariation; any microbial cross-habitat comparison of covariation stability against level and composition stability; any microbial study of how dimension estimates change with normalisation, sparsity, presence/absence, overlapping gene sets or sample size; any study holding taxonomy fixed while habitat varies.
>
> - **D3 case D (covariation vs levels and composition)**: No microbial cross-habitat comparison was found.
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

## CB3/gwp-metric.2 (claim)

AR6 warns that "The choice of metric depends on the purpose of the analysis and all GHG emission metrics have limitations and uncertainties".

- conf: not stated
- class: not stated
- holds: IPCC AR6 WGIII Summary for Policymakers
- src: ipccSummaryPolicymakers2022
- trail: CB3-AG-EMISSIONS §Where the major sources differ

From the note:

> AR6 itself warns "The choice of metric depends on the purpose of the analysis and all GHG emission metrics have limitations and uncertainties" [16].
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

## CB1/lime-requirement.10 (claim)

The Ethiopian value-chain study reports that about 20 quintals (2 t) of lime per hectare is the average requirement.

- conf: not stated
- class: not stated
- holds: Ethiopia
- src: oumerAgriculturalLimeValue2023
- trail: CB1-LIMING §1. Application rates

From the note:

> The Ethiopian value-chain study reports that about 20 quintals (2 t) of lime per hectare is the average requirement, and that once the full recommended rate is applied "it can benefit farmers for up to five years" [8].
>

## H1-05/ordering.17 (claim)

After 14 years of moderate warming (0.8 to 2.0 C), 16S composition did not differ, while GeoChip functional-gene composition did (Adonis, ANOSIM, MRPP, P < 0.05), with n = 4 per treatment.

- conf: not stated
- class: meas (marker)
- holds: a Mediterranean-type grassland [5]; GeoChip against 16S; n = 4 per treatment
- src: gaoLongtermWarmingMediterraneantype2021 (FT, rechecked; measured)
- trail: H1-05 §1.3, §answers

From the note:

> - After 14 years of moderate warming (0.8 to 2.0 C), 16S composition did not differ, while GeoChip functional-gene composition did (Adonis, ANOSIM, MRPP, P < 0.05), with n = 4 per treatment [5] [FT, rechecked; measured].
>
> The reverse ordering (function responds where taxonomy does not) is reported under weak contrasts: 14 years of moderate warming (GeoChip [5]), erosion and deposition (GeoChip, abstract only [15]), and possibly an elevation gradient where functional distance decay was stronger (GeoChip; the reviewer's reading, not the authors' conclusion [6]).
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

## H1-02/same-sample-isolate.4 (claim)

Genes with low-identity matches plus genes that had been assembled but binned into other Enterobacteriaceae MAGs made up more than 95% of the missed genes.

- conf: single (note: "These figures are SINGLE SOURCE")
- class: not stated
- holds: one species in one low-diversity host environment
- src: mezitiReliabilityMetagenomeassembledGenomes2021
- trail: H1-02 §2.1

From the note:

> Genes with low-identity matches plus genes that had been assembled but binned into other Enterobacteriaceae MAGs made up more than 95% of the missed genes.
>
> These figures are SINGLE SOURCE for one species in one low-diversity host environment.
>

## H1-02/mobile-region-loss.6 (claim)

No plasmid-borne AMR or virulence gene was binned correctly.

- conf: not stated
- class: model (note: "modelled; engineered")
- holds: the same simulated community
- src: maguireMetagenomeAssembledGenomeBinning2020
- trail: H1-02 §2.4

From the note:

> No plasmid-borne AMR or virulence gene was binned correctly (modelled; engineered).
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

## H2-01/heldout-study.1 (claim)

One direct microbial test of functional covariation on a withheld study was found (Chen2020, human gut).

- conf: single (marker)
- class: search (note: "Chen et al. (2020) is the only direct microbial test found")
- holds: human gut, between cohorts; removing it leaves no direct microbial test of functional covariation on held-out data
- src: chenGutMicrobialCoabundance2020 (FT, figures re-checked; measured; SINGLE SOURCE)
- trail: H2-01 §3.2, §answers, §critic
- rating: "Weak for withheld-study (one study, one habitat)"

From the note:

> Chen et al. (2020) is the only direct microbial test found [Chen2020; FT, figures re-checked; measured; SINGLE SOURCE].
>
> Withheld study, same habitat: one study.
>
> Weak for withheld-study (one study, one habitat).
>
> Removing Chen2020 leaves no direct microbial test of functional covariation on held-out data.
>
> The closest microbial evidence is a between-cohort, single-habitat (human gut) study [Chen2020].
>
> Withheld study, same habitat: one study (Chen2020, verified against full text).
>

## H1-05/marker-inferred.1 (claim)

Nano ZnO dose separated taxa but not PICRUSt-type predicted functions.

- conf: not stated
- class: deriv (marker)
- holds: soil polluted with nano ZnO [25]; PICRUSt-type inferred function
- src: dineshSoilPollutedNano2023 (AB; derived)
- trail: H1-05 §1.2

From the note:

> - Marker-inferred function: ZnO dose separated taxa but not PICRUSt-type predicted functions [25] [AB; derived].
>

## H2-04/dns.2 (do not say)

"Annotation dominates pipelines", or "annotation reference choice (65.4% of network variance)" as the size of the annotation artefact for function profiles.

- why: the figure is the 16S taxonomy database's share of variance among taxon networks, from one study; it says nothing directly about functional annotation schemes
- instead: association-networks.13
- trail: H2-04 §critic, §Adversarial critique

From the note:

> Annotation dominates pipelines: the 16S reference database contributed 65.4% of the variance among inferred networks and OTU processing 26.8% [13, FT; measured; single study].
>
> Artefacts: compositional closure [8 abstract; 31 full text], method disagreement (31.5% shared edges) [31], annotation reference choice (65.4% of network variance) [13, full text], weighting choices (27% of sign changes in trait ecology) [32, abstract], and aggregation of unit-level values that produces correlations among community means through repeated co-occurrence alone [12, abstract, modelled].
>
> The 'annotation reference choice' figure (65.4%, Kishore 2023, checked against full text) is the 16S taxonomy database's share of variance among taxon networks.
>
> It says nothing directly about functional annotation schemes, so it is indirect for function profiles.
>
> (3) The Kishore 16S-taxonomy database share is presented as an annotation artefact without saying it concerns taxonomic, not functional, annotation.
>
> - Section 3.1 'Annotation dominates pipelines' rests on Kishore et al. 2023 alone, and on 16S taxonomy databases, not functional annotation.
>
> - D1(a)/section 3.1: taxonomic annotation (16S reference database, Kishore) is presented as the magnitude of 'annotation reference choice' artefacts for function profiles.
>

## 16S/dns.2 (do not say)

"Departures occur at every step."

- why: field sampling for water and host tissue was not searched, and several choices showed no detectable effect; departures were measured at most steps examined
- instead: workflow-bias.2
- trail: MB-01 §critic, §Adversarial

From the note:

> D2's 'departures found at every step' includes unsearched field-sampling steps.
>
> For the review's stronger 'departures found at every step': no.
>
> Field sampling for water and host tissue was not searched, and several choices showed no detectable effect (PCR replicate pooling, lane and day, cycle number in some studies, storage relative to between-soil differences).
>
> The answer should say departures were measured at most steps examined.
>
> **D2.** Departures occur at every step.
>

## 16S/denoising-clustering.3 (claim)

Bacteroides varied from 20.6% to 24.6% across pipelines in human faeces, and operating system mattered little for pipeline output.

- conf: not stated
- class: not stated
- holds: human faecal samples
- src: marizzoniComparisonBioinformaticsPipelines2020
- trail: MB-01 §answers, §2. Steps, §7. Bounds

From the note:

> Bacteroides varied from 20.6% to 24.6% across pipelines (Marizzoni 2020).
>
> Bacteroides 20.6 to 24.6% across pipelines | 10 to 200 times more units than expected (mothur, QIIME1). 50 to 80% spurious taxa unfiltered | Not stated | Nearing 2018; Straub 2020; Reitmeier 2021; Marizzoni 2020 |
>
> - operating system, for pipeline output (Marizzoni 2020).
>

## H1-RES/n-cycle-hgt.15 (claim)

Jones et al. (2008): codon usage and G+C content analyses showed no evidence for recent HGT of any denitrification gene, and the close proximity of denitrification gene copies in several genomes suggested duplication rather than horizontal acquisition; HGT cannot be ruled out, but gene duplication and divergence and lineage sorting may have influenced each denitrification gene differently.

- conf: not stated
- class: not stated
- holds: denitrification genes in the genomes analysed
- src: jones2008
- trail: H1-RES §Counter-Evidence: Vertical

From the note:

> Codon usage and G+C content analyses showed no evidence for recent HGT of any denitrification genes, and the close proximity of denitrification gene copies in several genomes suggested duplication rather than horizontal acquisition [13].
>
> The study concluded that while HGT cannot be ruled out, alternative processes such as gene duplication/divergence and lineage sorting may have differently influenced the evolution of each denitrification gene [13].
>

## H1-RES/n-cycle-hgt.23 (claim)

Pothier et al. (2008) found that *Azospirillum brasilense* Sp245 nirK1 and nirK2 clustered with beta-proteobacterial sequences rather than other *Azospirillum* or alpha-proteobacterial sequences, pointing to past horizontal transfer followed by duplication.

- conf: not stated
- class: not stated
- holds: one strain
- src: pothier2008
- trail: H1-RES §Gene-Specific

From the note:

> Pothier et al. (2008) found that *Azospirillum brasilense* Sp245 nirK1 and nirK2 clustered with beta-proteobacterial sequences rather than other *Azospirillum* or alpha-proteobacterial sequences, pointing to past horizontal transfer followed by duplication [15].
>

## H1-06/moisture-preference.3 (claim)

Lennon et al. themselves caution that their isolate numbers are small (5 bacterial phyla, 19 genera).

- conf: not stated
- class: not stated
- holds: the bacterial isolates of Lennon 2012
- src: lennonMappingNicheSpace2012
- trail: H1-06 §2. Part A1

From the note:

> The authors themselves caution that isolate numbers are small (5 bacterial phyla, 19 genera).
>

## CB3/food-system.16 (claim)

A search for published criticism or formal comment disputing the EDGAR-FOOD "one third" figure or its land-use attribution found none; the qualifications on that figure come from its own authors and from boundary comparisons (Tubiello, OWID), not from an adversarial literature.

- conf: not stated
- class: search (note: "found none")
- holds: the review's search by web search, direct page fetch, and where available the biblion corpus and Scholar Gateway semantic search
- src: none (a search result)
- trail: CB3-AG-EMISSIONS §Bounding and negative facts

From the note:

> - **Absence of evidence.** I searched specifically for published criticism or formal comment disputing the EDGAR-FOOD "one third" figure or its land-use attribution and **found none**.
>
> The qualifications on that figure come from its own authors and from boundary comparisons (Tubiello, OWID), not from an adversarial literature.
>
> Sources: web search, direct page fetch, and where available the biblion corpus and Scholar Gateway semantic search.
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

## 16S/denoising-clustering.5 (claim)

DADA2 had the best sensitivity and UNOISE3 the best balance, while QIIME-uclust produced on average 134 one-off and 412 other spurious OTUs.

- conf: repl (marker)
- class: meas (marker)
- holds: three mock runs
- src: prodanComparingBioinformaticPipelines2020 (FT; meas; repl)
- trail: MB-01 §2.10

From the note:

> - DADA2 had the best sensitivity and UNOISE3 the best balance (Prodan 2020) [FT; meas; repl].
>
> **Spurious units.**
>
> QIIME-uclust produced on average 134 one-off and 412 other spurious OTUs.
>

## CB2/catalogue-recovery.5 (claim)

The Nayfach catalogue's mean completeness is 83% with mean contamination 1.3%, and the paper names "problems assembling the 16S rRNA locus" as one reason new species' MAGs came out less complete than known ones.

- conf: not stated
- class: not stated
- holds: the GEM catalogue
- src: nayfachGenomicCatalogEarths2020
- trail: CB2-RRNA §1. Measured recovery

From the note:

> The Nayfach catalogue's mean completeness is 83% with mean contamination 1.3%, and the paper names "problems assembling the 16S rRNA locus" as one reason new species' MAGs came out less complete than known ones.
>

## H1-RES/redundancy.15 (claim)

Community-scale functional redundancy is well attested in soil: across the eleven tabulated studies, taxonomic composition varies widely between sites while functional composition (gene abundances, predicted metabolic categories) stays comparatively conserved.

- conf: not stated
- class: reading (note: "Synthesis written from the eleven studies tabulated above")
- holds: the eleven soil studies; the synthesis was written manually, not by the research round
- src: none (the owner's synthesis from the tabulated studies)
- trail: H1-RES §Assessment: redundancy
- rating: "well attested"

From the note:

> *(Synthesis written from the eleven studies tabulated above; the round did not reach this synthesis itself.)*
>
> Community-scale functional redundancy is well attested in soil, and the soil evidence is direct enough to stand in for the ocean precedent.
>
> Across the supplied corpus, the repeated pattern is that taxonomic composition varies widely between sites while functional composition (gene abundances, predicted metabolic categories) stays comparatively conserved.
>

## 16S/denoising-clustering.2 (claim)

In an independent benchmark, relative abundances of expected taxa within each mock were similar across DADA2, UNOISE3, Deblur and open-reference OTUs, while counts of units differed widely: open-reference clustering gave 453 OTUs on the HMP mock and 8,891 on the Extreme mock, and on one soil DADA2 gave 16,609 ASVs, UNOISE3 11,613, Deblur 8,270 and open-reference 21,297 OTUs; no pipeline recovered every expected sequence, and on the Zymo mock all pipelines "markedly differed" from expected composition.

- conf: repl (marker)
- class: meas (marker)
- holds: mocks (HMP, Extreme, Zymo) and one soil
- src: nearingDenoisingDenoisersIndependent2018 (FT; meas; repl)
- trail: MB-01 §2.10, §answers, §Adversarial

From the note:

> **Relative abundance is robust to the pipeline; counts of taxa are not.** In an independent benchmark, relative abundances of expected taxa within each mock were similar across DADA2, UNOISE3, Deblur and open-reference OTUs (Nearing 2018) [FT; meas; repl].
>
> Counts of units differed widely.
>
> Open-reference clustering gave 453 OTUs on the HMP mock and 8,891 on the Extreme mock.
>
> On one soil, DADA2 gave 16,609 ASVs, UNOISE3 11,613, Deblur 8,270 and open-reference 21,297 OTUs.
>
> No pipeline recovered every expected sequence.
>
> On the Zymo mock, all pipelines "markedly differed" from expected composition.
>
> Denoising and clustering.
>
> RA of expected taxa was similar across pipelines (Nearing 2018).
>
> | Denoising, clustering | Expected-taxon RA similar across pipelines.
>
> - Section 2.10 heading: 'Relative abundance is robust to the pipeline; counts of taxa are not' generalises from Nearing 2018 (with Marizzoni 2020). Nearing 2018 itself reports that all pipelines 'markedly differed' from expected composition on the Zymo mock, and Straub 2020 reports pipeline-dependent interpretations.
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

## H1-06/a1-environmental-preferences.2 (claim)

The frequently repeated statement that pH optimum, soil moisture optimum and habitat association sit in deep clades appears in Martiny et al. 2013 as a discussion claim resting on other studies; that paper does not measure any of these.

- conf: not stated
- class: assert (note: "asserted, SECONDARY")
- holds: Martiny et al. 2013's discussion
- src: martinyPhylogeneticConservatismFunctional2013 (asserted, SECONDARY)
- trail: H1-06 §2. Part A1

From the note:

> **No consenTRAIT depth for any environmental optimum was found.** The frequently repeated statement that pH optimum, soil moisture optimum and habitat association sit in deep clades appears in Martiny et al. 2013 as a discussion claim resting on other studies.
>
> That paper does not measure any of these (asserted, SECONDARY) [1].
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

## H1-02/sample-dependence.5 (claim)

In marine samples, dependence on diversity and depth was not measured for gene content; the evidence covers MAG yield only.

- conf: not stated
- class: search (critic: C-011)
- holds: natural marine
- src: royaltyTheoreticalSimulationBasedInvestigation2019
- trail: H1-02 §critic, §Verdict as delivered, §5. Verdicts

From the note:

> NOT MEASURED for diversity or depth.
>
> Dependence on diversity and depth: NOT MEASURED for gene content.
>
> The evidence covers MAG yield only [16].
>
> Not measured for diversity or depth.
>

## H1-05/redundancy.6 (claim)

The review counts as against or complicating redundancy: coupling holds when all genes are used [31]; functional dispersion tracks taxonomic dispersion [22]; decoupling vanishes at species resolution within groups [11]; averaging alone reproduces lower functional variability [29][30]; function is more responsive under some weak contrasts [5][15].

- conf: not stated
- class: not stated
- holds: the review's classification of its sources
- src: galandStrongLinkMarine2018, xuDistinctivePatternMechanism2022, liuReciprocalChangesDominant2023, hoChallengesInterpretingFunctional2025, hoChallengesQuantifyingFunctional2024, gaoLongtermWarmingMediterraneantype2021, maDivergentTaxonomicFunctional2017
- trail: H1-05 §3.4, §answers

From the note:

> - **Against or complicating:**
>
> - Functional dispersion tracks taxonomic dispersion [22].
>
> - Decoupling vanishes at species resolution within groups [11].
>
> - Averaging alone reproduces lower functional variability [29][30].
>
> - Function is more responsive under some weak contrasts [5][15].
>
> Against or complicating, [11][22][31][29].
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

## H2-04/dns.6 (do not say)

"Moderate for the pattern that whole-community co-occurrence associates with overlap, replicated across independent groups but with weak effects."

- why: the overlap side rests on co-occurrence inference, which is method-dependent and poorly validated, with no error rate applied to it; the critic grades it weak to moderate
- instead: complementarity-overlap.5, complementarity-overlap.19
- trail: H2-04 §critic, §Adversarial critique

From the note:

> *Strength:* Moderate for the pattern that whole-community co-occurrence associates with overlap, replicated across independent groups but with weak effects.
>
> Strength: weak to moderate for overlap, weak for complementarity.
>
> - D1(c): the overlap side is rated moderate and 'replicated across independent groups', although it rests on co-occurrence inference.
>
> Section 3 of the review shows that inference to be method-dependent (31.5% shared edges) and poorly validated.
>
> The complementarity side's genome-derived auxotrophy caution is quantified (43.4 to 75.5% sensitivity), but no equivalent error rate is applied to the co-occurrence side when the strength ratings are set.
>

## CB3/synthetic-fertiliser.4 (claim)

Menegat et al. 2022: "the synthetic N fertiliser supply chain was responsible for estimated emissions of 1.13 GtCO2e in 2018, representing 10.6% of agricultural emissions and 2.1% of global GHG emissions", with production 38.8%, field emissions 58.6% and transportation 2.6%.

- conf: not stated
- class: not stated
- holds: whole synthetic N supply chain; 2018; CO2 + N2O
- src: menegatGreenhouseGasEmissions2022 (Abstract read only)
- trail: CB3-AG-EMISSIONS §Boundary D, §No adversarial pass
- limit: access (note: "note where the review itself says it read only an abstract")

From the note:

> - Whole synthetic N supply chain, Menegat et al. 2022: "the synthetic N fertiliser supply chain was responsible for estimated emissions of **1.13 GtCO2e in 2018, representing 10.6% of agricultural emissions and 2.1% of global GHG emissions**.
>
> Synthetic N fertiliser production accounted for 38.8% ... field emissions 58.6% ... transportation 2.6%" [13].
>
> (Abstract read only; an author correction exists but concerns figure axis labels and a supplementary table, not the headline [13a].)
>
> | 25 | Synthetic N fertiliser, whole supply chain | 2.1% | 1.13 Gt CO2e | 2018 | CO2 + N2O | Menegat et al. 2022 [13] | abstract only |
>
> Treat the numbers as unconfirmed until spot-checked against the primary text, and note where the review itself says it read only an abstract.
>

## 16S/read-depth.1 (claim)

The Earth Microbiome Project averaged 80,000 sequences per sample over 27,751 samples and rarefied to 5,000; in four environments, mean prevalence of tag sequences rose with depth up to 50,000, so 5,000 under-estimated prevalence.

- conf: not stated
- class: not stated
- holds: EMP
- src: thompsonCommunalCatalogueReveals2017
- trail: MB-01 §3.3, §answers

From the note:

> **Large survey.** The EMP averaged 80,000 sequences per sample over 27,751 samples and rarefied to 5,000 (Thompson 2017).
>
> In four environments, mean prevalence of tag sequences rose with depth up to 50,000, so 5,000 under-estimated prevalence.
>
> Reads per sample.
>
> The EMP averaged 80,000 per sample over 27,751 samples (Thompson 2017).
>

## H2-04/covariation-sources.3 (claim)

On the reviewer's own generalisation, the literature rarely names more than two of these sources in the same study; the review gives no source for it.

- conf: not stated
- class: reading (critic: H2-04:C-111)
- holds: section 1 of the review, without a source
- src: none (the reviewer's generalisation)
- trail: H2-04 §What the question contains, §Adversarial critique

From the note:

> - Section 1 asserts, without a source, that the literature 'rarely names more than two [sources] in the same study'. This is the reviewer's generalisation presented as a property of the field.
>

## H1-02/pathway-completeness.1 (claim)

Regressing DRAM KEGG module fullness on CheckM completeness across 11,842 GTDB genomes, a rise in completeness from 70% to 100% was associated with a 15 ± 10% increase in module fullness, and the association held above 90% completeness.

- conf: not stated
- class: meas (note: "treated here as a measured association")
- holds: 11,842 GTDB genomes; the search agents disagreed on its class (measured against inferred); a measured association with an inferred causal reading
- src: eisenhoferImpactMicrobialGenome2023
- trail: H1-02 §2.5, §Search record

From the note:

> Eisenhofer et al. [3] regressed DRAM KEGG module fullness on CheckM completeness across 11,842 GTDB genomes.
>
> A rise in completeness from 70% to 100% was associated with a 15 ± 10% increase in module fullness, and the association held above 90% completeness.
>
> The search agents disagreed on its class (measured versus inferred); it is treated here as a measured association with an inferred causal reading.
>
> The agents disagreed on the evidence class of [3] (measured against inferred) and on whether [13] and [24] were usable.
>

## H1-06/uncontrolled-rank-studies.10 (claim)

Apart from the one controlled reanalysis, the rank-wise studies are uncontrolled, and two are preprints.

- conf: not stated
- class: not stated
- holds: Mayjonade 2024 and Chakraverti-Wuerthwein 2026 are the preprints
- src: mayjonadeRelativeEffectsAbiotic2024, chakravertiwuerthweinPhylogeneticCoherenceMicrobiome2026
- trail: H1-06 §5. Bounds and failure modes

From the note:

> The other rank-wise studies are uncontrolled, and two are preprints [24, 29].
>

## H1-02/same-sample-isolate.8 (claim)

Sequence not classified as Enterobacteriaceae averaged 4.4% of the MAGs, above the MiGA contamination estimates (0.9% to 2.7%).

- conf: single (note: "These figures are SINGLE SOURCE")
- class: not stated
- holds: one species in one low-diversity host environment
- src: mezitiReliabilityMetagenomeassembledGenomes2021
- trail: H1-02 §2.1

From the note:

> Sequence not classified as Enterobacteriaceae averaged 4.4%, above the MiGA contamination estimates (0.9% to 2.7%).
>
> These figures are SINGLE SOURCE for one species in one low-diversity host environment.
>

## CB3/n2o.1 (claim)

AR6 Table 7.1: total net anthropogenic N2O is 9.4 ± 5.6 MtN2O yr−1, or 2.6 ± 1.5 GtCO2-eq yr−1, of which AFOLU is 69%.

- conf: not stated
- class: not stated
- holds: 2010–2019; AR6 GWP100
- src: nabuursAgricultureForestryOther2022
- trail: CB3-AG-EMISSIONS §Boundary D

From the note:

> **All anthropogenic N2O.** AR6 Table 7.1: total net anthropogenic N2O is 9.4 ± 5.6 MtN2O yr−1, or 2.6 ± 1.5 GtCO2-eq yr−1, of which AFOLU is 69% [1].
>

## TSL/minimum-support.4 (claim)

Schofield et al. (2017) found that removing very-low-frequency terms has negligible impact, partly undermining the "too specific to matter" belief.

- conf: not stated
- class: not stated
- holds: topic models
- src: schofieldPullingOutStops2017
- trail: TSL §4. Minimum-support

From the note:

> Schofield et al. (2017) found removing very-low-frequency terms has negligible impact, partly undermining the "too specific to matter" belief.
>

## 16S/dns.43 (do not say)

"Occupancy-based core methods performed best" as an established standard.

- why: rests on one simulation study (Custer 2023)
- instead: term-sensitivity.7
- trail: MB-02 §Adversarial

From the note:

> - D2: 'Occupancy-based core methods performed best' rests on one simulation study (Custer et al. 2023 [52]) and is listed among proposed standards as if established.
>

## CB3/co2-accounting.1 (claim)

The CO2 accounting method (bookkeeping models versus national inventories/FAOSTAT) moves AFOLU between 13% and 21% of global emissions; AR6 states this directly.

- conf: not stated
- class: not stated
- holds: AFOLU, 2010–2019, IPCC AR6 WGIII Ch. 7
- src: nabuursAgricultureForestryOther2022
- trail: CB3-AG-EMISSIONS §Where the major sources differ

From the note:

> **CO2 accounting method** (bookkeeping models vs national inventories/FAOSTAT).
>
> AR6 states this directly: it moves AFOLU between 13% and 21% [1].
>

## H1-RES/redundancy.1 (claim)

Chen et al. (2022): across 17 climate zones, taxonomic composition varied widely across climate and edaphic gradients while metagenomic functional attributes (gene abundances) were redundant; taxonomies were more distinct than functional potentials.

- conf: not stated
- class: not stated
- holds: soil metagenomes across the globe, 17 climate zones
- src: chenFunctionalRedundancySoil2022
- trail: H1-RES §Soil redundancy evidence

From the note:

> |  Functional Redundancy in Soil Microbial Community Based on Metagenomics Across the Globe, Huaihai Chen et al., 2022  | Taxonomic composition varied widely across climate and edaphic gradients while metagenomic functional attributes (gene abundances) were redundant; taxonomies were more distinct than functional potentials across 17 climate zones [1].  |
>
> Chen et al. (2022) found taxonomies more distinct than functional potentials across 17 climate zones [1]; Bao et al. (2020) found metabolic composition of straw-degraders conserved across sites where taxonomy was highly variable [3]; and the strongest single statistic, Chen et al. (2021), reported a ~72% loss of taxonomic richness with only limited change in functional-category abundances [6].
>

## H1-06/ph-preference.3 (claim)

Correlogram Moran's I for pH preference stayed below 0.25 at every depth, shallow ones included.

- conf: single (critic: C-001)
- class: meas (critic: C-001)
- holds: the same five datasets; natural systems
- src: ramonedaBuildingGenomebasedUnderstanding2023
- trail: H1-06 §2. Part A1, §answers, §critic

From the note:

> Correlogram Moran's I stayed below 0.25 at every depth, shallow ones included.
>
> Natural-system field evidence (Ramoneda 2023, SILVA 138, 16S trees) gives weak signal for pH preference (Pagel's lambda 0.22 to 0.78, Moran's I < 0.25 at all depths), while a preprint (Chakraverti-Wuerthwein 2026) reports strong phylogenetic signal in the loadings of the pH-aligned canonical axis of global topsoil composition.
>
> **Reformulated verdict:** A1 (environmental preferences): natural systems, measured for pH only, SINGLE SOURCE (Ramoneda et al. 2023).
>
> Signal is significant in 4 of 5 datasets but weak (Pagel's lambda 0.22 to 0.78, Moran's I < 0.25 at all depths), there is no consenTRAIT-style depth, and families span 3.7 to 4.2 pH units.
>
> Checks against sources: Ramoneda's lambda, Moran's I, the phylum quote, R2 = 0.21 / MAE 0.93, 6 to 24% GTDB matches and ~35% MAG/SAG all verified.
>

## CB1/emission-factor.10 (claim)

West and McBride estimated 4.4–6.6 Tg CO₂ for the US in 2001 from 20–30 Tg of aglime.

- conf: not stated
- class: not stated
- holds: United States, 2001
- src: westContributionAgriculturalLime2005
- trail: CB1-LIMING §4. Carbon dioxide

From the note:

> They estimated 4.4–6.6 Tg CO₂ for the US in 2001 from 20–30 Tg of aglime.
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

## NFERT/emission-share.7 (claim)

Gao and Cabrera Serrenho report that manure emits about 23 t CO₂-equivalent per tonne of N, some 1.9 times an average synthetic fertiliser, because much of its nitrogen is lost.

- conf: not stated
- class: not stated
- holds: manure against an average synthetic fertiliser
- src: gaoGreenhouseGasEmissions2023
- trail: NFERT §Share of emissions

From the note:

> They identify nitrogen-use efficiency as the single most effective mitigation lever, and report that manure emits about 23 t CO₂-equivalent per tonne of N, some 1.9 times an average synthetic fertiliser, because much of its nitrogen is lost.
>

## H1-RES/taxonomy-function.5 (claim)

That environmental preferences explain more variance in pangenome features than phylogenetic inertia suggests that ecological context, not taxonomy alone, determines the stability of functional capacity.

- conf: not stated
- class: reading (note: "suggests that ecological context")
- holds: as pangenome.14
- src: none (cited only as SC1 [37]; the note gives no reference list)
- trail: H1-RES §Taxon-Dependence

From the note:

> The observation that environmental preferences explain more variance in pangenome features than phylogenetic inertia [37] suggests that ecological context, not taxonomy alone, determines the stability of functional capacity.
>

## 16S/ploidy.13 (claim)

That 16S copies per cell scale with origin number more than with genome number in fast growers is the reviewer's inference from one abstract; no source in the review measures 16S copies per cell against origin number.

- conf: not stated
- class: reading (critic: MB-02:C-140)
- holds: inference from Couturier and Rocha 2006 (abstract only)
- src: couturierReplicationassociatedGeneDosage2006 (AB)
- trail: MB-02 §D1.3, §answers, §critic, §Adversarial

From the note:

> In fast growers, origin number is therefore the better guide to 16S dosage than genome number.
>
> Because rRNA operons sit near the origin in fast growers [20], 16S copies per cell scale with origin number more than with genome number; E. coli has about 7.9 to 9.5 rRNA genes per genome equivalent across growth rates (secondary, Bremer and Dennis via BioNumbers [21]).
>
> The claim that 16S copies per cell scale with origin number is the reviewer's inference from an abstract [20]; no source in the review measures it.
>
> - D1(b): 'Because rRNA operons sit near the origin in fast growers, 16S copies per cell scale with origin number more than with genome number' rests on one abstract (Couturier and Rocha 2006 [20]) plus reviewer inference. No source in the review measures 16S copies per cell against origin number.
>
> - D1.3 and the D1(b) answer: '16S copies per cell scale with origin number more than with genome number' is the reviewer's inference from Couturier and Rocha's abstract, presented without a 'reviewer's reading' label.
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

## TSL/altitude-ordering.7 (claim)

No controlled head-to-head exists comparing collection df vs class df vs IC for ordering descriptive cluster labels general→specific; the closest tests (Joho & Sanderson; Yang & Callan) are over WordNet / taxonomy induction, indirect for the label-ordering task.

- conf: not stated
- class: search (note: "no controlled head-to-head exists")
- holds: the sources the review found; the closest tests are WordNet and taxonomy induction
- src: johoDocumentFrequencyTerm2007, yangMetricbasedFrameworkAutomatic2009
- trail: TSL §Verdict, §Open Questions

From the note:

> **The most important negative result:** **no controlled head-to-head exists** comparing collection df vs class df vs IC for *ordering descriptive cluster labels* general→specific.
>
> The closest tests [S4, S5] are over WordNet / taxonomy induction — indirect for the label-ordering task.
>
> **Head-to-head (the core gap):** has any benchmark compared collection df vs class df (c-TF-IDF) vs IC for *ordering cluster labels* general→specific?
>
> Appears **not done**; closest tests are WordNet/taxonomy induction (indirect).
>

## H2-01/direct-dimension.17 (claim)

In each direct estimate, n is small or only about half the variance is in the leading axes.

- conf: not stated
- class: not stated
- holds: Jiang2012 (n = 45), Piton2023 (about half the variance in two axes)
- src: none (the reviewer's synthesis)
- trail: H2-01 §answers

From the note:

> But in each case n is small or only about half the variance is in the leading axes, and the leading structure is partly a shared mean profile (profiles barely change when genes are permuted across samples [Sun2020]; HMP pathway levels much more constant than taxa [HMP2012]) or a genome-size axis (Piton axis 1 vs genome size R2 0.64; genome size and normalisation effects [Nayfach2015; Manor2015]).
>

## CB1/soil-carbon.1 (claim)

Holland et al., in a UK review, state that "the impacts of liming on soil carbon storage are variable and strongly relate to soil type, land use, climate and multiple management factors."

- conf: not stated
- class: not stated
- holds: UK review
- src: hollandLimingImpactsSoils2018 (abstract or structured summary only)
- trail: CB1-LIMING §5. Where the numbers

From the note:

> Holland et al., in a UK review, state that "the impacts of liming on soil carbon storage are variable and strongly relate to soil type, land use, climate and multiple management factors" [15].
>
> **Read as abstract or structured summary only**: Wang et al. (2021) [11]; Cho et al. (2019) [12]; Rousset et al. (2024) [13]; Silva et al. (2025) [14]; Holland et al. (2018) [15]; Aramburu Merlos et al. (2023), where I read the full text but used only its framing [16]; Li et al. (2024), where numbers came from an automated extraction of the full article rather than a line-by-line read [17].
>

## CB1/consumption.3 (claim)

About 1% of 1.5 billion tonnes is arithmetically about 15 Mt.

- conf: not stated
- class: deriv (note: "arithmetically")
- holds: the reviewer's arithmetic on the USGS share
- src: none (the reviewer's arithmetic)
- trail: CB1-LIMING §2. Consumption

From the note:

> USGS reports that about 1% of the 1.5 billion tonnes of crushed stone produced in the US in 2024 went to agricultural uses [3], which is arithmetically about 15 Mt — and earlier editions put the share at 2%.
>

## CB3/synthetic-fertiliser.6 (claim)

EDGAR's 0.4 Gt and FAOSTAT's 0.601 Gt for the same quantity, field N2O from synthetic fertiliser, differ by roughly 50%; neither source the review read states a reason for this gap, and AR6 notes only that FAOSTAT, EDGAR and USEPA global means "are within the uncertainty bounds of EDGAR" given assessed uncertainties of 30% (CH4) and 60% (N2O).

- conf: not stated
- class: not stated
- holds: 2019; EDGAR via AR6 Figure 7.3 and FAOSTAT Table 1; AR6 Table 7.1 footnote c
- src: nabuursAgricultureForestryOther2022, tubielloPrePostproductionProcesses2022
- trail: CB3-AG-EMISSIONS §Boundary D

From the note:

> EDGAR's 0.4 Gt and FAOSTAT's 0.601 Gt for the *same* quantity — field N2O from synthetic fertiliser — differ by roughly 50%.
>
> Neither source I read states a reason for this specific gap; AR6 notes only that FAOSTAT, EDGAR and USEPA global means "are within the uncertainty bounds of EDGAR" given assessed uncertainties of 30% (CH4) and 60% (N2O) [1, Table 7.1 fn c].
>

## 16S/absolute-quantification.11 (claim)

qPCR and sequencing both count extracellular DNA, unlike cell counts.

- conf: not stated
- class: not stated
- holds: Jian 2020
- src: jianQuantitativePCRProvides2020
- trail: MB-01 §5.5

From the note:

> - qPCR and sequencing both count extracellular DNA, unlike cell counts (Jian 2020).
>

## H1-02/annotation-coverage.1 (claim)

UHGG core genes had KEGG annotation for a median of 69% of genes, while accessory genes had significantly more unknowns.

- conf: not stated
- class: meas (note: "These are measured, gut only")
- holds: human gut only
- src: almeidaUnifiedCatalog2042020
- trail: H1-02 §3.6

From the note:

> UHGG core genes had KEGG annotation for a median of 69% of genes, while accessory genes had significantly more unknowns [10].
>
> These are measured, gut only.
>

## H1-RES/n-cycle-hgt.26 (claim)

The sub-claim that key nitrogen-cycle genes move horizontally across soil bacterial taxa is supported by substantial evidence, but it is gene-specific, clade-specific and context-dependent: the strongest signal is in nirK and in specialised nif islands spread across free-living lineages, while vertical inheritance of core nif operons, congruence of nosZ with taxonomy in specific contexts, and the lack of recent HGT signatures in codon usage show that vertical inheritance remains an important force; both processes shaped the distribution of nitrogen-cycle genes, their relative importance varying by gene, lineage and ecological context.

- conf: not stated
- class: not stated
- holds: the Sub-claim 3 studies
- src: none (the reviewer's synthesis)
- trail: H1-RES §Gene-Specific
- rating: "supported by substantial evidence"

From the note:

> The sub-claim that key nitrogen-cycle genes move horizontally across soil bacterial taxa is supported by substantial evidence, but this evidence is gene-specific, clade-specific, and context-dependent.
>
> The strongest HGT signal appears in nirK, with habitat clustering overriding taxonomy, and in specialized nif islands that spread across free-living lineages.
>
> However, the counter-evidence showing vertical inheritance for core nif operons, congruence of nosZ with taxonomy in specific contexts, and lack of recent HGT signatures in codon usage analyses demonstrates that vertical inheritance remains an important evolutionary force.
>
> Instead, the evidence indicates a complex evolutionary history where both vertical inheritance and horizontal transfer have shaped the distribution of nitrogen-cycle genes, with the relative importance of each process varying by gene, lineage, and ecological context.
>

## H1-RES/accessory-function.23 (claim)

A large fraction of accessory content represents structural variation, selfish genetic elements, or genes whose function cannot be inferred from sequence alone.

- conf: not stated
- class: reading (note: "This pattern suggests")
- holds: inferred from the counter-evidence
- src: none (the reviewer's inference)
- trail: H1-RES §Assessment: Context

From the note:

> This pattern suggests that a large fraction of accessory content represents structural variation, selfish genetic elements, or genes whose function cannot be inferred from sequence alone.
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

## H1-02/sample-dependence.10 (claim)

In sediment, dependence was not measured in this setting: the only data are MAG yield against depth in one estuarine data set and habitat-level yield for coastal sediments, and nothing was found on content artefacts.

- conf: not stated
- class: search (critic: C-012)
- holds: natural sediment; MAG yield only
- src: royaltyTheoreticalSimulationBasedInvestigation2019, sereikaGenomeresolvedLongreadSequencing2025
- trail: H1-02 §critic, §Verdict as delivered, §5. Verdicts, §3.4

From the note:

> Part B, soil and sediment: NOT MEASURED IN THIS SETTING, with indirect recovery-quality evidence only.
>
> Dependence on sample properties: sediment (natural)**: NOT MEASURED IN THIS SETTING.
>
> The only data are MAG yield against depth in one estuarine data set [16] and habitat-level yield for coastal sediments [17].
>
> - Sediment: **not measured in this setting** (yield only [16, 17]).
>
> Nothing was found on content artefacts.
>

## CB1/delivered-cost.5 (claim)

The delivered cost is dominated by moving the material, not by obtaining it: roughly 5.5 ETB/Qt at the quarry against 60–163 ETB/Qt to transport it to a rural distribution point, so the rock at the quarry costs roughly an order of magnitude less than moving it. This is the clearest published cost breakdown showing transport dominance the reviewer found.

- conf: not stated
- class: not stated
- holds: Ethiopia
- src: oumerAgriculturalLimeValue2023
- trail: CB1-LIMING §3. Energy and transport, §Verdict on the scarcity

From the note:

> **The clearest published cost breakdown showing transport dominance is Ethiopian.** Oumer et al. report that a private supplier won a bid to supply core limestone at 47 ETB per cubic metre, equivalent to 5.5 ETB per quintal.
>
> The rock at the quarry costs roughly an order of magnitude less than moving it.
>
> - The delivered cost is dominated by moving the material, not by obtaining it: roughly 5.5 ETB/Qt at the quarry against 60–163 ETB/Qt to transport it to a rural distribution point [8].
>

## TAXRES/gtdb-ncbi-divergence.6 (claim)

Names are converging while the underlying classification basis still differs: the divergence is active and partly converged.

- conf: not stated
- class: reading (note: "So names are converging while the underlying classification basis still differs")
- holds: phylum names, GTDB against NCBI Taxonomy / LPSN
- src: anonHarmonizingProkaryoticNomenclature2022
- trail: TAXRES §The NCBI-vs-GTDB divergence, §Provisional verdicts

From the note:

> So **names are converging while the underlying classification basis still differs**.
>
> **(a) Single authoritative taxonomy across prokaryotes, fungi, plants? — MUST INTEGRATE SEVERAL.** Prokaryotes split between **GTDB** (genome-based, RED-normalised) and **NCBI Taxonomy / LPSN** (nomenclatural code), with an active and partly-converged divergence; fungi sit under Index Fungorum / MycoBank / Fungal Names; the nearest single cross-kingdom backbone is the **Catalogue of Life (eXtended)** that now drives the GBIF Backbone, but it is coarse.
>

## TSL/frequency-bucketing.3 (claim)

No reviewed source benchmarks discrete bands for ordering labels.

- conf: not stated
- class: search (note: "No reviewed source benchmarks discrete bands")
- holds: the sources the review found
- src: none (a statement about what the review found)
- trail: TSL §Verdict

From the note:

> No reviewed source benchmarks discrete bands for *ordering* labels; log binning is only a *proposed* mitigation for distribution analysis [S7b], not validated for label banding.
>

## CB1/delivered-cost.7 (claim)

For the US or Europe, the reviewer found only trade-press and forum material with no verifiable method for a comparable delivered-cost breakdown, and does not report those numbers.

- conf: not stated
- class: search (note: "I searched for a comparable delivered-cost breakdown")
- holds: the reviewer's searches
- src: none (a statement about what the review found)
- trail: CB1-LIMING §3. Energy and transport

From the note:

> I searched for a comparable delivered-cost breakdown for the US or Europe and found only trade-press and forum material with no verifiable method.
>
> I am not reporting those numbers.
>

## 16S/sampling-model.1 (claim)

A Poisson random-sampling model of long-tailed abundance distributions predicted the low OTU overlap among soil technical replicates with no significant difference from the observed values, and about 60,900 sequences per replicate would be needed for 90% overlap.

- conf: single (marker)
- class: model (marker)
- holds: Zhou 2011's 24 Oklahoma grassland soils on 454; the predicted reads for 90% overlap rest on Zhou 2013
- src: zhouRandomSamplingProcess2013 (FT; model; single)
- trail: MB-01 §4.1, §answers

From the note:

> A Poisson random-sampling model predicted these overlaps with no significant difference from the observed values.
>
> About 60,900 sequences per replicate would be needed for 90% overlap (Zhou 2013) [FT; model; single].
>
> **sampling explains much of the replicate variation in taxa detected; extra-sampling variation is real but measured in few studies**: Sampling from the amplified pool.
>
> Poisson or multinomial sampling of long-tailed abundance distributions predicted the low OTU overlap seen among soil technical replicates, with no significant difference from the observed values (Zhou 2013, modelled; 454).
>
> About 60,900 reads were predicted to be needed for 90% overlap (Zhou 2013).
>
> The predicted reads for 90% overlap rest on Zhou 2013.
>

## 16S/copy-number-correction.6 (claim)

In Kembel's data, correction moved ear samples to cluster with nostrils rather than feet but left ocean clustering largely unchanged.

- conf: not stated
- class: not stated
- holds: human body sites and ocean
- src: kembelIncorporating16SGene2012 (FT)
- trail: MB-02 §D1.4, §answers

From the note:

> - **Clustering.** Correction moved ear samples to cluster with nostrils rather than feet, but left ocean clustering largely unchanged [28, FT].
>
> Effects on ecological conclusions are mixed: correction changed the most abundant OTU in about 20% (human) and 31% (Earth Microbiome Project) of communities but left PERMANOVA variance explained essentially unchanged [33]; it changed human body-site clustering but not ocean clustering [28]; it changed enterotype number from two to three [29]; in a forest soil example Acidobacteria rose from 50.1% of sequences to an estimated 66.0% of genomes [6].
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

## NFERT/substitution.3 (claim)

No reviewed source isolates microbial-community efficiency from confounding soil and management variables as the cause of a reduced synthetic requirement at held yield.

- conf: not stated
- class: search (note: "No reviewed source isolates microbial-community efficiency")
- holds: the sources the review read
- src: none (a statement about what the review found)
- trail: NFERT §Verdicts

From the note:

> No reviewed source isolates microbial-community efficiency from confounding soil and management variables as the cause of a reduced synthetic requirement at held yield.
>

## 16S/sampling-model.6 (claim)

The "technical replicates are Poisson" assumption comes from RNA-seq: Illumina lane replicates fit a Poisson model, with about 0.5% of genes deviating; McMurdie and Holmes adopt it for technical replicates, so it rests on RNA-seq, not on 16S technical replicates.

- conf: not stated
- class: meas (marker)
- holds: RNA-seq lane replicates, labelled INDIRECT
- src: marioniRNAseqAssessmentTechnical2008 (FT; meas; INDIRECT), mcmurdieWasteNotWant2014
- trail: MB-01 §4.1, §answers

From the note:

> **Origin of the Poisson assumption.** In RNA-seq, Illumina lane replicates fit a Poisson model, with about 0.5% of genes deviating (Marioni 2008) [FT; meas; INDIRECT].
>
> McMurdie and Holmes adopt this assumption for technical replicates; it rests on RNA-seq, not on 16S technical replicates.
>
> The 'technical replicates are Poisson' assumption comes from RNA-seq lane replicates (Marioni 2008, indirect).
>

## H1-05/null-model.2 (claim)

Not measured: any label-shuffling, trait or phylogenetic null applied to field-soil shotgun, GeoChip, RNA or protein profiles to test whether functional turnover is lower than expected given taxonomic turnover, and nulls across environmental-contrast sizes in soil.

- conf: not stated
- class: search (note: "Not measured")
- holds: soil
- src: none (a search result)
- trail: H1-05 §answers

From the note:

> *Not measured:* Any label-shuffling, trait or phylogenetic null applied to field-soil shotgun, GeoChip, RNA or protein profiles to test whether functional turnover is lower than expected given taxonomic turnover.
>
> Nulls across environmental-contrast sizes in soil.
>

## 16S/index-misassignment.9 (claim)

With mammal and arthropod markers, 2.1 to 2.6% of sequences came from tag jumps.

- conf: not stated
- class: meas (marker)
- holds: other markers, labelled INDIRECT; abstract only
- src: schnellTagJumpsIlluminated2015 (AB; meas; INDIRECT)
- trail: MB-01 §2.8, §answers

From the note:

> | Mammal and arthropod markers | 2.1 to 2.6% of sequences from tag jumps | Schnell 2015 [AB; meas; INDIRECT] |
>
> Tag jumps were 2.1-2.6% (Schnell 2015, other markers).
>

## H1-RES/n-cycle-hgt.3 (claim)

Phylogenetic incongruence studies provide the broadest evidence for HGT of nitrogen-cycle genes; genomic island analyses provide structural evidence, and mobile element documentation direct mechanistic evidence.

- conf: not stated
- class: not stated
- holds: the study types in Sub-claim 3
- src: none (the reviewer's synthesis)
- trail: H1-RES §Multi-Level HGT

From the note:

> Phylogenetic incongruence studies provide the broadest evidence for HGT of nitrogen-cycle genes.
>
> Genomic island analyses provide structural evidence for HGT.
>
> Mobile element documentation provides direct mechanistic evidence.
>

## H1-05/dns.6 (do not say)

"Aggregation alone lowers functional variability, so 'function lower' is not by itself evidence of redundancy", as a methodological point bearing on every soil study, or "Ho and Huang show analytically and by simulation" with a 'Moderate' rating.

- why: it rests on Ho and Huang [29][30] only and is modelled; the 'Moderate' firmness rests on a summary of the preprint, the published version having been read as abstract only (access)
- instead: averaging.1, averaging.10
- trail: H1-05 §Adversarial critique

From the note:

> Moderate as a methodological point, but single source: Ho and Huang [29][30] show analytically and by simulation that aggregation alone lowers functional variability, so 'function lower than taxonomy' is not by itself evidence of redundancy or selection.
>
> - [29] Cell Systems version: abstract only, yet the D3 answer says the method 'shows analytically and by simulation' and rates it 'Moderate'. That firmness rests on a summary of the preprint.
>
> - D3: 'aggregation alone lowers functional variability, so function lower is not by itself evidence of redundancy' is framed as a methodological point bearing on every soil study. It rests on Ho and Huang [29][30] only, and is modelled.
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

