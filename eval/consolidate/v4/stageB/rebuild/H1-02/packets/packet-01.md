## mag-recovery.1 (claim)

Direct measurements exist of how far recovery (incompleteness, contamination, failure to assemble or bin variable and mobile regions, uneven annotation) changes the called gene or pathway content of a recovered genome, although they are few.

- conf: not stated
- class: not stated
- holds: the review's reading of the literature its search found on recovered genomes
- src: none (the reviewer's synthesis)
- trail: H1-02 §1. Scope

From the note:

> H1-02:B-0022 [1. Scope of the evidence] The first asks how far recovery (incompleteness, contamination, failure to assemble or bin variable and mobile regions, uneven annotation) changes the called gene or pathway content of a recovered genome.
>
> H1-02:B-0024 [1. Scope of the evidence] The first layer has direct measurements, although few.
>

Not found in the cited text (where to look, not what is wrong): holds: review; holds: its

## mag-recovery.2 (claim)

Whether the size of that change depends on properties of the sample has almost no measurements expressed in gene content; what exists are measurements of recovery quality, MAG yield and chimerism rates, which are proxies.

- conf: not stated
- class: not stated
- holds: the review's reading of the literature its search found; the review labels the proxies as such
- src: none (the reviewer's synthesis)
- trail: H1-02 §1. Scope

From the note:

> H1-02:B-0023 [1. Scope of the evidence] The second asks whether the size of that change depends on properties of the sample.
>
> H1-02:B-0025 [1. Scope of the evidence] The second has almost no measurements expressed in gene content.
>
> H1-02:B-0026 [1. Scope of the evidence] What it has are measurements of recovery quality, MAG yield and chimerism rates.
>
> H1-02:B-0027 [1. Scope of the evidence] These are proxies, and the review labels them as such.
>

Not found in the cited text (where to look, not what is wrong): holds: its

## mag-recovery.3 (claim)

In the review's search, one natural-sample study compared MAGs with isolate genomes of the same lineage from the same sample at gene level (Meziti et al.: eight E. coli pairs from human stool); a second study reused five of those pairs, so it is not independent. This is a statement about the search, not a structural fact of the literature: it omits SAG-referenced comparisons (Alneberg et al. 2018).

- conf: not stated
- class: search (critic: C-052)
- search: not stated
- holds: natural samples; comparisons against same-sample isolate genomes of the same lineage at gene level; SAG-referenced comparisons not covered
- src: mezitiReliabilityMetagenomeassembledGenomes2021, liCriticalAssessmentPangenomic2022, alnebergGenomesUncultivatedProkaryotes2018
- trail: H1-02 §1. Scope, §Adversarial

From the note:

> H1-02:B-0029 [1. Scope of the evidence] Only one natural-sample study compared MAGs with isolate genomes of the same lineage from the same sample at gene level [1]: eight E. coli pairs from human stool.
>
> H1-02:B-0030 [1. Scope of the evidence] A second study reused five of those pairs [2], so it is not independent.
>
> H1-02:C-052 [warning: Adversarial critique, full findings] - 'Only one natural-sample study compared MAGs with isolate genomes of the same lineage from the same sample at gene level' is framed as a structural fact of the literature. It is a statement about the search, and it omits SAG-referenced comparisons (Alneberg et al. 2018).
>

## completeness-estimates.1 (claim)

CheckM simulations found systematic overestimation of completeness under non-redundant contamination, and plasmids and phage were invisible to the estimates.

- conf: not stated
- class: model (note: "modelled")
- holds: CheckM's own simulations
- src: parksCheckMAssessingQuality2015
- trail: H1-02 §2.7

From the note:

> H1-02:B-0118 [2.7 Filters and corrections: real-sample validation] - Completeness estimation itself: CheckM simulations found systematic overestimation of completeness under non-redundant contamination, and plasmids and phage were invisible to the estimates [33] (modelled).
>

## completeness-estimates.2 (claim)

In Meziti et al., true recovery of the population's genes was on average 16.9% lower than the MiGA completeness estimate and 20.4% lower than the CheckM estimate: two average shortfalls against two estimators, not a range.

- conf: single (note: "single source")
- class: meas (note: "measured")
- holds: natural human gut; MaxBin 2.0 MAGs against isolate genomes from the same diarrhoeal stool samples; E. coli, n = 8 pairs
- src: mezitiReliabilityMetagenomeassembledGenomes2021
- trail: H1-02 §2.7, §critic

From the note:

> H1-02:B-0119 [2.7 Filters and corrections: real-sample validation] Meziti et al. found true recovery 16.9% to 20.4% below the estimates [1] (measured, natural, single source).
>
> H1-02:C-026 [danger: Critic: verdict partly supported] Figure-level errors: (i) [1]'s '16.9% to 20.4%' is not a range.
>
> H1-02:C-027 [danger: Critic: verdict partly supported] The paper reports average shortfalls against two estimators: 'lower than the completeness assessments of MiGA and CheckM, by 16.9% and 20.4%, respectively, on average'.
>
> H1-02:B-0032 [2.1 Direct same-sample comparisons (natural, human gut)] Meziti et al. [1] compared MaxBin 2.0 MAGs with isolate genomes from the same diarrhoeal stool samples.
>
> H1-02:C-002 [danger: Critic: verdict partly supported] In gut, one isolate-referenced study found that MAGs estimated about 95% complete held about 77% of population core genes and 50% of variable genes (n = 8 E. coli pairs; SINGLE SOURCE [1]; [2] reuses its data).
>

Not found in the cited text (where to look, not what is wrong): holds: human

## completeness-estimates.3 (claim)

The text of Meziti et al. gives MiGA completeness of its MAGs as 81.1% to 95.5%.

- conf: not stated
- class: not stated
- holds: Meziti et al.'s MaxBin 2.0 MAGs from diarrhoeal stool samples; the critic's reading of the paper
- src: mezitiReliabilityMetagenomeassembledGenomes2021
- trail: H1-02 §critic

From the note:

> H1-02:C-028 [danger: Critic: verdict partly supported] (ii) The quoted completeness range 81.1% to 97.2% mixes estimator columns.
>
> H1-02:C-029 [danger: Critic: verdict partly supported] The paper's text gives MiGA MAG completeness as 81.1% to 95.5%.
>
> H1-02:B-0032 [2.1 Direct same-sample comparisons (natural, human gut)] Meziti et al. [1] compared MaxBin 2.0 MAGs with isolate genomes from the same diarrhoeal stool samples.
>

## completeness-estimates.4 (claim)

Meziti et al. conclude that "the quality of MAGs may often be worse than estimated".

- conf: single (note: "SINGLE SOURCE")
- class: not stated
- holds: one species in one low-diversity host environment (MAGs and isolates from the same diarrhoeal stool samples)
- src: mezitiReliabilityMetagenomeassembledGenomes2021
- trail: H1-02 §2.1

From the note:

> H1-02:B-0032 [2.1 Direct same-sample comparisons (natural, human gut)] Meziti et al. [1] compared MaxBin 2.0 MAGs with isolate genomes from the same diarrhoeal stool samples.
>
> H1-02:B-0041 [2.1 Direct same-sample comparisons (natural, human gut)] The authors conclude that "the quality of MAGs may often be worse than estimated".
>
> H1-02:B-0042 [2.1 Direct same-sample comparisons (natural, human gut)] These figures are SINGLE SOURCE for one species in one low-diversity host environment.
>

## completeness-estimates.5 (claim)

CheckM and GUNC contamination estimates correlated at r = 0.2.

- conf: not stated
- class: meas (note: "measured")
- holds: natural samples, in Orakov et al.'s study of GUNC on CheckM-prefiltered MAG catalogues
- src: orakovGUNCDetectionChimerism2021
- trail: H1-02 §2.2

From the note:

> H1-02:B-0058 [2.2 Real-data artefacts without an isolate reference (natural)] Orakov et al. [9] found that GUNC flagged 15.1% to 29.9% of CheckM-prefiltered human gut MAG catalogues as chimeric at genus level or above.
>
> H1-02:B-0060 [2.2 Real-data artefacts without an isolate reference (natural)] CheckM and GUNC contamination estimates correlated at r = 0.2 (measured; natural).
>

Not found in the cited text (where to look, not what is wrong): holds: in

## completeness-estimates.6 (claim)

In an illustrative analysis, GTDB MAGs estimated 99.89% and 93.59% complete covered about 80% and 60% of same-species references; the authors state that habitat, strain and pipeline are confounded.

- conf: not stated
- class: not stated
- limit: access (note: "Seen only as search snippet (WebSearch); not fetched")
- holds: an opinion article; not used for any verdict, used for context only; the search agents disagreed on whether it was usable; the note's reference list reports its content while its not-obtained list says it was seen only as a search snippet
- src: pellegrinettiRethinkingMetagenomeAssembledGenome2026
- trail: H1-02 §References, §Search record

From the note:

> H1-02:R-0137 [References] [24] Pellegrinetti, Thierry Alexandre; Molligan, Joshua; Mendes, Lucas William; Pedrinho, Alexandre; Pérez-López, Edel (2026).
>
> H1-02:R-0138 [References] Rethinking metagenome-assembled genome completeness: are we truly recovering complete genomes?
>
> H1-02:R-0139 [References] Frontiers in Microbiology 17: 1884628. https://doi.org/10.3389/fmicb.2026.1884628 (opinion article with an illustrative analysis.
>
> H1-02:R-0140 [References] It reports GTDB MAGs estimated 99.89% and 93.59% complete that covered about 80% and 60% of same-species references.
>
> H1-02:R-0141 [References] The authors state that habitat, strain and pipeline are confounded.
>
> H1-02:R-0142 [References] Not used for any verdict)
>
> H1-02:R-0025 [failure: Sources not obtained] - (Frontiers in Microbiology 2026) Rethinking metagenome-assembled genome completeness: are we truly recovering complete genomes? https://doi.org/10.3389/fmicb.2026.1884628 (routes tried: Seen only as search snippet (WebSearch); not fetched.
>
> H1-02:B-0190 [Search record] The agents disagreed on the evidence class of [3] (measured against inferred) and on whether [13] and [24] were usable.
>
> H1-02:B-0191 [Search record] The review treats [3] as a measured association with an inferred artefact reading, and uses [13] and [24] for context only.
>

Not found in the cited text (where to look, not what is wrong): holds: its; holds: not-obtained

## content-loss.1 (claim)

MAGs with completeness estimates near 95% captured only 77% of the population core genes and 50% of the variable genes, on average, against isolate genomes from the same samples.

- conf: single (critic: C-002)
- class: meas (note: "evidence class: measured")
- holds: natural human gut; MaxBin 2.0 MAGs against isolate genomes from the same diarrhoeal stool samples; one species (E. coli), n = 8 pairs, metagenomes 0.21 to 2.8 Gbp; one low-diversity host environment; Li and Yin reuse its data, so they are not independent of it
- src: mezitiReliabilityMetagenomeassembledGenomes2021
- trail: H1-02 §2.1, §critic

From the note:

> H1-02:B-0032 [2.1 Direct same-sample comparisons (natural, human gut)] Meziti et al. [1] compared MaxBin 2.0 MAGs with isolate genomes from the same diarrhoeal stool samples.
>
> H1-02:B-0036 [2.1 Direct same-sample comparisons (natural, human gut)] In the authors' summary, MAGs "with completeness estimates near 95% captured only 77% of the population core genes and 50% of the variable genes, on average" (evidence class: measured; system: natural; regime: one species, n = 8 pairs, metagenomes 0.21 to 2.8 Gbp).
>
> H1-02:B-0042 [2.1 Direct same-sample comparisons (natural, human gut)] These figures are SINGLE SOURCE for one species in one low-diversity host environment.
>
> H1-02:C-002 [danger: Critic: verdict partly supported] In gut, one isolate-referenced study found that MAGs estimated about 95% complete held about 77% of population core genes and 50% of variable genes (n = 8 E. coli pairs; SINGLE SOURCE [1]; [2] reuses its data).
>
> H1-02:C-044 [warning: Adversarial critique, full findings] - Part A gut isolate-referenced losses (77% core, 50% variable genes; 11.31% to 34.7% core missed) rest on Meziti et al. [1] alone.
>
> H1-02:C-045 [warning: Adversarial critique, full findings] [2] reuses 5 of the same pairs, so it is not independent.
>

Not found in the cited text (where to look, not what is wrong): holds: human; holds: li; holds: yin

## content-loss.2 (claim)

Population core genes missed by the MAG ranged from 11.31% to 34.7% (mean 24.84%), and population-variable genes missed from 13.63% to 69.56% (mean 50.17%).

- conf: single (critic: C-044)
- class: meas (note: "evidence class: measured")
- holds: natural human gut; MAGs against isolate genomes from the same diarrhoeal stool samples; one species, n = 8 pairs
- src: mezitiReliabilityMetagenomeassembledGenomes2021
- trail: H1-02 §2.1, §Adversarial

From the note:

> H1-02:B-0032 [2.1 Direct same-sample comparisons (natural, human gut)] Meziti et al. [1] compared MaxBin 2.0 MAGs with isolate genomes from the same diarrhoeal stool samples.
>
> H1-02:B-0034 [2.1 Direct same-sample comparisons (natural, human gut)] Population core genes missed by the MAG ranged from 11.31% to 34.7% (mean 24.84%).
>
> H1-02:B-0035 [2.1 Direct same-sample comparisons (natural, human gut)] Population-variable genes missed ranged from 13.63% to 69.56% (mean 50.17%).
>
> H1-02:B-0036 [2.1 Direct same-sample comparisons (natural, human gut)] In the authors' summary, MAGs "with completeness estimates near 95% captured only 77% of the population core genes and 50% of the variable genes, on average" (evidence class: measured; system: natural; regime: one species, n = 8 pairs, metagenomes 0.21 to 2.8 Gbp).
>
> H1-02:C-044 [warning: Adversarial critique, full findings] - Part A gut isolate-referenced losses (77% core, 50% variable genes; 11.31% to 34.7% core missed) rest on Meziti et al. [1] alone.
>

Not found in the cited text (where to look, not what is wrong): holds: human

## content-loss.3 (claim)

Genes with low-identity matches plus genes that had been assembled but binned into other Enterobacteriaceae MAGs made up more than 95% of the missed genes. The paper attributes the low-identity share to sequence divergence from the isolate or to assembly errors, so part of the "loss" may be biology and not recovery; mis-binned genes were 16% to 71% (core) and 64% to 71% (variable) of those without homologs.

- conf: single (note: "SINGLE SOURCE")
- class: not stated
- holds: Meziti et al.; natural human gut (diarrhoeal stool); E. coli MAG-isolate pairs, n = 8
- src: mezitiReliabilityMetagenomeassembledGenomes2021
- trail: H1-02 §2.1, §critic, §Adversarial

From the note:

> H1-02:B-0032 [2.1 Direct same-sample comparisons (natural, human gut)] Meziti et al. [1] compared MaxBin 2.0 MAGs with isolate genomes from the same diarrhoeal stool samples.
>
> H1-02:B-0037 [2.1 Direct same-sample comparisons (natural, human gut)] Genes with low-identity matches plus genes that had been assembled but binned into other Enterobacteriaceae MAGs made up more than 95% of the missed genes.
>
> H1-02:B-0042 [2.1 Direct same-sample comparisons (natural, human gut)] These figures are SINGLE SOURCE for one species in one low-diversity host environment.
>
> H1-02:C-002 [danger: Critic: verdict partly supported] In gut, one isolate-referenced study found that MAGs estimated about 95% complete held about 77% of population core genes and 50% of variable genes (n = 8 E. coli pairs; SINGLE SOURCE [1]; [2] reuses its data).
>
> H1-02:C-031 [danger: Critic: verdict partly supported] The low-identity share of missed genes is attributed to sequence divergence from the isolate or to assembly errors.
>
> H1-02:C-032 [danger: Critic: verdict partly supported] Mis-binned genes were 16% to 71% (core) and 64% to 71% (variable) of those without homologs.
>
> H1-02:C-086 [warning: Adversarial critique, full findings] [1] attributes low-identity missed genes to sequence differences from the isolate or to assembly errors, so part of the 'loss' may be biology and not recovery.
>

Not found in the cited text (where to look, not what is wrong): holds: human

## content-loss.4 (claim)

When five of Meziti et al.'s E. coli MAGs, or their paired isolates, were mixed with complete genomes, the MAGs lost about 25% of core genes at a 100% core threshold.

- conf: not stated
- class: meas (note: "measured")
- limit: access (note: "the detail is in a supplementary figure that none of the search agents read")
- holds: natural; n = 5 real pairs from human stool, reused from Meziti et al., so not independent of it; the critic: if the 25% comes from Supp. Fig. S14 rather than a main-text statement, it is a full-text breach, and the review should quote the main-text sentence or drop the figure
- src: liCriticalAssessmentPangenomic2022 (the detail is in a supplementary figure that none of the search agents read)
- trail: H1-02 §2.1, §Adversarial

From the note:

> H1-02:B-0029 [1. Scope of the evidence] Only one natural-sample study compared MAGs with isolate genomes of the same lineage from the same sample at gene level [1]: eight E. coli pairs from human stool.
>
> H1-02:B-0030 [1. Scope of the evidence] A second study reused five of those pairs [2], so it is not independent.
>
> H1-02:B-0043 [2.1 Direct same-sample comparisons (natural, human gut)] Li and Yin [2] mixed five of these E. coli MAGs, or their paired isolates, with complete genomes.
>
> H1-02:B-0044 [2.1 Direct same-sample comparisons (natural, human gut)] The MAGs lost about 25% of core genes at a 100% core threshold (measured; natural; n = 5; the detail is in a supplementary figure that none of the search agents read).
>
> H1-02:C-035 [warning: Adversarial critique, full findings] - Li and Yin [2]: 'MAGs lost about 25% of core genes at a 100% core threshold' in real pairs.
>
> H1-02:C-036 [warning: Adversarial critique, full findings] The review says the detail is in Supp. Fig. S14, which no agent read.
>
> H1-02:C-037 [warning: Adversarial critique, full findings] If the 25% comes from that figure rather than a main-text statement, it is a full-text breach.
>
> H1-02:C-038 [warning: Adversarial critique, full findings] The review should quote the main-text sentence or drop the figure.
>

Not found in the cited text (where to look, not what is wrong): Meziti; holds: meziti

## content-loss.5 (claim)

In curated MAGs compared with ten isolate genomes from the same cultures, genomes at 10x coverage or more had over 90% of their sequence recovered (85% at 11x; about 40% at 3.9x).

- conf: not stated
- class: meas (note: "measured")
- holds: engineered: two laboratory enrichment consortia
- src: nelsonBiasesGenomeReconstruction2020
- trail: H1-02 §2.4

From the note:

> H1-02:B-0067 [2.4 Which regions are lost (engineered, simulated, and one soil)] Nelson et al. [5] compared curated MAGs from two laboratory enrichment consortia with ten isolate genomes from the same cultures.
>
> H1-02:B-0068 [2.4 Which regions are lost (engineered, simulated, and one soil)] Genomes at 10x coverage or more had over 90% of their sequence recovered (85% at 11x; about 40% at 3.9x).
>
> H1-02:B-0070 [2.4 Which regions are lost (engineered, simulated, and one soil)] The authors conclude that reconstructions above 90% completeness "are likely to effectively represent organismal function", while uneven plasmid distribution "can lead to incorrect inferences" (measured; engineered).
>

## content-loss.6 (claim)

Regions not binned were enriched in repeats, atypical composition, rRNAs, tRNAs, transposases and genes of unknown function, and two plasmids were missed entirely.

- conf: not stated
- class: meas (note: "measured")
- holds: engineered: curated MAGs from two laboratory enrichment consortia against ten isolate genomes from the same cultures
- src: nelsonBiasesGenomeReconstruction2020
- trail: H1-02 §2.4

From the note:

> H1-02:B-0067 [2.4 Which regions are lost (engineered, simulated, and one soil)] Nelson et al. [5] compared curated MAGs from two laboratory enrichment consortia with ten isolate genomes from the same cultures.
>
> H1-02:B-0069 [2.4 Which regions are lost (engineered, simulated, and one soil)] Not-binned regions were enriched in repeats, atypical composition, rRNAs, tRNAs, transposases and genes of unknown function, and two plasmids were missed entirely.
>
> H1-02:B-0070 [2.4 Which regions are lost (engineered, simulated, and one soil)] The authors conclude that reconstructions above 90% completeness "are likely to effectively represent organismal function", while uneven plasmid distribution "can lead to incorrect inferences" (measured; engineered).
>

## content-loss.7 (claim)

Nelson et al. conclude that reconstructions above 90% completeness "are likely to effectively represent organismal function", while uneven plasmid distribution "can lead to incorrect inferences"; the review counts the conclusion as a bounding fact, but an engineered one.

- conf: not stated
- class: meas (note: "measured")
- holds: engineered: two laboratory enrichment consortia
- src: nelsonBiasesGenomeReconstruction2020
- trail: H1-02 §2.4, §2.6

From the note:

> H1-02:B-0067 [2.4 Which regions are lost (engineered, simulated, and one soil)] Nelson et al. [5] compared curated MAGs from two laboratory enrichment consortia with ten isolate genomes from the same cultures.
>
> H1-02:B-0070 [2.4 Which regions are lost (engineered, simulated, and one soil)] The authors conclude that reconstructions above 90% completeness "are likely to effectively represent organismal function", while uneven plasmid distribution "can lead to incorrect inferences" (measured; engineered).
>
> H1-02:B-0105 [2.6 Bounding and negative facts] - Nelson et al.'s conclusion above [5] is also bounding, but it is engineered.
>

## content-loss.8 (claim)

A companion analysis of Tara Oceans MAGs, inferred from composition statistics against unrelated RefSeq genomes, found lower repeat content in MAGs, consistent with the same exclusion operating in natural marine data.

- conf: not stated
- class: deriv (note: "inferred from composition statistics")
- holds: natural marine (Tara Oceans MAGs); against unrelated RefSeq genomes, not isolates from the same samples
- src: nelsonBiasesGenomeReconstruction2020
- trail: H1-02 §2.4

From the note:

> H1-02:B-0071 [2.4 Which regions are lost (engineered, simulated, and one soil)] The paper's companion analysis of Tara Oceans MAGs was inferred from composition statistics against unrelated RefSeq genomes.
>
> H1-02:B-0072 [2.4 Which regions are lost (engineered, simulated, and one soil)] It found lower repeat content in MAGs, consistent with the same exclusion operating in natural marine data.
>

## content-loss.9 (claim)

Across 12 assembler and binner combinations, 82% to 94% of chromosomes were recovered, against 38% to 44% of genomic islands and 1% to 29% of plasmids.

- conf: not stated
- class: model (note: "modelled")
- holds: a simulated 30-genome short-read metagenome
- src: maguireMetagenomeAssembledGenomeBinning2020
- trail: H1-02 §2.4

From the note:

> H1-02:B-0073 [2.4 Which regions are lost (engineered, simulated, and one soil)] Maguire et al. [4] simulated a 30-genome short-read metagenome.
>
> H1-02:B-0074 [2.4 Which regions are lost (engineered, simulated, and one soil)] Across 12 assembler and binner combinations, 82% to 94% of chromosomes were recovered, against 38% to 44% of genomic islands and 1% to 29% of plasmids.
>
> H1-02:B-0075 [2.4 Which regions are lost (engineered, simulated, and one soil)] No plasmid-borne AMR or virulence gene was binned correctly (modelled; engineered).
>

## content-loss.10 (claim)

No plasmid-borne AMR or virulence gene was binned correctly.

- conf: not stated
- class: model (note: "modelled")
- holds: a simulated 30-genome short-read metagenome
- src: maguireMetagenomeAssembledGenomeBinning2020
- trail: H1-02 §2.4

From the note:

> H1-02:B-0073 [2.4 Which regions are lost (engineered, simulated, and one soil)] Maguire et al. [4] simulated a 30-genome short-read metagenome.
>
> H1-02:B-0075 [2.4 Which regions are lost (engineered, simulated, and one soil)] No plasmid-borne AMR or virulence gene was binned correctly (modelled; engineered).
>

## content-loss.11 (claim)

Most binners lose plasmids.

- conf: not stated
- class: model (note: "modelled")
- holds: the CAMI II benchmark
- src: meyerCriticalAssessmentMetagenome2022
- trail: H1-02 §2.4

From the note:

> H1-02:B-0076 [2.4 Which regions are lost (engineered, simulated, and one soil)] CAMI II [7] likewise found that most binners lose plasmids (modelled).
>

## content-loss.12 (claim)

Checked against a PacBio HiFi assembly of the same system, only 24 of 614 long-read bins had at least half their 1 kb segments fully recovered by short reads, while 490 had at least half not recovered.

- conf: not stated
- class: meas (note: "measured")
- holds: natural soil: one biocrust community, one site; the reference is long-read bins, not isolates; the review's only natural soil evidence
- src: bergComparisonShortreadLongread2025
- trail: H1-02 §2.4

From the note:

> H1-02:B-0077 [2.4 Which regions are lost (engineered, simulated, and one soil)] Berg et al. [26] provide the only natural soil evidence.
>
> H1-02:B-0078 [2.4 Which regions are lost (engineered, simulated, and one soil)] In a biocrust community, short-read assemblies were checked against a PacBio HiFi assembly of the same system.
>
> H1-02:B-0079 [2.4 Which regions are lost (engineered, simulated, and one soil)] Of 614 long-read bins, only 24 had at least half their 1 kb segments fully recovered by short reads, while 490 had at least half not recovered.
>
> H1-02:B-0081 [2.4 Which regions are lost (engineered, simulated, and one soil)] The authors conclude that short-read metagenomes "can possibly underestimate the diversity of these genome regions" (measured; natural; one site; the reference is long-read bins, not isolates).
>

Not found in the cited text (where to look, not what is wrong): holds: review

## content-loss.13 (claim)

Segments missed by short-read assembly were low-coverage or came from populations with high sequence variation, and they were enriched in mobile-element and defence functions; the authors conclude that short-read metagenomes "can possibly underestimate the diversity of these genome regions".

- conf: not stated
- class: meas (note: "measured")
- holds: natural soil: one biocrust community, one site; short-read assemblies against a PacBio HiFi assembly of the same system
- src: bergComparisonShortreadLongread2025
- trail: H1-02 §2.4, §3.3

From the note:

> H1-02:B-0078 [2.4 Which regions are lost (engineered, simulated, and one soil)] In a biocrust community, short-read assemblies were checked against a PacBio HiFi assembly of the same system.
>
> H1-02:B-0080 [2.4 Which regions are lost (engineered, simulated, and one soil)] Missed segments were low-coverage or came from populations with high sequence variation, and they were enriched in mobile-element and defence functions.
>
> H1-02:B-0081 [2.4 Which regions are lost (engineered, simulated, and one soil)] The authors conclude that short-read metagenomes "can possibly underestimate the diversity of these genome regions" (measured; natural; one site; the reference is long-read bins, not isolates).
>
> H1-02:B-0139 [3.3 Soil (natural)] - Berg et al. [26] tie short-read assembly loss to within-sample coverage and population sequence variation.
>

Not found in the cited text (where to look, not what is wrong): holds: soil

## content-loss.14 (claim)

The soil short-read loss of variable regions concerns assembly, not the gene content of binned genomes compared across samples, so it is indirect support only for soils.

- conf: not stated
- class: not stated
- holds: one natural biocrust soil
- src: bergComparisonShortreadLongread2025
- trail: H1-02 §2.4, §Verdict as delivered, §5. Verdicts

From the note:

> H1-02:B-0082 [2.4 Which regions are lost (engineered, simulated, and one soil)] This concerns assembly, not the gene content of binned genomes compared across samples.
>
> H1-02:A-005 [quote: Verdict as delivered] One natural biocrust soil shows systematic short-read assembly loss of variable regions [26], which is indirect support only.
>
> H1-02:A-026 [5. Verdicts] Berg et al. [26] is indirect support.
>

## content-loss.15 (claim)

Transposase copies fell at the breakpoints of short-read assemblies of P. copri.

- conf: not stated
- class: not stated
- holds: qualitative only; given in the reference list and not cited in the body for any figure
- src: mossCompleteClosedBacterial2020
- trail: H1-02 §References

From the note:

> H1-02:R-0120 [References] [18] Moss, Eli L.; Maghini, Dylan G.; Bhatt, Ami S. (2020).
>
> H1-02:R-0121 [References] Complete, closed bacterial genomes from microbiomes using nanopore sequencing.
>
> H1-02:R-0122 [References] Nature Biotechnology 38(6): 701-707. https://doi.org/10.1038/s41587-020-0422-6 (qualitative only: transposase copies fell at the breakpoints of short-read assemblies of P. copri; not cited in the body for any figure)
>

## contamination-gain.1 (claim)

MAG-specific genes were 2.35% to 26.41% of MAG gene content (mean 14.42%).

- conf: single (note: "SINGLE SOURCE")
- class: not stated
- holds: natural human gut; MaxBin 2.0 MAGs against isolate genomes from the same diarrhoeal stool samples; one species in one low-diversity host environment
- src: mezitiReliabilityMetagenomeassembledGenomes2021
- trail: H1-02 §2.1

From the note:

> H1-02:B-0032 [2.1 Direct same-sample comparisons (natural, human gut)] Meziti et al. [1] compared MaxBin 2.0 MAGs with isolate genomes from the same diarrhoeal stool samples.
>
> H1-02:B-0039 [2.1 Direct same-sample comparisons (natural, human gut)] On the gain side, MAG-specific genes were 2.35% to 26.41% of MAG gene content (mean 14.42%).
>
> H1-02:B-0042 [2.1 Direct same-sample comparisons (natural, human gut)] These figures are SINGLE SOURCE for one species in one low-diversity host environment.
>

Not found in the cited text (where to look, not what is wrong): holds: human; holds: gut

## contamination-gain.2 (claim)

Sequence not classified as Enterobacteriaceae averaged 4.4% of the MAGs, above the MiGA contamination estimates (0.9% to 2.7%).

- conf: single (note: "SINGLE SOURCE")
- class: not stated
- holds: natural human gut; MaxBin 2.0 MAGs from diarrhoeal stool samples; one species in one low-diversity host environment
- src: mezitiReliabilityMetagenomeassembledGenomes2021
- trail: H1-02 §2.1

From the note:

> H1-02:B-0032 [2.1 Direct same-sample comparisons (natural, human gut)] Meziti et al. [1] compared MaxBin 2.0 MAGs with isolate genomes from the same diarrhoeal stool samples.
>
> H1-02:B-0040 [2.1 Direct same-sample comparisons (natural, human gut)] Sequence not classified as Enterobacteriaceae averaged 4.4%, above the MiGA contamination estimates (0.9% to 2.7%).
>
> H1-02:B-0042 [2.1 Direct same-sample comparisons (natural, human gut)] These figures are SINGLE SOURCE for one species in one low-diversity host environment.
>

Not found in the cited text (where to look, not what is wrong): holds: human; holds: gut

## contamination-gain.3 (claim)

Of 86 Lachnospiraceae genes that differed in prevalence between cirrhosis cases and controls, 33 (38%) were probable contaminants from disease-associated genera.

- conf: single (critic: C-051)
- class: meas (note: "measured")
- holds: natural human gut; one cirrhosis case-control cohort re-analysed with UHGG/MIDAS2 pangenomes; one family, Lachnospiraceae; the differential calls come from MIDAS2 read mapping to a reference pangenome that was partly contaminated, not from comparing genomes recovered from different samples
- src: majernikSmallAmountsMisassembly2025
- trail: H1-02 §2.2, §Adversarial

From the note:

> H1-02:B-0045 [2.2 Real-data artefacts without an isolate reference (natural)] Majernik et al. [22] re-analysed a cirrhosis case-control gut cohort with UHGG/MIDAS2 pangenomes.
>
> H1-02:B-0046 [2.2 Real-data artefacts without an isolate reference (natural)] Of 86 Lachnospiraceae genes that differed in prevalence between cases and controls, 33 (38%) were probable contaminants from disease-associated genera.
>
> H1-02:B-0048 [2.2 Real-data artefacts without an isolate reference (natural)] In the Lachnospira eligens pangenome, 22% of accessory genes had lineage-discordant annotation, against 7.6% when only isolate-derived genes were counted (measured; natural; one study, one disease contrast; SINGLE SOURCE).
>
> H1-02:C-051 [warning: Adversarial critique, full findings] - Contamination-driven false gene associations (38%, 33/86) come from one cirrhosis cohort and one family, Lachnospiraceae [22]. The quick re-run on Bacteroides thetaiotaomicron was 30 genes in the same data set.
>
> H1-02:C-082 [warning: Adversarial critique, full findings] The differential calls come from MIDAS2 read mapping to a reference pangenome that was partly contaminated.
>
> H1-02:C-083 [warning: Adversarial critique, full findings] They are not content differences between genomes recovered from different samples, so the review stretches [22] toward the brief's question without stating the mechanism difference.
>

Not found in the cited text (where to look, not what is wrong): holds: human

## contamination-gain.4 (claim)

Twenty-six of the 33 contaminant genes came from single assemblies with a mean CheckM contamination of 0.22%, and GUNC flagged none of them: the contaminants sat below 5% CheckM contamination.

- conf: not stated
- class: not stated
- holds: natural human gut; one cirrhosis case-control cohort (UHGG/MIDAS2 pangenomes); the critic confirms the figure in full text
- src: majernikSmallAmountsMisassembly2025
- trail: H1-02 §2.2, §Adversarial

From the note:

> H1-02:B-0045 [2.2 Real-data artefacts without an isolate reference (natural)] Majernik et al. [22] re-analysed a cirrhosis case-control gut cohort with UHGG/MIDAS2 pangenomes.
>
> H1-02:B-0046 [2.2 Real-data artefacts without an isolate reference (natural)] Of 86 Lachnospiraceae genes that differed in prevalence between cases and controls, 33 (38%) were probable contaminants from disease-associated genera.
>
> H1-02:B-0047 [2.2 Real-data artefacts without an isolate reference (natural)] Twenty-six of these came from single assemblies with a mean CheckM contamination of 0.22%, and GUNC flagged none of them.
>
> H1-02:C-092 [warning: Adversarial critique, full findings] Persistence above completeness thresholds has direct support in full text: [6] reports '20-40% of near-complete' MAGs lacking ribosomal protein genes, and [22] reports contaminants below 5% CheckM contamination that GUNC did not flag.
>

Not found in the cited text (where to look, not what is wrong): holds: human

## contamination-gain.5 (claim)

In the Lachnospira eligens pangenome, 22% of accessory genes had lineage-discordant annotation, against 7.6% when only isolate-derived genes were counted.

- conf: single (note: "SINGLE SOURCE")
- class: meas (note: "measured")
- holds: natural human gut; one study, one disease contrast (a cirrhosis case-control cohort, UHGG/MIDAS2 pangenomes)
- src: majernikSmallAmountsMisassembly2025
- trail: H1-02 §2.2

From the note:

> H1-02:B-0045 [2.2 Real-data artefacts without an isolate reference (natural)] Majernik et al. [22] re-analysed a cirrhosis case-control gut cohort with UHGG/MIDAS2 pangenomes.
>
> H1-02:B-0048 [2.2 Real-data artefacts without an isolate reference (natural)] In the Lachnospira eligens pangenome, 22% of accessory genes had lineage-discordant annotation, against 7.6% when only isolate-derived genes were counted (measured; natural; one study, one disease contrast; SINGLE SOURCE).
>

Not found in the cited text (where to look, not what is wrong): holds: human

## contamination-gain.6 (claim)

A quick re-run on Bacteroides thetaiotaomicron gave 30 genes in the same data set.

- conf: not stated
- class: not stated
- holds: the same cirrhosis cohort data set; the critic's reading of the paper
- src: majernikSmallAmountsMisassembly2025
- trail: H1-02 §Adversarial

From the note:

> H1-02:C-051 [warning: Adversarial critique, full findings] - Contamination-driven false gene associations (38%, 33/86) come from one cirrhosis cohort and one family, Lachnospiraceae [22]. The quick re-run on Bacteroides thetaiotaomicron was 30 genes in the same data set.
>

## contamination-gain.7 (claim)

Contamination of a reference pangenome produced false differential gene prevalence between sample groups; the calls come from read mapping to UHGG, not from comparing recovered genomes.

- conf: single (critic: C-003)
- class: not stated
- holds: natural human gut; one cirrhosis cohort; MIDAS2 read mapping to a partly contaminated reference pangenome
- src: majernikSmallAmountsMisassembly2025
- trail: H1-02 §critic, §Adversarial

From the note:

> H1-02:C-003 [danger: Critic: verdict partly supported] Separately, contamination of a reference pangenome produced false differential gene prevalence between sample groups (SINGLE SOURCE [22]; the calls come from read mapping to UHGG, not from comparing recovered genomes).
>
> H1-02:C-018 [danger: Critic: verdict partly supported] [22] measures false differential prevalence from reads mapped to a contaminated reference pangenome, not content differences between genomes recovered from different samples.
>
> H1-02:C-051 [warning: Adversarial critique, full findings] - Contamination-driven false gene associations (38%, 33/86) come from one cirrhosis cohort and one family, Lachnospiraceae [22]. The quick re-run on Bacteroides thetaiotaomicron was 30 genes in the same data set.
>
> H1-02:C-081 [warning: Adversarial critique, full findings] - [22] is presented as a case where contamination 'produced apparent content differences between sample groups' of recovered genomes.
>
> H1-02:C-082 [warning: Adversarial critique, full findings] The differential calls come from MIDAS2 read mapping to a reference pangenome that was partly contaminated.
>
> H1-02:C-083 [warning: Adversarial critique, full findings] They are not content differences between genomes recovered from different samples, so the review stretches [22] toward the brief's question without stating the mechanism difference.
>

Not found in the cited text (where to look, not what is wrong): holds: human; holds: gut

## contamination-gain.8 (claim)

After refinement of a composite Saccharibacteria MAG, a pangenome built with other Saccharibacteria genomes gained seven times as many single-copy core genes.

- conf: not stated
- class: meas (note: "measured")
- holds: natural; co-assembled oral plaque metagenomes; three MAGs; a letter
- src: shaiberCompositeMetagenomeAssembledGenomes2019
- trail: H1-02 §2.2

From the note:

> H1-02:B-0056 [2.2 Real-data artefacts without an isolate reference (natural)] Shaiber and Eren [8] refined a composite Saccharibacteria MAG from co-assembled oral plaque metagenomes.
>
> H1-02:B-0057 [2.2 Real-data artefacts without an isolate reference (natural)] After refinement, a pangenome built with other Saccharibacteria genomes gained seven times as many single-copy core genes (measured; natural; three MAGs; letter).
>

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

Not found in the cited text (where to look, not what is wrong): holds: re-opened

## contamination-gain.10 (claim)

In the multi-habitat GMGC set, GUNC flagged 9.4% of MIMAG high-quality MAGs and 20.5% of genomes passing CheckM's contamination threshold of under 5%.

- conf: not stated
- class: meas (note: "The study measures chimerism")
- holds: natural, multi-habitat (GMGC); chimerism, not called gene content
- src: orakovGUNCDetectionChimerism2021
- trail: H1-02 §2.2

From the note:

> H1-02:B-0058 [2.2 Real-data artefacts without an isolate reference (natural)] Orakov et al. [9] found that GUNC flagged 15.1% to 29.9% of CheckM-prefiltered human gut MAG catalogues as chimeric at genus level or above.
>
> H1-02:B-0059 [2.2 Real-data artefacts without an isolate reference (natural)] In the multi-habitat GMGC set, 9.4% of MIMAG high-quality MAGs were flagged, and so were 20.5% of genomes passing CheckM's contamination threshold of under 5%.
>
> H1-02:B-0061 [2.2 Real-data artefacts without an isolate reference (natural)] The study measures chimerism, not called gene content.
>

## contamination-gain.11 (claim)

In one chimerism survey (Orakov et al.) and one species-level case study (Majernik et al.), genomes that passed the contamination filters in use still carried chimeric or contaminant material.

- conf: not stated
- class: not stated
- holds: human gut and the multi-habitat GMGC set (Orakov et al.); one cirrhosis cohort, Lachnospiraceae (Majernik et al.)
- src: orakovGUNCDetectionChimerism2021, majernikSmallAmountsMisassembly2025
- trail: H1-02 §2.2, §Adversarial

From the note:

> H1-02:B-0045 [2.2 Real-data artefacts without an isolate reference (natural)] Majernik et al. [22] re-analysed a cirrhosis case-control gut cohort with UHGG/MIDAS2 pangenomes.
>
> H1-02:B-0058 [2.2 Real-data artefacts without an isolate reference (natural)] Orakov et al. [9] found that GUNC flagged 15.1% to 29.9% of CheckM-prefiltered human gut MAG catalogues as chimeric at genus level or above.
>
> H1-02:B-0059 [2.2 Real-data artefacts without an isolate reference (natural)] In the multi-habitat GMGC set, 9.4% of MIMAG high-quality MAGs were flagged, and so were 20.5% of genomes passing CheckM's contamination threshold of under 5%.
>
> H1-02:B-0062 [2.2 Real-data artefacts without an isolate reference (natural)] Taken with [22], it shows that the contamination filters in common use leave chimeric material in place.
>
> H1-02:C-048 [warning: Adversarial critique, full findings] - 'Taken with [22], it shows that the contamination filters in common use leave chimeric material in place' (Section 2.2) generalises to 'filters in common use' from one chimerism survey [9] plus one species-level case study [22].
>
> H1-02:C-051 [warning: Adversarial critique, full findings] - Contamination-driven false gene associations (38%, 33/86) come from one cirrhosis cohort and one family, Lachnospiraceae [22]. The quick re-run on Bacteroides thetaiotaomicron was 30 genes in the same data set.
>

## gene-class-specificity.1 (claim)

Core ribosomal protein genes "could be missing in more than 20-40% of near-complete" MAGs in four of five short-read catalogues (seawater, human gut, chicken gut, rice phyllosphere).

- conf: not stated
- class: meas (note: "measured")
- holds: natural; more than 190,000 MAGs; short-read catalogues; the critic confirms the figure in full text
- src: miseUnexpectedAbsenceRibosomal2022
- trail: H1-02 §2.2, §Adversarial

From the note:

> H1-02:B-0050 [2.2 Real-data artefacts without an isolate reference (natural)] Mise and Iwasaki [6] examined more than 190,000 MAGs.
>
> H1-02:B-0051 [2.2 Real-data artefacts without an isolate reference (natural)] Core ribosomal protein genes "could be missing in more than 20-40% of near-complete" MAGs in four of five short-read catalogues (seawater, human gut, chicken gut, rice phyllosphere).
>
> H1-02:B-0054 [2.2 Real-data artefacts without an isolate reference (natural)] Against phylogenetically close RefSeq genomes (not the same strains), CRISPR arrays and transposases were depleted in MAGs above 90% completeness, while glycolysis genes were not (measured; natural).
>
> H1-02:C-092 [warning: Adversarial critique, full findings] Persistence above completeness thresholds has direct support in full text: [6] reports '20-40% of near-complete' MAGs lacking ribosomal protein genes, and [22] reports contaminants below 5% CheckM contamination that GUNC did not flag.
>

## gene-class-specificity.2 (claim)

The ribosomal-protein deficit was absent from the GEM catalogue and from long-read or hybrid MAGs.

- conf: not stated
- class: meas (note: "measured")
- holds: natural; more than 190,000 MAGs across catalogues
- src: miseUnexpectedAbsenceRibosomal2022
- trail: H1-02 §2.2

From the note:

> H1-02:B-0050 [2.2 Real-data artefacts without an isolate reference (natural)] Mise and Iwasaki [6] examined more than 190,000 MAGs.
>
> H1-02:B-0052 [2.2 Real-data artefacts without an isolate reference (natural)] The deficit was absent from the GEM catalogue and from long-read or hybrid MAGs.
>
> H1-02:B-0054 [2.2 Real-data artefacts without an isolate reference (natural)] Against phylogenetically close RefSeq genomes (not the same strains), CRISPR arrays and transposases were depleted in MAGs above 90% completeness, while glycolysis genes were not (measured; natural).
>

## gene-class-specificity.3 (claim)

Raw reads carried the ribosomal protein genes, and single-amplified genomes did not show the deficit, so the authors locate the loss at tetranucleotide-based binning.

- conf: not stated
- class: meas (note: "measured")
- holds: natural; MAG catalogues with their raw reads and single-amplified genomes
- src: miseUnexpectedAbsenceRibosomal2022
- trail: H1-02 §2.2

From the note:

> H1-02:B-0050 [2.2 Real-data artefacts without an isolate reference (natural)] Mise and Iwasaki [6] examined more than 190,000 MAGs.
>
> H1-02:B-0053 [2.2 Real-data artefacts without an isolate reference (natural)] Raw reads carried the genes, and single-amplified genomes did not show the deficit, so the authors locate the loss at tetranucleotide-based binning.
>
> H1-02:B-0054 [2.2 Real-data artefacts without an isolate reference (natural)] Against phylogenetically close RefSeq genomes (not the same strains), CRISPR arrays and transposases were depleted in MAGs above 90% completeness, while glycolysis genes were not (measured; natural).
>

## gene-class-specificity.4 (claim)

Against phylogenetically close RefSeq genomes (not the same strains), CRISPR arrays and transposases were depleted in MAGs above 90% completeness, while glycolysis genes were not.

- conf: not stated
- class: meas (note: "measured")
- holds: natural MAGs above 90% completeness; the reference is close RefSeq genomes, not the same strains
- src: miseUnexpectedAbsenceRibosomal2022
- trail: H1-02 §2.2

From the note:

> H1-02:B-0054 [2.2 Real-data artefacts without an isolate reference (natural)] Against phylogenetically close RefSeq genomes (not the same strains), CRISPR arrays and transposases were depleted in MAGs above 90% completeness, while glycolysis genes were not (measured; natural).
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

Not found in the cited text (where to look, not what is wrong): holds: short-read; holds: mag; holds: review

## gene-class-specificity.6 (claim)

When 11 soil, seawater and gut metagenomes were assembled at three depths with two assemblers, contigs carrying ribosomal-protein genes were longer "regardless of environmental origins of samples, sequencing depths, and assemblers", and soil gave the shortest contigs. The review left this bounding fact out and cites Mise and Iwasaki only for gut and seawater.

- conf: not stated
- class: not stated
- holds: natural agricultural and paddy soil, seawater and gut metagenomes; assembly of a specific gene class; the critic's reading of the paper
- src: miseUnexpectedAbsenceRibosomal2022
- trail: H1-02 §critic, §Adversarial

From the note:

> H1-02:C-013 [danger: Critic: verdict partly supported] One bounding fact across soil, seawater and gut (ribosomal-protein contigs assembled well regardless of environment, three depths and two assemblers [6]) was omitted.
>
> H1-02:C-068 [warning: Adversarial critique, full findings] - gap: Mise and Iwasaki [6] assembled 11 soil, seawater and gut metagenomes at three depths with two assemblers.
>
> H1-02:C-069 [warning: Adversarial critique, full findings] Contigs carrying ribosomal-protein genes were longer 'regardless of environmental origins of samples, sequencing depths, and assemblers'.
>
> H1-02:C-070 [warning: Adversarial critique, full findings] Soil gave the shortest contigs.
>
> H1-02:C-072 [warning: Adversarial critique, full findings] This is a bounding fact relevant to Part B soil and depth, but the review cites [6] only for gut and seawater.; setting_or_class: Agricultural and paddy soil metagenomes; depth dependence of assembly of specific gene classes; brief_bullet: Re-read [6] Fig. 3 and Supp. Fig. S1 for soil and depth; check whether any other study reports gene-class recovery against depth in soil.
>

## gene-class-specificity.7 (claim)

The ribosomal-protein deficit was absent in Planctomycetota, Verrucomicrobiota and Acidobacteriota.

- conf: not stated
- class: not stated
- holds: the soil, seawater and gut metagenomes Mise and Iwasaki assembled; the critic's reading of the paper
- src: miseUnexpectedAbsenceRibosomal2022
- trail: H1-02 §Adversarial

From the note:

> H1-02:C-068 [warning: Adversarial critique, full findings] - gap: Mise and Iwasaki [6] assembled 11 soil, seawater and gut metagenomes at three depths with two assemblers.
>
> H1-02:C-071 [warning: Adversarial critique, full findings] The deficit was absent in Planctomycetota, Verrucomicrobiota and Acidobacteriota.
>

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

Not found in the cited text (where to look, not what is wrong): holds: coastal

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

Not found in the cited text (where to look, not what is wrong): holds: coastal; holds: marine

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

Not found in the cited text (where to look, not what is wrong): holds: coastal

## pathway-completeness.1 (claim)

A rise in CheckM completeness from 70% to 100% was associated with a 15 ± 10% increase in DRAM KEGG module fullness, and the association held above 90% completeness.

- conf: not stated
- class: meas (note: "treated here as a measured association")
- holds: 11,842 GTDB genomes, a cross-genome regression; the search agents disagreed on its class (measured versus inferred), and the review treats it as a measured association with an inferred causal reading; the note lists it among the sources re-verified in full text, while the critic says it rests on agent reads
- src: eisenhoferImpactMicrobialGenome2023
- trail: H1-02 §2.5, §Search record, §Adversarial

From the note:

> H1-02:B-0083 [2.5 Incompleteness and pathway completeness] Eisenhofer et al. [3] regressed DRAM KEGG module fullness on CheckM completeness across 11,842 GTDB genomes.
>
> H1-02:B-0084 [2.5 Incompleteness and pathway completeness] A rise in completeness from 70% to 100% was associated with a 15 ± 10% increase in module fullness, and the association held above 90% completeness.
>
> H1-02:B-0087 [2.5 Incompleteness and pathway completeness] The search agents disagreed on its class (measured versus inferred); it is treated here as a measured association with an inferred causal reading.
>
> H1-02:B-0012 [info: Provenance] Load-bearing figures were re-verified in full text: - Meziti 2021, via PMC HTML with a browser user agent. - Mise and Iwasaki 2022, Orellana 2023, Eisenhofer 2023 and Nelson 2020, via Europe PMC fullTextXML. - Berg 2025 (PMC12634412) and Kim 2026 (PMC13079874), via Europe PMC fullTextXML.
>
> H1-02:B-0190 [Search record] The agents disagreed on the evidence class of [3] (measured against inferred) and on whether [13] and [24] were usable.
>
> H1-02:B-0191 [Search record] The review treats [3] as a measured association with an inferred artefact reading, and uses [13] and [24] for context only.
>
> H1-02:C-093 [warning: Adversarial critique, full findings] [3] and [9] rest on agent reads.
>

Not found in the cited text (where to look, not what is wrong): holds: cross-genome

## pathway-completeness.2 (claim)

The association of module fullness with completeness differed by phylum and metabolic domain, with nucleotide metabolism and secondary-metabolite biosynthesis most affected.

- conf: not stated
- class: meas (note: "treated here as a measured association")
- holds: 11,842 GTDB genomes; DRAM KEGG modules
- src: eisenhoferImpactMicrobialGenome2023
- trail: H1-02 §2.5

From the note:

> H1-02:B-0083 [2.5 Incompleteness and pathway completeness] Eisenhofer et al. [3] regressed DRAM KEGG module fullness on CheckM completeness across 11,842 GTDB genomes.
>
> H1-02:B-0085 [2.5 Incompleteness and pathway completeness] It differed by phylum and metabolic domain, with nucleotide metabolism and secondary-metabolite biosynthesis most affected.
>
> H1-02:B-0087 [2.5 Incompleteness and pathway completeness] The search agents disagreed on its class (measured versus inferred); it is treated here as a measured association with an inferred causal reading.
>

## pathway-completeness.3 (claim)

Because the association is a cross-genome correlation, lineage biology is not fully separated from recovery artefact.

- conf: not stated
- class: reading (note: "Reviewer's reading")
- holds: the regression of module fullness on completeness across GTDB genomes
- src: eisenhoferImpactMicrobialGenome2023
- trail: H1-02 §2.5

From the note:

> H1-02:B-0083 [2.5 Incompleteness and pathway completeness] Eisenhofer et al. [3] regressed DRAM KEGG module fullness on CheckM completeness across 11,842 GTDB genomes.
>
> H1-02:B-0086 [2.5 Incompleteness and pathway completeness] Reviewer's reading: this is a cross-genome correlation, so lineage biology is not fully separated from recovery artefact.
>

## pathway-completeness.4 (claim)

Random contig subsampling of MAGs from an eight-species mock community shifted functional profiles in proportion to the subsampling.

- conf: not stated
- class: model (note: "modelled")
- holds: engineered: an eight-species mock community; random, not real, gaps
- src: eisenhoferImpactMicrobialGenome2023
- trail: H1-02 §2.5

From the note:

> H1-02:B-0088 [2.5 Incompleteness and pathway completeness] In the same paper, random contig subsampling of MAGs from an eight-species mock community shifted functional profiles in proportion to the subsampling (modelled; engineered).
>

## core-genome-inference.1 (claim)

Simulated random incompleteness of 1% left only about 36% of strict core families, and contamination inflated the cloud genome; the authors state that random removal "may overestimate" core loss. Simulations give larger numbers than real pairs because they strip sequence at random.

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

## core-genome-inference.2 (claim)

Unadjusted core counts were near zero at a 95% core threshold in a test on 500 E. coli assemblies with completeness drawn from MGnify.

- conf: not stated
- class: model (note: "modelled")
- holds: 500 E. coli assemblies with completeness drawn from MGnify (CELEBRIMBOR's test)
- src: hellewellCELEBRIMBORCoreAccessory2024
- trail: H1-02 §2.5

From the note:

> H1-02:B-0092 [2.5 Incompleteness and pathway completeness] CELEBRIMBOR's test on 500 E. coli assemblies with completeness drawn from MGnify [19] found unadjusted core counts near zero at a 95% threshold (modelled).
>

## core-genome-inference.3 (claim)

Fragmentation of isolate draft assemblies inflates accessory genomes about tenfold in some tools.

- conf: not stated
- class: not stated
- holds: isolate draft assemblies, not MAGs; the result does not transfer directly
- src: tonkinhillProducingPolishedProkaryotic2020
- trail: H1-02 §2.5

From the note:

> H1-02:B-0093 [2.5 Incompleteness and pathway completeness] Tonkin-Hill et al. [23] showed that fragmentation of isolate draft assemblies inflates accessory genomes about tenfold in some tools.
>
> H1-02:B-0094 [2.5 Incompleteness and pathway completeness] Those were isolates, not MAGs, and the result does not transfer directly.
>

## core-genome-inference.4 (claim)

Dereplication at 96.5% gANI removed 2,228 of 9,175 auxiliary gene clusters in 46 Microcystis MAGs.

- conf: not stated
- class: not stated
- holds: 46 Microcystis MAGs; a downstream processing step, not a recovery artefact; read in full by one agent and noted only for completeness; no verdict rests on it; the note's not-obtained list calls it an opinion piece, excluded
- src: evansDereplicateNotDereplicate2020
- trail: H1-02 §References, §Sources not obtained

From the note:

> H1-02:R-0108 [References] [13] Evans, Jacob T.; Denef, Vincent J. (2020).
>
> H1-02:R-0109 [References] To Dereplicate or Not To Dereplicate? mSphere 5(3): e00971-19. https://doi.org/10.1128/mSphere.00971-19 (read in full by one agent.
>
> H1-02:R-0110 [References] Its finding, that dereplication at 96.5% gANI removed 2,228 of 9,175 auxiliary gene clusters in 46 Microcystis MAGs, concerns a downstream processing step and is noted only for completeness; no verdict rests on it)
>
> H1-02:R-0038 [failure: Sources not obtained] - Evans, Jacob T.; Denef, Vincent J. (2020).
>
> H1-02:R-0039 [failure: Sources not obtained] To Dereplicate or Not To Dereplicate? mSphere 5(3): e00971-19. https://doi.org/10.1128/mSphere.00971-19 (read in full via Europe PMC but not used; volume, issue and article number from memory, not confirmed against Crossref) (routes tried: Full text obtained (PMC7380574).
>
> H1-02:R-0040 [failure: Sources not obtained] Excluded because it is an opinion piece whose content findings concern dereplication losing auxiliary genes, not recovery artefacts in gene content.)
>
> H1-02:B-0190 [Search record] The agents disagreed on the evidence class of [3] (measured against inferred) and on whether [13] and [24] were usable.
>
> H1-02:B-0191 [Search record] The review treats [3] as a measured association with an inferred artefact reading, and uses [13] and [24] for context only.
>

