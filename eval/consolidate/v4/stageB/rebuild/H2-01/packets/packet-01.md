## evidence-bodies.1 (claim)

Three bodies of work bear on the questions: metagenomics supplies sample-by-function matrices (KEGG orthologues, pathways, modules, Pfams, eggNOG groups) from shotgun data; trait ecology supplies community-weighted means (CWMs) and species-by-trait matrices, mostly from plants; and other fields that profile many correlated features, chiefly transcriptomics, supply most of the explicit held-out tests of learned covariation.

- conf: not stated
- class: not stated
- holds: the review's account of the literature it covered
- src: none (the reviewer's account of the literature)
- trail: H2-01 §1. What

From the note:

> H2-01:B-0028 [1. What the literature covers, and what it does not] Three bodies of work bear on the brief.
>
> H2-01:B-0029 [1. What the literature covers, and what it does not] Metagenomics supplies sample-by-function matrices (KEGG orthologues, pathways, modules, Pfams, eggNOG groups) from shotgun data.
>
> H2-01:B-0030 [1. What the literature covers, and what it does not] Trait ecology supplies community-weighted means (CWMs) and species-by-trait matrices, mostly from plants.
>
> H2-01:B-0031 [1. What the literature covers, and what it does not] Other fields that profile many correlated features, chiefly transcriptomics, supply most of the explicit held-out tests of learned covariation.
>

Not found in the cited text (where to look, not what is wrong): holds: review

## evidence-bodies.2 (claim)

The three bodies have asked different questions: metagenomics has mostly compared levels of functions with taxonomic composition; trait ecology has asked about the dimensionality and covariation of traits, and sometimes how covariation shifts along gradients; transcriptomics has asked whether covariation learned in one tissue or study reproduces another.

- conf: not stated
- class: not stated
- holds: the review's account of the literature it covered
- src: none (the reviewer's account of the literature)
- trail: H2-01 §1. What

From the note:

> H2-01:B-0032 [1. What the literature covers, and what it does not] The three have asked different questions.
>
> H2-01:B-0033 [1. What the literature covers, and what it does not] Metagenomics has mostly compared *levels* of functions with *taxonomic composition*.
>
> H2-01:B-0034 [1. What the literature covers, and what it does not] Trait ecology has asked about the *dimensionality* and *covariation* of traits, and sometimes how covariation shifts along gradients.
>
> H2-01:B-0035 [1. What the literature covers, and what it does not] Transcriptomics has asked whether covariation learned in one tissue or study reproduces another.
>

Not found in the cited text (where to look, not what is wrong): holds: review

## evidence-bodies.3 (claim)

The core cases of the questions are thinly covered: most of the evidence is either direct evidence on a neighbouring quantity or evidence from another field, and each is labelled as such.

- conf: not stated
- class: not stated
- holds: the review's account of the literature it covered
- src: none (the reviewer's account of the literature)
- trail: H2-01 §1. What

From the note:

> H2-01:B-0036 [1. What the literature covers, and what it does not] The core cases of the brief are thinly covered.
>
> H2-01:B-0040 [1. What the literature covers, and what it does not] Most of what follows is therefore either (a) direct evidence on a neighbouring quantity, or (b) evidence from another field.
>
> H2-01:B-0041 [1. What the literature covers, and what it does not] Each is labelled.
>

Not found in the cited text (where to look, not what is wrong): holds: review

## evidence-bodies.4 (claim)

A second reader judged the review careful on the whole: it labels most indirect evidence and keeps the core microbial cases (withheld habitat, cross-habitat covariation stability, case C) as not found.

- conf: not stated
- class: not stated
- holds: the critic's overall assessment of the review
- src: none (the critic's assessment)
- trail: H2-01 §critic

From the note:

> H2-01:C-044 [danger: Critic: answers partly supported] The review is careful on the whole.
>
> H2-01:C-045 [danger: Critic: answers partly supported] It labels most indirect evidence and keeps the core microbial cases (withheld habitat, cross-habitat covariation stability, case C) as not found.
>

## shared-mean-profile.1 (claim)

Per-sample Spearman correlations between predicted and measured KEGG gene profiles (0.53 to 0.87) barely changed when each gene's abundance was permuted across samples (soil example: 0.85 unpermuted, 0.84 permuted); the authors conclude that functional profiles vary little between samples relative to their mean.

- conf: not stated
- class: meas (marker)
- holds: a per-sample prediction-accuracy metric for predicted against measured KEGG gene profiles; the critic: not a decomposition that measures how much of a sample-by-function matrix is a mean profile, and from human-associated and a few soil datasets
- src: sunInferenceBasedAccuracyMetagenome2020 (FT; measured)
- trail: H2-01 §2.2, §critic

From the note:

> H2-01:I-0006 [2.2 A dominant mean profile] First, per-sample Spearman correlations between predicted and measured KEGG gene profiles (0.53 to 0.87) barely changed when each gene's abundance was permuted across samples (soil example: 0.85 unpermuted, 0.84 permuted) [Sun2020; FT; measured].
>
> H2-01:B-0061 [2.2 A dominant mean profile] The authors conclude that functional profiles vary little between samples relative to their mean.
>
> H2-01:C-003 [danger: Critic: answers partly supported] Sun2020 shows that a per-sample prediction-accuracy metric barely changes when genes are permuted across samples.
>
> H2-01:C-005 [danger: Critic: answers partly supported] Neither is a decomposition that measures how much of a sample-by-function matrix is a mean profile, and both come from human-associated and a few soil datasets.
>

## shared-mean-profile.2 (claim)

The Human Microbiome Project consortium reports pathway relative abundances "much more constant and evenly diverse" than organismal abundances across individuals within body sites, with a stable housekeeping core.

- conf: not stated
- class: meas (marker)
- holds: human body sites (HMP); the critic: "much more constant" is a quoted descriptive statement with no quantitative figure, which the review treats as measured evidence of equal weight
- src: theStructureFunctionDiversity2012 (FT; measured)
- trail: H2-01 §2.2, §4.1, §critic, §Adversarial

From the note:

> H2-01:I-0007 [2.2 A dominant mean profile] Second, the HMP consortium reports pathway relative abundances "much more constant and evenly diverse" than organismal abundances, with a stable housekeeping core [HMP2012; FT; measured].
>
> H2-01:I-0027 [4.1 Function levels against taxonomic composition, habitat held roughly constant, taxonomy turns over] - HMP: pathway relative abundances "much more constant" than organismal abundances across individuals within body sites [HMP2012; FT; measured].
>
> H2-01:C-004 [danger: Critic: answers partly supported] HMP2012 reports that pathway levels vary less than taxa in the human body.
>
> H2-01:C-022 [danger: Critic: answers partly supported] Two are full text (HMP2012, Burke2011); three rest on abstracts (Louca2016b, Shan2023, Aira2026).
>
> H2-01:C-069 [warning: Adversarial critique, full findings] - HMP2012's 'much more constant' is a quoted descriptive statement. The review gives no quantitative figure, yet D3 case A treats it as measured evidence of equal weight.
>

Not found in the cited text (where to look, not what is wrong): Microbiome; Project

## shared-mean-profile.3 (claim)

In a reference network of 796 human-associated genomes by 7,105 KOs, a nested structure, with many KOs carried by most genomes, makes community functional profiles conserved even when taxa vary.

- conf: single (marker)
- class: deriv/model (marker)
- holds: a genome-content network model of human-associated genomes, offered as a mechanistic account
- src: tianDecipheringFunctionalRedundancy2020 (FT; derived/modelled; SINGLE SOURCE)
- trail: H2-01 §2.2, §answers

From the note:

> H2-01:B-0062 [2.2 A dominant mean profile] A mechanistic account comes from a reference network of 796 human-associated genomes by 7,105 KOs.
>
> H2-01:I-0008 [2.2 A dominant mean profile] Its nested structure, with many KOs carried by most genomes, makes community functional profiles conserved even when taxa vary [Tian2020; FT; derived/modelled; SINGLE SOURCE].
>
> H2-01:A-056 [quote: Answers as delivered] A genome-content network model gives a reason (many functions carried by most genomes [Tian2020]).
>

## shared-mean-profile.4 (claim)

The review reads two findings (the permutation result for a per-sample accuracy metric and the HMP statement that pathways are more constant than taxa) as suggesting that much of the apparent low dimensionality of raw functional profiles is a shared mean; the critic holds that they support only this: in these datasets, per-sample functional profiles are highly similar to one another.

- conf: not stated
- class: not stated
- holds: human-associated and a few soil datasets; neither finding is a decomposition that measures how much of a sample-by-function matrix is a mean profile
- src: sunInferenceBasedAccuracyMetagenome2020, theStructureFunctionDiversity2012
- trail: H2-01 §2.2, §critic

From the note:

> H2-01:B-0060 [2.2 A dominant mean profile] Two findings suggest that much of what looks like low dimensionality in raw functional profiles is a shared mean.
>
> H2-01:C-002 [danger: Critic: answers partly supported] First, the closing summary line 'Profiles appear dominated by a shared mean' goes further than the evidence.
>
> H2-01:C-003 [danger: Critic: answers partly supported] Sun2020 shows that a per-sample prediction-accuracy metric barely changes when genes are permuted across samples.
>
> H2-01:C-004 [danger: Critic: answers partly supported] HMP2012 reports that pathway levels vary less than taxa in the human body.
>
> H2-01:C-005 [danger: Critic: answers partly supported] Neither is a decomposition that measures how much of a sample-by-function matrix is a mean profile, and both come from human-associated and a few soil datasets.
>
> H2-01:C-006 [danger: Critic: answers partly supported] The body supports only this: in these datasets, per-sample functional profiles are highly similar to one another.
>

Not found in the cited text (where to look, not what is wrong): HMP

## processing-effects.1 (claim)

Relative (sum-to-one) normalisation introduces a sample-level factor shared by all genes.

- conf: not stated
- class: not stated
- holds: relative normalisation of functional profiles
- src: none (the note cites no source for this sentence)
- trail: H2-01 §2.3

From the note:

> H2-01:B-0067 [2.3 How processing choices move the estimate] - **Normalisation and genome size.** Relative (sum-to-one) normalisation introduces a sample-level factor shared by all genes.
>

## processing-effects.2 (claim)

The relative abundance of universal single-copy genes correlated with average genome size at R = −0.78 across HMP body sites and −0.82 in stool.

- conf: not stated
- class: meas (marker)
- holds: HMP body sites and stool
- src: manorMUSiCCMarkerGenes2015 (FT; measured)
- trail: H2-01 §2.3

From the note:

> H2-01:I-0009 [2.3 How processing choices move the estimate] The relative abundance of universal single-copy genes correlated with average genome size at R = −0.78 across HMP body sites and −0.82 in stool [Manor2015; FT; measured].
>

## processing-effects.3 (claim)

Species abundance explained 74% of average-genome-size variation across HMP samples, and genome-size variation makes genes at equal per-cell copy number look variable and hides real per-cell variation, so genome size makes stable genes look variable and variable genes look stable.

- conf: not stated
- class: meas (marker)
- holds: HMP samples
- src: nayfachAverageGenomeSize2015 (FT per metagenomics angle, AB per statistics angle; measured)
- trail: H2-01 §2.3, §answers

From the note:

> H2-01:I-0010 [2.3 How processing choices move the estimate] Species abundance explained 74% of average-genome-size variation across HMP samples, and genome-size variation makes genes at equal per-cell copy number look variable and hides real per-cell variation [Nayfach2015; FT per metagenomics angle, AB per statistics angle; measured].
>
> H2-01:A-058 [quote: Answers as delivered] Relative normalisation and KEGG aggregation reduce functional variability [Manor2017], genome size makes stable genes look variable and variable genes look stable [Nayfach2015], a shared mean profile makes profiles look alike [Sun2020], and comparing fine taxonomy with coarse function favours functional stability by construction (reviewer's reading).
>

## processing-effects.4 (claim)

In soils, genome size tracked the ratio of polysaccharide-decomposition to biomass-synthesis genes across 2,650 genomes and a continental survey.

- conf: not stated
- class: not stated
- holds: soil bacteria; 2,650 genomes and a continental survey
- src: wuGlobalRelationshipGenome2025 (AB)
- trail: H2-01 §2.3

From the note:

> H2-01:B-0068 [2.3 How processing choices move the estimate] In soils, genome size tracked the ratio of polysaccharide-decomposition to biomass-synthesis genes across 2,650 genomes and a continental survey [Wu2025; AB].
>

Not found in the cited text (where to look, not what is wrong): holds: bacteria

## processing-effects.5 (claim)

In HMP gut samples, single-copy-gene (marker-gene) normalisation raised pathway coefficients of variation relative to relative normalisation, uniform mapping of KOs shared among pathways gave less variable pathway profiles than a sample-specific mapping, and aggregating KOs into KEGG pathways lowered variability relative to aggregates built from genome co-occurrence.

- conf: single (note: "SINGLE SOURCE for this set of quantities")
- class: meas (note: "What is measured")
- holds: HMP gut samples; across-sample variability of pathway profiles; the only measured test of aggregation and shared-member mapping
- src: manorRevisedComputationalMetagenomic2017 (FT)
- trail: H2-01 §2.3, §answers

From the note:

> H2-01:B-0072 [2.3 How processing choices move the estimate] - **Aggregation into gene sets that share members.** I re-checked Manor and Borenstein (2017) [FT].
>
> H2-01:B-0073 [2.3 How processing choices move the estimate] In HMP gut samples, single-copy-gene normalisation raised pathway coefficients of variation relative to relative normalisation.
>
> H2-01:B-0074 [2.3 How processing choices move the estimate] Uniform mapping of KOs shared among pathways gave less variable pathway profiles than a sample-specific mapping.
>
> H2-01:B-0076 [2.3 How processing choices move the estimate] Aggregating KOs into KEGG pathways lowered variability relative to aggregates built from genome co-occurrence.
>
> H2-01:B-0077 [2.3 How processing choices move the estimate] The authors conclude that reported functional uniformity is partly a processing artefact [SINGLE SOURCE for this set of quantities].
>
> H2-01:A-008 [quote: Answers as delivered] What is measured is that these choices change across-sample variance and covariance: marker-gene normalisation raises pathway variability, and uniform mapping of shared KOs and KEGG aggregation lower it [Manor2017]; naive mapping inflates pathway counts [YeDoak2009]; relative data distort correlation [Lovell2015].
>
> H2-01:A-028 [quote: Answers as delivered] Removing Manor2017 removes the only measurement of shared-member and aggregation effects on across-sample variability..
>
> H2-01:A-067 [quote: Answers as delivered] *Single-source sensitivity:* Removing Manor2017 would weaken the processing caution substantially (it is the only measured test of aggregation and shared-member mapping).
>

## processing-effects.6 (claim)

On average 9.5% of gene-family pairs within the same KEGG pathway were negatively correlated (R < −0.3).

- conf: not stated
- class: not stated
- holds: HMP gut samples
- src: manorRevisedComputationalMetagenomic2017 (FT)
- trail: H2-01 §2.3

From the note:

> H2-01:B-0072 [2.3 How processing choices move the estimate] - **Aggregation into gene sets that share members.** I re-checked Manor and Borenstein (2017) [FT].
>
> H2-01:B-0073 [2.3 How processing choices move the estimate] In HMP gut samples, single-copy-gene normalisation raised pathway coefficients of variation relative to relative normalisation.
>
> H2-01:B-0075 [2.3 How processing choices move the estimate] On average 9.5% of gene-family pairs within the same KEGG pathway were negatively correlated (R < −0.3).
>

## processing-effects.7 (claim)

Manor and Borenstein (2017) conclude that reported functional uniformity is partly a processing artefact, and call perceived functional uniformity "a potential misconception".

- conf: not stated
- class: not stated
- holds: HMP gut samples
- src: manorRevisedComputationalMetagenomic2017 (FT)
- trail: H2-01 §2.3, §critic

From the note:

> H2-01:B-0072 [2.3 How processing choices move the estimate] - **Aggregation into gene sets that share members.** I re-checked Manor and Borenstein (2017) [FT].
>
> H2-01:B-0073 [2.3 How processing choices move the estimate] In HMP gut samples, single-copy-gene normalisation raised pathway coefficients of variation relative to relative normalisation.
>
> H2-01:B-0077 [2.3 How processing choices move the estimate] The authors conclude that reported functional uniformity is partly a processing artefact [SINGLE SOURCE for this set of quantities].
>
> H2-01:C-025 [danger: Critic: answers partly supported] The authors call perceived functional uniformity 'a potential misconception'.
>

## processing-effects.8 (claim)

Naive mapping of a gene family to every pathway containing it inflates pathway counts.

- conf: not stated
- class: not stated
- holds: pathway reconstruction, mapping gene families to pathways
- src: yeParsimonyApproachBiological2009 (AB)
- trail: H2-01 §2.3

From the note:

> H2-01:R-0261 [Reference list] A parsimony approach to biological pathway reconstruction/inference for genomes and metagenomes.
>
> H2-01:B-0078 [2.3 How processing choices move the estimate] Naive mapping of a family to every pathway containing it inflates pathway counts [YeDoak2009; AB].
>
> H2-01:A-008 [quote: Answers as delivered] What is measured is that these choices change across-sample variance and covariance: marker-gene normalisation raises pathway variability, and uniform mapping of shared KOs and KEGG aggregation lower it [Manor2017]; naive mapping inflates pathway counts [YeDoak2009]; relative data distort correlation [Lovell2015].
>

## processing-effects.9 (claim)

In transcriptomics, pathways sharing genes shift each other's significance ("crosstalk").

- conf: not stated
- class: not stated
- holds: pathway significance analysis in transcriptomics, another field
- src: donatoAnalysisCorrectionCrosstalk2013 (AB; other field)
- trail: H2-01 §2.3

From the note:

> H2-01:B-0079 [2.3 How processing choices move the estimate] In transcriptomics, pathways sharing genes shift each other's significance ("crosstalk") [Donato2013; AB; other field].
>

## processing-effects.10 (claim)

Correlation is not a valid association measure for relative data; proportionality is offered instead.

- conf: not stated
- class: not stated
- holds: relative (compositional) data, from another field
- src: lovellProportionalityValidAlternative2015 (AB; other field)
- trail: H2-01 §2.3

From the note:

> H2-01:B-0082 [2.3 How processing choices move the estimate] - **Compositional closure.** Correlation is not a valid association measure for relative data; proportionality is offered instead [Lovell2015; AB; other field].
>
> H2-01:A-008 [quote: Answers as delivered] What is measured is that these choices change across-sample variance and covariance: marker-gene normalisation raises pathway variability, and uniform mapping of shared KOs and KEGG aggregation lower it [Manor2017]; naive mapping inflates pathway counts [YeDoak2009]; relative data distort correlation [Lovell2015].
>

## community-weighted-means.1 (claim)

In trait ecology, CWMs all share the same abundance weights, so the composition matrix itself induces structure among CWMs.

- conf: not stated
- class: not stated
- holds: community-weighted means in trait ecology
- src: none (the note cites no source for this sentence)
- trail: H2-01 §2.3

From the note:

> H2-01:B-0083 [2.3 How processing choices move the estimate] - **Community-weighted aggregates.** In trait ecology, CWMs all share the same abundance weights, so the composition matrix itself induces structure among CWMs.
>

## community-weighted-means.2 (claim)

CWM correlation tests have inflated error rates when only environment or only traits structure species distributions.

- conf: not stated
- class: model (marker)
- holds: CWM correlation tests; modelled
- src: peresnetoLinkingTraitVariation2017 (AB; modelled)
- trail: H2-01 §2.3

From the note:

> H2-01:I-0011 [2.3 How processing choices move the estimate] CWM correlation tests have inflated error rates when only environment or only traits structure species distributions [PeresNeto2017; AB; modelled].
>

## community-weighted-means.3 (claim)

The inflation of CWM correlation test error rates falls with compositional beta diversity and rises with sample size.

- conf: not stated
- class: model (marker)
- holds: CWM correlation tests; modelled
- src: zelenyWhichResultsStandard2018 (AB; modelled)
- trail: H2-01 §2.3

From the note:

> H2-01:I-0011 [2.3 How processing choices move the estimate] CWM correlation tests have inflated error rates when only environment or only traits structure species distributions [PeresNeto2017; AB; modelled].
>
> H2-01:I-0012 [2.3 How processing choices move the estimate] The inflation falls with compositional beta diversity and rises with sample size [Zeleny2018; AB; modelled].
>

## community-weighted-means.4 (claim)

By analogy, community-aggregated functional profiles share weights in the same way as CWMs.

- conf: not stated
- class: reading (note: "By analogy (reviewer's reading)")
- holds: community-aggregated microbial functional profiles, by analogy with trait-ecology CWMs
- src: none (the reviewer's reading)
- trail: H2-01 §2.3

From the note:

> H2-01:B-0083 [2.3 How processing choices move the estimate] - **Community-weighted aggregates.** In trait ecology, CWMs all share the same abundance weights, so the composition matrix itself induces structure among CWMs.
>
> H2-01:B-0084 [2.3 How processing choices move the estimate] By analogy (reviewer's reading), community-aggregated functional profiles share weights in the same way.
>

## community-weighted-means.5 (claim)

Abundance-weighted and unweighted trait moments disagreed in sign, significance or both for 71% of forest trait-climate results.

- conf: not stated
- class: not stated
- holds: forest trait-climate results
- src: wieczynskiClimateShapesShifts2018 (AB)
- trail: H2-01 §4.4

From the note:

> H2-01:B-0163 [4.4 Covariation among functions against levels and composition] - Weighting changes level comparisons: abundance-weighted and unweighted trait moments disagreed in sign, significance or both for 71% of forest trait-climate results [Wieczynski2019; AB], and CWM accuracy depended on trait coverage of the community [Borgy2017; AB].
>

## community-weighted-means.6 (claim)

CWM accuracy depended on trait coverage of the community.

- conf: not stated
- class: not stated
- holds: plant community trait data
- src: borgySensitivityCommunitylevelTraitenvironment2017 (AB)
- trail: H2-01 §4.4

From the note:

> H2-01:B-0162 [4.4 Covariation among functions against levels and composition] **Plant traits (other field, both directions).**
>
> H2-01:B-0163 [4.4 Covariation among functions against levels and composition] - Weighting changes level comparisons: abundance-weighted and unweighted trait moments disagreed in sign, significance or both for 71% of forest trait-climate results [Wieczynski2019; AB], and CWM accuracy depended on trait coverage of the community [Borgy2017; AB].
>

## dimensionality.1 (claim)

Few direct estimates of dimension exist for microbial sample-by-function matrices, and they use incompatible methods (NMF rank 5 for 8,214 Pfams in 45 ocean samples, two co-inertia axes carrying about half the variation in 128 soils, three KO clusters across 6,539 metagenomes); none uses a formal rank-selection rule (parallel analysis, cross-validated PCA or NMF, a random-matrix threshold) with stated n and p and tests how the estimate changes with processing.

- conf: single (critic: C-009)
- class: not stated
- holds: microbial sample-level functional profiles; each direct estimate is a single study, fitted and scored on the same samples
- src: jiangFunctionalBiogeographyOcean2012, pitonLifeHistoryStrategies2023, flinkstromMetagenomicClusteringLinks2024
- rating: "Weak for the microbial sample-level question"
- trail: H2-01 §2.1, §answers, §6. Answers, §critic

From the note:

> H2-01:A-001 [quote: Answers as delivered] **D1: dimensionality of functional profiles across samples, and its dependence on normalisation, sparsity, presence/absence, shared gene-set members and sample size**: Few direct estimates exist for microbial sample-by-function matrices, and they use incompatible methods.
>
> H2-01:B-0046 [2.1 Direct estimates on microbial sample-by-function matrices] Only a handful of studies report something that can be read as a dimension estimate for sample-level functional profiles.
>
> H2-01:B-0047 [2.1 Direct estimates on microbial sample-by-function matrices] None uses a formal rank-selection rule (parallel analysis, cross-validated PCA or NMF, a random-matrix threshold) with stated n and p *and* tests how the estimate changes with processing.
>
> H2-01:A-013 [quote: Answers as delivered] *Strength:* Weak for the microbial sample-level question.
>
> H2-01:A-014 [quote: Answers as delivered] Each direct estimate is a single study, and all are fitted and scored on the same samples.
>
> H2-01:A-104 [6. Answers by direction] **D1.** Direct estimates for microbial sample-level functional profiles are few and use different methods: NMF rank 5 for 8,214 Pfams in 45 ocean samples, two co-inertia axes carrying about half the variation in 128 soils, three KO clusters across 6,539 metagenomes.
>
> H2-01:C-001 [danger: Critic: answers partly supported] - **D1**: Supported as written, with two corrections.
>
> H2-01:C-009 [danger: Critic: answers partly supported] All three direct microbial estimates (Jiang2012, Piton2023, Flinkstrom2024) are single studies fitted and scored on the same samples.
>

## dimensionality.2 (claim)

Across 45 Global Ocean Sampling sites and 8,214 Pfam relative abundances, NMF was judged stable at rank 5 by a concordance criterion; no variance-explained figure was reported, the five components had "strikingly high" similarity to each other, a large ubiquitous, mostly primary-metabolism Pfam block loaded on all of them, and two components could not be interpreted.

- conf: single (critic: C-009)
- class: meas (marker)
- holds: ocean samples (Global Ocean Sampling sites), n = 45; fitted and scored on the same samples
- src: jiangFunctionalBiogeographyOcean2012 (FT; measured; fitted and scored on the same samples; SINGLE SOURCE)
- trail: H2-01 §2.1, §answers

From the note:

> H2-01:B-0048 [2.1 Direct estimates on microbial sample-by-function matrices] - **Ocean, Pfam, NMF.** Across 45 Global Ocean Sampling sites and 8,214 Pfam relative abundances, NMF was judged stable at rank 5 by a concordance criterion.
>
> H2-01:B-0049 [2.1 Direct estimates on microbial sample-by-function matrices] No variance-explained figure was reported.
>
> H2-01:B-0050 [2.1 Direct estimates on microbial sample-by-function matrices] The five components had "strikingly high" similarity to each other, and a large ubiquitous, mostly primary-metabolism Pfam block loaded on all of them.
>
> H2-01:I-0002 [2.1 Direct estimates on microbial sample-by-function matrices] Two components could not be interpreted [Jiang2012; FT; measured; fitted and scored on the same samples; SINGLE SOURCE].
>
> H2-01:A-002 [quote: Answers as delivered] NMF was stable at rank 5 for 8,214 Pfams across 45 ocean samples, with a large ubiquitous block loading on every component [Jiang2012].
>
> H2-01:C-009 [danger: Critic: answers partly supported] All three direct microbial estimates (Jiang2012, Piton2023, Flinkstrom2024) are single studies fitted and scored on the same samples.
>

## dimensionality.3 (claim)

Rank 5 is low relative to 8,214 features, but with n = 45 the rank cannot exceed 45, and much of the NMF fit is a shared mean-like profile.

- conf: not stated
- class: reading (note: "Reviewer's reading")
- holds: the ocean NMF estimate (45 sites, 8,214 Pfams)
- src: jiangFunctionalBiogeographyOcean2012
- trail: H2-01 §2.1

From the note:

> H2-01:B-0048 [2.1 Direct estimates on microbial sample-by-function matrices] - **Ocean, Pfam, NMF.** Across 45 Global Ocean Sampling sites and 8,214 Pfam relative abundances, NMF was judged stable at rank 5 by a concordance criterion.
>
> H2-01:B-0051 [2.1 Direct estimates on microbial sample-by-function matrices] Reviewer's reading: this is a low rank relative to 8,214 features, but with n = 45 the rank cannot exceed 45, and much of the fit is a shared mean-like profile.
>

## dimensionality.4 (claim)

In 128 soil metagenomes (global topsoil set) with KEGG, eggNOG, SEED, CAZy and genomic-trait tables (relative abundance normalised by annotated bacterial reads, log(x+1), z-scored), the first four multiple co-inertia axes captured 29%, 21%, 16% and 10% of variation, and the first axis tracked average genome size (R² = 0.64).

- conf: single (marker)
- class: meas (marker)
- holds: soil metagenomes, community-aggregated traits; fitted and scored on the same samples; the only variance-explained figure for a microbial functional profile; the critic: full text "per angle" and not re-checked by the reviewer
- src: pitonLifeHistoryStrategies2023 (FT; measured; SINGLE SOURCE)
- trail: H2-01 §2.1, §answers, §Adversarial

From the note:

> H2-01:B-0052 [2.1 Direct estimates on microbial sample-by-function matrices] - **Soil, community-aggregated traits, co-inertia.** In 128 soil metagenomes (global topsoil set) with KEGG, eggNOG, SEED, CAZy and genomic-trait tables (relative abundance normalised by annotated bacterial reads, log(x+1), z-scored), the first four multiple co-inertia axes captured 29%, 21%, 16% and 10% of variation.
>
> H2-01:I-0003 [2.1 Direct estimates on microbial sample-by-function matrices] The first axis tracked average genome size (R² = 0.64) [Piton2023; FT; measured; SINGLE SOURCE].
>
> H2-01:A-003 [quote: Answers as delivered] In 128 soils, two co-inertia axes carried 29% and 21% of variation and the next two 16% and 10% [Piton2023].
>
> H2-01:A-026 [quote: Answers as delivered] Removing Piton2023 leaves no variance-explained figure for a microbial functional profile.
>
> H2-01:C-009 [danger: Critic: answers partly supported] All three direct microbial estimates (Jiang2012, Piton2023, Flinkstrom2024) are single studies fitted and scored on the same samples.
>
> H2-01:C-062 [warning: Adversarial critique, full findings] - D1 access_basis says 'Mostly full text', but the synthesis re-opened only Chen2020 and Manor2017. Piton2023 (the only variance-explained figure), Mouillot2021 (the only measured dependence of dimension on feature and sample count), Nayfach2015, HMP2012 and Tian2020 are full text 'per angle' and were not re-checked, even though they are named as single points of failure.
>

## dimensionality.5 (claim)

Piton et al. call the soil co-inertia result a two-dimension "triangle" of life-history strategies, and warn that community-aggregated covariation does not show within-organism trade-offs and that only 5 to 15% of reads were annotated, with annotation coverage falling as genome size rose.

- conf: not stated
- class: not stated
- holds: 128 soil metagenomes
- src: pitonLifeHistoryStrategies2023
- trail: H2-01 §2.1

From the note:

> H2-01:B-0052 [2.1 Direct estimates on microbial sample-by-function matrices] - **Soil, community-aggregated traits, co-inertia.** In 128 soil metagenomes (global topsoil set) with KEGG, eggNOG, SEED, CAZy and genomic-trait tables (relative abundance normalised by annotated bacterial reads, log(x+1), z-scored), the first four multiple co-inertia axes captured 29%, 21%, 16% and 10% of variation.
>
> H2-01:B-0053 [2.1 Direct estimates on microbial sample-by-function matrices] The authors call this a two-dimension "triangle" of life-history strategies.
>
> H2-01:B-0054 [2.1 Direct estimates on microbial sample-by-function matrices] They also warn that community-aggregated covariation does not show within-organism trade-offs, and that only 5 to 15% of reads were annotated, with annotation coverage falling as genome size rose.
>

## dimensionality.6 (claim)

In the soil co-inertia result, two axes carry about half the variation; the other half is not low-dimensional on this evidence.

- conf: not stated
- class: reading (note: "Reviewer's reading")
- holds: 128 soil metagenomes
- src: pitonLifeHistoryStrategies2023
- trail: H2-01 §2.1

From the note:

> H2-01:B-0052 [2.1 Direct estimates on microbial sample-by-function matrices] - **Soil, community-aggregated traits, co-inertia.** In 128 soil metagenomes (global topsoil set) with KEGG, eggNOG, SEED, CAZy and genomic-trait tables (relative abundance normalised by annotated bacterial reads, log(x+1), z-scored), the first four multiple co-inertia axes captured 29%, 21%, 16% and 10% of variation.
>
> H2-01:B-0055 [2.1 Direct estimates on microbial sample-by-function matrices] Reviewer's reading: two axes carry about half the variation; the other half is not low-dimensional on this evidence.
>

## dimensionality.7 (claim)

Across 6,539 IMG/M assembled metagenomes (KO abundances, KOs in under 10% of samples removed, CLR), bootstrapped k-means found three clusters (terrestrial, aquatic, anaerobic), strongly associated with assembly GC content; cluster number is not an intrinsic-dimension estimate and is a nearest precedent only.

- conf: single (marker)
- class: meas (marker)
- holds: multi-biome assembled metagenomes; fitted and scored on the same samples
- src: flinkstromMetagenomicClusteringLinks2024 (FT; measured; SINGLE SOURCE)
- trail: H2-01 §2.1, §answers

From the note:

> H2-01:I-0004 [2.1 Direct estimates on microbial sample-by-function matrices] - **Multi-biome KO clusters.** Across 6,539 IMG/M assembled metagenomes (KO abundances, KOs in under 10% of samples removed, CLR), bootstrapped k-means found three clusters (terrestrial, aquatic, anaerobic), strongly associated with assembly GC content [Flinkstrom2024; FT; measured; SINGLE SOURCE].
>
> H2-01:B-0056 [2.1 Direct estimates on microbial sample-by-function matrices] Cluster number is not an intrinsic-dimension estimate, and it is reported here as a nearest precedent only.
>
> H2-01:A-004 [quote: Answers as delivered] Across 6,539 metagenomes, KO profiles formed three clusters [Flinkstrom2024], which is not a dimension estimate.
>
> H2-01:C-009 [danger: Critic: answers partly supported] All three direct microbial estimates (Jiang2012, Piton2023, Flinkstrom2024) are single studies fitted and scored on the same samples.
>

## dimensionality.8 (claim)

Across 25 GOS metagenomes, the first canonical correlation between KEGG module composition and environment was 0.944; with n = 25 and many modules, a high first canonical correlation on the same samples is expected, and it does not measure dimension.

- conf: not stated
- class: meas (marker)
- holds: ocean metagenomes (GOS), n = 25
- src: raesTowardMolecularTraitbased2011 (FT; measured)
- trail: H2-01 §2.1

From the note:

> H2-01:I-0005 [2.1 Direct estimates on microbial sample-by-function matrices] - **Ocean modules, CCA.** Across 25 GOS metagenomes, the first canonical correlation between KEGG module composition and environment was 0.944 [Raes2011; FT; measured].
>
> H2-01:B-0057 [2.1 Direct estimates on microbial sample-by-function matrices] With n = 25 and many modules, a high first canonical correlation on the same samples is expected.
>
> H2-01:B-0058 [2.1 Direct estimates on microbial sample-by-function matrices] It does not measure dimension.
>

## dimensionality.9 (claim)

Gianoulis et al. (2009) define "metabolic footprints" by CCA on GOS.

- conf: not stated
- class: not stated
- holds: GOS
- src: gianoulisQuantifyingEnvironmentalAdaptation2009 (AB)
- trail: H2-01 §2.1

From the note:

> H2-01:B-0059 [2.1 Direct estimates on microbial sample-by-function matrices] Gianoulis et al. (2009) similarly define "metabolic footprints" by CCA on GOS [Gianoulis2009; AB].
>

## dimensionality.10 (claim)

Read literally, the direct estimates are low relative to the number of functions, but in each case n is small or only about half the variance is in the leading axes, and the leading structure is partly a shared mean profile (evidence the critic reads as showing only that per-sample profiles are highly similar in these datasets) or a genome-size axis (Piton axis 1 against genome size R² 0.64; genome size and normalisation effects).

- conf: not stated
- class: not stated
- holds: the three direct microbial estimates
- src: jiangFunctionalBiogeographyOcean2012, pitonLifeHistoryStrategies2023, flinkstromMetagenomicClusteringLinks2024, sunInferenceBasedAccuracyMetagenome2020, theStructureFunctionDiversity2012, nayfachAverageGenomeSize2015, manorMUSiCCMarkerGenes2015
- trail: H2-01 §answers, §critic

From the note:

> H2-01:A-005 [quote: Answers as delivered] Read literally, these are low relative to the number of functions.
>
> H2-01:A-006 [quote: Answers as delivered] But in each case n is small or only about half the variance is in the leading axes, and the leading structure is partly a shared mean profile (profiles barely change when genes are permuted across samples [Sun2020]; HMP pathway levels much more constant than taxa [HMP2012]) or a genome-size axis (Piton axis 1 vs genome size R2 0.64; genome size and normalisation effects [Nayfach2015; Manor2015]).
>
> H2-01:C-006 [danger: Critic: answers partly supported] The body supports only this: in these datasets, per-sample functional profiles are highly similar to one another.
>

Not found in the cited text (where to look, not what is wrong): R²

## dimensionality.11 (claim)

No microbial study was found that re-estimated the dimension of functional profiles under different normalisations, sparsity filters, presence/absence against abundance, overlapping gene sets or sample sizes; none tested sensitivity to these choices with a formal rank rule and stated n and p.

- conf: not stated
- class: search (note: "Not found by these routes")
- holds: microbial sample-by-function profiles; the review's search routes
- src: none (a search result)
- search: searched, not found (note: "Not found by these routes")
- trail: H2-01 §2.3, §answers, §Provenance, §critic

From the note:

> H2-01:B-0065 [2.3 How processing choices move the estimate] No study was found that re-estimated the dimension of functional profiles under different normalisations, sparsity filters, presence/absence against abundance, or sample sizes.
>
> H2-01:B-0018 [info: Provenance] Not found by these routes: any microbial test withholding a habitat when scoring functional covariation; any microbial cross-habitat comparison of covariation stability against level and composition stability; any microbial study of how dimension estimates change with normalisation, sparsity, presence/absence, overlapping gene sets or sample size; any study holding taxonomy fixed while habitat varies.
>
> H2-01:A-007 [quote: Answers as delivered] No microbial study re-estimated dimension under different normalisation, sparsity filters, presence/absence against abundance, or sample size.
>
> H2-01:A-019 [quote: Answers as delivered] *Not measured:* No microbial estimate with a formal rank rule and stated n and p tested against normalisation, sparsity filtering, presence/absence against abundance, overlapping against non-overlapping gene sets, or subsampled sample size.
>
> H2-01:A-105 [6. Answers by direction] None tests sensitivity to normalisation, sparsity, presence against abundance, or sample size.
>
> H2-01:C-010 [danger: Critic: answers partly supported] No microbial study tested sensitivity to normalisation, sparsity, presence/absence against abundance, overlapping gene sets or sample size.
>

Not found in the cited text (where to look, not what is wrong): holds: sample-by-function; holds: review

## dimensionality.12 (claim)

What is measured is that processing choices change across-sample variance and covariance (normalisation, genome size, pathway aggregation, compositional closure), which a dimension estimate would inherit; that these shifts lower apparent dimension is the reviewer's inference, so the evidence is only indirect for dimension.

- conf: not stated
- class: reading (note: "is the reviewer's inference")
- holds: microbial functional profiles; indirect for dimension
- src: manorRevisedComputationalMetagenomic2017, yeParsimonyApproachBiological2009, lovellProportionalityValidAlternative2015
- trail: H2-01 §2.3, §answers, §6. Answers, §Adversarial

From the note:

> H2-01:B-0066 [2.3 How processing choices move the estimate] What exists is measured evidence that these choices change across-sample variance and covariance, which a dimension estimate would inherit (indirect for D1).
>
> H2-01:A-008 [quote: Answers as delivered] What is measured is that these choices change across-sample variance and covariance: marker-gene normalisation raises pathway variability, and uniform mapping of shared KOs and KEGG aggregation lower it [Manor2017]; naive mapping inflates pathway counts [YeDoak2009]; relative data distort correlation [Lovell2015].
>
> H2-01:A-009 [quote: Answers as delivered] That these shifts lower apparent dimension is the reviewer's inference.
>
> H2-01:A-015 [quote: Answers as delivered] Processing effects are measured but only indirect for dimension.
>
> H2-01:A-106 [6. Answers by direction] Evidence that these choices change across-sample variance and covariance is measured (normalisation, genome size, pathway aggregation, compositional closure) but indirect for dimension.
>
> H2-01:C-131 [warning: Adversarial critique, full findings] - Section 2.3 and the D1 answer mark 'these shifts lower apparent dimension' as the reviewer's inference, which is correct. The Section 6 summary then drops that label.
>

## dimensionality.13 (claim)

At least one leading axis of many functional-profile decompositions may be a genome-size or normalisation axis; the first Piton axis (R² = 0.64 with genome size) is consistent with this. This is an inference, not a measured decomposition.

- conf: not stated
- class: reading (note: "Reviewer's reading")
- holds: functional-profile decompositions
- src: pitonLifeHistoryStrategies2023
- trail: H2-01 §2.3

From the note:

> H2-01:B-0069 [2.3 How processing choices move the estimate] The first Piton axis (R² = 0.64 with genome size) is consistent with this [Piton2023].
>
> H2-01:B-0070 [2.3 How processing choices move the estimate] Reviewer's reading: at least one leading axis of many functional-profile decompositions may be a genome-size or normalisation axis.
>
> H2-01:B-0071 [2.3 How processing choices move the estimate] This is an inference, not a measured decomposition.
>

## dimensionality.14 (claim)

None of the gene-set studies measures a covariance matrix between overlapping gene sets; that shared members inflate pathway-pathway covariance, and so lower apparent dimension, is the reviewer's inference.

- conf: not stated
- class: reading (note: "is the reviewer's inference")
- holds: pathway profiles built from gene sets that share members
- src: manorRevisedComputationalMetagenomic2017, yeParsimonyApproachBiological2009, donatoAnalysisCorrectionCrosstalk2013
- trail: H2-01 §2.3

From the note:

> H2-01:B-0078 [2.3 How processing choices move the estimate] Naive mapping of a family to every pathway containing it inflates pathway counts [YeDoak2009; AB].
>
> H2-01:B-0079 [2.3 How processing choices move the estimate] In transcriptomics, pathways sharing genes shift each other's significance ("crosstalk") [Donato2013; AB; other field].
>
> H2-01:B-0080 [2.3 How processing choices move the estimate] None of these measures a covariance matrix between overlapping gene sets.
>
> H2-01:B-0081 [2.3 How processing choices move the estimate] The implication that shared members inflate pathway-pathway covariance, and so lower apparent dimension, is the reviewer's inference.
>

## dimensionality.15 (claim)

Whether a dimension estimate is taken before or after centring on the shared mean profile will change it; no microbial study found reports both.

- conf: not stated
- class: search (note: "No microbial study found reports both")
- holds: microbial functional profiles
- src: none (the reviewer's statement and a search result)
- search: searched, not found (note: "No microbial study found reports both")
- trail: H2-01 §2.2

From the note:

> H2-01:B-0063 [2.2 A dominant mean profile] Whether a dimension estimate is taken before or after centring on this mean will change it.
>
> H2-01:B-0064 [2.2 A dominant mean profile] No microbial study found reports both.
>

## dimensionality.16 (claim)

No held-out (cross-validated) rank estimate has been measured for functional profiles.

- conf: not stated
- class: search (note: "Not measured")
- holds: microbial functional profiles
- src: none (a search result)
- search: not stated
- trail: H2-01 §answers

From the note:

> H2-01:A-019 [quote: Answers as delivered] *Not measured:* No microbial estimate with a formal rank rule and stated n and p tested against normalisation, sparsity filtering, presence/absence against abundance, overlapping against non-overlapping gene sets, or subsampled sample size.
>
> H2-01:A-020 [quote: Answers as delivered] No held-out (cross-validated) rank estimate for functional profiles.
>

## dimensionality.17 (claim)

Dimension has not been compared by habitat; no search route targeted habitat-stratified decompositions (for example the per-biome NMF or PCA in multi-biome metagenome atlases).

- conf: not stated
- class: search (note: "Dimension by habitat not compared")
- holds: microbial functional profiles
- src: none (a search result)
- search: not searched (critic: C-113)
- trail: H2-01 §answers, §Adversarial

From the note:

> H2-01:A-021 [quote: Answers as delivered] Dimension by habitat not compared..
>
> H2-01:C-113 [warning: Adversarial critique, full findings] - gap: Dimension compared by habitat. It is noted as not measured, but no route targeted habitat-stratified decompositions (for example the per-biome NMF or PCA in multi-biome metagenome atlases).; setting_or_class: Multi-biome metagenome atlases stratified by biome; direction: D1
>

## dimension-elsewhere.1 (claim)

Across 2,621 bacterial genera, diffusion maps on presence/absence of 7,769 substrate-product traits found no single low-dimensional space but crossing low-dimensional manifolds with "dozens or possibly hundreds of meaningful coordinates".

- conf: single (marker)
- class: model (marker)
- holds: genomes as rows (genera), not samples; presence/absence; one modelled study
- src: fahimipourMappingBacterialMetabolic2020a (FT; modelled; SINGLE SOURCE)
- trail: H2-01 §2.4, §critic, §Adversarial

From the note:

> H2-01:I-0013 [2.4 Dimensionality elsewhere: genomes, trait databases, transcriptomes] - **Across bacterial genomes.** Diffusion maps on presence/absence of 7,769 substrate-product traits across 2,621 genera found no single low-dimensional space but crossing low-dimensional manifolds with "dozens or possibly hundreds of meaningful coordinates" [Fahimipour2020; FT; modelled; SINGLE SOURCE].
>
> H2-01:B-0085 [2.4 Dimensionality elsewhere: genomes, trait databases, transcriptomes] These are different objects (taxa as rows, or non-microbial samples) and are reported as related work.
>
> H2-01:A-011 [quote: Answers as delivered] Across genomes, metabolic presence/absence is high-dimensional (dozens to hundreds of coordinates [Fahimipour2020]).
>
> H2-01:C-007 [danger: Critic: answers partly supported] Second, 'across genomes, metabolic presence/absence is high-dimensional' rests on one modelled study (Fahimipour2020), and 'low dimensionality holds for leading components within datasets' rests on one study (Heimberg2016).
>
> H2-01:C-070 [warning: Adversarial critique, full findings] - D1 answer: 'Across genomes, metabolic presence/absence is high-dimensional (dozens to hundreds of coordinates)'. This rests on Fahimipour2020 alone (modelled, diffusion maps) and is phrased as a property of genomes in general.
>

## dimension-elsewhere.2 (claim)

A review names three main axes of quantitative bacterial traits (growth rate with rRNA copy number, genome size with signal transduction, cell size) and notes that quantitative traits vary widely within substrate-use pathways.

- conf: not stated
- class: assert (marker)
- holds: quantitative bacterial and archaeal traits
- src: westobyTraitDimensionsBacteria2021 (AB; asserted)
- trail: H2-01 §2.4

From the note:

> H2-01:R-0246 [Reference list] Trait dimensions in bacteria and archaea compared to vascular plants.
>
> H2-01:I-0014 [2.4 Dimensionality elsewhere: genomes, trait databases, transcriptomes] A review names three main axes of quantitative bacterial traits (growth rate with rRNA copy number, genome size with signal transduction, cell size) and notes that quantitative traits vary widely within substrate-use pathways [Westoby2021; AB; asserted].
>

Not found in the cited text (where to look, not what is wrong): holds: archaeal

## dimension-elsewhere.3 (claim)

The genome diffusion-map result and the three-axis trait review are not in conflict: they describe different trait sets, and together they bound any claim that "microbial function" has one dimensionality.

- conf: not stated
- class: not stated
- holds: bacterial trait sets across genomes
- src: fahimipourMappingBacterialMetabolic2020a, westobyTraitDimensionsBacteria2021
- trail: H2-01 §2.4

From the note:

> H2-01:I-0013 [2.4 Dimensionality elsewhere: genomes, trait databases, transcriptomes] - **Across bacterial genomes.** Diffusion maps on presence/absence of 7,769 substrate-product traits across 2,621 genera found no single low-dimensional space but crossing low-dimensional manifolds with "dozens or possibly hundreds of meaningful coordinates" [Fahimipour2020; FT; modelled; SINGLE SOURCE].
>
> H2-01:I-0014 [2.4 Dimensionality elsewhere: genomes, trait databases, transcriptomes] A review names three main axes of quantitative bacterial traits (growth rate with rRNA copy number, genome size with signal transduction, cell size) and notes that quantitative traits vary widely within substrate-use pathways [Westoby2021; AB; asserted].
>
> H2-01:B-0086 [2.4 Dimensionality elsewhere: genomes, trait databases, transcriptomes] These two are not in conflict: they describe different trait sets.
>
> H2-01:B-0087 [2.4 Dimensionality elsewhere: genomes, trait databases, transcriptomes] Together they bound any claim that "microbial function" has one dimensionality.
>

## dimension-elsewhere.4 (claim)

Across 30 species-by-trait datasets, the median dimension was 4 by an elbow rule (range 2 to 8) and 6 by an AUC threshold of 0.7 (range 2 to 17), and the two estimates were only weakly correlated.

- conf: not stated
- class: meas (marker)
- holds: species trait databases (species as rows, not samples)
- src: mouillotDimensionalityStructureSpecies2021 (FT; measured)
- trail: H2-01 §2.4, §answers

From the note:

> H2-01:I-0015 [2.4 Dimensionality elsewhere: genomes, trait databases, transcriptomes] - **Species trait databases.** Across 30 species-by-trait datasets, the median dimension was 4 by an elbow rule (range 2 to 8) and 6 by an AUC threshold of 0.7 (range 2 to 17), and the two estimates were only weakly correlated [Mouillot2021; FT; measured].
>
> H2-01:B-0085 [2.4 Dimensionality elsewhere: genomes, trait databases, transcriptomes] These are different objects (taxa as rows, or non-microbial samples) and are reported as related work.
>
> H2-01:A-010 [quote: Answers as delivered] How dimension depends on feature number, feature correlation and sample count has only been measured in species trait databases (median 4 or 6 axes depending on the rule, rising with number of traits, falling with trait correlation, and sensitive to species number only below about 100 to 200 [Mouillot2021]).
>

## dimension-elsewhere.5 (claim)

In species trait databases, threshold dimensionality rose with the log number of traits and fell with mean trait correlation (GLM R² = 0.61); in simulations, species number mattered only below about 100 to 200 species, and dropping half the traits lost much quality.

- conf: not stated
- class: not stated
- holds: species-by-trait datasets and simulations
- src: mouillotDimensionalityStructureSpecies2021
- trail: H2-01 §2.4, §answers

From the note:

> H2-01:I-0015 [2.4 Dimensionality elsewhere: genomes, trait databases, transcriptomes] - **Species trait databases.** Across 30 species-by-trait datasets, the median dimension was 4 by an elbow rule (range 2 to 8) and 6 by an AUC threshold of 0.7 (range 2 to 17), and the two estimates were only weakly correlated [Mouillot2021; FT; measured].
>
> H2-01:B-0088 [2.4 Dimensionality elsewhere: genomes, trait databases, transcriptomes] Threshold dimensionality rose with the log number of traits and fell with mean trait correlation (GLM R² = 0.61).
>
> H2-01:B-0089 [2.4 Dimensionality elsewhere: genomes, trait databases, transcriptomes] In simulations, species number mattered only below about 100 to 200 species, and dropping half the traits lost much quality.
>
> H2-01:A-010 [quote: Answers as delivered] How dimension depends on feature number, feature correlation and sample count has only been measured in species trait databases (median 4 or 6 axes depending on the rule, rising with number of traits, falling with trait correlation, and sensitive to species number only below about 100 to 200 [Mouillot2021]).
>

## dimension-elsewhere.6 (claim)

The species-trait study is the only source found that measures how a dimension estimate depends on the number of features, feature correlation and sample count; it concerns species-level traits, not sample-level profiles, from another setting.

- conf: single (note: "This is the only source found")
- class: not stated
- holds: species-by-trait matrices; the critic: read by a search agent and not re-opened by the reviewer, full text "per angle" and not re-checked
- src: mouillotDimensionalityStructureSpecies2021
- trail: H2-01 §2.4, §answers, §6. Answers, §critic, §Adversarial

From the note:

> H2-01:B-0090 [2.4 Dimensionality elsewhere: genomes, trait databases, transcriptomes] This is the only source found that measures how a dimension estimate depends on the number of features, feature correlation and sample count.
>
> H2-01:B-0091 [2.4 Dimensionality elsewhere: genomes, trait databases, transcriptomes] It concerns species-level traits, not sample-level profiles.
>
> H2-01:A-016 [quote: Answers as delivered] The dependence on feature number and sample count rests on one species-trait study from another setting..
>
> H2-01:A-027 [quote: Answers as delivered] Removing Mouillot2021 leaves no measured dependence of dimension on feature count or sample count.
>
> H2-01:A-107 [6. Answers by direction] The only source measuring how dimension estimates depend on feature number, feature correlation and sample count is from species trait databases.
>
> H2-01:C-011 [danger: Critic: answers partly supported] The dependence on feature count and sample count is measured only for species-by-trait matrices (Mouillot2021, read by a search agent and not re-opened by the reviewer).
>
> H2-01:C-062 [warning: Adversarial critique, full findings] - D1 access_basis says 'Mostly full text', but the synthesis re-opened only Chen2020 and Manor2017. Piton2023 (the only variance-explained figure), Mouillot2021 (the only measured dependence of dimension on feature and sample count), Nayfach2015, HMP2012 and Tian2020 are full text 'per angle' and were not re-checked, even though they are named as single points of failure.
>

## dimension-elsewhere.7 (claim)

Plant traits showed at most six dimensions in the largest of three datasets.

- conf: not stated
- class: not stated
- holds: plant trait datasets
- src: laughlinIntrinsicDimensionalityPlant2013 (AB)
- trail: H2-01 §2.4

From the note:

> H2-01:B-0092 [2.4 Dimensionality elsewhere: genomes, trait databases, transcriptomes] Plant traits: at most six dimensions in the largest of three datasets [Laughlin2014; AB].
>

## dimension-elsewhere.8 (claim)

Two components explain 74% of six key plant traits across 2,214 species.

- conf: not stated
- class: not stated
- holds: plant species traits; secondary, via Bruelheide2018
- src: bruelheideGlobalTraitenvironmentRelationships2018 (SEC, via Bruelheide2018)
- trail: H2-01 §2.4

From the note:

> H2-01:B-0093 [2.4 Dimensionality elsewhere: genomes, trait databases, transcriptomes] Two components explain 74% of six key plant traits across 2,214 species [SEC, via Bruelheide2018]; with 17 gap-filled traits across more than 20,000 species, PC1 33%, PC2 15%, PC3 9.4% [Joswig2022; FT].
>

## dimension-elsewhere.9 (claim)

With 17 gap-filled traits across more than 20,000 plant species, PC1 explained 33%, PC2 15% and PC3 9.4%.

- conf: not stated
- class: not stated
- holds: plant species, gap-filled trait matrix
- src: joswigClimaticSoilFactors2021 (FT)
- trail: H2-01 §2.4

From the note:

> H2-01:B-0093 [2.4 Dimensionality elsewhere: genomes, trait databases, transcriptomes] Two components explain 74% of six key plant traits across 2,214 species [SEC, via Bruelheide2018]; with 17 gap-filled traits across more than 20,000 species, PC1 33%, PC2 15%, PC3 9.4% [Joswig2022; FT].
>

## dimension-elsewhere.10 (claim)

The trait gap-filling method BHPMF imputes from trait-trait correlations.

- conf: not stated
- class: not stated
- holds: plant trait gap-filling
- src: schrodtScpBHPMFScp2015 (AB)
- trail: H2-01 §2.4

From the note:

> H2-01:B-0094 [2.4 Dimensionality elsewhere: genomes, trait databases, transcriptomes] The gap-filling (BHPMF) imputes from trait-trait correlations [Schrodt2015; AB], so covariation in imputed matrices is partly built in (reviewer's reading).
>

Not found in the cited text (where to look, not what is wrong): holds: plant

## dimension-elsewhere.11 (claim)

Because BHPMF imputes from trait-trait correlations, covariation in imputed trait matrices is partly built in.

- conf: not stated
- class: reading (note: "reviewer's reading")
- holds: gap-filled plant trait matrices
- src: schrodtScpBHPMFScp2015
- trail: H2-01 §2.4

From the note:

> H2-01:B-0094 [2.4 Dimensionality elsewhere: genomes, trait databases, transcriptomes] The gap-filling (BHPMF) imputes from trait-trait correlations [Schrodt2015; AB], so covariation in imputed matrices is partly built in (reviewer's reading).
>

Not found in the cited text (where to look, not what is wrong): holds: plant

## dimension-elsewhere.12 (claim)

Across 352 microarray datasets, the first principal value averaged about twice the second, the first five explained most variance, and per-gene shuffling removed this; the authors call low dimensionality fundamental.

- conf: single (critic: C-008)
- class: meas (marker)
- holds: gene expression microarray datasets, another field; within datasets
- src: heimbergLowDimensionalityGene2016 (FT; measured; SINGLE SOURCE; critic: C-008 was "FT; measured")
- trail: H2-01 §2.4, §critic, §Adversarial

From the note:

> H2-01:I-0016 [2.4 Dimensionality elsewhere: genomes, trait databases, transcriptomes] - **Gene expression.** Across 352 microarray datasets, the first principal value averaged about twice the second, the first five explained most variance, and per-gene shuffling removed this [Heimberg2016; FT; measured].
>
> H2-01:B-0095 [2.4 Dimensionality elsewhere: genomes, trait databases, transcriptomes] The authors call low dimensionality fundamental.
>
> H2-01:C-007 [danger: Critic: answers partly supported] Second, 'across genomes, metabolic presence/absence is high-dimensional' rests on one modelled study (Fahimipour2020), and 'low dimensionality holds for leading components within datasets' rests on one study (Heimberg2016).
>
> H2-01:C-008 [danger: Critic: answers partly supported] Both should be marked SINGLE SOURCE, as Lenz2016 is.
>
> H2-01:C-071 [warning: Adversarial critique, full findings] - D1 answer: 'In transcriptomics, low dimensionality holds for leading components within datasets [Heimberg2016]'.
>
> H2-01:C-072 [warning: Adversarial critique, full findings] One study, not flagged SINGLE SOURCE, while the opposing Lenz2016 is flagged.
>
> H2-01:C-073 [warning: Adversarial critique, full findings] The labelling is asymmetric.
>
> H2-01:C-119 [warning: Adversarial critique, full findings] - SINGLE SOURCE flags are applied unevenly.
>
> H2-01:C-121 [warning: Adversarial critique, full findings] Heimberg2016 (low dimension) and Pierson2015 (pooled networks poor) carry the same weight from one study and are not flagged.
>

Not found in the cited text (where to look, not what is wrong): holds: field

## dimension-elsewhere.13 (claim)

In large heterogeneous expression compendia (5,372 and 7,100 samples), the first three PCs explained about 36% of variance, components beyond the third were unstable between datasets, the residual space carried most tissue-specific signal, and PCA depended on the fraction of samples carrying a signal.

- conf: single (marker)
- class: meas (marker)
- holds: gene expression compendia, another field; across datasets
- src: lenzPrincipalComponentsAnalysis2016 (FT; measured; SINGLE SOURCE)
- trail: H2-01 §2.4, §answers

From the note:

> H2-01:B-0096 [2.4 Dimensionality elsewhere: genomes, trait databases, transcriptomes] Against this, in large heterogeneous compendia (5,372 and 7,100 samples), the first three PCs explained about 36% of variance, components beyond the third were unstable between datasets, and the residual space carried most tissue-specific signal.
>
> H2-01:I-0017 [2.4 Dimensionality elsewhere: genomes, trait databases, transcriptomes] PCA depended on the fraction of samples carrying a signal [Lenz2016; FT; measured; SINGLE SOURCE].
>
> H2-01:A-012 [quote: Answers as delivered] In transcriptomics, low dimensionality holds for leading components within datasets [Heimberg2016] but weakens across datasets [Lenz2016].
>

Not found in the cited text (where to look, not what is wrong): holds: field

## dimension-elsewhere.14 (claim)

In gene expression, "low-dimensional" holds for leading components within a dataset and weakens when dimension is judged by reproducibility across datasets or by information in the residual.

- conf: single (critic: C-007)
- class: not stated
- holds: transcriptomics, another field; the within-dataset side rests on one study and the across-dataset side on one study
- src: heimbergLowDimensionalityGene2016, lenzPrincipalComponentsAnalysis2016
- trail: H2-01 §2.4, §answers, §critic

From the note:

> H2-01:B-0097 [2.4 Dimensionality elsewhere: genomes, trait databases, transcriptomes] The conflict is informative: "low-dimensional" holds for leading components within a dataset and weakens when dimension is judged by reproducibility across datasets or by information in the residual.
>
> H2-01:A-012 [quote: Answers as delivered] In transcriptomics, low dimensionality holds for leading components within datasets [Heimberg2016] but weakens across datasets [Lenz2016].
>
> H2-01:C-007 [danger: Critic: answers partly supported] Second, 'across genomes, metabolic presence/absence is high-dimensional' rests on one modelled study (Fahimipour2020), and 'low dimensionality holds for leading components within datasets' rests on one study (Heimberg2016).
>
> H2-01:C-008 [danger: Critic: answers partly supported] Both should be marked SINGLE SOURCE, as Lenz2016 is.
>

Not found in the cited text (where to look, not what is wrong): holds: field

## dimension-elsewhere.15 (claim)

Low dimension estimates (Jiang2012, Piton2023's two leading axes, Heimberg2016) stand against higher ones (Fahimipour2020 across genomes; Lenz2016 across datasets; Piton's remaining half of variance); these largely reflect different objects (samples against genomes) and different criteria (within-dataset variance against cross-dataset stability), not direct contradiction on the same data.

- conf: not stated
- class: not stated
- holds: the D1 sources taken together
- src: jiangFunctionalBiogeographyOcean2012, pitonLifeHistoryStrategies2023, heimbergLowDimensionalityGene2016, fahimipourMappingBacterialMetabolic2020a, lenzPrincipalComponentsAnalysis2016
- trail: H2-01 §answers

From the note:

> H2-01:A-017 [quote: Answers as delivered] *Conflicts:* Low (Jiang2012, Piton2023's two leading axes, Heimberg2016) against higher (Fahimipour2020 across genomes; Lenz2016 across datasets; Piton's remaining half of variance).
>
> H2-01:A-018 [quote: Answers as delivered] These largely reflect different objects (samples against genomes) and different criteria (within-dataset variance against cross-dataset stability), not direct contradiction on the same data..
>

Not found in the cited text (where to look, not what is wrong): holds: d1

## covariation-transfer.1 (claim)

No study was found that fitted covariation among microbial functions (a covariance or correlation matrix, a factorisation, a network, or a regression of some functions on others) in a set of habitats and scored it on a withheld habitat; this is a statement about the routes searched, not a statement that the literature lacks such a study.

- conf: not stated
- class: search (note: "Not found by these routes")
- holds: microbial function-function covariation; withheld habitat; routes: Europe PMC, PubMed and PMC E-utilities, Crossref, Semantic Scholar, OpenAlex, Unpaywall and known literature, with WebSearch and Scholar Gateway unavailable
- src: none (a search result)
- search: searched, not found (note: "Not found by these routes")
- rating: "Absent for the withheld-habitat microbial case"
- trail: H2-01 §3.1, §1. What, §Provenance, §answers, §6. Answers, §critic

From the note:

> H2-01:B-0098 [3.1 Held-out habitat, microbial functional profiles: not found] No study was found that fitted covariation among functions (a covariance or correlation matrix, a factorisation, a network, or a regression of some functions on others) in a set of habitats and scored it on a withheld habitat.
>
> H2-01:B-0099 [3.1 Held-out habitat, microbial functional profiles: not found] The three search angles used Europe PMC, PubMed and PMC E-utilities, Crossref, Semantic Scholar, OpenAlex and known literature (see Search record); WebSearch and Scholar Gateway were unavailable.
>
> H2-01:B-0100 [3.1 Held-out habitat, microbial functional profiles: not found] This is a statement about those routes, not a statement that the literature lacks such a study.
>
> H2-01:B-0037 [1. What the literature covers, and what it does not] Across three independent search angles, no study was found that estimated covariation among microbial functions in some habitats and scored it on a habitat left out of the estimate (search routes in the Search record).
>
> H2-01:B-0018 [info: Provenance] Not found by these routes: any microbial test withholding a habitat when scoring functional covariation; any microbial cross-habitat comparison of covariation stability against level and composition stability; any microbial study of how dimension estimates change with normalisation, sparsity, presence/absence, overlapping gene sets or sample size; any study holding taxonomy fixed while habitat varies.
>
> H2-01:A-030 [quote: Answers as delivered] Answered per case: withheld habitat (microbial), withheld study within a habitat (microbial), other fields**: Withheld habitat, microbial functional covariation: not found.
>
> H2-01:A-031 [quote: Answers as delivered] The three search angles used Europe PMC, PubMed and PMC E-utilities, Crossref, Semantic Scholar, OpenAlex, Unpaywall and known literature (WebSearch and Scholar Gateway unavailable).
>
> H2-01:A-042 [quote: Answers as delivered] *Strength:* Absent for the withheld-habitat microbial case.
>
> H2-01:A-047 [quote: Answers as delivered] *Not measured:* Any microbial test withholding a whole habitat.
>
> H2-01:A-048 [quote: Answers as delivered] Any test of function-function covariance (as opposed to taxon-to-function mappings or classifiers) across habitats.
>
> H2-01:A-110 [6. Answers by direction] **D2.** No held-out-habitat test of microbial functional covariation was found.
>
> H2-01:C-012 [danger: Critic: answers partly supported] - **D2**: Withheld habitat, microbial function-function covariation: none found on the routes named.
>

## covariation-transfer.2 (claim)

Pathway co-abundances estimated in an IBD discovery cohort were tested in an independent IBD cohort (iHMP-IBD, 77 individuals): of 37,106 testable pathway co-abundances, 21,882 (59.0%) replicated at P < 0.05; of 2,090 species co-abundances, 531 (25.4%), so pathway co-abundances partly reproduced.

- conf: single (marker)
- class: meas (marker)
- holds: human gut metagenomes from four cohorts (n = 2,379), 134 species and 343 MetaCyc pathways (HUMAnN2), SparCC combined with SPIEC-EASI; the withheld unit is a study within the same habitat and disease state, not a habitat; the only direct microbial test of functional covariation on held-out data
- src: chenGutMicrobialCoabundance2020 (FT, figures re-checked; measured; SINGLE SOURCE)
- rating: "Weak for withheld-study (one study, one habitat)"
- trail: H2-01 §3.2, §answers, §6. Answers, §critic

From the note:

> H2-01:I-0018 [3.2 Held-out study, same habitat (microbial, direct)] Chen et al. (2020) is the only direct microbial test found [Chen2020; FT, figures re-checked; measured; SINGLE SOURCE].
>
> H2-01:B-0101 [3.2 Held-out study, same habitat (microbial, direct)] Human gut metagenomes from four cohorts (n = 2,379): 134 species and 343 MetaCyc pathways (HUMAnN2), SparCC combined with SPIEC-EASI to handle compositionality.
>
> H2-01:B-0103 [3.2 Held-out study, same habitat (microbial, direct)] - Pathway co-abundances estimated in an IBD discovery cohort were tested in an independent IBD cohort (iHMP-IBD, 77 individuals).
>
> H2-01:B-0104 [3.2 Held-out study, same habitat (microbial, direct)] Of 37,106 testable pathway co-abundances, 21,882 (59.0%) replicated at P < 0.05; of 2,090 species co-abundances, 531 (25.4%).
>
> H2-01:B-0110 [3.2 Held-out study, same habitat (microbial, direct)] The withheld unit is a study within the same habitat and disease state, not a habitat.
>
> H2-01:A-032 [quote: Answers as delivered] Withheld study, same habitat: one study.
>
> H2-01:A-033 [quote: Answers as delivered] Pathway co-abundances from an IBD gut cohort partly reproduced in an independent IBD cohort (59.0% of 37,106 at P < 0.05; species 25.4%), with the low species rate attributed to power [Chen2020].
>
> H2-01:A-043 [quote: Answers as delivered] Weak for withheld-study (one study, one habitat).
>
> H2-01:A-053 [quote: Answers as delivered] Removing Chen2020 leaves no direct microbial test of functional covariation on held-out data.
>
> H2-01:A-111 [6. Answers by direction] One held-out-study test in the same habitat (human gut) found partial reproduction (59% of pathway co-abundances at P < 0.05).
>
> H2-01:C-013 [danger: Critic: answers partly supported] Withheld study, same habitat: one study (Chen2020, verified against full text).
>
> H2-01:C-014 [danger: Critic: answers partly supported] Of 37,106 testable pathway co-abundances from the IBD discovery cohort, 21,882 (59.0%) replicated at P < 0.05 in 77 iHMP-IBD individuals; for species the figure was 531 of 2,090 (25.4%).
>

## covariation-transfer.3 (claim)

Chen et al. attribute the low species replication rate largely to power, since 81.6% of species and 65.1% of pathway co-abundances showed no significant difference in strength between the two IBD cohorts.

- conf: not stated
- class: not stated
- holds: the two IBD cohorts (discovery and iHMP-IBD)
- src: chenGutMicrobialCoabundance2020
- trail: H2-01 §3.2

From the note:

> H2-01:B-0103 [3.2 Held-out study, same habitat (microbial, direct)] - Pathway co-abundances estimated in an IBD discovery cohort were tested in an independent IBD cohort (iHMP-IBD, 77 individuals).
>
> H2-01:B-0105 [3.2 Held-out study, same habitat (microbial, direct)] The authors attribute the low species rate largely to power, since 81.6% of species and 65.1% of pathway co-abundances showed no significant difference in strength between the two cohorts.
>

## covariation-transfer.4 (claim)

For the reductive TCA cycle pathway, 94.7% of 76 IBD-specific co-abundances replicated.

- conf: not stated
- class: not stated
- holds: the IBD discovery and iHMP-IBD cohorts, human gut
- src: chenGutMicrobialCoabundance2020
- trail: H2-01 §3.2

From the note:

> H2-01:B-0101 [3.2 Held-out study, same habitat (microbial, direct)] Human gut metagenomes from four cohorts (n = 2,379): 134 species and 343 MetaCyc pathways (HUMAnN2), SparCC combined with SPIEC-EASI to handle compositionality.
>
> H2-01:B-0103 [3.2 Held-out study, same habitat (microbial, direct)] - Pathway co-abundances estimated in an IBD discovery cohort were tested in an independent IBD cohort (iHMP-IBD, 77 individuals).
>
> H2-01:B-0106 [3.2 Held-out study, same habitat (microbial, direct)] - For the reductive TCA cycle pathway, 94.7% of 76 IBD-specific co-abundances replicated.
>

