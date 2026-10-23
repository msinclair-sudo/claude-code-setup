## missing-features.1 (claim)

The literature on handling graph nodes that carry edges but lack feature vectors splits into two families plus a model-internal approach; the review describes neighbour feature propagation (diffusion imputation), model-internal imputation, structure-only/positional embedding, and dynamic/joint reconstruction.

- conf: not stated
- class: not stated
- holds: the published literature on graph nodes that carry edges but lack feature vectors, as the review groups it
- src: none (the reviewer's synthesis)
- trail: GHOST §Strategies

From the note:

> GHOST:B-0005 [abstract: Note Role] **Contains**: a returned literature-review result for the [[ghost-node-positioning]] brief — what the published literature establishes about handling graph nodes that carry edges but lack feature vectors, with verified claims, full references, and one verdict.
>
> GHOST:B-0008 [1. Strategies the field uses for featureless nodes] The literature splits cleanly into two families plus a model-internal approach:
>
> GHOST:B-0009 [1. Strategies the field uses for featureless nodes] - **Neighbour feature propagation / diffusion imputation.** Feature Propagation (FP) minimises Dirichlet energy, giving a diffusion-type PDE on the graph whose discretisation reconstructs missing features from observed neighbours — a simple, fast, scalable algorithm.
>
> GHOST:B-0013 [1. Strategies the field uses for featureless nodes] - **Model-internal imputation.** GCNMF folds Gaussian-mixture imputation inside a GCN [R3].
>
> GHOST:B-0015 [1. Strategies the field uses for featureless nodes] - **Structure-only / positional embedding.** A distinct family consuming *only* topology — LLE, Laplacian Eigenmaps, Graph Factorisation, GraRep, HOPE, DeepWalk, node2vec, SDNE, DNGR, LINE — operating on adjacency/similarity matrices; attribute-joint methods are treated as a separate, newer line [R8].
>
> GHOST:B-0017 [1. Strategies the field uses for featureless nodes] - **Dynamic / joint reconstruction.** "Attribute-missing graph" methods that jointly reconstruct attributes *and* update structure via alternating optimisation (EGS), rather than fixed mean/zero imputation on a static graph [R3, R4].
>

## missing-features.2 (claim)

"Existing graph learning methods including the popular GNN cannot provide satisfied learning performance since they are not specified for attribute-missing graphs."

- conf: not stated
- class: not stated
- holds: attribute-missing graphs; quoted from Chen et al. (2022)
- src: chenLearningAttributeMissingGraphs2022
- trail: GHOST §Bounding

From the note:

> GHOST:B-0039 [5. Bounding / negative facts] - **Standard GNNs are not built for this.** "Existing graph learning methods including the popular GNN cannot provide satisfied learning performance since they are not specified for attribute-missing graphs" [R3].
>
> GHOST:R-0005 [References] [R3] Chen, X., Chen, S., Yao, J., Zheng, H., Zhang, Y., Tsang, I. W. (2022).
>

## evidence-base.1 (claim)

Several key sources the review rests on are 2025–2026 preprints or under review, at high-quality venues but not all finalised.

- conf: not stated
- class: not stated
- holds: the sources the note numbers R5, R6 and R7 (Um et al. 2025; the anonymous 2025 low-variance paper; Ferrini et al. 2026)
- src: umPropagateInjectRevisiting2025, anonymousLowVarianceBottleneck2025, ferriniRethinkingGNNsMissing2026
- trail: GHOST §Standing caveats

From the note:

> GHOST:B-0050 [Standing caveats on the corpus] Several key sources are 2025–2026 preprints / under-review (R5, R6, R7) — high-quality venues but not all finalized.
>
> GHOST:R-0012 [References] [R5] Um, D., Kim, J., Park, [et al.], Lim, Ahn, Park (2025).
>
> GHOST:R-0016 [References] [R6] Anonymous (2025).
>
> GHOST:R-0019 [References] [R7] Ferrini, F., Lachi, V., Longa, A., Lepri, B., Akiyoshi, [et al.], Passerini, A., Liu, Jaeger (2026).
>

Not found in the cited text (where to look, not what is wrong): holds: low-variance

## feature-propagation.1 (claim)

Feature Propagation (FP) minimises Dirichlet energy, giving a diffusion-type PDE on the graph whose discretisation reconstructs missing features from observed neighbours: a simple, fast, scalable algorithm.

- conf: not stated
- class: not stated
- holds: graphs whose nodes have missing features
- src: rossiUnreasonableEffectivenessFeature2022
- rating: "Confidence: high (3-0)"
- trail: GHOST §Strategies

From the note:

> GHOST:B-0009 [1. Strategies the field uses for featureless nodes] - **Neighbour feature propagation / diffusion imputation.** Feature Propagation (FP) minimises Dirichlet energy, giving a diffusion-type PDE on the graph whose discretisation reconstructs missing features from observed neighbours — a simple, fast, scalable algorithm.
>
> GHOST:B-0012 [1. Strategies the field uses for featureless nodes] *Confidence: high (3-0).*
>

## feature-propagation.2 (claim)

Feature Propagation is the graph/diffusion instance of recovering structure under missing high-dimensional data.

- conf: not stated
- class: not stated
- holds: the review's framing, linked to the vault note on missing-data imputation
- src: none (the reviewer's framing; no source cited)
- trail: GHOST §Strategies

From the note:

> GHOST:B-0010 [1. Strategies the field uses for featureless nodes] (The graph/diffusion instance of [[Missing_Data_Imputation|recovering structure under missing high-dimensional data]].
>

Not found in the cited text (where to look, not what is wrong): Propagation; holds: review

## feature-propagation.3 (claim)

Feature Propagation's motivating setting is explicitly the partially-attributed, cold-start case ("age and gender available only for a small subset of users").

- conf: not stated
- class: not stated
- holds: the setting Rossi et al. (2022) motivate FP with
- src: rossiUnreasonableEffectivenessFeature2022
- rating: "Confidence: high (3-0)"
- trail: GHOST §Strategies

From the note:

> GHOST:B-0011 [1. Strategies the field uses for featureless nodes] Its motivating setting is explicitly the partially-attributed / cold-start case ("age and gender available only for a small subset of users") [R1].
>
> GHOST:B-0012 [1. Strategies the field uses for featureless nodes] *Confidence: high (3-0).*
>
> GHOST:R-0001 [References] [R1] Rossi, E., Kenlay, H., Gorinova, M. I., Chamberlain, B. P., Dong, X., Bronstein, M. M. (2022).
>

Not found in the cited text (where to look, not what is wrong): Propagation; holds: fp

## feature-propagation.4 (claim)

Feature Propagation rests on a feature-homophily assumption and degrades on heterophilous graphs.

- conf: not stated
- class: not stated
- holds: heterophilous graphs; given as a caveat of Rossi et al. (2022)
- src: rossiUnreasonableEffectivenessFeature2022 (caveat)
- trail: GHOST §Degradation

From the note:

> GHOST:B-0030 [2. Degradation as the featureless fraction rises] FP rests on a feature-homophily assumption and degrades on heterophilous graphs [R1, caveat].
>
> GHOST:R-0001 [References] [R1] Rossi, E., Kenlay, H., Gorinova, M. I., Chamberlain, B. P., Dong, X., Bronstein, M. M. (2022).
>

Not found in the cited text (where to look, not what is wrong): Propagation

## feature-propagation.5 (claim)

Feature Propagation outperformed prior missing-feature methods on seven benchmarks; this is a 2022 historical fact, not current state of the art.

- conf: not stated
- class: not stated
- holds: the seven benchmarks of Rossi et al. (2022); homophilous, sparse, MCAR benchmarks, mostly author-reported; a 2022 result
- src: rossiUnreasonableEffectivenessFeature2022
- trail: GHOST §Degradation, §Standing caveats

From the note:

> GHOST:B-0020 [2. Degradation as the featureless fraction rises] - FP: on average ~4% relative node-classification accuracy drop at **99% missing** across seven benchmarks; it outperformed prior missing-feature methods on those benchmarks [R1].
>
> GHOST:B-0029 [2. Degradation as the featureless fraction rises] **Caveat carried on every number above:** homophilous + sparse + MCAR, and mostly author-reported.
>
> GHOST:B-0052 [Standing caveats on the corpus] "FP outperforms previous methods" is a 2022 historical fact, not current SOTA.
>
> GHOST:R-0001 [References] [R1] Rossi, E., Kenlay, H., Gorinova, M. I., Chamberlain, B. P., Dong, X., Bronstein, M. M. (2022).
>

Not found in the cited text (where to look, not what is wrong): Propagation

## feature-propagation.6 (claim)

Feature Propagation is now a baseline, superseded as state of the art by PCFI, DART and others.

- conf: not stated
- class: not stated
- holds: the field at the time of the review
- src: none (the reviewer's statement; no source cited)
- trail: GHOST §Degradation

From the note:

> GHOST:B-0021 [2. Degradation as the featureless fraction rises] *(Historical fact — FP is now a baseline, superseded as SOTA by PCFI/DART/etc.)*
>

Not found in the cited text (where to look, not what is wrong): Propagation; holds: field; holds: review

## feature-propagation.7 (claim)

Propagation produces low-variance, near-constant channels that contribute little downstream; this is established with empirical evidence and a theoretical proof, and independently corroborated at a second venue.

- conf: repl (note: "independently corroborated at a second venue")
- class: meas/deriv (note: "established with empirical evidence and a theoretical proof")
- holds: propagation-based feature imputation; both sources are 2025 papers among the note's preprints or under-review sources
- src: umPropagateInjectRevisiting2025 (preprint / under review), anonymousLowVarianceBottleneck2025 (preprint / under review)
- rating: "proven"
- trail: GHOST §Verdict, §Bounding

From the note:

> GHOST:A-007 [Verdict] **Propagation has a proven systematic defect.** It produces low-variance channels that contribute little downstream — established with empirical evidence *and* a theoretical proof, and independently corroborated at a second venue [R5, R6].
>
> GHOST:B-0036 [5. Bounding / negative facts] - **Low-variance defect (proven).** Propagation produces near-constant channels that add little downstream — empirical + theoretical proof, independently corroborated [R5, R6].
>
> GHOST:B-0050 [Standing caveats on the corpus] Several key sources are 2025–2026 preprints / under-review (R5, R6, R7) — high-quality venues but not all finalized.
>
> GHOST:R-0012 [References] [R5] Um, D., Kim, J., Park, [et al.], Lim, Ahn, Park (2025).
>
> GHOST:R-0016 [References] [R6] Anonymous (2025).
>

Not found in the cited text (where to look, not what is wrong): holds: propagation-based

## feature-propagation.8 (claim)

The low-variance defect bounds propagation but does not refute it: the high-variance channels do the work.

- conf: not stated
- class: not stated
- holds: propagation-based feature imputation
- src: none (the reviewer's reading of the low-variance finding)
- trail: GHOST §Bounding

From the note:

> GHOST:B-0036 [5. Bounding / negative facts] - **Low-variance defect (proven).** Propagation produces near-constant channels that add little downstream — empirical + theoretical proof, independently corroborated [R5, R6].
>
> GHOST:B-0037 [5. Bounding / negative facts] Bounds, does not refute, the strategy: the high-variance channels do the work.
>

Not found in the cited text (where to look, not what is wrong): holds: propagation-based

## model-internal-imputation.1 (claim)

GCNMF folds Gaussian-mixture imputation inside a GCN.

- conf: not stated
- class: not stated
- holds: graphs with missing node features
- src: chenLearningAttributeMissingGraphs2022
- trail: GHOST §Strategies

From the note:

> GHOST:B-0013 [1. Strategies the field uses for featureless nodes] - **Model-internal imputation.** GCNMF folds Gaussian-mixture imputation inside a GCN [R3].
>

## model-internal-imputation.2 (claim)

Model-internal imputation is the strategy that fails badly under high missingness.

- conf: not stated
- class: not stated
- holds: high missingness
- src: none (the reviewer's summary of the high-missingness figures)
- trail: GHOST §Strategies

From the note:

> GHOST:B-0013 [1. Strategies the field uses for featureless nodes] - **Model-internal imputation.** GCNMF folds Gaussian-mixture imputation inside a GCN [R3].
>
> GHOST:B-0014 [1. Strategies the field uses for featureless nodes] This is the strategy that fails badly under high missingness (below).
>

## joint-reconstruction.1 (claim)

"Attribute-missing graph" methods jointly reconstruct attributes and update structure via alternating optimisation (EGS), rather than imputing a fixed mean or zero on a static graph.

- conf: not stated
- class: not stated
- holds: attribute-missing graphs
- src: chenLearningAttributeMissingGraphs2022, songDynamicGraphStructure2025
- rating: "Confidence: high (3-0 / 2-1)"
- trail: GHOST §Strategies

From the note:

> GHOST:B-0017 [1. Strategies the field uses for featureless nodes] - **Dynamic / joint reconstruction.** "Attribute-missing graph" methods that jointly reconstruct attributes *and* update structure via alternating optimisation (EGS), rather than fixed mean/zero imputation on a static graph [R3, R4].
>
> GHOST:B-0018 [1. Strategies the field uses for featureless nodes] *Confidence: high (3-0 / 2-1).*
>

## structure-only-embedding.1 (claim)

A distinct family of methods consumes only topology (LLE, Laplacian Eigenmaps, Graph Factorisation, GraRep, HOPE, DeepWalk, node2vec, SDNE, DNGR, LINE), operating on adjacency or similarity matrices; attribute-joint methods are treated as a separate, newer line.

- conf: not stated
- class: not stated
- holds: the classical methods of a 2018 survey
- src: goyalGraphEmbeddingTechniques2018
- rating: "Confidence: high (3-0)"
- trail: GHOST §Strategies

From the note:

> GHOST:B-0015 [1. Strategies the field uses for featureless nodes] - **Structure-only / positional embedding.** A distinct family consuming *only* topology — LLE, Laplacian Eigenmaps, Graph Factorisation, GraRep, HOPE, DeepWalk, node2vec, SDNE, DNGR, LINE — operating on adjacency/similarity matrices; attribute-joint methods are treated as a separate, newer line [R8].
>
> GHOST:B-0016 [1. Strategies the field uses for featureless nodes] *Confidence: high (3-0).*
>
> GHOST:B-0051 [Standing caveats on the corpus] The structure-only taxonomy rests on a 2018 survey (R8); the topology-only characterisation of those classical methods remains accurate, but the field has expanded since.
>

## structure-only-embedding.2 (claim)

The structure-only taxonomy rests on a 2018 survey; its topology-only characterisation of those classical methods remains accurate, but the field has expanded since.

- conf: not stated
- class: not stated
- holds: the classical structure-only methods; a 2018 survey
- src: goyalGraphEmbeddingTechniques2018
- trail: GHOST §Standing caveats

From the note:

> GHOST:B-0051 [Standing caveats on the corpus] The structure-only taxonomy rests on a 2018 survey (R8); the topology-only characterisation of those classical methods remains accurate, but the field has expanded since.
>

## structure-only-embedding.3 (claim)

Structure-only embeddings are regime-dependent with no single winner, though higher-order-proximity methods generally win.

- conf: not stated
- class: not stated
- holds: the structure-only methods compared in a 2018 survey
- src: goyalGraphEmbeddingTechniques2018
- trail: GHOST §Bounding

From the note:

> GHOST:B-0040 [5. Bounding / negative facts] - **Structure-only embeddings are regime-dependent with no single winner.** Higher-order-proximity methods generally win, but node2vec leads on node classification yet loses on a structured SBM graph where labels reflect communities and there is no structural equivalence between nodes [R8].
>
> GHOST:B-0051 [Standing caveats on the corpus] The structure-only taxonomy rests on a 2018 survey (R8); the topology-only characterisation of those classical methods remains accurate, but the field has expanded since.
>

Not found in the cited text (where to look, not what is wrong): holds: in

## structure-only-embedding.4 (claim)

node2vec leads on node classification yet loses on a structured SBM graph where labels reflect communities and there is no structural equivalence between nodes.

- conf: not stated
- class: not stated
- holds: node classification, and a structured SBM graph with community labels and no structural equivalence; from a 2018 survey
- src: goyalGraphEmbeddingTechniques2018
- trail: GHOST §Bounding

From the note:

> GHOST:B-0040 [5. Bounding / negative facts] - **Structure-only embeddings are regime-dependent with no single winner.** Higher-order-proximity methods generally win, but node2vec leads on node classification yet loses on a structured SBM graph where labels reflect communities and there is no structural equivalence between nodes [R8].
>
> GHOST:B-0051 [Standing caveats on the corpus] The structure-only taxonomy rests on a 2018 survey (R8); the topology-only characterisation of those classical methods remains accurate, but the field has expanded since.
>

## positional-vs-structural.1 (claim)

GNNs cannot capture position when node features are absent or identical: structurally isomorphic but positionally distinct nodes get identical embeddings, which is strictly true in the featureless or identical-feature regime.

- conf: not stated
- class: not stated
- holds: GNNs with absent or identical node features
- src: youPositionawareGraphNeural2019
- trail: GHOST §Bounding

From the note:

> GHOST:B-0041 [5. Bounding / negative facts] - **GNNs cannot capture position when features are absent/identical.** Structurally-isomorphic but positionally-distinct nodes get identical embeddings — strictly true in the featureless/identical-feature regime central to this brief [R10].
>

## positional-vs-structural.2 (claim)

Positional embeddings are formally samples from a G-equivariant distribution whose expectation is the structural representation; this formal sampling relationship and its directionality (positional = samples of structural) survived verification.

- conf: not stated
- class: deriv (note: "Positional embeddings are formally samples")
- holds: the formal relationship between positional embeddings and structural representations, not their interchangeability for tasks
- src: srinivasanEquivalencePositionalNode2020
- trail: GHOST §Bounding, §Refuted

From the note:

> GHOST:B-0042 [5. Bounding / negative facts] Positional embeddings are formally samples from a G-equivariant distribution whose expectation is the structural representation [R9].
>
> GHOST:C-002 [Refuted (killed in verification — do NOT reintroduce)] - ✗ **"Positional and structural representations are practically interchangeable for tasks."** Vote 0-3. Only the formal sampling relationship and its directionality (positional = samples of structural) survived [R9].
>

## benchmark-regime.1 (claim)

The robustness numbers for imputing missing node features are measured almost entirely on homophilous, sparse bag-of-words citation and co-purchase graphs (Cora, Citeseer, PubMed, Photo) under Missing-Completely-At-Random missingness, and many are self-reported by the method authors.

- conf: not stated
- class: not stated
- holds: the robustness figures of Rossi et al. (2022), Lei et al. (2023) and Song et al. (2025)
- src: rossiUnreasonableEffectivenessFeature2022, leiSelfsupervisedGuidedHypergraph2023, songDynamicGraphStructure2025
- trail: GHOST §Verdict, §Degradation

From the note:

> GHOST:A-005 [Verdict] **The robustness numbers are regime-bound.** They are measured almost entirely on homophilous, sparse bag-of-words citation/co-purchase graphs (Cora, Citeseer, PubMed, Photo) under Missing-Completely-At-Random missingness, and many are self-reported by the method authors [R1, R2, R4].
>
> GHOST:B-0029 [2. Degradation as the featureless fraction rises] **Caveat carried on every number above:** homophilous + sparse + MCAR, and mostly author-reported.
>
> GHOST:R-0001 [References] [R1] Rossi, E., Kenlay, H., Gorinova, M. I., Chamberlain, B. P., Dong, X., Bronstein, M. M. (2022).
>
> GHOST:R-0003 [References] [R2] Lei, C., Fu, J., Wang, X., Qiu, X., Hu, Z., Peng, Y., You, J. (2023).
>
> GHOST:R-0008 [References] [R4] Song, [et al.], Zhou, Wang, Liu (2025).
>

## benchmark-regime.2 (claim)

High feature sparsity provably bounds the information loss from missingness, "making all models appear robust and preventing a meaningful comparison": on standard benchmarks all models look robust and cannot be distinguished.

- conf: not stated
- class: deriv (note: "provably bounds")
- holds: standard benchmarks with high feature sparsity; a 2026 result, under review
- src: ferriniRethinkingGNNsMissing2026 (preprint / under review)
- rating: "proven"
- trail: GHOST §Verdict, §Bounding

From the note:

> GHOST:A-006 [Verdict] **A 2026 result proves the benchmark itself hides the differences.** High feature sparsity provably bounds the information loss from missingness, "making all models appear robust and preventing a meaningful comparison" — so the dominance of propagation on standard benchmarks may be an artifact, not a regime-general property [R7].
>
> GHOST:B-0038 [5. Bounding / negative facts] - **Benchmark artifact (proven).** High sparsity bounds missingness-induced information loss, so all models look robust and cannot be distinguished on standard benchmarks; dense-feature and non-MCAR (MNAR) regimes are under-evaluated [R7].
>
> GHOST:B-0050 [Standing caveats on the corpus] Several key sources are 2025–2026 preprints / under-review (R5, R6, R7) — high-quality venues but not all finalized.
>

## benchmark-regime.3 (claim)

The dominance of propagation on standard benchmarks may therefore be an artifact, not a regime-general property.

- conf: not stated
- class: not stated
- holds: standard benchmarks with high feature sparsity
- src: ferriniRethinkingGNNsMissing2026
- trail: GHOST §Verdict

From the note:

> GHOST:A-006 [Verdict] **A 2026 result proves the benchmark itself hides the differences.** High feature sparsity provably bounds the information loss from missingness, "making all models appear robust and preventing a meaningful comparison" — so the dominance of propagation on standard benchmarks may be an artifact, not a regime-general property [R7].
>

## benchmark-regime.4 (claim)

Dense-feature and non-MCAR (MNAR) regimes are under-evaluated.

- conf: not stated
- class: not stated
- holds: evaluation of methods for missing node features
- src: ferriniRethinkingGNNsMissing2026
- trail: GHOST §Bounding

From the note:

> GHOST:B-0038 [5. Bounding / negative facts] - **Benchmark artifact (proven).** High sparsity bounds missingness-induced information loss, so all models look robust and cannot be distinguished on standard benchmarks; dense-feature and non-MCAR (MNAR) regimes are under-evaluated [R7].
>

## benchmark-regime.5 (claim)

Ferrini et al. argue that standard benchmarks cannot answer whether propagation's robustness survives on dense, semantically meaningful features and structural or feature-dependent (MNAR) missingness, and introduce new protocols, but cross-method results are not yet established.

- conf: not stated
- class: not stated
- holds: dense features and MNAR missingness
- src: ferriniRethinkingGNNsMissing2026
- trail: GHOST §Open Questions

From the note:

> GHOST:B-0046 [Open Questions (unanswered by the literature)] **Dense + non-MCAR regimes:** does propagation robustness survive on dense, semantically meaningful features and structural/feature-dependent (MNAR) missingness?
>
> GHOST:B-0047 [Open Questions (unanswered by the literature)] Ferrini et al. argue standard benchmarks cannot answer this and introduce new protocols, but cross-method results are not yet established [R7].
>

## degradation.1 (claim)

Diffusion/propagation imputation (Feature Propagation and variants) reconstructs entirely-missing node features from observed neighbours and degrades only marginally, about 2–4% relative node-classification accuracy at 99% missing, while model-internal imputation (GCNMF) collapses to about 35% on the same benchmark.

- conf: repl (note: "The single most replicated empirical result")
- class: meas (note: "empirical result")
- holds: homophilous, sparse bag-of-words citation and co-purchase graphs (Cora, Citeseer, PubMed, Photo) under Missing-Completely-At-Random missingness, many figures self-reported by the method authors; the 2–4% range is the note's, across Feature Propagation and its variants; the unscoped version was killed in verification
- src: rossiUnreasonableEffectivenessFeature2022, leiSelfsupervisedGuidedHypergraph2023, chenLearningAttributeMissingGraphs2022
- trail: GHOST §Verdict, §Refuted

From the note:

> GHOST:A-002 [Verdict] The single most replicated empirical result is that diffusion/propagation imputation (Feature Propagation and variants) reconstructs entirely-missing node features from observed neighbours and degrades only marginally — ~2–4% relative node-classification accuracy at 99% missing — while model-internal imputation (GCNMF) collapses to ~35% on the same benchmark [R1, R2, R3].
>
> GHOST:A-005 [Verdict] **The robustness numbers are regime-bound.** They are measured almost entirely on homophilous, sparse bag-of-words citation/co-purchase graphs (Cora, Citeseer, PubMed, Photo) under Missing-Completely-At-Random missingness, and many are self-reported by the method authors [R1, R2, R4].
>
> GHOST:C-001 [Refuted (killed in verification — do NOT reintroduce)] - ✗ **"FP robustness (~4% at 99% missing) is a general fact."** Vote 1-2. The *unscoped* version fails; only the homophilous-sparse-MCAR-scoped version survives [R1, contra R7].
>

Not found in the cited text (where to look, not what is wrong): holds: its; holds: in

## degradation.2 (claim)

Feature Propagation loses on average about 4% relative node-classification accuracy at 99% missing across seven benchmarks.

- conf: not stated
- class: meas (note: "across seven benchmarks")
- holds: seven benchmarks, 99% of node features missing; homophilous, sparse, MCAR, mostly author-reported
- src: rossiUnreasonableEffectivenessFeature2022
- trail: GHOST §Degradation

From the note:

> GHOST:B-0020 [2. Degradation as the featureless fraction rises] - FP: on average ~4% relative node-classification accuracy drop at **99% missing** across seven benchmarks; it outperformed prior missing-feature methods on those benchmarks [R1].
>
> GHOST:B-0029 [2. Degradation as the featureless fraction rises] **Caveat carried on every number above:** homophilous + sparse + MCAR, and mostly author-reported.
>

Not found in the cited text (where to look, not what is wrong): Propagation

## degradation.3 (claim)

SGHFP, a hypergraph variant of feature propagation, loses on average 2.67% relative accuracy at 99% missing across four datasets.

- conf: not stated
- class: meas (note: "across four datasets")
- holds: four datasets, 99% missing; homophilous, sparse, MCAR, mostly author-reported
- src: leiSelfsupervisedGuidedHypergraph2023
- rating: "Confidence: high (3-0)"
- trail: GHOST §Degradation

From the note:

> GHOST:B-0022 [2. Degradation as the featureless fraction rises] - SGHFP (hypergraph variant): average **2.67%** relative drop at 99% missing across four datasets; verified per-dataset from Table 2 — Cora 81.23→79.41 (−2.25%), Photo 91.73→87.73 (−4.36%, the worst case), PubMed 77.36→74.29 (−3.97%) [R2].
>
> GHOST:B-0023 [2. Degradation as the featureless fraction rises] *Confidence: high (3-0).*
>
> GHOST:B-0029 [2. Degradation as the featureless fraction rises] **Caveat carried on every number above:** homophilous + sparse + MCAR, and mostly author-reported.
>

## degradation.4 (claim)

Per dataset at 99% missing, SGHFP goes from 81.23 to 79.41 on Cora (−2.25%), from 91.73 to 87.73 on Photo (−4.36%, the worst case) and from 77.36 to 74.29 on PubMed (−3.97%).

- conf: not stated
- class: meas (note: "verified per-dataset from Table 2")
- holds: Cora, Photo and PubMed, 99% missing, from Table 2 of Lei et al. (2023); homophilous, sparse, MCAR, mostly author-reported
- src: leiSelfsupervisedGuidedHypergraph2023
- rating: "Confidence: high (3-0)"
- trail: GHOST §Degradation

From the note:

> GHOST:B-0022 [2. Degradation as the featureless fraction rises] - SGHFP (hypergraph variant): average **2.67%** relative drop at 99% missing across four datasets; verified per-dataset from Table 2 — Cora 81.23→79.41 (−2.25%), Photo 91.73→87.73 (−4.36%, the worst case), PubMed 77.36→74.29 (−3.97%) [R2].
>
> GHOST:B-0023 [2. Degradation as the featureless fraction rises] *Confidence: high (3-0).*
>
> GHOST:B-0029 [2. Degradation as the featureless fraction rises] **Caveat carried on every number above:** homophilous + sparse + MCAR, and mostly author-reported.
>
> GHOST:R-0003 [References] [R2] Lei, C., Fu, J., Wang, X., Qiu, X., Hu, Z., Peng, Y., You, J. (2023).
>

## degradation.5 (claim)

At 99% missing on Cora, propagation sits at about 78–79%.

- conf: not stated
- class: meas (note: "Contrast at 99% missing on Cora")
- holds: Cora, 99% missing; homophilous, sparse, MCAR, mostly author-reported
- src: rossiUnreasonableEffectivenessFeature2022, leiSelfsupervisedGuidedHypergraph2023
- rating: "Confidence: high (3-0 / 2-1)"
- trail: GHOST §Degradation

From the note:

> GHOST:B-0024 [2. Degradation as the featureless fraction rises] - Contrast at 99% missing on Cora: propagation ~78–79% vs **GCNMF 34.54%** — the latter confirmed by two independent papers [R1, R2].
>
> GHOST:B-0026 [2. Degradation as the featureless fraction rises] *Confidence: high (3-0 / 2-1).*
>
> GHOST:B-0029 [2. Degradation as the featureless fraction rises] **Caveat carried on every number above:** homophilous + sparse + MCAR, and mostly author-reported.
>

## degradation.6 (claim)

At 99% missing on Cora, GCNMF scores 34.54%, a figure confirmed by two independent papers.

- conf: repl (note: "confirmed by two independent papers")
- class: meas (note: "Contrast at 99% missing on Cora")
- holds: Cora, 99% missing; homophilous, sparse, MCAR, mostly author-reported
- src: rossiUnreasonableEffectivenessFeature2022, leiSelfsupervisedGuidedHypergraph2023
- rating: "Confidence: high (3-0 / 2-1)"
- trail: GHOST §Degradation

From the note:

> GHOST:B-0024 [2. Degradation as the featureless fraction rises] - Contrast at 99% missing on Cora: propagation ~78–79% vs **GCNMF 34.54%** — the latter confirmed by two independent papers [R1, R2].
>
> GHOST:B-0026 [2. Degradation as the featureless fraction rises] *Confidence: high (3-0 / 2-1).*
>
> GHOST:B-0029 [2. Degradation as the featureless fraction rises] **Caveat carried on every number above:** homophilous + sparse + MCAR, and mostly author-reported.
>

## degradation.7 (claim)

At 99% missing on Cora, PaGNN sits at about 58%: low, but not the catastrophic collapse of GCNMF.

- conf: not stated
- class: meas (note: "Contrast at 99% missing on Cora")
- holds: Cora, 99% missing; homophilous, sparse, MCAR, mostly author-reported
- src: chenLearningAttributeMissingGraphs2022
- rating: "Confidence: high (3-0 / 2-1)"
- trail: GHOST §Degradation

From the note:

> GHOST:B-0024 [2. Degradation as the featureless fraction rises] - Contrast at 99% missing on Cora: propagation ~78–79% vs **GCNMF 34.54%** — the latter confirmed by two independent papers [R1, R2].
>
> GHOST:B-0025 [2. Degradation as the featureless fraction rises] PaGNN sits at ~58% — low, but not the catastrophic collapse of GCNMF [R3].
>
> GHOST:B-0026 [2. Degradation as the featureless fraction rises] *Confidence: high (3-0 / 2-1).*
>
> GHOST:B-0029 [2. Degradation as the featureless fraction rises] **Caveat carried on every number above:** homophilous + sparse + MCAR, and mostly author-reported.
>

## degradation.8 (claim)

EGS degrades gently against a PAGNN baseline on Cora from 5% to 75% missing (baseline 81.36 to 74.05; EGS 84.77 to 82.13).

- conf: not stated
- class: not stated
- holds: Cora, 5% to 75% missing; self-reported by the method's authors; homophilous, sparse, MCAR
- src: songDynamicGraphStructure2025 (self-reported)
- rating: "Confidence: high"
- trail: GHOST §Degradation

From the note:

> GHOST:B-0027 [2. Degradation as the featureless fraction rises] - EGS degrades gently vs a PAGNN baseline (Cora, 5%→75% missing: baseline 81.36→74.05; EGS 84.77→82.13) — self-reported [R4].
>
> GHOST:B-0028 [2. Degradation as the featureless fraction rises] *Confidence: high.*
>
> GHOST:B-0029 [2. Degradation as the featureless fraction rises] **Caveat carried on every number above:** homophilous + sparse + MCAR, and mostly author-reported.
>

## degradation.9 (claim)

Degradation is quantified within propagation but never located against structure-only baselines across regimes.

- conf: not stated
- class: search (note: "never located against structure-only baselines")
- holds: the featureless fraction or graph sparsity at which neighbour aggregation would lose to structure-only embedding
- src: none (an absence in the reviewed literature)
- search: not stated
- trail: GHOST §Open Questions

From the note:

> GHOST:B-0048 [Open Questions (unanswered by the literature)] **Crossover point:** at what featureless fraction / graph sparsity does neighbour aggregation become too sparse to help and lose to structure-only embedding?
>
> GHOST:B-0049 [Open Questions (unanswered by the literature)] Degradation is quantified within propagation but never located against structure-only baselines across regimes.
>

## contamination.1 (claim)

No controlled benchmark measures whether imputed or structure-only nodes contaminate the clusters of feature-bearing nodes: no controlled head-to-head and no controlled mixed-population benchmark was found.

- conf: not stated
- class: search (note: "No controlled head-to-head was found")
- holds: mixed populations of feature-bearing and imputed or structure-only nodes (brief item 3)
- src: none (an absence: no source measured it)
- search: searched, not found (note: "No controlled head-to-head was found")
- trail: GHOST §Verdict, §Contamination, §Open Questions

From the note:

> GHOST:A-009 [Verdict] **The two questions the brief cared about most are unanswered by the literature** (see *Open Questions*): no controlled benchmark measures whether imputed/structure-only nodes *contaminate* the clusters of feature-bearing nodes, and none measures layout distortion on mixed populations.
>
> GHOST:B-0031 [3. Contamination of feature-bearing nodes (brief item 3)] **No controlled head-to-head was found.** The only support is *indirect and motivational*: Song et al. argue (by molecular-graph analogy) that severe missingness "can alter the semantic information of the graph, leading to changes in the graph structure," which is why they update structure jointly [R4].
>
> GHOST:B-0043 [Open Questions (unanswered by the literature)] **Contamination (brief item 3):** does inserting imputed/structure-only nodes measurably distort feature-bearing nodes' clusters?
>
> GHOST:B-0044 [Open Questions (unanswered by the literature)] No controlled mixed-population benchmark found.
>

## contamination.2 (claim)

Song et al. argue, by molecular-graph analogy, that severe missingness "can alter the semantic information of the graph, leading to changes in the graph structure", which is why they update structure jointly; this is a theoretical, motivational statement, not a measured demonstration that featureless nodes distort feature-bearing nodes' clusters.

- conf: not stated
- class: assert (note: "This is a theoretical/motivational statement")
- holds: indirect and motivational support only, by molecular-graph analogy
- src: songDynamicGraphStructure2025 (indirect and motivational)
- rating: "verification vote 2-1"
- trail: GHOST §Contamination

From the note:

> GHOST:B-0031 [3. Contamination of feature-bearing nodes (brief item 3)] **No controlled head-to-head was found.** The only support is *indirect and motivational*: Song et al. argue (by molecular-graph analogy) that severe missingness "can alter the semantic information of the graph, leading to changes in the graph structure," which is why they update structure jointly [R4].
>
> GHOST:B-0032 [3. Contamination of feature-bearing nodes (brief item 3)] This is a theoretical/motivational statement (verification vote 2-1), **not** a measured demonstration that featureless nodes distort feature-bearing nodes' clusters.
>
> GHOST:B-0033 [3. Contamination of feature-bearing nodes (brief item 3)] Cite as indirect only.
>

## layout-distortion.1 (claim)

No reviewed source measured layout distortion on mixed populations: the visualization search angle returned sources, but none yielded a confirmed claim tying topology-only node placement to distortion artifacts (centroid piling, hub collapse) on mixed attributed and featureless populations.

- conf: not stated
- class: search (note: "No reviewed source measured this")
- holds: topology-only node placement on mixed attributed and featureless populations (brief item 4)
- src: none (an absence: no source measured it)
- search: searched, not found (note: "The visualization search angle returned sources but none yielded a confirmed claim")
- trail: GHOST §Verdict, §Layout distortion, §Open Questions

From the note:

> GHOST:A-009 [Verdict] **The two questions the brief cared about most are unanswered by the literature** (see *Open Questions*): no controlled benchmark measures whether imputed/structure-only nodes *contaminate* the clusters of feature-bearing nodes, and none measures layout distortion on mixed populations.
>
> GHOST:B-0034 [4. Layout distortion on mixed populations (brief item 4)] **No reviewed source measured this.** The visualization search angle returned sources but none yielded a confirmed claim tying topology-only node placement to distortion artifacts (centroid piling, hub collapse) on mixed attributed/featureless populations.
>
> GHOST:B-0035 [4. Layout distortion on mixed populations (brief item 4)] Treat the brief's specific layout-artifact question as unanswered by the retrieved corpus.
>
> GHOST:B-0045 [Open Questions (unanswered by the literature)] **Layout distortion (brief item 4):** centroid piling / hub collapse on mixed populations — unmeasured in the retrieved corpus.
>

## layout-distortion.2 (claim)

The strategy of laying out topology separately and then mapping it onto attribute space surfaced only as the conceptual positional-vs-structural distinction, not as a benchmarked layout pipeline.

- conf: not stated
- class: search (note: "not as a benchmarked layout pipeline")
- holds: the strategy as named in the brief
- src: srinivasanEquivalencePositionalNode2020, youPositionawareGraphNeural2019
- search: searched, not found (note: "surfaced only as the conceptual positional-vs-structural distinction")
- trail: GHOST §Strategies

From the note:

> GHOST:B-0019 [1. Strategies the field uses for featureless nodes] The "lay out topology separately then map onto attribute space" strategy named in the brief surfaced only as the conceptual positional-vs-structural distinction [R9, R10], **not** as a benchmarked layout pipeline.
>

## default-strategy.1 (claim)

The answer is regime-dependent: neighbour feature propagation is a defensible default only in the homophilous, sparse-feature regime where its robustness has actually been demonstrated.

- conf: not stated
- class: not stated
- holds: the review's verdict (c)
- src: none (the review's verdict)
- contrary: not stated
- trail: GHOST §Verdict

From the note:

> GHOST:A-001 [Verdict] **(c) Regime-dependent — with neighbour feature propagation a defensible default *only* in the homophilous, sparse-feature regime where its robustness has actually been demonstrated.**
>

Not found in the cited text (where to look, not what is wrong): holds: review

## default-strategy.2 (claim)

Propagation's marginal degradation looks like a clean win for neighbour feature propagation, but it is not, for three reasons the verification surfaced and confirmed: the robustness numbers are regime-bound, a 2026 result proves the benchmark itself hides the differences, and propagation has a proven low-variance defect.

- conf: not stated
- class: not stated
- holds: the review's verdict on option (a)
- src: none (the review's verdict)
- contrary: not stated
- trail: GHOST §Verdict

From the note:

> GHOST:A-003 [Verdict] That looks like a clean win for option (a).
>
> GHOST:A-004 [Verdict] It is not, for three reasons that the verification surfaced and confirmed:
>
> GHOST:A-005 [Verdict] **The robustness numbers are regime-bound.** They are measured almost entirely on homophilous, sparse bag-of-words citation/co-purchase graphs (Cora, Citeseer, PubMed, Photo) under Missing-Completely-At-Random missingness, and many are self-reported by the method authors [R1, R2, R4].
>
> GHOST:A-006 [Verdict] **A 2026 result proves the benchmark itself hides the differences.** High feature sparsity provably bounds the information loss from missingness, "making all models appear robust and preventing a meaningful comparison" — so the dominance of propagation on standard benchmarks may be an artifact, not a regime-general property [R7].
>
> GHOST:A-007 [Verdict] **Propagation has a proven systematic defect.** It produces low-variance channels that contribute little downstream — established with empirical evidence *and* a theoretical proof, and independently corroborated at a second venue [R5, R6].
>

Not found in the cited text (where to look, not what is wrong): holds: review

## default-strategy.3 (claim)

Propagation is the right default where the graph is homophilous and features are sparse; outside that regime the evidence does not support it as a default, and structure-only or positional embedding becomes a live alternative whose performance is itself strongly regime-dependent with no single winner.

- conf: not stated
- class: not stated
- holds: the review's verdict; structure-only or positional embedding is option (b)
- src: goyalGraphEmbeddingTechniques2018, srinivasanEquivalencePositionalNode2020, youPositionawareGraphNeural2019
- contrary: not stated
- trail: GHOST §Verdict

From the note:

> GHOST:A-008 [Verdict] So propagation is the right default where the graph is homophilous and features are sparse; outside that regime the evidence does not support it as a default, and structure-only / positional embedding (option b) becomes a live alternative whose performance is itself strongly regime-dependent with no single winner [R8, R9, R10].
>

Not found in the cited text (where to look, not what is wrong): holds: review

## dns.1 (do not say)

"Feature Propagation's robustness, about 4% loss at 99% missing features, is a general fact."

- why: This unscoped claim was killed in verification (vote 1-2); only the version scoped to homophilous, sparse, MCAR benchmarks survives.
- instead: degradation.1, degradation.2
- trail: GHOST §Refuted

From the note:

> GHOST:C-001 [Refuted (killed in verification — do NOT reintroduce)] - ✗ **"FP robustness (~4% at 99% missing) is a general fact."** Vote 1-2. The *unscoped* version fails; only the homophilous-sparse-MCAR-scoped version survives [R1, contra R7].
>

Not found in the cited text (where to look, not what is wrong): Propagation; "Feature Propagation robustness, about 4% loss at 99% missing features, is a general fact."

## dns.2 (do not say)

"Positional and structural representations are practically interchangeable for tasks."

- why: This was killed in verification (vote 0-3); only the formal sampling relationship and its directionality (positional embeddings are samples of the structural representation) survived.
- instead: positional-vs-structural.2
- trail: GHOST §Refuted

From the note:

> GHOST:C-002 [Refuted (killed in verification — do NOT reintroduce)] - ✗ **"Positional and structural representations are practically interchangeable for tasks."** Vote 0-3. Only the formal sampling relationship and its directionality (positional = samples of structural) survived [R9].
>

## dns.3 (do not say)

"Song et al. showed that featureless nodes distort the clusters of feature-bearing nodes."

- why: Song et al.'s statement is theoretical and motivational, argued by molecular-graph analogy (verification vote 2-1), not a measured demonstration, and the note says to cite it as indirect only.
- instead: contamination.1, contamination.2
- trail: GHOST §Contamination

From the note:

> GHOST:B-0031 [3. Contamination of feature-bearing nodes (brief item 3)] **No controlled head-to-head was found.** The only support is *indirect and motivational*: Song et al. argue (by molecular-graph analogy) that severe missingness "can alter the semantic information of the graph, leading to changes in the graph structure," which is why they update structure jointly [R4].
>
> GHOST:B-0032 [3. Contamination of feature-bearing nodes (brief item 3)] This is a theoretical/motivational statement (verification vote 2-1), **not** a measured demonstration that featureless nodes distort feature-bearing nodes' clusters.
>
> GHOST:B-0033 [3. Contamination of feature-bearing nodes (brief item 3)] Cite as indirect only.
>

Not found in the cited text (where to look, not what is wrong): "Song et al. showed that featureless nodes distort the clusters of feature-bearing nodes."

## dns.4 (do not say)

"The absence of evidence on contamination and layout distortion counts in favour of one of the options."

- why: The note says to report the two unanswered questions as "no controlled evidence found", not as a point in favour of any option.
- instead: contamination.1, layout-distortion.1
- trail: GHOST §Verdict

From the note:

> GHOST:A-009 [Verdict] **The two questions the brief cared about most are unanswered by the literature** (see *Open Questions*): no controlled benchmark measures whether imputed/structure-only nodes *contaminate* the clusters of feature-bearing nodes, and none measures layout distortion on mixed populations.
>
> GHOST:A-010 [Verdict] Report this as "no controlled evidence found," not as a point in favour of any option.
>

Not found in the cited text (where to look, not what is wrong): "The absence of evidence on contamination and layout distortion counts in favour of one of the options."

## dns.5 (do not say)

"Feature Propagation outperforms previous methods and is the state of the art for missing node features."

- why: That Feature Propagation outperforms previous methods is a 2022 historical fact, not current state of the art; it is now a baseline, superseded by PCFI, DART and others.
- instead: feature-propagation.5, feature-propagation.6
- trail: GHOST §Degradation, §Standing caveats

From the note:

> GHOST:B-0021 [2. Degradation as the featureless fraction rises] *(Historical fact — FP is now a baseline, superseded as SOTA by PCFI/DART/etc.)*
>
> GHOST:B-0052 [Standing caveats on the corpus] "FP outperforms previous methods" is a 2022 historical fact, not current SOTA.
>

Not found in the cited text (where to look, not what is wrong): Propagation; "Feature Propagation outperforms previous methods and is the state of the art for missing node features."; Feature

