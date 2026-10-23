## compositional-closure.2 (claim)

Friedman and Alm state that compositional methods "for inferring more general dependencies between components, equivalent to rank correlations and mutual information for non-compositional data, have not yet been developed", a gap that remained open when SPRING was introduced seven years later.

- conf: not stated
- class: not stated
- holds: compositional microbial data
- src: friedmanInferringCorrelationNetworks2012, yoonMicrobialNetworksSPRING2019
- trail: C-RANKNET §The rank device in microbial

From the note:

> C-RANKNET:B-0107 [The rank device in microbial abundance data] They also state that compositional methods "for inferring more general dependencies between components, equivalent to rank correlations and mutual information for non-compositional data, have not yet been developed" [15], a gap that remained open when SPRING was introduced seven years later.
>

## spring.1 (claim)

SPRING (Semi-Parametric Rank-based INference in Graphical models) estimates a latent correlation from Kendall's tau through a closed-form bridge function for a truncated Gaussian copula, with an estimated zero truncation threshold, so exact zeros are modelled rather than replaced by pseudocounts, then runs Meinshausen-Buhlmann neighbourhood selection with StARS.

- conf: not stated
- class: not stated
- holds: microbiome count data
- src: yoonMicrobialNetworksSPRING2019
- trail: C-RANKNET §The rank device in microbial, §Glossary

From the note:

> C-RANKNET:B-0081 [The rank device in microbial abundance data] **A copula estimator built on Kendall's tau.** SPRING estimates a latent correlation from Kendall's tau through a closed-form bridge function for a truncated Gaussian copula, so exact zeros are modelled rather than replaced by pseudocounts, then runs Meinshausen-Buhlmann neighbourhood selection with StARS [12].
>
> C-RANKNET:B-0190 [Glossary: what each field calls the rank device] **SPRING (Semi-Parametric Rank-based INference in Graphical models)**: microbiome: latent Gaussian copula correlation recovered from Kendall's tau with an estimated zero truncation threshold, then neighbourhood selection with StARS.
>

## spring.2 (claim)

For relative-abundance input SPRING first applies a modified clr (mclr) transform, pseudocount-free, that is "invariant to the addition of extra zero components, preserves the original zero measurements, and is overall rank-preserving".

- conf: not stated
- class: not stated
- holds: relative-abundance input
- src: yoonMicrobialNetworksSPRING2019
- trail: C-RANKNET §The rank device in microbial, §Glossary

From the note:

> C-RANKNET:B-0082 [The rank device in microbial abundance data] For relative-abundance input it first applies a modified clr transform that is "invariant to the addition of extra zero components, preserves the original zero measurements, and is overall rank-preserving" [12].
>
> C-RANKNET:B-0191 [Glossary: what each field calls the rank device] **mclr (modified centred log-ratio)**: the pseudocount-free, rank-preserving transform that lets SPRING run on relative abundances; explicitly not compositionally aware.
>

## spring.3 (claim)

SPRING is rank-based but not compositionally aware when run on relative abundances, by its authors' own statement that the mclr transform "does not take into the account the compositional nature of the data".

- conf: not stated
- class: not stated
- holds: relative-abundance input
- src: yoonMicrobialNetworksSPRING2019
- trail: C-RANKNET §The rank device in microbial, §What sequencing count, §Search record

From the note:

> C-RANKNET:B-0083 [The rank device in microbial abundance data] The authors state explicitly that this transform "does not take into the account the compositional nature of the data" [12], which matters for how SPRING should be classed.
>
> C-RANKNET:B-0118 [What sequencing count properties do to rank methods] SPRING is rank-based but is not compositionally aware when run on relative abundances, by its authors' own statement [12].
>
> C-RANKNET:B-0219 [Search record (synthesis agent)] I also verified the paper's statement that mclr "does not take into the account the compositional nature of the data".
>

Not found in the cited text (where to look, not what is wrong): holds: relative-abundance

## spring.4 (claim)

Yoon, Gaynanova and Müller report SPRING with the highest AUPR of four methods on synthetic quantitative microbiome counts: 0.95 against 0.91 for SPIEC-EASI on a band graph at n equal to 2000 and p equal to 100, 0.95 against 0.93 on a cluster graph, 0.96 against 0.93 on scale-free, and at n equal to 500 with p equal to 200, 0.93/0.89, 0.90/0.83 and 0.58/0.55, with Pearson-based neighbourhood selection far behind throughout (0.42, 0.32, 0.26, 0.20, 0.25, 0.01).

- conf: not stated
- class: model (note: "every entry is a simulation")
- holds: synthetic quantitative microbiome counts; band, cluster and scale-free graphs; n 2000 with p 100, and n 500 with p 200; the authors' own simulations
- src: yoonMicrobialNetworksSPRING2019
- trail: C-RANKNET §The rank device in microbial

From the note:

> C-RANKNET:B-0085 [The rank device in microbial abundance data] The benchmark record for these is as follows, and every entry is a simulation.
>
> C-RANKNET:B-0087 [The rank device in microbial abundance data] Yoon, Gaynanova and Müller report SPRING with the highest AUPR of four methods on synthetic quantitative microbiome counts: 0.95 against 0.91 for SPIEC-EASI on a band graph at n equal to 2000 and p equal to 100, 0.95 against 0.93 on a cluster graph, 0.96 against 0.93 on scale-free, and at n equal to 500 with p equal to 200, 0.93/0.89, 0.90/0.83 and 0.58/0.55, with Pearson-based neighbourhood selection far behind throughout (0.42, 0.32, 0.26, 0.20, 0.25, 0.01) [12].
>

## spring.5 (claim)

SPRING's margin over SPIEC-EASI is small and it vanishes in the hardest regime.

- conf: not stated
- class: model (note: "every entry is a simulation")
- holds: the authors' simulations
- src: yoonMicrobialNetworksSPRING2019
- trail: C-RANKNET §The rank device in microbial

From the note:

> C-RANKNET:B-0085 [The rank device in microbial abundance data] The benchmark record for these is as follows, and every entry is a simulation.
>
> C-RANKNET:B-0088 [The rank device in microbial abundance data] Three bounds sit in the same paper.
>
> C-RANKNET:B-0089 [The rank device in microbial abundance data] First, the margin over SPIEC-EASI is small and it vanishes in the hardest regime.
>

## spring.6 (claim)

Under distortion of sample totals by a random factor in [0.5, 3], "SPRING is still best or among the best methods for band and cluster graph types, and is outperformed by the compositional methods for scale-free graph type in the low sample size regime", falling to AUPR 0.50 against 0.54 for both compositional methods.

- conf: not stated
- class: model (note: "every entry is a simulation")
- holds: the authors' simulations with distorted sample totals
- src: yoonMicrobialNetworksSPRING2019
- trail: C-RANKNET §The rank device in microbial

From the note:

> C-RANKNET:B-0085 [The rank device in microbial abundance data] The benchmark record for these is as follows, and every entry is a simulation.
>
> C-RANKNET:B-0090 [The rank device in microbial abundance data] Second, under distortion of sample totals by a random factor in [0.5, 3], "SPRING is still best or among the best methods for band and cluster graph types, and is outperformed by the compositional methods for scale-free graph type in the low sample size regime" [12], falling to AUPR 0.50 against 0.54 for both compositional methods.
>

## spring.7 (claim)

Table 2 of the SPRING paper shows an input asymmetry: SPRING runs on absolute abundance with no transform, while SPIEC-EASI and invSparCC run on relative abundance, with clr and log SparCC respectively.

- conf: not stated
- class: not stated
- holds: the SPRING benchmark
- src: yoonMicrobialNetworksSPRING2019
- trail: C-RANKNET §The rank device in microbial, §Search record

From the note:

> C-RANKNET:B-0091 [The rank device in microbial abundance data] Third, and least discussed, Table 2 of that paper shows the input asymmetry: SPRING runs on absolute abundance with no transform, while SPIEC-EASI and invSparCC run on relative abundance [12].
>
> C-RANKNET:B-0216 [Search record (synthesis agent)] (2) The SPRING benchmark's Table 2 states the input asymmetry explicitly: SPRING runs on absolute abundance with no transform, SPIEC-EASI and invSparCC on relative abundance with clr and log SparCC respectively.
>

## spring.8 (claim)

The SPRING authors' own conclusion is that "incorporating quantitative abundance information in the analysis leads to more reliable graphical model inference", which attributes the gain to the data type rather than to the rank estimator.

