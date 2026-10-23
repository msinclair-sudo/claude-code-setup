## community-copy-number.4 (claim)

Animal-associated samples have a predicted community copy number of about 3.4, with gut and saliva highest.

- conf: single (critic: MB-01:C-024)
- class: not stated
- holds: EMP animal-associated samples; predictions from one source
- src: thompsonCommunalCatalogueReveals2017
- trail: MB-01 §3.2, §answers, §critic

From the note:

> MB-01:B-0206 [3.2 16S rRNA gene copy number] | Environment | Value | Source |
>
> MB-01:B-0209 [3.2 16S rRNA gene copy number] | Hosts | About 3.4 for animal-associated samples; gut and saliva highest | Thompson 2017 |
>
> MB-01:A-151 [quote: Answers as delivered] Hosts: predicted about 3.4 for animal-associated samples, with gut and saliva highest (Thompson 2017).
>
> MB-01:C-024 [danger: Critic: answers partly supported] (1) Environment-level copy numbers (ACN about 2.2 for free-living and plant-associated samples, about 3.4 for animal-associated, soil lowest) are predictions from one source (Thompson 2017); the review flags this.
>

Not found in the cited text (where to look, not what is wrong): holds: emp

## community-copy-number.5 (claim)

No separate copy-number value for water was found; the EMP gives about 2.2 for free-living (soil, water, sediment) and plant-associated samples pooled together.

- conf: single (critic: MB-01:C-024)
- class: not stated
- holds: EMP, free-living and plant-associated samples pooled
- src: thompsonCommunalCatalogueReveals2017
- trail: MB-01 §3.2, §answers, §critic, §Adversarial

From the note:

> MB-01:B-0207 [3.2 16S rRNA gene copy number] | Water | No separate value found.
>
> MB-01:B-0208 [3.2 16S rRNA gene copy number] EMP groups free-living and plant-associated samples at about 2.2 | Thompson 2017 |
>
> MB-01:A-149 [quote: Answers as delivered] Water: no separate value was found.
>
> MB-01:A-150 [quote: Answers as delivered] The EMP reports about 2.2 for free-living and plant-associated samples together.
>
> MB-01:C-024 [danger: Critic: answers partly supported] (1) Environment-level copy numbers (ACN about 2.2 for free-living and plant-associated samples, about 3.4 for animal-associated, soil lowest) are predictions from one source (Thompson 2017); the review flags this.
>
> MB-01:C-136 [warning: Adversarial critique, full findings] - D3 copy number by environment: the EMP ACN of about 2.2 pools free-living (soil, water, sediment) and plant-associated samples; the review notes this but still offers it in the 'water' row.
>

## community-copy-number.6 (claim)

Environment-level copy number rests entirely on one source, its values are predictions, and they conflict with the finding that such predictions are unreliable for taxa more than about 15% divergent from sequenced genomes.

- conf: single (note: "single source")
- class: not stated
- holds: EMP predictions
- src: thompsonCommunalCatalogueReveals2017, loucaCorrecting16SRRNA2018
- trail: MB-01 §answers, §3.2
- rating: "Weak for environment-level copy number"

From the note:

> MB-01:A-169 [quote: Answers as delivered] Weak for environment-level copy number: predicted, single source, and with prediction accuracy itself contested.
>
> MB-01:A-177 [quote: Answers as delivered] Copy-number estimates for environments conflict with Louca 2018's finding that the predictions are inaccurate.
>
> MB-01:A-183 [quote: Answers as delivered] *Single-source sensitivity:* Environment-level copy number rests entirely on Thompson 2017.
>
> MB-01:B-0210 [3.2 16S rRNA gene copy number] Louca 2018 shows that the predictions underlying these values are unreliable for taxa more than about 15% divergent from sequenced genomes, and about 49% of SILVA-tree OTUs exceed that.
>

Not found in the cited text (where to look, not what is wrong): holds: emp

## community-copy-number.7 (claim)

Measured (not predicted) community-average copy number in soil, water or host samples was not found; community-average copy number from shotgun metagenomes (16S reads normalised to single-copy marker genes) was not searched, so the not-found rests on prediction-only sources.

- conf: not stated
- class: search (critic: MB-01:C-112)
- holds: soil, water and host samples
- src: none (a search result)
- trail: MB-01 §answers, §critic, §Adversarial, §Search record, §Provenance
- search: not searched (critic: MB-01:C-112)

From the note:

> MB-01:A-178 [quote: Answers as delivered] *Not measured:* Not found: measured (not predicted) community-average copy number in soil, water or host samples; a separate value for water; absolute per-cycle efficiencies for 16S primers; within-run read-count CV after equimolar pooling (all three angles searched; web search returned only forum posts); the archaeal copy-number distribution beyond its 1-4 range; abundance-distribution shapes reported separately for water and host-associated 16S data.
>
> MB-01:B-0017 [info: Provenance] Not found by any route: within-run CV of reads per sample; absolute per-cycle 16S efficiencies; measured (not predicted) community copy number by environment; 16S-specific index hopping on patterned flow cells; overdispersion fitted to 16S technical replicates; an independent microbial benchmark of coverage-based standardisation; abundance-distribution shapes reported separately for water and host.
>
> MB-01:B-0380 [Search record] - Measured, rather than predicted, community copy number by environment (lab and bioinformatics angles).
>
> MB-01:C-029 [danger: Critic: answers partly supported] Absent: measured community copy number, a within-run read-count coefficient of variation, absolute per-cycle efficiencies, and per-environment abundance-distribution shapes for water and for host samples.
>
> MB-01:C-112 [warning: Adversarial critique, full findings] - gap: Community-average copy number from shotgun metagenomes (16S reads normalised to single-copy marker genes) was not searched, so 'measured copy number by environment not found' rests on prediction-only sources.; setting_or_class: Metagenome-derived 16S copies per genome in soil, water and host samples; direction: D3
>

## library-sequencing.1 (claim)

Across 73 MiSeq datasets, library preparation method and primer choice were the most significant sources of bias, with distinct, motif-linked error patterns; this rests on one study.

- conf: single (marker)
- class: meas (marker)
- holds: 73 MiSeq datasets
- src: schirmerInsightBiasesSequencing2015 (FT; meas; single)
- trail: MB-01 §2.6, §answers, §Adversarial

From the note:

> MB-01:I-0041 [2.6 Library preparation and sample indexing] Across 73 MiSeq datasets, library preparation method and primer choice were the most significant sources of bias, with distinct, motif-linked error patterns (Schirmer 2015) [FT; meas; single].
>
> MB-01:A-076 [quote: Answers as delivered] Library preparation and sequencing.
>
> MB-01:A-077 [quote: Answers as delivered] Library preparation and primers were the largest sources of error-profile bias (Schirmer 2015).
>
> MB-01:B-0071 [2. Steps from sample to table (D1) and departures from the sampled community (D2)] | Library prep, sequencing | Library prep and primers are the largest drivers of error profile | Spurious OTUs severely inflate Chao1 | Error rate rises with cluster density | Schirmer 2015; Kozich 2013; Pinto and Raskin 2012 |
>
> MB-01:C-088 [warning: Adversarial critique, full findings] - Table 1 and section 2.6: 'Library prep and primers are the largest drivers of error profile' rests on Schirmer 2015 alone, with no SINGLE SOURCE flag in the table.
>

## library-sequencing.2 (claim)

Library design also affected error and chimera rates across four platforms.

- conf: not stated
- class: not stated
- holds: four platforms
- src: damoreComprehensiveBenchmarkingStudy2016
- trail: MB-01 §2.6

From the note:

