## functional-profile.1 (claim)

Turnover here means between-sample dissimilarity. "Function" in the soil literature means several different things: shotgun reads annotated to SEED, KEGG or eggNOG; GeoChip probe arrays; gene-family counts from assemblies or MAGs; profiles inferred from 16S (PICRUSt, FAPROTAX); and, in two cases, measured enzyme activity or protein.

- conf: not stated
- class: not stated
- holds: the soil literature reviewed
- src: none (the reviewer's definitions)
- trail: H1-05 §Functional versus taxonomic turnover

From the note:

> H1-05:B-0029 [Functional versus taxonomic turnover in soil microbial communities] Turnover here means between-sample dissimilarity.
>
> H1-05:B-0030 [Functional versus taxonomic turnover in soil microbial communities] "Function" in the soil literature means several different things, and they are kept apart below: shotgun reads annotated to SEED, KEGG or eggNOG; GeoChip probe arrays; gene-family counts from assemblies or MAGs; profiles inferred from 16S (PICRUSt, FAPROTAX); and, in two cases, measured enzyme activity or protein.
>

Not found in the cited text (where to look, not what is wrong): holds: reviewed

## covariation.1 (claim)

Across 16 soils from cold desert, hot desert, forest, grassland and tundra, Bray-Curtis dissimilarity of MG-RAST/SEED gene profiles correlated with 16S Bray-Curtis (Mantel r = 0.76) and with unweighted UniFrac (r = 0.82); only 13 to 23% of reads were annotatable, and desert and non-desert samples separated almost completely (ANOSIM R about 0.97 to 0.98).

- conf: not stated
- class: meas (marker)
- holds: 16 soils at a strong cross-biome contrast; figures confirmed against full text by the critic
- src: fiererCrossbiomeMetagenomicAnalyses2012 (FT; measured; critic: C-053 was "FT, via search agents; measured")
- trail: H1-05 §Covariation at strong contrasts, §answers, §critic, §Adversarial critique

From the note:

> H1-05:I-0001 [1.1 Covariation at strong contrasts] Across 16 soils from cold desert, hot desert, forest, grassland and tundra, Bray-Curtis dissimilarity of MG-RAST/SEED gene profiles correlated with 16S Bray-Curtis (Mantel r = 0.76) and unweighted UniFrac (r = 0.82) [1] [FT, via search agents; measured].
>
> H1-05:B-0035 [1.1 Covariation at strong contrasts] Only 13 to 23% of reads were annotatable, and desert and non-desert samples separated almost completely (ANOSIM R about 0.97 to 0.98).
>
> H1-05:A-006 [quote: Answers as delivered] The clearest cases come from strong cross-biome or between-site contrasts (Mantel r 0.76 to 0.82 across 16 soils [1]; Spearman rho 0.87 across 6 NutNet sites [2]; r2 0.28 across 845 pooled metagenomes [3]).
>
> H1-05:C-001 [danger: Critic: answers partly supported] - **D1, soil, DNA-measured functional profiles**: Positive covariation of functional and taxonomic dissimilarity is shown in three soil datasets at strong contrasts [1][2][3] (numbers confirmed against full text: Mantel r 0.76 and 0.82 [1]; rho 0.87 [2]; r2 0.2831 over 356,090 pairs from 845 MG-RAST metagenomes [3]).
>
> H1-05:C-033 [danger: Critic: answers partly supported] Most numbers checked against full text are reported accurately: Chen 2022 r2 0.2831, 44-99% vs 9-100%, t = 67.5, DistLM 16.3 vs 13.5%, 845 metagenomes; Fierer 2012 Mantel 0.76 and 0.82, 13-23% annotated; Leff rho 0.87; Igwe PERMANOVA R2 0.061/0.027 with residual df 19 vs 16; Gao n = 4 and the three tests; Xu dispersion pattern, with the ±30% decrease in function confirmed; Ulva envfit 0.70/0.17; Graco-Roza Mantel 0.254/0.115 and 13 deviating datasets (3 faster, 10 slower).
>
> H1-05:C-052 [warning: Adversarial critique, full findings] - [1] and [2] are labelled 'FT via search agents', not rechecked by the reviewer.
>
> H1-05:C-053 [warning: Adversarial critique, full findings] This critic confirmed the figures via PMC3535587 and PMC4568213, so the label can be upgraded.
>

## covariation.2 (claim)

On the reviewer's reading, not the authors', a single dominant desert/non-desert split drives both matrices in the 16-soil study, so the correlation may say more about that split than about fine-scale coupling; the critic adds that the authors made a parallel caveat for alpha diversity (the correlations were not significant without the cold-desert soils).

- conf: not stated
- class: reading (note: "My reading, not the authors'")
- holds: 16 soils, dominated by a desert/non-desert split
- src: fiererCrossbiomeMetagenomicAnalyses2012
- trail: H1-05 §Covariation at strong contrasts, §answers, §Adversarial critique

From the note:

> H1-05:B-0036 [1.1 Covariation at strong contrasts] My reading, not the authors': a single dominant split drives both matrices, so the correlation may say more about that split than about fine-scale coupling.
>
> H1-05:A-016 [quote: Answers as delivered] *Strength:* Moderate for covariation at strong contrasts (three independent soil datasets read in full, though all three share the Fierer group or MG-RAST pipeline lineage, and [1] rests on 16 samples dominated by a desert/non-desert split).
>
> H1-05:C-054 [warning: Adversarial critique, full findings] The reviewer's own reading of [1] (a desert/non-desert split drives the correlation) should note that the authors made a parallel caveat for alpha diversity (the correlations were not significant without the cold-desert soils).
>

## covariation.3 (claim)

The authors of Fierer 2012 conclude that functional redundancy 'is not so pervasive as to obscure' the taxonomy-function relationship.

- conf: not stated
- class: not stated
- holds: Fierer 2012
- src: fiererCrossbiomeMetagenomicAnalyses2012
- trail: H1-05 §Adversarial critique

From the note:

> H1-05:C-097 [warning: Adversarial critique, full findings] - Fierer 2012 [1] explicitly concludes that functional redundancy 'is not so pervasive as to obscure' the taxonomy-function relationship. The review lists [1] only as an annotation-fraction critique, not among the 'against redundancy' sources.
>

## covariation.4 (claim)

Across six NutNet grassland sites, functional-gene and bacterial dissimilarity correlated with rho = 0.87, mostly between sites; within-site N and P additions shifted both.

- conf: not stated
- class: meas (marker)
- holds: six NutNet grassland sites; figures confirmed against full text by the critic
- src: leffConsistentResponsesSoil2015 (FT; measured; critic: C-053 was "FT, measured")
- trail: H1-05 §Covariation at strong contrasts, §answers, §critic

From the note:

> H1-05:B-0037 [1.1 Covariation at strong contrasts] Across six NutNet grassland sites, functional-gene and bacterial dissimilarity correlated with rho = 0.87, mostly between sites.
>
> H1-05:I-0002 [1.1 Covariation at strong contrasts] Within-site N and P additions shifted both [2] [FT, measured].
>
> H1-05:A-006 [quote: Answers as delivered] The clearest cases come from strong cross-biome or between-site contrasts (Mantel r 0.76 to 0.82 across 16 soils [1]; Spearman rho 0.87 across 6 NutNet sites [2]; r2 0.28 across 845 pooled metagenomes [3]).
>
> H1-05:C-001 [danger: Critic: answers partly supported] - **D1, soil, DNA-measured functional profiles**: Positive covariation of functional and taxonomic dissimilarity is shown in three soil datasets at strong contrasts [1][2][3] (numbers confirmed against full text: Mantel r 0.76 and 0.82 [1]; rho 0.87 [2]; r2 0.2831 over 356,090 pairs from 845 MG-RAST metagenomes [3]).
>
> H1-05:C-033 [danger: Critic: answers partly supported] Most numbers checked against full text are reported accurately: Chen 2022 r2 0.2831, 44-99% vs 9-100%, t = 67.5, DistLM 16.3 vs 13.5%, 845 metagenomes; Fierer 2012 Mantel 0.76 and 0.82, 13-23% annotated; Leff rho 0.87; Igwe PERMANOVA R2 0.061/0.027 with residual df 19 vs 16; Gao n = 4 and the three tests; Xu dispersion pattern, with the ±30% decrease in function confirmed; Ulva envfit 0.70/0.17; Graco-Roza Mantel 0.254/0.115 and 13 deviating datasets (3 faster, 10 slower).
>
> H1-05:C-053 [warning: Adversarial critique, full findings] This critic confirmed the figures via PMC3535587 and PMC4568213, so the label can be upgraded.
>

## covariation.5 (claim)

In 845 pooled public soil metagenomes (356,090 pairs), pairwise functional and taxonomic Bray-Curtis similarities correlated (r2 = 0.2831).

- conf: not stated
- class: meas (marker)
- holds: 845 pooled MG-RAST soil metagenomes; rechecked against full text by the reviewer and the critic
- src: chenFunctionalRedundancySoil2022 (FT, rechecked by this reviewer; measured)
- trail: H1-05 §Covariation at strong contrasts, §answers, §critic

From the note:

> H1-05:I-0003 [1.1 Covariation at strong contrasts] In 845 pooled public soil metagenomes, pairwise functional and taxonomic Bray-Curtis similarities correlated (r2 = 0.2831) [3] [FT, rechecked by this reviewer; measured].
>
> H1-05:A-006 [quote: Answers as delivered] The clearest cases come from strong cross-biome or between-site contrasts (Mantel r 0.76 to 0.82 across 16 soils [1]; Spearman rho 0.87 across 6 NutNet sites [2]; r2 0.28 across 845 pooled metagenomes [3]).
>
> H1-05:C-001 [danger: Critic: answers partly supported] - **D1, soil, DNA-measured functional profiles**: Positive covariation of functional and taxonomic dissimilarity is shown in three soil datasets at strong contrasts [1][2][3] (numbers confirmed against full text: Mantel r 0.76 and 0.82 [1]; rho 0.87 [2]; r2 0.2831 over 356,090 pairs from 845 MG-RAST metagenomes [3]).
>
> H1-05:C-033 [danger: Critic: answers partly supported] Most numbers checked against full text are reported accurately: Chen 2022 r2 0.2831, 44-99% vs 9-100%, t = 67.5, DistLM 16.3 vs 13.5%, 845 metagenomes; Fierer 2012 Mantel 0.76 and 0.82, 13-23% annotated; Leff rho 0.87; Igwe PERMANOVA R2 0.061/0.027 with residual df 19 vs 16; Gao n = 4 and the three tests; Xu dispersion pattern, with the ±30% decrease in function confirmed; Ulva envfit 0.70/0.17; Graco-Roza Mantel 0.254/0.115 and 13 deviating datasets (3 faster, 10 slower).
>

## covariation.6 (claim)

At one site under coal-fire heating, metagenome and amplicon ordinations were concordant (Procrustes 0.802, m2 = 0.357), alongside stable functional similarity, so 'stable function' and 'covariation' coexist in one dataset.

- conf: not stated
- class: not stated
- holds: one site; a preprint read via a fetch summary
- src: barnettDisturbanceIncreasesSoil2025 (secondary or abstract-level; preprint; critic: C-048 was "FT via fetch summary; preprint")
- trail: H1-05 §Covariation at strong contrasts, §answers

From the note:

> H1-05:B-0038 [1.1 Covariation at strong contrasts] At one site under coal-fire heating, metagenome and amplicon ordinations were concordant (Procrustes 0.802, m2 = 0.357) [8] [FT via fetch summary; preprint].
>
> H1-05:A-024 [quote: Answers as delivered] [8] reports stable functional similarity alongside a strong metagenome-amplicon Procrustes correlation (0.80), so 'stable function' and 'covariation' coexist in one dataset..
>
> H1-05:C-047 [warning: Adversarial critique, full findings] - [30] Ho and Huang preprint, [8] Barnett and Shade, [35] Burke, [49] Swenson are labelled 'FT via fetch summary'.
>
> H1-05:C-048 [warning: Adversarial critique, full findings] A fetch summary is not a full-text reading, so these should be labelled secondary or abstract-level unless the text was read.
>

## covariation.7 (claim)

Across soils, functional and taxonomic dissimilarity are usually positively correlated; the clearest cases come from strong cross-biome or between-site contrasts (Mantel r 0.76 to 0.82 across 16 soils; Spearman rho 0.87 across 6 NutNet sites; r2 0.28 across 845 pooled metagenomes), and strong contrasts give covariation.

- conf: not stated
- class: meas (marker)
- holds: three soil datasets at strong contrasts, all using Bray-Curtis on annotated profiles and correlation-type tests; none used a null model; the critic: not independent in lineage, as two come from one group and the third pools MG-RAST submissions that may include the first
- src: fiererCrossbiomeMetagenomicAnalyses2012, leffConsistentResponsesSoil2015, chenFunctionalRedundancySoil2022
- rating: "Moderate for covariation at strong contrasts" (critic: C-002: these datasets are not independent in lineage)
- trail: H1-05 §answers, §Covariation at strong contrasts, §Contrast size, §critic

From the note:

> H1-05:A-001 [quote: Answers as delivered] **D1, soil, DNA-measured functional profiles: mixed.
>
> H1-05:A-002 [quote: Answers as delivered] Covariation is well supported at strong cross-site contrasts.
>
> H1-05:A-005 [quote: Answers as delivered] No clean dependence on contrast size is established.**: Across soils, functional and taxonomic dissimilarity are usually positively correlated.
>
> H1-05:A-006 [quote: Answers as delivered] The clearest cases come from strong cross-biome or between-site contrasts (Mantel r 0.76 to 0.82 across 16 soils [1]; Spearman rho 0.87 across 6 NutNet sites [2]; r2 0.28 across 845 pooled metagenomes [3]).
>
> H1-05:A-010 [quote: Answers as delivered] On contrast size: covariation is shown mainly at strong contrasts.
>
> H1-05:A-016 [quote: Answers as delivered] *Strength:* Moderate for covariation at strong contrasts (three independent soil datasets read in full, though all three share the Fierer group or MG-RAST pipeline lineage, and [1] rests on 16 samples dominated by a desert/non-desert split).
>
> H1-05:B-0034 [1.1 Covariation at strong contrasts] The best-documented soil result is that functional and taxonomic dissimilarity are positively correlated when samples span very different environments.
>
> H1-05:B-0039 [1.1 Covariation at strong contrasts] Standing: replicated across three independent datasets, all using Bray-Curtis on annotated profiles and correlation-type tests.
>
> H1-05:B-0040 [1.1 Covariation at strong contrasts] None used a null model.
>
> H1-05:B-0070 [1.4 Contrast size] Across studies, strong contrasts [1][2] give covariation.
>
> H1-05:C-001 [danger: Critic: answers partly supported] - **D1, soil, DNA-measured functional profiles**: Positive covariation of functional and taxonomic dissimilarity is shown in three soil datasets at strong contrasts [1][2][3] (numbers confirmed against full text: Mantel r 0.76 and 0.82 [1]; rho 0.87 [2]; r2 0.2831 over 356,090 pairs from 845 MG-RAST metagenomes [3]).
>
> H1-05:C-002 [danger: Critic: answers partly supported] These datasets are not independent in lineage: [1] and [2] come from one group, and [3] pools MG-RAST submissions that may include [1].
>
> H1-05:C-038 [danger: Critic: answers partly supported] (2) Section 1.1 calls [1][2][3] 'three independent datasets', while the strength note concedes they share a lineage.
>
> H1-05:I-0001 [1.1 Covariation at strong contrasts] Across 16 soils from cold desert, hot desert, forest, grassland and tundra, Bray-Curtis dissimilarity of MG-RAST/SEED gene profiles correlated with 16S Bray-Curtis (Mantel r = 0.76) and unweighted UniFrac (r = 0.82) [1] [FT, via search agents; measured].
>

## turnover-ordering.1 (claim)

Covariation and "function less variable" are compatible: covariation says nothing about which turnover is larger, because a correlation between dissimilarity matrices says nothing about their relative magnitudes; two soil datasets report both.

- conf: not stated
- class: not stated
- holds: the 845 pooled soil metagenomes and the coal-fire site
- src: chenFunctionalRedundancySoil2022, barnettDisturbanceIncreasesSoil2025
- trail: H1-05 §How the cases relate, §critic

From the note:

> H1-05:B-0146 [5. How the cases relate] Covariation and "function less variable" are compatible.
>
> H1-05:B-0147 [5. How the cases relate] [3] and [8] report both in one dataset, because a correlation between dissimilarity matrices says nothing about their relative magnitudes.
>
> H1-05:C-003 [danger: Critic: answers partly supported] Covariation says nothing about which turnover is larger.
>
> H1-05:C-037 [danger: Critic: answers partly supported] The body's own Section 5 concedes that covariation and magnitude are separate.
>
> H1-05:I-0003 [1.1 Covariation at strong contrasts] In 845 pooled public soil metagenomes, pairwise functional and taxonomic Bray-Curtis similarities correlated (r2 = 0.2831) [3] [FT, rechecked by this reviewer; measured].
>
> H1-05:B-0038 [1.1 Covariation at strong contrasts] At one site under coal-fire heating, metagenome and amplicon ordinations were concordant (Procrustes 0.802, m2 = 0.357) [8] [FT via fetch summary; preprint].
>

## turnover-ordering.2 (claim)

In the global pooled dataset, functional Bray-Curtis similarity ranged 44 to 99% and taxonomic 9 to 100% (paired t = 67.5); climate plus soil explained 16.3% of taxonomic and 13.5% of functional variation (DistLM). The authors call this strong evidence for functional redundancy. It is the one large soil magnitude comparison, and it finds functional similarity higher than taxonomic at a strong (global) contrast; removing it would leave the 'function lower' ordering resting on small single-site studies and significance contrasts.

- conf: single (note: "SINGLE SOURCE for this sample size")
- class: not stated
- holds: 845 pooled public soil metagenomes; the profiles pool assembled and unassembled MG-RAST submissions from many studies; SEED level 3 (1,135 functions) compared with RefSeq genus (1,113 taxa); nothing tests whether a lower functional dissimilarity is expected from aggregation alone; figures checked against full text by the reviewer and the critic
- src: chenFunctionalRedundancySoil2022 (FT, rechecked)
- trail: H1-05 §Functional turnover reported lower, §answers, §critic

From the note:

> H1-05:B-0041 [1.2 Functional turnover reported lower than taxonomic] The same global dataset [3] shows the ordering most often cited for redundancy.
>
> H1-05:B-0042 [1.2 Functional turnover reported lower than taxonomic] Functional similarity ranged 44 to 99% and taxonomic 9 to 100% (paired t = 67.5).
>
> H1-05:B-0043 [1.2 Functional turnover reported lower than taxonomic] Climate plus soil explained 16.3% of taxonomic and 13.5% of functional variation (DistLM) [FT, rechecked].
>
> H1-05:B-0044 [1.2 Functional turnover reported lower than taxonomic] The authors call this strong evidence for functional redundancy.
>
> H1-05:B-0045 [1.2 Functional turnover reported lower than taxonomic] Caveats: the profiles pool assembled and unassembled MG-RAST submissions from many studies, SEED level 3 (1,135 functions) is compared with RefSeq genus (1,113 taxa), and nothing tests whether a lower functional dissimilarity is expected from aggregation alone (see Section 3).
>
> H1-05:B-0046 [1.2 Functional turnover reported lower than taxonomic] SINGLE SOURCE for this sample size.
>
> H1-05:A-007 [quote: Answers as delivered] Several studies also report that functional profiles are more similar across samples than taxonomic profiles are.
>
> H1-05:A-008 [quote: Answers as delivered] The largest of these is the global comparison (functional Bray-Curtis similarity 44 to 99% vs taxonomic 9 to 100% [3]); the others are a significant taxonomic shift with no significant functional shift at serpentine/non-serpentine pairs [4], stable KO similarity during fire-disturbance recovery [8], and several abstract-only or cross-paper comparisons [13][14][18][24].
>
> H1-05:A-019 [quote: Answers as delivered] [3] pools heterogeneous MG-RAST studies.
>
> H1-05:A-032 [quote: Answers as delivered] *Single-source sensitivity:* Removing Chen et al. 2022 [3] would remove the only large-sample soil evidence that functional similarity exceeds taxonomic similarity on the same samples and metric.
>
> H1-05:A-033 [quote: Answers as delivered] The 'function lower' ordering would then rest on small single-site studies and significance contrasts.
>
> H1-05:C-004 [danger: Critic: answers partly supported] The one large soil magnitude comparison [3] finds functional similarity higher than taxonomic, and it does so at a strong (global) contrast.
>
> H1-05:C-033 [danger: Critic: answers partly supported] Most numbers checked against full text are reported accurately: Chen 2022 r2 0.2831, 44-99% vs 9-100%, t = 67.5, DistLM 16.3 vs 13.5%, 845 metagenomes; Fierer 2012 Mantel 0.76 and 0.82, 13-23% annotated; Leff rho 0.87; Igwe PERMANOVA R2 0.061/0.027 with residual df 19 vs 16; Gao n = 4 and the three tests; Xu dispersion pattern, with the ±30% decrease in function confirmed; Ulva envfit 0.70/0.17; Graco-Roza Mantel 0.254/0.115 and 13 deviating datasets (3 faster, 10 slower).
>

## turnover-ordering.3 (claim)

Between serpentine and non-serpentine site pairs, bacterial composition differed (PERMANOVA R2 = 0.061, P = 0.004) while eggNOG functional composition did not (R2 = 0.027, P = 0.391); the authors conclude redundancy, and note that specialized functions such as siderophore biosynthesis did differ.

- conf: not stated
- class: meas (marker)
- holds: serpentine and non-serpentine soil pairs; residual df 19 against 16; figures rechecked by the reviewer and the critic
- src: igweRedundancyMaintainsMicrobial2026 (FT, rechecked; measured)
- trail: H1-05 §Functional turnover reported lower, §answers, §critic

From the note:

> H1-05:I-0004 [1.2 Functional turnover reported lower than taxonomic] - Serpentine vs non-serpentine pairs: bacterial composition differed (PERMANOVA R2 = 0.061, P = 0.004), eggNOG functional composition did not (R2 = 0.027, P = 0.391) [4] [FT, rechecked; measured].
>
> H1-05:B-0048 [1.2 Functional turnover reported lower than taxonomic] The authors conclude redundancy, and they note that specialized functions such as siderophore biosynthesis did differ.
>
> H1-05:A-008 [quote: Answers as delivered] The largest of these is the global comparison (functional Bray-Curtis similarity 44 to 99% vs taxonomic 9 to 100% [3]); the others are a significant taxonomic shift with no significant functional shift at serpentine/non-serpentine pairs [4], stable KO similarity during fire-disturbance recovery [8], and several abstract-only or cross-paper comparisons [13][14][18][24].
>
> H1-05:C-033 [danger: Critic: answers partly supported] Most numbers checked against full text are reported accurately: Chen 2022 r2 0.2831, 44-99% vs 9-100%, t = 67.5, DistLM 16.3 vs 13.5%, 845 metagenomes; Fierer 2012 Mantel 0.76 and 0.82, 13-23% annotated; Leff rho 0.87; Igwe PERMANOVA R2 0.061/0.027 with residual df 19 vs 16; Gao n = 4 and the three tests; Xu dispersion pattern, with the ±30% decrease in function confirmed; Ulva envfit 0.70/0.17; Graco-Roza Mantel 0.254/0.115 and 13 deviating datasets (3 faster, 10 slower).
>

Not found in the cited text (where to look, not what is wrong): holds: soil

## turnover-ordering.4 (claim)

On the reviewer's reading, the serpentine result is a significant test set against a non-significant one, on datasets of different size after QC (the functional dataset is smaller): site pairs explained about 56% of variation in both functional (non-significant, F(19,16)) and bacterial (significant) composition, which suggests limited power on the functional side rather than an absence of structure.

- conf: not stated
- class: reading (note: "My reading")
- holds: serpentine and non-serpentine soil pairs
- src: igweRedundancyMaintainsMicrobial2026
- trail: H1-05 §Functional turnover reported lower, §answers

From the note:

> H1-05:B-0049 [1.2 Functional turnover reported lower than taxonomic] My reading: this is a significant test set against a non-significant one, on datasets of different size after QC.
>
> H1-05:B-0050 [1.2 Functional turnover reported lower than taxonomic] Site pairs explained about 56% of variation in both functional (non-significant, F(19,16)) and bacterial (significant) composition, which suggests limited power on the functional side rather than an absence of structure.
>
> H1-05:A-020 [quote: Answers as delivered] In [4] the functional dataset is smaller, and the result compares a significant test with a non-significant one.
>

Not found in the cited text (where to look, not what is wrong): holds: non-serpentine; holds: soil

## turnover-ordering.5 (claim)

Along a latitudinal forest gradient in China, bacterial Bray-Curtis showed strong distance decay, while GeoChip function (summarized as DCA axes, not pairwise dissimilarity) was "highly convergent"; the two turnovers are not on a common basis.

- conf: not stated
- class: not stated
- holds: natural broadleaf forest along a latitudinal gradient in China; GeoChip against 16S
- src: zhangSoilBacterialEndemism2016 (FT via agents)
- trail: H1-05 §Functional turnover reported lower

From the note:

> H1-05:B-0051 [1.2 Functional turnover reported lower than taxonomic] - A latitudinal forest gradient in China: bacterial Bray-Curtis showed strong distance decay, while GeoChip function (summarized as DCA axes, not pairwise dissimilarity) was "highly convergent" [7] [FT via agents].
>
> H1-05:B-0052 [1.2 Functional turnover reported lower than taxonomic] The two turnovers are not on a common basis.
>
> H1-05:R-0045 [Reference list] Soil bacterial endemism and potential functional redundancy in natural broadleaf forest along a latitudinal gradient.
>

Not found in the cited text (where to look, not what is wrong): holds: 16s

## turnover-ordering.6 (claim)

Under coal-fire disturbance, OTU similarity to reference rose as soils cooled, while KO similarity stayed high throughout (stable KO similarity during fire-disturbance recovery); MAG-based redundancy rose with disturbance, which the authors attribute to lower diversity and smaller genomes.

- conf: not stated
- class: not stated
- holds: one coal-fire site; a preprint with no published version found, read via a fetch summary
- src: barnettDisturbanceIncreasesSoil2025 (secondary or abstract-level; preprint, no published version found; critic: C-048 was "FT via fetch summary; preprint, no published version found")
- trail: H1-05 §Functional turnover reported lower, §answers

From the note:

> H1-05:B-0053 [1.2 Functional turnover reported lower than taxonomic] - Coal-fire disturbance: OTU similarity to reference rose as soils cooled, while KO similarity stayed high throughout.
>
> H1-05:B-0054 [1.2 Functional turnover reported lower than taxonomic] MAG-based redundancy rose with disturbance, which the authors attribute to lower diversity and smaller genomes [8] [FT via fetch summary; preprint, no published version found].
>
> H1-05:A-008 [quote: Answers as delivered] The largest of these is the global comparison (functional Bray-Curtis similarity 44 to 99% vs taxonomic 9 to 100% [3]); the others are a significant taxonomic shift with no significant functional shift at serpentine/non-serpentine pairs [4], stable KO similarity during fire-disturbance recovery [8], and several abstract-only or cross-paper comparisons [13][14][18][24].
>
> H1-05:C-048 [warning: Adversarial critique, full findings] A fetch summary is not a full-text reading, so these should be labelled secondary or abstract-level unless the text was read.
>

Not found in the cited text (where to look, not what is wrong): holds: site

## turnover-ordering.7 (claim)

No fertilizer effect on functional profiles after 54 years, despite taxonomic shifts.

- conf: not stated
- class: not stated
- holds: long-term N, P, K and NPK fertilization of grassland soil, 54 years; abstract only
- src: panImpactLongtermN2014 (AB)
- trail: H1-05 §Functional turnover reported lower

From the note:

> H1-05:B-0055 [1.2 Functional turnover reported lower than taxonomic] - Abstract-only reports: no fertilizer effect on functional profiles after 54 years despite taxonomic shifts [13]; stable functional potential across a 1 to 30 C peat incubation while taxonomy changed [14]; taxonomic differences "far greater" than SEED functional differences under tillage and rotation, with the two measured in different papers [18]; similar functional capacities in arid vs hyperarid saline drylands despite structural differences [24] [FT via agents, abstract and methods only closely read]; high Hg with little change in C and N genes but a significant shift in predicted-gene beta diversity [16]; taxonomic diversity falling and gene-pool diversity rising after aromatic pollution in a microcosm (alpha, not turnover) [17].
>
> H1-05:R-0057 [Reference list] Impact of long-term N, P, K, and NPK fertilization on the composition and potential functions of the bacterial community in grassland soil.
>

## turnover-ordering.8 (claim)

Stable functional potential across a 1 to 30 C peat incubation while taxonomy changed.

- conf: not stated
- class: not stated
- holds: peat incubation; abstract only
- src: yangDecouplingMicrobialCommunity2021 (AB)
- trail: H1-05 §Functional turnover reported lower

From the note:

> H1-05:B-0055 [1.2 Functional turnover reported lower than taxonomic] - Abstract-only reports: no fertilizer effect on functional profiles after 54 years despite taxonomic shifts [13]; stable functional potential across a 1 to 30 C peat incubation while taxonomy changed [14]; taxonomic differences "far greater" than SEED functional differences under tillage and rotation, with the two measured in different papers [18]; similar functional capacities in arid vs hyperarid saline drylands despite structural differences [24] [FT via agents, abstract and methods only closely read]; high Hg with little change in C and N genes but a significant shift in predicted-gene beta diversity [16]; taxonomic diversity falling and gene-pool diversity rising after aromatic pollution in a microcosm (alpha, not turnover) [17].
>

## turnover-ordering.9 (claim)

Taxonomic differences "far greater" than SEED functional differences under tillage and rotation, with the two measured in different papers.

- conf: not stated
- class: not stated
- holds: a soil under different tillage and crop-management (rotation) regimes; abstract only; a cross-paper comparison
- src: souzaMetagenomicAnalysisReveals2015 (AB)
- trail: H1-05 §Functional turnover reported lower

From the note:

> H1-05:B-0055 [1.2 Functional turnover reported lower than taxonomic] - Abstract-only reports: no fertilizer effect on functional profiles after 54 years despite taxonomic shifts [13]; stable functional potential across a 1 to 30 C peat incubation while taxonomy changed [14]; taxonomic differences "far greater" than SEED functional differences under tillage and rotation, with the two measured in different papers [18]; similar functional capacities in arid vs hyperarid saline drylands despite structural differences [24] [FT via agents, abstract and methods only closely read]; high Hg with little change in C and N genes but a significant shift in predicted-gene beta diversity [16]; taxonomic diversity falling and gene-pool diversity rising after aromatic pollution in a microcosm (alpha, not turnover) [17].
>
> H1-05:R-0067 [Reference list] Metagenomic analysis reveals microbial functional redundancies and specificities in a soil under different tillage and crop-management regimes.
>

Not found in the cited text (where to look, not what is wrong): holds: cross-paper

## turnover-ordering.10 (claim)

Similar functional capacities in arid and hyperarid saline drylands despite structural differences.

- conf: not stated
- class: not stated
- holds: arid and hyperarid saline drylands; only the abstract and methods closely read, so abstract-level for its result claim
- src: saumasanchezFunctionalRedundancyBuffers2024 (AB for its result claim; critic: C-051 was "FT via agents, abstract and methods only closely read")
- trail: H1-05 §Functional turnover reported lower, §Adversarial critique

From the note:

> H1-05:B-0055 [1.2 Functional turnover reported lower than taxonomic] - Abstract-only reports: no fertilizer effect on functional profiles after 54 years despite taxonomic shifts [13]; stable functional potential across a 1 to 30 C peat incubation while taxonomy changed [14]; taxonomic differences "far greater" than SEED functional differences under tillage and rotation, with the two measured in different papers [18]; similar functional capacities in arid vs hyperarid saline drylands despite structural differences [24] [FT via agents, abstract and methods only closely read]; high Hg with little change in C and N genes but a significant shift in predicted-gene beta diversity [16]; taxonomic diversity falling and gene-pool diversity rising after aromatic pollution in a microcosm (alpha, not turnover) [17].
>
> H1-05:C-051 [warning: Adversarial critique, full findings] - [24] is labelled 'FT via agents, partly read' (abstract and methods only). It should be abstract-level for its result claim, and it is used in D1 as a 'function lower' result.
>

## turnover-ordering.11 (claim)

Under high Hg, little change in C and N genes but a significant shift in predicted-gene beta diversity.

- conf: not stated
- class: not stated
- holds: long-term mercury contamination of soils (high Hg); abstract only
- src: freyLongtermMercuryContamination2022 (AB)
- trail: H1-05 §Functional turnover reported lower

From the note:

> H1-05:B-0055 [1.2 Functional turnover reported lower than taxonomic] - Abstract-only reports: no fertilizer effect on functional profiles after 54 years despite taxonomic shifts [13]; stable functional potential across a 1 to 30 C peat incubation while taxonomy changed [14]; taxonomic differences "far greater" than SEED functional differences under tillage and rotation, with the two measured in different papers [18]; similar functional capacities in arid vs hyperarid saline drylands despite structural differences [24] [FT via agents, abstract and methods only closely read]; high Hg with little change in C and N genes but a significant shift in predicted-gene beta diversity [16]; taxonomic diversity falling and gene-pool diversity rising after aromatic pollution in a microcosm (alpha, not turnover) [17].
>
> H1-05:R-0063 [Reference list] Long-term mercury contamination does not affect the microbial gene potential for C and N cycling in soils but enhances detoxification gene abundance.
>

## turnover-ordering.12 (claim)

After aromatic pollution in a microcosm, taxonomic diversity fell and gene-pool diversity rose (alpha diversity, not turnover).

- conf: not stated
- class: not stated
- holds: a microcosm; alpha, not turnover; abstract only
- src: katoTimeseriesMetagenomicAnalysis2015 (AB)
- trail: H1-05 §Functional turnover reported lower

From the note:

> H1-05:B-0055 [1.2 Functional turnover reported lower than taxonomic] - Abstract-only reports: no fertilizer effect on functional profiles after 54 years despite taxonomic shifts [13]; stable functional potential across a 1 to 30 C peat incubation while taxonomy changed [14]; taxonomic differences "far greater" than SEED functional differences under tillage and rotation, with the two measured in different papers [18]; similar functional capacities in arid vs hyperarid saline drylands despite structural differences [24] [FT via agents, abstract and methods only closely read]; high Hg with little change in C and N genes but a significant shift in predicted-gene beta diversity [16]; taxonomic diversity falling and gene-pool diversity rising after aromatic pollution in a microcosm (alpha, not turnover) [17].
>

## turnover-ordering.13 (claim)

Fungal endemism with convergent enzyme activity across North America: a non-DNA case, indirect for DNA profiles.

- conf: not stated
- class: not stated
- holds: soil fungi across North America; measured enzyme activity, not DNA; abstract only
- src: talbotEndemismFunctionalConvergence2014 (AB)
- trail: H1-05 §Functional turnover reported lower

From the note:

> H1-05:B-0056 [1.2 Functional turnover reported lower than taxonomic] - Non-DNA function: fungal endemism with convergent enzyme activity across North America [21] [AB].
>
> H1-05:B-0057 [1.2 Functional turnover reported lower than taxonomic] This is a labelled non-DNA case and indirect for DNA profiles.
>

Not found in the cited text (where to look, not what is wrong): holds: soil; holds: fungi

## turnover-ordering.14 (claim)

With marker-inferred function, ZnO dose separated taxa but not PICRUSt-type predicted functions.

- conf: not stated
- class: deriv (marker)
- holds: soil polluted with nano ZnO, by dose; function inferred from the same 16S data, so not independent of taxonomy; abstract only
- src: dineshSoilPollutedNano2023 (AB; derived)
- trail: H1-05 §Functional turnover reported lower, §answers

From the note:

> H1-05:I-0005 [1.2 Functional turnover reported lower than taxonomic] - Marker-inferred function: ZnO dose separated taxa but not PICRUSt-type predicted functions [25] [AB; derived].
>
> H1-05:A-045 [quote: Answers as delivered] Soil PICRUSt2-inferred profiles are not independent of taxonomy, and such studies report either decoupling [25] or functional dissimilarity closer to phylogenetic than to taxonomic dissimilarity [26].
>
> H1-05:B-0058 [1.2 Functional turnover reported lower than taxonomic] Both infer function from the same 16S data, so they are not independent tests.
>
> H1-05:R-0084 [Reference list] Soil polluted with nano ZnO reveals unstable bacterial communities and decoupling of taxonomic and functional diversities.
>

## turnover-ordering.15 (claim)

Along an alpine gradient, PICRUSt2 function was redundant and tracked phylogenetic more than taxonomic dissimilarity.

- conf: not stated
- class: deriv (marker)
- holds: an alpine altitudinal gradient; function inferred from the same 16S data, so not independent of taxonomy
- src: liAsynchronousPatternsSoil2024 (FT via agents; derived)
- trail: H1-05 §Functional turnover reported lower, §answers

From the note:

> H1-05:I-0006 [1.2 Functional turnover reported lower than taxonomic] Along an alpine gradient, PICRUSt2 function was redundant and tracked phylogenetic more than taxonomic dissimilarity [26] [FT via agents; derived].
>
> H1-05:A-045 [quote: Answers as delivered] Soil PICRUSt2-inferred profiles are not independent of taxonomy, and such studies report either decoupling [25] or functional dissimilarity closer to phylogenetic than to taxonomic dissimilarity [26].
>
> H1-05:B-0058 [1.2 Functional turnover reported lower than taxonomic] Both infer function from the same 16S data, so they are not independent tests.
>
> H1-05:R-0086 [Reference list] Asynchronous patterns in soil bacterial diversity and functional potentials along an alpine altitudinal gradient.
>

## turnover-ordering.16 (claim)

After 14 years of moderate warming (0.8 to 2.0 C), 16S composition did not differ while GeoChip functional-gene composition did (Adonis, ANOSIM, MRPP, P < 0.05), with n = 4 per treatment; the authors conclude that functional potential is more sensitive than taxonomy. Plant and abiotic variables were unchanged, so the contrast was weak.

- conf: not stated
- class: meas (marker)
- holds: one long-term warming site in a Mediterranean-type grassland, n = 4 per treatment, GeoChip against 16S; n and the three tests checked by the critic
- src: gaoLongtermWarmingMediterraneantype2021 (FT, rechecked; measured)
- trail: H1-05 §Functional turnover reported higher, §answers, §critic

From the note:

> H1-05:I-0007 [1.3 Functional turnover reported higher or more responsive] - After 14 years of moderate warming (0.8 to 2.0 C), 16S composition did not differ, while GeoChip functional-gene composition did (Adonis, ANOSIM, MRPP, P < 0.05), with n = 4 per treatment [5] [FT, rechecked; measured].
>
> H1-05:B-0059 [1.3 Functional turnover reported higher or more responsive] The authors conclude that functional potential is more sensitive than taxonomy.
>
> H1-05:B-0060 [1.3 Functional turnover reported higher or more responsive] Plant and abiotic variables were unchanged, so the contrast was weak.
>
> H1-05:A-009 [quote: Answers as delivered] The reverse ordering (function responds where taxonomy does not) is reported under weak contrasts: 14 years of moderate warming (GeoChip [5]), erosion and deposition (GeoChip, abstract only [15]), and possibly an elevation gradient where functional distance decay was stronger (GeoChip; the reviewer's reading, not the authors' conclusion [6]).
>
> H1-05:A-021 [quote: Answers as delivered] Weak for the reverse ordering (n = 4 per treatment in [5]; platforms differ)..
>
> H1-05:C-033 [danger: Critic: answers partly supported] Most numbers checked against full text are reported accurately: Chen 2022 r2 0.2831, 44-99% vs 9-100%, t = 67.5, DistLM 16.3 vs 13.5%, 845 metagenomes; Fierer 2012 Mantel 0.76 and 0.82, 13-23% annotated; Leff rho 0.87; Igwe PERMANOVA R2 0.061/0.027 with residual df 19 vs 16; Gao n = 4 and the three tests; Xu dispersion pattern, with the ±30% decrease in function confirmed; Ulva envfit 0.70/0.17; Graco-Roza Mantel 0.254/0.115 and 13 deviating datasets (3 faster, 10 slower).
>
> H1-05:R-0042 [Reference list] Long-term warming in a Mediterranean-type grassland affects soil bacterial functional potential but not bacterial taxonomic composition. npj Biofilms and Microbiomes 2021;7(1):17. doi:10.1038/s41522-021-00187-7 [FT, rechecked] [6] Congcong Shen, Yu Shi, Yingying Ni, Ye Deng, Joy D. Van Nostrand, Zhili He, Jizhong Zhou, Haiyan Chu.
>

Not found in the cited text (where to look, not what is wrong): holds: site

## turnover-ordering.17 (claim)

Under aeolian erosion and deposition, soil nutrients correlated with functional but not taxonomic structure (Mantel).

- conf: not stated
- class: not stated
- holds: field simulation of aeolian soil erosion and deposition; GeoChip; abstract only
- src: maDivergentTaxonomicFunctional2017 (AB)
- trail: H1-05 §Functional turnover reported higher, §answers

From the note:

> H1-05:B-0061 [1.3 Functional turnover reported higher or more responsive] - Aeolian erosion and deposition: soil nutrients correlated with functional but not taxonomic structure (Mantel) [15] [AB].
>
> H1-05:A-009 [quote: Answers as delivered] The reverse ordering (function responds where taxonomy does not) is reported under weak contrasts: 14 years of moderate warming (GeoChip [5]), erosion and deposition (GeoChip, abstract only [15]), and possibly an elevation gradient where functional distance decay was stronger (GeoChip; the reviewer's reading, not the authors' conclusion [6]).
>
> H1-05:R-0061 [Reference list] Divergent taxonomic and functional responses of microbial communities to field simulation of aeolian soil erosion and deposition.
>

## turnover-ordering.18 (claim)

Along the Changbai elevation gradient, functional-gene distance decay (r = 0.708) was stronger than bacterial (r = 0.409) on the reviewer's reading; the authors describe the patterns as similar, with different drivers (pH for taxa, DOC for genes), and the two r values come from different platforms (16S against GeoChip) and are not on a common scale.

- conf: not stated
- class: reading (note: "This is my reading")
- holds: Changbai elevation gradient
- src: shenDramaticIncreasesSoil2016 (FT via agents)
- trail: H1-05 §Functional turnover reported higher, §answers

From the note:

> H1-05:B-0062 [1.3 Functional turnover reported higher or more responsive] - Changbai elevation gradient: functional-gene distance decay (r = 0.708) was stronger than bacterial (r = 0.409) [6] [FT via agents].
>
> H1-05:B-0063 [1.3 Functional turnover reported higher or more responsive] This is my reading.
>
> H1-05:B-0064 [1.3 Functional turnover reported higher or more responsive] The authors describe the patterns as similar, with different drivers (pH for taxa, DOC for genes).
>
> H1-05:B-0065 [1.3 Functional turnover reported higher or more responsive] The two r values come from different platforms (16S vs GeoChip) and are not on a common scale.
>
> H1-05:A-009 [quote: Answers as delivered] The reverse ordering (function responds where taxonomy does not) is reported under weak contrasts: 14 years of moderate warming (GeoChip [5]), erosion and deposition (GeoChip, abstract only [15]), and possibly an elevation gradient where functional distance decay was stronger (GeoChip; the reviewer's reading, not the authors' conclusion [6]).
>

## turnover-ordering.19 (claim)

Lower functional than taxonomic turnover is the most common reported ordering in soil but rests on weak comparisons: none of the 'function lower' soil studies compares the two turnovers on a common test with a null, and the single-site 'function lower' results mostly set a significant test against a non-significant one.

- conf: not stated
- class: not stated
- holds: soil, DNA-measured functional profiles
- src: chenFunctionalRedundancySoil2022, igweRedundancyMaintainsMicrobial2026, panImpactLongtermN2014, yangDecouplingMicrobialCommunity2021, souzaMetagenomicAnalysisReveals2015, saumasanchezFunctionalRedundancyBuffers2024
- rating: "Weak for the ordering"
- trail: H1-05 §answers, §critic

From the note:

> H1-05:A-003 [quote: Answers as delivered] Lower functional than taxonomic turnover is the most common reported ordering but rests on weak comparisons.
>
> H1-05:A-017 [quote: Answers as delivered] Weak for the ordering.
>
> H1-05:A-018 [quote: Answers as delivered] None of the 'function lower' soil studies compares the two turnovers on a common test with a null.
>
> H1-05:C-006 [danger: Critic: answers partly supported] Single-site 'function lower' results [4][13][14][18][24] mostly set a significant test against a non-significant one.
>

Not found in the cited text (where to look, not what is wrong): holds: dna-measured

## turnover-ordering.20 (claim)

The reverse ordering (function responds where taxonomy does not) is reported under weak contrasts and rests on two GeoChip studies from one group (one abstract only) plus a reviewer's reading of a third; removing the warming study would leave only the abstract-only study and that reading.

- conf: not stated
- class: not stated
- holds: 14 years of moderate warming (n = 4 per treatment), erosion and deposition, and possibly an elevation gradient; platforms differ; the critic: the power-asymmetry critique made against the serpentine study is not applied to the warming study (n = 4, significant functional against non-significant taxonomic)
- src: gaoLongtermWarmingMediterraneantype2021, maDivergentTaxonomicFunctional2017, shenDramaticIncreasesSoil2016
- rating: "Weak for the reverse ordering"
- contrary: one-sided (critic: C-093)
- trail: H1-05 §answers, §critic, §Adversarial critique

From the note:

> H1-05:A-004 [quote: Answers as delivered] The reverse ordering is reported under weak contrasts.
>
> H1-05:A-009 [quote: Answers as delivered] The reverse ordering (function responds where taxonomy does not) is reported under weak contrasts: 14 years of moderate warming (GeoChip [5]), erosion and deposition (GeoChip, abstract only [15]), and possibly an elevation gradient where functional distance decay was stronger (GeoChip; the reviewer's reading, not the authors' conclusion [6]).
>
> H1-05:A-021 [quote: Answers as delivered] Weak for the reverse ordering (n = 4 per treatment in [5]; platforms differ)..
>
> H1-05:A-034 [quote: Answers as delivered] Removing Gao et al. 2021 [5] would leave the reverse ordering supported only by an abstract-only study [15] and a reviewer's reading of [6].
>
> H1-05:C-007 [danger: Critic: answers partly supported] The reverse ordering rests on two GeoChip studies from one group [5][15] (one abstract only) plus a reviewer's reading of [6].
>
> H1-05:C-093 [warning: Adversarial critique, full findings] - The review scrutinises 'function lower' studies for lacking an averaging null, but it does not apply the same caution to 'function higher' GeoChip results [5][15].
>
> H1-05:C-094 [warning: Adversarial critique, full findings] GeoChip probes preselected known genes, whose detection depends on hybridisation thresholds, and it is set against 16S on a different platform.
>
> H1-05:C-095 [warning: Adversarial critique, full findings] The platform caveat is noted, but the power asymmetry critique made against [4] (significant vs non-significant test, n differences) is not applied to [5] (n = 4, significant functional vs non-significant taxonomic).
>
> H1-05:I-0004 [1.2 Functional turnover reported lower than taxonomic] - Serpentine vs non-serpentine pairs: bacterial composition differed (PERMANOVA R2 = 0.061, P = 0.004), eggNOG functional composition did not (R2 = 0.027, P = 0.391) [4] [FT, rechecked; measured].
>

## turnover-ordering.21 (claim)

In soil, function more responsive (the 14-year warming and erosion studies) is in conflict with function less responsive (the serpentine, fertilizer, peat, tillage and dryland studies), all at single sites or weak or moderate contrasts.

- conf: cont (note: "Conflicts: Soil: [5] and [15] (function more responsive) against")
- class: not stated
- holds: single sites or weak or moderate contrasts
- src: gaoLongtermWarmingMediterraneantype2021, maDivergentTaxonomicFunctional2017, igweRedundancyMaintainsMicrobial2026, panImpactLongtermN2014, yangDecouplingMicrobialCommunity2021, souzaMetagenomicAnalysisReveals2015, saumasanchezFunctionalRedundancyBuffers2024
- trail: H1-05 §answers

From the note:

> H1-05:A-022 [quote: Answers as delivered] *Conflicts:* Soil: [5] and [15] (function more responsive) against [4][13][14][18][24] (function less responsive), all at single sites or weak or moderate contrasts.
>
> H1-05:I-0007 [1.3 Functional turnover reported higher or more responsive] - After 14 years of moderate warming (0.8 to 2.0 C), 16S composition did not differ, while GeoChip functional-gene composition did (Adonis, ANOSIM, MRPP, P < 0.05), with n = 4 per treatment [5] [FT, rechecked; measured].
>
> H1-05:B-0061 [1.3 Functional turnover reported higher or more responsive] - Aeolian erosion and deposition: soil nutrients correlated with functional but not taxonomic structure (Mantel) [15] [AB].
>
> H1-05:I-0004 [1.2 Functional turnover reported lower than taxonomic] - Serpentine vs non-serpentine pairs: bacterial composition differed (PERMANOVA R2 = 0.061, P = 0.004), eggNOG functional composition did not (R2 = 0.027, P = 0.391) [4] [FT, rechecked; measured].
>
> H1-05:B-0055 [1.2 Functional turnover reported lower than taxonomic] - Abstract-only reports: no fertilizer effect on functional profiles after 54 years despite taxonomic shifts [13]; stable functional potential across a 1 to 30 C peat incubation while taxonomy changed [14]; taxonomic differences "far greater" than SEED functional differences under tillage and rotation, with the two measured in different papers [18]; similar functional capacities in arid vs hyperarid saline drylands despite structural differences [24] [FT via agents, abstract and methods only closely read]; high Hg with little change in C and N genes but a significant shift in predicted-gene beta diversity [16]; taxonomic diversity falling and gene-pool diversity rising after aromatic pollution in a microcosm (alpha, not turnover) [17].
>

## contrast-size.1 (claim)

No soil study was found that tests (or plots) how the functional-taxonomic gap scales with environmental distance; systematic comparisons across a graded range of environmental distances were not measured.

- conf: not stated
- class: search (note: "No soil study was found that tests how the functional-taxonomic gap scales with environmental distance")
- holds: soil
- src: none (a search result)
- search: searched, not found (note: "No soil study was found that tests how the functional-taxonomic gap scales with environmental distance")
- trail: H1-05 §answers, §Contrast size

From the note:

> H1-05:A-013 [quote: Answers as delivered] No soil study was found that tests how the functional-taxonomic gap scales with environmental distance.
>
> H1-05:A-026 [quote: Answers as delivered] Systematic comparisons across a graded range of environmental distances.
>
> H1-05:B-0066 [1.4 Contrast size] No soil study was found that plots the functional-taxonomic gap against environmental distance.
>

## contrast-size.2 (claim)

In a single-site precipitation experiment, ±30% precipitation slightly decreased and ±60% strongly increased within-treatment dispersion (PERMDISP) of taxa, genes, proteins and enzyme activities alike; gene, protein and enzyme dissimilarities were Mantel-correlated with taxonomic dissimilarity, and neither taxonomy nor function showed a directional PERMANOVA shift. The authors conclude that "taxonomic stochasticity translated into functional stochasticity", not redundancy.

- conf: not stated
- class: meas (marker)
- holds: one Eurasian steppe site under two magnitudes of precipitation change; within-treatment dispersion, not a comparison of the two turnovers' magnitudes, so indirect for the ordering question; the ±30% decrease in function confirmed by the critic
- src: xuDistinctivePatternMechanism2022 (FT, rechecked; measured)
- trail: H1-05 §Contrast size, §answers, §critic, §Adversarial critique

From the note:

> H1-05:I-0008 [1.4 Contrast size] The nearest is a single-site precipitation experiment [22] [FT, rechecked; measured].
>
> H1-05:B-0067 [1.4 Contrast size] There, ±30% precipitation slightly decreased and ±60% strongly increased within-treatment dispersion (PERMDISP) of taxa, genes, proteins and enzyme activities alike.
>
> H1-05:B-0068 [1.4 Contrast size] Gene, protein and enzyme dissimilarities were Mantel-correlated with taxonomic dissimilarity, and neither taxonomy nor function showed a directional PERMANOVA shift.
>
> H1-05:B-0069 [1.4 Contrast size] The authors conclude that "taxonomic stochasticity translated into functional stochasticity", not redundancy.
>
> H1-05:A-012 [quote: Answers as delivered] The one soil study that varied contrast size within a site [22] found that functional dispersion tracked taxonomic dispersion at both levels (a small decrease at ±30% precipitation, a large increase at ±60%) and did not find a change in ordering.
>
> H1-05:A-023 [quote: Answers as delivered] [22] finds function tracks taxonomy under both contrast sizes, while [7] finds taxonomic dissimilarity explains almost none of functional variation along a latitudinal gradient.
>
> H1-05:A-025 [quote: Answers as delivered] *Not measured:* Soil RNA (metatranscriptome) and protein (metaproteome) turnover comparisons, apart from [22] (metaproteome dispersion tracked taxonomy).
>
> H1-05:C-009 [danger: Critic: answers partly supported] [22] tests within-treatment dispersion under two magnitudes of precipitation change.
>
> H1-05:C-010 [danger: Critic: answers partly supported] Neither taxonomy nor function shifted directionally there, and the study does not compare the two turnovers' magnitudes, so it bears only indirectly on D1.
>
> H1-05:C-033 [danger: Critic: answers partly supported] Most numbers checked against full text are reported accurately: Chen 2022 r2 0.2831, 44-99% vs 9-100%, t = 67.5, DistLM 16.3 vs 13.5%, 845 metagenomes; Fierer 2012 Mantel 0.76 and 0.82, 13-23% annotated; Leff rho 0.87; Igwe PERMANOVA R2 0.061/0.027 with residual df 19 vs 16; Gao n = 4 and the three tests; Xu dispersion pattern, with the ±30% decrease in function confirmed; Ulva envfit 0.70/0.17; Graco-Roza Mantel 0.254/0.115 and 13 deviating datasets (3 faster, 10 slower).
>
> H1-05:C-040 [danger: Critic: answers partly supported] It measures within-treatment dispersion with no directional shift in either community, and it does not compare magnitudes, so it is indirect and should be labelled so.
>
> H1-05:R-0075 [Reference list] Distinctive pattern and mechanism of precipitation changes affecting soil microbial assemblages in the Eurasian steppe. iScience 2022;25(3):103893. doi:10.1016/j.isci.2022.103893 [FT, rechecked] [23] Haidong Gu, Zhuxiu Liu, Song Liu, Xiaojing Hu, Zhenhua Yu, Yansheng Li, Lujun Li, Yueyu Sui, Jian Jin, Xiaobing Liu, Zhongjun Jia, Lei Sun, Jonathan M Adams, Marcel G A van der Heijden, Junjie Liu, Guanghua Wang.
>

## contrast-size.3 (claim)

At weak single-site contrasts the ordering has gone both ways (function lower in the serpentine, 54-year fertilizer and tillage studies; function higher in the 14-year warming and erosion studies); cross-study comparison of contrast size is confounded by platform (GeoChip against shotgun), group, sample size and test, so no dependence on contrast size can be read off.

- conf: not stated
- class: not stated
- holds: soil; strong contrasts give covariation, weak single-site contrasts give both orderings
- src: igweRedundancyMaintainsMicrobial2026, panImpactLongtermN2014, souzaMetagenomicAnalysisReveals2015, gaoLongtermWarmingMediterraneantype2021, maDivergentTaxonomicFunctional2017
- trail: H1-05 §answers, §Contrast size, §critic

From the note:

> H1-05:A-005 [quote: Answers as delivered] No clean dependence on contrast size is established.**: Across soils, functional and taxonomic dissimilarity are usually positively correlated.
>
> H1-05:A-011 [quote: Answers as delivered] At weak single-site contrasts the ordering has gone both ways.
>
> H1-05:B-0071 [1.4 Contrast size] Weak single-site contrasts give both orderings: function lower in [4][13][18], function higher in [5][15].
>
> H1-05:B-0072 [1.4 Contrast size] Cross-study comparison of contrast size is confounded by platform, sample size and test.
>
> H1-05:C-008 [danger: Critic: answers partly supported] Platform (GeoChip vs shotgun), group and contrast size are confounded, so no dependence on contrast size can be read off.
>
> H1-05:I-0004 [1.2 Functional turnover reported lower than taxonomic] - Serpentine vs non-serpentine pairs: bacterial composition differed (PERMANOVA R2 = 0.061, P = 0.004), eggNOG functional composition did not (R2 = 0.027, P = 0.391) [4] [FT, rechecked; measured].
>
> H1-05:B-0055 [1.2 Functional turnover reported lower than taxonomic] - Abstract-only reports: no fertilizer effect on functional profiles after 54 years despite taxonomic shifts [13]; stable functional potential across a 1 to 30 C peat incubation while taxonomy changed [14]; taxonomic differences "far greater" than SEED functional differences under tillage and rotation, with the two measured in different papers [18]; similar functional capacities in arid vs hyperarid saline drylands despite structural differences [24] [FT via agents, abstract and methods only closely read]; high Hg with little change in C and N genes but a significant shift in predicted-gene beta diversity [16]; taxonomic diversity falling and gene-pool diversity rising after aromatic pollution in a microcosm (alpha, not turnover) [17].
>
> H1-05:I-0007 [1.3 Functional turnover reported higher or more responsive] - After 14 years of moderate warming (0.8 to 2.0 C), 16S composition did not differ, while GeoChip functional-gene composition did (Adonis, ANOSIM, MRPP, P < 0.05), with n = 4 per treatment [5] [FT, rechecked; measured].
>
> H1-05:B-0061 [1.3 Functional turnover reported higher or more responsive] - Aeolian erosion and deposition: soil nutrients correlated with functional but not taxonomic structure (Mantel) [15] [AB].
>

## contrast-size.4 (claim)

On the reviewer's synthesis, the reverse ordering appears only in GeoChip or single-site weak-contrast studies, so platform, contrast size and sample size are entangled; the magnitude comparison is the claim that most needs a null, and in soil it has none.

- conf: not stated
- class: reading (critic: C-103)
- holds: soil; mostly labelled as the reviewer's reading
- src: none (the reviewer's synthesis)
- trail: H1-05 §How the cases relate, §Adversarial critique

From the note:

> H1-05:B-0148 [5. How the cases relate] The magnitude comparison is the claim that most needs a null, and in soil it has none.
>
> H1-05:B-0149 [5. How the cases relate] The reverse ordering appears only in GeoChip or single-site weak-contrast studies, so platform, contrast size and sample size are entangled.
>
> H1-05:C-103 [warning: Adversarial critique, full findings] - Section 5 and the D1 conflicts note offer the reviewer's synthesis ('platform, contrast size and sample size are entangled', 'the magnitude comparison is the claim that most needs a null').
>
> H1-05:C-104 [warning: Adversarial critique, full findings] This is mostly labelled as the reviewer's reading.
>
> H1-05:C-105 [warning: Adversarial critique, full findings] It stays close to argument rather than literature finding, but does not evaluate a research design.
>

## contrast-size.5 (claim)

Along a latitudinal gradient, taxonomic dissimilarity explains almost none of functional variation, while in the precipitation experiment function tracks taxonomy under both contrast sizes: the review lists these as in conflict.

- conf: cont (note: "Conflicts:")
- class: not stated
- holds: a latitudinal forest gradient against one precipitation experiment
- src: zhangSoilBacterialEndemism2016, xuDistinctivePatternMechanism2022
- trail: H1-05 §answers

From the note:

> H1-05:A-023 [quote: Answers as delivered] [22] finds function tracks taxonomy under both contrast sizes, while [7] finds taxonomic dissimilarity explains almost none of functional variation along a latitudinal gradient.
>
> H1-05:A-022 [quote: Answers as delivered] *Conflicts:* Soil: [5] and [15] (function more responsive) against [4][13][14][18][24] (function less responsive), all at single sites or weak or moderate contrasts.
>
> H1-05:I-0008 [1.4 Contrast size] The nearest is a single-site precipitation experiment [22] [FT, rechecked; measured].
>
> H1-05:B-0051 [1.2 Functional turnover reported lower than taxonomic] - A latitudinal forest gradient in China: bacterial Bray-Curtis showed strong distance decay, while GeoChip function (summarized as DCA axes, not pairwise dissimilarity) was "highly convergent" [7] [FT via agents].
>

## chronosequence-precedents.1 (claim)

Over 143 years of grassland restoration, bacterial richness falls while SEED functional richness expands (alpha diversity; no paired turnover comparison).

- conf: not stated
- class: not stated
- holds: grassland restoration chronosequence; alpha, not turnover; the preprint's "profound functional decoupling" was softened to "a decoupling" in the published version
- src: goodallTaxonomicFilteringAccompanies2026 (FT via agents)
- trail: H1-05 §Nearest precedents, §answers, §Preprints and published versions

From the note:

> H1-05:B-0073 [1.5 Nearest precedents: chronosequences and within-site disturbance] Chronosequence papers report alpha diversity moving in opposite directions but no paired turnover comparison.
>
> H1-05:B-0074 [1.5 Nearest precedents: chronosequences and within-site disturbance] Examples: bacterial richness falls while SEED functional richness expands over 143 years of grassland restoration [9]; taxonomic diversity falls while C, N and P gene diversity rises along Swedish succession, with PICRUSt2 used for the redundancy analyses [10] [both FT via agents].
>
> H1-05:A-027 [quote: Answers as delivered] Chronosequences with a head-to-head beta comparison ([9][10] report alpha, not paired turnover).
>
> H1-05:B-0142 [4. Preprints and published versions] | Goodall et al. [9] | bioRxiv to ISME J 2026 | "profound functional decoupling" softened to "a decoupling"; driver taxa named differently |
>

## chronosequence-precedents.2 (claim)

Along Swedish succession, taxonomic diversity falls while C, N and P gene diversity rises, with PICRUSt2 used for the redundancy analyses (alpha diversity; no paired turnover comparison).

- conf: not stated
- class: not stated
- holds: Swedish successional chronosequence; alpha, not turnover; the preprint's "causal link" was softened to "the link" in the published version
- src: sveenFunctionalDiversitySoil2025 (FT via agents)
- trail: H1-05 §Nearest precedents, §answers, §Preprints and published versions

From the note:

> H1-05:B-0073 [1.5 Nearest precedents: chronosequences and within-site disturbance] Chronosequence papers report alpha diversity moving in opposite directions but no paired turnover comparison.
>
> H1-05:B-0074 [1.5 Nearest precedents: chronosequences and within-site disturbance] Examples: bacterial richness falls while SEED functional richness expands over 143 years of grassland restoration [9]; taxonomic diversity falls while C, N and P gene diversity rises along Swedish succession, with PICRUSt2 used for the redundancy analyses [10] [both FT via agents].
>
> H1-05:A-027 [quote: Answers as delivered] Chronosequences with a head-to-head beta comparison ([9][10] report alpha, not paired turnover).
>
> H1-05:B-0143 [4. Preprints and published versions] | Sveen et al. [10] | bioRxiv 2025 to Nat Commun 2025 | "causal link" softened to "the link" |
>

## chronosequence-precedents.3 (claim)

Global N-cycling pathway frequencies track habitat and soil C and N much better than the genera that encode them; this contrasts drivers, not turnovers, so it is indirect.

- conf: not stated
- class: not stated
- holds: global soils; N-cycling traits
- src: nelsonGlobalBiogeographyMicrobial2016 (FT via agents)
- trail: H1-05 §Nearest precedents

From the note:

> H1-05:B-0075 [1.5 Nearest precedents: chronosequences and within-site disturbance] Global N-cycling pathway frequencies track habitat and soil C and N much better than the genera that encode them [12] [FT via agents].
>
> H1-05:B-0076 [1.5 Nearest precedents: chronosequences and within-site disturbance] This is indirect, because it contrasts drivers, not turnovers.
>

## other-habitats.1 (claim)

On algal surfaces, taxonomic similarity was 15% against 70% COG similarity.

- conf: not stated
- class: not stated
- holds: algal surfaces; read via a fetch summary
- src: burkeBacterialCommunityAssembly2011 (secondary or abstract-level; critic: C-048 was "FT via fetch summary")
- trail: H1-05 §Other habitats, §answers

From the note:

> H1-05:B-0080 [1.6 Other habitats (reported separately)] - Algal surfaces: 15% taxonomic vs 70% COG similarity [35] [FT via fetch summary].
>
> H1-05:A-014 [quote: Answers as delivered] Other habitats (kept separate): marine and host-associated studies mostly report lower functional turnover, including under a strong 2000 km salinity contrast [36] and on algal surfaces [35], while a marine time series finds tight coupling [31].
>
> H1-05:C-048 [warning: Adversarial critique, full findings] A fetch summary is not a full-text reading, so these should be labelled secondary or abstract-level unless the text was read.
>

## other-habitats.2 (claim)

In the Ulva microbiome across a 2000 km, 5 to 35 PSU salinity gradient, salinity explained R2 = 0.70 of taxonomic and 0.17 of KO-based functional variation (envfit), although 23 KEGG modules still shifted: function stays lower under a strong contrast.

- conf: single (critic: C-062)
- class: not stated
- holds: Ulva microbiome; one study, MAG-based taxonomy; envfit figures checked by the critic; the only strong-contrast case outside soil; soil has not tested function lower at a strong contrast with a common metric
- src: vanderloosLowFunctionalChange2025 (FT, rechecked)
- trail: H1-05 §Other habitats, §answers, §critic, §Adversarial critique, §How the cases relate

From the note:

> H1-05:B-0081 [1.6 Other habitats (reported separately)] - Ulva microbiome across a 2000 km, 5 to 35 PSU salinity gradient: salinity explained R2 = 0.70 of taxonomic and 0.17 of KO-based functional variation (envfit), although 23 KEGG modules still shifted [36] [FT, rechecked].
>
> H1-05:A-014 [quote: Answers as delivered] Other habitats (kept separate): marine and host-associated studies mostly report lower functional turnover, including under a strong 2000 km salinity contrast [36] and on algal surfaces [35], while a marine time series finds tight coupling [31].
>
> H1-05:C-033 [danger: Critic: answers partly supported] Most numbers checked against full text are reported accurately: Chen 2022 r2 0.2831, 44-99% vs 9-100%, t = 67.5, DistLM 16.3 vs 13.5%, 845 metagenomes; Fierer 2012 Mantel 0.76 and 0.82, 13-23% annotated; Leff rho 0.87; Igwe PERMANOVA R2 0.061/0.027 with residual df 19 vs 16; Gao n = 4 and the three tests; Xu dispersion pattern, with the ±30% decrease in function confirmed; Ulva envfit 0.70/0.17; Graco-Roza Mantel 0.254/0.115 and 13 deviating datasets (3 faster, 10 slower).
>
> H1-05:C-062 [warning: Adversarial critique, full findings] - D1: 'Other habitats: marine and host-associated studies mostly report lower functional turnover' mixes FAPROTAX-derived [32], abstract-only [33] and a single time series [31]. The only strong-contrast case is [36] (single study, MAG-based taxonomy).
>
> H1-05:B-0150 [5. How the cases relate] Marine and algal studies extend "function lower" to a strong contrast [36], which soil has not tested with a common metric.
>

## other-habitats.3 (claim)

In a coastal Mediterranean time series, all-gene similarity tracked 16S similarity closely (R2 = 0.77); the authors reject strict redundancy.

- conf: not stated
- class: not stated
- holds: one marine time series; its full-text XML returned empty to the reviewer, so it rests on the agents' reading
- src: galandStrongLinkMarine2018 (FT via agents)
- trail: H1-05 §Other habitats, §answers, §Provenance

From the note:

> H1-05:B-0083 [1.6 Other habitats (reported separately)] - Coastal Mediterranean time series: all-gene similarity tracked 16S similarity closely (R2 = 0.77) [31] [FT via agents].
>
> H1-05:B-0084 [1.6 Other habitats (reported separately)] The authors reject strict redundancy.
>
> H1-05:A-014 [quote: Answers as delivered] Other habitats (kept separate): marine and host-associated studies mostly report lower functional turnover, including under a strong 2000 km salinity contrast [36] and on algal surfaces [35], while a marine time series finds tight coupling [31].
>
> H1-05:B-0019 [info: Provenance] Full-text XML for Fierer 2012 and Galand 2018 returned empty, so those rest on the agents' reading.
>

Not found in the cited text (where to look, not what is wrong): holds: its

## other-habitats.4 (claim)

In subsurface sediments, taxa CVs were about 10 times those of gene groups of similar mean abundance: taxa were about an order of magnitude more variable than gene groups at every KEGG level and EC, after abundance matching.

- conf: not stated
- class: not stated
- holds: Oregon coastal subsurface sediments
- src: soufiTaxonomicVariabilityFunctional2024 (FT via agents)
- trail: H1-05 §Other habitats, §answers

From the note:

> H1-05:B-0085 [1.6 Other habitats (reported separately)] - Subsurface sediments: taxa CVs about 10 times those of gene groups of similar mean abundance [37] [FT via agents].
>
> H1-05:A-049 [quote: Answers as delivered] In sediments, taxa were about an order of magnitude more variable than gene groups at every KEGG level and EC, after abundance matching [37].
>
> H1-05:R-0106 [Reference list] Taxonomic variability and functional stability across Oregon coastal subsurface microbiomes.
>

## other-habitats.5 (claim)

In bromeliads, functional-group structure was stable while within-group taxonomy varied.

- conf: not stated
- class: not stated
- holds: bromeliad communities; abstract only
- src: loucaHighTaxonomicVariability2016 (AB)
- trail: H1-05 §Other habitats

From the note:

> H1-05:B-0086 [1.6 Other habitats (reported separately)] - Bromeliads: stable functional-group structure with variable within-group taxonomy [33] [AB].
>

## other-habitats.6 (claim)

In the global ocean, with FAPROTAX (derived) functional groups, environment strongly shapes functional groups but weakly shapes within-group taxonomy.

- conf: not stated
- class: deriv (note: "Global ocean, FAPROTAX (derived)")
- holds: global ocean; FAPROTAX-derived function; abstract only
- src: loucaDecouplingFunctionTaxonomy2016 (AB)
- trail: H1-05 §Other habitats

From the note:

> H1-05:B-0087 [1.6 Other habitats (reported separately)] - Global ocean, FAPROTAX (derived): environment strongly shapes functional groups but weakly shapes within-group taxonomy [32] [AB].
>

## other-habitats.7 (claim)

During vermicomposting, PICRUSt2 turnover was about 12 times slower than taxonomic turnover.

- conf: not stated
- class: deriv (marker)
- holds: vermicomposting; PICRUSt2-inferred function
- src: airaFasterTurnoverTaxonomic2026 (FT via agents; derived)
- trail: H1-05 §Other habitats

From the note:

> H1-05:I-0009 [1.6 Other habitats (reported separately)] - Vermicomposting: PICRUSt2 turnover about 12 times slower than taxonomic turnover [45] [FT via agents; derived].
>

Not found in the cited text (where to look, not what is wrong): holds: picrust2-inferred

## other-habitats.8 (claim)

Across 148 trait datasets, mean Mantel r along space was 0.254 taxonomic against 0.115 functional, with about 31 of 148 datasets reversed.

- conf: not stated
- class: not stated
- holds: 148 datasets including diatoms and fungi but no bacteria, so not 'non-microbial'; Mantel values checked by the critic
- src: gracorozaDistanceDecay22022 (FT via agents)
- trail: H1-05 §Other habitats, §critic, §Adversarial critique

From the note:

> H1-05:B-0088 [1.6 Other habitats (reported separately)] - Non-microbial, 148 trait datasets: mean Mantel r along space 0.254 taxonomic vs 0.115 functional, with about 31 of 148 datasets reversed [48] [FT via agents].
>
> H1-05:C-011 [danger: Critic: answers partly supported] Evidence on non-soil systems: [48] includes diatoms and fungi but no bacteria, so it is not 'non-microbial'.
>
> H1-05:C-033 [danger: Critic: answers partly supported] Most numbers checked against full text are reported accurately: Chen 2022 r2 0.2831, 44-99% vs 9-100%, t = 67.5, DistLM 16.3 vs 13.5%, 845 metagenomes; Fierer 2012 Mantel 0.76 and 0.82, 13-23% annotated; Leff rho 0.87; Igwe PERMANOVA R2 0.061/0.027 with residual df 19 vs 16; Gao n = 4 and the three tests; Xu dispersion pattern, with the ±30% decrease in function confirmed; Ulva envfit 0.70/0.17; Graco-Roza Mantel 0.254/0.115 and 13 deviating datasets (3 faster, 10 slower).
>
> H1-05:C-055 [warning: Adversarial critique, full findings] - [48] is labelled 'FT via agents' but is openly available (PMC9322010). Its characterisation as 'non-microbial' is wrong: it includes diatoms and fungi (it lacks bacteria).
>
> H1-05:C-101 [warning: Adversarial critique, full findings] - [48] is labelled 'non-microbial' but includes diatoms and fungi. That blurs the microbial vs non-microbial split the review uses.
>

## other-habitats.9 (claim)

In European fish, functional beta diversity is below taxonomic, driven by turnover.

- conf: not stated
- class: not stated
- holds: European fish assemblages; abstract only
- src: villegerDecomposingFunctionalDiversity2013 (AB)
- trail: H1-05 §Other habitats

From the note:

> H1-05:B-0089 [1.6 Other habitats (reported separately)] European fish: functional beta below taxonomic, driven by turnover [50] [AB].
>

## other-habitats.10 (claim)

Yet in European fish, functional homogenization over time exceeded taxonomic homogenization six-fold.

- conf: not stated
- class: not stated
- holds: European fish assemblages; abstract only
- src: villegerFunctionalHomogenizationExceeds2014 (AB)
- trail: H1-05 §Other habitats

From the note:

> H1-05:B-0090 [1.6 Other habitats (reported separately)] Yet functional homogenization over time exceeded taxonomic homogenization six-fold [51] [AB].
>

Not found in the cited text (where to look, not what is wrong): European; holds: european

## other-habitats.11 (claim)

Outside soil, marine and host-associated studies report lower functional turnover, including under a strong 2000 km salinity contrast and on algal surfaces, while a marine time series finds tight coupling; this mixes FAPROTAX-derived, abstract-only and single-time-series evidence, and the only strong-contrast case is the Ulva study across 2000 km of salinity.

- conf: not stated
- class: not stated
- holds: marine and host-associated systems, kept separate from soil
- src: vanderloosLowFunctionalChange2025, burkeBacterialCommunityAssembly2011, galandStrongLinkMarine2018, loucaDecouplingFunctionTaxonomy2016, loucaHighTaxonomicVariability2016
- trail: H1-05 §answers, §Adversarial critique

From the note:

> H1-05:A-014 [quote: Answers as delivered] Other habitats (kept separate): marine and host-associated studies mostly report lower functional turnover, including under a strong 2000 km salinity contrast [36] and on algal surfaces [35], while a marine time series finds tight coupling [31].
>
> H1-05:C-062 [warning: Adversarial critique, full findings] - D1: 'Other habitats: marine and host-associated studies mostly report lower functional turnover' mixes FAPROTAX-derived [32], abstract-only [33] and a single time series [31]. The only strong-contrast case is [36] (single study, MAG-based taxonomy).
>
> H1-05:B-0081 [1.6 Other habitats (reported separately)] - Ulva microbiome across a 2000 km, 5 to 35 PSU salinity gradient: salinity explained R2 = 0.70 of taxonomic and 0.17 of KO-based functional variation (envfit), although 23 KEGG modules still shifted [36] [FT, rechecked].
>

Not found in the cited text (where to look, not what is wrong): holds: soil

## other-habitats.12 (claim)

Non-bacterial communities (148 datasets including diatoms and fungi; European fish) show lower functional decay on average, but with many reversals.

- conf: not stated
- class: not stated
- holds: non-bacterial communities
- src: gracorozaDistanceDecay22022, villegerDecomposingFunctionalDiversity2013, villegerFunctionalHomogenizationExceeds2014
- trail: H1-05 §answers, §critic

From the note:

> H1-05:A-015 [quote: Answers as delivered] Non-microbial communities show lower functional decay on average but with many reversals [48][50][51].
>
> H1-05:C-011 [danger: Critic: answers partly supported] Evidence on non-soil systems: [48] includes diatoms and fungi but no bacteria, so it is not 'non-microbial'.
>
> H1-05:B-0088 [1.6 Other habitats (reported separately)] - Non-microbial, 148 trait datasets: mean Mantel r along space 0.254 taxonomic vs 0.115 functional, with about 31 of 148 datasets reversed [48] [FT via agents].
>
> H1-05:B-0089 [1.6 Other habitats (reported separately)] European fish: functional beta below taxonomic, driven by turnover [50] [AB].
>

Not found in the cited text (where to look, not what is wrong): holds: non-bacterial

## unit-annotation-metric.1 (claim)

In the 845 pooled soil metagenomes, functional similarity exceeded taxonomic similarity at SEED levels 1 and 2 against all five taxonomic ranks, so the ordering did not reverse at any combination tested; the authors say coarser levels are more conserved, and state only that the ordering held at all levels. It is the only soil evidence on annotation level.

- conf: single (critic: C-012)
- class: not stated
- holds: 845 metagenomes (Chen 2022); SEED levels; rechecked by the reviewer
- src: chenFunctionalRedundancySoil2022 (FT, rechecked)
- trail: H1-05 §Dependence on unit, §answers, §critic

From the note:

> H1-05:B-0092 [2. Dependence on unit, annotation and metric (D2)] - **Annotation level.** In [3], functional similarity exceeded taxonomic similarity at SEED levels 1 and 2 against all five taxonomic ranks [FT, rechecked].
>
> H1-05:B-0093 [2. Dependence on unit, annotation and metric (D2)] The authors say coarser levels are more conserved.
>
> H1-05:A-037 [quote: Answers as delivered] Other habitats: the strength of coupling depends on the annotation scheme.**: Soil: one study reports the comparison at several annotation levels [3].
>
> H1-05:A-038 [quote: Answers as delivered] Functional similarity exceeded taxonomic similarity at SEED levels 1 and 2 against all five taxonomic ranks, so the gap widens as functions are aggregated.
>
> H1-05:A-063 [quote: Answers as delivered] *Single-source sensitivity:* Removing Chen et al. 2022 [3] leaves no soil evidence on annotation level.
>
> H1-05:C-013 [danger: Critic: answers partly supported] In [3], functional similarity exceeded taxonomic similarity at SEED levels 1 and 2 against all five taxonomic ranks.
>
> H1-05:C-014 [danger: Critic: answers partly supported] The ordering therefore did not reverse at any combination tested.
>
> H1-05:C-045 [danger: Critic: answers partly supported] Chen states only that the ordering held at all levels.
>
> H1-05:C-033 [danger: Critic: answers partly supported] Most numbers checked against full text are reported accurately: Chen 2022 r2 0.2831, 44-99% vs 9-100%, t = 67.5, DistLM 16.3 vs 13.5%, 845 metagenomes; Fierer 2012 Mantel 0.76 and 0.82, 13-23% annotated; Leff rho 0.87; Igwe PERMANOVA R2 0.061/0.027 with residual df 19 vs 16; Gao n = 4 and the three tests; Xu dispersion pattern, with the ±30% decrease in function confirmed; Ulva envfit 0.70/0.17; Graco-Roza Mantel 0.254/0.115 and 13 deviating datasets (3 faster, 10 slower).
>
> H1-05:I-0003 [1.1 Covariation at strong contrasts] In 845 pooled public soil metagenomes, pairwise functional and taxonomic Bray-Curtis similarities correlated (r2 = 0.2831) [3] [FT, rechecked by this reviewer; measured].
>
> H1-05:C-012 [danger: Critic: answers partly supported] - **D2, soil**: Single-study evidence only.
>

## unit-annotation-metric.2 (claim)

Finer functional units (KO, gene clusters) were not tested in that study, which explicitly chose SEED over KO, COG and NOG, so whether the ordering can reverse at fine resolution is open.

- conf: not stated
- class: not stated
- holds: the global pooled soil metagenomes
- src: chenFunctionalRedundancySoil2022
- trail: H1-05 §Dependence on unit, §answers, §critic

From the note:

> H1-05:A-039 [quote: Answers as delivered] Finer units (KO, gene clusters) were not tested there.
>
> H1-05:B-0094 [2. Dependence on unit, annotation and metric (D2)] Finer functional units (KO, gene clusters) were not tested, so whether the ordering can reverse at fine resolution is open.
>
> H1-05:C-016 [danger: Critic: answers partly supported] [3] explicitly chose SEED over KO, COG and NOG, so finer units were not tested.
>

Not found in the cited text (where to look, not what is wrong): holds: global; holds: soil

## unit-annotation-metric.3 (claim)

In one soil experiment, dissimilarity from all reads including unannotated ones (Mash) and from assembled genes gave within-treatment patterns similar to annotated-read dissimilarity, so in that case the annotation did not change the result.

- conf: single (critic: C-012)
- class: not stated
- holds: one Eurasian steppe precipitation experiment; within-treatment dispersion; rechecked by the reviewer
- src: xuDistinctivePatternMechanism2022 (FT, rechecked)
- trail: H1-05 §Dependence on unit, §answers, §critic, §Provenance

From the note:

> H1-05:B-0095 [2. Dependence on unit, annotation and metric (D2)] - **Annotated vs all reads.** In soil, [22] found that Mash all-read dissimilarity (including unannotated reads) and assembled-gene dissimilarity gave patterns similar to annotated-read dissimilarity [FT, rechecked].
>
> H1-05:A-040 [quote: Answers as delivered] In one soil experiment, dissimilarity from all reads including unannotated ones (Mash) and from assembled genes gave patterns similar to annotated-gene dissimilarity [22], so in that case the annotation did not change the result.
>
> H1-05:C-017 [danger: Critic: answers partly supported] [22] reports that Mash all-read and assembled-gene within-treatment dissimilarities patterned like annotated-read dissimilarity.
>
> H1-05:B-0018 [info: Provenance] Additions from this recheck: Igwe's site-pair R2 values, and Xu's Mash all-read result and PERMANOVA null.
>
> H1-05:R-0075 [Reference list] Distinctive pattern and mechanism of precipitation changes affecting soil microbial assemblages in the Eurasian steppe. iScience 2022;25(3):103893. doi:10.1016/j.isci.2022.103893 [FT, rechecked] [23] Haidong Gu, Zhuxiu Liu, Song Liu, Xiaojing Hu, Zhenhua Yu, Yansheng Li, Lujun Li, Yueyu Sui, Jian Jin, Xiaobing Liu, Zhongjun Jia, Lei Sun, Jonathan M Adams, Marcel G A van der Heijden, Junjie Liu, Guanghua Wang.
>
> H1-05:C-012 [danger: Critic: answers partly supported] - **D2, soil**: Single-study evidence only.
>

## unit-annotation-metric.4 (claim)

In a marine time series, the functional-taxonomic correlation fell from R2 0.77 (all genes) to 0.58 (KEGG) to 0.16 (FAPROTAX/PICRUSt, taxonomy-inferred functions): coupling strength depends on the annotation scheme. Removing this study removes the main direct evidence for that.

- conf: single (note: "single study")
- class: not stated
- holds: marine, one time series
- src: galandStrongLinkMarine2018 (full text, single study, marine)
- rating: "Moderate for the general point, outside soil, that annotation scheme changes the strength of coupling"
- trail: H1-05 §answers, §Dependence on unit, §critic

From the note:

> H1-05:A-048 [quote: Answers as delivered] Other habitats: in a marine time series, the functional-taxonomic correlation fell from R2 0.77 (all genes) to 0.58 (KEGG) to 0.16 (FAPROTAX/PICRUSt) [31].
>
> H1-05:A-054 [quote: Answers as delivered] Moderate for the general point, outside soil, that annotation scheme changes the strength of coupling (Galand [31], full text, single study, marine)..
>
> H1-05:A-064 [quote: Answers as delivered] Removing Galand et al. 2018 [31] removes the main direct evidence that annotation scheme changes coupling strength.
>
> H1-05:B-0096 [2. Dependence on unit, annotation and metric (D2)] In marine water, [31] found coupling strongest with all genes, weaker with KEGG (R2 0.58), and weakest with taxonomy-inferred functions (R2 0.16).
>
> H1-05:C-021 [danger: Critic: answers partly supported] Outside soil, [31] (marine, single study) shows coupling strength depends on the annotation scheme.
>

## unit-annotation-metric.5 (claim)

The marine time series finds that restricting to annotated genes weakens the coupling (all-read coupling is strongest), while the soil precipitation experiment finds all-read and annotated dissimilarity behave alike; the two use different measures (regression of similarities against within-treatment dispersion) and habitats, so they do not directly contradict.

- conf: not stated
- class: not stated
- holds: marine water against one soil experiment
- src: galandStrongLinkMarine2018, xuDistinctivePatternMechanism2022
- trail: H1-05 §answers, §Dependence on unit

From the note:

> H1-05:A-055 [quote: Answers as delivered] *Conflicts:* [31] finds that restricting to annotated genes weakens the coupling (all-read coupling is strongest), while [22] finds all-read and annotated dissimilarity behave alike in soil.
>
> H1-05:A-056 [quote: Answers as delivered] The two use different measures (regression of similarities vs within-treatment dispersion) and habitats, so they do not directly contradict.
>
> H1-05:B-0097 [2. Dependence on unit, annotation and metric (D2)] The two measure different things (dispersion vs a similarity regression).
>
> H1-05:I-0008 [1.4 Contrast size] The nearest is a single-site precipitation experiment [22] [FT, rechecked; measured].
>

Not found in the cited text (where to look, not what is wrong): holds: marine

## unit-annotation-metric.6 (claim)

Unknown-function genes are prevalent in fine-textured, higher-pH soils and are often mobile-element associated, so the unannotated fraction can vary along soil gradients (with soil properties): indirect support for an annotation-bias critique, not a demonstration of its effect on turnover.

- conf: not stated
- class: not stated
- holds: soils; a preprint, abstract only
- src: hollandmoritzEcologicalPerspectiveMicrobial2021 (AB; preprint)
- trail: H1-05 §Dependence on unit, §answers

From the note:

> H1-05:B-0098 [2. Dependence on unit, annotation and metric (D2)] Unknown-function genes are prevalent in fine-textured, higher-pH soils and are often mobile-element associated [27] [AB; preprint].
>
> H1-05:B-0099 [2. Dependence on unit, annotation and metric (D2)] So the unannotated fraction can vary along soil gradients: indirect support for an annotation-bias critique, not a demonstration of its effect on turnover.
>
> H1-05:A-047 [quote: Answers as delivered] The unannotated fraction varies with soil properties [27] (preprint, abstract only).
>

## unit-annotation-metric.7 (claim)

On the same 27 paired steppe and cropland soils, the dispersion-based analysis found KEGG gene assemblages homogenized in cropland at local and regional scales while bacterial taxa were homogenized only locally, whereas an earlier distance-decay-slope analysis of the same data had found greater KEGG functional turnover in cropland: the choice of turnover statistic changed the functional conclusion.

- conf: single (critic: C-063)
- class: not stated
- holds: 27 paired steppe and cropland soils; the only soil case where metric choice reversed a conclusion; rechecked by the reviewer
- src: guLandConversionCropland2025 (FT, rechecked)
- trail: H1-05 §Nearest precedents, §Dependence on unit, §answers, §critic

From the note:

> H1-05:B-0077 [1.5 Nearest precedents: chronosequences and within-site disturbance] On 27 paired steppe and cropland soils, the dispersion-based analysis found KEGG gene assemblages homogenized in cropland at local and regional scales, while bacterial taxa were homogenized only locally.
>
> H1-05:B-0078 [1.5 Nearest precedents: chronosequences and within-site disturbance] An earlier slope-based analysis of the same data had found greater functional turnover in cropland [23] [FT, rechecked].
>
> H1-05:B-0100 [2. Dependence on unit, annotation and metric (D2)] - **Metric or statistic.** On the same soils, distance-decay slopes and dispersion gave opposite functional conclusions [23].
>
> H1-05:A-041 [quote: Answers as delivered] The choice of turnover statistic changed the conclusion on the same 27 paired soils [23].
>
> H1-05:A-042 [quote: Answers as delivered] An earlier distance-decay-slope analysis found greater KEGG functional turnover in cropland, while dispersion found functional homogenization, and taxonomic homogenization differed by scale.
>
> H1-05:A-065 [quote: Answers as delivered] Removing Gu et al. 2025 [23] removes the only soil case where metric choice reversed a conclusion..
>
> H1-05:C-018 [danger: Critic: answers partly supported] [23] shows that the choice of statistic (distance-decay slope vs dispersion) changed the functional conclusion.
>
> H1-05:C-063 [warning: Adversarial critique, full findings] - D2: 'metric choice reversed the conclusion' rests on [23] alone. It is flagged in the sensitivity note but stated generally in Section 2.
>

## unit-annotation-metric.8 (claim)

No soil study compared Bray-Curtis with Aitchison or Jaccard (dissimilarity measures or transforms) for the functional-taxonomic ordering.

- conf: not stated
- class: search (note: "No soil study compared Bray-Curtis with Aitchison or Jaccard")
- holds: soil; searches by both agents (soil agent queries); the critic: compositional comparisons reported as not found without naming the routes
- src: none (a search result)
- search: searched, not found (note: "No soil study compared Bray-Curtis with Aitchison or Jaccard for the functional-taxonomic ordering (searches by both agents)")
- trail: H1-05 §Dependence on unit, §critic, §Provenance

From the note:

> H1-05:B-0101 [2. Dependence on unit, annotation and metric (D2)] No soil study compared Bray-Curtis with Aitchison or Jaccard for the functional-taxonomic ordering (searches by both agents).
>
> H1-05:C-020 [danger: Critic: answers partly supported] No soil study was found that compares dissimilarity measures or transforms for the ordering.
>
> H1-05:B-0020 [info: Provenance] Not found, with routes: field-soil null models on the functional-taxonomic difference (both agents' Europe PMC queries on soil with metagenome, GeoChip, null, shuffle, randomization, NST or betaNTI); soil comparisons across dissimilarity measures or KO/COG/gene-cluster units (soil agent queries); and relic-DNA, compositionality or sequencing-depth effects on the comparison (not searched in depth by either agent, so this absence is weakly established).
>
> H1-05:C-084 [warning: Adversarial critique, full findings] - gap: Sequencing depth and annotation-rate effects on functional-profile dissimilarity (for example the comparative-metagenomics normalization literature beyond Nayfach 2015) were not searched. Compositional (Aitchison, CLR) comparisons were reported as 'not found' without naming the routes used.; setting_or_class: shotgun functional profiles, methodological; direction: D2
>

## unit-annotation-metric.9 (claim)

For ectomycorrhizal fungi, turnover appeared at the level of gene sequence variants but not gene-family abundance.

- conf: not stated
- class: not stated
- holds: ectomycorrhizal fungal communities across a precipitation gradient; targeted gene families; abstract only
- src: pellitierPotentialFunctionalDivergence2024 (AB)
- trail: H1-05 §Dependence on unit, §answers

From the note:

> H1-05:B-0103 [2. Dependence on unit, annotation and metric (D2)] Ectomycorrhizal turnover appeared in gene sequence variants but not gene-family abundance [20] [AB].
>
> H1-05:A-043 [quote: Answers as delivered] For ectomycorrhizal fungi, turnover appeared at the level of gene sequence variants but not gene-family abundance [20] (abstract only).
>
> H1-05:A-028 [quote: Answers as delivered] Fungi-specific shotgun comparisons, beyond [20] (targeted gene families, abstract only)..
>
> H1-05:R-0071 [Reference list] Potential for functional divergence in ectomycorrhizal fungal communities across a precipitation gradient.
>

## unit-annotation-metric.10 (claim)

Within one grazing and P-addition grassland site, species-level resolution within functional groups gave strong taxon-function consistency (Procrustes) and removed an apparent decoupling; the authors attribute stable function to reciprocal changes in two dominant species rather than redundancy.

- conf: not stated
- class: not stated
- holds: one grassland site under grazing and P addition
- src: liuReciprocalChangesDominant2023 (FT via agents)
- trail: H1-05 §Nearest precedents, §Dependence on unit, §answers

From the note:

> H1-05:B-0079 [1.5 Nearest precedents: chronosequences and within-site disturbance] Within one grazing and P-addition site, species-level resolution within functional groups gave strong taxon-function consistency (Procrustes), and the authors attribute stable function to reciprocal changes in two dominant species rather than redundancy [11] [FT via agents].
>
> H1-05:B-0102 [2. Dependence on unit, annotation and metric (D2)] - **Taxonomic resolution.** Species-level resolution within functional groups removed apparent decoupling in [11].
>
> H1-05:A-044 [quote: Answers as delivered] Resolving taxa within functional groups at species level removed an apparent decoupling in one grassland [11].
>
> H1-05:A-071 [quote: Answers as delivered] One grassland study argues against redundancy, attributing apparent decoupling to reciprocal changes in dominant species [11].
>

## unit-annotation-metric.11 (claim)

In anaerobic digesters, taxonomic convergence depended on taxonomic rank: inoculum identity was recoverable at genus but less at phylum level.

- conf: not stated
- class: not stated
- holds: anaerobic digestion communities, outside soil; abstract only
- src: jourdainEnvironmentalSelectionConstrains2026 (AB)
- trail: H1-05 §answers, §Dependence on unit

From the note:

> H1-05:A-051 [quote: Answers as delivered] In anaerobic digesters, taxonomic convergence depended on taxonomic rank [44] (abstract only).
>
> H1-05:B-0104 [2. Dependence on unit, annotation and metric (D2)] Outside soil, inoculum identity was recoverable at genus but less at phylum level [44] [AB], and lake-enrichment redundancy was higher with EC than KO grouping [38] [FT via agents].
>

