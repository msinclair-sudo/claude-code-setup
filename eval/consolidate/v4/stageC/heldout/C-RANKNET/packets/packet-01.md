## known-truth.1 (claim)

Ghaeli, Aghdam and Eslahchi open by stating the field's core obstacle: "the lack of experimentally validated gold standards presents a significant obstacle in evaluating the biological accuracy of inferred networks".

- conf: not stated
- class: not stated
- holds: microbial network inference
- src: ghaeliEvaluatingMicrobialNetwork2026
- trail: C-RANKNET §The rank device in microbial

From the note:

> C-RANKNET:B-0100 [The rank device in microbial abundance data] That paper opens by stating the field's core obstacle: "the lack of experimentally validated gold standards presents a significant obstacle in evaluating the biological accuracy of inferred networks" [19].
>

## known-truth.2 (claim)

Faust's review states that no DREAM-style challenge exists for microbial network inference, and that "interactions observed previously in nature cannot be used to determine the accuracy of network inference tools but only their sensitivity", which is why a truth-based comparison on real data is unavailable.

- conf: single (critic: C-027)
- class: assert (critic: C-027)
- holds: microbial network inference; the critic: rests on Faust 2021 alone, asserted in a review
- src: faustOpenChallengesMicrobial2021
- trail: C-RANKNET §The rank device in microbial, §Single-source claims

From the note:

> C-RANKNET:B-0112 [The rank device in microbial abundance data] The same review explains why a truth-based comparison on real data is unavailable: no DREAM-style challenge exists for microbial network inference, and "interactions observed previously in nature cannot be used to determine the accuracy of network inference tools but only their sensitivity" [20].
>
> C-RANKNET:C-027 [Single-source claims (6)] - 'No DREAM-style challenge exists for microbial network inference' rests on Faust 2021 alone and is asserted in a review, correctly labelled SECONDARY once but then used in the Part B verdict as an established field fact.
>

## rank-device.1 (claim)

Two research communities have independently reached for ranks when building networks of features measured across many samples, and they reached for different ranks: gene co-expression uses the rank of a correlation coefficient inside a gene's own neighbour list, producing reciprocal-rank constructions such as mutual rank and highest reciprocal rank; microbial ecology uses the rank of the measurement itself, feeding Spearman's rho or Kendall's tau into an edge weight or into a copula estimator.

- conf: not stated
- class: not stated
- holds: gene co-expression and microbial ecology network construction
- src: obayashiRankCorrelationCoefficient2009, mutwilAssemblyInteractiveCorrelation2010, yoonMicrobialNetworksSPRING2019, weissCorrelationDetectionStrategies2016
- trail: C-RANKNET §The review as returned

From the note:

> C-RANKNET:B-0015 [The review as returned] Two research communities have independently reached for ranks when building networks of features measured across many samples, and they reached for different ranks.
>
> C-RANKNET:B-0016 [The review as returned] Gene co-expression uses the rank of a correlation coefficient inside a gene's own neighbour list, producing reciprocal-rank constructions such as mutual rank and highest reciprocal rank [1,3].
>
> C-RANKNET:B-0017 [The review as returned] Microbial ecology uses the rank of the measurement itself, feeding Spearman's rho or Kendall's tau into an edge weight or into a copula estimator [12,13].
>

## rank-device.2 (claim)

A third community, community ecology, tracks the rank of a taxon's abundance through time; the three vocabularies barely overlap in the literature, and only the first two (gene co-expression and microbial ecology) have been benchmarked against known truth.

- conf: not stated
- class: not stated
- holds: gene co-expression, microbial ecology and community ecology literatures
- src: battyRankClocks2006 (†: read in full text by a search agent and not re-opened by the reviewer), collinsRankClocksPlant2008 (†), avolioComprehensiveApproachAnalyzing2019 (†)
- trail: C-RANKNET §The review as returned

From the note:

> C-RANKNET:B-0015 [The review as returned] Two research communities have independently reached for ranks when building networks of features measured across many samples, and they reached for different ranks.
>
> C-RANKNET:B-0018 [The review as returned] A third community, community ecology, tracks the rank of a taxon's abundance through time [25†,26†,27†].
>
> C-RANKNET:B-0019 [The review as returned] The three vocabularies barely overlap in the literature, and only the first two have been benchmarked against known truth.
>
> C-RANKNET:B-0020 [The review as returned] A note on notation: references marked † in the list were read in full text by a search agent and not re-opened by me.
>

Not found in the cited text (where to look, not what is wrong): holds: co-expression

## rank-statistics.1 (claim)

Spearman's rank correlation (rho) is Pearson correlation computed on the ranks; it is the microbiome field's default correlation-based co-occurrence measure, usually thresholded at absolute rho 0.6 to 0.8.

