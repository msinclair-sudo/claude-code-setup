---
type: knowledge
title: Recovery of rRNA genes from metagenome assemblies and MAGs
inputs:
  - CB2-RRNA: PhD/Proposal/Research/Results/Recovery of rRNA Genes from Metagenome Assemblies and MAGs.md
refs: PhD/Proposal/Refs/Refs.bib
built: 2026-10-21
status: draft
tags:
  - research
  - knowledge
---

# Recovery of rRNA genes from metagenome assemblies and MAGs

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
| CB2-RRNA | [[Recovery of rRNA Genes from Metagenome Assemblies and MAGs]] | no (the note says none ran) | narrative author-year | no | no | fallback |

## Concepts

### rrna-gene: The 16S rRNA gene and its copies
needs: none
- **rrna-gene.bg1** The 16S rRNA gene is present in almost all bacteria, often as a multigene family or in operons; its function has not changed over time, and it is large enough for informatics purposes.
  kind: background · ref: janda16SRRNAGene2007 · check: DOI 10.1128/JCM.01228-07 resolves on Crossref (J Clin Microbiol 45(9), 2761–2764; PMC2045242); stated in the opening paragraphs of the PMC full text, before the first heading
- **rrna-gene.1** Větrovský & Baldrian extracted 7,081 16S sequences from 1,690 bacterial genomes: 1–15 copies per genome, mean 4.2, with mean within-genome similarity 99.70 ± 0.46%.
  conf: not stated · class: meas (note: "extracted 7,081 16S sequences") · holds: 1,690 bacterial genomes · src: vetrovskyVariability16SRRNA2013 (full text, targeted verbatim quotations via automated fetch) · trail: CB2-RRNA §The mechanism · from: CB2-RRNA:B-0061
- **rrna-gene.2** Near-identical repeats of about 1.5 kb (within an operon of about 5 kb) are the classic short-read assembly failure mode.
  conf: not stated · class: not stated · holds: short-read assembly; the reviewer's statement, no source cited for it · src: none (the reviewer's statement; no source cited) · trail: CB2-RRNA §The mechanism · from: CB2-RRNA:B-0062

### mimag-hq: The MIMAG high-quality standard
needs: rrna-gene
- **mimag-hq.1** The MIMAG high-quality bar requires 5S, 16S and 23S rRNA plus at least 18 tRNAs on top of at least 90% completeness and at most 5% contamination.
  conf: not stated · class: not stated · holds: Bowers et al. 2017, as applied in the catalogue papers · src: bowers2017 · trail: CB2-RRNA §Measured recovery rates · from: CB2-RRNA:B-0019
- **mimag-hq.2** That composite makes the rRNA requirement the binding constraint on the high-quality bar, and several papers say so directly.
  conf: not stated · class: not stated · holds: the catalogue papers reviewed · src: nayfachGenomicCatalogEarths2020, maGenomicCatalogueSoil2023, almeidaUnifiedCatalog2042020 · trail: CB2-RRNA §Measured recovery rates · from: CB2-RRNA:B-0020

### catalogue-recovery: rRNA recovery measured in published MAG catalogues
needs: mimag-hq
- **catalogue-recovery.1** GEM (all biomes, more than 10,000 metagenomes): 9,143 of 52,515 MAGs (17.4%) were high quality, carrying the full rRNA set.
  conf: not stated · class: meas (note: "Measured recovery rates in published catalogues") · holds: all biomes, more than 10,000 metagenomes · src: nayfachGenomicCatalogEarths2020 (full text, targeted verbatim quotations via automated fetch) · trail: CB2-RRNA §Measured recovery rates · from: CB2-RRNA:B-0021, CB2-RRNA:B-0022
- **catalogue-recovery.2** The GEM catalogue's mean completeness is 83% with mean contamination 1.3%, and the paper names "problems assembling the 16S rRNA locus" as one reason new species' MAGs came out less complete than known ones.
  conf: not stated · class: not stated · holds: GEM catalogue · src: nayfachGenomicCatalogEarths2020 · trail: CB2-RRNA §Measured recovery rates · from: CB2-RRNA:B-0028
- **catalogue-recovery.3** SMAG (soil, 3,304 metagenomes): 3,641 of 40,039 MAGs (9.1%) were high quality, carrying the full rRNA set.
  conf: not stated · class: meas (note: "Measured recovery rates in published catalogues") · holds: soil, 3,304 metagenomes · src: maGenomicCatalogueSoil2023 (full text, targeted verbatim quotations via automated fetch) · trail: CB2-RRNA §Measured recovery rates · from: CB2-RRNA:B-0023
- **catalogue-recovery.4** UHGG (human gut): of 4,644 species representatives, 573 carried the full rRNA set, of which 38 are MAGs and 535 are isolates.
  conf: not stated · class: meas (note: "Measured recovery rates in published catalogues") · holds: human gut, species representatives · src: almeidaUnifiedCatalog2042020 (full text, targeted verbatim quotations via automated fetch) · trail: CB2-RRNA §Measured recovery rates · from: CB2-RRNA:B-0024
- **catalogue-recovery.5** Tropical activated sludge (Haryono et al.): of 9,079 bins, 142 (1.6% of all bins) carried 5S, 16S and 23S rRNA genes, and 58 met the full MIMAG standard.
  conf: not stated · class: meas (note: "Measured recovery rates in published catalogues") · holds: engineered system, tropical full-scale activated sludge · src: haryonoRecoveryHighQuality2022, haryono2021 (verified in extracted text) · trail: CB2-RRNA §Measured recovery rates · from: CB2-RRNA:B-0025
