---
type: knowledge
title: Rank-based association networks against known truth
inputs:
  - C-RANKNET: PhD/Proposal/Research/Results/Rank-based association networks what exists, what has been benchmarked against known truth, and where the comparison has not been made.md
refs: PhD/Proposal/Refs/Refs.bib
built: 2026-10-24
status: draft
tags:
  - research
  - knowledge
---
# Rank-based association networks against known truth

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
| C-RANKNET | [[Rank-based association networks what exists, what has been benchmarked against known truth, and where the comparison has not been made]] | yes | numbered | no | no | fallback |

## Concepts

### known-truth: benchmarking against known truth
needs: none
- **known-truth.1** Ghaeli, Aghdam and Eslahchi open by stating the field's core obstacle: "the lack of experimentally validated gold standards presents a significant obstacle in evaluating the biological accuracy of inferred networks".
  conf: not stated · class: not stated · holds: microbial network inference · src: ghaeliEvaluatingMicrobialNetwork2026 · trail: C-RANKNET §The rank device in microbial · from: C-RANKNET:B-0100
- **known-truth.2** Faust's review states that no DREAM-style challenge exists for microbial network inference, and that "interactions observed previously in nature cannot be used to determine the accuracy of network inference tools but only their sensitivity", which is why a truth-based comparison on real data is unavailable.
  conf: single (critic: C-027) · class: assert (critic: C-027) · holds: microbial network inference; the critic: rests on Faust 2021 alone, asserted in a review · src: faustOpenChallengesMicrobial2021 · trail: C-RANKNET §The rank device in microbial, §Single-source claims · from: C-RANKNET:B-0112, C-RANKNET:C-027

### rank-device: which rank a method uses
needs: none
- **rank-device.1** Two research communities have independently reached for ranks when building networks of features measured across many samples, and they reached for different ranks: gene co-expression uses the rank of a correlation coefficient inside a gene's own neighbour list, producing reciprocal-rank constructions such as mutual rank and highest reciprocal rank; microbial ecology uses the rank of the measurement itself, feeding Spearman's rho or Kendall's tau into an edge weight or into a copula estimator.
  conf: not stated · class: not stated · holds: gene co-expression and microbial ecology network construction · src: obayashiRankCorrelationCoefficient2009, mutwilAssemblyInteractiveCorrelation2010, yoonMicrobialNetworksSPRING2019, weissCorrelationDetectionStrategies2016 · trail: C-RANKNET §The review as returned · from: C-RANKNET:B-0015..0017
- **rank-device.2** A third community, community ecology, tracks the rank of a taxon's abundance through time; the three vocabularies barely overlap in the literature, and only the first two (gene co-expression and microbial ecology) have been benchmarked against known truth.
  conf: not stated · class: not stated · holds: gene co-expression, microbial ecology and community ecology literatures · src: battyRankClocks2006 (†: read in full text by a search agent and not re-opened by the reviewer), collinsRankClocksPlant2008 (†), avolioComprehensiveApproachAnalyzing2019 (†) · trail: C-RANKNET §The review as returned · from: C-RANKNET:B-0015, C-RANKNET:B-0018..0020

### rank-statistics: rank statistics and their non-rank comparators
needs: rank-device
- **rank-statistics.1** Spearman's rank correlation (rho) is Pearson correlation computed on the ranks; it is the microbiome field's default correlation-based co-occurrence measure, usually thresholded at absolute rho 0.6 to 0.8.
  conf: not stated · class: not stated · holds: the review's glossary; used in every field · src: none (the review's glossary) · trail: C-RANKNET §Glossary · from: C-RANKNET:B-0185
- **rank-statistics.2** Kendall's tau is the concordant minus discordant pair fraction; it is the base statistic for copula-based latent correlation estimators and one member of CoNet-style ensembles.
  conf: not stated · class: not stated · holds: the review's glossary · src: none (the review's glossary) · trail: C-RANKNET §Glossary · from: C-RANKNET:B-0186
- **rank-statistics.3** Weighted rank correlation is a Spearman-type coefficient weighting agreement among the top ranks more heavily; Hoeffding's D is a rank statistic testing general, not only monotonic, dependence.
  conf: not stated · class: not stated · holds: the review's glossary · src: none (the review's glossary) · trail: C-RANKNET §Glossary · from: C-RANKNET:B-0187, C-RANKNET:B-0188
- **rank-statistics.4** Theil-Sen and rank Theil-Sen are median-of-pairwise-slopes regression on raw values and on ranks respectively; the raw version is not a rank method.
  conf: not stated · class: not stated · holds: the review's glossary · src: none (the review's glossary) · trail: C-RANKNET §Glossary · from: C-RANKNET:B-0189
- **rank-statistics.5** The comparators in this literature that are not rank-based are Pearson; biweight midcorrelation; mutual information and MIC; proportionality (rho_p, phi_s); SparCC and FastSpar; CCLasso; REBACCA; gCoda; OIPCQ; SPIEC-EASI in glasso and MB modes; FlashWeave; COZINE; HARMONIES; mLDM; and WGCNA with topological overlap.
  conf: not stated · class: not stated · holds: the review's glossary · src: none (the review's glossary) · trail: C-RANKNET §Glossary · from: C-RANKNET:B-0200

### mutual-rank: mutual rank (MR) and logit-MR
needs: rank-device
- **mutual-rank.1** The original argument for ranking is that a Pearson correlation coefficient is not comparable across gene pairs, datasets or preprocessing pipelines: Obayashi and Kinoshita showed that the PCC distribution shifts with sample selection and with the GeneChip summarisation method, so that functionally related genes accumulate at high ranks but at widely different coefficient values.
  conf: not stated · class: meas (note: "measured; four microarray compendia") · holds: four microarray compendia, Arabidopsis 1,388 chips, human 5,188, mouse 2,226, rat 632; unordered cross-sectional samples · src: obayashiRankCorrelationCoefficient2009 · trail: C-RANKNET §The rank device in gene · from: C-RANKNET:B-0023, C-RANKNET:B-0024
- **mutual-rank.2** Obayashi and Kinoshita defined mutual rank as the geometric mean of the two reciprocal Pearson-correlation ranks, sqrt(rank A to B times rank B to A), low being strong, and justified the geometric rather than arithmetic mean on the argument that rank differences act logarithmically: "the impact of the difference of 1 and 3 in PCC rank can be similar with that of 100 and 300". It is used in gene co-expression (ATTED-II, COXPRESdb, plant and animal transcriptomics).
  conf: not stated · class: not stated · holds: gene co-expression · src: obayashiRankCorrelationCoefficient2009 · trail: C-RANKNET §The rank device in gene, §Glossary · from: C-RANKNET:B-0025, C-RANKNET:B-0179
- **mutual-rank.3** Mutual rank is not statistically calibrated by construction: it ranges from 1 to N minus 1, so values are not comparable across platforms with different gene counts, and it is precise near the ends of its range but "easily affected by chance" in the middle, where the error distribution is not normal.
  conf: not stated · class: meas (note: "measured; ATTED-II v9") · holds: ATTED-II v9, 16 platforms, nine plant species, microarray and RNA-seq, 100 bootstrap resamples per platform · src: obayashiATTEDII2018Plant2018 · trail: C-RANKNET §The rank device in gene · from: C-RANKNET:B-0026, C-RANKNET:B-0027
- **mutual-rank.4** The ATTED-II group's fix (logit-MR) is to divide MR by gene number and apply a logit transform, which gives normally distributed error with roughly constant variance and therefore confidence intervals.
  conf: not stated · class: not stated · holds: ATTED-II · src: obayashiATTEDII2018Plant2018 · trail: C-RANKNET §The rank device in gene, §Glossary · from: C-RANKNET:B-0028, C-RANKNET:B-0180
- **mutual-rank.5** The logit-MR fix is a repair to a known defect of the rank index, not evidence that the index wins.
  conf: not stated · class: not stated · holds: ATTED-II's logit-MR · src: obayashiATTEDII2018Plant2018 · trail: C-RANKNET §The rank device in gene · from: C-RANKNET:B-0028, C-RANKNET:B-0029
- **mutual-rank.6** MutRank computes MR for a reference gene's top 200 coexpressed genes (maximum 1,000) rather than all pairs, because "calculating all pair-wise MR values on the resources available on most personal computers is impractical", and needs no temporal ordering.
  conf: not stated · class: not stated · holds: the MutRank R shiny web-application · src: poretskyMutRankRShiny2020 · trail: C-RANKNET §Data requirements · from: C-RANKNET:B-0139, C-RANKNET:R-0042

### hrr: highest reciprocal rank (HRR) and modules on HRR networks
needs: rank-device
- **hrr.1** Highest reciprocal rank is the other rank rule in gene co-expression: an edge survives only if both genes appear in each other's top N list (usually N equal to 30), so HRR is operationally the larger of the two reciprocal ranks; PCC-HRR and SCC-HRR are HRR applied to Pearson or to Spearman coefficients.
  conf: not stated · class: not stated · holds: plant co-expression (AraGenNet, PlaNet, CoNekT) · src: mutwilAssemblyInteractiveCorrelation2010, lieseckeRankingGenomewideCorrelation2018, lieseckeImprovedGeneCoexpression2019 · trail: C-RANKNET §The rank device in gene, §Glossary · from: C-RANKNET:B-0030, C-RANKNET:B-0181, C-RANKNET:B-0182
- **hrr.2** Mutwil and colleagues capped HRR at 30 and weighted edges by band, producing an Arabidopsis network of 103,587 edges over 20,785 nodes against 231,882 edges over only 7,178 nodes for a PCC r at or above 0.8 network on the same data, with 29,956 edges and 6,942 nodes shared.
  conf: not stated · class: meas (note: "measured; 351 RMA-normalised ATH1 arrays") · holds: 351 RMA-normalised ATH1 arrays, Arabidopsis; the critic could not verify these numbers from any route · src: mutwilAssemblyInteractiveCorrelation2010 · trail: C-RANKNET §The rank device in gene, §Full-text breaches · limit: access (critic: C-012) · from: C-RANKNET:B-0031, C-RANKNET:C-012..014
- **hrr.3** Mutwil and colleagues' stated motivation for HRR is coverage, not accuracy: an r cutoff leaves genes with narrow correlation distributions unconnected, illustrated by the redundant transcription factors MYB33 and MYB65, which correlate at r equal to 0.7 and so miss an r equal to 0.8 cutoff but sit second in each other's lists.
  conf: not stated · class: not stated · holds: Mutwil et al.'s Arabidopsis HRR network; the MYB33/MYB65 example is unverified by the critic · src: mutwilAssemblyInteractiveCorrelation2010 · trail: C-RANKNET §The rank device in gene, §Full-text breaches · limit: access (critic: C-012) · from: C-RANKNET:B-0031, C-RANKNET:B-0032, C-RANKNET:C-012, C-RANKNET:C-014
- **hrr.4** Mutwil and colleagues justify ranking by citing Obayashi and Kinoshita rather than by running their own rank-versus-magnitude accuracy comparison.
  conf: not stated · class: not stated · holds: Mutwil et al. 2010 · src: mutwilAssemblyInteractiveCorrelation2010 · trail: C-RANKNET §The rank device in gene · from: C-RANKNET:B-0033
- **hrr.5** Module detection built for rank networks exists and has been compared, but only against other clustering algorithms on a fixed rank network: the Heuristic Cluster Chiseling Algorithm grows a node vicinity network around a seed and removes nodes better connected outside it, and on the Arabidopsis HRR-30 network it gave the best modularity against MCL, k-means and MCODE, a Davies-Bouldin index comparable to MCL and MCODE, and robustness of adjusted Rand index 0.3818 (4 percent standard deviation) when 20 percent of genes were dropped.
  conf: not stated · class: not stated · holds: the Arabidopsis HRR-30 network; the critic could not verify the adjusted Rand index 0.3818 · src: mutwilAssemblyInteractiveCorrelation2010 · trail: C-RANKNET §Head to head, §Glossary, §Full-text breaches · limit: access (critic: C-012) · from: C-RANKNET:B-0074, C-RANKNET:B-0075, C-RANKNET:B-0184, C-RANKNET:C-012, C-RANKNET:C-014
- **hrr.6** The HCCA comparison makes no comparison of rank-built against magnitude-built networks.
  conf: not stated · class: not stated · holds: the HCCA benchmark on the Arabidopsis HRR-30 network · src: mutwilAssemblyInteractiveCorrelation2010 · trail: C-RANKNET §Head to head · from: C-RANKNET:B-0075, C-RANKNET:B-0076

### rank-aggregation: ranks as an aggregation device
needs: rank-device, hrr
- **rank-aggregation.1** A third use of ranks in gene co-expression is as an aggregation device rather than an association measure: Ballouz, Verleyen and Gillis replace each within-experiment correlation with its rank in that network before averaging networks across experiments (a rank-standardised network), so that "changes in the distribution of actual correlations (induced by sample size dependencies) have no impact on our results".
  conf: not stated · class: meas (note: "measured; 50 human RNA-seq experiments") · holds: 50 human RNA-seq experiments, 1,970 samples, plus 30 microarray experiments; guilt-by-association AUROC against GO; Gillis lab, EGAD · src: ballouzGuidanceRNAseqCoexpression2015 · trail: C-RANKNET §The rank device in gene, §Glossary · from: C-RANKNET:B-0034, C-RANKNET:B-0035, C-RANKNET:B-0183
- **rank-aggregation.2** In Ballouz and colleagues' work, aggregating lifted average AUROC from about 0.585 for individual networks to about 0.7, matching the microarray aggregate.
  conf: not stated · class: not stated · holds: human RNA-seq co-expression networks; guilt-by-association AUROC against GO · src: ballouzGuidanceRNAseqCoexpression2015 · trail: C-RANKNET §The rank device in gene · from: C-RANKNET:B-0035, C-RANKNET:B-0036
- **rank-aggregation.3** The measured gain in Ballouz and colleagues' work is attributable to aggregation; the paper reports no ranked-against-unranked head-to-head.
  conf: not stated · class: not stated · holds: Ballouz, Verleyen and Gillis 2015 · src: ballouzGuidanceRNAseqCoexpression2015 · trail: C-RANKNET §The rank device in gene · from: C-RANKNET:B-0037
- **rank-aggregation.4** When HRR values were used as the edge weight during aggregation of many small networks, co-occurrence aggregation (keeping edges that recur across networks) was significantly more predictive on GO AUROC: +0.02 against -0.016, Student's t test, p < 2e-16.
  conf: not stated · class: meas (note: "measured; Arabidopsis microarray and RNA-seq compendia") · holds: Arabidopsis microarray and RNA-seq compendia, six aggregation methods, HRR as the base weight throughout; the p value is the critic's reading of the source · src: lieseckeImprovedGeneCoexpression2019 · trail: C-RANKNET §Head to head, §Reference errors · from: C-RANKNET:B-0067, C-RANKNET:C-046
- **rank-aggregation.5** The aggregation result bounds the use of the rank value as a carried quantity, not the rank construction itself.
  conf: not stated · class: not stated · holds: HRR as an aggregation weight · src: lieseckeImprovedGeneCoexpression2019 · trail: C-RANKNET §Head to head · from: C-RANKNET:B-0067, C-RANKNET:B-0068

