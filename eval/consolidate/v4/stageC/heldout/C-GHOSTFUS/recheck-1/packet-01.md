## missingness-regime.7 (claim)

SPECTER2 (768-d, dense, semantic) is exactly the dense regime where the comfortable missing-fraction crossover may move sharply leftward.

- conf: not stated
- class: not stated
- holds: SPECTER2 features
- src: none (the reviewer's reasoning)
- trail: C-GHOSTFUS §Q2

From the note:

> C-GHOSTFUS:B-0023 [Q2 — At what degree threshold does this regime re-enter the "proven" zone?] **Verdict: PARTIALLY DEMONSTRATED that a missing-fraction crossover exists; the specific threshold for biblion is NOT established and the trade-off against discarded structure is unquantified in the literature.**
>
> C-GHOSTFUS:B-0030 [Q2 — At what degree threshold does this regime re-enter the "proven" zone?] SPECTER2 (768-d, dense, semantic) is exactly the dense regime where the comfortable crossover may move sharply leftward.
>

## co-citation-bridge.1 (claim)

The relationship A -> ghost -> B is encoded by construction, but not validated downstream: the bridge is real in the propagation operator.

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

## co-citation-bridge.10 (claim)

A bridge "preserved" only because A and B were already close via other paths is not evidence that the ghost did the work.

- conf: not stated
- class: not stated
- holds: real-real pairs with competing non-ghost paths
- src: none (the reviewer's reasoning)
- trail: C-GHOSTFUS §Q1

From the note:

> C-GHOSTFUS:B-0017 [Q1 — Does diffusion imputation preserve the co-citation bridge?] - A clean contrast between real-real pairs bridged ONLY by a degree>=2 ghost versus pairs with a direct edge versus pairs with a real shared intermediary, holding citation distance fixed.
>
> C-GHOSTFUS:B-0020 [Q1 — Does diffusion imputation preserve the co-citation bridge?] - Confounds: ghost degree (a degree-2 ghost is a much weaker conduit than a degree-50 one), homophily of the bridged pair, and the number of competing non-ghost paths between A and B. A bridge "preserved" only because A and B were already close via other paths is not evidence the ghost did the work.
>

## degree-threshold.9 (claim)

If a modest threshold increase (say to >=3) cuts the featureless fraction well below 50% while retaining most bridges, that likely buys more than any operator tweak.

- conf: not stated
- class: not stated
- holds: conditional on the threshold sweep the review recommends
- src: none (the reviewer's judgement)
- trail: C-GHOSTFUS §Recommendations

From the note:

> C-GHOSTFUS:B-0111 [Recommendations] **Sweep the degree threshold (Q2) and plot reliability against retained structure.** Move to >=3 or >=5 only if imputation self-consistency improves materially AND bridge/edge retention stays acceptable.
>
> C-GHOSTFUS:B-0112 [Recommendations] If a modest threshold increase (say to >=3) cuts the featureless fraction well below 50% while retaining most bridges, that likely buys more than any operator tweak.
>

Not found in the cited text (where to look, not what is wrong): holds: review

## denoise-order.2 (claim)

Morehead et al. (arXiv:2203.12522) apply PCA-100 and an autoencoder a priori (before the GNN) and find it preserves accuracy and reduces prediction variance across seeds (Cora GCN: 80.82% original, std 0.62, vs 80.98% PCA-100, std 0.80, means over five seeds), though one model (GraphConv) degraded badly with the autoencoder bottleneck.

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

## denoise-order.6 (claim)

Any preprocessing that rescales magnitude (PCA centering, whitening, normalization) interacts with the zero-imputation magnitude bias.

- conf: not stated
- class: not stated
- holds: preprocessing before propagation
- src: yiWhyNotUse2020
- trail: C-GHOSTFUS §Q4

From the note:

> C-GHOSTFUS:B-0076 [Q4 — Interaction of the denoise stage with featureless-node injection] - **Order-of-operations on full features.** Morehead et al. (arXiv:2203.12522) apply PCA-100 and an autoencoder a priori (before the GNN) and find it preserves accuracy and reduces prediction variance across seeds (Cora GCN: 80.82% original, std 0.62, vs 80.98% PCA-100, std 0.80, means over five seeds).
>
> C-GHOSTFUS:B-0079 [Q4 — Interaction of the denoise stage with featureless-node injection] - **Zero-imputation magnitude bias.** Yi et al. (ICLR 2020) prove output magnitude scales with the observed fraction (their Theorem 1: expected output proportional to mu_m).
>
> C-GHOSTFUS:B-0080 [Q4 — Interaction of the denoise stage with featureless-node injection] Any preprocessing that rescales magnitude (PCA centering, whitening, normalization) therefore interacts with this bias.
>

## denoise-order.8 (claim)

Denoising tends to dampen the raw magnitude of low-variance directions.

- conf: not stated
- class: not stated
- holds: PCA denoising
- src: none (the reviewer's reasoning)
- trail: C-GHOSTFUS §Q4

From the note:

> C-GHOSTFUS:B-0085 [Q4 — Interaction of the denoise stage with featureless-node injection] Composing these: in biblion the PCA denoise runs on the REAL anchors only (a ghost has no features to denoise), so denoising happens before ghosts get any anchor.
>
> C-GHOSTFUS:B-0086 [Q4 — Interaction of the denoise stage with featureless-node injection] Denoising tends to dampen the raw magnitude of low-variance directions.
>

## dns.1 (do not say)

"Feature propagation is robust at biblion's missingness: Rossi et al. lost only 4.12% relative accuracy at 99% missing features."

- why: The note says the 4.12% figure is an MCAR, per-channel, sparse-feature, homophilous, node-classification-accuracy result, while biblion has structural (whole-node) missingness, dense SPECTER2 features, ~70% featureless nodes and unsupervised clustering, so the transfer is not warranted.
- instead: missingness-regime.3, feature-propagation.1
- trail: C-GHOSTFUS §Caveats

From the note:

> C-GHOSTFUS:A-008 [Key Findings] **The "proven zone" for feature propagation does not include biblion's regime.** Rossi et al. report only a 4.12% relative accuracy drop at 99% missing features, but explicitly under MCAR per-channel masking on homophilous benchmarks, and they note the method degrades toward the zero baseline as homophily falls. biblion has structural (whole-node) missingness, dense features, and ~70% featureless nodes at degree >= 2.
>
> C-GHOSTFUS:B-0118 [Caveats] - The headline robustness number (4.12% relative drop at 99% missing) is an MCAR, per-channel, sparse-feature, homophilous, node-classification-accuracy result. biblion is structural (whole-node) missingness, dense SPECTER2 features, ~70% featureless, unsupervised clustering.
>
> C-GHOSTFUS:B-0119 [Caveats] The transfer is not warranted; treat published thresholds as optimistic bounds.
>

Not found in the cited text (where to look, not what is wrong): "Feature propagation is robust at biblion missingness: Rossi et al. lost only 4.12% relative accuracy at 99% missing features."

