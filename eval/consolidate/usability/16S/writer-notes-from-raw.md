# Notes on writing the 16S piece

## 1. Wanted or needed, not found in the material

- **Why the 16S gene at all.** Nothing explains what makes it suitable: conserved stretches for universal primers, variable regions that separate lineages, what a "variable region" is. The material names V1 to V9 and primer pairs but assumes the reader knows. My one sentence on this ("its sequence differs enough between lineages to be matched against reference databases") is the most I could support.
- **Why the counts are relative.** The piece leans on "the table is relative", but the material never explains the mechanism: equimolar pooling and a fixed run capacity setting the read total, so depth carries no information about biomass. It mentions pooling only as a source of depth variation (Schloss's attribution), and it says depth *correlates* with biomass despite normalisation (secondary, via Schloss). The compositional argument appears only as a review's assertion read at abstract level (Gloor 2017).
- **Definitions of downstream terms.** Alpha and beta diversity, Bray-Curtis, Jaccard, UniFrac, Aitchison distance, PERMANOVA, FDR, "differential abundance", Hill numbers and Good's coverage all appear undefined. I left most out instead of defining them from outside knowledge.
- **How denoising and OTU clustering work.** All the material gives is "97% or 99% identity" and "ASVs from DADA2, Deblur or UNOISE3". It has nothing on what a denoiser does with error profiles or why OTUs and ASVs give different richness.
- **What rarefying costs, concretely.** The material says it "loses data and power" and "adds variance", but gives no figure for how much is discarded in a typical study.
- **A sense of scale for a typical sample.** How many taxa a typical sample holds, and how many reads it typically gets. The only figures are scattered: 774 to 2,869 phylotypes per soil sample (one global study); EMP mean 80,000 reads; one run averaging 9,913 pairs. There is nothing comparable for water or host samples.
- **Field sampling for water and host tissue.** The material says this was never searched (filter volume and pore size, swab versus biopsy).
- **Long-read 16S (PacBio, Nanopore).** Only a developer's claim for PacBio and nothing on Nanopore, so the piece is silent on full-length sequencing.
- **Within-run read-count variation** after equimolar pooling, and **absolute per-cycle PCR efficiency**. Both are reported as not found.
- **Whether bias is consistent across samples.** It is unresolved, and the evidence on both sides is thin (one 7-taxon reanalysis versus a few field and stool results). The piece's closing advice, that within-taxon ratios across samples are the best-protected quantity, rests on one model (McLaren 2019) supported by one dataset. I hedged it with "in principle", but the material offers no empirical test of that advice in real communities.
- **A worked end-to-end example.** I would have liked one sample traced through every step with numbers. The material's figures come from different studies, mocks and platforms, so there is no single chain to follow.
- **Practical guidance on controls and mocks.** One study's title argues for a mock in every run, but the material gives no recommended practice beyond decontam benchmarks and the Hornung control-usage figure. That figure covers all community-sequencing types, not 16S alone. I worded it as "community-sequencing papers" for that reason.

## 2. Hard to use in the material

- **The critique overrides the body, so every figure needed a cross-check.** Each review has an "answers as delivered" block, a body, and an adversarial critique that corrects both. Several figures I wanted were wrong or overstated in the body and answers, and the fix was only in the critique. Examples:
  - The SAR11 bias applies to 515F-Y/806R, not the original V4 primers.
  - Galazzo's r = -0.50 is qPCR versus flow cytometry, not ddPCR.
  - McLaren's calibration result comes from the 16S cell mixtures, not shotgun data.
  - The "extraction > PCR > sequencing" ordering rests on one dataset.
  - Wen 2017's plateau in presence/absence overlap contradicts the "sampling explains it" answer.
  - Reitmeier's 50 to 80% spurious taxa was measured after filtering, not before.
  - Willis 2019 is argument plus a worked example, not bare assertion.

  A reader taking the body or answers at face value would repeat these errors.
- **Inconsistent numbers between and within the two files**, which I had to reconcile:
  - Maximum copies per genome: 15 in research-1, 21 to 22 in research-2's rrnDB derivation.
  - Archaeal maximum: 4 or 5.
  - Acidobacteria mean: 1.0 (4 genomes) or 1.4 (29 species).
  - Index misassignment: "0.1 to 6%" in one table, "0.2 to 6%" in another.
  - Zhou 2011 replicate overlap: the abstract and discussion give different values.
- **Shorthand that is hard to read.** Access and evidence tags ([FT; meas; single]), numbered references in research-2 against author-year in research-1, and many unexpanded acronyms (EMP, MBQC, CSS, VST, SRS, TMM, RLE, iNEXT, ACN). All of it had to be translated before anything could go to an outside reader.
- **Measures that don't line up.** Bias is reported as "maximum pairwise fold" in one study, "average factor per taxon" in another and "% of true proportion" in a third. Replicate agreement is reported as OTU overlap, CV, Jaccard distance or Bray-Curtis. That makes it hard to give a reader one sense of "how big" an effect is. I quoted each figure in its own terms.
- **Most of research-2 is off-topic for this piece.** It covers soil rarity definitions, abundance-occupancy relationships and abundance distributions. Only the copy-number-per-genome and ploidy sections were usable, and the ploidy evidence comes mostly from one laboratory's method, with contrary cases left out of its answers.
- **Uncertain reading depth.** Many "full text" labels mean keyword-in-context extraction, and some were shown not to be open full text at all. That leaves real doubt about figures the critique didn't recheck. I preferred figures the synthesis agent or critic verified (McLaren, Sze and Schloss, Schloss 2024b, Silverman 2021, Karstens 2019).
- **Repetition.** The "Sources not obtained" list in research-1 has every entry twice, and much of the research-1 body is repeated across the answers block, Table 1, the body and "Answers in brief". The repeats differ slightly in wording and sometimes in substance.
