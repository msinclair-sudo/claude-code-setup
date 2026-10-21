# Fact-check: piece B against "16S amplicon sequencing from sample to count table"

Authority: `Topics/Biology/Research/Knowledge/16S amplicon sequencing from sample to count table.md` (Concepts, Do not say, Gaps). Nothing else read.

| # | Statement (verbatim) | Verdict | Entries | Note |
|---|---|---|---|---|
| 1 | "Every bacterium and archaeon carries a gene for the 16S ribosomal RNA." | unsupported (illustration) | (copy-number.1, copy-number.2) | Background. Consistent with the copy-number ranges starting at 1, but no entry states it. |
| 2 | "16S amplicon sequencing copies a stretch of that gene (one or more of its variable regions, named V1 to V9, or the full length) from all the DNA in a sample, sequences millions of the copies, sorts them into types and counts them." | unsupported (illustration) | (primers.1, workflow-steps.1) | Background description. Regions and full length are consistent with primers.1; "millions" has no entry (read-depth.6 is a maker's per-run claim). |
| 3 | "The output is a table: samples down one side, taxa across the top, read counts in the cells." | unsupported (illustration) | none | Background. |
| 4 | "How that table is made, and where it bends, decides what it can be used for." | unsupported (illustration) | none | The writer's framing. |
| 5 | "The documented route has twelve steps." | supported | workflow-steps.1 | |
| 6 | "Six happen at the bench." / "The other six happen on a computer." | unsupported (illustration) | (workflow-steps.1) | The bench/computer split is the writer's arrangement. The note lists twelve steps but does not divide them this way (contaminant handling, for example, includes negative controls, which are bench work). |
| 7 | "The sample is collected and preserved (frozen, in ethanol, on FTA paper cards, or in a commercial preservative)." | supported | sampling-storage.1 | |
| 8 | "DNA is extracted with a kit, with more or less vigorous bead beating to break cells open." | supported | extraction.1 | |
| 9 | "Primers are chosen for a gene region." | supported | primers.1 | |
| 10 | "PCR amplifies that region; documented protocols run 25 to 35 cycles." | number | pcr-efficiency.1 | The note has two documented protocols, not a range: 35 cycles (EMP, one-step) and 25 amplicon cycles plus 8 index cycles (Illumina, two-step). Stating them as "25 to 35" drops the 8 index cycles and implies intermediate protocols. |
| 11 | "Each sample's amplicons are tagged with a short index sequence so that hundreds of samples can share one sequencing run." | supported | library-prep.1, read-depth.2 | "Hundreds" is consistent with the 360-sample MiSeq run in read-depth.2. |
| 12 | "The pool is then sequenced, for example on an Illumina MiSeq as paired 250- or 300-base reads, or full length on PacBio." | supported | sequencing-platform.1 | |
| 13 | "Reads are sorted back to samples by their index." | supported | index-misassignment.1 | |
| 14 | "Low-quality reads are filtered and read pairs merged." | supported | quality-filtering.1 | |
| 15 | "Sequencing errors are handled in one of two ways: reads are clustered into operational taxonomic units (OTUs) of reads within 97% or 99% similarity, or exact amplicon sequence variants (ASVs) are inferred with tools such as DADA2, Deblur or UNOISE3." | supported | denoising-clustering.1, denoising-clustering.bg1 | |
| 16 | "Chimeras, hybrid sequences stitched together from two parent templates during PCR, are detected and removed." | supported | chimeras.1 (chimeras.3, chimeras.4) | The definition is background, consistent with the "parents" of chimeras.4. |
| 17 | "A classifier assigns names against a reference database such as SILVA, Greengenes, RDP or GTDB." | supported | taxonomic-assignment.1 | |
| 18 | "Finally, contaminants from reagents are dealt with, using negative controls, statistical tools or abundance cutoffs." | supported | contamination.1 | |
| 19 | "The steps themselves are not disputed; the right choice within them is," | supported | workflow-steps.1 | |
| 20 | "and how often each choice is made across the field has not been measured." | supported | workflow-steps.2 | |
| 21 | "The one exception is controls: a survey of 265 community-sequencing papers published in *Microbiome* and *The ISME Journal* in 2018 (16S and other methods together) found that 30% reported a negative control and 10% a positive one." | supported | contamination.8 | Keeps the not-16S-only scope and avoids dns.11. |
| 22 | "The main test is a mock community, a mixture of cells or DNA of known composition run through the workflow." | unsupported (illustration) | (workflow-bias.1) | Definition and background. No entry calls mocks "the main test". |
| 23 | "Every mock study found the observed composition departing from the known one." | overstated | workflow-bias.1 | Minor. The entry says every mock study *in the body* (of the review). The piece drops that scope, so it reads as all mock studies. |
| 24 | "Two kinds of error behave differently." | supported | workflow-bias.3, workflow-bias.4 | The note splits taxon counts from relative abundance in the same way. |
| 25 | "**The number of taxa** is usually inflated, often grossly." | supported | workflow-bias.3 | |
| 26 | "Sequencing errors, chimeras, reads leaking between samples and reagent contamination add spurious taxa, and together with the choice of clustering or denoising method they can shift the count by one to two orders of magnitude." | supported | workflow-bias.3 | |
| 27 | "On mocks where about 20 taxa were expected, reference-based OTU clustering reported 1,607 to 5,824." | overstated | denoising-clustering.8 | Minor. The figures are right, but the entry is QIIME's closed- and open-reference OTUs on V4 mocks, from a single source. The piece states one tool's result as a property of reference-based OTU clustering in general. |
| 28 | "Contamination grows as the real DNA shrinks:" | supported | contamination.5 (contamination.2, contamination.6) | |
| 29 | "when an eight-member mock was diluted step by step, contaminant reads rose from 0.1% to 80.1% and the number of ASVs from 18 to 381." | supported | contamination.3 | |
| 30 | "Taxa also go missing: a whole phylum, Verrucomicrobia, appeared in stool with some primer pairs and not others." | supported | primers.7 | |
| 31 | "**Relative abundance** errs in a more structured way." | unsupported (claim) | (bias-consistency.1, bias-consistency.10, extraction.5, primers.3, pcr.4) | No entry says relative-abundance error is more structured than taxon-count error. The nearest are the taxon-specific biases and the multiplicative model, whose consistency across samples the note rates weak (bias-consistency.10). Not dns.14, which is about robustness to the pipeline. |
| 32 | "Harder bead beating raised DNA from Gram-positive bacteria by up to 400% in activated sludge." | supported | extraction.5 | |
| 33 | "Primer mismatches under-represent some groups, such as the marine SAR11 clade." | supported | primers.3, primers.6, technical-variation.11 | |
| 34 | "After 35 PCR cycles, one gut mock was off by an average factor of 2.6." | supported | pcr.6, pcr-efficiency.3 | |
| 35 | "Genomes also differ in how many copies of the 16S gene they carry, from 1 to about 15 in most bacteria (database maxima now reach 21 to 22, not yet checked against assembly quality)," | supported | copy-number.1, copy-number.7, gap.36 | gap.36 is stated correctly, as unchecked. |
| 36 | "with Bacillota averaging about 7 per species and soil-common Acidobacteriota about 1.4." | number | copy-number.14, copy-number.13 | 6.9 (1,274 species) and 1.4 (29 species) are set side by side without their n. copy-number.13 says the 1.4 rests on 29 species and calls it imprecise. This is the pattern dns.47 warns against, although dns.47 names the 1.0 figure (Vetrovsky, 4 genomes), not 1.4. Both are reviewer-derived values from rrnDB v5.10. |
| 37 | "Errors of 2 to 30-fold or more between pairs of taxa are reported." | supported | workflow-bias.4 | |
| 38 | "In one seven-taxon dataset extraction contributed most, then PCR, then sequencing, but other studies disagree, and that ordering should not be taken as general." | supported | workflow-bias.4, extraction.2, workflow-bias.6 | Avoids dns.3 and dns.4. |
| 39 | "Correcting for copy number is itself contested:" | supported | copy-number-correction.16 | |
| 40 | "copy numbers must be predicted from sequenced relatives," | supported | copy-number-correction.3, copy-number.23 | |
| 41 | "about half of reference OTUs are too distant from any sequenced genome for good prediction," | supported | copy-number-correction.3 | 49% of SILVA OTUs are more than 15% from a sequenced genome. "Too distant for good prediction" glosses the 15% threshold, which rests on Louca 2018 alone. |
| 42 | "and on ten DNA-based mocks uncorrected data fitted the truth 7.1% better." | supported | copy-number-correction.11 | Uses n = 10, avoiding dns.50. |
| 43 | "The more consequential question is whether these biases are **the same in every sample**." | unsupported (illustration) | (dns.22) | The writer's framing of importance. It stops short of dns.22 ("This determines whether a fixed correction can work"). |
| 44 | "One model treats each step as multiplying every taxon by its own fixed efficiency." | supported | bias-consistency.1 | |
| 45 | "If that holds, the ratio between two taxa is off by the same factor in every sample, while their proportions are off by amounts that change in size and even direction from sample to sample, because a proportion depends on what else is present." | supported | bias-consistency.1, compositional-analysis.3, bias-consistency.4 | |
| 46 | "In the dataset where this was tested, calibrating against control mixtures cut the mean Bray-Curtis dissimilarity between observed and true composition from 0.35 to 0.08." | supported | bias-consistency.2 | Does not call it shotgun (dns.5). |
| 47 | "That consistency rests mainly on that one seven-taxon reanalysis, though." | supported | bias-consistency.10, bias-consistency.5 | |
| 48 | "Against it, in one study SAR11 was under-represented 4 to 10-fold in field samples but only about 2-fold in mocks with the same primers," | supported | primers.4, bias-consistency.7 | Does not attribute it to the original 515F/806R (dns.6) and does not generalise it (dns.7). It omits that the source is abstract-only and covers one primer pair. |
| 49 | "a DNA standard spiked into samples was recovered at anywhere from 40% to 84% through extraction," | supported | extraction.10, bias-consistency.7 | The note says "synthetic spike-in". "DNA standard" is the writer's wording. |
| 50 | "and PCR cycle effects differed between four stool samples." | supported | pcr.9, bias-consistency.7 | |
| 51 | "On top of systematic bias sits noise." | unsupported (illustration) | none | The writer's framing. |
| 52 | "Technical replicates of the same soil DNA extracts shared only a third of their OTUs." | overstated | technical-replicates.3 (technical-replicates.1) | One study (Wen 2017: 18 soil extracts on MiSeq) is stated as a general fact about soil replicates. "A third" is the between-two-replicates figure (33.4%); among three it was 20.2%, and Zhou 2011 on 454 gave 17.2%. So it also loses its definition. |
| 53 | "In deeply sequenced replicates of one soil, presence-absence agreement stalled near 44% even at 160,000 reads, while abundance-weighted agreement reached 95%." | supported | technical-replicates.2, technical-replicates.3, sampling-model.3 | The plateau began near 30,000 reads (at 39%). 43.9% is the value at 160,000. |
| 54 | "Abundant taxa replicate well and rare ones do not." | overstated | technical-replicates.2, technical-replicates.3, technical-replicates.7, sampling-model.5, technical-variation.8 | Stated as a general rule without a hedge. The support is the weighted-versus-unweighted contrast in one soil, one fungal ITS study (INDIRECT), one caecal extract and one five-run study. abundance-occupancy.9 calls the related generalisation the reviewer's argument. This is close to dns.45 in spirit, but it makes no occupancy claim. |
| 55 | "Whether random sampling of molecules explains this is contested;" | supported | sampling-model.2 | Avoids dns.12. |
| 56 | "replicates sequenced in different runs agreed less," | supported | technical-replicates.3 | |
| 57 | "and one run lost an archaeal mock member from every sample." | supported | technical-variation.6 | |
| 58 | "Samples in one study can differ up to about 100-fold in read number." | supported | read-depth.4 | |
| 59 | "Observed richness and the richness estimators Chao1 and ACE rise with depth;" | supported | alpha-diversity.2, alpha-diversity.3 | |
| 60 | "in one set of null models Shannon diversity was less sensitive and inverse Simpson not at all." | supported | alpha-diversity.2 | |
| 61 | "Estimators cannot see the unsampled rare tail;" | supported | richness-estimators.1, abundance-distribution.2 | |
| 62 | "in one test Chao's estimator ranked a community with twenty times fewer species as ten times richer." | supported | richness-estimators.1 | |
| 63 | "Rarefying, randomly subsampling every sample down to a common depth, is contested." | supported | rarefying.16, rarefying.2 | |
| 64 | "One benchmark found that rarefied data gave high false-positive rates in tests for differing taxa." | supported | rarefying.13 | |
| 65 | "A later set of null models found that only repeated rarefaction removed the link between depth and diversity, for both within-sample and between-sample measures." | supported | rarefying.2, rarefying.3, rarefying.5 | |
| 66 | "But those models contain sampling noise only, with no taxon bias or load differences," | supported | rarefying.4 | |
| 67 | "and simulations on both sides flip with their design choices." | supported | rarefying.16, rarefying.13 | Does not state the causal diagnosis as established (dns.23). |
| 68 | "Total load matters because the table is relative." | supported | absolute-quantification.1 (compositional-analysis.1) | "The table is relative" is background reasoning. |
| 69 | "Microbial load differs up to tenfold between healthy human faeces and by more than six orders of magnitude between mouse gut sites." | supported | microbial-load.1, microbial-load.3 | |
| 70 | "A taxon can hold steady or grow in absolute terms while its share falls." | supported | absolute-quantification.4, absolute-quantification.3 | |
| 71 | "Measuring load by qPCR, flow cytometry or added spike-ins has reversed conclusions;" | supported | absolute-quantification.1 | |
| 72 | "a reported trade-off between Bacteroides and Prevotella in the gut turned out to be an artefact of relative data." | supported | absolute-quantification.2 | |
| 73 | "But these measurements do not remove taxon-specific bias," | supported | absolute-quantification.10 | |
| 74 | "and they do not always agree with each other." | supported | absolute-quantification.12, absolute-quantification.16 | |
| 75 | "Tests for which taxa differ between groups disagree widely." | supported | differential-abundance.9 | |
| 76 | "Fourteen methods applied to the same 38 datasets called between 0.8% and 40.5% of ASVs significant," | number | differential-abundance.1 | Minor. The entry gives these as unfiltered means (each method's mean share of significant ASVs across datasets). The piece drops "mean" and "unfiltered", so the figure loses its definition. |
| 77 | "and excess false discoveries were common." | supported | differential-abundance.2, differential-abundance.9 | |
| 78 | "Which method is best is contested," | supported | differential-abundance.9 | |
| 79 | "and no approach has been shown to handle depth, load and taxon bias together." | supported | absolute-quantification.17 | |
| 80 | "On this evidence, a count table is most trustworthy for abundant taxa compared within one study run through a single protocol, and least trustworthy for how many taxa a sample holds or how much of each it contains in absolute terms." | unsupported (claim) | (workflow-bias.3, workflow-bias.7, bias-consistency.5, bias-consistency.10, absolute-quantification.1) | The writer's ranking of trustworthiness, which no entry states. Its parts lean on taxon-count inflation, interlaboratory differences and ratio-scale consistency within a protocol. The note rates that consistency weak, and the "abundant taxa" part rests on row 54. |

## Gaps stated as known

None. gap.36 (the 21 to 22 maxima unchecked against assembly quality) is stated correctly as unchecked. Row 79 states a "not shown", in line with absolute-quantification.17.

## Totals

| verdict | count |
|---|---|
| supported | 63 |
| overstated | 4 |
| number | 3 |
| unsupported (claim) | 2 |
| unsupported (illustration) | 8 |
| dns | 0 |
| **total** | **80** |
