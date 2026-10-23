## depth-effect.3 (claim)

Philip et al. report the coverage floor: "we need more than 10 read pairs, and in most cases more then 40, to be able to reconstruct a 16S with some substantial length".

- conf: not stated
- class: not stated
- holds: 16S reconstruction from read pairs, as Philip et al. report it
- src: philipMETASEEDNovelApproach2024 (single-pass extraction)
- trail: CB2-RRNA §What is measured about variation

From the note:

> CB2-RRNA:B-0099 [5. What is measured about variation in recovery] Philip et al. report the coverage floor from the other side: "we need more than 10 read pairs, and in most cases more then 40, to be able to reconstruct a 16S with some substantial length" (single-pass extraction).
>

## depth-effect.4 (claim)

Nobody the review found has subsampled a real metagenome to a depth series, run a standard assemble-and-bin pipeline at each depth, and counted how many MAGs carry a 16S gene.

- conf: not stated
- class: search (note: "What nobody I found has done")
- search: searched, not found (note: "What nobody I found has done")
- holds: real metagenomes, library depth, assemble-and-bin pipelines
- src: none (a search result of the review)
- trail: CB2-RRNA §What is measured about variation, §Verdict on the second question

From the note:

> CB2-RRNA:B-0100 [5. What is measured about variation in recovery] What nobody I found has done: subsample a *real* metagenome to a depth series, run a standard assemble-and-bin pipeline at each depth, and count how many MAGs carry a 16S gene.
>
> CB2-RRNA:A-010 [Verdict on the second question] Sequencing depth is directly measured, but only as simulated per-genome coverage in targeted-assembly benchmarks (Pericard et al.'s 2×–50× series; Philip et al.'s read-pair floor) — not as library depth in a real assemble-and-bin pipeline counting rRNA in MAGs, which I could not find anywhere.
>

## depth-effect.5 (claim)

Haryono et al. show MAG quality tracking normalised coverage decile by decile, but their quality axis there is the completeness/contamination classification, not rRNA presence.

- conf: not stated
- class: not stated
- holds: MAG quality as the completeness/contamination classification
- src: haryonoRecoveryHighQuality2022
- trail: CB2-RRNA §What is measured about variation

From the note:

> CB2-RRNA:B-0101 [5. What is measured about variation in recovery] The closest is Haryono et al., who show MAG quality tracking normalised coverage decile by decile — but their quality axis there is the completeness/contamination classification, not rRNA presence.
>

## depth-effect.6 (claim)

Coverage of an organism is not the same variable as depth of a library, and the two are only loosely coupled through community evenness.

