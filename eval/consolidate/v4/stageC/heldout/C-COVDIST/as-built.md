---
type: knowledge
title: Distance from training data to test points in continuous covariate space
inputs:
  - C-COVDIST: PhD/Proposal/Research/Results/Quantifying Distance from Training Data to Test Points in Continuous Covariate Space.md
answers:
  - C-COVDIST: §TL;DR, §Key Findings
refs: PhD/Proposal/Refs/Refs.bib
built: 2026-10-24
status: draft
tags:
  - research
  - knowledge
---

# Distance from training data to test points in continuous covariate space

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
| C-COVDIST | [[Quantifying Distance from Training Data to Test Points in Continuous Covariate Space]] | no | narrative author-year | no | no | fallback (answers and critique; the note has no labelled citations) |

## Concepts

### standardisation: making incommensurable covariates comparable
needs: none

- **standardisation.1** Because covariates have different units and scales, all distance constructions require prior commensuration; incommensurable variables are made comparable by z-score standardisation, range scaling, PCA/whitening, or Mahalanobis covariance-scaling, and this is itself a design choice, not a convention.
  conf: not stated · class: not stated · holds: distance constructions in continuous covariate space · src: none (the reviewer's synthesis) · trail: C-COVDIST §Key Findings, §Standardisation · from: C-COVDIST:A-006, C-COVDIST:B-0051
- **standardisation.2** z-score standardisation (subtract the mean, divide by the SD) is used by AOA's Dissimilarity Index before weighting, and is the univariate building block of MESS/NT1.
  conf: not stated · class: not stated · holds: AOA, MESS and ExDet NT1 · src: meyerPredictingUnknownSpace2020, elithArtModellingRangeshifting2010, mesgaranHereBeDragons2014 · trail: C-COVDIST §Standardisation · from: C-COVDIST:B-0005, C-COVDIST:B-0016, C-COVDIST:B-0021, C-COVDIST:B-0052
- **standardisation.3** Range scaling (to [0,1]) is used in several digital soil mapping (DSM) implementations before distance computation.
  conf: not stated · class: not stated · holds: several DSM implementations · src: none (the note names no implementation) · trail: C-COVDIST §Standardisation · from: C-COVDIST:A-002, C-COVDIST:B-0053
- **standardisation.4** PCA / whitening rotates to uncorrelated axes and rescales to unit variance; it is used in QSAR (PCA on descriptors) and is the conceptual basis of feature normalisation in deep OOD detection.
  conf: not stated · class: not stated · holds: QSAR descriptors; deep OOD detection · src: none (the note cites no source for it) · trail: C-COVDIST §Standardisation · from: C-COVDIST:B-0054
- **standardisation.5** Mahalanobis covariance-scaling with the inverse covariance matrix Σ⁻¹ simultaneously standardises variances and "de-correlates"/whitens the space; it is the natural multivariate generalisation of the z-score.
  conf: not stated · class: not stated · holds: multivariate covariate spaces · src: none (the note cites no source for it) · trail: C-COVDIST §Standardisation · from: C-COVDIST:B-0055
- **standardisation.6** The choice whether to z-score, range-scale, PCA-whiten or Mahalanobis-scale, and whether to weight by predictor importance (as AOA does), changes which points are flagged.
  conf: not stated · class: not stated · holds: distance-based novelty flags · src: none (the reviewer's synthesis) · trail: C-COVDIST §Recommendations · from: C-COVDIST:B-0084..0085

### near-neighbour-metrics: nearest-training-neighbour constructions
needs: standardisation

- **near-neighbour-metrics.1** Meyer and Pebesma proposed the Area of Applicability (AOA) for spatial prediction models: a Dissimilarity Index (DI) based on the minimum distance, in predictor space, from a prediction point to the nearest training point, with predictors weighted by their model-derived importance and standardised.
  conf: not stated · class: not stated · holds: spatial prediction models · src: meyerPredictingUnknownSpace2020 · trail: C-COVDIST §The named · from: C-COVDIST:B-0005
- **near-neighbour-metrics.2** A point is "outside the AOA" when its DI exceeds the (outlier-removed) maximum DI observed among training points during cross-validation.
  conf: not stated · class: not stated · holds: the AOA method · src: meyerPredictingUnknownSpace2020 · trail: C-COVDIST §The named · from: C-COVDIST:B-0005..0006
- **near-neighbour-metrics.3** The AOA's DI captures whether any close analogue exists in the training set, and guards against local data sparsity / no nearby support, even if the point is well inside the global cloud.
  conf: not stated · class: not stated · holds: the AOA Dissimilarity Index · src: meyerPredictingUnknownSpace2020 · trail: C-COVDIST §The named · from: C-COVDIST:B-0005, C-COVDIST:B-0007..0008
- **near-neighbour-metrics.4** In their original simulations, Meyer and Pebesma found that "the prediction error within the AOA is comparable to the cross-validation error of the trained model, while the cross-validation error does not apply outside the AOA."
  conf: not stated · class: model (note: "In their original simulations") · holds: simulated data (the note: a virtual catalogue; controlled-condition findings that may not capture real biotic interactions, measurement error or sampling bias) · src: meyerPredictingUnknownSpace2020 · trail: C-COVDIST §The named, §Caveats · from: C-COVDIST:B-0009, C-COVDIST:B-0090
- **near-neighbour-metrics.5** The AOA DI uses a weighted Euclidean distance, not the full covariance.
  conf: not stated · class: not stated · holds: the AOA Dissimilarity Index · src: meyerPredictingUnknownSpace2020 · trail: C-COVDIST §The near · from: C-COVDIST:B-0037..0038
- **near-neighbour-metrics.6** Shape (Velazco et al.) is a model-agnostic SDM metric that computes the Mahalanobis distance from each projection point to its nearest training point (not the centroid), relativised by a dispersion factor (the average Mahalanobis distance of training points to their centroid).
  conf: not stated · class: not stated · holds: species distribution modelling (SDM) · src: velazcoHowFarCan2024 · trail: C-COVDIST §The named · from: C-COVDIST:A-002, C-COVDIST:B-0010
- **near-neighbour-metrics.7** Shape captures near-neighbour novelty that follows the actual "shape" of the training cloud, with an adjustable threshold; it guards against the same failure mode as AOA, but is explicitly tunable and able to follow non-convex data geometry.
  conf: not stated · class: not stated · holds: SDM projection points · src: velazcoHowFarCan2024 · trail: C-COVDIST §The named · from: C-COVDIST:B-0010..0012
- **near-neighbour-metrics.8** Mobility-Oriented Parity (MOP; Owens et al.) measures environmental similarity by averaging the distance to a user-specified nearest fraction (for example the nearest 5–10%) of the training cloud, flagging "strict extrapolation" (value 0) where conditions are outside the training range.
  conf: not stated · class: not stated · holds: ecological niche models · src: owensConstraintsInterpretationEcological2013 · trail: C-COVDIST §The named · from: C-COVDIST:B-0013, C-COVDIST:R-0037
- **near-neighbour-metrics.9** MOP captures near-neighbour similarity to a portion of the reference cloud and guards against strict (univariate-range) extrapolation, while partially solving the centroid-reference problem; it is range-based, not correlation-aware.
  conf: not stated · class: not stated · holds: MOP · src: owensConstraintsInterpretationEcological2013 · trail: C-COVDIST §The named, §The near · from: C-COVDIST:B-0013..0015, C-COVDIST:B-0037, C-COVDIST:B-0040
- **near-neighbour-metrics.10** NNDM / kNNDM (Milà et al.; Linnenbrink et al.) are near-neighbour constructions in geographic distance, to which correlation-awareness does not apply.
  conf: not stated · class: not stated · holds: geographic distance · src: milaNearestNeighbourDistance2022, linnenbrinkKNNDMCVKfold2024 · trail: C-COVDIST §The near · from: C-COVDIST:B-0037, C-COVDIST:B-0041
- **near-neighbour-metrics.11** kNN-distance applicability-domain methods, local outlier factor (LOF) and isolation forest are near-neighbour (local density) constructions whose correlation-awareness varies.
  conf: not stated · class: not stated · holds: kNN-distance AD, LOF, isolation forest · src: none (the note cites no source for it) · trail: C-COVDIST §The near · from: C-COVDIST:B-0037, C-COVDIST:B-0042

### envelope-metrics: envelope and centroid constructions
needs: standardisation

- **envelope-metrics.1** MESS (Multivariate Environmental Similarity Surface; Elith, Kearney & Phillips) computes, for each variable, how far a point sits relative to the range of the reference set, referenced to the training distribution; the overall MESS is driven by the most negative (most dissimilar) single variable, and negative values flag points outside the univariate range of at least one variable.
  conf: not stated · class: not stated · holds: species distribution modelling · src: elithArtModellingRangeshifting2010 · trail: C-COVDIST §The named · from: C-COVDIST:B-0016..0017, C-COVDIST:B-0050
- **envelope-metrics.2** MESS captures whether a point is outside overall univariate coverage and guards against univariate range exceedance (Type-1 novelty); its blind spot is that it cannot detect novel combinations of variables that are each individually in-range, and it references the centroid, so it can poorly reflect true environmental distance.
  conf: not stated · class: not stated · holds: MESS · src: elithArtModellingRangeshifting2010 · trail: C-COVDIST §The named · from: C-COVDIST:B-0016, C-COVDIST:B-0018..0020
- **envelope-metrics.3** ExDet (Extrapolation Detection; Mesgaran, Cousens & Webber) has two metrics: NT1, univariate, the sum across variables of how far each is outside its reference min/max (ranging −∞ to 0); and NT2, the combinational novelty index, based on Mahalanobis distance to the training centroid, with NT2 > 1 flagging a novel combination.
  conf: not stated · class: not stated · holds: projecting species distribution models · src: mesgaranHereBeDragons2014 · trail: C-COVDIST §The named · from: C-COVDIST:B-0021, C-COVDIST:R-0024
- **envelope-metrics.4** ExDet captures both range novelty (NT1) and correlation-structure novelty (NT2), guarding against the "point inside every marginal range but in a never-seen combination" case, the canonical Type-2 failure that MESS and bounding boxes miss.
  conf: not stated · class: not stated · holds: ExDet · src: mesgaranHereBeDragons2014 · trail: C-COVDIST §The named · from: C-COVDIST:B-0021..0023
- **envelope-metrics.5** In Mesgaran et al.'s own analysis of Acacia cyclops, "more than half of the points (6617 of 10,785) from the global projection space that were found to lie within the univariate range of reference data exhibited distorted correlations."
  conf: not stated · class: not stated · holds: Acacia cyclops, global projection space · src: mesgaranHereBeDragons2014 · trail: C-COVDIST §The named · from: C-COVDIST:B-0024
- **envelope-metrics.6** Mahalanobis distance to the centroid is the covariance-scaled distance from a point to the training mean: equivalently the standardized distance generalised to correlated multivariate data, and the term in the exponent of the multivariate normal density.
  conf: not stated · class: not stated · holds: multivariate covariate spaces · src: none (the note cites no source for it) · trail: C-COVDIST §The named · from: C-COVDIST:B-0025
- **envelope-metrics.7** Mahalanobis distance to the centroid captures position relative to the overall (ellipsoidal) training cloud, accounting for variance and correlation, and guards against outlier/combination novelty under an assumption of a (roughly) elliptical training distribution.
  conf: not stated · class: not stated · holds: (roughly) elliptical training distributions · src: none (the note cites no source for it) · trail: C-COVDIST §The named · from: C-COVDIST:B-0025..0027
- **envelope-metrics.8** Mahalanobis distance is used directly for ecological niche modelling; sample mean/covariance, minimum covariance determinant and minimum volume ellipsoid are the three common ways to parameterise its location/scatter.
  conf: not stated · class: not stated · holds: ecological niche modelling · src: none (the note cites no source for it) · trail: C-COVDIST §The named · from: C-COVDIST:B-0025, C-COVDIST:B-0028
- **envelope-metrics.9** In QSAR, the leverage (diagonal of the hat matrix X(XᵀX)⁻¹Xᵀ) measures a compound's distance from the descriptor-space centroid in the model's metric; the Williams plot displays standardized residuals against leverage, with a warning threshold h* (commonly 3p/n).
  conf: not stated · class: not stated · holds: QSAR applicability-domain (AD) methods · src: none (the note cites no source for it) · trail: C-COVDIST §The named · from: C-COVDIST:B-0029
- **envelope-metrics.10** Bounding box and convex hull define the interpolation region geometrically; they are pure coverage constructs, while leverage is a centroid/envelope construct, monotone in Mahalanobis distance to the descriptor centroid. All guard against structural extrapolation beyond the descriptor space spanned by the training set.
  conf: not stated · class: not stated · holds: QSAR descriptor space · src: none (the note cites no source for it) · trail: C-COVDIST §The named · from: C-COVDIST:B-0029..0032
- **envelope-metrics.11** Correlation-awareness of the envelope and centroid constructions: MESS no; ExDet NT1 no; ExDet NT2 yes; Mahalanobis-to-centroid yes; leverage / hat values yes (in the model metric); bounding box no, convex hull partially.
  conf: not stated · class: not stated · holds: the review's assignment table · src: elithArtModellingRangeshifting2010, mesgaranHereBeDragons2014 · trail: C-COVDIST §The near · from: C-COVDIST:B-0037, C-COVDIST:B-0043..0048

### density-novelty: density-ratio and one-class novelty constructions
needs: none

- **density-novelty.bg1** Covariate shift is the situation in which training and test input points follow different distributions while the conditional distribution of output values given the inputs is unchanged.
  kind: background · ref: sugiyamaCovariateShiftAdaptation2007 · check: the JMLR page (jmlr.org/papers/v8/sugiyama07a.html) resolves (Sugiyama, Krauledat and Müller 2007, JMLR 8:985-1005); stated in the abstract
- **density-novelty.1** Weighted conformal prediction (Tibshirani, Barber, Candès & Ramdas) reweights nonconformity scores by the train→test covariate likelihood ratio w(x)=dP̃_X/dP_X to retain finite-sample coverage under covariate shift.
  conf: not stated · class: not stated · holds: covariate shift · src: tibshiraniConformalPredictionCovariate2019 · trail: C-COVDIST §The named · from: C-COVDIST:B-0033
- **density-novelty.2** Weighted conformal prediction is not a "distance" but a density-ratio construction: it answers "how much rarer/commoner is this covariate value in training than in deployment?"
  conf: not stated · class: not stated · holds: weighted conformal prediction · src: tibshiraniConformalPredictionCovariate2019 · trail: C-COVDIST §The named · from: C-COVDIST:B-0033..0034
- **density-novelty.3** Kernel density, one-class SVM, isolation forest and local outlier factor are used as covariate-space novelty detectors; in deep learning, Mahalanobis distance to class-conditional feature means is a standard post-hoc OOD score.
  conf: not stated · class: not stated · holds: covariate-space novelty detection; deep-learning OOD scoring · src: none (the note cites no source for it) · trail: C-COVDIST §The named · from: C-COVDIST:B-0035
- **density-novelty.4** These detectors capture density/typicality rather than raw distance: LOF and isolation forest capture local density, kernel density and one-class SVM capture global support (correlation-awareness varies).
  conf: not stated · class: not stated · holds: one-class and density-based novelty detectors · src: none (the note cites no source for it) · trail: C-COVDIST §The named, §The near · from: C-COVDIST:B-0036..0037, C-COVDIST:B-0049

### distance-modes: near-neighbour against envelope/centroid
needs: near-neighbour-metrics, envelope-metrics, density-novelty

- **distance-modes.1** The dominant constructions split cleanly into two modes: near-neighbour (is there a close training analogue?) and envelope/centroid (is the point outside overall coverage of the training cloud?).
  conf: not stated · class: not stated · holds: OOD judgement in continuous covariate space · src: none (the reviewer's synthesis) · trail: C-COVDIST §TL;DR · from: C-COVDIST:A-001
- **distance-modes.2** Every named construction can be assigned to a near-neighbour/local mode (distance to the closest training point: AOA's Dissimilarity Index, Shape, MOP, NNDM, k-nearest-neighbour AD, local outlier factor) or an envelope/centroid/global mode (distance to the training centroid or coverage boundary: MESS, ExDet's NT1/NT2, Mahalanobis-to-centroid, leverage/hat values, bounding box, convex hull); some tools combine both.
  conf: not stated · class: not stated · holds: the constructions the review names · src: none (the reviewer's synthesis) · trail: C-COVDIST §Key Findings, §The near · from: C-COVDIST:A-004..0005, C-COVDIST:B-0037..0049
- **distance-modes.3** The dichotomy is explicit in the SDM benchmarking literature: MESS and ExDet reference the training centroid and a rectilinear envelope, so their lowest extrapolation values sit near the centroid, "a poor reflection of the real environmental distance", whereas AOA and Shape reference each training point, following the cloud's shape.
  conf: not stated · class: not stated · holds: species distribution modelling benchmarks · src: none (the note names the SDM benchmarking literature without a citation for this sentence) · trail: C-COVDIST §The near · from: C-COVDIST:B-0050
- **distance-modes.4** Different constructions guard against different failure modes (univariate range exceedance vs. novel covariate combinations vs. local data sparsity), and several validation studies explicitly recommend reporting multiple complementary metrics rather than trusting one.
  conf: not stated · class: not stated · holds: validation studies the review surveyed · src: none (the note names no study for it) · trail: C-COVDIST §TL;DR · from: C-COVDIST:A-003

### correlation-handling: correlation and combinational novelty
needs: envelope-metrics, near-neighbour-metrics

- **correlation-handling.1** Inter-variable correlation is the dividing line between "Type-1" (marginal-range) novelty detectors and "Type-2" (combinational) detectors: Mahalanobis-based methods and PCA/whitening explicitly account for correlation, whereas MESS and bounding-box methods do not.
  conf: not stated · class: not stated · holds: novelty detectors in covariate space · src: none (the reviewer's synthesis) · trail: C-COVDIST §Key Findings · from: C-COVDIST:A-007
- **correlation-handling.2** Methods that ignore correlation (MESS, NT1, bounding box, Euclidean kNN on standardized variables) detect only marginal-range novelty; methods that incorporate the covariance matrix (Mahalanobis, ExDet NT2, Shape, leverage, PCA/whitening) can detect combinational novelty, a point inside every marginal range but in a never-observed combination.
  conf: not stated · class: not stated · holds: the methods the review names · src: none (the reviewer's synthesis) · trail: C-COVDIST §Standardisation · from: C-COVDIST:B-0056..0057
- **correlation-handling.3** ExDet was explicitly built to add NT2 (correlation-change novelty) on top of MESS-style NT1.
  conf: not stated · class: not stated · holds: ExDet · src: mesgaranHereBeDragons2014 · trail: C-COVDIST §Standardisation · from: C-COVDIST:B-0021, C-COVDIST:B-0058
- **correlation-handling.4** The choice of how to estimate the covariance/location (sample, minimum covariance determinant, minimum volume ellipsoid) materially affects results, especially with small samples, error and bias.
  conf: not stated · class: not stated · holds: covariance-based methods, especially with small samples · src: none (the note cites no source for it) · trail: C-COVDIST §Standardisation · from: C-COVDIST:B-0059
- **correlation-handling.5** Novel combinations of in-range covariates are common with correlated predictors, the typical situation with genomic/environmental features.
  conf: not stated · class: not stated · holds: genomic/environmental features · src: none (the reviewer's statement) · trail: C-COVDIST §Recommendations · from: C-COVDIST:B-0082

### spatial-cv: distance-based spatial cross-validation
needs: near-neighbour-metrics

- **spatial-cv.1** A related literature treats the geographic/feature distance between folds as a surrogate for prediction difficulty: Roberts et al. (2017) argued for blocking to reduce optimistic bias.
  conf: not stated · class: not stated · holds: spatial cross-validation · src: robertsCrossvalidationStrategiesData2016 · trail: C-COVDIST §Spatial · from: C-COVDIST:B-0072..0073
- **spatial-cv.2** Milà et al. (2022) proposed Nearest-Neighbour Distance Matching (NNDM) LOO-CV, matching the test-to-train nearest-neighbour distance distribution to the prediction-to-train distribution, and Linnenbrink et al. (2024) extended this to k-fold (kNNDM).
  conf: not stated · class: not stated · holds: map validation · src: milaNearestNeighbourDistance2022, linnenbrinkKNNDMCVKfold2024 · trail: C-COVDIST §Spatial · from: C-COVDIST:B-0073, C-COVDIST:R-0034
- **spatial-cv.3** Whether spatial cross-validation is the right way to evaluate map accuracy is disputed: Wadoux et al. (2021) countered that "spatial cross-validation is not the right way to evaluate map accuracy" when sampling is sound, and there is active disagreement about the right construction.
  conf: cont (note: "active disagreement") · class: not stated · holds: map accuracy evaluation when sampling is sound · src: wadouxSpatialCrossvalidationNot2021, robertsCrossvalidationStrategiesData2016, milaNearestNeighbourDistance2022 · trail: C-COVDIST §Spatial · contrary: not stated · from: C-COVDIST:B-0073..0075
- **spatial-cv.4** In this field the distribution of nearest-neighbour distances between deployment points and training data is treated as the operative quantity.
  conf: not stated · class: not stated · holds: spatial cross-validation literature · src: milaNearestNeighbourDistance2022, linnenbrinkKNNDMCVKfold2024 · trail: C-COVDIST §Spatial · from: C-COVDIST:B-0073, C-COVDIST:B-0075

### conformal-shift: conformal prediction under covariate shift
needs: density-novelty

- **conformal-shift.1** Weighted conformal prediction (Tibshirani, Barber, Candès & Ramdas, 2019) provides finite-sample coverage under covariate shift via the covariate likelihood ratio, sidestepping the need for a single "distance threshold".
  conf: not stated · class: not stated · holds: covariate shift · src: tibshiraniConformalPredictionCovariate2019 · trail: C-COVDIST §Conformal · from: C-COVDIST:B-0076
- **conformal-shift.2** Barber et al. (2023) generalised conformal prediction to non-exchangeable data (NexCP) with fixed weights; localized conformal prediction and randomly-localized variants add local adaptivity; recent extensions include conformal predictive systems under covariate shift (2024) and robustness to general distribution shift (for example Wasserstein-regularised and Lévy–Prokhorov approaches, 2025).
  conf: not stated · class: not stated · holds: non-exchangeable data and general distribution shift · src: barberConformalPredictionBeyond2023 · trail: C-COVDIST §Conformal · from: C-COVDIST:B-0077
- **conformal-shift.3** The conformal framing reframes "OOD" as density ratio rather than distance, and it does not resolve into a single covariate-space metric either; conformal/density-ratio methods require estimating the likelihood ratio and still do not produce a single universal distance threshold.
  conf: not stated · class: not stated · holds: conformal and density-ratio methods under covariate shift · src: tibshiraniConformalPredictionCovariate2019, barberConformalPredictionBeyond2023 · trail: C-COVDIST §Conformal, §Recommendations · from: C-COVDIST:B-0076..0078, C-COVDIST:B-0089
- **conformal-shift.4** The conformal-under-covariate-shift literature is moving fast (2022–2026); the newest robustness extensions are largely theoretical/empirical-on-benchmarks, and their performance on real ecological/genomic covariate spaces is not yet well established.
  conf: not stated · class: not stated · holds: real ecological/genomic covariate spaces · src: none (the note cites no source for it) · trail: C-COVDIST §Caveats · rating: "not yet well established" · from: C-COVDIST:B-0093

### transfer-error: whether any metric predicts transfer error
needs: distance-modes, correlation-handling

- **transfer-error.1** No single distance/novelty metric reliably predicts observed transfer error: benchmarks in species distribution modelling, digital soil mapping, QSAR and machine-learning OOD detection independently report that metric performance depends on dataset, model and failure mode, and that metric–error correlation is sometimes weak or near-zero. The review calls this its strongest empirical finding, and these four independent "no single metric dominates" results the core of the review; the decisive empirical evidence is negative.
  conf: repl (note: "These four independent") · class: not stated · holds: four fields (SDM, DSM, QSAR, ML OOD detection); point-level transfer error across datasets and models · src: velazcoHowFarCan2024, hateffardEvaluatingExtrapolationPotential2023, toplakAssessmentMachineLearning2014, yangOpenOODBenchmarkingGeneralized2022 · trail: C-COVDIST §TL;DR, §Key Findings, §Does any, §Recommendations · contrary: not stated · from: C-COVDIST:A-002, C-COVDIST:A-008..009, C-COVDIST:B-0060, C-COVDIST:B-0079
- **transfer-error.2** The "no single metric dominates" conclusion is robust across fields, but is itself partly a function of how each benchmark defines "success" (RMSE improvement, AUROC, correlation with error); a metric weak on one criterion may be useful on another.
  conf: not stated · class: not stated · holds: the four benchmarks' success criteria · src: none (the reviewer's caveat) · trail: C-COVDIST §Caveats · from: C-COVDIST:B-0092
- **transfer-error.3** Velazco et al. (Ecography 2024) used "760 virtual species to define different modeling conditions determined by species niche tolerance, distribution equilibrium condition, sample size, and algorithm," across six algorithms (generalized additive model, generalized linear model, Gaussian process, maximum entropy/Maxent, random forest and support vector machine), comparing Shape against MESS, EO, MOP, ExDet and AOA by the RMSE improvement (over n = 584,521 worldwide cells) from truncating predictions in non-analogue space.
  conf: not stated · class: model (note: "760 virtual species") · holds: virtual species (controlled-condition findings that may not capture real biotic interactions, measurement error or sampling bias); six SDM algorithms; 584,521 worldwide cells · src: velazcoHowFarCan2024 · trail: C-COVDIST §Does any, §Caveats · from: C-COVDIST:B-0061, C-COVDIST:B-0090
- **transfer-error.4** In Velazco et al.'s benchmark, improvement from truncation was substantial but largely independent of which extrapolation metric was used; AOA performed similarly to or worse than MESS/EO/MOP/ExDet; Shape's edge came entirely from its tunable threshold, with optimal thresholds depending on species niche breadth.
  conf: not stated · class: model (note: "760-virtual-species SDM benchmark") · holds: 760 virtual species, six algorithms · src: velazcoHowFarCan2024 · trail: C-COVDIST §Does any, §Key Findings · from: C-COVDIST:A-008, C-COVDIST:B-0061..0062
- **transfer-error.5** In Velazco et al.'s benchmark no conventional metric dominated, and all algorithms "had trouble predicting species niches."
  conf: not stated · class: model (note: "760 virtual species") · holds: 760 virtual species, six algorithms · src: velazcoHowFarCan2024 · trail: C-COVDIST §Does any · from: C-COVDIST:B-0061, C-COVDIST:B-0063
- **transfer-error.6** Hateffard, Steinbuch & Heuvelink (Geoderma 2024) compared four similarity/extrapolation measures (soil-type similarity, homosoil, AOA's DI, and quantile-regression-forest interval width) against validation RMSE and model efficiency coefficient (MEC), and reported that "weak correlation was found between the AOA dissimilarity index and DSM prediction accuracy."
  conf: not stated · class: not stated · holds: random forest digital soil mapping in four African countries · src: hateffardEvaluatingExtrapolationPotential2023 · trail: C-COVDIST §Does any · from: C-COVDIST:B-0064, C-COVDIST:R-0015
- **transfer-error.7** Hateffard et al. concluded: "none of the measures had a strong correlation with the validation metrics. This was particularly disappointing for AOA and QRF… homosoil and soil type methods had the strongest correlation with validation metrics."
  conf: not stated · class: not stated · holds: digital soil mapping in four African countries · src: hateffardEvaluatingExtrapolationPotential2023 · trail: C-COVDIST §Does any · from: C-COVDIST:B-0064..0065
- **transfer-error.8** Hateffard et al.'s result directly contradicts the premise that the AOA's DI indicates prediction quality in new environments.
  conf: not stated · class: not stated · holds: digital soil mapping in four African countries · src: hateffardEvaluatingExtrapolationPotential2023 · trail: C-COVDIST §Does any · contrary: not stated · from: C-COVDIST:B-0064, C-COVDIST:B-0066
- **transfer-error.9** Toplak et al. (J Chem Inf Model 2014), across "20 public QSAR data sets with continuous response," assessed "10 reliability scoring methods" by their correlation with prediction error: error-estimation methods could outperform pure similarity-to-training scores, but "the quality of reliability scoring methods is sensitive to data set characteristics and to the regression method used in QSAR", that is, there is no universally best applicability-domain (AD) method.
  conf: not stated · class: not stated · holds: 20 public QSAR data sets with continuous response; 10 reliability scoring methods · src: toplakAssessmentMachineLearning2014 · trail: C-COVDIST §Does any, §Key Findings · from: C-COVDIST:A-008, C-COVDIST:B-0067, C-COVDIST:R-0046
- **transfer-error.10** Later QSPR benchmarks and reviews reach the same conclusion, that no single AD algorithm is universally accepted.
  conf: not stated · class: not stated · holds: QSPR benchmarks and reviews · src: none (the note names later QSPR benchmarks and reviews without references) · trail: C-COVDIST §Does any · from: C-COVDIST:B-0068
- **transfer-error.11** OpenOOD (Yang et al., NeurIPS 2022; v1.5, 2023/2024), benchmarking 40 methods across multiple test environments, reports that "there is no single method that consistently outperforms others across benchmarks, and the ranking can be quite different from one data set to another," with rankings differing between near-OOD and far-OOD regimes: different metrics capture different failure modes.
  conf: not stated · class: not stated · holds: machine-learning OOD detection; 40 methods; near-OOD and far-OOD regimes · src: yangOpenOODBenchmarkingGeneralized2022 · trail: C-COVDIST §Does any · from: C-COVDIST:B-0069
- **transfer-error.12** In OpenOOD, Mahalanobis-distance scoring is strong on far-OOD but weaker on near-OOD, and its performance is sensitive to feature normalisation.
  conf: not stated · class: not stated · holds: machine-learning OOD detection · src: yangOpenOODBenchmarkingGeneralized2022 · trail: C-COVDIST §Does any · from: C-COVDIST:B-0069..0070
- **transfer-error.13** Distance in predictor space often correlates with error on average (Meyer & Pebesma's simulations; the broad cross-validation literature noting "increasing distance in predictor space often correlates with increasing error"), but this average relationship does not translate into a reliable point-level predictor of error in real case studies, and the strength of the relationship varies by dataset and model.
  conf: not stated · class: not stated · holds: average relationships, several from simulation studies (Meyer & Pebesma's virtual catalogue; Velazco et al.'s virtual species), to be read as controlled-condition findings; real case studies at point level · src: meyerPredictingUnknownSpace2020 · trail: C-COVDIST §Does any, §Caveats · from: C-COVDIST:B-0071, C-COVDIST:B-0090

### ood-standard: a standard for out-of-distribution status
needs: transfer-error, distance-modes, conformal-shift, spatial-cv

- **ood-standard.1** There is no settled, single standard for judging out-of-distribution (OOD) status in continuous covariate space; practice is irreducibly plural.
  conf: not stated · class: not stated · holds: OOD judgement in continuous covariate space, across the four surveyed fields · src: none (the reviewer's synthesis) · trail: C-COVDIST §TL;DR · contrary: not stated · from: C-COVDIST:A-001..002
- **ood-standard.2** The QSAR and ecology literatures use different vocabularies ("applicability domain", "extrapolation", "novelty", "area of applicability", "OOD") for overlapping constructions; apparent disagreements sometimes reflect terminology rather than substance.
  conf: not stated · class: not stated · holds: QSAR and ecology literatures · src: none (the reviewer's caveat) · trail: C-COVDIST §Caveats · from: C-COVDIST:B-0091

## Do not say

- **dns.1** "The AOA dissimilarity index indicates prediction quality in new environments."
  why: Hateffard et al. found only weak correlation between the AOA dissimilarity index and digital soil mapping prediction accuracy, which the note says directly contradicts this premise. · instead: transfer-error.6, transfer-error.8 · trail: C-COVDIST §Does any · from: C-COVDIST:B-0064, C-COVDIST:B-0066
- **dns.2** "A test point's distance from the training data in predictor space predicts its prediction error."
  why: The note says distance often correlates with error on average, but that this average relationship does not translate into a reliable point-level predictor of error in real case studies, and that its strength varies by dataset and model. · instead: transfer-error.13, transfer-error.1 · trail: C-COVDIST §Does any · from: C-COVDIST:B-0071
- **dns.3** "Meyer & Pebesma's and Velazco et al.'s results show how distance metrics track error in real species and soil data."
  why: The note says these average-relationship results come from simulation studies (a virtual catalogue, virtual species) that may not capture real biotic interactions, measurement error or sampling bias, so they should be read as controlled-condition findings. · instead: near-neighbour-metrics.4, transfer-error.3 · trail: C-COVDIST §Caveats · from: C-COVDIST:B-0090
- **dns.4** "Since no single metric dominates, distance metrics are no use for judging transfer."
  why: The note says the "no single metric dominates" conclusion is partly a function of how each benchmark defines success, and that a metric weak on one criterion may be useful on another. · instead: transfer-error.2 · trail: C-COVDIST §Caveats · from: C-COVDIST:B-0092
- **dns.5** "Spatial cross-validation is the right way to evaluate map accuracy."
  why: The note reports that Wadoux et al. (2021) countered this when sampling is sound, and that the debate is unsettled. · instead: spatial-cv.3 · trail: C-COVDIST §Spatial · from: C-COVDIST:B-0074

## Gaps

- **gap.1** The findings were never checked by a second reader: the note has no critique. Its answers rest on the four benchmarks: Velazco et al.'s 760 virtual species, Hateffard et al.'s digital soil mapping comparison, Toplak et al.'s 20 QSAR data sets, and OpenOOD's 40 methods.
  blocks: transfer-error, ood-standard · origin: no critique in the input, so no second reader checked it · search: not stated · from: C-COVDIST:A-002, C-COVDIST:A-008, C-COVDIST:B-0079
- **gap.2** The note contradicts itself on the strength of Hateffard et al.'s AOA result: its Key Findings say the study found "almost no correlation" and its Recommendations "the near-zero AOA–RMSE relationship", while the study as quoted in the body reports that "weak correlation was found between the AOA dissimilarity index and DSM prediction accuracy".
  blocks: transfer-error · origin: the note's summaries and its quotation of the study disagree · search: not stated · src: hateffardEvaluatingExtrapolationPotential2023 · from: C-COVDIST:A-008, C-COVDIST:B-0064, C-COVDIST:B-0088
- **gap.3** How the newest conformal robustness extensions perform on real ecological/genomic covariate spaces is not yet well established.
  blocks: conformal-shift · origin: the note's caveat · search: not stated · from: C-COVDIST:B-0093
- **gap.4** Several works the text relies on have no reference entry: the later QSPR benchmarks and reviews, the broad cross-validation literature quoted on distance and error, localized and randomly-localized conformal prediction, conformal predictive systems under covariate shift (2024), the Wasserstein-regularised and Lévy–Prokhorov approaches (2025), OpenOOD v1.5, the EO metric compared by Velazco et al., and the sources for the leverage, Mahalanobis and one-class constructions.
  blocks: transfer-error, conformal-shift, envelope-metrics, density-novelty · origin: references missing in the note · search: not stated · from: C-COVDIST:B-0025, C-COVDIST:B-0029, C-COVDIST:B-0035, C-COVDIST:B-0061, C-COVDIST:B-0068..0069, C-COVDIST:B-0071, C-COVDIST:B-0077

## Out of scope

## Sources

```bibtex
@inproceedings{anthonyUseMahalanobisDistance2023,
  author = {Anthony, Harry and Kamnitsas, Konstantinos},
  title = {On the use of Mahalanobis distance for out-of-distribution detection with neural networks for medical imaging},
  booktitle = {Uncertainty for Safe Utilization of Machine Learning in Medical Imaging (UNSURE 2023)},
  series = {Lecture Notes in Computer Science},
  volume = {14291},
  publisher = {Springer, Cham},
  year = {2023},
  doi = {10.1007/978-3-031-44336-7_14},
  note = {access: not stated; not cited: listed, never cited by name in the text}
}
@article{barberConformalPredictionBeyond2023,
  author = {Barber, Rina Foygel and Cand{\`e}s, Emmanuel J. and Ramdas, Aaditya and Tibshirani, Ryan J.},
  title = {Conformal prediction beyond exchangeability},
  journal = {The Annals of Statistics},
  year = {2023},
  volume = {51},
  number = {2},
  pages = {816--845},
  doi = {10.1214/23-AOS2276},
  note = {access: not stated}
}
@article{bouchetDsmextraExtrapolationAssessment2020,
  author = {Bouchet, Phil J. and Miller, David L. and Roberts, Jason J. and Mannocci, Laura and Harris, Catriona M. and Thomas, Len},
  title = {dsmextra: Extrapolation assessment tools for density surface models},
  journal = {Methods in Ecology and Evolution},
  year = {2020},
  volume = {11},
  number = {11},
  pages = {1464--1469},
  doi = {10.1111/2041-210X.13469},
  note = {access: not stated; not cited: listed, never cited by name in the text}
}
@article{elithArtModellingRangeshifting2010,
  author = {Elith, Jane and Kearney, Michael and Phillips, Steven},
  title = {The art of modelling range-shifting species},
  journal = {Methods in Ecology and Evolution},
  year = {2010},
  volume = {1},
  number = {4},
  pages = {330--342},
  doi = {10.1111/j.2041-210X.2010.00036.x},
  note = {access: not stated}
}
@article{hateffardEvaluatingExtrapolationPotential2023,
  author = {Hateffard, Fatemeh and Steinbuch, Luc and Heuvelink, Gerard B. M.},
  title = {Evaluating the extrapolation potential of random forest digital soil mapping},
  journal = {Geoderma},
  year = {2024},
  volume = {441},
  pages = {116740},
  doi = {10.1016/j.geoderma.2023.116740},
  note = {access: not stated; key kept from the refs bibliography}
}
@article{linnenbrinkKNNDMCVKfold2024,
  author = {Linnenbrink, Jan and Mil{\`a}, Carles and Ludwig, Marvin and Meyer, Hanna},
  title = {kNNDM CV: k-fold nearest-neighbour distance matching cross-validation for map accuracy estimation},
  journal = {Geoscientific Model Development},
  year = {2024},
  volume = {17},
  number = {13},
  pages = {5897--5912},
  doi = {10.5194/gmd-17-5897-2024},
  note = {access: not stated}
}
@article{ludwigAssessingImprovingTransferability2023,
  author = {Ludwig, Marvin and Moreno-Martinez, Alvaro and H{\"o}lzel, Norbert and Pebesma, Edzer and Meyer, Hanna},
  title = {Assessing and improving the transferability of current global spatial prediction models},
  journal = {Global Ecology and Biogeography},
  year = {2023},
  volume = {32},
  number = {3},
  pages = {356--368},
  doi = {10.1111/geb.13635},
  note = {access: not stated; not cited: listed, never cited by name in the text}
}
@article{mesgaranHereBeDragons2014,
  author = {Mesgaran, Mohsen B. and Cousens, Roger D. and Webber, Bruce L.},
  title = {Here be dragons: a tool for quantifying novelty due to covariate range and correlation change when projecting species distribution models},
  journal = {Diversity and Distributions},
  year = {2014},
  volume = {20},
  number = {10},
  pages = {1147--1159},
  doi = {10.1111/ddi.12209},
  note = {access: not stated}
}
@article{meyerPredictingUnknownSpace2020,
  author = {Meyer, Hanna and Pebesma, Edzer},
  title = {Predicting into unknown space? Estimating the area of applicability of spatial prediction models},
  journal = {Methods in Ecology and Evolution},
  year = {2021},
  volume = {12},
  number = {9},
  pages = {1620--1633},
  doi = {10.1111/2041-210X.13650},
  note = {access: not stated; key kept from the refs bibliography}
}
@article{meyerMachineLearningbasedGlobal2022,
  author = {Meyer, Hanna and Pebesma, Edzer},
  title = {Machine learning-based global maps of ecological variables and the challenge of assessing them},
  journal = {Nature Communications},
  year = {2022},
  volume = {13},
  pages = {2208},
  doi = {10.1038/s41467-022-29838-9},
  note = {access: not stated; not cited: listed, never cited with its year in the text}
}
@article{milaNearestNeighbourDistance2022,
  author = {Mil{\`a}, Carles and Mateu, Jorge and Pebesma, Edzer and Meyer, Hanna},
  title = {Nearest neighbour distance matching leave-one-out cross-validation for map validation},
  journal = {Methods in Ecology and Evolution},
  year = {2022},
  volume = {13},
  number = {6},
  pages = {1304--1316},
  doi = {10.1111/2041-210X.13851},
  note = {access: not stated}
}
@article{owensConstraintsInterpretationEcological2013,
  author = {Owens, Hannah L. and Campbell, Lindsay P. and Dornak, L. Lynnette and Saupe, Erin E. and Barve, Narayani and Sober{\'o}n, Jorge and Ingenloff, Kate and Lira-Noriega, Andr{\'e}s and Hensz, Christopher M. and Myers, Corinne E. and Peterson, A. Townsend},
  title = {Constraints on interpretation of ecological niche models by limited environmental ranges on calibration areas},
  journal = {Ecological Modelling},
  year = {2013},
  volume = {263},
  pages = {10--18},
  doi = {10.1016/j.ecolmodel.2013.04.011},
  note = {access: not stated}
}
@article{robertsCrossvalidationStrategiesData2016,
  author = {Roberts, David R. and Bahn, Volker and Ciuti, Simone and Boyce, Mark S. and Elith, Jane and Guillera-Arroita, Gurutzeta and Hauenstein, Severin and Lahoz-Monfort, Jos{\'e} J. and Schr{\"o}der, Boris and Thuiller, Wilfried and Warton, David I. and Wintle, Brendan A. and Hartig, Florian and Dormann, Carsten F.},
  title = {Cross-validation strategies for data with temporal, spatial, hierarchical, or phylogenetic structure},
  journal = {Ecography},
  year = {2017},
  volume = {40},
  number = {8},
  pages = {913--929},
  doi = {10.1111/ecog.02881},
  note = {access: not stated; key kept from the refs bibliography}
}
@inproceedings{tibshiraniConformalPredictionCovariate2019,
  author = {Tibshirani, Ryan J. and Foygel Barber, Rina and Cand{\`e}s, Emmanuel J. and Ramdas, Aaditya},
  title = {Conformal prediction under covariate shift},
  booktitle = {Advances in Neural Information Processing Systems 32 (NeurIPS 2019)},
  pages = {2526--2536},
  year = {2019},
  url = {https://papers.nips.cc/paper/8522-conformal-prediction-under-covariate-shift},
  note = {access: not stated}
}
@article{toplakAssessmentMachineLearning2014,
  author = {Toplak, Marko and Mo{\v{c}}nik, Rok and Polajnar, Matija and Bosni{\'c}, Zoran and Carlsson, Lars and Hasselgren, Catrin and Dem{\v{s}}ar, Janez and Boyer, Scott and Zupan, Bla{\v{z}} and St{\aa}lring, Jonna},
  title = {Assessment of machine learning reliability methods for quantifying the applicability domain of QSAR regression models},
  journal = {Journal of Chemical Information and Modeling},
  year = {2014},
  volume = {54},
  number = {2},
  pages = {431--441},
  doi = {10.1021/ci4006595},
  note = {access: not stated}
}
@article{velazcoHowFarCan2024,
  author = {Velazco, Santiago Jos{\'e} El{\'i}as and Rose, Miranda Brooke and De Marco, Paulo, Jr. and Regan, Helen M. and Franklin, Janet},
  title = {How far can I extrapolate my species distribution model? Exploring shape, a novel method},
  journal = {Ecography},
  year = {2024},
  volume = {2024},
  number = {3},
  pages = {e06992},
  doi = {10.1111/ecog.06992},
  note = {access: not stated}
}
@article{wadouxSpatialCrossvalidationNot2021,
  author = {Wadoux, Alexandre M. J.-C. and Heuvelink, Gerard B. M. and de Bruin, Sytze and Brus, Dick J.},
  title = {Spatial cross-validation is not the right way to evaluate map accuracy},
  journal = {Ecological Modelling},
  year = {2021},
  volume = {457},
  pages = {109692},
  doi = {10.1016/j.ecolmodel.2021.109692},
  note = {access: not stated}
}
@inproceedings{yangOpenOODBenchmarkingGeneralized2022,
  author = {Yang, Jingkang and Wang, Pengyun and Zou, Dejian and Zhou, Zitang and Ding, Kunyuan and Peng, Wenxuan and Wang, Haoqi and Chen, Guangyao and Li, Bo and Sun, Yiyou and Du, Xuefeng and Zhou, Kaiyang and Zhang, Wayne and Hendrycks, Dan and Li, Yixuan and Liu, Ziwei},
  title = {OpenOOD: Benchmarking generalized out-of-distribution detection},
  booktitle = {Advances in Neural Information Processing Systems 35 (NeurIPS 2022) Datasets and Benchmarks Track},
  year = {2022},
  doi = {10.48550/arXiv.2210.07242},
  note = {access: not stated}
}
@article{sugiyamaCovariateShiftAdaptation2007,
  author = {Sugiyama, Masashi and Krauledat, Matthias and M{\"u}ller, Klaus-Robert},
  title = {Covariate Shift Adaptation by Importance Weighted Cross Validation},
  journal = {Journal of Machine Learning Research},
  year = {2007},
  volume = {8},
  pages = {985--1005},
  url = {https://jmlr.org/papers/v8/sugiyama07a.html},
  note = {background; access: abstract_only (the JMLR abstract page)}
}
```
