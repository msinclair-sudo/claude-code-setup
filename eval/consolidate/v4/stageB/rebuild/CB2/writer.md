# Recovery of rRNA genes from metagenome assemblies and MAGs: writer's view

> [!abstract] About this view
> What the research found, for writing from. Each claim gives who found it, the setting it holds for, the kind of evidence, its standing where the research stated one, and for an absence whether it was searched for. A claim with no standing given has none stated in the research; "limited by access" means a source was not read in full, which is not the same as weak evidence. Sources are listed at the end. The view is generated from the knowledge note `Recovery of rRNA genes from metagenome assemblies and MAGs.md`, where every claim is checked against the research.

## What the research found, by question

### CB2-RRNA

**D1. How completely are ribosomal RNA genes, particularly the small-subunit gene, recovered from assembled metagenomes and from binned genomes, compared with single-copy protein-coding marker genes? What mechanisms are given for the difference, and does published work measure how recovery varies with sequencing depth, read length, assembler, or study of origin?**

*Answer, as the research gave it; not checked by a second reader.* **Verdict on the second question**

**Direct evidence found — for three of the four axes; no evidence exists for the fourth.** Read length and sequencing technology are directly and repeatedly measured, including one controlled same-sample comparison (Orellana et al.: 88% vs 23%) in which depth ran *against* the effect, and one study (Overholt et al.) where the hybrid-versus-short-read difference in rRNA recovery was not significant. Assembler choice is directly measured on identical inputs by CAMI II, Yuan et al., Pericard et al. and Vollmers et al., with short-read 16S completeness clustering around 30–37% against 47–60% for hybrids. Sequencing depth is directly measured, but only as simulated per-genome coverage in targeted-assembly benchmarks (Pericard et al.'s 2×–50× series; Philip et al.'s read-pair floor) — not as library depth in a real assemble-and-bin pipeline counting rRNA in MAGs, which I could not find anywhere. For study of origin, the answer is **no evidence exists** in the literature I searched. The large catalogues pool across thousands of source studies and report one number; no paper stratifies rRNA recovery by the study a dataset came from. This is an absence, not weak support, and it should not be filled in from the mechanism.

## Concepts

In an order where each concept comes after the ones it builds on; the order means nothing more.

### Genome completeness and contamination from marker genes

- The completeness and contamination of draft genomes, metagenome-derived ones included, are estimated from sets of marker genes; CheckM uses marker genes specific to the genome's position in a reference genome tree, with information about the collocation of these genes. (Parks et al. 2015)
  Background, not from the research.

### Metagenome binning

- Metagenome binning groups large genomic fragments assembled from shotgun metagenomic sequences into genome bins; MetaBAT, for example, does so using genome abundance and tetranucleotide frequency. (Kang et al. 2015)
  Background, not from the research.

### The MIMAG high-quality bar and its rRNA requirement

Builds on: Genome completeness and contamination from marker genes.

- The MIMAG high-quality bar requires 5S, 16S and 23S rRNA plus ≥18 tRNAs on top of ≥90% completeness and ≤5% contamination. (Bowers 2017)
  Holds for: the MIMAG standard as applied in the catalogue papers.