## bounding-comparisons.1 (claim)

GEM states that MAG sizes matched isolate genomes of the same species, "indicating no major loss of gene content", with one exception, a composite Sinorhizobium MAG.

- conf: not stated
- class: assert (critic: C-039)
- limit: access and evidence (note: "The statement rests on genome size in a supplementary figure that none of the agents read, not on gene-by-gene comparison")
- holds: the GEM catalogue; an author assertion resting on genome size, not gene-by-gene comparison
- src: nayfachGenomicCatalogEarths2020 (Supp. Fig. 2 not read)
- trail: H1-02 §2.6, §Adversarial

From the note:

> H1-02:B-0095 [2.6 Bounding and negative facts] - GEM [11] states that MAG sizes matched isolate genomes of the same species, "indicating no major loss of gene content".
>
> H1-02:B-0096 [2.6 Bounding and negative facts] One exception was a composite Sinorhizobium MAG.
>
> H1-02:B-0097 [2.6 Bounding and negative facts] The statement rests on genome size in a supplementary figure that none of the agents read, not on gene-by-gene comparison.
>
> H1-02:C-039 [warning: Adversarial critique, full findings] - GEM [11]: 'no major loss of gene content' is an author assertion. The review admits the underlying Supp. Fig. 2 was not read, so the claim is asserted, not measured, and should be tagged that way in Section 2.6.
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