- conf: not stated
- class: not stated
- holds: the review's reasoning
- src: none (the reviewer's reasoning)
- trail: CB2-RRNA §What is measured about variation

From the note:

> CB2-RRNA:B-0102 [5. What is measured about variation in recovery] Coverage of an *organism* is not the same variable as depth of a *library*, and the two are only loosely coupled through community evenness.
>

Not found in the cited text (where to look, not what is wrong): holds: review

## depth-effect.7 (claim)

Sequencing depth is directly measured only as simulated per-genome coverage in targeted-assembly benchmarks (Pericard et al.'s 2×–50× series; Philip et al.'s read-pair floor), not as library depth in a real assemble-and-bin pipeline counting rRNA in MAGs: the depth axis is measured for targeted 16S reconstruction in simulation and unmeasured for rRNA-in-MAG recovery in real data.

- conf: not stated
- class: not stated
- rating: "DIRECT EVIDENCE, but only in simulation and only for targeted assembly"
- holds: simulated per-genome coverage, targeted 16S reconstruction
- src: pericardMATAMReconstructionPhylogenetic2018, philipMETASEEDNovelApproach2024
- trail: CB2-RRNA §Verdict, §Verdict on the second question, §What is measured about variation

From the note:

> CB2-RRNA:A-004 [quote: Verdict] Sequencing depth is measured, but only as simulated per-genome coverage in targeted-assembly benchmarks — not as library depth in a real assemble-and-bin pipeline counting rRNA in MAGs.
>
> CB2-RRNA:A-010 [Verdict on the second question] Sequencing depth is directly measured, but only as simulated per-genome coverage in targeted-assembly benchmarks (Pericard et al.'s 2×–50× series; Philip et al.'s read-pair floor) — not as library depth in a real assemble-and-bin pipeline counting rRNA in MAGs, which I could not find anywhere.
>
> CB2-RRNA:B-0096 [5. What is measured about variation in recovery] **Sequencing depth — DIRECT EVIDENCE, but only in simulation and only for targeted assembly.** Pericard et al. simulated five depths (50×, 20×, 10×, 5×, 2× per genome) over 122 genomes carrying 287 distinct 16S copies.
>
> CB2-RRNA:B-0103 [5. What is measured about variation in recovery] So: the depth axis is measured for targeted 16S reconstruction in simulation, and unmeasured for rRNA-in-MAG recovery in real data.
>

## study-of-origin.1 (claim)

The review found nothing that measures rRNA gene recovery as a function of which study or sequencing run a dataset came from, holding environment and pipeline constant, and states that no evidence exists in the literature it searched; it calls this an absence, not weak support, which should not be filled in from the mechanism.

- conf: not stated
- class: search (note: "I looked for this specifically, from several angles")
- search: searched, not found (note: "I looked for this specifically, from several angles")
- rating: "NO EVIDENCE FOUND"
- holds: searched through cross-study comparisons of MAG catalogues, batch effects in metagenome assembly, meta-analyses of public metagenomes, and recent work on variation in MAG recovery
- src: none (a search result of the review)
- trail: CB2-RRNA §What is measured about variation, §Verdict, §Verdict on the second question

From the note:

> CB2-RRNA:B-0104 [5. What is measured about variation in recovery] **Study of origin — NO EVIDENCE FOUND.** I looked for this specifically, from several angles: cross-study comparisons of MAG catalogues, batch effects in metagenome assembly, meta-analyses of public metagenomes, and recent work on variation in MAG recovery.
>
> CB2-RRNA:B-0105 [5. What is measured about variation in recovery] I found nothing that measures rRNA gene recovery as a function of which study or sequencing run a dataset came from, holding environment and pipeline constant.
>
> CB2-RRNA:A-005 [quote: Verdict] For **study of origin** the review reports a plain absence: the large catalogues pool across thousands of source studies and report one number, and no paper stratifies rRNA recovery by originating study.
>
> CB2-RRNA:A-006 [quote: Verdict] The review states explicitly that this is an absence, not weak support, and must not be filled in from the mechanism.
>
> CB2-RRNA:A-011 [Verdict on the second question] For study of origin, the answer is **no evidence exists** in the literature I searched.
>
> CB2-RRNA:A-013 [Verdict on the second question] This is an absence, not weak support, and it should not be filled in from the mechanism.
>

## study-of-origin.2 (claim)

The large catalogues pool across hundreds or thousands of source studies (GEM: >10,000 metagenomes; SMAG: 3,304; UHGG: thousands) and report a single overall figure; none of them stratifies rRNA recovery by source study.

- conf: not stated
- class: not stated
- holds: GEM, SMAG and UHGG
- src: nayfachGenomicCatalogEarths2020, maGenomicCatalogueSoil2023, almeidaUnifiedCatalog2042020
- trail: CB2-RRNA §What is measured about variation, §Verdict on the second question

From the note:

> CB2-RRNA:B-0106 [5. What is measured about variation in recovery] The catalogue papers pool across hundreds or thousands of studies (GEM: >10,000 metagenomes; SMAG: 3,304; UHGG: thousands) and report a single overall figure; none of them stratifies it by source study.
>
> CB2-RRNA:A-005 [quote: Verdict] For **study of origin** the review reports a plain absence: the large catalogues pool across thousands of source studies and report one number, and no paper stratifies rRNA recovery by originating study.
>
> CB2-RRNA:A-012 [Verdict on the second question] The large catalogues pool across thousands of source studies and report one number; no paper stratifies rRNA recovery by the study a dataset came from.
>

## study-of-origin.3 (claim)

Nebauer et al., the closest recent work on systematic variation in MAG recovery, measure taxonomic bias (recovery skewed toward smaller, low-GC organisms) and do not measure rRNA genes at all.

- conf: not stated
- class: not stated
- holds: variation in MAG recovery by taxon
- src: nebauerTaxonomyBiasMetagenomeAssembled2026
- trail: CB2-RRNA §What is measured about variation

From the note:

> CB2-RRNA:B-0107 [5. What is measured about variation in recovery] The closest recent work on systematic variation in MAG recovery, Nebauer et al., measures taxonomic bias — recovery skewed toward smaller, low-GC organisms — and does not measure rRNA genes at all.
>

## study-of-origin.4 (claim)

The Singleton-versus-Ye comparison is between two studies, but it varies technology, plant, depth and pipeline simultaneously and was not designed to isolate study of origin.

- conf: not stated
- class: not stated
- holds: two activated sludge studies
- src: singletonConnectingStructureFunction2021, ye2020 (cited within Singleton et al., not independently retrieved)
- trail: CB2-RRNA §What is measured about variation

From the note:

> CB2-RRNA:B-0108 [5. What is measured about variation in recovery] The Singleton-versus-Ye comparison in section 4 is between two studies, but it varies technology, plant, depth and pipeline simultaneously and was not designed to isolate study of origin.
>
> CB2-RRNA:R-0057 [References] *Cited within Singleton et al. 2021 but not independently retrieved, and therefore not given a reference entry here: Ye et al. (2020), the short-read activated sludge catalogue of 2,045 MAGs.
>

## study-of-origin.5 (claim)

Because the mechanism depends on community composition, sequence diversity and coverage, all of which differ between studies, it is plausible that recovery varies by study of origin; this is an inference, indirect at best, and not a measured finding.

- conf: not stated
- class: reading (note: "That is an inference")
- rating: "INDIRECT at best"
- holds: an inference made at the brief's explicit instruction; nobody has measured it
- src: none (the reviewer's inference)
- trail: CB2-RRNA §What is measured about variation

From the note:

> CB2-RRNA:B-0109 [5. What is measured about variation in recovery] Per the brief's explicit instruction: the mechanism in section 3 depends on community composition, sequence diversity and coverage, all of which differ between studies, and it is therefore *plausible* that recovery varies by study of origin.
>
> CB2-RRNA:B-0110 [5. What is measured about variation in recovery] That is an inference, **INDIRECT** at best, and it is not a measured finding.
>
> CB2-RRNA:B-0111 [5. What is measured about variation in recovery] Nobody has measured it.
>

## variation-axes.1 (claim)

Of the four axes of variation in rRNA recovery that the brief named, direct evidence was found for three (read length and sequencing technology, assembler choice, sequencing depth); for the fourth, study of origin, no evidence exists.

- conf: not stated
- class: not stated
- holds: the four axes the brief named
- src: none (the review's verdict)
- trail: CB2-RRNA §Verdict, §Verdict on the second question

From the note:

> CB2-RRNA:A-001 [quote: Verdict] **Direct evidence found for three of the four axes; for study of origin, NO EVIDENCE EXISTS.**
>
> CB2-RRNA:A-002 [quote: Verdict] Read length and sequencing technology are directly and repeatedly measured, including a controlled same-sample comparison (88% vs 23%) in which depth ran *against* the effect.
>
> CB2-RRNA:A-003 [quote: Verdict] Assembler choice is directly measured on identical inputs, with short-read 16S completeness clustering around 30–37% against 47–60% for hybrids.
>
> CB2-RRNA:A-004 [quote: Verdict] Sequencing depth is measured, but only as simulated per-genome coverage in targeted-assembly benchmarks — not as library depth in a real assemble-and-bin pipeline counting rRNA in MAGs.
>
> CB2-RRNA:A-007 [Verdict on the second question] **Direct evidence found — for three of the four axes; no evidence exists for the fourth.**
>
> CB2-RRNA:B-0082 [5. What is measured about variation in recovery] This is the second target of the brief, and the four axes it names have very different evidentiary status.
>

## dns.1 (do not say)

"Recovery of rRNA genes from metagenomes varies with the study a dataset comes from."

- why: No paper stratifies rRNA recovery by originating study; the review calls this an absence, not weak support, that must not be filled in from the mechanism, and says the plausibility of such variation is an inference, indirect at best, that nobody has measured.
- instead: study-of-origin.1, study-of-origin.5
- trail: CB2-RRNA §Verdict, §What is measured about variation

From the note:

> CB2-RRNA:A-005 [quote: Verdict] For **study of origin** the review reports a plain absence: the large catalogues pool across thousands of source studies and report one number, and no paper stratifies rRNA recovery by originating study.
>
> CB2-RRNA:A-006 [quote: Verdict] The review states explicitly that this is an absence, not weak support, and must not be filled in from the mechanism.
>
> CB2-RRNA:A-013 [Verdict on the second question] This is an absence, not weak support, and it should not be filled in from the mechanism.
>
> CB2-RRNA:B-0109 [5. What is measured about variation in recovery] Per the brief's explicit instruction: the mechanism in section 3 depends on community composition, sequence diversity and coverage, all of which differ between studies, and it is therefore *plausible* that recovery varies by study of origin.
>
> CB2-RRNA:B-0110 [5. What is measured about variation in recovery] That is an inference, **INDIRECT** at best, and it is not a measured finding.
>
> CB2-RRNA:B-0111 [5. What is measured about variation in recovery] Nobody has measured it.
>

Not found in the cited text (where to look, not what is wrong): "Recovery of rRNA genes from metagenomes varies with the study a dataset comes from."

## dns.2 (do not say)

"Only 7% of metagenome-assembled genomes carry a 16S rRNA gene."

- why: The 7% figure comes from Hiseni et al. (2022), an Opinion article with no methods section that does not document how the figure was obtained; the review would not build anything on that number alone.
- instead: catalogue-recovery.1, catalogue-recovery.2, catalogue-recovery.3, catalogue-recovery.4, catalogue-recovery.7
- trail: CB2-RRNA §Measured recovery rates

From the note:

> CB2-RRNA:B-0029 [1. Measured recovery rates in published catalogues] The most-quoted single number in this literature — that only 7% of >270,000 MAGs yield a 16S sequence under a barrnap search, against 93% of >106,000 RefSeq genomes — comes from Hiseni et al. 2022.
>
> CB2-RRNA:B-0030 [1. Measured recovery rates in published catalogues] **Treat this one carefully.** It is published as an Opinion article in *Frontiers in Microbiology*, and when I went looking for the methods behind it there is no methods section: no barrnap length threshold, no statement of which source catalogues the MAGs came from beyond the authors' own HumGut collection, no breakdown.
>
> CB2-RRNA:B-0031 [1. Measured recovery rates in published catalogues] The direction of the result agrees with every catalogue in the table above, but the specific 7% figure rests on a piece that does not document how it was obtained.
>
> CB2-RRNA:B-0032 [1. Measured recovery rates in published catalogues] I would not build anything on that number alone.
>

Not found in the cited text (where to look, not what is wrong): "Only 7% of metagenome-assembled genomes carry a 16S rRNA gene."

## dns.3 (do not say)

"The 16S sequences that MAGs carry are often wrong: MAG clusters share only 93% 16S identity."

- why: This argument comes from the same Hiseni et al. Opinion article, which has no methods section, and the review says the same caveat applies.
- instead: catalogue-recovery.8
- trail: CB2-RRNA §Measured recovery rates

From the note:

> CB2-RRNA:B-0030 [1. Measured recovery rates in published catalogues] **Treat this one carefully.** It is published as an Opinion article in *Frontiers in Microbiology*, and when I went looking for the methods behind it there is no methods section: no barrnap length threshold, no statement of which source catalogues the MAGs came from beyond the authors' own HumGut collection, no breakdown.
>
> CB2-RRNA:B-0031 [1. Measured recovery rates in published catalogues] The direction of the result agrees with every catalogue in the table above, but the specific 7% figure rests on a piece that does not document how it was obtained.
>
> CB2-RRNA:B-0033 [1. Measured recovery rates in published catalogues] Hiseni et al. also report that 97.5%-ANI clusters composed purely of MAGs share on average 93% 16S identity, while clusters of complete RefSeq genomes share 99.8% — an anomaly for a gene that conserved, and their argument that the 16S sequences MAGs *do* carry are often wrong.
>
> CB2-RRNA:B-0034 [1. Measured recovery rates in published catalogues] Same caveat applies.
>

Not found in the cited text (where to look, not what is wrong): "The 16S sequences that MAGs carry are often wrong: MAG clusters share only 93% 16S identity."

## dns.4 (do not say)

"Long-read sequencing raised the share of activated sludge MAGs with rRNA genes from 1.2% (Ye et al.) to 91.3% (Singleton et al.)."

- why: That contrast is across two different studies and two different plants, so it confounds technology with everything else; the review gives the controlled comparison separately.
- instead: read-length-effect.4, read-length-effect.5
- trail: CB2-RRNA §Bounding facts

From the note:

> CB2-RRNA:B-0067 [4. Bounding facts: what works, and how well] **Long reads change the number substantially.** Singleton et al.: all 1,083 MAGs in their high-quality set "encode full-length 16S rRNA, 23S rRNA, 5S rRNA, and >18 tRNA genes", and 91.3% (1,045/1,145) of near-complete MAGs carried full-length 16S.
>
> CB2-RRNA:B-0068 [4. Bounding facts: what works, and how well] They contrast this with a short-read activated sludge study: of Ye et al.'s MAGs, "31% (644) met the MIMAG HQ completeness and contamination threshold … but only 1.2% (25 MAGs) were of HQ according to the MIMAG standards and encoded the rRNA genes".
>
> CB2-RRNA:B-0069 [4. Bounding facts: what works, and how well] That contrast is across two different studies and two different plants, so it confounds technology with everything else; the controlled version is in section 5.
>

Not found in the cited text (where to look, not what is wrong): "Long-read sequencing raised the share of activated sludge MAGs with rRNA genes from 1.2% (Ye et al.) to 91.3% (Singleton et al.)."

## dns.5 (do not say)

"The Singleton and Ye activated sludge studies show that rRNA recovery differs between studies."

- why: The comparison varies technology, plant, depth and pipeline simultaneously and was not designed to isolate study of origin.
- instead: study-of-origin.4
- trail: CB2-RRNA §What is measured about variation

From the note:

> CB2-RRNA:B-0108 [5. What is measured about variation in recovery] The Singleton-versus-Ye comparison in section 4 is between two studies, but it varies technology, plant, depth and pipeline simultaneously and was not designed to isolate study of origin.
>

Not found in the cited text (where to look, not what is wrong): "The Singleton and Ye activated sludge studies show that rRNA recovery differs between studies."

## dns.6 (do not say)

"Deeper sequencing has been shown to increase the number of MAGs that carry a 16S gene."

- why: Depth is measured only as simulated per-genome coverage in targeted-assembly benchmarks, not as library depth in a real assemble-and-bin pipeline counting rRNA in MAGs; coverage of an organism is not the same variable as depth of a library.
- instead: depth-effect.4, depth-effect.7
- trail: CB2-RRNA §What is measured about variation

From the note:

> CB2-RRNA:A-004 [quote: Verdict] Sequencing depth is measured, but only as simulated per-genome coverage in targeted-assembly benchmarks — not as library depth in a real assemble-and-bin pipeline counting rRNA in MAGs.
>
> CB2-RRNA:B-0102 [5. What is measured about variation in recovery] Coverage of an *organism* is not the same variable as depth of a *library*, and the two are only loosely coupled through community evenness.
>
> CB2-RRNA:B-0103 [5. What is measured about variation in recovery] So: the depth axis is measured for targeted 16S reconstruction in simulation, and unmeasured for rRNA-in-MAG recovery in real data.
>

Not found in the cited text (where to look, not what is wrong): "Deeper sequencing has been shown to increase the number of MAGs that carry a 16S gene."

## dns.7 (do not say)

"Haryono et al. show rRNA recovery rising with coverage."

- why: Haryono et al. show MAG quality tracking normalised coverage, but their quality axis there is the completeness/contamination classification, not rRNA presence.
- instead: depth-effect.5
- trail: CB2-RRNA §What is measured about variation

From the note:

> CB2-RRNA:B-0101 [5. What is measured about variation in recovery] The closest is Haryono et al., who show MAG quality tracking normalised coverage decile by decile — but their quality axis there is the completeness/contamination classification, not rRNA presence.
>

Not found in the cited text (where to look, not what is wrong): "Haryono et al. show rRNA recovery rising with coverage."

## dns.8 (do not say)

"Assembly recovers near-full-length 16S genes from metagenomes adequately, with fewer chimeras than PCR amplicons."

- why: That result (Fan et al.) comes from 454 pyrosequencing with ~350 nt reads of a sponge community low-complexity relative to soil; the review would not generalise it to Illumina-length reads in a complex environment, and no later work it found does.
- instead: rrna-reconstruction.6, rrna-reconstruction.7
- trail: CB2-RRNA §Bounding facts

From the note:

> CB2-RRNA:B-0078 [4. Bounding facts: what works, and how well] **One paper reports recovery as adequate, from an older technology.** Fan et al. recovered near-full-length 16S from 454 pyrosequencing of a sponge metagenome with a 3.6% chimera rate before filtering, which they note is below the 5–45% typically reported for PCR amplicons.
>
> CB2-RRNA:B-0079 [4. Bounding facts: what works, and how well] Read length there was ~350 nt and the community was low-complexity relative to soil; I would not generalise it to Illumina-length reads in a complex environment, and no later work I found does.
>

Not found in the cited text (where to look, not what is wrong): "Assembly recovers near-full-length 16S genes from metagenomes adequately, with fewer chimeras than PCR amplicons."

## dns.9 (do not say)

"Overholt et al. agree with Orellana et al. and Singleton et al. that adding long reads raises rRNA recovery."

- why: Within Overholt et al. the hybrid-versus-short-read effect on rRNA was null (not significant) and only the long-read-only effect was large; the review says this should be stated as disagreement in magnitude, not as agreement.
- instead: read-length-effect.9, read-length-effect.10, read-length-effect.11
- trail: CB2-RRNA §What is measured about variation

From the note:

> CB2-RRNA:B-0088 [5. What is measured about variation in recovery] - Overholt et al., verified in extracted text from the preprint: among 44 MAGs recovered by both the Illumina-only and the hybrid assembly of the same aquifer samples, the hybrid set had 16 MAGs with a 16S gene against 10 for Illumina-only (and 16 vs 15 for 5S, 13 vs 9 for 23S), a difference that was **not** significant on a two-proportion z-test.
>
> CB2-RRNA:B-0090 [5. What is measured about variation in recovery] So within this one study the hybrid-versus-short-read effect on rRNA was null and the long-read-only effect was large.
>
> CB2-RRNA:B-0091 [5. What is measured about variation in recovery] That is worth stating as disagreement in magnitude with Orellana et al. and Singleton et al., not as agreement.
>

Not found in the cited text (where to look, not what is wrong): "Overholt et al. agree with Orellana et al. and Singleton et al. that adding long reads raises rRNA recovery."

## dns.10 (do not say)

"Vollmers et al. and Gruber-Vodicka et al. measured how conserved regions fragment 16S assemblies."

- why: Both describe the mechanism, and neither statement is itself a measurement.
- instead: assembly-fragmentation.1, assembly-fragmentation.2, assembly-fragmentation.4
- trail: CB2-RRNA §The mechanism

From the note:

> CB2-RRNA:B-0047 [3. The mechanism, and how much of it is actually measured] **Conservation collapses the assembly graph.** Vollmers et al. describe 16S genes as posing "a highly challenging problem for metagenome assemblers" because multiple highly conserved regions interspersed with hypervariable stretches produce "highly complex branched assembly graph structures", splitting the gene into short contigs confined to conserved regions.
>
> CB2-RRNA:B-0048 [3. The mechanism, and how much of it is actually measured] Gruber-Vodicka et al. give the same account in k-mer terms: conserved regions "lead to sets of shared k-mers among the SSU rRNA sequences present in the read pool that confound the assembly graph structure and eventually cause fragmented assemblies".
>
> CB2-RRNA:B-0049 [3. The mechanism, and how much of it is actually measured] Neither statement is itself a measurement.
>

Not found in the cited text (where to look, not what is wrong): "Vollmers et al. and Gruber-Vodicka et al. measured how conserved regions fragment 16S assemblies."

