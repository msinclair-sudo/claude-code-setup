---
type: knowledge
title: Recovery of rRNA genes from metagenome assemblies and MAGs
inputs:
  - CB2-RRNA: PhD/Proposal/Research/Results/Recovery of rRNA Genes from Metagenome Assemblies and MAGs.md
refs: PhD/Proposal/Refs/Refs.bib
built: 2026-10-23
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
| CB2-RRNA | [[Recovery of rRNA Genes from Metagenome Assemblies and MAGs]] | no (the note says none ran) | narrative author-year | no | no | fallback (answers and critique; the note has no labelled citations) |

## Concepts

### marker-completeness: Genome completeness and contamination from marker genes
needs: none

- **marker-completeness.bg1** The completeness and contamination of draft genomes, metagenome-derived ones included, are estimated from sets of marker genes; CheckM uses marker genes specific to the genome's position in a reference genome tree, with information about the collocation of these genes.
  kind: background · ref: parksCheckMAssessingQuality2015 · check: DOI 10.1101/gr.186072.114 resolves on Crossref; stated in the abstract (read through Europe PMC)

### binning: Metagenome binning
needs: none

- **binning.bg1** Metagenome binning groups large genomic fragments assembled from shotgun metagenomic sequences into genome bins; MetaBAT, for example, does so using genome abundance and tetranucleotide frequency.
  kind: background · ref: kangMetaBATEfficientTool2015 · check: DOI 10.7717/peerj.1165 resolves on Crossref; stated in the abstract (read through Europe PMC)

### mimag-hq: The MIMAG high-quality bar and its rRNA requirement
needs: marker-completeness

- **mimag-hq.1** The MIMAG high-quality bar requires 5S, 16S and 23S rRNA plus ≥18 tRNAs on top of ≥90% completeness and ≤5% contamination.
  conf: not stated · class: not stated · holds: the MIMAG standard as applied in the catalogue papers · src: bowers2017 · trail: CB2-RRNA §Measured recovery rates · from: CB2-RRNA:B-0019
