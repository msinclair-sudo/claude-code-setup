---
type: knowledge
title: Sources of functional covariation and cross-level functional axes
inputs:
  - "H2-04: PhD/Proposal/Research/Results/Sources of functional covariation across microbial community samples, their partition, and the relation between genome-level and community-level functional axes a literature review.md"
refs: PhD/Proposal/Refs/Refs.bib
built: 2026-10-22
status: draft
tags:
  - research
  - knowledge
---
# Sources of functional covariation and cross-level functional axes

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
| H2-04 | [[Sources of functional covariation across microbial community samples, their partition, and the relation between genome-level and community-level functional axes a literature review]] | yes | labelled (access; class; standing) | yes (12 of 47 labels) | no | exact |

## Concepts

### covariation-sources: sources of covariation among functions in community profiles
needs: none
- **covariation-sources.1** Five sources of covariation among functions across community samples are each identified in the literature, but by largely separate communities and almost always for taxa, not for function-by-sample tables.
  conf: not stated · class: not stated · holds: the critic: each source is named somewhere, almost always for taxa · src: none (the reviewer's synthesis of the cases below) · trail: H2-04 §answers, §critic · from: H2-04:A-001, H2-04:C-002, H2-04:C-008 · rating: "moderate for existence at the taxon level, weak or indirect at the function level"
- **covariation-sources.2** No study was found that names all five sources for the same function-by-sample table.
  conf: not stated · class: search (note: "No study found") · holds: routes: Europe PMC REST keyword searches, Crossref, OpenAlex, PMC full text, three independent search angles (complementarity, co-occurrence, trait ecology); WebSearch and Scholar Gateway unavailable · src: none (a search result) · trail: H2-04 §answers · from: H2-04:A-009, H2-04:A-011
- **covariation-sources.3** On the reviewer's own generalisation, the literature rarely names more than two of these sources in the same study; the review gives no source for it.
  conf: not stated · class: reading (critic: H2-04:C-111) · holds: section 1 of the review, without a source · src: none (the reviewer's generalisation) · trail: H2-04 §What the question contains, §Adversarial critique · from: H2-04:C-111
- **covariation-sources.4** The claims that each source exists survive removal of any one source.
  conf: not stated · class: not stated · holds: the review's single-source sensitivity check for case D1(a) · src: none (the review's sensitivity check) · trail: H2-04 §answers · from: H2-04:A-016

### genome-linkage: linkage of functions within genomes
needs: covariation-sources
- **genome-linkage.1** Across 396 human gut metagenomes, co-abundance binning clustered genes into 7,381 co-abundance groups, including 741 metagenomic species, from which 238 high-quality genomes were assembled: gene covariation across metagenomes is strongly structured by genome membership, but no share of total gene covariation attributable to genome membership is reported.
  conf: single (critic: H2-04:C-003) · class: meas (marker) · holds: human gut metagenomes (n = 396), gene level; the critic: within-genome linkage at gene level rests on one abstract, with no covariance share · src: metahitIdentificationAssemblyGenomes2014 (AB; measured; replicated method family) · trail: H2-04 §Linkage within genomes, §answers, §critic · from: H2-04:I-0003, H2-04:A-002, H2-04:A-017, H2-04:C-003, H2-04:C-045 · limit: access and evidence (note: "rests on Nielsen et al. 2014 (abstract only)")
- **genome-linkage.2** In 2,540 aquifer genomes, most organisms carried one step of sequential redox pathways, few carried two, and very few three or more (a stepwise division of redox pathways across genomes); the authors argue incompleteness does not explain this.
  conf: single (marker) · class: deriv (marker) · holds: one aquifer system; community composition and genomes from the same metagenomes; the critic: one aquifer study, not a class of functions · src: anantharamanThousandsMicrobialGenomes2016 (FT; derived; single study) · trail: H2-04 §Linkage within genomes, §answers, §Adversarial critique · from: H2-04:I-0004, H2-04:A-042, H2-04:C-066
- **genome-linkage.3** Genome incompleteness produces false gene absences: predicted auxotrophies correlate negatively with genome completeness, and model auxotrophy sensitivity falls with genome incompleteness.
  conf: not stated · class: not stated · holds: genome-derived auxotrophy predictions · src: starkeAminoAcidAuxotrophies2023 (FT) · trail: H2-04 §Linkage within genomes, §answers · from: H2-04:I-0005, H2-04:A-044
- **genome-linkage.4** Annotation gaps produce apparent pathway holes: 9 of 11 amino-acid gaps in 10 genera were filled by unannotated enzymes; predicted auxotrophies are often annotation gaps.
  conf: not stated · class: meas (marker) · holds: amino-acid biosynthesis pathways, 10 genera · src: priceFillingGapsBacterial2018 (AB; measured) · trail: H2-04 §Linkage within genomes, §answers · from: H2-04:I-0005, H2-04:A-044
- **genome-linkage.5** Horizontal gene transfer is 25-fold more frequent among human-associated bacteria than among ecologically diverse non-human isolates, and is structured by shared habitat; it is concentrated among co-habitants, which can generate shared gene content without shared ancestry.
  conf: single (marker) · class: deriv (marker) · holds: human-associated bacteria versus ecologically diverse non-human isolates; the critic: rests on one abstract, yet used in D1(c) as a general caution · src: smillieEcologyDrivesGlobal2011 (AB; derived; single study) · trail: H2-04 §Linkage within genomes, §answers, §Adversarial critique · from: H2-04:I-0005, H2-04:A-045, H2-04:C-067
- **genome-linkage.6** No source was found that quantifies the effect of contamination on measured within-genome linkage.
  conf: not stated · class: search (critic: H2-04:C-089) · holds: the review's search routes; the critic names MAG contamination and chimerism work not covered · src: none (a search result) · trail: H2-04 §Linkage within genomes, §Adversarial critique · from: H2-04:C-089

### association-networks: co-occurrence and association networks among taxa
needs: covariation-sources, shared-environment
group: networks-environment
- **association-networks.bg1** Microbiome datasets generated by high-throughput sequencing (16S rRNA amplicon, metagenome, metatranscriptome) are compositional, because the instrument imposes an arbitrary total on each sample.
  kind: background · ref: gloorMicrobiomeDatasetsCompositional2017 · check: DOI resolves on Crossref (Frontiers in Microbiology 8:2224, 2017); stated in the abstract (Semantic Scholar record)
- **association-networks.1** Taxon co-occurrence networks have been built in quantity; Fierer et al. 2014, cited among them by the review, is a community-aggregated-traits perspective, not a network study, and is removed from the list.
  conf: not stated · class: not stated · holds: taxon (16S) networks · src: barberanUsingNetworkAnalysis2011, faustMicrobialCooccurrenceRelationships2012, levyMetabolicModelingSpecies2013, fiererSeeingForestGenes2014 (AB; not a network study, critic: H2-04:C-004) · trail: H2-04 §Taxon networks, §critic · from: H2-04:A-003, H2-04:C-004, H2-04:C-047, H2-04:C-073..075
- **association-networks.2** Eight correlation tools run on the same simulated data shared on average 31.5% of edges; constraining totals produced incorrect edges for most tools, worst below an effective species number of about 13; the best precision for sparse Lotka-Volterra relations was 0.2.
  conf: repl (marker) · class: model (marker) · holds: simulated data, eight tools; the critic: these figures are unverified (the PMC XML was not retrievable in the critique) · src: weissCorrelationDetectionStrategies2016 (FT; modelled; replicated) · trail: H2-04 §Taxon networks, §Adversarial critique · from: H2-04:I-0006, H2-04:I-0002, H2-04:C-060, H2-04:C-100 · limit: access (critic: H2-04:C-060)
- **association-networks.3** Compositional closure alone can flip correlation signs; on HMP data, standard correlation was estimated to give about 3 spurious edges per true one, relative to SparCC as reference, not relative to known truth.
  conf: not stated · class: model (marker) · holds: HMP data; SparCC as the reference · src: friedmanInferringCorrelationNetworks2012 (AB; modelled) · trail: H2-04 §Taxon networks · from: H2-04:I-0007, H2-04:I-0002
- **association-networks.4** Whether compositionally aware methods remove closure artefacts is in conflict: their own benchmarks say they beat other methods, while an independent population-dynamics simulation found them no better than Pearson correlation (and better at recovering competition than predator-prey relations).
  conf: cont (note: "Conflicts: Whether compositionally aware methods remove closure artefacts") · class: model (marker) · holds: the methods' own benchmarks versus one independent population-dynamics simulation · src: kurtzSparseCompositionallyRobust2015 (AB), hiranoDifficultyInferringMicrobial2019 (FT; modelled) · trail: H2-04 §Taxon networks, §answers · from: H2-04:I-0008, H2-04:A-008
- **association-networks.5** Two gut species pairs from a network were co-cultured and behaved as the edges predicted (n = 2).
  conf: single (marker) · class: meas (marker) · holds: human gut species, two pairs · src: dasVitroCoculturesHuman2018 (FT; measured; single study; listed in references as 6a) · trail: H2-04 §Taxon networks · from: H2-04:I-0009
- **association-networks.6** In a non-microbial rocky-intertidal system, a co-occurrence network matched an independently resolved interaction network at about chance (sensitivity 0.469, specificity 0.527).
  conf: not stated · class: meas (marker) · holds: non-microbial, rocky intertidal; figures checked by the critic · src: freilichSpeciesCooccurrenceNetworks2018 (AB; measured; non-microbial) · trail: H2-04 §Taxon networks, §critic · from: H2-04:I-0010, H2-04:C-045
- **association-networks.7** Co-occurrence is a poor proxy for interaction (a theoretical and review conclusion, non-microbial).
  conf: not stated · class: assert (marker) · holds: non-microbial · src: blanchetCooccurrenceNotEvidence2020 (AB; asserted; non-microbial) · trail: H2-04 §Taxon networks, §answers · from: H2-04:I-0011, H2-04:A-045
- **association-networks.8** The meaning of network edges is uncertain, and strategies to remove environmental edges have not been systematically compared.
  conf: not stated · class: assert (marker) · holds: theoretical and review papers · src: faustOpenChallengesMicrobial2021 (FT; asserted) · trail: H2-04 §Taxon networks · from: H2-04:I-0011
- **association-networks.9** Correlation almost never gives reliable information on direct biotic interactions in real ecosystems.
  conf: not stated · class: assert (marker) · holds: theoretical and review papers · src: carrUseAbuseCorrelation2019 (SEC; asserted; critic: H2-04:C-052..054 was "FT-s; asserted") · trail: H2-04 §Taxon networks, §Adversarial critique · from: H2-04:I-0011, H2-04:A-045, H2-04:C-052..054 · limit: access (critic: H2-04:C-054)
- **association-networks.10** In macroecology, joint species distribution models cannot separate environment from interaction.
  conf: not stated · class: deriv (marker) · holds: macroecology, non-microbial · src: poggiatoInterpretationsJointModeling2021 (AB; derived) · trail: H2-04 §Taxon networks · from: H2-04:I-0012
- **association-networks.11** Residual correlations in joint species distribution models depend on prevalence.
  conf: not stated · class: model (marker) · holds: macroecology · src: zurellDoJointSpecies2018 (AB; modelled) · trail: H2-04 §Taxon networks · from: H2-04:I-0012
- **association-networks.12** Metacommunity disturbance alone can generate associations between non-interacting species.
  conf: not stated · class: model (marker) · holds: macroecology; a preprint · src: calcagnoMetacommunityDynamicsDetection2021 (AB; modelled; preprint) · trail: H2-04 §Taxon networks · from: H2-04:I-0012
- **association-networks.13** The 16S taxonomy reference database contributed 65.4% of the variance among inferred taxon networks, and OTU processing 26.8%; this concerns taxonomic, not functional, annotation, so it is indirect for function profiles.
  conf: single (marker) · class: meas (marker) · holds: amplicon data, taxon networks, pipeline steps; figures checked by the critic against full text; the critic: says nothing directly about functional annotation schemes · src: kishoreInferringMicrobialCooccurrence2023 (FT; measured; single study) · trail: H2-04 §Taxon networks, §answers, §critic · from: H2-04:I-0013, H2-04:I-0002, H2-04:A-023, H2-04:A-017, H2-04:C-005, H2-04:C-006, H2-04:C-045, H2-04:C-064

### shared-environment: shared response to environment
needs: covariation-sources, association-networks
group: networks-environment
- **shared-environment.1** Environmental heterogeneity is argued to be usually the strongest driver of correlation structure.
  conf: single (critic: H2-04:C-068) · class: assert (marker) · holds: asserted, and read only via tool summary · src: carrUseAbuseCorrelation2019 (SEC; asserted; critic: H2-04:C-052..054 was "FT-s; asserted") · trail: H2-04 §Shared response to environment, §Adversarial critique · from: H2-04:I-0029, H2-04:I-0001, H2-04:C-007, H2-04:C-068, H2-04:C-052..054 · limit: access (critic: H2-04:C-068)
- **shared-environment.2** In simulation, co-occurrence networks lose interpretability when habitat filtering is significant.
  conf: not stated · class: model (marker) · holds: simulation · src: berryDecipheringMicrobialInteractions2014 (AB; modelled) · trail: H2-04 §Shared response to environment · from: H2-04:I-0029, H2-04:I-0001
- **shared-environment.3** In a 10-year monthly marine association network of 29,820 taxon edges, four methods classified 8.3% (intersection of the four) to 24.8%, 25.7% and 84.6% (individual methods) of edges as environmentally driven; in simulation the individual methods also removed 38 to 86% of true interactions, and the intersection approach removed 25%.
  conf: single (marker) · class: meas/model (marker) · holds: one marine time series, taxon association edges; figures rechecked by the reviewer and checked by the critic against full text · src: deutschmannDisentanglingEnvironmentalEffects2021 (FT; measured and modelled; single study; figures rechecked by the reviewer against full text) · trail: H2-04 §Shared response to environment, §answers, §critic · from: H2-04:I-0030, H2-04:I-0001, H2-04:A-020, H2-04:C-011, H2-04:C-012, H2-04:C-045
- **shared-environment.4** The environment-driven share of edges is method-dependent (the methods disagree by an order of magnitude, 8.3% to 84.6%), limited to measured environmental factors, and of low reliability.
  conf: not stated · class: not stated · holds: Deutschmann et al. 2021 · src: deutschmannDisentanglingEnvironmentalEffects2021 · trail: H2-04 §answers · from: H2-04:A-021, H2-04:A-030
- **shared-environment.5** Ocean functional groups track environment strongly while taxonomy within groups does not; the functional groups are assigned from taxonomy, so they are not independent of composition.
  conf: cont (marker) · class: deriv (marker) · holds: the global ocean · src: loucaDecouplingFunctionTaxonomy2016 (AB; derived; functional groups assigned from taxonomy, so not independent of composition; contested) · trail: H2-04 §Shared response to environment · from: H2-04:I-0031
- **shared-environment.6** Enrichment communities converge in function and in family-level taxonomy under a given carbon source.
  conf: not stated · class: meas (marker) · holds: enrichment communities; the cross-feeding mechanism modelled · src: goldfordEmergentSimplicityMicrobial2018 (AB; measured, with the cross-feeding mechanism modelled) · trail: H2-04 §Shared response to environment · from: H2-04:I-0032
- **shared-environment.7** A consumer-resource model reproduces survey-level patterns from shared environments.
  conf: not stated · class: model (marker) · holds: a model · src: marslandMinimalModelMicrobial2020 (AB; modelled) · trail: H2-04 §Shared response to environment · from: H2-04:I-0033
- **shared-environment.8** Much of the environment argument is asserted (perspectives) rather than measured: the shared-environment source rests on an assertion read through a tool summary plus one taxon-level measured partition.
  conf: not stated · class: not stated · holds: the critic: Carr 2019 plus Deutschmann 2021 · src: carrUseAbuseCorrelation2019, deutschmannDisentanglingEnvironmentalEffects2021 · trail: H2-04 §answers, §critic · from: H2-04:A-007, H2-04:C-007

### shared-ancestry: shared ancestry of the organisms carrying functions
needs: covariation-sources
- **shared-ancestry.1** Phylogeny is the largest single predictor of pairwise co-occurrence among the indices tested.
  conf: single (critic: H2-04:C-065) · class: not stated · holds: pairwise co-occurrence of gut taxa; four genomic indices tested; the data of Levy & Borenstein reused · src: kamnevaGenomeCompositionPhylogeny2017 (FT) · trail: H2-04 §Shared ancestry, §answers, §Adversarial critique · from: H2-04:A-004, H2-04:C-065
- **shared-ancestry.2** Co-occurring and positively associated taxa are phylogenetically close and functionally similar; in HMP data, positive associations were enriched for phylogenetic and functional similarity.
  conf: not stated · class: deriv (marker) · holds: HMP data (Faust 2012) · src: chaffronGlobalNetworkCoexisting2010 (FT), faustMicrobialCooccurrenceRelationships2012 (FT; derived) · trail: H2-04 §Shared ancestry, §answers · from: H2-04:A-004, H2-04:I-0017
- **shared-ancestry.3** At the community level, genomic trait distance tracks UniFrac distance (R2 = 0.32).
  conf: not stated · class: not stated · holds: community level; the critic: the R2 = 0.32 could not be rechecked · src: pitonLifeHistoryStrategies2023 (FT) · trail: H2-04 §Shared ancestry, §answers, §Adversarial critique · from: H2-04:A-004, H2-04:C-058 · limit: access (critic: H2-04:C-058)

### aggregation-artefacts: artefacts of aggregating and weighting unit-level values into community profiles
needs: covariation-sources
- **aggregation-artefacts.bg1** Community-aggregated trait values are computed from species' trait values weighed according to the relative abundance of the species in the community.
  kind: background · ref: garnierPlantFunctionalMarkers2004 · check: DOI resolves on Crossref (Ecology 85(9):2630-2637, 2004); stated in the abstract (Europe PMC record: community-aggregated traits "weighed according to the relative abundance of species")
- **aggregation-artefacts.1** Community means of randomly assigned species attributes correlate with each other and with richness through repeated species co-occurrence alone, with variance explained rising with co-occurrence.
  conf: not stated · class: model (marker) · holds: non-microbial community and assemblage data · src: hawkinsStructuralBiasAggregated2017 (AB; modelled; non-microbial) · trail: H2-04 §Artefacts of aggregation · from: H2-04:I-0034, H2-04:I-0002
- **aggregation-artefacts.2** Standard tests of community-weighted mean versus environment have inflated Type I error that rises as beta diversity falls.
  conf: not stated · class: model (marker) · holds: trait ecology · src: zelenyWhichResultsStandard2018 (AB; modelled) · trail: H2-04 §Artefacts of aggregation · from: H2-04:I-0035
- **aggregation-artefacts.3** The fourth-corner approach is proposed as a remedy for the inflated community-weighted mean tests.
  conf: not stated · class: not stated · holds: trait ecology · src: peresnetoLinkingTraitVariation2017 (AB) · trail: H2-04 §Artefacts of aggregation · from: H2-04:I-0035
- **aggregation-artefacts.4** Abundance-weighted versus species-weighted aggregation changed the sign of 27% of significant trait-climate results.
  conf: single (marker) · class: meas (marker) · holds: trait ecology (trait-climate results); figure checked by the critic against the abstract · src: wieczynskiClimateShapesShifts2018 (AB; measured; single study) · trail: H2-04 §Artefacts of aggregation, §critic · from: H2-04:I-0036, H2-04:I-0002, H2-04:C-045

### gene-level-networks: networks built among functions
needs: association-networks, genome-linkage
- **gene-level-networks.1** GeoChip functional-gene networks in grassland soil differed between ambient and elevated CO2, and their links were interpreted as interactions among the populations carrying the genes.
  conf: not stated · class: meas (marker) · holds: grassland soil; profiles independent of any genome set · src: zhouFunctionalMolecularEcological2010 (FT; measured; profiles independent of any genome set) · trail: H2-04 §Gene-level networks, §answers · from: H2-04:I-0014, H2-04:A-003
- **gene-level-networks.2** A KO co-occurrence network from a decade of monthly marine metagenomes found vitamin metabolism the most connected pathway.
  conf: not stated · class: meas (marker) · holds: monthly marine metagenomes over a decade; MAGs from the same metagenomes; a preprint · src: arandiagorostidiMetagenomicbasedNetworkAnalysis2025 (SEC; measured; preprint; critic: H2-04:C-052..054 was "FT-s; measured; preprint; MAGs from the same metagenomes") · trail: H2-04 §Gene-level networks, §Adversarial critique · from: H2-04:I-0015, H2-04:A-003, H2-04:C-052..054 · limit: access (critic: H2-04:C-054)
- **gene-level-networks.3** On the reviewer's reading, neither gene-level network study removes within-genome linkage, closure or environment; both interpret their edges as interactions among populations.
  conf: not stated · class: reading (note: "on the reviewer's reading") · holds: the two gene-level network studies; the critic: gene-level network interpretation rests on Zhou 2010 and one preprint · src: zhouFunctionalMolecularEcological2010, arandiagorostidiMetagenomicbasedNetworkAnalysis2025 · trail: H2-04 §Gene-level networks, §answers · from: H2-04:A-003, H2-04:C-070
- **gene-level-networks.4** The only direct work on gene-level (as opposed to taxon-level) covariation is two single studies that do not separate sources.
  conf: single (note: "two single studies") · class: not stated · holds: gene-level networks · src: zhouFunctionalMolecularEcological2010, arandiagorostidiMetagenomicbasedNetworkAnalysis2025 · trail: H2-04 §answers · from: H2-04:A-006 · rating: "Weak"
- **gene-level-networks.5** Gene-level networks controlling for within-genome linkage were not found.
  conf: not stated · class: search (note: "were not found") · holds: the routes of case D1(a) · src: none (a search result) · trail: H2-04 §answers · from: H2-04:A-010

### covariance-partition: partitions of covariation among sources
needs: covariation-sources, shared-environment, shared-ancestry, association-networks
- **covariance-partition.1** No study was found that partitions covariation among functions in community profiles into within-genome linkage, organism co-occurrence, shared environment, shared ancestry and artefact shares; the partitions that exist are of other quantities.
  conf: not stated · class: search (note: "No study found") · holds: routes as in case D1(a), plus Europe PMC queries on community-aggregated traits with covariation and trade-off terms, and on strain-level versus taxonomic turnover; the critic: an absence that is the review's own search result, with routes named · src: none (a search result) · trail: H2-04 §answers, §critic · from: H2-04:A-018, H2-04:A-019, H2-04:A-033, H2-04:C-010, H2-04:C-116
- **covariance-partition.2** In pairwise co-occurrence of gut taxa, phylogeny explains 9.84% of the variance and the genomic indices add about 3.81%, so most variance is unexplained.
  conf: not stated · class: deriv (marker) · holds: pairwise co-occurrence of gut taxa, the data of Levy & Borenstein; figures checked by the critic against full text · src: kamnevaGenomeCompositionPhylogeny2017 (FT; derived; not independent of 17) · trail: H2-04 §Complementarity versus overlap, §answers, §critic · from: H2-04:A-022, H2-04:I-0019, H2-04:C-013, H2-04:C-045
- **covariance-partition.3** Handling of turnover, closure and depth in the microbial partitions: Deutschmann used relative abundances with no log-ratio treatment reported in the findings; Kamneva used Jaccard presence data; Piton normalised by annotated reads and log(x+1), with no log-ratio treatment and 5 to 15% of reads annotated.
  conf: not stated · class: not stated · holds: the three microbial studies; the critic: the 5 to 15% figure could not be rechecked · src: deutschmannDisentanglingEnvironmentalEffects2021, kamnevaGenomeCompositionPhylogeny2017, pitonLifeHistoryStrategies2023 · trail: H2-04 §answers, §Adversarial critique · from: H2-04:A-026, H2-04:C-058
- **covariance-partition.4** Every microbial partition found is a single study with its own denominator, so the shares cannot be pooled.
  conf: single (note: "single study") · class: not stated · holds: the microbial partitions of case D1(b) · src: none (the review's assessment of its sources) · trail: H2-04 §answers, §critic · from: H2-04:A-027, H2-04:A-028, H2-04:C-016 · rating: "Weak"
- **covariance-partition.5** The only quantitative environmental-share partition for microbial associations is Deutschmann et al. 2021; removing it leaves only asserted statements.
  conf: single (note: "Single-source sensitivity: Yes") · class: not stated · holds: microbial associations · src: deutschmannDisentanglingEnvironmentalEffects2021 · trail: H2-04 §answers · from: H2-04:A-036, H2-04:A-037
- **covariance-partition.6** No partition of function-by-function covariance in metagenomic or genome-derived community profiles, and no microbial analogue of the Lepš-type turnover versus within-taxon decomposition, was found (Lepš et al. 2011 itself not obtained).
  conf: not stated · class: search (note: "Not measured") · holds: the routes of case D1(b) · src: lepsCommunityTraitResponse2011 (not obtained) · trail: H2-04 §answers · from: H2-04:A-032
- **covariance-partition.7** On the reviewer's reading (unlabelled as such in the review), the functional-profile question has been approached from two sides that do not meet.
  conf: not stated · class: reading (critic: H2-04:C-112) · holds: section 10 of the review · src: none (the reviewer's synthesis) · trail: H2-04 §How the cases relate, §Adversarial critique · from: H2-04:C-112

### within-between-partition: within-unit versus between-unit trait partitions in plants (non-microbial)
needs: none
- **within-between-partition.1** Species trait covariation split into among-community and within-community components shows strong among-community covariation and weak within-community covariation in California woody plants.
  conf: not stated · class: not stated · holds: California woody plants; non-microbial; species traits · src: ackerlyTraitbasedApproachCommunity2007 (abstract) · trail: H2-04 §Within-unit versus between-unit, §answers, §critic · from: H2-04:A-024, H2-04:C-014, H2-04:C-038
- **within-between-partition.2** In grasslands, 92 to 98% of trait variance lies within communities.
  conf: not stated · class: not stated · holds: grasslands; non-microbial; species traits; rechecked by the reviewer and checked by the critic against full text · src: kembelIndependentEvolutionLeaf2011 (full text, rechecked) · trail: H2-04 §Within-unit versus between-unit, §answers, §critic · from: H2-04:A-024, H2-04:C-014, H2-04:C-045
- **within-between-partition.3** In grasslands, SLA and specific root length correlate positively within communities and negatively among communities, a sign reversal between the two components; it is the only full-text among-versus-within-community sign reversal found, and the plant sign-reversal case rests on it.
  conf: not stated · class: not stated · holds: grasslands; non-microbial · src: kembelIndependentEvolutionLeaf2011 (full text, rechecked) · trail: H2-04 §Within-unit versus between-unit, §answers · from: H2-04:A-024, H2-04:A-073, H2-04:A-038, H2-04:A-083
- **within-between-partition.4** In grasslands, phylogenetic signal is found in within-community trait components only.
  conf: not stated · class: not stated · holds: grasslands; non-microbial · src: kembelIndependentEvolutionLeaf2011 (full text, rechecked) · trail: H2-04 §Within-unit versus between-unit, §Shared ancestry, §answers · from: H2-04:A-024
- **within-between-partition.5** Ackerly & Cornwell find among-community covariation dominant, while Kembel & Cahill find correlations among species means driven by the within-community component; these are different systems.
  conf: not stated · class: not stated · holds: California woody plants versus grasslands · src: ackerlyTraitbasedApproachCommunity2007, kembelIndependentEvolutionLeaf2011 · trail: H2-04 §answers · from: H2-04:A-031
- **within-between-partition.6** Intraspecific variation accounts for 25% of within-community and 32% of among-community trait variance on average across 629 plant communities; this is a variance partition, not a covariance partition, and a different partition (within-species versus between-species) from within- versus among-community components.
  conf: not stated · class: not stated · holds: 629 plant communities; figures checked by the critic · src: siefertGlobalMetaanalysisRelative2015 (abstract) · trail: H2-04 §Within-unit versus between-unit, §answers, §critic · from: H2-04:A-025, H2-04:C-015, H2-04:C-045, H2-04:C-110
- **within-between-partition.7** A scale-dependent trade-off framework holds that within-species constraints often do not apply across species, and vice versa.
  conf: not stated · class: assert (marker) · holds: the review's trait-ecology section, labelled non-microbial · src: agrawalScaledependentFrameworkTradeoffs2020 (AB; asserted) · trail: H2-04 §Within-unit versus between-unit · from: H2-04:I-0037
- **within-between-partition.8** T-statistics and HMSC joint models are frameworks for partitioning trait variation within and between units.
  conf: not stated · class: not stated · holds: trait ecology · src: violleReturnVarianceIntraspecific2012 (AB), ovaskainenHowMakeMore2017 (AB) · trail: H2-04 §Within-unit versus between-unit · from: H2-04:I-0037
- **within-between-partition.9** The plant partitions are measured and partly replicated, but concern species traits, not gene content.
  conf: not stated · class: meas (note: "The plant partitions are measured") · holds: plant trait ecology · src: none (the review's assessment of the plant sources) · trail: H2-04 §answers · from: H2-04:A-029

### genome-level-axes: axes of functional variation among microbial genomes
needs: none
- **genome-level-axes.1** Growth rate, genome size and cell size are near-independent in pairwise correlations (r2 at most 0.012; the maximum, 0.0121, is genome size versus cell diameter); the paper also reports a weak nonlinearity (about 6% of variance) and habitat effects (about 11%), which qualify near-independence.
  conf: not stated · class: not stated · holds: pairwise correlations; confirmed by the critic against full text · src: westobyCellSizeGenome2021 (FT) · trail: H2-04 §Genome-level versus community-level, §answers, §critic · from: H2-04:A-060, H2-04:C-032, H2-04:C-033, H2-04:C-045, H2-04:C-062
- **genome-level-axes.2** Trait relations reverse depending on genome size, across about 18,000 genomes.
  conf: not stated · class: not stated · holds: about 18,000 genomes; the critic: read as abstract only, although a PMC full text exists · src: beierTraittraitRelationshipsTradeoffs2022 (abstract) · trail: H2-04 §Genome-level versus community-level, §answers, §Adversarial critique · from: H2-04:A-060, H2-04:C-061 · limit: access (critic: H2-04:C-061)

### community-level-axes: axes of functional variation among community profiles
needs: none
- **community-level-axes.1** Across 128 soil metagenomes, the first two co-inertia axes captured 29% and 21% of community genomic trait variation, the first running from streamlined to large, metabolically expanded genomes (average genome size R2 = 0.64).
  conf: single (marker) · class: meas (marker) · holds: 128 soil metagenomes; profiles independent of isolate genomes; read-based annotation of 5 to 15% of reads; no log-ratio treatment; the critic: these figures could not be rechecked, and the abstract confirms only the qualitative claim · src: pitonLifeHistoryStrategies2023 (FT; measured; single study; profiles independent of isolate genomes; read-based annotation of 5 to 15% of reads; no log-ratio treatment) · trail: H2-04 §Genome-level versus community-level, §answers, §Adversarial critique · from: H2-04:I-0038, H2-04:A-057, H2-04:C-030, H2-04:C-057..059 · limit: access (critic: H2-04:C-058)
- **community-level-axes.2** Community-only functional axes exist from non-negative matrix factorisation of ocean metagenome protein families, without a genome-level comparison.
  conf: not stated · class: not stated · holds: ocean metagenomes · src: jiangFunctionalBiogeographyOcean2012 (abstract) · trail: H2-04 §Genome-level versus community-level, §answers · from: H2-04:A-061
- **community-level-axes.3** Piton et al. assert that community-average rRNA copy number varies less than isolate values (a compression of variance at the community level).
  conf: not stated · class: assert (note: "asserted") · holds: community averages versus isolate values · src: pitonLifeHistoryStrategies2023 (asserted) · trail: H2-04 §Genome-level versus community-level, §answers · from: H2-04:A-066

### axis-agreement: agreement between genome-level and community-level functional axes
needs: genome-level-axes, community-level-axes
- **axis-agreement.1** No study was found that compares the main axes of functional variation among genomes with those among community profiles using a formal agreement measure (eigenvector angle, Procrustes, congruence coefficient).
  conf: not stated · class: search (note: "No study found") · holds: routes: Europe PMC queries on community-aggregated traits, metagenome trait axes and genome-level trait trade-offs; citation follow-up from Piton 2023 and Westoby 2021; three independent search angles; the critic: an absence that is the review's own search result · src: none (a search result) · trail: H2-04 §answers, §critic · from: H2-04:A-056, H2-04:A-063, H2-04:A-068, H2-04:C-028, H2-04:C-034, H2-04:C-116 · rating: "Absent as direct evidence"
- **axis-agreement.2** Piton et al. 2023 is the nearest precedent: the authors say their community axes are consistent with isolate-based trait axes without testing it (the abstract: the two community trait dimensions "support previous theoretical and isolate-based studies"), and state that community-aggregated patterns "do not directly inform on the within-organism tradeoffs"; the community profiles are metagenomic and independent of the isolate genomes.
  conf: single (marker) · class: not stated · holds: 128 soil metagenomes; a qualitative comparison, no test · src: pitonLifeHistoryStrategies2023 (FT; measured; single study; profiles independent of isolate genomes; read-based annotation of 5 to 15% of reads; no log-ratio treatment) · trail: H2-04 §Genome-level versus community-level, §answers, §critic · from: H2-04:I-0038, H2-04:A-057, H2-04:A-058, H2-04:C-029, H2-04:C-030, H2-04:C-059
- **axis-agreement.3** A genome-level sugar-versus-acid catabolic axis carried to enrichment communities gives lower GC in sugar-enriched communities (p < 1e-5): qualitative agreement, with no axis statistic.
  conf: not stated · class: not stated · holds: enrichment communities; preprint read through a tool summary, published version abstract only · src: gralkaFundamentalMetabolicStrategies2022 (SEC; critic: H2-04:C-052..054 was "preprint full text via summary"), gralkaGenomeContentPredicts2023 (published version abstract only) · trail: H2-04 §Genome-level versus community-level, §answers, §critic · from: H2-04:A-059, H2-04:C-031, H2-04:C-052..054 · limit: access (critic: H2-04:C-031)
- **axis-agreement.4** By modelling on profiles built from the same genomes, how genes are distributed across genomes (functional redundancy) governs how community functional profiles respond to taxonomic perturbation (predicted versus observed shifts r = 0.86, n = 8): a modelled, indirect link.
  conf: not stated · class: model (marker) · holds: profiles built from the same genomes; n = 8; the critic: r = 0.86 could not be rechecked · src: engTaxafunctionRobustnessMicrobial2018 (FT; modelled; indirect) · trail: H2-04 §Genome-level versus community-level, §answers, §Adversarial critique · from: H2-04:I-0039, H2-04:A-062, H2-04:C-063 · limit: access (critic: H2-04:C-063)
- **axis-agreement.5** The nearest microbial precedents are single studies with qualitative comparisons; removing Piton et al. 2023 leaves only the Gralka enrichment-community comparison.
  conf: single (note: "single studies") · class: not stated · holds: case D2(a) · src: pitonLifeHistoryStrategies2023, gralkaFundamentalMetabolicStrategies2022 · trail: H2-04 §answers · from: H2-04:A-064, H2-04:A-070
- **axis-agreement.6** No conflict was found, because no quantitative comparison exists; Piton's own caveat and the asserted compression of community-average rRNA copy number variance cut against reading the qualitative agreement as axis identity.
  conf: not stated · class: search (note: "None found") · holds: case D2(a) · src: pitonLifeHistoryStrategies2023 · trail: H2-04 §answers · from: H2-04:A-065, H2-04:A-066

### plant-axis-analogues: species-level versus community-level trait axes in plants (non-microbial)
needs: within-between-partition, axis-agreement
- **plant-axis-analogues.1** The two main community-mean trait axes across more than 1.1 million plots (stature, resource acquisitiveness) "reflect the trade-offs at the species level"; the community means are computed from the same species' database trait values, so not independent; the abstract gives no agreement statistic and itself notes the prior expectation of decoupling; the positive-agreement reading rests on this study alone.
  conf: single (marker) · class: not stated · holds: global plant plots (more than 1.1 million); community means from the same species' values · src: bruelheideGlobalTraitenvironmentRelationships2018 (AB; single study; community means from the same species' values) · trail: H2-04 §Genome-level versus community-level, §answers, §critic · from: H2-04:I-0040, H2-04:A-072, H2-04:A-076, H2-04:A-082, H2-04:C-037, H2-04:C-042, H2-04:C-069 · rating: "Weak for the positive agreement claim" · limit: access and evidence (note: "rests on one abstract")
- **plant-axis-analogues.2** Some leaf-economics correlations reverse sign within versus across species.
  conf: not stated · class: not stated · holds: leaf economics traits; within- versus across-species · src: andereggWithinspeciesPatternsChallenge2018 (abstract) · trail: H2-04 §Genome-level versus community-level, §answers · from: H2-04:A-073, H2-04:C-039
- **plant-axis-analogues.3** Area-based leaf traits scale with LMA within species but not across species, for different mechanistic reasons.
  conf: not stated · class: not stated · holds: within- versus across-species · src: osnasDivergentDriversLeaf2018 (full text) · trail: H2-04 §Genome-level versus community-level, §answers · from: H2-04:A-073, H2-04:C-039
- **plant-axis-analogues.4** Leaf traits vary almost independently among species yet shift jointly across sites along shared climate gradients; this concerns trait-environment responses, not axis reversal.
  conf: not stated · class: not stated · holds: leaf traits along climate gradients · src: dongComponentsLeaftraitVariation2020 (abstract) · trail: H2-04 §Within-unit versus between-unit, §answers, §critic · from: H2-04:A-073, H2-04:C-040, H2-04:C-105
- **plant-axis-analogues.5** The one quantitative cross-level agreement measure found is eigenvector angles and eigenvalue ratios with permutation tests, used to show that including intraspecific variation rotates leaf trait axes.
  conf: not stated · class: not stated · holds: leaf trait spaces, within- versus across-species · src: puglielliIntraspecificVariabilityLeaf2024 (abstract), puglielliQuantifyingInfluenceIntraspecific2025 (full text) · trail: H2-04 §Genome-level versus community-level, §answers · from: H2-04:A-074, H2-04:C-039
- **plant-axis-analogues.6** Three different partitions are involved and are kept apart: (i) species-level trade-offs versus community-mean axes (Bruelheide 2018); (ii) within-community versus among-community components (Kembel & Cahill, Ackerly & Cornwell); (iii) within-species versus across-species (Anderegg, Osnas, Puglielli). Evidence that cross-level structure can differ, and can reverse in sign, comes from (ii) and (iii), not from the species-versus-community-mean comparison D2 is closest to; for (i) the only evidence is a single abstract, and it reports agreement.
  conf: not stated · class: not stated · holds: plant trait ecology; the review rates the disagreement side as replicated across independent plant datasets, and the critic says that mixes partition types · src: bruelheideGlobalTraitenvironmentRelationships2018, kembelIndependentEvolutionLeaf2011, ackerlyTraitbasedApproachCommunity2007, andereggWithinspeciesPatternsChallenge2018, osnasDivergentDriversLeaf2018, puglielliIntraspecificVariabilityLeaf2024, puglielliQuantifyingInfluenceIntraspecific2025 · trail: H2-04 §critic, §Adversarial critique, §answers · from: H2-04:C-036, H2-04:C-037, H2-04:C-038, H2-04:C-039, H2-04:C-041, H2-04:C-042, H2-04:C-069, H2-04:A-075 · rating: "Moderate"
- **plant-axis-analogues.7** Correlation strength only bounds how dissimilar cross-scale structures can be.
  conf: not stated · class: not stated · holds: cross-scale structures · src: messierTraitVariationIntegration2016 (abstract) · trail: H2-04 §answers · from: H2-04:A-078
- **plant-axis-analogues.8** On the reviewer's reading, the bound on cross-scale dissimilarity may reconcile Bruelheide 2018 (agreement at global scale) with Kembel & Cahill 2011, Anderegg 2018 and Osnas 2018 (disagreement or sign reversal at local or within-species scale).
  conf: not stated · class: reading (note: "that is the reviewer's reading") · holds: case D2(b); the critic: labelled as the reviewer's reading, which is acceptable · src: messierTraitVariationIntegration2016 · trail: H2-04 §answers, §Adversarial critique · from: H2-04:A-078, H2-04:A-077, H2-04:C-113

### complementarity-overlap: complementarity versus functional overlap among co-occurring organisms
needs: association-networks, shared-ancestry, genome-linkage
- **complementarity-overlap.1** Co-occurring 16S lineages mapped to complete genomes had more similar pathway content and genome size than random pairs, beyond phylogeny; the authors read this as competition or habitat sharing rather than cooperation. "Beyond phylogeny" is not stated in the abstract and could not be verified in full text by the critic.
  conf: not stated · class: deriv (marker) · holds: profiles independent of genomes · src: chaffronGlobalNetworkCoexisting2010 (FT; derived; profiles independent of genomes) · trail: H2-04 §Complementarity versus overlap, §answers, §Adversarial critique · from: H2-04:I-0016, H2-04:A-040, H2-04:C-051, H2-04:C-056 · limit: access (critic: H2-04:C-056)
- **complementarity-overlap.2** In HMP data, positive associations were enriched for phylogenetic and functional similarity, and negative ones for the inverse.
  conf: not stated · class: deriv (marker) · holds: HMP data · src: faustMicrobialCooccurrenceRelationships2012 (FT; derived) · trail: H2-04 §Complementarity versus overlap, §answers · from: H2-04:I-0017, H2-04:A-040
- **complementarity-overlap.3** Across 154 gut species, co-occurrence correlated with modelled metabolic competition (rho = 0.211) and negatively with modelled complementarity (rho = -0.193); the effects are weak.
  conf: not stated · class: model (marker) · holds: 154 gut species; profiles mapped to the same reference genomes; the critic: the rho values rest on a tool summary and could not be rechecked · src: levyMetabolicModelingSpecies2013 (SEC; modelled; critic: H2-04:C-052..054 was "FT-s; modelled") · trail: H2-04 §Complementarity versus overlap, §answers, §Adversarial critique · from: H2-04:I-0018, H2-04:A-040, H2-04:C-063, H2-04:C-052..054 · limit: access (critic: H2-04:C-063)
- **complementarity-overlap.4** A reanalysis of the same gut data makes both metabolic competition (coefficient -0.013, p = 0.71) and metabolic complementarity (p = 0.14) non-significant once phylogeny and genome content similarity are included, so it undercuts Levy & Borenstein's modelled competition signal as well as its complementarity signal; the reanalysis is not independent of the data it reanalyses.
  conf: not stated · class: deriv (marker) · holds: the gut data of Levy & Borenstein 2013 · src: kamnevaGenomeCompositionPhylogeny2017 (FT; derived; not independent of 17) · trail: H2-04 §Complementarity versus overlap, §critic, §Adversarial critique · from: H2-04:I-0019, H2-04:A-048, H2-04:C-019, H2-04:C-020, H2-04:C-046, H2-04:C-096, H2-04:C-097
- **complementarity-overlap.5** At whole-community scale, co-occurrence is associated with genome similarity (Chaffron, from the abstract; Faust; Kamneva's genome-content similarity index).
  conf: not stated · class: not stated · holds: whole-community scale · src: chaffronGlobalNetworkCoexisting2010 (abstract, as the critic read it), faustMicrobialCooccurrenceRelationships2012, kamnevaGenomeCompositionPhylogeny2017 · trail: H2-04 §critic · from: H2-04:C-018, H2-04:C-025 · rating: "weak to moderate for overlap"
- **complementarity-overlap.6** Human microbiome samples had higher functional redundancy than random draws from the body-site species pool; this measures within-sample redundancy against a species-pool null, not pairwise co-occurrence, and is a separate case.
  conf: not stated · class: deriv (marker) · holds: human microbiome; profiles computed from the same reference genomes, with a reference-free replication · src: tianDecipheringFunctionalRedundancy2020 (FT; derived; profiles computed from the same reference genomes, with a reference-free replication) · trail: H2-04 §Complementarity versus overlap, §answers, §critic · from: H2-04:I-0020, H2-04:A-040, H2-04:C-022, H2-04:C-045
- **complementarity-overlap.7** In small co-occurring groups (pairs to quadruplets, more than 800 communities), modelled resource overlap was barely distinguishable from random while modelled metabolic interaction potential was elevated.
  conf: not stated · class: model (marker) · holds: more than 800 communities; groups of two to four; the critic: figures read only through a tool summary · src: zelezniakMetabolicDependenciesDrive2015 (SEC; modelled; critic: H2-04:C-052..054 was "FT-s; modelled") · trail: H2-04 §Complementarity versus overlap, §answers, §critic · from: H2-04:I-0021, H2-04:A-041, H2-04:C-023, H2-04:C-055, H2-04:C-052..054 · limit: access (critic: H2-04:C-023)
- **complementarity-overlap.8** Co-occurring groups of up to 40 species polarise into cooperative groups (small genomes, auxotrophies) and competitive groups (large genomes, overlapping requirements, mainly soils); the authors attribute the difference from Levy & Borenstein to scale.
  conf: not stated · class: model (marker) · holds: groups of up to 40 species · src: machadoPolarizationMicrobialCommunities2021 (FT; modelled) · trail: H2-04 §Complementarity versus overlap, §answers · from: H2-04:I-0022, H2-04:A-041
- **complementarity-overlap.9** Complementarity among co-occurring organisms at the small-group scale comes from one method family (Zelezniak 2015 and Machado 2021 share authors and SMETANA); removing these papers would remove nearly all support for complementarity among co-occurring organisms in natural surveys.
  conf: single (critic: H2-04:C-023) · class: not stated · holds: natural surveys, small co-occurring groups · src: zelezniakMetabolicDependenciesDrive2015, machadoPolarizationMicrobialCommunities2021 · trail: H2-04 §answers, §critic · from: H2-04:A-047, H2-04:A-055, H2-04:C-023 · rating: "Weak for complementarity at the small-group scale"
- **complementarity-overlap.10** Whether co-occurrence tracks complementarity is in conflict between Levy & Borenstein 2013 and Zelezniak 2015 with Machado 2021; Machado attributes the difference to scale.
  conf: cont (note: "Conflicts") · class: not stated · holds: whole-community versus small-group scale · src: levyMetabolicModelingSpecies2013, zelezniakMetabolicDependenciesDrive2015, machadoPolarizationMicrobialCommunities2021 · trail: H2-04 §answers · from: H2-04:A-049
- **complementarity-overlap.11** Pairwise metabolic models predict that cooperative potential peaks at moderate overlap.
  conf: not stated · class: model (marker) · holds: pairwise models · src: freilichCompetitiveCooperativeMetabolic2011 (AB; modelled) · trail: H2-04 §Complementarity versus overlap · from: H2-04:I-0023
- **complementarity-overlap.12** Costless metabolic secretions create broad cross-feeding opportunities.
  conf: not stated · class: model (marker) · holds: models · src: pachecoCostlessMetabolicSecretions2019 (AB; modelled) · trail: H2-04 §Complementarity versus overlap · from: H2-04:I-0023
- **complementarity-overlap.13** The Black Queen hypothesis predicts complementary gene content for leaky functions.
  conf: not stated · class: assert (marker) · holds: a hypothesis · src: morrisBlackQueenHypothesis2012 (AB; asserted) · trail: H2-04 §Complementarity versus overlap · from: H2-04:I-0024
- **complementarity-overlap.14** Among 20 soil isolates in 40 carbon environments, overlap in carbon use predicted competition (68% for the most similar non-identical pairs) and difference predicted facilitation (Spearman 0.75); this bears on mechanism, not on covariation across samples.
  conf: not stated · class: meas (marker) · holds: in vitro, no community profiles; figures checked by the critic against full text · src: kehePositiveInteractionsCommon2021 (FT; measured; in vitro, no community profiles) · trail: H2-04 §Complementarity versus overlap, §answers, §critic · from: H2-04:I-0025, H2-04:A-043, H2-04:C-024, H2-04:C-045
- **complementarity-overlap.15** Antagonism rose with metabolic similarity, with small effect (pseudo-R2 0.015 to 0.032).
  conf: not stated · class: meas (marker) · holds: in vitro; read through a tool summary · src: russelAntagonismCorrelatesMetabolic2017 (SEC; measured; critic: H2-04:C-052..054 was "FT-s; measured") · trail: H2-04 §Complementarity versus overlap, §answers, §critic · from: H2-04:I-0026, H2-04:A-043, H2-04:C-050, H2-04:C-052..054 · limit: access (critic: H2-04:C-050)
- **complementarity-overlap.16** Among tree-hole isolates, most pairwise interactions were net negative: competition dominates.
  conf: not stated · class: meas (marker) · holds: culturable tree-hole isolates, a single environment · src: fosterCompetitionNotCooperation2012 (AB; measured; single environment) · trail: H2-04 §Complementarity versus overlap, §answers · from: H2-04:I-0027, H2-04:A-043
- **complementarity-overlap.17** In vitro results conflict: Kehe 2021 finds positive interactions common, while Foster & Bell 2012 find competition dominant (in a single environment).
  conf: cont (note: "Conflicts") · class: not stated · holds: in vitro · src: kehePositiveInteractionsCommon2021, fosterCompetitionNotCooperation2012 · trail: H2-04 §answers · from: H2-04:A-049, H2-04:A-050
- **complementarity-overlap.18** The complementarity readings rest on genome-derived auxotrophies, whose sensitivity against 36 strains with known auxotrophies was 75.5% (gapseq) and 43.4% (AGORA2), and on annotation gaps.
  conf: not stated · class: model (marker) · holds: modelled with measured validation, 36 strains · src: starkeAminoAcidAuxotrophies2023 (FT; modelled with measured validation), priceFillingGapsBacterial2018 · trail: H2-04 §Complementarity versus overlap, §answers, §Adversarial critique · from: H2-04:I-0028, H2-04:A-044, H2-04:C-101
- **complementarity-overlap.19** Both the overlap and the complementarity readings depend on co-occurrence inference, which the review's section 3 shows to be method-dependent (31.5% shared edges) and poorly validated; no error rate equivalent to the auxotrophy sensitivity is applied to the co-occurrence side.
  conf: not stated · class: not stated · holds: case D1(c) · src: none (the critic's reading of the review's own evidence) · trail: H2-04 §critic, §Adversarial critique · from: H2-04:C-026, H2-04:C-100, H2-04:C-101
- **complementarity-overlap.20** The evidence on complementarity versus overlap splits by scale and by evidence class.
  conf: not stated · class: not stated · holds: case D1(c) · src: none (the reviewer's synthesis) · trail: H2-04 §answers · from: H2-04:A-039
- **complementarity-overlap.21** Removing Chaffron et al. 2010 would leave the overlap pattern supported by Faust 2012, Levy & Borenstein 2013 and Tian 2020; the critic keeps Tian 2020 as a separate case.
  conf: not stated · class: not stated · holds: the review's single-source sensitivity check for case D1(c) · src: faustMicrobialCooccurrenceRelationships2012, levyMetabolicModelingSpecies2013, tianDecipheringFunctionalRedundancy2020 · trail: H2-04 §answers, §critic · from: H2-04:A-054, H2-04:C-022

## Do not say
- **dns.1** "Taxon co-occurrence networks exist in quantity [6, 9, 10, 17]", with Fierer, Barberán & Laughlin 2014 among the network studies.
  why: its abstract is a community-aggregated-traits perspective, not a network study; the metadata are correct but the citation is misattributed · instead: association-networks.1 · trail: H2-04 §critic, §Adversarial critique · from: H2-04:A-003, H2-04:C-004, H2-04:C-047, H2-04:C-073..075
- **dns.2** "Annotation dominates pipelines", or "annotation reference choice (65.4% of network variance)" as the size of the annotation artefact for function profiles.
  why: the figure is the 16S taxonomy database's share of variance among taxon networks, from one study; it says nothing directly about functional annotation schemes · instead: association-networks.13 · trail: H2-04 §critic, §Adversarial critique · from: H2-04:I-0013, H2-04:I-0002, H2-04:C-005, H2-04:C-006, H2-04:C-048, H2-04:C-064, H2-04:C-107
- **dns.3** "Moderate for the existence of each source, which is replicated across independent groups for closure, method dependence, shared ancestry and environment."
  why: the critic grades existence moderate at the taxon level only, weak or indirect at the function level; the shared-environment source is an assertion read through a tool summary plus one measured partition; phylogeny as largest predictor rests on one study · instead: covariation-sources.1, shared-environment.8, shared-ancestry.1 · trail: H2-04 §critic · from: H2-04:A-005, H2-04:C-007, H2-04:C-008, H2-04:C-065
- **dns.4** "The reanalysis found complementarity non-significant in the combined model", reported without the competition result.
  why: the same model makes metabolic competition non-significant too (coefficient -0.013, p = 0.71); only the result against complementarity was carried into the review, so the overlap side escaped the same reanalysis · instead: complementarity-overlap.4 · trail: H2-04 §critic, §Adversarial critique · from: H2-04:I-0019, H2-04:C-021, H2-04:C-046, H2-04:C-096..098
- **dns.5** Tian 2020 as a replication of the co-occurrence overlap pattern.
  why: it measures within-sample redundancy against a species-pool null, not pairwise co-occurrence; counting it lowers the bar for replication on the overlap side · instead: complementarity-overlap.6 · trail: H2-04 §critic, §Adversarial critique · from: H2-04:C-022, H2-04:C-102, H2-04:C-108
- **dns.6** "Moderate for the pattern that whole-community co-occurrence associates with overlap, replicated across independent groups but with weak effects."
  why: the overlap side rests on co-occurrence inference, which is method-dependent and poorly validated, with no error rate applied to it; the critic grades it weak to moderate · instead: complementarity-overlap.5, complementarity-overlap.19 · trail: H2-04 §critic, §Adversarial critique · from: H2-04:A-046, H2-04:C-025, H2-04:C-099..101
- **dns.7** "Growth rate, genome size and cell size are near-independent (r2 at most 0.012)", without the paper's qualifications.
  why: the review omits the weak nonlinearity (about 6% of variance) and the habitat contribution (about 11%) that the paper reports, which qualify near-independence · instead: genome-level-axes.1 · trail: H2-04 §critic, §Adversarial critique · from: H2-04:A-060, H2-04:C-033, H2-04:C-062
- **dns.8** "Plant ecology has made the comparison, with mixed results", and "cross-level axis agreement is not guaranteed and can reverse in sign, replicated across independent plant datasets", as answers to the species-versus-community-mean comparison.
  why: three different partitions are merged; sign reversal comes from within-community and within-species partitions, which do not answer the species-versus-community-mean comparison closest to D2; for that comparison the only evidence is one abstract, and it reports agreement · instead: plant-axis-analogues.6, plant-axis-analogues.1 · trail: H2-04 §critic, §Adversarial critique · from: H2-04:A-071, H2-04:A-075, H2-04:C-036, H2-04:C-041, H2-04:C-049, H2-04:C-069, H2-04:C-104, H2-04:C-106
- **dns.9** "Bruelheide 2018 (agreement at global scale) versus Kembel & Cahill 2011, Anderegg 2018 and Osnas 2018 (disagreement or sign reversal)" as a conflict over the same comparison.
  why: the cases are different partitions; sign reversal within species does not answer the species-versus-community-mean comparison · instead: plant-axis-analogues.6 · trail: H2-04 §answers, §Adversarial critique · from: H2-04:A-077, H2-04:C-106
- **dns.10** Dong 2020 as evidence of axis reversal across levels.
  why: it is about trait-environment responses, not axis reversal · instead: plant-axis-analogues.4 · trail: H2-04 §critic, §Adversarial critique · from: H2-04:C-040, H2-04:C-105
- **dns.11** "For such functions, within-genome linkage is weak and pathway completion is distributed across organisms."
  why: it generalises from one aquifer study to a class of functions · instead: genome-linkage.2 · trail: H2-04 §Adversarial critique · from: H2-04:C-066
- **dns.12** Horizontal transfer "25-fold more frequent" and structured by habitat as a general caution on the overlap side.
  why: it rests on one abstract (Smillie 2011) · instead: genome-linkage.5 · trail: H2-04 §Adversarial critique · from: H2-04:C-067
- **dns.13** Environmental heterogeneity as "usually the strongest driver of correlation structure", stated as a finding.
  why: it rests on one perspective, asserted and read only via a tool summary · instead: shared-environment.1 · trail: H2-04 §Adversarial critique · from: H2-04:C-068
- **dns.14** "Phylogeny is the largest single predictor of pairwise co-occurrence", stated generally.
  why: it rests on Kamneva 2017 alone, which reuses Levy & Borenstein's gut data and tested only four genomic indices · instead: shared-ancestry.1 · trail: H2-04 §Adversarial critique · from: H2-04:C-065
- **dns.15** The literature "rarely names more than two [sources] in the same study", as a property of the field.
  why: the reviewer's generalisation, without a source · instead: covariation-sources.3 · trail: H2-04 §Adversarial critique · from: H2-04:C-111
- **dns.16** The functional-profile question "approached from two sides that do not meet", as a finding.
  why: the reviewer's synthesis argument, unlabelled as the reviewer's reading · instead: covariance-partition.7 · trail: H2-04 §Adversarial critique · from: H2-04:C-112
- **dns.17** Co-occurring lineages share pathway content "beyond phylogeny", as a verified result.
  why: the abstract does not state phylogenetic control and the critic could not reach the full text (access); the review took it at face value while discounting the complementarity side for shared authorship · instead: complementarity-overlap.1 · trail: H2-04 §critic, §Adversarial critique · from: H2-04:C-051, H2-04:C-056, H2-04:C-103
- **dns.18** Zelezniak 2015, Levy & Borenstein 2013, Russel 2017, Carr 2019, Arandia-Gorostidi 2025 and the Gralka preprint as read in full text.
  why: they were read through web-fetch tool summaries ('FT-s'), closer to secondary, with quotes still to be rechecked (access) · instead: none · trail: H2-04 §critic, §Adversarial critique · from: H2-04:C-050, H2-04:C-052..054
- **dns.19** The intraspecific share of trait variance (25%, 32%) as a covariance partition, or as the same partition as within- versus among-community components.
  why: it is a variance partition, not a covariance partition, and a within-species versus between-species partition · instead: within-between-partition.6 · trail: H2-04 §answers, §critic, §Adversarial critique · from: H2-04:A-025, H2-04:C-015, H2-04:C-110
- **dns.20** Taxon co-occurrence networks as evidence for co-occurrence of organisms as a source of covariation among functions.
  why: a different measurement type (taxa, 16S) stands in for function-level covariation · instead: association-networks.1 · trail: H2-04 §Adversarial critique · from: H2-04:C-109
- **dns.21** Gene-level network edges as interactions among the populations carrying the genes.
  why: on the reviewer's reading the studies do not remove within-genome linkage, closure or environment · instead: gene-level-networks.3 · trail: H2-04 §answers · from: H2-04:A-003
- **dns.22** The community axes of Piton 2023 as identical to isolate-based trait axes.
  why: Piton's own caveat and the asserted compression of community-average rRNA copy number variance cut against reading the qualitative agreement as axis identity · instead: axis-agreement.2, axis-agreement.6 · trail: H2-04 §answers · from: H2-04:A-066
- **dns.23** Messier 2017 as reconciling global agreement with local disagreement, stated as a finding.
  why: that is the reviewer's reading · instead: plant-axis-analogues.7, plant-axis-analogues.8 · trail: H2-04 §answers · from: H2-04:A-078
- **dns.24** Ackerly & Cornwell and Kembel & Cahill as contradicting each other.
  why: these are different systems and are not contradictory in the strict sense · instead: within-between-partition.5 · trail: H2-04 §answers · from: H2-04:A-031
- **dns.25** A pooled microbial share of covariation across the partitions found.
  why: every microbial partition is a single study with a different denominator, so the shares cannot be pooled · instead: covariance-partition.4 · trail: H2-04 §answers · from: H2-04:A-028
- **dns.26** Zelezniak 2015 and Machado 2021 as independent lines of evidence for complementarity.
  why: they share authors and SMETANA, one method family · instead: complementarity-overlap.9 · trail: H2-04 §answers, §critic · from: H2-04:A-047, H2-04:C-023
- **dns.27** Kamneva 2017 as an independent test of Levy & Borenstein 2013.
  why: it reuses Levy & Borenstein data and is not independent · instead: complementarity-overlap.4 · trail: H2-04 §answers · from: H2-04:A-048
- **dns.28** In vitro interaction results as evidence of covariation across samples.
  why: they bear on mechanism, not on covariation across samples · instead: complementarity-overlap.14 · trail: H2-04 §critic · from: H2-04:C-024

## Gaps
- **gap.1** Phylogenetic profiling of gene co-occurrence across genomes, and pangenome gene co-occurrence or avoidance.
  blocks: genome-linkage, genome-level-axes · origin: critic coverage gap: an explicit related-work bullet in the brief, with nothing in the review, not even a "not found" with routes; also named by the stage 2 check · from: H2-04:C-084 · trail: H2-04 §Adversarial critique, §Stage 2 check
- **gap.2** Partition of community functional variation into taxonomic turnover versus within-taxon change for metagenomic or metatranscriptomic function profiles; the Lepš-type decomposition itself was not obtained.
  blocks: covariance-partition · origin: critic coverage gap (Salazar et al. 2019 named as the candidate); not found by the review; Lepš et al. 2011 not obtained; named by the stage 2 check · from: H2-04:C-085, H2-04:A-032 · src: lepsCommunityTraitResponse2011 · trail: H2-04 §Adversarial critique, §Stage 2 check
- **gap.3** Covariation of functions or pathways with environment across metagenomes, using function-level data rather than taxa.
  blocks: shared-environment · origin: critic coverage gap (Gianoulis et al. 2009; Raes et al. 2011; Fierer et al. 2012 named) · from: H2-04:C-086 · trail: H2-04 §Adversarial critique
- **gap.4** Normalisation and sequencing-depth handling for gene-abundance profiles (average genome size correction, single-copy-gene normalisation, comparisons of normalisation methods).
  blocks: aggregation-artefacts · origin: critic coverage gap: the artefact section covers only closure in taxon data · from: H2-04:C-087 · trail: H2-04 §Adversarial critique
- **gap.5** Functional annotation-scheme artefacts (KEGG versus COG versus eggNOG or Pfam; annotation rate differences between samples).
  blocks: aggregation-artefacts, association-networks.13 · origin: critic coverage gap: the only magnitude given is for a 16S taxonomy database · from: H2-04:C-088 · trail: H2-04 §Adversarial critique
- **gap.6** Contamination and chimerism in MAGs as they bear on measured within-genome linkage.
  blocks: genome-linkage · origin: critic coverage gap; the review's search found no source (search record, not found item 6) · from: H2-04:C-089 · trail: H2-04 §Adversarial critique, §Provenance
- **gap.7** Gene co-abundance binning beyond one abstract, checked for reported shares of gene covariance explained by bin membership.
  blocks: genome-linkage.1 · origin: critic coverage gap; named by the stage 2 check · from: H2-04:C-090 · trail: H2-04 §Adversarial critique, §Stage 2 check
- **gap.8** Community function profiles predicted from reference genomes versus measured metagenomes (PICRUSt, PICRUSt2, Tax4Fun), which report agreement statistics between genome-built and independently measured profiles.
  blocks: axis-agreement, covariance-partition · origin: critic coverage gap: bears on the brief's "built from the same genomes or measured independently" requirement · from: H2-04:C-091 · trail: H2-04 §Adversarial critique
- **gap.9** Within-unit versus between-unit covariance comparisons in quantitative genetics and morphometrics (G-matrix versus among-population divergence, static versus evolutionary allometry), where formal agreement measures were developed.
  blocks: axis-agreement, plant-axis-analogues · origin: critic coverage gap; the critic: these analogues were not searched; named by the stage 2 check · from: H2-04:C-092, H2-04:C-043 · trail: H2-04 §Adversarial critique, §critic, §Stage 2 check
- **gap.10** Animal trait ecology analogues of species-level versus community-level trait axes.
  blocks: plant-axis-analogues · origin: reported as not found in the routes used, with no routes named beyond the general list (critic coverage gap); search record: not specifically searched · from: H2-04:C-093, H2-04:A-080 · trail: H2-04 §answers, §Adversarial critique, §Provenance
- **gap.11** Taxonomy-function coupling across samples measured with Procrustes or Mantel tests between taxonomic and functional ordinations.
  blocks: axis-agreement · origin: critic coverage gap: nearest precedents for an ordination agreement measure · from: H2-04:C-094 · trail: H2-04 §Adversarial critique
- **gap.12** Genome-level structure of gene content (such as the nestedness of the genome-content network) related to community-level axes.
  blocks: genome-level-axes, axis-agreement · origin: critic coverage gap · from: H2-04:C-095 · trail: H2-04 §Adversarial critique
- **gap.13** A partition of function-by-function covariance in metagenomic or genome-derived community profiles into its sources.
  blocks: covariance-partition · origin: not found through any route (the review's search record and answers) · from: H2-04:A-032, H2-04:C-010 · trail: H2-04 §answers, §Provenance
- **gap.14** Gene-level (gene or KO) co-occurrence networks that remove within-genome linkage.
  blocks: gene-level-networks · origin: not found through any route · from: H2-04:A-010 · trail: H2-04 §answers, §Provenance
- **gap.15** Complementarity or overlap measured with community profiles built independently of the genomes analysed, and at the gene level; validation of any network edge against measured interactions beyond two species pairs.
  blocks: complementarity-overlap, association-networks · origin: not measured in any study found · from: H2-04:A-051 · trail: H2-04 §answers
- **gap.16** A formal genome-level versus community-level axis comparison in any microbial habitat, and comparisons where community profiles are built from the same genomes versus measured independently.
  blocks: axis-agreement · origin: not measured in any study found; not found through any route · from: H2-04:A-067 · trail: H2-04 §answers, §Provenance
- **gap.17** Quantitative agreement statistics for species-level versus community-mean trait axes at global scale.
  blocks: plant-axis-analogues · origin: not measured in any study found · from: H2-04:A-079 · trail: H2-04 §answers
- **gap.18** Recheck of the quotes and figures read only through web-fetch tool summaries: Levy & Borenstein 2013, Zelezniak 2015, Russel 2017, Carr 2019, Arandia-Gorostidi 2025 and the Gralka preprint.
  blocks: complementarity-overlap.3, complementarity-overlap.7, complementarity-overlap.15, shared-environment.1, association-networks.9, gene-level-networks.2, axis-agreement.3 · origin: the review's search record (not re-opened by the synthesis agent; should be rechecked) and the critic · from: H2-04:A-015, H2-04:C-054 · trail: H2-04 §Provenance, §Adversarial critique
- **gap.19** Figures and statements the critic could not recheck: Chaffron's "beyond phylogeny", Piton's 29%, 21%, R2 0.64, R2 0.32 and 5 to 15% of reads annotated, Weiss's 31.5% shared edges, precision 0.2 and effective species number, Eng & Borenstein's r = 0.86 and Levy & Borenstein's rho values.
  blocks: complementarity-overlap.1, community-level-axes.1, shared-ancestry.3, association-networks.2, axis-agreement.4, complementarity-overlap.3 · origin: critic access errors (full texts not reachable in the critique) · from: H2-04:C-051, H2-04:C-056, H2-04:C-058, H2-04:C-060, H2-04:C-063 · trail: H2-04 §critic, §Adversarial critique
- **gap.20** Beier 2022, load-bearing as a genome-level reference axis, was read as abstract only although a PMC full text exists.
  blocks: genome-level-axes.2 · origin: critic access error: could have been upgraded · from: H2-04:C-061 · src: beierTraittraitRelationshipsTradeoffs2022 · trail: H2-04 §Adversarial critique
- **gap.21** The follow-up the stage 2 check called for: a targeted brief on phylogenetic profiling, subspace comparison methods and turnover decompositions, sized separately.
  blocks: genome-linkage, covariance-partition, axis-agreement · origin: the note's stage 2 check, triggered by the critic's coverage gaps · trail: H2-04 §Stage 2 check
- **gap.22** The note contradicts itself on five sources: its Sources not obtained list says "Nothing beyond a citation was reachable for these; none supports any claim in the review", while the reference list labels Lima-Mendez 2015 [17a], Freilich S 2011 [10c], Goldford 2018 [11b], Blanchet 2020 [3b] and Freilich MA 2018 [10b] as abstract only and the body cites them (the critic checked the Freilich 2018 figures).
  blocks: association-networks.6, association-networks.7, complementarity-overlap.11, shared-environment.6 · origin: a note that contradicts itself · from: H2-04:I-0010, H2-04:I-0011, H2-04:I-0023, H2-04:I-0032, H2-04:C-045 · src: limamendezDeterminantsCommunityStructure2015, freilichCompetitiveCooperativeMetabolic2011, goldfordEmergentSimplicityMicrobial2018, blanchetCooccurrenceNotEvidence2020, freilichSpeciesCooccurrenceNetworks2018 · trail: H2-04 §Sources not obtained, §Reference list
- **gap.23** A test of the aggregation artefact of repeated co-occurrence (Hawkins type) on microbial functional profiles.
  blocks: aggregation-artefacts · origin: not found in any microbial study (the review's artefacts section) · trail: H2-04 §Artefacts of aggregation

## Out of scope
- H2-04:C-001, H2-04:C-009, H2-04:C-017, H2-04:C-027, H2-04:C-035, H2-04:C-044: the critic's verdict on each answer as a whole (a grade of the answers, not a finding)
- H2-04:C-071, H2-04:C-072, H2-04:C-076..083: reference corrections and citation-form errors, applied in Sources
- H2-04:C-114, H2-04:C-115: expectation echo, the brief's wording (provenance)
- H2-04:A-012..014, H2-04:A-034, H2-04:A-035, H2-04:A-052, H2-04:A-053, H2-04:A-069, H2-04:A-081: access basis and routes of the answers (provenance, recorded in Sources)

## Sources

```bibtex
@article{ackerlyTraitbasedApproachCommunity2007,
  author = {Ackerly, DD and Cornwell, WK},
  title = {A trait-based approach to community assembly: partitioning of species trait values into within- and among-community components},
  journal = {Ecology Letters},
  year = {2007},
  volume = {10},
  number = {2},
  pages = {135-145},
  doi = {10.1111/j.1461-0248.2006.01006.x},
  note = {access: abstract_only; cited as: H2-04 [1]}
}

@article{andereggWithinspeciesPatternsChallenge2018,
  author = {Anderegg, LDL and Berner, LT and Badgley, G and Sethi, ML and Law, BE and HilleRisLambers, J},
  title = {Within-species patterns challenge our understanding of the leaf economics spectrum},
  journal = {Ecology Letters},
  year = {2018},
  volume = {21},
  number = {5},
  pages = {734-744},
  doi = {10.1111/ele.12945},
  note = {access: abstract_only; cited as: H2-04 [1a]}
}

@article{agrawalScaledependentFrameworkTradeoffs2020,
  author = {Agrawal, AA},
  title = {A scale-dependent framework for trade-offs, syndromes, and specialization in organismal biology},
  journal = {Ecology},
  year = {2020},
  volume = {101},
  number = {2},
  pages = {e02924},
  doi = {10.1002/ecy.2924},
  note = {access: abstract_only; cited as: H2-04 [1b]}
}

@misc{arandiagorostidiMetagenomicbasedNetworkAnalysis2025,
  author = {Arandia-Gorostidi, N and Montiel, L and Latorre, F and Balagué, V and Gasol, JM and Simó, R and Giner, CR and Logares, R},
  title = {Metagenomic-based network analysis reveals the importance of vitamin cross-feeding in marine microbial assemblages},
  howpublished = {bioRxiv},
  year = {2025},
  doi = {10.1101/2025.08.08.668683},
  note = {access: secondary (critic: H2-04:C-052..054; the note said FT-s, full text read through a web-fetch tool summary, quotes to be rechecked); type: preprint; cited as: H2-04 [2]}
}

@article{beierTraittraitRelationshipsTradeoffs2022,
  author = {Beier, S and Werner, J and Bouvier, T and Mouquet, N and Violle, C},
  title = {Trait-trait relationships and tradeoffs vary with genome size in prokaryotes},
  journal = {Frontiers in Microbiology},
  year = {2022},
  volume = {13},
  pages = {985216},
  doi = {10.3389/fmicb.2022.985216},
  note = {access: abstract_only; cited as: H2-04 [2a]; a PMC full text exists, PMC9634001 (critic: H2-04:C-061)}
}

@article{barberanExplorationCommunityTraits2011,
  author = {Barberán, A and Fernández-Guerra, A and Bohannan, BJM and Casamayor, EO},
  title = {Exploration of community traits as ecological markers in microbial metagenomes},
  journal = {Molecular Ecology},
  year = {2012},
  volume = {21},
  number = {8},
  pages = {1909-1917},
  doi = {10.1111/j.1365-294X.2011.05383.x},
  note = {access: abstract_only; cited as: H2-04 [2b]}
}

@article{berryDecipheringMicrobialInteractions2014,
  author = {Berry, D and Widder, S},
  title = {Deciphering microbial interactions and detecting keystone species with co-occurrence networks},
  journal = {Frontiers in Microbiology},
  year = {2014},
  volume = {5},
  pages = {219},
  doi = {10.3389/fmicb.2014.00219},
  note = {access: abstract_only; cited as: H2-04 [3]}
}

@article{anantharamanThousandsMicrobialGenomes2016,
  author = {Anantharaman, K and Brown, CT and Hug, LA and Sharon, I and Castelle, CJ and Probst, AJ and Thomas, BC and Singh, A and Wilkins, MJ and Karaoz, U and Brodie, EL and Williams, KH and Hubbard, SS and Banfield, JF},
  title = {Thousands of microbial genomes shed light on interconnected biogeochemical processes in an aquifer system},
  journal = {Nature Communications},
  year = {2016},
  volume = {7},
  pages = {13219},
  doi = {10.1038/ncomms13219},
  note = {access: full_text; cited as: H2-04 [3a]}
}

@article{blanchetCooccurrenceNotEvidence2020,
  author = {Blanchet, FG and Cazelles, K and Gravel, D},
  title = {Co-occurrence is not evidence of ecological interactions},
  journal = {Ecology Letters},
  year = {2020},
  volume = {23},
  number = {7},
  pages = {1050-1063},
  doi = {10.1111/ele.13525},
  note = {access: abstract_only; cited as: H2-04 [3b]; also listed in Sources not obtained, which says nothing beyond a citation was reachable and that it supports no claim, while the reference list labels [3b] AB and the body cites it (conflict between the note's lists)}
}

@article{bruelheideGlobalTraitenvironmentRelationships2018,
  author = {Bruelheide, H and Dengler, J and Purschke, O and Lenoir, J and Jiménez-Alfaro, B and Hennekens, SM and Botta-Dukát, Z and Chytrý, M and Field, R and Jansen, F and Kattge, J and Pillar, VD and Schrodt, F and Mahecha, MD and Peet, RK and Sandel, B and van Bodegom, P and Altman, J and Alvarez-Dávila, E and Arfin Khan, MAS and Attorre, F and Aubin, I and Baraloto, C and Barroso, JG and Bauters, M and Bergmeier, E and Biurrun, I and Bjorkman, AD and Blonder, B and Čarni, A and Cayuela, L and Černý, T and Cornelissen, JHC and Craven, D and Dainese, M and Derroire, G and De Sanctis, M and Díaz, S and Doležal, J and Farfan-Rios, W and Feldpausch, TR and Fenton, NJ and Garnier, E and Guerin, GR and Gutiérrez, AG and Haider, S and Hattab, T and Henry, G and Hérault, B and Higuchi, P and Hölzel, N and Homeier, J and Jentsch, A and Jürgens, N and Kącki, Z and Karger, DN and Kessler, M and Kleyer, M and Knollová, I and Korolyuk, AY and Kühn, I and Laughlin, DC and Lens, F and Loos, J and Louault, F and Lyubenova, MI and Malhi, Y and Marcenò, C and Mencuccini, M and Müller, JV and Munzinger, J and Myers-Smith, IH and Neill, DA and Niinemets, Ü and Orwin, KH and Ozinga, WA and Penuelas, J and Pérez-Haase, A and Petřík, P and Phillips, OL and Pärtel, M and Reich, PB and Römermann, C and Rodrigues, AV and Sabatini, FM and Sardans, J and Schmidt, M and Seidler, G and Silva Espejo, JE and Silveira, M and Smyth, A and Sporbert, M and Svenning, JC and Tang, Z and Thomas, R and Tsiripidis, I and Vassilev, K and Violle, C and Virtanen, R and Weiher, E and Welk, E and Wesche, K and Winter, M and Wirth, C and Jandt, U},
  title = {Global trait-environment relationships of plant communities},
  journal = {Nature Ecology & Evolution},
  year = {2018},
  volume = {2},
  number = {12},
  pages = {1906-1917},
  doi = {10.1038/s41559-018-0699-8},
  note = {access: abstract_only; cited as: H2-04 [3c]}
}

@article{chaffronGlobalNetworkCoexisting2010,
  author = {Chaffron, S and Rehrauer, H and Pernthaler, J and von Mering, C},
  title = {A global network of coexisting microbes from environmental and whole-genome sequence data},
  journal = {Genome Research},
  year = {2010},
  volume = {20},
  number = {7},
  pages = {947-959},
  doi = {10.1101/gr.104521.109},
  note = {access: full_text; cited as: H2-04 [4]}
}

@misc{calcagnoMetacommunityDynamicsDetection2021,
  author = {Calcagno, V and Cunniffe, N and Hamelin, FM},
  title = {Metacommunity dynamics and the detection of species associations in co-occurrence analyses: why patch disturbance matters},
  howpublished = {bioRxiv},
  year = {2021},
  doi = {10.1101/2021.06.14.448327},
  note = {access: abstract_only; type: preprint; cited as: H2-04 [4a]}
}

@article{chenLifehistoryStrategiesSoil2020,
  author = {Chen, Y and Neilson, JW and Kushwaha, P and Maier, RM and Barberán, A},
  title = {Life-history strategies of soil microbial communities in an arid ecosystem},
  journal = {The ISME Journal},
  year = {2021},
  volume = {15},
  number = {3},
  pages = {649-657},
  doi = {10.1038/s41396-020-00803-y},
  note = {access: abstract_only; cited as: H2-04 [4b]}
}

@article{carrUseAbuseCorrelation2019,
  author = {Carr, A and Diener, C and Baliga, NS and Gibbons, SM},
  title = {Use and abuse of correlation analyses in microbial ecology},
  journal = {The ISME Journal},
  year = {2019},
  volume = {13},
  number = {11},
  pages = {2647-2655},
  doi = {10.1038/s41396-019-0459-z},
  note = {access: secondary (critic: H2-04:C-052..054; the note said FT-s, full text read through a web-fetch tool summary, quotes to be rechecked); cited as: H2-04 [5]}
}

@article{barberanUsingNetworkAnalysis2011,
  author = {Barberán, A and Bates, ST and Casamayor, EO and Fierer, N},
  title = {Using network analysis to explore co-occurrence patterns in soil microbial communities},
  journal = {The ISME Journal},
  year = {2012},
  volume = {6},
  number = {2},
  pages = {343-351},
  doi = {10.1038/ismej.2011.119},
  note = {access: abstract_only; cited as: H2-04 [6]}
}

@article{dasVitroCoculturesHuman2018,
  author = {Das, P and Ji, B and Kovatcheva-Datchary, P and Bäckhed, F and Nielsen, J},
  title = {In vitro co-cultures of human gut bacterial species as predicted from co-occurrence network analysis},
  journal = {PLOS ONE},
  year = {2018},
  volume = {13},
  number = {3},
  pages = {e0195161},
  doi = {10.1371/journal.pone.0195161},
  note = {access: full_text; cited as: H2-04 [6a]; cited in the body by name, not by marker (critic: H2-04:C-082)}
}

@article{diazGlobalSpectrumPlant2015,
  author = {Díaz, S and Kattge, J and Cornelissen, JHC and Wright, IJ and Lavorel, S and Dray, S and Reu, B and Kleyer, M and Wirth, C and Prentice, IC and Garnier, E and Bönisch, G and Westoby, M and Poorter, H and Reich, PB and Moles, AT and Dickie, J and Gillison, AN and Zanne, AE and Chave, J and Wright, SJ and Sheremet'ev, SN and Jactel, H and Baraloto, C and Cerabolini, B and Pierce, S and Shipley, B and Kirkup, D and Casanoves, F and Joswig, JS and Günther, A and Falczuk, V and Rüger, N and Mahecha, MD and Gorné, LD},
  title = {The global spectrum of plant form and function},
  journal = {Nature},
  year = {2016},
  volume = {529},
  number = {7585},
  pages = {167-171},
  doi = {10.1038/nature16489},
  note = {access: abstract_only; cited as: H2-04 [6b]}
}

@article{deutschmannDisentanglingEnvironmentalEffects2021,
  author = {Deutschmann, IM and Lima-Mendez, G and Krabberød, AK and Raes, J and Vallina, SM and Faust, K and Logares, R},
  title = {Disentangling environmental effects in microbial association networks},
  journal = {Microbiome},
  year = {2021},
  volume = {9},
  number = {1},
  pages = {232},
  doi = {10.1186/s40168-021-01141-7},
  note = {access: full_text; cited as: H2-04 [7]}
}

@article{dongComponentsLeaftraitVariation2020,
  author = {Dong, N and Prentice, IC and Wright, IJ and Evans, BJ and Togashi, HF and Caddy-Retalic, S and McInerney, FA and Sparrow, B and Leitch, E and Lowe, AJ},
  title = {Components of leaf-trait variation along environmental gradients},
  journal = {New Phytologist},
  year = {2020},
  volume = {228},
  number = {1},
  pages = {82-94},
  doi = {10.1111/nph.16558},
  note = {access: abstract_only; cited as: H2-04 [7a]}
}

@article{friedmanInferringCorrelationNetworks2012,
  author = {Friedman, J and Alm, EJ},
  title = {Inferring correlation networks from genomic survey data},
  journal = {PLoS Computational Biology},
  year = {2012},
  volume = {8},
  number = {9},
  pages = {e1002687},
  doi = {10.1371/journal.pcbi.1002687},
  note = {access: abstract_only; cited as: H2-04 [8]}
}

@article{engTaxafunctionRobustnessMicrobial2018,
  author = {Eng, A and Borenstein, E},
  title = {Taxa-function robustness in microbial communities},
  journal = {Microbiome},
  year = {2018},
  volume = {6},
  number = {1},
  pages = {45},
  doi = {10.1186/s40168-018-0425-4},
  note = {access: full_text; cited as: H2-04 [8a]}
}

@article{faustMicrobialCooccurrenceRelationships2012,
  author = {Faust, K and Sathirapongsasuti, JF and Izard, J and Segata, N and Gevers, D and Raes, J and Huttenhower, C},
  title = {Microbial co-occurrence relationships in the human microbiome},
  journal = {PLoS Computational Biology},
  year = {2012},
  volume = {8},
  number = {7},
  pages = {e1002606},
  doi = {10.1371/journal.pcbi.1002606},
  note = {access: full_text; cited as: H2-04 [9]}
}

@article{faustOpenChallengesMicrobial2021,
  author = {Faust, K},
  title = {Open challenges for microbial network construction and analysis},
  journal = {The ISME Journal},
  year = {2021},
  volume = {15},
  number = {11},
  pages = {3111-3118},
  doi = {10.1038/s41396-021-01027-4},
  note = {access: full_text; cited as: H2-04 [9a]}
}

@article{fiererSeeingForestGenes2014,
  author = {Fierer, N and Barberán, A and Laughlin, DC},
  title = {Seeing the forest for the genes: using metagenomics to infer the aggregated traits of microbial communities},
  journal = {Frontiers in Microbiology},
  year = {2014},
  volume = {5},
  pages = {614},
  doi = {10.3389/fmicb.2014.00614},
  note = {access: abstract_only; cited as: H2-04 [10]; cited as a co-occurrence network study, which it is not (critic: H2-04:C-073..075; a community-aggregated-traits perspective)}
}

@article{fosterCompetitionNotCooperation2012,
  author = {Foster, KR and Bell, T},
  title = {Competition, not cooperation, dominates interactions among culturable microbial species},
  journal = {Current Biology},
  year = {2012},
  volume = {22},
  number = {19},
  pages = {1845-1850},
  doi = {10.1016/j.cub.2012.08.005},
  note = {access: abstract_only; cited as: H2-04 [10a]}
}

@article{freilichSpeciesCooccurrenceNetworks2018,
  author = {Freilich, MA and Wieters, E and Broitman, BR and Marquet, PA and Navarrete, SA},
  title = {Species co-occurrence networks: Can they reveal trophic and non-trophic interactions in ecological communities?},
  journal = {Ecology},
  year = {2018},
  volume = {99},
  number = {3},
  pages = {690-699},
  doi = {10.1002/ecy.2142},
  note = {access: abstract_only; cited as: H2-04 [10b]; also listed in Sources not obtained, which says nothing beyond a citation was reachable and that it supports no claim, while the reference list labels [10b] AB and the body cites it (conflict between the note's lists)}
}

@article{freilichCompetitiveCooperativeMetabolic2011,
  author = {Freilich, S and Zarecki, R and Eilam, O and Shtifman Segal, E and Henry, CS and Kupiec, M and Gophna, U and Sharan, R and Ruppin, E},
  title = {Competitive and cooperative metabolic interactions in bacterial communities},
  journal = {Nature Communications},
  year = {2011},
  volume = {2},
  pages = {589},
  doi = {10.1038/ncomms1597},
  note = {access: abstract_only; cited as: H2-04 [10c]; author corrected (critic: H2-04:C-072; the note said Segal ES); also listed in Sources not obtained, which says nothing beyond a citation was reachable and that it supports no claim, while the reference list labels it AB and the body cites it (conflict between the note's lists)}
}

@article{hiranoDifficultyInferringMicrobial2019,
  author = {Hirano, H and Takemoto, K},
  title = {Difficulty in inferring microbial community structure based on co-occurrence network approaches},
  journal = {BMC Bioinformatics},
  year = {2019},
  volume = {20},
  number = {1},
  pages = {329},
  doi = {10.1186/s12859-019-2915-1},
  note = {access: full_text; cited as: H2-04 [11]}
}

@misc{gralkaFundamentalMetabolicStrategies2022,
  author = {Gralka, M and Pollak, S and Cordero, OX},
  title = {Fundamental metabolic strategies of heterotrophic bacteria},
  howpublished = {bioRxiv},
  year = {2022},
  doi = {10.1101/2022.08.04.502823},
  note = {access: secondary (critic: H2-04:C-052..054; the note said FT-s, preprint read through a web-fetch tool summary); type: preprint; cited as: H2-04 [11a] (the preprint read)}
}

@article{gralkaGenomeContentPredicts2023,
  author = {Gralka, M and Pollak, S and Cordero, OX},
  title = {Genome content predicts the carbon catabolic preferences of heterotrophic bacteria},
  journal = {Nature Microbiology},
  year = {2023},
  volume = {8},
  number = {10},
  pages = {1799-1808},
  doi = {10.1038/s41564-023-01458-z},
  note = {access: abstract_only; cited as: H2-04 [11a] (published version of the preprint)}
}

@article{goldfordEmergentSimplicityMicrobial2018,
  author = {Goldford, JE and Lu, N and Bajić, D and Estrela, S and Tikhonov, M and Sanchez-Gorostiaga, A and Segrè, D and Mehta, P and Sanchez, A},
  title = {Emergent simplicity in microbial community assembly},
  journal = {Science},
  year = {2018},
  volume = {361},
  number = {6401},
  pages = {469-474},
  doi = {10.1126/science.aat1168},
  note = {access: abstract_only; cited as: H2-04 [11b]; also listed in Sources not obtained, which says nothing beyond a citation was reachable and that it supports no claim, while the reference list labels [11b] AB and the body cites it (conflict between the note's lists)}
}

@article{hawkinsStructuralBiasAggregated2017,
  author = {Hawkins, BA and Leroy, B and Rodríguez, MÁ and Singer, A and Vilela, B and Villalobos, F and Wang, X and Zelený, D},
  title = {Structural bias in aggregated species-level variables driven by repeated species co-occurrences: a pervasive problem in community and assemblage data},
  journal = {Journal of Biogeography},
  year = {2017},
  volume = {44},
  number = {6},
  pages = {1199-1211},
  doi = {10.1111/jbi.12953},
  note = {access: abstract_only; cited as: H2-04 [12]}
}

@article{kishoreInferringMicrobialCooccurrence2023,
  author = {Kishore, D and Birzu, G and Hu, Z and DeLisi, C and Korolev, KS and Segrè, D},
  title = {Inferring microbial co-occurrence networks from amplicon data: a systematic evaluation},
  journal = {mSystems},
  year = {2023},
  volume = {8},
  number = {4},
  pages = {e00961-22},
  doi = {10.1128/msystems.00961-22},
  note = {access: full_text; cited as: H2-04 [13]; volume 8, issue 4 not in the Crossref record, which gives only article e00961-22 (critic: H2-04:C-080)}
}

@article{jiangFunctionalBiogeographyOcean2012,
  author = {Jiang, X and Langille, MGI and Neches, RY and Elliot, M and Levin, SA and Eisen, JA and Weitz, JS and Dushoff, J},
  title = {Functional biogeography of ocean microbes revealed through non-negative matrix factorization},
  journal = {PLoS ONE},
  year = {2012},
  volume = {7},
  number = {9},
  pages = {e43866},
  doi = {10.1371/journal.pone.0043866},
  note = {access: abstract_only; cited as: H2-04 [13a]}
}

@article{kamnevaGenomeCompositionPhylogeny2017,
  author = {Kamneva, OK},
  title = {Genome composition and phylogeny of microbes predict their co-occurrence in the environment},
  journal = {PLOS Computational Biology},
  year = {2017},
  volume = {13},
  number = {2},
  pages = {e1005366},
  doi = {10.1371/journal.pcbi.1005366},
  note = {access: full_text; cited as: H2-04 [14]}
}

@article{kurtzSparseCompositionallyRobust2015,
  author = {Kurtz, ZD and Müller, CL and Miraldi, ER and Littman, DR and Blaser, MJ and Bonneau, RA},
  title = {Sparse and compositionally robust inference of microbial ecological networks},
  journal = {PLOS Computational Biology},
  year = {2015},
  volume = {11},
  number = {5},
  pages = {e1004226},
  doi = {10.1371/journal.pcbi.1004226},
  note = {access: abstract_only; cited as: H2-04 [15]}
}

@article{kembelIndependentEvolutionLeaf2011,
  author = {Kembel, SW and Cahill, JF},
  title = {Independent evolution of leaf and root traits within and among temperate grassland plant communities},
  journal = {PLoS ONE},
  year = {2011},
  volume = {6},
  number = {6},
  pages = {e19992},
  doi = {10.1371/journal.pone.0019992},
  note = {access: full_text; cited as: H2-04 [16]}
}

@article{levyMetabolicModelingSpecies2013,
  author = {Levy, R and Borenstein, E},
  title = {Metabolic modeling of species interaction in the human microbiome elucidates community-level assembly rules},
  journal = {Proceedings of the National Academy of Sciences of the United States of America},
  year = {2013},
  volume = {110},
  number = {31},
  pages = {12804-12809},
  doi = {10.1073/pnas.1300926110},
  note = {access: secondary (critic: H2-04:C-052..054; the note said FT-s, full text read through a web-fetch tool summary, quotes to be rechecked); cited as: H2-04 [17]}
}

@article{limamendezDeterminantsCommunityStructure2015,
  author = {Lima-Mendez, G and Faust, K and Henry, N and Decelle, J and Colin, S and Carcillo, F and Chaffron, S and Ignacio-Espinosa, JC and Roux, S and Vincent, F and Bittner, L and Darzi, Y and Wang, J and Audic, S and Berline, L and Bontempi, G and Cabello, AM and Coppola, L and Cornejo-Castillo, FM and d'Ovidio, F and De Meester, L and Ferrera, I and Garet-Delmas, MJ and Guidi, L and Lara, E and Pesant, S and Royo-Llonch, M and Salazar, G and Sánchez, P and Sebastian, M and Souffreau, C and Dimier, C and Picheral, M and Searson, S and Kandels-Lewis, S and {Tara Oceans coordinators} and Gorsky, G and Not, F and Ogata, H and Speich, S and Stemmann, L and Weissenbach, J and Wincker, P and Acinas, SG and Sunagawa, S and Bork, P and Sullivan, MB and Karsenti, E and Bowler, C and de Vargas, C and Raes, J},
  title = {Determinants of community structure in the global plankton interactome},
  journal = {Science},
  year = {2015},
  volume = {348},
  number = {6237},
  pages = {1262073},
  doi = {10.1126/science.1262073},
  note = {access: abstract_only; cited as: H2-04 [17a]; also listed in Sources not obtained, which says nothing beyond a citation was reachable and that it supports no claim, while the reference list labels [17a] AB and the body cites it (conflict between the note's lists)}
}

@article{metahitIdentificationAssemblyGenomes2014,
  author = {{MetaHIT Consortium} and Nielsen, HB and Almeida, M and Juncker, AS and Rasmussen, S and Li, J and Sunagawa, S and Plichta, DR and Gautier, L and Pedersen, AG and Le Chatelier, E and Pelletier, E and Bonde, I and Nielsen, T and Manichanh, C and Arumugam, M and Batto, JM and Quintanilha dos Santos, MB and Blom, N and Borruel, N and Burgdorf, KS and Boumezbeur, F and Casellas, F and Doré, J and Dworzynski, P and Guarner, F and Hansen, T and Hildebrand, F and Kaas, RS and Kennedy, S and Kristiansen, K and Kultima, JR and Léonard, P and Levenez, F and Lund, O and Moumen, B and Le Paslier, D and Pons, N and Pedersen, O and Prifti, E and Qin, J and Raes, J and Sørensen, S and Tap, J and Tims, S and Ussery, DW and Yamada, T and Renault, P and Sicheritz-Ponten, T and Bork, P and Wang, J and Brunak, S and Ehrlich, SD},
  title = {Identification and assembly of genomes and genetic elements in complex metagenomic samples without using reference genomes},
  journal = {Nature Biotechnology},
  year = {2014},
  volume = {32},
  number = {8},
  pages = {822-828},
  doi = {10.1038/nbt.2939},
  note = {access: abstract_only; cited as: H2-04 [18]; Crossref lists MetaHIT Consortium first (the note's search record)}
}

@article{morrisBlackQueenHypothesis2012,
  author = {Morris, JJ and Lenski, RE and Zinser, ER},
  title = {The Black Queen Hypothesis: evolution of dependencies through adaptive gene loss},
  journal = {mBio},
  year = {2012},
  volume = {3},
  number = {2},
  pages = {e00036-12},
  doi = {10.1128/mBio.00036-12},
  note = {access: abstract_only; cited as: H2-04 [18a]}
}

@article{loucaDecouplingFunctionTaxonomy2016,
  author = {Louca, S and Parfrey, LW and Doebeli, M},
  title = {Decoupling function and taxonomy in the global ocean microbiome},
  journal = {Science},
  year = {2016},
  volume = {353},
  number = {6305},
  pages = {1272-1277},
  doi = {10.1126/science.aaf4507},
  note = {access: abstract_only; cited as: H2-04 [18b]}
}

@article{machadoPolarizationMicrobialCommunities2021,
  author = {Machado, D and Maistrenko, OM and Andrejev, S and Kim, Y and Bork, P and Patil, Kaustubh R. and Patil, Kiran R.},
  title = {Polarization of microbial communities between competitive and cooperative metabolism},
  journal = {Nature Ecology & Evolution},
  year = {2021},
  volume = {5},
  number = {2},
  pages = {195-203},
  doi = {10.1038/s41559-020-01353-4},
  note = {access: full_text; cited as: H2-04 [19]; the two Patil authors given in full (critic: H2-04:C-076..078; the note said Patil KR, Patil KR)}
}

@article{marslandMinimalModelMicrobial2020,
  author = {Marsland, R and Cui, W and Mehta, P},
  title = {A minimal model for microbial biodiversity can reproduce experimentally observed ecological patterns},
  journal = {Scientific Reports},
  year = {2020},
  volume = {10},
  number = {1},
  pages = {3308},
  doi = {10.1038/s41598-020-60130-2},
  note = {access: abstract_only; cited as: H2-04 [19a]}
}

@article{kehePositiveInteractionsCommon2021,
  author = {Kehe, J and Ortiz, A and Kulesa, A and Gore, J and Blainey, PC and Friedman, J},
  title = {Positive interactions are common among culturable bacteria},
  journal = {Science Advances},
  year = {2021},
  volume = {7},
  number = {45},
  pages = {eabi7159},
  doi = {10.1126/sciadv.abi7159},
  note = {access: full_text; cited as: H2-04 [20]}
}

@article{messierHowDoTraits2010,
  author = {Messier, J and McGill, BJ and Lechowicz, MJ},
  title = {How do traits vary across ecological scales? A case for trait-based ecology},
  journal = {Ecology Letters},
  year = {2010},
  volume = {13},
  number = {7},
  pages = {838-848},
  doi = {10.1111/j.1461-0248.2010.01476.x},
  note = {access: abstract_only; cited as: H2-04 [20a]}
}

@article{messierTraitVariationIntegration2016,
  author = {Messier, J and McGill, BJ and Enquist, BJ and Lechowicz, MJ},
  title = {Trait variation and integration across scales: is the leaf economic spectrum present at local scales?},
  journal = {Ecography},
  year = {2017},
  volume = {40},
  number = {6},
  pages = {685-697},
  doi = {10.1111/ecog.02006},
  note = {access: abstract_only; cited as: H2-04 [20b]}
}

@article{loucaFunctionFunctionalRedundancy2018,
  author = {Louca, S and Polz, MF and Mazel, F and Albright, MBN and Huber, JA and O'Connor, MI and Ackermann, M and Hahn, AS and Srivastava, DS and Crowe, SA and Doebeli, M and Parfrey, LW},
  title = {Function and functional redundancy in microbial systems},
  journal = {Nature Ecology & Evolution},
  year = {2018},
  volume = {2},
  number = {6},
  pages = {936-943},
  doi = {10.1038/s41559-018-0519-1},
  note = {access: abstract_only; cited as: H2-04 [21]; not cited (critic: H2-04:C-081)}
}

@article{osnasDivergentDriversLeaf2018,
  author = {Osnas, JLD and Katabuchi, M and Kitajima, K and Wright, SJ and Reich, PB and Van Bael, SA and Kraft, NJB and Samaniego, MJ and Pacala, SW and Lichstein, JW},
  title = {Divergent drivers of leaf trait variation within species, among species, and among functional groups},
  journal = {Proceedings of the National Academy of Sciences of the United States of America},
  year = {2018},
  volume = {115},
  number = {21},
  pages = {5480-5485},
  doi = {10.1073/pnas.1803989115},
  note = {access: full_text; cited as: H2-04 [22]}
}

@article{ovaskainenHowMakeMore2017,
  author = {Ovaskainen, O and Tikhonov, G and Norberg, A and Blanchet, FG and Duan, L and Dunson, D and Roslin, T and Abrego, N},
  title = {How to make more out of community data? A conceptual framework and its implementation as models and software},
  journal = {Ecology Letters},
  year = {2017},
  volume = {20},
  number = {5},
  pages = {561-576},
  doi = {10.1111/ele.12757},
  note = {access: abstract_only; cited as: H2-04 [22a]}
}

@article{pitonLifeHistoryStrategies2023,
  author = {Piton, G and Allison, SD and Bahram, M and Hildebrand, F and Martiny, JBH and Treseder, KK and Martiny, AC},
  title = {Life history strategies of soil bacterial communities across global terrestrial biomes},
  journal = {Nature Microbiology},
  year = {2023},
  volume = {8},
  number = {11},
  pages = {2093-2102},
  doi = {10.1038/s41564-023-01465-0},
  note = {access: full_text (accepted manuscript); cited as: H2-04 [23]}
}

@article{peresnetoLinkingTraitVariation2017,
  author = {Peres-Neto, PR and Dray, S and ter Braak, CJF},
  title = {Linking trait variation to the environment: critical issues with community-weighted mean correlation resolved by the fourth-corner approach},
  journal = {Ecography},
  year = {2017},
  volume = {40},
  number = {7},
  pages = {806-816},
  doi = {10.1111/ecog.02302},
  note = {access: abstract_only; cited as: H2-04 [23a]; title corrected (critic: H2-04:C-071; the note said resolved by applying a fourth-corner approach)}
}

@article{puglielliIntraspecificVariabilityLeaf2024,
  author = {Puglielli, G and Bricca, A and Chelli, S and Petruzzellis, F and Acosta, ATR and Bacaro, G and Beccari, E and Bernardo, L and Bonari, G and Bolpagni, R and Boscutti, F and Calvia, G and Campetella, G and Cancellieri, L and Canullo, R and Carbognani, M and Carboni, M and Carranza, ML and Castellani, MB and Ciccarelli, D and Coppi, A and Cutini, M and Dalla Vecchia, A and Dalle Fratte, M and de Francesco, MC and De Frenne, P and De Sanctis, M and de Simone, L and Di Cecco, V and Fanelli, G and Farris, E and Ferrara, A and Fenu, G and Filibeck, G and Gasperini, C and Gargano, D and Kindermann, E and La Bella, G and Lastrucci, L and Lazzaro, L and Maccherini, S and Marignani, M and Mugnai, M and Naselli-Flores, L and Passalacqua, NG and Pavanetto, N and Petraglia, A and Rota, F and Santoianni, LA and Schettino, A and Selvi, F and Stanisci, A and Trotta, G and Vangansbeke, P and Varricchione, M and Vuerich, M and Wellstein, C and Tordoni, E},
  title = {Intraspecific variability of leaf form and function across habitat types},
  journal = {Ecology Letters},
  year = {2024},
  volume = {27},
  number = {3},
  pages = {e14396},
  doi = {10.1111/ele.14396},
  note = {access: abstract_only; cited as: H2-04 [24a]}
}

@article{puglielliQuantifyingInfluenceIntraspecific2025,
  author = {Puglielli, G and Carmona, CP and Bissi, A and Tordoni, E},
  title = {Quantifying the influence of intraspecific variability in trait spaces},
  journal = {npj Biodiversity},
  year = {2025},
  volume = {4},
  pages = {36},
  doi = {10.1038/s44185-025-00101-w},
  note = {access: full_text; cited as: H2-04 [24b]}
}

@article{poggiatoInterpretationsJointModeling2021,
  author = {Poggiato, G and Münkemüller, T and Bystrova, D and Arbel, J and Clark, JS and Thuiller, W},
  title = {On the interpretations of joint modeling in community ecology},
  journal = {Trends in Ecology & Evolution},
  year = {2021},
  volume = {36},
  number = {5},
  pages = {391-401},
  doi = {10.1016/j.tree.2021.01.002},
  note = {access: abstract_only; cited as: H2-04 [24c]}
}

@article{pachecoCostlessMetabolicSecretions2019,
  author = {Pacheco, AR and Moel, M and Segrè, D},
  title = {Costless metabolic secretions as drivers of interspecies interactions in microbial ecosystems},
  journal = {Nature Communications},
  year = {2019},
  volume = {10},
  number = {1},
  pages = {103},
  doi = {10.1038/s41467-018-07946-9},
  note = {access: abstract_only; cited as: H2-04 [24d]}
}

@article{priceFillingGapsBacterial2018,
  author = {Price, MN and Zane, GM and Kuehl, JV and Melnyk, RA and Wall, JD and Deutschbauer, AM and Arkin, AP},
  title = {Filling gaps in bacterial amino acid biosynthesis pathways with high-throughput genetics},
  journal = {PLOS Genetics},
  year = {2018},
  volume = {14},
  number = {1},
  pages = {e1007147},
  doi = {10.1371/journal.pgen.1007147},
  note = {access: abstract_only; cited as: H2-04 [25]}
}

@article{smillieEcologyDrivesGlobal2011,
  author = {Smillie, CS and Smith, MB and Friedman, J and Cordero, OX and David, LA and Alm, EJ},
  title = {Ecology drives a global network of gene exchange connecting the human microbiome},
  journal = {Nature},
  year = {2011},
  volume = {480},
  number = {7376},
  pages = {241-244},
  doi = {10.1038/nature10571},
  note = {access: abstract_only; cited as: H2-04 [26]}
}

@article{siefertGlobalMetaanalysisRelative2015,
  author = {Siefert, A and Violle, C and Chalmandrier, L and Albert, CH and Taudiere, A and Fajardo, A and Aarssen, LW and Baraloto, C and Carlucci, MB and Cianciaruso, MV and Dantas, VL and de Bello, F and Duarte, LDS and Fonseca, CR and Freschet, GT and Gaucherand, S and Gross, N and Hikosaka, K and Jackson, B and Jung, V and Kamiyama, C and Katabuchi, M and Kembel, SW and Kichenin, E and Kraft, NJB and Lagerström, A and Le Bagousse-Pinguet, Y and Li, Y and Mason, N and Messier, J and Nakashizuka, T and Overton, JM and Peltzer, DA and Pérez-Ramos, IM and Pillar, VD and Prentice, HC and Richardson, S and Sasaki, T and Schamp, BS and Schöb, C and Shipley, B and Sundqvist, M and Sykes, MT and Vandewalle, M and Wardle, DA},
  title = {A global meta-analysis of the relative extent of intraspecific trait variation in plant communities},
  journal = {Ecology Letters},
  year = {2015},
  volume = {18},
  number = {12},
  pages = {1406-1419},
  doi = {10.1111/ele.12508},
  note = {access: abstract_only; cited as: H2-04 [27]}
}

@article{russelAntagonismCorrelatesMetabolic2017,
  author = {Russel, J and Røder, HL and Madsen, JS and Burmølle, M and Sørensen, SJ},
  title = {Antagonism correlates with metabolic similarity in diverse bacteria},
  journal = {Proceedings of the National Academy of Sciences of the United States of America},
  year = {2017},
  volume = {114},
  number = {40},
  pages = {10684-10688},
  doi = {10.1073/pnas.1706016114},
  note = {access: secondary (critic: H2-04:C-052..054; the note said FT-s, full text read through a web-fetch tool summary, quotes to be rechecked); cited as: H2-04 [28]}
}

@article{starkeAminoAcidAuxotrophies2023,
  author = {Starke, S and Harris, DMM and Zimmermann, J and Schuchardt, S and Oumari, M and Frank, D and Bang, C and Rosenstiel, P and Schreiber, S and Frey, N and Franke, A and Aden, K and Waschina, S},
  title = {Amino acid auxotrophies in human gut bacteria are linked to higher microbiome diversity and long-term stability},
  journal = {The ISME Journal},
  year = {2023},
  volume = {17},
  number = {12},
  pages = {2370-2380},
  doi = {10.1038/s41396-023-01537-3},
  note = {access: full_text; cited as: H2-04 [29]}
}

@article{tianDecipheringFunctionalRedundancy2020,
  author = {Tian, L and Wang, XW and Wu, AK and Fan, Y and Friedman, J and Dahlin, A and Waldor, MK and Weinstock, GM and Weiss, ST and Liu, YY},
  title = {Deciphering functional redundancy in the human microbiome},
  journal = {Nature Communications},
  year = {2020},
  volume = {11},
  number = {1},
  pages = {6217},
  doi = {10.1038/s41467-020-19940-1},
  note = {access: full_text; cited as: H2-04 [30]}
}

@article{weissCorrelationDetectionStrategies2016,
  author = {Weiss, S and Van Treuren, W and Lozupone, C and Faust, K and Friedman, J and Deng, Y and Xia, LC and Xu, ZZ and Ursell, L and Alm, EJ and Birmingham, A and Cram, JA and Fuhrman, JA and Raes, J and Sun, F and Zhou, J and Knight, R},
  title = {Correlation detection strategies in microbial data sets vary widely in sensitivity and precision},
  journal = {The ISME Journal},
  year = {2016},
  volume = {10},
  number = {7},
  pages = {1669-1681},
  doi = {10.1038/ismej.2015.235},
  note = {access: full_text; cited as: H2-04 [31]}
}

@article{wieczynskiClimateShapesShifts2018,
  author = {Wieczynski, DJ and Boyle, B and Buzzard, V and Duran, SM and Henderson, AN and Hulshof, CM and Kerkhoff, AJ and McCarthy, MC and Michaletz, ST and Swenson, NG and Asner, GP and Bentley, LP and Enquist, BJ and Savage, VM},
  title = {Climate shapes and shifts functional biodiversity in forests worldwide},
  journal = {Proceedings of the National Academy of Sciences of the United States of America},
  year = {2019},
  volume = {116},
  number = {2},
  pages = {587-592},
  doi = {10.1073/pnas.1813723116},
  note = {access: abstract_only; cited as: H2-04 [32]}
}

@article{violleReturnVarianceIntraspecific2012,
  author = {Violle, C and Enquist, BJ and McGill, BJ and Jiang, L and Albert, CH and Hulshof, C and Jung, V and Messier, J},
  title = {The return of the variance: intraspecific variability in community ecology},
  journal = {Trends in Ecology & Evolution},
  year = {2012},
  volume = {27},
  number = {4},
  pages = {244-252},
  doi = {10.1016/j.tree.2011.11.014},
  note = {access: abstract_only; cited as: H2-04 [32a]}
}

@article{westobyCellSizeGenome2021,
  author = {Westoby, M and Nielsen, DA and Gillings, MR and Litchman, E and Madin, JS and Paulsen, IT and Tetu, SG},
  title = {Cell size, genome size, and maximum growth rate are near-independent dimensions of ecological variation across bacteria and archaea},
  journal = {Ecology and Evolution},
  year = {2021},
  volume = {11},
  number = {9},
  pages = {3956-3976},
  doi = {10.1002/ece3.7290},
  note = {access: full_text; cited as: H2-04 [33]}
}

@article{vieirasilvaSystemicImprintGrowth2010,
  author = {Vieira-Silva, S and Rocha, EPC},
  title = {The systemic imprint of growth and its uses in ecological (meta)genomics},
  journal = {PLoS Genetics},
  year = {2010},
  volume = {6},
  number = {1},
  pages = {e1000808},
  doi = {10.1371/journal.pgen.1000808},
  note = {access: abstract_only; cited as: H2-04 [33a]}
}

@article{westobyTraitDimensionsBacteria2021,
  author = {Westoby, M and Gillings, MR and Madin, JS and Nielsen, DA and Paulsen, IT and Tetu, SG},
  title = {Trait dimensions in bacteria and archaea compared to vascular plants},
  journal = {Ecology Letters},
  year = {2021},
  volume = {24},
  number = {7},
  pages = {1487-1504},
  doi = {10.1111/ele.13742},
  note = {access: abstract_only; cited as: H2-04 [33b]; not cited (critic: H2-04:C-081)}
}

@article{zhouFunctionalMolecularEcological2010,
  author = {Zhou, J and Deng, Y and Luo, F and He, Z and Tu, Q and Zhi, X},
  title = {Functional molecular ecological networks},
  journal = {mBio},
  year = {2010},
  volume = {1},
  number = {4},
  pages = {e00169-10},
  doi = {10.1128/mBio.00169-10},
  note = {access: full_text; cited as: H2-04 [34]}
}

@article{wrightWorldwideLeafEconomics2004,
  author = {Wright, IJ and Reich, PB and Westoby, M and Ackerly, DD and Baruch, Z and Bongers, F and Cavender-Bares, J and Chapin, T and Cornelissen, JHC and Diemer, M and Flexas, J and Garnier, E and Groom, PK and Gulias, J and Hikosaka, K and Lamont, BB and Lee, T and Lee, W and Lusk, C and Midgley, JJ and Navas, ML and Niinemets, Ü and Oleksyn, J and Osada, N and Poorter, H and Poot, P and Prior, L and Pyankov, VI and Roumet, C and Thomas, SC and Tjoelker, MG and Veneklaas, EJ and Villar, R},
  title = {The worldwide leaf economics spectrum},
  journal = {Nature},
  year = {2004},
  volume = {428},
  number = {6985},
  pages = {821-827},
  doi = {10.1038/nature02403},
  note = {access: abstract_only; cited as: H2-04 [34a]}
}

@article{zelenyWhichResultsStandard2018,
  author = {Zelený, D},
  title = {Which results of the standard test for community-weighted mean approach are too optimistic?},
  journal = {Journal of Vegetation Science},
  year = {2018},
  volume = {29},
  number = {6},
  pages = {953-966},
  doi = {10.1111/jvs.12688},
  note = {access: abstract_only (via bioRxiv preprint abstract doi:10.1101/349589); cited as: H2-04 [35]}
}

@article{zelezniakMetabolicDependenciesDrive2015,
  author = {Zelezniak, A and Andrejev, S and Ponomarova, O and Mende, DR and Bork, P and Patil, KR},
  title = {Metabolic dependencies drive species co-occurrence in diverse microbial communities},
  journal = {Proceedings of the National Academy of Sciences of the United States of America},
  year = {2015},
  volume = {112},
  number = {20},
  pages = {6449-6454},
  doi = {10.1073/pnas.1421834112},
  note = {access: secondary (critic: H2-04:C-052..054; the note said FT-s, full text read through a web-fetch tool summary, quotes to be rechecked); cited as: H2-04 [36]}
}

@article{zurellDoJointSpecies2018,
  author = {Zurell, D and Pollock, LJ and Thuiller, W},
  title = {Do joint species distribution models reliably detect interspecific interactions from co-occurrence data in homogenous environments?},
  journal = {Ecography},
  year = {2018},
  volume = {41},
  number = {11},
  pages = {1812-1819},
  doi = {10.1111/ecog.03315},
  note = {access: abstract_only; cited as: H2-04 [37]}
}

@article{gusevaDiversityComplexityMicrobial2022,
  author = {Guseva, K and Darcy, S and Simon, E and Alteio, LV and Montesinos-Navarro, A and Kaiser, C},
  title = {From diversity to complexity: Microbial networks in soils},
  journal = {Soil Biology and Biochemistry},
  year = {2022},
  volume = {169},
  pages = {108604},
  doi = {10.1016/j.soilbio.2022.108604},
  note = {access: full_text; cited as: H2-04 [38]; listed only: not cited in the body; the review's additional notes after the reference list discuss it}
}

@article{pascualgarciaBacteriaDialogSanta2014,
  author = {Pascual-García, A and Tamames, J and Bastolla, U},
  title = {Bacteria dialog with Santa Rosalia: Are aggregations of cosmopolitan bacteria mainly explained by habitat filtering or by ecological interactions?},
  journal = {BMC Microbiology},
  year = {2014},
  volume = {14},
  number = {1},
  pages = {284},
  doi = {10.1186/s12866-014-0284-5},
  note = {access: full_text; cited as: H2-04 [39]; listed only: not cited in the body; the review's additional notes after the reference list discuss it}
}

@article{manorSystematicCharacterizationAnalysis2017,
  author = {Manor, O and Borenstein, E},
  title = {Systematic characterization and analysis of the taxonomic drivers of functional shifts in the human microbiome},
  journal = {Cell Host & Microbe},
  year = {2017},
  volume = {21},
  number = {2},
  pages = {254-267},
  doi = {10.1016/j.chom.2016.12.014},
  note = {access: abstract_only; cited as: H2-04 [40]; listed only: not cited in the body; the review's additional notes after the reference list discuss it}
}

@article{tackmannRapidInferenceDirect2019,
  author = {Tackmann, J and Matias Rodrigues, JF and von Mering, C},
  title = {Rapid inference of direct interactions in large-scale ecological networks from heterogeneous microbial sequencing data},
  journal = {Cell Systems},
  year = {2019},
  volume = {9},
  number = {3},
  pages = {286-296.e8},
  doi = {10.1016/j.cels.2019.08.002},
  note = {access: abstract_only; cited as: H2-04 [41]; listed only: not cited in the body; the review's additional notes after the reference list discuss it}
}

@article{gobernaCautionaryNotesUse2022,
  author = {Goberna, M and Verdú, M},
  title = {Cautionary notes on the use of co-occurrence networks in soil ecology},
  journal = {Soil Biology and Biochemistry},
  year = {2022},
  volume = {166},
  pages = {108534},
  doi = {10.1016/j.soilbio.2021.108534},
  note = {access: not_obtained (Europe PMC abstract seen only in index record; full text not attempted); not cited; listed in Sources not obtained}
}

@article{lepsCommunityTraitResponse2011,
  author = {Lepš, J. and de Bello, F. and Šmilauer, P. and Doležal, J.},
  title = {Community trait response to environment: disentangling species turnover vs intraspecific trait variability effects},
  journal = {Ecography},
  year = {2011},
  volume = {34},
  number = {5},
  pages = {856-863},
  doi = {10.1111/j.1600-0587.2010.06904.x},
  note = {access: not_obtained (Crossref metadata only; abstract elided; no OA location; Wiley HTTP 403); not cited; listed twice in Sources not obtained; named in the answers as Leps et al. 2011, not obtained}
}

@article{debelloQuantifyingRelevanceIntraspecific2010,
  author = {de Bello, F. and Lavorel, S. and Albert, C. H. and Thuiller, W. and Grigulis, K. and Dolezal, J. and Janeček, Š. and Lepš, J.},
  title = {Quantifying the relevance of intraspecific trait variability for functional diversity},
  journal = {Methods in Ecology and Evolution},
  year = {2011},
  volume = {2},
  number = {2},
  pages = {163-174},
  doi = {10.1111/j.2041-210X.2010.00071.x},
  note = {access: not_obtained (Crossref metadata only; Wiley 403); not cited; listed twice in Sources not obtained; key kept from the refs bibliography}
}

@article{hadfieldGeneralQuantitativeGenetic2010,
  author = {Hadfield, J. D. and Nakagawa, S.},
  title = {General quantitative genetic methods for comparative biology: phylogenies, taxonomies and multi-trait models for continuous and categorical characters},
  journal = {Journal of Evolutionary Biology},
  year = {2010},
  volume = {23},
  number = {3},
  pages = {494-508},
  doi = {10.1111/j.1420-9101.2009.01915.x},
  note = {access: not_obtained (Europe PMC abstract read; full text not attempted); not cited; listed twice in Sources not obtained, which says nothing beyond a citation was reachable, while its routes say the abstract was read (conflict within the list)}
}

@article{neyretSlowfastTraitContinuum2024,
  author = {Neyret, M. and Le Provost, G. and Boesing, A. L. and others},
  title = {A slow-fast trait continuum at the whole community level in relation to land-use intensification},
  journal = {Nature Communications},
  year = {2024},
  volume = {15},
  pages = {1251},
  doi = {10.1038/s41467-024-45113-5},
  note = {access: full_text (Europe PMC full text XML, PMC10858939, obtained and grepped); not cited; listed in Sources not obtained although its full text was obtained, and not entered as a finding (conflict between the list's heading and its routes); incomplete: author}
}

@article{faustMicrobialInteractionsNetworks2012,
  author = {Faust, K and Raes, J},
  title = {Microbial interactions: from networks to models},
  journal = {Nature Reviews Microbiology},
  year = {2012},
  volume = {10},
  number = {8},
  pages = {538-550},
  doi = {10.1038/nrmicro2832},
  note = {access: not_obtained (Crossref citation and DOI verification only; not read); not cited; listed in Sources not obtained}
}

@article{rottjersHairballsHypothesesbiologicalInsights2018,
  author = {Röttjers, L and Faust, K},
  title = {From hairballs to hypotheses: biological insights from microbial networks},
  journal = {FEMS Microbiology Reviews},
  year = {2018},
  volume = {42},
  number = {6},
  pages = {761-780},
  doi = {10.1093/femsre/fuy030},
  note = {access: not_obtained (Crossref citation and DOI verification only; not read); not cited; listed in Sources not obtained; key kept from the refs bibliography}
}
@article{gloorMicrobiomeDatasetsCompositional2017,
  author = {Gloor, Gregory B. and Macklaim, Jean M. and Pawlowsky-Glahn, Vera and Egozcue, Juan J.},
  title = {Microbiome Datasets Are Compositional: And This Is Not Optional},
  journal = {Frontiers in Microbiology},
  year = {2017},
  volume = {8},
  pages = {2224},
  doi = {10.3389/fmicb.2017.02224},
  note = {background; access: abstract_only (checked for the background entry: Crossref record and Semantic Scholar abstract)}
}

@article{garnierPlantFunctionalMarkers2004,
  author = {Garnier, Eric and Cortez, Jacques and Billès, Georges and Navas, Marie-Laure and Roumet, Catherine and Debussche, Max and Laurent, Gérard and Blanchard, Alain and Aubry, David and Bellmann, Astrid and Neill, Cathy and Toussaint, Jean-Patrick},
  title = {Plant Functional Markers Capture Ecosystem Properties During Secondary Succession},
  journal = {Ecology},
  year = {2004},
  volume = {85},
  number = {9},
  pages = {2630-2637},
  doi = {10.1890/03-0799},
  note = {background; access: abstract_only (checked for the background entry: Crossref record and Europe PMC abstract)}
}
```