- That composite makes the rRNA requirement the binding constraint on the high-quality bar, and several papers say so directly. (the reviewer's synthesis)
  Holds for: the MIMAG high-quality bar.

### rRNA recovery in published MAG catalogues

Builds on: The MIMAG high-quality bar and its rRNA requirement, Metagenome binning.

- In the GEM catalogue (all biomes, >10,000 metagenomes), 9,143 of 52,515 MAGs (17.4%) were high quality, carrying the full rRNA set. (Nayfach et al. 2021)
  Holds for: GEM, all biomes, >10,000 metagenomes.
  Evidence: rated "The most reliable figures" by the research.
- In the SMAG soil catalogue (3,304 metagenomes), 3,641 of 40,039 MAGs (9.1%) were high quality, carrying the full rRNA set. (Ma et al. 2023)
  Holds for: soil, SMAG, 3,304 metagenomes.
  Evidence: rated "The most reliable figures" by the research.
- In the UHGG human gut catalogue, 573 of 4,644 species representatives carried the full rRNA set, and of those only 38 are MAGs (535 are isolates). (Almeida et al. 2021)
  Holds for: human gut, UHGG species representatives.
  Evidence: rated "The most reliable figures" by the research.
- In tropical activated sludge, 142 of 9,079 bins (1.6% of all bins) carried 5S+16S+23S, and 58 met the full MIMAG standard. (Haryono et al. 2022)
  Holds for: tropical activated sludge (engineered), Haryono et al.
  Evidence: rated "The most reliable figures" by the research.
- The GEM catalogue's MAGs have a mean completeness of 83% with mean contamination of 1.3%. (Nayfach et al. 2021)
  Holds for: GEM (Nayfach catalogue).
- Nayfach et al. name "problems assembling the 16S rRNA locus" as one reason the MAGs of new species came out less complete than those of known species. (Nayfach et al. 2021)
  Holds for: GEM (Nayfach catalogue).
- Hiseni et al. (2022) report that only 7% of >270,000 MAGs yield a 16S sequence under a barrnap search, against 93% of >106,000 RefSeq genomes. It is the most-quoted single number in this literature, but it is published in an Opinion article with no methods section (no barrnap length threshold, no statement of which source catalogues the MAGs came from beyond the authors' own HumGut collection, no breakdown); its direction agrees with every catalogue above, and the review would not build anything on the 7% figure alone. (Hiseni et al. 2022)
  Holds for: a barrnap search; MAGs from the authors' own HumGut collection and sources the article does not state.
  Evidence: rated "Treat this one carefully" by the research.
- Hiseni et al. also report that 97.5%-ANI clusters made only of MAGs share on average 93% 16S identity, while clusters of complete RefSeq genomes share 99.8%, an anomaly for a gene that conserved, and they argue that the 16S sequences MAGs do carry are often wrong; the same caveat applies (an Opinion article with no methods section). (Hiseni et al. 2022)
  Holds for: 97.5%-ANI clusters of MAGs against clusters of complete RefSeq genomes.
- Gruber-Vodicka et al. state that "most metagenome-assembled genomes (MAGs) do not contain even fragments of the SSU rRNA gene, not to mention the full gene." (Gruber-Vodicka et al. 2020)
  Holds for: MAGs in general, as a review and tool paper states it.
  Evidence: asserted.
- Ma et al. state that "near full-complement rRNA genes sequences are challenging for assembling from metagenomes, especially for near-complete MAGs." (Ma et al. 2023)
  Holds for: as Ma et al. state it.
  Evidence: asserted.

### rRNA recovery against single-copy marker completeness

Builds on: Genome completeness and contamination from marker genes, The MIMAG high-quality bar and its rRNA requirement.

- In the SMAG soil catalogue, 3,641 MAGs were high quality with rRNA, and a further 5,184 MAGs reached ≥90% completeness and <5% contamination but failed on "the absence of all rRNA genes or less than 18 tRNAs"; so of 8,825 soil MAGs that the single-copy marker estimate calls near-complete, roughly 41% carry the rRNA complement. (Ma et al. 2023)
  Holds for: soil, SMAG.
- In activated sludge, of 9,079 bins, 1,085 (11.9%) were "putative high quality" on single-copy marker statistics; of those, 142 (13.1%) "contained at least one copy of the 5S, 16S and 23S SSU-rRNA genes"; and applying the stringent MIMAG criteria left "only 58 HQ-MAGs". As the abstract puts it, around 1,000 MAGs looked high quality by marker genes and 58 formally were. (Haryono et al. 2022)
  Holds for: activated sludge, Haryono et al.
- In UHGG, 3,207 of 4,644 species representatives were >90% complete and <5% contaminated; 573 additionally had 5S/16S/23S plus ≥18 tRNAs, and only 38 of those 573 were MAGs. (Almeida et al. 2021)
  Holds for: human gut, UHGG species representatives.
- The UHGG paper attributes the shortfall of MAGs with rRNA to the rRNA operon being "a problematic region to assemble from short-read metagenomic datasets". (Almeida et al. 2021)
  Holds for: human gut, UHGG.
- In Hiseni et al.'s analysis all the MAGs were >95% complete with <5% contamination on the conventional single-copy marker criterion, and 7% had a detectable 16S. (Hiseni et al. 2022)
  Holds for: human gut; an Opinion article with no methods section.
- A genome can be scored 90–95% complete on conserved single-copy protein-coding genes and still have no assembled, correctly binned 16S; the pattern is consistent across four environments and four pipelines. (Almeida et al. 2021; Haryono et al. 2022; Hiseni et al. 2022; Ma et al. 2023)
  Holds for: the papers that report both numbers on the same genome set: soil (SMAG), activated sludge (Haryono et al.), human gut (UHGG) and human gut (Hiseni et al.).
  Evidence: replicated.
- The completeness statistic and the rRNA statistic are not measuring the same thing, and the gap between them is large: typically a factor of two to ten depending on the catalogue. (the reviewer's synthesis)
  Holds for: the catalogues the review compared.

### rRNA gene copies per genome

- Větrovský and Baldrian extracted 7,081 16S sequences from 1,690 bacterial genomes: 1–15 copies per genome, mean 4.2, with mean within-genome similarity of 99.70 ± 0.46%. (Vetrovsky and Baldrian 2013)
  Holds for: 1,690 bacterial genomes.
  Evidence: measured.

### Why rRNA genes fragment in metagenome assembly

Builds on: rRNA gene copies per genome.

- Vollmers et al. describe 16S genes as posing "a highly challenging problem for metagenome assemblers" because multiple highly conserved regions interspersed with hypervariable stretches produce "highly complex branched assembly graph structures", splitting the gene into short contigs confined to conserved regions. (Vollmers et al. 2017)
  Holds for: an account of the mechanism, not a measurement.
  Evidence: asserted.
- Gruber-Vodicka et al. give the same account in k-mer terms: conserved regions "lead to sets of shared k-mers among the SSU rRNA sequences present in the read pool that confound the assembly graph structure and eventually cause fragmented assemblies". (Gruber-Vodicka et al. 2020)
  Holds for: an account of the mechanism, not a measurement.
  Evidence: asserted.
- Near-identical repeats of ~1.5 kb (within an ~5 kb operon) are the classic short-read assembly failure mode. (the reviewer's statement)
  Holds for: short-read assembly of multiple rRNA copies per genome.
- In CAMI II, for every assembler except the two hybrids, the median length of contigs aligning to a 16S gene was below the average 16S gene length of 1,503 bp: the gene is typically fragmented, not recovered. (Meyer et al. 2022)
  Holds for: the CAMI II marine dataset, simulated data, 131 known 16S sequences.
  Evidence: modelled.
- In the MATAM benchmark, on a synthetic community of 64 organisms, SPAdes and MEGAHIT run on SortMeRNA-extracted 16S reads recovered genome fractions of 39.9% and 44.3% respectively. (Pericard et al. 2018)
  Holds for: a synthetic community of 64 organisms.
- Averaged across five simulated depths, SPAdes contigs were 21.2% chimeric and MEGAHIT contigs 23.8%. (Pericard et al. 2018)
  Holds for: the MATAM synthetic community of 64 organisms, five simulated depths.
  Evidence: modelled.
- In METASEED, assembling simulated shotgun data conventionally yielded 253 distinct 16S sequences, of which "only 1 gave a >99% match to some of the actual 16S sequences"; the result points the same way as the MATAM chimera rates. (Philip et al. 2024)
  Holds for: simulated shotgun data, conventional assembly.
  Evidence: modelled; a single source; rated "would call its support thin" by the research.
- On real seafloor sediment, METASEED's 26,133,575 contigs yielded 150 distinct 16S sequences after clustering, and only 51 matched amplicon OTUs from the same samples at >99%. (Philip et al. 2024)
  Holds for: seafloor sediment, compared with amplicon OTUs from the same samples.
  Evidence: measured.
- The METASEED authors' framing is that conventional assembly produces mosaic sequences. (Philip et al. 2024)
  Holds for: the METASEED authors' framing.
- The review found no independent replication of the METASEED "1 of 253" result. (a search result of the review)
  Holds for: the literature the review reached.
  Evidence: a search result.
  Searched for and not found.

### Why rRNA genes are lost in binning

Builds on: Metagenome binning, rRNA gene copies per genome, Why rRNA genes fragment in metagenome assembly.

- Three mechanisms are offered: two on the assembly side (conservation collapses the assembly graph; multiple copies per genome, with intragenomic variation) and one on the binning side (copy number defeats coverage-based binning). (the reviewer's synthesis)
  Holds for: the mechanisms the review found offered in the literature.
- Song et al. state that multiple 16S copies "result in unusually high read-depth information" for the contig carrying them, which, together with "atypical nucleotide composition, hinders its correct binning with the rest of the genome"; Gruber-Vodicka et al. make the same point. (Gruber-Vodicka et al. 2020; Song et al. 2022)
  Holds for: coverage-based binning.
- The review found no paper that isolates and quantifies the binning contribution separately from the assembly contribution: nobody it found measured what fraction of missing 16S genes were assembled but then binned elsewhere, against never assembled at all. (a search result of the review)
  Holds for: the literature the review reached.
  Evidence: a search result.
  Searched for and not found.

### Targeted reconstruction of rRNA genes, and how well it works

Builds on: Why rRNA genes fragment in metagenome assembly.

- In Yuan et al.'s benchmark of generic against targeted assemblers on a simulated 11-species set, REAGO recovered 11/11 genes with 1 incorrect assembly, EMIRGE 6/11 (genus-excluded database) with 17 incorrect, IDBA-UD 3/11 with 413 incorrect and MetaVelvet 1/11 with 1,257 incorrect. (Yuan et al. 2015)
  Holds for: a simulated 11-species set.
  Evidence: modelled.
- On Yuan et al.'s 64-species synthetic community, REAGO recovered 58/64 genes (2 incorrect), IDBA-UD 39/64 (28 incorrect), EMIRGE 19/64 (89 incorrect) and MetaVelvet 4/64 (131 incorrect). (Yuan et al. 2015)
  Holds for: a 64-species synthetic community.
- The targeted tools are not clean either: on the MATAM synthetic community, MATAM reached a genome fraction of 83.1% with 3.2% chimeras, EMIRGE 50.7% with 17.4% chimeras and REAGO 42.8% with 15.5% chimeras. (Pericard et al. 2018)
  Holds for: the MATAM synthetic community.
- The MATAM authors note that all methods handled genes sharing <90% identity with their nearest neighbour, but that "performances significantly dropped" for paralogous copies around 99% identity, where EMIRGE and REAGO merged reads from distinct paralogs into single erroneous sequences. (Pericard et al. 2018)
  Holds for: the MATAM benchmark.
- METASEED reports 1,631 reconstructions with 1,534 matching at >99% (6% false positives), against EMIRGE 1,589/1,118 (30%) and MATAM 992/832 (16%). (Philip et al. 2024)
  Holds for: as reported by the tool's own authors.
- Fan et al. recovered near-full-length 16S from 454 pyrosequencing of a sponge metagenome with a 3.6% chimera rate before filtering, which they note is below the 5–45% typically reported for PCR amplicons; read length there was ~350 nt and the community was low-complexity relative to soil. (Fan et al. 2012)
  Holds for: 454 pyrosequencing (~350 nt reads) of a sponge metagenome, a community low-complexity relative to soil.
- The review would not generalise Fan et al.'s result to Illumina-length reads in a complex environment, and no later work it found does. (Fan et al. 2012)
  Holds for: Illumina-length reads in a complex environment.
  Evidence: a search result.
  Searched for and not found.

### Linking 16S genes to MAGs

Builds on: Why rRNA genes are lost in binning.

- MarkerMAG, on benchmark datasets at 100% linking accuracy, recovered 88.2% (15/17 MAGs) on the low-complexity MBARC-26 dataset, 53.5% (23/43) on the medium-complexity and 46.7% (14/30) on the high-complexity dataset. (Song et al. 2022)
  Holds for: benchmark datasets of low, medium and high complexity, at 100% linking accuracy.
- On real data, MarkerMAG's improvement over baseline ranged from 1.1-fold (macroalgae) to 14.2-fold (pig gut). (Song et al. 2022)
  Holds for: real datasets, macroalgae to pig gut.
- Linking tools recover part but not most of the gap. (Song et al. 2022)
  Holds for: the review's reading of the MarkerMAG figures.

### Read length and sequencing technology

Builds on: The MIMAG high-quality bar and its rRNA requirement, Why rRNA genes fragment in metagenome assembly.

- In Singleton et al.'s long-read activated sludge study, all 1,083 MAGs in the high-quality set "encode full-length 16S rRNA, 23S rRNA, 5S rRNA, and >18 tRNA genes". (Singleton et al. 2021)
  Holds for: activated sludge, long-read.
- In Singleton et al., 91.3% (1,045/1,145) of near-complete MAGs carried full-length 16S. (Singleton et al. 2021)
  Holds for: activated sludge, long-read, near-complete MAGs.
- Singleton et al. contrast their result with a short-read activated sludge study: of Ye et al.'s MAGs, "31% (644) met the MIMAG HQ completeness and contamination threshold … but only 1.2% (25 MAGs) were of HQ according to the MIMAG standards and encoded the rRNA genes". (Singleton et al. 2021; Ye 2020)
  Holds for: a short-read activated sludge catalogue of 2,045 MAGs.
  Evidence: limited by access (a source was not read in full; not the same as weak evidence).
- The Singleton-versus-Ye contrast is across two different studies and two different plants, so it confounds technology with everything else. (the reviewer's reading)
  Holds for: two studies of two different activated sludge plants.
- Orellana et al. sequenced the same North Sea bloom samples with Illumina HiSeq (~240 bp paired-end, ~36 Gbp per sample) and PacBio HiFi (~6 kbp CCS reads, ~12 Gbp per sample): "88% of the total long-read MAGs carried a 16S rRNA gene compared to only 23% of MAGs recovered from short-read metagenomes." (Orellana et al. 2023)
  Holds for: North Sea bloom samples (marine time series), 254 long-read against 341 short-read MAGs.
  Evidence: measured; rated "the cleanest controlled comparison I found on any axis" by the research.
- In Orellana et al. the short-read libraries were three times deeper and still recovered 16S in a quarter as many MAGs: depth ran against the effect. (Orellana et al. 2023)
  Holds for: the same North Sea bloom samples.
- On the same simulated CAMI II data, the hybrid assemblers reached mean 16S completeness of 60.1% (GATB) and 47.1% (OPERA-MS), against 29.6–36.9% for the short-read assemblers. (Meyer et al. 2022)
  Holds for: CAMI II simulated data.
  Evidence: modelled.
- On the CAMI II data the median length of 16S-aligning contigs was 8,513 bp and 4,430 bp for the two hybrid assemblers, against below 1,503 bp for the rest. (Meyer et al. 2022)
  Holds for: CAMI II simulated data.
  Evidence: modelled.
- In the Overholt et al. preprint, among 44 MAGs recovered by both the Illumina-only and the hybrid assembly of the same aquifer samples, the hybrid set had 16 MAGs with a 16S gene against 10 for Illumina-only (and 16 vs 15 for 5S, 13 vs 9 for 23S), a difference that was not significant on a two-proportion z-test. (Overholt et al. 2020)
  Holds for: aquifer samples; 44 MAGs recovered by both assemblies.
- The published version of Overholt et al. adds an ONT-only assembly and reports in its abstract that the ONT-only MAGs had a probability of containing rRNA genes "3× higher than either of the other methods." (Overholt et al. 2020)
  Holds for: the ONT-only assembly is in the published version, not the preprint.
- Within Overholt et al. the hybrid-versus-short-read effect on rRNA was null and the long-read-only effect was large, which is a disagreement in magnitude with Orellana et al. and Singleton et al., not agreement. (Orellana et al. 2023; Overholt et al. 2020; Singleton et al. 2021)
  Holds for: hybrid against short-read assembly (Overholt et al.) compared with long-read against short-read (Orellana et al., Singleton et al.).
  Evidence: contested.
- Read length and sequencing technology are directly and repeatedly measured as influences on rRNA recovery, including one controlled same-sample comparison (Orellana et al.: 88% vs 23%) in which depth ran against the effect, and one study (Overholt et al.) where the hybrid-versus-short-read difference in rRNA recovery was not significant. (Orellana et al. 2023; Overholt et al. 2020)
  Holds for: the review's assessment of the read-length and technology axis.
  Evidence: rated "DIRECT EVIDENCE, and it is good" by the research.

### Assembler choice

Builds on: Why rRNA genes fragment in metagenome assembly, Targeted reconstruction of rRNA genes, and how well it works.

- CAMI II quantified 16S completeness per assembler against 131 known 16S sequences in the marine dataset: short-read assemblies recovered 16S at mean completeness between 29.6% (HipMer) and 36.9% (MEGAHIT). (Meyer et al. 2022)
  Holds for: the CAMI II marine dataset, simulated data, 131 known 16S sequences.
  Evidence: modelled.
- Vollmers et al. counted rRNA phylotypes per assembler: on the low-diversity kelp biofilm (KBF) metagenome, metaSPAdes and Ray Meta each recovered 18 sequences, more than any other assembler, and on the high-diversity forest soil metagenome metaSPAdes and IDBA-UD gave the most phylotypes; their main text does not tabulate per-assembler rRNA counts across both datasets, so only the KBF figure is a clean number. (Vollmers et al. 2017)
  Holds for: a low-diversity kelp biofilm metagenome and a high-diversity forest soil metagenome.
- Assembler choice is directly measured on identical inputs by CAMI II (per-assembler 16S completeness), Yuan et al. (per-assembler counts of correctly recovered genes), Pericard et al. (per-tool genome fraction and chimera rate) and Vollmers et al., with short-read 16S completeness clustering around 30–37% against 47–60% for hybrids. (Meyer et al. 2022; Pericard et al. 2018; Vollmers et al. 2017; Yuan et al. 2015)
  Holds for: identical inputs within each benchmark.
  Evidence: rated "DIRECT EVIDENCE" by the research.

### Sequencing depth

Builds on: Targeted reconstruction of rRNA genes, and how well it works, Metagenome binning.

- Pericard et al. simulated five depths (50×, 20×, 10×, 5×, 2× per genome) over 122 genomes carrying 287 distinct 16S copies: "MATAM recovered from 76% to 85% of the reference sequences for sequencing depths greater than 10x, while EMIRGE recovered less than 55% of the reference sequence, and the GF for other methods is lower than 22%." (Pericard et al. 2018)
  Holds for: simulated per-genome depths of 50× to 2× over 122 genomes; targeted 16S reconstruction.
  Evidence: modelled.
- At a low sequencing depth of 2×, MATAM reached a genome fraction of 33%, while the genome fractions of all other assemblers ranged between 5% and 10%. (Pericard et al. 2018)
  Holds for: simulated depth of 2× per genome.
  Evidence: modelled.
- Philip et al. report the coverage floor: "we need more than 10 read pairs, and in most cases more then 40, to be able to reconstruct a 16S with some substantial length". (Philip et al. 2024)
  Holds for: 16S reconstruction from read pairs, as Philip et al. report it.
- Nobody the review found has subsampled a real metagenome to a depth series, run a standard assemble-and-bin pipeline at each depth, and counted how many MAGs carry a 16S gene. (a search result of the review)
  Holds for: real metagenomes, library depth, assemble-and-bin pipelines.
  Evidence: a search result.
  Searched for and not found.
- Haryono et al. show MAG quality tracking normalised coverage decile by decile, but their quality axis there is the completeness/contamination classification, not rRNA presence. (Haryono et al. 2022)
  Holds for: MAG quality as the completeness/contamination classification.
- Coverage of an organism is not the same variable as depth of a library, and the two are only loosely coupled through community evenness. (the reviewer's reasoning)
  Holds for: the review's reasoning.
- Sequencing depth is directly measured only as simulated per-genome coverage in targeted-assembly benchmarks (Pericard et al.'s 2×–50× series; Philip et al.'s read-pair floor), not as library depth in a real assemble-and-bin pipeline counting rRNA in MAGs: the depth axis is measured for targeted 16S reconstruction in simulation and unmeasured for rRNA-in-MAG recovery in real data. (Pericard et al. 2018; Philip et al. 2024)
  Holds for: simulated per-genome coverage, targeted 16S reconstruction.
  Evidence: rated "DIRECT EVIDENCE, but only in simulation and only for targeted assembly" by the research.

### Variation in recovery by study of origin

Builds on: rRNA recovery in published MAG catalogues, Why rRNA genes are lost in binning.

- The review found nothing that measures rRNA gene recovery as a function of which study or sequencing run a dataset came from, holding environment and pipeline constant, and states that no evidence exists in the literature it searched; it calls this an absence, not weak support, which should not be filled in from the mechanism. (a search result of the review)
  Holds for: searched through cross-study comparisons of MAG catalogues, batch effects in metagenome assembly, meta-analyses of public metagenomes, and recent work on variation in MAG recovery.
  Evidence: a search result; rated "NO EVIDENCE FOUND" by the research.
  Searched for and not found.
- The large catalogues pool across hundreds or thousands of source studies (GEM: >10,000 metagenomes; SMAG: 3,304; UHGG: thousands) and report a single overall figure; none of them stratifies rRNA recovery by source study. (Almeida et al. 2021; Ma et al. 2023; Nayfach et al. 2021)
  Holds for: GEM, SMAG and UHGG.
- Nebauer et al., the closest recent work on systematic variation in MAG recovery, measure taxonomic bias (recovery skewed toward smaller, low-GC organisms) and do not measure rRNA genes at all. (Nebauer et al. 2026)
  Holds for: variation in MAG recovery by taxon.
- The Singleton-versus-Ye comparison is between two studies, but it varies technology, plant, depth and pipeline simultaneously and was not designed to isolate study of origin. (Singleton et al. 2021; Ye 2020)
  Holds for: two activated sludge studies.
- Because the mechanism depends on community composition, sequence diversity and coverage, all of which differ between studies, it is plausible that recovery varies by study of origin; this is an inference, indirect at best, and not a measured finding. (the reviewer's inference)
  Holds for: an inference made at the brief's explicit instruction; nobody has measured it.
  Evidence: the reviewer's reading; rated "INDIRECT at best" by the research.

### Which axes of variation in recovery are measured

Builds on: Read length and sequencing technology, Assembler choice, Sequencing depth, Variation in recovery by study of origin.

- Of the four axes of variation in rRNA recovery that the brief named, direct evidence was found for three (read length and sequencing technology, assembler choice, sequencing depth), though depth is measured only as simulated per-genome coverage in targeted-assembly benchmarks, not as library depth in a real assemble-and-bin pipeline counting rRNA in MAGs; for the fourth, study of origin, no evidence exists. (the review's verdict)
  Holds for: the four axes the brief named.

## Do not say

Wordings the research itself says are wrong or overstated, each with the reason and what to say instead.

- Do not write: "Recovery of rRNA genes from metagenomes varies with the study a dataset comes from."
  Why: No paper stratifies rRNA recovery by originating study; the review calls this an absence, not weak support, that must not be filled in from the mechanism, and says the plausibility of such variation is an inference, indirect at best, that nobody has measured.
  Say instead: The review found nothing that measures rRNA gene recovery as a function of which study or sequencing run a dataset came from, holding environment and pipeline constant, and states that no evidence exists in the literature it searched; it calls this an absence, not weak support, which should not be filled in from the mechanism. (a search result of the review)
  Holds for: searched through cross-study comparisons of MAG catalogues, batch effects in metagenome assembly, meta-analyses of public metagenomes, and recent work on variation in MAG recovery.
  Evidence: a search result; rated "NO EVIDENCE FOUND" by the research.
  Searched for and not found.
  Say instead: Because the mechanism depends on community composition, sequence diversity and coverage, all of which differ between studies, it is plausible that recovery varies by study of origin; this is an inference, indirect at best, and not a measured finding. (the reviewer's inference)
  Holds for: an inference made at the brief's explicit instruction; nobody has measured it.
  Evidence: the reviewer's reading; rated "INDIRECT at best" by the research.
- Do not write: "Only 7% of metagenome-assembled genomes carry a 16S rRNA gene."
  Why: The 7% figure comes from Hiseni et al. (2022), an Opinion article with no methods section that does not document how the figure was obtained; the review would not build anything on that number alone.
  Say instead: In the GEM catalogue (all biomes, >10,000 metagenomes), 9,143 of 52,515 MAGs (17.4%) were high quality, carrying the full rRNA set. (Nayfach et al. 2021)
  Holds for: GEM, all biomes, >10,000 metagenomes.
  Evidence: rated "The most reliable figures" by the research.
  Say instead: In the SMAG soil catalogue (3,304 metagenomes), 3,641 of 40,039 MAGs (9.1%) were high quality, carrying the full rRNA set. (Ma et al. 2023)
  Holds for: soil, SMAG, 3,304 metagenomes.
  Evidence: rated "The most reliable figures" by the research.
  Say instead: In the UHGG human gut catalogue, 573 of 4,644 species representatives carried the full rRNA set, and of those only 38 are MAGs (535 are isolates). (Almeida et al. 2021)
  Holds for: human gut, UHGG species representatives.
  Evidence: rated "The most reliable figures" by the research.
  Say instead: In tropical activated sludge, 142 of 9,079 bins (1.6% of all bins) carried 5S+16S+23S, and 58 met the full MIMAG standard. (Haryono et al. 2022)
  Holds for: tropical activated sludge (engineered), Haryono et al.
  Evidence: rated "The most reliable figures" by the research.
  Say instead: Hiseni et al. (2022) report that only 7% of >270,000 MAGs yield a 16S sequence under a barrnap search, against 93% of >106,000 RefSeq genomes. It is the most-quoted single number in this literature, but it is published in an Opinion article with no methods section (no barrnap length threshold, no statement of which source catalogues the MAGs came from beyond the authors' own HumGut collection, no breakdown); its direction agrees with every catalogue above, and the review would not build anything on the 7% figure alone. (Hiseni et al. 2022)
  Holds for: a barrnap search; MAGs from the authors' own HumGut collection and sources the article does not state.
  Evidence: rated "Treat this one carefully" by the research.
- Do not write: "The 16S sequences that MAGs carry are often wrong: MAG clusters share only 93% 16S identity."
  Why: This argument comes from the same Hiseni et al. Opinion article, which has no methods section, and the review says the same caveat applies.
  Say instead: Hiseni et al. also report that 97.5%-ANI clusters made only of MAGs share on average 93% 16S identity, while clusters of complete RefSeq genomes share 99.8%, an anomaly for a gene that conserved, and they argue that the 16S sequences MAGs do carry are often wrong; the same caveat applies (an Opinion article with no methods section). (Hiseni et al. 2022)
  Holds for: 97.5%-ANI clusters of MAGs against clusters of complete RefSeq genomes.
- Do not write: "Long-read sequencing raised the share of activated sludge MAGs with rRNA genes from 1.2% (Ye et al.) to 91.3% (Singleton et al.)."
  Why: That contrast is across two different studies and two different plants, so it confounds technology with everything else; the review gives the controlled comparison separately.
  Say instead: The Singleton-versus-Ye contrast is across two different studies and two different plants, so it confounds technology with everything else. (the reviewer's reading)
  Holds for: two studies of two different activated sludge plants.
  Say instead: Orellana et al. sequenced the same North Sea bloom samples with Illumina HiSeq (~240 bp paired-end, ~36 Gbp per sample) and PacBio HiFi (~6 kbp CCS reads, ~12 Gbp per sample): "88% of the total long-read MAGs carried a 16S rRNA gene compared to only 23% of MAGs recovered from short-read metagenomes." (Orellana et al. 2023)
  Holds for: North Sea bloom samples (marine time series), 254 long-read against 341 short-read MAGs.
  Evidence: measured; rated "the cleanest controlled comparison I found on any axis" by the research.
- Do not write: "The Singleton and Ye activated sludge studies show that rRNA recovery differs between studies."
  Why: The comparison varies technology, plant, depth and pipeline simultaneously and was not designed to isolate study of origin.
  Say instead: The Singleton-versus-Ye comparison is between two studies, but it varies technology, plant, depth and pipeline simultaneously and was not designed to isolate study of origin. (Singleton et al. 2021; Ye 2020)
  Holds for: two activated sludge studies.
- Do not write: "Deeper sequencing has been shown to increase the number of MAGs that carry a 16S gene."
  Why: Depth is measured only as simulated per-genome coverage in targeted-assembly benchmarks, not as library depth in a real assemble-and-bin pipeline counting rRNA in MAGs; coverage of an organism is not the same variable as depth of a library.
  Say instead: Nobody the review found has subsampled a real metagenome to a depth series, run a standard assemble-and-bin pipeline at each depth, and counted how many MAGs carry a 16S gene. (a search result of the review)
  Holds for: real metagenomes, library depth, assemble-and-bin pipelines.
  Evidence: a search result.
  Searched for and not found.
  Say instead: Sequencing depth is directly measured only as simulated per-genome coverage in targeted-assembly benchmarks (Pericard et al.'s 2×–50× series; Philip et al.'s read-pair floor), not as library depth in a real assemble-and-bin pipeline counting rRNA in MAGs: the depth axis is measured for targeted 16S reconstruction in simulation and unmeasured for rRNA-in-MAG recovery in real data. (Pericard et al. 2018; Philip et al. 2024)
  Holds for: simulated per-genome coverage, targeted 16S reconstruction.
  Evidence: rated "DIRECT EVIDENCE, but only in simulation and only for targeted assembly" by the research.
- Do not write: "Haryono et al. show rRNA recovery rising with coverage."
  Why: Haryono et al. show MAG quality tracking normalised coverage, but their quality axis there is the completeness/contamination classification, not rRNA presence.
  Say instead: Haryono et al. show MAG quality tracking normalised coverage decile by decile, but their quality axis there is the completeness/contamination classification, not rRNA presence. (Haryono et al. 2022)
  Holds for: MAG quality as the completeness/contamination classification.
- Do not write: "Assembly recovers near-full-length 16S genes from metagenomes adequately, with fewer chimeras than PCR amplicons."
  Why: That result (Fan et al.) comes from 454 pyrosequencing with ~350 nt reads of a sponge community low-complexity relative to soil; the review would not generalise it to Illumina-length reads in a complex environment, and no later work it found does.
  Say instead: Fan et al. recovered near-full-length 16S from 454 pyrosequencing of a sponge metagenome with a 3.6% chimera rate before filtering, which they note is below the 5–45% typically reported for PCR amplicons; read length there was ~350 nt and the community was low-complexity relative to soil. (Fan et al. 2012)
  Holds for: 454 pyrosequencing (~350 nt reads) of a sponge metagenome, a community low-complexity relative to soil.
  Say instead: The review would not generalise Fan et al.'s result to Illumina-length reads in a complex environment, and no later work it found does. (Fan et al. 2012)
  Holds for: Illumina-length reads in a complex environment.
  Evidence: a search result.
  Searched for and not found.
- Do not write: "Overholt et al. agree with Orellana et al. and Singleton et al. that adding long reads raises rRNA recovery."
  Why: Within Overholt et al. the hybrid-versus-short-read effect on rRNA was null (not significant) and only the long-read-only effect was large; the review says this should be stated as disagreement in magnitude, not as agreement.
  Say instead: In the Overholt et al. preprint, among 44 MAGs recovered by both the Illumina-only and the hybrid assembly of the same aquifer samples, the hybrid set had 16 MAGs with a 16S gene against 10 for Illumina-only (and 16 vs 15 for 5S, 13 vs 9 for 23S), a difference that was not significant on a two-proportion z-test. (Overholt et al. 2020)
  Holds for: aquifer samples; 44 MAGs recovered by both assemblies.
  Say instead: The published version of Overholt et al. adds an ONT-only assembly and reports in its abstract that the ONT-only MAGs had a probability of containing rRNA genes "3× higher than either of the other methods." (Overholt et al. 2020)
  Holds for: the ONT-only assembly is in the published version, not the preprint.
  Say instead: Within Overholt et al. the hybrid-versus-short-read effect on rRNA was null and the long-read-only effect was large, which is a disagreement in magnitude with Orellana et al. and Singleton et al., not agreement. (Orellana et al. 2023; Overholt et al. 2020; Singleton et al. 2021)
  Holds for: hybrid against short-read assembly (Overholt et al.) compared with long-read against short-read (Orellana et al., Singleton et al.).
  Evidence: contested.
- Do not write: "Vollmers et al. and Gruber-Vodicka et al. measured how conserved regions fragment 16S assemblies."
  Why: Both describe the mechanism, and neither statement is itself a measurement.
  Say instead: Vollmers et al. describe 16S genes as posing "a highly challenging problem for metagenome assemblers" because multiple highly conserved regions interspersed with hypervariable stretches produce "highly complex branched assembly graph structures", splitting the gene into short contigs confined to conserved regions. (Vollmers et al. 2017)
  Holds for: an account of the mechanism, not a measurement.
  Evidence: asserted.
  Say instead: Gruber-Vodicka et al. give the same account in k-mer terms: conserved regions "lead to sets of shared k-mers among the SSU rRNA sequences present in the read pool that confound the assembly graph structure and eventually cause fragmented assemblies". (Gruber-Vodicka et al. 2020)
  Holds for: an account of the mechanism, not a measurement.
  Evidence: asserted.
  Say instead: In CAMI II, for every assembler except the two hybrids, the median length of contigs aligning to a 16S gene was below the average 16S gene length of 1,503 bp: the gene is typically fragmented, not recovered. (Meyer et al. 2022)
  Holds for: the CAMI II marine dataset, simulated data, 131 known 16S sequences.
  Evidence: modelled.

## Gaps

What the research did not establish.

- The findings were never checked by a second reader: no independent critic ran, no second agent re-derived the load-bearing figures, and the post-hoc check covered the references, not the claims. The answers rest on Orellana et al.'s 88% against 23% (with short-read libraries three times deeper), CAMI II's short-read 16S completeness of 29.6–36.9% against 47.1–60.1% for hybrids, Pericard et al.'s simulated 2×–50× depth series, Philip et al.'s read-pair floor (more than 10, in most cases more than 40), and Overholt et al.'s 16 against 10 MAGs with a 16S gene.
  The research does not say whether this was searched for.
- Whether rRNA recovery varies by study of origin, holding environment and pipeline constant.
  Searched for and not found.
- How library depth affects the number of MAGs carrying a 16S gene: a real metagenome subsampled to a depth series and run through a standard assemble-and-bin pipeline at each depth.
  Searched for and not found.
- How much of the missing 16S is lost in binning rather than assembly: what fraction of missing 16S genes were assembled but binned elsewhere, against never assembled.
  Searched for and not found.
- An independent replication of the METASEED result that only 1 of 253 conventionally assembled 16S sequences matched at >99%. (Philip et al. 2024)
  Searched for and not found.
- A documented source for the share of MAGs that carry a 16S gene across catalogues: the most-quoted figure (7%) rests on an Opinion article that does not document its method. (Hiseni et al. 2022)
  The research does not say whether this was searched for.
- The figures taken by single-pass extraction (METASEED's assembly and false-positive figures, MarkerMAG's linking rates, Philip et al.'s read-pair floor) have not been verified in extracted text.
  The research does not say whether this was searched for.
- Ye et al. (2020) was not retrieved: its 31% and 1.2% figures are known only as quoted by Singleton et al. (Ye 2020)
  The research does not say whether this was searched for.
- Per-assembler rRNA counts for Vollmers et al.'s high-diversity forest soil metagenome: the main text does not tabulate them, so only the kelp biofilm figure is a clean number. (Vollmers et al. 2017)
  The research does not say whether this was searched for.
- Whether reconstruction of near-full-length 16S with few chimeras, shown for 454 reads of a low-complexity sponge community, holds for Illumina-length reads in a complex environment. (Fan et al. 2012)
  Searched for and not found.

## References

- Almeida, A.; Nayfach, S.; Boland, M.; Strozzi, F.; Beracochea, M.; Shi, Z. J.; Pollard, K. S.; Sakharova, E.; Parks, D. H.; Hugenholtz, P.; Segata, N.; Kyrpides, N. C.; Finn, R. D. (2021). A unified catalog of 204,938 reference genomes from the human gut microbiome. Nature Biotechnology 39(1): 105--114. https://doi.org/10.1038/s41587-020-0603-3
- Bowers (2017).
- Fan, L.; McElroy, K.; Thomas, T. (2012). Reconstruction of ribosomal RNA genes from metagenomic data. PLoS ONE 7(6): e39948. https://doi.org/10.1371/journal.pone.0039948
- Gruber-Vodicka, H. R.; Seah, B. K. B.; Pruesse, E. (2020). phyloFlash: rapid small-subunit rRNA profiling and targeted assembly from metagenomes. mSystems 5(5): e00920-20. https://doi.org/10.1128/mSystems.00920-20
- Haryono, M. A. S.; Law, Y. Y.; Arumugam, K.; Liew, L. C.-W.; Nguyen, T. Q. N.; Drautz-Moses, D. I.; Schuster, S. C.; Wuertz, S.; Williams, R. B. H. (2022). Recovery of high quality metagenome-assembled genomes from full-scale activated sludge microbial communities in a tropical climate using longitudinal metagenome sampling. Frontiers in Microbiology 13: 869135. https://doi.org/10.3389/fmicb.2022.869135
- Hiseni, P.; Snipen, L.; Wilson, R. C.; Furu, K.; Rudi, K. (2022). Questioning the quality of 16S rRNA gene sequences derived from human gut metagenome-assembled genomes. Frontiers in Microbiology 12: 822301. https://doi.org/10.3389/fmicb.2021.822301
- Kang, Dongwan D.; Froula, Jeff; Egan, Rob; Wang, Zhong (2015). MetaBAT, an efficient tool for accurately reconstructing single genomes from complex microbial communities. PeerJ 3: e1165. https://doi.org/10.7717/peerj.1165
- Ma, B.; Lu, C.; Wang, Y.; Yu, J.; Zhao, K.; Xue, R.; Ren, H.; Lv, X.; Pan, R.; Zhang, J.; Zhu, Y.; Xu, J. (2023). A genomic catalogue of soil microbiomes boosts mining of biodiversity and genetic resources. Nature Communications 14(1): 7318. https://doi.org/10.1038/s41467-023-43000-z
- Meyer, F.; Fritz, A.; Deng, Z.-L.; Koslicki, D.; Lesker, T. R.; Gurevich, A.; Robertson, G.; Alser, M.; Antipov, D.; Beghini, F.; others (2022). Critical Assessment of Metagenome Interpretation: the second round of challenges. Nature Methods 19(4): 429--440. https://doi.org/10.1038/s41592-022-01431-4
- Nayfach, S.; Roux, S.; Seshadri, R.; Udwary, D.; Varghese, N.; Schulz, F.; Wu, D.; Paez-Espino, D.; Chen, I.-M.; Huntemann, M.; Palaniappan, K.; Ladau, J.; Mukherjee, S.; Reddy, T. B. K.; Nielsen, T.; Kirton, E.; Faria, J. P.; Edirisinghe, J. N.; Henry, C. S.; Jungbluth, S. P.; Chivian, D.; Dehal, P.; Wood-Charlson, E. M.; Arkin, A. P.; Tringe, S. G.; Visel, A.; IMG/M Data Consortium; Woyke, T.; Mouncey, N. J.; Ivanova, N. N.; Kyrpides, N. C.; Eloe-Fadrosh, E. A. (2021). A genomic catalog of Earth's microbiomes. Nature Biotechnology 39(4): 499--509. https://doi.org/10.1038/s41587-020-0718-6
- Nebauer, D. J.; Nelson, T.; Romanis, C.; Neilan, B. A.; Timms, V. J. (2026). Taxonomy bias in metagenome-assembled genome recovery. Microbial Genomics 12(6): 001736. https://doi.org/10.1099/mgen.0.001736
- Orellana, L. H.; Kruger, K.; Sidhu, C.; Amann, R. (2023). Comparing genomes recovered from time-series metagenomes using long- and short-read sequencing technologies. Microbiome 11: 105. https://doi.org/10.1186/s40168-023-01557-3
- Overholt, W. A.; Holzer, M.; Geesink, P.; Diezel, C.; Marz, M.; Kusel, K. (2020). Inclusion of Oxford Nanopore long reads improves all microbial and viral metagenome-assembled genomes from a complex aquifer system. Environmental Microbiology 22(9): 4000--4013. https://doi.org/10.1111/1462-2920.15186
- Parks, Donovan H.; Imelfort, Michael; Skennerton, Connor T.; Hugenholtz, Philip; Tyson, Gene W. (2015). CheckM: assessing the quality of microbial genomes recovered from isolates, single cells, and metagenomes. Genome Research 25(7): 1043--1055. https://doi.org/10.1101/gr.186072.114
- Pericard, P.; Dufresne, Y.; Couderc, L.; Blanquart, S.; Touzet, H. (2018). MATAM: reconstruction of phylogenetic marker genes from short sequencing reads in metagenomes. Bioinformatics 34(4): 585--591. https://doi.org/10.1093/bioinformatics/btx644
- Philip, M.; Rudi, K.; Ormaasen, I.; Angell, I. L.; Pettersen, R.; Keeley, N. B.; Snipen, L.-G. (2024). METASEED: a novel approach to full-length 16S rRNA gene reconstruction from short read data. BMC Bioinformatics 25(1): 237. https://doi.org/10.1186/s12859-024-05837-z
- Singleton, C. M.; Petriglieri, F.; Kristensen, J. M.; Kirkegaard, R. H.; Michaelsen, T. Y.; Andersen, M. H.; Kondrotaite, Z.; Karst, S. M.; Dueholm, M. S.; Nielsen, P. H.; Albertsen, M. (2021). Connecting structure to function with the recovery of over 1000 high-quality metagenome-assembled genomes from activated sludge using long-read sequencing. Nature Communications 12: 2009. https://doi.org/10.1038/s41467-021-22203-2
- Song, W.; Zhang, S.; Thomas, T. (2022). MarkerMAG: linking metagenome-assembled genomes (MAGs) with 16S rRNA marker genes using paired-end short reads. Bioinformatics 38(15): 3684--3688. https://doi.org/10.1093/bioinformatics/btac398
- Vetrovsky, T.; Baldrian, P. (2013). The variability of the 16S rRNA gene in bacterial genomes and its consequences for bacterial community analyses. PLoS ONE 8(2): e57923. https://doi.org/10.1371/journal.pone.0057923
- Vollmers, J.; Wiegand, S.; Kaster, A.-K. (2017). Comparing and evaluating metagenome assembly tools from a microbiologist's perspective - not only size matters!. PLoS ONE 12(1): e0169662. https://doi.org/10.1371/journal.pone.0169662
- Ye (2020).
- Yuan, C.; Lei, J.; Cole, J.; Sun, Y. (2015). Reconstructing 16S rRNA genes in metagenomic data. Bioinformatics 31(12): i35--i43. https://doi.org/10.1093/bioinformatics/btv231