- **catalogue-recovery.6** The most-quoted single number in this literature is that only 7% of more than 270,000 MAGs yield a 16S sequence under a barrnap search, against 93% of more than 106,000 RefSeq genomes (Hiseni et al. 2022); its direction agrees with every catalogue above, but the figure rests on an Opinion article with no methods section (no barrnap length threshold, no statement of which source catalogues the MAGs came from beyond the authors' HumGut collection, no breakdown).
  conf: not stated · class: not stated · holds: human gut MAGs (HumGut) against RefSeq genomes; method undocumented · src: hiseniQuestioningQuality16S2022 (Opinion article; no methods section) · trail: CB2-RRNA §Measured recovery rates · from: CB2-RRNA:B-0029, CB2-RRNA:B-0030, CB2-RRNA:B-0031
- **catalogue-recovery.7** Hiseni et al. also report that 97.5%-ANI clusters composed purely of MAGs share on average 93% 16S identity, while clusters of complete RefSeq genomes share 99.8%, an anomaly for a gene that conserved; they argue that the 16S sequences MAGs do carry are often wrong. The same caveat (no documented method) applies.
  conf: not stated · class: not stated · holds: human gut MAG clusters against RefSeq clusters; method undocumented · src: hiseniQuestioningQuality16S2022 (Opinion article; no methods section) · trail: CB2-RRNA §Measured recovery rates · from: CB2-RRNA:B-0033, CB2-RRNA:B-0034
- **catalogue-recovery.8** Gruber-Vodicka et al. state that "most metagenome-assembled genomes (MAGs) do not contain even fragments of the SSU rRNA gene, not to mention the full gene," and Ma et al. that "near full-complement rRNA genes sequences are challenging for assembling from metagenomes, especially for near-complete MAGs."
  conf: not stated · class: not stated · holds: statements in a tool paper and a catalogue paper · src: grubervodickaPhyloFlashRapidSmallsubunit2020, maGenomicCatalogueSoil2023 · trail: CB2-RRNA §Bounding facts · from: CB2-RRNA:B-0080, CB2-RRNA:B-0081

### marker-gap: rRNA presence against single-copy-marker completeness
needs: catalogue-recovery
- **marker-gap.1** In SMAG (soil), 3,641 MAGs were high quality with rRNA, and a further 5,184 reached at least 90% completeness and under 5% contamination but failed on "the absence of all rRNA genes or less than 18 tRNAs"; so of 8,825 soil MAGs that the single-copy marker estimate calls near-complete, roughly 41% carry the rRNA complement.
  conf: not stated · class: not stated · holds: soil (SMAG); the 41% is the reviewer's arithmetic from the paper's counts · src: maGenomicCatalogueSoil2023 · trail: CB2-RRNA §Side by side · from: CB2-RRNA:B-0035, CB2-RRNA:B-0036, CB2-RRNA:B-0037
- **marker-gap.2** In tropical activated sludge (Haryono et al.), of 9,079 bins 1,085 (11.9%) were "putative high quality" on single-copy marker statistics; of those, 142 (13.1%) "contained at least one copy of the 5S, 16S and 23S SSU-rRNA genes"; the stringent MIMAG criteria left "only 58 HQ-MAGs" (around 1,000 looked high quality by marker genes, 58 formally were).
  conf: not stated · class: not stated · holds: tropical full-scale activated sludge · src: haryono2021 (verified in extracted text), haryonoRecoveryHighQuality2022 · trail: CB2-RRNA §Side by side · from: CB2-RRNA:B-0038, CB2-RRNA:B-0039
- **marker-gap.3** In UHGG (human gut), 3,207 of 4,644 species representatives were over 90% complete and under 5% contaminated; 573 additionally had 5S/16S/23S plus at least 18 tRNAs, and only 38 of those 573 were MAGs. The paper attributes this to the rRNA operon being "a problematic region to assemble from short-read metagenomic datasets".
  conf: not stated · class: not stated · holds: human gut species representatives · src: almeidaUnifiedCatalog2042020 · trail: CB2-RRNA §Side by side · from: CB2-RRNA:B-0040, CB2-RRNA:B-0041
- **marker-gap.4** In Hiseni et al.'s human gut analysis, all MAGs were over 95% complete with under 5% contamination on the single-copy marker criterion, and 7% had a detectable 16S.
  conf: not stated · class: not stated · holds: human gut MAGs; method undocumented (Opinion article) · src: hiseniQuestioningQuality16S2022 (Opinion article; no methods section) · trail: CB2-RRNA §Side by side · from: CB2-RRNA:B-0042
- **marker-gap.5** Across four environments and four pipelines, a genome can be scored 90–95% complete on conserved single-copy protein-coding genes and still have no assembled, correctly binned 16S: the completeness statistic and the rRNA statistic do not measure the same thing, and the gap is typically a factor of two to ten depending on the catalogue.
  conf: repl (note: "consistent across four environments and four pipelines") · class: not stated · holds: four environments and four pipelines · src: maGenomicCatalogueSoil2023, haryonoRecoveryHighQuality2022, almeidaUnifiedCatalog2042020, hiseniQuestioningQuality16S2022 · trail: CB2-RRNA §Side by side · from: CB2-RRNA:B-0043, CB2-RRNA:B-0044

### assembly-fragmentation: Fragmentation and chimeras in assembled rRNA genes
needs: rrna-gene
- **assembly-fragmentation.1** Three mechanisms are offered for the shortfall: two assembly-side and one binning-side.
  conf: not stated · class: not stated · holds: the mechanisms offered in the reviewed papers · src: vollmersComparingEvaluatingMetagenome2017, grubervodickaPhyloFlashRapidSmallsubunit2020, vetrovskyVariability16SRRNA2013, songMarkerMAGLinkingMetagenomeassembled2022 · trail: CB2-RRNA §The mechanism · from: CB2-RRNA:B-0045, CB2-RRNA:B-0046
- **assembly-fragmentation.2** Vollmers et al. describe 16S genes as posing "a highly challenging problem for metagenome assemblers" because multiple highly conserved regions interspersed with hypervariable stretches produce "highly complex branched assembly graph structures", splitting the gene into short contigs confined to conserved regions.
  conf: not stated · class: assert (note: "Neither statement is itself a measurement") · holds: a mechanism statement, not a measurement · src: vollmersComparingEvaluatingMetagenome2017 · trail: CB2-RRNA §The mechanism · from: CB2-RRNA:B-0047, CB2-RRNA:B-0049
- **assembly-fragmentation.3** Gruber-Vodicka et al. give the same account in k-mer terms: conserved regions "lead to sets of shared k-mers among the SSU rRNA sequences present in the read pool that confound the assembly graph structure and eventually cause fragmented assemblies".
  conf: not stated · class: assert (note: "Neither statement is itself a measurement") · holds: a mechanism statement, not a measurement · src: grubervodickaPhyloFlashRapidSmallsubunit2020 · trail: CB2-RRNA §The mechanism · from: CB2-RRNA:B-0048, CB2-RRNA:B-0049
- **assembly-fragmentation.4** CAMI II quantified 16S completeness per assembler against 131 known 16S sequences in the marine dataset: short-read assemblies recovered 16S at mean completeness between 29.6% (HipMer) and 36.9% (MEGAHIT).
  conf: not stated · class: model (note: "same simulated data across submissions") · holds: CAMI II marine dataset, 131 known 16S sequences · src: meyerCriticalAssessmentMetagenome2022 · trail: CB2-RRNA §The mechanism · from: CB2-RRNA:B-0050, CB2-RRNA:B-0051, CB2-RRNA:B-0052, CB2-RRNA:B-0087
- **assembly-fragmentation.5** In CAMI II, for every assembler except the two hybrids, the median length of contigs aligning to a 16S gene was below the average 16S gene length of 1,503 bp: the gene is typically fragmented, not recovered.
  conf: not stated · class: model (note: "same simulated data across submissions") · holds: CAMI II marine dataset · src: meyerCriticalAssessmentMetagenome2022 · trail: CB2-RRNA §The mechanism · from: CB2-RRNA:B-0053, CB2-RRNA:B-0087
- **assembly-fragmentation.6** On a synthetic community of 64 organisms, SPAdes and MEGAHIT run on SortMeRNA-extracted 16S reads recovered genome fractions of 39.9% and 44.3% respectively; averaged across five simulated depths, SPAdes contigs were 21.2% chimeric and MEGAHIT 23.8%.
  conf: not stated · class: model (note: "five simulated depths") · holds: MATAM benchmark, synthetic community of 64 organisms, five simulated depths · src: pericard2017 (verified in extracted text), pericardMATAMReconstructionPhylogenetic2018 · trail: CB2-RRNA §The mechanism · from: CB2-RRNA:B-0054, CB2-RRNA:B-0055, CB2-RRNA:B-0056
- **assembly-fragmentation.7** Assembling simulated shotgun data conventionally yielded 253 distinct 16S sequences, of which "only 1 gave a >99% match to some of the actual 16S sequences" (METASEED).
  conf: single (note: "This is one paper and one lab") · class: model (note: "assembling simulated shotgun data") · holds: simulated shotgun data; no independent replication found · src: philipMETASEEDNovelApproach2024 (single-pass extraction) · trail: CB2-RRNA §The mechanism · from: CB2-RRNA:B-0057, CB2-RRNA:B-0060
- **assembly-fragmentation.8** On real seafloor sediment, 26,133,575 contigs yielded 150 distinct 16S sequences after clustering, and only 51 matched amplicon OTUs from the same samples at more than 99%.
  conf: single (note: "This is one paper and one lab") · class: meas (note: "On real seafloor sediment") · holds: seafloor sediment, amplicon OTUs from the same samples · src: philipMETASEEDNovelApproach2024 (single-pass extraction) · trail: CB2-RRNA §The mechanism · from: CB2-RRNA:B-0058, CB2-RRNA:B-0060
- **assembly-fragmentation.9** The METASEED authors' framing is that conventional assembly produces mosaic sequences; the reviewer calls the support for the "1 of 253" result thin, though it points the same way as the MATAM chimera rates.
  conf: single (note: "This is one paper and one lab") · class: not stated · holds: one paper, one lab · src: philipMETASEEDNovelApproach2024 (single-pass extraction), pericard2017 · trail: CB2-RRNA §The mechanism · from: CB2-RRNA:B-0059, CB2-RRNA:B-0060

### binning-loss: Loss of rRNA genes in binning
needs: rrna-gene
- **binning-loss.1** Song et al. state that multiple 16S copies "result in unusually high read-depth information" for the contig carrying them, which together with "atypical nucleotide composition, hinders its correct binning with the rest of the genome"; Gruber-Vodicka et al. make the same point.
  conf: not stated · class: not stated · holds: coverage-based binning; a mechanism statement · src: songMarkerMAGLinkingMetagenomeassembled2022, grubervodickaPhyloFlashRapidSmallsubunit2020 · trail: CB2-RRNA §The mechanism · from: CB2-RRNA:B-0063, CB2-RRNA:B-0064
- **binning-loss.2** No paper the reviewer found isolates and quantifies the binning contribution separately from the assembly contribution: nobody measured what fraction of missing 16S genes were assembled but then binned elsewhere, against never assembled at all.
  conf: not stated · class: search (note: "I did not find a paper that isolates and quantifies the binning contribution") · holds: the literature searched by the review · src: none (a search result) · trail: CB2-RRNA §The mechanism · from: CB2-RRNA:B-0065, CB2-RRNA:B-0066

### sequencing-technology: Read length and sequencing technology
needs: catalogue-recovery, assembly-fragmentation
- **sequencing-technology.1** Read length and sequencing technology are directly and repeatedly measured as an axis of variation in rRNA recovery.
  conf: not stated · class: not stated · holds: Orellana et al., CAMI II, Overholt et al., Singleton et al. · src: orellanaComparingGenomesRecovered2023, meyerCriticalAssessmentMetagenome2022, overholtInclusionOxfordNanopore2020, singletonConnectingStructureFunction2021 · trail: CB2-RRNA §Verdict, §What is measured about variation, §Verdict on the second · from: CB2-RRNA:A-002, CB2-RRNA:A-008, CB2-RRNA:B-0083 · rating: "DIRECT EVIDENCE, and it is good"
- **sequencing-technology.2** Orellana et al. sequenced the same North Sea bloom samples with Illumina HiSeq (about 240 bp paired-end, about 36 Gbp per sample) and PacBio HiFi (about 6 kbp CCS reads, about 12 Gbp per sample): "88% of the total long-read MAGs carried a 16S rRNA gene compared to only 23% of MAGs recovered from short-read metagenomes" (254 long-read against 341 short-read MAGs).
  conf: not stated · class: meas (note: "North Sea bloom samples") · holds: North Sea time series, marine; same samples, two technologies · src: orellanaComparingGenomesRecovered2023 · trail: CB2-RRNA §Measured recovery rates, §What is measured about variation · from: CB2-RRNA:B-0027, CB2-RRNA:B-0083, CB2-RRNA:B-0084, CB2-RRNA:A-002, CB2-RRNA:A-008 · rating: "DIRECT EVIDENCE, and it is good"
- **sequencing-technology.3** In Orellana et al. the depth confound runs against the effect: the short-read libraries were three times deeper and still recovered 16S in a quarter as many MAGs; this is the cleanest controlled comparison the reviewer found on any axis.
  conf: not stated · class: not stated · holds: Orellana et al., same samples · src: orellanaComparingGenomesRecovered2023 · trail: CB2-RRNA §What is measured about variation · from: CB2-RRNA:B-0085, CB2-RRNA:B-0086, CB2-RRNA:A-002, CB2-RRNA:A-008
- **sequencing-technology.4** Singleton et al. (long-read activated sludge): all 1,083 MAGs in their high-quality set "encode full-length 16S rRNA, 23S rRNA, 5S rRNA, and >18 tRNA genes", and 91.3% (1,045 of 1,145) of near-complete MAGs carried full-length 16S.
  conf: not stated · class: not stated · holds: activated sludge, long-read sequencing · src: singletonConnectingStructureFunction2021 · trail: CB2-RRNA §Measured recovery rates, §Bounding facts · from: CB2-RRNA:B-0026, CB2-RRNA:B-0067
- **sequencing-technology.5** Singleton et al. contrast this with a short-read activated sludge study: of Ye et al.'s MAGs, "31% (644) met the MIMAG HQ completeness and contamination threshold … but only 1.2% (25 MAGs) were of HQ according to the MIMAG standards and encoded the rRNA genes". The contrast is across two studies and two plants and confounds technology with everything else (plant, depth, pipeline).
  conf: not stated · class: not stated · holds: two different studies and plants; Ye et al.'s figures as reported by Singleton et al., not verified against the original · src: singletonConnectingStructureFunction2021, ye2020 (cited within Singleton et al. 2021; not independently retrieved) · trail: CB2-RRNA §Bounding facts, §What is measured about variation · from: CB2-RRNA:B-0068, CB2-RRNA:B-0069, CB2-RRNA:B-0108
- **sequencing-technology.6** CAMI II, on the same simulated data across submissions: hybrid assemblers GATB (mean 16S completeness 60.1%) and OPERA-MS (47.1%) against short-read assemblers at 29.6–36.9%; median 16S-aligning contig length 8,513 bp and 4,430 bp for the two hybrids against below 1,503 bp for the rest.
  conf: not stated · class: model (note: "same simulated data across submissions") · holds: CAMI II marine dataset, simulated · src: meyerCriticalAssessmentMetagenome2022 · trail: CB2-RRNA §What is measured about variation, §Verdict · from: CB2-RRNA:B-0083, CB2-RRNA:B-0087, CB2-RRNA:A-003, CB2-RRNA:A-009 · rating: "DIRECT EVIDENCE, and it is good"
- **sequencing-technology.7** Overholt et al. (preprint): among 44 MAGs recovered by both the Illumina-only and the hybrid assembly of the same aquifer samples, the hybrid set had 16 MAGs with a 16S gene against 10 for Illumina-only (16 against 15 for 5S, 13 against 9 for 23S), a difference that was not significant on a two-proportion z-test.
  conf: not stated · class: meas (note: "same aquifer samples") · holds: one aquifer system, 44 shared MAGs, hybrid against Illumina-only · src: overholt2019 (verified in extracted text), overholtInclusionOxfordNanopore2020 · trail: CB2-RRNA §What is measured about variation, §Verdict on the second · from: CB2-RRNA:B-0088, CB2-RRNA:A-008
- **sequencing-technology.8** The published Overholt et al. version adds an ONT-only assembly and reports in its abstract that the ONT-only MAGs had a probability of containing rRNA genes "3× higher than either of the other methods"; within this one study the hybrid-against-short-read effect on rRNA was null and the long-read-only effect large.
  conf: not stated · class: not stated · holds: one aquifer system; the ONT-only result from the published abstract (the preprint lacks it) · src: overholtInclusionOxfordNanopore2020 (abstract) · trail: CB2-RRNA §What is measured about variation · from: CB2-RRNA:B-0089, CB2-RRNA:B-0090
- **sequencing-technology.9** The size of the long-read effect differs between studies: Overholt et al.'s null hybrid-against-short-read result is a disagreement in magnitude with Orellana et al. and Singleton et al., not an agreement.
  conf: cont (note: "disagreement in magnitude") · class: not stated · holds: Overholt et al. (aquifer), Orellana et al. (North Sea), Singleton et al. (activated sludge) · src: overholtInclusionOxfordNanopore2020, orellanaComparingGenomesRecovered2023, singletonConnectingStructureFunction2021 · trail: CB2-RRNA §What is measured about variation · from: CB2-RRNA:B-0091

### targeted-reconstruction: Targeted rRNA reconstruction tools
needs: assembly-fragmentation
- **targeted-reconstruction.1** Targeted tools recover far more than general assembly: Yuan et al. benchmarked generic against targeted assemblers; on a simulated 11-species set, REAGO recovered 11/11 genes with 1 incorrect assembly, EMIRGE 6/11 (genus-excluded database) with 17 incorrect, IDBA-UD 3/11 with 413 incorrect and MetaVelvet 1/11 with 1,257.
  conf: not stated · class: model (note: "On a simulated 11-species set") · holds: simulated 11-species set · src: yuanReconstructing16SRRNA2015 · trail: CB2-RRNA §Bounding facts · from: CB2-RRNA:B-0070, CB2-RRNA:B-0071
- **targeted-reconstruction.2** On a 64-species synthetic community (Yuan et al.): REAGO 58/64 (2 incorrect), IDBA-UD 39/64 (28 incorrect), EMIRGE 19/64 (89 incorrect), MetaVelvet 4/64 (131 incorrect).
  conf: not stated · class: not stated · holds: 64-species synthetic community; the note does not say whether simulated or sequenced · src: yuanReconstructing16SRRNA2015 · trail: CB2-RRNA §Bounding facts · from: CB2-RRNA:B-0072
- **targeted-reconstruction.3** The targeted tools are not clean either: on the synthetic community, MATAM reached genome fraction 83.1% with 3.2% chimeras, EMIRGE 50.7% with 17.4% chimeras and REAGO 42.8% with 15.5% chimeras.
  conf: not stated · class: not stated · holds: MATAM benchmark, synthetic community of 64 organisms · src: pericard2017 (verified in extracted text), pericardMATAMReconstructionPhylogenetic2018 · trail: CB2-RRNA §Bounding facts · from: CB2-RRNA:B-0073
- **targeted-reconstruction.4** All methods handled genes sharing under 90% identity with their nearest neighbour, but "performances significantly dropped" for paralogous copies around 99% identity, where EMIRGE and REAGO merged reads from distinct paralogs into single erroneous sequences.
  conf: not stated · class: not stated · holds: MATAM benchmark · src: pericard2017 (verified in extracted text) · trail: CB2-RRNA §Bounding facts · from: CB2-RRNA:B-0074
- **targeted-reconstruction.5** METASEED reports 1,631 reconstructions with 1,534 matching at more than 99% (6% false positives), against EMIRGE 1,589/1,118 (30%) and MATAM 992/832 (16%).
  conf: not stated · class: not stated · holds: the tool's own authors' benchmark · src: philipMETASEEDNovelApproach2024 (single-pass extraction; from the tool's own authors) · trail: CB2-RRNA §Bounding facts · from: CB2-RRNA:B-0075
- **targeted-reconstruction.6** Fan et al. recovered near-full-length 16S from 454 pyrosequencing of a sponge metagenome with a 3.6% chimera rate before filtering, which they note is below the 5–45% typically reported for PCR amplicons.
  conf: not stated · class: meas (note: "454 pyrosequencing of a sponge metagenome") · holds: read length about 350 nt; a sponge community, low-complexity relative to soil; not shown for Illumina-length reads in a complex environment · src: fanReconstructionRibosomalRNA2012 · trail: CB2-RRNA §Bounding facts · from: CB2-RRNA:B-0078, CB2-RRNA:B-0079

### linking-tools: Linking 16S genes to MAGs
needs: binning-loss, catalogue-recovery
- **linking-tools.1** MarkerMAG, on benchmark datasets at 100% linking accuracy, recovered 88.2% (15/17 MAGs, low-complexity MBARC-26), 53.5% (23/43, medium complexity) and 46.7% (14/30, high complexity); on real data the improvement over baseline ranged from 1.1-fold (macroalgae) to 14.2-fold (pig gut). Linking tools recover part but not most of the gap.
  conf: not stated · class: not stated · holds: benchmark datasets of three complexities; real data from macroalgae to pig gut · src: songMarkerMAGLinkingMetagenomeassembled2022 (single-pass extraction of the article HTML) · trail: CB2-RRNA §Bounding facts · from: CB2-RRNA:B-0076, CB2-RRNA:B-0077

### assembler-choice: Assembler choice
needs: assembly-fragmentation, targeted-reconstruction
- **assembler-choice.1** Assembler choice is directly measured on identical inputs: CAMI II gives per-assembler 16S completeness, Yuan et al. per-assembler counts of correctly recovered genes, and MATAM per-tool genome fraction and chimera rate; short-read 16S completeness clusters around 30–37% against 47–60% for hybrids.
  conf: not stated · class: not stated · holds: identical inputs within each benchmark (CAMI II, Yuan et al., Pericard et al.) · src: meyerCriticalAssessmentMetagenome2022, yuanReconstructing16SRRNA2015, pericardMATAMReconstructionPhylogenetic2018 · trail: CB2-RRNA §Verdict, §What is measured about variation, §Verdict on the second · from: CB2-RRNA:A-003, CB2-RRNA:A-009, CB2-RRNA:B-0092, CB2-RRNA:B-0093, CB2-RRNA:B-0094 · rating: "DIRECT EVIDENCE"
- **assembler-choice.2** Vollmers et al. counted rRNA phylotypes per assembler: on the low-diversity kelp biofilm metagenome, metaSPAdes and Ray Meta each recovered 18 sequences, more than any other assembler; on the high-diversity forest soil metagenome, metaSPAdes and IDBA-UD gave the most phylotypes, but the main text does not tabulate per-assembler rRNA counts across both datasets, so only the kelp biofilm figure is a clean number.
  conf: not stated · class: not stated · holds: two metagenomes, kelp biofilm (low diversity) and forest soil (high diversity) · src: vollmersComparingEvaluatingMetagenome2017 · trail: CB2-RRNA §What is measured about variation · from: CB2-RRNA:B-0095, CB2-RRNA:A-009

### sequencing-depth: Sequencing depth and coverage
needs: targeted-reconstruction
- **sequencing-depth.1** Sequencing depth is directly measured, but only as simulated per-genome coverage in targeted-assembly benchmarks, not as library depth in a real assemble-and-bin pipeline counting rRNA in MAGs.
  conf: not stated · class: search (note: "which I could not find anywhere") · holds: Pericard et al.'s 2×–50× series and Philip et al.'s read-pair floor · src: pericardMATAMReconstructionPhylogenetic2018, philipMETASEEDNovelApproach2024 · trail: CB2-RRNA §Verdict, §What is measured about variation, §Verdict on the second · from: CB2-RRNA:A-004, CB2-RRNA:A-010, CB2-RRNA:B-0103 · rating: "DIRECT EVIDENCE, but only in simulation and only for targeted assembly"
- **sequencing-depth.2** Pericard et al. simulated five depths (50×, 20×, 10×, 5× and 2× per genome) over 122 genomes carrying 287 distinct 16S copies: "MATAM recovered from 76% to 85% of the reference sequences for sequencing depths greater than 10x, while EMIRGE recovered less than 55% of the reference sequence, and the GF for other methods is lower than 22%."
  conf: not stated · class: model (note: "simulated five depths") · holds: simulated data, 122 genomes, 287 distinct 16S copies, depths above 10× · src: pericard2017 (verified in extracted text) · trail: CB2-RRNA §What is measured about variation · from: CB2-RRNA:B-0096, CB2-RRNA:B-0097
- **sequencing-depth.3** At a low sequencing depth of 2×, MATAM reached a genome fraction of 33%, while genome fractions ranged between 5% and 10% with all other assemblers.
  conf: not stated · class: model (note: "simulated five depths") · holds: simulated data, 2× per genome · src: pericard2017 (verified in extracted text) · trail: CB2-RRNA §What is measured about variation · from: CB2-RRNA:B-0096, CB2-RRNA:B-0098
- **sequencing-depth.4** Philip et al. report the coverage floor: "we need more than 10 read pairs, and in most cases more then 40, to be able to reconstruct a 16S with some substantial length".
  conf: not stated · class: not stated · holds: METASEED reconstruction · src: philipMETASEEDNovelApproach2024 (single-pass extraction) · trail: CB2-RRNA §What is measured about variation · from: CB2-RRNA:B-0099
- **sequencing-depth.5** No study the reviewer found subsamples a real metagenome to a depth series, runs a standard assemble-and-bin pipeline at each depth, and counts how many MAGs carry a 16S gene; the depth axis is unmeasured for rRNA-in-MAG recovery in real data.
  conf: not stated · class: search (note: "What nobody I found has done") · holds: the literature searched by the review · src: none (a search result) · trail: CB2-RRNA §What is measured about variation · from: CB2-RRNA:B-0100, CB2-RRNA:B-0103
- **sequencing-depth.6** The closest is Haryono et al., who show MAG quality tracking normalised coverage decile by decile, but their quality axis there is the completeness/contamination classification, not rRNA presence.
  conf: not stated · class: not stated · holds: tropical activated sludge · src: haryono2021, haryonoRecoveryHighQuality2022 · trail: CB2-RRNA §What is measured about variation · from: CB2-RRNA:B-0101
- **sequencing-depth.7** Coverage of an organism is not the same variable as depth of a library; the two are only loosely coupled through community evenness.
  conf: not stated · class: not stated · holds: the reviewer's statement; no source cited · src: none (the reviewer's statement; no source cited) · trail: CB2-RRNA §What is measured about variation · from: CB2-RRNA:B-0102

### study-of-origin: Study of origin
needs: catalogue-recovery, assembly-fragmentation
- **study-of-origin.1** No evidence exists, in the literature searched, of rRNA gene recovery measured as a function of which study or sequencing run a dataset came from, holding environment and pipeline constant; the search covered cross-study comparisons of MAG catalogues, batch effects in metagenome assembly, meta-analyses of public metagenomes and recent work on variation in MAG recovery.
  conf: not stated · class: search (note: "I found nothing that measures rRNA gene recovery") · holds: the literature searched by the review · src: none (a search result) · trail: CB2-RRNA §Verdict, §What is measured about variation, §Verdict on the second · from: CB2-RRNA:A-005, CB2-RRNA:A-011, CB2-RRNA:B-0104, CB2-RRNA:B-0105, CB2-RRNA:B-0111 · rating: "NO EVIDENCE FOUND"
- **study-of-origin.2** The catalogue papers pool across hundreds or thousands of source studies (GEM: more than 10,000 metagenomes; SMAG: 3,304; UHGG: thousands) and report a single overall figure; none stratifies it by source study.
  conf: not stated · class: not stated · holds: GEM, SMAG, UHGG · src: nayfachGenomicCatalogEarths2020, maGenomicCatalogueSoil2023, almeidaUnifiedCatalog2042020 · trail: CB2-RRNA §What is measured about variation, §Verdict on the second · from: CB2-RRNA:A-005, CB2-RRNA:A-012, CB2-RRNA:B-0106
- **study-of-origin.3** The closest recent work on systematic variation in MAG recovery, Nebauer et al., measures taxonomic bias (recovery skewed toward smaller, low-GC organisms) and does not measure rRNA genes at all.
  conf: not stated · class: not stated · holds: MAG recovery generally, not rRNA genes · src: nebauerTaxonomyBiasMetagenomeAssembled2026 · trail: CB2-RRNA §What is measured about variation · from: CB2-RRNA:B-0107
- **study-of-origin.4** The Singleton-against-Ye comparison is between two studies but varies technology, plant, depth and pipeline simultaneously, and was not designed to isolate study of origin.
  conf: not stated · class: not stated · holds: two activated sludge studies · src: singletonConnectingStructureFunction2021, ye2020 · trail: CB2-RRNA §What is measured about variation · from: CB2-RRNA:B-0108
- **study-of-origin.5** Because the assembly and binning mechanism depends on community composition, sequence diversity and coverage, all of which differ between studies, it is plausible that recovery varies by study of origin; this is an inference, indirect at best, not a measured finding.
  conf: not stated · class: reading (note: "That is an inference") · holds: inferred from the mechanism; never measured · src: none (the reviewer's inference, made per the brief's instruction) · trail: CB2-RRNA §What is measured about variation · from: CB2-RRNA:B-0109, CB2-RRNA:B-0110 · rating: "INDIRECT"
- **study-of-origin.6** For study of origin the absence is an absence, not weak support.
  conf: not stated · class: search (note: "This is an absence, not weak support") · holds: the literature searched by the review · src: none (a search result) · trail: CB2-RRNA §Verdict, §Verdict on the second · from: CB2-RRNA:A-006, CB2-RRNA:A-013

### recovery-variation: What is measured about variation in recovery
needs: sequencing-technology, assembler-choice, sequencing-depth, study-of-origin
- **recovery-variation.1** Of the four axes of variation in rRNA recovery the brief names (read length / sequencing technology, assembler choice, sequencing depth, study of origin), direct evidence was found for three and none for study of origin; the four have very different evidentiary status.
  conf: not stated · class: not stated · holds: the review's verdict over the literature searched · src: none (the reviewer's synthesis) · trail: CB2-RRNA §Verdict, §What is measured about variation, §Verdict on the second · from: CB2-RRNA:A-001, CB2-RRNA:A-007, CB2-RRNA:B-0082