Not found in the cited text (where to look, not what is wrong): holds: human; holds: search-agent; holds: cross-agent

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

Not found in the cited text (where to look, not what is wrong): holds: human; holds: search-agent

## bounding-comparisons.4 (claim)

In 55 of 78 human-microbiome species, MAG and GenBank persistent genomes differed by less than 1.2-fold and shared 90% of content; in the other 23 species, MAG persistent genomes held 60% of the GenBank set. Shell differences mix biology with recovery.

- conf: not stated
- class: meas (note: "measured")
- holds: natural, human microbiome; MAGs against GenBank genomes, not same-sample isolates; the critic: an unverified second-hand figure, resting on search-agent reads with no cross-agent confirmation
- src: gautreauPPanGGOLiNDepictingMicrobial2020
- trail: H1-02 §2.6, §Adversarial

From the note:

> H1-02:B-0102 [2.6 Bounding and negative facts] - Gautreau et al. [20]: in 55 of 78 human-microbiome species, MAG and GenBank persistent genomes differed by less than 1.2-fold and shared 90% of content.
>
> H1-02:B-0103 [2.6 Bounding and negative facts] In the other 23 species, MAG persistent genomes held 60% of the GenBank set.
>
> H1-02:B-0104 [2.6 Bounding and negative facts] Shell differences mix biology with recovery (measured; natural).
>
> H1-02:C-040 [warning: Adversarial critique, full findings] - Nayfach et al. 2019 [21], Pasolli et al. [25], Gautreau et al. [20], Johansen et al. [28], Sereika et al. [17], Pan et al. [31], Han et al. [32], Rocha et al. [34] and Maranga et al. [35]: none was re-opened at synthesis.
>
> H1-02:C-041 [warning: Adversarial critique, full findings] Their figures rest on search-agent reads with no cross-agent confirmation, including the Han 22% to 30% ARG-host figure, Johansen's 57% against 27% and 73% against 47%, and Gautreau's 55 of 78 species.
>
> H1-02:C-042 [warning: Adversarial critique, full findings] These are not breaches as such, but they are unverified second-hand figures, and several carry weight in the soil Part B indirect evidence.
>

