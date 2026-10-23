---
type: knowledge
title: Sources of functional covariation and cross-level functional axes
inputs:
  - H2-04: PhD/Proposal/Research/Results/Sources of functional covariation across microbial community samples, their partition, and the relation between genome-level and community-level functional axes a literature review.md
refs: PhD/Proposal/Refs/Refs.bib
built: 2026-10-23
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

### within-genome-linkage: linkage of genes within genomes
needs: none

- **within-genome-linkage.1** Gene covariation across metagenomes is organised by genome membership in gene co-abundance binning: across 396 human gut metagenomes, genes clustered into 7,381 co-abundance groups, including 741 metagenomic species, from which 238 high-quality genomes were assembled; no share of total gene covariation attributable to genome membership is reported.
  conf: single (critic: C-003) · class: meas (marker) · holds: 396 human gut metagenomes; read in the abstract only; the within-genome-linkage evidence at gene level rests on this one abstract; the counts were checked against the abstract by the critic · src: metahitIdentificationAssemblyGenomes2014 (AB; measured; single; critic: C-003 was "AB; measured; replicated method family") · trail: H2-04 §Linkage within genomes, §answers, §critic · from: H2-04:I-0003, H2-04:B-0031, H2-04:A-002, H2-04:A-017, H2-04:C-003, H2-04:C-045
- **within-genome-linkage.2** No search route found a fraction of total gene-gene covariance attributable to genome membership.
  conf: not stated · class: search (note: "no search route found one") · holds: gene co-abundance binning of gut metagenomes; routes as in the note's search record · src: metahitIdentificationAssemblyGenomes2014 (AB) · search: searched, not found (note: "no search route found one") · trail: H2-04 §Linkage within genomes · from: H2-04:B-0031, H2-04:I-0003, H2-04:B-0010
- **within-genome-linkage.3** In 2,540 aquifer genomes, most organisms carried one step of sequential redox pathways, few carried two, and very few three or more; the authors argue incompleteness does not explain this (stepwise division of redox pathways across aquifer genomes).
  conf: single (marker) · class: deriv (marker) · holds: one aquifer system; community composition and genomes from the same metagenomes; the critic: one aquifer study, not evidence for a class of functions · src: anantharamanThousandsMicrobialGenomes2016 (FT; derived; single study) · trail: H2-04 §Linkage within genomes, §answers, §Adversarial critique · from: H2-04:I-0004, H2-04:A-042, H2-04:C-066
- **within-genome-linkage.4** Genome incompleteness produces false gene absences: predicted auxotrophies correlate negatively with genome completeness.
  conf: not stated · class: not stated · holds: amino acid auxotrophies predicted from human gut bacterial genomes, as a caution on measured linkage · src: starkeAminoAcidAuxotrophies2023 (FT) · trail: H2-04 §Linkage within genomes, §answers · from: H2-04:I-0005, H2-04:A-044, H2-04:R-0128
- **within-genome-linkage.5** Annotation gaps produce apparent pathway holes: 9 of 11 amino-acid gaps in 10 genera were filled by unannotated enzymes, so predicted auxotrophies are often annotation gaps.
  conf: not stated · class: meas (marker) · holds: amino-acid biosynthesis pathway gaps in 10 bacterial genera; abstract only · src: priceFillingGapsBacterial2018 (AB; measured) · trail: H2-04 §Linkage within genomes, §answers · from: H2-04:I-0005, H2-04:A-044, H2-04:R-0121
- **within-genome-linkage.6** Horizontal transfer is 25-fold more frequent among human-associated bacteria than among ecologically diverse non-human isolates, and is structured by shared habitat.
  conf: single (marker) · class: deriv (marker) · holds: human-associated bacteria against ecologically diverse non-human isolates; abstract only; the critic: one study, used in the answers as a general caution on the overlap side · src: smillieEcologyDrivesGlobal2011 (AB; derived; single study) · trail: H2-04 §Linkage within genomes, §Adversarial critique · from: H2-04:I-0005, H2-04:C-067
- **within-genome-linkage.7** No source found quantifies contamination effects on measured within-genome linkage specifically.
  conf: not stated · class: search (note: "No source found quantifies contamination effects on linkage estimates specifically") · holds: routes as in the note's search record · src: none (a search result) · search: searched, not found (note: "No source found quantifies contamination effects on linkage estimates specifically") · trail: H2-04 §Linkage within genomes, §Provenance · from: H2-04:B-0034, H2-04:B-0017

### association-networks: co-occurrence and association networks, and what their edges indicate
needs: shared-environment
group: networks-environment

- **association-networks.bg1** Microbiome datasets generated by high-throughput sequencing (16S rRNA gene amplicons, metagenomes, metatranscriptomes) are compositional, because the instrument imposes an arbitrary total on each sample.
  kind: background · ref: gloorMicrobiomeDatasetsCompositional2017 · check: DOI 10.3389/fmicb.2017.02224 resolves on Crossref (title, authors, Front. Microbiol. 8:2224); stated in the abstract ("microbiome datasets generated by HTS are compositional because they have an arbitrary total imposed by the instrument")
- **association-networks.1** Taxon association (co-occurrence) networks are built in quantity, but benchmarks limit what their edges can indicate.
  conf: not stated · class: not stated · holds: taxon networks, not functions; the critic removed Fierer et al. 2014 from the list of network studies (a community-aggregated-traits perspective, not a network study) · src: barberanUsingNetworkAnalysis2011, faustMicrobialCooccurrenceRelationships2012, levyMetabolicModelingSpecies2013 · trail: H2-04 §Taxon networks, §answers, §critic · from: H2-04:B-0035, H2-04:A-003, H2-04:C-004
- **association-networks.2** Eight correlation tools run on the same simulated data shared on average 31.5% of edges; constraining totals produced incorrect edges for most tools, worst below an effective species number of about 13; the best precision for sparse Lotka-Volterra relations was 0.2.
  conf: repl (marker) · class: model (marker) · holds: simulated data; the critic could not retrieve the PMC XML, so these figures are unverified in the critique · src: weissCorrelationDetectionStrategies2016 (FT; modelled; replicated) · limit: access (critic: C-060) · trail: H2-04 §Taxon networks, §Adversarial critique · from: H2-04:I-0006, H2-04:C-060, H2-04:R-0131
- **association-networks.3** Closure alone can flip correlation signs; on HMP data, standard correlation was estimated to give about 3 spurious edges per true one, relative to SparCC as the reference and not relative to known truth.
  conf: not stated · class: model (marker) · holds: HMP data; SparCC as reference; abstract only · src: friedmanInferringCorrelationNetworks2012 (AB; modelled) · trail: H2-04 §Taxon networks · from: H2-04:I-0007
- **association-networks.4** Whether compositionally aware methods remove closure artefacts is a conflict: they beat other methods in their own benchmarks, but in an independent population-dynamics simulation they did no better than Pearson correlation, and recovered competition better than predator-prey relations; the conflict is not resolved.
  conf: cont (note: "That is a genuine conflict and it is not resolved") · class: not stated · holds: the methods' own benchmarks (abstract) against one independent simulation · src: kurtzSparseCompositionallyRobust2015 (AB), hiranoDifficultyInferringMicrobial2019 (FT; modelled) · trail: H2-04 §Taxon networks, §answers · from: H2-04:I-0008, H2-04:B-0036, H2-04:A-008
- **association-networks.5** Direct validation of network edges is thin: two gut species pairs from a network were co-cultured and behaved as the edges predicted (n = 2).
  conf: single (marker) · class: meas (marker) · holds: two human gut bacterial species pairs from a network, co-cultured in vitro · src: dasVitroCoculturesHuman2018 (FT; measured; single study) · trail: H2-04 §Taxon networks · from: H2-04:I-0009, H2-04:B-0037, H2-04:R-0062
- **association-networks.6** In a non-microbial rocky-intertidal system, a co-occurrence network matched an independently resolved interaction network at about chance (sensitivity 0.469, specificity 0.527).
  conf: not stated · class: meas (marker) · holds: rocky intertidal, non-microbial; abstract only; figures checked by the critic · src: freilichSpeciesCooccurrenceNetworks2018 (AB; measured; non-microbial) · trail: H2-04 §Taxon networks, §critic · from: H2-04:I-0010, H2-04:C-045
- **association-networks.7** Theoretical and review papers conclude that co-occurrence is a poor proxy for interaction (co-occurrence is not interaction).
  conf: not stated · class: assert (marker) · holds: non-microbial; abstract only · src: blanchetCooccurrenceNotEvidence2020 (AB; asserted; non-microbial) · trail: H2-04 §Taxon networks, §answers · from: H2-04:I-0011, H2-04:A-045
- **association-networks.8** Edge meaning in microbial networks is uncertain, and strategies to remove environmental edges have not been systematically compared.
  conf: not stated · class: assert (marker) · holds: a theoretical or review paper · src: faustOpenChallengesMicrobial2021 (FT; asserted) · trail: H2-04 §Taxon networks · from: H2-04:I-0011, H2-04:R-0072
- **association-networks.9** Correlation almost never gives reliable information on direct biotic interactions in real ecosystems.
  conf: not stated · class: assert (marker) · holds: a theoretical or review paper; read through a web-fetch tool summary (FT-s) · src: carrUseAbuseCorrelation2019 (closer to secondary; asserted; critic: C-053 was "FT-s; asserted") · trail: H2-04 §Taxon networks · from: H2-04:I-0011
- **association-networks.10** In macroecology, joint species distribution models cannot separate environment from interaction.
  conf: not stated · class: deriv (marker) · holds: macroecology; abstract only · src: poggiatoInterpretationsJointModeling2021 (AB; derived) · trail: H2-04 §Taxon networks · from: H2-04:I-0012
- **association-networks.11** Residual correlations of joint species distribution models depend on prevalence.
  conf: not stated · class: model (marker) · holds: macroecology; abstract only · src: zurellDoJointSpecies2018 (AB; modelled) · trail: H2-04 §Taxon networks · from: H2-04:I-0012
- **association-networks.12** Metacommunity disturbance alone can generate associations between non-interacting species.
  conf: not stated · class: model (marker) · holds: macroecology; a preprint; abstract only · src: calcagnoMetacommunityDynamicsDetection2021 (AB; modelled; preprint) · trail: H2-04 §Taxon networks · from: H2-04:I-0012
- **association-networks.13** Among taxon co-occurrence networks inferred from amplicon data, the 16S reference (taxonomy) database contributed 65.4% of the variance among inferred networks and OTU processing 26.8%; this concerns taxonomic, not functional, annotation, so it is indirect for function profiles.
  conf: single (marker) · class: meas (marker) · holds: taxon networks (16S); the annotation-artefact magnitude rests on this study alone; figures checked against full text by the critic; says nothing directly about functional annotation schemes · src: kishoreInferringMicrobialCooccurrence2023 (FT; measured; single study) · trail: H2-04 §Taxon networks, §answers, §critic · from: H2-04:I-0013, H2-04:A-023, H2-04:A-017, H2-04:C-005, H2-04:C-006, H2-04:C-045, H2-04:C-064, H2-04:R-0085
- **association-networks.14** Edge sets from Spearman, SparCC and GLASSO overlap only partly on the same soil data; citing theory, environmental filtering is expected to dominate as sampling-unit scale grows.
  conf: not stated · class: not stated · holds: soil data; a source not cited in the review's body but annotated in its reference list · src: gusevaDiversityComplexityMicrobial2022 (FT) · trail: H2-04 §Reference list · from: H2-04:R-0152, H2-04:R-0151
- **association-networks.15** Many bacterial aggregations survive a habitat-aware null model, though the authors state they cannot conclusively reject unmodelled environmental preference.
  conf: not stated · class: not stated · holds: cosmopolitan bacteria; annotated in the reference list, not cited in the body · src: pascualgarciaBacteriaDialogSanta2014 (FT) · trail: H2-04 §Reference list · from: H2-04:R-0153, H2-04:R-0151, H2-04:R-0147
- **association-networks.16** FlashWeave conditions on metadata to separate direct from indirect associations, with simulation-only evaluation.
  conf: not stated · class: not stated · holds: simulation only; annotated in the reference list, not cited in the body · src: tackmannRapidInferenceDirect2019 (AB) · trail: H2-04 §Reference list · from: H2-04:R-0155, H2-04:R-0151

### shared-environment: shared response to environment
needs: association-networks
group: networks-environment

- **shared-environment.1** Environmental heterogeneity is argued to be usually the strongest driver of correlation structure; named as such, the shared-environment source is asserted.
  conf: single (critic: C-068) · class: assert (marker) · holds: asserted; read only through a tool summary · src: carrUseAbuseCorrelation2019 (closer to secondary; asserted; single; critic: C-053, C-068 was "FT-s; asserted") · trail: H2-04 §Shared response, §answers, §critic · from: H2-04:I-0029, H2-04:I-0001, H2-04:C-007, H2-04:C-068
- **shared-environment.2** Simulation shows co-occurrence networks lose interpretability when habitat filtering is significant (modelled as destroying network interpretability).
  conf: not stated · class: model (marker) · holds: simulation; abstract only · src: berryDecipheringMicrobialInteractions2014 (AB; modelled) · trail: H2-04 §Shared response, §answers · from: H2-04:I-0029, H2-04:I-0001
- **shared-environment.3** The one quantitative partition of environmental effects found is for taxa: in a 10-year monthly marine association network of 29,820 edges, four methods classified 8.3% (the intersection of the four) to 24.8%, 25.7% and 84.6% (individual methods) of edges as environmentally driven; in simulation the individual methods removed 38 to 86% of true interactions along with environmental edges, and the intersection approach also removed 25%. It is the only quantitative environmental-share partition for microbial associations; removing it leaves only asserted statements.
  conf: single (marker) · class: meas/model (marker) · holds: taxon association edges in one 10-year monthly marine time series; relative abundances with no log-ratio treatment reported in the findings; the share is limited to measured environmental factors; figures rechecked against full text by the reviewer and by the critic · src: deutschmannDisentanglingEnvironmentalEffects2021 (FT; measured and modelled; single study) · trail: H2-04 §Shared response, §answers, §critic, §Provenance · from: H2-04:I-0030, H2-04:I-0001, H2-04:A-020, H2-04:A-026, H2-04:A-036, H2-04:A-037, H2-04:C-007, H2-04:C-011, H2-04:C-012, H2-04:C-045, H2-04:B-0014, H2-04:A-021
- **shared-environment.4** The environment-driven share of association edges is method-dependent: the methods disagree by an order of magnitude (8.3% to 84.6%), and reliability is low.
  conf: single (marker) · class: meas/model (marker) · holds: one marine time series; share limited to measured environmental factors · src: deutschmannDisentanglingEnvironmentalEffects2021 (FT; measured and modelled; single study) · trail: H2-04 §answers, §Shared response · from: H2-04:A-021, H2-04:A-030, H2-04:I-0030
- **shared-environment.5** Tara Oceans authors conclude that environment is an incomplete predictor of community structure; the numbers were not reached.
  conf: not stated · class: not stated · holds: the global plankton interactome (Tara Oceans); abstract only · src: limamendezDeterminantsCommunityStructure2015 (AB) · limit: access (note: "the numbers were not reached") · trail: H2-04 §Shared response · from: H2-04:B-0050, H2-04:R-0093
- **shared-environment.6** For functions, ocean functional groups track environment strongly while taxonomy within groups does not; the functional groups are assigned from taxonomy, so they are not independent of composition.
  conf: cont (marker) · class: deriv (marker) · holds: the global ocean microbiome; functional groups assigned from taxonomy; abstract only · src: loucaDecouplingFunctionTaxonomy2016 (AB; derived; contested) · trail: H2-04 §Shared response · from: H2-04:I-0031, H2-04:R-0097
- **shared-environment.7** Enrichment communities converge in function and in family-level taxonomy under a given carbon source.
  conf: not stated · class: meas (marker) · holds: enrichment communities; the cross-feeding mechanism modelled; abstract only · src: goldfordEmergentSimplicityMicrobial2018 (AB; measured, with the cross-feeding mechanism modelled) · trail: H2-04 §Shared response · from: H2-04:I-0032
- **shared-environment.8** A consumer-resource model reproduces survey-level patterns from shared environments.
  conf: not stated · class: model (marker) · holds: a model; abstract only · src: marslandMinimalModelMicrobial2020 (AB; modelled) · trail: H2-04 §Shared response · from: H2-04:I-0033

### gene-level-networks: networks built among functions (genes, KOs)
needs: association-networks, within-genome-linkage

- **gene-level-networks.1** GeoChip functional-gene networks in grassland soil differed between ambient and elevated CO2, and their links were interpreted as interactions among populations carrying the genes.
  conf: single (note: "the only direct work is two single studies") · class: meas (marker) · holds: grassland soil; profiles independent of any genome set; one of the two studies that build networks among functions directly; gene-level network interpretation rests on this and one preprint · src: zhouFunctionalMolecularEcological2010 (FT; measured) · rating: "Weak for gene-level (as opposed to taxon-level) covariation" · trail: H2-04 §Gene-level networks, §answers, §Adversarial critique · from: H2-04:I-0014, H2-04:B-0038, H2-04:A-006, H2-04:C-070
