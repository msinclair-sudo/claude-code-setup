## transfer-error.12 (claim)

In OpenOOD, Mahalanobis-distance scoring is strong on far-OOD but weaker on near-OOD, and its performance is sensitive to feature normalisation.

- conf: not stated
- class: not stated
- holds: machine-learning OOD detection
- src: yangOpenOODBenchmarkingGeneralized2022
- trail: C-COVDIST §Does any

From the note:

> C-COVDIST:B-0069 [4. Does any single metric reliably predict observed transfer error? (The central question)] - **Machine-learning OOD detection — OpenOOD (Yang et al., NeurIPS 2022; v1.5, 2023/2024).** Benchmarking 40 methods across multiple test environments, the authors report that "there is no single method that consistently outperforms others across benchmarks, and the ranking can be quite different from one data set to another," with rankings differing between near-OOD and far-OOD regimes — different metrics capture different failure modes.
>
> C-COVDIST:B-0070 [4. Does any single metric reliably predict observed transfer error? (The central question)] Mahalanobis-distance scoring is strong on far-OOD but weaker on near-OOD, and its performance is sensitive to feature normalisation.
>

## transfer-error.13 (claim)

Distance in predictor space often correlates with error on average (Meyer & Pebesma's simulations; the broad cross-validation literature noting "increasing distance in predictor space often correlates with increasing error"), but this average relationship does not translate into a reliable point-level predictor of error in real case studies, and the strength of the relationship varies by dataset and model.

- conf: not stated
- class: not stated
- holds: average relationships, several from simulation studies (Meyer & Pebesma's virtual catalogue; Velazco et al.'s virtual species), to be read as controlled-condition findings; real case studies at point level
- src: meyerPredictingUnknownSpace2020
- trail: C-COVDIST §Does any, §Caveats

From the note:

> C-COVDIST:B-0071 [4. Does any single metric reliably predict observed transfer error? (The central question)] A consistent secondary theme: **distance in predictor space often correlates with error on average** (Meyer & Pebesma's simulations; the broad cross-validation literature noting "increasing distance in predictor space often correlates with increasing error"), but this average relationship does **not** translate into a reliable *point-level* predictor of error in real case studies, and the strength of the relationship varies by dataset and model.
>
> C-COVDIST:B-0090 [Caveats] - Several supporting "average relationship" claims (distance correlates with error) come from simulation studies (Meyer & Pebesma's virtual catalogue; Velazco et al.'s virtual species); virtual-species and virtual-soil designs may not capture real biotic interactions, measurement error, or sampling bias, so their conclusions about metric behaviour should be read as controlled-condition findings.
>

## ood-standard.1 (claim)

There is no settled, single standard for judging out-of-distribution (OOD) status in continuous covariate space; practice is irreducibly plural.

- conf: not stated
- class: not stated
- holds: OOD judgement in continuous covariate space, across the four surveyed fields
- src: none (the reviewer's synthesis)
- trail: C-COVDIST §TL;DR
- contrary: not stated

From the note:

> C-COVDIST:A-001 [TL;DR] - There is **no settled, single standard** for judging out-of-distribution (OOD) status in continuous covariate space; practice is irreducibly **plural**, and the dominant constructions split cleanly into two modes — **near-neighbour** (is there a close training analogue?) and **envelope/centroid** (is the point outside overall coverage of the training cloud?).
>
> C-COVDIST:A-002 [TL;DR] - The strongest empirical finding across all four surveyed fields is that **no single distance/novelty metric reliably predicts observed transfer error**: benchmarks in species distribution modelling, digital soil mapping, QSAR, and machine-learning OOD detection independently report that metric performance depends on dataset, model, and failure mode, and that metric–error correlation is sometimes weak or near-zero.
>

## ood-standard.2 (claim)

The QSAR and ecology literatures use different vocabularies ("applicability domain", "extrapolation", "novelty", "area of applicability", "OOD") for overlapping constructions; apparent disagreements sometimes reflect terminology rather than substance.

- conf: not stated
- class: not stated
- holds: QSAR and ecology literatures
- src: none (the reviewer's caveat)
- trail: C-COVDIST §Caveats

From the note:

> C-COVDIST:B-0091 [Caveats] - The QSAR and ecology literatures use different vocabularies ("applicability domain," "extrapolation," "novelty," "area of applicability," "OOD") for overlapping constructions; apparent disagreements sometimes reflect terminology rather than substance.
>

## dns.1 (do not say)

"The AOA dissimilarity index indicates prediction quality in new environments."

- why: Hateffard et al. found only weak correlation between the AOA dissimilarity index and digital soil mapping prediction accuracy, which the note says directly contradicts this premise.
- instead: transfer-error.6, transfer-error.8
- trail: C-COVDIST §Does any

From the note:

> C-COVDIST:B-0064 [4. Does any single metric reliably predict observed transfer error? (The central question)] - **Digital soil mapping — Hateffard, Steinbuch & Heuvelink (Geoderma 2024), four African countries.** Comparing four similarity/extrapolation measures (soil-type similarity, homosoil, AOA's DI, and quantile-regression-forest interval width) against validation RMSE and model efficiency coefficient (MEC), they reported that "weak correlation was found between the AOA dissimilarity index and DSM prediction accuracy," and concluded: "none of the measures had a strong correlation with the validation metrics.
>
> C-COVDIST:B-0066 [4. Does any single metric reliably predict observed transfer error? (The central question)] This directly contradicts the premise that the DI indicates prediction quality in new environments.
>

Not found in the cited text (where to look, not what is wrong): "The AOA dissimilarity index indicates prediction quality in new environments."

## dns.2 (do not say)

"A test point's distance from the training data in predictor space predicts its prediction error."

- why: The note says distance often correlates with error on average, but that this average relationship does not translate into a reliable point-level predictor of error in real case studies, and that its strength varies by dataset and model.
- instead: transfer-error.13, transfer-error.1
- trail: C-COVDIST §Does any

From the note:

> C-COVDIST:B-0071 [4. Does any single metric reliably predict observed transfer error? (The central question)] A consistent secondary theme: **distance in predictor space often correlates with error on average** (Meyer & Pebesma's simulations; the broad cross-validation literature noting "increasing distance in predictor space often correlates with increasing error"), but this average relationship does **not** translate into a reliable *point-level* predictor of error in real case studies, and the strength of the relationship varies by dataset and model.
>

Not found in the cited text (where to look, not what is wrong): "A test point distance from the training data in predictor space predicts its prediction error."

## dns.3 (do not say)

"Meyer & Pebesma's and Velazco et al.'s results show how distance metrics track error in real species and soil data."

- why: The note says these average-relationship results come from simulation studies (a virtual catalogue, virtual species) that may not capture real biotic interactions, measurement error or sampling bias, so they should be read as controlled-condition findings.
- instead: near-neighbour-metrics.4, transfer-error.3
- trail: C-COVDIST §Caveats

From the note:

> C-COVDIST:B-0090 [Caveats] - Several supporting "average relationship" claims (distance correlates with error) come from simulation studies (Meyer & Pebesma's virtual catalogue; Velazco et al.'s virtual species); virtual-species and virtual-soil designs may not capture real biotic interactions, measurement error, or sampling bias, so their conclusions about metric behaviour should be read as controlled-condition findings.
>

Not found in the cited text (where to look, not what is wrong): "Meyer & Pebesma and Velazco et al. results show how distance metrics track error in real species and soil data."

## dns.4 (do not say)

"Since no single metric dominates, distance metrics are no use for judging transfer."

- why: The note says the "no single metric dominates" conclusion is partly a function of how each benchmark defines success, and that a metric weak on one criterion may be useful on another.
- instead: transfer-error.2
- trail: C-COVDIST §Caveats

From the note:

> C-COVDIST:B-0092 [Caveats] - The "no single metric dominates" conclusion is robust across fields but is itself partly a function of how each benchmark defines "success" (RMSE improvement, AUROC, correlation with error); a metric weak on one criterion may be useful on another.
>

Not found in the cited text (where to look, not what is wrong): "Since no single metric dominates, distance metrics are no use for judging transfer."

## dns.5 (do not say)

"Spatial cross-validation is the right way to evaluate map accuracy."

- why: The note reports that Wadoux et al. (2021) countered this when sampling is sound, and that the debate is unsettled.
- instead: spatial-cv.3
- trail: C-COVDIST §Spatial

From the note:

> C-COVDIST:B-0074 [5. Spatial cross-validation as a parallel, distance-based response] Wadoux et al. (2021) countered that "spatial cross-validation is not the right way to evaluate map accuracy" when sampling is sound, showing the debate is unsettled.
>

Not found in the cited text (where to look, not what is wrong): "Spatial cross-validation is the right way to evaluate map accuracy."

