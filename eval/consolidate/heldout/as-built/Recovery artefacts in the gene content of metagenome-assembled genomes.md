---
type: knowledge
title: Recovery artefacts in the gene content of metagenome-assembled genomes
inputs:
  - H1-02: PhD/Proposal/Research/Results/Recovery artefacts in the gene and pathway content of related metagenome-assembled genomes what has been measured, and how it depends on sample properties.md
refs: PhD/Proposal/Refs/Refs.bib
built: 2026-10-22
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
| H1-02 | [[Recovery artefacts in the gene and pathway content of related metagenome-assembled genomes what has been measured, and how it depends on sample properties]] | yes | numbered | no | no | fallback (answers and critique; the note has no labelled citations) |

## Concepts

### pangenome: core and accessory genes of a pangenome
needs: none
- **pangenome.bg1** A species pan-genome comprises a core genome shared by all isolates and a dispensable genome of partially shared and strain-specific genes.
  kind: background · ref: tettelinGenomeAnalysisMultiple2005 · check: DOI 10.1073/pnas.0506758102 resolves on Crossref; stated in the abstract in the Crossref record

### completeness-estimate: completeness and contamination estimates
needs: same-sample-isolate
group: estimate-check
- **completeness-estimate.bg1** CheckM estimates the completeness and contamination of a genome from lineage-specific marker genes.
  kind: background · ref: parksCheckMAssessingQuality2015 · check: DOI 10.1101/gr.186072.114 resolves on Crossref; stated in the abstract in the Crossref record
- **completeness-estimate.1** CheckM simulations found systematic overestimation of completeness under non-redundant contamination, and plasmids and phage were invisible to the estimates.
  conf: not stated · class: model (note: "modelled") · holds: simulations · src: parksCheckMAssessingQuality2015 · trail: H1-02 §2.7 · from: H1-02:B-0118
- **completeness-estimate.2** In the same-sample isolate comparison, true recovery was lower than the completeness assessments of MiGA and CheckM by 16.9% and 20.4% respectively, on average.
  conf: single (note: "single source") · class: meas (note: "measured, natural") · holds: natural human gut, the Meziti et al. E. coli MAG and isolate pairs; two average shortfalls against two estimators, not a range (the critic) · src: mezitiReliabilityMetagenomeassembledGenomes2021 · trail: H1-02 §2.7, §critic · from: H1-02:B-0119, H1-02:C-026, H1-02:C-027

### same-sample-isolate: MAGs against isolate genomes from the same sample
needs: pangenome, completeness-estimate
group: estimate-check
- **same-sample-isolate.1** MaxBin 2.0 MAGs with completeness estimates near 95% captured only 77% of the population core genes and 50% of the variable genes, on average, against isolate genomes from the same diarrhoeal stool samples.
  conf: single (critic: C-002) · class: meas (note: "evidence class: measured") · holds: natural human gut; one species (E. coli), n = 8 pairs, metagenomes 0.21 to 2.8 Gbp; one low-diversity host environment; MiGA MAG completeness 81.1% to 95.5% in the paper's text (the critic); Li and Yin reuse 5 of the same pairs, so not independent · src: mezitiReliabilityMetagenomeassembledGenomes2021 · trail: H1-02 §2.1, §critic, §Adversarial critique · from: H1-02:B-0032, H1-02:B-0036, H1-02:B-0042, H1-02:C-002, H1-02:C-029, H1-02:C-047, H1-02:C-048
- **same-sample-isolate.2** Population core genes missed by the MAG ranged from 11.31% to 34.7% (mean 24.84%).
  conf: single (critic: C-047) · class: not stated · holds: the same eight E. coli MAG and isolate pairs from human stool · src: mezitiReliabilityMetagenomeassembledGenomes2021 · trail: H1-02 §2.1, §Adversarial critique · from: H1-02:B-0034, H1-02:B-0042, H1-02:C-047
- **same-sample-isolate.3** Population-variable genes missed by the MAG ranged from 13.63% to 69.56% (mean 50.17%).
  conf: single (note: "These figures are SINGLE SOURCE") · class: not stated · holds: one species in one low-diversity host environment · src: mezitiReliabilityMetagenomeassembledGenomes2021 · trail: H1-02 §2.1 · from: H1-02:B-0035, H1-02:B-0042
- **same-sample-isolate.4** Genes with low-identity matches plus genes that had been assembled but binned into other Enterobacteriaceae MAGs made up more than 95% of the missed genes.
  conf: single (note: "These figures are SINGLE SOURCE") · class: not stated · holds: one species in one low-diversity host environment · src: mezitiReliabilityMetagenomeassembledGenomes2021 · trail: H1-02 §2.1 · from: H1-02:B-0037, H1-02:B-0042
- **same-sample-isolate.5** The paper attributes the low-identity share of missed genes to sequence divergence from the isolate or to assembly errors, so part of the loss may be biology and not recovery.
  conf: not stated · class: not stated · holds: the critic's reading of the full text of Meziti et al. · src: mezitiReliabilityMetagenomeassembledGenomes2021 · trail: H1-02 §critic, §Adversarial critique · from: H1-02:C-031, H1-02:C-095
- **same-sample-isolate.6** Mis-binned genes were 16% to 71% (core) and 64% to 71% (variable) of the missed genes without homologs.
  conf: not stated · class: not stated · holds: the critic's reading of the full text of Meziti et al. · src: mezitiReliabilityMetagenomeassembledGenomes2021 · trail: H1-02 §critic · from: H1-02:C-032
- **same-sample-isolate.7** On the gain side, MAG-specific genes were 2.35% to 26.41% of MAG gene content (mean 14.42%).
  conf: single (note: "These figures are SINGLE SOURCE") · class: not stated · holds: one species in one low-diversity host environment · src: mezitiReliabilityMetagenomeassembledGenomes2021 · trail: H1-02 §2.1 · from: H1-02:B-0039, H1-02:B-0042
- **same-sample-isolate.8** Sequence not classified as Enterobacteriaceae averaged 4.4% of the MAGs, above the MiGA contamination estimates (0.9% to 2.7%).
  conf: single (note: "These figures are SINGLE SOURCE") · class: not stated · holds: one species in one low-diversity host environment · src: mezitiReliabilityMetagenomeassembledGenomes2021 · trail: H1-02 §2.1 · from: H1-02:B-0040, H1-02:B-0042
- **same-sample-isolate.9** The authors conclude that the quality of MAGs may often be worse than estimated.
  conf: not stated · class: not stated · holds: the authors' conclusion from the eight E. coli pairs · src: mezitiReliabilityMetagenomeassembledGenomes2021 · trail: H1-02 §2.1 · from: H1-02:B-0041
- **same-sample-isolate.10** Mixing five of the same E. coli MAGs, or their paired isolates, with complete genomes, the MAGs lost about 25% of core genes at a 100% core threshold.
  conf: not stated · class: meas (note: "measured; natural; n = 5") · holds: natural human gut, n = 5 pairs reused from Meziti et al., so not independent; the critic: if the 25% comes from Supp. Fig. S14 rather than a main-text statement it is a full-text breach · src: liCriticalAssessmentPangenomic2022 · trail: H1-02 §2.1, §Adversarial critique · from: H1-02:B-0043, H1-02:B-0044, H1-02:C-035..039, H1-02:C-048 · limit: access (note: "a supplementary figure that none of the search agents read")
- **same-sample-isolate.11** The review's search found one natural-sample study that compared MAGs with isolate genomes of the same lineage from the same sample at gene level (eight E. coli pairs from human stool); a second study reused five of those pairs.
  conf: not stated · class: search (critic: C-055) · holds: the review's search routes; the critic: a statement about the search that omits SAG-referenced comparisons (Alneberg et al. 2018) · src: mezitiReliabilityMetagenomeassembledGenomes2021, liCriticalAssessmentPangenomic2022 · trail: H1-02 §1. Scope, §Adversarial critique · from: H1-02:B-0029, H1-02:B-0030, H1-02:C-055

### mimag-quality: MIMAG genome quality standard
needs: completeness-estimate
- **mimag-quality.bg1** MIMAG is a reporting standard for metagenome-assembled genomes of bacteria and archaea that covers assembly quality and estimates of genome completeness and contamination.
  kind: background · ref: bowersMinimumInformationSingle2017 · check: DOI 10.1038/nbt.3893 resolves on Crossref; stated in the abstract in the Crossref record

### chimerism: chimerism and contamination in MAG catalogues
needs: completeness-estimate, mimag-quality
- **chimerism.1** GUNC flagged 15.1% to 29.9% of CheckM-prefiltered human gut MAG catalogues as chimeric at genus level or above, the rate ranging by study.
  conf: not stated · class: not stated · holds: natural human gut catalogues; the study measures chimerism, not called gene content; the critic: study of origin is confounded with pipeline and sample set, and the source rests on agent reads · src: orakovGUNCDetectionChimerism2021 · trail: H1-02 §2.2, §3.1, §critic, §Adversarial critique · from: H1-02:B-0058, H1-02:B-0061, H1-02:B-0123, H1-02:C-021, H1-02:C-102
- **chimerism.2** In the multi-habitat GMGC set, GUNC flagged 9.4% of MIMAG high-quality MAGs and 20.5% of genomes passing CheckM's contamination threshold of under 5%.
  conf: not stated · class: not stated · holds: the multi-habitat GMGC set; the study measures chimerism, not called gene content · src: orakovGUNCDetectionChimerism2021 · trail: H1-02 §2.2 · from: H1-02:B-0059, H1-02:B-0061
- **chimerism.3** CheckM and GUNC contamination estimates correlated at r = 0.2.
  conf: not stated · class: meas (note: "measured; natural") · holds: natural MAG catalogues · src: orakovGUNCDetectionChimerism2021 · trail: H1-02 §2.2 · from: H1-02:B-0060

### contaminated-pangenome: contaminated reference pangenomes and differential gene prevalence
needs: pangenome, chimerism, completeness-estimate
- **contaminated-pangenome.1** In a cirrhosis case-control gut cohort re-analysed with UHGG/MIDAS2 pangenomes, 33 (38%) of 86 Lachnospiraceae genes that differed in prevalence between cases and controls were probable contaminants from disease-associated genera; the differential calls come from read mapping to a partly contaminated reference pangenome, not from comparing recovered genomes.
  conf: single (critic: C-003) · class: not stated · holds: one cirrhosis cohort and one family, Lachnospiraceae (the critic); natural human gut; false differential prevalence, not content differences between genomes recovered from different samples · src: majernikSmallAmountsMisassembly2025 · trail: H1-02 §2.2, §critic, §Adversarial critique · from: H1-02:B-0045, H1-02:B-0046, H1-02:C-003, H1-02:C-018, H1-02:C-054, H1-02:C-091
- **contaminated-pangenome.2** Twenty-six of these contaminant genes came from single assemblies with a mean CheckM contamination of 0.22%, and GUNC flagged none of them.
  conf: not stated · class: not stated · holds: the same cirrhosis cohort; the critic: direct support in full text for contaminants below 5% CheckM contamination that GUNC did not flag · src: majernikSmallAmountsMisassembly2025 · trail: H1-02 §2.2, §Adversarial critique · from: H1-02:B-0047, H1-02:C-101
- **contaminated-pangenome.3** In the Lachnospira eligens pangenome, 22% of accessory genes had lineage-discordant annotation, against 7.6% when only isolate-derived genes were counted.
  conf: single (note: "SINGLE SOURCE") · class: meas (note: "measured; natural") · holds: one study, one disease contrast · src: majernikSmallAmountsMisassembly2025 · trail: H1-02 §2.2 · from: H1-02:B-0048
- **contaminated-pangenome.4** A quick re-run on Bacteroides thetaiotaomicron in the same data set gave 30 genes.
  conf: single (critic: C-054) · class: not stated · holds: the same cirrhosis data set · src: majernikSmallAmountsMisassembly2025 · trail: H1-02 §Adversarial critique · from: H1-02:C-054

### gene-class-loss: gene classes missing from binned MAGs
needs: completeness-estimate
- **gene-class-loss.1** Among more than 190,000 MAGs examined, core ribosomal protein genes could be missing in more than 20-40% of near-complete MAGs in four of five short-read catalogues (seawater, human gut, chicken gut, rice phyllosphere).
  conf: not stated · class: not stated · holds: natural, short-read catalogues compared, not matched samples; the critic: direct support in full text · src: miseUnexpectedAbsenceRibosomal2022 · trail: H1-02 §2.2, §Adversarial critique · from: H1-02:B-0050, H1-02:B-0051, H1-02:C-101
- **gene-class-loss.2** The ribosomal-protein deficit was absent from the GEM catalogue and from long-read or hybrid MAGs, so its presence depended on the catalogue.
  conf: not stated · class: not stated · holds: a cross-catalogue comparison, not matched samples · src: miseUnexpectedAbsenceRibosomal2022 · trail: H1-02 §2.2, §3.1, §3.2, §Verdict as delivered · from: H1-02:B-0052, H1-02:B-0124, H1-02:B-0129, H1-02:A-011
- **gene-class-loss.3** Raw reads carried the ribosomal protein genes and single-amplified genomes did not show the deficit, so the authors locate the loss at tetranucleotide-based binning.
  conf: not stated · class: not stated · holds: the same catalogues · src: miseUnexpectedAbsenceRibosomal2022 · trail: H1-02 §2.2 · from: H1-02:B-0053
- **gene-class-loss.4** Against phylogenetically close RefSeq genomes (not the same strains), CRISPR arrays and transposases were depleted in MAGs above 90% completeness, while glycolysis genes were not.
  conf: not stated · class: meas (note: "measured; natural") · holds: reference genomes not the same strains · src: miseUnexpectedAbsenceRibosomal2022 · trail: H1-02 §2.2 · from: H1-02:B-0054
