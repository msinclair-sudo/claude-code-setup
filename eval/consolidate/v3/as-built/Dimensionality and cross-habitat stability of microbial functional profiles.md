---
type: knowledge
title: Dimensionality and cross-habitat stability of microbial functional profiles
inputs:
  - "H2-01: PhD/Proposal/Research/Results/Dimensionality of microbial functional profiles, and the cross-habitat stability of functional covariation, function levels and taxonomic composition a literature review.md"
refs: PhD/Proposal/Refs/Refs.bib
built: 2026-10-21
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

### functional-profile: Functional profiles and the bodies of work that supply them
needs: none
- **functional-profile.1** Metagenomics supplies sample-by-function matrices (KEGG orthologues, pathways, modules, Pfams, eggNOG groups) from shotgun data.
  conf: not stated · class: not stated · holds: the review's account of the three bodies of work that bear on the brief · src: none (the reviewer's account of the literature) · trail: H2-01 §1. What · from: H2-01:B-0028, H2-01:B-0029
- **functional-profile.2** Trait ecology supplies community-weighted means (CWMs) and species-by-trait matrices, mostly from plants.
  conf: not stated · class: not stated · holds: the review's account of the three bodies of work that bear on the brief · src: none (the reviewer's account of the literature) · trail: H2-01 §1. What · from: H2-01:B-0028, H2-01:B-0030
- **functional-profile.3** Other fields that profile many correlated features, chiefly transcriptomics, supply most of the explicit held-out tests of learned covariation.
  conf: not stated · class: not stated · holds: the review's account of the three bodies of work that bear on the brief · src: none (the reviewer's account of the literature) · trail: H2-01 §1. What · from: H2-01:B-0028, H2-01:B-0031