## Do not say

- **dns.1** "Only 7% of MAGs carry a 16S gene", used as the figure on its own.
  why: the note: the 7% rests on an Opinion article that does not document how it was obtained; "I would not build anything on that number alone" · instead: catalogue-recovery.6, marker-gap.5 · trail: CB2-RRNA §Measured recovery rates · from: CB2-RRNA:B-0030, CB2-RRNA:B-0031, CB2-RRNA:B-0032
- **dns.2** Hiseni et al.'s 93% against 99.8% 16S identity used on its own as evidence that MAG 16S sequences are wrong.
  why: the note: the same caveat applies (no documented method) · instead: catalogue-recovery.7 · trail: CB2-RRNA §Measured recovery rates · from: CB2-RRNA:B-0030, CB2-RRNA:B-0034
- **dns.3** "rRNA gene recovery varies by study of origin", stated as a finding.
  why: the note: an inference, indirect at best, not a measured finding; an absence, not weak support, which must not be filled in from the mechanism · instead: study-of-origin.1, study-of-origin.5 · trail: CB2-RRNA §Verdict, §What is measured about variation · from: CB2-RRNA:A-006, CB2-RRNA:A-013, CB2-RRNA:B-0110, CB2-RRNA:B-0111
- **dns.4** Singleton et al.'s 91.3% against Ye et al.'s 1.2% given as the effect of long reads.
  why: the note: the contrast is across two studies and two plants and confounds technology with everything else · instead: sequencing-technology.2, sequencing-technology.3 · trail: CB2-RRNA §Bounding facts · from: CB2-RRNA:B-0069