- **gene-level-networks.2** A KO co-occurrence network from a decade of monthly marine metagenomes found vitamin metabolism the most connected pathway.
  conf: single (note: "the only direct work is two single studies") · class: meas (marker) · holds: monthly marine metagenomes over a decade; a preprint; MAGs from the same metagenomes; read through a tool summary · src: arandiagorostidiMetagenomicbasedNetworkAnalysis2025 (closer to secondary; measured; preprint; critic: C-053 was "FT-s; measured; preprint") · rating: "Weak for gene-level (as opposed to taxon-level) covariation" · trail: H2-04 §Gene-level networks, §answers, §Adversarial critique · from: H2-04:I-0015, H2-04:B-0038, H2-04:A-006, H2-04:C-070
- **gene-level-networks.3** On the reviewer's reading, neither gene-level network study separates genes that covary because they share a genome, nor corrects for closure, nor conditions on environment; their authors conclude interaction, which the reviewer cannot confirm from the reported analyses.
  conf: not stated · class: reading (note: "Reviewer's reading") · holds: the GeoChip and KO networks · src: zhouFunctionalMolecularEcological2010 (full text), arandiagorostidiMetagenomicbasedNetworkAnalysis2025 (closer to secondary; critic: C-053 was "full text via fetch summary") · trail: H2-04 §Gene-level networks, §answers · from: H2-04:B-0039, H2-04:B-0040, H2-04:A-003
- **gene-level-networks.4** Gene-level (gene or KO) co-occurrence networks controlling for within-genome linkage were not found.
  conf: not stated · class: search (note: "Gene-level networks controlling for within-genome linkage were not found") · holds: routes: Europe PMC REST keyword searches, Crossref, OpenAlex, PMC full text, three independent search angles; WebSearch and Scholar Gateway unavailable · src: none (a search result) · search: searched, not found (note: "Gene-level networks controlling for within-genome linkage were not found") · trail: H2-04 §answers, §Provenance · from: H2-04:A-010, H2-04:A-011, H2-04:B-0017

### shared-ancestry: shared ancestry (phylogeny) of the organisms carrying functions
needs: association-networks

- **shared-ancestry.1** Phylogeny is the largest single predictor of pairwise co-occurrence among the indices tested.
  conf: single (critic: C-065) · class: not stated · holds: one study, which reuses Levy & Borenstein's gut data and tested only four genomic indices · src: kamnevaGenomeCompositionPhylogeny2017 (FT; single; critic: C-065 was "FT") · trail: H2-04 §Shared ancestry, §answers, §Adversarial critique, §Reference list · from: H2-04:B-0051, H2-04:A-004, H2-04:C-065, H2-04:R-0156
- **shared-ancestry.2** Co-occurring and positively associated taxa are phylogenetically close and functionally similar.
  conf: not stated · class: not stated · holds: taxa · src: chaffronGlobalNetworkCoexisting2010 (FT), faustMicrobialCooccurrenceRelationships2012 (FT) · trail: H2-04 §Shared ancestry, §answers · from: H2-04:B-0051, H2-04:A-004
- **shared-ancestry.3** At the community level, distance on the first two genomic trait axes correlated with UniFrac distance (R2 = 0.32; 0.46 below median genome size, 0.15 above).
  conf: not stated · class: not stated · holds: community-level genomic trait axes from 128 soil metagenomes; the critic could not recheck R2 = 0.32 (open copies returned HTML) · src: pitonLifeHistoryStrategies2023 (FT) · limit: access (critic: C-058) · trail: H2-04 §Shared ancestry, §answers, §Adversarial critique · from: H2-04:B-0052, H2-04:A-004, H2-04:C-058, H2-04:I-0038
- **shared-ancestry.4** All 11 genomic traits across about 18,000 genomes carry phylogenetic signal.
  conf: not stated · class: not stated · holds: about 18,000 prokaryote genomes; abstract only · src: beierTraittraitRelationshipsTradeoffs2022 (AB) · trail: H2-04 §Shared ancestry · from: H2-04:B-0053, H2-04:R-0048

### aggregation-artefacts: artefacts of aggregating unit-level values into community profiles
needs: none

- **aggregation-artefacts.bg1** A community-aggregated trait value is the species' trait values weighted according to the relative abundance of the species in the community.
  kind: background · ref: garnierPlantFunctionalMarkers2004 · check: DOI 10.1890/03-0799 resolves on Crossref (Ecology 85(9):2630-2637); stated in the abstract ("community-aggregated (i.e., weighed according to the relative abundance of species) functional leaf traits")
- **aggregation-artefacts.1** Community means of randomly assigned species attributes correlate with each other and with richness through repeated co-occurrence alone, with variance explained rising with co-occurrence: aggregation of unit-level values produces correlations among community means.
  conf: not stated · class: model (marker) · holds: trait ecology, non-microbial; abstract only · src: hawkinsStructuralBiasAggregated2017 (AB; modelled; non-microbial) · trail: H2-04 §Artefacts of aggregation, §answers · from: H2-04:I-0034, H2-04:B-0055, H2-04:I-0002
- **aggregation-artefacts.2** Standard tests of community-weighted mean versus environment have inflated Type I error that rises as beta diversity falls.
  conf: not stated · class: model (marker) · holds: trait ecology; abstract only, via a bioRxiv preprint abstract · src: zelenyWhichResultsStandard2018 (AB; modelled) · trail: H2-04 §Artefacts of aggregation · from: H2-04:I-0035, H2-04:R-0143, H2-04:B-0055
- **aggregation-artefacts.3** The fourth-corner approach is proposed as a remedy for community-weighted mean tests.
  conf: not stated · class: not stated · holds: trait ecology; abstract only · src: peresnetoLinkingTraitVariation2017 (AB) · trail: H2-04 §Artefacts of aggregation · from: H2-04:I-0035, H2-04:B-0055
- **aggregation-artefacts.4** Abundance-weighted versus species-weighted aggregation changed the sign of 27% of significant trait-climate results.
  conf: single (marker) · class: meas (marker) · holds: trait ecology (trait-climate results); abstract only; the figure checked against the abstract by the critic · src: wieczynskiClimateShapesShifts2018 (AB; measured; single study) · trail: H2-04 §Artefacts of aggregation, §answers, §critic · from: H2-04:I-0036, H2-04:I-0002, H2-04:C-045
- **aggregation-artefacts.5** In metagenomes, inter-trait relations among community traits have been proposed as indicators of processing artefacts.
  conf: not stated · class: not stated · holds: microbial metagenomes; abstract only · src: barberanExplorationCommunityTraits2011 (AB) · trail: H2-04 §Artefacts of aggregation · from: H2-04:B-0056
- **aggregation-artefacts.6** Annotation coverage differs systematically between metagenome sample groups, with more unannotated genes in bare desert soils.
  conf: not stated · class: not stated · holds: soil communities in an arid ecosystem, including bare desert soils; abstract only · src: chenLifehistoryStrategiesSoil2020 (AB) · trail: H2-04 §Artefacts of aggregation · from: H2-04:B-0056, H2-04:R-0058
- **aggregation-artefacts.7** No microbial study found tests the Hawkins-type aggregation artefact on functional profiles.
  conf: not stated · class: search (note: "No microbial study found tests the Hawkins-type aggregation artefact") · holds: routes in the note's search record · src: none (a search result) · search: searched, not found (note: "No microbial study found tests the Hawkins-type aggregation artefact") · trail: H2-04 §Artefacts of aggregation · from: H2-04:B-0057

### complementarity-overlap: complementarity versus functional overlap (redundancy) among co-occurring organisms
needs: association-networks, shared-ancestry, within-genome-linkage

- **complementarity-overlap.1** Co-occurring 16S lineages mapped to complete genomes had more similar pathway content and genome size than random pairs, beyond phylogeny; the authors read this as competition or habitat sharing rather than cooperation.
  conf: not stated · class: deriv (marker) · holds: profiles independent of genomes; the critic: 'beyond phylogeny' is not stated in the abstract and the full text could not be reached, so it is unverified, and the review took it at face value · src: chaffronGlobalNetworkCoexisting2010 (FT; derived) · limit: access (critic: C-056) · contrary: one-sided (critic: C-100) · trail: H2-04 §Complementarity versus overlap, §answers, §Adversarial critique · from: H2-04:I-0016, H2-04:A-040, H2-04:C-051, H2-04:C-056, H2-04:C-100
- **complementarity-overlap.2** In HMP data, positive associations were enriched for phylogenetic and functional similarity, and negative ones for the inverse (dissimilarity).
  conf: not stated · class: deriv (marker) · holds: Human Microbiome Project data · src: faustMicrobialCooccurrenceRelationships2012 (FT; derived) · trail: H2-04 §Complementarity versus overlap, §answers · from: H2-04:I-0017, H2-04:A-040
- **complementarity-overlap.3** Across 154 gut species, co-occurrence correlated with modelled metabolic competition (rho = 0.211) and negatively with modelled complementarity (rho = -0.193); the effects are weak.
  conf: not stated · class: model (marker) · holds: 154 gut species of the human microbiome; profiles mapped to the same reference genomes; read through a tool summary; the critic could not recheck the rho values (PMC text not retrievable) · src: levyMetabolicModelingSpecies2013 (closer to secondary; modelled; critic: C-053 was "FT-s; modelled") · limit: access (critic: C-063) · trail: H2-04 §Complementarity versus overlap, §answers, §Adversarial critique · from: H2-04:I-0018, H2-04:A-040, H2-04:C-063, H2-04:R-0092
- **complementarity-overlap.4** A reanalysis of the same gut data found phylogeny alone explained 9.84% of pairwise co-occurrence variance and all genomic indices together about 3.81% more; in its combined model both metabolic competition (coefficient -0.013, p = 0.71) and metabolic complementarity (p = 0.14) were non-significant once phylogeny and genome content similarity were included.
  conf: not stated · class: deriv (marker) · holds: Levy & Borenstein's gut data, so not independent of that study; four genomic indices; figures checked against full text by the critic · src: kamnevaGenomeCompositionPhylogeny2017 (FT; derived; not independent of 17) · trail: H2-04 §Complementarity versus overlap, §critic, §Adversarial critique, §Stage 2 check, §Reference list · from: H2-04:I-0019, H2-04:A-048, H2-04:C-013, H2-04:C-065, H2-04:C-019, H2-04:C-045, H2-04:C-093, H2-04:C-094, H2-04:B-0024, H2-04:R-0156
- **complementarity-overlap.5** So the only reanalysis undercuts Levy & Borenstein's modelled competition (overlap) signal as well as its complementarity signal, which weakens the overlap side; the review reported only the complementarity half.
  conf: not stated · class: not stated · holds: the gut data of Levy & Borenstein and its reanalysis by Kamneva · src: kamnevaGenomeCompositionPhylogeny2017 (FT), levyMetabolicModelingSpecies2013 (closer to secondary; critic: C-053 was "FT-s") · contrary: one-sided (critic: C-095) · trail: H2-04 §critic, §Adversarial critique · from: H2-04:C-020, H2-04:C-021, H2-04:C-046, H2-04:C-095, H2-04:I-0018
- **complementarity-overlap.6** Human microbiome samples had higher functional redundancy than random draws from the body-site species pool; this measures within-sample redundancy against a species-pool null, not pairwise co-occurrence, and is a separate case from the co-occurrence and genome-similarity studies.
  conf: not stated · class: deriv (marker) · holds: human microbiome body sites; profiles computed from the same reference genomes, with a reference-free replication; the species-pool null checked by the critic · src: tianDecipheringFunctionalRedundancy2020 (FT; derived) · trail: H2-04 §Complementarity versus overlap, §answers, §critic, §Adversarial critique · from: H2-04:I-0020, H2-04:A-040, H2-04:C-022, H2-04:C-045, H2-04:C-099, H2-04:C-105
- **complementarity-overlap.7** At the level of small co-occurring groups (pairs to quadruplets, more than 800 communities), modelled resource overlap was barely distinguishable from random while modelled metabolic interaction potential was elevated.
  conf: not stated · class: model (marker) · holds: modelled; more than 800 communities; the figures read only through a tool summary · src: zelezniakMetabolicDependenciesDrive2015 (closer to secondary; modelled; critic: C-053 was "FT-s; modelled") · limit: access (critic: C-023) · trail: H2-04 §Complementarity versus overlap, §answers, §critic · from: H2-04:I-0021, H2-04:A-041, H2-04:C-023
- **complementarity-overlap.8** Co-occurring groups of up to 40 species polarised into cooperative groups (small genomes, auxotrophies) and competitive groups (large genomes, overlapping requirements, mainly soils); the authors attribute the difference from Levy & Borenstein to scale. The study reanalyses the Chaffron 16S collection.
  conf: not stated · class: model (marker) · holds: modelled; groups of up to 40 species · src: machadoPolarizationMicrobialCommunities2021 (FT; modelled) · trail: H2-04 §Complementarity versus overlap, §answers, §Reference list · from: H2-04:I-0022, H2-04:A-041, H2-04:R-0157
- **complementarity-overlap.9** Complementarity among small co-occurring groups rests on one method family: Zelezniak 2015 and Machado 2021 share authors and framework (SMETANA) and count as one line of evidence; removing these Patil group papers would remove nearly all support for complementarity among co-occurring organisms in natural surveys.
  conf: single (critic: C-023) · class: model (marker) · holds: modelled small-group analyses; the Zelezniak figures read only through a tool summary · src: zelezniakMetabolicDependenciesDrive2015 (closer to secondary; modelled; critic: C-053 was "FT-s; modelled"), machadoPolarizationMicrobialCommunities2021 (FT; modelled) · rating: "Weak for complementarity at the small-group scale" · trail: H2-04 §Complementarity versus overlap, §answers, §critic, §Adversarial critique, §Reference list · from: H2-04:B-0044, H2-04:A-047, H2-04:A-055, H2-04:C-023, H2-04:C-055, H2-04:R-0157, H2-04:I-0021, H2-04:I-0022
- **complementarity-overlap.10** Pairwise metabolic models predict that cooperative potential peaks at moderate overlap.
  conf: not stated · class: model (marker) · holds: modelled; abstract only · src: freilichCompetitiveCooperativeMetabolic2011 (AB; modelled) · trail: H2-04 §Complementarity versus overlap · from: H2-04:I-0023
- **complementarity-overlap.11** Costless metabolic secretions create broad cross-feeding opportunities.
  conf: not stated · class: model (marker) · holds: modelled; abstract only · src: pachecoCostlessMetabolicSecretions2019 (AB; modelled) · trail: H2-04 §Complementarity versus overlap · from: H2-04:I-0023
- **complementarity-overlap.12** The Black Queen hypothesis predicts complementary gene content for leaky functions.
  conf: not stated · class: assert (marker) · holds: a hypothesis; abstract only · src: morrisBlackQueenHypothesis2012 (AB; asserted) · trail: H2-04 §Complementarity versus overlap · from: H2-04:I-0024
- **complementarity-overlap.13** Among 20 soil isolates in 40 carbon environments, overlap in carbon use predicted competition (68% for the most similar non-identical pairs) and difference predicted facilitation (Spearman 0.75).
  conf: not stated · class: meas (marker) · holds: in vitro, no community profiles; bears on mechanism, not on covariation across samples; figures checked against full text by the critic · src: kehePositiveInteractionsCommon2021 (FT; measured; in vitro, no community profiles) · trail: H2-04 §Complementarity versus overlap, §answers, §critic · from: H2-04:I-0025, H2-04:A-043, H2-04:B-0046, H2-04:C-024, H2-04:C-045
- **complementarity-overlap.14** Antagonism rose with metabolic similarity, with a small effect (pseudo-R2 0.015 to 0.032).
  conf: not stated · class: meas (marker) · holds: in vitro bacteria, no community profiles; read through a tool summary · src: russelAntagonismCorrelatesMetabolic2017 (closer to secondary; measured; critic: C-053 was "FT-s; measured") · trail: H2-04 §Complementarity versus overlap, §answers · from: H2-04:I-0026, H2-04:A-043, H2-04:B-0046, H2-04:R-0127
- **complementarity-overlap.15** Among tree-hole isolates, most pairwise interactions were net negative (competition dominates).
  conf: not stated · class: meas (marker) · holds: culturable tree-hole isolates in a single environment; in vitro; abstract only · src: fosterCompetitionNotCooperation2012 (AB; measured; single environment) · trail: H2-04 §Complementarity versus overlap, §answers · from: H2-04:I-0027, H2-04:A-043, H2-04:B-0046, H2-04:R-0075
- **complementarity-overlap.16** In vitro results conflict: Kehe 2021 finds positive interactions common, while Foster & Bell 2012 find competition dominant (in a single environment).
  conf: cont (note: "Conflicts:") · class: meas (marker) · holds: in vitro isolates; Foster & Bell in a single environment · src: kehePositiveInteractionsCommon2021 (FT; measured), fosterCompetitionNotCooperation2012 (AB; measured; single environment) · trail: H2-04 §answers · from: H2-04:A-050, H2-04:A-049, H2-04:I-0025, H2-04:I-0027
