## contamination-gain.9 (claim)

GUNC flagged 15.1% to 29.9% of CheckM-prefiltered human gut MAG catalogues as chimeric at genus level or above.

- conf: not stated
- class: meas (note: "The study measures chimerism")
- holds: natural human gut MAG catalogues; the study measures chimerism, not called gene content; the critic: not re-opened at synthesis, resting on agent reads
- src: orakovGUNCDetectionChimerism2021
- trail: H1-02 §2.2, §3.1

From the note:

> H1-02:B-0058 [2.2 Real-data artefacts without an isolate reference (natural)] Orakov et al. [9] found that GUNC flagged 15.1% to 29.9% of CheckM-prefiltered human gut MAG catalogues as chimeric at genus level or above.
>
> H1-02:B-0061 [2.2 Real-data artefacts without an isolate reference (natural)] The study measures chimerism, not called gene content.
>
> H1-02:B-0123 [3.1 Human gut (natural)] Chimerism in CheckM-prefiltered catalogues ranged from 15.1% to 29.9% by study [9].
>
> H1-02:C-093 [warning: Adversarial critique, full findings] [3] and [9] rest on agent reads.
>
> H1-02:B-0178 [Search record] Not re-opened at synthesis: [2], [4], [7], [9], [10], [11], [14] to [25] and [28] to [35].
>

## gene-class-specificity.5 (claim)

The artefact is gene-class specific and passes a completeness filter, across seawater, gut, chicken gut and phyllosphere catalogues.

- conf: not stated
- class: not stated
- holds: natural short-read MAG catalogues; the review's conclusion from Mise and Iwasaki
- src: miseUnexpectedAbsenceRibosomal2022
- trail: H1-02 §2.2, §4. Where, §Verdict as delivered

From the note:

> H1-02:B-0055 [2.2 Real-data artefacts without an isolate reference (natural)] The artefact is therefore gene-class specific and passes a completeness filter.
>
> H1-02:B-0161 [4. Where the evidence is strongest, and its limits] Mise and Iwasaki [6] support the gene-class specificity across environments.
>
> H1-02:A-001 [quote: Verdict as delivered] **A. Size of recovery artefacts in gene or pathway content of related recovered genomes**: MEASURED AND MATERIAL, in natural human gut samples (direct same-sample isolate comparisons, n = 8 E. coli pairs [1]; real-data contamination of differential gene calls [22]) and in natural coastal marine samples (read-technology gene-count difference at equal estimated completeness [12]), with gene-class-specific losses across seawater, gut, chicken gut and phyllosphere catalogues [6].
>
> H1-02:B-0051 [2.2 Real-data artefacts without an isolate reference (natural)] Core ribosomal protein genes "could be missing in more than 20-40% of near-complete" MAGs in four of five short-read catalogues (seawater, human gut, chicken gut, rice phyllosphere).
>

Not found in the cited text (where to look, not what is wrong): holds: review

## read-technology.1 (claim)

In MAG pairs sharing 99% ANI or more from the same DNA extracts, the PacBio HiFi MAG carried more predicted genes than the Illumina MAG (median 1,872 against 1,704, p < 0.05) and was longer (1.98 against 1.85 Mbp), while CheckM completeness and contamination did not differ.

- conf: single (note: "SINGLE SOURCE")
- class: meas (note: "measured")
- holds: natural coastal marine; North Sea DNA extracts, 4 samples, one time series; the number of pairs is given only in a figure; short-read libraries had about 3 times more sequenced bases, so read technology and depth are confounded
- src: orellanaComparingGenomesRecovered2023
- trail: H1-02 §2.3, §critic

From the note:

> H1-02:B-0063 [2.3 Read technology on the same DNA (natural, marine)] Orellana et al. [12] sequenced the same North Sea DNA extracts with Illumina and PacBio HiFi.
>
> H1-02:B-0064 [2.3 Read technology on the same DNA (natural, marine)] In MAG pairs sharing 99% ANI or more, the long-read MAG carried more predicted genes (median 1,872 against 1,704, p < 0.05) and was longer (1.98 against 1.85 Mbp), while CheckM completeness and contamination did not differ.
>
> H1-02:B-0065 [2.3 Read technology on the same DNA (natural, marine)] A 16S rRNA gene was present in 88% of long-read MAGs and 23% of short-read MAGs (measured; natural; SINGLE SOURCE; the number of pairs is given only in a figure).
>
> H1-02:C-004 [danger: Critic: verdict partly supported] In marine samples, short-read MAGs carried about 9% fewer predicted genes than long-read MAGs at equal CheckM completeness (SINGLE SOURCE [12]; 4 samples; short-read libraries had about 3 times more sequenced bases, so read technology and depth are confounded).
>
> H1-02:C-049 [warning: Adversarial critique, full findings] - Marine Part B verdict 'measured and systematic for read technology' rests on Orellana et al. [12]: 4 North Sea samples, one time series. 'Systematic' is a field-level phrasing for n = 1 study.
>
> H1-02:C-001 [danger: Critic: verdict partly supported] **Reformulated verdict:** Part A: MEASURED AND MATERIAL, but only in natural human gut and, from a single source, coastal marine samples.
>