- **dns.5** Overholt et al. cited as agreeing with Orellana et al. and Singleton et al. on the long-read effect.
  why: the note: worth stating as disagreement in magnitude, not as agreement · instead: sequencing-technology.9 · trail: CB2-RRNA §What is measured about variation · from: CB2-RRNA:B-0091
- **dns.6** Fan et al.'s adequate 16S recovery generalised to Illumina-length reads in a complex environment.
  why: the note: read length there was about 350 nt and the community low-complexity; "I would not generalise it", and no later work found does · instead: targeted-reconstruction.6 · trail: CB2-RRNA §Bounding facts · from: CB2-RRNA:B-0079
- **dns.7** The assembly-graph mechanism (Vollmers et al.; Gruber-Vodicka et al.) cited as a measurement.
  why: the note: neither statement is itself a measurement · instead: assembly-fragmentation.4, assembly-fragmentation.5 · trail: CB2-RRNA §The mechanism · from: CB2-RRNA:B-0049
- **dns.8** Simulated per-genome coverage results cited as the effect of library sequencing depth on rRNA in MAGs.
  why: the note: coverage of an organism is not the same variable as depth of a library; the depth axis is unmeasured for rRNA-in-MAG recovery in real data · instead: sequencing-depth.1, sequencing-depth.7 · trail: CB2-RRNA §What is measured about variation · from: CB2-RRNA:B-0102, CB2-RRNA:B-0103
