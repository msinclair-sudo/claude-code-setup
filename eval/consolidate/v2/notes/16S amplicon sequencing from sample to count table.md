---
type: knowledge
title: 16S amplicon sequencing from sample to count table
inputs:
  - "MB-01: Topics/Biology/Research/Results/From sample to count table in 16S rRNA gene amplicon sequencing where counts depart from community composition, what the workflow's quantities measure, and how samples with unequal depth or load are compared. A literature review.md"
  - "MB-02: Topics/Biology/Research/Results/16S rRNA gene copies per genome and per cell, abundance and rarity terms, and abundance in soil. A literature review.md"
refs: PhD/Proposal/Refs/Refs.bib
built: 2026-10-21
status: draft
tags:
  - research
  - knowledge
---
# 16S amplicon sequencing from sample to count table

> [!abstract] Note Role
> **Contains**: what the research in the inputs found, one claim per finding, organised by concept, with the standing, conditions and sources the notes give, and links back to where each was verified.
> **Cannot contain**: anything not in the inputs (except background entries, marked), verification (it stays in the result notes), or guidance on writing, story or order of telling.
> **Order**: the concepts are listed in one valid ordering of the `needs` graph. It has no narrative meaning; other valid orderings are equally correct.

## Inputs
| id | note | critique | citations | standing labels | run record | omission check |
|---|---|---|---|---|---|---|
| MB-01 | [[From sample to count table in 16S rRNA gene amplicon sequencing where counts depart from community composition, what the workflow's quantities measure, and how samples with unequal depth or load are compared. A literature review]] | yes | labelled (access; class; standing) | yes (130 of 147 labels) | yes | exact (every labelled sentence, every answer sentence, and the critique) |
| MB-02 | [[16S rRNA gene copies per genome and per cell, abundance and rarity terms, and abundance in soil. A literature review]] | yes | numbered | no | no | fallback (answers and critique; the note has no labelled citations) |

## Concepts
### workflow: steps from sample to count table
needs: none

- **workflow.1** Twelve steps from sample to count table are documented, each with named alternatives; there is no conflict over what the steps are.
  conf: not stated · class: not stated · holds: documented in protocols, software documentation and benchmarks, mostly full text; makers' statements labelled as such; the procedural descriptions would not change if any single source were removed · src: none (the reviewer's synthesis of the step descriptions in section 2) · trail: MB-01 §2. Steps, §critic · from: MB-01:A-001, MB-01:A-018, MB-01:A-020, MB-01:A-032, MB-01:A-294, MB-01:A-295, MB-01:C-001, MB-01:C-002, MB-01:B-0098..0099 · rating: "Strong for the existence of these choices and the alternatives used"
- **workflow.2** How often each choice is made across the field is unmeasured, apart from the use of controls.
  conf: not stated · class: search (note: "No source found on how often each choice is used across the field") · holds: the only usage survey is Hornung 2019, which covers controls and is not 16S-specific (see contamination.9) · src: hornungIssuesCurrentStandards2019 (FT; meas; single) · trail: MB-01 §critic, §answers · from: MB-01:A-019, MB-01:A-026, MB-01:C-009, MB-01:C-005 · rating: "weak on how often each is used"
- **workflow.3** Within steps the recommended choice is disputed: quality-filter stringency (Bokulich 2013 versus Kopylova 2016), OTUs versus ASVs (Schloss 2021 versus the ASV developers), and pooled versus single PCR (Marotz 2019 and Smith and Peay 2014 versus the triplicate pooling in the EMP protocol).
  conf: cont (note: "Within steps, the recommended choice is disputed") · class: not stated · holds: disputes over recommendations, reported in detail under quality-filtering, denoising-clustering and pcr · src: bokulichQualityfilteringVastlyImproves2013 (FT; meas; repl), kopylovaOpensourceSequenceClustering2016 (FT; meas; cont), schlossAmpliconSequenceVariants2021 (FT; deriv; cont), marotzTriplicatePCRReactions2019 (AB; meas; repl), smithSequenceDepthNot2014 (FT; meas; INDIRECT), earth16SIlluminaAmplicon (PROTOCOL) · trail: MB-01 §answers, §2.9, §2.10, §2.4 · from: MB-01:A-021, MB-01:A-022, MB-01:A-023, MB-01:A-024, MB-01:A-025

### departure: departure of observed composition from the sampled community
needs: workflow

- **departure.1** Every mock-community study in the body found observed composition departing from known composition.
  conf: repl (critic: MB-01:C-010) · class: meas (note: "Every mock-community comparison found") · holds: mock-community and dilution studies with known composition, full text (D'Amore 2016, Fouhy 2016, Pinto and Raskin 2012, Brooks 2015, Karstens 2019, Silverman 2021, Sze and Schloss 2019); the existence of departures, not their size; the brief presupposed departures exist, and independent support for their existence is yes · src: damoreComprehensiveBenchmarkingStudy2016 (FT; meas; repl), fouhy16SRRNAGene2016 (FT; meas; repl), pintoPCRBiasesDistort2012 (FT; meas; repl), brooksTruthMetagenomicsQuantifying2015 (FT; meas; cont), karstensControllingContaminantsLowbiomass2019 (FT; meas; single), silvermanMeasuringMitigatingPCR2021 (FT; meas; single), szeImpactDNAPolymerase2019 (FT, re-opened; meas; single) · trail: MB-01 §1. Overview, §critic · from: MB-01:C-010, MB-01:C-144, MB-01:C-145, MB-01:C-146, MB-01:A-034, MB-01:A-301, MB-01:B-0088 · rating: "strong qualitatively"
- **departure.2** The size of the bias depends on platform, region, primer, extraction and pipeline.
  conf: mixed (marker) · class: meas (marker) · holds: mock-community comparisons; three sources labelled replicated and Brooks 2015 contested · src: damoreComprehensiveBenchmarkingStudy2016 (FT; meas; repl), fouhy16SRRNAGene2016 (FT; meas; repl), pintoPCRBiasesDistort2012 (FT; meas; repl), brooksTruthMetagenomicsQuantifying2015 (FT; meas; cont) · trail: MB-01 §1. Overview · from: MB-01:I-0001
- **departure.3** Departures were measured at most of the steps examined, not at all of them: field sampling for water and host tissue was not searched, and several choices showed little or no detectable effect (PCR replicate pooling, preparation day and lane, cycle number in some studies, and storage in one soil).
  conf: not stated · class: not stated · holds: the critic's correction of the answer's "departures found at every step" · src: none (the critic's reading of the review's body and search record) · trail: MB-01 §critic, §7. Bounds · from: MB-01:C-011, MB-01:C-012, MB-01:C-013, MB-01:C-147, MB-01:C-148, MB-01:C-149, MB-01:B-0410
- **departure.4** For the number of taxa detected, inflation by spurious sequences (sequencing error, chimeras, cross-sample leakage, reagent contamination) and by the choice of clustering or denoising is the largest distortion: 10 to 200-fold excess units (Straub 2020) and contaminants rising from 0.1% to 80.1% of reads in a diluted mock (Karstens 2019); counts of taxa can change by one to two orders of magnitude.
  conf: repl (critic: MB-01:C-014) · class: meas (note: "replicated across independent mocks and dilution series") · holds: independent mocks and dilution series; number of taxa detected, kept apart from relative abundance as the brief asks · src: straubInterpretationsEnvironmentalMicrobial2020 (FT; meas; repl), karstensControllingContaminantsLowbiomass2019 (FT; meas; single) · trail: MB-01 §1. Overview, §critic · from: MB-01:C-014, MB-01:A-298, MB-01:B-0089, MB-01:B-0092, MB-01:B-0093 · rating: "moderate for the inflation of taxon counts"
- **departure.5** For relative abundance, the ordering in which extraction is the largest step, followed by PCR and then sequencing (fold errors of about 2 to 30 or more between taxon pairs), rests on one 7-taxon vaginal dataset (Brooks 2015, reanalysed by McLaren 2019), with Albertsen 2015 (sludge, bead beating only) as partial support; it is contested by Fouhy 2016 and qualified by MBQC (specimen type mattered more than extraction).
  conf: single (critic: MB-01:C-017) · class: not stated · holds: one re-analysed 454 dataset of 7 taxa; not a field-wide ordering · src: mclarenConsistentCorrectableBias2019 (FT, re-opened; deriv/model; single dataset), brooksTruthMetagenomicsQuantifying2015 (FT; meas; cont), albertsenBackBasicsInfluence2015 (FT; meas; repl), fouhy16SRRNAGene2016 (FT; meas; repl), sinhaAssessmentVariationMicrobial2017 (FT; meas; single) · trail: MB-01 §critic, §2.2, §1. Overview · from: MB-01:C-015, MB-01:C-016, MB-01:C-017, MB-01:C-084, MB-01:A-131, MB-01:A-297, MB-01:B-0090, MB-01:B-0091 · rating: "weak for per-step relative-abundance magnitudes"
- **departure.6** Per-step magnitudes mostly come from one or two small mocks of 7 to 20 taxa, often on 454 or Ion Torrent.
  conf: not stated · class: not stated · holds: magnitudes of relative-abundance error per step · src: none (the reviewer's and critic's summary of the sources) · trail: MB-01 §critic, §answers · from: MB-01:C-018, MB-01:A-113 · rating: "weak for per-step relative-abundance magnitudes"
- **departure.7** Across 15 laboratories, variability depended most on specimen type, then DNA extraction, then the handling laboratory, then bioinformatics (MBQC).
  conf: single (marker) · class: meas (marker) · holds: interlaboratory study, 15 laboratories · src: sinhaAssessmentVariationMicrobial2017 (FT; meas; single) · trail: MB-01 §2.2 · from: MB-01:I-0011, MB-01:A-105
- **departure.8** In mocks, 16S read frequencies had essentially no correlation ("no meaningful correlation") with species frequencies.
  conf: single (note: "reported as a single-source contrary result") · class: not stated · holds: one preprint by the tool's author, abstract only; it conflicts with the good fits obtained by Brooks, McLaren and Silverman · src: edgarUNBIASAttemptCorrect2017 (AB; PREPRINT; meas; single) · trail: MB-01 §2.14, MB-02 §D1.4 · from: MB-01:A-106, MB-01:B-0255, MB-01:B-0256, MB-02:B-0213, MB-02:A-044
- **departure.9** A review states that PCR-based estimates can deviate by "several orders of magnitude" if extraction, PCR, copy number and analysis errors are ignored.
  conf: not stated · class: assert (marker) · holds: a review, abstract only · src: bonkPCRbasedQuantificationTaxaspecific2018 (AB; assert) · trail: MB-01 §2.14 · from: MB-01:I-0077

### sample-storage: field sampling, preservation, storage and sample mass
needs: departure

- **sample-storage.1** Documented preservation choices are freezing or refrigeration, 95% ethanol, FTA cards, OMNIgene Gut, 70% ethanol or none, for various times and temperatures.
  conf: not stated · class: not stated · holds: documented choices across studies · src: songPreservationMethodsDiffer2016 (FT; meas; repl), rubinInvestigatingImpactStorage2013 (FT; meas; repl) · trail: MB-01 §2.1 · from: MB-01:A-002, MB-01:B-0134
- **sample-storage.2** Sample mass can also be chosen; in soil it ranged from 0.25 to 100 g.
  conf: not stated · class: not stated · holds: one agricultural field · src: pentonSizeMattersAssessing2016 (FT; meas; single) · trail: MB-01 §2.1 · from: MB-01:A-003
- **sample-storage.3** Human and dog faeces held at ambient temperature for 8 weeks in 95% ethanol, on FTA cards or in OMNIgene Gut changed by about as much as technical replicates differ; unpreserved samples and 70% ethanol changed by amounts comparable to differences between individual humans.
  conf: repl (marker) · class: meas (marker) · holds: faeces, 8 weeks at ambient temperature · src: songPreservationMethodsDiffer2016 (FT; meas; repl) · trail: MB-01 §2.1 · from: MB-01:I-0004, MB-01:A-038, MB-01:B-0104, MB-01:B-0105, MB-01:B-0135
- **sample-storage.4** Storage altered taxon frequencies more than presence or absence: weighted UniFrac effects exceeded unweighted, and the number of taxa detected was affected less.
  conf: not stated · class: not stated · holds: faeces (Song 2016) · src: songPreservationMethodsDiffer2016 (FT; meas; repl) · trail: MB-01 §2.1 · from: MB-01:B-0136, MB-01:A-037, MB-01:A-039
- **sample-storage.5** FTA cards produced a systematic shift that could be detrended, the one storage effect shown to be consistent across samples; for the other methods consistency was not measured.
  conf: not stated · class: not stated · holds: faeces (Song 2016) · src: songPreservationMethodsDiffer2016 (FT; meas; repl) · trail: MB-01 §2.1 · from: MB-01:B-0137, MB-01:A-040, MB-01:B-0106, MB-01:B-0107
- **sample-storage.6** Storage for 1 to 14 days at room temperature, 4 C or -20 C changed a single soil's community, most at 3 to 7 days and least when frozen; these changes were small relative to differences among more than 500 Earth Microbiome Project soils.
  conf: repl (marker) · class: meas (marker) · holds: a single soil compared against more than 500 EMP soils · src: rubinInvestigatingImpactStorage2013 (FT; meas; repl) · trail: MB-01 §2.1 · from: MB-01:I-0005, MB-01:A-041, MB-01:B-0138, MB-01:B-0411
- **sample-storage.7** In one agricultural field, extracting 0.25, 1, 5, 10 or 100 g of soil changed community structure, replicate dispersion and OTU counts; 10 g extractions gave the highest diversity and the lowest dispersion.
  conf: single (marker) · class: meas (marker) · holds: one agricultural field · src: pentonSizeMattersAssessing2016 (FT; meas; single) · trail: MB-01 §2.1 · from: MB-01:I-0006, MB-01:B-0140, MB-01:B-0141
- **sample-storage.8** Field sampling choices for water (volume filtered, filter pore size) and for host tissue are unsearched on the review's own search record, not "not found".
  conf: not stated · class: search (critic: MB-01:C-008) · holds: the review's section 2.1 says the lab angle searched preservation and storage terms through Crossref, Europe PMC and web search; its search record says no angle searched water or host-tissue sampling · src: none (the review's search record) · trail: MB-01 §critic, §Search record · from: MB-01:C-006, MB-01:C-007, MB-01:C-008, MB-01:C-012, MB-01:A-027, MB-01:B-0018, MB-01:B-0143, MB-01:B-0450

### extraction: DNA extraction
needs: departure

- **extraction.1** Documented extraction choices are the kit, bead-beating intensity, plate or single tube, and whether relic DNA is removed with PMA or DNase.
  conf: not stated · class: not stated · holds: lab protocols and benchmarks · src: albertsenBackBasicsInfluence2015 (FT; meas; repl), minichQuantifyingUnderstandingWelltowell2019 (FT; meas; single), cariniRelicDNAAbundant2016 (AB; meas; cont), lennonHowWhereRelic2018 (FT; meas; cont) · trail: MB-01 §2.2 · from: MB-01:A-004
- **extraction.2** In McLaren's reanalysis of Brooks's 80 cell mixtures of 7 vaginal taxa (V1-V3, 454), the extraction step had a maximum pairwise bias of 36.6-fold and a mean of 5.5-fold; PCR followed (maximum 5.2, mean 2.3), then sequencing and classification (maximum 1.6, mean 1.2).
  conf: single (marker) · class: deriv/model (marker) · holds: one 7-taxon cell-mixture dataset, 454; the largest single step in this mock; figures checked against the re-opened full text · src: mclarenConsistentCorrectableBias2019 (FT, re-opened; deriv/model; single dataset), brooksTruthMetagenomicsQuantifying2015 (FT; meas; cont) · trail: MB-01 §2.2, §critic · from: MB-01:I-0007, MB-01:A-042, MB-01:A-043, MB-01:B-0108, MB-01:B-0144, MB-01:B-0145
- **extraction.3** Total bias in the same cell mixtures was a maximum of 29.3-fold and a mean of 5.6-fold, smaller than extraction bias alone, which the review reads as partial cancellation between steps.
  conf: not stated · class: reading (note: "which implies partial cancellation between steps") · holds: the 7-taxon cell mixtures (McLaren 2019 reanalysis) · src: mclarenConsistentCorrectableBias2019 (FT, re-opened) · trail: MB-01 §2.2 · from: MB-01:B-0146, MB-01:B-0147
- **extraction.4** Brooks et al. reported a median total bias per taxon ranging from -32.6% to +39.1% of the true proportion.
  conf: cont (marker) · class: meas (marker) · holds: 7-taxon vaginal cell mixtures · src: brooksTruthMetagenomicsQuantifying2015 (FT; meas; cont) · trail: MB-01 §2.2 · from: MB-01:I-0008, MB-01:B-0148, MB-01:I-0007
- **extraction.5** Swapping extraction kits changed Enterococcus by about 50%.
  conf: cont (marker) · class: meas (marker) · holds: 7-taxon vaginal cell mixtures · src: brooksTruthMetagenomicsQuantifying2015 (FT; meas; cont) · trail: MB-01 §2.2 · from: MB-01:I-0008, MB-01:B-0150, MB-01:I-0007
- **extraction.6** In activated sludge, bead-beating intensity and primer choice had the largest effects of all parameters tested; harder beating increased DNA from Gram-positive bacteria by up to 400%.
  conf: repl (marker) · class: meas (marker) · holds: activated sludge; bead beating only · src: albertsenBackBasicsInfluence2015 (FT; meas; repl) · trail: MB-01 §2.2 · from: MB-01:I-0009, MB-01:A-044, MB-01:B-0109, MB-01:B-0151
- **extraction.7** In a 20-species gut mock, two extraction methods (QIAamp stool kit versus repeat bead beating) gave "very similar" data; primer and platform mattered more.
  conf: repl (marker) · class: meas (marker) · holds: one gut mock of 20 species · src: fouhy16SRRNAGene2016 (FT; meas; repl) · trail: MB-01 §2.2 · from: MB-01:I-0010, MB-01:A-045, MB-01:B-0110, MB-01:B-0152, MB-01:B-0415
- **extraction.8** The size of the extraction effect is contested: Fouhy 2016 against Albertsen 2015, Brooks 2015 and MBQC.
  conf: cont (critic: MB-01:C-016) · class: not stated · holds: mocks and sludge; see extraction.6, extraction.7, departure.7 · src: fouhy16SRRNAGene2016 (FT; meas; repl), albertsenBackBasicsInfluence2015 (FT; meas; repl), brooksTruthMetagenomicsQuantifying2015 (FT; meas; cont), sinhaAssessmentVariationMicrobial2017 (FT; meas; single) · trail: MB-01 §6. Where, §answers · from: MB-01:A-117, MB-01:B-0401, MB-01:C-016
- **extraction.9** In MBQC's artificial communities, the largest contributor to inaccuracy was contamination or omission of microbes whose DNA was not extracted.
  conf: not stated · class: not stated · holds: interlaboratory artificial communities · src: sinhaAssessmentVariationMicrobial2017 (FT; meas; single) · trail: MB-01 §2.2 · from: MB-01:B-0153, MB-01:A-046
- **extraction.10** No more than 6% of inoculated lambda DNA was recovered from six soils.
  conf: repl (marker) · class: meas (marker) · holds: older soil work, pre-NGS, INDIRECT · src: frostegardQuantificationBiasRelated1999 (AB; meas; repl) · trail: MB-01 §2.2 · from: MB-01:I-0014
- **extraction.11** Extraction method changed soil fingerprint profiles.
  conf: repl (marker) · class: meas (marker) · holds: older soil work, pre-NGS, INDIRECT · src: martinlaurentDNAExtractionSoils2001 (AB; meas; repl) · trail: MB-01 §2.2 · from: MB-01:I-0015
- **extraction.12** No mock study in a soil matrix with known composition was found; soil evidence comes from spike-ins, dilutions and relic DNA.
  conf: not stated · class: search (note: "No mock study in soil matrix with known composition was found") · holds: lab and bioinformatics angles · src: none (the review's search) · trail: MB-01 §answers · from: MB-01:A-124, MB-01:A-126

### primers: primers and gene region
needs: departure

- **primers.1** Documented primer choices include V1-V2 through V7-V9 and full length, degenerate variants of 515F and 806R, and PNA clamps against host plastids; in silico surveys cover 175 primers and 512 pairs.
  conf: not stated · class: not stated · holds: primer surveys and protocols · src: waltersImprovedBacterial16S2016 (FT; meas; repl), abellanschneyderPrimerPipelinesParameters2021 (FT; meas; repl), fitzpatrickChloroplastSequenceVariation2018 (FT; meas; single), klindworthEvaluationGeneral16S2013 (FT; deriv; repl) · trail: MB-01 §2.3 · from: MB-01:A-005, MB-01:A-006
- **primers.2** In silico, 175 primers and 512 pairs differ widely in coverage and phylum spectrum against SILVA 108.
  conf: repl (marker) · class: deriv (marker) · holds: in silico, SILVA 108 · src: klindworthEvaluationGeneral16S2013 (FT; deriv; repl) · trail: MB-01 §2.3 · from: MB-01:I-0017
- **primers.3** The original 515F/806R V4 primers under-represented SAR11 and over-represented Gammaproteobacteria in marine samples.
  conf: repl (marker) · class: meas (marker) · holds: marine field samples; abstract only · src: paradaEveryBaseMatters2016 (AB; meas; repl) · trail: MB-01 §2.3 · from: MB-01:I-0018
- **primers.4** For the 515F-Y/806R pair, bias against SAR11 was about 4 to 10-fold in marine field samples but only about 2-fold in mocks, so mock-measured bias understated field bias for this taxon.
  conf: single (critic: MB-01:C-092) · class: not stated · holds: one primer pair (515F-Y/806R), one taxon (SAR11), abstract only; the review attributed the figures to the original 515F/806R pair, which the critic corrected · src: paradaEveryBaseMatters2016 (AB; meas; repl) · trail: MB-01 §critic, §2.3 · from: MB-01:C-056, MB-01:C-070, MB-01:C-092, MB-01:B-0113, MB-01:B-0161, MB-01:B-0162, MB-01:B-0252
- **primers.5** On marine clone mocks, 515F-Y/926R fit expected composition with r2 = 0.95, against about 0.5 for 515F-Y/806R.
  conf: not stated · class: not stated · holds: marine clone mocks; abstract only · src: paradaEveryBaseMatters2016 (AB) · trail: MB-01 §2.3 · from: MB-01:B-0160
- **primers.6** Even perfectly matched primers showed preferential amplification.
  conf: not stated · class: not stated · holds: marine mocks; abstract only · src: paradaEveryBaseMatters2016 (AB) · trail: MB-01 §2.3 · from: MB-01:B-0163, MB-01:I-0018, MB-01:B-0160
- **primers.7** Adding degeneracy to 515F and 806R improved detection of Thaumarchaeota and SAR11 in stool, soil and built-environment sets without degrading other taxa.
  conf: repl (marker) · class: meas (marker) · holds: stool, soil and built-environment sets · src: waltersImprovedBacterial16S2016 (FT; meas; repl) · trail: MB-01 §2.3 · from: MB-01:I-0019, MB-01:A-055
- **primers.8** In human stool and mocks with seven primer pairs, Verrucomicrobia appeared only with V3-V4, V4, V6-V8 and V7-V9 primers: whole phyla appeared or disappeared with primer choice.
  conf: repl (marker) · class: meas (marker) · holds: human stool and mocks, seven primer pairs · src: abellanschneyderPrimerPipelinesParameters2021 (FT; meas; repl) · trail: MB-01 §2.3 · from: MB-01:I-0020, MB-01:A-054, MB-01:B-0114
- **primers.9** In a gut mock, 55 to 80% of expected species were detected, and 29 to 80% of detected species were misidentified or false hits, depending on primer, platform and extraction.
  conf: not stated · class: not stated · holds: one gut mock · src: fouhy16SRRNAGene2016 (FT) · trail: MB-01 §2.3 · from: MB-01:B-0164
- **primers.10** Preferential amplification of a matched template over a mismatched one (63F) rose almost exponentially as annealing temperature went from 47 to 61 C; a perfectly matched primer showed no such effect.
  conf: single (marker) · class: meas (marker) · holds: T-RFLP, pre-NGS; abstract only · src: siposEffectPrimerMismatch2007 (AB; meas; single; T-RFLP, pre-NGS) · trail: MB-01 §2.3 · from: MB-01:I-0021, MB-01:B-0165
- **primers.11** With universal PNA clamps, host plastid reads averaged 23% across 32 plant species but reached 62 to 94% in some lineages.
  conf: single (marker) · class: meas (marker) · holds: plant roots, 32 species · src: fitzpatrickChloroplastSequenceVariation2018 (FT; meas; single) · trail: MB-01 §2.3 · from: MB-01:I-0022, MB-01:A-053
- **primers.12** A modified clamp cut Asteraceae contamination from 65% to 23% but raised it from 12% to 69% in other species.
  conf: not stated · class: not stated · holds: plant samples · src: fitzpatrickChloroplastSequenceVariation2018 (FT) · trail: MB-01 §2.3 · from: MB-01:B-0166
- **primers.13** PNA type did not detectably change bacterial alpha or beta diversity.
  conf: not stated · class: not stated · holds: plant samples · src: fitzpatrickChloroplastSequenceVariation2018 (FT) · trail: MB-01 §2.3, §7. Bounds · from: MB-01:B-0167, MB-01:B-0417, MB-01:I-0022
- **primers.14** The makers of PCR clamps state that clamps enrich microbial sequences "without introducing bias".
  conf: not stated · class: assert (note: "The makers of PCR clamps state") · holds: makers' claim, abstract only · src: lundbergPracticalInnovationsHighthroughput2013 (AB; makers' claim) · trail: MB-01 §2.3 · from: MB-01:B-0168
- **primers.15** In silico, 56% of V4 amplicons failed to match their species of origin with confidence, while full-length sequences classified nearly all correctly.
  conf: single (marker) · class: deriv (marker) · holds: in silico · src: johnsonEvaluation16SRRNA2019 (FT; deriv; single) · trail: MB-01 §2.3 · from: MB-01:I-0023

### copy-number: 16S rRNA gene copies per genome
needs: none

- **copy-number.1** Bacterial genomes carry 1 to 15 copies of the 16S rRNA gene in every database release and genome survey until about 2015: the first rrnDB release ("one to as many as 15 copies"), the 2009 release (785 bacterial and 69 archaeal strains), the 2015 release (2,635 bacterial records, 1,383 species), Acinas 2004 and Větrovský and Baldrian 2013.
  conf: not stated · class: not stated · holds: sequenced genomes; the MB-02 critic says the sources draw on overlapping NCBI genome sets, so they are not independent replications; MB-02 rates the range "Strong" · src: stoddardRrnDBImprovedTools2015 (FT; deriv; repl), klappenbachRrndbRibosomalRNA2001 (AB), leeRrnDBDocumentingNumber2009 (AB), acinasDivergenceRedundancy16S2004 (AB), vetrovskyVariability16SRRNA2013 (FT) · trail: MB-01 §3.2, MB-02 §D1.1, §D1.2, §critic · from: MB-01:A-142, MB-01:A-168, MB-01:B-0121, MB-01:B-0263, MB-02:A-001, MB-02:A-017, MB-02:A-126, MB-02:C-001, MB-02:C-006, MB-02:B-0092..0095, MB-02:A-009, MB-02:B-0139, MB-02:B-0142 · rating: "Moderate for copy-number ranges across genomes"
- **copy-number.2** Archaea carry 1 to 4 copies in rrnDB to v5.0 (the 2015 release: 175 archaeal records, 148 species) and 1 to 5 from v5.6 onward, but Acinas 2004 already reports a maximum of five archaeal operons, so the sources conflict on the archaeal maximum.
  conf: cont (critic: MB-02:C-002) · class: deriv (marker) · holds: archaeal genomes, few species (148 in 2015); the later rrnDB values are the reviewer's derivation · src: stoddardRrnDBImprovedTools2015 (FT; deriv; repl), schmidtlaboratoryRrnDBReleaseFiles2025 (FT; statistics derived by reviewer), acinasDivergenceRedundancy16S2004 (AB) · trail: MB-02 §critic, §D1.1, §D1.2, MB-01 §3.2 · from: MB-01:I-0079, MB-01:A-144, MB-02:A-002, MB-02:A-127, MB-02:C-002, MB-02:C-138, MB-02:B-0141
- **copy-number.3** Over 1,690 bacterial genomes (909 species, GenBank 2012; 7,081 16S sequences extracted in silico) the mean was 4.2 and the maximum 15; about 15% of genomes carried one copy and 21% two.
  conf: not stated · class: deriv (note: "Vetrovsky and Baldrian 2013, derived") · holds: GenBank genomes, collection skewed; figures checked against full text by the MB-02 critic · src: vetrovskyVariability16SRRNA2013 (FT) · trail: MB-01 §3.2, MB-02 §D1.2 · from: MB-01:B-0265, MB-02:A-003, MB-02:B-0142, MB-02:C-057, MB-01:A-143
- **copy-number.4** Phylum means in Větrovský and Baldrian 2013: Acidobacteria 1.0, Alphaproteobacteria 2.2, Deltaproteobacteria 2.7, Actinobacteria 3.1, Betaproteobacteria 3.3, Bacteroidetes 3.5, Firmicutes 5.8 and Gammaproteobacteria 5.8.
  conf: not stated · class: deriv (note: "Vetrovsky and Baldrian 2013, derived") · holds: GenBank genomes; the Acidobacteria mean rests on 4 genomes from 4 species (their Table 1), presented beside large-n phyla without the n · src: vetrovskyVariability16SRRNA2013 (FT) · trail: MB-01 §3.2, MB-02 §D1.2, §critic · from: MB-01:A-143, MB-01:B-0266, MB-02:B-0143, MB-02:A-004, MB-02:C-003, MB-02:C-089
- **copy-number.5** The low copy numbers for soil-relevant Acidobacteria are imprecise: 1.0 rests on 4 genomes from 4 species (Větrovský and Baldrian) and the rrnDB v5.10 figure of 1.4 on 29 species; the soil correction example (Acidobacteria 50.1% to 66.0%) depends on them.
  conf: not stated · class: not stated · holds: the critic's reading of the sources' sample sizes · src: vetrovskyVariability16SRRNA2013 (FT), schmidtlaboratoryRrnDBReleaseFiles2025 (FT; statistics derived by reviewer) · trail: MB-02 §critic · from: MB-02:C-003, MB-02:C-004, MB-02:C-005
- **copy-number.6** In rrnDB v5.10, the mean of species means is 4.4 (median 4) for bacteria and 1.7 (median 1) for archaea; 11.3% of bacterial species and 51.6% of archaeal species average one copy.
  conf: single (note: "rest on the reviewer's derivation from rrnDB alone") · class: deriv (note: "derived by the reviewer") · holds: rrnDB v5.10 release files (June 2025); species grouped by the first two words of the NCBI name, which is approximate; no published check against assembly quality · src: schmidtlaboratoryRrnDBReleaseFiles2025 (FT; statistics derived by reviewer) · trail: MB-02 §D1.1, §critic · from: MB-02:A-003, MB-02:A-018, MB-02:A-128, MB-02:A-130, MB-02:C-007, MB-02:C-141, MB-02:B-0103, MB-02:B-0118, MB-02:B-0101, MB-02:A-010 · rating: "Moderate for exact means and shares"
- **copy-number.7** Across rrnDB releases v3.1.227, v4.4.3, v5.0, v5.6 and v5.10, bacterial records grew from 1,297 to 48,053, the range from 1 to 15 to 1 to 22, the record mean from 4.20 to 5.52, and the mean of species means from 3.87 to 4.36, while the share of records at one copy fell from 17.5% to 7.5%; the archaeal range went from 1 to 4 to 1 to 5 and the archaeal species mean stayed between 1.66 and 1.73.
  conf: single (note: "rest on the reviewer's derivation from rrnDB alone") · class: deriv (note: "derived by the reviewer") · holds: rrnDB release files; reviewer's computation · src: schmidtlaboratoryRrnDBReleaseFiles2025 (FT; statistics derived by reviewer) · trail: MB-02 §D1.1 · from: MB-02:B-0101..0109, MB-02:A-018
- **copy-number.8** The long-quoted ceiling of 15 is no longer the database maximum: rrnDB v5.6 contains a Photobacterium damselae genome with 21 copies and v5.10 a Mesobacillus maritimus genome with 22, several Photobacterium and Bacillaceae genomes have 20 to 21, and archaea reach 5 (Natronorubrum, Natrinema, Methanococcoides, Methanolobus and others); no source checked whether these extremes survive scrutiny of assembly quality.
  conf: single (note: "rest on the reviewer's derivation from rrnDB alone") · class: deriv (note: "derived by the reviewer") · holds: rrnDB v5.6 and v5.10; the maximum is 15 in every source to about 2015 · src: schmidtlaboratoryRrnDBReleaseFiles2025 (FT; statistics derived by reviewer) · trail: MB-02 §D1.1, §critic · from: MB-02:A-001, MB-02:A-011, MB-02:A-018, MB-02:A-126, MB-02:A-130, MB-02:C-007, MB-02:C-141, MB-02:B-0110..0114
- **copy-number.9** Record-level summaries drift upward across rrnDB releases (record mean 4.2 in v3.1.227 to 5.5 in v5.10) mainly because heavily resequenced species dominate later releases (in v5.10, E. coli contributes 3,902 records, 3,860 at 7 copies; Klebsiella pneumoniae 2,534, mostly 8; Salmonella enterica 1,770, mostly 7); species-level means move much less (3.9 to 4.4).
  conf: not stated · class: deriv (note: "derived by the reviewer") · holds: means differ by counting unit (record mean 5.5 versus species mean 4.4 in the same release) · src: schmidtlaboratoryRrnDBReleaseFiles2025 (FT; statistics derived by reviewer) · trail: MB-02 §D1.1 · from: MB-02:A-005, MB-02:A-010, MB-02:A-012, MB-02:B-0115..0117, MB-02:B-0102 · rating: "Moderate for exact means and shares"
- **copy-number.10** Per-phylum species means in rrnDB v5.10: Bacillota 6.9 (1,274 species), Pseudomonadota 4.4 (3,050), Bacteroidota 3.8 (662), Actinomycetota 3.5 (1,334), Cyanobacteriota 2.8 (102), Planctomycetota 2.0 (62), Verrucomicrobiota 1.8 (35), Chloroflexota 1.6 (20), Acidobacteriota 1.4 (29), Euryarchaeota 1.9 (332), Thermoproteota 1.0 (65), Nitrososphaerota 1.1 (18).
  conf: single (note: "rest on the reviewer's derivation from rrnDB alone") · class: deriv (note: "derived by the reviewer") · holds: rrnDB v5.10 species means · src: schmidtlaboratoryRrnDBReleaseFiles2025 (FT; statistics derived by reviewer) · trail: MB-02 §D1.1 · from: MB-02:A-004, MB-02:A-128, MB-02:B-0120..0132, MB-02:A-018, MB-02:B-0102
- **copy-number.11** Copy number is strongly structured by taxon, with per-taxon means differing several-fold; taxon dependence is the strongest regularity.
  conf: not stated · class: not stated · holds: sequenced genomes in rrnDB and genome surveys; the MB-02 critic says these sources overlap and are not independent replications · src: vetrovskyVariability16SRRNA2013 (FT), schmidtlaboratoryRrnDBReleaseFiles2025 (FT; statistics derived by reviewer), anglyCopyRighterRapidTool2014 (AB) · trail: MB-02 §D1.1, §D1.2 · from: MB-02:A-004, MB-02:A-009, MB-02:A-129, MB-02:B-0119, MB-02:B-0138, MB-02:C-006 · rating: "Strong for the range and the taxon dependence"
- **copy-number.12** Phyla common in soil but poorly represented among genomes (Acidobacteriota, Verrucomicrobiota, Chloroflexota) sit at the low end of copy number, on small numbers of species.
  conf: not stated · class: deriv (note: "derived by the reviewer") · holds: rrnDB v5.10 · src: schmidtlaboratoryRrnDBReleaseFiles2025 (FT; statistics derived by reviewer) · trail: MB-02 §D1.1 · from: MB-02:B-0133, MB-02:B-0102, MB-02:B-0120
- **copy-number.13** Among 301 species with at least two genome records in Stoddard et al.'s rrnDB data (dated 2014 in the answers, the 2015 figure in the body), 77% had identical counts, 16% differed by one copy and 3% by more than two.
  conf: not stated · class: deriv (note: "measured from genomes; derived class") · holds: rrnDB 2015, far fewer genomes than v5.10 · src: stoddardRrnDBImprovedTools2015 (FT) · trail: MB-02 §D1.1 · from: MB-02:A-006, MB-02:B-0098, MB-02:B-0137
- **copy-number.14** In rrnDB v5.10, 44% of the 1,038 species with at least five genomes show some within-species variation in copy number, although the median range is 0.
  conf: not stated · class: deriv (note: "derived by the reviewer") · holds: rrnDB v5.10; conflicts with the 77% identical of 2015, which used far fewer genomes · src: schmidtlaboratoryRrnDBReleaseFiles2025 (FT; statistics derived by reviewer) · trail: MB-02 §D1.1 · from: MB-02:A-006, MB-02:A-013, MB-02:B-0134, MB-02:B-0135, MB-02:B-0137
- **copy-number.15** In the reviewer's reading, part of the within-species variation in rrnDB v5.10 is likely assembly error rather than biology: for example, 18 of 3,902 E. coli records report a single copy.
  conf: not stated · class: reading (note: "In the reviewer's reading") · holds: an untested reading · src: schmidtlaboratoryRrnDBReleaseFiles2025 (FT; statistics derived by reviewer) · trail: MB-02 §D1.1 · from: MB-02:A-013, MB-02:B-0136
- **copy-number.16** Means over all genomes mislead because some species are over-represented, and within-family copy-number distributions can be bimodal (Enterobacteriaceae 1 to 9, with a low-copy peak made up of insect symbionts).
  conf: not stated · class: not stated · holds: rrnDB 2015 · src: stoddardRrnDBImprovedTools2015 (FT; deriv; repl) · trail: MB-01 §3.2, MB-02 §D1.1 · from: MB-01:B-0264, MB-02:B-0096, MB-02:B-0097
- **copy-number.17** From version 5.0 onward, rrnDB counts 16S genes by BLAST against gap-free NCBI assemblies rather than from annotation, so genome records report 16S gene counts only, not operons or 23S counts.
  conf: not stated · class: not stated · holds: rrnDB About page · src: schmidtlaboratoryRrnDBReleaseFiles2025 (FT) · trail: MB-02 §D1.1 · from: MB-02:A-008, MB-02:B-0099, MB-02:B-0100
- **copy-number.18** Bacteria carry up to 15 operons, with copy numbers up to 7 common and about 40% of organisms carrying one or two operons; a single operon dominated in archaea, with a maximum of five.
  conf: not stated · class: not stated · holds: genome survey, abstract only · src: acinasDivergenceRedundancy16S2004 (AB) · trail: MB-02 §D1.2 · from: MB-02:B-0139..0141, MB-02:C-058
- **copy-number.19** Copy number was less conserved across taxonomic levels than genome size.
  conf: not stated · class: not stated · holds: 1,690 bacterial genomes · src: vetrovskyVariability16SRRNA2013 (FT) · trail: MB-02 §D1.2 · from: MB-02:B-0144, MB-02:B-0142
- **copy-number.20** 16S copy number has moderate phylogenetic signal (K = 0.48 on 484 taxa).
  conf: not stated · class: not stated · holds: sequenced genomes; checked against full text by the critic · src: kembelIncorporating16SGene2012 (FT) · trail: MB-02 §D1.2 · from: MB-02:B-0145, MB-02:C-057
- **copy-number.21** Copy number is "strongly linked" to taxonomy (2,900 genomes), and Archaea are potentially under-represented in amplicon profiles.
  conf: not stated · class: not stated · holds: tool-development paper, abstract only · src: anglyCopyRighterRapidTool2014 (AB) · trail: MB-02 §D1.2 · from: MB-02:B-0146
- **copy-number.22** 16S gene counts and operon counts diverge where rRNA genes are unlinked: unlinked 16S and 23S genes are common in Deinococcus-Thermus, Chloroflexi and Planctomycetes, and up to 41% of rRNA genes in soil long-read metagenomes were unlinked, against none in human gut.
  conf: single (note: "This is SINGLE SOURCE for the soil figure") · class: not stated · holds: soil and human-gut long-read metagenomes; abstract only · src: brewerUnlinkedRRNAGenes2020 (AB) · trail: MB-02 §D1.2, §critic · from: MB-02:A-007, MB-02:A-019, MB-02:A-131, MB-02:C-093, MB-02:B-0147..0150
- **copy-number.23** Copies within a genome are not always identical: intragenomic heterogeneity was found in 952 of 2,013 genomes, 87.5% of it below 1% divergence; inflation of unique-sequence richness reached 123.7% for full-length genes but was smaller at 97% clustering.
  conf: not stated · class: not stated · holds: sequenced genomes, abstract only · src: sunIntragenomicHeterogeneity16S2013 (AB) · trail: MB-02 §D1.2 · from: MB-02:B-0151..0153
- **copy-number.24** Operon redundancy gives an upper bound of about threefold diversity overestimation.
  conf: not stated · class: not stated · holds: genome survey, abstract only · src: acinasDivergenceRedundancy16S2004 (AB) · trail: MB-02 §D1.2 · from: MB-02:B-0154
- **copy-number.25** Soil isolates that formed colonies quickly averaged 5.5 copies, against 1.4 for slow responders.
  conf: single (critic: MB-01:C-091) · class: meas (marker) · holds: cultured soil isolates; one abstract-only study; a measured association · src: klappenbachRRNAOperonCopy2000 (AB; meas; repl) · trail: MB-01 §3.2, §critic, MB-02 §D1.2 · from: MB-01:I-0080, MB-01:A-145, MB-01:B-0267, MB-01:C-091, MB-02:B-0155, MB-02:B-0156, MB-02:B-0158
- **copy-number.26** Maximum reproductive rate doubles with a doubling of rRNA operon copy number, across 1,167 species.
  conf: single (marker) · class: meas (marker) · holds: 1,167 species; abstract only; a measured association · src: rollerExploitingRRNAOperon2016 (AB; meas; single) · trail: MB-01 §3.2, MB-02 §D1.2 · from: MB-01:I-0081, MB-02:B-0157, MB-02:B-0158

- **copy-number.bg1** The 16S rRNA gene is present in almost all bacteria, often as a multigene family or operons, and its function has not changed over time.
  kind: background · ref: janda16SRRNAGene2007 · check: DOI 10.1128/JCM.01228-07 resolves on Crossref (J Clin Microbiol 45(9):2761-2764, 2007); stated in the opening paragraph of the open PMC full text (PMC2045242), before the heading "Bacterial Identification Using 16S rRNA Sequencing"

### pcr: PCR conditions, cycle number and per-cycle efficiency
needs: departure, copy-number

- **pcr.1** Documented PCR choices are the polymerase, cycle number, input amount, and single versus pooled replicate reactions.
  conf: not stated · class: not stated · holds: protocols and benchmarks · src: none (the reviewer's synthesis of the PCR literature) · trail: MB-01 §2.4 · from: MB-01:A-007
- **pcr.2** Documented protocols use 35 cycles in triplicate 25 uL reactions, pooling 240 ng per sample (EMP protocol, one-step), or 25 amplicon cycles plus 8 index cycles with 12.5 ng input (Illumina guide, two-step).
  conf: not stated · class: not stated · holds: makers' protocols and documentation; the EMP's 35 cycles in triplicate and 240 ng pooling were checked on the live page by the critic · src: earth16SIlluminaAmplicon (PROTOCOL), illumina16SMetagenomicSequencing (DOCUMENTATION; maker's claim) · trail: MB-01 §3.1, §2.6, §critic · from: MB-01:A-008, MB-01:A-135, MB-01:A-170, MB-01:A-302, MB-01:C-023, MB-01:B-0190, MB-01:B-0191, MB-01:B-0257 · rating: "Moderate for documented cycle numbers"
- **pcr.3** Experiments span 10 to 35 cycles (Silverman 2021), 15 or 20 to 35 (Sze and Schloss 2019), 20 versus 40 (Salter 2014) and 24 (Laursen 2017).
  conf: not stated · class: not stated · holds: experimental studies · src: silvermanMeasuringMitigatingPCR2021 (FT), szeImpactDNAPolymerase2019 (FT, re-opened), salterReagentLaboratoryContamination2014 (FT), laursenGenomicGCcontentAffects2017 (FT) · trail: MB-01 §3.1 · from: MB-01:A-136, MB-01:B-0258
- **pcr.4** Two-template 27F-338R mixtures converged toward 1:1 products regardless of starting ratio; the bias depended strongly on cycle number and fit a kinetic model of product reannealing.
  conf: repl (marker) · class: meas (marker) · holds: two-template mixtures; abstract only · src: suzukiBiasCausedTemplate1996 (AB; meas; repl) · trail: MB-01 §2.4 · from: MB-01:I-0024, MB-01:A-060, MB-01:B-0117, MB-01:B-0169
- **pcr.5** Reproducible over-amplification of specific templates in genomic mixtures was explained largely by primer binding energy, not copy number, and was reduced by higher template concentration, fewer cycles and pooling of reactions.
  conf: repl (marker) · class: meas (marker) · holds: genomic mixtures; abstract only · src: polzBiasTemplatetoproductRatios1998 (AB; meas; repl) · trail: MB-01 §2.4 · from: MB-01:I-0025, MB-01:B-0170
- **pcr.6** In a 20-strain mock, genomic GC content correlated negatively with observed abundance; longer initial denaturation raised the three highest-GC members but did not change overall evenness.
  conf: single (marker) · class: meas (marker) · holds: one 20-strain mock · src: laursenGenomicGCcontentAffects2017 (FT; meas; single) · trail: MB-01 §2.4 · from: MB-01:I-0026, MB-01:A-061, MB-01:B-0118, MB-01:B-0171
- **pcr.7** High-GC templates were also under-represented in Pinto and Raskin's mocks.
  conf: not stated · class: not stated · holds: as reported for Pinto and Raskin 2012 · src: pintoPCRBiasesDistort2012 (FT) · trail: MB-01 §2.4 · from: MB-01:B-0172, MB-01:A-061
- **pcr.8** In a gut-isolate mock with primer mismatch removed by pre-amplification, log-ratios changed linearly with cycle number from 10 to 35 cycles; after 35 cycles relative abundances were biased by an average factor of 2.6 per taxon (95% credible set 2.3 to 2.9), and the B. longum to E. faecalis ratio shifted about 16-fold.
  conf: single (marker) · class: meas (marker) · holds: gut-isolate mock; the per-cycle bias magnitude rests on Silverman 2021 alone; figures checked against full text by the critic · src: silvermanMeasuringMitigatingPCR2021 (FT; meas; single) · trail: MB-01 §2.4, §critic · from: MB-01:I-0027, MB-01:A-057, MB-01:A-059, MB-01:A-132, MB-01:B-0115, MB-01:B-0173, MB-01:C-054
- **pcr.9** In four artificial-gut communities about 19% of taxa were biased more than 4-fold.
  conf: single (note: "Silverman 2021, single study") · class: not stated · holds: four artificial-gut communities · src: silvermanMeasuringMitigatingPCR2021 (FT) · trail: MB-01 §2.4 · from: MB-01:A-058, MB-01:B-0116, MB-01:B-0174
- **pcr.10** Only relative per-cycle efficiencies have been measured: taxon-specific log-ratio changes per cycle, which compound to an average 2.6-fold bias after 35 cycles in a gut mock.
  conf: single (note: "Relative per-cycle efficiency rests on Silverman 2021") · class: meas (note: "only relative efficiencies have been measured") · holds: gut mock · src: silvermanMeasuringMitigatingPCR2021 (FT; meas; single) · trail: MB-01 §3.1 · from: MB-01:A-137, MB-01:A-138, MB-01:A-171, MB-01:A-185, MB-01:B-0259, MB-01:B-0260 · rating: "Weak for per-cycle efficiencies"
- **pcr.11** Kelly 2019 drew per-cycle efficiencies from beta distributions fitted to eukaryotic eDNA mocks and modelled amplicons as starting copies x (1 + a_i)^cycles.
  conf: not stated · class: model (marker) · holds: eukaryotic eDNA mocks; INDIRECT · src: kellyUnderstandingPCRProcesses2019 (FT; model; INDIRECT) · trail: MB-01 §3.1 · from: MB-01:I-0078, MB-01:A-139
- **pcr.12** No absolute per-cycle efficiency for universal 16S primers on environmental templates was found; the lab angle searched Crossref, Europe PMC and web search, and the qPCR methods literature (per-reaction efficiency from amplification curves, inhibition in environmental extracts) was not searched.
  conf: not stated · class: search (note: "No absolute per-cycle efficiency for universal 16S primers on environmental templates was found") · holds: lab angle's terms only · src: none (the review's search) · trail: MB-01 §3.1, §critic · from: MB-01:A-140, MB-01:A-304, MB-01:C-113, MB-01:B-0261, MB-01:B-0445
- **pcr.13** In Sze and Schloss's tests of five polymerases at 20 to 35 cycles, error rate, chimera fraction and deviation from the expected profile all rose with cycle number in the mock.
  conf: single (marker) · class: meas (marker) · holds: mock community · src: szeImpactDNAPolymerase2019 (FT, re-opened; meas; single) · trail: MB-01 §2.4 · from: MB-01:I-0028, MB-01:B-0177
- **pcr.14** Template-to-product ratios were little affected by cycle number.
  conf: single (marker) · class: meas (marker) · holds: abstract only · src: siposEffectPrimerMismatch2007 (AB; meas; single) · trail: MB-01 §2.4 · from: MB-01:I-0029, MB-01:A-062, MB-01:B-0179, MB-01:B-0414
- **pcr.15** Clone libraries amplified for different numbers of cycles showed no detectable skew.
  conf: single (marker) · class: meas (marker) · holds: Sanger clone libraries; abstract only · src: acinasPCRinducedSequenceArtifacts2005 (AB; meas; single; Sanger) · trail: MB-01 §2.4 · from: MB-01:I-0030, MB-01:A-062, MB-01:B-0414
- **pcr.16** 30 versus 35 cycles changed proportions only slightly.
  conf: not stated · class: not stated · holds: Brooks 2015 · src: brooksTruthMetagenomicsQuantifying2015 (FT) · trail: MB-01 §2.4 · from: MB-01:B-0180, MB-01:A-062
- **pcr.17** The effect of cycle number is contested: small effects (Sipos 2007, Acinas 2005, Brooks 2015) against growing bias (Suzuki 1996, Silverman 2021, the Sze and Schloss 2019 mock); cycle number had little influence in some studies.
  conf: cont (note: "Where the evidence conflicts") · class: not stated · holds: see pcr.4, pcr.8, pcr.13 to pcr.16 · src: siposEffectPrimerMismatch2007 (AB; meas; single), acinasPCRinducedSequenceArtifacts2005 (AB; meas; single), brooksTruthMetagenomicsQuantifying2015 (FT), suzukiBiasCausedTemplate1996 (AB; meas; repl), silvermanMeasuringMitigatingPCR2021 (FT; meas; single), szeImpactDNAPolymerase2019 (FT, re-opened; meas; single) · trail: MB-01 §6. Where, §answers · from: MB-01:A-116, MB-01:B-0119, MB-01:B-0399, MB-01:C-013
- **pcr.18** Low template (0.1 ng versus 5 to 10 ng) increased profile variability in soil and faecal samples.
  conf: single (marker) · class: meas (marker) · holds: soil and faecal samples; abstract only · src: kennedyEvaluatingBiasIlluminabased2014 (AB; meas; single) · trail: MB-01 §2.4 · from: MB-01:I-0031, MB-01:B-0181, MB-01:B-0182
- **pcr.19** Pooling of PCR replicates did not change profile variability.
  conf: single (marker) · class: meas (marker) · holds: soil and faecal samples; abstract only · src: kennedyEvaluatingBiasIlluminabased2014 (AB; meas; single) · trail: MB-01 §2.4 · from: MB-01:I-0031, MB-01:A-212, MB-01:B-0412, MB-01:B-0182
- **pcr.20** Single versus triplicate pooled PCRs made no significant difference.
  conf: repl (marker) · class: meas (marker) · holds: abstract only; the critic notes an open PMC copy exists · src: marotzTriplicatePCRReactions2019 (AB; meas; repl) · trail: MB-01 §2.4 · from: MB-01:I-0032, MB-01:A-212, MB-01:B-0412, MB-01:C-080
- **pcr.21** In fungal ITS, pooling 1 to 16 PCR replicates had no detectable effect on alpha or beta diversity.
  conf: not stated · class: meas (marker) · holds: fungal ITS, INDIRECT · src: smithSequenceDepthNot2014 (FT; meas; INDIRECT) · trail: MB-01 §2.4 · from: MB-01:I-0033, MB-01:A-212, MB-01:B-0412

### copy-number-correction: copy number versus read-based abundance; prediction and correction
needs: copy-number, pcr

- **copy-number-correction.1** Copy number is a property of each taxon rather than a workflow step, but it acts through PCR.
  conf: not stated · class: not stated · holds: the review's framing · src: none (the reviewer's synthesis) · trail: MB-01 §2.5 · from: MB-01:B-0184
- **copy-number-correction.2** With equimolar DNA from species pairs, PCR product ratios matched rrn genes per unit DNA for two pairs but deviated for a Bacillus pair.
  conf: not stated · class: meas (note: "AB, measured") · holds: experimental species pairs; abstract only · src: farrellyEffectGenomeSize1995 (AB) · trail: MB-02 §D1.4 · from: MB-02:A-040, MB-02:B-0201
- **copy-number-correction.3** Applying copy-number (and genome-size) correction to a forest soil moved Acidobacteria from 50.1% of 16S sequences to an estimated 66.0% of genomes, Actinobacteria from 11.8% to 7.6% and Firmicutes from 3.2% to 1.1%.
  conf: mixed (inputs: MB-01 repl, MB-02 single) · class: deriv (marker) · holds: one forest soil, the only soil example of correction size; it depends on the imprecise Acidobacteria copy numbers (copy-number.5); checked against full text by the MB-02 critic · src: vetrovskyVariability16SRRNA2013 (FT; deriv; repl) · trail: MB-01 §2.5, MB-02 §D1.4, §critic · from: MB-01:I-0035, MB-02:A-045, MB-02:A-059, MB-02:B-0223, MB-02:B-0224, MB-02:C-005, MB-02:C-057
- **copy-number-correction.4** In 100 simulated communities, phylogenetically corrected abundances correlated better with true organism abundance (r = 0.81) than raw gene abundances did (r = 0.70).
  conf: cont (marker) · class: model (marker) · holds: simulated communities, not real data · src: kembelIncorporating16SGene2012 (FT; model; cont) · trail: MB-01 §2.5, MB-02 §D1.4 · from: MB-01:I-0036, MB-01:A-070, MB-02:A-043, MB-02:B-0205, MB-02:C-021, MB-02:C-057
- **copy-number-correction.5** Phylogenetic prediction of copy number had a leave-one-out error of about one copy.
  conf: not stated · class: not stated · holds: phylogenetic prediction · src: kembelIncorporating16SGene2012 (FT) · trail: MB-02 §D1.4 · from: MB-02:A-042, MB-02:B-0204
- **copy-number-correction.6** Copy-number autocorrelation falls below 0.5 at about 15% 16S divergence and reaches zero at about 30%, so prediction is accurate only within about 15% divergence of a sequenced genome.
  conf: single (note: "rest on Louca et al. 2018 [30] alone") · class: deriv (note: "Bounding (derived)") · holds: about 6,800 genomes; the quantitative thresholds rest on Louca 2018; checked against full text by the MB-02 critic · src: loucaCorrecting16SRRNA2018 (FT) · trail: MB-01 §2.5, MB-02 §D1.4 · from: MB-01:B-0123, MB-01:B-0186, MB-01:A-153, MB-02:A-041, MB-02:A-057, MB-02:A-140, MB-02:B-0206, MB-02:B-0207, MB-02:C-057
- **copy-number-correction.7** The decline of copy-number prediction accuracy with distance to sequenced genomes is consistent across four analyses.
  conf: repl (note: "consistent across four independent analyses") · class: not stated · holds: Kembel 2012, Louca 2018, Edgar 2017 (preprint) and Gao and Wu 2023 · src: kembelIncorporating16SGene2012 (FT), loucaCorrecting16SRRNA2018 (FT), edgarUNBIASAttemptCorrect2017 (AB, preprint), gaoAccounting16SRRNA2023 (FT) · trail: MB-02 §answers, §critic · from: MB-02:A-048, MB-02:A-057, MB-02:C-021
- **copy-number-correction.8** About 49% of SILVA OTUs lie more than 15% from a sequenced genome.
  conf: not stated · class: not stated · holds: SILVA tree; checked against full text by the MB-02 critic · src: loucaCorrecting16SRRNA2018 (FT) · trail: MB-01 §3.2, MB-02 §D1.4 · from: MB-01:B-0273, MB-02:A-041, MB-02:A-140, MB-02:B-0208, MB-02:C-057
- **copy-number-correction.9** PICRUSt, CopyRighter and PAPRICA sometimes explained under 10% of variance against complete genomes and disagreed with each other (R2 < 0.5) for most of 635 communities, which included soils.
  conf: repl (marker) · class: deriv (marker) · holds: 635 environmental communities including soils · src: loucaCorrecting16SRRNA2018 (FT; deriv; repl) · trail: MB-01 §2.5, MB-02 §D1.4 · from: MB-01:I-0037, MB-01:A-069, MB-01:B-0424, MB-02:A-041, MB-02:B-0209, MB-02:B-0210
- **copy-number-correction.10** Louca et al. recommend against default correction unless OTUs are close to sequenced genomes.
  conf: not stated · class: not stated · holds: the authors' recommendation · src: loucaCorrecting16SRRNA2018 (FT) · trail: MB-02 §D1.4 · from: MB-02:B-0211
- **copy-number-correction.11** Phylogenetic copy-number predictions had a precision of about 0.96, with uncertainty rising with distance to sequenced genomes.
  conf: not stated · class: not stated · holds: within the distance limit; checked against full text by the critic · src: gaoAccounting16SRRNA2023 (FT) · trail: MB-02 §D1.4 · from: MB-02:A-042, MB-02:B-0212, MB-02:C-057
- **copy-number-correction.12** On 10 V4 mocks (one of eleven excluded; nine genomic DNA mixes and two cloned-gene mixes), uncorrected data fit known composition 7.1% (SE 3.6%) better than copy-number-corrected data.
  conf: repl (marker) · class: meas (marker) · holds: DNA-based or cloned-gene mocks only, not cell-based · src: starke16SRRNAGene2020 (FT; meas; repl) · trail: MB-01 §2.5, MB-02 §D1.4, §critic · from: MB-01:I-0038, MB-01:A-068, MB-01:B-0423, MB-02:A-044, MB-02:B-0218, MB-02:C-022, MB-02:C-065
- **copy-number-correction.13** DNA-based mocks already fix genome copies and size, so they test correction against a DNA truth, not a cell truth.
  conf: not stated · class: reading (note: "Reviewer's note") · holds: the reviewer's note on Starke 2021 · src: starke16SRRNAGene2020 (FT) · trail: MB-02 §D1.4 · from: MB-02:A-051, MB-02:B-0219
- **copy-number-correction.14** Across 7 taxa, copy number explained about 60% of estimated PCR bias (R2 about 0.60, p about 0.021) but only about 10% of total bias (R2 about 0.10).
  conf: single (note: "SINGLE SOURCE, and only 7 points") · class: deriv (note: "Partial (derived)") · holds: 7-taxon vaginal mock; verified in the re-opened full text · src: mclarenConsistentCorrectableBias2019 (FT, re-opened) · trail: MB-01 §2.5 · from: MB-01:A-067, MB-01:B-0122, MB-01:B-0187, MB-01:B-0188
- **copy-number-correction.15** Correction with CopyRighter improved agreement with mock communities and metagenomes, changed qPCR totals and diversity estimates, and reclassified twin gut samples from two enterotypes to three.
  conf: not stated · class: not stated · holds: tool-development paper; abstract only · src: anglyCopyRighterRapidTool2014 (AB) · trail: MB-02 §D1.4 · from: MB-02:A-043, MB-02:A-045, MB-02:B-0217
- **copy-number-correction.16** Correction raised the chance of identifying the true most abundant OTU from 13% to 65% in simulations.
  conf: not stated · class: model (note: "in simulations") · holds: simulated communities; checked against full text by the critic · src: gaoAccounting16SRRNA2023 (FT) · trail: MB-02 §answers · from: MB-02:A-043, MB-02:C-057
- **copy-number-correction.17** Correction changed the most abundant OTU in about 20% of Human Microbiome Project communities and 31% of Earth Microbiome Project communities, judged against predicted, not measured, truth.
  conf: single (note: "rest on Gao and Wu 2023 [33]") · class: not stated · holds: HMP and EMP communities; predicted truth · src: gaoAccounting16SRRNA2023 (FT) · trail: MB-02 §D1.4, §critic · from: MB-02:A-045, MB-02:A-058, MB-02:A-142, MB-02:B-0220, MB-02:C-023, MB-02:C-057
- **copy-number-correction.18** In simulations, correction reduced sample shifts in ordinations but left PERMANOVA variance explained essentially unchanged (5.27 to 19.65% true versus 5.27 to 19.82% uncorrected).
  conf: not stated · class: model (note: "In simulations") · holds: simulated communities · src: gaoAccounting16SRRNA2023 (FT) · trail: MB-02 §D1.4, §critic · from: MB-02:A-045, MB-02:A-142, MB-02:B-0221, MB-02:C-024
- **copy-number-correction.19** Correction moved ear samples to cluster with nostrils rather than feet, but left ocean clustering largely unchanged.
  conf: not stated · class: not stated · holds: human body-site and ocean data · src: kembelIncorporating16SGene2012 (FT) · trail: MB-02 §D1.4 · from: MB-02:A-045, MB-02:B-0222
- **copy-number-correction.20** Copy numbers can be estimated from draft assemblies by read depth, with a median deviation of 14% against qPCR.
  conf: not stated · class: not stated · holds: draft genome assemblies; abstract only · src: perisin16StimatorStatisticalEstimation2016 (AB) · trail: MB-02 §D1.4 · from: MB-02:B-0215
- **copy-number-correction.21** Correction for copy number and primer mismatch reached r of about 0.6 only in ideal cases (exact references), falling to about 0.4 at 97% and about 0.2 at 95% identity.
  conf: single (marker) · class: meas (marker) · holds: mocks; one preprint by the tool's author, abstract only · src: edgarUNBIASAttemptCorrect2017 (AB; PREPRINT; meas; single) · trail: MB-01 §2.14, MB-02 §D1.4 · from: MB-01:I-0076, MB-01:B-0425, MB-02:A-044, MB-02:A-141, MB-02:B-0214
- **copy-number-correction.22** Whether to correct for copy number is contested: studies recommending routine correction (Kembel 2012, Angly 2014, Gao and Wu 2023) conflict with studies recommending against default correction or finding it unhelpful in mocks (Louca 2018, Edgar 2017, Starke 2021, and McLaren 2019 in MB-01); part of the conflict reflects what "truth" is (cell-based versus DNA-based mocks, simulated versus real communities, closeness to references), and correction changing dominant taxa but not beta-diversity tests lets both camps' observations hold together.
  conf: cont (note: "Direct conflict between studies recommending routine correction") · class: not stated · holds: evidence mostly from simulations, mocks of few species or non-soil communities · src: kembelIncorporating16SGene2012 (FT; model; cont), anglyCopyRighterRapidTool2014 (AB), gaoAccounting16SRRNA2023 (FT), loucaCorrecting16SRRNA2018 (FT; deriv; repl), edgarUNBIASAttemptCorrect2017 (AB; PREPRINT; meas; single), starke16SRRNAGene2020 (FT; meas; repl), mclarenConsistentCorrectableBias2019 (FT, re-opened) · trail: MB-01 §2.5, §6. Where, MB-02 §answers, §critic · from: MB-01:A-119, MB-01:B-0185, MB-02:A-047, MB-02:A-049, MB-02:A-050, MB-02:A-051, MB-02:A-052, MB-02:A-141, MB-02:A-143, MB-02:C-020, MB-02:C-021 · rating: "moderate and conflicting"
- **copy-number-correction.23** A review asserts that rDNA copy number can change within species in response to the environment; the prokaryote evidence for this was not quantified in the sources read.
  conf: not stated · class: assert (note: "AB, asserted") · holds: one review, abstract only · src: lavrinienkoDoesIntraspecificVariation2021 (AB) · trail: MB-02 §D1.4 · from: MB-02:A-055, MB-02:B-0225, MB-02:B-0226
- **copy-number-correction.24** No soil mock-community or soil cell-count benchmark of copy-number correction was found, and no study combining copy-number correction with per-cell genome copy measurements in a real community; the polyploidy literature asserts that ploidy also biases community analyses (Soppa 2017, not obtained).
  conf: not stated · class: search (note: "No soil mock community or soil cell-count benchmark of copy-number correction was found") · holds: the soil literature on community-weighted rrn copy number was not searched · src: soppaPolyploidyCommunityStructure2017 (not obtained) · trail: MB-02 §answers, §critic · from: MB-02:A-053, MB-02:A-054, MB-02:A-143, MB-02:C-026, MB-02:C-027

### genome-copies-per-cell: genome and 16S copies per cell
needs: copy-number

- **genome-copies-per-cell.1** In cultures, genome copies per cell range from about one (Caulobacter, Wolinella, crenarchaea) through merodiploid and oligoploid states to tens or hundreds (P. putida, haloarchaea, methanogens, Synechocystis), and depend on taxon, growth rate and phase; copy number does not change in one direction with growth phase.
  conf: not stated · class: meas (note: "All figures below are measured") · holds: cultures; apart from Pecoraro 2011 the evidence rests largely on abstracts and on one laboratory's qPCR method; the general conclusion that ploidy varies by taxon and growth phase would survive any single removal · src: pecoraroQuantificationPloidyProteobacteria2011 (FT), hildenbrandGenomeCopyNumbers2011 (AB), breuertRegulatedPolyploidyHalophilic2006 (AB), zerullaPloidyLevelSynechocystis2016 (AB), griesePloidyCyanobacteria2011 (AB) · trail: MB-02 §D1.3, §critic · from: MB-02:A-020, MB-02:A-039, MB-02:A-134, MB-02:C-008, MB-02:C-009, MB-02:C-014, MB-02:B-0161 · rating: "Evidence is moderate, not strong"
- **genome-copies-per-cell.2** Most direct measurements of genome copies per cell come from one laboratory's real-time PCR protocol (Soppa group), cross-checked in several studies against Southern blots, flow cytometry or published E. coli values.
  conf: single (note: "Most direct measurements come from one laboratory's real-time PCR protocol") · class: meas (note: "All figures below are measured") · holds: cultures · src: pecoraroQuantificationPloidyProteobacteria2011 (FT), bottingerRegulatedPloidyBacillus2018 (AB), breuertRegulatedPolyploidyHalophilic2006 (AB), hildenbrandGenomeCopyNumbers2011 (AB), griesePloidyCyanobacteria2011 (AB), zerullaPloidyLevelSynechocystis2016 (AB), bruckOneAdvantageBeing2023 (AB), zerullaPolyploidyHaloarchaeaAdvantages2014 (AB) · trail: MB-02 §D1.3, §critic · from: MB-02:A-029, MB-02:A-136, MB-02:B-0159..0161, MB-02:C-014
- **genome-copies-per-cell.3** E. coli has 6.8 origins and 1.7 termini per cell at a 25 min doubling time but 2.5 origins and 1.2 termini at 103 min.
  conf: single (note: "would remove the only direct origin and terminus counts for E. coli") · class: meas (note: "All figures below are measured") · holds: E. coli cultures; checked against full text by the critic · src: pecoraroQuantificationPloidyProteobacteria2011 (FT) · trail: MB-02 §D1.3 · from: MB-02:A-022, MB-02:A-036, MB-02:B-0163, MB-02:C-057, MB-02:B-0161
- **genome-copies-per-cell.4** E. coli stationary-phase batch cultures always contained some multi-chromosome cells, even after days.
  conf: not stated · class: meas (note: "All figures below are measured") · holds: batch cultures; abstract only · src: akerlundAnalysisCellSize1995 (AB) · trail: MB-02 §D1.3 · from: MB-02:A-024, MB-02:B-0164, MB-02:B-0161
- **genome-copies-per-cell.5** Caulobacter crescentus (93 min doubling) had about 2.1 genome-equivalents at a mid-chromosome locus, read as monoploid (one chromosome plus replication), and Wolinella succinogenes (96 min) about 0.9.
  conf: not stated · class: meas (note: "All figures below are measured") · holds: cultures; checked against full text by the critic · src: pecoraroQuantificationPloidyProteobacteria2011 (FT) · trail: MB-02 §D1.3 · from: MB-02:A-021, MB-02:B-0165, MB-02:B-0166, MB-02:C-057, MB-02:B-0161
- **genome-copies-per-cell.6** Pseudomonas putida (46 min doubling) had about 20 origins and 14 termini per cell.
  conf: single (note: "would remove the only direct origin and terminus counts for E. coli at two growth rates and the P. putida value") · class: meas (note: "All figures below are measured") · holds: cultures; checked against full text by the critic · src: pecoraroQuantificationPloidyProteobacteria2011 (FT) · trail: MB-02 §D1.3 · from: MB-02:A-023, MB-02:A-036, MB-02:B-0167, MB-02:C-057, MB-02:B-0161
- **genome-copies-per-cell.7** Only three to four of 11 proteobacterial species with measured ploidy were monoploid, with no correlation to genome size, temperature or lifestyle.
  conf: not stated · class: not stated · holds: proteobacterial cultures · src: pecoraroQuantificationPloidyProteobacteria2011 (FT) · trail: MB-02 §D1.3 · from: MB-02:B-0176, MB-02:B-0177
- **genome-copies-per-cell.8** B. subtilis and three soil Bacillus and Paenibacillus isolates are mero-oligoploid in exponential phase (B. subtilis 5.9 origins, 1.2 termini) and down-regulate origins in stationary phase.
  conf: not stated · class: meas (note: "All figures below are measured") · holds: cultures; abstract only · src: bottingerRegulatedPloidyBacillus2018 (AB) · trail: MB-02 §D1.3 · from: MB-02:A-022, MB-02:B-0168, MB-02:B-0161
- **genome-copies-per-cell.9** Synechococcus strains PCC 7942 and WH7803 carry 3 to 4 genome copies, and Synechocystis PCC 6803 carried 218 (exponential) to 58 (stationary) in one substrain.
  conf: not stated · class: meas (note: "All figures below are measured") · holds: cyanobacterial cultures; abstract only · src: griesePloidyCyanobacteria2011 (AB) · trail: MB-02 §D1.3 · from: MB-02:A-023, MB-02:B-0169, MB-02:B-0170, MB-02:B-0161
- **genome-copies-per-cell.10** Across six Synechocystis substrains, copies fell from about 20 to 4 between exponential and stationary phase, and cells became monoploid only after prolonged phosphate starvation.
  conf: not stated · class: meas (note: "All figures below are measured") · holds: cultures; abstract only · src: zerullaPloidyLevelSynechocystis2016 (AB) · trail: MB-02 §D1.3 · from: MB-02:A-023, MB-02:A-033, MB-02:B-0170, MB-02:B-0161
- **genome-copies-per-cell.11** Halobacterium salinarum carried 25 (exponential) to 15 (stationary) genome copies and Haloferax volcanii 18 to 10.
  conf: not stated · class: meas (note: "All figures below are measured") · holds: haloarchaeal cultures; abstract only · src: breuertRegulatedPolyploidyHalophilic2006 (AB) · trail: MB-02 §D1.3 · from: MB-02:A-023, MB-02:B-0171, MB-02:B-0161
- **genome-copies-per-cell.12** In H. salinarum, single-cell measurements showed wide cell-to-cell variation in copy number, larger in exponential than in stationary phase; the full text, which the review did not read, reports single-cell CLSM and FACS distributions of genome copy number.
  conf: not stated · class: meas (note: "Single-cell measurements in H. salinarum showed") · holds: cultures; read at abstract level although an open full text exists · src: breuertRegulatedPolyploidyHalophilic2006 (AB) · trail: MB-02 §D1.3, §critic · from: MB-02:B-0179, MB-02:C-069, MB-02:C-070
- **genome-copies-per-cell.13** Methanococcus maripaludis carried up to 55 genome copies (exponential) and about 30 (stationary), and Methanosarcina acetivorans 17 (fast growth) and 3 (slow growth).
  conf: not stated · class: meas (note: "All figures below are measured") · holds: methanogen cultures; abstract only · src: hildenbrandGenomeCopyNumbers2011 (AB) · trail: MB-02 §D1.3 · from: MB-02:A-023, MB-02:B-0172, MB-02:B-0173, MB-02:B-0161
- **genome-copies-per-cell.14** None of seven euryarchaeal species was monoploid, against all six crenarchaeal species (four genera).
  conf: not stated · class: meas (note: "All figures below are measured") · holds: compiled archaeal cultures; abstract only · src: hildenbrandGenomeCopyNumbers2011 (AB) · trail: MB-02 §D1.3 · from: MB-02:A-021, MB-02:B-0174, MB-02:B-0178, MB-02:B-0161
- **genome-copies-per-cell.15** Three polyploid species (Zymomonas mobilis, Azotobacter vinelandii, H. salinarum) stayed at about five copies in phosphate-starved stationary phase rather than becoming monoploid, whereas Synechocystis went to one copy.
  conf: not stated · class: meas (note: "All figures below are measured") · holds: phosphate-starved cultures; abstract only · src: bruckOneAdvantageBeing2023 (AB), zerullaPloidyLevelSynechocystis2016 (AB) · trail: MB-02 §D1.3 · from: MB-02:A-023, MB-02:A-033, MB-02:B-0175, MB-02:B-0161
- **genome-copies-per-cell.16** Azotobacter vinelandii and Methanosarcina acetivorans carry more chromosomes in stationary than in exponential phase: about 4 versus 80 for A. vinelandii, and 2.5 versus 5 for M. acetivorans.
  conf: not stated · class: not stated · holds: reported in the open full text of Brück 2023, which the review read only as an abstract; known to this note through the critic (SECONDARY) · src: bruckOneAdvantageBeing2023 (AB) · trail: MB-02 §critic · from: MB-02:C-011, MB-02:C-064, MB-02:C-072, MB-02:C-073, MB-02:C-074
- **genome-copies-per-cell.17** Pecoraro et al. 2011's Table 5 lists A. vinelandii as 1 (up to 8) copies in slow growth and 40 in fast growth (attributed to another laboratory), Desulfovibrio 9 to 17, Neisseria 3 to 4 and Buchnera 120, and the paper mentions polyploid Deinococcus, Borrelia and rhizobial bacteroids; the Azotobacter, Desulfovibrio, Neisseria and Deinococcus measurements are non-Soppa.
  conf: not stated · class: not stated · holds: a table in a paper read in full by the review but not reported; known to this note through the critic · src: pecoraroQuantificationPloidyProteobacteria2011 (FT) · trail: MB-02 §critic · from: MB-02:C-012, MB-02:C-013, MB-02:C-075, MB-02:C-131, MB-02:C-063
- **genome-copies-per-cell.18** rRNA operons cluster near the replication origin in fast-growing bacteria, and gene-dosage effects shape this placement.
  conf: not stated · class: not stated · holds: genome analysis; abstract only · src: couturierReplicationassociatedGeneDosage2006 (AB) · trail: MB-02 §D1.3 · from: MB-02:A-025, MB-02:B-0181
- **genome-copies-per-cell.19** That 16S copies per cell scale with origin number more than with genome number in fast growers is the reviewer's inference from one abstract; no source in the review measures 16S copies per cell against origin number.
  conf: not stated · class: reading (critic: MB-02:C-015) · holds: an untested inference · src: couturierReplicationassociatedGeneDosage2006 (AB) · trail: MB-02 §critic, §D1.3 · from: MB-02:C-015, MB-02:C-088, MB-02:C-140, MB-02:B-0182
- **genome-copies-per-cell.20** For E. coli, rRNA genes per genome equivalent range from about 7.9 to 9.5 across growth rates.
  conf: not stated · class: not stated · holds: SECONDARY, Bremer and Dennis (1996) Table 3 as reported by BioNumbers · src: bionumbersAverageNumberRRNA (SEC), bremerModulationChemicalComposition1996 (not obtained) · trail: MB-02 §D1.3 · from: MB-02:A-025, MB-02:B-0183, MB-02:B-0184
- **genome-copies-per-cell.21** Indigenous soil bacteria extracted from a clay loam contained 1.5 to 15 fg DNA per cell by flow cytometry, most below 4 fg, with an average around 2 fg; larger cells, and cells that grew in soil extract, had more DNA.
  conf: single (note: "would leave no soil measurement of DNA per cell at all") · class: meas (note: "by flow cytometry") · holds: one clay loam; DNA mass cannot separate genome size from copy number; abstract only; confirms earlier work by the same group (Bakken and Olsen 1989, secondary) · src: christensenFlowCytometricMeasurements1995 (AB), bakkenDNAcontentSoilBacteria1989 (SEC) · trail: MB-02 §D1.3 · from: MB-02:A-026, MB-02:A-037, MB-02:B-0187..0190, MB-02:C-058
- **genome-copies-per-cell.22** About 2 fg of DNA is less than one copy of a 4 Mb genome, which suggests many soil cells hold one copy of a small genome.
  conf: not stated · class: reading (note: "In the reviewer's reading") · holds: an inference from DNA mass, which cannot separate genome size from copy number · src: christensenFlowCytometricMeasurements1995 (AB) · trail: MB-02 §D1.3 · from: MB-02:B-0191
- **genome-copies-per-cell.23** A typical seawater sample had a mean of 2.5 fg DNA per cell, in two populations described as 1n and 2n clusters, with 10 to 30% of cells "dim" low-DNA cells; the authors treat increased copy number with growth rate in nature as "likely", an inference rather than a measurement.
  conf: not stated · class: not stated · holds: seawater; full text read to 100,000 characters · src: buttonDeterminationDNAContent2001 (FT, first 100,000 characters) · trail: MB-02 §D1.3 · from: MB-02:A-026, MB-02:B-0192, MB-02:B-0193, MB-02:A-035
- **genome-copies-per-cell.24** The two DNA-content populations in seawater could reflect replicating monoploid cells or larger genomes, and DNA mass per cell in soil cannot separate genome size from copy number.
  conf: not stated · class: reading (note: "Tension in interpretation") · holds: interpretation of Button and Robertson 2001 and Christensen 1995 · src: buttonDeterminationDNAContent2001 (FT, first 100,000 characters), christensenFlowCytometricMeasurements1995 (AB) · trail: MB-02 §answers · from: MB-02:A-032
- **genome-copies-per-cell.25** In the equatorial Pacific, Prochlorococcus DNA replication ran in phase with the light cycle, in the afternoon, with division at night.
  conf: not stated · class: not stated · holds: abstract only; the abstract gives no share of cells · src: vaulotGrowthProchlorococcusPhotosynthetic1995 (AB) · trail: MB-02 §D1.3, §critic · from: MB-02:A-026, MB-02:B-0194, MB-02:C-079, MB-02:C-080
- **genome-copies-per-cell.26** Flow cytometric cell-cycle analyses of Prochlorococcus and Synechococcus in situ are, by method, taxon-specific measurements of the share of cells with replicated DNA (G1 versus S/G2) in natural seawater.
  conf: not stated · class: not stated · holds: known to this note through the critic; the review read Vaulot 1995 only at abstract level · src: vaulotGrowthProchlorococcusPhotosynthetic1995 (AB) · trail: MB-02 §critic · from: MB-02:C-017, MB-02:C-106
- **genome-copies-per-cell.27** In groundwater metagenomes, population-average replication indices (iRep) were mostly low: Candidate Phyla Radiation bacteria had a median iRep of 1.34, and only 16.1% of values exceeded 1.5; the authors read an iRep of 1.25 as about a quarter of cells replicating.
  conf: single (note: "would leave no environmental replication-index figure") · class: not stated · holds: groundwater; full text read to 100,000 characters · src: brownMeasurementBacterialReplication2016 (FT, first 100,000 characters) · trail: MB-02 §D1.3 · from: MB-02:A-026, MB-02:A-038, MB-02:B-0195..0197, MB-02:A-035
- **genome-copies-per-cell.28** Gut metagenome peak-to-trough ratios track growth rate in culture and in vivo.
  conf: not stated · class: not stated · holds: gut; abstract only · src: koremGrowthDynamicsGut2015 (AB) · trail: MB-02 §D1.3 · from: MB-02:B-0198
- **genome-copies-per-cell.29** In natural communities the evidence on genome copies per cell is indirect and sparse (soil DNA mass per cell, seawater DNA-content populations, groundwater iRep), mostly non-soil and single-study per setting; nothing comparable was found for soil.
  conf: single (note: "single-study per setting") · class: not stated · holds: soil, seawater, groundwater · src: christensenFlowCytometricMeasurements1995 (AB), buttonDeterminationDNAContent2001 (FT, first 100,000 characters), brownMeasurementBacterialReplication2016 (FT, first 100,000 characters) · trail: MB-02 §answers, §critic · from: MB-02:A-030, MB-02:A-137, MB-02:C-016, MB-02:C-019 · rating: "Weak for environmental samples"
- **genome-copies-per-cell.30** In the sources reached, no source reports, for any natural community, the share of cells carrying exactly one genome copy versus more than one, by taxon; no source measured 16S copies per cell directly in environmental cells, and no replication indices for soil metagenomes were found.
  conf: not stated · class: search (note: "No source found reports, for any natural community") · holds: Europe PMC and web searches on replication indices with soil and on genome copies per cell; the critic notes the in situ Prochlorococcus cell-cycle literature was read only at abstract level, so the wider statement that no such share exists is not established · src: none (the review's search) · trail: MB-02 §D1.3, §Search record · from: MB-02:A-027, MB-02:A-138, MB-02:B-0185, MB-02:B-0199, MB-02:B-0200, MB-02:C-018, MB-02:B-0368

- **genome-copies-per-cell.31** In most of the species measured by the Soppa group, genome copies fall in stationary phase or starvation.
  conf: not stated · class: not stated · holds: cultures; not all species, and not always to one copy (see genome-copies-per-cell.15, genome-copies-per-cell.16) · src: breuertRegulatedPolyploidyHalophilic2006 (AB), hildenbrandGenomeCopyNumbers2011 (AB), zerullaPloidyLevelSynechocystis2016 (AB), bottingerRegulatedPloidyBacillus2018 (AB) · trail: MB-02 §critic, §D1.3 · from: MB-02:C-010

### community-copy-number: community-average copy number by environment
needs: copy-number-correction

- **community-copy-number.1** Every environment-level copy number found is predicted from reference genomes, not measured; a measured community-average copy number for soil, water or host samples was not found, and community copy number from shotgun metagenomes (16S reads normalised to single-copy marker genes) was not searched.
  conf: not stated · class: search (note: "Every value found is predicted from reference genomes, not measured") · holds: lab and bioinformatics angles · src: thompsonCommunalCatalogueReveals2017 (FT; deriv; single) · trail: MB-01 §3.2, §critic · from: MB-01:A-152, MB-01:A-178, MB-01:B-0268, MB-01:B-0446, MB-01:C-112
- **community-copy-number.2** Environment-level copy numbers (about 2.2 for free-living and plant-associated samples, about 3.4 for animal-associated, soil lowest) are predictions from one source.
  conf: single (critic: MB-01:C-024) · class: deriv (note: "predicted, not measured") · holds: Earth Microbiome Project samples; predictions from reference genomes · src: thompsonCommunalCatalogueReveals2017 (FT; deriv; single) · trail: MB-01 §critic, §3.2 · from: MB-01:C-024, MB-01:A-169, MB-01:A-183, MB-01:A-303 · rating: "Weak for environment-level copy number"
- **community-copy-number.3** Soil had the lowest abundance-weighted copy-number distribution in the EMP.
  conf: single (marker) · class: deriv (marker) · holds: predicted, not measured · src: thompsonCommunalCatalogueReveals2017 (FT; deriv; single) · trail: MB-01 §3.2 · from: MB-01:I-0082, MB-01:A-147
- **community-copy-number.4** Predicted community copy number declines through succession in soil and sediment.
  conf: single (marker) · class: deriv (marker) · holds: predicted · src: nemergutDecreasesAverageBacterial2015 (FT; deriv; single) · trail: MB-01 §3.2 · from: MB-01:I-0083, MB-01:A-148
- **community-copy-number.5** No separate value for water was found; the EMP groups free-living samples (soil, water, sediment) and plant-associated samples together at about 2.2.
  conf: not stated · class: deriv (note: "All environment values are predictions from reference genomes") · holds: EMP · src: thompsonCommunalCatalogueReveals2017 (FT) · trail: MB-01 §3.2, §critic · from: MB-01:A-149, MB-01:A-150, MB-01:B-0270, MB-01:B-0271, MB-01:C-136, MB-01:A-152
- **community-copy-number.6** Animal-associated samples are predicted at about 3.4, with gut and saliva highest.
  conf: not stated · class: deriv (note: "predicted, not measured") · holds: EMP · src: thompsonCommunalCatalogueReveals2017 (FT) · trail: MB-01 §3.2 · from: MB-01:A-151, MB-01:B-0272
- **community-copy-number.7** The environment-level copy-number predictions conflict with Louca 2018's finding that such predictions are inaccurate beyond about 15% divergence from a sequenced genome.
  conf: cont (note: "conflict with Louca 2018's finding") · class: not stated · holds: see copy-number-correction.6 · src: thompsonCommunalCatalogueReveals2017 (FT; deriv; single), loucaCorrecting16SRRNA2018 (FT) · trail: MB-01 §3.2, §answers · from: MB-01:A-153, MB-01:A-177

### library-sequencing: library preparation, indexing and sequencing platform
needs: workflow, departure

- **library-sequencing.1** Documented library-preparation choices are one-step fusion, two-step tailed or ligation designs, with single, combinatorial or unique dual indexes.
  conf: not stated · class: not stated · holds: protocols and documentation · src: none (the reviewer's synthesis of protocols) · trail: MB-01 §2.6 · from: MB-01:A-009
- **library-sequencing.2** Documented platforms and read lengths are MiSeq 2x250 or 2x300, HiSeq, NovaSeq, Ion Torrent, 454, or PacBio CCS full length.
  conf: not stated · class: not stated · holds: protocols and benchmarks · src: none (the reviewer's synthesis of protocols) · trail: MB-01 §2.7 · from: MB-01:A-010
- **library-sequencing.3** Across 73 MiSeq datasets, library preparation method and primer choice were the most significant sources of bias, with distinct, motif-linked error patterns.
  conf: single (marker) · class: meas (marker) · holds: MiSeq datasets; rests on Schirmer 2015 alone · src: schirmerInsightBiasesSequencing2015 (FT; meas; single) · trail: MB-01 §2.6, §critic · from: MB-01:I-0041, MB-01:A-077, MB-01:B-0126, MB-01:C-088
- **library-sequencing.4** Library design also affected error and chimera rates across four platforms.
  conf: not stated · class: not stated · holds: benchmark across four platforms · src: damoreComprehensiveBenchmarkingStudy2016 (FT) · trail: MB-01 §2.6 · from: MB-01:B-0189
- **library-sequencing.5** Dual-index MiSeq error depended on read overlap: raw V4 error rose with cluster density from 0.25% to 1.08%, and partially overlapping regions stayed worse.
  conf: repl (marker) · class: meas (marker) · holds: MiSeq; the critic could not confirm open full text for this source · src: kozichDevelopmentDualindexSequencing2013 (FT; meas; repl) · trail: MB-01 §2.7 · from: MB-01:I-0042, MB-01:A-078, MB-01:B-0193, MB-01:B-0195, MB-01:C-073, MB-01:C-074
- **library-sequencing.6** A delta-Q of 6 cut the raw V4 error to 0.05 to 0.06%, and preclustering to 0.01%.
  conf: not stated · class: not stated · holds: MiSeq, V4 · src: kozichDevelopmentDualindexSequencing2013 (FT) · trail: MB-01 §2.7 · from: MB-01:B-0194, MB-01:A-078
- **library-sequencing.7** After preclustering, V3-V4 error was 0.10 to 0.21% and V4-V5 0.36 to 0.64% per the bioinformatics angle; the lab angle reports 0.24 to 0.37% and 0.58 to 0.87%, read through a fetch-tool summary, probably at an earlier stage of curation.
  conf: not stated · class: not stated · holds: two search angles' readings of the same source disagree · src: kozichDevelopmentDualindexSequencing2013 (FT) · trail: MB-01 §2.7 · from: MB-01:B-0196, MB-01:B-0197
- **library-sequencing.8** PacBio CCS with DADA2 recovered all expected full-length variants in two mocks with no residual errors.
  conf: not stated · class: not stated · holds: the developer's own claim; there are no independent long-read mock benchmarks · src: callahanHighthroughputAmpliconSequencing2019 (FT; developer claim) · trail: MB-01 §2.7, §critic · from: MB-01:B-0198, MB-01:C-109
- **library-sequencing.9** The DADA2 maintainer states that NovaSeq's binned quality scores break loess smoothing in error learning; at the time of the issue the method had not been tested on NovaSeq data.
  conf: not stated · class: assert (note: "DOCUMENTATION; assert") · holds: an issue-tracker statement · src: benjjnebConsequencesUsingDada2 (DOCUMENTATION; assert) · trail: MB-01 §2.7 · from: MB-01:B-0199, MB-01:B-0200

### index-misassignment: demultiplexing and index misassignment
needs: library-sequencing

- **index-misassignment.1** Demultiplexing can be done with or without filtering on index-read quality.
  conf: not stated · class: not stated · holds: non-16S amplicons · src: wrightQualityFilteringIllumina2016 (FT; INDIRECT) · trail: MB-01 §2.8 · from: MB-01:A-011, MB-01:I-0045
- **index-misassignment.2** On Illumina GAIIx with non-16S libraries, 0.51 to 0.76% of index pairs were wrong, and 0.06 to 0.43% after index-quality filtering.
  conf: repl (marker) · class: meas (marker) · holds: GAIIx, non-16S libraries, INDIRECT · src: kircherDoubleIndexingOvercomes2012 (FT; meas; repl; INDIRECT) · trail: MB-01 §2.8 · from: MB-01:I-0043
- **index-misassignment.3** On patterned flow cells (HiSeq X, 3000/4000, NovaSeq) with non-16S libraries, index misassignment was 0.2 to 6% in every run and about 10-fold lower on MiSeq; unique dual indexes cut it from 0.89% to 0.13%.
  conf: repl (marker) · class: meas (marker) · holds: non-16S genome and exome libraries, INDIRECT · src: costelloCharacterizationRemediationSample2018 (FT; meas; repl; INDIRECT) · trail: MB-01 §2.8 · from: MB-01:I-0044, MB-01:A-082, MB-01:C-133
- **index-misassignment.4** Illumina's documentation gives 0.1 to 2% index hopping on patterned flow cells.
  conf: not stated · class: assert (note: "DOCUMENTATION; maker's claim") · holds: maker's claim · src: illuminaIndexHoppingWeb (DOCUMENTATION; maker's claim) · trail: MB-01 §2.8 · from: MB-01:B-0202
- **index-misassignment.5** On HiSeq 2500 with non-16S amplicons, cross-talk was 0.24%, and 0.03% after index-quality filtering (88% of reads kept).
  conf: single (marker) · class: meas (marker) · holds: non-16S amplicons, INDIRECT · src: wrightQualityFilteringIllumina2016 (FT; meas; single; INDIRECT) · trail: MB-01 §2.8 · from: MB-01:I-0045, MB-01:A-083
- **index-misassignment.6** In 16S data from GAIIx and 11 MiSeq runs, about 2% of reads were misassigned.
  conf: single (marker) · class: meas (marker) · holds: 16S; one preprint abstract · src: edgarUNCROSSFilteringHighfrequency2016 (AB; PREPRINT; meas; single) · trail: MB-01 §2.8 · from: MB-01:I-0046, MB-01:A-084
- **index-misassignment.7** Barcode leakage was negligible on 16S plates.
  conf: single (marker) · class: meas (marker) · holds: 16S plates · src: minichQuantifyingUnderstandingWelltowell2019 (FT; meas; single) · trail: MB-01 §2.8 · from: MB-01:I-0047, MB-01:A-085
- **index-misassignment.8** In eukaryotic 18S data, up to 28.2% of unique sequences were undetectable mistags.
  conf: not stated · class: meas (marker) · holds: eukaryotic 18S, INDIRECT · src: eslingAccurateMultiplexingFiltering2015 (FT; meas; INDIRECT) · trail: MB-01 §2.8 · from: MB-01:I-0048
- **index-misassignment.9** With mammal and arthropod markers, 2.1 to 2.6% of sequences came from tag jumps.
  conf: not stated · class: meas (marker) · holds: other markers, INDIRECT; abstract only · src: schnellTagJumpsIlluminated2015 (AB; meas; INDIRECT) · trail: MB-01 §2.8 · from: MB-01:I-0049, MB-01:A-086
- **index-misassignment.10** Index-misassignment rates are fractions of reads assigned to the wrong sample; they mainly create false presences of taxa, concentrated where abundant taxa from other samples leak in.
  conf: not stated · class: not stated · holds: the review's reading of the sources in index-misassignment.2 to 9 · src: none (the reviewer's synthesis) · trail: MB-01 §2.8 · from: MB-01:B-0203, MB-01:B-0204, MB-01:B-0127
- **index-misassignment.11** Index-misassignment rates vary with platform, library type and run, and the 16S-specific evidence is thin: one preprint abstract and one plate study.
  conf: not stated · class: not stated · holds: see index-misassignment.2 to 9 · src: none (the reviewer's synthesis) · trail: MB-01 §2.8 · from: MB-01:A-087, MB-01:B-0205, MB-01:B-0206
- **index-misassignment.12** No 16S-specific measurement of index hopping on patterned flow cells (NovaSeq, NextSeq 2000) was found.
  conf: not stated · class: search (note: "No 16S-specific measurement of index hopping on patterned flow cells") · holds: bioinformatics angle · src: none (the review's search) · trail: MB-01 §Search record, §critic · from: MB-01:A-122, MB-01:B-0447, MB-01:C-110

### quality-filtering: quality filtering and read merging
needs: library-sequencing

- **quality-filtering.1** Documented quality-filtering and merging choices are quality, length, expected-error and abundance thresholds, plus the delta-Q rule when merging.
  conf: not stated · class: not stated · holds: benchmarks and pipelines · src: bokulichQualityfilteringVastlyImproves2013 (FT), kozichDevelopmentDualindexSequencing2013 (FT) · trail: MB-01 §2.9 · from: MB-01:A-012
- **quality-filtering.2** On mocks from GAIIx, HiSeq and MiSeq runs, minimum read length, quality threshold and a minimum OTU abundance filter strongly affected alpha diversity and composition; ambiguous bases and bad run length did not.
  conf: repl (marker) · class: meas (marker) · holds: mocks on three Illumina platforms · src: bokulichQualityfilteringVastlyImproves2013 (FT; meas; repl) · trail: MB-01 §2.9 · from: MB-01:I-0050, MB-01:B-0207
- **quality-filtering.3** Almost every setting needed an abundance filter of 0.0001 to 0.01% to reach expected taxon counts, and 0.005% is recommended.
  conf: not stated · class: not stated · holds: mocks · src: bokulichQualityfilteringVastlyImproves2013 (FT) · trail: MB-01 §2.9 · from: MB-01:B-0208, MB-01:B-0207
- **quality-filtering.4** Under quality filtering, weighted UniFrac conclusions were robust; unweighted metrics were sensitive.
  conf: not stated · class: not stated · holds: mocks · src: bokulichQualityfilteringVastlyImproves2013 (FT) · trail: MB-01 §2.9 · from: MB-01:B-0209, MB-01:B-0207
- **quality-filtering.5** Stringent UPARSE-style filtering could significantly underestimate abundance and diversity, and newer clusterers produced up to 60% fewer spurious OTUs than UCLUST.
  conf: cont (marker) · class: meas (marker) · holds: benchmark · src: kopylovaOpensourceSequenceClustering2016 (FT; meas; cont) · trail: MB-01 §2.9 · from: MB-01:I-0051, MB-01:B-0428
- **quality-filtering.6** Error correction plus overlapping cut substitution errors by 93% on average.
  conf: not stated · class: not stated · holds: as reported for Schirmer 2015 · src: schirmerInsightBiasesSequencing2015 (FT) · trail: MB-01 §2.9 · from: MB-01:B-0210
- **quality-filtering.7** The USEARCH author reports that most paired-read assemblers compute incorrect posterior quality scores.
  conf: not stated · class: assert (note: "The USEARCH author reports") · holds: developer claim, abstract only · src: edgarErrorFilteringPair2015 (AB; developer claim) · trail: MB-01 §2.9 · from: MB-01:B-0211

### denoising-clustering: denoising and clustering (OTUs, ASVs and spurious units)
needs: quality-filtering, copy-number

- **denoising-clustering.1** Documented error-handling choices are 97% or 99% OTUs (de novo, closed or open reference) or ASVs from DADA2, Deblur or UNOISE3; DADA2 can process samples independently, pooled or pseudo-pooled.
  conf: not stated · class: not stated · holds: pipelines and documentation · src: none (the reviewer's synthesis of pipeline documentation) · trail: MB-01 §2.10 · from: MB-01:A-013
- **denoising-clustering.2** In an independent benchmark, relative abundances of expected taxa within each mock were similar across DADA2, UNOISE3, Deblur and open-reference OTUs; on the Zymo mock, however, all pipelines "markedly differed" from expected composition.
  conf: repl (marker) · class: meas (marker) · holds: mocks; the review's heading generalises from this benchmark (with Marizzoni 2020) to "relative abundance is robust to the pipeline", which the critic flags · src: nearingDenoisingDenoisersIndependent2018 (FT; meas; repl) · trail: MB-01 §2.10, §critic · from: MB-01:I-0052, MB-01:A-092, MB-01:B-0129, MB-01:B-0216, MB-01:C-087
- **denoising-clustering.3** Counts of units differed widely between pipelines: open-reference clustering gave 453 OTUs on the HMP mock and 8,891 on the Extreme mock, and on one soil DADA2 gave 16,609 ASVs, UNOISE3 11,613, Deblur 8,270 and open-reference 21,297 OTUs; no pipeline recovered every expected sequence.
  conf: not stated · class: not stated · holds: mocks and one soil · src: nearingDenoisingDenoisersIndependent2018 (FT) · trail: MB-01 §2.10 · from: MB-01:B-0212..0215
- **denoising-clustering.4** Bacteroides varied from 20.6% to 24.6% across pipelines.
  conf: not stated · class: not stated · holds: pipeline comparison · src: marizzoniComparisonBioinformaticsPipelines2020 (FT) · trail: MB-01 §2.10 · from: MB-01:A-093, MB-01:B-0130
- **denoising-clustering.5** The operating system mattered little for pipeline output.
  conf: not stated · class: not stated · holds: pipeline comparison · src: marizzoniComparisonBioinformaticsPipelines2020 (FT) · trail: MB-01 §7. Bounds · from: MB-01:B-0421
- **denoising-clustering.6** mothur and QIIME1 returned 10 to 200 times the expected number of sequences.
  conf: repl (marker) · class: meas (marker) · holds: the authors also built nf-core/ampliseq; they report pipeline-dependent interpretations · src: straubInterpretationsEnvironmentalMicrobial2020 (FT; meas; repl; authors also built nf-core/ampliseq) · trail: MB-01 §2.10 · from: MB-01:I-0053, MB-01:A-094, MB-01:B-0218, MB-01:C-087
- **denoising-clustering.7** Faith's PD was overestimated 1.3 to 2.7-fold by QIIME2, 2 to 18-fold by QIIME1 and 3.5 to 29-fold by mothur.
  conf: repl (marker) · class: meas (marker) · holds: QIIME2, QIIME1 and mothur; the authors also built nf-core/ampliseq · src: straubInterpretationsEnvironmentalMicrobial2020 (FT; meas; repl; authors also built nf-core/ampliseq) · trail: MB-01 §2.10 · from: MB-01:I-0053
- **denoising-clustering.8** DADA2 had the best sensitivity and UNOISE3 the best balance; QIIME-uclust produced on average 134 one-off and 412 other spurious OTUs.
  conf: repl (marker) · class: meas (marker) · holds: mock runs · src: prodanComparingBioinformaticPipelines2020 (FT; meas; repl) · trail: MB-01 §2.10 · from: MB-01:I-0054, MB-01:B-0219, MB-01:B-0279
- **denoising-clustering.9** The DADA2 developers report 93 output sequences on a 57-strain mock, against 249 for mothur and 378 for QIIME.
  conf: not stated · class: meas (marker) · holds: developer claim · src: callahanDADA2HighresolutionSample2016 (FT; meas; developer claim) · trail: MB-01 §2.10 · from: MB-01:I-0055
- **denoising-clustering.10** After OTU clustering and singleton removal, tables were about 50% (mock communities) to 80% (gnotobiotic mice) spurious taxa; the authors propose a 0.25% relative-abundance cutoff.
  conf: single (marker) · class: meas (marker) · holds: mocks and gnotobiotic mice; the review called the tables "unfiltered", which the critic corrected · src: reitmeierHandlingSpuriousSequences2021 (FT; meas; single) · trail: MB-01 §critic, §2.10 · from: MB-01:I-0056, MB-01:C-058, MB-01:C-072
- **denoising-clustering.11** The most abundant spurious taxon in mocks had a median relative abundance of 0.12%.
  conf: not stated · class: not stated · holds: mocks · src: reitmeierHandlingSpuriousSequences2021 (FT) · trail: MB-01 §2.13 · from: MB-01:B-0243
- **denoising-clustering.12** QIIME closed- and open-reference OTUs inflated richness to 1,607 to 5,824 OTUs where about 20 were expected; on V4 mocks, 56 to 88% of predicted genus names were false positives.
  conf: single (marker) · class: meas (marker) · holds: mocks · src: edgarAccuracyMicrobialCommunity2017 (FT; meas; single) · trail: MB-01 §2.10 · from: MB-01:I-0057, MB-01:B-0131, MB-01:B-0221
- **denoising-clustering.13** In leaf litter, bacterial OTU richness was about half of ESV richness (slope 0.46), but alpha and beta metrics correlated at r > 0.90 and inferences matched.
  conf: cont (marker) · class: meas (marker) · holds: leaf litter · src: glassmanBroadscaleEcologicalPatterns2018 (FT; meas; cont) · trail: MB-01 §2.10 · from: MB-01:I-0058, MB-01:B-0418
- **denoising-clustering.14** In 227 freshwater sediment, seston and mussel-gut samples, ASV richness was about half of OTU richness, and Mollicutes dominated mussel gut by ASVs but were absent from OTU tables; the authors attribute the reversal partly to higher richness in sediment.
  conf: cont (marker) · class: meas (marker) · holds: freshwater samples · src: chiarelloRankingBiasesChoice2022 (FT; meas; cont) · trail: MB-01 §2.10 · from: MB-01:I-0059, MB-01:B-0223, MB-01:B-0224
- **denoising-clustering.15** The direction of the OTU versus ASV richness difference conflicts between studies (Glassman and Martiny 2018 versus Chiarello 2022).
  conf: cont (note: "OTU versus ASV richness (contested)") · class: not stated · holds: leaf litter versus freshwater samples · src: glassmanBroadscaleEcologicalPatterns2018 (FT; meas; cont), chiarelloRankingBiasesChoice2022 (FT; meas; cont) · trail: MB-01 §2.10, §6. Where · from: MB-01:A-096, MB-01:A-120, MB-01:B-0222, MB-01:B-0402
- **denoising-clustering.16** In soil and plant samples, OTUs versus ASVs changed which families were called differentially abundant, mostly families under 0.1% abundance.
  conf: single (marker) · class: meas (marker) · holds: soil and plant samples · src: joosDaringDifferentialMetabarcoding2020 (FT; meas; single) · trail: MB-01 §2.10 · from: MB-01:I-0060
- **denoising-clustering.17** The identity threshold that best matched species was about 99% for full-length 16S and about 100% for V4.
  conf: single (marker) · class: deriv (marker) · holds: abstract only · src: edgarUpdating97Identity2018 (AB; deriv; single) · trail: MB-01 §2.10 · from: MB-01:I-0061
- **denoising-clustering.18** As biomass fell in a dilution series, contaminants made up a growing share of inferred communities under every method; the authors state no inference method alone separates contaminants from true sequences.
  conf: single (marker) · class: meas (marker) · holds: dilution series · src: carusoPerformanceMicrobiomeSequence2019 (FT; meas; single) · trail: MB-01 §2.10 · from: MB-01:I-0062, MB-01:B-0225
- **denoising-clustering.19** According to the DADA2 documentation, independent per-sample processing needs at least two error-free reads to detect an ASV, and pooling finds more ASVs per sample.
  conf: not stated · class: not stated · holds: documentation · src: callahanDADA2DocumentationPseudopooling (DOCUMENTATION) · trail: MB-01 §2.10 · from: MB-01:B-0226, MB-01:B-0227
- **denoising-clustering.20** Intragenomic variants split genomes into several ASVs: on average 0.58 variants per copy for full-length 16S and 0.25 for V4.
  conf: cont (marker) · class: deriv (marker) · holds: full-length 16S and V4 · src: schlossAmpliconSequenceVariants2021 (FT; deriv; cont) · trail: MB-01 §2.5 · from: MB-01:I-0039, MB-01:A-071, MB-01:B-0123
- **denoising-clustering.21** Full-length PacBio sequencing recovered intragenomic variants in their expected integral ratios.
  conf: single (marker) · class: meas (marker) · holds: developer study · src: callahanHighthroughputAmpliconSequencing2019 (FT; meas; single; developer) · trail: MB-01 §2.5 · from: MB-01:I-0040

### chimeras: chimera formation and detection
needs: pcr, denoising-clustering

- **chimeras.1** Documented chimera-detection choices are UCHIME, UCHIME2 and ChimeraSlayer.
  conf: not stated · class: not stated · holds: pipelines · src: none (the reviewer's synthesis) · trail: MB-01 §2.11 · from: MB-01:A-014
- **chimeras.2** Chimeras formed reproducibly across independent amplifications of a known mixture.
  conf: single (critic: MB-01:C-090) · class: meas (marker) · holds: Sanger and 454; rests on Haas 2011 alone · src: haasChimeric16SRRNA2011 (FT; meas; repl; Sanger and 454) · trail: MB-01 §2.11, §critic · from: MB-01:I-0063, MB-01:A-075, MB-01:B-0125, MB-01:C-090
- **chimeras.3** Less-abundant species showed chimera rates above 70%, and chimera count correlated with organism abundance (R2 = 0.97) in a staggered mock.
  conf: not stated · class: not stated · holds: 454, staggered mock · src: haasChimeric16SRRNA2011 (FT) · trail: MB-01 §2.11 · from: MB-01:A-074, MB-01:B-0228, MB-01:B-0229
- **chimeras.4** Chimeras inflate richness and create false novel taxa.
  conf: not stated · class: not stated · holds: as reported in the D2 answer and Table 1 · src: haasChimeric16SRRNA2011 (FT), szeImpactDNAPolymerase2019 (FT, re-opened) · trail: MB-01 §2.11 · from: MB-01:A-072, MB-01:B-0124
- **chimeras.5** At 30 cycles, chimeras made up 0.9% (Accuprime) to 18.2% (Platinum) of reads depending on polymerase, and UCHIME sensitivity was 50 to 87% at 25 or more cycles.
  conf: not stated · class: not stated · holds: five polymerases; figures checked against the re-opened full text · src: szeImpactDNAPolymerase2019 (FT, re-opened) · trail: MB-01 §2.11, §critic · from: MB-01:A-073, MB-01:B-0232
- **chimeras.6** ChimeraSlayer detected over 87% of simulated chimeras when parents diverged by 4% or more, with a 1.6% false-positive rate, and sensitivity fell for every method as parents became more similar.
  conf: not stated · class: model (note: "simulated chimeras") · holds: simulated chimeras · src: none (the note names no source for this sentence) · trail: MB-01 §2.11 · from: MB-01:B-0230, MB-01:B-0231
- **chimeras.7** UCHIME2's author states that error-free chimera prediction is "impossible in principle".
  conf: not stated · class: assert (note: "developer claim") · holds: preprint, abstract only · src: edgarUCHIME2ImprovedChimera2016 (AB; PREPRINT; developer claim) · trail: MB-01 §2.11 · from: MB-01:B-0233

### taxonomy: taxonomic assignment
needs: denoising-clustering

- **taxonomy.1** Documented classification choices are RDP NBC, q2-feature-classifier, SINTAX, IDTAXA or MAPseq, against SILVA, Greengenes, RDP or GTDB-type references, optionally with habitat-weighted priors.
  conf: not stated · class: not stated · holds: software and benchmarks · src: kaehlerSpeciesAbundanceInformation2019 (FT) · trail: MB-01 §2.12 · from: MB-01:A-015
- **taxonomy.2** Cross-validated by identity to the reference, all tested classifiers were at most 50% accurate on V4: genus accuracy was about 100% at 100% identity and about 50% at 97%.
  conf: single (marker) · class: meas (marker) · holds: reference sets; from one author who also develops competing classifiers · src: edgarAccuracyTaxonomyPrediction2018 (FT; meas; single) · trail: MB-01 §2.12, §critic · from: MB-01:I-0064, MB-01:A-097, MB-01:B-0131, MB-01:B-0234, MB-01:C-089
- **taxonomy.3** Edgar argues that mocks overstate classification accuracy because all their members are named type strains.
  conf: not stated · class: not stated · holds: the author's argument · src: edgarAccuracyTaxonomyPrediction2018 (FT) · trail: MB-01 §2.12 · from: MB-01:A-099, MB-01:B-0235
- **taxonomy.4** On mocks, the q2-feature-classifier methods reached median genus F above 0.8.
  conf: not stated · class: meas (marker) · holds: developer claim · src: bokulichOptimizingTaxonomicClassification2018 (FT; meas; developer claim) · trail: MB-01 §2.12 · from: MB-01:I-0065, MB-01:A-099
- **taxonomy.5** Habitat-weighted priors cut species-level error from 25% to 14%.
  conf: not stated · class: meas (marker) · holds: developer claim · src: kaehlerSpeciesAbundanceInformation2019 (FT; meas; developer claim) · trail: MB-01 §2.12 · from: MB-01:I-0066
- **taxonomy.6** IDTAXA over-classified less when the true taxa were absent from the training set.
  conf: not stated · class: meas (marker) · holds: developer claim; reference listed under Murali, cited by the bioinformatics angle · src: muraliIDTAXANovelApproach2018 (FT; meas; developer claim) · trail: MB-01 §2.12 · from: MB-01:I-0067, MB-01:B-0236
- **taxonomy.7** Estimated annotation error is about 10% for RDP and about 17% for SILVA v128 and Greengenes 13.5, judged from conflicting labels on identical sequences.
  conf: single (marker) · class: deriv (marker) · holds: reference databases; from one author who also develops competing classifiers · src: edgarTaxonomyAnnotationGuide2018 (FT; deriv; single) · trail: MB-01 §2.12, §critic · from: MB-01:I-0068, MB-01:A-098, MB-01:C-089
- **taxonomy.8** On simulated gut, ocean and soil communities, genus recall was 67 to 80%, and assignments varied by up to 40% between 16S subregions within a pipeline.
  conf: single (marker) · class: model (marker) · holds: simulated communities · src: almeidaBenchmarkingTaxonomicAssignments2018 (FT; model; single) · trail: MB-01 §2.12 · from: MB-01:I-0069

### contamination: contaminants, negative controls and well-to-well leakage
needs: departure

- **contamination.1** Documented contaminant-handling choices are dropping taxa seen in negative controls, decontam (frequency or prevalence mode), SourceTracker, or relative-abundance cutoffs.
  conf: not stated · class: not stated · holds: tools and practice · src: davisSimpleStatisticalIdentification2018 (FT), karstensControllingContaminantsLowbiomass2019 (FT) · trail: MB-01 §2.13 · from: MB-01:A-016
- **contamination.2** In a Salmonella bongori dilution series run at three institutes, contaminants dominated by about 10^3 input cells, more so at 40 than at 20 cycles; profiles differed by kit and laboratory.
  conf: repl (marker) · class: meas (marker) · holds: dilution series at three institutes · src: salterReagentLaboratoryContamination2014 (FT; meas; repl) · trail: MB-01 §2.13 · from: MB-01:I-0070, MB-01:A-100, MB-01:B-0133, MB-01:B-0237
- **contamination.3** In an 8-member mock diluted 3-fold eight times, contaminant reads rose from 0.1% to 80.1% and ASVs from 18 to 381.
  conf: single (marker) · class: meas (marker) · holds: one diluted mock · src: karstensControllingContaminantsLowbiomass2019 (FT; meas; single) · trail: MB-01 §2.13 · from: MB-01:I-0071, MB-01:A-101, MB-01:B-0132, MB-01:B-0238
- **contamination.4** Removing every sequence present in the negative control wrongly removed more than 20% of expected sequences, since three of the eight mock ASVs appeared in the control.
  conf: not stated · class: not stated · holds: one diluted mock · src: karstensControllingContaminantsLowbiomass2019 (FT) · trail: MB-01 §2.13 · from: MB-01:B-0239, MB-01:B-0426
- **contamination.5** decontam's frequency method removed 70 to 90% of contaminants and no expected sequences.
  conf: not stated · class: not stated · holds: one diluted mock · src: karstensControllingContaminantsLowbiomass2019 (FT) · trail: MB-01 §2.13 · from: MB-01:B-0240, MB-01:I-0071
- **contamination.6** SourceTracker removed over 98% of contaminants when sources were well defined but failed on over 97% when they were not.
  conf: not stated · class: not stated · holds: one diluted mock · src: karstensControllingContaminantsLowbiomass2019 (FT) · trail: MB-01 §2.13 · from: MB-01:B-0241, MB-01:B-0427, MB-01:I-0071
- **contamination.7** Well-to-well contamination arose mainly at extraction, less at library preparation, mostly into neighbouring wells (rarely up to 10 wells away), and was greatest in low-biomass samples.
  conf: single (marker) · class: meas (marker) · holds: well-to-well leakage · src: minichQuantifyingUnderstandingWelltowell2019 (FT; meas; single) · trail: MB-01 §2.13 · from: MB-01:I-0072, MB-01:A-102
- **contamination.8** decontam's makers describe a frequency mode that assumes contaminant DNA is roughly constant across samples.
  conf: not stated · class: assert (note: "decontam's makers describe") · holds: developer claim · src: davisSimpleStatisticalIdentification2018 (FT; developer claim) · trail: MB-01 §2.13 · from: MB-01:B-0242
- **contamination.9** In a survey of 265 papers in the 2018 issues of Microbiome and The ISME Journal that used any high-throughput community sequencing (16S, shotgun, metatranscriptomics, ITS, 18S and others), 30% (79) reported a negative control and 10% (27) a positive control; it is not a 16S-only figure.
  conf: single (critic: MB-01:C-005) · class: meas (marker) · holds: two journals, one year, all community sequencing types; the only usage survey · src: hornungIssuesCurrentStandards2019 (FT; meas; single) · trail: MB-01 §critic, §2.13 · from: MB-01:C-004, MB-01:C-005, MB-01:I-0073, MB-01:A-017, MB-01:A-033
- **contamination.10** A review proposes the RIDE checklist.
  conf: not stated · class: assert (marker) · holds: a review, abstract only · src: eisenhoferContaminationLowMicrobial2019 (AB; assert) · trail: MB-01 §2.13 · from: MB-01:I-0074
- **contamination.11** Contamination varies inversely with biomass and is specific to the kit and laboratory.
  conf: not stated · class: not stated · holds: see contamination.2, contamination.3, contamination.7 · src: salterReagentLaboratoryContamination2014 (FT), karstensControllingContaminantsLowbiomass2019 (FT), minichQuantifyingUnderstandingWelltowell2019 (FT) · trail: MB-01 §2.13 · from: MB-01:A-103

### run-batch: run, batch and laboratory effects
needs: library-sequencing

- **run-batch.1** One HiSeq run lost an archaeal mock taxon from all samples and shifted others by more than 2-fold; re-running the same amplicons was normal.
  conf: single (marker) · class: meas (marker) · holds: one HiSeq run · src: yehTaxonDisappearanceMicrobiome2018 (FT; meas; single) · trail: MB-01 §4.3 · from: MB-01:I-0101, MB-01:A-089, MB-01:B-0128, MB-01:B-0309
- **run-batch.2** A PCR machine with a mis-set annealing temperature produced a batch outlier.
  conf: not stated · class: not stated · holds: checked against full text by the critic · src: silvermanMeasuringMitigatingPCR2021 (FT) · trail: MB-01 §4.3, §critic · from: MB-01:B-0310, MB-01:C-054
- **run-batch.3** Per-strain CV across five runs had a median of 11.8% (range 5.5 to 73.7%), and under-represented strains varied most.
  conf: not stated · class: not stated · holds: 20-strain mock · src: laursenGenomicGCcontentAffects2017 (FT) · trail: MB-01 §4.3 · from: MB-01:A-204, MB-01:B-0311, MB-01:B-0171
- **run-batch.4** There was no significant lane or day effect, and preparation day and lane did not change profile variability.
  conf: single (marker) · class: meas (marker) · holds: soil and faecal samples; abstract only · src: kennedyEvaluatingBiasIlluminabased2014 (AB; meas; single) · trail: MB-01 §4.3, §2.4 · from: MB-01:I-0031, MB-01:A-090, MB-01:B-0312, MB-01:B-0413, MB-01:B-0182
- **run-batch.5** Mean relative abundances were reproducible across two runs and two depths.
  conf: not stated · class: not stated · holds: two runs and two depths · src: pintoPCRBiasesDistort2012 (FT) · trail: MB-01 §4.3 · from: MB-01:A-199, MB-01:B-0313
- **run-batch.6** Interlaboratory differences were substantial, and absolute diversity was not comparable between laboratories even with the same pipeline.
  conf: not stated · class: not stated · holds: 15 laboratories (MBQC) · src: sinhaAssessmentVariationMicrobial2017 (FT) · trail: MB-01 §2.2, §4.3 · from: MB-01:B-0154, MB-01:B-0314, MB-01:I-0011
- **run-batch.7** Batch-correction tools exist, and their makers claim they work.
  conf: not stated · class: assert (note: "their makers claim they work") · holds: makers' claims, abstract only · src: gibbonsCorrectingBatchEffects2018 (AB), lingBatchEffectsRemoval2022 (AB; makers' claims) · trail: MB-01 §4.3 · from: MB-01:B-0315
- **run-batch.8** Run and batch effects are reported as whole-run taxon loss (Yeh 2018), a batch outlier (Silverman 2021) and between-laboratory effects (MBQC), against no lane or day effect (Kennedy 2014) and relative abundances reproducible across runs (Pinto and Raskin 2012).
  conf: not stated · class: not stated · holds: see run-batch.1 to run-batch.6 · src: yehTaxonDisappearanceMicrobiome2018 (FT; meas; single), silvermanMeasuringMitigatingPCR2021 (FT), sinhaAssessmentVariationMicrobial2017 (FT), kennedyEvaluatingBiasIlluminabased2014 (AB; meas; single), pintoPCRBiasesDistort2012 (FT) · trail: MB-01 §answers · from: MB-01:A-198, MB-01:A-199

### bias-consistency: whether the departure is consistent across samples, and its calibration
needs: extraction, primers, pcr, copy-number-correction

- **bias-consistency.1** Whether bias is consistent across samples is less settled, and it is where the evidence is thinnest: it rests mainly on one reanalysis of 7 taxa, with contrary or limiting field evidence.
  conf: unclear (note: "Whether bias is consistent across samples is less settled") · class: not stated · holds: mocks and a few field and stool studies · src: none (the reviewer's synthesis across bias-consistency.2 to 13) · trail: MB-01 §1. Overview, §2.14, §critic · from: MB-01:B-0094, MB-01:A-114, MB-01:C-022, MB-01:B-0244 · rating: "weak for per-step relative-abundance magnitudes and for consistency across samples"
- **bias-consistency.2** Modelling each step as multiplying taxon abundances by a taxon-specific efficiency, the error in taxon ratios was "consistent across samples", while the error in proportions "varied dramatically in both magnitude and direction"; bias behaves as a consistent multiplicative factor per taxon that calibration controls can correct.
  conf: single (marker) · class: model (marker) · holds: one dataset modelled for this question: 7 taxa mixed as cells (Brooks 2015 cell mixtures), reanalysed · src: mclarenConsistentCorrectableBias2019 (FT; model; single) · trail: MB-01 §2.14, §1. Overview, MB-02 §D1.4 · from: MB-01:I-0002, MB-01:A-108, MB-01:A-299, MB-01:B-0245, MB-01:B-0246, MB-01:C-019, MB-01:C-128, MB-02:B-0202, MB-01:A-301 · rating: "weak for consistency"
- **bias-consistency.3** On the ratio scale, extraction bias was consistent across samples within a protocol in the 7-taxon vaginal mock.
  conf: not stated · class: not stated · holds: one 16S cell-mixture dataset · src: mclarenConsistentCorrectableBias2019 (FT, re-opened) · trail: MB-01 §2.2 · from: MB-01:A-048, MB-01:B-0111, MB-01:B-0158
- **bias-consistency.4** A 10-species shotgun spike-in gave a consistent extraction-bias profile across faecal backgrounds; protocol H showed up to 2,751-fold maximum pairwise bias.
  conf: not stated · class: not stated · holds: shotgun, not 16S (INDIRECT); known only through McLaren 2019 (secondary) · src: costeaTowardsStandardsHuman2017 (SEC; INDIRECT, shotgun), mclarenConsistentCorrectableBias2019 (FT, re-opened) · trail: MB-01 §2.2 · from: MB-01:A-049, MB-01:B-0159, MB-01:C-019
- **bias-consistency.5** Six parameters explained almost all systematic error in the Brooks 16S cell mixtures, and calibration (2 calibration samples, 69 calibrated samples) cut mean Bray-Curtis error from 0.35 to 0.08, a 92.6% lower mean squared error; the Costea shotgun calibration is reported only qualitatively ("removed most of the systematic error").
  conf: not stated · class: not stated · holds: 7-taxon 16S cell mixtures; the review attributed the Bray-Curtis figure to a shotgun dataset, which the critic corrected against the full text · src: mclarenConsistentCorrectableBias2019 (FT, re-opened), costeaTowardsStandardsHuman2017 (SEC; INDIRECT, shotgun) · trail: MB-01 §critic, §2.14 · from: MB-01:C-021, MB-01:C-055, MB-01:C-066, MB-01:C-067, MB-01:C-068, MB-01:C-069, MB-01:B-0247
- **bias-consistency.6** The authors of the ratio-scale model list where it may fail: PCR saturation, taxa aggregated with differing efficiencies, matrix differences between controls and samples, and taxa absent from the controls.
  conf: not stated · class: not stated · holds: the authors' stated limits · src: mclarenConsistentCorrectableBias2019 (FT, re-opened) · trail: MB-01 §2.14 · from: MB-01:B-0248
- **bias-consistency.7** Brooks et al. found significant mixture-blending terms on the same data and concluded that one taxon's observed proportion depends on which others are present (bias is composition dependent).
  conf: not stated · class: not stated · holds: the same 7-taxon cell mixtures as McLaren 2019 · src: brooksTruthMetagenomicsQuantifying2015 (FT) · trail: MB-01 §2.14, §1. Overview · from: MB-01:A-109, MB-01:B-0095, MB-01:B-0249
- **bias-consistency.8** The ratio-scale and composition-dependence readings of the same data conflict; McLaren et al. attribute the apparent dependence to working on the proportion scale.
  conf: cont (note: "The two readings conflict") · class: not stated · holds: one dataset, two analyses · src: mclarenConsistentCorrectableBias2019 (FT, re-opened), brooksTruthMetagenomicsQuantifying2015 (FT; meas; cont) · trail: MB-01 §2.14, §6. Where · from: MB-01:A-115, MB-01:B-0250, MB-01:B-0398
- **bias-consistency.9** PCR bias was consistent per taxon in mocks.
  conf: not stated · class: not stated · holds: mocks · src: silvermanMeasuringMitigatingPCR2021 (FT) · trail: MB-01 §2.4 · from: MB-01:A-064, MB-01:B-0119
- **bias-consistency.10** PCR-bias calibration corrected composition toward truth in all 10 held-out mocks; the authors note that their mock "ground truth" carried its own bias and that the method sometimes estimated the wrong direction for some taxa.
  conf: not stated · class: not stated · holds: gut-isolate mocks · src: silvermanMeasuringMitigatingPCR2021 (FT) · trail: MB-01 §2.4 · from: MB-01:B-0175, MB-01:B-0176, MB-01:I-0027
- **bias-consistency.11** In four stool samples, the sample explained R2 = 0.79 of variation, cycle number 0.044 and polymerase 0.033, and "this bias was inconsistent for human stool samples": cycle-related shifts were inconsistent across stool samples and small next to between-person differences.
  conf: single (marker) · class: meas (marker) · holds: four human stool samples; figures checked against the re-opened full text · src: szeImpactDNAPolymerase2019 (FT, re-opened; meas; single) · trail: MB-01 §2.4, §2.14, §critic · from: MB-01:I-0028, MB-01:A-065, MB-01:B-0120, MB-01:B-0178, MB-01:B-0253, MB-01:B-0400, MB-01:C-020
- **bias-consistency.12** Field and stool studies show bias that does not carry over from mocks (Parada 2016) or that varies between samples (Sze and Schloss 2019).
  conf: mixed (marker) · class: meas (marker) · holds: marine field samples (abstract only, one primer pair, one taxon) and four stool samples · src: paradaEveryBaseMatters2016 (AB; meas; repl), szeImpactDNAPolymerase2019 (FT; meas; single) · trail: MB-01 §1. Overview, §2.14 · from: MB-01:I-0003, MB-01:A-110, MB-01:A-300, MB-01:C-092, MB-01:C-020
- **bias-consistency.13** Variation between sample types or samples is shown by a field-versus-mock SAR11 bias for the 515F-Y/806R pair (Parada 2016, abstract only), inconsistent cycle effects in four stool samples (Sze and Schloss 2019), an extraction yield of 40 to 84% (Zemb 2020) and a 66.7-fold spike-in range (Zhou 2011, abstract).
  conf: not stated · class: not stated · holds: the critic's list of evidence on variation, each from one study · src: paradaEveryBaseMatters2016 (AB), szeImpactDNAPolymerase2019 (FT, re-opened), zembAbsoluteQuantitationMicrobes2020 (FT; meas; single), zhouReproducibilityQuantitationAmplicon2011 (FT per statistics angle; meas; single) · trail: MB-01 §critic, §2.14 · from: MB-01:C-020, MB-01:B-0251
- **bias-consistency.14** A synthetic spike-in quantified before and after extraction recovered 40% to 84%, so extraction yield varied between samples.
  conf: single (marker) · class: meas (marker) · holds: a synthetic spike-in · src: zembAbsoluteQuantitationMicrobes2020 (FT; meas; single) · trail: MB-01 §2.2, §2.14, §5.5 · from: MB-01:I-0016, MB-01:A-050, MB-01:A-268, MB-01:B-0112, MB-01:B-0254, MB-01:B-0387
- **bias-consistency.15** A 0.1% genomic spike was recovered at 0.06% to 5.34% of reads across soils, a 66.7-fold range.
  conf: single (marker) · class: meas (marker) · holds: soils, 454; the 66.7-fold figure is in the abstract (AB-derived), while the 0.06 to 5.34% range needs the body and could not be confirmed by the critic · src: zhouReproducibilityQuantitationAmplicon2011 (FT per statistics angle; meas; single) · trail: MB-01 §2.14, §critic · from: MB-01:I-0075, MB-01:A-268, MB-01:B-0387, MB-01:C-075, MB-01:C-076, MB-01:C-031
- **bias-consistency.16** Whether mock-derived bias applies to field samples is contested: Parada 2016 against calibration claims (McLaren 2019; Silverman 2021).
  conf: cont (note: "Where the evidence conflicts") · class: not stated · holds: one marine primer-pair study against two mock-based calibration studies · src: paradaEveryBaseMatters2016 (AB; meas; repl), mclarenConsistentCorrectableBias2019 (FT, re-opened), silvermanMeasuringMitigatingPCR2021 (FT) · trail: MB-01 §6. Where, §answers · from: MB-01:A-121, MB-01:B-0403
- **bias-consistency.17** Modelling the PCR process, calibrated with mocks, has been used to estimate starting proportions in eukaryotic eDNA.
  conf: not stated · class: model (marker) · holds: eukaryotic eDNA, INDIRECT; abstract only · src: sheltonTowardQuantitativeMetabarcoding2023 (AB; model; INDIRECT) · trail: MB-01 §5.1 · from: MB-01:I-0111
- **bias-consistency.18** The consistency of extraction bias across real soil or water matrices has not been measured in the sources found.
  conf: not stated · class: search (note: "has not been measured in the sources found") · holds: lab and bioinformatics angles · src: none (the review's search) · trail: MB-01 §answers · from: MB-01:A-125, MB-01:A-126

### reads-per-sample: reads per sample and their variation between samples
needs: library-sequencing

- **reads-per-sample.1** The Earth Microbiome Project averaged 80,000 sequences per sample over 27,751 samples and rarefied to 5,000.
  conf: not stated · class: not stated · holds: EMP survey · src: thompsonCommunalCatalogueReveals2017 (FT) · trail: MB-01 §3.3 · from: MB-01:A-155, MB-01:B-0274
- **reads-per-sample.2** In four environments of the EMP, mean prevalence of tag sequences rose with depth up to 50,000, so 5,000 under-estimated prevalence.
  conf: not stated · class: not stated · holds: EMP, four environments · src: thompsonCommunalCatalogueReveals2017 (FT) · trail: MB-01 §3.3 · from: MB-01:B-0275, MB-01:B-0274
- **reads-per-sample.3** In one 360-sample MiSeq run, reads averaged 9,913 pairs per sample, with 95% of samples above 2,454.
  conf: not stated · class: not stated · holds: one run; figures need the body, which the critic could not confirm as open full text · src: kozichDevelopmentDualindexSequencing2013 (FT) · trail: MB-01 §3.3, §critic · from: MB-01:A-156, MB-01:B-0277, MB-01:C-076
- **reads-per-sample.4** A dilution-series run ranged from 40,927 to 251,419 reads per sample.
  conf: not stated · class: not stated · holds: one run · src: karstensControllingContaminantsLowbiomass2019 (FT) · trail: MB-01 §3.3 · from: MB-01:A-157, MB-01:B-0278
- **reads-per-sample.5** Three mock runs gave 36,464 to 146,653 read pairs.
  conf: not stated · class: not stated · holds: mock runs · src: prodanComparingBioinformaticPipelines2020 (FT) · trail: MB-01 §3.3 · from: MB-01:B-0279
- **reads-per-sample.6** Across 12 public V4 studies, reads per sample varied up to about 100-fold within a study: human 10,439 to 422,904 (median 32,452, n = 490), bioethanol 3,690 to 356,027, mice 1,804 to 30,311, soil 46,622 to 58,935 (n = 18) and marine 132,895 to 256,758 (n = 7).
  conf: single (marker) · class: meas (marker) · holds: per study, not per run; rests mainly on Schloss 2024b Table 1, checked against the re-opened full text · src: schlossRarefactionCurrentlyBest2024 (FT, re-opened; meas; single) · trail: MB-01 §3.3, §critic · from: MB-01:I-0084, MB-01:A-158, MB-01:A-172, MB-01:A-184, MB-01:A-302, MB-01:B-0280, MB-01:C-023 · rating: "Moderate for reads per sample per study"
- **reads-per-sample.7** Schloss attributes the spread of reads per sample to compounding random error when PCR products are pooled.
  conf: not stated · class: not stated · holds: the author's attribution · src: schlossRarefactionCurrentlyBest2024 (FT, re-opened) · trail: MB-01 §3.3 · from: MB-01:B-0281
- **reads-per-sample.8** Schloss cites studies reporting that depth correlates positively with biomass despite normalisation (Minich et al. 2022 on 101 fish species; Cruz et al. 2021 on an equivolumetric protocol), known only secondarily.
  conf: not stated · class: not stated · holds: SECONDARY via Schloss 2024b; the primary studies were not opened · src: schlossRarefactionCurrentlyBest2024 (FT, re-opened) · trail: MB-01 §3.3, §critic · from: MB-01:B-0282, MB-01:C-111
- **reads-per-sample.9** Makers state more than 20 million reads per MiSeq v3 run and more than 100,000 per sample at 96-plex, "sufficient to fully survey the bacterial composition"; a core facility gives about 20 million (v3) and about 16 million (v2) reads per run, with more than 100,000 per sample recommended.
  conf: not stated · class: assert (note: "maker's claim") · holds: makers' and core-facility statements · src: illumina16SMetagenomicSequencing (DOCUMENTATION; maker's claim), emoryAmplicon16SMetagenomics (PROTOCOL) · trail: MB-01 §3.3 · from: MB-01:A-159, MB-01:B-0283, MB-01:B-0284
- **reads-per-sample.10** No peer-reviewed coefficient of variation of reads per sample within a run after equimolar pooling was found; the primary studies on the correlation of library size with biomass (Minich et al. 2022; Cruz et al. 2021) are known only through Schloss 2024b and were not opened.
  conf: not stated · class: search (note: "No peer-reviewed coefficient of variation of reads per sample within a run after equimolar pooling") · holds: all three angles searched; web search returned only forum posts · src: none (the review's search) · trail: MB-01 §3.3, §Search record, §critic · from: MB-01:A-160, MB-01:A-173, MB-01:A-304, MB-01:B-0287, MB-01:B-0288, MB-01:B-0444, MB-01:C-029, MB-01:C-111

### microbial-load: microbial load
needs: none

- **microbial-load.1** Microbial load differed up to tenfold among healthy human faeces.
  conf: repl (marker) · class: meas (marker) · holds: human faeces; abstract only · src: vandeputteQuantitativeMicrobiomeProfiling2017 (AB; meas; repl) · trail: MB-01 §3.5 · from: MB-01:I-0089, MB-01:A-167, MB-01:C-023
- **microbial-load.2** Prokaryote load differed 27-fold among Antarctic seawater stations.
  conf: single (marker) · class: meas (marker) · holds: Antarctic seawater · src: linTowardsQuantitativeMicrobiome2019 (FT; meas; single) · trail: MB-01 §3.5 · from: MB-01:I-0090, MB-01:A-167
- **microbial-load.3** Microbial load varied by more than six orders of magnitude across mouse gut sites.
  conf: single (marker) · class: meas (marker) · holds: mouse gut · src: barlowQuantitativeSequencingFramework2020 (FT; meas; single) · trail: MB-01 §3.5 · from: MB-01:I-0091, MB-01:A-167

### abundance-distribution: shape of taxon abundance distributions
needs: none

- **abundance-distribution.1** In 24 grassland soils, the best-fitting distributions were reported as exponential or inverse gamma; these best fits are in supplementary Table S3, the main text does not state which distributions won, and they were not verified.
  conf: single (marker) · class: model (marker) · holds: 24 Oklahoma grassland soils, 454; rests on unread or unshown supplementary material · src: zhouRandomSamplingProcess2013 (FT; model; single) · trail: MB-01 §3.4, §critic · from: MB-01:I-0085, MB-01:A-162, MB-01:C-026, MB-01:C-077, MB-01:C-078, MB-01:C-079, MB-01:C-031
- **abundance-distribution.2** In the Brazil soil, 26,079 reads and 2,880 observed species were fitted equally well by communities of 10^4, 10^5 and 10^6 species, so the tail cannot be identified from sample data.
  conf: repl (marker) · class: model (marker) · holds: one Brazilian soil; rests on a full text that was not openly retrievable, and the figures could not be confirmed by the critic · src: haegemanRobustEstimationMicrobial2013 (FT; model; repl) · trail: MB-01 §3.4, §critic · from: MB-01:I-0086, MB-01:A-163, MB-01:C-028, MB-01:C-076
- **abundance-distribution.3** After copy-number correction, rank-abundance distributions from human skin and ocean fit a lognormal better.
  conf: single (critic: MB-01:C-027) · class: not stated · holds: one study that pools ocean and skin into one item; the same paper's simulations assumed a lognormal · src: kembelIncorporating16SGene2012 (FT) · trail: MB-01 §3.4, §critic · from: MB-01:A-164, MB-01:B-0289, MB-01:C-027, MB-01:C-134
- **abundance-distribution.4** Lognormal dynamics best explained abundance distributions across more than 20,000 samples.
  conf: single (marker) · class: model (marker) · holds: environmental, engineered and host samples including soils; no per-environment breakdown in the abstract; abstract only · src: shoemakerMacroecologicalTheoryMicrobial2017 (AB; model; single) · trail: MB-01 §3.4, MB-02 §D3.1 · from: MB-01:I-0087, MB-01:A-165, MB-01:B-0291, MB-02:A-087, MB-02:B-0307, MB-02:B-0309
- **abundance-distribution.5** Mean abundances across taxa were lognormal "for all the data sets considered", and each taxon's abundance across communities was gamma-distributed, with variance proportional to the squared mean (Taylor's law with exponent 2).
  conf: single (marker) · class: model (marker) · holds: several biomes; per-biome results are in supplementary figures that were not read · src: grilliMacroecologicalLawsDescribe2020 (FT, partly re-opened; model; single) · trail: MB-01 §3.4, §4.2 · from: MB-01:I-0088, MB-01:A-166, MB-01:A-193, MB-01:B-0292, MB-01:B-0299
- **abundance-distribution.6** A dominance scaling law held across about 35,000 sites.
  conf: not stated · class: not stated · holds: cross-environment compilation including soils, not reported separately in the abstract · src: loceyScalingLawsPredict2016 (AB) · trail: MB-02 §D3.1 · from: MB-02:A-087, MB-02:B-0308
- **abundance-distribution.7** The soil abundance-distribution shape is contested between exponential or inverse gamma (Zhou 2013) and lognormal (Shoemaker 2017; Grilli 2020); these use different fitting targets, so the conflict is only partial, and Haegeman 2013 argues the tail is not identifiable from sample data at all.
  conf: cont (note: "the conflict is only partial") · class: not stated · holds: soil shape rests on Zhou 2013 and Haegeman 2013 · src: zhouRandomSamplingProcess2013 (FT; model; single), shoemakerMacroecologicalTheoryMicrobial2017 (AB; model; single), grilliMacroecologicalLawsDescribe2020 (FT, partly re-opened; model; single), haegemanRobustEstimationMicrobial2013 (FT; model; repl) · trail: MB-01 §answers · from: MB-01:A-175, MB-01:A-176, MB-01:A-186
- **abundance-distribution.8** Abundance-distribution shapes reported separately for water and for host-associated 16S data were not found beyond Kembel 2012; the field-wide sources do not separate soil, water and host, and Grilli 2020's per-biome supplementary figures and Shoemaker 2017's full text were not read.
  conf: not stated · class: search (note: "no angle located such a breakdown") · holds: no angle located such a breakdown · src: grilliMacroecologicalLawsDescribe2020 (FT, partly re-opened), shoemakerMacroecologicalTheoryMicrobial2017 (AB) · trail: MB-01 §3.4, §Search record, §critic · from: MB-01:A-174, MB-01:A-305, MB-01:B-0290, MB-01:B-0293, MB-01:B-0451, MB-01:C-025, MB-01:C-114 · rating: "Weak for abundance-distribution shapes split by environment"
- **abundance-distribution.9** In bulk-soil amplicon data from the global datasets found, a small minority of taxa carries a large share of reads.
  conf: not stated · class: not stated · holds: amplicon reads, bulk soil; the two figures behind it must be kept apart (abundance-distribution.10, abundance-distribution.11) · src: delgadobaquerizoGlobalAtlasDominant2018 (FT), bickelChosenFewVariations2021 (FT) · trail: MB-02 §critic, §D3.1 · from: MB-02:C-039, MB-02:A-081, MB-02:A-090 · rating: "Moderate for the qualitative shape"
- **abundance-distribution.10** Across 237 soils (per-sample richness 774 to 2,869 phylotypes), 511 of 25,224 phylotypes (2%), defined as dominant jointly by abundance and ubiquity, accounted on average for 41% of 16S reads per sample: more than half in arid forests and only about 20% in tropical forests.
  conf: not stated · class: not stated · holds: global bulk soils, amplicon reads; a per-sample mean under a joint abundance-and-ubiquity definition · src: delgadobaquerizoGlobalAtlasDominant2018 (FT) · trail: MB-02 §D3.1, §critic · from: MB-02:A-081, MB-02:B-0291, MB-02:C-041
- **abundance-distribution.11** Across 844 soils (318 sites, 90-bp V4 ASVs), 0.4% of ASVs, classed common on the globally pooled rank-abundance distribution, held about 58% of pooled relative abundance, and the 99.6% classed rare held 42%.
  conf: not stated · class: not stated · holds: global bulk soils, amplicon reads; pooled global relative abundance; checked against full text by the critic · src: bickelChosenFewVariations2021 (FT) · trail: MB-02 §D3.1, §critic · from: MB-02:A-082, MB-02:B-0292, MB-02:C-042, MB-02:C-057
- **abundance-distribution.12** The dominant shares of Delgado-Baquerizo 2018 (about 41%) and Bickel and Or 2021 (about 58%) use different definitions and denominators and are not comparable figures.
  conf: not stated · class: not stated · holds: see abundance-distribution.10 and 11 · src: delgadobaquerizoGlobalAtlasDominant2018 (FT), bickelChosenFewVariations2021 (FT) · trail: MB-02 §D3.1, §critic · from: MB-02:A-094, MB-02:B-0297, MB-02:C-040
- **abundance-distribution.13** Drier soils had more even abundance distributions, and the ratio of rare to common richness declined with rainfall frequency (Pearson r = -0.41, n = 318).
  conf: not stated · class: not stated · holds: global bulk soils · src: bickelChosenFewVariations2021 (FT) · trail: MB-02 §D3.1 · from: MB-02:A-082, MB-02:B-0293, MB-02:B-0294
- **abundance-distribution.14** Across 146 soils, archaeal reads averaged 2% of 16S reads (0 to over 10%), and two Thaumarchaeota (then Crenarchaeota) phylotypes made up more than 70% of archaeal sequences.
  conf: single (critic: MB-02:C-044) · class: not stated · holds: one study, 2010-era 454 data, abstract only; archaeal figures rest on Bates 2011 alone · src: batesExaminingGlobalDistribution2011 (AB) · trail: MB-02 §D3.1, §critic · from: MB-02:A-083, MB-02:A-099, MB-02:B-0295, MB-02:B-0296, MB-02:C-044, MB-02:C-091
- **abundance-distribution.15** In DNA reassociation kinetics (whole-community DNA, neither reads nor cells), a power law fitted best, implying over a million distinct genomes in a pristine soil; metal pollution cut diversity by over 99.9%. It is the main contrary result on the shape of the distribution.
  conf: single (note: "removes the power-law side of the functional-form conflict") · class: not stated · holds: soil DNA reassociation; abstract only · src: gansComputationalImprovementsReveal2005 (AB) · trail: MB-02 §D3.1 · from: MB-02:A-085, MB-02:A-098, MB-02:B-0304..0306
- **abundance-distribution.16** Four Arizona soils were consistent with lognormal null models; small surveys reproduced richness but not composition, and documenting half the species would need 16,284 to 44,000 individuals.
  conf: not stated · class: model (note: "lognormal null models") · holds: clone libraries; abstract only · src: dunbarEmpiricalTheoreticalBacterial2002 (AB) · trail: MB-02 §D3.1 · from: MB-02:A-086, MB-02:B-0299..0301
- **abundance-distribution.17** Lognormal-based estimates gave 6,400 to 38,000 taxa per gram of soil.
  conf: not stated · class: model (note: "lognormal-based estimates gave 6,400 to 38,000 taxa per gram (modelled)") · holds: model estimates; abstract only · src: curtisEstimatingProkaryoticDiversity2002 (AB) · trail: MB-02 §D3.1 · from: MB-02:A-086, MB-02:B-0302
- **abundance-distribution.18** Soils may need hundreds of times current sampling to reach 90% of taxa, and diversity estimates depend on the distribution assumed.
  conf: not stated · class: not stated · holds: model; abstract only · src: quinceRationalExplorationMicrobial2008 (AB) · trail: MB-02 §D3.1 · from: MB-02:A-086, MB-02:B-0303
- **abundance-distribution.19** The functional form of the soil abundance distribution (lognormal versus power law) is contested and method-dependent: power law from reassociation kinetics against lognormal from clone-library models and large amplicon compilations, with most of the evidence abstract-only or modelled.
  conf: cont (critic: MB-02:C-045) · class: not stated · holds: soil; different measurement types · src: gansComputationalImprovementsReveal2005 (AB), curtisEstimatingProkaryoticDiversity2002 (AB), dunbarEmpiricalTheoreticalBacterial2002 (AB), shoemakerMacroecologicalTheoryMicrobial2017 (AB) · trail: MB-02 §answers, §critic · from: MB-02:A-091, MB-02:A-093, MB-02:A-149, MB-02:C-045 · rating: "Weak for the functional form"
- **abundance-distribution.20** Iowa corn and prairie soil metagenomes totalled about 300 Gbp, yet 80% of reads could not be assembled for low coverage, and 48% and 31% of contigs had coverage below 10x.
  conf: not stated · class: not stated · holds: two soil metagenomes · src: howeTacklingSoilDiversity2014 (FT) · trail: MB-02 §D3.1 · from: MB-02:A-088, MB-02:B-0312
- **abundance-distribution.21** Tropical soils are among the least-covered communities by Nonpareil estimates.
  conf: not stated · class: not stated · holds: metagenome coverage estimates; qualitative · src: rodriguezrEstimatingCoverageMetagenomic2014 (FT, qualitative) · trail: MB-02 §D3.1 · from: MB-02:A-088, MB-02:B-0313
- **abundance-distribution.22** 85% of the amplicon-defined dominant phylotypes were also dominant in 123 shotgun soil metagenomes.
  conf: single (note: "removes the only global amplicon-metagenome cross-check") · class: not stated · holds: global soils · src: delgadobaquerizoGlobalAtlasDominant2018 (FT) · trail: MB-02 §D3.1 · from: MB-02:A-088, MB-02:A-097, MB-02:B-0314
- **abundance-distribution.23** No soil taxon abundance distribution was found from metagenome coverage or from cell counts; the cell-based soil data found concern only total DNA per cell.
  conf: not stated · class: search (note: "No taxon abundance distribution from cell counts in soil was found") · holds: extended web searches on FISH, flow cytometry, spike-ins and absolute quantification; the route was narrow (taxon-specific FISH or CARD-FISH counts not searched beyond SAD queries; global genome-resolved soil metagenomes not examined) · src: none (the review's search) · trail: MB-02 §D3.1, §Search record, §critic · from: MB-02:A-088, MB-02:A-089, MB-02:A-092, MB-02:A-150, MB-02:B-0310, MB-02:B-0311, MB-02:B-0315, MB-02:C-046, MB-02:B-0369, MB-02:C-116, MB-02:C-117 · rating: "Absent for cell-count-based distributions in soil"

### rarity-terms: abundance, rarity, dominance and core terms
needs: abundance-distribution

- **rarity-terms.1** Three families of definition are in use and are not interchangeable: within-sample relative-abundance thresholds (0.1% the most common cutoff for rare), occupancy or prevalence across samples (core, mostly occurrence-only), and pooled, regional or global classes; usage is heterogeneous and often unstated.
  conf: not stated · class: not stated · holds: two systematic literature surveys plus reviews · src: pascoalDefinitionMicrobialRare2025 (FT), neuDefiningQuantifyingCore2021 (FT, first 100,000 characters) · trail: MB-02 §critic, §D2.1, §D2.2, §D2.3 · from: MB-02:A-060, MB-02:A-070, MB-02:A-144, MB-02:A-145, MB-02:C-028, MB-02:C-029, MB-02:C-030 · rating: "Strong on the fact of heterogeneity"
- **rarity-terms.2** The "rare biosphere" entered usage with deep-sea tag sequencing, which found thousands of low-abundance populations alongside a few dominants.
  conf: not stated · class: not stated · holds: deep sea; abstract only · src: soginMicrobialDiversityDeep2006 (AB) · trail: MB-02 §D2.1 · from: MB-02:B-0227
- **rarity-terms.3** Reviews describe a few dominant taxa and many rare ones without fixing a threshold.
  conf: not stated · class: not stated · holds: reviews, abstract only · src: pedrosalioRareBacterialBiosphere2012 (AB), lynchEcologyExplorationRare2015 (AB), pascoalMicrobialRareBiosphere2021 (AB) · trail: MB-02 §D2.1 · from: MB-02:B-0228
- **rarity-terms.4** Within-sample thresholds: rare is most often below 0.1% of reads per sample, sometimes below 0.01% or 0.001%, and abundant is usually above 1%.
  conf: not stated · class: not stated · holds: Lynch and Neufeld 2015, Galand 2009 and Dai 2016; Jia 2022, also cited by the review, uses a single rare/common cutoff and does not support "abundant above 1%" · src: lynchEcologyExplorationRare2015 (AB), galandEcologyRareMicrobial2009 (FT), daiIdentifyingKeyTaxonomic2016 (AB) · trail: MB-02 §D2.1, §critic · from: MB-02:A-061, MB-02:B-0229, MB-02:C-032, MB-02:C-065
- **rarity-terms.5** Galand et al. defined rare as below 0.01% and abundant as above 1% per sample, called the 0.01% cutoff "much more severe than the <0.1% criteria proposed earlier", and tied it to a singleton in the smallest library.
  conf: not stated · class: not stated · holds: Arctic Ocean · src: galandEcologyRareMicrobial2009 (FT) · trail: MB-02 §D2.1 · from: MB-02:B-0230, MB-02:B-0231, MB-02:B-0262
- **rarity-terms.6** Dai et al. defined rare as below 0.1% and abundant as above 1%, and combined these thresholds with behaviour across samples in six categories: always abundant, conditionally abundant, always rare, conditionally rare, moderate, and conditionally rare or abundant.
  conf: not stated · class: not stated · holds: abstract only · src: daiIdentifyingKeyTaxonomic2016 (AB) · trail: MB-02 §D2.1 · from: MB-02:A-063, MB-02:B-0232, MB-02:B-0233
- **rarity-terms.7** In a survey of 181 rare-biosphere articles from 2006 to 2024, about 37% gave no clear method; of those with a method, about 84% used relative-abundance thresholds, about 60% of those a single threshold, and about half used 0.1%, about 70% of them per sample rather than on the pooled dataset.
  conf: single (note: "rare-biosphere usage on Pascoal et al. 2025") · class: not stated · holds: one systematic survey; checked against full text by the critic · src: pascoalDefinitionMicrobialRare2025 (FT) · trail: MB-02 §D2.1 · from: MB-02:A-062, MB-02:A-079, MB-02:B-0234..0238, MB-02:C-057
- **rarity-terms.8** "Core" is the main occupancy term; it was first framed as the members shared across samples (the overlap of Venn diagrams), with later calls to add persistence and connectivity.
  conf: not stated · class: not stated · holds: abstract only · src: shadeBeyondVennDiagram2012 (AB) · trail: MB-02 §D2.2 · from: MB-02:B-0239, MB-02:B-0240
- **rarity-terms.9** In a survey of 224 core-microbiome studies, 75.4% defined the core by occurrence only, 4% by relative abundance only and 11.6% by both, with over 18% not stating a method; occurrence cutoffs ranged from 30% to 100% of samples (100% the most common) and abundance cutoffs in combined methods from 0.1% to 4.5%.
  conf: single (note: "core usage on Neu et al. 2021") · class: not stated · holds: one systematic survey, full text read to 100,000 characters · src: neuDefiningQuantifyingCore2021 (FT, first 100,000 characters) · trail: MB-02 §D2.2 · from: MB-02:A-064, MB-02:A-079, MB-02:B-0241..0247, MB-02:A-070
- **rarity-terms.10** Citing other work, Neu et al. report that only two OTUs were shared by all of 24 soil locations and none across 51 wastewater plants.
  conf: not stated · class: not stated · holds: SECONDARY via Neu 2021 · src: neuDefiningQuantifyingCore2021 (FT, first 100,000 characters) · trail: MB-02 §D2.2 · from: MB-02:B-0248
- **rarity-terms.11** Risely distinguishes five kinds of core (common, temporal, ecological, functional, host-adapted) and argues that no one definition captures all.
  conf: not stated · class: not stated · holds: abstract only · src: riselyApplyingCoreMicrobiome2020 (AB) · trail: MB-02 §D2.2 · from: MB-02:B-0249
- **rarity-terms.12** Conditionally rare taxa are defined by a bimodal abundance distribution over time (coefficient of bimodality) together with a maximum relative abundance above 1%; across 42 non-soil time series they made up 1.5 to 28% of membership.
  conf: not stated · class: not stated · holds: non-soil time series; full text read as excerpts · src: shadeConditionallyRareTaxa2014 (FT, excerpts) · trail: MB-02 §D2.2 · from: MB-02:A-063, MB-02:B-0250..0252
- **rarity-terms.13** A three-way split into permanently, transiently and conditionally rare taxa has been applied in soil.
  conf: not stated · class: not stated · holds: a salt-marsh soil chronosequence · src: jiaUnravellingInterplayEcological2022 (FT) · trail: MB-02 §D2.2 · from: MB-02:A-063, MB-02:B-0253, MB-02:B-0265
- **rarity-terms.14** In soil, "dominant" has been defined jointly: in the top 10% of phylotypes by share of 16S reads and present in more than half of 237 soils.
  conf: not stated · class: not stated · holds: 237 soils · src: delgadobaquerizoGlobalAtlasDominant2018 (FT) · trail: MB-02 §D2.3 · from: MB-02:A-065, MB-02:B-0254
- **rarity-terms.15** "Common" versus "rare" has also been set by a data-driven minimum cross-entropy threshold on the globally pooled rank-abundance distribution (about 0.019% of pooled relative abundance), with prevalence across samples then reported separately.
  conf: not stated · class: not stated · holds: 844 global soils; checked against full text by the critic · src: bickelChosenFewVariations2021 (FT) · trail: MB-02 §D2.3 · from: MB-02:A-065, MB-02:B-0255, MB-02:B-0256, MB-02:C-057, MB-02:B-0292
- **rarity-terms.16** Terms are used inconsistently: "dominant" sometimes means abundant within a sample and sometimes abundant and ubiquitous, and "common" means high pooled abundance in Bickel and Or 2021 but high occupancy elsewhere.
  conf: not stated · class: not stated · holds: soil and general microbial ecology · src: delgadobaquerizoGlobalAtlasDominant2018 (FT), bickelChosenFewVariations2021 (FT) · trail: MB-02 §answers · from: MB-02:A-074
- **rarity-terms.17** Reviews treat habitat specificity and geographic range as microbial rarity axes alongside local abundance.
  conf: not stated · class: not stated · holds: review · src: joussetWhereLessMay2017 (FT) · trail: MB-02 §D2.3 · from: MB-02:B-0257
- **rarity-terms.18** Rabinowitz classified rarity by geographic range, habitat specificity and local abundance; Jousset et al. state these concepts "can be easily transferred to microbial communities".
  conf: not stated · class: not stated · holds: general ecology; SECONDARY via Jousset 2017, original not obtained · src: rabinowitzSevenFormsRarity1981 (not obtained; SEC), joussetWhereLessMay2017 (FT) · trail: MB-02 §D2.4 · from: MB-02:A-066, MB-02:B-0258..0260
- **rarity-terms.19** In a 21-year estuarine fish record, persistent and abundant "core" species fitted a lognormal, while infrequent "occasional" species fitted a log series; Galand et al. report the same split for rare versus abundant Arctic Ocean prokaryotes (log series versus lognormal).
  conf: not stated · class: not stated · holds: estuarine fish (abstract only) and Arctic Ocean prokaryotes · src: magurranExplainingExcessRare2003 (AB), galandEcologyRareMicrobial2009 (FT) · trail: MB-02 §D2.4 · from: MB-02:A-066, MB-02:B-0261, MB-02:B-0262
- **rarity-terms.20** Rarer taxa better predicted soil community structure across 30 datasets (1,998 samples); the study does not report abundance-occupancy and is not used in the answers.
  conf: not stated · class: not stated · holds: soil; read at abstract level · src: ramirezDetectingMacroecologicalPatterns2017 (AB) · trail: MB-02 §Search record · from: MB-02:B-0374, MB-02:B-0375
- **rarity-terms.21** Proposed standards for defining rarity and core include unsupervised classification (ulrb), multivariate cutoff analysis (also recommended for rare-biosphere assembly work), abundance-occupancy ranking with a neutral-model fit to prioritise core members, and explicit reporting with an explicit spatial and temporal scale of the core, deep sequencing and no rarefying when quantifying the core.
  conf: not stated · class: not stated · holds: proposals; none shown to be adopted · src: pascoalDefinitionMicrobialRare2025 (FT), gobetMultivariateCutoffLevel2010 (AB), jiaCommunityAssemblyProcesses2018 (AB), shadeAbundanceoccupancyDistributionsPrioritize2019 (AB), neuDefiningQuantifyingCore2021 (FT, first 100,000 characters) · trail: MB-02 §D2.5 · from: MB-02:A-068, MB-02:B-0284..0288
- **rarity-terms.22** No evidence was found that any proposed standard for defining rarity or core has become a field standard.
  conf: not stated · class: search (note: "I found no evidence that any of these has become a field standard") · holds: the review's searches · src: none (the review's search) · trail: MB-02 §D2.5 · from: MB-02:A-069, MB-02:A-147, MB-02:B-0289
- **rarity-terms.23** No survey was found that tallies definitions specifically within soil studies, or separately for bulk soil and rhizosphere.
  conf: not stated · class: search (note: "No survey found that tallies definitions specifically within soil studies") · holds: the review's searches · src: none (the review's search) · trail: MB-02 §answers · from: MB-02:A-075

### threshold-sensitivity: whether classifications and conclusions hold across thresholds
needs: rarity-terms

- **threshold-sensitivity.1** Tests of threshold sensitivity point both ways and are each single-system: some report conclusions that hold across thresholds or definitions (Jia 2022, Galand 2009, Gobet 2010, Astudillo-García 2017), others classifications or conclusions that change (Pascoal 2025, Custer 2023, Salonen 2012); they are not strictly contradictory because they test different outputs (membership counts versus beta-diversity or assembly inferences).
  conf: single (critic: MB-02:C-036) · class: not stated · holds: soil, marine, coastal-sand, sponge, human-gut and Arabidopsis-root systems · src: jiaUnravellingInterplayEcological2022 (FT), galandEcologyRareMicrobial2009 (FT), gobetMultivariateCutoffLevel2010 (AB), astudillogarciaEvaluatingCoreMicrobiota2017 (AB), pascoalDefinitionMicrobialRare2025 (FT), custerComparativeAnalysisCore2023 (FT, first 100,000 characters), salonenAdultIntestinalCore2012 (AB) · trail: MB-02 §D2.5, §critic · from: MB-02:A-067, MB-02:A-071, MB-02:A-072, MB-02:A-073, MB-02:A-146, MB-02:C-036, MB-02:B-0264 · rating: "Moderate on threshold sensitivity"
- **threshold-sensitivity.2** In the Schiermonnikoog salt-marsh soil chronosequence (five stages over 110 years, amplicon ASVs), the rare fraction of reads was 61.6%, 45.7% and 28.4% at cutoffs of 0.2%, 0.1% and 0.05%.
  conf: single (note: "The only soil test of threshold sensitivity found is Jia et al. 2022") · class: not stated · holds: one soil chronosequence; checked against full text by the critic · src: jiaUnravellingInterplayEcological2022 (FT) · trail: MB-02 §D2.5 · from: MB-02:A-067, MB-02:A-080, MB-02:A-084, MB-02:B-0265, MB-02:B-0266, MB-02:C-057
- **threshold-sensitivity.3** As the cutoff tightened, permanently and transiently rare ASVs fell in proportion, conditionally rare ASVs rose, and the relative importance of selection rose; beta-diversity patterns and the main assembly inference (homogeneous selection for the rare biosphere, variable selection for the common) were reported as similar across cutoffs: classification changed while the qualitative conclusion held.
  conf: single (note: "The only soil test of threshold sensitivity found is Jia et al. 2022") · class: not stated · holds: one soil chronosequence · src: jiaUnravellingInterplayEcological2022 (FT) · trail: MB-02 §D2.5, §critic · from: MB-02:A-067, MB-02:B-0267..0269, MB-02:C-037
- **threshold-sensitivity.4** In Arctic Ocean data, the biogeography of rare taxa persisted at a 0.001% cutoff.
  conf: not stated · class: not stated · holds: Arctic Ocean · src: galandEcologyRareMicrobial2009 (FT) · trail: MB-02 §D2.5 · from: MB-02:A-067, MB-02:B-0270
- **threshold-sensitivity.5** In coastal sands, ecological patterns were maintained after removing up to 35 to 40% of rare sequences.
  conf: not stated · class: not stated · holds: coastal sands; abstract only · src: gobetMultivariateCutoffLevel2010 (AB) · trail: MB-02 §D2.5 · from: MB-02:A-067, MB-02:B-0271
- **threshold-sensitivity.6** In marine samples, the 0.1% per-sample rule gave more rare than abundant ASVs with V4V5 amplicons and the reverse with full-length 16S, and threshold-based classes behaved differently across OTUs, ASVs and metagenomic OTUs, while the unsupervised method gave the same pattern across these.
  conf: not stated · class: not stated · holds: marine samples; checked against full text by the critic · src: pascoalDefinitionMicrobialRare2025 (FT) · trail: MB-02 §D2.5 · from: MB-02:A-067, MB-02:B-0272..0274, MB-02:C-057
- **threshold-sensitivity.7** Four core methods, compared on human faecal (319 samples) and Arabidopsis root (288 samples) data, assigned 1.2% to 9.4% of taxa as core, nearly 10-fold apart; 165 to 176 taxa were agreed by all four, which is 13 to 16% of core assignments.
  conf: not stated · class: not stated · holds: two datasets, full text read to 100,000 characters; the review's "about 1% of taxa" agreed by all four is its own derivation, not a figure in the source · src: custerComparativeAnalysisCore2023 (FT, first 100,000 characters) · trail: MB-02 §D2.5, §critic · from: MB-02:A-067, MB-02:B-0275, MB-02:B-0276, MB-02:C-033, MB-02:C-057, MB-02:C-034
- **threshold-sensitivity.8** In Custer's human data, a temporal effect significant in the full dataset was reported as not significant in core-based analyses; Custer's text is internally inconsistent on whether core analyses gained or lost the temporal effect.
  conf: not stated · class: not stated · holds: one human faecal dataset · src: custerComparativeAnalysisCore2023 (FT, first 100,000 characters) · trail: MB-02 §D2.5, §critic · from: MB-02:A-067, MB-02:B-0278, MB-02:C-035
- **threshold-sensitivity.9** Occupancy-based core methods were most accurate in simulations.
  conf: single (critic: MB-02:C-092) · class: model (note: "Occupancy-based methods were most accurate in simulations") · holds: one simulation study · src: custerComparativeAnalysisCore2023 (FT, first 100,000 characters) · trail: MB-02 §D2.5, §critic · from: MB-02:A-068, MB-02:B-0279, MB-02:C-092
- **threshold-sensitivity.10** In Arabidopsis root data, core size varied 7-fold among methods.
  conf: not stated · class: not stated · holds: Arabidopsis root data · src: custerComparativeAnalysisCore2023 (FT, first 100,000 characters) · trail: MB-02 §D3.2 · from: MB-02:B-0333
- **threshold-sensitivity.11** In sponges, core definitions changed alpha and beta diversity in some cases but not conclusions on host specificity, environmental quality or networks; the authors call the approach "surprisingly robust".
  conf: not stated · class: not stated · holds: sponges; abstract only · src: astudillogarciaEvaluatingCoreMicrobiota2017 (AB) · trail: MB-02 §D2.5 · from: MB-02:A-067, MB-02:B-0280, MB-02:B-0281
- **threshold-sensitivity.12** In human gut, core size depended mostly on analysis depth and required prevalence.
  conf: not stated · class: not stated · holds: human gut; abstract only · src: salonenAdultIntestinalCore2012 (AB) · trail: MB-02 §D2.5 · from: MB-02:A-067, MB-02:B-0282
- **threshold-sensitivity.13** In Loess Plateau soils, two primer pairs gave different diversity responses to land use, so rare and abundant classes depend on the primer, not only the cutoff.
  conf: not stated · class: not stated · holds: one soil region; abstract only · src: zengIdentifyingBiogeographicPatterns2021 (AB) · trail: MB-02 §D2.5 · from: MB-02:B-0283
- **threshold-sensitivity.14** No study was found that compares threshold-based rarity classes between amplicon and metagenome data from the same soil samples, and copy-number-corrected thresholds were not found to have been tested.
  conf: not stated · class: search (note: "No study found that compares threshold-based rarity classes between amplicon and metagenome data") · holds: the ulrb comparison of amplicon and metagenome units used marine samples · src: none (the review's search) · trail: MB-02 §answers · from: MB-02:A-076, MB-02:A-077

### count-sampling: sampling from the amplified pool
needs: reads-per-sample, abundance-distribution

- **count-sampling.1** Technical replicates (the same soil DNA amplified with different barcodes) shared 17.2 ± 2.3% of OTUs between two replicates and 8.2 ± 2.3% among three, on 454.
  conf: single (marker) · class: meas (marker) · holds: 24 Oklahoma grassland soil communities, 454; the figures are in the abstract, so they are AB-derived, and MB-02 read the source as an abstract · src: zhouReproducibilityQuantitationAmplicon2011 (FT; meas; single) · trail: MB-01 §4.1, §critic, MB-02 §D3.3 · from: MB-01:I-0092, MB-01:A-208, MB-01:C-075, MB-02:A-108, MB-02:B-0336, MB-02:C-058, MB-01:C-031
- **count-sampling.2** Zhou 2011's discussion gives 13.1% and 5.9% for replicate OTU overlap, which differ from its abstract.
  conf: not stated · class: not stated · holds: the discussion values need the body, which the critic could not confirm · src: zhouReproducibilityQuantitationAmplicon2011 (FT per statistics and bioinformatics angles) · trail: MB-01 §4.1, §critic · from: MB-01:B-0294, MB-01:C-076
- **count-sampling.3** A Poisson random-sampling model of long-tailed abundance distributions predicted the low OTU overlaps among soil technical replicates, with no significant difference from the observed values.
  conf: single (marker) · class: model (marker) · holds: the same 24 Oklahoma grassland soils on 454 that Zhou 2011 reported · src: zhouRandomSamplingProcess2013 (FT; model; single) · trail: MB-01 §4.1 · from: MB-01:I-0093, MB-01:A-188, MB-01:B-0295, MB-01:C-031
- **count-sampling.4** About 60,900 sequences per replicate were predicted to be needed for 90% OTU overlap.
  conf: single (marker) · class: model (marker) · holds: 24 grassland soils; the predicted reads rest on Zhou 2013 · src: zhouRandomSamplingProcess2013 (FT; model; single) · trail: MB-01 §4.1 · from: MB-01:I-0093, MB-01:A-210, MB-01:A-229, MB-01:C-031
- **count-sampling.5** That Poisson or multinomial sampling explains replicate disagreement in taxa detected comes from one dataset (Zhou 2013 modelled the same 24 Oklahoma grassland soils, sequenced on 454, that Zhou 2011 reported; Wen 2017 is from the same laboratory), and Wen 2017's MiSeq replicates cut against pure sampling; that sampling alone explains replicate disagreement in taxa detected is weak and contested.
  conf: cont (critic: MB-01:C-036) · class: not stated · holds: one soil dataset and one laboratory; one dataset counted as several studies by the review · src: zhouRandomSamplingProcess2013 (FT; model; single), zhouReproducibilityQuantitationAmplicon2011 (FT; meas; single), wenEvaluationReproducibilityAmplicon2017 (FT; meas; repl) · trail: MB-01 §critic, §4.1 · from: MB-01:C-030, MB-01:C-031, MB-01:C-032, MB-01:C-033, MB-01:C-036, MB-01:C-135 · rating: "weak and contested"
- **count-sampling.6** In Wen 2017, unweighted OTU overlap among MiSeq soil replicates plateaued at 39% near 30,000 reads (with singletons) and reached only 43.9% at 160,000 reads, far below Zhou 2013's predicted 90% at about 60,900; Wen's authors attribute rare-OTU variation to random sampling plus sequencing artefacts and report that "biases other than random sampling" affect unweighted metrics more.
  conf: not stated · class: not stated · holds: one deeply sequenced soil sample, MiSeq; known to this note through the critic, the review cites Wen 2017 only as support for depth-dependent agreement · src: wenEvaluationReproducibilityAmplicon2017 (FT) · trail: MB-01 §critic · from: MB-01:C-034, MB-01:C-035, MB-01:C-120, MB-01:C-121, MB-01:B-0324, MB-01:B-0325, MB-01:C-033
- **count-sampling.7** For one caecal extract, the abundance at which the CV of relative abundance reached 30% fell with the square root of read depth, as Poisson noise would predict.
  conf: single (marker) · class: meas (marker) · holds: one caecal extract with four technical replicates · src: barlowQuantitativeSequencingFramework2020 (FT; meas; single) · trail: MB-01 §4.1, §critic · from: MB-01:I-0094, MB-01:A-189, MB-01:A-206, MB-01:C-037, MB-01:C-085
- **count-sampling.8** In RNA-seq, Illumina lane replicates fit a Poisson model, with about 0.5% of genes deviating; McMurdie and Holmes adopt this assumption for technical replicates, so it rests on RNA-seq, not on 16S technical replicates.
  conf: not stated · class: meas (marker) · holds: RNA-seq, INDIRECT · src: marioniRNAseqAssessmentTechnical2008 (FT; meas; INDIRECT), mcmurdieWasteNotWant2014 (FT) · trail: MB-01 §4.1 · from: MB-01:I-0095, MB-01:A-191, MB-01:B-0296
- **count-sampling.9** Sampling as the cause of replicate variation (Zhou 2013; Grilli 2020) conflicts with technical variance beyond counting (Silverman 2018; Dyrhovden 2021 at low load); the review notes that Zhou 2013 and Silverman 2018 differ in setting and measure (OTU overlap versus variance of relative abundance), a caution the critic says it did not apply to the sampling side.
  conf: cont (note: "Where the evidence conflicts") · class: not stated · holds: studies that differ in setting and measure · src: zhouRandomSamplingProcess2013 (FT; model; single), grilliMacroecologicalLawsDescribe2020 (FT), silvermanDynamicLinearModels2018 (FT; model; single), dyrhovdenManagingContaminationDiverse2021 (FT; meas; single) · trail: MB-01 §6. Where, §answers, §critic · from: MB-01:A-218, MB-01:B-0404, MB-01:C-122, MB-01:C-123

### overdispersion: overdispersed count models
needs: count-sampling

- **overdispersion.1** Human oral plaque counts rejected the multinomial in favour of the Dirichlet-multinomial, with overdispersion theta of 0.047 and 0.054.
  conf: repl (marker) · class: meas (marker) · holds: between biological samples · src: larosaHypothesisTestingPower2012 (FT; meas; repl) · trail: MB-01 §4.2 · from: MB-01:I-0096, MB-01:A-192
- **overdispersion.2** Every public dataset surveyed showed more variance than Poisson among biological replicates.
  conf: repl (marker) · class: meas (marker) · holds: between biological samples · src: mcmurdieWasteNotWant2014 (FT; meas; repl) · trail: MB-01 §4.2 · from: MB-01:I-0097, MB-01:A-192
- **overdispersion.3** Hierarchical Dirichlet-multinomial models detected shifts better than alternatives in simulation.
  conf: single (marker) · class: model (marker) · holds: simulation; abstract only · src: harrisonDirichletmultinomialModellingOutperforms2020 (AB; model; single) · trail: MB-01 §4.2 · from: MB-01:I-0098
- **overdispersion.4** Beta-binomial and logistic-normal network models relax the multinomial further, by their makers' account.
  conf: not stated · class: assert (note: "makers' claims") · holds: makers' claims, abstract only · src: martinModelingMicrobialAbundances2020 (AB; makers' claims), willisEstimatingDiversityNetworked2022 (AB; makers' claims) · trail: MB-01 §4.2 · from: MB-01:B-0298
- **overdispersion.5** Dirichlet-multinomial overdispersion has been shown only between biological samples, not among technical replicates: no study fitting overdispersion to 16S technical replicates was found.
  conf: not stated · class: search (note: "No study fitting overdispersion to 16S technical replicates was found") · holds: statistics angle; replicate-at-depth studies are confined to one soil laboratory and one mouse caecum · src: none (the review's search) · trail: MB-01 §4.2, §critic · from: MB-01:A-217, MB-01:B-0301, MB-01:B-0448, MB-01:C-039, MB-01:C-115

### technical-variation: processes other than sampling
needs: count-sampling, pcr, primers, run-batch

- **technical-variation.1** In four artificial-gut vessels sampled hourly with 20 technical replicates per vessel, 76% of observed variation was attributed to technical sources beyond sequence counting.
  conf: single (marker) · class: model (marker) · holds: artificial guts; the 76% figure rests on Silverman 2018 alone · src: silvermanDynamicLinearModels2018 (FT; model; single) · trail: MB-01 §4.3 · from: MB-01:I-0099, MB-01:A-195, MB-01:A-226
- **technical-variation.2** Replicates split before PCR differed strongly, while replicates split after PCR were nearly identical; in negative extraction controls, most species appeared in only one of five PCR replicates (mean Jaccard distance 0.80, range 0.65 to 0.87).
  conf: single (marker) · class: meas (marker) · holds: clinical samples at low load and negative extraction controls; the before-versus-after split rests on Dyrhovden 2021; the review gave the figure as "mean Jaccard 0.80" without "distance" · src: dyrhovdenManagingContaminationDiverse2021 (FT; meas; single) · trail: MB-01 §4.3, §critic · from: MB-01:I-0100, MB-01:A-197, MB-01:A-228, MB-01:B-0303, MB-01:C-059, MB-01:C-082, MB-01:B-0304
- **technical-variation.3** At 1:10^5 dilution of a staggered mock, 12 species appeared in only 2 of 4 PCR replicates.
  conf: not stated · class: not stated · holds: one staggered mock · src: dyrhovdenManagingContaminationDiverse2021 (FT) · trail: MB-01 §4.3 · from: MB-01:B-0305
- **technical-variation.4** At low input, library preparation reached its Poisson loading limit, the two rarest taxa dropped out, and contaminants appeared below about 10^4 copies.
  conf: not stated · class: not stated · holds: Barlow 2020 · src: barlowQuantitativeSequencingFramework2020 (FT) · trail: MB-01 §4.3 · from: MB-01:A-202, MB-01:B-0306
- **technical-variation.5** In low-input pools of unique synthetic barcodes, random per-molecule amplification in early cycles was the main source of skew; late-cycle polymerase errors stayed at low copy number, template switching was rare and GC bias minor.
  conf: single (marker) · class: meas (marker) · holds: synthetic barcode pools, non-16S, INDIRECT · src: kebschullSourcesPCRinducedDistortions2015 (FT; meas; single; INDIRECT, non-16S) · trail: MB-01 §2.4, §4.3 · from: MB-01:I-0034, MB-01:A-063, MB-01:A-196, MB-01:B-0183, MB-01:B-0302, MB-01:B-0307
- **technical-variation.6** Primer mismatch and low efficiency remove or suppress specific taxa (non-random dropout).
  conf: not stated · class: not stated · holds: Parada 2016 and Walters 2016 · src: paradaEveryBaseMatters2016 (AB), waltersImprovedBacterial16S2016 (FT) · trail: MB-01 §4.3 · from: MB-01:A-200, MB-01:B-0316
- **technical-variation.7** In eDNA simulations with a low-efficiency primer set, a median of 88 of 1,000 taxa were detected after 20 cycles.
  conf: not stated · class: model (note: "Kelly 2019, indirect, modelled") · holds: eukaryotic eDNA simulations, INDIRECT · src: kellyUnderstandingPCRProcesses2019 (FT; model; INDIRECT) · trail: MB-01 §4.3 · from: MB-01:A-201, MB-01:B-0317, MB-01:I-0078
- **technical-variation.8** Technical variance beyond counting (76% of variation at hourly sampling in artificial guts), early stochastic amplification at low load and whole-run taxon loss are each measured in single studies.
  conf: single (critic: MB-01:C-038) · class: not stated · holds: Silverman 2018, Dyrhovden 2021, Yeh 2018 · src: silvermanDynamicLinearModels2018 (FT; model; single), dyrhovdenManagingContaminationDiverse2021 (FT; meas; single), yehTaxonDisappearanceMicrobiome2018 (FT; meas; single) · trail: MB-01 §critic, §answers · from: MB-01:C-038, MB-01:A-215, MB-01:A-308 · rating: "Weak on how much non-sampling technical variance there is"
- **technical-variation.9** Pooled versus single PCR showed no effect at moderate to high input (Kennedy 2014; Marotz 2019; Smith and Peay 2014), but replicates split before PCR disagreed strongly at low load (Dyrhovden 2021).
  conf: not stated · class: not stated · holds: no single study tested both conditions · src: kennedyEvaluatingBiasIlluminabased2014 (AB; meas; single), marotzTriplicatePCRReactions2019 (AB; meas; repl), smithSequenceDepthNot2014 (FT; meas; INDIRECT), dyrhovdenManagingContaminationDiverse2021 (FT; meas; single) · trail: MB-01 §answers · from: MB-01:A-220
- **technical-variation.10** That the difference in load explains the pooled-versus-single PCR contrast is the reviewer's own reconciliation, untested by any single study.
  conf: not stated · class: reading (critic: MB-01:C-140) · holds: no study tested both conditions · src: none (the reviewer's reconciliation) · trail: MB-01 §critic, §answers · from: MB-01:A-221, MB-01:C-139, MB-01:C-140, MB-01:C-141

### zeros: zeros in count tables
needs: count-sampling

- **zeros.1** In simulation, simple count models sufficed across four zero-generating processes, and zero inflation was warranted only under narrow conditions.
  conf: single (marker) · class: model (marker) · holds: simulation; abstract only · src: silvermanNaughtAllZeros2020 (AB; model; single) · trail: MB-01 §4.3 · from: MB-01:I-0102, MB-01:A-213
- **zeros.2** Pseudocounts made tests conservative.
  conf: single (marker) · class: model (marker) · holds: simulation; abstract only · src: kaulAnalysisMicrobiomeData2017 (AB; model; single) · trail: MB-01 §4.3 · from: MB-01:I-0103
- **zeros.3** Schloss asserts that a microbiome zero more likely means true absence, which conflicts with Grilli 2020's sampling interpretation of absences.
  conf: cont (note: "which conflicts with Grilli 2020's sampling interpretation") · class: assert (marker) · holds: an assertion against a model-based interpretation · src: schlossWasteNotWant2024 (FT; assert), grilliMacroecologicalLawsDescribe2020 (FT) · trail: MB-01 §4.3, §6. Where · from: MB-01:I-0104, MB-01:A-219, MB-01:B-0409

### replicate-agreement: technical replicates at different read depths
needs: count-sampling

- **replicate-agreement.1** Technical variation was under 5% for most taxa, while error from bias exceeded 85% in some samples.
  conf: cont (marker) · class: meas (marker) · holds: 7-taxon vaginal cell mixtures · src: brooksTruthMetagenomicsQuantifying2015 (FT; meas; cont) · trail: MB-01 §4.4, §2.2 · from: MB-01:I-0008, MB-01:A-205, MB-01:B-0149, MB-01:B-0319, MB-01:I-0007
- **replicate-agreement.2** In one soil sample, abundance-weighted OTU overlap among technical replicates rose from 56.7% at 2,000 reads to 95.3% at 160,000.
  conf: not stated · class: not stated · holds: one soil sample; checked against full text by the critic · src: wenEvaluationReproducibilityAmplicon2017 (FT) · trail: MB-01 §4.4 · from: MB-01:A-207, MB-01:B-0320, MB-01:C-054
- **replicate-agreement.3** Bray-Curtis dissimilarity among technical replicates was 0.269, against 0.374 among treatment replicates.
  conf: repl (marker) · class: meas (marker) · holds: soil, MiSeq · src: wenEvaluationReproducibilityAmplicon2017 (FT; meas; repl) · trail: MB-01 §4.4 · from: MB-01:I-0105, MB-01:B-0324
- **replicate-agreement.4** Greater depth improved replicate agreement in beta diversity for some mocks only.
  conf: not stated · class: not stated · holds: some mocks only · src: pintoPCRBiasesDistort2012 (FT) · trail: MB-01 §4.4 · from: MB-01:B-0321
- **replicate-agreement.5** A preprint reports replicate Jaccard distances of typically about 0.15, and up to 0.71 across runs.
  conf: not stated · class: not stated · holds: preprint abstract · src: edgarUNBIASAttemptCorrect2017 (AB; PREPRINT) · trail: MB-01 §4.4 · from: MB-01:B-0322, MB-01:A-225
- **replicate-agreement.6** On MiSeq, 18 soil extracts shared 33.4% of OTUs between two replicates and 20.2% among three; in one deeply sequenced sample, presence/absence overlap rose from 20.7% at 2,000 reads to 43.9% at 160,000, plateauing near 30,000.
  conf: single (note: "Depth curves for replicate overlap on MiSeq rest on Wen 2017") · class: not stated · holds: soil, MiSeq; the plateau was at 39% · src: wenEvaluationReproducibilityAmplicon2017 (FT) · trail: MB-01 §4.4, §critic · from: MB-01:A-209, MB-01:A-227, MB-01:B-0324, MB-01:B-0325, MB-01:C-034
- **replicate-agreement.7** Overlap among technical replicates was lower when they were sequenced in separate runs (a run effect).
  conf: not stated · class: not stated · holds: soil, MiSeq; known to this note through the critic · src: wenEvaluationReproducibilityAmplicon2017 (FT) · trail: MB-01 §critic · from: MB-01:C-035, MB-01:C-121, MB-01:B-0324
- **replicate-agreement.8** In fungal ITS, OTUs averaging more than 10 reads were detected in nearly all replicates, and replicate dissimilarity (pseudo-beta-diversity) fell markedly with depth.
  conf: not stated · class: not stated · holds: fungal ITS, INDIRECT · src: smithSequenceDepthNot2014 (FT; INDIRECT, ITS) · trail: MB-01 §4.4 · from: MB-01:A-190, MB-01:A-211, MB-01:B-0326
- **replicate-agreement.9** Replicate variation affected beta diversity more than alpha diversity.
  conf: not stated · class: not stated · holds: soil, 454 · src: zhouReproducibilityQuantitationAmplicon2011 (FT) · trail: MB-01 §4.4 · from: MB-01:B-0327, MB-01:C-031
- **replicate-agreement.10** Alpha diversity did not differ among technical replicates.
  conf: not stated · class: not stated · holds: soil, MiSeq · src: wenEvaluationReproducibilityAmplicon2017 (FT) · trail: MB-01 §4.4 · from: MB-01:B-0328, MB-01:B-0324
- **replicate-agreement.11** Replicate agreement depends on read depth.
  conf: not stated · class: not stated · holds: Wen 2017, Zhou 2013, Smith and Peay 2014 and Barlow 2020; Wen 2017's own data also show a plateau below the predicted overlap (count-sampling.6) · src: wenEvaluationReproducibilityAmplicon2017 (FT), zhouRandomSamplingProcess2013 (FT), smithSequenceDepthNot2014 (FT; INDIRECT), barlowQuantitativeSequencingFramework2020 (FT) · trail: MB-01 §answers · from: MB-01:A-216 · rating: "Moderate for the depth dependence of replicate agreement"
- **replicate-agreement.12** No 16S study was found that tests whether technical-replicate variance of relative abundance exceeds multinomial expectation across controlled read depths, and no replicate-at-depth studies in water or host samples other than gut.
  conf: not stated · class: search (note: "Not found: a 16S study testing whether technical-replicate variance") · holds: statistics angle, Europe PMC and web search; soil dominates · src: none (the review's search) · trail: MB-01 §answers, §critic · from: MB-01:A-222, MB-01:C-040

### alpha-diversity: richness and other alpha-diversity measures
needs: reads-per-sample

- **alpha-diversity.1** Chao1, ACE, CatchAll, Shannon and Simpson all varied with library size in pyrosequencing data; the depth dependence of raw and estimator richness is replicated.
  conf: repl (marker) · class: meas (marker) · holds: pyrosequencing data; abstract only; replicated with Schloss 2024b and Haegeman 2013 · src: gihringMassivelyParallelRRNA2012 (AB; meas; repl) · trail: MB-01 §5.2 · from: MB-01:I-0112, MB-01:A-274
- **alpha-diversity.2** In null models built from 12 V4 datasets, observed richness, Chao1, ACE, breakaway and SRS-normalised richness all correlated with depth; Shannon was less depth-sensitive and inverse Simpson was not depth-sensitive.
  conf: cont (marker) · class: model (marker) · holds: null models with multinomial-type sampling only · src: schlossRarefactionCurrentlyBest2024 (FT, re-opened; model; cont) · trail: MB-01 §5.2 · from: MB-01:I-0113, MB-01:A-237, MB-01:A-242, MB-01:B-0334, MB-01:B-0340
- **alpha-diversity.3** Breakaway intervals were mostly too wide to be useful.
  conf: not stated · class: not stated · holds: null models from 12 V4 datasets · src: schlossRarefactionCurrentlyBest2024 (FT, re-opened) · trail: MB-01 §5.2 · from: MB-01:A-237, MB-01:B-0347, MB-01:I-0113
- **alpha-diversity.4** Sample data carry no information on the rare tail: Chao's estimator ranked in silico communities wrongly (a community with 20 times fewer species was estimated to have 10 times more), and bounds for Hill numbers of order 2 and above nearly coincide; the authors recommend Shannon and Simpson over richness.
  conf: repl (marker) · class: model (marker) · holds: in silico communities and one Brazilian soil; the full text was not openly retrievable · src: haegemanRobustEstimationMicrobial2013 (FT; model; repl) · trail: MB-01 §5.2 · from: MB-01:I-0115, MB-01:A-238, MB-01:A-242, MB-01:B-0349..0351, MB-01:C-028
- **alpha-diversity.5** Chao1 and ACE are invalid on ASV tables from algorithms that drop singletons, as DADA2 does by default.
  conf: single (marker) · class: assert (marker) · holds: an assertion · src: dengNonparametricRichnessEstimators2024 (FT; assert; single) · trail: MB-01 §5.2 · from: MB-01:I-0116, MB-01:A-240
- **alpha-diversity.6** Spurious OTUs severely inflated Chao1, and removing them severely underestimated Chao1 in uneven communities; abundance-weighted metrics were little affected.
  conf: not stated · class: not stated · holds: uneven communities · src: pintoPCRBiasesDistort2012 (FT) · trail: MB-01 §5.2, §2.6 · from: MB-01:A-079, MB-01:A-080, MB-01:A-241, MB-01:B-0126, MB-01:B-0352
- **alpha-diversity.7** An abundance filter makes ACE and Chao1 inapplicable.
  conf: not stated · class: not stated · holds: mocks · src: bokulichQualityfilteringVastlyImproves2013 (FT) · trail: MB-01 §5.2 · from: MB-01:B-0353, MB-01:B-0207
- **alpha-diversity.8** A singleton-replacement estimator for error-inflated data has been proposed.
  conf: single (marker) · class: model (marker) · holds: abstract only · src: chiuEstimatingComparingMicrobial2016 (AB; model; single) · trail: MB-01 §5.2 · from: MB-01:I-0117, MB-01:A-241
- **alpha-diversity.9** Pyrosequencing errors inflated rare-tail richness.
  conf: not stated · class: not stated · holds: 454; abstract only · src: kuninWrinklesRareBiosphere2010 (AB) · trail: MB-02 §D3.3 · from: MB-02:A-110, MB-02:B-0338
- **alpha-diversity.10** Better OTU clustering cut richness by 30 to 60% but did not remove the long tail.
  conf: not stated · class: not stated · holds: abstract only · src: huseIroningOutWrinkles2010 (AB) · trail: MB-02 §D3.3 · from: MB-02:A-110, MB-02:B-0339
- **alpha-diversity.11** Multiplicative bias can make an uneven sample look more even, biasing Shannon and inverse Simpson.
  conf: not stated · class: model (note: "McLaren 2019, modelled") · holds: model · src: mclarenConsistentCorrectableBias2019 (FT, re-opened) · trail: MB-01 §5.2 · from: MB-01:A-252, MB-01:B-0354
- **alpha-diversity.12** PCR-bias calibration improved Shannon in 7 of 10 mocks.
  conf: not stated · class: not stated · holds: gut-isolate mocks · src: silvermanMeasuringMitigatingPCR2021 (FT) · trail: MB-01 §5.2 · from: MB-01:B-0355, MB-01:I-0027
- **alpha-diversity.13** In simulated faecal communities with load varying from 1.9 x 10^9 to 10^13 cells per gram, all 13 transformations reproduced Shannon and Simpson, but richness was recovered reliably only by quantitative profiling in a bloom scenario.
  conf: single (marker) · class: model (marker) · holds: simulated faeces without taxon-specific bias · src: llorensricoBenchmarkingMicrobiomeTransformations2021 (FT; model; single) · trail: MB-01 §5.2 · from: MB-01:I-0118, MB-01:A-243, MB-01:B-0356, MB-01:C-051
- **alpha-diversity.14** In freshwater and sediment 454 data, 5,000 sequences captured Shannon trends and over 80% of Chao1 trends.
  conf: single (marker) · class: meas (marker) · holds: freshwater and sediment, 454; abstract only · src: lundinWhichSequencingDepth2012 (AB; meas; single) · trail: MB-01 §5.2 · from: MB-01:I-0119
- **alpha-diversity.15** Hill-number extrapolation is reliable only to about 2 to 3 times the reference sample size for richness.
  conf: not stated · class: model (marker) · holds: ecology, INDIRECT · src: chaoRarefactionExtrapolationHill2014 (FT; model; INDIRECT) · trail: MB-01 §5.1 · from: MB-01:I-0108, MB-01:A-239

### beta-diversity: beta diversity
needs: reads-per-sample

- **beta-diversity.1** Library-size normalisation had very little effect on beta-diversity separation compared with the choice of distance metric.
  conf: single (marker) · class: meas (marker) · holds: abstract only · src: thorsenLargescaleBenchmarkingReveals2016 (AB; meas; single) · trail: MB-01 §5.3, §7. Bounds · from: MB-01:I-0124, MB-01:A-250, MB-01:B-0420
- **beta-diversity.2** 1,000 denoised sequences explained 90% of the Bray-Curtis trends seen at 15,000 to 20,000.
  conf: not stated · class: not stated · holds: freshwater and sediment, 454; abstract only · src: lundinWhichSequencingDepth2012 (AB) · trail: MB-01 §5.3 · from: MB-01:B-0363, MB-01:I-0119
- **beta-diversity.3** Bray-Curtis was usually the most powerful metric, and metric choice changes power.
  conf: single (marker) · class: meas (marker) · holds: abstract only · src: kersPowerMicrobiomeStudies2022 (AB; meas; single) · trail: MB-01 §5.3 · from: MB-01:I-0126
- **beta-diversity.4** Which normalisation removes depth effects on beta diversity is contested and simulation-based.
  conf: cont (note: "Beta: contested, simulation-based") · class: model (note: "Beta: contested, simulation-based") · holds: see rarefying.7 to rarefying.11 and proportions.1 to 2 · src: none (the reviewer's synthesis) · trail: MB-01 §answers · from: MB-01:A-276

### differential-abundance: tests of which taxa differ in abundance
needs: reads-per-sample

- **differential-abundance.1** Fourteen differential-abundance methods on 38 datasets gave 0.8% to 40.5% significant ASVs on the same data (unfiltered means).
  conf: single (marker) · class: meas (marker) · holds: 38 real datasets · src: nearingMicrobiomeDifferentialAbundance2022 (FT; meas; single) · trail: MB-01 §5.4 · from: MB-01:I-0129, MB-01:A-264, MB-01:B-0371
- **differential-abundance.2** ALDEx2 and ANCOM-II were the most consistent methods across 38 datasets.
  conf: single (marker) · class: meas (marker) · holds: 38 real datasets · src: nearingMicrobiomeDifferentialAbundance2022 (FT; meas; single) · trail: MB-01 §5.4 · from: MB-01:I-0129, MB-01:A-259
- **differential-abundance.3** edgeR and LEfSe produced many false positives on random splits.
  conf: single (marker) · class: meas (marker) · holds: 38 real datasets · src: nearingMicrobiomeDifferentialAbundance2022 (FT; meas; single) · trail: MB-01 §5.4 · from: MB-01:I-0129, MB-01:B-0371
- **differential-abundance.4** Excess false discoveries were widespread across differential-abundance methods.
  conf: repl (marker) · class: model (marker) · holds: abstract only · src: hawinkelBrokenPromiseMicrobiome2019 (AB; model; repl) · trail: MB-01 §5.4 · from: MB-01:I-0130, MB-01:A-265
- **differential-abundance.5** Methods with the highest false-positive rates had the most power.
  conf: not stated · class: not stated · holds: abstract only · src: thorsenLargescaleBenchmarkingReveals2016 (AB) · trail: MB-01 §5.4 · from: MB-01:B-0372
- **differential-abundance.6** Microbiome-specific methods did not beat RNA-seq methods.
  conf: single (marker) · class: meas (marker) · holds: abstract only · src: calgaroAssessmentStatisticalMethods2020 (AB; meas; single) · trail: MB-01 §5.4 · from: MB-01:I-0131
- **differential-abundance.7** In implanted-signal benchmarks, only linear models, Wilcoxon, t-test, limma and fastANCOM controlled FDR at relatively high sensitivity.
  conf: repl (marker) · class: model (marker) · holds: implanted-signal benchmark · src: wirbelRealisticBenchmarkDifferential2024 (FT; model; repl) · trail: MB-01 §5.4 · from: MB-01:I-0132, MB-01:A-263
- **differential-abundance.8** fitZig reached an observed FDR of 80%.
  conf: repl (marker) · class: model (marker) · holds: implanted-signal benchmark · src: wirbelRealisticBenchmarkDifferential2024 (FT; model; repl) · trail: MB-01 §5.4, §7. Bounds · from: MB-01:I-0132, MB-01:B-0431
- **differential-abundance.9** ANCOM and ANCOM-BC controlled FDR only at 200 or more samples per group.
  conf: repl (marker) · class: model (marker) · holds: implanted-signal benchmark · src: wirbelRealisticBenchmarkDifferential2024 (FT; model; repl) · trail: MB-01 §5.4, §7. Bounds · from: MB-01:I-0132, MB-01:A-260, MB-01:B-0430
- **differential-abundance.10** Elementary methods on relative abundances were the most replicable across 53 studies; elementary tests such as Wilcoxon and linear models were among the most replicable.
  conf: single (marker) · class: meas (marker) · holds: abstract only · src: peltoElementaryMethodsProvide2025 (AB; meas; single) · trail: MB-01 §5.4 · from: MB-01:I-0133, MB-01:A-263
- **differential-abundance.11** No differential-abundance method was "simultaneously robust, powerful, and flexible".
  conf: repl (marker) · class: model (marker) · holds: simulation benchmark · src: yangComprehensiveEvaluationMicrobial2022 (FT; model; repl) · trail: MB-01 §5.4 · from: MB-01:I-0128
- **differential-abundance.12** ANCOM-BC showed type I inflation in some settings.
  conf: not stated · class: not stated · holds: some settings · src: yangComprehensiveEvaluationMicrobial2022 (FT) · trail: MB-01 §answers · from: MB-01:A-260
- **differential-abundance.13** Differential-abundance methods disagree widely, and FDR failures are common.
  conf: not stated · class: not stated · holds: Nearing 2022, Hawinkel 2019, Yang and Chen 2022, Wirbel 2024 · src: nearingMicrobiomeDifferentialAbundance2022 (FT), hawinkelBrokenPromiseMicrobiome2019 (AB), yangComprehensiveEvaluationMicrobial2022 (FT), wirbelRealisticBenchmarkDifferential2024 (FT) · trail: MB-01 §answers, §8. Answers · from: MB-01:A-277, MB-01:A-311 · rating: "robust in showing large disagreement between methods and frequent FDR failures"
- **differential-abundance.14** Which differential-abundance method is best is contested.
  conf: cont (note: "Which method is best is contested") · class: not stated · holds: see differential-abundance.1 to 12 · src: none (the reviewer's synthesis) · trail: MB-01 §answers · from: MB-01:A-278, MB-01:C-041

### rarefying: rarefying and rarefaction
needs: alpha-diversity, beta-diversity, differential-abundance

- **rarefying.1** Rarefaction comes from ecology, traced to Sanders 1968, Hurlbert 1971 and Simberloff 1972.
  conf: not stated · class: not stated · holds: SECONDARY via Chao and Jost 2012 · src: sandersMarineBenthicDiversity1968 (SEC), hurlbertNonconceptSpeciesDiversity1971 (SEC), simberloff1972 (SEC), chaoCoveragebasedRarefactionExtrapolation2012 (FT) · trail: MB-01 §5.1 · from: MB-01:B-0329
- **rarefying.2** Gotelli and Colwell argue that individual-based rarefaction allows meaningful comparison and that asymptotic estimators give lower bounds.
  conf: not stated · class: assert (marker) · holds: ecology, INDIRECT; a review, abstract only · src: gotelliQuantifyingBiodiversityProcedures2001 (AB; assert; INDIRECT) · trail: MB-01 §5.1 · from: MB-01:I-0106
- **rarefying.3** Schloss distinguishes "rarefying" (one random subsample) from "rarefaction" (the mean over many subsamples).
  conf: not stated · class: not stated · holds: terminology · src: schlossRarefactionCurrentlyBest2024 (FT, re-opened) · trail: MB-01 §5.2 · from: MB-01:B-0335
- **rarefying.4** In null models built from 12 V4 datasets, only rarefaction removed the correlation between richness and depth; size-based iNEXT nearly did, except for the small, evenly sequenced marine and soil sets.
  conf: single (note: "rests mostly on simulations from one author") · class: model (note: "under multinomial-type null models built from 12 V4 datasets") · holds: null models with multinomial-type sampling only; the author's conclusion · src: schlossRarefactionCurrentlyBest2024 (FT, re-opened) · trail: MB-01 §5.2 · from: MB-01:A-231, MB-01:A-232, MB-01:A-275, MB-01:A-290, MB-01:A-310, MB-01:B-0336, MB-01:B-0337
- **rarefying.5** When depth was confounded with group, only rarefaction and size-based iNEXT held a 5% false-positive rate for richness, and rarefaction gave the highest power.
  conf: single (note: "rests mostly on simulations from one author") · class: model (note: "under multinomial-type null models built from 12 V4 datasets") · holds: null models · src: schlossRarefactionCurrentlyBest2024 (FT, re-opened) · trail: MB-01 §5.2 · from: MB-01:A-231, MB-01:B-0338
- **rarefying.6** The null model reassigns sequences at random, so samples differ only through multinomial-type sampling: taxon-specific bias, technical variation beyond counting and differences in load are absent from its simulated truth.
  conf: not stated · class: reading (note: "statistics angle's reading") · holds: Schloss 2024b design · src: schlossRarefactionCurrentlyBest2024 (FT, re-opened) · trail: MB-01 §5.2 · from: MB-01:B-0339, MB-01:B-0340, MB-01:B-0341
- **rarefying.7** In the same null models, Jaccard and Bray-Curtis computed from raw counts, relative abundances, CSS or SRS, Aitchison distances (four zero-handling variants) and DESeq2 VST Euclidean distances all correlated with depth differences; only rarefaction removed the correlation and held 5% false positives in PERMANOVA under confounding.
  conf: single (note: "rests on Schloss 2024b") · class: model (note: "under multinomial-type null models built from 12 V4 datasets") · holds: null models; supported in part by Weiss 2017 for beta and differential abundance · src: schlossRarefactionCurrentlyBest2024 (FT, re-opened) · trail: MB-01 §5.3 · from: MB-01:A-245, MB-01:A-251, MB-01:A-271, MB-01:A-290, MB-01:B-0357, MB-01:B-0358
- **rarefying.8** Rarefying clustered samples better for presence/absence metrics, and other normalisations were vulnerable below about 1,000 reads per sample.
  conf: repl (marker) · class: model (marker) · holds: simulations · src: weissNormalizationMicrobialDifferential2017 (FT; model; repl) · trail: MB-01 §5.3 · from: MB-01:I-0120
- **rarefying.9** In simulations from Global Patterns, rarefying to the 15th percentile and dropping samples below it reduced clustering accuracy.
  conf: cont (marker) · class: model (marker) · holds: simulations · src: mcmurdieWasteNotWant2014 (FT; model; cont) · trail: MB-01 §5.3 · from: MB-01:I-0121, MB-01:A-246
- **rarefying.10** Schloss identified 11 design choices that disadvantaged rarefying in McMurdie and Holmes 2014; notably, low-depth samples were removed only in the rarefied arm.
  conf: single (marker) · class: model (marker) · holds: re-analysis of a simulation design · src: schlossWasteNotWant2024 (FT; model; single) · trail: MB-01 §5.3 · from: MB-01:I-0122, MB-01:A-246, MB-01:B-0359
- **rarefying.11** In real river data, rarefying barely changed Bray-Curtis or Jaccard (r > 0.9) and did not change weighted UniFrac.
  conf: not stated · class: not stated · holds: real freshwater data · src: chiarelloRankingBiasesChoice2022 (FT) · trail: MB-01 §5.3, §7. Bounds · from: MB-01:A-247, MB-01:B-0362, MB-01:B-0419
- **rarefying.12** Repeated rarefying shows that the random variation rarefying introduces grows as rarefied depth shrinks.
  conf: single (marker) · class: meas (marker) · holds: repeated rarefying of real data · src: cameronEnhancingDiversityAnalysis2021 (FT; meas; single) · trail: MB-01 §5.3 · from: MB-01:I-0125, MB-01:A-248
- **rarefying.13** Rarefied counts and proportions gave high false-positive rates in differential-abundance tests, while DESeq2 and edgeR were near zero.
  conf: not stated · class: not stated · holds: differential-abundance tests · src: mcmurdieWasteNotWant2014 (FT) · trail: MB-01 §5.4 · from: MB-01:A-254, MB-01:B-0364, MB-01:B-0365
- **rarefying.14** Rarefying did not raise FDR for most methods, and lowered it at about 10x group differences in library size, at a cost in sensitivity.
  conf: not stated · class: not stated · holds: most methods · src: weissNormalizationMicrobialDifferential2017 (FT) · trail: MB-01 §5.4 · from: MB-01:A-255, MB-01:B-0366, MB-01:B-0367
- **rarefying.15** Rarefying followed by permutation controls type I error; the sensitivity loss is negligible when overdispersion is high and is summarised by a rarefaction efficiency index.
  conf: single (marker) · class: model (marker) · holds: high overdispersion · src: hongRarefyNotRarefy2022 (FT; model; single) · trail: MB-01 §5.4 · from: MB-01:I-0127, MB-01:A-256, MB-01:B-0369
- **rarefying.16** Rarefying is contested: McMurdie and Holmes 2014 against Schloss 2024a and 2024b, Weiss 2017 and Hong 2022 (partial), with Willis 2019 opposing it for richness; removing Schloss 2024b would leave McMurdie and Holmes 2014 as the main benchmark against it.
  conf: cont (critic: MB-01:C-041) · class: not stated · holds: mostly simulation benchmarks; the strongest pro-rarefaction evidence comes mainly from one author · src: mcmurdieWasteNotWant2014 (FT; model; cont), schlossWasteNotWant2024 (FT; model; single), schlossRarefactionCurrentlyBest2024 (FT, re-opened; model; cont), weissNormalizationMicrobialDifferential2017 (FT; model; repl), hongRarefyNotRarefy2022 (FT; model; single), willisRarefactionAlphaDiversity2019 (FT; assert; cont) · trail: MB-01 §6. Where, §answers, §critic · from: MB-01:A-280, MB-01:A-291, MB-01:A-309, MB-01:B-0405, MB-01:B-0406, MB-01:C-041
- **rarefying.17** Willis argues that plug-in and rarefied richness are both negatively biased and that rarefying can create false differences between environments with equal richness but different abundance structures; she recommends estimators with variance estimates compared through measurement-error models.
  conf: cont (marker) · class: not stated · holds: statistical argument plus a worked simulated example; the review labels it asserted, which the critic says understates the evidence against rarefying for richness · src: willisRarefactionAlphaDiversity2019 (FT; assert; cont) · trail: MB-01 §5.2, §critic · from: MB-01:I-0114, MB-01:A-233, MB-01:B-0345, MB-01:C-043, MB-01:C-044
- **rarefying.18** Breakaway and betta are offered by their makers as estimators with variance estimates.
  conf: not stated · class: assert (note: "makers' claims") · holds: makers' claims, abstract only · src: willisEstimatingDiversityFrequency2015 (AB; makers' claims), willisImprovedDetectionChanges2017 (AB; makers' claims) · trail: MB-01 §5.2 · from: MB-01:B-0346
- **rarefying.19** Rarefaction curves display sampling completeness (ecology) but were not benchmarked as a comparison method in the sources found.
  conf: not stated · class: search (note: "Not benchmarked as a comparison method in the sources found") · holds: the sources found · src: none (the review's search) · trail: MB-01 §5.6 · from: MB-01:B-0394

### coverage-standardisation: coverage-based standardisation and sample coverage
needs: alpha-diversity, rarefying

- **coverage-standardisation.1** Standardising by sample completeness rather than size gives less biased richness ratios, by Chao and Jost's argument.
  conf: not stated · class: model (marker) · holds: ecology, INDIRECT · src: chaoCoveragebasedRarefactionExtrapolation2012 (FT; model; INDIRECT) · trail: MB-01 §5.1 · from: MB-01:I-0107, MB-01:A-234
- **coverage-standardisation.2** A 2026 test on terrestrial inventories finds coverage-based rarefaction "does not respond predictably" to richness.
  conf: single (marker) · class: model (marker) · holds: terrestrial inventories, non-microbial, INDIRECT; abstract only · src: alroyCoveragebasedRarefactionFails2026 (AB; model; single; INDIRECT) · trail: MB-01 §5.1 · from: MB-01:I-0109, MB-01:A-235
- **coverage-standardisation.3** In Schloss 2024b's null models, coverage-based iNEXT estimates were among those that "showed a strong correlation between richness and the number of sequences"; the text exempts only "rarefaction and possibly the size-based iNEXT estimates". This is the only microbial amplicon test of coverage-based standardisation found.
  conf: not stated · class: model (note: "under multinomial-type null models built from 12 V4 datasets") · holds: null models; the synthesis agent's reading of the re-opened full text, verified by the critic · src: schlossRarefactionCurrentlyBest2024 (FT, re-opened) · trail: MB-01 §5.2, §critic, §Search record · from: MB-01:A-236, MB-01:B-0342..0344, MB-01:B-0440, MB-01:C-049
- **coverage-standardisation.4** Beyond Schloss 2024b, the evidence on coverage-based standardisation is non-microbial: it has almost no microbial benchmark.
  conf: not stated · class: search (note: "Not found: an independent microbial amplicon benchmark of coverage-based standardisation") · holds: statistics angle · src: none (the review's search) · trail: MB-01 §critic, §8. Answers · from: MB-01:A-313, MB-01:C-050, MB-01:B-0449, MB-01:A-285
- **coverage-standardisation.5** Coverage-based standardisation is contested: Chao and Jost 2012 against Alroy 2026 (both non-microbial) and the microbial null model in Schloss 2024b.
  conf: cont (note: "Coverage-based standardisation: Chao and Jost 2012 versus Alroy 2026") · class: not stated · holds: two non-microbial studies and one microbial null model · src: chaoCoveragebasedRarefactionExtrapolation2012 (FT; model; INDIRECT), alroyCoveragebasedRarefactionFails2026 (AB; model; single; INDIRECT), schlossRarefactionCurrentlyBest2024 (FT, re-opened) · trail: MB-01 §answers · from: MB-01:A-282
- **coverage-standardisation.6** Median Good's coverage ranged from 89.4% (seagrass) to 99.8% (human); reaching 95% and 99% coverage required about 3 and 101 times the sequences needed for 90%.
  conf: not stated · class: deriv (note: "Schloss 2024b) [deriv]") · holds: 12 public V4 studies; checked against full text by the critic · src: schlossRarefactionCurrentlyBest2024 (FT, re-opened) · trail: MB-01 §3.3, §critic · from: MB-01:B-0285, MB-01:B-0286, MB-01:I-0084, MB-01:C-054

### proportions: proportions (relative abundance) for comparing samples
needs: beta-diversity, differential-abundance, bias-consistency

- **proportions.1** Proportions and rarefying were the only methods that fully normalised depth, and scaling methods masked differences in common OTUs.
  conf: single (marker) · class: model (marker) · holds: abstract only · src: mcknightMethodsNormalizingMicrobiome2019 (AB; model; single) · trail: MB-01 §5.3 · from: MB-01:I-0123, MB-01:A-249
- **proportions.2** McKnight 2019's result for proportions conflicts with Schloss 2024b, in which relative-abundance Bray-Curtis stayed depth-sensitive under the null.
  conf: cont (note: "This conflicts with Schloss 2024b") · class: not stated · holds: two simulation designs · src: mcknightMethodsNormalizingMicrobiome2019 (AB; model; single), schlossRarefactionCurrentlyBest2024 (FT, re-opened) · trail: MB-01 §5.3, §6. Where · from: MB-01:A-249, MB-01:A-281, MB-01:B-0360, MB-01:B-0407
- **proportions.3** With a tenfold depth difference, tests on proportions had severe type I inflation, which rarefying controlled.
  conf: not stated · class: not stated · holds: tenfold depth difference · src: yangComprehensiveEvaluationMicrobial2022 (FT) · trail: MB-01 §5.4 · from: MB-01:A-257, MB-01:B-0370
- **proportions.4** Proportion-based differential-abundance results err when the community's mean efficiency is associated with the condition.
  conf: single (marker) · class: model (marker) · holds: preprint, abstract only · src: mclarenImplicationsTaxonomicBias2022 (AB; PREPRINT; model; single) · trail: MB-01 §5.4 · from: MB-01:I-0135, MB-01:A-262

### scaling-normalisation: scaling normalisation
needs: beta-diversity, differential-abundance

- **scaling-normalisation.1** Total-count scaling can bias differential-expression estimates in RNA-seq.
  conf: not stated · class: not stated · holds: RNA-seq, INDIRECT; abstract only · src: bullardEvaluationStatisticalMethods2010 (AB; INDIRECT) · trail: MB-01 §5.1 · from: MB-01:B-0330
- **scaling-normalisation.2** TMM and DESeq's negative binomial model also come from RNA-seq, and both assume most features are unchanged between conditions; the scaling normalisations used on microbiome data (TMM, RLE, CSS, VST, SRS, Wrench) come from RNA-seq.
  conf: not stated · class: not stated · holds: RNA-seq origins, INDIRECT; the assumption as noted by Weiss 2017 · src: robinsonScalingNormalizationMethod2010 (AB; INDIRECT), andersDifferentialExpressionAnalysis2010 (AB; INDIRECT), bullardEvaluationStatisticalMethods2010 (AB; INDIRECT), weissNormalizationMicrobialDifferential2017 (FT) · trail: MB-01 §5.1, §answers · from: MB-01:A-270, MB-01:B-0331, MB-01:B-0332
- **scaling-normalisation.3** In shotgun gene-abundance data, TMM and RLE performed best.
  conf: not stated · class: not stated · holds: shotgun, INDIRECT; abstract only · src: pereiraComparisonNormalizationMethods2018 (AB; INDIRECT, shotgun) · trail: MB-01 §5.1 · from: MB-01:B-0333
- **scaling-normalisation.4** Under Schloss's null models, scaling normalisations did not remove depth effects.
  conf: not stated · class: model (note: "Under Schloss's null they did not remove depth effects") · holds: null models · src: schlossRarefactionCurrentlyBest2024 (FT, re-opened) · trail: MB-01 §answers · from: MB-01:A-271
- **scaling-normalisation.5** In a simulation, RLE and VST came close to quantitative methods for association tests in a dysbiosis scenario.
  conf: not stated · class: model (note: "In the Llorens-Rico 2021 simulation") · holds: simulated faeces without taxon bias · src: llorensricoBenchmarkingMicrobiomeTransformations2021 (FT) · trail: MB-01 §answers · from: MB-01:A-272, MB-01:C-051
- **scaling-normalisation.6** DESeq2's FDR rose with more samples or uneven libraries.
  conf: not stated · class: not stated · holds: more samples or uneven libraries · src: weissNormalizationMicrobialDifferential2017 (FT) · trail: MB-01 §5.4 · from: MB-01:B-0368
- **scaling-normalisation.7** Wrench's makers state that library-size scaling and rarefaction cannot correct compositional bias that is uncorrelated with library size.
  conf: not stated · class: assert (note: "Wrench's makers state") · holds: makers' claim, abstract only · src: kumarAnalysisCorrectionCompositional2018 (AB; makers' claim) · trail: MB-01 §5.4 · from: MB-01:B-0375
- **scaling-normalisation.8** SRS's makers claim better reproducibility than rarefying.
  conf: not stated · class: assert (note: "SRS's makers claim") · holds: makers' claim, abstract only · src: beuleImprovedNormalizationSpecies2020 (AB) · trail: MB-01 §5.4 · from: MB-01:B-0376

### compositional-methods: compositional data analysis and log-ratio methods
needs: differential-abundance, beta-diversity, bias-consistency

- **compositional-methods.1** A review argues that 16S data are compositions "at all stages" and should be analysed with log-ratios.
  conf: cont (marker) · class: assert (marker) · holds: a review, abstract only · src: gloorMicrobiomeDatasetsCompositional2017 (AB; assert; cont) · trail: MB-01 §5.1 · from: MB-01:I-0110
- **compositional-methods.2** ANCOM had the best FDR control, controlling FDR well where other methods did not.
  conf: not stated · class: not stated · holds: Weiss 2017 · src: weissNormalizationMicrobialDifferential2017 (FT) · trail: MB-01 §5.4 · from: MB-01:A-258, MB-01:B-0368
- **compositional-methods.3** Reference frames make differential rankings invariant to load.
  conf: single (marker) · class: meas (marker) · holds: abstract only · src: mortonEstablishingMicrobialComposition2019 (AB; meas; single) · trail: MB-01 §5.4 · from: MB-01:I-0134, MB-01:A-261
- **compositional-methods.4** Fold changes in taxon ratios are invariant to multiplicative bias, while fold changes in proportions are not and can change sign.
  conf: single (note: "The bias-invariance of ratio-based methods rests on McLaren 2019") · class: not stated · holds: model · src: mclarenConsistentCorrectableBias2019 (FT, re-opened) · trail: MB-01 §5.4 · from: MB-01:A-262, MB-01:A-293, MB-01:B-0377
- **compositional-methods.5** Makers claim FDR control for ANCOM-BC and ANCOM; independent benchmarks (Yang and Chen 2022; Wirbel 2024) disagree in part.
  conf: cont (note: "Independent benchmarks disagree in part") · class: not stated · holds: makers' claims, abstract only, against independent simulation and implanted-signal benchmarks · src: linAnalysisCompositionsMicrobiomes2020 (AB; makers' claims), mandalAnalysisCompositionMicrobiomes2015 (AB; makers' claims), yangComprehensiveEvaluationMicrobial2022 (FT; model; repl), wirbelRealisticBenchmarkDifferential2024 (FT; model; repl) · trail: MB-01 §5.4, §answers · from: MB-01:A-283, MB-01:B-0373, MB-01:B-0374

### absolute-quantification: absolute quantification of total load
needs: microbial-load, bias-consistency, differential-abundance

- **absolute-quantification.1** Absolute quantification (qPCR, flow cytometry, dPCR, spike-ins) can reverse conclusions drawn from relative abundance, but does not remove taxon-specific extraction and PCR bias.
  conf: repl (note: "replicated that it changes conclusions") · class: meas (note: "Load measurements change conclusions drawn from relative data") · holds: several studies · src: vandeputteQuantitativeMicrobiomeProfiling2017 (AB), propsAbsoluteQuantificationMicrobial2016 (AB), barlowQuantitativeSequencingFramework2020 (FT), tkaczAbsoluteQuantitationMicrobiota2018 (FT) · trail: MB-01 §5.5, §critic · from: MB-01:A-266, MB-01:A-279, MB-01:A-312, MB-01:B-0378, MB-01:C-042
- **absolute-quantification.2** Flow-cytometry quantitative profiling showed the Bacteroides-Prevotella trade-off in relative data to be an artefact, and load drove Crohn's-associated differences.
  conf: not stated · class: not stated · holds: human faeces; abstract only · src: vandeputteQuantitativeMicrobiomeProfiling2017 (AB) · trail: MB-01 §5.5 · from: MB-01:B-0379
- **absolute-quantification.3** Relative enrichment did not imply absolute outgrowth.
  conf: not stated · class: not stated · holds: engineered freshwater; abstract only · src: propsAbsoluteQuantificationMicrobial2016 (AB; engineered freshwater) · trail: MB-01 §5.5 · from: MB-01:B-0380
- **absolute-quantification.4** Absolute abundance could hold steady or rise while relative abundance fell.
  conf: not stated · class: not stated · holds: soil · src: tkaczAbsoluteQuantitationMicrobiota2018 (FT; soil) · trail: MB-01 §5.5 · from: MB-01:B-0381
- **absolute-quantification.5** Spike-in bacteria added before extraction recovered ratios of absolute abundances across mouse faecal dilutions; the three spike-in species gave different read yields.
  conf: repl (marker) · class: meas (marker) · holds: mouse faecal dilutions · src: stammlerAdjustingMicrobiomeProfiles2016 (FT; meas; repl) · trail: MB-01 §5.5 · from: MB-01:I-0136, MB-01:B-0382
- **absolute-quantification.6** dPCR anchoring gave about 2x extraction accuracy above 8.3 x 10^4 input copies, and absolute but not relative analysis revealed diet effects.
  conf: single (marker) · class: meas (marker) · holds: above 8.3 x 10^4 input copies · src: barlowQuantitativeSequencingFramework2020 (FT; meas; single) · trail: MB-01 §5.5 · from: MB-01:I-0137
- **absolute-quantification.7** Soil internal standards tracked PLFA and respiration biomass better than those two measures tracked each other.
  conf: single (marker) · class: meas (marker) · holds: soil; abstract only · src: smetsMethodSimultaneousMeasurement2016 (AB; meas; single) · trail: MB-01 §5.5 · from: MB-01:I-0138
- **absolute-quantification.8** Total 16S qPCR multiplied by relative abundance correlated near-perfectly with taxon-specific qPCR.
  conf: single (marker) · class: meas (marker) · holds: four taxa; a comparison of methods that share an upstream (qPCR versus qPCR-anchored sequencing) · src: jianQuantitativePCRProvides2020 (FT; meas; single) · trail: MB-01 §5.5, §critic · from: MB-01:I-0139, MB-01:C-127, MB-01:C-106
- **absolute-quantification.9** In simulation, experimental quantitative profiling outperformed computational transformations for associations.
  conf: not stated · class: model (note: "In simulation") · holds: simulated faeces without taxon bias · src: llorensricoBenchmarkingMicrobiomeTransformations2021 (FT) · trail: MB-01 §5.5 · from: MB-01:B-0383, MB-01:C-051
- **absolute-quantification.10** Absolute quantification leaves taxon-specific extraction and PCR bias in place.
  conf: not stated · class: not stated · holds: McLaren 2019 and Bonk 2018 · src: mclarenConsistentCorrectableBias2019 (FT, re-opened), bonkPCRbasedQuantificationTaxaspecific2018 (AB) · trail: MB-01 §5.5 · from: MB-01:A-267, MB-01:B-0384, MB-01:B-0385
- **absolute-quantification.11** qPCR and sequencing both count extracellular DNA, unlike cell counts.
  conf: not stated · class: not stated · holds: Jian 2020 · src: jianQuantitativePCRProvides2020 (FT) · trail: MB-01 §5.5 · from: MB-01:B-0386
- **absolute-quantification.12** qPCR and flow cytometry agreed on a whole-cell mock (|r| = 0.967) but gave "highly divergent" profiles for faeces (qPCR versus flow-cytometry enumeration, Pearson r = -0.50); ddPCR correlated strongly with qPCR, which the authors used to rule out qPCR imprecision as the cause of the divergence.
  conf: single (marker) · class: meas (marker) · holds: whole-cell mock and faeces; the divergence of absolute-quantification methods rests on Galazzo 2020; the review gave the faecal correlation as ddPCR versus flow, which the critic corrected · src: galazzoHowCountOur2020 (FT; meas; single) · trail: MB-01 §5.5, §critic · from: MB-01:I-0140, MB-01:A-267, MB-01:A-292, MB-01:C-045, MB-01:C-057, MB-01:C-071
- **absolute-quantification.13** Synthetic spike-ins had differing detection efficiencies and small departures from linearity, and correlations were weaker with Taq than with KOD polymerase.
  conf: repl (marker) · class: meas (marker) · holds: synthetic spike-ins · src: tourlousseSyntheticSpikeinStandards2016 (FT; meas; repl) · trail: MB-01 §5.5 · from: MB-01:I-0141, MB-01:B-0388
- **absolute-quantification.14** Seawater internal standards agreed with flow cytometry at r2 = 0.19 until corrections for copy number and particle association (with four outliers removed) raised it to 0.61; the authors conclude that the method "is quantitative" and "provided results consistent with ... total bacterial counts by flow cytometry".
  conf: single (marker) · class: meas (marker) · holds: Antarctic seawater; the r2 figures need the body and could not be verified by the critic; the review reported the failure mode without the authors' conclusion · src: linTowardsQuantitativeMicrobiome2019 (FT; meas; single) · trail: MB-01 §5.5, §critic · from: MB-01:I-0142, MB-01:A-269, MB-01:C-046, MB-01:C-047, MB-01:C-048, MB-01:C-081, MB-01:B-0429, MB-01:I-0090
- **absolute-quantification.15** A review states that internal standards often underperform or fail.
  conf: not stated · class: assert (marker) · holds: review, abstract only · src: harrisonQuestAbsoluteAbundance2020 (AB; assert) · trail: MB-01 §5.5 · from: MB-01:I-0143
- **absolute-quantification.16** Agreement between quantification methods is contested: Jian 2020 against Galazzo 2020.
  conf: cont (note: "Where the evidence conflicts") · class: not stated · holds: one study each · src: jianQuantitativePCRProvides2020 (FT; meas; single), galazzoHowCountOur2020 (FT; meas; single) · trail: MB-01 §6. Where, §answers · from: MB-01:A-283, MB-01:B-0408, MB-01:A-279 · rating: "weak on the agreement between quantification methods"
- **absolute-quantification.17** Absolute-abundance work multiplies relative abundance by total counts (flow cytometry or qPCR), which converts gene copies but not cells per taxon.
  conf: not stated · class: not stated · holds: non-soil; abstract only · src: propsAbsoluteQuantificationMicrobial2016 (AB) · trail: MB-02 §D3.1 · from: MB-02:B-0316
- **absolute-quantification.18** Apart from Llorens-Rico 2021, which simulated faeces without taxon bias, no benchmark of any approach for unequal depth or load builds taxon-specific bias and differences in total load into the simulated truth together, and none in soil or water uses measured absolute loads as truth.
  conf: not stated · class: search (note: "Not found: an independent microbial amplicon benchmark") · holds: statistics angle; lab and bioinformatics angles for spike-ins · src: llorensricoBenchmarkingMicrobiomeTransformations2021 (FT) · trail: MB-01 §answers, §critic · from: MB-01:A-285, MB-01:C-051

### relic-dna: relic DNA
needs: extraction, alpha-diversity

- **relic-dna.1** Across soils, an average of 40% of DNA was extracellular or from non-intact cells.
  conf: cont (marker) · class: meas (marker) · holds: soils; abstract only · src: cariniRelicDNAAbundant2016 (AB; meas; cont) · trail: MB-01 §2.2, MB-02 §D3.3 · from: MB-01:I-0012, MB-01:B-0156, MB-02:A-109, MB-02:B-0341
- **relic-dna.2** Removing relic DNA with propidium monoazide showed it inflated soil richness by up to 55%, more so at high pH and not at all in some soils, and misestimated relative abundances.
  conf: cont (marker) · class: meas (marker) · holds: soils; abstract only · src: cariniRelicDNAAbundant2016 (AB; meas; cont) · trail: MB-01 §2.2, MB-02 §D3.3 · from: MB-01:I-0012, MB-01:A-047, MB-01:B-0111, MB-02:A-109, MB-02:B-0341
- **relic-dna.3** Relic DNA averaged 33% across soil, sediment, water and mammalian gut (over 80% in some samples) but had minimal effect on diversity estimates.
  conf: cont (marker) · class: meas (marker) · holds: four ecosystem types; MB-02 read it as an abstract · src: lennonHowWhereRelic2018 (FT; meas; cont) · trail: MB-01 §2.2, §7. Bounds, MB-02 §D3.3 · from: MB-01:I-0013, MB-01:A-047, MB-01:B-0157, MB-01:B-0416, MB-02:A-109, MB-02:B-0342
- **relic-dna.4** Models predict relic-DNA bias only when relic and intact abundance distributions differ.
  conf: cont (marker) · class: meas (marker) · holds: models in a measured study · src: lennonHowWhereRelic2018 (FT; meas; cont) · trail: MB-01 §2.2 · from: MB-01:I-0013
- **relic-dna.5** The effect of relic DNA on diversity is contested: Carini 2016 against Lennon 2018.
  conf: cont (marker) · class: not stated · holds: soils against four ecosystem types · src: cariniRelicDNAAbundant2016 (AB; meas; cont), lennonHowWhereRelic2018 (FT; meas; cont) · trail: MB-01 §2.2, §answers, MB-02 §D3.3 · from: MB-01:I-0012, MB-01:I-0013, MB-01:A-118, MB-01:B-0155, MB-02:A-118, MB-02:B-0340

### abundance-occupancy: local abundance and occupancy across soils
needs: rarity-terms, count-sampling, relic-dna

- **abundance-occupancy.1** In 88 North and South American soils (about 1,500 reads per soil), the ten most abundant OTUs per sample occurred on average in 28% of soils, against 2% for all OTUs; in 27 tropical forest soils within one hectare, the figures were 69% against 8%.
  conf: not stated · class: not stated · holds: bulk soil, amplicon reads; the critic could not verify these figures, and the source's abstract frames the study across Earth's major habitat types, not soils alone · src: nemergutGlobalPatternsBiogeography2011 (FT) · trail: MB-02 §D3.2, §critic · from: MB-02:A-101, MB-02:B-0318, MB-02:B-0319, MB-02:C-066, MB-02:C-067, MB-02:C-082, MB-02:C-083
- **abundance-occupancy.2** Total abundance and number of soils occupied were significantly and positively related; no coefficient is given.
  conf: not stated · class: not stated · holds: bulk soil; summed abundance also rises with occupancy by construction · src: nemergutGlobalPatternsBiogeography2011 (FT) · trail: MB-02 §D3.2, §critic · from: MB-02:A-101, MB-02:B-0320, MB-02:C-125
- **abundance-occupancy.3** The authors note that abundant taxa may simply be easier to detect, and that undersampling could hide intermediate distributions.
  conf: not stated · class: not stated · holds: bulk soil · src: nemergutGlobalPatternsBiogeography2011 (FT) · trail: MB-02 §D3.2 · from: MB-02:A-107, MB-02:B-0321, MB-02:B-0317
- **abundance-occupancy.4** Across 844 global soils, median prevalence was 0.3 for common taxa and 0.001 for rare taxa.
  conf: not stated · class: not stated · holds: a class-level contrast, a different measure from a taxon-level abundance-occupancy relationship; the common class is defined on the globally pooled rank-abundance distribution, and pooled abundance rises mechanically with prevalence; checked against full text by the critic · src: bickelChosenFewVariations2021 (FT) · trail: MB-02 §D3.2, §critic · from: MB-02:A-102, MB-02:B-0323, MB-02:C-124, MB-02:C-137, MB-02:C-057
- **abundance-occupancy.5** Across about 124,000 taxa in 3.41 km2 of urban park soil, occupancy correlated strongly with environmental range; abundance was not the axis tested.
  conf: not stated · class: not stated · holds: one urban park; abstract only · src: barberanWhyAreMicrobes2014 (AB) · trail: MB-02 §D3.2 · from: MB-02:A-103, MB-02:B-0324, MB-02:B-0325
- **abundance-occupancy.6** The global list of dominant soil bacteria cannot serve as an independent test of the abundance-occupancy relationship, because dominance there is defined by abundance and ubiquity together.
  conf: not stated · class: not stated · holds: 237 soils · src: delgadobaquerizoGlobalAtlasDominant2018 (FT) · trail: MB-02 §D3.2 · from: MB-02:A-104, MB-02:B-0326, MB-02:B-0254
- **abundance-occupancy.7** Soil also holds taxa that are abundant at some times or places and rare elsewhere: 2,197 conditionally rare ASVs alongside 11,838 permanently rare and 8,333 transiently rare ASVs.
  conf: not stated · class: not stated · holds: one salt-marsh soil chronosequence; checked against full text by the critic · src: jiaUnravellingInterplayEcological2022 (FT) · trail: MB-02 §D3.2 · from: MB-02:A-105, MB-02:B-0327, MB-02:C-057, MB-02:B-0265
- **abundance-occupancy.8** Conditionally rare taxa show that some taxa are locally abundant but occupy few samples, cutting against a uniform abundance-occupancy relationship.
  conf: not stated · class: not stated · holds: conditionally rare taxa · src: shadeConditionallyRareTaxa2014 (FT, excerpts), jiaUnravellingInterplayEcological2022 (FT) · trail: MB-02 §answers · from: MB-02:A-120
- **abundance-occupancy.9** In the two bulk-soil amplicon studies with figures (Nemergut 2011; Bickel and Or 2021), more abundant taxa occupy more soils; the two are not fully independent (Bickel and Or reanalysed compiled datasets including the Earth Microbiome Project, which plausibly overlaps the soils Nemergut used), and both measures are partly built in by construction.
  conf: not stated · class: not stated · holds: bulk soil, amplicon reads; consistent with general macroecology; removing Nemergut 2011 leaves one quantitative bulk-soil figure · src: nemergutGlobalPatternsBiogeography2011 (FT), bickelChosenFewVariations2021 (FT) · trail: MB-02 §critic, §D3.2 · from: MB-02:C-048, MB-02:C-049, MB-02:C-050, MB-02:A-115, MB-02:A-123 · rating: "Moderate for the existence of a positive relationship"
- **abundance-occupancy.10** Whether a soil abundance-occupancy relationship exists beyond sampling, and how strong it is, is unresolved: detection limits (a single 454-era study at one site) and neutral or sampling models predict a positive relationship without selection, and no soil test against a sampling null was found, so the share attributable to biology is unknown.
  conf: unclear (note: "the share attributable to biology is unknown") · class: not stated · holds: bulk soil; the sampling-null evidence comes from non-soil data · src: zhouReproducibilityQuantitationAmplicon2011 (AB), grilliMacroecologicalLawsDescribe2020 (FT), sloanQuantifyingRolesImmigration2006 (AB) · trail: MB-02 §critic, §answers · from: MB-02:A-114, MB-02:A-116, MB-02:A-153, MB-02:C-051, MB-02:C-052, MB-02:C-053 · rating: "Weak for its interpretation"
- **abundance-occupancy.11** In common bean rhizospheres across four US regions plus a Colombian dataset, 48 bacterial and archaeal taxa were detected in every sample, and in a neutral-model fit to the abundance-occupancy distribution 13.7% of bacterial and archaeal taxa deviated from neutral expectation; samples were rarefied to 31,255 reads.
  conf: single (note: "The rhizosphere neutral-deviation figure rests on Stopnisek and Shade 2021 [74] alone") · class: not stated · holds: common bean rhizosphere; checked against full text by the critic · src: stopnisekPersistentMicrobiomeMembers2021 (FT) · trail: MB-02 §D3.2, §critic · from: MB-02:A-106, MB-02:A-125, MB-02:A-152, MB-02:B-0329..0331, MB-02:C-054, MB-02:C-057
- **abundance-occupancy.12** In 4,866 maize rhizosphere samples, seven OTUs were present in all, five of them responsive to host genotype.
  conf: not stated · class: not stated · holds: maize rhizosphere; abstract only · src: waltersLargescaleReplicatedField2018 (AB) · trail: MB-02 §D3.2 · from: MB-02:A-106, MB-02:A-152, MB-02:B-0332
- **abundance-occupancy.13** Rhizosphere evidence is limited to core-membership studies of two to three crops, and none reports an abundance-occupancy correlation coefficient in the passages read.
  conf: not stated · class: search (note: "None of these rhizosphere studies reports an abundance-occupancy correlation coefficient") · holds: bean, maize and Arabidopsis root data · src: stopnisekPersistentMicrobiomeMembers2021 (FT), waltersLargescaleReplicatedField2018 (AB), custerComparativeAnalysisCore2023 (FT, first 100,000 characters) · trail: MB-02 §D3.2, §critic · from: MB-02:A-117, MB-02:B-0328, MB-02:B-0334, MB-02:C-055
- **abundance-occupancy.14** A neutral community model with immigration and drift only predicts that abundant taxa occur in more samples, so a positive abundance-occupancy relationship is expected without selection; its use in the bean study treats deviations, not the relationship itself, as signal.
  conf: not stated · class: model (note: "the model predicts that abundant taxa occur in more samples") · holds: model; abstract only · src: sloanQuantifyingRolesImmigration2006 (AB), stopnisekPersistentMicrobiomeMembers2021 (FT) · trail: MB-02 §D3.3 · from: MB-02:A-112, MB-02:B-0344..0346
- **abundance-occupancy.15** Gamma-distributed abundance fluctuations plus finite read sampling predicted each species' occupancy from its mean and variance with no further parameters: absences were mostly attributable to sampling, and the model reproduced the abundance-occupancy relationship.
  conf: single (note: "removes the only parameter-free sampling null") · class: model (marker) · holds: non-soil biomes in the text read (nearest precedent); whether the datasets include soil was not checked in the supplementary information · src: grilliMacroecologicalLawsDescribe2020 (FT, partly re-opened; model; single) · trail: MB-02 §D3.3, MB-01 §4.2 · from: MB-01:I-0088, MB-01:A-193, MB-01:B-0300, MB-02:A-112, MB-02:A-124, MB-02:B-0347..0349, MB-02:C-120
- **abundance-occupancy.16** Positive intraspecific and interspecific abundance-occupancy relationships are general in the British flora and fauna, and multiple explanations have been tested; the sampling-artefact literature (Wright 1991; Holt et al. 2002) was not obtained.
  conf: not stated · class: not stated · holds: general macroecology; abstract only · src: gastonAbundanceoccupancyRelationships2000 (AB), wrightCorrelationsIncidenceAbundance1991 (not obtained), holtOccupancyabundanceRelationshipsSpatial2002 (not obtained) · trail: MB-02 §D2.4, §D3.3 · from: MB-02:A-066, MB-02:A-113, MB-02:B-0263, MB-02:B-0350, MB-02:B-0351
- **abundance-occupancy.17** The same positive relationship is read as ecological signal by some authors and as near-null by others; in the reviewer's reading this is a difference of interpretation, not of data.
  conf: not stated · class: reading (note: "the reviewer notes this is a difference of interpretation") · holds: neutral-model studies · src: sloanQuantifyingRolesImmigration2006 (AB) · trail: MB-02 §answers · from: MB-02:A-119
- **abundance-occupancy.18** The Bickel and Or global common-rare threshold was robust to using a quarter of the samples.
  conf: not stated · class: not stated · holds: 844 global soils · src: bickelChosenFewVariations2021 (FT) · trail: MB-02 §D3.3 · from: MB-02:A-111, MB-02:B-0343, MB-02:B-0292
- **abundance-occupancy.19** No soil study was found that tests whether the bulk-soil abundance-occupancy relationship exceeds a sampling or detection null, and none from cell counts or metagenomes, none specific to archaea, and none comparing bulk soil and rhizosphere within one study.
  conf: not stated · class: search (note: "I found no soil study that tests whether the observed bulk-soil abundance-occupancy relationship exceeds a sampling or detection null") · holds: a Europe PMC query whose 25 hits were reviewed by title, and a neutral-model query · src: none (the review's search) · trail: MB-02 §D3.3, §Search record, §critic · from: MB-02:A-114, MB-02:A-121, MB-02:B-0352, MB-02:B-0353, MB-02:C-052, MB-02:B-0370

### sample-comparison: comparing samples with unequal depth or load
needs: rarefying, coverage-standardisation, proportions, scaling-normalisation, compositional-methods, absolute-quantification

- **sample-comparison.1** How to compare samples with unequal depth or load is contested: rarefying, proportions and differential-abundance methods are all disputed, and no approach is shown to correct depth, load and taxon-specific bias together.
  conf: cont (critic: MB-01:C-041) · class: not stated · holds: mostly simulation benchmarks; the answer depends on the simulation design · src: none (the reviewer's synthesis across rarefying, proportions, scaling-normalisation, compositional-methods and absolute-quantification) · trail: MB-01 §critic, §answers, §1. Overview · from: MB-01:A-230, MB-01:A-273, MB-01:A-309, MB-01:B-0096, MB-01:C-041 · rating: "Weak to moderate overall"
- **sample-comparison.2** Weiss 2017, Hong 2022 and Schloss 2024a each say that results depend on data-generating assumptions, and Weiss 2017 and Schloss 2024a say that simulation results flip with design choices.
  conf: not stated · class: not stated · holds: simulation benchmarks; the review's stronger causal diagnosis is partly supported only · src: weissNormalizationMicrobialDifferential2017 (FT), hongRarefyNotRarefy2022 (FT), schlossWasteNotWant2024 (FT) · trail: MB-01 §answers, §critic · from: MB-01:A-284, MB-01:C-142

## Do not say

- **dns.1** "Departures occur at every step." / "departures found at every step"
  why: field sampling for water and host tissue was not searched, and several choices showed little or no detectable effect; the critic says departures were measured at most steps examined · instead: departure.3 · trail: MB-01 §critic · from: MB-01:A-034, MB-01:A-296, MB-01:C-062, MB-01:C-147, MB-01:C-148, MB-01:C-149
- **dns.2** "The largest measured distortions [in relative abundance] arise from taxon-specific efficiencies at DNA extraction and PCR", with the ordering extraction, then PCR, then sequencing, rated strong and backed by "many independent mock studies".
  why: the ordering rests on one 7-taxon dataset (Brooks 2015 reanalysed by McLaren 2019), with Albertsen 2015 as partial support, is contradicted by Fouhy 2016 and qualified by MBQC; it should be presented as SINGLE DATASET, not as a field-wide ordering, as the review's own single-source sensitivity field concedes · instead: departure.5, departure.7, extraction.8 · trail: MB-01 §critic · from: MB-01:A-111, MB-01:A-112, MB-01:C-015, MB-01:C-017, MB-01:C-061, MB-01:C-083, MB-01:C-084, MB-01:B-0090
- **dns.3** "calibration cut mean Bray-Curtis error from 0.35 to 0.08 in a shotgun dataset"
  why: the full text places the figure in the Brooks et al. 2015 16S cell mixtures; the Costea shotgun calibration is reported only qualitatively · instead: bias-consistency.5 · trail: MB-01 §critic · from: MB-01:C-021, MB-01:C-055, MB-01:C-066, MB-01:C-067, MB-01:C-068, MB-01:C-069, MB-01:B-0247
- **dns.4** "the original V4 primers [515F/806R] under-represented SAR11 by about 4-10 fold in marine field samples but only about 2-fold in mocks"
  why: the abstract gives these figures for 515F-Y/806R, not the original 515F-C/806R · instead: primers.4 · trail: MB-01 §critic · from: MB-01:A-052, MB-01:C-056, MB-01:C-070, MB-01:B-0113, MB-01:B-0161
- **dns.5** "Mock bias did not transfer to the field."
  why: rests on Parada 2016 (abstract only) for one primer pair (515F-Y/806R) and one taxon (SAR11) · instead: primers.4, bias-consistency.16 · trail: MB-01 §critic · from: MB-01:C-092, MB-01:B-0114
- **dns.6** "ddPCR versus flow correlated at only r = 0.50"
  why: the full text reports qPCR versus flow-cytometry enumeration on faeces (Pearson r = -0.50); ddPCR correlated strongly with qPCR · instead: absolute-quantification.12 · trail: MB-01 §critic · from: MB-01:C-045, MB-01:C-057, MB-01:C-071, MB-01:I-0140
- **dns.7** "Unfiltered OTU tables were about 50% (mocks) to 80% (gnotobiotic mice) spurious taxa."
  why: the source says after OTU clustering and singleton removal, not unfiltered · instead: denoising-clustering.10 · trail: MB-01 §critic · from: MB-01:A-095, MB-01:C-058, MB-01:C-072, MB-01:B-0130, MB-01:B-0220
- **dns.8** "mean Jaccard 0.80" (for PCR replicates of negative extraction controls)
  why: the source reports a mean Jaccard distance of 0.80; without "distance" the figure reads as high similarity · instead: technical-variation.2 · trail: MB-01 §critic · from: MB-01:C-059, MB-01:C-082, MB-01:B-0304
- **dns.9** "Multinomial or Poisson sampling explains much replicate disagreement in taxa detected", rated moderate "from several soil studies".
  why: the evidence is one 454 dataset of 24 Oklahoma soils (Zhou 2011 data modelled by Zhou 2013) and one laboratory (Wen 2017), whose MiSeq replicates do not fit the model; one dataset is counted as several studies, and Wen 2017's contrary depth plateau is left out · instead: count-sampling.5, count-sampling.6 · trail: MB-01 §critic · from: MB-01:A-187, MB-01:A-214, MB-01:A-306, MB-01:C-063, MB-01:C-086, MB-01:C-135, MB-01:C-120, MB-01:C-121, MB-01:C-122, MB-01:C-123
- **dns.10** "Agreement in relative abundance rises with depth, roughly as a square root."
  why: rests on one caecal extract with four technical replicates (Barlow 2020, SINGLE SOURCE) · instead: count-sampling.7 · trail: MB-01 §critic · from: MB-01:A-307, MB-01:C-037, MB-01:C-085
- **dns.11** "Relative abundance is robust to the pipeline; counts of taxa are not."
  why: generalises from Nearing 2018 (with Marizzoni 2020); Nearing 2018 itself reports that all pipelines "markedly differed" from expected composition on the Zymo mock, and Straub 2020 reports pipeline-dependent interpretations · instead: denoising-clustering.2, denoising-clustering.4, denoising-clustering.6 · trail: MB-01 §critic · from: MB-01:C-087, MB-01:I-0052
- **dns.12** "Library prep and primers are the largest drivers of error profile" (without a single-source flag).
  why: rests on Schirmer 2015 alone · instead: library-sequencing.3 · trail: MB-01 §critic · from: MB-01:C-088
- **dns.13** "V4 genus accuracy was about 50% at 97% identity" and "Reference databases carry about 10-17% annotation error", without a single-source qualifier.
  why: both rest on Edgar 2018b and 2018c, from one author who also develops competing classifiers · instead: taxonomy.2, taxonomy.7 · trail: MB-01 §critic · from: MB-01:C-089, MB-01:A-097, MB-01:A-098
- **dns.14** "chimera formation was reproducible across amplifications" (as a general consistency finding)
  why: rests on Haas 2011 (Sanger and 454) alone · instead: chimeras.2 · trail: MB-01 §critic · from: MB-01:C-090
- **dns.15** "Fast-responding soil isolates averaged 5.5 copies against 1.4" (as a general finding)
  why: rests on one abstract-only study (Klappenbach 2000) · instead: copy-number.25 · trail: MB-01 §critic · from: MB-01:C-091
- **dns.16** "in a survey of two journals for 2018, 30% of papers reported any negative control and 10% any positive control" (as a figure for 16S practice)
  why: Hornung 2019 surveyed papers using any high-throughput community sequencing (16S, shotgun, metatranscriptomics, ITS, 18S and others); it is not a 16S-only figure, and it is SINGLE SOURCE · instead: contamination.9 · trail: MB-01 §critic · from: MB-01:C-004, MB-01:C-005, MB-01:C-132, MB-01:A-017
- **dns.17** "No source found that documents field sampling choices for water (filter pore size, volume) or for host tissue"
  why: the review contradicts itself; on its own search record these choices are unsearched, not "not found" · instead: sample-storage.8 · trail: MB-01 §critic · from: MB-01:C-006, MB-01:C-007, MB-01:C-008, MB-01:B-0142, MB-01:A-027
- **dns.18** "Willis 2019 (asserted)" and rarefaction "contested by an assertion (Willis 2019)"
  why: Willis 2019 presents statistical argument plus a worked simulated example; calling it an assertion against Schloss's "modelled" simulations understates the evidence against rarefying for richness and applies the evidence class unevenly · instead: rarefying.17, rarefying.16 · trail: MB-01 §critic · from: MB-01:A-275, MB-01:C-043, MB-01:C-044, MB-01:C-064, MB-01:C-124, MB-01:C-125, MB-01:C-126
- **dns.19** "Spike-in totals agreed poorly with flow cytometry (r2 0.19) until corrected" (reported as a failure mode without the authors' conclusion)
  why: the authors conclude the internal-standard method is quantitative and consistent with flow cytometry; reporting only r2 = 0.19 breaches the review's own rule, and the figure could not be verified · instead: absolute-quantification.14 · trail: MB-01 §critic · from: MB-01:C-046, MB-01:C-047, MB-01:C-081, MB-01:C-127, MB-01:A-269, MB-01:C-048
- **dns.20** "Total 16S qPCR multiplied by relative abundance correlated near-perfectly with taxon-specific qPCR" (at face value)
  why: it is a comparison of methods that share an upstream (qPCR versus qPCR-anchored sequencing) · instead: absolute-quantification.8 · trail: MB-01 §critic · from: MB-01:C-127, MB-01:I-0139
- **dns.21** "Soil: in 24 grassland soils, the best-fitting distributions were exponential or inverse gamma" (as a verified main-text finding)
  why: the best-fit results are in supplementary Table S3; the main text does not state which distributions won, and the claim rests on unread or unshown supplementary material · instead: abundance-distribution.1 · trail: MB-01 §critic · from: MB-01:C-026, MB-01:C-077, MB-01:C-078, MB-01:C-079
- **dns.22** "Water and hosts: copy-corrected ocean and skin rank-abundance data fitted a lognormal better" (as the answer for water and for hosts)
  why: one study (Kembel 2012) pools ocean and human skin into one item, folding the separate water and host cases together; its simulations assumed a lognormal · instead: abundance-distribution.3, abundance-distribution.8 · trail: MB-01 §critic · from: MB-01:C-027, MB-01:C-134, MB-01:A-164
- **dns.23** EMP average copy number of about 2.2 given as the value for water.
  why: the EMP value pools free-living (soil, water, sediment) and plant-associated samples · instead: community-copy-number.5 · trail: MB-01 §critic · from: MB-01:C-136
- **dns.24** Extraction bias "consistent on the ratio scale" as one finding across a 16S cell mixture and a shotgun spike-in.
  why: combines a 16S cell-mixture result and a secondary shotgun spike-in result, mixing measurement types · instead: bias-consistency.3, bias-consistency.4 · trail: MB-01 §critic · from: MB-01:C-137
- **dns.25** Index misassignment of "0.1 to 6% of reads moved between samples" (as one 16S figure)
  why: merges non-16S genome and exome libraries (Costello 2018), Illumina's own documentation, non-16S amplicons (Wright 2016) and 16S data, without INDIRECT labels · instead: index-misassignment.2, index-misassignment.3, index-misassignment.4, index-misassignment.5, index-misassignment.6, index-misassignment.7 · trail: MB-01 §critic · from: MB-01:C-133
- **dns.26** "This determines whether a fixed correction can work" (as a finding about bias consistency)
  why: the reviewer's framing of what matters for analysis design, not a literature finding · instead: none · trail: MB-01 §critic · from: MB-01:C-138, MB-01:B-0244
- **dns.27** "The difference in load is the likely reason" for the pooled-versus-single PCR contrast, as a finding.
  why: the reviewer's own reconciliation, labelled untested but not marked as the reviewer's reading · instead: technical-variation.10 · trail: MB-01 §critic · from: MB-01:C-139, MB-01:C-140, MB-01:C-141
- **dns.28** "Simulations disagree mainly because they build different data-generating processes into the truth" (as the review's causal diagnosis)
  why: only partly supported: Weiss 2017, Hong 2022 and Schloss 2024a each say results depend on data-generating assumptions · instead: sample-comparison.2 · trail: MB-01 §critic · from: MB-01:C-142, MB-01:B-0097
- **dns.29** The section 5.6 summary of what each approach is "shown to correct", read as a recommendation.
  why: its cells mix makers' claims and simulation results with measured results without per-cell evidence class, so it reads closer to a method recommendation than the brief allows · instead: rarefying.4, rarefying.7, rarefying.16, absolute-quantification.1, compositional-methods.4 · trail: MB-01 §critic · from: MB-01:C-143, MB-01:B-0389..0397
- **dns.30** Edgar 2017b (UNBIAS) as "a strong pessimistic claim" set aside as single-source, against pro-correction results without a matching label.
  why: the pro-correction results it conflicts with (McLaren, Silverman) each also rest on a single mock design · instead: departure.8, copy-number-correction.21, bias-consistency.2, bias-consistency.10 · trail: MB-01 §critic · from: MB-01:C-131
- **dns.31** McLaren 2019's ratio-scale consistency as the main evidence, with field evidence of inconsistency (Parada) weighed as merely "limiting".
  why: the ratio-scale result comes from 7 taxa mixed as cells and reanalysed; neither side's small-n and access limits are stated symmetrically · instead: bias-consistency.1, bias-consistency.2, bias-consistency.12 · trail: MB-01 §critic · from: MB-01:C-128, MB-01:C-129, MB-01:C-130
- **dns.32** "In bulk-soil amplicon data, a small fraction of taxa (0.4 to 2% by the two definitions) holds about 41 to 58% of reads"
  why: pools the Delgado-Baquerizo 2% / 41% (per-sample mean, joint abundance-and-ubiquity definition) and Bickel and Or 0.4% / 58% (pooled global relative abundance) figures, which the review's own body says must not be combined · instead: abundance-distribution.10, abundance-distribution.11, abundance-distribution.12 · trail: MB-02 §critic · from: MB-02:A-148, MB-02:C-040, MB-02:C-043, MB-02:C-060, MB-02:C-135
- **dns.33** "two phylotypes dominate soil archaea" (as a general finding)
  why: rests on Bates 2011 alone (abstract only, 2010-era 454 data, 146 soils) · instead: abundance-distribution.14 · trail: MB-02 §critic · from: MB-02:C-091
- **dns.34** "Bulk soil shows a positive abundance-occupancy relationship in amplicon data wherever tested"
  why: "wherever tested" overstates a search whose 25 hits were reviewed by title, on two partly overlapping datasets whose metrics are partly circular; the circularity caution was applied to Delgado-Baquerizo but not to Bickel and Or or Nemergut, and the positive answer is the review's own reading · instead: abundance-occupancy.9, abundance-occupancy.10 · trail: MB-02 §critic · from: MB-02:A-100, MB-02:A-151, MB-02:C-053, MB-02:C-061, MB-02:C-062, MB-02:C-123, MB-02:C-126, MB-02:C-127, MB-02:C-144, MB-02:C-145
- **dns.35** Bickel and Or's median prevalence of common versus rare classes as evidence of an interspecific abundance-occupancy relationship.
  why: a class-level contrast is a different measure from Nemergut's taxon-level relationship · instead: abundance-occupancy.4 · trail: MB-02 §critic · from: MB-02:C-137
- **dns.36** "Low-abundance taxa are routinely recorded absent where present, which by itself produces lower occupancy for rarer taxa" (as a finding of Zhou 2011)
  why: generalises from one 454 study at one Oklahoma warming site; the second clause is the reviewer's inference, and Zhou's abstract attributes low replicate overlap to random sampling without drawing the occupancy conclusion · instead: count-sampling.1, abundance-occupancy.10 · trail: MB-02 §critic · from: MB-02:A-108, MB-02:B-0337, MB-02:C-086, MB-02:C-139
- **dns.37** "Copies usually fall in stationary phase or starvation" (as a property of prokaryotes)
  why: rests largely on one laboratory's (Soppa group) abstracts and merges taxon-specific and sometimes opposite behaviours; in sources the review cites, ploidy rises in stationary phase in A. vinelandii and in slow growth in M. acetivorans · instead: genome-copies-per-cell.1, genome-copies-per-cell.16 · trail: MB-02 §critic · from: MB-02:A-135, MB-02:C-009, MB-02:C-087, MB-02:C-128, MB-02:C-129, MB-02:C-136
- **dns.38** "Strong for cultures" (genome copies per cell)
  why: apart from Pecoraro 2011 all ploidy studies were read at abstract level, and most values come from one laboratory's qPCR method; evidence is moderate, not strong · instead: genome-copies-per-cell.1, genome-copies-per-cell.2 · trail: MB-02 §critic · from: MB-02:A-028, MB-02:A-136, MB-02:C-014, MB-02:C-068, MB-02:B-0014
- **dns.39** "No direct contradictions found" and independent-laboratory ploidy measurements "not located".
  why: Pecoraro 2011, read in full, lists A. vinelandii polyploidy (40 copies in fast growth) and other non-Soppa measurements in its Table 5, and Brück 2023 reports A. vinelandii rising from 4 to 80 copies into stationary phase · instead: genome-copies-per-cell.16, genome-copies-per-cell.17 · trail: MB-02 §critic · from: MB-02:A-029, MB-02:A-031, MB-02:B-0180, MB-02:C-063, MB-02:C-130, MB-02:C-131, MB-02:C-064
- **dns.40** "Because rRNA operons sit near the origin in fast growers, 16S copies per cell scale with origin number more than with genome number"
  why: the reviewer's inference from one abstract (Couturier and Rocha 2006), presented without a reviewer's-reading label; no source in the review measures 16S copies per cell against origin number · instead: genome-copies-per-cell.18, genome-copies-per-cell.19 · trail: MB-02 §critic · from: MB-02:A-025, MB-02:C-015, MB-02:C-088, MB-02:C-140
- **dns.41** "the share of cells carrying two genomes changes over the day" (Prochlorococcus)
  why: the abstract gives no share; it states only that replication occurred in the afternoon and division at night · instead: genome-copies-per-cell.25 · trail: MB-02 §critic · from: MB-02:C-078, MB-02:C-079, MB-02:C-080
- **dns.42** That no share of single-copy cells by taxon exists for any natural community.
  why: in situ flow cytometric cell-cycle analyses of Prochlorococcus are, by method, taxon-specific measurements of the share of cells with replicated DNA; the review read only the abstract · instead: genome-copies-per-cell.26, genome-copies-per-cell.30 · trail: MB-02 §critic · from: MB-02:C-017, MB-02:C-018, MB-02:C-107
- **dns.43** "the abstract gives no per-cell shares" (H. salinarum), as if no per-cell shares were available.
  why: Breuert 2006 is open in PMC, and its full text reports single-cell CLSM and FACS distributions of genome copy number · instead: genome-copies-per-cell.12 · trail: MB-02 §critic · from: MB-02:C-069, MB-02:C-070, MB-02:C-071
- **dns.44** "Other biases (extraction, primers) are of similar or larger size and multiply with copy number"
  why: rests on McLaren 2019 read at abstract level only; the abstract does not compare their magnitude with copy-number bias · instead: copy-number-correction.14 · trail: MB-02 §critic · from: MB-02:A-046, MB-02:C-025, MB-02:C-077, MB-02:C-090, MB-02:C-132, MB-02:C-133, MB-02:C-134
- **dns.45** "eleven DNA-based mock communities fitted 7.1% better without correction"
  why: Starke 2021 computed its 7.1% on n = 10 mocks; one of the eleven was excluded · instead: copy-number-correction.12 · trail: MB-02 §critic · from: MB-02:A-044, MB-02:B-0218, MB-02:C-022, MB-02:C-065
- **dns.46** "correction changed the most abundant OTU in about 20% (human) and 31% (Earth Microbiome Project) of communities" (as an error of uncorrected data).
  why: judged against predicted, not measured, truth · instead: copy-number-correction.17 · trail: MB-02 §critic · from: MB-02:C-023, MB-02:A-045
- **dns.47** "abundant is usually above 1% [40,43,44,49]"
  why: Jia 2022 [49] uses a single rare/common cutoff and does not support "abundant above 1%" · instead: rarity-terms.4 · trail: MB-02 §critic · from: MB-02:A-061, MB-02:C-032, MB-02:C-065
- **dns.48** "only about 1% of taxa agreed by all" four core methods
  why: not a figure in the source, which gives 165 and 176 taxa as 13% and 15.85% of core assignments; the review's 1% is its own derivation · instead: threshold-sensitivity.7 · trail: MB-02 §critic · from: MB-02:A-067, MB-02:B-0277, MB-02:C-034, MB-02:C-081
- **dns.49** "occupancy-based core methods, which performed best in simulations" (listed among proposed standards as established)
  why: rests on one simulation study (Custer 2023) · instead: threshold-sensitivity.9 · trail: MB-02 §critic · from: MB-02:A-068, MB-02:C-092
- **dns.50** "Archaea carry 1 to 4 (to v5.0)" given as the whole record of the archaeal maximum.
  why: Acinas 2004 already reports a maximum of five archaeal operons; the review's sources conflict on the archaeal maximum and it does not reconcile them · instead: copy-number.2 · trail: MB-02 §critic · from: MB-02:C-002, MB-02:C-138, MB-02:A-002
- **dns.51** "Acidobacteria 1.0" presented beside large-n phyla without its n.
  why: rests on 4 genomes from 4 species; the soil correction example depends on it · instead: copy-number.4, copy-number.5 · trail: MB-02 §critic · from: MB-02:C-003, MB-02:C-089
- **dns.52** "consistent across five rrnDB generations, two independent genome surveys and two tool-development papers" (as independent replication of the 1 to 15 range)
  why: those sources draw on overlapping NCBI genome sets, so they are not independent replications · instead: copy-number.1 · trail: MB-02 §critic · from: MB-02:A-009, MB-02:C-006
- **dns.53** "up to 41% of rRNA genes in soil long-read data were unlinked" (in the answer, without its single-source flag)
  why: rests on Brewer 2020 (abstract only) alone; the body flags this, the answer does not · instead: copy-number.22 · trail: MB-02 §critic · from: MB-02:C-093, MB-02:A-007

## Gaps

- **gap.1** Same-sample comparisons of 16S amplicon data against shotgun metagenomes, culture, microscopy or FISH, or taxon-specific qPCR (beyond Jian 2020's four taxa); the only shotgun evidence is Costea 2017, known secondarily via McLaren.
  blocks: bias-consistency, departure · origin: critic coverage gap (nearest precedents named in the brief almost entirely missing) · from: MB-01:C-105, MB-01:C-106, MB-01:C-107 · src: costeaTowardsStandardsHuman2017, jianQuantitativePCRProvides2020
- **gap.2** Field sampling choices for water (volume filtered, filter pore size, prefiltration, filter storage) and for host tissue (swab versus biopsy versus lavage, plant tissue surface sterilisation): unsearched by any angle.
  blocks: sample-storage · origin: critic coverage gap; the review's search record · from: MB-01:C-108, MB-01:C-012, MB-01:B-0018, MB-01:B-0450
- **gap.3** Long-read platforms: Nanopore (ONT) full-length 16S sequencing is absent, and PacBio full-length evidence is only the developer's own claim; no independent long-read mock benchmarks.
  blocks: library-sequencing.8, denoising-clustering.21 · origin: critic coverage gap · from: MB-01:C-109, MB-01:B-0049, MB-01:B-0050 · src: callahanHighthroughputAmpliconSequencing2019
- **gap.4** A 16S-specific index-hopping measurement on patterned flow cells (NovaSeq, NextSeq 2000); the 16S rate is one preprint abstract.
  blocks: index-misassignment · origin: critic coverage gap; "not found" (bioinformatics angle) · from: MB-01:C-110, MB-01:A-122, MB-01:B-0051, MB-01:B-0052 · src: edgarUNCROSSFilteringHighfrequency2016, sinhaIndexSwitchingCauses2017
- **gap.5** Within-run read-count variation per sample after pooling, and the correlation of library size with biomass; Schloss 2024b cites two primary studies (Minich et al. 2022 on 101 fish species; Cruz et al. 2021 on an equivolumetric protocol) that the review knows only secondarily and did not open.
  blocks: reads-per-sample · origin: critic coverage gap; "not found" by all three angles · from: MB-01:C-111, MB-01:B-0053, MB-01:B-0054, MB-01:B-0017 · src: schlossRarefactionCurrentlyBest2024
- **gap.6** Measured community-average 16S copy number by environment, for example from shotgun metagenomes (16S reads normalised to single-copy marker genes), which was not searched.
  blocks: community-copy-number · origin: critic coverage gap; "not found" (lab and bioinformatics angles) · from: MB-01:C-112, MB-01:C-029
- **gap.7** Absolute per-cycle amplification efficiency of universal 16S primers on environmental extracts (soil, sediment, water, faeces); the qPCR methods literature on per-reaction efficiency and inhibition was not searched.
  blocks: pcr.10, pcr.12 · origin: critic coverage gap · from: MB-01:C-113, MB-01:B-0055, MB-01:B-0056
- **gap.8** Abundance-distribution shapes for marine or freshwater and for host-associated 16S datasets: Grilli 2020's per-biome supplementary figures and Shoemaker 2017's full text were not read, although the sources exist.
  blocks: abundance-distribution · origin: critic coverage gap; "not found" · from: MB-01:C-114, MB-01:B-0057, MB-01:B-0058 · src: grilliMacroecologicalLawsDescribe2020, shoemakerMacroecologicalTheoryMicrobial2017
- **gap.9** A Dirichlet-multinomial or overdispersion fit to 16S technical replicates, and technical replicates across depths in aquatic, plant and human non-gut samples; replicate-at-depth studies are confined to one soil laboratory (Zhou, Wen) and one mouse caecum (Barlow).
  blocks: overdispersion, replicate-agreement, count-sampling · origin: critic coverage gap; "not found" (statistics angle) · from: MB-01:C-115, MB-01:B-0059, MB-01:B-0060
- **gap.10** Contaminant-removal tools beyond decontam and SourceTracker (for example tools modelling well-to-well leakage), and independent benchmarks of decontam's prevalence mode, for low-biomass samples.
  blocks: contamination · origin: critic coverage gap · from: MB-01:C-116
- **gap.11** Primary-source benchmarks of compositional beta-diversity variants (robust Aitchison, phylogenetic isometric log-ratio) and microbiome scaling methods such as GMPR and ANCOM-BC2; coverage relies on Yang and Chen 2022 and Llorens-Rico 2021.
  blocks: compositional-methods, scaling-normalisation, beta-diversity · origin: critic coverage gap · from: MB-01:C-117
- **gap.12** A benchmark of any method for comparing samples with unequal depth or load in soil or water with measured absolute loads as truth; a known-richness mock tested across depths; and a benchmark building taxon-specific bias and load differences into the simulated truth together.
  blocks: absolute-quantification, alpha-diversity, sample-comparison · origin: critic coverage gap; "not found" (statistics angle) · from: MB-01:C-118, MB-01:C-051
- **gap.13** Archaeal evidence is thin: one archaeal-rich mock (Pinto and Raskin 2012), a copy-number range from 148 species and one run-failure case (Yeh 2018); archaeal primer bias measured against known composition is absent, and no archaeal-rich mock was found beyond Pinto and Raskin 2012 and D'Amore 2016.
  blocks: primers, copy-number.2, run-batch.1 · origin: critic coverage gap; "not found" · from: MB-01:C-119, MB-01:A-123, MB-01:B-0061, MB-01:B-0062
- **gap.14** An independent microbial amplicon benchmark of coverage-based standardisation with known truth.
  blocks: coverage-standardisation · origin: "not found" (statistics angle) · from: MB-01:B-0449, MB-01:C-050
- **gap.15** Consistency of extraction bias across real soil or water matrices, and a mock community in a soil matrix with known composition.
  blocks: bias-consistency, extraction · origin: "not found" in the D2 answer · from: MB-01:A-124, MB-01:A-125
- **gap.16** How often each workflow choice is made across the field, beyond the use of controls; a 16S-specific survey of control use.
  blocks: workflow.2, contamination.9 · origin: "not found"; critic correction · from: MB-01:A-026, MB-01:C-009, MB-01:C-005
- **gap.17** Figures that need the full text of sources whose "full text" labels the critic could not confirm: Zhou 2011's 0.06 to 5.34% spike range and its 13.1% and 5.9% discussion values, Kozich 2013's 9,913 and 2,454 reads, Haegeman 2013's 26,079 reads and 2,880 species, and Lin 2019's r2 of 0.19 and 0.61.
  blocks: bias-consistency.15, count-sampling.2, reads-per-sample.3, abundance-distribution.2, absolute-quantification.14 · origin: critic access errors; figures to recheck · from: MB-01:C-065, MB-01:C-073, MB-01:C-074, MB-01:C-076, MB-01:C-028, MB-01:C-048 · src: zhouReproducibilityQuantitationAmplicon2011, kozichDevelopmentDualindexSequencing2013, haegemanRobustEstimationMicrobial2013, linTowardsQuantitativeMicrobiome2019
- **gap.18** Zhou 2013's best-fitting soil abundance distributions in supplementary Table S3 were not read or verified.
  blocks: abundance-distribution.1, abundance-distribution.7 · origin: critic access error · from: MB-01:C-077, MB-01:C-078, MB-01:C-079 · src: zhouRandomSamplingProcess2013
- **gap.19** Kozich 2013's post-preclustering error rates for V3-V4 and V4-V5: the bioinformatics angle reports 0.10 to 0.21% and 0.36 to 0.64%, the lab angle 0.24 to 0.37% and 0.58 to 0.87% (read through a fetch-tool summary).
  blocks: library-sequencing.7 · origin: the note gives two readings of one source · from: MB-01:B-0196, MB-01:B-0197 · src: kozichDevelopmentDualindexSequencing2013
- **gap.20** Sources not obtained that bear on findings: Gohl 2016 (one-step versus two-step library preparation and cycle number on mocks), Costea 2017 (interlaboratory extraction with spike-in, used only via McLaren), Lauber 2010 (storage in soil, faeces and skin, known only via Rubin 2013), Wesolowska-Andersen 2014 (retrieved but not searched), Weiss 2014 (contamination), Kunin 2010 (sequencing-error inflation; listed as not obtained in MB-01 but used at abstract level in MB-02), Smets 2016 and Shoemaker 2017 (each listed both as used and as not obtained in MB-01).
  blocks: library-sequencing, extraction, sample-storage, contamination, alpha-diversity.9, absolute-quantification.7, abundance-distribution.4 · origin: sources not obtained that matter; conflicts between the note's lists · from: MB-01:B-0139, MB-01:B-0192 · src: gohlSystematicImprovementAmplicon2016, costeaTowardsStandardsHuman2017, lauberEffectStorageConditions2010, wesolowskaandersenChoiceBacterialDNA2014, weissTrackingDownSources2014, kuninWrinklesRareBiosphere2010, smetsMethodSimultaneousMeasurement2016, shoemakerMacroecologicalTheoryMicrobial2017
- **gap.21** MB-01's stage-2 check is triggered (per-cycle efficiency, metagenome-derived copy number, 16S index hopping on patterned flow cells, within-run read counts against load, long-read platform error); the follow-up brief is not yet written.
  blocks: pcr, community-copy-number, index-misassignment, reads-per-sample, library-sequencing · origin: stage-2 check called for a follow-up · from: MB-01:B-0076, MB-01:B-0077
- **gap.22** Polyploidy of soil and plant-associated bacteria measured outside the Soppa laboratory: Azotobacter vinelandii (40 to 80 copies, rising in stationary phase), Deinococcus radiodurans, and endoreduplicated Sinorhizobium bacteroids in nodules (Mergaert et al. 2006); ploidy of cultured soil Acidobacteriota, Verrucomicrobiota or Nitrososphaerota.
  blocks: genome-copies-per-cell · origin: critic coverage gap; "not measured" · from: MB-02:C-102, MB-02:A-034
- **gap.23** Single-cell genome-copy distributions in cultures (flow-cytometric chromosome run-out giving 1, 2, 4 and 8 chromosomes per cell, for example Skarstad, Boye and Steen 1986; Caulobacter swarmer-cell G1 shares), the direct measurements of the share of cells at one genome copy versus several.
  blocks: genome-copies-per-cell · origin: critic coverage gap · from: MB-02:C-103, MB-02:C-104, MB-02:C-105
- **gap.24** In situ cell-cycle analyses of Prochlorococcus and Synechococcus (Vaulot 1995 and successors), which report the fraction of cells in G1 versus S/G2 by taxon in natural seawater, read only at abstract level.
  blocks: genome-copies-per-cell.26, genome-copies-per-cell.30 · origin: critic coverage gap · from: MB-02:C-106, MB-02:C-107, MB-02:C-108 · src: vaulotGrowthProchlorococcusPhotosynthetic1995
- **gap.25** Ploidy of dormant forms (endospores, Streptomyces spores, Azotobacter cysts) and of non-growing small soil cells; share of single-copy cells in soil, rhizosphere or dormant natural populations; genome copies per cell for named soil taxa in situ; any direct measurement of 16S copies per cell in environmental cells.
  blocks: genome-copies-per-cell · origin: critic coverage gap; "not measured" · from: MB-02:C-109, MB-02:A-034, MB-02:A-138
- **gap.26** In situ growth measures in soil: qSIP growth rates and growth-rate potential from genomes in soil and rhizosphere (Chuckran et al. 2025 on rewetted soil; Lopez et al. 2023 on rhizosphere versus bulk soil, which reports 6.6% more rRNA operons in rhizosphere bacteria via a cited study); replication indices for soil metagenomes.
  blocks: genome-copies-per-cell, community-copy-number · origin: critic coverage gap; "not found" · from: MB-02:C-110, MB-02:A-034
- **gap.27** Soil studies using community-weighted rrn copy number (for example Nemergut et al. 2016 on succession; rhizosphere versus bulk comparisons) and soil absolute quantification (for example Smets et al. 2016) were not searched for copy-number correction or abundance distributions; no soil mock or soil cell-count benchmark of correction, and no study combining correction with ploidy.
  blocks: copy-number-correction, community-copy-number · origin: critic coverage gap; "not measured" · from: MB-02:C-111, MB-02:C-027, MB-02:A-053, MB-02:A-054 · src: nemergutDecreasesAverageBacterial2015, smetsMethodSimultaneousMeasurement2016
- **gap.28** Occupancy-based classification terms: habitat generalist versus specialist (Levins niche breadth, for example Szekely and Langenheder 2014), cosmopolitan versus endemic, and the microbial core-satellite partition (for example van der Gast et al. 2011).
  blocks: rarity-terms · origin: critic coverage gap · from: MB-02:C-038, MB-02:C-112
- **gap.29** The soil literature contrasting "abundant" and "rare" subcommunities' distribution ranges and niche breadth across regions (for example Jiao and Lu 2020; Jiao, Chen and Wei 2017), which bears on abundance versus occupancy and on threshold usage in soil; a survey of definitions within soil studies or for bulk soil and rhizosphere separately.
  blocks: rarity-terms, abundance-occupancy, threshold-sensitivity · origin: critic coverage gap; "not found" · from: MB-02:C-113, MB-02:C-114, MB-02:C-115, MB-02:A-075
- **gap.30** Global genome-resolved or metagenome-based soil datasets (for example Bahram et al. 2018) examined for taxon abundance distributions or occupancy; metagenome-based soil taxon abundance distributions.
  blocks: abundance-distribution, abundance-occupancy · origin: critic coverage gap; "not measured" · from: MB-02:C-116, MB-02:C-047, MB-02:A-095
- **gap.31** Taxon-specific cell counts in soil (FISH or CARD-FISH phylum or class shares); "no cell-count evidence" rests on a narrow search route.
  blocks: abundance-distribution.23 · origin: critic coverage gap · from: MB-02:C-117
- **gap.32** Non-soil nearest precedents for the shape of the abundance distribution that contradict the lognormal view (for example power-law tails of non-dominant plankton, Ser-Giacomi et al. 2018).
  blocks: abundance-distribution.19 · origin: critic coverage gap · from: MB-02:C-118
- **gap.33** Explicit sampling or occupancy-detection models applied to soil microbes (site-occupancy models, gamma-Poisson occupancy predictions on soil data); whether Grilli 2020's datasets include soil.
  blocks: abundance-occupancy.10, abundance-occupancy.15 · origin: critic coverage gap; "not found" · from: MB-02:C-119, MB-02:C-120, MB-02:C-121 · src: grilliMacroecologicalLawsDescribe2020
- **gap.34** Technical-replicate detection studies after the 454 era (Illumina, deeper sequencing) testing whether Zhou 2011's low replicate overlap generalises to soil.
  blocks: count-sampling.1, abundance-occupancy.10 · origin: critic coverage gap · from: MB-02:C-122
- **gap.35** Nemergut 2011's bulk-soil figures (28% versus 2%, 69% versus 8%) could not be verified by the critic, and its abstract frames the study across Earth's major habitat types; the figures should be rechecked.
  blocks: abundance-occupancy.1, abundance-occupancy.9 · origin: critic access error · from: MB-02:C-084, MB-02:C-085 · src: nemergutGlobalPatternsBiogeography2011
- **gap.36** Open full texts the review read only as abstracts: Breuert 2006 (single-cell genome-copy distributions), Brück 2023 (stationary-phase chromosome numbers) and Hildenbrand 2011 (a PMC route exists).
  blocks: genome-copies-per-cell.12, genome-copies-per-cell.13, genome-copies-per-cell.16 · origin: critic access errors · from: MB-02:C-069, MB-02:C-072, MB-02:C-076 · src: breuertRegulatedPolyploidyHalophilic2006, bruckOneAdvantageBeing2023, hildenbrandGenomeCopyNumbers2011
- **gap.37** Whether core-based analyses gained or lost the temporal effect in Custer 2023's human data: the source's text is internally inconsistent.
  blocks: threshold-sensitivity.8 · origin: critic finding · from: MB-02:C-035 · src: custerComparativeAnalysisCore2023
- **gap.38** Copy numbers of uncultured lineages without genomes (many soil Acidobacteriota, Verrucomicrobiota, Chloroflexota and candidate phyla), and 16S copy number in environmental populations of soil archaea beyond cultured or enriched Nitrososphaerota; within-species copy-number plasticity in prokaryotes.
  blocks: copy-number, copy-number-correction.23 · origin: "not measured" · from: MB-02:A-014, MB-02:A-015, MB-02:A-132, MB-02:A-055
- **gap.39** Threshold-based rarity classes compared between amplicon and metagenome data from the same soil samples, and copy-number-corrected thresholds.
  blocks: threshold-sensitivity · origin: "not found" · from: MB-02:A-076, MB-02:A-077
- **gap.40** Soil taxon abundance distributions and abundance-occupancy relationships from cell counts, copy-number- or ploidy-corrected data, rhizosphere-specific data, archaea-specific data, and bulk soil against rhizosphere within one study.
  blocks: abundance-distribution, abundance-occupancy · origin: "not measured" · from: MB-02:A-095, MB-02:A-121
- **gap.41** MB-02's stage-2 check is triggered (unsearched per-cell and growth-state evidence for soil: in situ growth measures, ploidy of dormant forms, CARD-FISH counts, soil studies weighting by rrn copy number; also occupancy-based terms and global soil metagenomes); the follow-up brief is not written.
  blocks: genome-copies-per-cell, rarity-terms, abundance-distribution · origin: stage-2 check called for a follow-up · from: MB-02:B-0084..0088

## Out of scope

- MB-01:C-003, MB-01:C-060: the critic's sub-headings ("Two corrections.", "Answer-level over-reach."), structure, not findings
- MB-01:C-052, MB-01:C-053: the critic's overall verdict on the review, an assessment of the note rather than a finding
- MB-01:C-054: the critic's record of which figures it verified against full text (provenance, kept in the result note)
- MB-01:C-080: access correction (an open PMC copy of Marotz 2019 exists), recorded in Sources
- MB-01:C-093..104: reference corrections and Crossref checks, applied in Sources
- MB-01:A-028, MB-01:A-126, MB-01:A-179, MB-01:A-286: search routes of the answers (provenance, kept in the result note)
- MB-01:A-029..031, MB-01:A-127..130, MB-01:A-180..182, MB-01:A-223, MB-01:A-224, MB-01:A-287..289: access basis of the answers (provenance; access is recorded per source in Sources)
- MB-01:A-035, MB-01:A-036, MB-01:A-051, MB-01:A-056, MB-01:A-066, MB-01:A-076, MB-01:A-081, MB-01:A-088, MB-01:A-091, MB-01:A-104, MB-01:A-107, MB-01:A-134, MB-01:A-141, MB-01:A-146, MB-01:A-154, MB-01:A-161, MB-01:A-194, MB-01:A-203, MB-01:A-244, MB-01:A-253: sub-headings and layout notes inside the answers, routing within the answer, not findings
- MB-01:A-133: single-source sensitivity remark that no other removal changes the answer; no claim of its own
- MB-02:C-031, MB-02:C-059: the critic's sub-headings ("Three corrections.", "The answers over-reach in specific places."), structure, not findings
- MB-02:C-056: the critic's overall verdict on the review, an assessment of the note rather than a finding
- MB-02:C-094..101: reference checks against Crossref, applied in Sources
- MB-02:C-142, MB-02:C-143: the critic's expectation-echo check on the brief (the brief states no expected direction), provenance of the framing
- MB-02:A-016, MB-02:A-035, MB-02:A-056, MB-02:A-078, MB-02:A-096, MB-02:A-122, MB-02:A-133, MB-02:A-139: access basis of the answers (provenance; access is recorded per source in Sources)

## Sources

```bibtex
@article{abellanschneyderPrimerPipelinesParameters2021,
  author = {Abellan-Schneyder, Isabel and Matchado, Monica S. and Reitmeier, Sandra and Sommer, Alina and Sewald, Zeno and Baumbach, Jan and List, Markus and Neuhaus, Klaus},
  title = {Primer, pipelines, parameters: issues in 16S rRNA gene sequencing},
  journal = {mSphere},
  volume = {6},
  number = {1},
  pages = {e01202-20},
  year = {2021},
  doi = {10.1128/mSphere.01202-20},
  note = {access: full_text (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Abellan-Schneyder 2021}
}

@article{acinasPCRinducedSequenceArtifacts2005,
  author = {Acinas, Silvia G. and Sarma-Rupavtarm, Ramahi and Klepac-Ceraj, Vanja and Polz, Martin F.},
  title = {PCR-induced sequence artifacts and bias: insights from comparison of two 16S rRNA clone libraries constructed from the same sample},
  journal = {Applied and Environmental Microbiology},
  volume = {71},
  number = {12},
  pages = {8966-8969},
  year = {2005},
  doi = {10.1128/AEM.71.12.8966-8969.2005},
  note = {access: abstract_only (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Acinas 2005}
}

@article{albertsenBackBasicsInfluence2015,
  author = {Albertsen, Mads and Karst, Søren M. and Ziegler, Anja S. and Kirkegaard, Rasmus H. and Nielsen, Per H.},
  title = {Back to basics: the influence of DNA extraction and primer choice on phylogenetic analysis of activated sludge communities},
  journal = {PLOS ONE},
  volume = {10},
  number = {7},
  pages = {e0132783},
  year = {2015},
  doi = {10.1371/journal.pone.0132783},
  note = {access: full_text (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Albertsen 2015}
}

@article{almeidaBenchmarkingTaxonomicAssignments2018,
  author = {Almeida, Alexandre and Mitchell, Alex L. and Tarkowska, Aleksandra and Finn, Robert D.},
  title = {Benchmarking taxonomic assignments based on 16S rRNA gene profiling of the microbiota from commonly sampled environments},
  journal = {GigaScience},
  volume = {7},
  number = {5},
  pages = {giy054},
  year = {2018},
  doi = {10.1093/gigascience/giy054},
  note = {access: full_text (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Almeida 2018}
}

@article{alroyCoveragebasedRarefactionFails2026,
  author = {Alroy, John},
  title = {Coverage-based rarefaction fails to quantify relative species richness},
  journal = {Oikos},
  pages = {e11607},
  year = {2026},
  doi = {10.1002/oik.11607},
  note = {access: abstract_only (DOI checked on Crossref by the synthesis agent) (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Alroy 2026; published online 2026-09-14; volume not yet assigned}
}

@article{andersDifferentialExpressionAnalysis2010,
  author = {Anders, Simon and Huber, Wolfgang},
  title = {Differential expression analysis for sequence count data},
  journal = {Genome Biology},
  volume = {11},
  number = {10},
  pages = {R106},
  year = {2010},
  doi = {10.1186/gb-2010-11-10-r106},
  note = {access: abstract_only (INDIRECT) (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Anders and Huber 2010}
}

@article{barlowQuantitativeSequencingFramework2020,
  author = {Barlow, Jacob T. and Bogatyrev, Said R. and Ismagilov, Rustem F.},
  title = {A quantitative sequencing framework for absolute abundance measurements of mucosal and lumenal microbial communities},
  journal = {Nature Communications},
  volume = {11},
  pages = {2590},
  year = {2020},
  doi = {10.1038/s41467-020-16224-6},
  note = {access: full_text (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Barlow 2020}
}

@article{beuleImprovedNormalizationSpecies2020,
  author = {Beule, Lukas and Karlovsky, Petr},
  title = {Improved normalization of species count data in ecology by scaling with ranked subsampling (SRS): application to microbial communities},
  journal = {PeerJ},
  volume = {8},
  pages = {e9593},
  year = {2020},
  doi = {10.7717/peerj.9593},
  note = {access: abstract_only (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Beule and Karlovsky 2020}
}

@article{bokulichQualityfilteringVastlyImproves2013,
  author = {Bokulich, Nicholas A. and Subramanian, Sathish and Faith, Jeremiah J. and Gevers, Dirk and Gordon, Jeffrey I. and Knight, Rob and Mills, David A. and Caporaso, J. Gregory},
  title = {Quality-filtering vastly improves diversity estimates from Illumina amplicon sequencing},
  journal = {Nature Methods},
  volume = {10},
  number = {1},
  pages = {57-59},
  year = {2013},
  doi = {10.1038/nmeth.2276},
  note = {access: full_text (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Bokulich 2013}
}

@article{bokulichOptimizingTaxonomicClassification2018,
  author = {Bokulich, Nicholas A. and Kaehler, Benjamin D. and Rideout, Jai Ram and Dillon, Matthew and Bolyen, Evan and Knight, Rob and Huttley, Gavin A. and Caporaso, J. Gregory},
  title = {Optimizing taxonomic classification of marker-gene amplicon sequences with QIIME 2's q2-feature-classifier plugin},
  journal = {Microbiome},
  volume = {6},
  pages = {90},
  year = {2018},
  doi = {10.1186/s40168-018-0470-z},
  note = {access: full_text (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Bokulich 2018}
}

@article{bonkPCRbasedQuantificationTaxaspecific2018,
  author = {Bonk, Fabian and Popp, Denny and Harms, Hauke and Centler, Florian},
  title = {PCR-based quantification of taxa-specific abundances in microbial communities: quantifying and avoiding common pitfalls},
  journal = {Journal of Microbiological Methods},
  volume = {153},
  pages = {139-147},
  year = {2018},
  doi = {10.1016/j.mimet.2018.09.015},
  note = {access: abstract_only (MB-01); type: peer reviewed review (MB-01); cited as: MB-01 Bonk 2018}
}

@article{brooksTruthMetagenomicsQuantifying2015,
  author = {Brooks, J. Paul and Edwards, David J. and Harwich, Michael D. Jr and Rivera, Maria C. and Fettweis, Jennifer M. and Serrano, Myrna G. and Reris, Robert A. and Sheth, Nihar U. and Huang, Bernice and Girerd, Philippe and Vaginal Microbiome Consortium and Strauss, Jerome F. 3rd and Jefferson, Kimberly K. and Buck, Gregory A.},
  title = {The truth about metagenomics: quantifying and counteracting bias in 16S rRNA studies},
  journal = {BMC Microbiology},
  volume = {15},
  pages = {66},
  year = {2015},
  doi = {10.1186/s12866-015-0351-6},
  note = {access: full_text (title corrected against Crossref) (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Brooks 2015; correction: title corrected to 'metagenomics' against Crossref (MB-01); Crossref puts the consortium entry first with no family name, the review places it after Girerd (MB-01 critic: minor order difference)}
}

@article{bullardEvaluationStatisticalMethods2010,
  author = {Bullard, James H. and Purdom, Elizabeth and Hansen, Kasper D. and Dudoit, Sandrine},
  title = {Evaluation of statistical methods for normalization and differential expression in mRNA-Seq experiments},
  journal = {BMC Bioinformatics},
  volume = {11},
  pages = {94},
  year = {2010},
  doi = {10.1186/1471-2105-11-94},
  note = {access: abstract_only (INDIRECT) (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Bullard 2010}
}

@article{pereiraComparisonNormalizationMethods2018,
  author = {Buongermino Pereira, Mariana and Wallroth, Mikael and Jonsson, Viktor and Kristiansson, Erik},
  title = {Comparison of normalization methods for the analysis of metagenomic gene abundance data},
  journal = {BMC Genomics},
  volume = {19},
  pages = {274},
  year = {2018},
  doi = {10.1186/s12864-018-4637-6},
  note = {access: abstract_only (INDIRECT) (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Buongermino Pereira 2018}
}

@article{calgaroAssessmentStatisticalMethods2020,
  author = {Calgaro, Matteo and Romualdi, Chiara and Waldron, Levi and Risso, Davide and Vitulo, Nicola},
  title = {Assessment of statistical methods from single cell, bulk RNA-seq, and metagenomics applied to microbiome data},
  journal = {Genome Biology},
  volume = {21},
  pages = {191},
  year = {2020},
  doi = {10.1186/s13059-020-02104-1},
  note = {access: abstract_only (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Calgaro 2020}
}

@article{callahanDADA2HighresolutionSample2016,
  author = {Callahan, Benjamin J. and McMurdie, Paul J. and Rosen, Michael J. and Han, Andrew W. and Johnson, Amy Jo A. and Holmes, Susan P.},
  title = {DADA2: High-resolution sample inference from Illumina amplicon data},
  journal = {Nature Methods},
  volume = {13},
  number = {7},
  pages = {581-583},
  year = {2016},
  doi = {10.1038/nmeth.3869},
  note = {access: full_text (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Callahan 2016}
}

@article{callahanHighthroughputAmpliconSequencing2019,
  author = {Callahan, Benjamin J. and Wong, Joan and Heiner, Cheryl and Oh, Steve and Theriot, Casey M. and Gulati, Ajay S. and McGill, Sarah K. and Dougherty, Michael K.},
  title = {High-throughput amplicon sequencing of the full-length 16S rRNA gene with single-nucleotide resolution},
  journal = {Nucleic Acids Research},
  volume = {47},
  number = {18},
  pages = {e103},
  year = {2019},
  doi = {10.1093/nar/gkz569},
  note = {access: full_text (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Callahan 2019}
}

@article{cameronEnhancingDiversityAnalysis2021,
  author = {Cameron, Ellen S. and Schmidt, Philip J. and Tremblay, Benjamin J.-M. and Emelko, Monica B. and Müller, Kirsten M.},
  title = {Enhancing diversity analysis by repeatedly rarefying next generation sequencing data describing microbial communities},
  journal = {Scientific Reports},
  volume = {11},
  pages = {22302},
  year = {2021},
  doi = {10.1038/s41598-021-01636-1},
  note = {access: full_text (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Cameron 2021}
}

@article{cariniRelicDNAAbundant2016,
  author = {Carini, Paul and Marsden, Patrick J. and Leff, Jonathan W. and Morgan, Emily E. and Strickland, Michael S. and Fierer, Noah},
  title = {Relic DNA is abundant in soil and obscures estimates of soil microbial diversity},
  journal = {Nature Microbiology},
  volume = {2},
  number = {3},
  pages = {16242},
  year = {2016},
  doi = {10.1038/nmicrobiol.2016.242},
  note = {access: abstract_only (MB-01), abstract_only (MB-02); type: peer reviewed (MB-01); cited as: MB-01 Carini 2016, MB-02 [77]}
}

@article{carusoPerformanceMicrobiomeSequence2019,
  author = {Caruso, Vincent and Song, Xubo and Asquith, Mark and Karstens, Lisa},
  title = {Performance of microbiome sequence inference methods in environments with varying biomass},
  journal = {mSystems},
  volume = {4},
  number = {1},
  pages = {e00163-18},
  year = {2019},
  doi = {10.1128/mSystems.00163-18},
  note = {access: full_text (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Caruso 2019}
}

@article{chaoCoveragebasedRarefactionExtrapolation2012,
  author = {Chao, Anne and Jost, Lou},
  title = {Coverage-based rarefaction and extrapolation: standardizing samples by completeness rather than size},
  journal = {Ecology},
  volume = {93},
  number = {12},
  pages = {2533-2547},
  year = {2012},
  doi = {10.1890/11-1952.1},
  note = {access: full_text (via third-party PDF https://www.davidzeleny.net/wiki/lib/exe/fetch.php/vegecol:materials:chao-jost2012_ecology.pdf, accessed 2026-10-20; INDIRECT) (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Chao and Jost 2012}
}

@article{chaoRarefactionExtrapolationHill2014,
  author = {Chao, Anne and Gotelli, Nicholas J. and Hsieh, T. C. and Sander, Elizabeth L. and Ma, K. H. and Colwell, Robert K. and Ellison, Aaron M.},
  title = {Rarefaction and extrapolation with Hill numbers: a framework for sampling and estimation in species diversity studies},
  journal = {Ecological Monographs},
  volume = {84},
  number = {1},
  pages = {45-67},
  year = {2014},
  doi = {10.1890/13-0133.1},
  note = {access: full_text (via author PDF https://www.uvm.edu/~ngotelli/manuscriptpdfs/ChaoHill.pdf, accessed 2026-10-20; INDIRECT) (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Chao 2014}
}

@article{chiarelloRankingBiasesChoice2022,
  author = {Chiarello, Marlène and McCauley, Mark and Villéger, Sébastien and Jackson, Colin R.},
  title = {Ranking the biases: the choice of OTUs vs. ASVs in 16S rRNA amplicon data analysis has stronger effects on diversity measures than rarefaction and OTU identity threshold},
  journal = {PLOS ONE},
  volume = {17},
  number = {2},
  pages = {e0264443},
  year = {2022},
  doi = {10.1371/journal.pone.0264443},
  note = {access: full_text (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Chiarello 2022}
}

@article{chiuEstimatingComparingMicrobial2016,
  author = {Chiu, Chun-Huo and Chao, Anne},
  title = {Estimating and comparing microbial diversity in the presence of sequencing errors},
  journal = {PeerJ},
  volume = {4},
  pages = {e1634},
  year = {2016},
  doi = {10.7717/peerj.1634},
  note = {access: abstract_only (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Chiu and Chao 2016}
}

@article{costelloCharacterizationRemediationSample2018,
  author = {Costello, Maura and Fleharty, Mark and Abreu, Justin and Farjoun, Yossi and Ferriera, Steven and Holmes, Laurie and Granger, Brian and Green, Lisa and Howd, Tom and Mason, Tamara and Vicente, Gina and Dasilva, Michael and Brodeur, Wendy and DeSmet, Timothy and Dodge, Sheila and Lennon, Niall J. and Gabriel, Stacey},
  title = {Characterization and remediation of sample index swaps by non-redundant dual indexing on massively parallel sequencing platforms},
  journal = {BMC Genomics},
  volume = {19},
  pages = {332},
  year = {2018},
  doi = {10.1186/s12864-018-4703-0},
  note = {access: full_text (INDIRECT) (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Costello 2018}
}

@article{damoreComprehensiveBenchmarkingStudy2016,
  author = {D'Amore, Rosalinda and Ijaz, Umer Zeeshan and Schirmer, Melanie and Kenny, John G. and Gregory, Richard and Darby, Alistair C. and Shakya, Migun and Podar, Mircea and Quince, Christopher and Hall, Neil},
  title = {A comprehensive benchmarking study of protocols and sequencing platforms for 16S rRNA community profiling},
  journal = {BMC Genomics},
  volume = {17},
  pages = {55},
  year = {2016},
  doi = {10.1186/s12864-015-2194-9},
  note = {access: full_text (MB-01); type: peer reviewed (MB-01); cited as: MB-01 D'Amore 2016}
}

@article{davisSimpleStatisticalIdentification2018,
  author = {Davis, Nicole M. and Proctor, Diana M. and Holmes, Susan P. and Relman, David A. and Callahan, Benjamin J.},
  title = {Simple statistical identification and removal of contaminant sequences in marker-gene and metagenomics data},
  journal = {Microbiome},
  volume = {6},
  pages = {226},
  year = {2018},
  doi = {10.1186/s40168-018-0605-2},
  note = {access: full_text (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Davis 2018}
}

@article{dengNonparametricRichnessEstimators2024,
  author = {Deng, Yongcui and Umbach, Alexander K. and Neufeld, Josh D.},
  title = {Nonparametric richness estimators Chao1 and ACE must not be used with amplicon sequence variant data},
  journal = {The ISME Journal},
  volume = {18},
  number = {1},
  pages = {wrae106},
  year = {2024},
  doi = {10.1093/ismejo/wrae106},
  note = {access: full_text (DOI checked by the synthesis agent) (MB-01); type: peer reviewed perspective (MB-01); cited as: MB-01 Deng 2024}
}

@article{dyrhovdenManagingContaminationDiverse2021,
  author = {Dyrhovden, Ruben and Rippin, Martin and Øvrebø, Kjell Kåre and Nygaard, Randi M. and Ulvestad, Elling and Kommedal, Øyvind},
  title = {Managing contamination and diverse bacterial loads in 16S rRNA deep sequencing of clinical samples: implications of the law of small numbers},
  journal = {mBio},
  volume = {12},
  number = {3},
  pages = {e00598-21},
  year = {2021},
  doi = {10.1128/mBio.00598-21},
  note = {access: full_text (DOI checked by the synthesis agent) (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Dyrhovden 2021}
}

@article{edgarUNCROSSFilteringHighfrequency2016,
  author = {Edgar, Robert C.},
  title = {UNCROSS: filtering of high-frequency cross-talk in 16S amplicon reads},
  journal = {bioRxiv},
  pages = {088666},
  year = {2016},
  doi = {10.1101/088666},
  note = {access: abstract_only (MB-01); type: PREPRINT (MB-01); cited as: MB-01 Edgar 2016a}
}

@article{edgarUCHIME2ImprovedChimera2016,
  author = {Edgar, Robert C.},
  title = {UCHIME2: improved chimera prediction for amplicon sequencing},
  journal = {bioRxiv},
  pages = {074252},
  year = {2016},
  doi = {10.1101/074252},
  note = {access: abstract_only (MB-01); type: PREPRINT (MB-01); cited as: MB-01 Edgar 2016b}
}

@article{edgarUCHIMEImprovesSensitivity2011,
  author = {Edgar, Robert C. and Haas, Brian J. and Clemente, Jose C. and Quince, Christopher and Knight, Rob},
  title = {UCHIME improves sensitivity and speed of chimera detection},
  journal = {Bioinformatics},
  volume = {27},
  number = {16},
  pages = {2194-2200},
  year = {2011},
  doi = {10.1093/bioinformatics/btr381},
  note = {access: full_text (per bioinformatics angle) (MB-01); type: peer reviewed (MB-01); not cited; cited as: MB-01 Edgar 2011}
}

@article{edgarAccuracyMicrobialCommunity2017,
  author = {Edgar, Robert C.},
  title = {Accuracy of microbial community diversity estimated by closed- and open-reference OTUs},
  journal = {PeerJ},
  volume = {5},
  pages = {e3889},
  year = {2017},
  doi = {10.7717/peerj.3889},
  note = {access: full_text (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Edgar 2017a}
}

@article{edgarUNBIASAttemptCorrect2017,
  author = {Edgar, Robert C.},
  title = {UNBIAS: an attempt to correct abundance bias in 16S sequencing, with limited success},
  journal = {bioRxiv},
  pages = {124149},
  year = {2017},
  doi = {10.1101/124149},
  note = {access: abstract_only (DOI checked by the synthesis agent) (MB-01), abstract_only (MB-02); type: PREPRINT (MB-01); cited as: MB-01 Edgar 2017b, MB-02 [31]}
}

@article{edgarUpdating97Identity2018,
  author = {Edgar, Robert C.},
  title = {Updating the 97% identity threshold for 16S ribosomal RNA OTUs},
  journal = {Bioinformatics},
  volume = {34},
  number = {14},
  pages = {2371-2375},
  year = {2018},
  doi = {10.1093/bioinformatics/bty113},
  note = {access: abstract_only (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Edgar 2018a}
}

@article{edgarAccuracyTaxonomyPrediction2018,
  author = {Edgar, Robert C.},
  title = {Accuracy of taxonomy prediction for 16S rRNA and fungal ITS sequences},
  journal = {PeerJ},
  volume = {6},
  pages = {e4652},
  year = {2018},
  doi = {10.7717/peerj.4652},
  note = {access: full_text (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Edgar 2018b}
}

@article{edgarTaxonomyAnnotationGuide2018,
  author = {Edgar, Robert},
  title = {Taxonomy annotation and guide tree errors in 16S rRNA databases},
  journal = {PeerJ},
  volume = {6},
  pages = {e5030},
  year = {2018},
  doi = {10.7717/peerj.5030},
  note = {access: full_text (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Edgar 2018c}
}

@article{edgarErrorFilteringPair2015,
  author = {Edgar, Robert C. and Flyvbjerg, Henrik},
  title = {Error filtering, pair assembly and error correction for next-generation sequencing reads},
  journal = {Bioinformatics},
  volume = {31},
  number = {21},
  pages = {3476-3482},
  year = {2015},
  doi = {10.1093/bioinformatics/btv401},
  note = {access: abstract_only (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Edgar and Flyvbjerg 2015}
}

@article{eisenhoferContaminationLowMicrobial2019,
  author = {Eisenhofer, Raphael and Minich, Jeremiah J. and Marotz, Clarisse and Cooper, Alan and Knight, Rob and Weyrich, Laura S.},
  title = {Contamination in low microbial biomass microbiome studies: issues and recommendations},
  journal = {Trends in Microbiology},
  volume = {27},
  number = {2},
  pages = {105-117},
  year = {2019},
  doi = {10.1016/j.tim.2018.11.003},
  note = {access: abstract_only (MB-01); type: peer reviewed review (MB-01); cited as: MB-01 Eisenhofer 2019}
}

@article{eslingAccurateMultiplexingFiltering2015,
  author = {Esling, Philippe and Lejzerowicz, Franck and Pawlowski, Jan},
  title = {Accurate multiplexing and filtering for high-throughput amplicon-sequencing},
  journal = {Nucleic Acids Research},
  volume = {43},
  number = {5},
  pages = {2513-2524},
  year = {2015},
  doi = {10.1093/nar/gkv107},
  note = {access: full_text (INDIRECT) (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Esling 2015}
}

@article{fitzpatrickChloroplastSequenceVariation2018,
  author = {Fitzpatrick, Connor R. and Lu-Irving, Patricia and Copeland, Julia and Guttman, David S. and Wang, Pauline W. and Baltrus, David A. and Dlugosch, Katrina M. and Johnson, Marc T. J.},
  title = {Chloroplast sequence variation and the efficacy of peptide nucleic acids for blocking host amplification in plant microbiome studies},
  journal = {Microbiome},
  volume = {6},
  pages = {144},
  year = {2018},
  doi = {10.1186/s40168-018-0534-0},
  note = {access: full_text (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Fitzpatrick 2018}
}

@article{fouhy16SRRNAGene2016,
  author = {Fouhy, Fiona and Clooney, Adam G. and Stanton, Catherine and Claesson, Marcus J. and Cotter, Paul D.},
  title = {16S rRNA gene sequencing of mock microbial populations: impact of DNA extraction method, primer choice and sequencing platform},
  journal = {BMC Microbiology},
  volume = {16},
  pages = {123},
  year = {2016},
  doi = {10.1186/s12866-016-0738-z},
  note = {access: full_text (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Fouhy 2016}
}

@article{frostegardQuantificationBiasRelated1999,
  author = {Frostegård, Åsa and Courtois, Sophie and Ramisse, Vincent and Clerc, Sylvie and Bernillon, Dominique and Le Gall, Francoise and Jeannin, Pascale and Nesme, Xavier and Simonet, Pascal},
  title = {Quantification of bias related to the extraction of DNA directly from soils},
  journal = {Applied and Environmental Microbiology},
  volume = {65},
  number = {12},
  pages = {5409-5420},
  year = {1999},
  doi = {10.1128/AEM.65.12.5409-5420.1999},
  note = {access: abstract_only (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Frostegård 1999; correction: third author and Le Gall corrected to Crossref's 'Vincent Ramisse' and 'Francoise Le Gall' (MB-01 critic)}
}

@article{galazzoHowCountOur2020,
  author = {Galazzo, Gianluca and van Best, Niels and Benedikter, Birke J. and Janssen, Kevin and Bervoets, Liene and Driessen, Christel and Oomen, Melissa and Lucchesi, Mayk and van Eijck, Pascalle H. and Becker, Heike E. F. and Hornef, Mathias W. and Savelkoul, Paul H. and Stassen, Frank R. M. and Wolffs, Petra F. and Penders, John},
  title = {How to count our microbes? The effect of different quantitative microbiome profiling approaches},
  journal = {Frontiers in Cellular and Infection Microbiology},
  volume = {10},
  pages = {403},
  year = {2020},
  doi = {10.3389/fcimb.2020.00403},
  note = {access: full_text (DOI checked by the synthesis agent) (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Galazzo 2020}
}

@article{gibbonsCorrectingBatchEffects2018,
  author = {Gibbons, Sean M. and Duvallet, Claire and Alm, Eric J.},
  title = {Correcting for batch effects in case-control microbiome studies},
  journal = {PLOS Computational Biology},
  volume = {14},
  number = {4},
  pages = {e1006102},
  year = {2018},
  doi = {10.1371/journal.pcbi.1006102},
  note = {access: abstract_only (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Gibbons 2018}
}

@article{gihringMassivelyParallelRRNA2012,
  author = {Gihring, Thomas M. and Green, Stefan J. and Schadt, Christopher W.},
  title = {Massively parallel rRNA gene sequencing exacerbates the potential for biased community diversity comparisons due to variable library sizes},
  journal = {Environmental Microbiology},
  volume = {14},
  number = {2},
  pages = {285-290},
  year = {2012},
  doi = {10.1111/j.1462-2920.2011.02550.x},
  note = {access: abstract_only (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Gihring 2012}
}

@article{glassmanBroadscaleEcologicalPatterns2018,
  author = {Glassman, Sydney I. and Martiny, Jennifer B. H.},
  title = {Broadscale ecological patterns are robust to use of exact sequence variants versus operational taxonomic units},
  journal = {mSphere},
  volume = {3},
  number = {4},
  pages = {e00148-18},
  year = {2018},
  doi = {10.1128/mSphere.00148-18},
  note = {access: full_text (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Glassman and Martiny 2018}
}

@article{gloorMicrobiomeDatasetsCompositional2017,
  author = {Gloor, Gregory B. and Macklaim, Jean M. and Pawlowsky-Glahn, Vera and Egozcue, Juan J.},
  title = {Microbiome datasets are compositional: and this is not optional},
  journal = {Frontiers in Microbiology},
  volume = {8},
  pages = {2224},
  year = {2017},
  doi = {10.3389/fmicb.2017.02224},
  note = {access: abstract_only (MB-01); type: peer reviewed mini review (MB-01); cited as: MB-01 Gloor 2017}
}

@article{gotelliQuantifyingBiodiversityProcedures2001,
  author = {Gotelli, Nicholas J. and Colwell, Robert K.},
  title = {Quantifying biodiversity: procedures and pitfalls in the measurement and comparison of species richness},
  journal = {Ecology Letters},
  volume = {4},
  number = {4},
  pages = {379-391},
  year = {2001},
  doi = {10.1046/j.1461-0248.2001.00230.x},
  note = {access: abstract_only (INDIRECT) (MB-01); type: peer reviewed review (MB-01); cited as: MB-01 Gotelli and Colwell 2001}
}

@article{grilliMacroecologicalLawsDescribe2020,
  author = {Grilli, Jacopo},
  title = {Macroecological laws describe variation and diversity in microbial communities},
  journal = {Nature Communications},
  volume = {11},
  pages = {4743},
  year = {2020},
  doi = {10.1038/s41467-020-18529-y},
  note = {access: full_text (partly re-opened by the synthesis agent) (MB-01), full_text (MB-02); type: peer reviewed (MB-01); cited as: MB-01 Grilli 2020, MB-02 [72]}
}

@article{haasChimeric16SRRNA2011,
  author = {Haas, Brian J. and Gevers, Dirk and Earl, Ashlee M. and Feldgarden, Mike and Ward, Doyle V. and Giannoukos, Georgia and Ciulla, Dawn and Tabbaa, Diana and Highlander, Sarah K. and Sodergren, Erica and Methé, Barbara and DeSantis, Todd Z. and The Human Microbiome Consortium and Petrosino, Joseph F. and Knight, Rob and Birren, Bruce W.},
  title = {Chimeric 16S rRNA sequence formation and detection in Sanger and 454-pyrosequenced PCR amplicons},
  journal = {Genome Research},
  volume = {21},
  number = {3},
  pages = {494-504},
  year = {2011},
  doi = {10.1101/gr.112730.110},
  note = {access: full_text (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Haas 2011}
}

@article{haegemanRobustEstimationMicrobial2013,
  author = {Haegeman, Bart and Hamelin, Jérôme and Moriarty, John and Neal, Peter and Dushoff, Jonathan and Weitz, Joshua S.},
  title = {Robust estimation of microbial diversity in theory and in practice},
  journal = {The ISME Journal},
  volume = {7},
  number = {6},
  pages = {1092-1101},
  year = {2013},
  doi = {10.1038/ismej.2013.10},
  note = {access: full_text (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Haegeman 2013}
}

@article{harrisonDirichletmultinomialModellingOutperforms2020,
  author = {Harrison, Joshua G. and Calder, W. John and Shastry, Vivaswat and Buerkle, C. Alex},
  title = {Dirichlet-multinomial modelling outperforms alternatives for analysis of microbiome and other ecological count data},
  journal = {Molecular Ecology Resources},
  volume = {20},
  number = {2},
  pages = {481-497},
  year = {2020},
  doi = {10.1111/1755-0998.13128},
  note = {access: abstract_only (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Harrison 2020}
}

@article{harrisonQuestAbsoluteAbundance2020,
  author = {Harrison, Joshua G. and Calder, W. John and Shuman, Bryan and Buerkle, C. Alex},
  title = {The quest for absolute abundance: the use of internal standards for DNA-based community ecology},
  journal = {Molecular Ecology Resources},
  volume = {21},
  number = {1},
  pages = {30-43},
  year = {2021},
  doi = {10.1111/1755-0998.13247},
  note = {access: abstract_only (MB-01); type: peer reviewed review (MB-01); cited as: MB-01 Harrison 2021}
}

@article{hawinkelBrokenPromiseMicrobiome2019,
  author = {Hawinkel, Stijn and Mattiello, Federico and Bijnens, Luc and Thas, Olivier},
  title = {A broken promise: microbiome differential abundance methods do not control the false discovery rate},
  journal = {Briefings in Bioinformatics},
  volume = {20},
  number = {1},
  pages = {210-221},
  year = {2019},
  doi = {10.1093/bib/bbx104},
  note = {access: abstract_only (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Hawinkel 2019}
}

@article{hongRarefyNotRarefy2022,
  author = {Hong, Johnny and Karaoz, Ulas and de Valpine, Perry and Fithian, William},
  title = {To rarefy or not to rarefy: robustness and efficiency trade-offs of rarefying microbiome data},
  journal = {Bioinformatics},
  volume = {38},
  number = {9},
  pages = {2389-2396},
  year = {2022},
  doi = {10.1093/bioinformatics/btac127},
  note = {access: full_text (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Hong 2022}
}

@article{hornungIssuesCurrentStandards2019,
  author = {Hornung, Bastian V. H. and Zwittink, Romy D. and Kuijper, Ed J.},
  title = {Issues and current standards of controls in microbiome research},
  journal = {FEMS Microbiology Ecology},
  volume = {95},
  number = {5},
  pages = {fiz045},
  year = {2019},
  doi = {10.1093/femsec/fiz045},
  note = {access: full_text (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Hornung 2019}
}

@article{jianQuantitativePCRProvides2020,
  author = {Jian, Ching and Luukkonen, Panu and Yki-Järvinen, Hannele and Salonen, Anne and Korpela, Katri},
  title = {Quantitative PCR provides a simple and accessible method for quantitative microbiota profiling},
  journal = {PLOS ONE},
  volume = {15},
  number = {1},
  pages = {e0227285},
  year = {2020},
  doi = {10.1371/journal.pone.0227285},
  note = {access: full_text (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Jian 2020}
}

@article{johnsonEvaluation16SRRNA2019,
  author = {Johnson, Jethro S. and Spakowicz, Daniel J. and Hong, Bo-Young and Petersen, Lauren M. and Demkowicz, Patrick and Chen, Lei and Leopold, Shana R. and Hanson, Blake M. and Agresta, Hanako O. and Gerstein, Mark and Sodergren, Erica and Weinstock, George M.},
  title = {Evaluation of 16S rRNA gene sequencing for species and strain-level microbiome analysis},
  journal = {Nature Communications},
  volume = {10},
  pages = {5029},
  year = {2019},
  doi = {10.1038/s41467-019-13036-1},
  note = {access: full_text (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Johnson 2019}
}

@article{joosDaringDifferentialMetabarcoding2020,
  author = {Joos, Lisa and Beirinckx, Stien and Haegeman, Annelies and Debode, Jane and Vandecasteele, Bart and Baeyen, Steve and Goormachtig, Sofie and Clement, Lieven and De Tender, Caroline},
  title = {Daring to be differential: metabarcoding analysis of soil and plant-related microbial communities using amplicon sequence variants and operational taxonomical units},
  journal = {BMC Genomics},
  volume = {21},
  pages = {733},
  year = {2020},
  doi = {10.1186/s12864-020-07126-4},
  note = {access: full_text (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Joos 2020}
}

@article{kaehlerSpeciesAbundanceInformation2019,
  author = {Kaehler, Benjamin D. and Bokulich, Nicholas A. and McDonald, Daniel and Knight, Rob and Caporaso, J. Gregory and Huttley, Gavin A.},
  title = {Species abundance information improves sequence taxonomy classification accuracy},
  journal = {Nature Communications},
  volume = {10},
  pages = {4643},
  year = {2019},
  doi = {10.1038/s41467-019-12669-6},
  note = {access: full_text (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Kaehler 2019}
}

@article{karstensControllingContaminantsLowbiomass2019,
  author = {Karstens, Lisa and Asquith, Mark and Davin, Sean and Fair, Damien and Gregory, W. Thomas and Wolfe, Alan J. and Braun, Jonathan and McWeeney, Shannon},
  title = {Controlling for contaminants in low-biomass 16S rRNA gene sequencing experiments},
  journal = {mSystems},
  volume = {4},
  number = {4},
  pages = {e00290-19},
  year = {2019},
  doi = {10.1128/mSystems.00290-19},
  note = {access: full_text (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Karstens 2019}
}

@article{kaulAnalysisMicrobiomeData2017,
  author = {Kaul, Abhishek and Mandal, Siddhartha and Davidov, Ori and Peddada, Shyamal D.},
  title = {Analysis of microbiome data in the presence of excess zeros},
  journal = {Frontiers in Microbiology},
  volume = {8},
  pages = {2114},
  year = {2017},
  doi = {10.3389/fmicb.2017.02114},
  note = {access: abstract_only (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Kaul 2017}
}

@article{kebschullSourcesPCRinducedDistortions2015,
  author = {Kebschull, Justus M. and Zador, Anthony M.},
  title = {Sources of PCR-induced distortions in high-throughput sequencing data sets},
  journal = {Nucleic Acids Research},
  volume = {43},
  number = {21},
  pages = {e143},
  year = {2015},
  doi = {10.1093/nar/gkv717},
  note = {access: full_text (INDIRECT) (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Kebschull and Zador 2015; correction: Crossref lacks volume/issue; the review's values are the published ones (MB-01 critic)}
}

@article{kellyUnderstandingPCRProcesses2019,
  author = {Kelly, Ryan P. and Shelton, Andrew Olaf and Gallego, Ramón},
  title = {Understanding PCR processes to draw meaningful conclusions from environmental DNA studies},
  journal = {Scientific Reports},
  volume = {9},
  pages = {12133},
  year = {2019},
  doi = {10.1038/s41598-019-48546-x},
  note = {access: full_text (INDIRECT) (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Kelly 2019}
}

@article{kembelIncorporating16SGene2012,
  author = {Kembel, Steven W. and Wu, Martin and Eisen, Jonathan A. and Green, Jessica L.},
  title = {Incorporating 16S gene copy number information improves estimates of microbial diversity and abundance},
  journal = {PLOS Computational Biology},
  volume = {8},
  number = {10},
  pages = {e1002743},
  year = {2012},
  doi = {10.1371/journal.pcbi.1002743},
  note = {access: full_text (MB-01), full_text (MB-02); type: peer reviewed (MB-01); cited as: MB-01 Kembel 2012, MB-02 [28]}
}

@article{kennedyEvaluatingBiasIlluminabased2014,
  author = {Kennedy, Katherine and Hall, Michael W. and Lynch, Michael D. J. and Moreno-Hagelsieb, Gabriel and Neufeld, Josh D.},
  title = {Evaluating bias of Illumina-based bacterial 16S rRNA gene profiles},
  journal = {Applied and Environmental Microbiology},
  volume = {80},
  number = {18},
  pages = {5717-5722},
  year = {2014},
  doi = {10.1128/AEM.01451-14},
  note = {access: abstract_only (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Kennedy 2014}
}

@article{kersPowerMicrobiomeStudies2022,
  author = {Kers, Jannigje Gerdien and Saccenti, Edoardo},
  title = {The power of microbiome studies: some considerations on which alpha and beta metrics to use and how to report results},
  journal = {Frontiers in Microbiology},
  volume = {12},
  pages = {796025},
  year = {2022},
  doi = {10.3389/fmicb.2021.796025},
  note = {access: abstract_only (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Kers and Saccenti 2022}
}

@article{kircherDoubleIndexingOvercomes2012,
  author = {Kircher, Martin and Sawyer, Susanna and Meyer, Matthias},
  title = {Double indexing overcomes inaccuracies in multiplex sequencing on the Illumina platform},
  journal = {Nucleic Acids Research},
  volume = {40},
  number = {1},
  pages = {e3},
  year = {2012},
  doi = {10.1093/nar/gkr771},
  note = {access: full_text (INDIRECT) (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Kircher 2012}
}

@article{klappenbachRRNAOperonCopy2000,
  author = {Klappenbach, Joel A. and Dunbar, John M. and Schmidt, Thomas M.},
  title = {rRNA operon copy number reflects ecological strategies of bacteria},
  journal = {Applied and Environmental Microbiology},
  volume = {66},
  number = {4},
  pages = {1328-1333},
  year = {2000},
  doi = {10.1128/AEM.66.4.1328-1333.2000},
  note = {access: abstract_only (MB-01), abstract_only (MB-02); type: peer reviewed (MB-01); cited as: MB-01 Klappenbach 2000, MB-02 [9]}
}

@article{klindworthEvaluationGeneral16S2013,
  author = {Klindworth, Anna and Pruesse, Elmar and Schweer, Timmy and Peplies, Jörg and Quast, Christian and Horn, Matthias and Glöckner, Frank Oliver},
  title = {Evaluation of general 16S ribosomal RNA gene PCR primers for classical and next-generation sequencing-based diversity studies},
  journal = {Nucleic Acids Research},
  volume = {41},
  number = {1},
  pages = {e1},
  year = {2013},
  doi = {10.1093/nar/gks808},
  note = {access: full_text (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Klindworth 2013}
}

@article{kopylovaOpensourceSequenceClustering2016,
  author = {Kopylova, Evguenia and Navas-Molina, Jose A. and Mercier, Céline and Xu, Zhenjiang Zech and Mahé, Frédéric and He, Yan and Zhou, Hong-Wei and Rognes, Torbjørn and Caporaso, J. Gregory and Knight, Rob},
  title = {Open-source sequence clustering methods improve the state of the art},
  journal = {mSystems},
  volume = {1},
  number = {1},
  pages = {e00003-15},
  year = {2016},
  doi = {10.1128/mSystems.00003-15},
  note = {access: full_text (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Kopylova 2016}
}

@article{kozichDevelopmentDualindexSequencing2013,
  author = {Kozich, James J. and Westcott, Sarah L. and Baxter, Nielson T. and Highlander, Sarah K. and Schloss, Patrick D.},
  title = {Development of a dual-index sequencing strategy and curation pipeline for analyzing amplicon sequence data on the MiSeq Illumina sequencing platform},
  journal = {Applied and Environmental Microbiology},
  volume = {79},
  number = {17},
  pages = {5112-5120},
  year = {2013},
  doi = {10.1128/AEM.01043-13},
  note = {access: full_text (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Kozich 2013}
}

@article{kumarAnalysisCorrectionCompositional2018,
  author = {Kumar, M. Senthil and Slud, Eric V. and Okrah, Kwame and Hicks, Stephanie C. and Hannenhalli, Sridhar and Corrada Bravo, Héctor},
  title = {Analysis and correction of compositional bias in sparse sequencing count data},
  journal = {BMC Genomics},
  volume = {19},
  pages = {799},
  year = {2018},
  doi = {10.1186/s12864-018-5160-5},
  note = {access: abstract_only (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Kumar 2018}
}

@article{larosaHypothesisTestingPower2012,
  author = {La Rosa, Patricio S. and Brooks, J. Paul and Deych, Elena and Boone, Edward L. and Edwards, David J. and Wang, Qin and Sodergren, Erica and Weinstock, George and Shannon, William D.},
  title = {Hypothesis testing and power calculations for taxonomic-based human microbiome data},
  journal = {PLOS ONE},
  volume = {7},
  number = {12},
  pages = {e52078},
  year = {2012},
  doi = {10.1371/journal.pone.0052078},
  note = {access: full_text (MB-01); type: peer reviewed (MB-01); cited as: MB-01 La Rosa 2012}
}

@article{laursenGenomicGCcontentAffects2017,
  author = {Laursen, Martin F. and Dalgaard, Marlene D. and Bahl, Martin I.},
  title = {Genomic GC-content affects the accuracy of 16S rRNA gene sequencing based microbial profiling due to PCR bias},
  journal = {Frontiers in Microbiology},
  volume = {8},
  pages = {1934},
  year = {2017},
  doi = {10.3389/fmicb.2017.01934},
  note = {access: full_text (corrigendum 2022) (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Laursen 2017}
}

@article{lennonHowWhereRelic2018,
  author = {Lennon, Jay T. and Muscarella, Mario E. and Placella, Sarah A. and Lehmkuhl, Brent K.},
  title = {How, when, and where relic DNA affects microbial diversity},
  journal = {mBio},
  volume = {9},
  number = {3},
  pages = {e00637-18},
  year = {2018},
  doi = {10.1128/mBio.00637-18},
  note = {access: full_text (MB-01), abstract_only (MB-02); type: peer reviewed (MB-01); cited as: MB-01 Lennon 2018, MB-02 [78]}
}

@article{linAnalysisCompositionsMicrobiomes2020,
  author = {Lin, Huang and Peddada, Shyamal Das},
  title = {Analysis of compositions of microbiomes with bias correction},
  journal = {Nature Communications},
  volume = {11},
  pages = {3514},
  year = {2020},
  doi = {10.1038/s41467-020-17041-7},
  note = {access: abstract_only (makers' claims) (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Lin and Peddada 2020}
}

@article{linTowardsQuantitativeMicrobiome2019,
  author = {Lin, Yajuan and Gifford, Scott and Ducklow, Hugh and Schofield, Oscar and Cassar, Nicolas},
  title = {Towards quantitative microbiome community profiling using internal standards},
  journal = {Applied and Environmental Microbiology},
  volume = {85},
  number = {5},
  pages = {e02634-18},
  year = {2019},
  doi = {10.1128/AEM.02634-18},
  note = {access: full_text (DOI checked by the synthesis agent) (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Lin 2019}
}

@article{lingBatchEffectsRemoval2022,
  author = {Ling, Wodan and Lu, Jiuyao and Zhao, Ni and Lulla, Anju and Plantinga, Anna M. and Fu, Weijia and Zhang, Angela and Liu, Hongjiao and Song, Hoseung and Li, Zhigang and Chen, Jun and Randolph, Timothy W. and Koay, Wei Li A. and White, James R. and Launer, Lenore J. and Fodor, Anthony A. and Meyer, Katie A. and Wu, Michael C.},
  title = {Batch effects removal for microbiome data via conditional quantile regression},
  journal = {Nature Communications},
  volume = {13},
  pages = {5418},
  year = {2022},
  doi = {10.1038/s41467-022-33071-9},
  note = {access: abstract_only (makers' claims) (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Ling 2022}
}

@article{llorensricoBenchmarkingMicrobiomeTransformations2021,
  author = {Lloréns-Rico, Verónica and Vieira-Silva, Sara and Gonçalves, Pedro J. and Falony, Gwen and Raes, Jeroen},
  title = {Benchmarking microbiome transformations favors experimental quantitative approaches to address compositionality and sampling depth biases},
  journal = {Nature Communications},
  volume = {12},
  pages = {3562},
  year = {2021},
  doi = {10.1038/s41467-021-23821-6},
  note = {access: full_text (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Lloréns-Rico 2021}
}

@article{loucaCorrecting16SRRNA2018,
  author = {Louca, Stilianos and Doebeli, Michael and Parfrey, Laura Wegener},
  title = {Correcting for 16S rRNA gene copy numbers in microbiome surveys remains an unsolved problem},
  journal = {Microbiome},
  volume = {6},
  pages = {41},
  year = {2018},
  doi = {10.1186/s40168-018-0420-9},
  note = {access: full_text (MB-01), full_text (MB-02); type: peer reviewed (MB-01); cited as: MB-01 Louca 2018, MB-02 [30]}
}

@article{lundbergPracticalInnovationsHighthroughput2013,
  author = {Lundberg, Derek S. and Yourstone, Scott and Mieczkowski, Piotr and Jones, Corbin D. and Dangl, Jeffery L.},
  title = {Practical innovations for high-throughput amplicon sequencing},
  journal = {Nature Methods},
  volume = {10},
  number = {10},
  pages = {999-1002},
  year = {2013},
  doi = {10.1038/nmeth.2634},
  note = {access: abstract_only (makers' claims) (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Lundberg 2013}
}

@article{lundinWhichSequencingDepth2012,
  author = {Lundin, Daniel and Severin, Ina and Logue, Jürg Brendan and Östman, Örjan and Andersson, Anders F. and Lindström, Eva S.},
  title = {Which sequencing depth is sufficient to describe patterns in bacterial alpha- and beta-diversity?},
  journal = {Environmental Microbiology Reports},
  volume = {4},
  number = {3},
  pages = {367-372},
  year = {2012},
  doi = {10.1111/j.1758-2229.2012.00345.x},
  note = {access: abstract_only (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Lundin 2012}
}

@article{mandalAnalysisCompositionMicrobiomes2015,
  author = {Mandal, Siddhartha and Van Treuren, Will and White, Richard A. and Eggesbø, Merete and Knight, Rob and Peddada, Shyamal D.},
  title = {Analysis of composition of microbiomes: a novel method for studying microbial composition},
  journal = {Microbial Ecology in Health and Disease},
  volume = {26},
  pages = {27663},
  year = {2015},
  doi = {10.3402/mehd.v26.27663},
  note = {access: abstract_only (makers' claims) (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Mandal 2015}
}

@article{marioniRNAseqAssessmentTechnical2008,
  author = {Marioni, John C. and Mason, Christopher E. and Mane, Shrikant M. and Stephens, Matthew and Gilad, Yoav},
  title = {RNA-seq: an assessment of technical reproducibility and comparison with gene expression arrays},
  journal = {Genome Research},
  volume = {18},
  number = {9},
  pages = {1509-1517},
  year = {2008},
  doi = {10.1101/gr.079558.108},
  note = {access: full_text (INDIRECT) (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Marioni 2008}
}

@article{marizzoniComparisonBioinformaticsPipelines2020,
  author = {Marizzoni, Moira and Gurry, Thomas and Provasi, Stefania and Greub, Gilbert and Lopizzo, Nicola and Ribaldi, Federica and Festari, Cristina and Mazzelli, Monica and Mombelli, Elisa and Salvatore, Marco and Mirabelli, Peppino and Franzese, Monica and Soricelli, Andrea and Frisoni, Giovanni B. and Cattaneo, Annamaria},
  title = {Comparison of bioinformatics pipelines and operating systems for the analyses of 16S rRNA gene amplicon sequences in human fecal samples},
  journal = {Frontiers in Microbiology},
  volume = {11},
  pages = {1262},
  year = {2020},
  doi = {10.3389/fmicb.2020.01262},
  note = {access: full_text (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Marizzoni 2020}
}

@article{marotzTriplicatePCRReactions2019,
  author = {Marotz, Clarisse and Sharma, Amnon and Humphrey, Greg and Gottel, Neil and Daum, Christopher and Gilbert, Jack A. and Eloe-Fadrosh, Emiley and Knight, Rob},
  title = {Triplicate PCR reactions for 16S rRNA gene amplicon sequencing are unnecessary},
  journal = {BioTechniques},
  volume = {67},
  number = {1},
  pages = {29-32},
  year = {2019},
  doi = {10.2144/btn-2018-0192},
  note = {access: abstract_only (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Marotz 2019; correction: an open PMC copy exists (PMC7030937), so the AB label understates access (MB-01 critic)}
}

@article{martinModelingMicrobialAbundances2020,
  author = {Martin, Bryan D. and Witten, Daniela and Willis, Amy D.},
  title = {Modeling microbial abundances and dysbiosis with beta-binomial regression},
  journal = {The Annals of Applied Statistics},
  volume = {14},
  number = {1},
  pages = {94-115},
  year = {2020},
  doi = {10.1214/19-AOAS1283},
  note = {access: abstract_only (makers' claims) (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Martin 2020}
}

@article{martinlaurentDNAExtractionSoils2001,
  author = {Martin-Laurent, Fabrice and Philippot, Laurent and Hallet, Sabine and Chaussod, Rémi and Germon, Jean-Claude and Soulas, Guy and Catroux, Gérard},
  title = {DNA extraction from soils: old bias for new microbial diversity analysis methods},
  journal = {Applied and Environmental Microbiology},
  volume = {67},
  number = {5},
  pages = {2354-2359},
  year = {2001},
  doi = {10.1128/AEM.67.5.2354-2359.2001},
  note = {access: abstract_only (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Martin-Laurent 2001}
}

@article{mcknightMethodsNormalizingMicrobiome2019,
  author = {McKnight, Donald T. and Huerlimann, Roger and Bower, Deborah S. and Schwarzkopf, Lin and Alford, Ross A. and Zenger, Kyall R.},
  title = {Methods for normalizing microbiome data: an ecological perspective},
  journal = {Methods in Ecology and Evolution},
  volume = {10},
  number = {3},
  pages = {389-400},
  year = {2019},
  doi = {10.1111/2041-210X.13115},
  note = {access: abstract_only (MB-01); type: peer reviewed (MB-01); cited as: MB-01 McKnight 2019}
}

@article{mclarenConsistentCorrectableBias2019,
  author = {McLaren, Michael R. and Willis, Amy D. and Callahan, Benjamin J.},
  title = {Consistent and correctable bias in metagenomic sequencing experiments},
  journal = {eLife},
  volume = {8},
  pages = {e46923},
  year = {2019},
  doi = {10.7554/eLife.46923},
  note = {access: full_text (re-opened by the synthesis agent) (MB-01), abstract_only (MB-02); type: peer reviewed (MB-01); cited as: MB-01 McLaren 2019, MB-02 [35]}
}

@article{mclarenImplicationsTaxonomicBias2022,
  author = {McLaren, Michael R. and Nearing, Jacob T. and Willis, Amy D. and Lloyd, Karen G. and Callahan, Benjamin J.},
  title = {Implications of taxonomic bias for microbial differential-abundance analysis},
  journal = {bioRxiv},
  pages = {2022.08.19.504330},
  year = {2022},
  doi = {10.1101/2022.08.19.504330},
  note = {access: abstract_only (MB-01); type: PREPRINT (MB-01); cited as: MB-01 McLaren 2022}
}

@article{mcmurdieWasteNotWant2014,
  author = {McMurdie, Paul J. and Holmes, Susan},
  title = {Waste not, want not: why rarefying microbiome data is inadmissible},
  journal = {PLOS Computational Biology},
  volume = {10},
  number = {4},
  pages = {e1003531},
  year = {2014},
  doi = {10.1371/journal.pcbi.1003531},
  note = {access: full_text (MB-01); type: peer reviewed (MB-01); cited as: MB-01 McMurdie and Holmes 2014}
}

@article{minichQuantifyingUnderstandingWelltowell2019,
  author = {Minich, Jeremiah J. and Sanders, Jon G. and Amir, Amnon and Humphrey, Greg and Gilbert, Jack A. and Knight, Rob},
  title = {Quantifying and understanding well-to-well contamination in microbiome research},
  journal = {mSystems},
  volume = {4},
  number = {4},
  pages = {e00186-19},
  year = {2019},
  doi = {10.1128/mSystems.00186-19},
  note = {access: full_text (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Minich 2019}
}

@article{mortonEstablishingMicrobialComposition2019,
  author = {Morton, James T. and Marotz, Clarisse and Washburne, Alex and Silverman, Justin and Zaramela, Livia S. and Edlund, Anna and Zengler, Karsten and Knight, Rob},
  title = {Establishing microbial composition measurement standards with reference frames},
  journal = {Nature Communications},
  volume = {10},
  pages = {2719},
  year = {2019},
  doi = {10.1038/s41467-019-10656-5},
  note = {access: abstract_only (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Morton 2019}
}

@article{muraliIDTAXANovelApproach2018,
  author = {Murali, Adithya and Bhargava, Aniruddha and Wright, Erik S.},
  title = {IDTAXA: a novel approach for accurate taxonomic classification of microbiome sequences},
  journal = {Microbiome},
  volume = {6},
  pages = {140},
  year = {2018},
  doi = {10.1186/s40168-018-0521-5},
  note = {access: full_text (developer claims) (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Murali 2018}
}

@article{nearingDenoisingDenoisersIndependent2018,
  author = {Nearing, Jacob T. and Douglas, Gavin M. and Comeau, André M. and Langille, Morgan G. I.},
  title = {Denoising the Denoisers: an independent evaluation of microbiome sequence error-correction approaches},
  journal = {PeerJ},
  volume = {6},
  pages = {e5364},
  year = {2018},
  doi = {10.7717/peerj.5364},
  note = {access: full_text (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Nearing 2018}
}

@article{nearingMicrobiomeDifferentialAbundance2022,
  author = {Nearing, Jacob T. and Douglas, Gavin M. and Hayes, Molly G. and MacDonald, Jocelyn and Desai, Dhwani K. and Allward, Nicole and Jones, Casey M. A. and Wright, Robyn J. and Dhanani, Akhilesh S. and Comeau, André M. and Langille, Morgan G. I.},
  title = {Microbiome differential abundance methods produce different results across 38 datasets},
  journal = {Nature Communications},
  volume = {13},
  pages = {342},
  year = {2022},
  doi = {10.1038/s41467-022-28034-z},
  note = {access: full_text (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Nearing 2022}
}

@article{nemergutDecreasesAverageBacterial2015,
  author = {Nemergut, Diana R. and Knelman, Joseph E. and Ferrenberg, Scott and Bilinski, Teresa and Melbourne, Brett and Jiang, Lin and Violle, Cyrille and Darcy, John L. and Prest, Tiffany and Schmidt, Steven K. and Townsend, Alan R.},
  title = {Decreases in average bacterial community rRNA operon copy number during succession},
  journal = {The ISME Journal},
  volume = {10},
  number = {5},
  pages = {1147-1156},
  year = {2016},
  doi = {10.1038/ismej.2015.191},
  note = {access: full_text (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Nemergut 2016}
}

@article{paradaEveryBaseMatters2016,
  author = {Parada, Alma E. and Needham, David M. and Fuhrman, Jed A.},
  title = {Every base matters: assessing small subunit rRNA primers for marine microbiomes with mock communities, time series and global field samples},
  journal = {Environmental Microbiology},
  volume = {18},
  number = {5},
  pages = {1403-1414},
  year = {2016},
  doi = {10.1111/1462-2920.13023},
  note = {access: abstract_only (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Parada 2016}
}

@article{peltoElementaryMethodsProvide2025,
  author = {Pelto, Juho and Auranen, Kari and Kujala, Janne V. and Lahti, Leo},
  title = {Elementary methods provide more replicable results in microbial differential abundance analysis},
  journal = {Briefings in Bioinformatics},
  volume = {26},
  number = {2},
  pages = {bbaf130},
  year = {2025},
  doi = {10.1093/bib/bbaf130},
  note = {access: abstract_only (DOI checked by the synthesis agent) (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Pelto 2025}
}

@article{pentonSizeMattersAssessing2016,
  author = {Penton, C. Ryan and Gupta, Vadakattu V. S. R. and Yu, Julian and Tiedje, James M.},
  title = {Size matters: assessing optimum soil sample size for fungal and bacterial community structure analyses using high throughput sequencing of rRNA gene amplicons},
  journal = {Frontiers in Microbiology},
  volume = {7},
  pages = {824},
  year = {2016},
  doi = {10.3389/fmicb.2016.00824},
  note = {access: full_text (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Penton 2016}
}

@article{pintoPCRBiasesDistort2012,
  author = {Pinto, Ameet J. and Raskin, Lutgarde},
  title = {PCR biases distort bacterial and archaeal community structure in pyrosequencing datasets},
  journal = {PLOS ONE},
  volume = {7},
  number = {8},
  pages = {e43093},
  year = {2012},
  doi = {10.1371/journal.pone.0043093},
  note = {access: full_text (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Pinto and Raskin 2012}
}

@article{polzBiasTemplatetoproductRatios1998,
  author = {Polz, Martin F. and Cavanaugh, Colleen M.},
  title = {Bias in template-to-product ratios in multitemplate PCR},
  journal = {Applied and Environmental Microbiology},
  volume = {64},
  number = {10},
  pages = {3724-3730},
  year = {1998},
  doi = {10.1128/AEM.64.10.3724-3730.1998},
  note = {access: abstract_only (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Polz and Cavanaugh 1998}
}

@article{prodanComparingBioinformaticPipelines2020,
  author = {Prodan, Andrei and Tremaroli, Valentina and Brolin, Harald and Zwinderman, Aeilko H. and Nieuwdorp, Max and Levin, Evgeni},
  title = {Comparing bioinformatic pipelines for microbial 16S rRNA amplicon sequencing},
  journal = {PLOS ONE},
  volume = {15},
  number = {1},
  pages = {e0227434},
  year = {2020},
  doi = {10.1371/journal.pone.0227434},
  note = {access: full_text (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Prodan 2020}
}

@article{propsAbsoluteQuantificationMicrobial2016,
  author = {Props, Ruben and Kerckhof, Frederiek-Maarten and Rubbens, Peter and De Vrieze, Jo and Hernandez Sanabria, Emma and Waegeman, Willem and Monsieurs, Pieter and Hammes, Frederik and Boon, Nico},
  title = {Absolute quantification of microbial taxon abundances},
  journal = {The ISME Journal},
  volume = {11},
  number = {2},
  pages = {584-587},
  year = {2017},
  doi = {10.1038/ismej.2016.117},
  note = {access: abstract_only (MB-01), abstract_only (MB-02); type: peer reviewed (MB-01); cited as: MB-01 Props 2017, MB-02 [83]}
}

@article{reitmeierHandlingSpuriousSequences2021,
  author = {Reitmeier, Sandra and Hitch, Thomas C. A. and Treichel, Nicole and Fikas, Nikolaos and Hausmann, Bela and Ramer-Tait, Amanda E. and Neuhaus, Klaus and Berry, David and Haller, Dirk and Lagkouvardos, Ilias and Clavel, Thomas},
  title = {Handling of spurious sequences affects the outcome of high-throughput 16S rRNA gene amplicon profiling},
  journal = {ISME Communications},
  volume = {1},
  number = {1},
  pages = {31},
  year = {2021},
  doi = {10.1038/s43705-021-00033-z},
  note = {access: full_text (DOI checked by the synthesis agent) (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Reitmeier 2021}
}

@article{robinsonScalingNormalizationMethod2010,
  author = {Robinson, Mark D. and Oshlack, Alicia},
  title = {A scaling normalization method for differential expression analysis of RNA-seq data},
  journal = {Genome Biology},
  volume = {11},
  number = {3},
  pages = {R25},
  year = {2010},
  doi = {10.1186/gb-2010-11-3-r25},
  note = {access: abstract_only (INDIRECT) (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Robinson and Oshlack 2010}
}

@article{rollerExploitingRRNAOperon2016,
  author = {Roller, Benjamin R. K. and Stoddard, Steven F. and Schmidt, Thomas M.},
  title = {Exploiting rRNA operon copy number to investigate bacterial reproductive strategies},
  journal = {Nature Microbiology},
  volume = {1},
  number = {11},
  pages = {16160},
  year = {2016},
  doi = {10.1038/nmicrobiol.2016.160},
  note = {access: abstract_only (MB-01), abstract_only (MB-02); type: peer reviewed (MB-01); cited as: MB-01 Roller 2016, MB-02 [10]}
}

@article{rubinInvestigatingImpactStorage2013,
  author = {Rubin, Benjamin E. R. and Gibbons, Sean M. and Kennedy, Suzanne and Hampton-Marcell, Jarrad and Owens, Sarah and Gilbert, Jack A.},
  title = {Investigating the impact of storage conditions on microbial community composition in soil samples},
  journal = {PLOS ONE},
  volume = {8},
  number = {7},
  pages = {e70460},
  year = {2013},
  doi = {10.1371/journal.pone.0070460},
  note = {access: full_text (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Rubin 2013}
}

@article{salterReagentLaboratoryContamination2014,
  author = {Salter, Susannah J. and Cox, Michael J. and Turek, Elena M. and Calus, Szymon T. and Cookson, William O. and Moffatt, Miriam F. and Turner, Paul and Parkhill, Julian and Loman, Nicholas J. and Walker, Alan W.},
  title = {Reagent and laboratory contamination can critically impact sequence-based microbiome analyses},
  journal = {BMC Biology},
  volume = {12},
  pages = {87},
  year = {2014},
  doi = {10.1186/s12915-014-0087-z},
  note = {access: full_text (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Salter 2014}
}

@article{schirmerInsightBiasesSequencing2015,
  author = {Schirmer, Melanie and Ijaz, Umer Z. and D'Amore, Rosalinda and Hall, Neil and Sloan, William T. and Quince, Christopher},
  title = {Insight into biases and sequencing errors for amplicon sequencing with the Illumina MiSeq platform},
  journal = {Nucleic Acids Research},
  volume = {43},
  number = {6},
  pages = {e37},
  year = {2015},
  doi = {10.1093/nar/gku1341},
  note = {access: full_text (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Schirmer 2015}
}

@article{schlossAmpliconSequenceVariants2021,
  author = {Schloss, Patrick D.},
  title = {Amplicon sequence variants artificially split bacterial genomes into separate clusters},
  journal = {mSphere},
  volume = {6},
  number = {4},
  pages = {e00191-21},
  year = {2021},
  doi = {10.1128/mSphere.00191-21},
  note = {access: full_text (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Schloss 2021}
}

@article{schlossWasteNotWant2024,
  author = {Schloss, Patrick D.},
  title = {Waste not, want not: revisiting the analysis that called into question the practice of rarefaction},
  journal = {mSphere},
  volume = {9},
  number = {1},
  pages = {e00355-23},
  year = {2024},
  doi = {10.1128/msphere.00355-23},
  note = {access: full_text (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Schloss 2024a}
}

@article{schlossRarefactionCurrentlyBest2024,
  author = {Schloss, Patrick D.},
  title = {Rarefaction is currently the best approach to control for uneven sequencing effort in amplicon sequence analyses},
  journal = {mSphere},
  volume = {9},
  number = {2},
  pages = {e00354-23},
  year = {2024},
  doi = {10.1128/msphere.00354-23},
  note = {access: full_text (re-opened by the synthesis agent; DOI checked) (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Schloss 2024b}
}

@article{schnellTagJumpsIlluminated2015,
  author = {Schnell, Ida Bærholm and Bohmann, Kristine and Gilbert, M. Thomas P.},
  title = {Tag jumps illuminated: reducing sequence-to-sample misidentifications in metabarcoding studies},
  journal = {Molecular Ecology Resources},
  volume = {15},
  number = {6},
  pages = {1289-1303},
  year = {2015},
  doi = {10.1111/1755-0998.12402},
  note = {access: abstract_only (INDIRECT) (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Schnell 2015}
}

@article{sheltonTowardQuantitativeMetabarcoding2023,
  author = {Shelton, Andrew Olaf and Gold, Zachary J. and Jensen, Alexander J. and D'Agnese, Erin and Andruszkiewicz Allan, Elizabeth and Van Cise, Amy and Gallego, Ramón and Ramón-Laca, Ana and Garber-Yonts, Maya and Parsons, Kim and Kelly, Ryan P.},
  title = {Toward quantitative metabarcoding},
  journal = {Ecology},
  volume = {104},
  number = {2},
  pages = {e3906},
  year = {2023},
  doi = {10.1002/ecy.3906},
  note = {access: abstract_only (INDIRECT) (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Shelton 2023}
}

@article{shoemakerMacroecologicalTheoryMicrobial2017,
  author = {Shoemaker, William R. and Locey, Kenneth J. and Lennon, Jay T.},
  title = {A macroecological theory of microbial biodiversity},
  journal = {Nature Ecology & Evolution},
  volume = {1},
  number = {5},
  pages = {0107},
  year = {2017},
  doi = {10.1038/s41559-017-0107},
  note = {access: abstract_only (per lab angle; DOI checked by the synthesis agent) (MB-01), abstract_only (MB-02), not_obtained (only a web-search engine summary seen, not used as a finding) (MB-01, sources not obtained); type: peer reviewed (MB-01); cited as: MB-01 Shoemaker 2017, MB-02 [70]; conflict: MB-01 lists it both as used (AB per lab angle) and under Sources not obtained (only a web-search summary seen, not used as a finding)}
}

@article{silvermanDynamicLinearModels2018,
  author = {Silverman, Justin D. and Durand, Heather K. and Bloom, Rachael J. and Mukherjee, Sayan and David, Lawrence A.},
  title = {Dynamic linear models guide design and analysis of microbiota studies within artificial human guts},
  journal = {Microbiome},
  volume = {6},
  pages = {202},
  year = {2018},
  doi = {10.1186/s40168-018-0584-3},
  note = {access: full_text (DOI checked by the synthesis agent) (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Silverman 2018}
}

@article{silvermanNaughtAllZeros2020,
  author = {Silverman, Justin D. and Roche, Kimberly and Mukherjee, Sayan and David, Lawrence A.},
  title = {Naught all zeros in sequence count data are the same},
  journal = {Computational and Structural Biotechnology Journal},
  volume = {18},
  pages = {2789-2798},
  year = {2020},
  doi = {10.1016/j.csbj.2020.09.014},
  note = {access: abstract_only (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Silverman 2020}
}

@article{silvermanMeasuringMitigatingPCR2021,
  author = {Silverman, Justin D. and Bloom, Rachael J. and Jiang, Sharon and Durand, Heather K. and Dallow, Eric and Mukherjee, Sayan and David, Lawrence A.},
  title = {Measuring and mitigating PCR bias in microbiota datasets},
  journal = {PLOS Computational Biology},
  volume = {17},
  number = {7},
  pages = {e1009113},
  year = {2021},
  doi = {10.1371/journal.pcbi.1009113},
  note = {access: full_text (DOI checked by the synthesis agent) (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Silverman 2021}
}

@article{sinhaAssessmentVariationMicrobial2017,
  author = {Sinha, Rashmi and Abu-Ali, Galeb and Vogtmann, Emily and Fodor, Anthony A. and Ren, Boyu and Amir, Amnon and Schwager, Emma and Crabtree, Jonathan and Ma, Siyuan and The Microbiome Quality Control Project Consortium and Abnet, Christian C. and Knight, Rob and White, Owen and Huttenhower, Curtis},
  title = {Assessment of variation in microbial community amplicon sequencing by the Microbiome Quality Control (MBQC) project consortium},
  journal = {Nature Biotechnology},
  volume = {35},
  number = {11},
  pages = {1077-1086},
  year = {2017},
  doi = {10.1038/nbt.3981},
  note = {access: full_text (per bioinformatics angle) (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Sinha 2017; correction: Crossref lists The Microbiome Quality Control Project Consortium as the first author entry; the review places it after Siyuan Ma (MB-01 critic: author order mismatch)}
}

@article{siposEffectPrimerMismatch2007,
  author = {Sipos, Rita and Székely, Anna J. and Palatinszky, Márton and Révész, Sára and Márialigeti, Károly and Nikolausz, Marcell},
  title = {Effect of primer mismatch, annealing temperature and PCR cycle number on 16S rRNA gene-targetting bacterial community analysis},
  journal = {FEMS Microbiology Ecology},
  volume = {60},
  number = {2},
  pages = {341-350},
  year = {2007},
  doi = {10.1111/j.1574-6941.2007.00283.x},
  note = {access: abstract_only (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Sipos 2007}
}

@article{smetsMethodSimultaneousMeasurement2016,
  author = {Smets, Wenke and Leff, Jonathan W. and Bradford, Mark A. and McCulley, Rebecca L. and Lebeer, Sarah and Fierer, Noah},
  title = {A method for simultaneous measurement of soil bacterial abundances and community composition via 16S rRNA gene sequencing},
  journal = {Soil Biology and Biochemistry},
  volume = {96},
  pages = {145-151},
  year = {2016},
  doi = {10.1016/j.soilbio.2016.02.003},
  note = {access: abstract_only (per lab angle) (MB-01), not_obtained (Crossref (no abstract), Europe PMC (not indexed)) (MB-01, sources not obtained); type: peer reviewed (MB-01); cited as: MB-01 Smets 2016; conflict: MB-01 lists it both as used (AB per lab angle) and under Sources not obtained (Crossref no abstract; Europe PMC not indexed)}
}

@article{smithSequenceDepthNot2014,
  author = {Smith, Dylan P. and Peay, Kabir G.},
  title = {Sequence depth, not PCR replication, improves ecological inference from next generation DNA sequencing},
  journal = {PLOS ONE},
  volume = {9},
  number = {2},
  pages = {e90234},
  year = {2014},
  doi = {10.1371/journal.pone.0090234},
  note = {access: full_text (INDIRECT, ITS) (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Smith and Peay 2014}
}

@article{songPreservationMethodsDiffer2016,
  author = {Song, Se Jin and Amir, Amnon and Metcalf, Jessica L. and Amato, Katherine R. and Xu, Zhenjiang Zech and Humphrey, Greg and Knight, Rob},
  title = {Preservation methods differ in fecal microbiome stability, affecting suitability for field studies},
  journal = {mSystems},
  volume = {1},
  number = {3},
  pages = {e00021-16},
  year = {2016},
  doi = {10.1128/mSystems.00021-16},
  note = {access: full_text (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Song 2016}
}

@article{stammlerAdjustingMicrobiomeProfiles2016,
  author = {Stämmler, Frank and Gläsner, Joachim and Hiergeist, Andreas and Holler, Ernst and Weber, Daniela and Oefner, Peter J. and Gessner, André and Spang, Rainer},
  title = {Adjusting microbiome profiles for differences in microbial load by spike-in bacteria},
  journal = {Microbiome},
  volume = {4},
  pages = {28},
  year = {2016},
  doi = {10.1186/s40168-016-0175-0},
  note = {access: full_text (per lab angle) (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Stämmler 2016}
}

@article{starke16SRRNAGene2020,
  author = {Starke, Robert and Pylro, Victor Satler and Morais, Daniel Kumazawa},
  title = {16S rRNA gene copy number normalization does not provide more reliable conclusions in metataxonomic surveys},
  journal = {Microbial Ecology},
  volume = {81},
  number = {2},
  pages = {535-539},
  year = {2021},
  doi = {10.1007/s00248-020-01586-7},
  note = {access: full_text (MB-01), full_text (MB-02); type: peer reviewed (MB-01); cited as: MB-01 Starke 2021, MB-02 [32]}
}

@article{stoddardRrnDBImprovedTools2015,
  author = {Stoddard, Steven F. and Smith, Byron J. and Hein, Robert and Roller, Benjamin R. K. and Schmidt, Thomas M.},
  title = {rrnDB: improved tools for interpreting rRNA gene abundance in bacteria and archaea and a new foundation for future development},
  journal = {Nucleic Acids Research},
  volume = {43},
  number = {D1},
  pages = {D593-D598},
  year = {2015},
  doi = {10.1093/nar/gku1201},
  note = {access: full_text (MB-01), full_text (MB-02); type: peer reviewed database paper (MB-01); cited as: MB-01 Stoddard 2015, MB-02 [3]}
}

@article{straubInterpretationsEnvironmentalMicrobial2020,
  author = {Straub, Daniel and Blackwell, Nia and Langarica-Fuentes, Adrian and Peltzer, Alexander and Nahnsen, Sven and Kleindienst, Sara},
  title = {Interpretations of environmental microbial community studies are biased by the selected 16S rRNA (gene) amplicon sequencing pipeline},
  journal = {Frontiers in Microbiology},
  volume = {11},
  pages = {550420},
  year = {2020},
  doi = {10.3389/fmicb.2020.550420},
  note = {access: full_text (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Straub 2020}
}

@article{suzukiBiasCausedTemplate1996,
  author = {Suzuki, Marcelino T. and Giovannoni, Stephen J.},
  title = {Bias caused by template annealing in the amplification of mixtures of 16S rRNA genes by PCR},
  journal = {Applied and Environmental Microbiology},
  volume = {62},
  number = {2},
  pages = {625-630},
  year = {1996},
  doi = {10.1128/aem.62.2.625-630.1996},
  note = {access: abstract_only (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Suzuki and Giovannoni 1996}
}

@article{szeImpactDNAPolymerase2019,
  author = {Sze, Marc A. and Schloss, Patrick D.},
  title = {The impact of DNA polymerase and number of rounds of amplification in PCR on 16S rRNA gene sequence data},
  journal = {mSphere},
  volume = {4},
  number = {3},
  pages = {e00163-19},
  year = {2019},
  doi = {10.1128/mSphere.00163-19},
  note = {access: full_text (re-opened by the synthesis agent) (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Sze and Schloss 2019}
}

@article{thompsonCommunalCatalogueReveals2017,
  author = {Thompson, Luke R. and Sanders, Jon G. and McDonald, Daniel and Amir, Amnon and Ladau, Joshua and Locey, Kenneth J. and Prill, Robert J. and Tripathi, Anupriya and Gibbons, Sean M. and Ackermann, Gail and Navas-Molina, Jose A. and Janssen, Stefan and Kopylova, Evguenia and Vázquez-Baeza, Yoshiki and González, Antonio and Morton, James T. and Mirarab, Siavash and Xu, Zhenjiang Zech and Jiang, Lingjing and Haroon, Mohamed F. and Kanbar, Jad and Zhu, Qiyun and Song, Se Jin and Kosciolek, Tomasz and Bokulich, Nicholas A. and Lefler, Joshua and Brislawn, Colin J. and Humphrey, Gregory and Owens, Sarah M. and Hampton-Marcell, Jarrad and Berg-Lyons, Donna and McKenzie, Valerie and Fierer, Noah and Fuhrman, Jed A. and Clauset, Aaron and Stevens, Rick L. and Shade, Ashley and Pollard, Katherine S. and Goodwin, Kelly D. and Jansson, Janet K. and Gilbert, Jack A. and Knight, Rob and The Earth Microbiome Project Consortium (consortium members as listed in the Crossref record)},
  title = {A communal catalogue reveals Earth's multiscale microbial diversity},
  journal = {Nature},
  volume = {551},
  number = {7681},
  pages = {457-463},
  year = {2017},
  doi = {10.1038/nature24621},
  note = {access: full_text (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Thompson 2017; correction: author list truncated at the consortium; Crossref lists several hundred named consortium members (MB-01 critic); incomplete: author}
}

@article{thorsenLargescaleBenchmarkingReveals2016,
  author = {Thorsen, Jonathan and Brejnrod, Asker and Mortensen, Martin and Rasmussen, Morten A. and Stokholm, Jakob and Abu Al-Soud, Waleed and Sørensen, Søren and Bisgaard, Hans and Waage, Johannes},
  title = {Large-scale benchmarking reveals false discoveries and count transformation sensitivity in 16S rRNA gene amplicon data analysis methods used in microbiome studies},
  journal = {Microbiome},
  volume = {4},
  pages = {62},
  year = {2016},
  doi = {10.1186/s40168-016-0208-8},
  note = {access: abstract_only (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Thorsen 2016}
}

@article{tkaczAbsoluteQuantitationMicrobiota2018,
  author = {Tkacz, Andrzej and Hortala, Marion and Poole, Philip S.},
  title = {Absolute quantitation of microbiota abundance in environmental samples},
  journal = {Microbiome},
  volume = {6},
  pages = {110},
  year = {2018},
  doi = {10.1186/s40168-018-0491-7},
  note = {access: full_text (per lab angle) (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Tkacz 2018}
}

@article{tourlousseSyntheticSpikeinStandards2016,
  author = {Tourlousse, Dieter M. and Yoshiike, Satowa and Ohashi, Akiko and Matsukura, Satoko and Noda, Naohiro and Sekiguchi, Yuji},
  title = {Synthetic spike-in standards for high-throughput 16S rRNA gene amplicon sequencing},
  journal = {Nucleic Acids Research},
  volume = {45},
  number = {4},
  pages = {e23},
  year = {2017},
  doi = {10.1093/nar/gkw984},
  note = {access: full_text (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Tourlousse 2017; correction: Crossref lacks volume/issue; the review's values are the published ones (MB-01 critic)}
}

@article{vandeputteQuantitativeMicrobiomeProfiling2017,
  author = {Vandeputte, Doris and Kathagen, Gunter and D'hoe, Kevin and Vieira-Silva, Sara and Valles-Colomer, Mireia and Sabino, João and Wang, Jun and Tito, Raul Y. and De Commer, Lindsey and Darzi, Youssef and Vermeire, Séverine and Falony, Gwen and Raes, Jeroen},
  title = {Quantitative microbiome profiling links gut community variation to microbial load},
  journal = {Nature},
  volume = {551},
  number = {7681},
  pages = {507-511},
  year = {2017},
  doi = {10.1038/nature24460},
  note = {access: abstract_only (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Vandeputte 2017}
}

@article{vetrovskyVariability16SRRNA2013,
  author = {Větrovský, Tomáš and Baldrian, Petr},
  title = {The variability of the 16S rRNA gene in bacterial genomes and its consequences for bacterial community analyses},
  journal = {PLOS ONE},
  volume = {8},
  number = {2},
  pages = {e57923},
  year = {2013},
  doi = {10.1371/journal.pone.0057923},
  note = {access: full_text (MB-01), full_text (MB-02); type: peer reviewed (MB-01); cited as: MB-01 Větrovský and Baldrian 2013, MB-02 [6]}
}

@article{waltersImprovedBacterial16S2016,
  author = {Walters, William and Hyde, Embriette R. and Berg-Lyons, Donna and Ackermann, Gail and Humphrey, Greg and Parada, Alma and Gilbert, Jack A. and Jansson, Janet K. and Caporaso, J. Gregory and Fuhrman, Jed A. and Apprill, Amy and Knight, Rob},
  title = {Improved bacterial 16S rRNA gene (V4 and V4-5) and fungal internal transcribed spacer marker gene primers for microbial community surveys},
  journal = {mSystems},
  volume = {1},
  number = {1},
  pages = {e00009-15},
  year = {2016},
  doi = {10.1128/mSystems.00009-15},
  note = {access: full_text (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Walters 2016}
}

@article{weissNormalizationMicrobialDifferential2017,
  author = {Weiss, Sophie and Xu, Zhenjiang Zech and Peddada, Shyamal and Amir, Amnon and Bittinger, Kyle and Gonzalez, Antonio and Lozupone, Catherine and Zaneveld, Jesse R. and Vázquez-Baeza, Yoshiki and Birmingham, Amanda and Hyde, Embriette R. and Knight, Rob},
  title = {Normalization and microbial differential abundance strategies depend upon data characteristics},
  journal = {Microbiome},
  volume = {5},
  pages = {27},
  year = {2017},
  doi = {10.1186/s40168-017-0237-y},
  note = {access: full_text (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Weiss 2017}
}

@article{wenEvaluationReproducibilityAmplicon2017,
  author = {Wen, Chongqing and Wu, Liyou and Qin, Yujia and Van Nostrand, Joy D. and Ning, Daliang and Sun, Bo and Xue, Kai and Liu, Feifei and Deng, Ye and Liang, Yuting and Zhou, Jizhong},
  title = {Evaluation of the reproducibility of amplicon sequencing with Illumina MiSeq platform},
  journal = {PLOS ONE},
  volume = {12},
  number = {4},
  pages = {e0176716},
  year = {2017},
  doi = {10.1371/journal.pone.0176716},
  note = {access: full_text (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Wen 2017}
}

@article{willisRarefactionAlphaDiversity2019,
  author = {Willis, Amy D.},
  title = {Rarefaction, alpha diversity, and statistics},
  journal = {Frontiers in Microbiology},
  volume = {10},
  pages = {2407},
  year = {2019},
  doi = {10.3389/fmicb.2019.02407},
  note = {access: full_text (MB-01); type: peer reviewed perspective (MB-01); cited as: MB-01 Willis 2019}
}

@article{willisEstimatingDiversityFrequency2015,
  author = {Willis, Amy and Bunge, John},
  title = {Estimating diversity via frequency ratios},
  journal = {Biometrics},
  volume = {71},
  number = {4},
  pages = {1042-1049},
  year = {2015},
  doi = {10.1111/biom.12332},
  note = {access: abstract_only (makers' claims) (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Willis and Bunge 2015}
}

@article{willisImprovedDetectionChanges2017,
  author = {Willis, Amy and Bunge, John and Whitman, Thea},
  title = {Improved detection of changes in species richness in high diversity microbial communities},
  journal = {Journal of the Royal Statistical Society Series C: Applied Statistics},
  volume = {66},
  number = {5},
  pages = {963-977},
  year = {2017},
  doi = {10.1111/rssc.12206},
  note = {access: abstract_only (makers' claims) (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Willis, Bunge and Whitman 2017}
}

@article{willisEstimatingDiversityNetworked2022,
  author = {Willis, Amy D. and Martin, Bryan D.},
  title = {Estimating diversity in networked ecological communities},
  journal = {Biostatistics},
  volume = {23},
  number = {1},
  pages = {207-222},
  year = {2022},
  doi = {10.1093/biostatistics/kxaa015},
  note = {access: abstract_only (makers' claims) (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Willis and Martin 2022}
}

@article{wirbelRealisticBenchmarkDifferential2024,
  author = {Wirbel, Jakob and Essex, Morgan and Forslund, Sofia Kirke and Zeller, Georg},
  title = {A realistic benchmark for differential abundance testing and confounder adjustment in human microbiome studies},
  journal = {Genome Biology},
  volume = {25},
  pages = {247},
  year = {2024},
  doi = {10.1186/s13059-024-03390-9},
  note = {access: full_text (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Wirbel 2024}
}

@article{wrightQualityFilteringIllumina2016,
  author = {Wright, Erik Scott and Vetsigian, Kalin Horen},
  title = {Quality filtering of Illumina index reads mitigates sample cross-talk},
  journal = {BMC Genomics},
  volume = {17},
  pages = {876},
  year = {2016},
  doi = {10.1186/s12864-016-3217-x},
  note = {access: full_text (INDIRECT) (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Wright and Vetsigian 2016}
}

@article{yangComprehensiveEvaluationMicrobial2022,
  author = {Yang, Lu and Chen, Jun},
  title = {A comprehensive evaluation of microbial differential abundance analysis methods: current status and potential solutions},
  journal = {Microbiome},
  volume = {10},
  pages = {130},
  year = {2022},
  doi = {10.1186/s40168-022-01320-0},
  note = {access: full_text (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Yang and Chen 2022}
}

@article{yehTaxonDisappearanceMicrobiome2018,
  author = {Yeh, Yi-Chun and Needham, David M. and Sieradzki, Ella T. and Fuhrman, Jed A.},
  title = {Taxon disappearance from microbiome analysis reinforces the value of mock communities as a standard in every sequencing run},
  journal = {mSystems},
  volume = {3},
  number = {3},
  pages = {e00023-18},
  year = {2018},
  doi = {10.1128/mSystems.00023-18},
  note = {access: full_text (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Yeh 2018}
}

@article{zembAbsoluteQuantitationMicrobes2020,
  author = {Zemb, Olivier and Achard, Caroline S. and Hamelin, Jérôme and De Almeida, Marie-Léa and Gabinaud, Béatrice and Cauquil, Laurent and Verschuren, Lisanne M. G. and Godon, Jean-Jacques},
  title = {Absolute quantitation of microbes using 16S rRNA gene metabarcoding: a rapid normalization of relative abundances by quantitative PCR targeting a 16S rRNA gene spike-in standard},
  journal = {MicrobiologyOpen},
  volume = {9},
  number = {3},
  pages = {e977},
  year = {2020},
  doi = {10.1002/mbo3.977},
  note = {access: full_text (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Zemb 2020}
}

@article{zhouReproducibilityQuantitationAmplicon2011,
  author = {Zhou, Jizhong and Wu, Liyou and Deng, Ye and Zhi, Xiaoyang and Jiang, Yi-Huei and Tu, Qichao and Xie, Jianping and Van Nostrand, Joy D. and He, Zhili and Yang, Yunfeng},
  title = {Reproducibility and quantitation of amplicon sequencing-based detection},
  journal = {The ISME Journal},
  volume = {5},
  number = {8},
  pages = {1303-1313},
  year = {2011},
  doi = {10.1038/ismej.2011.11},
  note = {access: full_text (per statistics and bioinformatics angles) (MB-01), abstract_only (MB-02); type: peer reviewed (MB-01); cited as: MB-01 Zhou 2011, MB-02 [76]}
}

@article{zhouRandomSamplingProcess2013,
  author = {Zhou, Jizhong and Jiang, Yi-Huei and Deng, Ye and Shi, Zhou and Zhou, Benjamin Yamin and Xue, Kai and Wu, Liyou and He, Zhili and Yang, Yunfeng},
  title = {Random sampling process leads to overestimation of beta-diversity of microbial communities},
  journal = {mBio},
  volume = {4},
  number = {3},
  pages = {e00324-13},
  year = {2013},
  doi = {10.1128/mBio.00324-13},
  note = {access: full_text (MB-01); type: peer reviewed (MB-01); cited as: MB-01 Zhou 2013}
}

@article{klappenbachRrndbRibosomalRNA2001,
  author = {Klappenbach, Joel A. and Saxman, Paul R. and Cole, James R. and Schmidt, Thomas M.},
  title = {rrndb: the Ribosomal RNA Operon Copy Number Database},
  journal = {Nucleic Acids Research},
  volume = {29},
  number = {1},
  pages = {181-184},
  year = {2001},
  doi = {10.1093/nar/29.1.181},
  note = {access: abstract_only ((Crossref lists only the first author; full list from Europe PMC and rrnDB.)) (MB-02); cited as: MB-02 [1]; correction: Crossref lists only the first author; full list from Europe PMC and rrnDB (MB-02)}
}

@article{leeRrnDBDocumentingNumber2009,
  author = {Lee, Zarraz M.-P. and Bussema, III, Carl and Schmidt, Thomas M.},
  title = {rrnDB: documenting the number of rRNA and tRNA genes in bacteria and archaea},
  journal = {Nucleic Acids Research},
  volume = {37},
  number = {Database issue},
  pages = {D489-D493},
  year = {2009},
  doi = {10.1093/nar/gkn689},
  note = {access: abstract_only (MB-02); cited as: MB-02 [2]; correction: Crossref gives 'C. Bussema' without the suffix 'III' (MB-02 critic: trivial)}
}

@article{acinasDivergenceRedundancy16S2004,
  author = {Acinas, Silvia G. and Marcelino, Luisa A. and Klepac-Ceraj, Vanja and Polz, Martin F.},
  title = {Divergence and redundancy of 16S rRNA sequences in genomes with multiple rrn operons},
  journal = {Journal of Bacteriology},
  volume = {186},
  number = {9},
  pages = {2629-2635},
  year = {2004},
  doi = {10.1128/JB.186.9.2629-2635.2004},
  note = {access: abstract_only (MB-02); cited as: MB-02 [5]}
}

@article{brewerUnlinkedRRNAGenes2020,
  author = {Brewer, Tess E. and Albertsen, Mads and Edwards, Arwyn and Kirkegaard, Rasmus H. and Rocha, Eduardo P. C. and Fierer, Noah},
  title = {Unlinked rRNA genes are widespread among bacteria and archaea},
  journal = {The ISME Journal},
  volume = {14},
  number = {2},
  pages = {597-608},
  year = {2020},
  doi = {10.1038/s41396-019-0552-3},
  note = {access: abstract_only (MB-02); cited as: MB-02 [7]}
}

@article{sunIntragenomicHeterogeneity16S2013,
  author = {Sun, Dong-Lei and Jiang, Xuan and Wu, Qinglong L. and Zhou, Ning-Yi},
  title = {Intragenomic heterogeneity of 16S rRNA genes causes overestimation of prokaryotic diversity},
  journal = {Applied and Environmental Microbiology},
  volume = {79},
  number = {19},
  pages = {5962-5969},
  year = {2013},
  doi = {10.1128/AEM.01282-13},
  note = {access: abstract_only (MB-02); cited as: MB-02 [8]}
}

@article{pecoraroQuantificationPloidyProteobacteria2011,
  author = {Pecoraro, Vito and Zerulla, Karolin and Lange, Christian and Soppa, Jörg},
  title = {Quantification of ploidy in proteobacteria revealed the existence of monoploid, (mero-)oligoploid and polyploid species},
  journal = {PLoS ONE},
  volume = {6},
  number = {1},
  pages = {e16392},
  year = {2011},
  doi = {10.1371/journal.pone.0016392},
  note = {access: full_text (MB-02); cited as: MB-02 [11]}
}

@article{akerlundAnalysisCellSize1995,
  author = {Akerlund, T. and Nordström, K. and Bernander, R.},
  title = {Analysis of cell size and DNA content in exponentially growing and stationary-phase batch cultures of Escherichia coli},
  journal = {Journal of Bacteriology},
  volume = {177},
  number = {23},
  pages = {6791-6797},
  year = {1995},
  doi = {10.1128/jb.177.23.6791-6797.1995},
  note = {access: abstract_only (MB-02); cited as: MB-02 [12]}
}

@article{bottingerRegulatedPloidyBacillus2018,
  author = {Böttinger, Benjamin and Semmler, Florian and Zerulla, Karolin and Ludt, Katharina and Soppa, Jörg},
  title = {Regulated ploidy of Bacillus subtilis and three new isolates of Bacillus and Paenibacillus},
  journal = {FEMS Microbiology Letters},
  volume = {365},
  number = {4},
  pages = {fnx282},
  year = {2018},
  doi = {10.1093/femsle/fnx282},
  note = {access: abstract_only (MB-02); cited as: MB-02 [13]}
}

@article{breuertRegulatedPolyploidyHalophilic2006,
  author = {Breuert, Sebastian and Allers, Thorsten and Spohn, Gabi and Soppa, Jörg},
  title = {Regulated polyploidy in halophilic archaea},
  journal = {PLoS ONE},
  volume = {1},
  number = {1},
  pages = {e92},
  year = {2006},
  doi = {10.1371/journal.pone.0000092},
  note = {access: abstract_only (MB-02); cited as: MB-02 [14]}
}

@article{hildenbrandGenomeCopyNumbers2011,
  author = {Hildenbrand, Catherina and Stock, Tilmann and Lange, Christian and Rother, Michael and Soppa, Jörg},
  title = {Genome copy numbers and gene conversion in methanogenic archaea},
  journal = {Journal of Bacteriology},
  volume = {193},
  number = {3},
  pages = {734-743},
  year = {2011},
  doi = {10.1128/JB.01016-10},
  note = {access: abstract_only (MB-02); cited as: MB-02 [15]}
}

@article{griesePloidyCyanobacteria2011,
  author = {Griese, Marco and Lange, Christian and Soppa, Jörg},
  title = {Ploidy in cyanobacteria},
  journal = {FEMS Microbiology Letters},
  volume = {323},
  number = {2},
  pages = {124-131},
  year = {2011},
  doi = {10.1111/j.1574-6968.2011.02368.x},
  note = {access: abstract_only (MB-02); cited as: MB-02 [16]}
}

@article{zerullaPloidyLevelSynechocystis2016,
  author = {Zerulla, Karolin and Ludt, Katharina and Soppa, Jörg},
  title = {The ploidy level of Synechocystis sp. PCC 6803 is highly variable and is influenced by growth phase and by chemical and physical external parameters},
  journal = {Microbiology},
  volume = {162},
  number = {5},
  pages = {730-739},
  year = {2016},
  doi = {10.1099/mic.0.000264},
  note = {access: abstract_only (MB-02); cited as: MB-02 [17]}
}

@article{bruckOneAdvantageBeing2023,
  author = {Brück, Patrik and Wasser, Daniel and Soppa, Jörg},
  title = {One advantage of being polyploid: prokaryotes of various phylogenetic groups can grow in the absence of an environmental phosphate source at the expense of their high genome copy numbers},
  journal = {Microorganisms},
  volume = {11},
  number = {9},
  pages = {2267},
  year = {2023},
  doi = {10.3390/microorganisms11092267},
  note = {access: abstract_only (MB-02); cited as: MB-02 [18]}
}

@article{zerullaPolyploidyHaloarchaeaAdvantages2014,
  author = {Zerulla, Karolin and Soppa, Jörg},
  title = {Polyploidy in haloarchaea: advantages for growth and survival},
  journal = {Frontiers in Microbiology},
  volume = {5},
  pages = {274},
  year = {2014},
  doi = {10.3389/fmicb.2014.00274},
  note = {access: abstract_only (MB-02); cited as: MB-02 [19]}
}

@article{couturierReplicationassociatedGeneDosage2006,
  author = {Couturier, Etienne and Rocha, Eduardo P. C.},
  title = {Replication-associated gene dosage effects shape the genomes of fast-growing bacteria but only for transcription and translation genes},
  journal = {Molecular Microbiology},
  volume = {59},
  number = {5},
  pages = {1506-1518},
  year = {2006},
  doi = {10.1111/j.1365-2958.2006.05046.x},
  note = {access: abstract_only (MB-02); cited as: MB-02 [20]}
}

@article{christensenFlowCytometricMeasurements1995,
  author = {Christensen, H. and Olsen, R. A. and Bakken, L. R.},
  title = {Flow cytometric measurements of cell volumes and DNA contents during culture of indigenous soil bacteria},
  journal = {Microbial Ecology},
  volume = {29},
  number = {1},
  pages = {49-62},
  year = {1995},
  doi = {10.1007/BF00217422},
  note = {access: abstract_only (MB-02); cited as: MB-02 [22]; correction: Crossref has no page range; pages 49-62 not confirmed (MB-02 critic)}
}

@article{buttonDeterminationDNAContent2001,
  author = {Button, D. K. and Robertson, Betsy R.},
  title = {Determination of DNA content of aquatic bacteria by flow cytometry},
  journal = {Applied and Environmental Microbiology},
  volume = {67},
  number = {4},
  pages = {1636-1645},
  year = {2001},
  doi = {10.1128/AEM.67.4.1636-1645.2001},
  note = {access: full_text (first 100,000 characters) (MB-02); cited as: MB-02 [23]}
}

@article{vaulotGrowthProchlorococcusPhotosynthetic1995,
  author = {Vaulot, Daniel and Marie, Dominique and Olson, Robert J. and Chisholm, Sallie W.},
  title = {Growth of Prochlorococcus, a photosynthetic prokaryote, in the equatorial Pacific Ocean},
  journal = {Science},
  volume = {268},
  number = {5216},
  pages = {1480-1482},
  year = {1995},
  doi = {10.1126/science.268.5216.1480},
  note = {access: abstract_only (MB-02); cited as: MB-02 [24]}
}

@article{brownMeasurementBacterialReplication2016,
  author = {Brown, Christopher T. and Olm, Matthew R. and Thomas, Brian C. and Banfield, Jillian F.},
  title = {Measurement of bacterial replication rates in microbial communities},
  journal = {Nature Biotechnology},
  volume = {34},
  number = {12},
  pages = {1256-1263},
  year = {2016},
  doi = {10.1038/nbt.3704},
  note = {access: full_text (first 100,000 characters) (MB-02); cited as: MB-02 [25]}
}

@article{koremGrowthDynamicsGut2015,
  author = {Korem, Tal and Zeevi, David and Suez, Jotham and Weinberger, Adina and Avnit-Sagi, Tali and Pompan-Lotan, Maya and Matot, Elad and Jona, Ghil and Harmelin, Alon and Cohen, Nadav and Sirota-Madi, Alexandra and Thaiss, Christoph A. and Pevsner-Fischer, Meirav and Sorek, Rotem and Xavier, Ramnik J. and Elinav, Eran and Segal, Eran},
  title = {Growth dynamics of gut microbiota in health and disease inferred from single metagenomic samples},
  journal = {Science},
  volume = {349},
  number = {6252},
  pages = {1101-1106},
  year = {2015},
  doi = {10.1126/science.aac4812},
  note = {access: abstract_only (MB-02); cited as: MB-02 [26]}
}

@article{farrellyEffectGenomeSize1995,
  author = {Farrelly, V. and Rainey, F. A. and Stackebrandt, E.},
  title = {Effect of genome size and rrn gene copy number on PCR amplification of 16S rRNA genes from a mixture of bacterial species},
  journal = {Applied and Environmental Microbiology},
  volume = {61},
  number = {7},
  pages = {2798-2801},
  year = {1995},
  doi = {10.1128/aem.61.7.2798-2801.1995},
  note = {access: abstract_only (MB-02); cited as: MB-02 [27]}
}

@article{anglyCopyRighterRapidTool2014,
  author = {Angly, Florent E. and Dennis, Paul G. and Skarshewski, Adam and Vanwonterghem, Inka and Hugenholtz, Philip and Tyson, Gene W.},
  title = {CopyRighter: a rapid tool for improving the accuracy of microbial community profiles through lineage-specific gene copy number correction},
  journal = {Microbiome},
  volume = {2},
  pages = {11},
  year = {2014},
  doi = {10.1186/2049-2618-2-11},
  note = {access: abstract_only (MB-02); cited as: MB-02 [29]}
}

@article{gaoAccounting16SRRNA2023,
  author = {Gao, Yingnan and Wu, Martin},
  title = {Accounting for 16S rRNA copy number prediction uncertainty and its implications in bacterial diversity analyses},
  journal = {ISME Communications},
  volume = {3},
  pages = {59},
  year = {2023},
  doi = {10.1038/s43705-023-00266-0},
  note = {access: full_text (MB-02); cited as: MB-02 [33]}
}

@article{perisin16StimatorStatisticalEstimation2016,
  author = {Perisin, Matthew and Vetter, Madlen and Gilbert, Jack A. and Bergelson, Joy},
  title = {16Stimator: statistical estimation of ribosomal gene copy numbers from draft genome assemblies},
  journal = {The ISME Journal},
  volume = {10},
  number = {4},
  pages = {1020-1024},
  year = {2016},
  doi = {10.1038/ismej.2015.161},
  note = {access: abstract_only (MB-02); cited as: MB-02 [34]}
}

@article{lavrinienkoDoesIntraspecificVariation2021,
  author = {Lavrinienko, Anton and Jernfors, Toni and Koskimäki, Janne J. and Pirttilä, Anna Maria and Watts, Phillip C.},
  title = {Does intraspecific variation in rDNA copy number affect analysis of microbial communities?},
  journal = {Trends in Microbiology},
  volume = {29},
  number = {1},
  pages = {19-27},
  year = {2021},
  doi = {10.1016/j.tim.2020.05.019},
  note = {access: abstract_only (MB-02); cited as: MB-02 [36]}
}

@article{soginMicrobialDiversityDeep2006,
  author = {Sogin, Mitchell L. and Morrison, Hilary G. and Huber, Julie A. and Welch, David Mark and Huse, Susan M. and Neal, Phillip R. and Arrieta, Jesus M. and Herndl, Gerhard J.},
  title = {Microbial diversity in the deep sea and the underexplored "rare biosphere"},
  journal = {PNAS},
  volume = {103},
  number = {32},
  pages = {12115-12120},
  year = {2006},
  doi = {10.1073/pnas.0605127103},
  note = {access: abstract_only (MB-02); cited as: MB-02 [38]}
}

@article{pedrosalioRareBacterialBiosphere2012,
  author = {Pedrós-Alió, Carlos},
  title = {The rare bacterial biosphere},
  journal = {Annual Review of Marine Science},
  volume = {4},
  pages = {449-466},
  year = {2012},
  doi = {10.1146/annurev-marine-120710-100948},
  note = {access: abstract_only (MB-02); cited as: MB-02 [39]}
}

@article{lynchEcologyExplorationRare2015,
  author = {Lynch, Michael D. J. and Neufeld, Josh D.},
  title = {Ecology and exploration of the rare biosphere},
  journal = {Nature Reviews Microbiology},
  volume = {13},
  number = {4},
  pages = {217-229},
  year = {2015},
  doi = {10.1038/nrmicro3400},
  note = {access: abstract_only (MB-02); cited as: MB-02 [40]}
}

@article{pascoalMicrobialRareBiosphere2021,
  author = {Pascoal, Francisco and Costa, Rodrigo and Magalhães, Catarina},
  title = {The microbial rare biosphere: current concepts, methods and ecological principles},
  journal = {FEMS Microbiology Ecology},
  volume = {97},
  number = {1},
  pages = {fiaa227},
  year = {2021},
  doi = {10.1093/femsec/fiaa227},
  note = {access: abstract_only (MB-02); cited as: MB-02 [41]}
}

@article{pascoalDefinitionMicrobialRare2025,
  author = {Pascoal, Francisco and Branco, Paula and Torgo, Luís and Costa, Rodrigo and Magalhães, Catarina},
  title = {Definition of the microbial rare biosphere through unsupervised machine learning},
  journal = {Communications Biology},
  volume = {8},
  pages = {544},
  year = {2025},
  doi = {10.1038/s42003-025-07912-4},
  note = {access: full_text (MB-02); cited as: MB-02 [42]}
}

@article{galandEcologyRareMicrobial2009,
  author = {Galand, Pierre E. and Casamayor, Emilio O. and Kirchman, David L. and Lovejoy, Connie},
  title = {Ecology of the rare microbial biosphere of the Arctic Ocean},
  journal = {PNAS},
  volume = {106},
  number = {52},
  pages = {22427-22432},
  year = {2009},
  doi = {10.1073/pnas.0908284106},
  note = {access: full_text (MB-02); cited as: MB-02 [43]}
}

@article{daiIdentifyingKeyTaxonomic2016,
  author = {Dai, Tianjiao and Zhang, Yan and Tang, Yushi and Bai, Yaohui and Tao, Yile and Huang, Bei and Wen, Donghui},
  title = {Identifying the key taxonomic categories that characterize microbial community diversity using full-scale classification: a case study of microbial communities in the sediments of Hangzhou Bay},
  journal = {FEMS Microbiology Ecology},
  volume = {92},
  number = {10},
  pages = {fiw150},
  year = {2016},
  doi = {10.1093/femsec/fiw150},
  note = {access: abstract_only (MB-02); cited as: MB-02 [44]}
}

@article{shadeConditionallyRareTaxa2014,
  author = {Shade, Ashley and Jones, Stuart E. and Caporaso, J. Gregory and Handelsman, Jo and Knight, Rob and Fierer, Noah and Gilbert, Jack A.},
  title = {Conditionally rare taxa disproportionately contribute to temporal changes in microbial diversity},
  journal = {mBio},
  volume = {5},
  number = {4},
  pages = {e01371-14},
  year = {2014},
  doi = {10.1128/mBio.01371-14},
  note = {access: full_text (excerpts) (MB-02); cited as: MB-02 [45]}
}

@article{gobetMultivariateCutoffLevel2010,
  author = {Gobet, Angélique and Quince, Christopher and Ramette, Alban},
  title = {Multivariate Cutoff Level Analysis (MultiCoLA) of large community data sets},
  journal = {Nucleic Acids Research},
  volume = {38},
  number = {15},
  pages = {e155},
  year = {2010},
  doi = {10.1093/nar/gkq545},
  note = {access: abstract_only (MB-02); cited as: MB-02 [46]}
}

@article{joussetWhereLessMay2017,
  author = {Jousset, Alexandre and Bienhold, Christina and Chatzinotas, Antonis and Gallien, Laure and Gobet, Angélique and Kurm, Viola and Küsel, Kirsten and Rillig, Matthias C. and Rivett, Damian W. and Salles, Joana F. and van der Heijden, Marcel G. A. and Youssef, Noha H. and Zhang, Xiaowei and Wei, Zhong and Hol, W. H. Gera},
  title = {Where less may be more: how the rare biosphere pulls ecosystems strings},
  journal = {The ISME Journal},
  volume = {11},
  number = {4},
  pages = {853-862},
  year = {2017},
  doi = {10.1038/ismej.2016.174},
  note = {access: full_text (MB-02); cited as: MB-02 [47]}
}

@article{jiaCommunityAssemblyProcesses2018,
  author = {Jia, Xiu and Dini-Andreote, Francisco and Salles, Joana Falcão},
  title = {Community assembly processes of the microbial rare biosphere},
  journal = {Trends in Microbiology},
  volume = {26},
  number = {9},
  pages = {738-747},
  year = {2018},
  doi = {10.1016/j.tim.2018.02.011},
  note = {access: abstract_only (MB-02); cited as: MB-02 [48]}
}

@article{jiaUnravellingInterplayEcological2022,
  author = {Jia, Xiu and Dini-Andreote, Francisco and Salles, Joana Falcão},
  title = {Unravelling the interplay of ecological processes structuring the bacterial rare biosphere},
  journal = {ISME Communications},
  volume = {2},
  pages = {96},
  year = {2022},
  doi = {10.1038/s43705-022-00177-6},
  note = {access: full_text (MB-02); cited as: MB-02 [49]}
}

@article{shadeBeyondVennDiagram2012,
  author = {Shade, Ashley and Handelsman, Jo},
  title = {Beyond the Venn diagram: the hunt for a core microbiome},
  journal = {Environmental Microbiology},
  volume = {14},
  number = {1},
  pages = {4-12},
  year = {2012},
  doi = {10.1111/j.1462-2920.2011.02585.x},
  note = {access: abstract_only (MB-02); cited as: MB-02 [50]}
}

@article{neuDefiningQuantifyingCore2021,
  author = {Neu, Alexander T. and Allen, Eric E. and Roy, Kaustuv},
  title = {Defining and quantifying the core microbiome: challenges and prospects},
  journal = {PNAS},
  volume = {118},
  number = {51},
  pages = {e2104429118},
  year = {2021},
  doi = {10.1073/pnas.2104429118},
  note = {access: full_text (first 100,000 characters) (MB-02); cited as: MB-02 [51]}
}

@article{custerComparativeAnalysisCore2023,
  author = {Custer, Gordon F. and Gans, Maya and van Diepen, Linda T. A. and Dini-Andreote, Francisco and Buerkle, C. Alex},
  title = {Comparative analysis of core microbiome assignments: implications for ecological synthesis},
  journal = {mSystems},
  volume = {8},
  number = {1},
  pages = {e01066-22},
  year = {2023},
  doi = {10.1128/msystems.01066-22},
  note = {access: full_text (first 100,000 characters) (MB-02); cited as: MB-02 [52]}
}

@article{astudillogarciaEvaluatingCoreMicrobiota2017,
  author = {Astudillo-García, Carmen and Bell, James J. and Webster, Nicole S. and Glasl, Bettina and Jompa, Jamaluddin and Montoya, Jose M. and Taylor, Michael W.},
  title = {Evaluating the core microbiota in complex communities: a systematic investigation},
  journal = {Environmental Microbiology},
  volume = {19},
  number = {4},
  pages = {1450-1462},
  year = {2017},
  doi = {10.1111/1462-2920.13647},
  note = {access: abstract_only (MB-02); cited as: MB-02 [53]}
}

@article{salonenAdultIntestinalCore2012,
  author = {Salonen, A. and Salojärvi, J. and Lahti, L. and de Vos, W. M.},
  title = {The adult intestinal core microbiota is determined by analysis depth and health status},
  journal = {Clinical Microbiology and Infection},
  volume = {18},
  number = {Suppl 4},
  pages = {16-20},
  year = {2012},
  doi = {10.1111/j.1469-0691.2012.03855.x},
  note = {access: abstract_only (MB-02); cited as: MB-02 [54]}
}

@article{riselyApplyingCoreMicrobiome2020,
  author = {Risely, Alice},
  title = {Applying the core microbiome to understand host-microbe systems},
  journal = {Journal of Animal Ecology},
  volume = {89},
  number = {7},
  pages = {1549-1558},
  year = {2020},
  doi = {10.1111/1365-2656.13229},
  note = {access: abstract_only (MB-02); cited as: MB-02 [55]}
}

@article{shadeAbundanceoccupancyDistributionsPrioritize2019,
  author = {Shade, Ashley and Stopnisek, Nejc},
  title = {Abundance-occupancy distributions to prioritize plant core microbiome membership},
  journal = {Current Opinion in Microbiology},
  volume = {49},
  pages = {50-58},
  year = {2019},
  doi = {10.1016/j.mib.2019.09.008},
  note = {access: abstract_only (MB-02); cited as: MB-02 [56]}
}

@article{magurranExplainingExcessRare2003,
  author = {Magurran, Anne E. and Henderson, Peter A.},
  title = {Explaining the excess of rare species in natural species abundance distributions},
  journal = {Nature},
  volume = {422},
  number = {6933},
  pages = {714-716},
  year = {2003},
  doi = {10.1038/nature01547},
  note = {access: abstract_only (MB-02); cited as: MB-02 [57]}
}

@article{gastonAbundanceoccupancyRelationships2000,
  author = {Gaston, Kevin J. and Blackburn, Tim M. and Greenwood, Jeremy J. D. and Gregory, Richard D. and Quinn, Rachel M. and Lawton, John H.},
  title = {Abundance-occupancy relationships},
  journal = {Journal of Applied Ecology},
  volume = {37},
  number = {s1},
  pages = {39-59},
  year = {2000},
  doi = {10.1046/j.1365-2664.2000.00485.x},
  note = {access: abstract_only (MB-02); cited as: MB-02 [58]}
}

@article{zengIdentifyingBiogeographicPatterns2021,
  author = {Zeng, Quanchao and An, Shaoshan},
  title = {Identifying the biogeographic patterns of rare and abundant bacterial communities using different primer sets on the Loess Plateau},
  journal = {Microorganisms},
  volume = {9},
  number = {1},
  pages = {139},
  year = {2021},
  doi = {10.3390/microorganisms9010139},
  note = {access: abstract_only (MB-02); cited as: MB-02 [59]}
}

@article{delgadobaquerizoGlobalAtlasDominant2018,
  author = {Delgado-Baquerizo, Manuel and Oliverio, Angela M. and Brewer, Tess E. and Benavent-González, Alberto and Eldridge, David J. and Bardgett, Richard D. and Maestre, Fernando T. and Singh, Brajesh K. and Fierer, Noah},
  title = {A global atlas of the dominant bacteria found in soil},
  journal = {Science},
  volume = {359},
  number = {6373},
  pages = {320-325},
  year = {2018},
  doi = {10.1126/science.aap9516},
  note = {access: full_text (publisher PDF via NOAA repository) (MB-02); cited as: MB-02 [60]}
}

@article{bickelChosenFewVariations2021,
  author = {Bickel, Samuel and Or, Dani},
  title = {The chosen few - variations in common and rare soil bacteria across biomes},
  journal = {The ISME Journal},
  volume = {15},
  number = {11},
  pages = {3315-3325},
  year = {2021},
  doi = {10.1038/s41396-021-00981-3},
  note = {access: full_text (MB-02); cited as: MB-02 [61]}
}

@article{nemergutGlobalPatternsBiogeography2011,
  author = {Nemergut, Diana R. and Costello, Elizabeth K. and Hamady, Micah and Lozupone, Catherine and Jiang, Lin and Schmidt, Steven K. and Fierer, Noah and Townsend, Alan R. and Cleveland, Cory C. and Stanish, Lee and Knight, Rob},
  title = {Global patterns in the biogeography of bacterial taxa},
  journal = {Environmental Microbiology},
  volume = {13},
  number = {1},
  pages = {135-144},
  year = {2011},
  doi = {10.1111/j.1462-2920.2010.02315.x},
  note = {access: full_text (MB-02); cited as: MB-02 [62]}
}

@article{barberanWhyAreMicrobes2014,
  author = {Barberán, Albert and Ramirez, Kelly S. and Leff, Jonathan W. and Bradford, Mark A. and Wall, Diana H. and Fierer, Noah},
  title = {Why are some microbes more ubiquitous than others? Predicting the habitat breadth of soil bacteria},
  journal = {Ecology Letters},
  volume = {17},
  number = {7},
  pages = {794-802},
  year = {2014},
  doi = {10.1111/ele.12282},
  note = {access: abstract_only (MB-02); cited as: MB-02 [63]}
}

@article{batesExaminingGlobalDistribution2011,
  author = {Bates, Scott T. and Berg-Lyons, Donna and Caporaso, J. Gregory and Walters, William A. and Knight, Rob and Fierer, Noah},
  title = {Examining the global distribution of dominant archaeal populations in soil},
  journal = {The ISME Journal},
  volume = {5},
  number = {5},
  pages = {908-917},
  year = {2011},
  doi = {10.1038/ismej.2010.171},
  note = {access: abstract_only (MB-02); cited as: MB-02 [64]}
}

@article{gansComputationalImprovementsReveal2005,
  author = {Gans, Jason and Wolinsky, Murray and Dunbar, John},
  title = {Computational improvements reveal great bacterial diversity and high metal toxicity in soil},
  journal = {Science},
  volume = {309},
  number = {5739},
  pages = {1387-1390},
  year = {2005},
  doi = {10.1126/science.1112665},
  note = {access: abstract_only (MB-02); cited as: MB-02 [66]}
}

@article{curtisEstimatingProkaryoticDiversity2002,
  author = {Curtis, Thomas P. and Sloan, William T. and Scannell, Jack W.},
  title = {Estimating prokaryotic diversity and its limits},
  journal = {PNAS},
  volume = {99},
  number = {16},
  pages = {10494-10499},
  year = {2002},
  doi = {10.1073/pnas.142680199},
  note = {access: abstract_only (MB-02); cited as: MB-02 [67]}
}

@article{dunbarEmpiricalTheoreticalBacterial2002,
  author = {Dunbar, John and Barns, Susan M. and Ticknor, Lawrence O. and Kuske, Cheryl R.},
  title = {Empirical and theoretical bacterial diversity in four Arizona soils},
  journal = {Applied and Environmental Microbiology},
  volume = {68},
  number = {6},
  pages = {3035-3045},
  year = {2002},
  doi = {10.1128/AEM.68.6.3035-3045.2002},
  note = {access: abstract_only (MB-02); cited as: MB-02 [68]}
}

@article{quinceRationalExplorationMicrobial2008,
  author = {Quince, Christopher and Curtis, Thomas P. and Sloan, William T.},
  title = {The rational exploration of microbial diversity},
  journal = {The ISME Journal},
  volume = {2},
  number = {10},
  pages = {997-1006},
  year = {2008},
  doi = {10.1038/ismej.2008.69},
  note = {access: abstract_only (MB-02); cited as: MB-02 [69]}
}

@article{loceyScalingLawsPredict2016,
  author = {Locey, Kenneth J. and Lennon, Jay T.},
  title = {Scaling laws predict global microbial diversity},
  journal = {PNAS},
  volume = {113},
  number = {21},
  pages = {5970-5975},
  year = {2016},
  doi = {10.1073/pnas.1521291113},
  note = {access: abstract_only (MB-02); cited as: MB-02 [71]}
}

@article{sloanQuantifyingRolesImmigration2006,
  author = {Sloan, William T. and Lunn, Mary and Woodcock, Stephen and Head, Ian M. and Nee, Sean and Curtis, Thomas P.},
  title = {Quantifying the roles of immigration and chance in shaping prokaryote community structure},
  journal = {Environmental Microbiology},
  volume = {8},
  number = {4},
  pages = {732-740},
  year = {2006},
  doi = {10.1111/j.1462-2920.2005.00956.x},
  note = {access: abstract_only (MB-02); cited as: MB-02 [73]}
}

@article{stopnisekPersistentMicrobiomeMembers2021,
  author = {Stopnisek, Nejc and Shade, Ashley},
  title = {Persistent microbiome members in the common bean rhizosphere: an integrated analysis of space, time, and plant genotype},
  journal = {The ISME Journal},
  volume = {15},
  number = {9},
  pages = {2708-2722},
  year = {2021},
  doi = {10.1038/s41396-021-00955-5},
  note = {access: full_text (MB-02); cited as: MB-02 [74]}
}

@article{waltersLargescaleReplicatedField2018,
  author = {Walters, William A. and Jin, Zhao and Youngblut, Nicholas and Wallace, Jason G. and Sutter, Jessica and Zhang, Wei and González-Peña, Antonio and Peiffer, Jason and Koren, Omry and Shi, Qiaojuan and Knight, Rob and Glavina del Rio, Tijana and Tringe, Susannah G. and Buckler, Edward S. and Dangl, Jeffery L. and Ley, Ruth E.},
  title = {Large-scale replicated field study of maize rhizosphere identifies heritable microbes},
  journal = {PNAS},
  volume = {115},
  number = {28},
  pages = {7368-7373},
  year = {2018},
  doi = {10.1073/pnas.1800918115},
  note = {access: abstract_only (MB-02); cited as: MB-02 [75]}
}

@article{howeTacklingSoilDiversity2014,
  author = {Chuang Howe, Adina and Jansson, Janet K. and Malfatti, Stephanie A. and Tringe, Susannah G. and Tiedje, James M. and Brown, C. Titus},
  title = {Tackling soil diversity with the assembly of large, complex metagenomes},
  journal = {PNAS},
  volume = {111},
  number = {13},
  pages = {4904-4909},
  year = {2014},
  doi = {10.1073/pnas.1402564111},
  note = {access: full_text (MB-02); cited as: MB-02 [79]}
}

@article{rodriguezrEstimatingCoverageMetagenomic2014,
  author = {Rodriguez-R, Luis M. and Konstantinidis, Konstantinos T.},
  title = {Estimating coverage in metagenomic data sets and why it matters},
  journal = {The ISME Journal},
  volume = {8},
  number = {11},
  pages = {2349-2351},
  year = {2014},
  doi = {10.1038/ismej.2014.76},
  note = {access: full_text (MB-02); cited as: MB-02 [80]}
}

@article{kuninWrinklesRareBiosphere2010,
  author = {Kunin, Victor and Engelbrektson, Anna and Ochman, Howard and Hugenholtz, Philip},
  title = {Wrinkles in the rare biosphere: pyrosequencing errors can lead to artificial inflation of diversity estimates},
  journal = {Environmental Microbiology},
  volume = {12},
  number = {1},
  pages = {118-123},
  year = {2010},
  doi = {10.1111/j.1462-2920.2009.02051.x},
  note = {access: abstract_only (MB-02), not_obtained (abstract and full text not retrieved) (MB-01, sources not obtained); cited as: MB-02 [81], MB-01 Kunin 2010; conflict: MB-01 lists it under Sources not obtained (abstract and full text not retrieved); MB-02 uses it at abstract level}
}

@article{huseIroningOutWrinkles2010,
  author = {Huse, Susan M. and Welch, David Mark and Morrison, Hilary G. and Sogin, Mitchell L.},
  title = {Ironing out the wrinkles in the rare biosphere through improved OTU clustering},
  journal = {Environmental Microbiology},
  volume = {12},
  number = {7},
  pages = {1889-1898},
  year = {2010},
  doi = {10.1111/j.1462-2920.2010.02193.x},
  note = {access: abstract_only (MB-02); cited as: MB-02 [82]}
}

@misc{callahanDADA2DocumentationPseudopooling,
  author = {Callahan, Benjamin J.},
  title = {DADA2 documentation: Pseudo-pooling},
  url = {https://benjjneb.github.io/dada2/pseudo.html},
  note = {access: full_text (MB-01); type: DOCUMENTATION (MB-01); cited as: MB-01 DADA2 pseudo-pooling page; accessed 2026-10-20; incomplete: year}
}

@misc{benjjnebConsequencesUsingDada2,
  author = {{benjjneb (DADA2 maintainer) and contributors}},
  title = {Consequences of using dada2 on NovaSeq data},
  howpublished = {GitHub issue #791, benjjneb/dada2},
  url = {https://github.com/benjjneb/dada2/issues/791},
  note = {access: full_text (DOCUMENTATION, issue tracker) (MB-01); type: DOCUMENTATION (MB-01); cited as: MB-01 DADA2 GitHub issue #791; accessed 2026-10-20; incomplete: year}
}

@misc{earth16SIlluminaAmplicon,
  author = {{Earth Microbiome Project}},
  title = {16S Illumina Amplicon Protocol},
  url = {https://earthmicrobiome.org/protocols-and-standards/16s/},
  note = {access: full_text (MB-01); type: PROTOCOL (MB-01); cited as: MB-01 EMP protocol; accessed 2026-10-20; incomplete: year}
}

@misc{emoryAmplicon16SMetagenomics,
  author = {{Emory Integrated Genomics Core / ECGC}},
  title = {Amplicon 16S metagenomics (methods description)},
  url = {https://www.cores.emory.edu/ecgc/_includes/documents/sections/resources/amplicon-16s-metagenomics.pdf},
  note = {access: full_text (MB-01); type: PROTOCOL (MB-01); cited as: MB-01 Emory core; accessed 2026-10-20; incomplete: year}
}

@manual{illumina16SMetagenomicSequencing,
  author = {{Illumina, Inc.}},
  title = {16S Metagenomic Sequencing Library Preparation: Preparing 16S Ribosomal RNA Gene Amplicons for the Illumina MiSeq System},
  number = {Part # 15044223 Rev. B},
  url = {https://support.illumina.com/documents/documentation/chemistry_documentation/16s/16s-metagenomic-library-prep-guide-15044223-b.pdf},
  note = {access: full_text (maker's claims) (MB-01); type: DOCUMENTATION (MB-01); cited as: MB-01 Illumina guide; accessed 2026-10-20; incomplete: year}
}

@misc{illuminaIndexHoppingWeb,
  author = {{Illumina, Inc.}},
  title = {Index hopping (web page)},
  url = {https://www.illumina.com/techniques/sequencing/ngs-library-prep/multiplexing/index-hopping.html},
  note = {access: full_text (maker's claims) (MB-01); type: DOCUMENTATION (MB-01); cited as: MB-01 Illumina index-hopping page; accessed 2026-10-20; incomplete: year}
}

@misc{zymoZymoBIOMICSMicrobialCommunity,
  author = {{Zymo Research}},
  title = {ZymoBIOMICS Microbial Community Standard (product page)},
  url = {https://www.zymoresearch.com/products/zymobiomics-microbial-community-standard},
  note = {access: full_text (maker's claims) (MB-01); type: DOCUMENTATION (MB-01); not cited; cited as: MB-01 Zymo product page; accessed 2026-10-20; incomplete: year}
}

@misc{schmidtlaboratoryRrnDBReleaseFiles2025,
  author = {{Schmidt Laboratory, University of Michigan}},
  title = {rrnDB release files v3.1.227, v4.4.3, v5.0, v5.6 and v5.10, and About page},
  year = {2025},
  url = {https://rrndb.umms.med.umich.edu/static/download/},
  note = {access: full_text (statistics derived by reviewer) (MB-02); cited as: MB-02 [4]; v5.10 dated 6 June 2025; accessed 2026-10-20}
}

@misc{bionumbersAverageNumberRRNA,
  author = {{BioNumbers}},
  title = {Average number of rRNA genes per genome (BioNumbers entry 102360)},
  url = {https://bionumbers.hms.harvard.edu/bionumber.aspx?id=102360},
  note = {access: secondary (MB-02); cited as: MB-02 [21]; cites Bremer and Dennis (1996), ch. 97, Table 3; incomplete: year}
}

@article{miloBioNumbersDatabaseKey2010,
  author = {Milo, Ron and Jorgensen, Paul and Moran, Uri and Weber, Griffin and Springer, Michael},
  title = {BioNumbers - the database of key numbers in molecular and cell biology},
  journal = {Nucleic Acids Research},
  volume = {38},
  number = {suppl_1},
  pages = {D750-D753},
  year = {2010},
  doi = {10.1093/nar/gkp889},
  note = {access: secondary (MB-02); cited as: MB-02 [21]; the database behind reference [21]; listed only, not cited for a finding}
}

@article{ramirezDetectingMacroecologicalPatterns2017,
  author = {Ramirez},
  journal = {Nature Microbiology},
  volume = {3},
  number = {2},
  pages = {189-196},
  year = {2018},
  doi = {10.1038/s41564-017-0062-x},
  note = {access: abstract_only (MB-02); cited as: MB-02 [65]; listed as 'Ramirez et al.'; not used in the body; see search record; incomplete: author (given names, co-authors), title}
}

@article{pei2010,
  author = {Pei},
  journal = {Applied and Environmental Microbiology},
  volume = {76},
  pages = {3886},
  year = {2010},
  note = {access: not_obtained (not used) (MB-02); cited as: MB-02 Pei et al. 2010; reading notes: mean copy figure 2.22 ± 0.81 whose meaning was unclear from the abstract; not used; incomplete: author (given names, co-authors), title, number, doi}
}

@article{gohlSystematicImprovementAmplicon2016,
  author = {Gohl, Daryl M. and Vangay, Pajau and Garbe, John and MacLean, Allison and Hauge, Adam and Becker, Aaron and Gould, Trevor J. and Clayton, Jonathan B. and Johnson, Timothy J. and Hunter, Ryan and Knights, Dan and Beckman, Kenneth B.},
  title = {Systematic improvement of amplicon marker gene methods for increased accuracy in microbiome studies},
  journal = {Nature Biotechnology},
  volume = {34},
  number = {9},
  pages = {942-949},
  year = {2016},
  doi = {10.1038/nbt.3601},
  note = {access: not_obtained (abstract only, too thin to report figures) (MB-01, sources not obtained); cited as: MB-01 Gohl 2016}
}

@article{costeaTowardsStandardsHuman2017,
  author = {Costea, Paul I. and Zeller, Georg and Sunagawa, Shinichi},
  title = {Towards standards for human fecal sample processing in metagenomic studies},
  journal = {Nature Biotechnology},
  volume = {35},
  number = {11},
  pages = {1069-1076},
  year = {2017},
  doi = {10.1038/nbt.3960},
  note = {access: secondary (known only through McLaren 2019; shotgun, INDIRECT) (MB-01, sources not obtained); cited as: MB-01 Costea 2017; incomplete: author (et al.)}
}

@article{lauberEffectStorageConditions2010,
  author = {Lauber, Christian L. and Zhou, Nicholas and Gordon, Jeffrey I. and Knight, Rob and Fierer, Noah},
  title = {Effect of storage conditions on the assessment of bacterial community structure in soil and human-associated samples},
  journal = {FEMS Microbiology Letters},
  volume = {307},
  number = {1},
  pages = {80-86},
  year = {2010},
  doi = {10.1111/j.1574-6968.2010.01965.x},
  note = {access: secondary (known only through Rubin 2013) (MB-01, sources not obtained); cited as: MB-01 Lauber 2010}
}

@article{wesolowskaandersenChoiceBacterialDNA2014,
  author = {Wesolowska-Andersen, Agata and Bahl, Martin I. and Carvalho, Vera and Kristiansen, Karsten and Sicheritz-Ponten, Thomas and Gupta, Ramneek and Licht, Tine R.},
  title = {Choice of bacterial DNA extraction method from fecal material influences community structure as evaluated by metagenomic analysis},
  journal = {Microbiome},
  volume = {2},
  pages = {19},
  year = {2014},
  doi = {10.1186/2049-2618-2-19},
  note = {access: not_obtained (full text retrieved but not searched before scratch cleanup; no findings extracted) (MB-01, sources not obtained); cited as: MB-01 Wesolowska-Andersen 2014}
}

@article{kimOptimizingMethodsDodging2017,
  author = {Kim, Dorothy and Hofstaedter, Casey E. and Zhao, Chunyu and Mattei, Lisa and Tanes, Ceylan and Clarke, Erik and Lauder, Abigail and Sherrill-Mix, Scott and Chehoud, Christel and Kelsen, Judith and Conrad, Máire and Collman, Ronald G. and Baldassano, Robert and Bushman, Frederic D. and Bittinger, Kyle},
  title = {Optimizing methods and dodging pitfalls in microbiome research},
  journal = {Microbiome},
  volume = {5},
  pages = {52},
  year = {2017},
  doi = {10.1186/s40168-017-0267-5},
  note = {access: not_obtained (full text keyword-searched; review content not reported to avoid secondary duplication) (MB-01, sources not obtained); cited as: MB-01 Kim 2017}
}

@misc{rrndbRrnDBCurrentRelease,
  author = {{rrnDB}},
  title = {rrnDB current release statistics},
  url = {https://rrndb.umms.med.umich.edu/},
  note = {access: not_obtained (WebFetch failed with TLS certificate error) (MB-01, sources not obtained); cited as: MB-01 rrnDB current release statistics; incomplete: year}
}

@article{weissTrackingDownSources2014,
  author = {Weiss, Sophie and Amir, Amnon and Hyde, Embriette R. and Metcalf, Jessica L. and Song, Se Jin and Knight, Rob},
  title = {Tracking down the sources of experimental contamination in microbiome studies},
  journal = {Genome Biology},
  volume = {15},
  pages = {564},
  year = {2014},
  doi = {10.1186/s13059-014-0564-2},
  note = {access: not_obtained (Crossref verified only) (MB-01, sources not obtained); cited as: MB-01 Weiss 2014}
}

@article{pauvertBioinformaticsMattersAccuracy2019,
  author = {Pauvert, Charlie and Buée, Marc and Laval, Valérie and Edel-Hermann, Véronique and Fauchery, Laure and Gautier, Angélique and Lesur, Isabelle and Vallance, Jessica and Vacher, Corinne},
  title = {Bioinformatics matters: the accuracy of plant and soil fungal community data is highly dependent on the metabarcoding pipeline},
  journal = {Fungal Ecology},
  volume = {41},
  pages = {23-33},
  year = {2019},
  doi = {10.1016/j.funeco.2019.03.005},
  note = {access: not_obtained (ITS, indirect) (MB-01, sources not obtained); cited as: MB-01 Pauvert 2019}
}

@article{sinhaIndexSwitchingCauses2017,
  author = {Sinha, Rahul and Stanley, Geoff and Gulati, Gunsagar S. and Ezran, Camille and Travaglini, Kyle J. and Wei, Eric and Chan, Charles K. F. and Nabhan, Ahmad N. and Su, Tianying and Morganti, Rachel M. and Conley, Stephanie D. and Chaib, Hassan and Red-Horse, Kristy and Longaker, Michael T. and Snyder, Michael P. and Krasnow, Mark A. and Weissman, Irving L.},
  title = {Index switching causes 'spreading-of-signal' among multiplexed samples in Illumina HiSeq 4000 DNA sequencing},
  journal = {bioRxiv},
  pages = {125724},
  year = {2017},
  doi = {10.1101/125724},
  note = {access: not_obtained (PREPRINT) (MB-01, sources not obtained); type: PREPRINT (MB-01); cited as: MB-01 Sinha (Rahul) 2017}
}

@article{hakimzadehPilePipelinesOverview2024,
  author = {Hakimzadeh, Ali and Abdala Asbun, Alejandro and Albanese, Davide and Bernard, Maria and Buchner, Dominik and Callahan, Benjamin and Caporaso, J. Gregory and Curd, Emily and Djemiel, Christophe and Brandström Durling, Mikael and Elbrecht, Vasco and Gold, Zachary and Gweon, Hyun S. and Hajibabaei, Mehrdad and Hildebrand, Falk and Mikryukov, Vladimir and Normandeau, Eric and Özkurt, Ezgi and Palmer, Jonathan M. and Pascal, Géraldine and Porter, Teresita M. and Straub, Daniel and Vasar, Martti and Větrovský, Tomáš and Zafeiropoulos, Haris and Anslan, Sten},
  title = {A pile of pipelines: an overview of the bioinformatics software for metabarcoding data analyses},
  journal = {Molecular Ecology Resources},
  volume = {24},
  number = {5},
  pages = {e13847},
  year = {2024},
  doi = {10.1111/1755-0998.13847},
  note = {access: not_obtained (Crossref only) (MB-01, sources not obtained); cited as: MB-01 Hakimzadeh 2024}
}

@article{sandersMarineBenthicDiversity1968,
  author = {Sanders, Howard L.},
  title = {Marine benthic diversity: a comparative study},
  journal = {The American Naturalist},
  volume = {102},
  number = {925},
  pages = {243-282},
  year = {1968},
  doi = {10.1086/282541},
  note = {access: secondary (known only through Chao and Jost 2012 and Willis 2019) (MB-01, sources not obtained); cited as: MB-01 Sanders 1968}
}

@article{hurlbertNonconceptSpeciesDiversity1971,
  author = {Hurlbert, Stuart H.},
  title = {The nonconcept of species diversity: a critique and alternative parameters},
  journal = {Ecology},
  volume = {52},
  number = {4},
  pages = {577-586},
  year = {1971},
  doi = {10.2307/1934145},
  note = {access: secondary (known only through Chao and Jost 2012 and Willis 2019) (MB-01, sources not obtained); cited as: MB-01 Hurlbert 1971}
}

@misc{simberloff1972,
  author = {Simberloff},
  year = {1972},
  note = {access: secondary (known only through Chao and Jost 2012; no reference given) (MB-01, sources not obtained); cited as: MB-01 Simberloff 1972; incomplete: author (given names), title, journal, volume, pages, doi}
}

@article{goodPopulationFrequenciesSpecies1953,
  author = {Good, I. J.},
  title = {The population frequencies of species and the estimation of population parameters},
  journal = {Biometrika},
  volume = {40},
  number = {3-4},
  pages = {237-264},
  year = {1953},
  doi = {10.1093/biomet/40.3-4.237},
  note = {access: not_obtained (Crossref metadata only) (MB-01, sources not obtained); cited as: MB-01 Good 1953}
}

@article{hsiehINEXTRPackage2016,
  author = {Hsieh, T. C. and Ma, K. H. and Chao, Anne},
  title = {iNEXT: an R package for rarefaction and extrapolation of species diversity (Hill numbers)},
  journal = {Methods in Ecology and Evolution},
  volume = {7},
  number = {12},
  pages = {1451-1456},
  year = {2016},
  doi = {10.1111/2041-210X.12613},
  note = {access: not_obtained (Crossref metadata only) (MB-01, sources not obtained); cited as: MB-01 Hsieh 2016}
}

@article{paulsonDifferentialAbundanceAnalysis2013,
  author = {Paulson, Joseph N. and Stine, O. Colin and Corrada Bravo, Héctor and Pop, Mihai},
  title = {Differential abundance analysis for microbial marker-gene surveys},
  journal = {Nature Methods},
  volume = {10},
  number = {12},
  pages = {1200-1202},
  year = {2013},
  doi = {10.1038/nmeth.2658},
  note = {access: not_obtained (Europe PMC abstract only (read)) (MB-01, sources not obtained); cited as: MB-01 Paulson 2013}
}

@article{loveModeratedEstimationFold2014,
  author = {Love, Michael I. and Huber, Wolfgang and Anders, Simon},
  title = {Moderated estimation of fold change and dispersion for RNA-seq data with DESeq2},
  journal = {Genome Biology},
  volume = {15},
  number = {12},
  pages = {550},
  year = {2014},
  doi = {10.1186/s13059-014-0550-8},
  note = {access: not_obtained (Crossref metadata only) (MB-01, sources not obtained); cited as: MB-01 Love 2014}
}

@incollection{rabinowitzSevenFormsRarity1981,
  author = {Rabinowitz, Deborah},
  title = {Seven forms of rarity},
  booktitle = {The Biological Aspects of Rare Plant Conservation},
  editor = {Synge, H.},
  publisher = {Wiley},
  pages = {205-217},
  year = {1981},
  note = {access: secondary (used only as described in Jousset et al. 2017) (MB-02, sources not obtained); cited as: MB-02 Rabinowitz 1981}
}

@article{wrightCorrelationsIncidenceAbundance1991,
  author = {Wright, David H.},
  title = {Correlations between incidence and abundance are expected by chance},
  journal = {Journal of Biogeography},
  volume = {18},
  number = {4},
  pages = {463-466},
  year = {1991},
  doi = {10.2307/2845487},
  note = {access: not_obtained (Crossref metadata located; no abstract) (MB-02, sources not obtained); cited as: MB-02 Wright 1991; correction: Crossref gives only a start page (463); end page 466 not confirmed (MB-02 critic)}
}

@article{holtOccupancyabundanceRelationshipsSpatial2002,
  author = {Holt, Alison R. and Gaston, Kevin J. and He, Fangliang},
  title = {Occupancy-abundance relationships and spatial distribution: a review},
  journal = {Basic and Applied Ecology},
  volume = {3},
  number = {1},
  pages = {1-13},
  year = {2002},
  doi = {10.1078/1439-1791-00083},
  note = {access: not_obtained (MB-02, sources not obtained); cited as: MB-02 Holt 2002}
}

@article{hanskiDynamicsRegionalDistribution1982,
  author = {Hanski, Ilkka},
  title = {Dynamics of regional distribution: the core and satellite species hypothesis},
  journal = {Oikos},
  volume = {38},
  number = {2},
  pages = {210-221},
  year = {1982},
  doi = {10.2307/3544021},
  note = {access: not_obtained (Crossref metadata only) (MB-02, sources not obtained); cited as: MB-02 Hanski 1982}
}

@article{bakkenDNAcontentSoilBacteria1989,
  author = {Bakken, Lars R. and Olsen, Rolf A.},
  title = {DNA-content of soil bacteria of different cell size},
  journal = {Soil Biology and Biochemistry},
  volume = {21},
  number = {6},
  pages = {789-793},
  year = {1989},
  doi = {10.1016/0038-0717(89)90172-7},
  note = {access: secondary (known only via Christensen et al. 1995 abstract) (MB-02, sources not obtained); cited as: MB-02 Bakken and Olsen 1989}
}

@article{christensenSoilBacterialDNA1993,
  author = {Christensen, Henrik and Bakken, Lars R. and Olsen, Rolf A.},
  title = {Soil bacterial DNA and biovolume profiles measured by flow-cytometry},
  journal = {FEMS Microbiology Ecology},
  volume = {11},
  number = {3-4},
  pages = {129-140},
  year = {1993},
  doi = {10.1111/j.1574-6968.1993.tb05804.x},
  note = {access: not_obtained (MB-02, sources not obtained); cited as: MB-02 Christensen 1993; correction: two Crossref records: FEMS Microbiology Ecology 11(3-4):129-140 / FEMS Microbiology Letters 102(3-4):129-140}
}

@article{soppaPolyploidyCommunityStructure2017,
  author = {Soppa, Jörg},
  title = {Polyploidy and community structure},
  journal = {Nature Microbiology},
  volume = {2},
  pages = {16261},
  year = {2017},
  doi = {10.1038/nmicrobiol.2016.261},
  note = {access: not_obtained (no abstract in Europe PMC) (MB-02, sources not obtained); cited as: MB-02 Soppa 2017}
}

@incollection{bremerModulationChemicalComposition1996,
  author = {Bremer, H. and Dennis, P. P.},
  title = {Modulation of chemical composition and other parameters of the cell by growth rate},
  booktitle = {Escherichia coli and Salmonella: Cellular and Molecular Biology, 2nd ed., chapter 97},
  editor = {Neidhardt, F. C. and others},
  publisher = {ASM Press},
  year = {1996},
  note = {access: secondary (via BioNumbers; chapter itself not reached) (MB-02, sources not obtained); cited as: MB-02 Bremer and Dennis 1996}
}

@book{gastonRarity1994,
  author = {Gaston, Kevin J.},
  title = {Rarity},
  publisher = {Chapman and Hall},
  address = {London},
  year = {1994},
  note = {access: not_obtained (not searched beyond citation trail) (MB-02, sources not obtained); cited as: MB-02 Gaston 1994}
}

@article{janda16SRRNAGene2007,
  author = {Janda, J. Michael and Abbott, Sharon L.},
  title = {16S rRNA Gene Sequencing for Bacterial Identification in the Diagnostic Laboratory: Pluses, Perils, and Pitfalls},
  journal = {Journal of Clinical Microbiology},
  volume = {45},
  number = {9},
  pages = {2761-2764},
  year = {2007},
  doi = {10.1128/JCM.01228-07},
  note = {background; access: full_text (open PMC copy, checked for the background entry); not cited by the inputs}
}
```