## read-technology.2 (claim)

A 16S rRNA gene was present in 88% of long-read MAGs and 23% of short-read MAGs.

- conf: single (note: "SINGLE SOURCE")
- class: meas (note: "measured")
- holds: natural coastal marine; the same North Sea DNA extracts sequenced with Illumina and PacBio HiFi
- src: orellanaComparingGenomesRecovered2023
- trail: H1-02 §2.3

From the note:

> H1-02:B-0063 [2.3 Read technology on the same DNA (natural, marine)] Orellana et al. [12] sequenced the same North Sea DNA extracts with Illumina and PacBio HiFi.
>
> H1-02:B-0065 [2.3 Read technology on the same DNA (natural, marine)] A 16S rRNA gene was present in 88% of long-read MAGs and 23% of short-read MAGs (measured; natural; SINGLE SOURCE; the number of pairs is given only in a figure).
>
> H1-02:C-001 [danger: Critic: verdict partly supported] **Reformulated verdict:** Part A: MEASURED AND MATERIAL, but only in natural human gut and, from a single source, coastal marine samples.
>

## read-technology.3 (claim)

Short-read MAGs carried about 9% fewer predicted genes than long-read MAGs at equal CheckM completeness, a difference invisible to completeness estimates. Short-read libraries had about 3 times more sequenced bases (about 36 Gbp per sample for Illumina against 12 Gbp for PacBio), so read technology and depth are confounded.

- conf: single (critic: C-004)
- class: not stated
- holds: natural coastal marine; 4 North Sea samples, one time series
- src: orellanaComparingGenomesRecovered2023
- trail: H1-02 §2.3, §critic, §Adversarial

From the note:

> H1-02:B-0066 [2.3 Read technology on the same DNA (natural, marine)] Reviewer's reading: a gene-count difference of about 9%, which depended on read technology, was invisible to completeness estimates.
>
> H1-02:C-004 [danger: Critic: verdict partly supported] In marine samples, short-read MAGs carried about 9% fewer predicted genes than long-read MAGs at equal CheckM completeness (SINGLE SOURCE [12]; 4 samples; short-read libraries had about 3 times more sequenced bases, so read technology and depth are confounded).
>
> H1-02:C-017 [danger: Critic: verdict partly supported] [12]'s gene-count gap is confounded with depth: the paper reports about 36 Gbp per sample for Illumina against 12 Gbp for PacBio.
>
> H1-02:C-049 [warning: Adversarial critique, full findings] - Marine Part B verdict 'measured and systematic for read technology' rests on Orellana et al. [12]: 4 North Sea samples, one time series. 'Systematic' is a field-level phrasing for n = 1 study.
>
> H1-02:C-088 [warning: Adversarial critique, full findings] - The Orellana reading ('a gene-count difference of about 9%, which depended on read technology') omits the paper's reported 3-fold difference in sequenced bases between platforms. It attributes the effect to technology alone.
>
> H1-02:C-001 [danger: Critic: verdict partly supported] **Reformulated verdict:** Part A: MEASURED AND MATERIAL, but only in natural human gut and, from a single source, coastal marine samples.
>

## core-genome-inference.1 (claim)

Simulated random incompleteness of 1% left only about 36% of strict core families, and contamination inflated the cloud genome; the authors state that random removal "may overestimate" core loss. Simulations of core-genome inference give larger numbers because they strip sequence at random.

- conf: not stated
- class: model (note: "Simulations of core-genome inference")
- holds: simulations of core-genome inference with sequence removed at random
- src: liCriticalAssessmentPangenomic2022
- trail: H1-02 §2.5

From the note:

> H1-02:B-0089 [2.5 Incompleteness and pathway completeness] Simulations of core-genome inference give larger numbers because they strip sequence at random.
>
> H1-02:B-0090 [2.5 Incompleteness and pathway completeness] Li and Yin [2] found that 1% random incompleteness left only about 36% of strict core families, and contamination inflated the cloud genome.
>
> H1-02:B-0091 [2.5 Incompleteness and pathway completeness] The authors state that random removal "may overestimate" core loss.
>