- **dns.9** A MAG scored 90–95% complete on single-copy markers taken to carry its 16S gene.
  why: the note: the completeness statistic and the rRNA statistic are not measuring the same thing · instead: marker-gap.5 · trail: CB2-RRNA §Side by side · from: CB2-RRNA:B-0043, CB2-RRNA:B-0044
- **dns.10** Vollmers et al.'s forest-soil result given as per-assembler rRNA counts.
  why: the note: the main text does not tabulate per-assembler counts across both datasets; only the kelp biofilm figure is a clean number · instead: assembler-choice.2 · trail: CB2-RRNA §What is measured about variation · from: CB2-RRNA:B-0095
- **dns.11** Haryono et al.'s coverage-decile trend cited as rRNA presence against depth.
  why: the note: their quality axis there is the completeness/contamination classification, not rRNA presence · instead: sequencing-depth.6 · trail: CB2-RRNA §What is measured about variation · from: CB2-RRNA:B-0101
- **dns.12** Nebauer et al. cited as measuring variation in rRNA gene recovery.
  why: the note: it measures taxonomic bias and does not measure rRNA genes at all · instead: study-of-origin.3 · trail: CB2-RRNA §What is measured about variation · from: CB2-RRNA:B-0107
- **dns.13** METASEED's "1 of 253" given as an established rate for conventional assembly.
  why: the note: one paper and one lab, no independent replication found; the reviewer calls its support thin · instead: assembly-fragmentation.7, assembly-fragmentation.9 · trail: CB2-RRNA §The mechanism · from: CB2-RRNA:B-0060

