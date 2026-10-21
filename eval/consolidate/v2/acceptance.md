# Acceptance tests: knowledge note "16S amplicon sequencing from sample to count table"

Knowledge note: `Topics/Biology/Research/Knowledge/16S amplicon sequencing from sample to count table.md` (built 2026-10-21, status draft). Entry IDs below are the note's (`<concept>.<n>`, `dns.<n>`, `gap.<n>`).

## Test A: the 28 MB-01 critic corrections

| # | Correction | Verdict | Entries / what is missing |
|---|---|---|---|
| 1 | Hornung 2019: 265 papers, 2 journals, all community sequencing; not 16S-only; single | applied | contamination.9 (conf single, full scope and counts), dns.16, workflow.2, gap.16 |
| 2 | Water and host sampling unsearched, not "not found" | applied | sample-storage.8, dns.17, gap.2, departure.3 |
| 3 | Departures at most steps, not every step; null effects listed | applied | departure.3, dns.1; null effects in pcr.19-21, run-batch.4, pcr.17, sample-storage.6 |
| 4 | Extraction > PCR > sequencing rests on one 7-taxon dataset; Fouhy contrary, MBQC qualifies | applied | departure.5 (conf single), departure.7, extraction.8, dns.2 |
| 5 | McLaren Bray-Curtis 0.35 to 0.08 is from Brooks 16S cell mixtures (2 calibration, 69 calibrated, 92.6% lower MSE); Costea qualitative | applied | bias-consistency.5, dns.3 |
| 6 | Parada SAR11 4-10-fold vs 2-fold is 515F-Y/806R | applied | primers.4 (conf single, one pair, one taxon), dns.4 |
| 7 | Galazzo: qPCR vs flow r = -0.50; ddPCR agreed with qPCR | applied | absolute-quantification.12, dns.6 |
| 8 | Reitmeier 50-80% spurious after clustering and singleton removal, not "unfiltered" | applied | denoising-clustering.10, dns.7 |
| 9 | Dyrhovden mean Jaccard *distance* 0.80 (0.65-0.87) | applied | technical-variation.2, dns.8 |
| 10 | Lin 2019: authors conclude "is quantitative"; r2 0.19/0.61 unverifiable | applied | absolute-quantification.14 (authors' conclusion, r2 unverified), dns.19, gap.17 |
| 11 | Willis 2019 is argument plus simulated example, not "asserted"; uneven weighting | applied | rarefying.17 (holds), rarefying.16, dns.18. Residue: the src label on Willis in rarefying.16 and rarefying.17 still reads "(FT; assert; cont)" beside Schloss's "model" |
| 12 | Sampling explains replicate disagreement: one 454 dataset; Wen 2017 plateau 39%/43.9% vs predicted 90%; "biases other than random sampling"; run effect | applied | count-sampling.5 (conf cont, "weak and contested"), count-sampling.6, replicate-agreement.6, replicate-agreement.7, count-sampling.9, dns.9 |
| 13 | Square-root decline of CV: one caecal extract, four replicates | applied | count-sampling.7 (conf single), dns.10 |
| 14 | "Relative abundance robust to pipeline" overgeneralised; Zymo "markedly differed"; Straub pipeline-dependent | applied | denoising-clustering.2, denoising-clustering.6, dns.11 |
| 15 | Schirmer 2015 single source | applied | library-sequencing.3 (conf single), dns.12 |
| 16 | Edgar 2018b/c single author with competing classifiers | applied | taxonomy.2, taxonomy.7 (holds), dns.13 |
| 17 | Chimera reproducibility: Haas 2011 alone (Sanger, 454) | applied | chimeras.2 (conf single), dns.14 |
| 18 | Klappenbach 5.5 vs 1.4: one abstract-only study | applied | copy-number.25 (conf single), dns.15 |
| 19 | "Mock bias did not transfer": Parada abstract, one pair, one taxon | applied | dns.5, primers.4, bias-consistency.12, bias-consistency.16 |
| 20 | Access labels: "FT" for Zhou 2011, Kozich 2013, Haegeman 2013, Lin 2019, Kennedy 2014 not confirmable; Zhou 2011 abstract figures; list of unconfirmable figures | partly | Figure-level caveats present: count-sampling.1 (AB-derived), count-sampling.2, bias-consistency.15, reads-per-sample.3, library-sequencing.5, abundance-distribution.2, alpha-diversity.4, absolute-quantification.14, gap.17. Missing: the Sources access notes for Zhou 2011, Kozich 2013, Haegeman 2013 and Lin 2019 still read plain "full_text" with no "not confirmable" qualifier, and in-entry src labels still say "FT" (e.g. microbial-load.2 cites Lin 2019 "FT" with no caveat). Kennedy 2014 is labelled AB throughout, so no problem there |
| 21 | Zhou 2013 soil SAD exponential/inverse gamma: supplementary, unverified | applied | abundance-distribution.1, abundance-distribution.7, dns.21, gap.18 |
| 22 | Kembel 2012 lognormal pools ocean and skin; simulations assumed lognormal | applied | abundance-distribution.3 (conf single), abundance-distribution.8, dns.22 |
| 23 | EMP 2.2 is not a water value | applied | community-copy-number.2, community-copy-number.5, dns.23 |
| 24 | Merged cases: index misassignment 0.1-6%; extraction ratio-scale consistency mixing 16S and shotgun | applied | dns.25 with index-misassignment.2-7 kept separate; dns.24 with bias-consistency.3, bias-consistency.4 |
| 25 | Uneven labels: UNBIAS single-source while McLaren/Silverman not; Jian 2020 shared upstream | applied | dns.30, departure.8, bias-consistency.2 (conf single), dns.31, absolute-quantification.8, dns.20 |
| 26 | Scope drift: DGP diagnosis and load reconciliation are the reviewer's; 5.6 table mixes claims | applied | dns.28 / sample-comparison.2; dns.27 / technical-variation.10; dns.29 |
| 27 | Coverage-based iNEXT stayed depth-correlated (verified) | applied | coverage-standardisation.3, coverage-standardisation.5, rarefying.4, rarefying.5 |
| 28 | Reference errors: Frostegard third author Vincent Ramisse; consortium positions in MBQC and Brooks; Thompson 2017 list truncated | partly | Frostegard author list corrected; Thompson flagged "incomplete: author". Missing: Brooks 2015 and Sinha 2017 (MBQC) author fields still place the consortium where the review did (after Girerd; after Ma); the Crossref order is only recorded in the note field, not applied |

**Totals (A):** applied 26, partly 2, missing 0.

General observation for A: the note's convention keeps each review's original per-citation label inside the `src` parenthesis and puts the correction in `conf`/`holds`. So corrected standing and the uncorrected label sit side by side (Klappenbach "repl" under conf single in copy-number.25; Parada "repl" under conf single in primers.4; Willis "assert"). Anyone reading `src` alone gets the uncorrected standing.

## Test B: literature claims in claims.yaml (kind quoted or derived)

Skipped as video-only (pipeline.py / scene.py): m1, m2, m6, m10, m11, m13, m20, m21, m22, m23, m24, m33, m34. Assessed: 29 claims.

| id | Claim (short) | Verdict | Entries | Notes |
|---|---|---|---|---|
| m3 | Bead beating; tougher cells give less DNA; up to 400% Gram-positive (Albertsen) | claim, stronger | extraction.6, extraction.1, extraction.8 | "often by bead beating" is a usage-frequency claim; the note says frequency of choices is unmeasured (workflow.2). "Tougher cells give up less DNA" is stated as a general rule; extraction.6 is activated sludge only, and extraction effect size is contested (extraction.8) |
| m4 | 16S read as a marker for which bacteria are present (Caporaso 2011) | absent | (nearest: copy-number.bg1) | **Caporaso 2011 is not in Sources.** bg1 (Janda 2007) says the gene is in almost all bacteria, not that it is the marker |
| m5 | 1 to about 15 copies per genome, rarely more, by taxon (Stoddard, Vetrovsky, rrnDB) | claim | copy-number.1, copy-number.3, copy-number.8, copy-number.11 | Consistent; copy-number.8 carries the 21/22 maxima with the reviewer-derivation flag |
| m7 | Conserved and variable regions; one pair fits most bacteria (86% exact, 94.5% one mismatch); each cycle can nearly double (Illumina, Klindworth, Kelly) | claim (partial), stronger | primers.2, pcr.11 | Absent: the conserved/variable-region structure, "no pair fits all", and Klindworth's 86% / 94.5% figures (primers.2 says only that coverage "differs widely"). "Each cycle can nearly double" implies an absolute per-cycle efficiency the note lists as unmeasured (pcr.12, gap.7) |
| m8 | Two widely used protocols, 25 (+8 index) and 35 cycles (Illumina, EMP) | claim, stronger | pcr.2 | Numbers match. "Widely used" is a usage claim the note says is unmeasured (workflow.2); minor |
| m9 | Silverman: 19% of taxa >4-fold off after 35 cycles; 2.6-fold average in mock | claim | pcr.8, pcr.9, pcr.10 | Video adds "10-strain" and attaches "after 35 cycles" to the 19%; neither detail is in the note, but neither is firmer |
| m12 | Index per sample; many samples pooled per run (Illumina, Kozich) | claim | library-sequencing.1, pcr.2, reads-per-sample.3 | |
| m14 | Within one study deepest sample nearly 100x the shallowest (Schloss 2024b) | claim | reads-per-sample.6 | |
| m15 | Some reads land in the wrong sample via index mix-ups or spillover between neighbouring wells; about 2% in one 16S study (Wright, Edgar 2016a, Minich) | claim, stronger | index-misassignment.6, index-misassignment.5, index-misassignment.7, contamination.7, index-misassignment.11 | The 2% is one preprint abstract (index-misassignment.6, conf single); the video gives it no preprint/abstract standing. It also counts neighbouring-well spillover as a cause of wrong-sample reads at demultiplexing, but contamination.7 places well-to-well contamination mainly at extraction, and index-misassignment.7 says barcode leakage on 16S plates was negligible |
| m16 | Reads merged, low-quality/short dropped; stringency changes diversity (Bokulich 2013) | claim | quality-filtering.1, quality-filtering.2, quality-filtering.5, workflow.3 | |
| m17 | Errors make near-copies; ASVs vs 97% OTUs; one soil 8,270 / 11,613 / 16,609 (Nearing, Callahan) | claim | denoising-clustering.1, denoising-clustering.3 | Numbers match |
| m18 | Chimeras 0.9-18.2% at 30 cycles by polymerase; detection catches many, not all (Sze) | claim | chimeras.5, chimeras.4, chimeras.7 | |
| m19 | Classifier names each ASV against a reference; count table (Bokulich 2018) | claim | taxonomy.1, taxonomy.4 | |
| m25 | Rarefying one draw, noise grows as depth shrinks, rarefaction averages; null models: rarefaction removed richness-depth link; estimates expected taxa in subsample (Schloss, Cameron, Hurlbert, Gotelli) | claim (partial) | rarefying.3, rarefying.4, rarefying.12, rarefying.1, rarefying.2 | The definition "estimates the taxa expected in a subsample of the smaller size" has no entry (Hurlbert is in Sources only as SEC via Chao and Jost). Video gives no single-author standing for rarefying.4, but its scope ("in null-model simulations") matches |
| m26 | Rarefying sets aside 48,000 reads; does not remove extraction, copy-number or PCR bias (derived; McLaren) | claim | sample-comparison.1, scaling-normalisation.7, rarefying.6, bias-consistency.2 | Covered only indirectly: no entry states plainly that rarefying leaves taxon bias in place |
| m27 | Bias, or its effect on shares, can differ between samples (Sze, McLaren, Parada) | claim | bias-consistency.11, bias-consistency.2, bias-consistency.12, bias-consistency.13, primers.4, bias-consistency.1 | Wording is as cautious as the note; consistent with dns.31 |
| m28 | Whether to rarefy is still argued; answer differs for alpha, beta, DA | claim | rarefying.16, beta-diversity.4, differential-abundance.14, sample-comparison.1 | |
| m29 | Shares cannot show total load; spike-ins or flow counts measure it (Vandeputte, Tkacz) | claim | absolute-quantification.1, absolute-quantification.2, absolute-quantification.4, microbial-load.1 | Video does not mention that the methods disagree with each other (absolute-quantification.12, .16), but it is no firmer |
| m30 | Cells hold one to dozens or more genome copies in culture; soil barely measured (Pecoraro, MB-02) | claim | genome-copies-per-cell.1, .3, .5, .6, .13, .17, .29, .30; gap.25 | |
| m31 | Dominant 2% of phylotypes about 41% of reads per average sample (Delgado-Baquerizo 2018) | claim | abundance-distribution.10, rarity-terms.14, abundance-distribution.12 | Not pooled with Bickel and Or, so dns.32 is respected |
| m32 | V4 widely used, amplified by EMP with 515F/806R; Illumina guide V3-V4 (EMP, Caporaso 2011) | claim (partial), stronger | primers.3, primers.1 | Absent: that EMP amplifies V4, and that the Illumina guide uses V3-V4. "Widely used" is unmeasured (workflow.2). **Caporaso 2011 is not in Sources** |
| m35 | Paired reads overlap and merge (Illumina, Kozich) | claim | library-sequencing.2, library-sequencing.5, quality-filtering.1, quality-filtering.6 | |
| m36 | Expected barcode length; one V4 dataset ASVs 251-255, most 253 (DADA2 tutorial) | absent | none | **DADA2 Pipeline Tutorial is not in Sources** (callahanDADA2DocumentationPseudopooling is a different page) |
| m37 | Illumina quality falls toward read end; trimming shortens reads; non-specific priming gives odd lengths (DADA2 tutorial, Bokulich) | absent | (nearest: quality-filtering.1, quality-filtering.2) | The thresholds are covered in general terms; the quality decline along the read, truncation, and non-specific priming are not. **DADA2 tutorial missing from Sources** |
| m38 | Cut-offs are a judgement from plots; one set usually applied to all samples; too strict / too loose; changes diversity (DADA2 tutorial, Bokulich, Kopylova) | claim (partial), stronger | quality-filtering.2, quality-filtering.3, quality-filtering.5, workflow.3 | "Judged from quality and length plots" is absent (tutorial not in Sources). "Usually applied to every sample" is a usage-frequency claim the note says is unmeasured (workflow.2), even with the video's "shown in practice" hedge |
| m39 | Bacteria look alike under a microscope; told apart by 16S, which separates most groups but not always close relatives (Woese 1987) | absent | (partial support: primers.15, taxonomy.2, denoising-clustering.17) | Nothing in the note on morphology. "Not always close relatives" is supported by primers.15 / taxonomy.2. **Woese 1987 is not in Sources** |
| m40 | Pool holds far more copies than a run reads, so the run reads a random draw (derived; Illumina MiSeq specs) | claim | reads-per-sample.9, count-sampling.3, count-sampling.8 | **Illumina MiSeq specifications are not in Sources**; the note's maker figure is ">20 million per v3 run" (reads-per-sample.9), the video's is "up to about 25 million read pairs". The molecule arithmetic is the video's own |
| m41 | Overlapping reads check each other; trimming + error correction + overlapping cut substitutions 93% (Schirmer, Edgar and Flyvbjerg) | claim | quality-filtering.6, quality-filtering.7 | Mismatch: quality-filtering.6 credits the 93% to "error correction plus overlapping"; the video adds quality trimming to that combination. quality-filtering.7 (Edgar) is about wrong posterior quality scores, not support for "check each other" |
| m42 | Pooling roughly equimolar but never even; samples yield different usable DNA, so reads differ (Illumina, Schloss 2024b) | claim + gap, stronger | reads-per-sample.7, reads-per-sample.8, reads-per-sample.10, gap.5 | The video states the cause as fact. The note has it only as Schloss's attribution (reads-per-sample.7), the biomass link only second-hand via Schloss (reads-per-sample.8), and within-run variation after equimolar pooling and the library-size-biomass correlation as unfound (reads-per-sample.10, gap.5) |

**Totals (B), 29 claims:** claim 25 (of which stronger 7: m3, m7, m8, m15, m32, m38, m42; partial coverage 5: m7, m25, m32, m38, plus m42 which also touches a gap), dns 0, gap 0 as primary verdict (m42 partly rests on gap.5), absent 4 (m4, m36, m37, m39).

**Sources the knowledge note lacks** (cited by the video): Caporaso 2011 PNAS (m4, m32); Woese 1987 (m39); Callahan DADA2 Pipeline Tutorial 1.16 (m36, m37, m38); Illumina MiSeq specifications (m40). All the other video sources are in Sources. Hurlbert 1971 is there only as SEC.