### literature-coverage: What the literature covers, and what it does not
needs: functional-profile
- **literature-coverage.1** The three bodies of work have asked different questions: metagenomics has mostly compared levels of functions with taxonomic composition; trait ecology has asked about the dimensionality and covariation of traits, and sometimes how covariation shifts along gradients; transcriptomics has asked whether covariation learned in one tissue or study reproduces another.
  conf: not stated · class: not stated · holds: metagenomics, trait ecology (mostly plants) and transcriptomics as the review found them · src: none (the reviewer's account of the literature) · trail: H2-01 §1. What · from: H2-01:B-0032, H2-01:B-0033, H2-01:B-0034, H2-01:B-0035
- **literature-coverage.2** The core cases of the brief are thinly covered: most of the evidence is either direct evidence on a neighbouring quantity or evidence from another field, and each is labelled as such.
  conf: not stated · class: not stated · holds: the core microbial cases (withheld habitat, cross-habitat covariation stability, taxonomy held fixed) are kept as not found; the critic: the review labels most indirect evidence · src: none (the reviewer's account of the literature) · trail: H2-01 §1. What, §critic · from: H2-01:B-0036, H2-01:B-0040, H2-01:B-0041, H2-01:C-045
- **literature-coverage.3** The brief's third direction asks for three pairwise comparisons (covariation, levels, composition) in two cases (taxonomy turns over, taxonomy does not), and the evidence is very uneven across the six cells.
  conf: not stated · class: not stated · holds: microbial and other-field evidence on stability across habitats · src: none (the reviewer's account of the literature) · trail: H2-01 §4. D3 · from: H2-01:B-0129, H2-01:B-0130

### dimension-estimate: Dimension estimates for sample-by-function matrices
needs: functional-profile
- **dimension-estimate.bg1** Principal component analysis (PCA) reduces the dimensionality of a dataset by creating new uncorrelated variables, the principal components, that successively maximise variance.
  kind: background · ref: jolliffePrincipalComponentAnalysis2016 · check: DOI 10.1098/rsta.2015.0202 resolves on Crossref; stated in the abstract (Crossref record)
- **dimension-estimate.1** Few direct dimension estimates exist for microbial sample-by-function matrices, and they use incompatible methods (NMF rank 5 for 8,214 Pfams in 45 ocean samples, two co-inertia axes carrying about half the variation in 128 soils, three KO clusters across 6,539 metagenomes).
  conf: not stated · class: search (note: "Only a handful of studies report something that can be read as a dimension estimate") · holds: sample-level microbial functional profiles; the critic: the D1 answer is supported as written, with two corrections (see shared-mean.1, genome-dimension.1, expression-dimension.1) · src: jiangFunctionalBiogeographyOcean2012 (FT), pitonLifeHistoryStrategies2023 (FT), flinkstromMetagenomicClusteringLinks2024 (FT) · trail: H2-01 §answers, §2.1, §6 · from: H2-01:A-001, H2-01:A-104, H2-01:A-013, H2-01:B-0046, H2-01:C-001 · rating: "Weak for the microbial sample-level question"
- **dimension-estimate.2** Each direct microbial estimate (Jiang2012, Piton2023, Flinkstrom2024) is a single study, and all are fitted and scored on the same samples.
  conf: single (critic: H2-01:C-009) · class: not stated · holds: microbial sample-by-function matrices · src: jiangFunctionalBiogeographyOcean2012 (FT), pitonLifeHistoryStrategies2023 (FT), flinkstromMetagenomicClusteringLinks2024 (FT) · trail: H2-01 §critic, §answers · from: H2-01:A-014, H2-01:C-009
- **dimension-estimate.3** No held-out (cross-validated) rank estimate for functional profiles was found.
  conf: not stated · class: search (note: "No held-out (cross-validated) rank estimate for functional profiles") · holds: the routes in the search record · src: none (a search result) · trail: H2-01 §answers · from: H2-01:A-020
- **dimension-estimate.4** Dimension has not been compared by habitat; no search route targeted habitat-stratified decompositions such as per-biome NMF or PCA in multi-biome metagenome atlases.
  conf: not stated · class: search (note: "Dimension by habitat not compared") · holds: microbial functional profiles; the routes in the search record · src: none (a search result) · trail: H2-01 §answers, §critic · from: H2-01:A-021, H2-01:C-115

### shared-mean: Similarity of per-sample functional profiles (the "shared mean")
needs: functional-profile, dimension-estimate
- **shared-mean.1** In the datasets examined, per-sample functional profiles are highly similar to one another.
  conf: not stated · class: not stated · holds: human-associated and a few soil datasets; rests on a per-sample prediction-accuracy metric that barely changes under permutation (Sun2020) and on HMP2012's report that pathway levels vary less than taxa; neither is a decomposition that measures how much of a sample-by-function matrix is a mean profile (the critic) · src: sunInferenceBasedAccuracyMetagenome2020 (FT; measured), theStructureFunctionDiversity2012 (FT; measured) · trail: H2-01 §critic, §2.2 · from: H2-01:C-002, H2-01:C-003, H2-01:C-004, H2-01:C-005, H2-01:C-006, H2-01:B-0060
- **shared-mean.2** Per-sample Spearman correlations between predicted and measured KEGG gene profiles (0.53 to 0.87) barely changed when each gene's abundance was permuted across samples (soil example: 0.85 unpermuted, 0.84 permuted); the per-sample metric is almost insensitive to permuting genes across samples.
  conf: not stated · class: meas (marker) · holds: metagenome prediction tools scored per sample, across human, non-human and soil datasets · src: sunInferenceBasedAccuracyMetagenome2020 (FT; measured) · trail: H2-01 §2.2, §3.3 · from: H2-01:I-0006, H2-01:B-0111, H2-01:C-003
- **shared-mean.3** Sun2020's authors conclude that functional profiles vary little between samples relative to their mean.
  conf: not stated · class: not stated · holds: the datasets of Sun2020 · src: sunInferenceBasedAccuracyMetagenome2020 (FT) · trail: H2-01 §2.2 · from: H2-01:B-0061
- **shared-mean.4** A reference network of 796 human-associated genomes by 7,105 KOs has a nested structure, with many KOs carried by most genomes, which makes community functional profiles conserved even when taxa vary.
  conf: single (marker) · class: deriv/model (marker) · holds: human-associated genomes; offered as a mechanistic account of the similarity of profiles and as a reason for stable function levels · src: tianDecipheringFunctionalRedundancy2020 (FT per statistics angle, not re-checked by the reviewer, critic: H2-01:C-064; derived/modelled; SINGLE SOURCE) · trail: H2-01 §2.2, §answers · from: H2-01:B-0062, H2-01:I-0008, H2-01:A-056, H2-01:C-064
- **shared-mean.5** Whether a dimension estimate is taken before or after centring on the mean profile will change it.
  conf: not stated · class: not stated · holds: dimension estimates of functional profiles · src: none (the reviewer's statement) · trail: H2-01 §2.2 · from: H2-01:B-0063
- **shared-mean.6** No microbial study was found that reports a dimension estimate both before and after centring on the mean profile.
  conf: not stated · class: search (note: "No microbial study found reports both") · holds: the routes in the search record · src: none (a search result) · trail: H2-01 §2.2 · from: H2-01:B-0063, H2-01:B-0064

### direct-dimension: Direct estimates on microbial sample-by-function matrices
needs: dimension-estimate, shared-mean, genome-size
group: leading-axes
- **direct-dimension.1** Across 45 Global Ocean Sampling sites and 8,214 Pfam relative abundances, NMF was judged stable at rank 5 by a concordance criterion; no variance-explained figure was reported.
  conf: single (critic: H2-01:C-009) · class: not stated · holds: 45 ocean sites, Pfam relative abundances; fitted and scored on the same samples · src: jiangFunctionalBiogeographyOcean2012 (FT) · trail: H2-01 §2.1 · from: H2-01:B-0048, H2-01:B-0049, H2-01:A-002, H2-01:C-009
- **direct-dimension.2** The five NMF components had "strikingly high" similarity to each other, and a large ubiquitous, mostly primary-metabolism Pfam block loaded on all of them.
  conf: single (critic: H2-01:C-009) · class: not stated · holds: 45 Global Ocean Sampling sites, 8,214 Pfams · src: jiangFunctionalBiogeographyOcean2012 (FT) · trail: H2-01 §2.1 · from: H2-01:B-0050, H2-01:A-002, H2-01:C-009
- **direct-dimension.3** Two of the five NMF components could not be interpreted.
  conf: single (marker) · class: meas (marker) · holds: 45 ocean sites, 8,214 Pfams; fitted and scored on the same samples · src: jiangFunctionalBiogeographyOcean2012 (FT; measured; fitted and scored on the same samples; SINGLE SOURCE) · trail: H2-01 §2.1 · from: H2-01:I-0002
- **direct-dimension.4** Rank 5 is low relative to 8,214 features, but with n = 45 the rank cannot exceed 45, and much of the fit is a shared mean-like profile.
  conf: not stated · class: reading (note: "Reviewer's reading") · holds: Jiang2012's NMF on 45 samples · src: none (the reviewer's reading of Jiang2012) · trail: H2-01 §2.1 · from: H2-01:B-0051
- **direct-dimension.5** In 128 soil metagenomes, the first four multiple co-inertia axes captured 29%, 21%, 16% and 10% of variation; this is the only variance-explained figure for a microbial functional profile.
  conf: single (critic: H2-01:C-009) · class: not stated · holds: global topsoil set; KEGG, eggNOG, SEED, CAZy and genomic-trait tables, relative abundance normalised by annotated bacterial reads, log(x+1), z-scored · src: pitonLifeHistoryStrategies2023 (FT per trait-ecology angle, not re-checked by the reviewer, critic: H2-01:C-064) · trail: H2-01 §2.1, §answers · from: H2-01:B-0052, H2-01:A-003, H2-01:A-026, H2-01:C-009, H2-01:C-064
- **direct-dimension.6** The first Piton co-inertia axis tracked average genome size (R² = 0.64).
  conf: single (marker) · class: meas (marker) · holds: 128 soil metagenomes · src: pitonLifeHistoryStrategies2023 (FT; measured; SINGLE SOURCE) · trail: H2-01 §2.1 · from: H2-01:I-0003
- **direct-dimension.7** Piton2023's authors call the structure a two-dimension "triangle" of life-history strategies.
  conf: not stated · class: not stated · holds: 128 soil metagenomes · src: pitonLifeHistoryStrategies2023 (FT) · trail: H2-01 §2.1 · from: H2-01:B-0053
- **direct-dimension.8** Piton2023's authors warn that community-aggregated covariation does not show within-organism trade-offs.
  conf: not stated · class: not stated · holds: community-aggregated functional tables of 128 soils · src: pitonLifeHistoryStrategies2023 (FT) · trail: H2-01 §2.1 · from: H2-01:B-0054
- **direct-dimension.9** In Piton2023 only 5 to 15% of reads were annotated, and annotation coverage fell as genome size rose.
  conf: not stated · class: not stated · holds: 128 soil metagenomes · src: pitonLifeHistoryStrategies2023 (FT) · trail: H2-01 §2.1 · from: H2-01:B-0054
- **direct-dimension.10** Two co-inertia axes carry about half the variation in Piton2023; the other half is not low-dimensional on this evidence.
  conf: not stated · class: reading (note: "Reviewer's reading") · holds: 128 soil metagenomes · src: none (the reviewer's reading of Piton2023) · trail: H2-01 §2.1 · from: H2-01:B-0055
- **direct-dimension.11** Across 6,539 IMG/M assembled metagenomes, bootstrapped k-means on KO profiles found three clusters (terrestrial, aquatic, anaerobic), strongly associated with assembly GC content.
  conf: single (marker) · class: meas (marker) · holds: KO abundances, KOs in under 10% of samples removed, CLR · src: flinkstromMetagenomicClusteringLinks2024 (FT; measured; SINGLE SOURCE) · trail: H2-01 §2.1 · from: H2-01:I-0004, H2-01:A-004
- **direct-dimension.12** Cluster number is not an intrinsic-dimension estimate; the three KO clusters are reported only as a nearest precedent.
  conf: not stated · class: not stated · holds: Flinkstrom2024 · src: none (the reviewer's statement on Flinkstrom2024) · trail: H2-01 §2.1 · from: H2-01:B-0056, H2-01:A-004
- **direct-dimension.13** Across 25 Global Ocean Sampling metagenomes, the first canonical correlation between KEGG module composition and environment was 0.944.
  conf: not stated · class: meas (marker) · holds: 25 GOS metagenomes, KEGG modules · src: raesTowardMolecularTraitbased2011 (FT; measured) · trail: H2-01 §2.1 · from: H2-01:I-0005
- **direct-dimension.14** With n = 25 and many modules, a high first canonical correlation on the same samples is expected, and it does not measure dimension.
  conf: not stated · class: not stated · holds: Raes2011's CCA · src: none (the reviewer's statement on Raes2011) · trail: H2-01 §2.1 · from: H2-01:B-0057, H2-01:B-0058
- **direct-dimension.15** Gianoulis2009 similarly define "metabolic footprints" by CCA on Global Ocean Sampling data.
  conf: not stated · class: not stated · holds: GOS metagenomes · src: gianoulisQuantifyingEnvironmentalAdaptation2009 (AB) · trail: H2-01 §2.1 · from: H2-01:B-0059
- **direct-dimension.16** Read literally, the direct estimates are low relative to the number of functions.
  conf: not stated · class: not stated · holds: Jiang2012, Piton2023, Flinkstrom2024 · src: none (the reviewer's synthesis) · trail: H2-01 §answers · from: H2-01:A-005
- **direct-dimension.17** In each direct estimate, n is small or only about half the variance is in the leading axes.
  conf: not stated · class: not stated · holds: Jiang2012 (n = 45), Piton2023 (about half the variance in two axes) · src: none (the reviewer's synthesis) · trail: H2-01 §answers · from: H2-01:A-006

### genome-size: Genome size and normalisation
needs: functional-profile, direct-dimension
group: leading-axes
- **genome-size.1** Relative (sum-to-one) normalisation introduces a sample-level factor shared by all genes.
  conf: not stated · class: not stated · holds: relatively normalised functional profiles · src: none (the note cites no source for this sentence) · trail: H2-01 §2.3 · from: H2-01:B-0067
- **genome-size.2** The relative abundance of universal single-copy genes correlated with average genome size at R = −0.78 across HMP body sites and −0.82 in stool.
  conf: not stated · class: meas (marker) · holds: HMP body sites and stool · src: manorMUSiCCMarkerGenes2015 (FT; measured) · trail: H2-01 §2.3 · from: H2-01:I-0009
- **genome-size.3** Species abundance explained 74% of average-genome-size variation across HMP samples.
  conf: not stated · class: meas (marker) · holds: HMP samples · src: nayfachAverageGenomeSize2015 (FT per metagenomics angle, AB per statistics angle, not re-checked by the reviewer, critic: H2-01:C-064; measured) · trail: H2-01 §2.3 · from: H2-01:I-0010, H2-01:C-064
- **genome-size.4** Genome-size variation makes genes at equal per-cell copy number look variable and hides real per-cell variation, so stable genes can look variable and variable genes stable.
  conf: not stated · class: meas (marker) · holds: HMP samples · src: nayfachAverageGenomeSize2015 (FT per metagenomics angle, AB per statistics angle; measured) · trail: H2-01 §2.3, §answers · from: H2-01:I-0010, H2-01:A-058
- **genome-size.5** In soils, genome size tracked the ratio of polysaccharide-decomposition to biomass-synthesis genes across 2,650 genomes and a continental survey.
  conf: not stated · class: not stated · holds: soil bacteria, 2,650 genomes and a continental survey · src: wuGlobalRelationshipGenome2025 (AB) · trail: H2-01 §2.3 · from: H2-01:B-0068
- **genome-size.6** The first Piton axis (R² = 0.64 with genome size) is consistent with genome-size and normalisation effects.
  conf: not stated · class: not stated · holds: 128 soil metagenomes · src: pitonLifeHistoryStrategies2023 · trail: H2-01 §2.3 · from: H2-01:B-0069, H2-01:A-006
- **genome-size.7** At least one leading axis of many functional-profile decompositions may be a genome-size or normalisation axis; this is an inference, not a measured decomposition.
  conf: not stated · class: reading (note: "This is an inference, not a measured decomposition") · holds: functional-profile decompositions generally · src: none (the reviewer's inference) · trail: H2-01 §2.3 · from: H2-01:B-0070, H2-01:B-0071, H2-01:A-006

### gene-set-aggregation: Aggregation into gene sets that share members
needs: functional-profile
- **gene-set-aggregation.1** In HMP gut samples, single-copy-gene normalisation raised pathway coefficients of variation relative to relative normalisation.
  conf: single (note: "SINGLE SOURCE for this set of quantities") · class: not stated · holds: HMP gut samples, KEGG pathways · src: manorRevisedComputationalMetagenomic2017 (FT, re-checked by the reviewer) · trail: H2-01 §2.3 · from: H2-01:B-0072, H2-01:B-0073, H2-01:B-0077, H2-01:A-008
- **gene-set-aggregation.2** Uniform mapping of KOs shared among pathways gave less variable pathway profiles than a sample-specific mapping.
  conf: single (note: "SINGLE SOURCE for this set of quantities") · class: not stated · holds: HMP gut samples, KEGG pathways · src: manorRevisedComputationalMetagenomic2017 (FT, re-checked by the reviewer) · trail: H2-01 §2.3 · from: H2-01:B-0074, H2-01:B-0077, H2-01:A-008
- **gene-set-aggregation.3** On average 9.5% of gene-family pairs within the same KEGG pathway were negatively correlated (R < −0.3).
  conf: single (note: "SINGLE SOURCE for this set of quantities") · class: not stated · holds: HMP gut samples · src: manorRevisedComputationalMetagenomic2017 (FT, re-checked by the reviewer) · trail: H2-01 §2.3 · from: H2-01:B-0075, H2-01:B-0077
- **gene-set-aggregation.4** Aggregating KOs into KEGG pathways lowered variability relative to aggregates built from genome co-occurrence.
  conf: single (note: "SINGLE SOURCE for this set of quantities") · class: not stated · holds: HMP gut samples · src: manorRevisedComputationalMetagenomic2017 (FT, re-checked by the reviewer) · trail: H2-01 §2.3 · from: H2-01:B-0076, H2-01:B-0077, H2-01:A-008
- **gene-set-aggregation.5** Manor and Borenstein (2017) conclude that reported functional uniformity is partly a processing artefact.
  conf: single (note: "SINGLE SOURCE for this set of quantities") · class: not stated · holds: HMP gut samples · src: manorRevisedComputationalMetagenomic2017 (FT, re-checked by the reviewer) · trail: H2-01 §2.3 · from: H2-01:B-0077
- **gene-set-aggregation.6** Manor2017 is the only measurement found of shared-member and aggregation effects on across-sample variability.
  conf: single (note: "SINGLE SOURCE for this set of quantities") · class: search (note: "removes the only measurement of shared-member and aggregation effects on across-sample variability") · holds: microbial functional profiles; removing it would weaken the processing caution substantially · src: manorRevisedComputationalMetagenomic2017 (FT, re-checked by the reviewer) · trail: H2-01 §answers · from: H2-01:A-028, H2-01:A-067, H2-01:B-0077
- **gene-set-aggregation.7** Naive mapping of a gene family to every pathway containing it inflates pathway counts.
  conf: not stated · class: not stated · holds: pathway reconstruction for genomes and metagenomes · src: yeParsimonyApproachBiological2009 (AB) · trail: H2-01 §2.3 · from: H2-01:B-0078, H2-01:A-008
- **gene-set-aggregation.8** In transcriptomics, pathways sharing genes shift each other's significance ("crosstalk").
  conf: not stated · class: not stated · holds: pathway analysis of expression data (other field) · src: donatoAnalysisCorrectionCrosstalk2013 (AB; other field) · trail: H2-01 §2.3 · from: H2-01:B-0079
- **gene-set-aggregation.9** None of the processing studies measures a covariance matrix between overlapping gene sets.
  conf: not stated · class: not stated · holds: Manor2017, YeDoak2009, Donato2013 · src: none (the reviewer's statement) · trail: H2-01 §2.3 · from: H2-01:B-0080
- **gene-set-aggregation.10** That shared members inflate pathway-pathway covariance, and so lower apparent dimension, is the reviewer's inference.
  conf: not stated · class: reading (note: "is the reviewer's inference") · holds: pathway profiles built from shared KOs · src: none (the reviewer's inference) · trail: H2-01 §2.3 · from: H2-01:B-0081

### compositional-closure: Compositional closure
needs: functional-profile
- **compositional-closure.bg1** Microbiome datasets from high-throughput sequencing (16S rRNA gene amplicons, metagenomes, metatranscriptomes) are compositional, because the instrument imposes an arbitrary total.
  kind: background · ref: gloorMicrobiomeDatasetsCompositional2017 · check: DOI 10.3389/fmicb.2017.02224 resolves on Crossref; stated in the abstract (Europe PMC record)
- **compositional-closure.1** Correlation is not a valid association measure for relative data; proportionality is offered instead.
  conf: not stated · class: not stated · holds: relative data in general (other field) · src: lovellProportionalityValidAlternative2015 (AB; other field) · trail: H2-01 §2.3 · from: H2-01:B-0082, H2-01:A-008

### cwm: Community-weighted aggregates
needs: functional-profile
- **cwm.bg1** Community-aggregated traits weight the trait values of species according to their relative abundance in the community.
  kind: background · ref: garnierPlantFunctionalMarkers2004 · check: DOI 10.1890/03-0799 resolves on Crossref; stated in the abstract (OpenAlex record)
- **cwm.1** In trait ecology, CWMs all share the same abundance weights, so the composition matrix itself induces structure among CWMs.
  conf: not stated · class: not stated · holds: community-weighted means of traits · src: none (the note cites no source for this sentence) · trail: H2-01 §2.3 · from: H2-01:B-0083
- **cwm.2** CWM correlation tests have inflated error rates when only environment or only traits structure species distributions.
  conf: not stated · class: model (marker) · holds: CWM-environment correlation tests · src: peresnetoLinkingTraitVariation2017 (AB; modelled) · trail: H2-01 §2.3 · from: H2-01:I-0011
- **cwm.3** The inflation of CWM test error rates falls with compositional beta diversity and rises with sample size.
  conf: not stated · class: model (marker) · holds: CWM-environment correlation tests · src: zelenyWhichResultsStandard2018 (AB; modelled) · trail: H2-01 §2.3 · from: H2-01:I-0012
- **cwm.4** By analogy, community-aggregated functional profiles share weights in the same way as CWMs.
  conf: not stated · class: reading (note: "By analogy (reviewer's reading)") · holds: community-aggregated microbial functional profiles · src: none (the reviewer's reading) · trail: H2-01 §2.3 · from: H2-01:B-0084
- **cwm.5** Abundance-weighted and unweighted trait moments disagreed in sign, significance or both for 71% of forest trait-climate results.
  conf: not stated · class: not stated · holds: forest plots worldwide · src: wieczynskiClimateShapesShifts2018 (AB) · trail: H2-01 §4.4 · from: H2-01:B-0163
- **cwm.6** CWM accuracy depended on trait coverage of the community.
  conf: not stated · class: not stated · holds: plant community-level trait-environment relationships · src: borgySensitivityCommunitylevelTraitenvironment2017 (AB) · trail: H2-01 §4.4 · from: H2-01:B-0163

### processing-dimension: How processing choices move a dimension estimate
needs: dimension-estimate, genome-size, gene-set-aggregation, compositional-closure, cwm
- **processing-dimension.1** No microbial study was found that re-estimated the dimension of functional profiles under different normalisations, sparsity filters, presence/absence against abundance, overlapping against non-overlapping gene sets, or sample sizes, and none uses a formal rank-selection rule (parallel analysis, cross-validated PCA or NMF, a random-matrix threshold) with stated n and p while testing processing.
  conf: not stated · class: search (note: "No microbial study re-estimated dimension under different normalisation, sparsity filters, presence/absence against abundance, or sample size") · holds: three search angles via Europe PMC REST, NCBI E-utilities, Crossref, Unpaywall, OpenAlex, Semantic Scholar, WebFetch of PMC pages and repository PDFs; WebSearch and Scholar Gateway unavailable · src: none (a search result) · trail: H2-01 §answers, §2.3, §Provenance · from: H2-01:A-007, H2-01:A-019, H2-01:A-105, H2-01:B-0047, H2-01:B-0065, H2-01:B-0010, H2-01:B-0011, H2-01:B-0018, H2-01:C-010
- **processing-dimension.2** Normalisation, genome size, pathway aggregation and compositional closure measurably change across-sample variance and covariance, which a dimension estimate would inherit; the evidence is indirect for dimension.
  conf: not stated · class: meas (note: "What exists is measured evidence that these choices change across-sample variance and covariance") · holds: microbial functional profiles (HMP), and relative data in general · src: manorRevisedComputationalMetagenomic2017 (FT, re-checked by the reviewer), manorMUSiCCMarkerGenes2015 (FT), nayfachAverageGenomeSize2015 (FT per metagenomics angle), yeParsimonyApproachBiological2009 (AB), lovellProportionalityValidAlternative2015 (AB) · trail: H2-01 §2.3, §answers, §6 · from: H2-01:B-0066, H2-01:A-008, H2-01:A-015, H2-01:A-106
- **processing-dimension.3** That these processing shifts lower apparent dimension is the reviewer's inference.
  conf: not stated · class: reading (note: "That these shifts lower apparent dimension is the reviewer's inference") · holds: microbial functional profiles; the critic: correctly labelled in Section 2.3 and the D1 answer, but the Section 6 summary drops the label · src: none (the reviewer's inference) · trail: H2-01 §answers, §critic · from: H2-01:A-009, H2-01:C-133

### genome-dimension: Dimensionality across bacterial genomes
needs: dimension-estimate
- **genome-dimension.1** Diffusion maps on presence/absence of 7,769 substrate-product traits across 2,621 genera found no single low-dimensional space but crossing low-dimensional manifolds with "dozens or possibly hundreds of meaningful coordinates".
  conf: single (marker) · class: model (marker) · holds: bacterial genera as rows, presence/absence of metabolic traits; one modelled study, not a property of genomes in general (the critic) · src: fahimipourMappingBacterialMetabolic2020a (FT; modelled; SINGLE SOURCE) · trail: H2-01 §2.4, §critic · from: H2-01:I-0013, H2-01:C-007, H2-01:C-008, H2-01:C-072
- **genome-dimension.2** A review names three main axes of quantitative bacterial traits (growth rate with rRNA copy number, genome size with signal transduction, cell size) and notes that quantitative traits vary widely within substrate-use pathways.
  conf: not stated · class: assert (marker) · holds: quantitative traits of bacteria and archaea · src: westobyTraitDimensionsBacteria2021 (AB; asserted) · trail: H2-01 §2.4 · from: H2-01:I-0014
- **genome-dimension.3** Fahimipour2020 and Westoby2021 are not in conflict, because they describe different trait sets; together they bound any claim that "microbial function" has one dimensionality.
  conf: not stated · class: not stated · holds: genome-level trait sets · src: none (the reviewer's statement) · trail: H2-01 §2.4 · from: H2-01:B-0086, H2-01:B-0087

### trait-dimension: Dimensionality of species trait databases
needs: dimension-estimate, cwm
- **trait-dimension.1** Across 30 species-by-trait datasets, the median dimension was 4 by an elbow rule (range 2 to 8) and 6 by an AUC threshold of 0.7 (range 2 to 17), and the two estimates were only weakly correlated.
  conf: not stated · class: meas (marker) · holds: species-level trait matrices · src: mouillotDimensionalityStructureSpecies2021 (FT, read by a search agent and not re-opened by the reviewer, critic: H2-01:C-011; measured) · trail: H2-01 §2.4 · from: H2-01:I-0015, H2-01:A-010, H2-01:C-011
- **trait-dimension.2** Threshold dimensionality rose with the log number of traits and fell with mean trait correlation (GLM R² = 0.61).
  conf: not stated · class: not stated · holds: 30 species-by-trait datasets · src: mouillotDimensionalityStructureSpecies2021 (FT) · trail: H2-01 §2.4 · from: H2-01:B-0088, H2-01:A-010
- **trait-dimension.3** In simulations, species number mattered only below about 100 to 200 species, and dropping half the traits lost much quality.
  conf: not stated · class: model (note: "In simulations") · holds: simulated species-by-trait matrices · src: mouillotDimensionalityStructureSpecies2021 (FT) · trail: H2-01 §2.4 · from: H2-01:B-0089, H2-01:A-010
- **trait-dimension.4** Mouillot2021 is the only source found that measures how a dimension estimate depends on the number of features, feature correlation and sample count, and it concerns species-level traits, not sample-level profiles.
  conf: single (note: "This is the only source found that measures how a dimension estimate depends on the number of features") · class: search (note: "This is the only source found") · holds: species-by-trait matrices; the empirical dependence of rank on p/n rests on it alone; full text per angle, not re-checked by the reviewer (the critic) · src: mouillotDimensionalityStructureSpecies2021 (FT) · trail: H2-01 §2.4, §answers, §critic · from: H2-01:B-0090, H2-01:B-0091, H2-01:A-016, H2-01:A-027, H2-01:A-107, H2-01:C-011, H2-01:C-064, H2-01:C-109
- **trait-dimension.5** Plant traits have at most six dimensions in the largest of three datasets.
  conf: not stated · class: not stated · holds: three plant trait datasets · src: laughlinIntrinsicDimensionalityPlant2013 (AB) · trail: H2-01 §2.4 · from: H2-01:B-0092
- **trait-dimension.6** Two components explain 74% of six key plant traits across 2,214 species.
  conf: not stated · class: not stated · holds: six plant traits, 2,214 species · src: bruelheideGlobalTraitenvironmentRelationships2018 (SEC, via Bruelheide2018) · trail: H2-01 §2.4 · from: H2-01:B-0093
- **trait-dimension.7** With 17 gap-filled traits across more than 20,000 plant species, PC1 explained 33%, PC2 15% and PC3 9.4%.
  conf: not stated · class: not stated · holds: gap-filled (BHPMF) plant trait matrix · src: joswigClimaticSoilFactors2021 (FT) · trail: H2-01 §2.4 · from: H2-01:B-0093
- **trait-dimension.8** The BHPMF gap-filling imputes from trait-trait correlations.
  conf: not stated · class: not stated · holds: plant trait gap-filling · src: schrodtScpBHPMFScp2015 (AB) · trail: H2-01 §2.4 · from: H2-01:B-0094
- **trait-dimension.9** Covariation in imputed trait matrices is partly built in.
  conf: not stated · class: reading (note: "so covariation in imputed matrices is partly built in (reviewer's reading)") · holds: gap-filled plant trait matrices · src: none (the reviewer's reading) · trail: H2-01 §2.4 · from: H2-01:B-0094

### expression-dimension: Dimensionality of gene expression data
needs: dimension-estimate
- **expression-dimension.1** Across 352 microarray datasets, the first principal value averaged about twice the second, the first five components explained most variance, and per-gene shuffling removed this.
  conf: single (critic: H2-01:C-074) · class: meas (marker) · holds: microarray gene expression datasets, within dataset (other field) · src: heimbergLowDimensionalityGene2016 (FT; measured; SINGLE SOURCE; critic: H2-01:C-074 was "FT; measured") · trail: H2-01 §2.4, §critic · from: H2-01:I-0016, H2-01:C-007, H2-01:C-008, H2-01:C-073, H2-01:C-074, H2-01:C-075, H2-01:C-121, H2-01:C-123
- **expression-dimension.2** Heimberg2016's authors call low dimensionality fundamental.
  conf: not stated · class: not stated · holds: gene expression data · src: heimbergLowDimensionalityGene2016 (FT) · trail: H2-01 §2.4 · from: H2-01:B-0095
- **expression-dimension.3** In large heterogeneous compendia (5,372 and 7,100 samples), the first three PCs explained about 36% of variance, components beyond the third were unstable between datasets, and the residual space carried most tissue-specific signal.
  conf: single (critic: H2-01:C-122) · class: not stated · holds: heterogeneous expression compendia (other field); the critic's spot check confirmed n = 5,372 and 7,100 and that the fourth component was unstable · src: lenzPrincipalComponentsAnalysis2016 (FT) · trail: H2-01 §2.4, §critic · from: H2-01:B-0096, H2-01:C-048, H2-01:C-122
- **expression-dimension.4** PCA of expression compendia depended on the fraction of samples carrying a signal.
  conf: single (marker) · class: meas (marker) · holds: heterogeneous expression compendia · src: lenzPrincipalComponentsAnalysis2016 (FT; measured; SINGLE SOURCE) · trail: H2-01 §2.4 · from: H2-01:I-0017
- **expression-dimension.5** In transcriptomics, "low-dimensional" holds for leading components within a dataset and weakens when dimension is judged by reproducibility across datasets or by information in the residual.
  conf: single (critic: H2-01:C-007) · class: not stated · holds: gene expression data; the within-dataset half rests on one study (Heimberg2016) · src: heimbergLowDimensionalityGene2016 (FT), lenzPrincipalComponentsAnalysis2016 (FT) · trail: H2-01 §2.4, §answers · from: H2-01:B-0097, H2-01:A-012, H2-01:C-007

### dimension-comparison: Low against higher dimension estimates
needs: direct-dimension, genome-dimension, expression-dimension
- **dimension-comparison.1** The low dimension estimates (Jiang2012, Piton2023's two leading axes, Heimberg2016) and the higher ones (Fahimipour2020 across genomes, Lenz2016 across datasets, Piton's remaining half of variance) largely reflect different objects (samples against genomes) and different criteria (within-dataset variance against cross-dataset stability), not direct contradiction on the same data.
  conf: not stated · class: not stated · holds: the sources of D1, which differ in object (taxa as rows, or non-microbial samples, for the related work) · src: jiangFunctionalBiogeographyOcean2012, pitonLifeHistoryStrategies2023, heimbergLowDimensionalityGene2016, fahimipourMappingBacterialMetabolic2020a, lenzPrincipalComponentsAnalysis2016 · trail: H2-01 §answers, §2.4 · from: H2-01:A-017, H2-01:A-018, H2-01:B-0085

### heldout-habitat: Covariation fitted in some habitats and scored on a withheld habitat
needs: functional-profile
- **heldout-habitat.1** No study was found that fitted covariation among microbial functions (a covariance or correlation matrix, a factorisation, a network, or a regression of some functions on others) in a set of habitats and scored it on a withheld habitat; this is a statement about the routes used, not that the literature lacks such a study.
  conf: not stated · class: search (note: "No study was found that fitted covariation among functions") · holds: three search angles via Europe PMC, PubMed and PMC E-utilities, Crossref, Semantic Scholar, OpenAlex, Unpaywall and known literature; WebSearch and Scholar Gateway unavailable; no test of function-function covariance (as opposed to taxon-to-function mappings or classifiers) across habitats either · src: none (a search result) · trail: H2-01 §3.1, §answers, §critic · from: H2-01:A-030, H2-01:A-031, H2-01:A-042, H2-01:A-047, H2-01:A-048, H2-01:A-110, H2-01:B-0037, H2-01:B-0098, H2-01:B-0099, H2-01:B-0100, H2-01:B-0018, H2-01:C-012 · rating: "Absent for the withheld-habitat microbial case"
- **heldout-habitat.2** No held-out test was found with presence/absence profiles, or comparing annotation schemes.
  conf: not stated · class: search (note: "Any test with presence/absence profiles, or comparing annotation schemes, in a held-out design") · holds: the routes in the search record · src: none (a search result) · trail: H2-01 §answers · from: H2-01:A-049
- **heldout-habitat.3** No held-out test was found in soils, oceans or other non-human habitats at all.
  conf: not stated · class: search (note: "Held-out tests in soils, oceans or other non-human habitats at all") · holds: the routes in the search record · src: none (a search result) · trail: H2-01 §answers · from: H2-01:A-050

### heldout-study: Covariation tested on a withheld study in the same habitat
needs: functional-profile, gene-set-aggregation
- **heldout-study.1** One direct microbial test of functional covariation on a withheld study was found (Chen2020, human gut).
  conf: single (marker) · class: search (note: "Chen et al. (2020) is the only direct microbial test found") · holds: human gut, between cohorts; removing it leaves no direct microbial test of functional covariation on held-out data · src: chenGutMicrobialCoabundance2020 (FT, figures re-checked; measured; SINGLE SOURCE) · trail: H2-01 §3.2, §answers, §critic · from: H2-01:I-0018, H2-01:A-032, H2-01:A-043, H2-01:A-053, H2-01:B-0039, H2-01:C-013 · rating: "Weak for withheld-study (one study, one habitat)"
- **heldout-study.2** Pathway co-abundances estimated in an IBD discovery cohort and tested in an independent IBD cohort (iHMP-IBD, 77 individuals) partly reproduced: of 37,106 testable pathway co-abundances, 21,882 (59.0%) replicated at P < 0.05; of 2,090 species co-abundances, 531 (25.4%).
  conf: single (critic: H2-01:C-013) · class: not stated · holds: human gut metagenomes from four cohorts (n = 2,379), 134 species and 343 MetaCyc pathways (HUMAnN2), SparCC combined with SPIEC-EASI to handle compositionality; withheld unit is a study, not a habitat · src: chenGutMicrobialCoabundance2020 (FT, re-checked by the reviewer) · trail: H2-01 §3.2, §answers, §critic · from: H2-01:B-0101, H2-01:B-0103, H2-01:B-0104, H2-01:A-033, H2-01:A-111, H2-01:C-013, H2-01:C-014
- **heldout-study.3** Chen2020's authors attribute the low species replication rate largely to power, since 81.6% of species and 65.1% of pathway co-abundances showed no significant difference in strength between the two cohorts.
  conf: not stated · class: not stated · holds: the IBD discovery cohort against iHMP-IBD · src: chenGutMicrobialCoabundance2020 (FT, re-checked by the reviewer) · trail: H2-01 §3.2 · from: H2-01:B-0105, H2-01:A-033
- **heldout-study.4** For the reductive TCA cycle pathway, 94.7% of 76 IBD-specific co-abundances replicated.
  conf: not stated · class: not stated · holds: the IBD discovery cohort against iHMP-IBD · src: chenGutMicrobialCoabundance2020 (FT, re-checked by the reviewer) · trail: H2-01 §3.2 · from: H2-01:B-0106
- **heldout-study.5** MetaCyc pathways share reactions and contributing species, so pathway-pathway co-abundance partly reflects shared members, and 43,355 of about 58,653 possible pathway pairs were significant in at least one cohort, which points to strong common factors that would make replication easy.
  conf: not stated · class: reading (note: "Cautions (reviewer's reading)") · holds: Chen2020's pathway co-abundances · src: chenGutMicrobialCoabundance2020 (FT) · trail: H2-01 §3.2 · from: H2-01:B-0108
- **heldout-study.6** "Replicated at P < 0.05" with n = 77 is a lenient bar.
  conf: not stated · class: reading (note: "Cautions (reviewer's reading)") · holds: Chen2020's replication test · src: none (the reviewer's reading of Chen2020) · trail: H2-01 §3.2 · from: H2-01:B-0108, H2-01:B-0109
- **heldout-study.7** Shared pathway members, strong common factors and a lenient threshold make the 59% replication an optimistic reading of transfer.
  conf: not stated · class: reading (note: "Cautions (reviewer's reading)") · holds: Chen2020; the critic: the review applies this caution to the replication result but not to the temporal stability or the between-cohort comparison · src: none (the reviewer's reading of Chen2020) · trail: H2-01 §answers, §3.2, §critic · from: H2-01:A-034, H2-01:B-0108, H2-01:B-0109, H2-01:C-116
- **heldout-study.8** In Chen2020 the withheld unit is a study within the same habitat and disease state, not a habitat.
  conf: not stated · class: not stated · holds: Chen2020 · src: none (the reviewer's statement) · trail: H2-01 §3.2 · from: H2-01:B-0110

### neighbouring-transfer: Neighbouring microbial held-out tests of other quantities
needs: functional-profile, shared-mean
- **neighbouring-transfer.1** PICRUSt accuracy fell with distance to the nearest reference genome (NSTI), across all samples (r = −0.4) and within each habitat (r = −0.25 to −0.82); accuracy was high in soils (0.81) and low in a hypersaline mat (reported 0.25, mean NSTI 0.23).
  conf: not stated · class: meas (marker) · holds: 16S-based prediction of metagenome functions across habitats · src: langillePredictiveFunctionalProfiling2013 (FT; measured) · trail: H2-01 §3.3 · from: H2-01:I-0019
- **neighbouring-transfer.2** Inference-level agreement of metagenome prediction tools was reasonable in human datasets and much lower in non-human and soil datasets.
  conf: not stated · class: not stated · holds: human, non-human and soil datasets · src: sunInferenceBasedAccuracyMetagenome2020 (FT) · trail: H2-01 §3.3 · from: H2-01:B-0111
- **neighbouring-transfer.3** These prediction tests transfer a genome-derived taxon-to-gene mapping, not covariation among functions.
  conf: not stated · class: not stated · holds: Langille2013, Sun2020 · src: none (the reviewer's statement) · trail: H2-01 §3.3, §answers · from: H2-01:B-0112, H2-01:A-035
- **neighbouring-transfer.4** Taxon-to-function mappings transfer less well as reference coverage of the target habitat falls.
  conf: not stated · class: not stated · holds: 16S-based functional prediction (Langille2013, Sun2020) · src: langillePredictiveFunctionalProfiling2013 (FT), sunInferenceBasedAccuracyMetagenome2020 (FT) · trail: H2-01 §3.3, §answers · from: H2-01:B-0113, H2-01:A-035
- **neighbouring-transfer.5** Colorectal cancer classifiers on eggNOG groups gave AUROC 0.70 to 0.81 study-to-study and 0.78 to 0.89 leave-one-study-out, similar to species-level classifiers.
  conf: not stated · class: meas (marker) · holds: human gut only; a classifier, not a covariance structure · src: wirbelMetaanalysisFecalMetagenomes2019 (FT; measured) · trail: H2-01 §3.3 · from: H2-01:I-0020, H2-01:B-0114, H2-01:A-035
- **neighbouring-transfer.6** In the E. coli pangenome, accessory-gene presence was predicted from other accessory genes on held-out random genomes; after filtering and removing phylogenetic signal, 16.7% of families were predictable at F1 ≥ 0.9 against a chance rate of about 1 to 1.7%.
  conf: single (marker) · class: not stated · holds: one species pangenome, held-out genomes · src: beavanContingencyRepeatabilityPredictability2023 (FT; SINGLE SOURCE) · trail: H2-01 §3.3 · from: H2-01:I-0021, H2-01:A-035
- **neighbouring-transfer.7** Across about 3,000 genomes, gene gain and loss in metabolic pathways was predictable in a hold-one-phylum-out test for each of the 10 largest phyla, with predictability differing significantly among phyla.
  conf: single (marker) · class: model (marker) · holds: bacterial genomes, phylogenetic gain/loss prediction · src: konnoMachineLearningEnables2023 (FT; modelled; SINGLE SOURCE) · trail: H2-01 §3.3 · from: H2-01:I-0022, H2-01:A-035
- **neighbouring-transfer.8** Gene content predicted MAG niche position along Baltic Sea gradients better than phylogeny under genome-level cross-validation.
  conf: not stated · class: not stated · holds: Baltic Sea MAGs · src: alnebergEcosystemwideMetagenomicBinning2020 (FT) · trail: H2-01 §3.3 · from: H2-01:B-0115
- **neighbouring-transfer.9** Phylogenetic-profile co-occurrence recovered same-pathway enzyme pairs better than homology.
  conf: not stated · class: not stated · holds: a benchmark partly circular with KEGG membership · src: chungAssemblingBacterialPuzzles2024 (AB) · trail: H2-01 §3.3 · from: H2-01:B-0116
- **neighbouring-transfer.10** A low-dimensional gene-to-function map transferred from strains to communities for denitrification.
  conf: not stated · class: not stated · holds: denitrification · src: gowdaGenomicStructurePredicts2022 (AB) · trail: H2-01 §3.3 · from: H2-01:B-0117
- **neighbouring-transfer.11** Five "generalizable" enterosignatures were derived from 5,230 gut metagenomes; what "generalizable" means as a held-out design was not read.
  conf: not stated · class: not stated · holds: taxonomic low-rank structure, human gut · src: friouxEnterosignaturesDefineCommon2023 (AB) · trail: H2-01 §3.3 · from: H2-01:B-0118, H2-01:B-0119 · limit: access (note: "(held-out design) was not read")

### other-field-transfer: Held-out tests of learned covariation in other fields
needs: none
- **other-field-transfer.1** Sparse module dictionaries learned on 5% of samples recovered expression of the same TCGA tumour type at about 87% (Spearman, SMAF), and a dictionary from a different tumour type gave 68% on average, related tumour types doing better; this is recovery of expression from 25 random composite measurements through a learned dictionary (compressed sensing), not a direct covariance-reproduction score.
  conf: single (marker) · class: meas (marker) · holds: TCGA tumour types (other field); simulated random composite measurements, m = 25, g = 5,000; the only other-field test found that withholds a biologically distinct group (the closest analogue of a habitat) · src: clearyEfficientGenerationTranscriptomic2017 (FT; measured; SINGLE SOURCE) · trail: H2-01 §3.4, §critic, §answers · from: H2-01:B-0120, H2-01:I-0023, H2-01:A-037, H2-01:A-054, H2-01:C-019, H2-01:C-020, H2-01:C-065, H2-01:C-066, H2-01:C-067
- **other-field-transfer.2** Cleary2017's authors warn that a dictionary is biased when training data do not represent the test data.
  conf: not stated · class: not stated · holds: TCGA tumour types · src: clearyEfficientGenerationTranscriptomic2017 (FT) · trail: H2-01 §3.4 · from: H2-01:B-0121
- **other-field-transfer.3** A linear model from about 1,000 landmark genes, trained on GEO microarrays, inferred 81% of non-measured transcripts well in independent GTEx RNA-seq (8,555 samples); about 19% were not well inferred.
  conf: single (marker) · class: meas (marker) · holds: withheld study and platform (other field) · src: subramanianNextGenerationConnectivity2017 (FT; measured; SINGLE SOURCE) · trail: H2-01 §3.4 · from: H2-01:I-0024, H2-01:A-038
- **other-field-transfer.4** A single co-expression network fitted to all 35 GTEx tissues pooled had held-out likelihood so low it was dropped from the comparison; per-tissue networks did better, and sharing between related tissues did better again; samples, not tissues, were withheld.
  conf: single (critic: H2-01:C-123) · class: meas (marker) · holds: 35 GTEx tissues, held-out samples within tissue (other field) · src: piersonSharingSpecificityCoexpression2015 (FT; measured; SINGLE SOURCE; critic: H2-01:C-123 was "FT; measured") · trail: H2-01 §3.4, §critic · from: H2-01:I-0025, H2-01:B-0122, H2-01:A-039, H2-01:C-015, H2-01:C-123
- **other-field-transfer.5** Individual co-expression networks predicted GO membership with mean AUROC 0.60 (bulk) and 0.56 (single cell); aggregating 163 networks reached 0.73 (bulk); sample size did not predict performance.
  conf: single (critic: H2-01:C-015) · class: meas (marker) · holds: co-expression replicability (other field) · src: crowExploitingSinglecellExpression2016 (FT; measured) · trail: H2-01 §3.4, §critic · from: H2-01:I-0026, H2-01:A-040, H2-01:C-015
- **other-field-transfer.6** A latent space learned on recount2 was concordant with dataset-specific models in rare-disease studies, with broader training capturing more pathways.
  conf: single (critic: H2-01:C-077) · class: not stated · holds: transcriptomics (other field); qualitative · src: taroniMultiPLIERTransferLearning2019 (FT; qualitative) · trail: H2-01 §3.4, §critic · from: H2-01:B-0123, H2-01:C-077
- **other-field-transfer.7** projectR tests whether a pattern is shared by projection.
  conf: not stated · class: not stated · holds: a framework, with no failure rate · src: steinobrienDecomposingCellIdentity2019 (FT; framework, no failure rate) · trail: H2-01 §3.4 · from: H2-01:B-0123
- **other-field-transfer.8** Global leaf-economics correlations may not hold at local scales, since correlation strength only bounds how differently traits can vary across scales.
  conf: not stated · class: not stated · holds: plant leaf traits across scales · src: messierTraitVariationIntegration2016 (AB) · trail: H2-01 §3.4 · from: H2-01:B-0124
- **other-field-transfer.9** Some leaf-trait correlations reverse sign within species compared with across species.
  conf: not stated · class: not stated · holds: plant leaf traits, within against across species · src: andereggWithinspeciesPatternsChallenge2018 (AB) · trail: H2-01 §3.4 · from: H2-01:B-0125
- **other-field-transfer.10** The plant-trait scale results are transfers across scale or taxonomic level, not across habitat.
  conf: not stated · class: not stated · holds: Messier2017, Anderegg2018 · src: none (the reviewer's statement) · trail: H2-01 §3.4 · from: H2-01:B-0126
- **other-field-transfer.11** In other fields covariation transfers partly, and each quantitative result is a single study.
  conf: single (critic: H2-01:C-015) · class: not stated · holds: transcriptomics; another field from microbial functional profiles · src: clearyEfficientGenerationTranscriptomic2017 (FT), subramanianNextGenerationConnectivity2017 (FT), piersonSharingSpecificityCoexpression2015 (FT), crowExploitingSinglecellExpression2016 (FT) · trail: H2-01 §answers, §critic · from: H2-01:A-036, H2-01:A-044, H2-01:C-015 · rating: "Moderate for partial transfer in transcriptomics"

### transfer-dependencies: What transfer appears to depend on
needs: heldout-study, neighbouring-transfer, other-field-transfer, expression-dimension, shared-mean
- **transfer-dependencies.1** There is no direct conflict on the same quantity: reproduction is high in some tests (Subramanian 81%; Chen reductive TCA 94.7%) and low in others (Cleary cross-type drop; pooled networks in Pierson; sign reversals across scales in plant traits).
  conf: not stated · class: not stated · holds: tests of different quantities in different fields · src: subramanianNextGenerationConnectivity2017 (FT), chenGutMicrobialCoabundance2020 (FT), clearyEfficientGenerationTranscriptomic2017 (FT), piersonSharingSpecificityCoexpression2015 (FT), andereggWithinspeciesPatternsChallenge2018 (AB) · trail: H2-01 §answers · from: H2-01:A-045, H2-01:A-046
- **transfer-dependencies.2** That transfer depends on similarity between training and target, breadth of training, and how much of the target is shared mean structure is the reviewer's synthesis across incommensurable tests; it pools covariance or dictionary transfer (Cleary2017, Pierson2015), taxon-to-gene mapping accuracy (Langille2013 NSTI), per-sample accuracy metrics (Sun2020) and phylogenetic gene gain/loss prediction (KonnoIwasaki2023); breadth rests on Taroni2019 alone (qualitative), and each dependency rests on one to three sources measuring different quantities.
  conf: not stated · class: reading (critic: H2-01:C-018) · holds: other-field and neighbouring microbial tests; none of these dependencies has been measured for microbial function-function covariation across habitats · src: clearyEfficientGenerationTranscriptomic2017 (FT), piersonSharingSpecificityCoexpression2015 (FT), langillePredictiveFunctionalProfiling2013 (FT), sunInferenceBasedAccuracyMetagenome2020 (FT), konnoMachineLearningEnables2023 (FT), taroniMultiPLIERTransferLearning2019 (FT), lenzPrincipalComponentsAnalysis2016 (FT) · trail: H2-01 §3.5, §critic, §answers · from: H2-01:A-041, H2-01:A-046, H2-01:A-112, H2-01:B-0127, H2-01:B-0128, H2-01:C-016, H2-01:C-017, H2-01:C-018, H2-01:C-054, H2-01:C-077, H2-01:C-128

### levels-within: Function levels against taxonomic composition within a habitat (case A)
needs: functional-profile, shared-mean, genome-size, gene-set-aggregation
- **levels-within.1** Within a habitat where taxonomy turns over, several studies report function levels more stable than taxonomic composition (HMP2012, Louca2016b, Burke2011, Shan2023, Aira2026); the direction depends on processing, and there is direct measured contrary evidence in human gut (Manor2017) and coastal ocean (Galand2018, abstract).
  conf: cont (note: "Conflicts: Galand2018 (and the processing studies Manor2017, Nayfach2015) against HMP2012, Louca2016b, Burke2011") · class: not stated · holds: two of the supporting studies are full text (HMP2012, Burke2011) and three rest on abstracts (Louca2016b, Shan2023, Aira2026); none controls for normalisation, aggregation and granularity together; the best-covered cell of D3 · src: theStructureFunctionDiversity2012 (FT; measured), loucaHighTaxonomicVariability2016 (AB; measured), burkeBacterialCommunityAssembly2011 (FT; measured), shanAnnotationfreeDiscoveryFunctional2023 (AB), airaFasterTurnoverTaxonomic2026 (AB), manorRevisedComputationalMetagenomic2017 (FT, re-checked), galandStrongLinkMarine2018 (AB) · trail: H2-01 §critic, §answers, §4.1 · from: H2-01:A-055, H2-01:A-057, H2-01:A-061, H2-01:A-062, H2-01:A-063, H2-01:A-113, H2-01:B-0131, H2-01:C-021, H2-01:C-022, H2-01:C-023, H2-01:C-027, H2-01:C-124, H2-01:C-126 · rating: "Moderate for the direction as reported"
- **levels-within.2** The HMP consortium reports pathway relative abundances "much more constant and evenly diverse" than organismal abundances across individuals within body sites, with a stable housekeeping core; this is a quoted descriptive statement, and the review gives no quantitative figure.
  conf: not stated · class: meas (marker) · holds: healthy human body sites; not re-checked by the reviewer (the critic) · src: theStructureFunctionDiversity2012 (FT; measured) · trail: H2-01 §2.2, §4.1, §critic · from: H2-01:I-0007, H2-01:I-0027, H2-01:C-004, H2-01:C-064, H2-01:C-071
- **levels-within.3** In bromeliad tank microcosms, functional-group structure was similar across replicates while taxonomy within groups was highly variable.
  conf: not stated · class: meas (marker) · holds: bromeliad tank microcosms · src: loucaHighTaxonomicVariability2016 (AB; measured) · trail: H2-01 §4.1 · from: H2-01:I-0028
- **levels-within.4** On a macroalgal host, similarity was about 15% in species composition against 70% in COG composition; the contrast compares a species table with a coarser COG table, and the taxonomic figure is from an earlier study.
  conf: not stated · class: meas (marker) · holds: one macroalgal host · src: burkeBacterialCommunityAssembly2011 (FT; measured) · trail: H2-01 §4.1 · from: H2-01:I-0029, H2-01:B-0132
- **levels-within.5** In replicate soil microcosms, annotation-free functional groups were stable in summed abundance despite large variation in species composition.
  conf: not stated · class: not stated · holds: replicate soil microcosms · src: shanAnnotationfreeDiscoveryFunctional2023 (AB) · trail: H2-01 §4.1 · from: H2-01:B-0133
- **levels-within.6** During vermicomposting, taxonomic turnover was about twelve times functional turnover.
  conf: not stated · class: not stated · holds: vermicomposting over time; no non-earthworm control · src: airaFasterTurnoverTaxonomic2026 (AB; no non-earthworm control) · trail: H2-01 §4.1 · from: H2-01:B-0134
- **levels-within.7** In a model, taxa-function robustness was higher in gut than in vaginal communities, so how far function tracks taxonomy may itself vary by habitat.
  conf: single (critic: H2-01:C-084) · class: model (marker) · holds: human gut and vaginal communities; one modelled, abstract-only study · src: engTaxafunctionRobustnessMicrobial2018 (AB; modelled) · trail: H2-01 §4.1, §critic · from: H2-01:I-0030, H2-01:A-060, H2-01:C-084
- **levels-within.8** Within the human gut, how consistently genera carry metabolic modules differs among genera, and module-derived redundancy was lower in the Bacteroides enterotype.
  conf: not stated · class: not stated · holds: human gut · src: vieirasilvaSpeciesfunctionRelationshipsShape2016 (AB) · trail: H2-01 §4.1 · from: H2-01:B-0135
- **levels-within.9** Revised processing (MUSiCC normalisation, filtering of prevalent families, non-uniform mapping) gave functional profiles that identified hosts as well as strain-level taxonomic markers did; the authors call perceived functional uniformity "a potential misconception".
  conf: not stated · class: meas (critic: H2-01:C-125) · holds: human microbiome (HMP); contrary evidence to levels-within.1, measured in full text · src: manorRevisedComputationalMetagenomic2017 (FT, re-checked by the reviewer) · trail: H2-01 §critic · from: H2-01:C-023, H2-01:C-024, H2-01:C-025, H2-01:C-051, H2-01:C-125
- **levels-within.10** The counter-evidence to the levels-stable pattern is methodological and applies to every study in this cell: relative normalisation and pathway aggregation reduce apparent functional variability, genome size creates both spurious variability and spurious stability, and a dominant mean profile makes profiles look alike.
  conf: not stated · class: not stated · holds: same-habitat comparisons of function levels with taxonomic composition · src: manorRevisedComputationalMetagenomic2017 (FT, re-checked), nayfachAverageGenomeSize2015 (FT per metagenomics angle), manorMUSiCCMarkerGenes2015 (FT), sunInferenceBasedAccuracyMetagenome2020 (FT) · trail: H2-01 §4.1, §answers · from: H2-01:B-0136, H2-01:B-0137, H2-01:A-058, H2-01:C-124
- **levels-within.11** Comparing a fine taxonomic table with a coarse functional table favours functional stability by construction; this applies equally to Burke2011 and Ramírez-Flandes2019.
  conf: not stated · class: reading (note: "reviewer's reading") · holds: comparisons of tables at different granularity · src: none (the reviewer's reading) · trail: H2-01 §4.1, §answers · from: H2-01:B-0137, H2-01:A-058
- **levels-within.12** In a coastal Mediterranean time series, the taxonomy-function link was strong when function was measured from all reads or all predicted genes and weaker with annotated orthologues or taxonomy-inferred functions; the authors conclude that this challenges functional redundancy, and the abstract is explicit that using all reads, not annotated genes, was essential.
  conf: not stated · class: not stated · holds: one coastal Mediterranean time series · src: galandStrongLinkMarine2018 (AB for me; the reported R² values came from an automated summary and are not used) · trail: H2-01 §4.1, §Provenance · from: H2-01:B-0138, H2-01:B-0139, H2-01:A-059, H2-01:B-0015 · limit: access (note: "it stays abstract only and its R2 values are not used")
- **levels-within.13** The "levels stable, taxonomy variable" pattern depends on annotation scheme.
  conf: not stated · class: not stated · holds: same-habitat comparisons · src: galandStrongLinkMarine2018 (AB) · trail: H2-01 §4.1, §answers · from: H2-01:B-0140, H2-01:A-057
- **levels-within.14** Whether the greater stability of function levels is biological rather than processing-driven is weakly supported: none of the studies controls for normalisation, aggregation and granularity together.
  conf: not stated · class: not stated · holds: same-habitat studies of case A · src: none (the reviewer's synthesis) · trail: H2-01 §answers · from: H2-01:A-061, H2-01:A-062 · rating: "weak for the claim that the stability is biological rather than processing-driven"
- **levels-within.15** Not measured: same-habitat comparisons using marker-normalised, unaggregated or all-read functional profiles alongside taxonomy at matched resolution; non-human habitats beyond a few microcosm and marine examples.
  conf: not stated · class: search (note: "Not measured: Same-habitat comparisons using marker-normalised, unaggregated or all-read functional profiles") · holds: the routes in the search record · src: none (a search result) · trail: H2-01 §answers · from: H2-01:A-064

### levels-across: Function levels against taxonomic composition across habitats (case B)
needs: functional-profile, levels-within
- **levels-across.1** Across habitats where taxonomy turns over, whether function levels track taxonomic composition is contested, and the coupled and decoupled results are incommensurable.
  conf: cont (critic: H2-01:C-028) · class: not stated · holds: coupled side Fierer2012 and Salazar2019, decoupled side Louca2016a and Nelson2016; several measured studies in each direction, but several are single studies or abstract only; the result depends on annotation and resolution · src: fiererCrossbiomeMetagenomicAnalyses2012 (FT per trait-ecology angle), salazarGeneExpressionChanges2019 (FT), loucaDecouplingFunctionTaxonomy2016 (AB), nelsonGlobalBiogeographyMicrobial2016 (SECONDARY/unverified) · trail: H2-01 §critic, §answers, §4.2 · from: H2-01:A-069, H2-01:A-075, H2-01:A-076, H2-01:A-078, H2-01:A-114, H2-01:B-0141, H2-01:C-028 · rating: "Weak to moderate"
- **levels-across.2** The coupled and decoupled results use different function definitions (all reads or gene categories against taxonomy-derived groups) and different comparisons (distance-matrix correlation against variance partitioning), and cannot be pooled.
  conf: not stated · class: reading (note: "Reviewer's reading") · holds: the case B studies · src: none (the reviewer's reading) · trail: H2-01 §4.2, §answers · from: H2-01:B-0149, H2-01:A-073
- **levels-across.3** Across 16 soils from five biomes, functional and taxonomic Bray-Curtis distances correlated (Mantel r = 0.76; with unweighted UniFrac, 0.82).
  conf: not stated · class: meas (marker) · holds: 16 soils, five biomes; small n; removing it would leave the coupled side resting on Salazar2019's global statement · src: fiererCrossbiomeMetagenomicAnalyses2012 (FT per trait-ecology angle; measured; small n) · trail: H2-01 §4.2, §critic, §Provenance · from: H2-01:I-0031, H2-01:A-070, H2-01:A-086, H2-01:B-0016, H2-01:C-032, H2-01:C-061, H2-01:C-062, H2-01:C-063 · limit: access (critic: H2-01:C-062)
- **levels-across.4** In Tara Oceans, OG-level metagenomic and metatranscriptomic differentiation tracked taxonomic differentiation along latitude, and the authors conclude that "on a global scale, taxonomic composition largely shapes the composition of gene functional content".
  conf: not stated · class: meas (marker) · holds: global ocean; the critic: the conclusion is taken at the authors' word, and taxonomic and OG profiles come from the same reads and share compositional structure · src: salazarGeneExpressionChanges2019 (FT; measured) · trail: H2-01 §4.2, §critic · from: H2-01:I-0032, H2-01:A-070, H2-01:C-127
- **levels-across.5** A CCA on phylogenetic composition agreed with functional trends across the Global Ocean Sampling metagenomes.
  conf: not stated · class: not stated · holds: GOS metagenomes · src: raesTowardMolecularTraitbased2011 (FT) · trail: H2-01 §4.2 · from: H2-01:B-0142
- **levels-across.6** Function separated habitats more strongly than taxonomy: across 247 metagenomes from 18 biomes, oxidoreductase profiles gave PERMANOVA F = 12.5 and all 6,789 KOs F = 10.7, against 1.8 for 4,011 species and 2.8 at the fourth taxonomic rank; the feature sets differ in size and sparsity, so the F statistics are not commensurable.
  conf: not stated · class: not stated · holds: 247 metagenomes, 18 biomes; bears on which separates habitats more, a different question from coupling · src: ramirezflandesRedoxTraitsCharacterize2019 (FT) · trail: H2-01 §4.2, §answers · from: H2-01:B-0143, H2-01:B-0144, H2-01:A-071, H2-01:A-079
- **levels-across.7** Functional and taxonomic diversity rankings of biomes did not correspond.
  conf: single (marker) · class: meas (marker) · holds: 247 metagenomes, 18 biomes · src: ramirezflandesRedoxTraitsCharacterize2019 (FT; measured; SINGLE SOURCE) · trail: H2-01 §4.2 · from: H2-01:I-0033
- **levels-across.8** Nine biomes were strongly discriminated by metabolic profiles.
  conf: not stated · class: not stated · holds: nine biomes · src: dinsdaleFunctionalMetagenomicProfiling2008 (AB) · trail: H2-01 §4.2 · from: H2-01:B-0145
- **levels-across.9** In the global ocean, environment strongly shaped functional-group distribution and weakly shaped taxonomy within groups, "roughly independent axes of variation".
  conf: not stated · class: deriv (marker) · holds: global ocean; functional groups assigned from taxonomy; removing it would leave the decoupled side resting on Nelson2016 alone · src: loucaDecouplingFunctionTaxonomy2016 (AB; derived, because functional groups were assigned from taxonomy) · trail: H2-01 §4.2, §answers · from: H2-01:I-0034, H2-01:I-0001, H2-01:A-085, H2-01:C-030
- **levels-across.10** Soil nitrogen-pathway frequencies were explained by habitat and soil C and N, while taxonomy within N functional groups was poorly predicted by environment.
  conf: not stated · class: not stated · holds: soils across habitats; read only through an automated summary, figures not re-verified · src: nelsonGlobalBiogeographyMicrobial2016 (SECONDARY/unverified; critic: H2-01:C-059 was "FT via an automated summary") · trail: H2-01 §4.2, §critic, §Provenance · from: H2-01:B-0146, H2-01:I-0001, H2-01:B-0016, H2-01:C-029, H2-01:C-030, H2-01:C-031, H2-01:C-056, H2-01:C-057, H2-01:C-058, H2-01:C-059, H2-01:C-060 · limit: access (critic: H2-01:C-060)
- **levels-across.11** At 95%-identity gene resolution, most genes were specific to one of 14 habitats.
  conf: not stated · class: not stated · holds: 14 habitats · src: coelhoTowardsBiogeographyProkaryotic2021 (AB) · trail: H2-01 §4.2 · from: H2-01:B-0147, H2-01:A-072
- **levels-across.12** At the level of core OG functions, more than 73% of ocean core-function abundance was shared with the human gut.
  conf: not stated · class: not stated · holds: Tara Oceans against human gut · src: sunagawaStructureFunctionGlobal2015 (AB) · trail: H2-01 §4.2 · from: H2-01:B-0147, H2-01:A-072
- **levels-across.13** The same data can support turnover or constancy depending on resolution; resolution decides much of the case B result.
  conf: not stated · class: not stated · holds: Coelho2022 and Sunagawa2015 · src: coelhoTowardsBiogeographyProkaryotic2021 (AB), sunagawaStructureFunctionGlobal2015 (AB) · trail: H2-01 §4.2, §answers · from: H2-01:B-0148, H2-01:A-072
- **levels-across.14** Not measured: case B with taxonomy and function at matched resolution and matched feature counts; case B with marker-normalised functional profiles.
  conf: not stated · class: search (note: "Case B with taxonomy and function at matched resolution and matched feature counts") · holds: the routes in the search record · src: none (a search result) · trail: H2-01 §answers · from: H2-01:A-081, H2-01:A-082

### taxonomy-fixed: Function levels where habitat changes but taxonomy does not (case C)
needs: levels-within
- **taxonomy-fixed.1** No microbial metagenomic study was found that holds taxonomy fixed while habitat varies and compares function levels; transplant, common-garden and single-lineage-across-habitat designs are not listed among the routes searched.
  conf: not stated · class: search (note: "No microbial metagenomic study was found that holds taxonomy fixed while habitat varies") · holds: the routes in the search record · src: none (a search result) · trail: H2-01 §4.3, §answers, §critic · from: H2-01:B-0150, H2-01:A-074, H2-01:A-077, H2-01:A-080, H2-01:B-0018, H2-01:C-033, H2-01:C-034 · rating: "Case C: absent"
- **taxonomy-fixed.2** Salazar2019 separate regulatory change (metatranscriptome) from community turnover in the ocean, and per the search agent's reading turnover dominated at global scale; this concerns expression, not gene content.
  conf: not stated · class: not stated · holds: global ocean, metatranscriptomes · src: salazarGeneExpressionChanges2019 (FT) · trail: H2-01 §4.3 · from: H2-01:B-0151, H2-01:B-0152

### covariation-stability: Covariation among functions against levels and composition (case D)
needs: heldout-study, cwm, levels-within
- **covariation-stability.1** No microbial study was found that compares the between-habitat stability of function-function covariation with that of function levels or taxonomic composition.
  conf: not stated · class: search (note: "No microbial study was found that compares the between-habitat stability of function-function covariation") · holds: search routes as for D2 · src: none (a search result) · trail: H2-01 §answers, §1. What, §critic · from: H2-01:A-087, H2-01:A-094, H2-01:A-117, H2-01:B-0038, H2-01:B-0018, H2-01:C-035 · rating: "Absent for the microbial cross-habitat case"
- **covariation-stability.2** Not measured: the covariation comparison where taxonomy does not turn over; covariation in presence/absence profiles; a comparison corrected for shared gene-set members.
  conf: not stated · class: search (note: "covariation in presence/absence profiles; comparison corrected for shared gene-set members") · holds: the routes in the search record · src: none (a search result) · trail: H2-01 §answers · from: H2-01:A-099
- **covariation-stability.3** Across four human gut cohorts, 64.3% of pathway co-abundances and 38.6% of species co-abundances differed in strength (Cochran's Q, FDR < 0.05).
  conf: single (critic: H2-01:C-082) · class: not stated · holds: human gut cohorts that differ in disease state and population (IBD, obesity, two population cohorts), not habitat; compares pathway covariation with species covariation, not composition; heterogeneity tests have more power for stronger and more numerous correlations, and that caution is not applied in the review (the critic); removing it leaves no microbial measurement of functional covariation stability · src: chenGutMicrobialCoabundance2020 (FT, re-checked) · trail: H2-01 §4.4, §critic, §answers · from: H2-01:B-0153, H2-01:B-0156, H2-01:B-0157, H2-01:A-088, H2-01:A-095, H2-01:A-102, H2-01:C-036, H2-01:C-039, H2-01:C-040, H2-01:C-041, H2-01:C-082, H2-01:C-118, H2-01:C-129 · rating: "Weak (one study) for the microbial between-cohort case"
- **covariation-stability.4** Among the entities involved in variable co-abundances, 84% of 304 pathways and also 76% of 100 species differed in level between cohorts.
  conf: single (critic: H2-01:C-082) · class: not stated · holds: four human gut cohorts · src: chenGutMicrobialCoabundance2020 (FT, re-checked) · trail: H2-01 §4.4, §critic · from: H2-01:B-0154, H2-01:A-088, H2-01:C-037, H2-01:C-055, H2-01:C-082
- **covariation-stability.5** In this one study, pathway co-abundances varied between cohorts more often than species co-abundances, and variable covariation usually co-occurred with variable levels, for pathways and species alike; the comparison is with taxonomic covariation, not composition, and the power caution applies.
  conf: single (critic: H2-01:C-082) · class: not stated · holds: one study, one habitat, one heterogeneity test; the same test logic is treated leniently where it supports stability and variability claims (the critic) · src: chenGutMicrobialCoabundance2020 (FT, re-checked) · trail: H2-01 §4.4, §answers, §critic · from: H2-01:B-0155, H2-01:A-089, H2-01:C-037, H2-01:C-081, H2-01:C-082, H2-01:C-083, H2-01:C-119
- **covariation-stability.6** Covariation among microbial functions has otherwise been fitted only on pooled cross-habitat data, and none of these studies measures whether the covariation differs by habitat.
  conf: not stated · class: not stated · holds: Nelson2016, Salazar2019, Gianoulis2009, Barberan2012 · src: nelsonGlobalBiogeographyMicrobial2016, salazarGeneExpressionChanges2019 (FT), gianoulisQuantifyingEnvironmentalAdaptation2009 (AB), barberanExplorationCommunityTraits2011 (AB) · trail: H2-01 §4.4, §answers · from: H2-01:B-0160, H2-01:B-0161, H2-01:A-091
- **covariation-stability.7** Soil nitrogen-pathway frequencies were "overwhelmingly positively correlated" across 365 soils from 10 habitat types.
  conf: not stated · class: not stated · holds: pooled across 365 soils and 10 habitat types; read only through an automated summary · src: nelsonGlobalBiogeographyMicrobial2016 (SECONDARY/unverified; critic: H2-01:C-059 was "FT via an automated summary") · trail: H2-01 §4.4, §critic · from: H2-01:B-0160, H2-01:B-0146, H2-01:C-059, H2-01:C-060 · limit: access (critic: H2-01:C-060)
- **covariation-stability.8** Co-abundance and co-expression of ocean OGs predicted shared KEGG membership.
  conf: not stated · class: not stated · holds: global ocean, pooled; fitted and scored on the same samples; partly circular · src: salazarGeneExpressionChanges2019 (FT; fitted and scored on the same samples; partly circular) · trail: H2-01 §4.4 · from: H2-01:B-0160
- **covariation-stability.9** Amino-acid transport and cofactor synthesis covaried across the Global Ocean Sampling metagenomes.
  conf: not stated · class: not stated · holds: GOS, pooled · src: gianoulisQuantifyingEnvironmentalAdaptation2009 (AB) · trail: H2-01 §4.4 · from: H2-01:B-0160
- **covariation-stability.10** Community genomic traits covaried, some possibly for technical reasons.
  conf: not stated · class: not stated · holds: microbial metagenomes, pooled · src: barberanExplorationCommunityTraits2011 (AB) · trail: H2-01 §4.4 · from: H2-01:B-0160
- **covariation-stability.11** In plant traits the evidence runs both ways: CWM covariation more stable than levels in one study, covariation shifting with environment in others; each item is a single study.
  conf: cont (note: "Conflicts: Bruelheide2018 (covariation stable, levels variable) against FloresMoreno2019, Wright2005 and DwyerLaughlin2017 (covariation shifts with environment)") · class: not stated · holds: plant traits (other field); the plant sources differ in level (community against species), in imputation and in gradient · src: bruelheideGlobalTraitenvironmentRelationships2018 (FT), floresmorenoRobustnessTraitConnections2019 (FT), wrightModulationLeafEconomic2005 (AB), dwyerConstraintsTraitCombinations2017 (AB) · trail: H2-01 §answers, §4.4, §critic · from: H2-01:A-092, H2-01:A-096, H2-01:A-097, H2-01:A-098, H2-01:A-116, H2-01:B-0162, H2-01:C-043 · rating: "Mixed and other-field for plant traits and expression"
- **covariation-stability.12** Community-weighted plant traits across 1.1 million plots showed the same two covariation axes as species-level traits, "unexpected" per the authors, while climate and soil explained only 10.8 to 14.0% of CWM variation.
  conf: single (marker) · class: meas (marker) · holds: plant communities worldwide; removing it removes the only large-scale case of covariation more stable than levels · src: bruelheideGlobalTraitenvironmentRelationships2018 (FT; measured; SINGLE SOURCE) · trail: H2-01 §4.4, §answers · from: H2-01:I-0035, H2-01:A-092, H2-01:A-103, H2-01:C-122
- **covariation-stability.13** Precision-matrix trait networks differed among climate regions in density and modularity, with some edges present everywhere and others region-specific.
  conf: single (critic: H2-01:C-043) · class: not stated · holds: plant traits across climate regions; heavy imputation · src: floresmorenoRobustnessTraitConnections2019 (FT; heavy imputation) · trail: H2-01 §4.4 · from: H2-01:I-0036, H2-01:A-092, H2-01:C-043
- **covariation-stability.14** Leaf-economic slopes shifted with climate.
  conf: single (critic: H2-01:C-043) · class: not stated · holds: leaf economic traits across climates · src: wrightModulationLeafEconomic2005 (AB) · trail: H2-01 §4.4 · from: H2-01:I-0036, H2-01:A-092, H2-01:C-043
- **covariation-stability.15** Along an aridity gradient, a height-seed mass covariance strengthened while level-type functional diversity was poorly explained by aridity.
  conf: single (marker) · class: not stated · holds: one aridity gradient · src: dwyerConstraintsTraitCombinations2017 (AB; SINGLE SOURCE) · trail: H2-01 §4.4 · from: H2-01:I-0036, H2-01:A-092
- **covariation-stability.16** A review reports trait-network topology shifting along resource gradients.
  conf: not stated · class: assert (marker) · holds: plant trait networks · src: hePlantTraitNetworks2020 (AB; asserted) · trail: H2-01 §4.4 · from: H2-01:I-0037
- **covariation-stability.17** Tissue-specific co-expression networks outperformed pooled ones, and modules conserved across tissues carried shared housekeeping functions.
  conf: single (critic: H2-01:C-123) · class: not stated · holds: 35 GTEx tissues (other field) · src: piersonSharingSpecificityCoexpression2015 (FT) · trail: H2-01 §4.4, §answers · from: H2-01:B-0164, H2-01:A-093, H2-01:C-123

### temporal-covariation: Temporal stability of functional covariation
needs: heldout-study
- **temporal-covariation.1** Between the first and last iHMP-IBD time points, about one year apart, 99.6% of pathway and 90.6% of species co-abundances showed no significant difference in strength (Cochran's Q, P > 0.05); this is a count of non-significant differences at n = 77, an absence-of-evidence count, not near-complete stability.
  conf: single (note: "One microbial measurement") · class: not stated · holds: one IBD cohort, 77 individuals; the same lenient bar the review criticises for replication (the critic) · src: chenGutMicrobialCoabundance2020 (FT, re-checked by the reviewer) · trail: H2-01 §3.2, §4.5, §critic · from: H2-01:B-0107, H2-01:B-0165, H2-01:B-0014, H2-01:C-042, H2-01:C-068, H2-01:C-069, H2-01:C-070, H2-01:C-117
- **temporal-covariation.2** No trait-ecology study of temporal CWM covariation was found, and the statement names no routes.
  conf: not stated · class: search (note: "No trait-ecology study of temporal CWM covariation was found") · holds: no routes named (the critic) · src: none (a search result) · trail: H2-01 §4.5, §critic · from: H2-01:B-0166, H2-01:C-104

### function-definition: What is treated as "a function"
needs: levels-within, levels-across, processing-dimension, expression-dimension, other-field-transfer, heldout-study, trait-dimension
- **function-definition.1** The answer to every direction depends on what is treated as "a function".
  conf: not stated · class: reading (critic: H2-01:C-132) · holds: all three directions · src: none (the reviewer's synthesis) · trail: H2-01 §5. How, §critic · from: H2-01:B-0167, H2-01:C-132
- **function-definition.2** Coarse, aggregated, relatively normalised functions look stable, and fine, marker-normalised or all-read functions look more tied to taxonomy; the pieces are measured (Manor2017, Manor2015, Nayfach2015, Sun2020, Coelho2022, Galand2018 abstract), each a single study for its specific quantity, and merging annotation granularity, normalisation, mapping and all-read comparison into one coarse-fine axis is the reviewer's synthesis.
  conf: single (note: "each is a single study for its specific quantity") · class: reading (critic: H2-01:C-132) · holds: same-habitat and cross-habitat comparisons of levels and taxonomy · src: manorRevisedComputationalMetagenomic2017 (FT), manorMUSiCCMarkerGenes2015 (FT), nayfachAverageGenomeSize2015 (FT per metagenomics angle), sunInferenceBasedAccuracyMetagenome2020 (FT), coelhoTowardsBiogeographyProkaryotic2021 (AB), galandStrongLinkMarine2018 (AB) · trail: H2-01 §5. How, §critic · from: H2-01:B-0168, H2-01:B-0169, H2-01:C-080, H2-01:C-131, H2-01:C-132
- **function-definition.3** No cited source estimated dimension for fine against coarse functions.
  conf: not stated · class: search (critic: H2-01:C-079) · holds: the sources of Section 5 · src: none (the critic's reading of the sources) · trail: H2-01 §critic · from: H2-01:C-053, H2-01:C-079
- **function-definition.4** The same pattern appears in transcriptomics, where low dimensionality within datasets (Heimberg2016) coexists with unstable higher components across datasets (Lenz2016) and partial transfer across tissue types (Cleary2017).
  conf: not stated · class: reading (critic: H2-01:C-132) · holds: transcriptomics (other field) · src: heimbergLowDimensionalityGene2016 (FT), lenzPrincipalComponentsAnalysis2016 (FT), clearyEfficientGenerationTranscriptomic2017 (FT) · trail: H2-01 §5. How · from: H2-01:B-0170, H2-01:C-132
- **function-definition.5** Failure modes to expect in this literature: dimension estimates dominated by a mean profile; a genome-size axis that is partly technical; covariation between gene sets that share members; per-sample correlation metrics that ignore across-sample variance; comparisons of tables at different granularity; covariation inherited from imputation (plant traits); and replication judged against lenient thresholds with strong common factors (Chen2020).
  conf: not stated · class: not stated · holds: the literature reviewed for all three directions · src: none (the reviewer's synthesis) · trail: H2-01 §5. How · from: H2-01:B-0171

## Do not say

- **dns.1** "Profiles appear dominated by a shared mean."
  why: generalises a per-sample Spearman accuracy metric under permutation (Sun2020) and HMP descriptive statements (human body sites) to functional profiles in general, and merges sample-level profiles, genome-level presence/absence and a per-sample metric into one characterisation; neither source is a decomposition that measures a mean profile · instead: shared-mean.1 · trail: H2-01 §critic · from: H2-01:A-108, H2-01:C-002, H2-01:C-052, H2-01:C-076, H2-01:C-130
- **dns.2** "Much of what looks like low dimensionality in raw functional profiles is a shared mean" / "the leading structure is partly a shared mean profile".
  why: the critic: the body supports only that per-sample functional profiles are highly similar in these datasets; neither Sun2020 nor HMP2012 measures how much of a sample-by-function matrix is a mean profile · instead: shared-mean.1, direct-dimension.17 · trail: H2-01 §critic · from: H2-01:B-0060, H2-01:A-006, H2-01:C-005, H2-01:C-006
- **dns.3** "Across genomes, metabolic presence/absence is high-dimensional (dozens to hundreds of coordinates)."
  why: rests on one modelled study (Fahimipour2020, diffusion maps) and is phrased as a property of genomes in general · instead: genome-dimension.1 · trail: H2-01 §critic · from: H2-01:A-011, H2-01:A-108, H2-01:C-072
- **dns.4** "These processing shifts lower apparent dimension" (stated as a finding, without the label).
  why: the critic: it is the reviewer's inference, labelled as such in Section 2.3 and the D1 answer; the Section 6 summary drops that label · instead: processing-dimension.3 · trail: H2-01 §critic · from: H2-01:C-133
- **dns.5** "Across fields, transfer appears to depend on similarity between training and target, breadth of training, and how much of the target is shared mean structure."
  why: pools incommensurable tests (covariance or dictionary transfer, taxon-to-gene mapping accuracy, per-sample accuracy metrics, phylogenetic gene gain/loss prediction); breadth rests on Taroni2019 alone; the body does not support it as a finding · instead: transfer-dependencies.2 · trail: H2-01 §critic · from: H2-01:A-041, H2-01:C-016, H2-01:C-054, H2-01:C-077, H2-01:C-128
- **dns.6** "Other fields show partial transfer that falls with dissimilarity between training and target."
  why: the same pooled dependency stated as a finding across incommensurable tests · instead: other-field-transfer.11, transfer-dependencies.2 · trail: H2-01 §critic · from: H2-01:A-112, H2-01:C-016, H2-01:C-054
- **dns.7** "Module dictionaries recovered held-out profiles" (Cleary2017's 87% to 68% as reproduction of covariation).
  why: the figures are Spearman recovery from 25 simulated random composite measurements through the dictionary (compressed sensing), not a direct covariance-reproduction score; the answer states the transfer more directly than the full text supports · instead: other-field-transfer.1 · trail: H2-01 §critic · from: H2-01:A-037, H2-01:C-019, H2-01:C-020, H2-01:C-065, H2-01:C-066, H2-01:C-067
- **dns.8** "Galand2018 is the only direct same-habitat contrary result."
  why: Manor2017's full text directly measures that revised functional profiles identify hosts as well as strain-level taxonomy does; contrary evidence is under-weighted relative to its access · instead: levels-within.9, levels-within.12 · trail: H2-01 §critic · from: H2-01:A-068, H2-01:C-026, H2-01:C-050
- **dns.9** "HMP pathways are much more constant than organisms" as measured evidence of equal weight to the quantified studies.
  why: a quoted descriptive statement with no quantitative figure in the review · instead: levels-within.2 · trail: H2-01 §critic · from: H2-01:C-071
- **dns.10** "Nelson2016 (full text)."
  why: read only through an automated summary of the PMC page, figures not re-verified; a machine summary is not a full-text reading (critic: SECONDARY/unverified) · instead: levels-across.10 · trail: H2-01 §critic · from: H2-01:A-083, H2-01:C-031, H2-01:C-056, H2-01:C-058
- **dns.11** "84% of pathways in variable co-abundances also differed in level" (without the species figure).
  why: the full text gives the matching figure that 76% of 100 species also did, so the pathway result looks more distinctive than it is · instead: covariation-stability.4 · trail: H2-01 §critic · from: H2-01:C-038, H2-01:C-120
- **dns.12** "One microbial single-habitat study found pathway covariation less stable than species covariation and linked to level differences."
  why: stated without the power caveat (heterogeneity tests detect stronger, more numerous correlations more easily) and without the qualifier that the comparison is with species covariation, not composition · instead: covariation-stability.3, covariation-stability.5 · trail: H2-01 §critic · from: H2-01:A-115, H2-01:C-083, H2-01:C-129
- **dns.13** "Pathway co-abundances almost fully stable over about a year within one cohort (99.6%)."
  why: a count of co-abundances with no significant difference at n = 77, an absence-of-evidence count; it should not be read as near-complete stability · instead: temporal-covariation.1 · trail: H2-01 §critic · from: H2-01:A-090, H2-01:B-0159, H2-01:C-042, H2-01:C-068, H2-01:C-070, H2-01:C-117
- **dns.14** "Fine, marker-normalised or all-read functions look higher-dimensional and more tied to taxonomy."
  why: no cited source estimated dimension for fine against coarse functions; the reviewer's synthesis presented as a pattern that measured pieces "establish" · instead: function-definition.2, function-definition.3 · trail: H2-01 §critic · from: H2-01:B-0168, H2-01:C-053, H2-01:C-078, H2-01:C-079, H2-01:C-080, H2-01:C-131

## Gaps

- **gap.1** Network rewiring and differential co-occurrence across habitats in microbial data (taxonomic or functional): only Chen2020 is covered, Faust2012 was not obtained, and no cross-biome network comparisons or stress-driven rewiring studies appear.
  blocks: covariation-stability · origin: critic coverage gap; setting: microbial co-occurrence network comparisons across habitats and body sites (soil drought or warming networks, cross-biome network topology, body-site network differences) · from: H2-01:C-100, H2-01:C-101, H2-01:C-102, H2-01:C-103 · src: faustMicrobialCooccurrenceRelationships2012
- **gap.2** Temporal stability of functional covariation beyond one IBD cohort: microbial time series with metagenomes or metatranscriptomes and plant CWM time series were not searched.
  blocks: temporal-covariation · origin: critic coverage gap; setting: longitudinal metagenome and metatranscriptome series (human gut longitudinal cohorts, marine time-series stations); repeated-survey CWM data · from: H2-01:C-104
- **gap.3** Held-out transfer of residual or covariance structure in community ecology: tests of joint species distribution model transferability to new regions or communities, the closest other-field analogue of a withheld habitat.
  blocks: heldout-habitat, other-field-transfer · origin: critic coverage gap; setting: joint species distribution models (HMSC and similar), spatial and temporal transferability tests · from: H2-01:C-105
- **gap.4** Held-out transfer in omics fields beyond bulk transcriptomics.
  blocks: other-field-transfer · origin: critic coverage gap; setting: single-cell reference mapping and latent-space transfer across tissues or species; proteomics and metabolomics covariance transfer · from: H2-01:C-106
- **gap.5** Formal rank estimation on microbiome matrices under compositional transforms (cross-validated NMF or PCA, robust Aitchison PCA, random-matrix thresholds); Raguideau2016, Jiang et al. 2012 (J Math Biol) and Gavish and Donoho were not obtained, and the empirical dependence of rank on p/n is left to Mouillot2021 alone.
  blocks: dimension-estimate, processing-dimension · origin: critic coverage gap; sources not obtained that matter; setting: microbiome compositional PCA and NMF rank selection, sample-size subsampling · from: H2-01:C-107, H2-01:C-108, H2-01:C-109 · src: raguideauInferringAggregatedFunctional2016, jiangNonnegativeMatrixFactorization2011, gavishOptimalHardThreshold2014, johnstoneDistributionLargestEigenvalue2001
- **gap.6** Presence/absence against abundance for sample-level functional profiles; the only presence/absence source is across genomes (Fahimipour2020), not across samples.
  blocks: processing-dimension, genome-dimension · origin: critic coverage gap; setting: gene or KO presence/absence matrices across metagenome samples or MAG collections by habitat · from: H2-01:C-110
- **gap.7** Methodological caution on sequencing approach for composition (16S amplicon against shotgun, and resolution effects on turnover estimates); resolution is discussed only through the Coelho2022 and Sunagawa2015 abstracts.
  blocks: levels-across · origin: critic coverage gap; setting: 16S versus shotgun taxonomic profiling; OTU, ASV and species-level resolution effects on beta diversity · from: H2-01:C-111
- **gap.8** Correction for shared gene-set members in covariance or correlation; only Donato2013 (significance crosstalk, abstract) is cited.
  blocks: gene-set-aggregation · origin: critic coverage gap; setting: gene-set overlap correction methods in expression analysis; pathway-pathway correlation with shared genes · from: H2-01:C-112 · src: donatoAnalysisCorrectionCrosstalk2013
- **gap.9** Case C nearest precedents were not searched: reciprocal transplant and common-garden experiments with microbial communities, single-species pangenomes across hosts or habitats, and synthetic communities across media.
  blocks: taxonomy-fixed · origin: critic coverage gap; unsearched · from: H2-01:C-113
- **gap.10** Held-out tests in non-human habitats: the PICRUSt2 and Tax4Fun2 cross-habitat validations were not obtained, although the answer relies on Langille2013 for the habitat-dependence of transfer.
  blocks: heldout-habitat, neighbouring-transfer · origin: critic coverage gap; sources not obtained that matter; setting: soil, marine and engineered-system functional prediction validation · from: H2-01:C-114 · src: douglasPicrust2PredictionMetagenome2020, wemheuerTax4fun2PredictionHabitatSpecific2020
- **gap.11** Dimension compared by habitat: no route targeted habitat-stratified decompositions, for example the per-biome NMF or PCA in multi-biome metagenome atlases.
  blocks: dimension-estimate.4 · origin: critic coverage gap; "not compared" in the answers · from: H2-01:C-115, H2-01:A-021
- **gap.12** The stage-2 check fired on both arms: write a targeted follow-up brief on the rank-estimation literature and on held-out functional validations outside human habitats, sized separately; the gaps also name cross-habitat network rewiring, temporal covariation series and case C designs.
  blocks: dimension-estimate, heldout-habitat, covariation-stability, temporal-covariation, taxonomy-fixed · origin: a follow-up the note's stage-2 check called for · trail: H2-01 §Stage 2 · from: H2-01:B-0022, H2-01:B-0023, H2-01:B-0024, H2-01:B-0025, H2-01:B-0026, H2-01:B-0027
- **gap.13** Any microbial test withholding a whole habitat when scoring function-function covariation: not found on the routes named.
  blocks: heldout-habitat · origin: "not found" result · from: H2-01:A-047, H2-01:B-0098
- **gap.14** Microbial cross-habitat comparison of covariation stability against level stability and composition stability, and the case where taxonomy does not turn over: not found.
  blocks: covariation-stability, taxonomy-fixed · origin: "not found" result · from: H2-01:A-099, H2-01:A-087, H2-01:B-0150
- **gap.15** The note contradicts itself on access to two cited sources: its "Sources not obtained" list says "Nothing beyond a citation was reachable for these; none supports any claim in the review", yet lists Manor2017 ("DOI from memory, not verified"), which the body re-checked in full text ("I re-checked Manor and Borenstein (2017) [FT]") and uses as load-bearing, and VieiraSilva2016 ("Not reached"), which the body cites as abstract only; the same list gives Lee2025 as "Europe PMC full text read in part".
  blocks: gene-set-aggregation, levels-within.8 · origin: the note contradicts itself (Sources not obtained against the body) · trail: H2-01 §Sources not obtained, §2.3 · from: H2-01:B-0072 · src: manorRevisedComputationalMetagenomic2017, vieirasilvaSpeciesfunctionRelationshipsShape2016, leeFunctionalRegimesDefine2025
- **gap.16** Full text of the load-bearing case B sources was not reached by the synthesis: Fierer2012 and Nelson2016 PMC returns contained only the abstract, and Galand2018's full text could not be reached, so its R² values are not used.
  blocks: levels-across.3, levels-across.10, levels-within.12 · origin: sources not obtained in full that matter · trail: H2-01 §Provenance · from: H2-01:B-0015, H2-01:B-0016, H2-01:C-060, H2-01:C-063
- **gap.17** D1's load-bearing full-text sources were read per search angle and not re-checked by the synthesis: Piton2023 (the only variance-explained figure), Mouillot2021 (the only measured dependence of dimension on feature and sample count), Nayfach2015, HMP2012 and Tian2020.
  blocks: direct-dimension.5, trait-dimension.4 · origin: critic access finding; a check the research still owes · from: H2-01:C-064, H2-01:C-011

## Out of scope

- H2-01:C-044: the critic's overall assessment of the review (provenance)
- H2-01:C-046, H2-01:C-047: the critic's verification record of five sources and their figures (provenance, kept in the result note; trails reach §critic)
- H2-01:C-049: the count of over-reaches, an index to C-050..055, which are accounted for
- H2-01:C-085..099: reference checks and corrections, applied in Sources
- H2-01:C-134..136: the critic's expectation-echo check on the brief's framing (provenance, no finding)
- H2-01:A-022..024: access basis of the D1 answer (provenance; access is in src and Sources)
- H2-01:A-051, H2-01:A-052: access basis of the D2 answer (provenance; access is in src and Sources)
- H2-01:A-065, H2-01:A-066: access basis of the D3 case A answer (provenance; access is in src and Sources)
- H2-01:A-083, H2-01:A-084: access basis of the D3 case B answer (provenance; Nelson2016's label corrected in src and Sources)
- H2-01:A-100, H2-01:A-101: access basis of the D3 case D answer (provenance; access is in src and Sources)
- H2-01:A-025: the heading of the D1 single-source list (its items are accounted for)
- H2-01:A-029: the heading of the D2 answer (the question, not a finding)
- H2-01:A-109: routing to the structured answers (not a finding)

## Sources

```bibtex
@article{airaFasterTurnoverTaxonomic2026,
  author = {Aira, Manuel and Pérez-Losada, Marcos and Crandall, Keith A. and Domínguez, Jorge},
  title = {{Faster turnover of taxonomic over functional bacterial composition during vermicomposting indicates increasing functional redundancy}},
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
  title = {{Ecosystem-wide metagenomic binning enables prediction of ecological niches from genomes}},
  journal = {Communications Biology},
  year = {2020},
  volume = {3},
  pages = {119},
  doi = {10.1038/s42003-020-0856-x},
  note = {access: full_text; cited as: H2-01 [Alneberg2020]}
}

@article{andereggWithinspeciesPatternsChallenge2018,
  author = {Anderegg, Leander D. L. and Berner, Logan T. and Badgley, Grayson and Sethi, Meera L. and Law, Beverly E. and HilleRisLambers, Janneke},
  title = {{Within-species patterns challenge our understanding of the leaf economics spectrum}},
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
  title = {{Exploration of community traits as ecological markers in microbial metagenomes}},
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
  title = {{Contingency, repeatability, and predictability in the evolution of a prokaryotic pangenome}},
  journal = {Proceedings of the National Academy of Sciences of the USA},
  year = {2024},
  volume = {121},
  number = {1},
  pages = {e2304934120},
  doi = {10.1073/pnas.2304934120},
  note = {access: full_text; cited as: H2-01 [Beavan2024]; year 2024 as the note gives it; the note's parenthetical says Crossref issued date 2023, online, volume 121 is 2024; critic H2-01:C-094..096: Crossref gives the issue year as 2024 and the citation is correct}
}

@article{borgySensitivityCommunitylevelTraitenvironment2017,
  author = {Borgy, Benjamin and Violle, Cyrille and Choler, Philippe and Garnier, Eric and Kattge, Jens and Loranger, Jessy and Amiaud, Bernard and Cellier, Pierre and Debarros, Guilhem and Denelle, Pierre and Diquelou, Sylvain and Gachet, Sophie and Jolivet, Claudy and Lavorel, Sandra and Lemauviel-Lavenant, Servane and Mikolajczak, Alexis and Munoz, François and Olivier, Jean and Viovy, Nicolas},
  title = {{Sensitivity of community-level trait-environment relationships to data representativeness: A test for functional biogeography}},
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
  title = {{Global trait-environment relationships of plant communities}},
  journal = {Nature Ecology \& Evolution},
  year = {2018},
  volume = {2},
  number = {12},
  pages = {1906-1917},
  doi = {10.1038/s41559-018-0699-8},
  note = {access: full_text (author-accepted version; author list from Crossref); cited as: H2-01 [Bruelheide2018]; also cited as SEC for a statement it reports (two components explain 74% of six key plant traits)}
}

@article{burkeBacterialCommunityAssembly2011,
  author = {Burke, Catherine and Steinberg, Peter and Rusch, Doug and Kjelleberg, Staffan and Thomas, Torsten},
  title = {{Bacterial community assembly based on functional genes rather than species}},
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
  title = {{Gut microbial co-abundance networks show specificity in inflammatory bowel disease and obesity}},
  journal = {Nature Communications},
  year = {2020},
  volume = {11},
  pages = {4018},
  doi = {10.1038/s41467-020-17840-y},
  note = {access: full_text (re-checked by reviewer); cited as: H2-01 [Chen2020]}
}

@article{chungAssemblingBacterialPuzzles2024,
  author = {Chung, Henri C. and Friedberg, Iddo and Bromberg, Yana},
  title = {{Assembling bacterial puzzles: piecing together functions into microbial pathways}},
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
  title = {{Efficient generation of transcriptomic profiles by random composite measurements}},
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
  title = {{Towards the biogeography of prokaryotic genes}},
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
  title = {{Exploiting single-cell expression to characterize co-expression replicability}},
  journal = {Genome Biology},
  year = {2016},
  volume = {17},
  pages = {101},
  doi = {10.1186/s13059-016-0964-6},
  note = {access: full_text; cited as: H2-01 [Crow2016]}
}

@article{dinsdaleFunctionalMetagenomicProfiling2008,
  author = {Dinsdale, Elizabeth A. and Edwards, Robert A. and Hall, Dana and Angly, Florent and Breitbart, Mya and Brulc, Jennifer M. and Furlan, Mike and Desnues, Christelle and Haynes, Matthew and Li, Linlin and McDaniel, Lauren and Moran, Mary Ann and Nelson, Karen E. and Nilsson, Christina and Olson, Robert and Paul, John and Rodriguez Brito, Beltran and Ruan, Yijun and Swan, Brandon K. and Stevens, Rick and Valentine, David L. and Vega Thurber, Rebecca and Wegley, Linda and White, Bryan A. and Rohwer, Forest},
  title = {{Functional metagenomic profiling of nine biomes}},
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
  title = {{Analysis and correction of crosstalk effects in pathway analysis}},
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
  title = {{Constraints on trait combinations explain climatic drivers of biodiversity: the importance of trait covariance in community assembly}},
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
  title = {{Taxa-function robustness in microbial communities}},
  journal = {Microbiome},
  year = {2018},
  volume = {6},
  pages = {45},
  doi = {10.1186/s40168-018-0425-4},
  note = {access: abstract_only; cited as: H2-01 [EngBorenstein2018]}
}

@article{fahimipourMappingBacterialMetabolic2020a,
  author = {Fahimipour, Ashkaan K. and Gross, Thilo},
  title = {{Mapping the bacterial metabolic niche space}},
  journal = {Nature Communications},
  year = {2020},
  volume = {11},
  pages = {4887},
  doi = {10.1038/s41467-020-18695-z},
  note = {access: full_text; cited as: H2-01 [Fahimipour2020]}
}

@article{fiererCrossbiomeMetagenomicAnalyses2012,
  author = {Fierer, Noah and Leff, Jonathan W. and Adams, Byron J. and Nielsen, Uffe N. and Bates, Scott Thomas and Lauber, Christian L. and Owens, Sarah and Gilbert, Jack A. and Wall, Diana H. and Caporaso, J. Gregory},
  title = {{Cross-biome metagenomic analyses of soil microbial communities and their functional attributes}},
  journal = {Proceedings of the National Academy of Sciences of the USA},
  year = {2012},
  volume = {109},
  number = {52},
  pages = {21390-21395},
  doi = {10.1073/pnas.1215210110},
  note = {access: full_text (per trait-ecology angle; other angles AB; critic H2-01:C-062: read in full text by one angle only and not re-checked by the reviewer); cited as: H2-01 [Fierer2012]}
}

@article{flinkstromMetagenomicClusteringLinks2024,
  author = {Flinkstrom, Zachary and Bryson, Samuel and Candry, Pieter and Winkler, Mari-Karoliina H.},
  title = {{Metagenomic clustering links specific metabolic functions to globally relevant ecosystems}},
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
  title = {{Robustness of trait connections across environmental gradients and growth forms}},
  journal = {Global Ecology and Biogeography},
  year = {2019},
  volume = {28},
  number = {12},
  pages = {1806-1826},
  doi = {10.1111/geb.12996},
  note = {access: full_text (accepted version); cited as: H2-01 [FloresMoreno2019]}
}

@article{friouxEnterosignaturesDefineCommon2023,
  author = {Frioux, Clémence and Ansorge, Rebecca and Özkurt, Ezgi and Ghassemi Nedjad, Chabname and Fritscher, Joachim and Quince, Christopher and Waszak, Sebastian M. and Hildebrand, Falk},
  title = {{Enterosignatures define common bacterial guilds in the human gut microbiome}},
  journal = {Cell Host \& Microbe},
  year = {2023},
  volume = {31},
  number = {7},
  pages = {1111-1125.e6},
  doi = {10.1016/j.chom.2023.05.024},
  note = {access: abstract_only; cited as: H2-01 [Frioux2023]}
}

@article{galandStrongLinkMarine2018,
  author = {Galand, Pierre E. and Pereira, Olivier and Hochart, Corentin and Auguet, Jean Christophe and Debroas, Didier},
  title = {{A strong link between marine microbial community composition and function challenges the idea of functional redundancy}},
  journal = {The ISME Journal},
  year = {2018},
  volume = {12},
  number = {10},
  pages = {2470-2478},
  doi = {10.1038/s41396-018-0158-1},
  note = {access: abstract_only (one angle read an automated page summary only; full-text attempts failed, R2 values not used); cited as: H2-01 [Galand2018]}
}

@article{gianoulisQuantifyingEnvironmentalAdaptation2009,
  author = {Gianoulis, Tara A. and Raes, Jeroen and Patel, Prianka V. and Bjornson, Robert and Korbel, Jan O. and Letunic, Ivica and Yamada, Takuji and Paccanaro, Alberto and Jensen, Lars J. and Snyder, Michael and Bork, Peer and Gerstein, Mark B.},
  title = {{Quantifying environmental adaptation of metabolic pathways in metagenomics}},
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
  title = {{Genomic structure predicts metabolite dynamics in microbial communities}},
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
  title = {{Plant trait networks: improved resolution of the dimensionality of adaptation}},
  journal = {Trends in Ecology \& Evolution},
  year = {2020},
  volume = {35},
  number = {10},
  pages = {908-918},
  doi = {10.1016/j.tree.2020.06.003},
  note = {access: abstract_only; cited as: H2-01 [He2020]; type: review (the note: 'A review')}
}

@article{heimbergLowDimensionalityGene2016,
  author = {Heimberg, Graham and Bhatnagar, Rajat and El-Samad, Hana and Thomson, Matt},
  title = {{Low dimensionality in gene expression data enables the accurate extraction of transcriptional programs from shallow sequencing}},
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
  title = {{Structure, function and diversity of the healthy human microbiome}},
  journal = {Nature},
  year = {2012},
  volume = {486},
  number = {7402},
  pages = {207-214},
  doi = {10.1038/nature11234},
  note = {access: full_text (per metagenomics angle); cited as: H2-01 [HMP2012]}
}

@article{jiangFunctionalBiogeographyOcean2012,
  author = {Jiang, Xingpeng and Langille, Morgan G. I. and Neches, Russell Y. and Elliot, Marie and Levin, Simon A. and Eisen, Jonathan A. and Weitz, Joshua S. and Dushoff, Jonathan},
  title = {{Functional biogeography of ocean microbes revealed through non-negative matrix factorization}},
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
  title = {{Climatic and soil factors explain the two-dimensional spectrum of global plant trait variation}},
  journal = {Nature Ecology \& Evolution},
  year = {2022},
  volume = {6},
  number = {1},
  pages = {36-50},
  doi = {10.1038/s41559-021-01616-8},
  note = {access: full_text; cited as: H2-01 [Joswig2022]; online 2021 (the note); critic H2-01:C-093: no error}
}

@article{konnoMachineLearningEnables2023,
  author = {Konno, Naoki and Iwasaki, Wataru},
  title = {{Machine learning enables prediction of metabolic system evolution in bacteria}},
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
  title = {{Predictive functional profiling of microbial communities using 16S rRNA marker gene sequences}},
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
  title = {{The intrinsic dimensionality of plant traits and its relevance to community assembly}},
  journal = {Journal of Ecology},
  year = {2014},
  volume = {102},
  number = {1},
  pages = {186-193},
  doi = {10.1111/1365-2745.12187},
  note = {access: abstract_only; cited as: H2-01 [Laughlin2014]; online 2013 (the note)}
}

@article{lenzPrincipalComponentsAnalysis2016,
  author = {Lenz, Michael and Müller, Franz-Josef and Zenke, Martin and Schuppert, Andreas},
  title = {{Principal components analysis and the reported low intrinsic dimensionality of gene expression microarray data}},
  journal = {Scientific Reports},
  year = {2016},
  volume = {6},
  pages = {25696},
  doi = {10.1038/srep25696},
  note = {access: full_text; cited as: H2-01 [Lenz2016]}
}

@article{loucaDecouplingFunctionTaxonomy2016,
  author = {Louca, Stilianos and Parfrey, Laura Wegener and Doebeli, Michael},
  title = {{Decoupling function and taxonomy in the global ocean microbiome}},
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
  title = {{High taxonomic variability despite stable functional structure across microbial communities}},
  journal = {Nature Ecology \& Evolution},
  year = {2016},
  volume = {1},
  number = {1},
  pages = {0015},
  doi = {10.1038/s41559-016-0015},
  note = {access: abstract_only; cited as: H2-01 [Louca2016b]}
}

@article{loucaFunctionFunctionalRedundancy2018,
  author = {Louca, Stilianos and Polz, Martin F. and Mazel, Florent and Albright, Michaeline B. N. and Huber, Julie A. and O'Connor, Mary I. and Ackermann, Martin and Hahn, Aria S. and Srivastava, Diane S. and Crowe, Sean A. and Doebeli, Michael and Parfrey, Laura Wegener},
  title = {{Function and functional redundancy in microbial systems}},
  journal = {Nature Ecology \& Evolution},
  year = {2018},
  volume = {2},
  number = {6},
  pages = {936-943},
  doi = {10.1038/s41559-018-0519-1},
  note = {access: abstract_only (review, asserted; cited only for its position that redundancy is general); cited as: H2-01 [Louca2018]; type: review; not cited (in the reference list, cited nowhere in the body or answers)}
}

@article{lovellProportionalityValidAlternative2015,
  author = {Lovell, David and Pawlowsky-Glahn, Vera and Egozcue, Juan José and Marguerat, Samuel and Bähler, Jürg},
  title = {{Proportionality: a valid alternative to correlation for relative data}},
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
  title = {{MUSiCC: a marker genes based framework for metagenomic normalization and accurate profiling of gene abundances in the microbiome}},
  journal = {Genome Biology},
  year = {2015},
  volume = {16},
  pages = {53},
  doi = {10.1186/s13059-015-0610-8},
  note = {access: full_text; cited as: H2-01 [Manor2015]}
}

@article{manorRevisedComputationalMetagenomic2017,
  author = {Manor, Ohad and Borenstein, Elhanan},
  title = {{Revised computational metagenomic processing uncovers hidden and biologically meaningful functional variation in the human microbiome}},
  journal = {Microbiome},
  year = {2017},
  volume = {5},
  pages = {19},
  doi = {10.1186/s40168-017-0231-4},
  note = {access: full_text (re-checked by reviewer); cited as: H2-01 [Manor2017]; conflict: the note also lists this work under Sources not obtained ('DOI from memory, not verified'; routes tried: Europe PMC keyword search (no hit returned in top results); PubMed not queried by exact title; WebSearch budget exhausted), where it says none of those sources supports any claim}
}

@article{messierTraitVariationIntegration2016,
  author = {Messier, Julie and McGill, Brian J. and Enquist, Brian J. and Lechowicz, Martin J.},
  title = {{Trait variation and integration across scales: is the leaf economic spectrum present at local scales?}},
  journal = {Ecography},
  year = {2017},
  volume = {40},
  number = {6},
  pages = {685-697},
  doi = {10.1111/ecog.02006},
  note = {access: abstract_only; cited as: H2-01 [Messier2017]; online 2016 (the note)}
}

@article{mouillotDimensionalityStructureSpecies2021,
  author = {Mouillot, David and Loiseau, Nicolas and Grenié, Matthias and Algar, Adam C. and Allegra, Michele and Cadotte, Marc W. and Casajus, Nicolas and Denelle, Pierre and Guéguen, Maya and Maire, Anthony and Maitner, Brian and McGill, Brian J. and McLean, Matthew and Mouquet, Nicolas and Munoz, François and Thuiller, Wilfried and Villéger, Sébastien and Violle, Cyrille and Auber, Arnaud},
  title = {{The dimensionality and structure of species trait spaces}},
  journal = {Ecology Letters},
  year = {2021},
  volume = {24},
  number = {9},
  pages = {1988-2009},
  doi = {10.1111/ele.13778},
  note = {access: full_text (Archimer author version); cited as: H2-01 [Mouillot2021]}
}

@article{nayfachAverageGenomeSize2015,
  author = {Nayfach, Stephen and Pollard, Katherine S.},
  title = {{Average genome size estimation improves comparative metagenomics and sheds light on the functional ecology of the human microbiome}},
  journal = {Genome Biology},
  year = {2015},
  volume = {16},
  pages = {51},
  doi = {10.1186/s13059-015-0611-7},
  note = {access: full_text (per metagenomics angle); cited as: H2-01 [Nayfach2015]}
}

@article{nelsonGlobalBiogeographyMicrobial2016,
  author = {Nelson, Michaeline B. and Martiny, Adam C. and Martiny, Jennifer B. H.},
  title = {{Global biogeography of microbial nitrogen-cycling traits in soil}},
  journal = {Proceedings of the National Academy of Sciences of the USA},
  year = {2016},
  volume = {113},
  number = {29},
  pages = {8033-8040},
  doi = {10.1073/pnas.1601070113},
  note = {access: secondary (critic: H2-01:C-059; the note said full_text via automated summary of the PMC page; figures not re-verified); cited as: H2-01 [Nelson2016]}
}

@article{peresnetoLinkingTraitVariation2017,
  author = {Peres-Neto, Pedro R. and Dray, Stéphane and ter Braak, Cajo J. F.},
  title = {{Linking trait variation to the environment: critical issues with community-weighted mean correlation resolved by the fourth-corner approach}},
  journal = {Ecography},
  year = {2017},
  volume = {40},
  number = {7},
  pages = {806-816},
  doi = {10.1111/ecog.02302},
  note = {access: abstract_only; cited as: H2-01 [PeresNeto2017]}
}

@article{piersonSharingSpecificityCoexpression2015,
  author = {Pierson, Emma and {the GTEx Consortium} and Koller, Daphne and Battle, Alexis and Mostafavi, Sara},
  title = {{Sharing and specificity of co-expression networks across 35 human tissues}},
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
  title = {{Life history strategies of soil bacterial communities across global terrestrial biomes}},
  journal = {Nature Microbiology},
  year = {2023},
  volume = {8},
  number = {11},
  pages = {2093-2102},
  doi = {10.1038/s41564-023-01465-0},
  note = {access: full_text (eScholarship author version, per trait-ecology angle); cited as: H2-01 [Piton2023]}
}

@article{raesTowardMolecularTraitbased2011,
  author = {Raes, Jeroen and Letunic, Ivica and Yamada, Takuji and Jensen, Lars Juhl and Bork, Peer},
  title = {{Toward molecular trait-based ecology through integration of biogeochemical, geographical and metagenomic data}},
  journal = {Molecular Systems Biology},
  year = {2011},
  volume = {7},
  pages = {473},
  doi = {10.1038/msb.2011.6},
  note = {access: full_text; cited as: H2-01 [Raes2011]; critic H2-01:C-092: Crossref gives the article number as MSB20116; 473 is the journal's published article number}
}

@article{ramirezflandesRedoxTraitsCharacterize2019,
  author = {Ramírez-Flandes, Salvador and González, Bernardo and Ulloa, Osvaldo},
  title = {{Redox traits characterize the organization of global microbial communities}},
  journal = {Proceedings of the National Academy of Sciences of the USA},
  year = {2019},
  volume = {116},
  number = {9},
  pages = {3630-3635},
  doi = {10.1073/pnas.1817554116},
  note = {access: full_text; cited as: H2-01 [RamirezFlandes2019]}
}

@article{salazarGeneExpressionChanges2019,
  author = {Salazar, Guillem and Paoli, Lucas and Alberti, Adriana and Huerta-Cepas, Jaime and Ruscheweyh, Hans-Joachim and Cuenca, Miguelangel and Field, Christopher M. and Coelho, Luis Pedro and Cruaud, Corinne and Engelen, Stefan and Gregory, Ann C. and Labadie, Karine and Marec, Claudie and Pelletier, Eric and Royo-Llonch, Marta and Roux, Simon and Sánchez, Pablo and Uehara, Hideya and Zayed, Ahmed A. and Zeller, Georg and Carmichael, Margaux and Dimier, Céline and Ferland, Joannie and Kandels, Stefanie and Picheral, Marc and Pisarev, Sergey and Poulain, Julie and {Tara Oceans Coordinators} and Acinas, Silvia G. and Babin, Marcel and Bork, Peer and Bowler, Chris and de Vargas, Colomban and Guidi, Lionel and Hingamp, Pascal and Iudicone, Daniele and Karp-Boss, Lee and Karsenti, Eric and Ogata, Hiroyuki and Pesant, Stephane and Speich, Sabrina and Sullivan, Matthew B. and Wincker, Patrick and Sunagawa, Shinichi and others},
  title = {{Gene expression changes and community turnover differentially shape the global ocean metatranscriptome}},
  journal = {Cell},
  year = {2019},
  volume = {179},
  number = {5},
  pages = {1068-1083.e21},
  doi = {10.1016/j.cell.2019.10.014},
  note = {access: full_text; cited as: H2-01 [Salazar2019]; incomplete: author (critic H2-01:C-089..091: Crossref lists 71 author entries, including coordinator members; the list here is the note's, shorter)}
}

@article{schrodtScpBHPMFScp2015,
  author = {Schrodt, Franziska and Kattge, Jens and Shan, Hanhuai and Fazayeli, Farideh and Joswig, Julia and Banerjee, Arindam and Reichstein, Markus and Bönisch, Gerhard and Díaz, Sandra and Dickie, John and Gillison, Andy and Karpatne, Anuj and Lavorel, Sandra and Leadley, Paul and Wirth, Christian B. and Wright, Ian J. and Wright, S. Joseph and Reich, Peter B.},
  title = {{BHPMF: a hierarchical Bayesian approach to gap-filling and trait prediction for macroecology and functional biogeography}},
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
  title = {{Annotation-free discovery of functional groups in microbial communities}},
  journal = {Nature Ecology \& Evolution},
  year = {2023},
  volume = {7},
  number = {5},
  pages = {716-724},
  doi = {10.1038/s41559-023-02021-z},
  note = {access: abstract_only; cited as: H2-01 [Shan2023]}
}

@article{steinobrienDecomposingCellIdentity2019,
  author = {Stein-O'Brien, Genevieve L. and Clark, Brian S. and Sherman, Thomas and Zibetti, Cristina and Hu, Qiwen and Sealfon, Rachel and Liu, Sheng and Qian, Jiang and Colantuoni, Carlo and Blackshaw, Seth and Goff, Loyal A. and Fertig, Elana J.},
  title = {{Decomposing cell identity for transfer learning across cellular measurements, platforms, tissues, and species}},
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
  title = {{A next generation connectivity map: L1000 platform and the first 1,000,000 profiles}},
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
  title = {{Inference-based accuracy of metagenome prediction tools varies across sample types and functional categories}},
  journal = {Microbiome},
  year = {2020},
  volume = {8},
  pages = {46},
  doi = {10.1186/s40168-020-00815-y},
  note = {access: full_text; cited as: H2-01 [Sun2020]}
}

@article{sunagawaStructureFunctionGlobal2015,
  author = {Sunagawa, Shinichi and Coelho, Luis Pedro and Chaffron, Samuel and Kultima, Jens Roat and Labadie, Karine and Salazar, Guillem and Djahanschiri, Bardya and Zeller, Georg and Mende, Daniel R. and Alberti, Adriana and Cornejo-Castillo, Francisco M. and Costea, Paul I. and Cruaud, Corinne and d'Ovidio, Francesco and Engelen, Stefan and Ferrera, Isabel and Gasol, Josep M. and Guidi, Lionel and Hildebrand, Falk and Kokoszka, Florian and Lepoivre, Cyrille and Lima-Mendez, Gipsi and Poulain, Julie and Poulos, Bonnie T. and Royo-Llonch, Marta and Sarmento, Hugo and Vieira-Silva, Sara and Dimier, Céline and Picheral, Marc and Searson, Sarah and Kandels-Lewis, Stefanie and {Tara Oceans coordinators} and Bowler, Chris and de Vargas, Colomban and Gorsky, Gabriel and Grimsley, Nigel and Hingamp, Pascal and Iudicone, Daniele and Jaillon, Olivier and Not, Fabrice and Ogata, Hiroyuki and Pesant, Stephane and Speich, Sabrina and Stemmann, Lars and Sullivan, Matthew B. and Weissenbach, Jean and Wincker, Patrick and Karsenti, Eric and Raes, Jeroen and Acinas, Silvia G. and Bork, Peer and others},
  title = {{Structure and function of the global ocean microbiome}},
  journal = {Science},
  year = {2015},
  volume = {348},
  number = {6237},
  pages = {1261359},
  doi = {10.1126/science.1261359},
  note = {access: abstract_only; cited as: H2-01 [Sunagawa2015]; incomplete: author (critic H2-01:C-085..088: Crossref lists 60 authors; the list here is the note's 51, ending at Bork; omitted after Bork: Boss, Bowler (second entry), Follows, Karp-Boss, Krzic, Reynaud, Sardet, Sieracki, Velayoudon; the last author in the registry is Velayoudon, Didier)}
}

@article{tianDecipheringFunctionalRedundancy2020,
  author = {Tian, Liang and Wang, Xu-Wen and Wu, Ang-Kun and Fan, Yuhang and Friedman, Jonathan and Dahlin, Amber and Waldor, Matthew K. and Weinstock, George M. and Weiss, Scott T. and Liu, Yang-Yu},
  title = {{Deciphering functional redundancy in the human microbiome}},
  journal = {Nature Communications},
  year = {2020},
  volume = {11},
  pages = {6217},
  doi = {10.1038/s41467-020-19940-1},
  note = {access: full_text (per statistics angle); cited as: H2-01 [Tian2020]}
}

@article{taroniMultiPLIERTransferLearning2019,
  author = {Taroni, Jaclyn N. and Grayson, Peter C. and Hu, Qiwen and Eddy, Sean and Kretzler, Matthias and Merkel, Peter A. and Greene, Casey S.},
  title = {{MultiPLIER: a transfer learning framework for transcriptomics reveals systemic features of rare disease}},
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
  title = {{Species-function relationships shape ecological properties of the human gut microbiome}},
  journal = {Nature Microbiology},
  year = {2016},
  volume = {1},
  number = {8},
  pages = {16088},
  doi = {10.1038/nmicrobiol.2016.88},
  note = {access: abstract_only; cited as: H2-01 [VieiraSilva2016]; conflict: the note also lists this work under Sources not obtained ('from memory, not verified'; routes tried: not reached; search APIs rate-limited), where it says none of those sources supports any claim}
}

@article{westobyTraitDimensionsBacteria2021,
  author = {Westoby, Mark and Gillings, Michael R. and Madin, Joshua S. and Nielsen, Daniel A. and Paulsen, Ian T. and Tetu, Sasha G.},
  title = {{Trait dimensions in bacteria and archaea compared to vascular plants}},
  journal = {Ecology Letters},
  year = {2021},
  volume = {24},
  number = {7},
  pages = {1487-1504},
  doi = {10.1111/ele.13742},
  note = {access: abstract_only; cited as: H2-01 [Westoby2021]; type: review (the note: 'A review')}
}

@article{wieczynskiClimateShapesShifts2018,
  author = {Wieczynski, Daniel J. and Boyle, Brad and Buzzard, Vanessa and Duran, Sandra M. and Henderson, Amanda N. and Hulshof, Catherine M. and Kerkhoff, Andrew J. and McCarthy, Megan C. and Michaletz, Sean T. and Swenson, Nathan G. and Asner, Gregory P. and Bentley, Lisa Patrick and Enquist, Brian J. and Savage, Van M.},
  title = {{Climate shapes and shifts functional biodiversity in forests worldwide}},
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
  title = {{Meta-analysis of fecal metagenomes reveals global microbial signatures that are specific for colorectal cancer}},
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
  title = {{Modulation of leaf economic traits and trait relationships by climate}},
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
  title = {{A global relationship between genome size and encoded carbon metabolic strategies of soil bacteria}},
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
  title = {{A parsimony approach to biological pathway reconstruction/inference for genomes and metagenomes}},
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
  title = {{Which results of the standard test for community-weighted mean approach are too optimistic?}},
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
  title = {{PICRUSt2 for prediction of metagenome functions}},
  journal = {Nature Biotechnology},
  year = {2020},
  volume = {38},
  pages = {685-688},
  doi = {10.1038/s41587-020-0548-6},
  note = {access: not_obtained (routes tried: PubMed XML abstract fetch returned no abstract text in the output; full text not attempted (PMC7365738 available)); cited as: H2-01 Sources not obtained; incomplete: author}
}

@article{wemheuerTax4fun2PredictionHabitatSpecific2020,
  author = {Wemheuer, F. and others},
  title = {{Tax4Fun2: prediction of habitat-specific functional profiles and functional redundancy based on 16S rRNA gene sequences}},
  journal = {Environmental Microbiome},
  year = {2020},
  volume = {15},
  pages = {11},
  doi = {10.1186/s40793-020-00358-7},
  note = {access: not_obtained (routes tried: found in Europe PMC search listing only; not opened); cited as: H2-01 Sources not obtained (listed twice); incomplete: author}
}

@article{lloydpriceStrainsFunctionsDynamics2017,
  author = {Lloyd-Price, J. and others},
  title = {{Strains, functions and dynamics in the expanded Human Microbiome Project}},
  journal = {Nature},
  year = {2017},
  volume = {550},
  pages = {61-66},
  doi = {10.1038/nature23889},
  note = {access: not_obtained (routes tried: Crossref metadata only); cited as: H2-01 Sources not obtained; incomplete: author}
}

@article{leeFunctionalRegimesDefine2025,
  author = {Lee, K. K. and others},
  title = {{Functional regimes define soil microbiome response to environmental change}},
  journal = {Nature},
  year = {2025},
  volume = {644},
  pages = {1028-1038},
  doi = {10.1038/s41586-025-09264-9},
  note = {access: not_obtained (routes tried: Europe PMC full text read in part (PMC12390847)); cited as: H2-01 Sources not obtained; conflict: listed under Sources not obtained, which says nothing beyond a citation was reachable, yet its routes say the full text was read in part; incomplete: author}
}

@article{jiangNonnegativeMatrixFactorization2011,
  author = {Jiang, X. and Weitz, J. S. and Dushoff, J.},
  title = {{A non-negative matrix factorization framework for identifying modular patterns in metagenomic profile data}},
  journal = {Journal of Mathematical Biology},
  year = {2012},
  volume = {64},
  pages = {697-711},
  doi = {10.1007/s00285-011-0428-2},
  note = {access: not_obtained (routes tried: Europe PMC listing only; no OA full text located); cited as: H2-01 Sources not obtained; Stage 2 check and critic coverage gap name it}
}

@article{raguideauInferringAggregatedFunctional2016,
  author = {Raguideau, S. and others},
  title = {{Inferring aggregated functional traits from metagenomic data using constrained non-negative matrix factorization}},
  journal = {PLoS Computational Biology},
  year = {2016},
  volume = {12},
  number = {12},
  pages = {e1005252},
  doi = {10.1371/journal.pcbi.1005252},
  note = {access: not_obtained (routes tried: Europe PMC listing only; not opened owing to time); cited as: H2-01 Sources not obtained; incomplete: author}
}

@article{chuckranEdaphicControlsGenome2023,
  author = {Chuckran, P. F. and Flagg, C. and Propster, J. and Rutherford, W. A. and Sieradzki, E. T. and Blazewicz, S. J. and Hungate, B. and Pett-Ridge, J. and Schwartz, E. and Dijkstra, P.},
  title = {{Edaphic controls on genome size and GC content of bacteria in soil microbial communities}},
  journal = {Soil Biology and Biochemistry},
  year = {2023},
  volume = {178},
  pages = {108935},
  doi = {10.1016/j.soilbio.2022.108935},
  note = {access: not_obtained (routes tried: Crossref (metadata only), OpenAlex (no abstract returned); bioRxiv preprint 10.1101/2021.11.17.469016 identified but not read); cited as: H2-01 Sources not obtained (listed twice)}
}

@article{malikDefiningTraitbasedMicrobial2019,
  author = {Malik, A. A. and Martiny, J. B. H. and Brodie, E. L. and Martiny, A. C. and Treseder, K. K. and Allison, S. D.},
  title = {{Defining trait-based microbial strategies with consequences for soil carbon cycling under climate change}},
  journal = {The ISME Journal},
  year = {2020},
  volume = {14},
  number = {1},
  pages = {1-9},
  doi = {10.1038/s41396-019-0510-0},
  note = {access: not_obtained (routes tried: Crossref metadata only; not fetched); cited as: H2-01 Sources not obtained (listed twice)}
}

@article{madinSynthesisBacterialArchaeal2020,
  author = {Madin, J. S. and others},
  title = {{A synthesis of bacterial and archaeal phenotypic trait data}},
  journal = {Scientific Data},
  year = {2020},
  volume = {7},
  pages = {170},
  doi = {10.1038/s41597-020-0497-4},
  note = {access: not_obtained (routes tried: Crossref metadata only; not read); cited as: H2-01 Sources not obtained (listed twice); incomplete: author}
}

@article{maynardGlobalRelationshipsTree2022,
  author = {Maynard and others},
  title = {{Global relationships in tree functional traits}},
  journal = {Nature Communications},
  year = {2022},
  note = {access: not_obtained (routes tried: Crossref bibliographic query returned a different paper; DOI not confirmed); cited as: H2-01 Sources not obtained (listed twice); incomplete: author, volume, pages, doi (critic H2-01:C-099: no DOI and incomplete, not checked)}
}

@article{johnstoneDistributionLargestEigenvalue2001,
  author = {Johnstone, Iain M.},
  title = {{On the distribution of the largest eigenvalue in principal components analysis}},
  journal = {The Annals of Statistics},
  year = {2001},
  volume = {29},
  number = {2},
  pages = {295-327},
  doi = {10.1214/aos/1009210544},
  note = {access: not_obtained (routes tried: Crossref metadata only (DOI confirmed); body and abstract not retrieved; WebSearch budget exhausted; Europe PMC and PubMed do not index it); cited as: H2-01 Sources not obtained (listed twice), Stage 2 check}
}

@article{gavishOptimalHardThreshold2014,
  author = {Gavish, Matan and Donoho, David L.},
  title = {{The Optimal Hard Threshold for Singular Values is 4/sqrt(3)}},
  journal = {IEEE Transactions on Information Theory},
  year = {2014},
  volume = {60},
  number = {8},
  pages = {5040-5053},
  doi = {10.1109/TIT.2014.2323359},
  note = {access: not_obtained (routes tried: Crossref metadata only (DOI confirmed; no abstract in record); WebSearch unavailable; arXiv not queried); cited as: H2-01 Sources not obtained (listed twice), Stage 2 check, critic coverage gap}
}

@article{royaltyContributionEvennessFunctional2020,
  author = {Royalty, Taylor M. and Steen, Andrew D.},
  title = {{Contribution Evenness: A functional redundancy metric sensitive to trait stability in microbial communities}},
  journal = {bioRxiv},
  year = {2020},
  doi = {10.1101/2020.04.22.054593},
  note = {access: not_obtained (routes tried: Europe PMC abstract retrieved; full text not fetched; judged peripheral (redundancy metric, not covariation)); type: preprint; cited as: H2-01 Sources not obtained}
}

@article{faustMicrobialCooccurrenceRelationships2012,
  author = {Faust, Karoline and Sathirapongsasuti, J. Fah and Izard, Jacques and Segata, Nicola and Gevers, Dirk and Raes, Jeroen and Huttenhower, Curtis},
  title = {{Microbial co-occurrence relationships in the human microbiome}},
  journal = {PLoS Computational Biology},
  year = {2012},
  volume = {8},
  number = {7},
  pages = {e1002606},
  doi = {10.1371/journal.pcbi.1002606},
  note = {access: not_obtained (from memory, not verified; routes tried: not searched directly after Europe PMC returned 503 errors and OpenAlex and Semantic Scholar rate-limited); cited as: H2-01 Sources not obtained (listed twice), critic coverage gap}
}

@article{langfelderMyNetworkModule2011,
  author = {Langfelder, P. and others},
  title = {{Is my network module preserved and reproducible?}},
  journal = {PLoS Computational Biology},
  year = {2011},
  volume = {7},
  pages = {e1001057},
  doi = {10.1371/journal.pcbi.1001057},
  note = {access: not_obtained (routes tried: metadata only (trait-ecology angle); outside that angle); cited as: H2-01 Sources not obtained; incomplete: author}
}

@article{bahramStructureFunctionGlobal2018,
  author = {Bahram and others},
  journal = {Nature},
  year = {2018},
  volume = {560},
  number = {7717},
  pages = {233-237},
  doi = {10.1038/s41586-018-0386-6},
  note = {access: abstract_only; not cited (reported by the search angles but not used in the body: peripheral or superseded); incomplete: author, title}
}

@article{lepsCommunityTraitResponse2011,
  author = {Lep{\v{s}} and others},
  journal = {Ecography},
  year = {2011},
  volume = {34},
  number = {5},
  pages = {856-863},
  doi = {10.1111/j.1600-0587.2010.06904.x},
  note = {access: abstract_only; not cited (reported by the search angles but not used in the body: peripheral or superseded); incomplete: author, title}
}

@article{nemergutDecreasesAverageBacterial2015,
  author = {Nemergut and others},
  journal = {The ISME Journal},
  year = {2016},
  volume = {10},
  number = {5},
  pages = {1147-1156},
  doi = {10.1038/ismej.2015.191},
  note = {access: abstract_only; not cited (reported by the search angles but not used in the body: peripheral or superseded); incomplete: author, title}
}

@article{fiererSeeingForestGenes2014,
  author = {Fierer and Barber{\'a}n and Laughlin},
  journal = {Frontiers in Microbiology},
  year = {2014},
  volume = {5},
  pages = {614},
  doi = {10.3389/fmicb.2014.00614},
  note = {access: abstract_only (asserted); not cited (reported by the search angles but not used in the body: peripheral or superseded); incomplete: author given names, title}
}

@article{brbicLandscapeMicrobialPhenotypic2016,
  author = {Brbi{\'c} and others},
  journal = {Nucleic Acids Research},
  year = {2016},
  volume = {44},
  number = {21},
  pages = {10074-10090},
  doi = {10.1093/nar/gkw964},
  note = {access: abstract_only (volume and pages from the search agent, the Crossref record lists only an article ID); not cited (reported by the search angles but not used in the body: peripheral or superseded); incomplete: author, title; critic H2-01:C-099: not checked}
}

@article{jolliffePrincipalComponentAnalysis2016,
  author = {Jolliffe, Ian T. and Cadima, Jorge},
  title = {{Principal component analysis: a review and recent developments}},
  journal = {Philosophical Transactions of the Royal Society A: Mathematical, Physical and Engineering Sciences},
  year = {2016},
  volume = {374},
  number = {2065},
  pages = {20150202},
  doi = {10.1098/rsta.2015.0202},
  note = {background; type: review; looked up on Crossref for the background entry dimension-estimate.bg1}
}

@article{gloorMicrobiomeDatasetsCompositional2017,
  author = {Gloor, Gregory B. and Macklaim, Jean M. and Pawlowsky-Glahn, Vera and Egozcue, Juan J.},
  title = {{Microbiome Datasets Are Compositional: And This Is Not Optional}},
  journal = {Frontiers in Microbiology},
  year = {2017},
  volume = {8},
  pages = {2224},
  doi = {10.3389/fmicb.2017.02224},
  note = {background; type: review; looked up on Crossref and Europe PMC for the background entry compositional-closure.bg1}
}

@article{garnierPlantFunctionalMarkers2004,
  author = {Garnier, Eric and Cortez, Jacques and Bill{\`e}s, Georges and Navas, Marie-Laure and Roumet, Catherine and Debussche, Max and Laurent, G{\'e}rard and Blanchard, Alain and Aubry, David and Bellmann, Astrid and Neill, Cathy and Toussaint, Jean-Patrick},
  title = {{Plant functional markers capture ecosystem properties during secondary succession}},
  journal = {Ecology},
  year = {2004},
  volume = {85},
  number = {9},
  pages = {2630-2637},
  doi = {10.1890/03-0799},
  note = {background; looked up on Crossref and OpenAlex for the background entry cwm.bg1}
}
```