- **complementarity-overlap.17** Whether co-occurrence tracks complementarity is in conflict between Levy & Borenstein 2013 and Zelezniak 2015 with Machado 2021; Machado attributes the difference to scale.
  conf: cont (note: "Conflicts: Levy & Borenstein 2013 versus Zelezniak 2015 and Machado 2021") · class: model (marker) · holds: whole-community gut analysis against small-group analyses · src: levyMetabolicModelingSpecies2013 (closer to secondary; modelled; critic: C-053 was "FT-s; modelled"), zelezniakMetabolicDependenciesDrive2015 (closer to secondary; modelled; critic: C-053 was "FT-s; modelled"), machadoPolarizationMicrobialCommunities2021 (FT; modelled) · trail: H2-04 §answers, §Complementarity versus overlap · from: H2-04:A-049, H2-04:I-0018, H2-04:I-0021, H2-04:I-0022, H2-04:A-040, H2-04:A-041
- **complementarity-overlap.18** The complementarity readings rest on genome-derived auxotrophies, whose sensitivity against 36 strains with known auxotrophies was 75.5% (gapseq) and 43.4% (AGORA2) and falls with genome incompleteness, and on annotation gaps.
  conf: not stated · class: model (marker) · holds: 36 strains with known auxotrophies; modelled with measured validation · src: starkeAminoAcidAuxotrophies2023 (FT; modelled with measured validation), priceFillingGapsBacterial2018 · trail: H2-04 §Complementarity versus overlap, §answers · from: H2-04:I-0028, H2-04:A-044
- **complementarity-overlap.19** Cautions apply to both sides: the overlap readings rest on co-occurrence inference, which carries the network artefacts and is method-dependent (31.5% shared edges) and poorly validated; the complementarity side's auxotrophy caution is quantified (43.4 to 75.5% sensitivity), but no equivalent error rate is applied to the co-occurrence side when the strength ratings are set; both sides mostly analyse only taxa mappable to reference genomes.
  conf: not stated · class: not stated · holds: both sides of the complementarity-overlap question · src: none (the reviewer's synthesis and the critic's finding) · contrary: one-sided (critic: C-098) · trail: H2-04 §Complementarity versus overlap, §critic, §Adversarial critique · from: H2-04:B-0047, H2-04:B-0048, H2-04:B-0049, H2-04:C-026, H2-04:C-096, H2-04:C-097, H2-04:C-098
