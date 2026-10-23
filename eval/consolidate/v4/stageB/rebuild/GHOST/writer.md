# Positioning graph nodes that lack features: writer's view

> [!abstract] About this view
> What the research found, for writing from. Each claim gives who found it, the setting it holds for, the kind of evidence, its standing where the research stated one, and for an absence whether it was searched for. A claim with no standing given has none stated in the research; "limited by access" means a source was not read in full, which is not the same as weak evidence. Sources are listed at the end. The view is generated from the knowledge note `Positioning graph nodes that lack features.md`, where every claim is checked against the research.

## What the research found, by question

### GHOST

**D1. In methods that represent graphs by combining node features with graph structure (feature based graph embedding, graph neural networks, attribute aware dimensionality reduction, and network layout), how are nodes that have no features handled when a subset of nodes is featureless, cold start, or only partially attributed? What are the measured effects on downstream tasks (node classification, clustering, link prediction, and visual layout distortion) of each handling strategy, and under what graph regimes does each succeed or fail?**

*Answer, as the research gave it; not checked by a second reader.* **Verdict**

**(c) Regime-dependent — with neighbour feature propagation a defensible default *only* in the homophilous, sparse-feature regime where its robustness has actually been demonstrated.** The single most replicated empirical result is that diffusion/propagation imputation (Feature Propagation and variants) reconstructs entirely-missing node features from observed neighbours and degrades only marginally — ~2–4% relative node-classification accuracy at 99% missing — while model-internal imputation (GCNMF) collapses to ~35% on the same benchmark [R1, R2, R3]. That looks like a clean win for option (a). It is not, for three reasons that the verification surfaced and confirmed: 1. **The robustness numbers are regime-bound.** They are measured almost entirely on homophilous, sparse bag-of-words citation/co-purchase graphs (Cora, Citeseer, PubMed, Photo) under Missing-Completely-At-Random missingness, and many are self-reported by the method authors [R1, R2, R4]. 2. **A 2026 result proves the benchmark itself hides the differences.** High feature sparsity provably bounds the information loss from missingness, "making all models appear robust and preventing a meaningful comparison" — so the dominance of propagation on standard benchmarks may be an artifact, not a regime-general property [R7]. 3. **Propagation has a proven systematic defect.** It produces low-variance channels that contribute little downstream — established with empirical evidence *and* a theoretical proof, and independently corroborated at a second venue [R5, R6]. So propagation is the right default where the graph is homophilous and features are sparse; outside that regime the evidence does not support it as a default, and structure-only / positional embedding (option b) becomes a live alternative whose performance is itself strongly regime-dependent with no single winner [R8, R9, R10]. **The two questions the brief cared about most are unanswered by the literature** (see *Open Questions*): no controlled benchmark measures whether imputed/structure-only nodes *contaminate* the clusters of feature-bearing nodes, and none measures layout distortion on mixed populations. Report this as "no controlled evidence found," not as a point in favour of any option.

*Answer, as the research gave it; not checked by a second reader.* **Open Questions (unanswered by the literature)**

1. **Contamination (brief item 3):** does inserting imputed/structure-only nodes measurably distort feature-bearing nodes' clusters? No controlled mixed-population benchmark found. 2. **Layout distortion (brief item 4):** centroid piling / hub collapse on mixed populations — unmeasured in the retrieved corpus. 3. **Dense + non-MCAR regimes:** does propagation robustness survive on dense, semantically meaningful features and structural/feature-dependent (MNAR) missingness? Ferrini et al. argue standard benchmarks cannot answer this and introduce new protocols, but cross-method results are not yet established [R7]. 4. **Crossover point:** at what featureless fraction / graph sparsity does neighbour aggregation become too sparse to help and lose to structure-only embedding? Degradation is quantified within propagation but never located against structure-only baselines across regimes.

## Concepts

In an order where each concept comes after the ones it builds on; the order means nothing more.

### Graph nodes that carry edges but lack feature vectors

