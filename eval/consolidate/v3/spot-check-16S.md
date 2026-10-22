# Spot-check: 16S amplicon sequencing from sample to count table

- Knowledge note: `Topics/Biology/Research/Knowledge/16S amplicon sequencing from sample to count table.md`
- Drawn: 20 of the 460 claims and do-not-say entries, `random.Random(20261021).sample` over them in file order (`kn.py spotcheck --seed 20261021`)
- Entries: workflow-steps.1, sampling-storage.4, extraction.1, primers.5, copy-number-correction.8, copy-number-correction.15, denoising-clustering.6, workflow-bias.2, workflow-bias.4, bias-consistency.1, bias-consistency.4, abundance-distribution.22, technical-variation.7, beta-diversity.3, rarefying.1, coverage-standardisation.3, richness-estimators.6, compositional-analysis.3, absolute-quantification.4, dns.27

Judge each entry only against the note text quoted under it, as the checker does: does the entry say what that text says? Not whether the research is right. The trail is there if you want the context; the checker never sees it. Mark `ok`, or one or more faults:

- `stronger`: the entry is firmer than its text: standing raised, a hedge dropped, scope widened (one setting stated as general), a single study stated as a pattern.
- `conf`: `conf`, `class` or `limit` gives a value its text does not state (a standing inferred from tone, the basis quoted does not say it, or `limit: access` where the text gives no access reason; abstract only, not obtained, second-hand and "not read in the original" are access reasons). `not stated` is always acceptable.
- `numbers`: a figure differs from its text, lost its definition or denominator, or figures from different sources were combined.
- `absent`: the entry says something its quoted text does not contain.
- `critic`: the quoted critique corrects the claim, or a source's label in `src`, and the entry keeps the uncorrected version.
- `merged`: two cases the text keeps apart are folded into one entry.
- `holds`: the setting in `holds` is missing or differs from the text.

## 1. workflow-steps.1 (claim)

Twelve steps between a sample and a table of taxon counts are documented, each with named alternatives; what the steps are is not in conflict, while the recommended choice within a step is disputed.

