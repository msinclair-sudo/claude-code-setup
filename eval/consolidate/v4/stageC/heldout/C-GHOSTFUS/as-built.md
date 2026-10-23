---
type: knowledge
title: Featureless ghost nodes in anchored graph-diffusion fusion
inputs:
  - C-GHOSTFUS: PhD/biblion/research/results/Featureless Ghost Nodes in Anchored Graph-Diffusion Fusion_ A Ve.md
answers:
  - C-GHOSTFUS: §TL;DR, §Key Findings
refs: PhD/Proposal/Refs/Refs.bib
built: 2026-10-24
status: draft
tags:
  - research
  - knowledge
---

# Featureless ghost nodes in anchored graph-diffusion fusion

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
| C-GHOSTFUS | [[Featureless Ghost Nodes in Anchored Graph-Diffusion Fusion_ A Ve]] | no | narrative author-year | no | no | fallback (answers and critique; the note has no labelled citations) |

## Concepts

### ghost-nodes: featureless ("ghost") nodes in biblion's citation graph
needs: none

- **ghost-nodes.1** biblion has structural (whole-node) missingness, dense features, and about 70% featureless nodes at degree >= 2.
  conf: not stated · class: not stated · holds: biblion's citation graph at a degree threshold of >= 2 · src: none (the note's description of biblion) · trail: C-GHOSTFUS §Key Findings · from: C-GHOSTFUS:A-008
- **ghost-nodes.2** In the fallworm example there are 3,392 ghosts against 1,405 real nodes at degree >= 2.
  conf: not stated · class: not stated · holds: the fallworm graph at degree >= 2 · src: none (the note's description of biblion) · trail: C-GHOSTFUS §Q2 · from: C-GHOSTFUS:B-0033
- **ghost-nodes.3** biblion's features are SPECTER2 embeddings (768-d, dense, semantic), and its downstream is unsupervised clustering with UMAP and HDBSCAN.
  conf: not stated · class: not stated · holds: the biblion pipeline · src: none (the note's description of biblion) · trail: C-GHOSTFUS §Q2, §Caveats, §Q1 · from: C-GHOSTFUS:B-0014, C-GHOSTFUS:B-0030, C-GHOSTFUS:B-0118

### appnp-propagation: APPNP (personalized-PageRank) propagation
needs: none

- **appnp-propagation.1** APPNP's closed form, h = alpha(I - (1-alpha)D^-1 A)^-1 X, is a personalized-PageRank random walk with restart, so a path through a shared intermediary does contribute to the stationary similarity between A and B.
  conf: not stated · class: not stated · holds: the APPNP propagation operator · src: anon (cited by URL) · trail: C-GHOSTFUS §Q1 · from: C-GHOSTFUS:B-0003
- **appnp-propagation.2** APPNP's teleport term (alpha = 0.3 in biblion) is specifically designed to resist oversmoothing by re-anchoring each node to X each step, which is good for real nodes but is exactly what a ghost node lacks.
  conf: not stated · class: not stated · holds: biblion's APPNP with alpha = 0.3 · src: none (the reviewer's reasoning) · trail: C-GHOSTFUS §Q1 · from: C-GHOSTFUS:B-0010..0011

### feature-propagation: feature propagation (FP) and its relatives
needs: none

- **feature-propagation.bg1** Data are missing completely at random (MCAR) when the probability of the missingness pattern, given the data, does not depend on the data.
  kind: background · ref: seamanWhatMeantMissing2013 · check: DOI 10.1214/13-STS415 resolves on Crossref (Seaman, Galati, Jackson and Carlin 2013, Statistical Science 28(2):257-268); defined in Section 2 ("Two Definitions of MAR and MCAR", realised and everywhere MCAR), read in arXiv:1306.2812
- **feature-propagation.1** Rossi et al. (LoG 2022) report only a 4.12% relative accuracy drop at 99% missing features, explicitly under MCAR per-channel masking on homophilous benchmarks.
  conf: not stated · class: not stated · holds: MCAR per-channel masking; homophilous, sparse-feature benchmarks; node-classification accuracy · src: rossiUnreasonableEffectivenessFeature2022 · trail: C-GHOSTFUS §Key Findings, §Caveats · from: C-GHOSTFUS:A-001, C-GHOSTFUS:A-008, C-GHOSTFUS:B-0118
- **feature-propagation.2** Rossi et al. note that feature propagation degrades toward the zero baseline as homophily falls.
  conf: not stated · class: not stated · holds: their benchmarks, as homophily decreases · src: rossiUnreasonableEffectivenessFeature2022 · trail: C-GHOSTFUS §Key Findings · from: C-GHOSTFUS:A-008
- **feature-propagation.3** Rossi et al. observe that "most methods perform extremely well up to 50% of missing features, suggesting that in general node features are redundant... The gap between methods opens up from around 60% of missing features, and is particularly large for extremely high rates of missing features (90% or 99%): FP is the only feature-aware method which is robust to these high rates on all datasets."
  conf: not stated · class: not stated · holds: their benchmarks (sparse features, MCAR masking, node-classification accuracy); FP is the only method shown robust past 90% missing on the tested benchmarks · src: rossiUnreasonableEffectivenessFeature2022 · trail: C-GHOSTFUS §Q2, §Key Findings, §Recommendations · from: C-GHOSTFUS:A-011, C-GHOSTFUS:B-0024..0025, C-GHOSTFUS:B-0036, C-GHOSTFUS:B-0116
- **feature-propagation.4** Feature Propagation's steady state is independent (invariant) of the zero initialization of unknown features, because the diffusion resets known features each step and lets unknowns be determined purely by the boundary.
  conf: not stated · class: not stated · holds: FP with boundary reset · src: rossiUnreasonableEffectivenessFeature2022 · trail: C-GHOSTFUS §Q3, §Recommendations · from: C-GHOSTFUS:B-0058, C-GHOSTFUS:B-0116
- **feature-propagation.5** PCFI's confidence weighting uses the channel-wise shortest-path distance to the nearest observed node; the review calls it a ready-made way to down-weight deep-ghost anchors.
  conf: not stated · class: not stated · holds: PCFI imputation · src: umConfidenceBasedFeatureImputation2023 · trail: C-GHOSTFUS §Recommendations · from: C-GHOSTFUS:B-0117

### missingness-regime: sparse against dense, uniform against structural missingness
needs: feature-propagation, ghost-nodes

- **missingness-regime.1** The published feature-propagation robustness results (Rossi et al., LoG 2022) cover homophilous, MCAR, mostly-sparse-feature, small-to-moderate-missing-fraction regimes, none of which match biblion's ~70%-featureless, dense-SPECTER2-feature, structural-missingness regime: the "proven zone" for feature propagation does not include biblion's regime.
  conf: not stated · class: not stated · holds: published FP results against biblion's regime · src: rossiUnreasonableEffectivenessFeature2022 · trail: C-GHOSTFUS §TL;DR, §Key Findings · from: C-GHOSTFUS:A-001, C-GHOSTFUS:A-008
- **missingness-regime.2** All four of the review's questions are at best partially demonstrated and at worst genuinely open.
  conf: not stated · class: not stated · holds: the review's four questions · src: none (the review's overall verdict) · trail: C-GHOSTFUS §TL;DR · rating: "at best PARTIALLY demonstrated and at worst genuinely open" · contrary: not stated · from: C-GHOSTFUS:A-001