### expression-benchmarks: ranked against unranked in expression data
needs: mutual-rank, hrr, rank-statistics
- **expression-benchmarks.1** Five studies in gene expression put the ranked-against-unranked comparison directly, and they do not agree, because they do not score the same thing.
  conf: not stated · class: not stated · holds: bulk gene expression · src: none (the reviewer's synthesis) · trail: C-RANKNET §Head to head · from: C-RANKNET:B-0038
- **expression-benchmarks.2** Across four species and all three GO branches, PCC rank and mutual rank predicted a gene's GO annotation from its neighbours better than raw PCC, for all four summarisation methods, with MR and PCC rank statistically indistinguishable from each other; the authors conclude that "the relatively higher performance of PCC rank is a general feature". This rank-of-coefficient result is the one study that tested it directly.
  conf: single (critic: C-006) · class: meas (critic: C-002) · holds: microarray compendia of four species, GO prediction from neighbours; SINGLE SOURCE for mutual rank specifically · src: obayashiRankCorrelationCoefficient2009 · trail: C-RANKNET §Head to head, §critic · from: C-RANKNET:B-0024, C-RANKNET:B-0039..0041, C-RANKNET:C-002, C-RANKNET:C-003, C-RANKNET:C-006, C-RANKNET:A-042, C-RANKNET:A-045
- **expression-benchmarks.3** In Obayashi and Kinoshita's benchmark the absolute AUC values are only shown in figures whose axes deliberately do not start at 0.5, so the size of the gain cannot be extracted from the text.
  conf: not stated · class: not stated · holds: Obayashi and Kinoshita 2009 · src: obayashiRankCorrelationCoefficient2009 · trail: C-RANKNET §Head to head · from: C-RANKNET:B-0041
- **expression-benchmarks.4** Obayashi and Kinoshita 2009 also reports Spearman value approximately equal to Pearson value in the same paper (Supplementary Fig. S3), while PCC rank does not behave like Pearson value: the cleanest internal evidence that rank of the coefficient and rank of the value behave differently. The review read this full text and did not report it.
  conf: not stated · class: not stated · holds: Obayashi and Kinoshita 2009 · src: obayashiRankCorrelationCoefficient2009 · trail: C-RANKNET §critic, §Verdict assessment, §Scope drift · from: C-RANKNET:C-003, C-RANKNET:A-042, C-RANKNET:A-038, C-RANKNET:C-084
- **expression-benchmarks.5** Liesecke and colleagues built global and pathway-level networks from 9,953 ATH1 microarrays and 1,676 RNA-seq samples under seven normalisations, with six measures including PCC, SCC, PCC-HRR, SCC-HRR, mutual information and partial correlation, scored against GO and against five curated pathways with known sub-pathway structure.
  conf: not stated · class: meas (note: "measured; unordered cross-sectional samples") · holds: Arabidopsis; unordered cross-sectional samples · src: lieseckeRankingGenomewideCorrelation2018 · trail: C-RANKNET §Head to head · from: C-RANKNET:B-0042
- **expression-benchmarks.6** In Liesecke and colleagues' pathway-level (Pathway Level Correlation) subnetworks, averaged over five pathways in the RNA-seq normalisation comparison, ranking nearly doubled modularity (0.35 raw against 0.68 HRR) and raised the normalised chi-squared statistic for recovering the known sub-pathway partitions (0.20 against 0.35), both at p below 2.2e-16, while on neighbour-voting AUROC against GO the raw coefficients were better, 0.58 against 0.57, p below 0.01. These are not genome-wide results.
  conf: single (critic: C-025) · class: meas (note: "measured; unordered cross-sectional samples") · holds: pathway-level co-expression subnetworks averaged over five pathways, RNA-seq normalisation comparison, not the genome-wide benchmark; the critic: the structural win rests entirely on this study and on its pathway-level analysis · src: lieseckeRankingGenomewideCorrelation2018 · trail: C-RANKNET §Head to head, §Reference errors, §Search record · from: C-RANKNET:B-0042..0044, C-RANKNET:B-0214, C-RANKNET:C-025, C-RANKNET:C-037, C-RANKNET:A-034
- **expression-benchmarks.7** Liesecke and colleagues describe the pathway-level result as a trade-off in which "guide genes were clustered correctly at the expense of capturing GO associated gene pairs".
  conf: not stated · class: not stated · holds: pathway-level co-expression subnetworks · src: lieseckeRankingGenomewideCorrelation2018 · trail: C-RANKNET §Head to head · from: C-RANKNET:B-0045
- **expression-benchmarks.8** At the global level Liesecke and colleagues conclude that "HRR CCs are able to generate complete genome-wide networks with good performances similar to other classical measures such a MI and PC", which is a null, not a loss.
  conf: not stated · class: not stated · holds: genome-wide networks, Arabidopsis · src: lieseckeRankingGenomewideCorrelation2018 · trail: C-RANKNET §Verdict assessment, §Reference errors · from: C-RANKNET:A-035, C-RANKNET:C-039
- **expression-benchmarks.9** In Liesecke and colleagues' pathway-level intersection analysis, PCC-HRR gave 550 co-occurring edges against 18,334 for mutual information, averaged over five pathways; the 75 percent guide-gene, modularity 0.78 and chi-squared 0.70 intersection figures sit in Figure 7 panels and were not read as numbers.
  conf: not stated · class: not stated · holds: pathway-level intersection counts, averaged over five pathways · src: lieseckeRankingGenomewideCorrelation2018 · trail: C-RANKNET §Search record · from: C-RANKNET:B-0215
- **expression-benchmarks.10** At a fixed budget of one million edges in Liesecke and colleagues' study, PCC-HRR gave 26,645 vertices at mean degree 116 and SCC-HRR 24,731 at degree 124, whereas raw PCC gave 13,164 at degree 511 and raw SCC 9,986 at degree 465: ranking spreads the same edges across roughly twice as many genes at a quarter of the hub degree.
  conf: single (critic: C-025) · class: not stated · holds: one million edges, Arabidopsis co-expression; the critic: rests entirely on Liesecke et al. 2018 · src: lieseckeRankingGenomewideCorrelation2018 · trail: C-RANKNET §Head to head, §Single-source claims · from: C-RANKNET:B-0042, C-RANKNET:B-0047..0049, C-RANKNET:C-025
- **expression-benchmarks.11** Partial correlation networks in Liesecke and colleagues' study sat at chance (neighbour-voting AUROC 0.5) and were not rescued by any other metric.
  conf: not stated · class: not stated · holds: Liesecke et al. 2018 · src: lieseckeRankingGenomewideCorrelation2018 · trail: C-RANKNET §Head to head · from: C-RANKNET:B-0050
- **expression-benchmarks.12** Kumari and colleagues compared eight association measures on 108 Arabidopsis ATH1 arrays and 189 human embryonic stem cell arrays; against AraCyc pathway co-membership for 576 genes in 30 pathways, Spearman, Kendall and Hoeffding's D were the effective measures, and "the widely used Pearson method is generally less efficient, and so is the Distance Covariance method".
  conf: not stated · class: meas (note: "measured") · holds: 108 Arabidopsis ATH1 arrays and 189 human embryonic stem cell arrays; AraCyc pathway co-membership, 576 genes in 30 pathways; a small-sample benchmark · src: kumariEvaluationGeneAssociation2012 · trail: C-RANKNET §Head to head · from: C-RANKNET:B-0051, C-RANKNET:B-0052
- **expression-benchmarks.13** On Kumari and colleagues' curated coordinated-transcription-factor task, the top seven clusters recovered 40 positive TFs for Theil-Sen, rank Theil-Sen, Spearman and weighted rank, then 36 for Hoeffding, 31 for Kendall, 28 for Pearson and 27 for distance covariance, with mean per-cluster positive rates of 74 percent (Hoeffding), 70 (Kendall), 68 (rank Theil-Sen), 65 (Spearman), 65 (weighted rank) and 55 (Theil-Sen).
  conf: not stated · class: not stated · holds: the curated coordinated-transcription-factor task, top seven clusters · src: kumariEvaluationGeneAssociation2012 · trail: C-RANKNET §Head to head · from: C-RANKNET:B-0053
- **expression-benchmarks.14** In Kumari and colleagues' study Theil-Sen, a median-of-pairwise-slopes estimator on raw values and not a rank statistic, tied for first on the TF task, so the ordering is not cleanly "rank beats magnitude"; rank-family measures are ahead of Pearson on two curated truth sets, with the non-rank estimator tying for first on one of them.
  conf: not stated · class: not stated · holds: the TF task and the AraCyc pathway task · src: kumariEvaluationGeneAssociation2012 · trail: C-RANKNET §Head to head, §Verdicts · from: C-RANKNET:B-0054, C-RANKNET:B-0055, C-RANKNET:A-007
- **expression-benchmarks.15** Kumari and colleagues conclude that the ranking of methods is "largely contingent upon the biological processes, which necessitates the pre-analysis to identify the best performing method": Kendall was sixth of eight on the Arabidopsis TF task and first on the human data.
  conf: not stated · class: not stated · holds: Arabidopsis and human expression data · src: kumariEvaluationGeneAssociation2012 · trail: C-RANKNET §Head to head · from: C-RANKNET:B-0056, C-RANKNET:A-007
- **expression-benchmarks.16** Kumari and colleagues' sensitivity, specificity and predicted-accuracy figures for the pathway task rest on an ad hoc definition of true and false negatives drawn from three slices of the ranked pair list, and the numbers themselves were not read by the review.
  conf: not stated · class: not stated · holds: the AraCyc pathway task · src: kumariEvaluationGeneAssociation2012 · trail: C-RANKNET §Head to head · limit: access (note: "the numbers themselves live in a supplementary table I did not read") · from: C-RANKNET:B-0057
- **expression-benchmarks.17** In Vandenbon's sweep, "Using Spearman's correlation instead of Pearson correlation resulted on average in a 0.011 decrease in Quality (equivalent to a 8.2% decrease in sample count)", where Quality is the first principal component of quality measures based on enrichment of functional annotations and of regulatory motifs in promoters, a composite network-quality score.
  conf: not stated · class: meas (note: "measured") · holds: 7,200 co-expression networks from 8,796 human and 12,114 mouse bulk RNA-seq samples across 144 cell types and tissues under 50 workflows · src: vandenbonEvaluationCriticalData2022 · trail: C-RANKNET §Head to head, §Reference errors · from: C-RANKNET:B-0058, C-RANKNET:B-0059, C-RANKNET:C-004, C-RANKNET:C-043, C-RANKNET:C-044
- **expression-benchmarks.18** In Vandenbon's sweep, for small datasets (sample count < 30) Spearman's correlation had on average an advantage over Pearson, with Pearson ahead for roughly 30 to 100 samples and the gap shrinking above that; the recommended workflow uses Spearman only below 30 samples.
  conf: single (critic: C-022) · class: meas (note: "measured") · holds: bulk RNA-seq, human and mouse; one study, one data type, one composite metric · src: vandenbonEvaluationCriticalData2022 · trail: C-RANKNET §Head to head, §What sequencing count, §Single-source claims · from: C-RANKNET:B-0058, C-RANKNET:B-0060, C-RANKNET:B-0061, C-RANKNET:B-0134, C-RANKNET:C-022
- **expression-benchmarks.19** The mechanism Vandenbon gives for the small-sample advantage is that rank correlation is less sensitive to extreme values, which matters most when few samples are present.
  conf: not stated · class: not stated · holds: bulk RNA-seq · src: vandenbonEvaluationCriticalData2022 · trail: C-RANKNET §Head to head, §What sequencing count · from: C-RANKNET:B-0062, C-RANKNET:B-0134
- **expression-benchmarks.20** In Vandenbon's sweep the correlation measure mattered far less than normalisation, batch correction or sample count.
  conf: not stated · class: not stated · holds: bulk RNA-seq, human and mouse · src: vandenbonEvaluationCriticalData2022 · trail: C-RANKNET §Head to head, §What sequencing count · from: C-RANKNET:B-0058, C-RANKNET:B-0063, C-RANKNET:B-0132
- **expression-benchmarks.21** Song, Langfelder and Horvath compared co-expression measures on eight empirical datasets from n equal to 44 to n equal to 1,084 and state "In our study we find that all 3 correlation measures lead to very similar findings", with the supplementary comparison of bicor, Pearson and Spearman concluding "All three types of correlation are similar in terms of GO enrichment".
  conf: not stated · class: not stated · holds: eight empirical datasets, n 44 to 1,084, inside WGCNA · src: songComparisonCoexpressionMeasures2012 · trail: C-RANKNET §Head to head · from: C-RANKNET:B-0064, C-RANKNET:B-0065
- **expression-benchmarks.22** Song and colleagues' 6-of-8 significance result is for correlation plus topological overlap against mutual information, not for Spearman against Pearson.
  conf: not stated · class: not stated · holds: Song, Langfelder and Horvath 2012 · src: songComparisonCoexpressionMeasures2012 · trail: C-RANKNET §Head to head · from: C-RANKNET:B-0066
- **expression-benchmarks.23** Wisecaver and colleagues built MR networks from 21,876 experiments across eight plant species and detected overlapping modules with ClusterONE; their MR-versus-PCC claim is about comparability, not accuracy: "MR-based networks consistently included nearly all genes in a given data set, regardless of the MR threshold stringency employed; that was not the case with PCC-based networks", and no AUC or precision comparison against PCC is reported.
  conf: not stated · class: meas (note: "measured") · holds: 21,876 experiments across eight plant species · src: wisecaverGlobalCoexpressionNetwork2017 · trail: C-RANKNET §Head to head · from: C-RANKNET:B-0070, C-RANKNET:B-0071
- **expression-benchmarks.24** Against known truth, Wisecaver and colleagues' MR modules recovered experimentally validated pathways (14 of 34 aliphatic glucosinolate genes in a single 17-gene N1 module, rising to 56.3 and 71.9 percent in the larger N2 and N3 modules; validated biosynthetic gene clusters at median MR 17.4, P equal to 3.20e-4); this is the closest thing to a truth-based test of mutual rank modules.
  conf: not stated · class: not stated · holds: specialized metabolic pathways in plants, eight plant species · src: wisecaverGlobalCoexpressionNetwork2017 · trail: C-RANKNET §Head to head · from: C-RANKNET:B-0069, C-RANKNET:B-0070, C-RANKNET:B-0072, C-RANKNET:R-0022
- **expression-benchmarks.25** Wisecaver and colleagues' MR modules failed on computationally predicted clusters (EC-based clusters median MR 9,670, P equal to 0.187; antiSMASH clusters median MR 10,890, P equal to 0.027, significantly worse than controls; only 7 of 188 putative clusters overlapped a module by three or more genes): a negative result about the predicted clusters, not about MR, that shows how a rank network behaves when the truth set is wrong.
  conf: not stated · class: not stated · holds: computationally predicted gene clusters, eight plant species · src: wisecaverGlobalCoexpressionNetwork2017 · trail: C-RANKNET §Head to head · from: C-RANKNET:B-0070, C-RANKNET:B-0072, C-RANKNET:B-0073

### verdict-a: rank against magnitude construction in any data type
needs: expression-benchmarks, rank-aggregation
- **verdict-a.1** Rank-based against magnitude-based network construction has been measured, and the answer splits by which rank device and which criterion, not by "rank versus magnitude" as a single question.
  conf: not stated · class: meas (critic: C-002) · holds: bulk gene expression benchmarks · src: none (the critic's verdict over the review's sources) · trail: C-RANKNET §critic, §Verdict the body · from: C-RANKNET:C-002, C-RANKNET:A-041
- **verdict-a.2** Rank of the value (Spearman, Kendall) is indistinguishable from Pearson (Song et al.), slightly behind on a composite network-quality score except below 30 samples (Vandenbon), and ahead of Pearson on two curated truth sets where a non-rank estimator ties for first (Kumari et al.).
  conf: not stated · class: meas (critic: C-002) · holds: bulk gene expression · src: songComparisonCoexpressionMeasures2012, vandenbonEvaluationCriticalData2022, kumariEvaluationGeneAssociation2012 · trail: C-RANKNET §critic, §Verdict the body · from: C-RANKNET:C-002, C-RANKNET:C-004, C-RANKNET:A-043
- **verdict-a.3** Ranking wins measurably on coverage, modularity and sub-pathway recovery (Liesecke et al. 2018, pathway-level networks; Wisecaver et al.): higher modularity, better recovery of known sub-pathway partitions and roughly twice the vertex coverage at a fixed edge budget, comparable network size across species and datasets, and inclusion of functionally redundant pairs that fall below a fixed coefficient cutoff.
  conf: single (critic: C-025) · class: meas (critic: C-002) · holds: Liesecke et al. 2018 pathway-level networks, Wisecaver et al. across species and datasets, Mutwil et al. for the redundant pairs; reproducible-in-one-study per the critic · src: lieseckeRankingGenomewideCorrelation2018, wisecaverGlobalCoexpressionNetwork2017, mutwilAssemblyInteractiveCorrelation2010 · trail: C-RANKNET §critic, §Verdict the body, §Verdicts, §Single-source claims · from: C-RANKNET:C-002, C-RANKNET:C-005, C-RANKNET:C-006, C-RANKNET:C-025, C-RANKNET:A-044, C-RANKNET:A-006, C-RANKNET:R-0009
- **verdict-a.4** In sum, measured: no general accuracy advantage for rank of the value, one unreplicated accuracy advantage for rank of the coefficient, and structural advantages reproducible in one study.
  conf: not stated · class: meas (critic: C-006) · holds: bulk gene expression · src: none (the critic's verdict over the review's sources) · trail: C-RANKNET §critic, §Verdict the body · from: C-RANKNET:C-006, C-RANKNET:A-045
- **verdict-a.5** The review's sensitivity check for its own pooled Part A verdict: removing Obayashi and Kinoshita removes the strongest pro-rank result and strengthens that verdict; removing Vandenbon, Liesecke et al. 2018 or Song et al. still leaves two independent null-or-negative results on function-prediction accuracy.
  conf: not stated · class: not stated · holds: the review's Part A verdict as delivered, which the critic replaced ("Use this verdict, not the one above") · src: obayashiRankCorrelationCoefficient2009, vandenbonEvaluationCriticalData2022, lieseckeRankingGenomewideCorrelation2018, songComparisonCoexpressionMeasures2012 · trail: C-RANKNET §Verdicts, §critic · from: C-RANKNET:A-016, C-RANKNET:A-017, C-RANKNET:C-001

### microbial-rank-devices: rank devices used on microbial abundance data
needs: rank-device, rank-statistics, mutual-rank, hrr
- **microbial-rank-devices.1** On microbial abundance data the rank device is the rank of the abundance value, used in three ways: Spearman and Kendall as edge measures, a copula estimator built on Kendall's tau (SPRING), and a rank-vector normal transform inside a time-series method (eLSA).
  conf: not stated · class: not stated · holds: microbial abundance data · src: peschelNetCoMiNetworkConstruction2021, yoonMicrobialNetworksSPRING2019, xiaExtendedLocalSimilarity2011 · trail: C-RANKNET §The rank device in microbial · from: C-RANKNET:B-0078, C-RANKNET:B-0079, C-RANKNET:B-0081, C-RANKNET:B-0084
- **microbial-rank-devices.2** Spearman and Kendall are the microbiome field's default "correlation-based" options and are offered as such in the standard tooling; they require only unordered cross-sectional samples.
  conf: not stated · class: not stated · holds: microbiome network tooling (NetCoMi) · src: peschelNetCoMiNetworkConstruction2021 · trail: C-RANKNET §The rank device in microbial · from: C-RANKNET:B-0079, C-RANKNET:B-0080
- **microbial-rank-devices.3** The review's searches found no study applying mutual rank or highest reciprocal rank to microbial abundance data: Europe PMC returned five multi-omics hits in which mutual rank was applied to the gene side only, and the top hit, opened in full, confirms the split: co-expressed genes were "selected with a Pearson's correlation coefficient higher than 0.75 and a Mutual Rank of at least 2.2", while the microbial side used Spearman's rank correlations on OTUs.
  conf: not stated · class: search (note: "Each statement is about the searches run, not about what the literature has ruled out") · holds: routes: web searches pairing "mutual rank" and "highest reciprocal rank" with microbiome, taxa, co-abundance, metagenomic, OTU and 16S; Europe PMC exact-phrase search for "mutual rank" with microbiome, microbial, OTU or 16S; the routes are inherited from the search agents, the synthesis agent could not run new keyword searches · src: kudjordjieFusariumOxysporumDisrupts2022 · trail: C-RANKNET §Gaps, with the routes, §Search record · search: searched, not found (note: "Each statement is about the searches run, not about what the literature has ruled out") · from: C-RANKNET:B-0170..0172, C-RANKNET:B-0223..0226

### compositional-closure: compositional closure
needs: microbial-rank-devices
- **compositional-closure.bg1** Microbiome datasets generated by high-throughput sequencing are compositional because the instrument imposes an arbitrary total, so only relative abundances are available.
  kind: background · ref: gloorMicrobiomeDatasetsCompositional2017 · check: DOI 10.3389/fmicb.2017.02224 resolves on Crossref (Front. Microbiol. 8:2224); stated in the abstract and the Figure 1 legend
- **compositional-closure.1** Rank correlation is partially, not fully, protected from compositional closure: Friedman and Alm demonstrated compositional distortion in Spearman as well as Pearson and found Spearman "only marginally better", and Weiss and colleagues found rank measures "less affected by compositional data but still not immune".
  conf: not stated · class: not stated · holds: simulated microbial abundance data · src: friedmanInferringCorrelationNetworks2012, weissCorrelationDetectionStrategies2016 · trail: C-RANKNET §What sequencing count · from: C-RANKNET:B-0085, C-RANKNET:B-0108, C-RANKNET:B-0116, C-RANKNET:B-0117
- **compositional-closure.2** Friedman and Alm state that compositional methods "for inferring more general dependencies between components, equivalent to rank correlations and mutual information for non-compositional data, have not yet been developed", a gap that remained open when SPRING was introduced seven years later.
  conf: not stated · class: not stated · holds: compositional microbial data · src: friedmanInferringCorrelationNetworks2012, yoonMicrobialNetworksSPRING2019 · trail: C-RANKNET §The rank device in microbial · from: C-RANKNET:B-0107

### spring: SPRING, a rank-based copula estimator
needs: microbial-rank-devices, compositional-closure, known-truth
- **spring.1** SPRING (Semi-Parametric Rank-based INference in Graphical models) estimates a latent correlation from Kendall's tau through a closed-form bridge function for a truncated Gaussian copula, with an estimated zero truncation threshold, so exact zeros are modelled rather than replaced by pseudocounts, then runs Meinshausen-Buhlmann neighbourhood selection with StARS.
  conf: not stated · class: not stated · holds: microbiome count data · src: yoonMicrobialNetworksSPRING2019 · trail: C-RANKNET §The rank device in microbial, §Glossary · from: C-RANKNET:B-0081, C-RANKNET:B-0190
- **spring.2** For relative-abundance input SPRING first applies a modified clr (mclr) transform, pseudocount-free, that is "invariant to the addition of extra zero components, preserves the original zero measurements, and is overall rank-preserving".
  conf: not stated · class: not stated · holds: relative-abundance input · src: yoonMicrobialNetworksSPRING2019 · trail: C-RANKNET §The rank device in microbial, §Glossary · from: C-RANKNET:B-0082, C-RANKNET:B-0191
- **spring.3** SPRING is rank-based but not compositionally aware when run on relative abundances, by its authors' own statement that the mclr transform "does not take into the account the compositional nature of the data".
  conf: not stated · class: not stated · holds: relative-abundance input · src: yoonMicrobialNetworksSPRING2019 · trail: C-RANKNET §The rank device in microbial, §What sequencing count, §Search record · from: C-RANKNET:B-0083, C-RANKNET:B-0118, C-RANKNET:B-0219
- **spring.4** Yoon, Gaynanova and Müller report SPRING with the highest AUPR of four methods on synthetic quantitative microbiome counts: 0.95 against 0.91 for SPIEC-EASI on a band graph at n equal to 2000 and p equal to 100, 0.95 against 0.93 on a cluster graph, 0.96 against 0.93 on scale-free, and at n equal to 500 with p equal to 200, 0.93/0.89, 0.90/0.83 and 0.58/0.55, with Pearson-based neighbourhood selection far behind throughout (0.42, 0.32, 0.26, 0.20, 0.25, 0.01).
  conf: not stated · class: model (note: "every entry is a simulation") · holds: synthetic quantitative microbiome counts; band, cluster and scale-free graphs; n 2000 with p 100, and n 500 with p 200; the authors' own simulations · src: yoonMicrobialNetworksSPRING2019 · trail: C-RANKNET §The rank device in microbial · from: C-RANKNET:B-0085, C-RANKNET:B-0087
- **spring.5** SPRING's margin over SPIEC-EASI is small and it vanishes in the hardest regime.
  conf: not stated · class: model (note: "every entry is a simulation") · holds: the authors' simulations · src: yoonMicrobialNetworksSPRING2019 · trail: C-RANKNET §The rank device in microbial · from: C-RANKNET:B-0085, C-RANKNET:B-0088, C-RANKNET:B-0089
- **spring.6** Under distortion of sample totals by a random factor in [0.5, 3], "SPRING is still best or among the best methods for band and cluster graph types, and is outperformed by the compositional methods for scale-free graph type in the low sample size regime", falling to AUPR 0.50 against 0.54 for both compositional methods.
  conf: not stated · class: model (note: "every entry is a simulation") · holds: the authors' simulations with distorted sample totals · src: yoonMicrobialNetworksSPRING2019 · trail: C-RANKNET §The rank device in microbial · from: C-RANKNET:B-0085, C-RANKNET:B-0090
- **spring.7** Table 2 of the SPRING paper shows an input asymmetry: SPRING runs on absolute abundance with no transform, while SPIEC-EASI and invSparCC run on relative abundance, with clr and log SparCC respectively.
  conf: not stated · class: not stated · holds: the SPRING benchmark · src: yoonMicrobialNetworksSPRING2019 · trail: C-RANKNET §The rank device in microbial, §Search record · from: C-RANKNET:B-0091, C-RANKNET:B-0216
- **spring.8** The SPRING authors' own conclusion is that "incorporating quantitative abundance information in the analysis leads to more reliable graphical model inference", which attributes the gain to the data type rather than to the rank estimator.
  conf: not stated · class: not stated · holds: the SPRING benchmark · src: yoonMicrobialNetworksSPRING2019 · trail: C-RANKNET §The rank device in microbial, §Search record · from: C-RANKNET:B-0092, C-RANKNET:B-0217
- **spring.9** The SPRING benchmark does separate the rank estimator from the absolute-abundance input: in Yoon et al.'s own Table 2/Table 3, MB (sample Pearson correlation, absolute abundance, no transform) shares SPRING's input type and scores 0.42/0.32/0.26/0.20/0.25/0.01 AUPR against SPRING's 0.95/0.95/0.96/0.93/0.90/0.58.
  conf: not stated · class: model (critic: C-009) · holds: the authors' simulations · src: yoonMicrobialNetworksSPRING2019 · trail: C-RANKNET §critic, §Verdict assessment, §Scope drift · from: C-RANKNET:C-008, C-RANKNET:C-009, C-RANKNET:A-029, C-RANKNET:A-030, C-RANKNET:A-047, C-RANKNET:C-081
- **spring.10** The SPRING paper's edge-overlap analysis recommends intersecting SPRING, SPIEC-EASI and invSparCC (joint true positive rate 0.95 over roughly 246 edges) rather than using the rank method alone.
  conf: not stated · class: not stated · holds: the SPRING benchmark · src: yoonMicrobialNetworksSPRING2019 · trail: C-RANKNET §The rank device in microbial · from: C-RANKNET:B-0094
- **spring.11** Kishore and colleagues included SPRING among ten methods scored against two synthetic generators and report SpiecEasi as the best individual method (average precision 0.944 on NorTA data, 0.624 on seqtime data), with consensus schemes above it; SPRING is not named as a leader, but its own precision values sit in figures S5 and S6, which the review could not obtain, so the absence of its name is not a measured underperformance.
  conf: not stated · class: model (note: "every entry is a simulation") · holds: two synthetic generators (NorTA, seqtime), ten methods · src: kishoreInferringMicrobialCooccurrence2023 (main text and figure legends; figures S5 and S6 not obtained) · trail: C-RANKNET §The rank device in microbial, §Full-text breaches, §Sources not obtained · limit: access and evidence (critic: C-020) · from: C-RANKNET:B-0085, C-RANKNET:B-0096, C-RANKNET:C-020, C-RANKNET:R-0165..0167
- **spring.12** Ghaeli, Aghdam and Eslahchi evaluated six algorithms on four real 16S datasets under bootstrap, noise and synthetic perturbation, scoring reproducibility (F-score and Jaccard similarity between networks inferred from the perturbed variants) in a paper whose premise is that no gold standard exists; SPRING appears in neither of their two top-performer tables, which are filled by SparCC, gCoda and SPIEC-EASI(glasso).
  conf: not stated · class: not stated · holds: four real 16S datasets; reproducibility, not truth; Tables 3 and 4 only, the supplementary tables not obtained · src: ghaeliEvaluatingMicrobialNetwork2026 (main text only) · trail: C-RANKNET §The rank device in microbial, §Reference errors, §Search record · from: C-RANKNET:B-0098, C-RANKNET:B-0220, C-RANKNET:C-047, C-RANKNET:R-0168..0170
- **spring.13** Ghaeli and colleagues' reported limitation for SPRING, "a general lack of discriminative power, as multiple topologies yielded non-significant differences across all datasets", is reported in the same terms for OIPCQ, gCoda, S-E(glasso) and S-E(mb), so it is a property of the benchmark as much as of SPRING.
  conf: not stated · class: not stated · holds: Ghaeli et al.'s reproducibility benchmark on four real 16S datasets · src: ghaeliEvaluatingMicrobialNetwork2026 · trail: C-RANKNET §The rank device in microbial, §Search record · from: C-RANKNET:B-0099, C-RANKNET:B-0220

### microbial-benchmarks: plain rank against magnitude correlation on simulated microbial data
needs: microbial-rank-devices, compositional-closure, known-truth
- **microbial-benchmarks.1** The benchmark record for rank methods on microbial abundance data is all simulation: modelled throughout, on in silico count tables whose truth is a generated correlation or interaction matrix, not an experimentally verified interaction.
  conf: not stated · class: model (note: "modelled throughout") · holds: Spearman, Kendall, SPRING and eLSA benchmarks on microbial abundance data · src: none (the reviewer's synthesis over the benchmarks) · trail: C-RANKNET §The rank device in microbial · from: C-RANKNET:B-0078, C-RANKNET:B-0079, C-RANKNET:B-0081, C-RANKNET:B-0084..0086
- **microbial-benchmarks.2** Berry and Widder, on generalized Lotka-Volterra metacommunities with a known interaction network: "Pearson and Spearman coefficients had the highest sensitivity, followed by Kendall coefficient and Bray-Curtis dissimilarity, and then Jaccard index (p < 0.05 for all comparisons except Pearson vs. Spearman and Kendall vs. Bray-Curtis)"; Spearman and Pearson were statistically indistinguishable, and Kendall was measurably worse.
  conf: not stated · class: model (note: "every entry is a simulation") · holds: simulated generalized Lotka-Volterra metacommunities · src: berryDecipheringMicrobialInteractions2014 · trail: C-RANKNET §The rank device in microbial · from: C-RANKNET:B-0085, C-RANKNET:B-0102, C-RANKNET:B-0103
- **microbial-benchmarks.3** Hirano and Takemoto, on relative abundances generated by gLV dynamics: "The performance of Spearman's correlation-based and MIC-based methods was almost equal to or higher than those of compositional-data methods because they can consider nonlinear associations", but "Pearson's correlation-based method also exhibited a similar or higher performance than that of the compositional-data methods".
  conf: not stated · class: model (note: "every entry is a simulation") · holds: relative abundances generated by gLV dynamics · src: hiranoDifficultyInferringMicrobial2019 · trail: C-RANKNET §The rank device in microbial · from: C-RANKNET:B-0085, C-RANKNET:B-0104
- **microbial-benchmarks.4** In Hirano and Takemoto's benchmark the best AUPR across all methods was at most about 0.65 at n equal to 50 species and mean degree 2, falling to about 0.45 at mean degree 8.
  conf: not stated · class: model (note: "every entry is a simulation") · holds: gLV-generated relative abundances, 50 species · src: hiranoDifficultyInferringMicrobial2019 · trail: C-RANKNET §The rank device in microbial · from: C-RANKNET:B-0085, C-RANKNET:B-0104, C-RANKNET:B-0105
- **microbial-benchmarks.5** Friedman and Alm, the paper that introduced SparCC: "these compositional effects are not limited to Pearson correlation, and are also present in non-parametric correlations, such as Spearman correlations", and "Spearman correlations performed only marginally better".
  conf: not stated · class: model (note: "every entry is a simulation") · holds: simulated compositional data · src: friedmanInferringCorrelationNetworks2012 · trail: C-RANKNET §The rank device in microbial · from: C-RANKNET:B-0085, C-RANKNET:B-0106
- **microbial-benchmarks.6** Weiss and colleagues, the field's largest correlation benchmark: "Rank-based measures such as MIC and Spearman, as well as Bray-Curtis, are less affected by compositional data but still not immune".
  conf: not stated · class: model (note: "91 simulated OTU tables") · holds: eight tools, 91 simulated OTU tables, 200 to 10,000 features, eight generative models · src: weissCorrelationDetectionStrategies2016 (main text only) · trail: C-RANKNET §The rank device in microbial · from: C-RANKNET:B-0108, C-RANKNET:R-0052
- **microbial-benchmarks.7** In Weiss and colleagues' benchmark Spearman was one of only three tools (with SparCC and LSA) that "correctly identify competitive relationships as mutual exclusions".
  conf: not stated · class: model (note: "91 simulated OTU tables") · holds: 91 simulated OTU tables · src: weissCorrelationDetectionStrategies2016 · trail: C-RANKNET §The rank device in microbial · from: C-RANKNET:B-0108, C-RANKNET:B-0109
- **microbial-benchmarks.8** Kishore and colleagues excluded Pearson and Spearman from all quantitative comparison a priori because "they tend to generate a large number of spurious edges as they are not intended for compositional data sets", which is an assumption rather than a measurement in that paper.
  conf: not stated · class: not stated · holds: Kishore et al. 2023 · src: kishoreInferringMicrobialCooccurrence2023 · trail: C-RANKNET §The rank device in microbial · from: C-RANKNET:B-0097
- **microbial-benchmarks.9** Faust's review reads the record the same way: "Interestingly, in both evaluations, classical correlation measures such as Pearson and Spearman performed often as well as more sophisticated new network inference algorithms".
  conf: not stated · class: assert (note: "asserted") · holds: the evaluations by Weiss 2016 and Hirano and Takemoto 2019 · src: faustOpenChallengesMicrobial2021 (SECONDARY to Weiss 2016 and Hirano and Takemoto 2019) · trail: C-RANKNET §The rank device in microbial · from: C-RANKNET:B-0110, C-RANKNET:B-0111

### microbial-modules: module detection on microbial rank networks
needs: microbial-rank-devices
- **microbial-modules.1** MNetClass builds a Spearman network, partitions it with Walktrap and scores subnetworks with a rank-sum-ratio and entropy-weight model; against six other community detection algorithms on 50 FABIA-simulated matrices with true cluster labels it was significantly better on sensitivity and accuracy and not different from manta or WGCNA on positive predictive value.
  conf: not stated · class: model (note: "50 FABIA-simulated matrices with true cluster labels") · holds: 50 FABIA-simulated matrices with true cluster labels · src: wangMNetClassControlfreeMicrobial2025 · trail: C-RANKNET §The rank device in microbial · from: C-RANKNET:B-0113, C-RANKNET:B-0114
- **microbial-modules.2** In the MNetClass benchmark, edge betweenness, label propagation, leading eigenvector, fast greedy, Louvain and manta used MNetClass's network, while WGCNA was run with "default parameters to automatically construct the network", its own Pearson-based construction; WGCNA is also one of the two comparators MNetClass could not beat on PPV, which makes that comparison partly a rank-versus-magnitude construction comparison.
  conf: not stated · class: not stated · holds: the MNetClass benchmark on simulated matrices · src: wangMNetClassControlfreeMicrobial2025 · trail: C-RANKNET §Reference errors · from: C-RANKNET:C-040..042

### zero-ties: zeros and the rank ties they create
needs: microbial-rank-devices, spring
- **zero-ties.1** Connor, Barberán and Clauset, working on a soil 16S matrix in which "abundance values of zero comprise fully 85% of the matrix", state that "both matrix sparsity and a heavy-tailed distribution of abundances will induce a very large number of multi-way ties, which will then have identical ranks", that the result is an inflated pairwise correlation score under Spearman, and that standard implementations of Spearman's in Matlab, R and Python all rely on the user to correct for ties.
  conf: single (critic: C-021) · class: meas (note: "measured on real data, no truth set") · holds: one soil 16S matrix, 85 percent zeros, no truth set · src: connorUsingNullModels2017 · trail: C-RANKNET §What sequencing count, §Single-source claims · from: C-RANKNET:B-0120..0123, C-RANKNET:C-021
- **zero-ties.2** Connor and colleagues' fix is Monte Carlo tie-breaking with real-valued noise that preserves the original partial ordering, followed by a permutation null; without it the null distribution of rho is disjoint rather than smooth.
  conf: not stated · class: not stated · holds: the soil 16S matrix · src: connorUsingNullModels2017 · trail: C-RANKNET §What sequencing count, §Glossary · from: C-RANKNET:B-0120, C-RANKNET:B-0124, C-RANKNET:B-0192
- **zero-ties.3** Connor and colleagues frame the tie correction as preventing "the spurious conclusion that two taxa are ecologically related because they are both absent from many of the same locations".
  conf: not stated · class: not stated · holds: microbial co-occurrence networks · src: connorUsingNullModels2017 · trail: C-RANKNET §What sequencing count · from: C-RANKNET:B-0125
- **zero-ties.4** SPRING's copula approach attacks the zero-tie problem differently, by estimating a zero truncation threshold from the observed zero count.
  conf: not stated · class: not stated · holds: SPRING · src: yoonMicrobialNetworksSPRING2019 · trail: C-RANKNET §What sequencing count · from: C-RANKNET:B-0126

### elsa: eLSA and LSA, rank transforms on ordered samples
needs: microbial-rank-devices
- **elsa.1** eLSA (extended Local Similarity Analysis) normalises each series by a normal score transformation of the rank vector before local and time-lagged similarity scoring, and requires ordered samples because it scores local and time-delayed subinterval associations.
  conf: single (critic: C-028) · class: not stated · holds: microbial community and other time series with replicates, ordered samples; the critic: rests on the eLSA paper itself · src: xiaExtendedLocalSimilarity2011 · trail: C-RANKNET §The rank device in microbial, §Data requirements, §Single-source claims · from: C-RANKNET:B-0084, C-RANKNET:B-0140, C-RANKNET:B-0193, C-RANKNET:C-028, C-RANKNET:R-0085

### sparsity: sparsity overall
needs: microbial-rank-devices, elsa
- **sparsity.1** In Weiss and colleagues' benchmark raising sparsity from about 40 to about 70 percent zeros "drastically reduces tool performance to little better than random guessing", "precision of the tools is also extremely poor (close to or at zero) under realistic conditions", and among rank-based options only "LSA, and at a few times, MIC and Spearman rise above the 45-degree line; however, not far above the line": no method survives sparsity.
  conf: not stated · class: model (note: "91 simulated OTU tables") · holds: 91 simulated OTU tables · src: weissCorrelationDetectionStrategies2016 · trail: C-RANKNET §What sequencing count · from: C-RANKNET:B-0108, C-RANKNET:B-0127, C-RANKNET:B-0128
- **sparsity.2** In Weiss and colleagues' benchmark the true-to-false-positive ratio "decreases markedly at ~50% OTU sparsity", which is the basis of their recommendation to delete features above that threshold.
  conf: not stated · class: model (note: "91 simulated OTU tables") · holds: 91 simulated OTU tables · src: weissCorrelationDetectionStrategies2016 · trail: C-RANKNET §What sequencing count · from: C-RANKNET:B-0108, C-RANKNET:B-0129
- **sparsity.3** The single best precision figure reported for any rank-normalised tool on the hardest case, sparse Lotka-Volterra relationships, is LSA at 0.2, which is four false positives per true positive; whether this per-tool figure is in the main text read or in the supplementary files not obtained is unsettled.
  conf: not stated · class: not stated · holds: sparse Lotka-Volterra relationships in Weiss et al.'s simulations · src: weissCorrelationDetectionStrategies2016 (main text only) · trail: C-RANKNET §What sequencing count, §Full-text breaches · limit: access (critic: C-015) · from: C-RANKNET:B-0130, C-RANKNET:C-015..018, C-RANKNET:A-040, C-RANKNET:R-0052

### sequencing-depth: uneven sequencing depth
needs: microbial-rank-devices, expression-benchmarks
- **sequencing-depth.1** Uneven sequencing depth is directly addressed only as a normalisation question: Weiss and colleagues tested rarefying, cumulative-sum scaling and DESeq variance stabilisation.
  conf: not stated · class: not stated · holds: Weiss et al.'s simulated OTU tables; per-tool numbers in the unobtained supplement · src: weissCorrelationDetectionStrategies2016 · trail: C-RANKNET §What sequencing count, §Sources not obtained · from: C-RANKNET:B-0108, C-RANKNET:B-0131, C-RANKNET:B-0132, C-RANKNET:R-0161
- **sequencing-depth.2** In the plant work, variance-stabilising and sample-scaling procedures produced networks with average node degree 712 against 114 and average neighbour-voting AUROC 0.47 against 0.62.
  conf: not stated · class: not stated · holds: the plant co-expression work of Liesecke et al. 2018 · src: lieseckeRankingGenomewideCorrelation2018 · trail: C-RANKNET §What sequencing count · from: C-RANKNET:B-0132, C-RANKNET:R-0013
- **sequencing-depth.3** The review found no benchmark isolating depth variation as a factor in rank-versus-magnitude performance, and names no search routes for that statement.
  conf: not stated · class: search (note: "I found no benchmark isolating depth variation") · holds: rank-versus-magnitude benchmarks; no search routes named (the critic) · src: none (the review's search) · trail: C-RANKNET §What sequencing count, §Scope drift · search: searched, not found (note: "I found no benchmark isolating depth variation") · from: C-RANKNET:B-0133, C-RANKNET:C-083

### sample-size: few samples relative to features
needs: expression-benchmarks, microbial-benchmarks
- **sample-size.1** On the microbial side, Berry and Widder found specificity plateaus at about 25 sampling sites while sensitivity keeps rising to 100; the result does not separate rank from magnitude at low n.
  conf: not stated · class: model (note: "every entry is a simulation") · holds: simulated gLV metacommunities · src: berryDecipheringMicrobialInteractions2014 · trail: C-RANKNET §What sequencing count · from: C-RANKNET:B-0085, C-RANKNET:B-0102, C-RANKNET:B-0135
- **sample-size.2** Hirano and Takemoto found performance roughly independent of sample number above 200; the result does not separate rank from magnitude at low n.
  conf: not stated · class: model (note: "every entry is a simulation") · holds: gLV-generated relative abundances · src: hiranoDifficultyInferringMicrobial2019 · trail: C-RANKNET §What sequencing count · from: C-RANKNET:B-0085, C-RANKNET:B-0104, C-RANKNET:B-0135
- **sample-size.3** Tool disagreement in the few-samples regime is severe: Weiss and colleagues report "an average of 31.5% shared edge inference for all pair-wise combinations of tools, and for all data sets/models tested".
  conf: not stated · class: model (note: "91 simulated OTU tables") · holds: Weiss et al.'s simulated OTU tables · src: weissCorrelationDetectionStrategies2016 · trail: C-RANKNET §What sequencing count · from: C-RANKNET:B-0108, C-RANKNET:B-0136

### ordered-samples: ordered samples or not
needs: mutual-rank, hrr, microbial-rank-devices, spring, elsa
- **ordered-samples.1** Every rank-based construction with a benchmark works on unordered cross-sectional samples: mutual rank, HRR, Spearman, Kendall and SPRING all take a feature-by-sample matrix with no ordering variable; eLSA is the exception.
  conf: not stated · class: not stated · holds: benchmarked rank-based constructions · src: obayashiRankCorrelationCoefficient2009, mutwilAssemblyInteractiveCorrelation2010, lieseckeRankingGenomewideCorrelation2018, yoonMicrobialNetworksSPRING2019, peschelNetCoMiNetworkConstruction2021 · trail: C-RANKNET §Data requirements · from: C-RANKNET:B-0137, C-RANKNET:B-0138, C-RANKNET:B-0140

### rank-trajectories: rank through time
needs: rank-device
- **rank-trajectories.1** The rank clock comes from urban demography, where Batty plotted each element's size rank on a radius per time step (a polar plot with rank increasing outward) and defined a rank shift distance and its average over a common set.
  conf: not stated · class: meas (note: "measured; city size rankings, not biological") · holds: city size rankings, not biological · src: battyRankClocks2006 (†: read in full text by a search agent and not re-opened by the reviewer) · trail: C-RANKNET §Rank through time, §Glossary · from: C-RANKNET:B-0020, C-RANKNET:B-0142, C-RANKNET:B-0194
- **rank-trajectories.2** Batty's statement about grouping is a suggestion: different rank trajectories "suggest a possible basis for future classification of city types based on their local dynamics"; no algorithm is given.
  conf: not stated · class: assert (note: "asserted") · holds: city size rankings · src: battyRankClocks2006 (†) · trail: C-RANKNET §Rank through time · from: C-RANKNET:B-0020, C-RANKNET:B-0143, C-RANKNET:B-0144
- **rank-trajectories.3** Collins and colleagues imported the rank clock into plant community ecology and defined mean rank shift (the mean absolute change in relative rank between consecutive years over species present in both) and proportional persistence; mean rank shift is unstandardised, so not comparable across communities of different richness.
  conf: not stated · class: meas (note: "measured; three US LTER grassland and desert datasets") · holds: three US LTER grassland and desert datasets · src: collinsRankClocksPlant2008 (†: read in full text by a search agent and not re-opened by the reviewer) · trail: C-RANKNET §Rank through time, §Glossary · from: C-RANKNET:B-0020, C-RANKNET:B-0145, C-RANKNET:B-0195
- **rank-trajectories.4** Avolio and colleagues redefined the quantity as rank change, standardised by the pooled species number and bounded between 0 and 0.5, and supplied the same quantity as a rank difference between two replicates at a single time, so the comparison also works on unordered replicates; both are implemented in codyn.
  conf: not stated · class: not stated · holds: community ecology (codyn) · src: avolioComprehensiveApproachAnalyzing2019 (†: read in full text by a search agent and not re-opened by the reviewer), hallettCodynRPackage2016 (†) · trail: C-RANKNET §Rank through time, §Glossary · from: C-RANKNET:B-0020, C-RANKNET:B-0146, C-RANKNET:B-0147, C-RANKNET:B-0196
- **rank-trajectories.5** Every one of the rank-through-time metrics is a single scalar per comparison describing the whole community; none produces a pairwise quantity between taxa.
  conf: not stated · class: not stated · holds: rank shift, mean rank shift, rank change and rank difference · src: battyRankClocks2006, collinsRankClocksPlant2008, avolioComprehensiveApproachAnalyzing2019 · trail: C-RANKNET §Rank through time · from: C-RANKNET:B-0148, C-RANKNET:B-0149
- **rank-trajectories.6** Everything in the rank-trajectory family requires ordered samples by definition.
  conf: not stated · class: not stated · holds: the rank-trajectory family · src: none (the reviewer's statement) · trail: C-RANKNET §Data requirements · from: C-RANKNET:B-0141
- **rank-trajectories.7** Larsen and colleagues computed rank shift on vineyard soil 16S and ITS data only for taxa observed in both compared years, so the zero-inflated portion of the table is discarded before ranks are formed, reporting about 20 percent shift for fungi and 11 percent for bacteria.
  conf: not stated · class: not stated · holds: vineyard soils, 16S and ITS · src: larsenDistinctTemporallyStable2023 (†: read in full text by a search agent and not re-opened by the reviewer) · trail: C-RANKNET §Rank through time · from: C-RANKNET:B-0020, C-RANKNET:B-0161, C-RANKNET:B-0162
- **rank-trajectories.8** Yao and colleagues found unstandardised mean rank shift incomparable across communities of different richness: phage MRS between adjacent time points ran from 400 to 1,000, far above bacterial values, which the authors attribute partly to phage taxa simply being more numerous.
  conf: not stated · class: not stated · holds: polyhydroxyalkanoate-producing mixed microbial cultures, phage and bacterial communities between adjacent time points · src: yaoPhagesbacteriaInteractionsUnderlying2025 (†: read in full text by a search agent and not re-opened by the reviewer) · trail: C-RANKNET §Rank through time · from: C-RANKNET:B-0020, C-RANKNET:B-0163, C-RANKNET:R-0136
- **rank-trajectories.9** The codyn reference implementation collapses every absent taxon in a sample to a single shared rank S plus 1, so in a sparse table a large block of taxa carries one identical rank and contributes no rank change; the rule is known from a search agent's read of the package source, not from any full text the reviewer holds.
  conf: not stated · class: not stated · holds: codyn; zero-inflated tables · src: hallettCodynRPackage2016 (†), hallettCodynRPackage2025 (read in full by a search agent) · trail: C-RANKNET §Rank through time, §Full-text breaches, §Sources not obtained (all · limit: access (critic: C-019) · from: C-RANKNET:B-0164, C-RANKNET:C-019, C-RANKNET:R-0300, C-RANKNET:R-0301
- **rank-trajectories.10** codyn handles ties with average ranks.
  conf: not stated · class: not stated · holds: the codyn package source (add_ranks, RAC_change, rank_shift) · src: hallettCodynRPackage2025 (read in full by a search agent, not fetched by the synthesiser) · trail: C-RANKNET §Sources not obtained (all · from: C-RANKNET:R-0298, C-RANKNET:R-0300

### taxon-grouping: whether rank trajectories group taxa
needs: rank-trajectories, microbial-rank-devices
- **taxon-grouping.1** In the studies the reviewer read, rank-through-time metrics have not been used to group taxa: Duran-Pinedo and colleagues used rank clocks and mean rank shift as descriptive summaries of reordering in a 360-sample, 12-month oral microbiome time series, then built the association network with SPIEC-EASI and clustered taxa with a Dirichlet process Gaussian process mixture over abundance trajectories.
  conf: not stated · class: meas (note: "measured; 15 individuals, 45 teeth, 16S and ITS") · holds: human oral microbiome, 360 samples over 12 months, 15 individuals, 45 teeth, 16S and ITS · src: duranpinedoLongtermDynamicsHuman2021 · trail: C-RANKNET §Rank through time, §Search record · from: C-RANKNET:B-0150..0152, C-RANKNET:B-0230
- **taxon-grouping.2** Liu and colleagues defined subcommunities with latent Dirichlet allocation first and then computed Collins-style rank change and evenness change on those subcommunities.
  conf: not stated · class: meas (note: "measured; 59 samples, five sites, two years") · holds: large-river deltaic estuaries, 59 samples, five sites, two years · src: liuMicrobesClimateRefugia2025 · trail: C-RANKNET §Rank through time, §Search record · from: C-RANKNET:B-0153, C-RANKNET:B-0230, C-RANKNET:R-0116
- **taxon-grouping.3** In both the Duran-Pinedo and the Liu studies the rank quantity is reported alongside a separate magnitude-based or log-ratio-based grouping step, never as the basis of one.
  conf: not stated · class: not stated · holds: two microbial time-series studies · src: duranpinedoLongtermDynamicsHuman2021, liuMicrobesClimateRefugia2025 · trail: C-RANKNET §Rank through time · from: C-RANKNET:B-0154
- **taxon-grouping.4** The review's searches found no study using rank clocks, mean rank shift or rank change to build a taxon association network or define taxon modules; in every full-text source located that computes these quantities, they are community-level or taxon-level descriptors reported beside a separate grouping step.
  conf: not stated · class: search (note: "Each statement is about the searches run, not about what the literature has ruled out") · holds: routes: Europe PMC exact-phrase sweeps on "rank clocks" (8 records), "rank clock" (12), "mean rank shift" or "mean rank shifts" (25), and codyn combined with reordering or rank change (18), with every ecological and microbial title inspected; Semantic Scholar graph search for rank-based network construction from abundance time series and for rank trajectory clustering; routes inherited from the search agents · src: duranpinedoLongtermDynamicsHuman2021, liuMicrobesClimateRefugia2025, buckleyMeasuringChangeBiological2021 · trail: C-RANKNET §Gaps, with the routes, §Search record · search: searched, not found (note: "Each statement is about the searches run, not about what the literature has ruled out") · from: C-RANKNET:B-0170, C-RANKNET:B-0177, C-RANKNET:B-0178, C-RANKNET:B-0224, C-RANKNET:B-0229
- **taxon-grouping.5** The benchmarked method for grouping microbial taxa by behaviour across ordered samples is magnitude-based: Ananke normalises counts by per-sample depth, z-scores each trajectory, computes a short time-series slope-difference distance and clusters with DBSCAN, scoring adjusted mutual information above 0.8 against six ground-truth patterns with as few as ten time points, and dropping to median 0.69 at 500 points and 0.62 at 1,000.
  conf: not stated · class: model (note: "modelled; simulated 16S-style series") · holds: simulated 16S-style series, six ground-truth patterns · src: hallAnankeTemporalClustering2017 · trail: C-RANKNET §Rank through time, §Glossary · from: C-RANKNET:B-0155, C-RANKNET:B-0156, C-RANKNET:B-0199
- **taxon-grouping.6** Ananke's comparator set is Euclidean and Manhattan distance on the same standardised trajectories, with no rank-based comparator, and its stated failure mode is that the slope-difference distance cannot separate low-variance from high-variance stationary profiles.
  conf: not stated · class: not stated · holds: simulated 16S-style series · src: hallAnankeTemporalClustering2017 · trail: C-RANKNET §Rank through time · from: C-RANKNET:B-0157
- **taxon-grouping.7** A methods roadmap written for community time series with fewer than 25 temporal replicates lists rank abundance distributions and rank clocks as one of seven method families, described as graphs that "can be combined with dissimilarity methods and rank clocks".
  conf: not stated · class: not stated · holds: community time series with fewer than 25 temporal replicates · src: buckleyMeasuringChangeBiological2021 · trail: C-RANKNET §Rank through time · from: C-RANKNET:B-0158
- **taxon-grouping.8** The roadmap's seven method families contain no rank-based network construction and no rank-based module detection; that absence is the reviewer's reading of the list, not a statement the authors make.
  conf: not stated · class: reading (note: "That absence is my reading of the reviewed list") · holds: Buckley et al. 2021 · src: buckleyMeasuringChangeBiological2021 · trail: C-RANKNET §Rank through time · from: C-RANKNET:B-0159, C-RANKNET:B-0160

### adjacent-instruments: rank instruments that set network structure aside
needs: rank-trajectories
- **adjacent-instruments.1** Rank-turbulence divergence, a tunable rank-rank divergence, compares two ranked lists with fractional ranks for ties and states that "whatever complexities these systems may contain, such as networks of components, we are implicitly leaving them aside".
  conf: not stated · class: not stated · holds: complex systems · src: doddsAllotaxonometryRankturbulenceDivergence2023 (†: read in full text by a search agent and not re-opened by the reviewer) · trail: C-RANKNET §Rank through time, §Glossary · from: C-RANKNET:B-0020, C-RANKNET:B-0165, C-RANKNET:B-0166, C-RANKNET:B-0197
- **adjacent-instruments.2** The physics-of-ranking literature defines rank turnover, rank flux and a rank change probability, temporal descriptors of a ranked list, none of which yields pairwise associations or modules.
  conf: not stated · class: not stated · holds: physics of ranking · src: iniguezDynamicsRanking2022 (†: read in full text by a search agent and not re-opened by the reviewer) · trail: C-RANKNET §Rank through time, §Glossary · from: C-RANKNET:B-0020, C-RANKNET:B-0167, C-RANKNET:B-0198
- **adjacent-instruments.3** In beta-diversity methodology, decoupling of species ranks appears as a simulated truth axis for testing dissimilarity metrics rather than as a method.
  conf: not stated · class: not stated · holds: beta-diversity methodology · src: barwellMeasuringBetadiversitySpecies2015 (†: read in full text by a search agent and not re-opened by the reviewer) · trail: C-RANKNET §Rank through time · from: C-RANKNET:B-0020, C-RANKNET:B-0168

### verdict-b: rank-based network construction on microbial abundance data
needs: microbial-benchmarks, spring, known-truth, taxon-grouping
- **verdict-b.1** On microbial abundance data, measured in simulation only, plain rank correlation as an edge measure performs no better or worse than Pearson: benchmarked at least four times, it was statistically indistinguishable from Pearson and jointly top in gLV metacommunities (Berry and Widder), similar to Pearson and both at or above compositional methods in gLV relative abundances (Hirano and Takemoto), "only marginally better" than Pearson under compositional closure (Friedman and Alm), and less distorted by closure but "still not immune" in the largest correlation benchmark (Weiss et al.).
  conf: repl (critic: C-094) · class: model (critic: C-007) · holds: simulated microbial abundance data; four separate simulation benchmarks; the critic: the verdict would stand without any one of them, and the verdict direction survives on these four · src: berryDecipheringMicrobialInteractions2014, hiranoDifficultyInferringMicrobial2019, friedmanInferringCorrelationNetworks2012, weissCorrelationDetectionStrategies2016 · trail: C-RANKNET §critic, §Verdicts, §Expectation echo · from: C-RANKNET:C-007, C-RANKNET:A-046, C-RANKNET:A-011, C-RANKNET:B-0101, C-RANKNET:C-094, C-RANKNET:C-095, C-RANKNET:A-031
- **verdict-b.2** One rank-based copula estimator (SPRING) beats both Pearson-based and compositional neighbourhood selection in its authors' simulations and loses to compositional methods only in the distorted low-sample scale-free case.
  conf: not stated · class: model (critic: C-009) · holds: the SPRING authors' simulations · src: yoonMicrobialNetworksSPRING2019 · trail: C-RANKNET §critic, §Verdict the body · from: C-RANKNET:C-009, C-RANKNET:A-048
- **verdict-b.3** Nothing on microbial abundance data has been measured against experimentally validated interactions: all of the evidence is modelled, on in silico tables whose truth is a generated matrix, and the field states that no experimentally validated gold standard and no DREAM-style challenge exists.
  conf: not stated · class: model (critic: C-009) · holds: microbial abundance data; the DREAM-style statement rests on Faust 2021 alone (critic) · src: ghaeliEvaluatingMicrobialNetwork2026, faustOpenChallengesMicrobial2021 · trail: C-RANKNET §critic, §Verdicts · from: C-RANKNET:C-009, C-RANKNET:A-013, C-RANKNET:A-014, C-RANKNET:C-027
- **verdict-b.4** Two subfamilies named in the question, reciprocal-rank neighbourhoods and rank trajectories, have never been applied to microbial abundance data, let alone benchmarked there.
  conf: not stated · class: search (note: "Each statement is about the searches run, not about what the literature has ruled out") · holds: the review's searches for mutual rank or HRR on microbial data and for rank clocks, mean rank shift or rank change as a basis for taxon networks or modules · src: none (the review's search) · trail: C-RANKNET §critic, §Verdicts, §Gaps, with the routes · search: searched, not found (note: "Each statement is about the searches run, not about what the literature has ruled out") · from: C-RANKNET:C-009, C-RANKNET:A-015, C-RANKNET:A-048, C-RANKNET:B-0170, C-RANKNET:B-0171, C-RANKNET:B-0177
- **verdict-b.5** The review's sensitivity check for Part B: removing Yoon et al. removes the only pro-rank result and makes the verdict firmer rather than reversing it; removing Weiss et al. still leaves Hirano and Takemoto, Friedman and Alm and Berry and Widder on the same side.
  conf: not stated · class: not stated · holds: the review's Part B verdict · src: yoonMicrobialNetworksSPRING2019, weissCorrelationDetectionStrategies2016, hiranoDifficultyInferringMicrobial2019, friedmanInferringCorrelationNetworks2012, berryDecipheringMicrobialInteractions2014 · trail: C-RANKNET §Verdicts · from: C-RANKNET:A-018, C-RANKNET:A-019

## Do not say
- **dns.1** "Rank-based methods perform no better or worse than magnitude-based methods for building networks, in any data type."
  why: The critic replaced this verdict: the answer splits by which rank device and which criterion, the verdict pooled rank of the coefficient with rank of the value and four incommensurable metrics, and the brief primed a "no better or worse" direction that the review repeated, taking every negative datum at face value and arguing every positive one down. · instead: verdict-a.1, verdict-a.4 · trail: C-RANKNET §critic, §Verdict assessment, §Expectation echo · from: C-RANKNET:A-001, C-RANKNET:A-003, C-RANKNET:A-020, C-RANKNET:A-037, C-RANKNET:C-001, C-RANKNET:C-002, C-RANKNET:C-088..093, C-RANKNET:C-096, C-RANKNET:C-098
- **dns.2** "On function-prediction accuracy against GO, the record is a wash pointing slightly against ranking."
  why: The tally pools rank-of-coefficient and rank-of-value devices and four incommensurable criteria (neighbour-voting AUROC against GO, a composite PC1 quality score including promoter motif enrichment, GO enrichment p-value rankings, and counts of positive transcription factors in top clusters), and the Liesecke number in it belongs to a different analysis level. · instead: verdict-a.2, expression-benchmarks.2 · trail: C-RANKNET §Verdicts, §Scope drift · from: C-RANKNET:A-005, C-RANKNET:C-084, C-RANKNET:C-085
- **dns.3** "In Liesecke and colleagues' genome-wide benchmark, ranking loses slightly on GO accuracy: the raw coefficients scored 0.58 against 0.57."
  why: The 0.58 against 0.57 AUROC (with the 0.35/0.68 modularity and 0.20/0.35 chi-squared pairs) comes from the Pathway Level Correlation subnetworks averaged over five pathways in the RNA-seq normalisation comparison, not from the genome-wide benchmark, whose conclusion is that HRR performs similarly to classical measures: a null, not a loss. · instead: expression-benchmarks.6, expression-benchmarks.8 · trail: C-RANKNET §Head to head, §Verdict assessment, §Reference errors · from: C-RANKNET:B-0042, C-RANKNET:B-0046, C-RANKNET:A-021, C-RANKNET:A-032, C-RANKNET:A-033, C-RANKNET:A-036, C-RANKNET:C-037, C-RANKNET:C-038
- **dns.4** "Vandenbon found Spearman 0.011 lower than Pearson in function-prediction accuracy against GO."
  why: Vandenbon's Quality is the first principal component of quality measures based on enrichment of functional annotations and of regulatory motifs in promoters, so listing it alongside neighbour-voting AUROC as the same criterion pools incommensurable metrics. · instead: expression-benchmarks.17 · trail: C-RANKNET §Reference errors · from: C-RANKNET:C-043..045
- **dns.5** "Bulk gene expression is the only data type in which the rank-against-magnitude comparison has been run properly."
  why: This evaluates the quality of other fields' research designs, which the brief forbids; the defensible statement is that other data types' benchmarks are simulation-based or unobtained, not that they are improper. · instead: microbial-benchmarks.1 · trail: C-RANKNET §Verdicts, §Scope drift · from: C-RANKNET:A-004, C-RANKNET:C-082
- **dns.6** "Rank correlation has a reproducible advantage at small sample size: Spearman beats Pearson below 30 samples."
  why: The advantage comes from one study (Vandenbon 2022), one data type (bulk RNA-seq) and one composite metric, and reproducible implies replication the body does not contain. · instead: expression-benchmarks.18 · trail: C-RANKNET §What sequencing count, §Single-source claims, §Scope drift · from: C-RANKNET:B-0134, C-RANKNET:A-009, C-RANKNET:C-022..024, C-RANKNET:C-086
- **dns.7** "Ranking has a specific, reproducible advantage in coverage, comparability and module structure."
  why: The structural win rests entirely on Liesecke et al. 2018, and on its pathway-level analysis, so a single-study result is being presented as a field property. · instead: verdict-a.3 · trail: C-RANKNET §Verdicts, §Single-source claims, §Scope drift · from: C-RANKNET:A-009, C-RANKNET:C-025, C-RANKNET:C-086
- **dns.8** "The evidence does not support a general accuracy advantage for ranking."
  why: The critic splits it by device: there is no general accuracy advantage for rank of the value, but there is one unreplicated accuracy advantage for rank of the coefficient. · instead: verdict-a.4 · trail: C-RANKNET §Verdicts, §critic · from: C-RANKNET:A-008, C-RANKNET:C-006
- **dns.9** "SPRING's benchmark cannot separate a rank-based win from an absolute-abundance win, and no published study separates them."
  why: The fourth method in the same tables, MB, runs sample Pearson correlation on absolute abundance with no transform, sharing SPRING's input type, and is far behind SPRING in every cell; the absence claim names no search routes, and the review argued down this one pro-rank result on a confound argument the source's own tables refute. · instead: spring.9 · trail: C-RANKNET §The rank device in microbial, §Verdict assessment, §Scope drift, §Expectation echo · from: C-RANKNET:B-0093, C-RANKNET:A-012, C-RANKNET:A-021, C-RANKNET:A-026..031, C-RANKNET:C-008, C-RANKNET:C-081, C-RANKNET:C-097
- **dns.10** "Independent evaluations do not reproduce a SPRING advantage: SPRING is not a top performer in either of the two independent evaluations."
  why: In Kishore et al. this is inferred from SPRING not being named, while its values sit in figures the review could not obtain, and the absence of a name is not a measured underperformance; Ghaeli et al. measure reproducibility on real data with no truth set, so the two are not evaluations of performance of the same kind as the simulation benchmarks. · instead: spring.11, spring.12 · trail: C-RANKNET §The rank device in microbial, §Full-text breaches, §Reference errors, §Scope drift · from: C-RANKNET:B-0095, C-RANKNET:A-012, C-RANKNET:C-020, C-RANKNET:C-047, C-RANKNET:C-087
- **dns.11** "In the MNetClass benchmark every comparator used the same Spearman network, so it says nothing about rank against magnitude construction."
  why: WGCNA was run with its own default, Pearson-based construction, and it is one of the two comparators MNetClass could not beat on PPV, which makes that comparison partly a rank-versus-magnitude construction comparison. · instead: microbial-modules.2 · trail: C-RANKNET §The rank device in microbial, §Reference errors, §Search record · from: C-RANKNET:B-0115, C-RANKNET:B-0231, C-RANKNET:C-040..042
- **dns.12** "Co-occurrence aggregation beat HRR-weighted aggregation on GO AUROC at p below 0.001."
  why: The source reports +0.02 against -0.016 GO AUROC, Student's t test, p < 2e-16; p below 0.001 is the figure's asterisk threshold, not the reported p value. · instead: rank-aggregation.4 · trail: C-RANKNET §Head to head, §Reference errors · from: C-RANKNET:B-0067, C-RANKNET:C-046
- **dns.13** "Zero-induced rank ties inflate Spearman correlations in sequencing count data generally, the sharpest mechanical result in the literature."
  why: The whole mechanism rests on Connor, Barberán and Clauset 2017, one soil 16S matrix with no truth set, and carries no SINGLE SOURCE label. · instead: zero-ties.1 · trail: C-RANKNET §What sequencing count, §Single-source claims · from: C-RANKNET:B-0119, C-RANKNET:C-021
- **dns.14** "The microbiome field has never adopted reciprocal-rank neighbourhoods."
  why: It rests on the reviewer's own search plus one multi-omics paper (Kudjordjie et al. 2022), and one illustrative paper does not establish a field-wide practice. · instead: microbial-rank-devices.3 · trail: C-RANKNET §The rank device in microbial, §Single-source claims · from: C-RANKNET:B-0077, C-RANKNET:C-026
- **dns.15** "It is an established fact of the field that no DREAM-style challenge exists for microbial network inference."
  why: The statement rests on Faust 2021 alone and is asserted in a review, labelled SECONDARY once and then used in the Part B verdict as an established field fact. · instead: known-truth.2 · trail: C-RANKNET §Single-source claims · from: C-RANKNET:C-027
- **dns.16** "eLSA is the one widely used microbiome association method that requires ordered samples."
  why: It rests on the eLSA paper itself, no source is cited for the exclusivity claim, and time-series microbiome methods such as MetaMIS, LIMITS, TIME and Granger-style inference are not considered. · instead: elsa.1 · trail: C-RANKNET §The rank device in microbial, §Glossary, §Single-source claims · from: C-RANKNET:B-0084, C-RANKNET:B-0193, C-RANKNET:C-028
- **dns.17** "On microbial abundance data, rank-based methods perform no better or worse than magnitude-based ones."
  why: The critic's Part B narrows this to plain rank correlation, and adds that one rank-based copula estimator beats both Pearson-based and compositional neighbourhood selection in its authors' simulations. · instead: verdict-b.1, verdict-b.2 · trail: C-RANKNET §Verdict as delivered, §Verdicts, §critic · from: C-RANKNET:A-002, C-RANKNET:A-010, C-RANKNET:C-009

## Gaps
- **gap.1** Rank-based interaction networks in proteomics (co-fractionation and co-elution interactome inference: PrInCE, EPIC and the CORUM-benchmarked scoring functions, which use rank correlations and reciprocal-best-partner scoring and are benchmarked against curated complexes) are absent; a follow-up should search that community's own terms.
  blocks: rank-device · origin: critic coverage gap (brief bullet: the rank-based methods that exist, by field) · search: not stated · from: C-RANKNET:C-048..051 · trail: C-RANKNET §Coverage gaps
- **gap.2** Single-cell transcriptomics is absent: Skinnider, Squair and Foster 2019, the only benchmark that puts rank correlations (Spearman, Kendall, zero-inflated Kendall, weighted rank) against compositionally aware proportionality on zero-rich data (GO by neighbour voting across 43 datasets), was not obtained, so Part A rests entirely on bulk expression; a search agent reported that proportionality beat rank correlation and that rank correlations gave among the least reproducible networks, but that access could not be reproduced and the result carries no weight. The same field's rank-neighbourhood graphs (kNN, shared nearest neighbour, mutual nearest neighbours) and rank-based gene networks (bigSCale, scLink) are also absent.
  blocks: verdict-a · origin: critic coverage gap; source not obtained; routes not yet tried: UBC cIRcle, the dismay software repository and its preprint, ResearchGate author copy, the Nature Methods reader-share link · search: not stated · src: skinniderEvaluatingMeasuresAssociation2019 · from: C-RANKNET:C-052..055, C-RANKNET:B-0174, C-RANKNET:R-0157..0160 · trail: C-RANKNET §Coverage gaps, §Sources not obtained
- **gap.3** Relative expression ordering (REO) methods in transcriptomics (top scoring pairs and k-TSP, DIRAC, RankComp and RankCompV3, singscore), which build gene-pair relation networks from within-sample orderings, are motivated by normalisation and batch invariance, and have published benchmarks against known class labels, are missing; the note's stage-2 routing check fired on this family as a candidate for a follow-up brief on its benchmarks alone, to be confirmed first.
  blocks: rank-device · origin: critic coverage gap; the note's stage 2 check (FIRED, a keyword prefilter, not a judgement) · search: not stated · from: C-RANKNET:C-056..058, C-RANKNET:B-0010..0014 · trail: C-RANKNET §Coverage gaps, §Stage 2 check
- **gap.4** The ATTED-II and COXPRESdb database papers after 2009 (COXPRESdb releases in Nucleic Acids Research, 2019 and 2022, and the ATTED-II 2022 release) report AUC comparisons of MR-based against other coexpression measures; they were not searched, so the SINGLE SOURCE status of the MR accuracy result may be an artefact of the search.
  blocks: expression-benchmarks.2 · origin: critic coverage gap · search: not searched (critic: C-061) · from: C-RANKNET:C-059..062 · trail: C-RANKNET §Coverage gaps
- **gap.5** Tie handling in rank statistics other than Spearman (Kendall tau-b and tau-c tie corrections, the zero-inflated Kendall estimator used in single-cell work, and SPRING's truncation threshold as a competing tie treatment) has not been compared head to head; the zero-inflated Kendall work (Pimentel et al. 2015; Denuit and Mesfioui 2017) is known only second-hand.
  blocks: zero-ties · origin: critic coverage gap; sources not obtained · search: not stated · src: pimentel2015, denuitBoundsKendallS2017 · from: C-RANKNET:C-063..065, C-RANKNET:R-0230..0232 · trail: C-RANKNET §Coverage gaps, §Sources not obtained (all
- **gap.6** Module detection on microbial correlation networks beyond MNetClass (SCNIC, manta, CoNet ensemble module workflows) is absent, as is any benchmark that varies the construction (rank versus magnitude versus compositional) while holding the clustering fixed.
  blocks: microbial-modules · origin: critic coverage gap; the review's not-found result on modules from rank-built against magnitude-built microbiome networks · search: searched, not found (note: "No benchmark comparing modules recovered from rank-built against magnitude-built microbiome networks") · from: C-RANKNET:C-066..068, C-RANKNET:B-0231 · trail: C-RANKNET §Coverage gaps, §Search record
- **gap.7** Microbiome time-series association methods beyond eLSA (MetaMIS, TIME, LIMITS, Granger-causality and convergent cross mapping applied to 16S series) are not covered, and no benchmark number is given for eLSA or LSA beyond one precision value quoted second-hand.
  blocks: elsa, ordered-samples · origin: critic coverage gap · search: not stated · from: C-RANKNET:C-069..071 · trail: C-RANKNET §Coverage gaps
- **gap.8** Sequencing depth as an isolated factor in rank-versus-magnitude performance: the review names no search routes for its not-found statement; the obvious targets are Weiss et al.'s rarefying, CSS and DESeq comparison (per-tool numbers in the unobtained supplement) and the rarefaction methodology literature.
  blocks: sequencing-depth · origin: critic coverage gap · search: not stated (critic: C-072) · from: C-RANKNET:C-072..074 · trail: C-RANKNET §Coverage gaps
- **gap.9** Community ecology's own co-occurrence network literature (null-model and checkerboard approaches, rank-based dissimilarity and association measures on plant and animal abundance matrices) was not searched, so community ecology is answered only for trajectories, not for network construction.
  blocks: rank-trajectories · origin: critic coverage gap · search: not searched (critic: C-076) · from: C-RANKNET:C-075..077 · trail: C-RANKNET §Coverage gaps
- **gap.10** Metabolomics and multi-omics networks: mutual rank is used in plant metabolite-gene and metabolomics network construction, but no metabolomics application or benchmark is reported.
  blocks: mutual-rank · origin: critic coverage gap · search: not stated · from: C-RANKNET:C-078..080 · trail: C-RANKNET §Coverage gaps
- **gap.11** No benchmark compares a reciprocal-rank construction against a compositionally aware method on the same data; the nearest published comparison of rank against compositional measures is in single-cell transcriptomics and was not obtained.
  blocks: verdict-b · origin: the review's not-found result · search: searched, not found (note: "Routes as above, plus searches on compositional microbiome network inference benchmarks") · src: skinniderEvaluatingMeasuresAssociation2019 · from: C-RANKNET:B-0173, C-RANKNET:B-0174, C-RANKNET:B-0227 · trail: C-RANKNET §Gaps, with the routes
- **gap.12** No benchmark tests MR or HRR under sequencing count properties specifically (compositional closure, zero-driven ties or uneven depth); the HRR literature's RNA-seq normalisation work tests TPM, VST and sample scaling but never closure or ties.
  blocks: mutual-rank, hrr · origin: the review's not-found result · search: searched, not found (note: "Routes: the searches above plus the RNA-seq normalisation work in the HRR literature") · src: lieseckeRankingGenomewideCorrelation2018, lieseckeImprovedGeneCoexpression2019 · from: C-RANKNET:B-0175, C-RANKNET:B-0176, C-RANKNET:B-0228 · trail: C-RANKNET §Gaps, with the routes
- **gap.13** The Mutwil et al. 2010 numbers that carry the coverage half of Part A (edge and node counts, shared edges, the MYB33/MYB65 example, the 351 arrays, the HCCA adjusted Rand index) were not verified by the critic from any route.
  blocks: hrr.2, hrr.3, hrr.5, verdict-a.3 · origin: critic full-text breach · search: not stated · src: mutwilAssemblyInteractiveCorrelation2010 · from: C-RANKNET:A-039, C-RANKNET:C-012..014 · trail: C-RANKNET §Verdict assessment, §Full-text breaches
- **gap.14** Whether Weiss et al.'s LSA precision of 0.2 is in the main text or comes from the supplementary files the review could not obtain is unsettled; the per-tool precision, sensitivity and F1 numbers for Spearman, MIC and LSA against SparCC and CoNet are in that unobtained supplement, of which only the main text's qualitative statements were used.
  blocks: sparsity.3 · origin: critic full-text breach; source not obtained · search: not stated · src: weissCorrelationDetectionStrategies2016 · from: C-RANKNET:A-040, C-RANKNET:C-015..018, C-RANKNET:R-0161..0164 · trail: C-RANKNET §Full-text breaches, §Sources not obtained
- **gap.15** Kishore et al. 2023 figures S5 and S6 hold the only published per-method precision and sensitivity values for SPRING on a common simulated benchmark, and Ghaeli et al. 2026's supplementary tables and figures hold its per-algorithm F-score and Jaccard values; neither was obtained.
  blocks: spring.11, spring.12 · origin: sources not obtained · search: not stated · src: kishoreInferringMicrobialCooccurrence2023, ghaeliEvaluatingMicrobialNetwork2026 · from: C-RANKNET:R-0165..0170 · trail: C-RANKNET §Sources not obtained
- **gap.16** Obayashi and Kinoshita's 2013 partial ROC study, which would be the sharpest direct partial-AUC benchmark of MR against PCC rank and raw PCC, was not obtained (only an abstract record located).
  blocks: expression-benchmarks.2 · origin: source not obtained · search: not stated · src: obayashiPartialROCReveals2013 · from: C-RANKNET:R-0171..0174 · trail: C-RANKNET §Sources not obtained
- **gap.17** Two works on rank reordering in community dynamics were not obtained: Avolio et al. 2015, cited repeatedly as the origin of the rank-abundance-curve change framework, and Jones, Ripplinger and Collins 2017, the most-cited empirical claim that reordering rather than richness change drives long-term community dynamics.
  blocks: rank-trajectories · origin: sources not obtained · search: not stated · src: avolioFrameworkQuantifyingMagnitude2015, jonesSpeciesReorderingNot2017 · from: C-RANKNET:R-0175..0184 · trail: C-RANKNET §Sources not obtained
- **gap.18** Gupta and Pereira 2019, reported by a search agent to list PCC, mutual information, mutual rank and HRR side by side as interchangeable similarity measures with no comparative evaluation, was not opened or used.
  blocks: expression-benchmarks · origin: source not obtained · search: not stated · src: guptaRecentAdvancesGene2019 · from: C-RANKNET:R-0185..0189 · trail: C-RANKNET §Sources not obtained

## Out of scope
- C-RANKNET:C-010: a link to the critique section (navigation, not a finding)
- C-RANKNET:C-011: how the critique was produced (provenance, kept in the result note)
- C-RANKNET:C-029..036: reference corrections (Yao et al. title; Avolio et al. 2015 authors and pages), applied in Sources
- C-RANKNET:A-022..025: the critic's check of the reference apparatus and the quotes (verification, kept in the result note; its two reference exceptions applied in Sources)

## Sources
```bibtex
@article{obayashiRankCorrelationCoefficient2009,
  author = {Obayashi, Takeshi and Kinoshita, Kengo},
  title = {Rank of correlation coefficient as a comparable measure for biological significance of gene coexpression},
  journal = {DNA Research},
  volume = {16},
  number = {5},
  pages = {249--260},
  year = {2009},
  doi = {10.1093/dnares/dsp016},
  note = {access: full_text (C-RANKNET; Europe PMC XML, PMC2762411); cited as: C-RANKNET [1]}
}
@article{obayashiATTEDII2018Plant2018,
  author = {Obayashi, Takeshi and Aoki, Yuichi and Tadaka, Shu and Kagaya, Yuki and Kinoshita, Kengo},
  title = {ATTED-II in 2018: a plant coexpression database based on investigation of the statistical property of the mutual rank index},
  journal = {Plant and Cell Physiology},
  volume = {59},
  number = {1},
  pages = {e3},
  year = {2018},
  doi = {10.1093/pcp/pcx191},
  note = {access: full_text (C-RANKNET; PMC5914358); published online 4 December 2017; cited as: C-RANKNET [2]}
}
@article{mutwilAssemblyInteractiveCorrelation2010,
  author = {Mutwil, Marek and Usadel, Björn and Schütte, Moritz and Loraine, Ann and Ebenhöh, Oliver and Persson, Staffan},
  title = {Assembly of an interactive correlation network for the Arabidopsis genome using a novel heuristic clustering algorithm},
  journal = {Plant Physiology},
  volume = {152},
  number = {1},
  pages = {29--43},
  year = {2010},
  doi = {10.1104/pp.109.145318},
  note = {access: full_text (C-RANKNET; read through the summarising WebFetch tool, PMC2799344; the critic could not verify its numbers from any route); Crossref issued date 2009 (online) against a 2010 issue; cited as: C-RANKNET [3]}
}
@article{lieseckeRankingGenomewideCorrelation2018,
  author = {Liesecke, Franziska and Daudu, Dimitri and Dugé de Bernonville, Rodolphe and Besseau, Sébastien and Clastre, Marc and Courdavault, Vincent and de Craene, Johan-Owen and Crèche, Joël and Giglioli-Guivarc'h, Nathalie and Glévarec, Gaëlle and Pichon, Olivier and Dugé de Bernonville, Thomas},
  title = {Ranking genome-wide correlation measurements improves microarray and RNA-seq based global and targeted co-expression networks},
  journal = {Scientific Reports},
  volume = {8},
  number = {1},
  pages = {10885},
  year = {2018},
  doi = {10.1038/s41598-018-29077-3},
  note = {access: full_text (C-RANKNET; nature.com HTML); cited as: C-RANKNET [4]}
}
@article{lieseckeImprovedGeneCoexpression2019,
  author = {Liesecke, Franziska and De Craene, Johan-Owen and Besseau, Sébastien and Courdavault, Vincent and Clastre, Marc and Vergès, Valentin and Papon, Nicolas and Giglioli-Guivarc'h, Nathalie and Glévarec, Gaëlle and Pichon, Olivier and Dugé de Bernonville, Thomas},
  title = {Improved gene co-expression network quality through expression dataset down-sampling and network aggregation},
  journal = {Scientific Reports},
  volume = {9},
  number = {1},
  pages = {14431},
  year = {2019},
  doi = {10.1038/s41598-019-50885-8},
  note = {access: full_text (C-RANKNET; PMC6783424); cited as: C-RANKNET [5]}
}
@article{wisecaverGlobalCoexpressionNetwork2017,
  author = {Wisecaver, Jennifer H. and Borowsky, Alexander T. and Tzin, Vered and Jander, Georg and Kliebenstein, Daniel J. and Rokas, Antonis},
  title = {A global coexpression network approach for connecting genes to specialized metabolic pathways in plants},
  journal = {The Plant Cell},
  volume = {29},
  number = {5},
  pages = {944--959},
  year = {2017},
  doi = {10.1105/tpc.17.00009},
  note = {access: full_text (C-RANKNET; read through the summarising WebFetch tool, PMC5466033); cited as: C-RANKNET [6]}
}
@article{kumariEvaluationGeneAssociation2012,
  author = {Kumari, Sapna and Nie, Jeff and Chen, Huann-Sheng and Ma, Hao and Stewart, Ron and Li, Xiang and Lu, Meng-Zhu and Taylor, William M. and Wei, Hairong},
  title = {Evaluation of gene association methods for coexpression network construction and biological knowledge discovery},
  journal = {PLoS ONE},
  volume = {7},
  number = {11},
  pages = {e50411},
  year = {2012},
  doi = {10.1371/journal.pone.0050411},
  note = {access: full_text (C-RANKNET; PLOS HTML; a supplementary table not read); cited as: C-RANKNET [7]}
}
@article{vandenbonEvaluationCriticalData2022,
  author = {Vandenbon, Alexis},
  title = {Evaluation of critical data processing steps for reliable prediction of gene co-expression from large collections of RNA-seq data},
  journal = {PLOS ONE},
  volume = {17},
  number = {1},
  pages = {e0263344},
  year = {2022},
  doi = {10.1371/journal.pone.0263344},
  note = {access: full_text (C-RANKNET; PLOS HTML); cited as: C-RANKNET [8]}
}
@article{songComparisonCoexpressionMeasures2012,
  author = {Song, Lin and Langfelder, Peter and Horvath, Steve},
  title = {Comparison of co-expression measures: mutual information, correlation, and model based indices},
  journal = {BMC Bioinformatics},
  volume = {13},
  number = {1},
  pages = {328},
  year = {2012},
  doi = {10.1186/1471-2105-13-328},
  note = {access: full_text (C-RANKNET; the synthesiser's read, PMC3586947); conflict: the coexpression search agent lists it as not obtained (PARTIAL: per-measure numbers for Spearman against Pearson and bicor could not be extracted); cited as: C-RANKNET [9]}
}
@article{ballouzGuidanceRNAseqCoexpression2015,
  author = {Ballouz, Sara and Verleyen, Wim and Gillis, Jesse},
  title = {Guidance for RNA-seq co-expression network construction and analysis: safety in numbers},
  journal = {Bioinformatics},
  volume = {31},
  number = {13},
  pages = {2123--2130},
  year = {2015},
  doi = {10.1093/bioinformatics/btv118},
  note = {access: full_text (C-RANKNET; read through the summarising WebFetch tool, academic.oup.com article page); Crossref stores initials only, given names as published; cited as: C-RANKNET [10]}
}
@article{poretskyMutRankRShiny2020,
  author = {Poretsky, Elly and Huffaker, Alisa},
  title = {MutRank: an R shiny web-application for exploratory targeted mutual rank-based coexpression analyses integrated with user-provided supporting information},
  journal = {PeerJ},
  volume = {8},
  pages = {e10264},
  year = {2020},
  doi = {10.7717/peerj.10264},
  note = {access: full_text (C-RANKNET; PMC7659623); cited as: C-RANKNET [11]}
}
@article{yoonMicrobialNetworksSPRING2019,
  author = {Yoon, Grace and Gaynanova, Irina and Müller, Christian L.},
  title = {Microbial networks in SPRING: semi-parametric rank-based correlation and partial correlation estimation for quantitative microbiome data},
  journal = {Frontiers in Genetics},
  volume = {10},
  pages = {516},
  year = {2019},
  doi = {10.3389/fgene.2019.00516},
  note = {access: full_text (C-RANKNET; Frontiers HTML, including Tables 2 and 3); cited as: C-RANKNET [12]}
}
@article{weissCorrelationDetectionStrategies2016,
  author = {Weiss, Sophie and Van Treuren, Will and Lozupone, Catherine and Faust, Karoline and Friedman, Jonathan and Deng, Ye and Xia, Li Charlie and Xu, Zhenjiang Zech and Ursell, Luke and Alm, Eric J. and Birmingham, Amanda and Cram, Jacob A. and Fuhrman, Jed A. and Raes, Jeroen and Sun, Fengzhu and Zhou, Jizhong and Knight, Rob},
  title = {Correlation detection strategies in microbial data sets vary widely in sensitivity and precision},
  journal = {The ISME Journal},
  volume = {10},
  number = {7},
  pages = {1669--1681},
  year = {2016},
  doi = {10.1038/ismej.2015.235},
  note = {access: full_text (C-RANKNET; read as the author accepted manuscript, eScholarship qt3ps0c507; main text only); its supplementary note, supplementary figures 1-17 and supplementary tables 1-3 (and Table 1/Figure 7 recommendation summary): not_obtained; cited as: C-RANKNET [13]}
}
@article{hiranoDifficultyInferringMicrobial2019,
  author = {Hirano, Hokuto and Takemoto, Kazuhiro},
  title = {Difficulty in inferring microbial community structure based on co-occurrence network approaches},
  journal = {BMC Bioinformatics},
  volume = {20},
  number = {1},
  pages = {329},
  year = {2019},
  doi = {10.1186/s12859-019-2915-1},
  note = {access: full_text (C-RANKNET; PMC6567618); cited as: C-RANKNET [14]}
}
@article{friedmanInferringCorrelationNetworks2012,
  author = {Friedman, Jonathan and Alm, Eric J.},
  title = {Inferring correlation networks from genomic survey data},
  journal = {PLoS Computational Biology},
  volume = {8},
  number = {9},
  pages = {e1002687},
  year = {2012},
  doi = {10.1371/journal.pcbi.1002687},
  note = {access: full_text (C-RANKNET; PMC3447976); cited as: C-RANKNET [15]}
}
@article{berryDecipheringMicrobialInteractions2014,
  author = {Berry, David and Widder, Stefanie},
  title = {Deciphering microbial interactions and detecting keystone species with co-occurrence networks},
  journal = {Frontiers in Microbiology},
  volume = {5},
  pages = {219},
  year = {2014},
  doi = {10.3389/fmicb.2014.00219},
  note = {access: full_text (C-RANKNET; PMC4033041); no article number in Crossref; cited as: C-RANKNET [16]}
}
@article{connorUsingNullModels2017,
  author = {Connor, Nora and Barberán, Albert and Clauset, Aaron},
  title = {Using null models to infer microbial co-occurrence networks},
  journal = {PLOS ONE},
  volume = {12},
  number = {5},
  pages = {e0176751},
  year = {2017},
  doi = {10.1371/journal.pone.0176751},
  note = {access: full_text (C-RANKNET; PLOS HTML); cited as: C-RANKNET [17]}
}
@article{kishoreInferringMicrobialCooccurrence2023,
  author = {Kishore, Dileep and Birzu, Gabriel and Hu, Zhenjun and DeLisi, Charles and Korolev, Kirill S. and Segrè, Daniel},
  title = {Inferring microbial co-occurrence networks from amplicon data: a systematic evaluation},
  journal = {mSystems},
  volume = {8},
  number = {4},
  pages = {e00961-22},
  year = {2023},
  doi = {10.1128/msystems.00961-22},
  note = {access: full_text (C-RANKNET; main text and figure legends, PMC10469762); figures S5 and S6 (per-method precision and sensitivity, including SPRING): not_obtained; cited as: C-RANKNET [18]}
}
@article{ghaeliEvaluatingMicrobialNetwork2026,
  author = {Ghaeli, Zahra and Aghdam, Rosa and Eslahchi, Changiz},
  title = {Evaluating microbial network inference methods: moving beyond synthetic data with reproducibility-driven benchmarks},
  journal = {BMC Bioinformatics},
  volume = {27},
  number = {1},
  pages = {215},
  year = {2026},
  doi = {10.1186/s12859-026-06510-3},
  note = {access: full_text (C-RANKNET; main text only, PMC13555938); supplementary tables S7-S38 and figures S25-S65: not_obtained; cited as: C-RANKNET [19]}
}
@article{faustOpenChallengesMicrobial2021,
  author = {Faust, Karoline},
  title = {Open challenges for microbial network construction and analysis},
  journal = {The ISME Journal},
  volume = {15},
  number = {11},
  pages = {3111--3118},
  year = {2021},
  doi = {10.1038/s41396-021-01027-4},
  note = {access: full_text (C-RANKNET; PMC8528840); cited as: C-RANKNET [20]}
}
@article{peschelNetCoMiNetworkConstruction2021,
  author = {Peschel, Stefanie and Müller, Christian L. and von Mutius, Erika and Boulesteix, Anne-Laure and Depner, Martin},
  title = {NetCoMi: network construction and comparison for microbiome data in R},
  journal = {Briefings in Bioinformatics},
  volume = {22},
  number = {4},
  pages = {bbaa290},
  year = {2021},
  doi = {10.1093/bib/bbaa290},
  note = {access: full_text (C-RANKNET; PMC8293835); published online 2020 (Crossref issued date 2020 against a 2021 issue); cited as: C-RANKNET [21]}
}
@article{xiaExtendedLocalSimilarity2011,
  author = {Xia, Li C. and Steele, Joshua A. and Cram, Jacob A. and Cardon, Zoe G. and Simmons, Sheri L. and Vallino, Joseph J. and Fuhrman, Jed A. and Sun, Fengzhu},
  title = {Extended local similarity analysis (eLSA) of microbial community and other time series data with replicates},
  journal = {BMC Systems Biology},
  volume = {5},
  number = {Suppl 2},
  pages = {S15},
  year = {2011},
  doi = {10.1186/1752-0509-5-S2-S15},
  note = {access: full_text (C-RANKNET; PMC3287481); cited as: C-RANKNET [22]}
}
@article{kudjordjieFusariumOxysporumDisrupts2022,
  author = {Kudjordjie, Enoch Narh and Hooshmand, Kourosh and Sapkota, Rumakanta and Darbani, Behrooz and Fomsgaard, Inge S. and Nicolaisen, Mogens},
  title = {Fusarium oxysporum disrupts microbiome-metabolome networks in Arabidopsis thaliana roots},
  journal = {Microbiology Spectrum},
  volume = {10},
  number = {4},
  pages = {e01226-22},
  year = {2022},
  doi = {10.1128/spectrum.01226-22},
  note = {access: full_text (C-RANKNET; PMC9430778); author list arrived garbled from the search blocks and was taken from Crossref by the synthesiser; a search agent's list says the Crossref author-name pass was not run on it; cited as: C-RANKNET [23]}
}
@article{wangMNetClassControlfreeMicrobial2025,
  author = {Wang, Yihua and Hou, Qingzhen and Wei, Fulan and Liu, Bingqiang and Feng, Qiang},
  title = {MNetClass: a control-free microbial network clustering framework for identifying central subcommunities across ecological niches},
  journal = {mSystems},
  volume = {10},
  number = {12},
  pages = {e00989-25},
  year = {2025},
  doi = {10.1128/msystems.00989-25},
  note = {access: full_text (C-RANKNET; PMC12710344); cited as: C-RANKNET [24]}
}
@article{battyRankClocks2006,
  author = {Batty, Michael},
  title = {Rank clocks},
  journal = {Nature},
  volume = {444},
  number = {7119},
  pages = {592--596},
  year = {2006},
  doi = {10.1038/nature05302},
  note = {access: full_text (C-RANKNET; read in full text by a search agent, not re-opened by the synthesiser; dagger); cited as: C-RANKNET [25]}
}
@article{collinsRankClocksPlant2008,
  author = {Collins, Scott L. and Suding, Katharine N. and Cleland, Elsa E. and Batty, Michael and Pennings, Steven C. and Gross, Katherine L. and Grace, James B. and Gough, Laura and Fargione, Joe E. and Clark, Christopher M.},
  title = {Rank clocks and plant community dynamics},
  journal = {Ecology},
  volume = {89},
  number = {12},
  pages = {3534--3541},
  year = {2008},
  doi = {10.1890/07-1646.1},
  note = {access: full_text (C-RANKNET; read in full text by a search agent, not re-opened by the synthesiser; dagger); conflict: two search agents list it as not obtained (no open full text found; known only through Hallett et al. 2016 and Liu et al. 2025), one giving the second author as Scott C. Pennings; cited as: C-RANKNET [26]}
}
@article{avolioComprehensiveApproachAnalyzing2019,
  author = {Avolio, Meghan L. and Carroll, Ian T. and Collins, Scott L. and Houseman, Gregory R. and Hallett, Lauren M. and Isbell, Forest and Koerner, Sally E. and Komatsu, Kimberly J. and Smith, Melinda D. and Wilcox, Kevin R.},
  title = {A comprehensive approach to analyzing community dynamics using rank abundance curves},
  journal = {Ecosphere},
  volume = {10},
  number = {10},
  pages = {e02881},
  year = {2019},
  doi = {10.1002/ecs2.2881},
  note = {access: full_text (C-RANKNET; read in full text by a search agent, not re-opened by the synthesiser; dagger); conflict: the coexpression search agent lists it as not obtained (Crossref metadata verified but no full text read); cited as: C-RANKNET [27]}
}
@article{hallettCodynRPackage2016,
  author = {Hallett, Lauren M. and Jones, Sydney K. and MacDonald, A. Andrew M. and Jones, Matthew B. and Flynn, Dan F. B. and Ripplinger, Julie and Slaughter, Peter and Gries, Corinna and Collins, Scott L.},
  title = {codyn: an R package of community dynamics metrics},
  journal = {Methods in Ecology and Evolution},
  volume = {7},
  number = {10},
  pages = {1146--1151},
  year = {2016},
  doi = {10.1111/2041-210X.12569},
  note = {access: full_text (C-RANKNET; read in full text by a search agent, not re-opened by the synthesiser; dagger); conflict: the microbiome search agent lists the paper as not obtained and took the metric definitions from the CRAN codyn reference manual and package source instead; cited as: C-RANKNET [28]}
}
@article{duranpinedoLongtermDynamicsHuman2021,
  author = {Duran-Pinedo, Ana and Solbiati, Jose and Teles, Flavia and Teles, Ricardo and Zang, Yanping and Frias-Lopez, Jorge},
  title = {Long-term dynamics of the human oral microbiome during clinical disease progression},
  journal = {BMC Biology},
  volume = {19},
  number = {1},
  pages = {240},
  year = {2021},
  doi = {10.1186/s12915-021-01169-z},
  note = {access: full_text (C-RANKNET; PMC8572441); cited as: C-RANKNET [29]}
}
@article{liuMicrobesClimateRefugia2025,
  author = {Liu, Huaiqiang and Zhong, Zhenghua and Xu, Juan and Qu, Liping and Liu, Haijun and Zheng, Fengfeng and Zhang, Chuanlun and Xie, Wei},
  title = {Microbes under climate refugia: equable subcommunity rank dynamics in large-river deltaic estuaries},
  journal = {Ecology and Evolution},
  volume = {15},
  number = {8},
  pages = {e72014},
  year = {2025},
  doi = {10.1002/ece3.72014},
  note = {access: full_text (C-RANKNET; PMC12356829); cited as: C-RANKNET [30]}
}
@article{hallAnankeTemporalClustering2017,
  author = {Hall, Michael W. and Rohwer, Robin R. and Perrie, Jonathan and McMahon, Katherine D. and Beiko, Robert G.},
  title = {Ananke: temporal clustering reveals ecological dynamics of microbial communities},
  journal = {PeerJ},
  volume = {5},
  pages = {e3812},
  year = {2017},
  doi = {10.7717/peerj.3812},
  note = {access: full_text (C-RANKNET; PMC5621509); cited as: C-RANKNET [31]}
}
@article{buckleyMeasuringChangeBiological2021,
  author = {Buckley, Hannah L. and Day, Nicola J. and Case, Bradley S. and Lear, Gavin},
  title = {Measuring change in biological communities: multivariate analysis approaches for temporal datasets with low sample size},
  journal = {PeerJ},
  volume = {9},
  pages = {e11096},
  year = {2021},
  doi = {10.7717/peerj.11096},
  note = {access: full_text (C-RANKNET; PMC8038644); cited as: C-RANKNET [32]}
}
@article{ghoshTemporalTurnoverSpecies2024,
  author = {Ghosh, Shyamolina and Matthews, Blake},
  title = {Temporal turnover in species' ranks can explain variation in Taylor's slope for ecological timeseries},
  journal = {Ecology},
  volume = {105},
  number = {9},
  pages = {e4381},
  year = {2024},
  doi = {10.1002/ecy.4381},
  note = {access: full_text (C-RANKNET; read in full text by a search agent, not re-opened by the synthesiser; dagger); not cited: listed in the references, cited nowhere in the review; cited as: C-RANKNET [33]}
}
@article{larsenDistinctTemporallyStable2023,
  author = {Larsen, Stefano and Albanese, Davide and Stegen, James and Franceschi, Pietro and Coller, Emanuela and Zanzotti, Roberto and Ioriatti, Claudio and Stefani, Erika and Pindo, Massimo and Cestaro, Alessandro and Donati, Claudio},
  title = {Distinct and temporally stable assembly mechanisms shape bacterial and fungal communities in vineyard soils},
  journal = {Microbial Ecology},
  volume = {86},
  number = {1},
  pages = {337--349},
  year = {2023},
  doi = {10.1007/s00248-022-02065-x},
  note = {access: full_text (C-RANKNET; read in full text by a search agent, not re-opened by the synthesiser; dagger); cited as: C-RANKNET [34]}
}
@article{yaoPhagesbacteriaInteractionsUnderlying2025,
  author = {Yao, Jian and Zeng, Yan and Hong, Xia and Wang, Meng and Zhang, Quan and Chen, Yating and Gou, Min and Xia, Zi-Yuan and Tang, Yue-Qin},
  title = {Phages-bacteria interactions underlying the dynamics of polyhydroxyalkanoate-producing mixed microbial cultures via meta-omics study},
  journal = {mSystems},
  volume = {10},
  number = {4},
  pages = {e00200-25},
  year = {2025},
  doi = {10.1128/msystems.00200-25},
  note = {access: full_text (C-RANKNET; read in full text by a search agent, not re-opened by the synthesiser; dagger); title corrected (critic: C-RANKNET:C-029..031; the note said 'via metagenomics and metatranscriptomics'); cited as: C-RANKNET [35]}
}
@article{doddsAllotaxonometryRankturbulenceDivergence2023,
  author = {Dodds, Peter Sheridan and Minot, Joshua R. and Arnold, Michael V. and Alshaabi, Thayer and Adams, Jane Lydia and Dewhurst, David Rushing and Gray, Tyler J. and Frank, Morgan R. and Reagan, Andrew J. and Danforth, Christopher M.},
  title = {Allotaxonometry and rank-turbulence divergence: a universal instrument for comparing complex systems},
  journal = {EPJ Data Science},
  volume = {12},
  number = {1},
  pages = {37},
  year = {2023},
  doi = {10.1140/epjds/s13688-023-00400-x},
  note = {access: full_text (C-RANKNET; read in full text by a search agent, not re-opened by the synthesiser; dagger); cited as: C-RANKNET [36]}
}
@article{iniguezDynamicsRanking2022,
  author = {Iñiguez, Gerardo and Pineda, Carlos and Gershenson, Carlos and Barabási, Albert-László},
  title = {Dynamics of ranking},
  journal = {Nature Communications},
  volume = {13},
  number = {1},
  pages = {1646},
  year = {2022},
  doi = {10.1038/s41467-022-29256-x},
  note = {access: full_text (C-RANKNET; read in full text by a search agent, not re-opened by the synthesiser; dagger); cited as: C-RANKNET [37]}
}
@article{barwellMeasuringBetadiversitySpecies2015,
  author = {Barwell, Louise J. and Isaac, Nick J. B. and Kunin, William E.},
  title = {Measuring beta-diversity with species abundance data},
  journal = {Journal of Animal Ecology},
  volume = {84},
  number = {4},
  pages = {1112--1122},
  year = {2015},
  doi = {10.1111/1365-2656.12362},
  note = {access: full_text (C-RANKNET; read in full text by a search agent, not re-opened by the synthesiser; dagger); cited as: C-RANKNET [38]}
}
@article{skinniderEvaluatingMeasuresAssociation2019,
  author = {Skinnider, Michael A. and Squair, Jordan W. and Foster, Leonard J.},
  title = {Evaluating measures of association for single-cell transcriptomics},
  journal = {Nature Methods},
  volume = {16},
  number = {5},
  pages = {381--386},
  year = {2019},
  doi = {10.1038/s41592-019-0372-4},
  note = {access: not_obtained (C-RANKNET; a search agent reported reading it in full from an author-hosted PDF; the synthesiser could not reproduce that access and gives the result no weight); listed in Sources not obtained}
}
@inproceedings{obayashiPartialROCReveals2013,
  author = {Obayashi, Takeshi and Kinoshita, Kengo},
  title = {Partial ROC reveals superiority of mutual rank of Pearson's correlation coefficient as a coexpression measure to elucidate functional association of genes},
  booktitle = {Conference proceedings (Quantitative Biology)},
  year = {2013},
  note = {access: not_obtained (C-RANKNET; only an ADS abstract record located, ui.adsabs.harvard.edu/abs/2013qbi..conf..229O); incomplete: doi, pages; listed in Sources not obtained}
}
@article{avolioFrameworkQuantifyingMagnitude2015,
  author = {Avolio, Meghan L. and La Pierre, Kimberly J. and Houseman, Gregory R. and Koerner, Sally E. and Grman, Emily and Isbell, Forest and Johnson, David Samuel and Wilcox, Kevin R.},
  title = {A framework for quantifying the magnitude and variability of community responses to global change drivers},
  journal = {Ecosphere},
  volume = {6},
  number = {12},
  pages = {1--14},
  year = {2015},
  doi = {10.1890/ES15-00317.1},
  note = {access: not_obtained (C-RANKNET); author list and pages corrected (critic: C-RANKNET:C-032..036; the note said 'Meghan L. Avolio, Kevin R. Wilcox, Kimberly J. Komatsu, Sally E. Koerner, Melinda D. Smith and colleagues' and article 280); listed in Sources not obtained}
}
@article{jonesSpeciesReorderingNot2017,
  author = {Jones, Sydney K. and Ripplinger, Julie and Collins, Scott L.},
  title = {Species reordering, not changes in richness, drives long-term dynamics in grassland communities},
  journal = {Ecology Letters},
  volume = {20},
  number = {12},
  pages = {1556--1565},
  year = {2017},
  doi = {10.1111/ele.12864},
  note = {access: not_obtained (C-RANKNET); listed in Sources not obtained}
}
@article{guptaRecentAdvancesGene2019,
  author = {Gupta, Chirag and Pereira, Andy},
  title = {Recent advances in gene function prediction using context-specific coexpression networks in plants},
  journal = {F1000Research},
  volume = {8},
  pages = {153},
  year = {2019},
  doi = {10.12688/f1000research.17207.1},
  note = {access: not_obtained (C-RANKNET; a search agent reported reading it; the synthesiser did not open it and has not used it); listed in Sources not obtained}
}
@article{pimentel2015,
  author = {Pimentel, Kenneth and Nelsen, Roger B. and others},
  year = {2015},
  note = {access: not_obtained (C-RANKNET; on Kendall's tau for zero-inflated continuous data; known only through Perrone, van den Heuvel and Zhan, arXiv:2208.03155); incomplete: title, journal, volume, pages, doi; listed in Sources not obtained}
}
@article{denuitBoundsKendallS2017,
  author = {Denuit, Michel and Mesfioui, Mhamed},
  title = {Bounds on Kendall's tau for zero-inflated continuous variables},
  journal = {Statistics \& Probability Letters},
  year = {2017},
  note = {access: not_obtained (C-RANKNET; known only through Perrone, van den Heuvel and Zhan, arXiv:2208.03155); incomplete: volume, pages, doi; listed in Sources not obtained}
}
@article{yoonSparseSemiparametricCanonical2020,
  author = {Yoon, Grace and Carroll, Raymond J. and Gaynanova, Irina},
  title = {Sparse semiparametric canonical correlation analysis for data of mixed types},
  journal = {Biometrika},
  year = {2020},
  note = {access: not_obtained (C-RANKNET; cited in SPRING as Yoon et al. 2018); incomplete: volume, pages, doi; listed in Sources not obtained}
}
@article{fan2017,
  author = {Fan, Jianqing and others},
  year = {2017},
  note = {access: not_obtained (C-RANKNET; on latent Gaussian copula graphical models); incomplete: title, journal, volume, pages, doi; listed in Sources not obtained}
}
@misc{huangLatentcor,
  author = {Huang, Mingze and Müller, Christian L. and Gaynanova, Irina},
  title = {latentcor},
  howpublished = {arXiv:2108.09180},
  note = {access: not_obtained (C-RANKNET); incomplete: full title, year; listed in Sources not obtained}
}
@misc{anonStatisticalComputationMethods,
  title = {Statistical computation methods for microbiome compositional data network inference},
  howpublished = {arXiv:2109.01993},
  note = {access: not_obtained (C-RANKNET; surfaced in web searches, not fetched); incomplete: author, year; listed in Sources not obtained}
}
@misc{anonCMiNetConsensusMicrobiome,
  title = {CMiNet consensus microbiome network},
  howpublished = {bioRxiv 2025.05.09.653200},
  note = {access: not_obtained (C-RANKNET; surfaced in web searches, not fetched); incomplete: author, full title, year; listed in Sources not obtained}
}
@article{anonMetaanalysisMicrobiomeAssociation2022,
  title = {Meta-analysis of microbiome association networks reveal patterns of dysbiosis},
  journal = {Scientific Reports},
  year = {2022},
  doi = {10.1038/s41598-022-22541-1},
  note = {access: not_obtained (C-RANKNET; surfaced in web searches, not fetched); incomplete: author, volume, pages; listed in Sources not obtained}
}
@article{anonMetaNet2026,
  title = {MetaNet},
  journal = {Bioinformatics},
  year = {2026},
  doi = {10.1093/bioinformatics/btag321},
  note = {access: full_text (C-RANKNET; a search agent read it via Europe PMC fullTextXML); dropped by the synthesiser because its author list was unconfirmed; not cited; incomplete: author, full title, volume, pages; listed in Sources not obtained}
}
@article{cochoRankDiversityLanguages2015,
  author = {Cocho, Germinal and Flores, Jorge and Gershenson, Carlos and Pineda, Carlos and Sanchez, Sergio},
  title = {Rank diversity of languages: generic behavior in computational linguistics},
  journal = {PLOS ONE},
  volume = {10},
  number = {4},
  pages = {e0121898},
  year = {2015},
  doi = {10.1371/journal.pone.0121898},
  note = {access: not_obtained (C-RANKNET; identified and verified in Crossref but not read); listed in Sources not obtained}
}
@misc{wohlgemuth2016,
  author = {Wohlgemuth and others},
  year = {2016},
  note = {access: not_obtained (C-RANKNET; known only through Ghosh and Matthews 2024, as showing a role for species reordering rather than evenness in maintaining ecosystem functioning); incomplete: author given names, title, journal, volume, pages, doi; listed in Sources not obtained}
}
@manual{hallettCodynRPackage2025,
  author = {Hallett, Lauren M. and others},
  title = {codyn R package reference manual and source (add_ranks, RAC_change, rank_shift)},
  organization = {CRAN},
  year = {2025},
  url = {https://cran.r-project.org/package=codyn},
  note = {access: full_text (C-RANKNET; read in full by a search agent, not fetched by the synthesiser); listed in Sources not obtained (all agents)}
}
@article{gloorMicrobiomeDatasetsCompositional2017,
  author = {Gloor, Gregory B. and Macklaim, Jean M. and Pawlowsky-Glahn, Vera and Egozcue, Juan J.},
  title = {Microbiome Datasets Are Compositional: And This Is Not Optional},
  journal = {Frontiers in Microbiology},
  volume = {8},
  pages = {2224},
  year = {2017},
  doi = {10.3389/fmicb.2017.02224},
  note = {background (compositional-closure); access: full_text (checked on the publisher page)}
}
```
