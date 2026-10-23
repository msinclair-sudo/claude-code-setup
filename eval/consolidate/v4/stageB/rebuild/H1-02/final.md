---
type: knowledge
title: Recovery artefacts in the gene content of metagenome-assembled genomes
inputs:
  - H1-02: PhD/Proposal/Research/Results/Recovery artefacts in the gene and pathway content of related metagenome-assembled genomes what has been measured, and how it depends on sample properties.md
refs: PhD/Proposal/Refs/Refs.bib
built: 2026-10-23
status: draft
tags:
  - research
  - knowledge
---
# Recovery artefacts in the gene content of metagenome-assembled genomes

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
| H1-02 | [[Recovery artefacts in the gene and pathway content of related metagenome-assembled genomes what has been measured, and how it depends on sample properties]] | yes | numbered | no | no | fallback |

## Concepts

### mag-recovery: Recovery of genomes from metagenomes and what it can change
needs: none

- **mag-recovery.bg1** Under the MIMAG standard, a high-quality draft metagenome-assembled genome is more than 90% complete with less than 5% contamination and carries the 23S, 16S and 5S rRNA genes and at least 18 tRNAs; a medium-quality draft is at least 50% complete with less than 10% contamination.
  kind: background · ref: bowersMinimumInformationSingle2017 · check: DOI 10.1038/nbt.3893 resolves on Crossref; stated in Table 1 and the section "Mandatory standard metrics" (full text, PMC6436528)
- **mag-recovery.1** Direct measurements exist of how far recovery (incompleteness, contamination, failure to assemble or bin variable and mobile regions, uneven annotation) changes the called gene or pathway content of a recovered genome, although they are few.
  conf: not stated · class: not stated · holds: the review's reading of the literature its search found on recovered genomes · src: none (the reviewer's synthesis) · trail: H1-02 §1. Scope · from: H1-02:B-0022, H1-02:B-0024
- **mag-recovery.2** Whether the size of that change depends on properties of the sample has almost no measurements expressed in gene content; what exists are measurements of recovery quality, MAG yield and chimerism rates, which are proxies.
  conf: not stated · class: not stated · holds: the review's reading of the literature its search found; the review labels the proxies as such · src: none (the reviewer's synthesis) · trail: H1-02 §1. Scope · from: H1-02:B-0023, H1-02:B-0025..0027
- **mag-recovery.3** In the review's search, one natural-sample study compared MAGs with isolate genomes of the same lineage from the same sample at gene level (Meziti et al.: eight E. coli pairs from human stool); a second study reused five of those pairs, so it is not independent. This is a statement about the search, not a structural fact of the literature: it omits SAG-referenced comparisons (Alneberg et al. 2018).
  conf: not stated · class: search (critic: C-052) · search: not stated · holds: natural samples; comparisons against same-sample isolate genomes of the same lineage at gene level; SAG-referenced comparisons not covered · src: mezitiReliabilityMetagenomeassembledGenomes2021, liCriticalAssessmentPangenomic2022, alnebergGenomesUncultivatedProkaryotes2018 · trail: H1-02 §1. Scope, §Adversarial · from: H1-02:B-0029, H1-02:B-0030, H1-02:C-052

### completeness-estimates: Completeness and contamination estimates and how far they track true recovery
needs: mag-recovery

- **completeness-estimates.bg1** CheckM estimates the completeness and contamination of a genome from a set of marker genes specific to the genome's position in a reference genome tree, rather than from a few markers shared by all bacteria or archaea.
  kind: background · ref: parksCheckMAssessingQuality2015 · check: DOI 10.1101/gr.186072.114 resolves on Crossref; stated in the abstract
- **completeness-estimates.1** CheckM simulations found systematic overestimation of completeness under non-redundant contamination, and plasmids and phage were invisible to the estimates.
  conf: not stated · class: model (note: "modelled") · holds: CheckM's own simulations · src: parksCheckMAssessingQuality2015 · trail: H1-02 §2.7 · from: H1-02:B-0118
- **completeness-estimates.2** In Meziti et al., true recovery of the population's genes was on average 16.9% lower than the MiGA completeness estimate and 20.4% lower than the CheckM estimate: two average shortfalls against two estimators, not a range.
  conf: single (note: "single source") · class: meas (note: "measured") · holds: natural human gut; MaxBin 2.0 MAGs against isolate genomes from the same diarrhoeal stool samples; E. coli, n = 8 pairs · src: mezitiReliabilityMetagenomeassembledGenomes2021 · trail: H1-02 §2.7, §critic · from: H1-02:B-0119, H1-02:C-026, H1-02:C-027, H1-02:B-0032, H1-02:C-002
- **completeness-estimates.3** The text of Meziti et al. gives MiGA completeness of its MAGs as 81.1% to 95.5%.
  conf: not stated · class: not stated · holds: Meziti et al.'s MaxBin 2.0 MAGs from diarrhoeal stool samples; the critic's reading of the paper · src: mezitiReliabilityMetagenomeassembledGenomes2021 · trail: H1-02 §critic · from: H1-02:C-028, H1-02:C-029, H1-02:B-0032
- **completeness-estimates.4** Meziti et al. conclude that "the quality of MAGs may often be worse than estimated".
  conf: single (note: "SINGLE SOURCE") · class: not stated · holds: one species in one low-diversity host environment (MAGs and isolates from the same diarrhoeal stool samples) · src: mezitiReliabilityMetagenomeassembledGenomes2021 · trail: H1-02 §2.1 · from: H1-02:B-0032, H1-02:B-0041, H1-02:B-0042
- **completeness-estimates.5** CheckM and GUNC contamination estimates correlated at r = 0.2.
  conf: not stated · class: meas (note: "measured") · holds: natural samples, in Orakov et al.'s study of GUNC on CheckM-prefiltered MAG catalogues · src: orakovGUNCDetectionChimerism2021 · trail: H1-02 §2.2 · from: H1-02:B-0058, H1-02:B-0060
- **completeness-estimates.6** In an illustrative analysis, GTDB MAGs estimated 99.89% and 93.59% complete covered about 80% and 60% of same-species references; the authors state that habitat, strain and pipeline are confounded.
  conf: not stated · class: not stated · limit: access (note: "Seen only as search snippet (WebSearch); not fetched") · holds: an opinion article; not used for any verdict, used for context only; the search agents disagreed on whether it was usable; the note's reference list reports its content while its not-obtained list says it was seen only as a search snippet · src: pellegrinettiRethinkingMetagenomeAssembledGenome2026 · trail: H1-02 §References, §Search record · from: H1-02:R-0137..0142, H1-02:R-0025, H1-02:B-0190, H1-02:B-0191

### content-loss: Gene content lost in recovery (missed core, variable and mobile genes)
needs: mag-recovery, completeness-estimates

- **content-loss.1** MAGs with completeness estimates near 95% captured only 77% of the population core genes and 50% of the variable genes, on average, against isolate genomes from the same samples.
  conf: single (critic: C-002) · class: meas (note: "evidence class: measured") · holds: natural human gut; MaxBin 2.0 MAGs against isolate genomes from the same diarrhoeal stool samples; one species (E. coli), n = 8 pairs, metagenomes 0.21 to 2.8 Gbp; one low-diversity host environment; Li and Yin reuse its data, so they are not independent of it · src: mezitiReliabilityMetagenomeassembledGenomes2021 · trail: H1-02 §2.1, §critic · from: H1-02:B-0032, H1-02:B-0036, H1-02:B-0042, H1-02:C-002, H1-02:C-044, H1-02:C-045
- **content-loss.2** Population core genes missed by the MAG ranged from 11.31% to 34.7% (mean 24.84%), and population-variable genes missed from 13.63% to 69.56% (mean 50.17%).
  conf: single (critic: C-044) · class: meas (note: "evidence class: measured") · holds: natural human gut; MAGs against isolate genomes from the same diarrhoeal stool samples; one species, n = 8 pairs · src: mezitiReliabilityMetagenomeassembledGenomes2021 · trail: H1-02 §2.1, §Adversarial · from: H1-02:B-0032, H1-02:B-0034..0036, H1-02:C-044
- **content-loss.3** Genes with low-identity matches plus genes that had been assembled but binned into other Enterobacteriaceae MAGs made up more than 95% of the missed genes. The paper attributes the low-identity share to sequence divergence from the isolate or to assembly errors, so part of the "loss" may be biology and not recovery; mis-binned genes were 16% to 71% (core) and 64% to 71% (variable) of those without homologs.
  conf: single (note: "SINGLE SOURCE") · class: not stated · holds: Meziti et al.; natural human gut (diarrhoeal stool); E. coli MAG-isolate pairs, n = 8 · src: mezitiReliabilityMetagenomeassembledGenomes2021 · trail: H1-02 §2.1, §critic, §Adversarial · from: H1-02:B-0032, H1-02:B-0037, H1-02:B-0042, H1-02:C-002, H1-02:C-031, H1-02:C-032, H1-02:C-086
- **content-loss.4** When five of Meziti et al.'s E. coli MAGs, or their paired isolates, were mixed with complete genomes, the MAGs lost about 25% of core genes at a 100% core threshold.
  conf: not stated · class: meas (note: "measured") · limit: access (note: "the detail is in a supplementary figure that none of the search agents read") · holds: natural; n = 5 real pairs from human stool, reused from Meziti et al., so not independent of it; the critic: if the 25% comes from Supp. Fig. S14 rather than a main-text statement, it is a full-text breach, and the review should quote the main-text sentence or drop the figure · src: liCriticalAssessmentPangenomic2022 (the detail is in a supplementary figure that none of the search agents read) · trail: H1-02 §2.1, §Adversarial · from: H1-02:B-0029, H1-02:B-0030, H1-02:B-0043, H1-02:B-0044, H1-02:C-035..038
- **content-loss.5** In curated MAGs compared with ten isolate genomes from the same cultures, genomes at 10x coverage or more had over 90% of their sequence recovered (85% at 11x; about 40% at 3.9x).
  conf: not stated · class: meas (note: "measured") · holds: engineered: two laboratory enrichment consortia · src: nelsonBiasesGenomeReconstruction2020 · trail: H1-02 §2.4 · from: H1-02:B-0067, H1-02:B-0068, H1-02:B-0070
- **content-loss.6** Regions not binned were enriched in repeats, atypical composition, rRNAs, tRNAs, transposases and genes of unknown function, and two plasmids were missed entirely.
  conf: not stated · class: meas (note: "measured") · holds: engineered: curated MAGs from two laboratory enrichment consortia against ten isolate genomes from the same cultures · src: nelsonBiasesGenomeReconstruction2020 · trail: H1-02 §2.4 · from: H1-02:B-0067, H1-02:B-0069, H1-02:B-0070
- **content-loss.7** Nelson et al. conclude that reconstructions above 90% completeness "are likely to effectively represent organismal function", while uneven plasmid distribution "can lead to incorrect inferences"; the review counts the conclusion as a bounding fact, but an engineered one.
  conf: not stated · class: meas (note: "measured") · holds: engineered: two laboratory enrichment consortia · src: nelsonBiasesGenomeReconstruction2020 · trail: H1-02 §2.4, §2.6 · from: H1-02:B-0067, H1-02:B-0070, H1-02:B-0105
- **content-loss.8** A companion analysis of Tara Oceans MAGs, inferred from composition statistics against unrelated RefSeq genomes, found lower repeat content in MAGs, consistent with the same exclusion operating in natural marine data.
  conf: not stated · class: deriv (note: "inferred from composition statistics") · holds: natural marine (Tara Oceans MAGs); against unrelated RefSeq genomes, not isolates from the same samples · src: nelsonBiasesGenomeReconstruction2020 · trail: H1-02 §2.4 · from: H1-02:B-0071, H1-02:B-0072
- **content-loss.9** Across 12 assembler and binner combinations, 82% to 94% of chromosomes were recovered, against 38% to 44% of genomic islands and 1% to 29% of plasmids.
  conf: not stated · class: model (note: "modelled") · holds: a simulated 30-genome short-read metagenome · src: maguireMetagenomeAssembledGenomeBinning2020 · trail: H1-02 §2.4 · from: H1-02:B-0073..0075
- **content-loss.10** No plasmid-borne AMR or virulence gene was binned correctly.
  conf: not stated · class: model (note: "modelled") · holds: a simulated 30-genome short-read metagenome · src: maguireMetagenomeAssembledGenomeBinning2020 · trail: H1-02 §2.4 · from: H1-02:B-0073, H1-02:B-0075
- **content-loss.11** Most binners lose plasmids.
  conf: not stated · class: model (note: "modelled") · holds: the CAMI II benchmark · src: meyerCriticalAssessmentMetagenome2022 · trail: H1-02 §2.4 · from: H1-02:B-0076
- **content-loss.12** Checked against a PacBio HiFi assembly of the same system, only 24 of 614 long-read bins had at least half their 1 kb segments fully recovered by short reads, while 490 had at least half not recovered.
  conf: not stated · class: meas (note: "measured") · holds: natural soil: one biocrust community, one site; the reference is long-read bins, not isolates; the review's only natural soil evidence · src: bergComparisonShortreadLongread2025 · trail: H1-02 §2.4 · from: H1-02:B-0077..0079, H1-02:B-0081
- **content-loss.13** Segments missed by short-read assembly were low-coverage or came from populations with high sequence variation, and they were enriched in mobile-element and defence functions; the authors conclude that short-read metagenomes "can possibly underestimate the diversity of these genome regions".
  conf: not stated · class: meas (note: "measured") · holds: natural soil: one biocrust community, one site; short-read assemblies against a PacBio HiFi assembly of the same system · src: bergComparisonShortreadLongread2025 · trail: H1-02 §2.4, §3.3 · from: H1-02:B-0078, H1-02:B-0080, H1-02:B-0081, H1-02:B-0139
- **content-loss.14** The soil short-read loss of variable regions concerns assembly, not the gene content of binned genomes compared across samples, so it is indirect support only for soils.
  conf: not stated · class: not stated · holds: one natural biocrust soil · src: bergComparisonShortreadLongread2025 · trail: H1-02 §2.4, §Verdict as delivered, §5. Verdicts · from: H1-02:B-0082, H1-02:A-005, H1-02:A-026
- **content-loss.15** Transposase copies fell at the breakpoints of short-read assemblies of P. copri.
  conf: not stated · class: not stated · holds: qualitative only; given in the reference list and not cited in the body for any figure · src: mossCompleteClosedBacterial2020 · trail: H1-02 §References · from: H1-02:R-0120..0122

### contamination-gain: Content gained in recovery (contamination and chimerism)
needs: mag-recovery, completeness-estimates

- **contamination-gain.1** MAG-specific genes were 2.35% to 26.41% of MAG gene content (mean 14.42%).
  conf: single (note: "SINGLE SOURCE") · class: not stated · holds: natural human gut; MaxBin 2.0 MAGs against isolate genomes from the same diarrhoeal stool samples; one species in one low-diversity host environment · src: mezitiReliabilityMetagenomeassembledGenomes2021 · trail: H1-02 §2.1 · from: H1-02:B-0032, H1-02:B-0039, H1-02:B-0042