- **complementarity-overlap.20** The evidence on complementarity versus overlap splits by scale and by evidence class: at whole-community scale, co-occurrence is associated with genome similarity (overlap), with weak effects; modelled small-group analyses find complementarity.
  conf: not stated · class: deriv/model (note: "Derived and modelled whole-community analyses find overlap") · holds: whole-community co-occurrence (Chaffron from its abstract, Faust, Kamneva's genome-content similarity index) against modelled small groups; both sides depend on co-occurrence inference · src: chaffronGlobalNetworkCoexisting2010 (abstract), faustMicrobialCooccurrenceRelationships2012, kamnevaGenomeCompositionPhylogeny2017 · rating: "Moderate for the pattern that whole-community co-occurrence associates with overlap" (critic: C-025: weak to moderate for overlap, weak for complementarity) · contrary: one-sided (critic: C-096) · trail: H2-04 §answers, §critic, §Complementarity versus overlap · from: H2-04:A-039, H2-04:A-040, H2-04:A-041, H2-04:A-046, H2-04:B-0041, H2-04:B-0042, H2-04:B-0043, H2-04:C-017, H2-04:C-018, H2-04:C-025, H2-04:C-096, H2-04:C-026
- **complementarity-overlap.21** Removing Chaffron et al. 2010 would leave the overlap pattern supported by Faust 2012, Levy & Borenstein 2013 and Tian 2020.
  conf: not stated · class: not stated · holds: the review's single-source sensitivity; the critic: Tian measures within-sample redundancy against a species-pool null, which lowers the bar for replication on the overlap side · src: faustMicrobialCooccurrenceRelationships2012, levyMetabolicModelingSpecies2013, tianDecipheringFunctionalRedundancy2020 · trail: H2-04 §answers, §Adversarial critique · from: H2-04:A-054, H2-04:C-099
- **complementarity-overlap.22** Not measured: complementarity or overlap measured with community profiles built independently of the genomes analysed and at the gene level; validation of any network edge against measured interactions beyond two species pairs (Das 2018).
  conf: not stated · class: search (note: "Routes as in case (a)") · holds: routes as for the sources of covariation (Europe PMC REST keyword searches, Crossref, OpenAlex, PMC full text, three search angles) · src: dasVitroCoculturesHuman2018 (full text) · search: searched, not found (note: "Routes as in case (a)") · trail: H2-04 §answers · from: H2-04:A-051, H2-04:A-052, H2-04:A-011
- **complementarity-overlap.23** Cautions on the overlap side: co-occurrence is not interaction, and horizontal transfer is concentrated among co-habitants, which can generate shared gene content without shared ancestry.
  conf: not stated · class: not stated · holds: the horizontal-transfer caution rests on one abstract (Smillie 2011) used as a general caution · src: blanchetCooccurrenceNotEvidence2020 (abstract), carrUseAbuseCorrelation2019, smillieEcologyDrivesGlobal2011 (abstract) · trail: H2-04 §answers, §Adversarial critique · from: H2-04:A-045, H2-04:C-067

### covariation-sources: the sources of covariation among functions across community samples
needs: within-genome-linkage, association-networks, shared-environment, shared-ancestry, aggregation-artefacts

- **covariation-sources.1** Two functions can rise and fall together across community samples because they sit in the same genomes, because different organisms carrying them co-occur, because both respond to the same environmental gradient, because their carriers share ancestry, or because the covariation is manufactured by closure, normalisation, annotation or aggregation. Each of the five sources is named in the literature, by largely separate communities, and almost always for taxa, not for function-by-sample tables.
  conf: not stated · class: not stated · holds: identified mostly for taxa; existence at the taxon level, weak or indirect at the function level · src: none (the reviewer's synthesis of the sources below) · rating: "Moderate for the existence of each source" (critic: C-008: moderate for existence at the taxon level, weak or indirect at the function level) · trail: H2-04 §What the question contains, §answers, §critic · from: H2-04:B-0025, H2-04:B-0026, H2-04:A-001, H2-04:A-005, H2-04:C-001, H2-04:C-002, H2-04:C-008
- **covariation-sources.2** The existence of closure, method dependence and shared ancestry as sources of covariation is replicated across independent groups, at the taxon level.
  conf: repl (note: "replicated across independent groups for closure, method dependence, shared ancestry and environment") · class: not stated · holds: taxon-level work; the critic narrows the standing to existence at the taxon level · src: none (the reviewer's synthesis of the sources below) · rating: "Moderate for the existence of each source" (critic: C-008: moderate for existence at the taxon level, weak or indirect at the function level) · trail: H2-04 §answers, §critic · from: H2-04:A-005, H2-04:C-008
- **covariation-sources.3** The shared-environment source is asserted (Carr 2019, read only through a tool summary) plus one taxon-level measured partition (Deutschmann 2021): much of the environment argument is asserted (perspectives) rather than measured.
  conf: single (critic: C-007) · class: assert (note: "Much of the environment argument is asserted (perspectives) rather than measured") · holds: taxon-level · src: carrUseAbuseCorrelation2019 (closer to secondary; asserted; critic: C-053 was "FT-s; asserted"), deutschmannDisentanglingEnvironmentalEffects2021 (FT; measured and modelled; single study) · trail: H2-04 §critic, §answers · from: H2-04:C-007, H2-04:A-007, H2-04:I-0029, H2-04:I-0030
- **covariation-sources.4** The existence claims for the sources survive the removal of any one source.
  conf: not stated · class: not stated · holds: the review's single-source sensitivity · src: none (the reviewer's sensitivity check) · trail: H2-04 §answers · from: H2-04:A-016
- **covariation-sources.5** The artefact sources named are compositional closure, method disagreement (31.5% shared edges), annotation reference choice (65.4% of network variance, for the 16S taxonomy database in taxon networks), weighting choices (27% of sign changes in trait ecology), and aggregation of unit-level values that produces correlations among community means through repeated co-occurrence alone (modelled).
  conf: not stated · class: not stated · holds: taxon networks and trait ecology; the 65.4% is indirect for function profiles · src: friedmanInferringCorrelationNetworks2012 (abstract), weissCorrelationDetectionStrategies2016 (full text), kishoreInferringMicrobialCooccurrence2023 (full text), wieczynskiClimateShapesShifts2018 (abstract), hawkinsStructuralBiasAggregated2017 (abstract, modelled) · trail: H2-04 §answers, §critic · from: H2-04:I-0002, H2-04:C-005, H2-04:C-006
- **covariation-sources.6** No study found names all five sources for the same function-by-sample table.
  conf: not stated · class: search (note: "No study found that names all five sources for the same function-by-sample table") · holds: routes: Europe PMC REST keyword searches, Crossref, OpenAlex, PMC full text, three independent search angles (complementarity, co-occurrence, trait ecology); WebSearch and Scholar Gateway unavailable · src: none (a search result) · search: searched, not found (note: "No study found that names all five sources for the same function-by-sample table") · trail: H2-04 §answers, §Adversarial critique · from: H2-04:A-009, H2-04:A-011, H2-04:C-113
- **covariation-sources.7** On the reviewer's reading, microbial work has characterised each covariation source separately, and for taxa; the functional-profile question has been approached from two sides that do not meet: gene-level networks that do not separate sources, and genome-mapped co-occurrence studies that relate pairwise genome similarity to co-occurrence but do not partition covariance among functions.
  conf: not stated · class: reading (critic: C-109) · holds: the review's synthesis argument, unlabelled in the review as the reviewer's reading · src: none (the reviewer's synthesis) · trail: H2-04 §How the cases relate, §Adversarial critique · from: H2-04:B-0073, H2-04:B-0074, H2-04:C-109

### trait-partitions: within-unit versus between-unit partitions in trait ecology (non-microbial)
needs: none

- **trait-partitions.1** The only measured covariance partitions found are within-unit versus between-unit partitions in trait ecology (plants, non-microbial).
  conf: not stated · class: search (note: "These are the only measured covariance partitions found") · holds: non-microbial; species traits, not gene content · src: none (a search result) · search: searched, not found (note: "These are the only measured covariance partitions found") · trail: H2-04 §Within-unit versus between-unit · from: H2-04:B-0058, H2-04:A-029, H2-04:C-014, H2-04:B-0059
- **trait-partitions.2** In California woody plants, the among-community (beta) components of four traits covaried strongly along a moisture gradient while the within-community (alpha) components were largely uncorrelated.
  conf: not stated · class: not stated · holds: California woody plants, non-microbial; species traits; abstract only · src: ackerlyTraitbasedApproachCommunity2007 (AB) · trail: H2-04 §Within-unit versus between-unit, §answers, §critic · from: H2-04:B-0059, H2-04:A-024, H2-04:C-014, H2-04:C-038
- **trait-partitions.3** In Alberta grasslands (76 species, 27 communities), 92 to 98% of trait variance was within communities; SLA and specific root length correlated positively within communities and negatively among communities (a sign reversal between the two components); phylogenetic signal was present in nearly all within-community trait components and none of the among-community components; correlations among species means are driven by the within-community component.
  conf: single (note: "Single-source sensitivity: Yes") · class: not stated · holds: Alberta grasslands, non-microbial; species traits; rechecked against full text by the reviewer and checked by the critic; removing it would remove the only full-text among-versus-within-community sign reversal · src: kembelIndependentEvolutionLeaf2011 (FT) · trail: H2-04 §Within-unit versus between-unit, §Shared ancestry, §answers, §critic, §Provenance · from: H2-04:B-0060, H2-04:B-0054, H2-04:A-024, H2-04:A-031, H2-04:A-036, H2-04:A-038, H2-04:A-073, H2-04:A-083, H2-04:C-014, H2-04:C-038, H2-04:C-045, H2-04:B-0014
- **trait-partitions.4** In plants, Ackerly & Cornwell find among-community covariation dominant while Kembel & Cahill find correlations among species means driven by the within-community component; these are different systems and are not contradictory in the strict sense.
  conf: not stated · class: not stated · holds: California woody plants against Alberta grasslands · src: ackerlyTraitbasedApproachCommunity2007 (abstract), kembelIndependentEvolutionLeaf2011 (full text) · trail: H2-04 §answers · from: H2-04:A-031, H2-04:B-0059, H2-04:B-0060
- **trait-partitions.5** Along a 705-species Australian transect, leaf traits varied almost independently among species but shifted jointly across sites with temperature, vapour pressure deficit and pH; within-species contributions to geographic variation were under 10% for leaf area and over 90% for chi.
  conf: not stated · class: not stated · holds: Australian transect, 705 species; abstract only; the critic: about trait-environment responses, not axis reversal · src: dongComponentsLeaftraitVariation2020 (AB) · trail: H2-04 §Within-unit versus between-unit, §answers, §critic · from: H2-04:B-0061, H2-04:A-073, H2-04:C-040, H2-04:C-102
- **trait-partitions.6** Plot-level LMA and LDMC showed virtually no variance despite high species turnover.
  conf: not stated · class: not stated · holds: plants; abstract only · src: messierHowDoTraits2010 (AB) · trail: H2-04 §Within-unit versus between-unit · from: H2-04:B-0062
- **trait-partitions.7** Intraspecific variation made up 25% of within-community and 32% of among-community trait variance on average across 629 plant communities; this is a variance partition, not a covariance partition, and a within-species versus between-species partition, which differs from the within-community versus among-community partitions.
  conf: not stated · class: not stated · holds: 629 plant communities; abstract only; figures checked by the critic · src: siefertGlobalMetaanalysisRelative2015 (AB; variance, not covariance) · trail: H2-04 §Within-unit versus between-unit, §answers, §critic · from: H2-04:B-0063, H2-04:A-025, H2-04:C-015, H2-04:C-045, H2-04:C-107
- **trait-partitions.8** Frameworks for these partitions include T-statistics and HMSC joint models.
  conf: not stated · class: not stated · holds: trait ecology; abstract only · src: violleReturnVarianceIntraspecific2012 (AB), ovaskainenHowMakeMore2017 (AB) · trail: H2-04 §Within-unit versus between-unit · from: H2-04:I-0037
- **trait-partitions.9** A scale-dependent trade-off framework holds that within-species constraints often do not apply across species, and vice versa.
  conf: not stated · class: assert (marker) · holds: a framework for organismal biology; abstract only · src: agrawalScaledependentFrameworkTradeoffs2020 (AB; asserted) · trail: H2-04 §Within-unit versus between-unit · from: H2-04:I-0037, H2-04:R-0047
- **trait-partitions.10** The plant partitions are measured and partly replicated but concern species traits, not gene content.
  conf: not stated · class: meas (note: "The plant partitions are measured and partly replicated") · holds: plants, non-microbial · src: ackerlyTraitbasedApproachCommunity2007 (abstract), kembelIndependentEvolutionLeaf2011 (full text) · trail: H2-04 §answers, §critic · from: H2-04:A-029, H2-04:C-014

### covariation-partition: partitions of covariation among the sources, with shares and reliability
needs: covariation-sources, trait-partitions

- **covariation-partition.1** No study found partitions covariation among functions in community profiles into within-genome linkage, organism co-occurrence, shared environment, shared ancestry and artefact shares; the partitions that exist are of other quantities.
  conf: not stated · class: search (note: "No study found partitions covariation among functions in community profiles") · holds: metagenomic or genome-derived community profiles; routes as for the sources, plus Europe PMC queries on community-aggregated traits with covariation and trade-off terms and on strain-level versus taxonomic turnover; the critic: the headline absence is stated with appropriate restraint · src: none (a search result) · rating: "Weak" (critic: C-009: Supported) · search: searched, not found (note: "No study found partitions covariation among functions in community profiles") · trail: H2-04 §answers, §critic, §Provenance · from: H2-04:A-018, H2-04:A-019, H2-04:A-027, H2-04:A-033, H2-04:C-009, H2-04:C-010, H2-04:C-044, H2-04:B-0017, H2-04:A-032
- **covariation-partition.2** For pairwise co-occurrence of gut taxa, phylogeny explains 9.84% and genomic indices add about 3.81%, so most variance is unexplained; the analysis used Jaccard presence data.
  conf: not stated · class: deriv (marker) · holds: gut taxa (Levy & Borenstein's data); Jaccard presence data · src: kamnevaGenomeCompositionPhylogeny2017 (FT; derived; not independent of 17) · trail: H2-04 §answers, §critic · from: H2-04:A-022, H2-04:A-026, H2-04:C-013, H2-04:I-0019, H2-04:R-0156
- **covariation-partition.3** Handling of turnover, closure and depth in the partitions that exist: Deutschmann used relative abundances with no log-ratio treatment reported in the findings; Kamneva used Jaccard presence data; Piton normalised by annotated reads and log(x+1), with no log-ratio treatment and 5 to 15% of reads annotated.
  conf: not stated · class: not stated · holds: the three microbial studies; the critic could not recheck Piton's 5 to 15% figure (open copies returned HTML) · src: deutschmannDisentanglingEnvironmentalEffects2021, kamnevaGenomeCompositionPhylogeny2017, pitonLifeHistoryStrategies2023 · limit: access (critic: C-058) · trail: H2-04 §answers, §Adversarial critique · from: H2-04:A-026, H2-04:C-058
- **covariation-partition.4** Every microbial partition is a single study with its own (different) denominator, so the shares cannot be pooled.
  conf: single (note: "Every microbial partition is a single study with a different denominator") · class: not stated · holds: the Deutschmann, Kamneva and Kishore partitions · src: deutschmannDisentanglingEnvironmentalEffects2021, kamnevaGenomeCompositionPhylogeny2017, kishoreInferringMicrobialCooccurrence2023 · rating: "Weak" · trail: H2-04 §answers, §critic · from: H2-04:A-027, H2-04:A-028, H2-04:C-016, H2-04:A-020, H2-04:A-022, H2-04:A-023
- **covariation-partition.5** Not measured: any partition of function-by-function covariance in metagenomic or genome-derived community profiles, and any microbial analogue of the Leps-type turnover versus within-taxon decomposition (Leps et al. 2011 itself not obtained).
  conf: not stated · class: search (note: "also Europe PMC queries on community-aggregated traits with covariation and trade-off terms") · holds: routes as for the sources, plus Europe PMC queries on community-aggregated traits with covariation and trade-off terms, and on strain-level versus taxonomic turnover · src: lepsCommunityTraitResponse2011 (not obtained) · search: searched, not found (note: "also Europe PMC queries on community-aggregated traits with covariation and trade-off terms") · trail: H2-04 §answers, §Provenance · from: H2-04:A-032, H2-04:A-033, H2-04:B-0017
- **covariation-partition.6** On the reviewer's reading, trait ecology has the partitioning machinery and shows that within-unit and between-unit covariation can differ in sign and in cause; it has not been applied to metagenomic function in any study found.
  conf: not stated · class: reading (critic: C-109) · holds: trait ecology; metagenomic function · src: none (the reviewer's synthesis) · trail: H2-04 §How the cases relate · from: H2-04:B-0075, H2-04:C-109

### genome-community-axes: genome-level versus community-level functional axes (microbial)
needs: aggregation-artefacts

- **genome-community-axes.1** No study found compares the main axes of functional variation among genomes with those among community profiles using a formal agreement measure (eigenvector angle, Procrustes, congruence coefficient); so no conflicts were found, because no quantitative comparison exists. Not measured: every microbial habitat for a formal axis comparison, and comparisons where community profiles are built from the same genomes versus measured independently.
  conf: not stated · class: search (note: "No study found compares the main axes of functional variation among genomes with those among community profiles") · holds: microbial systems; routes: Europe PMC queries on community-aggregated traits, metagenome trait axes and genome-level trait trade-offs, citation follow-up from Piton 2023 and Westoby 2021, three independent search angles; the critic: the headline absence is stated with appropriate restraint · src: none (a search result) · rating: "Absent as direct evidence" (critic: C-027: Supported) · search: searched, not found (note: "No study found compares the main axes of functional variation among genomes with those among community profiles") · trail: H2-04 §answers, §Genome-level versus community-level, §critic, §Provenance · from: H2-04:A-056, H2-04:A-063, H2-04:A-065, H2-04:A-067, H2-04:A-068, H2-04:B-0064, H2-04:C-027, H2-04:C-028, H2-04:C-034, H2-04:C-044, H2-04:B-0017
- **genome-community-axes.2** The nearest precedent: across 128 soil metagenomes, the first two co-inertia axes captured 29% and 21% of community genomic trait variation, the first running from streamlined to large, metabolically expanded genomes (average genome size R2 = 0.64); the authors say this is consistent with isolate-based trait axes without testing it (the abstract says the two dimensions 'support previous theoretical and isolate-based studies'), and state that community-aggregated patterns 'do not directly inform on the within-organism tradeoffs'. Removing this study leaves only the Gralka enrichment-community comparison as a microbial precedent.
  conf: single (marker) · class: meas (marker) · holds: 128 soil metagenomes; profiles metagenomic and independent of the isolate genomes; read-based annotation of 5 to 15% of reads; no log-ratio treatment; the critic could not recheck the figures (open copies returned HTML; the abstract confirms only the qualitative claim) · src: pitonLifeHistoryStrategies2023 (FT; measured; single study) · limit: access (critic: C-058) · trail: H2-04 §answers, §Genome-level versus community-level, §critic, §Adversarial critique · from: H2-04:I-0038, H2-04:A-057, H2-04:A-058, H2-04:A-070, H2-04:B-0019, H2-04:C-029, H2-04:C-030, H2-04:C-057, H2-04:C-058, H2-04:C-059
- **genome-community-axes.3** The same paper asserts that community-average rRNA copy number varies less than isolate values, a compression that would change loadings between levels; this and the authors' own caveat cut against reading the qualitative agreement as axis identity.
  conf: not stated · class: assert (marker) · holds: soil metagenomes against isolates · src: pitonLifeHistoryStrategies2023 (asserted) · trail: H2-04 §Genome-level versus community-level, §answers · from: H2-04:B-0065, H2-04:A-066, H2-04:I-0038
- **genome-community-axes.4** A genome-level sugar-versus-acid catabolic axis derived from 186 isolates was carried to enrichment communities, finding the corresponding GC signature (lower GC in sugar-enriched communities, p < 1e-5): qualitative agreement with no axis statistic.
  conf: not stated · class: not stated · holds: 186 isolates and enrichment communities; the preprint read through a tool summary of full text, the published version abstract only · src: gralkaFundamentalMetabolicStrategies2022 (closer to secondary; preprint; critic: C-053 was "FT-s preprint"), gralkaGenomeContentPredicts2023 (AB) · limit: access (critic: C-031) · trail: H2-04 §Genome-level versus community-level, §answers, §critic · from: H2-04:B-0066, H2-04:A-059, H2-04:C-031
- **genome-community-axes.5** Across bacteria and archaea, growth rate, genome size and cell size are near-independent: pairwise r2 is at most 0.012 (maximum 0.0121, genome size versus cell diameter); the paper also reports a weak nonlinearity (about 6% of variance) and habitat effects (about 11%), which qualify 'near-independent'.
  conf: not stated · class: not stated · holds: genome-level reference axes; pairwise values confirmed against full text by the critic · src: westobyCellSizeGenome2021 (FT) · trail: H2-04 §Genome-level versus community-level, §answers, §critic, §Adversarial critique · from: H2-04:B-0067, H2-04:A-060, H2-04:C-032, H2-04:C-033, H2-04:C-045, H2-04:C-062, H2-04:R-0136
- **genome-community-axes.6** Across about 18,000 genomes, trait relations reverse with genome size, above about 5 Mb.
  conf: not stated · class: not stated · holds: about 18,000 prokaryote genomes; abstract only, though the critic notes a PMC full text exists (PMC9634001) and is load-bearing as a genome-level reference axis · src: beierTraittraitRelationshipsTradeoffs2022 (AB) · trail: H2-04 §Genome-level versus community-level, §answers, §Adversarial critique · from: H2-04:B-0067, H2-04:A-060, H2-04:C-061, H2-04:R-0048
- **genome-community-axes.7** Growth-related genome traits are strongly correlated and have been used to read metagenomes.
  conf: not stated · class: not stated · holds: genomes and metagenomes; abstract only · src: vieirasilvaSystemicImprintGrowth2010 (AB) · trail: H2-04 §Genome-level versus community-level · from: H2-04:B-0067
- **genome-community-axes.8** Community-only functional axes exist: NMF of ocean metagenome protein families, without a genome-level comparison.
  conf: not stated · class: not stated · holds: ocean metagenomes; abstract only · src: jiangFunctionalBiogeographyOcean2012 (AB) · trail: H2-04 §Genome-level versus community-level, §answers · from: H2-04:B-0068, H2-04:A-061
- **genome-community-axes.9** By modelling on profiles built from the same genomes, how genes are distributed across genomes (functional redundancy) governs how community functional profiles respond to taxonomic perturbation (predicted versus observed shifts r = 0.86, n = 8): a modelled, indirect link.
  conf: not stated · class: model (marker) · holds: profiles built from the same genomes; modelled; the critic could not recheck r = 0.86, n = 8 · src: engTaxafunctionRobustnessMicrobial2018 (FT; modelled; indirect) · trail: H2-04 §Genome-level versus community-level, §answers, §Adversarial critique · from: H2-04:I-0039, H2-04:A-062, H2-04:C-063
- **genome-community-axes.10** Functional shifts decomposed into taxon contributions show that the contributing taxa vary markedly between functions.
  conf: not stated · class: not stated · holds: human microbiome; abstract only; annotated in the reference list, not cited in the body · src: manorSystematicCharacterizationAnalysis2017 (AB) · trail: H2-04 §Reference list · from: H2-04:R-0154, H2-04:R-0151, H2-04:R-0148
- **genome-community-axes.11** The nearest microbial precedents for a genome-level versus community-level axis comparison are single studies with qualitative comparisons.
  conf: single (note: "The nearest precedents are single studies with qualitative comparisons") · class: not stated · holds: Piton 2023 and the Gralka enrichment communities · src: pitonLifeHistoryStrategies2023, gralkaFundamentalMetabolicStrategies2022 · rating: "Absent as direct evidence" · trail: H2-04 §answers · from: H2-04:A-063, H2-04:A-064, H2-04:A-070

### plant-cross-level-axes: species-level versus community-level trait axes in plants (non-microbial analogues)
needs: trait-partitions

- **plant-cross-level-axes.1** The two main community-mean trait axes across more than 1.1 million plots (stature, resource acquisitiveness) 'reflect the trade-offs at the species level'; the community means are computed from the same species' database trait values, so not independent, and the abstract gives no agreement statistic; the paper itself notes the prior expectation of decoupling. The positive-agreement reading rests on this study alone; removing it leaves only disagreement or sign-reversal cases.
  conf: single (marker) · class: not stated · holds: plant communities, more than 1.1 million plots; abstract only; species-level trade-offs versus community-mean axes · src: bruelheideGlobalTraitenvironmentRelationships2018 (AB; single study) · rating: "Weak for the positive agreement claim, which rests on one abstract" · trail: H2-04 §Genome-level versus community-level, §answers, §critic · from: H2-04:I-0040, H2-04:A-072, H2-04:A-076, H2-04:A-082, H2-04:C-037, H2-04:C-042, H2-04:C-069
- **plant-cross-level-axes.2** The species-level reference axes are the two-dimensional global spectrum of plant form and function and the leaf economics spectrum.
  conf: not stated · class: not stated · holds: plants; abstract only · src: diazGlobalSpectrumPlant2015 (AB), wrightWorldwideLeafEconomics2004 (AB) · trail: H2-04 §Genome-level versus community-level · from: H2-04:B-0070, H2-04:R-0064
- **plant-cross-level-axes.3** Some leaf-economics correlations reverse sign within versus across species.
  conf: not stated · class: not stated · holds: plants; within-species versus across-species; abstract only · src: andereggWithinspeciesPatternsChallenge2018 (AB) · trail: H2-04 §answers, §Genome-level versus community-level · from: H2-04:A-073, H2-04:B-0071
- **plant-cross-level-axes.4** Area-based leaf traits scale with LMA within species but not across species, for different mechanistic reasons (mass-proportional versus area-proportional variation within versus across species).
  conf: not stated · class: not stated · holds: plants; within-species versus across-species · src: osnasDivergentDriversLeaf2018 (FT) · trail: H2-04 §answers, §Genome-level versus community-level · from: H2-04:A-073, H2-04:B-0071
- **plant-cross-level-axes.5** Correlation strength only bounds how dissimilar cross-scale trait structures can be.
  conf: not stated · class: not stated · holds: the leaf economic spectrum across scales, including local scales; abstract only · src: messierTraitVariationIntegration2016 (abstract) · trail: H2-04 §Genome-level versus community-level, §answers · from: H2-04:B-0071, H2-04:A-078, H2-04:R-0106
- **plant-cross-level-axes.6** That correlation strength only bounds cross-scale dissimilarity may reconcile the global agreement with the local or within-species disagreements, on the reviewer's reading.
  conf: not stated · class: reading (note: "that is the reviewer's reading") · holds: the reviewer's reading, labelled as such; the critic: acceptable, and no research-design evaluation was found · src: messierTraitVariationIntegration2016 (abstract) · trail: H2-04 §answers, §Adversarial critique · from: H2-04:A-078, H2-04:A-077, H2-04:C-110
- **plant-cross-level-axes.7** The one quantitative cross-level agreement measure found is eigenvector angles and eigenvalue ratios with permutation tests, used to show that including intraspecific variation rotates leaf trait axes.
  conf: not stated · class: not stated · holds: plant leaf traits; within-species versus across-species · src: puglielliIntraspecificVariabilityLeaf2024 (AB), puglielliQuantifyingInfluenceIntraspecific2025 (FT) · trail: H2-04 §answers, §Genome-level versus community-level · from: H2-04:A-074, H2-04:B-0072
- **plant-cross-level-axes.8** The plant analogues are three different partitions, kept apart: (i) species-level trade-offs versus community-mean axes (Bruelheide 2018, abstract only, which states agreement qualitatively); (ii) within-community versus among-community components (Kembel & Cahill, full text; Ackerly & Cornwell, abstract); (iii) within-species versus across-species (Anderegg, abstract; Osnas, full text; Puglielli, eigenvector angles). Evidence that cross-level structure can differ comes from (ii) and (iii), not from the species-versus-community-mean comparison closest to the genome-versus-community question; for (i) the only evidence is a single abstract, and it reports agreement.
  conf: not stated · class: not stated · holds: plants, non-microbial · src: bruelheideGlobalTraitenvironmentRelationships2018 (AB), kembelIndependentEvolutionLeaf2011 (FT), ackerlyTraitbasedApproachCommunity2007 (AB), andereggWithinspeciesPatternsChallenge2018 (AB), osnasDivergentDriversLeaf2018 (FT), puglielliIntraspecificVariabilityLeaf2024, puglielliQuantifyingInfluenceIntraspecific2025 · rating: "Partly supported" (critic: C-035: three different partitions are merged and should be kept apart) · trail: H2-04 §critic, §Adversarial critique · from: H2-04:C-035, H2-04:C-036, H2-04:C-037, H2-04:C-038, H2-04:C-039, H2-04:C-041, H2-04:C-042, H2-04:C-049, H2-04:C-101, H2-04:C-103
- **plant-cross-level-axes.9** In plants, cross-level axis agreement is not guaranteed and can reverse in sign, in within-community versus among-community and within-species versus across-species partitions.
  conf: not stated · class: not stated · holds: plant datasets; the critic: the review's 'replicated across independent plant datasets' mixes partition types · src: kembelIndependentEvolutionLeaf2011, andereggWithinspeciesPatternsChallenge2018, osnasDivergentDriversLeaf2018 · rating: "Moderate that cross-level axis agreement is not guaranteed and can reverse in sign" (critic: C-069: the replication across independent plant datasets mixes partition types) · trail: H2-04 §answers, §Adversarial critique, §critic · from: H2-04:A-075, H2-04:C-069, H2-04:C-041, H2-04:C-038, H2-04:C-039
- **plant-cross-level-axes.10** Not measured: quantitative agreement statistics for species-level versus community-mean axes at global scale.
  conf: not stated · class: search (note: "Not measured: Quantitative agreement statistics") · holds: plants, global scale · src: none (a search result) · search: not stated · trail: H2-04 §answers · from: H2-04:A-079, H2-04:A-071
- **plant-cross-level-axes.11** Animal trait analogues (and quantitative-genetic and morphometric analogues) of within- versus between-unit covariance partitions were not searched; the review reports animal analogues as not found in the routes used.
  conf: not stated · class: search (critic: C-043) · holds: animal trait ecology; quantitative genetics (G-matrix versus divergence); morphometrics (static versus evolutionary allometry) · src: none (a search result) · search: not searched (critic: C-043) · trail: H2-04 §answers, §critic, §Provenance · from: H2-04:A-080, H2-04:C-043, H2-04:B-0017
- **plant-cross-level-axes.12** Over 150 grassland plots, the first principal component across guild-level slow-fast axes explained 25% of combined variation, but no species-level versus community-level axis comparison was found in the paper, and the note did not enter it as a finding.
  conf: not stated · class: not stated · holds: 150 grassland plots; listed under the note's sources not obtained, though its full text XML was obtained and grepped · src: neyretSlowfastTraitContinuum2024 (full text XML obtained and grepped) · trail: H2-04 §Sources not obtained · from: H2-04:R-0027, H2-04:R-0028

## Do not say

- **dns.1** "Taxon co-occurrence networks have been built in quantity (Barberán 2012; Faust 2012; Fierer et al. 2014)."
  why: Fierer, Barberán & Laughlin 2014 is a community-aggregated-traits perspective, not a co-occurrence network study; the citation is misattributed, although its metadata is correct. · instead: association-networks.1 · trail: H2-04 §critic, §Adversarial critique · from: H2-04:C-004, H2-04:C-047, H2-04:C-073, H2-04:C-074, H2-04:C-075
- **dns.2** "Annotation dominates pipelines: annotation reference choice accounts for 65.4% of the variance in function profiles."
  why: The 65.4% is the 16S taxonomy database's share of variance among taxon networks (Kishore 2023 alone); it concerns taxonomic, not functional, annotation and says nothing directly about functional annotation schemes. · instead: association-networks.13 · trail: H2-04 §critic, §Adversarial critique · from: H2-04:C-005, H2-04:C-006, H2-04:C-048, H2-04:C-064, H2-04:C-104, H2-04:I-0013
- **dns.3** "Kamneva's reanalysis found complementarity non-significant once phylogeny is included, while the competition signal stands."
  why: The same combined model makes metabolic competition non-significant too (coefficient -0.013, p = 0.71); only the result against complementarity was carried into the review, so the overlap side escaped the same reanalysis. · instead: complementarity-overlap.4, complementarity-overlap.5 · trail: H2-04 §critic, §Adversarial critique, §Stage 2 check · from: H2-04:C-021, H2-04:C-046, H2-04:C-093, H2-04:C-094, H2-04:C-095, H2-04:B-0024, H2-04:I-0019
- **dns.4** "That whole-community co-occurrence associates with functional overlap is replicated across independent groups, at moderate strength."
  why: The overlap side rests on co-occurrence inference, which the review itself shows to be method-dependent (31.5% shared edges) and poorly validated; the critic rates it weak to moderate. · instead: complementarity-overlap.20 · trail: H2-04 §critic, §Adversarial critique · from: H2-04:C-025, H2-04:C-096, H2-04:C-097, H2-04:A-046
- **dns.5** "Tian 2020 replicates the co-occurrence pattern of functional overlap."
  why: Tian 2020 measures within-sample redundancy against a species-pool null, not pairwise co-occurrence; counting it as replication lowers the bar on the overlap side. · instead: complementarity-overlap.6 · trail: H2-04 §critic, §Adversarial critique · from: H2-04:C-022, H2-04:C-099, H2-04:C-105
- **dns.6** "Linkage is not uniform across functions: for sequential redox pathways, within-genome linkage is weak and pathway completion is distributed across organisms."
  why: This generalises from one aquifer study (Anantharaman 2016) to a class of functions. · instead: within-genome-linkage.3 · trail: H2-04 §Adversarial critique, §Linkage within genomes · from: H2-04:B-0032, H2-04:B-0033, H2-04:C-066, H2-04:I-0004
- **dns.7** "Horizontal transfer, concentrated among co-habitants, is a general caution on readings of functional overlap."
  why: The 25-fold figure and its structuring by habitat rest on one abstract (Smillie 2011), yet the answers use it as a general caution on the overlap side. · instead: within-genome-linkage.6, complementarity-overlap.23 · trail: H2-04 §Adversarial critique · from: H2-04:C-067, H2-04:A-045
- **dns.8** "Environmental heterogeneity is usually the strongest driver of correlation structure."
  why: This rests on Carr 2019 alone, which asserts it and was read only through a tool summary; the one measured partition (Deutschmann 2021) is for taxa. · instead: shared-environment.1, shared-environment.3 · trail: H2-04 §Adversarial critique, §critic · from: H2-04:C-068, H2-04:C-007, H2-04:I-0029
- **dns.9** "Phylogeny is the largest single predictor of pairwise co-occurrence."
  why: This rests on Kamneva 2017 alone, which reuses Levy & Borenstein's gut data and tested only four genomic indices. · instead: shared-ancestry.1 · trail: H2-04 §Adversarial critique · from: H2-04:C-065, H2-04:B-0051
- **dns.10** "The literature rarely names more than two sources of covariation in the same study."
  why: The review asserts this without a source; it is the reviewer's generalisation presented as a property of the field. · instead: covariation-sources.1 · trail: H2-04 §Adversarial critique, §What the question contains · from: H2-04:C-108, H2-04:B-0027
- **dns.11** "The functional-profile question has been approached from two sides that do not meet."
  why: This is the reviewer's synthesis argument, reasonable but not labelled as the reviewer's reading in the review; stated as a finding it presents a reading as evidence. · instead: covariation-sources.7 · trail: H2-04 §Adversarial critique, §How the cases relate · from: H2-04:C-109, H2-04:B-0074
- **dns.12** "Plant ecology has compared species-level and community-level axes with mixed results: Bruelheide 2018 finds agreement at global scale, against the disagreement or sign reversal of Kembel & Cahill 2011, Anderegg 2018 and Osnas 2018."
  why: This folds three distinct partitions into one comparison; sign reversals from within-species and within-community partitions do not answer the species-versus-community-mean comparison, for which the only evidence is Bruelheide's single abstract, and it reports agreement. · instead: plant-cross-level-axes.8 · trail: H2-04 §answers, §critic, §Adversarial critique · from: H2-04:A-071, H2-04:A-077, H2-04:C-036, H2-04:C-041, H2-04:C-049, H2-04:C-101, H2-04:C-103, H2-04:C-037, H2-04:C-042
- **dns.13** "That cross-level axis agreement can reverse in sign is replicated across independent plant datasets."
  why: The 'replicated across independent plant datasets' strength mixes partition types (within-community versus among-community and within-species versus across-species). · instead: plant-cross-level-axes.9 · trail: H2-04 §Adversarial critique · from: H2-04:C-069, H2-04:A-075, H2-04:C-038, H2-04:C-039, H2-04:C-041
- **dns.14** "Dong 2020 shows trait axes reversing between levels."
  why: Dong 2020 is about trait-environment responses (variation along gradients), not about axis reversal or an axis comparison. · instead: trait-partitions.5 · trail: H2-04 §critic, §Adversarial critique · from: H2-04:C-040, H2-04:C-102
- **dns.15** "Intraspecific variation accounts for 25% of within-community and 32% of among-community trait covariance."
  why: The Siefert figures are a variance partition, not a covariance partition, and a within-species versus between-species partition, which differs from the within-community versus among-community partitions beside which the answer lists it. · instead: trait-partitions.7 · trail: H2-04 §answers, §critic, §Adversarial critique · from: H2-04:A-025, H2-04:C-015, H2-04:C-107
- **dns.16** "Growth rate, genome size and cell size are near-independent (r2 at most 0.012)."
  why: The pairwise values are right, but the paper also reports a weak nonlinearity (about 6% of variance) and habitat effects (about 11%), which qualify 'near-independent'; the review states 'near-independent' without them. · instead: genome-community-axes.5 · trail: H2-04 §critic, §Adversarial critique · from: H2-04:C-033, H2-04:C-062, H2-04:B-0067
- **dns.17** "In simulation, only the individual methods removed true interactions (38 to 86%)."
  why: The review omits that the intersection approach also removed 25% of true interactions. · instead: shared-environment.3 · trail: H2-04 §critic · from: H2-04:C-012, H2-04:C-011
- **dns.18** "Zelezniak 2015, Levy & Borenstein 2013, Russel 2017, Carr 2019, Arandia-Gorostidi 2025 and the Gralka preprint were read in full text."
  why: They were read through web-fetch tool summaries ('FT-s'), which are not one of the protocol's access categories and are closer to secondary; the review's own legend says their quotes are to be rechecked. · instead: none · trail: H2-04 §critic, §Adversarial critique · from: H2-04:C-050, H2-04:C-052, H2-04:C-053, H2-04:C-054
- **dns.19** "Gene-level networks show interactions among the populations carrying the genes."
  why: That is their authors' conclusion; the reviewer cannot confirm it from the reported analyses, which neither separate genes that share a genome, nor correct for closure, nor condition on environment. · instead: gene-level-networks.3 · trail: H2-04 §Gene-level networks · from: H2-04:B-0039, H2-04:B-0040
- **dns.20** "In vitro interaction studies show how functions covary across community samples."
  why: None of these studies involve community profiles; they bear on mechanism, not on covariation across samples. · instead: complementarity-overlap.13 · trail: H2-04 §Complementarity versus overlap, §critic · from: H2-04:B-0046, H2-04:C-024
- **dns.21** "Zelezniak 2015 and Machado 2021 independently show complementarity among co-occurring groups."
  why: The two papers share authors and framework and should be counted as one line of evidence; the Zelezniak figures were read only through a tool summary. · instead: complementarity-overlap.9 · trail: H2-04 §Complementarity versus overlap, §critic · from: H2-04:B-0044, H2-04:C-023, H2-04:C-055
- **dns.22** "Community-level genomic trait axes in soil are the same as the isolate-based genome-level axes (Piton 2023)."
  why: The authors say the community axes are consistent with isolate-based axes without testing it, and their own caveat and the asserted compression of community-average rRNA copy number cut against reading the qualitative agreement as axis identity. · instead: genome-community-axes.2, genome-community-axes.3 · trail: H2-04 §answers · from: H2-04:A-066, H2-04:A-057
- **dns.23** "The plant results show how genome-level and community-level functional axes relate in microbes."
  why: Transferring the plant results to microbes would be an inference, not evidence. · instead: none · trail: H2-04 §How the cases relate · from: H2-04:B-0076
- **dns.24** "Taxon co-occurrence networks show that co-occurrence of organisms is a source of covariation among functions."
  why: Taxon (16S) co-occurrence networks are a different measurement type standing in for function-level covariation, which the review only partly acknowledges. · instead: covariation-sources.1, association-networks.1 · trail: H2-04 §Adversarial critique · from: H2-04:C-106
- **dns.25** "Compositionally aware methods remove closure artefacts."
  why: Their own papers say yes, but an independent simulation found they did no better than Pearson correlation; the review calls this a genuine conflict that is not resolved. · instead: association-networks.4 · trail: H2-04 §Taxon networks, §answers · from: H2-04:B-0036, H2-04:I-0008, H2-04:A-008
- **dns.26** "Gene co-abundance binning gives replicated evidence that gene covariation across metagenomes is structured by genome membership."
  why: Within-genome linkage at gene level rests on one abstract (Nielsen 2014: 7,381 co-abundance groups, 741 metagenomic species, 396 gut metagenomes), which reports no covariance share. · instead: within-genome-linkage.1 · trail: H2-04 §critic · from: H2-04:C-003, H2-04:I-0003
- **dns.27** "Ackerly & Cornwell and Kembel & Cahill contradict each other on whether among-community or within-community covariation dominates."
  why: They are different systems and, in the review's words, not contradictory in the strict sense. · instead: trait-partitions.4 · trail: H2-04 §answers · from: H2-04:A-031

## Gaps

- **gap.1** Phylogenetic profiling of gene co-occurrence across genomes, and pangenome gene co-occurrence or avoidance (the Pellegrini et al. 1999 lineage; pangenome co-occurrence tools such as Coinfinder), an explicit related-work item in the brief on which the review contains nothing, not even a not-found with routes.
  blocks: within-genome-linkage, genome-community-axes · origin: critic coverage gap; comparative genomics · search: not searched (critic: C-081) · from: H2-04:C-081
- **gap.2** Partition of community functional variation into taxonomic turnover versus within-taxon change for metagenomic or metatranscriptomic function profiles; Salazar et al. 2019 (Cell), separating gene-expression change from community turnover in the ocean metatranscriptome, is the obvious candidate.
  blocks: covariation-partition · origin: critic coverage gap; marine metatranscriptomics · search: not stated · from: H2-04:C-082
- **gap.3** Covariation of functions or pathways with environment across metagenomes using function-level data rather than taxa (e.g., Gianoulis et al. 2009 PNAS canonical correlation of pathways with ocean environment; Raes et al. 2011 Mol Syst Biol; Fierer et al. 2012 PNAS cross-biome soil metagenomes).
  blocks: shared-environment · origin: critic coverage gap; ocean and soil shotgun metagenomes · search: not stated · from: H2-04:C-083
- **gap.4** Normalisation and sequencing-depth handling for gene-abundance profiles: average genome size correction, single-copy-gene normalisation (e.g., MUSiCC, Manor & Borenstein 2015), and comparisons of normalisation methods for metagenomic gene abundances (e.g., Pereira et al. 2018 BMC Genomics); the artefact section covers only closure in taxon data.
  blocks: aggregation-artefacts, covariation-sources · origin: critic coverage gap; shotgun metagenome function profiles · search: not stated · from: H2-04:C-084
- **gap.5** Functional annotation-scheme artefacts (KEGG versus COG versus eggNOG or Pfam, annotation rate differences between samples); the only magnitude given is for a 16S taxonomy database.
  blocks: association-networks.13, covariation-sources · origin: critic coverage gap; functional annotation of metagenomes · search: not stated · from: H2-04:C-085
- **gap.6** Contamination and chimerism in MAGs that bear on measured within-genome linkage (e.g., Shaiber & Eren 2019 mBio on composite MAGs; GUNC chimerism estimates; CheckM); the review says no source was found that quantifies contamination effects on linkage.
  blocks: within-genome-linkage · origin: critic coverage gap; the review's not-found result · search: searched, not found (note: "No source found quantifies contamination effects on linkage estimates specifically") · from: H2-04:C-086, H2-04:B-0034
- **gap.7** Gene co-abundance binning beyond one abstract (e.g., Qin et al. 2012 metagenomic linkage groups; MSPminer; CONCOCT and other differential-coverage binning); none was checked for reported shares of gene covariance explained by bin membership.
  blocks: within-genome-linkage · origin: critic coverage gap; human gut and other multi-sample metagenome series · search: not stated · from: H2-04:C-087
- **gap.8** Community profiles predicted from reference genomes versus measured metagenomes (PICRUSt, Langille 2013; PICRUSt2, Douglas 2020; Tax4Fun), which report agreement statistics between genome-built and independently measured function profiles; this bears on the brief's requirement that profiles be built from the same genomes or measured independently.
  blocks: genome-community-axes, covariation-sources · origin: critic coverage gap; 16S-predicted versus shotgun-measured function profiles · search: not stated · from: H2-04:C-088
- **gap.9** Within-unit versus between-unit covariance comparisons in evolutionary quantitative genetics and morphometrics, where formal agreement measures (Krzanowski subspace comparison, vector correlations, random skewers) were developed: G-matrix versus among-population divergence (Schluter 1996 'lines of least resistance'), static versus evolutionary allometry.
  blocks: genome-community-axes, trait-partitions · origin: critic coverage gap; animal and plant · search: not searched (critic: C-043) · from: H2-04:C-089, H2-04:C-043
- **gap.10** Animal trait ecology analogues (e.g., fish, birds, invertebrates: community-weighted means versus species-level trait axes), reported as not found with no routes named beyond the general list.
  blocks: plant-cross-level-axes · origin: critic coverage gap · search: not searched (critic: C-043) · from: H2-04:C-090, H2-04:C-043
- **gap.11** Taxonomy-function coupling across samples measured with Procrustes or Mantel between taxonomic and functional ordinations (e.g., HMP 2012; Burke et al. 2011 PNAS on Ulva-associated communities assembled by function), the nearest precedents for an ordination agreement measure.
  blocks: genome-community-axes · origin: critic coverage gap; human microbiome and marine host-associated metagenomes · search: not stated · from: H2-04:C-091
- **gap.12** Genome-level structure of gene content, such as the nestedness of the genome-content network (Tian 2020, cited only for redundancy), not related to community-level axes.
  blocks: genome-community-axes · origin: critic coverage gap; human microbiome reference genomes · search: not stated · from: H2-04:C-092
- **gap.13** The stage-2 check was triggered: a targeted follow-up brief on phylogenetic profiling, subspace comparison methods and turnover decompositions, sized separately, because the critic's gaps name partition methods and fields not searched (phylogenetic profiling and pangenome gene co-occurrence; G-matrix and subspace comparison; turnover against within-taxon decomposition; gene co-abundance binning beyond Nielsen 2014; and artefact gaps in gene-abundance normalisation, annotation-scheme effects, MAG chimerism and PICRUSt-type agreement).
  blocks: covariation-partition, within-genome-linkage, genome-community-axes · origin: the note's stage-2 check (ROUTING condition) · search: not searched (note: "The gaps name partition methods and fields not searched") · trail: H2-04 §Stage 2 check · from: H2-04:B-0020, H2-04:B-0021, H2-04:B-0022, H2-04:B-0023
- **gap.14** A partition of function-by-function covariance in community profiles into within-genome linkage, co-occurrence, environment, ancestry and artefact shares.
  blocks: covariation-partition · origin: the review's not-found result · search: searched, not found (note: "No study found partitions covariation among functions in community profiles") · trail: H2-04 §answers, §Provenance · from: H2-04:A-018, H2-04:B-0017
- **gap.15** A formal agreement statistic between genome-level and community-level functional axes in any microbial system, with community profiles built from the same genomes and measured independently.
  blocks: genome-community-axes · origin: the review's not-found result · search: searched, not found (note: "No study found compares the main axes of functional variation among genomes with those among community profiles") · trail: H2-04 §answers, §Provenance · from: H2-04:A-056, H2-04:A-067, H2-04:B-0017
- **gap.16** A gene or KO co-occurrence network that removes within-genome linkage.
  blocks: gene-level-networks · origin: the review's not-found result · search: searched, not found (note: "Gene-level networks controlling for within-genome linkage were not found") · trail: H2-04 §answers · from: H2-04:A-010
- **gap.17** A microbial application of the turnover versus within-taxon (Leps-type) decomposition to functional profiles; Leps et al. 2011 itself was not obtained.
  blocks: covariation-partition · origin: the review's not-found result and a source not obtained · src: lepsCommunityTraitResponse2011 · search: searched, not found (note: "also Europe PMC queries on community-aggregated traits with covariation and trade-off terms") · trail: H2-04 §answers, §Sources not obtained · from: H2-04:A-032, H2-04:A-033
- **gap.18** Quantitative agreement statistics for species-level versus community-mean trait axes at global scale.
  blocks: plant-cross-level-axes · origin: the review's not-measured result · search: not stated · from: H2-04:A-079
- **gap.19** Quotes and figures read only through web-fetch tool summaries need rechecking in the original: Levy & Borenstein 2013, Zelezniak 2015, Russel 2017, Carr 2019, Arandia-Gorostidi 2025 and the Gralka preprint; the synthesis agent did not re-open them.
  blocks: complementarity-overlap, shared-environment, gene-level-networks, genome-community-axes · origin: the note's synthesis-stage check; critic access findings · search: not stated · trail: H2-04 §Provenance, §critic · from: H2-04:B-0015, H2-04:B-0016, H2-04:C-050
- **gap.20** Figures the critic could not verify for access reasons: Chaffron 2010's 'beyond phylogeny' (not in the abstract; full text blocked), Piton 2023's 29%, 21%, R2 = 0.64, R2 = 0.32 and 5 to 15% of reads annotated (open copies returned HTML), Weiss 2016's 31.5% shared edges, precision 0.2 and effective species about 13 (PMC XML not retrievable), and Eng & Borenstein's r = 0.86, n = 8 and Levy & Borenstein's rho values.
  blocks: complementarity-overlap, genome-community-axes, association-networks · origin: critic access findings · search: not stated · trail: H2-04 §critic, §Adversarial critique · from: H2-04:C-051, H2-04:C-056, H2-04:C-058, H2-04:C-060, H2-04:C-063
- **gap.21** Beier 2022, load-bearing as a genome-level reference axis, was read in the abstract only, although a PMC full text exists (PMC9634001).
  blocks: genome-community-axes · origin: critic access finding · src: beierTraittraitRelationshipsTradeoffs2022 · search: not stated · trail: H2-04 §Adversarial critique · from: H2-04:C-061
- **gap.22** The note contradicts itself on its sources not obtained: the list says nothing beyond a citation was reachable for them and none supports any claim in the review, yet Blanchet 2020, Freilich 2011, Freilich 2018, Goldford 2018 and Lima-Mendez 2015 are also in the reference list as abstract-only sources and are cited in the body; for Lima-Mendez the body says the numbers were not reached.
  blocks: association-networks, shared-environment, complementarity-overlap · origin: a note that contradicts itself · src: blanchetCooccurrenceNotEvidence2020, freilichCompetitiveCooperativeMetabolic2011, freilichSpeciesCooccurrenceNetworks2018, goldfordEmergentSimplicityMicrobial2018, limamendezDeterminantsCommunityStructure2015 · search: not stated · trail: H2-04 §Sources not obtained, §Shared response, §Reference list · from: H2-04:R-0001, H2-04:B-0050

## Out of scope

- H2-04:C-071, H2-04:C-072, H2-04:C-076, H2-04:C-077: reference corrections, applied in Sources
- H2-04:C-078, H2-04:C-079: citation bookkeeping (uncited sources, a source cited by name), recorded in Sources
- H2-04:C-080: the critic's confirmation that the remaining DOIs and author lists match Crossref (verification record, kept in the result note)
- H2-04:C-111, H2-04:C-112: the brief's wording in the expectation-echo check (provenance, kept in the result note)
- H2-04:A-012..015, H2-04:A-034, H2-04:A-035, H2-04:A-053, H2-04:A-069, H2-04:A-081: access basis of the answers (provenance; each source's access is in Sources)

## Sources

```bibtex
@article{ackerlyTraitbasedApproachCommunity2007,
  author = {Ackerly, D. D. and Cornwell, W. K.},
  title = {A trait-based approach to community assembly: partitioning of species trait values into within- and among-community components},
  journal = {Ecology Letters},
  year = {2007},
  volume = {10},
  number = {2},
  pages = {135--145},
  doi = {10.1111/j.1461-0248.2006.01006.x},
  note = {access: abstract_only; cited as: H2-04 [1]}
}
@article{andereggWithinspeciesPatternsChallenge2018,
  author = {Anderegg, L. D. L. and Berner, L. T. and Badgley, G. and Sethi, M. L. and Law, B. E. and HilleRisLambers, J.},
  title = {Within-species patterns challenge our understanding of the leaf economics spectrum},
  journal = {Ecology Letters},
  year = {2018},
  volume = {21},
  number = {5},
  pages = {734--744},
  doi = {10.1111/ele.12945},
  note = {access: abstract_only; cited as: H2-04 [1a]}
}
@article{agrawalScaledependentFrameworkTradeoffs2020,
  author = {Agrawal, A. A.},
  title = {A scale-dependent framework for trade-offs, syndromes, and specialization in organismal biology},
  journal = {Ecology},
  year = {2020},
  volume = {101},
  number = {2},
  pages = {e02924},
  doi = {10.1002/ecy.2924},
  note = {access: abstract_only; cited as: H2-04 [1b]}
}
@article{beierTraittraitRelationshipsTradeoffs2022,
  author = {Beier, S. and Werner, J. and Bouvier, T. and Mouquet, N. and Violle, C.},
  title = {Trait-trait relationships and tradeoffs vary with genome size in prokaryotes},
  journal = {Frontiers in Microbiology},
  year = {2022},
  volume = {13},
  pages = {985216},
  doi = {10.3389/fmicb.2022.985216},
  note = {access: abstract_only; cited as: H2-04 [2a]; critic: H2-04:C-061, a PMC full text exists (PMC9634001)}
}
@article{barberanExplorationCommunityTraits2011,
  author = {Barberán, A. and Fernández-Guerra, A. and Bohannan, B. J. M. and Casamayor, E. O.},
  title = {Exploration of community traits as ecological markers in microbial metagenomes},
  journal = {Molecular Ecology},
  year = {2012},
  volume = {21},
  number = {8},
  pages = {1909--1917},
  doi = {10.1111/j.1365-294X.2011.05383.x},
  note = {access: abstract_only; cited as: H2-04 [2b]}
}
@article{berryDecipheringMicrobialInteractions2014,
  author = {Berry, D. and Widder, S.},
  title = {Deciphering microbial interactions and detecting keystone species with co-occurrence networks},
  journal = {Frontiers in Microbiology},
  year = {2014},
  volume = {5},
  pages = {219},
  doi = {10.3389/fmicb.2014.00219},
  note = {access: abstract_only; cited as: H2-04 [3]}
}
@article{anantharamanThousandsMicrobialGenomes2016,
  author = {Anantharaman, K. and Brown, C. T. and Hug, L. A. and Sharon, I. and Castelle, C. J. and Probst, A. J. and Thomas, B. C. and Singh, A. and Wilkins, M. J. and Karaoz, U. and Brodie, E. L. and Williams, K. H. and Hubbard, S. S. and Banfield, J. F.},
  title = {Thousands of microbial genomes shed light on interconnected biogeochemical processes in an aquifer system},
  journal = {Nature Communications},
  year = {2016},
  volume = {7},
  pages = {13219},
  doi = {10.1038/ncomms13219},
  note = {access: full_text; cited as: H2-04 [3a]}
}
@article{blanchetCooccurrenceNotEvidence2020,
  author = {Blanchet, F. G. and Cazelles, K. and Gravel, D.},
  title = {Co-occurrence is not evidence of ecological interactions},
  journal = {Ecology Letters},
  year = {2020},
  volume = {23},
  number = {7},
  pages = {1050--1063},
  doi = {10.1111/ele.13525},
  note = {access: abstract_only; cited as: H2-04 [3b]; also listed under Sources not obtained, abstract only (conflict between the note's lists)}
}
@article{bruelheideGlobalTraitenvironmentRelationships2018,
  author = {Bruelheide, H. and Dengler, J. and Purschke, O. and Lenoir, J. and Jiménez-Alfaro, B. and Hennekens, S. M. and Botta-Dukát, Z. and Chytrý, M. and Field, R. and Jansen, F. and Kattge, J. and Pillar, V. D. and Schrodt, F. and Mahecha, M. D. and Peet, R. K. and Sandel, B. and van Bodegom, P. and Altman, J. and Alvarez-Dávila, E. and Arfin Khan, M. A. S. and Attorre, F. and Aubin, I. and Baraloto, C. and Barroso, J. G. and Bauters, M. and Bergmeier, E. and Biurrun, I. and Bjorkman, A. D. and Blonder, B. and Čarni, A. and Cayuela, L. and Černý, T. and Cornelissen, J. H. C. and Craven, D. and Dainese, M. and Derroire, G. and De Sanctis, M. and Díaz, S. and Doležal, J. and Farfan-Rios, W. and Feldpausch, T. R. and Fenton, N. J. and Garnier, E. and Guerin, G. R. and Gutiérrez, A. G. and Haider, S. and Hattab, T. and Henry, G. and Hérault, B. and Higuchi, P. and Hölzel, N. and Homeier, J. and Jentsch, A. and Jürgens, N. and Kącki, Z. and Karger, D. N. and Kessler, M. and Kleyer, M. and Knollová, I. and Korolyuk, A. Y. and Kühn, I. and Laughlin, D. C. and Lens, F. and Loos, J. and Louault, F. and Lyubenova, M. I. and Malhi, Y. and Marcenò, C. and Mencuccini, M. and Müller, J. V. and Munzinger, J. and Myers-Smith, I. H. and Neill, D. A. and {Niinemets Ü} and Orwin, K. H. and Ozinga, W. A. and Penuelas, J. and Pérez-Haase, A. and Petřík, P. and Phillips, O. L. and Pärtel, M. and Reich, P. B. and Römermann, C. and Rodrigues, A. V. and Sabatini, F. M. and Sardans, J. and Schmidt, M. and Seidler, G. and Silva Espejo, J. E. and Silveira, M. and Smyth, A. and Sporbert, M. and Svenning, J. C. and Tang, Z. and Thomas, R. and Tsiripidis, I. and Vassilev, K. and Violle, C. and Virtanen, R. and Weiher, E. and Welk, E. and Wesche, K. and Winter, M. and Wirth, C. and Jandt, U.},
  title = {Global trait-environment relationships of plant communities},
  journal = {Nature Ecology & Evolution},
  year = {2018},
  volume = {2},
  number = {12},
  pages = {1906--1917},
  doi = {10.1038/s41559-018-0699-8},
  note = {access: abstract_only; cited as: H2-04 [3c]}
}
@article{chaffronGlobalNetworkCoexisting2010,
  author = {Chaffron, S. and Rehrauer, H. and Pernthaler, J. and von Mering, C.},
  title = {A global network of coexisting microbes from environmental and whole-genome sequence data},
  journal = {Genome Research},
  year = {2010},
  volume = {20},
  number = {7},
  pages = {947--959},
  doi = {10.1101/gr.104521.109},
  note = {access: full_text; cited as: H2-04 [4]; critic: H2-04:C-056 could not reach the full text, so 'beyond phylogeny' is unverified}
}
@article{chenLifehistoryStrategiesSoil2020,
  author = {Chen, Y. and Neilson, J. W. and Kushwaha, P. and Maier, R. M. and Barberán, A.},
  title = {Life-history strategies of soil microbial communities in an arid ecosystem},
  journal = {The ISME Journal},
  year = {2021},
  volume = {15},
  number = {3},
  pages = {649--657},
  doi = {10.1038/s41396-020-00803-y},
  note = {access: abstract_only; cited as: H2-04 [4b]}
}
@article{carrUseAbuseCorrelation2019,
  author = {Carr, A. and Diener, C. and Baliga, N. S. and Gibbons, S. M.},
  title = {Use and abuse of correlation analyses in microbial ecology},
  journal = {The ISME Journal},
  year = {2019},
  volume = {13},
  number = {11},
  pages = {2647--2655},
  doi = {10.1038/s41396-019-0459-z},
  note = {access: secondary (critic: H2-04:C-053, a model's summary of a paper is closer to secondary; the note said FT-s, full text read through a web-fetch tool summary, quotes to be rechecked); cited as: H2-04 [5]}
}
@article{barberanUsingNetworkAnalysis2011,
  author = {Barberán, A. and Bates, S. T. and Casamayor, E. O. and Fierer, N.},
  title = {Using network analysis to explore co-occurrence patterns in soil microbial communities},
  journal = {The ISME Journal},
  year = {2012},
  volume = {6},
  number = {2},
  pages = {343--351},
  doi = {10.1038/ismej.2011.119},
  note = {access: abstract_only; cited as: H2-04 [6]}
}
@article{dasVitroCoculturesHuman2018,
  author = {Das, P. and Ji, B. and Kovatcheva-Datchary, P. and Bäckhed, F. and Nielsen, J.},
  title = {In vitro co-cultures of human gut bacterial species as predicted from co-occurrence network analysis},
  journal = {PLOS ONE},
  year = {2018},
  volume = {13},
  number = {3},
  pages = {e0195161},
  doi = {10.1371/journal.pone.0195161},
  note = {access: full_text; cited as: H2-04 [6a]; cited in the body by name, not by marker (critic: H2-04:C-079)}
}
@article{diazGlobalSpectrumPlant2015,
  author = {Díaz, S. and Kattge, J. and Cornelissen, J. H. C. and Wright, I. J. and Lavorel, S. and Dray, S. and Reu, B. and Kleyer, M. and Wirth, C. and Prentice, I. C. and Garnier, E. and Bönisch, G. and Westoby, M. and Poorter, H. and Reich, P. B. and Moles, A. T. and Dickie, J. and Gillison, A. N. and Zanne, A. E. and Chave, J. and Wright, S. J. and Sheremet'ev, S. N. and Jactel, H. and Baraloto, C. and Cerabolini, B. and Pierce, S. and Shipley, B. and Kirkup, D. and Casanoves, F. and Joswig, J. S. and Günther, A. and Falczuk, V. and Rüger, N. and Mahecha, M. D. and Gorné, L. D.},
  title = {The global spectrum of plant form and function},
  journal = {Nature},
  year = {2016},
  volume = {529},
  number = {7585},
  pages = {167--171},
  doi = {10.1038/nature16489},
  note = {access: abstract_only; cited as: H2-04 [6b]}
}
@article{deutschmannDisentanglingEnvironmentalEffects2021,
  author = {Deutschmann, I. M. and Lima-Mendez, G. and Krabberød, A. K. and Raes, J. and Vallina, S. M. and Faust, K. and Logares, R.},
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
  author = {Dong, N. and Prentice, I. C. and Wright, I. J. and Evans, B. J. and Togashi, H. F. and Caddy-Retalic, S. and McInerney, F. A. and Sparrow, B. and Leitch, E. and Lowe, A. J.},
  title = {Components of leaf-trait variation along environmental gradients},
  journal = {New Phytologist},
  year = {2020},
  volume = {228},
  number = {1},
  pages = {82--94},
  doi = {10.1111/nph.16558},
  note = {access: abstract_only; cited as: H2-04 [7a]}
}
@article{friedmanInferringCorrelationNetworks2012,
  author = {Friedman, J. and Alm, E. J.},
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
  author = {Eng, A. and Borenstein, E.},
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
  author = {Faust, K. and Sathirapongsasuti, J. F. and Izard, J. and Segata, N. and Gevers, D. and Raes, J. and Huttenhower, C.},
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
  author = {Faust, K.},
  title = {Open challenges for microbial network construction and analysis},
  journal = {The ISME Journal},
  year = {2021},
  volume = {15},
  number = {11},
  pages = {3111--3118},
  doi = {10.1038/s41396-021-01027-4},
  note = {access: full_text; cited as: H2-04 [9a]}
}
@article{fiererSeeingForestGenes2014,
  author = {Fierer, N. and Barberán, A. and Laughlin, D. C.},
  title = {Seeing the forest for the genes: using metagenomics to infer the aggregated traits of microbial communities},
  journal = {Frontiers in Microbiology},
  year = {2014},
  volume = {5},
  pages = {614},
  doi = {10.3389/fmicb.2014.00614},
  note = {access: abstract_only; cited as: H2-04 [10]; critic: H2-04:C-073..075, cited as a co-occurrence network study but its abstract is about community-aggregated traits (misattributed citation; metadata correct); not cited by any claim here, since the critic removed it from the list it supported}
}
@article{fosterCompetitionNotCooperation2012,
  author = {Foster, K. R. and Bell, T.},
  title = {Competition, not cooperation, dominates interactions among culturable microbial species},
  journal = {Current Biology},
  year = {2012},
  volume = {22},
  number = {19},
  pages = {1845--1850},
  doi = {10.1016/j.cub.2012.08.005},
  note = {access: abstract_only; cited as: H2-04 [10a]}
}
@article{freilichSpeciesCooccurrenceNetworks2018,
  author = {Freilich, M. A. and Wieters, E. and Broitman, B. R. and Marquet, P. A. and Navarrete, S. A.},
  title = {Species co-occurrence networks: Can they reveal trophic and non-trophic interactions in ecological communities?},
  journal = {Ecology},
  year = {2018},
  volume = {99},
  number = {3},
  pages = {690--699},
  doi = {10.1002/ecy.2142},
  note = {access: abstract_only; cited as: H2-04 [10b]; also listed under Sources not obtained, abstract only (conflict between the note's lists)}
}
@article{freilichCompetitiveCooperativeMetabolic2011,
  author = {Freilich, S. and Zarecki, R. and Eilam, O. and Shtifman Segal, Ella and Henry, C. S. and Kupiec, M. and Gophna, U. and Sharan, R. and Ruppin, E.},
  title = {Competitive and cooperative metabolic interactions in bacterial communities},
  journal = {Nature Communications},
  year = {2011},
  volume = {2},
  pages = {589},
  doi = {10.1038/ncomms1597},
  note = {access: abstract_only; cited as: H2-04 [10c]; author corrected (critic: H2-04:C-072, the note had Segal ES); also listed under Sources not obtained (conflict between the note's lists)}
}
@article{hiranoDifficultyInferringMicrobial2019,
  author = {Hirano, H. and Takemoto, K.},
  title = {Difficulty in inferring microbial community structure based on co-occurrence network approaches},
  journal = {BMC Bioinformatics},
  year = {2019},
  volume = {20},
  number = {1},
  pages = {329},
  doi = {10.1186/s12859-019-2915-1},
  note = {access: full_text; cited as: H2-04 [11]}
}
@article{gralkaFundamentalMetabolicStrategies2022,
  author = {Gralka, M. and Pollak, S. and Cordero, O. X.},
  title = {Fundamental metabolic strategies of heterotrophic bacteria},
  journal = {bioRxiv},
  year = {2022},
  doi = {10.1101/2022.08.04.502823},
  note = {access: secondary (critic: H2-04:C-053, a model's summary of a paper is closer to secondary; the note said FT-s, preprint read through a web-fetch tool summary); type: preprint; cited as: H2-04 [11a]; incomplete: volume, pages}
}
@article{gralkaGenomeContentPredicts2023,
  author = {Gralka, M. and Pollak, S. and Cordero, O. X.},
  title = {Genome content predicts the carbon catabolic preferences of heterotrophic bacteria},
  journal = {Nature Microbiology},
  year = {2023},
  volume = {8},
  number = {10},
  pages = {1799--1808},
  doi = {10.1038/s41564-023-01458-z},
  note = {access: abstract_only; published version of the preprint; cited as: H2-04 [11a]}
}
@article{arandiagorostidiMetagenomicbasedNetworkAnalysis2025,
  author = {Arandia-Gorostidi, N. and Montiel, L. and Latorre, F. and Balagué, V. and Gasol, J. M. and Simó, R. and Giner, C. R. and Logares, R.},
  title = {Metagenomic-based network analysis reveals the importance of vitamin cross-feeding in marine microbial assemblages},
  journal = {bioRxiv},
  year = {2025},
  doi = {10.1101/2025.08.08.668683},
  note = {access: secondary (critic: H2-04:C-053, a model's summary of a paper is closer to secondary; the note said FT-s, full text read through a web-fetch tool summary); type: preprint; cited as: H2-04 [2]; incomplete: volume, pages}
}
@article{calcagnoMetacommunityDynamicsDetection2021,
  author = {Calcagno, V. and Cunniffe, N. and Hamelin, F. M.},
  title = {Metacommunity dynamics and the detection of species associations in co-occurrence analyses: why patch disturbance matters},
  journal = {bioRxiv},
  year = {2021},
  doi = {10.1101/2021.06.14.448327},
  note = {access: abstract_only; type: preprint; cited as: H2-04 [4a]; incomplete: volume, pages}
}
@article{tackmannRapidInferenceDirect2019,
  author = {Tackmann, J. and Matias Rodrigues, J. F. and von Mering, C.},
  title = {Rapid inference of direct interactions in large-scale ecological networks from heterogeneous microbial sequencing data},
  journal = {Cell Systems},
  year = {2019},
  volume = {9},
  number = {3},
  pages = {286--296.e8},
  doi = {10.1016/j.cels.2019.08.002},
  note = {access: abstract_only; not cited in the body, annotated in the reference list (critic: H2-04:C-078); cited as: H2-04 [41]}
}
@article{gobernaCautionaryNotesUse2022,
  author = {Goberna, M. and Verdú, M.},
  title = {Cautionary notes on the use of co-occurrence networks in soil ecology},
  journal = {Soil Biology and Biochemistry},
  year = {2022},
  volume = {166},
  pages = {108534},
  doi = {10.1016/j.soilbio.2021.108534},
  note = {access: not_obtained (abstract seen only in an index record); listed under Sources not obtained; not cited}
}
@article{lepsCommunityTraitResponse2011,
  author = {Lepš, J. and de Bello, F. and Šmilauer, P. and Doležal, J.},
  title = {Community trait response to environment: disentangling species turnover vs intraspecific trait variability effects},
  journal = {Ecography},
  year = {2011},
  volume = {34},
  number = {5},
  pages = {856--863},
  doi = {10.1111/j.1600-0587.2010.06904.x},
  note = {access: not_obtained; listed twice under Sources not obtained; named in the answers (Leps et al. 2011 itself not obtained)}
}
@article{debelloQuantifyingRelevanceIntraspecific2010,
  author = {de Bello, F. and Lavorel, S. and Albert, C. H. and Thuiller, W. and Grigulis, K. and Dolezal, J. and Janeček, Š. and Lepš, J.},
  title = {Quantifying the relevance of intraspecific trait variability for functional diversity},
  journal = {Methods in Ecology and Evolution},
  year = {2011},
  volume = {2},
  number = {2},
  pages = {163--174},
  doi = {10.1111/j.2041-210X.2010.00071.x},
  note = {access: not_obtained (Crossref metadata only); listed twice under Sources not obtained; not cited}
}
@article{hadfieldGeneralQuantitativeGenetic2010,
  author = {Hadfield, J. D. and Nakagawa, S.},
  title = {General quantitative genetic methods for comparative biology: phylogenies, taxonomies and multi-trait models for continuous and categorical characters},
  journal = {Journal of Evolutionary Biology},
  year = {2010},
  volume = {23},
  number = {3},
  pages = {494--508},
  doi = {10.1111/j.1420-9101.2009.01915.x},
  note = {access: not_obtained (Europe PMC abstract read; full text not attempted); listed twice under Sources not obtained; not cited}
}
@article{neyretSlowfastTraitContinuum2024,
  author = {Neyret, M. and Le Provost, G. and Boesing, A. L.},
  title = {A slow-fast trait continuum at the whole community level in relation to land-use intensification},
  journal = {Nature Communications},
  year = {2024},
  volume = {15},
  pages = {1251},
  doi = {10.1038/s41467-024-45113-5},
  note = {access: not_obtained, listed under Sources not obtained, although the note says the Europe PMC full text XML (PMC10858939) was obtained and grepped (conflict within the note's list); not entered as a finding by the note; incomplete: author (listed as et al.), number}
}
@article{faustMicrobialInteractionsNetworks2012,
  author = {Faust, K. and Raes, J.},
  title = {Microbial interactions: from networks to models},
  journal = {Nature Reviews Microbiology},
  year = {2012},
  volume = {10},
  number = {8},
  pages = {538--550},
  doi = {10.1038/nrmicro2832},
  note = {access: not_obtained (Crossref citation and DOI verification only; not read); listed under Sources not obtained together with Röttjers & Faust 2018; not cited}
}
@article{rottjersHairballsHypothesesbiologicalInsights2018,
  author = {Röttjers, L. and Faust, K.},
  title = {From hairballs to hypotheses: biological insights from microbial networks},
  journal = {FEMS Microbiology Reviews},
  year = {2018},
  volume = {42},
  number = {6},
  pages = {761--780},
  doi = {10.1093/femsre/fuy030},
  note = {access: not_obtained (Crossref citation and DOI verification only; not read); listed under Sources not obtained together with Faust & Raes 2012; not cited}
}
@article{goldfordEmergentSimplicityMicrobial2018,
  author = {Goldford, J. E. and Lu, N. and Bajić, D. and Estrela, S. and Tikhonov, M. and Sanchez-Gorostiaga, A. and Segrè, D. and Mehta, P. and Sanchez, A.},
  title = {Emergent simplicity in microbial community assembly},
  journal = {Science},
  year = {2018},
  volume = {361},
  number = {6401},
  pages = {469--474},
  doi = {10.1126/science.aat1168},
  note = {access: abstract_only; cited as: H2-04 [11b]; also listed under Sources not obtained, full text PMC6405290 not reached (conflict between the note's lists)}
}
@article{hawkinsStructuralBiasAggregated2017,
  author = {Hawkins, B. A. and Leroy, B. and {Rodríguez MÁ} and Singer, A. and Vilela, B. and Villalobos, F. and Wang, X. and Zelený, D.},
  title = {Structural bias in aggregated species-level variables driven by repeated species co-occurrences: a pervasive problem in community and assemblage data},
  journal = {Journal of Biogeography},
  year = {2017},
  volume = {44},
  number = {6},
  pages = {1199--1211},
  doi = {10.1111/jbi.12953},
  note = {access: abstract_only; cited as: H2-04 [12]}
}
@article{kishoreInferringMicrobialCooccurrence2023,
  author = {Kishore, D. and Birzu, G. and Hu, Z. and DeLisi, C. and Korolev, K. S. and Segrè, D.},
  title = {Inferring microbial co-occurrence networks from amplicon data: a systematic evaluation},
  journal = {mSystems},
  year = {2023},
  volume = {8},
  number = {4},
  pages = {e00961--22},
  doi = {10.1128/msystems.00961-22},
  note = {access: full_text; cited as: H2-04 [13]; critic: H2-04:C-077, volume 8 and issue 4 are not in the Crossref record}
}
@article{jiangFunctionalBiogeographyOcean2012,
  author = {Jiang, X. and Langille, M. G. I. and Neches, R. Y. and Elliot, M. and Levin, S. A. and Eisen, J. A. and Weitz, J. S. and Dushoff, J.},
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
  author = {Kamneva, O. K.},
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
  author = {Kurtz, Z. D. and Müller, C. L. and Miraldi, E. R. and Littman, D. R. and Blaser, M. J. and Bonneau, R. A.},
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
  author = {Kembel, S. W. and Cahill, J. F.},
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
  author = {Levy, R. and Borenstein, E.},
  title = {Metabolic modeling of species interaction in the human microbiome elucidates community-level assembly rules},
  journal = {Proceedings of the National Academy of Sciences of the United States of America},
  year = {2013},
  volume = {110},
  number = {31},
  pages = {12804--12809},
  doi = {10.1073/pnas.1300926110},
  note = {access: secondary (critic: H2-04:C-053, a model's summary of a paper is closer to secondary; the note said FT-s, full text read through a web-fetch tool summary, quotes to be rechecked); cited as: H2-04 [17]}
}
@article{limamendezDeterminantsCommunityStructure2015,
  author = {Lima-Mendez, G. and Faust, K. and Henry, N. and Decelle, J. and Colin, S. and Carcillo, F. and Chaffron, S. and Ignacio-Espinosa, J. C. and Roux, S. and Vincent, F. and Bittner, L. and Darzi, Y. and Wang, J. and Audic, S. and Berline, L. and Bontempi, G. and Cabello, A. M. and Coppola, L. and Cornejo-Castillo, F. M. and d'Ovidio, F. and De Meester, L. and Ferrera, I. and Garet-Delmas, M. J. and Guidi, L. and Lara, E. and Pesant, S. and Royo-Llonch, M. and Salazar, G. and Sánchez, P. and Sebastian, M. and Souffreau, C. and Dimier, C. and Picheral, M. and Searson, S. and Kandels-Lewis, S. and {Tara Oceans coordinators} and Gorsky, G. and Not, F. and Ogata, H. and Speich, S. and Stemmann, L. and Weissenbach, J. and Wincker, P. and Acinas, S. G. and Sunagawa, S. and Bork, P. and Sullivan, M. B. and Karsenti, E. and Bowler, C. and de Vargas, C. and Raes, J.},
  title = {Determinants of community structure in the global plankton interactome},
  journal = {Science},
  year = {2015},
  volume = {348},
  number = {6237},
  pages = {1262073},
  doi = {10.1126/science.1262073},
  note = {access: abstract_only; cited as: H2-04 [17a]; also listed under Sources not obtained (conflict between the note's lists)}
}
@article{metahitIdentificationAssemblyGenomes2014,
  author = {{MetaHIT Consortium} and Nielsen, H. B. and Almeida, M. and Juncker, A. S. and Rasmussen, S. and Li, J. and Sunagawa, S. and Plichta, D. R. and Gautier, L. and Pedersen, A. G. and Le Chatelier, E. and Pelletier, E. and Bonde, I. and Nielsen, T. and Manichanh, C. and Arumugam, M. and Batto, J. M. and Quintanilha dos Santos, M. B. and Blom, N. and Borruel, N. and Burgdorf, K. S. and Boumezbeur, F. and Casellas, F. and Doré, J. and Dworzynski, P. and Guarner, F. and Hansen, T. and Hildebrand, F. and Kaas, R. S. and Kennedy, S. and Kristiansen, K. and Kultima, J. R. and Léonard, P. and Levenez, F. and Lund, O. and Moumen, B. and Le Paslier, D. and Pons, N. and Pedersen, O. and Prifti, E. and Qin, J. and Raes, J. and Sørensen, S. and Tap, J. and Tims, S. and Ussery, D. W. and Yamada, T. and Renault, P. and Sicheritz-Ponten, T. and Bork, P. and Wang, J. and Brunak, S. and Ehrlich, S. D.},
  title = {Identification and assembly of genomes and genetic elements in complex metagenomic samples without using reference genomes},
  journal = {Nature Biotechnology},
  year = {2014},
  volume = {32},
  number = {8},
  pages = {822--828},
  doi = {10.1038/nbt.2939},
  note = {access: abstract_only; cited as: H2-04 [18]; Crossref lists MetaHIT Consortium first (note's search record)}
}
@article{morrisBlackQueenHypothesis2012,
  author = {Morris, J. J. and Lenski, R. E. and Zinser, E. R.},
  title = {The Black Queen Hypothesis: evolution of dependencies through adaptive gene loss},
  journal = {mBio},
  year = {2012},
  volume = {3},
  number = {2},
  pages = {e00036--12},
  doi = {10.1128/mBio.00036-12},
  note = {access: abstract_only; cited as: H2-04 [18a]}
}
@article{loucaDecouplingFunctionTaxonomy2016,
  author = {Louca, S. and Parfrey, L. W. and Doebeli, M.},
  title = {Decoupling function and taxonomy in the global ocean microbiome},
  journal = {Science},
  year = {2016},
  volume = {353},
  number = {6305},
  pages = {1272--1277},
  doi = {10.1126/science.aaf4507},
  note = {access: abstract_only; cited as: H2-04 [18b]}
}
@article{machadoPolarizationMicrobialCommunities2021,
  author = {Machado, D. and Maistrenko, O. M. and Andrejev, S. and Kim, Y. and Bork, P. and Patil, Kaustubh R. and Patil, Kiran R.},
  title = {Polarization of microbial communities between competitive and cooperative metabolism},
  journal = {Nature Ecology & Evolution},
  year = {2021},
  volume = {5},
  number = {2},
  pages = {195--203},
  doi = {10.1038/s41559-020-01353-4},
  note = {access: full_text; cited as: H2-04 [19]; authors Patil KR, Patil KR resolved by the critic (H2-04:C-076: Kaustubh R. Patil and Kiran R. Patil)}
}
@article{marslandMinimalModelMicrobial2020,
  author = {Marsland, R. and Cui, W. and Mehta, P.},
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
  author = {Kehe, J. and Ortiz, A. and Kulesa, A. and Gore, J. and Blainey, P. C. and Friedman, J.},
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
  author = {Messier, J. and McGill, B. J. and Lechowicz, M. J.},
  title = {How do traits vary across ecological scales? A case for trait-based ecology},
  journal = {Ecology Letters},
  year = {2010},
  volume = {13},
  number = {7},
  pages = {838--848},
  doi = {10.1111/j.1461-0248.2010.01476.x},
  note = {access: abstract_only; cited as: H2-04 [20a]}
}
@article{messierTraitVariationIntegration2016,
  author = {Messier, J. and McGill, B. J. and Enquist, B. J. and Lechowicz, M. J.},
  title = {Trait variation and integration across scales: is the leaf economic spectrum present at local scales?},
  journal = {Ecography},
  year = {2017},
  volume = {40},
  number = {6},
  pages = {685--697},
  doi = {10.1111/ecog.02006},
  note = {access: abstract_only; cited as: H2-04 [20b]}
}
@article{loucaFunctionFunctionalRedundancy2018,
  author = {Louca, S. and Polz, M. F. and Mazel, F. and Albright, M. B. N. and Huber, J. A. and O'Connor, M. I. and Ackermann, M. and Hahn, A. S. and Srivastava, D. S. and Crowe, S. A. and Doebeli, M. and Parfrey, L. W.},
  title = {Function and functional redundancy in microbial systems},
  journal = {Nature Ecology & Evolution},
  year = {2018},
  volume = {2},
  number = {6},
  pages = {936--943},
  doi = {10.1038/s41559-018-0519-1},
  note = {access: abstract_only; cited as: H2-04 [21]; not cited (critic: H2-04:C-078)}
}
@article{osnasDivergentDriversLeaf2018,
  author = {Osnas, J. L. D. and Katabuchi, M. and Kitajima, K. and Wright, S. J. and Reich, P. B. and Van Bael, S. A. and Kraft, N. J. B. and Samaniego, M. J. and Pacala, S. W. and Lichstein, J. W.},
  title = {Divergent drivers of leaf trait variation within species, among species, and among functional groups},
  journal = {Proceedings of the National Academy of Sciences of the United States of America},
  year = {2018},
  volume = {115},
  number = {21},
  pages = {5480--5485},
  doi = {10.1073/pnas.1803989115},
  note = {access: full_text; cited as: H2-04 [22]}
}
@article{ovaskainenHowMakeMore2017,
  author = {Ovaskainen, O. and Tikhonov, G. and Norberg, A. and Blanchet, F. G. and Duan, L. and Dunson, D. and Roslin, T. and Abrego, N.},
  title = {How to make more out of community data? A conceptual framework and its implementation as models and software},
  journal = {Ecology Letters},
  year = {2017},
  volume = {20},
  number = {5},
  pages = {561--576},
  doi = {10.1111/ele.12757},
  note = {access: abstract_only; cited as: H2-04 [22a]}
}
@article{pitonLifeHistoryStrategies2023,
  author = {Piton, G. and Allison, S. D. and Bahram, M. and Hildebrand, F. and Martiny, J. B. H. and Treseder, K. K. and Martiny, A. C.},
  title = {Life history strategies of soil bacterial communities across global terrestrial biomes},
  journal = {Nature Microbiology},
  year = {2023},
  volume = {8},
  number = {11},
  pages = {2093--2102},
  doi = {10.1038/s41564-023-01465-0},
  note = {access: full_text (accepted manuscript); cited as: H2-04 [23]; critic: H2-04:C-057..059, the figures could not be rechecked (open copies returned HTML)}
}
@article{peresnetoLinkingTraitVariation2017,
  author = {Peres-Neto, P. R. and Dray, S. and ter Braak, C. J. F.},
  title = {Linking trait variation to the environment: critical issues with community-weighted mean correlation resolved by the fourth-corner approach},
  journal = {Ecography},
  year = {2017},
  volume = {40},
  number = {7},
  pages = {806--816},
  doi = {10.1111/ecog.02302},
  note = {access: abstract_only; cited as: H2-04 [23a]; title corrected (critic: H2-04:C-071, the note had 'resolved by the fourth-corner approach')}
}
@article{puglielliIntraspecificVariabilityLeaf2024,
  author = {Puglielli, G. and Bricca, A. and Chelli, S. and Petruzzellis, F. and Acosta, A. T. R. and Bacaro, G. and Beccari, E. and Bernardo, L. and Bonari, G. and Bolpagni, R. and Boscutti, F. and Calvia, G. and Campetella, G. and Cancellieri, L. and Canullo, R. and Carbognani, M. and Carboni, M. and Carranza, M. L. and Castellani, M. B. and Ciccarelli, D. and Coppi, A. and Cutini, M. and Dalla Vecchia, A. and Dalle Fratte, M. and de Francesco, M. C. and De Frenne, P. and De Sanctis, M. and de Simone, L. and Di Cecco, V. and Fanelli, G. and Farris, E. and Ferrara, A. and Fenu, G. and Filibeck, G. and Gasperini, C. and Gargano, D. and Kindermann, E. and La Bella, G. and Lastrucci, L. and Lazzaro, L. and Maccherini, S. and Marignani, M. and Mugnai, M. and Naselli-Flores, L. and Passalacqua, N. G. and Pavanetto, N. and Petraglia, A. and Rota, F. and Santoianni, L. A. and Schettino, A. and Selvi, F. and Stanisci, A. and Trotta, G. and Vangansbeke, P. and Varricchione, M. and Vuerich, M. and Wellstein, C. and Tordoni, E.},
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
  author = {Puglielli, G. and Carmona, C. P. and Bissi, A. and Tordoni, E.},
  title = {Quantifying the influence of intraspecific variability in trait spaces},
  journal = {npj Biodiversity},
  year = {2025},
  volume = {4},
  pages = {36},
  doi = {10.1038/s44185-025-00101-w},
  note = {access: full_text; cited as: H2-04 [24b]}
}
@article{poggiatoInterpretationsJointModeling2021,
  author = {Poggiato, G. and Münkemüller, T. and Bystrova, D. and Arbel, J. and Clark, J. S. and Thuiller, W.},
  title = {On the interpretations of joint modeling in community ecology},
  journal = {Trends in Ecology & Evolution},
  year = {2021},
  volume = {36},
  number = {5},
  pages = {391--401},
  doi = {10.1016/j.tree.2021.01.002},
  note = {access: abstract_only; cited as: H2-04 [24c]}
}
@article{pachecoCostlessMetabolicSecretions2019,
  author = {Pacheco, A. R. and Moel, M. and Segrè, D.},
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
  author = {Price, M. N. and Zane, G. M. and Kuehl, J. V. and Melnyk, R. A. and Wall, J. D. and Deutschbauer, A. M. and Arkin, A. P.},
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
  author = {Smillie, C. S. and Smith, M. B. and Friedman, J. and Cordero, O. X. and David, L. A. and Alm, E. J.},
  title = {Ecology drives a global network of gene exchange connecting the human microbiome},
  journal = {Nature},
  year = {2011},
  volume = {480},
  number = {7376},
  pages = {241--244},
  doi = {10.1038/nature10571},
  note = {access: abstract_only; cited as: H2-04 [26]}
}
@article{siefertGlobalMetaanalysisRelative2015,
  author = {Siefert, A. and Violle, C. and Chalmandrier, L. and Albert, C. H. and Taudiere, A. and Fajardo, A. and Aarssen, L. W. and Baraloto, C. and Carlucci, M. B. and Cianciaruso, M. V. and Dantas, V. L. and de Bello, F. and Duarte, L. D. S. and Fonseca, C. R. and Freschet, G. T. and Gaucherand, S. and Gross, N. and Hikosaka, K. and Jackson, B. and Jung, V. and Kamiyama, C. and Katabuchi, M. and Kembel, S. W. and Kichenin, E. and Kraft, N. J. B. and Lagerström, A. and Le Bagousse-Pinguet, Y. and Li, Y. and Mason, N. and Messier, J. and Nakashizuka, T. and Overton, J. M. and Peltzer, D. A. and Pérez-Ramos, I. M. and Pillar, V. D. and Prentice, H. C. and Richardson, S. and Sasaki, T. and Schamp, B. S. and Schöb, C. and Shipley, B. and Sundqvist, M. and Sykes, M. T. and Vandewalle, M. and Wardle, D. A.},
  title = {A global meta-analysis of the relative extent of intraspecific trait variation in plant communities},
  journal = {Ecology Letters},
  year = {2015},
  volume = {18},
  number = {12},
  pages = {1406--1419},
  doi = {10.1111/ele.12508},
  note = {access: abstract_only; cited as: H2-04 [27]}
}
@article{russelAntagonismCorrelatesMetabolic2017,
  author = {Russel, J. and Røder, H. L. and Madsen, J. S. and Burmølle, M. and Sørensen, S. J.},
  title = {Antagonism correlates with metabolic similarity in diverse bacteria},
  journal = {Proceedings of the National Academy of Sciences of the United States of America},
  year = {2017},
  volume = {114},
  number = {40},
  pages = {10684--10688},
  doi = {10.1073/pnas.1706016114},
  note = {access: secondary (critic: H2-04:C-053, a model's summary of a paper is closer to secondary; the note said FT-s, full text read through a web-fetch tool summary, quotes to be rechecked); cited as: H2-04 [28]}
}
@article{starkeAminoAcidAuxotrophies2023,
  author = {Starke, S. and Harris, D. M. M. and Zimmermann, J. and Schuchardt, S. and Oumari, M. and Frank, D. and Bang, C. and Rosenstiel, P. and Schreiber, S. and Frey, N. and Franke, A. and Aden, K. and Waschina, S.},
  title = {Amino acid auxotrophies in human gut bacteria are linked to higher microbiome diversity and long-term stability},
  journal = {The ISME Journal},
  year = {2023},
  volume = {17},
  number = {12},
  pages = {2370--2380},
  doi = {10.1038/s41396-023-01537-3},
  note = {access: full_text; cited as: H2-04 [29]}
}
@article{tianDecipheringFunctionalRedundancy2020,
  author = {Tian, L. and Wang, X. W. and Wu, A. K. and Fan, Y. and Friedman, J. and Dahlin, A. and Waldor, M. K. and Weinstock, G. M. and Weiss, S. T. and Liu, Y. Y.},
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
  author = {Weiss, S. and Van Treuren, W. and Lozupone, C. and Faust, K. and Friedman, J. and Deng, Y. and Xia, L. C. and Xu, Z. Z. and Ursell, L. and Alm, E. J. and Birmingham, A. and Cram, J. A. and Fuhrman, J. A. and Raes, J. and Sun, F. and Zhou, J. and Knight, R.},
  title = {Correlation detection strategies in microbial data sets vary widely in sensitivity and precision},
  journal = {The ISME Journal},
  year = {2016},
  volume = {10},
  number = {7},
  pages = {1669--1681},
  doi = {10.1038/ismej.2015.235},
  note = {access: full_text; cited as: H2-04 [31]; critic: H2-04:C-060, figures unverified (PMC XML not retrievable in the critique)}
}
@article{wieczynskiClimateShapesShifts2018,
  author = {Wieczynski, D. J. and Boyle, B. and Buzzard, V. and Duran, S. M. and Henderson, A. N. and Hulshof, C. M. and Kerkhoff, A. J. and McCarthy, M. C. and Michaletz, S. T. and Swenson, N. G. and Asner, G. P. and Bentley, L. P. and Enquist, B. J. and Savage, V. M.},
  title = {Climate shapes and shifts functional biodiversity in forests worldwide},
  journal = {Proceedings of the National Academy of Sciences of the United States of America},
  year = {2019},
  volume = {116},
  number = {2},
  pages = {587--592},
  doi = {10.1073/pnas.1813723116},
  note = {access: abstract_only; cited as: H2-04 [32]}
}
@article{violleReturnVarianceIntraspecific2012,
  author = {Violle, C. and Enquist, B. J. and McGill, B. J. and Jiang, L. and Albert, C. H. and Hulshof, C. and Jung, V. and Messier, J.},
  title = {The return of the variance: intraspecific variability in community ecology},
  journal = {Trends in Ecology & Evolution},
  year = {2012},
  volume = {27},
  number = {4},
  pages = {244--252},
  doi = {10.1016/j.tree.2011.11.014},
  note = {access: abstract_only; cited as: H2-04 [32a]}
}
@article{westobyCellSizeGenome2021,
  author = {Westoby, M. and Nielsen, D. A. and Gillings, M. R. and Litchman, E. and Madin, J. S. and Paulsen, I. T. and Tetu, S. G.},
  title = {Cell size, genome size, and maximum growth rate are near-independent dimensions of ecological variation across bacteria and archaea},
  journal = {Ecology and Evolution},
  year = {2021},
  volume = {11},
  number = {9},
  pages = {3956--3976},
  doi = {10.1002/ece3.7290},
  note = {access: full_text; cited as: H2-04 [33]}
}
@article{vieirasilvaSystemicImprintGrowth2010,
  author = {Vieira-Silva, S. and Rocha, E. P. C.},
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
  author = {Westoby, M. and Gillings, M. R. and Madin, J. S. and Nielsen, D. A. and Paulsen, I. T. and Tetu, S. G.},
  title = {Trait dimensions in bacteria and archaea compared to vascular plants},
  journal = {Ecology Letters},
  year = {2021},
  volume = {24},
  number = {7},
  pages = {1487--1504},
  doi = {10.1111/ele.13742},
  note = {access: abstract_only; cited as: H2-04 [33b]; not cited (critic: H2-04:C-078)}
}
@article{zhouFunctionalMolecularEcological2010,
  author = {Zhou, J. and Deng, Y. and Luo, F. and He, Z. and Tu, Q. and Zhi, X.},
  title = {Functional molecular ecological networks},
  journal = {mBio},
  year = {2010},
  volume = {1},
  number = {4},
  pages = {e00169--10},
  doi = {10.1128/mBio.00169-10},
  note = {access: full_text; cited as: H2-04 [34]}
}
@article{wrightWorldwideLeafEconomics2004,
  author = {Wright, I. J. and Reich, P. B. and Westoby, M. and Ackerly, D. D. and Baruch, Z. and Bongers, F. and Cavender-Bares, J. and Chapin, T. and Cornelissen, J. H. C. and Diemer, M. and Flexas, J. and Garnier, E. and Groom, P. K. and Gulias, J. and Hikosaka, K. and Lamont, B. B. and Lee, T. and Lee, W. and Lusk, C. and Midgley, J. J. and Navas, M. L. and {Niinemets Ü} and Oleksyn, J. and Osada, N. and Poorter, H. and Poot, P. and Prior, L. and Pyankov, V. I. and Roumet, C. and Thomas, S. C. and Tjoelker, M. G. and Veneklaas, E. J. and Villar, R.},
  title = {The worldwide leaf economics spectrum},
  journal = {Nature},
  year = {2004},
  volume = {428},
  number = {6985},
  pages = {821--827},
  doi = {10.1038/nature02403},
  note = {access: abstract_only; cited as: H2-04 [34a]}
}
@article{zelenyWhichResultsStandard2018,
  author = {Zelený, D.},
  title = {Which results of the standard test for community-weighted mean approach are too optimistic?},
  journal = {Journal of Vegetation Science},
  year = {2018},
  volume = {29},
  number = {6},
  pages = {953--966},
  doi = {10.1111/jvs.12688},
  note = {access: abstract_only (via bioRxiv preprint abstract doi:10.1101/349589); cited as: H2-04 [35]}
}
@article{zelezniakMetabolicDependenciesDrive2015,
  author = {Zelezniak, A. and Andrejev, S. and Ponomarova, O. and Mende, D. R. and Bork, P. and Patil, K. R.},
  title = {Metabolic dependencies drive species co-occurrence in diverse microbial communities},
  journal = {Proceedings of the National Academy of Sciences of the United States of America},
  year = {2015},
  volume = {112},
  number = {20},
  pages = {6449--6454},
  doi = {10.1073/pnas.1421834112},
  note = {access: secondary (critic: H2-04:C-053, a model's summary of a paper is closer to secondary; the note said FT-s, full text read through a web-fetch tool summary, quotes to be rechecked); cited as: H2-04 [36]}
}
@article{zurellDoJointSpecies2018,
  author = {Zurell, D. and Pollock, L. J. and Thuiller, W.},
  title = {Do joint species distribution models reliably detect interspecific interactions from co-occurrence data in homogenous environments?},
  journal = {Ecography},
  year = {2018},
  volume = {41},
  number = {11},
  pages = {1812--1819},
  doi = {10.1111/ecog.03315},
  note = {access: abstract_only; cited as: H2-04 [37]}
}
@article{gusevaDiversityComplexityMicrobial2022,
  author = {Guseva, K. and Darcy, S. and Simon, E. and Alteio, L. V. and Montesinos-Navarro, A. and Kaiser, C.},
  title = {From diversity to complexity: Microbial networks in soils},
  journal = {Soil Biology and Biochemistry},
  year = {2022},
  volume = {169},
  pages = {108604},
  doi = {10.1016/j.soilbio.2022.108604},
  note = {access: full_text; cited as: H2-04 [38]; not cited in the body, annotated in the reference list (critic: H2-04:C-078)}
}
@article{pascualgarciaBacteriaDialogSanta2014,
  author = {Pascual-García, A. and Tamames, J. and Bastolla, U.},
  title = {Bacteria dialog with Santa Rosalia: Are aggregations of cosmopolitan bacteria mainly explained by habitat filtering or by ecological interactions?},
  journal = {BMC Microbiology},
  year = {2014},
  volume = {14},
  number = {1},
  pages = {284},
  doi = {10.1186/s12866-014-0284-5},
  note = {access: full_text; cited as: H2-04 [39]; not cited in the body, annotated in the reference list (critic: H2-04:C-078)}
}
@article{manorSystematicCharacterizationAnalysis2017,
  author = {Manor, O. and Borenstein, E.},
  title = {Systematic characterization and analysis of the taxonomic drivers of functional shifts in the human microbiome},
  journal = {Cell Host & Microbe},
  year = {2017},
  volume = {21},
  number = {2},
  pages = {254--267},
  doi = {10.1016/j.chom.2016.12.014},
  note = {access: abstract_only; cited as: H2-04 [40]; not cited in the body, annotated in the reference list (critic: H2-04:C-078)}
}
@article{gloorMicrobiomeDatasetsCompositional2017,
  author = {Gloor, Gregory B. and Macklaim, Jean M. and Pawlowsky-Glahn, Vera and Egozcue, Juan J.},
  title = {Microbiome Datasets Are Compositional: And This Is Not Optional},
  journal = {Frontiers in Microbiology},
  year = {2017},
  volume = {8},
  pages = {2224},
  doi = {10.3389/fmicb.2017.02224},
  note = {background; checked on Crossref and the publisher's abstract}
}
@article{garnierPlantFunctionalMarkers2004,
  author = {Garnier, Eric and Cortez, Jacques and Billès, Georges and Navas, Marie-Laure and Roumet, Catherine and Debussche, Max and Laurent, Gérard and Blanchard, Alain and Aubry, David and Bellmann, Astrid and Neill, Cathy and Toussaint, Jean-Patrick},
  title = {Plant Functional Markers Capture Ecosystem Properties During Secondary Succession},
  journal = {Ecology},
  year = {2004},
  volume = {85},
  number = {9},
  pages = {2630--2637},
  doi = {10.1890/03-0799},
  note = {background; checked on Crossref and the abstract (AGRIS record)}
}
```
