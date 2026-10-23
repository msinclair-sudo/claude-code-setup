## conduit-operator.15 (claim)

A masked ghost with no anchor and few edges may become a free-floating low-degree node that UMAP scatters.

- conf: not stated
- class: not stated
- holds: masked ghosts with few edges, under UMAP
- src: none (the reviewer's reasoning)
- trail: C-GHOSTFUS §Q3

From the note:

> C-GHOSTFUS:B-0071 [Q3 — Conduit-only featureless nodes vs imputed-position nodes] - Confound: a masked ghost with no anchor and few edges may become a free-floating low-degree node that UMAP scatters; check that excluding the anchor does not create new artifacts.
>

## conduit-operator.16 (claim)

Zero rows in the propagation can interact with row-normalization (division by degree), for isolated or near-isolated ghosts.

- conf: not stated
- class: not stated
- holds: row-normalized propagation
- src: none (the reviewer's reasoning)
- trail: C-GHOSTFUS §Q3

From the note:

> C-GHOSTFUS:B-0072 [Q3 — Conduit-only featureless nodes vs imputed-position nodes] - Numerical stability: zero rows in the propagation can interact with row-normalization (division by degree); document handling of isolated or near-isolated ghosts.
>

Not found in the cited text (where to look, not what is wrong): holds: row-normalized

## denoise-order.1 (claim)

The interaction of the PCA denoise stage with ghost injection (PCA denoise of real anchors x ghost injection, and denoise-then-propagate vs propagate-then-denoise) is unstudied at biblion's missingness and feature density: the component results exist (PCA-a-priori experiments on full features; zero-imputation magnitude bias; SVD-spectrum bias under zero-imputation) but no single source tests their interaction.

- conf: not stated
- class: search (note: "no single source tests their interaction")
- search: not stated
- holds: high, dense missingness (~70% missing, dense features)
- src: none (the review's verdict on the question)
- trail: C-GHOSTFUS §Q4, §Key Findings, §Caveats
- rating: "NO DIRECT EVIDENCE; genuinely open"

From the note:

> C-GHOSTFUS:A-015 [Key Findings] **The denoise-then-propagate vs propagate-then-denoise interaction under high dense missingness is essentially unstudied.** The pieces exist (PCA-a-priori experiments on full features; zero-imputation magnitude bias; SVD-spectrum bias under zero-imputation) but the specific combination biblion runs is an open question.
>
> C-GHOSTFUS:B-0073 [Q4 — Interaction of the denoise stage with featureless-node injection] **Verdict: NO DIRECT EVIDENCE; genuinely open.
>
> C-GHOSTFUS:B-0074 [Q4 — Interaction of the denoise stage with featureless-node injection] The component results exist but the specific interaction (PCA denoise of real anchors x ghost injection, and denoise-then-propagate vs propagate-then-denoise) is unstudied at biblion's missingness and feature density.**
>
> C-GHOSTFUS:B-0075 [Q4 — Interaction of the denoise stage with featureless-node injection] What is known decomposes into three established pieces that must be composed, because no single source tests their interaction:
>
> C-GHOSTFUS:B-0088 [Q4 — Interaction of the denoise stage with featureless-node injection] The literature does not resolve which dominates at ~70% missing on dense features.
>
> C-GHOSTFUS:B-0123 [Caveats] - Q4 is genuinely open.
>
> C-GHOSTFUS:B-0124 [Caveats] No source tests the PCA-denoise x ghost-injection interaction at this missingness and feature density; the recommendation rests on composed inference, not a demonstrated result.
>

## denoise-order.2 (claim)

Morehead et al. (arXiv:2203.12522) apply PCA-100 and an autoencoder a priori (before the GNN) and find it preserves accuracy and reduces prediction variance across seeds (Cora GCN: 80.82% original, std 0.62, vs 80.98% PCA-100, std 0.80, means over five seeds).

- conf: not stated
- class: not stated
- holds: full features with no missingness, sparse bag-of-words (Cora); reduce-then-propagate on complete data; not shown for ghosts
- src: moreheadSemiSupervisedGraphLearning2022
- trail: C-GHOSTFUS §Q4

From the note:

> C-GHOSTFUS:B-0076 [Q4 — Interaction of the denoise stage with featureless-node injection] - **Order-of-operations on full features.** Morehead et al. (arXiv:2203.12522) apply PCA-100 and an autoencoder a priori (before the GNN) and find it preserves accuracy and reduces prediction variance across seeds (Cora GCN: 80.82% original, std 0.62, vs 80.98% PCA-100, std 0.80, means over five seeds).
>
> C-GHOSTFUS:B-0077 [Q4 — Interaction of the denoise stage with featureless-node injection] But this is on full features with no missingness; it speaks only to reduce-then-propagate on complete data, and one model (GraphConv) degraded badly with the autoencoder bottleneck.
>
> C-GHOSTFUS:B-0078 [Q4 — Interaction of the denoise stage with featureless-node injection] It does not address ghosts.
>
> C-GHOSTFUS:B-0091 [Q4 — Interaction of the denoise stage with featureless-node injection] Morehead et al.: full features, sparse bag-of-words, no missingness.
>

## denoise-order.3 (claim)

In Morehead et al., one model (GraphConv) degraded badly with the autoencoder bottleneck.

- conf: not stated
- class: not stated
- holds: full features, no missingness
- src: moreheadSemiSupervisedGraphLearning2022
- trail: C-GHOSTFUS §Q4

From the note:

> C-GHOSTFUS:B-0076 [Q4 — Interaction of the denoise stage with featureless-node injection] - **Order-of-operations on full features.** Morehead et al. (arXiv:2203.12522) apply PCA-100 and an autoencoder a priori (before the GNN) and find it preserves accuracy and reduces prediction variance across seeds (Cora GCN: 80.82% original, std 0.62, vs 80.98% PCA-100, std 0.80, means over five seeds).
>
> C-GHOSTFUS:B-0077 [Q4 — Interaction of the denoise stage with featureless-node injection] But this is on full features with no missingness; it speaks only to reduce-then-propagate on complete data, and one model (GraphConv) degraded badly with the autoencoder bottleneck.
>

## denoise-order.4 (claim)

In classical PCA-with-missing-data, treating missing entries as zero biases the covariance/singular-value spectrum downward, and regularized iterative PCA (missMDA) deliberately shrinks singular values further as missingness grows.

- conf: not stated
- class: not stated
- holds: non-graph PCA with missing data
- src: anonb (cited by URL), josseMissMDAPackageHandling2016, anonc (cited by URL)
- trail: C-GHOSTFUS §Q4

From the note:

> C-GHOSTFUS:B-0082 [Q4 — Interaction of the denoise stage with featureless-node injection] - **SVD-spectrum bias under missingness.** In classical PCA-with-missing-data, treating missing entries as zero biases the covariance/singular-value spectrum downward; [arxiv](https://arxiv.org/pdf/1508.05431) regularized iterative PCA (missMDA) deliberately shrinks singular values further as missingness grows.
>
> C-GHOSTFUS:B-0083 [Q4 — Interaction of the denoise stage with featureless-node injection] [RDocumentation](https://www.rdocumentation.org/packages/missMDA/versions/1.18/topics/imputePCA) "Impute-then-SVD" and "SVD-on-observed-only" (O-ALS vs I-SVD) are distinct procedures that introduce different biases.
>
> C-GHOSTFUS:B-0093 [Q4 — Interaction of the denoise stage with featureless-node injection] PCA-missing-data: non-graph.
>

## denoise-order.5 (claim)

"Impute-then-SVD" and "SVD-on-observed-only" (O-ALS vs I-SVD) are distinct procedures that introduce different biases: the non-graph analogue of biblion's ordering question.

- conf: not stated
- class: not stated
- holds: non-graph PCA with missing data
- src: anond (cited by URL)
- trail: C-GHOSTFUS §Q4

From the note:

> C-GHOSTFUS:B-0083 [Q4 — Interaction of the denoise stage with featureless-node injection] [RDocumentation](https://www.rdocumentation.org/packages/missMDA/versions/1.18/topics/imputePCA) "Impute-then-SVD" and "SVD-on-observed-only" (O-ALS vs I-SVD) are distinct procedures that introduce different biases.
>
> C-GHOSTFUS:B-0084 [Q4 — Interaction of the denoise stage with featureless-node injection] [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0169743924000935) This is the non-graph analogue of biblion's ordering question.
>
> C-GHOSTFUS:B-0093 [Q4 — Interaction of the denoise stage with featureless-node injection] PCA-missing-data: non-graph.
>

## denoise-order.6 (claim)

Any preprocessing that rescales magnitude (PCA centering, whitening, normalization) interacts with the zero-imputation magnitude bias.

- conf: not stated
- class: not stated
- holds: preprocessing before propagation
- src: yiWhyNotUse2020
- trail: C-GHOSTFUS §Q4

From the note:

> C-GHOSTFUS:B-0079 [Q4 — Interaction of the denoise stage with featureless-node injection] - **Zero-imputation magnitude bias.** Yi et al. (ICLR 2020) prove output magnitude scales with the observed fraction (their Theorem 1: expected output proportional to mu_m).
>
> C-GHOSTFUS:B-0080 [Q4 — Interaction of the denoise stage with featureless-node injection] Any preprocessing that rescales magnitude (PCA centering, whitening, normalization) therefore interacts with this bias.
>

## denoise-order.7 (claim)

In biblion the PCA denoise runs on the real anchors only (a ghost has no features to denoise), so denoising happens before ghosts get any anchor; PCA is fit on real nodes only, so the basis is defined by real-feature covariance.

- conf: not stated
- class: not stated
- holds: the biblion pipeline
- src: none (the note's description of biblion)
- trail: C-GHOSTFUS §Q4

From the note:

> C-GHOSTFUS:B-0085 [Q4 — Interaction of the denoise stage with featureless-node injection] Composing these: in biblion the PCA denoise runs on the REAL anchors only (a ghost has no features to denoise), so denoising happens before ghosts get any anchor.
>
> C-GHOSTFUS:B-0101 [Q4 — Interaction of the denoise stage with featureless-node injection] - Confound: PCA is fit on real nodes only, so the basis is defined by real-feature covariance; injecting ghosts after the fit vs refitting with imputed ghosts are different and should be separated.
>

## denoise-order.8 (claim)

Denoising tends to dampen the raw magnitude of low-variance directions.

- conf: not stated
- class: not stated
- holds: PCA denoising
- src: none (the reviewer's reasoning)
- trail: C-GHOSTFUS §Q4

From the note:

> C-GHOSTFUS:B-0086 [Q4 — Interaction of the denoise stage with featureless-node injection] Denoising tends to dampen the raw magnitude of low-variance directions.
>

Not found in the cited text (where to look, not what is wrong): holds: pca

## denoise-order.9 (claim)

If a ghost is zero-anchored after denoising, the origin-pull it exerts is on already-centered, reduced-variance real vectors; the relative distortion could be larger (each retained dimension carries more relative weight) or smaller (absolute magnitudes are smaller), and the literature does not resolve which dominates at ~70% missing on dense features.

- conf: not stated
- class: not stated
- holds: ~70% missing, dense features
- src: none (the reviewer's reasoning)
- trail: C-GHOSTFUS §Q4

From the note:

> C-GHOSTFUS:B-0087 [Q4 — Interaction of the denoise stage with featureless-node injection] If a ghost is later zero-anchored, the origin-pull it exerts is on already-centered, reduced-variance real vectors; the relative distortion could be larger (because each retained dimension now carries more relative weight) or smaller (because absolute magnitudes are smaller).
>
> C-GHOSTFUS:B-0088 [Q4 — Interaction of the denoise stage with featureless-node injection] The literature does not resolve which dominates at ~70% missing on dense features.
>

## denoise-order.10 (claim)

The denoise-then-propagate order biblion uses is plausibly more robust than propagate-then-denoise, because FP-style diffusion is itself a low-pass denoiser, so denoising first avoids double-smoothing the imputed values.

- conf: not stated
- class: reading (note: "this is an inference, not a result")
- holds: biblion's denoise-then-propagate order
- src: none (the reviewer's inference)
- trail: C-GHOSTFUS §Q4

From the note:

> C-GHOSTFUS:B-0089 [Q4 — Interaction of the denoise stage with featureless-node injection] The denoise-then-propagate order biblion uses is plausibly more robust than propagate-then-denoise (because FP-style diffusion is itself a low-pass denoiser, so denoising first avoids double-smoothing the imputed values), but this is an inference, not a result.
>

## denoise-order.11 (claim)

Every supporting source for the denoise question is outside biblion's exact regime: Morehead et al. used full features, sparse bag-of-words and no missingness; Yi et al. are non-graph and MCAR; the PCA-missing-data work is non-graph; Ferrini et al. use mask-concatenation, not PCA ordering. The interaction is an open question that biblion is well-positioned to be the first to characterize.

- conf: not stated
- class: not stated
- holds: the sources the review located for the denoise question
- src: moreheadSemiSupervisedGraphLearning2022, yiWhyNotUse2020, ferriniRethinkingGNNsMissing2026
- trail: C-GHOSTFUS §Q4

From the note:

> C-GHOSTFUS:B-0090 [Q4 — Interaction of the denoise stage with featureless-node injection] Scope/bound: every supporting source is outside biblion's exact regime.
>
> C-GHOSTFUS:B-0091 [Q4 — Interaction of the denoise stage with featureless-node injection] Morehead et al.: full features, sparse bag-of-words, no missingness.
>
> C-GHOSTFUS:B-0092 [Q4 — Interaction of the denoise stage with featureless-node injection] Yi et al.: non-graph, MCAR.
>
> C-GHOSTFUS:B-0093 [Q4 — Interaction of the denoise stage with featureless-node injection] PCA-missing-data: non-graph.
>
> C-GHOSTFUS:B-0094 [Q4 — Interaction of the denoise stage with featureless-node injection] Ferrini et al.: dense-feature regime and structural missingness but mask-concatenation, [arxiv](https://arxiv.org/pdf/2601.04855) not PCA ordering.
>
> C-GHOSTFUS:B-0095 [Q4 — Interaction of the denoise stage with featureless-node injection] The interaction is an open question that biblion is well-positioned to be the first to characterize.
>

Not found in the cited text (where to look, not what is wrong): holds: review

## denoise-order.12 (claim)

A zero-anchored ghost may inject energy into low-variance directions that PCA would otherwise discard.

- conf: not stated
- class: not stated
- holds: PCA at 100-d
- src: none (the reviewer's reasoning)
- trail: C-GHOSTFUS §Q4

From the note:

> C-GHOSTFUS:B-0100 [Q4 — Interaction of the denoise stage with featureless-node injection] - Track explained-variance retained by PCA at 100-d and whether ghost-injected directions fall inside or outside the retained subspace; a zero-anchored ghost may inject energy into low-variance directions that PCA would otherwise discard.
>

## denoise-order.13 (claim)

Whitening equalizes variance across dimensions and would change the origin-pull geometry more than centering alone.

- conf: not stated
- class: not stated
- holds: whitening against centering-only
- src: none (the reviewer's reasoning)
- trail: C-GHOSTFUS §Q4

From the note:

> C-GHOSTFUS:B-0102 [Q4 — Interaction of the denoise stage with featureless-node injection] - Whitening vs centering-only: whitening equalizes variance across dimensions and would change the origin-pull geometry more than centering alone; treat as a controlled variable.
>

## denoise-order.14 (claim)

The order effect (denoise-then-propagate against propagate-then-denoise) is only interpretable when the ghost-injection space is also varied.

- conf: not stated
- class: not stated
- holds: raw 768-d against 100-d ghost injection
- src: none (the reviewer's reasoning)
- trail: C-GHOSTFUS §Q4

From the note:

> C-GHOSTFUS:B-0097 [Q4 — Interaction of the denoise stage with featureless-node injection] - Cross the two factors explicitly: {denoise-then-propagate, propagate-then-denoise} x {raw 768-d ghost injection, 100-d ghost injection} x {zero anchor, imputed anchor, masked conduit}.
>
> C-GHOSTFUS:B-0098 [Q4 — Interaction of the denoise stage with featureless-node injection] The order effect is only interpretable when ghost-injection space is also varied.
>

## dns.1 (do not say)

"Feature propagation is robust at biblion's missingness: Rossi et al. lost only 4.12% relative accuracy at 99% missing features."

- why: The note says the 4.12% figure is an MCAR, per-channel, sparse-feature, homophilous, node-classification-accuracy result, while biblion has structural (whole-node) missingness, dense SPECTER2 features, ~70% featureless nodes and unsupervised clustering, so the transfer is not warranted.
- instead: missingness-regime.3, feature-propagation.1
- trail: C-GHOSTFUS §Caveats

From the note:

> C-GHOSTFUS:B-0118 [Caveats] - The headline robustness number (4.12% relative drop at 99% missing) is an MCAR, per-channel, sparse-feature, homophilous, node-classification-accuracy result. biblion is structural (whole-node) missingness, dense SPECTER2 features, ~70% featureless, unsupervised clustering.
>
> C-GHOSTFUS:B-0119 [Caveats] The transfer is not warranted; treat published thresholds as optimistic bounds.
>

Not found in the cited text (where to look, not what is wrong): Rossi; "Feature propagation is robust at biblion missingness: Rossi et al. lost only 4.12% relative accuracy at 99% missing features."

## dns.2 (do not say)

"Because APPNP encodes the co-citation bridge by construction, the bridge survives into biblion's UMAP embedding and HDBSCAN clusters."

- why: The note says "encoded by construction" is not "validated downstream": low-variance collapse, oversmoothing and UMAP/HDBSCAN can all erode the bridge, and only stage-wise measurement on biblion can settle whether it survives.
- instead: co-citation-bridge.6, co-citation-bridge.8
- trail: C-GHOSTFUS §Caveats

From the note:

> C-GHOSTFUS:B-0120 [Caveats] - "Encoded by construction" is not "validated downstream.
>
> C-GHOSTFUS:B-0121 [Caveats] The co-citation bridge provably contributes to the APPNP stationary similarity, but low-variance collapse, oversmoothing, and UMAP/HDBSCAN can all erode it.
>
> C-GHOSTFUS:B-0122 [Caveats] Only stage-wise measurement on biblion can settle whether it survives.
>

Not found in the cited text (where to look, not what is wrong): "Because APPNP encodes the co-citation bridge by construction, the bridge survives into biblion UMAP embedding and HDBSCAN clusters."

## dns.3 (do not say)

"Below about 60% missing features, biblion is in the proven zone for feature propagation."

- why: The note says the ~50-60% figure is an empirical, sparse-feature, MCAR, node-classification-accuracy observation, to be treated as an upper-optimistic bound, not a target.
- instead: degree-threshold.2
- trail: C-GHOSTFUS §Q2

From the note:

> C-GHOSTFUS:B-0036 [Q2 — At what degree threshold does this regime re-enter the "proven" zone?] The ~50-60% figure is an empirical, sparse-feature, MCAR, node-classification-accuracy observation.
>
> C-GHOSTFUS:B-0037 [Q2 — At what degree threshold does this regime re-enter the "proven" zone?] Treat it as an upper-optimistic bound, not a target.
>

Not found in the cited text (where to look, not what is wrong): "Below about 60% missing features, biblion is in the proven zone for feature propagation."

## dns.4 (do not say)

"A masked, conduit-only ghost operator has been shown to prevent zero-anchor corruption."

- why: The note says no paper tests exactly biblion's zero-anchor-corruption mechanism, so conduit-only participation is a design recommendation, not a proven result.
- instead: conduit-operator.2, conduit-operator.8
- trail: C-GHOSTFUS §Key Findings

From the note:

> C-GHOSTFUS:A-013 [Key Findings] **Conduit-only (masked) participation is a recognized and defensible operator design.** Virtual-node and masked-aggregation literature supports keeping a node in the propagation topology while excluding its (absent) features from the aggregation term.
>
> C-GHOSTFUS:A-014 [Key Findings] No paper tests exactly biblion's zero-anchor-corruption mechanism, so this is a design recommendation, not a proven result.
>

Not found in the cited text (where to look, not what is wrong): "A masked, conduit-only ghost operator has been shown to prevent zero-anchor corruption."

## dns.5 (do not say)

"Denoising before propagation has been shown to be more robust than propagating before denoising."

- why: The note says this order is plausibly more robust but that this is an inference, not a result, and that its recommendation on the denoise stage rests on composed inference, not a demonstrated result.
- instead: denoise-order.10, denoise-order.1
- trail: C-GHOSTFUS §Q4

From the note:

> C-GHOSTFUS:B-0089 [Q4 — Interaction of the denoise stage with featureless-node injection] The denoise-then-propagate order biblion uses is plausibly more robust than propagate-then-denoise (because FP-style diffusion is itself a low-pass denoiser, so denoising first avoids double-smoothing the imputed values), but this is an inference, not a result.
>
> C-GHOSTFUS:B-0124 [Caveats] No source tests the PCA-denoise x ghost-injection interaction at this missingness and feature density; the recommendation rests on composed inference, not a demonstrated result.
>

Not found in the cited text (where to look, not what is wrong): "Denoising before propagation has been shown to be more robust than propagating before denoising."