- **gene-class-loss.5** The artefact is gene-class specific and passes a completeness filter, and Mise and Iwasaki support the gene-class specificity across environments.
  conf: not stated · class: not stated · holds: short-read catalogues from seawater, human gut, chicken gut and rice phyllosphere · src: miseUnexpectedAbsenceRibosomal2022 · trail: H1-02 §2.2, §4. Where · from: H1-02:B-0055, H1-02:B-0161
- **gene-class-loss.6** In 11 soil, seawater and gut metagenomes assembled at three depths with two assemblers, contigs carrying ribosomal-protein genes were longer regardless of environmental origins of samples, sequencing depths, and assemblers.
  conf: not stated · class: not stated · holds: the critic's reading of the full text; a bounding fact relevant to soil and depth that the review omitted, citing the source only for gut and seawater · src: miseUnexpectedAbsenceRibosomal2022 · trail: H1-02 §critic, §Adversarial critique · from: H1-02:C-013, H1-02:C-073, H1-02:C-074, H1-02:C-077
- **gene-class-loss.7** In those assemblies, soil gave the shortest contigs.
  conf: not stated · class: not stated · holds: the critic's reading of the full text · src: miseUnexpectedAbsenceRibosomal2022 · trail: H1-02 §Adversarial critique · from: H1-02:C-075
- **gene-class-loss.8** The ribosomal-protein deficit was absent in Planctomycetota, Verrucomicrobiota and Acidobacteriota.
  conf: not stated · class: not stated · holds: the critic's reading of the full text · src: miseUnexpectedAbsenceRibosomal2022 · trail: H1-02 §Adversarial critique · from: H1-02:C-076

### mobile-region-loss: variable, mobile and repetitive regions lost in recovery
needs: completeness-estimate
- **mobile-region-loss.1** Comparing curated MAGs from two laboratory enrichment consortia with ten isolate genomes from the same cultures, genomes at 10x coverage or more had over 90% of their sequence recovered (85% at 11x; about 40% at 3.9x).
  conf: not stated · class: not stated · holds: engineered, two laboratory enrichment consortia · src: nelsonBiasesGenomeReconstruction2020 · trail: H1-02 §2.4 · from: H1-02:B-0067, H1-02:B-0068
- **mobile-region-loss.2** Not-binned regions were enriched in repeats, atypical composition, rRNAs, tRNAs, transposases and genes of unknown function, and two plasmids were missed entirely.
  conf: not stated · class: not stated · holds: the same two enrichment consortia · src: nelsonBiasesGenomeReconstruction2020 · trail: H1-02 §2.4 · from: H1-02:B-0069
- **mobile-region-loss.3** The authors conclude that reconstructions above 90% completeness are likely to effectively represent organismal function, while uneven plasmid distribution can lead to incorrect inferences.
  conf: not stated · class: meas (note: "measured; engineered") · holds: engineered; a bounding conclusion, but engineered · src: nelsonBiasesGenomeReconstruction2020 · trail: H1-02 §2.4, §2.6 · from: H1-02:B-0070, H1-02:B-0105
- **mobile-region-loss.4** The paper's companion analysis of Tara Oceans MAGs found lower repeat content in MAGs, consistent with the same exclusion operating in natural marine data.
  conf: not stated · class: deriv (note: "inferred from composition statistics") · holds: natural marine; composition statistics against unrelated RefSeq genomes · src: nelsonBiasesGenomeReconstruction2020 · trail: H1-02 §2.4 · from: H1-02:B-0071, H1-02:B-0072
- **mobile-region-loss.5** In a simulated 30-genome short-read metagenome, across 12 assembler and binner combinations, 82% to 94% of chromosomes were recovered, against 38% to 44% of genomic islands and 1% to 29% of plasmids.
  conf: not stated · class: model (note: "simulated a 30-genome short-read metagenome") · holds: one simulated 30-genome community · src: maguireMetagenomeAssembledGenomeBinning2020 · trail: H1-02 §2.4 · from: H1-02:B-0073, H1-02:B-0074
- **mobile-region-loss.6** No plasmid-borne AMR or virulence gene was binned correctly.
  conf: not stated · class: model (note: "modelled; engineered") · holds: the same simulated community · src: maguireMetagenomeAssembledGenomeBinning2020 · trail: H1-02 §2.4 · from: H1-02:B-0075
- **mobile-region-loss.7** CAMI II found that most binners lose plasmids.
  conf: not stated · class: model (note: "modelled") · holds: CAMI II benchmark data · src: meyerCriticalAssessmentMetagenome2022 · trail: H1-02 §2.4 · from: H1-02:B-0076
- **mobile-region-loss.8** In a natural biocrust soil community, short-read assemblies were checked against a PacBio HiFi assembly of the same system: of 614 long-read bins, only 24 had at least half their 1 kb segments fully recovered by short reads, while 490 had at least half not recovered.
  conf: not stated · class: not stated · holds: one site; the reference is long-read bins, not isolates; concerns assembly, not the gene content of binned genomes compared across samples · src: bergComparisonShortreadLongread2025 · trail: H1-02 §2.4 · from: H1-02:B-0077, H1-02:B-0078, H1-02:B-0079, H1-02:B-0081, H1-02:B-0082
- **mobile-region-loss.9** Missed segments were low-coverage or came from populations with high sequence variation, and they were enriched in mobile-element and defence functions.
  conf: not stated · class: not stated · holds: the same biocrust soil, within-sample coverage and population sequence variation · src: bergComparisonShortreadLongread2025 · trail: H1-02 §2.4, §3.3 · from: H1-02:B-0080, H1-02:B-0139
- **mobile-region-loss.10** The authors conclude that short-read metagenomes can possibly underestimate the diversity of these genome regions.
  conf: single (note: "one site") · class: meas (note: "measured; natural; one site") · holds: one natural biocrust soil site; the reference is long-read bins, not isolates · src: bergComparisonShortreadLongread2025 · trail: H1-02 §2.4 · from: H1-02:B-0081

### sequencing-depth: sequencing depth
needs: chimerism, completeness-estimate
- **sequencing-depth.1** One binning benchmark states, in a sentence with no reported statistic, figure panel or stated dataset range, that GUNC-flagged chimerism in real samples did not correlate with sequencing depth; the chimerism figures shown are gut datasets, and it is unclear which datasets the statement covers.
  conf: single (critic: C-053) · class: assert (critic: C-046) · holds: real samples, no ground truth; the review widens it to real gut, ocean and soil samples (the critic); the one explicit negative result on depth in the review, so removing it removes the only negative result on depth · src: kimComprehensiveBenchmarkingMetagenomic2026 · trail: H1-02 §3.1, §4. Where, §Verdict as delivered, §5. Verdicts, §critic, §Adversarial critique · from: H1-02:B-0125, H1-02:B-0126, H1-02:B-0127, H1-02:B-0168, H1-02:A-008, H1-02:A-009, H1-02:A-030, H1-02:A-041, H1-02:C-009, H1-02:C-033, H1-02:C-034, H1-02:C-046, H1-02:C-053
- **sequencing-depth.2** Rarefying one surface-ocean data set, MAG yield followed a Gompertz curve (lag 1.2 Gbp) and declined above about 25 Gbp.
  conf: not stated · class: not stated · holds: natural marine, one data set; concerns yield, not content · src: royaltyTheoreticalSimulationBasedInvestigation2019 · trail: H1-02 §3.2, §Verdict as delivered · from: H1-02:B-0130, H1-02:B-0131, H1-02:A-013
- **sequencing-depth.3** Maize soil gave the longest lag in MAG yield against sequencing effort (6.1 Gbp).
  conf: not stated · class: not stated · holds: natural soil; MAG yield · src: royaltyTheoreticalSimulationBasedInvestigation2019 · trail: H1-02 §3.3 · from: H1-02:B-0136
- **sequencing-depth.4** One estuarine sediment rarefaction gave a lag of 3.7 Gbp and the lowest maximum MAG yield.
  conf: not stated · class: not stated · holds: natural sediment, one data set; MAG yield · src: royaltyTheoreticalSimulationBasedInvestigation2019 · trail: H1-02 §3.4 · from: H1-02:B-0144
- **sequencing-depth.5** In simulations, completeness correlated with depth at ρ = 0.20.
  conf: not stated · class: model (note: "modelled") · holds: Kim et al.'s simulations · src: kimComprehensiveBenchmarkingMetagenomic2026 · trail: H1-02 §3.5 · from: H1-02:B-0149
- **sequencing-depth.6** Depth effects on true-positive recovery reversed between pipelines around 60 million reads.
  conf: not stated · class: model (note: "modelled") · holds: simulated communities · src: rochaSimulation69Microbial2024 · trail: H1-02 §3.5 · from: H1-02:B-0150

### read-technology: long-read against short-read recovery
needs: completeness-estimate, sequencing-depth
- **read-technology.1** Sequencing the same North Sea DNA extracts with Illumina and PacBio HiFi, in MAG pairs sharing 99% ANI or more the long-read MAG carried more predicted genes (median 1,872 against 1,704, p < 0.05) and was longer (1.98 against 1.85 Mbp), while CheckM completeness and contamination did not differ.
  conf: single (critic: C-004) · class: not stated · holds: natural coastal marine, 4 North Sea samples, one time series; the paper reports about 36 Gbp per sample for Illumina against 12 Gbp for PacBio, so read technology and depth are confounded (the critic) · src: orellanaComparingGenomesRecovered2023 · trail: H1-02 §2.3, §critic, §Adversarial critique · from: H1-02:B-0063, H1-02:B-0064, H1-02:C-004, H1-02:C-017, H1-02:C-052
- **read-technology.2** A 16S rRNA gene was present in 88% of long-read MAGs and 23% of short-read MAGs.
  conf: single (note: "SINGLE SOURCE") · class: meas (note: "measured; natural") · holds: the same North Sea DNA extracts; the number of pairs is given only in a figure · src: orellanaComparingGenomesRecovered2023 · trail: H1-02 §2.3 · from: H1-02:B-0065
- **read-technology.3** Short-read MAGs carried about 9% fewer predicted genes than long-read MAGs at equal CheckM completeness, a difference invisible to completeness estimates; the short-read libraries had about 3 times more sequenced bases, so read technology and depth are confounded.
  conf: single (critic: C-004) · class: reading (note: "Reviewer's reading") · holds: natural coastal marine, 4 samples; the review's reading attributed the difference to read technology alone (the critic) · src: orellanaComparingGenomesRecovered2023 · trail: H1-02 §2.3, §critic, §Adversarial critique · from: H1-02:B-0066, H1-02:C-004, H1-02:C-097
- **read-technology.4** In one anaerobic digester sample, long reads gave far more high-quality, less fragmented MAGs.
  conf: not stated · class: not stated · holds: engineered, one sample · src: sereikaOxfordNanoporeR102022 · trail: H1-02 §3.5, §Verdict as delivered · from: H1-02:B-0151, H1-02:B-0153, H1-02:A-020
- **read-technology.5** Long-read activated-sludge MAGs carried full rRNA operons in 91.3% of cases.
  conf: not stated · class: not stated · holds: engineered (activated sludge) · src: singletonConnectingStructureFunction2021 · trail: H1-02 §3.5, §Verdict as delivered · from: H1-02:B-0152, H1-02:B-0153, H1-02:A-020

### pathway-completeness: incompleteness and pathway completeness
needs: completeness-estimate
- **pathway-completeness.1** Regressing DRAM KEGG module fullness on CheckM completeness across 11,842 GTDB genomes, a rise in completeness from 70% to 100% was associated with a 15 ± 10% increase in module fullness, and the association held above 90% completeness.
  conf: not stated · class: meas (note: "treated here as a measured association") · holds: 11,842 GTDB genomes; the search agents disagreed on its class (measured against inferred); a measured association with an inferred causal reading · src: eisenhoferImpactMicrobialGenome2023 · trail: H1-02 §2.5, §Search record · from: H1-02:B-0083, H1-02:B-0084, H1-02:B-0087, H1-02:B-0190
- **pathway-completeness.2** The association differed by phylum and metabolic domain, with nucleotide metabolism and secondary-metabolite biosynthesis most affected.
  conf: not stated · class: not stated · holds: the same 11,842 GTDB genomes · src: eisenhoferImpactMicrobialGenome2023 · trail: H1-02 §2.5 · from: H1-02:B-0085
- **pathway-completeness.3** The association is a cross-genome correlation, so lineage biology is not fully separated from recovery artefact.
  conf: not stated · class: reading (note: "Reviewer's reading") · holds: the same regression · src: eisenhoferImpactMicrobialGenome2023 · trail: H1-02 §2.5 · from: H1-02:B-0086
- **pathway-completeness.4** Random contig subsampling of MAGs from an eight-species mock community shifted functional profiles in proportion to the subsampling.
  conf: not stated · class: model (note: "modelled; engineered") · holds: one eight-species mock community · src: eisenhoferImpactMicrobialGenome2023 · trail: H1-02 §2.5 · from: H1-02:B-0088

