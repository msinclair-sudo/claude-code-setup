## adjacent-instruments.3 (claim)

In beta-diversity methodology, decoupling of species ranks appears as a simulated truth axis for testing dissimilarity metrics rather than as a method.

- conf: not stated
- class: not stated
- holds: beta-diversity methodology
- src: barwellMeasuringBetadiversitySpecies2015 (†: read in full text by a search agent and not re-opened by the reviewer)
- trail: C-RANKNET §Rank through time

From the note:

> C-RANKNET:B-0020 [The review as returned] A note on notation: references marked † in the list were read in full text by a search agent and not re-opened by me.
>
> C-RANKNET:B-0168 [Rank through time in community ecology, and whether it groups taxa] In beta-diversity methodology, decoupling of species ranks appears as a simulated truth axis for testing dissimilarity metrics rather than as a method [38†].
>

## verdict-b.1 (claim)

On microbial abundance data, measured in simulation only, plain rank correlation as an edge measure performs no better or worse than Pearson: benchmarked at least four times, it was statistically indistinguishable from Pearson and jointly top in gLV metacommunities (Berry and Widder), similar to Pearson and both at or above compositional methods in gLV relative abundances (Hirano and Takemoto), "only marginally better" than Pearson under compositional closure (Friedman and Alm), and less distorted by closure but "still not immune" in the largest correlation benchmark (Weiss et al.).

- conf: repl (critic: C-094)
- class: model (critic: C-007)
- holds: simulated microbial abundance data; four separate simulation benchmarks; the critic: the verdict would stand without any one of them, and the verdict direction survives on these four
- src: berryDecipheringMicrobialInteractions2014, hiranoDifficultyInferringMicrobial2019, friedmanInferringCorrelationNetworks2012, weissCorrelationDetectionStrategies2016
- trail: C-RANKNET §critic, §Verdicts, §Expectation echo

From the note:

> C-RANKNET:C-007 [danger: Critic: verdict partly supported] Part B (microbial abundance data): measured in simulation only, and plain rank correlation performs no better or worse than Pearson (Weiss, Hirano and Takemoto, Friedman and Alm, Berry and Widder).
>
> C-RANKNET:A-046 [Verdict the body actually supports] Part B (microbial abundance data): measured in simulation only, and plain rank correlation performs no better or worse than Pearson (Weiss, Hirano and Takemoto, Friedman and Alm, Berry and Widder).
>
> C-RANKNET:A-011 [Verdicts] Rank correlation as an edge measure has been benchmarked on simulated microbial abundance data at least four times, and in every case it matched Pearson rather than beating it: statistically indistinguishable from Pearson and jointly top in gLV metacommunities [16], similar to Pearson and both at or above compositional methods in gLV relative abundances [14], "only marginally better" than Pearson under compositional closure [15], and less distorted by closure but "still not immune" in the largest correlation benchmark [13].
>
> C-RANKNET:B-0101 [The rank device in microbial abundance data] Where plain rank correlation has been compared with magnitude correlation on simulated microbial data, the answer is consistently "no difference".
>
> C-RANKNET:C-094 [Expectation echo] For Part B the 'no better or worse' direction has genuine independent support in four separate simulation benchmarks that I verified in full text: Berry and Widder (Pearson versus Spearman the only non-significant pair), Hirano and Takemoto (Spearman-based 'almost equal to or higher' than compositional methods, with Pearson-based 'similar or higher' too), Friedman and Alm ('Spearman correlations performed only marginally better'), and Weiss et al. ('less affected ... but still not immune').
>
> C-RANKNET:C-095 [Expectation echo] That verdict would stand without any one of them.
>
> C-RANKNET:A-031 [Verdict assessment] The verdict direction survives on the other four benchmarks, but the argument given for it does not.
>

## verdict-b.2 (claim)

One rank-based copula estimator (SPRING) beats both Pearson-based and compositional neighbourhood selection in its authors' simulations and loses to compositional methods only in the distorted low-sample scale-free case.

- conf: not stated
- class: model (critic: C-009)
- holds: the SPRING authors' simulations
- src: yoonMicrobialNetworksSPRING2019
- trail: C-RANKNET §critic, §Verdict the body

From the note:

> C-RANKNET:C-009 [danger: Critic: verdict partly supported] Part B should read: measured in silico; plain rank correlation no better or worse than magnitude correlation; one rank-based copula estimator beats both Pearson-based and compositional neighbourhood selection in its authors' simulations and loses to compositional methods only in the distorted low-sample scale-free case; nothing measured against experimentally validated interactions; reciprocal-rank neighbourhoods and rank trajectories never applied to this data type.
>
> C-RANKNET:A-048 [Verdict the body actually supports] Part B should read: measured in silico; plain rank correlation no better or worse than magnitude correlation; one rank-based copula estimator beats both Pearson-based and compositional neighbourhood selection in its authors' simulations and loses to compositional methods only in the distorted low-sample scale-free case; nothing measured against experimentally validated interactions; reciprocal-rank neighbourhoods and rank trajectories never applied to this data type.
>