- **contamination-gain.2** Sequence not classified as Enterobacteriaceae averaged 4.4% of the MAGs, above the MiGA contamination estimates (0.9% to 2.7%).
  conf: single (note: "SINGLE SOURCE") · class: not stated · holds: natural human gut; MaxBin 2.0 MAGs from diarrhoeal stool samples; one species in one low-diversity host environment · src: mezitiReliabilityMetagenomeassembledGenomes2021 · trail: H1-02 §2.1 · from: H1-02:B-0032, H1-02:B-0040, H1-02:B-0042
- **contamination-gain.3** Of 86 Lachnospiraceae genes that differed in prevalence between cirrhosis cases and controls, 33 (38%) were probable contaminants from disease-associated genera.
  conf: single (critic: C-051) · class: meas (note: "measured") · holds: natural human gut; one cirrhosis case-control cohort re-analysed with UHGG/MIDAS2 pangenomes; one family, Lachnospiraceae; the differential calls come from MIDAS2 read mapping to a reference pangenome that was partly contaminated, not from comparing genomes recovered from different samples · src: majernikSmallAmountsMisassembly2025 · trail: H1-02 §2.2, §Adversarial · from: H1-02:B-0045, H1-02:B-0046, H1-02:B-0048, H1-02:C-051, H1-02:C-082, H1-02:C-083
- **contamination-gain.4** Twenty-six of the 33 contaminant genes came from single assemblies with a mean CheckM contamination of 0.22%, and GUNC flagged none of them: the contaminants sat below 5% CheckM contamination.
  conf: not stated · class: not stated · holds: natural human gut; one cirrhosis case-control cohort (UHGG/MIDAS2 pangenomes); the critic confirms the figure in full text · src: majernikSmallAmountsMisassembly2025 · trail: H1-02 §2.2, §Adversarial · from: H1-02:B-0045..0047, H1-02:C-092
- **contamination-gain.5** In the Lachnospira eligens pangenome, 22% of accessory genes had lineage-discordant annotation, against 7.6% when only isolate-derived genes were counted.
  conf: single (note: "SINGLE SOURCE") · class: meas (note: "measured") · holds: natural human gut; one study, one disease contrast (a cirrhosis case-control cohort, UHGG/MIDAS2 pangenomes) · src: majernikSmallAmountsMisassembly2025 · trail: H1-02 §2.2 · from: H1-02:B-0045, H1-02:B-0048
- **contamination-gain.6** A quick re-run on Bacteroides thetaiotaomicron gave 30 genes in the same data set.
  conf: not stated · class: not stated · holds: the same cirrhosis cohort data set; the critic's reading of the paper · src: majernikSmallAmountsMisassembly2025 · trail: H1-02 §Adversarial · from: H1-02:C-051
- **contamination-gain.7** Contamination of a reference pangenome produced false differential gene prevalence between sample groups; the calls come from read mapping to UHGG, not from comparing recovered genomes.
  conf: single (critic: C-003) · class: not stated · holds: natural human gut; one cirrhosis cohort; MIDAS2 read mapping to a partly contaminated reference pangenome · src: majernikSmallAmountsMisassembly2025 · trail: H1-02 §critic, §Adversarial · from: H1-02:C-003, H1-02:C-018, H1-02:C-051, H1-02:C-081..083
- **contamination-gain.8** After refinement of a composite Saccharibacteria MAG, a pangenome built with other Saccharibacteria genomes gained seven times as many single-copy core genes.
  conf: not stated · class: meas (note: "measured") · holds: natural; co-assembled oral plaque metagenomes; three MAGs; a letter · src: shaiberCompositeMetagenomeAssembledGenomes2019 · trail: H1-02 §2.2 · from: H1-02:B-0056, H1-02:B-0057
- **contamination-gain.9** GUNC flagged 15.1% to 29.9% of CheckM-prefiltered human gut MAG catalogues as chimeric at genus level or above.
  conf: not stated · class: meas (note: "The study measures chimerism") · holds: natural human gut MAG catalogues; the study measures chimerism, not called gene content; the critic: not re-opened at synthesis, resting on agent reads · src: orakovGUNCDetectionChimerism2021 · trail: H1-02 §2.2, §3.1 · from: H1-02:B-0058, H1-02:B-0061, H1-02:B-0123, H1-02:C-093, H1-02:B-0178
- **contamination-gain.10** In the multi-habitat GMGC set, GUNC flagged 9.4% of MIMAG high-quality MAGs and 20.5% of genomes passing CheckM's contamination threshold of under 5%.
  conf: not stated · class: meas (note: "The study measures chimerism") · holds: natural, multi-habitat (GMGC); chimerism, not called gene content · src: orakovGUNCDetectionChimerism2021 · trail: H1-02 §2.2 · from: H1-02:B-0058, H1-02:B-0059, H1-02:B-0061
- **contamination-gain.11** In one chimerism survey (Orakov et al.) and one species-level case study (Majernik et al.), genomes that passed the contamination filters in use still carried chimeric or contaminant material.
  conf: not stated · class: not stated · holds: human gut and the multi-habitat GMGC set (Orakov et al.); one cirrhosis cohort, Lachnospiraceae (Majernik et al.) · src: orakovGUNCDetectionChimerism2021, majernikSmallAmountsMisassembly2025 · trail: H1-02 §2.2, §Adversarial · from: H1-02:B-0045, H1-02:B-0058, H1-02:B-0059, H1-02:B-0062, H1-02:C-048, H1-02:C-051

### gene-class-specificity: Gene classes lost selectively (ribosomal protein genes, CRISPR arrays, transposases)
needs: content-loss

- **gene-class-specificity.1** Core ribosomal protein genes "could be missing in more than 20-40% of near-complete" MAGs in four of five short-read catalogues (seawater, human gut, chicken gut, rice phyllosphere).
  conf: not stated · class: meas (note: "measured") · holds: natural; more than 190,000 MAGs; short-read catalogues; the critic confirms the figure in full text · src: miseUnexpectedAbsenceRibosomal2022 · trail: H1-02 §2.2, §Adversarial · from: H1-02:B-0050, H1-02:B-0051, H1-02:B-0054, H1-02:C-092
- **gene-class-specificity.2** The ribosomal-protein deficit was absent from the GEM catalogue and from long-read or hybrid MAGs.
  conf: not stated · class: meas (note: "measured") · holds: natural; more than 190,000 MAGs across catalogues · src: miseUnexpectedAbsenceRibosomal2022 · trail: H1-02 §2.2 · from: H1-02:B-0050, H1-02:B-0052, H1-02:B-0054
- **gene-class-specificity.3** Raw reads carried the ribosomal protein genes, and single-amplified genomes did not show the deficit, so the authors locate the loss at tetranucleotide-based binning.
  conf: not stated · class: meas (note: "measured") · holds: natural; MAG catalogues with their raw reads and single-amplified genomes · src: miseUnexpectedAbsenceRibosomal2022 · trail: H1-02 §2.2 · from: H1-02:B-0050, H1-02:B-0053, H1-02:B-0054
- **gene-class-specificity.4** Against phylogenetically close RefSeq genomes (not the same strains), CRISPR arrays and transposases were depleted in MAGs above 90% completeness, while glycolysis genes were not.
  conf: not stated · class: meas (note: "measured") · holds: natural MAGs above 90% completeness; the reference is close RefSeq genomes, not the same strains · src: miseUnexpectedAbsenceRibosomal2022 · trail: H1-02 §2.2 · from: H1-02:B-0054
- **gene-class-specificity.5** The artefact is gene-class specific and passes a completeness filter, across seawater, gut, chicken gut and phyllosphere catalogues.
  conf: not stated · class: not stated · holds: natural short-read MAG catalogues; the review's conclusion from Mise and Iwasaki · src: miseUnexpectedAbsenceRibosomal2022 · trail: H1-02 §2.2, §4. Where, §Verdict as delivered · from: H1-02:B-0055, H1-02:B-0161, H1-02:A-001, H1-02:B-0051
- **gene-class-specificity.6** When 11 soil, seawater and gut metagenomes were assembled at three depths with two assemblers, contigs carrying ribosomal-protein genes were longer "regardless of environmental origins of samples, sequencing depths, and assemblers", and soil gave the shortest contigs. The review left this bounding fact out and cites Mise and Iwasaki only for gut and seawater.
  conf: not stated · class: not stated · holds: natural agricultural and paddy soil, seawater and gut metagenomes; assembly of a specific gene class; the critic's reading of the paper · src: miseUnexpectedAbsenceRibosomal2022 · trail: H1-02 §critic, §Adversarial · from: H1-02:C-013, H1-02:C-068..070, H1-02:C-072
- **gene-class-specificity.7** The ribosomal-protein deficit was absent in Planctomycetota, Verrucomicrobiota and Acidobacteriota.
  conf: not stated · class: not stated · holds: the soil, seawater and gut metagenomes Mise and Iwasaki assembled; the critic's reading of the paper · src: miseUnexpectedAbsenceRibosomal2022 · trail: H1-02 §Adversarial · from: H1-02:C-068, H1-02:C-071

### read-technology: Short against long reads on the same DNA
needs: content-loss, completeness-estimates

- **read-technology.1** In MAG pairs sharing 99% ANI or more from the same DNA extracts, the PacBio HiFi MAG carried more predicted genes than the Illumina MAG (median 1,872 against 1,704, p < 0.05) and was longer (1.98 against 1.85 Mbp), while CheckM completeness and contamination did not differ.
  conf: single (note: "SINGLE SOURCE") · class: meas (note: "measured") · holds: natural coastal marine; North Sea DNA extracts, 4 samples, one time series; the number of pairs is given only in a figure; short-read libraries had about 3 times more sequenced bases, so read technology and depth are confounded · src: orellanaComparingGenomesRecovered2023 · trail: H1-02 §2.3, §critic · from: H1-02:B-0063..0065, H1-02:C-004, H1-02:C-049, H1-02:C-001
- **read-technology.2** A 16S rRNA gene was present in 88% of long-read MAGs and 23% of short-read MAGs.
  conf: single (note: "SINGLE SOURCE") · class: meas (note: "measured") · holds: natural coastal marine; the same North Sea DNA extracts sequenced with Illumina and PacBio HiFi · src: orellanaComparingGenomesRecovered2023 · trail: H1-02 §2.3 · from: H1-02:B-0063, H1-02:B-0065, H1-02:C-001
- **read-technology.3** Short-read MAGs carried about 9% fewer predicted genes than long-read MAGs at equal CheckM completeness, a difference invisible to completeness estimates. Short-read libraries had about 3 times more sequenced bases (about 36 Gbp per sample for Illumina against 12 Gbp for PacBio), so read technology and depth are confounded.
  conf: single (critic: C-004) · class: not stated · holds: natural coastal marine; 4 North Sea samples, one time series · src: orellanaComparingGenomesRecovered2023 · trail: H1-02 §2.3, §critic, §Adversarial · from: H1-02:B-0066, H1-02:C-004, H1-02:C-017, H1-02:C-049, H1-02:C-088, H1-02:C-001

### pathway-completeness: Genome incompleteness and pathway (module) completeness
needs: completeness-estimates

- **pathway-completeness.1** A rise in CheckM completeness from 70% to 100% was associated with a 15 ± 10% increase in DRAM KEGG module fullness, and the association held above 90% completeness.
  conf: not stated · class: meas (note: "treated here as a measured association") · holds: 11,842 GTDB genomes, a cross-genome regression; the search agents disagreed on its class (measured versus inferred), and the review treats it as a measured association with an inferred causal reading; the note lists it among the sources re-verified in full text, while the critic says it rests on agent reads · src: eisenhoferImpactMicrobialGenome2023 · trail: H1-02 §2.5, §Search record, §Adversarial · from: H1-02:B-0083, H1-02:B-0084, H1-02:B-0087, H1-02:B-0012, H1-02:B-0190, H1-02:B-0191, H1-02:C-093
- **pathway-completeness.2** The association of module fullness with completeness differed by phylum and metabolic domain, with nucleotide metabolism and secondary-metabolite biosynthesis most affected.
  conf: not stated · class: meas (note: "treated here as a measured association") · holds: 11,842 GTDB genomes; DRAM KEGG modules · src: eisenhoferImpactMicrobialGenome2023 · trail: H1-02 §2.5 · from: H1-02:B-0083, H1-02:B-0085, H1-02:B-0087
- **pathway-completeness.3** Because the association is a cross-genome correlation, lineage biology is not fully separated from recovery artefact.
  conf: not stated · class: reading (note: "Reviewer's reading") · holds: the regression of module fullness on completeness across GTDB genomes · src: eisenhoferImpactMicrobialGenome2023 · trail: H1-02 §2.5 · from: H1-02:B-0083, H1-02:B-0086
- **pathway-completeness.4** Random contig subsampling of MAGs from an eight-species mock community shifted functional profiles in proportion to the subsampling.
  conf: not stated · class: model (note: "modelled") · holds: engineered: an eight-species mock community; random, not real, gaps · src: eisenhoferImpactMicrobialGenome2023 · trail: H1-02 §2.5 · from: H1-02:B-0088

### core-genome-inference: Pangenome core and accessory inference from MAGs
needs: content-loss, contamination-gain

- **core-genome-inference.bg1** A bacterial species can be described by a pan-genome: a core genome shared by all isolates plus a dispensable genome of partially shared and strain-specific genes.
  kind: background · ref: tettelinGenomeAnalysisMultiple2005 · check: DOI 10.1073/pnas.0506758102 resolves on Crossref; stated in the abstract
- **core-genome-inference.1** Simulated random incompleteness of 1% left only about 36% of strict core families, and contamination inflated the cloud genome; the authors state that random removal "may overestimate" core loss. Simulations of core-genome inference give larger numbers because they strip sequence at random.
  conf: not stated · class: model (note: "Simulations of core-genome inference") · holds: simulations of core-genome inference with sequence removed at random · src: liCriticalAssessmentPangenomic2022 · trail: H1-02 §2.5 · from: H1-02:B-0089..0091