- conf: not stated
- class: not stated
- holds: the SPRING benchmark
- src: yoonMicrobialNetworksSPRING2019
- trail: C-RANKNET §The rank device in microbial, §Search record

From the note:

> C-RANKNET:B-0092 [The rank device in microbial abundance data] The authors' own conclusion is that "incorporating quantitative abundance information in the analysis leads to more reliable graphical model inference" [12], which attributes the gain to the data type rather than to the rank estimator.
>
> C-RANKNET:B-0217 [Search record (synthesis agent)] The authors' own discussion attributes the gain to quantitative abundance information.
>

Not found in the cited text (where to look, not what is wrong): SPRING; holds: spring

## spring.9 (claim)

The SPRING benchmark does separate the rank estimator from the absolute-abundance input: in Yoon et al.'s own Table 2/Table 3, MB (sample Pearson correlation, absolute abundance, no transform) shares SPRING's input type and scores 0.42/0.32/0.26/0.20/0.25/0.01 AUPR against SPRING's 0.95/0.95/0.96/0.93/0.90/0.58.

- conf: not stated
- class: model (critic: C-009)
- holds: the authors' simulations
- src: yoonMicrobialNetworksSPRING2019
- trail: C-RANKNET §critic, §Verdict assessment, §Scope drift

From the note:

> C-RANKNET:C-008 [danger: Critic: verdict partly supported] But the review's stated reason for discounting the one pro-rank result does not survive checking: in Yoon et al.'s own Table 2/Table 3, MB (sample Pearson correlation, absolute abundance, no transform) shares SPRING's input type and scores 0.42/0.32/0.26/0.20/0.25/0.01 AUPR against SPRING's 0.95/0.95/0.96/0.93/0.90/0.58, so that benchmark does separate the rank estimator from the absolute-abundance input, contrary to the review's "no published study separates them".
>
> C-RANKNET:C-009 [danger: Critic: verdict partly supported] Part B should read: measured in silico; plain rank correlation no better or worse than magnitude correlation; one rank-based copula estimator beats both Pearson-based and compositional neighbourhood selection in its authors' simulations and loses to compositional methods only in the distorted low-sample scale-free case; nothing measured against experimentally validated interactions; reciprocal-rank neighbourhoods and rank trajectories never applied to this data type.
>
> C-RANKNET:A-029 [Verdict assessment] The fourth method in that same table, MB, runs on absolute abundance with no transform and estimates sample Pearson correlation.
>
> C-RANKNET:A-030 [Verdict assessment] It is the control the review says does not exist, and it is far behind SPRING in every cell.
>
> C-RANKNET:A-047 [Verdict the body actually supports] But the review's stated reason for discounting the one pro-rank result does not survive checking: in Yoon et al.'s own Table 2/Table 3, MB (sample Pearson correlation, absolute abundance, no transform) shares SPRING's input type and scores 0.42/0.32/0.26/0.20/0.25/0.01 AUPR against SPRING's 0.95/0.95/0.96/0.93/0.90/0.58, so that benchmark does separate the rank estimator from the absolute-abundance input, contrary to the review's "no published study separates them".
>
> C-RANKNET:C-081 [Scope drift (7)] - 'My reading is that this benchmark does not separate rank-based wins from absolute abundance wins, and no published study separates them.' This is the reviewer's own argument carrying a verdict, it is an absence claim with no search routes named (Common rule 7), and it is contradicted by Table 2 and Table 3 of the very source cited: MB runs Pearson on absolute abundance with no transform and scores 0.42 to 0.01 AUPR against SPRING's 0.95 to 0.58.
>

## spring.10 (claim)

The SPRING paper's edge-overlap analysis recommends intersecting SPRING, SPIEC-EASI and invSparCC (joint true positive rate 0.95 over roughly 246 edges) rather than using the rank method alone.

- conf: not stated
- class: not stated
- holds: the SPRING benchmark
- src: yoonMicrobialNetworksSPRING2019
- trail: C-RANKNET §The rank device in microbial

From the note:

> C-RANKNET:B-0094 [The rank device in microbial abundance data] The same paper's edge-overlap analysis recommends intersecting SPRING, SPIEC-EASI and invSparCC (joint true positive rate 0.95 over roughly 246 edges) rather than using the rank method alone [12].
>

## spring.11 (claim)

Kishore and colleagues included SPRING among ten methods scored against two synthetic generators and report SpiecEasi as the best individual method (average precision 0.944 on NorTA data, 0.624 on seqtime data), with consensus schemes above it; SPRING is not named as a leader, but its own precision values sit in figures S5 and S6, which the review could not obtain, so the absence of its name is not a measured underperformance.

- conf: not stated
- class: model (note: "every entry is a simulation")
- holds: two synthetic generators (NorTA, seqtime), ten methods
- src: kishoreInferringMicrobialCooccurrence2023 (main text and figure legends; figures S5 and S6 not obtained)
- trail: C-RANKNET §The rank device in microbial, §Full-text breaches, §Sources not obtained
- limit: access and evidence (critic: C-020)

From the note:

> C-RANKNET:B-0085 [The rank device in microbial abundance data] The benchmark record for these is as follows, and every entry is a simulation.
>
> C-RANKNET:B-0096 [The rank device in microbial abundance data] Kishore and colleagues included SPRING among ten methods scored against two synthetic generators and report SpiecEasi as the best individual method (average precision 0.944 on NorTA data, 0.624 on seqtime data), with consensus schemes above it [18]; SPRING is not named as a leader.
>
> C-RANKNET:C-020 [Full-text breaches (4)] - Kishore et al. 2023 (ref 18): the claim that independent evaluation 'does not reproduce a SPRING advantage' is inferred from SPRING not being named in the text, while the per-method precision values for SPRING sit in figures S5 and S6 that the review says it could not obtain. Absence of a name in a legend is not a measured underperformance, yet the Part B verdict cites it as one of 'two independent evaluations'.
>
> C-RANKNET:R-0165 [Sources not obtained] **Kishore et al. 2023 figures S5 and S6 (DOI 10.1128/msystems.00961-22).** These hold the only published per-method precision and sensitivity values for SPRING on a common simulated benchmark.
>
> C-RANKNET:R-0166 [Sources not obtained] Europe PMC fullTextXML supplied the main text and the figure legends but not the figure data.
>
> C-RANKNET:R-0167 [Sources not obtained] Only the SpiecEasi headline numbers quoted inside the legends were used.
>

## spring.12 (claim)

Ghaeli, Aghdam and Eslahchi evaluated six algorithms on four real 16S datasets under bootstrap, noise and synthetic perturbation, scoring reproducibility (F-score and Jaccard similarity between networks inferred from the perturbed variants) in a paper whose premise is that no gold standard exists; SPRING appears in neither of their two top-performer tables, which are filled by SparCC, gCoda and SPIEC-EASI(glasso).

- conf: not stated
- class: not stated
- holds: four real 16S datasets; reproducibility, not truth; Tables 3 and 4 only, the supplementary tables not obtained
- src: ghaeliEvaluatingMicrobialNetwork2026 (main text only)
- trail: C-RANKNET §The rank device in microbial, §Reference errors, §Search record

From the note:

> C-RANKNET:B-0098 [The rank device in microbial abundance data] Ghaeli, Aghdam and Eslahchi evaluated six algorithms on four real 16S datasets under bootstrap, noise and synthetic perturbation; SPRING appears in neither of their two top-performer tables, which are filled by SparCC, gCoda and SPIEC-EASI(glasso) [19].
>
> C-RANKNET:B-0220 [Search record (synthesis agent)] (3) The Ghaeli et al. "general lack of discriminative power" is reported in identical terms for OIPCQ, gCoda, S-E(glasso) and S-E(mb) as well as SPRING, so it is a property of that benchmark rather than a property of the rank method; I verified that SPRING appears in neither of their top-performer tables, which is the defensible claim.
>
> C-RANKNET:C-047 [Reference errors (7)] - Ref 19 (Ghaeli et al. 2026): the metric is reproducibility, F-score and Jaccard similarity between networks inferred from bootstrap and noise-perturbed variants of real data, in a paper whose premise is that no gold standard exists. The review's Part B verdict uses SPRING's absence from Tables 3 and 4 as evidence about performance alongside truth-based simulation benchmarks.
>
> C-RANKNET:R-0168 [Sources not obtained] **Ghaeli et al. 2026 supplementary tables S7-S38 and figures S25-S65 (DOI 10.1186/s12859-026-06510-3).** These hold the per-algorithm F-score and Jaccard values for SPRING.
>
> C-RANKNET:R-0169 [Sources not obtained] Europe PMC fullTextXML supplied main text only.
>
> C-RANKNET:R-0170 [Sources not obtained] Only the narrative rankings and Tables 3 and 4 were used.
>

