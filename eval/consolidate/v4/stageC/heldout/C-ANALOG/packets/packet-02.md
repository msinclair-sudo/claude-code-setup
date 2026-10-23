## soil-novelty-methods.1 (claim)

Meyer and Pebesma define the area of applicability (AOA) by a dissimilarity index, the minimum importance-weighted distance from a prediction point to the training data divided by the mean training-to-training distance, with the threshold at the outlier-removed maximum index of the training data under cross-validation; in simulations, error inside the AOA matched cross-validation error, and the AOA judges analogy on combinations of predictors.

- conf: not stated
- class: model (marker)
- holds: simulations
- src: meyerPredictingUnknownSpace2020 (AB, modelled)
- trail: C-ANALOG §2.2

From the note:

> C-ANALOG:I-0017 [2.2 Methods for detecting present-day analogues and novelty in soil space] - **Area of applicability (AOA).** Meyer and Pebesma [20, AB, modelled] define a dissimilarity index: the minimum importance-weighted distance from a prediction point to the training data, divided by the mean training-to-training distance.
>
> C-ANALOG:B-0122 [2.2 Methods for detecting present-day analogues and novelty in soil space] The threshold is the outlier-removed maximum index of the training data under cross-validation.
>
> C-ANALOG:B-0123 [2.2 Methods for detecting present-day analogues and novelty in soil space] In simulations, error inside the AOA matched cross-validation error.
>
> C-ANALOG:B-0124 [2.2 Methods for detecting present-day analogues and novelty in soil space] The AOA judges analogy on combinations of predictors.
>

## soil-novelty-methods.2 (claim)

For WoSIS soil CEC profiles, distances from global prediction locations to the nearest profile far exceed the distances between profiles, and geographic gaps do not always imply feature-space gaps.

- conf: not stated
- class: meas (marker)
- holds: global maps from WoSIS profiles
- src: meyerMachineLearningbasedGlobal2022 (FT-s, measured)
- trail: C-ANALOG §2.2

From the note:

> C-ANALOG:I-0018 [2.2 Methods for detecting present-day analogues and novelty in soil space] - **Global maps and the AOA.** Meyer and Pebesma [21, FT-s, measured] show that for WoSIS soil CEC profiles, distances from global prediction locations to the nearest profile far exceed the distances between profiles.
>
> C-ANALOG:B-0125 [2.2 Methods for detecting present-day analogues and novelty in soil space] They note that geographic gaps do not always imply feature-space gaps.
>

## soil-novelty-methods.3 (claim)

Ludwig et al. report that "reliable gap-free global predictions were not possible" even after predictor reduction; the shares outside the AOA were not obtained.

- conf: not stated
- class: not stated
- holds: current global spatial prediction models
- src: ludwigAssessingImprovingTransferability2023 (AB)
- trail: C-ANALOG §2.2, §References
- limit: access (note: "the shares outside the AOA were not obtained")

From the note:

> C-ANALOG:B-0126 [2.2 Methods for detecting present-day analogues and novelty in soil space] Ludwig et al. [22, AB] report that "reliable gap-free global predictions were not possible" even after predictor reduction; the shares outside the AOA were not obtained.
>
> C-ANALOG:R-0142 [References] Assessing and improving the transferability of current global spatial prediction models.
>

## soil-novelty-methods.4 (claim)

The HELS hypercube method checks legacy soil samples against quantile strata of covariates, so it assesses coverage stratum by stratum rather than by distance.

- conf: not stated
- class: meas (marker)
- holds: legacy soil samples for digital soil mapping
- src: carreEstimationPotentialImprovement2007 (AB, measured)
- trail: C-ANALOG §2.2, §References

From the note:

> C-ANALOG:I-0019 [2.2 Methods for detecting present-day analogues and novelty in soil space] - **Stratified coverage.** The HELS hypercube method [23, AB, measured] checks legacy soil samples against quantile strata of covariates, so it assesses coverage stratum by stratum rather than by distance.
>
> C-ANALOG:R-0145 [References] Estimation and potential improvement of the quality of legacy soil samples for digital soil mapping.
>

## soil-novelty-methods.5 (claim)

The homosoil approach searches the globe for places sharing soil-forming factors; homosoil-based extrapolation worked for Mali, but accuracy "dramatically improved" with local data, and homosoil maps beat global products for silt, sand and pH, not for clay, organic carbon or total N, so an analogue in soil-forming factors does not guarantee transferable soil relationships.

- conf: not stated
- class: meas (marker)
- holds: Mali; a bounding result; the original homosoil chapter is known only via this abstract
- src: nenkamUsingHomosoilsQuantitative2022 (AB, measured), mallavanHomosoilMethodologyQuantitative2010 (SEC)
- trail: C-ANALOG §2.2

From the note:

> C-ANALOG:B-0127 [2.2 Methods for detecting present-day analogues and novelty in soil space] - **Homosoils.** The homosoil approach searches the globe for places sharing soil-forming factors.
>
> C-ANALOG:I-0020 [2.2 Methods for detecting present-day analogues and novelty in soil space] Nenkam et al. [24, AB, measured] found that homosoil-based extrapolation worked for Mali, but accuracy "dramatically improved" with local data.
>
> C-ANALOG:B-0128 [2.2 Methods for detecting present-day analogues and novelty in soil space] Homosoil maps beat global products for silt, sand and pH, not for clay, organic carbon or total N. This is a BOUNDING result: an analogue in soil-forming factors does not guarantee transferable soil relationships.
>
> C-ANALOG:B-0129 [2.2 Methods for detecting present-day analogues and novelty in soil space] The original homosoil chapter is known only via this abstract (SEC).
>

## soil-site-coverage.1 (claim)

Guerra et al. mapped 17,186 soil biodiversity and function sampling sites against SoilGrids and CHELSA layers: soil texture and pH are well represented "with the exception of extreme ranges (e.g., pH > 7.33 or silt content <19%)", and the authors write that 'most soil-related variables are well covered'.

- conf: not stated
- class: meas (marker)
- holds: soil biodiversity and function sampling sites; present-day conditions, not changed ones
- src: guerraBlindSpotsGlobal2020 (FT-s, measured)
- trail: C-ANALOG §2.3, §critic

From the note:

> C-ANALOG:I-0021 [2.3 How well present-day sites cover soil space] Guerra et al. [25, FT-s, measured] mapped 17,186 soil biodiversity and function sampling sites against SoilGrids and CHELSA layers.
>
> C-ANALOG:B-0130 [2.3 How well present-day sites cover soil space] - Soil texture and pH are well represented "with the exception of extreme ranges (e.g., pH > 7.33 or silt content <19%)".
>
> C-ANALOG:B-0133 [2.3 How well present-day sites cover soil space] This concerns the reference set, not changed conditions.
>
> C-ANALOG:C-023 [danger: Critic: answers partly supported] Guerra et al. 2020 (full text, verified) show that soil texture and pH are well covered by present-day sampling except at the extremes, that 59.6% of climate combinations are uncovered, and that some high-altitude, low-pH, high-carbon combinations in Central and West Europe are uncovered.
>
> C-ANALOG:C-040 [danger: Critic: answers partly supported] (6) The D2 answer's 'coverage poorer for combinations than for pH or texture singly [25]' is not a like-for-like contrast in Guerra: the 59.6% figure is for climate combinations, and the authors write that 'most soil-related variables are well covered'.
>

## soil-site-coverage.2 (claim)

59.6% of global climate conditions are not covered by any study (Mahalanobis distance, chi-square 0.975 cut-off).

- conf: not stated
- class: not stated
- holds: climate variables, not soil variables
- src: guerraBlindSpotsGlobal2020
- trail: C-ANALOG §2.3, §critic

From the note:

> C-ANALOG:B-0131 [2.3 How well present-day sites cover soil space] - 59.6% of global climate conditions are not covered by any study (Mahalanobis distance, chi-square 0.975 cut-off).
>
> C-ANALOG:C-023 [danger: Critic: answers partly supported] Guerra et al. 2020 (full text, verified) show that soil texture and pH are well covered by present-day sampling except at the extremes, that 59.6% of climate combinations are uncovered, and that some high-altitude, low-pH, high-carbon combinations in Central and West Europe are uncovered.
>

## soil-site-coverage.3 (claim)

Even in well-sampled Central and West Europe, combinations of high altitude, low pH and high carbon are uncovered; this is the only soil-combination statement, it is qualitative, and it rests on Guerra 2020 alone, so the review's contrast of combined against univariate coverage is not a like-for-like soil contrast.

- conf: single (critic: C-063)
- class: not stated
- holds: Central and West Europe; present-day sampling coverage
- src: guerraBlindSpotsGlobal2020
- trail: C-ANALOG §2.3, §critic, §Adversarial

From the note:

> C-ANALOG:B-0132 [2.3 How well present-day sites cover soil space] - Even in well-sampled Central and West Europe, combinations of high altitude, low pH and high carbon are uncovered.
>
> C-ANALOG:B-0135 [2.3 How well present-day sites cover soil space] SINGLE SOURCE.
>
> C-ANALOG:C-023 [danger: Critic: answers partly supported] Guerra et al. 2020 (full text, verified) show that soil texture and pH are well covered by present-day sampling except at the extremes, that 59.6% of climate combinations are uncovered, and that some high-altitude, low-pH, high-carbon combinations in Central and West Europe are uncovered.
>
> C-ANALOG:C-024 [danger: Critic: answers partly supported] That is not a like-for-like soil univariate vs soil combination contrast, because the 59.6% figure concerns climate variables.
>
> C-ANALOG:C-063 [warning: Adversarial critique, full findings] - The D2 answer's combined-vs-univariate coverage claim rests on Guerra 2020 alone and misreads it (see merged_cases).
>
> C-ANALOG:C-098 [warning: Adversarial critique, full findings] - Guerra 2020 [25]: the review's 'combined coverage worse than univariate coverage' merges soil univariate coverage (well covered) with climate combination coverage (59.6% uncovered).
>
> C-ANALOG:C-099 [warning: Adversarial critique, full findings] The only soil-combination statement is qualitative (high altitude with low pH and high carbon in Europe).
>

## soil-site-coverage.4 (claim)

SoilGrids 2.0 uncertainty is highest where observations are sparse, especially at high latitudes.

- conf: not stated
- class: not stated
- holds: SoilGrids 2.0
- src: poggioSoilGrids202021 (AB)
- trail: C-ANALOG §2.3

From the note:

> C-ANALOG:B-0136 [2.3 How well present-day sites cover soil space] Poggio et al. [26, AB] note that SoilGrids 2.0 uncertainty is highest where observations are sparse, especially at high latitudes.
>

## soil-site-coverage.5 (claim)

205 German long-term field experiments broadly match the area shares of climatic water balance and soil quality classes of national agricultural area, with a bias toward high soil quality, and one grassland climate class (3% of grassland) has no experiment; this assesses the experiments' background conditions, not whether treated plots leave the regional range.

- conf: not stated
- class: meas (marker)
- holds: German national agricultural area
- src: grosseLongtermFieldExperiments2020 (FT-s, measured)
- trail: C-ANALOG §2.3, §Adversarial

From the note:

> C-ANALOG:I-0022 [2.3 How well present-day sites cover soil space] Grosse et al. [54, FT-s, measured] compared 205 German long-term field experiments with national agricultural area.
>
> C-ANALOG:B-0137 [2.3 How well present-day sites cover soil space] The experiments broadly match area shares of climatic water balance and soil quality classes, with a bias toward high soil quality.
>
> C-ANALOG:B-0138 [2.3 How well present-day sites cover soil space] One grassland climate class (3% of grassland) has no experiment.
>
> C-ANALOG:B-0139 [2.3 How well present-day sites cover soil space] This assesses the experiments' background conditions, not whether treated plots leave the regional range.
>
> C-ANALOG:C-079 [warning: Adversarial critique, full findings] Only Grosse 2020 (background conditions) was found.
>

## soil-analogue-uses.1 (claim)

Emde et al. predicted each German inventory site's SOC under the alternative land use from sites currently under that use, excluding sites outside the AOA (threshold 0.95) of the alternative-use training set; this is the closest operational use of the soil question found, with land-use change as the driver and national inventory sites as the reference, but the number of excluded sites appears only in a figure the search agent could not extract, so the share is unknown.

- conf: single (note: "SINGLE SOURCE")
- class: model (marker)
- holds: German agricultural and forest inventory sites
- src: emdeSiteSpecificDriversLandUse2025 (FT-s, modelled)
- trail: C-ANALOG §2.4, §critic, §answers, §3. How

From the note:

> C-ANALOG:I-0023 [2.4 Uses of present-day sites as analogues for changed soils] - **Land-use change.** Emde et al. [29, FT-s, modelled] predicted each German inventory site's SOC under the alternative land use from sites currently under that use.
>
> C-ANALOG:B-0140 [2.4 Uses of present-day sites as analogues for changed soils] They excluded sites outside the AOA (threshold 0.95) of the alternative-use training set.
>
> C-ANALOG:B-0141 [2.4 Uses of present-day sites as analogues for changed soils] This is the closest operational use of the D2 question found, with land-use change as the driver and national inventory sites as the reference.
>
> C-ANALOG:B-0142 [2.4 Uses of present-day sites as analogues for changed soils] The number of excluded sites appears only in a figure the search agent could not extract, so the share is unknown.
>
> C-ANALOG:B-0144 [2.4 Uses of present-day sites as analogues for changed soils] SINGLE SOURCE.
>
> C-ANALOG:C-021 [danger: Critic: answers partly supported] Nearest precedents: Emde et al. 2025 excluded land-use-change predictions outside the area of applicability but report the share only in a figure (search-agent full text, single source).
>
> C-ANALOG:A-054 [quote: Answers as delivered] Emde et al. 2025 excluded German inventory sites whose predictors fell outside the area of applicability of sites under the alternate land use, but the counts appear only in a figure [29, full text via search agent].
>
> C-ANALOG:A-115 [4. Answers] - an AOA exclusion of changed land-use states with no reported share [29];
>
> C-ANALOG:B-0193 [3. How the two cases relate] It has used it to judge where maps can be trusted, and in one case (land-use change [29]) to exclude changed states from prediction, but not to report how many changed states lack analogues.
>
> C-ANALOG:R-0164 [References] Site-specific drivers of land-use change effects on organic carbon in German agriculture and forest soils.
>

Not found in the cited text (where to look, not what is wrong): holds: agricultural

## soil-analogue-uses.2 (claim)

Removing Emde 2025 leaves no soil study that applies an analogue or AOA test to changed conditions.

