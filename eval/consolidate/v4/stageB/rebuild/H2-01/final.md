---
type: knowledge
title: Dimensionality and cross-habitat stability of microbial functional profiles
inputs:
  - H2-01: PhD/Proposal/Research/Results/Dimensionality of microbial functional profiles, and the cross-habitat stability of functional covariation, function levels and taxonomic composition a literature review.md
refs: PhD/Proposal/Refs/Refs.bib
built: 2026-10-23
status: draft
tags:
  - research
  - knowledge
---
# Dimensionality and cross-habitat stability of microbial functional profiles

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
| H2-01 | [[Dimensionality of microbial functional profiles, and the cross-habitat stability of functional covariation, function levels and taxonomic composition a literature review]] | yes | labelled (access; class; standing) | yes (14 of 39 labels) | no | exact (every labelled sentence, every answer sentence, and the critique) |

## Concepts

### evidence-bodies: the bodies of work that bear on the questions
needs: none
- **evidence-bodies.1** Three bodies of work bear on the questions: metagenomics supplies sample-by-function matrices (KEGG orthologues, pathways, modules, Pfams, eggNOG groups) from shotgun data; trait ecology supplies community-weighted means (CWMs) and species-by-trait matrices, mostly from plants; and other fields that profile many correlated features, chiefly transcriptomics, supply most of the explicit held-out tests of learned covariation.
  conf: not stated · class: not stated · holds: the review's account of the literature it covered · src: none (the reviewer's account of the literature) · trail: H2-01 §1. What · from: H2-01:B-0028..0031
- **evidence-bodies.2** The three bodies have asked different questions: metagenomics has mostly compared levels of functions with taxonomic composition; trait ecology has asked about the dimensionality and covariation of traits, and sometimes how covariation shifts along gradients; transcriptomics has asked whether covariation learned in one tissue or study reproduces another.
  conf: not stated · class: not stated · holds: the review's account of the literature it covered · src: none (the reviewer's account of the literature) · trail: H2-01 §1. What · from: H2-01:B-0032..0035
- **evidence-bodies.3** The core cases of the questions are thinly covered: most of the evidence is either direct evidence on a neighbouring quantity or evidence from another field, and each is labelled as such.
  conf: not stated · class: not stated · holds: the review's account of the literature it covered · src: none (the reviewer's account of the literature) · trail: H2-01 §1. What · from: H2-01:B-0036, H2-01:B-0040, H2-01:B-0041
- **evidence-bodies.4** A second reader judged the review careful on the whole: it labels most indirect evidence and keeps the core microbial cases (withheld habitat, cross-habitat covariation stability, case C) as not found.
  conf: not stated · class: not stated · holds: the critic's overall assessment of the review · src: none (the critic's assessment) · trail: H2-01 §critic · from: H2-01:C-044, H2-01:C-045

### shared-mean-profile: a dominant shared mean profile
needs: none
- **shared-mean-profile.1** Per-sample Spearman correlations between predicted and measured KEGG gene profiles (0.53 to 0.87) barely changed when each gene's abundance was permuted across samples (soil example: 0.85 unpermuted, 0.84 permuted); the authors conclude that functional profiles vary little between samples relative to their mean.
  conf: not stated · class: meas (marker) · holds: a per-sample prediction-accuracy metric for predicted against measured KEGG gene profiles; the critic: not a decomposition that measures how much of a sample-by-function matrix is a mean profile, and from human-associated and a few soil datasets · src: sunInferenceBasedAccuracyMetagenome2020 (FT; measured) · trail: H2-01 §2.2, §critic · from: H2-01:I-0006, H2-01:B-0061, H2-01:C-003, H2-01:C-005
- **shared-mean-profile.2** The Human Microbiome Project consortium reports pathway relative abundances "much more constant and evenly diverse" than organismal abundances across individuals within body sites, with a stable housekeeping core.
  conf: not stated · class: meas (marker) · holds: human body sites (HMP); the critic: "much more constant" is a quoted descriptive statement with no quantitative figure, which the review treats as measured evidence of equal weight · src: theStructureFunctionDiversity2012 (FT; measured) · trail: H2-01 §2.2, §4.1, §critic, §Adversarial · from: H2-01:I-0007, H2-01:I-0027, H2-01:C-004, H2-01:C-022, H2-01:C-069
- **shared-mean-profile.3** In a reference network of 796 human-associated genomes by 7,105 KOs, a nested structure, with many KOs carried by most genomes, makes community functional profiles conserved even when taxa vary.
  conf: single (marker) · class: deriv/model (marker) · holds: a genome-content network model of human-associated genomes, offered as a mechanistic account · src: tianDecipheringFunctionalRedundancy2020 (FT; derived/modelled; SINGLE SOURCE) · trail: H2-01 §2.2, §answers · from: H2-01:B-0062, H2-01:I-0008, H2-01:A-056
- **shared-mean-profile.4** The review reads two findings (the permutation result for a per-sample accuracy metric and the HMP statement that pathways are more constant than taxa) as suggesting that much of the apparent low dimensionality of raw functional profiles is a shared mean; the critic holds that they support only this: in these datasets, per-sample functional profiles are highly similar to one another.
  conf: not stated · class: not stated · holds: human-associated and a few soil datasets; neither finding is a decomposition that measures how much of a sample-by-function matrix is a mean profile · src: sunInferenceBasedAccuracyMetagenome2020, theStructureFunctionDiversity2012 · trail: H2-01 §2.2, §critic · from: H2-01:B-0060, H2-01:C-002..006

### processing-effects: normalisation, genome size, gene-set aggregation and compositional closure
needs: none
- **processing-effects.bg1** Compositional data are proportions of some whole; their sample space is the simplex, and their statistical analysis has needed methods of its own.
  kind: background · ref: aitchisonStatisticalAnalysisCompositional1982 · check: DOI 10.1111/j.2517-6161.1982.tb01195.x resolves on Crossref; stated in the first two sentences of the abstract
- **processing-effects.1** Relative (sum-to-one) normalisation introduces a sample-level factor shared by all genes.
  conf: not stated · class: not stated · holds: relative normalisation of functional profiles · src: none (the note cites no source for this sentence) · trail: H2-01 §2.3 · from: H2-01:B-0067
- **processing-effects.2** The relative abundance of universal single-copy genes correlated with average genome size at R = −0.78 across HMP body sites and −0.82 in stool.
  conf: not stated · class: meas (marker) · holds: HMP body sites and stool · src: manorMUSiCCMarkerGenes2015 (FT; measured) · trail: H2-01 §2.3 · from: H2-01:I-0009
- **processing-effects.3** Species abundance explained 74% of average-genome-size variation across HMP samples, and genome-size variation makes genes at equal per-cell copy number look variable and hides real per-cell variation, so genome size makes stable genes look variable and variable genes look stable.
  conf: not stated · class: meas (marker) · holds: HMP samples · src: nayfachAverageGenomeSize2015 (FT per metagenomics angle, AB per statistics angle; measured) · trail: H2-01 §2.3, §answers · from: H2-01:I-0010, H2-01:A-058
- **processing-effects.4** In soils, genome size tracked the ratio of polysaccharide-decomposition to biomass-synthesis genes across 2,650 genomes and a continental survey.
  conf: not stated · class: not stated · holds: soil bacteria; 2,650 genomes and a continental survey · src: wuGlobalRelationshipGenome2025 (AB) · trail: H2-01 §2.3 · from: H2-01:R-0258, H2-01:B-0068
- **processing-effects.5** In HMP gut samples, single-copy-gene (marker-gene) normalisation raised pathway coefficients of variation relative to relative normalisation, uniform mapping of KOs shared among pathways gave less variable pathway profiles than a sample-specific mapping, and aggregating KOs into KEGG pathways lowered variability relative to aggregates built from genome co-occurrence.
  conf: single (note: "SINGLE SOURCE for this set of quantities") · class: meas (note: "What is measured") · holds: HMP gut samples; across-sample variability of pathway profiles; the only measured test of aggregation and shared-member mapping · src: manorRevisedComputationalMetagenomic2017 (FT) · trail: H2-01 §2.3, §answers · from: H2-01:B-0072..0074, H2-01:B-0076, H2-01:B-0077, H2-01:A-008, H2-01:A-028, H2-01:A-067
- **processing-effects.6** On average 9.5% of gene-family pairs within the same KEGG pathway were negatively correlated (R < −0.3).
  conf: not stated · class: not stated · holds: HMP gut samples · src: manorRevisedComputationalMetagenomic2017 (FT) · trail: H2-01 §2.3 · from: H2-01:B-0072, H2-01:B-0073, H2-01:B-0075
- **processing-effects.7** Manor and Borenstein (2017) conclude that reported functional uniformity is partly a processing artefact, and call perceived functional uniformity "a potential misconception".
  conf: not stated · class: not stated · holds: HMP gut samples · src: manorRevisedComputationalMetagenomic2017 (FT) · trail: H2-01 §2.3, §critic · from: H2-01:B-0072, H2-01:B-0073, H2-01:B-0077, H2-01:C-025
- **processing-effects.8** Naive mapping of a gene family to every pathway containing it inflates pathway counts.
  conf: not stated · class: not stated · holds: pathway reconstruction, mapping gene families to pathways · src: yeParsimonyApproachBiological2009 (AB) · trail: H2-01 §2.3 · from: H2-01:R-0261, H2-01:B-0078, H2-01:A-008
- **processing-effects.9** In transcriptomics, pathways sharing genes shift each other's significance ("crosstalk").
  conf: not stated · class: not stated · holds: pathway significance analysis in transcriptomics, another field · src: donatoAnalysisCorrectionCrosstalk2013 (AB; other field) · trail: H2-01 §2.3 · from: H2-01:B-0079
- **processing-effects.10** Correlation is not a valid association measure for relative data; proportionality is offered instead.
  conf: not stated · class: not stated · holds: relative (compositional) data, from another field · src: lovellProportionalityValidAlternative2015 (AB; other field) · trail: H2-01 §2.3 · from: H2-01:B-0082, H2-01:A-008

### community-weighted-means: community-weighted means and abundance weighting
needs: none
- **community-weighted-means.bg1** A community-weighted (community-aggregated) trait value weights each species' trait according to its relative abundance in the community.
  kind: background · ref: garnierPlantFunctionalMarkers2004 · check: DOI 10.1890/03-0799 resolves on Crossref; stated in the abstract ("community-aggregated (i.e., weighed according to the relative abundance of species)")
- **community-weighted-means.1** In trait ecology, CWMs all share the same abundance weights, so the composition matrix itself induces structure among CWMs.
  conf: not stated · class: not stated · holds: community-weighted means in trait ecology · src: none (the note cites no source for this sentence) · trail: H2-01 §2.3 · from: H2-01:B-0083
- **community-weighted-means.2** CWM correlation tests have inflated error rates when only environment or only traits structure species distributions.
  conf: not stated · class: model (marker) · holds: CWM correlation tests; modelled · src: peresnetoLinkingTraitVariation2017 (AB; modelled) · trail: H2-01 §2.3 · from: H2-01:I-0011
- **community-weighted-means.3** The inflation of CWM correlation test error rates falls with compositional beta diversity and rises with sample size.
  conf: not stated · class: model (marker) · holds: CWM correlation tests; modelled · src: zelenyWhichResultsStandard2018 (AB; modelled) · trail: H2-01 §2.3 · from: H2-01:I-0011, H2-01:I-0012
