# Dimensionality and cross-habitat stability of microbial functional profiles: writer's view

> [!abstract] About this view
> What the research found, for writing from. Each claim gives who found it, the setting it holds for, the kind of evidence, its standing where the research stated one, and for an absence whether it was searched for. A claim with no standing given has none stated in the research; "limited by access" means a source was not read in full, which is not the same as weak evidence. Sources are listed at the end. The view is generated from the knowledge note `Dimensionality and cross-habitat stability of microbial functional profiles.md`, where every claim is checked against the research.

## What the research found, by question

### H2-01

**D1. What has been measured about the dimensionality of functional profiles across samples, whether low or high relative to the number of functions measured, how was it estimated, and how does the estimate depend on normalisation, sparsity, presence against abundance data, gene sets that share members, and sample size?**

*Answer, as corrected by a second reader.*

Supported as written, with two corrections. First, the closing summary line 'Profiles appear dominated by a shared mean' goes further than the evidence. Sun2020 shows that a per-sample prediction-accuracy metric barely changes when genes are permuted across samples. HMP2012 reports that pathway levels vary less than taxa in the human body. Neither is a decomposition that measures how much of a sample-by-function matrix is a mean profile, and both come from human-associated and a few soil datasets. The body supports only this: in these datasets, per-sample functional profiles are highly similar to one another. Second, 'across genomes, metabolic presence/absence is high-dimensional' rests on one modelled study (Fahimipour2020), and 'low dimensionality holds for leading components within datasets' rests on one study (Heimberg2016). Both should be marked SINGLE SOURCE, as Lenz2016 is. All three direct microbial estimates (Jiang2012, Piton2023, Flinkstrom2024) are single studies fitted and scored on the same samples. No microbial study tested sensitivity to normalisation, sparsity, presence/absence against abundance, overlapping gene sets or sample size. The dependence on feature count and sample count is measured only for species-by-trait matrices (Mouillot2021, read by a search agent and not re-opened by the reviewer).

**D2. When covariation among functions is estimated in some habitats or studies and applied to a habitat or study not used in the estimate, does it reproduce, partly reproduce or fail to reproduce those profiles, and on what does that depend?**

*Answer, as corrected by a second reader.*

Withheld habitat, microbial function-function covariation: none found on the routes named. Withheld study, same habitat: one study (Chen2020, verified against full text). Of 37,106 testable pathway co-abundances from the IBD discovery cohort, 21,882 (59.0%) replicated at P < 0.05 in 77 iHMP-IBD individuals; for species the figure was 531 of 2,090 (25.4%). Other fields show partial transfer, each result from a single study. The body does not support the cross-field sentence 'transfer appears to depend on similarity between training and target, breadth of training, and shared mean structure' as a finding. It pools different quantities: covariance or dictionary transfer (Cleary2017, Pierson2015), taxon-to-gene mapping accuracy (Langille2013 NSTI), and phylogenetic gene gain/loss prediction (KonnoIwasaki2023). It should be labelled the reviewer's synthesis across incommensurable tests. Cleary2017's 87% to 68% is recovery of expression from 25 random composite measurements through a learned dictionary (compressed sensing). It is not a direct covariance-reproduction score, and the answer should say so.

**D3. Across habitats, how stable are covariation among functions, levels of individual functions, and taxonomic composition, each compared with the others in either direction, both where taxonomic composition turns over and where it does not?**

*Answer, as corrected by a second reader.* **D3 case A (levels vs composition, habitat fixed)**

Several studies report function levels more stable than composition. Two are full text (HMP2012, Burke2011); three rest on abstracts (Louca2016b, Shan2023, Aira2026). Contrary same-habitat evidence exists and is measured in full text, not only in the abstract-only Galand2018. Manor2017 (verified) found that revised processing (MUSiCC normalisation, filtering of prevalent families, non-uniform mapping) gave functional profiles that identified hosts as well as strain-level taxonomic markers did. The authors call perceived functional uniformity 'a potential misconception'. The single-source sensitivity statement that Galand2018 is 'the only direct same-habitat contrary result' is therefore wrong. The direction is best described as reported by several studies but dependent on processing, with direct measured contrary evidence in human gut (Manor2017) and coastal ocean (Galand2018, abstract).

*Answer, as corrected by a second reader.* **D3 case B/C (levels vs composition across habitats; taxonomy fixed)**

Case B is contested and incommensurable, as stated. The access labelling needs correcting. The decoupled side rests on Louca2016a (abstract only, taxonomy-derived function) and Nelson2016, which was read only through an automated summary with figures not re-verified. That is not full-text access, yet the answer lists it under 'Full text'. The coupled side's key figures (Fierer2012 Mantel r) were read in full text by only one angle and were not re-checked. Case C: no microbial study found on the named routes. Transplant, common-garden and single-lineage-across-habitat designs are not listed among the routes searched.

*Answer, as corrected by a second reader.* **D3 case D (covariation vs levels and composition)**