## spring.13 (claim)

Ghaeli and colleagues' reported limitation for SPRING, "a general lack of discriminative power, as multiple topologies yielded non-significant differences across all datasets", is reported in the same terms for OIPCQ, gCoda, S-E(glasso) and S-E(mb), so it is a property of the benchmark as much as of SPRING.

- conf: not stated
- class: not stated
- holds: Ghaeli et al.'s reproducibility benchmark on four real 16S datasets
- src: ghaeliEvaluatingMicrobialNetwork2026
- trail: C-RANKNET §The rank device in microbial, §Search record

From the note:

> C-RANKNET:B-0099 [The rank device in microbial abundance data] Their reported limitation for SPRING, "a general lack of discriminative power, as multiple topologies yielded non-significant differences across all datasets" [19], is reported in the same terms for OIPCQ, gCoda, S-E(glasso) and S-E(mb), so it is a property of the benchmark as much as of SPRING.
>
> C-RANKNET:B-0220 [Search record (synthesis agent)] (3) The Ghaeli et al. "general lack of discriminative power" is reported in identical terms for OIPCQ, gCoda, S-E(glasso) and S-E(mb) as well as SPRING, so it is a property of that benchmark rather than a property of the rank method; I verified that SPRING appears in neither of their top-performer tables, which is the defensible claim.
>

Not found in the cited text (where to look, not what is wrong): holds: 16s

## microbial-benchmarks.1 (claim)

The benchmark record for rank methods on microbial abundance data is all simulation: modelled throughout, on in silico count tables whose truth is a generated correlation or interaction matrix, not an experimentally verified interaction.