### core-genome-inference: core and accessory genome inference from MAGs
needs: pangenome, completeness-estimate
- **core-genome-inference.1** Simulations of core-genome inference give larger numbers than real comparisons because they strip sequence at random.
  conf: not stated · class: not stated · holds: simulated incompleteness · src: none (the reviewer's synthesis) · trail: H1-02 §2.5 · from: H1-02:B-0089
- **core-genome-inference.2** 1% random incompleteness left only about 36% of strict core families, and contamination inflated the cloud genome.
  conf: not stated · class: model (note: "Simulations of core-genome inference") · holds: simulated random incompleteness · src: liCriticalAssessmentPangenomic2022 · trail: H1-02 §2.5 · from: H1-02:B-0089, H1-02:B-0090
- **core-genome-inference.3** The authors state that random removal may overestimate core loss.
  conf: not stated · class: not stated · holds: Li and Yin's simulations · src: liCriticalAssessmentPangenomic2022 · trail: H1-02 §2.5 · from: H1-02:B-0091
- **core-genome-inference.4** CELEBRIMBOR's test on 500 E. coli assemblies with completeness drawn from MGnify found unadjusted core counts near zero at a 95% threshold.
  conf: not stated · class: model (note: "modelled") · holds: 500 E. coli assemblies, completeness drawn from MGnify · src: hellewellCELEBRIMBORCoreAccessory2024 · trail: H1-02 §2.5 · from: H1-02:B-0092
- **core-genome-inference.5** Fragmentation of isolate draft assemblies inflates accessory genomes about tenfold in some tools.
  conf: not stated · class: not stated · holds: isolates, not MAGs; the result does not transfer directly · src: tonkinhillProducingPolishedProkaryotic2020 · trail: H1-02 §2.5 · from: H1-02:B-0093, H1-02:B-0094
- **core-genome-inference.6** After refinement of a composite Saccharibacteria MAG from co-assembled oral plaque metagenomes, a pangenome built with other Saccharibacteria genomes gained seven times as many single-copy core genes.
  conf: not stated · class: meas (note: "measured; natural; three MAGs") · holds: natural oral plaque, three MAGs · src: shaiberCompositeMetagenomeAssembledGenomes2019 · trail: H1-02 §2.2 · from: H1-02:B-0056, H1-02:B-0057

### bounding-comparisons: coarse comparisons of MAGs with isolate genomes
needs: same-sample-isolate, mimag-quality
- **bounding-comparisons.1** GEM states that MAG sizes matched isolate genomes of the same species, indicating no major loss of gene content, with one exception (a composite Sinorhizobium MAG); the statement rests on genome size in a supplementary figure, not on gene-by-gene comparison.
  conf: not stated · class: assert (critic: C-040) · holds: genome size, same species; the supplementary figure was not read · src: nayfachGenomicCatalogEarths2020 · trail: H1-02 §2.6, §Adversarial critique · from: H1-02:B-0095, H1-02:B-0096, H1-02:B-0097, H1-02:C-040, H1-02:C-041, H1-02:C-042 · limit: access (critic: C-042)
- **bounding-comparisons.2** Near-complete gut MAGs had lengths similar to isolates of the same OTU, and KEGG annotations were concordant per OTU (n = 665).
  conf: not stated · class: deriv (note: "(inferred)") · holds: natural human gut; aggregated comparisons across different strains; the critic: not re-opened at synthesis, figures rest on search-agent reads · src: nayfachNewInsightsUncultivated2019 · trail: H1-02 §2.6, §Adversarial critique · from: H1-02:B-0098, H1-02:B-0099, H1-02:C-043
- **bounding-comparisons.3** Only 14.5% of those MAGs met MIMAG high quality, mostly because rRNA genes were missing.
  conf: not stated · class: deriv (note: "(inferred)") · holds: natural human gut · src: nayfachNewInsightsUncultivated2019 · trail: H1-02 §2.6 · from: H1-02:B-0099
- **bounding-comparisons.4** 36 MAGs were almost identical by ANI to 18 isolates from the same samples.
  conf: not stated · class: not stated · holds: human microbiome; identity metrics do not test accessory content; the critic: not re-opened at synthesis · src: pasolliExtensiveUnexploredHuman2019 · trail: H1-02 §2.6, §Adversarial critique · from: H1-02:B-0100, H1-02:B-0101, H1-02:C-043
- **bounding-comparisons.5** In 55 of 78 human-microbiome species, MAG and GenBank persistent genomes differed by less than 1.2-fold and shared 90% of content.
  conf: not stated · class: meas (note: "measured; natural") · holds: human-microbiome species, MAGs against GenBank genomes; shell differences mix biology with recovery; the critic: an unverified second-hand figure · src: gautreauPPanGGOLiNDepictingMicrobial2020 · trail: H1-02 §2.6, §Adversarial critique · from: H1-02:B-0102, H1-02:B-0104, H1-02:C-043, H1-02:C-044
- **bounding-comparisons.6** In the other 23 species, MAG persistent genomes held 60% of the GenBank set.
  conf: not stated · class: meas (note: "measured; natural") · holds: human-microbiome species; shell differences mix biology with recovery · src: gautreauPPanGGOLiNDepictingMicrobial2020 · trail: H1-02 §2.6 · from: H1-02:B-0103, H1-02:B-0104
- **bounding-comparisons.7** These bounds are coarse (genome size, ANI, per-OTU annotation overlap) and do not contradict the gene-level losses in Meziti et al., which fall on variable and mobile genes that length and ANI do not register.
  conf: not stated · class: reading (note: "Reviewer's reading") · holds: the bounding comparisons above; the critic: correctly labelled, but used to discount the bounding evidence in favour of Meziti et al. without a source saying so · src: none (the reviewer's synthesis) · trail: H1-02 §2.6, §Adversarial critique · from: H1-02:B-0106, H1-02:C-098

### filters-corrections: filters and corrections, and their real-sample validation
needs: same-sample-isolate, core-genome-inference, pathway-completeness, contaminated-pangenome, chimerism, gene-class-loss
- **filters-corrections.1** A minimum contig length of 1 kb reduced contamination and non-shared genes in real stool MAGs, with small completeness costs, and was not shown to recover missed genes.
  conf: not stated · class: not stated · holds: real samples, n = 8 · src: mezitiReliabilityMetagenomeassembledGenomes2021 · trail: H1-02 §2.7 · from: H1-02:B-0107, H1-02:B-0108, H1-02:B-0109
- **filters-corrections.2** A relaxed core threshold (90%) reduced core loss in five real E. coli pairs.
  conf: not stated · class: not stated · holds: real samples, n = 5, gut · src: liCriticalAssessmentPangenomic2022 · trail: H1-02 §2.7 · from: H1-02:B-0110, H1-02:B-0111
- **filters-corrections.3** The two filters tested on real data, the contig-length filter and the relaxed core threshold, reduced the artefact without removing it, and no filter has been validated on real samples as removing the artefact.
  conf: not stated · class: not stated · holds: n = 8 and n = 5 gut E. coli pairs · src: mezitiReliabilityMetagenomeassembledGenomes2021, liCriticalAssessmentPangenomic2022 · trail: H1-02 §Verdict as delivered, §5. Verdicts, §critic · from: H1-02:A-002, H1-02:A-003, H1-02:A-024, H1-02:C-005
- **filters-corrections.4** Eisenhofer's GLM correction was validated on mock-community subsamples and over-corrected some genomes.
  conf: not stated · class: not stated · holds: mock-community subsamples · src: eisenhoferImpactMicrobialGenome2023 · trail: H1-02 §2.7 · from: H1-02:B-0112
- **filters-corrections.5** CELEBRIMBOR was validated on simulations, and the authors state that non-random loss violates its missing-at-random assumption.
  conf: not stated · class: not stated · holds: simulations · src: hellewellCELEBRIMBORCoreAccessory2024 · trail: H1-02 §2.7 · from: H1-02:B-0113
- **filters-corrections.6** mOTUpan was checked against a few closed Prochlorococcus genomes plus bootstraps, and its authors state that genes hard to assemble or bin leave an inevitable underestimate of the accessory genomes.
  conf: not stated · class: not stated · holds: a few closed Prochlorococcus genomes · src: buckMOTUpanRobustBayesian2022 · trail: H1-02 §2.7 · from: H1-02:B-0113
- **filters-corrections.7** MetaPathPredict was tested on random annotation downsampling only.
  conf: not stated · class: not stated · holds: random annotation downsampling · src: gellermcgrathPredictingMetabolicModules2024 · trail: H1-02 §2.7 · from: H1-02:B-0114
- **filters-corrections.8** None of the completeness-model corrections was validated against ground truth on natural-sample MAGs with real, non-random gaps, and the search found no correction so validated.
  conf: not stated · class: search (critic: C-103) · holds: routes: Europe PMC and WebSearch on mOTUpan, CELEBRIMBOR, MetaPathPredict, completeness bias correction and missing-at-random pangenome correction; the critic: supported by the named search routes and the authors' own stated assumptions · src: eisenhoferImpactMicrobialGenome2023, hellewellCELEBRIMBORCoreAccessory2024, buckMOTUpanRobustBayesian2022, gellermcgrathPredictingMetabolicModules2024 · trail: H1-02 §2.7, §Search record, §Adversarial critique · from: H1-02:B-0115, H1-02:B-0184, H1-02:B-0185, H1-02:C-103
- **filters-corrections.9** Artefacts persist above completeness thresholds: module fullness bias above 90%, ribosomal-protein, CRISPR and transposase deficits above 90%, chimerism in MIMAG high-quality sets, and contaminant genes below the 5% contamination threshold; no source showed that a completeness threshold removes the problem.
  conf: not stated · class: not stated · holds: spans four sources; the critic: direct full-text support for the ribosomal-protein and contaminant figures, while the module-fullness and chimerism sources rest on agent reads · src: eisenhoferImpactMicrobialGenome2023, miseUnexpectedAbsenceRibosomal2022, orakovGUNCDetectionChimerism2021, majernikSmallAmountsMisassembly2025 · trail: H1-02 §2.7, §5. Verdicts, §Adversarial critique · from: H1-02:B-0116, H1-02:B-0117, H1-02:A-023, H1-02:C-101, H1-02:C-102
- **filters-corrections.10** Gene-to-species correlation filtering classified contaminants with AUROC 0.97 on real gut data, against BLAST rather than ground truth.
  conf: not stated · class: not stated · holds: real gut data, BLAST as reference · src: majernikSmallAmountsMisassembly2025 · trail: H1-02 §2.7 · from: H1-02:B-0120

### community-diversity: community and strain diversity
needs: completeness-estimate, mobile-region-loss
- **community-diversity.1** In CAMI II, mean bin completeness fell from 36.9% (marine gold-standard assembly) to 18.2% under high strain diversity, and to 5.2% on MEGAHIT assemblies.
  conf: not stated · class: model (note: "in simulations") · holds: CAMI II simulated data · src: meyerCriticalAssessmentMetagenome2022 · trail: H1-02 §3.5, §Verdict as delivered · from: H1-02:B-0146, H1-02:A-018
- **community-diversity.2** In CAMI II, genomes with close relatives assembled far worse.
  conf: not stated · class: model (note: "modelled") · holds: CAMI II simulated data · src: meyerCriticalAssessmentMetagenome2022 · trail: H1-02 §3.5 · from: H1-02:B-0147
- **community-diversity.3** In a simulated 30-genome community, close relatives had no clear effect.
  conf: not stated · class: model (note: "modelled") · holds: one low-complexity simulation · src: maguireMetagenomeAssembledGenomeBinning2020 · trail: H1-02 §3.5, §Verdict as delivered · from: H1-02:B-0148, H1-02:A-019
- **community-diversity.4** In simulations, completeness correlated with taxonomic complexity at ρ = −0.55.
  conf: not stated · class: model (note: "modelled") · holds: Kim et al.'s simulations · src: kimComprehensiveBenchmarkingMetagenomic2026 · trail: H1-02 §3.5 · from: H1-02:B-0149
- **community-diversity.5** In one anaerobic digester sample, microdiversity increased fragmentation.
  conf: not stated · class: not stated · holds: engineered, one sample · src: sereikaOxfordNanoporeR102022 · trail: H1-02 §3.5 · from: H1-02:B-0151, H1-02:B-0153
- **community-diversity.6** In Danish agricultural soils sequenced to a mean depth of 107 Gb, the less diverse clay field reached 73% Nonpareil coverage, against 47% for sandy fields.
  conf: not stated · class: not stated · holds: natural soil; the critic: an unverified second-hand figure · src: johansenUnveilingSoilMicrobial2025 · trail: H1-02 §3.3, §Adversarial critique · from: H1-02:B-0132, H1-02:B-0133, H1-02:C-044
- **community-diversity.7** Reads assembled into contigs longer than 2 kb were 57% (clay) against 27% (sandy), and co-assembly raised both.
  conf: not stated · class: not stated · holds: the same Danish agricultural soils; the critic: an unverified second-hand figure · src: johansenUnveilingSoilMicrobial2025 · trail: H1-02 §3.3, §Adversarial critique · from: H1-02:B-0134, H1-02:C-044

### habitat: habitat
needs: sequencing-depth
- **habitat.1** Agricultural soils gave the lowest assembled fraction and MAG yield, and coastal samples still yielded more MAGs after depth normalisation.
  conf: not stated · class: not stated · holds: n = 3 + 3; the critic: not re-opened at synthesis · src: sereikaGenomeresolvedLongreadSequencing2025 · trail: H1-02 §3.3, §Adversarial critique · from: H1-02:B-0135, H1-02:C-043
- **habitat.2** Most binners struggled to recover high-quality soil genomes at depths comparable to gut and ocean.
  conf: not stated · class: not stated · holds: real soil, gut and ocean samples · src: kimComprehensiveBenchmarkingMetagenomic2026 · trail: H1-02 §3.3 · from: H1-02:B-0137

### pipeline: study of origin, pipeline, binner and processing mode
needs: chimerism, completeness-estimate
- **pipeline.1** For the same 1,554 gut samples binned by three studies, conspecific genomes had a median aligned fraction of 94.5% at 90% completeness or more and 86.6% at medium quality.
  conf: not stated · class: not stated · holds: natural human gut; aligned fraction by quality tier, not by study (the critic); gene content was not compared · src: almeidaUnifiedCatalog2042020 · trail: H1-02 §3.1, §critic · from: H1-02:B-0121, H1-02:B-0122, H1-02:C-022
- **pipeline.2** Different pipelines applied to identical reads disagreed on roughly 5% to 13% of aligned sequence, with the gap set by quality tier.
  conf: not stated · class: meas (note: "measured; gene content was not compared") · holds: the same 1,554 gut samples; gene content was not compared · src: almeidaUnifiedCatalog2042020 · trail: H1-02 §3.1 · from: H1-02:B-0122
- **pipeline.3** GUNC-flagged chimerism in real samples varied by binner.
  conf: not stated · class: not stated · holds: real samples; the chimerism figures shown are gut datasets (the critic) · src: kimComprehensiveBenchmarkingMetagenomic2026 · trail: H1-02 §3.1, §critic · from: H1-02:B-0125, H1-02:C-034
- **pipeline.4** SemiBin gains over other binners were largest in soil.
  conf: not stated · class: not stated · holds: real data across environments; the critic: not re-opened at synthesis · src: panDeepSiameseNeural2022 · trail: H1-02 §3.3, §Adversarial critique · from: H1-02:B-0138, H1-02:C-043
- **pipeline.5** Multi-sample binning identified 22% to 30% more potential ARG hosts than single-sample binning, so processing mode alone changes how many genomes carry an annotated trait.
  conf: not stated · class: meas (note: "measured; mixed natural and engineered") · holds: real marine, cheese, gut and sludge data; the critic: an unverified second-hand figure · src: hanBenchmarkingMetagenomicBinning2025 · trail: H1-02 §3.5, §Adversarial critique · from: H1-02:B-0154, H1-02:B-0155, H1-02:C-044

### annotation-coverage: annotation coverage
needs: pangenome
- **annotation-coverage.1** UHGG core genes had KEGG annotation for a median of 69% of genes, while accessory genes had significantly more unknowns.
  conf: not stated · class: meas (note: "These are measured, gut only") · holds: human gut only · src: almeidaUnifiedCatalog2042020 · trail: H1-02 §3.6 · from: H1-02:B-0156, H1-02:B-0158
- **annotation-coverage.2** Orthology-based GO coverage in an infant gut catalogue was 12%, and it favoured Gammaproteobacteria.
  conf: not stated · class: meas (note: "These are measured, gut only") · holds: infant gut only; the critic: not re-opened at synthesis · src: marangaComprehensiveFunctionalAnnotation2023 · trail: H1-02 §3.6, §Adversarial critique · from: H1-02:B-0157, H1-02:B-0158, H1-02:C-043
- **annotation-coverage.3** No source measured how annotation coverage differs between samples or environments for the same lineage.
  conf: not stated · class: search (note: "Route: WebSearch on annotation coverage bias") · holds: one route, WebSearch on annotation coverage bias for novel lineages · src: none (a search result) · trail: H1-02 §3.6, §Search record · from: H1-02:B-0159, H1-02:B-0188, H1-02:B-0189

### artefact-size: size of recovery artefacts in gene content
needs: same-sample-isolate, contaminated-pangenome, read-technology, gene-class-loss, mobile-region-loss, filters-corrections
- **artefact-size.1** Recovery artefacts in the gene content of related recovered genomes are measured and material, but only in natural human gut and, from a single source, coastal marine samples; for gut this rests on one isolate-comparison study (n = 8, one species) plus one mechanism-adjacent study.
  conf: single (critic: C-016) · class: meas (critic: C-001) · holds: three direct sources, each single-source with caveats the delivered verdict leaves out (the critic); gut isolate pairs, contamination of differential gene calls, marine read-technology pairs, and gene-class-specific losses across seawater, gut, chicken gut and phyllosphere catalogues · src: mezitiReliabilityMetagenomeassembledGenomes2021, majernikSmallAmountsMisassembly2025, orellanaComparingGenomesRecovered2023, miseUnexpectedAbsenceRibosomal2022 · trail: H1-02 §critic, §Verdict as delivered, §5. Verdicts · from: H1-02:C-001, H1-02:C-016, H1-02:C-019, H1-02:A-001, H1-02:A-022
- **artefact-size.2** The three direct sources measure different things in two environments (two human gut, one coastal marine), and their effect sizes are not commensurable: percentages of population core or variable genes, a median gene count, and a fraction of differentially prevalent genes; they are reported separately and not pooled.
  conf: single (note: "All three direct sources are SINGLE SOURCE in their setting") · class: not stated · holds: Meziti et al., Orellana et al., Majernik et al.; each single in its setting (the critic) · src: mezitiReliabilityMetagenomeassembledGenomes2021, orellanaComparingGenomesRecovered2023, majernikSmallAmountsMisassembly2025 · trail: H1-02 §4. Where, §Adversarial critique · from: H1-02:B-0162, H1-02:B-0163, H1-02:B-0164, H1-02:B-0165, H1-02:C-050
- **artefact-size.3** The first layer of the question, how far recovery changes the called gene or pathway content of a recovered genome, has direct measurements, although few.
  conf: not stated · class: not stated · holds: incompleteness, contamination, failure to assemble or bin variable and mobile regions, uneven annotation · src: none (the reviewer's synthesis) · trail: H1-02 §1. Scope · from: H1-02:B-0022, H1-02:B-0024
- **artefact-size.4** For soils and sediments, a gene-content comparison between related recovered genomes and a closed or isolate reference was not measured in the sources found; no equivalent of the same-sample isolate study was found for soil, sediment or any other high-diversity natural environment, and the closest hit (a mangrove long-read study, 2023) reported no gene-content difference.
  conf: not stated · class: search (note: "NOT MEASURED in the sources found") · holds: routes: WebSearch, Europe PMC title and abstract queries on MAG against isolate same sample, and long-read sediment comparisons · src: zhangLongreadAssembledMetagenomic2023 · trail: H1-02 §Verdict as delivered, §1. Scope, §Search record, §critic · from: H1-02:A-004, H1-02:B-0031, H1-02:B-0181, H1-02:B-0182, H1-02:B-0183, H1-02:C-006
- **artefact-size.5** One natural biocrust soil shows systematic short-read assembly loss of variable regions, which is indirect support only for soil.
  conf: not stated · class: not stated · holds: one natural biocrust soil; assembly loss, not gene content of recovered genomes · src: bergComparisonShortreadLongread2025 · trail: H1-02 §Verdict as delivered, §5. Verdicts · from: H1-02:A-005, H1-02:A-026
- **artefact-size.6** Removing Meziti et al. would leave Part A as measured and material on Majernik et al. and Orellana et al., but would remove the only natural same-sample isolate comparison and every figure for missed core and variable genes, since Li and Yin reuse its data.
  conf: not stated · class: not stated · holds: the review's sensitivity analysis · src: mezitiReliabilityMetagenomeassembledGenomes2021, majernikSmallAmountsMisassembly2025, orellanaComparingGenomesRecovered2023, liCriticalAssessmentPangenomic2022 · trail: H1-02 §5. Verdicts · from: H1-02:A-038

### sample-dependence: dependence of artefact size on sample properties
needs: artefact-size, pipeline, sequencing-depth, community-diversity, habitat, read-technology, annotation-coverage, gene-class-loss
- **sample-dependence.1** The second layer of the question, whether the size of the change depends on properties of the sample, has almost no measurements expressed in gene content; what it has are measurements of recovery quality, MAG yield and chimerism rates, which are proxies, and the sample-property dependence that has been measured concerns yield, completeness, chimerism or assembled fraction.
  conf: not stated · class: not stated · holds: across the review's sources · src: none (the reviewer's synthesis) · trail: H1-02 §1. Scope, §4. Where · from: H1-02:B-0023, H1-02:B-0025, H1-02:B-0026, H1-02:B-0027, H1-02:B-0166, H1-02:B-0167
- **sample-dependence.2** In the human gut, dependence on sample properties was not measured for gene or pathway content; proxies (chimerism rate, aligned fraction, ribosomal-protein absence by catalogue) differ between catalogues, but catalogue is confounded with pipeline and sample set, and these are not gene-content measures.
  conf: not stated · class: search (critic: C-007) · holds: natural human gut; the body supports not measured for gene content, with indirect proxy evidence that varies by catalogue (the critic) · src: orakovGUNCDetectionChimerism2021, almeidaUnifiedCatalog2042020, miseUnexpectedAbsenceRibosomal2022 · trail: H1-02 §critic, §Adversarial critique · from: H1-02:C-007, H1-02:C-008, H1-02:C-020, H1-02:C-023, H1-02:C-096
- **sample-dependence.3** In the human gut, dependence on community diversity and sequencing depth was not measured for gene content, and no study measuring how gene-content artefacts between conspecific MAGs scale with community diversity or depth across samples was found.
  conf: not stated · class: search (note: "Routes: WebSearch and Europe PMC on sequencing effort") · holds: routes: WebSearch and Europe PMC on sequencing effort against binning, batch or study effects in MAG catalogues, and soil MAG against depth · src: none (a search result) · trail: H1-02 §Verdict as delivered, §5. Verdicts, §3.1, §Search record · from: H1-02:A-007, H1-02:A-029, H1-02:B-0128, H1-02:B-0186, H1-02:B-0187
- **sample-dependence.4** In marine samples, dependence on read technology was measured, from a single source of 4 samples, confounded with depth.
  conf: single (critic: C-010) · class: meas (critic: C-010) · holds: natural coastal marine, 4 North Sea samples, one time series · src: orellanaComparingGenomesRecovered2023 · trail: H1-02 §critic, §Adversarial critique · from: H1-02:C-010, H1-02:C-024, H1-02:C-052
- **sample-dependence.5** In marine samples, dependence on diversity and depth was not measured for gene content; the evidence covers MAG yield only.
  conf: not stated · class: search (critic: C-011) · holds: natural marine · src: royaltyTheoreticalSimulationBasedInvestigation2019 · trail: H1-02 §critic, §Verdict as delivered, §5. Verdicts · from: H1-02:C-011, H1-02:A-012, H1-02:A-013, H1-02:A-032
- **sample-dependence.6** Removing Orellana et al. would change the marine dependence verdict to not measured for gene content, and marine Part A would then rest on Mise and Iwasaki alone.
  conf: not stated · class: not stated · holds: the review's sensitivity analysis · src: orellanaComparingGenomesRecovered2023, miseUnexpectedAbsenceRibosomal2022 · trail: H1-02 §5. Verdicts · from: H1-02:A-039
- **sample-dependence.7** In soil, dependence of the gene or pathway content of related recovered genomes on sample properties was not measured in this setting, and there is indirect recovery-quality evidence only; none of the soil evidence measures the gene or pathway content of related genomes recovered from different soil samples.
  conf: not stated · class: search (critic: C-012) · holds: natural soil · src: none (a search result) · trail: H1-02 §critic, §Verdict as delivered, §5. Verdicts, §3.3 · from: H1-02:C-012, H1-02:A-014, H1-02:A-033, H1-02:B-0141
- **sample-dependence.8** In soil, recovery quality (assembly fraction, MAG yield, bin quality) depends systematically on field diversity and depth, habitat and binner, and short-read assembly loss tracks within-sample coverage and population sequence variation.
  conf: not stated · class: meas (note: "All of this is measured and natural") · holds: natural soil; several of the figures carrying weight here are unverified second-hand figures (the critic) · src: johansenUnveilingSoilMicrobial2025, sereikaGenomeresolvedLongreadSequencing2025, kimComprehensiveBenchmarkingMetagenomic2026, panDeepSiameseNeural2022, bergComparisonShortreadLongread2025 · trail: H1-02 §Verdict as delivered, §5. Verdicts, §3.3, §Adversarial critique · from: H1-02:A-015, H1-02:A-034, H1-02:B-0140, H1-02:C-045
- **sample-dependence.9** Soil differs from gut in diversity, coverage and microdiversity, and the direction and size of the difference in artefacts are unmeasured.
  conf: not stated · class: not stated · holds: gut against soil · src: none (the reviewer's synthesis) · trail: H1-02 §3.3 · from: H1-02:B-0143
- **sample-dependence.10** In sediment, dependence was not measured in this setting: the only data are MAG yield against depth in one estuarine data set and habitat-level yield for coastal sediments, and nothing was found on content artefacts.
  conf: not stated · class: search (critic: C-012) · holds: natural sediment; MAG yield only · src: royaltyTheoreticalSimulationBasedInvestigation2019, sereikaGenomeresolvedLongreadSequencing2025 · trail: H1-02 §critic, §Verdict as delivered, §5. Verdicts, §3.4 · from: H1-02:C-012, H1-02:A-016, H1-02:A-017, H1-02:A-035, H1-02:B-0145
- **sample-dependence.11** No soil or sediment dependence verdict depends on any single source, because none reaches gene content.
  conf: not stated · class: not stated · holds: the review's sensitivity analysis · src: none (the reviewer's synthesis) · trail: H1-02 §5. Verdicts · from: H1-02:A-042
- **sample-dependence.12** Dependence on sample properties is measured and systematic in simulations (strain diversity degrades completeness and purity; depth effects are pipeline-dependent) and in engineered bioreactors (read technology changes contiguity and rRNA recovery), with one null for close relatives, but none of these answers the question for natural samples.
  conf: not stated · class: model (note: "in simulations") · holds: simulations and engineered systems, kept separate from natural samples · src: meyerCriticalAssessmentMetagenome2022, rochaSimulation69Microbial2024, maguireMetagenomeAssembledGenomeBinning2020, sereikaOxfordNanoporeR102022, singletonConnectingStructureFunction2021 · trail: H1-02 §Verdict as delivered, §5. Verdicts, §critic · from: H1-02:A-018, H1-02:A-021, H1-02:A-036, H1-02:A-037, H1-02:C-014
- **sample-dependence.13** The soil and sediment not-measured result is partly search-limited: the search missed SAG-referenced comparisons (Alneberg et al. 2018) and soil assembly data inside a source it already cites (Mise and Iwasaki), so the absence reflects the search more than the literature.
  conf: not stated · class: search (critic: C-106) · holds: the critic; the soil and sediment not-measured verdict is consistent with the body and echoes the brief's expected absence · src: alnebergGenomesUncultivatedProkaryotes2018, miseUnexpectedAbsenceRibosomal2022 · trail: H1-02 §critic, §Adversarial critique · from: H1-02:C-025, H1-02:C-104, H1-02:C-105, H1-02:C-106

## Do not say

- **dns.1** "Human gut: measured and systematic for study of origin (pipeline)."
  why: the critic: catalogue is confounded with pipeline and sample set; aligned fraction is reported by quality tier, not by study; the review's own Section 4 says the measured dependence concerns yield, completeness, chimerism or assembled fraction, not gene content; none of the sources measures artefact size in gene content against a study variable with sample set held constant (also the sensitivity line that the verdict stays "systematic" without Orakov et al.) · instead: sample-dependence.2, chimerism.1, pipeline.1 · trail: H1-02 §critic, §Adversarial critique · from: H1-02:A-006, H1-02:A-028, H1-02:A-040, H1-02:C-020, H1-02:C-021, H1-02:C-022, H1-02:C-023, H1-02:C-096
- **dns.2** "Marine: measured and systematic for read technology."
  why: the critic: one study of 4 samples with a depth confound, so 'systematic' is too strong for n = 1 study · instead: sample-dependence.4, read-technology.3 · trail: H1-02 §critic, §Adversarial critique · from: H1-02:A-010, H1-02:A-031, H1-02:C-024, H1-02:C-052
- **dns.3** "Meziti et al. found true recovery 16.9% to 20.4% below the estimates."
  why: the critic: not a range; the paper reports average shortfalls against two estimators, MiGA and CheckM · instead: completeness-estimate.2 · trail: H1-02 §critic · from: H1-02:B-0119, H1-02:C-026, H1-02:C-027
- **dns.4** "The MAGs had CheckM/MiGA completeness estimates of 81.1% to 97.2%."
  why: the critic: the range mixes estimator columns; the paper's text gives MiGA MAG completeness as 81.1% to 95.5% · instead: same-sample-isolate.1 · trail: H1-02 §critic · from: H1-02:B-0033, H1-02:C-028, H1-02:C-029
- **dns.5** "The main mechanism was therefore mis-binning among co-occurring relatives, not a failure to sequence."
  why: the critic: the reviewer's inference, which over-reads the source; the low-identity share of missed genes is attributed to sequence divergence or assembly errors, and mis-binned genes were only part of those without homologs · instead: same-sample-isolate.4, same-sample-isolate.5, same-sample-isolate.6 · trail: H1-02 §2.1, §critic, §Adversarial critique · from: H1-02:B-0038, H1-02:C-030, H1-02:C-093, H1-02:C-094, H1-02:C-095
- **dns.6** "GUNC-estimated chimerism did not correlate with depth across real gut, ocean and soil samples" (as a measured negative result).
  why: the critic: one unquantified sentence with no statistic, figure panel or stated dataset range, asserted-class evidence tagged as measured; the chimerism figures shown are gut datasets, so the regime is widened · instead: sequencing-depth.1 · trail: H1-02 §critic, §Adversarial critique · from: H1-02:A-008, H1-02:C-034, H1-02:C-046, H1-02:C-053
- **dns.7** "The strongest evidence comes from three natural-sample sources that do not depend on each other" (as together establishing a field-level finding).
  why: the critic: they measure different things in two environments, and each is single in its setting · instead: artefact-size.2 · trail: H1-02 §4. Where, §Adversarial critique · from: H1-02:B-0160, H1-02:C-049, H1-02:C-050
- **dns.8** "The contamination filters in common use leave chimeric material in place."
  why: the critic: generalises to filters in common use from one chimerism survey plus one species-level case study · instead: chimerism.1, chimerism.2, contaminated-pangenome.2 · trail: H1-02 §2.2, §Adversarial critique · from: H1-02:B-0062, H1-02:C-051
- **dns.9** "The contamination produced apparent content differences between sample groups" (of recovered genomes), and "contamination-driven gains were measured directly."
  why: the critic: the differential calls come from MIDAS2 read mapping to a partly contaminated reference pangenome; they are not content differences between genomes recovered from different samples · instead: contaminated-pangenome.1 · trail: H1-02 §2.2, §critic, §Adversarial critique · from: H1-02:B-0049, H1-02:A-023, H1-02:C-018, H1-02:C-090, H1-02:C-091, H1-02:C-092
- **dns.10** "A gene-count difference of about 9%, which depended on read technology."
  why: the critic: omits the paper's reported 3-fold difference in sequenced bases between platforms and attributes the effect to technology alone · instead: read-technology.3 · trail: H1-02 §2.3, §critic, §Adversarial critique · from: H1-02:B-0066, H1-02:C-017, H1-02:C-097
- **dns.11** "Only one natural-sample study compared MAGs with isolate genomes of the same lineage from the same sample at gene level" (as a structural fact of the literature).
  why: the critic: a statement about the search, which omits SAG-referenced comparisons (Alneberg et al. 2018) · instead: same-sample-isolate.11 · trail: H1-02 §1. Scope, §Adversarial critique · from: H1-02:B-0028, H1-02:B-0029, H1-02:C-055
- **dns.12** "GEM: no major loss of gene content" (as a measured finding).
  why: the critic: an author assertion; the underlying Supp. Fig. 2 was not read, so the claim is asserted, not measured · instead: bounding-comparisons.1 · trail: H1-02 §2.6, §Adversarial critique · from: H1-02:B-0095, H1-02:C-040, H1-02:C-042
- **dns.13** "For soils and sediments the setting has not been measured at gene-content level" (as a fact about the literature).
  why: the critic: partly search-limited; the search missed SAG-referenced comparisons and soil assembly data inside a source it already cites, so the absence reflects the search more than the literature · instead: artefact-size.4, sample-dependence.13 · trail: H1-02 §5. Verdicts, §Adversarial critique · from: H1-02:A-025, H1-02:C-104, H1-02:C-105, H1-02:C-106
- **dns.14** "The gut artefact sizes in Sections 2.1 and 2.2 apply to soil."
  why: the note: the gut findings should not be transferred to soil; the setting differs in diversity, coverage and microdiversity, and the direction and size of the difference are unmeasured · instead: sample-dependence.9 · trail: H1-02 §3.3 · from: H1-02:B-0142, H1-02:B-0143

## Gaps

- **gap.1** Genomes from the same natural sample compared with a non-isolate reference: single-amplified genomes against MAGs, gene-content overlap and 16S presence (Alneberg et al. 2018, brackish Baltic Sea bacterioplankton); follow-up search on SAG and MAG comparisons of the same sample in marine, freshwater and soil.
  blocks: same-sample-isolate, artefact-size · origin: critic coverage gap; the review treats isolates as the only same-sample reference · src: alnebergGenomesUncultivatedProkaryotes2018 · from: H1-02:C-069..072
- **gap.2** Gene-class recovery against depth in soil: re-read Mise and Iwasaki Fig. 3 and Supp. Fig. S1 for soil and depth, and check whether any other study reports gene-class recovery against depth in soil.
  blocks: gene-class-loss, sample-dependence · origin: critic coverage gap · src: miseUnexpectedAbsenceRibosomal2022 · from: H1-02:C-077, H1-02:C-078
- **gap.3** Annotation-coverage bias across lineages, and between-sample or between-environment differences in annotation coverage for one lineage, in novel and understudied phyla typical of soils and sediments (Lobb et al. 2020; KEGG or Pfam annotation rate against phylogenetic novelty in soil MAG catalogues).
  blocks: annotation-coverage · origin: critic coverage gap; a not-found result of the search · src: lobbAssessmentGenomeAnnotation2020 · from: H1-02:C-079..082, H1-02:B-0188
- **gap.4** Long-read or HiFi against short-read MAG content in a complex natural host-associated community (sheep and ruminant gut), including plasmid and mobile-element content; Bickhart et al. 2022 was not obtained.
  blocks: read-technology · origin: critic coverage gap; a source not obtained · src: bickhartGeneratingLineageresolvedComplete2022 · from: H1-02:C-083
- **gap.5** Freshwater lakes and hypersaline salterns are absent from both parts; Puente-Sánchez et al. and Conrad et al. were not obtained.
  blocks: sample-dependence · origin: critic coverage gap; sources not obtained · src: puentesanchezExploringEnvironmentalIntraspecies2023, conradTowardQuantifyingAdaptive2021 · from: H1-02:C-084
- **gap.6** How microdiversity or strain heterogeneity in natural samples, measured per population, changes the MAG gene content recovered across samples; only CAMI simulations and Berg et al. touch it.
  blocks: community-diversity · origin: critic coverage gap · from: H1-02:C-085
- **gap.7** Sediments have only yield data: long-read against short-read comparisons and SAG-MAG comparisons in deep-sea, freshwater and estuarine sediments were not searched by name, and the mangrove study's gene-content statements were not reported.
  blocks: sample-dependence · origin: critic coverage gap · src: zhangLongreadAssembledMetagenomic2023 · from: H1-02:C-086..088
- **gap.8** Proximity-ligation (Hi-C) binning evaluations of plasmid and mobile-element assignment on natural samples, against shotgun-only binning.
  blocks: mobile-region-loss · origin: critic coverage gap · from: H1-02:C-089
- **gap.9** A targeted follow-up brief on soil and sediment recovery artefacts, sized separately, with the SAG-against-MAG reference and Hi-C binning of mobile elements as the named routes.
  blocks: sample-dependence, artefact-size · origin: the note's stage-2 check, triggered by coverage gaps naming sample types without direct measurement · trail: H1-02 §Stage 2 check · from: H1-02:B-0017, H1-02:B-0018, H1-02:B-0019, H1-02:B-0020
- **gap.10** Supplementary material that carries figures was not read: whether Li and Yin's 25% core-gene loss comes from Supp. Fig. S14 or a main-text statement, and GEM's Supp. Fig. 2 behind its genome-size statement; CAMI I, CheckM2 and Bickhart 2022 were also not read for budget.
  blocks: same-sample-isolate.10, bounding-comparisons.1 · origin: critic full-text breaches; budget limits · from: H1-02:C-035..039, H1-02:C-041, H1-02:B-0016
- **gap.11** Figures from Nayfach et al. 2019, Pasolli et al., Gautreau et al., Johansen et al., Sereika et al. 2025, Pan et al., Han et al., Rocha et al. and Maranga et al. rest on search-agent reads with no cross-agent confirmation, and several carry weight in the soil indirect evidence.
  blocks: bounding-comparisons, community-diversity, habitat, pipeline, sample-dependence.8 · origin: critic: unverified second-hand figures, not re-opened at synthesis · from: H1-02:C-043..045, H1-02:B-0178, H1-02:B-0179
- **gap.12** Whether Eisenhofer et al. was re-checked in full text: the Search record says "[6], [12], [3] and [5] from Europe PMC XML", while the critic says "[3] and [9] rest on agent reads".
  blocks: pathway-completeness.1, filters-corrections.9 · origin: the note and its critic disagree · from: H1-02:B-0012, H1-02:B-0175, H1-02:C-102
- **gap.13** A completeness or missingness correction validated on natural-sample MAGs with non-random gaps against ground truth was not found.
  blocks: filters-corrections · origin: not found in the search, with routes · from: H1-02:B-0184, H1-02:B-0185
- **gap.14** How gene-content artefacts between conspecific MAGs scale with community diversity or depth across samples was not found.
  blocks: sample-dependence · origin: not found in the search, with routes · from: H1-02:B-0186, H1-02:B-0187
- **gap.15** A soil or sediment study comparing gene content of MAGs with isolate or closed genomes of the same lineage was not found.
  blocks: artefact-size · origin: not found in the search, with routes · from: H1-02:B-0181, H1-02:B-0182, H1-02:B-0183
- **gap.16** Which datasets Kim et al.'s statement that chimerism did not correlate with sequencing depth covers.
  blocks: sequencing-depth.1 · origin: critic: unclear which datasets it covers · src: kimComprehensiveBenchmarkingMetagenomic2026 · from: H1-02:C-009, H1-02:C-033

## Out of scope

- H1-02:C-015: the critic's record of what it checked (provenance, kept in the result note)
- H1-02:C-056..068: reference corrections, applied in Sources
- H1-02:C-099, H1-02:C-100: the critic's expectation-echo check of the brief's wording (provenance of the run, not a finding)
- H1-02:A-027: a heading of the verdict list, not a finding

## Sources

```bibtex
@article{mezitiReliabilityMetagenomeassembledGenomes2021,
  author = {Meziti, Alexandra and Rodriguez-R, Luis M. and Hatt, Janet K. and Peña-Gonzalez, Angela and Levy, Karen and Konstantinidis, Konstantinos T.},
  title = {{The Reliability of Metagenome-Assembled Genomes (MAGs) in Representing Natural Populations: Insights from Comparing MAGs against Isolate Genomes Derived from the Same Fecal Sample}},
  journal = {Applied and Environmental Microbiology},
  year = {2021},
  volume = {87},
  number = {6},
  pages = {e02593-20},
  doi = {10.1128/AEM.02593-20},
  note = {access: full_text (re-verified at synthesis via PMC HTML; the critic checked the full text); cited as: H1-02 [1]}
}

@article{liCriticalAssessmentPangenomic2022,
  author = {Li, Tang and Yin, Yanbin},
  title = {{Critical assessment of pan-genomic analysis of metagenome-assembled genomes}},
  journal = {Briefings in Bioinformatics},
  year = {2022},
  volume = {23},
  number = {6},
  pages = {bbac413},
  doi = {10.1093/bib/bbac413},
  note = {access: full_text (the search agents' full-text reads; not re-opened at synthesis; Supp. Fig. S14 not read); cited as: H1-02 [2]}
}

@article{eisenhoferImpactMicrobialGenome2023,
  author = {Eisenhofer, Raphael and Odriozola, Iñaki and Alberdi, Antton},
  title = {{Impact of microbial genome completeness on metagenomic functional inference}},
  journal = {ISME Communications},
  year = {2023},
  volume = {3},
  number = {1},
  pages = {12},
  doi = {10.1038/s43705-023-00221-z},
  note = {access: full_text (re-verified at synthesis via Europe PMC XML, per the Search record; the critic: rests on agent reads, H1-02:C-102); cited as: H1-02 [3]}
}

@article{maguireMetagenomeAssembledGenomeBinning2020,
  author = {Maguire, Finlay and Jia, Baofeng and Gray, Kristen L. and Lau, Wing Yin Venus and Beiko, Robert G. and Brinkman, Fiona S. L.},
  title = {{Metagenome-assembled genome binning methods with short reads disproportionately fail for plasmids and genomic Islands}},
  journal = {Microbial Genomics},
  year = {2020},
  volume = {6},
  number = {10},
  pages = {e000436},
  doi = {10.1099/mgen.0.000436},
  note = {access: full_text (the search agents' full-text reads; not re-opened at synthesis); cited as: H1-02 [4]}
}

@article{nelsonBiasesGenomeReconstruction2020,
  author = {Nelson, William C. and Tully, Benjamin J. and Mobberley, Jennifer M.},
  title = {{Biases in genome reconstruction from metagenomic data}},
  journal = {PeerJ},
  year = {2020},
  volume = {8},
  pages = {e10119},
  doi = {10.7717/peerj.10119},
  note = {access: full_text (re-verified at synthesis via Europe PMC XML); cited as: H1-02 [5]}
}

@article{miseUnexpectedAbsenceRibosomal2022,
  author = {Mise, Kazumori and Iwasaki, Wataru},
  title = {{Unexpected absence of ribosomal protein genes from metagenome-assembled genomes}},
  journal = {ISME Communications},
  year = {2022},
  volume = {2},
  number = {1},
  pages = {118},
  doi = {10.1038/s43705-022-00204-6},
  note = {access: full_text (re-verified at synthesis via Europe PMC XML; the critic checked the full text); cited as: H1-02 [6]}
}

@article{meyerCriticalAssessmentMetagenome2022,
  author = {Meyer, Fernando and Fritz, Adrian and Deng, Zhi-Luo and Koslicki, David and Lesker, Till Robin and Gurevich, Alexey and Robertson, Gary and Alser, Mohammed and Antipov, Dmitry and Beghini, Francesco and Bertrand, Denis and Brito, Jaqueline J. and Brown, C. Titus and Buchmann, Jan and Buluç, Aydin and Chen, Bo and Chikhi, Rayan and Clausen, Philip T. L. C. and Cristian, Alexandru and Dabrowski, Piotr Wojciech and Darling, Aaron E. and Egan, Rob and Eskin, Eleazar and Georganas, Evangelos and Goltsman, Eugene and Gray, Melissa A. and Hansen, Lars Hestbjerg and Hofmeyr, Steven and Huang, Pingqin and Irber, Luiz and Jia, Huijue and Jørgensen, Tue Sparholt and Kieser, Silas D. and Klemetsen, Terje and Kola, Axel and Kolmogorov, Mikhail and Korobeynikov, Anton and Kwan, Jason and LaPierre, Nathan and Lemaitre, Claire and Li, Chenhao and Limasset, Antoine and Malcher-Miranda, Fabio and Mangul, Serghei and Marcelino, Vanessa R. and Marchet, Camille and Marijon, Pierre and Meleshko, Dmitry and Mende, Daniel R. and Milanese, Alessio and Nagarajan, Niranjan and Nissen, Jakob and Nurk, Sergey and Oliker, Leonid and Paoli, Lucas and Peterlongo, Pierre and Piro, Vitor C. and Porter, Jacob S. and Rasmussen, Simon and Rees, Evan R. and Reinert, Knut and Renard, Bernhard and Robertsen, Espen Mikal and Rosen, Gail L. and Ruscheweyh, Hans-Joachim and Sarwal, Varuni and Segata, Nicola and Seiler, Enrico and Shi, Lizhen and Sun, Fengzhu and Sunagawa, Shinichi and Sørensen, Søren Johannes and Thomas, Ashleigh and Tong, Chengxuan and Trajkovski, Mirko and Tremblay, Julien and Uritskiy, Gherman and Vicedomini, Riccardo and Wang, Zhengyang and Wang, Ziye and Wang, Zhong and Warren, Andrew and Willassen, Nils Peder and Yelick, Katherine and You, Ronghui and Zeller, Georg and Zhao, Zhengqiao and Zhu, Shanfeng and Zhu, Jie and Garrido-Oter, Ruben and Gastmeier, Petra and Hacquard, Stephane and Häußler, Susanne and Khaledi, Ariane and Maechler, Friederike and Mesny, Fantin and Radutoiu, Simona and Schulze-Lefert, Paul and Smit, Nathiana and Strowig, Till and Bremges, Andreas and Sczyrba, Alexander and McHardy, Alice Carolyn},
  title = {{Critical Assessment of Metagenome Interpretation: the second round of challenges}},
  journal = {Nature Methods},
  year = {2022},
  volume = {19},
  number = {4},
  pages = {429-440},
  doi = {10.1038/s41592-022-01431-4},
  note = {access: full_text (the search agents' full-text reads; not re-opened at synthesis; the critic checked the full text); cited as: H1-02 [7]}
}

@article{shaiberCompositeMetagenomeAssembledGenomes2019,
  author = {Shaiber, Alon and Eren, A. Murat},
  title = {{Composite Metagenome-Assembled Genomes Reduce the Quality of Public Genome Repositories}},
  journal = {mBio},
  year = {2019},
  volume = {10},
  number = {3},
  pages = {e00725-19},
  doi = {10.1128/mBio.00725-19},
  note = {access: full_text (the search agents' full-text reads); type: letter; cited as: H1-02 [8]}
}

@article{orakovGUNCDetectionChimerism2021,
  author = {Orakov, Askarbek and Fullam, Anthony and Coelho, Luis Pedro and Khedkar, Supriya and Szklarczyk, Damian and Mende, Daniel R. and Schmidt, Thomas S. B. and Bork, Peer},
  title = {{GUNC: detection of chimerism and contamination in prokaryotic genomes}},
  journal = {Genome Biology},
  year = {2021},
  volume = {22},
  number = {1},
  pages = {178},
  doi = {10.1186/s13059-021-02393-0},
  note = {access: full_text (the search agents' full-text reads; not re-opened at synthesis); cited as: H1-02 [9]}
}

@article{almeidaUnifiedCatalog2042020,
  author = {Almeida, Alexandre and Nayfach, Stephen and Boland, Miguel and Strozzi, Francesco and Beracochea, Martin and Shi, Zhou Jason and Pollard, Katherine S. and Sakharova, Ekaterina and Parks, Donovan H. and Hugenholtz, Philip and Segata, Nicola and Kyrpides, Nikos C. and Finn, Robert D.},
  title = {{A unified catalog of 204,938 reference genomes from the human gut microbiome}},
  journal = {Nature Biotechnology},
  year = {2021},
  volume = {39},
  number = {1},
  pages = {105-114},
  doi = {10.1038/s41587-020-0603-3},
  note = {access: full_text (the search agents' full-text reads; not re-opened at synthesis); the critic: Crossref issued date is 2020-07-20 (online), the 2021 volume 39(1) is the print date (H1-02:C-059); cited as: H1-02 [10]}
}

@article{nayfachGenomicCatalogEarths2020,
  author = {Nayfach, Stephen and Roux, Simon and Seshadri, Rekha and Udwary, Daniel and Varghese, Neha and Schulz, Frederik and Wu, Dongying and Paez-Espino, David and Chen, I-Min and Huntemann, Marcel and Palaniappan, Krishna and Ladau, Joshua and Mukherjee, Supratim and Reddy, T. B. K. and Nielsen, Torben and Kirton, Edward and Faria, José P. and Edirisinghe, Janaka N. and Henry, Christopher S. and Jungbluth, Sean P. and Chivian, Dylan and Dehal, Paramvir and Wood-Charlson, Elisha M. and Arkin, Adam P. and Tringe, Susannah G. and Visel, Axel and {IMG/M Data Consortium} and Abreu, Helena and Acinas, Silvia G. and Allen, Eric and Allen, Michelle A. and Alteio, Lauren V. and Andersen, Gary and Anesio, Alexandre M. and Attwood, Graeme and Avila-Magaña, Viridiana and Badis, Yacine and Bailey, Jake and Baker, Brett and Baldrian, Petr and Barton, Hazel A. and Beck, David A. C. and Becraft, Eric D. and Beller, Harry R. and Beman, J. Michael and Bernier-Latmani, Rizlan and Berry, Timothy D. and Bertagnolli, Anthony and Bertilsson, Stefan and Bhatnagar, Jennifer M. and Bird, Jordan T. and Blanchard, Jeffrey L. and Blumer-Schuette, Sara E. and Bohannan, Brendan and Borton, Mikayla A. and Brady, Allyson and Brawley, Susan H. and Brodie, Juliet and Brown, Steven and Brum, Jennifer R. and Brune, Andreas and Bryant, Donald A. and Buchan, Alison and Buckley, Daniel H. and Buongiorno, Joy and Cadillo-Quiroz, Hinsby and Caffrey, Sean M. and Campbell, Ashley N. and Campbell, Barbara and Carr, Stephanie and Carroll, JoLynn and Cary, S. Craig and Cates, Anna M. and Cattolico, Rose Ann and Cavicchioli, Ricardo and Chistoserdova, Ludmila and Coleman, Maureen L. and Constant, Philippe and Conway, Jonathan M. and Mac Cormack, Walter P. and Crowe, Sean and Crump, Byron and Currie, Cameron and Daly, Rebecca and DeAngelis, Kristen M. and Denef, Vincent and Denman, Stuart E. and Desta, Adey and Dionisi, Hebe and Dodsworth, Jeremy and Dombrowski, Nina and Donohue, Timothy and Dopson, Mark and Driscoll, Timothy and Dunfield, Peter and Dupont, Christopher L. and Dynarski, Katherine A. and Edgcomb, Virginia and Edwards, Elizabeth A. and Elshahed, Mostafa S. and Figueroa, Israel and Flood, Beverly and Fortney, Nathaniel and Fortunato, Caroline S. and Francis, Christopher and Gachon, Claire M. M. and Garcia, Sarahi L. and Gazitua, Maria C. and Gentry, Terry and Gerwick, Lena and Gharechahi, Javad and Girguis, Peter and Gladden, John and Gradoville, Mary and Grasby, Stephen E. and Gravuer, Kelly and Grettenberger, Christen L. and Gruninger, Robert J. and Guo, Jiarong and Habteselassie, Mussie Y. and Hallam, Steven J. and Hatzenpichler, Roland and Hausmann, Bela and Hazen, Terry C. and Hedlund, Brian and Henny, Cynthia and Herfort, Lydie and Hernandez, Maria and Hershey, Olivia S. and Hess, Matthias and Hollister, Emily B. and Hug, Laura A. and Hunt, Dana and Jansson, Janet and Jarett, Jessica and Kadnikov, Vitaly V. and Kelly, Charlene and Kelly, Robert and Kelly, William and Kerfeld, Cheryl A. and Kimbrel, Jeff and Klassen, Jonathan L. and Konstantinidis, Konstantinos T. and Lee, Laura L. and Li, Wen-Jun and Loder, Andrew J. and Loy, Alexander and Lozada, Mariana and MacGregor, Barbara and Magnabosco, Cara and Maria da Silva, Aline and McKay, R. Michael and McMahon, Katherine and McSweeney, Chris S. and Medina, Mónica and Meredith, Laura and Mizzi, Jessica and Mock, Thomas and Momper, Lily and Moran, Mary Ann and Morgan-Lang, Connor and Moser, Duane and Muyzer, Gerard and Myrold, David and Nash, Maisie and Nesbø, Camilla L. and Neumann, Anthony P. and Neumann, Rebecca B. and Noguera, Daniel and Northen, Trent and Norton, Jeanette and Nowinski, Brent and Nüsslein, Klaus and O'Malley, Michelle A. and Oliveira, Rafael S. and Maia de Oliveira, Valeria and Onstott, Tullis and Osvatic, Jay and Ouyang, Yang and Pachiadaki, Maria and Parnell, Jacob and Partida-Martinez, Laila P. and Peay, Kabir G. and Pelletier, Dale and Peng, Xuefeng and Pester, Michael and Pett-Ridge, Jennifer and Peura, Sari and Pjevac, Petra and Plominsky, Alvaro M. and Poehlein, Anja and Pope, Phillip B. and Ravin, Nikolai and Redmond, Molly C. and Reiss, Rebecca and Rich, Virginia and Rinke, Christian and Rodrigues, Jorge L. Mazza and Rodriguez-Reillo, William and Rossmassler, Karen and Sackett, Joshua and Salekdeh, Ghasem Hosseini and Saleska, Scott and Scarborough, Matthew and Schachtman, Daniel and Schadt, Christopher W. and Schrenk, Matthew and Sczyrba, Alexander and Sengupta, Aditi and Setubal, Joao C. and Shade, Ashley and Sharp, Christine and Sherman, David H. and Shubenkova, Olga V. and Sierra-Garcia, Isabel Natalia and Simister, Rachel and Simon, Holly and Sjöling, Sara and Slonczewski, Joan and Correa de Souza, Rafael Soares and Spear, John R. and Stegen, James C. and Stepanauskas, Ramunas and Stewart, Frank and Suen, Garret and Sullivan, Matthew and Sumner, Dawn and Swan, Brandon K. and Swingley, Wesley and Tarn, Jonathan and Taylor, Gordon T. and Teeling, Hanno and Tekere, Memory and Teske, Andreas and Thomas, Torsten and Thrash, Cameron and Tiedje, James and Ting, Claire S. and Tully, Benjamin and Tyson, Gene and Ulloa, Osvlado and Valentine, David L. and Van Goethem, Marc W. and VanderGheynst, Jean and Verbeke, Tobin J. and Vollmers, John and Vuillemin, Aurèle and Waldo, Nicholas B. and Walsh, David A. and Weimer, Bart C. and Whitman, Thea and van der Wielen, Paul and Wilkins, Michael and Williams, Timothy J. and Woodcroft, Ben and Woolet, Jamie and Wrighton, Kelly and Ye, Jun and Young, Erica B. and Youssef, Noha H. and Yu, Feiqiao Brian and Zemskaya, Tamara I. and Ziels, Ryan and Woyke, Tanja and Mouncey, Nigel J. and Ivanova, Natalia N. and Kyrpides, Nikos C. and Eloe-Fadrosh, Emiley A.},
  title = {{A genomic catalog of Earth's microbiomes}},
  journal = {Nature Biotechnology},
  year = {2021},
  volume = {39},
  number = {4},
  pages = {499-509},
  doi = {10.1038/s41587-020-0718-6},
  note = {access: full_text (the search agents' full-text reads; not re-opened at synthesis; main text only, Supp. Fig. 2, Supp. Table 3 and Supp. Note not read); author list as in the Crossref record, including the Osvlado spelling as registered; cited as: H1-02 [11]}
}

@article{orellanaComparingGenomesRecovered2023,
  author = {Orellana, Luis H. and Krüger, Karen and Sidhu, Chandni and Amann, Rudolf},
  title = {{Comparing genomes recovered from time-series metagenomes using long- and short-read sequencing technologies}},
  journal = {Microbiome},
  year = {2023},
  volume = {11},
  number = {1},
  pages = {105},
  doi = {10.1186/s40168-023-01557-3},
  note = {access: full_text (re-verified at synthesis via Europe PMC XML; the critic checked the full text); cited as: H1-02 [12]}
}

@article{evansDereplicateNotDereplicate2020,
  author = {Evans, Jacob T. and Denef, Vincent J.},
  title = {{To Dereplicate or Not To Dereplicate?}},
  journal = {mSphere},
  year = {2020},
  volume = {5},
  number = {3},
  pages = {e00971-19},
  doi = {10.1128/mSphere.00971-19},
  note = {access: full_text (read in full by one agent); type: opinion piece; not cited (the reference list notes its finding for completeness; the note also lists it under Sources not obtained as read in full but not used); cited as: H1-02 [13]}
}

@article{buckMOTUpanRobustBayesian2022,
  author = {Buck, Moritz and Mehrshad, Maliheh and Bertilsson, Stefan},
  title = {{mOTUpan: a robust Bayesian approach to leverage metagenome-assembled genomes for core-genome estimation}},
  journal = {NAR Genomics and Bioinformatics},
  year = {2022},
  volume = {4},
  number = {3},
  pages = {lqac060},
  doi = {10.1093/nargab/lqac060},
  note = {access: full_text (the search agents' full-text reads; not re-opened at synthesis); cited as: H1-02 [14]}
}

@article{gellermcgrathPredictingMetabolicModules2024,
  author = {Geller-McGrath, David and Konwar, Kishori M. and Edgcomb, Virginia P. and Pachiadaki, Maria and Roddy, Jack W. and Wheeler, Travis J. and McDermott, Jason E.},
  title = {{Predicting metabolic modules in incomplete bacterial genomes with MetaPathPredict}},
  journal = {eLife},
  year = {2024},
  volume = {13},
  pages = {e85749},
  doi = {10.7554/eLife.85749},
  note = {access: full_text (the search agents' full-text reads; not re-opened at synthesis); the critic: Crossref lists given-name initials without periods (H1-02:C-060); cited as: H1-02 [15]}
}

@article{royaltyTheoreticalSimulationBasedInvestigation2019,
  author = {Royalty, Taylor M. and Steen, Andrew D.},
  title = {{Theoretical and Simulation-Based Investigation of the Relationship between Sequencing Effort, Microbial Community Richness, and Diversity in Binning Metagenome-Assembled Genomes}},
  journal = {mSystems},
  year = {2019},
  volume = {4},
  number = {5},
  pages = {e00384-19},
  doi = {10.1128/mSystems.00384-19},
  note = {access: full_text (the search agents' full-text reads; not re-opened at synthesis); cited as: H1-02 [16]}
}

@article{sereikaGenomeresolvedLongreadSequencing2025,
  author = {Sereika, Mantas and Mussig, Aaron James and Jiang, Chenjing and Knudsen, Kalinka Sand and Jensen, Thomas Bygh Nymann and Petriglieri, Francesca and Yang, Yu and Jørgensen, Vibeke Rudkjøbing and Delogu, Francesco and Sørensen, Emil Aarre and Nielsen, Per Halkjær and Singleton, Caitlin Margaret and Hugenholtz, Philip and Albertsen, Mads},
  title = {{Genome-resolved long-read sequencing expands known microbial diversity across terrestrial habitats}},
  journal = {Nature Microbiology},
  year = {2025},
  volume = {10},
  number = {8},
  pages = {2018-2030},
  doi = {10.1038/s41564-025-02062-z},
  note = {access: full_text (the search agents' full-text reads; not re-opened at synthesis); cited as: H1-02 [17]}
}

@article{mossCompleteClosedBacterial2020,
  author = {Moss, Eli L. and Maghini, Dylan G. and Bhatt, Ami S.},
  title = {{Complete, closed bacterial genomes from microbiomes using nanopore sequencing}},
  journal = {Nature Biotechnology},
  year = {2020},
  volume = {38},
  number = {6},
  pages = {701-707},
  doi = {10.1038/s41587-020-0422-6},
  note = {access: full_text (the search agents' full-text reads; not re-opened at synthesis); not cited (qualitative only, not cited in the body for any figure); cited as: H1-02 [18]}
}

@article{hellewellCELEBRIMBORCoreAccessory2024,
  author = {Hellewell, Joel and Horsfield, Samuel T. and von Wachsmann, Johanna and Gurbich, Tatiana A. and Finn, Robert D. and Iqbal, Zamin and Roberts, Leah W. and Lees, John A.},
  title = {{CELEBRIMBOR: core and accessory genes from metagenomes}},
  journal = {Bioinformatics},
  year = {2024},
  volume = {40},
  number = {9},
  pages = {btae542},
  doi = {10.1093/bioinformatics/btae542},
  note = {access: full_text (the search agents' full-text reads; not re-opened at synthesis; Supp. Fig. S6 not read); cited as: H1-02 [19]}
}

@article{gautreauPPanGGOLiNDepictingMicrobial2020,
  author = {Gautreau, Guillaume and Bazin, Adelme and Gachet, Mathieu and Planel, Rémi and Burlot, Laura and Dubois, Mathieu and Perrin, Amandine and Médigue, Claudine and Calteau, Alexandra and Cruveiller, Stéphane and Matias, Catherine and Ambroise, Christophe and Rocha, Eduardo P. C. and Vallenet, David},
  title = {{PPanGGOLiN: Depicting microbial diversity via a partitioned pangenome graph}},
  journal = {PLOS Computational Biology},
  year = {2020},
  volume = {16},
  number = {3},
  pages = {e1007732},
  doi = {10.1371/journal.pcbi.1007732},
  note = {access: full_text (the search agents' full-text reads; not re-opened at synthesis); cited as: H1-02 [20]}
}

@article{nayfachNewInsightsUncultivated2019,
  author = {Nayfach, Stephen and Shi, Zhou Jason and Seshadri, Rekha and Pollard, Katherine S. and Kyrpides, Nikos C.},
  title = {{New insights from uncultivated genomes of the global human gut microbiome}},
  journal = {Nature},
  year = {2019},
  volume = {568},
  number = {7753},
  pages = {505-510},
  doi = {10.1038/s41586-019-1058-x},
  note = {access: full_text (the search agents' full-text reads; not re-opened at synthesis; Extended Data Fig. 3f not read); cited as: H1-02 [21]}
}

@article{majernikSmallAmountsMisassembly2025,
  author = {Majernik, Stephanie N. and Beaver, Larry and Bradley, Patrick H.},
  title = {{Small amounts of misassembly can have disproportionate effects on pangenome-based metagenomic analyses}},
  journal = {mSphere},
  year = {2025},
  volume = {10},
  number = {5},
  pages = {e00857-24},
  doi = {10.1128/msphere.00857-24},
  note = {access: full_text (published version read; a bioRxiv preprint also exists; the critic checked the full text); cited as: H1-02 [22]}
}

@article{tonkinhillProducingPolishedProkaryotic2020,
  author = {Tonkin-Hill, Gerry and MacAlasdair, Neil and Ruis, Christopher and Weimann, Aaron and Horesh, Gal and Lees, John A. and Gladstone, Rebecca A. and Lo, Stephanie and Beaudoin, Christopher and Floto, R. Andres and Frost, Simon D. W. and Corander, Jukka and Bentley, Stephen D. and Parkhill, Julian},
  title = {{Producing polished prokaryotic pangenomes with the Panaroo pipeline}},
  journal = {Genome Biology},
  year = {2020},
  volume = {21},
  number = {1},
  pages = {180},
  doi = {10.1186/s13059-020-02090-4},
  note = {access: full_text (the search agents' full-text reads; not re-opened at synthesis); cited as: H1-02 [23]}
}

@article{pellegrinettiRethinkingMetagenomeAssembledGenome2026,
  author = {Pellegrinetti, Thierry Alexandre and Molligan, Joshua and Mendes, Lucas William and Pedrinho, Alexandre and Pérez-López, Edel},
  title = {{Rethinking metagenome-assembled genome completeness: are we truly recovering complete genomes?}},
  journal = {Frontiers in Microbiology},
  year = {2026},
  volume = {17},
  pages = {1884628},
  doi = {10.3389/fmicb.2026.1884628},
  note = {access: not_obtained (Sources not obtained: seen only as search snippet, not fetched); type: opinion article; not cited; conflict: the reference list annotates its content (an illustrative analysis) while the not-obtained list says it was never fetched; cited as: H1-02 [24]}
}

@article{pasolliExtensiveUnexploredHuman2019,
  author = {Pasolli, Edoardo and Asnicar, Francesco and Manara, Serena and Zolfo, Moreno and Karcher, Nicolai and Armanini, Federica and Beghini, Francesco and Manghi, Paolo and Tett, Adrian and Ghensi, Paolo and Collado, Maria Carmen and Rice, Benjamin L. and DuLong, Casey and Morgan, Xochitl C. and Golden, Christopher D. and Quince, Christopher and Huttenhower, Curtis and Segata, Nicola},
  title = {{Extensive Unexplored Human Microbiome Diversity Revealed by Over 150,000 Genomes from Metagenomes Spanning Age, Geography, and Lifestyle}},
  journal = {Cell},
  year = {2019},
  volume = {176},
  number = {3},
  pages = {649-662.e20},
  doi = {10.1016/j.cell.2019.01.001},
  note = {access: full_text (the search agents' full-text reads; not re-opened at synthesis; Table S2 and Fig. 7 supplementary data not read); cited as: H1-02 [25]}
}

@article{bergComparisonShortreadLongread2025,
  author = {Berg, Maureen and Reiter, Taylor and Emerson, Joanne and Brown, C. Titus and Roux, Simon},
  title = {{Comparison of short-read and long-read metagenome assemblies in a natural soil community highlights systematic bias in recovery of high-diversity populations}},
  journal = {NAR Genomics and Bioinformatics},
  year = {2025},
  volume = {7},
  number = {4},
  pages = {lqaf163},
  doi = {10.1093/nargab/lqaf163},
  note = {access: full_text (re-verified at synthesis via Europe PMC XML, PMC12634412); cited as: H1-02 [26]}
}

@article{kimComprehensiveBenchmarkingMetagenomic2026,
  author = {Kim, Jungyeon and Kim, Nayeon and Cha, Jun Hyung and Ma, Junyeong and Lee, Insuk},
  title = {{Comprehensive benchmarking of metagenomic binning tools reveals key factors for improved genome recovery}},
  journal = {Nature Communications},
  year = {2026},
  volume = {17},
  pages = {3467},
  doi = {10.1038/s41467-026-71521-w},
  note = {access: full_text (re-verified at synthesis via Europe PMC XML, PMC13079874; the critic checked the full text); cited as: H1-02 [27]}
}

@article{johansenUnveilingSoilMicrobial2025,
  author = {Johansen, Pi Lærke and Chatzigiannidou, Ioanna and Berzina, Lelde and Kristiansen, Karsten and Brix, Susanne},
  title = {{Unveiling soil microbial diversity through ultra-deep short-read metagenomic sequencing and co-assembly}},
  journal = {iMeta},
  year = {2025},
  volume = {4},
  number = {5},
  pages = {e70075},
  doi = {10.1002/imt2.70075},
  note = {access: full_text (the search agents' full-text reads; not re-opened at synthesis); cited as: H1-02 [28]}
}

@article{sereikaOxfordNanoporeR102022,
  author = {Sereika, Mantas and Kirkegaard, Rasmus Hansen and Karst, Søren Michael and Michaelsen, Thomas Yssing and Sørensen, Emil Aarre and Wollenberg, Rasmus Dam and Albertsen, Mads},
  title = {{Oxford Nanopore R10.4 long-read sequencing enables the generation of near-finished bacterial genomes from pure cultures and metagenomes without short-read or reference polishing}},
  journal = {Nature Methods},
  year = {2022},
  volume = {19},
  number = {7},
  pages = {823-826},
  doi = {10.1038/s41592-022-01539-7},
  note = {access: full_text (the search agents' full-text reads; not re-opened at synthesis); cited as: H1-02 [29]}
}

@article{singletonConnectingStructureFunction2021,
  author = {Singleton, Caitlin M. and Petriglieri, Francesca and Kristensen, Jannie M. and Kirkegaard, Rasmus H. and Michaelsen, Thomas Y. and Andersen, Martin H. and Kondrotaite, Zivile and Karst, Søren M. and Dueholm, Morten S. and Nielsen, Per H. and Albertsen, Mads},
  title = {{Connecting structure to function with the recovery of over 1000 high-quality metagenome-assembled genomes from activated sludge using long-read sequencing}},
  journal = {Nature Communications},
  year = {2021},
  volume = {12},
  number = {1},
  pages = {2009},
  doi = {10.1038/s41467-021-22203-2},
  note = {access: full_text (the search agents' full-text reads; not re-opened at synthesis); cited as: H1-02 [30]}
}

@article{panDeepSiameseNeural2022,
  author = {Pan, Shaojun and Zhu, Chengkai and Zhao, Xing-Ming and Coelho, Luis Pedro},
  title = {{A deep siamese neural network improves metagenome-assembled genomes in microbiome datasets across different environments}},
  journal = {Nature Communications},
  year = {2022},
  volume = {13},
  number = {1},
  pages = {2326},
  doi = {10.1038/s41467-022-29843-y},
  note = {access: full_text (the search agents' full-text reads; not re-opened at synthesis); cited as: H1-02 [31]}
}

@article{hanBenchmarkingMetagenomicBinning2025,
  author = {Han, Haitao and Wang, Ziye and Zhu, Shanfeng},
  title = {{Benchmarking metagenomic binning tools on real datasets across sequencing platforms and binning modes}},
  journal = {Nature Communications},
  year = {2025},
  volume = {16},
  number = {1},
  pages = {2865},
  doi = {10.1038/s41467-025-57957-6},
  note = {access: full_text (the search agents' full-text reads; not re-opened at synthesis); cited as: H1-02 [32]}
}

@article{parksCheckMAssessingQuality2015,
  author = {Parks, Donovan H. and Imelfort, Michael and Skennerton, Connor T. and Hugenholtz, Philip and Tyson, Gene W.},
  title = {{CheckM: assessing the quality of microbial genomes recovered from isolates, single cells, and metagenomes}},
  journal = {Genome Research},
  year = {2015},
  volume = {25},
  number = {7},
  pages = {1043-1055},
  doi = {10.1101/gr.186072.114},
  note = {access: full_text (per the Search record, the search agents' full-text reads) and not_obtained (Sources not obtained: not fetched (budget), known via Eisenhofer 2023 and Orakov 2021 citations): conflict between the note's lists; background; cited as: H1-02 [33]}
}

@article{rochaSimulation69Microbial2024,
  author = {Rocha, Ulisses and Kasmanas, Jonas Coelho and Toscan, Rodolfo and Sanches, Danilo S. and Magnusdottir, Stefania and Saraiva, Joao Pedro},
  title = {{Simulation of 69 microbial communities indicates sequencing depth and false positives are major drivers of bias in prokaryotic metagenome-assembled genome recovery}},
  journal = {PLOS Computational Biology},
  year = {2024},
  volume = {20},
  number = {10},
  pages = {e1012530},
  doi = {10.1371/journal.pcbi.1012530},
  note = {access: full_text (the search agents' full-text reads; not re-opened at synthesis); cited as: H1-02 [34]}
}

@article{marangaComprehensiveFunctionalAnnotation2023,
  author = {Maranga, Mary and Szczerbiak, Pawel and Bezshapkin, Valentyn and Gligorijevic, Vladimir and Chandler, Chris and Bonneau, Richard and Xavier, Ramnik J. and Vatanen, Tommi and Kosciolek, Tomasz},
  title = {{Comprehensive Functional Annotation of Metagenomes and Microbial Genomes Using a Deep Learning-Based Method}},
  journal = {mSystems},
  year = {2023},
  volume = {8},
  number = {2},
  pages = {e01178-22},
  doi = {10.1128/msystems.01178-22},
  note = {access: full_text (the search agents' full-text reads; not re-opened at synthesis); cited as: H1-02 [35]}
}

@article{sczyrbaCriticalAssessmentMetagenome2017,
  author = {Sczyrba, Alexander and others},
  title = {{Critical Assessment of Metagenome Interpretation: a benchmark of metagenomics software}},
  journal = {Nature Methods},
  year = {2017},
  volume = {14},
  number = {11},
  pages = {1063-1071},
  doi = {10.1038/nmeth.4458},
  note = {access: not_obtained (Sources not obtained; routes tried: not fetched (budget), CAMI II read instead, known only via citing papers; Europe PMC fullTextXML empty, PMC blocked); listed twice; incomplete: author (the note gives et al.; the critic: breaks the complete-reference rule, H1-02:C-062)}
}

@article{parksRecoveryNearly82017,
  author = {Parks, Donovan H. and others},
  title = {{Recovery of nearly 8,000 metagenome-assembled genomes substantially expands the tree of life}},
  journal = {Nature Microbiology},
  year = {2017},
  volume = {2},
  pages = {1533-1542},
  doi = {10.1038/s41564-017-0012-7},
  note = {access: not_obtained (Sources not obtained; routes tried: Europe PMC DOI search, no PMCID); incomplete: author, number (the note gives et al., H1-02:C-062)}
}

@article{chklovskiCheckM2RapidScalable2023,
  author = {Chklovski, Alex and Parks, Donovan H. and Woodcroft, Ben J. and Tyson, Gene W.},
  title = {{CheckM2: a rapid, scalable and accurate tool for assessing microbial genome quality using machine learning}},
  journal = {Nature Methods},
  year = {2023},
  volume = {20},
  number = {8},
  pages = {1203-1212},
  doi = {10.1038/s41592-023-01940-w},
  note = {access: not_obtained (Sources not obtained; routes tried: no PMC copy, not open access; bioRxiv preprint not fetched); listed twice; title and issue as corrected by the critic (H1-02:C-067)}
}

@article{chenAccurateCompleteGenomes2020,
  author = {Chen, Lin-Xing and Anantharaman, Karthik and Shaiber, Alon and Eren, A. Murat and Banfield, Jillian F.},
  title = {{Accurate and complete genomes from metagenomes}},
  journal = {Genome Research},
  year = {2020},
  volume = {30},
  number = {3},
  pages = {315-333},
  doi = {10.1101/gr.258640.119},
  note = {access: full_text (obtained via Europe PMC, PMC7111523, but only skimmed by keyword; no findings extracted); listed twice under Sources not obtained; not cited}
}

@article{sahebkashafIntegratingCultivationMetagenomics2021,
  author = {Saheb Kashaf, Sara and others},
  title = {{Integrating cultivation and metagenomics for a multi-kingdom view of skin microbiome diversity and functions}},
  journal = {Nature Microbiology},
  year = {2022},
  volume = {7},
  pages = {169-179},
  doi = {10.1038/s41564-021-01011-w},
  note = {access: not_obtained (Sources not obtained; routes tried: Europe PMC fullTextXML empty; PMC HTML not attempted); listed twice; incomplete: author, number (the note gives et al., H1-02:C-063)}
}

@article{voslooEvaluatingIDe2021,
  author = {Vosloo, Solize and Huo, Linxuan and Anderson, Christopher L. and Dai, Zihan and Sevillano, Maria and Pinto, Ameet},
  title = {{Evaluating de Novo Assembly and Binning Strategies for Time Series Drinking Water Metagenomes}},
  journal = {Microbiology Spectrum},
  year = {2021},
  volume = {9},
  number = {3},
  pages = {e01434-21},
  doi = {10.1128/Spectrum.01434-21},
  note = {access: full_text (obtained, PMC8567270, but only the abstract and keyword hits read); listed twice under Sources not obtained; not cited; not Crossref-checked (the critic: contrary to Common rule 8, H1-02:C-068)}
}

@article{delgadoEvaluatingMetagenomicAssembly2022,
  author = {Delgado, Luis Fernando and Andersson, Anders F.},
  title = {{Evaluating metagenomic assembly approaches for biome-specific gene catalogues}},
  journal = {Microbiome},
  year = {2022},
  volume = {10},
  pages = {72},
  doi = {10.1186/s40168-022-01259-2},
  note = {access: full_text (obtained, PMC9074274, but only the abstract read; concerns gene catalogues, not genome bins); listed twice under Sources not obtained; not cited; not Crossref-checked (H1-02:C-068)}
}

@article{conradTowardQuantifyingAdaptive2021,
  author = {Conrad, Roth E. and Viver, Tomeu and Gago, Juan F. and Hatt, Janet K. and Venter, Stephanus N. and Rossello-Mora, Ramon and Konstantinidis, Konstantinos T.},
  title = {{Toward quantifying the adaptive role of bacterial pangenomes during environmental perturbations}},
  journal = {The ISME Journal},
  year = {2022},
  volume = {16},
  number = {5},
  pages = {1222-1234},
  doi = {10.1038/s41396-021-01149-9},
  note = {access: not_obtained (Sources not obtained; routes tried: not in the Europe PMC OA subset; PMC HTML blocked by reCAPTCHA; the bioRxiv preprint 10.1101/2021.03.15.435471 seen only through a web-fetch summary)}
}

@article{puentesanchezExploringEnvironmentalIntraspecies2023,
  author = {Puente-S{\'a}nchez, Fernando and Hoetzinger, Matthias and Buck, Moritz and Bertilsson, Stefan},
  title = {{Exploring environmental intra-species diversity through non-redundant pangenome assemblies}},
  journal = {Molecular Ecology Resources},
  year = {2023},
  doi = {10.1111/1755-0998.13826},
  note = {access: not_obtained (Sources not obtained; routes tried: no PMC full text; the bioRxiv preprint 10.1101/2022.03.25.485477 seen only through a web-fetch summary); incomplete: volume, pages (H1-02:C-068)}
}

@article{gabrielaiteGenAPIToolGene2020,
  author = {Gabrielaite, Migle and Marvig, Rasmus L.},
  title = {{GenAPI: a tool for gene absence-presence identification in fragmented bacterial genome sequences}},
  journal = {BMC Bioinformatics},
  year = {2020},
  volume = {21},
  pages = {320},
  doi = {10.1186/s12859-020-03657-5},
  note = {access: not_obtained (Sources not obtained; routes tried: identified via Europe PMC, PMC7372895, not downloaded, time budget); volume and article number from memory, not confirmed against Crossref (H1-02:C-068)}
}

@article{bickhartGeneratingLineageresolvedComplete2022,
  author = {Bickhart, Derek M. and Kolmogorov, Mikhail and Tseng, Elizabeth and Portik, Daniel M. and Korobeynikov, Anton and Tolstoganov, Ivan and Uritskiy, Gherman and Liachko, Ivan and Sullivan, Shawn T. and Shin, Sung Bong and Zorea, Alvah and Andreu, Vict{\`o}ria Pascal and Panke-Buisse, Kevin and Medema, Marnix H. and Mizrahi, Itzhak and Pevzner, Pavel A. and Smith, Timothy P. L.},
  title = {{Generating lineage-resolved, complete metagenome-assembled genomes from complex microbial communities}},
  journal = {Nature Biotechnology},
  year = {2022},
  volume = {40},
  pages = {711-719},
  doi = {10.1038/s41587-021-01130-z},
  note = {access: not_obtained (Sources not obtained; routes tried: Europe PMC DOI search, no PMCID, not open access); author list from the critic's Crossref record (H1-02:C-062, C-063); incomplete: number}
}

@article{zhangLongreadAssembledMetagenomic2023,
  author = {Zhang, Zhi-Feng and Liu, Li-Rui and Pan, Yue-Ping and Pan, Jie and Li, Meng},
  title = {{Long-read assembled metagenomic approaches improve our understanding on metabolic potentials of microbial community in mangrove sediments}},
  journal = {Microbiome},
  year = {2023},
  volume = {11},
  pages = {188},
  doi = {10.1186/s40168-023-01630-x},
  note = {access: full_text (obtained via Europe PMC, PMC10464287; compares MAG counts and collinearity, reports no gene-content difference; not used as a finding); listed twice under Sources not obtained; authors, volume and article number from the critic's Crossref record (H1-02:C-064..066)}
}

@article{alnebergGenomesUncultivatedProkaryotes2018,
  author = {Alneberg, J. and others},
  title = {{Genomes from uncultivated prokaryotes: a comparison of metagenome-assembled and single-amplified genomes}},
  journal = {Microbiome},
  year = {2018},
  volume = {6},
  pages = {173},
  doi = {10.1186/s40168-018-0550-0},
  note = {access: not stated (named by the critic as missed by the search, H1-02:C-070; PMC6162917); incomplete: author}
}

@article{lobbAssessmentGenomeAnnotation2020,
  author = {Lobb, B. and Tremblay, B. J.-M. and Moreno-Hagelsieb, G. and Doxey, A. C.},
  title = {{An assessment of genome annotation coverage across the bacterial tree of life}},
  journal = {Microbial Genomics},
  year = {2020},
  volume = {6},
  number = {3},
  doi = {10.1099/mgen.0.000341},
  note = {access: not stated (named by the critic in a coverage gap, H1-02:C-079..081); incomplete: pages}
}

@article{bowersMinimumInformationSingle2017,
  author = {{The Genome Standards Consortium} and Bowers, Robert M. and Kyrpides, Nikos C. and Stepanauskas, Ramunas and others},
  title = {{Minimum information about a single amplified genome (MISAG) and a metagenome-assembled genome (MIMAG) of bacteria and archaea}},
  journal = {Nature Biotechnology},
  year = {2017},
  volume = {35},
  number = {8},
  pages = {725-731},
  doi = {10.1038/nbt.3893},
  note = {background; access: abstract_only (the Crossref record, for the background check)}
}

@article{tettelinGenomeAnalysisMultiple2005,
  author = {Tettelin, Herv{\'e} and Masignani, Vega and Cieslewicz, Michael J. and others},
  title = {{Genome analysis of multiple pathogenic isolates of Streptococcus agalactiae: Implications for the microbial pan-genome}},
  journal = {Proceedings of the National Academy of Sciences},
  year = {2005},
  volume = {102},
  number = {39},
  pages = {13950-13955},
  doi = {10.1073/pnas.0506758102},
  note = {background; access: abstract_only (the Crossref record, for the background check)}
}
```