- **mimag-hq.2** That composite makes the rRNA requirement the binding constraint on the high-quality bar, and several papers say so directly.
  conf: not stated · class: not stated · holds: the MIMAG high-quality bar · src: none (the reviewer's synthesis) · trail: CB2-RRNA §Measured recovery rates · from: CB2-RRNA:B-0019..0020

### catalogue-recovery: rRNA recovery in published MAG catalogues
needs: mimag-hq, binning

- **catalogue-recovery.1** In the GEM catalogue (all biomes, >10,000 metagenomes), 9,143 of 52,515 MAGs (17.4%) were high quality, carrying the full rRNA set.
  conf: not stated · class: not stated · rating: "The most reliable figures" · holds: GEM, all biomes, >10,000 metagenomes · src: nayfachGenomicCatalogEarths2020 · trail: CB2-RRNA §Measured recovery rates · from: CB2-RRNA:B-0019, CB2-RRNA:B-0021..0022
- **catalogue-recovery.2** In the SMAG soil catalogue (3,304 metagenomes), 3,641 of 40,039 MAGs (9.1%) were high quality, carrying the full rRNA set.
  conf: not stated · class: not stated · rating: "The most reliable figures" · holds: soil, SMAG, 3,304 metagenomes · src: maGenomicCatalogueSoil2023 · trail: CB2-RRNA §Measured recovery rates · from: CB2-RRNA:B-0019, CB2-RRNA:B-0021, CB2-RRNA:B-0023
- **catalogue-recovery.3** In the UHGG human gut catalogue, 573 of 4,644 species representatives carried the full rRNA set, and of those only 38 are MAGs (535 are isolates).
  conf: not stated · class: not stated · rating: "The most reliable figures" · holds: human gut, UHGG species representatives · src: almeidaUnifiedCatalog2042020 · trail: CB2-RRNA §Measured recovery rates · from: CB2-RRNA:B-0019, CB2-RRNA:B-0021, CB2-RRNA:B-0024
- **catalogue-recovery.4** In tropical activated sludge, 142 of 9,079 bins (1.6% of all bins) carried 5S+16S+23S, and 58 met the full MIMAG standard.
  conf: not stated · class: not stated · rating: "The most reliable figures" · holds: tropical activated sludge (engineered), Haryono et al. · src: haryonoRecoveryHighQuality2022 · trail: CB2-RRNA §Measured recovery rates · from: CB2-RRNA:B-0019, CB2-RRNA:B-0021, CB2-RRNA:B-0025
- **catalogue-recovery.5** The GEM catalogue's MAGs have a mean completeness of 83% with mean contamination of 1.3%.
  conf: not stated · class: not stated · holds: GEM (Nayfach catalogue) · src: nayfachGenomicCatalogEarths2020 · trail: CB2-RRNA §Measured recovery rates · from: CB2-RRNA:B-0028
- **catalogue-recovery.6** Nayfach et al. name "problems assembling the 16S rRNA locus" as one reason the MAGs of new species came out less complete than those of known species.
  conf: not stated · class: not stated · holds: GEM (Nayfach catalogue) · src: nayfachGenomicCatalogEarths2020 · trail: CB2-RRNA §Measured recovery rates · from: CB2-RRNA:B-0028
- **catalogue-recovery.7** Hiseni et al. (2022) report that only 7% of >270,000 MAGs yield a 16S sequence under a barrnap search, against 93% of >106,000 RefSeq genomes. It is the most-quoted single number in this literature, but it is published in an Opinion article with no methods section (no barrnap length threshold, no statement of which source catalogues the MAGs came from beyond the authors' own HumGut collection, no breakdown); its direction agrees with every catalogue above, and the review would not build anything on the 7% figure alone.
  conf: not stated · class: not stated · rating: "Treat this one carefully" · holds: a barrnap search; MAGs from the authors' own HumGut collection and sources the article does not state · src: hiseniQuestioningQuality16S2022 (Opinion article; no methods section) · trail: CB2-RRNA §Measured recovery rates · from: CB2-RRNA:B-0029..0032
- **catalogue-recovery.8** Hiseni et al. also report that 97.5%-ANI clusters made only of MAGs share on average 93% 16S identity, while clusters of complete RefSeq genomes share 99.8%, an anomaly for a gene that conserved, and they argue that the 16S sequences MAGs do carry are often wrong; the same caveat applies (an Opinion article with no methods section).
  conf: not stated · class: not stated · holds: 97.5%-ANI clusters of MAGs against clusters of complete RefSeq genomes · src: hiseniQuestioningQuality16S2022 (Opinion article; no methods section) · trail: CB2-RRNA §Measured recovery rates · from: CB2-RRNA:B-0030, CB2-RRNA:B-0033..0034
- **catalogue-recovery.9** Gruber-Vodicka et al. state that "most metagenome-assembled genomes (MAGs) do not contain even fragments of the SSU rRNA gene, not to mention the full gene."
  conf: not stated · class: assert (note: "state the limit flatly") · holds: MAGs in general, as a review and tool paper states it · src: grubervodickaPhyloFlashRapidSmallsubunit2020 · trail: CB2-RRNA §Bounding facts · from: CB2-RRNA:B-0080
- **catalogue-recovery.10** Ma et al. state that "near full-complement rRNA genes sequences are challenging for assembling from metagenomes, especially for near-complete MAGs."
  conf: not stated · class: assert (note: "state the limit flatly") · holds: as Ma et al. state it · src: maGenomicCatalogueSoil2023 · trail: CB2-RRNA §Bounding facts · from: CB2-RRNA:B-0080..0081

### rrna-vs-markers: rRNA recovery against single-copy marker completeness
needs: marker-completeness, mimag-hq

- **rrna-vs-markers.1** In the SMAG soil catalogue, 3,641 MAGs were high quality with rRNA, and a further 5,184 MAGs reached ≥90% completeness and <5% contamination but failed on "the absence of all rRNA genes or less than 18 tRNAs"; so of 8,825 soil MAGs that the single-copy marker estimate calls near-complete, roughly 41% carry the rRNA complement.
  conf: not stated · class: not stated · holds: soil, SMAG · src: maGenomicCatalogueSoil2023 · trail: CB2-RRNA §Side by side · from: CB2-RRNA:B-0036..0037
- **rrna-vs-markers.2** In activated sludge, of 9,079 bins, 1,085 (11.9%) were "putative high quality" on single-copy marker statistics; of those, 142 (13.1%) "contained at least one copy of the 5S, 16S and 23S SSU-rRNA genes"; and applying the stringent MIMAG criteria left "only 58 HQ-MAGs". As the abstract puts it, around 1,000 MAGs looked high quality by marker genes and 58 formally were.
  conf: not stated · class: not stated · holds: activated sludge, Haryono et al. · src: haryonoRecoveryHighQuality2022 (verified in extracted text) · trail: CB2-RRNA §Side by side · from: CB2-RRNA:B-0038..0039
- **rrna-vs-markers.3** In UHGG, 3,207 of 4,644 species representatives were >90% complete and <5% contaminated; 573 additionally had 5S/16S/23S plus ≥18 tRNAs, and only 38 of those 573 were MAGs.
  conf: not stated · class: not stated · holds: human gut, UHGG species representatives · src: almeidaUnifiedCatalog2042020 · trail: CB2-RRNA §Side by side · from: CB2-RRNA:B-0040
- **rrna-vs-markers.4** The UHGG paper attributes the shortfall of MAGs with rRNA to the rRNA operon being "a problematic region to assemble from short-read metagenomic datasets".
  conf: not stated · class: not stated · holds: human gut, UHGG · src: almeidaUnifiedCatalog2042020 · trail: CB2-RRNA §Side by side · from: CB2-RRNA:B-0040..0041
- **rrna-vs-markers.5** In Hiseni et al.'s analysis all the MAGs were >95% complete with <5% contamination on the conventional single-copy marker criterion, and 7% had a detectable 16S.
  conf: not stated · class: not stated · holds: human gut; an Opinion article with no methods section · src: hiseniQuestioningQuality16S2022 (Opinion article; no methods section) · trail: CB2-RRNA §Side by side, §Measured recovery rates · from: CB2-RRNA:B-0042, CB2-RRNA:B-0030
- **rrna-vs-markers.6** A genome can be scored 90–95% complete on conserved single-copy protein-coding genes and still have no assembled, correctly binned 16S; the pattern is consistent across four environments and four pipelines.
  conf: repl (note: "The pattern is consistent across four environments and four pipelines") · class: not stated · holds: the papers that report both numbers on the same genome set: soil (SMAG), activated sludge (Haryono et al.), human gut (UHGG) and human gut (Hiseni et al.) · src: maGenomicCatalogueSoil2023, haryonoRecoveryHighQuality2022, almeidaUnifiedCatalog2042020, hiseniQuestioningQuality16S2022 (Opinion article; no methods section) · trail: CB2-RRNA §Side by side · from: CB2-RRNA:B-0035..0036, CB2-RRNA:B-0038, CB2-RRNA:B-0040, CB2-RRNA:B-0042..0043
- **rrna-vs-markers.7** The completeness statistic and the rRNA statistic are not measuring the same thing, and the gap between them is large: typically a factor of two to ten depending on the catalogue.
  conf: not stated · class: not stated · holds: the catalogues the review compared · src: none (the reviewer's synthesis) · trail: CB2-RRNA §Side by side · from: CB2-RRNA:B-0044

### rrna-copy-number: rRNA gene copies per genome
needs: none

- **rrna-copy-number.1** Větrovský and Baldrian extracted 7,081 16S sequences from 1,690 bacterial genomes: 1–15 copies per genome, mean 4.2, with mean within-genome similarity of 99.70 ± 0.46%.
  conf: not stated · class: meas (note: "extracted 7,081 16S sequences from 1,690 bacterial genomes") · holds: 1,690 bacterial genomes · src: vetrovskyVariability16SRRNA2013 · trail: CB2-RRNA §The mechanism · from: CB2-RRNA:B-0061

### assembly-fragmentation: Why rRNA genes fragment in metagenome assembly
needs: rrna-copy-number

- **assembly-fragmentation.1** Vollmers et al. describe 16S genes as posing "a highly challenging problem for metagenome assemblers" because multiple highly conserved regions interspersed with hypervariable stretches produce "highly complex branched assembly graph structures", splitting the gene into short contigs confined to conserved regions.
  conf: not stated · class: assert (note: "Neither statement is itself a measurement") · holds: an account of the mechanism, not a measurement · src: vollmersComparingEvaluatingMetagenome2017 · trail: CB2-RRNA §The mechanism · from: CB2-RRNA:B-0047, CB2-RRNA:B-0049
- **assembly-fragmentation.2** Gruber-Vodicka et al. give the same account in k-mer terms: conserved regions "lead to sets of shared k-mers among the SSU rRNA sequences present in the read pool that confound the assembly graph structure and eventually cause fragmented assemblies".
  conf: not stated · class: assert (note: "Neither statement is itself a measurement") · holds: an account of the mechanism, not a measurement · src: grubervodickaPhyloFlashRapidSmallsubunit2020 · trail: CB2-RRNA §The mechanism · from: CB2-RRNA:B-0048..0049
- **assembly-fragmentation.3** Near-identical repeats of ~1.5 kb (within an ~5 kb operon) are the classic short-read assembly failure mode.
  conf: not stated · class: not stated · holds: short-read assembly of multiple rRNA copies per genome · src: none (the reviewer's statement) · trail: CB2-RRNA §The mechanism · from: CB2-RRNA:B-0061..0062
- **assembly-fragmentation.4** In CAMI II, for every assembler except the two hybrids, the median length of contigs aligning to a 16S gene was below the average 16S gene length of 1,503 bp: the gene is typically fragmented, not recovered.
  conf: not stated · class: model (note: "same simulated data across submissions") · holds: the CAMI II marine dataset, simulated data, 131 known 16S sequences · src: meyerCriticalAssessmentMetagenome2022 · trail: CB2-RRNA §The mechanism, §What is measured about variation · from: CB2-RRNA:B-0051, CB2-RRNA:B-0053, CB2-RRNA:B-0087
- **assembly-fragmentation.5** In the MATAM benchmark, on a synthetic community of 64 organisms, SPAdes and MEGAHIT run on SortMeRNA-extracted 16S reads recovered genome fractions of 39.9% and 44.3% respectively.
  conf: not stated · class: not stated · holds: a synthetic community of 64 organisms · src: pericardMATAMReconstructionPhylogenetic2018 (verified in extracted text) · trail: CB2-RRNA §The mechanism · from: CB2-RRNA:B-0054..0055
- **assembly-fragmentation.6** Averaged across five simulated depths, SPAdes contigs were 21.2% chimeric and MEGAHIT contigs 23.8%.
  conf: not stated · class: model (note: "five simulated depths") · holds: the MATAM synthetic community of 64 organisms, five simulated depths · src: pericardMATAMReconstructionPhylogenetic2018 (verified in extracted text) · trail: CB2-RRNA §The mechanism · from: CB2-RRNA:B-0054..0056
- **assembly-fragmentation.7** In METASEED, assembling simulated shotgun data conventionally yielded 253 distinct 16S sequences, of which "only 1 gave a >99% match to some of the actual 16S sequences"; the result points the same way as the MATAM chimera rates.
  conf: single (note: "This is one paper and one lab") · class: model (note: "assembling simulated shotgun data") · rating: "would call its support thin" · holds: simulated shotgun data, conventional assembly · src: philipMETASEEDNovelApproach2024 (single-pass extraction of the PMC text) · trail: CB2-RRNA §The mechanism · from: CB2-RRNA:B-0057, CB2-RRNA:B-0060
- **assembly-fragmentation.8** On real seafloor sediment, METASEED's 26,133,575 contigs yielded 150 distinct 16S sequences after clustering, and only 51 matched amplicon OTUs from the same samples at >99%.
  conf: not stated · class: meas (note: "On real seafloor sediment") · holds: seafloor sediment, compared with amplicon OTUs from the same samples · src: philipMETASEEDNovelApproach2024 (single-pass extraction of the PMC text) · trail: CB2-RRNA §The mechanism · from: CB2-RRNA:B-0057..0058
- **assembly-fragmentation.9** The METASEED authors' framing is that conventional assembly produces mosaic sequences.
  conf: not stated · class: not stated · holds: the METASEED authors' framing · src: philipMETASEEDNovelApproach2024 · trail: CB2-RRNA §The mechanism · from: CB2-RRNA:B-0057, CB2-RRNA:B-0059
- **assembly-fragmentation.10** The review found no independent replication of the METASEED "1 of 253" result.
  conf: not stated · class: search (note: "I have not found an independent replication") · search: searched, not found (note: "I have not found an independent replication") · holds: the literature the review reached · src: none (a search result of the review) · trail: CB2-RRNA §The mechanism · from: CB2-RRNA:B-0060

### rrna-binning: Why rRNA genes are lost in binning
needs: binning, rrna-copy-number, assembly-fragmentation

- **rrna-binning.1** Three mechanisms are offered: two on the assembly side (conservation collapses the assembly graph; multiple copies per genome, with intragenomic variation) and one on the binning side (copy number defeats coverage-based binning).
  conf: not stated · class: not stated · holds: the mechanisms the review found offered in the literature · src: none (the reviewer's synthesis) · trail: CB2-RRNA §The mechanism · from: CB2-RRNA:B-0045..0047, CB2-RRNA:B-0061, CB2-RRNA:B-0063
- **rrna-binning.2** Song et al. state that multiple 16S copies "result in unusually high read-depth information" for the contig carrying them, which, together with "atypical nucleotide composition, hinders its correct binning with the rest of the genome"; Gruber-Vodicka et al. make the same point.
  conf: not stated · class: not stated · holds: coverage-based binning · src: songMarkerMAGLinkingMetagenomeassembled2022, grubervodickaPhyloFlashRapidSmallsubunit2020 · trail: CB2-RRNA §The mechanism · from: CB2-RRNA:B-0063..0064
- **rrna-binning.3** The review found no paper that isolates and quantifies the binning contribution separately from the assembly contribution: nobody it found measured what fraction of missing 16S genes were assembled but then binned elsewhere, against never assembled at all.
  conf: not stated · class: search (note: "I did not find a paper that isolates and quantifies the binning contribution") · search: searched, not found (note: "I did not find a paper that isolates and quantifies the binning contribution") · holds: the literature the review reached · src: none (a search result of the review) · trail: CB2-RRNA §The mechanism · from: CB2-RRNA:B-0065..0066

### rrna-reconstruction: Targeted reconstruction of rRNA genes, and how well it works
needs: assembly-fragmentation

- **rrna-reconstruction.1** In Yuan et al.'s benchmark of generic against targeted assemblers on a simulated 11-species set, REAGO recovered 11/11 genes with 1 incorrect assembly, EMIRGE 6/11 (genus-excluded database) with 17 incorrect, IDBA-UD 3/11 with 413 incorrect and MetaVelvet 1/11 with 1,257 incorrect.
  conf: not stated · class: model (note: "On a simulated 11-species set") · holds: a simulated 11-species set · src: yuanReconstructing16SRRNA2015 · trail: CB2-RRNA §Bounding facts · from: CB2-RRNA:B-0070..0071
- **rrna-reconstruction.2** On Yuan et al.'s 64-species synthetic community, REAGO recovered 58/64 genes (2 incorrect), IDBA-UD 39/64 (28 incorrect), EMIRGE 19/64 (89 incorrect) and MetaVelvet 4/64 (131 incorrect).
  conf: not stated · class: not stated · holds: a 64-species synthetic community · src: yuanReconstructing16SRRNA2015 · trail: CB2-RRNA §Bounding facts · from: CB2-RRNA:B-0070, CB2-RRNA:B-0072
- **rrna-reconstruction.3** The targeted tools are not clean either: on the MATAM synthetic community, MATAM reached a genome fraction of 83.1% with 3.2% chimeras, EMIRGE 50.7% with 17.4% chimeras and REAGO 42.8% with 15.5% chimeras.
  conf: not stated · class: not stated · holds: the MATAM synthetic community · src: pericardMATAMReconstructionPhylogenetic2018 (verified in extracted text) · trail: CB2-RRNA §Bounding facts · from: CB2-RRNA:B-0073
- **rrna-reconstruction.4** The MATAM authors note that all methods handled genes sharing <90% identity with their nearest neighbour, but that "performances significantly dropped" for paralogous copies around 99% identity, where EMIRGE and REAGO merged reads from distinct paralogs into single erroneous sequences.
  conf: not stated · class: not stated · holds: the MATAM benchmark · src: pericardMATAMReconstructionPhylogenetic2018 · trail: CB2-RRNA §Bounding facts · from: CB2-RRNA:B-0073..0074
- **rrna-reconstruction.5** METASEED reports 1,631 reconstructions with 1,534 matching at >99% (6% false positives), against EMIRGE 1,589/1,118 (30%) and MATAM 992/832 (16%).
  conf: not stated · class: not stated · holds: as reported by the tool's own authors · src: philipMETASEEDNovelApproach2024 (single-pass extraction; from the tool's own authors) · trail: CB2-RRNA §Bounding facts · from: CB2-RRNA:B-0075
- **rrna-reconstruction.6** Fan et al. recovered near-full-length 16S from 454 pyrosequencing of a sponge metagenome with a 3.6% chimera rate before filtering, which they note is below the 5–45% typically reported for PCR amplicons; read length there was ~350 nt and the community was low-complexity relative to soil.
  conf: not stated · class: not stated · holds: 454 pyrosequencing (~350 nt reads) of a sponge metagenome, a community low-complexity relative to soil · src: fanReconstructionRibosomalRNA2012 · trail: CB2-RRNA §Bounding facts · from: CB2-RRNA:B-0078..0079
- **rrna-reconstruction.7** The review would not generalise Fan et al.'s result to Illumina-length reads in a complex environment, and no later work it found does.
  conf: not stated · class: search (note: "no later work I found does") · search: searched, not found (note: "no later work I found does") · holds: Illumina-length reads in a complex environment · src: fanReconstructionRibosomalRNA2012 · trail: CB2-RRNA §Bounding facts · from: CB2-RRNA:B-0078..0079

### linking-tools: Linking 16S genes to MAGs
needs: rrna-binning

- **linking-tools.1** MarkerMAG, on benchmark datasets at 100% linking accuracy, recovered 88.2% (15/17 MAGs) on the low-complexity MBARC-26 dataset, 53.5% (23/43) on the medium-complexity and 46.7% (14/30) on the high-complexity dataset.
  conf: not stated · class: not stated · holds: benchmark datasets of low, medium and high complexity, at 100% linking accuracy · src: songMarkerMAGLinkingMetagenomeassembled2022 (single-pass extraction of the article HTML) · trail: CB2-RRNA §Bounding facts · from: CB2-RRNA:B-0076..0077
- **linking-tools.2** On real data, MarkerMAG's improvement over baseline ranged from 1.1-fold (macroalgae) to 14.2-fold (pig gut).
  conf: not stated · class: not stated · holds: real datasets, macroalgae to pig gut · src: songMarkerMAGLinkingMetagenomeassembled2022 (single-pass extraction of the article HTML) · trail: CB2-RRNA §Bounding facts · from: CB2-RRNA:B-0076..0077
- **linking-tools.3** Linking tools recover part but not most of the gap.
  conf: not stated · class: not stated · holds: the review's reading of the MarkerMAG figures · src: songMarkerMAGLinkingMetagenomeassembled2022 · trail: CB2-RRNA §Bounding facts · from: CB2-RRNA:B-0076

### read-length-effect: Read length and sequencing technology
needs: mimag-hq, assembly-fragmentation

- **read-length-effect.1** In Singleton et al.'s long-read activated sludge study, all 1,083 MAGs in the high-quality set "encode full-length 16S rRNA, 23S rRNA, 5S rRNA, and >18 tRNA genes".
  conf: not stated · class: not stated · holds: activated sludge, long-read · src: singletonConnectingStructureFunction2021 · trail: CB2-RRNA §Bounding facts · from: CB2-RRNA:B-0026, CB2-RRNA:B-0067
- **read-length-effect.2** In Singleton et al., 91.3% (1,045/1,145) of near-complete MAGs carried full-length 16S.
  conf: not stated · class: not stated · holds: activated sludge, long-read, near-complete MAGs · src: singletonConnectingStructureFunction2021 · trail: CB2-RRNA §Measured recovery rates, §Bounding facts · from: CB2-RRNA:B-0026, CB2-RRNA:B-0067
- **read-length-effect.3** Singleton et al. contrast their result with a short-read activated sludge study: of Ye et al.'s MAGs, "31% (644) met the MIMAG HQ completeness and contamination threshold … but only 1.2% (25 MAGs) were of HQ according to the MIMAG standards and encoded the rRNA genes".
  conf: not stated · class: not stated · limit: access (note: "quoted as reported by Singleton et al., not verified against the original") · holds: a short-read activated sludge catalogue of 2,045 MAGs · src: singletonConnectingStructureFunction2021, ye2020 (cited within Singleton et al., not independently retrieved) · trail: CB2-RRNA §Bounding facts, §References · from: CB2-RRNA:B-0067..0068, CB2-RRNA:R-0057..0058
- **read-length-effect.4** The Singleton-versus-Ye contrast is across two different studies and two different plants, so it confounds technology with everything else.
  conf: not stated · class: not stated · holds: two studies of two different activated sludge plants · src: none (the reviewer's reading) · trail: CB2-RRNA §Bounding facts · from: CB2-RRNA:B-0068..0069
- **read-length-effect.5** Orellana et al. sequenced the same North Sea bloom samples with Illumina HiSeq (~240 bp paired-end, ~36 Gbp per sample) and PacBio HiFi (~6 kbp CCS reads, ~12 Gbp per sample): "88% of the total long-read MAGs carried a 16S rRNA gene compared to only 23% of MAGs recovered from short-read metagenomes."
  conf: not stated · class: meas (note: "sequenced the same North Sea bloom samples") · rating: "the cleanest controlled comparison I found on any axis" · holds: North Sea bloom samples (marine time series), 254 long-read against 341 short-read MAGs · src: orellanaComparingGenomesRecovered2023 · trail: CB2-RRNA §What is measured about variation, §Measured recovery rates · from: CB2-RRNA:B-0027, CB2-RRNA:B-0084, CB2-RRNA:B-0086, CB2-RRNA:A-002, CB2-RRNA:A-008
- **read-length-effect.6** In Orellana et al. the short-read libraries were three times deeper and still recovered 16S in a quarter as many MAGs: depth ran against the effect.
  conf: not stated · class: not stated · holds: the same North Sea bloom samples · src: orellanaComparingGenomesRecovered2023 · trail: CB2-RRNA §What is measured about variation · from: CB2-RRNA:B-0084..0085, CB2-RRNA:A-002
- **read-length-effect.7** On the same simulated CAMI II data, the hybrid assemblers reached mean 16S completeness of 60.1% (GATB) and 47.1% (OPERA-MS), against 29.6–36.9% for the short-read assemblers.
  conf: not stated · class: model (note: "same simulated data across submissions") · holds: CAMI II simulated data · src: meyerCriticalAssessmentMetagenome2022 · trail: CB2-RRNA §What is measured about variation · from: CB2-RRNA:B-0087
- **read-length-effect.8** On the CAMI II data the median length of 16S-aligning contigs was 8,513 bp and 4,430 bp for the two hybrid assemblers, against below 1,503 bp for the rest.
  conf: not stated · class: model (note: "same simulated data across submissions") · holds: CAMI II simulated data · src: meyerCriticalAssessmentMetagenome2022 · trail: CB2-RRNA §What is measured about variation · from: CB2-RRNA:B-0087
- **read-length-effect.9** In the Overholt et al. preprint, among 44 MAGs recovered by both the Illumina-only and the hybrid assembly of the same aquifer samples, the hybrid set had 16 MAGs with a 16S gene against 10 for Illumina-only (and 16 vs 15 for 5S, 13 vs 9 for 23S), a difference that was not significant on a two-proportion z-test.
  conf: not stated · class: not stated · holds: aquifer samples; 44 MAGs recovered by both assemblies · src: overholtInclusionOxfordNanopore2020 (verified in extracted text from the preprint) · trail: CB2-RRNA §What is measured about variation · from: CB2-RRNA:B-0088
- **read-length-effect.10** The published version of Overholt et al. adds an ONT-only assembly and reports in its abstract that the ONT-only MAGs had a probability of containing rRNA genes "3× higher than either of the other methods."
  conf: not stated · class: not stated · holds: the ONT-only assembly is in the published version, not the preprint · src: overholtInclusionOxfordNanopore2020 (published version, abstract) · trail: CB2-RRNA §What is measured about variation · from: CB2-RRNA:B-0089, CB2-RRNA:R-0035
- **read-length-effect.11** Within Overholt et al. the hybrid-versus-short-read effect on rRNA was null and the long-read-only effect was large, which is a disagreement in magnitude with Orellana et al. and Singleton et al., not agreement.
  conf: cont (note: "disagreement in magnitude") · class: not stated · holds: hybrid against short-read assembly (Overholt et al.) compared with long-read against short-read (Orellana et al., Singleton et al.) · src: overholtInclusionOxfordNanopore2020, orellanaComparingGenomesRecovered2023, singletonConnectingStructureFunction2021 · trail: CB2-RRNA §What is measured about variation, §Verdict on the second question · from: CB2-RRNA:B-0090..0091, CB2-RRNA:A-008
- **read-length-effect.12** Read length and sequencing technology are directly and repeatedly measured as influences on rRNA recovery, including one controlled same-sample comparison (Orellana et al.: 88% vs 23%) in which depth ran against the effect, and one study (Overholt et al.) where the hybrid-versus-short-read difference in rRNA recovery was not significant.
  conf: not stated · class: not stated · rating: "DIRECT EVIDENCE, and it is good" · holds: the review's assessment of the read-length and technology axis · src: orellanaComparingGenomesRecovered2023, overholtInclusionOxfordNanopore2020 · trail: CB2-RRNA §Verdict, §Verdict on the second question, §What is measured about variation · from: CB2-RRNA:A-002, CB2-RRNA:A-008, CB2-RRNA:B-0083

### assembler-effect: Assembler choice
needs: assembly-fragmentation, rrna-reconstruction

- **assembler-effect.1** CAMI II quantified 16S completeness per assembler against 131 known 16S sequences in the marine dataset: short-read assemblies recovered 16S at mean completeness between 29.6% (HipMer) and 36.9% (MEGAHIT).
  conf: not stated · class: model (note: "same simulated data across submissions") · holds: the CAMI II marine dataset, simulated data, 131 known 16S sequences · src: meyerCriticalAssessmentMetagenome2022 · trail: CB2-RRNA §The mechanism · from: CB2-RRNA:B-0051..0052, CB2-RRNA:B-0087
- **assembler-effect.2** Vollmers et al. counted rRNA phylotypes per assembler: on the low-diversity kelp biofilm (KBF) metagenome, metaSPAdes and Ray Meta each recovered 18 sequences, more than any other assembler, and on the high-diversity forest soil metagenome metaSPAdes and IDBA-UD gave the most phylotypes; their main text does not tabulate per-assembler rRNA counts across both datasets, so only the KBF figure is a clean number.
  conf: not stated · class: not stated · holds: a low-diversity kelp biofilm metagenome and a high-diversity forest soil metagenome · src: vollmersComparingEvaluatingMetagenome2017 · trail: CB2-RRNA §What is measured about variation · from: CB2-RRNA:B-0095
- **assembler-effect.3** Assembler choice is directly measured on identical inputs by CAMI II (per-assembler 16S completeness), Yuan et al. (per-assembler counts of correctly recovered genes), Pericard et al. (per-tool genome fraction and chimera rate) and Vollmers et al., with short-read 16S completeness clustering around 30–37% against 47–60% for hybrids.
  conf: not stated · class: not stated · rating: "DIRECT EVIDENCE" · holds: identical inputs within each benchmark · src: meyerCriticalAssessmentMetagenome2022, yuanReconstructing16SRRNA2015, pericardMATAMReconstructionPhylogenetic2018, vollmersComparingEvaluatingMetagenome2017 · trail: CB2-RRNA §Verdict, §Verdict on the second question, §What is measured about variation · from: CB2-RRNA:A-003, CB2-RRNA:A-009, CB2-RRNA:B-0092..0094

### depth-effect: Sequencing depth
needs: rrna-reconstruction, binning

- **depth-effect.1** Pericard et al. simulated five depths (50×, 20×, 10×, 5×, 2× per genome) over 122 genomes carrying 287 distinct 16S copies: "MATAM recovered from 76% to 85% of the reference sequences for sequencing depths greater than 10x, while EMIRGE recovered less than 55% of the reference sequence, and the GF for other methods is lower than 22%."
  conf: not stated · class: model (note: "Pericard et al. simulated five depths") · holds: simulated per-genome depths of 50× to 2× over 122 genomes; targeted 16S reconstruction · src: pericardMATAMReconstructionPhylogenetic2018 (verified in extracted text) · trail: CB2-RRNA §What is measured about variation · from: CB2-RRNA:B-0096..0097
- **depth-effect.2** At a low sequencing depth of 2×, MATAM reached a genome fraction of 33%, while the genome fractions of all other assemblers ranged between 5% and 10%.
  conf: not stated · class: model (note: "Pericard et al. simulated five depths") · holds: simulated depth of 2× per genome · src: pericardMATAMReconstructionPhylogenetic2018 (verified in extracted text) · trail: CB2-RRNA §What is measured about variation · from: CB2-RRNA:B-0096..0098
- **depth-effect.3** Philip et al. report the coverage floor: "we need more than 10 read pairs, and in most cases more then 40, to be able to reconstruct a 16S with some substantial length".
  conf: not stated · class: not stated · holds: 16S reconstruction from read pairs, as Philip et al. report it · src: philipMETASEEDNovelApproach2024 (single-pass extraction) · trail: CB2-RRNA §What is measured about variation · from: CB2-RRNA:B-0099
- **depth-effect.4** Nobody the review found has subsampled a real metagenome to a depth series, run a standard assemble-and-bin pipeline at each depth, and counted how many MAGs carry a 16S gene.
  conf: not stated · class: search (note: "What nobody I found has done") · search: searched, not found (note: "What nobody I found has done") · holds: real metagenomes, library depth, assemble-and-bin pipelines · src: none (a search result of the review) · trail: CB2-RRNA §What is measured about variation, §Verdict on the second question · from: CB2-RRNA:B-0100, CB2-RRNA:A-010
- **depth-effect.5** Haryono et al. show MAG quality tracking normalised coverage decile by decile, but their quality axis there is the completeness/contamination classification, not rRNA presence.
  conf: not stated · class: not stated · holds: MAG quality as the completeness/contamination classification · src: haryonoRecoveryHighQuality2022 · trail: CB2-RRNA §What is measured about variation · from: CB2-RRNA:B-0101
- **depth-effect.6** Coverage of an organism is not the same variable as depth of a library, and the two are only loosely coupled through community evenness.
  conf: not stated · class: not stated · holds: the review's reasoning · src: none (the reviewer's reasoning) · trail: CB2-RRNA §What is measured about variation · from: CB2-RRNA:B-0102
- **depth-effect.7** Sequencing depth is directly measured only as simulated per-genome coverage in targeted-assembly benchmarks (Pericard et al.'s 2×–50× series; Philip et al.'s read-pair floor), not as library depth in a real assemble-and-bin pipeline counting rRNA in MAGs: the depth axis is measured for targeted 16S reconstruction in simulation and unmeasured for rRNA-in-MAG recovery in real data.
  conf: not stated · class: not stated · rating: "DIRECT EVIDENCE, but only in simulation and only for targeted assembly" · holds: simulated per-genome coverage, targeted 16S reconstruction · src: pericardMATAMReconstructionPhylogenetic2018, philipMETASEEDNovelApproach2024 · trail: CB2-RRNA §Verdict, §Verdict on the second question, §What is measured about variation · from: CB2-RRNA:A-004, CB2-RRNA:A-010, CB2-RRNA:B-0096, CB2-RRNA:B-0103

### study-of-origin: Variation in recovery by study of origin
needs: catalogue-recovery, rrna-binning

- **study-of-origin.1** The review found nothing that measures rRNA gene recovery as a function of which study or sequencing run a dataset came from, holding environment and pipeline constant, and states that no evidence exists in the literature it searched; it calls this an absence, not weak support, which should not be filled in from the mechanism.
  conf: not stated · class: search (note: "I looked for this specifically, from several angles") · search: searched, not found (note: "I looked for this specifically, from several angles") · rating: "NO EVIDENCE FOUND" · holds: searched through cross-study comparisons of MAG catalogues, batch effects in metagenome assembly, meta-analyses of public metagenomes, and recent work on variation in MAG recovery · src: none (a search result of the review) · trail: CB2-RRNA §What is measured about variation, §Verdict, §Verdict on the second question · from: CB2-RRNA:B-0104..0105, CB2-RRNA:A-005..006, CB2-RRNA:A-011, CB2-RRNA:A-013
- **study-of-origin.2** The large catalogues pool across hundreds or thousands of source studies (GEM: >10,000 metagenomes; SMAG: 3,304; UHGG: thousands) and report a single overall figure; none of them stratifies rRNA recovery by source study.
  conf: not stated · class: not stated · holds: GEM, SMAG and UHGG · src: nayfachGenomicCatalogEarths2020, maGenomicCatalogueSoil2023, almeidaUnifiedCatalog2042020 · trail: CB2-RRNA §What is measured about variation, §Verdict on the second question · from: CB2-RRNA:B-0106, CB2-RRNA:A-005, CB2-RRNA:A-012
- **study-of-origin.3** Nebauer et al., the closest recent work on systematic variation in MAG recovery, measure taxonomic bias (recovery skewed toward smaller, low-GC organisms) and do not measure rRNA genes at all.
  conf: not stated · class: not stated · holds: variation in MAG recovery by taxon · src: nebauerTaxonomyBiasMetagenomeAssembled2026 · trail: CB2-RRNA §What is measured about variation · from: CB2-RRNA:B-0107
- **study-of-origin.4** The Singleton-versus-Ye comparison is between two studies, but it varies technology, plant, depth and pipeline simultaneously and was not designed to isolate study of origin.
  conf: not stated · class: not stated · holds: two activated sludge studies · src: singletonConnectingStructureFunction2021, ye2020 (cited within Singleton et al., not independently retrieved) · trail: CB2-RRNA §What is measured about variation · from: CB2-RRNA:B-0108, CB2-RRNA:R-0057
- **study-of-origin.5** Because the mechanism depends on community composition, sequence diversity and coverage, all of which differ between studies, it is plausible that recovery varies by study of origin; this is an inference, indirect at best, and not a measured finding.
  conf: not stated · class: reading (note: "That is an inference") · rating: "INDIRECT at best" · holds: an inference made at the brief's explicit instruction; nobody has measured it · src: none (the reviewer's inference) · trail: CB2-RRNA §What is measured about variation · from: CB2-RRNA:B-0109..0111

### variation-axes: Which axes of variation in recovery are measured
needs: read-length-effect, assembler-effect, depth-effect, study-of-origin

- **variation-axes.1** Of the four axes of variation in rRNA recovery that the brief named, direct evidence was found for three (read length and sequencing technology, assembler choice, sequencing depth); for the fourth, study of origin, no evidence exists.
  conf: not stated · class: not stated · holds: the four axes the brief named · src: none (the review's verdict) · trail: CB2-RRNA §Verdict, §Verdict on the second question · from: CB2-RRNA:A-001..004, CB2-RRNA:A-007, CB2-RRNA:B-0082

## Do not say

- **dns.1** "Recovery of rRNA genes from metagenomes varies with the study a dataset comes from."
  why: No paper stratifies rRNA recovery by originating study; the review calls this an absence, not weak support, that must not be filled in from the mechanism, and says the plausibility of such variation is an inference, indirect at best, that nobody has measured. · instead: study-of-origin.1, study-of-origin.5 · trail: CB2-RRNA §Verdict, §What is measured about variation · from: CB2-RRNA:A-005..006, CB2-RRNA:A-013, CB2-RRNA:B-0109..0111
- **dns.2** "Only 7% of metagenome-assembled genomes carry a 16S rRNA gene."
  why: The 7% figure comes from Hiseni et al. (2022), an Opinion article with no methods section that does not document how the figure was obtained; the review would not build anything on that number alone. · instead: catalogue-recovery.1, catalogue-recovery.2, catalogue-recovery.3, catalogue-recovery.4, catalogue-recovery.7 · trail: CB2-RRNA §Measured recovery rates · from: CB2-RRNA:B-0029..0032
- **dns.3** "The 16S sequences that MAGs carry are often wrong: MAG clusters share only 93% 16S identity."
  why: This argument comes from the same Hiseni et al. Opinion article, which has no methods section, and the review says the same caveat applies. · instead: catalogue-recovery.8 · trail: CB2-RRNA §Measured recovery rates · from: CB2-RRNA:B-0030..0031, CB2-RRNA:B-0033..0034
- **dns.4** "Long-read sequencing raised the share of activated sludge MAGs with rRNA genes from 1.2% (Ye et al.) to 91.3% (Singleton et al.)."
  why: That contrast is across two different studies and two different plants, so it confounds technology with everything else; the review gives the controlled comparison separately. · instead: read-length-effect.4, read-length-effect.5 · trail: CB2-RRNA §Bounding facts · from: CB2-RRNA:B-0067..0069
- **dns.5** "The Singleton and Ye activated sludge studies show that rRNA recovery differs between studies."
  why: The comparison varies technology, plant, depth and pipeline simultaneously and was not designed to isolate study of origin. · instead: study-of-origin.4 · trail: CB2-RRNA §What is measured about variation · from: CB2-RRNA:B-0108
- **dns.6** "Deeper sequencing has been shown to increase the number of MAGs that carry a 16S gene."
  why: Depth is measured only as simulated per-genome coverage in targeted-assembly benchmarks, not as library depth in a real assemble-and-bin pipeline counting rRNA in MAGs; coverage of an organism is not the same variable as depth of a library. · instead: depth-effect.4, depth-effect.7 · trail: CB2-RRNA §What is measured about variation · from: CB2-RRNA:A-004, CB2-RRNA:B-0102..0103
- **dns.7** "Haryono et al. show rRNA recovery rising with coverage."
  why: Haryono et al. show MAG quality tracking normalised coverage, but their quality axis there is the completeness/contamination classification, not rRNA presence. · instead: depth-effect.5 · trail: CB2-RRNA §What is measured about variation · from: CB2-RRNA:B-0101
- **dns.8** "Assembly recovers near-full-length 16S genes from metagenomes adequately, with fewer chimeras than PCR amplicons."
  why: That result (Fan et al.) comes from 454 pyrosequencing with ~350 nt reads of a sponge community low-complexity relative to soil; the review would not generalise it to Illumina-length reads in a complex environment, and no later work it found does. · instead: rrna-reconstruction.6, rrna-reconstruction.7 · trail: CB2-RRNA §Bounding facts · from: CB2-RRNA:B-0078..0079
- **dns.9** "Overholt et al. agree with Orellana et al. and Singleton et al. that adding long reads raises rRNA recovery."
  why: Within Overholt et al. the hybrid-versus-short-read effect on rRNA was null (not significant) and only the long-read-only effect was large; the review says this should be stated as disagreement in magnitude, not as agreement. · instead: read-length-effect.9, read-length-effect.10, read-length-effect.11 · trail: CB2-RRNA §What is measured about variation · from: CB2-RRNA:B-0088, CB2-RRNA:B-0090..0091
- **dns.10** "Vollmers et al. and Gruber-Vodicka et al. measured how conserved regions fragment 16S assemblies."
  why: Both describe the mechanism, and neither statement is itself a measurement. · instead: assembly-fragmentation.1, assembly-fragmentation.2, assembly-fragmentation.4 · trail: CB2-RRNA §The mechanism · from: CB2-RRNA:B-0047..0049

## Gaps

- **gap.1** The findings were never checked by a second reader: no independent critic ran, no second agent re-derived the load-bearing figures, and the post-hoc check covered the references, not the claims. The answers rest on Orellana et al.'s 88% against 23% (with short-read libraries three times deeper), CAMI II's short-read 16S completeness of 29.6–36.9% against 47.1–60.1% for hybrids, Pericard et al.'s simulated 2×–50× depth series, Philip et al.'s read-pair floor (more than 10, in most cases more than 40), and Overholt et al.'s 16 against 10 MAGs with a 16S gene.
  blocks: variation-axes, read-length-effect, assembler-effect, depth-effect · origin: no critic: the note's own warning that no adversarial pass was run and the claims rest on a single agent's reading; it asks that the numbers be treated as unconfirmed until spot-checked against the primary text · search: not stated · trail: CB2-RRNA §No adversarial pass, §Verification log · from: CB2-RRNA:B-0016..0018, CB2-RRNA:B-0118..0119, CB2-RRNA:A-002..003, CB2-RRNA:A-008..010, CB2-RRNA:B-0085, CB2-RRNA:B-0087..0088, CB2-RRNA:B-0099
- **gap.2** Whether rRNA recovery varies by study of origin, holding environment and pipeline constant.
  blocks: study-of-origin, variation-axes · origin: not found; the catalogues pool across studies and report one figure · search: searched, not found (note: "I looked for this specifically, from several angles") · from: CB2-RRNA:B-0104..0106, CB2-RRNA:B-0111
- **gap.3** How library depth affects the number of MAGs carrying a 16S gene: a real metagenome subsampled to a depth series and run through a standard assemble-and-bin pipeline at each depth.
  blocks: depth-effect · origin: not found · search: searched, not found (note: "What nobody I found has done") · from: CB2-RRNA:B-0100, CB2-RRNA:B-0103
- **gap.4** How much of the missing 16S is lost in binning rather than assembly: what fraction of missing 16S genes were assembled but binned elsewhere, against never assembled.
  blocks: rrna-binning · origin: not found; the review calls it a real gap · search: searched, not found (note: "I did not find a paper that isolates and quantifies the binning contribution") · from: CB2-RRNA:B-0065..0066
- **gap.5** An independent replication of the METASEED result that only 1 of 253 conventionally assembled 16S sequences matched at >99%.
  blocks: assembly-fragmentation · origin: one paper and one lab; the review calls its support thin · search: searched, not found (note: "I have not found an independent replication") · src: philipMETASEEDNovelApproach2024 · from: CB2-RRNA:B-0057, CB2-RRNA:B-0060
- **gap.6** A documented source for the share of MAGs that carry a 16S gene across catalogues: the most-quoted figure (7%) rests on an Opinion article that does not document its method.
  blocks: catalogue-recovery · origin: the review's caution about Hiseni et al. (2022) · search: not stated · src: hiseniQuestioningQuality16S2022 · from: CB2-RRNA:B-0029..0032
- **gap.7** The figures taken by single-pass extraction (METASEED's assembly and false-positive figures, MarkerMAG's linking rates, Philip et al.'s read-pair floor) have not been verified in extracted text.
  blocks: assembly-fragmentation, rrna-reconstruction, linking-tools, depth-effect · origin: the note's warning that numbers marked single-pass extraction carry the risk of an automated read returning figures not in the document · search: not stated · from: CB2-RRNA:B-0006..0008, CB2-RRNA:B-0057, CB2-RRNA:B-0075, CB2-RRNA:B-0077, CB2-RRNA:B-0099
- **gap.8** Ye et al. (2020) was not retrieved: its 31% and 1.2% figures are known only as quoted by Singleton et al.
  blocks: read-length-effect · origin: source not obtained; cited within Singleton et al. · search: not stated · src: ye2020 · from: CB2-RRNA:R-0057..0058
- **gap.9** Per-assembler rRNA counts for Vollmers et al.'s high-diversity forest soil metagenome: the main text does not tabulate them, so only the kelp biofilm figure is a clean number.
  blocks: assembler-effect · origin: not tabulated in the source's main text · search: not stated · src: vollmersComparingEvaluatingMetagenome2017 · from: CB2-RRNA:B-0095
- **gap.10** Whether reconstruction of near-full-length 16S with few chimeras, shown for 454 reads of a low-complexity sponge community, holds for Illumina-length reads in a complex environment.
  blocks: rrna-reconstruction · origin: not found; Fan et al. used ~350 nt reads · search: searched, not found (note: "no later work I found does") · src: fanReconstructionRibosomalRNA2012 · from: CB2-RRNA:B-0078..0079

## Out of scope

None: every required item is cited by an entry.

## Sources

```bibtex
@article{almeidaUnifiedCatalog2042020,
  author = {Almeida, A. and Nayfach, S. and Boland, M. and Strozzi, F. and Beracochea, M. and Shi, Z. J. and Pollard, K. S. and Sakharova, E. and Parks, D. H. and Hugenholtz, P. and Segata, N. and Kyrpides, N. C. and Finn, R. D.},
  title = {A unified catalog of 204,938 reference genomes from the human gut microbiome},
  journal = {Nature Biotechnology},
  volume = {39},
  number = {1},
  pages = {105--114},
  year = {2021},
  doi = {10.1038/s41587-020-0603-3},
  note = {access: full_text (CB2-RRNA; targeted verbatim quotations from the publisher or PMC full text via automated fetch); cited as: CB2-RRNA Almeida et al. (UHGG)}
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
  note = {access: full_text (CB2-RRNA; targeted verbatim quotations via automated fetch); cited as: CB2-RRNA Fan et al.}
}

@article{grubervodickaPhyloFlashRapidSmallsubunit2020,
  author = {Gruber-Vodicka, H. R. and Seah, B. K. B. and Pruesse, E.},
  title = {phyloFlash: rapid small-subunit rRNA profiling and targeted assembly from metagenomes},
  journal = {mSystems},
  volume = {5},
  number = {5},
  pages = {e00920-20},
  year = {2020},
  doi = {10.1128/mSystems.00920-20},
  note = {access: full_text (CB2-RRNA; targeted verbatim quotations via automated fetch); cited as: CB2-RRNA Gruber-Vodicka et al. (phyloFlash)}
}

@article{haryonoRecoveryHighQuality2022,
  author = {Haryono, M. A. S. and Law, Y. Y. and Arumugam, K. and Liew, L. C.-W. and Nguyen, T. Q. N. and Drautz-Moses, D. I. and Schuster, S. C. and Wuertz, S. and Williams, R. B. H.},
  title = {Recovery of high quality metagenome-assembled genomes from full-scale activated sludge microbial communities in a tropical climate using longitudinal metagenome sampling},
  journal = {Frontiers in Microbiology},
  volume = {13},
  pages = {869135},
  year = {2022},
  doi = {10.3389/fmicb.2022.869135},
  note = {access: full_text (CB2-RRNA; preprint read in full as extracted text: bioRxiv 2021.08.21.456929, doi 10.1101/2021.08.21.456929); cited as: CB2-RRNA Haryono et al.}
}

@article{hiseniHumGutComprehensiveHuman2021,
  author = {Hiseni, P. and Rudi, K. and Wilson, R. C. and Hegge, F. T. and Snipen, L.},
  title = {HumGut: a comprehensive human gut prokaryotic genomes collection filtered by metagenome data},
  journal = {Microbiome},
  volume = {9},
  number = {1},
  pages = {165},
  year = {2021},
  doi = {10.1186/s40168-021-01114-w},
  note = {access: not stated; not cited (listed; the HumGut collection is named in the text); cited as: CB2-RRNA reference list}
}

@article{hiseniQuestioningQuality16S2022,
  author = {Hiseni, P. and Snipen, L. and Wilson, R. C. and Furu, K. and Rudi, K.},
  title = {Questioning the quality of 16S rRNA gene sequences derived from human gut metagenome-assembled genomes},
  journal = {Frontiers in Microbiology},
  volume = {12},
  pages = {822301},
  year = {2022},
  doi = {10.3389/fmicb.2021.822301},
  note = {access: full_text (CB2-RRNA; targeted verbatim quotations via automated fetch); type: Opinion article, no methods section; cited as: CB2-RRNA Hiseni et al. 2022}
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
  note = {access: full_text (CB2-RRNA; targeted verbatim quotations via automated fetch); cited as: CB2-RRNA Ma et al. (SMAG)}
}

@article{meyerCriticalAssessmentMetagenome2022,
  author = {Meyer, F. and Fritz, A. and Deng, Z.-L. and Koslicki, D. and Lesker, T. R. and Gurevich, A. and Robertson, G. and Alser, M. and Antipov, D. and Beghini, F. and others},
  title = {Critical Assessment of Metagenome Interpretation: the second round of challenges},
  journal = {Nature Methods},
  volume = {19},
  number = {4},
  pages = {429--440},
  year = {2022},
  doi = {10.1038/s41592-022-01431-4},
  note = {access: full_text (CB2-RRNA; targeted verbatim quotations via automated fetch); cited as: CB2-RRNA Meyer et al. (CAMI II); incomplete: author (first ten of 127 given)}
}

@article{nayfachGenomicCatalogEarths2020,
  author = {Nayfach, S. and Roux, S. and Seshadri, R. and Udwary, D. and Varghese, N. and Schulz, F. and Wu, D. and Paez-Espino, D. and Chen, I.-M. and Huntemann, M. and Palaniappan, K. and Ladau, J. and Mukherjee, S. and Reddy, T. B. K. and Nielsen, T. and Kirton, E. and Faria, J. P. and Edirisinghe, J. N. and Henry, C. S. and Jungbluth, S. P. and Chivian, D. and Dehal, P. and Wood-Charlson, E. M. and Arkin, A. P. and Tringe, S. G. and Visel, A. and {IMG/M Data Consortium} and Woyke, T. and Mouncey, N. J. and Ivanova, N. N. and Kyrpides, N. C. and Eloe-Fadrosh, E. A.},
  title = {A genomic catalog of Earth's microbiomes},
  journal = {Nature Biotechnology},
  volume = {39},
  number = {4},
  pages = {499--509},
  year = {2021},
  doi = {10.1038/s41587-020-0718-6},
  note = {access: full_text (CB2-RRNA; targeted verbatim quotations via automated fetch); cited as: CB2-RRNA Nayfach et al. (GEM)}
}

@article{nebauerTaxonomyBiasMetagenomeAssembled2026,
  author = {Nebauer, D. J. and Nelson, T. and Romanis, C. and Neilan, B. A. and Timms, V. J.},
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
  author = {Orellana, L. H. and Krüger, K. and Sidhu, C. and Amann, R.},
  title = {Comparing genomes recovered from time-series metagenomes using long- and short-read sequencing technologies},
  journal = {Microbiome},
  volume = {11},
  pages = {105},
  year = {2023},
  doi = {10.1186/s40168-023-01557-3},
  note = {access: full_text (CB2-RRNA; targeted verbatim quotations via automated fetch); cited as: CB2-RRNA Orellana et al.}
}

@article{overholtInclusionOxfordNanopore2020,
  author = {Overholt, W. A. and Hölzer, M. and Geesink, P. and Diezel, C. and Marz, M. and Küsel, K.},
  title = {Inclusion of Oxford Nanopore long reads improves all microbial and viral metagenome-assembled genomes from a complex aquifer system},
  journal = {Environmental Microbiology},
  volume = {22},
  number = {9},
  pages = {4000--4013},
  year = {2020},
  doi = {10.1111/1462-2920.15186},
  note = {access: full_text (CB2-RRNA; preprint read in full as extracted text: bioRxiv 2019.12.18.880807, doi 10.1101/2019.12.18.880807; the preprint lacks the ONT-only assembly present in the published version, whose abstract the review cites); cited as: CB2-RRNA Overholt et al.}
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
  note = {access: full_text (CB2-RRNA; preprint read in full as extracted text: bioRxiv 141176, doi 10.1101/141176); cited as: CB2-RRNA Pericard et al. (MATAM)}
}

@article{philipMETASEEDNovelApproach2024,
  author = {Philip, M. and Rudi, K. and Ormaasen, I. and Angell, I. L. and Pettersen, R. and Keeley, N. B. and Snipen, L.-G.},
  title = {METASEED: a novel approach to full-length 16S rRNA gene reconstruction from short read data},
  journal = {BMC Bioinformatics},
  volume = {25},
  number = {1},
  pages = {237},
  year = {2024},
  doi = {10.1186/s12859-024-05837-z},
  note = {access: full_text (CB2-RRNA; targeted verbatim quotations via automated fetch; several figures single-pass extraction); cited as: CB2-RRNA Philip et al. (METASEED)}
}

@article{singletonConnectingStructureFunction2021,
  author = {Singleton, C. M. and Petriglieri, F. and Kristensen, J. M. and Kirkegaard, R. H. and Michaelsen, T. Y. and Andersen, M. H. and Kondrotaite, Z. and Karst, S. M. and Dueholm, M. S. and Nielsen, P. H. and Albertsen, M.},
  title = {Connecting structure to function with the recovery of over 1000 high-quality metagenome-assembled genomes from activated sludge using long-read sequencing},
  journal = {Nature Communications},
  volume = {12},
  pages = {2009},
  year = {2021},
  doi = {10.1038/s41467-021-22203-2},
  note = {access: full_text (CB2-RRNA; targeted verbatim quotations via automated fetch); cited as: CB2-RRNA Singleton et al.}
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
  note = {access: full_text (CB2-RRNA; targeted verbatim quotations via automated fetch; benchmark figures single-pass extraction of the article HTML); cited as: CB2-RRNA Song et al. (MarkerMAG)}
}

@article{vetrovskyVariability16SRRNA2013,
  author = {Větrovský, T. and Baldrian, P.},
  title = {The variability of the 16S rRNA gene in bacterial genomes and its consequences for bacterial community analyses},
  journal = {PLoS ONE},
  volume = {8},
  number = {2},
  pages = {e57923},
  year = {2013},
  doi = {10.1371/journal.pone.0057923},
  note = {access: full_text (CB2-RRNA; targeted verbatim quotations via automated fetch); cited as: CB2-RRNA Větrovský and Baldrian}
}

@article{vollmersComparingEvaluatingMetagenome2017,
  author = {Vollmers, J. and Wiegand, S. and Kaster, A.-K.},
  title = {Comparing and evaluating metagenome assembly tools from a microbiologist's perspective - not only size matters!},
  journal = {PLoS ONE},
  volume = {12},
  number = {1},
  pages = {e0169662},
  year = {2017},
  doi = {10.1371/journal.pone.0169662},
  note = {access: full_text (CB2-RRNA; targeted verbatim quotations via automated fetch); cited as: CB2-RRNA Vollmers et al.}
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
  note = {access: full_text (CB2-RRNA; targeted verbatim quotations via automated fetch); cited as: CB2-RRNA Yuan et al. (REAGO)}
}

@misc{bowers2017,
  author = {Bowers},
  year = {2017},
  note = {access: not stated (CB2-RRNA); cited in the text as "Bowers et al. 2017, as applied in the sources below" for the MIMAG high-quality bar, with no entry in the reference list; incomplete: author, title, journal, volume, pages, doi}
}

@misc{ye2020,
  author = {Ye},
  year = {2020},
  note = {access: secondary (CB2-RRNA; cited within Singleton et al. 2021 and not independently retrieved; its 31% and 1.2% figures are quoted as reported by Singleton et al., not verified against the original); described as the short-read activated sludge catalogue of 2,045 MAGs; not in the reference list; incomplete: author, title, journal, volume, pages, doi}
}

@article{parksCheckMAssessingQuality2015,
  author = {Parks, Donovan H. and Imelfort, Michael and Skennerton, Connor T. and Hugenholtz, Philip and Tyson, Gene W.},
  title = {CheckM: assessing the quality of microbial genomes recovered from isolates, single cells, and metagenomes},
  journal = {Genome Research},
  volume = {25},
  number = {7},
  pages = {1043--1055},
  year = {2015},
  doi = {10.1101/gr.186072.114},
  note = {background}
}

@article{kangMetaBATEfficientTool2015,
  author = {Kang, Dongwan D. and Froula, Jeff and Egan, Rob and Wang, Zhong},
  title = {MetaBAT, an efficient tool for accurately reconstructing single genomes from complex microbial communities},
  journal = {PeerJ},
  volume = {3},
  pages = {e1165},
  year = {2015},
  doi = {10.7717/peerj.1165},
  note = {background}
}
```