## bounding-comparisons.2 (claim)

Near-complete gut MAGs had lengths similar to isolates of the same OTU, and KEGG annotations were concordant per OTU (n = 665); only 14.5% of the MAGs met MIMAG high quality, mostly because rRNA genes were missing.

- conf: not stated
- class: deriv (note: "inferred")
- holds: natural human gut; aggregated comparisons across different strains; the critic: not re-opened at synthesis, resting on search-agent reads with no cross-agent confirmation
- src: nayfachNewInsightsUncultivated2019
- trail: H1-02 §2.6, §Adversarial

From the note:

> H1-02:B-0098 [2.6 Bounding and negative facts] - Nayfach et al. 2019 [21]: near-complete gut MAGs had lengths similar to isolates of the same OTU, and KEGG annotations were concordant per OTU (n = 665).
>
> H1-02:B-0099 [2.6 Bounding and negative facts] These are aggregated comparisons across different strains, and only 14.5% of the MAGs met MIMAG high quality, mostly because rRNA genes were missing (inferred).
>
> H1-02:C-040 [warning: Adversarial critique, full findings] - Nayfach et al. 2019 [21], Pasolli et al. [25], Gautreau et al. [20], Johansen et al. [28], Sereika et al. [17], Pan et al. [31], Han et al. [32], Rocha et al. [34] and Maranga et al. [35]: none was re-opened at synthesis.
>
> H1-02:C-042 [warning: Adversarial critique, full findings] These are not breaches as such, but they are unverified second-hand figures, and several carry weight in the soil Part B indirect evidence.
>
> H1-02:C-041 [warning: Adversarial critique, full findings] Their figures rest on search-agent reads with no cross-agent confirmation, including the Han 22% to 30% ARG-host figure, Johansen's 57% against 27% and 73% against 47%, and Gautreau's 55 of 78 species.
>
> H1-02:R-0130 [References] New insights from uncultivated genomes of the global human gut microbiome.
>

## bounding-comparisons.3 (claim)

36 MAGs were almost identical by ANI to 18 isolates from the same samples; identity metrics do not test accessory content.

- conf: not stated
- class: not stated
- holds: human microbiome samples (Pasolli et al.); ANI only; the critic: not re-opened at synthesis, resting on search-agent reads
- src: pasolliExtensiveUnexploredHuman2019
- trail: H1-02 §2.6, §Adversarial

From the note:

> H1-02:B-0100 [2.6 Bounding and negative facts] - Pasolli et al. [25]: 36 MAGs were almost identical by ANI to 18 isolates from the same samples.
>
> H1-02:B-0101 [2.6 Bounding and negative facts] Identity metrics do not test accessory content.
>
> H1-02:C-040 [warning: Adversarial critique, full findings] - Nayfach et al. 2019 [21], Pasolli et al. [25], Gautreau et al. [20], Johansen et al. [28], Sereika et al. [17], Pan et al. [31], Han et al. [32], Rocha et al. [34] and Maranga et al. [35]: none was re-opened at synthesis.
>
> H1-02:C-042 [warning: Adversarial critique, full findings] These are not breaches as such, but they are unverified second-hand figures, and several carry weight in the soil Part B indirect evidence.
>
> H1-02:C-041 [warning: Adversarial critique, full findings] Their figures rest on search-agent reads with no cross-agent confirmation, including the Han 22% to 30% ARG-host figure, Johansen's 57% against 27% and 73% against 47%, and Gautreau's 55 of 78 species.
>
> H1-02:R-0144 [References] Extensive Unexplored Human Microbiome Diversity Revealed by Over 150,000 Genomes from Metagenomes Spanning Age, Geography, and Lifestyle.
>

## filters-corrections.5 (claim)

Eisenhofer's completeness-model correction (a GLM) was validated on mock-community subsamples and over-corrected some genomes.

- conf: not stated
- class: not stated
- holds: mock-community subsamples, not natural-sample MAGs
- src: eisenhoferImpactMicrobialGenome2023
- trail: H1-02 §2.7

From the note:

> H1-02:B-0112 [2.7 Filters and corrections: real-sample validation] - Completeness-model corrections: Eisenhofer's GLM [3] was validated on mock-community subsamples and over-corrected some genomes.
>
> H1-02:B-0115 [2.7 Filters and corrections: real-sample validation] None of these was validated against ground truth on natural-sample MAGs with real, non-random gaps.
>

## annotation-coverage.2 (claim)