- conf: not stated
- class: reading (note: "Single-source sensitivity")
- holds: the D2 evidence base
- src: none (the reviewer's sensitivity reading)
- trail: C-ANALOG §answers

From the note:

> C-ANALOG:A-090 [quote: Answers as delivered] *Single-source sensitivity:* The absence finding does not depend on one source.
>
> C-ANALOG:A-091 [quote: Answers as delivered] The nearest direct operational precedent rests on Emde et al. 2025 [29] alone; remove it and no soil study applies an analogue or AOA test to changed conditions.
>

Not found in the cited text (where to look, not what is wrong): holds: d2

## soil-analogue-uses.3 (claim)

The Emde authors' own conclusion concerns depth: about 30% of land-use-change-driven SOC change occurs at 30-90 cm.

- conf: not stated
- class: not stated
- holds: German soils
- src: emdeSiteSpecificDriversLandUse2025
- trail: C-ANALOG §2.4

From the note:

> C-ANALOG:B-0143 [2.4 Uses of present-day sites as analogues for changed soils] The authors' own conclusion concerns depth: about 30% of land-use-change-driven SOC change occurs at 30-90 cm.
>

Not found in the cited text (where to look, not what is wrong): holds: german; holds: soils

## soil-analogue-uses.4 (claim)

Wang et al. paired 113,013 profiles into "ambient" and "warm" 1 degree C classes matched on landform, soil type and precipitation (difference <50 mm) and estimate 6.0 +/- 1.6% loss of topsoil SOC stock per degree; pairs were sparse in tundra (<100), but no share of conditions lacking a matched analogue is reported.

- conf: not stated
- class: deriv (marker)
- holds: 113,013 global soil profiles
- src: wangGlobalSoilProfiles2022 (FT-s, derived)
- trail: C-ANALOG §2.4, §critic, §answers, §4. Answers

From the note:

> C-ANALOG:I-0024 [2.4 Uses of present-day sites as analogues for changed soils] - **Warming.** Wang et al. [30, FT-s, derived] paired 113,013 profiles into "ambient" and "warm" 1 degree C classes, matched on landform, soil type and precipitation (difference <50 mm).
>
> C-ANALOG:B-0145 [2.4 Uses of present-day sites as analogues for changed soils] They estimate 6.0 +/- 1.6% loss of topsoil SOC stock per degree.
>
> C-ANALOG:B-0146 [2.4 Uses of present-day sites as analogues for changed soils] Pairs were sparse in tundra (<100), but no share of conditions lacking a matched analogue is reported.
>
> C-ANALOG:C-022 [danger: Critic: answers partly supported] Wang et al. 2022 matched warming analogue pairs but report no share without a match.
>
> C-ANALOG:A-055 [quote: Answers as delivered] Wang et al. 2022 paired ambient with warmer soil profiles matched on landform, soil type and precipitation; they note sparse tundra pairs but give no share of conditions lacking a match [30].
>
> C-ANALOG:A-116 [4. Answers] - analogue pairing for warming with no reported share [30];
>
> C-ANALOG:R-0167 [References] Global soil profiles indicate depth-dependent soil carbon losses under a warmer climate.
>

## soil-analogue-uses.5 (claim)

The same paper compiled 85 warming experiments (261 observations) and found forest SOC change "on average neutral", against significant losses from space-for-time; the authors attribute the gap to short experiments, partial warming and the assumption of similar soil histories.

- conf: single (critic: C-027)
- class: meas (note: "measured; BOUNDING")
- holds: forests; one paper
- src: wangGlobalSoilProfiles2022
- trail: C-ANALOG §2.4, §answers, §critic

From the note:

> C-ANALOG:B-0147 [2.4 Uses of present-day sites as analogues for changed soils] The same paper compiled 85 warming experiments (261 observations) and found forest SOC change "on average neutral", against significant losses from space-for-time (measured; BOUNDING).
>
> C-ANALOG:B-0148 [2.4 Uses of present-day sites as analogues for changed soils] The authors attribute the gap to short experiments, partial warming and the assumption of similar soil histories.
>
> C-ANALOG:A-064 [quote: Answers as delivered] Space-for-time SOC loss disagrees with warming experiments, especially in forests [30].
>
> C-ANALOG:A-079 [quote: Answers as delivered] *Conflicts:* Wang et al. 2022: space-for-time analogues predict significant SOC loss in forests, while field warming experiments show on average neutral change [30].
>
> C-ANALOG:A-080 [quote: Answers as delivered] The authors attribute this to short experiments and differing soil histories.
>
> C-ANALOG:C-027 [danger: Critic: answers partly supported] Space-for-time vs experiment disagreement for forest SOC rests on Wang 2022 alone.
>

## soil-analogue-uses.6 (claim)

Heuvelink et al. predicted only modest change in Argentinian SOC from 1982 to 2017, with substantial uncertainty that they attribute to the number and distribution of calibration data.

- conf: not stated
- class: not stated
- holds: Argentina, space-time mapping
- src: heuvelinkMachineLearningSpace2020 (AB)
- trail: C-ANALOG §2.4

From the note:

> C-ANALOG:B-0149 [2.4 Uses of present-day sites as analogues for changed soils] - **Space-time mapping.** Heuvelink et al. [27, AB] predicted only modest change in Argentinian SOC from 1982 to 2017, with substantial uncertainty that they attribute to the number and distribution of calibration data.
>

Not found in the cited text (where to look, not what is wrong): holds: argentina

## soil-analogue-uses.7 (claim)

Helfenstein et al. mapped 2050 soil organic matter in the Netherlands and name "predicting future trends based on historic data" as their main limitation; neither space-time mapping study reports whether future covariates fall inside the training space.

- conf: not stated
- class: not stated
- holds: the Netherlands, space-time mapping
- src: helfensteinNatureinclusiveFutureHealthy2024 (AB), heuvelinkMachineLearningSpace2020
- trail: C-ANALOG §2.4

From the note:

> C-ANALOG:B-0150 [2.4 Uses of present-day sites as analogues for changed soils] Helfenstein et al. [28, AB] mapped 2050 soil organic matter in the Netherlands and name "predicting future trends based on historic data" as their main limitation.
>
> C-ANALOG:B-0151 [2.4 Uses of present-day sites as analogues for changed soils] Neither reports whether future covariates fall inside the training space.
>

Not found in the cited text (where to look, not what is wrong): holds: space-time

## soil-driver-magnitudes.1 (claim)

None of the driver studies compares changed values with the range of other sites: the comparisons are the reviewer's readings, per-variable (almost all pH) and indirect, and most rest on abstracts or on a summarising tool (Leff 2015).

- conf: not stated
- class: reading (note: "reviewer's readings")
- holds: liming, N addition, long-term ammonium sulphate and Chinese cropland acidification
- src: none (the reviewer's reading)
- trail: C-ANALOG §2.5, §critic, §answers, §Adversarial
- rating: "The indirect driver-specific readings are weak"
- contrary: one-sided (critic: C-097)

From the note:

> C-ANALOG:B-0152 [2.5 Driver-specific evidence on how far soil variables move, relative to cross-site ranges] None of these studies compares changed values with the range of other sites.
>
> C-ANALOG:B-0153 [2.5 Driver-specific evidence on how far soil variables move, relative to cross-site ranges] The comparisons below are the **reviewer's readings**, per-variable (almost all pH), and INDIRECT.
>
> C-ANALOG:C-025 [danger: Critic: answers partly supported] Driver-by-driver per-variable magnitudes (liming, N addition, long-term ammonium sulphate, Chinese cropland acidification) can be set against cross-site pH ranges only in the reviewer's own reading.
>
> C-ANALOG:C-026 [danger: Critic: answers partly supported] Most rest on abstracts or on a summarising tool (Leff).
>
> C-ANALOG:C-097 [warning: Adversarial critique, full findings] - D2 driver readings are treated evenly as the reviewer's reading. However, liming and N-addition evidence ('within range') is developed at length, while evidence that could put changed conditions outside the range (extreme Park Grass acidification, Geescroft pH 4.4, salinity and pollution) is thin or unsearched.
>
> C-ANALOG:A-058 [quote: Answers as delivered] Third, driver-specific magnitudes that can be set against cross-site ranges only by the reviewer, not by the authors.
>
> C-ANALOG:A-078 [quote: Answers as delivered] The indirect driver-specific readings are weak: each rests on one or two studies, is per-variable (pH), and is the reviewer's reading rather than the authors' analysis..
>

Not found in the cited text (where to look, not what is wrong): 2015

## soil-driver-magnitudes.2 (claim)

On the Hoosfield acid strip at Rothamsted, a 19th-century chalk application left a pH gradient of 4.0-8.3 within about 200 m (the abstract says 180 m).

- conf: not stated
- class: not stated
- holds: one arable field
- src: rouskSoilBacterialFungal2010 (FT-s)
- trail: C-ANALOG §2.5, §Adversarial, §References

From the note:

> C-ANALOG:B-0154 [2.5 Driver-specific evidence on how far soil variables move, relative to cross-site ranges] - **Liming (management).** On the Hoosfield acid strip at Rothamsted, a 19th-century chalk application left a pH gradient of 4.0-8.3 within about 200 m.
>
> C-ANALOG:C-050 [warning: Adversarial critique, full findings] - Rousk et al. 2010 [34]: the '88 American soils spanning pH below 3.5 to nearly 9.0' range is Rousk's citation of another study (Lauber et al. 2009), so it is SECONDARY for that range. The abstract says 180 m, not 'about 200 m'.
>
> C-ANALOG:R-0180 [References] Soil bacterial and fungal communities across a pH gradient in an arable soil.
>

Not found in the cited text (where to look, not what is wrong): holds: field

## soil-driver-magnitudes.3 (claim)

Bacterial community variation across the Hoosfield gradient matched that among 88 American soils spanning pH below 3.5 to nearly 9.0; the 88-soils range is Rousk's citation of another study (Lauber et al. 2009).

- conf: not stated
- class: meas (marker)
- holds: one field against a continental set of 88 American soils
- src: rouskSoilBacterialFungal2010 (SEC, measured; critic: C-050 was "FT-s, measured"), lauber2009
- trail: C-ANALOG §2.5, §Adversarial

From the note:

> C-ANALOG:I-0025 [2.5 Driver-specific evidence on how far soil variables move, relative to cross-site ranges] Bacterial community variation across it matched that among 88 American soils spanning pH below 3.5 to nearly 9.0 [34, FT-s, measured].
>
> C-ANALOG:C-050 [warning: Adversarial critique, full findings] - Rousk et al. 2010 [34]: the '88 American soils spanning pH below 3.5 to nearly 9.0' range is Rousk's citation of another study (Lauber et al. 2009), so it is SECONDARY for that range. The abstract says 180 m, not 'about 200 m'.
>
> C-ANALOG:B-0155 [2.5 Driver-specific evidence on how far soil variables move, relative to cross-site ranges] Reviewer's reading: a management-generated pH range at one site spans most of a continental cross-site pH range.
>

Not found in the cited text (where to look, not what is wrong): Hoosfield; holds: field

## soil-driver-magnitudes.4 (claim)

The reviewer reads the liming result as a management-generated pH range at one site that spans most of a continental cross-site pH range and sits inside it, not beyond it; the authors' conclusion concerns pH control of microbial communities, not analogues, and the reading rests on Rousk 2010.

- conf: not stated
- class: reading (note: "Reviewer's reading")
- holds: one field
- src: rouskSoilBacterialFungal2010
- trail: C-ANALOG §2.5, §answers

From the note:

> C-ANALOG:B-0155 [2.5 Driver-specific evidence on how far soil variables move, relative to cross-site ranges] Reviewer's reading: a management-generated pH range at one site spans most of a continental cross-site pH range.
>
> C-ANALOG:B-0156 [2.5 Driver-specific evidence on how far soil variables move, relative to cross-site ranges] It sits inside that range, not beyond it.
>
> C-ANALOG:B-0157 [2.5 Driver-specific evidence on how far soil variables move, relative to cross-site ranges] The authors' conclusion concerns pH control of microbial communities, not analogues.
>
> C-ANALOG:A-059 [quote: Answers as delivered] Liming: one field spans pH 4.0-8.3, most of the 3.5-9.0 range across 88 American soils [34].
>
> C-ANALOG:A-092 [quote: Answers as delivered] The reading that liming-generated pH lies within the continental cross-site range rests on Rousk et al. 2010 [34].
>

## soil-driver-magnitudes.5 (claim)

Goulding and Holland et al. describe liming as pulling pH toward agronomic targets (UK 6.5 arable, 6.0 grassland), report non-representative figures of about 40% of arable and 57% of grassland soils below target, and Holland et al. note that liming changes "all elements in soils" simultaneously, which bears on combinations, though no combination has been tested.

- conf: not stated
- class: assert (marker)
- holds: the UK
- src: gouldingSoilAcidificationImportance2016 (FT-s, asserted), hollandLimingImpactsSoils2018 (AB, asserted)
- trail: C-ANALOG §2.5, §answers

From the note:

> C-ANALOG:I-0026 [2.5 Driver-specific evidence on how far soil variables move, relative to cross-site ranges] Goulding [42, FT-s, asserted] and Holland et al. [43, AB, asserted] describe liming as pulling pH toward agronomic targets (UK 6.5 arable, 6.0 grassland).
>
> C-ANALOG:B-0158 [2.5 Driver-specific evidence on how far soil variables move, relative to cross-site ranges] They report non-representative figures of about 40% of arable and 57% of grassland soils below target.
>
> C-ANALOG:B-0159 [2.5 Driver-specific evidence on how far soil variables move, relative to cross-site ranges] Holland et al. note that liming changes "all elements in soils" simultaneously.
>
> C-ANALOG:B-0160 [2.5 Driver-specific evidence on how far soil variables move, relative to cross-site ranges] That is relevant to combinations, but no combination has been tested.
>
> C-ANALOG:A-071 [quote: Answers as delivered] Authors assert that liming and acidification change several soil variables jointly [36, 43].
>

## soil-driver-magnitudes.6 (claim)

In 25 Nutrient Network grasslands, N addition lowered pH by 0.16 units against an among-site range of 4.5-8.4, and the authors conclude the pH change was too small to drive the microbial shifts; the two figures are not in the abstract.

- conf: not stated
- class: meas (marker)
- holds: a global grassland network (Nutrient Network)
- src: leffConsistentResponsesSoil2015 (secondary, measured; critic: C-048 was "FT-s via a summarising fetch tool, measured")
- trail: C-ANALOG §2.5, §Adversarial, §answers
- limit: access (critic: C-049)

From the note:

> C-ANALOG:I-0027 [2.5 Driver-specific evidence on how far soil variables move, relative to cross-site ranges] - **N fertilisation and N addition.** In 25 Nutrient Network grasslands, N addition lowered pH by 0.16 units against an among-site range of 4.5-8.4 [33, FT-s via a summarising fetch tool, measured].
>
> C-ANALOG:B-0161 [2.5 Driver-specific evidence on how far soil variables move, relative to cross-site ranges] The authors conclude the pH change was too small to drive the microbial shifts.
>
> C-ANALOG:C-047 [warning: Adversarial critique, full findings] - Leff et al. 2015 [33] is labelled FT-s but was read through a page-summarising fetch tool.
>
> C-ANALOG:C-048 [warning: Adversarial critique, full findings] A summary is not full text; label it secondary or unverified.
>
> C-ANALOG:C-049 [warning: Adversarial critique, full findings] The -0.16 pH change and the 4.5-8.4 among-site range are not in the abstract.
>
> C-ANALOG:A-093 [quote: Answers as delivered] The reading that N-driven pH change is small against among-site range rests on Leff et al. 2015 [33], read via a summarising tool.
>
> C-ANALOG:A-060 [quote: Answers as delivered] N addition: a mean pH change of -0.16 against a 4.5-8.4 among-site range in a global grassland network [33]; a -0.26 meta-analytic mean, with no response where initial pH was 3-4 [31, 44].
>

## soil-driver-magnitudes.7 (claim)

Tian and Niu's meta-analysis of 106 studies found a mean pH change of -0.26 (-0.49 in grasslands) under N addition, a response rising with N rate above about 5 g N m-2 yr-1, and no response where initial pH was 3-4 (initial pH range 3-7.7); the last detail is not in the abstract and was unverified.

- conf: not stated
- class: meas (marker)
- holds: 106 N-addition studies
- src: tianGlobalAnalysisSoil2015 (FT-s, measured)
- trail: C-ANALOG §2.5, §answers, §Adversarial
- limit: access (critic: C-061)

From the note:

> C-ANALOG:I-0028 [2.5 Driver-specific evidence on how far soil variables move, relative to cross-site ranges] Tian and Niu's meta-analysis of 106 studies [31, FT-s, measured] found:
>
> C-ANALOG:B-0162 [2.5 Driver-specific evidence on how far soil variables move, relative to cross-site ranges] - a mean pH change of -0.26 (-0.49 in grasslands);
>
> C-ANALOG:B-0163 [2.5 Driver-specific evidence on how far soil variables move, relative to cross-site ranges] - a response rising with N rate above about 5 g N m-2 yr-1;
>
> C-ANALOG:B-0164 [2.5 Driver-specific evidence on how far soil variables move, relative to cross-site ranges] - no response where initial pH was 3-4 (initial pH range 3-7.7).
>
> C-ANALOG:A-060 [quote: Answers as delivered] N addition: a mean pH change of -0.16 against a 4.5-8.4 among-site range in a global grassland network [33]; a -0.26 meta-analytic mean, with no response where initial pH was 3-4 [31, 44].
>
> C-ANALOG:C-055 [warning: Adversarial critique, full findings] - Tian and Niu 2015 [31]: 'no response where initial pH was 3-4' is FT-s and not in the abstract. The abstract's finding that effects diminish in experiments longer than 20 years is relevant to long-term plots and was omitted.
>
> C-ANALOG:C-061 [warning: Adversarial critique, full findings] - The reviewer's reading that 'the acid end of the natural range acts as a floor' rests on Tian and Niu 2015 (the initial pH 3-4 detail is not in the abstract and was unverified) plus Lu 2014 (abstract only).
>

## soil-driver-magnitudes.8 (claim)

The Tian and Niu abstract reports that N-addition effects on soil pH diminish in experiments longer than 20 years, a finding relevant to long-term plots that the review omitted.

- conf: not stated
- class: not stated
- holds: N-addition experiments by duration
- src: tianGlobalAnalysisSoil2015 (abstract)
- trail: C-ANALOG §Adversarial

From the note:

> C-ANALOG:C-055 [warning: Adversarial critique, full findings] - Tian and Niu 2015 [31]: 'no response where initial pH was 3-4' is FT-s and not in the abstract. The abstract's finding that effects diminish in experiments longer than 20 years is relevant to long-term plots and was omitted.
>

Not found in the cited text (where to look, not what is wrong): N-addition; holds: n-addition

## soil-driver-magnitudes.9 (claim)

N addition to an already very acid tropical forest soil (pH <4.0) did not change exchangeable Al3+.

- conf: not stated
- class: meas (marker)
- holds: a tropical forest soil
- src: luNitrogenDepositionContributes2014 (AB, measured)
- trail: C-ANALOG §2.5

From the note:

> C-ANALOG:I-0029 [2.5 Driver-specific evidence on how far soil variables move, relative to cross-site ranges] Lu et al. [44, AB, measured] likewise found that N addition to an already very acid tropical forest soil (pH <4.0) did not change exchangeable Al3+.
>

## soil-driver-magnitudes.10 (claim)

The reviewer reads the acid end of the natural range as acting as a floor in the N-addition data; the reading rests on Tian and Niu 2015 (the initial pH 3-4 detail unverified) plus Lu 2014 (abstract only).

- conf: not stated
- class: reading (note: "Reviewer's reading: the acid end of the natural range acts as a floor")
- holds: N addition to acid soils
- src: tianGlobalAnalysisSoil2015, luNitrogenDepositionContributes2014
- trail: C-ANALOG §2.5, §Adversarial

From the note:

> C-ANALOG:B-0165 [2.5 Driver-specific evidence on how far soil variables move, relative to cross-site ranges] Reviewer's reading: the acid end of the natural range acts as a floor in these data.
>
> C-ANALOG:C-061 [warning: Adversarial critique, full findings] - The reviewer's reading that 'the acid end of the natural range acts as a floor' rests on Tian and Niu 2015 (the initial pH 3-4 detail is not in the abstract and was unverified) plus Lu 2014 (abstract only).
>

Not found in the cited text (where to look, not what is wrong): N-addition; holds: soils

## soil-driver-magnitudes.11 (claim)

Experimental N rates (0.93-60 g m-2 yr-1) mostly exceed the 5-35 kg ha-1 yr-1 (0.5-3.5 g m-2 yr-1) ambient deposition gradient across 68 British grasslands, so the driver itself is often applied outside the range of present-day deposition even where the resulting pH is not outside the range of present-day soils.

- conf: not stated
- class: reading (note: "A second reviewer's reading, derived from two papers")
- holds: experimental N rates against 68 British grasslands
- src: stevensImpactNitrogenDeposition2004 (AB)
- trail: C-ANALOG §2.5

From the note:

> C-ANALOG:B-0166 [2.5 Driver-specific evidence on how far soil variables move, relative to cross-site ranges] A second reviewer's reading, derived from two papers: experimental N rates (0.93-60 g m-2 yr-1) mostly exceed the 5-35 kg ha-1 yr-1 (0.5-3.5 g m-2 yr-1) ambient deposition gradient across 68 British grasslands [32, AB].
>
> C-ANALOG:B-0167 [2.5 Driver-specific evidence on how far soil variables move, relative to cross-site ranges] So the driver itself is often applied outside the range of present-day deposition, even where the resulting pH is not outside the range of present-day soils.
>

## soil-driver-magnitudes.12 (claim)

Park Grass plot pH spans about 3.3-7.4 or 3.6-7, and the plots reach pH 3.3-3.6 under long-term ammonium sulphate.

- conf: not stated
- class: not stated
- holds: the Park Grass Experiment
- src: rouskFungalBacterialGrowth2011 (AB), zhalninaSoilPHDetermines2014 (AB)
- trail: C-ANALOG §2.5, §answers

From the note:

> C-ANALOG:B-0168 [2.5 Driver-specific evidence on how far soil variables move, relative to cross-site ranges] - **Long-term ammonium sulphate and liming (Park Grass, Ukulinga, Rothamsted).**
>
> C-ANALOG:B-0169 [2.5 Driver-specific evidence on how far soil variables move, relative to cross-site ranges] - Park Grass plot pH spans about 3.3-7.4 [35, AB] or 3.6-7 [36, AB].
>
> C-ANALOG:A-061 [quote: Answers as delivered] Long-term ammonium sulphate: Park Grass plots reach pH 3.3-3.6 [35, 36].
>

Not found in the cited text (where to look, not what is wrong): holds: experiment

## soil-driver-magnitudes.13 (claim)

Ammonium sulphate also raises soil carbon and C/N at Park Grass.

- conf: not stated
- class: assert (note: "asserted in the abstract")
- holds: the Park Grass Experiment
- src: zhalninaSoilPHDetermines2014
- trail: C-ANALOG §2.5

From the note:

> C-ANALOG:B-0170 [2.5 Driver-specific evidence on how far soil variables move, relative to cross-site ranges] - Ammonium sulphate also raises soil carbon and C/N [36, asserted in the abstract].
>

Not found in the cited text (where to look, not what is wrong): Park; Grass; holds: park; holds: grass; holds: experiment

## soil-driver-magnitudes.14 (claim)

Grassland diversity recovered after N stopped, except "where there has been extreme acidification"; Crawley et al. report large pH decreases and richness from 3 to 44 species.

- conf: not stated
- class: not stated
- holds: the Park Grass Experiment
- src: storkeyGrasslandBiodiversityBounces2015 (AB), crawleyDeterminantsSpeciesRichness2005 (AB)
- trail: C-ANALOG §2.5

From the note:

> C-ANALOG:B-0171 [2.5 Driver-specific evidence on how far soil variables move, relative to cross-site ranges] - Storkey et al. [38, AB] report diversity recovery after N stopped, except "where there has been extreme acidification".
>
> C-ANALOG:B-0172 [2.5 Driver-specific evidence on how far soil variables move, relative to cross-site ranges] Crawley et al. [37, AB] report large pH decreases and richness from 3 to 44 species.
>
> C-ANALOG:B-0168 [2.5 Driver-specific evidence on how far soil variables move, relative to cross-site ranges] - **Long-term ammonium sulphate and liming (Park Grass, Ukulinga, Rothamsted).**
>

Not found in the cited text (where to look, not what is wrong): holds: experiment

## soil-driver-magnitudes.15 (claim)

Ward et al. reproduce the Park Grass pattern in a 65-year South African experiment.

- conf: not stated
- class: not stated
- holds: Ukulinga, South Africa
- src: wardAfricanGrasslandResponds2017 (AB)
- trail: C-ANALOG §2.5

From the note:

> C-ANALOG:B-0168 [2.5 Driver-specific evidence on how far soil variables move, relative to cross-site ranges] - **Long-term ammonium sulphate and liming (Park Grass, Ukulinga, Rothamsted).**
>
> C-ANALOG:B-0173 [2.5 Driver-specific evidence on how far soil variables move, relative to cross-site ranges] - Ward et al. [40, AB] reproduce the pattern in a 65-year South African experiment.
>

Not found in the cited text (where to look, not what is wrong): holds: africa

## soil-driver-magnitudes.16 (claim)

Poulton et al. report Geescroft Wilderness pH falling from 7.1 (1883) to 4.4 (1999), and manure plots raising SOC toward new equilibria over 80-100 years.

- conf: not stated
- class: not stated
- holds: Rothamsted long-term experiments
- src: poultonMajorLimitationsAchieving2018 (FT-s)
- trail: C-ANALOG §2.5

From the note:

> C-ANALOG:B-0174 [2.5 Driver-specific evidence on how far soil variables move, relative to cross-site ranges] - Poulton et al. [41, FT-s] report Geescroft Wilderness pH falling from 7.1 (1883) to 4.4 (1999), and manure plots raising SOC toward new equilibria over 80-100 years.
>
> C-ANALOG:B-0168 [2.5 Driver-specific evidence on how far soil variables move, relative to cross-site ranges] - **Long-term ammonium sulphate and liming (Park Grass, Ukulinga, Rothamsted).**
>

Not found in the cited text (where to look, not what is wrong): holds: experiments

## soil-driver-magnitudes.17 (claim)

The reviewer reads the most acidified Park Grass plots as lying near the bottom of cross-site pH ranges, and the joint shift in pH, C and C/N as a candidate route to combinations not found elsewhere; no study found tests either against a regional reference set.

- conf: not stated
- class: reading (note: "Reviewer's reading: the most acidified Park Grass plots")
- holds: the Park Grass Experiment
- src: none (the reviewer's reading)
- trail: C-ANALOG §2.5, §Adversarial
- search: not stated

From the note:

> C-ANALOG:B-0175 [2.5 Driver-specific evidence on how far soil variables move, relative to cross-site ranges] Reviewer's reading: the most acidified Park Grass plots lie near the bottom of cross-site pH ranges, and the joint shift in pH, C and C/N is a candidate route to combinations not found elsewhere.
>
> C-ANALOG:B-0176 [2.5 Driver-specific evidence on how far soil variables move, relative to cross-site ranges] No study found tests either against a regional reference set.
>
> C-ANALOG:C-113 [warning: Adversarial critique, full findings] It reports that no quantitative comparison was found, and offers only a labelled reviewer reading that the most acidified Park Grass plots lie near the bottom of cross-site pH ranges.
>

Not found in the cited text (where to look, not what is wrong): holds: experiment

## soil-driver-magnitudes.18 (claim)

Silvertown et al. state that comparisons among sites, nutrient inputs or soil acidity "may in general underestimate the threat" from long-term nutrient change.

- conf: single (note: "SINGLE SOURCE")
- class: assert (marker)
- holds: one abstract on the Park Grass Experiment, used as a bounding result
- src: silvertownParkGrassExperiment2006 (AB, asserted)
- trail: C-ANALOG §2.5, §answers, §Adversarial

From the note:

> C-ANALOG:I-0030 [2.5 Driver-specific evidence on how far soil variables move, relative to cross-site ranges] Silvertown et al. [39, AB, asserted] state that comparisons among sites, nutrient inputs or soil acidity "may in general underestimate the threat" from long-term nutrient change.
>
> C-ANALOG:B-0177 [2.5 Driver-specific evidence on how far soil variables move, relative to cross-site ranges] BOUNDING, SINGLE SOURCE.
>
> C-ANALOG:A-065 [quote: Answers as delivered] Park Grass authors assert that cross-site comparisons underestimate temporal loss [39].
>
> C-ANALOG:C-064 [warning: Adversarial critique, full findings] - Silvertown 2006's assertion that cross-site comparisons underestimate temporal change is one abstract, used as a BOUNDING result in the D2 answer.
>

Not found in the cited text (where to look, not what is wrong): holds: experiment

## soil-driver-magnitudes.19 (claim)

Chinese cropland pH fell significantly from the 1980s to the 2000s.

- conf: not stated
- class: meas (marker)
- holds: major Chinese croplands
- src: guoSignificantAcidificationMajor2010 (AB, measured)
- trail: C-ANALOG §2.5, §References

From the note:

> C-ANALOG:I-0031 [2.5 Driver-specific evidence on how far soil variables move, relative to cross-site ranges] - **National-scale acidification from fertiliser.** Chinese cropland pH fell significantly from the 1980s to the 2000s [45, AB, measured].
>
> C-ANALOG:R-0214 [References] Significant acidification in major Chinese croplands.
>

## soil-driver-magnitudes.20 (claim)

Chinese national mean cropland pH went from 7.1 (1980) to 6.6 (2018), and about a quarter of neutral soils moved into acidic classes.

- conf: not stated
- class: meas (marker)
- holds: Chinese croplands, 1980 to 2018
- src: chenNationalScaleAssessmentSoil2025 (AB, measured)
- trail: C-ANALOG §2.5, §answers

From the note:

> C-ANALOG:I-0032 [2.5 Driver-specific evidence on how far soil variables move, relative to cross-site ranges] National mean pH went from 7.1 (1980) to 6.6 (2018), and about a quarter of neutral soils moved into acidic classes [46, AB, measured].
>
> C-ANALOG:A-062 [quote: Answers as delivered] National cropland acidification: about a quarter of neutral Chinese cropland soils moved into acidic classes already present nationally [46, abstract].
>

## soil-driver-magnitudes.21 (claim)

A scenario of 1% annual growth in N input projects a further fall in Chinese cropland pH of about one unit by 2050.

- conf: not stated
- class: model (marker)
- holds: Chinese croplands
- src: zhuCroplandAcidificationIncreases2020 (AB, modelled)
- trail: C-ANALOG §2.5

From the note:

> C-ANALOG:I-0033 [2.5 Driver-specific evidence on how far soil variables move, relative to cross-site ranges] A scenario of 1% annual growth in N input projects a further fall of about one unit by 2050 [47, AB, modelled].
>
> C-ANALOG:I-0031 [2.5 Driver-specific evidence on how far soil variables move, relative to cross-site ranges] - **National-scale acidification from fertiliser.** Chinese cropland pH fell significantly from the 1980s to the 2000s [45, AB, measured].
>

## soil-driver-magnitudes.22 (claim)

The reviewer reads the Chinese change as movement between classes already occupied nationally; whether any cells left the 1980 range was not tested in the abstract, and the full text was not obtained.

- conf: not stated
- class: reading (note: "Reviewer's reading of [46]")
- holds: Chinese croplands
- src: chenNationalScaleAssessmentSoil2025 (abstract)
- trail: C-ANALOG §2.5
- limit: access (note: "the full text was not obtained")

From the note:

> C-ANALOG:B-0178 [2.5 Driver-specific evidence on how far soil variables move, relative to cross-site ranges] Reviewer's reading of [46]: the change is reported as movement between classes already occupied nationally.
>
> C-ANALOG:B-0179 [2.5 Driver-specific evidence on how far soil variables move, relative to cross-site ranges] Whether any cells left the 1980 range was not tested in the abstract, and the full text was not obtained.
>

Not found in the cited text (where to look, not what is wrong): Chinese; holds: chinese; holds: croplands

## soil-driver-magnitudes.23 (claim)

Soil pH in England and Wales rose under all land uses from 1978 to 2003, during recovery from acid deposition.

- conf: not stated
- class: not stated
- holds: the national inventory of England and Wales
- src: kirkChangesSoilPH2009 (AB)
- trail: C-ANALOG §2.5

From the note:

> C-ANALOG:B-0180 [2.5 Driver-specific evidence on how far soil variables move, relative to cross-site ranges] - **Recovery from acid deposition and liming changes (national resurveys).**
>
> C-ANALOG:B-0181 [2.5 Driver-specific evidence on how far soil variables move, relative to cross-site ranges] - Soil pH in England and Wales rose under all land uses from 1978 to 2003 [49, AB].
>

## soil-driver-magnitudes.24 (claim)

Topsoil carbon change in Great Britain is contested: the National Soil Inventory reported SOC loss of 0.6% per year, while the Countryside Survey found no net topsoil C change from 1978 to 2007 and calls the difference "unresolved".

- conf: cont (note: "contested")
- class: not stated
- holds: national resurveys of Great Britain
- src: bellamyCarbonLossesAll2005 (AB), reynoldsCountrysideSurveyNational2013 (AB)
- trail: C-ANALOG §2.5, §answers

From the note:

> C-ANALOG:B-0182 [2.5 Driver-specific evidence on how far soil variables move, relative to cross-site ranges] - The same inventory reported SOC loss of 0.6% per year [50, AB].
>
> C-ANALOG:B-0183 [2.5 Driver-specific evidence on how far soil variables move, relative to cross-site ranges] - The GB Countryside Survey found no net topsoil C change from 1978 to 2007, and calls the difference from the inventory "unresolved" [51, AB]; contested.
>
> C-ANALOG:A-081 [quote: Answers as delivered] Countryside Survey vs National Soil Inventory on GB topsoil carbon change: no net change [51] vs 0.6% per year loss [50], which the authors call unresolved.
>

Not found in the cited text (where to look, not what is wrong): Great; Britain; holds: great; holds: britain

## soil-driver-magnitudes.25 (claim)

The national resurveys report shifts in means by habitat, not shares of sites leaving the reference distribution.

- conf: not stated
- class: not stated
- holds: national resurveys
- src: kirkChangesSoilPH2009, bellamyCarbonLossesAll2005, reynoldsCountrysideSurveyNational2013
- trail: C-ANALOG §2.5

From the note:

> C-ANALOG:B-0184 [2.5 Driver-specific evidence on how far soil variables move, relative to cross-site ranges] - These resurveys report shifts in means by habitat, not shares of sites leaving the reference distribution.
>

## soil-driver-magnitudes.26 (claim)

Global soil pH shows an abrupt alkaline-to-acid transition where precipitation exceeds potential evapotranspiration, the shape of the present-day reference distribution any comparison would use.

- conf: not stated
- class: meas (marker)
- holds: global soils
- src: slessarevWaterBalanceCreates2016 (AB, measured)
- trail: C-ANALOG §2.5

From the note:

> C-ANALOG:I-0034 [2.5 Driver-specific evidence on how far soil variables move, relative to cross-site ranges] - **Background distribution.** Global soil pH shows an abrupt alkaline-to-acid transition where precipitation exceeds potential evapotranspiration [48, AB, measured].
>
> C-ANALOG:B-0185 [2.5 Driver-specific evidence on how far soil variables move, relative to cross-site ranges] This is the shape of the present-day reference distribution any comparison would use.
>

## soil-driver-magnitudes.27 (claim)

A machine-learning estimate puts P-fertilisation-driven increases in resin P at 37% and N-driven decreases at 10%, relative to unfertilised soil, not to the range across sites.

- conf: not stated
- class: model (marker)
- holds: global-scale, agricultural fertilisation against unfertilised soil
- src: qiGlobalscalePatternsBioavailable2026 (AB, modelled)
- trail: C-ANALOG §2.5, §References

From the note:

> C-ANALOG:I-0035 [2.5 Driver-specific evidence on how far soil variables move, relative to cross-site ranges] - **Phosphorus.** A machine-learning estimate puts P-fertilisation-driven increases in resin P at 37% and N-driven decreases at 10%, relative to unfertilised soil, not to the range across sites [55, AB, modelled].
>
> C-ANALOG:R-0244 [References] Global-scale patterns of bioavailable soil phosphorus driven by agricultural fertilization.
>

## soil-failure-modes.1 (claim)

Change that depends on the baseline value is partly regression to the mean; a published comment disputes aspects of the proposed correction, known only secondarily via the search agent.

- conf: cont (note: "a published comment disputes aspects")
- class: deriv (marker)
- holds: baseline-dependent change in soil monitoring
- src: larkBaselineValuesChange2006 (AB, derived)
- trail: C-ANALOG §2.6, §answers

From the note:

> C-ANALOG:I-0036 [2.6 Failure modes specific to soil] - Change that depends on the baseline value is partly regression to the mean [52, AB, derived]; a published comment disputes aspects (SEC via search agent).
>
> C-ANALOG:A-066 [quote: Answers as delivered] Baseline-dependent change carries a regression-to-the-mean artefact [52].
>
> C-ANALOG:A-082 [quote: Answers as delivered] Lark et al. 2006 propose a regression-to-the-mean correction that a published comment disputes (secondary, via the search agent).
>
> C-ANALOG:R-0235 [References] Baseline values and change in the soil, and implications for monitoring.
>

## soil-failure-modes.2 (claim)

Monitoring networks may need about 10 years to detect some large SOC changes, which bounds any attempt to place measured change against spatial variability.

- conf: not stated
- class: model (marker)
- holds: European soil-monitoring networks
- src: sabyWillEuropeanSoilmonitoring2008 (AB, modelled)
- trail: C-ANALOG §2.6, §answers, §References

From the note:

> C-ANALOG:I-0037 [2.6 Failure modes specific to soil] - Monitoring networks may need about 10 years to detect some large SOC changes [53, AB, modelled], which bounds any attempt to place measured change against spatial variability.
>
> C-ANALOG:A-067 [quote: Answers as delivered] Soil-monitoring networks need about a decade to detect large SOC changes [53].
>
> C-ANALOG:R-0238 [References] Will European soil-monitoring networks be able to detect changes in topsoil organic carbon content?
>

## soil-failure-modes.3 (claim)

Bounding results caution against inferring temporal change from spatial contrasts.

- conf: not stated
- class: not stated
- holds: Wang 2022, Silvertown 2006 and Lark 2006
- src: wangGlobalSoilProfiles2022, silvertownParkGrassExperiment2006, larkBaselineValuesChange2006
- trail: C-ANALOG §4. Answers, §answers

From the note:

> C-ANALOG:A-119 [4. Answers] Bounding results caution against inferring temporal change from spatial contrasts [30, 39, 52].
>
> C-ANALOG:A-063 [quote: Answers as delivered] Fourth, bounding results on inferring change from space.
>

Not found in the cited text (where to look, not what is wrong): holds: wang; holds: 2022; holds: silvertown; holds: 2006; holds: lark

## climate-soil-relation.1 (claim)

Two literatures answer the question very differently: the climate literature has a shared toolkit (scaled distance, a biome-calibrated or percentile threshold, an explicit candidate pool) that it has used to produce shares comparable within studies, while the soil literature has the equivalent toolkit (the AOA dissimilarity index, hypercube coverage, homosoils) and has used it to judge where maps can be trusted and, in one case (land-use change), to exclude changed states from prediction, but not to report how many changed states lack analogues.

- conf: not stated
- class: not stated
- holds: the climate and soil literatures the review covers
- src: none (the reviewer's synthesis)
- trail: C-ANALOG §3. How, §Present-day

From the note:

> C-ANALOG:B-0025 [Present-day analogues for changed climate and changed soil conditions: a literature review] Two literatures answer this question very differently.
>
> C-ANALOG:B-0026 [Present-day analogues for changed climate and changed soil conditions: a literature review] For climate, a mature modelling literature has asked many times what fraction of projected future climates has a counterpart somewhere in present-day climate space.
>
> C-ANALOG:B-0028 [Present-day analogues for changed climate and changed soil conditions: a literature review] There is a methods literature built to detect extrapolation in soil mapping, and scattered evidence on how far particular drivers move soil variables.
>
> C-ANALOG:B-0029 [Present-day analogues for changed climate and changed soil conditions: a literature review] These two cases are kept apart throughout.
>
> C-ANALOG:B-0190 [3. How the two cases relate] The climate literature has a shared toolkit: scaled distance, a biome-calibrated or percentile threshold, and an explicit candidate pool.
>
> C-ANALOG:B-0191 [3. How the two cases relate] It has used that toolkit to produce shares, and those shares can be compared within studies.
>
> C-ANALOG:B-0192 [3. How the two cases relate] The soil literature has the equivalent toolkit (the AOA dissimilarity index, hypercube coverage, homosoils).
>
> C-ANALOG:B-0193 [3. How the two cases relate] It has used it to judge where maps can be trusted, and in one case (land-use change [29]) to exclude changed states from prediction, but not to report how many changed states lack analogues.
>

Not found in the cited text (where to look, not what is wrong): holds: review

## climate-soil-relation.2 (claim)

Evidence from climate does not answer the soil question, and nor does the ocean pH result, which is seawater chemistry under a globally uniform forcing.

- conf: not stated
- class: not stated
- holds: the climate and ocean studies against the soil question
- src: lotterhosNovelDisappearingClimates2021
- trail: C-ANALOG §3. How

From the note:

> C-ANALOG:B-0194 [3. How the two cases relate] Evidence from climate does not answer the soil question.
>
> C-ANALOG:B-0195 [3. How the two cases relate] Nor does the ocean pH result [11]: it is seawater chemistry under a globally uniform forcing, and most soil drivers (liming, fertiliser) are local and imposed on already varied soils.
>

## climate-soil-relation.3 (claim)

The reviewer argues, without a source, that ocean pH evidence does not transfer because most soil drivers (liming, fertiliser) are local and imposed on already varied soils.

- conf: not stated
- class: reading (critic: C-105)
- holds: the reviewer's argument
- src: none (the reviewer's argument)
- trail: C-ANALOG §3. How, §Adversarial

From the note:

> C-ANALOG:B-0195 [3. How the two cases relate] Nor does the ocean pH result [11]: it is seawater chemistry under a globally uniform forcing, and most soil drivers (liming, fertiliser) are local and imposed on already varied soils.
>
> C-ANALOG:C-105 [warning: Adversarial critique, full findings] - Section 3 asserts, without a source, that ocean pH evidence does not transfer because 'most soil drivers (liming, fertiliser) are local and imposed on already varied soils'. This is the reviewer's argument presented in the synthesis without a label.
>

## dns.1 (do not say)

"Projected climates are novel on 67-76% of land by 2100 and on over 97% by 2300."

- why: These are unverified figures from a search agent's reading of Ordonez 2024, and its abstract gives different headline figures, over 50% of land by 2100 and over 80% by 2300, for novel ecosystems combined across three metrics.
- instead: global-climate-shares.6, global-climate-shares.7
- trail: C-ANALOG §critic, §Adversarial

From the note:

> C-ANALOG:C-035 [danger: Critic: answers partly supported] (3) Ordonez: the abstract gives >50% by 2100 and >80% by 2300 for 'novel ecosystems' combined across three metrics.
>
> C-ANALOG:C-036 [danger: Critic: answers partly supported] The review's 67-76% and >97% are unverified FT-s figures, yet they carry the headline conflict with Williams.
>
> C-ANALOG:C-044 [warning: Adversarial critique, full findings] Its abstract gives different headline figures (>50% of land by 2100 and >80% by 2300 for novel ecosystems across three combined metrics) from the review's 67-76% and >97%.
>
> C-ANALOG:A-010 [quote: Answers as delivered] (2) Horizon: 67-76% of land is novel by 2100 and over 97% by 2300 [2, full text via search agent, not re-opened]; 2.1% by 2100 vs 8.7% by 2280 with a deep-time pool [8].
>
> C-ANALOG:A-096 [4. Answers] Estimates run from 0.3-2.2% of land novel (phytoclimate space [3]) through 4-39% ([1]) to 67-76% by 2100 and >97% by 2300 ([2]).
>

Not found in the cited text (where to look, not what is wrong): "Projected climates are novel on 67-76% of land by 2100 and on over 97% by 2300."; 2024

## dns.2 (do not say)

"Ordonez et al. 2024 find roughly double Williams et al.'s share of novel climate for comparable forcing, the largest conflict in the literature."

- why: The 'roughly double Williams' conflict is not established as like for like: the Ordonez abstract figure combines three metrics and the review compares it directly with Williams' single-metric no-analogue share, and the answer states the conflict firmly on unverified access.
- instead: global-climate-shares.9, global-climate-shares.8
- trail: C-ANALOG §critic, §Adversarial, §1.2

From the note:

> C-ANALOG:C-010 [danger: Critic: answers partly supported] So the 'roughly double Williams' conflict is not established as like for like.
>
> C-ANALOG:C-045 [warning: Adversarial critique, full findings] The answer states the conflict firmly on unverified access.
>
> C-ANALOG:C-102 [warning: Adversarial critique, full findings] - The Ordonez 2024 'novel' coverage appears, from its abstract, to combine three metrics (new combinations, velocity, disaggregation) into novel-ecosystem coverage. The review compares it directly with Williams' single-metric no-analogue share.
>
> C-ANALOG:B-0054 [1.2 Global land estimates] For comparable forcing this is roughly double Williams et al.'s upper bound.
>
> C-ANALOG:A-029 [quote: Answers as delivered] *Conflicts:* The largest conflict is on the global share for comparable forcing.
>

Not found in the cited text (where to look, not what is wrong): "Ordonez et al. 2024 find roughly double Williams et al. share of novel climate for comparable forcing, the largest conflict in the literature."

## dns.3 (do not say)

"3% to 68% of land shows significant phytoclimate change by 2070."

- why: The source says 33% to 68%; the review misprints it.
- instead: global-climate-shares.11
- trail: C-ANALOG §critic, §Adversarial

From the note:

> C-ANALOG:C-032 [danger: Critic: answers partly supported] Problems found: (1) Conradi: '3% to 68%' should be 33% to 68%.
>
> C-ANALOG:C-054 [warning: Adversarial critique, full findings] - Conradi et al. 2024 [3] is marked FT-r (re-read), yet the review gives '3% to 68%' where the source says 33% to 68%.
>
> C-ANALOG:C-070 [warning: Adversarial critique, full findings] - Not a reference error, but a content error attached to [3]: the phrase '3% to 68% of land' does not match the source, which says 33% to 68%.
>
> C-ANALOG:B-0059 [1.2 Global land estimates] - 3% to 68% of land shows significant phytoclimate change by 2070.
>

## dns.4 (do not say)

"With a deep-time pool, fewer than 1.5% of locations lack an analogue under RCP4.5."

- why: The Burke 2018 abstract says under 1% for RCP4.5, and the review's full-text figures were not re-opened.
- instead: reference-domain.7
- trail: C-ANALOG §critic, §Adversarial

From the note:

> C-ANALOG:C-037 [danger: Critic: answers partly supported] (4) Burke: the abstract gives <1% for RCP4.5; the review gives <1.5%.
>
> C-ANALOG:C-052 [warning: Adversarial critique, full findings] - Burke et al. 2018 [8]: the review reports '<1.5%' for RCP4.5 and '2.1% by 2100', but the abstract says '<1%'. The FT-s figures were not re-opened.
>
> C-ANALOG:B-0072 [1.3 Reference domain and search extent] Fewer than 1.5% of locations lacked an analogue under RCP4.5.
>
> C-ANALOG:A-015 [quote: Answers as delivered] Widening the pool to Eocene through historical climates cuts novelty to <1.5-8.7% [8].
>

Not found in the cited text (where to look, not what is wrong): RCP4; "With a deep-time pool, fewer than 1.5% of locations lack an analogue under RCP4.5."

## dns.5 (do not say)

"The candidate pool is the single most consistent control on the share of novel climate."

- why: As a controlled contrast this rests on two within-study contrasts only, Williams 2007 (500 km) and Burke 2018 (deep time); the crop, county and city studies are between-study comparisons.
- instead: reference-domain.10
- trail: C-ANALOG §Adversarial, §critic

From the note:

> C-ANALOG:C-058 [warning: Adversarial critique, full findings] - Section 1.3 opener: 'The candidate pool is the single most consistent control on the share'. As a controlled contrast this rests on Williams 2007 (500 km) and Burke 2018 (deep time) only; the crop, county and city studies are between-study comparisons.
>
> C-ANALOG:C-039 [danger: Critic: answers partly supported] Those studies contain no unrestricted contrast, so the 'single most consistent control' claim rests on two within-study contrasts (Williams, Burke).
>
> C-ANALOG:B-0066 [1.3 Reference domain and search extent] The candidate pool is the single most consistent control on the share, and it acts in both directions.
>

Not found in the cited text (where to look, not what is wrong): "The candidate pool is the single most consistent control on the share of novel climate."

## dns.6 (do not say)

"Restricting the pool to a crop's own area, a national county set or a city hull raises novelty, as Pugh, Chaudhary and Bastin show."

- why: Those studies contain no unrestricted contrast, so they do not show that narrowing the pool raises novelty; the answer mixes them with within-study controlled contrasts.
- instead: reference-domain.10
- trail: C-ANALOG §critic, §Adversarial, §4. Answers

From the note:

> C-ANALOG:C-013 [danger: Critic: answers partly supported] The crop, county and city figures (Pugh, Chaudhary, Bastin) have no unrestricted comparison, so they do not show that narrowing the pool raises novelty.
>
> C-ANALOG:C-038 [danger: Critic: answers partly supported] (5) The D1 answer and section 1.3 treat Pugh, Chaudhary and Bastin as evidence that narrowing the pool raises novelty.
>
> C-ANALOG:C-103 [warning: Adversarial critique, full findings] - The D1 answer's reference-domain item mixes within-study controlled contrasts (Williams 500 km, Burke deep time) with between-study figures that differ in variables, metric, unit and horizon (Pugh crop area, Chaudhary counties, Bastin city hull).
>
> C-ANALOG:A-102 [4. Answers] - it rises when the pool is a crop's own area or a national set [9, 10];
>
> C-ANALOG:B-0067 [1.3 Reference domain and search extent] - **Narrowing the pool raises novelty.**
>

Not found in the cited text (where to look, not what is wrong): "Restricting the pool to a crop own area, a national county set or a city hull raises novelty, as Pugh, Chaudhary and Bastin show."

## dns.7 (do not say)

"Bastin et al. overstate their reference set by claiming that these climates do not exist 'on the planet today'."

- why: That phrase is not in the abstract, which says 'not currently experienced by any existing major cities', so the critique of the authors rests on a misquote or on unverified body text.
- instead: reference-domain.5
- trail: C-ANALOG §critic, §Adversarial

From the note:

> C-ANALOG:C-033 [danger: Critic: answers partly supported] (2) Bastin: the review says the abstract claims climates that do not exist 'on the planet today' and criticises it for overstating its reference set.
>
> C-ANALOG:C-034 [danger: Critic: answers partly supported] The abstract actually says 'not currently experienced by any existing major cities', so the critique rests on a misquote.
>
> C-ANALOG:C-053 [warning: Adversarial critique, full findings] - Bastin et al. 2019 [7]: the quoted 'on the planet today' phrase is not in the abstract ('not currently experienced by any existing major cities'). The reviewer's critique of the authors therefore rests on a misquote or on unverified body text.
>
> C-ANALOG:C-109 [warning: Adversarial critique, full findings] - The Bastin critique ('overstates the reference set') is a reviewer judgement about the authors that rests on an unverified quote.
>
> C-ANALOG:B-0070 [1.3 Reference domain and search extent] The abstract says these climates do not exist "on the planet today".
>
> C-ANALOG:B-0071 [1.3 Reference domain and search extent] The reviewer's reading is that this overstates the reference set, which was cities, not global land.
>

Not found in the cited text (where to look, not what is wrong): "Bastin et al. overstate their reference set by claiming that these climates do not exist 'on the planet today'."

## dns.8 (do not say)

"Judging climate variable by variable understates novelty."

- why: The claim is phrased generally but rests on two nearest precedents from different settings (Mesgaran 2014, abstract only; Mahony and Cannon 2018), neither of which addresses how distance measures scale with dimension.
- instead: variable-count.4
- trail: C-ANALOG §Adversarial, §critic

From the note:

> C-ANALOG:C-059 [warning: Adversarial critique, full findings] - 'Judging variable by variable understates novelty' (1.6 and the D1 answer) is phrased generally but rests on two nearest precedents from different settings (Mesgaran 2014, abstract only; Mahony and Cannon 2018).
>
> C-ANALOG:C-018 [danger: Critic: answers partly supported] Neither addresses how raw distance-based measures scale with dimension, so 'more variables means more novelty' is not established for spatial analogue shares.
>
> C-ANALOG:B-0103 [1.6 Number of variables combined] Both point the same way: judging variable by variable understates novelty.
>

Not found in the cited text (where to look, not what is wrong): "Judging climate variable by variable understates novelty."

## dns.9 (do not say)

"Recasting climate in a biological state space is the clearest demonstration that the state space moves the share by one to two orders of magnitude."

- why: The state-space effect rests on Conradi 2024 alone; the review flags this but still calls it the clearest demonstration in the set.
- instead: global-climate-shares.13
- trail: C-ANALOG §Adversarial

From the note:

> C-ANALOG:C-062 [warning: Adversarial critique, full findings] - The state-space effect of one to two orders of magnitude rests on Conradi 2024 alone. The review flags this, but section 1.2 still calls it 'the clearest demonstration in the set'.
>
> C-ANALOG:B-0064 [1.2 Global land estimates] This is the clearest demonstration in the set that the space in which analogues are sought can move the answer by one to two orders of magnitude.
>

Not found in the cited text (where to look, not what is wrong): "Recasting climate in a biological state space is the clearest demonstration that the state space moves the share by one to two orders of magnitude."

## dns.10 (do not say)

"Present-day soil sampling covers combinations of soil variables worse than single soil variables."

- why: In Guerra 2020 the 59.6% uncovered figure is for climate combinations, and the authors write that most soil-related variables are well covered; the only soil-combination statement is qualitative, so the review's reading merges soil univariate with climate combination coverage and carries it into the D2 answer as a soil result.
- instead: soil-site-coverage.3, soil-site-coverage.1
- trail: C-ANALOG §critic, §Adversarial, §4. Answers

From the note:

> C-ANALOG:C-040 [danger: Critic: answers partly supported] (6) The D2 answer's 'coverage poorer for combinations than for pH or texture singly [25]' is not a like-for-like contrast in Guerra: the 59.6% figure is for climate combinations, and the authors write that 'most soil-related variables are well covered'.
>
> C-ANALOG:C-098 [warning: Adversarial critique, full findings] - Guerra 2020 [25]: the review's 'combined coverage worse than univariate coverage' merges soil univariate coverage (well covered) with climate combination coverage (59.6% uncovered).
>
> C-ANALOG:C-100 [warning: Adversarial critique, full findings] This reading is carried into the D2 answer as a soil result.
>
> C-ANALOG:A-057 [quote: Answers as delivered] Soil sampling covers pH and texture well except at extremes, and covers combinations (and climate) poorly [25].
>
> C-ANALOG:A-070 [quote: Answers as delivered] The only soil-relevant contrast is for present-day sampling coverage, where combined coverage is worse than univariate coverage [25].
>
> C-ANALOG:A-094 [quote: Answers as delivered] The contrast between combined and univariate coverage rests on Guerra et al. 2020 [25]..
>
> C-ANALOG:A-117 [4. Answers] - coverage of present-day sampling, which is poorer for combinations than for pH or texture singly [25];
>
> C-ANALOG:B-0134 [2.3 How well present-day sites cover soil space] It is the only soil-relevant evidence here that combined coverage is worse than univariate coverage.
>

Not found in the cited text (where to look, not what is wrong): "Present-day soil sampling covers combinations of soil variables worse than single soil variables."

