## known-truth.1 (claim)

Ghaeli, Aghdam and Eslahchi open by stating the field's core obstacle: "the lack of experimentally validated gold standards presents a significant obstacle in evaluating the biological accuracy of inferred networks".

- conf: not stated
- class: not stated
- holds: microbial network inference
- src: ghaeliEvaluatingMicrobialNetwork2026
- trail: C-RANKNET §The rank device in microbial

From the note:

> C-RANKNET:B-0098 [The rank device in microbial abundance data] Ghaeli, Aghdam and Eslahchi evaluated six algorithms on four real 16S datasets under bootstrap, noise and synthetic perturbation; SPRING appears in neither of their two top-performer tables, which are filled by SparCC, gCoda and SPIEC-EASI(glasso) [19].
>
> C-RANKNET:B-0100 [The rank device in microbial abundance data] That paper opens by stating the field's core obstacle: "the lack of experimentally validated gold standards presents a significant obstacle in evaluating the biological accuracy of inferred networks" [19].
>

## expression-benchmarks.1 (claim)

Five studies in gene expression put the ranked-against-unranked comparison directly, and they do not agree, because they do not score the same thing.

- conf: not stated
- class: not stated
- holds: bulk gene expression
- src: none (the reviewer's synthesis)
- trail: C-RANKNET §Head to head, §Verdicts

From the note:

> C-RANKNET:B-0038 [Head to head: ranked against unranked in expression data] Five studies put the comparison directly, and they do not agree, because they do not score the same thing.
>
> C-RANKNET:A-004 [Verdicts] The comparison has been run repeatedly in bulk gene expression, which is the only data type where it has been run properly, and the direction depends entirely on the criterion.
>

## expression-benchmarks.7 (claim)

Liesecke and colleagues describe the pathway-level result as a trade-off in which "guide genes were clustered correctly at the expense of capturing GO associated gene pairs".

- conf: not stated
- class: not stated
- holds: pathway-level co-expression subnetworks
- src: lieseckeRankingGenomewideCorrelation2018
- trail: C-RANKNET §Head to head, §Search record

From the note:

> C-RANKNET:B-0043 [Head to head: ranked against unranked in expression data] Ranking nearly doubled modularity (0.35 raw against 0.68 HRR) and raised the normalised chi-squared statistic for recovering the known sub-pathway partitions (0.20 against 0.35), both at p below 2.2e-16.
>
> C-RANKNET:B-0044 [Head to head: ranked against unranked in expression data] On neighbour-voting AUROC against GO, the raw coefficients were better, 0.58 against 0.57, p below 0.01 [4].
>
> C-RANKNET:B-0045 [Head to head: ranked against unranked in expression data] The authors describe this as a trade-off in which "guide genes were clustered correctly at the expense of capturing GO associated gene pairs" [4].
>
> C-RANKNET:B-0214 [Search record (synthesis agent)] (1) The Liesecke et al. 2018 raw-against-HRR head-to-head (NV AUROC 0.58 against 0.57, modularity 0.35 against 0.68, normalised chi-squared 0.20 against 0.35) is reported for pathway-level co-expression subnetworks, not for the global networks; the incoming finding did not make that distinction.
>

## expression-benchmarks.8 (claim)

At the global level Liesecke and colleagues conclude that "HRR CCs are able to generate complete genome-wide networks with good performances similar to other classical measures such a MI and PC", which is a null, not a loss.

- conf: not stated
- class: not stated
- holds: genome-wide networks from 9,953 ATH1 microarrays and 1,676 RNA-seq samples
- src: lieseckeRankingGenomewideCorrelation2018
- trail: C-RANKNET §Verdict assessment, §Reference errors, §Head to head

From the note:

> C-RANKNET:A-035 [Verdict assessment] At the global level the same paper concludes that "HRR CCs are able to generate complete genome-wide networks with good performances similar to other classical measures such a MI and PC", which is a null, not a loss.
>
> C-RANKNET:C-039 [Reference errors (7)] The paper's global-level conclusion is the opposite in tone: 'HRR CCs are able to generate complete genome-wide networks with good performances similar to other classical measures such a MI and PC'.
>
> C-RANKNET:B-0042 [Head to head: ranked against unranked in expression data] **Ranking loses slightly on the same criterion in the largest plant replication.** Liesecke and colleagues built global and pathway-level networks from 9,953 ATH1 microarrays and 1,676 RNA-seq samples under seven normalisations, with six measures including PCC, SCC, PCC-HRR, SCC-HRR, mutual information and partial correlation, scored against GO and against five curated pathways with known sub-pathway structure [4] (measured; unordered cross-sectional samples).
>

## expression-benchmarks.14 (claim)

In Kumari and colleagues' study Theil-Sen, a median-of-pairwise-slopes estimator on raw values and not a rank statistic, tied for first on the TF task, so the ordering is not cleanly "rank beats magnitude"; rank-family measures are ahead of Pearson on two curated truth sets, with the non-rank estimator tying for first on one of them, and the authors themselves conclude the ordering is contingent on the biological process.

- conf: not stated
- class: not stated
- holds: the TF task and the AraCyc pathway task
- src: kumariEvaluationGeneAssociation2012
- trail: C-RANKNET §Head to head, §Verdicts

From the note:

> C-RANKNET:B-0052 [Head to head: ranked against unranked in expression data] Against AraCyc pathway co-membership for 576 genes in 30 pathways, Spearman, Kendall and Hoeffding's D were the effective measures, and "the widely used Pearson method is generally less efficient, and so is the Distance Covariance method" [7].
>
> C-RANKNET:B-0054 [Head to head: ranked against unranked in expression data] Two bounds sit inside this result.
>
> C-RANKNET:B-0055 [Head to head: ranked against unranked in expression data] Theil-Sen, a median-of-pairwise-slopes estimator on raw values and not a rank statistic, tied for first on the TF task, so the ordering is not cleanly "rank beats magnitude".
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

> C-RANKNET:B-0052 [Head to head: ranked against unranked in expression data] Against AraCyc pathway co-membership for 576 genes in 30 pathways, Spearman, Kendall and Hoeffding's D were the effective measures, and "the widely used Pearson method is generally less efficient, and so is the Distance Covariance method" [7].
>
> C-RANKNET:B-0057 [Head to head: ranked against unranked in expression data] The sensitivity, specificity and predicted-accuracy figures for the pathway task rest on an ad hoc definition of true and false negatives drawn from three slices of the ranked pair list, and the numbers themselves live in a supplementary table I did not read.
>

## verdict-a.1 (claim)

Rank-based against magnitude-based network construction has been measured, and the answer splits by which rank device and which criterion, not by "rank versus magnitude" as a single question.

- conf: not stated
- class: meas (critic: C-002)
- holds: Part A, any data type; the evidence rests entirely on bulk expression
- src: none (the critic's verdict over the review's sources)
- trail: C-RANKNET §critic, §Verdict the body, §Coverage gaps

From the note:

> C-RANKNET:C-002 [danger: Critic: verdict partly supported] Part A (any data type): measured, and the answer splits by which rank device and which criterion, not by "rank versus magnitude" as a single question.
>
> C-RANKNET:A-041 [Verdict the body actually supports] Part A (any data type): measured, and the answer splits by which rank device and which criterion, not by "rank versus magnitude" as a single question.
>
> C-RANKNET:C-052 [Coverage gaps (10)] - **Single-cell transcriptomics**: Skinnider, Squair and Foster 2019 is the only benchmark that puts rank correlations against compositionally aware proportionality on zero-rich data, and it is unobtained, so the review's Part A rests entirely on bulk expression.
>

## verdict-a.2 (claim)

Rank of the value (Spearman, Kendall) is indistinguishable from Pearson (Song et al.), slightly behind on a composite network-quality score except below 30 samples (Vandenbon), and ahead of Pearson on two curated truth sets where a non-rank estimator ties for first (Kumari et al.).

- conf: not stated
- class: meas (critic: C-002)
- holds: Part A, any data type; the evidence rests entirely on bulk expression
- src: songComparisonCoexpressionMeasures2012, vandenbonEvaluationCriticalData2022, kumariEvaluationGeneAssociation2012
- trail: C-RANKNET §critic, §Verdict the body, §Coverage gaps

From the note:

> C-RANKNET:C-002 [danger: Critic: verdict partly supported] Part A (any data type): measured, and the answer splits by which rank device and which criterion, not by "rank versus magnitude" as a single question.
>
> C-RANKNET:C-004 [danger: Critic: verdict partly supported] Rank of the *value* (Spearman, Kendall) is indistinguishable from Pearson (Song et al.), slightly behind on a composite network-quality score except below 30 samples (Vandenbon), and ahead of Pearson on two curated truth sets where a non-rank estimator ties for first (Kumari et al.).
>
> C-RANKNET:A-043 [Verdict the body actually supports] Rank of the *value* (Spearman, Kendall) is indistinguishable from Pearson (Song et al.), slightly behind on a composite network-quality score except below 30 samples (Vandenbon), and ahead of Pearson on two curated truth sets where a non-rank estimator ties for first (Kumari et al.).
>
> C-RANKNET:C-052 [Coverage gaps (10)] - **Single-cell transcriptomics**: Skinnider, Squair and Foster 2019 is the only benchmark that puts rank correlations against compositionally aware proportionality on zero-rich data, and it is unobtained, so the review's Part A rests entirely on bulk expression.
>

## verdict-a.4 (claim)

In sum, measured: no general accuracy advantage for rank of the value, one unreplicated accuracy advantage for rank of the coefficient, and structural advantages reproducible in one study.

- conf: not stated
- class: meas (critic: C-006)
- holds: Part A, any data type; the evidence rests entirely on bulk expression
- src: none (the critic's verdict over the review's sources)
- trail: C-RANKNET §critic, §Verdict the body, §Coverage gaps

From the note:

> C-RANKNET:C-006 [danger: Critic: verdict partly supported] So: measured; no general accuracy advantage for rank-of-value, one unreplicated accuracy advantage for rank-of-coefficient, and reproducible-in-one-study structural advantages.
>
> C-RANKNET:A-045 [Verdict the body actually supports] So: measured; no general accuracy advantage for rank-of-value, one unreplicated accuracy advantage for rank-of-coefficient, and reproducible-in-one-study structural advantages.
>
> C-RANKNET:C-052 [Coverage gaps (10)] - **Single-cell transcriptomics**: Skinnider, Squair and Foster 2019 is the only benchmark that puts rank correlations against compositionally aware proportionality on zero-rich data, and it is unobtained, so the review's Part A rests entirely on bulk expression.
>

## verdict-a.5 (claim)

The review's sensitivity check for its own pooled Part A verdict: removing Obayashi and Kinoshita removes the strongest pro-rank result and strengthens that verdict; removing Vandenbon, Liesecke et al. 2018 or Song et al. still leaves two independent null-or-negative results on function-prediction accuracy.

- conf: not stated
- class: not stated
- holds: the review's Part A verdict as delivered, which the critic replaced ("Use this verdict, not the one above")
- src: obayashiRankCorrelationCoefficient2009, vandenbonEvaluationCriticalData2022, lieseckeRankingGenomewideCorrelation2018, songComparisonCoexpressionMeasures2012
- trail: C-RANKNET §Verdicts, §critic, §Verdict assessment

From the note:

> C-RANKNET:A-016 [Verdicts] **Sensitivity to any single source.** Neither verdict changes if any one source is removed.
>
> C-RANKNET:A-017 [Verdicts] For Part A, removing Obayashi and Kinoshita [1] removes the strongest pro-rank result and strengthens the verdict; removing Vandenbon [8], Liesecke et al. 2018 [4] or Song et al. [9] still leaves two independent null-or-negative results on function-prediction accuracy.
>
> C-RANKNET:C-001 [danger: Critic: verdict partly supported] **Use this verdict, not the one above.**
>
> C-RANKNET:A-037 [Verdict assessment] Beyond those, the Part A verdict pools two devices the review's own opening paragraph separates, rank of the coefficient and rank of the value, and pools four incommensurable metrics (neighbour-voting AUROC, a composite PC1 "Quality" that includes promoter motif enrichment, GO enrichment p-values, TF cluster counts) into a single direction count.
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
> C-RANKNET:R-0082 [References] NetCoMi: network construction and comparison for microbiome data in R. *Briefings in Bioinformatics*, volume 22, issue 4, 2021, article bbaa290 (published online 2020).
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
> C-RANKNET:B-0101 [The rank device in microbial abundance data] Where plain rank correlation has been compared with magnitude correlation on simulated microbial data, the answer is consistently "no difference".
>
> C-RANKNET:B-0106 [The rank device in microbial abundance data] - Friedman and Alm, the paper that introduced SparCC: "these compositional effects are not limited to Pearson correlation, and are also present in non-parametric correlations, such as Spearman correlations", and "Spearman correlations performed only marginally better" [15].
>
> C-RANKNET:B-0108 [The rank device in microbial abundance data] - Weiss and colleagues, the field's largest correlation benchmark (eight tools, 91 simulated OTU tables, 200 to 10,000 features, eight generative models): "Rank-based measures such as MIC and Spearman, as well as Bray-Curtis, are less affected by compositional data but still not immune" [13].
>
> C-RANKNET:B-0116 [What sequencing count properties do to rank methods] **Compositional closure.** Rank correlation is partially, not fully, protected.
>
> C-RANKNET:B-0117 [What sequencing count properties do to rank methods] Friedman and Alm demonstrated compositional distortion in Spearman as well as Pearson and found Spearman "only marginally better" [15]; Weiss and colleagues found rank measures "less affected by compositional data but still not immune" [13].
>

## spring.13 (claim)

Ghaeli and colleagues' reported limitation for SPRING, "a general lack of discriminative power, as multiple topologies yielded non-significant differences across all datasets", is reported in the same terms for OIPCQ, gCoda, S-E(glasso) and S-E(mb), so it is a property of the benchmark as much as of SPRING.

- conf: not stated
- class: not stated
- holds: Ghaeli et al.'s reproducibility benchmark on four real 16S datasets
- src: ghaeliEvaluatingMicrobialNetwork2026
- trail: C-RANKNET §The rank device in microbial, §Search record, §Reference errors

From the note:

> C-RANKNET:B-0098 [The rank device in microbial abundance data] Ghaeli, Aghdam and Eslahchi evaluated six algorithms on four real 16S datasets under bootstrap, noise and synthetic perturbation; SPRING appears in neither of their two top-performer tables, which are filled by SparCC, gCoda and SPIEC-EASI(glasso) [19].
>
> C-RANKNET:B-0099 [The rank device in microbial abundance data] Their reported limitation for SPRING, "a general lack of discriminative power, as multiple topologies yielded non-significant differences across all datasets" [19], is reported in the same terms for OIPCQ, gCoda, S-E(glasso) and S-E(mb), so it is a property of the benchmark as much as of SPRING.
>
> C-RANKNET:B-0220 [Search record (synthesis agent)] (3) The Ghaeli et al. "general lack of discriminative power" is reported in identical terms for OIPCQ, gCoda, S-E(glasso) and S-E(mb) as well as SPRING, so it is a property of that benchmark rather than a property of the rank method; I verified that SPRING appears in neither of their top-performer tables, which is the defensible claim.
>
> C-RANKNET:C-047 [Reference errors (7)] - Ref 19 (Ghaeli et al. 2026): the metric is reproducibility, F-score and Jaccard similarity between networks inferred from bootstrap and noise-perturbed variants of real data, in a paper whose premise is that no gold standard exists. The review's Part B verdict uses SPRING's absence from Tables 3 and 4 as evidence about performance alongside truth-based simulation benchmarks.
>

## microbial-modules.2 (claim)

In the MNetClass benchmark, edge betweenness, label propagation, leading eigenvector, fast greedy, Louvain and manta used MNetClass's network, while WGCNA was run with "default parameters to automatically construct the network", its own Pearson-based construction; WGCNA is also one of the two comparators MNetClass could not beat on PPV, which makes that comparison partly a rank-versus-magnitude construction comparison.

- conf: not stated
- class: not stated
- holds: the MNetClass benchmark on simulated matrices
- src: wangMNetClassControlfreeMicrobial2025
- trail: C-RANKNET §Reference errors, §The rank device in microbial

From the note:

> C-RANKNET:C-040 [Reference errors (7)] - Ref 24 (MNetClass): 'Every comparator used the same Spearman network' is not what the paper says.
>
> C-RANKNET:C-041 [Reference errors (7)] Edge betweenness, label propagation, leading eigenvector, fast greedy, Louvain and manta used MNetClass's network; WGCNA was run with 'default parameters to automatically construct the network', that is, its own Pearson-based construction.
>
> C-RANKNET:C-042 [Reference errors (7)] WGCNA is also one of the two comparators MNetClass could not beat on PPV, which makes that comparison partly a rank-versus-magnitude construction comparison, the opposite of the review's dismissal.
>
> C-RANKNET:B-0114 [The rank device in microbial abundance data] MNetClass builds a Spearman network, partitions it with Walktrap and scores subnetworks with a rank-sum-ratio and entropy-weight model; against six other community detection algorithms on 50 FABIA-simulated matrices with true cluster labels it was significantly better on sensitivity and accuracy and not different from manta or WGCNA on positive predictive value [24].
>

## zero-ties.3 (claim)

Connor and colleagues frame the tie correction as preventing "the spurious conclusion that two taxa are ecologically related because they are both absent from many of the same locations".

- conf: not stated
- class: not stated
- holds: microbial co-occurrence networks
- src: connorUsingNullModels2017
- trail: C-RANKNET §What sequencing count

From the note:

> C-RANKNET:B-0125 [What sequencing count properties do to rank methods] They frame the correction as preventing "the spurious conclusion that two taxa are ecologically related because they are both absent from many of the same locations" [17].
>
> C-RANKNET:R-0066 [References] Using null models to infer microbial co-occurrence networks.
>

## sparsity.3 (claim)

The single best precision figure reported for any rank-normalised tool on the hardest case, sparse Lotka-Volterra relationships, is LSA at 0.2, which is four false positives per true positive; whether this per-tool figure is in the main text read or in the supplementary files not obtained is unsettled.

- conf: not stated
- class: not stated
- holds: sparse Lotka-Volterra relationships in Weiss et al.'s simulations
- src: weissCorrelationDetectionStrategies2016 (main text only)
- trail: C-RANKNET §What sequencing count, §Full-text breaches
- limit: access (critic: C-015)

From the note:

> C-RANKNET:B-0108 [The rank device in microbial abundance data] - Weiss and colleagues, the field's largest correlation benchmark (eight tools, 91 simulated OTU tables, 200 to 10,000 features, eight generative models): "Rank-based measures such as MIC and Spearman, as well as Bray-Curtis, are less affected by compositional data but still not immune" [13].
>
> C-RANKNET:B-0130 [What sequencing count properties do to rank methods] The single best precision figure reported for any rank-normalised tool on the hardest case, sparse Lotka-Volterra relationships, is LSA at 0.2 [13], which is four false positives per true positive.
>
> C-RANKNET:C-015 [Full-text breaches (4)] - Weiss et al. 2016 (ref 13): the review states that the per-tool precision, sensitivity and F1 numbers live in supplementary files it could not obtain, then quotes 'the single best precision figure reported for any rank-normalised tool on the hardest case ... is LSA at 0.2'.
>
> C-RANKNET:C-016 [Full-text breaches (4)] That is a per-tool precision number.
>
> C-RANKNET:C-017 [Full-text breaches (4)] Either it is in the main text, in which case the not-obtained note is too broad, or it is not, in which case it breaches Common rule 1.
>
> C-RANKNET:C-018 [Full-text breaches (4)] I could not reach the eScholarship accepted manuscript (HTTP 403 to curl, blank to WebFetch) to settle it.
>
> C-RANKNET:A-040 [Verdict assessment] Same for the Weiss LSA precision 0.2, which sits oddly next to the review's own statement that the per-tool precision values live in supplementary files it could not obtain.
>
> C-RANKNET:R-0052 [References] DOI: 10.1038/ismej.2015.235 (read as the author accepted manuscript, eScholarship qt3ps0c507; main text only)
>
> C-RANKNET:C-015 [Full-text breaches (4)] - Weiss et al. 2016 (ref 13): the review states that the per-tool precision, sensitivity and F1 numbers live in supplementary files it could not obtain, then quotes 'the single best precision figure reported for any rank-normalised tool on the hardest case ... is LSA at 0.2'.
>

Not found in the cited text (where to look, not what is wrong): holds: simulations

## sequencing-depth.2 (claim)

In the plant work, variance-stabilising and sample-scaling procedures produced networks with average node degree 712 against 114 and average neighbour-voting AUROC 0.47 against 0.62.

- conf: not stated
- class: not stated
- holds: the plant co-expression work of Liesecke et al. 2018
- src: lieseckeRankingGenomewideCorrelation2018
- trail: C-RANKNET §What sequencing count

From the note:

> C-RANKNET:B-0132 [What sequencing count properties do to rank methods] Weiss and colleagues tested rarefying, cumulative-sum scaling and DESeq variance stabilisation [13]; Vandenbon found normalisation and batch correction far more consequential than the choice of correlation measure [8], and that variance-stabilising and sample-scaling procedures in the plant work produced networks with average node degree 712 against 114 and average neighbour-voting AUROC 0.47 against 0.62 [4].
>
> C-RANKNET:R-0013 [References] [4] Franziska Liesecke, Dimitri Daudu, Rodolphe Dugé de Bernonville, Sébastien Besseau, Marc Clastre, Vincent Courdavault, Johan-Owen de Craene, Joël Crèche, Nathalie Giglioli-Guivarc'h, Gaëlle Glévarec, Olivier Pichon, Thomas Dugé de Bernonville.
>
> C-RANKNET:R-0014 [References] Ranking genome-wide correlation measurements improves microarray and RNA-seq based global and targeted co-expression networks.
>

Not found in the cited text (where to look, not what is wrong): holds: 2018

## sample-size.3 (claim)

Tool disagreement in the few-samples regime is severe, on a figure that covers every data set and model: Weiss and colleagues report "an average of 31.5% shared edge inference for all pair-wise combinations of tools, and for all data sets/models tested".

- conf: not stated
- class: model (note: "91 simulated OTU tables")
- holds: Weiss et al.'s simulated OTU tables
- src: weissCorrelationDetectionStrategies2016
- trail: C-RANKNET §What sequencing count

From the note:

> C-RANKNET:B-0108 [The rank device in microbial abundance data] - Weiss and colleagues, the field's largest correlation benchmark (eight tools, 91 simulated OTU tables, 200 to 10,000 features, eight generative models): "Rank-based measures such as MIC and Spearman, as well as Bray-Curtis, are less affected by compositional data but still not immune" [13].
>
> C-RANKNET:B-0134 [What sequencing count properties do to rank methods] **Few samples relative to features.** Rank correlation's one reproducible advantage sits here: Spearman beats Pearson below 30 samples in bulk RNA-seq [8], attributed to reduced leverage of extreme values.
>
> C-RANKNET:B-0136 [What sequencing count properties do to rank methods] Tool disagreement in this regime is severe: Weiss and colleagues report "an average of 31.5% shared edge inference for all pair-wise combinations of tools, and for all data sets/models tested" [13].
>

## taxon-grouping.1 (claim)

In the studies the reviewer read, rank-through-time metrics have not been used to group taxa: Duran-Pinedo and colleagues used rank clocks and mean rank shift as descriptive summaries of reordering in a 360-sample, 12-month oral microbiome time series, then built the association network with SPIEC-EASI and clustered taxa with a Dirichlet process Gaussian process mixture over abundance trajectories.

- conf: not stated
- class: meas (note: "measured; 15 individuals, 45 teeth, 16S and ITS")
- holds: human oral microbiome, 360 samples over 12 months, 15 individuals, 45 teeth, 16S and ITS
- src: duranpinedoLongtermDynamicsHuman2021
- trail: C-RANKNET §Rank through time, §Search record

From the note:

> C-RANKNET:B-0150 [Rank through time in community ecology, and whether it groups taxa] Has any of it been used to group taxa?
>
> C-RANKNET:B-0151 [Rank through time in community ecology, and whether it groups taxa] In the studies I read myself, no.
>
> C-RANKNET:B-0152 [Rank through time in community ecology, and whether it groups taxa] Duran-Pinedo and colleagues used rank clocks and mean rank shift as descriptive summaries of reordering in a 360-sample, 12-month oral microbiome time series, then built the association network with SPIEC-EASI and clustered taxa with a Dirichlet process Gaussian process mixture over abundance trajectories [29] (measured; 15 individuals, 45 teeth, 16S and ITS).
>
> C-RANKNET:B-0230 [Search record (synthesis agent)] I confirmed the pattern myself in the two microbial cases I read in full: Duran-Pinedo et al. 2021 computes rank clocks and mean rank shift descriptively while building the network with SPIEC-EASI and grouping taxa with a Dirichlet process Gaussian process mixture, and Liu et al. 2025 defines subcommunities with latent Dirichlet allocation first and computes rank change on them afterwards.
>
> C-RANKNET:R-0112 [References] Long-term dynamics of the human oral microbiome during clinical disease progression.
>

## taxon-grouping.3 (claim)

In both the Duran-Pinedo and the Liu studies the rank quantity is reported alongside a separate magnitude-based or log-ratio-based grouping step, never as the basis of one.

- conf: not stated
- class: not stated
- holds: two microbial time-series studies
- src: duranpinedoLongtermDynamicsHuman2021, liuMicrobesClimateRefugia2025
- trail: C-RANKNET §Rank through time, §Search record

From the note:

> C-RANKNET:B-0152 [Rank through time in community ecology, and whether it groups taxa] Duran-Pinedo and colleagues used rank clocks and mean rank shift as descriptive summaries of reordering in a 360-sample, 12-month oral microbiome time series, then built the association network with SPIEC-EASI and clustered taxa with a Dirichlet process Gaussian process mixture over abundance trajectories [29] (measured; 15 individuals, 45 teeth, 16S and ITS).
>
> C-RANKNET:B-0154 [Rank through time in community ecology, and whether it groups taxa] In both cases the rank quantity is reported alongside a separate magnitude-based or log-ratio-based grouping step, never as the basis of one.
>
> C-RANKNET:B-0230 [Search record (synthesis agent)] I confirmed the pattern myself in the two microbial cases I read in full: Duran-Pinedo et al. 2021 computes rank clocks and mean rank shift descriptively while building the network with SPIEC-EASI and grouping taxa with a Dirichlet process Gaussian process mixture, and Liu et al. 2025 defines subcommunities with latent Dirichlet allocation first and computes rank change on them afterwards.
>

## taxon-grouping.6 (claim)

Ananke's comparator set is Euclidean and Manhattan distance on the same standardised trajectories, with no rank-based comparator, and its stated failure mode is that the slope-difference distance cannot separate low-variance from high-variance stationary profiles.

- conf: not stated
- class: not stated
- holds: simulated 16S-style series
- src: hallAnankeTemporalClustering2017
- trail: C-RANKNET §Rank through time

From the note:

> C-RANKNET:B-0156 [Rank through time in community ecology, and whether it groups taxa] Ananke normalises counts by per-sample depth, z-scores each trajectory, computes a short time-series slope-difference distance and clusters with DBSCAN, scoring adjusted mutual information above 0.8 against six ground-truth patterns with as few as ten time points, and dropping to median 0.69 at 500 points and 0.62 at 1,000 [31] (modelled; simulated 16S-style series).
>
> C-RANKNET:B-0157 [Rank through time in community ecology, and whether it groups taxa] Its comparator set is Euclidean and Manhattan distance on the same standardised trajectories, with no rank-based comparator, and its stated failure mode is that the slope-difference distance cannot separate low-variance from high-variance stationary profiles [31].
>

## verdict-b.2 (claim)

One rank-based copula estimator (SPRING) beats both Pearson-based and compositional neighbourhood selection in its authors' simulations and loses to compositional methods only in the distorted low-sample scale-free case.

- conf: not stated
- class: model (critic: C-009)
- holds: the SPRING authors' simulations
- src: yoonMicrobialNetworksSPRING2019
- trail: C-RANKNET §critic, §Verdict the body

From the note:

> C-RANKNET:C-008 [danger: Critic: verdict partly supported] But the review's stated reason for discounting the one pro-rank result does not survive checking: in Yoon et al.'s own Table 2/Table 3, MB (sample Pearson correlation, absolute abundance, no transform) shares SPRING's input type and scores 0.42/0.32/0.26/0.20/0.25/0.01 AUPR against SPRING's 0.95/0.95/0.96/0.93/0.90/0.58, so that benchmark does separate the rank estimator from the absolute-abundance input, contrary to the review's "no published study separates them".
>
> C-RANKNET:C-009 [danger: Critic: verdict partly supported] Part B should read: measured in silico; plain rank correlation no better or worse than magnitude correlation; one rank-based copula estimator beats both Pearson-based and compositional neighbourhood selection in its authors' simulations and loses to compositional methods only in the distorted low-sample scale-free case; nothing measured against experimentally validated interactions; reciprocal-rank neighbourhoods and rank trajectories never applied to this data type.
>
> C-RANKNET:A-048 [Verdict the body actually supports] Part B should read: measured in silico; plain rank correlation no better or worse than magnitude correlation; one rank-based copula estimator beats both Pearson-based and compositional neighbourhood selection in its authors' simulations and loses to compositional methods only in the distorted low-sample scale-free case; nothing measured against experimentally validated interactions; reciprocal-rank neighbourhoods and rank trajectories never applied to this data type.
>

## verdict-b.3 (claim)

Nothing on microbial abundance data has been measured against experimentally validated interactions: all of the evidence is modelled, on in silico tables whose truth is a generated matrix, and the lack of experimentally validated gold standards is stated as the field's core obstacle (Ghaeli et al.), while the absence of a DREAM-style challenge rests on Faust 2021 alone, asserted in a review, not an established field fact.

- conf: not stated
- class: model (critic: C-009)
- holds: microbial abundance data
- src: ghaeliEvaluatingMicrobialNetwork2026, faustOpenChallengesMicrobial2021
- trail: C-RANKNET §critic, §Verdicts, §Single-source claims, §The rank device in microbial

From the note:

> C-RANKNET:C-009 [danger: Critic: verdict partly supported] Part B should read: measured in silico; plain rank correlation no better or worse than magnitude correlation; one rank-based copula estimator beats both Pearson-based and compositional neighbourhood selection in its authors' simulations and loses to compositional methods only in the distorted low-sample scale-free case; nothing measured against experimentally validated interactions; reciprocal-rank neighbourhoods and rank trajectories never applied to this data type.
>
> C-RANKNET:A-013 [Verdicts] Two qualifications bound this verdict.
>
> C-RANKNET:A-014 [Verdicts] All of the evidence is modelled, on in silico tables whose truth is a generated matrix; the field states that no experimentally validated gold standard and no DREAM-style challenge exists [19,20], so nothing here has been measured against real interactions.
>
> C-RANKNET:C-027 [Single-source claims (6)] - 'No DREAM-style challenge exists for microbial network inference' rests on Faust 2021 alone and is asserted in a review, correctly labelled SECONDARY once but then used in the Part B verdict as an established field fact.
>
> C-RANKNET:B-0100 [The rank device in microbial abundance data] That paper opens by stating the field's core obstacle: "the lack of experimentally validated gold standards presents a significant obstacle in evaluating the biological accuracy of inferred networks" [19].
>
> C-RANKNET:B-0112 [The rank device in microbial abundance data] The same review explains why a truth-based comparison on real data is unavailable: no DREAM-style challenge exists for microbial network inference, and "interactions observed previously in nature cannot be used to determine the accuracy of network inference tools but only their sensitivity" [20].
>

## dns.2 (do not say)

"On function-prediction accuracy against GO, the record is a wash pointing slightly against ranking."

- why: The tally pools rank-of-coefficient and rank-of-value devices and four incommensurable criteria (neighbour-voting AUROC against GO, a composite PC1 quality score including promoter motif enrichment, GO enrichment p-value rankings, and counts of positive transcription factors in top clusters), and the Liesecke number in it belongs to a different analysis level.
- instead: verdict-a.2, expression-benchmarks.2
- trail: C-RANKNET §Verdicts, §Scope drift, §Expectation echo

From the note:

> C-RANKNET:A-005 [Verdicts] On function-prediction accuracy against GO, the record is a wash pointing slightly against ranking: one study finds rank better across four species [1], one finds raw better by 0.58 against 0.57 [4], one finds Pearson better by an average 0.011 in quality except below 30 samples [8], and one finds Spearman, Pearson and bicor indistinguishable [9].
>
> C-RANKNET:C-084 [Scope drift (7)] - The Part A verdict pools rank-of-coefficient constructions (mutual rank, HRR) with rank-of-value measures (Spearman, Kendall) into one direction tally, although the review's own opening paragraph identifies them as different devices used by different communities, and Obayashi's full text (read by the reviewer) contains the internal control showing Spearman value behaves like Pearson value while PCC rank does not. This is the rule 5 problem applied to directions rather than numbers.
>
> C-RANKNET:C-085 [Scope drift (7)] - The same verdict pools four incommensurable criteria as though they answered one question: neighbour-voting AUROC against GO, a composite PC1 quality score including promoter motif enrichment, GO enrichment p-value rankings, and counts of positive transcription factors in top clusters.
>
> C-RANKNET:C-096 [Expectation echo] For Part A the echo is stronger: the only unambiguous pro-rank accuracy result in the corpus (Obayashi and Kinoshita, four species, all three GO branches, all four summarisation methods) is correctly labelled SINGLE SOURCE and then outweighed by a number that belongs to a different analysis level (Liesecke's pathway-level 0.58 versus 0.57), a composite score misdescribed as GO accuracy (Vandenbon), and a null (Song).
>

## dns.3 (do not say)

"In Liesecke and colleagues' genome-wide benchmark, ranking loses slightly on GO accuracy: the raw coefficients scored 0.58 against 0.57."

- why: The 0.58 against 0.57 AUROC (with the 0.35/0.68 modularity and 0.20/0.35 chi-squared pairs) comes from the Pathway Level Correlation subnetworks averaged over five pathways in the RNA-seq normalisation comparison, not from the genome-wide benchmark, whose conclusion is that HRR performs similarly to classical measures: a null, not a loss.
- instead: expression-benchmarks.6, expression-benchmarks.8
- trail: C-RANKNET §Head to head, §Verdict assessment, §Reference errors

From the note:

> C-RANKNET:B-0042 [Head to head: ranked against unranked in expression data] **Ranking loses slightly on the same criterion in the largest plant replication.** Liesecke and colleagues built global and pathway-level networks from 9,953 ATH1 microarrays and 1,676 RNA-seq samples under seven normalisations, with six measures including PCC, SCC, PCC-HRR, SCC-HRR, mutual information and partial correlation, scored against GO and against five curated pathways with known sub-pathway structure [4] (measured; unordered cross-sectional samples).
>
> C-RANKNET:B-0046 [Head to head: ranked against unranked in expression data] Their title is "Ranking genome-wide correlation measurements improves microarray and RNA-seq based global and targeted co-expression networks"; their own accuracy number goes the other way, and I read that number as the one that answers the accuracy question, while they read the structural gain as the headline.
>
> C-RANKNET:A-021 [Verdicts] The two claims I had to argue down against the initial findings were the Liesecke 2018 result (whose title asserts improvement while its own accuracy number does not) and the SPRING result (whose margin is confounded with absolute-abundance input by the paper's own Table 2).
>
> C-RANKNET:A-032 [Verdict assessment] Second, the Liesecke 2018 numbers.
>
> C-RANKNET:A-033 [Verdict assessment] The review presents "0.58 against 0.57" as the study's neighbour-voting AUROC against GO, one of four data points in the Part A tally.
>
> C-RANKNET:A-035 [Verdict assessment] At the global level the same paper concludes that "HRR CCs are able to generate complete genome-wide networks with good performances similar to other classical measures such a MI and PC", which is a null, not a loss.
>
> C-RANKNET:A-036 [Verdict assessment] The review's framing ("Ranking loses slightly on the same criterion in the largest plant replication") over-reads a pathway-level trade-off into a global accuracy verdict.
>
> C-RANKNET:C-037 [Reference errors (7)] - Ref 4 (Liesecke et al. 2018): the figures 0.58 versus 0.57 NV AUROC, 0.35 versus 0.68 modularity and 0.20 versus 0.35 normalised chi-squared are pathway-level (PLC) subnetwork results averaged over five pathways in the RNA-seq normalisation comparison.
>
> C-RANKNET:C-038 [Reference errors (7)] The review presents the AUROC pair as the study's global GO benchmark.
>
> C-RANKNET:C-039 [Reference errors (7)] The paper's global-level conclusion is the opposite in tone: 'HRR CCs are able to generate complete genome-wide networks with good performances similar to other classical measures such a MI and PC'.
>

Not found in the cited text (where to look, not what is wrong): "In Liesecke and colleagues' genome-wide benchmark, ranking loses slightly on GO accuracy: the raw coefficients scored 0.58 against 0.57."

## dns.4 (do not say)

"Vandenbon found Spearman 0.011 lower than Pearson in function-prediction accuracy against GO."

- why: Vandenbon's Quality is the first principal component of quality measures based on enrichment of functional annotations and of regulatory motifs in promoters, so listing it alongside neighbour-voting AUROC as the same criterion pools incommensurable metrics.
- instead: expression-benchmarks.17
- trail: C-RANKNET §Reference errors, §Head to head, §Verdicts

From the note:

> C-RANKNET:C-043 [Reference errors (7)] - Ref 8 (Vandenbon 2022): 'Quality' is described in the Part A verdict as function-prediction accuracy against GO.
>
> C-RANKNET:C-044 [Reference errors (7)] It is the first principal component of quality measures based on enrichment of functional annotations *and* of regulatory motifs in promoters.
>
> C-RANKNET:C-045 [Reference errors (7)] Listing it alongside neighbour-voting AUROC as the same criterion pools incommensurable metrics.
>
> C-RANKNET:B-0059 [Head to head: ranked against unranked in expression data] "Using Spearman's correlation instead of Pearson correlation resulted on average in a 0.011 decrease in Quality (equivalent to a 8.2% decrease in sample count).
>
> C-RANKNET:A-005 [Verdicts] On function-prediction accuracy against GO, the record is a wash pointing slightly against ranking: one study finds rank better across four species [1], one finds raw better by 0.58 against 0.57 [4], one finds Pearson better by an average 0.011 in quality except below 30 samples [8], and one finds Spearman, Pearson and bicor indistinguishable [9].
>

Not found in the cited text (where to look, not what is wrong): "Vandenbon found Spearman 0.011 lower than Pearson in function-prediction accuracy against GO."