Not found in the cited text (where to look, not what is wrong): SPRING; holds: spring

## verdict-b.3 (claim)

Nothing on microbial abundance data has been measured against experimentally validated interactions: all of the evidence is modelled, on in silico tables whose truth is a generated matrix, and the field states that no experimentally validated gold standard and no DREAM-style challenge exists.

- conf: not stated
- class: model (critic: C-009)
- holds: microbial abundance data; the DREAM-style statement rests on Faust 2021 alone (critic)
- src: ghaeliEvaluatingMicrobialNetwork2026, faustOpenChallengesMicrobial2021
- trail: C-RANKNET §critic, §Verdicts

From the note:

> C-RANKNET:C-009 [danger: Critic: verdict partly supported] Part B should read: measured in silico; plain rank correlation no better or worse than magnitude correlation; one rank-based copula estimator beats both Pearson-based and compositional neighbourhood selection in its authors' simulations and loses to compositional methods only in the distorted low-sample scale-free case; nothing measured against experimentally validated interactions; reciprocal-rank neighbourhoods and rank trajectories never applied to this data type.
>
> C-RANKNET:A-013 [Verdicts] Two qualifications bound this verdict.
>
> C-RANKNET:A-014 [Verdicts] All of the evidence is modelled, on in silico tables whose truth is a generated matrix; the field states that no experimentally validated gold standard and no DREAM-style challenge exists [19,20], so nothing here has been measured against real interactions.
>
> C-RANKNET:C-027 [Single-source claims (6)] - 'No DREAM-style challenge exists for microbial network inference' rests on Faust 2021 alone and is asserted in a review, correctly labelled SECONDARY once but then used in the Part B verdict as an established field fact.
>

## verdict-b.4 (claim)

Two subfamilies named in the question, reciprocal-rank neighbourhoods and rank trajectories, have never been applied to microbial abundance data, let alone benchmarked there.

