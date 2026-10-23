---
type: knowledge
title: Positioning graph nodes that lack features
inputs:
  - GHOST: PhD/biblion/research/results/ghost-node-positioning-result.md
refs: PhD/Proposal/Refs/Refs.bib
built: 2026-10-23
status: draft
tags:
  - research
  - knowledge
---

# Positioning graph nodes that lack features

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
| GHOST | [[ghost-node-positioning-result]] | refutations only | bracket keys | no | no | fallback (answers and critique; the note has no labelled citations) |

## Concepts

### missing-features: Graph nodes that carry edges but lack feature vectors
needs: none
- **missing-features.1** The literature on handling graph nodes that carry edges but lack feature vectors splits into two families plus a model-internal approach; the review describes neighbour feature propagation (diffusion imputation), model-internal imputation, structure-only/positional embedding, and dynamic/joint reconstruction.
  conf: not stated · class: not stated · holds: the published literature on graph nodes that carry edges but lack feature vectors, as the review groups it · src: none (the reviewer's synthesis) · trail: GHOST §Strategies · from: GHOST:B-0005, GHOST:B-0008, GHOST:B-0009, GHOST:B-0013, GHOST:B-0015, GHOST:B-0017
- **missing-features.2** "Existing graph learning methods including the popular GNN cannot provide satisfied learning performance since they are not specified for attribute-missing graphs."
  conf: not stated · class: not stated · holds: attribute-missing graphs; quoted from Chen et al. (2022) · src: chenLearningAttributeMissingGraphs2022 · trail: GHOST §Bounding · from: GHOST:B-0039, GHOST:R-0005

### homophily: Homophilous and heterophilous graphs
needs: none
- **homophily.bg1** In a homophilous graph connected nodes tend to share class labels and features; under heterophily (low homophily) connected nodes may have different class labels and dissimilar features.
  kind: background · ref: zhuBeyondHomophilyGraph2020 · check: arXiv:2006.11468 resolves (NeurIPS 2020); heterophily is defined in the abstract ("networks where connected nodes may have different class labels and dissimilar features")

### missingness-mechanism: Mechanisms of missingness (MCAR, MNAR)
needs: none
- **missingness-mechanism.bg1** Values are missing completely at random (MCAR) when the probability that a value is missing depends on neither the observed nor the missing values; missingness that depends on the missing values themselves is missing not at random (MNAR).
  kind: background · ref: littleStatisticalAnalysisMissing2019 · check: DOI 10.1002/9781119482260 resolves on Crossref (Wiley monograph, third edition); missingness mechanisms are in Chapter 1, Sections 1.2 "Missingness Patterns and Mechanisms" and 1.3 "Mechanisms That Lead to Missing Data", per the table of contents; the section text itself was not read

### evidence-base: The sources the review rests on
needs: none
- **evidence-base.1** Several key sources the review rests on are 2025–2026 preprints or under review, at high-quality venues but not all finalised.
  conf: not stated · class: not stated · holds: the sources the note numbers R5, R6 and R7 (Um et al. 2025; the anonymous 2025 low-variance paper; Ferrini et al. 2026) · src: umPropagateInjectRevisiting2025, anonymousLowVarianceBottleneck2025, ferriniRethinkingGNNsMissing2026 · trail: GHOST §Standing caveats · from: GHOST:B-0050, GHOST:R-0012, GHOST:R-0016, GHOST:R-0017, GHOST:R-0019

### feature-propagation: Neighbour feature propagation (diffusion imputation)
needs: missing-features, homophily
- **feature-propagation.1** Feature Propagation (FP) minimises Dirichlet energy, giving a diffusion-type PDE on the graph whose discretisation reconstructs missing features from observed neighbours: a simple, fast, scalable algorithm.
  conf: not stated · class: not stated · holds: graphs whose nodes have missing features · src: rossiUnreasonableEffectivenessFeature2022 · rating: "Confidence: high (3-0)" · trail: GHOST §Strategies · from: GHOST:B-0009, GHOST:B-0012
- **feature-propagation.2** Feature Propagation is the graph/diffusion instance of recovering structure under missing high-dimensional data.
  conf: not stated · class: not stated · holds: the review's framing, linked to the vault note on missing-data imputation · src: none (the reviewer's framing; no source cited) · trail: GHOST §Strategies · from: GHOST:B-0010