Orthology-based GO coverage in an infant gut catalogue was 12%, and it favoured Gammaproteobacteria.

- conf: not stated
- class: meas (note: "These are measured, gut only")
- holds: one infant gut catalogue; the critic: not re-opened at synthesis, resting on search-agent reads
- src: marangaComprehensiveFunctionalAnnotation2023
- trail: H1-02 §3.6, §Adversarial

From the note:

> H1-02:B-0157 [3.6 Annotation coverage] Orthology-based GO coverage in an infant gut catalogue was 12%, and it favoured Gammaproteobacteria [35].
>
> H1-02:B-0158 [3.6 Annotation coverage] These are measured, gut only.
>
> H1-02:C-040 [warning: Adversarial critique, full findings] - Nayfach et al. 2019 [21], Pasolli et al. [25], Gautreau et al. [20], Johansen et al. [28], Sereika et al. [17], Pan et al. [31], Han et al. [32], Rocha et al. [34] and Maranga et al. [35]: none was re-opened at synthesis.
>
> H1-02:C-042 [warning: Adversarial critique, full findings] These are not breaches as such, but they are unverified second-hand figures, and several carry weight in the soil Part B indirect evidence.
>
> H1-02:C-041 [warning: Adversarial critique, full findings] Their figures rest on search-agent reads with no cross-agent confirmation, including the Han 22% to 30% ARG-host figure, Johansen's 57% against 27% and 73% against 47%, and Gautreau's 55 of 78 species.
>

## marine-dependence.1 (claim)

In marine samples, dependence of gene content on a sample property has been measured for read technology only, in a single source, and confounded with depth: one study of 4 samples.

- conf: single (critic: C-010)
- class: not stated
- rating: "MEASURED AND SYSTEMATIC for read technology" (critic: C-024: 'systematic' is too strong for n = 1 study)
- holds: natural coastal marine; 4 North Sea samples, one time series
- src: orellanaComparingGenomesRecovered2023
- trail: H1-02 §critic, §Adversarial, §Verdict as delivered

From the note:

> H1-02:C-010 [danger: Critic: verdict partly supported] Part B, marine: MEASURED for read technology only, SINGLE SOURCE [12], confounded with depth.
>
> H1-02:C-024 [danger: Critic: verdict partly supported] The marine read-technology verdict rests on one study of 4 samples with a depth confound, so 'systematic' is too strong for n = 1 study.
>
> H1-02:C-049 [warning: Adversarial critique, full findings] - Marine Part B verdict 'measured and systematic for read technology' rests on Orellana et al. [12]: 4 North Sea samples, one time series. 'Systematic' is a field-level phrasing for n = 1 study.
>
> H1-02:A-010 [quote: Verdict as delivered] **B. Dependence on sample properties: marine / seawater (natural)**: MEASURED AND SYSTEMATIC for read technology, but this rests on a SINGLE SOURCE for gene content: about 9% fewer predicted genes in short-read than long-read MAG pairs from the same DNA, at equal CheckM completeness [12].
>
> H1-02:C-001 [danger: Critic: verdict partly supported] **Reformulated verdict:** Part A: MEASURED AND MATERIAL, but only in natural human gut and, from a single source, coastal marine samples.
>

## marine-dependence.2 (claim)

In marine samples, dependence of gene content on diversity or depth has not been measured; the evidence covers MAG yield only.

- conf: not stated
- class: search (note: "Not found, with routes")
- search: searched, not found (note: "Routes: WebSearch and Europe PMC on sequencing effort against binning, batch or study effects in MAG catalogues, and soil MAG against depth")
- holds: natural marine and seawater
- src: royaltyTheoreticalSimulationBasedInvestigation2019
- trail: H1-02 §Verdict as delivered, §critic, §5. Verdicts

From the note:

> H1-02:A-012 [quote: Verdict as delivered] Dependence on diversity and depth: NOT MEASURED for gene content.
>
> H1-02:A-013 [quote: Verdict as delivered] The evidence covers MAG yield only [16].
>
> H1-02:C-011 [danger: Critic: verdict partly supported] NOT MEASURED for diversity or depth.
>
> H1-02:A-032 [5. Verdicts] Not measured for diversity or depth.
>
> H1-02:B-0181 [Search record] Not found, with routes: (1) A soil or sediment study comparing gene content of MAGs with isolate or closed genomes of the same lineage.
>
> H1-02:B-0186 [Search record] (3) Any study measuring how gene-content artefacts between conspecific MAGs scale with community diversity or depth across samples.
>
> H1-02:B-0187 [Search record] Routes: WebSearch and Europe PMC on sequencing effort against binning, batch or study effects in MAG catalogues, and soil MAG against depth.
>
> H1-02:A-010 [quote: Verdict as delivered] **B. Dependence on sample properties: marine / seawater (natural)**: MEASURED AND SYSTEMATIC for read technology, but this rests on a SINGLE SOURCE for gene content: about 9% fewer predicted genes in short-read than long-read MAG pairs from the same DNA, at equal CheckM completeness [12].
>
> H1-02:A-031 [5. Verdicts] - Marine: **measured and systematic** for read technology [12] (SINGLE SOURCE for gene content; [6] indirect).
>
> H1-02:C-010 [danger: Critic: verdict partly supported] Part B, marine: MEASURED for read technology only, SINGLE SOURCE [12], confounded with depth.
>

