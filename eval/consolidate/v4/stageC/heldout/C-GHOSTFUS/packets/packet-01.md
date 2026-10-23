## ghost-nodes.1 (claim)

biblion has structural (whole-node) missingness, dense features, and about 70% featureless nodes at degree >= 2.

- conf: not stated
- class: not stated
- holds: biblion's citation graph at a degree threshold of >= 2
- src: none (the note's description of biblion)
- trail: C-GHOSTFUS §Key Findings

From the note:

> C-GHOSTFUS:A-008 [Key Findings] **The "proven zone" for feature propagation does not include biblion's regime.** Rossi et al. report only a 4.12% relative accuracy drop at 99% missing features, but explicitly under MCAR per-channel masking on homophilous benchmarks, and they note the method degrades toward the zero baseline as homophily falls. biblion has structural (whole-node) missingness, dense features, and ~70% featureless nodes at degree >= 2.
>

## ghost-nodes.2 (claim)

In the fallworm example there are 3,392 ghosts against 1,405 real nodes at degree >= 2.

- conf: not stated
- class: not stated
- holds: the fallworm graph at degree >= 2
- src: none (the note's description of biblion)
- trail: C-GHOSTFUS §Q2

From the note:

> C-GHOSTFUS:B-0033 [Q2 — At what degree threshold does this regime re-enter the "proven" zone?] Raising the degree threshold does shrink the featureless fraction (the fallworm example: 3,392 ghosts vs 1,405 real at degree >= 2), but the cost is structural: higher thresholds discard nodes and edges, removing the very co-citation bridges Q1 cares about and shrinking the recovered graph.
>

## ghost-nodes.3 (claim)

biblion's features are SPECTER2 embeddings (768-d, dense, semantic), and its downstream is unsupervised clustering with UMAP and HDBSCAN.

- conf: not stated
- class: not stated
- holds: the biblion pipeline
- src: none (the note's description of biblion)
- trail: C-GHOSTFUS §Q2, §Caveats, §Q1

From the note:

> C-GHOSTFUS:B-0014 [Q1 — Does diffusion imputation preserve the co-citation bridge?] None of it covers the case where the intermediary's own vector is fabricated, nor the ~70%-ghost dense-feature regime, nor the specific UMAP+HDBSCAN downstream.
>
> C-GHOSTFUS:B-0030 [Q2 — At what degree threshold does this regime re-enter the "proven" zone?] SPECTER2 (768-d, dense, semantic) is exactly the dense regime where the comfortable crossover may move sharply leftward.
>
> C-GHOSTFUS:B-0118 [Caveats] - The headline robustness number (4.12% relative drop at 99% missing) is an MCAR, per-channel, sparse-feature, homophilous, node-classification-accuracy result. biblion is structural (whole-node) missingness, dense SPECTER2 features, ~70% featureless, unsupervised clustering.
>

## appnp-propagation.1 (claim)

APPNP's closed form, h = alpha(I - (1-alpha)D^-1 A)^-1 X, is a personalized-PageRank random walk with restart, so a path through a shared intermediary does contribute to the stationary similarity between A and B.

- conf: not stated
- class: not stated
- holds: the APPNP propagation operator
- src: anon (cited by URL)
- trail: C-GHOSTFUS §Q1

From the note:

> C-GHOSTFUS:B-0003 [Q1 — Does diffusion imputation preserve the co-citation bridge?] APPNP's closed form, h = alpha(I - (1-alpha)D^-1 A)^-1 X, is a personalized-PageRank random walk with restart, [arxiv](https://arxiv.org/pdf/2312.16183) so a path through a shared intermediary does contribute to the stationary similarity between A and B. This is the graph-diffusion analogue of second-order proximity: LINE (Tang et al., 2015) formalizes that nodes with shared neighbors are likely to be similar, and bibliographic-coupling/co-citation theory treats two documents sharing a cited third work as similar by construction.
>

## appnp-propagation.2 (claim)

APPNP's teleport term (alpha = 0.3 in biblion) is specifically designed to resist oversmoothing by re-anchoring each node to X each step, which is good for real nodes but is exactly what a ghost node lacks.

- conf: not stated
- class: not stated
- holds: biblion's APPNP with alpha = 0.3
- src: none (the reviewer's reasoning)
- trail: C-GHOSTFUS §Q1

From the note:

> C-GHOSTFUS:B-0010 [Q1 — Does diffusion imputation preserve the co-citation bridge?] - **Oversmoothing / variance collapse.** Repeated aggregation is Laplacian smoothing; node features converge toward a degree-scaled constant vector and Dirichlet energy decays to zero (Cai & Wang; Oono & Suzuki).
>
> C-GHOSTFUS:B-0011 [Q1 — Does diffusion imputation preserve the co-citation bridge?] [arxiv](https://arxiv.org/pdf/2601.07419) APPNP's teleport term (alpha = 0.3 here) is specifically designed to resist this by re-anchoring each node to X each step, which is good for real nodes but is exactly what a ghost node lacks.
>

## feature-propagation.1 (claim)

Rossi et al. (LoG 2022) report only a 4.12% relative accuracy drop at 99% missing features, explicitly under MCAR per-channel masking on homophilous benchmarks.

- conf: not stated
- class: not stated
- holds: MCAR per-channel masking; homophilous, sparse-feature benchmarks; node-classification accuracy
- src: rossiUnreasonableEffectivenessFeature2022
- trail: C-GHOSTFUS §Key Findings, §Caveats

From the note:

> C-GHOSTFUS:A-001 [TL;DR] - All four questions are at best PARTIALLY demonstrated and at worst genuinely open: the published feature-propagation robustness results (Rossi et al., LoG 2022) cover homophilous, MCAR, mostly-sparse-feature, small-to-moderate-missing-fraction regimes, none of which match biblion's ~70%-featureless, dense-SPECTER2-feature, structural-missingness regime.
>
> C-GHOSTFUS:A-008 [Key Findings] **The "proven zone" for feature propagation does not include biblion's regime.** Rossi et al. report only a 4.12% relative accuracy drop at 99% missing features, but explicitly under MCAR per-channel masking on homophilous benchmarks, and they note the method degrades toward the zero baseline as homophily falls. biblion has structural (whole-node) missingness, dense features, and ~70% featureless nodes at degree >= 2.
>
> C-GHOSTFUS:B-0118 [Caveats] - The headline robustness number (4.12% relative drop at 99% missing) is an MCAR, per-channel, sparse-feature, homophilous, node-classification-accuracy result. biblion is structural (whole-node) missingness, dense SPECTER2 features, ~70% featureless, unsupervised clustering.
>

## feature-propagation.2 (claim)

Rossi et al. note that feature propagation degrades toward the zero baseline as homophily falls.

- conf: not stated
- class: not stated
- holds: their benchmarks, as homophily decreases
- src: rossiUnreasonableEffectivenessFeature2022
- trail: C-GHOSTFUS §Key Findings

From the note:

> C-GHOSTFUS:A-008 [Key Findings] **The "proven zone" for feature propagation does not include biblion's regime.** Rossi et al. report only a 4.12% relative accuracy drop at 99% missing features, but explicitly under MCAR per-channel masking on homophilous benchmarks, and they note the method degrades toward the zero baseline as homophily falls. biblion has structural (whole-node) missingness, dense features, and ~70% featureless nodes at degree >= 2.
>

## feature-propagation.3 (claim)

Rossi et al. observe that "most methods perform extremely well up to 50% of missing features, suggesting that in general node features are redundant... The gap between methods opens up from around 60% of missing features, and is particularly large for extremely high rates of missing features (90% or 99%): FP is the only feature-aware method which is robust to these high rates on all datasets."

- conf: not stated
- class: not stated
- holds: their benchmarks (sparse features, MCAR masking, node-classification accuracy); FP is the only method shown robust past 90% missing on the tested benchmarks
- src: rossiUnreasonableEffectivenessFeature2022
- trail: C-GHOSTFUS §Q2, §Key Findings, §Recommendations

From the note:

> C-GHOSTFUS:A-011 [Key Findings] **A degree-threshold crossover exists in principle but is dataset-specific.** Rossi et al. observe methods perform well up to ~50% missing and that "the gap between methods opens up from around 60% of missing features.
>
> C-GHOSTFUS:B-0024 [Q2 — At what degree threshold does this regime re-enter the "proven" zone?] The clearest anchor is Rossi et al.'s observation that "most methods perform extremely well up to 50% of missing features, suggesting that in general node features are redundant...
>
> C-GHOSTFUS:B-0025 [Q2 — At what degree threshold does this regime re-enter the "proven" zone?] The gap between methods opens up from around 60% of missing features, and is particularly large for extremely high rates of missing features (90% or 99%): FP is the only feature-aware method which is robust to these high rates on all datasets.
>
> C-GHOSTFUS:B-0036 [Q2 — At what degree threshold does this regime re-enter the "proven" zone?] The ~50-60% figure is an empirical, sparse-feature, MCAR, node-classification-accuracy observation.
>
> C-GHOSTFUS:B-0116 [Recommendations] **Throughout, prefer feature-propagation-style boundary-reset imputation (FP, PCFI) over naive zero or mean imputation** if an anchor is needed at all, because FP's steady state is invariant to zero-init [mlr](https://proceedings.mlr.press/v198/rossi22a/rossi22a.pdf) and is the only method shown robust past 90% missing on the tested benchmarks.
>

## feature-propagation.4 (claim)

Feature Propagation's steady state is independent (invariant) of the zero initialization of unknown features, because the diffusion resets known features each step and lets unknowns be determined purely by the boundary.

- conf: not stated
- class: not stated
- holds: FP with boundary reset
- src: rossiUnreasonableEffectivenessFeature2022
- trail: C-GHOSTFUS §Q3, §Recommendations

From the note:

> C-GHOSTFUS:B-0058 [Q3 — Conduit-only featureless nodes vs imputed-position nodes] Crucially, Rossi et al.'s Feature Propagation already embodies a related insight: its steady state is independent of the zero initialization of unknown features, because the diffusion resets known features each step and lets unknowns be determined purely by the boundary.
>
> C-GHOSTFUS:B-0116 [Recommendations] **Throughout, prefer feature-propagation-style boundary-reset imputation (FP, PCFI) over naive zero or mean imputation** if an anchor is needed at all, because FP's steady state is invariant to zero-init [mlr](https://proceedings.mlr.press/v198/rossi22a/rossi22a.pdf) and is the only method shown robust past 90% missing on the tested benchmarks.
>

## feature-propagation.5 (claim)

PCFI's confidence weighting uses the channel-wise shortest-path distance to the nearest observed node; the review calls it a ready-made way to down-weight deep-ghost anchors.

- conf: not stated
- class: not stated
- holds: PCFI imputation
- src: umConfidenceBasedFeatureImputation2023
- trail: C-GHOSTFUS §Recommendations

From the note:

> C-GHOSTFUS:B-0117 [Recommendations] Consider PCFI's confidence weighting (channel-wise shortest-path distance to nearest observed node) as a ready-made way to down-weight deep-ghost anchors.
>

## missingness-regime.1 (claim)

The published feature-propagation robustness results (Rossi et al., LoG 2022) cover homophilous, MCAR, mostly-sparse-feature, small-to-moderate-missing-fraction regimes, none of which match biblion's ~70%-featureless, dense-SPECTER2-feature, structural-missingness regime: the "proven zone" for feature propagation does not include biblion's regime.

- conf: not stated
- class: not stated
- holds: published FP results against biblion's regime
- src: rossiUnreasonableEffectivenessFeature2022
- trail: C-GHOSTFUS §TL;DR, §Key Findings

From the note:

> C-GHOSTFUS:A-001 [TL;DR] - All four questions are at best PARTIALLY demonstrated and at worst genuinely open: the published feature-propagation robustness results (Rossi et al., LoG 2022) cover homophilous, MCAR, mostly-sparse-feature, small-to-moderate-missing-fraction regimes, none of which match biblion's ~70%-featureless, dense-SPECTER2-feature, structural-missingness regime.
>
> C-GHOSTFUS:A-008 [Key Findings] **The "proven zone" for feature propagation does not include biblion's regime.** Rossi et al. report only a 4.12% relative accuracy drop at 99% missing features, but explicitly under MCAR per-channel masking on homophilous benchmarks, and they note the method degrades toward the zero baseline as homophily falls. biblion has structural (whole-node) missingness, dense features, and ~70% featureless nodes at degree >= 2.
>

Not found in the cited text (where to look, not what is wrong): holds: fp

## missingness-regime.2 (claim)

All four of the review's questions are at best partially demonstrated and at worst genuinely open.

- conf: not stated
- class: not stated
- holds: the review's four questions
- src: none (the review's overall verdict)
- trail: C-GHOSTFUS §TL;DR
- rating: "at best PARTIALLY demonstrated and at worst genuinely open"
- contrary: not stated

From the note:

> C-GHOSTFUS:A-001 [TL;DR] - All four questions are at best PARTIALLY demonstrated and at worst genuinely open: the published feature-propagation robustness results (Rossi et al., LoG 2022) cover homophilous, MCAR, mostly-sparse-feature, small-to-moderate-missing-fraction regimes, none of which match biblion's ~70%-featureless, dense-SPECTER2-feature, structural-missingness regime.
>

Not found in the cited text (where to look, not what is wrong): holds: review

## missingness-regime.3 (claim)

The headline robustness number (4.12% relative drop at 99% missing) is an MCAR, per-channel, sparse-feature, homophilous, node-classification-accuracy result, while biblion is structural (whole-node) missingness, dense SPECTER2 features, ~70% featureless and unsupervised clustering; the transfer is not warranted, and published thresholds are optimistic bounds.

- conf: not stated
- class: not stated
- holds: Rossi et al.'s benchmarks against biblion
- src: rossiUnreasonableEffectivenessFeature2022
- trail: C-GHOSTFUS §Caveats
- contrary: not stated

From the note:

> C-GHOSTFUS:B-0118 [Caveats] - The headline robustness number (4.12% relative drop at 99% missing) is an MCAR, per-channel, sparse-feature, homophilous, node-classification-accuracy result. biblion is structural (whole-node) missingness, dense SPECTER2 features, ~70% featureless, unsupervised clustering.
>
> C-GHOSTFUS:B-0119 [Caveats] The transfer is not warranted; treat published thresholds as optimistic bounds.
>

Not found in the cited text (where to look, not what is wrong): holds: rossi

## missingness-regime.4 (claim)

Ferrini et al. (2026, "Rethinking GNNs and Missing Features") prove that "in highly sparse settings, the mutual information between features and labels is barely affected by additional missingness, except at extremely high missing rates... with performance degrading only when more than 90% of entries are removed," and argue robustness cannot be meaningfully assessed when most features are already absent.

- conf: not stated
- class: deriv (note: "prove")
- holds: highly sparse feature settings
- src: ferriniRethinkingGNNsMissing2026 (very recent preprint; limited independent replication)
- trail: C-GHOSTFUS §Q2, §Caveats

From the note:

> C-GHOSTFUS:B-0028 [Q2 — At what degree threshold does this regime re-enter the "proven" zone?] - **Sparse vs dense.** Ferrini et al. (2026, "Rethinking GNNs and Missing Features") prove that "in highly sparse settings, the mutual information between features and labels is barely affected by additional missingness, except at extremely high missing rates... with performance degrading only when more than 90% of entries are removed," and argue robustness cannot be meaningfully assessed when most features are already absent.
>
> C-GHOSTFUS:B-0126 [Caveats] - Several supporting sources are very recent preprints (Ferrini et al. 2026; Um et al. 2025; FSD-CAP 2026) and have had limited independent replication; weight them accordingly.
>

## missingness-regime.5 (claim)

Ferrini et al.'s experiments show that methods that look robust on sparse bag-of-words features fail on dense, low-dimensional features.

- conf: not stated
- class: not stated
- holds: sparse bag-of-words against dense, low-dimensional features
- src: ferriniRethinkingGNNsMissing2026 (very recent preprint; limited independent replication)
- trail: C-GHOSTFUS §Q2

From the note:

> C-GHOSTFUS:B-0028 [Q2 — At what degree threshold does this regime re-enter the "proven" zone?] - **Sparse vs dense.** Ferrini et al. (2026, "Rethinking GNNs and Missing Features") prove that "in highly sparse settings, the mutual information between features and labels is barely affected by additional missingness, except at extremely high missing rates... with performance degrading only when more than 90% of entries are removed," and argue robustness cannot be meaningfully assessed when most features are already absent.
>
> C-GHOSTFUS:B-0029 [Q2 — At what degree threshold does this regime re-enter the "proven" zone?] Their experiments show methods that look robust on sparse bag-of-words fail on dense, low-dimensional features.
>
> C-GHOSTFUS:B-0126 [Caveats] - Several supporting sources are very recent preprints (Ferrini et al. 2026; Um et al. 2025; FSD-CAP 2026) and have had limited independent replication; weight them accordingly.
>

## missingness-regime.6 (claim)

Ferrini et al. work in the dense-feature regime and under structural missingness, but with mask-concatenation, not PCA ordering.

- conf: not stated
- class: not stated
- holds: dense features, structural missingness
- src: ferriniRethinkingGNNsMissing2026 (cited by URL)
- trail: C-GHOSTFUS §Q4

From the note:

> C-GHOSTFUS:B-0094 [Q4 — Interaction of the denoise stage with featureless-node injection] Ferrini et al.: dense-feature regime and structural missingness but mask-concatenation, [arxiv](https://arxiv.org/pdf/2601.04855) not PCA ordering.
>

## missingness-regime.7 (claim)

SPECTER2 (768-d, dense, semantic) is exactly the dense regime where the comfortable missing-fraction crossover may move sharply leftward.

- conf: not stated
- class: not stated
- holds: SPECTER2 features
- src: none (the reviewer's reasoning)
- trail: C-GHOSTFUS §Q2

From the note:

> C-GHOSTFUS:B-0030 [Q2 — At what degree threshold does this regime re-enter the "proven" zone?] SPECTER2 (768-d, dense, semantic) is exactly the dense regime where the comfortable crossover may move sharply leftward.
>

## missingness-regime.8 (claim)

Yun et al. (2024, "Oldie but Goodie") report that FP's performance-drop rate became steeper in structurally missing scenarios, because whole-node missingness means a ghost has no observed channel anywhere on the node.

- conf: not stated
- class: not stated
- holds: structural (whole-node) against uniform missingness
- src: yunOldieButGoodie2024
- trail: C-GHOSTFUS §Q2

From the note:

> C-GHOSTFUS:B-0031 [Q2 — At what degree threshold does this regime re-enter the "proven" zone?] - **Structural vs uniform missingness.** Yun et al. (2024, "Oldie but Goodie") report that FP's performance-drop rate became steeper in structurally missing scenarios, because whole-node missingness means a ghost has no observed channel anywhere on the node.
>

## missingness-regime.9 (claim)

Structural missingness is biblion's exact case, which predicts that its crossover is worse than the 60% sparse-MCAR figure suggests.

- conf: not stated
- class: not stated
- holds: biblion's whole-node missingness
- src: yunOldieButGoodie2024
- trail: C-GHOSTFUS §Q2

From the note:

> C-GHOSTFUS:B-0031 [Q2 — At what degree threshold does this regime re-enter the "proven" zone?] - **Structural vs uniform missingness.** Yun et al. (2024, "Oldie but Goodie") report that FP's performance-drop rate became steeper in structurally missing scenarios, because whole-node missingness means a ghost has no observed channel anywhere on the node.
>
> C-GHOSTFUS:B-0032 [Q2 — At what degree threshold does this regime re-enter the "proven" zone?] This is biblion's exact case and predicts the crossover is worse than the 60% sparse-MCAR figure suggests.
>

## washout.1 (claim)

Um et al. (ICML 2025, "Propagate and Inject") prove that diffusion-based imputation methods "produce channels with nearly identical values within each channel, and these low-variance channels contribute very little to performance in graph learning tasks"; diffusion-based imputation provably produces low-variance, near-constant channels under high missingness. The review calls this the single most important finding: the mechanism biblion most needs to fear is documented.

- conf: not stated
- class: deriv (note: "prove")
- holds: diffusion-based imputation under high missingness
- src: umPropagateInjectRevisiting2025 (very recent preprint; limited independent replication)
- trail: C-GHOSTFUS §TL;DR, §Q1, §Caveats

From the note:

> C-GHOSTFUS:A-002 [TL;DR] - The single most important finding: the mechanism biblion most needs to fear is documented.
>
> C-GHOSTFUS:A-003 [TL;DR] Diffusion-based imputation provably produces low-variance, near-constant channels under high missingness (Um et al., ICML 2025), and zero-imputation biases representation magnitude in proportion to the observed fraction (Yi et al., ICLR 2020, the "variable sparsity problem").
>
> C-GHOSTFUS:B-0008 [Q1 — Does diffusion imputation preserve the co-citation bridge?] - **Low-variance collapse.** Um et al. (ICML 2025, "Propagate and Inject") prove that diffusion-based imputation methods "produce channels with nearly identical values within each channel, and these low-variance channels contribute very little to performance in graph learning tasks.
>
> C-GHOSTFUS:B-0126 [Caveats] - Several supporting sources are very recent preprints (Ferrini et al. 2026; Um et al. 2025; FSD-CAP 2026) and have had limited independent replication; weight them accordingly.
>

## washout.2 (claim)

A ghost node whose anchor is itself the diffusion average is exactly such a low-variance signal; pushing similarity between A and B through it can yield a near-constant contribution that carries little discriminative information.

- conf: not stated
- class: not stated
- holds: a ghost anchored to the diffusion average
- src: none (the reviewer's reasoning)
- trail: C-GHOSTFUS §Q1

From the note:

> C-GHOSTFUS:B-0009 [Q1 — Does diffusion imputation preserve the co-citation bridge?] A ghost node whose anchor is itself the diffusion average is exactly such a low-variance signal; pushing similarity between A and B through it can yield a near-constant contribution that carries little discriminative information.
>

## washout.3 (claim)

Repeated aggregation is Laplacian smoothing: node features converge toward a degree-scaled constant vector and Dirichlet energy decays to zero.

- conf: not stated
- class: not stated
- holds: repeated aggregation (oversmoothing / variance collapse)
- src: caiNoteOverSmoothingGraph2020, oonoGraphNeuralNetworks2020, anona (cited by URL)
- trail: C-GHOSTFUS §Q1

From the note:

> C-GHOSTFUS:B-0010 [Q1 — Does diffusion imputation preserve the co-citation bridge?] - **Oversmoothing / variance collapse.** Repeated aggregation is Laplacian smoothing; node features converge toward a degree-scaled constant vector and Dirichlet energy decays to zero (Cai & Wang; Oono & Suzuki).
>
> C-GHOSTFUS:B-0011 [Q1 — Does diffusion imputation preserve the co-citation bridge?] [arxiv](https://arxiv.org/pdf/2601.07419) APPNP's teleport term (alpha = 0.3 here) is specifically designed to resist this by re-anchoring each node to X each step, which is good for real nodes but is exactly what a ghost node lacks.
>

## washout.4 (claim)

UMAP optimizes local-neighbor preservation, so if a bridge produces only a weak global pull between A and B, min_dist and n_neighbors settings can absorb it, and HDBSCAN's mutual-reachability core-distance can treat a thin bridge as noise.

- conf: not stated
- class: not stated
- holds: UMAP followed by HDBSCAN
- src: none (the reviewer's reasoning)
- trail: C-GHOSTFUS §Q1

From the note:

> C-GHOSTFUS:B-0012 [Q1 — Does diffusion imputation preserve the co-citation bridge?] - **Dimensionality reduction smoothing.** UMAP optimizes local-neighbor preservation; if the bridge produces only a weak global pull between A and B, min_dist and n_neighbors settings can absorb it, and HDBSCAN's mutual-reachability core-distance can treat a thin bridge as noise.
>

## co-citation-bridge.1 (claim)

The relationship A -> ghost -> B is encoded by construction: the bridge is real in the propagation operator.

- conf: not stated
- class: not stated
- holds: APPNP propagation
- src: none (the reviewer's synthesis)
- trail: C-GHOSTFUS §Q1, §Key Findings

From the note:

> C-GHOSTFUS:A-009 [Key Findings] **The co-citation bridge is encoded by construction but not validated downstream.** Personalized-PageRank propagation (APPNP) does transmit similarity through shared intermediaries, and second-order proximity theory (LINE) confirms shared-neighbor nodes should embed closely.
>
> C-GHOSTFUS:B-0002 [Q1 — Does diffusion imputation preserve the co-citation bridge?] The relationship A -> ghost -> B is encoded by construction.
>
> C-GHOSTFUS:B-0005 [Q1 — Does diffusion imputation preserve the co-citation bridge?] So the bridge is real in the propagation operator.
>

## co-citation-bridge.2 (claim)

Personalized-PageRank propagation (APPNP) does transmit similarity through shared intermediaries, and second-order proximity theory (LINE) confirms that shared-neighbor nodes should embed closely.

- conf: not stated
- class: not stated
- holds: in principle; not shown for a fabricated intermediary, the ~70%-ghost dense-feature regime or a UMAP+HDBSCAN downstream
- src: tangLINELargescaleInformation2015
- trail: C-GHOSTFUS §Key Findings, §Q1

From the note:

> C-GHOSTFUS:A-009 [Key Findings] **The co-citation bridge is encoded by construction but not validated downstream.** Personalized-PageRank propagation (APPNP) does transmit similarity through shared intermediaries, and second-order proximity theory (LINE) confirms shared-neighbor nodes should embed closely.
>
> C-GHOSTFUS:B-0013 [Q1 — Does diffusion imputation preserve the co-citation bridge?] Scope/bound: all positive evidence (LINE second-order proximity, APPNP propagation, deep bibliographic coupling) establishes that shared intermediaries transmit similarity in principle.
>
> C-GHOSTFUS:B-0014 [Q1 — Does diffusion imputation preserve the co-citation bridge?] None of it covers the case where the intermediary's own vector is fabricated, nor the ~70%-ghost dense-feature regime, nor the specific UMAP+HDBSCAN downstream.
>

## co-citation-bridge.3 (claim)

The bridge is the graph-diffusion analogue of second-order proximity: LINE (Tang et al., 2015) formalizes that nodes with shared neighbors are likely to be similar, and bibliographic-coupling/co-citation theory treats two documents sharing a cited third work as similar by construction.

- conf: not stated
- class: not stated
- holds: second-order proximity; bibliographic coupling and co-citation
- src: tangLINELargescaleInformation2015
- trail: C-GHOSTFUS §Q1

From the note:

> C-GHOSTFUS:B-0003 [Q1 — Does diffusion imputation preserve the co-citation bridge?] APPNP's closed form, h = alpha(I - (1-alpha)D^-1 A)^-1 X, is a personalized-PageRank random walk with restart, [arxiv](https://arxiv.org/pdf/2312.16183) so a path through a shared intermediary does contribute to the stationary similarity between A and B. This is the graph-diffusion analogue of second-order proximity: LINE (Tang et al., 2015) formalizes that nodes with shared neighbors are likely to be similar, and bibliographic-coupling/co-citation theory treats two documents sharing a cited third work as similar by construction.
>

## co-citation-bridge.4 (claim)

Deep bibliographic coupling work extends coupling through graph diffusion precisely to densify sparse co-citation signal.

- conf: not stated
- class: not stated
- holds: citation graphs with sparse co-citation signal
- src: none (the note names deep bibliographic coupling work without a reference)
- trail: C-GHOSTFUS §Q1

From the note:

> C-GHOSTFUS:B-0004 [Q1 — Does diffusion imputation preserve the co-citation bridge?] Deep bibliographic coupling work extends coupling through graph diffusion precisely to densify sparse co-citation signal.
>

## co-citation-bridge.5 (claim)

All the positive evidence (LINE second-order proximity, APPNP propagation, deep bibliographic coupling) establishes only that shared intermediaries transmit similarity in principle; none of it covers the case where the intermediary's own vector is fabricated, nor the ~70%-ghost dense-feature regime, nor the specific UMAP+HDBSCAN downstream.

- conf: not stated
- class: search (note: "None of it covers")
- search: not stated
- holds: the evidence the review located
- src: tangLINELargescaleInformation2015
- trail: C-GHOSTFUS §Q1

From the note:

> C-GHOSTFUS:B-0013 [Q1 — Does diffusion imputation preserve the co-citation bridge?] Scope/bound: all positive evidence (LINE second-order proximity, APPNP propagation, deep bibliographic coupling) establishes that shared intermediaries transmit similarity in principle.
>
> C-GHOSTFUS:B-0014 [Q1 — Does diffusion imputation preserve the co-citation bridge?] None of it covers the case where the intermediary's own vector is fabricated, nor the ~70%-ghost dense-feature regime, nor the specific UMAP+HDBSCAN downstream.
>

Not found in the cited text (where to look, not what is wrong): holds: review

## co-citation-bridge.6 (claim)

The 1-hop co-citation relationship through a ghost is encoded, but there is no direct evidence that it survives usefully downstream in biblion's regime, and there are strong mechanistic reasons to expect partial washout: downstream survival is the problem, and three documented mechanisms threaten it (low-variance collapse, oversmoothing / variance collapse, dimensionality reduction smoothing).

- conf: not stated
- class: not stated
- holds: biblion's regime: ~70% ghosts, dense features, UMAP and HDBSCAN downstream
- src: umPropagateInjectRevisiting2025, caiNoteOverSmoothingGraph2020, oonoGraphNeuralNetworks2020
- trail: C-GHOSTFUS §Q1
- rating: "PARTIALLY DEMONSTRATED that the 1-hop relationship is encoded; NO DIRECT EVIDENCE that it survives usefully downstream in biblion's regime"
- contrary: not stated

From the note:

> C-GHOSTFUS:B-0001 [Q1 — Does diffusion imputation preserve the co-citation bridge?] **Verdict: PARTIALLY DEMONSTRATED that the 1-hop relationship is encoded; NO DIRECT EVIDENCE that it survives usefully downstream in biblion's regime, and strong mechanistic reasons to expect partial washout.**
>
> C-GHOSTFUS:B-0006 [Q1 — Does diffusion imputation preserve the co-citation bridge?] The downstream survival is the problem.
>
> C-GHOSTFUS:B-0007 [Q1 — Does diffusion imputation preserve the co-citation bridge?] Three documented mechanisms threaten it:
>
> C-GHOSTFUS:B-0008 [Q1 — Does diffusion imputation preserve the co-citation bridge?] - **Low-variance collapse.** Um et al. (ICML 2025, "Propagate and Inject") prove that diffusion-based imputation methods "produce channels with nearly identical values within each channel, and these low-variance channels contribute very little to performance in graph learning tasks.
>
> C-GHOSTFUS:B-0010 [Q1 — Does diffusion imputation preserve the co-citation bridge?] - **Oversmoothing / variance collapse.** Repeated aggregation is Laplacian smoothing; node features converge toward a degree-scaled constant vector and Dirichlet energy decays to zero (Cai & Wang; Oono & Suzuki).
>
> C-GHOSTFUS:B-0012 [Q1 — Does diffusion imputation preserve the co-citation bridge?] - **Dimensionality reduction smoothing.** UMAP optimizes local-neighbor preservation; if the bridge produces only a weak global pull between A and B, min_dist and n_neighbors settings can absorb it, and HDBSCAN's mutual-reachability core-distance can treat a thin bridge as noise.
>
> C-GHOSTFUS:B-0014 [Q1 — Does diffusion imputation preserve the co-citation bridge?] None of it covers the case where the intermediary's own vector is fabricated, nor the ~70%-ghost dense-feature regime, nor the specific UMAP+HDBSCAN downstream.
>

## co-citation-bridge.7 (claim)

A fabricated or zero anchor on the bridge node injects a low-variance or origin-pulling signal that variance collapse and oversmoothing can wash out before UMAP/HDBSCAN ever see it.

- conf: not stated
- class: not stated
- holds: a ghost bridge node with a fabricated or zero anchor
- src: none (the reviewer's synthesis)
- trail: C-GHOSTFUS §Key Findings

From the note:

> C-GHOSTFUS:A-010 [Key Findings] But a fabricated/zero anchor on the bridge node injects a low-variance or origin-pulling signal that variance-collapse and oversmoothing can wash out before UMAP/HDBSCAN ever see it.
>

## co-citation-bridge.8 (claim)

The co-citation bridge provably contributes to the APPNP stationary similarity, but low-variance collapse, oversmoothing and UMAP/HDBSCAN can all erode it; only stage-wise measurement on biblion can settle whether it survives.

- conf: not stated
- class: not stated
- holds: biblion's pipeline
- src: none (the reviewer's synthesis)
- trail: C-GHOSTFUS §Caveats

From the note:

> C-GHOSTFUS:B-0121 [Caveats] The co-citation bridge provably contributes to the APPNP stationary similarity, but low-variance collapse, oversmoothing, and UMAP/HDBSCAN can all erode it.
>
> C-GHOSTFUS:B-0122 [Caveats] Only stage-wise measurement on biblion can settle whether it survives.
>

## co-citation-bridge.9 (claim)

A degree-2 ghost is a much weaker conduit than a degree-50 one.

- conf: not stated
- class: not stated
- holds: ghost nodes by degree
- src: none (the reviewer's reasoning)
- trail: C-GHOSTFUS §Q1

From the note:

> C-GHOSTFUS:B-0020 [Q1 — Does diffusion imputation preserve the co-citation bridge?] - Confounds: ghost degree (a degree-2 ghost is a much weaker conduit than a degree-50 one), homophily of the bridged pair, and the number of competing non-ghost paths between A and B. A bridge "preserved" only because A and B were already close via other paths is not evidence the ghost did the work.
>

## co-citation-bridge.10 (claim)

A bridge "preserved" only because A and B were already close via other paths is not evidence that the ghost did the work.

- conf: not stated
- class: not stated
- holds: real-real pairs with competing non-ghost paths
- src: none (the reviewer's reasoning)
- trail: C-GHOSTFUS §Q1

From the note:

> C-GHOSTFUS:B-0020 [Q1 — Does diffusion imputation preserve the co-citation bridge?] - Confounds: ghost degree (a degree-2 ghost is a much weaker conduit than a degree-50 one), homophily of the bridged pair, and the number of competing non-ghost paths between A and B. A bridge "preserved" only because A and B were already close via other paths is not evidence the ghost did the work.
>

Not found in the cited text (where to look, not what is wrong): holds: real-real

## zero-anchor.1 (claim)

Yi et al. (ICLR 2020) prove the variable sparsity problem (VSP): with zero-imputation "the output of a predictive model largely varies with respect to the rate of missingness in the given input," scaling with the observed fraction, so that zero-imputation biases representation magnitude in proportion to the observed fraction; they correct it with Sparsity Normalization.

- conf: not stated
- class: deriv (note: "prove")
- holds: non-graph models, MCAR missingness
- src: yiWhyNotUse2020
- trail: C-GHOSTFUS §Q3, §TL;DR, §Q4

From the note:

> C-GHOSTFUS:A-003 [TL;DR] Diffusion-based imputation provably produces low-variance, near-constant channels under high missingness (Um et al., ICML 2025), and zero-imputation biases representation magnitude in proportion to the observed fraction (Yi et al., ICLR 2020, the "variable sparsity problem").
>
> C-GHOSTFUS:B-0049 [Q3 — Conduit-only featureless nodes vs imputed-position nodes] Yi et al. (ICLR 2020) prove the variable sparsity problem (VSP): with zero-imputation "the output of a predictive model largely varies with respect to the rate of missingness in the given input," scaling with the observed fraction, and they correct it with Sparsity Normalization.
>
> C-GHOSTFUS:B-0092 [Q4 — Interaction of the denoise stage with featureless-node injection] Yi et al.: non-graph, MCAR.
>

## zero-anchor.2 (claim)

Yi et al. prove that output magnitude scales with the observed fraction (their Theorem 1: expected output proportional to mu_m).

- conf: not stated
- class: deriv (note: "prove")
- holds: non-graph models, MCAR missingness
- src: yiWhyNotUse2020
- trail: C-GHOSTFUS §Q4

From the note:

> C-GHOSTFUS:B-0079 [Q4 — Interaction of the denoise stage with featureless-node injection] - **Zero-imputation magnitude bias.** Yi et al. (ICLR 2020) prove output magnitude scales with the observed fraction (their Theorem 1: expected output proportional to mu_m).
>
> C-GHOSTFUS:B-0092 [Q4 — Interaction of the denoise stage with featureless-node injection] Yi et al.: non-graph, MCAR.
>

Not found in the cited text (where to look, not what is wrong): holds: models

## zero-anchor.3 (claim)

Yi et al. note that GCN's Laplacian normalization "precisely matches" their Sparsity Normalization operation, tying the mechanism directly to graph message passing.

- conf: not stated
- class: not stated
- holds: GCN Laplacian normalization
- src: yiWhyNotUse2020 (cited by URL)
- trail: C-GHOSTFUS §Q4

From the note:

> C-GHOSTFUS:B-0079 [Q4 — Interaction of the denoise stage with featureless-node injection] - **Zero-imputation magnitude bias.** Yi et al. (ICLR 2020) prove output magnitude scales with the observed fraction (their Theorem 1: expected output proportional to mu_m).
>
> C-GHOSTFUS:B-0081 [Q4 — Interaction of the denoise stage with featureless-node injection] They note that GCN's Laplacian normalization "precisely matches" their Sparsity Normalization operation, [arxiv](https://arxiv.org/pdf/1906.00150) tying the mechanism directly to graph message passing.
>

## zero-anchor.4 (claim)

A zero-anchored ghost injects zeros into its neighbours' diffusion sums; in an averaging operator like D^-1 A it does what Rossi et al. describe for the Zero baseline ("the effect of zero-imputation is simply to reduce the norm of the average embeddings"), so it pulls its real neighbours toward the origin, distorting real-node geometry.

- conf: not stated
- class: not stated
- holds: an averaging operator such as D^-1 A with zero-anchored ghosts
- src: rossiUnreasonableEffectivenessFeature2022
- trail: C-GHOSTFUS §Q3
- rating: "well supported"

From the note:

> C-GHOSTFUS:B-0047 [Q3 — Conduit-only featureless nodes vs imputed-position nodes] The mechanism the question identifies is real and documented.
>
> C-GHOSTFUS:B-0048 [Q3 — Conduit-only featureless nodes vs imputed-position nodes] A zero-anchored ghost injects zeros into its neighbours' diffusion sums.
>
> C-GHOSTFUS:B-0049 [Q3 — Conduit-only featureless nodes vs imputed-position nodes] Yi et al. (ICLR 2020) prove the variable sparsity problem (VSP): with zero-imputation "the output of a predictive model largely varies with respect to the rate of missingness in the given input," scaling with the observed fraction, and they correct it with Sparsity Normalization.
>
> C-GHOSTFUS:B-0050 [Q3 — Conduit-only featureless nodes vs imputed-position nodes] In an averaging operator like D^-1 A, a zero-anchored neighbour does exactly what Rossi et al. describe for the Zero baseline: the effect of zero-imputation is simply to reduce the norm of the average embeddings.
>
> C-GHOSTFUS:B-0051 [Q3 — Conduit-only featureless nodes vs imputed-position nodes] So a zero-anchored ghost pulls its real neighbours toward the origin, distorting real-node geometry, precisely as the question states.
>
> C-GHOSTFUS:B-0063 [Q3 — Conduit-only featureless nodes vs imputed-position nodes] The mechanism is well supported; the head-to-head outcome in biblion is open.
>

## degree-threshold.1 (claim)

A missing-fraction crossover exists, but the specific degree threshold for biblion is not established and the trade-off against discarded structure is unquantified in the literature.

- conf: not stated
- class: not stated
- holds: biblion's degree threshold
- src: rossiUnreasonableEffectivenessFeature2022
- trail: C-GHOSTFUS §Q2
- rating: "PARTIALLY DEMONSTRATED that a missing-fraction crossover exists"
- contrary: not stated

From the note:

> C-GHOSTFUS:B-0023 [Q2 — At what degree threshold does this regime re-enter the "proven" zone?] **Verdict: PARTIALLY DEMONSTRATED that a missing-fraction crossover exists; the specific threshold for biblion is NOT established and the trade-off against discarded structure is unquantified in the literature.**
>
> C-GHOSTFUS:B-0024 [Q2 — At what degree threshold does this regime re-enter the "proven" zone?] The clearest anchor is Rossi et al.'s observation that "most methods perform extremely well up to 50% of missing features, suggesting that in general node features are redundant...
>

## degree-threshold.2 (claim)

A degree-threshold crossover exists in principle but is dataset-specific: Rossi et al.'s observations identify a soft crossover near 50-60% missing on their benchmarks, an empirical, sparse-feature, MCAR, node-classification-accuracy (downstream-accuracy) observation that is not a guarantee for dense SPECTER2 geometry.

- conf: not stated
- class: not stated
- holds: sparse-feature benchmarks under MCAR masking; node-classification accuracy
- src: rossiUnreasonableEffectivenessFeature2022
- trail: C-GHOSTFUS §Key Findings, §Q2

From the note:

> C-GHOSTFUS:A-011 [Key Findings] **A degree-threshold crossover exists in principle but is dataset-specific.** Rossi et al. observe methods perform well up to ~50% missing and that "the gap between methods opens up from around 60% of missing features.
>
> C-GHOSTFUS:A-012 [Key Findings] This ~60% figure is a downstream-accuracy crossover on sparse benchmarks, not a guarantee for dense SPECTER2 geometry, and raising the threshold discards graph structure.
>
> C-GHOSTFUS:B-0026 [Q2 — At what degree threshold does this regime re-enter the "proven" zone?] This identifies a soft crossover near 50-60% missing on their benchmarks. biblion at ~70% featureless sits just beyond it, in the region where only the strongest feature-aware methods (FP, PCFI) held up, and even those were tested under MCAR per-channel masking, not whole-node structural missingness.
>
> C-GHOSTFUS:B-0036 [Q2 — At what degree threshold does this regime re-enter the "proven" zone?] The ~50-60% figure is an empirical, sparse-feature, MCAR, node-classification-accuracy observation.
>

## degree-threshold.3 (claim)

biblion at ~70% featureless sits just beyond the crossover, in the region where only the strongest feature-aware methods (FP, PCFI) held up, and even those were tested under MCAR per-channel masking, not whole-node structural missingness.

- conf: not stated
- class: not stated
- holds: biblion's ~70% featureless fraction
- src: rossiUnreasonableEffectivenessFeature2022, umConfidenceBasedFeatureImputation2023
- trail: C-GHOSTFUS §Q2

From the note:

> C-GHOSTFUS:B-0026 [Q2 — At what degree threshold does this regime re-enter the "proven" zone?] This identifies a soft crossover near 50-60% missing on their benchmarks. biblion at ~70% featureless sits just beyond it, in the region where only the strongest feature-aware methods (FP, PCFI) held up, and even those were tested under MCAR per-channel masking, not whole-node structural missingness.
>

## degree-threshold.4 (claim)

Raising the degree threshold does shrink the featureless fraction, but at a structural cost: higher thresholds discard nodes and edges, removing the very co-citation bridges and shrinking the recovered graph.

- conf: not stated
- class: not stated
- holds: biblion's citation graph (the fallworm example)
- src: none (the reviewer's reasoning)
- trail: C-GHOSTFUS §Q2, §Key Findings

From the note:

> C-GHOSTFUS:A-012 [Key Findings] This ~60% figure is a downstream-accuracy crossover on sparse benchmarks, not a guarantee for dense SPECTER2 geometry, and raising the threshold discards graph structure.
>
> C-GHOSTFUS:B-0033 [Q2 — At what degree threshold does this regime re-enter the "proven" zone?] Raising the degree threshold does shrink the featureless fraction (the fallworm example: 3,392 ghosts vs 1,405 real at degree >= 2), but the cost is structural: higher thresholds discard nodes and edges, removing the very co-citation bridges Q1 cares about and shrinking the recovered graph.
>

## degree-threshold.5 (claim)

The literature does not quantify the recovered-structure-against-reliability trade-off for citation graphs; it must be measured on biblion.

- conf: not stated
- class: search (note: "The literature does not quantify")
- search: not stated
- holds: citation graphs
- src: none (the review's search)
- trail: C-GHOSTFUS §Q2

From the note:

> C-GHOSTFUS:B-0034 [Q2 — At what degree threshold does this regime re-enter the "proven" zone?] The literature does not quantify this recovered-structure-vs-reliability trade-off for citation graphs; it must be measured on biblion.
>

## degree-threshold.6 (claim)

There is no published phase-transition theorem giving a clean threshold as a function of missing fraction for dense features under structural missingness.

- conf: not stated
- class: search (note: "there is no published phase-transition theorem")
- search: not stated
- holds: dense features under structural missingness
- src: none (the review's search)
- trail: C-GHOSTFUS §Q2

From the note:

> C-GHOSTFUS:B-0035 [Q2 — At what degree threshold does this regime re-enter the "proven" zone?] Scope/bound: there is no published phase-transition theorem giving a clean threshold as a function of missing fraction for dense features under structural missingness.
>

## degree-threshold.7 (claim)

Raising the threshold also changes the degree distribution and homophily of the surviving graph, which independently affects diffusion quality.

- conf: not stated
- class: not stated
- holds: the graph surviving a higher degree threshold
- src: none (the reviewer's reasoning)
- trail: C-GHOSTFUS §Q2

From the note:

> C-GHOSTFUS:B-0042 [Q2 — At what degree threshold does this regime re-enter the "proven" zone?] - Confound: raising the threshold also changes the degree distribution and homophily of the surviving graph, which independently affects diffusion quality.
>

## degree-threshold.8 (claim)

A node in a dense real-feature neighborhood is in a different regime than one surrounded by ghosts, even at the same global threshold.

- conf: not stated
- class: not stated
- holds: local against global missingness
- src: none (the reviewer's reasoning)
- trail: C-GHOSTFUS §Q2

From the note:

> C-GHOSTFUS:B-0041 [Q2 — At what degree threshold does this regime re-enter the "proven" zone?] - Stratify by local rather than global missingness: a node in a dense real-feature neighborhood is in a different regime than one surrounded by ghosts, even at the same global threshold.
>

## degree-threshold.9 (claim)

If a modest threshold increase (say to >=3) cuts the featureless fraction well below 50% while retaining most bridges, that likely buys more than any operator tweak.

- conf: not stated
- class: not stated
- holds: conditional on the threshold sweep the review recommends
- src: none (the reviewer's judgement)
- trail: C-GHOSTFUS §Recommendations

From the note:

> C-GHOSTFUS:B-0112 [Recommendations] If a modest threshold increase (say to >=3) cuts the featureless fraction well below 50% while retaining most bridges, that likely buys more than any operator tweak.
>

Not found in the cited text (where to look, not what is wrong): holds: review

## conduit-operator.1 (claim)

Conduit-only participation is a sound operator design, but there is no direct evidence testing the specific zero-anchor-corruption mechanism in an APPNP fusion pipeline; the review calls this the most actionable open design question.

- conf: not stated
- class: not stated
- holds: APPNP fusion pipelines
- src: none (the review's verdict on the question)
- trail: C-GHOSTFUS §Q3
- rating: "PARTIALLY DEMONSTRATED as a sound operator design"
- contrary: not stated

From the note:

> C-GHOSTFUS:B-0045 [Q3 — Conduit-only featureless nodes vs imputed-position nodes] **Verdict: PARTIALLY DEMONSTRATED as a sound operator design; NO DIRECT EVIDENCE testing the specific zero-anchor-corruption mechanism in an APPNP fusion pipeline.
>
> C-GHOSTFUS:B-0046 [Q3 — Conduit-only featureless nodes vs imputed-position nodes] This is the most actionable open design question.**
>

## conduit-operator.2 (claim)

Conduit-only (masked) participation is a recognized and defensible operator design: virtual-node and masked-aggregation literature supports keeping a node in the propagation topology while excluding its (absent) features from the aggregation term. No paper tests exactly biblion's zero-anchor-corruption mechanism, so this is a design recommendation, not a proven result.

- conf: not stated
- class: not stated
- holds: virtual-node and masked-aggregation literature; not tested for biblion's mechanism
- src: gilmerNeuralMessagePassing2017, caiUnderstandingVirtualNodes2024
- trail: C-GHOSTFUS §Key Findings, §Q3
- contrary: not stated

From the note:

> C-GHOSTFUS:A-013 [Key Findings] **Conduit-only (masked) participation is a recognized and defensible operator design.** Virtual-node and masked-aggregation literature supports keeping a node in the propagation topology while excluding its (absent) features from the aggregation term.
>
> C-GHOSTFUS:A-014 [Key Findings] No paper tests exactly biblion's zero-anchor-corruption mechanism, so this is a design recommendation, not a proven result.
>
> C-GHOSTFUS:B-0052 [Q3 — Conduit-only featureless nodes vs imputed-position nodes] Conduit-only participation is supported by two literatures:
>
> C-GHOSTFUS:B-0053 [Q3 — Conduit-only featureless nodes vs imputed-position nodes] - **Virtual / pass-through nodes.** Virtual-node message passing (Gilmer et al.; Cai et al., "Understanding Virtual Nodes") routinely uses nodes that participate in topology and routing without contributing native features, serving as bridges for long-range information.
>

## conduit-operator.3 (claim)

Virtual-node message passing (Gilmer et al.; Cai et al., "Understanding Virtual Nodes") routinely uses nodes that participate in topology and routing without contributing native features, serving as bridges for long-range information: the structural precedent for a ghost that transmits A -> B influence without an anchor.

- conf: not stated
- class: not stated
- holds: virtual / pass-through nodes in message passing
- src: gilmerNeuralMessagePassing2017, caiUnderstandingVirtualNodes2024
- trail: C-GHOSTFUS §Q3

From the note:

> C-GHOSTFUS:B-0053 [Q3 — Conduit-only featureless nodes vs imputed-position nodes] - **Virtual / pass-through nodes.** Virtual-node message passing (Gilmer et al.; Cai et al., "Understanding Virtual Nodes") routinely uses nodes that participate in topology and routing without contributing native features, serving as bridges for long-range information.
>
> C-GHOSTFUS:B-0054 [Q3 — Conduit-only featureless nodes vs imputed-position nodes] This is the structural precedent for a ghost that transmits A -> B influence without an anchor.
>

## conduit-operator.4 (claim)

Feature-propagation variants and masked GNNs keep a binary mask B distinguishing observed from unobserved entries, and only the observed entries enter the feature-aggregation/teleport term.

- conf: not stated
- class: not stated
- holds: masked aggregation
- src: none (the note names feature-propagation variants and masked GNNs without a reference)
- trail: C-GHOSTFUS §Q3

From the note:

> C-GHOSTFUS:B-0055 [Q3 — Conduit-only featureless nodes vs imputed-position nodes] - **Masked aggregation.** Feature-propagation variants and masked GNNs keep a binary mask B distinguishing observed from unobserved entries, and only the observed entries enter the feature-aggregation/teleport term.
>

## conduit-operator.5 (claim)

A "no-self-anchor" or masked-APPNP variant would exclude the teleport contribution of a ghost (mask it out of the alpha*X term) while still letting it carry the (1-alpha)D^-1 A propagation term; this is mechanically straightforward in the APPNP recurrence and avoids the origin-pull.

- conf: not stated
- class: not stated
- holds: the APPNP recurrence
- src: none (the reviewer's design)
- trail: C-GHOSTFUS §Q3

From the note:

> C-GHOSTFUS:B-0056 [Q3 — Conduit-only featureless nodes vs imputed-position nodes] A "no-self-anchor" or masked-APPNP variant would exclude the teleport contribution of a ghost (mask it out of the alpha*X term) while still letting it carry the (1-alpha)D^-1 A propagation term.
>
> C-GHOSTFUS:B-0057 [Q3 — Conduit-only featureless nodes vs imputed-position nodes] This is mechanically straightforward in the APPNP recurrence and avoids the origin-pull.
>

## conduit-operator.6 (claim)

Feature Propagation's boundary-reset steady state is essentially a conduit treatment of unknown nodes, and it is why FP is robust where naive zero-imputation-then-GNN is not.

- conf: not stated
- class: not stated
- holds: FP against zero-imputation followed by a GNN
- src: rossiUnreasonableEffectivenessFeature2022
- trail: C-GHOSTFUS §Q3

From the note:

> C-GHOSTFUS:B-0058 [Q3 — Conduit-only featureless nodes vs imputed-position nodes] Crucially, Rossi et al.'s Feature Propagation already embodies a related insight: its steady state is independent of the zero initialization of unknown features, because the diffusion resets known features each step and lets unknowns be determined purely by the boundary.
>
> C-GHOSTFUS:B-0059 [Q3 — Conduit-only featureless nodes vs imputed-position nodes] [mlr](https://proceedings.mlr.press/v198/rossi22a/rossi22a.pdf) That is essentially a conduit treatment of unknown nodes, and it is why FP is robust where naive zero-imputation-then-GNN is not.
>

## conduit-operator.7 (claim)

Biblion's anchored APPNP, by contrast, gives every node (including ghosts) a fixed teleport anchor each step; if that anchor is fabricated, the ghost is not a clean conduit but a persistent injector. This is the strongest theoretical argument that a masked/no-self-anchor variant should better preserve the co-citation signal and distort real nodes less.

- conf: not stated
- class: not stated
- holds: biblion's anchored APPNP
- src: none (the reviewer's reasoning)
- trail: C-GHOSTFUS §Q3
- contrary: not stated

From the note:

> C-GHOSTFUS:B-0060 [Q3 — Conduit-only featureless nodes vs imputed-position nodes] Biblion's anchored APPNP, by contrast, gives every node (including ghosts) a fixed teleport anchor each step; if that anchor is fabricated, the ghost is NOT a clean conduit, it is a persistent injector.
>
> C-GHOSTFUS:B-0061 [Q3 — Conduit-only featureless nodes vs imputed-position nodes] This is the strongest theoretical argument that a masked/no-self-anchor variant should better preserve the co-citation signal and distort real nodes less.
>

## conduit-operator.8 (claim)

No located source runs the exact A/B test of "imputed-anchor ghost" vs "zero-anchor ghost" vs "masked conduit ghost" inside an APPNP fusion feeding UMAP/HDBSCAN; the mechanism is well supported, but the head-to-head outcome in biblion is open.

- conf: not stated
- class: search (note: "no located source")
- search: searched, not found (note: "no located source")
- holds: APPNP fusion feeding UMAP/HDBSCAN
- src: none (the review's search)
- trail: C-GHOSTFUS §Q3

From the note:

> C-GHOSTFUS:B-0062 [Q3 — Conduit-only featureless nodes vs imputed-position nodes] Scope/bound: no located source runs the exact A/B test of "imputed-anchor ghost" vs "zero-anchor ghost" vs "masked conduit ghost" inside an APPNP fusion feeding UMAP/HDBSCAN.
>
> C-GHOSTFUS:B-0063 [Q3 — Conduit-only featureless nodes vs imputed-position nodes] The mechanism is well supported; the head-to-head outcome in biblion is open.
>

## conduit-operator.9 (claim)

Low-variance collapse and zero-imputation magnitude bias both directly threaten the co-citation bridge and motivate a conduit-only operator.

- conf: not stated
- class: not stated
- holds: biblion's co-citation bridge
- src: umPropagateInjectRevisiting2025, yiWhyNotUse2020
- trail: C-GHOSTFUS §TL;DR

From the note:

> C-GHOSTFUS:A-003 [TL;DR] Diffusion-based imputation provably produces low-variance, near-constant channels under high missingness (Um et al., ICML 2025), and zero-imputation biases representation magnitude in proportion to the observed fraction (Yi et al., ICLR 2020, the "variable sparsity problem").
>
> C-GHOSTFUS:A-005 [TL;DR] Both directly threaten the co-citation bridge (Q1) and motivate a conduit-only operator (Q3).
>

## conduit-operator.10 (claim)

biblion should not assume imputed ghost anchors are reliable.

- conf: not stated
- class: not stated
- holds: biblion's imputed ghost anchors
- src: none (the review's conclusion)
- trail: C-GHOSTFUS §TL;DR
- contrary: not stated

From the note:

> C-GHOSTFUS:A-006 [TL;DR] - biblion should not assume imputed ghost anchors are reliable.
>

## conduit-operator.11 (claim)

The fabricated-anchor problem is specific to anchored fusion: a non-anchored diffusion (pure FP with boundary reset) sidesteps it, which is part of why the masked-operator recommendation is strong; but moving fully to FP would change biblion's architecture more than the targeted masked-APPNP variant.

- conf: not stated
- class: not stated
- holds: anchored against non-anchored diffusion
- src: none (the reviewer's reasoning)
- trail: C-GHOSTFUS §Caveats

From the note:

> C-GHOSTFUS:B-0127 [Caveats] - The fabricated-anchor problem is specific to ANCHORED fusion.
>
> C-GHOSTFUS:B-0128 [Caveats] A non-anchored diffusion (pure FP with boundary reset) sidesteps it, which is part of why the masked-operator recommendation is strong; but moving fully to FP would change biblion's architecture more than the targeted masked-APPNP variant.
>

## conduit-operator.12 (claim)

The masked / no-self-anchor APPNP variant is the highest-leverage, lowest-cost change and the design the FP literature most supports.

- conf: not stated
- class: not stated
- holds: biblion's pipeline
- src: none (the reviewer's judgement)
- trail: C-GHOSTFUS §Recommendations

From the note:

> C-GHOSTFUS:B-0108 [Recommendations] **Implement and A/B test a masked / no-self-anchor APPNP variant (Q3).** Exclude ghost teleport anchors from the alpha*X term while retaining ghosts in the (1-alpha)D^-1 A propagation.
>
> C-GHOSTFUS:B-0109 [Recommendations] This is the highest-leverage, lowest-cost change and is the design the FP literature most supports.
>

## conduit-operator.13 (claim)

Whether ghosts are included in the degree D of their neighbours changes the averaging weights even in the masked case.

- conf: not stated
- class: not stated
- holds: masked APPNP with degree normalization
- src: none (the reviewer's reasoning)
- trail: C-GHOSTFUS §Q3

From the note:

> C-GHOSTFUS:B-0068 [Q3 — Conduit-only featureless nodes vs imputed-position nodes] - Degree-normalization interaction: whether ghosts are included in the degree D of their neighbours changes the averaging weights even in the masked case; treat "in-degree-but-not-in-aggregation" vs "fully excluded" as separate conditions.
>

Not found in the cited text (where to look, not what is wrong): holds: appnp

## conduit-operator.14 (claim)

Bringing A and B closer through a masked ghost (the bridge) and reducing origin-pull are two goals that can trade off.

- conf: not stated
- class: not stated
- holds: the masked variant
- src: none (the reviewer's reasoning)
- trail: C-GHOSTFUS §Q3

From the note:

> C-GHOSTFUS:B-0069 [Q3 — Conduit-only featureless nodes vs imputed-position nodes] - Conduit efficacy metric: does the masked variant still bring A and B closer (the Q1 bridge) while reducing origin-pull?
>
> C-GHOSTFUS:B-0070 [Q3 — Conduit-only featureless nodes vs imputed-position nodes] The two goals can trade off.
>