- conf: not stated
- class: model (note: "modelled throughout")
- holds: Spearman, Kendall, SPRING and eLSA benchmarks on microbial abundance data
- src: none (the reviewer's synthesis over the benchmarks)
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
> C-RANKNET:B-0085 [The rank device in microbial abundance data] The benchmark record for these is as follows, and every entry is a simulation.
>
> C-RANKNET:B-0086 [The rank device in microbial abundance data] Evidence class: modelled throughout, on in silico count tables whose truth is a generated correlation or interaction matrix, not an experimentally verified interaction.
>

## microbial-benchmarks.2 (claim)

Berry and Widder, on generalized Lotka-Volterra metacommunities with a known interaction network: "Pearson and Spearman coefficients had the highest sensitivity, followed by Kendall coefficient and Bray-Curtis dissimilarity, and then Jaccard index (p < 0.05 for all comparisons except Pearson vs. Spearman and Kendall vs. Bray-Curtis)"; Spearman and Pearson were statistically indistinguishable, and Kendall was measurably worse.

- conf: not stated
- class: model (note: "every entry is a simulation")
- holds: simulated generalized Lotka-Volterra metacommunities
- src: berryDecipheringMicrobialInteractions2014
- trail: C-RANKNET §The rank device in microbial

From the note:

> C-RANKNET:B-0085 [The rank device in microbial abundance data] The benchmark record for these is as follows, and every entry is a simulation.
>
> C-RANKNET:B-0102 [The rank device in microbial abundance data] - Berry and Widder, on generalized Lotka-Volterra metacommunities with a known interaction network: "Pearson and Spearman coefficients had the highest sensitivity, followed by Kendall coefficient and Bray-Curtis dissimilarity, and then Jaccard index (p < 0.05 for all comparisons except Pearson vs. Spearman and Kendall vs. Bray-Curtis)" [16].
>
> C-RANKNET:B-0103 [The rank device in microbial abundance data] Spearman and Pearson were statistically indistinguishable; Kendall was measurably worse.
>

Not found in the cited text (where to look, not what is wrong): holds: simulated

## microbial-benchmarks.3 (claim)

Hirano and Takemoto, on relative abundances generated by gLV dynamics: "The performance of Spearman's correlation-based and MIC-based methods was almost equal to or higher than those of compositional-data methods because they can consider nonlinear associations", but "Pearson's correlation-based method also exhibited a similar or higher performance than that of the compositional-data methods".

- conf: not stated
- class: model (note: "every entry is a simulation")
- holds: relative abundances generated by gLV dynamics
- src: hiranoDifficultyInferringMicrobial2019
- trail: C-RANKNET §The rank device in microbial

From the note:

> C-RANKNET:B-0085 [The rank device in microbial abundance data] The benchmark record for these is as follows, and every entry is a simulation.
>
> C-RANKNET:B-0104 [The rank device in microbial abundance data] - Hirano and Takemoto, on relative abundances generated by gLV dynamics: "The performance of Spearman's correlation-based and MIC-based methods was almost equal to or higher than those of compositional-data methods because they can consider nonlinear associations", but "Pearson's correlation-based method also exhibited a similar or higher performance than that of the compositional-data methods" [14].
>

## microbial-benchmarks.4 (claim)

In Hirano and Takemoto's benchmark the best AUPR across all methods was at most about 0.65 at n equal to 50 species and mean degree 2, falling to about 0.45 at mean degree 8.

- conf: not stated
- class: model (note: "every entry is a simulation")
- holds: gLV-generated relative abundances, 50 species
- src: hiranoDifficultyInferringMicrobial2019
- trail: C-RANKNET §The rank device in microbial

From the note:

> C-RANKNET:B-0085 [The rank device in microbial abundance data] The benchmark record for these is as follows, and every entry is a simulation.
>
> C-RANKNET:B-0104 [The rank device in microbial abundance data] - Hirano and Takemoto, on relative abundances generated by gLV dynamics: "The performance of Spearman's correlation-based and MIC-based methods was almost equal to or higher than those of compositional-data methods because they can consider nonlinear associations", but "Pearson's correlation-based method also exhibited a similar or higher performance than that of the compositional-data methods" [14].
>
> C-RANKNET:B-0105 [The rank device in microbial abundance data] Best AUPR across all methods was at most about 0.65 at n equal to 50 species and mean degree 2, falling to about 0.45 at mean degree 8.
>

## microbial-benchmarks.5 (claim)

Friedman and Alm, the paper that introduced SparCC: "these compositional effects are not limited to Pearson correlation, and are also present in non-parametric correlations, such as Spearman correlations", and "Spearman correlations performed only marginally better".

- conf: not stated
- class: model (note: "every entry is a simulation")
- holds: simulated compositional data
- src: friedmanInferringCorrelationNetworks2012
- trail: C-RANKNET §The rank device in microbial

From the note:

> C-RANKNET:B-0085 [The rank device in microbial abundance data] The benchmark record for these is as follows, and every entry is a simulation.
>
> C-RANKNET:B-0106 [The rank device in microbial abundance data] - Friedman and Alm, the paper that introduced SparCC: "these compositional effects are not limited to Pearson correlation, and are also present in non-parametric correlations, such as Spearman correlations", and "Spearman correlations performed only marginally better" [15].
>

Not found in the cited text (where to look, not what is wrong): holds: simulated

## microbial-benchmarks.6 (claim)

Weiss and colleagues, the field's largest correlation benchmark: "Rank-based measures such as MIC and Spearman, as well as Bray-Curtis, are less affected by compositional data but still not immune".

- conf: not stated
- class: model (note: "91 simulated OTU tables")
- holds: eight tools, 91 simulated OTU tables, 200 to 10,000 features, eight generative models
- src: weissCorrelationDetectionStrategies2016 (main text only)
- trail: C-RANKNET §The rank device in microbial

From the note:

> C-RANKNET:B-0108 [The rank device in microbial abundance data] - Weiss and colleagues, the field's largest correlation benchmark (eight tools, 91 simulated OTU tables, 200 to 10,000 features, eight generative models): "Rank-based measures such as MIC and Spearman, as well as Bray-Curtis, are less affected by compositional data but still not immune" [13].
>
> C-RANKNET:R-0052 [References] DOI: 10.1038/ismej.2015.235 (read as the author accepted manuscript, eScholarship qt3ps0c507; main text only)
>

## microbial-benchmarks.7 (claim)

In Weiss and colleagues' benchmark Spearman was one of only three tools (with SparCC and LSA) that "correctly identify competitive relationships as mutual exclusions".

- conf: not stated
- class: model (note: "91 simulated OTU tables")
- holds: 91 simulated OTU tables
- src: weissCorrelationDetectionStrategies2016
- trail: C-RANKNET §The rank device in microbial

From the note:

> C-RANKNET:B-0108 [The rank device in microbial abundance data] - Weiss and colleagues, the field's largest correlation benchmark (eight tools, 91 simulated OTU tables, 200 to 10,000 features, eight generative models): "Rank-based measures such as MIC and Spearman, as well as Bray-Curtis, are less affected by compositional data but still not immune" [13].
>
> C-RANKNET:B-0109 [The rank device in microbial abundance data] Spearman was one of only three tools (with SparCC and LSA) that "correctly identify competitive relationships as mutual exclusions" [13].
>

## microbial-benchmarks.8 (claim)

Kishore and colleagues excluded Pearson and Spearman from all quantitative comparison a priori because "they tend to generate a large number of spurious edges as they are not intended for compositional data sets", which is an assumption rather than a measurement in that paper.

- conf: not stated
- class: not stated
- holds: Kishore et al. 2023
- src: kishoreInferringMicrobialCooccurrence2023
- trail: C-RANKNET §The rank device in microbial

From the note:

> C-RANKNET:B-0097 [The rank device in microbial abundance data] That study also excluded Pearson and Spearman from all quantitative comparison a priori because "they tend to generate a large number of spurious edges as they are not intended for compositional data sets" [18], which is an assumption rather than a measurement in that paper.
>

Not found in the cited text (where to look, not what is wrong): holds: kishore; holds: 2023

## microbial-benchmarks.9 (claim)

Faust's review reads the record the same way: "Interestingly, in both evaluations, classical correlation measures such as Pearson and Spearman performed often as well as more sophisticated new network inference algorithms".

- conf: not stated
- class: assert (note: "asserted")
- holds: the evaluations by Weiss 2016 and Hirano and Takemoto 2019
- src: faustOpenChallengesMicrobial2021 (SECONDARY to Weiss 2016 and Hirano and Takemoto 2019)
- trail: C-RANKNET §The rank device in microbial

From the note:

> C-RANKNET:B-0110 [The rank device in microbial abundance data] Two review-level statements from the microbial network community read this record the same way.
>
> C-RANKNET:B-0111 [The rank device in microbial abundance data] Faust: "Interestingly, in both evaluations, classical correlation measures such as Pearson and Spearman performed often as well as more sophisticated new network inference algorithms" [20] (asserted; SECONDARY to Weiss 2016 and Hirano and Takemoto 2019).
>

## microbial-modules.1 (claim)

MNetClass builds a Spearman network, partitions it with Walktrap and scores subnetworks with a rank-sum-ratio and entropy-weight model; against six other community detection algorithms on 50 FABIA-simulated matrices with true cluster labels it was significantly better on sensitivity and accuracy and not different from manta or WGCNA on positive predictive value.

- conf: not stated
- class: model (note: "50 FABIA-simulated matrices with true cluster labels")
- holds: 50 FABIA-simulated matrices with true cluster labels
- src: wangMNetClassControlfreeMicrobial2025
- trail: C-RANKNET §The rank device in microbial

From the note:

> C-RANKNET:B-0113 [The rank device in microbial abundance data] Module detection on a rank-correlation microbial network has been benchmarked against simulated cluster labels, but with construction held fixed.
>
> C-RANKNET:B-0114 [The rank device in microbial abundance data] MNetClass builds a Spearman network, partitions it with Walktrap and scores subnetworks with a rank-sum-ratio and entropy-weight model; against six other community detection algorithms on 50 FABIA-simulated matrices with true cluster labels it was significantly better on sensitivity and accuracy and not different from manta or WGCNA on positive predictive value [24].
>

## microbial-modules.2 (claim)

In the MNetClass benchmark, edge betweenness, label propagation, leading eigenvector, fast greedy, Louvain and manta used MNetClass's network, while WGCNA was run with "default parameters to automatically construct the network", its own Pearson-based construction; WGCNA is also one of the two comparators MNetClass could not beat on PPV, which makes that comparison partly a rank-versus-magnitude construction comparison.

- conf: not stated
- class: not stated
- holds: the MNetClass benchmark on simulated matrices
- src: wangMNetClassControlfreeMicrobial2025
- trail: C-RANKNET §Reference errors

From the note:

> C-RANKNET:C-040 [Reference errors (7)] - Ref 24 (MNetClass): 'Every comparator used the same Spearman network' is not what the paper says.
>
> C-RANKNET:C-041 [Reference errors (7)] Edge betweenness, label propagation, leading eigenvector, fast greedy, Louvain and manta used MNetClass's network; WGCNA was run with 'default parameters to automatically construct the network', that is, its own Pearson-based construction.
>
> C-RANKNET:C-042 [Reference errors (7)] WGCNA is also one of the two comparators MNetClass could not beat on PPV, which makes that comparison partly a rank-versus-magnitude construction comparison, the opposite of the review's dismissal.
>

Not found in the cited text (where to look, not what is wrong): holds: simulated

## zero-ties.1 (claim)

Connor, Barberán and Clauset, working on a soil 16S matrix in which "abundance values of zero comprise fully 85% of the matrix", state that "both matrix sparsity and a heavy-tailed distribution of abundances will induce a very large number of multi-way ties, which will then have identical ranks", that the result is an inflated pairwise correlation score under Spearman, and that standard implementations of Spearman's in Matlab, R and Python all rely on the user to correct for ties.

- conf: single (critic: C-021)
- class: meas (note: "measured on real data, no truth set")
- holds: one soil 16S matrix, 85 percent zeros, no truth set
- src: connorUsingNullModels2017
- trail: C-RANKNET §What sequencing count, §Single-source claims

From the note:

> C-RANKNET:B-0120 [What sequencing count properties do to rank methods] Connor, Barberán and Clauset, working on a soil 16S matrix in which "abundance values of zero comprise fully 85% of the matrix", state that "both matrix sparsity and a heavy-tailed distribution of abundances will induce a very large number of multi-way ties, which will then have identical ranks.
>
> C-RANKNET:B-0121 [What sequencing count properties do to rank methods] The result is an inflated pairwise correlation score under Spearman.
>
> C-RANKNET:B-0122 [What sequencing count properties do to rank methods] (Standard implementations of Spearman's in Matlab, R, and Python all rely on the user to correct for ties in the data.
>
> C-RANKNET:B-0123 [What sequencing count properties do to rank methods] [17] (measured on real data, no truth set).
>
> C-RANKNET:C-021 [Single-source claims (6)] - Zeros, ties and inflated Spearman: the entire mechanism rests on Connor, Barberan and Clauset 2017, one soil 16S matrix with no truth set, yet the review calls it 'the sharpest mechanical result in the whole literature' and treats it as a property of sequencing count data generally. No SINGLE SOURCE label is applied.
>

## zero-ties.2 (claim)

Connor and colleagues' fix is Monte Carlo tie-breaking with real-valued noise that preserves the original partial ordering, followed by a permutation null; without it the null distribution of rho is disjoint rather than smooth.

- conf: not stated
- class: not stated
- holds: the soil 16S matrix
- src: connorUsingNullModels2017
- trail: C-RANKNET §What sequencing count, §Glossary

From the note:

> C-RANKNET:B-0120 [What sequencing count properties do to rank methods] Connor, Barberán and Clauset, working on a soil 16S matrix in which "abundance values of zero comprise fully 85% of the matrix", state that "both matrix sparsity and a heavy-tailed distribution of abundances will induce a very large number of multi-way ties, which will then have identical ranks.
>
> C-RANKNET:B-0124 [What sequencing count properties do to rank methods] Their fix is Monte Carlo tie-breaking with real-valued noise that preserves the original partial ordering, followed by a permutation null; without it the null distribution of rho is disjoint rather than smooth [17].
>
> C-RANKNET:B-0192 [Glossary: what each field calls the rank device] **Tie-broken (jittered) Spearman with a permutation null**: microbiome: Monte Carlo real-valued noise preserving the original partial ordering, added to break zero-induced rank ties before correlating.
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

Not found in the cited text (where to look, not what is wrong): holds: co-occurrence

## zero-ties.4 (claim)

SPRING's copula approach attacks the zero-tie problem differently, by estimating a zero truncation threshold from the observed zero count.

- conf: not stated
- class: not stated
- holds: SPRING
- src: yoonMicrobialNetworksSPRING2019
- trail: C-RANKNET §What sequencing count

From the note:

> C-RANKNET:B-0126 [What sequencing count properties do to rank methods] SPRING's copula approach attacks the same problem differently, by estimating a zero truncation threshold from the observed zero count [12].
>

## elsa.1 (claim)

eLSA (extended Local Similarity Analysis) normalises each series by a normal score transformation of the rank vector before local and time-lagged similarity scoring, and requires ordered samples because it scores local and time-delayed subinterval associations.

- conf: single (critic: C-028)
- class: not stated
- holds: microbial community and other time series with replicates, ordered samples; the critic: rests on the eLSA paper itself
- src: xiaExtendedLocalSimilarity2011
- trail: C-RANKNET §The rank device in microbial, §Data requirements, §Single-source claims

From the note:

> C-RANKNET:B-0084 [The rank device in microbial abundance data] **A rank-vector normal transform inside a time-series method.** eLSA normalises each series by a normal score transformation before local and time-lagged similarity scoring [22], and is the one widely used microbiome association method that requires ordered samples.
>
> C-RANKNET:B-0140 [Data requirements: ordered samples or not] The exception is eLSA, which requires ordered samples because it scores local and time-delayed subinterval associations after a normal score transform of each series [22].
>
> C-RANKNET:B-0193 [Glossary: what each field calls the rank device] **eLSA / LSA (extended Local Similarity Analysis)**: microbiome: rank-vector normal-score transform followed by local and time-lagged similarity scoring; the one common microbiome association method requiring ordered samples.
>
> C-RANKNET:C-028 [Single-source claims (6)] - eLSA described as 'the one widely used microbiome association method that requires ordered samples' rests on the eLSA paper itself; no source is cited for the exclusivity claim, and time-series microbiome methods such as MetaMIS, LIMITS, TIME and Granger-style inference are not considered.
>
> C-RANKNET:R-0085 [References] Extended local similarity analysis (eLSA) of microbial community and other time series data with replicates.
>

## sparsity.1 (claim)

In Weiss and colleagues' benchmark raising sparsity from about 40 to about 70 percent zeros "drastically reduces tool performance to little better than random guessing", "precision of the tools is also extremely poor (close to or at zero) under realistic conditions", and among rank-based options only "LSA, and at a few times, MIC and Spearman rise above the 45-degree line; however, not far above the line": no method survives sparsity.

- conf: not stated
- class: model (note: "91 simulated OTU tables")
- holds: 91 simulated OTU tables
- src: weissCorrelationDetectionStrategies2016
- trail: C-RANKNET §What sequencing count

From the note:

> C-RANKNET:B-0108 [The rank device in microbial abundance data] - Weiss and colleagues, the field's largest correlation benchmark (eight tools, 91 simulated OTU tables, 200 to 10,000 features, eight generative models): "Rank-based measures such as MIC and Spearman, as well as Bray-Curtis, are less affected by compositional data but still not immune" [13].
>
> C-RANKNET:B-0127 [What sequencing count properties do to rank methods] **Sparsity overall.** No method survives it.
>
> C-RANKNET:B-0128 [What sequencing count properties do to rank methods] Weiss and colleagues report that raising sparsity from about 40 to about 70 percent zeros "drastically reduces tool performance to little better than random guessing", that "precision of the tools is also extremely poor (close to or at zero) under realistic conditions", and that among rank-based options only "LSA, and at a few times, MIC and Spearman rise above the 45-degree line; however, not far above the line" [13].
>

## sparsity.2 (claim)

In Weiss and colleagues' benchmark the true-to-false-positive ratio "decreases markedly at ~50% OTU sparsity", which is the basis of their recommendation to delete features above that threshold.

- conf: not stated
- class: model (note: "91 simulated OTU tables")
- holds: 91 simulated OTU tables
- src: weissCorrelationDetectionStrategies2016
- trail: C-RANKNET §What sequencing count

From the note:

> C-RANKNET:B-0108 [The rank device in microbial abundance data] - Weiss and colleagues, the field's largest correlation benchmark (eight tools, 91 simulated OTU tables, 200 to 10,000 features, eight generative models): "Rank-based measures such as MIC and Spearman, as well as Bray-Curtis, are less affected by compositional data but still not immune" [13].
>
> C-RANKNET:B-0129 [What sequencing count properties do to rank methods] The true-to-false-positive ratio "decreases markedly at ~50% OTU sparsity", which is the basis of their recommendation to delete features above that threshold [13].
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

## sequencing-depth.1 (claim)

Uneven sequencing depth is directly addressed only as a normalisation question: Weiss and colleagues tested rarefying, cumulative-sum scaling and DESeq variance stabilisation.

- conf: not stated
- class: not stated
- holds: Weiss et al.'s simulated OTU tables; per-tool numbers in the unobtained supplement
- src: weissCorrelationDetectionStrategies2016
- trail: C-RANKNET §What sequencing count, §Sources not obtained

From the note:

> C-RANKNET:B-0108 [The rank device in microbial abundance data] - Weiss and colleagues, the field's largest correlation benchmark (eight tools, 91 simulated OTU tables, 200 to 10,000 features, eight generative models): "Rank-based measures such as MIC and Spearman, as well as Bray-Curtis, are less affected by compositional data but still not immune" [13].
>
> C-RANKNET:B-0131 [What sequencing count properties do to rank methods] **Uneven sequencing depth.** Directly addressed only as a normalisation question.
>
> C-RANKNET:B-0132 [What sequencing count properties do to rank methods] Weiss and colleagues tested rarefying, cumulative-sum scaling and DESeq variance stabilisation [13]; Vandenbon found normalisation and batch correction far more consequential than the choice of correlation measure [8], and that variance-stabilising and sample-scaling procedures in the plant work produced networks with average node degree 712 against 114 and average neighbour-voting AUROC 0.47 against 0.62 [4].
>
> C-RANKNET:R-0161 [Sources not obtained] **Weiss et al. 2016 supplementary note, supplementary figures 1-17 and supplementary tables 1-3 (DOI 10.1038/ismej.2015.235).** The per-tool precision, sensitivity and F1 numbers for Spearman, MIC and LSA against SparCC and CoNet live here.
>

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

Not found in the cited text (where to look, not what is wrong): holds: co-expression; holds: 2018

## sequencing-depth.3 (claim)

The review found no benchmark isolating depth variation as a factor in rank-versus-magnitude performance, and names no search routes for that statement.

- conf: not stated
- class: search (note: "I found no benchmark isolating depth variation")
- holds: rank-versus-magnitude benchmarks; no search routes named (the critic)
- src: none (the review's search)
- trail: C-RANKNET §What sequencing count, §Scope drift
- search: searched, not found (note: "I found no benchmark isolating depth variation")

From the note:

> C-RANKNET:B-0133 [What sequencing count properties do to rank methods] I found no benchmark isolating depth variation as a factor in rank-versus-magnitude performance.
>
> C-RANKNET:C-083 [Scope drift (7)] - 'I found no benchmark isolating depth variation as a factor in rank-versus-magnitude performance' is an absence claim with no routes named, in violation of Common rule 7, which the review otherwise honours carefully in its Gaps section.
>

## sample-size.1 (claim)

On the microbial side, Berry and Widder found specificity plateaus at about 25 sampling sites while sensitivity keeps rising to 100; the result does not separate rank from magnitude at low n.

- conf: not stated
- class: model (note: "every entry is a simulation")
- holds: simulated gLV metacommunities
- src: berryDecipheringMicrobialInteractions2014
- trail: C-RANKNET §What sequencing count

From the note:

> C-RANKNET:B-0085 [The rank device in microbial abundance data] The benchmark record for these is as follows, and every entry is a simulation.
>
> C-RANKNET:B-0102 [The rank device in microbial abundance data] - Berry and Widder, on generalized Lotka-Volterra metacommunities with a known interaction network: "Pearson and Spearman coefficients had the highest sensitivity, followed by Kendall coefficient and Bray-Curtis dissimilarity, and then Jaccard index (p < 0.05 for all comparisons except Pearson vs. Spearman and Kendall vs. Bray-Curtis)" [16].
>
> C-RANKNET:B-0135 [What sequencing count properties do to rank methods] On the microbial side, Berry and Widder found specificity plateaus at about 25 sampling sites while sensitivity keeps rising to 100 [16], and Hirano and Takemoto found performance roughly independent of sample number above 200 [14]; neither separates rank from magnitude at low n.
>

Not found in the cited text (where to look, not what is wrong): holds: simulated

## sample-size.2 (claim)

Hirano and Takemoto found performance roughly independent of sample number above 200; the result does not separate rank from magnitude at low n.

- conf: not stated
- class: model (note: "every entry is a simulation")
- holds: gLV-generated relative abundances
- src: hiranoDifficultyInferringMicrobial2019
- trail: C-RANKNET §What sequencing count

From the note:

> C-RANKNET:B-0085 [The rank device in microbial abundance data] The benchmark record for these is as follows, and every entry is a simulation.
>
> C-RANKNET:B-0104 [The rank device in microbial abundance data] - Hirano and Takemoto, on relative abundances generated by gLV dynamics: "The performance of Spearman's correlation-based and MIC-based methods was almost equal to or higher than those of compositional-data methods because they can consider nonlinear associations", but "Pearson's correlation-based method also exhibited a similar or higher performance than that of the compositional-data methods" [14].
>
> C-RANKNET:B-0135 [What sequencing count properties do to rank methods] On the microbial side, Berry and Widder found specificity plateaus at about 25 sampling sites while sensitivity keeps rising to 100 [16], and Hirano and Takemoto found performance roughly independent of sample number above 200 [14]; neither separates rank from magnitude at low n.
>

## sample-size.3 (claim)

Tool disagreement in the few-samples regime is severe: Weiss and colleagues report "an average of 31.5% shared edge inference for all pair-wise combinations of tools, and for all data sets/models tested".

- conf: not stated
- class: model (note: "91 simulated OTU tables")
- holds: Weiss et al.'s simulated OTU tables
- src: weissCorrelationDetectionStrategies2016
- trail: C-RANKNET §What sequencing count

From the note:

> C-RANKNET:B-0108 [The rank device in microbial abundance data] - Weiss and colleagues, the field's largest correlation benchmark (eight tools, 91 simulated OTU tables, 200 to 10,000 features, eight generative models): "Rank-based measures such as MIC and Spearman, as well as Bray-Curtis, are less affected by compositional data but still not immune" [13].
>
> C-RANKNET:B-0136 [What sequencing count properties do to rank methods] Tool disagreement in this regime is severe: Weiss and colleagues report "an average of 31.5% shared edge inference for all pair-wise combinations of tools, and for all data sets/models tested" [13].
>

## ordered-samples.1 (claim)

Every rank-based construction with a benchmark works on unordered cross-sectional samples: mutual rank, HRR, Spearman, Kendall and SPRING all take a feature-by-sample matrix with no ordering variable; eLSA is the exception.

- conf: not stated
- class: not stated
- holds: benchmarked rank-based constructions
- src: obayashiRankCorrelationCoefficient2009, mutwilAssemblyInteractiveCorrelation2010, lieseckeRankingGenomewideCorrelation2018, yoonMicrobialNetworksSPRING2019, peschelNetCoMiNetworkConstruction2021
- trail: C-RANKNET §Data requirements

From the note:

> C-RANKNET:B-0137 [Data requirements: ordered samples or not] Every rank-based construction with a benchmark works on unordered cross-sectional samples.
>
> C-RANKNET:B-0138 [Data requirements: ordered samples or not] Mutual rank, HRR, Spearman, Kendall and SPRING all take a feature-by-sample matrix with no ordering variable [1,3,4,12,21].
>
> C-RANKNET:B-0140 [Data requirements: ordered samples or not] The exception is eLSA, which requires ordered samples because it scores local and time-delayed subinterval associations after a normal score transform of each series [22].
>

## rank-trajectories.1 (claim)

The rank clock comes from urban demography, where Batty plotted each element's size rank on a radius per time step (a polar plot with rank increasing outward) and defined a rank shift distance and its average over a common set.

- conf: not stated
- class: meas (note: "measured; city size rankings, not biological")
- holds: city size rankings, not biological
- src: battyRankClocks2006 (†: read in full text by a search agent and not re-opened by the reviewer)
- trail: C-RANKNET §Rank through time, §Glossary

From the note:

> C-RANKNET:B-0020 [The review as returned] A note on notation: references marked † in the list were read in full text by a search agent and not re-opened by me.
>
> C-RANKNET:B-0142 [Rank through time in community ecology, and whether it groups taxa] The rank clock comes from urban demography, where Batty plotted each element's size rank on a radius per time step and defined a rank shift distance and its average over a common set [25†] (measured; city size rankings, not biological).
>
> C-RANKNET:B-0194 [Glossary: what each field calls the rank device] **Rank clock**: urban and complex systems, then community ecology: polar plot with one radius per time step and rank increasing outward.
>

## rank-trajectories.2 (claim)

Batty's statement about grouping is a suggestion: different rank trajectories "suggest a possible basis for future classification of city types based on their local dynamics"; no algorithm is given.

- conf: not stated
- class: assert (note: "asserted")
- holds: city size rankings
- src: battyRankClocks2006 (†)
- trail: C-RANKNET §Rank through time

From the note:

> C-RANKNET:B-0020 [The review as returned] A note on notation: references marked † in the list were read in full text by a search agent and not re-opened by me.
>
> C-RANKNET:B-0143 [Rank through time in community ecology, and whether it groups taxa] Batty's own statement about grouping is a suggestion and nothing more: different rank trajectories "suggest a possible basis for future classification of city types based on their local dynamics" [25†] (asserted).
>
> C-RANKNET:B-0144 [Rank through time in community ecology, and whether it groups taxa] No algorithm is given.
>

## rank-trajectories.3 (claim)

Collins and colleagues imported the rank clock into plant community ecology and defined mean rank shift (the mean absolute change in relative rank between consecutive years over species present in both) and proportional persistence; mean rank shift is unstandardised, so not comparable across communities of different richness.

- conf: not stated
- class: meas (note: "measured; three US LTER grassland and desert datasets")
- holds: three US LTER grassland and desert datasets
- src: collinsRankClocksPlant2008 (†: read in full text by a search agent and not re-opened by the reviewer)
- trail: C-RANKNET §Rank through time, §Glossary

From the note:

> C-RANKNET:B-0020 [The review as returned] A note on notation: references marked † in the list were read in full text by a search agent and not re-opened by me.
>
> C-RANKNET:B-0145 [Rank through time in community ecology, and whether it groups taxa] Collins and colleagues imported the device into plant community ecology and defined mean rank shift, the mean absolute change in relative rank between consecutive years over species present in both, and proportional persistence [26†] (measured; three US LTER grassland and desert datasets).
>
> C-RANKNET:B-0195 [Glossary: what each field calls the rank device] **Rank shift distance, mean rank shift (MRS)**: mean absolute rank change between consecutive times over elements present in both; unstandardised, so not comparable across communities of different richness.
>

## rank-trajectories.4 (claim)

Avolio and colleagues redefined the quantity as rank change, standardised by the pooled species number and bounded between 0 and 0.5, and supplied the same quantity as a rank difference between two replicates at a single time, so the comparison also works on unordered replicates; both are implemented in codyn.

- conf: not stated
- class: not stated
- holds: community ecology (codyn)
- src: avolioComprehensiveApproachAnalyzing2019 (†: read in full text by a search agent and not re-opened by the reviewer), hallettCodynRPackage2016 (†)
- trail: C-RANKNET §Rank through time, §Glossary

From the note:

> C-RANKNET:B-0020 [The review as returned] A note on notation: references marked † in the list were read in full text by a search agent and not re-opened by me.
>
> C-RANKNET:B-0146 [Rank through time in community ecology, and whether it groups taxa] Avolio and colleagues redefined the quantity as rank change, standardised by the pooled species number and bounded between 0 and 0.5, and supplied the same quantity as a rank difference between two replicates at a single time, so the comparison also works on unordered replicates [27†].
>
> C-RANKNET:B-0147 [Rank through time in community ecology, and whether it groups taxa] Both are implemented in codyn [28†].
>
> C-RANKNET:B-0196 [Glossary: what each field calls the rank device] **Rank change (delta R) and rank difference (R.D.)**: community ecology (codyn): mean absolute rank change divided by the pooled taxon number, bounded 0 to 0.5; the second is the same quantity between two replicates at one time.
>

## rank-trajectories.5 (claim)

Every one of the rank-through-time metrics is a single scalar per comparison describing the whole community; none produces a pairwise quantity between taxa.

- conf: not stated
- class: not stated
- holds: rank shift, mean rank shift, rank change and rank difference
- src: battyRankClocks2006, collinsRankClocksPlant2008, avolioComprehensiveApproachAnalyzing2019
- trail: C-RANKNET §Rank through time

From the note:

> C-RANKNET:B-0148 [Rank through time in community ecology, and whether it groups taxa] Every one of these is a single scalar per comparison describing the whole community.
>
> C-RANKNET:B-0149 [Rank through time in community ecology, and whether it groups taxa] None produces a pairwise quantity between taxa.
>

## rank-trajectories.6 (claim)

Everything in the rank-trajectory family requires ordered samples by definition.

- conf: not stated
- class: not stated
- holds: the rank-trajectory family
- src: none (the reviewer's statement)
- trail: C-RANKNET §Data requirements

From the note:

> C-RANKNET:B-0141 [Data requirements: ordered samples or not] Everything in the rank-trajectory family below requires ordered samples by definition.
>

## rank-trajectories.7 (claim)

Larsen and colleagues computed rank shift on vineyard soil 16S and ITS data only for taxa observed in both compared years, so the zero-inflated portion of the table is discarded before ranks are formed, reporting about 20 percent shift for fungi and 11 percent for bacteria.

- conf: not stated
- class: not stated
- holds: vineyard soils, 16S and ITS
- src: larsenDistinctTemporallyStable2023 (†: read in full text by a search agent and not re-opened by the reviewer)
- trail: C-RANKNET §Rank through time

From the note:

> C-RANKNET:B-0020 [The review as returned] A note on notation: references marked † in the list were read in full text by a search agent and not re-opened by me.
>
> C-RANKNET:B-0161 [Rank through time in community ecology, and whether it groups taxa] Two bounding facts about applying these metrics to sequencing data.
>
> C-RANKNET:B-0162 [Rank through time in community ecology, and whether it groups taxa] Larsen and colleagues computed rank shift on vineyard soil 16S and ITS data only for taxa observed in both compared years, so the zero-inflated portion of the table is discarded before ranks are formed, reporting about 20 percent shift for fungi and 11 percent for bacteria [34†].
>

## rank-trajectories.8 (claim)

Yao and colleagues found unstandardised mean rank shift incomparable across communities of different richness: phage MRS between adjacent time points ran from 400 to 1,000, far above bacterial values, which the authors attribute partly to phage taxa simply being more numerous.

- conf: not stated
- class: not stated
- holds: polyhydroxyalkanoate-producing mixed microbial cultures, phage and bacterial communities between adjacent time points
- src: yaoPhagesbacteriaInteractionsUnderlying2025 (†: read in full text by a search agent and not re-opened by the reviewer)
- trail: C-RANKNET §Rank through time

From the note:

> C-RANKNET:B-0020 [The review as returned] A note on notation: references marked † in the list were read in full text by a search agent and not re-opened by me.
>
> C-RANKNET:B-0163 [Rank through time in community ecology, and whether it groups taxa] Yao and colleagues found unstandardised mean rank shift incomparable across communities of different richness: phage MRS between adjacent time points ran from 400 to 1,000, far above bacterial values, which the authors attribute partly to phage taxa simply being more numerous [35†].
>
> C-RANKNET:R-0136 [References] Phages-bacteria interactions underlying the dynamics of polyhydroxyalkanoate-producing mixed microbial cultures via metagenomics and metatranscriptomics.
>

## rank-trajectories.9 (claim)

The codyn reference implementation collapses every absent taxon in a sample to a single shared rank S plus 1, so in a sparse table a large block of taxa carries one identical rank and contributes no rank change; the rule is known from a search agent's read of the package source, not from any full text the reviewer holds.

- conf: not stated
- class: not stated
- holds: codyn; zero-inflated tables
- src: hallettCodynRPackage2016 (†), hallettCodynRPackage2025 (read in full by a search agent)
- trail: C-RANKNET §Rank through time, §Full-text breaches, §Sources not obtained (all
- limit: access (critic: C-019)

From the note:

> C-RANKNET:B-0164 [Rank through time in community ecology, and whether it groups taxa] The reference implementation compounds this by collapsing every absent taxon in a sample to a single shared rank S plus 1 [28†], so in a sparse table a large block of taxa carries one identical rank and contributes no rank change.
>
> C-RANKNET:C-019 [Full-text breaches (4)] - The ten dagger-marked references (Batty, Collins, Avolio, codyn, Ghosh and Matthews, Larsen, Yao, Dodds, Iniguez, Barwell) were read by a search agent and not re-opened by the synthesiser. That is disclosed and no verdict rests on them, but one of them is load-bearing for a sequencing-properties claim: the codyn rule collapsing every absent taxon to rank S+1, which is the review's mechanism for why rank-shift metrics fail on zero-inflated tables, is sourced to a search agent's read of package source, not to any full text the reviewer holds.
>
> C-RANKNET:R-0300 [Sources not obtained (all agents)] - *Routes tried*: Not fetched by me; read in full by a search agent, which reported the tie handling (average ranks) and the rule collapsing absent taxa to rank S+1.
>
> C-RANKNET:R-0301 [Sources not obtained (all agents)] I cite that behaviour once, attributed to the search agent's read of the package source, and no verdict rests on it.
>

## rank-trajectories.10 (claim)

codyn handles ties with average ranks.

- conf: not stated
- class: not stated
- holds: the codyn package source (add_ranks, RAC_change, rank_shift)
- src: hallettCodynRPackage2025 (read in full by a search agent, not fetched by the synthesiser)
- trail: C-RANKNET §Sources not obtained (all

From the note:

> C-RANKNET:R-0298 [Sources not obtained (all agents)] - Lauren M. Hallett et al. codyn R package reference manual and source (add_ranks, RAC_change, rank_shift).
>
> C-RANKNET:R-0300 [Sources not obtained (all agents)] - *Routes tried*: Not fetched by me; read in full by a search agent, which reported the tie handling (average ranks) and the rule collapsing absent taxa to rank S+1.
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

Not found in the cited text (where to look, not what is wrong): holds: human

## taxon-grouping.2 (claim)

Liu and colleagues defined subcommunities with latent Dirichlet allocation first and then computed Collins-style rank change and evenness change on those subcommunities.

- conf: not stated
- class: meas (note: "measured; 59 samples, five sites, two years")
- holds: large-river deltaic estuaries, 59 samples, five sites, two years
- src: liuMicrobesClimateRefugia2025
- trail: C-RANKNET §Rank through time, §Search record

From the note:

> C-RANKNET:B-0153 [Rank through time in community ecology, and whether it groups taxa] Liu and colleagues defined subcommunities with latent Dirichlet allocation first and then computed Collins-style rank change and evenness change on those subcommunities [30] (measured; 59 samples, five sites, two years).
>
> C-RANKNET:B-0230 [Search record (synthesis agent)] I confirmed the pattern myself in the two microbial cases I read in full: Duran-Pinedo et al. 2021 computes rank clocks and mean rank shift descriptively while building the network with SPIEC-EASI and grouping taxa with a Dirichlet process Gaussian process mixture, and Liu et al. 2025 defines subcommunities with latent Dirichlet allocation first and computes rank change on them afterwards.
>
> C-RANKNET:R-0116 [References] Microbes under climate refugia: equable subcommunity rank dynamics in large-river deltaic estuaries.
>

## taxon-grouping.3 (claim)

In both the Duran-Pinedo and the Liu studies the rank quantity is reported alongside a separate magnitude-based or log-ratio-based grouping step, never as the basis of one.

- conf: not stated
- class: not stated
- holds: two microbial time-series studies
- src: duranpinedoLongtermDynamicsHuman2021, liuMicrobesClimateRefugia2025
- trail: C-RANKNET §Rank through time

From the note:

> C-RANKNET:B-0154 [Rank through time in community ecology, and whether it groups taxa] In both cases the rank quantity is reported alongside a separate magnitude-based or log-ratio-based grouping step, never as the basis of one.
>

Not found in the cited text (where to look, not what is wrong): holds: time-series

## taxon-grouping.4 (claim)

The review's searches found no study using rank clocks, mean rank shift or rank change to build a taxon association network or define taxon modules; in every full-text source located that computes these quantities, they are community-level or taxon-level descriptors reported beside a separate grouping step.

- conf: not stated
- class: search (note: "Each statement is about the searches run, not about what the literature has ruled out")
- holds: routes: Europe PMC exact-phrase sweeps on "rank clocks" (8 records), "rank clock" (12), "mean rank shift" or "mean rank shifts" (25), and codyn combined with reordering or rank change (18), with every ecological and microbial title inspected; Semantic Scholar graph search for rank-based network construction from abundance time series and for rank trajectory clustering; routes inherited from the search agents
- src: duranpinedoLongtermDynamicsHuman2021, liuMicrobesClimateRefugia2025, buckleyMeasuringChangeBiological2021
- trail: C-RANKNET §Gaps, with the routes, §Search record
- search: searched, not found (note: "Each statement is about the searches run, not about what the literature has ruled out")

From the note:

> C-RANKNET:B-0170 [Gaps, with the routes behind them] Each statement is about the searches run, not about what the literature has ruled out.
>
> C-RANKNET:B-0177 [Gaps, with the routes behind them] **No study using rank clocks, mean rank shift or rank change to build a taxon association network or define taxon modules.** Routes: Europe PMC exact-phrase sweeps on "rank clocks" (8 records), "rank clock" (12), "mean rank shift" or "mean rank shifts" (25), and codyn combined with reordering or rank change (18), with every ecological and microbial title inspected; Semantic Scholar graph search for rank-based network construction from abundance time series and for rank trajectory clustering.
>
> C-RANKNET:B-0178 [Gaps, with the routes behind them] In every full-text source located that computes these quantities, they are community-level or taxon-level descriptors reported beside a separate grouping step [29,30,32].
>
> C-RANKNET:B-0224 [Search record (synthesis agent)] NOT-FOUND CLAIMS AND THE ROUTES BEHIND THEM (all inherited from the search agents, whose route lists I reproduce, plus my own full-text confirmation where noted).
>
> C-RANKNET:B-0229 [Search record (synthesis agent)] (4) No study using rank clocks, mean rank shift or rank change to build a taxon association network or define taxon modules: Europe PMC exact-phrase sweeps on "rank clocks" (8 records), "rank clock" (12), "mean rank shift" OR "mean rank shifts" (25), and codyn AND (reordering OR "rank change") (18), with every ecological and microbial title inspected; Semantic Scholar graph search for rank-based network construction from abundance time series and for rank trajectory clustering.
>

## taxon-grouping.5 (claim)

The benchmarked method for grouping microbial taxa by behaviour across ordered samples is magnitude-based: Ananke normalises counts by per-sample depth, z-scores each trajectory, computes a short time-series slope-difference distance and clusters with DBSCAN, scoring adjusted mutual information above 0.8 against six ground-truth patterns with as few as ten time points, and dropping to median 0.69 at 500 points and 0.62 at 1,000.

- conf: not stated
- class: model (note: "modelled; simulated 16S-style series")
- holds: simulated 16S-style series, six ground-truth patterns
- src: hallAnankeTemporalClustering2017
- trail: C-RANKNET §Rank through time, §Glossary

From the note:

> C-RANKNET:B-0155 [Rank through time in community ecology, and whether it groups taxa] The benchmarked method for grouping microbial taxa by behaviour across ordered samples is magnitude-based.
>
> C-RANKNET:B-0156 [Rank through time in community ecology, and whether it groups taxa] Ananke normalises counts by per-sample depth, z-scores each trajectory, computes a short time-series slope-difference distance and clusters with DBSCAN, scoring adjusted mutual information above 0.8 against six ground-truth patterns with as few as ten time points, and dropping to median 0.69 at 500 points and 0.62 at 1,000 [31] (modelled; simulated 16S-style series).
>
> C-RANKNET:B-0199 [Glossary: what each field calls the rank device] **Ananke time-series clusters (TSCs)**: microbial time-series clustering: DBSCAN on a short time-series slope-difference distance between depth-normalised z-scored trajectories; magnitude-based, not rank-based.
>

## taxon-grouping.6 (claim)

Ananke's comparator set is Euclidean and Manhattan distance on the same standardised trajectories, with no rank-based comparator, and its stated failure mode is that the slope-difference distance cannot separate low-variance from high-variance stationary profiles.

- conf: not stated
- class: not stated
- holds: simulated 16S-style series
- src: hallAnankeTemporalClustering2017
- trail: C-RANKNET §Rank through time

From the note:

> C-RANKNET:B-0157 [Rank through time in community ecology, and whether it groups taxa] Its comparator set is Euclidean and Manhattan distance on the same standardised trajectories, with no rank-based comparator, and its stated failure mode is that the slope-difference distance cannot separate low-variance from high-variance stationary profiles [31].
>

Not found in the cited text (where to look, not what is wrong): holds: simulated; holds: 16s-style

## taxon-grouping.7 (claim)

A methods roadmap written for community time series with fewer than 25 temporal replicates lists rank abundance distributions and rank clocks as one of seven method families, described as graphs that "can be combined with dissimilarity methods and rank clocks".

- conf: not stated
- class: not stated
- holds: community time series with fewer than 25 temporal replicates
- src: buckleyMeasuringChangeBiological2021
- trail: C-RANKNET §Rank through time

From the note:

> C-RANKNET:B-0158 [Rank through time in community ecology, and whether it groups taxa] A methods roadmap written for community time series with fewer than 25 temporal replicates lists rank abundance distributions and rank clocks as one of seven method families, described as graphs that "can be combined with dissimilarity methods and rank clocks" [32].
>

## taxon-grouping.8 (claim)

The roadmap's seven method families contain no rank-based network construction and no rank-based module detection; that absence is the reviewer's reading of the list, not a statement the authors make.

- conf: not stated
- class: reading (note: "That absence is my reading of the reviewed list")
- holds: Buckley et al. 2021
- src: buckleyMeasuringChangeBiological2021
- trail: C-RANKNET §Rank through time

From the note:

> C-RANKNET:B-0159 [Rank through time in community ecology, and whether it groups taxa] Its seven families contain no rank-based network construction and no rank-based module detection at all.
>
> C-RANKNET:B-0160 [Rank through time in community ecology, and whether it groups taxa] That absence is my reading of the reviewed list, not a statement the authors make.
>

Not found in the cited text (where to look, not what is wrong): holds: buckley; holds: 2021

## adjacent-instruments.1 (claim)

Rank-turbulence divergence, a tunable rank-rank divergence, compares two ranked lists with fractional ranks for ties and states that "whatever complexities these systems may contain, such as networks of components, we are implicitly leaving them aside".

- conf: not stated
- class: not stated
- holds: complex systems
- src: doddsAllotaxonometryRankturbulenceDivergence2023 (†: read in full text by a search agent and not re-opened by the reviewer)
- trail: C-RANKNET §Rank through time, §Glossary

From the note:

> C-RANKNET:B-0020 [The review as returned] A note on notation: references marked † in the list were read in full text by a search agent and not re-opened by me.
>
> C-RANKNET:B-0165 [Rank through time in community ecology, and whether it groups taxa] Adjacent instruments exist and explicitly set network structure aside.
>
> C-RANKNET:B-0166 [Rank through time in community ecology, and whether it groups taxa] Rank-turbulence divergence compares two ranked lists with fractional ranks for ties and states that "whatever complexities these systems may contain, such as networks of components, we are implicitly leaving them aside" [36†].
>
> C-RANKNET:B-0197 [Glossary: what each field calls the rank device] **Rank-turbulence divergence (RTD)**: complex systems: tunable rank-rank divergence between two ranked lists, with network structure explicitly set aside.
>

## adjacent-instruments.2 (claim)

The physics-of-ranking literature defines rank turnover, rank flux and a rank change probability, temporal descriptors of a ranked list, none of which yields pairwise associations or modules.

- conf: not stated
- class: not stated
- holds: physics of ranking
- src: iniguezDynamicsRanking2022 (†: read in full text by a search agent and not re-opened by the reviewer)
- trail: C-RANKNET §Rank through time, §Glossary

From the note:

> C-RANKNET:B-0020 [The review as returned] A note on notation: references marked † in the list were read in full text by a search agent and not re-opened by me.
>
> C-RANKNET:B-0167 [Rank through time in community ecology, and whether it groups taxa] The physics-of-ranking literature defines rank turnover, rank flux and a rank change probability, none of which yields pairwise associations or modules [37†].
>
> C-RANKNET:B-0198 [Glossary: what each field calls the rank device] **Rank turnover, rank flux, rank change probability**: physics of ranking: temporal descriptors of a ranked list, producing no pairwise associations.
>