- **community-weighted-means.4** By analogy, community-aggregated functional profiles share weights in the same way as CWMs.
  conf: not stated · class: reading (note: "By analogy (reviewer's reading)") · holds: community-aggregated microbial functional profiles, by analogy with trait-ecology CWMs · src: none (the reviewer's reading) · trail: H2-01 §2.3 · from: H2-01:B-0083, H2-01:B-0084
- **community-weighted-means.5** Abundance-weighted and unweighted trait moments disagreed in sign, significance or both for 71% of forest trait-climate results.
  conf: not stated · class: not stated · holds: forest trait-climate results · src: wieczynskiClimateShapesShifts2018 (AB) · trail: H2-01 §4.4 · from: H2-01:B-0163
- **community-weighted-means.6** CWM accuracy depended on trait coverage of the community.
  conf: not stated · class: not stated · holds: plant community trait data · src: borgySensitivityCommunitylevelTraitenvironment2017 (AB) · trail: H2-01 §4.4 · from: H2-01:B-0162, H2-01:B-0163

### dimensionality: dimensionality of microbial sample-by-function profiles
needs: shared-mean-profile, processing-effects
- **dimensionality.bg1** Non-negative matrix factorization (NMF) decomposes a non-negative data matrix into non-negative parts whose constraints allow only additive, not subtractive, combinations.
  kind: background · ref: leeLearningPartsObjects1999 · check: DOI 10.1038/44565 resolves on Crossref; stated in the abstract (PubMed 10548103)
- **dimensionality.1** Few direct estimates of dimension exist for microbial sample-by-function matrices, and they use incompatible methods (NMF rank 5 for 8,214 Pfams in 45 ocean samples, two co-inertia axes carrying about half the variation in 128 soils, three KO clusters across 6,539 metagenomes); none uses a formal rank-selection rule (parallel analysis, cross-validated PCA or NMF, a random-matrix threshold) with stated n and p and tests how the estimate changes with processing.
  conf: single (critic: C-009) · class: not stated · holds: microbial sample-level functional profiles; each direct estimate is a single study, fitted and scored on the same samples · src: jiangFunctionalBiogeographyOcean2012, pitonLifeHistoryStrategies2023, flinkstromMetagenomicClusteringLinks2024 · rating: "Weak for the microbial sample-level question" · trail: H2-01 §2.1, §answers, §6. Answers, §critic · from: H2-01:A-001, H2-01:B-0046, H2-01:B-0047, H2-01:A-013, H2-01:A-014, H2-01:A-104, H2-01:C-001, H2-01:C-009
- **dimensionality.2** Across 45 Global Ocean Sampling sites and 8,214 Pfam relative abundances, NMF was judged stable at rank 5 by a concordance criterion; no variance-explained figure was reported, the five components had "strikingly high" similarity to each other, a large ubiquitous, mostly primary-metabolism Pfam block loaded on all of them, and two components could not be interpreted.
  conf: single (critic: C-009) · class: meas (marker) · holds: ocean samples (Global Ocean Sampling sites), n = 45; fitted and scored on the same samples · src: jiangFunctionalBiogeographyOcean2012 (FT; measured; fitted and scored on the same samples; SINGLE SOURCE) · trail: H2-01 §2.1, §answers · from: H2-01:B-0048..0050, H2-01:I-0002, H2-01:A-002, H2-01:C-009
- **dimensionality.3** Rank 5 is low relative to 8,214 features, but with n = 45 the rank cannot exceed 45, and much of the NMF fit is a shared mean-like profile.
  conf: not stated · class: reading (note: "Reviewer's reading") · holds: the ocean NMF estimate (45 sites, 8,214 Pfams) · src: jiangFunctionalBiogeographyOcean2012 · trail: H2-01 §2.1 · from: H2-01:B-0048, H2-01:B-0051
- **dimensionality.4** In 128 soil metagenomes (global topsoil set) with KEGG, eggNOG, SEED, CAZy and genomic-trait tables (relative abundance normalised by annotated bacterial reads, log(x+1), z-scored), the first four multiple co-inertia axes captured 29%, 21%, 16% and 10% of variation, and the first axis tracked average genome size (R² = 0.64).
  conf: single (marker) · class: meas (marker) · holds: soil metagenomes, community-aggregated traits; fitted and scored on the same samples; the only variance-explained figure for a microbial functional profile; the critic: full text "per angle" and not re-checked by the reviewer · src: pitonLifeHistoryStrategies2023 (FT; measured; SINGLE SOURCE) · trail: H2-01 §2.1, §answers, §Adversarial · from: H2-01:B-0052, H2-01:I-0003, H2-01:A-003, H2-01:A-026, H2-01:C-009, H2-01:C-062
- **dimensionality.5** Piton et al. call the soil co-inertia result a two-dimension "triangle" of life-history strategies, and warn that community-aggregated covariation does not show within-organism trade-offs and that only 5 to 15% of reads were annotated, with annotation coverage falling as genome size rose.
  conf: not stated · class: not stated · holds: 128 soil metagenomes · src: pitonLifeHistoryStrategies2023 · trail: H2-01 §2.1 · from: H2-01:B-0052..0054
- **dimensionality.6** In the soil co-inertia result, two axes carry about half the variation; the other half is not low-dimensional on this evidence.
  conf: not stated · class: reading (note: "Reviewer's reading") · holds: 128 soil metagenomes · src: pitonLifeHistoryStrategies2023 · trail: H2-01 §2.1 · from: H2-01:B-0052, H2-01:B-0055
- **dimensionality.7** Across 6,539 IMG/M assembled metagenomes (KO abundances, KOs in under 10% of samples removed, CLR), bootstrapped k-means found three clusters (terrestrial, aquatic, anaerobic), strongly associated with assembly GC content; cluster number is not an intrinsic-dimension estimate and is a nearest precedent only.
  conf: single (marker) · class: meas (marker) · holds: multi-biome assembled metagenomes; fitted and scored on the same samples · src: flinkstromMetagenomicClusteringLinks2024 (FT; measured; SINGLE SOURCE) · trail: H2-01 §2.1, §answers · from: H2-01:I-0004, H2-01:B-0056, H2-01:A-004, H2-01:C-009
- **dimensionality.8** Across 25 GOS metagenomes, the first canonical correlation between KEGG module composition and environment was 0.944; with n = 25 and many modules, a high first canonical correlation on the same samples is expected, and it does not measure dimension.
  conf: not stated · class: meas (marker) · holds: ocean metagenomes (GOS), n = 25 · src: raesTowardMolecularTraitbased2011 (FT; measured) · trail: H2-01 §2.1 · from: H2-01:I-0005, H2-01:B-0057, H2-01:B-0058
- **dimensionality.9** Gianoulis et al. (2009) define "metabolic footprints" by CCA on GOS.
  conf: not stated · class: not stated · holds: GOS · src: gianoulisQuantifyingEnvironmentalAdaptation2009 (AB) · trail: H2-01 §2.1 · from: H2-01:B-0059
- **dimensionality.10** Read literally, the direct estimates are low relative to the number of functions, but in each case n is small or only about half the variance is in the leading axes, and the leading structure is partly a shared mean profile (evidence the critic reads as showing only that per-sample profiles are highly similar in these datasets) or a genome-size axis (Piton axis 1 against genome size R² 0.64; genome size and normalisation effects).
  conf: not stated · class: not stated · holds: the three direct microbial estimates · src: jiangFunctionalBiogeographyOcean2012, pitonLifeHistoryStrategies2023, flinkstromMetagenomicClusteringLinks2024, sunInferenceBasedAccuracyMetagenome2020, theStructureFunctionDiversity2012, nayfachAverageGenomeSize2015, manorMUSiCCMarkerGenes2015 · trail: H2-01 §answers, §critic · from: H2-01:A-005, H2-01:A-006, H2-01:C-006
- **dimensionality.11** No microbial study was found that re-estimated the dimension of functional profiles under different normalisations, sparsity filters, presence/absence against abundance, overlapping gene sets or sample sizes; none tested sensitivity to these choices with a formal rank rule and stated n and p.
  conf: not stated · class: search (note: "Not found by these routes") · holds: microbial sample-by-function profiles; the review's search routes · src: none (a search result) · search: searched, not found (note: "Not found by these routes") · trail: H2-01 §2.3, §answers, §Provenance, §critic · from: H2-01:B-0065, H2-01:B-0018, H2-01:A-007, H2-01:A-019, H2-01:A-105, H2-01:C-010
- **dimensionality.12** What is measured is that processing choices change across-sample variance and covariance (normalisation, genome size, pathway aggregation, compositional closure), which a dimension estimate would inherit; that these shifts lower apparent dimension is the reviewer's inference, so the evidence is only indirect for dimension.
  conf: not stated · class: reading (note: "is the reviewer's inference") · holds: microbial functional profiles; indirect for dimension · src: manorRevisedComputationalMetagenomic2017, yeParsimonyApproachBiological2009, lovellProportionalityValidAlternative2015 · trail: H2-01 §2.3, §answers, §6. Answers, §Adversarial · from: H2-01:B-0066, H2-01:A-008, H2-01:A-009, H2-01:A-015, H2-01:A-106, H2-01:C-131
- **dimensionality.13** At least one leading axis of many functional-profile decompositions may be a genome-size or normalisation axis; the first Piton axis (R² = 0.64 with genome size) is consistent with this. This is an inference, not a measured decomposition.
  conf: not stated · class: reading (note: "Reviewer's reading") · holds: functional-profile decompositions · src: pitonLifeHistoryStrategies2023 · trail: H2-01 §2.3 · from: H2-01:B-0069..0071
- **dimensionality.14** None of the gene-set studies measures a covariance matrix between overlapping gene sets; that shared members inflate pathway-pathway covariance, and so lower apparent dimension, is the reviewer's inference.
  conf: not stated · class: reading (note: "is the reviewer's inference") · holds: pathway profiles built from gene sets that share members · src: manorRevisedComputationalMetagenomic2017, yeParsimonyApproachBiological2009, donatoAnalysisCorrectionCrosstalk2013 · trail: H2-01 §2.3 · from: H2-01:B-0078..0081
- **dimensionality.15** Whether a dimension estimate is taken before or after centring on the shared mean profile will change it; no microbial study found reports both.
  conf: not stated · class: search (note: "No microbial study found reports both") · holds: microbial functional profiles · src: none (the reviewer's statement and a search result) · search: searched, not found (note: "No microbial study found reports both") · trail: H2-01 §2.2 · from: H2-01:B-0063, H2-01:B-0064
- **dimensionality.16** No held-out (cross-validated) rank estimate has been measured for functional profiles.
  conf: not stated · class: search (note: "Not measured") · holds: microbial functional profiles · src: none (a search result) · search: not stated · trail: H2-01 §answers · from: H2-01:A-019, H2-01:A-020
- **dimensionality.17** Dimension has not been compared by habitat; no search route targeted habitat-stratified decompositions (for example the per-biome NMF or PCA in multi-biome metagenome atlases).
  conf: not stated · class: search (note: "Dimension by habitat not compared") · holds: microbial functional profiles · src: none (a search result) · search: not searched (critic: C-113) · trail: H2-01 §answers, §Adversarial · from: H2-01:A-021, H2-01:C-113

### dimension-elsewhere: dimensionality of genomes, trait databases and transcriptomes
needs: dimensionality
- **dimension-elsewhere.1** Across 2,621 bacterial genera, diffusion maps on presence/absence of 7,769 substrate-product traits found no single low-dimensional space but crossing low-dimensional manifolds with "dozens or possibly hundreds of meaningful coordinates".
  conf: single (marker) · class: model (marker) · holds: genomes as rows (genera), not samples; presence/absence; one modelled study · src: fahimipourMappingBacterialMetabolic2020a (FT; modelled; SINGLE SOURCE) · trail: H2-01 §2.4, §critic, §Adversarial · from: H2-01:I-0013, H2-01:B-0085, H2-01:A-011, H2-01:C-007, H2-01:C-070
- **dimension-elsewhere.2** A review names three main axes of quantitative bacterial traits (growth rate with rRNA copy number, genome size with signal transduction, cell size) and notes that quantitative traits vary widely within substrate-use pathways.
  conf: not stated · class: assert (marker) · holds: quantitative bacterial and archaeal traits · src: westobyTraitDimensionsBacteria2021 (AB; asserted) · trail: H2-01 §2.4 · from: H2-01:R-0246, H2-01:I-0014
- **dimension-elsewhere.3** The genome diffusion-map result and the three-axis trait review are not in conflict: they describe different trait sets, and together they bound any claim that "microbial function" has one dimensionality.
  conf: not stated · class: not stated · holds: bacterial trait sets across genomes · src: fahimipourMappingBacterialMetabolic2020a, westobyTraitDimensionsBacteria2021 · trail: H2-01 §2.4 · from: H2-01:I-0013, H2-01:I-0014, H2-01:B-0086, H2-01:B-0087
- **dimension-elsewhere.4** Across 30 species-by-trait datasets, the median dimension was 4 by an elbow rule (range 2 to 8) and 6 by an AUC threshold of 0.7 (range 2 to 17), and the two estimates were only weakly correlated.
  conf: not stated · class: meas (marker) · holds: species trait databases (species as rows, not samples) · src: mouillotDimensionalityStructureSpecies2021 (FT; measured) · trail: H2-01 §2.4, §answers · from: H2-01:I-0015, H2-01:B-0085, H2-01:A-010
- **dimension-elsewhere.5** In species trait databases, threshold dimensionality rose with the log number of traits and fell with mean trait correlation (GLM R² = 0.61); in simulations, species number mattered only below about 100 to 200 species, and dropping half the traits lost much quality.
  conf: not stated · class: not stated · holds: species-by-trait datasets and simulations · src: mouillotDimensionalityStructureSpecies2021 · trail: H2-01 §2.4, §answers · from: H2-01:I-0015, H2-01:B-0088, H2-01:B-0089, H2-01:A-010
- **dimension-elsewhere.6** The species-trait study is the only source found that measures how a dimension estimate depends on the number of features, feature correlation and sample count; it concerns species-level traits, not sample-level profiles, from another setting.
  conf: single (note: "This is the only source found") · class: not stated · holds: species-by-trait matrices; the critic: read by a search agent and not re-opened by the reviewer, full text "per angle" and not re-checked · src: mouillotDimensionalityStructureSpecies2021 · trail: H2-01 §2.4, §answers, §6. Answers, §critic, §Adversarial · from: H2-01:B-0090, H2-01:B-0091, H2-01:A-016, H2-01:A-027, H2-01:A-107, H2-01:C-011, H2-01:C-062
- **dimension-elsewhere.7** Plant traits showed at most six dimensions in the largest of three datasets.
  conf: not stated · class: not stated · holds: plant trait datasets · src: laughlinIntrinsicDimensionalityPlant2013 (AB) · trail: H2-01 §2.4 · from: H2-01:B-0092
- **dimension-elsewhere.8** Two components explain 74% of six key plant traits across 2,214 species.
  conf: not stated · class: not stated · holds: plant species traits; secondary, via Bruelheide2018 · src: bruelheideGlobalTraitenvironmentRelationships2018 (SEC, via Bruelheide2018) · trail: H2-01 §2.4 · from: H2-01:B-0093
- **dimension-elsewhere.9** With 17 gap-filled traits across more than 20,000 plant species, PC1 explained 33%, PC2 15% and PC3 9.4%.
  conf: not stated · class: not stated · holds: plant species, gap-filled trait matrix · src: joswigClimaticSoilFactors2021 (FT) · trail: H2-01 §2.4 · from: H2-01:B-0093
- **dimension-elsewhere.10** The trait gap-filling method BHPMF imputes from trait-trait correlations.
  conf: not stated · class: not stated · holds: plant trait gap-filling · src: schrodtScpBHPMFScp2015 (AB) · trail: H2-01 §2.4 · from: H2-01:B-0093, H2-01:B-0094
- **dimension-elsewhere.11** Because BHPMF imputes from trait-trait correlations, covariation in imputed trait matrices is partly built in.
  conf: not stated · class: reading (note: "reviewer's reading") · holds: gap-filled plant trait matrices · src: schrodtScpBHPMFScp2015 · trail: H2-01 §2.4 · from: H2-01:B-0093, H2-01:B-0094
- **dimension-elsewhere.12** Across 352 microarray datasets, the first principal value averaged about twice the second, the first five explained most variance, and per-gene shuffling removed this; the authors call low dimensionality fundamental.
  conf: single (critic: C-008) · class: meas (marker) · holds: gene expression microarray datasets, another field; within datasets · src: heimbergLowDimensionalityGene2016 (FT; measured; SINGLE SOURCE; critic: C-008 was "FT; measured") · trail: H2-01 §2.4, §critic, §Adversarial · from: H2-01:I-0016, H2-01:B-0095, H2-01:C-007, H2-01:C-008, H2-01:C-071..073, H2-01:C-119, H2-01:C-121
- **dimension-elsewhere.13** In large heterogeneous expression compendia (5,372 and 7,100 samples), the first three PCs explained about 36% of variance, components beyond the third were unstable between datasets, the residual space carried most tissue-specific signal, and PCA depended on the fraction of samples carrying a signal.
  conf: single (marker) · class: meas (marker) · holds: gene expression compendia, another field; across datasets · src: lenzPrincipalComponentsAnalysis2016 (FT; measured; SINGLE SOURCE) · trail: H2-01 §2.4, §answers · from: H2-01:B-0096, H2-01:I-0017, H2-01:A-012
- **dimension-elsewhere.14** In gene expression, "low-dimensional" holds for leading components within a dataset and weakens when dimension is judged by reproducibility across datasets or by information in the residual.
  conf: single (critic: C-007) · class: not stated · holds: transcriptomics, another field; the within-dataset side rests on one study and the across-dataset side on one study · src: heimbergLowDimensionalityGene2016, lenzPrincipalComponentsAnalysis2016 · trail: H2-01 §2.4, §answers, §critic · from: H2-01:B-0097, H2-01:A-012, H2-01:C-007, H2-01:C-008
- **dimension-elsewhere.15** Low dimension estimates (Jiang2012, Piton2023's two leading axes, Heimberg2016) stand against higher ones (Fahimipour2020 across genomes; Lenz2016 across datasets; Piton's remaining half of variance); these largely reflect different objects (samples against genomes) and different criteria (within-dataset variance against cross-dataset stability), not direct contradiction on the same data.
  conf: not stated · class: not stated · holds: the D1 sources taken together · src: jiangFunctionalBiogeographyOcean2012, pitonLifeHistoryStrategies2023, heimbergLowDimensionalityGene2016, fahimipourMappingBacterialMetabolic2020a, lenzPrincipalComponentsAnalysis2016 · trail: H2-01 §answers · from: H2-01:A-017, H2-01:A-018

### covariation-transfer: held-out transfer of microbial functional covariation
needs: none
- **covariation-transfer.1** No study was found that fitted covariation among microbial functions (a covariance or correlation matrix, a factorisation, a network, or a regression of some functions on others) in a set of habitats and scored it on a withheld habitat; this is a statement about the routes searched, not a statement that the literature lacks such a study.
  conf: not stated · class: search (note: "Not found by these routes") · holds: microbial function-function covariation; withheld habitat; routes: Europe PMC, PubMed and PMC E-utilities, Crossref, Semantic Scholar, OpenAlex, Unpaywall and known literature, with WebSearch and Scholar Gateway unavailable · src: none (a search result) · search: searched, not found (note: "Not found by these routes") · rating: "Absent for the withheld-habitat microbial case" · trail: H2-01 §3.1, §1. What, §Provenance, §answers, §6. Answers, §critic · from: H2-01:B-0098..0100, H2-01:B-0037, H2-01:B-0018, H2-01:A-030, H2-01:A-031, H2-01:A-042, H2-01:A-047, H2-01:A-048, H2-01:A-110, H2-01:C-012
- **covariation-transfer.2** Pathway co-abundances estimated in an IBD discovery cohort were tested in an independent IBD cohort (iHMP-IBD, 77 individuals): of 37,106 testable pathway co-abundances, 21,882 (59.0%) replicated at P < 0.05; of 2,090 species co-abundances, 531 (25.4%), so pathway co-abundances partly reproduced.
  conf: single (marker) · class: meas (marker) · holds: human gut metagenomes from four cohorts (n = 2,379), 134 species and 343 MetaCyc pathways (HUMAnN2), SparCC combined with SPIEC-EASI; the withheld unit is a study within the same habitat and disease state, not a habitat; the only direct microbial test of functional covariation on held-out data · src: chenGutMicrobialCoabundance2020 (FT, figures re-checked; measured; SINGLE SOURCE) · rating: "Weak for withheld-study (one study, one habitat)" · trail: H2-01 §3.2, §answers, §6. Answers, §critic · from: H2-01:I-0018, H2-01:B-0101, H2-01:B-0103, H2-01:B-0104, H2-01:B-0110, H2-01:A-032, H2-01:A-033, H2-01:A-043, H2-01:A-053, H2-01:A-111, H2-01:C-013, H2-01:C-014
- **covariation-transfer.3** Chen et al. attribute the low species replication rate largely to power, since 81.6% of species and 65.1% of pathway co-abundances showed no significant difference in strength between the two IBD cohorts.
  conf: not stated · class: not stated · holds: the two IBD cohorts (discovery and iHMP-IBD) · src: chenGutMicrobialCoabundance2020 · trail: H2-01 §3.2 · from: H2-01:B-0103, H2-01:B-0105
- **covariation-transfer.4** For the reductive TCA cycle pathway, 94.7% of 76 IBD-specific co-abundances replicated.
  conf: not stated · class: not stated · holds: the IBD discovery and iHMP-IBD cohorts, human gut · src: chenGutMicrobialCoabundance2020 · trail: H2-01 §3.2 · from: H2-01:B-0101, H2-01:B-0103, H2-01:B-0106
- **covariation-transfer.5** MetaCyc pathways share reactions and contributing species, so pathway-pathway co-abundance partly reflects shared members; 43,355 of about 58,653 possible pathway pairs were significant in at least one cohort, which points to strong common factors that would make replication easy; and "replicated at P < 0.05" with n = 77 is a lenient bar, so the 59% is an optimistic reading of transfer.
  conf: not stated · class: reading (note: "Cautions (reviewer's reading)") · holds: the IBD replication test · src: chenGutMicrobialCoabundance2020 · trail: H2-01 §3.2, §answers · from: H2-01:A-033, H2-01:B-0108, H2-01:B-0109, H2-01:A-034
- **covariation-transfer.6** No held-out test has used presence/absence profiles or compared annotation schemes.
  conf: not stated · class: search (note: "Not measured") · holds: microbial functional profiles in a held-out design · src: none (a statement of what was not measured) · search: not stated · trail: H2-01 §answers · from: H2-01:A-047, H2-01:A-049
- **covariation-transfer.7** No held-out test has been made in soils, oceans or other non-human habitats at all.
  conf: not stated · class: search (note: "Not measured") · holds: held-out tests of microbial functional profiles · src: none (a statement of what was not measured) · search: not stated · trail: H2-01 §answers · from: H2-01:A-047, H2-01:A-050

### neighbouring-transfer: transfer of taxon-to-function mappings, classifiers and gene co-occurrence
needs: shared-mean-profile
- **neighbouring-transfer.1** PICRUSt accuracy fell with distance to the nearest reference genome (NSTI), across all samples (r = −0.4) and within each habitat (r = −0.25 to −0.82); accuracy was high in soils (0.81) and low in a hypersaline mat (reported 0.25, mean NSTI 0.23).
  conf: not stated · class: meas (marker) · holds: a genome-derived taxon-to-gene mapping transferred across habitats, not covariation among functions · src: langillePredictiveFunctionalProfiling2013 (FT; measured) · trail: H2-01 §3.3 · from: H2-01:I-0019, H2-01:B-0112
- **neighbouring-transfer.2** The per-sample Spearman metric is almost insensitive to permuting genes across samples, and inference-level agreement of metagenome prediction tools was reasonable in human datasets and much lower in non-human and soil datasets.
  conf: not stated · class: not stated · holds: human, non-human and soil datasets; a taxon-to-gene mapping, not covariation among functions · src: sunInferenceBasedAccuracyMetagenome2020 (FT) · trail: H2-01 §3.3 · from: H2-01:R-0231, H2-01:B-0111, H2-01:B-0112
- **neighbouring-transfer.3** These mapping results suggest that taxon-to-function mappings transfer less well as reference coverage of the target habitat falls.
  conf: not stated · class: not stated · holds: taxon-to-function mappings, a quantity other than function-function covariation · src: langillePredictiveFunctionalProfiling2013, sunInferenceBasedAccuracyMetagenome2020 · trail: H2-01 §3.3, §answers · from: H2-01:B-0113, H2-01:A-035
- **neighbouring-transfer.4** Colorectal cancer classifiers on eggNOG groups gave AUROC 0.70 to 0.81 study-to-study and 0.78 to 0.89 leave-one-study-out, similar to species-level classifiers.
  conf: not stated · class: meas (marker) · holds: human gut only; a classifier, not a covariance structure · src: wirbelMetaanalysisFecalMetagenomes2019 (FT; measured) · trail: H2-01 §3.3, §answers · from: H2-01:I-0020, H2-01:B-0114, H2-01:A-035
- **neighbouring-transfer.5** In the E. coli pangenome, accessory-gene presence was predicted from other accessory genes on held-out random genomes; after filtering and removing phylogenetic signal, 16.7% of families were predictable at F1 ≥ 0.9 against a chance rate of about 1 to 1.7%.
  conf: single (marker) · class: not stated · holds: gene co-occurrence across genomes of the E. coli pangenome, not across samples · src: beavanContingencyRepeatabilityPredictability2023 (FT; SINGLE SOURCE) · trail: H2-01 §3.3, §answers · from: H2-01:I-0021, H2-01:A-035
- **neighbouring-transfer.6** Across about 3,000 genomes, gene gain and loss in metabolic pathways was predictable in a hold-one-phylum-out test for each of the 10 largest phyla, with predictability differing significantly among phyla.
  conf: single (marker) · class: model (marker) · holds: about 3,000 bacterial genomes; phylogenetic gene gain/loss prediction in metabolic pathways · src: konnoMachineLearningEnables2023 (FT; modelled; SINGLE SOURCE) · trail: H2-01 §3.3, §answers · from: H2-01:R-0159, H2-01:C-017, H2-01:I-0022, H2-01:A-035
- **neighbouring-transfer.7** Gene content predicted MAG niche position along Baltic Sea gradients better than phylogeny under genome-level cross-validation.
  conf: not stated · class: not stated · holds: Baltic Sea metagenome-assembled genomes · src: alnebergEcosystemwideMetagenomicBinning2020 (FT) · trail: H2-01 §3.3 · from: H2-01:B-0115
- **neighbouring-transfer.8** Phylogenetic-profile co-occurrence recovered same-pathway enzyme pairs better than homology, in a benchmark partly circular with KEGG membership.
  conf: not stated · class: not stated · holds: a benchmark partly circular with KEGG membership · src: chungAssemblingBacterialPuzzles2024 (AB) · trail: H2-01 §3.3 · from: H2-01:B-0116
- **neighbouring-transfer.9** A low-dimensional gene-to-function map transferred from strains to communities for denitrification.
  conf: not stated · class: not stated · holds: denitrification · src: gowdaGenomicStructurePredicts2022 (AB) · trail: H2-01 §3.3 · from: H2-01:B-0117
- **neighbouring-transfer.10** Five "generalizable" enterosignatures were found from 5,230 gut metagenomes; what "generalizable" means (the held-out design) was not read.
  conf: not stated · class: not stated · holds: human gut metagenomes; taxonomic low-rank structure · src: friouxEnterosignaturesDefineCommon2023 (AB) · limit: access (note: "was not read") · trail: H2-01 §3.3 · from: H2-01:R-0132, H2-01:B-0118, H2-01:B-0119

### other-field-transfer: held-out covariation tests in transcriptomics and plant traits
needs: none
- **other-field-transfer.1** Sparse module dictionaries learned on 5% of samples of a TCGA tumour type gave about 87% recovery (Spearman, SMAF) within the same tumour type, and a dictionary from a different tumour type gave 68% on average, with related tumour types doing better; these figures are Spearman recovery of expression from 25 simulated random composite measurements through the dictionary (compressed sensing, m = 25, g = 5,000), not a direct covariance-reproduction score.
  conf: single (marker) · class: meas (marker) · holds: TCGA tumour types, transcriptomics; a withheld tissue type, the closest other-field analogue of a withheld habitat; the authors warn a dictionary is biased when training data do not represent the test data · src: clearyEfficientGenerationTranscriptomic2017 (FT; measured; SINGLE SOURCE) · trail: H2-01 §3.4, §answers, §critic, §Adversarial · from: H2-01:B-0170, H2-01:B-0120, H2-01:I-0023, H2-01:B-0121, H2-01:A-037, H2-01:A-054, H2-01:C-019, H2-01:C-020, H2-01:C-063..065
- **other-field-transfer.2** A linear model from about 1,000 landmark genes, trained on GEO microarrays, inferred 81% of non-measured transcripts well in independent GTEx RNA-seq (8,555 samples); about 19% were not well inferred.
  conf: single (marker) · class: meas (marker) · holds: transcriptomics; a withheld study and platform · src: subramanianNextGenerationConnectivity2017 (FT; measured; SINGLE SOURCE) · trail: H2-01 §3.4, §answers · from: H2-01:I-0024, H2-01:A-038
- **other-field-transfer.3** A single co-expression network fitted to all 35 GTEx tissues pooled had held-out likelihood so low it was dropped from the comparison; per-tissue networks did better, and sharing between related tissues did better again, so pooled networks represented individual tissues poorly.
  conf: single (critic: C-121) · class: meas (marker) · holds: 35 GTEx human tissues; samples, not tissues, were withheld · src: piersonSharingSpecificityCoexpression2015 (FT; measured; SINGLE SOURCE; critic: C-121 was "FT; measured") · trail: H2-01 §3.4, §answers, §Adversarial · from: H2-01:R-0204, H2-01:I-0025, H2-01:B-0122, H2-01:A-039, H2-01:C-119, H2-01:C-121
- **other-field-transfer.4** Individual co-expression networks predicted GO membership with mean AUROC 0.60 (bulk) and 0.56 (single cell), aggregating 163 networks reached 0.73 (bulk), and sample size did not predict performance, so individual co-expression networks replicate modestly.
  conf: not stated · class: meas (marker) · holds: co-expression networks, bulk and single-cell expression · src: crowExploitingSinglecellExpression2016 (FT; measured) · trail: H2-01 §3.4, §answers · from: H2-01:I-0026, H2-01:A-040
- **other-field-transfer.5** A latent space learned on recount2 was concordant with dataset-specific models in rare-disease studies, with broader training capturing more pathways.
  conf: not stated · class: not stated · holds: transcriptomics, rare-disease studies; qualitative · src: taroniMultiPLIERTransferLearning2019 (FT; qualitative) · trail: H2-01 §3.4 · from: H2-01:R-0240, H2-01:B-0123
- **other-field-transfer.6** projectR tests whether a pattern is shared by projection; it is a framework and reports no failure rate.
  conf: not stated · class: not stated · holds: a projection framework for transfer learning across cellular measurements · src: steinobrienDecomposingCellIdentity2019 (FT; framework, no failure rate) · trail: H2-01 §3.4 · from: H2-01:R-0225, H2-01:B-0123
- **other-field-transfer.7** Global leaf-economics correlations may not hold at local scales, since correlation strength only bounds how differently traits can vary across scales.
  conf: not stated · class: not stated · holds: plant leaf traits; transfer across scale, not across habitat · src: messierTraitVariationIntegration2016 (AB) · trail: H2-01 §3.4 · from: H2-01:B-0124, H2-01:B-0126
- **other-field-transfer.8** Some leaf-trait correlations reverse sign within species compared with across species.
  conf: not stated · class: not stated · holds: plant leaf traits; transfer across taxonomic level, not across habitat · src: andereggWithinspeciesPatternsChallenge2018 (AB) · trail: H2-01 §3.4 · from: H2-01:B-0125, H2-01:B-0126
- **other-field-transfer.9** In other fields, covariation transfers partly, each result from a single study.
  conf: single (critic: C-015) · class: not stated · holds: transcriptomics and other fields, not microbial · src: clearyEfficientGenerationTranscriptomic2017, subramanianNextGenerationConnectivity2017, piersonSharingSpecificityCoexpression2015, crowExploitingSinglecellExpression2016 · rating: "Moderate for partial transfer in transcriptomics, but that is another field and each quantitative result is a single study" · trail: H2-01 §answers, §critic · from: H2-01:A-036, H2-01:A-044, H2-01:C-015
- **other-field-transfer.10** There is no direct conflict on the same quantity: reproduction is high in some tests (Subramanian's 81%; Chen's reductive TCA cycle at 94.7%) and low in others (Cleary's cross-type drop; pooled networks in Pierson; sign reversals across scales in plant traits).
  conf: not stated · class: not stated · holds: the held-out tests across fields · src: subramanianNextGenerationConnectivity2017, chenGutMicrobialCoabundance2020, clearyEfficientGenerationTranscriptomic2017, piersonSharingSpecificityCoexpression2015, andereggWithinspeciesPatternsChallenge2018 · trail: H2-01 §answers · from: H2-01:A-045, H2-01:A-046

### transfer-dependence: what transfer appears to depend on
needs: covariation-transfer, neighbouring-transfer, other-field-transfer, dimension-elsewhere
- **transfer-dependence.1** The review's synthesis is that, across the other-field and neighbouring evidence, transfer appears to depend on the similarity of the training set to the target (related tumour types; related tissues; NSTI; phylum differences), the breadth of the training set, and the fraction of the target that is shared mean structure against target-specific signal; the critic holds that this pools incommensurable tests of different quantities (covariance or dictionary transfer, taxon-to-gene mapping accuracy, per-sample accuracy metrics, phylogenetic gene gain/loss prediction) and is the reviewer's synthesis, not a finding.
  conf: not stated · class: reading (critic: C-018) · holds: each dependency rests on one to three sources measuring different quantities, breadth on one qualitative study alone; none of these dependencies has been measured for microbial function-function covariation across habitats · src: none (the reviewer's synthesis) · trail: H2-01 §3.5, §answers, §critic, §Adversarial · from: H2-01:B-0127, H2-01:B-0128, H2-01:A-041, H2-01:A-046, H2-01:C-016..018, H2-01:C-054, H2-01:C-075, H2-01:C-126

### levels-within-habitat: function levels against taxonomic composition within a habitat (case A)
needs: shared-mean-profile, processing-effects
- **levels-within-habitat.1** Within a habitat where taxonomy turns over, several studies report function levels more stable than taxonomic composition (HMP pathways against organisms; bromeliad microcosms; macroalgal host COGs against species; soil microcosm functional groups; vermicomposting turnover rates), two in full text and three resting on abstracts; the direction is best described as reported by several studies but dependent on processing, with direct measured contrary evidence in human gut and coastal ocean.
  conf: not stated · class: not stated · holds: habitat held roughly fixed; none of the studies controls for normalisation, aggregation and granularity together · src: theStructureFunctionDiversity2012 (FT), burkeBacterialCommunityAssembly2011 (FT), loucaHighTaxonomicVariability2016 (AB), shanAnnotationfreeDiscoveryFunctional2023 (AB), airaFasterTurnoverTaxonomic2026 (AB), manorRevisedComputationalMetagenomic2017, galandStrongLinkMarine2018 (AB) · rating: "Moderate for the direction as reported, weak for the claim that the stability is biological rather than processing-driven" · contrary: one-sided (critic: C-123) · trail: H2-01 §4.1, §answers, §6. Answers, §critic, §Adversarial · from: H2-01:B-0131, H2-01:A-055, H2-01:A-057, H2-01:A-061..063, H2-01:A-113, H2-01:C-021..023, H2-01:C-027, H2-01:C-122..124
- **levels-within-habitat.2** Bromeliad tank microcosms showed similar functional-group structure across replicates and highly variable taxonomy within groups.
  conf: not stated · class: meas (marker) · holds: bromeliad tank microcosms · src: loucaHighTaxonomicVariability2016 (AB; measured) · trail: H2-01 §4.1 · from: H2-01:I-0028
- **levels-within-habitat.3** On a macroalgal host, species composition was about 15% similar against 70% similarity in COG composition; the contrast compares a species table with a coarser COG table, and the taxonomic figure is from an earlier study.
  conf: not stated · class: meas (marker) · holds: bacterial communities on a macroalgal host · src: burkeBacterialCommunityAssembly2011 (FT; measured) · trail: H2-01 §4.1 · from: H2-01:R-0091, H2-01:I-0029, H2-01:B-0132
- **levels-within-habitat.4** In replicate soil microcosms, annotation-free functional groups were stable in summed abundance despite large variation in species composition.
  conf: not stated · class: not stated · holds: replicate soil microcosms · src: shanAnnotationfreeDiscoveryFunctional2023 (AB) · trail: H2-01 §4.1 · from: H2-01:B-0133
- **levels-within-habitat.5** During vermicomposting, taxonomic turnover over time was about twelve times functional turnover.
  conf: not stated · class: not stated · holds: vermicomposting over time; no non-earthworm control · src: airaFasterTurnoverTaxonomic2026 (AB; no non-earthworm control) · trail: H2-01 §4.1 · from: H2-01:B-0134
- **levels-within-habitat.6** A model found taxa-function robustness higher in gut than in vaginal communities, so how far function tracks taxonomy may itself vary by habitat.
  conf: single (critic: C-082) · class: model (marker) · holds: one modelled, abstract-only study comparing gut and vaginal communities · src: engTaxafunctionRobustnessMicrobial2018 (AB; modelled) · trail: H2-01 §4.1, §answers, §Adversarial · from: H2-01:I-0030, H2-01:A-060, H2-01:C-082
- **levels-within-habitat.7** Within the human gut, how consistently genera carry metabolic modules differs among genera, and module-derived redundancy was lower in the Bacteroides enterotype.
  conf: not stated · class: not stated · holds: human gut · src: vieirasilvaSpeciesfunctionRelationshipsShape2016 (AB) · trail: H2-01 §4.1 · from: H2-01:B-0135
- **levels-within-habitat.8** In a coastal Mediterranean time series, Galand et al. (2018) report a strong taxonomy-function link when function is measured from all reads or all predicted genes, and weaker links with annotated orthologues or taxonomy-inferred functions, and conclude that this challenges functional redundancy; the abstract is explicit that using all reads, not annotated genes, was essential.
  conf: not stated · class: not stated · holds: coastal Mediterranean time series; the reported R² values came from an automated summary and are not used · src: galandStrongLinkMarine2018 (AB) · limit: access (note: "so it stays abstract only and its R2 values are not used") · trail: H2-01 §4.1, §answers, §Provenance · from: H2-01:B-0138, H2-01:B-0139, H2-01:A-059, H2-01:B-0015
- **levels-within-habitat.9** Revised processing (MUSiCC normalisation, filtering of prevalent families, non-uniform mapping) gave functional profiles that identified hosts as well as strain-level taxonomic markers did: a direct, measured same-habitat counter-result to functional stability.
  conf: not stated · class: meas (critic: C-123) · holds: human gut; verified against full text by the critic · src: manorRevisedComputationalMetagenomic2017 (FT, re-checked) · trail: H2-01 §critic, §Adversarial · from: H2-01:C-023, H2-01:C-024, H2-01:C-027, H2-01:C-051, H2-01:C-123
- **levels-within-habitat.10** The counter-evidence within a habitat is methodological and applies to every study above: relative normalisation and pathway aggregation reduce apparent functional variability, genome size creates both spurious variability and spurious stability, and a dominant mean profile makes profiles look alike, so the "levels stable, taxonomy variable" pattern depends on processing and annotation scheme.
  conf: not stated · class: not stated · holds: same-habitat comparisons of function levels and taxonomic composition · src: manorRevisedComputationalMetagenomic2017 (FT, re-checked), nayfachAverageGenomeSize2015, manorMUSiCCMarkerGenes2015, sunInferenceBasedAccuracyMetagenome2020 · trail: H2-01 §4.1, §answers · from: H2-01:B-0136, H2-01:B-0137, H2-01:B-0140, H2-01:A-057, H2-01:A-058
- **levels-within-habitat.11** Comparing a fine taxonomic table with a coarse functional table favours functional stability by construction, which applies equally to Burke2011 and Ramírez-Flandes2019.
  conf: not stated · class: reading (note: "reviewer's reading") · holds: comparisons of tables at different granularity · src: burkeBacterialCommunityAssembly2011, ramirezflandesRedoxTraitsCharacterize2019 · trail: H2-01 §4.1, §answers · from: H2-01:B-0137, H2-01:A-058
- **levels-within-habitat.12** Same-habitat comparisons using marker-normalised, unaggregated or all-read functional profiles alongside taxonomy at matched resolution have not been measured, nor have non-human habitats beyond a few microcosm and marine examples; none of the studies controls for normalisation, aggregation and granularity together.
  conf: not stated · class: search (note: "Not measured") · holds: function levels against taxonomic composition within a habitat · src: none (a statement of what was not measured) · search: not stated · trail: H2-01 §answers · from: H2-01:A-062, H2-01:A-064

### levels-across-habitats: function levels against taxonomic composition across habitats (case B)
needs: processing-effects
- **levels-across-habitats.1** Across habitats where taxonomy turns over, whether function tracks taxonomic composition is contested and incommensurable: the coupled and decoupled results use different function definitions (all reads or gene categories against taxonomy-derived groups) and different comparisons (distance-matrix correlation against variance partitioning), and cannot be pooled; the answer depends on annotation and resolution.
  conf: cont (critic: C-028) · class: not stated · holds: several measured studies in each direction, not commensurable, several single studies or abstract only · src: fiererCrossbiomeMetagenomicAnalyses2012, salazarGeneExpressionChanges2019, loucaDecouplingFunctionTaxonomy2016, nelsonGlobalBiogeographyMicrobial2016 · rating: "Weak to moderate" · trail: H2-01 §4.2, §answers, §6. Answers, §critic · from: H2-01:B-0141, H2-01:B-0149, H2-01:A-069, H2-01:A-073, H2-01:A-075, H2-01:A-076, H2-01:A-078, H2-01:A-114, H2-01:C-028
- **levels-across-habitats.2** Across 16 soils from five biomes, functional and taxonomic Bray-Curtis distances correlated (Mantel r = 0.76; with unweighted UniFrac, 0.82).
  conf: not stated · class: meas (marker) · holds: 16 soils from five biomes; small n; the coupled side of case B, which without this study would rest on one global ocean statement · src: fiererCrossbiomeMetagenomicAnalyses2012 (FT per trait-ecology angle; measured; small n) · limit: access (critic: C-061) · trail: H2-01 §4.2, §answers, §critic, §Adversarial, §Provenance · from: H2-01:I-0031, H2-01:A-070, H2-01:A-086, H2-01:C-032, H2-01:C-061, H2-01:B-0016
- **levels-across-habitats.3** In Tara Oceans, OG-level metagenomic and metatranscriptomic differentiation tracked taxonomic differentiation along latitude, and the authors conclude that "on a global scale, taxonomic composition largely shapes the composition of gene functional content".
  conf: not stated · class: meas (marker) · holds: global ocean (Tara Oceans); the critic: taxonomic and OG profiles come from the same reads and share compositional structure, which the review does not note · src: salazarGeneExpressionChanges2019 (FT; measured) · contrary: one-sided (critic: C-125) · trail: H2-01 §4.2, §answers, §Adversarial · from: H2-01:I-0032, H2-01:A-070, H2-01:C-125
- **levels-across-habitats.4** A CCA on phylogenetic composition agreed with functional trends across GOS.
  conf: not stated · class: not stated · holds: GOS ocean metagenomes · src: raesTowardMolecularTraitbased2011 (FT) · trail: H2-01 §4.2 · from: H2-01:B-0142
- **levels-across-habitats.5** Across 247 metagenomes from 18 biomes, function separated biomes more strongly than taxonomy: oxidoreductase profiles gave PERMANOVA F = 12.5 and all 6,789 KOs F = 10.7, against 1.8 for 4,011 species and 2.8 at fourth taxonomic rank, and functional and taxonomic diversity rankings of biomes did not correspond; the feature sets differ in size and sparsity, so the F statistics are not commensurable.
  conf: single (marker) · class: meas (marker) · holds: 247 metagenomes from 18 biomes; bears on which separates habitats more, a different question from coupling · src: ramirezflandesRedoxTraitsCharacterize2019 (FT; measured; SINGLE SOURCE) · trail: H2-01 §4.2, §answers · from: H2-01:B-0143, H2-01:I-0033, H2-01:B-0144, H2-01:A-071, H2-01:A-079
- **levels-across-habitats.6** Nine biomes were strongly discriminated by metabolic profiles.
  conf: not stated · class: not stated · holds: metagenomes from nine biomes · src: dinsdaleFunctionalMetagenomicProfiling2008 (AB) · trail: H2-01 §4.2 · from: H2-01:B-0145
- **levels-across-habitats.7** In the global ocean, environment strongly shaped functional-group distribution and weakly shaped taxonomy within groups, "roughly independent axes of variation".
  conf: not stated · class: deriv (marker) · holds: global ocean; derived, because functional groups were assigned from taxonomy; one of the two studies on the decoupled side of case B · src: loucaDecouplingFunctionTaxonomy2016 (AB; derived, because functional groups were assigned from taxonomy) · trail: H2-01 §4.2, §answers, §critic · from: H2-01:I-0034, H2-01:I-0001, H2-01:A-085, H2-01:C-030
- **levels-across-habitats.8** Soil nitrogen-pathway frequencies were explained by habitat and soil C and N, while taxonomy within N functional groups was poorly predicted by environment.
  conf: not stated · class: not stated · holds: soils; one of the two studies on the decoupled side of case B · src: nelsonGlobalBiogeographyMicrobial2016 (SEC/unverified; critic: C-059 was "FT via an automated summary; figures not re-verified") · limit: access (critic: C-058) · trail: H2-01 §4.2, §answers, §critic, §Adversarial · from: H2-01:B-0146, H2-01:I-0001, H2-01:C-029..031, H2-01:C-056..060
- **levels-across-habitats.9** At 95%-identity gene resolution, most genes were specific to one of 14 habitats.
  conf: not stated · class: not stated · holds: prokaryotic genes at 95% identity across 14 habitats · src: coelhoTowardsBiogeographyProkaryotic2021 (AB) · trail: H2-01 §4.2 · from: H2-01:R-0103, H2-01:B-0147
- **levels-across-habitats.10** At the level of core OG functions, more than 73% of ocean core-function abundance was shared with the human gut.
  conf: not stated · class: not stated · holds: ocean and human gut metagenomes · src: sunagawaStructureFunctionGlobal2015 (AB) · trail: H2-01 §4.2 · from: H2-01:B-0147
- **levels-across-habitats.11** Resolution decides much of the coupling question: the same data can support turnover or constancy depending on resolution.
  conf: not stated · class: not stated · holds: comparisons of function and taxonomy across habitats · src: coelhoTowardsBiogeographyProkaryotic2021, sunagawaStructureFunctionGlobal2015 · trail: H2-01 §4.2, §answers · from: H2-01:B-0148, H2-01:A-072
- **levels-across-habitats.12** Case B has not been measured with taxonomy and function at matched resolution and matched feature counts, or with marker-normalised functional profiles.
  conf: not stated · class: search (note: "Not measured") · holds: function levels against taxonomic composition across habitats · src: none (a statement of what was not measured) · search: not stated · trail: H2-01 §answers · from: H2-01:A-080, H2-01:A-081, H2-01:A-082

### taxonomy-fixed: function levels where habitat changes but taxonomy does not (case C)
needs: none
- **taxonomy-fixed.1** No microbial metagenomic study was found that holds taxonomy fixed while habitat varies and compares function levels.
  conf: not stated · class: search (note: "Not found by these routes") · holds: the review's search routes; the critic: transplant, common-garden and single-lineage-across-habitat designs are not listed among the routes searched · src: none (a search result) · search: searched, not found (note: "Not found by these routes") · rating: "Case C: absent" · trail: H2-01 §4.3, §Provenance, §answers, §critic · from: H2-01:B-0150, H2-01:B-0018, H2-01:A-074, H2-01:A-077, H2-01:A-080, H2-01:C-033, H2-01:C-034
- **taxonomy-fixed.2** Salazar et al. (2019) separate regulatory change (metatranscriptome) from community turnover in the ocean; per the search agent's reading, turnover dominated at global scale. This is the nearest item to case C and concerns expression, not gene content.
  conf: not stated · class: not stated · holds: global ocean metatranscriptomes · src: salazarGeneExpressionChanges2019 · trail: H2-01 §4.3 · from: H2-01:B-0151, H2-01:B-0152

### covariation-stability: stability of functional covariation against levels and composition (case D)
needs: covariation-transfer, community-weighted-means
- **covariation-stability.1** No microbial study was found that compares the between-habitat stability of function-function covariation with that of function levels or taxonomic composition.
  conf: not stated · class: search (note: "Not found by these routes") · holds: microbial metagenomes; search routes as for withheld habitats · src: none (a search result) · search: searched, not found (note: "Not found by these routes") · rating: "Absent for the microbial cross-habitat case" · trail: H2-01 §1. What, §Provenance, §answers, §6. Answers, §critic · from: H2-01:B-0038, H2-01:B-0018, H2-01:A-087, H2-01:A-094, H2-01:A-099, H2-01:A-117, H2-01:C-035
- **covariation-stability.2** Across four human gut cohorts that differ in disease state and population (IBD, obesity, two population cohorts), 64.3% of pathway co-abundances and 38.6% of species co-abundances differed in strength (Cochran's Q, FDR < 0.05): in this setting pathway covariation was less stable across cohorts than species covariation. This compares functional covariation with taxonomic covariation, not with taxonomic composition, and the cohorts differ in disease state and population, not habitat.
  conf: single (critic: C-080) · class: not stated · holds: one human gut study, one heterogeneity test; the closest microbial evidence and the only microbial measurement of functional covariation stability; shared-member and common-factor cautions apply; the critic: heterogeneity tests have more power for stronger and more numerous correlations, and pathway correlations are stronger and more numerous, so easier to detect as heterogeneous · src: chenGutMicrobialCoabundance2020 (FT, re-checked) · rating: "Weak (one study) for the microbial between-cohort case" · contrary: one-sided (critic: C-116) · trail: H2-01 §4.4, §1. What, §answers, §6. Answers, §critic, §Adversarial · from: H2-01:B-0039, H2-01:B-0153, H2-01:B-0155..0158, H2-01:A-088, H2-01:A-089, H2-01:A-095, H2-01:A-102, H2-01:A-115, H2-01:C-036, H2-01:C-039..041, H2-01:C-079..081, H2-01:C-116, H2-01:C-127
- **covariation-stability.3** Among the entities involved in variable co-abundances across the four gut cohorts, 84% of 304 pathways and also 76% of 100 species differed in level; the review reported only the pathway figure, which makes the pathway result look more distinctive than it is.
  conf: not stated · class: not stated · holds: four human gut cohorts differing in disease state · src: chenGutMicrobialCoabundance2020 (FT, re-checked) · contrary: one-sided (critic: C-118) · trail: H2-01 §4.4, §answers, §critic, §Adversarial · from: H2-01:B-0154, H2-01:A-088, H2-01:A-089, H2-01:C-037, H2-01:C-038, H2-01:C-055, H2-01:C-118
- **covariation-stability.4** Outside that study, covariation among microbial functions has only been fitted on pooled cross-habitat data, not compared between habitats; none of the pooled studies measures whether the covariation differs by habitat.
  conf: not stated · class: not stated · holds: microbial functional covariation · src: nelsonGlobalBiogeographyMicrobial2016, salazarGeneExpressionChanges2019, gianoulisQuantifyingEnvironmentalAdaptation2009, barberanExplorationCommunityTraits2011 · trail: H2-01 §4.4, §answers · from: H2-01:B-0160, H2-01:B-0161, H2-01:A-091
- **covariation-stability.5** Soil nitrogen-pathway frequencies were "overwhelmingly positively correlated" across 365 soils from 10 habitat types.
  conf: not stated · class: not stated · holds: 365 soils from 10 habitat types, pooled · src: nelsonGlobalBiogeographyMicrobial2016 · trail: H2-01 §4.4 · from: H2-01:B-0160
- **covariation-stability.6** Co-abundance and co-expression of ocean OGs predicted shared KEGG membership, fitted and scored on the same samples and partly circular.
  conf: not stated · class: not stated · holds: global ocean, pooled; fitted and scored on the same samples · src: salazarGeneExpressionChanges2019 (fitted and scored on the same samples; partly circular) · trail: H2-01 §4.4 · from: H2-01:R-0216, H2-01:B-0160
- **covariation-stability.7** Amino-acid transport and cofactor synthesis covaried in GOS metagenomes.
  conf: not stated · class: not stated · holds: GOS ocean metagenomes, pooled · src: gianoulisQuantifyingEnvironmentalAdaptation2009 (AB) · trail: H2-01 §4.4 · from: H2-01:B-0160
- **covariation-stability.8** Community genomic traits covaried in microbial metagenomes, some of the covariation possibly technical in origin.
  conf: not stated · class: not stated · holds: microbial metagenomes, pooled · src: barberanExplorationCommunityTraits2011 (AB) · trail: H2-01 §4.4 · from: H2-01:B-0160
- **covariation-stability.9** Community-weighted plant traits across 1.1 million plots showed the same two covariation axes as species-level traits, "unexpected" per the authors, while climate and soil explained only 10.8 to 14.0% of CWM variation: covariation more stable than levels.
  conf: single (marker) · class: meas (marker) · holds: plant communities (other field); the only large-scale case of covariation more stable than levels · src: bruelheideGlobalTraitenvironmentRelationships2018 (FT; measured; SINGLE SOURCE) · trail: H2-01 §4.4, §answers, §Adversarial · from: H2-01:B-0162, H2-01:I-0035, H2-01:A-092, H2-01:A-103, H2-01:C-120
- **covariation-stability.10** Precision-matrix plant trait networks differed among climate regions in density and modularity, with some edges present everywhere and others region-specific.
  conf: not stated · class: not stated · holds: plant traits (other field); heavy imputation · src: floresmorenoRobustnessTraitConnections2019 (FT; heavy imputation) · trail: H2-01 §4.4, §answers · from: H2-01:B-0162, H2-01:I-0036, H2-01:A-092
- **covariation-stability.11** Leaf-economic slopes shifted with climate.
  conf: not stated · class: not stated · holds: plant leaf traits (other field) · src: wrightModulationLeafEconomic2005 (AB) · trail: H2-01 §4.4, §answers · from: H2-01:B-0162, H2-01:I-0036, H2-01:A-092
- **covariation-stability.12** Along an aridity gradient, a height-seed mass covariance strengthened while level-type functional diversity was poorly explained by aridity.
  conf: single (marker) · class: not stated · holds: plant communities along an aridity gradient (other field) · src: dwyerConstraintsTraitCombinations2017 (AB; SINGLE SOURCE) · trail: H2-01 §4.4, §answers · from: H2-01:B-0162, H2-01:I-0036, H2-01:A-092
- **covariation-stability.13** A review reports plant trait-network topology shifting along resource gradients.
  conf: not stated · class: assert (marker) · holds: plant trait networks (other field) · src: hePlantTraitNetworks2020 (AB; asserted) · trail: H2-01 §4.4 · from: H2-01:B-0162, H2-01:I-0037
- **covariation-stability.14** In plant traits, the evidence on whether covariation is more stable than levels runs both ways, and each item is a single study; the plant sources differ in level (community against species), in imputation and in gradient.
  conf: cont (note: "Conflicts: Bruelheide2018 (covariation stable, levels variable) against FloresMoreno2019, Wright2005 and DwyerLaughlin2017 (covariation shifts with environment)") · class: not stated · holds: plant traits, another field; each item a single study · src: bruelheideGlobalTraitenvironmentRelationships2018, floresmorenoRobustnessTraitConnections2019, wrightModulationLeafEconomic2005, dwyerConstraintsTraitCombinations2017 · rating: "Mixed and other-field for plant traits and expression" · trail: H2-01 §4.4, §answers, §6. Answers, §critic · from: H2-01:B-0162, H2-01:A-092, H2-01:A-096..098, H2-01:A-116, H2-01:C-043
- **covariation-stability.15** Tissue-specific co-expression networks outperformed pooled ones, and modules conserved across tissues carried shared housekeeping functions.
  conf: single (critic: C-121) · class: not stated · holds: human tissues, transcriptomics (other field) · src: piersonSharingSpecificityCoexpression2015 (FT; SINGLE SOURCE; critic: C-121 was "FT") · trail: H2-01 §4.4, §answers, §Adversarial · from: H2-01:R-0204, H2-01:B-0164, H2-01:A-093, H2-01:C-121
- **covariation-stability.16** Covariation in presence/absence profiles, and comparison corrected for shared gene-set members, have not been measured across habitats.
  conf: not stated · class: search (note: "Not measured") · holds: microbial functional covariation · src: none (a statement of what was not measured) · search: not stated · trail: H2-01 §answers · from: H2-01:A-099

### temporal-covariation: temporal stability of functional covariation
needs: covariation-transfer
- **temporal-covariation.1** Between the first and last iHMP-IBD time points, about one year apart, 90.6% of species and 99.6% of pathway co-abundances showed no significant difference in strength (Cochran's Q, P > 0.05) in 77 individuals; this is a count of non-significant differences, an absence-of-evidence count at the same lenient bar the review criticises for replication, and should not be read as near-complete stability.
  conf: not stated · class: not stated · holds: one IBD cohort (iHMP-IBD), human gut, n = 77; the only microbial measurement · src: chenGutMicrobialCoabundance2020 (FT) · contrary: one-sided (critic: C-115) · trail: H2-01 §3.2, §4.5, §4.4, §answers, §Provenance, §critic, §Adversarial · from: H2-01:B-0101, H2-01:B-0107, H2-01:B-0165, H2-01:B-0159, H2-01:B-0014, H2-01:A-090, H2-01:C-042, H2-01:C-055, H2-01:C-066..068, H2-01:C-114, H2-01:C-115, H2-01:C-117
- **temporal-covariation.2** The review found no trait-ecology study of temporal CWM covariation; the critic notes that plant CWM time series were not searched and that the statement names no routes.
  conf: not stated · class: search (critic: C-102) · holds: trait ecology · src: none (a search result) · search: not searched (critic: C-102) · trail: H2-01 §4.5, §Adversarial · from: H2-01:B-0166, H2-01:C-102

### function-definition: what counts as a function, and failure modes
needs: dimensionality, dimension-elsewhere, levels-within-habitat, levels-across-habitats, other-field-transfer
- **function-definition.1** The reviewer's synthesis is that the answer to every direction depends on what is treated as "a function": coarse, aggregated, relatively normalised functions look stable, and fine, marker-normalised or all-read functions look more tied to taxonomy, with the measured pieces each a single study for its specific quantity; that they also differ in dimension (coarse functions looking low-dimensional, fine ones higher-dimensional) is the reviewer's inference, which no cited source measured.
  conf: single (note: "each is a single study for its specific quantity") · class: reading (critic: C-130) · holds: the measured pieces cover annotation granularity, normalisation, mapping and all-read comparison; none of them measured dimension · src: manorRevisedComputationalMetagenomic2017, manorMUSiCCMarkerGenes2015, nayfachAverageGenomeSize2015, sunInferenceBasedAccuracyMetagenome2020, coelhoTowardsBiogeographyProkaryotic2021, galandStrongLinkMarine2018 (abstract) · trail: H2-01 §5. How, §critic, §Adversarial · from: H2-01:B-0167..0169, H2-01:C-053, H2-01:C-076..078, H2-01:C-129, H2-01:C-130
- **function-definition.2** In transcriptomics, low dimensionality within datasets coexists with unstable higher components across datasets and partial transfer across tissue types, which the review reads as the same pattern.
  conf: not stated · class: not stated · holds: transcriptomics, another field · src: heimbergLowDimensionalityGene2016, lenzPrincipalComponentsAnalysis2016, clearyEfficientGenerationTranscriptomic2017 · trail: H2-01 §5. How · from: H2-01:B-0170
- **function-definition.3** Failure modes to expect in this literature are dimension estimates dominated by a mean profile; a genome-size axis that is partly technical; covariation between gene sets that share members; per-sample correlation metrics that ignore across-sample variance; comparisons of tables at different granularity; covariation inherited from imputation (plant traits); and replication judged against lenient thresholds with strong common factors.
  conf: not stated · class: not stated · holds: the literature the review covered · src: chenGutMicrobialCoabundance2020 · trail: H2-01 §5. How · from: H2-01:B-0171

## Do not say

- **dns.1** "Microbial functional profiles are dominated by a shared mean, while across genomes metabolic content is high-dimensional."
  why: The evidence is a per-sample accuracy metric under permutation and descriptive HMP statements from human-associated and a few soil datasets, not a decomposition of a sample-by-function matrix, and the sentence merges sample-level functional profiles, genome-level presence/absence and a per-sample accuracy metric into one characterisation of "functional profiles". · instead: shared-mean-profile.4, dimension-elsewhere.1 · trail: H2-01 §critic, §Adversarial · from: H2-01:C-005, H2-01:A-108, H2-01:C-002, H2-01:C-052, H2-01:C-074, H2-01:C-128
- **dns.2** "Across genomes, metabolic presence/absence is high-dimensional, with dozens to hundreds of coordinates."
  why: This rests on one modelled study (diffusion maps across genera) and is phrased as a property of genomes in general. · instead: dimension-elsewhere.1 · trail: H2-01 §critic, §Adversarial · from: H2-01:I-0013, H2-01:A-011, H2-01:C-007, H2-01:C-070
- **dns.3** "Gene expression data are low-dimensional within datasets."
  why: The within-dataset result rests on one study that the review did not flag SINGLE SOURCE while flagging the opposing study; the labelling is asymmetric. · instead: dimension-elsewhere.12, dimension-elsewhere.14 · trail: H2-01 §Adversarial · from: H2-01:A-012, H2-01:C-071..073
- **dns.4** "Normalisation, pathway aggregation and compositional closure lower the apparent dimension of functional profiles."
  why: That these shifts lower apparent dimension is the reviewer's inference, correctly marked in Section 2.3 and the D1 answer but dropped in the Section 6 summary; no cited source measured dimension under these choices. · instead: dimensionality.12 · trail: H2-01 §Adversarial · from: H2-01:A-106, H2-01:C-131
- **dns.5** "Module dictionaries recovered held-out expression profiles at about 87% within a tumour type and 68% across tumour types."
  why: The 87% and 68% are Spearman recovery of expression from 25 simulated random composite measurements through a learned dictionary (compressed sensing), not a direct covariance-reproduction score; the answer states the transfer more directly than the full text supports. · instead: other-field-transfer.1 · trail: H2-01 §critic, §Adversarial · from: H2-01:A-037, H2-01:C-019, H2-01:C-020, H2-01:C-063..065
- **dns.6** "Across fields, transfer depends on similarity between training and target, breadth of training, and how much of the target is shared mean structure."
  why: The sentence pools incommensurable transfer tests of different quantities (covariance or dictionary transfer, taxon-to-gene mapping accuracy, per-sample accuracy metrics, phylogenetic gene gain/loss prediction); breadth rests on one qualitative study, and the whole is the reviewer's synthesis, not a finding. · instead: transfer-dependence.1 · trail: H2-01 §critic, §Adversarial · from: H2-01:A-041, H2-01:A-112, H2-01:C-016..018, H2-01:C-054, H2-01:C-075, H2-01:C-126
- **dns.7** "Galand et al. (2018) is the only direct same-habitat result contrary to function levels being more stable than taxonomic composition."
  why: Manor and Borenstein's full text (2017) directly measures that revised functional profiles identify hosts as well as strain-level taxonomy does, so contrary same-habitat evidence also exists in full text, and Galand et al. (2018) is abstract only. · instead: levels-within-habitat.1, levels-within-habitat.9 · trail: H2-01 §critic · from: H2-01:C-021, H2-01:C-023, H2-01:B-0072, H2-01:A-068, H2-01:C-026, H2-01:C-050, H2-01:C-051
- **dns.8** "How far function tracks taxonomy is itself habitat-dependent."
  why: This rests on one modelled, abstract-only study comparing gut and vaginal communities. · instead: levels-within-habitat.6 · trail: H2-01 §Adversarial · from: H2-01:I-0030, H2-01:C-082
- **dns.9** "Across habitats, functional covariation was less stable than taxonomic covariation."
  why: The finding is from one human gut study with one heterogeneity test, whose cohorts differ in disease state and population, not habitat; it compares pathway covariation with species covariation, not with composition; and heterogeneity tests have more power for the stronger, more numerous pathway correlations. · instead: covariation-stability.2 · trail: H2-01 §critic, §Adversarial · from: H2-01:C-036, H2-01:A-089, H2-01:C-039..041, H2-01:C-079..081, H2-01:C-116, H2-01:C-127
- **dns.10** "Pathway covariation changes came with changes in pathway levels: 84% of the 304 pathways involved also differed in level."
  why: Reported alone, the pathway figure looks more distinctive than it is: the same study found that 76% of 100 species involved in variable co-abundances also differed in level. · instead: covariation-stability.3 · trail: H2-01 §critic, §Adversarial · from: H2-01:C-037, H2-01:C-038, H2-01:C-118
- **dns.11** "Pathway co-abundances were almost fully stable over about a year (99.6%)."
  why: The 99.6% is a count of co-abundances with no significant difference (Cochran's Q, P > 0.05) in 77 individuals, an absence-of-evidence count at a lenient bar, so it should not be read as near-complete stability. · instead: temporal-covariation.1 · trail: H2-01 §critic, §Adversarial · from: H2-01:A-090, H2-01:C-042, H2-01:C-066..068
- **dns.12** "Coarse, aggregated functions look low-dimensional and stable, while fine, marker-normalised or all-read functions look higher-dimensional and more tied to taxonomy."
  why: No cited source estimated dimension for fine against coarse functions; the sentence merges annotation granularity, normalisation, mapping and all-read comparison into one axis and presents the reviewer's synthesis as a pattern that measured pieces establish. · instead: function-definition.1 · trail: H2-01 §critic, §Adversarial · from: H2-01:B-0168, H2-01:C-053, H2-01:C-076..078, H2-01:C-129, H2-01:C-130

## Gaps

- **gap.1** Network rewiring and differential co-occurrence across habitats in microbial data (taxonomic or functional): microbial co-occurrence network comparisons across habitats and body sites (soil drought or warming networks, cross-biome network topology, body-site network differences).
  blocks: covariation-stability · origin: critic coverage gap; only one study (Chen2020) is covered, the Faust 2012 co-occurrence study was not obtained, and no cross-biome network comparisons or stress-driven rewiring studies appear · search: not stated · src: faustMicrobialCooccurrenceRelationships2012 · from: H2-01:C-098..101
- **gap.2** Temporal stability of functional covariation beyond one IBD cohort: longitudinal metagenome and metatranscriptome series (human gut longitudinal cohorts, marine time-series stations) and repeated-survey CWM data.
  blocks: temporal-covariation · origin: critic coverage gap · search: not searched (critic: C-102) · from: H2-01:C-102
- **gap.3** Held-out transfer of residual or covariance structure in community ecology: tests of joint species distribution model (HMSC and similar) transferability to new regions or communities, the closest other-field analogue of a withheld habitat.
  blocks: covariation-transfer · origin: critic coverage gap; also named by the note's stage-2 check · search: not stated · from: H2-01:C-103, H2-01:B-0025
- **gap.4** Held-out transfer in other omics fields beyond bulk transcriptomics: single-cell reference mapping and latent-space transfer across tissues or species; proteomics and metabolomics covariance transfer.
  blocks: other-field-transfer · origin: critic coverage gap · search: not stated · from: H2-01:C-104
- **gap.5** Formal rank estimation on microbiome matrices under compositional transforms (cross-validated NMF or PCA, robust Aitchison PCA, random-matrix thresholds, sample-size subsampling), including any held-out rank estimate for functional profiles; the empirical dependence of rank on p/n is left to one species-trait study.
  blocks: dimensionality · origin: critic coverage gap and the note's stage-2 check; Raguideau 2016, Jiang et al. 2012 (J Math Biol), Johnstone 2001 and Gavish and Donoho 2014 were not obtained · search: not stated · src: raguideauInferringAggregatedFunctional2016, jiangNonnegativeMatrixFactorization2011, johnstoneDistributionLargestEigenvalue2001, gavishOptimalHardThreshold2014, mouillotDimensionalityStructureSpecies2021 · from: H2-01:C-105..107, H2-01:B-0024, H2-01:A-020
- **gap.6** Presence/absence against abundance for sample-level functional profiles: gene or KO presence/absence matrices across metagenome samples or MAG collections by habitat; the only presence/absence source is across genomes, not across samples.
  blocks: dimensionality · origin: critic coverage gap · search: not stated · src: fahimipourMappingBacterialMetabolic2020a · from: H2-01:C-108
- **gap.7** Methodological caution on sequencing approach for composition: 16S amplicon against shotgun taxonomic profiling, and OTU, ASV and species-level resolution effects on beta diversity and turnover estimates; resolution is discussed only through two abstracts.
  blocks: levels-across-habitats, levels-within-habitat · origin: critic coverage gap; the brief asks for it explicitly · search: not stated · src: coelhoTowardsBiogeographyProkaryotic2021, sunagawaStructureFunctionGlobal2015 · from: H2-01:C-109
- **gap.8** Correction for shared gene-set members in covariance or correlation: gene-set overlap correction methods in expression analysis, and pathway-pathway correlation with shared genes; only a significance-crosstalk study (abstract) is cited.
  blocks: processing-effects, covariation-transfer, covariation-stability · origin: critic coverage gap · search: not stated · src: donatoAnalysisCorrectionCrosstalk2013 · from: H2-01:C-110
- **gap.9** Case C nearest precedents: reciprocal transplant and common-garden experiments with microbial communities, single-species pangenomes (conspecific strains) across hosts or habitats, and synthetic communities across media.
  blocks: taxonomy-fixed · origin: critic coverage gap; also named by the note's stage-2 check · search: not searched (critic: C-111) · from: H2-01:C-111, H2-01:B-0026
- **gap.10** Held-out tests of functional prediction in non-human habitats: soil, marine and engineered-system validations, including the PICRUSt2 and Tax4Fun2 cross-habitat validations, which were not obtained although the answer relies on Langille 2013 for the habitat-dependence of transfer.
  blocks: neighbouring-transfer, covariation-transfer · origin: critic coverage gap and the note's stage-2 check · search: not stated · src: douglasPicrust2PredictionMetagenome2020, wemheuerTax4fun2PredictionHabitatSpecific2020 · from: H2-01:C-112, H2-01:B-0025, H2-01:A-050
- **gap.11** Dimension compared by habitat: habitat-stratified decompositions, for example per-biome NMF or PCA in multi-biome metagenome atlases.
  blocks: dimensionality · origin: critic coverage gap; noted as not measured, but no route targeted it · search: not searched (critic: C-113) · from: H2-01:C-113, H2-01:A-021
- **gap.12** A targeted follow-up on the rank-estimation literature and on held-out functional validations outside human habitats, sized separately: the note's stage-2 routing condition was triggered on both arms.
  blocks: dimensionality, neighbouring-transfer · origin: the note's stage-2 check · search: not stated · from: H2-01:B-0022, H2-01:B-0023, H2-01:B-0027
- **gap.13** Full-text verification of the load-bearing figures for the two sides of case B: Fierer 2012's Mantel r values were read in full text by one search angle only, and Nelson 2016 was read only through an automated summary; PMC returns for both contained only the abstract.
  blocks: levels-across-habitats · origin: critic access findings and the note's provenance · search: not stated · src: fiererCrossbiomeMetagenomicAnalyses2012, nelsonGlobalBiogeographyMicrobial2016 · from: H2-01:C-058, H2-01:C-061, H2-01:B-0016
- **gap.14** Galand 2018 in full text: attempts to reach it failed, so it stays abstract only and its R² values are not used, although it is direct same-habitat contrary evidence.
  blocks: levels-within-habitat · origin: a source not obtained in full that matters · search: not stated · src: galandStrongLinkMarine2018 · from: H2-01:B-0015, H2-01:C-027
- **gap.15** Comparisons of function and taxonomy at matched resolution and feature counts, with marker-normalised, unaggregated or all-read functional profiles, within and across habitats.
  blocks: levels-within-habitat, levels-across-habitats · origin: the note's not-measured lists · search: not stated · from: H2-01:A-064, H2-01:A-081, H2-01:A-082

## Out of scope

- H2-01:A-022..024, H2-01:A-051, H2-01:A-052, H2-01:A-065, H2-01:A-066, H2-01:A-083, H2-01:A-084, H2-01:A-100, H2-01:A-101: access basis of the answers (provenance; applied in Sources and in each src label, with the critic's access corrections)
- H2-01:A-025: heading of the D1 single-source sensitivity list (its items are in the claims they concern)
- H2-01:A-029: the D2 question heading (routing, not a finding)
- H2-01:A-109: pointer to the structured answers (navigation)
- H2-01:C-046..048: the critic's own full-text checks of load-bearing sources (provenance; the figures matched)
- H2-01:C-049: count of the over-reaches itemised in C-050 to C-055
- H2-01:C-083..097: reference corrections and Crossref checks, applied in Sources
- H2-01:C-132..134: expectation-echo check of the brief's framing (provenance)

## Sources

```bibtex
@article{airaFasterTurnoverTaxonomic2026,
  author = {Aira, Manuel and Pérez-Losada, Marcos and Crandall, Keith A. and Domínguez, Jorge},
  title = {Faster turnover of taxonomic over functional bacterial composition during vermicomposting indicates increasing functional redundancy},
  journal = {PLOS One},
  year = {2026},
  volume = {21},
  number = {7},
  pages = {e0354276},
  doi = {10.1371/journal.pone.0354276},
  note = {access: abstract_only; cited as: H2-01 [Aira2026]}
}

@article{alnebergEcosystemwideMetagenomicBinning2020,
  author = {Alneberg, Johannes and Bennke, Christin and Beier, Sara and Bunse, Carina and Quince, Christopher and Ininbergs, Karolina and Riemann, Lasse and Ekman, Martin and Jürgens, Klaus and Labrenz, Matthias and Pinhassi, Jarone and Andersson, Anders F.},
  title = {Ecosystem-wide metagenomic binning enables prediction of ecological niches from genomes},
  journal = {Communications Biology},
  year = {2020},
  volume = {3},
  pages = {119},
  doi = {10.1038/s42003-020-0856-x},
  note = {access: full_text; cited as: H2-01 [Alneberg2020]}
}

@article{andereggWithinspeciesPatternsChallenge2018,
  author = {Anderegg, Leander D. L. and Berner, Logan T. and Badgley, Grayson and Sethi, Meera L. and Law, Beverly E. and HilleRisLambers, Janneke},
  title = {Within-species patterns challenge our understanding of the leaf economics spectrum},
  journal = {Ecology Letters},
  year = {2018},
  volume = {21},
  number = {5},
  pages = {734-744},
  doi = {10.1111/ele.12945},
  note = {access: abstract_only; cited as: H2-01 [Anderegg2018]}
}

@article{barberanExplorationCommunityTraits2011,
  author = {Barberán, Albert and Fernández-Guerra, Antoni and Bohannan, Brendan J. M. and Casamayor, Emilio O.},
  title = {Exploration of community traits as ecological markers in microbial metagenomes},
  journal = {Molecular Ecology},
  year = {2012},
  volume = {21},
  number = {8},
  pages = {1909-1917},
  doi = {10.1111/j.1365-294X.2011.05383.x},
  note = {access: abstract_only; cited as: H2-01 [Barberan2012]}
}

@article{beavanContingencyRepeatabilityPredictability2023,
  author = {Beavan, Alan J. S. and Domingo-Sananes, Maria Rosa and McInerney, James O.},
  title = {Contingency, repeatability, and predictability in the evolution of a prokaryotic pangenome},
  journal = {Proceedings of the National Academy of Sciences of the USA},
  year = {2024},
  volume = {121},
  number = {1},
  pages = {e2304934120},
  doi = {10.1073/pnas.2304934120},
  note = {access: full_text; cited as: H2-01 [Beavan2024]; the note adds: Crossref issued date 2023, online; volume 121 is 2024; critic H2-01:C-092..094: Crossref gives the issue year as 2024, not 2023; the citation itself is correct}
}

@article{borgySensitivityCommunitylevelTraitenvironment2017,
  author = {Borgy, Benjamin and Violle, Cyrille and Choler, Philippe and Garnier, Eric and Kattge, Jens and Loranger, Jessy and Amiaud, Bernard and Cellier, Pierre and Debarros, Guilhem and Denelle, Pierre and Diquelou, Sylvain and Gachet, Sophie and Jolivet, Claudy and Lavorel, Sandra and Lemauviel-Lavenant, Servane and Mikolajczak, Alexis and Munoz, François and Olivier, Jean and Viovy, Nicolas},
  title = {Sensitivity of community-level trait-environment relationships to data representativeness: A test for functional biogeography},
  journal = {Global Ecology and Biogeography},
  year = {2017},
  volume = {26},
  number = {6},
  pages = {729-739},
  doi = {10.1111/geb.12573},
  note = {access: abstract_only; cited as: H2-01 [Borgy2017]}
}

@article{bruelheideGlobalTraitenvironmentRelationships2018,
  author = {Bruelheide, Helge and Dengler, Jürgen and Purschke, Oliver and Lenoir, Jonathan and Jiménez-Alfaro, Borja and Hennekens, Stephan M. and Botta-Dukát, Zoltán and Chytrý, Milan and Field, Richard and Jansen, Florian and Kattge, Jens and Pillar, Valério D. and Schrodt, Franziska and Mahecha, Miguel D. and Peet, Robert K. and Sandel, Brody and van Bodegom, Peter and Altman, Jan and Alvarez-Dávila, Esteban and Arfin Khan, Mohammed A. S. and Attorre, Fabio and Aubin, Isabelle and Baraloto, Christopher and Barroso, Jorcely G. and Bauters, Marijn and Bergmeier, Erwin and Biurrun, Idoia and Bjorkman, Anne D. and Blonder, Benjamin and Čarni, Andraž and Cayuela, Luis and Černý, Tomáš and Cornelissen, J. Hans C. and Craven, Dylan and Dainese, Matteo and Derroire, Géraldine and De Sanctis, Michele and Díaz, Sandra and Doležal, Jiří and Farfan-Rios, William and Feldpausch, Ted R. and Fenton, Nicole J. and Garnier, Eric and Guerin, Greg R. and Gutiérrez, Alvaro G. and Haider, Sylvia and Hattab, Tarek and Henry, Greg and Hérault, Bruno and Higuchi, Pedro and Hölzel, Norbert and Homeier, Jürgen and Jentsch, Anke and Jürgens, Norbert and Kącki, Zygmunt and Karger, Dirk N. and Kessler, Michael and Kleyer, Michael and Knollová, Ilona and Korolyuk, Andrey Y. and Kühn, Ingolf and Laughlin, Daniel C. and Lens, Frederic and Loos, Jacqueline and Louault, Frédérique and Lyubenova, Mariyana I. and Malhi, Yadvinder and Marcenò, Corrado and Mencuccini, Maurizio and Müller, Jonas V. and Munzinger, Jérôme and Myers-Smith, Isla H. and Neill, David A. and Niinemets, Ülo and Orwin, Kate H. and Ozinga, Wim A. and Penuelas, Josep and Pérez-Haase, Aaron and Petřík, Petr and Phillips, Oliver L. and Pärtel, Meelis and Reich, Peter B. and Römermann, Christine and Rodrigues, Arthur V. and Sabatini, Francesco Maria and Sardans, Jordi and Schmidt, Marco and Seidler, Gunnar and Silva Espejo, Javier Eduardo and Silveira, Marcos and Smyth, Anita and Sporbert, Maria and Svenning, Jens-Christian and Tang, Zhiyao and Thomas, Raquel and Tsiripidis, Ioannis and Vassilev, Kiril and Violle, Cyrille and Virtanen, Risto and Weiher, Evan and Welk, Erik and Wesche, Karsten and Winter, Marten and Wirth, Christian and Jandt, Ute},
  title = {Global trait-environment relationships of plant communities},
  journal = {Nature Ecology & Evolution},
  year = {2018},
  volume = {2},
  number = {12},
  pages = {1906-1917},
  doi = {10.1038/s41559-018-0699-8},
  note = {access: full_text (FT, author-accepted version; author list from Crossref); cited as: H2-01 [Bruelheide2018]}
}

@article{burkeBacterialCommunityAssembly2011,
  author = {Burke, Catherine and Steinberg, Peter and Rusch, Doug and Kjelleberg, Staffan and Thomas, Torsten},
  title = {Bacterial community assembly based on functional genes rather than species},
  journal = {Proceedings of the National Academy of Sciences of the USA},
  year = {2011},
  volume = {108},
  number = {34},
  pages = {14288-14293},
  doi = {10.1073/pnas.1101591108},
  note = {access: full_text; cited as: H2-01 [Burke2011]}
}

@article{chenGutMicrobialCoabundance2020,
  author = {Chen, Lianmin and Collij, Valerie and Jaeger, Martin and van den Munckhof, Inge C. L. and Vich Vila, Arnau and Kurilshikov, Alexander and Gacesa, Ranko and Sinha, Trishla and Oosting, Marije and Joosten, Leo A. B. and Rutten, Joost H. W. and Riksen, Niels P. and Xavier, Ramnik J. and Kuipers, Folkert and Wijmenga, Cisca and Zhernakova, Alexandra and Netea, Mihai G. and Weersma, Rinse K. and Fu, Jingyuan},
  title = {Gut microbial co-abundance networks show specificity in inflammatory bowel disease and obesity},
  journal = {Nature Communications},
  year = {2020},
  volume = {11},
  pages = {4018},
  doi = {10.1038/s41467-020-17840-y},
  note = {access: full_text (FT, re-checked by reviewer); cited as: H2-01 [Chen2020]}
}

@article{chungAssemblingBacterialPuzzles2024,
  author = {Chung, Henri C. and Friedberg, Iddo and Bromberg, Yana},
  title = {Assembling bacterial puzzles: piecing together functions into microbial pathways},
  journal = {NAR Genomics and Bioinformatics},
  year = {2024},
  volume = {6},
  number = {3},
  pages = {lqae109},
  doi = {10.1093/nargab/lqae109},
  note = {access: abstract_only; cited as: H2-01 [Chung2024]}
}

@article{clearyEfficientGenerationTranscriptomic2017,
  author = {Cleary, Brian and Cong, Le and Cheung, Anthea and Lander, Eric S. and Regev, Aviv},
  title = {Efficient generation of transcriptomic profiles by random composite measurements},
  journal = {Cell},
  year = {2017},
  volume = {171},
  number = {6},
  pages = {1424-1436.e18},
  doi = {10.1016/j.cell.2017.10.023},
  note = {access: full_text; cited as: H2-01 [Cleary2017]}
}

@article{coelhoTowardsBiogeographyProkaryotic2021,
  author = {Coelho, Luis Pedro and Alves, Renato and Rodríguez del Río, Álvaro and Myers, Pernille Neve and Cantalapiedra, Carlos P. and Giner-Lamia, Joaquín and Schmidt, Thomas Sebastian and Mende, Daniel R. and Orakov, Askarbek and Letunic, Ivica and Hildebrand, Falk and Van Rossum, Thea and Forslund, Sofia K. and Khedkar, Supriya and Maistrenko, Oleksandr M. and Pan, Shaojun and Jia, Longhao and Ferretti, Pamela and Sunagawa, Shinichi and Zhao, Xing-Ming and Nielsen, Henrik Bjørn and Huerta-Cepas, Jaime and Bork, Peer},
  title = {Towards the biogeography of prokaryotic genes},
  journal = {Nature},
  year = {2022},
  volume = {601},
  number = {7892},
  pages = {252-256},
  doi = {10.1038/s41586-021-04233-4},
  note = {access: abstract_only; cited as: H2-01 [Coelho2022]}
}

@article{crowExploitingSinglecellExpression2016,
  author = {Crow, Megan and Paul, Anirban and Ballouz, Sara and Huang, Z. Josh and Gillis, Jesse},
  title = {Exploiting single-cell expression to characterize co-expression replicability},
  journal = {Genome Biology},
  year = {2016},
  volume = {17},
  pages = {101},
  doi = {10.1186/s13059-016-0964-6},
  note = {access: full_text; cited as: H2-01 [Crow2016]}
}

@article{dinsdaleFunctionalMetagenomicProfiling2008,
  author = {Dinsdale, Elizabeth A. and Edwards, Robert A. and Hall, Dana and Angly, Florent and Breitbart, Mya and Brulc, Jennifer M. and Furlan, Mike and Desnues, Christelle and Haynes, Matthew and Li, Linlin and McDaniel, Lauren and Moran, Mary Ann and Nelson, Karen E. and Nilsson, Christina and Olson, Robert and Paul, John and Rodriguez Brito, Beltran and Ruan, Yijun and Swan, Brandon K. and Stevens, Rick and Valentine, David L. and Vega Thurber, Rebecca and Wegley, Linda and White, Bryan A. and Rohwer, Forest},
  title = {Functional metagenomic profiling of nine biomes},
  journal = {Nature},
  year = {2008},
  volume = {452},
  number = {7187},
  pages = {629-632},
  doi = {10.1038/nature06810},
  note = {access: abstract_only; cited as: H2-01 [Dinsdale2008]}
}

@article{donatoAnalysisCorrectionCrosstalk2013,
  author = {Donato, Michele and Xu, Zhonghui and Tomoiaga, Alin and Granneman, James G. and MacKenzie, Robert G. and Bao, Riyue and Than, Nandor Gabor and Westfall, Peter H. and Romero, Roberto and Draghici, Sorin},
  title = {Analysis and correction of crosstalk effects in pathway analysis},
  journal = {Genome Research},
  year = {2013},
  volume = {23},
  number = {11},
  pages = {1885-1893},
  doi = {10.1101/gr.153551.112},
  note = {access: abstract_only; cited as: H2-01 [Donato2013]}
}

@article{dwyerConstraintsTraitCombinations2017,
  author = {Dwyer, John M. and Laughlin, Daniel C.},
  title = {Constraints on trait combinations explain climatic drivers of biodiversity: the importance of trait covariance in community assembly},
  journal = {Ecology Letters},
  year = {2017},
  volume = {20},
  number = {7},
  pages = {872-882},
  doi = {10.1111/ele.12781},
  note = {access: abstract_only; cited as: H2-01 [DwyerLaughlin2017]}
}

@article{engTaxafunctionRobustnessMicrobial2018,
  author = {Eng, Alexander and Borenstein, Elhanan},
  title = {Taxa-function robustness in microbial communities},
  journal = {Microbiome},
  year = {2018},
  volume = {6},
  pages = {45},
  doi = {10.1186/s40168-018-0425-4},
  note = {access: abstract_only; cited as: H2-01 [EngBorenstein2018]}
}

@article{fahimipourMappingBacterialMetabolic2020a,
  author = {Fahimipour, Ashkaan K. and Gross, Thilo},
  title = {Mapping the bacterial metabolic niche space},
  journal = {Nature Communications},
  year = {2020},
  volume = {11},
  pages = {4887},
  doi = {10.1038/s41467-020-18695-z},
  note = {access: full_text; cited as: H2-01 [Fahimipour2020]}
}

@article{fiererCrossbiomeMetagenomicAnalyses2012,
  author = {Fierer, Noah and Leff, Jonathan W. and Adams, Byron J. and Nielsen, Uffe N. and Bates, Scott Thomas and Lauber, Christian L. and Owens, Sarah and Gilbert, Jack A. and Wall, Diana H. and Caporaso, J. Gregory},
  title = {Cross-biome metagenomic analyses of soil microbial communities and their functional attributes},
  journal = {Proceedings of the National Academy of Sciences of the USA},
  year = {2012},
  volume = {109},
  number = {52},
  pages = {21390-21395},
  doi = {10.1073/pnas.1215210110},
  note = {access: full_text (FT per trait-ecology angle; other angles AB; PMC E-utilities returns contained only the abstract; critic: H2-01:C-061: read in full text by one angle only, not re-opened by the reviewer); cited as: H2-01 [Fierer2012]}
}

@article{flinkstromMetagenomicClusteringLinks2024,
  author = {Flinkstrom, Zachary and Bryson, Samuel and Candry, Pieter and Winkler, Mari-Karoliina H.},
  title = {Metagenomic clustering links specific metabolic functions to globally relevant ecosystems},
  journal = {mSystems},
  year = {2024},
  volume = {9},
  number = {8},
  pages = {e00573-24},
  doi = {10.1128/msystems.00573-24},
  note = {access: full_text; cited as: H2-01 [Flinkstrom2024]}
}

@article{floresmorenoRobustnessTraitConnections2019,
  author = {Flores-Moreno, Habacuc and Fazayeli, Farideh and Banerjee, Arindam and Datta, Abhirup and Kattge, Jens and Butler, Ethan E. and Atkin, Owen K. and Wythers, Kirk and Chen, Ming and Anand, Madhur and Bahn, Michael and Byun, Chaeho and Cornelissen, J. Hans C. and Craine, Joseph and Gonzalez-Melo, Andres and Hattingh, Wesley N. and Jansen, Steven and Kraft, Nathan J. B. and Kramer, Koen and Laughlin, Daniel C. and Minden, Vanessa and Niinemets, Ülo and Onipchenko, Vladimir and Peñuelas, Josep and Soudzilovskaia, Nadejda A. and Dalrymple, Rhiannon L. and Reich, Peter B.},
  title = {Robustness of trait connections across environmental gradients and growth forms},
  journal = {Global Ecology and Biogeography},
  year = {2019},
  volume = {28},
  number = {12},
  pages = {1806-1826},
  doi = {10.1111/geb.12996},
  note = {access: full_text (FT, accepted version); cited as: H2-01 [FloresMoreno2019]}
}

@article{friouxEnterosignaturesDefineCommon2023,
  author = {Frioux, Clémence and Ansorge, Rebecca and Özkurt, Ezgi and Ghassemi Nedjad, Chabname and Fritscher, Joachim and Quince, Christopher and Waszak, Sebastian M. and Hildebrand, Falk},
  title = {Enterosignatures define common bacterial guilds in the human gut microbiome},
  journal = {Cell Host & Microbe},
  year = {2023},
  volume = {31},
  number = {7},
  pages = {1111-1125.e6},
  doi = {10.1016/j.chom.2023.05.024},
  note = {access: abstract_only; cited as: H2-01 [Frioux2023]}
}

@article{galandStrongLinkMarine2018,
  author = {Galand, Pierre E. and Pereira, Olivier and Hochart, Corentin and Auguet, Jean Christophe and Debroas, Didier},
  title = {A strong link between marine microbial community composition and function challenges the idea of functional redundancy},
  journal = {The ISME Journal},
  year = {2018},
  volume = {12},
  number = {10},
  pages = {2470-2478},
  doi = {10.1038/s41396-018-0158-1},
  note = {access: abstract_only (AB; one angle read an automated page summary only); cited as: H2-01 [Galand2018]}
}

@article{gianoulisQuantifyingEnvironmentalAdaptation2009,
  author = {Gianoulis, Tara A. and Raes, Jeroen and Patel, Prianka V. and Bjornson, Robert and Korbel, Jan O. and Letunic, Ivica and Yamada, Takuji and Paccanaro, Alberto and Jensen, Lars J. and Snyder, Michael and Bork, Peer and Gerstein, Mark B.},
  title = {Quantifying environmental adaptation of metabolic pathways in metagenomics},
  journal = {Proceedings of the National Academy of Sciences of the USA},
  year = {2009},
  volume = {106},
  number = {5},
  pages = {1374-1379},
  doi = {10.1073/pnas.0808022106},
  note = {access: abstract_only; cited as: H2-01 [Gianoulis2009]}
}

@article{gowdaGenomicStructurePredicts2022,
  author = {Gowda, Karna and Ping, Derek and Mani, Madhav and Kuehn, Seppe},
  title = {Genomic structure predicts metabolite dynamics in microbial communities},
  journal = {Cell},
  year = {2022},
  volume = {185},
  number = {3},
  pages = {530-546.e25},
  doi = {10.1016/j.cell.2021.12.036},
  note = {access: abstract_only; cited as: H2-01 [Gowda2022]}
}

@article{hePlantTraitNetworks2020,
  author = {He, Nianpeng and Li, Ying and Liu, Congcong and Xu, Li and Li, Mingxu and Zhang, Jiahui and He, Jinsheng and Tang, Zhiyao and Han, Xingguo and Ye, Qing and Xiao, Chunwang and Yu, Qiang and Liu, Shirong and Sun, Wei and Niu, Shuli and Li, Shenggong and Sack, Lawren and Yu, Guirui},
  title = {Plant trait networks: improved resolution of the dimensionality of adaptation},
  journal = {Trends in Ecology & Evolution},
  year = {2020},
  volume = {35},
  number = {10},
  pages = {908-918},
  doi = {10.1016/j.tree.2020.06.003},
  note = {access: abstract_only; type: review; cited as: H2-01 [He2020]}
}

@article{heimbergLowDimensionalityGene2016,
  author = {Heimberg, Graham and Bhatnagar, Rajat and El-Samad, Hana and Thomson, Matt},
  title = {Low dimensionality in gene expression data enables the accurate extraction of transcriptional programs from shallow sequencing},
  journal = {Cell Systems},
  year = {2016},
  volume = {2},
  number = {4},
  pages = {239-250},
  doi = {10.1016/j.cels.2016.04.001},
  note = {access: full_text; cited as: H2-01 [Heimberg2016]}
}

@article{theStructureFunctionDiversity2012,
  author = {{The Human Microbiome Project Consortium}},
  title = {Structure, function and diversity of the healthy human microbiome},
  journal = {Nature},
  year = {2012},
  volume = {486},
  number = {7402},
  pages = {207-214},
  doi = {10.1038/nature11234},
  note = {access: full_text (FT per metagenomics angle; critic: H2-01:C-062: not re-checked); cited as: H2-01 [HMP2012]}
}

@article{jiangFunctionalBiogeographyOcean2012,
  author = {Jiang, Xingpeng and Langille, Morgan G. I. and Neches, Russell Y. and Elliot, Marie and Levin, Simon A. and Eisen, Jonathan A. and Weitz, Joshua S. and Dushoff, Jonathan},
  title = {Functional biogeography of ocean microbes revealed through non-negative matrix factorization},
  journal = {PLoS ONE},
  year = {2012},
  volume = {7},
  number = {9},
  pages = {e43866},
  doi = {10.1371/journal.pone.0043866},
  note = {access: full_text; cited as: H2-01 [Jiang2012]}
}

@article{joswigClimaticSoilFactors2021,
  author = {Joswig, Julia S. and Wirth, Christian and Schuman, Meredith C. and Kattge, Jens and Reu, Björn and Wright, Ian J. and Sippel, Sebastian D. and Rüger, Nadja and Richter, Ronny and Schaepman, Michael E. and van Bodegom, Peter M. and Cornelissen, J. H. C. and Díaz, Sandra and Hattingh, Wesley N. and Kramer, Koen and Lens, Frederic and Niinemets, Ülo and Reich, Peter B. and Reichstein, Markus and Römermann, Christine and Schrodt, Franziska and Anand, Madhur and Bahn, Michael and Byun, Chaeho and Campetella, Giandiego and Cerabolini, Bruno E. L. and Craine, Joseph M. and Gonzalez-Melo, Andres and Gutiérrez, Alvaro G. and He, Tianhua and Higuchi, Pedro and Jactel, Hervé and Kraft, Nathan J. B. and Minden, Vanessa and Onipchenko, Vladimir and Peñuelas, Josep and Pillar, Valério D. and Sosinski, Ênio and Soudzilovskaia, Nadejda A. and Weiher, Evan and Mahecha, Miguel D.},
  title = {Climatic and soil factors explain the two-dimensional spectrum of global plant trait variation},
  journal = {Nature Ecology & Evolution},
  year = {2022},
  volume = {6},
  number = {1},
  pages = {36-50},
  doi = {10.1038/s41559-021-01616-8},
  note = {access: full_text; cited as: H2-01 [Joswig2022]; the note adds: online 2021}
}

@article{konnoMachineLearningEnables2023,
  author = {Konno, Naoki and Iwasaki, Wataru},
  title = {Machine learning enables prediction of metabolic system evolution in bacteria},
  journal = {Science Advances},
  year = {2023},
  volume = {9},
  number = {2},
  pages = {eadc9130},
  doi = {10.1126/sciadv.adc9130},
  note = {access: full_text; cited as: H2-01 [KonnoIwasaki2023]}
}

@article{langillePredictiveFunctionalProfiling2013,
  author = {Langille, Morgan G. I. and Zaneveld, Jesse and Caporaso, J. Gregory and McDonald, Daniel and Knights, Dan and Reyes, Joshua A. and Clemente, Jose C. and Burkepile, Deron E. and Vega Thurber, Rebecca L. and Knight, Rob and Beiko, Robert G. and Huttenhower, Curtis},
  title = {Predictive functional profiling of microbial communities using 16S rRNA marker gene sequences},
  journal = {Nature Biotechnology},
  year = {2013},
  volume = {31},
  number = {9},
  pages = {814-821},
  doi = {10.1038/nbt.2676},
  note = {access: full_text; cited as: H2-01 [Langille2013]}
}

@article{laughlinIntrinsicDimensionalityPlant2013,
  author = {Laughlin, Daniel C.},
  title = {The intrinsic dimensionality of plant traits and its relevance to community assembly},
  journal = {Journal of Ecology},
  year = {2014},
  volume = {102},
  number = {1},
  pages = {186-193},
  doi = {10.1111/1365-2745.12187},
  note = {access: abstract_only; cited as: H2-01 [Laughlin2014]; the note adds: online 2013}
}

@article{lenzPrincipalComponentsAnalysis2016,
  author = {Lenz, Michael and Müller, Franz-Josef and Zenke, Martin and Schuppert, Andreas},
  title = {Principal components analysis and the reported low intrinsic dimensionality of gene expression microarray data},
  journal = {Scientific Reports},
  year = {2016},
  volume = {6},
  pages = {25696},
  doi = {10.1038/srep25696},
  note = {access: full_text; cited as: H2-01 [Lenz2016]}
}

@article{loucaDecouplingFunctionTaxonomy2016,
  author = {Louca, Stilianos and Parfrey, Laura Wegener and Doebeli, Michael},
  title = {Decoupling function and taxonomy in the global ocean microbiome},
  journal = {Science},
  year = {2016},
  volume = {353},
  number = {6305},
  pages = {1272-1277},
  doi = {10.1126/science.aaf4507},
  note = {access: abstract_only; cited as: H2-01 [Louca2016a]}
}

@article{loucaHighTaxonomicVariability2016,
  author = {Louca, Stilianos and Jacques, Saulo M. S. and Pires, Aliny P. F. and Leal, Juliana S. and Srivastava, Diane S. and Parfrey, Laura Wegener and Farjalla, Vinicius F. and Doebeli, Michael},
  title = {High taxonomic variability despite stable functional structure across microbial communities},
  journal = {Nature Ecology & Evolution},
  year = {2016},
  volume = {1},
  number = {1},
  pages = {0015},
  doi = {10.1038/s41559-016-0015},
  note = {access: abstract_only; cited as: H2-01 [Louca2016b]}
}

@article{loucaFunctionFunctionalRedundancy2018,
  author = {Louca, Stilianos and Polz, Martin F. and Mazel, Florent and Albright, Michaeline B. N. and Huber, Julie A. and O'Connor, Mary I. and Ackermann, Martin and Hahn, Aria S. and Srivastava, Diane S. and Crowe, Sean A. and Doebeli, Michael and Parfrey, Laura Wegener},
  title = {Function and functional redundancy in microbial systems},
  journal = {Nature Ecology & Evolution},
  year = {2018},
  volume = {2},
  number = {6},
  pages = {936-943},
  doi = {10.1038/s41559-018-0519-1},
  note = {access: abstract_only (AB; review, asserted; cited only for its position that redundancy is general); type: review; not cited: listed in the reference list but cited nowhere in the body; cited as: H2-01 [Louca2018]}
}

@article{lovellProportionalityValidAlternative2015,
  author = {Lovell, David and Pawlowsky-Glahn, Vera and Egozcue, Juan José and Marguerat, Samuel and Bähler, Jürg},
  title = {Proportionality: a valid alternative to correlation for relative data},
  journal = {PLOS Computational Biology},
  year = {2015},
  volume = {11},
  number = {3},
  pages = {e1004075},
  doi = {10.1371/journal.pcbi.1004075},
  note = {access: abstract_only; cited as: H2-01 [Lovell2015]}
}

@article{manorMUSiCCMarkerGenes2015,
  author = {Manor, Ohad and Borenstein, Elhanan},
  title = {MUSiCC: a marker genes based framework for metagenomic normalization and accurate profiling of gene abundances in the microbiome},
  journal = {Genome Biology},
  year = {2015},
  volume = {16},
  pages = {53},
  doi = {10.1186/s13059-015-0610-8},
  note = {access: full_text; cited as: H2-01 [Manor2015]}
}

@article{manorRevisedComputationalMetagenomic2017,
  author = {Manor, Ohad and Borenstein, Elhanan},
  title = {Revised computational metagenomic processing uncovers hidden and biologically meaningful functional variation in the human microbiome},
  journal = {Microbiome},
  year = {2017},
  volume = {5},
  pages = {19},
  doi = {10.1186/s40168-017-0231-4},
  note = {access: full_text (FT, re-checked by reviewer); cited as: H2-01 [Manor2017]; conflict between the note's lists: also listed under Sources not obtained (DOI from memory, not verified; Europe PMC keyword search found no hit)}
}

@article{messierTraitVariationIntegration2016,
  author = {Messier, Julie and McGill, Brian J. and Enquist, Brian J. and Lechowicz, Martin J.},
  title = {Trait variation and integration across scales: is the leaf economic spectrum present at local scales?},
  journal = {Ecography},
  year = {2017},
  volume = {40},
  number = {6},
  pages = {685-697},
  doi = {10.1111/ecog.02006},
  note = {access: abstract_only; cited as: H2-01 [Messier2017]; the note adds: online 2016}
}

@article{mouillotDimensionalityStructureSpecies2021,
  author = {Mouillot, David and Loiseau, Nicolas and Grenié, Matthias and Algar, Adam C. and Allegra, Michele and Cadotte, Marc W. and Casajus, Nicolas and Denelle, Pierre and Guéguen, Maya and Maire, Anthony and Maitner, Brian and McGill, Brian J. and McLean, Matthew and Mouquet, Nicolas and Munoz, François and Thuiller, Wilfried and Villéger, Sébastien and Violle, Cyrille and Auber, Arnaud},
  title = {The dimensionality and structure of species trait spaces},
  journal = {Ecology Letters},
  year = {2021},
  volume = {24},
  number = {9},
  pages = {1988-2009},
  doi = {10.1111/ele.13778},
  note = {access: full_text (FT, Archimer author version; critic: H2-01:C-011, C-062: read by a search agent, not re-opened by the reviewer); cited as: H2-01 [Mouillot2021]}
}

@article{nayfachAverageGenomeSize2015,
  author = {Nayfach, Stephen and Pollard, Katherine S.},
  title = {Average genome size estimation improves comparative metagenomics and sheds light on the functional ecology of the human microbiome},
  journal = {Genome Biology},
  year = {2015},
  volume = {16},
  pages = {51},
  doi = {10.1186/s13059-015-0611-7},
  note = {access: full_text (FT per metagenomics angle; AB per statistics angle; critic: H2-01:C-062: not re-checked); cited as: H2-01 [Nayfach2015]}
}

@article{nelsonGlobalBiogeographyMicrobial2016,
  author = {Nelson, Michaeline B. and Martiny, Adam C. and Martiny, Jennifer B. H.},
  title = {Global biogeography of microbial nitrogen-cycling traits in soil},
  journal = {Proceedings of the National Academy of Sciences of the USA},
  year = {2016},
  volume = {113},
  number = {29},
  pages = {8033-8040},
  doi = {10.1073/pnas.1601070113},
  note = {access: secondary (critic: H2-01:C-059: SECONDARY/unverified; the note said full_text: FT via automated summary of the PMC page; figures not re-verified); cited as: H2-01 [Nelson2016]}
}

@article{peresnetoLinkingTraitVariation2017,
  author = {Peres-Neto, Pedro R. and Dray, Stéphane and ter Braak, Cajo J. F.},
  title = {Linking trait variation to the environment: critical issues with community-weighted mean correlation resolved by the fourth-corner approach},
  journal = {Ecography},
  year = {2017},
  volume = {40},
  number = {7},
  pages = {806-816},
  doi = {10.1111/ecog.02302},
  note = {access: abstract_only; cited as: H2-01 [PeresNeto2017]}
}

@article{piersonSharingSpecificityCoexpression2015,
  author = {Pierson, Emma and the GTEx Consortium and Koller, Daphne and Battle, Alexis and Mostafavi, Sara},
  title = {Sharing and specificity of co-expression networks across 35 human tissues},
  journal = {PLOS Computational Biology},
  year = {2015},
  volume = {11},
  number = {5},
  pages = {e1004220},
  doi = {10.1371/journal.pcbi.1004220},
  note = {access: full_text; cited as: H2-01 [Pierson2015]}
}

@article{pitonLifeHistoryStrategies2023,
  author = {Piton, Gabin and Allison, Steven D. and Bahram, Mohammad and Hildebrand, Falk and Martiny, Jennifer B. H. and Treseder, Kathleen K. and Martiny, Adam C.},
  title = {Life history strategies of soil bacterial communities across global terrestrial biomes},
  journal = {Nature Microbiology},
  year = {2023},
  volume = {8},
  number = {11},
  pages = {2093-2102},
  doi = {10.1038/s41564-023-01465-0},
  note = {access: full_text (FT, eScholarship author version, per trait-ecology angle; critic: H2-01:C-062: not re-checked); cited as: H2-01 [Piton2023]}
}

@article{raesTowardMolecularTraitbased2011,
  author = {Raes, Jeroen and Letunic, Ivica and Yamada, Takuji and Jensen, Lars Juhl and Bork, Peer},
  title = {Toward molecular trait-based ecology through integration of biogeochemical, geographical and metagenomic data},
  journal = {Molecular Systems Biology},
  year = {2011},
  volume = {7},
  pages = {473},
  doi = {10.1038/msb.2011.6},
  note = {access: full_text; cited as: H2-01 [Raes2011]; critic H2-01:C-090: Crossref gives the article number as MSB20116; 473 is the journal's published article number}
}

@article{ramirezflandesRedoxTraitsCharacterize2019,
  author = {Ramírez-Flandes, Salvador and González, Bernardo and Ulloa, Osvaldo},
  title = {Redox traits characterize the organization of global microbial communities},
  journal = {Proceedings of the National Academy of Sciences of the USA},
  year = {2019},
  volume = {116},
  number = {9},
  pages = {3630-3635},
  doi = {10.1073/pnas.1817554116},
  note = {access: full_text; cited as: H2-01 [RamirezFlandes2019]}
}

@article{salazarGeneExpressionChanges2019,
  author = {Salazar, Guillem and Paoli, Lucas and Alberti, Adriana and Huerta-Cepas, Jaime and Ruscheweyh, Hans-Joachim and Cuenca, Miguelangel and Field, Christopher M. and Coelho, Luis Pedro and Cruaud, Corinne and Engelen, Stefan and Gregory, Ann C. and Labadie, Karine and Marec, Claudie and Pelletier, Eric and Royo-Llonch, Marta and Roux, Simon and Sánchez, Pablo and Uehara, Hideya and Zayed, Ahmed A. and Zeller, Georg and Carmichael, Margaux and Dimier, Céline and Ferland, Joannie and Kandels, Stefanie and Picheral, Marc and Pisarev, Sergey and Poulain, Julie and Tara Oceans Coordinators and Acinas, Silvia G. and Babin, Marcel and Bork, Peer and Bowler, Chris and de Vargas, Colomban and Guidi, Lionel and Hingamp, Pascal and Iudicone, Daniele and Karp-Boss, Lee and Karsenti, Eric and Ogata, Hiroyuki and Pesant, Stephane and Speich, Sabrina and Sullivan, Matthew B. and Wincker, Patrick and Sunagawa, Shinichi},
  title = {Gene expression changes and community turnover differentially shape the global ocean metatranscriptome},
  journal = {Cell},
  year = {2019},
  volume = {179},
  number = {5},
  pages = {1068-1083.e21},
  doi = {10.1016/j.cell.2019.10.014},
  note = {access: full_text; cited as: H2-01 [Salazar2019]; incomplete: author (critic H2-01:C-087..089: Crossref lists 71 author entries including coordinator members; the note's list is shorter)}
}

@article{schrodtScpBHPMFScp2015,
  author = {Schrodt, Franziska and Kattge, Jens and Shan, Hanhuai and Fazayeli, Farideh and Joswig, Julia and Banerjee, Arindam and Reichstein, Markus and Bönisch, Gerhard and Díaz, Sandra and Dickie, John and Gillison, Andy and Karpatne, Anuj and Lavorel, Sandra and Leadley, Paul and Wirth, Christian B. and Wright, Ian J. and Wright, S. Joseph and Reich, Peter B.},
  title = {BHPMF: a hierarchical Bayesian approach to gap-filling and trait prediction for macroecology and functional biogeography},
  journal = {Global Ecology and Biogeography},
  year = {2015},
  volume = {24},
  number = {12},
  pages = {1510-1521},
  doi = {10.1111/geb.12335},
  note = {access: abstract_only; cited as: H2-01 [Schrodt2015]}
}

@article{shanAnnotationfreeDiscoveryFunctional2023,
  author = {Shan, Xiaoyu and Goyal, Akshit and Gregor, Rachel and Cordero, Otto X.},
  title = {Annotation-free discovery of functional groups in microbial communities},
  journal = {Nature Ecology & Evolution},
  year = {2023},
  volume = {7},
  number = {5},
  pages = {716-724},
  doi = {10.1038/s41559-023-02021-z},
  note = {access: abstract_only; cited as: H2-01 [Shan2023]}
}

@article{steinobrienDecomposingCellIdentity2019,
  author = {Stein-O'Brien, Genevieve L. and Clark, Brian S. and Sherman, Thomas and Zibetti, Cristina and Hu, Qiwen and Sealfon, Rachel and Liu, Sheng and Qian, Jiang and Colantuoni, Carlo and Blackshaw, Seth and Goff, Loyal A. and Fertig, Elana J.},
  title = {Decomposing cell identity for transfer learning across cellular measurements, platforms, tissues, and species},
  journal = {Cell Systems},
  year = {2019},
  volume = {8},
  number = {5},
  pages = {395-411.e8},
  doi = {10.1016/j.cels.2019.04.004},
  note = {access: full_text; cited as: H2-01 [SteinOBrien2019]}
}

@article{subramanianNextGenerationConnectivity2017,
  author = {Subramanian, Aravind and Narayan, Rajiv and Corsello, Steven M. and Peck, David D. and Natoli, Ted E. and Lu, Xiaodong and Gould, Joshua and Davis, John F. and Tubelli, Andrew A. and Asiedu, Jacob K. and Lahr, David L. and Hirschman, Jodi E. and Liu, Zihan and Donahue, Melanie and Julian, Bina and Khan, Mariya and Wadden, David and Smith, Ian C. and Lam, Daniel and Liberzon, Arthur and Toder, Courtney and Bagul, Mukta and Orzechowski, Marek and Enache, Oana M. and Piccioni, Federica and Johnson, Sarah A. and Lyons, Nicholas J. and Berger, Alice H. and Shamji, Alykhan F. and Brooks, Angela N. and Vrcic, Anita and Flynn, Corey and Rosains, Jacqueline and Takeda, David Y. and Hu, Roger and Davison, Desiree and Lamb, Justin and Ardlie, Kristin and Hogstrom, Larson and Greenside, Peyton and Gray, Nathanael S. and Clemons, Paul A. and Silver, Serena and Wu, Xiaoyun and Zhao, Wen-Ning and Read-Button, Willis and Wu, Xiaohua and Haggarty, Stephen J. and Ronco, Lucienne V. and Boehm, Jesse S. and Schreiber, Stuart L. and Doench, John G. and Bittker, Joshua A. and Root, David E. and Wong, Bang and Golub, Todd R.},
  title = {A next generation connectivity map: L1000 platform and the first 1,000,000 profiles},
  journal = {Cell},
  year = {2017},
  volume = {171},
  number = {6},
  pages = {1437-1452.e17},
  doi = {10.1016/j.cell.2017.10.049},
  note = {access: full_text; cited as: H2-01 [Subramanian2017]}
}

@article{sunInferenceBasedAccuracyMetagenome2020,
  author = {Sun, Shan and Jones, Roshonda B. and Fodor, Anthony A.},
  title = {Inference-based accuracy of metagenome prediction tools varies across sample types and functional categories},
  journal = {Microbiome},
  year = {2020},
  volume = {8},
  pages = {46},
  doi = {10.1186/s40168-020-00815-y},
  note = {access: full_text; cited as: H2-01 [Sun2020]}
}

@article{sunagawaStructureFunctionGlobal2015,
  author = {Sunagawa, Shinichi and Coelho, Luis Pedro and Chaffron, Samuel and Kultima, Jens Roat and Labadie, Karine and Salazar, Guillem and Djahanschiri, Bardya and Zeller, Georg and Mende, Daniel R. and Alberti, Adriana and Cornejo-Castillo, Francisco M. and Costea, Paul I. and Cruaud, Corinne and d'Ovidio, Francesco and Engelen, Stefan and Ferrera, Isabel and Gasol, Josep M. and Guidi, Lionel and Hildebrand, Falk and Kokoszka, Florian and Lepoivre, Cyrille and Lima-Mendez, Gipsi and Poulain, Julie and Poulos, Bonnie T. and Royo-Llonch, Marta and Sarmento, Hugo and Vieira-Silva, Sara and Dimier, Céline and Picheral, Marc and Searson, Sarah and Kandels-Lewis, Stefanie and Tara Oceans coordinators and Bowler, Chris and de Vargas, Colomban and Gorsky, Gabriel and Grimsley, Nigel and Hingamp, Pascal and Iudicone, Daniele and Jaillon, Olivier and Not, Fabrice and Ogata, Hiroyuki and Pesant, Stephane and Speich, Sabrina and Stemmann, Lars and Sullivan, Matthew B. and Weissenbach, Jean and Wincker, Patrick and Karsenti, Eric and Raes, Jeroen and Acinas, Silvia G. and Bork, Peer},
  title = {Structure and function of the global ocean microbiome},
  journal = {Science},
  year = {2015},
  volume = {348},
  number = {6237},
  pages = {1261359},
  doi = {10.1126/science.1261359},
  note = {access: abstract_only; cited as: H2-01 [Sunagawa2015]; incomplete: author (critic H2-01:C-083..086: Crossref lists 60 authors, the note 51, omitting Tara Oceans coordinator names after Bork; last author in the registry Velayoudon, Didier)}
}

@article{tianDecipheringFunctionalRedundancy2020,
  author = {Tian, Liang and Wang, Xu-Wen and Wu, Ang-Kun and Fan, Yuhang and Friedman, Jonathan and Dahlin, Amber and Waldor, Matthew K. and Weinstock, George M. and Weiss, Scott T. and Liu, Yang-Yu},
  title = {Deciphering functional redundancy in the human microbiome},
  journal = {Nature Communications},
  year = {2020},
  volume = {11},
  pages = {6217},
  doi = {10.1038/s41467-020-19940-1},
  note = {access: full_text (FT per statistics angle; critic: H2-01:C-062: not re-checked); cited as: H2-01 [Tian2020]}
}

@article{taroniMultiPLIERTransferLearning2019,
  author = {Taroni, Jaclyn N. and Grayson, Peter C. and Hu, Qiwen and Eddy, Sean and Kretzler, Matthias and Merkel, Peter A. and Greene, Casey S.},
  title = {MultiPLIER: a transfer learning framework for transcriptomics reveals systemic features of rare disease},
  journal = {Cell Systems},
  year = {2019},
  volume = {8},
  number = {5},
  pages = {380-394.e4},
  doi = {10.1016/j.cels.2019.04.003},
  note = {access: full_text; cited as: H2-01 [Taroni2019]}
}

@article{vieirasilvaSpeciesfunctionRelationshipsShape2016,
  author = {Vieira-Silva, Sara and Falony, Gwen and Darzi, Youssef and Lima-Mendez, Gipsi and Garcia Yunta, Roberto and Okuda, Shujiro and Vandeputte, Doris and Valles-Colomer, Mireia and Hildebrand, Falk and Chaffron, Samuel and Raes, Jeroen},
  title = {Species-function relationships shape ecological properties of the human gut microbiome},
  journal = {Nature Microbiology},
  year = {2016},
  volume = {1},
  number = {8},
  pages = {16088},
  doi = {10.1038/nmicrobiol.2016.88},
  note = {access: abstract_only; cited as: H2-01 [VieiraSilva2016]; conflict between the note's lists: also listed under Sources not obtained (from memory, not verified; not reached)}
}

@article{westobyTraitDimensionsBacteria2021,
  author = {Westoby, Mark and Gillings, Michael R. and Madin, Joshua S. and Nielsen, Daniel A. and Paulsen, Ian T. and Tetu, Sasha G.},
  title = {Trait dimensions in bacteria and archaea compared to vascular plants},
  journal = {Ecology Letters},
  year = {2021},
  volume = {24},
  number = {7},
  pages = {1487-1504},
  doi = {10.1111/ele.13742},
  note = {access: abstract_only; type: review; cited as: H2-01 [Westoby2021]}
}

@article{wieczynskiClimateShapesShifts2018,
  author = {Wieczynski, Daniel J. and Boyle, Brad and Buzzard, Vanessa and Duran, Sandra M. and Henderson, Amanda N. and Hulshof, Catherine M. and Kerkhoff, Andrew J. and McCarthy, Megan C. and Michaletz, Sean T. and Swenson, Nathan G. and Asner, Gregory P. and Bentley, Lisa Patrick and Enquist, Brian J. and Savage, Van M.},
  title = {Climate shapes and shifts functional biodiversity in forests worldwide},
  journal = {Proceedings of the National Academy of Sciences of the USA},
  year = {2019},
  volume = {116},
  number = {2},
  pages = {587-592},
  doi = {10.1073/pnas.1813723116},
  note = {access: abstract_only; cited as: H2-01 [Wieczynski2019]}
}

@article{wirbelMetaanalysisFecalMetagenomes2019,
  author = {Wirbel, Jakob and Pyl, Paul Theodor and Kartal, Ece and Zych, Konrad and Kashani, Alireza and Milanese, Alessio and Fleck, Jonas S. and Voigt, Anita Y. and Palleja, Albert and Ponnudurai, Ruby and Sunagawa, Shinichi and Coelho, Luis Pedro and Schrotz-King, Petra and Vogtmann, Emily and Habermann, Nina and Niméus, Emma and Thomas, Andrew M. and Manghi, Paolo and Gandini, Sara and Serrano, Davide and Mizutani, Sayaka and Shiroma, Hirotsugu and Shiba, Satoshi and Shibata, Tatsuhiro and Yachida, Shinichi and Yamada, Takuji and Waldron, Levi and Naccarati, Alessio and Segata, Nicola and Sinha, Rashmi and Ulrich, Cornelia M. and Brenner, Hermann and Arumugam, Manimozhiyan and Bork, Peer and Zeller, Georg},
  title = {Meta-analysis of fecal metagenomes reveals global microbial signatures that are specific for colorectal cancer},
  journal = {Nature Medicine},
  year = {2019},
  volume = {25},
  number = {4},
  pages = {679-689},
  doi = {10.1038/s41591-019-0406-6},
  note = {access: full_text; cited as: H2-01 [Wirbel2019]}
}

@article{wrightModulationLeafEconomic2005,
  author = {Wright, Ian J. and Reich, Peter B. and Cornelissen, Johannes H. C. and Falster, Daniel S. and Groom, Philip K. and Hikosaka, Kouki and Lee, William and Lusk, Christopher H. and Niinemets, Ülo and Oleksyn, Jacek and Osada, Noriyuki and Poorter, Hendrik and Warton, David I. and Westoby, Mark},
  title = {Modulation of leaf economic traits and trait relationships by climate},
  journal = {Global Ecology and Biogeography},
  year = {2005},
  volume = {14},
  number = {5},
  pages = {411-421},
  doi = {10.1111/j.1466-822X.2005.00172.x},
  note = {access: abstract_only; cited as: H2-01 [Wright2005]}
}

@article{wuGlobalRelationshipGenome2025,
  author = {Wu, Xingjie and Peng, Jingjing and Malik, Ashish Anil and Peng, Ziheng and Luo, Yu and Fan, Fenliang and Lu, Yahai and Wei, Gehong and Delgado-Baquerizo, Manuel and Liesack, Werner and Jiao, Shuo},
  title = {A global relationship between genome size and encoded carbon metabolic strategies of soil bacteria},
  journal = {Ecology Letters},
  year = {2025},
  volume = {28},
  number = {1},
  pages = {e70064},
  doi = {10.1111/ele.70064},
  note = {access: abstract_only; cited as: H2-01 [Wu2025]}
}

@article{yeParsimonyApproachBiological2009,
  author = {Ye, Yuzhen and Doak, Thomas G.},
  title = {A parsimony approach to biological pathway reconstruction/inference for genomes and metagenomes},
  journal = {PLoS Computational Biology},
  year = {2009},
  volume = {5},
  number = {8},
  pages = {e1000465},
  doi = {10.1371/journal.pcbi.1000465},
  note = {access: abstract_only; cited as: H2-01 [YeDoak2009]}
}

@article{zelenyWhichResultsStandard2018,
  author = {Zelený, David},
  title = {Which results of the standard test for community-weighted mean approach are too optimistic?},
  journal = {Journal of Vegetation Science},
  year = {2018},
  volume = {29},
  number = {6},
  pages = {953-966},
  doi = {10.1111/jvs.12688},
  note = {access: abstract_only; cited as: H2-01 [Zeleny2018]}
}

@article{douglasPicrust2PredictionMetagenome2020,
  author = {Douglas, G. M. and others},
  title = {PICRUSt2 for prediction of metagenome functions},
  journal = {Nature Biotechnology},
  year = {2020},
  volume = {38},
  pages = {685--688},
  doi = {10.1038/s41587-020-0548-6},
  note = {access: not_obtained (PubMed XML abstract fetch returned no abstract text; full text not attempted (PMC7365738 available)); incomplete: author; cited as: H2-01 Sources not obtained}
}

@article{wemheuerTax4fun2PredictionHabitatSpecific2020,
  author = {Wemheuer, F. and others},
  title = {Tax4Fun2: prediction of habitat-specific functional profiles and functional redundancy based on 16S rRNA gene sequences},
  journal = {Environmental Microbiome},
  year = {2020},
  volume = {15},
  pages = {11},
  doi = {10.1186/s40793-020-00358-7},
  note = {access: not_obtained (found in Europe PMC search listing only; not opened); incomplete: author; listed twice in Sources not obtained; cited as: H2-01 Sources not obtained}
}

@article{lloydpriceStrainsFunctionsDynamics2017,
  author = {Lloyd-Price, J. and others},
  title = {Strains, functions and dynamics in the expanded Human Microbiome Project},
  journal = {Nature},
  year = {2017},
  volume = {550},
  pages = {61--66},
  doi = {10.1038/nature23889},
  note = {access: not_obtained (Crossref metadata only); incomplete: author; not cited; cited as: H2-01 Sources not obtained}
}

@article{leeFunctionalRegimesDefine2025,
  author = {Lee, K. K. and others},
  title = {Functional regimes define soil microbiome response to environmental change},
  journal = {Nature},
  year = {2025},
  volume = {644},
  pages = {1028--1038},
  doi = {10.1038/s41586-025-09264-9},
  note = {access: not_obtained (routes tried: Europe PMC full text read in part (PMC12390847); listed under Sources not obtained, whose heading says nothing beyond a citation was reachable); incomplete: author; not cited; cited as: H2-01 Sources not obtained}
}

@article{jiangNonnegativeMatrixFactorization2011,
  author = {Jiang, X. and Weitz, J. S. and Dushoff, J.},
  title = {A non-negative matrix factorization framework for identifying modular patterns in metagenomic profile data},
  journal = {Journal of Mathematical Biology},
  year = {2012},
  volume = {64},
  pages = {697--711},
  doi = {10.1007/s00285-011-0428-2},
  note = {access: not_obtained (Europe PMC listing only; no OA full text located); cited as: H2-01 Sources not obtained}
}

@article{raguideauInferringAggregatedFunctional2016,
  author = {Raguideau, S. and others},
  title = {Inferring aggregated functional traits from metagenomic data using constrained non-negative matrix factorization},
  journal = {PLoS Computational Biology},
  year = {2016},
  volume = {12},
  number = {12},
  pages = {e1005252},
  doi = {10.1371/journal.pcbi.1005252},
  note = {access: not_obtained (Europe PMC listing only; not opened owing to time); incomplete: author; cited as: H2-01 Sources not obtained}
}

@article{chuckranEdaphicControlsGenome2023,
  author = {Chuckran, P. F. and Flagg, C. and Propster, J. and Rutherford, W. A. and Sieradzki, E. T. and Blazewicz, S. J. and Hungate, B. and Pett-Ridge, J. and Schwartz, E. and Dijkstra, P.},
  title = {Edaphic controls on genome size and GC content of bacteria in soil microbial communities},
  journal = {Soil Biology and Biochemistry},
  year = {2023},
  volume = {178},
  pages = {108935},
  doi = {10.1016/j.soilbio.2022.108935},
  note = {access: not_obtained (Crossref metadata only; OpenAlex no abstract; bioRxiv preprint 10.1101/2021.11.17.469016 identified but not read); not cited; listed twice in Sources not obtained; cited as: H2-01 Sources not obtained}
}

@article{malikDefiningTraitbasedMicrobial2019,
  author = {Malik, A. A. and Martiny, J. B. H. and Brodie, E. L. and Martiny, A. C. and Treseder, K. K. and Allison, S. D.},
  title = {Defining trait-based microbial strategies with consequences for soil carbon cycling under climate change},
  journal = {The ISME Journal},
  year = {2020},
  volume = {14},
  number = {1},
  pages = {1--9},
  doi = {10.1038/s41396-019-0510-0},
  note = {access: not_obtained (Crossref metadata only; not fetched); not cited; listed twice in Sources not obtained; cited as: H2-01 Sources not obtained}
}

@article{madinSynthesisBacterialArchaeal2020,
  author = {Madin, J. S. and others},
  title = {A synthesis of bacterial and archaeal phenotypic trait data},
  journal = {Scientific Data},
  year = {2020},
  volume = {7},
  pages = {170},
  doi = {10.1038/s41597-020-0497-4},
  note = {access: not_obtained (Crossref metadata only; not read); incomplete: author; not cited; listed twice in Sources not obtained; cited as: H2-01 Sources not obtained}
}

@article{maynardGlobalRelationshipsTree2022,
  author = {Maynard and others},
  title = {Global relationships in tree functional traits},
  journal = {Nature Communications},
  year = {2022},
  note = {access: not_obtained (Crossref bibliographic query returned a different paper; DOI not confirmed); incomplete: author, volume, pages, doi (critic H2-01:C-097: no DOI, incomplete); not cited; listed twice in Sources not obtained; cited as: H2-01 Sources not obtained}
}

@article{johnstoneDistributionLargestEigenvalue2001,
  author = {Johnstone, Iain M.},
  title = {On the distribution of the largest eigenvalue in principal components analysis},
  journal = {The Annals of Statistics},
  year = {2001},
  volume = {29},
  number = {2},
  pages = {295--327},
  doi = {10.1214/aos/1009210544},
  note = {access: not_obtained (Crossref metadata only, DOI confirmed; body and abstract not retrieved); listed twice in Sources not obtained; cited as: H2-01 Sources not obtained and stage-2 check}
}

@article{gavishOptimalHardThreshold2014,
  author = {Gavish, Matan and Donoho, David L.},
  title = {The Optimal Hard Threshold for Singular Values is 4/sqrt(3)},
  journal = {IEEE Transactions on Information Theory},
  year = {2014},
  volume = {60},
  number = {8},
  pages = {5040--5053},
  doi = {10.1109/TIT.2014.2323359},
  note = {access: not_obtained (Crossref metadata only, DOI confirmed, no abstract in record; arXiv not queried); listed twice in Sources not obtained; cited as: H2-01 Sources not obtained and stage-2 check}
}

@article{royaltyContributionEvennessFunctional2020,
  author = {Royalty, Taylor M. and Steen, Andrew D.},
  title = {Contribution Evenness: A functional redundancy metric sensitive to trait stability in microbial communities},
  journal = {bioRxiv},
  year = {2020},
  doi = {10.1101/2020.04.22.054593},
  note = {access: not_obtained (Europe PMC abstract retrieved; full text not fetched; judged peripheral (redundancy metric, not covariation)); type: preprint; not cited; cited as: H2-01 Sources not obtained}
}

@article{faustMicrobialCooccurrenceRelationships2012,
  author = {Faust, Karoline and Sathirapongsasuti, J. Fah and Izard, Jacques and Segata, Nicola and Gevers, Dirk and Raes, Jeroen and Huttenhower, Curtis},
  title = {Microbial co-occurrence relationships in the human microbiome},
  journal = {PLoS Computational Biology},
  year = {2012},
  volume = {8},
  number = {7},
  pages = {e1002606},
  doi = {10.1371/journal.pcbi.1002606},
  note = {access: not_obtained (from memory, not verified; not searched after Europe PMC 503 and OpenAlex/Semantic Scholar rate limits); listed twice in Sources not obtained; cited as: H2-01 Sources not obtained}
}

@article{langfelderMyNetworkModule2011,
  author = {Langfelder, P. and others},
  title = {Is my network module preserved and reproducible?},
  journal = {PLoS Computational Biology},
  year = {2011},
  volume = {7},
  pages = {e1001057},
  doi = {10.1371/journal.pcbi.1001057},
  note = {access: not_obtained (metadata only, trait-ecology angle); incomplete: author; not cited; cited as: H2-01 Sources not obtained}
}

@article{bahramStructureFunctionGlobal2018,
  author = {Bahram and others},
  journal = {Nature},
  year = {2018},
  volume = {560},
  number = {7717},
  pages = {233--237},
  doi = {10.1038/s41586-018-0386-6},
  note = {access: abstract_only (AB); incomplete: author, title; not cited: reported by the search angles but not used in the body (peripheral or superseded); cited as: H2-01 Reference list, sources not used}
}

@article{lepsCommunityTraitResponse2011,
  author = {Lepš and others},
  journal = {Ecography},
  year = {2011},
  volume = {34},
  number = {5},
  pages = {856--863},
  doi = {10.1111/j.1600-0587.2010.06904.x},
  note = {access: abstract_only (AB); incomplete: author, title; not cited: reported by the search angles but not used in the body (peripheral or superseded); cited as: H2-01 Reference list, sources not used}
}

@article{nemergutDecreasesAverageBacterial2015,
  author = {Nemergut and others},
  journal = {The ISME Journal},
  year = {2016},
  volume = {10},
  number = {5},
  pages = {1147--1156},
  doi = {10.1038/ismej.2015.191},
  note = {access: abstract_only (AB); incomplete: author, title; not cited: reported by the search angles but not used in the body (peripheral or superseded); cited as: H2-01 Reference list, sources not used}
}

@article{fiererSeeingForestGenes2014,
  author = {Fierer and Barberán and Laughlin},
  journal = {Frontiers in Microbiology},
  year = {2014},
  volume = {5},
  pages = {614},
  doi = {10.3389/fmicb.2014.00614},
  note = {access: abstract_only (AB, asserted); incomplete: author, title; not cited: reported by the search angles but not used in the body (peripheral or superseded); cited as: H2-01 Reference list, sources not used}
}

@article{brbicLandscapeMicrobialPhenotypic2016,
  author = {Brbić and others},
  journal = {Nucleic Acids Research},
  year = {2016},
  volume = {44},
  number = {21},
  pages = {10074--10090},
  doi = {10.1093/nar/gkw964},
  note = {access: abstract_only (AB; volume and pages from the search agent, the Crossref record lists only an article ID); incomplete: author, title; not cited: reported by the search angles but not used in the body; cited as: H2-01 Reference list, sources not used}
}

@article{maGeneticCorrelationNetwork2018,
  author = {Ma and others},
  journal = {The ISME Journal},
  year = {2018},
  doi = {10.1038/s41396-018-0232-8},
  note = {access: not stated (returned by an E-utilities fetch with a mistaken ID; a forest-soil gene correlation network study; not assessed); incomplete: author, title, volume, pages; not cited; cited as: H2-01 Provenance}
}

@article{leeLearningPartsObjects1999,
  author = {Lee, Daniel D. and Seung, H. Sebastian},
  title = {Learning the parts of objects by non-negative matrix factorization},
  journal = {Nature},
  year = {1999},
  volume = {401},
  number = {6755},
  pages = {788--791},
  doi = {10.1038/44565},
  note = {background}
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
  note = {background}
}

@article{aitchisonStatisticalAnalysisCompositional1982,
  author = {Aitchison, J.},
  title = {The Statistical Analysis of Compositional Data},
  journal = {Journal of the Royal Statistical Society Series B: Statistical Methodology},
  year = {1982},
  volume = {44},
  number = {2},
  pages = {139--160},
  doi = {10.1111/j.2517-6161.1982.tb01195.x},
  note = {background}
}
```