- **missingness-regime.3** The headline robustness number (4.12% relative drop at 99% missing) is an MCAR, per-channel, sparse-feature, homophilous, node-classification-accuracy result, while biblion is structural (whole-node) missingness, dense SPECTER2 features, ~70% featureless and unsupervised clustering; the transfer is not warranted, and published thresholds are optimistic bounds.
  conf: not stated · class: not stated · holds: Rossi et al.'s benchmarks against biblion · src: rossiUnreasonableEffectivenessFeature2022 · trail: C-GHOSTFUS §Caveats · contrary: not stated · from: C-GHOSTFUS:B-0118..0119
- **missingness-regime.4** Ferrini et al. (2026, "Rethinking GNNs and Missing Features") prove that "in highly sparse settings, the mutual information between features and labels is barely affected by additional missingness, except at extremely high missing rates... with performance degrading only when more than 90% of entries are removed," and argue robustness cannot be meaningfully assessed when most features are already absent.
  conf: not stated · class: deriv (note: "prove") · holds: highly sparse feature settings · src: ferriniRethinkingGNNsMissing2026 (very recent preprint; limited independent replication) · trail: C-GHOSTFUS §Q2, §Caveats · from: C-GHOSTFUS:B-0028, C-GHOSTFUS:B-0126
- **missingness-regime.5** Ferrini et al.'s experiments show that methods that look robust on sparse bag-of-words features fail on dense, low-dimensional features.
  conf: not stated · class: not stated · holds: sparse bag-of-words against dense, low-dimensional features · src: ferriniRethinkingGNNsMissing2026 (very recent preprint; limited independent replication) · trail: C-GHOSTFUS §Q2 · from: C-GHOSTFUS:B-0028..0029, C-GHOSTFUS:B-0126
- **missingness-regime.6** Ferrini et al. work in the dense-feature regime and under structural missingness, but with mask-concatenation, not PCA ordering.
  conf: not stated · class: not stated · holds: dense features, structural missingness · src: ferriniRethinkingGNNsMissing2026 (cited by URL) · trail: C-GHOSTFUS §Q4 · from: C-GHOSTFUS:B-0094