## soil-sediment.3 (claim)

Recovery (assembly fraction, MAG yield, bin quality) in soil depends systematically on diversity, depth, habitat and binner, and short-read assembly loss tracks within-sample coverage and population sequence variation.

- conf: not stated
- class: meas (note: "All of this is measured and natural")
- holds: natural soils; recovery quality, not gene content; the critic: several of the figures behind it are unverified second-hand figures, resting on search-agent reads
- src: johansenUnveilingSoilMicrobial2025, sereikaGenomeresolvedLongreadSequencing2025, kimComprehensiveBenchmarkingMetagenomic2026, panDeepSiameseNeural2022, bergComparisonShortreadLongread2025
- trail: H1-02 §3.3, §Verdict as delivered, §5. Verdicts, §Adversarial

From the note:

> H1-02:A-015 [quote: Verdict as delivered] Indirect support only: recovery (assembly fraction, MAG yield, bin quality) depends systematically on field diversity and depth [28], habitat [17] and binner [27, 31], and short-read assembly loss tracks within-sample coverage and population sequence variation [26].
>
> H1-02:A-034 [5. Verdicts] There is indirect evidence that recovery quality varies systematically with diversity, depth, habitat and binner [17, 26, 27, 28, 31].
>
> H1-02:B-0140 [3.3 Soil (natural)] All of this is measured and natural, and it shows that recovery quality in soil depends systematically on diversity, depth and binner.
>
> H1-02:C-042 [warning: Adversarial critique, full findings] These are not breaches as such, but they are unverified second-hand figures, and several carry weight in the soil Part B indirect evidence.
>
> H1-02:C-040 [warning: Adversarial critique, full findings] - Nayfach et al. 2019 [21], Pasolli et al. [25], Gautreau et al. [20], Johansen et al. [28], Sereika et al. [17], Pan et al. [31], Han et al. [32], Rocha et al. [34] and Maranga et al. [35]: none was re-opened at synthesis.
>
> H1-02:C-041 [warning: Adversarial critique, full findings] Their figures rest on search-agent reads with no cross-agent confirmation, including the Han 22% to 30% ARG-host figure, Johansen's 57% against 27% and 73% against 47%, and Gautreau's 55 of 78 species.
>

## engineered-simulated.9 (claim)

In simulations and engineered systems, strain diversity and read technology have systematic effects, with one null for close relatives; these do not answer the question for natural samples.

- conf: not stated
- class: not stated
- rating: "MEASURED AND SYSTEMATIC in simulations"
- holds: simulations and engineered bioreactors; the critic accepts this verdict as stated
- src: meyerCriticalAssessmentMetagenome2022, rochaSimulation69Microbial2024, sereikaOxfordNanoporeR102022, singletonConnectingStructureFunction2021, maguireMetagenomeAssembledGenomeBinning2020
- trail: H1-02 §Verdict as delivered, §5. Verdicts, §critic

From the note:

> H1-02:A-018 [quote: Verdict as delivered] **B. Dependence on sample properties: engineered systems and simulations (kept separate)**: MEASURED AND SYSTEMATIC in simulations (strain diversity degrades completeness and purity [7]; depth effects are pipeline-dependent [34]).
>
> H1-02:A-021 [quote: Verdict as delivered] None of these answers the question for natural samples.
>
> H1-02:A-036 [5. Verdicts] - Engineered systems and simulations: systematic effects of strain diversity and read technology [7, 29, 30, 34], with one null for close relatives [4].
>
> H1-02:A-037 [5. Verdicts] These do not answer the natural-sample question.
>
> H1-02:C-014 [danger: Critic: verdict partly supported] Engineered systems and simulations: as stated, and they do not answer the natural-sample question.
>
> H1-02:A-020 [quote: Verdict as delivered] In engineered bioreactors, read technology changes contiguity and rRNA recovery [29, 30].
>