- conf: not stated
- class: not stated
- holds: the review's glossary; used in every field
- src: none (the review's glossary)
- trail: C-RANKNET §Glossary

From the note:

> C-RANKNET:B-0185 [Glossary: what each field calls the rank device] **Spearman's rank correlation (rho)**: every field: Pearson correlation computed on the ranks; the microbiome field's default correlation-based co-occurrence measure, usually thresholded at absolute rho 0.6 to 0.8.
>

Not found in the cited text (where to look, not what is wrong): holds: review; holds: in

## rank-statistics.2 (claim)

Kendall's tau is the concordant minus discordant pair fraction; it is the base statistic for copula-based latent correlation estimators and one member of CoNet-style ensembles.

- conf: not stated
- class: not stated
- holds: the review's glossary
- src: none (the review's glossary)
- trail: C-RANKNET §Glossary

From the note:

> C-RANKNET:B-0186 [Glossary: what each field calls the rank device] **Kendall's tau**: concordant minus discordant pair fraction; base statistic for copula-based latent correlation estimators and one member of CoNet-style ensembles.
>

Not found in the cited text (where to look, not what is wrong): holds: review

## rank-statistics.3 (claim)

Weighted rank correlation is a Spearman-type coefficient weighting agreement among the top ranks more heavily; Hoeffding's D is a rank statistic testing general, not only monotonic, dependence.

- conf: not stated
- class: not stated
- holds: the review's glossary
- src: none (the review's glossary)
- trail: C-RANKNET §Glossary

From the note:

> C-RANKNET:B-0187 [Glossary: what each field calls the rank device] **Weighted rank correlation**: Spearman-type coefficient weighting agreement among the top ranks more heavily.
>
> C-RANKNET:B-0188 [Glossary: what each field calls the rank device] **Hoeffding's D**: rank statistic testing general, not only monotonic, dependence.
>

Not found in the cited text (where to look, not what is wrong): holds: review

## rank-statistics.4 (claim)

Theil-Sen and rank Theil-Sen are median-of-pairwise-slopes regression on raw values and on ranks respectively; the raw version is not a rank method.

- conf: not stated
- class: not stated
- holds: the review's glossary
- src: none (the review's glossary)
- trail: C-RANKNET §Glossary

From the note:

> C-RANKNET:B-0189 [Glossary: what each field calls the rank device] **Theil-Sen and rank Theil-Sen**: median-of-pairwise-slopes regression on raw values and on ranks respectively; the raw version is not a rank method.
>

Not found in the cited text (where to look, not what is wrong): holds: review

## rank-statistics.5 (claim)

The comparators in this literature that are not rank-based are Pearson; biweight midcorrelation; mutual information and MIC; proportionality (rho_p, phi_s); SparCC and FastSpar; CCLasso; REBACCA; gCoda; OIPCQ; SPIEC-EASI in glasso and MB modes; FlashWeave; COZINE; HARMONIES; mLDM; and WGCNA with topological overlap.

- conf: not stated
- class: not stated
- holds: the review's glossary
- src: none (the review's glossary)
- trail: C-RANKNET §Glossary

From the note:

> C-RANKNET:B-0200 [Glossary: what each field calls the rank device] **Comparators that are not rank-based**: Pearson; biweight midcorrelation; mutual information and MIC; proportionality (rho_p, phi_s); SparCC and FastSpar; CCLasso; REBACCA; gCoda; OIPCQ; SPIEC-EASI in glasso and MB modes; FlashWeave; COZINE; HARMONIES; mLDM; WGCNA with topological overlap.
>

Not found in the cited text (where to look, not what is wrong): holds: review

## mutual-rank.1 (claim)

The original argument for ranking is that a Pearson correlation coefficient is not comparable across gene pairs, datasets or preprocessing pipelines: Obayashi and Kinoshita showed that the PCC distribution shifts with sample selection and with the GeneChip summarisation method, so that functionally related genes accumulate at high ranks but at widely different coefficient values.

- conf: not stated
- class: meas (note: "measured; four microarray compendia")
- holds: four microarray compendia, Arabidopsis 1,388 chips, human 5,188, mouse 2,226, rat 632; unordered cross-sectional samples
- src: obayashiRankCorrelationCoefficient2009
- trail: C-RANKNET §The rank device in gene

From the note:

> C-RANKNET:B-0023 [The rank device in gene co-expression] The original argument for ranking is that a Pearson correlation coefficient is not comparable across gene pairs, datasets or preprocessing pipelines.
>
> C-RANKNET:B-0024 [The rank device in gene co-expression] Obayashi and Kinoshita showed that the PCC distribution shifts with sample selection and with the GeneChip summarisation method, so that functionally related genes accumulate at high ranks but at widely different coefficient values [1] (measured; four microarray compendia, Arabidopsis 1,388 chips, human 5,188, mouse 2,226, rat 632; unordered cross-sectional samples).
>

## mutual-rank.2 (claim)

Obayashi and Kinoshita defined mutual rank as the geometric mean of the two reciprocal Pearson-correlation ranks, sqrt(rank A to B times rank B to A), low being strong, and justified the geometric rather than arithmetic mean on the argument that rank differences act logarithmically: "the impact of the difference of 1 and 3 in PCC rank can be similar with that of 100 and 300". It is used in gene co-expression (ATTED-II, COXPRESdb, plant and animal transcriptomics).

- conf: not stated
- class: not stated
- holds: gene co-expression
- src: obayashiRankCorrelationCoefficient2009
- trail: C-RANKNET §The rank device in gene, §Glossary

From the note:

> C-RANKNET:B-0025 [The rank device in gene co-expression] They defined mutual rank as the geometric mean of the two reciprocal ranks, and justified the geometric rather than arithmetic mean on the argument that rank differences act logarithmically: "the impact of the difference of 1 and 3 in PCC rank can be similar with that of 100 and 300" [1].
>
> C-RANKNET:B-0179 [Glossary: what each field calls the rank device] **Mutual rank (MR)**: gene co-expression (ATTED-II, COXPRESdb, plant and animal transcriptomics): geometric mean of the two reciprocal Pearson-correlation ranks, sqrt(rank A to B times rank B to A); low is strong.
>

## mutual-rank.3 (claim)

Mutual rank is not statistically calibrated by construction: it ranges from 1 to N minus 1, so values are not comparable across platforms with different gene counts, and it is precise near the ends of its range but "easily affected by chance" in the middle, where the error distribution is not normal.

- conf: not stated
- class: meas (note: "measured; ATTED-II v9")
- holds: ATTED-II v9, 16 platforms, nine plant species, microarray and RNA-seq, 100 bootstrap resamples per platform
- src: obayashiATTEDII2018Plant2018
- trail: C-RANKNET §The rank device in gene

From the note:

> C-RANKNET:B-0026 [The rank device in gene co-expression] Mutual rank is not statistically calibrated by construction.
>
> C-RANKNET:B-0027 [The rank device in gene co-expression] It ranges from 1 to N minus 1, so values are not comparable across platforms with different gene counts, and it is precise near the ends of its range but "easily affected by chance" in the middle, where the error distribution is not normal [2] (measured; ATTED-II v9, 16 platforms, nine plant species, microarray and RNA-seq, 100 bootstrap resamples per platform).
>

## mutual-rank.4 (claim)

The ATTED-II group's fix (logit-MR) is to divide MR by gene number and apply a logit transform, which gives normally distributed error with roughly constant variance and therefore confidence intervals.

- conf: not stated
- class: not stated
- holds: ATTED-II
- src: obayashiATTEDII2018Plant2018
- trail: C-RANKNET §The rank device in gene, §Glossary

From the note:

> C-RANKNET:B-0028 [The rank device in gene co-expression] The ATTED-II group's fix is to divide by gene number and apply a logit transform, which gives normally distributed error with roughly constant variance and therefore confidence intervals [2].
>
> C-RANKNET:B-0180 [Glossary: what each field calls the rank device] **Logit-MR**: ATTED-II: MR divided by gene number then logit-transformed, giving approximately constant-variance error and therefore confidence intervals.
>

## mutual-rank.5 (claim)

The logit-MR fix is a repair to a known defect of the rank index, not evidence that the index wins.

- conf: not stated
- class: not stated
- holds: ATTED-II's logit-MR
- src: obayashiATTEDII2018Plant2018
- trail: C-RANKNET §The rank device in gene

From the note:

> C-RANKNET:B-0028 [The rank device in gene co-expression] The ATTED-II group's fix is to divide by gene number and apply a logit transform, which gives normally distributed error with roughly constant variance and therefore confidence intervals [2].
>
> C-RANKNET:B-0029 [The rank device in gene co-expression] This is a repair to a known defect of the rank index, not evidence that the index wins.
>

Not found in the cited text (where to look, not what is wrong): holds: logit-mr

## mutual-rank.6 (claim)

MutRank computes MR for a reference gene's top 200 coexpressed genes (maximum 1,000) rather than all pairs, because "calculating all pair-wise MR values on the resources available on most personal computers is impractical", and needs no temporal ordering.

- conf: not stated
- class: not stated
- holds: the MutRank R shiny web-application
- src: poretskyMutRankRShiny2020
- trail: C-RANKNET §Data requirements

From the note:

> C-RANKNET:B-0139 [Data requirements: ordered samples or not] MutRank computes MR for a reference gene's top 200 coexpressed genes (maximum 1,000) rather than all pairs, because "calculating all pair-wise MR values on the resources available on most personal computers is impractical" [11], and needs no temporal ordering either.
>
> C-RANKNET:R-0042 [References] MutRank: an R shiny web-application for exploratory targeted mutual rank-based coexpression analyses integrated with user-provided supporting information.
>

## hrr.1 (claim)

Highest reciprocal rank is the other rank rule in gene co-expression: an edge survives only if both genes appear in each other's top N list (usually N equal to 30), so HRR is operationally the larger of the two reciprocal ranks; PCC-HRR and SCC-HRR are HRR applied to Pearson or to Spearman coefficients.

- conf: not stated
- class: not stated
- holds: plant co-expression (AraGenNet, PlaNet, CoNekT)
- src: mutwilAssemblyInteractiveCorrelation2010, lieseckeRankingGenomewideCorrelation2018, lieseckeImprovedGeneCoexpression2019
- trail: C-RANKNET §The rank device in gene, §Glossary

From the note:

> C-RANKNET:B-0030 [The rank device in gene co-expression] Highest reciprocal rank is the other rule in this field: an edge survives only if both genes appear in each other's top N list, so HRR is operationally the larger of the two reciprocal ranks [3,4,5].
>
> C-RANKNET:B-0181 [Glossary: what each field calls the rank device] **Highest reciprocal rank (HRR)**: plant co-expression (AraGenNet, PlaNet, CoNekT): the larger of the two reciprocal ranks; an edge exists only if both genes are in each other's top N list, usually N equal to 30.
>
> C-RANKNET:B-0182 [Glossary: what each field calls the rank device] **PCC-HRR / SCC-HRR**: HRR applied to Pearson or to Spearman coefficients respectively.
>

## hrr.2 (claim)

Mutwil and colleagues capped HRR at 30 and weighted edges by band, producing an Arabidopsis network of 103,587 edges over 20,785 nodes against 231,882 edges over only 7,178 nodes for a PCC r at or above 0.8 network on the same data, with 29,956 edges and 6,942 nodes shared.

- conf: not stated
- class: meas (note: "measured; 351 RMA-normalised ATH1 arrays")
- holds: 351 RMA-normalised ATH1 arrays, Arabidopsis; the critic could not verify these numbers from any route
- src: mutwilAssemblyInteractiveCorrelation2010
- trail: C-RANKNET §The rank device in gene, §Full-text breaches
- limit: access (critic: C-012)

From the note:

> C-RANKNET:B-0031 [The rank device in gene co-expression] Mutwil and colleagues capped HRR at 30 and weighted edges by band, producing an Arabidopsis network of 103,587 edges over 20,785 nodes against 231,882 edges over only 7,178 nodes for a PCC r at or above 0.8 network on the same data, with 29,956 edges and 6,942 nodes shared [3] (measured; 351 RMA-normalised ATH1 arrays).
>
> C-RANKNET:C-012 [Full-text breaches (4)] - Mutwil et al. 2010 (ref 3): none of the quoted numbers could be verified from any route available to me.
>
> C-RANKNET:C-013 [Full-text breaches (4)] Europe PMC fullTextXML returns a 150-byte stub for PMC2799344, NCBI efetch returns 'The publisher of this article does not allow downloading of the full text in XML form', pmc.ncbi.nlm.nih.gov is behind a Cloudflare interstitial and academic.oup.com returns HTTP 403.
>
> C-RANKNET:C-014 [Full-text breaches (4)] The 103,587/20,785 versus 231,882/7,178 edge and node counts, the 29,956 shared edges, the MYB33/MYB65 r = 0.7 example, the 351 arrays and the HCCA adjusted Rand index 0.3818 all carry weight in the Part A 'coverage wins' half of the verdict and are unverified here.
>
> C-RANKNET:C-012 [Full-text breaches (4)] - Mutwil et al. 2010 (ref 3): none of the quoted numbers could be verified from any route available to me.
>

## hrr.3 (claim)

Mutwil and colleagues' stated motivation for HRR is coverage, not accuracy: an r cutoff leaves genes with narrow correlation distributions unconnected, illustrated by the redundant transcription factors MYB33 and MYB65, which correlate at r equal to 0.7 and so miss an r equal to 0.8 cutoff but sit second in each other's lists.

- conf: not stated
- class: not stated
- holds: Mutwil et al.'s Arabidopsis HRR network; the MYB33/MYB65 example is unverified by the critic
- src: mutwilAssemblyInteractiveCorrelation2010
- trail: C-RANKNET §The rank device in gene, §Full-text breaches
- limit: access (critic: C-012)

From the note:

> C-RANKNET:B-0031 [The rank device in gene co-expression] Mutwil and colleagues capped HRR at 30 and weighted edges by band, producing an Arabidopsis network of 103,587 edges over 20,785 nodes against 231,882 edges over only 7,178 nodes for a PCC r at or above 0.8 network on the same data, with 29,956 edges and 6,942 nodes shared [3] (measured; 351 RMA-normalised ATH1 arrays).
>
> C-RANKNET:B-0032 [The rank device in gene co-expression] Their stated motivation is coverage, not accuracy: an r cutoff leaves genes with narrow correlation distributions unconnected, illustrated by the redundant transcription factors MYB33 and MYB65, which correlate at r equal to 0.7 and so miss an r equal to 0.8 cutoff but sit second in each other's lists [3].
>
> C-RANKNET:C-012 [Full-text breaches (4)] - Mutwil et al. 2010 (ref 3): none of the quoted numbers could be verified from any route available to me.
>
> C-RANKNET:C-014 [Full-text breaches (4)] The 103,587/20,785 versus 231,882/7,178 edge and node counts, the 29,956 shared edges, the MYB33/MYB65 r = 0.7 example, the 351 arrays and the HCCA adjusted Rand index 0.3818 all carry weight in the Part A 'coverage wins' half of the verdict and are unverified here.
>

## hrr.4 (claim)

Mutwil and colleagues justify ranking by citing Obayashi and Kinoshita rather than by running their own rank-versus-magnitude accuracy comparison.

- conf: not stated
- class: not stated
- holds: Mutwil et al. 2010
- src: mutwilAssemblyInteractiveCorrelation2010
- trail: C-RANKNET §The rank device in gene

From the note:

> C-RANKNET:B-0033 [The rank device in gene co-expression] They justify ranking by citing Obayashi and Kinoshita rather than by running their own rank-versus-magnitude accuracy comparison [3].
>

Not found in the cited text (where to look, not what is wrong): holds: mutwil; holds: 2010

## hrr.5 (claim)

Module detection built for rank networks exists and has been compared, but only against other clustering algorithms on a fixed rank network: the Heuristic Cluster Chiseling Algorithm grows a node vicinity network around a seed and removes nodes better connected outside it, and on the Arabidopsis HRR-30 network it gave the best modularity against MCL, k-means and MCODE, a Davies-Bouldin index comparable to MCL and MCODE, and robustness of adjusted Rand index 0.3818 (4 percent standard deviation) when 20 percent of genes were dropped.

- conf: not stated
- class: not stated
- holds: the Arabidopsis HRR-30 network; the critic could not verify the adjusted Rand index 0.3818
- src: mutwilAssemblyInteractiveCorrelation2010
- trail: C-RANKNET §Head to head, §Glossary, §Full-text breaches
- limit: access (critic: C-012)

From the note:

> C-RANKNET:B-0074 [Head to head: ranked against unranked in expression data] Module detection built specifically for rank networks exists and has been compared, but only against other clustering algorithms on a fixed rank network.
>
> C-RANKNET:B-0075 [Head to head: ranked against unranked in expression data] The Heuristic Cluster Chiseling Algorithm grows a node vicinity network around a seed and removes nodes better connected outside it; on the Arabidopsis HRR-30 network it gave the best modularity against MCL, k-means and MCODE, a Davies-Bouldin index comparable to MCL and MCODE, and robustness of adjusted Rand index 0.3818 (4 percent standard deviation) when 20 percent of genes were dropped [3].
>
> C-RANKNET:B-0184 [Glossary: what each field calls the rank device] **Node vicinity network (NVN) and the Heuristic Cluster Chiseling Algorithm (HCCA)**: plant co-expression: a co-expression neighbourhood within n steps of a seed, and the module detector that grows one then removes nodes better connected outside it.
>
> C-RANKNET:C-012 [Full-text breaches (4)] - Mutwil et al. 2010 (ref 3): none of the quoted numbers could be verified from any route available to me.
>
> C-RANKNET:C-014 [Full-text breaches (4)] The 103,587/20,785 versus 231,882/7,178 edge and node counts, the 29,956 shared edges, the MYB33/MYB65 r = 0.7 example, the 351 arrays and the HCCA adjusted Rand index 0.3818 all carry weight in the Part A 'coverage wins' half of the verdict and are unverified here.
>

## hrr.6 (claim)

The HCCA comparison makes no comparison of rank-built against magnitude-built networks.

- conf: not stated
- class: not stated
- holds: the HCCA benchmark on the Arabidopsis HRR-30 network
- src: mutwilAssemblyInteractiveCorrelation2010
- trail: C-RANKNET §Head to head

From the note:

> C-RANKNET:B-0075 [Head to head: ranked against unranked in expression data] The Heuristic Cluster Chiseling Algorithm grows a node vicinity network around a seed and removes nodes better connected outside it; on the Arabidopsis HRR-30 network it gave the best modularity against MCL, k-means and MCODE, a Davies-Bouldin index comparable to MCL and MCODE, and robustness of adjusted Rand index 0.3818 (4 percent standard deviation) when 20 percent of genes were dropped [3].
>
> C-RANKNET:B-0076 [Head to head: ranked against unranked in expression data] No comparison of rank-built against magnitude-built networks is made there.
>

Not found in the cited text (where to look, not what is wrong): HCCA; holds: hcca

## rank-aggregation.1 (claim)

A third use of ranks in gene co-expression is as an aggregation device rather than an association measure: Ballouz, Verleyen and Gillis replace each within-experiment correlation with its rank in that network before averaging networks across experiments (a rank-standardised network), so that "changes in the distribution of actual correlations (induced by sample size dependencies) have no impact on our results".

- conf: not stated
- class: meas (note: "measured; 50 human RNA-seq experiments")
- holds: 50 human RNA-seq experiments, 1,970 samples, plus 30 microarray experiments; guilt-by-association AUROC against GO; Gillis lab, EGAD
- src: ballouzGuidanceRNAseqCoexpression2015
- trail: C-RANKNET §The rank device in gene, §Glossary

From the note:

> C-RANKNET:B-0034 [The rank device in gene co-expression] A third use of ranks in this field is as an aggregation device rather than an association measure.
>
> C-RANKNET:B-0035 [The rank device in gene co-expression] Ballouz, Verleyen and Gillis replace each within-experiment correlation with its rank in that network before averaging networks across experiments, so that "changes in the distribution of actual correlations (induced by sample size dependencies) have no impact on our results" [10] (measured; 50 human RNA-seq experiments, 1,970 samples, plus 30 microarray experiments; guilt-by-association AUROC against GO).
>
> C-RANKNET:B-0183 [Glossary: what each field calls the rank device] **Rank-standardised network**: Gillis lab, EGAD: every within-experiment correlation replaced by its rank inside that network before networks are averaged across experiments.
>

## rank-aggregation.2 (claim)

In Ballouz and colleagues' work, aggregating lifted average AUROC from about 0.585 for individual networks to about 0.7, matching the microarray aggregate.

- conf: not stated
- class: not stated
- holds: human RNA-seq co-expression networks; guilt-by-association AUROC against GO
- src: ballouzGuidanceRNAseqCoexpression2015
- trail: C-RANKNET §The rank device in gene

From the note:

> C-RANKNET:B-0035 [The rank device in gene co-expression] Ballouz, Verleyen and Gillis replace each within-experiment correlation with its rank in that network before averaging networks across experiments, so that "changes in the distribution of actual correlations (induced by sample size dependencies) have no impact on our results" [10] (measured; 50 human RNA-seq experiments, 1,970 samples, plus 30 microarray experiments; guilt-by-association AUROC against GO).
>
> C-RANKNET:B-0036 [The rank device in gene co-expression] Aggregating lifted average AUROC from about 0.585 for individual networks to about 0.7, matching the microarray aggregate [10].
>

Not found in the cited text (where to look, not what is wrong): holds: co-expression

## rank-aggregation.3 (claim)

The measured gain in Ballouz and colleagues' work is attributable to aggregation; the paper reports no ranked-against-unranked head-to-head.

- conf: not stated
- class: not stated
- holds: Ballouz, Verleyen and Gillis 2015
- src: ballouzGuidanceRNAseqCoexpression2015
- trail: C-RANKNET §The rank device in gene

From the note:

> C-RANKNET:B-0037 [The rank device in gene co-expression] The measured gain there is attributable to aggregation; the paper reports no ranked-against-unranked head-to-head.
>

Not found in the cited text (where to look, not what is wrong): holds: ballouz; holds: verleyen; holds: gillis; holds: 2015

## rank-aggregation.4 (claim)

When HRR values were used as the edge weight during aggregation of many small networks, co-occurrence aggregation (keeping edges that recur across networks) was significantly more predictive on GO AUROC: +0.02 against -0.016, Student's t test, p < 2e-16.

- conf: not stated
- class: meas (note: "measured; Arabidopsis microarray and RNA-seq compendia")
- holds: Arabidopsis microarray and RNA-seq compendia, six aggregation methods, HRR as the base weight throughout; the p value is the critic's reading of the source
- src: lieseckeImprovedGeneCoexpression2019
- trail: C-RANKNET §Head to head, §Reference errors

From the note:

> C-RANKNET:B-0067 [Head to head: ranked against unranked in expression data] **Ranking as an aggregation weight loses to counting.** When HRR values were used as the edge weight during aggregation of many small networks, co-occurrence aggregation (keeping edges that recur across networks) was significantly more predictive on GO AUROC, p below 0.001 [5] (measured; Arabidopsis microarray and RNA-seq compendia, six aggregation methods, HRR as the base weight throughout).
>
> C-RANKNET:C-046 [Reference errors (7)] - Ref 5 (Liesecke et al. 2019): the co-occurrence versus HRR aggregation difference is reported in the source as +0.02 versus -0.016 GO AUROC, Student's t test, p < 2e-16. The review gives 'p below 0.001', which is the figure's asterisk threshold, not the reported p value.
>

## rank-aggregation.5 (claim)

The aggregation result bounds the use of the rank value as a carried quantity, not the rank construction itself.

- conf: not stated
- class: not stated
- holds: HRR as an aggregation weight
- src: lieseckeImprovedGeneCoexpression2019
- trail: C-RANKNET §Head to head

From the note:

> C-RANKNET:B-0067 [Head to head: ranked against unranked in expression data] **Ranking as an aggregation weight loses to counting.** When HRR values were used as the edge weight during aggregation of many small networks, co-occurrence aggregation (keeping edges that recur across networks) was significantly more predictive on GO AUROC, p below 0.001 [5] (measured; Arabidopsis microarray and RNA-seq compendia, six aggregation methods, HRR as the base weight throughout).
>
> C-RANKNET:B-0068 [Head to head: ranked against unranked in expression data] This bounds the use of the rank value as a carried quantity, not the construction itself.
>

## expression-benchmarks.1 (claim)

Five studies in gene expression put the ranked-against-unranked comparison directly, and they do not agree, because they do not score the same thing.

- conf: not stated
- class: not stated
- holds: bulk gene expression
- src: none (the reviewer's synthesis)
- trail: C-RANKNET §Head to head

From the note:

> C-RANKNET:B-0038 [Head to head: ranked against unranked in expression data] Five studies put the comparison directly, and they do not agree, because they do not score the same thing.
>

## expression-benchmarks.2 (claim)

Across four species and all three GO branches, PCC rank and mutual rank predicted a gene's GO annotation from its neighbours better than raw PCC, for all four summarisation methods, with MR and PCC rank statistically indistinguishable from each other; the authors conclude that "the relatively higher performance of PCC rank is a general feature". This rank-of-coefficient result is the one study that tested it directly.

- conf: single (critic: C-006)
- class: meas (critic: C-002)
- holds: microarray compendia of four species, GO prediction from neighbours; SINGLE SOURCE for mutual rank specifically
- src: obayashiRankCorrelationCoefficient2009
- trail: C-RANKNET §Head to head, §critic

From the note:

> C-RANKNET:B-0024 [The rank device in gene co-expression] Obayashi and Kinoshita showed that the PCC distribution shifts with sample selection and with the GeneChip summarisation method, so that functionally related genes accumulate at high ranks but at widely different coefficient values [1] (measured; four microarray compendia, Arabidopsis 1,388 chips, human 5,188, mouse 2,226, rat 632; unordered cross-sectional samples).
>
> C-RANKNET:B-0039 [Head to head: ranked against unranked in expression data] **Ranking wins on function prediction in the original benchmark.** Across four species and all three GO branches, PCC rank and mutual rank predicted a gene's GO annotation from its neighbours better than raw PCC, for all four summarisation methods, with MR and PCC rank statistically indistinguishable from each other [1].
>
> C-RANKNET:B-0040 [Head to head: ranked against unranked in expression data] The authors conclude that "the relatively higher performance of PCC rank is a general feature" [1].
>
> C-RANKNET:B-0041 [Head to head: ranked against unranked in expression data] This result is SINGLE SOURCE for mutual rank specifically, and the absolute AUC values are only shown in figures whose axes deliberately do not start at 0.5, so the size of the gain cannot be extracted from the text.
>
> C-RANKNET:C-002 [danger: Critic: verdict partly supported] Part A (any data type): measured, and the answer splits by which rank device and which criterion, not by "rank versus magnitude" as a single question.
>
> C-RANKNET:C-003 [danger: Critic: verdict partly supported] Rank of the *coefficient* (PCC rank, mutual rank) beat raw PCC on GO prediction across four species in the one study that tested it directly (Obayashi and Kinoshita 2009, which also reports Spearman value ≈ Pearson value in the same paper, Supplementary Fig. S3).
>
> C-RANKNET:C-006 [danger: Critic: verdict partly supported] So: measured; no general accuracy advantage for rank-of-value, one unreplicated accuracy advantage for rank-of-coefficient, and reproducible-in-one-study structural advantages.
>
> C-RANKNET:A-042 [Verdict the body actually supports] Rank of the *coefficient* (PCC rank, mutual rank) beat raw PCC on GO prediction across four species in the one study that tested it directly (Obayashi and Kinoshita 2009, which also reports Spearman value ≈ Pearson value in the same paper, Supplementary Fig. S3).
>
> C-RANKNET:A-045 [Verdict the body actually supports] So: measured; no general accuracy advantage for rank-of-value, one unreplicated accuracy advantage for rank-of-coefficient, and reproducible-in-one-study structural advantages.
>

## expression-benchmarks.3 (claim)

In Obayashi and Kinoshita's benchmark the absolute AUC values are only shown in figures whose axes deliberately do not start at 0.5, so the size of the gain cannot be extracted from the text.

- conf: not stated
- class: not stated
- holds: Obayashi and Kinoshita 2009
- src: obayashiRankCorrelationCoefficient2009
- trail: C-RANKNET §Head to head

From the note:

> C-RANKNET:B-0041 [Head to head: ranked against unranked in expression data] This result is SINGLE SOURCE for mutual rank specifically, and the absolute AUC values are only shown in figures whose axes deliberately do not start at 0.5, so the size of the gain cannot be extracted from the text.
>

Not found in the cited text (where to look, not what is wrong): holds: obayashi; holds: kinoshita; holds: 2009

## expression-benchmarks.4 (claim)

Obayashi and Kinoshita 2009 also reports Spearman value approximately equal to Pearson value in the same paper (Supplementary Fig. S3), while PCC rank does not behave like Pearson value: the cleanest internal evidence that rank of the coefficient and rank of the value behave differently. The review read this full text and did not report it.

- conf: not stated
- class: not stated
- holds: Obayashi and Kinoshita 2009
- src: obayashiRankCorrelationCoefficient2009
- trail: C-RANKNET §critic, §Verdict assessment, §Scope drift

From the note:

> C-RANKNET:C-003 [danger: Critic: verdict partly supported] Rank of the *coefficient* (PCC rank, mutual rank) beat raw PCC on GO prediction across four species in the one study that tested it directly (Obayashi and Kinoshita 2009, which also reports Spearman value ≈ Pearson value in the same paper, Supplementary Fig. S3).
>
> C-RANKNET:A-042 [Verdict the body actually supports] Rank of the *coefficient* (PCC rank, mutual rank) beat raw PCC on GO prediction across four species in the one study that tested it directly (Obayashi and Kinoshita 2009, which also reports Spearman value ≈ Pearson value in the same paper, Supplementary Fig. S3).
>
> C-RANKNET:A-038 [Verdict assessment] Obayashi's own SCC-value-versus-PCC-value null, which is the cleanest internal evidence that the two devices behave differently, is in the full text the review read and is not reported.
>
> C-RANKNET:C-084 [Scope drift (7)] - The Part A verdict pools rank-of-coefficient constructions (mutual rank, HRR) with rank-of-value measures (Spearman, Kendall) into one direction tally, although the review's own opening paragraph identifies them as different devices used by different communities, and Obayashi's full text (read by the reviewer) contains the internal control showing Spearman value behaves like Pearson value while PCC rank does not. This is the rule 5 problem applied to directions rather than numbers.
>

## expression-benchmarks.5 (claim)

Liesecke and colleagues built global and pathway-level networks from 9,953 ATH1 microarrays and 1,676 RNA-seq samples under seven normalisations, with six measures including PCC, SCC, PCC-HRR, SCC-HRR, mutual information and partial correlation, scored against GO and against five curated pathways with known sub-pathway structure.

- conf: not stated
- class: meas (note: "measured; unordered cross-sectional samples")
- holds: Arabidopsis; unordered cross-sectional samples
- src: lieseckeRankingGenomewideCorrelation2018
- trail: C-RANKNET §Head to head

From the note:

> C-RANKNET:B-0042 [Head to head: ranked against unranked in expression data] **Ranking loses slightly on the same criterion in the largest plant replication.** Liesecke and colleagues built global and pathway-level networks from 9,953 ATH1 microarrays and 1,676 RNA-seq samples under seven normalisations, with six measures including PCC, SCC, PCC-HRR, SCC-HRR, mutual information and partial correlation, scored against GO and against five curated pathways with known sub-pathway structure [4] (measured; unordered cross-sectional samples).
>

Not found in the cited text (where to look, not what is wrong): holds: arabidopsis

## expression-benchmarks.6 (claim)

In Liesecke and colleagues' pathway-level (Pathway Level Correlation) subnetworks, averaged over five pathways in the RNA-seq normalisation comparison, ranking nearly doubled modularity (0.35 raw against 0.68 HRR) and raised the normalised chi-squared statistic for recovering the known sub-pathway partitions (0.20 against 0.35), both at p below 2.2e-16, while on neighbour-voting AUROC against GO the raw coefficients were better, 0.58 against 0.57, p below 0.01. These are not genome-wide results.

- conf: single (critic: C-025)
- class: meas (note: "measured; unordered cross-sectional samples")
- holds: pathway-level co-expression subnetworks averaged over five pathways, RNA-seq normalisation comparison, not the genome-wide benchmark; the critic: the structural win rests entirely on this study and on its pathway-level analysis
- src: lieseckeRankingGenomewideCorrelation2018
- trail: C-RANKNET §Head to head, §Reference errors, §Search record

From the note:

> C-RANKNET:B-0042 [Head to head: ranked against unranked in expression data] **Ranking loses slightly on the same criterion in the largest plant replication.** Liesecke and colleagues built global and pathway-level networks from 9,953 ATH1 microarrays and 1,676 RNA-seq samples under seven normalisations, with six measures including PCC, SCC, PCC-HRR, SCC-HRR, mutual information and partial correlation, scored against GO and against five curated pathways with known sub-pathway structure [4] (measured; unordered cross-sectional samples).
>
> C-RANKNET:B-0043 [Head to head: ranked against unranked in expression data] Ranking nearly doubled modularity (0.35 raw against 0.68 HRR) and raised the normalised chi-squared statistic for recovering the known sub-pathway partitions (0.20 against 0.35), both at p below 2.2e-16.
>
> C-RANKNET:B-0044 [Head to head: ranked against unranked in expression data] On neighbour-voting AUROC against GO, the raw coefficients were better, 0.58 against 0.57, p below 0.01 [4].
>
> C-RANKNET:B-0214 [Search record (synthesis agent)] (1) The Liesecke et al. 2018 raw-against-HRR head-to-head (NV AUROC 0.58 against 0.57, modularity 0.35 against 0.68, normalised chi-squared 0.20 against 0.35) is reported for pathway-level co-expression subnetworks, not for the global networks; the incoming finding did not make that distinction.
>
> C-RANKNET:C-025 [Single-source claims (6)] - The structural win in Part A (nearly doubled modularity 0.35 to 0.68, chi-squared 0.20 to 0.35, twice the vertices at a quarter of the hub degree) rests entirely on Liesecke et al. 2018, and on its pathway-level analysis at that. The verdict calls this 'a specific, reproducible advantage in coverage, comparability and module structure'.
>
> C-RANKNET:C-037 [Reference errors (7)] - Ref 4 (Liesecke et al. 2018): the figures 0.58 versus 0.57 NV AUROC, 0.35 versus 0.68 modularity and 0.20 versus 0.35 normalised chi-squared are pathway-level (PLC) subnetwork results averaged over five pathways in the RNA-seq normalisation comparison.
>
> C-RANKNET:A-034 [Verdict assessment] In the source those figures, and the 0.35/0.68 modularity and 0.20/0.35 chi-squared pairs, come from the Pathway Level Correlation subnetworks averaged over five pathways in the RNA-seq normalisation comparison, not from the genome-wide benchmark.
>

## expression-benchmarks.7 (claim)

Liesecke and colleagues describe the pathway-level result as a trade-off in which "guide genes were clustered correctly at the expense of capturing GO associated gene pairs".

- conf: not stated
- class: not stated
- holds: pathway-level co-expression subnetworks
- src: lieseckeRankingGenomewideCorrelation2018
- trail: C-RANKNET §Head to head

From the note:

> C-RANKNET:B-0045 [Head to head: ranked against unranked in expression data] The authors describe this as a trade-off in which "guide genes were clustered correctly at the expense of capturing GO associated gene pairs" [4].
>

Not found in the cited text (where to look, not what is wrong): holds: pathway-level; holds: co-expression

## expression-benchmarks.8 (claim)

At the global level Liesecke and colleagues conclude that "HRR CCs are able to generate complete genome-wide networks with good performances similar to other classical measures such a MI and PC", which is a null, not a loss.

- conf: not stated
- class: not stated
- holds: genome-wide networks, Arabidopsis
- src: lieseckeRankingGenomewideCorrelation2018
- trail: C-RANKNET §Verdict assessment, §Reference errors

From the note:

> C-RANKNET:A-035 [Verdict assessment] At the global level the same paper concludes that "HRR CCs are able to generate complete genome-wide networks with good performances similar to other classical measures such a MI and PC", which is a null, not a loss.
>
> C-RANKNET:C-039 [Reference errors (7)] The paper's global-level conclusion is the opposite in tone: 'HRR CCs are able to generate complete genome-wide networks with good performances similar to other classical measures such a MI and PC'.
>

Not found in the cited text (where to look, not what is wrong): holds: arabidopsis

## expression-benchmarks.9 (claim)

In Liesecke and colleagues' pathway-level intersection analysis, PCC-HRR gave 550 co-occurring edges against 18,334 for mutual information, averaged over five pathways; the 75 percent guide-gene, modularity 0.78 and chi-squared 0.70 intersection figures sit in Figure 7 panels and were not read as numbers.

- conf: not stated
- class: not stated
- holds: pathway-level intersection counts, averaged over five pathways
- src: lieseckeRankingGenomewideCorrelation2018
- trail: C-RANKNET §Search record

From the note:

> C-RANKNET:B-0215 [Search record (synthesis agent)] I also dropped the 75 percent guide-gene, modularity 0.78 and chi-squared 0.70 intersection figures because they live in Figure 7 panels, which I cannot read as numbers; I used only the text-verifiable intersection counts (550 co-occurring edges for PCC-HRR against 18,334 for mutual information, averaged over five pathways).
>

Not found in the cited text (where to look, not what is wrong): holds: pathway-level

## expression-benchmarks.10 (claim)

At a fixed budget of one million edges in Liesecke and colleagues' study, PCC-HRR gave 26,645 vertices at mean degree 116 and SCC-HRR 24,731 at degree 124, whereas raw PCC gave 13,164 at degree 511 and raw SCC 9,986 at degree 465: ranking spreads the same edges across roughly twice as many genes at a quarter of the hub degree.

- conf: single (critic: C-025)
- class: not stated
- holds: one million edges, Arabidopsis co-expression; the critic: rests entirely on Liesecke et al. 2018
- src: lieseckeRankingGenomewideCorrelation2018
- trail: C-RANKNET §Head to head, §Single-source claims

From the note:

> C-RANKNET:B-0042 [Head to head: ranked against unranked in expression data] **Ranking loses slightly on the same criterion in the largest plant replication.** Liesecke and colleagues built global and pathway-level networks from 9,953 ATH1 microarrays and 1,676 RNA-seq samples under seven normalisations, with six measures including PCC, SCC, PCC-HRR, SCC-HRR, mutual information and partial correlation, scored against GO and against five curated pathways with known sub-pathway structure [4] (measured; unordered cross-sectional samples).
>
> C-RANKNET:B-0047 [Head to head: ranked against unranked in expression data] The same study also shows what ranking does to topology at a fixed edge budget.
>
> C-RANKNET:B-0048 [Head to head: ranked against unranked in expression data] At one million edges, PCC-HRR gave 26,645 vertices at mean degree 116 and SCC-HRR 24,731 at degree 124, whereas raw PCC gave 13,164 at degree 511 and raw SCC 9,986 at degree 465 [4].
>
> C-RANKNET:B-0049 [Head to head: ranked against unranked in expression data] Ranking spreads the same edges across roughly twice as many genes at a quarter of the hub degree.
>
> C-RANKNET:C-025 [Single-source claims (6)] - The structural win in Part A (nearly doubled modularity 0.35 to 0.68, chi-squared 0.20 to 0.35, twice the vertices at a quarter of the hub degree) rests entirely on Liesecke et al. 2018, and on its pathway-level analysis at that. The verdict calls this 'a specific, reproducible advantage in coverage, comparability and module structure'.
>

Not found in the cited text (where to look, not what is wrong): holds: arabidopsis; holds: co-expression

## expression-benchmarks.11 (claim)

Partial correlation networks in Liesecke and colleagues' study sat at chance (neighbour-voting AUROC 0.5) and were not rescued by any other metric.

- conf: not stated
- class: not stated
- holds: Liesecke et al. 2018
- src: lieseckeRankingGenomewideCorrelation2018
- trail: C-RANKNET §Head to head

From the note:

> C-RANKNET:B-0050 [Head to head: ranked against unranked in expression data] Partial correlation networks in the same study sat at chance (neighbour-voting AUROC 0.5) and were not rescued by any other metric [4].
>

Not found in the cited text (where to look, not what is wrong): holds: liesecke; holds: 2018

## expression-benchmarks.12 (claim)

Kumari and colleagues compared eight association measures on 108 Arabidopsis ATH1 arrays and 189 human embryonic stem cell arrays; against AraCyc pathway co-membership for 576 genes in 30 pathways, Spearman, Kendall and Hoeffding's D were the effective measures, and "the widely used Pearson method is generally less efficient, and so is the Distance Covariance method".

- conf: not stated
- class: meas (note: "measured")
- holds: 108 Arabidopsis ATH1 arrays and 189 human embryonic stem cell arrays; AraCyc pathway co-membership, 576 genes in 30 pathways; a small-sample benchmark
- src: kumariEvaluationGeneAssociation2012
- trail: C-RANKNET §Head to head

From the note:

> C-RANKNET:B-0051 [Head to head: ranked against unranked in expression data] **Ranking wins on two curated truth sets in a small-sample benchmark.** Kumari and colleagues compared eight association measures on 108 Arabidopsis ATH1 arrays and 189 human embryonic stem cell arrays [7] (measured).
>
> C-RANKNET:B-0052 [Head to head: ranked against unranked in expression data] Against AraCyc pathway co-membership for 576 genes in 30 pathways, Spearman, Kendall and Hoeffding's D were the effective measures, and "the widely used Pearson method is generally less efficient, and so is the Distance Covariance method" [7].
>

## expression-benchmarks.13 (claim)

On Kumari and colleagues' curated coordinated-transcription-factor task, the top seven clusters recovered 40 positive TFs for Theil-Sen, rank Theil-Sen, Spearman and weighted rank, then 36 for Hoeffding, 31 for Kendall, 28 for Pearson and 27 for distance covariance, with mean per-cluster positive rates of 74 percent (Hoeffding), 70 (Kendall), 68 (rank Theil-Sen), 65 (Spearman), 65 (weighted rank) and 55 (Theil-Sen).

- conf: not stated
- class: not stated
- holds: the curated coordinated-transcription-factor task, top seven clusters
- src: kumariEvaluationGeneAssociation2012
- trail: C-RANKNET §Head to head

From the note:

> C-RANKNET:B-0053 [Head to head: ranked against unranked in expression data] On the curated coordinated-transcription-factor task, the top seven clusters recovered 40 positive TFs for Theil-Sen, rank Theil-Sen, Spearman and weighted rank, then 36 for Hoeffding, 31 for Kendall, 28 for Pearson and 27 for distance covariance, with mean per-cluster positive rates of 74 percent (Hoeffding), 70 (Kendall), 68 (rank Theil-Sen), 65 (Spearman), 65 (weighted rank) and 55 (Theil-Sen) [7].
>

## expression-benchmarks.14 (claim)

In Kumari and colleagues' study Theil-Sen, a median-of-pairwise-slopes estimator on raw values and not a rank statistic, tied for first on the TF task, so the ordering is not cleanly "rank beats magnitude"; rank-family measures are ahead of Pearson on two curated truth sets, with the non-rank estimator tying for first on one of them.

- conf: not stated
- class: not stated
- holds: the TF task and the AraCyc pathway task
- src: kumariEvaluationGeneAssociation2012
- trail: C-RANKNET §Head to head, §Verdicts

From the note:

> C-RANKNET:B-0054 [Head to head: ranked against unranked in expression data] Two bounds sit inside this result.
>
> C-RANKNET:B-0055 [Head to head: ranked against unranked in expression data] Theil-Sen, a median-of-pairwise-slopes estimator on raw values and not a rank statistic, tied for first on the TF task, so the ordering is not cleanly "rank beats magnitude".
>
> C-RANKNET:A-007 [Verdicts] Kumari and colleagues find rank-family measures ahead of Pearson on two curated truth sets [7], but the non-rank Theil-Sen estimator ties for first on one of them and the authors themselves conclude the ordering is contingent on the biological process.
>

Not found in the cited text (where to look, not what is wrong): holds: aracyc

## expression-benchmarks.15 (claim)

Kumari and colleagues conclude that the ranking of methods is "largely contingent upon the biological processes, which necessitates the pre-analysis to identify the best performing method": Kendall was sixth of eight on the Arabidopsis TF task and first on the human data.

- conf: not stated
- class: not stated
- holds: Arabidopsis and human expression data
- src: kumariEvaluationGeneAssociation2012
- trail: C-RANKNET §Head to head

From the note:

> C-RANKNET:B-0056 [Head to head: ranked against unranked in expression data] And the authors' own conclusion is that the ranking of methods is "largely contingent upon the biological processes, which necessitates the pre-analysis to identify the best performing method" [7]: Kendall was sixth of eight on the Arabidopsis TF task and first on the human data.
>
> C-RANKNET:A-007 [Verdicts] Kumari and colleagues find rank-family measures ahead of Pearson on two curated truth sets [7], but the non-rank Theil-Sen estimator ties for first on one of them and the authors themselves conclude the ordering is contingent on the biological process.
>

## expression-benchmarks.16 (claim)

Kumari and colleagues' sensitivity, specificity and predicted-accuracy figures for the pathway task rest on an ad hoc definition of true and false negatives drawn from three slices of the ranked pair list, and the numbers themselves were not read by the review.

- conf: not stated
- class: not stated
- holds: the AraCyc pathway task
- src: kumariEvaluationGeneAssociation2012
- trail: C-RANKNET §Head to head
- limit: access (note: "the numbers themselves live in a supplementary table I did not read")

From the note:

> C-RANKNET:B-0057 [Head to head: ranked against unranked in expression data] The sensitivity, specificity and predicted-accuracy figures for the pathway task rest on an ad hoc definition of true and false negatives drawn from three slices of the ranked pair list, and the numbers themselves live in a supplementary table I did not read.
>

Not found in the cited text (where to look, not what is wrong): holds: aracyc

## expression-benchmarks.17 (claim)

In Vandenbon's sweep, "Using Spearman's correlation instead of Pearson correlation resulted on average in a 0.011 decrease in Quality (equivalent to a 8.2% decrease in sample count)", where Quality is the first principal component of quality measures based on enrichment of functional annotations and of regulatory motifs in promoters, a composite network-quality score.

- conf: not stated
- class: meas (note: "measured")
- holds: 7,200 co-expression networks from 8,796 human and 12,114 mouse bulk RNA-seq samples across 144 cell types and tissues under 50 workflows
- src: vandenbonEvaluationCriticalData2022
- trail: C-RANKNET §Head to head, §Reference errors

From the note:

> C-RANKNET:B-0058 [Head to head: ranked against unranked in expression data] **Ranking costs a little on average and helps only at small n in the largest sweep.** Vandenbon built 7,200 co-expression networks from 8,796 human and 12,114 mouse bulk RNA-seq samples across 144 cell types and tissues under 50 workflows [8] (measured).
>
> C-RANKNET:B-0059 [Head to head: ranked against unranked in expression data] "Using Spearman's correlation instead of Pearson correlation resulted on average in a 0.011 decrease in Quality (equivalent to a 8.2% decrease in sample count).
>
> C-RANKNET:C-004 [danger: Critic: verdict partly supported] Rank of the *value* (Spearman, Kendall) is indistinguishable from Pearson (Song et al.), slightly behind on a composite network-quality score except below 30 samples (Vandenbon), and ahead of Pearson on two curated truth sets where a non-rank estimator ties for first (Kumari et al.).
>
> C-RANKNET:C-043 [Reference errors (7)] - Ref 8 (Vandenbon 2022): 'Quality' is described in the Part A verdict as function-prediction accuracy against GO.
>
> C-RANKNET:C-044 [Reference errors (7)] It is the first principal component of quality measures based on enrichment of functional annotations *and* of regulatory motifs in promoters.
>

## expression-benchmarks.18 (claim)

In Vandenbon's sweep, for small datasets (sample count < 30) Spearman's correlation had on average an advantage over Pearson, with Pearson ahead for roughly 30 to 100 samples and the gap shrinking above that; the recommended workflow uses Spearman only below 30 samples.

- conf: single (critic: C-022)
- class: meas (note: "measured")
- holds: bulk RNA-seq, human and mouse; one study, one data type, one composite metric
- src: vandenbonEvaluationCriticalData2022
- trail: C-RANKNET §Head to head, §What sequencing count, §Single-source claims

From the note:

> C-RANKNET:B-0058 [Head to head: ranked against unranked in expression data] **Ranking costs a little on average and helps only at small n in the largest sweep.** Vandenbon built 7,200 co-expression networks from 8,796 human and 12,114 mouse bulk RNA-seq samples across 144 cell types and tissues under 50 workflows [8] (measured).
>
> C-RANKNET:B-0060 [Head to head: ranked against unranked in expression data] However, for small datasets (sample count < 30) Spearman's correlation had on average an advantage" [8], with Pearson ahead for roughly 30 to 100 samples and the gap shrinking above that.
>
> C-RANKNET:B-0061 [Head to head: ranked against unranked in expression data] The recommended workflow uses Spearman only below 30 samples [8].
>
> C-RANKNET:B-0134 [What sequencing count properties do to rank methods] **Few samples relative to features.** Rank correlation's one reproducible advantage sits here: Spearman beats Pearson below 30 samples in bulk RNA-seq [8], attributed to reduced leverage of extreme values.
>
> C-RANKNET:C-022 [Single-source claims (6)] - 'Rank correlation's one reproducible advantage sits here: Spearman beats Pearson below 30 samples': one study (Vandenbon 2022), one data type (bulk RNA-seq), one composite metric.
>

## expression-benchmarks.19 (claim)

The mechanism Vandenbon gives for the small-sample advantage is that rank correlation is less sensitive to extreme values, which matters most when few samples are present.

- conf: not stated
- class: not stated
- holds: bulk RNA-seq
- src: vandenbonEvaluationCriticalData2022
- trail: C-RANKNET §Head to head, §What sequencing count

From the note:

> C-RANKNET:B-0062 [Head to head: ranked against unranked in expression data] The mechanism the authors give is that rank correlation is less sensitive to extreme values, which matters most when few samples are present [8].
>
> C-RANKNET:B-0134 [What sequencing count properties do to rank methods] **Few samples relative to features.** Rank correlation's one reproducible advantage sits here: Spearman beats Pearson below 30 samples in bulk RNA-seq [8], attributed to reduced leverage of extreme values.
>

## expression-benchmarks.20 (claim)

In Vandenbon's sweep the correlation measure mattered far less than normalisation, batch correction or sample count.

- conf: not stated
- class: not stated
- holds: bulk RNA-seq, human and mouse
- src: vandenbonEvaluationCriticalData2022
- trail: C-RANKNET §Head to head, §What sequencing count

From the note:

> C-RANKNET:B-0058 [Head to head: ranked against unranked in expression data] **Ranking costs a little on average and helps only at small n in the largest sweep.** Vandenbon built 7,200 co-expression networks from 8,796 human and 12,114 mouse bulk RNA-seq samples across 144 cell types and tissues under 50 workflows [8] (measured).
>
> C-RANKNET:B-0063 [Head to head: ranked against unranked in expression data] Crucially, the correlation measure mattered far less than normalisation, batch correction or sample count.
>
> C-RANKNET:B-0132 [What sequencing count properties do to rank methods] Weiss and colleagues tested rarefying, cumulative-sum scaling and DESeq variance stabilisation [13]; Vandenbon found normalisation and batch correction far more consequential than the choice of correlation measure [8], and that variance-stabilising and sample-scaling procedures in the plant work produced networks with average node degree 712 against 114 and average neighbour-voting AUROC 0.47 against 0.62 [4].
>

## expression-benchmarks.21 (claim)

Song, Langfelder and Horvath compared co-expression measures on eight empirical datasets from n equal to 44 to n equal to 1,084 and state "In our study we find that all 3 correlation measures lead to very similar findings", with the supplementary comparison of bicor, Pearson and Spearman concluding "All three types of correlation are similar in terms of GO enrichment".

- conf: not stated
- class: not stated
- holds: eight empirical datasets, n 44 to 1,084, inside WGCNA
- src: songComparisonCoexpressionMeasures2012
- trail: C-RANKNET §Head to head

From the note:

> C-RANKNET:B-0064 [Head to head: ranked against unranked in expression data] **Ranking makes no difference inside WGCNA.** Song, Langfelder and Horvath compared co-expression measures on eight empirical datasets from n equal to 44 to n equal to 1,084 [9].
>
> C-RANKNET:B-0065 [Head to head: ranked against unranked in expression data] On the question of rank against magnitude their statement is flat: "In our study we find that all 3 correlation measures lead to very similar findings", with the supplementary comparison of bicor, Pearson and Spearman concluding "All three types of correlation are similar in terms of GO enrichment" [9].
>

## expression-benchmarks.22 (claim)

Song and colleagues' 6-of-8 significance result is for correlation plus topological overlap against mutual information, not for Spearman against Pearson.

- conf: not stated
- class: not stated
- holds: Song, Langfelder and Horvath 2012
- src: songComparisonCoexpressionMeasures2012
- trail: C-RANKNET §Head to head

From the note:

> C-RANKNET:B-0066 [Head to head: ranked against unranked in expression data] Their 6-of-8 significance result is for correlation plus topological overlap against mutual information, not for Spearman against Pearson.
>

Not found in the cited text (where to look, not what is wrong): holds: song; holds: langfelder; holds: horvath; holds: 2012

## expression-benchmarks.23 (claim)

Wisecaver and colleagues built MR networks from 21,876 experiments across eight plant species and detected overlapping modules with ClusterONE; their MR-versus-PCC claim is about comparability, not accuracy: "MR-based networks consistently included nearly all genes in a given data set, regardless of the MR threshold stringency employed; that was not the case with PCC-based networks", and no AUC or precision comparison against PCC is reported.

- conf: not stated
- class: meas (note: "measured")
- holds: 21,876 experiments across eight plant species
- src: wisecaverGlobalCoexpressionNetwork2017
- trail: C-RANKNET §Head to head

From the note:

> C-RANKNET:B-0070 [Head to head: ranked against unranked in expression data] Wisecaver and colleagues built MR networks from 21,876 experiments across eight plant species and detected overlapping modules with ClusterONE [6] (measured).
>
> C-RANKNET:B-0071 [Head to head: ranked against unranked in expression data] Their MR-versus-PCC claim is about comparability, not accuracy: "MR-based networks consistently included nearly all genes in a given data set, regardless of the MR threshold stringency employed; that was not the case with PCC-based networks" [6], and no AUC or precision comparison against PCC is reported.
>

## expression-benchmarks.24 (claim)

Against known truth, Wisecaver and colleagues' MR modules recovered experimentally validated pathways (14 of 34 aliphatic glucosinolate genes in a single 17-gene N1 module, rising to 56.3 and 71.9 percent in the larger N2 and N3 modules; validated biosynthetic gene clusters at median MR 17.4, P equal to 3.20e-4); this is the closest thing to a truth-based test of mutual rank modules.

- conf: not stated
- class: not stated
- holds: specialized metabolic pathways in plants, eight plant species
- src: wisecaverGlobalCoexpressionNetwork2017
- trail: C-RANKNET §Head to head

From the note:

> C-RANKNET:B-0069 [Head to head: ranked against unranked in expression data] One further result worth stating plainly, because it is the closest thing to a truth-based test of mutual rank modules.
>
> C-RANKNET:B-0070 [Head to head: ranked against unranked in expression data] Wisecaver and colleagues built MR networks from 21,876 experiments across eight plant species and detected overlapping modules with ClusterONE [6] (measured).
>
> C-RANKNET:B-0072 [Head to head: ranked against unranked in expression data] Against known truth, MR modules recovered experimentally validated pathways (14 of 34 aliphatic glucosinolate genes in a single 17-gene N1 module, rising to 56.3 and 71.9 percent in the larger N2 and N3 modules; validated biosynthetic gene clusters at median MR 17.4, P equal to 3.20e-4) but failed on computationally predicted clusters (EC-based clusters median MR 9,670, P equal to 0.187; antiSMASH clusters median MR 10,890, P equal to 0.027, significantly worse than controls; only 7 of 188 putative clusters overlapped a module by three or more genes) [6].
>
> C-RANKNET:R-0022 [References] A global coexpression network approach for connecting genes to specialized metabolic pathways in plants.
>

## expression-benchmarks.25 (claim)

Wisecaver and colleagues' MR modules failed on computationally predicted clusters (EC-based clusters median MR 9,670, P equal to 0.187; antiSMASH clusters median MR 10,890, P equal to 0.027, significantly worse than controls; only 7 of 188 putative clusters overlapped a module by three or more genes): a negative result about the predicted clusters, not about MR, that shows how a rank network behaves when the truth set is wrong.

- conf: not stated
- class: not stated
- holds: computationally predicted gene clusters, eight plant species
- src: wisecaverGlobalCoexpressionNetwork2017
- trail: C-RANKNET §Head to head

From the note:

> C-RANKNET:B-0070 [Head to head: ranked against unranked in expression data] Wisecaver and colleagues built MR networks from 21,876 experiments across eight plant species and detected overlapping modules with ClusterONE [6] (measured).
>
> C-RANKNET:B-0072 [Head to head: ranked against unranked in expression data] Against known truth, MR modules recovered experimentally validated pathways (14 of 34 aliphatic glucosinolate genes in a single 17-gene N1 module, rising to 56.3 and 71.9 percent in the larger N2 and N3 modules; validated biosynthetic gene clusters at median MR 17.4, P equal to 3.20e-4) but failed on computationally predicted clusters (EC-based clusters median MR 9,670, P equal to 0.187; antiSMASH clusters median MR 10,890, P equal to 0.027, significantly worse than controls; only 7 of 188 putative clusters overlapped a module by three or more genes) [6].
>
> C-RANKNET:B-0073 [Head to head: ranked against unranked in expression data] That is a negative result about the predicted clusters, not about MR, but it shows how a rank network behaves when the truth set is wrong.
>

## verdict-a.1 (claim)

Rank-based against magnitude-based network construction has been measured, and the answer splits by which rank device and which criterion, not by "rank versus magnitude" as a single question.

- conf: not stated
- class: meas (critic: C-002)
- holds: bulk gene expression benchmarks
- src: none (the critic's verdict over the review's sources)
- trail: C-RANKNET §critic, §Verdict the body

From the note:

> C-RANKNET:C-002 [danger: Critic: verdict partly supported] Part A (any data type): measured, and the answer splits by which rank device and which criterion, not by "rank versus magnitude" as a single question.
>
> C-RANKNET:A-041 [Verdict the body actually supports] Part A (any data type): measured, and the answer splits by which rank device and which criterion, not by "rank versus magnitude" as a single question.
>

## verdict-a.2 (claim)

Rank of the value (Spearman, Kendall) is indistinguishable from Pearson (Song et al.), slightly behind on a composite network-quality score except below 30 samples (Vandenbon), and ahead of Pearson on two curated truth sets where a non-rank estimator ties for first (Kumari et al.).

- conf: not stated
- class: meas (critic: C-002)
- holds: bulk gene expression
- src: songComparisonCoexpressionMeasures2012, vandenbonEvaluationCriticalData2022, kumariEvaluationGeneAssociation2012
- trail: C-RANKNET §critic, §Verdict the body

From the note:

> C-RANKNET:C-002 [danger: Critic: verdict partly supported] Part A (any data type): measured, and the answer splits by which rank device and which criterion, not by "rank versus magnitude" as a single question.
>
> C-RANKNET:C-004 [danger: Critic: verdict partly supported] Rank of the *value* (Spearman, Kendall) is indistinguishable from Pearson (Song et al.), slightly behind on a composite network-quality score except below 30 samples (Vandenbon), and ahead of Pearson on two curated truth sets where a non-rank estimator ties for first (Kumari et al.).
>
> C-RANKNET:A-043 [Verdict the body actually supports] Rank of the *value* (Spearman, Kendall) is indistinguishable from Pearson (Song et al.), slightly behind on a composite network-quality score except below 30 samples (Vandenbon), and ahead of Pearson on two curated truth sets where a non-rank estimator ties for first (Kumari et al.).
>

## verdict-a.3 (claim)

Ranking wins measurably on coverage, modularity and sub-pathway recovery (Liesecke et al. 2018, pathway-level networks; Wisecaver et al.): higher modularity, better recovery of known sub-pathway partitions and roughly twice the vertex coverage at a fixed edge budget, comparable network size across species and datasets, and inclusion of functionally redundant pairs that fall below a fixed coefficient cutoff.

- conf: single (critic: C-025)
- class: meas (critic: C-002)
- holds: Liesecke et al. 2018 pathway-level networks, Wisecaver et al. across species and datasets, Mutwil et al. for the redundant pairs; reproducible-in-one-study per the critic
- src: lieseckeRankingGenomewideCorrelation2018, wisecaverGlobalCoexpressionNetwork2017, mutwilAssemblyInteractiveCorrelation2010
- trail: C-RANKNET §critic, §Verdict the body, §Verdicts, §Single-source claims

From the note:

> C-RANKNET:C-002 [danger: Critic: verdict partly supported] Part A (any data type): measured, and the answer splits by which rank device and which criterion, not by "rank versus magnitude" as a single question.
>
> C-RANKNET:C-005 [danger: Critic: verdict partly supported] Ranking wins measurably on coverage, modularity and sub-pathway recovery (Liesecke et al. 2018, pathway-level networks; Wisecaver et al.).
>
> C-RANKNET:C-006 [danger: Critic: verdict partly supported] So: measured; no general accuracy advantage for rank-of-value, one unreplicated accuracy advantage for rank-of-coefficient, and reproducible-in-one-study structural advantages.
>
> C-RANKNET:C-025 [Single-source claims (6)] - The structural win in Part A (nearly doubled modularity 0.35 to 0.68, chi-squared 0.20 to 0.35, twice the vertices at a quarter of the hub degree) rests entirely on Liesecke et al. 2018, and on its pathway-level analysis at that. The verdict calls this 'a specific, reproducible advantage in coverage, comparability and module structure'.
>
> C-RANKNET:A-044 [Verdict the body actually supports] Ranking wins measurably on coverage, modularity and sub-pathway recovery (Liesecke et al. 2018, pathway-level networks; Wisecaver et al.).
>
> C-RANKNET:A-006 [Verdicts] On structural and coverage criteria, ranking measurably wins: higher modularity, better recovery of known sub-pathway partitions, roughly twice the vertex coverage at a fixed edge budget [4], comparable network size across species and datasets [6], and inclusion of functionally redundant pairs that fall below a fixed coefficient cutoff [3].
>
> C-RANKNET:R-0009 [References] [3] Marek Mutwil, Björn Usadel, Moritz Schütte, Ann Loraine, Oliver Ebenhöh, Staffan Persson.
>

## verdict-a.4 (claim)

In sum, measured: no general accuracy advantage for rank of the value, one unreplicated accuracy advantage for rank of the coefficient, and structural advantages reproducible in one study.

- conf: not stated
- class: meas (critic: C-006)
- holds: bulk gene expression
- src: none (the critic's verdict over the review's sources)
- trail: C-RANKNET §critic, §Verdict the body

From the note:

> C-RANKNET:C-006 [danger: Critic: verdict partly supported] So: measured; no general accuracy advantage for rank-of-value, one unreplicated accuracy advantage for rank-of-coefficient, and reproducible-in-one-study structural advantages.
>
> C-RANKNET:A-045 [Verdict the body actually supports] So: measured; no general accuracy advantage for rank-of-value, one unreplicated accuracy advantage for rank-of-coefficient, and reproducible-in-one-study structural advantages.
>

## verdict-a.5 (claim)

The review's sensitivity check for its own pooled Part A verdict: removing Obayashi and Kinoshita removes the strongest pro-rank result and strengthens that verdict; removing Vandenbon, Liesecke et al. 2018 or Song et al. still leaves two independent null-or-negative results on function-prediction accuracy.

- conf: not stated
- class: not stated
- holds: the review's Part A verdict as delivered, which the critic replaced ("Use this verdict, not the one above")
- src: obayashiRankCorrelationCoefficient2009, vandenbonEvaluationCriticalData2022, lieseckeRankingGenomewideCorrelation2018, songComparisonCoexpressionMeasures2012
- trail: C-RANKNET §Verdicts, §critic

From the note:

> C-RANKNET:A-016 [Verdicts] **Sensitivity to any single source.** Neither verdict changes if any one source is removed.
>
> C-RANKNET:A-017 [Verdicts] For Part A, removing Obayashi and Kinoshita [1] removes the strongest pro-rank result and strengthens the verdict; removing Vandenbon [8], Liesecke et al. 2018 [4] or Song et al. [9] still leaves two independent null-or-negative results on function-prediction accuracy.
>
> C-RANKNET:C-001 [danger: Critic: verdict partly supported] **Use this verdict, not the one above.**
>

Not found in the cited text (where to look, not what is wrong): holds: review

## microbial-rank-devices.1 (claim)

On microbial abundance data the rank device is the rank of the abundance value, used in three ways: Spearman and Kendall as edge measures, a copula estimator built on Kendall's tau (SPRING), and a rank-vector normal transform inside a time-series method (eLSA).

- conf: not stated
- class: not stated
- holds: microbial abundance data
- src: peschelNetCoMiNetworkConstruction2021, yoonMicrobialNetworksSPRING2019, xiaExtendedLocalSimilarity2011
- trail: C-RANKNET §The rank device in microbial

From the note:

> C-RANKNET:B-0078 [The rank device in microbial abundance data] Its rank device is the rank of the abundance value, used in three ways.
>
> C-RANKNET:B-0079 [The rank device in microbial abundance data] **Spearman and Kendall as edge measures.** These are the field's default "correlation-based" options and are offered as such in the standard tooling [21].
>
> C-RANKNET:B-0081 [The rank device in microbial abundance data] **A copula estimator built on Kendall's tau.** SPRING estimates a latent correlation from Kendall's tau through a closed-form bridge function for a truncated Gaussian copula, so exact zeros are modelled rather than replaced by pseudocounts, then runs Meinshausen-Buhlmann neighbourhood selection with StARS [12].
>
> C-RANKNET:B-0084 [The rank device in microbial abundance data] **A rank-vector normal transform inside a time-series method.** eLSA normalises each series by a normal score transformation before local and time-lagged similarity scoring [22], and is the one widely used microbiome association method that requires ordered samples.
>

## microbial-rank-devices.2 (claim)

Spearman and Kendall are the microbiome field's default "correlation-based" options and are offered as such in the standard tooling; they require only unordered cross-sectional samples.

- conf: not stated
- class: not stated
- holds: microbiome network tooling (NetCoMi)
- src: peschelNetCoMiNetworkConstruction2021
- trail: C-RANKNET §The rank device in microbial

From the note:

> C-RANKNET:B-0079 [The rank device in microbial abundance data] **Spearman and Kendall as edge measures.** These are the field's default "correlation-based" options and are offered as such in the standard tooling [21].
>
> C-RANKNET:B-0080 [The rank device in microbial abundance data] They require only unordered cross-sectional samples.
>

Not found in the cited text (where to look, not what is wrong): holds: netcomi

## microbial-rank-devices.3 (claim)

The review's searches found no study applying mutual rank or highest reciprocal rank to microbial abundance data: Europe PMC returned five multi-omics hits in which mutual rank was applied to the gene side only, and the top hit, opened in full, confirms the split: co-expressed genes were "selected with a Pearson's correlation coefficient higher than 0.75 and a Mutual Rank of at least 2.2", while the microbial side used Spearman's rank correlations on OTUs.

- conf: not stated
- class: search (note: "Each statement is about the searches run, not about what the literature has ruled out")
- holds: routes: web searches pairing "mutual rank" and "highest reciprocal rank" with microbiome, taxa, co-abundance, metagenomic, OTU and 16S; Europe PMC exact-phrase search for "mutual rank" with microbiome, microbial, OTU or 16S; the routes are inherited from the search agents, the synthesis agent could not run new keyword searches
- src: kudjordjieFusariumOxysporumDisrupts2022
- trail: C-RANKNET §Gaps, with the routes, §Search record
- search: searched, not found (note: "Each statement is about the searches run, not about what the literature has ruled out")

From the note:

> C-RANKNET:B-0170 [Gaps, with the routes behind them] Each statement is about the searches run, not about what the literature has ruled out.
>
> C-RANKNET:B-0171 [Gaps, with the routes behind them] **No study applying mutual rank or highest reciprocal rank to microbial abundance data.** Routes: web searches pairing "mutual rank" and "highest reciprocal rank" with microbiome, taxa, co-abundance, metagenomic, OTU and 16S; Europe PMC exact-phrase search for "mutual rank" combined with microbiome, microbial, OTU or 16S, returning five multi-omics hits in which mutual rank was applied to the gene side only.
>
> C-RANKNET:B-0172 [Gaps, with the routes behind them] The top hit confirms the split directly: in one experiment yielding both networks, co-expressed genes were "selected with a Pearson's correlation coefficient higher than 0.75 and a Mutual Rank of at least 2.2", while the microbial side used Spearman's rank correlations on OTUs [23].
>
> C-RANKNET:B-0223 [Search record (synthesis agent)] The session WebSearch quota was already exhausted (200 of 200) when I was invoked, so every route above was Crossref, Unpaywall, Europe PMC REST, direct curl or WebFetch; I could not run a single new keyword search, which is why the negative claims below rest on the search agents' route lists rather than on new sweeps of my own.
>
> C-RANKNET:B-0224 [Search record (synthesis agent)] NOT-FOUND CLAIMS AND THE ROUTES BEHIND THEM (all inherited from the search agents, whose route lists I reproduce, plus my own full-text confirmation where noted).
>
> C-RANKNET:B-0225 [Search record (synthesis agent)] (1) No study applying mutual rank or highest reciprocal rank to microbial abundance data: web searches pairing "mutual rank" and "highest reciprocal rank" with microbiome, taxa, co-abundance, metagenomic, OTU and 16S; Europe PMC exact-phrase search for "mutual rank" AND (microbiome OR microbial OR OTU OR "16S"), five hits, all multi-omics papers applying mutual rank to the gene side.
>
> C-RANKNET:B-0226 [Search record (synthesis agent)] I opened the top hit myself (Kudjordjie et al. 2022) and confirmed it uses mutual rank for Arabidopsis genes and plain Spearman for OTUs.
>

## compositional-closure.1 (claim)

Rank correlation is partially, not fully, protected from compositional closure: Friedman and Alm demonstrated compositional distortion in Spearman as well as Pearson and found Spearman "only marginally better", and Weiss and colleagues found rank measures "less affected by compositional data but still not immune".

- conf: not stated
- class: not stated
- holds: simulated microbial abundance data
- src: friedmanInferringCorrelationNetworks2012, weissCorrelationDetectionStrategies2016
- trail: C-RANKNET §What sequencing count

From the note:

> C-RANKNET:B-0085 [The rank device in microbial abundance data] The benchmark record for these is as follows, and every entry is a simulation.
>
> C-RANKNET:B-0108 [The rank device in microbial abundance data] - Weiss and colleagues, the field's largest correlation benchmark (eight tools, 91 simulated OTU tables, 200 to 10,000 features, eight generative models): "Rank-based measures such as MIC and Spearman, as well as Bray-Curtis, are less affected by compositional data but still not immune" [13].
>
> C-RANKNET:B-0116 [What sequencing count properties do to rank methods] **Compositional closure.** Rank correlation is partially, not fully, protected.
>
> C-RANKNET:B-0117 [What sequencing count properties do to rank methods] Friedman and Alm demonstrated compositional distortion in Spearman as well as Pearson and found Spearman "only marginally better" [15]; Weiss and colleagues found rank measures "less affected by compositional data but still not immune" [13].
>