- **feature-propagation.3** Feature Propagation's motivating setting is explicitly the partially-attributed, cold-start case ("age and gender available only for a small subset of users").
  conf: not stated · class: not stated · holds: the setting Rossi et al. (2022) motivate FP with · src: rossiUnreasonableEffectivenessFeature2022 · rating: "Confidence: high (3-0)" · trail: GHOST §Strategies · from: GHOST:B-0011, GHOST:B-0012, GHOST:R-0001
- **feature-propagation.4** Feature Propagation rests on a feature-homophily assumption and degrades on heterophilous graphs.
  conf: not stated · class: not stated · holds: heterophilous graphs; given as a caveat of Rossi et al. (2022) · src: rossiUnreasonableEffectivenessFeature2022 (caveat) · trail: GHOST §Degradation · from: GHOST:B-0030, GHOST:R-0001
- **feature-propagation.5** Feature Propagation outperformed prior missing-feature methods on seven benchmarks; this is a 2022 historical fact, not current state of the art.
  conf: not stated · class: not stated · holds: the seven benchmarks of Rossi et al. (2022); homophilous, sparse, MCAR benchmarks, mostly author-reported; a 2022 result · src: rossiUnreasonableEffectivenessFeature2022 · trail: GHOST §Degradation, §Standing caveats · from: GHOST:B-0020, GHOST:B-0029, GHOST:B-0052, GHOST:R-0001