- conf: not stated
- class: not stated
- holds: protocols, software documentation and benchmarks; the critic: the body supports the twelve-step description and the alternatives listed, mostly from full-text protocols, documentation and benchmarks, with makers' statements labelled as such; the procedural descriptions would not change if any single source were removed
- src: none (the reviewer's synthesis of the step-by-step evidence)
- trail: MB-01 §answers, §2. Steps, §critic
- rating: "Strong for the existence of these choices and the alternatives used"
- trail links: [[Topics/Biology/Research/Results/From sample to count table in 16S rRNA gene amplicon sequencing where counts depart from community composition, what the workflow's quantities measure, and how samples with unequal depth or load are compared. A literature review]] (callout: Answers as delivered), [[Topics/Biology/Research/Results/From sample to count table in 16S rRNA gene amplicon sequencing where counts depart from community composition, what the workflow's quantities measure, and how samples with unequal depth or load are compared. A literature review#2. Steps from sample to table (D1) and departures from the sampled community (D2)]], [[Topics/Biology/Research/Results/From sample to count table in 16S rRNA gene amplicon sequencing where counts depart from community composition, what the workflow's quantities measure, and how samples with unequal depth or load are compared. A literature review]] (callout: Critic: answers partly supported)

From the note:

> MB-01:A-001 [quote: Answers as delivered] **descriptive; per step**: Twelve steps are documented, each with named alternatives.
>
> MB-01:A-018 [quote: Answers as delivered] *Strength:* Strong for the existence of these choices and the alternatives used, which are documented in protocols, software documentation and benchmarks.
>
> MB-01:A-020 [quote: Answers as delivered] *Conflicts:* No conflict over what the steps are.
>
> MB-01:A-021 [quote: Answers as delivered] Within steps, the recommended choice is disputed.
>
> MB-01:A-032 [quote: Answers as delivered] *Single-source sensitivity:* The procedural descriptions would not change if any single source were removed.
>
> MB-01:A-294 [8. Answers in brief] **D1.** Twelve steps, each with documented alternatives (section 2).
>
> MB-01:C-001 [danger: Critic: answers partly supported] - **D1: steps and choices**: The body supports the twelve-step description and the alternatives listed for each step.
>
> MB-01:C-002 [danger: Critic: answers partly supported] Most of it comes from full-text protocols, documentation and benchmarks; makers' statements are labelled as such.
>

**Verdict:** ok

**Why:** text distiles the quotes

## 2. sampling-storage.4 (claim)

FTA cards produced a systematic shift that could be detrended, the one storage effect shown to be consistent across samples; for the other preservation methods consistency was not measured.

- conf: not stated
- class: not stated
- holds: faeces (Song 2016)
- src: songPreservationMethodsDiffer2016
- trail: MB-01 §2.1, §answers
- trail links: [[Topics/Biology/Research/Results/From sample to count table in 16S rRNA gene amplicon sequencing where counts depart from community composition, what the workflow's quantities measure, and how samples with unequal depth or load are compared. A literature review#2.1 Field sampling, preservation and storage]], [[Topics/Biology/Research/Results/From sample to count table in 16S rRNA gene amplicon sequencing where counts depart from community composition, what the workflow's quantities measure, and how samples with unequal depth or load are compared. A literature review]] (callout: Answers as delivered)

From the note:

> MB-01:B-0082 [2.1 Field sampling, preservation and storage] FTA cards produced a systematic shift that could be detrended, which is the one storage effect shown to be consistent across samples.
>
> MB-01:A-040 [quote: Answers as delivered] Consistency: FTA cards gave a systematic shift that could be removed; for the other methods consistency was not measured.
>
> MB-01:B-0051 [2. Steps from sample to table (D1) and departures from the sampled community (D2)] Soil storage shifts are small relative to between-soil differences | Smaller | FTA cards: systematic, removable shift.
>
> MB-01:B-0052 [2. Steps from sample to table (D1) and departures from the sampled community (D2)] Otherwise not measured | Song 2016; Rubin 2013 |
>

**Verdict:** ok

**Why:** text distiles the quotes

## 3. extraction.1 (claim)

Extraction choices include the kit, bead-beating intensity, plate or single tube, and whether relic DNA is removed with PMA or DNase.

- conf: not stated
- class: not stated
- holds: the extraction studies below
- src: albertsenBackBasicsInfluence2015, minichQuantifyingUnderstandingWelltowell2019, cariniRelicDNAAbundant2016, lennonHowWhereRelic2018
- trail: MB-01 §answers
- trail links: [[Topics/Biology/Research/Results/From sample to count table in 16S rRNA gene amplicon sequencing where counts depart from community composition, what the workflow's quantities measure, and how samples with unequal depth or load are compared. A literature review]] (callout: Answers as delivered)

From the note:

> MB-01:A-004 [quote: Answers as delivered] DNA extraction: kit, bead-beating intensity, plate or single tube, and whether relic DNA is removed with PMA or DNase (Albertsen 2015; Minich 2019; Carini 2016; Lennon 2018).
>

**Verdict:** ok

**Why:** text distiles the quotes

## 4. primers.5 (claim)

On marine clone mocks, 515F-Y/926R fit expected composition with r2 = 0.95, against about 0.5 for 515F-Y/806R, and even perfectly matched primers showed preferential amplification.

- conf: not stated
- class: not stated
- holds: marine clone mocks; abstract only
- src: paradaEveryBaseMatters2016
- trail: MB-01 §2.3
- trail links: [[Topics/Biology/Research/Results/From sample to count table in 16S rRNA gene amplicon sequencing where counts depart from community composition, what the workflow's quantities measure, and how samples with unequal depth or load are compared. A literature review#2.3 Primers and gene region]]

From the note:

> MB-01:B-0103 [2.3 Primers and gene region] On marine clone mocks, 515F-Y/926R fit expected composition with r2 = 0.95, against about 0.5 for 515F-Y/806R.
>
> MB-01:B-0106 [2.3 Primers and gene region] Even perfectly matched primers showed preferential amplification.
>

**Verdict:** ok

**Why:** matches quotes near exact

## 5. copy-number-correction.8 (claim)

Correction improves fit to simulated truth (Kembel 2012; Gao and Wu 2023).

- conf: not stated
- class: not stated
- holds: simulations
- src: kembelIncorporating16SGene2012, gaoAccounting16SRRNA2023
- trail: MB-02 §critic, §answers
- trail links: [[Topics/Biology/Research/Results/16S rRNA gene copies per genome and per cell, abundance and rarity terms, and abundance in soil. A literature review]] (callout: Critic: answers partly supported), [[Topics/Biology/Research/Results/16S rRNA gene copies per genome and per cell, abundance and rarity terms, and abundance in soil. A literature review]] (callout: Answers as delivered)

From the note:

> MB-02:C-020 [danger: Critic: answers partly supported] **D1 (c) copy number versus reads; correction**: Supported, with corrections.
>
> MB-02:C-021 [danger: Critic: answers partly supported] Prediction accuracy declines with distance to sequenced genomes [30, FT], and correction improves fit to simulated truth [28,33].
>
> MB-02:A-141 [Answers] Correction improves fit to simulated truth and some mocks [28,29,33] but not DNA mocks [32] or most mock tests in one preprint [31].
>

**Verdict:** bad

**Why:** misses information, nuances aren't captured 

## 6. copy-number-correction.15 (claim)

Applying copy-number (and genome-size) correction to a forest soil changed Acidobacteria from 50.1% of 16S sequences to an estimated 66.0% of genomes, Actinobacteria from 11.8% to 7.6% and Firmicutes from 3.2% to 1.1%; this is the only soil example of correction size, and it depends on the imprecise low Acidobacteria copy-number mean.

- conf: single (note: "SINGLE SOURCE for soil")
- class: deriv (marker)
- holds: one forest soil
- src: vetrovskyVariability16SRRNA2013 (FT; deriv; repl)
- trail: MB-01 §2.5, MB-02 §D1.4, §answers, §critic
- trail links: [[Topics/Biology/Research/Results/From sample to count table in 16S rRNA gene amplicon sequencing where counts depart from community composition, what the workflow's quantities measure, and how samples with unequal depth or load are compared. A literature review#2.5 16S rRNA gene copy number]], [[Topics/Biology/Research/Results/16S rRNA gene copies per genome and per cell, abundance and rarity terms, and abundance in soil. A literature review#D1.4 Copy number and read-based abundance]], [[Topics/Biology/Research/Results/16S rRNA gene copies per genome and per cell, abundance and rarity terms, and abundance in soil. A literature review]] (callout: Answers as delivered), [[Topics/Biology/Research/Results/16S rRNA gene copies per genome and per cell, abundance and rarity terms, and abundance in soil. A literature review]] (callout: Critic: answers partly supported)

From the note:

> MB-01:I-0035 [2.5 16S rRNA gene copy number] **Effect on proportions.** Applying copy-number correction to forest soil changed Acidobacteria from 50.1% of sequences to an estimated 66.0% of genomes, and Firmicutes from 3.2% to 1.1% (Vetrovsky and Baldrian 2013) [FT; deriv; repl].
>
> MB-02:B-0152 [D1.4 Copy number and read-based abundance] - **Soil.** In a forest soil, correcting with copy number and genome size moved Acidobacteria from 50.1% of 16S sequences to an estimated 66.0% of genomes, Actinobacteria from 11.8% to 7.6% and Firmicutes from 3.2% to 1.1% [6, FT, derived].
>
> MB-02:B-0153 [D1.4 Copy number and read-based abundance] This is SINGLE SOURCE for soil.
>
> MB-02:A-045 [quote: Answers as delivered] Effects on ecological conclusions are mixed: correction changed the most abundant OTU in about 20% (human) and 31% (Earth Microbiome Project) of communities but left PERMANOVA variance explained essentially unchanged [33]; it changed human body-site clustering but not ocean clustering [28]; it changed enterotype number from two to three [29]; in a forest soil example Acidobacteria rose from 50.1% of sequences to an estimated 66.0% of genomes [6].
>
> MB-02:A-059 [quote: Answers as delivered] The only soil example of correction size rests on Vetrovsky and Baldrian 2013 [6].
>
> MB-02:C-005 [danger: Critic: answers partly supported] These soil-relevant low values are imprecise, and the soil correction example (Acidobacteria 50.1% to 66.0%) depends on them.
>

**Verdict:** holds

**Why:** captures the relevant information. quotes numbers correctly, misses the  repeat warnings about low source material count

## 7. denoising-clustering.6 (claim)

The DADA2 developers report 93 output sequences on a 57-strain mock, against 249 for mothur and 378 for QIIME.

- conf: not stated
- class: meas (marker)
- holds: one 57-strain mock; developer claim
- src: callahanDADA2HighresolutionSample2016 (FT; meas; developer claim)
- trail: MB-01 §2.10
- trail links: [[Topics/Biology/Research/Results/From sample to count table in 16S rRNA gene amplicon sequencing where counts depart from community composition, what the workflow's quantities measure, and how samples with unequal depth or load are compared. A literature review#2.10 Denoising and clustering]]

From the note:

> MB-01:I-0055 [2.10 Denoising and clustering] - The DADA2 developers report 93 output sequences on a 57-strain mock, against 249 for mothur and 378 for QIIME (Callahan 2016) [FT; meas; developer claim].
>

**Verdict:** okay

**Why:** matches

## 8. workflow-bias.2 (claim)

Departures were measured at most steps examined, but not at all of them: field sampling for water and host tissue was not searched, and several choices showed little or no detectable effect (PCR replicate pooling, preparation day and lane, cycle number in some studies, storage in one soil).

- conf: not stated
- class: not stated
- holds: the steps the review searched
- src: none (the critic's reading of the review's body)
- trail: MB-01 §critic, §Adversarial
- trail links: [[Topics/Biology/Research/Results/From sample to count table in 16S rRNA gene amplicon sequencing where counts depart from community composition, what the workflow's quantities measure, and how samples with unequal depth or load are compared. A literature review]] (callout: Critic: answers partly supported), [[Topics/Biology/Research/Results/From sample to count table in 16S rRNA gene amplicon sequencing where counts depart from community composition, what the workflow's quantities measure, and how samples with unequal depth or load are compared. A literature review]] (callout: Adversarial critique, full findings)

From the note:

> MB-01:C-011 [danger: Critic: answers partly supported] Departures are measured at most steps, but not at all of them.
>
> MB-01:C-012 [danger: Critic: answers partly supported] Field sampling for water and host tissue was not searched.
>
> MB-01:C-013 [danger: Critic: answers partly supported] Several choices showed little or no detectable effect: PCR replicate pooling, preparation day and lane, cycle number in some studies, and storage in one soil.
>
> MB-01:C-147 [warning: Adversarial critique, full findings] For the review's stronger 'departures found at every step': no.
>
> MB-01:C-148 [warning: Adversarial critique, full findings] Field sampling for water and host tissue was not searched, and several choices showed no detectable effect (PCR replicate pooling, lane and day, cycle number in some studies, storage relative to between-soil differences).
>
> MB-01:C-149 [warning: Adversarial critique, full findings] The answer should say departures were measured at most steps examined.
>

**Verdict:** good

**Why:** describes the gap in the searches

## 9. workflow-bias.4 (claim)

For relative abundance, the ordering in which extraction is the largest step, followed by PCR and then sequencing, rests on one 7-taxon vaginal dataset (Brooks 2015 reanalysed by McLaren 2019), with Albertsen 2015 (sludge, bead beating only) as partial support; it is contested by Fouhy 2016 (two extraction methods gave very similar data) and qualified by MBQC (specimen type mattered more than extraction), and is a single-dataset result, not a field-wide ordering. Fold errors of 2 to 30 or more between taxon pairs are reported.

- conf: single (critic: MB-01:C-017)
- class: deriv/model (marker)
- holds: one re-analysed 454 dataset of 7 taxa; the per-step decomposition would weaken substantially without McLaren 2019 and Brooks 2015
- src: mclarenConsistentCorrectableBias2019 (FT, re-opened; deriv/model; single dataset), brooksTruthMetagenomicsQuantifying2015, albertsenBackBasicsInfluence2015, fouhy16SRRNAGene2016, sinhaAssessmentVariationMicrobial2017
- trail: MB-01 §critic, §Adversarial, §1. Overview, §answers, §8. Answers
- rating: "weak for per-step relative-abundance magnitudes"
- trail links: [[Topics/Biology/Research/Results/From sample to count table in 16S rRNA gene amplicon sequencing where counts depart from community composition, what the workflow's quantities measure, and how samples with unequal depth or load are compared. A literature review]] (callout: Critic: answers partly supported), [[Topics/Biology/Research/Results/From sample to count table in 16S rRNA gene amplicon sequencing where counts depart from community composition, what the workflow's quantities measure, and how samples with unequal depth or load are compared. A literature review]] (callout: Adversarial critique, full findings), [[Topics/Biology/Research/Results/From sample to count table in 16S rRNA gene amplicon sequencing where counts depart from community composition, what the workflow's quantities measure, and how samples with unequal depth or load are compared. A literature review#1. Overview]], [[Topics/Biology/Research/Results/From sample to count table in 16S rRNA gene amplicon sequencing where counts depart from community composition, what the workflow's quantities measure, and how samples with unequal depth or load are compared. A literature review]] (callout: Answers as delivered), [[Topics/Biology/Research/Results/From sample to count table in 16S rRNA gene amplicon sequencing where counts depart from community composition, what the workflow's quantities measure, and how samples with unequal depth or load are compared. A literature review#8. Answers in brief]]

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
> MB-01:A-131 [quote: Answers as delivered] *Single-source sensitivity:* The per-step decomposition (extraction largest, then PCR, then sequencing) and the ratio-consistency claim would weaken substantially without McLaren 2019 and its source data (Brooks 2015).
>
> MB-01:B-0035 [1. Overview] - **Relative abundance.** The largest measured distortions arise from taxon-specific efficiencies at DNA extraction and PCR.
>
> MB-01:B-0036 [1. Overview] Fold errors of 2 to 30 or more between taxon pairs are reported.
>
> MB-01:A-297 [8. Answers in brief] Extraction and PCR dominate relative-abundance error, at roughly 2 to 30-fold pairwise.
>
> MB-01:I-0007 [2.2 DNA extraction] **Magnitude in a defined mock.** McLaren et al. reanalysed Brooks et al.'s 80 cell mixtures of 7 vaginal taxa (V1-V3, 454) (McLaren 2019) [FT, re-opened; deriv/model; single dataset].
>
> MB-01:C-022 [danger: Critic: answers partly supported] Overall: strong qualitatively; moderate for the inflation of taxon counts; weak for per-step relative-abundance magnitudes and for consistency across samples.
>

**Verdict:** good

**Why:** captures it well

## 10. bias-consistency.1 (claim)

McLaren et al. modelled each step as multiplying taxon abundances by a taxon-specific efficiency; under this model the error in taxon ratios was "consistent across samples", while the error in proportions "varied dramatically in both magnitude and direction".

- conf: single (marker)
- class: model (marker)
- holds: one reanalysis of 7 taxa mixed as cells (Brooks 2015 data); the one dataset modelled for this question
- src: mclarenConsistentCorrectableBias2019 (FT; model; single)
- trail: MB-01 §1. Overview, §2.14, §answers
- trail links: [[Topics/Biology/Research/Results/From sample to count table in 16S rRNA gene amplicon sequencing where counts depart from community composition, what the workflow's quantities measure, and how samples with unequal depth or load are compared. A literature review#1. Overview]], [[Topics/Biology/Research/Results/From sample to count table in 16S rRNA gene amplicon sequencing where counts depart from community composition, what the workflow's quantities measure, and how samples with unequal depth or load are compared. A literature review#2.14 Is the departure consistent across samples?]], [[Topics/Biology/Research/Results/From sample to count table in 16S rRNA gene amplicon sequencing where counts depart from community composition, what the workflow's quantities measure, and how samples with unequal depth or load are compared. A literature review]] (callout: Answers as delivered)

From the note:

> MB-01:I-0002 [1. Overview] One reanalysis finds it consistent on the ratio scale, which implies it varies on the proportion scale (McLaren 2019) [FT; model; single].
>
> MB-01:B-0183 [2.14 Is the departure consistent across samples?] **Ratio-scale model.** McLaren et al. modelled each step as multiplying taxon abundances by a taxon-specific efficiency (McLaren 2019) [FT, re-opened].
>
> MB-01:B-0184 [2.14 Is the departure consistent across samples?] Under this model, the error in ratios was "consistent across samples", while the error in proportions "varied dramatically in both magnitude and direction".
>
> MB-01:A-107 [quote: Answers as delivered] Is bias consistent across samples?
>
> MB-01:A-108 [quote: Answers as delivered] In the one dataset modelled for this question, error in taxon ratios was consistent across samples while error in proportions varied in size and sign (McLaren 2019).
>
> MB-01:B-0039 [1. Overview] Whether bias is consistent across samples is less settled.
>

**Verdict:** good

**Why:** near verbose

## 11. bias-consistency.4 (claim)

Brooks et al. found significant mixture-blending terms on the same data and concluded that one taxon's observed proportion depends on which others are present; the two readings conflict, and McLaren's attributes the apparent dependence to working on the proportion scale.

- conf: cont (note: "The two readings conflict")
- class: not stated
- holds: the same 7-taxon cell-mixture data
- src: brooksTruthMetagenomicsQuantifying2015, mclarenConsistentCorrectableBias2019
- trail: MB-01 §2.14, §1. Overview, §answers, §6. Where
- trail links: [[Topics/Biology/Research/Results/From sample to count table in 16S rRNA gene amplicon sequencing where counts depart from community composition, what the workflow's quantities measure, and how samples with unequal depth or load are compared. A literature review#2.14 Is the departure consistent across samples?]], [[Topics/Biology/Research/Results/From sample to count table in 16S rRNA gene amplicon sequencing where counts depart from community composition, what the workflow's quantities measure, and how samples with unequal depth or load are compared. A literature review#1. Overview]], [[Topics/Biology/Research/Results/From sample to count table in 16S rRNA gene amplicon sequencing where counts depart from community composition, what the workflow's quantities measure, and how samples with unequal depth or load are compared. A literature review]] (callout: Answers as delivered), [[Topics/Biology/Research/Results/From sample to count table in 16S rRNA gene amplicon sequencing where counts depart from community composition, what the workflow's quantities measure, and how samples with unequal depth or load are compared. A literature review#6. Where the evidence conflicts]]

From the note:

> MB-01:B-0187 [2.14 Is the departure consistent across samples?] **Composition-dependence reading.** Brooks et al. found significant mixture-blending terms on the same data and concluded that one taxon's observed proportion depends on which others are present (Brooks 2015).
>
> MB-01:B-0188 [2.14 Is the departure consistent across samples?] The two readings conflict, and McLaren's attributes the apparent dependence to working on the proportion scale.
>
> MB-01:B-0040 [1. Overview] The original authors of the same data read it as composition dependent (Brooks 2015).
>
> MB-01:A-109 [quote: Answers as delivered] The original authors read the same data as composition-dependent (Brooks 2015).
>
> MB-01:A-115 [quote: Answers as delivered] *Conflicts:* Composition dependence of bias: Brooks 2015 versus McLaren 2019, on the same data.
>
> MB-01:B-0330 [6. Where the evidence conflicts] Bias composition dependence: Brooks 2015 versus McLaren 2019, on the same data.
>

**Verdict:** ok

**Why:** gets the point across, but muddies it with use of bad language

## 12. abundance-distribution.22 (claim)

85% of the amplicon-defined dominant soil phylotypes were also dominant in 123 shotgun soil metagenomes; this is the only global amplicon-metagenome cross-check.

- conf: not stated
- class: not stated
- holds: 123 shotgun soil metagenomes
- src: delgadobaquerizoGlobalAtlasDominant2018 (FT)
- trail: MB-02 §D3.1, §answers
- trail links: [[Topics/Biology/Research/Results/16S rRNA gene copies per genome and per cell, abundance and rarity terms, and abundance in soil. A literature review#D3.1 How abundance is distributed among soil taxa, by measurement]], [[Topics/Biology/Research/Results/16S rRNA gene copies per genome and per cell, abundance and rarity terms, and abundance in soil. A literature review]] (callout: Answers as delivered)

From the note:

> MB-02:B-0243 [D3.1 How abundance is distributed among soil taxa, by measurement] - 85% of the amplicon-defined dominant phylotypes were also dominant in 123 shotgun soil metagenomes [60, FT].
>
> MB-02:A-088 [quote: Answers as delivered] Metagenomes: no taxon abundance distribution for soil from metagenomes was found; what was found is that soil metagenomes are far from saturated (80% of about 300 Gbp of Iowa soil reads could not be assembled for low coverage; 48% and 31% of contigs below 10x) [79], soils sit among the least covered communities [80], and 85% of amplicon-defined dominant phylotypes were also dominant in 123 shotgun metagenomes [60].
>
> MB-02:A-097 [quote: Answers as delivered] *Single-source sensitivity:* Removing Delgado-Baquerizo et al. 2018 [60] removes the only global amplicon-metagenome cross-check.
>

**Verdict:** good

**Why:** 

## 13. technical-variation.7 (claim)

A PCR machine with a mis-set annealing temperature produced a batch outlier.

- conf: not stated
- class: not stated
- holds: Silverman 2021; checked by the critic
- src: silvermanMeasuringMitigatingPCR2021
- trail: MB-01 §4.3, §answers, §critic
- trail links: [[Topics/Biology/Research/Results/From sample to count table in 16S rRNA gene amplicon sequencing where counts depart from community composition, what the workflow's quantities measure, and how samples with unequal depth or load are compared. A literature review#4.3 Processes other than sampling]], [[Topics/Biology/Research/Results/From sample to count table in 16S rRNA gene amplicon sequencing where counts depart from community composition, what the workflow's quantities measure, and how samples with unequal depth or load are compared. A literature review]] (callout: Answers as delivered), [[Topics/Biology/Research/Results/From sample to count table in 16S rRNA gene amplicon sequencing where counts depart from community composition, what the workflow's quantities measure, and how samples with unequal depth or load are compared. A literature review]] (callout: Critic: answers partly supported)

From the note:

> MB-01:B-0246 [4.3 Processes other than sampling] - A PCR machine with a mis-set annealing temperature produced a batch outlier (Silverman 2021).
>
> MB-01:A-198 [quote: Answers as delivered] Run and batch effects: whole-run taxon loss (Yeh 2018, single source); a mis-set PCR machine produced a batch outlier (Silverman 2021); between-laboratory effects (MBQC).
>
> MB-01:C-054 [danger: Critic: answers partly supported] Verified against full text: McLaren 2019 per-step bias table (36.6 and 29.3 max, 5.5 and 5.6 mean), Silverman 2021 (2.6-fold, about 19% of taxa more than 4-fold, mis-set annealing machine), Sze and Schloss 2019 (R2 0.79, 0.044, 0.033; chimera rates 0.9 to 18.2%), Schloss 2024b (Table 1 read ranges, coverage-based iNEXT passage, Good's coverage 89.4 to 99.8%), Karstens 2019, Fitzpatrick 2018, Thompson 2017, Song 2016, Starke 2021, Louca 2018, Laursen 2017, Wen 2017, Weiss 2017, Nearing 2018 and 2022, Wirbel 2024, Zemb 2020, Glassman 2018, Chiarello 2022, Stoddard 2015, Vetrovsky 2013, Kembel 2012, Hornung 2019, Lennon 2018, Barlow 2020 and Dyrhovden 2021.
>

**Verdict:** yes

**Why:** 

## 14. beta-diversity.3 (claim)

Library-size normalisation had very little effect on beta-diversity separation compared with the choice of distance metric.

- conf: single (marker)
- class: meas (marker)
- holds: abstract only
- src: thorsenLargescaleBenchmarkingReveals2016 (AB; meas; single)
- trail: MB-01 §5.3, §7. Bounds, §answers
- trail links: [[Topics/Biology/Research/Results/From sample to count table in 16S rRNA gene amplicon sequencing where counts depart from community composition, what the workflow's quantities measure, and how samples with unequal depth or load are compared. A literature review#5.3 Beta diversity]], [[Topics/Biology/Research/Results/From sample to count table in 16S rRNA gene amplicon sequencing where counts depart from community composition, what the workflow's quantities measure, and how samples with unequal depth or load are compared. A literature review#7. Bounds and negative results]], [[Topics/Biology/Research/Results/From sample to count table in 16S rRNA gene amplicon sequencing where counts depart from community composition, what the workflow's quantities measure, and how samples with unequal depth or load are compared. A literature review]] (callout: Answers as delivered)

From the note:

> MB-01:I-0124 [5.3 Beta diversity] - Library-size normalisation had very little effect on beta-diversity separation compared with the choice of distance metric (Thorsen 2016) [AB; meas; single].
>
> MB-01:A-250 [quote: Answers as delivered] Library normalisation had very little effect on beta separation compared with the choice of metric (Thorsen 2016, abstract).
>
> MB-01:B-0355 [7. Bounds and negative results] - library normalisation, relative to metric choice (Thorsen 2016);
>

**Verdict:** good

**Why:** near verbose

## 15. rarefying.1 (claim)

Rarefaction comes from ecology, traced to Sanders 1968, Hurlbert 1971 and Simberloff 1972; Gotelli and Colwell argue that individual-based rarefaction allows meaningful comparison and that asymptotic estimators give lower bounds; rarefaction curves are a display of sampling completeness and were not benchmarked as a comparison method in the sources found.

- conf: not stated
- class: assert (marker)
- holds: ecology, labelled INDIRECT; the origins known only secondarily via Chao and Jost 2012
- src: gotelliQuantifyingBiodiversityProcedures2001 (AB; assert; INDIRECT), sandersMarineBenthicDiversity1968 (SEC), hurlbertNonconceptSpeciesDiversity1971 (SEC), chaoCoveragebasedRarefactionExtrapolation2012
- trail: MB-01 §5.1, §5.6
- trail links: [[Topics/Biology/Research/Results/From sample to count table in 16S rRNA gene amplicon sequencing where counts depart from community composition, what the workflow's quantities measure, and how samples with unequal depth or load are compared. A literature review#5.1 Origins of the approaches]], [[Topics/Biology/Research/Results/From sample to count table in 16S rRNA gene amplicon sequencing where counts depart from community composition, what the workflow's quantities measure, and how samples with unequal depth or load are compared. A literature review#5.6 Summary by approach]]

From the note:

> MB-01:B-0264 [5.1 Origins of the approaches] **Rarefaction.** The method comes from ecology, traced to Sanders 1968, Hurlbert 1971 and Simberloff 1972 (SEC via Chao and Jost 2012).
>
> MB-01:I-0106 [5.1 Origins of the approaches] Gotelli and Colwell argue that individual-based rarefaction allows meaningful comparison and that asymptotic estimators give lower bounds (Gotelli and Colwell 2001) [AB; assert; INDIRECT].
>
> MB-01:B-0326 [5.6 Summary by approach] | Rarefaction curves | Display of sampling completeness (ecology) | Not benchmarked as a comparison method in the sources found | Alpha |
>

**Verdict:** yes

**Why:** near verbose

## 16. coverage-standardisation.3 (claim)

In Schloss 2024b's null models, coverage-based iNEXT estimates were among those that "showed a strong correlation between richness and the number of sequences"; the text exempts "rarefaction and possibly the size-based iNEXT estimates". This is the only microbial amplicon test of coverage-based standardisation found; beyond it the evidence is non-microbial.

- conf: single (critic: MB-01:C-049)
- class: model (note: "null models")
- holds: Schloss's null models; the synthesis agent's re-reading of the full text, verified by the critic
- src: schlossRarefactionCurrentlyBest2024 (FT, re-opened)
- trail: MB-01 §5.2, §answers, §critic, §Search record
- trail links: [[Topics/Biology/Research/Results/From sample to count table in 16S rRNA gene amplicon sequencing where counts depart from community composition, what the workflow's quantities measure, and how samples with unequal depth or load are compared. A literature review#5.2 Richness and other alpha diversity measures]], [[Topics/Biology/Research/Results/From sample to count table in 16S rRNA gene amplicon sequencing where counts depart from community composition, what the workflow's quantities measure, and how samples with unequal depth or load are compared. A literature review]] (callout: Answers as delivered), [[Topics/Biology/Research/Results/From sample to count table in 16S rRNA gene amplicon sequencing where counts depart from community composition, what the workflow's quantities measure, and how samples with unequal depth or load are compared. A literature review]] (callout: Critic: answers partly supported), [[Topics/Biology/Research/Results/From sample to count table in 16S rRNA gene amplicon sequencing where counts depart from community composition, what the workflow's quantities measure, and how samples with unequal depth or load are compared. A literature review#Search record]]

From the note:

> MB-01:B-0277 [5.2 Richness and other alpha diversity measures] - **Coverage-based iNEXT.** In the synthesis agent's re-reading of the full text, coverage-based iNEXT estimates were among those that "showed a strong correlation between richness and the number of sequences".
>
> MB-01:B-0278 [5.2 Richness and other alpha diversity measures] The text exempts "rarefaction and possibly the size-based iNEXT estimates".
>
> MB-01:B-0279 [5.2 Richness and other alpha diversity measures] This is the only microbial amplicon test of coverage-based standardisation found.
>
> MB-01:A-236 [quote: Answers as delivered] In Schloss 2024b's null models the coverage-based iNEXT estimates stayed correlated with depth (the synthesis agent's reading of the full text).
>
> MB-01:B-0375 [Search record] One correction resulted: the Schloss 2024b passage shows coverage-based iNEXT estimates remained correlated with depth.
>
> MB-01:C-049 [danger: Critic: answers partly supported] Coverage-based standardisation has one microbial test (the Schloss 2024b null model, verified: all approaches 'except for rarefaction and possibly the size-based iNEXT estimates' remained depth-correlated).
>
> MB-01:C-050 [danger: Critic: answers partly supported] Beyond that, the evidence is non-microbial.
>
> MB-01:A-313 [8. Answers in brief] Coverage-based standardisation has almost no microbial benchmark.
>

**Verdict:** good

**Why:** captures everything. just bad language 

## 17. richness-estimators.6 (claim)

A singleton-replacement estimator for error-inflated data has been proposed.

- conf: single (marker)
- class: model (marker)
- holds: abstract only
- src: chiuEstimatingComparingMicrobial2016 (AB; model; single)
- trail: MB-01 §5.2, §answers
- trail links: [[Topics/Biology/Research/Results/From sample to count table in 16S rRNA gene amplicon sequencing where counts depart from community composition, what the workflow's quantities measure, and how samples with unequal depth or load are compared. A literature review#5.2 Richness and other alpha diversity measures]], [[Topics/Biology/Research/Results/From sample to count table in 16S rRNA gene amplicon sequencing where counts depart from community composition, what the workflow's quantities measure, and how samples with unequal depth or load are compared. A literature review]] (callout: Answers as delivered)

From the note:

> MB-01:I-0117 [5.2 Richness and other alpha diversity measures] - A singleton-replacement estimator for error-inflated data has been proposed (Chiu and Chao 2016) [AB; model; single].
>
> MB-01:A-241 [quote: Answers as delivered] Spurious singletons inflate them (Pinto and Raskin 2012; Chiu and Chao 2016).
>

**Verdict:** good

**Why:** near verbose

## 18. compositional-analysis.3 (claim)

Fold changes in taxon ratios are invariant to multiplicative bias, while fold changes in proportions are not and can change sign; the bias-invariance of ratio-based methods rests on McLaren 2019.

- conf: not stated
- class: not stated
- holds: McLaren 2019's model
- src: mclarenConsistentCorrectableBias2019
- trail: MB-01 §5.4, §answers
- trail links: [[Topics/Biology/Research/Results/From sample to count table in 16S rRNA gene amplicon sequencing where counts depart from community composition, what the workflow's quantities measure, and how samples with unequal depth or load are compared. A literature review#5.4 Tests of which taxa differ in abundance]], [[Topics/Biology/Research/Results/From sample to count table in 16S rRNA gene amplicon sequencing where counts depart from community composition, what the workflow's quantities measure, and how samples with unequal depth or load are compared. A literature review]] (callout: Answers as delivered)

From the note:

> MB-01:B-0310 [5.4 Tests of which taxa differ in abundance] **Taxonomic bias.** Fold changes in taxon ratios are invariant to multiplicative bias; fold changes in proportions are not and can change sign (McLaren 2019).
>
> MB-01:A-262 [quote: Answers as delivered] Ratio-based analyses are invariant to multiplicative bias, whereas proportion-based ones are biased when community mean efficiency tracks the condition (McLaren 2019; McLaren 2022 preprint).
>
> MB-01:A-293 [quote: Answers as delivered] The bias-invariance of ratio-based methods rests on McLaren 2019.
>

**Verdict:** holds

**Why:** misses a paper

## 19. absolute-quantification.4 (claim)

Absolute abundance could hold steady or rise while relative abundance fell.

- conf: not stated
- class: not stated
- holds: soil
- src: tkaczAbsoluteQuantitationMicrobiota2018 (FT; soil)
- trail: MB-01 §5.5
- trail links: [[Topics/Biology/Research/Results/From sample to count table in 16S rRNA gene amplicon sequencing where counts depart from community composition, what the workflow's quantities measure, and how samples with unequal depth or load are compared. A literature review#5.5 Absolute quantification of total load]]

From the note:

> MB-01:B-0314 [5.5 Absolute quantification of total load] - Absolute abundance could hold steady or rise while relative abundance fell (Tkacz 2018) [FT; soil].
>

**Verdict:** ok

**Why:** verbose

## 20. dns.27 (do not say)

"About 2.2" as the community copy number of water.

- why: the EMP value pools free-living (soil, water, sediment) and plant-associated samples
- instead: community-copy-number.1
- trail: MB-01 §Adversarial
- trail links: [[Topics/Biology/Research/Results/From sample to count table in 16S rRNA gene amplicon sequencing where counts depart from community composition, what the workflow's quantities measure, and how samples with unequal depth or load are compared. A literature review]] (callout: Adversarial critique, full findings)

From the note:

> MB-01:C-136 [warning: Adversarial critique, full findings] - D3 copy number by environment: the EMP ACN of about 2.2 pools free-living (soil, water, sediment) and plant-associated samples; the review notes this but still offers it in the 'water' row.
>

**Verdict:** bad

**Why:** nosense

