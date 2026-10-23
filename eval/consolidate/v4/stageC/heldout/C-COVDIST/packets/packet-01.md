## standardisation.1 (claim)

Because covariates have different units and scales, all distance constructions require prior commensuration; incommensurable variables are made comparable by z-score standardisation, range scaling, PCA/whitening, or Mahalanobis covariance-scaling, and this is itself a design choice, not a convention.

- conf: not stated
- class: not stated
- holds: distance constructions in continuous covariate space
- src: none (the reviewer's synthesis)
- trail: C-COVDIST §Key Findings, §Standardisation

From the note:

> C-COVDIST:A-006 [Key Findings] **Standardisation and correlation handling are themselves a design choice, not a convention.** Incommensurable variables are made comparable by z-score standardisation, range scaling, PCA/whitening, or Mahalanobis covariance-scaling.
>
> C-COVDIST:B-0051 [3. Standardisation across scales/units and handling of inter-variable correlation] Because covariates have different units and scales, all distance constructions require prior commensuration:
>

Not found in the cited text (where to look, not what is wrong): holds: in

## standardisation.2 (claim)

z-score standardisation (subtract the mean, divide by the SD) is used by AOA's Dissimilarity Index before weighting, and is the univariate building block of MESS/NT1.

- conf: not stated
- class: not stated
- holds: AOA, MESS and ExDet NT1
- src: meyerPredictingUnknownSpace2020, elithArtModellingRangeshifting2010, mesgaranHereBeDragons2014
- trail: C-COVDIST §Standardisation

From the note:

> C-COVDIST:B-0005 [1. The named distance constructions, what each measures, and the failure mode each guards against] **Nearest-training-neighbour distance — the Area of Applicability (AOA) and its Dissimilarity Index (DI).** Meyer and Pebesma proposed the AOA for spatial prediction models: a Dissimilarity Index based on the minimum distance, in predictor space, from a prediction point to the nearest training point, with predictors weighted by their model-derived importance and standardised.
>
> C-COVDIST:B-0016 [1. The named distance constructions, what each measures, and the failure mode each guards against] **MESS — Multivariate Environmental Similarity Surface (Elith, Kearney & Phillips).** For each variable, computes how far a point sits relative to the *range* of the reference set, referenced to the training distribution; the overall MESS is driven by the *most negative* (most dissimilar) single variable.
>
> C-COVDIST:B-0021 [1. The named distance constructions, what each measures, and the failure mode each guards against] **ExDet — Extrapolation Detection (Mesgaran, Cousens & Webber).** Two metrics: **NT1** (univariate, sum across variables of how far each is outside its reference min/max; ranges −∞ to 0) and **NT2** (the *combinational novelty* index, based on Mahalanobis distance to the training centroid; NT2 > 1 flags a novel combination).
>
> C-COVDIST:B-0052 [3. Standardisation across scales/units and handling of inter-variable correlation] - **z-score standardisation** (subtract mean, divide by SD): used by AOA's DI before weighting; the univariate building block of MESS/NT1.
>

## standardisation.3 (claim)

Range scaling (to [0,1]) is used in several digital soil mapping (DSM) implementations before distance computation.

- conf: not stated
- class: not stated
- holds: several DSM implementations
- src: none (the note names no implementation)
- trail: C-COVDIST §Standardisation

From the note:

> C-COVDIST:A-002 [TL;DR] - The strongest empirical finding across all four surveyed fields is that **no single distance/novelty metric reliably predicts observed transfer error**: benchmarks in species distribution modelling, digital soil mapping, QSAR, and machine-learning OOD detection independently report that metric performance depends on dataset, model, and failure mode, and that metric–error correlation is sometimes weak or near-zero.
>
> C-COVDIST:B-0053 [3. Standardisation across scales/units and handling of inter-variable correlation] - **Range scaling** (to [0,1]): used in several DSM implementations before distance computation.
>

## standardisation.4 (claim)

PCA / whitening rotates to uncorrelated axes and rescales to unit variance; it is used in QSAR (PCA on descriptors) and is the conceptual basis of feature normalisation in deep OOD detection.

- conf: not stated
- class: not stated
- holds: QSAR descriptors; deep OOD detection
- src: none (the note cites no source for it)
- trail: C-COVDIST §Standardisation

From the note:

> C-COVDIST:B-0054 [3. Standardisation across scales/units and handling of inter-variable correlation] - **PCA / whitening**: rotates to uncorrelated axes and rescales to unit variance, used in QSAR (PCA on descriptors) and as the conceptual basis of feature normalisation in deep OOD detection.
>

## standardisation.5 (claim)

Mahalanobis covariance-scaling with the inverse covariance matrix Σ⁻¹ simultaneously standardises variances and "de-correlates"/whitens the space; it is the natural multivariate generalisation of the z-score.

- conf: not stated
- class: not stated
- holds: multivariate covariate spaces
- src: none (the note cites no source for it)
- trail: C-COVDIST §Standardisation

From the note:

> C-COVDIST:B-0055 [3. Standardisation across scales/units and handling of inter-variable correlation] - **Mahalanobis covariance-scaling**: the inverse covariance matrix Σ⁻¹ simultaneously standardises variances and "de-correlates"/whitens the space; this is the natural multivariate generalisation of the z-score.
>

## standardisation.6 (claim)

The choice whether to z-score, range-scale, PCA-whiten or Mahalanobis-scale, and whether to weight by predictor importance (as AOA does), changes which points are flagged.

- conf: not stated
- class: not stated
- holds: distance-based novelty flags
- src: none (the reviewer's synthesis)
- trail: C-COVDIST §Recommendations

From the note:

> C-COVDIST:B-0084 [Recommendations] **Be explicit and consistent about standardisation.** Decide before computing distances whether you z-score, range-scale, PCA-whiten, or Mahalanobis-scale, and whether you weight by predictor importance (as AOA does).
>
> C-COVDIST:B-0085 [Recommendations] These choices change which points are flagged.
>

Not found in the cited text (where to look, not what is wrong): holds: distance-based

## near-neighbour-metrics.1 (claim)

Meyer and Pebesma proposed the Area of Applicability (AOA) for spatial prediction models: a Dissimilarity Index (DI) based on the minimum distance, in predictor space, from a prediction point to the nearest training point, with predictors weighted by their model-derived importance and standardised.

- conf: not stated
- class: not stated
- holds: spatial prediction models
- src: meyerPredictingUnknownSpace2020
- trail: C-COVDIST §The named

From the note:

> C-COVDIST:B-0005 [1. The named distance constructions, what each measures, and the failure mode each guards against] **Nearest-training-neighbour distance — the Area of Applicability (AOA) and its Dissimilarity Index (DI).** Meyer and Pebesma proposed the AOA for spatial prediction models: a Dissimilarity Index based on the minimum distance, in predictor space, from a prediction point to the nearest training point, with predictors weighted by their model-derived importance and standardised.
>

## near-neighbour-metrics.2 (claim)

A point is "outside the AOA" when its DI exceeds the (outlier-removed) maximum DI observed among training points during cross-validation.

- conf: not stated
- class: not stated
- holds: the AOA method
- src: meyerPredictingUnknownSpace2020
- trail: C-COVDIST §The named

From the note:

> C-COVDIST:B-0005 [1. The named distance constructions, what each measures, and the failure mode each guards against] **Nearest-training-neighbour distance — the Area of Applicability (AOA) and its Dissimilarity Index (DI).** Meyer and Pebesma proposed the AOA for spatial prediction models: a Dissimilarity Index based on the minimum distance, in predictor space, from a prediction point to the nearest training point, with predictors weighted by their model-derived importance and standardised.
>
> C-COVDIST:B-0006 [1. The named distance constructions, what each measures, and the failure mode each guards against] A point is "outside the AOA" when its DI exceeds the (outlier-removed) maximum DI observed among training points during cross-validation.
>

## near-neighbour-metrics.3 (claim)

The AOA's DI captures whether any close analogue exists in the training set, and guards against local data sparsity / no nearby support, even if the point is well inside the global cloud.

- conf: not stated
- class: not stated
- holds: the AOA Dissimilarity Index
- src: meyerPredictingUnknownSpace2020
- trail: C-COVDIST §The named

From the note:

> C-COVDIST:B-0005 [1. The named distance constructions, what each measures, and the failure mode each guards against] **Nearest-training-neighbour distance — the Area of Applicability (AOA) and its Dissimilarity Index (DI).** Meyer and Pebesma proposed the AOA for spatial prediction models: a Dissimilarity Index based on the minimum distance, in predictor space, from a prediction point to the nearest training point, with predictors weighted by their model-derived importance and standardised.
>
> C-COVDIST:B-0007 [1. The named distance constructions, what each measures, and the failure mode each guards against] *What it captures:* whether any close analogue exists in the training set.
>
> C-COVDIST:B-0008 [1. The named distance constructions, what each measures, and the failure mode each guards against] *Failure mode guarded against:* local data sparsity / no nearby support, even if the point is well inside the global cloud.
>

## near-neighbour-metrics.4 (claim)

In their original simulations, Meyer and Pebesma found that "the prediction error within the AOA is comparable to the cross-validation error of the trained model, while the cross-validation error does not apply outside the AOA."

- conf: not stated
- class: model (note: "In their original simulations")
- holds: simulated data (the note: a virtual catalogue; controlled-condition findings that may not capture real biotic interactions, measurement error or sampling bias)
- src: meyerPredictingUnknownSpace2020
- trail: C-COVDIST §The named, §Caveats

From the note:

> C-COVDIST:B-0009 [1. The named distance constructions, what each measures, and the failure mode each guards against] In their original simulations, Meyer and Pebesma found that "the prediction error within the AOA is comparable to the cross-validation error of the trained model, while the cross-validation error does not apply outside the AOA."
>
> C-COVDIST:B-0090 [Caveats] - Several supporting "average relationship" claims (distance correlates with error) come from simulation studies (Meyer & Pebesma's virtual catalogue; Velazco et al.'s virtual species); virtual-species and virtual-soil designs may not capture real biotic interactions, measurement error, or sampling bias, so their conclusions about metric behaviour should be read as controlled-condition findings.
>

Not found in the cited text (where to look, not what is wrong): holds: simulated

## near-neighbour-metrics.5 (claim)

The AOA DI uses a weighted Euclidean distance, not the full covariance.

- conf: not stated
- class: not stated
- holds: the AOA Dissimilarity Index
- src: meyerPredictingUnknownSpace2020
- trail: C-COVDIST §The near

From the note:

> C-COVDIST:B-0037 [2. The near-neighbour vs. envelope/centroid dichotomy (each construction assigned)] | Construction | Mode | Correlation-aware? |
>
> C-COVDIST:B-0038 [2. The near-neighbour vs. envelope/centroid dichotomy (each construction assigned)] | AOA Dissimilarity Index (Meyer & Pebesma) | Near-neighbour (local) | Weighted Euclidean; not full covariance |
>

Not found in the cited text (where to look, not what is wrong): DI

## near-neighbour-metrics.6 (claim)

Shape (Velazco et al.) is a model-agnostic SDM metric that computes the Mahalanobis distance from each projection point to its nearest training point (not the centroid), relativised by a dispersion factor (the average Mahalanobis distance of training points to their centroid).

- conf: not stated
- class: not stated
- holds: species distribution modelling (SDM)
- src: velazcoHowFarCan2024
- trail: C-COVDIST §The named

From the note:

> C-COVDIST:A-002 [TL;DR] - The strongest empirical finding across all four surveyed fields is that **no single distance/novelty metric reliably predicts observed transfer error**: benchmarks in species distribution modelling, digital soil mapping, QSAR, and machine-learning OOD detection independently report that metric performance depends on dataset, model, and failure mode, and that metric–error correlation is sometimes weak or near-zero.
>
> C-COVDIST:B-0010 [1. The named distance constructions, what each measures, and the failure mode each guards against] **Shape (Velazco et al.).** A model-agnostic SDM metric that computes the Mahalanobis distance from each projection point to its *nearest training point* (not the centroid), relativised by a dispersion factor (the average Mahalanobis distance of training points to their centroid).
>

## near-neighbour-metrics.7 (claim)

Shape captures near-neighbour novelty that follows the actual "shape" of the training cloud, with an adjustable threshold; it guards against the same failure mode as AOA, but is explicitly tunable and able to follow non-convex data geometry.

- conf: not stated
- class: not stated
- holds: SDM projection points
- src: velazcoHowFarCan2024
- trail: C-COVDIST §The named

From the note:

> C-COVDIST:B-0010 [1. The named distance constructions, what each measures, and the failure mode each guards against] **Shape (Velazco et al.).** A model-agnostic SDM metric that computes the Mahalanobis distance from each projection point to its *nearest training point* (not the centroid), relativised by a dispersion factor (the average Mahalanobis distance of training points to their centroid).
>
> C-COVDIST:B-0011 [1. The named distance constructions, what each measures, and the failure mode each guards against] *What it captures:* near-neighbour novelty that follows the actual "shape" of the training cloud, with an adjustable threshold.
>
> C-COVDIST:B-0012 [1. The named distance constructions, what each measures, and the failure mode each guards against] *Failure mode:* same as AOA but explicitly tunable and able to follow non-convex data geometry.
>

## near-neighbour-metrics.8 (claim)

Mobility-Oriented Parity (MOP; Owens et al.) measures environmental similarity by averaging the distance to a user-specified nearest fraction (for example the nearest 5–10%) of the training cloud, flagging "strict extrapolation" (value 0) where conditions are outside the training range.

- conf: not stated
- class: not stated
- holds: ecological niche models
- src: owensConstraintsInterpretationEcological2013
- trail: C-COVDIST §The named

From the note:

> C-COVDIST:B-0013 [1. The named distance constructions, what each measures, and the failure mode each guards against] **Mobility-Oriented Parity (MOP; Owens et al.).** Measures environmental similarity by averaging the distance to a user-specified nearest fraction (e.g., nearest 5–10%) of the training cloud, flagging "strict extrapolation" (value 0) where conditions are outside the training range.
>
> C-COVDIST:R-0037 [References] "Constraints on interpretation of ecological niche models by limited environmental ranges on calibration areas.
>

## near-neighbour-metrics.9 (claim)

MOP captures near-neighbour similarity to a portion of the reference cloud and guards against strict (univariate-range) extrapolation, while partially solving the centroid-reference problem; it is range-based, not correlation-aware.

- conf: not stated
- class: not stated
- holds: MOP
- src: owensConstraintsInterpretationEcological2013
- trail: C-COVDIST §The named, §The near

From the note:

> C-COVDIST:B-0013 [1. The named distance constructions, what each measures, and the failure mode each guards against] **Mobility-Oriented Parity (MOP; Owens et al.).** Measures environmental similarity by averaging the distance to a user-specified nearest fraction (e.g., nearest 5–10%) of the training cloud, flagging "strict extrapolation" (value 0) where conditions are outside the training range.
>
> C-COVDIST:B-0014 [1. The named distance constructions, what each measures, and the failure mode each guards against] *What it captures:* near-neighbour similarity to a portion of the reference cloud.
>
> C-COVDIST:B-0015 [1. The named distance constructions, what each measures, and the failure mode each guards against] *Failure mode:* strict (univariate-range) extrapolation, while partially solving the centroid-reference problem.
>
> C-COVDIST:B-0037 [2. The near-neighbour vs. envelope/centroid dichotomy (each construction assigned)] | Construction | Mode | Correlation-aware? |
>
> C-COVDIST:B-0040 [2. The near-neighbour vs. envelope/centroid dichotomy (each construction assigned)] | MOP (Owens et al.) | Near-neighbour (to nearest fraction) | No (range-based) |
>

## near-neighbour-metrics.10 (claim)

NNDM / kNNDM (Milà et al.; Linnenbrink et al.) are near-neighbour constructions in geographic distance, to which correlation-awareness does not apply.

- conf: not stated
- class: not stated
- holds: geographic distance
- src: milaNearestNeighbourDistance2022, linnenbrinkKNNDMCVKfold2024
- trail: C-COVDIST §The near

From the note:

> C-COVDIST:B-0037 [2. The near-neighbour vs. envelope/centroid dichotomy (each construction assigned)] | Construction | Mode | Correlation-aware? |
>
> C-COVDIST:B-0041 [2. The near-neighbour vs. envelope/centroid dichotomy (each construction assigned)] | NNDM / kNNDM (Milà et al.; Linnenbrink et al.) | Near-neighbour (geographic) | n/a (geographic distance) |
>

## near-neighbour-metrics.11 (claim)

kNN-distance applicability-domain methods, local outlier factor (LOF) and isolation forest are near-neighbour (local density) constructions whose correlation-awareness varies.

- conf: not stated
- class: not stated
- holds: kNN-distance AD, LOF, isolation forest
- src: none (the note cites no source for it)
- trail: C-COVDIST §The near

From the note:

> C-COVDIST:B-0037 [2. The near-neighbour vs. envelope/centroid dichotomy (each construction assigned)] | Construction | Mode | Correlation-aware? |
>
> C-COVDIST:B-0042 [2. The near-neighbour vs. envelope/centroid dichotomy (each construction assigned)] | kNN-distance AD; LOF; isolation forest | Near-neighbour (local density) | Varies |
>

## envelope-metrics.1 (claim)

MESS (Multivariate Environmental Similarity Surface; Elith, Kearney & Phillips) computes, for each variable, how far a point sits relative to the range of the reference set, referenced to the training distribution; the overall MESS is driven by the most negative (most dissimilar) single variable, and negative values flag points outside the univariate range of at least one variable.

- conf: not stated
- class: not stated
- holds: species distribution modelling
- src: elithArtModellingRangeshifting2010
- trail: C-COVDIST §The named

From the note:

> C-COVDIST:B-0016 [1. The named distance constructions, what each measures, and the failure mode each guards against] **MESS — Multivariate Environmental Similarity Surface (Elith, Kearney & Phillips).** For each variable, computes how far a point sits relative to the *range* of the reference set, referenced to the training distribution; the overall MESS is driven by the *most negative* (most dissimilar) single variable.
>
> C-COVDIST:B-0017 [1. The named distance constructions, what each measures, and the failure mode each guards against] Negative values flag points outside the univariate range of at least one variable.
>
> C-COVDIST:B-0050 [2. The near-neighbour vs. envelope/centroid dichotomy (each construction assigned)] The dichotomy is explicit in the SDM benchmarking literature: MESS and ExDet reference the training *centroid* and a rectilinear *envelope*, so their lowest extrapolation values sit near the centroid — "a poor reflection of the real environmental distance" — whereas AOA and Shape reference *each training point*, following the cloud's shape.
>

Not found in the cited text (where to look, not what is wrong): holds: modelling

## envelope-metrics.2 (claim)

MESS captures whether a point is outside overall univariate coverage and guards against univariate range exceedance (Type-1 novelty); its blind spot is that it cannot detect novel combinations of variables that are each individually in-range, and it references the centroid, so it can poorly reflect true environmental distance.

- conf: not stated
- class: not stated
- holds: MESS
- src: elithArtModellingRangeshifting2010
- trail: C-COVDIST §The named

From the note:

> C-COVDIST:B-0016 [1. The named distance constructions, what each measures, and the failure mode each guards against] **MESS — Multivariate Environmental Similarity Surface (Elith, Kearney & Phillips).** For each variable, computes how far a point sits relative to the *range* of the reference set, referenced to the training distribution; the overall MESS is driven by the *most negative* (most dissimilar) single variable.
>
> C-COVDIST:B-0018 [1. The named distance constructions, what each measures, and the failure mode each guards against] *What it captures:* whether a point is outside overall univariate coverage.
>
> C-COVDIST:B-0019 [1. The named distance constructions, what each measures, and the failure mode each guards against] *Failure mode guarded against:* univariate range exceedance (Type-1 novelty).
>
> C-COVDIST:B-0020 [1. The named distance constructions, what each measures, and the failure mode each guards against] *Blind spot:* it cannot detect novel combinations of variables that are each individually in-range, and it references the centroid, so it can poorly reflect true environmental distance.
>

## envelope-metrics.3 (claim)

ExDet (Extrapolation Detection; Mesgaran, Cousens & Webber) has two metrics: NT1, univariate, the sum across variables of how far each is outside its reference min/max (ranging −∞ to 0); and NT2, the combinational novelty index, based on Mahalanobis distance to the training centroid, with NT2 > 1 flagging a novel combination.

- conf: not stated
- class: not stated
- holds: projecting species distribution models
- src: mesgaranHereBeDragons2014
- trail: C-COVDIST §The named

From the note:

> C-COVDIST:B-0021 [1. The named distance constructions, what each measures, and the failure mode each guards against] **ExDet — Extrapolation Detection (Mesgaran, Cousens & Webber).** Two metrics: **NT1** (univariate, sum across variables of how far each is outside its reference min/max; ranges −∞ to 0) and **NT2** (the *combinational novelty* index, based on Mahalanobis distance to the training centroid; NT2 > 1 flags a novel combination).
>
> C-COVDIST:R-0024 [References] "Here be dragons: a tool for quantifying novelty due to covariate range and correlation change when projecting species distribution models.
>

## envelope-metrics.4 (claim)

ExDet captures both range novelty (NT1) and correlation-structure novelty (NT2), guarding against the "point inside every marginal range but in a never-seen combination" case, the canonical Type-2 failure that MESS and bounding boxes miss.

- conf: not stated
- class: not stated
- holds: ExDet
- src: mesgaranHereBeDragons2014
- trail: C-COVDIST §The named

From the note:

> C-COVDIST:B-0021 [1. The named distance constructions, what each measures, and the failure mode each guards against] **ExDet — Extrapolation Detection (Mesgaran, Cousens & Webber).** Two metrics: **NT1** (univariate, sum across variables of how far each is outside its reference min/max; ranges −∞ to 0) and **NT2** (the *combinational novelty* index, based on Mahalanobis distance to the training centroid; NT2 > 1 flags a novel combination).
>
> C-COVDIST:B-0022 [1. The named distance constructions, what each measures, and the failure mode each guards against] *What it captures:* both range novelty (NT1) and correlation-structure novelty (NT2).
>
> C-COVDIST:B-0023 [1. The named distance constructions, what each measures, and the failure mode each guards against] *Failure mode guarded against:* the "point inside every marginal range but in a never-seen combination" case — the canonical Type-2 failure that MESS and bounding boxes miss.
>

## envelope-metrics.5 (claim)

In Mesgaran et al.'s own analysis of Acacia cyclops, "more than half of the points (6617 of 10,785) from the global projection space that were found to lie within the univariate range of reference data exhibited distorted correlations."

- conf: not stated
- class: not stated
- holds: Acacia cyclops, global projection space
- src: mesgaranHereBeDragons2014
- trail: C-COVDIST §The named

From the note:

> C-COVDIST:B-0024 [1. The named distance constructions, what each measures, and the failure mode each guards against] In Mesgaran et al.'s own analysis of *Acacia cyclops*, "more than half of the points (6617 of 10,785) from the global projection space that were found to lie within the univariate range of reference data exhibited distorted correlations."
>

## envelope-metrics.6 (claim)

Mahalanobis distance to the centroid is the covariance-scaled distance from a point to the training mean: equivalently the standardized distance generalised to correlated multivariate data, and the term in the exponent of the multivariate normal density.

- conf: not stated
- class: not stated
- holds: multivariate covariate spaces
- src: none (the note cites no source for it)
- trail: C-COVDIST §The named

From the note:

> C-COVDIST:B-0025 [1. The named distance constructions, what each measures, and the failure mode each guards against] **Mahalanobis distance to the centroid.** The covariance-scaled distance from a point to the training mean; equivalently the standardized distance generalised to correlated multivariate data, and the term appearing in the exponent of the multivariate normal density.
>

## envelope-metrics.7 (claim)

Mahalanobis distance to the centroid captures position relative to the overall (ellipsoidal) training cloud, accounting for variance and correlation, and guards against outlier/combination novelty under an assumption of a (roughly) elliptical training distribution.

- conf: not stated
- class: not stated
- holds: (roughly) elliptical training distributions
- src: none (the note cites no source for it)
- trail: C-COVDIST §The named

From the note:

> C-COVDIST:B-0025 [1. The named distance constructions, what each measures, and the failure mode each guards against] **Mahalanobis distance to the centroid.** The covariance-scaled distance from a point to the training mean; equivalently the standardized distance generalised to correlated multivariate data, and the term appearing in the exponent of the multivariate normal density.
>
> C-COVDIST:B-0026 [1. The named distance constructions, what each measures, and the failure mode each guards against] *What it captures:* position relative to the overall (ellipsoidal) training cloud, accounting for variance and correlation.
>
> C-COVDIST:B-0027 [1. The named distance constructions, what each measures, and the failure mode each guards against] *Failure mode:* outlier/combination novelty under an assumption of (roughly) elliptical training distribution.
>

## envelope-metrics.8 (claim)

Mahalanobis distance is used directly for ecological niche modelling; sample mean/covariance, minimum covariance determinant and minimum volume ellipsoid are the three common ways to parameterise its location/scatter.

- conf: not stated
- class: not stated
- holds: ecological niche modelling
- src: none (the note cites no source for it)
- trail: C-COVDIST §The named

From the note:

> C-COVDIST:B-0025 [1. The named distance constructions, what each measures, and the failure mode each guards against] **Mahalanobis distance to the centroid.** The covariance-scaled distance from a point to the training mean; equivalently the standardized distance generalised to correlated multivariate data, and the term appearing in the exponent of the multivariate normal density.
>
> C-COVDIST:B-0028 [1. The named distance constructions, what each measures, and the failure mode each guards against] Used directly for ecological niche modelling; sample-mean/covariance, minimum covariance determinant, and minimum volume ellipsoid are the three common ways to parameterise its location/scatter.
>

## envelope-metrics.9 (claim)

In QSAR, the leverage (diagonal of the hat matrix X(XᵀX)⁻¹Xᵀ) measures a compound's distance from the descriptor-space centroid in the model's metric; the Williams plot displays standardized residuals against leverage, with a warning threshold h* (commonly 3p/n).

- conf: not stated
- class: not stated
- holds: QSAR applicability-domain (AD) methods
- src: none (the note cites no source for it)
- trail: C-COVDIST §The named

From the note:

> C-COVDIST:B-0029 [1. The named distance constructions, what each measures, and the failure mode each guards against] **Leverage / hat-matrix distance and range/convex-hull AD methods (QSAR).** The leverage (diagonal of the hat matrix X(XᵀX)⁻¹Xᵀ) measures a compound's distance from the descriptor-space centroid in the model's metric; the Williams plot displays standardized residuals vs. leverage, with a warning threshold h* (commonly 3p/n).
>

Not found in the cited text (where to look, not what is wrong): holds: applicability-domain

## envelope-metrics.10 (claim)

Bounding box and convex hull define the interpolation region geometrically; they are pure coverage constructs, while leverage is a centroid/envelope construct, monotone in Mahalanobis distance to the descriptor centroid. All guard against structural extrapolation beyond the descriptor space spanned by the training set.

- conf: not stated
- class: not stated
- holds: QSAR descriptor space
- src: none (the note cites no source for it)
- trail: C-COVDIST §The named

From the note:

> C-COVDIST:B-0029 [1. The named distance constructions, what each measures, and the failure mode each guards against] **Leverage / hat-matrix distance and range/convex-hull AD methods (QSAR).** The leverage (diagonal of the hat matrix X(XᵀX)⁻¹Xᵀ) measures a compound's distance from the descriptor-space centroid in the model's metric; the Williams plot displays standardized residuals vs. leverage, with a warning threshold h* (commonly 3p/n).
>
> C-COVDIST:B-0030 [1. The named distance constructions, what each measures, and the failure mode each guards against] Bounding box and convex hull define the interpolation region geometrically.
>
> C-COVDIST:B-0031 [1. The named distance constructions, what each measures, and the failure mode each guards against] *What it captures:* leverage is a centroid/envelope construct (it is monotone in Mahalanobis distance to the descriptor centroid); convex hull/range box are pure coverage constructs.
>
> C-COVDIST:B-0032 [1. The named distance constructions, what each measures, and the failure mode each guards against] *Failure mode:* structural extrapolation beyond the descriptor space spanned by the training set.
>

## envelope-metrics.11 (claim)

Correlation-awareness of the envelope and centroid constructions: MESS no; ExDet NT1 no; ExDet NT2 yes; Mahalanobis-to-centroid yes; leverage / hat values yes (in the model metric); bounding box no, convex hull partially.

- conf: not stated
- class: not stated
- holds: the review's assignment table
- src: elithArtModellingRangeshifting2010, mesgaranHereBeDragons2014
- trail: C-COVDIST §The near

From the note:

> C-COVDIST:B-0037 [2. The near-neighbour vs. envelope/centroid dichotomy (each construction assigned)] | Construction | Mode | Correlation-aware? |
>
> C-COVDIST:B-0043 [2. The near-neighbour vs. envelope/centroid dichotomy (each construction assigned)] | MESS (Elith et al.) | Envelope/centroid (univariate range + centroid) | No |
>
> C-COVDIST:B-0044 [2. The near-neighbour vs. envelope/centroid dichotomy (each construction assigned)] | ExDet NT1 (Mesgaran et al.) | Envelope (univariate range, summed) | No |
>
> C-COVDIST:B-0045 [2. The near-neighbour vs. envelope/centroid dichotomy (each construction assigned)] | ExDet NT2 (Mesgaran et al.) | Centroid (Mahalanobis) | Yes |
>
> C-COVDIST:B-0046 [2. The near-neighbour vs. envelope/centroid dichotomy (each construction assigned)] | Mahalanobis-to-centroid | Centroid | Yes |
>
> C-COVDIST:B-0047 [2. The near-neighbour vs. envelope/centroid dichotomy (each construction assigned)] | Leverage / hat values (QSAR) | Centroid | Yes (in model metric) |
>
> C-COVDIST:B-0048 [2. The near-neighbour vs. envelope/centroid dichotomy (each construction assigned)] | Bounding box / convex hull | Envelope | No (box) / partially (hull) |
>

Not found in the cited text (where to look, not what is wrong): holds: review

## density-novelty.1 (claim)

Weighted conformal prediction (Tibshirani, Barber, Candès & Ramdas) reweights nonconformity scores by the train→test covariate likelihood ratio w(x)=dP̃_X/dP_X to retain finite-sample coverage under covariate shift.

- conf: not stated
- class: not stated
- holds: covariate shift
- src: tibshiraniConformalPredictionCovariate2019
- trail: C-COVDIST §The named

From the note:

> C-COVDIST:B-0033 [1. The named distance constructions, what each measures, and the failure mode each guards against] **Conformal prediction, density-ratio/importance weighting, and one-class novelty detectors.** Weighted conformal prediction (Tibshirani, Barber, Candès & Ramdas) reweights nonconformity scores by the train→test covariate likelihood ratio w(x)=dP̃_X/dP_X to retain finite-sample coverage under covariate shift.
>

## density-novelty.2 (claim)

Weighted conformal prediction is not a "distance" but a density-ratio construction: it answers "how much rarer/commoner is this covariate value in training than in deployment?"

- conf: not stated
- class: not stated
- holds: weighted conformal prediction
- src: tibshiraniConformalPredictionCovariate2019
- trail: C-COVDIST §The named

From the note:

> C-COVDIST:B-0033 [1. The named distance constructions, what each measures, and the failure mode each guards against] **Conformal prediction, density-ratio/importance weighting, and one-class novelty detectors.** Weighted conformal prediction (Tibshirani, Barber, Candès & Ramdas) reweights nonconformity scores by the train→test covariate likelihood ratio w(x)=dP̃_X/dP_X to retain finite-sample coverage under covariate shift.
>
> C-COVDIST:B-0034 [1. The named distance constructions, what each measures, and the failure mode each guards against] This is not a "distance" but a *density-ratio* construction: it answers "how much rarer/commoner is this covariate value in training than in deployment?
>

## density-novelty.3 (claim)

Kernel density, one-class SVM, isolation forest and local outlier factor are used as covariate-space novelty detectors; in deep learning, Mahalanobis distance to class-conditional feature means is a standard post-hoc OOD score.

- conf: not stated
- class: not stated
- holds: covariate-space novelty detection; deep-learning OOD scoring
- src: none (the note cites no source for it)
- trail: C-COVDIST §The named

From the note:

> C-COVDIST:B-0035 [1. The named distance constructions, what each measures, and the failure mode each guards against] Kernel density, one-class SVM, isolation forest, and local outlier factor are used as covariate-space novelty detectors; in deep learning, Mahalanobis distance to class-conditional feature means is a standard post-hoc OOD score.
>

## density-novelty.4 (claim)

These detectors capture density/typicality rather than raw distance: LOF and isolation forest capture local density, kernel density and one-class SVM capture global support (correlation-awareness varies).

- conf: not stated
- class: not stated
- holds: one-class and density-based novelty detectors
- src: none (the note cites no source for it)
- trail: C-COVDIST §The named, §The near

From the note:

> C-COVDIST:B-0036 [1. The named distance constructions, what each measures, and the failure mode each guards against] *What they capture:* density/typicality rather than raw distance; LOF and isolation forest capture *local* density, kernel density and one-class SVM capture *global* support.
>
> C-COVDIST:B-0037 [2. The near-neighbour vs. envelope/centroid dichotomy (each construction assigned)] | Construction | Mode | Correlation-aware? |
>
> C-COVDIST:B-0049 [2. The near-neighbour vs. envelope/centroid dichotomy (each construction assigned)] | One-class SVM; kernel density | Global support/density | Varies |
>

Not found in the cited text (where to look, not what is wrong): holds: density-based

## distance-modes.1 (claim)

The dominant constructions split cleanly into two modes: near-neighbour (is there a close training analogue?) and envelope/centroid (is the point outside overall coverage of the training cloud?).

- conf: not stated
- class: not stated
- holds: OOD judgement in continuous covariate space
- src: none (the reviewer's synthesis)
- trail: C-COVDIST §TL;DR

From the note:

> C-COVDIST:A-001 [TL;DR] - There is **no settled, single standard** for judging out-of-distribution (OOD) status in continuous covariate space; practice is irreducibly **plural**, and the dominant constructions split cleanly into two modes — **near-neighbour** (is there a close training analogue?) and **envelope/centroid** (is the point outside overall coverage of the training cloud?).
>

## distance-modes.2 (claim)

Every named construction can be assigned to a near-neighbour/local mode (distance to the closest training point: AOA's Dissimilarity Index, Shape, MOP, NNDM, k-nearest-neighbour AD, local outlier factor) or an envelope/centroid/global mode (distance to the training centroid or coverage boundary: MESS, ExDet's NT1/NT2, Mahalanobis-to-centroid, leverage/hat values, bounding box, convex hull); some tools combine both.

- conf: not stated
- class: not stated
- holds: the constructions the review names
- src: none (the reviewer's synthesis)
- trail: C-COVDIST §Key Findings, §The near

From the note:

> C-COVDIST:A-004 [Key Findings] **Two modes, not one standard.** Every named construction can be assigned to either a *near-neighbour/local* mode (distance to the closest training point: AOA's Dissimilarity Index, Shape, MOP, NNDM, k-nearest-neighbour AD, local outlier factor) or an *envelope/centroid/global* mode (distance to the training centroid or coverage boundary: MESS, ExDet's NT1/NT2, Mahalanobis-to-centroid, leverage/hat values, bounding box, convex hull).
>
> C-COVDIST:A-005 [Key Findings] Some tools combine both.
>
> C-COVDIST:B-0037 [2. The near-neighbour vs. envelope/centroid dichotomy (each construction assigned)] | Construction | Mode | Correlation-aware? |
>
> C-COVDIST:B-0038 [2. The near-neighbour vs. envelope/centroid dichotomy (each construction assigned)] | AOA Dissimilarity Index (Meyer & Pebesma) | Near-neighbour (local) | Weighted Euclidean; not full covariance |
>
> C-COVDIST:B-0039 [2. The near-neighbour vs. envelope/centroid dichotomy (each construction assigned)] | Shape (Velazco et al.) | Near-neighbour (local) | Yes (Mahalanobis to nearest point) |
>
> C-COVDIST:B-0040 [2. The near-neighbour vs. envelope/centroid dichotomy (each construction assigned)] | MOP (Owens et al.) | Near-neighbour (to nearest fraction) | No (range-based) |
>
> C-COVDIST:B-0041 [2. The near-neighbour vs. envelope/centroid dichotomy (each construction assigned)] | NNDM / kNNDM (Milà et al.; Linnenbrink et al.) | Near-neighbour (geographic) | n/a (geographic distance) |
>
> C-COVDIST:B-0042 [2. The near-neighbour vs. envelope/centroid dichotomy (each construction assigned)] | kNN-distance AD; LOF; isolation forest | Near-neighbour (local density) | Varies |
>
> C-COVDIST:B-0043 [2. The near-neighbour vs. envelope/centroid dichotomy (each construction assigned)] | MESS (Elith et al.) | Envelope/centroid (univariate range + centroid) | No |
>
> C-COVDIST:B-0044 [2. The near-neighbour vs. envelope/centroid dichotomy (each construction assigned)] | ExDet NT1 (Mesgaran et al.) | Envelope (univariate range, summed) | No |
>
> C-COVDIST:B-0045 [2. The near-neighbour vs. envelope/centroid dichotomy (each construction assigned)] | ExDet NT2 (Mesgaran et al.) | Centroid (Mahalanobis) | Yes |
>
> C-COVDIST:B-0046 [2. The near-neighbour vs. envelope/centroid dichotomy (each construction assigned)] | Mahalanobis-to-centroid | Centroid | Yes |
>
> C-COVDIST:B-0047 [2. The near-neighbour vs. envelope/centroid dichotomy (each construction assigned)] | Leverage / hat values (QSAR) | Centroid | Yes (in model metric) |
>
> C-COVDIST:B-0048 [2. The near-neighbour vs. envelope/centroid dichotomy (each construction assigned)] | Bounding box / convex hull | Envelope | No (box) / partially (hull) |
>
> C-COVDIST:B-0049 [2. The near-neighbour vs. envelope/centroid dichotomy (each construction assigned)] | One-class SVM; kernel density | Global support/density | Varies |
>

Not found in the cited text (where to look, not what is wrong): holds: review

## distance-modes.3 (claim)

The dichotomy is explicit in the SDM benchmarking literature: MESS and ExDet reference the training centroid and a rectilinear envelope, so their lowest extrapolation values sit near the centroid, "a poor reflection of the real environmental distance", whereas AOA and Shape reference each training point, following the cloud's shape.

- conf: not stated
- class: not stated
- holds: species distribution modelling benchmarks
- src: none (the note names the SDM benchmarking literature without a citation for this sentence)
- trail: C-COVDIST §The near

From the note:

> C-COVDIST:B-0050 [2. The near-neighbour vs. envelope/centroid dichotomy (each construction assigned)] The dichotomy is explicit in the SDM benchmarking literature: MESS and ExDet reference the training *centroid* and a rectilinear *envelope*, so their lowest extrapolation values sit near the centroid — "a poor reflection of the real environmental distance" — whereas AOA and Shape reference *each training point*, following the cloud's shape.
>

Not found in the cited text (where to look, not what is wrong): holds: modelling

## distance-modes.4 (claim)

Different constructions guard against different failure modes (univariate range exceedance vs. novel covariate combinations vs. local data sparsity), and several validation studies explicitly recommend reporting multiple complementary metrics rather than trusting one.

- conf: not stated
- class: not stated
- holds: validation studies the review surveyed
- src: none (the note names no study for it)
- trail: C-COVDIST §TL;DR

From the note:

> C-COVDIST:A-003 [TL;DR] - Different constructions guard against **different failure modes** (univariate range exceedance vs. novel covariate combinations vs. local data sparsity), and several validation studies explicitly recommend reporting multiple complementary metrics rather than trusting one.
>

Not found in the cited text (where to look, not what is wrong): holds: review; holds: surveyed

## correlation-handling.1 (claim)

Inter-variable correlation is the dividing line between "Type-1" (marginal-range) novelty detectors and "Type-2" (combinational) detectors: Mahalanobis-based methods and PCA/whitening explicitly account for correlation, whereas MESS and bounding-box methods do not.

- conf: not stated
- class: not stated
- holds: novelty detectors in covariate space
- src: none (the reviewer's synthesis)
- trail: C-COVDIST §Key Findings

From the note:

> C-COVDIST:A-007 [Key Findings] Inter-variable correlation is the dividing line between "Type-1" (marginal-range) novelty detectors and "Type-2" (combinational) detectors: Mahalanobis-based methods and PCA/whitening explicitly account for correlation, whereas MESS and bounding-box methods do not.
>

Not found in the cited text (where to look, not what is wrong): holds: in

## correlation-handling.2 (claim)

Methods that ignore correlation (MESS, NT1, bounding box, Euclidean kNN on standardized variables) detect only marginal-range novelty; methods that incorporate the covariance matrix (Mahalanobis, ExDet NT2, Shape, leverage, PCA/whitening) can detect combinational novelty, a point inside every marginal range but in a never-observed combination.

- conf: not stated
- class: not stated
- holds: the methods the review names
- src: none (the reviewer's synthesis)
- trail: C-COVDIST §Standardisation

From the note:

> C-COVDIST:B-0056 [3. Standardisation across scales/units and handling of inter-variable correlation] **Correlation handling is the key axis distinguishing methods.** Methods that ignore correlation (MESS, NT1, bounding box, Euclidean kNN on standardized variables) detect only marginal-range novelty.
>
> C-COVDIST:B-0057 [3. Standardisation across scales/units and handling of inter-variable correlation] Methods that incorporate the covariance matrix (Mahalanobis, ExDet NT2, Shape, leverage, PCA/whitening) can detect *combinational* novelty — a point inside every marginal range but in a never-observed combination.
>

Not found in the cited text (where to look, not what is wrong): holds: review

## correlation-handling.3 (claim)

ExDet was explicitly built to add NT2 (correlation-change novelty) on top of MESS-style NT1.

- conf: not stated
- class: not stated
- holds: ExDet
- src: mesgaranHereBeDragons2014
- trail: C-COVDIST §Standardisation

From the note:

> C-COVDIST:B-0021 [1. The named distance constructions, what each measures, and the failure mode each guards against] **ExDet — Extrapolation Detection (Mesgaran, Cousens & Webber).** Two metrics: **NT1** (univariate, sum across variables of how far each is outside its reference min/max; ranges −∞ to 0) and **NT2** (the *combinational novelty* index, based on Mahalanobis distance to the training centroid; NT2 > 1 flags a novel combination).
>
> C-COVDIST:B-0058 [3. Standardisation across scales/units and handling of inter-variable correlation] ExDet was explicitly built to add NT2 (correlation-change novelty) on top of MESS-style NT1.
>

## correlation-handling.4 (claim)

The choice of how to estimate the covariance/location (sample, minimum covariance determinant, minimum volume ellipsoid) materially affects results, especially with small samples, error and bias.

- conf: not stated
- class: not stated
- holds: covariance-based methods, especially with small samples
- src: none (the note cites no source for it)
- trail: C-COVDIST §Standardisation

From the note:

> C-COVDIST:B-0059 [3. Standardisation across scales/units and handling of inter-variable correlation] The choice of how to estimate the covariance/location (sample, minimum covariance determinant, minimum volume ellipsoid) materially affects results, especially with small samples, error, and bias.
>

Not found in the cited text (where to look, not what is wrong): holds: covariance-based

## correlation-handling.5 (claim)

Novel combinations of in-range covariates are common with correlated predictors, the typical situation with genomic/environmental features.

- conf: not stated
- class: not stated
- holds: genomic/environmental features
- src: none (the reviewer's statement)
- trail: C-COVDIST §Recommendations

From the note:

> C-COVDIST:B-0082 [Recommendations] If your risk is *novel combinations* of in-range covariates (common with correlated predictors — the typical situation with genomic/environmental features), you need a correlation-aware metric: ExDet-NT2, Mahalanobis, or Shape.
>

## spatial-cv.1 (claim)

A related literature treats the geographic/feature distance between folds as a surrogate for prediction difficulty: Roberts et al. (2017) argued for blocking to reduce optimistic bias.

- conf: not stated
- class: not stated
- holds: spatial cross-validation
- src: robertsCrossvalidationStrategiesData2016
- trail: C-COVDIST §Spatial

From the note:

> C-COVDIST:B-0072 [5. Spatial cross-validation as a parallel, distance-based response] A related literature treats the *geographic/feature distance between folds* as a surrogate for prediction difficulty.
>
> C-COVDIST:B-0073 [5. Spatial cross-validation as a parallel, distance-based response] Roberts et al. (2017) argued for blocking to reduce optimistic bias; Milà et al. (2022) proposed Nearest-Neighbour Distance Matching (NNDM) LOO-CV, matching the test-to-train nearest-neighbour distance distribution to the prediction-to-train distribution; Linnenbrink et al. (2024) extended this to k-fold (kNNDM).
>

Not found in the cited text (where to look, not what is wrong): holds: cross-validation

## spatial-cv.2 (claim)

Milà et al. (2022) proposed Nearest-Neighbour Distance Matching (NNDM) LOO-CV, matching the test-to-train nearest-neighbour distance distribution to the prediction-to-train distribution, and Linnenbrink et al. (2024) extended this to k-fold (kNNDM).

- conf: not stated
- class: not stated
- holds: map validation
- src: milaNearestNeighbourDistance2022, linnenbrinkKNNDMCVKfold2024
- trail: C-COVDIST §Spatial

From the note:

> C-COVDIST:B-0073 [5. Spatial cross-validation as a parallel, distance-based response] Roberts et al. (2017) argued for blocking to reduce optimistic bias; Milà et al. (2022) proposed Nearest-Neighbour Distance Matching (NNDM) LOO-CV, matching the test-to-train nearest-neighbour distance distribution to the prediction-to-train distribution; Linnenbrink et al. (2024) extended this to k-fold (kNNDM).
>
> C-COVDIST:R-0034 [References] "Nearest neighbour distance matching leave-one-out cross-validation for map validation.
>

## spatial-cv.3 (claim)

Whether spatial cross-validation is the right way to evaluate map accuracy is disputed: Wadoux et al. (2021) countered that "spatial cross-validation is not the right way to evaluate map accuracy" when sampling is sound, and there is active disagreement about the right construction.

- conf: cont (note: "active disagreement")
- class: not stated
- holds: map accuracy evaluation when sampling is sound
- src: wadouxSpatialCrossvalidationNot2021, robertsCrossvalidationStrategiesData2016, milaNearestNeighbourDistance2022
- trail: C-COVDIST §Spatial
- contrary: not stated

From the note:

> C-COVDIST:B-0073 [5. Spatial cross-validation as a parallel, distance-based response] Roberts et al. (2017) argued for blocking to reduce optimistic bias; Milà et al. (2022) proposed Nearest-Neighbour Distance Matching (NNDM) LOO-CV, matching the test-to-train nearest-neighbour distance distribution to the prediction-to-train distribution; Linnenbrink et al. (2024) extended this to k-fold (kNNDM).
>
> C-COVDIST:B-0074 [5. Spatial cross-validation as a parallel, distance-based response] Wadoux et al. (2021) countered that "spatial cross-validation is not the right way to evaluate map accuracy" when sampling is sound, showing the debate is unsettled.
>
> C-COVDIST:B-0075 [5. Spatial cross-validation as a parallel, distance-based response] This field reinforces the main finding: the *distribution* of nearest-neighbour distances between deployment points and training data is treated as the operative quantity, and there is active disagreement about the right construction.
>

## spatial-cv.4 (claim)

In this field the distribution of nearest-neighbour distances between deployment points and training data is treated as the operative quantity.

- conf: not stated
- class: not stated
- holds: spatial cross-validation literature
- src: milaNearestNeighbourDistance2022, linnenbrinkKNNDMCVKfold2024
- trail: C-COVDIST §Spatial

From the note:

> C-COVDIST:B-0073 [5. Spatial cross-validation as a parallel, distance-based response] Roberts et al. (2017) argued for blocking to reduce optimistic bias; Milà et al. (2022) proposed Nearest-Neighbour Distance Matching (NNDM) LOO-CV, matching the test-to-train nearest-neighbour distance distribution to the prediction-to-train distribution; Linnenbrink et al. (2024) extended this to k-fold (kNNDM).
>
> C-COVDIST:B-0075 [5. Spatial cross-validation as a parallel, distance-based response] This field reinforces the main finding: the *distribution* of nearest-neighbour distances between deployment points and training data is treated as the operative quantity, and there is active disagreement about the right construction.
>

Not found in the cited text (where to look, not what is wrong): holds: cross-validation

## conformal-shift.1 (claim)

Weighted conformal prediction (Tibshirani, Barber, Candès & Ramdas, 2019) provides finite-sample coverage under covariate shift via the covariate likelihood ratio, sidestepping the need for a single "distance threshold".

- conf: not stated
- class: not stated
- holds: covariate shift
- src: tibshiraniConformalPredictionCovariate2019
- trail: C-COVDIST §Conformal

From the note:

> C-COVDIST:B-0076 [6. Conformal prediction under covariate shift (recent, 2019–2026)] Weighted conformal prediction (Tibshirani, Barber, Candès & Ramdas, 2019) provides finite-sample coverage under covariate shift via the covariate likelihood ratio, sidestepping the need for a single "distance threshold.
>

## conformal-shift.2 (claim)

Barber et al. (2023) generalised conformal prediction to non-exchangeable data (NexCP) with fixed weights; localized conformal prediction and randomly-localized variants add local adaptivity; recent extensions include conformal predictive systems under covariate shift (2024) and robustness to general distribution shift (for example Wasserstein-regularised and Lévy–Prokhorov approaches, 2025).

- conf: not stated
- class: not stated
- holds: non-exchangeable data and general distribution shift
- src: barberConformalPredictionBeyond2023
- trail: C-COVDIST §Conformal

From the note:

> C-COVDIST:B-0077 [6. Conformal prediction under covariate shift (recent, 2019–2026)] Barber et al. (2023) generalised to non-exchangeable data (NexCP) with fixed weights; localized conformal prediction and randomly-localized variants add local adaptivity; recent extensions include conformal predictive systems under covariate shift (2024) and robustness to general distribution shift (e.g., Wasserstein-regularised and Lévy–Prokhorov approaches, 2025).
>

## conformal-shift.3 (claim)

The conformal framing reframes "OOD" as density ratio rather than distance, and it does not resolve into a single covariate-space metric either; conformal/density-ratio methods require estimating the likelihood ratio and still do not produce a single universal distance threshold.

- conf: not stated
- class: not stated
- holds: conformal and density-ratio methods under covariate shift
- src: tibshiraniConformalPredictionCovariate2019, barberConformalPredictionBeyond2023
- trail: C-COVDIST §Conformal, §Recommendations

From the note:

> C-COVDIST:B-0076 [6. Conformal prediction under covariate shift (recent, 2019–2026)] Weighted conformal prediction (Tibshirani, Barber, Candès & Ramdas, 2019) provides finite-sample coverage under covariate shift via the covariate likelihood ratio, sidestepping the need for a single "distance threshold.
>
> C-COVDIST:B-0077 [6. Conformal prediction under covariate shift (recent, 2019–2026)] Barber et al. (2023) generalised to non-exchangeable data (NexCP) with fixed weights; localized conformal prediction and randomly-localized variants add local adaptivity; recent extensions include conformal predictive systems under covariate shift (2024) and robustness to general distribution shift (e.g., Wasserstein-regularised and Lévy–Prokhorov approaches, 2025).
>
> C-COVDIST:B-0078 [6. Conformal prediction under covariate shift (recent, 2019–2026)] The conformal framing reframes "OOD" as *density ratio* rather than *distance*, and it does not resolve into a single covariate-space metric either.
>
> C-COVDIST:B-0089 [Recommendations] **For rigorous uncertainty under covariate shift, prefer conformal/density-ratio methods** where coverage guarantees matter, recognising they require estimating the likelihood ratio and still do not produce a single universal distance threshold.
>

## conformal-shift.4 (claim)

The conformal-under-covariate-shift literature is moving fast (2022–2026); the newest robustness extensions are largely theoretical/empirical-on-benchmarks, and their performance on real ecological/genomic covariate spaces is not yet well established.

- conf: not stated
- class: not stated
- holds: real ecological/genomic covariate spaces
- src: none (the note cites no source for it)
- trail: C-COVDIST §Caveats
- rating: "not yet well established"

From the note:

> C-COVDIST:B-0093 [Caveats] - The conformal-under-covariate-shift literature is moving fast (2022–2026) and the newest robustness extensions are largely theoretical/empirical-on-benchmarks; their performance on real ecological/genomic covariate spaces is not yet well established.
>

## transfer-error.1 (claim)

No single distance/novelty metric reliably predicts observed transfer error: benchmarks in species distribution modelling, digital soil mapping, QSAR and machine-learning OOD detection independently report that metric performance depends on dataset, model and failure mode, and that metric–error correlation is sometimes weak or near-zero. The review calls this its strongest empirical finding, and these four independent "no single metric dominates" results the core of the review; the decisive empirical evidence is negative.

- conf: repl (note: "These four independent")
- class: not stated
- holds: four fields (SDM, DSM, QSAR, ML OOD detection); point-level transfer error across datasets and models
- src: velazcoHowFarCan2024, hateffardEvaluatingExtrapolationPotential2023, toplakAssessmentMachineLearning2014, yangOpenOODBenchmarkingGeneralized2022
- trail: C-COVDIST §TL;DR, §Key Findings, §Does any, §Recommendations
- contrary: not stated

From the note:

> C-COVDIST:A-002 [TL;DR] - The strongest empirical finding across all four surveyed fields is that **no single distance/novelty metric reliably predicts observed transfer error**: benchmarks in species distribution modelling, digital soil mapping, QSAR, and machine-learning OOD detection independently report that metric performance depends on dataset, model, and failure mode, and that metric–error correlation is sometimes weak or near-zero.
>
> C-COVDIST:A-008 [Key Findings] **The decisive empirical evidence is negative.** A 760-virtual-species SDM benchmark found improvement from truncation was largely *independent of which extrapolation metric* was used; a digital-soil-mapping study found *almost no correlation* between the AOA dissimilarity index and validation RMSE/MEC; a 20-dataset QSAR benchmark found reliability-scoring quality *sensitive to dataset and regression method*; and the OpenOOD machine-learning benchmark found *no single winner* across 40 methods.
>
> C-COVDIST:A-009 [Key Findings] These four independent "no single metric dominates" results are the core of this review.
>
> C-COVDIST:B-0060 [4. Does any single metric reliably predict observed transfer error? (The central question)] **The evidence converges on "no."**
>
> C-COVDIST:B-0079 [Recommendations] **Do not adopt a single metric as an OOD "standard."** The convergent benchmark evidence (Velazco et al. 2024; Hateffard et al. 2024; Toplak et al. 2014; OpenOOD 2022–2024) shows no metric reliably predicts point-level transfer error across datasets and models.
>

Not found in the cited text (where to look, not what is wrong): holds: dsm; holds: ml

## transfer-error.2 (claim)

The "no single metric dominates" conclusion is robust across fields, but is itself partly a function of how each benchmark defines "success" (RMSE improvement, AUROC, correlation with error); a metric weak on one criterion may be useful on another.

- conf: not stated
- class: not stated
- holds: the four benchmarks' success criteria
- src: none (the reviewer's caveat)
- trail: C-COVDIST §Caveats

From the note:

> C-COVDIST:B-0092 [Caveats] - The "no single metric dominates" conclusion is robust across fields but is itself partly a function of how each benchmark defines "success" (RMSE improvement, AUROC, correlation with error); a metric weak on one criterion may be useful on another.
>

## transfer-error.3 (claim)

Velazco et al. (Ecography 2024) used "760 virtual species to define different modeling conditions determined by species niche tolerance, distribution equilibrium condition, sample size, and algorithm," across six algorithms (generalized additive model, generalized linear model, Gaussian process, maximum entropy/Maxent, random forest and support vector machine), comparing Shape against MESS, EO, MOP, ExDet and AOA by the RMSE improvement (over n = 584,521 worldwide cells) from truncating predictions in non-analogue space.

- conf: not stated
- class: model (note: "760 virtual species")
- holds: virtual species (controlled-condition findings that may not capture real biotic interactions, measurement error or sampling bias); six SDM algorithms; 584,521 worldwide cells
- src: velazcoHowFarCan2024
- trail: C-COVDIST §Does any, §Caveats

From the note:

> C-COVDIST:B-0061 [4. Does any single metric reliably predict observed transfer error? (The central question)] - **SDM — Velazco et al. (Ecography 2024).** They used "760 virtual species to define different modeling conditions determined by species niche tolerance, distribution equilibrium condition, sample size, and algorithm," across six algorithms (generalized additive model, generalized linear model, Gaussian process, maximum entropy/Maxent, random forest, and support vector machine), comparing Shape against MESS, EO, MOP, ExDet, and AOA by measuring RMSE improvement (over n = 584,521 worldwide cells) from truncating predictions in non-analogue space.
>
> C-COVDIST:B-0090 [Caveats] - Several supporting "average relationship" claims (distance correlates with error) come from simulation studies (Meyer & Pebesma's virtual catalogue; Velazco et al.'s virtual species); virtual-species and virtual-soil designs may not capture real biotic interactions, measurement error, or sampling bias, so their conclusions about metric behaviour should be read as controlled-condition findings.
>

## transfer-error.4 (claim)

In Velazco et al.'s benchmark, improvement from truncation was substantial but largely independent of which extrapolation metric was used; AOA performed similarly to or worse than MESS/EO/MOP/ExDet; Shape's edge came entirely from its tunable threshold, with optimal thresholds depending on species niche breadth.

- conf: not stated
- class: model (note: "760-virtual-species SDM benchmark")
- holds: 760 virtual species, six algorithms
- src: velazcoHowFarCan2024
- trail: C-COVDIST §Does any, §Key Findings

From the note:

> C-COVDIST:A-008 [Key Findings] **The decisive empirical evidence is negative.** A 760-virtual-species SDM benchmark found improvement from truncation was largely *independent of which extrapolation metric* was used; a digital-soil-mapping study found *almost no correlation* between the AOA dissimilarity index and validation RMSE/MEC; a 20-dataset QSAR benchmark found reliability-scoring quality *sensitive to dataset and regression method*; and the OpenOOD machine-learning benchmark found *no single winner* across 40 methods.
>
> C-COVDIST:B-0061 [4. Does any single metric reliably predict observed transfer error? (The central question)] - **SDM — Velazco et al. (Ecography 2024).** They used "760 virtual species to define different modeling conditions determined by species niche tolerance, distribution equilibrium condition, sample size, and algorithm," across six algorithms (generalized additive model, generalized linear model, Gaussian process, maximum entropy/Maxent, random forest, and support vector machine), comparing Shape against MESS, EO, MOP, ExDet, and AOA by measuring RMSE improvement (over n = 584,521 worldwide cells) from truncating predictions in non-analogue space.
>
> C-COVDIST:B-0062 [4. Does any single metric reliably predict observed transfer error? (The central question)] Improvement from truncation was *substantial but largely independent of which metric was used*; AOA performed similarly to or worse than MESS/EO/MOP/ExDet; Shape's edge came entirely from its *tunable threshold*, with optimal thresholds depending on species niche breadth.
>

## transfer-error.5 (claim)

In Velazco et al.'s benchmark no conventional metric dominated, and all algorithms "had trouble predicting species niches."

- conf: not stated
- class: model (note: "760 virtual species")
- holds: 760 virtual species, six algorithms
- src: velazcoHowFarCan2024
- trail: C-COVDIST §Does any

From the note:

> C-COVDIST:B-0061 [4. Does any single metric reliably predict observed transfer error? (The central question)] - **SDM — Velazco et al. (Ecography 2024).** They used "760 virtual species to define different modeling conditions determined by species niche tolerance, distribution equilibrium condition, sample size, and algorithm," across six algorithms (generalized additive model, generalized linear model, Gaussian process, maximum entropy/Maxent, random forest, and support vector machine), comparing Shape against MESS, EO, MOP, ExDet, and AOA by measuring RMSE improvement (over n = 584,521 worldwide cells) from truncating predictions in non-analogue space.
>
> C-COVDIST:B-0063 [4. Does any single metric reliably predict observed transfer error? (The central question)] No conventional metric dominated; all algorithms "had trouble predicting species niches."
>

## transfer-error.6 (claim)

Hateffard, Steinbuch & Heuvelink (Geoderma 2024) compared four similarity/extrapolation measures (soil-type similarity, homosoil, AOA's DI, and quantile-regression-forest interval width) against validation RMSE and model efficiency coefficient (MEC), and reported that "weak correlation was found between the AOA dissimilarity index and DSM prediction accuracy."

- conf: not stated
- class: not stated
- holds: random forest digital soil mapping in four African countries
- src: hateffardEvaluatingExtrapolationPotential2023
- trail: C-COVDIST §Does any

From the note:

> C-COVDIST:B-0064 [4. Does any single metric reliably predict observed transfer error? (The central question)] - **Digital soil mapping — Hateffard, Steinbuch & Heuvelink (Geoderma 2024), four African countries.** Comparing four similarity/extrapolation measures (soil-type similarity, homosoil, AOA's DI, and quantile-regression-forest interval width) against validation RMSE and model efficiency coefficient (MEC), they reported that "weak correlation was found between the AOA dissimilarity index and DSM prediction accuracy," and concluded: "none of the measures had a strong correlation with the validation metrics.
>
> C-COVDIST:R-0015 [References] "Evaluating the extrapolation potential of random forest digital soil mapping.
>

Not found in the cited text (where to look, not what is wrong): holds: in

## transfer-error.7 (claim)

Hateffard et al. concluded: "none of the measures had a strong correlation with the validation metrics. This was particularly disappointing for AOA and QRF… homosoil and soil type methods had the strongest correlation with validation metrics."

- conf: not stated
- class: not stated
- holds: digital soil mapping in four African countries
- src: hateffardEvaluatingExtrapolationPotential2023
- trail: C-COVDIST §Does any

From the note:

> C-COVDIST:B-0064 [4. Does any single metric reliably predict observed transfer error? (The central question)] - **Digital soil mapping — Hateffard, Steinbuch & Heuvelink (Geoderma 2024), four African countries.** Comparing four similarity/extrapolation measures (soil-type similarity, homosoil, AOA's DI, and quantile-regression-forest interval width) against validation RMSE and model efficiency coefficient (MEC), they reported that "weak correlation was found between the AOA dissimilarity index and DSM prediction accuracy," and concluded: "none of the measures had a strong correlation with the validation metrics.
>
> C-COVDIST:B-0065 [4. Does any single metric reliably predict observed transfer error? (The central question)] This was particularly disappointing for AOA and QRF… homosoil and soil type methods had the strongest correlation with validation metrics.
>

Not found in the cited text (where to look, not what is wrong): holds: in

## transfer-error.8 (claim)

Hateffard et al.'s result directly contradicts the premise that the AOA's DI indicates prediction quality in new environments.

- conf: not stated
- class: not stated
- holds: digital soil mapping in four African countries
- src: hateffardEvaluatingExtrapolationPotential2023
- trail: C-COVDIST §Does any
- contrary: not stated

From the note:

> C-COVDIST:B-0064 [4. Does any single metric reliably predict observed transfer error? (The central question)] - **Digital soil mapping — Hateffard, Steinbuch & Heuvelink (Geoderma 2024), four African countries.** Comparing four similarity/extrapolation measures (soil-type similarity, homosoil, AOA's DI, and quantile-regression-forest interval width) against validation RMSE and model efficiency coefficient (MEC), they reported that "weak correlation was found between the AOA dissimilarity index and DSM prediction accuracy," and concluded: "none of the measures had a strong correlation with the validation metrics.
>
> C-COVDIST:B-0066 [4. Does any single metric reliably predict observed transfer error? (The central question)] This directly contradicts the premise that the DI indicates prediction quality in new environments.
>

## transfer-error.9 (claim)

Toplak et al. (J Chem Inf Model 2014), across "20 public QSAR data sets with continuous response," assessed "10 reliability scoring methods" by their correlation with prediction error: error-estimation methods could outperform pure similarity-to-training scores, but "the quality of reliability scoring methods is sensitive to data set characteristics and to the regression method used in QSAR", that is, there is no universally best applicability-domain (AD) method.

- conf: not stated
- class: not stated
- holds: 20 public QSAR data sets with continuous response; 10 reliability scoring methods
- src: toplakAssessmentMachineLearning2014
- trail: C-COVDIST §Does any, §Key Findings

From the note:

> C-COVDIST:A-008 [Key Findings] **The decisive empirical evidence is negative.** A 760-virtual-species SDM benchmark found improvement from truncation was largely *independent of which extrapolation metric* was used; a digital-soil-mapping study found *almost no correlation* between the AOA dissimilarity index and validation RMSE/MEC; a 20-dataset QSAR benchmark found reliability-scoring quality *sensitive to dataset and regression method*; and the OpenOOD machine-learning benchmark found *no single winner* across 40 methods.
>
> C-COVDIST:B-0067 [4. Does any single metric reliably predict observed transfer error? (The central question)] - **QSAR — Toplak et al. (J Chem Inf Model 2014).** Across "20 public QSAR data sets with continuous response," assessing "10 reliability scoring methods" by their correlation with prediction error, they found error-estimation methods could outperform pure similarity-to-training scores, but crucially that "the quality of reliability scoring methods is sensitive to data set characteristics and to the regression method used in QSAR" — i.e., no universally best AD method.
>
> C-COVDIST:R-0046 [References] "Assessment of machine learning reliability methods for quantifying the applicability domain of QSAR regression models.
>

## transfer-error.10 (claim)

Later QSPR benchmarks and reviews reach the same conclusion, that no single AD algorithm is universally accepted.

- conf: not stated
- class: not stated
- holds: QSPR benchmarks and reviews
- src: none (the note names later QSPR benchmarks and reviews without references)
- trail: C-COVDIST §Does any

From the note:

> C-COVDIST:B-0068 [4. Does any single metric reliably predict observed transfer error? (The central question)] Later QSPR benchmarks and reviews reach the same conclusion that no single AD algorithm is universally accepted.
>

## transfer-error.11 (claim)

OpenOOD (Yang et al., NeurIPS 2022; v1.5, 2023/2024), benchmarking 40 methods across multiple test environments, reports that "there is no single method that consistently outperforms others across benchmarks, and the ranking can be quite different from one data set to another," with rankings differing between near-OOD and far-OOD regimes: different metrics capture different failure modes.

- conf: not stated
- class: not stated
- holds: machine-learning OOD detection; 40 methods; near-OOD and far-OOD regimes
- src: yangOpenOODBenchmarkingGeneralized2022
- trail: C-COVDIST §Does any

From the note:

> C-COVDIST:B-0069 [4. Does any single metric reliably predict observed transfer error? (The central question)] - **Machine-learning OOD detection — OpenOOD (Yang et al., NeurIPS 2022; v1.5, 2023/2024).** Benchmarking 40 methods across multiple test environments, the authors report that "there is no single method that consistently outperforms others across benchmarks, and the ranking can be quite different from one data set to another," with rankings differing between near-OOD and far-OOD regimes — different metrics capture different failure modes.
>

