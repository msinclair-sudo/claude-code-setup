## contamination.1 (claim)

In a Salmonella bongori dilution series run at three institutes, contaminants dominated by about 10^3 cells, more so at 40 than at 20 cycles, and contaminant profiles differed by kit and laboratory.

- conf: repl (marker)
- class: meas (marker)
- holds: a dilution series at three institutes
- src: salterReagentLaboratoryContamination2014 (FT; meas; repl)
- trail: MB-01 §2.13, §answers

From the note:

> MB-01:B-0174 [2.13 Contaminants and negative controls] **Reagent contamination.** In a Salmonella bongori dilution series run at three institutes, contaminants dominated by about 10^3 cells, more so at 40 than at 20 cycles.
>
> MB-01:I-0070 [2.13 Contaminants and negative controls] Profiles differed by kit and laboratory (Salter 2014) [FT; meas; repl].
>
> MB-01:A-100 [quote: Answers as delivered] RA and taxa: contaminants dominated by about 10^3 input cells (Salter 2014).
>
> MB-01:B-0078 [2. Steps from sample to table (D1) and departures from the sampled community (D2)] Kit- and lab-specific | Salter 2014; Karstens 2019; Minich 2019 |
>

## contamination.2 (claim)

In an 8-member mock diluted 3-fold eight times, contaminant reads rose from 0.1% to 80.1% and ASVs from 18 to 381.

- conf: single (marker)
- class: meas (marker)
- holds: one diluted 8-member mock
- src: karstensControllingContaminantsLowbiomass2019 (FT; meas; single)
- trail: MB-01 §2.13, §answers

From the note:

> MB-01:I-0071 [2.13 Contaminants and negative controls] **Diluted mock.** In an 8-member mock diluted 3-fold eight times (Karstens 2019) [FT; meas; single]:
>
> MB-01:B-0175 [2.13 Contaminants and negative controls] - contaminant reads rose from 0.1% to 80.1% and ASVs from 18 to 381;
>
> MB-01:A-101 [quote: Answers as delivered] In a diluted mock, contaminants rose from 0.1% to 80.1% of reads and ASVs from 18 to 381 (Karstens 2019).
>
> MB-01:B-0077 [2. Steps from sample to table (D1) and departures from the sampled community (D2)] | Contamination | 0.1 to 80.1% of reads across a mock dilution series | ASVs 18 to 381 | Inversely related to biomass.
>

## contamination.3 (claim)

Removing every sequence present in the negative control wrongly removed more than 20% of expected sequences, since three of the eight mock ASVs appeared in the control.

- conf: single (marker)
- class: meas (marker)
- holds: one diluted 8-member mock
- src: karstensControllingContaminantsLowbiomass2019 (FT; meas; single)
- trail: MB-01 §2.13, §7. Bounds

From the note:

> MB-01:I-0071 [2.13 Contaminants and negative controls] **Diluted mock.** In an 8-member mock diluted 3-fold eight times (Karstens 2019) [FT; meas; single]:
>
> MB-01:B-0176 [2.13 Contaminants and negative controls] - removing every sequence present in the negative control wrongly removed more than 20% of expected sequences, since three of the eight mock ASVs appeared in the control;
>
> MB-01:B-0360 [7. Bounds and negative results] - removing every taxon seen in negative controls (Karstens 2019);
>

## contamination.4 (claim)

decontam's frequency method removed 70 to 90% of contaminants and no expected sequences.

- conf: single (marker)
- class: meas (marker)
- holds: one diluted 8-member mock
- src: karstensControllingContaminantsLowbiomass2019 (FT; meas; single)
- trail: MB-01 §2.13

From the note:

> MB-01:I-0071 [2.13 Contaminants and negative controls] **Diluted mock.** In an 8-member mock diluted 3-fold eight times (Karstens 2019) [FT; meas; single]:
>
> MB-01:B-0177 [2.13 Contaminants and negative controls] - decontam's frequency method removed 70 to 90% of contaminants and no expected sequences;
>

## contamination.5 (claim)

SourceTracker removed over 98% of contaminants when sources were well defined but failed on over 97% when they were not.

- conf: single (marker)
- class: meas (marker)
- holds: one diluted 8-member mock
- src: karstensControllingContaminantsLowbiomass2019 (FT; meas; single)
- trail: MB-01 §2.13, §7. Bounds

From the note:

> MB-01:I-0071 [2.13 Contaminants and negative controls] **Diluted mock.** In an 8-member mock diluted 3-fold eight times (Karstens 2019) [FT; meas; single]:
>
> MB-01:B-0178 [2.13 Contaminants and negative controls] - SourceTracker removed over 98% when sources were well defined but failed on over 97% when they were not.
>
> MB-01:B-0361 [7. Bounds and negative results] - SourceTracker with undefined sources (Karstens 2019);
>

## contamination.6 (claim)

Well-to-well contamination arose mainly at extraction, less at library preparation, mostly into neighbouring wells (rarely up to 10 wells away), and was greatest in low-biomass samples.

- conf: single (marker)
- class: meas (marker)
- holds: neighbouring wells
- src: minichQuantifyingUnderstandingWelltowell2019 (FT; meas; single)
- trail: MB-01 §2.13, §answers

From the note:

> MB-01:I-0072 [2.13 Contaminants and negative controls] **Well-to-well contamination.** This arose mainly at extraction, less at library preparation, mostly into neighbouring wells (rarely up to 10 wells away), and was greatest in low-biomass samples (Minich 2019) [FT; meas; single].
>
> MB-01:A-102 [quote: Answers as delivered] Well-to-well leakage occurred mainly during extraction (Minich 2019).
>

## contamination.7 (claim)

Contamination varies inversely with biomass and is specific to the kit and laboratory.

- conf: not stated
- class: not stated
- holds: as stated
- src: salterReagentLaboratoryContamination2014, karstensControllingContaminantsLowbiomass2019, minichQuantifyingUnderstandingWelltowell2019
- trail: MB-01 §answers

From the note:

> MB-01:A-103 [quote: Answers as delivered] Consistency: varies inversely with biomass and is specific to the kit and laboratory.
>
> MB-01:B-0077 [2. Steps from sample to table (D1) and departures from the sampled community (D2)] | Contamination | 0.1 to 80.1% of reads across a mock dilution series | ASVs 18 to 381 | Inversely related to biomass.
>
> MB-01:B-0078 [2. Steps from sample to table (D1) and departures from the sampled community (D2)] Kit- and lab-specific | Salter 2014; Karstens 2019; Minich 2019 |
>

## contamination.8 (claim)

decontam's makers describe a frequency mode that assumes contaminant DNA is roughly constant across samples.

- conf: not stated
- class: not stated
- holds: a developer claim
- src: davisSimpleStatisticalIdentification2018 (FT; developer claim)
- trail: MB-01 §2.13

From the note:

> MB-01:B-0179 [2.13 Contaminants and negative controls] **Tools and practice.** decontam's makers describe a frequency mode that assumes contaminant DNA is roughly constant across samples (Davis 2018) [FT; developer claim].
>

## contamination.9 (claim)

A review proposes the RIDE checklist for low-biomass studies.

- conf: not stated
- class: assert (marker)
- holds: a review
- src: eisenhoferContaminationLowMicrobial2019 (AB; assert)
- trail: MB-01 §2.13

From the note:

> MB-01:I-0074 [2.13 Contaminants and negative controls] A review proposes the RIDE checklist (Eisenhofer 2019) [AB; assert].
>

## contamination.10 (claim)

The most abundant spurious taxon in mocks had a median relative abundance of 0.12%.

- conf: not stated
- class: not stated
- holds: mocks
- src: reitmeierHandlingSpuriousSequences2021
- trail: MB-01 §2.13

From the note:

> MB-01:B-0180 [2.13 Contaminants and negative controls] **Spurious-taxon threshold.** The most abundant spurious taxon in mocks had a median relative abundance of 0.12% (Reitmeier 2021).
>

## dominant-steps.1 (claim)

The ordering in which DNA extraction is the largest source of relative-abundance error, followed by PCR and then sequencing, rests on one 7-taxon vaginal dataset (Brooks 2015, reanalysed by McLaren 2019), with Albertsen 2015 (sludge, bead beating only) as partial support; it is contested by Fouhy 2016 (two extraction methods gave very similar data) and qualified by MBQC (specimen type mattered more than extraction), and is a single-dataset result, not a field-wide ordering.

- conf: single (critic: MB-01:C-017)
- class: not stated
- holds: one 7-taxon vaginal dataset, 454
- src: mclarenConsistentCorrectableBias2019, brooksTruthMetagenomicsQuantifying2015, albertsenBackBasicsInfluence2015, fouhy16SRRNAGene2016, sinhaAssessmentVariationMicrobial2017
- trail: MB-01 §critic, §Adversarial, §1. Overview, §answers, §8. Answers
- rating: "Strong" (critic: MB-01:C-083: firmer than the access and source base allow)

From the note:

> MB-01:C-015 [danger: Critic: answers partly supported] For relative abundance, the claim that extraction is the largest step, followed by PCR and then sequencing, rests on one 7-taxon vaginal dataset (Brooks 2015, reanalysed by McLaren 2019).
>
> MB-01:C-016 [danger: Critic: answers partly supported] It is contested by Fouhy 2016 (two extraction methods gave very similar data) and qualified by MBQC (specimen type mattered more than extraction).
>
> MB-01:C-017 [danger: Critic: answers partly supported] It should be presented as SINGLE DATASET, not as a field-wide ordering.
>
> MB-01:C-061 [danger: Critic: answers partly supported] D2 calls the step ordering 'strong' and backed by 'many independent mock studies', while its own sensitivity note says the ordering rests on McLaren/Brooks.
>
> MB-01:C-083 [warning: Adversarial critique, full findings] - D2 'strength' field: rated 'Strong ... for the ordering', which is firmer than the access and source base allow (one re-analysed 454 dataset), as the review's own single_source_sensitivity field concedes.
>
> MB-01:C-084 [warning: Adversarial critique, full findings] - Overview and D2 answer: 'The largest measured distortions [in relative abundance] arise from taxon-specific efficiencies at DNA extraction and PCR' and the extraction > PCR > sequencing ordering are phrased as field properties and rated 'strong'. They rest on one 7-taxon dataset (Brooks 2015 reanalysed by McLaren 2019), with Albertsen 2015 (sludge, bead beating only) as partial support, and are contradicted by Fouhy 2016 and qualified by MBQC.
>
> MB-01:A-111 [quote: Answers as delivered] *Strength:* Strong that every step distorts composition, and for the ordering in which spurious taxa and contamination dominate richness error while extraction and PCR dominate relative-abundance error.
>
> MB-01:A-131 [quote: Answers as delivered] *Single-source sensitivity:* The per-step decomposition (extraction largest, then PCR, then sequencing) and the ratio-consistency claim would weaken substantially without McLaren 2019 and its source data (Brooks 2015).
>
> MB-01:A-297 [8. Answers in brief] Extraction and PCR dominate relative-abundance error, at roughly 2 to 30-fold pairwise.
>
> MB-01:B-0035 [1. Overview] - **Relative abundance.** The largest measured distortions arise from taxon-specific efficiencies at DNA extraction and PCR.
>
> MB-01:B-0036 [1. Overview] Fold errors of 2 to 30 or more between taxon pairs are reported.
>

## dominant-steps.2 (claim)

In the reanalysed 7-taxon cell mixtures, PCR followed extraction (maximum pairwise bias 5.2, mean 2.3), then sequencing and classification (maximum 1.6, mean 1.2).

- conf: single (critic: MB-01:C-017)
- class: deriv/model (marker)
- holds: 80 cell mixtures of 7 vaginal taxa, V1-V3, 454
- src: mclarenConsistentCorrectableBias2019 (FT, re-opened; deriv/model; single dataset)
- trail: MB-01 §2.2

From the note:

> MB-01:I-0007 [2.2 DNA extraction] **Magnitude in a defined mock.** McLaren et al. reanalysed Brooks et al.'s 80 cell mixtures of 7 vaginal taxa (V1-V3, 454) (McLaren 2019) [FT, re-opened; deriv/model; single dataset].
>
> MB-01:B-0090 [2.2 DNA extraction] PCR followed (max 5.2, mean 2.3), then sequencing and classification (max 1.6, mean 1.2).
>
> MB-01:C-017 [danger: Critic: answers partly supported] It should be presented as SINGLE DATASET, not as a field-wide ordering.
>
> MB-01:B-0089 [2.2 DNA extraction] The extraction step had a maximum pairwise bias of 36.6-fold and a mean of 5.5-fold.
>

## dominant-steps.3 (claim)

In the same cell mixtures, total bias was a maximum of 29.3-fold and a mean of 5.6-fold, smaller than extraction bias alone, which implies partial cancellation between steps.

- conf: single (critic: MB-01:C-017)
- class: deriv/model (marker)
- holds: 80 cell mixtures of 7 vaginal taxa
- src: mclarenConsistentCorrectableBias2019 (FT, re-opened; deriv/model; single dataset)
- trail: MB-01 §2.2, §critic

From the note:

> MB-01:I-0007 [2.2 DNA extraction] **Magnitude in a defined mock.** McLaren et al. reanalysed Brooks et al.'s 80 cell mixtures of 7 vaginal taxa (V1-V3, 454) (McLaren 2019) [FT, re-opened; deriv/model; single dataset].
>
> MB-01:B-0091 [2.2 DNA extraction] Total bias in cell mixtures was a maximum of 29.3-fold and a mean of 5.6-fold.
>
> MB-01:B-0092 [2.2 DNA extraction] Total bias is smaller than extraction bias alone, which implies partial cancellation between steps.
>
> MB-01:C-017 [danger: Critic: answers partly supported] It should be presented as SINGLE DATASET, not as a field-wide ordering.
>
> MB-01:C-054 [danger: Critic: answers partly supported] Verified against full text: McLaren 2019 per-step bias table (36.6 and 29.3 max, 5.5 and 5.6 mean), Silverman 2021 (2.6-fold, about 19% of taxa more than 4-fold, mis-set annealing machine), Sze and Schloss 2019 (R2 0.79, 0.044, 0.033; chimera rates 0.9 to 18.2%), Schloss 2024b (Table 1 read ranges, coverage-based iNEXT passage, Good's coverage 89.4 to 99.8%), Karstens 2019, Fitzpatrick 2018, Thompson 2017, Song 2016, Starke 2021, Louca 2018, Laursen 2017, Wen 2017, Weiss 2017, Nearing 2018 and 2022, Wirbel 2024, Zemb 2020, Glassman 2018, Chiarello 2022, Stoddard 2015, Vetrovsky 2013, Kembel 2012, Hornung 2019, Lennon 2018, Barlow 2020 and Dyrhovden 2021.
>

## dominant-steps.4 (claim)

Across 15 laboratories, variability depended most on specimen type, then DNA extraction, then handling laboratory, then bioinformatics.

- conf: single (marker)
- class: meas (marker)
- holds: the MBQC interlaboratory study, whole workflow
- src: sinhaAssessmentVariationMicrobial2017 (FT; meas; single)
- trail: MB-01 §2.2, §answers

From the note:

> MB-01:I-0011 [2.2 DNA extraction] **Interlaboratory.** Across 15 laboratories, variability depended most on specimen type, then DNA extraction, then handling laboratory, then bioinformatics (Sinha 2017, MBQC) [FT; meas; single].
>
> MB-01:A-104 [quote: Answers as delivered] Whole workflow.
>
> MB-01:A-105 [quote: Answers as delivered] Across 15 laboratories, specimen type mattered most, then extraction, then laboratory and bioinformatics (MBQC).
>

## dominant-steps.5 (claim)

For the number of taxa detected, inflation by spurious sequences (sequencing error, chimeras, cross-sample leakage, reagent contamination) and by the choice of clustering or denoising is replicated across independent mocks and dilution series: 10 to 200-fold excess units, and contaminants rising from 0.1% to 80.1% of reads in a diluted mock; these can change counts of taxa by one to two orders of magnitude.

- conf: repl (critic: MB-01:C-014)
- class: not stated
- holds: mocks and dilution series
- src: straubInterpretationsEnvironmentalMicrobial2020, karstensControllingContaminantsLowbiomass2019
- trail: MB-01 §critic, §1. Overview, §8. Answers
- rating: "Strong" (critic: MB-01:C-022: moderate for the inflation of taxon counts)

From the note:

> MB-01:C-014 [danger: Critic: answers partly supported] For number of taxa detected, inflation by spurious sequences, chimeras, reagent contamination and pipeline choice is replicated across independent mocks and dilution series: 10 to 200-fold excess units (Straub 2020), contaminants rising from 0.1% to 80.1% of reads in a diluted mock (Karstens 2019).
>
> MB-01:C-022 [danger: Critic: answers partly supported] Overall: strong qualitatively; moderate for the inflation of taxon counts; weak for per-step relative-abundance magnitudes and for consistency across samples.
>
> MB-01:A-298 [8. Answers in brief] Spurious sequences, contamination and pipeline choice dominate the number of taxa detected, by up to 10 to 200-fold in unit counts.
>
> MB-01:A-111 [quote: Answers as delivered] *Strength:* Strong that every step distorts composition, and for the ordering in which spurious taxa and contamination dominate richness error while extraction and PCR dominate relative-abundance error.
>
> MB-01:B-0037 [1. Overview] - **Number of taxa detected.** The largest distortions arise from spurious sequences (sequencing error, chimeras, cross-sample leakage, reagent contamination) and from the choice of clustering or denoising.
>
> MB-01:B-0038 [1. Overview] These can change counts of taxa by one to two orders of magnitude.
>

## dominant-steps.6 (claim)

Per-step magnitudes of departure mostly come from one or two small mocks (7 to 20 taxa), often on 454 or Ion Torrent.

- conf: not stated
- class: not stated
- holds: mocks of 7 to 20 taxa
- src: none (the reviewer's and critic's account of the evidence base)
- trail: MB-01 §answers, §critic
- rating: "Magnitudes per step are moderate" (critic: MB-01:C-022: weak for per-step relative-abundance magnitudes)

From the note:

> MB-01:A-113 [quote: Answers as delivered] Magnitudes per step are moderate: most come from one or two mocks of 7-20 taxa, often on 454 or Ion Torrent.
>
> MB-01:C-018 [danger: Critic: answers partly supported] Per-step magnitudes mostly come from one or two small mocks (7 to 20 taxa), often on 454.
>
> MB-01:C-022 [danger: Critic: answers partly supported] Overall: strong qualitatively; moderate for the inflation of taxon counts; weak for per-step relative-abundance magnitudes and for consistency across samples.
>
> MB-01:A-301 [8. Answers in brief] Strong qualitatively, moderate for magnitudes, weak for consistency.
>

## bias-consistency.1 (claim)

Modelling each step as multiplying taxon abundances by a taxon-specific efficiency, McLaren et al. found that the error in taxon ratios was "consistent across samples", while the error in proportions "varied dramatically in both magnitude and direction", in the one dataset modelled for this question (the vaginal cell mixtures; extraction bias was consistent on the ratio scale within a protocol); bias behaves as a multiplicative factor per taxon that calibration controls can correct.

- conf: single (note: "the one dataset modelled for this question")
- class: model (note: "modelled")
- holds: 7 taxa mixed as cells and reanalysed
- src: mclarenConsistentCorrectableBias2019 (FT, re-opened)
- trail: MB-01 §2.14, §2.2, §answers, §Adversarial, MB-02 §D1.4
- contrary: one-sided (critic: MB-01:C-130)

From the note:

> MB-01:B-0182 [2.14 Is the departure consistent across samples?] **Ratio-scale model.** McLaren et al. modelled each step as multiplying taxon abundances by a taxon-specific efficiency (McLaren 2019) [FT, re-opened].
>
> MB-01:B-0183 [2.14 Is the departure consistent across samples?] Under this model, the error in ratios was "consistent across samples", while the error in proportions "varied dramatically in both magnitude and direction".
>
> MB-01:A-107 [quote: Answers as delivered] Is bias consistent across samples?
>
> MB-01:A-108 [quote: Answers as delivered] In the one dataset modelled for this question, error in taxon ratios was consistent across samples while error in proportions varied in size and sign (McLaren 2019).
>
> MB-01:A-299 [8. Answers in brief] Consistency across samples is shown on the ratio scale in one 7-taxon dataset.
>
> MB-01:B-0101 [2.2 DNA extraction] **Consistency.** On the ratio scale, extraction bias was consistent across samples within a protocol in the vaginal mock (McLaren 2019).
>
> MB-01:A-048 [quote: Answers as delivered] Consistency: consistent on the ratio scale within a protocol in the vaginal mock.
>
> MB-01:B-0056 [2. Steps from sample to table (D1) and departures from the sampled community (D2)] Relic DNA: richness up to +55%, or minimal effect | Consistent on the ratio scale within a protocol (vaginal mock; shotgun spike-in SEC).
>
> MB-01:C-128 [warning: Adversarial critique, full findings] - D2 consistency of bias: McLaren 2019's ratio-scale consistency comes from 7 taxa mixed as cells and reanalysed.
>
> MB-01:C-129 [warning: Adversarial critique, full findings] It is presented as the main evidence 'in the one dataset modelled for this question', while field evidence of inconsistency (Parada, abstract only, one primer pair) is weighed as 'limiting'.
>
> MB-01:C-130 [warning: Adversarial critique, full findings] Neither side's small-n and access limits are stated symmetrically in the answer's strength line.
>
> MB-02:B-0131 [D1.4 Copy number and read-based abundance] Bias in sequencing measurements behaves as a consistent multiplicative factor per taxon, which can be corrected with calibration controls [35, AB].
>
> MB-01:I-0002 [1. Overview] One reanalysis finds it consistent on the ratio scale, which implies it varies on the proportion scale (McLaren 2019) [FT; model; single].
>

## bias-consistency.2 (claim)

Six parameters explained almost all systematic error in the cell mixtures, and calibration cut mean Bray-Curtis error from 0.35 to 0.08 (92.6% lower mean squared error); this result comes from the Brooks et al. 2015 16S cell mixtures (2 calibration samples, 69 calibrated samples), not from a shotgun dataset.

- conf: not stated
- class: not stated
- holds: the Brooks 16S cell mixtures
- src: mclarenConsistentCorrectableBias2019
- trail: MB-01 §2.14, §critic, §Adversarial
- contrary: one-sided (critic: MB-01:C-131)

From the note:

> MB-01:B-0184 [2.14 Is the departure consistent across samples?] Six parameters explained almost all systematic error in the cell mixtures, and calibration cut mean Bray-Curtis error from 0.35 to 0.08 in a shotgun dataset.
>
> MB-01:C-021 [danger: Critic: answers partly supported] Correction: McLaren's calibration result (Bray-Curtis error from 0.35 to 0.08, 92.6% lower mean squared error) comes from the Brooks 16S cell mixtures, not from a shotgun dataset.
>
> MB-01:C-055 [danger: Critic: answers partly supported] Errors found: (a) McLaren's calibration figure (Bray-Curtis 0.35 to 0.08) is attributed to a shotgun dataset; it is from the Brooks 16S cell mixtures.
>
> MB-01:C-066 [warning: Adversarial critique, full findings] - McLaren 2019 (re-opened, FT): section 2.14 says calibration 'cut mean Bray-Curtis error from 0.35 to 0.08 in a shotgun dataset'.
>
> MB-01:C-067 [warning: Adversarial critique, full findings] The full text places this in the Brooks et al. 2015 16S cell mixtures (2 calibration samples, 69 calibrated samples).
>
> MB-01:C-069 [warning: Adversarial critique, full findings] The error survives in a source the synthesis agent says it re-opened and checked.
>
> MB-01:C-131 [warning: Adversarial critique, full findings] - Section 2.14 labels Edgar 2017b (UNBIAS) a 'strong pessimistic claim' and sets it aside as a single-source contrary result. The pro-correction results it conflicts with (McLaren, Silverman) each also rest on a single mock design and get no matching single-source label at that point.
>

## bias-consistency.3 (claim)

A 10-species shotgun spike-in across faecal backgrounds also gave a consistent profile on the ratio scale, with protocol H showing up to 2,751-fold maximum pairwise bias; this is known only via McLaren 2019, and its calibration is reported only qualitatively ("removed most of the systematic error").

- conf: not stated
- class: not stated
- holds: shotgun, faecal backgrounds; secondary and indirect
- src: costeaTowardsStandardsHuman2017 (SEC; INDIRECT, shotgun)
- trail: MB-01 §2.2, §answers, §Adversarial
- limit: access (note: "known only via McLaren 2019")

From the note:

> MB-01:B-0102 [2.2 DNA extraction] The same held for a 10-species shotgun spike-in across faecal backgrounds: protocol H showed up to 2,751-fold maximum pairwise bias (Costea 2017, known only via McLaren 2019) [SEC; INDIRECT, shotgun].
>
> MB-01:A-049 [quote: Answers as delivered] A shotgun spike-in also gave a consistent profile across faecal backgrounds (Costea 2017, known only via McLaren; secondary; indirect).
>
> MB-01:C-068 [warning: Adversarial critique, full findings] The Costea shotgun calibration is reported only qualitatively ('removed most of the systematic error').
>
> MB-01:R-0613 [References] **Known only secondarily.** Costea, Paul I. et al. (2017), Nature Biotechnology 35(11): 1069-1076, https://doi.org/10.1038/nbt.3960, is known only through McLaren 2019 and is cited to McLaren as SEC.
>

## bias-consistency.4 (claim)

McLaren et al. list where the ratio model may fail: PCR saturation, taxa aggregated with differing efficiencies, matrix differences between controls and samples, and taxa absent from the controls.

- conf: not stated
- class: not stated
- holds: their model
- src: mclarenConsistentCorrectableBias2019
- trail: MB-01 §2.14

From the note:

> MB-01:B-0185 [2.14 Is the departure consistent across samples?] The authors list where the model may fail: PCR saturation, taxa aggregated with differing efficiencies, matrix differences between controls and samples, and taxa absent from the controls.
>
> MB-01:B-0182 [2.14 Is the departure consistent across samples?] **Ratio-scale model.** McLaren et al. modelled each step as multiplying taxon abundances by a taxon-specific efficiency (McLaren 2019) [FT, re-opened].
>

## bias-consistency.5 (claim)

On the same data, Brooks et al. found significant mixture-blending terms and concluded that one taxon's observed proportion depends on which others are present; the two readings conflict, and McLaren's attributes the apparent dependence to working on the proportion scale.

- conf: cont (note: "The two readings conflict")
- class: not stated
- holds: the Brooks 2015 cell mixtures
- src: brooksTruthMetagenomicsQuantifying2015, mclarenConsistentCorrectableBias2019
- trail: MB-01 §2.14, §answers, §1. Overview, §6. Where

From the note:

> MB-01:B-0186 [2.14 Is the departure consistent across samples?] **Composition-dependence reading.** Brooks et al. found significant mixture-blending terms on the same data and concluded that one taxon's observed proportion depends on which others are present (Brooks 2015).
>
> MB-01:B-0187 [2.14 Is the departure consistent across samples?] The two readings conflict, and McLaren's attributes the apparent dependence to working on the proportion scale.
>
> MB-01:A-109 [quote: Answers as delivered] The original authors read the same data as composition-dependent (Brooks 2015).
>
> MB-01:A-115 [quote: Answers as delivered] *Conflicts:* Composition dependence of bias: Brooks 2015 versus McLaren 2019, on the same data.
>
> MB-01:B-0039 [1. Overview] Whether bias is consistent across samples is less settled.
>
> MB-01:B-0040 [1. Overview] The original authors of the same data read it as composition dependent (Brooks 2015).
>
> MB-01:B-0329 [6. Where the evidence conflicts] Bias composition dependence: Brooks 2015 versus McLaren 2019, on the same data.
>

## bias-consistency.6 (claim)

Bias varies between sample types or samples: a field-versus-mock SAR11 bias for the 515F-Y/806R pair (abstract only), inconsistent cycle effects in four stool samples, extraction yield of 40 to 84%, and a 66.7-fold spike-in range (abstract).

- conf: mixed (marker)
- class: meas (marker)
- holds: field and mock samples, stool samples, spike-ins
- src: paradaEveryBaseMatters2016 (AB; meas; repl), szeImpactDNAPolymerase2019 (FT; meas; single), zembAbsoluteQuantitationMicrobes2020, zhouReproducibilityQuantitationAmplicon2011
- trail: MB-01 §critic, §1. Overview, §2.14, §answers, §8. Answers

From the note:

> MB-01:C-020 [danger: Critic: answers partly supported] Variation between sample types or samples is shown by a field-versus-mock SAR11 bias for the 515F-Y/806R pair (Parada 2016, abstract only), inconsistent cycle effects in four stool samples (Sze and Schloss 2019), extraction yield of 40 to 84% (Zemb 2020) and a 66.7-fold spike-in range (Zhou 2011, abstract).
>
> MB-01:I-0003 [1. Overview] Field and stool studies show bias that does not carry over from mocks (Parada 2016) [AB; meas; repl] or that varies between samples (Sze and Schloss 2019) [FT; meas; single].
>
> MB-01:A-110 [quote: Answers as delivered] The field-versus-mock discrepancy (Parada 2016) and the inconsistent stool results (Sze and Schloss 2019) are evidence that bias varies between sample types.
>
> MB-01:A-300 [8. Answers in brief] Field and stool evidence shows departures that vary.
>
> MB-01:B-0188 [2.14 Is the departure consistent across samples?] **Evidence that bias varies between sample types.**
>

## bias-consistency.7 (claim)

A 0.1% genomic spike was recovered at 0.06% to 5.34% of reads across soils, a 66.7-fold range; the 66.7-fold figure is in the abstract, and the 0.06 to 5.34% range, which needs the body, could not be confirmed.

- conf: single (marker)
- class: meas (marker)
- holds: soils, 454
- src: zhouReproducibilityQuantitationAmplicon2011 (AB; meas; single; critic: MB-01:C-075 was "FT per statistics angle; meas; single")
- trail: MB-01 §2.14, §5.5, §answers, §Adversarial
- limit: access (critic: MB-01:C-076)

From the note:

> MB-01:I-0075 [2.14 Is the departure consistent across samples?] - A 0.1% genomic spike was recovered at 0.06% to 5.34% of reads across soils, a 66.7-fold range (Zhou 2011) [FT per statistics angle; meas; single].
>
> MB-01:B-0319 [5.5 Absolute quantification of total load] - Spike-in yield varied 40 to 84% (Zemb 2020), and spike recovery varied 66.7-fold (Zhou 2011).
>
> MB-01:A-268 [quote: Answers as delivered] Spike-in recovery varied 40-84% (Zemb 2020) and 66.7-fold (Zhou 2011).
>
> MB-01:C-075 [warning: Adversarial critique, full findings] The figures that matter from Zhou 2011 (17.2%, 8.2%, 66.7-fold) are in its abstract and should be labelled AB-derived.
>
> MB-01:C-076 [warning: Adversarial critique, full findings] Figures needing the body (Zhou 2011's 0.06 to 5.34% spike range and its 13.1%/5.9% discussion values; Kozich's 9,913 and 2,454 reads; Haegeman's 26,079 reads and 2,880 species; Lin 2019's r2 0.19 and 0.61) could not be confirmed, and the review shows no evidence of full-text reading beyond 'per angle'.
>

Not found in the cited text (where to look, not what is wrong): holds: 454

## bias-consistency.8 (claim)

Whether mock-derived bias applies to field samples is disputed: Parada 2016 against the calibration claims of McLaren 2019 and Silverman 2021.

- conf: not stated
- class: not stated
- holds: field samples against calibration claims
- src: paradaEveryBaseMatters2016, mclarenConsistentCorrectableBias2019, silvermanMeasuringMitigatingPCR2021
- trail: MB-01 §answers, §6. Where

From the note:

> MB-01:A-121 [quote: Answers as delivered] Whether mock-derived bias applies to field samples: Parada 2016 versus calibration claims (McLaren 2019; Silverman 2021).
>
> MB-01:B-0337 [6. Where the evidence conflicts] Whether mock bias transfers to field samples: Parada 2016 versus calibration claims.
>

## bias-consistency.9 (claim)

Evidence on whether bias is consistent across samples rests mainly on one reanalysis of 7 taxa, with contrary or limiting field evidence; ratio-scale consistency is shown in one 16S cell-mixture dataset and one shotgun spike-in known only secondarily, and the ratio-consistency claim would weaken substantially without McLaren 2019 and its source data.

- conf: not stated
- class: not stated
- holds: one 16S cell-mixture dataset and one secondary shotgun spike-in
- src: mclarenConsistentCorrectableBias2019, brooksTruthMetagenomicsQuantifying2015, costeaTowardsStandardsHuman2017
- trail: MB-01 §answers, §critic
- rating: "weak to moderate" (critic: MB-01:C-022: weak for consistency across samples)

From the note:

> MB-01:A-114 [quote: Answers as delivered] Evidence on whether bias is consistent across samples is weak to moderate: it rests mainly on one reanalysis of 7 taxa, with contrary or limiting field evidence.
>
> MB-01:A-131 [quote: Answers as delivered] *Single-source sensitivity:* The per-step decomposition (extraction largest, then PCR, then sequencing) and the ratio-consistency claim would weaken substantially without McLaren 2019 and its source data (Brooks 2015).
>
> MB-01:C-019 [danger: Critic: answers partly supported] Consistency across samples: ratio-scale consistency is shown in one 16S cell-mixture dataset and one shotgun spike-in known only secondarily (Costea 2017 via McLaren).
>
> MB-01:C-022 [danger: Critic: answers partly supported] Overall: strong qualitatively; moderate for the inflation of taxon counts; weak for per-step relative-abundance magnitudes and for consistency across samples.
>

## bias-consistency.10 (claim)

A review states that PCR-based estimates can deviate by "several orders of magnitude" if extraction, PCR, copy number and analysis errors are ignored.

- conf: not stated
- class: assert (marker)
- holds: a review
- src: bonkPCRbasedQuantificationTaxaspecific2018 (AB; assert)
- trail: MB-01 §2.14

From the note:

> MB-01:I-0077 [2.14 Is the departure consistent across samples?] **Review assertions.** A review states that PCR-based estimates can deviate by "several orders of magnitude" if extraction, PCR, copy number and analysis errors are ignored (Bonk 2018) [AB; assert].
>

## bias-consistency.11 (claim)

No mock study in a soil matrix with known composition was found, and the consistency of extraction bias across real soil or water matrices has not been measured in the sources found; soil evidence comes from spike-ins, dilutions and relic DNA.

- conf: not stated
- class: search (note: "No mock study in soil matrix with known composition was found")
- holds: soil and water matrices
- src: none (a search result)
- trail: MB-01 §answers
- search: searched, not found (note: "No mock study in soil matrix with known composition was found")

From the note:

> MB-01:A-124 [quote: Answers as delivered] No mock study in soil matrix with known composition was found; soil evidence is from spike-ins, dilutions and relic DNA.
>
> MB-01:A-125 [quote: Answers as delivered] The consistency of extraction bias across real soil or water matrices has not been measured in the sources found.
>
> MB-01:A-126 [quote: Answers as delivered] Routes: lab and bioinformatics angles, Crossref, Europe PMC full text, web search.
>

## bias-consistency.12 (claim)

No archaeal-rich mock was found beyond Pinto and Raskin 2012 and D'Amore 2016.

- conf: not stated
- class: search (note: "No archaeal-rich mock was found")
- holds: archaeal-rich mocks
- src: pintoPCRBiasesDistort2012, damoreComprehensiveBenchmarkingStudy2016
- trail: MB-01 §answers
- search: searched, not found (note: "No archaeal-rich mock was found")

From the note:

> MB-01:A-123 [quote: Answers as delivered] No archaeal-rich mock was found beyond Pinto and Raskin 2012 and D'Amore 2016.
>

## bias-consistency.13 (claim)

In eukaryotic eDNA, modelling the PCR process, calibrated with mocks, has been used to estimate starting proportions.

- conf: not stated
- class: model (marker)
- holds: eukaryotic eDNA, indirect; an abstract
- src: sheltonTowardQuantitativeMetabarcoding2023 (AB; model; INDIRECT)
- trail: MB-01 §5.1

From the note:

> MB-01:I-0111 [5.1 Origins of the approaches] **PCR models from eukaryotic eDNA.** Modelling the PCR process, calibrated with mocks, to estimate starting proportions (Shelton 2023) [AB; model; INDIRECT].
>

## reads-per-sample.1 (claim)

The Earth Microbiome Project averaged 80,000 sequences per sample over 27,751 samples and rarefied to 5,000.

- conf: not stated
- class: not stated
- holds: the EMP survey
- src: thompsonCommunalCatalogueReveals2017
- trail: MB-01 §3.3, §answers

From the note:

> MB-01:B-0211 [3.3 Reads per sample, and variation between samples] **Large survey.** The EMP averaged 80,000 sequences per sample over 27,751 samples and rarefied to 5,000 (Thompson 2017).
>
> MB-01:A-154 [quote: Answers as delivered] Reads per sample.
>
> MB-01:A-155 [quote: Answers as delivered] The EMP averaged 80,000 per sample over 27,751 samples (Thompson 2017).
>

Not found in the cited text (where to look, not what is wrong): Earth; Microbiome; Project

## reads-per-sample.2 (claim)

In four environments of the EMP, mean prevalence of tag sequences rose with depth up to 50,000, so rarefying to 5,000 under-estimated prevalence.

- conf: not stated
- class: not stated
- holds: four environments of the EMP
- src: thompsonCommunalCatalogueReveals2017
- trail: MB-01 §3.3

From the note:

> MB-01:B-0212 [3.3 Reads per sample, and variation between samples] In four environments, mean prevalence of tag sequences rose with depth up to 50,000, so 5,000 under-estimated prevalence.
>
> MB-01:B-0211 [3.3 Reads per sample, and variation between samples] **Large survey.** The EMP averaged 80,000 sequences per sample over 27,751 samples and rarefied to 5,000 (Thompson 2017).
>

## reads-per-sample.3 (claim)

In one 360-sample MiSeq run, reads averaged 9,913 pairs per sample, with 95% of samples above 2,454; these figures need the paper's body and could not be confirmed.

- conf: not stated
- class: not stated
- holds: one MiSeq run
- src: kozichDevelopmentDualindexSequencing2013
- trail: MB-01 §3.3, §answers, §Adversarial
- limit: access (critic: MB-01:C-076)

From the note:

> MB-01:B-0213 [3.3 Reads per sample, and variation between samples] **Single runs.**
>
> MB-01:B-0214 [3.3 Reads per sample, and variation between samples] - In one 360-sample MiSeq run, reads averaged 9,913 pairs per sample, with 95% of samples above 2,454 (Kozich 2013).
>
> MB-01:A-156 [quote: Answers as delivered] One 360-sample MiSeq run averaged 9,913 pairs, with 95% of samples above 2,454 (Kozich 2013).
>
> MB-01:C-076 [warning: Adversarial critique, full findings] Figures needing the body (Zhou 2011's 0.06 to 5.34% spike range and its 13.1%/5.9% discussion values; Kozich's 9,913 and 2,454 reads; Haegeman's 26,079 reads and 2,880 species; Lin 2019's r2 0.19 and 0.61) could not be confirmed, and the review shows no evidence of full-text reading beyond 'per angle'.
>

## reads-per-sample.4 (claim)

A dilution-series run ranged from 40,927 to 251,419 reads per sample.

- conf: not stated
- class: not stated
- holds: one dilution-series run
- src: karstensControllingContaminantsLowbiomass2019
- trail: MB-01 §3.3, §answers

From the note:

> MB-01:B-0215 [3.3 Reads per sample, and variation between samples] - A dilution-series run ranged from 40,927 to 251,419 reads per sample (Karstens 2019).
>
> MB-01:A-157 [quote: Answers as delivered] A dilution-series run ranged from 40,927 to 251,419 (Karstens 2019).
>

## reads-per-sample.5 (claim)

Three mock runs gave 36,464 to 146,653 read pairs.

- conf: not stated
- class: not stated
- holds: three mock runs
- src: prodanComparingBioinformaticPipelines2020
- trail: MB-01 §3.3

From the note:

> MB-01:B-0216 [3.3 Reads per sample, and variation between samples] - Three mock runs gave 36,464 to 146,653 read pairs (Prodan 2020).
>

## reads-per-sample.6 (claim)

Across 12 public V4 studies, reads per sample varied up to about 100-fold within a study, for example human 10,439 to 422,904 (median 32,452, n = 490), bioethanol 3,690 to 356,027, mice 1,804 to 30,311, soil 46,622 to 58,935 (n = 18) and marine 132,895 to 256,758 (n = 7); these are per-study, not per-run, ranges.

- conf: single (marker)
- class: meas (marker)
- holds: 12 public V4 studies; per study, not per run
- src: schlossRarefactionCurrentlyBest2024 (FT, re-opened; meas; single)
- trail: MB-01 §3.3, §answers, §critic
- rating: "Moderate for reads per sample per study"

From the note:

> MB-01:I-0084 [3.3 Reads per sample, and variation between samples] **Within studies.** Across 12 public V4 studies, reads per sample varied up to about 100-fold within a study (Schloss 2024b) [FT, re-opened; meas; single].
>
> MB-01:B-0217 [3.3 Reads per sample, and variation between samples] Examples: human 10,439 to 422,904 (median 32,452, n = 490), bioethanol 3,690 to 356,027, mice 1,804 to 30,311, soil 46,622 to 58,935 (n = 18), marine 132,895 to 256,758 (n = 7).
>
> MB-01:A-158 [quote: Answers as delivered] In 12 public V4 studies, reads per sample varied within a study by up to about 100-fold; for example human studies ranged from 10,439 to 422,904 and bioethanol studies from 3,690 to 356,027 (Schloss 2024b; per study, not per run).
>
> MB-01:A-172 [quote: Answers as delivered] Moderate for reads per sample per study.
>
> MB-01:A-184 [quote: Answers as delivered] The within-study read range rests mainly on Schloss 2024b Table 1.
>
> MB-01:A-302 [8. Answers in brief] **D3.** Values exist for cycle numbers, for copy-number ranges across genomes, and for per-study read ranges.
>
> MB-01:C-023 [danger: Critic: answers partly supported] - **D3: measured values**: The body supports the values given: documented cycle numbers (the EMP protocol's 35 cycles in triplicate and 240 ng pooling were checked on the live page), copy-number ranges across genomes, per-study and per-run read ranges, and microbial-load ranges.
>

## reads-per-sample.7 (claim)

Schloss attributes the spread of reads per sample to compounding random error when PCR products are pooled.

- conf: not stated
- class: not stated
- holds: 12 public V4 studies
- src: schlossRarefactionCurrentlyBest2024
- trail: MB-01 §3.3

From the note:

> MB-01:B-0218 [3.3 Reads per sample, and variation between samples] Schloss attributes the spread to compounding random error when PCR products are pooled.
>
> MB-01:I-0084 [3.3 Reads per sample, and variation between samples] **Within studies.** Across 12 public V4 studies, reads per sample varied up to about 100-fold within a study (Schloss 2024b) [FT, re-opened; meas; single].
>

## reads-per-sample.8 (claim)

Schloss cites studies reporting that sequencing depth correlates positively with biomass despite normalisation; the two primary studies (one on 101 fish species, one on an equivolumetric protocol) are known only secondarily and were not opened.

- conf: not stated
- class: not stated
- holds: known secondarily via Schloss 2024b
- src: schlossRarefactionCurrentlyBest2024 (SEC)
- trail: MB-01 §3.3, §Adversarial
- limit: access (critic: MB-01:C-111)

From the note:

> MB-01:B-0219 [3.3 Reads per sample, and variation between samples] He cites studies reporting that depth correlates positively with biomass despite normalisation (SEC via Schloss).
>
> MB-01:C-111 [warning: Adversarial critique, full findings] - gap: Within-run read-count variation and the correlation of library size with biomass. Schloss 2024b cites two primary studies on this (Minich et al. 2022 Nat Commun on 101 fish species; Cruz et al. 2021 on an equivolumetric protocol); the review knows them only secondarily and did not open them, although they are directly relevant to D3 and D5.; setting_or_class: Read-count distribution per sample within a run after pooling, versus sample load; direction: D3, D5
>

## reads-per-sample.9 (claim)

The Illumina guide states more than 20 million reads per MiSeq v3 run and more than 100,000 per sample at 96-plex, said to be "sufficient to fully survey the bacterial composition".

- conf: not stated
- class: not stated
- holds: a maker's claim
- src: illumina16SMetagenomicSequencing (maker's claim)
- trail: MB-01 §3.3, §answers

From the note:

> MB-01:B-0220 [3.3 Reads per sample, and variation between samples] **Makers' figures.** More than 20 million reads per MiSeq v3 run, and more than 100,000 per sample at 96-plex, said to be "sufficient to fully survey the bacterial composition" (Illumina guide) [maker's claim].
>
> MB-01:A-159 [quote: Answers as delivered] Makers claim more than 20 million reads per MiSeq v3 run and more than 100,000 per sample at 96-plex (Illumina guide; Emory core protocol).
>
> MB-01:A-182 [quote: Answers as delivered] Protocols and documentation (EMP, Illumina, Emory) are makers' statements.
>

## reads-per-sample.10 (claim)

A core facility protocol gives about 20 million (v3) and about 16 million (v2) reads per run, with more than 100,000 reads per sample recommended.

- conf: not stated
- class: not stated
- holds: a protocol, a maker's statement
- src: emoryAmplicon16SMetagenomics (PROTOCOL)
- trail: MB-01 §3.3, §answers

From the note:

> MB-01:B-0221 [3.3 Reads per sample, and variation between samples] About 20 million (v3) and about 16 million (v2) reads per run, with more than 100,000 per sample recommended (Emory core) [PROTOCOL].
>
> MB-01:A-159 [quote: Answers as delivered] Makers claim more than 20 million reads per MiSeq v3 run and more than 100,000 per sample at 96-plex (Illumina guide; Emory core protocol).
>
> MB-01:A-182 [quote: Answers as delivered] Protocols and documentation (EMP, Illumina, Emory) are makers' statements.
>

## reads-per-sample.11 (claim)

Median Good's coverage ranged from 89.4% (seagrass) to 99.8% (human), and reaching 95% and 99% coverage required about 3 and 101 times the sequences needed for 90%.

- conf: not stated
- class: deriv (note: "(Schloss 2024b) [deriv]")
- holds: 12 public V4 studies
- src: schlossRarefactionCurrentlyBest2024 (deriv)
- trail: MB-01 §3.3

From the note:

> MB-01:B-0222 [3.3 Reads per sample, and variation between samples] **Coverage.** Median Good's coverage ranged from 89.4% (seagrass) to 99.8% (human).
>
> MB-01:B-0223 [3.3 Reads per sample, and variation between samples] Reaching 95% and 99% coverage required about 3 and 101 times the sequences needed for 90% (Schloss 2024b) [deriv].
>
> MB-01:I-0084 [3.3 Reads per sample, and variation between samples] **Within studies.** Across 12 public V4 studies, reads per sample varied up to about 100-fold within a study (Schloss 2024b) [FT, re-opened; meas; single].
>

## reads-per-sample.12 (claim)

No peer-reviewed coefficient of variation of reads per sample within a run after equimolar pooling was found; web search returned only forum posts.

- conf: not stated
- class: search (note: "All three angles searched")
- holds: all three search angles
- src: none (a search result)
- trail: MB-01 §3.3, §answers, §Search record, §Provenance, §critic
- rating: "Absent for the within-run coefficient of variation"
- search: searched, not found (note: "All three angles searched")

From the note:

> MB-01:B-0224 [3.3 Reads per sample, and variation between samples] **Not found.** No peer-reviewed coefficient of variation of reads per sample within a run after equimolar pooling.
>
> MB-01:B-0225 [3.3 Reads per sample, and variation between samples] All three angles searched; web search returned only forum posts.
>
> MB-01:A-160 [quote: Answers as delivered] No peer-reviewed coefficient of variation of reads within a run after equimolar pooling was found.
>
> MB-01:A-173 [quote: Answers as delivered] Absent for the within-run coefficient of variation.
>
> MB-01:A-178 [quote: Answers as delivered] *Not measured:* Not found: measured (not predicted) community-average copy number in soil, water or host samples; a separate value for water; absolute per-cycle efficiencies for 16S primers; within-run read-count CV after equimolar pooling (all three angles searched; web search returned only forum posts); the archaeal copy-number distribution beyond its 1-4 range; abundance-distribution shapes reported separately for water and host-associated 16S data.
>
> MB-01:A-304 [8. Answers in brief] Absolute per-cycle efficiencies and the within-run read CV were not found.
>
> MB-01:B-0017 [info: Provenance] Not found by any route: within-run CV of reads per sample; absolute per-cycle 16S efficiencies; measured (not predicted) community copy number by environment; 16S-specific index hopping on patterned flow cells; overdispersion fitted to 16S technical replicates; an independent microbial benchmark of coverage-based standardisation; abundance-distribution shapes reported separately for water and host.
>
> MB-01:B-0378 [Search record] - Within-run read-count CV after equimolar pooling (all angles; web search found only forums).
>
> MB-01:C-029 [danger: Critic: answers partly supported] Absent: measured community copy number, a within-run read-count coefficient of variation, absolute per-cycle efficiencies, and per-environment abundance-distribution shapes for water and for host samples.
>

## microbial-load.1 (claim)

Microbial load differed up to tenfold among healthy human individuals' faeces.

- conf: repl (marker)
- class: meas (marker)
- holds: human faeces
- src: vandeputteQuantitativeMicrobiomeProfiling2017 (AB; meas; repl)
- trail: MB-01 §3.5, §answers

From the note:

> MB-01:I-0089 [3.5 Microbial load (context for D5)] - Human faeces: up to tenfold differences in load among healthy individuals (Vandeputte 2017) [AB; meas; repl].
>
> MB-01:A-167 [quote: Answers as delivered] Microbial loads: up to tenfold among healthy human faeces (Vandeputte 2017, abstract); 27-fold among Antarctic seawater stations (Lin 2019); more than six orders of magnitude across mouse gut sites (Barlow 2020).
>
> MB-01:C-023 [danger: Critic: answers partly supported] - **D3: measured values**: The body supports the values given: documented cycle numbers (the EMP protocol's 35 cycles in triplicate and 240 ng pooling were checked on the live page), copy-number ranges across genomes, per-study and per-run read ranges, and microbial-load ranges.
>

## microbial-load.2 (claim)

Prokaryote load in Antarctic seawater differed 27-fold among stations.

- conf: single (marker)
- class: meas (marker)
- holds: Antarctic seawater
- src: linTowardsQuantitativeMicrobiome2019 (FT; meas; single)
- trail: MB-01 §3.5, §answers

From the note:

> MB-01:I-0090 [3.5 Microbial load (context for D5)] - Antarctic seawater: 27-fold among stations for prokaryotes (Lin 2019) [FT; meas; single].
>
> MB-01:A-167 [quote: Answers as delivered] Microbial loads: up to tenfold among healthy human faeces (Vandeputte 2017, abstract); 27-fold among Antarctic seawater stations (Lin 2019); more than six orders of magnitude across mouse gut sites (Barlow 2020).
>

## microbial-load.3 (claim)

Microbial load in the mouse gut spanned more than six orders of magnitude across sites.

- conf: single (marker)
- class: meas (marker)
- holds: mouse gut sites
- src: barlowQuantitativeSequencingFramework2020 (FT; meas; single)
- trail: MB-01 §3.5, §answers

From the note:

> MB-01:I-0091 [3.5 Microbial load (context for D5)] - Mouse gut: more than six orders of magnitude across sites (Barlow 2020) [FT; meas; single].
>
> MB-01:A-167 [quote: Answers as delivered] Microbial loads: up to tenfold among healthy human faeces (Vandeputte 2017, abstract); 27-fold among Antarctic seawater stations (Lin 2019); more than six orders of magnitude across mouse gut sites (Barlow 2020).
>

## abundance-distribution.1 (claim)

For 24 grassland soils, the best-fitting abundance distributions the review reports (exponential or inverse gamma) are in supplementary Table S3; the main text does not state which distributions won, and they were not verified.

- conf: single (marker)
- class: model (marker)
- holds: 24 grassland soils
- src: zhouRandomSamplingProcess2013 (FT; model; single)
- trail: MB-01 §3.4, §answers, §critic, §Adversarial
- limit: access (critic: MB-01:C-079)

From the note:

> MB-01:I-0085 [3.4 Shape of taxon abundance distributions] - In 24 grassland soils, the best-fitting distributions were exponential or inverse gamma (Zhou 2013) [FT; model; single].
>
> MB-01:A-161 [quote: Answers as delivered] Shape of abundance distributions.
>
> MB-01:A-162 [quote: Answers as delivered] Soil: exponential or inverse-gamma fits to 24 grassland soils (Zhou 2013, modelled).
>
> MB-01:A-186 [quote: Answers as delivered] Soil SAD shape rests on Zhou 2013 and Haegeman 2013.
>
> MB-01:C-026 [danger: Critic: answers partly supported] The soil 'exponential or inverse gamma' best fits are in Zhou 2013's supplementary Table S3; the main text does not state them and they were not verified.
>
> MB-01:C-077 [warning: Adversarial critique, full findings] - Zhou 2013 (FT): 'in 24 grassland soils, the best-fitting distributions were exponential or inverse gamma'.
>
> MB-01:C-078 [warning: Adversarial critique, full findings] The best-fit results are in supplementary Table S3; the main text does not state which distributions won.
>
> MB-01:C-079 [warning: Adversarial critique, full findings] The claim rests on unread or unshown supplementary material.
>

## abundance-distribution.2 (claim)

In a Brazil soil, 26,079 reads and 2,880 observed species were fitted equally well by communities of 10^4, 10^5 and 10^6 species, so the tail of the distribution cannot be identified from sample data; these figures rest on a full text that was not openly retrievable and could not be confirmed.

- conf: repl (marker)
- class: model (marker)
- holds: one Brazil soil
- src: haegemanRobustEstimationMicrobial2013 (FT; model; repl)
- trail: MB-01 §3.4, §answers, §critic, §Adversarial
- limit: access (critic: MB-01:C-028)

From the note:

> MB-01:I-0086 [3.4 Shape of taxon abundance distributions] - In the Brazil soil, 26,079 reads and 2,880 observed species were fitted equally well by communities of 10^4, 10^5 and 10^6 species, so the tail cannot be identified from sample data (Haegeman 2013) [FT; model; repl].
>
> MB-01:A-163 [quote: Answers as delivered] One Brazilian soil was fitted equally well by communities of 10^4, 10^5 and 10^6 species, so the tail cannot be identified from the data (Haegeman 2013).
>
> MB-01:C-028 [danger: Critic: answers partly supported] Haegeman 2013's Brazil-soil figures rest on a full text that was not openly retrievable.
>
> MB-01:C-076 [warning: Adversarial critique, full findings] Figures needing the body (Zhou 2011's 0.06 to 5.34% spike range and its 13.1%/5.9% discussion values; Kozich's 9,913 and 2,454 reads; Haegeman's 26,079 reads and 2,880 species; Lin 2019's r2 0.19 and 0.61) could not be confirmed, and the review shows no evidence of full-text reading beyond 'per angle'.
>

## abundance-distribution.3 (claim)

After copy-number correction, rank-abundance distributions from ocean and human skin fit a lognormal better, in a single study that pools ocean and skin into one item and whose own simulations assumed a lognormal.

- conf: single (critic: MB-01:C-027)
- class: not stated
- holds: ocean and human skin, pooled
- src: kembelIncorporating16SGene2012
- trail: MB-01 §3.4, §answers, §critic, §Adversarial

From the note:

> MB-01:B-0226 [3.4 Shape of taxon abundance distributions] **Water and hosts.** After copy-number correction, rank-abundance distributions from human skin and ocean fit a lognormal better (Kembel 2012).
>
> MB-01:A-164 [quote: Answers as delivered] Water and hosts: copy-corrected ocean and skin rank-abundance data fitted a lognormal better (Kembel 2012).
>
> MB-01:C-027 [danger: Critic: answers partly supported] The 'water and hosts' item is a single study (Kembel 2012) that pools ocean and skin into one item; the same paper's simulations assumed a lognormal.
>
> MB-01:C-134 [warning: Adversarial critique, full findings] - D3 abundance distributions: 'Water and hosts' are answered together from one study (Kembel 2012, ocean plus human skin), so the brief's separate water and host cases are folded into one item.
>

## abundance-distribution.4 (claim)

Lognormal dynamics best explained microbial abundance distributions across more than 20,000 samples; the abstract gives no per-environment breakdown, so soil is not reported separately.

- conf: single (marker)
- class: model (marker)
- holds: cross-environment compilation including soils; abstract only
- src: shoemakerMacroecologicalTheoryMicrobial2017 (AB; model; single)
- trail: MB-01 §3.4, §answers, MB-02 §D3.1, §answers

From the note:

> MB-01:I-0087 [3.4 Shape of taxon abundance distributions] - Lognormal dynamics best explained abundance distributions across more than 20,000 samples (Shoemaker 2017) [AB; model; single].
>
> MB-01:B-0227 [3.4 Shape of taxon abundance distributions] **Across environments, not separated.**
>
> MB-01:B-0228 [3.4 Shape of taxon abundance distributions] No per-environment breakdown in the abstract.
>
> MB-01:A-165 [quote: Answers as delivered] Across environments: lognormal across more than 20,000 samples (Shoemaker 2017, abstract only, no per-environment breakdown).
>
> MB-02:B-0236 [D3.1 How abundance is distributed among soil taxa, by measurement] **Cross-environment compilations, soils included.** Lognormal dynamics best explained abundance distributions in over 20,000 samples [70, AB].
>
> MB-02:B-0238 [D3.1 How abundance is distributed among soil taxa, by measurement] These abstracts do not report soil separately.
>
> MB-02:A-087 [quote: Answers as delivered] Cross-environment amplicon compilations, which include soils but do not report them separately in the abstracts read, found lognormal dynamics best explained microbial abundance distributions [70,71].
>

## abundance-distribution.5 (claim)

A dominance scaling law held across about 35,000 sites.

- conf: not stated
- class: not stated
- holds: a cross-environment compilation; the abstract does not report soil separately
- src: loceyScalingLawsPredict2016 (AB)
- trail: MB-02 §D3.1

From the note:

> MB-02:B-0237 [D3.1 How abundance is distributed among soil taxa, by measurement] A dominance scaling law held across about 35,000 sites [71, AB].
>
> MB-02:B-0238 [D3.1 How abundance is distributed among soil taxa, by measurement] These abstracts do not report soil separately.
>
> MB-02:B-0236 [D3.1 How abundance is distributed among soil taxa, by measurement] **Cross-environment compilations, soils included.** Lognormal dynamics best explained abundance distributions in over 20,000 samples [70, AB].
>

## abundance-distribution.6 (claim)

Mean abundances across taxa were lognormal "for all the data sets considered"; per-biome results are in supplementary figures that were not read.

- conf: single (marker)
- class: model (marker)
- holds: all the data sets considered; partly re-opened
- src: grilliMacroecologicalLawsDescribe2020 (FT, partly re-opened; model; single)
- trail: MB-01 §3.4, §answers

From the note:

> MB-01:I-0088 [3.4 Shape of taxon abundance distributions] - Mean abundances across taxa were lognormal "for all the data sets considered", and each taxon's abundance across communities was gamma-distributed with variance proportional to the squared mean (Grilli 2020) [FT, partly re-opened; model; single].
>
> MB-01:B-0229 [3.4 Shape of taxon abundance distributions] Per-biome results are in supplementary figures that were not read.
>
> MB-01:A-166 [quote: Answers as delivered] Mean abundances were lognormal and abundance fluctuations gamma-distributed across biomes (Grilli 2020; per-biome figures in supplements not read).
>

## abundance-distribution.7 (claim)

Soil abundance-distribution shape conflicts between exponential or inverse gamma fits and lognormal ones, but these use different fitting targets, so the conflict is only partial; one analysis argues the tail is not identifiable from sample data at all.

- conf: cont (note: "Conflicts")
- class: not stated
- holds: soil
- src: zhouRandomSamplingProcess2013, shoemakerMacroecologicalTheoryMicrobial2017, grilliMacroecologicalLawsDescribe2020, haegemanRobustEstimationMicrobial2013
- trail: MB-01 §answers

From the note:

> MB-01:A-175 [quote: Answers as delivered] *Conflicts:* Soil SAD shape: exponential or inverse gamma (Zhou 2013) versus lognormal (Shoemaker 2017; Grilli 2020).
>
> MB-01:A-176 [quote: Answers as delivered] These use different fitting targets, so the conflict is only partial; Haegeman 2013 argues the tail is not identifiable from sample data at all.
>

## abundance-distribution.8 (claim)

Abundance-distribution shapes split by environment are weaker than presented, because the field-wide sources do not separate soil, water and host.

- conf: not stated
- class: not stated
- holds: soil, water and host samples
- src: none (the reviewer's and critic's assessment)
- trail: MB-01 §answers, §critic, §8. Answers
- rating: "Weak for abundance-distribution shapes split by environment"

From the note:

> MB-01:A-174 [quote: Answers as delivered] Weak for abundance-distribution shapes split by environment, because the field-wide sources do not separate soil, water and host.
>
> MB-01:A-305 [8. Answers in brief] Abundance-distribution shapes are mostly not split by environment.
>
> MB-01:C-025 [danger: Critic: answers partly supported] (2) Abundance-distribution shapes split by environment are weaker than presented.
>

## abundance-distribution.9 (claim)

Abundance-distribution shapes reported separately for water and for host-associated 16S data were not found, beyond the copy-correction fits for ocean and skin, although per-biome supplementary figures and an unread full text exist.

- conf: not stated
- class: search (note: "no angle located such a breakdown")
- holds: water and host-associated 16S data
- src: grilliMacroecologicalLawsDescribe2020, shoemakerMacroecologicalTheoryMicrobial2017
- trail: MB-01 §3.4, §answers, §Search record, §Provenance, §critic, §Adversarial
- search: searched, not found (note: "no angle located such a breakdown")

From the note:

> MB-01:B-0230 [3.4 Shape of taxon abundance distributions] **Not found.** Abundance-distribution shapes reported separately for water and for host-associated 16S data, beyond the copy-correction fits in Kembel 2012.
>
> MB-01:A-178 [quote: Answers as delivered] *Not measured:* Not found: measured (not predicted) community-average copy number in soil, water or host samples; a separate value for water; absolute per-cycle efficiencies for 16S primers; within-run read-count CV after equimolar pooling (all three angles searched; web search returned only forum posts); the archaeal copy-number distribution beyond its 1-4 range; abundance-distribution shapes reported separately for water and host-associated 16S data.
>
> MB-01:B-0017 [info: Provenance] Not found by any route: within-run CV of reads per sample; absolute per-cycle 16S efficiencies; measured (not predicted) community copy number by environment; 16S-specific index hopping on patterned flow cells; overdispersion fitted to 16S technical replicates; an independent microbial benchmark of coverage-based standardisation; abundance-distribution shapes reported separately for water and host.
>
> MB-01:B-0385 [Search record] - Abundance-distribution shapes split by water and host (no angle located such a breakdown).
>
> MB-01:C-029 [danger: Critic: answers partly supported] Absent: measured community copy number, a within-run read-count coefficient of variation, absolute per-cycle efficiencies, and per-environment abundance-distribution shapes for water and for host samples.
>
> MB-01:C-114 [warning: Adversarial critique, full findings] - gap: Abundance-distribution shapes by environment. Grilli 2020's per-biome supplementary figures and Shoemaker 2017's full text were not read, so per-environment shapes for water and host samples are absent although the sources exist.; setting_or_class: Species abundance distributions in marine/freshwater and host-associated 16S datasets; direction: D3
>

## abundance-distribution.10 (claim)

In bulk-soil global amplicon datasets, a small minority of taxa carries a large share of reads and most taxa are rare; this qualitative shape is replicated across global amplicon datasets and older clone and reassociation studies.

- conf: repl (note: "replicated across global amplicon datasets")
- class: not stated
- holds: bulk soil, amplicon reads
- src: delgadobaquerizoGlobalAtlasDominant2018, bickelChosenFewVariations2021
- trail: MB-02 §critic, §answers
- rating: "Moderate for the qualitative shape"

From the note:

> MB-02:C-039 [danger: Critic: answers partly supported] **D3 (a) soil abundance distributions by measurement**: Amplicon reads, bulk soil: in the global datasets found, a small minority of taxa carries a large share of reads.
>
> MB-02:A-081 [quote: Answers as delivered] **D3, case (a): how abundance is distributed among soil bacterial and archaeal taxa, by measurement type**: Amplicon reads (bulk soil, global): a small fraction of taxa holds a large share of reads. 511 of 25,224 phylotypes (2%) that were both top-10% abundant and present in over half of 237 soils accounted for on average 41% of 16S reads (about 20% in tropical forests) [60].
>
> MB-02:A-090 [quote: Answers as delivered] *Strength:* Moderate for the qualitative shape (few taxa hold much of the reads, most taxa are rare): replicated across global amplicon datasets and older clone and reassociation studies.
>
> MB-02:B-0219 [D3.1 How abundance is distributed among soil taxa, by measurement] **Amplicon reads, bulk soil.**
>

## abundance-distribution.11 (claim)

Across 237 soils, per-sample richness ranged from 774 to 2,869 phylotypes, and 511 of 25,224 phylotypes (2%), defined as dominant jointly by abundance (top 10% by share of reads) and ubiquity (present in more than half of the soils), accounted on average for 41% of 16S reads per sample, more than half in arid forests and only about 20% in tropical forests.

- conf: not stated
- class: not stated
- holds: 237 soils, bulk soil, amplicon reads; per-sample mean
- src: delgadobaquerizoGlobalAtlasDominant2018 (FT)
- trail: MB-02 §D3.1, §D2.3, §answers, §critic

From the note:

> MB-02:B-0220 [D3.1 How abundance is distributed among soil taxa, by measurement] - **Delgado-Baquerizo et al. 2018** [60, FT]: per-sample richness ranged from 774 to 2,869 phylotypes across 237 soils. 511 of 25,224 phylotypes (2%), defined as dominant, accounted on average for 41% of 16S reads, more than half in arid forests and only about 20% in tropical forests.
>
> MB-02:B-0183 [D2.3 Regional and global distribution] In soil, "dominant" has been defined jointly: in the top 10% of phylotypes by share of 16S reads and present in more than half of 237 soils [60, FT].
>
> MB-02:A-081 [quote: Answers as delivered] **D3, case (a): how abundance is distributed among soil bacterial and archaeal taxa, by measurement type**: Amplicon reads (bulk soil, global): a small fraction of taxa holds a large share of reads. 511 of 25,224 phylotypes (2%) that were both top-10% abundant and present in over half of 237 soils accounted for on average 41% of 16S reads (about 20% in tropical forests) [60].
>
> MB-02:C-041 [danger: Critic: answers partly supported] In Delgado-Baquerizo et al. 2018, 2% of phylotypes, defined jointly by abundance and ubiquity, accounted on average for 41% of reads per sample.
>

## abundance-distribution.12 (claim)

Across 844 soils (318 sites, 90-bp V4 ASVs), 0.4% of ASVs were classed common on the globally pooled rank-abundance distribution and held about 58% of pooled relative abundance, while the 99.6% classed rare held 42%.

- conf: not stated
- class: not stated
- holds: 844 soils, pooled global relative abundance
- src: bickelChosenFewVariations2021 (FT)
- trail: MB-02 §D3.1, §answers, §critic

From the note:

> MB-02:B-0221 [D3.1 How abundance is distributed among soil taxa, by measurement] - **Bickel and Or 2021** [61, FT]: across 844 soils (318 sites, 90-bp V4 ASVs), 0.4% of taxa were common and the 99.6% classed rare held 42% of pooled relative abundance.
>
> MB-02:A-082 [quote: Answers as delivered] With a data-driven threshold across 844 soils, 0.4% of 90-bp ASVs were classed common and the remaining 99.6% held 42% of relative abundance; dry soils had more even distributions [61].
>
> MB-02:A-094 [quote: Answers as delivered] Share held by the dominant fraction depends on definition: about 41% for a top-10%-and-ubiquitous definition [60] versus about 58% for the 0.4% common class [61]; these are not comparable figures because the definitions and denominators differ.
>
> MB-02:C-042 [danger: Critic: answers partly supported] In Bickel and Or 2021, 0.4% of ASVs, classed common on the globally pooled rank-abundance distribution, held about 58% of pooled relative abundance.
>

Not found in the cited text (where to look, not what is wrong): holds: global

## abundance-distribution.13 (claim)

The dominant-fraction shares of the two global soil datasets (2% holding about 41% of reads per sample, and 0.4% holding about 58% of pooled relative abundance) use different definitions and denominators and must not be combined.

- conf: not stated
- class: not stated
- holds: two global soil amplicon datasets
- src: delgadobaquerizoGlobalAtlasDominant2018, bickelChosenFewVariations2021
- trail: MB-02 §D3.1, §answers, §critic

From the note:

> MB-02:B-0226 [D3.1 How abundance is distributed among soil taxa, by measurement] The dominant shares in [60] and [61] use different definitions and denominators and are not combined here.
>
> MB-02:A-094 [quote: Answers as delivered] Share held by the dominant fraction depends on definition: about 41% for a top-10%-and-ubiquitous definition [60] versus about 58% for the 0.4% common class [61]; these are not comparable figures because the definitions and denominators differ.
>
> MB-02:C-040 [danger: Critic: answers partly supported] The two figures must be kept apart.
>
> MB-02:C-041 [danger: Critic: answers partly supported] In Delgado-Baquerizo et al. 2018, 2% of phylotypes, defined jointly by abundance and ubiquity, accounted on average for 41% of reads per sample.
>
> MB-02:C-042 [danger: Critic: answers partly supported] In Bickel and Or 2021, 0.4% of ASVs, classed common on the globally pooled rank-abundance distribution, held about 58% of pooled relative abundance.
>

Not found in the cited text (where to look, not what is wrong): holds: global; holds: soil; holds: amplicon; holds: datasets

## abundance-distribution.14 (claim)

Drier soils had more even abundance distributions, and the ratio of rare to common richness declined with rainfall frequency (Pearson r = -0.41, n = 318).

- conf: not stated
- class: not stated
- holds: 318 sites
- src: bickelChosenFewVariations2021 (FT)
- trail: MB-02 §D3.1, §answers

From the note:

> MB-02:B-0222 [D3.1 How abundance is distributed among soil taxa, by measurement] Drier soils had more even distributions.
>
> MB-02:B-0223 [D3.1 How abundance is distributed among soil taxa, by measurement] The ratio of rare to common richness declined with rainfall frequency (Pearson r = -0.41, n = 318).
>
> MB-02:A-082 [quote: Answers as delivered] With a data-driven threshold across 844 soils, 0.4% of 90-bp ASVs were classed common and the remaining 99.6% held 42% of relative abundance; dry soils had more even distributions [61].
>

## abundance-distribution.15 (claim)

Across 146 soils, archaeal reads averaged 2% of 16S reads (0 to over 10%), and two Thaumarchaeota (then Crenarchaeota) phylotypes made up over 70% of archaeal sequences; this rests on one abstract-only study of 2010-era 454 data.

- conf: single (critic: MB-02:C-044)
- class: not stated
- holds: 146 soils, 454
- src: batesExaminingGlobalDistribution2011 (AB)
- trail: MB-02 §D3.1, §answers, §critic, §Adversarial

From the note:

> MB-02:B-0224 [D3.1 How abundance is distributed among soil taxa, by measurement] - **Archaea** [64, AB]: across 146 soils, archaeal reads averaged 2% of 16S reads (0 to over 10%).
>
> MB-02:B-0225 [D3.1 How abundance is distributed among soil taxa, by measurement] Two Thaumarchaeota (then Crenarchaeota) phylotypes made up over 70% of archaeal sequences.
>
> MB-02:A-083 [quote: Answers as delivered] For archaea across 146 soils, archaeal reads averaged 2% of 16S reads and two Thaumarchaeota (then Crenarchaeota) phylotypes accounted for over 70% of archaeal sequences [64].
>
> MB-02:A-099 [quote: Answers as delivered] Archaeal figures rest on Bates et al. 2011 [64] alone.
>
> MB-02:C-044 [danger: Critic: answers partly supported] Two phylotypes made up more than 70% of archaeal sequences across 146 soils (one study, abstract only).
>
> MB-02:C-091 [warning: Adversarial critique, full findings] - D3(a): 'two phylotypes dominate soil archaea' (more than 70% of archaeal sequences) rests on Bates et al. 2011 [64, AB] alone (2010-era 454 data, 146 soils). It is stated in the D3(a) answer as a general finding.
>

## abundance-distribution.16 (claim)

By DNA reassociation kinetics, which measure whole-community DNA rather than reads or cells, a power law described the soil abundance distribution best, implying over a million distinct genomes in a pristine soil, and metal pollution cut diversity by over 99.9%; this is the main contrary result on the shape of the distribution.

- conf: not stated
- class: not stated
- holds: whole-community DNA; a pristine soil
- src: gansComputationalImprovementsReveal2005 (AB)
- trail: MB-02 §D3.1, §answers

From the note:

> MB-02:B-0233 [D3.1 How abundance is distributed among soil taxa, by measurement] **DNA reassociation kinetics.** This measures whole-community DNA, neither reads nor cells.
>
> MB-02:B-0234 [D3.1 How abundance is distributed among soil taxa, by measurement] A power law fitted best, implying over a million distinct genomes in a pristine soil; metal pollution cut diversity by over 99.9% [66, AB].
>
> MB-02:B-0235 [D3.1 How abundance is distributed among soil taxa, by measurement] This is the main contrary result on the shape of the distribution.
>
> MB-02:A-085 [quote: Answers as delivered] DNA reassociation kinetics (whole community DNA, not reads or cells): a power law best described the abundance distribution, with over one million genomes in a pristine soil [66].
>
> MB-02:A-098 [quote: Answers as delivered] Removing Gans et al. 2005 [66] removes the power-law side of the functional-form conflict.
>