- The literature on handling graph nodes that carry edges but lack feature vectors splits into two families plus a model-internal approach; the review describes neighbour feature propagation (diffusion imputation), model-internal imputation, structure-only/positional embedding, and dynamic/joint reconstruction. (the reviewer's synthesis)
  Holds for: the published literature on graph nodes that carry edges but lack feature vectors, as the review groups it.
- "Existing graph learning methods including the popular GNN cannot provide satisfied learning performance since they are not specified for attribute-missing graphs." (Chen et al. 2022)
  Holds for: attribute-missing graphs; quoted from Chen et al. (2022).

### Homophilous and heterophilous graphs

- In a homophilous graph connected nodes tend to share class labels and features; under heterophily (low homophily) connected nodes may have different class labels and dissimilar features. (Zhu et al. 2020)
  Background, not from the research.

### Mechanisms of missingness (MCAR, MNAR)

- Values are missing completely at random (MCAR) when the probability that a value is missing depends on neither the observed nor the missing values; missingness that depends on the missing values themselves is missing not at random (MNAR). (Little and Rubin 2019)
  Background, not from the research.

### The sources the review rests on

- Several key sources the review rests on are 2025–2026 preprints or under review, at high-quality venues but not all finalised. (Um et al. 2025; Anonymous 2025; Ferrini et al. 2026)
  Holds for: the sources the note numbers R5, R6 and R7 (Um et al. 2025; the anonymous 2025 low-variance paper; Ferrini et al. 2026).

### Neighbour feature propagation (diffusion imputation)

Builds on: Graph nodes that carry edges but lack feature vectors, Homophilous and heterophilous graphs.

- Feature Propagation (FP) minimises Dirichlet energy, giving a diffusion-type PDE on the graph whose discretisation reconstructs missing features from observed neighbours: a simple, fast, scalable algorithm. (Rossi et al. 2022)
  Holds for: graphs whose nodes have missing features.
  Evidence: rated "Confidence: high (3-0)" by the research.
- Feature Propagation is the graph/diffusion instance of recovering structure under missing high-dimensional data. (the reviewer's framing; no source cited)
  Holds for: the review's framing, linked to the vault note on missing-data imputation.
- Feature Propagation's motivating setting is explicitly the partially-attributed, cold-start case ("age and gender available only for a small subset of users"). (Rossi et al. 2022)
  Holds for: the setting Rossi et al. (2022) motivate FP with.
  Evidence: rated "Confidence: high (3-0)" by the research.
- Feature Propagation rests on a feature-homophily assumption and degrades on heterophilous graphs. (Rossi et al. 2022)
  Holds for: heterophilous graphs; given as a caveat of Rossi et al. (2022).
- Feature Propagation outperformed prior missing-feature methods on seven benchmarks; this is a 2022 historical fact, not current state of the art. (Rossi et al. 2022)
  Holds for: the seven benchmarks of Rossi et al. (2022); homophilous, sparse, MCAR benchmarks, mostly author-reported; a 2022 result.
- Feature Propagation is now a baseline, superseded as state of the art by PCFI, DART and others. (the reviewer's statement; no source cited)
  Holds for: the field at the time of the review.
- Propagation produces low-variance, near-constant channels that contribute little downstream; this is established with empirical evidence and a theoretical proof, and independently corroborated at a second venue. (Um et al. 2025; Anonymous 2025)
  Holds for: propagation-based feature imputation; both sources are 2025 papers among the note's preprints or under-review sources.
  Evidence: measured and derived; replicated; rated "proven" by the research.
- The low-variance defect bounds propagation but does not refute it: the high-variance channels do the work. (the reviewer's reading of the low-variance finding)
  Holds for: propagation-based feature imputation.

### Model-internal imputation (GCNMF)

Builds on: Graph nodes that carry edges but lack feature vectors.

- GCNMF folds Gaussian-mixture imputation inside a GCN. (Chen et al. 2022)
  Holds for: graphs with missing node features.
- Model-internal imputation is the strategy that fails badly under high missingness. (the reviewer's summary of the high-missingness figures)
  Holds for: high missingness.

### Dynamic or joint reconstruction of attributes and structure

Builds on: Graph nodes that carry edges but lack feature vectors.

- "Attribute-missing graph" methods jointly reconstruct attributes and update structure via alternating optimisation (EGS), rather than imputing a fixed mean or zero on a static graph. (Chen et al. 2022; Song et al. 2025)
  Holds for: attribute-missing graphs.
  Evidence: rated "Confidence: high (3-0 / 2-1)" by the research.

### Structure-only (positional) embedding

Builds on: Graph nodes that carry edges but lack feature vectors.

- A distinct family of methods consumes only topology (LLE, Laplacian Eigenmaps, Graph Factorisation, GraRep, HOPE, DeepWalk, node2vec, SDNE, DNGR, LINE), operating on adjacency or similarity matrices; attribute-joint methods are treated as a separate, newer line. (Goyal and Ferrara 2018)
  Holds for: the classical methods of a 2018 survey.
  Evidence: rated "Confidence: high (3-0)" by the research.
- The structure-only taxonomy rests on a 2018 survey; its topology-only characterisation of those classical methods remains accurate, but the field has expanded since. (Goyal and Ferrara 2018)
  Holds for: the classical structure-only methods; a 2018 survey.
- Structure-only embeddings are regime-dependent with no single winner, though higher-order-proximity methods generally win. (Goyal and Ferrara 2018)
  Holds for: the structure-only methods compared in a 2018 survey.
- node2vec leads on node classification yet loses on a structured SBM graph where labels reflect communities and there is no structural equivalence between nodes. (Goyal and Ferrara 2018)
  Holds for: node classification, and a structured SBM graph with community labels and no structural equivalence; from a 2018 survey.

### Positional and structural node representations

Builds on: Structure-only (positional) embedding.

- GNNs cannot capture position when node features are absent or identical: structurally isomorphic but positionally distinct nodes get identical embeddings, which is strictly true in the featureless or identical-feature regime. (You et al. 2019)
  Holds for: GNNs with absent or identical node features.
- Positional embeddings are formally samples from a G-equivariant distribution whose expectation is the structural representation; this formal sampling relationship and its directionality (positional = samples of structural) survived verification. (Srinivasan and Ribeiro 2020)
  Holds for: the formal relationship between positional embeddings and structural representations, not their interchangeability for tasks.
  Evidence: derived.

### The benchmark regime (homophilous, sparse, MCAR)

Builds on: Graph nodes that carry edges but lack feature vectors, Homophilous and heterophilous graphs, Mechanisms of missingness (MCAR, MNAR), Neighbour feature propagation (diffusion imputation).

- The robustness numbers for imputing missing node features are measured almost entirely on homophilous, sparse bag-of-words citation and co-purchase graphs (Cora, Citeseer, PubMed, Photo) under Missing-Completely-At-Random missingness, and many are self-reported by the method authors. (Rossi et al. 2022; Lei et al. 2023; Song et al. 2025)
  Holds for: the robustness figures of Rossi et al. (2022), Lei et al. (2023) and Song et al. (2025).
- High feature sparsity provably bounds the information loss from missingness, "making all models appear robust and preventing a meaningful comparison": on standard benchmarks all models look robust and cannot be distinguished. (Ferrini et al. 2026)
  Holds for: standard benchmarks with high feature sparsity; a 2026 result, under review.
  Evidence: derived; rated "proven" by the research.
- The dominance of propagation on standard benchmarks may therefore be an artifact, not a regime-general property. (Ferrini et al. 2026)
  Holds for: standard benchmarks with high feature sparsity.
- Dense-feature and non-MCAR (MNAR) regimes are under-evaluated. (Ferrini et al. 2026)
  Holds for: evaluation of methods for missing node features.
- Ferrini et al. argue that standard benchmarks cannot answer whether propagation's robustness survives on dense, semantically meaningful features and structural or feature-dependent (MNAR) missingness, and introduce new protocols, but cross-method results are not yet established. (Ferrini et al. 2026)
  Holds for: dense features and MNAR missingness.

### Degradation as the featureless fraction rises

Builds on: Neighbour feature propagation (diffusion imputation), Model-internal imputation (GCNMF), Dynamic or joint reconstruction of attributes and structure, Structure-only (positional) embedding, The benchmark regime (homophilous, sparse, MCAR).

- Diffusion/propagation imputation (Feature Propagation and variants) reconstructs entirely-missing node features from observed neighbours and degrades only marginally, about 2–4% relative node-classification accuracy at 99% missing, while model-internal imputation (GCNMF) collapses to about 35% on the same benchmark. (Rossi et al. 2022; Lei et al. 2023; Chen et al. 2022)
  Holds for: homophilous, sparse bag-of-words citation and co-purchase graphs (Cora, Citeseer, PubMed, Photo) under Missing-Completely-At-Random missingness, many figures self-reported by the method authors; the 2–4% range is the note's, across Feature Propagation and its variants; the unscoped version was killed in verification.
  Evidence: measured; replicated.
- Feature Propagation loses on average about 4% relative node-classification accuracy at 99% missing across seven benchmarks. (Rossi et al. 2022)
  Holds for: seven benchmarks, 99% of node features missing; homophilous, sparse, MCAR, mostly author-reported.
  Evidence: measured.
- SGHFP, a hypergraph variant of feature propagation, loses on average 2.67% relative accuracy at 99% missing across four datasets. (Lei et al. 2023)
  Holds for: four datasets, 99% missing; homophilous, sparse, MCAR, mostly author-reported.
  Evidence: measured; rated "Confidence: high (3-0)" by the research.
- Per dataset at 99% missing, SGHFP goes from 81.23 to 79.41 on Cora (−2.25%), from 91.73 to 87.73 on Photo (−4.36%, the worst case) and from 77.36 to 74.29 on PubMed (−3.97%). (Lei et al. 2023)
  Holds for: Cora, Photo and PubMed, 99% missing, from Table 2 of Lei et al. (2023); homophilous, sparse, MCAR, mostly author-reported.
  Evidence: measured; rated "Confidence: high (3-0)" by the research.
- At 99% missing on Cora, propagation sits at about 78–79%. (Rossi et al. 2022; Lei et al. 2023)
  Holds for: Cora, 99% missing; homophilous, sparse, MCAR, mostly author-reported.
  Evidence: measured; rated "Confidence: high (3-0 / 2-1)" by the research.
- At 99% missing on Cora, GCNMF scores 34.54%, a figure confirmed by two independent papers. (Rossi et al. 2022; Lei et al. 2023)
  Holds for: Cora, 99% missing; homophilous, sparse, MCAR, mostly author-reported.
  Evidence: measured; replicated; rated "Confidence: high (3-0 / 2-1)" by the research.
- At 99% missing on Cora, PaGNN sits at about 58%: low, but not the catastrophic collapse of GCNMF. (Chen et al. 2022)
  Holds for: Cora, 99% missing; homophilous, sparse, MCAR, mostly author-reported.
  Evidence: measured; rated "Confidence: high (3-0 / 2-1)" by the research.
- EGS degrades gently against a PAGNN baseline on Cora from 5% to 75% missing (baseline 81.36 to 74.05; EGS 84.77 to 82.13). (Song et al. 2025)
  Holds for: Cora, 5% to 75% missing; self-reported by the method's authors; homophilous, sparse, MCAR.
  Evidence: rated "Confidence: high" by the research.
- Degradation is quantified within propagation but never located against structure-only baselines across regimes. (an absence in the reviewed literature)
  Holds for: the featureless fraction or graph sparsity at which neighbour aggregation would lose to structure-only embedding.
  Evidence: a search result.
  The research does not say whether this was searched for.

### Contamination of feature-bearing nodes

Builds on: Neighbour feature propagation (diffusion imputation), Dynamic or joint reconstruction of attributes and structure, Structure-only (positional) embedding.

- No controlled benchmark measures whether imputed or structure-only nodes contaminate the clusters of feature-bearing nodes: no controlled head-to-head and no controlled mixed-population benchmark was found. (an absence: no source measured it)
  Holds for: mixed populations of feature-bearing and imputed or structure-only nodes (brief item 3).
  Evidence: a search result.
  Searched for and not found.
- Song et al. argue, by molecular-graph analogy, that severe missingness "can alter the semantic information of the graph, leading to changes in the graph structure", which is why they update structure jointly; this is a theoretical, motivational statement, not a measured demonstration that featureless nodes distort feature-bearing nodes' clusters. (Song et al. 2025)
  Holds for: indirect and motivational support only, by molecular-graph analogy.
  Evidence: asserted; rated "verification vote 2-1" by the research.

### Layout distortion on mixed populations

Builds on: Structure-only (positional) embedding, Positional and structural node representations.

- No reviewed source measured layout distortion on mixed populations: the visualization search angle returned sources, but none yielded a confirmed claim tying topology-only node placement to distortion artifacts (centroid piling, hub collapse) on mixed attributed and featureless populations. (an absence: no source measured it)
  Holds for: topology-only node placement on mixed attributed and featureless populations (brief item 4).
  Evidence: a search result.
  Searched for and not found.
- The strategy of laying out topology separately and then mapping it onto attribute space surfaced only as the conceptual positional-vs-structural distinction, not as a benchmarked layout pipeline. (Srinivasan and Ribeiro 2020; You et al. 2019)
  Holds for: the strategy as named in the brief.
  Evidence: a search result.
  Searched for and not found.

### Which strategy is a defensible default

Builds on: Degradation as the featureless fraction rises, The benchmark regime (homophilous, sparse, MCAR), Neighbour feature propagation (diffusion imputation), Structure-only (positional) embedding, Contamination of feature-bearing nodes, Layout distortion on mixed populations.

- The answer is regime-dependent: neighbour feature propagation is a defensible default only in the homophilous, sparse-feature regime where its robustness has actually been demonstrated. (the review's verdict)
  Holds for: the review's verdict (c).
  The research does not say whether contrary evidence was searched for.
- Propagation's marginal degradation, against the collapse of model-internal imputation, looks like a clean win for option (a), but it is not, for three reasons the verification surfaced and confirmed: the robustness numbers are regime-bound, a 2026 result proves the benchmark itself hides the differences, and propagation has a proven low-variance defect. (the review's verdict)
  Holds for: the review's verdict on option (a).
  The research does not say whether contrary evidence was searched for.
- Propagation is the right default where the graph is homophilous and features are sparse; outside that regime the evidence does not support it as a default, and structure-only or positional embedding becomes a live alternative whose performance is itself strongly regime-dependent with no single winner. (Goyal and Ferrara 2018; Srinivasan and Ribeiro 2020; You et al. 2019)
  Holds for: the review's verdict; structure-only or positional embedding is option (b).
  The research does not say whether contrary evidence was searched for.

## Do not say

Wordings the research itself says are wrong or overstated, each with the reason and what to say instead.

- Do not write: "Feature Propagation's robustness, about 4% loss at 99% missing features, is a general fact."
  Why: This unscoped claim was killed in verification (vote 1-2); only the version scoped to homophilous, sparse, MCAR benchmarks survives.
  Say instead: Diffusion/propagation imputation (Feature Propagation and variants) reconstructs entirely-missing node features from observed neighbours and degrades only marginally, about 2–4% relative node-classification accuracy at 99% missing, while model-internal imputation (GCNMF) collapses to about 35% on the same benchmark. (Rossi et al. 2022; Lei et al. 2023; Chen et al. 2022)
  Holds for: homophilous, sparse bag-of-words citation and co-purchase graphs (Cora, Citeseer, PubMed, Photo) under Missing-Completely-At-Random missingness, many figures self-reported by the method authors; the 2–4% range is the note's, across Feature Propagation and its variants; the unscoped version was killed in verification.
  Evidence: measured; replicated.
  Say instead: Feature Propagation loses on average about 4% relative node-classification accuracy at 99% missing across seven benchmarks. (Rossi et al. 2022)
  Holds for: seven benchmarks, 99% of node features missing; homophilous, sparse, MCAR, mostly author-reported.
  Evidence: measured.
- Do not write: "Positional and structural representations are practically interchangeable for tasks."
  Why: This was killed in verification (vote 0-3); only the formal sampling relationship and its directionality (positional embeddings are samples of the structural representation) survived.
  Say instead: Positional embeddings are formally samples from a G-equivariant distribution whose expectation is the structural representation; this formal sampling relationship and its directionality (positional = samples of structural) survived verification. (Srinivasan and Ribeiro 2020)
  Holds for: the formal relationship between positional embeddings and structural representations, not their interchangeability for tasks.
  Evidence: derived.
- Do not write: "Song et al. showed that featureless nodes distort the clusters of feature-bearing nodes."
  Why: Song et al.'s statement is theoretical and motivational, argued by molecular-graph analogy (verification vote 2-1), not a measured demonstration, and the note says to cite it as indirect only.
  Say instead: No controlled benchmark measures whether imputed or structure-only nodes contaminate the clusters of feature-bearing nodes: no controlled head-to-head and no controlled mixed-population benchmark was found. (an absence: no source measured it)
  Holds for: mixed populations of feature-bearing and imputed or structure-only nodes (brief item 3).
  Evidence: a search result.
  Searched for and not found.
  Say instead: Song et al. argue, by molecular-graph analogy, that severe missingness "can alter the semantic information of the graph, leading to changes in the graph structure", which is why they update structure jointly; this is a theoretical, motivational statement, not a measured demonstration that featureless nodes distort feature-bearing nodes' clusters. (Song et al. 2025)
  Holds for: indirect and motivational support only, by molecular-graph analogy.
  Evidence: asserted; rated "verification vote 2-1" by the research.
- Do not write: "The absence of evidence on contamination and layout distortion counts in favour of one of the options."
  Why: The note says to report the two unanswered questions as "no controlled evidence found", not as a point in favour of any option.
  Say instead: No controlled benchmark measures whether imputed or structure-only nodes contaminate the clusters of feature-bearing nodes: no controlled head-to-head and no controlled mixed-population benchmark was found. (an absence: no source measured it)
  Holds for: mixed populations of feature-bearing and imputed or structure-only nodes (brief item 3).
  Evidence: a search result.
  Searched for and not found.
  Say instead: No reviewed source measured layout distortion on mixed populations: the visualization search angle returned sources, but none yielded a confirmed claim tying topology-only node placement to distortion artifacts (centroid piling, hub collapse) on mixed attributed and featureless populations. (an absence: no source measured it)
  Holds for: topology-only node placement on mixed attributed and featureless populations (brief item 4).
  Evidence: a search result.
  Searched for and not found.
- Do not write: "Feature Propagation outperforms previous methods and is the state of the art for missing node features."
  Why: That Feature Propagation outperforms previous methods is a 2022 historical fact, not current state of the art; it is now a baseline, superseded by PCFI, DART and others.
  Say instead: Feature Propagation outperformed prior missing-feature methods on seven benchmarks; this is a 2022 historical fact, not current state of the art. (Rossi et al. 2022)
  Holds for: the seven benchmarks of Rossi et al. (2022); homophilous, sparse, MCAR benchmarks, mostly author-reported; a 2022 result.
  Say instead: Feature Propagation is now a baseline, superseded as state of the art by PCFI, DART and others. (the reviewer's statement; no source cited)
  Holds for: the field at the time of the review.

## Gaps

What the research did not establish.

- The review's findings were never checked by a second reader: the figures its answers rest on (propagation's 2–4% relative accuracy loss at 99% missing, GCNMF's collapse to about 35% on the same benchmark, the sparsity bound on information loss and the low-variance defect) went through the harness's own 3-vote verification only, and the note records only its refutations.
  The research does not say whether this was searched for.
- Does inserting imputed or structure-only nodes measurably distort the clusters of feature-bearing nodes?
  Searched for and not found.
- Layout distortion (centroid piling, hub collapse) on mixed populations of attributed and featureless nodes.
  Searched for and not found.
- Does propagation's robustness survive on dense, semantically meaningful features and on structural or feature-dependent (MNAR) missingness? (Ferrini et al. 2026)
  The research does not say whether this was searched for.
- At what featureless fraction or graph sparsity does neighbour aggregation become too sparse to help and lose to structure-only embedding?
  The research does not say whether this was searched for.

## References

- Anonymous (2025). Low Variance: A Bottleneck in Diffusion-Based Graph Imputation. ICLR 2025 track. https://openreview.net/forum?id=4dhTYe5pjD
- Chen, X.; Chen, S.; Yao, J.; Zheng, H.; Zhang, Y.; Tsang, I. W. (2022). Learning on Attribute-Missing Graphs. IEEE Transactions on Pattern Analysis and Machine Intelligence 44(2): 740--757. https://doi.org/10.1109/TPAMI.2020.3032189
- Ferrini, F.; Lachi, V.; Longa, A.; Lepri, B.; Akiyoshi; Passerini, A.; Liu; Jaeger; others (2026). Rethinking GNNs and Missing Features: Challenges, Evaluation and a Robust Solution. https://arxiv.org/abs/2601.04855
- Goyal, P.; Ferrara, E. (2018). Graph Embedding Techniques, Applications, and Performance: A Survey. Knowledge-Based Systems 151: 78--94. https://doi.org/10.1016/j.knosys.2018.03.022
- Lei, C.; Fu, J.; Wang, X.; Qiu, X.; Hu, Z.; Peng, Y.; You, J. (2023). Self-supervised Guided Hypergraph Feature Propagation for Semi-supervised Classification with Missing Node Features. ICASSP 2023 -- IEEE International Conference on Acoustics, Speech and Signal Processing. https://arxiv.org/abs/2302.08250
- Little, Roderick J. A.; Rubin, Donald B. (2019). Statistical Analysis with Missing Data. Wiley. https://doi.org/10.1002/9781119482260
- Rossi, E.; Kenlay, H.; Gorinova, M. I.; Chamberlain, B. P.; Dong, X.; Bronstein, M. M. (2022). On the Unreasonable Effectiveness of Feature Propagation in Learning on Graphs with Missing Node Features. Proceedings of the First Learning on Graphs Conference (LoG 2022) 198: 11:1--11:16. https://proceedings.mlr.press/v198/rossi22a.html
- Song; Zhou; Wang; Liu; others (2025). Dynamic graph structure evolution for node classification with missing attributes. Scientific Reports 15. https://doi.org/10.1038/s41598-025-09840-z
- Srinivasan, B.; Ribeiro, B. (2020). On the Equivalence between Positional Node Embeddings and Structural Graph Representations. ICLR 2020. https://arxiv.org/abs/1910.00452
- Um, D.; Kim, J.; Park; Lim; Ahn; Park; others (2025). Propagate and Inject: Revisiting Propagation-Based Feature Imputation for Graphs with Partially Observed Features. ICML 2025. https://openreview.net/forum?id=QfKrcgyase
- You, J.; Ying, R.; Leskovec, J. (2019). Position-aware Graph Neural Networks. Proceedings of the 36th International Conference on Machine Learning (ICML 2019) 97. https://arxiv.org/abs/1906.04817
- Zhu, Jiong; Yan, Yujun; Zhao, Lingxiao; Heimann, Mark; Akoglu, Leman; Koutra, Danai (2020). Beyond Homophily in Graph Neural Networks: Current Limitations and Effective Designs. Advances in Neural Information Processing Systems (NeurIPS 2020). https://arxiv.org/abs/2006.11468
