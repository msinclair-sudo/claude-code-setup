# Acceptance tests: 16S knowledge note (MB-01 + MB-02)

Knowledge note: `Topics/Biology/Research/Knowledge/16S amplicon sequencing from sample to count table.md` (built 2026-10-21, 4,103 lines; Concepts, 50 do-not-say, 37 gaps, 254 BibTeX sources). Read against the files named in the brief only; no sources opened.

## Test A: MB-01 critic corrections (fact sheet section 1)

Rule used: `applied` when the corrected version is an entry (or sits in an entry's `holds`/`conf`/`src`) and the uncorrected version is a do-not-say entry or absent; `partly` when the uncorrected version survives unflagged elsewhere in a way that would mislead a reader of that entry alone.

| # | Correction | Verdict | Entries | Note |
|---|---|---|---|---|
| 1 | Hornung 2019 controls: all HT community sequencing, 265 papers, 30% (79) / 10% (27), single | applied | contamination.8, dns.11 (workflow-steps.2) | |
| 2 | Water and host sampling unsearched, not "not found" | applied | sampling-storage.7, dns.1, gap.2, gap.3 | |
| 3 | Departures at most steps examined, several choices no effect | applied | workflow-bias.2, dns.2 | |
| 4 | Extraction > PCR > sequencing ordering is one 7-taxon dataset, contested (Fouhy) and qualified (MBQC) | applied | workflow-bias.4, workflow-bias.6, extraction.2 (conf single), dns.3, dns.4 | |
| 5 | McLaren calibration 0.35 to 0.08 is the Brooks 16S cell mixtures (2 / 69; 92.6% MSE); Costea qualitative | applied | bias-consistency.2, dns.5 | |
| 6 | Parada SAR11 figures are 515F-Y/806R | applied | primers.3, primers.4, bias-consistency.7, dns.6 | |
| 7 | Galazzo: qPCR vs flow r = -0.50; ddPCR strong with qPCR | applied | absolute-quantification.12, dns.8 | |
| 8 | Reitmeier 50-80% after OTU clustering and singleton removal | applied | denoising-clustering.7, dns.9 | |
| 9 | Dyrhovden: mean Jaccard *distance* 0.80 (0.65-0.87) | applied | technical-variation.2, dns.10 | |
| 10 | Lin 2019: authors conclude "is quantitative"; r2 unverifiable | applied | absolute-quantification.14 (limit: access), dns.20 | |
| 11 | Willis 2019: argument plus worked simulated example, not assertion | applied | rarefying.11 (class relabelled, critic: C-043), dns.19 | |
| 12 | Sampling explains replicate disagreement: one 454 dataset, Wen 2017 against (39% plateau, 43.9% at 160k, run effect) | applied | sampling-model.2, sampling-model.3, technical-replicates.3, dns.12 | sampling-model.1 still states Zhou 2013's fit, but conf single and .2 sits beside it |
| 13 | Square-root CV decline: one caecal extract, four replicates | applied | sampling-model.5, dns.13 | |
| 14 | "Relative abundance robust to pipeline" overgeneralised | applied | denoising-clustering.2 (carries "markedly differed"), denoising-clustering.4, dns.14 | |
| 15 | Schirmer 2015 single source | applied | library-prep.2, dns.15 | |
| 16 | Edgar 2018b/c: single author, competing classifiers | applied | taxonomic-assignment.2, taxonomic-assignment.6, dns.16 | |
| 17 | Chimera reproducibility: Haas 2011 alone | applied | chimeras.2 (conf single, critic: C-090), dns.17 | src still reads "(FT; meas; repl; ...)", the note's original label, beside conf single |
| 18 | Klappenbach 2000: one abstract-only study | applied | copy-number.21 (conf single, critic: C-091), dns.18 | src still reads "(AB; meas; repl)" beside conf single |
| 19 | "Mock bias did not transfer": one abstract, one pair, one taxon | applied | primers.4, bias-consistency.9, dns.7 | |
| 20 | Access labels and unconfirmable figures | applied | Sources (Zhou 2011 relabelled AB; Kozich, Haegeman, Lin noted "open full text could not be confirmed"; Kennedy AB with conflict note); bias-consistency.8, technical-replicates.1, gap.18, read-depth.2, abundance-distribution.2, absolute-quantification.14, sequencing-platform.2 | microbial-load.2 (Lin) and richness-estimators.1 (Haegeman) carry "FT" in src with no caveat; their figures are not among the unconfirmable ones |
| 21 | Zhou 2013 SAD exponential / inverse gamma: supplementary Table S3, unverified | **partly** | abundance-distribution.1 (limit: access, C-079) | abundance-distribution.7 restates "exponential or inverse gamma (Zhou 2013) against lognormal" as one side of the conflict with no unverified flag, and no do-not-say covers it |
| 22 | Kembel 2012 lognormal pools ocean and skin; simulations assumed lognormal | applied | abundance-distribution.3, dns.26 | |
| 23 | EMP about 2.2 pools free-living and plant-associated | applied | community-copy-number.1, dns.27 | |
| 24 | Merged cases: index misassignment 0.1-6%; ratio-scale consistency | applied | index-misassignment.10, dns.25; bias-consistency.5, bias-consistency.6, dns.28 | |
| 25 | Uneven labels: UNBIAS vs McLaren/Silverman; Jian shared upstream | applied | copy-number-correction.13, dns.29, absolute-quantification.8 | |
| 26 | Scope drift: reviewer's readings; 5.6 table | applied | rarefying.17, dns.23; technical-replicates.9, dns.21; dns.24 | |
| 27 | Coverage-based iNEXT stayed depth-correlated (verified) | applied | coverage-standardisation.3, rarefying.2 | |
| 28 | Reference errors: Frostegard third author; MBQC and Brooks consortium positions; Thompson list truncated | applied | Sources: frostegardQuantificationBiasRelated1999, sinhaAssessmentVariationMicrobial2017, brooksTruthMetagenomicsQuantifying2015, thompsonCommunalCatalogueReveals2017 (flagged incomplete) | |

**Totals:** applied 27, partly 1, missing 0.

## Test B: claims.yaml literature claims

In scope: claims of kind `quoted` or `derived` with a literature source. Skipped as simulation-only or illustrative: m1, m2, m6, m10, m11, m13, m20, m21, m22, m23, m24, m33, m34. That leaves 29.

| id | Claim (short) | Verdict | Entries | Note |
|---|---|---|---|---|
| m3 | Bead beating; Gram-positive DNA up to 400% (Albertsen) | claim | extraction.1, extraction.5 | |
| m4 | 16S rRNA gene read as a marker for which bacteria are present (Caporaso 2011) | **absent** | none | Caporaso 2011 not in Sources |
| m5 | 1 to about 15 copies, rarely more (Stoddard; Vetrovsky; rrnDB 21/22) | claim | copy-number.1, copy-number.2, copy-number.7, copy-number.11 | |
| m7 | Conserved and variable regions; one pair fits most; best broad pair 86% exact, 94.5% one mismatch (Klindworth); (1+e) per cycle (Kelly) | claim, part absent | pcr-efficiency.4 (Kelly), primers.2 (Klindworth, coverage "differ widely") | Absent: conserved/variable structure (Illumina guide quote) and the 86% / 94.5% figures |
| m8 | "Two widely used" protocols, 25 and 35 cycles (Illumina 25+8; EMP 35) | claim, **stronger** | pcr-efficiency.1 | "Widely used" is a usage claim; workflow-steps.2 says how often each choice is made is unmeasured |
| m9 | 19% of taxa > 4-fold after 35 cycles in lab-grown gut communities; 2.6-fold in mock (Silverman) | claim | pcr.6, pcr.7, pcr-efficiency.3 | "Relative to a model-inferred cycle 0" is not in the note |
| m12 | Index per sample; samples pooled and sequenced together (Illumina; Kozich) | claim | library-prep.1, read-depth.2, read-depth.6 | |
| m14 | Within one study, deepest nearly 100x shallowest (Schloss 2024b) | claim | read-depth.4 | |
| m15 | Reads land in the wrong sample; about 2% in one 16S study (Wright; Edgar UNCROSS; Minich) | claim, **stronger** (standing, minor) | index-misassignment.5, index-misassignment.6, index-misassignment.7, index-misassignment.10, contamination.4 | The 2% is a preprint abstract (index-misassignment.6); the video calls it "one 16S study" |
| m16 | Read merging and filtering; strictness changes diversity (Bokulich 2013) | claim | quality-filtering.1, quality-filtering.2 | |
| m17 | ASVs vs 97% OTUs; one soil 8,270 / 11,613 / 16,609 (Nearing; Callahan 2016) | claim | denoising-clustering.bg1, denoising-clustering.1, denoising-clustering.2 | |
| m18 | Chimeras 0.9-18.2% at 30 cycles; detection catches many not all (Sze) | claim | chimeras.3 | |
| m19 | Classifier against reference database; count table (Bokulich 2018) | claim | taxonomic-assignment.1, taxonomic-assignment.3, workflow-steps.1 | |
| m25 | Rarefying vs repeated rarefaction; removes richness-depth link in null models; estimates taxa expected in a smaller subsample (Schloss; Cameron; Hurlbert; Gotelli) | claim, part absent | rarefying.1, rarefying.2, rarefying.10 | Absent: the "expected taxa in a subsample of the smaller size" definition. Hurlbert 1971 is cited directly, but Sources marks it not_obtained (known via Chao and Jost) |
| m26 | Rarefying sets aside 48,000 reads; does not remove bias or recover missed taxa (derived; McLaren) | claim (indirect) | bias-consistency.1, rarefying.4, absolute-quantification.10, absolute-quantification.17 | No entry says rarefying leaves bias in place; the note supports it only by combining entries |
| m27 | Bias, or its effect on shares, can differ between samples (Sze; McLaren; Parada) | claim | bias-consistency.1, bias-consistency.7, bias-consistency.10, pcr.9, primers.4 | |
| m28 | Whether to rarefy still argued; differs for alpha, beta, DA | claim | rarefying.16, rarefying.11, rarefying.13, beta-diversity.2 | |
| m29 | Shares cannot show total load; spike-ins or flow cytometry (Vandeputte; Tkacz) | claim | absolute-quantification.1, absolute-quantification.2, absolute-quantification.4, microbial-load.1 | |
| m30 | Genome copies per cell from one to dozens or more; in soil barely measured (Pecoraro) | claim | ploidy.1, ploidy.3, ploidy.4, ploidy.5, ploidy.8, ploidy.9, ploidy.15, ploidy.24 | The source line credits "a methanogen with about 50 copies" to Pecoraro; the note gives M. maripaludis up to 55 from Hildenbrand 2011 (ploidy.5) |
| m31 | Dominant 2% (abundant and widespread) about 41% of reads per average sample (Delgado-Baquerizo) | claim | abundance-distribution.10, global-classes.1, abundance-distribution.12 | |
| m32 | "One widely used" region is V4, EMP 515F/806R; Illumina uses V3-V4 (EMP; Caporaso 2011) | **absent** | nearest: primers.1 | Neither the EMP V4 515F/806R statement nor Illumina's V3-V4 is an entry; Caporaso 2011 not in Sources; "widely used" also unsupported (workflow-steps.2) |
| m35 | Paired reads overlap and are merged; fully overlapping V4 (Illumina; Kozich) | claim | sequencing-platform.1, sequencing-platform.2, quality-filtering.1 | |
| m36 | Expected length; one V4 dataset ASVs 251-255 bp, most 253 (DADA2 tutorial) | **absent** | none | DADA2 Pipeline Tutorial not in Sources |
| m37 | Quality falls toward read end; trimming shortens reads; non-specific priming gives odd lengths (DADA2 tutorial; Bokulich 2013) | **absent** | nearest: quality-filtering.2 | Tutorial not in Sources; Bokulich's truncation rule not stated in the note |
| m38 | Cut-offs a judgement from plots; one set for all samples; too strict / too loose; changes diversity (DADA2 tutorial; Bokulich; Kopylova) | claim, part absent | quality-filtering.2, quality-filtering.3, quality-filtering.4 | Absent: judgement from quality/length plots, one cut-off set per study (tutorial not in Sources) |
| m39 | Bacteria look alike; told apart by 16S sequence (Woese 1987) | **absent** | none | Woese 1987 not in Sources |
| m40 | PCR pool far exceeds reads, so the run reads a random draw (derived; MiSeq specifications) | **absent** | nearest: read-depth.6 (makers: > 20 million reads per v3 run) | Illumina MiSeq specifications not in Sources; the video's "up to about 25 million read pairs" is not in the note |
| m41 | Overlap lets reads check each other; trimming, error correction and overlapping cut substitution errors 93% (Schirmer; Edgar and Flyvbjerg) | claim | quality-filtering.5, sequencing-platform.2, quality-filtering.6 | Wording differs: quality-filtering.5 credits the 93% to error correction plus read overlapping, without quality trimming. Edgar and Flyvbjerg appears only for posterior quality scores |
| m42 | Pooling never even, and samples yield different amounts of usable DNA, so depths differ (Illumina; Schloss 2024b) | claim, **stronger**; also gap.6 | read-depth.5, read-depth.8, gap.6 | The video states the biomass/yield cause flatly; the note has it as Schloss's attribution, with the biomass link known only through Schloss, and lists it as a gap |

**Totals:** claim 23 (3 of them `stronger`: m8, m15, m42; 3 with a part absent: m7, m25, m38; m26 only indirect), absent 6 (m4, m32, m36, m37, m39, m40), dns 0, gap 0 as primary verdict (gap.6 is secondary on m42).

**Sources the knowledge note lacks:** Caporaso 2011 (m4, m32), Woese 1987 (m39), the DADA2 Pipeline Tutorial (m36, m37, m38), and the Illumina MiSeq specifications (m40). Whether MB-01 or MB-02 cite them was not checked, because only the named files were read. Hurlbert 1971 (m25) is in Sources but marked not_obtained. No video claim hits a do-not-say entry.