- **core-genome-inference.2** Unadjusted core counts were near zero at a 95% core threshold in a test on 500 E. coli assemblies with completeness drawn from MGnify.
  conf: not stated · class: model (note: "modelled") · holds: 500 E. coli assemblies with completeness drawn from MGnify (CELEBRIMBOR's test) · src: hellewellCELEBRIMBORCoreAccessory2024 · trail: H1-02 §2.5 · from: H1-02:B-0092
- **core-genome-inference.3** Fragmentation of isolate draft assemblies inflates accessory genomes about tenfold in some tools.
  conf: not stated · class: not stated · holds: isolate draft assemblies, not MAGs; the result does not transfer directly · src: tonkinhillProducingPolishedProkaryotic2020 · trail: H1-02 §2.5 · from: H1-02:B-0093, H1-02:B-0094
- **core-genome-inference.4** Dereplication at 96.5% gANI removed 2,228 of 9,175 auxiliary gene clusters in 46 Microcystis MAGs.
  conf: not stated · class: not stated · holds: 46 Microcystis MAGs; a downstream processing step, not a recovery artefact; read in full by one agent and noted only for completeness; no verdict rests on it; the note's not-obtained list calls it an opinion piece, excluded · src: evansDereplicateNotDereplicate2020 · trail: H1-02 §References, §Sources not obtained · from: H1-02:R-0108..0110, H1-02:R-0038..0040, H1-02:B-0190, H1-02:B-0191

### bounding-comparisons: Coarse comparisons of MAGs with isolates that bound the losses
needs: content-loss

- **bounding-comparisons.1** GEM states that MAG sizes matched isolate genomes of the same species, "indicating no major loss of gene content", with one exception, a composite Sinorhizobium MAG.
  conf: not stated · class: assert (critic: C-039) · limit: access and evidence (note: "The statement rests on genome size in a supplementary figure that none of the agents read, not on gene-by-gene comparison") · holds: the GEM catalogue; an author assertion resting on genome size, not gene-by-gene comparison · src: nayfachGenomicCatalogEarths2020 (Supp. Fig. 2 not read) · trail: H1-02 §2.6, §Adversarial · from: H1-02:B-0095..0097, H1-02:C-039
- **bounding-comparisons.2** Near-complete gut MAGs had lengths similar to isolates of the same OTU, and KEGG annotations were concordant per OTU (n = 665); only 14.5% of the MAGs met MIMAG high quality, mostly because rRNA genes were missing.
  conf: not stated · class: deriv (note: "inferred") · holds: natural human gut; aggregated comparisons across different strains; the critic: not re-opened at synthesis, resting on search-agent reads with no cross-agent confirmation · src: nayfachNewInsightsUncultivated2019 · trail: H1-02 §2.6, §Adversarial · from: H1-02:B-0098, H1-02:B-0099, H1-02:C-040, H1-02:C-042, H1-02:C-041, H1-02:R-0130
- **bounding-comparisons.3** 36 MAGs were almost identical by ANI to 18 isolates from the same samples; identity metrics do not test accessory content.
  conf: not stated · class: not stated · holds: human microbiome samples (Pasolli et al.); ANI only; the critic: not re-opened at synthesis, resting on search-agent reads · src: pasolliExtensiveUnexploredHuman2019 · trail: H1-02 §2.6, §Adversarial · from: H1-02:B-0100, H1-02:B-0101, H1-02:C-040, H1-02:C-042, H1-02:C-041, H1-02:R-0144
- **bounding-comparisons.4** In 55 of 78 human-microbiome species, MAG and GenBank persistent genomes differed by less than 1.2-fold and shared 90% of content; in the other 23 species, MAG persistent genomes held 60% of the GenBank set. Shell differences mix biology with recovery.
  conf: not stated · class: meas (note: "measured") · holds: natural, human microbiome; MAGs against GenBank genomes, not same-sample isolates; the critic: an unverified second-hand figure, resting on search-agent reads with no cross-agent confirmation · src: gautreauPPanGGOLiNDepictingMicrobial2020 · trail: H1-02 §2.6, §Adversarial · from: H1-02:B-0102..0104, H1-02:C-040..042
- **bounding-comparisons.5** These bounds are coarse (genome size, ANI, per-OTU annotation overlap) and do not contradict the gene-level losses in Meziti et al.'s comparison with isolate genomes from the same samples, which fall on variable and mobile genes that length and ANI do not register.
  conf: not stated · class: reading (note: "Reviewer's reading") · contrary: one-sided (critic: C-089) · holds: the coarse bounding facts set against the gene-level losses in one isolate comparison; the critic: correctly labelled, but used to discount the bounding evidence in favour of Meziti et al. without a source saying so · src: none (the reviewer's synthesis) · trail: H1-02 §2.6, §2.1, §Adversarial · from: H1-02:B-0106, H1-02:B-0032, H1-02:C-089

### filters-corrections: Filters and corrections, and their validation on real samples
needs: content-loss, contamination-gain, completeness-estimates, pathway-completeness, core-genome-inference

- **filters-corrections.1** A minimum contig length of 1 kb reduced contamination and non-shared genes in real stool MAGs, with small completeness costs; it was not shown to recover missed genes.
  conf: not stated · class: not stated · holds: real stool samples, n = 8 (gut E. coli pairs) · src: mezitiReliabilityMetagenomeassembledGenomes2021 · trail: H1-02 §2.7 · from: H1-02:B-0107..0109, H1-02:A-003
- **filters-corrections.2** A relaxed core threshold (90%) reduced core loss in five real E. coli pairs.
  conf: not stated · class: not stated · holds: real samples, n = 5, gut · src: liCriticalAssessmentPangenomic2022 · trail: H1-02 §2.7 · from: H1-02:B-0110, H1-02:B-0111
- **filters-corrections.3** The contig-length filter and the relaxed core threshold, tested on real data, reduced the artefact without removing it.
  conf: not stated · class: not stated · holds: only n = 8 and n = 5 gut E. coli pairs · src: mezitiReliabilityMetagenomeassembledGenomes2021, liCriticalAssessmentPangenomic2022 · trail: H1-02 §Verdict as delivered, §5. Verdicts · from: H1-02:A-003, H1-02:A-024
- **filters-corrections.4** No filter has been validated on real samples as removing the artefact.
  conf: not stated · class: not stated · search: not stated · holds: the filters tested on real samples, in small gut E. coli sets · src: none (the reviewer's synthesis) · trail: H1-02 §Verdict as delivered, §critic · from: H1-02:A-002, H1-02:C-005, H1-02:A-024
- **filters-corrections.5** Eisenhofer's completeness-model correction (a GLM) was validated on mock-community subsamples and over-corrected some genomes.
  conf: not stated · class: not stated · holds: mock-community subsamples, not natural-sample MAGs · src: eisenhoferImpactMicrobialGenome2023 · trail: H1-02 §2.7 · from: H1-02:B-0112, H1-02:B-0115
- **filters-corrections.6** CELEBRIMBOR was validated on simulations, and its authors state that non-random loss violates its missing-at-random assumption.
  conf: not stated · class: not stated · holds: simulations · src: hellewellCELEBRIMBORCoreAccessory2024 · trail: H1-02 §2.7 · from: H1-02:B-0113
- **filters-corrections.7** mOTUpan was checked against a few closed Prochlorococcus genomes plus bootstraps, and its authors state that genes hard to assemble or bin leave "an inevitable underestimate of the accessory genomes".
  conf: not stated · class: not stated · holds: a few closed Prochlorococcus genomes plus bootstraps · src: buckMOTUpanRobustBayesian2022 · trail: H1-02 §2.7 · from: H1-02:B-0113
- **filters-corrections.8** MetaPathPredict was tested on random annotation downsampling only.
  conf: not stated · class: not stated · holds: random annotation downsampling · src: gellermcgrathPredictingMetabolicModules2024 · trail: H1-02 §2.7 · from: H1-02:B-0114
- **filters-corrections.9** No completeness or missingness correction has been validated against ground truth on natural-sample MAGs with real, non-random gaps.
  conf: not stated · class: search (note: "Not found, with routes") · search: searched, not found (note: "Routes: Europe PMC and WebSearch on mOTUpan, CELEBRIMBOR, MetaPathPredict, completeness bias correction, and missing-at-random pangenome correction") · holds: Eisenhofer's GLM, CELEBRIMBOR, mOTUpan and MetaPathPredict, and the review's search for others; the critic: supported by the named search routes and the authors' own stated assumptions (CELEBRIMBOR, mOTUpan) · src: eisenhoferImpactMicrobialGenome2023, hellewellCELEBRIMBORCoreAccessory2024, buckMOTUpanRobustBayesian2022, gellermcgrathPredictingMetabolicModules2024 · trail: H1-02 §2.7, §Search record, §Adversarial · from: H1-02:B-0112, H1-02:B-0115, H1-02:B-0181, H1-02:B-0184, H1-02:B-0185, H1-02:B-0014, H1-02:B-0015, H1-02:C-094
- **filters-corrections.10** Artefacts persist above completeness thresholds: module fullness bias above 90%; ribosomal-protein, CRISPR and transposase deficits above 90%; chimerism in MIMAG high-quality sets; contaminant genes below the 5% contamination threshold. No source showed that a completeness threshold removes the problem.
  conf: not stated · class: not stated · search: not stated · holds: module fullness, ribosomal-protein and mobile-gene deficits, chimerism and contaminant genes, each from one source; the critic: the ribosomal-protein and contaminant figures have direct support in full text, while the module-fullness and chimerism sources rest on agent reads · src: eisenhoferImpactMicrobialGenome2023, miseUnexpectedAbsenceRibosomal2022, orakovGUNCDetectionChimerism2021, majernikSmallAmountsMisassembly2025 · trail: H1-02 §2.7, §5. Verdicts, §Adversarial · from: H1-02:B-0116, H1-02:B-0117, H1-02:A-023, H1-02:C-092, H1-02:C-093
- **filters-corrections.11** Gene-to-species correlation filtering classified contaminants with AUROC 0.97 on real gut data, judged against BLAST rather than ground truth.
  conf: not stated · class: not stated · holds: real gut data (the cirrhosis cohort); the comparison is BLAST, not ground truth · src: majernikSmallAmountsMisassembly2025 · trail: H1-02 §2.7 · from: H1-02:B-0120, H1-02:B-0045

### annotation-coverage: Annotation coverage of recovered genes
needs: mag-recovery

- **annotation-coverage.1** UHGG core genes had KEGG annotation for a median of 69% of genes, while accessory genes had significantly more unknowns.
  conf: not stated · class: meas (note: "These are measured, gut only") · holds: human gut only (UHGG) · src: almeidaUnifiedCatalog2042020 · trail: H1-02 §3.6 · from: H1-02:B-0156, H1-02:B-0158
- **annotation-coverage.2** Orthology-based GO coverage in an infant gut catalogue was 12%, and it favoured Gammaproteobacteria.
  conf: not stated · class: meas (note: "These are measured, gut only") · holds: one infant gut catalogue; the critic: not re-opened at synthesis, resting on search-agent reads · src: marangaComprehensiveFunctionalAnnotation2023 · trail: H1-02 §3.6, §Adversarial · from: H1-02:B-0157, H1-02:B-0158, H1-02:C-040, H1-02:C-042, H1-02:C-041
- **annotation-coverage.3** No source measured how annotation coverage differs between samples or environments for the same lineage.
  conf: not stated · class: search (note: "Not found, with routes") · search: searched, not found (note: "Route: WebSearch on annotation coverage bias for novel lineages") · holds: the review's search; one route only · src: none (a search result) · trail: H1-02 §3.6, §Search record · from: H1-02:B-0159, H1-02:B-0181, H1-02:B-0188, H1-02:B-0189

### artefact-size: How large recovery artefacts in gene or pathway content are (Part A)
needs: content-loss, contamination-gain, read-technology, gene-class-specificity

- **artefact-size.1** Recovery artefacts in the gene or pathway content of related recovered genomes have been measured and are material, but only in natural human gut and, from a single source, coastal marine samples. Part A for gut rests on one isolate-comparison study (n = 8, one species) plus one mechanism-adjacent study; the loss of variable and mobile genes, and contamination-driven gains, were measured directly in those sources.
  conf: single (critic: C-016) · class: not stated · rating: "MEASURED AND MATERIAL" (critic: C-001: only in natural human gut and, from a single source, coastal marine samples) · holds: natural human gut (same-sample isolate pairs, n = 8 E. coli pairs; contamination of differential gene calls) and natural coastal marine (read-technology gene-count difference at equal estimated completeness); the critic: each of the three direct sources is single-source and has caveats the verdict leaves out · src: mezitiReliabilityMetagenomeassembledGenomes2021, majernikSmallAmountsMisassembly2025, orellanaComparingGenomesRecovered2023 · trail: H1-02 §Verdict as delivered, §5. Verdicts, §critic · from: H1-02:A-001, H1-02:A-022, H1-02:A-023, H1-02:C-001, H1-02:C-016, H1-02:C-019
- **artefact-size.2** Effect sizes are not commensurable across the three direct sources: the isolate comparison reports percentages of population core or variable genes, the read-technology study a median gene count, and the contamination study a fraction of differentially prevalent genes; they are reported separately and not pooled.
  conf: not stated · class: not stated · holds: the three direct natural-sample sources: same-sample isolate pairs, contamination-driven differential gene calls and matched read-technology pairs · src: mezitiReliabilityMetagenomeassembledGenomes2021, orellanaComparingGenomesRecovered2023, majernikSmallAmountsMisassembly2025 · trail: H1-02 §4. Where · from: H1-02:B-0160, H1-02:B-0164, H1-02:B-0165
- **artefact-size.3** Each of the three direct sources is single in its setting: two are human gut and one is coastal marine, and they measure different things.
  conf: single (note: "SINGLE SOURCE") · class: not stated · holds: same-sample isolate pairs and contamination-driven differential gene calls (human gut); matched read-technology pairs (coastal marine) · src: mezitiReliabilityMetagenomeassembledGenomes2021, majernikSmallAmountsMisassembly2025, orellanaComparingGenomesRecovered2023 · trail: H1-02 §4. Where, §Adversarial · from: H1-02:B-0160, H1-02:B-0162, H1-02:B-0163, H1-02:C-047
- **artefact-size.4** Removing Meziti et al. would leave Part A as "measured and material" on the contamination and read-technology sources, but would remove the only natural same-sample isolate comparison and every figure for missed core and variable genes, since Li and Yin reuse its data.
  conf: not stated · class: not stated · holds: the review's sensitivity analysis · src: mezitiReliabilityMetagenomeassembledGenomes2021, majernikSmallAmountsMisassembly2025, orellanaComparingGenomesRecovered2023, liCriticalAssessmentPangenomic2022 · trail: H1-02 §5. Verdicts · from: H1-02:A-038, H1-02:B-0160

### sample-dependence: Whether artefact size depends on sample properties (Part B)
needs: artefact-size

- **sample-dependence.1** Part B is the weakest area for gene content: the sample-property dependence that has been measured concerns yield, completeness, chimerism or assembled fraction, not gene content.
  conf: not stated · class: not stated · holds: all sample types in the review · src: none (the reviewer's synthesis) · trail: H1-02 §4. Where, §critic · from: H1-02:B-0166, H1-02:B-0167, H1-02:C-020
- **sample-dependence.2** No study was found measuring how gene-content artefacts between conspecific MAGs scale with community diversity or depth across samples.
  conf: not stated · class: search (note: "Not found, with routes") · search: searched, not found (note: "Routes: WebSearch and Europe PMC on sequencing effort against binning, batch or study effects in MAG catalogues, and soil MAG against depth") · holds: the review's search · src: none (a search result) · trail: H1-02 §Search record · from: H1-02:B-0181, H1-02:B-0186, H1-02:B-0187

### gut-dependence: Human gut (natural)
needs: sample-dependence, contamination-gain, gene-class-specificity

- **gut-dependence.1** In the human gut, dependence of gene or pathway content artefacts on sample properties has not been measured. Proxies (chimerism rate, aligned fraction, ribosomal-protein absence by catalogue) differ between catalogues, but catalogue is confounded with pipeline and sample set, and the review's own Section 4 says these are not gene-content measures: the body supports "not measured for gene content, indirect proxy evidence varies by catalogue".
  conf: not stated · class: not stated · rating: "MEASURED AND SYSTEMATIC for study of origin (pipeline)" (critic: C-007: NOT MEASURED for gene or pathway content) · search: searched, not found (note: "Routes: WebSearch and Europe PMC on sequencing effort against binning, batch or study effects in MAG catalogues, and soil MAG against depth") · holds: natural human gut; none of the three catalogue sources measures artefact size in gene content against a study variable with sample set held constant, apart from aligned fraction, which is split by quality tier · src: orakovGUNCDetectionChimerism2021, almeidaUnifiedCatalog2042020, miseUnexpectedAbsenceRibosomal2022 · trail: H1-02 §critic, §Adversarial, §Verdict as delivered · from: H1-02:C-007, H1-02:C-008, H1-02:C-020, H1-02:C-023, H1-02:C-087, H1-02:A-006, H1-02:B-0186, H1-02:B-0187
- **gut-dependence.2** For the same 1,554 gut samples binned by three studies, conspecific genomes had a median aligned fraction of 94.5% at 90% completeness or more and 86.6% at medium quality, so different pipelines applied to identical reads disagreed on roughly 5% to 13% of aligned sequence, with the gap set by quality tier.
  conf: not stated · class: meas (note: "measured; gene content was not compared") · holds: natural human gut; aligned sequence, not genes; reported by quality tier, not by study · src: almeidaUnifiedCatalog2042020 · trail: H1-02 §3.1, §critic · from: H1-02:B-0121, H1-02:B-0122, H1-02:C-022
- **gut-dependence.3** Chimerism in CheckM-prefiltered gut catalogues ranged from 15.1% to 29.9% by study, about twofold between studies; study of origin is confounded with pipeline and sample set.
  conf: not stated · class: not stated · holds: natural human gut MAG catalogues; chimerism, not gene content · src: orakovGUNCDetectionChimerism2021 · trail: H1-02 §3.1, §critic · from: H1-02:B-0123, H1-02:A-006, H1-02:C-021
- **gut-dependence.4** Ribosomal-protein-gene absence was present or absent depending on the catalogue.
  conf: not stated · class: not stated · holds: natural gut MAG catalogues; catalogue is confounded with pipeline and sample set · src: miseUnexpectedAbsenceRibosomal2022 · trail: H1-02 §3.1, §critic · from: H1-02:B-0124, H1-02:C-008
- **gut-dependence.5** GUNC-flagged chimerism varied by binner, and Kim et al. state that it "did not correlate with sequencing depth": an unquantified sentence from one benchmark, with no reported statistic, figure panel or stated dataset range, and it is unclear which datasets it covers; the chimerism figures shown are gut datasets. It is the only negative result on depth and has no ground truth.
  conf: single (note: "SINGLE SOURCE") · class: assert (critic: C-043) · holds: real gut datasets (the chimerism figures shown); one benchmark of binning tools · src: kimComprehensiveBenchmarkingMetagenomic2026 · trail: H1-02 §3.1, §critic, §Adversarial, §5. Verdicts · from: H1-02:B-0125..0127, H1-02:C-009, H1-02:C-033, H1-02:C-034, H1-02:C-043, H1-02:A-009, H1-02:A-030, H1-02:A-041, H1-02:B-0168
- **gut-dependence.6** Dependence of gene-content artefacts on community diversity and sequencing depth has not been measured in the gut: no gut study measured how gene-content artefacts scale with community diversity.
  conf: not stated · class: search (note: "Not found, with routes") · search: searched, not found (note: "Routes: WebSearch and Europe PMC on sequencing effort against binning, batch or study effects in MAG catalogues, and soil MAG against depth") · holds: natural human gut · src: none (a search result) · trail: H1-02 §3.1, §Verdict as delivered, §5. Verdicts · from: H1-02:A-007, H1-02:A-029, H1-02:B-0128, H1-02:B-0181, H1-02:B-0186, H1-02:B-0187

### marine-dependence: Marine and seawater (natural)
needs: sample-dependence, read-technology, gene-class-specificity

- **marine-dependence.1** In marine samples, dependence of gene content on a sample property has been measured for read technology only, in a single source, and confounded with depth: one study of 4 samples.
  conf: single (critic: C-010) · class: not stated · rating: "MEASURED AND SYSTEMATIC for read technology" (critic: C-024: 'systematic' is too strong for n = 1 study) · holds: natural coastal marine; 4 North Sea samples, one time series · src: orellanaComparingGenomesRecovered2023 · trail: H1-02 §critic, §Adversarial, §Verdict as delivered · from: H1-02:C-010, H1-02:C-024, H1-02:C-049, H1-02:A-010, H1-02:C-001
- **marine-dependence.2** In marine samples, dependence of gene content on diversity or depth has not been measured; the evidence covers MAG yield only.
  conf: not stated · class: search (note: "Not found, with routes") · search: searched, not found (note: "Routes: WebSearch and Europe PMC on sequencing effort against binning, batch or study effects in MAG catalogues, and soil MAG against depth") · holds: natural marine and seawater · src: royaltyTheoreticalSimulationBasedInvestigation2019 · trail: H1-02 §Verdict as delivered, §critic, §5. Verdicts · from: H1-02:A-012, H1-02:A-013, H1-02:C-011, H1-02:A-032, H1-02:B-0181, H1-02:B-0186, H1-02:B-0187, H1-02:A-010, H1-02:A-031, H1-02:C-010
- **marine-dependence.3** In one rarefied surface-ocean data set, MAG yield followed a Gompertz curve (lag 1.2 Gbp) and declined above about 25 Gbp.
  conf: not stated · class: not stated · holds: one surface-ocean data set; yield, not content · src: royaltyTheoreticalSimulationBasedInvestigation2019 · trail: H1-02 §3.2 · from: H1-02:B-0130, H1-02:B-0131
- **marine-dependence.4** The ribosomal-protein deficit disappeared in long-read catalogues, which supports the read-technology dependence across catalogues rather than in matched samples.
  conf: not stated · class: not stated · holds: a cross-catalogue comparison, not matched samples; indirect for gene content · src: miseUnexpectedAbsenceRibosomal2022 · trail: H1-02 §3.2, §Verdict as delivered, §5. Verdicts · from: H1-02:B-0129, H1-02:A-011, H1-02:A-031
- **marine-dependence.5** Removing Orellana et al. would change the marine Part B verdict to "not measured" for gene content, and marine Part A would then rest on Mise and Iwasaki alone.
  conf: not stated · class: not stated · holds: the review's sensitivity analysis · src: orellanaComparingGenomesRecovered2023, miseUnexpectedAbsenceRibosomal2022 · trail: H1-02 §5. Verdicts · from: H1-02:A-039, H1-02:B-0050, H1-02:B-0063

### soil-sediment: Soils and sediments (natural)
needs: sample-dependence, content-loss

- **soil-sediment.1** For soils and sediments, a gene-content comparison between related recovered genomes and a closed or isolate reference has not been measured in the sources found. The critic: the search missed relevant data (Alneberg et al. 2018, a MAG-against-SAG comparison; Mise and Iwasaki's own soil assemblies), so the absence reflects the search more than the literature, and it echoes the absence the brief expected.
  conf: not stated · class: search (note: "No equivalent study was found") · rating: "NOT MEASURED" · search: searched, not found (note: "No equivalent study was found for soil, sediment or any other high-diversity natural environment") · holds: natural soils, sediments and other high-diversity environments; routes: WebSearch and Europe PMC title and abstract queries on MAG against isolate same sample, and long-read sediment comparisons; the closest hit (mangrove long-read, 2023) reported no gene-content difference · src: none (a search result) · trail: H1-02 §1. Scope, §Search record, §critic, §Adversarial · from: H1-02:A-004, H1-02:A-025, H1-02:C-006, H1-02:C-025, H1-02:C-095..097, H1-02:B-0031, H1-02:B-0181..0183
- **soil-sediment.2** In soil, gene or pathway content of related recovered genomes has not been measured; there is indirect recovery-quality evidence only.
  conf: not stated · class: search (note: "Not found, with routes") · rating: "NOT MEASURED IN THIS SETTING" · search: searched, not found (note: "Routes: WebSearch and Europe PMC on sequencing effort against binning, batch or study effects in MAG catalogues, and soil MAG against depth") · holds: natural soil; none of the soil studies measures the gene or pathway content of related genomes recovered from different soil samples · src: none (a search result) · trail: H1-02 §3.3, §Verdict as delivered, §critic · from: H1-02:A-014, H1-02:A-033, H1-02:C-012, H1-02:B-0141, H1-02:B-0181, H1-02:B-0186, H1-02:B-0187
- **soil-sediment.3** Recovery (assembly fraction, MAG yield, bin quality) in soil depends systematically on diversity, depth, habitat and binner, and short-read assembly loss tracks within-sample coverage and population sequence variation.
  conf: not stated · class: meas (note: "All of this is measured and natural") · holds: natural soils; recovery quality, not gene content; the critic: several of the figures behind it are unverified second-hand figures, resting on search-agent reads · src: johansenUnveilingSoilMicrobial2025, sereikaGenomeresolvedLongreadSequencing2025, kimComprehensiveBenchmarkingMetagenomic2026, panDeepSiameseNeural2022, bergComparisonShortreadLongread2025 · trail: H1-02 §3.3, §Verdict as delivered, §5. Verdicts, §Adversarial · from: H1-02:A-015, H1-02:A-034, H1-02:B-0140, H1-02:C-042, H1-02:C-040, H1-02:C-041
- **soil-sediment.4** Danish agricultural soils sequenced to a mean depth of 107 Gb reached 73% Nonpareil coverage in the less diverse clay field against 47% in sandy fields, and reads assembled into contigs longer than 2 kb were 57% (clay) against 27% (sandy); co-assembly raised both.
  conf: not stated · class: meas (note: "All of this is measured and natural") · holds: natural Danish agricultural soils; the critic: not re-opened at synthesis, an unverified second-hand figure resting on search-agent reads · src: johansenUnveilingSoilMicrobial2025 · trail: H1-02 §3.3, §Adversarial · from: H1-02:B-0132..0134, H1-02:B-0140, H1-02:C-040, H1-02:C-041
- **soil-sediment.5** Agricultural soils had the lowest assembled fraction and MAG yield, and coastal samples still yielded more MAGs after depth normalisation.
  conf: not stated · class: meas (note: "All of this is measured and natural") · holds: natural terrestrial habitats, long-read sequencing; n = 3 + 3 for the depth-normalised comparison; the critic: not re-opened at synthesis · src: sereikaGenomeresolvedLongreadSequencing2025 · trail: H1-02 §3.3, §Adversarial · from: H1-02:B-0135, H1-02:B-0140, H1-02:C-040, H1-02:R-0118
- **soil-sediment.6** Rarefaction gave the longest MAG-yield lag for maize soil (6.1 Gbp).
  conf: not stated · class: meas (note: "All of this is measured and natural") · holds: one maize soil data set, rarefied; yield, not content · src: royaltyTheoreticalSimulationBasedInvestigation2019 · trail: H1-02 §3.3, §3.2 · from: H1-02:B-0136, H1-02:B-0130, H1-02:B-0140
- **soil-sediment.7** Most binners struggled to recover high-quality soil genomes at depths comparable to gut and ocean.
  conf: not stated · class: meas (note: "All of this is measured and natural") · holds: natural soil, gut and ocean data in one benchmark of binning tools · src: kimComprehensiveBenchmarkingMetagenomic2026 · trail: H1-02 §3.3 · from: H1-02:B-0137, H1-02:B-0140
- **soil-sediment.8** SemiBin's gains over other binners were largest in soil.
  conf: not stated · class: meas (note: "All of this is measured and natural") · holds: microbiome datasets across different environments; the critic: not re-opened at synthesis · src: panDeepSiameseNeural2022 · trail: H1-02 §3.3, §Adversarial · from: H1-02:B-0138, H1-02:B-0140, H1-02:C-040, H1-02:R-0161
- **soil-sediment.9** For sediments, the only evidence is one estuarine sediment rarefaction (MAG yield; lag 3.7 Gbp, lowest maximum yield) and habitat-level yield for coastal sediments; nothing was found on content artefacts.
  conf: not stated · class: search (note: "Nothing was found on content artefacts") · rating: "NOT MEASURED IN THIS SETTING" · search: searched, not found (note: "Nothing was found on content artefacts") · holds: natural sediments; MAG yield only; the critic: deep-sea, freshwater and estuarine sediment long-read against short-read comparisons, and sediment SAG-MAG comparisons, were not searched by name · src: royaltyTheoreticalSimulationBasedInvestigation2019, sereikaGenomeresolvedLongreadSequencing2025 · trail: H1-02 §3.4, §Verdict as delivered, §5. Verdicts, §Adversarial · from: H1-02:B-0144, H1-02:B-0145, H1-02:A-016, H1-02:A-017, H1-02:A-035, H1-02:C-077, H1-02:C-078
- **soil-sediment.10** A long-read mangrove sediment study compares MAG counts and collinearity between Illumina, PacBio and hybrid assemblies and reports no gene-content difference.
  conf: not stated · class: not stated · holds: mangrove sediments; full text obtained but not used as a finding; the critic: the review did not report its gene-content statements · src: zhangLongreadAssembledMetagenomic2023 · trail: H1-02 §Sources not obtained, §Search record, §Adversarial · from: H1-02:R-0057, H1-02:R-0058, H1-02:R-0068, H1-02:R-0069, H1-02:B-0183, H1-02:C-079
- **soil-sediment.11** No Part B verdict in soil or sediment depends on any single source, because none reaches gene content.
  conf: not stated · class: not stated · holds: the review's sensitivity analysis · src: none (the reviewer's synthesis) · trail: H1-02 §5. Verdicts · from: H1-02:A-042

### engineered-simulated: Engineered systems and simulations (kept separate)
needs: sample-dependence, content-loss

- **engineered-simulated.1** Mean bin completeness fell from 36.9% (marine gold-standard assembly) to 18.2% under high strain diversity, and to 5.2% on MEGAHIT assemblies; genomes with close relatives assembled far worse, and strain diversity degraded completeness and purity.
  conf: not stated · class: model (note: "modelled") · holds: the CAMI II benchmark · src: meyerCriticalAssessmentMetagenome2022 · trail: H1-02 §3.5, §Verdict as delivered · from: H1-02:B-0146, H1-02:B-0147, H1-02:A-018
- **engineered-simulated.2** No clear effect of close relatives was found in a 30-genome community.
  conf: not stated · class: model (note: "modelled") · holds: one low-complexity simulation (30 genomes) · src: maguireMetagenomeAssembledGenomeBinning2020 · trail: H1-02 §3.5, §Verdict as delivered · from: H1-02:B-0148, H1-02:A-019
- **engineered-simulated.3** Completeness correlated with depth at ρ = 0.20 and with taxonomic complexity at ρ = −0.55.
  conf: not stated · class: model (note: "modelled") · holds: Kim et al.'s simulations · src: kimComprehensiveBenchmarkingMetagenomic2026 · trail: H1-02 §3.5 · from: H1-02:B-0149
- **engineered-simulated.4** Depth effects on true-positive recovery reversed between pipelines around 60 million reads: depth effects are pipeline-dependent.
  conf: not stated · class: model (note: "modelled") · holds: simulations of 69 microbial communities; the critic: not re-opened at synthesis · src: rochaSimulation69Microbial2024 · trail: H1-02 §3.5, §Adversarial · from: H1-02:B-0150, H1-02:A-018, H1-02:C-040, H1-02:R-0170
- **engineered-simulated.5** In one anaerobic digester sample, long reads gave far more high-quality, less fragmented MAGs, and microdiversity increased fragmentation.
  conf: not stated · class: not stated · holds: engineered; one anaerobic digester sample · src: sereikaOxfordNanoporeR102022 · trail: H1-02 §3.5 · from: H1-02:B-0151, H1-02:B-0153
- **engineered-simulated.6** Long-read activated-sludge MAGs carried full rRNA operons in 91.3% of cases.
  conf: not stated · class: not stated · holds: engineered; activated sludge · src: singletonConnectingStructureFunction2021 · trail: H1-02 §3.5 · from: H1-02:B-0152, H1-02:B-0153
- **engineered-simulated.7** In engineered bioreactors, read technology changes contiguity and rRNA recovery.
  conf: not stated · class: not stated · holds: one anaerobic digester sample and activated sludge · src: sereikaOxfordNanoporeR102022, singletonConnectingStructureFunction2021 · trail: H1-02 §Verdict as delivered, §3.5 · from: H1-02:A-020, H1-02:B-0151..0153
- **engineered-simulated.8** Multi-sample binning identified 22% to 30% more potential ARG hosts than single-sample binning, so processing mode alone changes how many genomes carry an annotated trait.
  conf: not stated · class: meas (note: "measured; mixed natural and engineered") · holds: real marine, cheese, gut and sludge data; the critic: an unverified second-hand figure, resting on search-agent reads with no cross-agent confirmation · src: hanBenchmarkingMetagenomicBinning2025 · trail: H1-02 §3.5, §Adversarial · from: H1-02:B-0154, H1-02:B-0155, H1-02:C-040, H1-02:C-041
- **engineered-simulated.9** In simulations and engineered systems, strain diversity and read technology have systematic effects, with one null for close relatives; these do not answer the question for natural samples.
  conf: not stated · class: not stated · rating: "MEASURED AND SYSTEMATIC in simulations" · holds: simulations and engineered bioreactors; the critic accepts this verdict as stated · src: meyerCriticalAssessmentMetagenome2022, rochaSimulation69Microbial2024, sereikaOxfordNanoporeR102022, singletonConnectingStructureFunction2021, maguireMetagenomeAssembledGenomeBinning2020 · trail: H1-02 §Verdict as delivered, §5. Verdicts, §critic · from: H1-02:A-018, H1-02:A-021, H1-02:A-036, H1-02:A-037, H1-02:C-014, H1-02:A-020

## Do not say

- **dns.1** "Meziti et al. found true recovery 16.9% to 20.4% below the completeness estimates."
  why: The two figures are not a range: they are average shortfalls against two estimators, 16.9% against MiGA and 20.4% against CheckM. · instead: completeness-estimates.2 · trail: H1-02 §critic · from: H1-02:B-0119, H1-02:C-026, H1-02:C-027
- **dns.2** "The MAGs had CheckM/MiGA completeness estimates of 81.1% to 97.2%."
  why: The range mixes estimator columns; the paper's text gives MiGA MAG completeness as 81.1% to 95.5%. · instead: completeness-estimates.3 · trail: H1-02 §critic · from: H1-02:B-0033, H1-02:C-028, H1-02:C-029
- **dns.3** "The main mechanism of gene loss in MAGs was mis-binning among co-occurring relatives, not a failure to sequence."
  why: That is the reviewer's inference and over-reads the paper, which attributes the low-identity share of missed genes to sequence divergence from the isolate or to assembly errors, so part of the loss may be biology and not recovery. · instead: content-loss.3 · trail: H1-02 §critic, §Adversarial · from: H1-02:B-0038, H1-02:C-030, H1-02:C-031, H1-02:C-084..086
- **dns.4** "Contamination produced apparent content differences between sample groups of recovered genomes."
  why: The differential calls come from MIDAS2 read mapping to a reference pangenome that was partly contaminated; they are not content differences between genomes recovered from different samples. · instead: contamination-gain.7 · trail: H1-02 §Adversarial · from: H1-02:B-0049, H1-02:C-081..083
- **dns.5** "The contamination filters in common use leave chimeric material in place."
  why: It generalises to the filters in common use from one chimerism survey plus one species-level case study. · instead: contamination-gain.11 · trail: H1-02 §Adversarial · from: H1-02:B-0062, H1-02:C-048
- **dns.6** "A gene-count difference of about 9% between short- and long-read MAGs depended on read technology."
  why: It omits the paper's reported 3-fold difference in sequenced bases between platforms and attributes the effect to technology alone; read technology and depth are confounded. · instead: read-technology.3 · trail: H1-02 §Adversarial · from: H1-02:B-0066, H1-02:C-017, H1-02:C-088
- **dns.7** "Three natural-sample sources that do not depend on each other establish that recovery produces material content differences."
  why: The three sources measure different things in two environments, and each is single in its setting; together they do not establish a field-level finding. · instead: artefact-size.1, artefact-size.3 · trail: H1-02 §Adversarial · from: H1-02:B-0160, H1-02:C-046, H1-02:C-047
- **dns.8** "Only one natural-sample study has ever compared MAGs with isolate genomes of the same lineage from the same sample at gene level."
  why: The review frames it as a structural fact of the literature, but it is a statement about the search, and it omits SAG-referenced comparisons (Alneberg et al. 2018). · instead: mag-recovery.3 · trail: H1-02 §Adversarial · from: H1-02:B-0029, H1-02:C-052
- **dns.9** "In the human gut, gene-content artefacts are measured and systematic for study of origin (pipeline)."
  why: The verdict contradicts the review's own Section 4, which says the measured dependence concerns yield, completeness, chimerism or assembled fraction, not gene content; study of origin is confounded with pipeline and sample set, and aligned fraction is reported by quality tier, not by study. · instead: gut-dependence.1 · trail: H1-02 §critic, §Adversarial · from: H1-02:A-006, H1-02:A-028, H1-02:C-007, H1-02:C-020..023, H1-02:C-087
- **dns.10** "Without Orakov et al., the gut study-of-origin verdict would still be systematic on aligned sequence and ribosomal-protein absence."
  why: It rests on the gut verdict 'measured and systematic for study of origin', which the critic corrects to not measured for gene content, with indirect proxy evidence varying by catalogue. · instead: gut-dependence.1 · trail: H1-02 §critic · from: H1-02:A-040, H1-02:C-020, H1-02:C-023
- **dns.11** "GUNC-estimated chimerism did not correlate with depth across real gut, ocean and soil samples."
  why: The statement is one unquantified sentence in Kim et al. with no reported statistic; the review extends it to real gut, ocean and soil samples, but the chimerism figures shown are gut datasets. · instead: gut-dependence.5 · trail: H1-02 §critic, §Adversarial · from: H1-02:A-008, H1-02:C-033, H1-02:C-034, H1-02:C-050
- **dns.12** "Kim et al. measured that chimerism does not correlate with sequencing depth."
  why: The depth-chimerism statement is a sentence with no statistic, figure panel or stated dataset range: it is asserted-class evidence that the review tagged as a measured negative result. · instead: gut-dependence.5 · trail: H1-02 §Adversarial · from: H1-02:C-043
- **dns.13** "In marine samples, gene-content artefacts are measured and systematic for read technology."
  why: It rests on one study of 4 North Sea samples, one time series, with a depth confound, so 'systematic' is too strong for n = 1 study. · instead: marine-dependence.1 · trail: H1-02 §critic, §Adversarial · from: H1-02:A-010, H1-02:A-031, H1-02:C-024, H1-02:C-049
- **dns.14** "GEM measured no major loss of gene content in its MAGs."
  why: 'No major loss of gene content' is an author assertion: the underlying Supp. Fig. 2 was not read, so the claim is asserted, not measured. · instead: bounding-comparisons.1 · trail: H1-02 §Adversarial · from: H1-02:C-039
- **dns.15** "The gene-content losses measured in gut MAGs also apply to soil MAGs."
  why: The review warns that the gut findings should not be transferred to soil: the setting differs in diversity, coverage and microdiversity, and the direction and size of the difference are unmeasured. · instead: soil-sediment.2 · trail: H1-02 §3.3 · from: H1-02:B-0142, H1-02:B-0143

## Gaps

- **gap.1** Genomes from the same natural sample compared with a non-isolate reference: single-amplified genomes against MAGs, for gene-content overlap. The review treats isolates as the only same-sample reference; Alneberg et al. 2018 aligns SAG-MAG pairs from the same station in brackish Baltic Sea bacterioplankton and reports gene-content overlap and 16S presence. Follow-up: search 'SAG MAG comparison same sample gene content' in marine, freshwater and soil.
  blocks: artefact-size, soil-sediment · origin: critic coverage gap; the stage-2 check names the SAG-against-MAG reference as a route for the follow-up brief · search: not stated · src: alnebergGenomesUncultivatedProkaryotes2018 · from: H1-02:C-064..067, H1-02:B-0020
- **gap.2** Whether ribosomal-protein and other gene-class recovery depends on depth in soil: re-read Mise and Iwasaki's Fig. 3 and Supp. Fig. S1 for soil and depth, and check whether any other study reports gene-class recovery against depth in soil.
  blocks: gene-class-specificity, soil-sediment · origin: critic coverage gap: a bounding fact relevant to Part B soil and depth that the review cites only for gut and seawater · search: not stated · src: miseUnexpectedAbsenceRibosomal2022 · from: H1-02:C-068, H1-02:C-072
- **gap.3** Annotation-coverage bias across lineages, for novel and understudied phyla typical of soils and sediments (Lobb et al. 2020), and studies of KEGG or Pfam annotation rate against phylogenetic novelty in soil MAG catalogues; the review's treatment of differing annotation coverage is gut only.
  blocks: annotation-coverage · origin: critic coverage gap · search: not stated · src: lobbAssessmentGenomeAnnotation2020 · from: H1-02:C-073
- **gap.4** Long-read or HiFi against short-read MAG content in a complex natural host-associated community (sheep and ruminant gut): Bickhart et al. 2022 was not obtained, and an author manuscript may exist; rumen HiFi MAG studies for plasmid and mobile-element content differences.
  blocks: read-technology · origin: critic coverage gap; source not obtained (budget limits) · search: not stated · src: bickhartGeneratingLineageresolvedComplete2022 · from: H1-02:C-074, H1-02:B-0016
- **gap.5** Freshwater and lake natural samples, and hypersaline salterns, are absent from both parts: Puente-Sánchez et al. and Conrad et al. (hypersaline Salinibacter pangenomes) were not obtained. Follow-up: retry full text, and search 'MAG pangenome accessory genes freshwater isolate comparison'.
  blocks: sample-dependence · origin: critic coverage gap; the stage-2 check is triggered by it · search: not stated · src: puentesanchezExploringEnvironmentalIntraspecies2023, conradTowardQuantifyingAdaptive2021 · from: H1-02:C-075, H1-02:B-0018
- **gap.6** How microdiversity or strain heterogeneity in natural samples, measured per population (for example inStrain nucleotide diversity), changes the MAG gene content recovered across samples; only CAMI simulations and Berg et al. touch it. Follow-up: the strain-resolved and population-genomics literature (inStrain, StrainPhlAn, DESMAN, STRONG) for recovered accessory-gene loss against population nucleotide diversity.
  blocks: sample-dependence, soil-sediment · origin: critic coverage gap; the stage-2 check names natural soils for the effect of strain heterogeneity · search: not stated · from: H1-02:C-076, H1-02:B-0018
- **gap.7** Sediments have only yield data: deep-sea, freshwater and estuarine sediment long-read against short-read comparisons, and sediment SAG-MAG comparisons, are needed; the mangrove study's gene-content statements were not reported. Follow-up: 'sediment long-read metagenome MAG gene content short-read comparison'; 'subseafloor SAG MAG'.
  blocks: soil-sediment · origin: critic coverage gap · search: not searched (critic: C-078) · src: zhangLongreadAssembledMetagenomic2023 · from: H1-02:C-077..079
- **gap.8** Proximity-ligation (Hi-C) binning evaluations of plasmid and mobile-element assignment on natural samples (gut, rumen, soil, wastewater), which directly address failure to bin mobile regions, against shotgun-only binning.
  blocks: content-loss · origin: critic coverage gap; the stage-2 check names Hi-C binning of mobile elements as a route · search: not stated · from: H1-02:C-080, H1-02:B-0020
- **gap.9** A follow-up brief on soil and sediment recovery artefacts, sized separately: the routing condition was triggered because the coverage gaps name sample types without direct measurement, and the soil and sediment 'not measured' verdict echoes the brief's expected absence, is partly search-limited, and so reflects the search more than the literature.
  blocks: soil-sediment · origin: the note's stage-2 check (triggered); critic's expectation-echo finding · search: not stated · from: H1-02:B-0017..0020, H1-02:C-091, H1-02:C-095..097
- **gap.10** Whether Li and Yin's 25% core-gene loss in real pairs is stated in the main text or only in Supp. Fig. S14, which no agent read.
  blocks: content-loss · origin: critic full-text breach; supplementary figure not read · search: not stated · src: liCriticalAssessmentPangenomic2022 · from: H1-02:C-035..038, H1-02:R-0070
- **gap.11** Supplementary materials and sources not read: GEM Supp. Fig. 2, Supp. Table 3 and Supplementary Note; UHGG and Pasolli et al. (Table S2, Fig. 7); Nayfach et al. 2019 Extended Data Fig. 3f; Hellewell et al. 2024 Supp. Fig. S6; CAMI I and CheckM2.
  blocks: bounding-comparisons, completeness-estimates · origin: sources not obtained (budget limits; supplementary files not downloaded) · search: not stated · src: nayfachGenomicCatalogEarths2020, pasolliExtensiveUnexploredHuman2019, nayfachNewInsightsUncultivated2019, hellewellCELEBRIMBORCoreAccessory2024, sczyrbaCriticalAssessmentMetagenome2017, chklovskiCheckM2RapidScalable2023 · from: H1-02:B-0016, H1-02:R-0053, H1-02:R-0070
- **gap.12** Figures not re-opened at synthesis and resting on search-agent reads with no cross-agent confirmation, including the Han 22% to 30% ARG-host figure, Johansen's 57% against 27% and 73% against 47%, and Gautreau's 55 of 78 species; several carry weight in the soil Part B indirect evidence.
  blocks: soil-sediment, bounding-comparisons, engineered-simulated · origin: critic: unverified second-hand figures · search: not stated · src: hanBenchmarkingMetagenomicBinning2025, johansenUnveilingSoilMicrobial2025, gautreauPPanGGOLiNDepictingMicrobial2020 · from: H1-02:C-040..042, H1-02:B-0178, H1-02:B-0179
- **gap.13** Which datasets Kim et al.'s depth-chimerism null covers, and whether it has a statistic.
  blocks: gut-dependence · origin: critic: an unquantified sentence from one benchmark · search: not stated · src: kimComprehensiveBenchmarkingMetagenomic2026 · from: H1-02:C-009, H1-02:C-033
- **gap.14** How gene-content artefacts between conspecific MAGs scale with community diversity or depth across natural samples, in any environment.
  blocks: sample-dependence, gut-dependence, marine-dependence, soil-sediment · origin: not found in the review's search · search: searched, not found (note: "Routes: WebSearch and Europe PMC on sequencing effort against binning, batch or study effects in MAG catalogues, and soil MAG against depth") · from: H1-02:B-0186, H1-02:B-0187
- **gap.15** A completeness or missingness correction validated on natural-sample MAGs with non-random gaps against ground truth.
  blocks: filters-corrections · origin: not found in the review's search · search: searched, not found (note: "Routes: Europe PMC and WebSearch on mOTUpan, CELEBRIMBOR, MetaPathPredict, completeness bias correction, and missing-at-random pangenome correction") · from: H1-02:B-0184, H1-02:B-0185
- **gap.16** A soil or sediment study comparing gene content of MAGs with isolate or closed genomes of the same lineage.
  blocks: soil-sediment · origin: not found in the review's search · search: searched, not found (note: "Europe PMC title and abstract queries on MAG against isolate same sample, and long-read sediment comparisons") · from: H1-02:B-0181..0183

## Out of scope

- H1-02:C-015: the critic's record of what it checked (provenance)
- H1-02:C-053..063: reference corrections, applied in Sources
- H1-02:C-090: the critic's quotation of the brief's wording (routing, not a finding)
- H1-02:A-027: a heading in the verdicts, not a finding

## Sources

```bibtex
@article{mezitiReliabilityMetagenomeassembledGenomes2021,
  author = {Meziti, Alexandra and Rodriguez-R, Luis M. and Hatt, Janet K. and Peña-Gonzalez, Angela and Levy, Karen and Konstantinidis, Konstantinos T.},
  title = {The Reliability of Metagenome-Assembled Genomes (MAGs) in Representing Natural Populations: Insights from Comparing MAGs against Isolate Genomes Derived from the Same Fecal Sample},
  journal = {Applied and Environmental Microbiology},
  year = {2021},
  volume = {87},
  number = {6},
  pages = {e02593-20},
  doi = {10.1128/AEM.02593-20},
  note = {access: full_text (re-verified at synthesis via PMC HTML); cited as: H1-02 [1]}
}
@article{liCriticalAssessmentPangenomic2022,
  author = {Li, Tang and Yin, Yanbin},
  title = {Critical assessment of pan-genomic analysis of metagenome-assembled genomes},
  journal = {Briefings in Bioinformatics},
  year = {2022},
  volume = {23},
  number = {6},
  pages = {bbac413},
  doi = {10.1093/bib/bbac413},
  note = {access: full_text (search agents' full-text reads; not re-opened at synthesis; Supp. Fig. S14 not read); cited as: H1-02 [2]}
}
@article{eisenhoferImpactMicrobialGenome2023,
  author = {Eisenhofer, Raphael and Odriozola, Iñaki and Alberdi, Antton},
  title = {Impact of microbial genome completeness on metagenomic functional inference},
  journal = {ISME Communications},
  year = {2023},
  volume = {3},
  number = {1},
  pages = {12},
  doi = {10.1038/s43705-023-00221-z},
  note = {access: full_text (re-verified at synthesis via Europe PMC fullTextXML; the critic says it rests on agent reads); cited as: H1-02 [3]}
}
@article{maguireMetagenomeAssembledGenomeBinning2020,
  author = {Maguire, Finlay and Jia, Baofeng and Gray, Kristen L. and Lau, Wing Yin Venus and Beiko, Robert G. and Brinkman, Fiona S. L.},
  title = {Metagenome-assembled genome binning methods with short reads disproportionately fail for plasmids and genomic Islands},
  journal = {Microbial Genomics},
  year = {2020},
  volume = {6},
  number = {10},
  pages = {e000436},
  doi = {10.1099/mgen.0.000436},
  note = {access: full_text (search agents' full-text reads; not re-opened at synthesis); cited as: H1-02 [4]}
}
@article{nelsonBiasesGenomeReconstruction2020,
  author = {Nelson, William C. and Tully, Benjamin J. and Mobberley, Jennifer M.},
  title = {Biases in genome reconstruction from metagenomic data},
  journal = {PeerJ},
  year = {2020},
  volume = {8},
  pages = {e10119},
  doi = {10.7717/peerj.10119},
  note = {access: full_text (re-verified at synthesis via Europe PMC fullTextXML); cited as: H1-02 [5]}
}
@article{miseUnexpectedAbsenceRibosomal2022,
  author = {Mise, Kazumori and Iwasaki, Wataru},
  title = {Unexpected absence of ribosomal protein genes from metagenome-assembled genomes},
  journal = {ISME Communications},
  year = {2022},
  volume = {2},
  number = {1},
  pages = {118},
  doi = {10.1038/s43705-022-00204-6},
  note = {access: full_text (re-verified at synthesis via Europe PMC fullTextXML); cited as: H1-02 [6]}
}
@article{meyerCriticalAssessmentMetagenome2022,
  author = {Meyer, Fernando and Fritz, Adrian and Deng, Zhi-Luo and Koslicki, David and Lesker, Till Robin and Gurevich, Alexey and Robertson, Gary and Alser, Mohammed and Antipov, Dmitry and Beghini, Francesco and Bertrand, Denis and Brito, Jaqueline J. and Brown, C. Titus and Buchmann, Jan and Buluç, Aydin and Chen, Bo and Chikhi, Rayan and Clausen, Philip T. L. C. and Cristian, Alexandru and Dabrowski, Piotr Wojciech and Darling, Aaron E. and Egan, Rob and Eskin, Eleazar and Georganas, Evangelos and Goltsman, Eugene and Gray, Melissa A. and Hansen, Lars Hestbjerg and Hofmeyr, Steven and Huang, Pingqin and Irber, Luiz and Jia, Huijue and Jørgensen, Tue Sparholt and Kieser, Silas D. and Klemetsen, Terje and Kola, Axel and Kolmogorov, Mikhail and Korobeynikov, Anton and Kwan, Jason and LaPierre, Nathan and Lemaitre, Claire and Li, Chenhao and Limasset, Antoine and Malcher-Miranda, Fabio and Mangul, Serghei and Marcelino, Vanessa R. and Marchet, Camille and Marijon, Pierre and Meleshko, Dmitry and Mende, Daniel R. and Milanese, Alessio and Nagarajan, Niranjan and Nissen, Jakob and Nurk, Sergey and Oliker, Leonid and Paoli, Lucas and Peterlongo, Pierre and Piro, Vitor C. and Porter, Jacob S. and Rasmussen, Simon and Rees, Evan R. and Reinert, Knut and Renard, Bernhard and Robertsen, Espen Mikal and Rosen, Gail L. and Ruscheweyh, Hans-Joachim and Sarwal, Varuni and Segata, Nicola and Seiler, Enrico and Shi, Lizhen and Sun, Fengzhu and Sunagawa, Shinichi and Sørensen, Søren Johannes and Thomas, Ashleigh and Tong, Chengxuan and Trajkovski, Mirko and Tremblay, Julien and Uritskiy, Gherman and Vicedomini, Riccardo and Wang, Zhengyang and Wang, Ziye and Wang, Zhong and Warren, Andrew and Willassen, Nils Peder and Yelick, Katherine and You, Ronghui and Zeller, Georg and Zhao, Zhengqiao and Zhu, Shanfeng and Zhu, Jie and Garrido-Oter, Ruben and Gastmeier, Petra and Hacquard, Stephane and Häußler, Susanne and Khaledi, Ariane and Maechler, Friederike and Mesny, Fantin and Radutoiu, Simona and Schulze-Lefert, Paul and Smit, Nathiana and Strowig, Till and Bremges, Andreas and Sczyrba, Alexander and McHardy, Alice Carolyn},
  title = {Critical Assessment of Metagenome Interpretation: the second round of challenges},
  journal = {Nature Methods},
  year = {2022},
  volume = {19},
  number = {4},
  pages = {429--440},
  doi = {10.1038/s41592-022-01431-4},
  note = {access: full_text (search agents' full-text reads; not re-opened at synthesis); cited as: H1-02 [7]}
}
@article{shaiberCompositeMetagenomeAssembledGenomes2019,
  author = {Shaiber, Alon and Eren, A. Murat},
  title = {Composite Metagenome-Assembled Genomes Reduce the Quality of Public Genome Repositories},
  journal = {mBio},
  year = {2019},
  volume = {10},
  number = {3},
  pages = {e00725-19},
  doi = {10.1128/mBio.00725-19},
  note = {access: full_text (search agents' full-text reads); type: letter; cited as: H1-02 [8]}
}
@article{orakovGUNCDetectionChimerism2021,
  author = {Orakov, Askarbek and Fullam, Anthony and Coelho, Luis Pedro and Khedkar, Supriya and Szklarczyk, Damian and Mende, Daniel R. and Schmidt, Thomas S. B. and Bork, Peer},
  title = {GUNC: detection of chimerism and contamination in prokaryotic genomes},
  journal = {Genome Biology},
  year = {2021},
  volume = {22},
  number = {1},
  pages = {178},
  doi = {10.1186/s13059-021-02393-0},
  note = {access: full_text (search agents' full-text reads; not re-opened at synthesis); cited as: H1-02 [9]}
}
@article{almeidaUnifiedCatalog2042020,
  author = {Almeida, Alexandre and Nayfach, Stephen and Boland, Miguel and Strozzi, Francesco and Beracochea, Martin and Shi, Zhou Jason and Pollard, Katherine S. and Sakharova, Ekaterina and Parks, Donovan H. and Hugenholtz, Philip and Segata, Nicola and Kyrpides, Nikos C. and Finn, Robert D.},
  title = {A unified catalog of 204,938 reference genomes from the human gut microbiome},
  journal = {Nature Biotechnology},
  year = {2021},
  volume = {39},
  number = {1},
  pages = {105--114},
  doi = {10.1038/s41587-020-0603-3},
  note = {access: full_text (search agents' full-text reads; not re-opened at synthesis; UHGG supplementary data not read); the critic: Crossref issued date 2020-07-20 (online), 2021 volume 39(1) for print; cited as: H1-02 [10]}
}
@article{nayfachGenomicCatalogEarths2020,
  author = {Nayfach, Stephen and Roux, Simon and Seshadri, Rekha and Udwary, Daniel and Varghese, Neha and Schulz, Frederik and Wu, Dongying and Paez-Espino, David and Chen, I-Min and Huntemann, Marcel and Palaniappan, Krishna and Ladau, Joshua and Mukherjee, Supratim and Reddy, T. B. K. and Nielsen, Torben and Kirton, Edward and Faria, José P. and Edirisinghe, Janaka N. and Henry, Christopher S. and Jungbluth, Sean P. and Chivian, Dylan and Dehal, Paramvir and Wood-Charlson, Elisha M. and Arkin, Adam P. and Tringe, Susannah G. and Visel, Axel and {IMG/M Data Consortium} and Abreu, Helena and Acinas, Silvia G. and Allen, Eric and Allen, Michelle A. and Alteio, Lauren V. and Andersen, Gary and Anesio, Alexandre M. and Attwood, Graeme and Avila-Magaña, Viridiana and Badis, Yacine and Bailey, Jake and Baker, Brett and Baldrian, Petr and Barton, Hazel A. and Beck, David A. C. and Becraft, Eric D. and Beller, Harry R. and Beman, J. Michael and Bernier-Latmani, Rizlan and Berry, Timothy D. and Bertagnolli, Anthony and Bertilsson, Stefan and Bhatnagar, Jennifer M. and Bird, Jordan T. and Blanchard, Jeffrey L. and Blumer-Schuette, Sara E. and Bohannan, Brendan and Borton, Mikayla A. and Brady, Allyson and Brawley, Susan H. and Brodie, Juliet and Brown, Steven and Brum, Jennifer R. and Brune, Andreas and Bryant, Donald A. and Buchan, Alison and Buckley, Daniel H. and Buongiorno, Joy and Cadillo-Quiroz, Hinsby and Caffrey, Sean M. and Campbell, Ashley N. and Campbell, Barbara and Carr, Stephanie and Carroll, JoLynn and Cary, S. Craig and Cates, Anna M. and Cattolico, Rose Ann and Cavicchioli, Ricardo and Chistoserdova, Ludmila and Coleman, Maureen L. and Constant, Philippe and Conway, Jonathan M. and Mac Cormack, Walter P. and Crowe, Sean and Crump, Byron and Currie, Cameron and Daly, Rebecca and DeAngelis, Kristen M. and Denef, Vincent and Denman, Stuart E. and Desta, Adey and Dionisi, Hebe and Dodsworth, Jeremy and Dombrowski, Nina and Donohue, Timothy and Dopson, Mark and Driscoll, Timothy and Dunfield, Peter and Dupont, Christopher L. and Dynarski, Katherine A. and Edgcomb, Virginia and Edwards, Elizabeth A. and Elshahed, Mostafa S. and Figueroa, Israel and Flood, Beverly and Fortney, Nathaniel and Fortunato, Caroline S. and Francis, Christopher and Gachon, Claire M. M. and Garcia, Sarahi L. and Gazitua, Maria C. and Gentry, Terry and Gerwick, Lena and Gharechahi, Javad and Girguis, Peter and Gladden, John and Gradoville, Mary and Grasby, Stephen E. and Gravuer, Kelly and Grettenberger, Christen L. and Gruninger, Robert J. and Guo, Jiarong and Habteselassie, Mussie Y. and Hallam, Steven J. and Hatzenpichler, Roland and Hausmann, Bela and Hazen, Terry C. and Hedlund, Brian and Henny, Cynthia and Herfort, Lydie and Hernandez, Maria and Hershey, Olivia S. and Hess, Matthias and Hollister, Emily B. and Hug, Laura A. and Hunt, Dana and Jansson, Janet and Jarett, Jessica and Kadnikov, Vitaly V. and Kelly, Charlene and Kelly, Robert and Kelly, William and Kerfeld, Cheryl A. and Kimbrel, Jeff and Klassen, Jonathan L. and Konstantinidis, Konstantinos T. and Lee, Laura L. and Li, Wen-Jun and Loder, Andrew J. and Loy, Alexander and Lozada, Mariana and MacGregor, Barbara and Magnabosco, Cara and Maria da Silva, Aline and McKay, R. Michael and McMahon, Katherine and McSweeney, Chris S. and Medina, Mónica and Meredith, Laura and Mizzi, Jessica and Mock, Thomas and Momper, Lily and Moran, Mary Ann and Morgan-Lang, Connor and Moser, Duane and Muyzer, Gerard and Myrold, David and Nash, Maisie and Nesbø, Camilla L. and Neumann, Anthony P. and Neumann, Rebecca B. and Noguera, Daniel and Northen, Trent and Norton, Jeanette and Nowinski, Brent and Nüsslein, Klaus and O'Malley, Michelle A. and Oliveira, Rafael S. and Maia de Oliveira, Valeria and Onstott, Tullis and Osvatic, Jay and Ouyang, Yang and Pachiadaki, Maria and Parnell, Jacob and Partida-Martinez, Laila P. and Peay, Kabir G. and Pelletier, Dale and Peng, Xuefeng and Pester, Michael and Pett-Ridge, Jennifer and Peura, Sari and Pjevac, Petra and Plominsky, Alvaro M. and Poehlein, Anja and Pope, Phillip B. and Ravin, Nikolai and Redmond, Molly C. and Reiss, Rebecca and Rich, Virginia and Rinke, Christian and Rodrigues, Jorge L. Mazza and Rodriguez-Reillo, William and Rossmassler, Karen and Sackett, Joshua and Salekdeh, Ghasem Hosseini and Saleska, Scott and Scarborough, Matthew and Schachtman, Daniel and Schadt, Christopher W. and Schrenk, Matthew and Sczyrba, Alexander and Sengupta, Aditi and Setubal, Joao C. and Shade, Ashley and Sharp, Christine and Sherman, David H. and Shubenkova, Olga V. and Sierra-Garcia, Isabel Natalia and Simister, Rachel and Simon, Holly and Sjöling, Sara and Slonczewski, Joan and Correa de Souza, Rafael Soares and Spear, John R. and Stegen, James C. and Stepanauskas, Ramunas and Stewart, Frank and Suen, Garret and Sullivan, Matthew and Sumner, Dawn and Swan, Brandon K. and Swingley, Wesley and Tarn, Jonathan and Taylor, Gordon T. and Teeling, Hanno and Tekere, Memory and Teske, Andreas and Thomas, Torsten and Thrash, Cameron and Tiedje, James and Ting, Claire S. and Tully, Benjamin and Tyson, Gene and Ulloa, Osvlado and Valentine, David L. and Van Goethem, Marc W. and VanderGheynst, Jean and Verbeke, Tobin J. and Vollmers, John and Vuillemin, Aurèle and Waldo, Nicholas B. and Walsh, David A. and Weimer, Bart C. and Whitman, Thea and van der Wielen, Paul and Wilkins, Michael and Williams, Timothy J. and Woodcroft, Ben and Woolet, Jamie and Wrighton, Kelly and Ye, Jun and Young, Erica B. and Youssef, Noha H. and Yu, Feiqiao Brian and Zemskaya, Tamara I. and Ziels, Ryan and Woyke, Tanja and Mouncey, Nigel J. and Ivanova, Natalia N. and Kyrpides, Nikos C. and Eloe-Fadrosh, Emiley A.},
  title = {A genomic catalog of Earth's microbiomes},
  journal = {Nature Biotechnology},
  year = {2021},
  volume = {39},
  number = {4},
  pages = {499--509},
  doi = {10.1038/s41587-020-0718-6},
  note = {access: full_text (search agents' full-text reads; not re-opened at synthesis; Supp. Fig. 2, Supp. Table 3 and Supplementary Note not read); cited as: H1-02 [11]; author list as in the Crossref record, including the Osvlado spelling as registered}
}
@article{orellanaComparingGenomesRecovered2023,
  author = {Orellana, Luis H. and Krüger, Karen and Sidhu, Chandni and Amann, Rudolf},
  title = {Comparing genomes recovered from time-series metagenomes using long- and short-read sequencing technologies},
  journal = {Microbiome},
  year = {2023},
  volume = {11},
  number = {1},
  pages = {105},
  doi = {10.1186/s40168-023-01557-3},
  note = {access: full_text (re-verified at synthesis via Europe PMC fullTextXML); cited as: H1-02 [12]}
}
@article{evansDereplicateNotDereplicate2020,
  author = {Evans, Jacob T. and Denef, Vincent J.},
  title = {To Dereplicate or Not To Dereplicate?},
  journal = {mSphere},
  year = {2020},
  volume = {5},
  number = {3},
  pages = {e00971-19},
  doi = {10.1128/mSphere.00971-19},
  note = {access: full_text (read in full by one agent; volume, issue and article number from memory, not confirmed against Crossref); type: opinion piece; not cited in the body; cited as: H1-02 [13]; also listed under Sources not obtained as read in full but not used, a conflict between the note's lists}
}
@article{buckMOTUpanRobustBayesian2022,
  author = {Buck, Moritz and Mehrshad, Maliheh and Bertilsson, Stefan},
  title = {mOTUpan: a robust Bayesian approach to leverage metagenome-assembled genomes for core-genome estimation},
  journal = {NAR Genomics and Bioinformatics},
  year = {2022},
  volume = {4},
  number = {3},
  pages = {lqac060},
  doi = {10.1093/nargab/lqac060},
  note = {access: full_text (search agents' full-text reads; not re-opened at synthesis); cited as: H1-02 [14]}
}
@article{gellermcgrathPredictingMetabolicModules2024,
  author = {Geller-McGrath, David and Konwar, Kishori M. and Edgcomb, Virginia P. and Pachiadaki, Maria and Roddy, Jack W. and Wheeler, Travis J. and McDermott, Jason E.},
  title = {Predicting metabolic modules in incomplete bacterial genomes with MetaPathPredict},
  journal = {eLife},
  year = {2024},
  volume = {13},
  pages = {e85749},
  doi = {10.7554/eLife.85749},
  note = {access: full_text (search agents' full-text reads; not re-opened at synthesis); cited as: H1-02 [15]}
}
@article{royaltyTheoreticalSimulationBasedInvestigation2019,
  author = {Royalty, Taylor M. and Steen, Andrew D.},
  title = {Theoretical and Simulation-Based Investigation of the Relationship between Sequencing Effort, Microbial Community Richness, and Diversity in Binning Metagenome-Assembled Genomes},
  journal = {mSystems},
  year = {2019},
  volume = {4},
  number = {5},
  pages = {e00384-19},
  doi = {10.1128/mSystems.00384-19},
  note = {access: full_text (search agents' full-text reads; not re-opened at synthesis); cited as: H1-02 [16]}
}
@article{sereikaGenomeresolvedLongreadSequencing2025,
  author = {Sereika, Mantas and Mussig, Aaron James and Jiang, Chenjing and Knudsen, Kalinka Sand and Jensen, Thomas Bygh Nymann and Petriglieri, Francesca and Yang, Yu and Jørgensen, Vibeke Rudkjøbing and Delogu, Francesco and Sørensen, Emil Aarre and Nielsen, Per Halkjær and Singleton, Caitlin Margaret and Hugenholtz, Philip and Albertsen, Mads},
  title = {Genome-resolved long-read sequencing expands known microbial diversity across terrestrial habitats},
  journal = {Nature Microbiology},
  year = {2025},
  volume = {10},
  number = {8},
  pages = {2018--2030},
  doi = {10.1038/s41564-025-02062-z},
  note = {access: full_text (search agents' full-text reads; not re-opened at synthesis); cited as: H1-02 [17]}
}
@article{mossCompleteClosedBacterial2020,
  author = {Moss, Eli L. and Maghini, Dylan G. and Bhatt, Ami S.},
  title = {Complete, closed bacterial genomes from microbiomes using nanopore sequencing},
  journal = {Nature Biotechnology},
  year = {2020},
  volume = {38},
  number = {6},
  pages = {701--707},
  doi = {10.1038/s41587-020-0422-6},
  note = {access: full_text (search agents' full-text reads; not re-opened at synthesis); not cited in the body for any figure; cited as: H1-02 [18]}
}
@article{hellewellCELEBRIMBORCoreAccessory2024,
  author = {Hellewell, Joel and Horsfield, Samuel T. and von Wachsmann, Johanna and Gurbich, Tatiana A. and Finn, Robert D. and Iqbal, Zamin and Roberts, Leah W. and Lees, John A.},
  title = {CELEBRIMBOR: core and accessory genes from metagenomes},
  journal = {Bioinformatics},
  year = {2024},
  volume = {40},
  number = {9},
  pages = {btae542},
  doi = {10.1093/bioinformatics/btae542},
  note = {access: full_text (search agents' full-text reads; not re-opened at synthesis; Supp. Fig. S6 not read); cited as: H1-02 [19]}
}
@article{gautreauPPanGGOLiNDepictingMicrobial2020,
  author = {Gautreau, Guillaume and Bazin, Adelme and Gachet, Mathieu and Planel, Rémi and Burlot, Laura and Dubois, Mathieu and Perrin, Amandine and Médigue, Claudine and Calteau, Alexandra and Cruveiller, Stéphane and Matias, Catherine and Ambroise, Christophe and Rocha, Eduardo P. C. and Vallenet, David},
  title = {PPanGGOLiN: Depicting microbial diversity via a partitioned pangenome graph},
  journal = {PLOS Computational Biology},
  year = {2020},
  volume = {16},
  number = {3},
  pages = {e1007732},
  doi = {10.1371/journal.pcbi.1007732},
  note = {access: full_text (search agents' full-text reads; not re-opened at synthesis); cited as: H1-02 [20]}
}
@article{nayfachNewInsightsUncultivated2019,
  author = {Nayfach, Stephen and Shi, Zhou Jason and Seshadri, Rekha and Pollard, Katherine S. and Kyrpides, Nikos C.},
  title = {New insights from uncultivated genomes of the global human gut microbiome},
  journal = {Nature},
  year = {2019},
  volume = {568},
  number = {7753},
  pages = {505--510},
  doi = {10.1038/s41586-019-1058-x},
  note = {access: full_text (search agents' full-text reads; not re-opened at synthesis; Extended Data Fig. 3f not read); cited as: H1-02 [21]}
}
@article{majernikSmallAmountsMisassembly2025,
  author = {Majernik, Stephanie N. and Beaver, Larry and Bradley, Patrick H.},
  title = {Small amounts of misassembly can have disproportionate effects on pangenome-based metagenomic analyses},
  journal = {mSphere},
  year = {2025},
  volume = {10},
  number = {5},
  pages = {e00857-24},
  doi = {10.1128/msphere.00857-24},
  note = {access: full_text (published version read; a bioRxiv preprint also exists); cited as: H1-02 [22]}
}
@article{tonkinhillProducingPolishedProkaryotic2020,
  author = {Tonkin-Hill, Gerry and MacAlasdair, Neil and Ruis, Christopher and Weimann, Aaron and Horesh, Gal and Lees, John A. and Gladstone, Rebecca A. and Lo, Stephanie and Beaudoin, Christopher and Floto, R. Andres and Frost, Simon D. W. and Corander, Jukka and Bentley, Stephen D. and Parkhill, Julian},
  title = {Producing polished prokaryotic pangenomes with the Panaroo pipeline},
  journal = {Genome Biology},
  year = {2020},
  volume = {21},
  number = {1},
  pages = {180},
  doi = {10.1186/s13059-020-02090-4},
  note = {access: full_text (search agents' full-text reads; not re-opened at synthesis); cited as: H1-02 [23]}
}
@article{pellegrinettiRethinkingMetagenomeAssembledGenome2026,
  author = {Pellegrinetti, Thierry Alexandre and Molligan, Joshua and Mendes, Lucas William and Pedrinho, Alexandre and Pérez-López, Edel},
  title = {Rethinking metagenome-assembled genome completeness: are we truly recovering complete genomes?},
  journal = {Frontiers in Microbiology},
  year = {2026},
  volume = {17},
  pages = {1884628},
  doi = {10.3389/fmicb.2026.1884628},
  note = {access: not_obtained (seen only as search snippet; not fetched; the reference list nonetheless reports its content, a conflict between the note's lists); type: opinion article with an illustrative analysis (the not-obtained list: a review, would be SECONDARY); not used for any verdict; cited as: H1-02 [24]}
}
@article{pasolliExtensiveUnexploredHuman2019,
  author = {Pasolli, Edoardo and Asnicar, Francesco and Manara, Serena and Zolfo, Moreno and Karcher, Nicolai and Armanini, Federica and Beghini, Francesco and Manghi, Paolo and Tett, Adrian and Ghensi, Paolo and Collado, Maria Carmen and Rice, Benjamin L. and DuLong, Casey and Morgan, Xochitl C. and Golden, Christopher D. and Quince, Christopher and Huttenhower, Curtis and Segata, Nicola},
  title = {Extensive Unexplored Human Microbiome Diversity Revealed by Over 150,000 Genomes from Metagenomes Spanning Age, Geography, and Lifestyle},
  journal = {Cell},
  year = {2019},
  volume = {176},
  number = {3},
  pages = {649--662.e20},
  doi = {10.1016/j.cell.2019.01.001},
  note = {access: full_text (search agents' full-text reads; not re-opened at synthesis; Table S2 and Fig. 7 supplementary data not read); cited as: H1-02 [25]}
}
@article{bergComparisonShortreadLongread2025,
  author = {Berg, Maureen and Reiter, Taylor and Emerson, Joanne and Brown, C. Titus and Roux, Simon},
  title = {Comparison of short-read and long-read metagenome assemblies in a natural soil community highlights systematic bias in recovery of high-diversity populations},
  journal = {NAR Genomics and Bioinformatics},
  year = {2025},
  volume = {7},
  number = {4},
  pages = {lqaf163},
  doi = {10.1093/nargab/lqaf163},
  note = {access: full_text (re-verified at synthesis via Europe PMC fullTextXML, PMC12634412); cited as: H1-02 [26]}
}
@article{kimComprehensiveBenchmarkingMetagenomic2026,
  author = {Kim, Jungyeon and Kim, Nayeon and Cha, Jun Hyung and Ma, Junyeong and Lee, Insuk},
  title = {Comprehensive benchmarking of metagenomic binning tools reveals key factors for improved genome recovery},
  journal = {Nature Communications},
  year = {2026},
  volume = {17},
  pages = {3467},
  doi = {10.1038/s41467-026-71521-w},
  note = {access: full_text (re-verified at synthesis via Europe PMC fullTextXML, PMC13079874); cited as: H1-02 [27]}
}
@article{johansenUnveilingSoilMicrobial2025,
  author = {Johansen, Pi Lærke and Chatzigiannidou, Ioanna and Berzina, Lelde and Kristiansen, Karsten and Brix, Susanne},
  title = {Unveiling soil microbial diversity through ultra-deep short-read metagenomic sequencing and co-assembly},
  journal = {iMeta},
  year = {2025},
  volume = {4},
  number = {5},
  pages = {e70075},
  doi = {10.1002/imt2.70075},
  note = {access: full_text (search agents' full-text reads; not re-opened at synthesis); cited as: H1-02 [28]}
}
@article{sereikaOxfordNanoporeR102022,
  author = {Sereika, Mantas and Kirkegaard, Rasmus Hansen and Karst, Søren Michael and Michaelsen, Thomas Yssing and Sørensen, Emil Aarre and Wollenberg, Rasmus Dam and Albertsen, Mads},
  title = {Oxford Nanopore R10.4 long-read sequencing enables the generation of near-finished bacterial genomes from pure cultures and metagenomes without short-read or reference polishing},
  journal = {Nature Methods},
  year = {2022},
  volume = {19},
  number = {7},
  pages = {823--826},
  doi = {10.1038/s41592-022-01539-7},
  note = {access: full_text (search agents' full-text reads; not re-opened at synthesis); cited as: H1-02 [29]}
}
@article{singletonConnectingStructureFunction2021,
  author = {Singleton, Caitlin M. and Petriglieri, Francesca and Kristensen, Jannie M. and Kirkegaard, Rasmus H. and Michaelsen, Thomas Y. and Andersen, Martin H. and Kondrotaite, Zivile and Karst, Søren M. and Dueholm, Morten S. and Nielsen, Per H. and Albertsen, Mads},
  title = {Connecting structure to function with the recovery of over 1000 high-quality metagenome-assembled genomes from activated sludge using long-read sequencing},
  journal = {Nature Communications},
  year = {2021},
  volume = {12},
  number = {1},
  pages = {2009},
  doi = {10.1038/s41467-021-22203-2},
  note = {access: full_text (search agents' full-text reads; not re-opened at synthesis); cited as: H1-02 [30]}
}
@article{panDeepSiameseNeural2022,
  author = {Pan, Shaojun and Zhu, Chengkai and Zhao, Xing-Ming and Coelho, Luis Pedro},
  title = {A deep siamese neural network improves metagenome-assembled genomes in microbiome datasets across different environments},
  journal = {Nature Communications},
  year = {2022},
  volume = {13},
  number = {1},
  pages = {2326},
  doi = {10.1038/s41467-022-29843-y},
  note = {access: full_text (search agents' full-text reads; not re-opened at synthesis); cited as: H1-02 [31]}
}
@article{hanBenchmarkingMetagenomicBinning2025,
  author = {Han, Haitao and Wang, Ziye and Zhu, Shanfeng},
  title = {Benchmarking metagenomic binning tools on real datasets across sequencing platforms and binning modes},
  journal = {Nature Communications},
  year = {2025},
  volume = {16},
  number = {1},
  pages = {2865},
  doi = {10.1038/s41467-025-57957-6},
  note = {access: full_text (search agents' full-text reads; not re-opened at synthesis); cited as: H1-02 [32]}
}
@article{parksCheckMAssessingQuality2015,
  author = {Parks, Donovan H. and Imelfort, Michael and Skennerton, Connor T. and Hugenholtz, Philip and Tyson, Gene W.},
  title = {CheckM: assessing the quality of microbial genomes recovered from isolates, single cells, and metagenomes},
  journal = {Genome Research},
  year = {2015},
  volume = {25},
  number = {7},
  pages = {1043--1055},
  doi = {10.1101/gr.186072.114},
  note = {access: not stated (cited as [33] for its simulations, but listed under Sources not obtained as not fetched (budget), known via Eisenhofer 2023 and Orakov 2021 citations: a conflict between the note's lists); cited as: H1-02 [33]; also background (completeness-estimates)}
}
@article{rochaSimulation69Microbial2024,
  author = {Rocha, Ulisses and Kasmanas, Jonas Coelho and Toscan, Rodolfo and Sanches, Danilo S. and Magnusdottir, Stefania and Saraiva, Joao Pedro},
  title = {Simulation of 69 microbial communities indicates sequencing depth and false positives are major drivers of bias in prokaryotic metagenome-assembled genome recovery},
  journal = {PLOS Computational Biology},
  year = {2024},
  volume = {20},
  number = {10},
  pages = {e1012530},
  doi = {10.1371/journal.pcbi.1012530},
  note = {access: full_text (search agents' full-text reads; not re-opened at synthesis); cited as: H1-02 [34]}
}
@article{marangaComprehensiveFunctionalAnnotation2023,
  author = {Maranga, Mary and Szczerbiak, Pawel and Bezshapkin, Valentyn and Gligorijevic, Vladimir and Chandler, Chris and Bonneau, Richard and Xavier, Ramnik J. and Vatanen, Tommi and Kosciolek, Tomasz},
  title = {Comprehensive Functional Annotation of Metagenomes and Microbial Genomes Using a Deep Learning-Based Method},
  journal = {mSystems},
  year = {2023},
  volume = {8},
  number = {2},
  pages = {e01178-22},
  doi = {10.1128/msystems.01178-22},
  note = {access: full_text (search agents' full-text reads; not re-opened at synthesis); cited as: H1-02 [35]}
}
@article{sczyrbaCriticalAssessmentMetagenome2017,
  author = {Sczyrba, Alexander and others},
  title = {Critical Assessment of Metagenome Interpretation: a benchmark of metagenomics software},
  journal = {Nature Methods},
  year = {2017},
  volume = {14},
  number = {11},
  pages = {1063--1071},
  doi = {10.1038/nmeth.4458},
  note = {access: not_obtained (not fetched (budget); Europe PMC fullTextXML empty, PMC blocked; known only via citing papers); listed twice under Sources not obtained; incomplete: author}
}
@article{chklovskiCheckM2RapidScalable2023,
  author = {Chklovski, Alex and Parks, Donovan H. and Woodcroft, Ben J. and Tyson, Gene W.},
  title = {CheckM2: a rapid, scalable and accurate tool for assessing microbial genome quality using machine learning},
  journal = {Nature Methods},
  year = {2023},
  volume = {20},
  number = {8},
  pages = {1203--1212},
  doi = {10.1038/s41592-023-01940-w},
  note = {access: not_obtained (no PMC copy; bioRxiv preprint not fetched (budget)); listed twice under Sources not obtained; title and issue as corrected by the critic (C-062)}
}
@article{chenAccurateCompleteGenomes2020,
  author = {Chen, Lin-Xing and Anantharaman, Karthik and Shaiber, Alon and Eren, A. Murat and Banfield, Jillian F.},
  title = {Accurate and complete genomes from metagenomes},
  journal = {Genome Research},
  year = {2020},
  volume = {30},
  number = {3},
  pages = {315--333},
  doi = {10.1101/gr.258640.119},
  note = {access: full_text (obtained via Europe PMC, PMC7111523, but only skimmed by keyword; no findings extracted); type: mainly a perspective; listed twice under Sources not obtained; not cited}
}
@article{sahebkashafIntegratingCultivationMetagenomics2021,
  author = {Saheb Kashaf, Sara and others},
  title = {Integrating cultivation and metagenomics for a multi-kingdom view of skin microbiome diversity and functions},
  journal = {Nature Microbiology},
  year = {2022},
  volume = {7},
  pages = {169--179},
  doi = {10.1038/s41564-021-01011-w},
  note = {access: not_obtained (Europe PMC fullTextXML empty; PMC HTML not attempted); listed twice under Sources not obtained; incomplete: author, number}
}
@article{voslooEvaluatingIDe2021,
  author = {Vosloo, Solize and Huo, Linxuan and Anderson, Christopher L. and Dai, Zihan and Sevillano, Maria and Pinto, Ameet},
  title = {Evaluating de Novo Assembly and Binning Strategies for Time Series Drinking Water Metagenomes},
  journal = {Microbiology Spectrum},
  year = {2021},
  volume = {9},
  number = {3},
  pages = {e01434-21},
  doi = {10.1128/Spectrum.01434-21},
  note = {access: abstract_only (full text obtained, PMC8567270, but only the abstract and keyword hits read; not used); bibliographic details not Crossref-checked; listed twice under Sources not obtained; not cited}
}
@article{delgadoEvaluatingMetagenomicAssembly2022,
  author = {Delgado, Luis Fernando and Andersson, Anders F.},
  title = {Evaluating metagenomic assembly approaches for biome-specific gene catalogues},
  journal = {Microbiome},
  year = {2022},
  volume = {10},
  pages = {72},
  doi = {10.1186/s40168-022-01259-2},
  note = {access: abstract_only (full text obtained, PMC9074274; only the abstract read; concerns gene catalogues not genome bins; not used); bibliographic details not Crossref-checked; listed twice under Sources not obtained; not cited}
}
@article{conradTowardQuantifyingAdaptive2021,
  author = {Conrad, Roth E. and Viver, Tomeu and Gago, Juan F. and Hatt, Janet K. and Venter, Stephanus N. and Rossello-Mora, Ramon and Konstantinidis, Konstantinos T.},
  title = {Toward quantifying the adaptive role of bacterial pangenomes during environmental perturbations},
  journal = {The ISME Journal},
  year = {2022},
  volume = {16},
  number = {5},
  pages = {1222--1234},
  doi = {10.1038/s41396-021-01149-9},
  note = {access: not_obtained (not in the Europe PMC OA subset; PMC HTML blocked; the bioRxiv preprint seen only through a web-fetch summary)}
}
@article{puentesanchezExploringEnvironmentalIntraspecies2023,
  author = {Puente-Sánchez, Fernando and Hoetzinger, Matthias and Buck, Moritz and Bertilsson, Stefan},
  title = {Exploring environmental intra-species diversity through non-redundant pangenome assemblies},
  journal = {Molecular Ecology Resources},
  year = {2023},
  doi = {10.1111/1755-0998.13826},
  note = {access: not_obtained (no PMC full text; the bioRxiv preprint seen only through a web-fetch summary; published version not attempted); incomplete: volume, pages}
}
@article{gabrielaiteGenAPIToolGene2020,
  author = {Gabrielaite, Migle and Marvig, Rasmus L.},
  title = {GenAPI: a tool for gene absence-presence identification in fragmented bacterial genome sequences},
  journal = {BMC Bioinformatics},
  year = {2020},
  volume = {21},
  pages = {320},
  doi = {10.1186/s12859-020-03657-5},
  note = {access: not_obtained (identified via Europe PMC, PMC7372895, not downloaded or read, time budget); volume and article number from memory, not confirmed against Crossref}
}
@article{parksRecoveryNearly82017,
  author = {Parks, Donovan H. and others},
  title = {Recovery of nearly 8,000 metagenome-assembled genomes substantially expands the tree of life},
  journal = {Nature Microbiology},
  year = {2017},
  volume = {2},
  pages = {1533--1542},
  doi = {10.1038/s41564-017-0012-7},
  note = {access: not_obtained (Europe PMC DOI search, no PMCID); incomplete: author}
}
@article{bickhartGeneratingLineageresolvedComplete2022,
  author = {Bickhart, Derek M. and Kolmogorov, Mikhail and Tseng, Elizabeth and Portik, Daniel M. and Korobeynikov, Anton and Tolstoganov, Ivan and Uritskiy, Gherman and Liachko, Ivan and Sullivan, Shawn T. and Shin, Sung Bong and Zorea, Alvah and Andreu, Victòria Pascal and Panke-Buisse, Kevin and Medema, Marnix H. and Mizrahi, Itzhak and Pevzner, Pavel A. and Smith, Timothy P. L.},
  title = {Generating lineage-resolved, complete metagenome-assembled genomes from complex microbial communities},
  journal = {Nature Biotechnology},
  year = {2022},
  volume = {40},
  pages = {711--719},
  doi = {10.1038/s41587-021-01130-z},
  note = {access: not_obtained (Europe PMC DOI search, no PMCID, not open access); author list from the critic's Crossref record (C-058)}
}
@article{zhangLongreadAssembledMetagenomic2023,
  author = {Zhang, Zhi-Feng and Liu, Li-Rui and Pan, Yue-Ping and Pan, Jie and Li, Meng},
  title = {Long-read assembled metagenomic approaches improve our understanding on metabolic potentials of microbial community in mangrove sediments},
  journal = {Microbiome},
  year = {2023},
  volume = {11},
  pages = {188},
  doi = {10.1186/s40168-023-01630-x},
  note = {access: full_text (obtained via Europe PMC, PMC10464287; not used as a finding); listed twice under Sources not obtained; authors, volume and article number from the critic's Crossref record (C-060, C-061)}
}
@article{alnebergGenomesUncultivatedProkaryotes2018,
  author = {Alneberg, J. and others},
  title = {Genomes from uncultivated prokaryotes: a comparison of metagenome-assembled and single-amplified genomes},
  journal = {Microbiome},
  year = {2018},
  volume = {6},
  pages = {173},
  doi = {10.1186/s40168-018-0550-0},
  note = {access: not stated (named in the critic's coverage gap, PMC6162917; not used by the review); incomplete: author}
}
@article{lobbAssessmentGenomeAnnotation2020,
  author = {Lobb, B. and Tremblay, B. J.-M. and Moreno-Hagelsieb, G. and Doxey, A. C.},
  title = {An assessment of genome annotation coverage across the bacterial tree of life},
  journal = {Microbial Genomics},
  year = {2020},
  volume = {6},
  number = {3},
  doi = {10.1099/mgen.0.000341},
  note = {access: not stated (named in the critic's coverage gap; not used by the review); incomplete: pages}
}
@article{bowersMinimumInformationSingle2017,
  author = {Bowers, Robert M. and Kyrpides, Nikos C. and Stepanauskas, Ramunas and others},
  title = {Minimum information about a single amplified genome (MISAG) and a metagenome-assembled genome (MIMAG) of bacteria and archaea},
  journal = {Nature Biotechnology},
  year = {2017},
  volume = {35},
  number = {8},
  pages = {725--731},
  doi = {10.1038/nbt.3893},
  note = {background (mag-recovery); not from the inputs}
}
@article{tettelinGenomeAnalysisMultiple2005,
  author = {Tettelin, Hervé and Masignani, Vega and Cieslewicz, Michael J. and others},
  title = {Genome analysis of multiple pathogenic isolates of Streptococcus agalactiae: Implications for the microbial pan-genome},
  journal = {Proceedings of the National Academy of Sciences},
  year = {2005},
  volume = {102},
  number = {39},
  pages = {13950--13955},
  doi = {10.1073/pnas.0506758102},
  note = {background (core-genome-inference); not from the inputs}
}
```