- conf: not stated
- class: search (note: "Each statement is about the searches run, not about what the literature has ruled out")
- holds: the review's searches for mutual rank or HRR on microbial data and for rank clocks, mean rank shift or rank change as a basis for taxon networks or modules
- src: none (the review's search)
- trail: C-RANKNET §critic, §Verdicts, §Gaps, with the routes
- search: searched, not found (note: "Each statement is about the searches run, not about what the literature has ruled out")

From the note:

> C-RANKNET:C-009 [danger: Critic: verdict partly supported] Part B should read: measured in silico; plain rank correlation no better or worse than magnitude correlation; one rank-based copula estimator beats both Pearson-based and compositional neighbourhood selection in its authors' simulations and loses to compositional methods only in the distorted low-sample scale-free case; nothing measured against experimentally validated interactions; reciprocal-rank neighbourhoods and rank trajectories never applied to this data type.
>
> C-RANKNET:A-015 [Verdicts] And two subfamilies named in the question, reciprocal-rank neighbourhoods and rank trajectories, have never been applied to microbial abundance data at all, let alone benchmarked there.
>
> C-RANKNET:A-048 [Verdict the body actually supports] Part B should read: measured in silico; plain rank correlation no better or worse than magnitude correlation; one rank-based copula estimator beats both Pearson-based and compositional neighbourhood selection in its authors' simulations and loses to compositional methods only in the distorted low-sample scale-free case; nothing measured against experimentally validated interactions; reciprocal-rank neighbourhoods and rank trajectories never applied to this data type.
>
> C-RANKNET:B-0170 [Gaps, with the routes behind them] Each statement is about the searches run, not about what the literature has ruled out.
>
> C-RANKNET:B-0171 [Gaps, with the routes behind them] **No study applying mutual rank or highest reciprocal rank to microbial abundance data.** Routes: web searches pairing "mutual rank" and "highest reciprocal rank" with microbiome, taxa, co-abundance, metagenomic, OTU and 16S; Europe PMC exact-phrase search for "mutual rank" combined with microbiome, microbial, OTU or 16S, returning five multi-omics hits in which mutual rank was applied to the gene side only.
>
> C-RANKNET:B-0177 [Gaps, with the routes behind them] **No study using rank clocks, mean rank shift or rank change to build a taxon association network or define taxon modules.** Routes: Europe PMC exact-phrase sweeps on "rank clocks" (8 records), "rank clock" (12), "mean rank shift" or "mean rank shifts" (25), and codyn combined with reordering or rank change (18), with every ecological and microbial title inspected; Semantic Scholar graph search for rank-based network construction from abundance time series and for rank trajectory clustering.
>

Not found in the cited text (where to look, not what is wrong): holds: review; holds: hrr

## verdict-b.5 (claim)

The review's sensitivity check for Part B: removing Yoon et al. removes the only pro-rank result and makes the verdict firmer rather than reversing it; removing Weiss et al. still leaves Hirano and Takemoto, Friedman and Alm and Berry and Widder on the same side.

- conf: not stated
- class: not stated
- holds: the review's Part B verdict
- src: yoonMicrobialNetworksSPRING2019, weissCorrelationDetectionStrategies2016, hiranoDifficultyInferringMicrobial2019, friedmanInferringCorrelationNetworks2012, berryDecipheringMicrobialInteractions2014
- trail: C-RANKNET §Verdicts

From the note:

> C-RANKNET:A-018 [Verdicts] For Part B, removing Yoon et al. [12] removes the only pro-rank result and strengthens the verdict; removing Weiss et al. [13] still leaves Hirano and Takemoto [14], Friedman and Alm [15] and Berry and Widder [16] on the same side.
>
> C-RANKNET:A-019 [Verdicts] The one source whose removal would most change the texture of Part B is Yoon et al. [12], because it is the only published claim of a rank-based win in this data type, but its removal makes the verdict firmer rather than reversing it.
>

Not found in the cited text (where to look, not what is wrong): holds: review

## dns.1 (do not say)

"Rank-based methods perform no better or worse than magnitude-based methods for building networks, in any data type."

- why: The critic replaced this verdict: the answer splits by which rank device and which criterion, the verdict pooled rank of the coefficient with rank of the value and four incommensurable metrics, and the brief primed a "no better or worse" direction that the review repeated, taking every negative datum at face value and arguing every positive one down.
- instead: verdict-a.1, verdict-a.4
- trail: C-RANKNET §critic, §Verdict assessment, §Expectation echo

From the note:

> C-RANKNET:A-001 [quote: Verdict as delivered by the synthesis agent] - **Part A (rank-based against magnitude-based network construction, any data type)**: measured and rank-based methods perform no better or worse
>
> C-RANKNET:A-003 [Verdicts] **Part A, rank-based against magnitude-based network construction benchmarked in any data type: measured and rank-based methods perform no better or worse.**
>
> C-RANKNET:A-020 [Verdicts] **Expectation check.** The brief's framing does not state a direction, and the verdicts here are not the ones a rank-friendly reading would produce.
>
> C-RANKNET:A-037 [Verdict assessment] Beyond those, the Part A verdict pools two devices the review's own opening paragraph separates, rank of the coefficient and rank of the value, and pools four incommensurable metrics (neighbour-voting AUROC, a composite PC1 "Quality" that includes promoter motif enrichment, GO enrichment p-values, TF cluster counts) into a single direction count.
>
> C-RANKNET:C-001 [danger: Critic: verdict partly supported] **Use this verdict, not the one above.**
>
> C-RANKNET:C-002 [danger: Critic: verdict partly supported] Part A (any data type): measured, and the answer splits by which rank device and which criterion, not by "rank versus magnitude" as a single question.
>
> C-RANKNET:C-088 [Expectation echo] - Brief states or implies an expectation: **True**
>
> C-RANKNET:C-089 [Expectation echo] - Review repeats it: **True**
>
> C-RANKNET:C-090 [Expectation echo] - Brief wording: The brief does not name a direction outright, but two of its bullets prime one: 'Bounding and negative facts: benchmarks in which rank-based methods did no better or did worse, and reviews stating the comparison has not been made', and 'A given named method may have no published benchmark; if so, report that plainly'.
>
> C-RANKNET:C-091 [Expectation echo] The deliverable's three verdict options likewise foreground 'no better or worse' and 'not measured'.
>
> C-RANKNET:C-092 [Expectation echo] Nothing in the brief solicits positive results with equal specificity.
>
> C-RANKNET:C-093 [Expectation echo] - Independent support: Partly independent, partly echo.
>
> C-RANKNET:C-096 [Expectation echo] For Part A the echo is stronger: the only unambiguous pro-rank accuracy result in the corpus (Obayashi and Kinoshita, four species, all three GO branches, all four summarisation methods) is correctly labelled SINGLE SOURCE and then outweighed by a number that belongs to a different analysis level (Liesecke's pathway-level 0.58 versus 0.57), a composite score misdescribed as GO accuracy (Vandenbon), and a null (Song).
>
> C-RANKNET:C-098 [Expectation echo] The pattern is that every negative datum is taken at face value and every positive datum is argued down, which is the shape an expectation echo makes even when the final direction happens to be defensible.
>

Not found in the cited text (where to look, not what is wrong): "Rank-based methods perform no better or worse than magnitude-based methods for building networks, in any data type."

## dns.2 (do not say)

"On function-prediction accuracy against GO, the record is a wash pointing slightly against ranking."

- why: The tally pools rank-of-coefficient and rank-of-value devices and four incommensurable criteria (neighbour-voting AUROC against GO, a composite PC1 quality score including promoter motif enrichment, GO enrichment p-value rankings, and counts of positive transcription factors in top clusters), and the Liesecke number in it belongs to a different analysis level.
- instead: verdict-a.2, expression-benchmarks.2
- trail: C-RANKNET §Verdicts, §Scope drift

From the note:

> C-RANKNET:A-005 [Verdicts] On function-prediction accuracy against GO, the record is a wash pointing slightly against ranking: one study finds rank better across four species [1], one finds raw better by 0.58 against 0.57 [4], one finds Pearson better by an average 0.011 in quality except below 30 samples [8], and one finds Spearman, Pearson and bicor indistinguishable [9].
>
> C-RANKNET:C-084 [Scope drift (7)] - The Part A verdict pools rank-of-coefficient constructions (mutual rank, HRR) with rank-of-value measures (Spearman, Kendall) into one direction tally, although the review's own opening paragraph identifies them as different devices used by different communities, and Obayashi's full text (read by the reviewer) contains the internal control showing Spearman value behaves like Pearson value while PCC rank does not. This is the rule 5 problem applied to directions rather than numbers.
>
> C-RANKNET:C-085 [Scope drift (7)] - The same verdict pools four incommensurable criteria as though they answered one question: neighbour-voting AUROC against GO, a composite PC1 quality score including promoter motif enrichment, GO enrichment p-value rankings, and counts of positive transcription factors in top clusters.
>

Not found in the cited text (where to look, not what is wrong): Liesecke

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
> C-RANKNET:A-036 [Verdict assessment] The review's framing ("Ranking loses slightly on the same criterion in the largest plant replication") over-reads a pathway-level trade-off into a global accuracy verdict.
>
> C-RANKNET:C-037 [Reference errors (7)] - Ref 4 (Liesecke et al. 2018): the figures 0.58 versus 0.57 NV AUROC, 0.35 versus 0.68 modularity and 0.20 versus 0.35 normalised chi-squared are pathway-level (PLC) subnetwork results averaged over five pathways in the RNA-seq normalisation comparison.
>
> C-RANKNET:C-038 [Reference errors (7)] The review presents the AUROC pair as the study's global GO benchmark.
>

Not found in the cited text (where to look, not what is wrong): "In Liesecke and colleagues' genome-wide benchmark, ranking loses slightly on GO accuracy: the raw coefficients scored 0.58 against 0.57."

## dns.4 (do not say)

"Vandenbon found Spearman 0.011 lower than Pearson in function-prediction accuracy against GO."

- why: Vandenbon's Quality is the first principal component of quality measures based on enrichment of functional annotations and of regulatory motifs in promoters, so listing it alongside neighbour-voting AUROC as the same criterion pools incommensurable metrics.
- instead: expression-benchmarks.17
- trail: C-RANKNET §Reference errors

From the note:

> C-RANKNET:C-043 [Reference errors (7)] - Ref 8 (Vandenbon 2022): 'Quality' is described in the Part A verdict as function-prediction accuracy against GO.
>
> C-RANKNET:C-044 [Reference errors (7)] It is the first principal component of quality measures based on enrichment of functional annotations *and* of regulatory motifs in promoters.
>
> C-RANKNET:C-045 [Reference errors (7)] Listing it alongside neighbour-voting AUROC as the same criterion pools incommensurable metrics.
>

Not found in the cited text (where to look, not what is wrong): 0.011; Spearman; Pearson; "Vandenbon found Spearman 0.011 lower than Pearson in function-prediction accuracy against GO."

## dns.5 (do not say)

"Bulk gene expression is the only data type in which the rank-against-magnitude comparison has been run properly."

- why: This evaluates the quality of other fields' research designs, which the brief forbids; the defensible statement is that other data types' benchmarks are simulation-based or unobtained, not that they are improper.
- instead: microbial-benchmarks.1
- trail: C-RANKNET §Verdicts, §Scope drift

From the note:

> C-RANKNET:A-004 [Verdicts] The comparison has been run repeatedly in bulk gene expression, which is the only data type where it has been run properly, and the direction depends entirely on the criterion.
>
> C-RANKNET:C-082 [Scope drift (7)] - 'bulk gene expression, which is the only data type where it has been run properly' evaluates the quality of other fields' research designs, which the brief forbids ('Do not evaluate or endorse any research design'). The defensible statement is that other data types' benchmarks are simulation-based or unobtained, not that they are improper.
>

Not found in the cited text (where to look, not what is wrong): "Bulk gene expression is the only data type in which the rank-against-magnitude comparison has been run properly."

## dns.6 (do not say)

"Rank correlation has a reproducible advantage at small sample size: Spearman beats Pearson below 30 samples."

- why: The advantage comes from one study (Vandenbon 2022), one data type (bulk RNA-seq) and one composite metric, and reproducible implies replication the body does not contain.
- instead: expression-benchmarks.18
- trail: C-RANKNET §What sequencing count, §Single-source claims, §Scope drift

From the note:

> C-RANKNET:B-0134 [What sequencing count properties do to rank methods] **Few samples relative to features.** Rank correlation's one reproducible advantage sits here: Spearman beats Pearson below 30 samples in bulk RNA-seq [8], attributed to reduced leverage of extreme values.
>
> C-RANKNET:A-009 [Verdicts] It supports a specific, reproducible advantage in coverage, comparability and module structure, and a specific, reproducible advantage at small sample size.
>
> C-RANKNET:C-022 [Single-source claims (6)] - 'Rank correlation's one reproducible advantage sits here: Spearman beats Pearson below 30 samples': one study (Vandenbon 2022), one data type (bulk RNA-seq), one composite metric.
>
> C-RANKNET:C-023 [Single-source claims (6)] The Part A verdict then calls it 'a specific, reproducible advantage at small sample size'.
>
> C-RANKNET:C-024 [Single-source claims (6)] Reproducible implies replication that the body does not contain.
>
> C-RANKNET:C-086 [Scope drift (7)] - 'Rank correlation's one reproducible advantage' and 'a specific, reproducible advantage in coverage, comparability and module structure' present single-study results as field properties, which Common rule 4 reserves for replicated findings.
>

Not found in the cited text (where to look, not what is wrong): "Rank correlation has a reproducible advantage at small sample size: Spearman beats Pearson below 30 samples."

## dns.7 (do not say)

"Ranking has a specific, reproducible advantage in coverage, comparability and module structure."

- why: The structural win rests entirely on Liesecke et al. 2018, and on its pathway-level analysis, so a single-study result is being presented as a field property.
- instead: verdict-a.3
- trail: C-RANKNET §Verdicts, §Single-source claims, §Scope drift

From the note:

> C-RANKNET:A-009 [Verdicts] It supports a specific, reproducible advantage in coverage, comparability and module structure, and a specific, reproducible advantage at small sample size.
>
> C-RANKNET:C-025 [Single-source claims (6)] - The structural win in Part A (nearly doubled modularity 0.35 to 0.68, chi-squared 0.20 to 0.35, twice the vertices at a quarter of the hub degree) rests entirely on Liesecke et al. 2018, and on its pathway-level analysis at that. The verdict calls this 'a specific, reproducible advantage in coverage, comparability and module structure'.
>
> C-RANKNET:C-086 [Scope drift (7)] - 'Rank correlation's one reproducible advantage' and 'a specific, reproducible advantage in coverage, comparability and module structure' present single-study results as field properties, which Common rule 4 reserves for replicated findings.
>

Not found in the cited text (where to look, not what is wrong): "Ranking has a specific, reproducible advantage in coverage, comparability and module structure."

## dns.8 (do not say)

"The evidence does not support a general accuracy advantage for ranking."

- why: The critic splits it by device: there is no general accuracy advantage for rank of the value, but there is one unreplicated accuracy advantage for rank of the coefficient.
- instead: verdict-a.4
- trail: C-RANKNET §Verdicts, §critic

From the note:

> C-RANKNET:A-008 [Verdicts] Taken together, the field has measured this, and the evidence does not support a general accuracy advantage for ranking.
>
> C-RANKNET:C-006 [danger: Critic: verdict partly supported] So: measured; no general accuracy advantage for rank-of-value, one unreplicated accuracy advantage for rank-of-coefficient, and reproducible-in-one-study structural advantages.
>

## dns.9 (do not say)

"SPRING's benchmark cannot separate a rank-based win from an absolute-abundance win, and no published study separates them."

- why: The fourth method in the same tables, MB, runs sample Pearson correlation on absolute abundance with no transform, sharing SPRING's input type, and is far behind SPRING in every cell; the absence claim names no search routes, and the review argued down this one pro-rank result on a confound argument the source's own tables refute.
- instead: spring.9
- trail: C-RANKNET §The rank device in microbial, §Verdict assessment, §Scope drift, §Expectation echo

From the note:

> C-RANKNET:B-0093 [The rank device in microbial abundance data] My reading is that this benchmark does not separate "rank-based wins" from "absolute abundance wins", and no published study separates them.
>
> C-RANKNET:A-012 [Verdicts] The one rank-based method that reports a win, SPRING, wins by a small margin in its own simulations with an input-data asymmetry the paper does not control for, loses to compositional methods when sample totals are distorted in the low-sample-size scale-free case [12], and does not appear as a top performer in either of the two independent evaluations that included it [18,19].
>
> C-RANKNET:A-021 [Verdicts] The two claims I had to argue down against the initial findings were the Liesecke 2018 result (whose title asserts improvement while its own accuracy number does not) and the SPRING result (whose margin is confounded with absolute-abundance input by the paper's own Table 2).
>
> C-RANKNET:A-026 [Verdict assessment] Two things break.
>
> C-RANKNET:A-027 [Verdict assessment] First, the SPRING confound argument, which is the reasoning that carries Part B's dismissal of the only pro-rank microbial result.
>
> C-RANKNET:A-028 [Verdict assessment] The review reads Table 2 as an input asymmetry (SPRING on absolute abundance, SPIEC-EASI and invSparCC on relative) and concludes the benchmark cannot separate "rank wins" from "absolute abundance wins", then adds the unsourced absence claim that no published study separates them.
>
> C-RANKNET:A-029 [Verdict assessment] The fourth method in that same table, MB, runs on absolute abundance with no transform and estimates sample Pearson correlation.
>
> C-RANKNET:A-030 [Verdict assessment] It is the control the review says does not exist, and it is far behind SPRING in every cell.
>
> C-RANKNET:A-031 [Verdict assessment] The verdict direction survives on the other four benchmarks, but the argument given for it does not.
>
> C-RANKNET:C-008 [danger: Critic: verdict partly supported] But the review's stated reason for discounting the one pro-rank result does not survive checking: in Yoon et al.'s own Table 2/Table 3, MB (sample Pearson correlation, absolute abundance, no transform) shares SPRING's input type and scores 0.42/0.32/0.26/0.20/0.25/0.01 AUPR against SPRING's 0.95/0.95/0.96/0.93/0.90/0.58, so that benchmark does separate the rank estimator from the absolute-abundance input, contrary to the review's "no published study separates them".
>
> C-RANKNET:C-081 [Scope drift (7)] - 'My reading is that this benchmark does not separate rank-based wins from absolute abundance wins, and no published study separates them.' This is the reviewer's own argument carrying a verdict, it is an absence claim with no search routes named (Common rule 7), and it is contradicted by Table 2 and Table 3 of the very source cited: MB runs Pearson on absolute abundance with no transform and scores 0.42 to 0.01 AUPR against SPRING's 0.95 to 0.58.
>
> C-RANKNET:C-097 [Expectation echo] In Part B the single pro-rank result is set aside on a confound argument that the source's own tables refute.
>

Not found in the cited text (where to look, not what is wrong): "SPRING benchmark cannot separate a rank-based win from an absolute-abundance win, and no published study separates them."

## dns.10 (do not say)

"Independent evaluations do not reproduce a SPRING advantage: SPRING is not a top performer in either of the two independent evaluations."

- why: In Kishore et al. this is inferred from SPRING not being named, while its values sit in figures the review could not obtain, and the absence of a name is not a measured underperformance; Ghaeli et al. measure reproducibility on real data with no truth set, so the two are not evaluations of performance of the same kind as the simulation benchmarks.
- instead: spring.11, spring.12
- trail: C-RANKNET §The rank device in microbial, §Full-text breaches, §Reference errors, §Scope drift

From the note:

> C-RANKNET:B-0095 [The rank device in microbial abundance data] Independent evaluations do not reproduce a SPRING advantage.
>
> C-RANKNET:A-012 [Verdicts] The one rank-based method that reports a win, SPRING, wins by a small margin in its own simulations with an input-data asymmetry the paper does not control for, loses to compositional methods when sample totals are distorted in the low-sample-size scale-free case [12], and does not appear as a top performer in either of the two independent evaluations that included it [18,19].
>
> C-RANKNET:C-020 [Full-text breaches (4)] - Kishore et al. 2023 (ref 18): the claim that independent evaluation 'does not reproduce a SPRING advantage' is inferred from SPRING not being named in the text, while the per-method precision values for SPRING sit in figures S5 and S6 that the review says it could not obtain. Absence of a name in a legend is not a measured underperformance, yet the Part B verdict cites it as one of 'two independent evaluations'.
>
> C-RANKNET:C-047 [Reference errors (7)] - Ref 19 (Ghaeli et al. 2026): the metric is reproducibility, F-score and Jaccard similarity between networks inferred from bootstrap and noise-perturbed variants of real data, in a paper whose premise is that no gold standard exists. The review's Part B verdict uses SPRING's absence from Tables 3 and 4 as evidence about performance alongside truth-based simulation benchmarks.
>
> C-RANKNET:C-087 [Scope drift (7)] - Presenting Ghaeli et al. (a reproducibility benchmark with no truth set, by its own framing) and Kishore et al. (whose SPRING numbers the review could not read) as 'two independent evaluations' of performance, then leaning on both in the Part B verdict, stretches what those sources measured.
>

Not found in the cited text (where to look, not what is wrong): "Independent evaluations do not reproduce a SPRING advantage: SPRING is not a top performer in either of the two independent evaluations."

## dns.11 (do not say)

"In the MNetClass benchmark every comparator used the same Spearman network, so it says nothing about rank against magnitude construction."

- why: WGCNA was run with its own default, Pearson-based construction, and it is one of the two comparators MNetClass could not beat on PPV, which makes that comparison partly a rank-versus-magnitude construction comparison.
- instead: microbial-modules.2
- trail: C-RANKNET §The rank device in microbial, §Reference errors, §Search record

From the note:

> C-RANKNET:B-0115 [The rank device in microbial abundance data] Every comparator used the same Spearman network [24], so this says nothing about rank against magnitude construction.
>
> C-RANKNET:B-0231 [Search record (synthesis agent)] (5) No benchmark comparing modules recovered from rank-built against magnitude-built microbiome networks: MNetClass, which I read in full, benchmarks seven clustering algorithms against FABIA ground truth but holds the construction fixed at Spearman for every comparator.
>
> C-RANKNET:C-040 [Reference errors (7)] - Ref 24 (MNetClass): 'Every comparator used the same Spearman network' is not what the paper says.
>
> C-RANKNET:C-041 [Reference errors (7)] Edge betweenness, label propagation, leading eigenvector, fast greedy, Louvain and manta used MNetClass's network; WGCNA was run with 'default parameters to automatically construct the network', that is, its own Pearson-based construction.
>
> C-RANKNET:C-042 [Reference errors (7)] WGCNA is also one of the two comparators MNetClass could not beat on PPV, which makes that comparison partly a rank-versus-magnitude construction comparison, the opposite of the review's dismissal.
>

Not found in the cited text (where to look, not what is wrong): "In the MNetClass benchmark every comparator used the same Spearman network, so it says nothing about rank against magnitude construction."

## dns.12 (do not say)

"Co-occurrence aggregation beat HRR-weighted aggregation on GO AUROC at p below 0.001."

- why: The source reports +0.02 against -0.016 GO AUROC, Student's t test, p < 2e-16; p below 0.001 is the figure's asterisk threshold, not the reported p value.
- instead: rank-aggregation.4
- trail: C-RANKNET §Head to head, §Reference errors

From the note:

> C-RANKNET:B-0067 [Head to head: ranked against unranked in expression data] **Ranking as an aggregation weight loses to counting.** When HRR values were used as the edge weight during aggregation of many small networks, co-occurrence aggregation (keeping edges that recur across networks) was significantly more predictive on GO AUROC, p below 0.001 [5] (measured; Arabidopsis microarray and RNA-seq compendia, six aggregation methods, HRR as the base weight throughout).
>
> C-RANKNET:C-046 [Reference errors (7)] - Ref 5 (Liesecke et al. 2019): the co-occurrence versus HRR aggregation difference is reported in the source as +0.02 versus -0.016 GO AUROC, Student's t test, p < 2e-16. The review gives 'p below 0.001', which is the figure's asterisk threshold, not the reported p value.
>

Not found in the cited text (where to look, not what is wrong): "Co-occurrence aggregation beat HRR-weighted aggregation on GO AUROC at p below 0.001."

## dns.13 (do not say)

"Zero-induced rank ties inflate Spearman correlations in sequencing count data generally, the sharpest mechanical result in the literature."

- why: The whole mechanism rests on Connor, Barberán and Clauset 2017, one soil 16S matrix with no truth set, and carries no SINGLE SOURCE label.
- instead: zero-ties.1
- trail: C-RANKNET §What sequencing count, §Single-source claims

From the note:

> C-RANKNET:B-0119 [What sequencing count properties do to rank methods] **Zeros and the ties they create.** This is the sharpest mechanical result in the whole literature.
>
> C-RANKNET:C-021 [Single-source claims (6)] - Zeros, ties and inflated Spearman: the entire mechanism rests on Connor, Barberan and Clauset 2017, one soil 16S matrix with no truth set, yet the review calls it 'the sharpest mechanical result in the whole literature' and treats it as a property of sequencing count data generally. No SINGLE SOURCE label is applied.
>

Not found in the cited text (where to look, not what is wrong): "Zero-induced rank ties inflate Spearman correlations in sequencing count data generally, the sharpest mechanical result in the literature."; Barberán

## dns.14 (do not say)

"The microbiome field has never adopted reciprocal-rank neighbourhoods."

- why: It rests on the reviewer's own search plus one multi-omics paper (Kudjordjie et al. 2022), and one illustrative paper does not establish a field-wide practice.
- instead: microbial-rank-devices.3
- trail: C-RANKNET §The rank device in microbial, §Single-source claims

From the note:

> C-RANKNET:B-0077 [The rank device in microbial abundance data] The microbiome field has never adopted reciprocal-rank neighbourhoods.
>
> C-RANKNET:C-026 [Single-source claims (6)] - 'The microbiome field has never adopted reciprocal-rank neighbourhoods' rests on the reviewer's own search plus one multi-omics paper (Kudjordjie et al. 2022) in which the gene side uses MR and the microbial side uses Spearman. One illustrative paper does not establish a field-wide practice.
>

## dns.15 (do not say)

"It is an established fact of the field that no DREAM-style challenge exists for microbial network inference."

- why: The statement rests on Faust 2021 alone and is asserted in a review, labelled SECONDARY once and then used in the Part B verdict as an established field fact.
- instead: known-truth.2
- trail: C-RANKNET §Single-source claims

From the note:

> C-RANKNET:C-027 [Single-source claims (6)] - 'No DREAM-style challenge exists for microbial network inference' rests on Faust 2021 alone and is asserted in a review, correctly labelled SECONDARY once but then used in the Part B verdict as an established field fact.
>

Not found in the cited text (where to look, not what is wrong): "It is an established fact of the field that no DREAM-style challenge exists for microbial network inference."

## dns.16 (do not say)

"eLSA is the one widely used microbiome association method that requires ordered samples."

- why: It rests on the eLSA paper itself, no source is cited for the exclusivity claim, and time-series microbiome methods such as MetaMIS, LIMITS, TIME and Granger-style inference are not considered.
- instead: elsa.1
- trail: C-RANKNET §The rank device in microbial, §Glossary, §Single-source claims

From the note:

> C-RANKNET:B-0084 [The rank device in microbial abundance data] **A rank-vector normal transform inside a time-series method.** eLSA normalises each series by a normal score transformation before local and time-lagged similarity scoring [22], and is the one widely used microbiome association method that requires ordered samples.
>
> C-RANKNET:B-0193 [Glossary: what each field calls the rank device] **eLSA / LSA (extended Local Similarity Analysis)**: microbiome: rank-vector normal-score transform followed by local and time-lagged similarity scoring; the one common microbiome association method requiring ordered samples.
>
> C-RANKNET:C-028 [Single-source claims (6)] - eLSA described as 'the one widely used microbiome association method that requires ordered samples' rests on the eLSA paper itself; no source is cited for the exclusivity claim, and time-series microbiome methods such as MetaMIS, LIMITS, TIME and Granger-style inference are not considered.
>

Not found in the cited text (where to look, not what is wrong): "eLSA is the one widely used microbiome association method that requires ordered samples."

## dns.17 (do not say)

"On microbial abundance data, rank-based methods perform no better or worse than magnitude-based ones."

- why: The critic's Part B narrows this to plain rank correlation, and adds that one rank-based copula estimator beats both Pearson-based and compositional neighbourhood selection in its authors' simulations.
- instead: verdict-b.1, verdict-b.2
- trail: C-RANKNET §Verdict as delivered, §Verdicts, §critic

From the note:

> C-RANKNET:A-002 [quote: Verdict as delivered by the synthesis agent] - **Part B (rank-based network construction on microbial abundance data)**: measured and rank-based methods perform no better or worse
>
> C-RANKNET:A-010 [Verdicts] **Part B, rank-based network construction benchmarked on microbial abundance data: measured and rank-based methods perform no better or worse.**
>
> C-RANKNET:C-009 [danger: Critic: verdict partly supported] Part B should read: measured in silico; plain rank correlation no better or worse than magnitude correlation; one rank-based copula estimator beats both Pearson-based and compositional neighbourhood selection in its authors' simulations and loses to compositional methods only in the distorted low-sample scale-free case; nothing measured against experimentally validated interactions; reciprocal-rank neighbourhoods and rank trajectories never applied to this data type.
>

Not found in the cited text (where to look, not what is wrong): "On microbial abundance data, rank-based methods perform no better or worse than magnitude-based ones."