- **missingness-regime.7** SPECTER2 (768-d, dense, semantic) is exactly the dense regime where the comfortable missing-fraction crossover may move sharply leftward.
  conf: not stated · class: not stated · holds: SPECTER2 features · src: none (the reviewer's reasoning) · trail: C-GHOSTFUS §Q2 · from: C-GHOSTFUS:B-0030
- **missingness-regime.8** Yun et al. (2024, "Oldie but Goodie") report that FP's performance-drop rate became steeper in structurally missing scenarios, because whole-node missingness means a ghost has no observed channel anywhere on the node.
  conf: not stated · class: not stated · holds: structural (whole-node) against uniform missingness · src: yunOldieButGoodie2024 · trail: C-GHOSTFUS §Q2 · from: C-GHOSTFUS:B-0031
- **missingness-regime.9** Structural missingness is biblion's exact case, which predicts that its crossover is worse than the 60% sparse-MCAR figure suggests.
  conf: not stated · class: not stated · holds: biblion's whole-node missingness · src: yunOldieButGoodie2024 · trail: C-GHOSTFUS §Q2 · from: C-GHOSTFUS:B-0031..0032

### washout: mechanisms that wash a bridge out downstream
needs: appnp-propagation, ghost-nodes

- **washout.bg1** UMAP (Uniform Manifold Approximation and Projection) is a manifold learning technique for dimension reduction.
  kind: background · ref: mcinnesUMAPUniformManifold2018 · check: arXiv:1802.03426 resolves (McInnes, Healy and Melville, first submitted 9 February 2018); the abstract's first sentence
- **washout.1** Um et al. (ICML 2025, "Propagate and Inject") prove that diffusion-based imputation methods "produce channels with nearly identical values within each channel, and these low-variance channels contribute very little to performance in graph learning tasks"; diffusion-based imputation provably produces low-variance, near-constant channels under high missingness. The review calls this the single most important finding: the mechanism biblion most needs to fear is documented.
  conf: not stated · class: deriv (note: "prove") · holds: diffusion-based imputation under high missingness · src: umPropagateInjectRevisiting2025 (very recent preprint; limited independent replication) · trail: C-GHOSTFUS §TL;DR, §Q1, §Caveats · from: C-GHOSTFUS:A-002..003, C-GHOSTFUS:B-0008, C-GHOSTFUS:B-0126
- **washout.2** A ghost node whose anchor is itself the diffusion average is exactly such a low-variance signal; pushing similarity between A and B through it can yield a near-constant contribution that carries little discriminative information.
  conf: not stated · class: not stated · holds: a ghost anchored to the diffusion average · src: none (the reviewer's reasoning) · trail: C-GHOSTFUS §Q1 · from: C-GHOSTFUS:B-0009
- **washout.3** Repeated aggregation is Laplacian smoothing: node features converge toward a degree-scaled constant vector and Dirichlet energy decays to zero.
  conf: not stated · class: not stated · holds: repeated aggregation (oversmoothing / variance collapse) · src: caiNoteOverSmoothingGraph2020, oonoGraphNeuralNetworks2020, anona (cited by URL) · trail: C-GHOSTFUS §Q1 · from: C-GHOSTFUS:B-0010..0011
- **washout.4** UMAP optimizes local-neighbor preservation, so if a bridge produces only a weak global pull between A and B, min_dist and n_neighbors settings can absorb it, and HDBSCAN's mutual-reachability core-distance can treat a thin bridge as noise.
  conf: not stated · class: not stated · holds: UMAP followed by HDBSCAN · src: none (the reviewer's reasoning) · trail: C-GHOSTFUS §Q1 · from: C-GHOSTFUS:B-0012

### co-citation-bridge: the co-citation bridge through a ghost
needs: appnp-propagation, washout

- **co-citation-bridge.1** The relationship A -> ghost -> B is encoded by construction: the bridge is real in the propagation operator.
  conf: not stated · class: not stated · holds: APPNP propagation · src: none (the reviewer's synthesis) · trail: C-GHOSTFUS §Q1, §Key Findings · from: C-GHOSTFUS:A-009, C-GHOSTFUS:B-0002, C-GHOSTFUS:B-0005
- **co-citation-bridge.2** Personalized-PageRank propagation (APPNP) does transmit similarity through shared intermediaries, and second-order proximity theory (LINE) confirms that shared-neighbor nodes should embed closely.
  conf: not stated · class: not stated · holds: in principle; not shown for a fabricated intermediary, the ~70%-ghost dense-feature regime or a UMAP+HDBSCAN downstream · src: tangLINELargescaleInformation2015 · trail: C-GHOSTFUS §Key Findings, §Q1 · from: C-GHOSTFUS:A-009, C-GHOSTFUS:B-0013..0014
- **co-citation-bridge.3** The bridge is the graph-diffusion analogue of second-order proximity: LINE (Tang et al., 2015) formalizes that nodes with shared neighbors are likely to be similar, and bibliographic-coupling/co-citation theory treats two documents sharing a cited third work as similar by construction.
  conf: not stated · class: not stated · holds: second-order proximity; bibliographic coupling and co-citation · src: tangLINELargescaleInformation2015 · trail: C-GHOSTFUS §Q1 · from: C-GHOSTFUS:B-0003
- **co-citation-bridge.4** Deep bibliographic coupling work extends coupling through graph diffusion precisely to densify sparse co-citation signal.
  conf: not stated · class: not stated · holds: citation graphs with sparse co-citation signal · src: none (the note names deep bibliographic coupling work without a reference) · trail: C-GHOSTFUS §Q1 · from: C-GHOSTFUS:B-0004
- **co-citation-bridge.5** All the positive evidence (LINE second-order proximity, APPNP propagation, deep bibliographic coupling) establishes only that shared intermediaries transmit similarity in principle; none of it covers the case where the intermediary's own vector is fabricated, nor the ~70%-ghost dense-feature regime, nor the specific UMAP+HDBSCAN downstream.
  conf: not stated · class: search (note: "None of it covers") · search: not stated · holds: the evidence the review located · src: tangLINELargescaleInformation2015 · trail: C-GHOSTFUS §Q1 · from: C-GHOSTFUS:B-0013..0014
- **co-citation-bridge.6** The 1-hop co-citation relationship through a ghost is encoded, but there is no direct evidence that it survives usefully downstream in biblion's regime, and there are strong mechanistic reasons to expect partial washout: downstream survival is the problem, and three documented mechanisms threaten it (low-variance collapse, oversmoothing / variance collapse, dimensionality reduction smoothing).
  conf: not stated · class: not stated · holds: biblion's regime: ~70% ghosts, dense features, UMAP and HDBSCAN downstream · src: umPropagateInjectRevisiting2025, caiNoteOverSmoothingGraph2020, oonoGraphNeuralNetworks2020 · trail: C-GHOSTFUS §Q1 · rating: "PARTIALLY DEMONSTRATED that the 1-hop relationship is encoded; NO DIRECT EVIDENCE that it survives usefully downstream in biblion's regime" · contrary: not stated · from: C-GHOSTFUS:B-0001, C-GHOSTFUS:B-0006..0008, C-GHOSTFUS:B-0010, C-GHOSTFUS:B-0012, C-GHOSTFUS:B-0014
- **co-citation-bridge.7** A fabricated or zero anchor on the bridge node injects a low-variance or origin-pulling signal that variance collapse and oversmoothing can wash out before UMAP/HDBSCAN ever see it.
  conf: not stated · class: not stated · holds: a ghost bridge node with a fabricated or zero anchor · src: none (the reviewer's synthesis) · trail: C-GHOSTFUS §Key Findings · from: C-GHOSTFUS:A-010
- **co-citation-bridge.8** The co-citation bridge provably contributes to the APPNP stationary similarity, but low-variance collapse, oversmoothing and UMAP/HDBSCAN can all erode it; only stage-wise measurement on biblion can settle whether it survives.
  conf: not stated · class: not stated · holds: biblion's pipeline · src: none (the reviewer's synthesis) · trail: C-GHOSTFUS §Caveats · from: C-GHOSTFUS:B-0121..0122
- **co-citation-bridge.9** A degree-2 ghost is a much weaker conduit than a degree-50 one.
  conf: not stated · class: not stated · holds: ghost nodes by degree · src: none (the reviewer's reasoning) · trail: C-GHOSTFUS §Q1 · from: C-GHOSTFUS:B-0020
- **co-citation-bridge.10** A bridge "preserved" only because A and B were already close via other paths is not evidence that the ghost did the work.
  conf: not stated · class: not stated · holds: real-real pairs with competing non-ghost paths · src: none (the reviewer's reasoning) · trail: C-GHOSTFUS §Q1 · from: C-GHOSTFUS:B-0020

### zero-anchor: zero-imputation and the origin pull
needs: appnp-propagation, ghost-nodes

- **zero-anchor.1** Yi et al. (ICLR 2020) prove the variable sparsity problem (VSP): with zero-imputation "the output of a predictive model largely varies with respect to the rate of missingness in the given input," scaling with the observed fraction, so that zero-imputation biases representation magnitude in proportion to the observed fraction; they correct it with Sparsity Normalization.
  conf: not stated · class: deriv (note: "prove") · holds: non-graph models, MCAR missingness · src: yiWhyNotUse2020 · trail: C-GHOSTFUS §Q3, §TL;DR, §Q4 · from: C-GHOSTFUS:A-003, C-GHOSTFUS:B-0049, C-GHOSTFUS:B-0092
- **zero-anchor.2** Yi et al. prove that output magnitude scales with the observed fraction (their Theorem 1: expected output proportional to mu_m).
  conf: not stated · class: deriv (note: "prove") · holds: non-graph models, MCAR missingness · src: yiWhyNotUse2020 · trail: C-GHOSTFUS §Q4 · from: C-GHOSTFUS:B-0079, C-GHOSTFUS:B-0092
- **zero-anchor.3** Yi et al. note that GCN's Laplacian normalization "precisely matches" their Sparsity Normalization operation, tying the mechanism directly to graph message passing.
  conf: not stated · class: not stated · holds: GCN Laplacian normalization · src: yiWhyNotUse2020 (cited by URL) · trail: C-GHOSTFUS §Q4 · from: C-GHOSTFUS:B-0079, C-GHOSTFUS:B-0081
- **zero-anchor.4** A zero-anchored ghost injects zeros into its neighbours' diffusion sums; in an averaging operator like D^-1 A it does what Rossi et al. describe for the Zero baseline ("the effect of zero-imputation is simply to reduce the norm of the average embeddings"), so it pulls its real neighbours toward the origin, distorting real-node geometry.
  conf: not stated · class: not stated · holds: an averaging operator such as D^-1 A with zero-anchored ghosts · src: rossiUnreasonableEffectivenessFeature2022 · trail: C-GHOSTFUS §Q3 · rating: "well supported" · from: C-GHOSTFUS:B-0047..0051, C-GHOSTFUS:B-0063

### degree-threshold: the degree threshold and the featureless fraction
needs: missingness-regime, co-citation-bridge

- **degree-threshold.1** A missing-fraction crossover exists, but the specific degree threshold for biblion is not established and the trade-off against discarded structure is unquantified in the literature.
  conf: not stated · class: not stated · holds: biblion's degree threshold · src: rossiUnreasonableEffectivenessFeature2022 · trail: C-GHOSTFUS §Q2 · rating: "PARTIALLY DEMONSTRATED that a missing-fraction crossover exists" · contrary: not stated · from: C-GHOSTFUS:B-0023..0024
- **degree-threshold.2** A degree-threshold crossover exists in principle but is dataset-specific: Rossi et al.'s observations identify a soft crossover near 50-60% missing on their benchmarks, an empirical, sparse-feature, MCAR, node-classification-accuracy (downstream-accuracy) observation that is not a guarantee for dense SPECTER2 geometry.
  conf: not stated · class: not stated · holds: sparse-feature benchmarks under MCAR masking; node-classification accuracy · src: rossiUnreasonableEffectivenessFeature2022 · trail: C-GHOSTFUS §Key Findings, §Q2 · from: C-GHOSTFUS:A-011..012, C-GHOSTFUS:B-0026, C-GHOSTFUS:B-0036
- **degree-threshold.3** biblion at ~70% featureless sits just beyond the crossover, in the region where only the strongest feature-aware methods (FP, PCFI) held up, and even those were tested under MCAR per-channel masking, not whole-node structural missingness.
  conf: not stated · class: not stated · holds: biblion's ~70% featureless fraction · src: rossiUnreasonableEffectivenessFeature2022, umConfidenceBasedFeatureImputation2023 · trail: C-GHOSTFUS §Q2 · from: C-GHOSTFUS:B-0026
- **degree-threshold.4** Raising the degree threshold does shrink the featureless fraction, but at a structural cost: higher thresholds discard nodes and edges, removing the very co-citation bridges and shrinking the recovered graph.
  conf: not stated · class: not stated · holds: biblion's citation graph (the fallworm example) · src: none (the reviewer's reasoning) · trail: C-GHOSTFUS §Q2, §Key Findings · from: C-GHOSTFUS:A-012, C-GHOSTFUS:B-0033
- **degree-threshold.5** The literature does not quantify the recovered-structure-against-reliability trade-off for citation graphs; it must be measured on biblion.
  conf: not stated · class: search (note: "The literature does not quantify") · search: not stated · holds: citation graphs · src: none (the review's search) · trail: C-GHOSTFUS §Q2 · from: C-GHOSTFUS:B-0034
- **degree-threshold.6** There is no published phase-transition theorem giving a clean threshold as a function of missing fraction for dense features under structural missingness.
  conf: not stated · class: search (note: "there is no published phase-transition theorem") · search: not stated · holds: dense features under structural missingness · src: none (the review's search) · trail: C-GHOSTFUS §Q2 · from: C-GHOSTFUS:B-0035
- **degree-threshold.7** Raising the threshold also changes the degree distribution and homophily of the surviving graph, which independently affects diffusion quality.
  conf: not stated · class: not stated · holds: the graph surviving a higher degree threshold · src: none (the reviewer's reasoning) · trail: C-GHOSTFUS §Q2 · from: C-GHOSTFUS:B-0042
- **degree-threshold.8** A node in a dense real-feature neighborhood is in a different regime than one surrounded by ghosts, even at the same global threshold.
  conf: not stated · class: not stated · holds: local against global missingness · src: none (the reviewer's reasoning) · trail: C-GHOSTFUS §Q2 · from: C-GHOSTFUS:B-0041
- **degree-threshold.9** If a modest threshold increase (say to >=3) cuts the featureless fraction well below 50% while retaining most bridges, that likely buys more than any operator tweak.
  conf: not stated · class: not stated · holds: conditional on the threshold sweep the review recommends · src: none (the reviewer's judgement) · trail: C-GHOSTFUS §Recommendations · from: C-GHOSTFUS:B-0112

### conduit-operator: conduit-only (masked) ghost nodes
needs: zero-anchor, feature-propagation, co-citation-bridge

- **conduit-operator.1** Conduit-only participation is a sound operator design, but there is no direct evidence testing the specific zero-anchor-corruption mechanism in an APPNP fusion pipeline; the review calls this the most actionable open design question.
  conf: not stated · class: not stated · holds: APPNP fusion pipelines · src: none (the review's verdict on the question) · trail: C-GHOSTFUS §Q3 · rating: "PARTIALLY DEMONSTRATED as a sound operator design" · contrary: not stated · from: C-GHOSTFUS:B-0045..0046
- **conduit-operator.2** Conduit-only (masked) participation is a recognized and defensible operator design: virtual-node and masked-aggregation literature supports keeping a node in the propagation topology while excluding its (absent) features from the aggregation term. No paper tests exactly biblion's zero-anchor-corruption mechanism, so this is a design recommendation, not a proven result.
  conf: not stated · class: not stated · holds: virtual-node and masked-aggregation literature; not tested for biblion's mechanism · src: gilmerNeuralMessagePassing2017, caiUnderstandingVirtualNodes2024 · trail: C-GHOSTFUS §Key Findings, §Q3 · contrary: not stated · from: C-GHOSTFUS:A-013..014, C-GHOSTFUS:B-0052..0053
- **conduit-operator.3** Virtual-node message passing (Gilmer et al.; Cai et al., "Understanding Virtual Nodes") routinely uses nodes that participate in topology and routing without contributing native features, serving as bridges for long-range information: the structural precedent for a ghost that transmits A -> B influence without an anchor.
  conf: not stated · class: not stated · holds: virtual / pass-through nodes in message passing · src: gilmerNeuralMessagePassing2017, caiUnderstandingVirtualNodes2024 · trail: C-GHOSTFUS §Q3 · from: C-GHOSTFUS:B-0053..0054
- **conduit-operator.4** Feature-propagation variants and masked GNNs keep a binary mask B distinguishing observed from unobserved entries, and only the observed entries enter the feature-aggregation/teleport term.
  conf: not stated · class: not stated · holds: masked aggregation · src: none (the note names feature-propagation variants and masked GNNs without a reference) · trail: C-GHOSTFUS §Q3 · from: C-GHOSTFUS:B-0055
- **conduit-operator.5** A "no-self-anchor" or masked-APPNP variant would exclude the teleport contribution of a ghost (mask it out of the alpha*X term) while still letting it carry the (1-alpha)D^-1 A propagation term; this is mechanically straightforward in the APPNP recurrence and avoids the origin-pull.
  conf: not stated · class: not stated · holds: the APPNP recurrence · src: none (the reviewer's design) · trail: C-GHOSTFUS §Q3 · from: C-GHOSTFUS:B-0056..0057
- **conduit-operator.6** Feature Propagation's boundary-reset steady state is essentially a conduit treatment of unknown nodes, and it is why FP is robust where naive zero-imputation-then-GNN is not.
  conf: not stated · class: not stated · holds: FP against zero-imputation followed by a GNN · src: rossiUnreasonableEffectivenessFeature2022 · trail: C-GHOSTFUS §Q3 · from: C-GHOSTFUS:B-0058..0059
- **conduit-operator.7** Biblion's anchored APPNP, by contrast, gives every node (including ghosts) a fixed teleport anchor each step; if that anchor is fabricated, the ghost is not a clean conduit but a persistent injector. This is the strongest theoretical argument that a masked/no-self-anchor variant should better preserve the co-citation signal and distort real nodes less.
  conf: not stated · class: not stated · holds: biblion's anchored APPNP · src: none (the reviewer's reasoning) · trail: C-GHOSTFUS §Q3 · contrary: not stated · from: C-GHOSTFUS:B-0060..0061
- **conduit-operator.8** No located source runs the exact A/B test of "imputed-anchor ghost" vs "zero-anchor ghost" vs "masked conduit ghost" inside an APPNP fusion feeding UMAP/HDBSCAN; the mechanism is well supported, but the head-to-head outcome in biblion is open.
  conf: not stated · class: search (note: "no located source") · search: searched, not found (note: "no located source") · holds: APPNP fusion feeding UMAP/HDBSCAN · src: none (the review's search) · trail: C-GHOSTFUS §Q3 · from: C-GHOSTFUS:B-0062..0063
- **conduit-operator.9** Low-variance collapse and zero-imputation magnitude bias both directly threaten the co-citation bridge and motivate a conduit-only operator.
  conf: not stated · class: not stated · holds: biblion's co-citation bridge · src: umPropagateInjectRevisiting2025, yiWhyNotUse2020 · trail: C-GHOSTFUS §TL;DR · from: C-GHOSTFUS:A-003, C-GHOSTFUS:A-005
- **conduit-operator.10** biblion should not assume imputed ghost anchors are reliable.
  conf: not stated · class: not stated · holds: biblion's imputed ghost anchors · src: none (the review's conclusion) · trail: C-GHOSTFUS §TL;DR · contrary: not stated · from: C-GHOSTFUS:A-006
- **conduit-operator.11** The fabricated-anchor problem is specific to anchored fusion: a non-anchored diffusion (pure FP with boundary reset) sidesteps it, which is part of why the masked-operator recommendation is strong; but moving fully to FP would change biblion's architecture more than the targeted masked-APPNP variant.
  conf: not stated · class: not stated · holds: anchored against non-anchored diffusion · src: none (the reviewer's reasoning) · trail: C-GHOSTFUS §Caveats · from: C-GHOSTFUS:B-0127..0128
- **conduit-operator.12** The masked / no-self-anchor APPNP variant is the highest-leverage, lowest-cost change and the design the FP literature most supports.
  conf: not stated · class: not stated · holds: biblion's pipeline · src: none (the reviewer's judgement) · trail: C-GHOSTFUS §Recommendations · from: C-GHOSTFUS:B-0108..0109
- **conduit-operator.13** Whether ghosts are included in the degree D of their neighbours changes the averaging weights even in the masked case.
  conf: not stated · class: not stated · holds: masked APPNP with degree normalization · src: none (the reviewer's reasoning) · trail: C-GHOSTFUS §Q3 · from: C-GHOSTFUS:B-0068
- **conduit-operator.14** Bringing A and B closer through a masked ghost (the bridge) and reducing origin-pull are two goals that can trade off.
  conf: not stated · class: not stated · holds: the masked variant · src: none (the reviewer's reasoning) · trail: C-GHOSTFUS §Q3 · from: C-GHOSTFUS:B-0069..0070
- **conduit-operator.15** A masked ghost with no anchor and few edges may become a free-floating low-degree node that UMAP scatters.
  conf: not stated · class: not stated · holds: masked ghosts with few edges, under UMAP · src: none (the reviewer's reasoning) · trail: C-GHOSTFUS §Q3 · from: C-GHOSTFUS:B-0071
- **conduit-operator.16** Zero rows in the propagation can interact with row-normalization (division by degree), for isolated or near-isolated ghosts.
  conf: not stated · class: not stated · holds: row-normalized propagation · src: none (the reviewer's reasoning) · trail: C-GHOSTFUS §Q3 · from: C-GHOSTFUS:B-0072

### denoise-order: the PCA denoise stage and ghost injection
needs: zero-anchor, missingness-regime

- **denoise-order.1** The interaction of the PCA denoise stage with ghost injection (PCA denoise of real anchors x ghost injection, and denoise-then-propagate vs propagate-then-denoise) is unstudied at biblion's missingness and feature density: the component results exist (PCA-a-priori experiments on full features; zero-imputation magnitude bias; SVD-spectrum bias under zero-imputation) but no single source tests their interaction.
  conf: not stated · class: search (note: "no single source tests their interaction") · search: not stated · holds: high, dense missingness (~70% missing, dense features) · src: none (the review's verdict on the question) · trail: C-GHOSTFUS §Q4, §Key Findings, §Caveats · rating: "NO DIRECT EVIDENCE; genuinely open" · from: C-GHOSTFUS:A-015, C-GHOSTFUS:B-0073..0075, C-GHOSTFUS:B-0088, C-GHOSTFUS:B-0123..0124
- **denoise-order.2** Morehead et al. (arXiv:2203.12522) apply PCA-100 and an autoencoder a priori (before the GNN) and find it preserves accuracy and reduces prediction variance across seeds (Cora GCN: 80.82% original, std 0.62, vs 80.98% PCA-100, std 0.80, means over five seeds).
  conf: not stated · class: not stated · holds: full features with no missingness, sparse bag-of-words (Cora); reduce-then-propagate on complete data; not shown for ghosts · src: moreheadSemiSupervisedGraphLearning2022 · trail: C-GHOSTFUS §Q4 · from: C-GHOSTFUS:B-0076..0078, C-GHOSTFUS:B-0091
- **denoise-order.3** In Morehead et al., one model (GraphConv) degraded badly with the autoencoder bottleneck.
  conf: not stated · class: not stated · holds: full features, no missingness · src: moreheadSemiSupervisedGraphLearning2022 · trail: C-GHOSTFUS §Q4 · from: C-GHOSTFUS:B-0076..0077
- **denoise-order.4** In classical PCA-with-missing-data, treating missing entries as zero biases the covariance/singular-value spectrum downward, and regularized iterative PCA (missMDA) deliberately shrinks singular values further as missingness grows.
  conf: not stated · class: not stated · holds: non-graph PCA with missing data · src: anonb (cited by URL), josseMissMDAPackageHandling2016, anonc (cited by URL) · trail: C-GHOSTFUS §Q4 · from: C-GHOSTFUS:B-0082..0083, C-GHOSTFUS:B-0093
- **denoise-order.5** "Impute-then-SVD" and "SVD-on-observed-only" (O-ALS vs I-SVD) are distinct procedures that introduce different biases: the non-graph analogue of biblion's ordering question.
  conf: not stated · class: not stated · holds: non-graph PCA with missing data · src: anond (cited by URL) · trail: C-GHOSTFUS §Q4 · from: C-GHOSTFUS:B-0083..0084, C-GHOSTFUS:B-0093
- **denoise-order.6** Any preprocessing that rescales magnitude (PCA centering, whitening, normalization) interacts with the zero-imputation magnitude bias.
  conf: not stated · class: not stated · holds: preprocessing before propagation · src: yiWhyNotUse2020 · trail: C-GHOSTFUS §Q4 · from: C-GHOSTFUS:B-0079..0080
- **denoise-order.7** In biblion the PCA denoise runs on the real anchors only (a ghost has no features to denoise), so denoising happens before ghosts get any anchor; PCA is fit on real nodes only, so the basis is defined by real-feature covariance.
  conf: not stated · class: not stated · holds: the biblion pipeline · src: none (the note's description of biblion) · trail: C-GHOSTFUS §Q4 · from: C-GHOSTFUS:B-0085, C-GHOSTFUS:B-0101
- **denoise-order.8** Denoising tends to dampen the raw magnitude of low-variance directions.
  conf: not stated · class: not stated · holds: PCA denoising · src: none (the reviewer's reasoning) · trail: C-GHOSTFUS §Q4 · from: C-GHOSTFUS:B-0086
- **denoise-order.9** If a ghost is zero-anchored after denoising, the origin-pull it exerts is on already-centered, reduced-variance real vectors; the relative distortion could be larger (each retained dimension carries more relative weight) or smaller (absolute magnitudes are smaller), and the literature does not resolve which dominates at ~70% missing on dense features.
  conf: not stated · class: not stated · holds: ~70% missing, dense features · src: none (the reviewer's reasoning) · trail: C-GHOSTFUS §Q4 · from: C-GHOSTFUS:B-0087..0088
- **denoise-order.10** The denoise-then-propagate order biblion uses is plausibly more robust than propagate-then-denoise, because FP-style diffusion is itself a low-pass denoiser, so denoising first avoids double-smoothing the imputed values.
  conf: not stated · class: reading (note: "this is an inference, not a result") · holds: biblion's denoise-then-propagate order · src: none (the reviewer's inference) · trail: C-GHOSTFUS §Q4 · from: C-GHOSTFUS:B-0089
- **denoise-order.11** Every supporting source for the denoise question is outside biblion's exact regime: Morehead et al. used full features, sparse bag-of-words and no missingness; Yi et al. are non-graph and MCAR; the PCA-missing-data work is non-graph; Ferrini et al. use mask-concatenation, not PCA ordering. The interaction is an open question that biblion is well-positioned to be the first to characterize.
  conf: not stated · class: not stated · holds: the sources the review located for the denoise question · src: moreheadSemiSupervisedGraphLearning2022, yiWhyNotUse2020, ferriniRethinkingGNNsMissing2026 · trail: C-GHOSTFUS §Q4 · from: C-GHOSTFUS:B-0090..0095
- **denoise-order.12** A zero-anchored ghost may inject energy into low-variance directions that PCA would otherwise discard.
  conf: not stated · class: not stated · holds: PCA at 100-d · src: none (the reviewer's reasoning) · trail: C-GHOSTFUS §Q4 · from: C-GHOSTFUS:B-0100
- **denoise-order.13** Whitening equalizes variance across dimensions and would change the origin-pull geometry more than centering alone.
  conf: not stated · class: not stated · holds: whitening against centering-only · src: none (the reviewer's reasoning) · trail: C-GHOSTFUS §Q4 · from: C-GHOSTFUS:B-0102
- **denoise-order.14** The order effect (denoise-then-propagate against propagate-then-denoise) is only interpretable when the ghost-injection space is also varied.
  conf: not stated · class: not stated · holds: raw 768-d against 100-d ghost injection · src: none (the reviewer's reasoning) · trail: C-GHOSTFUS §Q4 · from: C-GHOSTFUS:B-0097..0098

## Do not say

- **dns.1** "Feature propagation is robust at biblion's missingness: Rossi et al. lost only 4.12% relative accuracy at 99% missing features."
  why: The note says the 4.12% figure is an MCAR, per-channel, sparse-feature, homophilous, node-classification-accuracy result, while biblion has structural (whole-node) missingness, dense SPECTER2 features, ~70% featureless nodes and unsupervised clustering, so the transfer is not warranted. · instead: missingness-regime.3, feature-propagation.1 · trail: C-GHOSTFUS §Caveats · from: C-GHOSTFUS:B-0118..0119
- **dns.2** "Because APPNP encodes the co-citation bridge by construction, the bridge survives into biblion's UMAP embedding and HDBSCAN clusters."
  why: The note says "encoded by construction" is not "validated downstream": low-variance collapse, oversmoothing and UMAP/HDBSCAN can all erode the bridge, and only stage-wise measurement on biblion can settle whether it survives. · instead: co-citation-bridge.6, co-citation-bridge.8 · trail: C-GHOSTFUS §Caveats · from: C-GHOSTFUS:B-0120..0122
- **dns.3** "Below about 60% missing features, biblion is in the proven zone for feature propagation."
  why: The note says the ~50-60% figure is an empirical, sparse-feature, MCAR, node-classification-accuracy observation, to be treated as an upper-optimistic bound, not a target. · instead: degree-threshold.2 · trail: C-GHOSTFUS §Q2 · from: C-GHOSTFUS:B-0036..0037
- **dns.4** "A masked, conduit-only ghost operator has been shown to prevent zero-anchor corruption."
  why: The note says no paper tests exactly biblion's zero-anchor-corruption mechanism, so conduit-only participation is a design recommendation, not a proven result. · instead: conduit-operator.2, conduit-operator.8 · trail: C-GHOSTFUS §Key Findings · from: C-GHOSTFUS:A-013..014
- **dns.5** "Denoising before propagation has been shown to be more robust than propagating before denoising."
  why: The note says this order is plausibly more robust but that this is an inference, not a result, and that its recommendation on the denoise stage rests on composed inference, not a demonstrated result. · instead: denoise-order.10, denoise-order.1 · trail: C-GHOSTFUS §Q4 · from: C-GHOSTFUS:B-0089, C-GHOSTFUS:B-0124

## Gaps

- **gap.1** The findings were never checked by a second reader: the note has no critique. Its answers rest on Rossi et al.'s 4.12% relative accuracy drop at 99% missing features and the gap opening from around 60% missing, Um et al.'s low-variance-channel result, Yi et al.'s variable sparsity problem, and biblion's ~70% featureless fraction at degree >= 2.
  blocks: missingness-regime, washout, zero-anchor, degree-threshold · origin: no critique in the input, so no second reader checked it · search: not stated · from: C-GHOSTFUS:A-001, C-GHOSTFUS:A-003, C-GHOSTFUS:A-008, C-GHOSTFUS:A-011
- **gap.2** Whether the co-citation bridge through a ghost is "measurably closer and correctly co-clustered" in biblion is an empirical open question.
  blocks: co-citation-bridge · origin: the note's open question on the co-citation bridge · search: not stated · from: C-GHOSTFUS:B-0015, C-GHOSTFUS:B-0122
- **gap.3** The degree threshold at which biblion re-enters the proven zone is not established, and the trade-off between recovered structure and reliability is unquantified for citation graphs.
  blocks: degree-threshold · origin: the note's open question on the degree threshold · search: not stated · from: C-GHOSTFUS:B-0023, C-GHOSTFUS:B-0034
- **gap.4** No located source runs the head-to-head test of imputed-anchor, zero-anchor and masked-conduit ghosts inside an APPNP fusion feeding UMAP/HDBSCAN.
  blocks: conduit-operator · origin: the note's not-found result · search: searched, not found (note: "no located source") · from: C-GHOSTFUS:B-0062
- **gap.5** No source tests the PCA-denoise x ghost-injection interaction at this missingness and feature density.
  blocks: denoise-order · origin: the note's open question on the denoise stage · search: not stated · from: C-GHOSTFUS:B-0124
- **gap.6** The note contradicts itself on Morehead et al.: it says PCA-100 "reduces prediction variance across seeds", but the figures it gives (std 0.62 original against std 0.80 with PCA-100) show a larger standard deviation.
  blocks: denoise-order · origin: the note's statement and its own figures disagree · search: not stated · src: moreheadSemiSupervisedGraphLearning2022 · from: C-GHOSTFUS:B-0076
- **gap.7** Several sources the text relies on have no reference entry: five are cited by URL only (arXiv 2312.16183, 2601.07419 and 1508.05431, the missMDA imputePCA documentation, and ScienceDirect S0169743924000935), deep bibliographic coupling work is named without a reference, and FSD-CAP 2026 is named only among the recent preprints.
  blocks: appnp-propagation, washout, co-citation-bridge, denoise-order · origin: references missing in the note · search: not stated · src: anon, anona, anonb, anonc, anond · from: C-GHOSTFUS:B-0003..0004, C-GHOSTFUS:B-0011, C-GHOSTFUS:B-0082..0084, C-GHOSTFUS:B-0126

## Out of scope

- C-GHOSTFUS:A-004: a link to another vault note (navigation, not a finding)
- C-GHOSTFUS:A-007: the review's recommended path for biblion (routing, not a finding)

## Sources

```bibtex
@inproceedings{gasteigerPredictThenPropagate2019,
  title = {Predict then Propagate: Graph Neural Networks meet Personalized PageRank},
  author = {Gasteiger, Johannes and Bojchevski, Aleksandar and G{\"u}nnemann, Stephan},
  booktitle = {International Conference on Learning Representations (ICLR)},
  year = {2019},
  eprint = {1810.05997},
  note = {access: not stated; not cited: listed, and APPNP is named in the text, but no finding cites this work; cited as: C-GHOSTFUS gasteiger2019appnp (the note's key); the note: "author formerly Johannes Klicpera"}
}
@inproceedings{rossiUnreasonableEffectivenessFeature2022,
  title = {On the Unreasonable Effectiveness of Feature Propagation in Learning on Graphs with Missing Node Features},
  author = {Rossi, Emanuele and Kenlay, Henry and Gorinova, Maria I. and Chamberlain, Benjamin Paul and Dong, Xiaowen and Bronstein, Michael M.},
  booktitle = {Proceedings of the First Learning on Graphs Conference (LoG)},
  series = {Proceedings of Machine Learning Research},
  volume = {198},
  pages = {11:1--11:16},
  year = {2022},
  eprint = {2111.12128},
  url = {https://proceedings.mlr.press/v198/rossi22a/rossi22a.pdf},
  note = {access: not stated; cited as: C-GHOSTFUS rossi2022featureprop (the note's key), and by URL (mlr)}
}
@inproceedings{umConfidenceBasedFeatureImputation2023,
  title = {Confidence-Based Feature Imputation for Graphs with Partially Known Features},
  author = {Um, Daeho and Park, Jiwoong and Park, Seulki and Choi, Jin Young},
  booktitle = {International Conference on Learning Representations (ICLR)},
  year = {2023},
  eprint = {2305.16618},
  note = {access: not stated; cited as: C-GHOSTFUS um2023pcfi (the note's key); named in the text as PCFI}
}
@inproceedings{umPropagateInjectRevisiting2025,
  title = {Propagate and Inject: Revisiting Propagation-Based Feature Imputation for Graphs with Partially Observed Features},
  author = {Um, Daeho and Kim, Sunoh and Park, Jiwoong and Lim, Jongin and Ahn, Seong Jin and Park, Seulki},
  booktitle = {Proceedings of the 42nd International Conference on Machine Learning (ICML)},
  year = {2025},
  note = {access: not stated; cited as: C-GHOSTFUS um2025propagateinject (the note's key); the note calls it a very recent preprint with limited independent replication}
}
@inproceedings{yiWhyNotUse2020,
  title = {Why Not to Use Zero Imputation? Correcting Sparsity Bias in Training Neural Networks},
  author = {Yi, Joonyoung and Lee, Juhyuk and Kim, Kwang Joon and Hwang, Sung Ju and Yang, Eunho},
  booktitle = {International Conference on Learning Representations (ICLR)},
  year = {2020},
  eprint = {1906.00150},
  url = {https://arxiv.org/pdf/1906.00150},
  note = {access: not stated; cited as: C-GHOSTFUS yi2020zeroimputation (the note's key), and by URL (arxiv)}
}
@article{ferriniRethinkingGNNsMissing2026,
  title = {Rethinking GNNs and Missing Features: Challenges, Evaluation and a Robust Solution},
  author = {Ferrini, Francesco and Lachi, Veronica and Longa, Antonio and Lepri, Bruno and Matono, Akiyoshi and Passerini, Andrea and Liu, Xin and Jaeger, Manfred},
  journal = {arXiv preprint arXiv:2601.04855},
  year = {2026},
  url = {https://arxiv.org/pdf/2601.04855},
  note = {access: not stated; type: preprint; cited as: C-GHOSTFUS ferrini2026rethinking (the note's key), and by URL (arxiv); the note calls it a very recent preprint with limited independent replication}
}
@inproceedings{tangLINELargescaleInformation2015,
  title = {LINE: Large-scale Information Network Embedding},
  author = {Tang, Jian and Qu, Meng and Wang, Mingzhe and Zhang, Ming and Yan, Jun and Mei, Qiaozhu},
  booktitle = {Proceedings of the 24th International Conference on World Wide Web (WWW)},
  pages = {1067--1077},
  year = {2015},
  eprint = {1503.03578},
  note = {access: not stated; cited as: C-GHOSTFUS tang2015line (the note's key)}
}
@inproceedings{cohanSPECTERDocumentlevelRepresentation2020,
  title = {SPECTER: Document-level Representation Learning using Citation-informed Transformers},
  author = {Cohan, Arman and Feldman, Sergey and Beltagy, Iz and Downey, Doug and Weld, Daniel S.},
  booktitle = {Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics (ACL)},
  year = {2020},
  eprint = {2004.07180},
  note = {access: not stated; not cited: listed, never cited in the text; cited as: C-GHOSTFUS cohan2020specter (the note's key)}
}
@misc{singhSPECTER2AdaptingScientific2023,
  title = {SPECTER2: Adapting Scientific Document Embeddings to Multiple Fields and Task Formats},
  author = {Singh, Amanpreet and D'Arcy, Mike and Cohan, Arman and Downey, Doug and Feldman, Sergey},
  howpublished = {Allen Institute for AI; SciRepEval benchmark},
  year = {2023},
  note = {access: not stated; not cited: SPECTER2 is named in the text as biblion's features, never cited for a finding; cited as: C-GHOSTFUS specter2_2023 (the note's key)}
}
@article{moreheadSemiSupervisedGraphLearning2022,
  title = {Semi-Supervised Graph Learning Meets Dimensionality Reduction},
  author = {Morehead, Alex and Chantapakul, Watchanan and Cheng, Jianlin},
  journal = {arXiv preprint arXiv:2203.12522},
  year = {2022},
  note = {access: not stated; type: preprint; cited as: C-GHOSTFUS morehead2022dimreduction (the note's key)}
}
@article{yunOldieButGoodie2024,
  title = {Oldie but Goodie: Re-illuminating Label Propagation on Graphs with Partially Observed Features},
  author = {Yun, Sukwon and others},
  journal = {arXiv preprint arXiv:2508.01209},
  year = {2024},
  note = {access: not stated; type: preprint; cited as: C-GHOSTFUS yun2024goodie (the note's key); incomplete: author}
}
@article{caiNoteOverSmoothingGraph2020,
  title = {A Note on Over-Smoothing for Graph Neural Networks},
  author = {Cai, Chen and Wang, Yusu},
  journal = {arXiv preprint arXiv:2006.13318},
  year = {2020},
  note = {access: not stated; type: preprint; cited as: C-GHOSTFUS cai2020oversmoothing (the note's key)}
}
@article{oonoGraphNeuralNetworks2020,
  title = {Graph Neural Networks Exponentially Lose Expressive Power for Node Classification},
  author = {Oono, Kenta and Suzuki, Taiji},
  journal = {International Conference on Learning Representations (ICLR)},
  year = {2020},
  note = {access: not stated; cited as: C-GHOSTFUS oono2020graph (the note's key)}
}
@misc{caiUnderstandingVirtualNodes2024,
  title = {Understanding Virtual Nodes: Oversquashing and Node Heterogeneity},
  author = {Cai, Chen and others},
  howpublished = {arXiv preprint arXiv:2405.13526},
  year = {2024},
  note = {access: not stated; type: preprint; cited as: C-GHOSTFUS cai2024virtualnodes (the note's key); incomplete: author}
}
@inproceedings{gilmerNeuralMessagePassing2017,
  title = {Neural Message Passing for Quantum Chemistry},
  author = {Gilmer, Justin and Schoenholz, Samuel S. and Riley, Patrick F. and Vinyals, Oriol and Dahl, George E.},
  booktitle = {Proceedings of the 34th International Conference on Machine Learning (ICML)},
  year = {2017},
  note = {access: not stated; cited as: C-GHOSTFUS gilmer2017mpnn (the note's key)}
}
@article{josseMissMDAPackageHandling2016,
  title = {missMDA: A Package for Handling Missing Values in Multivariate Data Analysis},
  author = {Josse, Julie and Husson, Fran{\c{c}}ois},
  journal = {Journal of Statistical Software},
  volume = {70},
  number = {1},
  pages = {1--31},
  year = {2016},
  note = {access: not stated; cited as: C-GHOSTFUS josse2016missmda (the note's key); the text names missMDA}
}
@misc{anon,
  url = {https://arxiv.org/pdf/2312.16183},
  note = {access: not stated; cited in the text by URL only (arxiv), for APPNP's closed form as a personalized-PageRank random walk with restart; incomplete: author, title, year}
}
@misc{anona,
  url = {https://arxiv.org/pdf/2601.07419},
  note = {access: not stated; cited in the text by URL only (arxiv), for oversmoothing and Dirichlet energy decay; incomplete: author, title, year}
}
@misc{anonb,
  url = {https://arxiv.org/pdf/1508.05431},
  note = {access: not stated; cited in the text by URL only (arxiv), for zero-filled missing entries biasing the singular-value spectrum; incomplete: author, title, year}
}
@misc{anonc,
  url = {https://www.rdocumentation.org/packages/missMDA/versions/1.18/topics/imputePCA},
  note = {access: not stated; cited in the text by URL only (RDocumentation), the missMDA imputePCA documentation, version 1.18; incomplete: author, title, year}
}
@misc{anond,
  url = {https://www.sciencedirect.com/science/article/pii/S0169743924000935},
  note = {access: not stated; cited in the text by URL only (ScienceDirect), for O-ALS against I-SVD; incomplete: author, title, journal, year}
}
@article{seamanWhatMeantMissing2013,
  author = {Seaman, Shaun and Galati, John and Jackson, Dan and Carlin, John},
  title = {What Is Meant by "Missing at Random"?},
  journal = {Statistical Science},
  year = {2013},
  volume = {28},
  number = {2},
  pages = {257--268},
  doi = {10.1214/13-STS415},
  note = {background; access: full_text (arXiv:1306.2812)}
}
@misc{mcinnesUMAPUniformManifold2018,
  author = {McInnes, Leland and Healy, John and Melville, James},
  title = {UMAP: Uniform Manifold Approximation and Projection for Dimension Reduction},
  howpublished = {arXiv preprint arXiv:1802.03426},
  year = {2018},
  eprint = {1802.03426},
  note = {background; access: abstract_only (arXiv abstract page)}
}
```