## Gaps

- **gap.1** No figure in this note was checked by a second reader. The answers rest on: Orellana et al.'s 88% against 23%; CAMI II's 29.6–36.9% short-read against 47.1–60.1% hybrid 16S completeness; Overholt et al.'s 16 against 10 MAGs (not significant) and the ONT-only "3×"; Pericard et al.'s 76–85% above 10× and 33% at 2×; Philip et al.'s 10 to 40 read-pair floor. The note says to treat the numbers as unconfirmed until spot-checked against the primary text, and no claim-level verification was performed.
  blocks: sequencing-technology, assembler-choice, sequencing-depth, recovery-variation · origin: no critique; the note's own warning and verification log · trail: CB2-RRNA §No adversarial, §Verification log · from: CB2-RRNA:B-0016, CB2-RRNA:B-0017, CB2-RRNA:B-0018, CB2-RRNA:B-0118, CB2-RRNA:B-0119
- **gap.2** Numbers marked "single-pass extraction" (METASEED's figures, MarkerMAG's figures, Philip et al.'s read-pair floor) carry the risk the note found in an automated read of the Overholt PDF, which returned a table that does not exist in the document; they need checking against the extracted text.
  blocks: assembly-fragmentation.7, assembly-fragmentation.8, targeted-reconstruction.5, linking-tools.1, sequencing-depth.4 · origin: the note's own caution about automated extraction · trail: CB2-RRNA §Recovery of rRNA · from: CB2-RRNA:B-0006, CB2-RRNA:B-0007, CB2-RRNA:B-0008, CB2-RRNA:B-0077
- **gap.3** rRNA gene recovery as a function of the study or sequencing run a dataset came from, holding environment and pipeline constant.
  blocks: study-of-origin · origin: not found; the review searched for it specifically · trail: CB2-RRNA §What is measured about variation · from: CB2-RRNA:B-0105, CB2-RRNA:A-005
- **gap.4** A real metagenome subsampled to a depth series, run through a standard assemble-and-bin pipeline at each depth, counting MAGs that carry a 16S gene.
  blocks: sequencing-depth · origin: not found by the review · trail: CB2-RRNA §What is measured about variation · from: CB2-RRNA:B-0100, CB2-RRNA:B-0103
- **gap.5** The fraction of missing 16S genes that were assembled but binned elsewhere, against never assembled.
  blocks: binning-loss · origin: the note: "That is a real gap" · trail: CB2-RRNA §The mechanism · from: CB2-RRNA:B-0065, CB2-RRNA:B-0066
- **gap.6** An independent replication of METASEED's "1 of 253" result.
  blocks: assembly-fragmentation.7 · origin: not found by the review · trail: CB2-RRNA §The mechanism · from: CB2-RRNA:B-0060 · src: philipMETASEEDNovelApproach2024
- **gap.7** The method behind Hiseni et al.'s 7% figure and 16S identity result (barrnap threshold, source catalogues, breakdown).
  blocks: catalogue-recovery.6, catalogue-recovery.7, marker-gap.4 · origin: the source has no methods section · trail: CB2-RRNA §Measured recovery rates · from: CB2-RRNA:B-0030, CB2-RRNA:B-0031 · src: hiseniQuestioningQuality16S2022
- **gap.8** Ye et al. (2020), the short-read activated sludge catalogue of 2,045 MAGs, was not independently retrieved; its 31% and 1.2% figures are quoted as reported by Singleton et al.
  blocks: sequencing-technology.5 · origin: source not obtained (the note's reference list) · trail: CB2-RRNA §References · src: ye2020
- **gap.9** Recovery of near-full-length 16S from longer reads in complex communities: Fan et al.'s result is from 454 reads of a low-complexity sponge metagenome, and no later work the reviewer found generalises it.
  blocks: targeted-reconstruction.6 · origin: not found by the review · trail: CB2-RRNA §Bounding facts · from: CB2-RRNA:B-0079 · src: fanReconstructionRibosomalRNA2012
- **gap.10** Per-assembler rRNA counts for Vollmers et al.'s high-diversity forest soil metagenome, which the main text does not tabulate.
  blocks: assembler-choice.2 · origin: source does not report it in its main text · trail: CB2-RRNA §What is measured about variation · from: CB2-RRNA:B-0095 · src: vollmersComparingEvaluatingMetagenome2017

## Out of scope

## Sources

```bibtex
@article{almeidaUnifiedCatalog2042020,
  author = {Almeida, A. and Nayfach, S. and Boland, M. and Strozzi, F. and Beracochea, M. and Shi, Z.J. and Pollard, K.S. and Sakharova, E. and Parks, D.H. and Hugenholtz, P. and Segata, N. and Kyrpides, N.C. and Finn, R.D.},
  title = {A unified catalog of 204,938 reference genomes from the human gut microbiome},
  journal = {Nature Biotechnology},
  volume = {39},
  number = {1},
  pages = {105--114},
  year = {2021},
  doi = {10.1038/s41587-020-0603-3},
  note = {access: full_text (targeted verbatim quotations via automated fetch; "not end-to-end human-equivalent reads"); cited as: CB2-RRNA Almeida et al. (UHGG); key kept from Refs.bib}
}
@article{fanReconstructionRibosomalRNA2012,
  author = {Fan, L. and McElroy, K. and Thomas, T.},
  title = {Reconstruction of ribosomal RNA genes from metagenomic data},
  journal = {PLoS ONE},
  volume = {7},
  number = {6},
  pages = {e39948},
  year = {2012},
  doi = {10.1371/journal.pone.0039948},
  note = {access: full_text (targeted verbatim quotations via automated fetch); cited as: CB2-RRNA Fan et al.}
}
@article{grubervodickaPhyloFlashRapidSmallsubunit2020,
  author = {Gruber-Vodicka, H.R. and Seah, B.K.B. and Pruesse, E.},
  title = {phyloFlash: rapid small-subunit rRNA profiling and targeted assembly from metagenomes},
  journal = {mSystems},
  volume = {5},
  number = {5},
  pages = {e00920-20},
  year = {2020},
  doi = {10.1128/mSystems.00920-20},
  note = {access: full_text (targeted verbatim quotations via automated fetch); cited as: CB2-RRNA Gruber-Vodicka et al. (phyloFlash)}
}
@article{haryonoRecoveryHighQuality2022,
  author = {Haryono, M.A.S. and Law, Y.Y. and Arumugam, K. and Liew, L.C.-W. and Nguyen, T.Q.N. and Drautz-Moses, D.I. and Schuster, S.C. and Wuertz, S. and Williams, R.B.H.},
  title = {Recovery of high quality metagenome-assembled genomes from full-scale activated sludge microbial communities in a tropical climate using longitudinal metagenome sampling},
  journal = {Frontiers in Microbiology},
  volume = {13},
  pages = {869135},
  year = {2022},
  doi = {10.3389/fmicb.2022.869135},
  note = {access: not stated (the note read the preprint in full); cited as: CB2-RRNA Haryono et al. 2022, first of two works}
}
@misc{haryono2021,
  author = {Haryono, M.A.S. and others},
  year = {2021},
  doi = {10.1101/2021.08.21.456929},
  howpublished = {bioRxiv 2021.08.21.456929},
  note = {access: full_text ("Preprint read in full"; extracted with pdftotext); type: preprint of Haryono et al. 2022; cited as: CB2-RRNA Haryono et al. 2022, second of two works; incomplete: title, author}
}
@article{hiseniHumGutComprehensiveHuman2021,
  author = {Hiseni, P. and Rudi, K. and Wilson, R.C. and Hegge, F.T. and Snipen, L.},
  title = {HumGut: a comprehensive human gut prokaryotic genomes collection filtered by metagenome data},
  journal = {Microbiome},
  volume = {9},
  number = {1},
  pages = {165},
  year = {2021},
  doi = {10.1186/s40168-021-01114-w},
  note = {access: not stated; not cited (listed; HumGut named only as the authors' own collection in Hiseni et al. 2022); cited as: CB2-RRNA References}
}
@article{hiseniQuestioningQuality16S2022,
  author = {Hiseni, P. and Snipen, L. and Wilson, R.C. and Furu, K. and Rudi, K.},
  title = {Questioning the quality of 16S rRNA gene sequences derived from human gut metagenome-assembled genomes},
  journal = {Frontiers in Microbiology},
  volume = {12},
  pages = {822301},
  year = {2022},
  doi = {10.3389/fmicb.2021.822301},
  note = {access: full_text (targeted verbatim quotations via automated fetch); type: Opinion article (no methods section); cited as: CB2-RRNA Hiseni et al. 2022}
}
@article{maGenomicCatalogueSoil2023,
  author = {Ma, B. and Lu, C. and Wang, Y. and Yu, J. and Zhao, K. and Xue, R. and Ren, H. and Lv, X. and Pan, R. and Zhang, J. and Zhu, Y. and Xu, J.},
  title = {A genomic catalogue of soil microbiomes boosts mining of biodiversity and genetic resources},
  journal = {Nature Communications},
  volume = {14},
  number = {1},
  pages = {7318},
  year = {2023},
  doi = {10.1038/s41467-023-43000-z},
  note = {access: full_text (targeted verbatim quotations via automated fetch); cited as: CB2-RRNA Ma et al. (SMAG)}
}
@article{meyerCriticalAssessmentMetagenome2022,
  author = {Meyer, F. and Fritz, A. and Deng, Z.-L. and Koslicki, D. and Lesker, T.R. and Gurevich, A. and Robertson, G. and Alser, M. and Antipov, D. and Beghini, F. and others},
  title = {Critical Assessment of Metagenome Interpretation: the second round of challenges},
  journal = {Nature Methods},
  volume = {19},
  number = {4},
  pages = {429--440},
  year = {2022},
  doi = {10.1038/s41592-022-01431-4},
  note = {access: full_text (targeted verbatim quotations via automated fetch); cited as: CB2-RRNA Meyer et al. (CAMI II); 127 authors, list abbreviated in the note after the first ten; incomplete: author}
}
@article{nayfachGenomicCatalogEarths2020,
  author = {Nayfach, S. and Roux, S. and Seshadri, R. and Udwary, D. and Varghese, N. and Schulz, F. and Wu, D. and Paez-Espino, D. and Chen, I.-M. and Huntemann, M. and Palaniappan, K. and Ladau, J. and Mukherjee, S. and Reddy, T.B.K. and Nielsen, T. and Kirton, E. and Faria, J.P. and Edirisinghe, J.N. and Henry, C.S. and Jungbluth, S.P. and Chivian, D. and Dehal, P. and Wood-Charlson, E.M. and Arkin, A.P. and Tringe, S.G. and Visel, A. and {IMG/M Data Consortium} and Woyke, T. and Mouncey, N.J. and Ivanova, N.N. and Kyrpides, N.C. and Eloe-Fadrosh, E.A.},
  title = {A genomic catalog of Earth's microbiomes},
  journal = {Nature Biotechnology},
  volume = {39},
  number = {4},
  pages = {499--509},
  year = {2021},
  doi = {10.1038/s41587-020-0718-6},
  note = {access: full_text (targeted verbatim quotations via automated fetch); cited as: CB2-RRNA Nayfach et al. (GEM); key kept from Refs.bib}
}
@article{nebauerTaxonomyBiasMetagenomeAssembled2026,
  author = {Nebauer, D.J. and Nelson, T. and Romanis, C. and Neilan, B.A. and Timms, V.J.},
  title = {Taxonomy bias in metagenome-assembled genome recovery},
  journal = {Microbial Genomics},
  volume = {12},
  number = {6},
  pages = {001736},
  year = {2026},
  doi = {10.1099/mgen.0.001736},
  note = {access: not stated; cited as: CB2-RRNA Nebauer et al.}
}
@article{orellanaComparingGenomesRecovered2023,
  author = {Orellana, L.H. and Kr{\"u}ger, K. and Sidhu, C. and Amann, R.},
  title = {Comparing genomes recovered from time-series metagenomes using long- and short-read sequencing technologies},
  journal = {Microbiome},
  volume = {11},
  pages = {105},
  year = {2023},
  doi = {10.1186/s40168-023-01557-3},
  note = {access: full_text (targeted verbatim quotations via automated fetch); cited as: CB2-RRNA Orellana et al.}
}
@article{overholtInclusionOxfordNanopore2020,
  author = {Overholt, W.A. and H{\"o}lzer, M. and Geesink, P. and Diezel, C. and Marz, M. and K{\"u}sel, K.},
  title = {Inclusion of Oxford Nanopore long reads improves all microbial and viral metagenome-assembled genomes from a complex aquifer system},
  journal = {Environmental Microbiology},
  volume = {22},
  number = {9},
  pages = {4000--4013},
  year = {2020},
  doi = {10.1111/1462-2920.15186},
  note = {access: abstract_only (the ONT-only result is quoted from "the abstract" of the published version; the preprint was read in full); cited as: CB2-RRNA Overholt et al., first of two works}
}
@misc{overholt2019,
  author = {Overholt, W.A. and others},
  year = {2019},
  doi = {10.1101/2019.12.18.880807},
  howpublished = {bioRxiv 2019.12.18.880807},
  note = {access: full_text ("Preprint read in full"; extracted with pdftotext; "the preprint lacks the ONT-only assembly present in the published version"); type: preprint of Overholt et al. 2020; cited as: CB2-RRNA Overholt et al., second of two works; incomplete: title, author}
}
@article{pericardMATAMReconstructionPhylogenetic2018,
  author = {Pericard, P. and Dufresne, Y. and Couderc, L. and Blanquart, S. and Touzet, H.},
  title = {MATAM: reconstruction of phylogenetic marker genes from short sequencing reads in metagenomes},
  journal = {Bioinformatics},
  volume = {34},
  number = {4},
  pages = {585--591},
  year = {2018},
  doi = {10.1093/bioinformatics/btx644},
  note = {access: not stated (the note read the preprint in full); cited as: CB2-RRNA Pericard et al. (MATAM), first of two works}
}
@misc{pericard2017,
  author = {Pericard, P. and others},
  year = {2017},
  doi = {10.1101/141176},
  howpublished = {bioRxiv 141176},
  note = {access: full_text ("Preprint read in full"; extracted with pdftotext); type: preprint of Pericard et al. 2018; cited as: CB2-RRNA Pericard et al. (MATAM), second of two works; incomplete: title, author, year}
}
@article{philipMETASEEDNovelApproach2024,
  author = {Philip, M. and Rudi, K. and Ormaasen, I. and Angell, I.L. and Pettersen, R. and Keeley, N.B. and Snipen, L.-G.},
  title = {METASEED: a novel approach to full-length 16S rRNA gene reconstruction from short read data},
  journal = {BMC Bioinformatics},
  volume = {25},
  number = {1},
  pages = {237},
  year = {2024},
  doi = {10.1186/s12859-024-05837-z},
  note = {access: full_text (single-pass extraction of the PMC text); cited as: CB2-RRNA Philip et al. (METASEED)}
}
@article{singletonConnectingStructureFunction2021,
  author = {Singleton, C.M. and Petriglieri, F. and Kristensen, J.M. and Kirkegaard, R.H. and Michaelsen, T.Y. and Andersen, M.H. and Kondrotaite, Z. and Karst, S.M. and Dueholm, M.S. and Nielsen, P.H. and Albertsen, M.},
  title = {Connecting structure to function with the recovery of over 1000 high-quality metagenome-assembled genomes from activated sludge using long-read sequencing},
  journal = {Nature Communications},
  volume = {12},
  pages = {2009},
  year = {2021},
  doi = {10.1038/s41467-021-22203-2},
  note = {access: full_text (targeted verbatim quotations via automated fetch); cited as: CB2-RRNA Singleton et al.}
}
@article{songMarkerMAGLinkingMetagenomeassembled2022,
  author = {Song, W. and Zhang, S. and Thomas, T.},
  title = {MarkerMAG: linking metagenome-assembled genomes (MAGs) with 16S rRNA marker genes using paired-end short reads},
  journal = {Bioinformatics},
  volume = {38},
  number = {15},
  pages = {3684--3688},
  year = {2022},
  doi = {10.1093/bioinformatics/btac398},
  note = {access: full_text (single-pass extraction of the article HTML); cited as: CB2-RRNA Song et al. (MarkerMAG)}
}
@article{vetrovskyVariability16SRRNA2013,
  author = {V{\v{e}}trovsk{\'y}, T. and Baldrian, P.},
  title = {The variability of the 16S rRNA gene in bacterial genomes and its consequences for bacterial community analyses},
  journal = {PLoS ONE},
  volume = {8},
  number = {2},
  pages = {e57923},
  year = {2013},
  doi = {10.1371/journal.pone.0057923},
  note = {access: full_text (targeted verbatim quotations via automated fetch); cited as: CB2-RRNA Větrovský & Baldrian}
}
@article{vollmersComparingEvaluatingMetagenome2017,
  author = {Vollmers, J. and Wiegand, S. and Kaster, A.-K.},
  title = {Comparing and evaluating metagenome assembly tools from a microbiologist's perspective — not only size matters!},
  journal = {PLoS ONE},
  volume = {12},
  number = {1},
  pages = {e0169662},
  year = {2017},
  doi = {10.1371/journal.pone.0169662},
  note = {access: full_text (targeted verbatim quotations via automated fetch); cited as: CB2-RRNA Vollmers et al.}
}
@article{yuanReconstructing16SRRNA2015,
  author = {Yuan, C. and Lei, J. and Cole, J. and Sun, Y.},
  title = {Reconstructing 16S rRNA genes in metagenomic data},
  journal = {Bioinformatics},
  volume = {31},
  number = {12},
  pages = {i35--i43},
  year = {2015},
  doi = {10.1093/bioinformatics/btv231},
  note = {access: full_text (targeted verbatim quotations via automated fetch); cited as: CB2-RRNA Yuan et al. (REAGO)}
}
@misc{bowers2017,
  author = {Bowers and others},
  year = {2017},
  note = {access: secondary ("as applied in the sources below"); cited as: CB2-RRNA [Bowers et al. 2017] in text, with no entry in the reference list; incomplete: title, author, journal, doi}
}
@misc{ye2020,
  author = {Ye and others},
  year = {2020},
  note = {access: not_obtained ("Cited within Singleton et al. 2021 but not independently retrieved"); the short-read activated sludge catalogue of 2,045 MAGs; cited as: CB2-RRNA Ye et al. (2020), no entry in the reference list; incomplete: title, author, journal, doi}
}
@article{janda16SRRNAGene2007,
  author = {Janda, J. Michael and Abbott, Sharon L.},
  title = {16S rRNA Gene Sequencing for Bacterial Identification in the Diagnostic Laboratory: Pluses, Perils, and Pitfalls},
  journal = {Journal of Clinical Microbiology},
  volume = {45},
  number = {9},
  pages = {2761--2764},
  year = {2007},
  doi = {10.1128/JCM.01228-07},
  note = {background; checked on Crossref and PMC (PMC2045242) 2026-10-21}
}
```