No microbial cross-habitat comparison was found. In one human gut study (Chen2020, verified), 64.3% of pathway co-abundances and 38.6% of species co-abundances differed in strength across four cohorts (Cochran's Q, FDR < 0.05). Among the entities involved in variable co-abundances, 84% of 304 pathways and also 76% of 100 species differed in level. The review reports only the pathway figure. The comparison contrasts pathway covariation with species covariation, not with composition. The cohorts differ in disease state and population, not habitat. Heterogeneity tests have more power for stronger and more numerous correlations, and that caution is not applied. The 99.6% one-year 'stability' is a count of non-significant differences at n = 77, the same lenient bar the review criticises for replication, so it should not be read as near-complete stability. Plant-trait evidence runs both ways, and each item is a single study.

## Concepts

In an order where each concept comes after the ones it builds on; the order means nothing more.

### the bodies of work that bear on the questions

- Three bodies of work bear on the questions: metagenomics supplies sample-by-function matrices (KEGG orthologues, pathways, modules, Pfams, eggNOG groups) from shotgun data; trait ecology supplies community-weighted means (CWMs) and species-by-trait matrices, mostly from plants; and other fields that profile many correlated features, chiefly transcriptomics, supply most of the explicit held-out tests of learned covariation. (the reviewer's account of the literature)
  Holds for: the review's account of the literature it covered.
- The three bodies have asked different questions: metagenomics has mostly compared levels of functions with taxonomic composition; trait ecology has asked about the dimensionality and covariation of traits, and sometimes how covariation shifts along gradients; transcriptomics has asked whether covariation learned in one tissue or study reproduces another. (the reviewer's account of the literature)
  Holds for: the review's account of the literature it covered.
- The core cases of the questions are thinly covered: most of the evidence is either direct evidence on a neighbouring quantity or evidence from another field, and each is labelled as such. (the reviewer's account of the literature)
  Holds for: the review's account of the literature it covered.
- A second reader judged the review careful on the whole: it labels most indirect evidence and keeps the core microbial cases (withheld habitat, cross-habitat covariation stability, case C) as not found. (the critic's assessment)
  Holds for: the critic's overall assessment of the review.

### a dominant shared mean profile

- Per-sample Spearman correlations between predicted and measured KEGG gene profiles (0.53 to 0.87) barely changed when each gene's abundance was permuted across samples (soil example: 0.85 unpermuted, 0.84 permuted); the authors conclude that functional profiles vary little between samples relative to their mean. (Sun et al. 2020)
  Holds for: a per-sample prediction-accuracy metric for predicted against measured KEGG gene profiles; the critic: not a decomposition that measures how much of a sample-by-function matrix is a mean profile, and from human-associated and a few soil datasets.
  Evidence: measured.
- The Human Microbiome Project consortium reports pathway relative abundances "much more constant and evenly diverse" than organismal abundances across individuals within body sites, with a stable housekeeping core. (The 2012)
  Holds for: human body sites (HMP); the critic: "much more constant" is a quoted descriptive statement with no quantitative figure, which the review treats as measured evidence of equal weight.
  Evidence: measured.
- In a reference network of 796 human-associated genomes by 7,105 KOs, a nested structure, with many KOs carried by most genomes, makes community functional profiles conserved even when taxa vary. (Tian et al. 2020)
  Holds for: a genome-content network model of human-associated genomes, offered as a mechanistic account.
  Evidence: derived and modelled; a single source.
- The review reads two findings (the permutation result for a per-sample accuracy metric and the HMP statement that pathways are more constant than taxa) as suggesting that much of the apparent low dimensionality of raw functional profiles is a shared mean; the critic holds that they support only this: in these datasets, per-sample functional profiles are highly similar to one another. (The 2012; Sun et al. 2020)
  Holds for: human-associated and a few soil datasets; neither finding is a decomposition that measures how much of a sample-by-function matrix is a mean profile.

### normalisation, genome size, gene-set aggregation and compositional closure

- Compositional data are proportions of some whole; their sample space is the simplex, and their statistical analysis has needed methods of its own. (Aitchison 1982)
  Background, not from the research.
- Relative (sum-to-one) normalisation introduces a sample-level factor shared by all genes. (the note cites no source for this sentence)
  Holds for: relative normalisation of functional profiles.
- The relative abundance of universal single-copy genes correlated with average genome size at R = −0.78 across HMP body sites and −0.82 in stool. (Manor and Borenstein 2015)
  Holds for: HMP body sites and stool.
  Evidence: measured.
- Species abundance explained 74% of average-genome-size variation across HMP samples, and genome-size variation makes genes at equal per-cell copy number look variable and hides real per-cell variation, so genome size makes stable genes look variable and variable genes look stable. (Nayfach and Pollard 2015)
  Holds for: HMP samples.
  Evidence: measured.
- In soils, genome size tracked the ratio of polysaccharide-decomposition to biomass-synthesis genes across 2,650 genomes and a continental survey. (Wu et al. 2025)
  Holds for: soil bacteria; 2,650 genomes and a continental survey.
- In HMP gut samples, single-copy-gene (marker-gene) normalisation raised pathway coefficients of variation relative to relative normalisation, uniform mapping of KOs shared among pathways gave less variable pathway profiles than a sample-specific mapping, and aggregating KOs into KEGG pathways lowered variability relative to aggregates built from genome co-occurrence. (Manor and Borenstein 2017)
  Holds for: HMP gut samples; across-sample variability of pathway profiles; the only measured test of aggregation and shared-member mapping.
  Evidence: measured; a single source.
- On average 9.5% of gene-family pairs within the same KEGG pathway were negatively correlated (R < −0.3). (Manor and Borenstein 2017)
  Holds for: HMP gut samples.
- Manor and Borenstein (2017) conclude that reported functional uniformity is partly a processing artefact, and call perceived functional uniformity "a potential misconception". (Manor and Borenstein 2017)
  Holds for: HMP gut samples.
- Naive mapping of a gene family to every pathway containing it inflates pathway counts. (Ye and Doak 2009)
  Holds for: pathway reconstruction, mapping gene families to pathways.
- In transcriptomics, pathways sharing genes shift each other's significance ("crosstalk"). (Donato et al. 2013)
  Holds for: pathway significance analysis in transcriptomics, another field.
- Correlation is not a valid association measure for relative data; proportionality is offered instead. (Lovell et al. 2015)
  Holds for: relative (compositional) data, from another field.

### community-weighted means and abundance weighting

- A community-weighted (community-aggregated) trait value weights each species' trait according to its relative abundance in the community. (Garnier et al. 2004)
  Background, not from the research.
- In trait ecology, CWMs all share the same abundance weights, so the composition matrix itself induces structure among CWMs. (the note cites no source for this sentence)
  Holds for: community-weighted means in trait ecology.
- CWM correlation tests have inflated error rates when only environment or only traits structure species distributions. (Peres-Neto et al. 2017)
  Holds for: CWM correlation tests; modelled.
  Evidence: modelled.
- The inflation of CWM correlation test error rates falls with compositional beta diversity and rises with sample size. (Zeleny 2018)
  Holds for: CWM correlation tests; modelled.
  Evidence: modelled.
- By analogy, community-aggregated functional profiles share weights in the same way as CWMs. (the reviewer's reading)
  Holds for: community-aggregated microbial functional profiles, by analogy with trait-ecology CWMs.
  Evidence: reading (note: "By analogy (reviewer's reading)").
- Abundance-weighted and unweighted trait moments disagreed in sign, significance or both for 71% of forest trait-climate results. (Wieczynski et al. 2019)
  Holds for: forest trait-climate results.
- CWM accuracy depended on trait coverage of the community. (Borgy et al. 2017)
  Holds for: plant community trait data.

### dimensionality of microbial sample-by-function profiles

Builds on: a dominant shared mean profile, normalisation, genome size, gene-set aggregation and compositional closure.

- Non-negative matrix factorization (NMF) decomposes a non-negative data matrix into non-negative parts whose constraints allow only additive, not subtractive, combinations. (Lee and Seung 1999)
  Background, not from the research.
- Few direct estimates of dimension exist for microbial sample-by-function matrices, and they use incompatible methods (NMF rank 5 for 8,214 Pfams in 45 ocean samples, two co-inertia axes carrying about half the variation in 128 soils, three KO clusters across 6,539 metagenomes); none uses a formal rank-selection rule (parallel analysis, cross-validated PCA or NMF, a random-matrix threshold) with stated n and p and tests how the estimate changes with processing. (Flinkstrom et al. 2024; Jiang et al. 2012; Piton et al. 2023)
  Holds for: microbial sample-level functional profiles; each direct estimate is a single study, fitted and scored on the same samples.
  Evidence: a single source; rated "Weak for the microbial sample-level question" by the research.
- Across 45 Global Ocean Sampling sites and 8,214 Pfam relative abundances, NMF was judged stable at rank 5 by a concordance criterion; no variance-explained figure was reported, the five components had "strikingly high" similarity to each other, a large ubiquitous, mostly primary-metabolism Pfam block loaded on all of them, and two components could not be interpreted. (Jiang et al. 2012)
  Holds for: ocean samples (Global Ocean Sampling sites), n = 45; fitted and scored on the same samples.
  Evidence: measured; a single source.
- Rank 5 is low relative to 8,214 features, but with n = 45 the rank cannot exceed 45, and much of the NMF fit is a shared mean-like profile. (Jiang et al. 2012)
  Holds for: the ocean NMF estimate (45 sites, 8,214 Pfams).
  Evidence: the reviewer's reading.
- In 128 soil metagenomes (global topsoil set) with KEGG, eggNOG, SEED, CAZy and genomic-trait tables (relative abundance normalised by annotated bacterial reads, log(x+1), z-scored), the first four multiple co-inertia axes captured 29%, 21%, 16% and 10% of variation, and the first axis tracked average genome size (R² = 0.64). (Piton et al. 2023)
  Holds for: soil metagenomes, community-aggregated traits; fitted and scored on the same samples; the only variance-explained figure for a microbial functional profile; the critic: full text "per angle" and not re-checked by the reviewer.
  Evidence: measured; a single source.
- Piton et al. call the soil co-inertia result a two-dimension "triangle" of life-history strategies, and warn that community-aggregated covariation does not show within-organism trade-offs and that only 5 to 15% of reads were annotated, with annotation coverage falling as genome size rose. (Piton et al. 2023)
  Holds for: 128 soil metagenomes.
- In the soil co-inertia result, two axes carry about half the variation; the other half is not low-dimensional on this evidence. (Piton et al. 2023)
  Holds for: 128 soil metagenomes.
  Evidence: the reviewer's reading.
- Across 6,539 IMG/M assembled metagenomes (KO abundances, KOs in under 10% of samples removed, CLR), bootstrapped k-means found three clusters (terrestrial, aquatic, anaerobic), strongly associated with assembly GC content; cluster number is not an intrinsic-dimension estimate and is a nearest precedent only. (Flinkstrom et al. 2024)
  Holds for: multi-biome assembled metagenomes; fitted and scored on the same samples.
  Evidence: measured; a single source.
- Across 25 GOS metagenomes, the first canonical correlation between KEGG module composition and environment was 0.944; with n = 25 and many modules, a high first canonical correlation on the same samples is expected, and it does not measure dimension. (Raes et al. 2011)
  Holds for: ocean metagenomes (GOS), n = 25.
  Evidence: measured.
- Gianoulis et al. (2009) define "metabolic footprints" by CCA on GOS. (Gianoulis et al. 2009)
  Holds for: GOS.
- Read literally, the direct estimates are low relative to the number of functions, but in each case n is small or only about half the variance is in the leading axes, and the leading structure is partly a shared mean profile (evidence the critic reads as showing only that per-sample profiles are highly similar in these datasets) or a genome-size axis (Piton axis 1 against genome size R² 0.64; genome size and normalisation effects). (Flinkstrom et al. 2024; The 2012; Jiang et al. 2012; Manor and Borenstein 2015; Nayfach and Pollard 2015; Piton et al. 2023; Sun et al. 2020)
  Holds for: the three direct microbial estimates.
- No microbial study was found that re-estimated the dimension of functional profiles under different normalisations, sparsity filters, presence/absence against abundance, overlapping gene sets or sample sizes; none tested sensitivity to these choices with a formal rank rule and stated n and p. (a search result)
  Holds for: microbial sample-by-function profiles; the review's search routes.
  Evidence: a search result.
  Searched for and not found.
- What is measured is that processing choices change across-sample variance and covariance (normalisation, genome size, pathway aggregation, compositional closure), which a dimension estimate would inherit; that these shifts lower apparent dimension is the reviewer's inference, so the evidence is only indirect for dimension. (Lovell et al. 2015; Manor and Borenstein 2017; Ye and Doak 2009)
  Holds for: microbial functional profiles; indirect for dimension.
  Evidence: the reviewer's reading.
- At least one leading axis of many functional-profile decompositions may be a genome-size or normalisation axis; the first Piton axis (R² = 0.64 with genome size) is consistent with this. This is an inference, not a measured decomposition. (Piton et al. 2023)
  Holds for: functional-profile decompositions.
  Evidence: the reviewer's reading.
- None of the gene-set studies measures a covariance matrix between overlapping gene sets; that shared members inflate pathway-pathway covariance, and so lower apparent dimension, is the reviewer's inference. (Donato et al. 2013; Manor and Borenstein 2017; Ye and Doak 2009)
  Holds for: pathway profiles built from gene sets that share members.
  Evidence: the reviewer's reading.
- Whether a dimension estimate is taken before or after centring on the shared mean profile will change it; no microbial study found reports both. (the reviewer's statement and a search result)
  Holds for: microbial functional profiles.
  Evidence: a search result.
  Searched for and not found.
- No held-out (cross-validated) rank estimate has been measured for functional profiles. (a search result)
  Holds for: microbial functional profiles.
  Evidence: a search result.
  The research does not say whether this was searched for.
- Dimension has not been compared by habitat; no search route targeted habitat-stratified decompositions (for example the per-biome NMF or PCA in multi-biome metagenome atlases). (a search result)
  Holds for: microbial functional profiles.
  Evidence: a search result.
  Not searched for.

### dimensionality of genomes, trait databases and transcriptomes

Builds on: dimensionality of microbial sample-by-function profiles.

- Across 2,621 bacterial genera, diffusion maps on presence/absence of 7,769 substrate-product traits found no single low-dimensional space but crossing low-dimensional manifolds with "dozens or possibly hundreds of meaningful coordinates". (Fahimipour and Gross 2020)
  Holds for: genomes as rows (genera), not samples; presence/absence; one modelled study.
  Evidence: modelled; a single source.
- A review names three main axes of quantitative bacterial traits (growth rate with rRNA copy number, genome size with signal transduction, cell size) and notes that quantitative traits vary widely within substrate-use pathways. (Westoby et al. 2021)
  Holds for: quantitative bacterial and archaeal traits.
  Evidence: asserted.
- The genome diffusion-map result and the three-axis trait review are not in conflict: they describe different trait sets, and together they bound any claim that "microbial function" has one dimensionality. (Fahimipour and Gross 2020; Westoby et al. 2021)
  Holds for: bacterial trait sets across genomes.
- Across 30 species-by-trait datasets, the median dimension was 4 by an elbow rule (range 2 to 8) and 6 by an AUC threshold of 0.7 (range 2 to 17), and the two estimates were only weakly correlated. (Mouillot et al. 2021)
  Holds for: species trait databases (species as rows, not samples).
  Evidence: measured.
- In species trait databases, threshold dimensionality rose with the log number of traits and fell with mean trait correlation (GLM R² = 0.61); in simulations, species number mattered only below about 100 to 200 species, and dropping half the traits lost much quality. (Mouillot et al. 2021)
  Holds for: species-by-trait datasets and simulations.
- The species-trait study is the only source found that measures how a dimension estimate depends on the number of features, feature correlation and sample count; it concerns species-level traits, not sample-level profiles, from another setting. (Mouillot et al. 2021)
  Holds for: species-by-trait matrices; the critic: read by a search agent and not re-opened by the reviewer, full text "per angle" and not re-checked.
  Evidence: a single source.
- Plant traits showed at most six dimensions in the largest of three datasets. (Laughlin 2014)
  Holds for: plant trait datasets.
- Two components explain 74% of six key plant traits across 2,214 species. (Bruelheide et al. 2018)
  Holds for: plant species traits; secondary, via Bruelheide2018.
- With 17 gap-filled traits across more than 20,000 plant species, PC1 explained 33%, PC2 15% and PC3 9.4%. (Joswig et al. 2022)
  Holds for: plant species, gap-filled trait matrix.
- The trait gap-filling method BHPMF imputes from trait-trait correlations. (Schrodt et al. 2015)
  Holds for: plant trait gap-filling.
- Because BHPMF imputes from trait-trait correlations, covariation in imputed trait matrices is partly built in. (Schrodt et al. 2015)
  Holds for: gap-filled plant trait matrices.
  Evidence: the reviewer's reading.
- Across 352 microarray datasets, the first principal value averaged about twice the second, the first five explained most variance, and per-gene shuffling removed this; the authors call low dimensionality fundamental. (Heimberg et al. 2016)
  Holds for: gene expression microarray datasets, another field; within datasets.
  Evidence: measured; a single source.
- In large heterogeneous expression compendia (5,372 and 7,100 samples), the first three PCs explained about 36% of variance, components beyond the third were unstable between datasets, the residual space carried most tissue-specific signal, and PCA depended on the fraction of samples carrying a signal. (Lenz et al. 2016)
  Holds for: gene expression compendia, another field; across datasets.
  Evidence: measured; a single source.
- In gene expression, "low-dimensional" holds for leading components within a dataset and weakens when dimension is judged by reproducibility across datasets or by information in the residual. (Heimberg et al. 2016; Lenz et al. 2016)
  Holds for: transcriptomics, another field; the within-dataset side rests on one study and the across-dataset side on one study.
  Evidence: a single source.
- Low dimension estimates (Jiang2012, Piton2023's two leading axes, Heimberg2016) stand against higher ones (Fahimipour2020 across genomes; Lenz2016 across datasets; Piton's remaining half of variance); these largely reflect different objects (samples against genomes) and different criteria (within-dataset variance against cross-dataset stability), not direct contradiction on the same data. (Fahimipour and Gross 2020; Heimberg et al. 2016; Jiang et al. 2012; Lenz et al. 2016; Piton et al. 2023)
  Holds for: the D1 sources taken together.

### held-out transfer of microbial functional covariation

- No study was found that fitted covariation among microbial functions (a covariance or correlation matrix, a factorisation, a network, or a regression of some functions on others) in a set of habitats and scored it on a withheld habitat; this is a statement about the routes searched, not a statement that the literature lacks such a study. (a search result)
  Holds for: microbial function-function covariation; withheld habitat; routes: Europe PMC, PubMed and PMC E-utilities, Crossref, Semantic Scholar, OpenAlex, Unpaywall and known literature, with WebSearch and Scholar Gateway unavailable.
  Evidence: a search result; rated "Absent for the withheld-habitat microbial case" by the research.
  Searched for and not found.
- Pathway co-abundances estimated in an IBD discovery cohort were tested in an independent IBD cohort (iHMP-IBD, 77 individuals): of 37,106 testable pathway co-abundances, 21,882 (59.0%) replicated at P < 0.05; of 2,090 species co-abundances, 531 (25.4%), so pathway co-abundances partly reproduced. (Chen et al. 2020)
  Holds for: human gut metagenomes from four cohorts (n = 2,379), 134 species and 343 MetaCyc pathways (HUMAnN2), SparCC combined with SPIEC-EASI; the withheld unit is a study within the same habitat and disease state, not a habitat; the only direct microbial test of functional covariation on held-out data.
  Evidence: measured; a single source; rated "Weak for withheld-study (one study, one habitat)" by the research.
- Chen et al. attribute the low species replication rate largely to power, since 81.6% of species and 65.1% of pathway co-abundances showed no significant difference in strength between the two IBD cohorts. (Chen et al. 2020)
  Holds for: the two IBD cohorts (discovery and iHMP-IBD).
- For the reductive TCA cycle pathway, 94.7% of 76 IBD-specific co-abundances replicated. (Chen et al. 2020)
  Holds for: the IBD discovery and iHMP-IBD cohorts, human gut.
- MetaCyc pathways share reactions and contributing species, so pathway-pathway co-abundance partly reflects shared members; 43,355 of about 58,653 possible pathway pairs were significant in at least one cohort, which points to strong common factors that would make replication easy; and "replicated at P < 0.05" with n = 77 is a lenient bar, so the 59% is an optimistic reading of transfer. (Chen et al. 2020)
  Holds for: the IBD replication test.
  Evidence: reading (note: "Cautions (reviewer's reading)").
- No held-out test has used presence/absence profiles or compared annotation schemes. (a statement of what was not measured)
  Holds for: microbial functional profiles in a held-out design.
  Evidence: a search result.
  The research does not say whether this was searched for.
- No held-out test has been made in soils, oceans or other non-human habitats at all. (a statement of what was not measured)
  Holds for: held-out tests of microbial functional profiles.
  Evidence: a search result.
  The research does not say whether this was searched for.

### transfer of taxon-to-function mappings, classifiers and gene co-occurrence

Builds on: a dominant shared mean profile.

- PICRUSt accuracy fell with distance to the nearest reference genome (NSTI), across all samples (r = −0.4) and within each habitat (r = −0.25 to −0.82); accuracy was high in soils (0.81) and low in a hypersaline mat (reported 0.25, mean NSTI 0.23). (Langille et al. 2013)
  Holds for: a genome-derived taxon-to-gene mapping transferred across habitats, not covariation among functions.
  Evidence: measured.
- The per-sample Spearman metric is almost insensitive to permuting genes across samples, and inference-level agreement of metagenome prediction tools was reasonable in human datasets and much lower in non-human and soil datasets. (Sun et al. 2020)
  Holds for: human, non-human and soil datasets; a taxon-to-gene mapping, not covariation among functions.
- These mapping results suggest that taxon-to-function mappings transfer less well as reference coverage of the target habitat falls. (Langille et al. 2013; Sun et al. 2020)
  Holds for: taxon-to-function mappings, a quantity other than function-function covariation.
- Colorectal cancer classifiers on eggNOG groups gave AUROC 0.70 to 0.81 study-to-study and 0.78 to 0.89 leave-one-study-out, similar to species-level classifiers. (Wirbel et al. 2019)
  Holds for: human gut only; a classifier, not a covariance structure.
  Evidence: measured.
- In the E. coli pangenome, accessory-gene presence was predicted from other accessory genes on held-out random genomes; after filtering and removing phylogenetic signal, 16.7% of families were predictable at F1 ≥ 0.9 against a chance rate of about 1 to 1.7%. (Beavan et al. 2024)
  Holds for: gene co-occurrence across genomes of the E. coli pangenome, not across samples.
  Evidence: a single source.
- Across about 3,000 genomes, gene gain and loss in metabolic pathways was predictable in a hold-one-phylum-out test for each of the 10 largest phyla, with predictability differing significantly among phyla. (Konno and Iwasaki 2023)
  Holds for: about 3,000 bacterial genomes; phylogenetic gene gain/loss prediction in metabolic pathways.
  Evidence: modelled; a single source.
- Gene content predicted MAG niche position along Baltic Sea gradients better than phylogeny under genome-level cross-validation. (Alneberg et al. 2020)
  Holds for: Baltic Sea metagenome-assembled genomes.
- Phylogenetic-profile co-occurrence recovered same-pathway enzyme pairs better than homology, in a benchmark partly circular with KEGG membership. (Chung et al. 2024)
  Holds for: a benchmark partly circular with KEGG membership.
- A low-dimensional gene-to-function map transferred from strains to communities for denitrification. (Gowda et al. 2022)
  Holds for: denitrification.
- Five "generalizable" enterosignatures were found from 5,230 gut metagenomes; what "generalizable" means (the held-out design) was not read. (Frioux et al. 2023)
  Holds for: human gut metagenomes; taxonomic low-rank structure.
  Evidence: limited by access (a source was not read in full; not the same as weak evidence).

### held-out covariation tests in transcriptomics and plant traits

- Sparse module dictionaries learned on 5% of samples of a TCGA tumour type gave about 87% recovery (Spearman, SMAF) within the same tumour type, and a dictionary from a different tumour type gave 68% on average, with related tumour types doing better; these figures are Spearman recovery of expression from 25 simulated random composite measurements through the dictionary (compressed sensing, m = 25, g = 5,000), not a direct covariance-reproduction score. (Cleary et al. 2017)
  Holds for: TCGA tumour types, transcriptomics; a withheld tissue type, the closest other-field analogue of a withheld habitat; the authors warn a dictionary is biased when training data do not represent the test data.
  Evidence: measured; a single source.
- A linear model from about 1,000 landmark genes, trained on GEO microarrays, inferred 81% of non-measured transcripts well in independent GTEx RNA-seq (8,555 samples); about 19% were not well inferred. (Subramanian et al. 2017)
  Holds for: transcriptomics; a withheld study and platform.
  Evidence: measured; a single source.
- A single co-expression network fitted to all 35 GTEx tissues pooled had held-out likelihood so low it was dropped from the comparison; per-tissue networks did better, and sharing between related tissues did better again, so pooled networks represented individual tissues poorly. (Pierson et al. 2015)
  Holds for: 35 GTEx human tissues; samples, not tissues, were withheld.
  Evidence: measured; a single source.
- Individual co-expression networks predicted GO membership with mean AUROC 0.60 (bulk) and 0.56 (single cell), aggregating 163 networks reached 0.73 (bulk), and sample size did not predict performance, so individual co-expression networks replicate modestly. (Crow et al. 2016)
  Holds for: co-expression networks, bulk and single-cell expression.
  Evidence: measured.
- A latent space learned on recount2 was concordant with dataset-specific models in rare-disease studies, with broader training capturing more pathways. (Taroni et al. 2019)
  Holds for: transcriptomics, rare-disease studies; qualitative.
- projectR tests whether a pattern is shared by projection; it is a framework and reports no failure rate. (Stein-O'Brien et al. 2019)
  Holds for: a projection framework for transfer learning across cellular measurements.
- Global leaf-economics correlations may not hold at local scales, since correlation strength only bounds how differently traits can vary across scales. (Messier et al. 2017)
  Holds for: plant leaf traits; transfer across scale, not across habitat.
- Some leaf-trait correlations reverse sign within species compared with across species. (Anderegg et al. 2018)
  Holds for: plant leaf traits; transfer across taxonomic level, not across habitat.
- In other fields, covariation transfers partly, each result from a single study. (Cleary et al. 2017; Crow et al. 2016; Pierson et al. 2015; Subramanian et al. 2017)
  Holds for: transcriptomics and other fields, not microbial.
  Evidence: a single source; rated "Moderate for partial transfer in transcriptomics, but that is another field and each quantitative result is a single study" by the research.
- There is no direct conflict on the same quantity: reproduction is high in some tests (Subramanian's 81%; Chen's reductive TCA cycle at 94.7%) and low in others (Cleary's cross-type drop; pooled networks in Pierson; sign reversals across scales in plant traits). (Anderegg et al. 2018; Chen et al. 2020; Cleary et al. 2017; Pierson et al. 2015; Subramanian et al. 2017)
  Holds for: the held-out tests across fields.

### what transfer appears to depend on

Builds on: held-out transfer of microbial functional covariation, transfer of taxon-to-function mappings, classifiers and gene co-occurrence, held-out covariation tests in transcriptomics and plant traits, dimensionality of genomes, trait databases and transcriptomes.

- The review's synthesis is that, across the other-field and neighbouring evidence, transfer appears to depend on the similarity of the training set to the target (related tumour types; related tissues; NSTI; phylum differences), the breadth of the training set, and the fraction of the target that is shared mean structure against target-specific signal; the critic holds that this pools incommensurable tests of different quantities (covariance or dictionary transfer, taxon-to-gene mapping accuracy, per-sample accuracy metrics, phylogenetic gene gain/loss prediction) and is the reviewer's synthesis, not a finding. (the reviewer's synthesis)
  Holds for: each dependency rests on one to three sources measuring different quantities, breadth on one qualitative study alone; none of these dependencies has been measured for microbial function-function covariation across habitats.
  Evidence: the reviewer's reading.

### function levels against taxonomic composition within a habitat (case A)

Builds on: a dominant shared mean profile, normalisation, genome size, gene-set aggregation and compositional closure.

- Within a habitat where taxonomy turns over, several studies report function levels more stable than taxonomic composition (HMP pathways against organisms; bromeliad microcosms; macroalgal host COGs against species; soil microcosm functional groups; vermicomposting turnover rates), two in full text and three resting on abstracts; the direction is best described as reported by several studies but dependent on processing, with direct measured contrary evidence in human gut and coastal ocean. (Aira et al. 2026; Burke et al. 2011; Galand et al. 2018; The 2012; Louca et al. 2016; Manor and Borenstein 2017; Shan et al. 2023)
  Holds for: habitat held roughly fixed; none of the studies controls for normalisation, aggregation and granularity together.
  Evidence: rated "Moderate for the direction as reported, weak for the claim that the stability is biological rather than processing-driven" by the research.
  A second reader found the search for contrary evidence one-sided.
- Bromeliad tank microcosms showed similar functional-group structure across replicates and highly variable taxonomy within groups. (Louca et al. 2016)
  Holds for: bromeliad tank microcosms.
  Evidence: measured.
- On a macroalgal host, species composition was about 15% similar against 70% similarity in COG composition; the contrast compares a species table with a coarser COG table, and the taxonomic figure is from an earlier study. (Burke et al. 2011)
  Holds for: bacterial communities on a macroalgal host.
  Evidence: measured.
- In replicate soil microcosms, annotation-free functional groups were stable in summed abundance despite large variation in species composition. (Shan et al. 2023)
  Holds for: replicate soil microcosms.
- During vermicomposting, taxonomic turnover over time was about twelve times functional turnover. (Aira et al. 2026)
  Holds for: vermicomposting over time; no non-earthworm control.
- A model found taxa-function robustness higher in gut than in vaginal communities, so how far function tracks taxonomy may itself vary by habitat. (Eng and Borenstein 2018)
  Holds for: one modelled, abstract-only study comparing gut and vaginal communities.
  Evidence: modelled; a single source.
- Within the human gut, how consistently genera carry metabolic modules differs among genera, and module-derived redundancy was lower in the Bacteroides enterotype. (Vieira-Silva et al. 2016)
  Holds for: human gut.
- In a coastal Mediterranean time series, Galand et al. (2018) report a strong taxonomy-function link when function is measured from all reads or all predicted genes, and weaker links with annotated orthologues or taxonomy-inferred functions, and conclude that this challenges functional redundancy; the abstract is explicit that using all reads, not annotated genes, was essential. (Galand et al. 2018)
  Holds for: coastal Mediterranean time series; the reported R² values came from an automated summary and are not used.
  Evidence: limited by access (a source was not read in full; not the same as weak evidence).
- Revised processing (MUSiCC normalisation, filtering of prevalent families, non-uniform mapping) gave functional profiles that identified hosts as well as strain-level taxonomic markers did: a direct, measured same-habitat counter-result to functional stability. (Manor and Borenstein 2017)
  Holds for: human gut; verified against full text by the critic.
  Evidence: measured.
- The counter-evidence within a habitat is methodological and applies to every study above: relative normalisation and pathway aggregation reduce apparent functional variability, genome size creates both spurious variability and spurious stability, and a dominant mean profile makes profiles look alike, so the "levels stable, taxonomy variable" pattern depends on processing and annotation scheme. (Manor and Borenstein 2015; Manor and Borenstein 2017; Nayfach and Pollard 2015; Sun et al. 2020)
  Holds for: same-habitat comparisons of function levels and taxonomic composition.
- Comparing a fine taxonomic table with a coarse functional table favours functional stability by construction, which applies equally to Burke2011 and Ramírez-Flandes2019. (Burke et al. 2011; Ramirez-Flandes et al. 2019)
  Holds for: comparisons of tables at different granularity.
  Evidence: the reviewer's reading.
- Same-habitat comparisons using marker-normalised, unaggregated or all-read functional profiles alongside taxonomy at matched resolution have not been measured, nor have non-human habitats beyond a few microcosm and marine examples; none of the studies controls for normalisation, aggregation and granularity together. (a statement of what was not measured)
  Holds for: function levels against taxonomic composition within a habitat.
  Evidence: a search result.
  The research does not say whether this was searched for.

### function levels against taxonomic composition across habitats (case B)

Builds on: normalisation, genome size, gene-set aggregation and compositional closure.

- Across habitats where taxonomy turns over, whether function tracks taxonomic composition is contested and incommensurable: the coupled and decoupled results use different function definitions (all reads or gene categories against taxonomy-derived groups) and different comparisons (distance-matrix correlation against variance partitioning), and cannot be pooled; the answer depends on annotation and resolution. (Fierer et al. 2012; Louca et al. 2016; Nelson et al. 2016; Salazar et al. 2019)
  Holds for: several measured studies in each direction, not commensurable, several single studies or abstract only.
  Evidence: contested; rated "Weak to moderate" by the research.
- Across 16 soils from five biomes, functional and taxonomic Bray-Curtis distances correlated (Mantel r = 0.76; with unweighted UniFrac, 0.82). (Fierer et al. 2012)
  Holds for: 16 soils from five biomes; small n; the coupled side of case B, which without this study would rest on one global ocean statement.
  Evidence: measured; limited by access (a source was not read in full; not the same as weak evidence).
- In Tara Oceans, OG-level metagenomic and metatranscriptomic differentiation tracked taxonomic differentiation along latitude, and the authors conclude that "on a global scale, taxonomic composition largely shapes the composition of gene functional content". (Salazar et al. 2019)
  Holds for: global ocean (Tara Oceans); the critic: taxonomic and OG profiles come from the same reads and share compositional structure, which the review does not note.
  Evidence: measured.
  A second reader found the search for contrary evidence one-sided.
- A CCA on phylogenetic composition agreed with functional trends across GOS. (Raes et al. 2011)
  Holds for: GOS ocean metagenomes.
- Across 247 metagenomes from 18 biomes, function separated biomes more strongly than taxonomy: oxidoreductase profiles gave PERMANOVA F = 12.5 and all 6,789 KOs F = 10.7, against 1.8 for 4,011 species and 2.8 at fourth taxonomic rank, and functional and taxonomic diversity rankings of biomes did not correspond; the feature sets differ in size and sparsity, so the F statistics are not commensurable. (Ramirez-Flandes et al. 2019)
  Holds for: 247 metagenomes from 18 biomes; bears on which separates habitats more, a different question from coupling.
  Evidence: measured; a single source.
- Nine biomes were strongly discriminated by metabolic profiles. (Dinsdale et al. 2008)
  Holds for: metagenomes from nine biomes.
- In the global ocean, environment strongly shaped functional-group distribution and weakly shaped taxonomy within groups, "roughly independent axes of variation". (Louca et al. 2016)
  Holds for: global ocean; derived, because functional groups were assigned from taxonomy; one of the two studies on the decoupled side of case B.
  Evidence: derived.
- Soil nitrogen-pathway frequencies were explained by habitat and soil C and N, while taxonomy within N functional groups was poorly predicted by environment. (Nelson et al. 2016)
  Holds for: soils; one of the two studies on the decoupled side of case B.
  Evidence: limited by access (a source was not read in full; not the same as weak evidence).
- At 95%-identity gene resolution, most genes were specific to one of 14 habitats. (Coelho et al. 2022)
  Holds for: prokaryotic genes at 95% identity across 14 habitats.
- At the level of core OG functions, more than 73% of ocean core-function abundance was shared with the human gut. (Sunagawa et al. 2015)
  Holds for: ocean and human gut metagenomes.
- Resolution decides much of the coupling question: the same data can support turnover or constancy depending on resolution. (Coelho et al. 2022; Sunagawa et al. 2015)
  Holds for: comparisons of function and taxonomy across habitats.
- Case B has not been measured with taxonomy and function at matched resolution and matched feature counts, or with marker-normalised functional profiles. (a statement of what was not measured)
  Holds for: function levels against taxonomic composition across habitats.
  Evidence: a search result.
  The research does not say whether this was searched for.

### function levels where habitat changes but taxonomy does not (case C)

- No microbial metagenomic study was found that holds taxonomy fixed while habitat varies and compares function levels. (a search result)
  Holds for: the review's search routes; the critic: transplant, common-garden and single-lineage-across-habitat designs are not listed among the routes searched.
  Evidence: a search result; rated "Case C: absent" by the research.
  Searched for and not found.
- Salazar et al. (2019) separate regulatory change (metatranscriptome) from community turnover in the ocean; per the search agent's reading, turnover dominated at global scale. This is the nearest item to case C and concerns expression, not gene content. (Salazar et al. 2019)
  Holds for: global ocean metatranscriptomes.

### stability of functional covariation against levels and composition (case D)

Builds on: held-out transfer of microbial functional covariation, community-weighted means and abundance weighting.

- No microbial study was found that compares the between-habitat stability of function-function covariation with that of function levels or taxonomic composition. (a search result)
  Holds for: microbial metagenomes; search routes as for withheld habitats.
  Evidence: a search result; rated "Absent for the microbial cross-habitat case" by the research.
  Searched for and not found.
- Across four human gut cohorts that differ in disease state and population (IBD, obesity, two population cohorts), 64.3% of pathway co-abundances and 38.6% of species co-abundances differed in strength (Cochran's Q, FDR < 0.05): in this setting pathway covariation was less stable across cohorts than species covariation. This compares functional covariation with taxonomic covariation, not with taxonomic composition, and the cohorts differ in disease state and population, not habitat. (Chen et al. 2020)
  Holds for: one human gut study, one heterogeneity test; the closest microbial evidence and the only microbial measurement of functional covariation stability; shared-member and common-factor cautions apply; the critic: heterogeneity tests have more power for stronger and more numerous correlations, and pathway correlations are stronger and more numerous, so easier to detect as heterogeneous.
  Evidence: a single source; rated "Weak (one study) for the microbial between-cohort case" by the research.
  A second reader found the search for contrary evidence one-sided.
- Among the entities involved in variable co-abundances across the four gut cohorts, 84% of 304 pathways and also 76% of 100 species differed in level; the review reported only the pathway figure, which makes the pathway result look more distinctive than it is. (Chen et al. 2020)
  Holds for: four human gut cohorts differing in disease state.
  A second reader found the search for contrary evidence one-sided.
- Outside that study, covariation among microbial functions has only been fitted on pooled cross-habitat data, not compared between habitats; none of the pooled studies measures whether the covariation differs by habitat. (Barberan et al. 2012; Gianoulis et al. 2009; Nelson et al. 2016; Salazar et al. 2019)
  Holds for: microbial functional covariation.
- Soil nitrogen-pathway frequencies were "overwhelmingly positively correlated" across 365 soils from 10 habitat types. (Nelson et al. 2016)
  Holds for: 365 soils from 10 habitat types, pooled.
- Co-abundance and co-expression of ocean OGs predicted shared KEGG membership, fitted and scored on the same samples and partly circular. (Salazar et al. 2019)
  Holds for: global ocean, pooled; fitted and scored on the same samples.
- Amino-acid transport and cofactor synthesis covaried in GOS metagenomes. (Gianoulis et al. 2009)
  Holds for: GOS ocean metagenomes, pooled.
- Community genomic traits covaried in microbial metagenomes, some of the covariation possibly technical in origin. (Barberan et al. 2012)
  Holds for: microbial metagenomes, pooled.
- Community-weighted plant traits across 1.1 million plots showed the same two covariation axes as species-level traits, "unexpected" per the authors, while climate and soil explained only 10.8 to 14.0% of CWM variation: covariation more stable than levels. (Bruelheide et al. 2018)
  Holds for: plant communities (other field); the only large-scale case of covariation more stable than levels.
  Evidence: measured; a single source.
- Precision-matrix plant trait networks differed among climate regions in density and modularity, with some edges present everywhere and others region-specific. (Flores-Moreno et al. 2019)
  Holds for: plant traits (other field); heavy imputation.
- Leaf-economic slopes shifted with climate. (Wright et al. 2005)
  Holds for: plant leaf traits (other field).
- Along an aridity gradient, a height-seed mass covariance strengthened while level-type functional diversity was poorly explained by aridity. (Dwyer and Laughlin 2017)
  Holds for: plant communities along an aridity gradient (other field).
  Evidence: a single source.
- A review reports plant trait-network topology shifting along resource gradients. (He et al. 2020)
  Holds for: plant trait networks (other field).
  Evidence: asserted.
- In plant traits, the evidence on whether covariation is more stable than levels runs both ways, and each item is a single study; the plant sources differ in level (community against species), in imputation and in gradient. (Bruelheide et al. 2018; Dwyer and Laughlin 2017; Flores-Moreno et al. 2019; Wright et al. 2005)
  Holds for: plant traits, another field; each item a single study.
  Evidence: rated "Mixed and other-field for plant traits and expression" by the research.
- Tissue-specific co-expression networks outperformed pooled ones, and modules conserved across tissues carried shared housekeeping functions. (Pierson et al. 2015)
  Holds for: human tissues, transcriptomics (other field).
  Evidence: a single source.
- Covariation in presence/absence profiles, and comparison corrected for shared gene-set members, have not been measured across habitats. (a statement of what was not measured)
  Holds for: microbial functional covariation.
  Evidence: a search result.
  The research does not say whether this was searched for.

### temporal stability of functional covariation

Builds on: held-out transfer of microbial functional covariation.

- Between the first and last iHMP-IBD time points, about one year apart, 90.6% of species and 99.6% of pathway co-abundances showed no significant difference in strength (Cochran's Q, P > 0.05) in 77 individuals; this is a count of non-significant differences, an absence-of-evidence count at the same lenient bar the review criticises for replication, and should not be read as near-complete stability. (Chen et al. 2020)
  Holds for: one IBD cohort (iHMP-IBD), human gut, n = 77; the only microbial measurement.
  A second reader found the search for contrary evidence one-sided.
- The review found no trait-ecology study of temporal CWM covariation; the critic notes that plant CWM time series were not searched and that the statement names no routes. (a search result)
  Holds for: trait ecology.
  Evidence: a search result.
  Not searched for.

### what counts as a function, and failure modes

Builds on: dimensionality of microbial sample-by-function profiles, dimensionality of genomes, trait databases and transcriptomes, function levels against taxonomic composition within a habitat (case A), function levels against taxonomic composition across habitats (case B), held-out covariation tests in transcriptomics and plant traits.

- The reviewer's synthesis is that the answer to every direction depends on what is treated as "a function": coarse, aggregated, relatively normalised functions look stable, and fine, marker-normalised or all-read functions look more tied to taxonomy, with the measured pieces each a single study for its specific quantity; that they also differ in dimension (coarse functions looking low-dimensional, fine ones higher-dimensional) is the reviewer's inference, which no cited source measured. (Coelho et al. 2022; Galand et al. 2018; Manor and Borenstein 2015; Manor and Borenstein 2017; Nayfach and Pollard 2015; Sun et al. 2020)
  Holds for: the measured pieces cover annotation granularity, normalisation, mapping and all-read comparison; none of them measured dimension.
  Evidence: the reviewer's reading; a single source.
- In transcriptomics, low dimensionality within datasets coexists with unstable higher components across datasets and partial transfer across tissue types, which the review reads as the same pattern. (Cleary et al. 2017; Heimberg et al. 2016; Lenz et al. 2016)
  Holds for: transcriptomics, another field.
- Failure modes to expect in this literature are dimension estimates dominated by a mean profile; a genome-size axis that is partly technical; covariation between gene sets that share members; per-sample correlation metrics that ignore across-sample variance; comparisons of tables at different granularity; covariation inherited from imputation (plant traits); and replication judged against lenient thresholds with strong common factors. (Chen et al. 2020)
  Holds for: the literature the review covered.

## Do not say

Wordings the research itself says are wrong or overstated, each with the reason and what to say instead.

- Do not write: "Microbial functional profiles are dominated by a shared mean, while across genomes metabolic content is high-dimensional."
  Why: The evidence is a per-sample accuracy metric under permutation and descriptive HMP statements from human-associated and a few soil datasets, not a decomposition of a sample-by-function matrix, and the sentence merges sample-level functional profiles, genome-level presence/absence and a per-sample accuracy metric into one characterisation of "functional profiles".
  Say instead: The review reads two findings (the permutation result for a per-sample accuracy metric and the HMP statement that pathways are more constant than taxa) as suggesting that much of the apparent low dimensionality of raw functional profiles is a shared mean; the critic holds that they support only this: in these datasets, per-sample functional profiles are highly similar to one another. (The 2012; Sun et al. 2020)
  Holds for: human-associated and a few soil datasets; neither finding is a decomposition that measures how much of a sample-by-function matrix is a mean profile.
  Say instead: Across 2,621 bacterial genera, diffusion maps on presence/absence of 7,769 substrate-product traits found no single low-dimensional space but crossing low-dimensional manifolds with "dozens or possibly hundreds of meaningful coordinates". (Fahimipour and Gross 2020)
  Holds for: genomes as rows (genera), not samples; presence/absence; one modelled study.
  Evidence: modelled; a single source.
- Do not write: "Across genomes, metabolic presence/absence is high-dimensional, with dozens to hundreds of coordinates."
  Why: This rests on one modelled study (diffusion maps across genera) and is phrased as a property of genomes in general.
  Say instead: Across 2,621 bacterial genera, diffusion maps on presence/absence of 7,769 substrate-product traits found no single low-dimensional space but crossing low-dimensional manifolds with "dozens or possibly hundreds of meaningful coordinates". (Fahimipour and Gross 2020)
  Holds for: genomes as rows (genera), not samples; presence/absence; one modelled study.
  Evidence: modelled; a single source.
- Do not write: "Gene expression data are low-dimensional within datasets."
  Why: The within-dataset result rests on one study that the review did not flag SINGLE SOURCE while flagging the opposing study; the labelling is asymmetric.
  Say instead: Across 352 microarray datasets, the first principal value averaged about twice the second, the first five explained most variance, and per-gene shuffling removed this; the authors call low dimensionality fundamental. (Heimberg et al. 2016)
  Holds for: gene expression microarray datasets, another field; within datasets.
  Evidence: measured; a single source.
  Say instead: In gene expression, "low-dimensional" holds for leading components within a dataset and weakens when dimension is judged by reproducibility across datasets or by information in the residual. (Heimberg et al. 2016; Lenz et al. 2016)
  Holds for: transcriptomics, another field; the within-dataset side rests on one study and the across-dataset side on one study.
  Evidence: a single source.
- Do not write: "Normalisation, pathway aggregation and compositional closure lower the apparent dimension of functional profiles."
  Why: That these shifts lower apparent dimension is the reviewer's inference, correctly marked in Section 2.3 and the D1 answer but dropped in the Section 6 summary; no cited source measured dimension under these choices.
  Say instead: What is measured is that processing choices change across-sample variance and covariance (normalisation, genome size, pathway aggregation, compositional closure), which a dimension estimate would inherit; that these shifts lower apparent dimension is the reviewer's inference, so the evidence is only indirect for dimension. (Lovell et al. 2015; Manor and Borenstein 2017; Ye and Doak 2009)
  Holds for: microbial functional profiles; indirect for dimension.
  Evidence: the reviewer's reading.
- Do not write: "Module dictionaries recovered held-out expression profiles at about 87% within a tumour type and 68% across tumour types."
  Why: The 87% and 68% are Spearman recovery of expression from 25 simulated random composite measurements through a learned dictionary (compressed sensing), not a direct covariance-reproduction score; the answer states the transfer more directly than the full text supports.
  Say instead: Sparse module dictionaries learned on 5% of samples of a TCGA tumour type gave about 87% recovery (Spearman, SMAF) within the same tumour type, and a dictionary from a different tumour type gave 68% on average, with related tumour types doing better; these figures are Spearman recovery of expression from 25 simulated random composite measurements through the dictionary (compressed sensing, m = 25, g = 5,000), not a direct covariance-reproduction score. (Cleary et al. 2017)
  Holds for: TCGA tumour types, transcriptomics; a withheld tissue type, the closest other-field analogue of a withheld habitat; the authors warn a dictionary is biased when training data do not represent the test data.
  Evidence: measured; a single source.
- Do not write: "Across fields, transfer depends on similarity between training and target, breadth of training, and how much of the target is shared mean structure."
  Why: The sentence pools incommensurable transfer tests of different quantities (covariance or dictionary transfer, taxon-to-gene mapping accuracy, per-sample accuracy metrics, phylogenetic gene gain/loss prediction); breadth rests on one qualitative study, and the whole is the reviewer's synthesis, not a finding.
  Say instead: The review's synthesis is that, across the other-field and neighbouring evidence, transfer appears to depend on the similarity of the training set to the target (related tumour types; related tissues; NSTI; phylum differences), the breadth of the training set, and the fraction of the target that is shared mean structure against target-specific signal; the critic holds that this pools incommensurable tests of different quantities (covariance or dictionary transfer, taxon-to-gene mapping accuracy, per-sample accuracy metrics, phylogenetic gene gain/loss prediction) and is the reviewer's synthesis, not a finding. (the reviewer's synthesis)
  Holds for: each dependency rests on one to three sources measuring different quantities, breadth on one qualitative study alone; none of these dependencies has been measured for microbial function-function covariation across habitats.
  Evidence: the reviewer's reading.
- Do not write: "Galand et al. (2018) is the only direct same-habitat result contrary to function levels being more stable than taxonomic composition."
  Why: Manor and Borenstein's full text (2017) directly measures that revised functional profiles identify hosts as well as strain-level taxonomy does, so contrary same-habitat evidence also exists in full text, and Galand et al. (2018) is abstract only.
  Say instead: Within a habitat where taxonomy turns over, several studies report function levels more stable than taxonomic composition (HMP pathways against organisms; bromeliad microcosms; macroalgal host COGs against species; soil microcosm functional groups; vermicomposting turnover rates), two in full text and three resting on abstracts; the direction is best described as reported by several studies but dependent on processing, with direct measured contrary evidence in human gut and coastal ocean. (Aira et al. 2026; Burke et al. 2011; Galand et al. 2018; The 2012; Louca et al. 2016; Manor and Borenstein 2017; Shan et al. 2023)
  Holds for: habitat held roughly fixed; none of the studies controls for normalisation, aggregation and granularity together.
  Evidence: rated "Moderate for the direction as reported, weak for the claim that the stability is biological rather than processing-driven" by the research.
  A second reader found the search for contrary evidence one-sided.
  Say instead: Revised processing (MUSiCC normalisation, filtering of prevalent families, non-uniform mapping) gave functional profiles that identified hosts as well as strain-level taxonomic markers did: a direct, measured same-habitat counter-result to functional stability. (Manor and Borenstein 2017)
  Holds for: human gut; verified against full text by the critic.
  Evidence: measured.
- Do not write: "How far function tracks taxonomy is itself habitat-dependent."
  Why: This rests on one modelled, abstract-only study comparing gut and vaginal communities.
  Say instead: A model found taxa-function robustness higher in gut than in vaginal communities, so how far function tracks taxonomy may itself vary by habitat. (Eng and Borenstein 2018)
  Holds for: one modelled, abstract-only study comparing gut and vaginal communities.
  Evidence: modelled; a single source.
- Do not write: "Across habitats, functional covariation was less stable than taxonomic covariation."
  Why: The finding is from one human gut study with one heterogeneity test, whose cohorts differ in disease state and population, not habitat; it compares pathway covariation with species covariation, not with composition; and heterogeneity tests have more power for the stronger, more numerous pathway correlations.
  Say instead: Across four human gut cohorts that differ in disease state and population (IBD, obesity, two population cohorts), 64.3% of pathway co-abundances and 38.6% of species co-abundances differed in strength (Cochran's Q, FDR < 0.05): in this setting pathway covariation was less stable across cohorts than species covariation. This compares functional covariation with taxonomic covariation, not with taxonomic composition, and the cohorts differ in disease state and population, not habitat. (Chen et al. 2020)
  Holds for: one human gut study, one heterogeneity test; the closest microbial evidence and the only microbial measurement of functional covariation stability; shared-member and common-factor cautions apply; the critic: heterogeneity tests have more power for stronger and more numerous correlations, and pathway correlations are stronger and more numerous, so easier to detect as heterogeneous.
  Evidence: a single source; rated "Weak (one study) for the microbial between-cohort case" by the research.
  A second reader found the search for contrary evidence one-sided.
- Do not write: "Pathway covariation changes came with changes in pathway levels: 84% of the 304 pathways involved also differed in level."
  Why: Reported alone, the pathway figure looks more distinctive than it is: the same study found that 76% of 100 species involved in variable co-abundances also differed in level.
  Say instead: Among the entities involved in variable co-abundances across the four gut cohorts, 84% of 304 pathways and also 76% of 100 species differed in level; the review reported only the pathway figure, which makes the pathway result look more distinctive than it is. (Chen et al. 2020)
  Holds for: four human gut cohorts differing in disease state.
  A second reader found the search for contrary evidence one-sided.
- Do not write: "Pathway co-abundances were almost fully stable over about a year (99.6%)."
  Why: The 99.6% is a count of co-abundances with no significant difference (Cochran's Q, P > 0.05) in 77 individuals, an absence-of-evidence count at a lenient bar, so it should not be read as near-complete stability.
  Say instead: Between the first and last iHMP-IBD time points, about one year apart, 90.6% of species and 99.6% of pathway co-abundances showed no significant difference in strength (Cochran's Q, P > 0.05) in 77 individuals; this is a count of non-significant differences, an absence-of-evidence count at the same lenient bar the review criticises for replication, and should not be read as near-complete stability. (Chen et al. 2020)
  Holds for: one IBD cohort (iHMP-IBD), human gut, n = 77; the only microbial measurement.
  A second reader found the search for contrary evidence one-sided.
- Do not write: "Coarse, aggregated functions look low-dimensional and stable, while fine, marker-normalised or all-read functions look higher-dimensional and more tied to taxonomy."
  Why: No cited source estimated dimension for fine against coarse functions; the sentence merges annotation granularity, normalisation, mapping and all-read comparison into one axis and presents the reviewer's synthesis as a pattern that measured pieces establish.
  Say instead: The reviewer's synthesis is that the answer to every direction depends on what is treated as "a function": coarse, aggregated, relatively normalised functions look stable, and fine, marker-normalised or all-read functions look more tied to taxonomy, with the measured pieces each a single study for its specific quantity; that they also differ in dimension (coarse functions looking low-dimensional, fine ones higher-dimensional) is the reviewer's inference, which no cited source measured. (Coelho et al. 2022; Galand et al. 2018; Manor and Borenstein 2015; Manor and Borenstein 2017; Nayfach and Pollard 2015; Sun et al. 2020)
  Holds for: the measured pieces cover annotation granularity, normalisation, mapping and all-read comparison; none of them measured dimension.
  Evidence: the reviewer's reading; a single source.

## Gaps

What the research did not establish.

- Network rewiring and differential co-occurrence across habitats in microbial data (taxonomic or functional): microbial co-occurrence network comparisons across habitats and body sites (soil drought or warming networks, cross-biome network topology, body-site network differences). (Faust et al. 2012)
  The research does not say whether this was searched for.
- Temporal stability of functional covariation beyond one IBD cohort: longitudinal metagenome and metatranscriptome series (human gut longitudinal cohorts, marine time-series stations) and repeated-survey CWM data.
  Not searched for.
- Held-out transfer of residual or covariance structure in community ecology: tests of joint species distribution model (HMSC and similar) transferability to new regions or communities, the closest other-field analogue of a withheld habitat.
  The research does not say whether this was searched for.
- Held-out transfer in other omics fields beyond bulk transcriptomics: single-cell reference mapping and latent-space transfer across tissues or species; proteomics and metabolomics covariance transfer.
  The research does not say whether this was searched for.
- Formal rank estimation on microbiome matrices under compositional transforms (cross-validated NMF or PCA, robust Aitchison PCA, random-matrix thresholds, sample-size subsampling), including any held-out rank estimate for functional profiles; the empirical dependence of rank on p/n is left to one species-trait study. (Mouillot et al. 2021; Jiang et al. 2012; Raguideau and others 2016; Johnstone 2001; Gavish and Donoho 2014)
  The research does not say whether this was searched for.
- Presence/absence against abundance for sample-level functional profiles: gene or KO presence/absence matrices across metagenome samples or MAG collections by habitat; the only presence/absence source is across genomes, not across samples. (Fahimipour and Gross 2020)
  The research does not say whether this was searched for.
- Methodological caution on sequencing approach for composition: 16S amplicon against shotgun taxonomic profiling, and OTU, ASV and species-level resolution effects on beta diversity and turnover estimates; resolution is discussed only through two abstracts. (Coelho et al. 2022; Sunagawa et al. 2015)
  The research does not say whether this was searched for.
- Correction for shared gene-set members in covariance or correlation: gene-set overlap correction methods in expression analysis, and pathway-pathway correlation with shared genes; only a significance-crosstalk study (abstract) is cited. (Donato et al. 2013)
  The research does not say whether this was searched for.
- Case C nearest precedents: reciprocal transplant and common-garden experiments with microbial communities, single-species pangenomes (conspecific strains) across hosts or habitats, and synthetic communities across media.
  Not searched for.
- Held-out tests of functional prediction in non-human habitats: soil, marine and engineered-system validations, including the PICRUSt2 and Tax4Fun2 cross-habitat validations, which were not obtained although the answer relies on Langille 2013 for the habitat-dependence of transfer. (Douglas and others 2020; Wemheuer and others 2020)
  The research does not say whether this was searched for.
- Dimension compared by habitat: habitat-stratified decompositions, for example per-biome NMF or PCA in multi-biome metagenome atlases.
  Not searched for.
- A targeted follow-up on the rank-estimation literature and on held-out functional validations outside human habitats, sized separately: the note's stage-2 routing condition was triggered on both arms.
  The research does not say whether this was searched for.
- Full-text verification of the load-bearing figures for the two sides of case B: Fierer 2012's Mantel r values were read in full text by one search angle only, and Nelson 2016 was read only through an automated summary; PMC returns for both contained only the abstract. (Fierer et al. 2012; Nelson et al. 2016)
  The research does not say whether this was searched for.
- Galand 2018 in full text: attempts to reach it failed, so it stays abstract only and its R² values are not used, although it is direct same-habitat contrary evidence. (Galand et al. 2018)
  The research does not say whether this was searched for.
- Comparisons of function and taxonomy at matched resolution and feature counts, with marker-normalised, unaggregated or all-read functional profiles, within and across habitats.
  The research does not say whether this was searched for.

## References

- Aira, Manuel; Perez-Losada, Marcos; Crandall, Keith A.; Dominguez, Jorge (2026). Faster turnover of taxonomic over functional bacterial composition during vermicomposting indicates increasing functional redundancy. PLOS One 21(7): e0354276. https://doi.org/10.1371/journal.pone.0354276
- Aitchison, J. (1982). The Statistical Analysis of Compositional Data. Journal of the Royal Statistical Society Series B: Statistical Methodology 44(2): 139--160. https://doi.org/10.1111/j.2517-6161.1982.tb01195.x
- Alneberg, Johannes; Bennke, Christin; Beier, Sara; Bunse, Carina; Quince, Christopher; Ininbergs, Karolina; Riemann, Lasse; Ekman, Martin; Jurgens, Klaus; Labrenz, Matthias; Pinhassi, Jarone; Andersson, Anders F. (2020). Ecosystem-wide metagenomic binning enables prediction of ecological niches from genomes. Communications Biology 3: 119. https://doi.org/10.1038/s42003-020-0856-x
- Anderegg, Leander D. L.; Berner, Logan T.; Badgley, Grayson; Sethi, Meera L.; Law, Beverly E.; HilleRisLambers, Janneke (2018). Within-species patterns challenge our understanding of the leaf economics spectrum. Ecology Letters 21(5): 734-744. https://doi.org/10.1111/ele.12945
- Barberan, Albert; Fernandez-Guerra, Antoni; Bohannan, Brendan J. M.; Casamayor, Emilio O. (2012). Exploration of community traits as ecological markers in microbial metagenomes. Molecular Ecology 21(8): 1909-1917. https://doi.org/10.1111/j.1365-294X.2011.05383.x
- Beavan, Alan J. S.; Domingo-Sananes, Maria Rosa; McInerney, James O. (2024). Contingency, repeatability, and predictability in the evolution of a prokaryotic pangenome. Proceedings of the National Academy of Sciences of the USA 121(1): e2304934120. https://doi.org/10.1073/pnas.2304934120
- Borgy, Benjamin; Violle, Cyrille; Choler, Philippe; Garnier, Eric; Kattge, Jens; Loranger, Jessy; Amiaud, Bernard; Cellier, Pierre; Debarros, Guilhem; Denelle, Pierre; Diquelou, Sylvain; Gachet, Sophie; Jolivet, Claudy; Lavorel, Sandra; Lemauviel-Lavenant, Servane; Mikolajczak, Alexis; Munoz, Francois; Olivier, Jean; Viovy, Nicolas (2017). Sensitivity of community-level trait-environment relationships to data representativeness: A test for functional biogeography. Global Ecology and Biogeography 26(6): 729-739. https://doi.org/10.1111/geb.12573
- Bruelheide, Helge; Dengler, Jurgen; Purschke, Oliver; Lenoir, Jonathan; Jimenez-Alfaro, Borja; Hennekens, Stephan M.; Botta-Dukat, Zoltan; Chytry, Milan; Field, Richard; Jansen, Florian; Kattge, Jens; Pillar, Valerio D.; Schrodt, Franziska; Mahecha, Miguel D.; Peet, Robert K.; Sandel, Brody; van Bodegom, Peter; Altman, Jan; Alvarez-Davila, Esteban; Arfin Khan, Mohammed A. S.; Attorre, Fabio; Aubin, Isabelle; Baraloto, Christopher; Barroso, Jorcely G.; Bauters, Marijn; Bergmeier, Erwin; Biurrun, Idoia; Bjorkman, Anne D.; Blonder, Benjamin; Carni, Andraz; Cayuela, Luis; Cerny, Tomas; Cornelissen, J. Hans C.; Craven, Dylan; Dainese, Matteo; Derroire, Geraldine; De Sanctis, Michele; Diaz, Sandra; Dolezal, Jiri; Farfan-Rios, William; Feldpausch, Ted R.; Fenton, Nicole J.; Garnier, Eric; Guerin, Greg R.; Gutierrez, Alvaro G.; Haider, Sylvia; Hattab, Tarek; Henry, Greg; Herault, Bruno; Higuchi, Pedro; Holzel, Norbert; Homeier, Jurgen; Jentsch, Anke; Jurgens, Norbert; Kacki, Zygmunt; Karger, Dirk N.; Kessler, Michael; Kleyer, Michael; Knollova, Ilona; Korolyuk, Andrey Y.; Kuhn, Ingolf; Laughlin, Daniel C.; Lens, Frederic; Loos, Jacqueline; Louault, Frederique; Lyubenova, Mariyana I.; Malhi, Yadvinder; Marceno, Corrado; Mencuccini, Maurizio; Muller, Jonas V.; Munzinger, Jerome; Myers-Smith, Isla H.; Neill, David A.; Niinemets, Ulo; Orwin, Kate H.; Ozinga, Wim A.; Penuelas, Josep; Perez-Haase, Aaron; Petrik, Petr; Phillips, Oliver L.; Partel, Meelis; Reich, Peter B.; Romermann, Christine; Rodrigues, Arthur V.; Sabatini, Francesco Maria; Sardans, Jordi; Schmidt, Marco; Seidler, Gunnar; Silva Espejo, Javier Eduardo; Silveira, Marcos; Smyth, Anita; Sporbert, Maria; Svenning, Jens-Christian; Tang, Zhiyao; Thomas, Raquel; Tsiripidis, Ioannis; Vassilev, Kiril; Violle, Cyrille; Virtanen, Risto; Weiher, Evan; Welk, Erik; Wesche, Karsten; Winter, Marten; Wirth, Christian; Jandt, Ute (2018). Global trait-environment relationships of plant communities. Nature Ecology & Evolution 2(12): 1906-1917. https://doi.org/10.1038/s41559-018-0699-8
- Burke, Catherine; Steinberg, Peter; Rusch, Doug; Kjelleberg, Staffan; Thomas, Torsten (2011). Bacterial community assembly based on functional genes rather than species. Proceedings of the National Academy of Sciences of the USA 108(34): 14288-14293. https://doi.org/10.1073/pnas.1101591108
- Chen, Lianmin; Collij, Valerie; Jaeger, Martin; van den Munckhof, Inge C. L.; Vich Vila, Arnau; Kurilshikov, Alexander; Gacesa, Ranko; Sinha, Trishla; Oosting, Marije; Joosten, Leo A. B.; Rutten, Joost H. W.; Riksen, Niels P.; Xavier, Ramnik J.; Kuipers, Folkert; Wijmenga, Cisca; Zhernakova, Alexandra; Netea, Mihai G.; Weersma, Rinse K.; Fu, Jingyuan (2020). Gut microbial co-abundance networks show specificity in inflammatory bowel disease and obesity. Nature Communications 11: 4018. https://doi.org/10.1038/s41467-020-17840-y
- Chung, Henri C.; Friedberg, Iddo; Bromberg, Yana (2024). Assembling bacterial puzzles: piecing together functions into microbial pathways. NAR Genomics and Bioinformatics 6(3): lqae109. https://doi.org/10.1093/nargab/lqae109
- Cleary, Brian; Cong, Le; Cheung, Anthea; Lander, Eric S.; Regev, Aviv (2017). Efficient generation of transcriptomic profiles by random composite measurements. Cell 171(6): 1424-1436.e18. https://doi.org/10.1016/j.cell.2017.10.023
- Coelho, Luis Pedro; Alves, Renato; Rodriguez del Rio, Alvaro; Myers, Pernille Neve; Cantalapiedra, Carlos P.; Giner-Lamia, Joaquin; Schmidt, Thomas Sebastian; Mende, Daniel R.; Orakov, Askarbek; Letunic, Ivica; Hildebrand, Falk; Van Rossum, Thea; Forslund, Sofia K.; Khedkar, Supriya; Maistrenko, Oleksandr M.; Pan, Shaojun; Jia, Longhao; Ferretti, Pamela; Sunagawa, Shinichi; Zhao, Xing-Ming; Nielsen, Henrik Bjrn; Huerta-Cepas, Jaime; Bork, Peer (2022). Towards the biogeography of prokaryotic genes. Nature 601(7892): 252-256. https://doi.org/10.1038/s41586-021-04233-4
- Crow, Megan; Paul, Anirban; Ballouz, Sara; Huang, Z. Josh; Gillis, Jesse (2016). Exploiting single-cell expression to characterize co-expression replicability. Genome Biology 17: 101. https://doi.org/10.1186/s13059-016-0964-6
- Dinsdale, Elizabeth A.; Edwards, Robert A.; Hall, Dana; Angly, Florent; Breitbart, Mya; Brulc, Jennifer M.; Furlan, Mike; Desnues, Christelle; Haynes, Matthew; Li, Linlin; McDaniel, Lauren; Moran, Mary Ann; Nelson, Karen E.; Nilsson, Christina; Olson, Robert; Paul, John; Rodriguez Brito, Beltran; Ruan, Yijun; Swan, Brandon K.; Stevens, Rick; Valentine, David L.; Vega Thurber, Rebecca; Wegley, Linda; White, Bryan A.; Rohwer, Forest (2008). Functional metagenomic profiling of nine biomes. Nature 452(7187): 629-632. https://doi.org/10.1038/nature06810
- Donato, Michele; Xu, Zhonghui; Tomoiaga, Alin; Granneman, James G.; MacKenzie, Robert G.; Bao, Riyue; Than, Nandor Gabor; Westfall, Peter H.; Romero, Roberto; Draghici, Sorin (2013). Analysis and correction of crosstalk effects in pathway analysis. Genome Research 23(11): 1885-1893. https://doi.org/10.1101/gr.153551.112
- Douglas, G. M.; others (2020). PICRUSt2 for prediction of metagenome functions. Nature Biotechnology 38: 685--688. https://doi.org/10.1038/s41587-020-0548-6
- Dwyer, John M.; Laughlin, Daniel C. (2017). Constraints on trait combinations explain climatic drivers of biodiversity: the importance of trait covariance in community assembly. Ecology Letters 20(7): 872-882. https://doi.org/10.1111/ele.12781
- Eng, Alexander; Borenstein, Elhanan (2018). Taxa-function robustness in microbial communities. Microbiome 6: 45. https://doi.org/10.1186/s40168-018-0425-4
- Fahimipour, Ashkaan K.; Gross, Thilo (2020). Mapping the bacterial metabolic niche space. Nature Communications 11: 4887. https://doi.org/10.1038/s41467-020-18695-z
- Faust, Karoline; Sathirapongsasuti, J. Fah; Izard, Jacques; Segata, Nicola; Gevers, Dirk; Raes, Jeroen; Huttenhower, Curtis (2012). Microbial co-occurrence relationships in the human microbiome. PLoS Computational Biology 8(7): e1002606. https://doi.org/10.1371/journal.pcbi.1002606
- Fierer, Noah; Leff, Jonathan W.; Adams, Byron J.; Nielsen, Uffe N.; Bates, Scott Thomas; Lauber, Christian L.; Owens, Sarah; Gilbert, Jack A.; Wall, Diana H.; Caporaso, J. Gregory (2012). Cross-biome metagenomic analyses of soil microbial communities and their functional attributes. Proceedings of the National Academy of Sciences of the USA 109(52): 21390-21395. https://doi.org/10.1073/pnas.1215210110
- Flinkstrom, Zachary; Bryson, Samuel; Candry, Pieter; Winkler, Mari-Karoliina H. (2024). Metagenomic clustering links specific metabolic functions to globally relevant ecosystems. mSystems 9(8): e00573-24. https://doi.org/10.1128/msystems.00573-24
- Flores-Moreno, Habacuc; Fazayeli, Farideh; Banerjee, Arindam; Datta, Abhirup; Kattge, Jens; Butler, Ethan E.; Atkin, Owen K.; Wythers, Kirk; Chen, Ming; Anand, Madhur; Bahn, Michael; Byun, Chaeho; Cornelissen, J. Hans C.; Craine, Joseph; Gonzalez-Melo, Andres; Hattingh, Wesley N.; Jansen, Steven; Kraft, Nathan J. B.; Kramer, Koen; Laughlin, Daniel C.; Minden, Vanessa; Niinemets, Ulo; Onipchenko, Vladimir; Penuelas, Josep; Soudzilovskaia, Nadejda A.; Dalrymple, Rhiannon L.; Reich, Peter B. (2019). Robustness of trait connections across environmental gradients and growth forms. Global Ecology and Biogeography 28(12): 1806-1826. https://doi.org/10.1111/geb.12996
- Frioux, Clemence; Ansorge, Rebecca; Ozkurt, Ezgi; Ghassemi Nedjad, Chabname; Fritscher, Joachim; Quince, Christopher; Waszak, Sebastian M.; Hildebrand, Falk (2023). Enterosignatures define common bacterial guilds in the human gut microbiome. Cell Host & Microbe 31(7): 1111-1125.e6. https://doi.org/10.1016/j.chom.2023.05.024
- Galand, Pierre E.; Pereira, Olivier; Hochart, Corentin; Auguet, Jean Christophe; Debroas, Didier (2018). A strong link between marine microbial community composition and function challenges the idea of functional redundancy. The ISME Journal 12(10): 2470-2478. https://doi.org/10.1038/s41396-018-0158-1
- Garnier, Eric; Cortez, Jacques; Billes, Georges; Navas, Marie-Laure; Roumet, Catherine; Debussche, Max; Laurent, Gerard; Blanchard, Alain; Aubry, David; Bellmann, Astrid; Neill, Cathy; Toussaint, Jean-Patrick (2004). Plant Functional Markers Capture Ecosystem Properties During Secondary Succession. Ecology 85(9): 2630--2637. https://doi.org/10.1890/03-0799
- Gavish, Matan; Donoho, David L. (2014). The Optimal Hard Threshold for Singular Values is 4/sqrt(3). IEEE Transactions on Information Theory 60(8): 5040--5053. https://doi.org/10.1109/TIT.2014.2323359
- Gianoulis, Tara A.; Raes, Jeroen; Patel, Prianka V.; Bjornson, Robert; Korbel, Jan O.; Letunic, Ivica; Yamada, Takuji; Paccanaro, Alberto; Jensen, Lars J.; Snyder, Michael; Bork, Peer; Gerstein, Mark B. (2009). Quantifying environmental adaptation of metabolic pathways in metagenomics. Proceedings of the National Academy of Sciences of the USA 106(5): 1374-1379. https://doi.org/10.1073/pnas.0808022106
- Gowda, Karna; Ping, Derek; Mani, Madhav; Kuehn, Seppe (2022). Genomic structure predicts metabolite dynamics in microbial communities. Cell 185(3): 530-546.e25. https://doi.org/10.1016/j.cell.2021.12.036
- He, Nianpeng; Li, Ying; Liu, Congcong; Xu, Li; Li, Mingxu; Zhang, Jiahui; He, Jinsheng; Tang, Zhiyao; Han, Xingguo; Ye, Qing; Xiao, Chunwang; Yu, Qiang; Liu, Shirong; Sun, Wei; Niu, Shuli; Li, Shenggong; Sack, Lawren; Yu, Guirui (2020). Plant trait networks: improved resolution of the dimensionality of adaptation. Trends in Ecology & Evolution 35(10): 908-918. https://doi.org/10.1016/j.tree.2020.06.003
- Heimberg, Graham; Bhatnagar, Rajat; El-Samad, Hana; Thomson, Matt (2016). Low dimensionality in gene expression data enables the accurate extraction of transcriptional programs from shallow sequencing. Cell Systems 2(4): 239-250. https://doi.org/10.1016/j.cels.2016.04.001
- Jiang, X.; Weitz, J. S.; Dushoff, J. (2012). A non-negative matrix factorization framework for identifying modular patterns in metagenomic profile data. Journal of Mathematical Biology 64: 697--711. https://doi.org/10.1007/s00285-011-0428-2
- Jiang, Xingpeng; Langille, Morgan G. I.; Neches, Russell Y.; Elliot, Marie; Levin, Simon A.; Eisen, Jonathan A.; Weitz, Joshua S.; Dushoff, Jonathan (2012). Functional biogeography of ocean microbes revealed through non-negative matrix factorization. PLoS ONE 7(9): e43866. https://doi.org/10.1371/journal.pone.0043866
- Johnstone, Iain M. (2001). On the distribution of the largest eigenvalue in principal components analysis. The Annals of Statistics 29(2): 295--327. https://doi.org/10.1214/aos/1009210544
- Joswig, Julia S.; Wirth, Christian; Schuman, Meredith C.; Kattge, Jens; Reu, Bjorn; Wright, Ian J.; Sippel, Sebastian D.; Ruger, Nadja; Richter, Ronny; Schaepman, Michael E.; van Bodegom, Peter M.; Cornelissen, J. H. C.; Diaz, Sandra; Hattingh, Wesley N.; Kramer, Koen; Lens, Frederic; Niinemets, Ulo; Reich, Peter B.; Reichstein, Markus; Romermann, Christine; Schrodt, Franziska; Anand, Madhur; Bahn, Michael; Byun, Chaeho; Campetella, Giandiego; Cerabolini, Bruno E. L.; Craine, Joseph M.; Gonzalez-Melo, Andres; Gutierrez, Alvaro G.; He, Tianhua; Higuchi, Pedro; Jactel, Herve; Kraft, Nathan J. B.; Minden, Vanessa; Onipchenko, Vladimir; Penuelas, Josep; Pillar, Valerio D.; Sosinski, Enio; Soudzilovskaia, Nadejda A.; Weiher, Evan; Mahecha, Miguel D. (2022). Climatic and soil factors explain the two-dimensional spectrum of global plant trait variation. Nature Ecology & Evolution 6(1): 36-50. https://doi.org/10.1038/s41559-021-01616-8
- Konno, Naoki; Iwasaki, Wataru (2023). Machine learning enables prediction of metabolic system evolution in bacteria. Science Advances 9(2): eadc9130. https://doi.org/10.1126/sciadv.adc9130
- Langille, Morgan G. I.; Zaneveld, Jesse; Caporaso, J. Gregory; McDonald, Daniel; Knights, Dan; Reyes, Joshua A.; Clemente, Jose C.; Burkepile, Deron E.; Vega Thurber, Rebecca L.; Knight, Rob; Beiko, Robert G.; Huttenhower, Curtis (2013). Predictive functional profiling of microbial communities using 16S rRNA marker gene sequences. Nature Biotechnology 31(9): 814-821. https://doi.org/10.1038/nbt.2676
- Laughlin, Daniel C. (2014). The intrinsic dimensionality of plant traits and its relevance to community assembly. Journal of Ecology 102(1): 186-193. https://doi.org/10.1111/1365-2745.12187
- Lee, Daniel D.; Seung, H. Sebastian (1999). Learning the parts of objects by non-negative matrix factorization. Nature 401(6755): 788--791. https://doi.org/10.1038/44565
- Lenz, Michael; Muller, Franz-Josef; Zenke, Martin; Schuppert, Andreas (2016). Principal components analysis and the reported low intrinsic dimensionality of gene expression microarray data. Scientific Reports 6: 25696. https://doi.org/10.1038/srep25696
- Louca, Stilianos; Jacques, Saulo M. S.; Pires, Aliny P. F.; Leal, Juliana S.; Srivastava, Diane S.; Parfrey, Laura Wegener; Farjalla, Vinicius F.; Doebeli, Michael (2016). High taxonomic variability despite stable functional structure across microbial communities. Nature Ecology & Evolution 1(1): 0015. https://doi.org/10.1038/s41559-016-0015
- Louca, Stilianos; Parfrey, Laura Wegener; Doebeli, Michael (2016). Decoupling function and taxonomy in the global ocean microbiome. Science 353(6305): 1272-1277. https://doi.org/10.1126/science.aaf4507
- Lovell, David; Pawlowsky-Glahn, Vera; Egozcue, Juan Jose; Marguerat, Samuel; Bahler, Jurg (2015). Proportionality: a valid alternative to correlation for relative data. PLOS Computational Biology 11(3): e1004075. https://doi.org/10.1371/journal.pcbi.1004075
- Manor, Ohad; Borenstein, Elhanan (2015). MUSiCC: a marker genes based framework for metagenomic normalization and accurate profiling of gene abundances in the microbiome. Genome Biology 16: 53. https://doi.org/10.1186/s13059-015-0610-8
- Manor, Ohad; Borenstein, Elhanan (2017). Revised computational metagenomic processing uncovers hidden and biologically meaningful functional variation in the human microbiome. Microbiome 5: 19. https://doi.org/10.1186/s40168-017-0231-4
- Messier, Julie; McGill, Brian J.; Enquist, Brian J.; Lechowicz, Martin J. (2017). Trait variation and integration across scales: is the leaf economic spectrum present at local scales?. Ecography 40(6): 685-697. https://doi.org/10.1111/ecog.02006
- Mouillot, David; Loiseau, Nicolas; Grenie, Matthias; Algar, Adam C.; Allegra, Michele; Cadotte, Marc W.; Casajus, Nicolas; Denelle, Pierre; Gueguen, Maya; Maire, Anthony; Maitner, Brian; McGill, Brian J.; McLean, Matthew; Mouquet, Nicolas; Munoz, Francois; Thuiller, Wilfried; Villeger, Sebastien; Violle, Cyrille; Auber, Arnaud (2021). The dimensionality and structure of species trait spaces. Ecology Letters 24(9): 1988-2009. https://doi.org/10.1111/ele.13778
- Nayfach, Stephen; Pollard, Katherine S. (2015). Average genome size estimation improves comparative metagenomics and sheds light on the functional ecology of the human microbiome. Genome Biology 16: 51. https://doi.org/10.1186/s13059-015-0611-7
- Nelson, Michaeline B.; Martiny, Adam C.; Martiny, Jennifer B. H. (2016). Global biogeography of microbial nitrogen-cycling traits in soil. Proceedings of the National Academy of Sciences of the USA 113(29): 8033-8040. https://doi.org/10.1073/pnas.1601070113
- Peres-Neto, Pedro R.; Dray, Stephane; ter Braak, Cajo J. F. (2017). Linking trait variation to the environment: critical issues with community-weighted mean correlation resolved by the fourth-corner approach. Ecography 40(7): 806-816. https://doi.org/10.1111/ecog.02302
- Pierson, Emma; the GTEx Consortium; Koller, Daphne; Battle, Alexis; Mostafavi, Sara (2015). Sharing and specificity of co-expression networks across 35 human tissues. PLOS Computational Biology 11(5): e1004220. https://doi.org/10.1371/journal.pcbi.1004220
- Piton, Gabin; Allison, Steven D.; Bahram, Mohammad; Hildebrand, Falk; Martiny, Jennifer B. H.; Treseder, Kathleen K.; Martiny, Adam C. (2023). Life history strategies of soil bacterial communities across global terrestrial biomes. Nature Microbiology 8(11): 2093-2102. https://doi.org/10.1038/s41564-023-01465-0
- Raes, Jeroen; Letunic, Ivica; Yamada, Takuji; Jensen, Lars Juhl; Bork, Peer (2011). Toward molecular trait-based ecology through integration of biogeochemical, geographical and metagenomic data. Molecular Systems Biology 7: 473. https://doi.org/10.1038/msb.2011.6
- Raguideau, S.; others (2016). Inferring aggregated functional traits from metagenomic data using constrained non-negative matrix factorization. PLoS Computational Biology 12(12): e1005252. https://doi.org/10.1371/journal.pcbi.1005252
- Ramirez-Flandes, Salvador; Gonzalez, Bernardo; Ulloa, Osvaldo (2019). Redox traits characterize the organization of global microbial communities. Proceedings of the National Academy of Sciences of the USA 116(9): 3630-3635. https://doi.org/10.1073/pnas.1817554116
- Salazar, Guillem; Paoli, Lucas; Alberti, Adriana; Huerta-Cepas, Jaime; Ruscheweyh, Hans-Joachim; Cuenca, Miguelangel; Field, Christopher M.; Coelho, Luis Pedro; Cruaud, Corinne; Engelen, Stefan; Gregory, Ann C.; Labadie, Karine; Marec, Claudie; Pelletier, Eric; Royo-Llonch, Marta; Roux, Simon; Sanchez, Pablo; Uehara, Hideya; Zayed, Ahmed A.; Zeller, Georg; Carmichael, Margaux; Dimier, Celine; Ferland, Joannie; Kandels, Stefanie; Picheral, Marc; Pisarev, Sergey; Poulain, Julie; Tara Oceans Coordinators; Acinas, Silvia G.; Babin, Marcel; Bork, Peer; Bowler, Chris; de Vargas, Colomban; Guidi, Lionel; Hingamp, Pascal; Iudicone, Daniele; Karp-Boss, Lee; Karsenti, Eric; Ogata, Hiroyuki; Pesant, Stephane; Speich, Sabrina; Sullivan, Matthew B.; Wincker, Patrick; Sunagawa, Shinichi (2019). Gene expression changes and community turnover differentially shape the global ocean metatranscriptome. Cell 179(5): 1068-1083.e21. https://doi.org/10.1016/j.cell.2019.10.014
- Schrodt, Franziska; Kattge, Jens; Shan, Hanhuai; Fazayeli, Farideh; Joswig, Julia; Banerjee, Arindam; Reichstein, Markus; Bonisch, Gerhard; Diaz, Sandra; Dickie, John; Gillison, Andy; Karpatne, Anuj; Lavorel, Sandra; Leadley, Paul; Wirth, Christian B.; Wright, Ian J.; Wright, S. Joseph; Reich, Peter B. (2015). BHPMF: a hierarchical Bayesian approach to gap-filling and trait prediction for macroecology and functional biogeography. Global Ecology and Biogeography 24(12): 1510-1521. https://doi.org/10.1111/geb.12335
- Shan, Xiaoyu; Goyal, Akshit; Gregor, Rachel; Cordero, Otto X. (2023). Annotation-free discovery of functional groups in microbial communities. Nature Ecology & Evolution 7(5): 716-724. https://doi.org/10.1038/s41559-023-02021-z
- Stein-O'Brien, Genevieve L.; Clark, Brian S.; Sherman, Thomas; Zibetti, Cristina; Hu, Qiwen; Sealfon, Rachel; Liu, Sheng; Qian, Jiang; Colantuoni, Carlo; Blackshaw, Seth; Goff, Loyal A.; Fertig, Elana J. (2019). Decomposing cell identity for transfer learning across cellular measurements, platforms, tissues, and species. Cell Systems 8(5): 395-411.e8. https://doi.org/10.1016/j.cels.2019.04.004
- Subramanian, Aravind; Narayan, Rajiv; Corsello, Steven M.; Peck, David D.; Natoli, Ted E.; Lu, Xiaodong; Gould, Joshua; Davis, John F.; Tubelli, Andrew A.; Asiedu, Jacob K.; Lahr, David L.; Hirschman, Jodi E.; Liu, Zihan; Donahue, Melanie; Julian, Bina; Khan, Mariya; Wadden, David; Smith, Ian C.; Lam, Daniel; Liberzon, Arthur; Toder, Courtney; Bagul, Mukta; Orzechowski, Marek; Enache, Oana M.; Piccioni, Federica; Johnson, Sarah A.; Lyons, Nicholas J.; Berger, Alice H.; Shamji, Alykhan F.; Brooks, Angela N.; Vrcic, Anita; Flynn, Corey; Rosains, Jacqueline; Takeda, David Y.; Hu, Roger; Davison, Desiree; Lamb, Justin; Ardlie, Kristin; Hogstrom, Larson; Greenside, Peyton; Gray, Nathanael S.; Clemons, Paul A.; Silver, Serena; Wu, Xiaoyun; Zhao, Wen-Ning; Read-Button, Willis; Wu, Xiaohua; Haggarty, Stephen J.; Ronco, Lucienne V.; Boehm, Jesse S.; Schreiber, Stuart L.; Doench, John G.; Bittker, Joshua A.; Root, David E.; Wong, Bang; Golub, Todd R. (2017). A next generation connectivity map: L1000 platform and the first 1,000,000 profiles. Cell 171(6): 1437-1452.e17. https://doi.org/10.1016/j.cell.2017.10.049
- Sun, Shan; Jones, Roshonda B.; Fodor, Anthony A. (2020). Inference-based accuracy of metagenome prediction tools varies across sample types and functional categories. Microbiome 8: 46. https://doi.org/10.1186/s40168-020-00815-y
- Sunagawa, Shinichi; Coelho, Luis Pedro; Chaffron, Samuel; Kultima, Jens Roat; Labadie, Karine; Salazar, Guillem; Djahanschiri, Bardya; Zeller, Georg; Mende, Daniel R.; Alberti, Adriana; Cornejo-Castillo, Francisco M.; Costea, Paul I.; Cruaud, Corinne; d'Ovidio, Francesco; Engelen, Stefan; Ferrera, Isabel; Gasol, Josep M.; Guidi, Lionel; Hildebrand, Falk; Kokoszka, Florian; Lepoivre, Cyrille; Lima-Mendez, Gipsi; Poulain, Julie; Poulos, Bonnie T.; Royo-Llonch, Marta; Sarmento, Hugo; Vieira-Silva, Sara; Dimier, Celine; Picheral, Marc; Searson, Sarah; Kandels-Lewis, Stefanie; Tara Oceans coordinators; Bowler, Chris; de Vargas, Colomban; Gorsky, Gabriel; Grimsley, Nigel; Hingamp, Pascal; Iudicone, Daniele; Jaillon, Olivier; Not, Fabrice; Ogata, Hiroyuki; Pesant, Stephane; Speich, Sabrina; Stemmann, Lars; Sullivan, Matthew B.; Weissenbach, Jean; Wincker, Patrick; Karsenti, Eric; Raes, Jeroen; Acinas, Silvia G.; Bork, Peer (2015). Structure and function of the global ocean microbiome. Science 348(6237): 1261359. https://doi.org/10.1126/science.1261359
- Taroni, Jaclyn N.; Grayson, Peter C.; Hu, Qiwen; Eddy, Sean; Kretzler, Matthias; Merkel, Peter A.; Greene, Casey S. (2019). MultiPLIER: a transfer learning framework for transcriptomics reveals systemic features of rare disease. Cell Systems 8(5): 380-394.e4. https://doi.org/10.1016/j.cels.2019.04.003
- The Human Microbiome Project Consortium (2012). Structure, function and diversity of the healthy human microbiome. Nature 486(7402): 207-214. https://doi.org/10.1038/nature11234
- Tian, Liang; Wang, Xu-Wen; Wu, Ang-Kun; Fan, Yuhang; Friedman, Jonathan; Dahlin, Amber; Waldor, Matthew K.; Weinstock, George M.; Weiss, Scott T.; Liu, Yang-Yu (2020). Deciphering functional redundancy in the human microbiome. Nature Communications 11: 6217. https://doi.org/10.1038/s41467-020-19940-1
- Vieira-Silva, Sara; Falony, Gwen; Darzi, Youssef; Lima-Mendez, Gipsi; Garcia Yunta, Roberto; Okuda, Shujiro; Vandeputte, Doris; Valles-Colomer, Mireia; Hildebrand, Falk; Chaffron, Samuel; Raes, Jeroen (2016). Species-function relationships shape ecological properties of the human gut microbiome. Nature Microbiology 1(8): 16088. https://doi.org/10.1038/nmicrobiol.2016.88
- Wemheuer, F.; others (2020). Tax4Fun2: prediction of habitat-specific functional profiles and functional redundancy based on 16S rRNA gene sequences. Environmental Microbiome 15: 11. https://doi.org/10.1186/s40793-020-00358-7
- Westoby, Mark; Gillings, Michael R.; Madin, Joshua S.; Nielsen, Daniel A.; Paulsen, Ian T.; Tetu, Sasha G. (2021). Trait dimensions in bacteria and archaea compared to vascular plants. Ecology Letters 24(7): 1487-1504. https://doi.org/10.1111/ele.13742
- Wieczynski, Daniel J.; Boyle, Brad; Buzzard, Vanessa; Duran, Sandra M.; Henderson, Amanda N.; Hulshof, Catherine M.; Kerkhoff, Andrew J.; McCarthy, Megan C.; Michaletz, Sean T.; Swenson, Nathan G.; Asner, Gregory P.; Bentley, Lisa Patrick; Enquist, Brian J.; Savage, Van M. (2019). Climate shapes and shifts functional biodiversity in forests worldwide. Proceedings of the National Academy of Sciences of the USA 116(2): 587-592. https://doi.org/10.1073/pnas.1813723116
- Wirbel, Jakob; Pyl, Paul Theodor; Kartal, Ece; Zych, Konrad; Kashani, Alireza; Milanese, Alessio; Fleck, Jonas S.; Voigt, Anita Y.; Palleja, Albert; Ponnudurai, Ruby; Sunagawa, Shinichi; Coelho, Luis Pedro; Schrotz-King, Petra; Vogtmann, Emily; Habermann, Nina; Nimeus, Emma; Thomas, Andrew M.; Manghi, Paolo; Gandini, Sara; Serrano, Davide; Mizutani, Sayaka; Shiroma, Hirotsugu; Shiba, Satoshi; Shibata, Tatsuhiro; Yachida, Shinichi; Yamada, Takuji; Waldron, Levi; Naccarati, Alessio; Segata, Nicola; Sinha, Rashmi; Ulrich, Cornelia M.; Brenner, Hermann; Arumugam, Manimozhiyan; Bork, Peer; Zeller, Georg (2019). Meta-analysis of fecal metagenomes reveals global microbial signatures that are specific for colorectal cancer. Nature Medicine 25(4): 679-689. https://doi.org/10.1038/s41591-019-0406-6
- Wright, Ian J.; Reich, Peter B.; Cornelissen, Johannes H. C.; Falster, Daniel S.; Groom, Philip K.; Hikosaka, Kouki; Lee, William; Lusk, Christopher H.; Niinemets, Ulo; Oleksyn, Jacek; Osada, Noriyuki; Poorter, Hendrik; Warton, David I.; Westoby, Mark (2005). Modulation of leaf economic traits and trait relationships by climate. Global Ecology and Biogeography 14(5): 411-421. https://doi.org/10.1111/j.1466-822X.2005.00172.x
- Wu, Xingjie; Peng, Jingjing; Malik, Ashish Anil; Peng, Ziheng; Luo, Yu; Fan, Fenliang; Lu, Yahai; Wei, Gehong; Delgado-Baquerizo, Manuel; Liesack, Werner; Jiao, Shuo (2025). A global relationship between genome size and encoded carbon metabolic strategies of soil bacteria. Ecology Letters 28(1): e70064. https://doi.org/10.1111/ele.70064
- Ye, Yuzhen; Doak, Thomas G. (2009). A parsimony approach to biological pathway reconstruction/inference for genomes and metagenomes. PLoS Computational Biology 5(8): e1000465. https://doi.org/10.1371/journal.pcbi.1000465
- Zeleny, David (2018). Which results of the standard test for community-weighted mean approach are too optimistic?. Journal of Vegetation Science 29(6): 953-966. https://doi.org/10.1111/jvs.12688