- **feature-propagation.6** Feature Propagation is now a baseline, superseded as state of the art by PCFI, DART and others.
  conf: not stated · class: not stated · holds: the field at the time of the review · src: none (the reviewer's statement; no source cited) · trail: GHOST §Degradation · from: GHOST:B-0021
- **feature-propagation.7** Propagation produces low-variance, near-constant channels that contribute little downstream; this is established with empirical evidence and a theoretical proof, and independently corroborated at a second venue.
  conf: repl (note: "independently corroborated at a second venue") · class: meas/deriv (note: "established with empirical evidence and a theoretical proof") · holds: propagation-based feature imputation; both sources are 2025 papers among the note's preprints or under-review sources · src: umPropagateInjectRevisiting2025 (preprint / under review), anonymousLowVarianceBottleneck2025 (preprint / under review) · rating: "proven" · trail: GHOST §Verdict, §Bounding · from: GHOST:A-007, GHOST:B-0036, GHOST:B-0050, GHOST:R-0012, GHOST:R-0016
- **feature-propagation.8** The low-variance defect bounds propagation but does not refute it: the high-variance channels do the work.
  conf: not stated · class: not stated · holds: propagation-based feature imputation · src: none (the reviewer's reading of the low-variance finding) · trail: GHOST §Bounding · from: GHOST:B-0036, GHOST:B-0037

### model-internal-imputation: Model-internal imputation (GCNMF)
needs: missing-features
- **model-internal-imputation.1** GCNMF folds Gaussian-mixture imputation inside a GCN.
  conf: not stated · class: not stated · holds: graphs with missing node features · src: chenLearningAttributeMissingGraphs2022 · trail: GHOST §Strategies · from: GHOST:B-0013
- **model-internal-imputation.2** Model-internal imputation is the strategy that fails badly under high missingness.
  conf: not stated · class: not stated · holds: high missingness · src: none (the reviewer's summary of the high-missingness figures) · trail: GHOST §Strategies · from: GHOST:B-0013, GHOST:B-0014

### joint-reconstruction: Dynamic or joint reconstruction of attributes and structure
needs: missing-features
- **joint-reconstruction.1** "Attribute-missing graph" methods jointly reconstruct attributes and update structure via alternating optimisation (EGS), rather than imputing a fixed mean or zero on a static graph.
  conf: not stated · class: not stated · holds: attribute-missing graphs · src: chenLearningAttributeMissingGraphs2022, songDynamicGraphStructure2025 · rating: "Confidence: high (3-0 / 2-1)" · trail: GHOST §Strategies · from: GHOST:B-0017, GHOST:B-0018

### structure-only-embedding: Structure-only (positional) embedding
needs: missing-features
- **structure-only-embedding.1** A distinct family of methods consumes only topology (LLE, Laplacian Eigenmaps, Graph Factorisation, GraRep, HOPE, DeepWalk, node2vec, SDNE, DNGR, LINE), operating on adjacency or similarity matrices; attribute-joint methods are treated as a separate, newer line.
  conf: not stated · class: not stated · holds: the classical methods of a 2018 survey · src: goyalGraphEmbeddingTechniques2018 · rating: "Confidence: high (3-0)" · trail: GHOST §Strategies · from: GHOST:B-0015, GHOST:B-0016, GHOST:B-0051
- **structure-only-embedding.2** The structure-only taxonomy rests on a 2018 survey; its topology-only characterisation of those classical methods remains accurate, but the field has expanded since.
  conf: not stated · class: not stated · holds: the classical structure-only methods; a 2018 survey · src: goyalGraphEmbeddingTechniques2018 · trail: GHOST §Standing caveats · from: GHOST:B-0051
- **structure-only-embedding.3** Structure-only embeddings are regime-dependent with no single winner, though higher-order-proximity methods generally win.
  conf: not stated · class: not stated · holds: the structure-only methods compared in a 2018 survey · src: goyalGraphEmbeddingTechniques2018 · trail: GHOST §Bounding · from: GHOST:B-0040, GHOST:B-0051
- **structure-only-embedding.4** node2vec leads on node classification yet loses on a structured SBM graph where labels reflect communities and there is no structural equivalence between nodes.
  conf: not stated · class: not stated · holds: node classification, and a structured SBM graph with community labels and no structural equivalence; from a 2018 survey · src: goyalGraphEmbeddingTechniques2018 · trail: GHOST §Bounding · from: GHOST:B-0040, GHOST:B-0051

### positional-vs-structural: Positional and structural node representations
needs: structure-only-embedding
- **positional-vs-structural.1** GNNs cannot capture position when node features are absent or identical: structurally isomorphic but positionally distinct nodes get identical embeddings, which is strictly true in the featureless or identical-feature regime.
  conf: not stated · class: not stated · holds: GNNs with absent or identical node features · src: youPositionawareGraphNeural2019 · trail: GHOST §Bounding · from: GHOST:B-0041
- **positional-vs-structural.2** Positional embeddings are formally samples from a G-equivariant distribution whose expectation is the structural representation; this formal sampling relationship and its directionality (positional = samples of structural) survived verification.
  conf: not stated · class: deriv (note: "Positional embeddings are formally samples") · holds: the formal relationship between positional embeddings and structural representations, not their interchangeability for tasks · src: srinivasanEquivalencePositionalNode2020 · trail: GHOST §Bounding, §Refuted · from: GHOST:B-0042, GHOST:C-002

### benchmark-regime: The benchmark regime (homophilous, sparse, MCAR)
needs: missing-features, homophily, missingness-mechanism, feature-propagation
- **benchmark-regime.1** The robustness numbers for imputing missing node features are measured almost entirely on homophilous, sparse bag-of-words citation and co-purchase graphs (Cora, Citeseer, PubMed, Photo) under Missing-Completely-At-Random missingness, and many are self-reported by the method authors.
  conf: not stated · class: not stated · holds: the robustness figures of Rossi et al. (2022), Lei et al. (2023) and Song et al. (2025) · src: rossiUnreasonableEffectivenessFeature2022, leiSelfsupervisedGuidedHypergraph2023, songDynamicGraphStructure2025 · trail: GHOST §Verdict, §Degradation · from: GHOST:A-005, GHOST:B-0029, GHOST:R-0001, GHOST:R-0003, GHOST:R-0008
- **benchmark-regime.2** High feature sparsity provably bounds the information loss from missingness, "making all models appear robust and preventing a meaningful comparison": on standard benchmarks all models look robust and cannot be distinguished.
  conf: not stated · class: deriv (note: "provably bounds") · holds: standard benchmarks with high feature sparsity; a 2026 result, under review · src: ferriniRethinkingGNNsMissing2026 (preprint / under review) · rating: "proven" · trail: GHOST §Verdict, §Bounding · from: GHOST:A-006, GHOST:B-0038, GHOST:B-0050
- **benchmark-regime.3** The dominance of propagation on standard benchmarks may therefore be an artifact, not a regime-general property.
  conf: not stated · class: not stated · holds: standard benchmarks with high feature sparsity · src: ferriniRethinkingGNNsMissing2026 · trail: GHOST §Verdict · from: GHOST:A-006
- **benchmark-regime.4** Dense-feature and non-MCAR (MNAR) regimes are under-evaluated.
  conf: not stated · class: not stated · holds: evaluation of methods for missing node features · src: ferriniRethinkingGNNsMissing2026 · trail: GHOST §Bounding · from: GHOST:B-0038
- **benchmark-regime.5** Ferrini et al. argue that standard benchmarks cannot answer whether propagation's robustness survives on dense, semantically meaningful features and structural or feature-dependent (MNAR) missingness, and introduce new protocols, but cross-method results are not yet established.
  conf: not stated · class: not stated · holds: dense features and MNAR missingness · src: ferriniRethinkingGNNsMissing2026 · trail: GHOST §Open Questions · from: GHOST:B-0046, GHOST:B-0047

### degradation: Degradation as the featureless fraction rises
needs: feature-propagation, model-internal-imputation, joint-reconstruction, structure-only-embedding, benchmark-regime
- **degradation.1** Diffusion/propagation imputation (Feature Propagation and variants) reconstructs entirely-missing node features from observed neighbours and degrades only marginally, about 2–4% relative node-classification accuracy at 99% missing, while model-internal imputation (GCNMF) collapses to about 35% on the same benchmark.
  conf: repl (note: "The single most replicated empirical result") · class: meas (note: "empirical result") · holds: homophilous, sparse bag-of-words citation and co-purchase graphs (Cora, Citeseer, PubMed, Photo) under Missing-Completely-At-Random missingness, many figures self-reported by the method authors; the 2–4% range is the note's, across Feature Propagation and its variants; the unscoped version was killed in verification · src: rossiUnreasonableEffectivenessFeature2022, leiSelfsupervisedGuidedHypergraph2023, chenLearningAttributeMissingGraphs2022 · trail: GHOST §Verdict, §Refuted · from: GHOST:A-002, GHOST:A-005, GHOST:C-001
- **degradation.2** Feature Propagation loses on average about 4% relative node-classification accuracy at 99% missing across seven benchmarks.
  conf: not stated · class: meas (note: "across seven benchmarks") · holds: seven benchmarks, 99% of node features missing; homophilous, sparse, MCAR, mostly author-reported · src: rossiUnreasonableEffectivenessFeature2022 · trail: GHOST §Degradation · from: GHOST:B-0020, GHOST:B-0029
- **degradation.3** SGHFP, a hypergraph variant of feature propagation, loses on average 2.67% relative accuracy at 99% missing across four datasets.
  conf: not stated · class: meas (note: "across four datasets") · holds: four datasets, 99% missing; homophilous, sparse, MCAR, mostly author-reported · src: leiSelfsupervisedGuidedHypergraph2023 · rating: "Confidence: high (3-0)" · trail: GHOST §Degradation · from: GHOST:B-0022, GHOST:B-0023, GHOST:B-0029
- **degradation.4** Per dataset at 99% missing, SGHFP goes from 81.23 to 79.41 on Cora (−2.25%), from 91.73 to 87.73 on Photo (−4.36%, the worst case) and from 77.36 to 74.29 on PubMed (−3.97%).
  conf: not stated · class: meas (note: "verified per-dataset from Table 2") · holds: Cora, Photo and PubMed, 99% missing, from Table 2 of Lei et al. (2023); homophilous, sparse, MCAR, mostly author-reported · src: leiSelfsupervisedGuidedHypergraph2023 · rating: "Confidence: high (3-0)" · trail: GHOST §Degradation · from: GHOST:B-0022, GHOST:B-0023, GHOST:B-0029, GHOST:R-0003
- **degradation.5** At 99% missing on Cora, propagation sits at about 78–79%.
  conf: not stated · class: meas (note: "Contrast at 99% missing on Cora") · holds: Cora, 99% missing; homophilous, sparse, MCAR, mostly author-reported · src: rossiUnreasonableEffectivenessFeature2022, leiSelfsupervisedGuidedHypergraph2023 · rating: "Confidence: high (3-0 / 2-1)" · trail: GHOST §Degradation · from: GHOST:B-0024, GHOST:B-0026, GHOST:B-0029
- **degradation.6** At 99% missing on Cora, GCNMF scores 34.54%, a figure confirmed by two independent papers.
  conf: repl (note: "confirmed by two independent papers") · class: meas (note: "Contrast at 99% missing on Cora") · holds: Cora, 99% missing; homophilous, sparse, MCAR, mostly author-reported · src: rossiUnreasonableEffectivenessFeature2022, leiSelfsupervisedGuidedHypergraph2023 · rating: "Confidence: high (3-0 / 2-1)" · trail: GHOST §Degradation · from: GHOST:B-0024, GHOST:B-0026, GHOST:B-0029
- **degradation.7** At 99% missing on Cora, PaGNN sits at about 58%: low, but not the catastrophic collapse of GCNMF.
  conf: not stated · class: meas (note: "Contrast at 99% missing on Cora") · holds: Cora, 99% missing; homophilous, sparse, MCAR, mostly author-reported · src: chenLearningAttributeMissingGraphs2022 · rating: "Confidence: high (3-0 / 2-1)" · trail: GHOST §Degradation · from: GHOST:B-0024, GHOST:B-0025, GHOST:B-0026, GHOST:B-0029
- **degradation.8** EGS degrades gently against a PAGNN baseline on Cora from 5% to 75% missing (baseline 81.36 to 74.05; EGS 84.77 to 82.13).
  conf: not stated · class: not stated · holds: Cora, 5% to 75% missing; self-reported by the method's authors; homophilous, sparse, MCAR · src: songDynamicGraphStructure2025 (self-reported) · rating: "Confidence: high" · trail: GHOST §Degradation · from: GHOST:B-0027, GHOST:B-0028, GHOST:B-0029
- **degradation.9** Degradation is quantified within propagation but never located against structure-only baselines across regimes.
  conf: not stated · class: search (note: "never located against structure-only baselines") · holds: the featureless fraction or graph sparsity at which neighbour aggregation would lose to structure-only embedding · src: none (an absence in the reviewed literature) · search: not stated · trail: GHOST §Open Questions · from: GHOST:B-0048, GHOST:B-0049

### contamination: Contamination of feature-bearing nodes
needs: feature-propagation, joint-reconstruction, structure-only-embedding
- **contamination.1** No controlled benchmark measures whether imputed or structure-only nodes contaminate the clusters of feature-bearing nodes: no controlled head-to-head and no controlled mixed-population benchmark was found.
  conf: not stated · class: search (note: "No controlled head-to-head was found") · holds: mixed populations of feature-bearing and imputed or structure-only nodes (brief item 3) · src: none (an absence: no source measured it) · search: searched, not found (note: "No controlled head-to-head was found") · trail: GHOST §Verdict, §Contamination, §Open Questions · from: GHOST:A-009, GHOST:B-0031, GHOST:B-0043, GHOST:B-0044
- **contamination.2** Song et al. argue, by molecular-graph analogy, that severe missingness "can alter the semantic information of the graph, leading to changes in the graph structure", which is why they update structure jointly; this is a theoretical, motivational statement, not a measured demonstration that featureless nodes distort feature-bearing nodes' clusters.
  conf: not stated · class: assert (note: "This is a theoretical/motivational statement") · holds: indirect and motivational support only, by molecular-graph analogy · src: songDynamicGraphStructure2025 (indirect and motivational) · rating: "verification vote 2-1" · trail: GHOST §Contamination · from: GHOST:B-0031, GHOST:B-0032, GHOST:B-0033

### layout-distortion: Layout distortion on mixed populations
needs: structure-only-embedding, positional-vs-structural
- **layout-distortion.1** No reviewed source measured layout distortion on mixed populations: the visualization search angle returned sources, but none yielded a confirmed claim tying topology-only node placement to distortion artifacts (centroid piling, hub collapse) on mixed attributed and featureless populations.
  conf: not stated · class: search (note: "No reviewed source measured this") · holds: topology-only node placement on mixed attributed and featureless populations (brief item 4) · src: none (an absence: no source measured it) · search: searched, not found (note: "The visualization search angle returned sources but none yielded a confirmed claim") · trail: GHOST §Verdict, §Layout distortion, §Open Questions · from: GHOST:A-009, GHOST:B-0034, GHOST:B-0035, GHOST:B-0045
- **layout-distortion.2** The strategy of laying out topology separately and then mapping it onto attribute space surfaced only as the conceptual positional-vs-structural distinction, not as a benchmarked layout pipeline.
  conf: not stated · class: search (note: "not as a benchmarked layout pipeline") · holds: the strategy as named in the brief · src: srinivasanEquivalencePositionalNode2020, youPositionawareGraphNeural2019 · search: searched, not found (note: "surfaced only as the conceptual positional-vs-structural distinction") · trail: GHOST §Strategies · from: GHOST:B-0019

### default-strategy: Which strategy is a defensible default
needs: degradation, benchmark-regime, feature-propagation, structure-only-embedding, contamination, layout-distortion
- **default-strategy.1** The answer is regime-dependent: neighbour feature propagation is a defensible default only in the homophilous, sparse-feature regime where its robustness has actually been demonstrated.
  conf: not stated · class: not stated · holds: the review's verdict (c) · src: none (the review's verdict) · contrary: not stated · trail: GHOST §Verdict · from: GHOST:A-001
- **default-strategy.2** Propagation's marginal degradation, against the collapse of model-internal imputation, looks like a clean win for option (a), but it is not, for three reasons the verification surfaced and confirmed: the robustness numbers are regime-bound, a 2026 result proves the benchmark itself hides the differences, and propagation has a proven low-variance defect.
  conf: not stated · class: not stated · holds: the review's verdict on option (a) · src: none (the review's verdict) · contrary: not stated · trail: GHOST §Verdict · from: GHOST:A-002, GHOST:A-003, GHOST:A-004, GHOST:A-005, GHOST:A-006, GHOST:A-007
- **default-strategy.3** Propagation is the right default where the graph is homophilous and features are sparse; outside that regime the evidence does not support it as a default, and structure-only or positional embedding becomes a live alternative whose performance is itself strongly regime-dependent with no single winner.
  conf: not stated · class: not stated · holds: the review's verdict; structure-only or positional embedding is option (b) · src: goyalGraphEmbeddingTechniques2018, srinivasanEquivalencePositionalNode2020, youPositionawareGraphNeural2019 · contrary: not stated · trail: GHOST §Verdict · from: GHOST:A-008

## Do not say
- **dns.1** "Feature Propagation's robustness, about 4% loss at 99% missing features, is a general fact."
  why: This unscoped claim was killed in verification (vote 1-2); only the version scoped to homophilous, sparse, MCAR benchmarks survives. · instead: degradation.1, degradation.2 · trail: GHOST §Refuted · from: GHOST:C-001
- **dns.2** "Positional and structural representations are practically interchangeable for tasks."
  why: This was killed in verification (vote 0-3); only the formal sampling relationship and its directionality (positional embeddings are samples of the structural representation) survived. · instead: positional-vs-structural.2 · trail: GHOST §Refuted · from: GHOST:C-002
- **dns.3** "Song et al. showed that featureless nodes distort the clusters of feature-bearing nodes."
  why: Song et al.'s statement is theoretical and motivational, argued by molecular-graph analogy (verification vote 2-1), not a measured demonstration, and the note says to cite it as indirect only. · instead: contamination.1, contamination.2 · trail: GHOST §Contamination · from: GHOST:B-0031, GHOST:B-0032, GHOST:B-0033
- **dns.4** "The absence of evidence on contamination and layout distortion counts in favour of one of the options."
  why: The note says to report the two unanswered questions as "no controlled evidence found", not as a point in favour of any option. · instead: contamination.1, layout-distortion.1 · trail: GHOST §Verdict · from: GHOST:A-009, GHOST:A-010
- **dns.5** "Feature Propagation outperforms previous methods and is the state of the art for missing node features."
  why: That Feature Propagation outperforms previous methods is a 2022 historical fact, not current state of the art; it is now a baseline, superseded by PCFI, DART and others. · instead: feature-propagation.5, feature-propagation.6 · trail: GHOST §Degradation, §Standing caveats · from: GHOST:B-0021, GHOST:B-0052

## Gaps
- **gap.1** The review's findings were never checked by a second reader: the figures its answers rest on (propagation's 2–4% relative accuracy loss at 99% missing, GCNMF's collapse to about 35% on the same benchmark, the sparsity bound on information loss and the low-variance defect) went through the harness's own 3-vote verification only, and the note records only its refutations.
  blocks: degradation, default-strategy, benchmark-regime · origin: no critique; the note records only the two claims killed in verification (3-vote, 25 of 96 extracted claims verified) · search: not stated · from: GHOST:A-002, GHOST:A-006, GHOST:A-007, GHOST:B-0001
- **gap.2** Does inserting imputed or structure-only nodes measurably distort the clusters of feature-bearing nodes?
  blocks: contamination, default-strategy · origin: open question of the review (brief item 3); no controlled mixed-population benchmark · search: searched, not found (note: "No controlled mixed-population benchmark found") · trail: GHOST §Open Questions · from: GHOST:B-0043, GHOST:B-0044
- **gap.3** Layout distortion (centroid piling, hub collapse) on mixed populations of attributed and featureless nodes.
  blocks: layout-distortion, default-strategy · origin: open question of the review (brief item 4) · search: searched, not found (note: "unmeasured in the retrieved corpus") · trail: GHOST §Open Questions · from: GHOST:B-0045
- **gap.4** Does propagation's robustness survive on dense, semantically meaningful features and on structural or feature-dependent (MNAR) missingness?
  blocks: benchmark-regime, default-strategy · origin: open question of the review; Ferrini et al. introduce new protocols, but cross-method results are not yet established · search: not stated · src: ferriniRethinkingGNNsMissing2026 · trail: GHOST §Open Questions · from: GHOST:B-0046, GHOST:B-0047
- **gap.5** At what featureless fraction or graph sparsity does neighbour aggregation become too sparse to help and lose to structure-only embedding?
  blocks: degradation, default-strategy · origin: open question of the review; degradation is quantified within propagation but never located against structure-only baselines across regimes · search: not stated · trail: GHOST §Open Questions · from: GHOST:B-0048, GHOST:B-0049

## Out of scope

## Sources
```bibtex
@inproceedings{rossiUnreasonableEffectivenessFeature2022,
  author = {Rossi, E. and Kenlay, H. and Gorinova, M. I. and Chamberlain, B. P. and Dong, X. and Bronstein, M. M.},
  title = {On the Unreasonable Effectiveness of Feature Propagation in Learning on Graphs with Missing Node Features},
  booktitle = {Proceedings of the First Learning on Graphs Conference (LoG 2022)},
  series = {PMLR},
  volume = {198},
  pages = {11:1--11:16},
  year = {2022},
  eprint = {2111.12128},
  archiveprefix = {arXiv},
  url = {https://proceedings.mlr.press/v198/rossi22a.html},
  note = {access: not stated; cited as: GHOST [R1]}
}
@inproceedings{leiSelfsupervisedGuidedHypergraph2023,
  author = {Lei, C. and Fu, J. and Wang, X. and Qiu, X. and Hu, Z. and Peng, Y. and You, J.},
  title = {Self-supervised Guided Hypergraph Feature Propagation for Semi-supervised Classification with Missing Node Features},
  booktitle = {ICASSP 2023 -- IEEE International Conference on Acoustics, Speech and Signal Processing},
  year = {2023},
  eprint = {2302.08250},
  archiveprefix = {arXiv},
  url = {https://arxiv.org/abs/2302.08250},
  note = {access: not stated; cited as: GHOST [R2]}
}
@article{chenLearningAttributeMissingGraphs2022,
  author = {Chen, X. and Chen, S. and Yao, J. and Zheng, H. and Zhang, Y. and Tsang, I. W.},
  title = {Learning on Attribute-Missing Graphs},
  journal = {IEEE Transactions on Pattern Analysis and Machine Intelligence},
  volume = {44},
  number = {2},
  pages = {740--757},
  year = {2022},
  doi = {10.1109/TPAMI.2020.3032189},
  eprint = {2011.01623},
  archiveprefix = {arXiv},
  url = {https://arxiv.org/abs/2011.01623},
  note = {access: not stated; cited as: GHOST [R3]}
}
@article{songDynamicGraphStructure2025,
  author = {Song and Zhou and Wang and Liu and others},
  title = {Dynamic graph structure evolution for node classification with missing attributes},
  journal = {Scientific Reports},
  volume = {15},
  year = {2025},
  doi = {10.1038/s41598-025-09840-z},
  url = {https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12264138/},
  note = {access: not stated; cited as: GHOST [R4]; PMC12264138; incomplete: author (the note gives "Song, [et al.], Zhou, Wang, Liu" and says the author list is partial), pages}
}
@inproceedings{umPropagateInjectRevisiting2025,
  author = {Um, D. and Kim, J. and Park and Lim and Ahn and Park and others},
  title = {Propagate and Inject: Revisiting Propagation-Based Feature Imputation for Graphs with Partially Observed Features},
  booktitle = {ICML 2025},
  year = {2025},
  url = {https://openreview.net/forum?id=QfKrcgyase},
  note = {access: not stated; type: preprint or under review (the note: "2025–2026 preprints / under-review"); cited as: GHOST [R5]; OpenReview id=QfKrcgyase; code: github.com/daehoum1/fisf; incomplete: author (the note gives "Um, D., Kim, J., Park, [et al.], Lim, Ahn, Park" and says the author list is partial), pages}
}
@inproceedings{anonymousLowVarianceBottleneck2025,
  author = {Anonymous},
  title = {Low Variance: A Bottleneck in Diffusion-Based Graph Imputation},
  booktitle = {ICLR 2025 track},
  year = {2025},
  url = {https://openreview.net/forum?id=4dhTYe5pjD},
  note = {access: not stated; type: preprint or under review (the note: "2025–2026 preprints / under-review"); cited as: GHOST [R6]; OpenReview id=4dhTYe5pjD; incomplete: author (given as Anonymous), pages}
}
@misc{ferriniRethinkingGNNsMissing2026,
  author = {Ferrini, F. and Lachi, V. and Longa, A. and Lepri, B. and Akiyoshi and Passerini, A. and Liu and Jaeger and others},
  title = {Rethinking GNNs and Missing Features: Challenges, Evaluation and a Robust Solution},
  year = {2026},
  eprint = {2601.04855},
  archiveprefix = {arXiv},
  url = {https://arxiv.org/abs/2601.04855},
  note = {access: not stated; type: preprint, under review (the note: "Jan 2026; under review, OpenReview gvFOB8VCMr"); cited as: GHOST [R7]; incomplete: author (the note gives "Ferrini, F., Lachi, V., Longa, A., Lepri, B., Akiyoshi, [et al.], Passerini, A., Liu, Jaeger" and says the author list is partial)}
}
@article{goyalGraphEmbeddingTechniques2018,
  author = {Goyal, P. and Ferrara, E.},
  title = {Graph Embedding Techniques, Applications, and Performance: A Survey},
  journal = {Knowledge-Based Systems},
  volume = {151},
  pages = {78--94},
  year = {2018},
  doi = {10.1016/j.knosys.2018.03.022},
  eprint = {1705.02801},
  archiveprefix = {arXiv},
  note = {access: not stated; type: survey (the note: "a 2018 survey"); cited as: GHOST [R8]}
}
@inproceedings{srinivasanEquivalencePositionalNode2020,
  author = {Srinivasan, B. and Ribeiro, B.},
  title = {On the Equivalence between Positional Node Embeddings and Structural Graph Representations},
  booktitle = {ICLR 2020},
  year = {2020},
  eprint = {1910.00452},
  archiveprefix = {arXiv},
  url = {https://arxiv.org/abs/1910.00452},
  note = {access: not stated; cited as: GHOST [R9]}
}
@inproceedings{youPositionawareGraphNeural2019,
  author = {You, J. and Ying, R. and Leskovec, J.},
  title = {Position-aware Graph Neural Networks},
  booktitle = {Proceedings of the 36th International Conference on Machine Learning (ICML 2019)},
  series = {PMLR},
  volume = {97},
  year = {2019},
  eprint = {1906.04817},
  archiveprefix = {arXiv},
  url = {https://arxiv.org/abs/1906.04817},
  note = {access: not stated; cited as: GHOST [R10] (as "Position-aware Graph Neural Networks (P-GNN)")}
}
@inproceedings{zhuBeyondHomophilyGraph2020,
  author = {Zhu, Jiong and Yan, Yujun and Zhao, Lingxiao and Heimann, Mark and Akoglu, Leman and Koutra, Danai},
  title = {Beyond Homophily in Graph Neural Networks: Current Limitations and Effective Designs},
  booktitle = {Advances in Neural Information Processing Systems (NeurIPS 2020)},
  year = {2020},
  eprint = {2006.11468},
  archiveprefix = {arXiv},
  url = {https://arxiv.org/abs/2006.11468},
  note = {background; access: abstract_only (checked on arXiv)}
}
@book{littleStatisticalAnalysisMissing2019,
  author = {Little, Roderick J. A. and Rubin, Donald B.},
  title = {Statistical Analysis with Missing Data},
  edition = {Third},
  publisher = {Wiley},
  year = {2019},
  doi = {10.1002/9781119482260},
  note = {background; access: not_obtained (Crossref record and table of contents only)}
}
```