> MB-01:B-0127 [2.6 Library preparation and sample indexing] Library design also affected error and chimera rates across four platforms (D'Amore 2016).
>

## library-sequencing.3 (claim)

Dual-index MiSeq error depended on read overlap.

- conf: repl (marker)
- class: meas (marker)
- holds: dual-index MiSeq
- src: kozichDevelopmentDualindexSequencing2013 (FT; meas; repl)
- trail: MB-01 §2.7

From the note:

> MB-01:I-0042 [2.7 Sequencing platform and read length] **Error by region on MiSeq.** Dual-index MiSeq error depended on read overlap (Kozich 2013) [FT; meas; repl].
>

## library-sequencing.4 (claim)

Raw V4 MiSeq error rose with cluster density from 0.25% to 1.08%; a delta-Q of 6 cut it to 0.05 to 0.06%, and preclustering to 0.01%.

- conf: not stated
- class: not stated
- holds: V4 on MiSeq
- src: kozichDevelopmentDualindexSequencing2013
- trail: MB-01 §2.7, §answers

From the note:

> MB-01:B-0131 [2.7 Sequencing platform and read length] Raw V4 error rose with cluster density from 0.25% to 1.08%.
>
> MB-01:B-0132 [2.7 Sequencing platform and read length] A delta-Q of 6 cut it to 0.05 to 0.06%, and preclustering to 0.01%.
>
> MB-01:A-078 [quote: Answers as delivered] Raw MiSeq error was 0.25-1.08% and fell to 0.01% for V4 after curation (Kozich 2013).
>
> MB-01:B-0071 [2. Steps from sample to table (D1) and departures from the sampled community (D2)] | Library prep, sequencing | Library prep and primers are the largest drivers of error profile | Spurious OTUs severely inflate Chao1 | Error rate rises with cluster density | Schirmer 2015; Kozich 2013; Pinto and Raskin 2012 |
>

## library-sequencing.5 (claim)

Partially overlapping regions stayed worse: after preclustering, V3-V4 error was 0.10 to 0.21% and V4-V5 0.36 to 0.64%, per the bioinformatics angle.

- conf: not stated
- class: not stated
- holds: V3-V4 and V4-V5 after preclustering, per the bioinformatics angle
- src: kozichDevelopmentDualindexSequencing2013
- trail: MB-01 §2.7

From the note:

> MB-01:B-0133 [2.7 Sequencing platform and read length] Partially overlapping regions stayed worse.
>
> MB-01:B-0134 [2.7 Sequencing platform and read length] After preclustering, V3-V4 was 0.10 to 0.21% and V4-V5 0.36 to 0.64%, per the bioinformatics angle.
>

## library-sequencing.6 (claim)

The lab angle reports V3-V4 and V4-V5 error of 0.24 to 0.37% and 0.58 to 0.87%, read through a fetch-tool summary and probably at an earlier stage of curation.

- conf: not stated
- class: not stated
- holds: V3-V4 and V4-V5, per the lab angle
- src: kozichDevelopmentDualindexSequencing2013
- trail: MB-01 §2.7

From the note:

> MB-01:B-0135 [2.7 Sequencing platform and read length] The lab angle reports 0.24 to 0.37% and 0.58 to 0.87%, which it read through a fetch-tool summary, probably at an earlier stage of curation.
>

Not found in the cited text (where to look, not what is wrong): V3-V4; V4-V5; holds: v3-v4; holds: v4-v5

## library-sequencing.7 (claim)

PacBio CCS with DADA2 recovered all expected full-length variants in two mocks with no residual errors, by the developers' own account.

- conf: not stated
- class: not stated
- holds: two mocks; a developer claim
- src: callahanHighthroughputAmpliconSequencing2019 (developer claim)
- trail: MB-01 §2.7

From the note:

> MB-01:B-0136 [2.7 Sequencing platform and read length] **Full length.** PacBio CCS with DADA2 recovered all expected full-length variants in two mocks with no residual errors (Callahan 2019) [developer claim].
>

## library-sequencing.8 (claim)

The DADA2 maintainer states that NovaSeq's binned quality scores break loess smoothing in error learning; at the time of the issue the method had not been tested on NovaSeq data.

- conf: not stated
- class: assert (note: "DOCUMENTATION; assert")
- holds: DADA2 GitHub issue #791
- src: benjjnebConsequencesUsingDada2 (DOCUMENTATION; assert)
- trail: MB-01 §2.7

From the note:

> MB-01:B-0137 [2.7 Sequencing platform and read length] **NovaSeq.** The DADA2 maintainer states that NovaSeq's binned quality scores break loess smoothing in error learning.
>
> MB-01:B-0138 [2.7 Sequencing platform and read length] At the time of the issue the method had not been tested on NovaSeq data (DADA2 GitHub issue #791) [DOCUMENTATION; assert].
>

## index-misassignment.1 (claim)

On Illumina GAIIx with non-16S libraries, 0.51 to 0.76% of index pairs were wrong, and 0.06 to 0.43% after index-quality filtering.

- conf: repl (marker)
- class: meas (marker)
- holds: GAIIx, non-16S libraries, indirect
- src: kircherDoubleIndexingOvercomes2012 (FT; meas; repl; INDIRECT)
- trail: MB-01 §2.8

From the note:

> MB-01:I-0043 [2.8 Demultiplexing and index misassignment] | Illumina GAIIx, non-16S libraries | 0.51 to 0.76% of index pairs wrong; 0.06 to 0.43% after index-quality filtering | Kircher 2012 [FT; meas; repl; INDIRECT] |
>

## index-misassignment.2 (claim)

On patterned flow cells (HiSeq X, 3000/4000, NovaSeq) with non-16S libraries, 0.2 to 6% of reads were misassigned in every run, about 10-fold less on MiSeq, and unique dual indexes cut 0.89% to 0.13%.

- conf: repl (marker)
- class: meas (marker)
- holds: non-16S libraries, indirect
- src: costelloCharacterizationRemediationSample2018 (FT; meas; repl; INDIRECT)
- trail: MB-01 §2.8, §answers

From the note:

> MB-01:I-0044 [2.8 Demultiplexing and index misassignment] | Patterned flow cells (HiSeq X, 3000/4000, NovaSeq), non-16S | 0.2 to 6% in every run; about 10-fold lower on MiSeq; unique dual indexes cut 0.89% to 0.13% | Costello 2018 [FT; meas; repl; INDIRECT] |
>
> MB-01:A-082 [quote: Answers as delivered] Taxa (false presence) and RA: 0.2-6% of reads on patterned flow cells and about 10-fold less on MiSeq (Costello 2018, indirect, non-16S).
>

## index-misassignment.3 (claim)

Illumina documentation gives 0.1 to 2% index misassignment on patterned flow cells.

- conf: not stated
- class: not stated
- holds: a maker's claim
- src: illuminaIndexHoppingWeb (DOCUMENTATION; maker's claim)
- trail: MB-01 §2.8

From the note:

> MB-01:B-0139 [2.8 Demultiplexing and index misassignment] | Setting | Rate | Source |
>
> MB-01:B-0140 [2.8 Demultiplexing and index misassignment] | Illumina documentation | 0.1 to 2% on patterned flow cells | Illumina index-hopping page [DOCUMENTATION; maker's claim] |
>

## index-misassignment.4 (claim)

On HiSeq 2500 with non-16S amplicons, cross-talk was 0.24%, and 0.03% after index-quality filtering (88% of reads kept).

- conf: single (marker)
- class: meas (marker)
- holds: HiSeq 2500, non-16S amplicons, indirect
- src: wrightQualityFilteringIllumina2016 (FT; meas; single; INDIRECT)
- trail: MB-01 §2.8, §answers

From the note:

> MB-01:I-0045 [2.8 Demultiplexing and index misassignment] | HiSeq 2500, non-16S amplicons | 0.24% cross-talk; 0.03% after index-quality filtering (88% of reads kept) | Wright and Vetsigian 2016 [FT; meas; single; INDIRECT] |
>
> MB-01:A-083 [quote: Answers as delivered] About 0.24% on HiSeq 2500 amplicons (Wright 2016, indirect).
>

## index-misassignment.5 (claim)

In 16S data from GAIIx and 11 MiSeq runs, about 2% of reads were misassigned.

- conf: single (marker)
- class: meas (marker)
- holds: 16S; one preprint abstract
- src: edgarUNCROSSFilteringHighfrequency2016 (AB; PREPRINT; meas; single)
- trail: MB-01 §2.8, §answers

From the note:

> MB-01:I-0046 [2.8 Demultiplexing and index misassignment] | 16S, GAIIx and 11 MiSeq runs | about 2% of reads | Edgar 2016a [AB; PREPRINT; meas; single] |
>
> MB-01:A-084 [quote: Answers as delivered] About 2% in 16S MiSeq runs (Edgar 2016a, preprint abstract).
>

## index-misassignment.6 (claim)

On 16S plates, barcode leakage was negligible.

- conf: single (marker)
- class: meas (marker)
- holds: 16S plates
- src: minichQuantifyingUnderstandingWelltowell2019 (FT; meas; single)
- trail: MB-01 §2.8, §answers

From the note:

> MB-01:I-0047 [2.8 Demultiplexing and index misassignment] | 16S plates | barcode leakage negligible | Minich 2019 [FT; meas; single] |
>
> MB-01:A-085 [quote: Answers as delivered] Barcode leakage was negligible in Minich 2019.
>

## index-misassignment.7 (claim)

In eukaryotic 18S data, up to 28.2% of unique sequences were undetectable mistags.

- conf: not stated
- class: meas (marker)
- holds: eukaryotic 18S, indirect
- src: eslingAccurateMultiplexingFiltering2015 (FT; meas; INDIRECT)
- trail: MB-01 §2.8

From the note:

> MB-01:I-0048 [2.8 Demultiplexing and index misassignment] | Eukaryotic 18S | up to 28.2% of unique sequences undetectable mistags | Esling 2015 [FT; meas; INDIRECT] |
>

## index-misassignment.8 (claim)

With mammal and arthropod markers, 2.1 to 2.6% of sequences came from tag jumps.

- conf: not stated
- class: meas (marker)
- holds: mammal and arthropod markers, indirect
- src: schnellTagJumpsIlluminated2015 (AB; meas; INDIRECT)
- trail: MB-01 §2.8, §answers

From the note:

> MB-01:I-0049 [2.8 Demultiplexing and index misassignment] | Mammal and arthropod markers | 2.1 to 2.6% of sequences from tag jumps | Schnell 2015 [AB; meas; INDIRECT] |
>
> MB-01:A-086 [quote: Answers as delivered] Tag jumps were 2.1-2.6% (Schnell 2015, other markers).
>

## index-misassignment.9 (claim)

Index misassignment rates are fractions of reads assigned to the wrong sample; they mainly create false presences of taxa, concentrated where abundant taxa from other samples leak in, and also affect relative abundance.

- conf: not stated
- class: not stated
- holds: as stated
- src: none (the reviewer's synthesis)
- trail: MB-01 §2.8, §answers

From the note:

> MB-01:B-0141 [2.8 Demultiplexing and index misassignment] These are fractions of reads assigned to the wrong sample.
>
> MB-01:B-0142 [2.8 Demultiplexing and index misassignment] They mainly create false presences of taxa, and the false taxa are concentrated where abundant taxa from other samples leak in.
>
> MB-01:A-081 [quote: Answers as delivered] Index misassignment.
>
> MB-01:A-082 [quote: Answers as delivered] Taxa (false presence) and RA: 0.2-6% of reads on patterned flow cells and about 10-fold less on MiSeq (Costello 2018, indirect, non-16S).
>
> MB-01:B-0072 [2. Steps from sample to table (D1) and departures from the sampled community (D2)] | Index misassignment | 0.1 to 6% of reads moved between samples | False presences | Varies by platform, library type and run | Costello 2018; Wright 2016; Edgar 2016a; Minich 2019 |
>

## index-misassignment.10 (claim)

Index misassignment rates vary with platform, library type and run.

- conf: not stated
- class: not stated
- holds: as stated
- src: none (the reviewer's synthesis)
- trail: MB-01 §2.8, §answers

From the note:

> MB-01:B-0143 [2.8 Demultiplexing and index misassignment] Rates vary with platform, library type and run.
>
> MB-01:A-087 [quote: Answers as delivered] Consistency: varies by platform, library type and run.
>
> MB-01:B-0072 [2. Steps from sample to table (D1) and departures from the sampled community (D2)] | Index misassignment | 0.1 to 6% of reads moved between samples | False presences | Varies by platform, library type and run | Costello 2018; Wright 2016; Edgar 2016a; Minich 2019 |
>

## index-misassignment.11 (claim)

The 16S-specific evidence on index misassignment is thin: one preprint abstract and one plate study; no 16S-specific measurement of index hopping on patterned flow cells (NovaSeq, NextSeq 2000) was found.

- conf: not stated
- class: search (note: "No 16S-specific measurement of index hopping on patterned flow cells (NovaSeq) was found")
- holds: the bioinformatics angle's search
- src: edgarUNCROSSFilteringHighfrequency2016, minichQuantifyingUnderstandingWelltowell2019
- trail: MB-01 §2.8, §answers, §Search record, §Adversarial
- search: searched, not found (note: "No 16S-specific measurement of index hopping on patterned flow cells (NovaSeq) was found")

From the note:

> MB-01:B-0144 [2.8 Demultiplexing and index misassignment] The 16S-specific evidence is thin: one preprint abstract and one plate study.
>
> MB-01:A-122 [quote: Answers as delivered] *Not measured:* No 16S-specific measurement of index hopping on patterned flow cells (NovaSeq) was found.
>
> MB-01:B-0381 [Search record] - 16S-specific index hopping on patterned flow cells (bioinformatics angle).
>
> MB-01:C-110 [warning: Adversarial critique, full findings] - gap: No 16S-specific index-hopping measurement on patterned flow cells (NovaSeq, NextSeq 2000). The 16S rate is one preprint abstract (Edgar 2016a).; setting_or_class: Illumina patterned flow-cell 16S runs; direction: D2
>

## quality-filtering.1 (claim)

On mocks from GAIIx, HiSeq and MiSeq runs, minimum read length, quality threshold and a minimum OTU abundance filter strongly affected alpha diversity and composition; ambiguous bases and bad run length did not.

- conf: repl (marker)
- class: meas (marker)
- holds: mocks from GAIIx, HiSeq and MiSeq runs
- src: bokulichQualityfilteringVastlyImproves2013 (FT; meas; repl)
- trail: MB-01 §2.9

From the note:

> MB-01:B-0145 [2.9 Quality filtering and read merging] **Filtering parameters.** On mocks from GAIIx, HiSeq and MiSeq runs, minimum read length, quality threshold and a minimum OTU abundance filter strongly affected alpha diversity and composition.
>
> MB-01:I-0050 [2.9 Quality filtering and read merging] Ambiguous bases and bad run length did not (Bokulich 2013) [FT; meas; repl].
>

## quality-filtering.2 (claim)

Almost every filtering setting needed an abundance filter of 0.0001 to 0.01% to reach expected taxon counts, and 0.005% is recommended.

- conf: not stated
- class: not stated
- holds: mocks
- src: bokulichQualityfilteringVastlyImproves2013
- trail: MB-01 §2.9

From the note:

> MB-01:B-0146 [2.9 Quality filtering and read merging] Almost every setting needed an abundance filter of 0.0001 to 0.01% to reach expected taxon counts, and 0.005% is recommended.
>
> MB-01:B-0145 [2.9 Quality filtering and read merging] **Filtering parameters.** On mocks from GAIIx, HiSeq and MiSeq runs, minimum read length, quality threshold and a minimum OTU abundance filter strongly affected alpha diversity and composition.
>

## quality-filtering.3 (claim)

After quality filtering, weighted UniFrac conclusions were robust and unweighted metrics were sensitive.

- conf: not stated
- class: not stated
- holds: mocks
- src: bokulichQualityfilteringVastlyImproves2013
- trail: MB-01 §2.9

From the note:

> MB-01:B-0147 [2.9 Quality filtering and read merging] Weighted UniFrac conclusions were robust; unweighted metrics were sensitive.
>
> MB-01:B-0145 [2.9 Quality filtering and read merging] **Filtering parameters.** On mocks from GAIIx, HiSeq and MiSeq runs, minimum read length, quality threshold and a minimum OTU abundance filter strongly affected alpha diversity and composition.
>

## quality-filtering.4 (claim)

Stringent UPARSE-style filtering could significantly underestimate abundance and diversity, and newer clusterers produced up to 60% fewer spurious OTUs than UCLUST.

- conf: cont (marker)
- class: meas (marker)
- holds: Kopylova et al.'s benchmarks
- src: kopylovaOpensourceSequenceClustering2016 (FT; meas; cont)
- trail: MB-01 §2.9, §7. Bounds

From the note:

> MB-01:I-0051 [2.9 Quality filtering and read merging] **Contrary.** Stringent UPARSE-style filtering could significantly underestimate abundance and diversity, and newer clusterers produced up to 60% fewer spurious OTUs than UCLUST (Kopylova 2016) [FT; meas; cont].
>
> MB-01:B-0362 [7. Bounds and negative results] - stringent filtering (Kopylova 2016);
>

## quality-filtering.5 (claim)

Error correction plus overlapping cut substitution errors by 93% on average.

- conf: not stated
- class: not stated
- holds: one study
- src: schirmerInsightBiasesSequencing2015
- trail: MB-01 §2.9

From the note:

> MB-01:B-0148 [2.9 Quality filtering and read merging] **Error correction and merging.** Error correction plus overlapping cut substitution errors by 93% on average (Schirmer 2015).
>

## quality-filtering.6 (claim)

The USEARCH author reports that most paired-read assemblers compute incorrect posterior quality scores.

- conf: not stated
- class: not stated
- holds: a developer claim
- src: edgarErrorFilteringPair2015 (AB; developer claim)
- trail: MB-01 §2.9

From the note:

> MB-01:B-0149 [2.9 Quality filtering and read merging] The USEARCH author reports that most paired-read assemblers compute incorrect posterior quality scores (Edgar and Flyvbjerg 2015) [AB; developer claim].
>

## denoising-clustering.1 (claim)

In an independent benchmark, relative abundances of expected taxa within each mock were similar across DADA2, UNOISE3, Deblur and open-reference OTUs, yet on the Zymo mock all pipelines "markedly differed" from expected composition.

- conf: repl (marker)
- class: meas (marker)
- holds: mocks, one independent benchmark
- src: nearingDenoisingDenoisersIndependent2018 (FT; meas; repl)
- trail: MB-01 §2.10, §answers, §Adversarial

From the note:

> MB-01:I-0052 [2.10 Denoising and clustering] **Relative abundance is robust to the pipeline; counts of taxa are not.** In an independent benchmark, relative abundances of expected taxa within each mock were similar across DADA2, UNOISE3, Deblur and open-reference OTUs (Nearing 2018) [FT; meas; repl].
>
> MB-01:B-0154 [2.10 Denoising and clustering] On the Zymo mock, all pipelines "markedly differed" from expected composition.
>
> MB-01:A-091 [quote: Answers as delivered] Denoising and clustering.
>
> MB-01:A-092 [quote: Answers as delivered] RA of expected taxa was similar across pipelines (Nearing 2018).
>
> MB-01:B-0074 [2. Steps from sample to table (D1) and departures from the sampled community (D2)] | Denoising, clustering | Expected-taxon RA similar across pipelines.
>
> MB-01:C-087 [warning: Adversarial critique, full findings] - Section 2.10 heading: 'Relative abundance is robust to the pipeline; counts of taxa are not' generalises from Nearing 2018 (with Marizzoni 2020). Nearing 2018 itself reports that all pipelines 'markedly differed' from expected composition on the Zymo mock, and Straub 2020 reports pipeline-dependent interpretations.
>

## denoising-clustering.2 (claim)

Counts of units differed widely between pipelines: open-reference clustering gave 453 OTUs on the HMP mock and 8,891 on the Extreme mock; on one soil, DADA2 gave 16,609 ASVs, UNOISE3 11,613, Deblur 8,270 and open-reference 21,297 OTUs; no pipeline recovered every expected sequence.

- conf: not stated
- class: not stated
- holds: mocks and one soil
- src: nearingDenoisingDenoisersIndependent2018
- trail: MB-01 §2.10

From the note:

> MB-01:B-0150 [2.10 Denoising and clustering] Counts of units differed widely.
>
> MB-01:B-0151 [2.10 Denoising and clustering] Open-reference clustering gave 453 OTUs on the HMP mock and 8,891 on the Extreme mock.
>
> MB-01:B-0152 [2.10 Denoising and clustering] On one soil, DADA2 gave 16,609 ASVs, UNOISE3 11,613, Deblur 8,270 and open-reference 21,297 OTUs.
>
> MB-01:B-0153 [2.10 Denoising and clustering] No pipeline recovered every expected sequence.
>

## denoising-clustering.3 (claim)

Bacteroides varied from 20.6% to 24.6% across pipelines.

- conf: not stated
- class: not stated
- holds: one study
- src: marizzoniComparisonBioinformaticsPipelines2020
- trail: MB-01 §answers

From the note:

> MB-01:A-093 [quote: Answers as delivered] Bacteroides varied from 20.6% to 24.6% across pipelines (Marizzoni 2020).
>
> MB-01:B-0075 [2. Steps from sample to table (D1) and departures from the sampled community (D2)] Bacteroides 20.6 to 24.6% across pipelines | 10 to 200 times more units than expected (mothur, QIIME1). 50 to 80% spurious taxa unfiltered | Not stated | Nearing 2018; Straub 2020; Reitmeier 2021; Marizzoni 2020 |
>

## denoising-clustering.4 (claim)

mothur and QIIME1 returned 10 to 200 times the expected number of sequences, and Faith's PD was overestimated 1.3 to 2.7-fold by QIIME2, 2 to 18-fold by QIIME1 and 3.5 to 29-fold by mothur; pipeline choice biased interpretations.

- conf: repl (marker)
- class: meas (marker)
- holds: Straub et al.'s benchmark; the authors also built nf-core/ampliseq
- src: straubInterpretationsEnvironmentalMicrobial2020 (FT; meas; repl; authors also built nf-core/ampliseq)
- trail: MB-01 §2.10, §answers, §Adversarial

From the note:

> MB-01:I-0053 [2.10 Denoising and clustering] - mothur and QIIME1 returned 10 to 200 times the expected number of sequences. Faith's PD was overestimated 1.3 to 2.7-fold by QIIME2, 2 to 18-fold by QIIME1 and 3.5 to 29-fold by mothur (Straub 2020) [FT; meas; repl; authors also built nf-core/ampliseq].
>
> MB-01:A-094 [quote: Answers as delivered] Taxa: mothur and QIIME1 produced 10-200 times the expected number of sequences (Straub 2020).
>
> MB-01:B-0075 [2. Steps from sample to table (D1) and departures from the sampled community (D2)] Bacteroides 20.6 to 24.6% across pipelines | 10 to 200 times more units than expected (mothur, QIIME1). 50 to 80% spurious taxa unfiltered | Not stated | Nearing 2018; Straub 2020; Reitmeier 2021; Marizzoni 2020 |
>
> MB-01:C-087 [warning: Adversarial critique, full findings] - Section 2.10 heading: 'Relative abundance is robust to the pipeline; counts of taxa are not' generalises from Nearing 2018 (with Marizzoni 2020). Nearing 2018 itself reports that all pipelines 'markedly differed' from expected composition on the Zymo mock, and Straub 2020 reports pipeline-dependent interpretations.
>

## denoising-clustering.5 (claim)

DADA2 had the best sensitivity and UNOISE3 the best balance.

- conf: repl (marker)
- class: meas (marker)
- holds: mock runs
- src: prodanComparingBioinformaticPipelines2020 (FT; meas; repl)
- trail: MB-01 §2.10

From the note:

> MB-01:I-0054 [2.10 Denoising and clustering] - DADA2 had the best sensitivity and UNOISE3 the best balance (Prodan 2020) [FT; meas; repl].
>

Not found in the cited text (where to look, not what is wrong): holds: mock

## denoising-clustering.6 (claim)

QIIME-uclust produced on average 134 one-off and 412 other spurious OTUs.

- conf: not stated
- class: not stated
- holds: mock runs
- src: prodanComparingBioinformaticPipelines2020
- trail: MB-01 §2.10

From the note:

> MB-01:B-0155 [2.10 Denoising and clustering] **Spurious units.**
>
> MB-01:B-0156 [2.10 Denoising and clustering] QIIME-uclust produced on average 134 one-off and 412 other spurious OTUs.
>

Not found in the cited text (where to look, not what is wrong): holds: mock

## denoising-clustering.7 (claim)

The DADA2 developers report 93 output sequences on a 57-strain mock, against 249 for mothur and 378 for QIIME.

- conf: not stated
- class: meas (marker)
- holds: one 57-strain mock; a developer claim
- src: callahanDADA2HighresolutionSample2016 (FT; meas; developer claim)
- trail: MB-01 §2.10

From the note:

> MB-01:I-0055 [2.10 Denoising and clustering] - The DADA2 developers report 93 output sequences on a 57-strain mock, against 249 for mothur and 378 for QIIME (Callahan 2016) [FT; meas; developer claim].
>

## denoising-clustering.8 (claim)

After OTU clustering and singleton removal, tables were about 50% (mock communities) to 80% (gnotobiotic mice) spurious taxa; the authors propose a 0.25% relative-abundance cutoff.

- conf: single (marker)
- class: meas (marker)
- holds: mock communities and gnotobiotic mice
- src: reitmeierHandlingSpuriousSequences2021 (FT; meas; single)
- trail: MB-01 §2.10, §critic, §Adversarial, §answers

From the note:

> MB-01:I-0056 [2.10 Denoising and clustering] - Unfiltered OTU tables were about 50% (mocks) to 80% (gnotobiotic mice) spurious taxa. The authors propose a 0.25% relative-abundance cutoff (Reitmeier 2021) [FT; meas; single].
>
> MB-01:A-095 [quote: Answers as delivered] Unfiltered tables were 50-80% spurious taxa (Reitmeier 2021).
>
> MB-01:B-0075 [2. Steps from sample to table (D1) and departures from the sampled community (D2)] Bacteroides 20.6 to 24.6% across pipelines | 10 to 200 times more units than expected (mothur, QIIME1). 50 to 80% spurious taxa unfiltered | Not stated | Nearing 2018; Straub 2020; Reitmeier 2021; Marizzoni 2020 |
>
> MB-01:C-058 [danger: Critic: answers partly supported] (d) Reitmeier 2021's 50 to 80% spurious taxa is described as 'unfiltered'; the source says after OTU clustering and singleton removal.
>
> MB-01:C-072 [warning: Adversarial critique, full findings] - Reitmeier 2021 (FT): the D2 answer and section 2.10 call the 50 to 80% spurious-taxa figure 'unfiltered'. The source says 'OTU clustering and singleton removal ... delivered approximately 50% (mock communities) to 80% (gnotobiotic mice) spurious taxa'.
>

## denoising-clustering.9 (claim)

QIIME closed- and open-reference OTUs inflated richness to 1,607 to 5,824 OTUs where about 20 were expected.

- conf: single (note: "SINGLE SOURCE")
- class: not stated
- holds: mocks
- src: edgarAccuracyMicrobialCommunity2017
- trail: MB-01 §2.10

From the note:

> MB-01:B-0157 [2.10 Denoising and clustering] **Closed and open reference.** QIIME closed- and open-reference OTUs inflated richness to 1,607 to 5,824 OTUs where about 20 were expected.
>
> MB-01:B-0158 [2.10 Denoising and clustering] SINGLE SOURCE.
>

Not found in the cited text (where to look, not what is wrong): holds: mocks

## denoising-clustering.10 (claim)

In leaf litter, bacterial OTU richness was about half of ESV richness (slope 0.46), but alpha and beta metrics correlated at r > 0.90 and inferences matched.

- conf: cont (marker)
- class: meas (marker)
- holds: leaf litter
- src: glassmanBroadscaleEcologicalPatterns2018 (FT; meas; cont)
- trail: MB-01 §2.10

From the note:

> MB-01:I-0058 [2.10 Denoising and clustering] - In leaf litter, bacterial OTU richness was about half of ESV richness (slope 0.46), but alpha and beta metrics correlated at r > 0.90 and inferences matched (Glassman and Martiny 2018) [FT; meas; cont].
>

## denoising-clustering.11 (claim)

In 227 freshwater sediment, seston and mussel-gut samples the direction was reversed: ASV richness was about half of OTU richness, and Mollicutes dominated mussel gut by ASVs but were absent from OTU tables; the authors attribute the reversal partly to higher richness in sediment.

- conf: cont (marker)
- class: meas (marker)
- holds: 227 freshwater sediment, seston and mussel-gut samples
- src: chiarelloRankingBiasesChoice2022 (FT; meas; cont)
- trail: MB-01 §2.10

From the note:

> MB-01:B-0160 [2.10 Denoising and clustering] - In 227 freshwater sediment, seston and mussel-gut samples the direction was reversed.
>
> MB-01:I-0059 [2.10 Denoising and clustering] ASV richness was about half of OTU richness, and Mollicutes dominated mussel gut by ASVs but were absent from OTU tables (Chiarello 2022) [FT; meas; cont].
>
> MB-01:B-0161 [2.10 Denoising and clustering] The authors attribute the reversal partly to higher richness in sediment.
>

## denoising-clustering.12 (claim)

The direction of the OTU versus ASV richness difference conflicts between studies (Glassman and Martiny 2018 against Chiarello 2022).

- conf: cont (note: "OTU versus ASV richness (contested)")
- class: not stated
- holds: the two studies named
- src: glassmanBroadscaleEcologicalPatterns2018, chiarelloRankingBiasesChoice2022
- trail: MB-01 §2.10, §answers, §6. Where

From the note:

> MB-01:B-0159 [2.10 Denoising and clustering] **OTU versus ASV richness (contested).**
>
> MB-01:A-096 [quote: Answers as delivered] The direction of the OTU versus ASV richness difference conflicts between studies (Glassman and Martiny 2018 versus Chiarello 2022).
>
> MB-01:A-120 [quote: Answers as delivered] Direction of the OTU versus ASV richness difference: Glassman and Martiny 2018 versus Chiarello 2022.
>
> MB-01:B-0335 [6. Where the evidence conflicts] OTU versus ASV richness direction: Glassman and Martiny 2018 versus Chiarello 2022.
>

## denoising-clustering.13 (claim)

In soil and plant samples, OTUs versus ASVs changed which families were called differentially abundant, mostly families under 0.1% abundance.

- conf: single (marker)
- class: meas (marker)
- holds: soil and plant samples
- src: joosDaringDifferentialMetabarcoding2020 (FT; meas; single)
- trail: MB-01 §2.10

From the note:

> MB-01:I-0060 [2.10 Denoising and clustering] - In soil and plant samples, OTUs versus ASVs changed which families were called differentially abundant, mostly families under 0.1% abundance (Joos 2020) [FT; meas; single].
>

## denoising-clustering.14 (claim)

The identity threshold that best matched species was about 99% for full-length 16S and about 100% for V4.

- conf: single (marker)
- class: deriv (marker)
- holds: an abstract
- src: edgarUpdating97Identity2018 (AB; deriv; single)
- trail: MB-01 §2.10

From the note:

> MB-01:I-0061 [2.10 Denoising and clustering] **Threshold.** The identity threshold that best matched species was about 99% for full-length 16S and about 100% for V4 (Edgar 2018a) [AB; deriv; single].
>

## denoising-clustering.15 (claim)

As biomass fell in a dilution series, contaminants made up a growing share of inferred communities under every sequence-inference method; the authors state no inference method alone separates contaminants from true sequences.

- conf: single (marker)
- class: meas (marker)
- holds: a dilution series
- src: carusoPerformanceMicrobiomeSequence2019 (FT; meas; single)
- trail: MB-01 §2.10

From the note:

> MB-01:B-0162 [2.10 Denoising and clustering] **Low biomass.** As biomass fell in a dilution series, contaminants made up a growing share of inferred communities under every method.
>
> MB-01:I-0062 [2.10 Denoising and clustering] The authors state no inference method alone separates contaminants from true sequences (Caruso 2019) [FT; meas; single].
>

## denoising-clustering.16 (claim)

According to its documentation, DADA2's independent per-sample processing needs at least two error-free reads to detect an ASV, and pooling finds more ASVs per sample.

- conf: not stated
- class: not stated
- holds: DADA2 documentation
- src: callahanDADA2DocumentationPseudopooling (DOCUMENTATION)
- trail: MB-01 §2.10

From the note:

> MB-01:B-0163 [2.10 Denoising and clustering] **DADA2 modes.** According to its documentation, independent per-sample processing needs at least two error-free reads to detect an ASV.
>
> MB-01:B-0164 [2.10 Denoising and clustering] Pooling finds more ASVs per sample (DADA2 pseudo-pooling page) [DOCUMENTATION].
>

## chimeras.1 (claim)

Chimeras formed reproducibly across independent amplifications of a known mixture; that chimera formation is reproducible rests on this one study, on Sanger and 454 data.

- conf: single (critic: MB-01:C-090)
- class: meas (marker)
- holds: a known mixture, Sanger and 454
- src: haasChimeric16SRRNA2011 (FT; meas; repl; Sanger and 454)
- trail: MB-01 §2.11, §answers, §Adversarial

From the note:

> MB-01:I-0063 [2.11 Chimera detection] **Formation.** Chimeras formed reproducibly across independent amplifications of a known mixture (Haas 2011) [FT; meas; repl; Sanger and 454].
>
> MB-01:A-075 [quote: Answers as delivered] Consistency: chimera formation was reproducible across amplifications.
>
> MB-01:B-0070 [2. Steps from sample to table (D1) and departures from the sampled community (D2)] Up to over 70% chimeric for rare species (454) | Reproducible across amplifications | Sze and Schloss 2019; Haas 2011 |
>
> MB-01:C-090 [warning: Adversarial critique, full findings] - D2 answer: 'Chimeras ... Consistency: chimera formation was reproducible across amplifications' rests on Haas 2011 (Sanger and 454) alone.
>

## chimeras.2 (claim)

Less-abundant species showed chimera rates above 70% on 454, and chimera count correlated with organism abundance (R2 = 0.97) in a staggered mock.

- conf: not stated
- class: not stated
- holds: 454; a staggered mock
- src: haasChimeric16SRRNA2011
- trail: MB-01 §2.11, §answers

From the note:

> MB-01:B-0165 [2.11 Chimera detection] Less-abundant species showed chimera rates above 70%.
>
> MB-01:B-0166 [2.11 Chimera detection] Chimera count correlated with organism abundance (R2 = 0.97) in a staggered mock.
>
> MB-01:A-074 [quote: Answers as delivered] They exceeded 70% for rare species on 454 (Haas 2011).
>
> MB-01:B-0070 [2. Steps from sample to table (D1) and departures from the sampled community (D2)] Up to over 70% chimeric for rare species (454) | Reproducible across amplifications | Sze and Schloss 2019; Haas 2011 |
>

## chimeras.3 (claim)

ChimeraSlayer detected over 87% of simulated chimeras when parents diverged by 4% or more, with a 1.6% false-positive rate, and sensitivity fell for every method as parents became more similar.

- conf: not stated
- class: not stated
- holds: simulated chimeras
- src: haasChimeric16SRRNA2011
- trail: MB-01 §2.11

From the note:

> MB-01:B-0167 [2.11 Chimera detection] **Detection.** ChimeraSlayer detected over 87% of simulated chimeras when parents diverged by 4% or more, with a 1.6% false-positive rate.
>
> MB-01:B-0168 [2.11 Chimera detection] Sensitivity fell for every method as parents became more similar.
>

## chimeras.4 (claim)

At 30 cycles, chimeras made up 0.9% (Accuprime) to 18.2% (Platinum) of reads, depending on polymerase.

- conf: not stated
- class: not stated
- holds: 30 cycles; verified in full text
- src: szeImpactDNAPolymerase2019
- trail: MB-01 §2.11, §answers

From the note:

> MB-01:B-0169 [2.11 Chimera detection] At 30 cycles, chimera rates were 0.9% (Accuprime) to 18.2% (Platinum), and UCHIME sensitivity was 50 to 87% at 25 or more cycles (Sze and Schloss 2019, verified).
>
> MB-01:A-073 [quote: Answers as delivered] At 30 cycles they made up 0.9-18.2% of reads depending on polymerase (Sze and Schloss 2019).
>
> MB-01:B-0069 [2. Steps from sample to table (D1) and departures from the sampled community (D2)] | Chimeras | 0.9 to 18.2% of reads at 30 cycles, depending on polymerase | False novel taxa.
>

Not found in the cited text (where to look, not what is wrong): holds: in

## chimeras.5 (claim)

UCHIME sensitivity was 50 to 87% at 25 or more cycles.

- conf: not stated
- class: not stated
- holds: 25 or more cycles
- src: szeImpactDNAPolymerase2019
- trail: MB-01 §2.11

From the note:

> MB-01:B-0169 [2.11 Chimera detection] At 30 cycles, chimera rates were 0.9% (Accuprime) to 18.2% (Platinum), and UCHIME sensitivity was 50 to 87% at 25 or more cycles (Sze and Schloss 2019, verified).
>

## chimeras.6 (claim)

UCHIME2's author states that error-free chimera prediction is "impossible in principle".

- conf: not stated
- class: not stated
- holds: a developer claim in a preprint abstract
- src: edgarUCHIME2ImprovedChimera2016 (AB; PREPRINT; developer claim)
- trail: MB-01 §2.11

From the note:

> MB-01:B-0170 [2.11 Chimera detection] UCHIME2's author states error-free chimera prediction is "impossible in principle" (Edgar 2016b) [AB; PREPRINT; developer claim].
>

## chimeras.7 (claim)

Chimeras inflate richness and create false novel taxa.

- conf: not stated
- class: not stated
- holds: as stated in the answers
- src: szeImpactDNAPolymerase2019, haasChimeric16SRRNA2011
- trail: MB-01 §answers

From the note:

> MB-01:A-072 [quote: Answers as delivered] Taxa: chimeras inflate richness and create false novel taxa.
>
> MB-01:B-0069 [2. Steps from sample to table (D1) and departures from the sampled community (D2)] | Chimeras | 0.9 to 18.2% of reads at 30 cycles, depending on polymerase | False novel taxa.
>

Not found in the cited text (where to look, not what is wrong): holds: in

## taxonomy.1 (claim)

Cross-validated by identity to the reference, all tested classifiers were at most 50% accurate on V4; genus accuracy was about 100% at 100% identity and about 50% at 97%, derived from reference sets by one author who also develops competing classifiers.

- conf: single (marker)
- class: meas (marker)
- holds: V4, reference sets; accuracy depends on distance to reference
- src: edgarAccuracyTaxonomyPrediction2018 (FT; meas; single)
- trail: MB-01 §2.12, §answers, §Adversarial

From the note:

> MB-01:B-0171 [2.12 Taxonomic assignment] **Accuracy.** Cross-validated by identity to the reference, all tested classifiers were at most 50% accurate on V4.
>
> MB-01:I-0064 [2.12 Taxonomic assignment] Genus accuracy was about 100% at 100% identity and about 50% at 97% (Edgar 2018b) [FT; meas; single].
>
> MB-01:A-097 [quote: Answers as delivered] Taxa and labels: V4 genus accuracy was about 50% at 97% identity to the reference (Edgar 2018b, derived from reference sets).
>
> MB-01:B-0076 [2. Steps from sample to table (D1) and departures from the sampled community (D2)] | Classification | n/a | V4 genus accuracy about 50% at 97% identity. 56 to 88% false genus names with closed reference | Depends on distance to reference | Edgar 2018b; Edgar 2017a |
>
> MB-01:C-089 [warning: Adversarial critique, full findings] - Section 2.12: V4 genus accuracy of about 50% at 97% identity and 10 to 17% database annotation error rest on Edgar 2018b and 2018c, from one author who also develops competing classifiers. Flagged single in the text but used in the D2 answer without that qualifier.
>

## taxonomy.2 (claim)

Edgar 2018b's author argues that mocks overstate classification accuracy because all their members are named type strains.

- conf: not stated
- class: not stated
- holds: an argument
- src: edgarAccuracyTaxonomyPrediction2018
- trail: MB-01 §2.12, §answers

From the note:

> MB-01:B-0172 [2.12 Taxonomic assignment] The author argues that mocks overstate accuracy because all their members are named type strains.
>
> MB-01:A-099 [quote: Answers as delivered] On mocks, genus median F exceeded 0.8 (Bokulich 2018); Edgar 2018b argues that mocks overstate accuracy.
>

## taxonomy.3 (claim)

On mocks, the q2-feature-classifier methods reached median genus F above 0.8.

- conf: not stated
- class: meas (marker)
- holds: mocks; a developer claim
- src: bokulichOptimizingTaxonomicClassification2018 (FT; meas; developer claim)
- trail: MB-01 §2.12, §answers

From the note:

> MB-01:I-0065 [2.12 Taxonomic assignment] On mocks, the q2-feature-classifier methods reached median genus F above 0.8 (Bokulich 2018) [FT; meas; developer claim].
>
> MB-01:A-099 [quote: Answers as delivered] On mocks, genus median F exceeded 0.8 (Bokulich 2018); Edgar 2018b argues that mocks overstate accuracy.
>

## taxonomy.4 (claim)

Habitat-weighted priors cut species-level classification error from 25% to 14%.

- conf: not stated
- class: meas (marker)
- holds: a developer claim
- src: kaehlerSpeciesAbundanceInformation2019 (FT; meas; developer claim)
- trail: MB-01 §2.12

From the note:

> MB-01:I-0066 [2.12 Taxonomic assignment] Habitat-weighted priors cut species-level error from 25% to 14% (Kaehler 2019) [FT; meas; developer claim].
>

## taxonomy.5 (claim)

IDTAXA over-classified less when the true taxa were absent from the training set.

- conf: not stated
- class: meas (marker)
- holds: a developer claim; the reference is listed under Murali and cited by the bioinformatics angle
- src: muraliIDTAXANovelApproach2018 (FT; meas; developer claim)
- trail: MB-01 §2.12

From the note:

> MB-01:I-0067 [2.12 Taxonomic assignment] **Over-classification.** IDTAXA over-classified less when the true taxa were absent from the training set (Murali 2018) [FT; meas; developer claim].
>
> MB-01:B-0173 [2.12 Taxonomic assignment] (Reference listed under Murali; cited by the bioinformatics angle.)
>

## taxonomy.6 (claim)

Estimated annotation error in reference databases is about 10% for RDP and about 17% for SILVA v128 and Greengenes 13.5, judged from conflicting labels on identical sequences; this rests on one author who also develops competing classifiers.

- conf: single (marker)
- class: deriv (marker)
- holds: RDP, SILVA v128, Greengenes 13.5
- src: edgarTaxonomyAnnotationGuide2018 (FT; deriv; single)
- trail: MB-01 §2.12, §answers, §Adversarial

From the note:

> MB-01:I-0068 [2.12 Taxonomic assignment] **Databases.** Estimated annotation error is about 10% for RDP and about 17% for SILVA v128 and Greengenes 13.5, judged from conflicting labels on identical sequences (Edgar 2018c) [FT; deriv; single].
>
> MB-01:A-098 [quote: Answers as delivered] Reference databases carry about 10-17% annotation error (Edgar 2018c).
>
> MB-01:C-089 [warning: Adversarial critique, full findings] - Section 2.12: V4 genus accuracy of about 50% at 97% identity and 10 to 17% database annotation error rest on Edgar 2018b and 2018c, from one author who also develops competing classifiers. Flagged single in the text but used in the D2 answer without that qualifier.
>

## taxonomy.7 (claim)

On simulated gut, ocean and soil communities, genus recall was 67 to 80%, and assignments varied by up to 40% between 16S subregions within a pipeline.

- conf: single (marker)
- class: model (marker)
- holds: simulated gut, ocean and soil communities
- src: almeidaBenchmarkingTaxonomicAssignments2018 (FT; model; single)
- trail: MB-01 §2.12

From the note:

> MB-01:I-0069 [2.12 Taxonomic assignment] **Environment and region.** On simulated gut, ocean and soil communities, genus recall was 67 to 80% and assignments varied by up to 40% between 16S subregions within a pipeline (Almeida 2018) [FT; model; single].
>

## taxonomy.8 (claim)

On V4 mocks, 56 to 88% of predicted genus names were false positives with closed-reference OTUs.

- conf: single (marker)
- class: meas (marker)
- holds: V4 mocks
- src: edgarAccuracyMicrobialCommunity2017 (FT; meas; single)
- trail: MB-01 §2.10

From the note:

> MB-01:I-0057 [2.10 Denoising and clustering] On V4 mocks, 56 to 88% of predicted genus names were false positives (Edgar 2017a) [FT; meas; single].
>
> MB-01:B-0076 [2. Steps from sample to table (D1) and departures from the sampled community (D2)] | Classification | n/a | V4 genus accuracy about 50% at 97% identity. 56 to 88% false genus names with closed reference | Depends on distance to reference | Edgar 2018b; Edgar 2017a |
>