Not found in the cited text (where to look, not what is wrong): holds: same-sample

## bounding-comparisons.5 (claim)

These bounds are coarse (genome size, ANI, per-OTU annotation overlap) and do not contradict the gene-level losses in Meziti et al.'s comparison with isolate genomes from the same samples, which fall on variable and mobile genes that length and ANI do not register.

- conf: not stated
- class: reading (note: "Reviewer's reading")
- contrary: one-sided (critic: C-089)
- holds: the coarse bounding facts set against the gene-level losses in one isolate comparison; the critic: correctly labelled, but used to discount the bounding evidence in favour of Meziti et al. without a source saying so
- src: none (the reviewer's synthesis)
- trail: H1-02 §2.6, §2.1, §Adversarial

From the note:

> H1-02:B-0106 [2.6 Bounding and negative facts] Reviewer's reading: these bounds are coarse (genome size, ANI, per-OTU annotation overlap) and do not contradict the gene-level losses in [1], which fall on variable and mobile genes that length and ANI do not register.
>
> H1-02:B-0032 [2.1 Direct same-sample comparisons (natural, human gut)] Meziti et al. [1] compared MaxBin 2.0 MAGs with isolate genomes from the same diarrhoeal stool samples.
>
> H1-02:C-089 [warning: Adversarial critique, full findings] - 'Reviewer's reading: these bounds are coarse ... and do not contradict the gene-level losses' is correctly labelled. But it is used to discount the bounding evidence in favour of [1] without a source saying so.
>

## filters-corrections.1 (claim)

A minimum contig length of 1 kb reduced contamination and non-shared genes in real stool MAGs, with small completeness costs; it was not shown to recover missed genes.

- conf: not stated
- class: not stated
- holds: real stool samples, n = 8 (gut E. coli pairs)
- src: mezitiReliabilityMetagenomeassembledGenomes2021
- trail: H1-02 §2.7

From the note:

> H1-02:B-0107 [2.7 Filters and corrections: real-sample validation] - Minimum contig length (1 kb) reduced contamination and non-shared genes in real stool MAGs, with small completeness costs [1].
>
> H1-02:B-0108 [2.7 Filters and corrections: real-sample validation] It was not shown to recover missed genes.
>
> H1-02:B-0109 [2.7 Filters and corrections: real-sample validation] Real samples, n = 8.
>
> H1-02:A-003 [quote: Verdict as delivered] The contig-length filter [1] and relaxed core threshold [2] were tested on real data but only in n = 8 and n = 5 gut E. coli pairs, and they reduced the artefact without removing it.
>

## filters-corrections.2 (claim)

A relaxed core threshold (90%) reduced core loss in five real E. coli pairs.

- conf: not stated
- class: not stated
- holds: real samples, n = 5, gut
- src: liCriticalAssessmentPangenomic2022
- trail: H1-02 §2.7

From the note:

> H1-02:B-0110 [2.7 Filters and corrections: real-sample validation] - A relaxed core threshold (90%) reduced core loss in five real E. coli pairs [2].
>
> H1-02:B-0111 [2.7 Filters and corrections: real-sample validation] Real samples, n = 5, gut.
>

