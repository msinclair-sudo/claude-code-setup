---
type: knowledge
title: 16S amplicon sequencing from sample to count table
inputs:
  - MB-01: Topics/Biology/Research/Results/From sample to count table in 16S rRNA gene amplicon sequencing where counts depart from community composition, what the workflow's quantities measure, and how samples with unequal depth or load are compared. A literature review.md
  - MB-02: Topics/Biology/Research/Results/16S rRNA gene copies per genome and per cell, abundance and rarity terms, and abundance in soil. A literature review.md
refs: PhD/Proposal/Refs/Refs.bib
built: 2026-10-21
status: draft
tags:
  - research
  - knowledge
---
# 16S amplicon sequencing from sample to count table

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
| MB-01 | [[From sample to count table in 16S rRNA gene amplicon sequencing where counts depart from community composition, what the workflow's quantities measure, and how samples with unequal depth or load are compared. A literature review]] | yes | labelled (access; class; standing) | yes (130 of 147 labels) | yes | exact |
| MB-02 | [[16S rRNA gene copies per genome and per cell, abundance and rarity terms, and abundance in soil. A literature review]] | yes | numbered | no | no | fallback |

Checks run: detection and the omission check on both inputs (exact on MB-01, fallback on MB-02); the faithfulness check has not run yet. MB-01's run record (`.run.json`) was found and not needed.

## Concepts

### workflow-steps: the steps from sample to count table and the choices at each
needs: none
- **workflow-steps.1** Twelve steps between a sample and a table of taxon counts are documented, each with named alternatives; what the steps are is not in conflict, while the recommended choice within a step is disputed.
  conf: not stated · class: not stated · holds: protocols, software documentation and benchmarks; the critic: the body supports the twelve-step description and the alternatives listed, mostly from full-text protocols, documentation and benchmarks, with makers' statements labelled as such; the procedural descriptions would not change if any single source were removed · src: none (the reviewer's synthesis of the step-by-step evidence) · trail: MB-01 §answers, §2. Steps, §critic · from: MB-01:A-001, MB-01:A-018, MB-01:A-020, MB-01:A-021, MB-01:A-032, MB-01:A-294, MB-01:C-001, MB-01:C-002 · rating: "Strong for the existence of these choices and the alternatives used"
- **workflow-steps.2** How often each choice is made across the field is unmeasured, apart from the use of controls.
  conf: not stated · class: search (note: "No source found on how often each choice is used across the field") · holds: three search angles (lab, bioinformatics, statistics) via Crossref, Europe PMC, publisher pages and web search; the only usage survey is Hornung 2019, which covers controls · src: hornungIssuesCurrentStandards2019 (FT; meas; single) · trail: MB-01 §answers, §critic · from: MB-01:A-019, MB-01:A-026, MB-01:A-028, MB-01:A-295, MB-01:C-009 · rating: "weak on how often each is used"

### sampling-storage: field sampling, preservation, storage and sample mass
needs: workflow-steps
- **sampling-storage.1** Studies vary the preservative (none, 70% or 95% ethanol, FTA cards, OMNIgene Gut, freezing or refrigeration), the temperature and the duration of storage.
  conf: not stated · class: not stated · holds: the faeces and soil storage studies below · src: songPreservationMethodsDiffer2016, rubinInvestigatingImpactStorage2013 · trail: MB-01 §2.1, §answers · from: MB-01:B-0079, MB-01:A-002
- **sampling-storage.2** Human and dog faeces held at ambient temperature for 8 weeks changed by about as much as technical replicates differ when kept in 95% ethanol, on FTA cards or in OMNIgene Gut; unpreserved samples and 70% ethanol changed by amounts comparable to differences between individual humans.
  conf: repl (marker) · class: meas (marker) · holds: human and dog faeces, 8 weeks at ambient temperature · src: songPreservationMethodsDiffer2016 (FT; meas; repl) · trail: MB-01 §2.1, §answers · from: MB-01:B-0080, MB-01:I-0004, MB-01:A-038, MB-01:B-0050
- **sampling-storage.3** Storage altered taxon frequencies more than presence or absence: weighted UniFrac effects exceeded unweighted, and the number of taxa detected was affected less.
  conf: not stated · class: not stated · holds: faeces (Song 2016) · src: songPreservationMethodsDiffer2016 · trail: MB-01 §2.1, §answers · from: MB-01:B-0081, MB-01:A-036, MB-01:A-037, MB-01:A-039, MB-01:B-0049
- **sampling-storage.4** FTA cards produced a systematic shift that could be detrended, the one storage effect shown to be consistent across samples; for the other preservation methods consistency was not measured.
  conf: not stated · class: not stated · holds: faeces (Song 2016) · src: songPreservationMethodsDiffer2016 · trail: MB-01 §2.1, §answers · from: MB-01:B-0082, MB-01:A-040, MB-01:B-0051, MB-01:B-0052
- **sampling-storage.5** Storage of a single soil for 1 to 14 days at room temperature, 4 C or -20 C changed its community, most at 3 to 7 days and least when frozen; these changes were small relative to differences among more than 500 Earth Microbiome Project soils.
  conf: repl (marker) · class: meas (marker) · holds: one soil, 1 to 14 days, three temperatures, compared with more than 500 EMP soils; not shown for other soils · src: rubinInvestigatingImpactStorage2013 (FT; meas; repl), lauberEffectStorageConditions2010 (SEC) · trail: MB-01 §2.1, §answers, §7. Bounds · from: MB-01:B-0083, MB-01:I-0005, MB-01:A-041, MB-01:B-0346, MB-01:B-0084
- **sampling-storage.6** In one agricultural field, extracting 0.25, 1, 5, 10 or 100 g of soil changed community structure, replicate dispersion and OTU counts; 10 g extractions gave the highest diversity and the lowest dispersion.
  conf: single (marker) · class: meas (marker) · holds: one agricultural field, 0.25 to 100 g of soil · src: pentonSizeMattersAssessing2016 (FT; meas; single) · trail: MB-01 §2.1, §answers · from: MB-01:B-0085, MB-01:I-0006, MB-01:B-0086, MB-01:A-003
- **sampling-storage.7** Field sampling choices for water (volume filtered, filter pore size) and for host tissue were not searched by any angle: they are unsearched, not "not found".
  conf: not stated · class: search (critic: MB-01:C-008) · holds: the review's own Search record says no angle searched them; section 2.1 says the lab angle searched preservation and storage terms through Crossref, Europe PMC and web search, which the critic reads as a contradiction · src: none (a statement about the review's search) · trail: MB-01 §critic, §2.1, §Search record · from: MB-01:C-006, MB-01:C-007, MB-01:C-008, MB-01:C-012, MB-01:A-027, MB-01:B-0087, MB-01:B-0088, MB-01:B-0018, MB-01:B-0385

### extraction: DNA extraction
needs: workflow-steps
- **extraction.1** Extraction choices include the kit, bead-beating intensity, plate or single tube, and whether relic DNA is removed with PMA or DNase.
  conf: not stated · class: not stated · holds: the extraction studies below · src: albertsenBackBasicsInfluence2015, minichQuantifyingUnderstandingWelltowell2019, cariniRelicDNAAbundant2016, lennonHowWhereRelic2018 · trail: MB-01 §answers · from: MB-01:A-004
- **extraction.2** In McLaren's reanalysis of Brooks's 80 cell mixtures of 7 vaginal taxa (V1-V3, 454), the extraction step had a maximum pairwise bias of 36.6-fold and a mean of 5.5-fold, PCR a maximum of 5.2 and a mean of 2.3, and sequencing plus classification a maximum of 1.6 and a mean of 1.2; total bias in the cell mixtures was a maximum of 29.3-fold and a mean of 5.6-fold.
  conf: single (marker) · class: deriv/model (marker) · holds: one dataset, 7 vaginal taxa as cell mixtures, V1-V3 on 454 (Brooks 2015 data); figures checked against the full text by the synthesis agent and the critic · src: mclarenConsistentCorrectableBias2019 (FT, re-opened; deriv/model; single dataset), brooksTruthMetagenomicsQuantifying2015 · trail: MB-01 §2.2, §answers, §critic · from: MB-01:I-0007, MB-01:B-0089, MB-01:B-0090, MB-01:B-0091, MB-01:A-042, MB-01:A-043, MB-01:B-0053, MB-01:C-054
- **extraction.3** Total bias in the cell mixtures is smaller than extraction bias alone, which the note says implies partial cancellation between steps.
  conf: not stated · class: not stated · holds: the same 7-taxon reanalysis · src: mclarenConsistentCorrectableBias2019 · trail: MB-01 §2.2 · from: MB-01:B-0091, MB-01:B-0092
- **extraction.4** In the same data, Brooks et al. reported median total bias per taxon from -32.6% to +39.1% of true proportion, error from bias above 85% in some samples while technical variation was under 5% for most taxa, and a change of about 50% in Enterococcus when extraction kits were swapped.
  conf: not stated · class: not stated · holds: 7-taxon vaginal mock (Brooks 2015); the note's label sits on the sentence introducing the list, not on the list · src: brooksTruthMetagenomicsQuantifying2015 · trail: MB-01 §2.2, §4.4, §answers · from: MB-01:I-0008, MB-01:B-0093, MB-01:B-0094, MB-01:B-0095, MB-01:B-0255, MB-01:A-205
- **extraction.5** In activated sludge, bead-beating intensity and primer choice had the largest effects of all parameters tested; harder bead beating increased DNA from Gram-positive bacteria by up to 400%.
  conf: repl (marker) · class: meas (marker) · holds: activated sludge; bead beating only (the critic calls it partial support for the extraction ordering) · src: albertsenBackBasicsInfluence2015 (FT; meas; repl) · trail: MB-01 §2.2, §answers · from: MB-01:B-0096, MB-01:I-0009, MB-01:A-044, MB-01:B-0054, MB-01:C-084
- **extraction.6** In a 20-species gut mock, two extraction methods (QIAamp stool kit versus repeat bead beating) gave "very similar" data; primer and platform mattered more.
  conf: repl (marker) · class: meas (marker) · holds: one 20-species gut mock · src: fouhy16SRRNAGene2016 (FT; meas; repl) · trail: MB-01 §2.2, §answers, §7. Bounds · from: MB-01:B-0097, MB-01:I-0010, MB-01:A-045, MB-01:B-0055, MB-01:B-0350
- **extraction.7** Taxa whose DNA was never extracted were missing: in the MBQC artificial communities the largest contributor to inaccuracy was contamination or omission of microbes whose DNA was not extracted.
  conf: not stated · class: not stated · holds: MBQC, 15 laboratories, artificial communities · src: sinhaAssessmentVariationMicrobial2017 · trail: MB-01 §2.2, §answers · from: MB-01:B-0098, MB-01:A-046, MB-01:I-0011
- **extraction.8** No more than 6% of inoculated lambda DNA was recovered from six soils.
  conf: repl (marker) · class: meas (marker) · holds: six soils; pre-NGS, labelled INDIRECT · src: frostegardQuantificationBiasRelated1999 (AB; meas; repl) · trail: MB-01 §2.2 · from: MB-01:I-0014
- **extraction.9** Extraction method changed soil fingerprint profiles.
  conf: repl (marker) · class: meas (marker) · holds: soil; pre-NGS fingerprinting, labelled INDIRECT · src: martinlaurentDNAExtractionSoils2001 (AB; meas; repl) · trail: MB-01 §2.2 · from: MB-01:I-0015, MB-01:I-0014
- **extraction.10** Extraction yield varied between samples: a synthetic spike-in quantified before and after extraction was recovered at 40% to 84%.
  conf: single (marker) · class: meas (marker) · holds: one spike-in study · src: zembAbsoluteQuantitationMicrobes2020 (FT; meas; single) · trail: MB-01 §2.2, §2.14, §5.5, §answers · from: MB-01:I-0016, MB-01:A-050, MB-01:B-0057, MB-01:B-0192, MB-01:B-0320
- **extraction.11** The consistency of extraction bias across real soil or water matrices has not been measured, and no mock study in a soil matrix with known composition was found; soil evidence comes from spike-ins, dilutions and relic DNA.
  conf: not stated · class: search (note: "has not been measured in the sources found") · holds: lab and bioinformatics angles, Crossref, Europe PMC full text, web search · src: none (a statement about what the search found) · trail: MB-01 §answers · from: MB-01:A-124, MB-01:A-125, MB-01:A-126

### relic-dna: relic (extracellular) DNA
needs: extraction
- **relic-dna.1** Across soils, an average 40% of DNA was extracellular or from non-intact cells; removing it with propidium monoazide showed relic DNA inflated richness by up to 55%, more so at high pH and not at all in some soils, and misestimated relative abundances.
  conf: cont (marker) · class: meas (marker) · holds: soils · src: cariniRelicDNAAbundant2016 (AB; meas; cont) · trail: MB-01 §2.2, §answers, MB-02 §D3.3, §answers · from: MB-01:I-0012, MB-01:A-047, MB-01:B-0056, MB-02:B-0270, MB-02:A-109
- **relic-dna.2** Relic DNA averaged 33% (over 80% in some samples) across soil, sediment, water and mammalian gut but had minimal effect on diversity estimates; models predict bias only when relic and intact abundance distributions differ.
  conf: cont (marker) · class: meas (marker) · holds: soil, sediment, water and mammalian gut · src: lennonHowWhereRelic2018 (FT; meas; cont) · trail: MB-01 §2.2, §7. Bounds, MB-02 §D3.3 · from: MB-01:I-0013, MB-01:B-0351, MB-02:B-0271
- **relic-dna.3** Whether relic DNA distorts diversity estimates is contested: Carini 2016 against Lennon 2018.
  conf: cont (note: "contested") · class: not stated · holds: the two studies above · src: cariniRelicDNAAbundant2016, lennonHowWhereRelic2018 · trail: MB-01 §2.2, §6. Where, MB-02 §D3.3, §answers · from: MB-01:B-0100, MB-01:A-118, MB-01:B-0334, MB-02:B-0269, MB-02:A-118

### primers: primers and gene region
needs: workflow-steps
- **primers.1** Primer and region choices include V1-V2 through V7-V9 and full length, degenerate variants of 515F and 806R, and PNA clamps against host plastids.
  conf: not stated · class: not stated · holds: the primer studies below · src: waltersImprovedBacterial16S2016, abellanschneyderPrimerPipelinesParameters2021, fitzpatrickChloroplastSequenceVariation2018 · trail: MB-01 §answers · from: MB-01:A-006
- **primers.2** In silico, 175 primers and 512 pairs differ widely in coverage and phylum spectrum against SILVA 108.
  conf: repl (marker) · class: deriv (marker) · holds: in silico against SILVA 108 · src: klindworthEvaluationGeneral16S2013 (FT; deriv; repl) · trail: MB-01 §2.3, §answers · from: MB-01:I-0017, MB-01:A-005
- **primers.3** In marine samples, primer bias under-represented SAR11 and over-represented Gammaproteobacteria; the SAR11 bias figures belong to the 515F-Y/806R pair, not the original 515F-C/806R V4 primers to which the review attributes them.
  conf: repl (marker) · class: meas (marker) · holds: marine samples; abstract only · src: paradaEveryBaseMatters2016 (AB; meas; repl) · trail: MB-01 §2.3, MB-01 §Adversarial · from: MB-01:I-0018, MB-01:C-070
- **primers.4** For the 515F-Y/806R pair, SAR11 was under-represented about 4 to 10-fold in marine field samples but only about 2-fold in mocks, so mock-measured bias understated field bias for this taxon; this rests on one abstract, one primer pair and one taxon.
  conf: single (critic: MB-01:C-092) · class: meas (marker) · holds: marine field samples and marine clone mocks; one primer pair (515F-Y/806R) and one taxon (SAR11); abstract only · src: paradaEveryBaseMatters2016 (AB; meas; repl) · trail: MB-01 §2.3, §2.14, §critic, §Adversarial · from: MB-01:C-056, MB-01:C-070, MB-01:C-092, MB-01:C-020, MB-01:B-0104, MB-01:B-0105, MB-01:B-0058, MB-01:B-0190, MB-01:I-0003, MB-01:A-051, MB-01:A-052
- **primers.5** On marine clone mocks, 515F-Y/926R fit expected composition with r2 = 0.95, against about 0.5 for 515F-Y/806R, and even perfectly matched primers showed preferential amplification.
  conf: not stated · class: not stated · holds: marine clone mocks · src: paradaEveryBaseMatters2016 · trail: MB-01 §2.3 · from: MB-01:B-0103, MB-01:B-0106
- **primers.6** Adding degeneracy to 515F and 806R improved detection of Thaumarchaeota (archaea) and SAR11 in stool, soil and built-environment sets without degrading other taxa.
  conf: repl (marker) · class: meas (marker) · holds: stool, soil and built-environment sample sets · src: waltersImprovedBacterial16S2016 (FT; meas; repl) · trail: MB-01 §2.3, §answers · from: MB-01:I-0019, MB-01:A-055
- **primers.7** Whole phyla appeared or disappeared with primer choice: in human stool and mocks with seven primer pairs, Verrucomicrobia appeared only with V3-V4, V4, V6-V8 and V7-V9 primers.
  conf: repl (marker) · class: meas (marker) · holds: human stool and mocks, seven primer pairs · src: abellanschneyderPrimerPipelinesParameters2021 (FT; meas; repl) · trail: MB-01 §2.3, §answers · from: MB-01:I-0020, MB-01:A-054, MB-01:B-0059
- **primers.8** In a gut mock, 55 to 80% of expected species were detected, and 29 to 80% of detected species were misidentified or false hits, depending on primer, platform and extraction.
  conf: not stated · class: not stated · holds: one gut mock · src: fouhy16SRRNAGene2016 · trail: MB-01 §2.3 · from: MB-01:B-0107
- **primers.9** Preferential amplification of a matched template over a mismatched one (63F) rose almost exponentially as annealing temperature went from 47 to 61 C; a perfectly matched primer showed no such effect.
  conf: single (marker) · class: meas (marker) · holds: two-template system; T-RFLP, pre-NGS; abstract only · src: siposEffectPrimerMismatch2007 (AB; meas; single; T-RFLP, pre-NGS) · trail: MB-01 §2.3 · from: MB-01:B-0108, MB-01:I-0021
- **primers.10** With universal PNA clamps, host plastid reads averaged 23% across 32 plant species (plant roots) but reached 62 to 94% in some lineages.
  conf: single (marker) · class: meas (marker) · holds: 32 plant species · src: fitzpatrickChloroplastSequenceVariation2018 (FT; meas; single) · trail: MB-01 §2.3, §answers · from: MB-01:I-0022, MB-01:A-053
- **primers.11** A modified PNA clamp cut Asteraceae plastid contamination from 65% to 23% but raised it from 12% to 69% in other species, and PNA type did not detectably change bacterial alpha or beta diversity.
  conf: not stated · class: not stated · holds: the same plant study · src: fitzpatrickChloroplastSequenceVariation2018 · trail: MB-01 §2.3, §7. Bounds · from: MB-01:B-0109, MB-01:B-0110, MB-01:B-0352
- **primers.12** The makers of PCR clamps state that clamps enrich microbial sequences "without introducing bias".
  conf: not stated · class: not stated · holds: a maker's claim; abstract only · src: lundbergPracticalInnovationsHighthroughput2013 (AB; makers' claim) · trail: MB-01 §2.3 · from: MB-01:B-0111
- **primers.13** In silico, 56% of V4 amplicons failed to match their species of origin with confidence, while full-length sequences classified nearly all correctly.
  conf: single (marker) · class: deriv (marker) · holds: in silico · src: johnsonEvaluation16SRRNA2019 (FT; deriv; single) · trail: MB-01 §2.3 · from: MB-01:I-0023

### pcr: PCR conditions, cycle number and template amount
needs: primers
- **pcr.1** PCR choices include the polymerase, cycle number, input amount and single versus pooled replicate reactions.
  conf: not stated · class: not stated · holds: the PCR studies below · src: none (the reviewer's list of choices) · trail: MB-01 §answers · from: MB-01:A-007, MB-01:A-056
- **pcr.2** Two-template 27F-338R mixtures converged toward 1:1 products regardless of starting ratio; the bias depended strongly on cycle number and fit a kinetic model of product reannealing.
  conf: repl (marker) · class: meas (marker) · holds: two-template mixtures; abstract only · src: suzukiBiasCausedTemplate1996 (AB; meas; repl) · trail: MB-01 §2.4, §answers · from: MB-01:I-0024, MB-01:A-060, MB-01:B-0062
- **pcr.3** Reproducible over-amplification of specific templates in genomic mixtures was explained largely by primer binding energy, not copy number, and was reduced by higher template concentration, fewer cycles and pooling of reactions.
  conf: repl (marker) · class: meas (marker) · holds: genomic mixtures; abstract only · src: polzBiasTemplatetoproductRatios1998 (AB; meas; repl) · trail: MB-01 §2.4 · from: MB-01:I-0025
- **pcr.4** In a 20-strain mock, genomic GC content correlated negatively with observed abundance; longer initial denaturation raised the three highest-GC members but did not change overall evenness.
  conf: single (marker) · class: meas (marker) · holds: one 20-strain mock · src: laursenGenomicGCcontentAffects2017 (FT; meas; single) · trail: MB-01 §2.4, §answers · from: MB-01:B-0112, MB-01:I-0026, MB-01:A-061, MB-01:B-0063
- **pcr.5** High-GC templates were also under-represented in Pinto and Raskin 2012.
  conf: not stated · class: not stated · holds: Pinto and Raskin's mocks · src: pintoPCRBiasesDistort2012 · trail: MB-01 §2.4 · from: MB-01:B-0113
- **pcr.6** In a gut-isolate mock with primer mismatch removed by pre-amplification, log-ratios changed linearly with cycle number from 10 to 35 cycles; after 35 cycles relative abundances were biased by an average factor of 2.6 (95% credible set 2.3 to 2.9), and the B. longum to E. faecalis ratio shifted about 16-fold.
  conf: single (marker) · class: meas (marker) · holds: one gut-isolate mock, 10 to 35 cycles, primer mismatch removed; the per-cycle bias magnitude rests on this study alone · src: silvermanMeasuringMitigatingPCR2021 (FT; meas; single) · trail: MB-01 §2.4, §answers, §critic · from: MB-01:I-0027, MB-01:B-0114, MB-01:A-057, MB-01:A-059, MB-01:B-0060, MB-01:A-132, MB-01:C-054
- **pcr.7** In four artificial-gut communities about 19% of taxa were more than 4-fold biased.
  conf: single (note: "single study") · class: not stated · holds: four artificial-gut communities · src: silvermanMeasuringMitigatingPCR2021 · trail: MB-01 §2.4, §answers · from: MB-01:B-0115, MB-01:A-058, MB-01:B-0061
- **pcr.8** PCR bias was consistent per taxon in the mocks, and calibration corrected composition toward truth in all 10 held-out mocks; the authors note that their mock "ground truth" carried its own bias and that the method sometimes estimated the wrong direction for some taxa.
  conf: not stated · class: not stated · holds: Silverman's gut-isolate mocks · src: silvermanMeasuringMitigatingPCR2021 · trail: MB-01 §2.4, §answers · from: MB-01:B-0116, MB-01:B-0117, MB-01:A-064, MB-01:B-0064
- **pcr.9** Sze and Schloss tested five polymerases at 20 to 35 cycles: in the mock, error rate, chimera fraction and deviation from the expected profile all rose with cycle number; in stool, the sample explained R2 = 0.79 of variation, cycles 0.044 and polymerase 0.033, and "this bias was inconsistent for human stool samples".
  conf: single (marker) · class: meas (marker) · holds: one mock and four stool samples; re-opened and checked by the synthesis agent and the critic · src: szeImpactDNAPolymerase2019 (FT, re-opened; meas; single) · trail: MB-01 §2.4, §2.14, §answers, §critic · from: MB-01:I-0028, MB-01:B-0118, MB-01:B-0119, MB-01:A-065, MB-01:B-0065, MB-01:B-0191, MB-01:B-0332, MB-01:C-020
- **pcr.10** Several studies found cycle number mattered little: template-to-product ratios were little affected by cycle number (Sipos 2007); clone libraries amplified for different numbers of cycles showed no detectable skew (Acinas 2005); 30 versus 35 cycles changed proportions only slightly (Brooks 2015).
  conf: single (marker) · class: meas (marker) · holds: Sipos and Acinas are abstract only, Acinas on Sanger clone libraries; Brooks on the 7-taxon vaginal mock · src: siposEffectPrimerMismatch2007 (AB; meas; single), acinasPCRinducedSequenceArtifacts2005 (AB; meas; single; Sanger), brooksTruthMetagenomicsQuantifying2015 · trail: MB-01 §2.4, §7. Bounds, §answers, §critic · from: MB-01:B-0120, MB-01:I-0029, MB-01:I-0030, MB-01:B-0121, MB-01:A-062, MB-01:B-0349, MB-01:C-013
- **pcr.11** The effect of cycle number is in conflict: small effects (Sipos 2007; Acinas 2005; Brooks 2015) against growing bias (Suzuki 1996; Silverman 2021; Sze and Schloss 2019 mock).
  conf: not stated · class: not stated · holds: listed among the review's conflicts · src: siposEffectPrimerMismatch2007, acinasPCRinducedSequenceArtifacts2005, brooksTruthMetagenomicsQuantifying2015, suzukiBiasCausedTemplate1996, silvermanMeasuringMitigatingPCR2021, szeImpactDNAPolymerase2019 · trail: MB-01 §answers, §6. Where · from: MB-01:A-116, MB-01:B-0331
- **pcr.12** Low template (0.1 ng versus 5 to 10 ng) increased profile variability in soil and faecal samples; pooling of PCRs, preparation day and lane did not.
  conf: single (marker) · class: meas (marker) · holds: soil and faecal samples; abstract only · src: kennedyEvaluatingBiasIlluminabased2014 (AB; meas; single) · trail: MB-01 §2.4, §7. Bounds, §answers · from: MB-01:B-0122, MB-01:I-0031, MB-01:B-0347, MB-01:B-0348, MB-01:A-090, MB-01:B-0248
- **pcr.13** Single versus triplicate pooled PCRs made no significant difference.
  conf: repl (marker) · class: meas (marker) · holds: abstract only; the critic notes an open PMC copy exists, so the AB label understates rather than overstates access · src: marotzTriplicatePCRReactions2019 (AB; meas; repl) · trail: MB-01 §2.4, §Adversarial · from: MB-01:I-0032, MB-01:C-080
- **pcr.14** In fungal ITS, pooling 1 to 16 PCR replicates had no detectable effect on alpha or beta diversity.
  conf: not stated · class: meas (marker) · holds: fungal ITS, labelled INDIRECT · src: smithSequenceDepthNot2014 (FT; meas; INDIRECT) · trail: MB-01 §2.4 · from: MB-01:I-0033
- **pcr.15** Pooled versus single PCR is a disputed choice: Marotz 2019 and Smith and Peay 2014 against the triplicate pooling in the EMP protocol.
  conf: not stated · class: not stated · holds: listed among the disputed choices within steps · src: marotzTriplicatePCRReactions2019, smithSequenceDepthNot2014, earth16SIlluminaAmplicon · trail: MB-01 §answers · from: MB-01:A-024

### pcr-efficiency: PCR cycle numbers and per-cycle amplification efficiency
needs: pcr
- **pcr-efficiency.1** Documented protocols use 35 cycles in triplicate 25 uL reactions, pooling 240 ng per sample (EMP protocol, one-step), or 25 amplicon cycles plus 8 index cycles with 12.5 ng input (Illumina guide, two-step).
  conf: not stated · class: not stated · holds: makers' protocol and documentation; the critic checked the EMP protocol's 35 cycles in triplicate and 240 ng pooling on the live page · src: earth16SIlluminaAmplicon (PROTOCOL), illumina16SMetagenomicSequencing (DOCUMENTATION; maker's claim) · trail: MB-01 §3.1, §2.6, §answers, §critic · from: MB-01:B-0195, MB-01:B-0129, MB-01:B-0130, MB-01:A-008, MB-01:A-134, MB-01:A-135, MB-01:C-023, MB-01:A-170 · rating: "Moderate for documented cycle numbers"
- **pcr-efficiency.2** Experiments span 10 to 35 cycles (Silverman 2021), 15 or 20 to 35 (Sze and Schloss 2019), 20 versus 40 (Salter 2014) and 24 (Laursen 2017).
  conf: not stated · class: not stated · holds: the experimental studies named · src: silvermanMeasuringMitigatingPCR2021, szeImpactDNAPolymerase2019, salterReagentLaboratoryContamination2014, laursenGenomicGCcontentAffects2017 · trail: MB-01 §3.1, §answers · from: MB-01:B-0196, MB-01:A-136
- **pcr-efficiency.3** Only relative per-cycle efficiencies have been measured: Silverman 2021 estimated taxon-specific log-ratio changes per cycle, which compound to an average 2.6-fold bias after 35 cycles in a gut mock.
  conf: single (note: "SINGLE SOURCE") · class: meas (note: "only relative efficiencies have been measured") · holds: one gut mock · src: silvermanMeasuringMitigatingPCR2021 · trail: MB-01 §3.1, §answers · from: MB-01:B-0197, MB-01:B-0198, MB-01:A-137, MB-01:A-138, MB-01:A-171, MB-01:A-185 · rating: "Weak for per-cycle efficiencies"
- **pcr-efficiency.4** Kelly 2019 drew efficiencies from beta distributions fitted to eukaryotic eDNA mocks and modelled amplicons as starting copies x (1 + a_i)^cycles.
  conf: not stated · class: model (marker) · holds: eukaryotic eDNA mocks, labelled INDIRECT · src: kellyUnderstandingPCRProcesses2019 (FT; model; INDIRECT) · trail: MB-01 §3.1, §answers · from: MB-01:I-0078, MB-01:A-139
- **pcr-efficiency.5** No absolute per-cycle efficiency for universal 16S primers on environmental templates was found.
  conf: not stated · class: search (note: "was found by the lab angle") · holds: lab angle, Crossref, Europe PMC, web search; the critic: the qPCR methods literature was not searched, so this reflects only the lab angle's terms · src: none (a statement about what the search found) · trail: MB-01 §3.1, §answers, §Search record, §Adversarial · from: MB-01:B-0199, MB-01:A-140, MB-01:A-171, MB-01:B-0380, MB-01:C-113
- **pcr-efficiency.6** In eukaryotic eDNA work, the PCR process has been modelled, calibrated with mocks, to estimate starting proportions.
  conf: not stated · class: model (marker) · holds: eukaryotic eDNA, labelled INDIRECT; abstract only · src: sheltonTowardQuantitativeMetabarcoding2023 (AB; model; INDIRECT) · trail: MB-01 §5.1 · from: MB-01:I-0111

### copy-number: 16S rRNA gene copies per genome
needs: none
- **copy-number.1** Bacterial genomes carry 1 to about 15 copies of the 16S rRNA gene in every database release and genome survey to about 2015: the first rrnDB release ("can vary from one to as many as 15 copies"), the 2009 release (785 bacterial and 69 archaeal strains) and the 2015 release, Acinas 2004 and Vetrovsky and Baldrian 2013.
  conf: not stated · class: not stated · holds: sequenced genomes; MB-01 rates the copy-number ranges "Moderate" and calls them replicated across rrnDB and GenBank analyses; MB-02's critic: the range is consistent across sources, but those sources draw on overlapping NCBI genome sets, so they are not independent replications · src: klappenbachRrndbRibosomalRNA2001 (AB), leeRrnDBDocumentingNumber2009 (AB), stoddardRrnDBImprovedTools2015 (FT), acinasDivergenceRedundancy16S2004 (AB), vetrovskyVariability16SRRNA2013 (FT) · trail: MB-02 §D1.1, §D1.2, §answers, §critic, MB-01 §3.2, §answers · from: MB-02:B-0021, MB-02:B-0022, MB-02:B-0023, MB-02:B-0067, MB-02:A-001, MB-02:A-009, MB-02:A-017, MB-02:A-126, MB-02:A-129, MB-02:C-001, MB-02:C-006, MB-01:A-141, MB-01:A-142, MB-01:B-0201, MB-01:B-0066, MB-01:A-168, MB-02:B-0024, MB-02:B-0068, MB-02:B-0071 · rating: "Strong for the range and the taxon dependence"
- **copy-number.2** The 2015 rrnDB release held 2,635 bacterial records (1,383 species) and 175 archaeal records (148 species): bacteria 1 to 15 copies, archaea 1 to 4.
  conf: repl (marker) · class: deriv (marker) · holds: rrnDB 2015; archaea on only 148 species · src: stoddardRrnDBImprovedTools2015 (FT; deriv; repl) · trail: MB-01 §3.2, §answers, MB-02 §D1.1 · from: MB-01:I-0079, MB-01:A-144, MB-02:B-0024
- **copy-number.3** Copy-number distributions within a family can be bimodal (Enterobacteriaceae 1 to 9, with a low-copy peak made up of insect symbionts), and means over all genomes mislead because some species are over-represented.
  conf: not stated · class: not stated · holds: rrnDB 2015 (Stoddard 2015) · src: stoddardRrnDBImprovedTools2015 · trail: MB-01 §3.2, MB-02 §D1.1 · from: MB-01:B-0202, MB-02:B-0025, MB-02:B-0026
- **copy-number.4** Among 301 species with at least two genome records in rrnDB (Stoddard 2015), 77% had identical copy counts, 16% differed by one copy and 3% by more than two.
  conf: not stated · class: deriv (note: "derived class") · holds: 301 species; the answers date the 77% figure to 2014; the note also says measured from genomes · src: stoddardRrnDBImprovedTools2015 · trail: MB-02 §D1.1, §answers · from: MB-02:B-0027, MB-02:A-006
- **copy-number.5** From version 5.0 onward, rrnDB counts 16S genes by BLAST against gap-free NCBI assemblies rather than from annotation, so its genome records report 16S gene counts only, not operons or 23S counts.
  conf: not stated · class: not stated · holds: rrnDB About page · src: schmidtlaboratoryRrnDBReleaseFiles · trail: MB-02 §D1.1, §answers · from: MB-02:B-0028, MB-02:B-0029, MB-02:A-008
- **copy-number.6** In the reviewer's summary of the rrnDB release files, bacterial records and ranges were: v3.1.227, 1,297 records, 1 to 15, record mean 4.20 (median 3), 17.5% of records at one copy, mean of species means 3.87, archaea 1 to 4 (species mean 1.66); v4.4.3, 2,700, 1 to 15, 4.20 (4), 15.6%, 3.92, archaea 1 to 4 (1.66); v5.0, 5,856, 1 to 16, 4.60 (4), 13.3%, 4.04, archaea 1 to 4 (1.72); v5.6, 15,462, 1 to 21, 5.04 (5), 9.3%, 4.26, archaea 1 to 5 (1.66); v5.10, 48,053, 1 to 22, 5.52 (6), 7.5%, 4.36, archaea 1 to 5 (1.73).
  conf: not stated · class: deriv (note: "derived by the reviewer") · holds: release files downloaded and summarised by the reviewer (v5.10 dated June 2025, 48,077 bacterial and 623 archaeal records per the home page); species grouped by the first two words of the NCBI name, which is approximate · src: schmidtlaboratoryRrnDBReleaseFiles (FT; statistics derived by reviewer) · trail: MB-02 §D1.1, §Search record · from: MB-02:B-0030, MB-02:B-0031, MB-02:B-0032, MB-02:B-0033, MB-02:B-0034, MB-02:B-0035, MB-02:B-0036, MB-02:B-0037, MB-02:B-0038, MB-02:B-0306, MB-02:B-0307
- **copy-number.7** The long-quoted bacterial ceiling of 15 is no longer the database maximum: rrnDB v5.6 contains a Photobacterium damselae genome with 21 copies and v5.10 a Mesobacillus maritimus genome with 22, and several Photobacterium and Bacillaceae genomes have 20 to 21; no source checked whether these extremes survive scrutiny of assembly quality.
  conf: not stated · class: deriv (critic: MB-02:C-007) · holds: rrnDB v5.6 and v5.10; the reviewer's own derivation from rrnDB, with no published check against assembly quality; the critic: acceptable as labelled derived, but the answer leads with these computations over published values · src: schmidtlaboratoryRrnDBReleaseFiles (FT; statistics derived by reviewer) · trail: MB-02 §D1.1, §answers, §critic, §Adversarial · from: MB-02:B-0039, MB-02:B-0040, MB-02:B-0041, MB-02:B-0043, MB-02:A-011, MB-02:A-018, MB-02:A-130, MB-02:C-007, MB-02:C-141
- **copy-number.8** Archaea carry 1 to 4 copies in rrnDB up to v5.0 and 1 to 5 from v5.6 (Natronorubrum, Natrinema, Methanococcoides, Methanolobus and others); Acinas et al. 2004 already reported a maximum of five archaeal operons, so the review's sources conflict on the archaeal maximum.
  conf: cont (critic: MB-02:C-002) · class: not stated · holds: rrnDB releases and Acinas 2004 (abstract only); the rrnDB series is not the whole record · src: schmidtlaboratoryRrnDBReleaseFiles, acinasDivergenceRedundancy16S2004 (AB) · trail: MB-02 §D1.1, §D1.2, §answers, §critic, §Adversarial · from: MB-02:B-0042, MB-02:B-0070, MB-02:A-002, MB-02:A-127, MB-02:C-002, MB-02:C-138
- **copy-number.9** Record-level means rise across rrnDB releases (4.2 in v3.1.227 to 5.5 in v5.10) mainly because of resequencing effort: in v5.10 E. coli contributes 3,902 records (3,860 at 7 copies), Klebsiella pneumoniae 2,534 (mostly 8) and Salmonella enterica 1,770 (mostly 7); species-level means move much less (3.9 to 4.4).
  conf: not stated · class: deriv (note: "derived") · holds: the reviewer's derivation from rrnDB; the means depend on which genomes are counted (record versus species level) and on assembly completeness · src: schmidtlaboratoryRrnDBReleaseFiles · trail: MB-02 §D1.1, §answers · from: MB-02:B-0044, MB-02:B-0045, MB-02:B-0046, MB-02:A-005, MB-02:A-010, MB-02:A-012, MB-02:A-016 · rating: "Moderate for exact means and shares"
- **copy-number.10** In rrnDB v5.10 the mean of species means is 4.4 (median 4) for bacteria and 1.7 (median 1) for archaea, and 11.3% of bacterial species and 51.6% of archaeal species average one copy.
  conf: not stated · class: deriv (note: "derived") · holds: rrnDB v5.10, the reviewer's derivation; rests on rrnDB alone · src: schmidtlaboratoryRrnDBReleaseFiles · trail: MB-02 §D1.1, §answers · from: MB-02:B-0047, MB-02:A-003, MB-02:A-128
- **copy-number.11** Across 1,690 bacterial genomes (7,081 16S sequences extracted in silico; 909 species, GenBank 2012), copy number ranged from 1 to 15 with a mean of 4.2; 15% of genomes carried one copy and 21% two; phylum and class means were Acidobacteria 1.0, Alphaproteobacteria 2.2, Deltaproteobacteria 2.7, Actinobacteria 3.1, Betaproteobacteria 3.3, Bacteroidetes 3.5, Firmicutes 5.8 and Gammaproteobacteria 5.8.
  conf: not stated · class: deriv (note: "derived") · holds: 1,690 genomes, GenBank 2012; the genome collection is skewed · src: vetrovskyVariability16SRRNA2013 (FT) · trail: MB-01 §3.2, §answers, MB-02 §D1.2, §answers, §critic · from: MB-01:B-0203, MB-01:B-0204, MB-01:A-143, MB-02:B-0071, MB-02:B-0072, MB-02:A-003, MB-02:A-004, MB-02:C-057
- **copy-number.12** Copy number was less conserved across taxonomic levels than genome size.
  conf: not stated · class: not stated · holds: the same 1,690 genomes · src: vetrovskyVariability16SRRNA2013 · trail: MB-02 §D1.2 · from: MB-02:B-0073
- **copy-number.13** The Acidobacteria mean of 1.0 rests on 4 genomes from 4 species, and the rrnDB v5.10 Acidobacteriota mean of 1.4 on 29 species; these soil-relevant low values are imprecise.
  conf: not stated · class: not stated · holds: Vetrovsky and Baldrian's Table 1 and rrnDB v5.10 · src: vetrovskyVariability16SRRNA2013, schmidtlaboratoryRrnDBReleaseFiles · trail: MB-02 §critic, §Adversarial, §D1.1 · from: MB-02:C-003, MB-02:C-004, MB-02:C-005, MB-02:C-089, MB-02:B-0058
- **copy-number.14** Taxon dependence is the strongest regularity: per-phylum species means in rrnDB v5.10 are Bacillota 6.9 (1,274 species), Pseudomonadota 4.4 (3,050), Bacteroidota 3.8 (662), Actinomycetota 3.5 (1,334), Cyanobacteriota 2.8 (102), Planctomycetota 2.0 (62), Verrucomicrobiota 1.8 (35), Chloroflexota 1.6 (20), Acidobacteriota 1.4 (29), Euryarchaeota 1.9 (332), Thermoproteota 1.0 (65) and Nitrososphaerota 1.1 (18).
  conf: not stated · class: deriv (note: "derived") · holds: rrnDB v5.10, the reviewer's derivation · src: schmidtlaboratoryRrnDBReleaseFiles · trail: MB-02 §D1.1, §answers · from: MB-02:B-0048, MB-02:B-0049, MB-02:B-0050, MB-02:B-0051, MB-02:B-0052, MB-02:B-0053, MB-02:B-0054, MB-02:B-0055, MB-02:B-0056, MB-02:B-0057, MB-02:B-0059, MB-02:B-0060, MB-02:B-0061, MB-02:A-004, MB-02:B-0058
- **copy-number.15** Phyla common in soil but poorly represented among genomes (Acidobacteriota, Verrucomicrobiota, Chloroflexota) sit at the low end of copy number, on small numbers of species.
  conf: not stated · class: not stated · holds: rrnDB v5.10 · src: schmidtlaboratoryRrnDBReleaseFiles · trail: MB-02 §D1.1 · from: MB-02:B-0062
- **copy-number.16** Within species, rrnDB v5.10 is less uniform than the 2015 release: of 1,038 species with at least five genomes, 44% show some variation, although the median range is 0; the 2015 figure of 77% identical used far fewer genomes.
  conf: not stated · class: deriv (note: "derived") · holds: rrnDB v5.10, the reviewer's derivation · src: schmidtlaboratoryRrnDBReleaseFiles, stoddardRrnDBImprovedTools2015 · trail: MB-02 §D1.1, §answers · from: MB-02:B-0063, MB-02:B-0064, MB-02:B-0066, MB-02:A-006, MB-02:A-013
- **copy-number.17** In the reviewer's reading, part of the within-species variation in rrnDB v5.10 is likely assembly error rather than biology: for example, 18 of 3,902 E. coli records report a single copy.
  conf: not stated · class: reading (note: "In the reviewer's reading") · holds: rrnDB v5.10; not a tested claim · src: schmidtlaboratoryRrnDBReleaseFiles · trail: MB-02 §D1.1, §answers · from: MB-02:B-0065, MB-02:A-013
- **copy-number.18** Acinas et al. 2004 found up to 15 operons in bacteria, with copy numbers up to 7 common and about 40% of organisms having one or two operons; a single operon dominated in archaea.
  conf: not stated · class: not stated · holds: genome survey; abstract only · src: acinasDivergenceRedundancy16S2004 (AB) · trail: MB-02 §D1.2 · from: MB-02:B-0068, MB-02:B-0069, MB-02:B-0070
- **copy-number.19** 16S copy number shows moderate phylogenetic signal (K = 0.48 on 484 taxa), and copy number is "strongly linked" to taxonomy across 2,900 genomes, with Archaea potentially under-represented in amplicon profiles.
  conf: not stated · class: not stated · holds: Kembel 2012 (full text) and Angly 2014 (abstract only) · src: kembelIncorporating16SGene2012 (FT), anglyCopyRighterRapidTool2014 (AB) · trail: MB-02 §D1.2, §critic · from: MB-02:B-0074, MB-02:B-0075, MB-02:C-057
- **copy-number.20** 16S gene count and operon count diverge where rRNA genes are unlinked: unlinked 16S and 23S genes are common in Deinococcus-Thermus, Chloroflexi and Planctomycetes, and up to 41% of rRNA genes in soil long-read metagenomes were unlinked, against none in human gut.
  conf: single (note: "SINGLE SOURCE") · class: not stated · holds: long-read metagenomes; one abstract-only source for the soil figure · src: brewerUnlinkedRRNAGenes2020 (AB) · trail: MB-02 §D1.2, §answers, §Adversarial · from: MB-02:B-0076, MB-02:B-0077, MB-02:B-0078, MB-02:B-0079, MB-02:A-007, MB-02:A-019, MB-02:A-131, MB-02:C-093
- **copy-number.21** Copy number tracks ecological strategy: soil isolates that formed colonies quickly averaged 5.5 copies and slow responders 1.4.
  conf: single (critic: MB-01:C-091) · class: meas (marker) · holds: soil isolates; one abstract-only study; MB-02 calls it a measured association, cited as context · src: klappenbachRRNAOperonCopy2000 (AB; meas; repl) · trail: MB-01 §3.2, §answers, §Adversarial, MB-02 §D1.2 · from: MB-01:B-0205, MB-01:I-0080, MB-01:A-145, MB-01:C-091, MB-02:B-0084, MB-02:B-0085, MB-02:B-0087
- **copy-number.22** Maximum reproductive rate doubles with a doubling of rrn copy number across 1,167 species.
  conf: single (marker) · class: meas (marker) · holds: 1,167 species; abstract only · src: rollerExploitingRRNAOperon2016 (AB; meas; single) · trail: MB-01 §3.2, MB-02 §D1.2 · from: MB-01:I-0081, MB-02:B-0086
- **copy-number.23** Copy numbers for uncultured lineages without genomes (for example many soil Acidobacteriota, Verrucomicrobiota, Chloroflexota and candidate phyla) are not measured, genome databases over-represent cultured, clinically and industrially relevant taxa, and no source measured 16S copy number directly in environmental populations of soil archaea beyond genomes of cultured or enriched Nitrososphaerota; the archaeal copy-number distribution beyond its 1 to 4 range was not found.
  conf: not stated · class: search (note: "No source found measured 16S copy number directly") · holds: the searches in both notes' search records · src: loucaCorrecting16SRRNA2018 · trail: MB-02 §answers, MB-01 §answers · from: MB-02:A-014, MB-02:A-015, MB-02:A-132, MB-01:A-178

### ploidy: genome copies, and hence 16S copies, per cell
needs: copy-number
- **ploidy.1** In cultures, genome copies per cell range from about one (Caulobacter, Wolinella, crenarchaea) to tens or hundreds (P. putida, haloarchaea, methanogens, Synechocystis) and depend on taxon, growth rate and phase; copy number does not change in one direction with growth phase.
  conf: not stated · class: not stated · holds: cultures; apart from Pecoraro 2011 the evidence rests largely on abstracts and on one laboratory's qPCR method · src: pecoraroQuantificationPloidyProteobacteria2011 (FT), hildenbrandGenomeCopyNumbers2011 (AB), breuertRegulatedPolyploidyHalophilic2006 (AB), griesePloidyCyanobacteria2011 (AB), zerullaPloidyLevelSynechocystis2016 (AB) · trail: MB-02 §D1.3, §answers, §critic · from: MB-02:C-008, MB-02:C-009, MB-02:C-014, MB-02:A-020, MB-02:A-134, MB-02:A-039 · rating: "Evidence is moderate, not strong"
- **ploidy.2** Most direct measurements of genome copies per cell come from one laboratory's real-time PCR protocol (Soppa group), in several studies cross-checked against Southern blots, flow cytometry or published E. coli values.
  conf: single (note: "one laboratory") · class: meas (note: "All figures below are measured") · holds: cultures; Pecoraro 2011 full text, the other Soppa-group studies abstract only · src: pecoraroQuantificationPloidyProteobacteria2011 (FT), bottingerRegulatedPloidyBacillus2018 (AB), breuertRegulatedPolyploidyHalophilic2006 (AB), hildenbrandGenomeCopyNumbers2011 (AB), griesePloidyCyanobacteria2011 (AB), zerullaPloidyLevelSynechocystis2016 (AB), bruckOneAdvantageBeing2023 (AB), zerullaPolyploidyHaloarchaeaAdvantages2014 (AB) · trail: MB-02 §D1.3, §answers · from: MB-02:B-0088, MB-02:B-0089, MB-02:B-0090, MB-02:A-029, MB-02:A-035
- **ploidy.3** Monoploid examples: Caulobacter crescentus (about 2.1 genome-equivalents at a mid-chromosome locus at 93 min doubling, consistent with one chromosome plus replication), Wolinella succinogenes (about 0.9 at 96 min) and six crenarchaeal species of four genera.
  conf: not stated · class: meas (note: "All figures below are measured") · holds: cultures; Pecoraro 2011 full text (checked by the critic), Hildenbrand 2011 abstract only · src: pecoraroQuantificationPloidyProteobacteria2011 (FT), hildenbrandGenomeCopyNumbers2011 (AB) · trail: MB-02 §D1.3, §answers, §critic · from: MB-02:B-0090, MB-02:B-0094, MB-02:B-0095, MB-02:B-0103, MB-02:A-021, MB-02:C-057
- **ploidy.4** Growth-rate-dependent merodiploidy: E. coli has 6.8 origins and 1.7 termini per cell at 25 min doubling but 2.5 origins and 1.2 termini at 103 min; B. subtilis (5.9 origins, 1.2 termini) and three soil Bacillus and Paenibacillus isolates are mero-oligoploid in exponential phase and down-regulate origins in stationary phase.
  conf: not stated · class: meas (note: "All figures below are measured") · holds: cultures; Pecoraro 2011 is the only direct origin and terminus count for E. coli at two growth rates · src: pecoraroQuantificationPloidyProteobacteria2011 (FT), bottingerRegulatedPloidyBacillus2018 (AB) · trail: MB-02 §D1.3, §answers · from: MB-02:B-0090, MB-02:B-0092, MB-02:B-0097, MB-02:A-022, MB-02:A-036
- **ploidy.5** Polyploids: Pseudomonas putida about 20 origins and 14 termini (46 min doubling); Synechococcus PCC 7942 and WH7803 3 to 4 copies; Synechocystis PCC 6803 218 (exponential) to 58 (stationary) in one substrain and about 20 to 4 across six substrains; Halobacterium salinarum 25 to 15 and Haloferax volcanii 18 to 10 (exponential to stationary); Methanococcus maripaludis up to 55 (exponential) and about 30 (stationary); Methanosarcina acetivorans 17 (fast) and 3 (slow growth).
  conf: not stated · class: meas (note: "All figures below are measured") · holds: cultures; P. putida from Pecoraro 2011 (full text), the rest abstract only · src: pecoraroQuantificationPloidyProteobacteria2011 (FT), griesePloidyCyanobacteria2011 (AB), zerullaPloidyLevelSynechocystis2016 (AB), breuertRegulatedPolyploidyHalophilic2006 (AB), hildenbrandGenomeCopyNumbers2011 (AB) · trail: MB-02 §D1.3, §answers · from: MB-02:B-0090, MB-02:B-0096, MB-02:B-0098, MB-02:B-0099, MB-02:B-0100, MB-02:B-0101, MB-02:B-0102, MB-02:A-023
- **ploidy.6** Under phosphate starvation, polyploid down-regulation stops at about five copies in Zymomonas mobilis, Azotobacter vinelandii and H. salinarum rather than reaching monoploidy, but goes to one copy in Synechocystis after prolonged phosphate starvation.
  conf: not stated · class: meas (note: "All figures below are measured") · holds: phosphate-starved stationary cultures; abstracts only · src: bruckOneAdvantageBeing2023 (AB), zerullaPloidyLevelSynechocystis2016 (AB) · trail: MB-02 §D1.3, §answers · from: MB-02:B-0090, MB-02:B-0104, MB-02:A-033, MB-02:B-0099
- **ploidy.7** E. coli stationary-phase batch cultures always contained some multi-chromosome cells, even after days.
  conf: not stated · class: meas (note: "All figures below are measured") · holds: batch cultures; abstract only · src: akerlundAnalysisCellSize1995 (AB) · trail: MB-02 §D1.3, §answers · from: MB-02:B-0090, MB-02:B-0093, MB-02:A-024
- **ploidy.8** Copy number does not always fall in stationary phase: Azotobacter vinelandii is reported to rise from about 4 copies in exponential phase to about 80 in stationary phase, and M. acetivorans from 2.5 to 5 (Bruck 2023 full text, secondary via the critic); Pecoraro 2011 Table 5 gives A. vinelandii as 1 (up to 8) copies in slow growth and 40 in fast growth, attributed to another laboratory.
  conf: not stated · class: not stated · holds: cultures; reported by the critic from full texts the review did not use (Bruck 2023 labelled AB, Pecoraro Table 5 not reported) · src: bruckOneAdvantageBeing2023 (AB), pecoraroQuantificationPloidyProteobacteria2011 (FT) · trail: MB-02 §critic, §Adversarial · from: MB-02:C-010, MB-02:C-011, MB-02:C-012, MB-02:C-064, MB-02:C-072, MB-02:C-073, MB-02:C-074, MB-02:C-128, MB-02:C-129
- **ploidy.9** Measurements outside the Soppa laboratory exist and are listed in Pecoraro 2011: Azotobacter (40 copies in fast growth), Desulfovibrio (9 to 17), Neisseria (3 to 4), Buchnera (120), and polyploid Deinococcus, Borrelia and rhizobial bacteroids.
  conf: not stated · class: not stated · holds: Pecoraro 2011, read in full by the review but this part not reported · src: pecoraroQuantificationPloidyProteobacteria2011 (FT) · trail: MB-02 §critic, §Adversarial · from: MB-02:C-013, MB-02:C-075, MB-02:C-131
- **ploidy.10** Pecoraro et al. found only three to four of 11 proteobacterial species with measured ploidy to be monoploid, with no correlation to genome size, temperature or lifestyle; Hildenbrand et al. found none of seven euryarchaeal species monoploid, against all six crenarchaeal species.
  conf: not stated · class: not stated · holds: cross-study patterns in the source abstracts (Pecoraro full text) · src: pecoraroQuantificationPloidyProteobacteria2011 (FT), hildenbrandGenomeCopyNumbers2011 (AB) · trail: MB-02 §D1.3, §Adversarial · from: MB-02:B-0105, MB-02:B-0106, MB-02:B-0107, MB-02:C-076
- **ploidy.11** Single-cell measurements in H. salinarum showed wide cell-to-cell variation in genome copy number, larger in exponential than in stationary phase; the review read only the abstract, which gives no per-cell shares, although the open full text reports single-cell CLSM and FACS distributions.
  conf: not stated · class: not stated · holds: H. salinarum cultures · limit: access (critic: MB-02:C-071) · src: breuertRegulatedPolyploidyHalophilic2006 (AB) · trail: MB-02 §D1.3, §Adversarial · from: MB-02:B-0108, MB-02:C-069, MB-02:C-070, MB-02:C-071
- **ploidy.12** rRNA operons cluster near the replication origin in fast-growing bacteria, and gene-dosage effects shape this placement.
  conf: not stated · class: not stated · holds: genome analysis; abstract only · src: couturierReplicationassociatedGeneDosage2006 (AB) · trail: MB-02 §D1.3 · from: MB-02:B-0110
- **ploidy.13** That 16S copies per cell scale with origin number more than with genome number in fast growers is the reviewer's inference from one abstract; no source in the review measures 16S copies per cell against origin number.
  conf: not stated · class: reading (critic: MB-02:C-140) · holds: inference from Couturier and Rocha 2006 (abstract only) · src: couturierReplicationassociatedGeneDosage2006 (AB) · trail: MB-02 §D1.3, §answers, §critic, §Adversarial · from: MB-02:B-0111, MB-02:A-025, MB-02:C-015, MB-02:C-088, MB-02:C-140
- **ploidy.14** For E. coli, rRNA genes per genome equivalent range from about 7.9 to 9.5 across growth rates.
  conf: not stated · class: not stated · holds: E. coli; secondary, Bremer and Dennis (1996) Table 3 as reported by BioNumbers · src: bremerModulationChemicalComposition1996 (SEC), bionumbersAverageNumberRRNA (SEC) · trail: MB-02 §D1.3, §answers · from: MB-02:B-0112, MB-02:B-0113, MB-02:A-025
- **ploidy.15** No source measured 16S copies per cell directly in environmental cells, and in environmental samples the evidence on genome copies per cell is indirect and sparse: DNA mass per cell in soil, DNA-content populations in seawater and population-average replication indices in groundwater.
  conf: not stated · class: search (note: "No source I found measured 16S copies per cell directly in environmental cells") · holds: the searches behind MB-02's not-found claims; mostly non-soil, single study per setting · src: none (a statement about what the search found) · trail: MB-02 §D1.3, §answers, §critic · from: MB-02:B-0114, MB-02:B-0115, MB-02:A-030, MB-02:A-137, MB-02:C-016 · rating: "Weak for environmental samples"
- **ploidy.16** Indigenous soil bacteria extracted from a clay loam contained 1.5 to 15 fg DNA per cell by flow cytometry, most below 4 fg, with an average around 2 fg; larger cells, and cells that grew in soil extract, had more DNA. This confirms earlier work by the same group (Bakken and Olsen 1989).
  conf: not stated · class: not stated · holds: one clay loam; abstract only; Christensen 1995 is the only soil measurement of DNA per cell · src: christensenFlowCytometricMeasurements1995 (AB), bakkenDNAcontentSoilBacteria1989 (SEC) · trail: MB-02 §D1.3, §answers, §critic · from: MB-02:B-0116, MB-02:B-0117, MB-02:B-0118, MB-02:A-026, MB-02:A-037, MB-02:C-058
- **ploidy.17** DNA mass per cell cannot separate genome size from copy number.
  conf: not stated · class: not stated · holds: soil DNA-per-cell measurements · src: christensenFlowCytometricMeasurements1995 · trail: MB-02 §D1.3, §answers · from: MB-02:B-0119, MB-02:A-032
- **ploidy.18** In the reviewer's reading, about 2 fg of DNA is less than one copy of a 4 Mb genome, which suggests many soil cells hold one copy of a small genome; the note marks this as inference.
  conf: not stated · class: reading (note: "In the reviewer's reading") · holds: the clay-loam DNA-per-cell average · src: christensenFlowCytometricMeasurements1995 · trail: MB-02 §D1.3 · from: MB-02:B-0120
- **ploidy.19** A typical seawater sample had a mean of 2.5 fg DNA per cell, in two populations described as 1n and 2n clusters, with 10 to 30% low-DNA "dim" cells; the two populations could reflect replicating monoploid cells or larger genomes, and the authors treat increased copy number with growth rate in nature as "likely", an inference rather than a measurement.
  conf: not stated · class: not stated · holds: seawater; full text read to 100,000 characters · src: buttonDeterminationDNAContent2001 (FT, first 100,000 characters) · trail: MB-02 §D1.3, §answers · from: MB-02:B-0121, MB-02:B-0122, MB-02:A-026, MB-02:A-032, MB-02:A-035
- **ploidy.20** In Prochlorococcus in the equatorial Pacific, DNA replication occurred in the afternoon, in phase with the light cycle, and division at night; the abstract read gives no share of cells.
  conf: not stated · class: not stated · holds: equatorial Pacific; abstract only · limit: access (critic: MB-02:C-080) · src: vaulotGrowthProchlorococcusPhotosynthetic1995 (AB) · trail: MB-02 §D1.3, §answers, §Adversarial · from: MB-02:B-0123, MB-02:A-026, MB-02:C-078, MB-02:C-079, MB-02:C-080
- **ploidy.21** Flow cytometric cell-cycle analyses of Prochlorococcus (and Synechococcus) in situ are by method taxon-specific measurements of the share of cells with replicated DNA (G1 versus S/G2), so the review's statement that no such share exists for any natural community is not established; nothing comparable was found for soil.
  conf: not stated · class: not stated · holds: marine picocyanobacteria in situ; read only at abstract level by the review · limit: access (critic: MB-02:C-018) · src: vaulotGrowthProchlorococcusPhotosynthetic1995 (AB) · trail: MB-02 §critic, §Adversarial · from: MB-02:C-017, MB-02:C-018, MB-02:C-019, MB-02:C-106, MB-02:C-107
- **ploidy.22** In groundwater metagenomes, population-average replication indices (iRep) were mostly low: Candidate Phyla Radiation bacteria had a median iRep of 1.34, and only 16.1% of values exceeded 1.5; the authors interpret an iRep of 1.25 as about a quarter of cells replicating.
  conf: not stated · class: not stated · holds: groundwater; full text read to 100,000 characters; the only environmental replication-index figure · src: brownMeasurementBacterialReplication2016 (FT, first 100,000 characters) · trail: MB-02 §D1.3, §answers · from: MB-02:B-0124, MB-02:B-0125, MB-02:B-0126, MB-02:A-026, MB-02:A-038, MB-02:A-035
- **ploidy.23** Gut metagenome peak-to-trough ratios track growth rate in culture and in vivo.
  conf: not stated · class: not stated · holds: gut; abstract only · src: koremGrowthDynamicsGut2015 (AB) · trail: MB-02 §D1.3 · from: MB-02:B-0127
- **ploidy.24** Not found: genome copies per cell for named soil bacterial or archaeal taxa in situ; the share of single-copy cells in soil, rhizosphere or dormant natural populations; any direct measurement of 16S copies per cell in environmental cells; ploidy of cultured soil Acidobacteriota, Verrucomicrobiota or Nitrososphaerota; replication indices (iRep or peak-to-trough) for soil metagenomes.
  conf: not stated · class: search (note: "no source found by the searches used") · holds: Europe PMC queries combining iRep, peak-to-trough, GRiD or CoPTR with soil; WebSearch on soil iRep, rewetting and permafrost; WebSearch on environmental genome copies per cell and flow cytometry · src: none (a statement about what the search found) · trail: MB-02 §D1.3, §answers, §Search record · from: MB-02:B-0128, MB-02:A-034, MB-02:A-138, MB-02:B-0297, MB-02:B-0009
- **ploidy.25** That no natural community has a taxon-specific measurement of the share of cells by genome copy number is not established: in situ flow cytometric cell-cycle analyses of Prochlorococcus are by method taxon-specific measurements of the share of cells with replicated DNA, and the review read only their abstract. Nothing comparable was found for soil.
  conf: not stated · class: search (critic: MB-02:C-018) · holds: natural communities; the Prochlorococcus analyses were read only at abstract level, so the review's search result that the share "is not reported by taxon for any natural community in the sources reached" does not stand as stated · limit: access (critic: MB-02:C-018) · src: vaulotGrowthProchlorococcusPhotosynthetic1995 (AB) · trail: MB-02 §critic, §D1.3, §answers · from: MB-02:B-0129, MB-02:A-027, MB-02:B-0011, MB-02:C-017, MB-02:C-018, MB-02:C-019

### copy-number-correction: 16S copy number and read-based abundance; prediction and correction
needs: copy-number, pcr
- **copy-number-correction.1** Copy number is a property of each taxon rather than a workflow step, but it acts through PCR.
  conf: not stated · class: not stated · holds: the note's framing of section 2.5 · src: none (the reviewer's framing) · trail: MB-01 §2.5 · from: MB-01:B-0124
- **copy-number-correction.2** With equimolar DNA from species pairs, PCR product ratios matched rrn genes per unit DNA for two pairs but deviated for a Bacillus pair.
  conf: not stated · class: meas (note: "measured") · holds: species-pair DNA mixtures; abstract only · src: farrellyEffectGenomeSize1995 (AB) · trail: MB-02 §D1.4, §answers · from: MB-02:B-0130, MB-02:A-040
- **copy-number-correction.3** Copy-number prediction is accurate only near sequenced relatives: copy-number autocorrelation fell below 0.5 at about 15% 16S divergence and reached zero at about 30%; about 49% of SILVA OTUs are more than 15% from a sequenced genome; PICRUSt, CopyRighter and PAPRICA sometimes explained under 10% of variance against complete genomes and disagreed with each other (R2 below 0.5) for most of 635 communities, which included soils; the authors recommend against default correction unless OTUs are close to sequenced genomes.
  conf: repl (marker) · class: deriv (marker) · holds: about 6,800 genomes and 635 communities including soils; the quantitative thresholds (15% and 30%) rest on Louca 2018 alone, though the qualitative distance effect is replicated; figures checked by MB-02's critic · src: loucaCorrecting16SRRNA2018 (FT; deriv; repl) · trail: MB-01 §2.5, §3.2, §answers, MB-02 §D1.4, §answers, §critic · from: MB-01:I-0037, MB-01:B-0211, MB-01:A-069, MB-01:A-153, MB-01:B-0068, MB-01:B-0359, MB-02:B-0135, MB-02:B-0136, MB-02:B-0137, MB-02:B-0138, MB-02:B-0139, MB-02:B-0140, MB-02:A-041, MB-02:A-057, MB-02:A-140, MB-02:C-021, MB-02:C-057
- **copy-number-correction.4** The distance-dependence of prediction accuracy is consistent across four independent analyses (Kembel 2012, Louca 2018, Edgar 2017, Gao and Wu 2023).
  conf: repl (note: "consistent across four independent analyses") · class: not stated · holds: the four analyses named · src: kembelIncorporating16SGene2012 (FT), loucaCorrecting16SRRNA2018 (FT), edgarUNBIASAttemptCorrect2017 (AB), gaoAccounting16SRRNA2023 (FT) · trail: MB-02 §answers · from: MB-02:A-048, MB-02:B-0133, MB-02:B-0135, MB-02:B-0141, MB-02:B-0142
- **copy-number-correction.5** Phylogenetic copy-number prediction had a leave-one-out error of about one copy, and in 100 simulated communities correction raised the correlation with true organism abundance from r = 0.70 to 0.81.
  conf: cont (marker) · class: model (marker) · holds: simulated communities; figures checked by MB-02's critic · src: kembelIncorporating16SGene2012 (FT; model; cont) · trail: MB-01 §2.5, §answers, MB-02 §D1.4, §answers, §critic · from: MB-01:I-0036, MB-01:A-070, MB-02:B-0133, MB-02:B-0134, MB-02:A-042, MB-02:A-043, MB-02:C-057
- **copy-number-correction.6** In Kembel's data, correction moved ear samples to cluster with nostrils rather than feet but left ocean clustering largely unchanged.
  conf: not stated · class: not stated · holds: human body sites and ocean · src: kembelIncorporating16SGene2012 (FT) · trail: MB-02 §D1.4, §answers · from: MB-02:B-0151, MB-02:A-045
- **copy-number-correction.7** Gao and Wu report a prediction precision of about 0.96 at small distances, with uncertainty rising with distance; correction raised the chance of identifying the true most abundant OTU from 13% to 65% in simulations.
  conf: not stated · class: not stated · holds: simulations; figures checked by MB-02's critic · src: gaoAccounting16SRRNA2023 (FT) · trail: MB-02 §D1.4, §answers, §critic · from: MB-02:B-0141, MB-02:A-042, MB-02:A-043, MB-02:C-057
- **copy-number-correction.8** Correction improves fit to simulated truth (Kembel 2012; Gao and Wu 2023).
  conf: not stated · class: not stated · holds: simulations · src: kembelIncorporating16SGene2012, gaoAccounting16SRRNA2023 · trail: MB-02 §critic, §answers · from: MB-02:C-020, MB-02:C-021, MB-02:A-141
- **copy-number-correction.9** Correction changed the identity of the most abundant OTU in about 20% of Human Microbiome Project and 31% of Earth Microbiome Project communities, but against predicted, not measured, truth; in simulations it reduced sample shifts in ordinations but left PERMANOVA variance explained essentially unchanged (5.27 to 19.65% true versus 5.27 to 19.82% uncorrected).
  conf: not stated · class: not stated · holds: HMP and EMP communities and simulations; the only figures on how often correction changes the dominant taxon in real communities · src: gaoAccounting16SRRNA2023 (FT) · trail: MB-02 §D1.4, §answers, §critic · from: MB-02:B-0149, MB-02:B-0150, MB-02:A-045, MB-02:A-052, MB-02:A-058, MB-02:A-142, MB-02:C-023, MB-02:C-024
- **copy-number-correction.10** CopyRighter's correction improved agreement with mock communities and metagenomes, changed qPCR totals and diversity estimates, and reclassified twin gut samples from two enterotypes to three.
  conf: not stated · class: not stated · holds: the tool's own paper; abstract only · src: anglyCopyRighterRapidTool2014 (AB) · trail: MB-02 §D1.4, §answers · from: MB-02:B-0146, MB-02:A-043, MB-02:A-045
- **copy-number-correction.11** On 10 V4 mock communities, uncorrected data fit known composition 7.1% (SE 3.6%) better than copy-number-corrected data; one of the eleven mocks was excluded, and all were DNA-based (nine genomic DNA mixes) or cloned-gene mocks.
  conf: repl (marker) · class: meas (marker) · holds: n = 10 DNA-based or cloned-gene mocks; the reviewer's note: DNA-based mocks already fix genome copies and size, so they test correction against a DNA truth, not a cell truth · src: starke16SRRNAGene2020 (FT; meas; repl) · trail: MB-01 §2.5, §7. Bounds, §answers, MB-02 §D1.4, §answers, §critic · from: MB-01:I-0038, MB-01:A-068, MB-01:B-0358, MB-02:B-0147, MB-02:B-0148, MB-02:A-044, MB-02:A-141, MB-02:C-022, MB-02:C-065
- **copy-number-correction.12** Copy number explained about 60% of the estimated PCR bias (R2 about 0.60, p about 0.021) but only about 10% of total bias across 7 taxa.
  conf: single (note: "SINGLE SOURCE") · class: deriv (note: "Partial (derived)") · holds: the 7-taxon vaginal mock; only 7 points; verified in full text by the synthesis agent · src: mclarenConsistentCorrectableBias2019 (FT, re-opened) · trail: MB-01 §2.5, §answers · from: MB-01:B-0126, MB-01:B-0127, MB-01:A-066, MB-01:A-067, MB-01:B-0067
- **copy-number-correction.13** A preprint by the tool's author reports essentially no correlation ("no meaningful correlation") between 16S read and species frequencies in mocks; correction for copy number and primer mismatch reached r of about 0.6 only in ideal cases (exact references), falling to about 0.4 at 97% and about 0.2 at 95% identity.
  conf: single (marker) · class: meas (marker) · holds: mocks; preprint abstract only; MB-01 sets it aside as a single-source contrary result, which its critic says applies a single-source label to one side only, since the pro-correction results it conflicts with (McLaren, Silverman) each also rest on a single mock design · src: edgarUNBIASAttemptCorrect2017 (AB; PREPRINT; meas; single) · trail: MB-01 §2.14, §7. Bounds, §answers, §Adversarial, MB-02 §D1.4, §answers · from: MB-01:B-0193, MB-01:I-0076, MB-01:A-106, MB-01:B-0194, MB-01:B-0360, MB-01:C-131, MB-02:B-0142, MB-02:B-0143, MB-02:A-044, MB-02:C-133
- **copy-number-correction.14** Copy numbers can be estimated from draft assemblies by read depth, with a median deviation of 14% against qPCR.
  conf: not stated · class: not stated · holds: draft genome assemblies; abstract only · src: perisin16StimatorStatisticalEstimation2016 (AB) · trail: MB-02 §D1.4 · from: MB-02:B-0144
- **copy-number-correction.15** Applying copy-number (and genome-size) correction to a forest soil changed Acidobacteria from 50.1% of 16S sequences to an estimated 66.0% of genomes, Actinobacteria from 11.8% to 7.6% and Firmicutes from 3.2% to 1.1%; this is the only soil example of correction size, and it depends on the imprecise low Acidobacteria copy-number mean.
  conf: single (note: "SINGLE SOURCE for soil") · class: deriv (marker) · holds: one forest soil · src: vetrovskyVariability16SRRNA2013 (FT; deriv; repl) · trail: MB-01 §2.5, MB-02 §D1.4, §answers, §critic · from: MB-01:I-0035, MB-02:B-0152, MB-02:B-0153, MB-02:A-045, MB-02:A-059, MB-02:C-005
- **copy-number-correction.16** Whether copy-number correction helps is in conflict: studies recommending routine correction (Kembel 2012; Angly 2014; Gao and Wu 2023) against studies recommending against default correction or finding it unhelpful in mocks (Louca 2018; Edgar 2017; Starke 2021; McLaren 2019 in MB-01's list); part of the conflict reflects differences in what "truth" is (cell-based versus DNA-based mocks, simulated versus real communities, closeness to references), and correction changing dominant taxa but not beta-diversity test results lets both camps' observations hold together.
  conf: cont (note: "Direct conflict") · class: not stated · holds: simulations, mocks of few species and non-soil communities; no soil benchmark · src: kembelIncorporating16SGene2012, anglyCopyRighterRapidTool2014, gaoAccounting16SRRNA2023, loucaCorrecting16SRRNA2018, edgarUNBIASAttemptCorrect2017, starke16SRRNAGene2020, mclarenConsistentCorrectableBias2019 · trail: MB-02 §answers, MB-01 §answers, §6. Where, §2.5 · from: MB-02:A-049, MB-02:A-050, MB-02:A-051, MB-02:A-052, MB-02:A-047, MB-02:A-143, MB-01:A-119, MB-01:B-0335, MB-01:B-0125, MB-02:C-134, MB-02:B-0075, MB-02:B-0141, MB-02:B-0142 · rating: "Moderate"
- **copy-number-correction.17** Sequencing bias behaves as a consistent multiplicative factor per taxon, which can be corrected with calibration controls (McLaren 2019 abstract); the abstract does not compare the size of extraction and primer biases with copy-number bias.
  conf: not stated · class: not stated · holds: abstract only in MB-02 · limit: access (critic: MB-02:C-077) · src: mclarenConsistentCorrectableBias2019 (AB) · trail: MB-02 §D1.4, §critic, §Adversarial · from: MB-02:B-0131, MB-02:C-025, MB-02:C-077, MB-02:C-090
- **copy-number-correction.18** No soil mock community or soil cell-count benchmark of copy-number correction was found; the soil literature on community-weighted rrn copy number was not searched.
  conf: not stated · class: search (note: "No soil mock community or soil cell-count benchmark of copy-number correction was found") · holds: MB-02's searches · src: none (a statement about what the search found) · trail: MB-02 §answers, §critic · from: MB-02:A-053, MB-02:C-026, MB-02:C-027
- **copy-number-correction.19** No study was found that combines copy-number correction with per-cell genome copy measurements (ploidy) in a real community; the polyploidy literature asserts that ploidy also biases community analyses (Soppa 2017, not obtained).
  conf: not stated · class: search (note: "No study found that combines copy-number correction with per-cell genome copy measurements") · holds: MB-02's searches · src: soppaPolyploidyCommunityStructure2017 (not obtained) · trail: MB-02 §answers · from: MB-02:A-054
- **copy-number-correction.20** A review asserts that rDNA copy number can change within species in response to environment; the prokaryote evidence for this was not quantified in what the reviewer read.
  conf: not stated · class: assert (note: "asserted") · holds: one review; abstract only · src: lavrinienkoDoesIntraspecificVariation2021 (AB) · trail: MB-02 §D1.4, §answers · from: MB-02:B-0154, MB-02:B-0155, MB-02:A-055

### community-copy-number: average 16S copy number of communities by environment
needs: copy-number, copy-number-correction
- **community-copy-number.1** Every environment-level copy-number value found is predicted from reference genomes, not measured: soil had the lowest abundance-weighted copy-number distribution in the Earth Microbiome Project; the EMP groups free-living (soil, water, sediment) and plant-associated samples together at about 2.2, with no separate value for water; animal-associated samples are predicted at about 3.4, with gut and saliva highest.
  conf: single (marker) · class: deriv (marker) · holds: EMP predictions from reference genomes, one source (Thompson 2017); the about 2.2 value pools free-living and plant-associated samples and is not a water value · src: thompsonCommunalCatalogueReveals2017 (FT; deriv; single) · trail: MB-01 §3.2, §answers, §critic, §Adversarial · from: MB-01:B-0206, MB-01:I-0082, MB-01:B-0207, MB-01:B-0208, MB-01:B-0209, MB-01:B-0210, MB-01:A-146, MB-01:A-147, MB-01:A-149, MB-01:A-150, MB-01:A-151, MB-01:A-152, MB-01:A-183, MB-01:A-303, MB-01:C-024, MB-01:C-136, MB-01:A-169 · rating: "Weak for environment-level copy number"
- **community-copy-number.2** Predicted community copy number declines through succession in soil and sediment.
  conf: single (marker) · class: deriv (marker) · holds: predicted, not measured · src: nemergutDecreasesAverageBacterial2015 (FT; deriv; single) · trail: MB-01 §3.2, §answers · from: MB-01:I-0083, MB-01:A-148
- **community-copy-number.3** The environment-level copy-number predictions conflict with Louca 2018's finding that such predictions are inaccurate beyond about 15% divergence from a sequenced genome.
  conf: not stated · class: not stated · holds: environment-level predictions against Louca 2018 · src: thompsonCommunalCatalogueReveals2017, loucaCorrecting16SRRNA2018 · trail: MB-01 §answers · from: MB-01:A-169, MB-01:A-177, MB-01:A-153
- **community-copy-number.4** Measured (not predicted) community-average copy number in soil, water or host samples, and a separate value for water, were not found; community-average copy number from shotgun metagenomes was not searched, so this rests on prediction-only sources.
  conf: not stated · class: search (critic: MB-01:C-112) · holds: lab and bioinformatics angles · src: none (a statement about what the search found) · trail: MB-01 §answers, §Search record, §Adversarial · from: MB-01:A-178, MB-01:B-0381, MB-01:C-112, MB-01:C-029

### library-prep: library preparation and sample indexing
needs: pcr
- **library-prep.1** Library preparation and indexing choices include one-step fusion, two-step tailed or ligation designs, and single, combinatorial or unique dual indexes.
  conf: not stated · class: not stated · holds: protocols and documentation · src: none (the reviewer's list of choices) · trail: MB-01 §answers · from: MB-01:A-009
- **library-prep.2** Across 73 MiSeq datasets, library preparation method and primer choice were the most significant sources of bias, with distinct, motif-linked error patterns; this rests on Schirmer 2015 alone.
  conf: single (marker) · class: meas (marker) · holds: 73 MiSeq datasets; one study · src: schirmerInsightBiasesSequencing2015 (FT; meas; single) · trail: MB-01 §2.6, §answers, §Adversarial · from: MB-01:I-0041, MB-01:A-076, MB-01:A-077, MB-01:B-0071, MB-01:C-088
- **library-prep.3** Library design also affected error and chimera rates across four platforms.
  conf: not stated · class: not stated · holds: D'Amore 2016 benchmark · src: damoreComprehensiveBenchmarkingStudy2016 · trail: MB-01 §2.6 · from: MB-01:B-0128
- **library-prep.4** A mock-community comparison of one-step versus two-step library preparation (Gohl 2016) was not obtained in full.
  conf: not stated · class: search (note: "was not obtained in full") · holds: not obtained in full · src: gohlSystematicImprovementAmplicon2016 (not obtained) · trail: MB-01 §2.6, §Sources not obtained · from: MB-01:B-0131

### sequencing-platform: sequencing platform and read length
needs: library-prep
- **sequencing-platform.1** Platform and read-length choices include MiSeq 2x250 or 2x300, HiSeq, NovaSeq, Ion Torrent, 454, and PacBio CCS full length.
  conf: not stated · class: not stated · holds: protocols and benchmarks · src: none (the reviewer's list of choices) · trail: MB-01 §answers · from: MB-01:A-010
- **sequencing-platform.2** Dual-index MiSeq error depended on read overlap: raw V4 error rose with cluster density from 0.25% to 1.08%, a delta-Q of 6 cut it to 0.05 to 0.06% and preclustering to 0.01%, and partially overlapping regions stayed worse.
  conf: repl (marker) · class: meas (marker) · holds: MiSeq, V4 and partially overlapping regions; the critic could not confirm open full text for Kozich 2013 · src: kozichDevelopmentDualindexSequencing2013 (FT; meas; repl) · trail: MB-01 §2.7, §answers · from: MB-01:I-0042, MB-01:B-0132, MB-01:B-0133, MB-01:B-0134, MB-01:A-078, MB-01:B-0071, MB-01:C-065
- **sequencing-platform.3** After preclustering, V3-V4 error was 0.10 to 0.21% and V4-V5 0.36 to 0.64% per the bioinformatics angle; the lab angle reports 0.24 to 0.37% and 0.58 to 0.87%, read through a fetch-tool summary, probably at an earlier stage of curation.
  conf: not stated · class: not stated · holds: Kozich 2013; two angles' readings differ · src: kozichDevelopmentDualindexSequencing2013 · trail: MB-01 §2.7 · from: MB-01:B-0135, MB-01:B-0136
- **sequencing-platform.4** PacBio CCS with DADA2 recovered all expected full-length variants in two mocks with no residual errors; this is the developers' own claim, with no independent long-read mock benchmark.
  conf: not stated · class: not stated · holds: two mocks; developer claim · src: callahanHighthroughputAmpliconSequencing2019 (developer claim) · trail: MB-01 §2.7, §Adversarial · from: MB-01:B-0137, MB-01:C-109
- **sequencing-platform.5** The DADA2 maintainer states that NovaSeq's binned quality scores break loess smoothing in error learning; at the time of the issue the method had not been tested on NovaSeq data.
  conf: not stated · class: not stated · holds: a GitHub issue, documentation · src: benjjnebConsequencesUsingDada2 (DOCUMENTATION; assert) · trail: MB-01 §2.7 · from: MB-01:B-0138, MB-01:B-0139

### index-misassignment: demultiplexing and index misassignment
needs: library-prep
- **index-misassignment.1** Demultiplexing is done with or without filtering on index-read quality.
  conf: not stated · class: not stated · holds: Wright 2016 · src: wrightQualityFilteringIllumina2016 · trail: MB-01 §answers · from: MB-01:A-011
- **index-misassignment.2** On Illumina GAIIx with non-16S libraries, 0.51 to 0.76% of index pairs were wrong, falling to 0.06 to 0.43% after index-quality filtering.
  conf: repl (marker) · class: meas (marker) · holds: GAIIx, non-16S libraries, labelled INDIRECT · src: kircherDoubleIndexingOvercomes2012 (FT; meas; repl; INDIRECT) · trail: MB-01 §2.8 · from: MB-01:I-0043
- **index-misassignment.3** On patterned flow cells (HiSeq X, 3000/4000, NovaSeq) with non-16S genome and exome libraries, 0.2 to 6% of reads were misassigned in every run, about 10-fold less on MiSeq, and unique dual indexes cut 0.89% to 0.13%.
  conf: repl (marker) · class: meas (marker) · holds: non-16S libraries, labelled INDIRECT · src: costelloCharacterizationRemediationSample2018 (FT; meas; repl; INDIRECT) · trail: MB-01 §2.8, §answers · from: MB-01:I-0044, MB-01:A-081, MB-01:A-082, MB-01:C-133
- **index-misassignment.4** Illumina's documentation gives 0.1 to 2% index hopping on patterned flow cells.
  conf: not stated · class: not stated · holds: a maker's claim · src: illuminaIndexHopping (DOCUMENTATION; maker's claim) · trail: MB-01 §2.8 · from: MB-01:B-0141
- **index-misassignment.5** On HiSeq 2500 with non-16S amplicons, cross-talk was 0.24%, falling to 0.03% after index-quality filtering, which kept 88% of reads.
  conf: single (marker) · class: meas (marker) · holds: non-16S amplicons, labelled INDIRECT · src: wrightQualityFilteringIllumina2016 (FT; meas; single; INDIRECT) · trail: MB-01 §2.8, §answers · from: MB-01:I-0045, MB-01:A-083
- **index-misassignment.6** In 16S data from GAIIx and 11 MiSeq runs, about 2% of reads were misassigned.
  conf: single (marker) · class: meas (marker) · holds: one preprint abstract · src: edgarUNCROSSFilteringHighfrequency2016 (AB; PREPRINT; meas; single) · trail: MB-01 §2.8, §answers · from: MB-01:I-0046, MB-01:A-084
- **index-misassignment.7** Barcode leakage between 16S plate wells was negligible.
  conf: single (marker) · class: meas (marker) · holds: 16S plates · src: minichQuantifyingUnderstandingWelltowell2019 (FT; meas; single) · trail: MB-01 §2.8, §answers · from: MB-01:I-0047, MB-01:A-085
- **index-misassignment.8** In eukaryotic 18S data, up to 28.2% of unique sequences were undetectable mistags.
  conf: not stated · class: meas (marker) · holds: 18S, labelled INDIRECT · src: eslingAccurateMultiplexingFiltering2015 (FT; meas; INDIRECT) · trail: MB-01 §2.8 · from: MB-01:I-0048
- **index-misassignment.9** With mammal and arthropod markers, 2.1 to 2.6% of sequences came from tag jumps.
  conf: not stated · class: meas (marker) · holds: other markers, labelled INDIRECT; abstract only · src: schnellTagJumpsIlluminated2015 (AB; meas; INDIRECT) · trail: MB-01 §2.8, §answers · from: MB-01:I-0049, MB-01:A-086
- **index-misassignment.10** Index misassignment rates are fractions of reads assigned to the wrong sample; they mainly create false presences of taxa, concentrated where abundant taxa from other samples leak in, and they vary with platform, library type and run. The 16S-specific evidence is thin: one preprint abstract and one plate study.
  conf: not stated · class: not stated · holds: the eight settings above; the Table 1 summary (0.1 to 6% of reads) merges non-16S genome and exome libraries, Illumina documentation, non-16S amplicons and 16S data · src: costelloCharacterizationRemediationSample2018, wrightQualityFilteringIllumina2016, edgarUNCROSSFilteringHighfrequency2016, minichQuantifyingUnderstandingWelltowell2019 · trail: MB-01 §2.8, §2. Steps, §answers, §Adversarial · from: MB-01:B-0140, MB-01:B-0142, MB-01:B-0143, MB-01:B-0144, MB-01:B-0145, MB-01:A-087, MB-01:B-0072, MB-01:C-133
- **index-misassignment.11** No 16S-specific measurement of index hopping on patterned flow cells (NovaSeq, NextSeq 2000) was found; the 16S rate is one preprint abstract.
  conf: not stated · class: search (note: "No 16S-specific measurement of index hopping on patterned flow cells (NovaSeq) was found") · holds: bioinformatics angle · src: none (a statement about what the search found) · trail: MB-01 §answers, §Search record, §Adversarial · from: MB-01:A-122, MB-01:B-0382, MB-01:C-110

### quality-filtering: quality filtering, read merging and error correction
needs: sequencing-platform
- **quality-filtering.1** Quality filtering and merging choices include quality, length, expected-error and abundance thresholds, plus the delta-Q rule when merging.
  conf: not stated · class: not stated · holds: Bokulich 2013 and Kozich 2013 · src: bokulichQualityfilteringVastlyImproves2013, kozichDevelopmentDualindexSequencing2013 · trail: MB-01 §answers · from: MB-01:A-012
- **quality-filtering.2** On mocks from GAIIx, HiSeq and MiSeq runs, minimum read length, quality threshold and a minimum OTU abundance filter strongly affected alpha diversity and composition, while ambiguous bases and bad run length did not; almost every setting needed an abundance filter of 0.0001 to 0.01% to reach expected taxon counts (0.005% recommended), and weighted UniFrac conclusions were robust while unweighted metrics were sensitive.
  conf: repl (marker) · class: meas (marker) · holds: mocks from three platforms · src: bokulichQualityfilteringVastlyImproves2013 (FT; meas; repl) · trail: MB-01 §2.9 · from: MB-01:B-0146, MB-01:I-0050, MB-01:B-0147, MB-01:B-0148
- **quality-filtering.3** Stringent UPARSE-style filtering could significantly underestimate abundance and diversity, and newer clusterers produced up to 60% fewer spurious OTUs than UCLUST.
  conf: cont (marker) · class: meas (marker) · holds: Kopylova 2016 benchmark · src: kopylovaOpensourceSequenceClustering2016 (FT; meas; cont) · trail: MB-01 §2.9, §7. Bounds · from: MB-01:I-0051, MB-01:B-0363
- **quality-filtering.4** Quality-filter stringency is disputed: Bokulich 2013 against Kopylova 2016.
  conf: not stated · class: not stated · holds: listed among the disputed choices and the review's conflicts · src: bokulichQualityfilteringVastlyImproves2013, kopylovaOpensourceSequenceClustering2016 · trail: MB-01 §answers, §6. Where · from: MB-01:A-022, MB-01:B-0020, MB-01:B-0337
- **quality-filtering.5** Error correction plus read overlapping cut substitution errors by 93% on average.
  conf: not stated · class: not stated · holds: Schirmer 2015 · src: schirmerInsightBiasesSequencing2015 · trail: MB-01 §2.9 · from: MB-01:B-0149
- **quality-filtering.6** The USEARCH author reports that most paired-read assemblers compute incorrect posterior quality scores.
  conf: not stated · class: not stated · holds: developer claim; abstract only · src: edgarErrorFilteringPair2015 (AB; developer claim) · trail: MB-01 §2.9 · from: MB-01:B-0150

### denoising-clustering: error correction, denoising and clustering into OTUs or ASVs
needs: quality-filtering
- **denoising-clustering.bg1** An operational taxonomic unit (OTU) is a cluster of sequencing reads that differ by less than a fixed dissimilarity threshold; an amplicon sequence variant (ASV) is a sequence variant resolved exactly, down to single-nucleotide differences, by methods that control sequencing errors.
  kind: background · ref: callahanExactSequenceVariants2017 · check: DOI 10.1038/ismej.2017.119 resolves on Crossref (The ISME Journal 11(12): 2639-2643); both definitions are in the abstract (Europe PMC record), checked 2026-10-21
- **denoising-clustering.1** Error-handling choices are 97% or 99% OTUs (de novo, closed or open reference) or ASVs from DADA2, Deblur or UNOISE3; DADA2 can process samples independently, pooled or pseudo-pooled.
  conf: not stated · class: not stated · holds: documentation and benchmarks · src: callahanDADA2DocumentationPseudopooling · trail: MB-01 §answers · from: MB-01:A-013
- **denoising-clustering.2** In an independent benchmark, relative abundances of expected taxa within each mock were similar across DADA2, UNOISE3, Deblur and open-reference OTUs, while counts of units differed widely: open-reference clustering gave 453 OTUs on the HMP mock and 8,891 on the Extreme mock, and on one soil DADA2 gave 16,609 ASVs, UNOISE3 11,613, Deblur 8,270 and open-reference 21,297 OTUs; no pipeline recovered every expected sequence, and on the Zymo mock all pipelines "markedly differed" from expected composition.
  conf: repl (marker) · class: meas (marker) · holds: mocks (HMP, Extreme, Zymo) and one soil · src: nearingDenoisingDenoisersIndependent2018 (FT; meas; repl) · trail: MB-01 §2.10, §answers, §Adversarial · from: MB-01:I-0052, MB-01:B-0151, MB-01:B-0152, MB-01:B-0153, MB-01:B-0154, MB-01:B-0155, MB-01:A-091, MB-01:A-092, MB-01:B-0074, MB-01:C-087
- **denoising-clustering.3** Bacteroides varied from 20.6% to 24.6% across pipelines, and operating system mattered little for pipeline output.
  conf: not stated · class: not stated · holds: Marizzoni 2020 · src: marizzoniComparisonBioinformaticsPipelines2020 · trail: MB-01 §answers, §2. Steps, §7. Bounds · from: MB-01:A-093, MB-01:B-0075, MB-01:B-0356
- **denoising-clustering.4** mothur and QIIME1 returned 10 to 200 times the expected number of sequences, and Faith's PD was overestimated 1.3 to 2.7-fold by QIIME2, 2 to 18-fold by QIIME1 and 3.5 to 29-fold by mothur; the authors report pipeline-dependent interpretations.
  conf: repl (marker) · class: meas (marker) · holds: Straub 2020; the authors also built nf-core/ampliseq · src: straubInterpretationsEnvironmentalMicrobial2020 (FT; meas; repl; authors also built nf-core/ampliseq) · trail: MB-01 §2.10, §answers, §Adversarial · from: MB-01:I-0053, MB-01:A-094, MB-01:C-087
- **denoising-clustering.5** DADA2 had the best sensitivity and UNOISE3 the best balance, while QIIME-uclust produced on average 134 one-off and 412 other spurious OTUs.
  conf: repl (marker) · class: meas (marker) · holds: Prodan 2020 · src: prodanComparingBioinformaticPipelines2020 (FT; meas; repl) · trail: MB-01 §2.10 · from: MB-01:I-0054, MB-01:B-0156, MB-01:B-0157
- **denoising-clustering.6** The DADA2 developers report 93 output sequences on a 57-strain mock, against 249 for mothur and 378 for QIIME.
  conf: not stated · class: meas (marker) · holds: one 57-strain mock; developer claim · src: callahanDADA2HighresolutionSample2016 (FT; meas; developer claim) · trail: MB-01 §2.10 · from: MB-01:I-0055
- **denoising-clustering.7** After OTU clustering and singleton removal, tables contained approximately 50% (mock communities) to 80% (gnotobiotic mice) spurious taxa; the authors propose a 0.25% relative-abundance cutoff, and the most abundant spurious taxon in mocks had a median relative abundance of 0.12%.
  conf: single (marker) · class: meas (marker) · holds: mocks and gnotobiotic mice · src: reitmeierHandlingSpuriousSequences2021 (FT; meas; single) · trail: MB-01 §2.10, §2.13, §critic, §Adversarial · from: MB-01:I-0056, MB-01:A-095, MB-01:B-0181, MB-01:C-058, MB-01:C-072
- **denoising-clustering.8** QIIME closed- and open-reference OTUs inflated richness to 1,607 to 5,824 OTUs where about 20 were expected, and on V4 mocks 56 to 88% of predicted genus names were false positives.
  conf: single (marker) · class: meas (marker) · holds: V4 mocks; single source · src: edgarAccuracyMicrobialCommunity2017 (FT; meas; single) · trail: MB-01 §2.10, §2. Steps · from: MB-01:B-0158, MB-01:I-0057, MB-01:B-0159, MB-01:B-0076
- **denoising-clustering.9** In leaf litter, bacterial OTU richness was about half of ESV richness (slope 0.46), but alpha and beta metrics correlated at r > 0.90 and inferences matched, so OTU versus ESV mattered little for broad patterns.
  conf: cont (marker) · class: meas (marker) · holds: leaf litter · src: glassmanBroadscaleEcologicalPatterns2018 (FT; meas; cont) · trail: MB-01 §2.10, §7. Bounds · from: MB-01:B-0160, MB-01:I-0058, MB-01:B-0353
- **denoising-clustering.10** In 227 freshwater sediment, seston and mussel-gut samples the direction was reversed: ASV richness was about half of OTU richness, and Mollicutes dominated mussel gut by ASVs but were absent from OTU tables; the authors attribute the reversal partly to higher richness in sediment.
  conf: cont (marker) · class: meas (marker) · holds: freshwater sediment, seston and mussel gut · src: chiarelloRankingBiasesChoice2022 (FT; meas; cont) · trail: MB-01 §2.10 · from: MB-01:B-0161, MB-01:I-0059, MB-01:B-0162
- **denoising-clustering.11** The direction of the OTU versus ASV richness difference conflicts between studies (Glassman and Martiny 2018 against Chiarello 2022), and OTUs versus ASVs is a disputed choice (Schloss 2021 against the ASV developers).
  conf: cont (note: "conflicts between studies") · class: not stated · holds: leaf litter against freshwater samples · src: glassmanBroadscaleEcologicalPatterns2018, chiarelloRankingBiasesChoice2022, schlossAmpliconSequenceVariants2021 · trail: MB-01 §answers, §6. Where · from: MB-01:A-096, MB-01:A-120, MB-01:B-0336, MB-01:A-023
- **denoising-clustering.12** In soil and plant samples, OTUs versus ASVs changed which families were called differentially abundant, mostly families under 0.1% abundance.
  conf: single (marker) · class: meas (marker) · holds: soil and plant samples · src: joosDaringDifferentialMetabarcoding2020 (FT; meas; single) · trail: MB-01 §2.10 · from: MB-01:I-0060
- **denoising-clustering.13** The identity threshold that best matched species was about 99% for full-length 16S and about 100% for V4.
  conf: single (marker) · class: deriv (marker) · holds: abstract only · src: edgarUpdating97Identity2018 (AB; deriv; single) · trail: MB-01 §2.10 · from: MB-01:I-0061
- **denoising-clustering.14** According to the DADA2 documentation, independent per-sample processing needs at least two error-free reads to detect an ASV, and pooling finds more ASVs per sample.
  conf: not stated · class: not stated · holds: documentation · src: callahanDADA2DocumentationPseudopooling (DOCUMENTATION) · trail: MB-01 §2.10 · from: MB-01:B-0164, MB-01:B-0165

### intragenomic-variation: variation among 16S copies within a genome
needs: copy-number, denoising-clustering
- **intragenomic-variation.1** Intragenomic variants split genomes into several ASVs: 0.58 variants per copy for full-length 16S and 0.25 for V4.
  conf: cont (marker) · class: deriv (marker) · holds: genome-based analysis · src: schlossAmpliconSequenceVariants2021 (FT; deriv; cont) · trail: MB-01 §2.5, §answers · from: MB-01:I-0039, MB-01:A-071, MB-01:B-0068
- **intragenomic-variation.2** Full-length PacBio sequencing recovered intragenomic variants in their expected integral ratios.
  conf: single (marker) · class: meas (marker) · holds: developer study · src: callahanHighthroughputAmpliconSequencing2019 (FT; meas; single; developer) · trail: MB-01 §2.5 · from: MB-01:I-0040
- **intragenomic-variation.3** Copies within a genome are not always identical: heterogeneity was found in 952 of 2,013 genomes, 87.5% of it below 1% divergence; inflation of unique-sequence richness reached 123.7% for full-length genes but was smaller at 97% clustering.
  conf: not stated · class: not stated · holds: genome survey; abstract only · src: sunIntragenomicHeterogeneity16S2013 (AB) · trail: MB-02 §D1.2 · from: MB-02:B-0080, MB-02:B-0081, MB-02:B-0082
- **intragenomic-variation.4** Acinas et al. estimated an upper bound of about threefold diversity overestimation from operon redundancy.
  conf: not stated · class: not stated · holds: abstract only · src: acinasDivergenceRedundancy16S2004 (AB) · trail: MB-02 §D1.2 · from: MB-02:B-0083

### chimeras: chimera formation and detection
needs: pcr, denoising-clustering
- **chimeras.1** Chimera detection choices are UCHIME, UCHIME2 or ChimeraSlayer.
  conf: not stated · class: not stated · holds: software documentation · src: edgarUCHIMEImprovesSensitivity2011, edgarUCHIME2ImprovedChimera2016 · trail: MB-01 §answers · from: MB-01:A-014
- **chimeras.2** Chimeras formed reproducibly across independent amplifications of a known mixture; less-abundant species showed chimera rates above 70%, and chimera count correlated with organism abundance (R2 = 0.97) in a staggered mock; the reproducibility rests on this one study.
  conf: single (critic: MB-01:C-090) · class: meas (marker) · holds: Sanger and 454 · src: haasChimeric16SRRNA2011 (FT; meas; repl; Sanger and 454) · trail: MB-01 §2.11, §answers, §Adversarial · from: MB-01:I-0063, MB-01:B-0166, MB-01:B-0167, MB-01:A-074, MB-01:A-075, MB-01:B-0069, MB-01:B-0070, MB-01:C-090
- **chimeras.3** Chimeras inflate richness and create false novel taxa; at 30 cycles they made up 0.9% (Accuprime) to 18.2% (Platinum) of reads depending on polymerase, and UCHIME sensitivity was 50 to 87% at 25 or more cycles.
  conf: not stated · class: not stated · holds: Sze and Schloss 2019; verified by the synthesis agent and the critic · src: szeImpactDNAPolymerase2019 · trail: MB-01 §2.11, §answers, §critic · from: MB-01:B-0170, MB-01:A-072, MB-01:A-073, MB-01:C-054
- **chimeras.4** ChimeraSlayer detected over 87% of simulated chimeras when parents diverged by 4% or more, with a 1.6% false-positive rate, and sensitivity fell for every method as parents became more similar.
  conf: not stated · class: not stated · holds: simulated chimeras (Haas 2011) · src: haasChimeric16SRRNA2011 · trail: MB-01 §2.11 · from: MB-01:B-0168, MB-01:B-0169
- **chimeras.5** UCHIME2's author states error-free chimera prediction is "impossible in principle".
  conf: not stated · class: not stated · holds: developer claim; preprint abstract · src: edgarUCHIME2ImprovedChimera2016 (AB; PREPRINT; developer claim) · trail: MB-01 §2.11 · from: MB-01:B-0171

### taxonomic-assignment: taxonomic assignment, classifiers and reference databases
needs: denoising-clustering
- **taxonomic-assignment.1** Taxonomy choices are RDP NBC, q2-feature-classifier, SINTAX, IDTAXA or MAPseq, against SILVA, Greengenes, RDP or GTDB-type references, optionally with habitat-weighted priors.
  conf: not stated · class: not stated · holds: software documentation · src: kaehlerSpeciesAbundanceInformation2019 · trail: MB-01 §answers · from: MB-01:A-015
- **taxonomic-assignment.2** Cross-validated by identity to the reference, all tested classifiers were at most 50% accurate on V4: genus accuracy was about 100% at 100% identity and about 50% at 97%; the author argues that mocks overstate accuracy because all their members are named type strains. This rests on one author, who also develops competing classifiers.
  conf: single (marker) · class: meas (marker) · holds: reference sets; accuracy depends on distance to reference · src: edgarAccuracyTaxonomyPrediction2018 (FT; meas; single) · trail: MB-01 §2.12, §answers, §2. Steps, §Adversarial · from: MB-01:B-0172, MB-01:I-0064, MB-01:B-0173, MB-01:A-097, MB-01:B-0076, MB-01:C-089
- **taxonomic-assignment.3** On mocks, the q2-feature-classifier methods reached median genus F above 0.8.
  conf: not stated · class: meas (marker) · holds: mocks; developer claim · src: bokulichOptimizingTaxonomicClassification2018 (FT; meas; developer claim) · trail: MB-01 §2.12, §answers · from: MB-01:I-0065, MB-01:A-099
- **taxonomic-assignment.4** Habitat-weighted priors cut species-level error from 25% to 14%.
  conf: not stated · class: meas (marker) · holds: developer claim · src: kaehlerSpeciesAbundanceInformation2019 (FT; meas; developer claim) · trail: MB-01 §2.12 · from: MB-01:I-0066
- **taxonomic-assignment.5** IDTAXA over-classified less when the true taxa were absent from the training set.
  conf: not stated · class: meas (marker) · holds: developer claim; reference listed under Murali, cited by the bioinformatics angle · src: muraliIDTAXANovelApproach2018 (FT; meas; developer claim) · trail: MB-01 §2.12 · from: MB-01:I-0067, MB-01:B-0174
- **taxonomic-assignment.6** Estimated annotation error is about 10% for RDP and about 17% for SILVA v128 and Greengenes 13.5, judged from conflicting labels on identical sequences.
  conf: single (marker) · class: deriv (marker) · holds: three reference databases; one author · src: edgarTaxonomyAnnotationGuide2018 (FT; deriv; single) · trail: MB-01 §2.12, §answers, §Adversarial · from: MB-01:I-0068, MB-01:A-098, MB-01:C-089
- **taxonomic-assignment.7** On simulated gut, ocean and soil communities, genus recall was 67 to 80% and assignments varied by up to 40% between 16S subregions within a pipeline.
  conf: single (marker) · class: model (marker) · holds: simulated communities · src: almeidaBenchmarkingTaxonomicAssignments2018 (FT; model; single) · trail: MB-01 §2.12 · from: MB-01:I-0069

### contamination: contaminants and negative controls
needs: extraction
- **contamination.1** Contaminant-handling choices are dropping taxa seen in negative controls, decontam (frequency or prevalence mode), SourceTracker, or relative-abundance cutoffs.
  conf: not stated · class: not stated · holds: the contaminant studies below · src: davisSimpleStatisticalIdentification2018, karstensControllingContaminantsLowbiomass2019 · trail: MB-01 §answers · from: MB-01:A-016
- **contamination.2** In a Salmonella bongori dilution series run at three institutes, contaminants dominated by about 10^3 input cells, more so at 40 than at 20 cycles, and profiles differed by kit and laboratory.
  conf: repl (marker) · class: meas (marker) · holds: one organism dilution series, three institutes · src: salterReagentLaboratoryContamination2014 (FT; meas; repl) · trail: MB-01 §2.13, §answers · from: MB-01:B-0175, MB-01:I-0070, MB-01:A-100
- **contamination.3** In an 8-member mock diluted 3-fold eight times, contaminant reads rose from 0.1% to 80.1% and ASVs from 18 to 381; removing every sequence present in the negative control wrongly removed more than 20% of expected sequences, since three of the eight mock ASVs appeared in the control; decontam's frequency method removed 70 to 90% of contaminants and no expected sequences; SourceTracker removed over 98% when sources were well defined but failed on over 97% when they were not.
  conf: single (marker) · class: meas (marker) · holds: one diluted mock · src: karstensControllingContaminantsLowbiomass2019 (FT; meas; single) · trail: MB-01 §2.13, §7. Bounds, §answers · from: MB-01:I-0071, MB-01:B-0176, MB-01:B-0177, MB-01:B-0178, MB-01:B-0179, MB-01:A-101, MB-01:B-0077, MB-01:B-0361, MB-01:B-0362
- **contamination.4** Well-to-well contamination arose mainly at extraction, less at library preparation, mostly into neighbouring wells (rarely up to 10 wells away), and was greatest in low-biomass samples.
  conf: single (marker) · class: meas (marker) · holds: 16S plates · src: minichQuantifyingUnderstandingWelltowell2019 (FT; meas; single) · trail: MB-01 §2.13, §answers · from: MB-01:I-0072, MB-01:A-102
- **contamination.5** Contamination varies inversely with biomass and is specific to the kit and laboratory.
  conf: not stated · class: not stated · holds: Salter 2014, Karstens 2019, Minich 2019 · src: salterReagentLaboratoryContamination2014, karstensControllingContaminantsLowbiomass2019, minichQuantifyingUnderstandingWelltowell2019 · trail: MB-01 §answers, §2. Steps · from: MB-01:A-103, MB-01:B-0078
- **contamination.6** As biomass fell in a dilution series, contaminants made up a growing share of inferred communities under every sequence-inference method; the authors state no inference method alone separates contaminants from true sequences.
  conf: single (marker) · class: meas (marker) · holds: one dilution series · src: carusoPerformanceMicrobiomeSequence2019 (FT; meas; single) · trail: MB-01 §2.10 · from: MB-01:B-0163, MB-01:I-0062
- **contamination.7** decontam's makers describe a frequency mode that assumes contaminant DNA is roughly constant across samples.
  conf: not stated · class: not stated · holds: developer claim · src: davisSimpleStatisticalIdentification2018 (FT; developer claim) · trail: MB-01 §2.13 · from: MB-01:B-0180
- **contamination.8** Hornung 2019 surveyed 265 papers in the 2018 issues of Microbiome and The ISME Journal that used any high-throughput community sequencing (16S, shotgun, metatranscriptomics, ITS, 18S, virome, long-read and others): 30% (79) reported a negative control and 10% (27) a positive control. It is not a 16S-only figure, and it is a single source.
  conf: single (critic: MB-01:C-005) · class: meas (marker) · holds: two journals, 2018, all high-throughput community sequencing types · src: hornungIssuesCurrentStandards2019 (FT; meas; single) · trail: MB-01 §2.13, §answers, §critic, §Adversarial · from: MB-01:I-0073, MB-01:A-017, MB-01:A-033, MB-01:C-003, MB-01:C-004, MB-01:C-005, MB-01:C-132
- **contamination.9** A review proposes the RIDE checklist.
  conf: not stated · class: assert (marker) · holds: review; abstract only · src: eisenhoferContaminationLowMicrobial2019 (AB; assert) · trail: MB-01 §2.13 · from: MB-01:I-0074

### workflow-bias: departure of observed from known composition across the whole workflow
needs: extraction, pcr, denoising-clustering, contamination
- **workflow-bias.1** Every mock-community study in the body found observed composition departing from known composition, and the size of the bias depends on platform, region, primer, extraction and pipeline.
  conf: repl (marker) · class: meas (marker) · holds: mock communities and dilution series; the critic: multiple independent full-text mock and dilution studies show departures (Brooks 2015, Fouhy 2016, Pinto and Raskin 2012, D'Amore 2016, Karstens 2019, Silverman 2021, Sze and Schloss 2019) · src: damoreComprehensiveBenchmarkingStudy2016 (FT; meas; repl), fouhy16SRRNAGene2016 (FT; meas; repl), pintoPCRBiasesDistort2012 (FT; meas; repl), brooksTruthMetagenomicsQuantifying2015 (FT; meas; cont) · trail: MB-01 §1. Overview, §answers, §critic, §Adversarial · from: MB-01:B-0033, MB-01:I-0001, MB-01:A-034, MB-01:A-035, MB-01:C-010, MB-01:C-144, MB-01:C-145, MB-01:C-146
- **workflow-bias.2** Departures were measured at most steps examined, but not at all of them: field sampling for water and host tissue was not searched, and several choices showed little or no detectable effect (PCR replicate pooling, preparation day and lane, cycle number in some studies, storage in one soil).
  conf: not stated · class: not stated · holds: the steps the review searched · src: none (the critic's reading of the review's body) · trail: MB-01 §critic, §Adversarial · from: MB-01:C-011, MB-01:C-012, MB-01:C-013, MB-01:C-147, MB-01:C-148, MB-01:C-149
- **workflow-bias.3** For the number of taxa detected, inflation by spurious sequences (sequencing error, chimeras, cross-sample leakage), reagent contamination and the choice of clustering or denoising is replicated across independent mocks and dilution series, changing counts of taxa by one to two orders of magnitude: for example 10 to 200-fold excess units (Straub 2020) and contaminants rising from 0.1% to 80.1% of reads in a diluted mock (Karstens 2019).
  conf: repl (critic: MB-01:C-014) · class: meas (marker) · holds: mocks and dilution series · src: straubInterpretationsEnvironmentalMicrobial2020 (FT; meas; repl), karstensControllingContaminantsLowbiomass2019 (FT; meas; single) · trail: MB-01 §critic, §1. Overview, §8. Answers · from: MB-01:C-014, MB-01:B-0034, MB-01:B-0037, MB-01:B-0038, MB-01:A-298, MB-01:C-022 · rating: "moderate for the inflation of taxon counts"
- **workflow-bias.4** For relative abundance, the ordering in which extraction is the largest step, followed by PCR and then sequencing, rests on one 7-taxon vaginal dataset (Brooks 2015 reanalysed by McLaren 2019), with Albertsen 2015 (sludge, bead beating only) as partial support; it is contested by Fouhy 2016 (two extraction methods gave very similar data) and qualified by MBQC (specimen type mattered more than extraction), and is a single-dataset result, not a field-wide ordering. Fold errors of 2 to 30 or more between taxon pairs are reported.
  conf: single (critic: MB-01:C-017) · class: deriv/model (marker) · holds: one re-analysed 454 dataset of 7 taxa; the per-step decomposition would weaken substantially without McLaren 2019 and Brooks 2015 · src: mclarenConsistentCorrectableBias2019 (FT, re-opened; deriv/model; single dataset), brooksTruthMetagenomicsQuantifying2015, albertsenBackBasicsInfluence2015, fouhy16SRRNAGene2016, sinhaAssessmentVariationMicrobial2017 · trail: MB-01 §critic, §Adversarial, §1. Overview, §answers, §8. Answers · from: MB-01:C-015, MB-01:C-016, MB-01:C-017, MB-01:C-061, MB-01:C-083, MB-01:C-084, MB-01:A-131, MB-01:B-0035, MB-01:B-0036, MB-01:A-297, MB-01:I-0007, MB-01:C-022 · rating: "weak for per-step relative-abundance magnitudes"
- **workflow-bias.5** Per-step magnitudes mostly come from one or two small mocks (7 to 20 taxa), often on 454 or Ion Torrent.
  conf: not stated · class: not stated · holds: the step-wise evidence in the review · src: none (the critic's and the review's summary of the mock studies) · trail: MB-01 §critic, §answers · from: MB-01:C-018, MB-01:A-113
- **workflow-bias.6** The size of the extraction effect is in conflict: Fouhy 2016 against Albertsen 2015, Brooks 2015 and MBQC.
  conf: not stated · class: not stated · holds: listed among the review's conflicts · src: fouhy16SRRNAGene2016, albertsenBackBasicsInfluence2015, brooksTruthMetagenomicsQuantifying2015, sinhaAssessmentVariationMicrobial2017 · trail: MB-01 §answers, §6. Where · from: MB-01:A-117, MB-01:B-0333
- **workflow-bias.7** Across 15 laboratories, variability depended most on specimen type, then DNA extraction, then handling laboratory, then bioinformatics; interlaboratory differences were substantial, and absolute diversity was not comparable between laboratories even with the same pipeline.
  conf: single (marker) · class: meas (marker) · holds: MBQC, 15 laboratories · src: sinhaAssessmentVariationMicrobial2017 (FT; meas; single) · trail: MB-01 §2.2, §4.3, §answers · from: MB-01:I-0011, MB-01:A-104, MB-01:A-105, MB-01:B-0099, MB-01:B-0250
- **workflow-bias.8** A review states that PCR-based estimates can deviate by "several orders of magnitude" if extraction, PCR, copy number and analysis errors are ignored.
  conf: not stated · class: assert (marker) · holds: review; abstract only · src: bonkPCRbasedQuantificationTaxaspecific2018 (AB; assert) · trail: MB-01 §2.14 · from: MB-01:I-0077
- **workflow-bias.9** Archaeal evidence is thin: one archaeal-rich mock (Pinto and Raskin 2012), a copy-number range from 148 species, and one run-failure case (Yeh 2018); archaeal-specific primer bias measured against known composition is absent.
  conf: not stated · class: search (note: "No archaeal-rich mock was found") · holds: the review's own not-found line counts D'Amore 2016 as a second archaeal-rich mock; the critic counts one · src: pintoPCRBiasesDistort2012, stoddardRrnDBImprovedTools2015, yehTaxonDisappearanceMicrobiome2018 · trail: MB-01 §answers, §Adversarial · from: MB-01:A-123, MB-01:C-119
- **workflow-bias.10** Apart from McLaren 2019 and its source data (Brooks 2015), on which the per-step decomposition and ratio consistency rest, and Silverman 2021, on which the per-cycle PCR bias magnitude rests, removing any other single source would not change the answer.
  conf: not stated · class: not stated · holds: the review's single-source sensitivity for D2 · src: none (the reviewer's sensitivity statement) · trail: MB-01 §answers · from: MB-01:A-133, MB-01:A-131, MB-01:A-132

### bias-consistency: whether the departure is consistent across samples
needs: workflow-bias
- **bias-consistency.1** McLaren et al. modelled each step as multiplying taxon abundances by a taxon-specific efficiency; under this model the error in taxon ratios was "consistent across samples", while the error in proportions "varied dramatically in both magnitude and direction".
  conf: single (marker) · class: model (marker) · holds: 7 taxa mixed as cells and reanalysed; the one dataset modelled for this question · src: mclarenConsistentCorrectableBias2019 (FT; model; single) · trail: MB-01 §1. Overview, §2.14, §answers · from: MB-01:I-0002, MB-01:B-0183, MB-01:B-0184, MB-01:A-107, MB-01:A-108, MB-01:B-0039, MB-01:C-128
- **bias-consistency.2** Six parameters explained almost all systematic error in the cell mixtures, and calibration from control mixtures cut mean Bray-Curtis error from 0.35 to 0.08 (92.6% lower mean squared error) in the Brooks 16S cell mixtures (2 calibration samples, 69 calibrated samples); the Costea shotgun calibration is reported only qualitatively ("removed most of the systematic error").
  conf: not stated · class: not stated · holds: the Brooks 16S cell mixtures, not a shotgun dataset; verified in the full text by the critic · src: mclarenConsistentCorrectableBias2019 (FT, re-opened), costeaTowardsStandardsHuman2017 (SEC) · trail: MB-01 §2.14, §critic, §Adversarial · from: MB-01:B-0185, MB-01:C-021, MB-01:C-055, MB-01:C-066, MB-01:C-067, MB-01:C-068, MB-01:C-069
- **bias-consistency.3** The authors list where the multiplicative model may fail: PCR saturation, taxa aggregated with differing efficiencies, matrix differences between controls and samples, and taxa absent from the controls.
  conf: not stated · class: not stated · holds: McLaren 2019 · src: mclarenConsistentCorrectableBias2019 · trail: MB-01 §2.14 · from: MB-01:B-0186
- **bias-consistency.4** Brooks et al. found significant mixture-blending terms on the same data and concluded that one taxon's observed proportion depends on which others are present; the two readings conflict, and McLaren's attributes the apparent dependence to working on the proportion scale.
  conf: cont (note: "The two readings conflict") · class: not stated · holds: the same 7-taxon cell-mixture data · src: brooksTruthMetagenomicsQuantifying2015, mclarenConsistentCorrectableBias2019 · trail: MB-01 §2.14, §1. Overview, §answers, §6. Where · from: MB-01:B-0187, MB-01:B-0188, MB-01:B-0040, MB-01:A-109, MB-01:A-115, MB-01:B-0330
- **bias-consistency.5** On the ratio scale, extraction bias was consistent across samples within a protocol in the vaginal mock: ratio-scale consistency is shown in one 16S cell-mixture dataset.
  conf: single (critic: MB-01:C-019) · class: not stated · holds: one 16S cell-mixture dataset · src: mclarenConsistentCorrectableBias2019 · trail: MB-01 §2.2, §answers, §8. Answers, §critic · from: MB-01:B-0101, MB-01:A-048, MB-01:B-0056, MB-01:A-299, MB-01:C-019
- **bias-consistency.6** A 10-species shotgun spike-in also gave a consistent profile across faecal backgrounds, with protocol H showing up to 2,751-fold maximum pairwise bias; this is shotgun, not 16S, known only via McLaren 2019, and a different measurement type from the 16S cell-mixture result.
  conf: not stated · class: not stated · holds: shotgun metagenomics, faecal backgrounds; secondary and indirect · src: costeaTowardsStandardsHuman2017 (SEC; INDIRECT, shotgun), mclarenConsistentCorrectableBias2019 · trail: MB-01 §2.2, §answers, §Adversarial · from: MB-01:B-0102, MB-01:A-049, MB-01:A-130, MB-01:C-137
- **bias-consistency.7** Variation of bias between sample types or samples is shown by the field-versus-mock SAR11 bias for 515F-Y/806R (Parada 2016, abstract only), inconsistent cycle effects in four stool samples (Sze and Schloss 2019), extraction yield of 40 to 84% (Zemb 2020) and a 66.7-fold spike-in recovery range (Zhou 2011, abstract).
  conf: not stated · class: not stated · holds: the four studies named; each small-n, two abstract-level · src: paradaEveryBaseMatters2016 (AB), szeImpactDNAPolymerase2019 (FT), zembAbsoluteQuantitationMicrobes2020 (FT), zhouReproducibilityQuantitationAmplicon2011 (AB) · trail: MB-01 §critic, §2.14, §1. Overview, §answers, §8. Answers · from: MB-01:C-020, MB-01:B-0189, MB-01:A-110, MB-01:A-300, MB-01:I-0003
- **bias-consistency.8** A 0.1% genomic spike was recovered at 0.06% to 5.34% of reads across soils, a 66.7-fold range; the 66.7-fold figure is in the abstract, the 0.06 to 5.34% range needs the body and could not be confirmed.
  conf: single (marker) · class: meas (marker) · holds: soils · limit: access (critic: MB-01:C-076) · src: zhouReproducibilityQuantitationAmplicon2011 (AB; meas; single; critic: MB-01:C-075 was "FT per statistics angle; meas; single") · trail: MB-01 §2.14, §5.5, §answers, §Adversarial · from: MB-01:I-0075, MB-01:A-268, MB-01:B-0320, MB-01:C-073, MB-01:C-074, MB-01:C-075, MB-01:C-076
- **bias-consistency.9** Whether mock-derived bias applies to field samples is in conflict: Parada 2016 against calibration claims (McLaren 2019; Silverman 2021). Neither side's small-n and access limits are stated symmetrically in the review's strength line.
  conf: not stated · class: not stated · holds: one primer pair and one taxon (Parada, abstract only) against 7 taxa mixed as cells (McLaren) · src: paradaEveryBaseMatters2016, mclarenConsistentCorrectableBias2019, silvermanMeasuringMitigatingPCR2021 · trail: MB-01 §answers, §6. Where, §Adversarial · from: MB-01:A-121, MB-01:B-0338, MB-01:C-128, MB-01:C-129, MB-01:C-130, MB-01:C-092
- **bias-consistency.10** Evidence on whether bias is consistent across samples is weak: it rests mainly on one reanalysis of 7 taxa, with contrary or limiting field evidence.
  conf: not stated · class: not stated · holds: the evidence above · src: none (the review's and critic's rating of the evidence) · trail: MB-01 §answers, §8. Answers, §critic · from: MB-01:A-114, MB-01:A-301, MB-01:C-022 · rating: "weak for consistency"

### microbial-load: total microbial load
needs: none
- **microbial-load.1** Microbial load differs up to tenfold among healthy human faeces.
  conf: repl (marker) · class: meas (marker) · holds: healthy human faeces; abstract only; the critic says the body supports the microbial-load ranges · src: vandeputteQuantitativeMicrobiomeProfiling2017 (AB; meas; repl) · trail: MB-01 §3.5, §answers, §critic · from: MB-01:I-0089, MB-01:A-167, MB-01:C-023
- **microbial-load.2** Prokaryote load differed 27-fold among Antarctic seawater stations.
  conf: single (marker) · class: meas (marker) · holds: Antarctic seawater · src: linTowardsQuantitativeMicrobiome2019 (FT; meas; single) · trail: MB-01 §3.5, §answers · from: MB-01:I-0090, MB-01:A-167
- **microbial-load.3** Microbial load differed by more than six orders of magnitude across mouse gut sites.
  conf: single (marker) · class: meas (marker) · holds: mouse gut sites · src: barlowQuantitativeSequencingFramework2020 (FT; meas; single) · trail: MB-01 §3.5, §answers · from: MB-01:I-0091, MB-01:A-167

### read-depth: reads per sample and variation in depth between samples
needs: sequencing-platform
- **read-depth.1** The Earth Microbiome Project averaged 80,000 sequences per sample over 27,751 samples and rarefied to 5,000; in four environments, mean prevalence of tag sequences rose with depth up to 50,000, so 5,000 under-estimated prevalence.
  conf: not stated · class: not stated · holds: EMP · src: thompsonCommunalCatalogueReveals2017 · trail: MB-01 §3.3, §answers · from: MB-01:B-0212, MB-01:B-0213, MB-01:A-154, MB-01:A-155
- **read-depth.2** In one 360-sample MiSeq run, reads averaged 9,913 pairs per sample, with 95% of samples above 2,454.
  conf: not stated · class: not stated · holds: one run; the critic could not confirm these figures, which need the body · limit: access (critic: MB-01:C-076) · src: kozichDevelopmentDualindexSequencing2013 · trail: MB-01 §3.3, §answers, §Adversarial · from: MB-01:B-0214, MB-01:B-0215, MB-01:A-156, MB-01:C-076
- **read-depth.3** A dilution-series run ranged from 40,927 to 251,419 reads per sample, and three mock runs gave 36,464 to 146,653 read pairs.
  conf: not stated · class: not stated · holds: Karstens 2019 and Prodan 2020 · src: karstensControllingContaminantsLowbiomass2019, prodanComparingBioinformaticPipelines2020 · trail: MB-01 §3.3, §answers · from: MB-01:B-0216, MB-01:B-0217, MB-01:A-157
- **read-depth.4** Across 12 public V4 studies, reads per sample varied up to about 100-fold within a study: human 10,439 to 422,904 (median 32,452, n = 490), bioethanol 3,690 to 356,027, mice 1,804 to 30,311, soil 46,622 to 58,935 (n = 18), marine 132,895 to 256,758 (n = 7). These are per study, not per run.
  conf: single (marker) · class: meas (marker) · holds: 12 public V4 datasets; re-opened and checked by the synthesis agent and the critic (Table 1 read ranges); the within-study range rests mainly on Schloss 2024b Table 1 · src: schlossRarefactionCurrentlyBest2024 (FT, re-opened; meas; single) · trail: MB-01 §3.3, §answers, §critic · from: MB-01:I-0084, MB-01:B-0218, MB-01:A-158, MB-01:A-172, MB-01:A-184, MB-01:A-302, MB-01:C-054 · rating: "Moderate for reads per sample per study"
- **read-depth.5** Schloss attributes the within-study spread to compounding random error when PCR products are pooled, and cites studies reporting that depth correlates positively with biomass despite normalisation (known only through Schloss).
  conf: not stated · class: not stated · holds: secondary for the biomass correlation; the two primary studies (Minich 2022, Cruz 2021) were not opened · src: schlossRarefactionCurrentlyBest2024 · trail: MB-01 §3.3, §Adversarial · from: MB-01:B-0219, MB-01:B-0220, MB-01:C-111
- **read-depth.6** Makers claim more than 20 million reads per MiSeq v3 run and more than 100,000 per sample at 96-plex, said to be "sufficient to fully survey the bacterial composition"; a core facility gives about 20 million (v3) and about 16 million (v2) reads per run, with more than 100,000 per sample recommended.
  conf: not stated · class: not stated · holds: makers' and a core facility's statements · src: illumina16SMetagenomicSequencing (maker's claim), emoryAmplicon16SMetagenomics (PROTOCOL) · trail: MB-01 §3.3, §answers · from: MB-01:B-0221, MB-01:B-0222, MB-01:A-159, MB-01:A-182
- **read-depth.7** Median Good's coverage ranged from 89.4% (seagrass) to 99.8% (human), and reaching 95% and 99% coverage required about 3 and 101 times the sequences needed for 90%.
  conf: not stated · class: deriv (note: "[deriv]") · holds: the 12 public V4 datasets; checked by the critic · src: schlossRarefactionCurrentlyBest2024 · trail: MB-01 §3.3, §critic · from: MB-01:B-0223, MB-01:B-0224, MB-01:I-0084, MB-01:C-054
- **read-depth.8** No peer-reviewed coefficient of variation of reads per sample within a run after equimolar pooling was found; all three angles searched, and web search returned only forum posts.
  conf: not stated · class: search (note: "All three angles searched") · holds: all three angles; web search · src: none (a statement about what the search found) · trail: MB-01 §3.3, §answers, §Search record · from: MB-01:B-0225, MB-01:B-0226, MB-01:A-160, MB-01:A-173, MB-01:A-304, MB-01:B-0379, MB-01:B-0017

### abundance-distribution: how abundance is distributed among taxa (species abundance distributions)
needs: none
- **abundance-distribution.1** In 24 Oklahoma grassland soils, the best-fitting abundance distributions were exponential or inverse gamma; these best fits are in the paper's supplementary Table S3, the main text does not state which distributions won, and they were not verified.
  conf: single (marker) · class: model (marker) · holds: 24 grassland soils, 454 data; soil SAD shape rests on Zhou 2013 and Haegeman 2013 · limit: access (critic: MB-01:C-079) · src: zhouRandomSamplingProcess2013 (FT; model; single) · trail: MB-01 §3.4, §answers, §critic, §Adversarial · from: MB-01:I-0085, MB-01:A-161, MB-01:A-162, MB-01:A-186, MB-01:C-025, MB-01:C-026, MB-01:C-077, MB-01:C-078, MB-01:C-079, MB-01:C-031
- **abundance-distribution.2** In one Brazilian soil, 26,079 reads and 2,880 observed species were fitted equally well by communities of 10^4, 10^5 and 10^6 species, so the tail cannot be identified from sample data.
  conf: repl (marker) · class: model (marker) · holds: one Brazilian soil; the full text was not openly retrievable and these figures could not be confirmed · limit: access (critic: MB-01:C-028) · src: haegemanRobustEstimationMicrobial2013 (FT; model; repl) · trail: MB-01 §3.4, §answers, §critic · from: MB-01:I-0086, MB-01:A-163, MB-01:C-028
- **abundance-distribution.3** After copy-number correction, rank-abundance distributions from human skin and ocean fit a lognormal better; this single study pools ocean and skin into one item, and the same paper's simulations assumed a lognormal.
  conf: single (critic: MB-01:C-027) · class: not stated · holds: human skin and ocean together; water and host not separated · src: kembelIncorporating16SGene2012 · trail: MB-01 §3.4, §answers, §critic, §Adversarial · from: MB-01:B-0227, MB-01:A-164, MB-01:C-027, MB-01:C-134
- **abundance-distribution.4** Lognormal dynamics best explained microbial abundance distributions across more than 20,000 samples; the abstract gives no per-environment breakdown, and soils are included but not reported separately.
  conf: single (marker) · class: model (marker) · holds: cross-environment compilation; abstract only in both notes · src: shoemakerMacroecologicalTheoryMicrobial2017 (AB; model; single) · trail: MB-01 §3.4, §answers, MB-02 §D3.1, §answers · from: MB-01:I-0087, MB-01:B-0228, MB-01:B-0229, MB-01:A-165, MB-02:B-0236, MB-02:B-0238, MB-02:A-087
- **abundance-distribution.5** A dominance scaling law held across about 35,000 sites.
  conf: not stated · class: not stated · holds: cross-environment compilation including soils, not reported separately; abstract only · src: loceyScalingLawsPredict2016 (AB) · trail: MB-02 §D3.1, §answers · from: MB-02:B-0237, MB-02:A-087
- **abundance-distribution.6** Mean abundances across taxa were lognormal "for all the data sets considered", and each taxon's abundance across communities was gamma-distributed with variance proportional to the squared mean; per-biome results are in supplementary figures that were not read.
  conf: single (marker) · class: model (marker) · holds: Grilli's compiled datasets; partly re-opened by the synthesis agent · src: grilliMacroecologicalLawsDescribe2020 (FT, partly re-opened; model; single) · trail: MB-01 §3.4, §answers · from: MB-01:I-0088, MB-01:B-0230, MB-01:A-166
- **abundance-distribution.7** The soil SAD shape is in partial conflict: exponential or inverse gamma (Zhou 2013) against lognormal (Shoemaker 2017; Grilli 2020); these use different fitting targets, and Haegeman 2013 argues the tail is not identifiable from sample data at all.
  conf: cont (note: "the conflict is only partial") · class: not stated · holds: different fitting targets · src: zhouRandomSamplingProcess2013, shoemakerMacroecologicalTheoryMicrobial2017, grilliMacroecologicalLawsDescribe2020, haegemanRobustEstimationMicrobial2013 · trail: MB-01 §answers · from: MB-01:A-175, MB-01:A-176
- **abundance-distribution.8** Abundance-distribution shapes reported separately for water and for host-associated 16S data were not found beyond the copy-correction fits in Kembel 2012, although per-biome supplementary figures (Grilli 2020) and Shoemaker 2017's full text exist and were not read.
  conf: not stated · class: search (note: "no angle located such a breakdown") · holds: all angles · src: kembelIncorporating16SGene2012, grilliMacroecologicalLawsDescribe2020, shoemakerMacroecologicalTheoryMicrobial2017 · trail: MB-01 §3.4, §answers, §8. Answers, §Search record, §Adversarial · from: MB-01:B-0231, MB-01:B-0386, MB-01:A-174, MB-01:A-305, MB-01:C-114 · rating: "Weak for abundance-distribution shapes split by environment"
- **abundance-distribution.9** In bulk-soil amplicon data from the global datasets found, a small minority of taxa carries a large share of reads, and most taxa are rare.
  conf: repl (note: "replicated across global amplicon datasets") · class: not stated · holds: bulk-soil amplicon reads; also older clone and reassociation studies · src: delgadobaquerizoGlobalAtlasDominant2018, bickelChosenFewVariations2021 · trail: MB-02 §answers, §critic · from: MB-02:C-039, MB-02:A-081, MB-02:A-090, MB-02:B-0219 · rating: "Moderate for the qualitative shape"
- **abundance-distribution.10** Across 237 soils, per-sample richness ranged from 774 to 2,869 phylotypes, and 511 of 25,224 phylotypes (2%), defined as dominant jointly by abundance and ubiquity, accounted on average for 41% of 16S reads per sample: more than half in arid forests and only about 20% in tropical forests.
  conf: not stated · class: not stated · holds: 237 soils, global; per-sample mean · src: delgadobaquerizoGlobalAtlasDominant2018 (FT) · trail: MB-02 §D3.1, §answers, §critic · from: MB-02:B-0220, MB-02:A-081, MB-02:C-041
- **abundance-distribution.11** Across 844 soils (318 sites, 90-bp V4 ASVs), 0.4% of ASVs, classed common on the globally pooled rank-abundance distribution, held about 58% of pooled relative abundance, and the 99.6% classed rare held 42%; drier soils had more even distributions, and the ratio of rare to common richness declined with rainfall frequency (Pearson r = -0.41, n = 318).
  conf: not stated · class: not stated · holds: 844 soils pooled globally; checked by the critic · src: bickelChosenFewVariations2021 (FT) · trail: MB-02 §D3.1, §answers, §critic · from: MB-02:B-0221, MB-02:B-0222, MB-02:B-0223, MB-02:A-082, MB-02:C-042, MB-02:C-057
- **abundance-distribution.12** The two dominant-share figures must be kept apart: about 41% for a top-10%-and-ubiquitous definition (per-sample mean) and about 58% for the 0.4% common class (pooled global relative abundance) use different definitions and denominators and are not comparable.
  conf: not stated · class: not stated · holds: Delgado-Baquerizo 2018 and Bickel and Or 2021 · src: delgadobaquerizoGlobalAtlasDominant2018, bickelChosenFewVariations2021 · trail: MB-02 §D3.1, §answers, §critic, §Adversarial · from: MB-02:B-0226, MB-02:A-094, MB-02:C-040, MB-02:C-043, MB-02:C-060, MB-02:C-135, MB-02:A-148
- **abundance-distribution.13** Across 146 soils, archaeal reads averaged 2% of 16S reads (0 to over 10%), and two Thaumarchaeota (then Crenarchaeota) phylotypes made up over 70% of archaeal sequences.
  conf: single (critic: MB-02:C-044) · class: not stated · holds: 146 soils, 2010-era 454 data; one study, abstract only · src: batesExaminingGlobalDistribution2011 (AB) · trail: MB-02 §D3.1, §answers, §critic, §Adversarial · from: MB-02:B-0224, MB-02:B-0225, MB-02:A-083, MB-02:A-099, MB-02:C-044, MB-02:C-091
- **abundance-distribution.14** Four Arizona soils were consistent with lognormal null models; small surveys reproduced richness but not composition, and documenting half the species would need 16,284 to 44,000 individuals.
  conf: not stated · class: model (note: "lognormal null models") · holds: clone libraries, four Arizona soils; abstract only · src: dunbarEmpiricalTheoreticalBacterial2002 (AB) · trail: MB-02 §D3.1, §answers · from: MB-02:B-0227, MB-02:B-0228, MB-02:B-0229, MB-02:B-0230, MB-02:A-086
- **abundance-distribution.15** Lognormal-based estimates gave 6,400 to 38,000 taxa per gram of soil.
  conf: not stated · class: model (note: "modelled") · holds: abstract only · src: curtisEstimatingProkaryoticDiversity2002 (AB) · trail: MB-02 §D3.1, §answers · from: MB-02:B-0231, MB-02:A-086
- **abundance-distribution.16** Soils may need hundreds of times current sampling to reach 90% of taxa, and diversity estimates depend on the distribution assumed.
  conf: not stated · class: not stated · holds: abstract only · src: quinceRationalExplorationMicrobial2008 (AB) · trail: MB-02 §D3.1, §answers · from: MB-02:B-0232, MB-02:A-086
- **abundance-distribution.17** DNA reassociation kinetics, which measure whole-community DNA rather than reads or cells, were best fitted by a power law, implying over a million distinct genomes in a pristine soil; metal pollution cut diversity by over 99.9%. This is the main contrary result on the shape of the distribution, and removing it removes the power-law side of the conflict.
  conf: not stated · class: not stated · holds: whole-community DNA; abstract only · src: gansComputationalImprovementsReveal2005 (AB) · trail: MB-02 §D3.1, §answers · from: MB-02:B-0233, MB-02:B-0234, MB-02:B-0235, MB-02:A-085, MB-02:A-098
- **abundance-distribution.18** The functional form of the soil abundance distribution (lognormal versus power law) is contested and method-dependent: power law from reassociation kinetics against lognormal from clone-library models and large amplicon compilations; most of that evidence is abstract-only or modelled.
  conf: cont (critic: MB-02:C-045) · class: not stated · holds: the studies above · src: gansComputationalImprovementsReveal2005, curtisEstimatingProkaryoticDiversity2002, dunbarEmpiricalTheoreticalBacterial2002, shoemakerMacroecologicalTheoryMicrobial2017 · trail: MB-02 §answers, §critic · from: MB-02:C-045, MB-02:A-091, MB-02:A-093, MB-02:A-149 · rating: "Weak for the functional form"
- **abundance-distribution.19** No soil taxon abundance distribution built from metagenome coverage was found.
  conf: not stated · class: search (note: "I found no soil taxon abundance distribution built from metagenome coverage") · holds: MB-02's searches; genome-resolved global soil metagenomes were not covered · src: none (a statement about what the search found) · trail: MB-02 §D3.1, §answers, §critic · from: MB-02:B-0239, MB-02:B-0240, MB-02:A-088, MB-02:A-150, MB-02:C-046, MB-02:C-047
- **abundance-distribution.20** Iowa corn and prairie soil metagenomes totalled about 300 Gbp, yet 80% of reads could not be assembled for low coverage, and 48% and 31% of contigs had coverage below 10x.
  conf: not stated · class: not stated · holds: Iowa soils · src: howeTacklingSoilDiversity2014 (FT) · trail: MB-02 §D3.1, §answers · from: MB-02:B-0241, MB-02:A-088
- **abundance-distribution.21** Tropical soils are among the least-covered communities by Nonpareil estimates.
  conf: not stated · class: not stated · holds: qualitative · src: rodriguezrEstimatingCoverageMetagenomic2014 (FT, qualitative) · trail: MB-02 §D3.1, §answers · from: MB-02:B-0242, MB-02:A-088
- **abundance-distribution.22** 85% of the amplicon-defined dominant soil phylotypes were also dominant in 123 shotgun soil metagenomes; this is the only global amplicon-metagenome cross-check.
  conf: not stated · class: not stated · holds: 123 shotgun soil metagenomes · src: delgadobaquerizoGlobalAtlasDominant2018 (FT) · trail: MB-02 §D3.1, §answers · from: MB-02:B-0243, MB-02:A-088, MB-02:A-097
- **abundance-distribution.23** No taxon abundance distribution from cell counts in soil was found; the cell-based soil data found concern only total DNA per cell, and the search route for cell counts was narrow.
  conf: not stated · class: search (note: "No taxon abundance distribution from cell counts in soil was found") · holds: extended WebSearch on soil species abundance distributions from FISH, flow cytometry, spike-ins and absolute quantification; taxon-specific CARD-FISH cell counts were not searched beyond SAD-specific queries · src: none (a statement about what the search found) · trail: MB-02 §D3.1, §answers, §Search record, §Adversarial · from: MB-02:B-0244, MB-02:A-089, MB-02:A-092, MB-02:B-0298, MB-02:C-117
- **abundance-distribution.24** Absolute-abundance work multiplies relative abundance by total counts (flow cytometry or qPCR), which converts gene copies but not cells per taxon.
  conf: not stated · class: not stated · holds: non-soil; abstract only · src: propsAbsoluteQuantificationMicrobial2016 (AB) · trail: MB-02 §D3.1 · from: MB-02:B-0245
- **abundance-distribution.25** Not found for soil: metagenome-based taxon abundance distributions reported as a distribution, copy-number- or ploidy-corrected abundance distributions, and rhizosphere-specific abundance distributions.
  conf: not stated · class: search (note: "none found as such") · holds: MB-02's searches · src: none (a statement about what the search found) · trail: MB-02 §answers · from: MB-02:A-095

### sampling-model: sampling from the pool of amplified molecules (Poisson and multinomial models)
needs: read-depth, abundance-distribution, technical-replicates
group: replicates
- **sampling-model.1** A Poisson random-sampling model of long-tailed abundance distributions predicted the low OTU overlap among soil technical replicates with no significant difference from the observed values, and about 60,900 sequences per replicate would be needed for 90% overlap.
  conf: single (marker) · class: model (marker) · holds: Zhou 2011's 24 Oklahoma grassland soils on 454; the predicted reads for 90% overlap rest on Zhou 2013 · src: zhouRandomSamplingProcess2013 (FT; model; single) · trail: MB-01 §4.1, §answers · from: MB-01:B-0233, MB-01:I-0093, MB-01:A-187, MB-01:A-188, MB-01:A-210, MB-01:A-229, MB-01:C-031
- **sampling-model.2** The evidence that Poisson or multinomial sampling explains replicate disagreement in taxa detected comes from one dataset and one laboratory: Zhou 2013 modelled the same 24 Oklahoma grassland soils, sequenced on 454, that Zhou 2011 reported, and Wen 2017 is from the same laboratory; Wen 2017's MiSeq replicates cut against pure sampling. That sampling alone explains replicate disagreement in taxa detected is weak and contested.
  conf: cont (critic: MB-01:C-036) · class: not stated · holds: one 454 soil dataset and one laboratory · src: zhouRandomSamplingProcess2013, zhouReproducibilityQuantitationAmplicon2011, wenEvaluationReproducibilityAmplicon2017 · trail: MB-01 §critic, §Adversarial · from: MB-01:C-030, MB-01:C-031, MB-01:C-032, MB-01:C-033, MB-01:C-036, MB-01:C-086, MB-01:C-135
- **sampling-model.3** Zhou 2013 predicted about 60,900 reads for 90% OTU overlap, but in Wen 2017 unweighted overlap plateaued at 39% near 30,000 reads (with singletons) and reached only 43.9% at 160,000 reads; Wen's authors attribute rare-OTU variation to random sampling plus sequencing artefacts and report that "biases other than random sampling" affect unweighted metrics more.
  conf: not stated · class: not stated · holds: Wen 2017, as reported by the critic · src: zhouRandomSamplingProcess2013, wenEvaluationReproducibilityAmplicon2017 · trail: MB-01 §critic, §Adversarial · from: MB-01:C-034, MB-01:C-035, MB-01:C-120, MB-01:C-121, MB-01:C-063
- **sampling-model.4** The sampling account (Zhou 2013) and technical variance beyond counting (Silverman 2018, 76%) differ in setting and in measure (OTU overlap versus variance of relative abundance); the review holds only the beyond-counting side to that caution, while the sampling side's own counter-evidence is left out.
  conf: not stated · class: not stated · holds: the two differ in setting and in measure · src: zhouRandomSamplingProcess2013, silvermanDynamicLinearModels2018 · trail: MB-01 §answers, §6. Where, §Adversarial · from: MB-01:A-218, MB-01:B-0339, MB-01:C-122, MB-01:C-123
- **sampling-model.5** For one caecal extract, the abundance at which the CV of a taxon's relative abundance between technical replicates reached 30% fell with the square root of read depth, as Poisson noise would predict; this rests on one caecal extract with four technical replicates.
  conf: single (marker) · class: meas (marker) · holds: one mouse caecal extract, four technical replicates · src: barlowQuantitativeSequencingFramework2020 (FT; meas; single) · trail: MB-01 §4.1, §answers, §critic, §Adversarial · from: MB-01:I-0094, MB-01:A-189, MB-01:A-206, MB-01:C-037, MB-01:C-085, MB-01:C-115
- **sampling-model.6** The "technical replicates are Poisson" assumption comes from RNA-seq: Illumina lane replicates fit a Poisson model, with about 0.5% of genes deviating; McMurdie and Holmes adopt it for technical replicates, so it rests on RNA-seq, not on 16S technical replicates.
  conf: not stated · class: meas (marker) · holds: RNA-seq lane replicates, labelled INDIRECT · src: marioniRNAseqAssessmentTechnical2008 (FT; meas; INDIRECT), mcmurdieWasteNotWant2014 · trail: MB-01 §4.1, §answers · from: MB-01:I-0095, MB-01:B-0234, MB-01:A-191
- **sampling-model.7** Each taxon's abundance across communities followed a gamma distribution (Taylor's law with exponent 2); treating absences as Poisson sampling at each sample's depth predicted occupancy from mean abundance and variance with no further parameters, and the model reproduced the abundance-occupancy relationship, so the author attributes absences mostly to sampling. The text read does not name soil among the biomes.
  conf: not stated · class: not stated · holds: Grilli's compiled datasets; nearest precedent for soil (non-soil); whether the datasets include soil was not checked in the Supplementary Information; the only parameter-free sampling null · src: grilliMacroecologicalLawsDescribe2020 (FT) · trail: MB-01 §4.2, §answers, MB-02 §D3.3, §answers, §Adversarial · from: MB-01:B-0237, MB-01:B-0238, MB-01:A-193, MB-02:B-0276, MB-02:B-0277, MB-02:B-0278, MB-02:A-112, MB-02:A-124, MB-02:C-120

### technical-replicates: technical replicates at different read depths
needs: sampling-model, read-depth
group: replicates
- **technical-replicates.1** Technical replicates of the same soil DNA amplified with different barcodes shared 17.2 ± 2.3% of OTUs between two replicates and 8.2 ± 2.3% among three on 454, attributed to random sampling; the paper's discussion gives 13.1% and 5.9%, which differ from its abstract.
  conf: single (marker) · class: meas (marker) · holds: 24 communities from one Oklahoma warming site, 454; the figures 17.2% and 8.2% are in the abstract, the discussion values need the body and could not be confirmed · limit: access (critic: MB-01:C-076) · src: zhouReproducibilityQuantitationAmplicon2011 (AB; meas; single; critic: MB-01:C-075 was "FT; meas; single") · trail: MB-01 §4.1, §answers, §Adversarial, MB-02 §D3.3, §critic · from: MB-01:I-0092, MB-01:B-0232, MB-01:A-208, MB-01:C-065, MB-01:C-075, MB-01:C-076, MB-02:B-0265, MB-02:C-058, MB-02:C-086
- **technical-replicates.2** In one soil sample, abundance-weighted OTU overlap among technical replicates rose from 56.7% at 2,000 reads to 95.3% at 160,000, and Bray-Curtis among technical replicates was 0.269 against 0.374 among treatment replicates.
  conf: repl (marker) · class: meas (marker) · holds: one soil sample on MiSeq; depth curves for replicate overlap on MiSeq rest on Wen 2017 · src: wenEvaluationReproducibilityAmplicon2017 (FT; meas; repl) · trail: MB-01 §4.4, §answers · from: MB-01:I-0105, MB-01:A-203, MB-01:A-207, MB-01:A-227, MB-01:B-0254
- **technical-replicates.3** On MiSeq, 18 soil extracts shared 33.4% of OTUs between two replicates and 20.2% among three; in one deeply sequenced sample, presence/absence overlap rose from 20.7% at 2,000 reads to 43.9% at 160,000, plateauing near 30,000. Overlap was lower when replicates were sequenced in separate runs.
  conf: not stated · class: not stated · holds: 18 soil extracts, MiSeq; the run effect is reported by the critic · src: wenEvaluationReproducibilityAmplicon2017 · trail: MB-01 §4.4, §answers, §critic · from: MB-01:B-0258, MB-01:B-0259, MB-01:B-0260, MB-01:A-209, MB-01:C-035
- **technical-replicates.4** Alpha diversity did not differ among technical replicates (Wen 2017), and replicate variation affected beta diversity more than alpha diversity (Zhou 2011).
  conf: not stated · class: not stated · holds: technical replicates (Wen 2017; Zhou 2011) · src: wenEvaluationReproducibilityAmplicon2017, zhouReproducibilityQuantitationAmplicon2011 · trail: MB-01 §4.4 · from: MB-01:B-0262, MB-01:B-0263
- **technical-replicates.5** Greater depth improved replicate agreement in beta diversity for some mocks only.
  conf: not stated · class: not stated · holds: Pinto and Raskin's mocks · src: pintoPCRBiasesDistort2012 · trail: MB-01 §4.4 · from: MB-01:B-0256
- **technical-replicates.6** A preprint reports replicate Jaccard distances of typically about 0.15, and up to 0.71 across runs.
  conf: not stated · class: not stated · holds: preprint abstract · src: edgarUNBIASAttemptCorrect2017 (AB; PREPRINT) · trail: MB-01 §4.4, §answers · from: MB-01:B-0257, MB-01:A-225
- **technical-replicates.7** In fungal ITS, OTUs averaging more than 10 reads were detected in nearly all replicates, and replicate dissimilarity (pseudo-beta-diversity) fell markedly with depth.
  conf: not stated · class: not stated · holds: fungal ITS, labelled INDIRECT · src: smithSequenceDepthNot2014 (INDIRECT, ITS) · trail: MB-01 §4.4, §answers · from: MB-01:B-0261, MB-01:A-190, MB-01:A-211
- **technical-replicates.8** Pooling PCR replicates had no detectable effect at moderate to high input (Smith and Peay 2014; Marotz 2019, abstract; Kennedy 2014, abstract), but replicates split before PCR disagreed strongly at low load (Dyrhovden 2021).
  conf: not stated · class: not stated · holds: Smith and Peay 2014 is fungal ITS; no single study tested both conditions · src: smithSequenceDepthNot2014, marotzTriplicatePCRReactions2019, kennedyEvaluatingBiasIlluminabased2014, dyrhovdenManagingContaminationDiverse2021 · trail: MB-01 §answers, §7. Bounds · from: MB-01:A-212, MB-01:A-220, MB-01:B-0347, MB-01:A-221
- **technical-replicates.9** That the difference in load is the likely reason for the pooled-versus-single PCR contrast is the reviewer's own reconciliation; no single study tested both conditions.
  conf: not stated · class: reading (critic: MB-01:C-140) · holds: untested · src: none (the reviewer's reading) · trail: MB-01 §answers, §Adversarial · from: MB-01:A-221, MB-01:C-139, MB-01:C-140, MB-01:C-141
- **technical-replicates.10** The depth dependence of replicate agreement is rated moderate (Wen 2017; Zhou 2013; Smith and Peay 2014; Barlow 2020).
  conf: not stated · class: not stated · holds: the four studies named · src: wenEvaluationReproducibilityAmplicon2017, zhouRandomSamplingProcess2013, smithSequenceDepthNot2014, barlowQuantitativeSequencingFramework2020 · trail: MB-01 §answers · from: MB-01:A-216 · rating: "Moderate for the depth dependence of replicate agreement"
- **technical-replicates.11** Not found: a 16S study testing whether technical-replicate variance of relative abundance exceeds multinomial expectation across controlled read depths, and replicate-at-depth studies in water or host samples other than gut; replicate-at-depth studies are confined to one soil laboratory (Zhou, Wen) and one mouse caecum (Barlow).
  conf: not stated · class: search (note: "statistics angle; Europe PMC and web search") · holds: statistics angle · src: none (a statement about what the search found) · trail: MB-01 §answers, §critic, §Adversarial · from: MB-01:A-222, MB-01:C-040, MB-01:C-115

### overdispersion: overdispersed count models (Dirichlet-multinomial and others)
needs: sampling-model
- **overdispersion.1** Human oral plaque counts rejected the multinomial in favour of the Dirichlet-multinomial, with overdispersion theta of 0.047 and 0.054.
  conf: repl (marker) · class: meas (marker) · holds: oral plaque, between biological samples · src: larosaHypothesisTestingPower2012 (FT; meas; repl) · trail: MB-01 §4.2, §answers · from: MB-01:B-0235, MB-01:I-0096, MB-01:A-192
- **overdispersion.2** Every public dataset surveyed showed more variance than Poisson among biological replicates.
  conf: repl (marker) · class: meas (marker) · holds: public datasets, between biological replicates · src: mcmurdieWasteNotWant2014 (FT; meas; repl) · trail: MB-01 §4.2, §answers · from: MB-01:I-0097, MB-01:A-192
- **overdispersion.3** Hierarchical Dirichlet-multinomial models detected shifts better than alternatives in simulation.
  conf: single (marker) · class: model (marker) · holds: simulation; abstract only · src: harrisonDirichletmultinomialModellingOutperforms2020 (AB; model; single) · trail: MB-01 §4.2 · from: MB-01:I-0098
- **overdispersion.4** Beta-binomial and logistic-normal network models relax the multinomial further, according to their makers.
  conf: not stated · class: not stated · holds: makers' claims; abstracts only · src: martinModelingMicrobialAbundances2020 (AB; makers' claims), willisEstimatingDiversityNetworked2022 (AB; makers' claims) · trail: MB-01 §4.2 · from: MB-01:B-0236
- **overdispersion.5** Dirichlet-multinomial overdispersion has been shown only between biological samples, not among technical replicates: no study fitting overdispersion to 16S technical replicates was found.
  conf: not stated · class: search (note: "No study fitting overdispersion to 16S technical replicates was found") · holds: statistics angle · src: none (a statement about what the search found) · trail: MB-01 §4.2, §answers, §critic, §Search record · from: MB-01:B-0239, MB-01:A-217, MB-01:B-0383, MB-01:C-039

### technical-variation: processes other than sampling (early amplification, runs and batches, dropout)
needs: sampling-model, pcr
- **technical-variation.1** In four artificial-gut vessels sampled hourly with 20 technical replicates per vessel, 76% of observed variation was attributed to technical sources beyond sequence counting.
  conf: single (marker) · class: model (marker) · holds: one artificial-gut series; the 76% figure rests on Silverman 2018 alone · src: silvermanDynamicLinearModels2018 (FT; model; single) · trail: MB-01 §4.3, §answers, §critic · from: MB-01:I-0099, MB-01:B-0240, MB-01:A-194, MB-01:A-195, MB-01:A-226, MB-01:C-038
- **technical-variation.2** Replicates split before PCR differed strongly while replicates split after PCR were nearly identical; in negative extraction controls, most species appeared in only one of five PCR replicates, with a mean Jaccard distance of 0.80 (range 0.65 to 0.87).
  conf: single (marker) · class: meas (marker) · holds: negative extraction controls at low load; the before-versus-after PCR split rests on Dyrhovden 2021 · src: dyrhovdenManagingContaminationDiverse2021 (FT; meas; single) · trail: MB-01 §4.3, §answers, §critic, §Adversarial · from: MB-01:I-0100, MB-01:A-197, MB-01:A-228, MB-01:B-0241, MB-01:C-059, MB-01:C-082, MB-01:C-038
- **technical-variation.3** At 1:10^5 dilution of a staggered mock, 12 species appeared in only 2 of 4 PCR replicates.
  conf: not stated · class: not stated · holds: Dyrhovden's staggered mock · src: dyrhovdenManagingContaminationDiverse2021 · trail: MB-01 §4.3 · from: MB-01:B-0242
- **technical-variation.4** At low input, library preparation reached its Poisson loading limit, the two rarest taxa dropped out, and contaminants appeared below about 10^4 input copies.
  conf: not stated · class: not stated · holds: Barlow 2020 · src: barlowQuantitativeSequencingFramework2020 · trail: MB-01 §4.3, §answers · from: MB-01:B-0243, MB-01:A-202
- **technical-variation.5** In low-input pools of unique synthetic barcodes, random per-molecule amplification in early cycles was the main source of skew; late-cycle polymerase errors stayed at low copy number, template switching was rare and GC bias minor; at low input, early stochastic amplification and dropout affected detection.
  conf: single (marker) · class: meas (marker) · holds: synthetic barcode pools (Kebschull and Zador 2015), non-16S, labelled INDIRECT; the low-input detection clause also rests on Dyrhovden 2021 · src: kebschullSourcesPCRinducedDistortions2015 (FT; meas; single; INDIRECT, non-16S), dyrhovdenManagingContaminationDiverse2021 · trail: MB-01 §2.4, §4.3, §answers · from: MB-01:B-0123, MB-01:I-0034, MB-01:B-0244, MB-01:A-196, MB-01:A-063, MB-01:B-0064
- **technical-variation.6** One HiSeq run lost an archaeal mock taxon from all samples and shifted others by more than 2-fold, while re-running the same amplicons was normal.
  conf: single (marker) · class: meas (marker) · holds: one run, one mock · src: yehTaxonDisappearanceMicrobiome2018 (FT; meas; single) · trail: MB-01 §4.3, §2. Steps, §answers · from: MB-01:I-0101, MB-01:B-0245, MB-01:A-088, MB-01:A-089, MB-01:A-198, MB-01:B-0073
- **technical-variation.7** A PCR machine with a mis-set annealing temperature produced a batch outlier.
  conf: not stated · class: not stated · holds: Silverman 2021; checked by the critic · src: silvermanMeasuringMitigatingPCR2021 · trail: MB-01 §4.3, §answers, §critic · from: MB-01:B-0246, MB-01:A-198, MB-01:C-054
- **technical-variation.8** Per-strain CV across five runs had a median of 11.8% (range 5.5 to 73.7%), and under-represented strains varied most.
  conf: not stated · class: not stated · holds: Laursen 2017, five runs · src: laursenGenomicGCcontentAffects2017 · trail: MB-01 §4.3, §answers · from: MB-01:B-0247, MB-01:A-204
- **technical-variation.9** Mean relative abundances were reproducible across two runs and two depths.
  conf: not stated · class: not stated · holds: Pinto and Raskin 2012, two runs and two depths · src: pintoPCRBiasesDistort2012 · trail: MB-01 §4.3, §answers · from: MB-01:B-0249, MB-01:A-199
- **technical-variation.10** Batch-correction tools exist, and their makers claim they work.
  conf: not stated · class: not stated · holds: makers' claims; abstracts only · src: gibbonsCorrectingBatchEffects2018 (AB), lingBatchEffectsRemoval2022 (AB) · trail: MB-01 §4.3 · from: MB-01:B-0251
- **technical-variation.11** Primer mismatch and low efficiency remove or suppress specific taxa (non-random dropout); in eDNA simulations with a low-efficiency primer set, a median of 88 of 1,000 taxa were detected after 20 cycles.
  conf: not stated · class: model (note: "[model; INDIRECT]") · holds: Parada 2016 and Walters 2016 for mismatch; eukaryotic eDNA simulation (Kelly 2019), labelled INDIRECT · src: paradaEveryBaseMatters2016, waltersImprovedBacterial16S2016, kellyUnderstandingPCRProcesses2019 (model; INDIRECT) · trail: MB-01 §4.3, §answers · from: MB-01:B-0252, MB-01:B-0253, MB-01:A-200, MB-01:A-201
- **technical-variation.12** Technical variance beyond counting, early stochastic amplification at low load, run failures and primer-driven dropout are measured, but each mostly in a single study.
  conf: single (note: "each mostly in a single study") · class: not stated · holds: Silverman 2018, Dyrhovden 2021, Yeh 2018 · src: silvermanDynamicLinearModels2018, dyrhovdenManagingContaminationDiverse2021, yehTaxonDisappearanceMicrobiome2018 · trail: MB-01 §8. Answers, §answers · from: MB-01:A-308, MB-01:A-215 · rating: "Weak on how much non-sampling technical variance there is"

### zeros: zeros in count tables
needs: sampling-model
- **zeros.1** In simulation, simple count models sufficed across four zero-generating processes, and zero inflation was warranted only under narrow conditions.
  conf: single (marker) · class: model (marker) · holds: simulation; abstract only · src: silvermanNaughtAllZeros2020 (AB; model; single) · trail: MB-01 §4.3, §answers · from: MB-01:I-0102, MB-01:A-213
- **zeros.2** Pseudocounts made tests conservative.
  conf: single (marker) · class: model (marker) · holds: abstract only · src: kaulAnalysisMicrobiomeData2017 (AB; model; single) · trail: MB-01 §4.3 · from: MB-01:I-0103
- **zeros.3** Schloss asserts that a microbiome zero more likely means true absence, which conflicts with Grilli 2020's sampling interpretation.
  conf: not stated · class: assert (marker) · holds: assertion against Grilli's model · src: schlossWasteNotWant2024 (FT; assert), grilliMacroecologicalLawsDescribe2020 · trail: MB-01 §4.3, §answers, §6. Where · from: MB-01:I-0104, MB-01:A-219, MB-01:B-0344

### alpha-diversity: richness and other alpha diversity measures under unequal depth
needs: read-depth
- **alpha-diversity.1** Chao1, ACE, CatchAll, Shannon and Simpson all varied with library size in pyrosequencing data.
  conf: repl (marker) · class: meas (marker) · holds: pyrosequencing data; abstract only · src: gihringMassivelyParallelRRNA2012 (AB; meas; repl) · trail: MB-01 §5.2, §answers · from: MB-01:I-0112, MB-01:A-274
- **alpha-diversity.2** In Schloss's null models built from 12 V4 datasets, observed richness, Chao1, ACE, breakaway and SRS-normalised richness all correlated with depth; Shannon was less depth-sensitive and inverse Simpson was not depth-sensitive.
  conf: cont (marker) · class: model (marker) · holds: null models built from 12 V4 datasets; re-opened by the synthesis agent · src: schlossRarefactionCurrentlyBest2024 (FT, re-opened; model; cont) · trail: MB-01 §5.2, §answers · from: MB-01:I-0113, MB-01:B-0269, MB-01:A-237, MB-01:A-242, MB-01:A-230
- **alpha-diversity.3** The depth dependence of raw and estimator richness is replicated (Gihring 2012; Schloss 2024b; Haegeman 2013).
  conf: repl (note: "is replicated") · class: not stated · holds: pyrosequencing data (Gihring 2012), null models (Schloss 2024b) and Haegeman 2013 · src: gihringMassivelyParallelRRNA2012, schlossRarefactionCurrentlyBest2024, haegemanRobustEstimationMicrobial2013 · trail: MB-01 §answers, §5.2 · from: MB-01:A-274, MB-01:I-0112
- **alpha-diversity.4** Multiplicative bias can make an uneven sample look more even, biasing Shannon and inverse Simpson.
  conf: not stated · class: model (note: "[model]") · holds: McLaren 2019's model · src: mclarenConsistentCorrectableBias2019 (model) · trail: MB-01 §5.2, §answers · from: MB-01:B-0289, MB-01:A-252
- **alpha-diversity.5** PCR-bias calibration improved Shannon in 7 of 10 mocks.
  conf: not stated · class: not stated · holds: Silverman 2021, 10 mocks · src: silvermanMeasuringMitigatingPCR2021 · trail: MB-01 §5.2 · from: MB-01:B-0290
- **alpha-diversity.6** In simulated faecal communities with load varying from 1.9 x 10^9 to 10^13 cells per gram, all 13 transformations reproduced Shannon and Simpson, but richness was recovered reliably only by quantitative profiling in a bloom scenario.
  conf: single (marker) · class: model (marker) · holds: simulated faeces, no taxon-specific bias in the simulated truth · src: llorensricoBenchmarkingMicrobiomeTransformations2021 (FT; model; single) · trail: MB-01 §5.2, §answers · from: MB-01:B-0291, MB-01:I-0118, MB-01:A-243, MB-01:C-051
- **alpha-diversity.7** In freshwater and sediment 454 data, 5,000 sequences captured Shannon trends and over 80% of Chao1 trends.
  conf: single (marker) · class: meas (marker) · holds: freshwater and sediment, 454; abstract only · src: lundinWhichSequencingDepth2012 (AB; meas; single) · trail: MB-01 §5.2 · from: MB-01:I-0119

### beta-diversity: between-sample (beta) diversity under unequal depth
needs: read-depth
- **beta-diversity.1** Proportions and rarefying were the only methods that fully normalised depth, and scaling methods masked differences in common OTUs.
  conf: single (marker) · class: model (marker) · holds: abstract only · src: mcknightMethodsNormalizingMicrobiome2019 (AB; model; single) · trail: MB-01 §5.3, §answers · from: MB-01:I-0123, MB-01:A-244, MB-01:A-249
- **beta-diversity.2** Whether proportions suffice for beta diversity is in conflict: McKnight 2019 against Schloss 2024b, in which relative-abundance Bray-Curtis stayed depth-sensitive under the null.
  conf: cont (note: "This conflicts with Schloss 2024b") · class: not stated · holds: an abstract-level result (McKnight 2019) against a null model (Schloss 2024b) · src: mcknightMethodsNormalizingMicrobiome2019, schlossRarefactionCurrentlyBest2024 · trail: MB-01 §5.3, §answers, §6. Where · from: MB-01:B-0295, MB-01:A-249, MB-01:A-281, MB-01:B-0342, MB-01:B-0325
- **beta-diversity.3** Library-size normalisation had very little effect on beta-diversity separation compared with the choice of distance metric.
  conf: single (marker) · class: meas (marker) · holds: abstract only · src: thorsenLargescaleBenchmarkingReveals2016 (AB; meas; single) · trail: MB-01 §5.3, §7. Bounds, §answers · from: MB-01:I-0124, MB-01:A-250, MB-01:B-0355
- **beta-diversity.4** Bray-Curtis was usually the most powerful metric, and metric choice changes power.
  conf: single (marker) · class: meas (marker) · holds: abstract only · src: kersPowerMicrobiomeStudies2022 (AB; meas; single) · trail: MB-01 §5.3 · from: MB-01:I-0126
- **beta-diversity.5** 1,000 denoised sequences explained 90% of the Bray-Curtis trends seen at 15,000 to 20,000.
  conf: not stated · class: not stated · holds: Lundin 2012 · src: lundinWhichSequencingDepth2012 · trail: MB-01 §5.3 · from: MB-01:B-0296, MB-01:B-0298

### rarefying: rarefying and rarefaction to a common depth
needs: read-depth, alpha-diversity, beta-diversity
- **rarefying.1** Rarefaction comes from ecology, traced to Sanders 1968, Hurlbert 1971 and Simberloff 1972; Gotelli and Colwell argue that individual-based rarefaction allows meaningful comparison and that asymptotic estimators give lower bounds; rarefaction curves are a display of sampling completeness and were not benchmarked as a comparison method in the sources found.
  conf: not stated · class: assert (marker) · holds: ecology, labelled INDIRECT; the origins known only secondarily via Chao and Jost 2012 · src: gotelliQuantifyingBiodiversityProcedures2001 (AB; assert; INDIRECT), sandersMarineBenthicDiversity1968 (SEC), hurlbertNonconceptSpeciesDiversity1971 (SEC), chaoCoveragebasedRarefactionExtrapolation2012 · trail: MB-01 §5.1, §5.6 · from: MB-01:B-0264, MB-01:I-0106, MB-01:B-0326
- **rarefying.2** Schloss distinguishes "rarefying" (one random subsample) from "rarefaction" (the mean over many subsamples). In his null models built from 12 V4 datasets, only repeated rarefaction removed the correlation between richness and depth; size-based iNEXT nearly did, except for the small, evenly sequenced marine and soil sets; when depth was confounded with group, only rarefaction and size-based iNEXT held a 5% false-positive rate, and rarefaction gave the highest power.
  conf: not stated · class: model (note: "modelled") · holds: multinomial-type null models; the author's conclusion · src: schlossRarefactionCurrentlyBest2024 · trail: MB-01 §5.2, §answers · from: MB-01:B-0270, MB-01:B-0271, MB-01:B-0272, MB-01:B-0273, MB-01:A-231, MB-01:A-232
- **rarefying.3** In Schloss's null models, Jaccard and Bray-Curtis computed from raw counts, relative abundances, CSS or SRS, as well as Aitchison distances (four zero-handling variants) and DESeq2 VST Euclidean distances, all correlated with depth differences; only rarefaction removed the correlation, and only rarefaction held 5% false positives in PERMANOVA under confounding.
  conf: not stated · class: not stated · holds: the same null models · src: schlossRarefactionCurrentlyBest2024 · trail: MB-01 §5.3, §answers · from: MB-01:B-0292, MB-01:B-0293, MB-01:A-245, MB-01:A-251, MB-01:A-271, MB-01:B-0327, MB-01:B-0329
- **rarefying.4** The null model reassigns sequences at random, so samples differ only through multinomial-type sampling; taxon-specific bias, technical variation beyond counting and differences in load are absent from the simulated truth.
  conf: not stated · class: reading (note: "statistics angle's reading") · holds: Schloss 2024b's design · src: schlossRarefactionCurrentlyBest2024 · trail: MB-01 §5.2 · from: MB-01:B-0274, MB-01:B-0275, MB-01:B-0276
- **rarefying.5** The claim that only rarefaction removes the depth dependence of alpha and beta diversity under confounding rests on Schloss 2024b (supported in part by Weiss 2017 for beta and differential abundance); removing Schloss 2024b would leave rarefying contested, with McMurdie and Holmes 2014 as the main benchmark against it.
  conf: not stated · class: model (note: "null-model simulations") · holds: null-model simulations dominated by one author · src: schlossRarefactionCurrentlyBest2024, weissNormalizationMicrobialDifferential2017, mcmurdieWasteNotWant2014 · trail: MB-01 §answers, §8. Answers · from: MB-01:A-290, MB-01:A-291, MB-01:A-310, MB-01:A-273, MB-01:C-041 · rating: "Weak to moderate overall"
- **rarefying.6** In Weiss 2017, rarefying clustered samples better for presence/absence metrics, and other normalisations were vulnerable below about 1,000 reads per sample.
  conf: repl (marker) · class: model (marker) · holds: simulations · src: weissNormalizationMicrobialDifferential2017 (FT; model; repl) · trail: MB-01 §5.3 · from: MB-01:I-0120
- **rarefying.7** In simulations from Global Patterns, rarefying to the 15th percentile and dropping samples below it reduced clustering accuracy.
  conf: cont (marker) · class: model (marker) · holds: simulations from the Global Patterns data · src: mcmurdieWasteNotWant2014 (FT; model; cont) · trail: MB-01 §5.3, §answers · from: MB-01:I-0121, MB-01:A-246
- **rarefying.8** Schloss identified 11 design choices that disadvantaged rarefying in McMurdie and Holmes 2014; notably, low-depth samples were removed only in the rarefied arm.
  conf: single (marker) · class: model (marker) · holds: re-analysis of McMurdie and Holmes's simulation · src: schlossWasteNotWant2024 (FT; model; single) · trail: MB-01 §5.3, §answers · from: MB-01:B-0294, MB-01:I-0122, MB-01:A-246
- **rarefying.9** In real river data, rarefying barely changed Bray-Curtis or Jaccard (r > 0.9) and did not change weighted UniFrac.
  conf: not stated · class: not stated · holds: freshwater (river) samples · src: chiarelloRankingBiasesChoice2022 · trail: MB-01 §5.3, §7. Bounds, §answers · from: MB-01:B-0296, MB-01:B-0297, MB-01:A-247, MB-01:B-0354
- **rarefying.10** Repeated rarefying shows that the random variation rarefying introduces grows as rarefied depth shrinks.
  conf: single (marker) · class: meas (marker) · holds: one study · src: cameronEnhancingDiversityAnalysis2021 (FT; meas; single) · trail: MB-01 §5.3, §answers · from: MB-01:I-0125, MB-01:A-248
- **rarefying.11** Willis argues that plug-in and rarefied richness are both negatively biased and that rarefying can create false differences between environments with equal richness but different abundance structures; she recommends estimators with variance estimates compared through measurement-error models. The paper gives statistical argument plus a worked simulated example, not assertion alone.
  conf: cont (marker) · class: not stated (critic: MB-01:C-043) · holds: Willis 2019 · src: willisRarefactionAlphaDiversity2019 (FT; cont; critic: MB-01:C-043 was "FT; assert; cont") · trail: MB-01 §5.2, §answers, §critic, §Adversarial · from: MB-01:B-0280, MB-01:I-0114, MB-01:A-233, MB-01:C-043, MB-01:C-044, MB-01:C-064, MB-01:C-124, MB-01:C-125, MB-01:C-126, MB-01:B-0341
- **rarefying.12** Breakaway and betta are offered by their makers as estimators with variance estimates; Schloss 2024b found breakaway intervals mostly too wide to be useful.
  conf: not stated · class: not stated · holds: makers' claims (abstracts) and Schloss's null models · src: willisEstimatingDiversityFrequency2015 (AB; makers' claims), willisImprovedDetectionChanges2017 (AB; makers' claims), schlossRarefactionCurrentlyBest2024 · trail: MB-01 §5.2, §answers · from: MB-01:B-0281, MB-01:B-0282, MB-01:A-237
- **rarefying.13** Studies disagree on whether rarefying harms differential-abundance tests: rarefied counts and proportions gave high false-positive rates with DESeq2 and edgeR near zero (McMurdie and Holmes 2014); rarefying did not raise FDR for most methods and lowered it at about 10x group differences in library size, at a cost in sensitivity (Weiss 2017).
  conf: cont (note: "Studies disagree") · class: model (note: "Simulation results flip with design choices") · holds: simulations; results depend on data-generating assumptions · src: mcmurdieWasteNotWant2014, weissNormalizationMicrobialDifferential2017 · trail: MB-01 §5.4, §answers · from: MB-01:B-0299, MB-01:B-0300, MB-01:B-0301, MB-01:B-0302, MB-01:A-254, MB-01:A-255, MB-01:A-284
- **rarefying.14** Rarefying followed by permutation controls type I error; the sensitivity loss is negligible when overdispersion is high, and is summarised by a rarefaction efficiency index.
  conf: single (marker) · class: model (marker) · holds: simulations · src: hongRarefyNotRarefy2022 (FT; model; single) · trail: MB-01 §5.4, §answers · from: MB-01:I-0127, MB-01:A-256
- **rarefying.15** With a tenfold depth difference, tests on proportions had severe type I inflation, which rarefying controlled; no method was "simultaneously robust, powerful, and flexible".
  conf: repl (marker) · class: model (marker) · holds: simulations · src: yangComprehensiveEvaluationMicrobial2022 (FT; model; repl) · trail: MB-01 §5.4, §answers · from: MB-01:I-0128, MB-01:A-257
- **rarefying.16** Rarefying is contested: McMurdie and Holmes 2014 against Schloss 2024a and 2024b, Weiss 2017 and Hong 2022 (partial), with Willis 2019 opposing it for richness; beta-diversity results are contested and simulation-based, and simulation results flip with design choices, as Weiss 2017 and Schloss 2024a both say.
  conf: cont (note: "contested") · class: model (note: "simulation-based") · holds: simulations · src: mcmurdieWasteNotWant2014, schlossWasteNotWant2024, schlossRarefactionCurrentlyBest2024, weissNormalizationMicrobialDifferential2017, hongRarefyNotRarefy2022, willisRarefactionAlphaDiversity2019 · trail: MB-01 §answers, §6. Where · from: MB-01:A-280, MB-01:A-276, MB-01:A-284, MB-01:B-0340, MB-01:B-0341
- **rarefying.17** That simulations disagree because they build different data-generating processes into the truth is partly supported (Weiss 2017, Hong 2022 and Schloss 2024a each say results depend on data-generating assumptions) and is the review's own causal diagnosis.
  conf: not stated · class: reading (critic: MB-01:C-142) · holds: the review's overview · src: weissNormalizationMicrobialDifferential2017, hongRarefyNotRarefy2022, schlossWasteNotWant2024 · trail: MB-01 §1. Overview, §Adversarial · from: MB-01:B-0042, MB-01:C-142, MB-01:B-0041

### coverage-standardisation: coverage-based standardisation
needs: alpha-diversity, rarefying
- **coverage-standardisation.1** Chao and Jost argue that standardising by sample completeness rather than size gives less biased richness ratios.
  conf: not stated · class: model (marker) · holds: ecology, labelled INDIRECT · src: chaoCoveragebasedRarefactionExtrapolation2012 (FT; model; INDIRECT) · trail: MB-01 §5.1, §answers · from: MB-01:I-0107, MB-01:A-234, MB-01:B-0323
- **coverage-standardisation.2** A 2026 test on terrestrial inventories finds that coverage-based rarefaction "does not respond predictably" to richness.
  conf: single (marker) · class: model (marker) · holds: terrestrial (non-microbial) inventories; abstract only; labelled INDIRECT · src: alroyCoveragebasedRarefactionFails2026 (AB; model; single; INDIRECT) · trail: MB-01 §5.1, §answers · from: MB-01:I-0109, MB-01:A-235
- **coverage-standardisation.3** In Schloss 2024b's null models, coverage-based iNEXT estimates were among those that "showed a strong correlation between richness and the number of sequences"; the text exempts "rarefaction and possibly the size-based iNEXT estimates". This is the only microbial amplicon test of coverage-based standardisation found; beyond it the evidence is non-microbial.
  conf: single (critic: MB-01:C-049) · class: model (note: "null models") · holds: Schloss's null models; the synthesis agent's re-reading of the full text, verified by the critic · src: schlossRarefactionCurrentlyBest2024 (FT, re-opened) · trail: MB-01 §5.2, §answers, §critic, §Search record · from: MB-01:B-0277, MB-01:B-0278, MB-01:B-0279, MB-01:A-236, MB-01:B-0375, MB-01:C-049, MB-01:C-050, MB-01:A-313
- **coverage-standardisation.4** Coverage-based standardisation is in conflict: Chao and Jost 2012 against Alroy 2026 (both non-microbial) and the microbial null model in Schloss 2024b; an independent microbial amplicon benchmark of coverage-based standardisation with known truth was not found.
  conf: not stated · class: search (note: "An independent microbial benchmark of coverage-based standardisation (statistics angle)") · holds: statistics angle · src: chaoCoveragebasedRarefactionExtrapolation2012, alroyCoveragebasedRarefactionFails2026, schlossRarefactionCurrentlyBest2024 · trail: MB-01 §answers, §Search record · from: MB-01:A-282, MB-01:B-0384, MB-01:A-285

### richness-estimators: richness estimators and extrapolation
needs: alpha-diversity
- **richness-estimators.1** Sample data carry no information on the rare tail: Chao's estimator ranked in silico communities wrongly (a community with 20 times fewer species was estimated to have 10 times more), and bounds for Hill numbers of order 2 and above nearly coincide; the authors recommend Shannon and Simpson over richness.
  conf: repl (marker) · class: model (marker) · holds: in silico communities · src: haegemanRobustEstimationMicrobial2013 (FT; model; repl) · trail: MB-01 §5.2, §answers · from: MB-01:B-0283, MB-01:B-0284, MB-01:B-0285, MB-01:I-0115, MB-01:B-0286, MB-01:A-238, MB-01:A-242, MB-01:B-0328
- **richness-estimators.2** Hill-number extrapolation is reliable only to about 2 to 3 times the reference sample size for richness.
  conf: not stated · class: model (marker) · holds: labelled INDIRECT · src: chaoRarefactionExtrapolationHill2014 (FT; model; INDIRECT) · trail: MB-01 §5.1, §answers · from: MB-01:I-0108, MB-01:A-239
- **richness-estimators.3** Chao1 and ACE are invalid on ASV tables from algorithms that drop singletons, as DADA2 does by default.
  conf: single (marker) · class: assert (marker) · holds: Deng 2024 · src: dengNonparametricRichnessEstimators2024 (FT; assert; single) · trail: MB-01 §5.2, §answers · from: MB-01:I-0116, MB-01:A-240
- **richness-estimators.4** Spurious OTUs severely inflated Chao1, and removing them severely underestimated Chao1 in uneven communities, while abundance-weighted metrics were little affected.
  conf: not stated · class: not stated · holds: Pinto and Raskin 2012 · src: pintoPCRBiasesDistort2012 · trail: MB-01 §5.2, §answers, §2. Steps · from: MB-01:B-0287, MB-01:A-079, MB-01:A-080, MB-01:A-241, MB-01:B-0071
- **richness-estimators.5** An abundance filter makes ACE and Chao1 inapplicable.
  conf: not stated · class: not stated · holds: Bokulich 2013 · src: bokulichQualityfilteringVastlyImproves2013 · trail: MB-01 §5.2 · from: MB-01:B-0288
- **richness-estimators.6** A singleton-replacement estimator for error-inflated data has been proposed.
  conf: single (marker) · class: model (marker) · holds: abstract only · src: chiuEstimatingComparingMicrobial2016 (AB; model; single) · trail: MB-01 §5.2, §answers · from: MB-01:I-0117, MB-01:A-241

### compositional-analysis: compositional (log-ratio) approaches
needs: read-depth
- **compositional-analysis.1** A review argues that 16S data are compositions "at all stages" and should be analysed with log-ratios.
  conf: cont (marker) · class: assert (marker) · holds: a review; abstract only · src: gloorMicrobiomeDatasetsCompositional2017 (AB; assert; cont) · trail: MB-01 §5.1 · from: MB-01:I-0110
- **compositional-analysis.2** Aitchison (log-ratio) distances were depth-sensitive under Schloss's null model.
  conf: not stated · class: not stated · holds: Schloss 2024b null models · src: schlossRarefactionCurrentlyBest2024 · trail: MB-01 §answers, §5.6 · from: MB-01:A-251, MB-01:B-0324
- **compositional-analysis.3** Fold changes in taxon ratios are invariant to multiplicative bias, while fold changes in proportions are not and can change sign; the bias-invariance of ratio-based methods rests on McLaren 2019.
  conf: not stated · class: not stated · holds: McLaren 2019 · src: mclarenConsistentCorrectableBias2019 · trail: MB-01 §5.4, §answers · from: MB-01:B-0310, MB-01:A-262, MB-01:A-293
- **compositional-analysis.4** Proportion-based differential-abundance results err when the community's mean efficiency is associated with the condition.
  conf: single (marker) · class: model (marker) · holds: preprint abstract · src: mclarenImplicationsTaxonomicBias2022 (AB; PREPRINT; model; single) · trail: MB-01 §5.4, §answers · from: MB-01:I-0135, MB-01:A-262
- **compositional-analysis.5** Reference frames make differential rankings invariant to load.
  conf: single (marker) · class: meas (marker) · holds: abstract only · src: mortonEstablishingMicrobialComposition2019 (AB; meas; single) · trail: MB-01 §5.4, §answers · from: MB-01:I-0134, MB-01:A-261

### scaling-normalisation: scaling and normalisation methods
needs: read-depth
- **scaling-normalisation.1** Total-count scaling can bias differential-expression estimates in RNA-seq; TMM and DESeq's negative binomial model also come from RNA-seq, and both assume most features are unchanged between conditions.
  conf: not stated · class: not stated · holds: RNA-seq, labelled INDIRECT; abstracts only · src: bullardEvaluationStatisticalMethods2010 (AB; INDIRECT), robinsonScalingNormalizationMethod2010 (AB; INDIRECT), andersDifferentialExpressionAnalysis2010 (AB; INDIRECT), weissNormalizationMicrobialDifferential2017 · trail: MB-01 §5.1, §answers · from: MB-01:B-0265, MB-01:B-0266, MB-01:B-0267, MB-01:A-270
- **scaling-normalisation.2** In shotgun gene-abundance data, TMM and RLE performed best.
  conf: not stated · class: not stated · holds: shotgun, labelled INDIRECT; abstract only · src: pereiraComparisonNormalizationMethods2018 (AB; INDIRECT, shotgun) · trail: MB-01 §5.1 · from: MB-01:B-0268
- **scaling-normalisation.3** Under Schloss's null model, scaling normalisations (TMM, RLE, CSS, VST, SRS, Wrench) did not remove depth effects, while in the Llorens-Rico 2021 simulation RLE and VST came close to quantitative methods for association tests in a dysbiosis scenario.
  conf: not stated · class: not stated · holds: null models and simulated faeces · src: schlossRarefactionCurrentlyBest2024, llorensricoBenchmarkingMicrobiomeTransformations2021 · trail: MB-01 §answers, §5.6 · from: MB-01:A-271, MB-01:A-272, MB-01:B-0329
- **scaling-normalisation.4** Wrench's makers state that library-size scaling and rarefaction cannot correct compositional bias that is uncorrelated with library size, and SRS's makers claim better reproducibility than rarefying.
  conf: not stated · class: not stated · holds: makers' claims; abstracts only · src: kumarAnalysisCorrectionCompositional2018 (AB; makers' claim), beuleImprovedNormalizationSpecies2020 (AB) · trail: MB-01 §5.4 · from: MB-01:B-0308, MB-01:B-0309

### differential-abundance: tests of which taxa differ in abundance
needs: rarefying, compositional-analysis, scaling-normalisation
- **differential-abundance.1** Fourteen differential-abundance methods on 38 datasets gave 0.8% to 40.5% significant ASVs (unfiltered means); ALDEx2 and ANCOM-II were the most consistent, and edgeR and LEfSe produced many false positives on random splits.
  conf: single (marker) · class: meas (marker) · holds: 38 real datasets · src: nearingMicrobiomeDifferentialAbundance2022 (FT; meas; single) · trail: MB-01 §5.4, §answers · from: MB-01:B-0304, MB-01:I-0129, MB-01:A-253, MB-01:A-259, MB-01:A-264
- **differential-abundance.2** Excess false discoveries were widespread across methods.
  conf: repl (marker) · class: model (marker) · holds: abstract only · src: hawinkelBrokenPromiseMicrobiome2019 (AB; model; repl) · trail: MB-01 §5.4, §answers · from: MB-01:I-0130, MB-01:A-265
- **differential-abundance.3** Methods with the highest false-positive rates had the most power.
  conf: not stated · class: not stated · holds: Thorsen 2016 · src: thorsenLargescaleBenchmarkingReveals2016 · trail: MB-01 §5.4 · from: MB-01:B-0305
- **differential-abundance.4** Microbiome-specific methods did not beat RNA-seq methods.
  conf: single (marker) · class: meas (marker) · holds: abstract only · src: calgaroAssessmentStatisticalMethods2020 (AB; meas; single) · trail: MB-01 §5.4 · from: MB-01:I-0131
- **differential-abundance.5** In implanted-signal benchmarks, only linear models, Wilcoxon, t-test, limma and fastANCOM controlled FDR at relatively high sensitivity; fitZig reached an observed FDR of 80%, and ANCOM and ANCOM-BC controlled FDR only at 200 or more samples per group.
  conf: repl (marker) · class: model (marker) · holds: implanted-signal benchmarks · src: wirbelRealisticBenchmarkDifferential2024 (FT; model; repl) · trail: MB-01 §5.4, §7. Bounds, §answers · from: MB-01:I-0132, MB-01:A-260, MB-01:A-263, MB-01:B-0365, MB-01:B-0366
- **differential-abundance.6** Elementary methods on relative abundances (Wilcoxon, linear models) were the most replicable across 53 studies.
  conf: single (marker) · class: meas (marker) · holds: abstract only · src: peltoElementaryMethodsProvide2025 (AB; meas; single) · trail: MB-01 §5.4, §answers · from: MB-01:I-0133, MB-01:A-263
- **differential-abundance.7** ANCOM had the best FDR control in Weiss 2017, while DESeq2's FDR rose with more samples or uneven libraries.
  conf: not stated · class: not stated · holds: Weiss 2017 · src: weissNormalizationMicrobialDifferential2017 · trail: MB-01 §5.4, §answers · from: MB-01:B-0303, MB-01:A-258
- **differential-abundance.8** Makers claim FDR control for ANCOM-BC and ANCOM; independent benchmarks disagree in part, with ANCOM-BC showing type I inflation in some settings (Yang and Chen 2022) and controlling FDR only at 200 or more samples per group (Wirbel 2024).
  conf: not stated · class: not stated · holds: makers' claims (abstracts) against independent benchmarks · src: linAnalysisCompositionsMicrobiomes2020 (AB; makers' claims), mandalAnalysisCompositionMicrobiomes2015 (AB; makers' claims), yangComprehensiveEvaluationMicrobial2022, wirbelRealisticBenchmarkDifferential2024 · trail: MB-01 §5.4, §answers · from: MB-01:B-0306, MB-01:B-0307, MB-01:A-260, MB-01:A-283
- **differential-abundance.9** Differential-abundance methods disagree widely and FDR failures are common, which is robustly shown (Nearing 2022; Hawinkel 2019; Yang and Chen 2022; Wirbel 2024); which method is best is contested.
  conf: cont (note: "Which method is best is contested") · class: not stated · holds: the four benchmarks named · src: nearingMicrobiomeDifferentialAbundance2022, hawinkelBrokenPromiseMicrobiome2019, yangComprehensiveEvaluationMicrobial2022, wirbelRealisticBenchmarkDifferential2024 · trail: MB-01 §answers, §8. Answers · from: MB-01:A-277, MB-01:A-278, MB-01:A-311

### absolute-quantification: absolute quantification of total load (qPCR, flow cytometry, dPCR, spike-ins)
needs: microbial-load, workflow-bias
- **absolute-quantification.1** Load measurements change conclusions drawn from relative data: qPCR, flow cytometry, dPCR and spike-ins can reverse relative-abundance conclusions; this is replicated.
  conf: repl (note: "replicated that it changes conclusions") · class: not stated · holds: the four studies named · src: vandeputteQuantitativeMicrobiomeProfiling2017, propsAbsoluteQuantificationMicrobial2016, barlowQuantitativeSequencingFramework2020, tkaczAbsoluteQuantitationMicrobiota2018 · trail: MB-01 §5.5, §answers, §critic · from: MB-01:B-0311, MB-01:A-266, MB-01:A-279, MB-01:C-042, MB-01:B-0322
- **absolute-quantification.2** Flow-cytometry quantitative profiling showed the Bacteroides-Prevotella trade-off in relative data to be an artefact, and load drove Crohn's-associated differences.
  conf: not stated · class: not stated · holds: abstract only · src: vandeputteQuantitativeMicrobiomeProfiling2017 (AB) · trail: MB-01 §5.5 · from: MB-01:B-0312
- **absolute-quantification.3** Relative enrichment did not imply absolute outgrowth.
  conf: not stated · class: not stated · holds: engineered freshwater; abstract only · src: propsAbsoluteQuantificationMicrobial2016 (AB; engineered freshwater) · trail: MB-01 §5.5 · from: MB-01:B-0313
- **absolute-quantification.4** Absolute abundance could hold steady or rise while relative abundance fell.
  conf: not stated · class: not stated · holds: soil · src: tkaczAbsoluteQuantitationMicrobiota2018 (FT; soil) · trail: MB-01 §5.5 · from: MB-01:B-0314
- **absolute-quantification.5** Spike-in bacteria added before extraction recovered ratios of absolute abundances across mouse faecal dilutions, although the three spike-in species gave different read yields.
  conf: repl (marker) · class: meas (marker) · holds: mouse faecal dilutions · src: stammlerAdjustingMicrobiomeProfiles2016 (FT; meas; repl) · trail: MB-01 §5.5 · from: MB-01:I-0136, MB-01:B-0315
- **absolute-quantification.6** dPCR anchoring gave about 2x extraction accuracy above 8.3 x 10^4 input copies, and absolute but not relative analysis revealed diet effects.
  conf: single (marker) · class: meas (marker) · holds: Barlow 2020 · src: barlowQuantitativeSequencingFramework2020 (FT; meas; single) · trail: MB-01 §5.5 · from: MB-01:I-0137
- **absolute-quantification.7** Soil internal standards tracked PLFA and respiration biomass better than those two measures tracked each other.
  conf: single (marker) · class: meas (marker) · holds: soil; abstract only · src: smetsMethodSimultaneousMeasurement2016 (AB; meas; single) · trail: MB-01 §5.5 · from: MB-01:I-0138
- **absolute-quantification.8** Total 16S qPCR multiplied by relative abundance correlated near-perfectly with taxon-specific qPCR, a comparison of methods that share an upstream (qPCR versus qPCR-anchored sequencing), on four taxa.
  conf: single (marker) · class: meas (marker) · holds: four taxa; shared upstream · src: jianQuantitativePCRProvides2020 (FT; meas; single) · trail: MB-01 §5.5, §Adversarial · from: MB-01:I-0139, MB-01:C-106, MB-01:C-127
- **absolute-quantification.9** In simulation, experimental quantitative profiling outperformed computational transformations for associations.
  conf: not stated · class: not stated · holds: simulation (Llorens-Rico 2021) · src: llorensricoBenchmarkingMicrobiomeTransformations2021 · trail: MB-01 §5.5 · from: MB-01:B-0316
- **absolute-quantification.10** Absolute quantification does not correct taxon-specific extraction and PCR bias.
  conf: not stated · class: not stated · holds: McLaren 2019 and Bonk 2018 · src: mclarenConsistentCorrectableBias2019, bonkPCRbasedQuantificationTaxaspecific2018 · trail: MB-01 §5.5, §answers, §8. Answers, §critic · from: MB-01:B-0317, MB-01:B-0318, MB-01:A-267, MB-01:A-312, MB-01:C-042
- **absolute-quantification.11** qPCR and sequencing both count extracellular DNA, unlike cell counts.
  conf: not stated · class: not stated · holds: Jian 2020 · src: jianQuantitativePCRProvides2020 · trail: MB-01 §5.5 · from: MB-01:B-0319
- **absolute-quantification.12** qPCR and flow cytometry agreed on a whole-cell mock (|r| = 0.967) but gave "highly divergent" profiles for faeces, where qPCR against flow-cytometry enumeration correlated at Pearson r = -0.50; ddPCR correlated strongly with qPCR, which the authors used to rule out qPCR imprecision as the cause of the divergence. The divergence rests on this one study.
  conf: single (marker) · class: meas (marker) · holds: one whole-cell mock and faeces · src: galazzoHowCountOur2020 (FT; meas; single) · trail: MB-01 §5.5, §answers, §critic, §Adversarial · from: MB-01:I-0140, MB-01:A-267, MB-01:A-292, MB-01:C-045, MB-01:C-057, MB-01:C-071
- **absolute-quantification.13** Synthetic spike-ins had differing detection efficiencies and small departures from linearity, and correlations were weaker with Taq than with KOD polymerase.
  conf: repl (marker) · class: meas (marker) · holds: synthetic 16S spike-ins · src: tourlousseSyntheticSpikeinStandards2016 (FT; meas; repl) · trail: MB-01 §5.5 · from: MB-01:I-0141
- **absolute-quantification.14** Seawater internal standards agreed with flow cytometry at r2 = 0.19 until corrections for copy number and particle association (with four outliers removed) raised it to 0.61; the authors conclude that the method "provided results consistent with ... total bacterial counts by flow cytometry" and "is quantitative".
  conf: single (marker) · class: meas (marker) · holds: seawater; the r2 figures need the body and could not be confirmed · limit: access (critic: MB-01:C-076) · src: linTowardsQuantitativeMicrobiome2019 (FT; meas; single) · trail: MB-01 §5.5, §7. Bounds, §answers, §critic, §Adversarial · from: MB-01:I-0142, MB-01:A-269, MB-01:B-0364, MB-01:C-046, MB-01:C-047, MB-01:C-048, MB-01:C-076, MB-01:C-081, MB-01:C-127
- **absolute-quantification.15** A review states that internal standards often underperform or fail.
  conf: not stated · class: assert (marker) · holds: a review; abstract only · src: harrisonQuestAbsoluteAbundance2020 (AB; assert) · trail: MB-01 §5.5 · from: MB-01:I-0143
- **absolute-quantification.16** Agreement between absolute-quantification methods is weak and in conflict (Jian 2020 against Galazzo 2020).
  conf: not stated · class: not stated · holds: listed among the review's conflicts · src: jianQuantitativePCRProvides2020, galazzoHowCountOur2020 · trail: MB-01 §answers, §6. Where · from: MB-01:A-279, MB-01:A-283, MB-01:B-0343 · rating: "weak on the agreement between quantification methods"
- **absolute-quantification.17** No approach to comparing samples with unequal depth or load is shown to correct depth, load and taxon-specific bias together; benchmarks that build taxon-specific bias and load differences into the simulated truth together are absent apart from Llorens-Rico 2021 (simulated faeces without taxon bias), and no benchmark used measured absolute loads in soil or water as truth or tested richness corrections against known-richness mocks across depths.
  conf: not stated · class: search (note: "Not found") · holds: statistics angle (Europe PMC, Crossref, publisher HTML, author PDFs, web search); lab and bioinformatics angles for spike-ins · src: llorensricoBenchmarkingMicrobiomeTransformations2021 · trail: MB-01 §answers, §8. Answers, §critic · from: MB-01:A-230, MB-01:A-285, MB-01:A-286, MB-01:A-309, MB-01:C-051

### rare-biosphere: within-sample abundance terms (rare, abundant, conditionally rare) and rarity frameworks
needs: abundance-distribution
- **rare-biosphere.1** The "rare biosphere" entered usage with deep-sea tag sequencing, which found thousands of low-abundance populations alongside a few dominants; reviews describe a few dominant taxa and many rare ones without fixing a threshold.
  conf: not stated · class: not stated · holds: deep sea; abstracts only · src: soginMicrobialDiversityDeep2006 (AB), pedrosalioRareBacterialBiosphere2012 (AB), lynchEcologyExplorationRare2015 (AB), pascoalMicrobialRareBiosphere2021 (AB) · trail: MB-02 §D2.1 · from: MB-02:B-0156, MB-02:B-0157
- **rare-biosphere.2** Three families of definition are in use and are not interchangeable: within-sample relative-abundance thresholds (0.1% most common for rare), occupancy or prevalence across samples (core, mostly occurrence-only) and regional or global (pooled) classes; usage is heterogeneous and often unstated, from two systematic surveys.
  conf: not stated · class: not stated · holds: two systematic literature surveys (Pascoal 2025 for rare-biosphere usage, Neu 2021 for core usage) plus reviews; removing either removes the quantitative usage picture for that term · src: pascoalDefinitionMicrobialRare2025 (FT), neuDefiningQuantifyingCore2021 (FT) · trail: MB-02 §answers, §critic · from: MB-02:A-060, MB-02:A-144, MB-02:A-145, MB-02:A-070, MB-02:A-079, MB-02:C-028, MB-02:C-029, MB-02:C-030 · rating: "Strong on the fact of heterogeneity"
- **rare-biosphere.3** Within-sample thresholds: rare is most often below 0.1% of reads per sample, sometimes below 0.01% or 0.001%, and abundant is usually above 1% (Lynch and Neufeld 2015, Galand 2009, Dai 2016); Jia et al. 2022 uses a single rare/common cutoff and does not support "abundant above 1%".
  conf: not stated · class: not stated · holds: the studies cited for these thresholds · src: lynchEcologyExplorationRare2015 (AB), galandEcologyRareMicrobial2009 (FT), daiIdentifyingKeyTaxonomic2016 (AB), jiaUnravellingInterplayEcological2022 (FT) · trail: MB-02 §answers, §critic · from: MB-02:A-061, MB-02:C-031, MB-02:C-032, MB-02:C-065
- **rare-biosphere.4** Galand et al. 2009 set rare below 0.01% and abundant above 1% per sample, calling the 0.01% cutoff "much more severe than the <0.1% criteria proposed earlier" and tying it to a singleton in the smallest library.
  conf: not stated · class: not stated · holds: Arctic Ocean · src: galandEcologyRareMicrobial2009 (FT) · trail: MB-02 §D2.1 · from: MB-02:B-0158, MB-02:B-0159, MB-02:B-0160, MB-02:B-0199
- **rare-biosphere.5** Dai et al. 2016 set rare below 0.1% and abundant above 1%, with six categories combining these thresholds with behaviour across samples: always abundant, conditionally abundant, always rare, conditionally rare, moderate, and conditionally rare or abundant.
  conf: not stated · class: not stated · holds: abstract only · src: daiIdentifyingKeyTaxonomic2016 (AB) · trail: MB-02 §D2.1, §answers · from: MB-02:B-0161, MB-02:B-0162, MB-02:A-063
- **rare-biosphere.6** A survey of 181 rare-biosphere articles from 2006 to 2024 found that about 37% gave no clear method; of those with a method, about 84% used relative abundance thresholds, about 60% of those used a single threshold, and about half used 0.1%, about 70% of them per sample rather than on the pooled dataset.
  conf: not stated · class: not stated · holds: 181 articles; checked by the critic · src: pascoalDefinitionMicrobialRare2025 (FT) · trail: MB-02 §D2.1, §answers, §critic · from: MB-02:B-0163, MB-02:B-0164, MB-02:B-0165, MB-02:B-0166, MB-02:B-0167, MB-02:A-062, MB-02:C-057
- **rare-biosphere.7** Conditionally rare taxa are defined by a bimodal abundance distribution over time (coefficient of bimodality) together with a maximum relative abundance above 1%; across 42 non-soil time series they made up 1.5 to 28% of membership. A three-way split into permanently, transiently and conditionally rare taxa has been applied in soil.
  conf: not stated · class: not stated · holds: 42 non-soil time series (Shade 2014) and soil (Jia 2022) · src: shadeConditionallyRareTaxa2014 (FT, excerpts), jiaUnravellingInterplayEcological2022 (FT) · trail: MB-02 §D2.2, §answers · from: MB-02:B-0179, MB-02:B-0180, MB-02:B-0181, MB-02:B-0182, MB-02:A-063
- **rare-biosphere.8** From general ecology, rarity is classed along local abundance, habitat specificity and geographic range (Rabinowitz 1981), whose concepts the authors of a microbial review say "can be easily transferred to microbial communities"; reviews treat habitat specificity and geographic range as microbial rarity axes alongside local abundance.
  conf: not stated · class: not stated · holds: Rabinowitz known only secondarily via Jousset 2017; the original was not obtained · src: rabinowitzSevenFormsRarity1981 (SEC), joussetWhereLessMay2017 (FT) · trail: MB-02 §D2.4, §D2.3, §answers · from: MB-02:B-0187, MB-02:B-0188, MB-02:B-0189, MB-02:B-0186, MB-02:A-066
- **rare-biosphere.9** In a 21-year estuarine fish record, persistent and abundant "core" species fitted a lognormal while infrequent "occasional" species fitted a log series, and Galand et al. report the same split for rare versus abundant Arctic Ocean prokaryotes.
  conf: not stated · class: not stated · holds: estuarine fish (abstract only) and Arctic Ocean prokaryotes · src: magurranExplainingExcessRare2003 (AB), galandEcologyRareMicrobial2009 (FT) · trail: MB-02 §D2.4, §answers · from: MB-02:B-0190, MB-02:B-0191, MB-02:A-066
- **rare-biosphere.10** No survey was found that tallies definitions within soil studies or separately for bulk soil and rhizosphere; no study compares threshold-based rarity classes between amplicon and metagenome data from the same soil samples; copy-number-corrected thresholds were not found to have been tested.
  conf: not stated · class: search (note: "No survey found that tallies definitions specifically within soil studies") · holds: the Search record gives routes for threshold-sensitivity tests in soil (WebSearch standard and extended, and a Europe PMC query on rare biosphere thresholds); no route is given for the other two · src: none (a statement about what the search found) · trail: MB-02 §answers, §Search record · from: MB-02:A-075, MB-02:A-076, MB-02:A-077, MB-02:B-0300

### global-classes: regional and global distribution terms (dominant, common)
needs: rare-biosphere
- **global-classes.1** In soil, "dominant" has been defined jointly: in the top 10% of phylotypes by share of 16S reads and present in more than half of 237 soils.
  conf: not stated · class: not stated · holds: 237 soils, global · src: delgadobaquerizoGlobalAtlasDominant2018 (FT) · trail: MB-02 §D2.3, §answers · from: MB-02:B-0183, MB-02:A-065
- **global-classes.2** "Common" versus "rare" has also been set by a data-driven minimum cross-entropy threshold on the globally pooled rank-abundance distribution, about 0.019%, with prevalence across samples reported separately; the threshold was robust to using a quarter of the samples.
  conf: not stated · class: not stated · holds: 844 soils; checked by the critic · src: bickelChosenFewVariations2021 (FT) · trail: MB-02 §D2.3, §D3.3, §answers, §critic · from: MB-02:B-0184, MB-02:B-0185, MB-02:B-0272, MB-02:A-065, MB-02:A-111, MB-02:C-057, MB-02:B-0221
- **global-classes.3** Terms are used inconsistently: "dominant" sometimes means abundant within a sample and sometimes abundant and ubiquitous; "common" means high pooled abundance in Bickel and Or 2021 and high occupancy elsewhere.
  conf: not stated · class: not stated · holds: the definitions surveyed · src: delgadobaquerizoGlobalAtlasDominant2018, bickelChosenFewVariations2021 · trail: MB-02 §answers · from: MB-02:A-074

### core-microbiome: occupancy terms (core, prevalence)
needs: abundance-occupancy, rare-biosphere
group: occupancy
- **core-microbiome.1** "Core" is the main occupancy term: it was first framed as the members shared across samples, the overlap of Venn diagrams, with later calls to add persistence and connectivity; Risely distinguishes five kinds of core (common, temporal, ecological, functional, host-adapted) and argues that no one definition captures all.
  conf: not stated · class: not stated · holds: abstracts only · src: shadeBeyondVennDiagram2012 (AB), riselyApplyingCoreMicrobiome2020 (AB) · trail: MB-02 §D2.2 · from: MB-02:B-0168, MB-02:B-0169, MB-02:B-0178
- **core-microbiome.2** A survey of 224 core-microbiome studies found that 75.4% used occurrence only, 4% relative abundance only and 11.6% combined the two, with over 18% not stating a method; occurrence cutoffs ranged from 30% to 100% of samples (100% most common) and, in combined methods, abundance cutoffs from 0.1% to 4.5%.
  conf: not stated · class: not stated · holds: 224 studies; full text read to 100,000 characters · src: neuDefiningQuantifyingCore2021 (FT, first 100,000 characters) · trail: MB-02 §D2.2, §answers · from: MB-02:B-0170, MB-02:B-0171, MB-02:B-0172, MB-02:B-0173, MB-02:B-0174, MB-02:B-0175, MB-02:B-0176, MB-02:A-064, MB-02:A-078
- **core-microbiome.3** Neu et al. report, citing other work, that only two OTUs were shared by all of 24 soil locations and none across 51 wastewater plants.
  conf: not stated · class: not stated · holds: secondary via Neu 2021 · src: neuDefiningQuantifyingCore2021 (SEC) · trail: MB-02 §D2.2 · from: MB-02:B-0177
- **core-microbiome.4** In common bean rhizospheres across four US regions plus a Colombian dataset, 48 bacterial and archaeal taxa were detected in every sample; fitting a neutral model to the abundance-occupancy distribution, 13.7% of bacterial and archaeal taxa deviated from neutral expectation; samples were rarefied to 31,255 reads.
  conf: not stated · class: not stated · holds: common bean rhizosphere; the rhizosphere neutral-deviation figure rests on this study alone; checked by the critic · src: stopnisekPersistentMicrobiomeMembers2021 (FT) · trail: MB-02 §D3.2, §answers, §critic · from: MB-02:B-0257, MB-02:B-0258, MB-02:B-0259, MB-02:B-0260, MB-02:A-106, MB-02:A-125, MB-02:A-152, MB-02:C-054, MB-02:C-057
- **core-microbiome.5** In 4,866 maize rhizosphere samples, seven OTUs were present in all, five of them responsive to host genotype.
  conf: not stated · class: not stated · holds: maize rhizosphere; abstract only · src: waltersLargescaleReplicatedField2018 (AB) · trail: MB-02 §D3.2, §answers · from: MB-02:B-0261, MB-02:A-106
- **core-microbiome.6** Rhizosphere evidence on abundance and occupancy is limited to core-membership studies of two to three crops, and none of these rhizosphere studies reports an abundance-occupancy correlation coefficient in the passages read.
  conf: not stated · class: not stated · holds: bean, maize and an Arabidopsis root dataset; no systematic search was run for every crop rhizosphere core study, and neutral-model fits in soil, numerous single studies, were not pooled · src: stopnisekPersistentMicrobiomeMembers2021, waltersLargescaleReplicatedField2018, custerComparativeAnalysisCore2023 · trail: MB-02 §D3.2, §answers, §critic, §Search record · from: MB-02:B-0263, MB-02:A-117, MB-02:C-055, MB-02:B-0301, MB-02:B-0302, MB-02:B-0010
- **core-microbiome.7** Abundance-occupancy ranking with a neutral-model fit has been proposed to prioritise core members.
  conf: not stated · class: not stated · holds: abstract only · src: shadeAbundanceoccupancyDistributionsPrioritize2019 (AB) · trail: MB-02 §D2.5, §answers · from: MB-02:B-0216, MB-02:A-068

### abundance-occupancy: local abundance against occupancy across soils, and the role of sampling and detection
needs: core-microbiome, global-classes, abundance-distribution, sampling-model, technical-replicates
group: occupancy
- **abundance-occupancy.1** In 88 North and South American soils (about 1,500 reads per soil), the ten most abundant OTUs per sample occurred on average in 28% of soils, against 2% for all OTUs; in 27 tropical forest soils within one hectare the figures were 69% against 8%; total abundance and occupancy were significantly and positively related, with no coefficient given. These figures could not be verified by the critic, and the abstract frames the study across Earth's major habitat types, not soils alone.
  conf: not stated · class: not stated · holds: 88 American soils and 27 tropical forest soils; labelled FT, figures unverified · limit: access (critic: MB-02:C-084) · src: nemergutGlobalPatternsBiogeography2011 (FT) · trail: MB-02 §D3.2, §answers, §critic, §Adversarial · from: MB-02:B-0246, MB-02:B-0247, MB-02:B-0248, MB-02:B-0249, MB-02:A-101, MB-02:C-066, MB-02:C-067, MB-02:C-082, MB-02:C-083, MB-02:C-084, MB-02:C-085
- **abundance-occupancy.2** Nemergut's authors note that abundant taxa may simply be easier to detect, and that undersampling could hide intermediate distributions.
  conf: not stated · class: not stated · holds: the same study · src: nemergutGlobalPatternsBiogeography2011 · trail: MB-02 §D3.2, §answers · from: MB-02:B-0250, MB-02:A-107
- **abundance-occupancy.3** Across 844 global soils, median prevalence was 0.3 for common taxa and 0.001 for rare taxa; this is a class-level contrast, a different measure from Nemergut's taxon-level relationship.
  conf: not stated · class: not stated · holds: 844 soils; checked by the critic · src: bickelChosenFewVariations2021 (FT) · trail: MB-02 §D3.2, §answers, §Adversarial · from: MB-02:B-0251, MB-02:B-0252, MB-02:A-102, MB-02:C-137, MB-02:C-057
- **abundance-occupancy.4** In the two bulk-soil amplicon studies with figures (Bickel and Or 2021; Nemergut 2011), more abundant taxa occupy more soils, but the two are not fully independent (Bickel and Or reanalysed compiled datasets including the Earth Microbiome Project, which plausibly overlaps Nemergut's soils), and both measures are partly built in by construction: "total abundance" summed across samples and "common" defined on the pooled rank-abundance distribution both rise with occupancy. Whether a relationship exists beyond sampling, and how strong it is, is unresolved.
  conf: unclear (critic: MB-02:C-053) · class: not stated · holds: bulk-soil amplicon data; the search behind it reviewed about 25 titles · src: bickelChosenFewVariations2021, nemergutGlobalPatternsBiogeography2011 · trail: MB-02 §critic, §Adversarial, §answers · from: MB-02:C-048, MB-02:C-049, MB-02:C-050, MB-02:C-053, MB-02:C-123, MB-02:C-124, MB-02:C-125, MB-02:C-126, MB-02:A-115, MB-02:A-123
- **abundance-occupancy.5** The global "dominant" list cannot test the abundance-occupancy relationship, because dominance there is defined by abundance and ubiquity together.
  conf: not stated · class: not stated · holds: Delgado-Baquerizo 2018 · src: delgadobaquerizoGlobalAtlasDominant2018 (FT) · trail: MB-02 §D3.2, §answers · from: MB-02:B-0255, MB-02:A-104
- **abundance-occupancy.6** Across about 124,000 taxa in 3.41 km2 of urban park soil, occupancy correlated strongly with environmental range; abundance was not the axis tested.
  conf: not stated · class: not stated · holds: one urban park; abstract only · src: barberanWhyAreMicrobes2014 (AB) · trail: MB-02 §D3.2, §answers, §critic · from: MB-02:B-0253, MB-02:B-0254, MB-02:A-103, MB-02:C-058
- **abundance-occupancy.7** Soil also holds taxa that are abundant at some times or places and rare elsewhere: a salt-marsh chronosequence had 2,197 conditionally rare ASVs alongside 11,838 permanently rare and 8,333 transiently rare ASVs; such conditionally rare taxa are locally abundant but occupy few samples, cutting against a uniform relationship.
  conf: not stated · class: not stated · holds: one soil chronosequence; the ASV counts were checked by the critic · src: jiaUnravellingInterplayEcological2022 (FT), shadeConditionallyRareTaxa2014 · trail: MB-02 §D3.2, §answers, §critic · from: MB-02:B-0256, MB-02:A-105, MB-02:A-120, MB-02:C-057, MB-02:B-0194
- **abundance-occupancy.8** Core assignments in an Arabidopsis root dataset varied 7-fold among methods.
  conf: not stated · class: not stated · holds: Arabidopsis root data, 288 samples · src: custerComparativeAnalysisCore2023 (FT) · trail: MB-02 §D3.2, §answers · from: MB-02:B-0262, MB-02:A-106, MB-02:B-0205
- **abundance-occupancy.9** Low-abundance taxa are often recorded absent when present, because technical replicate soil libraries shared only 17.2% (two replicates) and 8.2% (three) of OTUs: this occupancy conclusion is the reviewer's argument, generalised from one 454-era study at one site whose abstract attributes the low overlap to random sampling but does not draw the occupancy conclusion.
  conf: single (critic: MB-02:C-086) · class: reading (critic: MB-02:C-139) · holds: 454 pyrosequencing, 24 communities from one Oklahoma warming site; abstract only · src: zhouReproducibilityQuantitationAmplicon2011 (AB) · trail: MB-02 §D3.3, §answers, §Adversarial · from: MB-02:B-0264, MB-02:B-0266, MB-02:A-108, MB-02:C-086, MB-02:C-139
- **abundance-occupancy.10** Pyrosequencing errors inflated rare-tail richness; better clustering cut richness by 30 to 60% but did not remove the long tail.
  conf: not stated · class: not stated · holds: 454 pyrosequencing; abstracts only · src: kuninWrinklesRareBiosphere2010 (AB), huseIroningOutWrinkles2010 (AB) · trail: MB-02 §D3.3, §answers · from: MB-02:B-0267, MB-02:B-0268, MB-02:A-110
- **abundance-occupancy.11** A neutral community model with immigration and drift only predicts that abundant taxa occur in more samples, so a positive abundance-occupancy relationship is expected without selection; its use in the bean rhizosphere treats deviations, not the relationship itself, as signal. Detection limits and neutral or sampling models predict a positive relationship without selection.
  conf: not stated · class: model (note: "the model predicts") · holds: neutral model (abstract only); the critic's list combines a single 454-era detection study, Grilli 2020 (non-soil) and Sloan 2006 · src: sloanQuantifyingRolesImmigration2006 (AB), stopnisekPersistentMicrobiomeMembers2021, grilliMacroecologicalLawsDescribe2020 · trail: MB-02 §D3.3, §answers, §critic · from: MB-02:B-0273, MB-02:B-0274, MB-02:B-0275, MB-02:A-112, MB-02:A-153, MB-02:C-051, MB-02:B-0258
- **abundance-occupancy.12** The same positive abundance-occupancy observation is read as ecological signal by some authors and as near-null by others; the reviewer notes this is a difference of interpretation, not of data.
  conf: not stated · class: reading (note: "the reviewer notes this is a difference of interpretation") · holds: neutral-model fits · src: sloanQuantifyingRolesImmigration2006 · trail: MB-02 §answers · from: MB-02:A-119
- **abundance-occupancy.13** In general macroecology, positive intraspecific and interspecific abundance-occupancy relationships are common (general in the British flora and fauna), and multiple explanations have been tested; the sampling-artefact literature (Wright 1991; Holt et al. 2002) was not obtained.
  conf: not stated · class: not stated · holds: British flora and fauna; abstract only · src: gastonAbundanceoccupancyRelationships2000 (AB), wrightCorrelationsIncidenceAbundance1991 (not obtained), holtOccupancyabundanceRelationshipsSpatial2002 (not obtained) · trail: MB-02 §D2.4, §D3.3, §answers · from: MB-02:B-0192, MB-02:B-0279, MB-02:B-0280, MB-02:A-066, MB-02:A-113
- **abundance-occupancy.14** No soil study was found that tests whether the observed bulk-soil abundance-occupancy relationship exceeds what sampling and detection alone would produce, so the share attributable to biology is unknown; none was found from cell counts or metagenomes, none specific to archaea, none comparing bulk soil and rhizosphere within one study, and none that is copy-number- or ploidy-corrected.
  conf: unclear (note: "the share attributable to biology is unknown") · class: search (note: "No soil study was found") · holds: Europe PMC query for abundance-occupancy with soil or rhizosphere and bacteria or archaea (25 hits reviewed by title, mostly core-microbiome applications); Europe PMC query for the neutral community model with bulk soil and rhizosphere · src: none (a statement about what the search found) · trail: MB-02 §D3.3, §answers, §critic, §Search record · from: MB-02:B-0281, MB-02:B-0282, MB-02:A-114, MB-02:A-121, MB-02:A-153, MB-02:C-052, MB-02:B-0299, MB-02:A-116 · rating: "Weak for its interpretation"
- **abundance-occupancy.15** Rarer taxa better predicted soil community structure across 30 datasets (1,998 samples); the study does not report abundance-occupancy and is not used in the review's answers.
  conf: not stated · class: not stated · holds: 30 soil datasets; abstract only · src: ramirezDetectingMacroecologicalPatterns2017 (AB) · trail: MB-02 §Search record · from: MB-02:B-0303, MB-02:B-0304
- **abundance-occupancy.16** The review's positive abundance-occupancy answer is its own reading of Bickel and Or 2021, Nemergut 2011 and general macroecology, not an echo of the brief, which states no expected direction.
  conf: not stated · class: reading (critic: MB-02:C-144) · holds: the brief's directions are open questions · src: bickelChosenFewVariations2021, nemergutGlobalPatternsBiogeography2011, gastonAbundanceoccupancyRelationships2000 · trail: MB-02 §Adversarial · from: MB-02:C-142, MB-02:C-143, MB-02:C-144, MB-02:C-145, MB-02:A-151

### term-sensitivity: whether classifications and conclusions hold across thresholds and definitions
needs: rare-biosphere, core-microbiome
- **term-sensitivity.1** In a soil salt-marsh chronosequence (five stages over 110 years, amplicon ASVs), the rare fraction of reads was 61.6%, 45.7% and 28.4% at cutoffs of 0.2%, 0.1% and 0.05%; as the cutoff tightened, permanently and transiently rare ASVs fell in proportion and conditionally rare ASVs rose, and the relative importance of selection rose, while beta-diversity patterns and the main assembly inference (homogeneous selection for the rare biosphere, variable selection for the common) were reported as similar across cutoffs. This is the only soil test of threshold sensitivity found.
  conf: not stated · class: not stated · holds: one soil chronosequence (Schiermonnikoog); checked by the critic · src: jiaUnravellingInterplayEcological2022 (FT) · trail: MB-02 §D2.5, §answers, §critic · from: MB-02:B-0194, MB-02:B-0195, MB-02:B-0196, MB-02:B-0197, MB-02:B-0198, MB-02:A-067, MB-02:A-080, MB-02:A-084, MB-02:C-037
- **term-sensitivity.2** In Arctic Ocean data, the biogeography of rare taxa persisted at a 0.001% cutoff.
  conf: not stated · class: not stated · holds: Arctic Ocean · src: galandEcologyRareMicrobial2009 (FT) · trail: MB-02 §D2.5, §answers · from: MB-02:B-0199, MB-02:A-067
- **term-sensitivity.3** In coastal sands, ecological patterns were maintained after removing up to 35 to 40% of rare sequences.
  conf: not stated · class: not stated · holds: coastal sands; abstract only · src: gobetMultivariateCutoffLevel2010 (AB) · trail: MB-02 §D2.5, §answers · from: MB-02:B-0200, MB-02:A-067
- **term-sensitivity.4** In marine samples, the 0.1% per-sample rule gave more rare than abundant ASVs with V4V5 amplicons and the reverse with full-length 16S, and threshold-based classes behaved differently across OTUs, ASVs and metagenomic OTUs, while the unsupervised method (ulrb) gave the same pattern across these.
  conf: not stated · class: not stated · holds: marine samples; checked by the critic · src: pascoalDefinitionMicrobialRare2025 (FT) · trail: MB-02 §D2.5, §answers, §critic · from: MB-02:B-0201, MB-02:B-0202, MB-02:B-0203, MB-02:A-067, MB-02:C-057
- **term-sensitivity.5** Four core-microbiome methods compared on human faecal (319 samples) and Arabidopsis root (288 samples) data assigned 1.2% to 9.4% of taxa as core (nearly 10-fold), and 165 to 176 taxa were agreed by all four methods, which is 13 to 16% of core assignments; the review's "about 1% of taxa" is its own derivation.
  conf: not stated · class: deriv (critic: MB-02:C-081) · holds: human faeces and Arabidopsis roots; full text read to 100,000 characters; checked by the critic (1.21 to 9.42%) · src: custerComparativeAnalysisCore2023 (FT, first 100,000 characters) · trail: MB-02 §D2.5, §answers, §critic, §Adversarial · from: MB-02:B-0204, MB-02:B-0205, MB-02:B-0206, MB-02:A-067, MB-02:C-033, MB-02:C-034, MB-02:C-081, MB-02:C-057, MB-02:A-078
- **term-sensitivity.6** In the human data of the core-method comparison, the review reports that a temporal effect significant in the full dataset was not significant in core-based analyses (a changed PERMANOVA conclusion); Custer's text is internally inconsistent on whether core analyses gained or lost the temporal effect.
  conf: unclear (critic: MB-02:C-035) · class: not stated · holds: human faecal data · src: custerComparativeAnalysisCore2023 · trail: MB-02 §D2.5, §critic · from: MB-02:B-0207, MB-02:A-067, MB-02:C-035
- **term-sensitivity.7** Occupancy-based core methods were most accurate in simulations; this rests on one simulation study.
  conf: single (critic: MB-02:C-092) · class: model (note: "in simulations") · holds: one simulation study · src: custerComparativeAnalysisCore2023 · trail: MB-02 §D2.5, §Adversarial · from: MB-02:B-0208, MB-02:C-092
- **term-sensitivity.8** In sponges, core definitions changed alpha and beta diversity in some cases but not conclusions on host specificity, environmental quality or networks; the authors call the approach "surprisingly robust".
  conf: not stated · class: not stated · holds: sponges; abstract only · src: astudillogarciaEvaluatingCoreMicrobiota2017 (AB) · trail: MB-02 §D2.5, §answers · from: MB-02:B-0209, MB-02:B-0210, MB-02:A-067
- **term-sensitivity.9** In the human gut, core size depended mostly on analysis depth and required prevalence.
  conf: not stated · class: not stated · holds: human gut; abstract only · src: salonenAdultIntestinalCore2012 (AB) · trail: MB-02 §D2.5, §answers · from: MB-02:B-0211, MB-02:A-067
- **term-sensitivity.10** In Loess Plateau soils, two primer pairs gave different diversity responses to land use, so rare and abundant classes depend on the primer, not only the cutoff.
  conf: not stated · class: not stated · holds: Loess Plateau soils; abstract only · src: zengIdentifyingBiogeographicPatterns2021 (AB) · trail: MB-02 §D2.5 · from: MB-02:B-0212
- **term-sensitivity.11** Tests of threshold sensitivity point both ways and are each single-system: some report conclusions that hold across thresholds or definitions (Jia 2022, Galand 2009, Gobet 2010, Astudillo-Garcia 2017) while others report classifications or conclusions that change (Pascoal 2025, Custer 2023, Salonen 2012); these are not strictly contradictory because they test different outputs (membership counts versus beta-diversity or assembly inferences).
  conf: not stated · class: not stated · holds: each test in one system · src: jiaUnravellingInterplayEcological2022, galandEcologyRareMicrobial2009, gobetMultivariateCutoffLevel2010, astudillogarciaEvaluatingCoreMicrobiota2017, pascoalDefinitionMicrobialRare2025, custerComparativeAnalysisCore2023, salonenAdultIntestinalCore2012 · trail: MB-02 §answers, §critic · from: MB-02:A-071, MB-02:A-072, MB-02:A-073, MB-02:A-146, MB-02:C-036 · rating: "Moderate on threshold sensitivity"
- **term-sensitivity.12** Proposed standards include unsupervised classification (ulrb), multivariate cutoff analysis (also recommended for rare-biosphere assembly work), abundance-occupancy ranking with neutral-model deviations for cores, and explicit reporting with explicit spatial and temporal scale of the core, deep sequencing and no rarefying when quantifying the core; no proposed standard was found to be widely adopted.
  conf: not stated · class: not stated · holds: proposals in reviews and methods papers · src: pascoalDefinitionMicrobialRare2025, gobetMultivariateCutoffLevel2010, jiaCommunityAssemblyProcesses2018 (AB), shadeAbundanceoccupancyDistributionsPrioritize2019, neuDefiningQuantifyingCore2021 · trail: MB-02 §D2.5, §answers · from: MB-02:B-0213, MB-02:B-0214, MB-02:B-0215, MB-02:B-0217, MB-02:B-0218, MB-02:A-068, MB-02:A-069, MB-02:A-147

## Do not say
- **dns.1** "No source found on the effect of water sampling choices (volume, filter pore size) or host tissue sampling."
  why: on the review's own Search record no angle searched these choices; they are unsearched, not "not found" · instead: sampling-storage.7 · trail: MB-01 §critic · from: MB-01:C-006, MB-01:C-007, MB-01:C-008
- **dns.2** "Departures occur at every step."
  why: field sampling for water and host tissue was not searched, and several choices showed no detectable effect; departures were measured at most steps examined · instead: workflow-bias.2 · trail: MB-01 §critic, §Adversarial · from: MB-01:C-062, MB-01:C-147, MB-01:C-148, MB-01:C-149, MB-01:A-296
- **dns.3** "Extraction is the largest step for relative-abundance error, then PCR, then sequencing" as a field-wide ordering, rated strong and backed by "many independent mock studies".
  why: one 7-taxon vaginal dataset (Brooks 2015 reanalysed by McLaren 2019); contested by Fouhy 2016 and qualified by MBQC; the review's own single-source sensitivity says the ordering rests on McLaren and Brooks · instead: workflow-bias.4 · trail: MB-01 §critic, §Adversarial · from: MB-01:C-015, MB-01:C-016, MB-01:C-017, MB-01:C-061, MB-01:C-083, MB-01:A-111, MB-01:A-112
- **dns.4** "The largest measured distortions in relative abundance arise from taxon-specific efficiencies at DNA extraction and PCR" as a property of the field.
  why: rests on one 7-taxon dataset, with Albertsen 2015 as partial support; contradicted by Fouhy 2016 and qualified by MBQC · instead: workflow-bias.4 · trail: MB-01 §Adversarial · from: MB-01:C-084, MB-01:B-0035
- **dns.5** "Calibration cut mean Bray-Curtis error from 0.35 to 0.08 in a shotgun dataset."
  why: the full text places this in the Brooks 2015 16S cell mixtures; the Costea shotgun calibration is reported only qualitatively · instead: bias-consistency.2 · trail: MB-01 §critic, §Adversarial · from: MB-01:C-021, MB-01:C-055, MB-01:C-066, MB-01:B-0185, MB-01:C-068
- **dns.6** "The original 515F/806R V4 primers under-represented SAR11 by about 4 to 10-fold in field samples but only about 2-fold in mocks."
  why: the abstract gives these figures for 515F-Y/806R, not the original 515F-C/806R · instead: primers.4 · trail: MB-01 §critic, §Adversarial · from: MB-01:C-056, MB-01:C-070, MB-01:A-052
- **dns.7** "Mock bias did not transfer to the field" as a general result.
  why: rests on one abstract-only study, for one primer pair (515F-Y/806R) and one taxon (SAR11) · instead: primers.4 · trail: MB-01 §Adversarial · from: MB-01:C-092, MB-01:B-0059
- **dns.8** "ddPCR versus flow cytometry correlated at only r = 0.50" (Galazzo 2020).
  why: the full text reports qPCR versus flow-cytometry enumeration on faeces (Pearson r = -0.50); ddPCR correlated strongly with qPCR · instead: absolute-quantification.12 · trail: MB-01 §critic, §Adversarial · from: MB-01:C-045, MB-01:C-057, MB-01:C-071, MB-01:I-0140
- **dns.9** "Unfiltered OTU tables were 50 to 80% spurious taxa."
  why: the source says after OTU clustering and singleton removal · instead: denoising-clustering.7 · trail: MB-01 §critic, §Adversarial · from: MB-01:C-058, MB-01:C-072, MB-01:A-095, MB-01:B-0075
- **dns.10** "Mean Jaccard 0.80" for PCR replicates of negative extraction controls.
  why: the source reports a mean Jaccard distance of 0.80; without "distance" the figure reads as high similarity · instead: technical-variation.2 · trail: MB-01 §critic, §Adversarial · from: MB-01:C-059, MB-01:C-082
- **dns.11** "30% of 16S amplicon papers report a negative control and 10% a positive control."
  why: Hornung 2019's rates cover all high-throughput community sequencing types in two journals, not 16S only, and are a single source · instead: contamination.8 · trail: MB-01 §critic, §Adversarial · from: MB-01:C-004, MB-01:C-005, MB-01:C-132
- **dns.12** "Multinomial or Poisson sampling explains much replicate disagreement in taxa detected", rated moderate "from several soil studies".
  why: one 454 dataset of 24 Oklahoma soils and one laboratory; Wen 2017 does not fit the model, and its contrary depth plateau is missing · instead: sampling-model.2, sampling-model.3 · trail: MB-01 §critic, §Adversarial · from: MB-01:C-063, MB-01:C-086, MB-01:C-135, MB-01:A-214, MB-01:A-306
- **dns.13** "Agreement in relative abundance rises with depth, roughly as a square root" as a general result.
  why: rests on one caecal extract with four technical replicates (Barlow 2020) · instead: sampling-model.5 · trail: MB-01 §Adversarial · from: MB-01:C-085, MB-01:A-307
- **dns.14** "Relative abundance is robust to the pipeline; counts of taxa are not."
  why: generalises from Nearing 2018 (with Marizzoni 2020); Nearing 2018 itself reports that all pipelines markedly differed from expected composition on the Zymo mock, and Straub 2020 reports pipeline-dependent interpretations · instead: denoising-clustering.2, denoising-clustering.4 · trail: MB-01 §Adversarial · from: MB-01:C-087, MB-01:I-0052
- **dns.15** "Library preparation and primers are the largest drivers of error profile" without a single-source flag.
  why: rests on Schirmer 2015 alone · instead: library-prep.2 · trail: MB-01 §Adversarial · from: MB-01:C-088
- **dns.16** "V4 genus accuracy is about 50% at 97% identity and reference databases carry 10 to 17% annotation error" without the single-source qualifier.
  why: rests on Edgar 2018b and 2018c, from one author who also develops competing classifiers; flagged single in the text but used in the D2 answer without that qualifier · instead: taxonomic-assignment.2, taxonomic-assignment.6 · trail: MB-01 §Adversarial · from: MB-01:C-089
- **dns.17** "Chimera formation is reproducible across amplifications" as an established consistency.
  why: rests on Haas 2011 (Sanger and 454) alone · instead: chimeras.2 · trail: MB-01 §Adversarial · from: MB-01:C-090
- **dns.18** "Fast-responding soil isolates average 5.5 copies against 1.4" as a general result.
  why: rests on one abstract-only study (Klappenbach 2000) · instead: copy-number.21 · trail: MB-01 §Adversarial · from: MB-01:C-091
- **dns.19** "Willis 2019 is an assertion", and rarefying for richness is "contested by an assertion".
  why: the paper gives statistical argument plus a worked simulated example; calling it an assertion against Schloss's modelled simulations understates the evidence against rarefying for richness · instead: rarefying.11 · trail: MB-01 §critic, §Adversarial · from: MB-01:C-043, MB-01:C-044, MB-01:C-124, MB-01:A-275
- **dns.20** "Spike-in totals agreed poorly with flow cytometry (r2 0.19)" (Lin 2019) as a failure without the authors' conclusion.
  why: the authors conclude the internal-standard method is quantitative and consistent with flow cytometry; the review omits this (Common rule 6), and the r2 figure could not be verified · instead: absolute-quantification.14 · trail: MB-01 §critic, §Adversarial · from: MB-01:C-046, MB-01:C-047, MB-01:C-081, MB-01:C-127, MB-01:C-048
- **dns.21** "The difference in load is the likely reason" for the pooled-versus-single PCR contrast, as a finding.
  why: the reviewer's own reconciliation, untested and not marked as the reviewer's reading · instead: technical-replicates.9 · trail: MB-01 §Adversarial · from: MB-01:C-139, MB-01:C-140, MB-01:C-141
- **dns.22** "This determines whether a fixed correction can work" (whether bias is consistent across samples).
  why: the reviewer's framing of what matters for analysis design, not a literature finding · instead: none · trail: MB-01 §Adversarial · from: MB-01:C-138, MB-01:B-0182
- **dns.23** "Simulations disagree mainly because they build different data-generating processes into the truth" as an established finding.
  why: only partly supported; phrased as the review's own causal diagnosis · instead: rarefying.17 · trail: MB-01 §Adversarial · from: MB-01:C-142
- **dns.24** The section 5.6 "Shown to correct" column as measured results.
  why: its cells mix makers' claims and simulation results with measured results without per-cell evidence class, so it reads closer to a method recommendation than the brief allows · instead: none · trail: MB-01 §Adversarial · from: MB-01:C-143, MB-01:B-0321
- **dns.25** "0.1 to 6% of reads move between samples" as a 16S index-misassignment rate.
  why: the Table 1 row merges non-16S genome and exome libraries, Illumina's documentation, non-16S amplicons and 16S data without INDIRECT labels · instead: index-misassignment.10 · trail: MB-01 §Adversarial · from: MB-01:C-133
- **dns.26** "Water and hosts: copy-corrected rank-abundance data fit a lognormal" as one answer for both.
  why: one study (Kembel 2012) pooling ocean and human skin into one item; the brief's separate water and host cases are folded together, and the paper's simulations assumed a lognormal · instead: abundance-distribution.3 · trail: MB-01 §critic, §Adversarial · from: MB-01:C-027, MB-01:C-134
- **dns.27** "About 2.2" as the community copy number of water.
  why: the EMP value pools free-living (soil, water, sediment) and plant-associated samples · instead: community-copy-number.1 · trail: MB-01 §Adversarial · from: MB-01:C-136
- **dns.28** Extraction bias is "consistent on the ratio scale" as one finding from a 16S cell mixture and a shotgun spike-in.
  why: combines a 16S cell-mixture result and a secondary shotgun spike-in result, mixing measurement types · instead: bias-consistency.5, bias-consistency.6 · trail: MB-01 §Adversarial · from: MB-01:C-137
- **dns.29** Edgar 2017b (UNBIAS) as a "strong pessimistic claim" set aside as a single-source contrary result, while the pro-correction results stand unlabelled.
  why: McLaren and Silverman each also rest on a single mock design and get no matching single-source label · instead: copy-number-correction.13 · trail: MB-01 §Adversarial · from: MB-01:C-131
- **dns.30** "16S technical replicates are Poisson."
  why: the note warns that the assumption rests on RNA-seq lane replicates, not on 16S technical replicates · instead: sampling-model.6 · trail: MB-01 §4.1 · from: MB-01:B-0234
- **dns.31** "In bulk-soil amplicon data, 0.4 to 2% of taxa hold about 41 to 58% of reads."
  why: pools a per-sample mean under a joint abundance-and-ubiquity definition (2%, 41%) with pooled global relative abundance (0.4%, 58%); the body says these must not be combined · instead: abundance-distribution.12 · trail: MB-02 §critic, §Adversarial · from: MB-02:C-043, MB-02:C-060, MB-02:C-135, MB-02:A-148
- **dns.32** "Bulk soil shows a positive abundance-occupancy relationship wherever tested."
  why: two partly overlapping datasets whose metrics are partly circular; the search reviewed about 25 titles; the circularity caution was applied only to Delgado-Baquerizo · instead: abundance-occupancy.4 · trail: MB-02 §critic, §Adversarial · from: MB-02:C-053, MB-02:C-061, MB-02:C-062, MB-02:C-127, MB-02:A-100, MB-02:A-151
- **dns.33** "Genome copies usually fall in stationary phase or starvation" as a property of prokaryotes.
  why: rests largely on one laboratory's abstracts; folds taxon-specific and sometimes opposite behaviours into one trend; ploidy rises in stationary phase in A. vinelandii, and in M. acetivorans in slow growth · instead: ploidy.1, ploidy.8 · trail: MB-02 §Adversarial · from: MB-02:C-087, MB-02:C-136, MB-02:A-135, MB-02:C-129
- **dns.34** "No direct contradictions found" for the ploidy values.
  why: Pecoraro 2011 Table 5, read in full, and Bruck 2023, an open full text, report contrary cases · instead: ploidy.8, ploidy.9 · trail: MB-02 §critic, §Adversarial · from: MB-02:C-063, MB-02:C-130, MB-02:A-031, MB-02:C-129
- **dns.35** "Evidence on genome copies per cell is strong for cultures."
  why: apart from Pecoraro 2011 all ploidy studies were read at abstract level and rest largely on one laboratory's qPCR method; moderate, not strong · instead: ploidy.1 · trail: MB-02 §critic, §Adversarial · from: MB-02:C-014, MB-02:C-068, MB-02:A-028, MB-02:A-136
- **dns.36** "Independent replication of the ploidy values by other groups was not located."
  why: the paper read in full (Pecoraro 2011) lists independent measurements (Azotobacter, Desulfovibrio, Neisseria, Buchnera, Deinococcus, Borrelia, rhizobial bacteroids) · instead: ploidy.9 · trail: MB-02 §Adversarial · from: MB-02:C-075, MB-02:C-131, MB-02:B-0109
- **dns.37** "16S copies per cell scale with origin number more than with genome number" as a finding.
  why: the reviewer's inference from one abstract (Couturier and Rocha 2006), not labelled as such; no source measures it · instead: ploidy.13 · trail: MB-02 §critic, §Adversarial · from: MB-02:C-015, MB-02:C-088, MB-02:C-140
- **dns.38** "In Prochlorococcus the share of cells carrying two genomes changes over the day."
  why: the abstract read gives no share; it states only that replication occurred in the afternoon and division at night · instead: ploidy.20 · trail: MB-02 §Adversarial · from: MB-02:C-078, MB-02:C-079, MB-02:C-080, MB-02:B-0123
- **dns.39** "No source reports, for any natural community, the share of cells carrying one genome copy versus more than one, by taxon" as established.
  why: in situ flow cytometric cell-cycle analyses of Prochlorococcus are taxon-specific measurements of the share of cells with replicated DNA; the review read only the abstract · instead: ploidy.21, ploidy.25 · trail: MB-02 §critic, §Adversarial · from: MB-02:C-018, MB-02:C-107, MB-02:C-017
- **dns.40** "Other biases (extraction, primers) are of similar or larger size than copy-number bias and multiply with it" (McLaren 2019).
  why: the McLaren abstract, the only part read, does not compare their magnitude with copy-number bias · instead: copy-number-correction.17 · trail: MB-02 §critic, §Adversarial · from: MB-02:C-025, MB-02:C-077, MB-02:C-090, MB-02:C-132, MB-02:A-046
- **dns.41** "Abundant is usually above 1%", citing Jia et al. 2022.
  why: Jia 2022 uses a single rare/common cutoff and does not support "abundant above 1%" · instead: rare-biosphere.3 · trail: MB-02 §critic · from: MB-02:C-032, MB-02:C-065
- **dns.42** "Only about 1% of taxa were agreed by all four core methods" as Custer's figure.
  why: the source gives 165 and 176 taxa as 13% and 15.85% of core assignments; "about 1%" is the reviewer's derivation and should carry a derived label · instead: term-sensitivity.5 · trail: MB-02 §critic, §Adversarial · from: MB-02:C-034, MB-02:C-081
- **dns.43** "Occupancy-based core methods performed best" as an established standard.
  why: rests on one simulation study (Custer 2023) · instead: term-sensitivity.7 · trail: MB-02 §Adversarial · from: MB-02:C-092
- **dns.44** "Two phylotypes dominate soil archaea" as a general finding.
  why: rests on one abstract-only study (Bates 2011, 2010-era 454 data, 146 soils) · instead: abundance-distribution.13 · trail: MB-02 §critic, §Adversarial · from: MB-02:C-044, MB-02:C-091
- **dns.45** "Low-abundance taxa are routinely recorded absent where present, which by itself produces lower occupancy for rarer taxa" as a finding of Zhou 2011.
  why: generalises from one 454-era study at one site, and the second clause is the reviewer's inference, not drawn in Zhou's abstract · instead: abundance-occupancy.9 · trail: MB-02 §Adversarial · from: MB-02:C-086, MB-02:C-139
- **dns.46** "Archaea carry 1 to 4 copies (to v5.0)" as the whole record.
  why: Acinas et al. 2004 already report a maximum of five archaeal operons; the review's sources conflict and it does not flag this · instead: copy-number.8 · trail: MB-02 §critic, §Adversarial · from: MB-02:C-002, MB-02:C-138
- **dns.47** "Acidobacteria average 1.0 copies" presented alongside large-n phyla without the n.
  why: the mean rests on 4 genomes from 4 species, and the soil correction example depends on it · instead: copy-number.13 · trail: MB-02 §critic, §Adversarial · from: MB-02:C-003, MB-02:C-089
- **dns.48** "Up to 41% of rRNA genes in soil are unlinked" without the single-source flag.
  why: rests on Brewer 2020 alone (abstract only); the body flags this, the answer does not · instead: copy-number.20 · trail: MB-02 §Adversarial · from: MB-02:C-093
- **dns.49** "The 1 to 15 range is consistent across independent sources" (replicated).
  why: the sources draw on overlapping NCBI genome sets, so they are not independent replications · instead: copy-number.1 · trail: MB-02 §critic · from: MB-02:C-006
- **dns.50** "Eleven DNA-based mock communities fitted 7.1% better without correction."
  why: Starke 2021 computed its 7.1% on n = 10 mocks; one of the eleven was excluded · instead: copy-number-correction.11 · trail: MB-02 §critic · from: MB-02:C-022, MB-02:C-065

## Gaps
- **gap.1** Same-sample comparisons of 16S amplicon data with shotgun metagenomic, culture-based, microscopy/FISH or taxon-specific qPCR measurements (nearest precedents named in the brief); the only shotgun evidence is Costea 2017, known secondarily via McLaren.
  blocks: workflow-bias, bias-consistency · origin: critic coverage gap (all environments; D2) · src: costeaTowardsStandardsHuman2017, jianQuantitativePCRProvides2020 · from: MB-01:C-105, MB-01:C-106, MB-01:C-107
- **gap.2** Field sampling and preservation choices for water (volume filtered, filter pore size, prefiltration, filter storage) and for host tissue (swab versus biopsy versus lavage, plant tissue surface sterilisation): unsearched on the review's own Search record.
  blocks: sampling-storage, sampling-storage.7 · origin: critic coverage gap (D1, D2) · from: MB-01:C-108
- **gap.3** The note contradicts itself on field sampling for water and host tissue: section 2.1 says "The lab angle searched preservation and storage terms through Crossref, Europe PMC and web search", while the Search record says "Water-sampling and host-tissue sampling choices (not searched by any angle)".
  blocks: sampling-storage.7 · origin: a note that contradicts itself, flagged by the critic · trail: MB-01 §2.1, §Search record · from: MB-01:B-0088, MB-01:B-0385, MB-01:C-006, MB-01:C-007
- **gap.4** Long-read platforms: Nanopore (ONT) full-length 16S is absent, PacBio full-length evidence is only the developer's own claim, and there are no independent long-read mock benchmarks.
  blocks: sequencing-platform, sequencing-platform.4 · origin: critic coverage gap (D1, D2); named in the stage 2 check · src: callahanHighthroughputAmpliconSequencing2019 · from: MB-01:C-109, MB-01:B-0021
- **gap.5** 16S-specific index hopping on Illumina patterned flow cells (NovaSeq, NextSeq 2000); the 16S rate is one preprint abstract.
  blocks: index-misassignment · origin: critic coverage gap (D2); "not found" result; named in the stage 2 check · src: edgarUNCROSSFilteringHighfrequency2016 · from: MB-01:C-110, MB-01:A-122, MB-01:B-0382
- **gap.6** Within-run read-count variation per sample after pooling, and the correlation of library size with biomass; Schloss 2024b cites two primary studies on this (Minich et al. 2022 on 101 fish species; Cruz et al. 2021 on an equivolumetric protocol), known only secondarily and not opened.
  blocks: read-depth, read-depth.5, read-depth.8 · origin: critic coverage gap (D3, D5); "not found" result; named in the stage 2 check · src: schlossRarefactionCurrentlyBest2024 · from: MB-01:C-111, MB-01:A-160, MB-01:B-0379
- **gap.7** Measured community-average 16S copy number by environment, for example from shotgun metagenomes (16S reads normalised to single-copy marker genes): not searched, so "not found" rests on prediction-only sources.
  blocks: community-copy-number · origin: critic coverage gap (D3); named in the stage 2 check · from: MB-01:C-112, MB-01:B-0381
- **gap.8** Absolute per-cycle amplification efficiency of universal 16S primers on soil, sediment, water and faecal extracts: the qPCR methods literature (per-reaction efficiency from amplification curves, inhibition in environmental extracts) was not searched.
  blocks: pcr-efficiency · origin: critic coverage gap (D3); "not found" result; named in the stage 2 check · from: MB-01:C-113, MB-01:B-0380
- **gap.9** Species abundance distributions in marine and freshwater and in host-associated 16S datasets: Grilli 2020's per-biome supplementary figures and Shoemaker 2017's full text were not read.
  blocks: abundance-distribution · origin: critic coverage gap (D3) · src: grilliMacroecologicalLawsDescribe2020, shoemakerMacroecologicalTheoryMicrobial2017 · from: MB-01:C-114, MB-01:B-0386
- **gap.10** Dirichlet-multinomial or overdispersion fits to 16S technical replicates, and technical replicates across depths in aquatic, plant and human non-gut samples.
  blocks: overdispersion, technical-replicates · origin: critic coverage gap (D4); "not found" result · from: MB-01:C-115, MB-01:B-0383
- **gap.11** Contaminant-removal tools beyond decontam and SourceTracker (for example tools modelling well-to-well leakage), and independent benchmarks of decontam's prevalence mode.
  blocks: contamination · origin: critic coverage gap (D1, D2) · src: davisSimpleStatisticalIdentification2018 · from: MB-01:C-116
- **gap.12** Compositional beta-diversity variants (robust Aitchison, phylogenetic isometric log-ratio) and microbiome scaling methods such as GMPR and ANCOM-BC2, benchmarked from primary sources; coverage relies on Yang and Chen 2022 and Llorens-Rico 2021.
  blocks: compositional-analysis, scaling-normalisation, beta-diversity · origin: critic coverage gap (D5) · from: MB-01:C-117
- **gap.13** Any D5 approach benchmarked in soil or water with measured absolute loads as truth, and a known-richness mock tested across depths.
  blocks: absolute-quantification, richness-estimators, rarefying · origin: critic coverage gap (D5); "not found" result · from: MB-01:C-118
- **gap.14** Archaea-rich environments (marine, sediment, methanogenic reactors): archaeal-specific primer bias against known composition is absent.
  blocks: primers, workflow-bias.9 · origin: critic coverage gap (D2, D3) · from: MB-01:C-119
- **gap.15** An independent microbial amplicon benchmark of coverage-based standardisation with known truth.
  blocks: coverage-standardisation · origin: "not found" result (statistics angle) · from: MB-01:B-0384
- **gap.16** MB-01's stage 2 check is triggered: a follow-up brief targeting per-cycle efficiency, metagenome-measured community copy number, 16S index hopping on patterned flow cells, within-run read-count variation against load and long-read platform error is not yet written.
  blocks: gap.4, gap.5, gap.6, gap.7, gap.8 · origin: a follow-up the note's stage-2 check called for · from: MB-01:B-0021, MB-01:B-0022
- **gap.17** MB-01's two angles report different Kozich 2013 error rates after preclustering for partially overlapping regions (V3-V4 0.10 to 0.21% and V4-V5 0.36 to 0.64%, against 0.24 to 0.37% and 0.58 to 0.87%).
  blocks: sequencing-platform.3 · origin: a note that reports two readings of one source · from: MB-01:B-0135, MB-01:B-0136
- **gap.18** Zhou 2011's discussion gives replicate OTU overlaps of 13.1% and 5.9%, which differ from its abstract's 17.2% and 8.2%; the discussion values could not be confirmed.
  blocks: technical-replicates.1 · origin: a source reported as inconsistent with itself, unchecked · from: MB-01:B-0232, MB-01:C-076
- **gap.19** Polyploidy of cultured soil and plant-associated bacteria measured outside the Soppa laboratory: Azotobacter vinelandii (40 to 80 copies, rising in stationary phase), Deinococcus radiodurans, and endoreduplicated Sinorhizobium bacteroids in nodules (Mergaert et al. 2006).
  blocks: ploidy · origin: critic coverage gap (D1b) · src: pecoraroQuantificationPloidyProteobacteria2011, bruckOneAdvantageBeing2023 · from: MB-02:C-102
- **gap.20** Single-cell genome-copy distributions in cultures (classic flow-cytometric chromosome run-out work giving per-cell distributions of 1, 2, 4 and 8 chromosomes, for example Skarstad, Boye and Steen 1986, and Caulobacter swarmer-cell G1 shares): the direct measurements of the share of cells at one genome copy versus several, not searched.
  blocks: ploidy · origin: critic coverage gap · from: MB-02:C-103, MB-02:C-104, MB-02:C-105
- **gap.21** In situ taxon-specific DNA-content distributions of marine picocyanobacteria (Prochlorococcus and Synechococcus cell-cycle analyses, Vaulot 1995 and successors), read only at abstract level.
  blocks: ploidy.21 · origin: critic coverage gap · src: vaulotGrowthProchlorococcusPhotosynthetic1995 · from: MB-02:C-106, MB-02:C-107, MB-02:C-108
- **gap.22** Ploidy of dormant and sporulated forms (endospores, Streptomyces spores, Azotobacter cysts) and of non-growing small soil cells.
  blocks: ploidy · origin: critic coverage gap; the brief asks for dormant states · from: MB-02:C-109
- **gap.23** In situ growth state of soil taxa: qSIP growth rates and soil and rhizosphere growth-rate potential from genomes (Chuckran et al. 2025 on rewetted soil; Lopez et al. 2023 on rhizosphere versus bulk soil, which also reports 6.6% more rRNA operons in rhizosphere bacteria via a cited study); no replication indices for soil metagenomes were found.
  blocks: ploidy, ploidy.24 · origin: critic coverage gap; "not found" result; named in the stage 2 check · from: MB-02:C-110, MB-02:B-0128, MB-02:B-0015
- **gap.24** Soil studies using community-weighted rrn copy number (for example Nemergut et al. 2016 on succession) and soil absolute quantification (for example Smets et al. 2016), not searched for MB-02's copy-number or soil-abundance answers.
  blocks: copy-number-correction, abundance-distribution · origin: critic coverage gap; named in the stage 2 check · src: nemergutDecreasesAverageBacterial2015, smetsMethodSimultaneousMeasurement2016 · from: MB-02:C-111, MB-02:C-027
- **gap.25** Occupancy-based classification terms: habitat generalist versus specialist (Levins niche breadth, for example Szekely and Langenheder 2014), cosmopolitan versus endemic, and the microbial core-satellite partition (for example van der Gast et al. 2011).
  blocks: core-microbiome, global-classes · origin: critic coverage gap; named in the stage 2 check · from: MB-02:C-038, MB-02:C-112, MB-02:B-0016
- **gap.26** The soil literature contrasting abundant and rare subcommunities' distribution ranges and niche breadth across regions (for example Jiao and Lu 2020; Jiao, Chen and Wei 2017), which bears on abundance versus occupancy and on threshold usage in soil.
  blocks: abundance-occupancy, rare-biosphere · origin: critic coverage gap · from: MB-02:C-113, MB-02:C-114, MB-02:C-115
- **gap.27** Global genome-resolved or metagenome-based soil datasets (for example Bahram et al. 2018, used by Bickel and Or) examined for taxon abundance distributions or occupancy.
  blocks: abundance-distribution.19, abundance-occupancy · origin: critic coverage gap; named in the stage 2 check · from: MB-02:C-116, MB-02:C-047
- **gap.28** Taxon-specific cell counts in soil (CARD-FISH or FISH phylum or class shares): not searched beyond SAD-specific queries.
  blocks: abundance-distribution.23 · origin: critic coverage gap; named in the stage 2 check · from: MB-02:C-117
- **gap.29** Non-soil nearest precedents for the shape of the abundance distribution that contradict the lognormal view (for example power-law tails of non-dominant plankton, Ser-Giacomi et al. 2018).
  blocks: abundance-distribution.18 · origin: critic coverage gap · from: MB-02:C-118
- **gap.30** Explicit sampling or occupancy-detection models applied to soil microbes (site-occupancy models, or gamma-Poisson occupancy predictions on soil data), and whether Grilli 2020's datasets include soil.
  blocks: abundance-occupancy.14, sampling-model.7 · origin: critic coverage gap; "not found" result · from: MB-02:C-119, MB-02:C-120, MB-02:C-121
- **gap.31** Technical-replicate detection studies after the 454 era (Illumina, deeper sequencing) in soil, to test whether Zhou 2011's low overlap generalises.
  blocks: abundance-occupancy.9, technical-replicates · origin: critic coverage gap · from: MB-02:C-122
- **gap.32** MB-02's stage 2 check is triggered: the critic names unsearched per-cell and growth-state evidence for soil; the follow-up brief is not written, and the owner decides.
  blocks: gap.19, gap.20, gap.22, gap.23, gap.24, gap.25, gap.27, gap.28 · origin: a follow-up the note's stage-2 check called for · from: MB-02:B-0013, MB-02:B-0014, MB-02:B-0017
- **gap.33** MB-02's D3(a) answer contradicts its body: the answer says "a small fraction of taxa (0.4 to 2% by the two definitions) holds about 41 to 58% of reads", while the body says "The dominant shares in [60] and [61] use different definitions and denominators and are not combined here".
  blocks: abundance-distribution.12 · origin: a note that contradicts itself, flagged by the critic · trail: MB-02 §answers, §D3.1 · from: MB-02:A-148, MB-02:B-0226, MB-02:C-043
- **gap.34** Custer 2023's text is internally inconsistent on whether core analyses gained or lost the temporal effect in the human data.
  blocks: term-sensitivity.6 · origin: a source reported by the critic as inconsistent with itself · from: MB-02:C-035
- **gap.35** Nemergut 2011's bulk-soil figures (28% against 2%, 69% against 8%) could not be verified and should be rechecked.
  blocks: abundance-occupancy.1 · origin: critic access finding · src: nemergutGlobalPatternsBiogeography2011 · from: MB-02:C-085
- **gap.36** The high rrnDB maxima (21 to 22 copies in bacteria) and the current shares have no published check against assembly quality.
  blocks: copy-number.7 · origin: a result no source checked · from: MB-02:A-011, MB-02:B-0043
- **gap.37** A mean copy figure in Pei et al. 2010 (2.22 ± 0.81) whose meaning was unclear from the abstract; not used.
  blocks: copy-number · origin: a source the note set aside, unread beyond the abstract · from: MB-02:B-0308, MB-02:B-0309

## Out of scope
- MB-01:C-052, MB-01:C-053, MB-01:C-060: the critic's overall verdict on the review (evaluation of the review, not a finding)
- MB-01:C-093..104: reference corrections and Crossref checks, applied in Sources
- MB-01:A-025: cross-reference to the D2 and D5 answers (routing, not a finding)
- MB-01:A-029..031, MB-01:A-127..129, MB-01:A-179..181, MB-01:A-223, MB-01:A-224, MB-01:A-287..289: access basis of the answers (provenance, kept in the result note and recorded per source in Sources)
- MB-02:C-056, MB-02:C-059: the critic's overall verdict on the review (evaluation of the review, not a finding)
- MB-02:C-094..101: reference checks against Crossref, applied in Sources
- MB-02:A-016, MB-02:A-056, MB-02:A-078, MB-02:A-096, MB-02:A-122, MB-02:A-133, MB-02:A-139: access basis of the answers (provenance, kept in the result note and recorded per source in Sources)

## Sources

```bibtex
@article{abellanschneyderPrimerPipelinesParameters2021,
  author = {Abellan-Schneyder, Isabel and Matchado, Monica S. and Reitmeier, Sandra and Sommer, Alina and Sewald, Zeno and Baumbach, Jan and List, Markus and Neuhaus, Klaus},
  title = {Primer, pipelines, parameters: issues in 16S rRNA gene sequencing},
  journal = {mSphere},
  year = {2021},
  volume = {6},
  number = {1},
  pages = {e01202-20},
  doi = {10.1128/mSphere.01202-20},
  note = {access: full_text (MB-01); type: peer reviewed}
}

@article{acinasPCRinducedSequenceArtifacts2005,
  author = {Acinas, Silvia G. and Sarma-Rupavtarm, Ramahi and Klepac-Ceraj, Vanja and Polz, Martin F.},
  title = {PCR-induced sequence artifacts and bias: insights from comparison of two 16S rRNA clone libraries constructed from the same sample},
  journal = {Applied and Environmental Microbiology},
  year = {2005},
  volume = {71},
  number = {12},
  pages = {8966-8969},
  doi = {10.1128/AEM.71.12.8966-8969.2005},
  note = {access: abstract_only (MB-01); type: peer reviewed}
}

@article{albertsenBackBasicsInfluence2015,
  author = {Albertsen, Mads and Karst, Søren M. and Ziegler, Anja S. and Kirkegaard, Rasmus H. and Nielsen, Per H.},
  title = {Back to basics: the influence of DNA extraction and primer choice on phylogenetic analysis of activated sludge communities},
  journal = {PLOS ONE},
  year = {2015},
  volume = {10},
  number = {7},
  pages = {e0132783},
  doi = {10.1371/journal.pone.0132783},
  note = {access: full_text (MB-01); type: peer reviewed}
}

@article{almeidaBenchmarkingTaxonomicAssignments2018,
  author = {Almeida, Alexandre and Mitchell, Alex L. and Tarkowska, Aleksandra and Finn, Robert D.},
  title = {Benchmarking taxonomic assignments based on 16S rRNA gene profiling of the microbiota from commonly sampled environments},
  journal = {GigaScience},
  year = {2018},
  volume = {7},
  number = {5},
  pages = {giy054},
  doi = {10.1093/gigascience/giy054},
  note = {access: full_text (MB-01); type: peer reviewed}
}

@article{alroyCoveragebasedRarefactionFails2026,
  author = {Alroy, John},
  title = {Coverage-based rarefaction fails to quantify relative species richness},
  year = {2026},
  doi = {10.1002/oik.11607},
  note = {access: abstract_only (MB-01; DOI checked on Crossref by the synthesis agent); type: peer reviewed; published online 2026-09-14, volume not yet assigned; incomplete: volume},
  journal = {Oikos},
  pages = {e11607}
}

@article{andersDifferentialExpressionAnalysis2010,
  author = {Anders, Simon and Huber, Wolfgang},
  title = {Differential expression analysis for sequence count data},
  journal = {Genome Biology},
  year = {2010},
  volume = {11},
  number = {10},
  pages = {R106},
  doi = {10.1186/gb-2010-11-10-r106},
  note = {access: abstract_only (MB-01; INDIRECT); type: peer reviewed}
}

@article{barlowQuantitativeSequencingFramework2020,
  author = {Barlow, Jacob T. and Bogatyrev, Said R. and Ismagilov, Rustem F.},
  title = {A quantitative sequencing framework for absolute abundance measurements of mucosal and lumenal microbial communities},
  journal = {Nature Communications},
  year = {2020},
  volume = {11},
  pages = {2590},
  doi = {10.1038/s41467-020-16224-6},
  note = {access: full_text (MB-01); type: peer reviewed}
}

@article{beuleImprovedNormalizationSpecies2020,
  author = {Beule, Lukas and Karlovsky, Petr},
  title = {Improved normalization of species count data in ecology by scaling with ranked subsampling (SRS): application to microbial communities},
  journal = {PeerJ},
  year = {2020},
  volume = {8},
  pages = {e9593},
  doi = {10.7717/peerj.9593},
  note = {access: abstract_only (MB-01); type: peer reviewed}
}

@article{bokulichQualityfilteringVastlyImproves2013,
  author = {Bokulich, Nicholas A. and Subramanian, Sathish and Faith, Jeremiah J. and Gevers, Dirk and Gordon, Jeffrey I. and Knight, Rob and Mills, David A. and Caporaso, J. Gregory},
  title = {Quality-filtering vastly improves diversity estimates from Illumina amplicon sequencing},
  journal = {Nature Methods},
  year = {2013},
  volume = {10},
  number = {1},
  pages = {57-59},
  doi = {10.1038/nmeth.2276},
  note = {access: full_text (MB-01); type: peer reviewed}
}

@article{bokulichOptimizingTaxonomicClassification2018,
  author = {Bokulich, Nicholas A. and Kaehler, Benjamin D. and Rideout, Jai Ram and Dillon, Matthew and Bolyen, Evan and Knight, Rob and Huttley, Gavin A. and Caporaso, J. Gregory},
  title = {Optimizing taxonomic classification of marker-gene amplicon sequences with QIIME 2's q2-feature-classifier plugin},
  journal = {Microbiome},
  year = {2018},
  volume = {6},
  pages = {90},
  doi = {10.1186/s40168-018-0470-z},
  note = {access: full_text (MB-01); type: peer reviewed}
}

@article{bonkPCRbasedQuantificationTaxaspecific2018,
  author = {Bonk, Fabian and Popp, Denny and Harms, Hauke and Centler, Florian},
  title = {PCR-based quantification of taxa-specific abundances in microbial communities: quantifying and avoiding common pitfalls},
  journal = {Journal of Microbiological Methods},
  year = {2018},
  volume = {153},
  pages = {139-147},
  doi = {10.1016/j.mimet.2018.09.015},
  note = {access: abstract_only (MB-01); type: peer reviewed review}
}

@article{brooksTruthMetagenomicsQuantifying2015,
  author = {{Vaginal Microbiome Consortium} and Brooks, J. Paul and Edwards, David J. and Harwich, Michael D. Jr and Rivera, Maria C. and Fettweis, Jennifer M. and Serrano, Myrna G. and Reris, Robert A. and Sheth, Nihar U. and Huang, Bernice and Girerd, Philippe and Strauss, Jerome F. 3rd and Jefferson, Kimberly K. and Buck, Gregory A.},
  title = {The truth about metagenomics: quantifying and counteracting bias in 16S rRNA studies},
  journal = {BMC Microbiology},
  year = {2015},
  volume = {15},
  pages = {66},
  doi = {10.1186/s12866-015-0351-6},
  note = {access: full_text (MB-01; title corrected against Crossref); type: peer reviewed; author order corrected (critic: MB-01:C-098..100; Crossref puts the consortium entry first)}
}

@article{bullardEvaluationStatisticalMethods2010,
  author = {Bullard, James H. and Purdom, Elizabeth and Hansen, Kasper D. and Dudoit, Sandrine},
  title = {Evaluation of statistical methods for normalization and differential expression in mRNA-Seq experiments},
  journal = {BMC Bioinformatics},
  year = {2010},
  volume = {11},
  pages = {94},
  doi = {10.1186/1471-2105-11-94},
  note = {access: abstract_only (MB-01; INDIRECT); type: peer reviewed}
}

@article{pereiraComparisonNormalizationMethods2018,
  author = {Buongermino Pereira, Mariana and Wallroth, Mikael and Jonsson, Viktor and Kristiansson, Erik},
  title = {Comparison of normalization methods for the analysis of metagenomic gene abundance data},
  journal = {BMC Genomics},
  year = {2018},
  volume = {19},
  pages = {274},
  doi = {10.1186/s12864-018-4637-6},
  note = {access: abstract_only (MB-01; INDIRECT); type: peer reviewed}
}

@article{calgaroAssessmentStatisticalMethods2020,
  author = {Calgaro, Matteo and Romualdi, Chiara and Waldron, Levi and Risso, Davide and Vitulo, Nicola},
  title = {Assessment of statistical methods from single cell, bulk RNA-seq, and metagenomics applied to microbiome data},
  journal = {Genome Biology},
  year = {2020},
  volume = {21},
  pages = {191},
  doi = {10.1186/s13059-020-02104-1},
  note = {access: abstract_only (MB-01); type: peer reviewed}
}

@article{callahanDADA2HighresolutionSample2016,
  author = {Callahan, Benjamin J. and McMurdie, Paul J. and Rosen, Michael J. and Han, Andrew W. and Johnson, Amy Jo A. and Holmes, Susan P.},
  title = {DADA2: High-resolution sample inference from Illumina amplicon data},
  journal = {Nature Methods},
  year = {2016},
  volume = {13},
  number = {7},
  pages = {581-583},
  doi = {10.1038/nmeth.3869},
  note = {access: full_text (MB-01); type: peer reviewed}
}

@article{callahanHighthroughputAmpliconSequencing2019,
  author = {Callahan, Benjamin J. and Wong, Joan and Heiner, Cheryl and Oh, Steve and Theriot, Casey M. and Gulati, Ajay S. and McGill, Sarah K. and Dougherty, Michael K.},
  title = {High-throughput amplicon sequencing of the full-length 16S rRNA gene with single-nucleotide resolution},
  journal = {Nucleic Acids Research},
  year = {2019},
  volume = {47},
  number = {18},
  pages = {e103},
  doi = {10.1093/nar/gkz569},
  note = {access: full_text (MB-01); type: peer reviewed}
}

@article{cameronEnhancingDiversityAnalysis2021,
  author = {Cameron, Ellen S. and Schmidt, Philip J. and Tremblay, Benjamin J.-M. and Emelko, Monica B. and Müller, Kirsten M.},
  title = {Enhancing diversity analysis by repeatedly rarefying next generation sequencing data describing microbial communities},
  journal = {Scientific Reports},
  year = {2021},
  volume = {11},
  pages = {22302},
  doi = {10.1038/s41598-021-01636-1},
  note = {access: full_text (MB-01); type: peer reviewed}
}

@article{cariniRelicDNAAbundant2016,
  author = {Carini, Paul and Marsden, Patrick J. and Leff, Jonathan W. and Morgan, Emily E. and Strickland, Michael S. and Fierer, Noah},
  title = {Relic DNA is abundant in soil and obscures estimates of soil microbial diversity},
  journal = {Nature Microbiology},
  year = {2016},
  volume = {2},
  number = {3},
  pages = {16242},
  doi = {10.1038/nmicrobiol.2016.242},
  note = {access: abstract_only (MB-01), abstract_only (MB-02; year given as 2017; online 2016); type: peer reviewed; cited as: MB-02 [77]}
}

@article{carusoPerformanceMicrobiomeSequence2019,
  author = {Caruso, Vincent and Song, Xubo and Asquith, Mark and Karstens, Lisa},
  title = {Performance of microbiome sequence inference methods in environments with varying biomass},
  journal = {mSystems},
  year = {2019},
  volume = {4},
  number = {1},
  pages = {e00163-18},
  doi = {10.1128/mSystems.00163-18},
  note = {access: full_text (MB-01); type: peer reviewed}
}

@article{chaoCoveragebasedRarefactionExtrapolation2012,
  author = {Chao, Anne and Jost, Lou},
  title = {Coverage-based rarefaction and extrapolation: standardizing samples by completeness rather than size},
  journal = {Ecology},
  year = {2012},
  volume = {93},
  number = {12},
  pages = {2533-2547},
  doi = {10.1890/11-1952.1},
  note = {access: full_text (MB-01; via third-party PDF https://www.davidzeleny.net/wiki/lib/exe/fetch.php/vegecol:materials:chao-jost2012_ecology.pdf, accessed 2026-10-20; INDIRECT); type: peer reviewed}
}

@article{chaoRarefactionExtrapolationHill2014,
  author = {Chao, Anne and Gotelli, Nicholas J. and Hsieh, T. C. and Sander, Elizabeth L. and Ma, K. H. and Colwell, Robert K. and Ellison, Aaron M.},
  title = {Rarefaction and extrapolation with Hill numbers: a framework for sampling and estimation in species diversity studies},
  journal = {Ecological Monographs},
  year = {2014},
  volume = {84},
  number = {1},
  pages = {45-67},
  doi = {10.1890/13-0133.1},
  note = {access: full_text (MB-01; via author PDF https://www.uvm.edu/~ngotelli/manuscriptpdfs/ChaoHill.pdf, accessed 2026-10-20; INDIRECT); type: peer reviewed}
}

@article{chiarelloRankingBiasesChoice2022,
  author = {Chiarello, Marlène and McCauley, Mark and Villéger, Sébastien and Jackson, Colin R.},
  title = {{Ranking the biases: the choice of OTUs vs. ASVs in 16S rRNA amplicon data analysis has stronger effects on diversity measures than rarefaction and OTU identity threshold}},
  journal = {PLOS ONE},
  year = {2022},
  volume = {17},
  number = {2},
  pages = {e0264443},
  doi = {10.1371/journal.pone.0264443},
  note = {access: full_text (MB-01); type: peer reviewed}
}

@article{chiuEstimatingComparingMicrobial2016,
  author = {Chiu, Chun-Huo and Chao, Anne},
  title = {Estimating and comparing microbial diversity in the presence of sequencing errors},
  journal = {PeerJ},
  year = {2016},
  volume = {4},
  pages = {e1634},
  doi = {10.7717/peerj.1634},
  note = {access: abstract_only (MB-01); type: peer reviewed}
}

@article{costelloCharacterizationRemediationSample2018,
  author = {Costello, Maura and Fleharty, Mark and Abreu, Justin and Farjoun, Yossi and Ferriera, Steven and Holmes, Laurie and Granger, Brian and Green, Lisa and Howd, Tom and Mason, Tamara and Vicente, Gina and Dasilva, Michael and Brodeur, Wendy and DeSmet, Timothy and Dodge, Sheila and Lennon, Niall J. and Gabriel, Stacey},
  title = {Characterization and remediation of sample index swaps by non-redundant dual indexing on massively parallel sequencing platforms},
  journal = {BMC Genomics},
  year = {2018},
  volume = {19},
  pages = {332},
  doi = {10.1186/s12864-018-4703-0},
  note = {access: full_text (MB-01; INDIRECT); type: peer reviewed}
}

@article{damoreComprehensiveBenchmarkingStudy2016,
  author = {D'Amore, Rosalinda and Ijaz, Umer Zeeshan and Schirmer, Melanie and Kenny, John G. and Gregory, Richard and Darby, Alistair C. and Shakya, Migun and Podar, Mircea and Quince, Christopher and Hall, Neil},
  title = {A comprehensive benchmarking study of protocols and sequencing platforms for 16S rRNA community profiling},
  journal = {BMC Genomics},
  year = {2016},
  volume = {17},
  pages = {55},
  doi = {10.1186/s12864-015-2194-9},
  note = {access: full_text (MB-01); type: peer reviewed}
}

@article{davisSimpleStatisticalIdentification2018,
  author = {Davis, Nicole M. and Proctor, Diana M. and Holmes, Susan P. and Relman, David A. and Callahan, Benjamin J.},
  title = {Simple statistical identification and removal of contaminant sequences in marker-gene and metagenomics data},
  journal = {Microbiome},
  year = {2018},
  volume = {6},
  pages = {226},
  doi = {10.1186/s40168-018-0605-2},
  note = {access: full_text (MB-01); type: peer reviewed}
}

@article{dengNonparametricRichnessEstimators2024,
  author = {Deng, Yongcui and Umbach, Alexander K. and Neufeld, Josh D.},
  title = {Nonparametric richness estimators Chao1 and ACE must not be used with amplicon sequence variant data},
  journal = {The ISME Journal},
  year = {2024},
  volume = {18},
  number = {1},
  pages = {wrae106},
  doi = {10.1093/ismejo/wrae106},
  note = {access: full_text (MB-01; DOI checked by the synthesis agent); type: peer reviewed perspective}
}

@article{dyrhovdenManagingContaminationDiverse2021,
  author = {Dyrhovden, Ruben and Rippin, Martin and Øvrebø, Kjell Kåre and Nygaard, Randi M. and Ulvestad, Elling and Kommedal, Øyvind},
  title = {Managing contamination and diverse bacterial loads in 16S rRNA deep sequencing of clinical samples: implications of the law of small numbers},
  journal = {mBio},
  year = {2021},
  volume = {12},
  number = {3},
  pages = {e00598-21},
  doi = {10.1128/mBio.00598-21},
  note = {access: full_text (MB-01; DOI checked by the synthesis agent); type: peer reviewed}
}

@misc{edgarUNCROSSFilteringHighfrequency2016,
  author = {Edgar, Robert C.},
  title = {UNCROSS: filtering of high-frequency cross-talk in 16S amplicon reads},
  year = {2016},
  doi = {10.1101/088666},
  note = {access: abstract_only (MB-01); type: PREPRINT},
  howpublished = {bioRxiv 088666}
}

@misc{edgarUCHIME2ImprovedChimera2016,
  author = {Edgar, Robert C.},
  title = {UCHIME2: improved chimera prediction for amplicon sequencing},
  year = {2016},
  doi = {10.1101/074252},
  note = {access: abstract_only (MB-01); type: PREPRINT},
  howpublished = {bioRxiv 074252}
}

@article{edgarUCHIMEImprovesSensitivity2011,
  author = {Edgar, Robert C. and Haas, Brian J. and Clemente, Jose C. and Quince, Christopher and Knight, Rob},
  title = {UCHIME improves sensitivity and speed of chimera detection},
  journal = {Bioinformatics},
  year = {2011},
  volume = {27},
  number = {16},
  pages = {2194-2200},
  doi = {10.1093/bioinformatics/btr381},
  note = {access: full_text (MB-01; per bioinformatics angle); type: peer reviewed}
}

@article{edgarAccuracyMicrobialCommunity2017,
  author = {Edgar, Robert C.},
  title = {Accuracy of microbial community diversity estimated by closed- and open-reference OTUs},
  journal = {PeerJ},
  year = {2017},
  volume = {5},
  pages = {e3889},
  doi = {10.7717/peerj.3889},
  note = {access: full_text (MB-01); type: peer reviewed}
}

@misc{edgarUNBIASAttemptCorrect2017,
  author = {Edgar, Robert C.},
  title = {UNBIAS: an attempt to correct abundance bias in 16S sequencing, with limited success},
  year = {2017},
  doi = {10.1101/124149},
  note = {access: abstract_only (MB-01; DOI checked by the synthesis agent), abstract_only (MB-02; preprint); type: PREPRINT; cited as: MB-02 [31]},
  howpublished = {bioRxiv 124149}
}

@article{edgarUpdating97Identity2018,
  author = {Edgar, Robert C.},
  title = {Updating the 97% identity threshold for 16S ribosomal RNA OTUs},
  journal = {Bioinformatics},
  year = {2018},
  volume = {34},
  number = {14},
  pages = {2371-2375},
  doi = {10.1093/bioinformatics/bty113},
  note = {access: abstract_only (MB-01); type: peer reviewed}
}

@article{edgarAccuracyTaxonomyPrediction2018,
  author = {Edgar, Robert C.},
  title = {Accuracy of taxonomy prediction for 16S rRNA and fungal ITS sequences},
  journal = {PeerJ},
  year = {2018},
  volume = {6},
  pages = {e4652},
  doi = {10.7717/peerj.4652},
  note = {access: full_text (MB-01); type: peer reviewed}
}

@article{edgarTaxonomyAnnotationGuide2018,
  author = {Edgar, Robert},
  title = {Taxonomy annotation and guide tree errors in 16S rRNA databases},
  journal = {PeerJ},
  year = {2018},
  volume = {6},
  pages = {e5030},
  doi = {10.7717/peerj.5030},
  note = {access: full_text (MB-01); type: peer reviewed}
}

@article{edgarErrorFilteringPair2015,
  author = {Edgar, Robert C. and Flyvbjerg, Henrik},
  title = {Error filtering, pair assembly and error correction for next-generation sequencing reads},
  journal = {Bioinformatics},
  year = {2015},
  volume = {31},
  number = {21},
  pages = {3476-3482},
  doi = {10.1093/bioinformatics/btv401},
  note = {access: abstract_only (MB-01); type: peer reviewed}
}

@article{eisenhoferContaminationLowMicrobial2019,
  author = {Eisenhofer, Raphael and Minich, Jeremiah J. and Marotz, Clarisse and Cooper, Alan and Knight, Rob and Weyrich, Laura S.},
  title = {Contamination in low microbial biomass microbiome studies: issues and recommendations},
  journal = {Trends in Microbiology},
  year = {2019},
  volume = {27},
  number = {2},
  pages = {105-117},
  doi = {10.1016/j.tim.2018.11.003},
  note = {access: abstract_only (MB-01); type: peer reviewed review}
}

@article{eslingAccurateMultiplexingFiltering2015,
  author = {Esling, Philippe and Lejzerowicz, Franck and Pawlowski, Jan},
  title = {Accurate multiplexing and filtering for high-throughput amplicon-sequencing},
  journal = {Nucleic Acids Research},
  year = {2015},
  volume = {43},
  number = {5},
  pages = {2513-2524},
  doi = {10.1093/nar/gkv107},
  note = {access: full_text (MB-01; INDIRECT); type: peer reviewed}
}

@article{fitzpatrickChloroplastSequenceVariation2018,
  author = {Fitzpatrick, Connor R. and Lu-Irving, Patricia and Copeland, Julia and Guttman, David S. and Wang, Pauline W. and Baltrus, David A. and Dlugosch, Katrina M. and Johnson, Marc T. J.},
  title = {Chloroplast sequence variation and the efficacy of peptide nucleic acids for blocking host amplification in plant microbiome studies},
  journal = {Microbiome},
  year = {2018},
  volume = {6},
  pages = {144},
  doi = {10.1186/s40168-018-0534-0},
  note = {access: full_text (MB-01); type: peer reviewed}
}

@article{fouhy16SRRNAGene2016,
  author = {Fouhy, Fiona and Clooney, Adam G. and Stanton, Catherine and Claesson, Marcus J. and Cotter, Paul D.},
  title = {16S rRNA gene sequencing of mock microbial populations: impact of DNA extraction method, primer choice and sequencing platform},
  journal = {BMC Microbiology},
  year = {2016},
  volume = {16},
  pages = {123},
  doi = {10.1186/s12866-016-0738-z},
  note = {access: full_text (MB-01); type: peer reviewed}
}

@article{frostegardQuantificationBiasRelated1999,
  author = {Frostegård, Åsa and Courtois, Sophie and Ramisse, Vincent and Clerc, Sylvie and Bernillon, Dominique and Le Gall, Francoise and Jeannin, Pascale and Nesme, Xavier and Simonet, Pascal},
  title = {Quantification of bias related to the extraction of DNA directly from soils},
  journal = {Applied and Environmental Microbiology},
  year = {1999},
  volume = {65},
  number = {12},
  pages = {5409-5420},
  doi = {10.1128/AEM.65.12.5409-5420.1999},
  note = {access: abstract_only (MB-01); type: peer reviewed; third author and sixth author corrected (critic: MB-01:C-093; the note had Valerie Ramisse and Francoise with a cedilla)}
}

@article{galazzoHowCountOur2020,
  author = {Galazzo, Gianluca and van Best, Niels and Benedikter, Birke J. and Janssen, Kevin and Bervoets, Liene and Driessen, Christel and Oomen, Melissa and Lucchesi, Mayk and van Eijck, Pascalle H. and Becker, Heike E. F. and Hornef, Mathias W. and Savelkoul, Paul H. and Stassen, Frank R. M. and Wolffs, Petra F. and Penders, John},
  title = {How to count our microbes? The effect of different quantitative microbiome profiling approaches},
  journal = {Frontiers in Cellular and Infection Microbiology},
  year = {2020},
  volume = {10},
  pages = {403},
  doi = {10.3389/fcimb.2020.00403},
  note = {access: full_text (MB-01; DOI checked by the synthesis agent); type: peer reviewed}
}

@article{gibbonsCorrectingBatchEffects2018,
  author = {Gibbons, Sean M. and Duvallet, Claire and Alm, Eric J.},
  title = {Correcting for batch effects in case-control microbiome studies},
  journal = {PLOS Computational Biology},
  year = {2018},
  volume = {14},
  number = {4},
  pages = {e1006102},
  doi = {10.1371/journal.pcbi.1006102},
  note = {access: abstract_only (MB-01); type: peer reviewed}
}

@article{gihringMassivelyParallelRRNA2012,
  author = {Gihring, Thomas M. and Green, Stefan J. and Schadt, Christopher W.},
  title = {Massively parallel rRNA gene sequencing exacerbates the potential for biased community diversity comparisons due to variable library sizes},
  journal = {Environmental Microbiology},
  year = {2012},
  volume = {14},
  number = {2},
  pages = {285-290},
  doi = {10.1111/j.1462-2920.2011.02550.x},
  note = {access: abstract_only (MB-01); type: peer reviewed}
}

@article{glassmanBroadscaleEcologicalPatterns2018,
  author = {Glassman, Sydney I. and Martiny, Jennifer B. H.},
  title = {Broadscale ecological patterns are robust to use of exact sequence variants versus operational taxonomic units},
  journal = {mSphere},
  year = {2018},
  volume = {3},
  number = {4},
  pages = {e00148-18},
  doi = {10.1128/mSphere.00148-18},
  note = {access: full_text (MB-01); type: peer reviewed}
}

@article{gloorMicrobiomeDatasetsCompositional2017,
  author = {Gloor, Gregory B. and Macklaim, Jean M. and Pawlowsky-Glahn, Vera and Egozcue, Juan J.},
  title = {Microbiome datasets are compositional: and this is not optional},
  journal = {Frontiers in Microbiology},
  year = {2017},
  volume = {8},
  pages = {2224},
  doi = {10.3389/fmicb.2017.02224},
  note = {access: abstract_only (MB-01); type: peer reviewed mini review}
}

@article{gotelliQuantifyingBiodiversityProcedures2001,
  author = {Gotelli, Nicholas J. and Colwell, Robert K.},
  title = {Quantifying biodiversity: procedures and pitfalls in the measurement and comparison of species richness},
  journal = {Ecology Letters},
  year = {2001},
  volume = {4},
  number = {4},
  pages = {379-391},
  doi = {10.1046/j.1461-0248.2001.00230.x},
  note = {access: abstract_only (MB-01; INDIRECT); type: peer reviewed review}
}

@article{grilliMacroecologicalLawsDescribe2020,
  author = {Grilli, Jacopo},
  title = {Macroecological laws describe variation and diversity in microbial communities},
  journal = {Nature Communications},
  year = {2020},
  volume = {11},
  pages = {4743},
  doi = {10.1038/s41467-020-18529-y},
  note = {access: full_text (MB-01; partly re-opened by the synthesis agent), full_text (MB-02); type: peer reviewed; cited as: MB-02 [72]}
}

@article{haasChimeric16SRRNA2011,
  author = {Haas, Brian J. and Gevers, Dirk and Earl, Ashlee M. and Feldgarden, Mike and Ward, Doyle V. and Giannoukos, Georgia and Ciulla, Dawn and Tabbaa, Diana and Highlander, Sarah K. and Sodergren, Erica and Methé, Barbara and DeSantis, Todd Z. and {The Human Microbiome Consortium} and Petrosino, Joseph F. and Knight, Rob and Birren, Bruce W.},
  title = {Chimeric 16S rRNA sequence formation and detection in Sanger and 454-pyrosequenced PCR amplicons},
  journal = {Genome Research},
  year = {2011},
  volume = {21},
  number = {3},
  pages = {494-504},
  doi = {10.1101/gr.112730.110},
  note = {access: full_text (MB-01); type: peer reviewed}
}

@article{haegemanRobustEstimationMicrobial2013,
  author = {Haegeman, Bart and Hamelin, Jérôme and Moriarty, John and Neal, Peter and Dushoff, Jonathan and Weitz, Joshua S.},
  title = {Robust estimation of microbial diversity in theory and in practice},
  journal = {The ISME Journal},
  year = {2013},
  volume = {7},
  number = {6},
  pages = {1092-1101},
  doi = {10.1038/ismej.2013.10},
  note = {access: full_text (MB-01; critic: MB-01:C-065, C-073..076, open full text could not be confirmed); type: peer reviewed}
}

@article{harrisonDirichletmultinomialModellingOutperforms2020,
  author = {Harrison, Joshua G. and Calder, W. John and Shastry, Vivaswat and Buerkle, C. Alex},
  title = {Dirichlet-multinomial modelling outperforms alternatives for analysis of microbiome and other ecological count data},
  journal = {Molecular Ecology Resources},
  year = {2020},
  volume = {20},
  number = {2},
  pages = {481-497},
  doi = {10.1111/1755-0998.13128},
  note = {access: abstract_only (MB-01); type: peer reviewed}
}

@article{harrisonQuestAbsoluteAbundance2020,
  author = {Harrison, Joshua G. and Calder, W. John and Shuman, Bryan and Buerkle, C. Alex},
  title = {The quest for absolute abundance: the use of internal standards for DNA-based community ecology},
  journal = {Molecular Ecology Resources},
  year = {2021},
  volume = {21},
  number = {1},
  pages = {30-43},
  doi = {10.1111/1755-0998.13247},
  note = {access: abstract_only (MB-01); type: peer reviewed review}
}

@article{hawinkelBrokenPromiseMicrobiome2019,
  author = {Hawinkel, Stijn and Mattiello, Federico and Bijnens, Luc and Thas, Olivier},
  title = {A broken promise: microbiome differential abundance methods do not control the false discovery rate},
  journal = {Briefings in Bioinformatics},
  year = {2019},
  volume = {20},
  number = {1},
  pages = {210-221},
  doi = {10.1093/bib/bbx104},
  note = {access: abstract_only (MB-01); type: peer reviewed}
}

@article{hongRarefyNotRarefy2022,
  author = {Hong, Johnny and Karaoz, Ulas and de Valpine, Perry and Fithian, William},
  title = {To rarefy or not to rarefy: robustness and efficiency trade-offs of rarefying microbiome data},
  journal = {Bioinformatics},
  year = {2022},
  volume = {38},
  number = {9},
  pages = {2389-2396},
  doi = {10.1093/bioinformatics/btac127},
  note = {access: full_text (MB-01); type: peer reviewed}
}

@article{hornungIssuesCurrentStandards2019,
  author = {Hornung, Bastian V. H. and Zwittink, Romy D. and Kuijper, Ed J.},
  title = {Issues and current standards of controls in microbiome research},
  journal = {FEMS Microbiology Ecology},
  year = {2019},
  volume = {95},
  number = {5},
  pages = {fiz045},
  doi = {10.1093/femsec/fiz045},
  note = {access: full_text (MB-01); type: peer reviewed}
}

@article{jianQuantitativePCRProvides2020,
  author = {Jian, Ching and Luukkonen, Panu and Yki-Järvinen, Hannele and Salonen, Anne and Korpela, Katri},
  title = {Quantitative PCR provides a simple and accessible method for quantitative microbiota profiling},
  journal = {PLOS ONE},
  year = {2020},
  volume = {15},
  number = {1},
  pages = {e0227285},
  doi = {10.1371/journal.pone.0227285},
  note = {access: full_text (MB-01); type: peer reviewed}
}

@article{johnsonEvaluation16SRRNA2019,
  author = {Johnson, Jethro S. and Spakowicz, Daniel J. and Hong, Bo-Young and Petersen, Lauren M. and Demkowicz, Patrick and Chen, Lei and Leopold, Shana R. and Hanson, Blake M. and Agresta, Hanako O. and Gerstein, Mark and Sodergren, Erica and Weinstock, George M.},
  title = {Evaluation of 16S rRNA gene sequencing for species and strain-level microbiome analysis},
  journal = {Nature Communications},
  year = {2019},
  volume = {10},
  pages = {5029},
  doi = {10.1038/s41467-019-13036-1},
  note = {access: full_text (MB-01); type: peer reviewed}
}

@article{joosDaringDifferentialMetabarcoding2020,
  author = {Joos, Lisa and Beirinckx, Stien and Haegeman, Annelies and Debode, Jane and Vandecasteele, Bart and Baeyen, Steve and Goormachtig, Sofie and Clement, Lieven and De Tender, Caroline},
  title = {Daring to be differential: metabarcoding analysis of soil and plant-related microbial communities using amplicon sequence variants and operational taxonomical units},
  journal = {BMC Genomics},
  year = {2020},
  volume = {21},
  pages = {733},
  doi = {10.1186/s12864-020-07126-4},
  note = {access: full_text (MB-01); type: peer reviewed}
}

@article{kaehlerSpeciesAbundanceInformation2019,
  author = {Kaehler, Benjamin D. and Bokulich, Nicholas A. and McDonald, Daniel and Knight, Rob and Caporaso, J. Gregory and Huttley, Gavin A.},
  title = {Species abundance information improves sequence taxonomy classification accuracy},
  journal = {Nature Communications},
  year = {2019},
  volume = {10},
  pages = {4643},
  doi = {10.1038/s41467-019-12669-6},
  note = {access: full_text (MB-01); type: peer reviewed}
}

@article{karstensControllingContaminantsLowbiomass2019,
  author = {Karstens, Lisa and Asquith, Mark and Davin, Sean and Fair, Damien and Gregory, W. Thomas and Wolfe, Alan J. and Braun, Jonathan and McWeeney, Shannon},
  title = {Controlling for contaminants in low-biomass 16S rRNA gene sequencing experiments},
  journal = {mSystems},
  year = {2019},
  volume = {4},
  number = {4},
  pages = {e00290-19},
  doi = {10.1128/mSystems.00290-19},
  note = {access: full_text (MB-01); type: peer reviewed}
}

@article{kaulAnalysisMicrobiomeData2017,
  author = {Kaul, Abhishek and Mandal, Siddhartha and Davidov, Ori and Peddada, Shyamal D.},
  title = {Analysis of microbiome data in the presence of excess zeros},
  journal = {Frontiers in Microbiology},
  year = {2017},
  volume = {8},
  pages = {2114},
  doi = {10.3389/fmicb.2017.02114},
  note = {access: abstract_only (MB-01); type: peer reviewed}
}

@article{kebschullSourcesPCRinducedDistortions2015,
  author = {Kebschull, Justus M. and Zador, Anthony M.},
  title = {Sources of PCR-induced distortions in high-throughput sequencing data sets},
  journal = {Nucleic Acids Research},
  year = {2015},
  volume = {43},
  number = {21},
  pages = {e143},
  doi = {10.1093/nar/gkv717},
  note = {access: full_text (MB-01; INDIRECT); type: peer reviewed}
}

@article{kellyUnderstandingPCRProcesses2019,
  author = {Kelly, Ryan P. and Shelton, Andrew Olaf and Gallego, Ramón},
  title = {Understanding PCR processes to draw meaningful conclusions from environmental DNA studies},
  journal = {Scientific Reports},
  year = {2019},
  volume = {9},
  pages = {12133},
  doi = {10.1038/s41598-019-48546-x},
  note = {access: full_text (MB-01; INDIRECT); type: peer reviewed}
}

@article{kembelIncorporating16SGene2012,
  author = {Kembel, Steven W. and Wu, Martin and Eisen, Jonathan A. and Green, Jessica L.},
  title = {Incorporating 16S gene copy number information improves estimates of microbial diversity and abundance},
  journal = {PLOS Computational Biology},
  year = {2012},
  volume = {8},
  number = {10},
  pages = {e1002743},
  doi = {10.1371/journal.pcbi.1002743},
  note = {access: full_text (MB-01), full_text (MB-02); type: peer reviewed; cited as: MB-02 [28]}
}

@article{kennedyEvaluatingBiasIlluminabased2014,
  author = {Kennedy, Katherine and Hall, Michael W. and Lynch, Michael D. J. and Moreno-Hagelsieb, Gabriel and Neufeld, Josh D.},
  title = {Evaluating bias of Illumina-based bacterial 16S rRNA gene profiles},
  journal = {Applied and Environmental Microbiology},
  year = {2014},
  volume = {80},
  number = {18},
  pages = {5717-5722},
  doi = {10.1128/AEM.01451-14},
  note = {access: abstract_only (MB-01); type: peer reviewed; conflict: the reference list and the in-text label say AB, while the critic (MB-01:C-073) lists it among sources labelled FT whose full text could not be confirmed}
}

@article{kersPowerMicrobiomeStudies2022,
  author = {Kers, Jannigje Gerdien and Saccenti, Edoardo},
  title = {The power of microbiome studies: some considerations on which alpha and beta metrics to use and how to report results},
  journal = {Frontiers in Microbiology},
  year = {2022},
  volume = {12},
  pages = {796025},
  doi = {10.3389/fmicb.2021.796025},
  note = {access: abstract_only (MB-01); type: peer reviewed}
}

@article{kircherDoubleIndexingOvercomes2012,
  author = {Kircher, Martin and Sawyer, Susanna and Meyer, Matthias},
  title = {Double indexing overcomes inaccuracies in multiplex sequencing on the Illumina platform},
  journal = {Nucleic Acids Research},
  year = {2012},
  volume = {40},
  number = {1},
  pages = {e3},
  doi = {10.1093/nar/gkr771},
  note = {access: full_text (MB-01; INDIRECT); type: peer reviewed}
}

@article{klappenbachRRNAOperonCopy2000,
  author = {Klappenbach, Joel A. and Dunbar, John M. and Schmidt, Thomas M.},
  title = {rRNA operon copy number reflects ecological strategies of bacteria},
  journal = {Applied and Environmental Microbiology},
  year = {2000},
  volume = {66},
  number = {4},
  pages = {1328-1333},
  doi = {10.1128/AEM.66.4.1328-1333.2000},
  note = {access: abstract_only (MB-01), abstract_only (MB-02); type: peer reviewed; cited as: MB-02 [9]}
}

@article{klindworthEvaluationGeneral16S2013,
  author = {Klindworth, Anna and Pruesse, Elmar and Schweer, Timmy and Peplies, Jörg and Quast, Christian and Horn, Matthias and Glöckner, Frank Oliver},
  title = {Evaluation of general 16S ribosomal RNA gene PCR primers for classical and next-generation sequencing-based diversity studies},
  journal = {Nucleic Acids Research},
  year = {2013},
  volume = {41},
  number = {1},
  pages = {e1},
  doi = {10.1093/nar/gks808},
  note = {access: full_text (MB-01); type: peer reviewed}
}

@article{kopylovaOpensourceSequenceClustering2016,
  author = {Kopylova, Evguenia and Navas-Molina, Jose A. and Mercier, Céline and Xu, Zhenjiang Zech and Mahé, Frédéric and He, Yan and Zhou, Hong-Wei and Rognes, Torbjørn and Caporaso, J. Gregory and Knight, Rob},
  title = {Open-source sequence clustering methods improve the state of the art},
  journal = {mSystems},
  year = {2016},
  volume = {1},
  number = {1},
  pages = {e00003-15},
  doi = {10.1128/mSystems.00003-15},
  note = {access: full_text (MB-01); type: peer reviewed}
}

@article{kozichDevelopmentDualindexSequencing2013,
  author = {Kozich, James J. and Westcott, Sarah L. and Baxter, Nielson T. and Highlander, Sarah K. and Schloss, Patrick D.},
  title = {Development of a dual-index sequencing strategy and curation pipeline for analyzing amplicon sequence data on the MiSeq Illumina sequencing platform},
  journal = {Applied and Environmental Microbiology},
  year = {2013},
  volume = {79},
  number = {17},
  pages = {5112-5120},
  doi = {10.1128/AEM.01043-13},
  note = {access: full_text (MB-01; critic: MB-01:C-065, C-073..076, open full text could not be confirmed); type: peer reviewed}
}

@article{kumarAnalysisCorrectionCompositional2018,
  author = {Kumar, M. Senthil and Slud, Eric V. and Okrah, Kwame and Hicks, Stephanie C. and Hannenhalli, Sridhar and Corrada Bravo, Héctor},
  title = {Analysis and correction of compositional bias in sparse sequencing count data},
  journal = {BMC Genomics},
  year = {2018},
  volume = {19},
  pages = {799},
  doi = {10.1186/s12864-018-5160-5},
  note = {access: abstract_only (MB-01); type: peer reviewed}
}

@article{larosaHypothesisTestingPower2012,
  author = {La Rosa, Patricio S. and Brooks, J. Paul and Deych, Elena and Boone, Edward L. and Edwards, David J. and Wang, Qin and Sodergren, Erica and Weinstock, George and Shannon, William D.},
  title = {Hypothesis testing and power calculations for taxonomic-based human microbiome data},
  journal = {PLOS ONE},
  year = {2012},
  volume = {7},
  number = {12},
  pages = {e52078},
  doi = {10.1371/journal.pone.0052078},
  note = {access: full_text (MB-01); type: peer reviewed}
}

@article{laursenGenomicGCcontentAffects2017,
  author = {Laursen, Martin F. and Dalgaard, Marlene D. and Bahl, Martin I.},
  title = {Genomic GC-content affects the accuracy of 16S rRNA gene sequencing based microbial profiling due to PCR bias},
  journal = {Frontiers in Microbiology},
  year = {2017},
  volume = {8},
  pages = {1934},
  doi = {10.3389/fmicb.2017.01934},
  note = {access: full_text (MB-01; corrigendum 2022); type: peer reviewed}
}

@article{lennonHowWhereRelic2018,
  author = {Lennon, Jay T. and Muscarella, Mario E. and Placella, Sarah A. and Lehmkuhl, Brent K.},
  title = {How, when, and where relic DNA affects microbial diversity},
  journal = {mBio},
  year = {2018},
  volume = {9},
  number = {3},
  pages = {e00637-18},
  doi = {10.1128/mBio.00637-18},
  note = {access: full_text (MB-01), abstract_only (MB-02); type: peer reviewed; cited as: MB-02 [78]}
}

@article{linAnalysisCompositionsMicrobiomes2020,
  author = {Lin, Huang and Peddada, Shyamal Das},
  title = {Analysis of compositions of microbiomes with bias correction},
  journal = {Nature Communications},
  year = {2020},
  volume = {11},
  pages = {3514},
  doi = {10.1038/s41467-020-17041-7},
  note = {access: abstract_only (MB-01; makers' claims); type: peer reviewed}
}

@article{linTowardsQuantitativeMicrobiome2019,
  author = {Lin, Yajuan and Gifford, Scott and Ducklow, Hugh and Schofield, Oscar and Cassar, Nicolas},
  title = {Towards quantitative microbiome community profiling using internal standards},
  journal = {Applied and Environmental Microbiology},
  year = {2019},
  volume = {85},
  number = {5},
  pages = {e02634-18},
  doi = {10.1128/AEM.02634-18},
  note = {access: full_text (MB-01; critic: MB-01:C-065, C-073..076, open full text could not be confirmed); type: peer reviewed}
}

@article{lingBatchEffectsRemoval2022,
  author = {Ling, Wodan and Lu, Jiuyao and Zhao, Ni and Lulla, Anju and Plantinga, Anna M. and Fu, Weijia and Zhang, Angela and Liu, Hongjiao and Song, Hoseung and Li, Zhigang and Chen, Jun and Randolph, Timothy W. and Koay, Wei Li A. and White, James R. and Launer, Lenore J. and Fodor, Anthony A. and Meyer, Katie A. and Wu, Michael C.},
  title = {Batch effects removal for microbiome data via conditional quantile regression},
  journal = {Nature Communications},
  year = {2022},
  volume = {13},
  pages = {5418},
  doi = {10.1038/s41467-022-33071-9},
  note = {access: abstract_only (MB-01; makers' claims); type: peer reviewed}
}

@article{llorensricoBenchmarkingMicrobiomeTransformations2021,
  author = {Lloréns-Rico, Verónica and Vieira-Silva, Sara and Gonçalves, Pedro J. and Falony, Gwen and Raes, Jeroen},
  title = {Benchmarking microbiome transformations favors experimental quantitative approaches to address compositionality and sampling depth biases},
  journal = {Nature Communications},
  year = {2021},
  volume = {12},
  pages = {3562},
  doi = {10.1038/s41467-021-23821-6},
  note = {access: full_text (MB-01); type: peer reviewed}
}

@article{loucaCorrecting16SRRNA2018,
  author = {Louca, Stilianos and Doebeli, Michael and Parfrey, Laura Wegener},
  title = {Correcting for 16S rRNA gene copy numbers in microbiome surveys remains an unsolved problem},
  journal = {Microbiome},
  year = {2018},
  volume = {6},
  pages = {41},
  doi = {10.1186/s40168-018-0420-9},
  note = {access: full_text (MB-01), full_text (MB-02); type: peer reviewed; cited as: MB-02 [30]}
}

@article{lundbergPracticalInnovationsHighthroughput2013,
  author = {Lundberg, Derek S. and Yourstone, Scott and Mieczkowski, Piotr and Jones, Corbin D. and Dangl, Jeffery L.},
  title = {Practical innovations for high-throughput amplicon sequencing},
  journal = {Nature Methods},
  year = {2013},
  volume = {10},
  number = {10},
  pages = {999-1002},
  doi = {10.1038/nmeth.2634},
  note = {access: abstract_only (MB-01; makers' claims); type: peer reviewed}
}

@article{lundinWhichSequencingDepth2012,
  author = {Lundin, Daniel and Severin, Ina and Logue, Jürg Brendan and Östman, Örjan and Andersson, Anders F. and Lindström, Eva S.},
  title = {{Which sequencing depth is sufficient to describe patterns in bacterial alpha- and beta-diversity?}},
  year = {2012},
  doi = {10.1111/j.1758-2229.2012.00345.x},
  note = {access: abstract_only (MB-01); type: peer reviewed},
  journal = {Environmental Microbiology Reports},
  volume = {4},
  number = {3},
  pages = {367-372}
}

@article{mandalAnalysisCompositionMicrobiomes2015,
  author = {Mandal, Siddhartha and Van Treuren, Will and White, Richard A. and Eggesbø, Merete and Knight, Rob and Peddada, Shyamal D.},
  title = {Analysis of composition of microbiomes: a novel method for studying microbial composition},
  journal = {Microbial Ecology in Health and Disease},
  year = {2015},
  volume = {26},
  pages = {27663},
  doi = {10.3402/mehd.v26.27663},
  note = {access: abstract_only (MB-01; makers' claims); type: peer reviewed}
}

@article{marioniRNAseqAssessmentTechnical2008,
  author = {Marioni, John C. and Mason, Christopher E. and Mane, Shrikant M. and Stephens, Matthew and Gilad, Yoav},
  title = {RNA-seq: an assessment of technical reproducibility and comparison with gene expression arrays},
  journal = {Genome Research},
  year = {2008},
  volume = {18},
  number = {9},
  pages = {1509-1517},
  doi = {10.1101/gr.079558.108},
  note = {access: full_text (MB-01; INDIRECT); type: peer reviewed}
}

@article{marizzoniComparisonBioinformaticsPipelines2020,
  author = {Marizzoni, Moira and Gurry, Thomas and Provasi, Stefania and Greub, Gilbert and Lopizzo, Nicola and Ribaldi, Federica and Festari, Cristina and Mazzelli, Monica and Mombelli, Elisa and Salvatore, Marco and Mirabelli, Peppino and Franzese, Monica and Soricelli, Andrea and Frisoni, Giovanni B. and Cattaneo, Annamaria},
  title = {Comparison of bioinformatics pipelines and operating systems for the analyses of 16S rRNA gene amplicon sequences in human fecal samples},
  journal = {Frontiers in Microbiology},
  year = {2020},
  volume = {11},
  pages = {1262},
  doi = {10.3389/fmicb.2020.01262},
  note = {access: full_text (MB-01); type: peer reviewed}
}

@article{marotzTriplicatePCRReactions2019,
  author = {Marotz, Clarisse and Sharma, Amnon and Humphrey, Greg and Gottel, Neil and Daum, Christopher and Gilbert, Jack A. and Eloe-Fadrosh, Emiley and Knight, Rob},
  title = {Triplicate PCR reactions for 16S rRNA gene amplicon sequencing are unnecessary},
  journal = {BioTechniques},
  year = {2019},
  volume = {67},
  number = {1},
  pages = {29-32},
  doi = {10.2144/btn-2018-0192},
  note = {access: abstract_only (MB-01; critic: MB-01:C-080, an open PMC copy exists, PMC7030937); type: peer reviewed}
}

@article{martinModelingMicrobialAbundances2020,
  author = {Martin, Bryan D. and Witten, Daniela and Willis, Amy D.},
  title = {Modeling microbial abundances and dysbiosis with beta-binomial regression},
  journal = {The Annals of Applied Statistics},
  year = {2020},
  volume = {14},
  number = {1},
  pages = {94-115},
  doi = {10.1214/19-AOAS1283},
  note = {access: abstract_only (MB-01; makers' claims); type: peer reviewed}
}

@article{martinlaurentDNAExtractionSoils2001,
  author = {Martin-Laurent, Fabrice and Philippot, Laurent and Hallet, Sabine and Chaussod, Rémi and Germon, Jean-Claude and Soulas, Guy and Catroux, Gérard},
  title = {DNA extraction from soils: old bias for new microbial diversity analysis methods},
  journal = {Applied and Environmental Microbiology},
  year = {2001},
  volume = {67},
  number = {5},
  pages = {2354-2359},
  doi = {10.1128/AEM.67.5.2354-2359.2001},
  note = {access: abstract_only (MB-01); type: peer reviewed}
}

@article{mcknightMethodsNormalizingMicrobiome2019,
  author = {McKnight, Donald T. and Huerlimann, Roger and Bower, Deborah S. and Schwarzkopf, Lin and Alford, Ross A. and Zenger, Kyall R.},
  title = {Methods for normalizing microbiome data: an ecological perspective},
  journal = {Methods in Ecology and Evolution},
  year = {2019},
  volume = {10},
  number = {3},
  pages = {389-400},
  doi = {10.1111/2041-210X.13115},
  note = {access: abstract_only (MB-01); type: peer reviewed}
}

@article{mclarenConsistentCorrectableBias2019,
  author = {McLaren, Michael R. and Willis, Amy D. and Callahan, Benjamin J.},
  title = {Consistent and correctable bias in metagenomic sequencing experiments},
  journal = {eLife},
  year = {2019},
  volume = {8},
  pages = {e46923},
  doi = {10.7554/eLife.46923},
  note = {access: full_text (MB-01; re-opened by the synthesis agent), abstract_only (MB-02; critic: MB-02:C-077, cited for a comparison of bias magnitudes the abstract does not contain); type: peer reviewed; cited as: MB-02 [35]}
}

@misc{mclarenImplicationsTaxonomicBias2022,
  author = {McLaren, Michael R. and Nearing, Jacob T. and Willis, Amy D. and Lloyd, Karen G. and Callahan, Benjamin J.},
  title = {Implications of taxonomic bias for microbial differential-abundance analysis},
  year = {2022},
  doi = {10.1101/2022.08.19.504330},
  note = {access: abstract_only (MB-01); type: PREPRINT},
  howpublished = {bioRxiv 2022.08.19.504330}
}

@article{mcmurdieWasteNotWant2014,
  author = {McMurdie, Paul J. and Holmes, Susan},
  title = {Waste not, want not: why rarefying microbiome data is inadmissible},
  journal = {PLOS Computational Biology},
  year = {2014},
  volume = {10},
  number = {4},
  pages = {e1003531},
  doi = {10.1371/journal.pcbi.1003531},
  note = {access: full_text (MB-01); type: peer reviewed}
}

@article{minichQuantifyingUnderstandingWelltowell2019,
  author = {Minich, Jeremiah J. and Sanders, Jon G. and Amir, Amnon and Humphrey, Greg and Gilbert, Jack A. and Knight, Rob},
  title = {Quantifying and understanding well-to-well contamination in microbiome research},
  journal = {mSystems},
  year = {2019},
  volume = {4},
  number = {4},
  pages = {e00186-19},
  doi = {10.1128/mSystems.00186-19},
  note = {access: full_text (MB-01); type: peer reviewed}
}

@article{mortonEstablishingMicrobialComposition2019,
  author = {Morton, James T. and Marotz, Clarisse and Washburne, Alex and Silverman, Justin and Zaramela, Livia S. and Edlund, Anna and Zengler, Karsten and Knight, Rob},
  title = {Establishing microbial composition measurement standards with reference frames},
  journal = {Nature Communications},
  year = {2019},
  volume = {10},
  pages = {2719},
  doi = {10.1038/s41467-019-10656-5},
  note = {access: abstract_only (MB-01); type: peer reviewed}
}

@article{muraliIDTAXANovelApproach2018,
  author = {Murali, Adithya and Bhargava, Aniruddha and Wright, Erik S.},
  title = {IDTAXA: a novel approach for accurate taxonomic classification of microbiome sequences},
  journal = {Microbiome},
  year = {2018},
  volume = {6},
  pages = {140},
  doi = {10.1186/s40168-018-0521-5},
  note = {access: full_text (MB-01; developer claims); type: peer reviewed}
}

@article{nearingDenoisingDenoisersIndependent2018,
  author = {Nearing, Jacob T. and Douglas, Gavin M. and Comeau, André M. and Langille, Morgan G. I.},
  title = {Denoising the Denoisers: an independent evaluation of microbiome sequence error-correction approaches},
  journal = {PeerJ},
  year = {2018},
  volume = {6},
  pages = {e5364},
  doi = {10.7717/peerj.5364},
  note = {access: full_text (MB-01); type: peer reviewed}
}

@article{nearingMicrobiomeDifferentialAbundance2022,
  author = {Nearing, Jacob T. and Douglas, Gavin M. and Hayes, Molly G. and MacDonald, Jocelyn and Desai, Dhwani K. and Allward, Nicole and Jones, Casey M. A. and Wright, Robyn J. and Dhanani, Akhilesh S. and Comeau, André M. and Langille, Morgan G. I.},
  title = {Microbiome differential abundance methods produce different results across 38 datasets},
  journal = {Nature Communications},
  year = {2022},
  volume = {13},
  pages = {342},
  doi = {10.1038/s41467-022-28034-z},
  note = {access: full_text (MB-01); type: peer reviewed}
}

@article{nemergutDecreasesAverageBacterial2015,
  author = {Nemergut, Diana R. and Knelman, Joseph E. and Ferrenberg, Scott and Bilinski, Teresa and Melbourne, Brett and Jiang, Lin and Violle, Cyrille and Darcy, John L. and Prest, Tiffany and Schmidt, Steven K. and Townsend, Alan R.},
  title = {Decreases in average bacterial community rRNA operon copy number during succession},
  journal = {The ISME Journal},
  year = {2016},
  volume = {10},
  number = {5},
  pages = {1147-1156},
  doi = {10.1038/ismej.2015.191},
  note = {access: full_text (MB-01); type: peer reviewed}
}

@article{paradaEveryBaseMatters2016,
  author = {Parada, Alma E. and Needham, David M. and Fuhrman, Jed A.},
  title = {Every base matters: assessing small subunit rRNA primers for marine microbiomes with mock communities, time series and global field samples},
  journal = {Environmental Microbiology},
  year = {2016},
  volume = {18},
  number = {5},
  pages = {1403-1414},
  doi = {10.1111/1462-2920.13023},
  note = {access: abstract_only (MB-01); type: peer reviewed}
}

@article{peltoElementaryMethodsProvide2025,
  author = {Pelto, Juho and Auranen, Kari and Kujala, Janne V. and Lahti, Leo},
  title = {Elementary methods provide more replicable results in microbial differential abundance analysis},
  journal = {Briefings in Bioinformatics},
  year = {2025},
  volume = {26},
  number = {2},
  pages = {bbaf130},
  doi = {10.1093/bib/bbaf130},
  note = {access: abstract_only (MB-01; DOI checked by the synthesis agent); type: peer reviewed}
}

@article{pentonSizeMattersAssessing2016,
  author = {Penton, C. Ryan and Gupta, Vadakattu V. S. R. and Yu, Julian and Tiedje, James M.},
  title = {Size matters: assessing optimum soil sample size for fungal and bacterial community structure analyses using high throughput sequencing of rRNA gene amplicons},
  journal = {Frontiers in Microbiology},
  year = {2016},
  volume = {7},
  pages = {824},
  doi = {10.3389/fmicb.2016.00824},
  note = {access: full_text (MB-01); type: peer reviewed}
}

@article{pintoPCRBiasesDistort2012,
  author = {Pinto, Ameet J. and Raskin, Lutgarde},
  title = {PCR biases distort bacterial and archaeal community structure in pyrosequencing datasets},
  journal = {PLOS ONE},
  year = {2012},
  volume = {7},
  number = {8},
  pages = {e43093},
  doi = {10.1371/journal.pone.0043093},
  note = {access: full_text (MB-01); type: peer reviewed}
}

@article{polzBiasTemplatetoproductRatios1998,
  author = {Polz, Martin F. and Cavanaugh, Colleen M.},
  title = {Bias in template-to-product ratios in multitemplate PCR},
  journal = {Applied and Environmental Microbiology},
  year = {1998},
  volume = {64},
  number = {10},
  pages = {3724-3730},
  doi = {10.1128/AEM.64.10.3724-3730.1998},
  note = {access: abstract_only (MB-01); type: peer reviewed}
}

@article{prodanComparingBioinformaticPipelines2020,
  author = {Prodan, Andrei and Tremaroli, Valentina and Brolin, Harald and Zwinderman, Aeilko H. and Nieuwdorp, Max and Levin, Evgeni},
  title = {Comparing bioinformatic pipelines for microbial 16S rRNA amplicon sequencing},
  journal = {PLOS ONE},
  year = {2020},
  volume = {15},
  number = {1},
  pages = {e0227434},
  doi = {10.1371/journal.pone.0227434},
  note = {access: full_text (MB-01); type: peer reviewed}
}

@article{propsAbsoluteQuantificationMicrobial2016,
  author = {Props, Ruben and Kerckhof, Frederiek-Maarten and Rubbens, Peter and De Vrieze, Jo and Hernandez Sanabria, Emma and Waegeman, Willem and Monsieurs, Pieter and Hammes, Frederik and Boon, Nico},
  title = {Absolute quantification of microbial taxon abundances},
  journal = {The ISME Journal},
  year = {2017},
  volume = {11},
  number = {2},
  pages = {584-587},
  doi = {10.1038/ismej.2016.117},
  note = {access: abstract_only (MB-01), abstract_only (MB-02); type: peer reviewed; cited as: MB-02 [83]}
}

@article{reitmeierHandlingSpuriousSequences2021,
  author = {Reitmeier, Sandra and Hitch, Thomas C. A. and Treichel, Nicole and Fikas, Nikolaos and Hausmann, Bela and Ramer-Tait, Amanda E. and Neuhaus, Klaus and Berry, David and Haller, Dirk and Lagkouvardos, Ilias and Clavel, Thomas},
  title = {Handling of spurious sequences affects the outcome of high-throughput 16S rRNA gene amplicon profiling},
  journal = {ISME Communications},
  year = {2021},
  volume = {1},
  number = {1},
  pages = {31},
  doi = {10.1038/s43705-021-00033-z},
  note = {access: full_text (MB-01; DOI checked by the synthesis agent); type: peer reviewed}
}

@article{robinsonScalingNormalizationMethod2010,
  author = {Robinson, Mark D. and Oshlack, Alicia},
  title = {A scaling normalization method for differential expression analysis of RNA-seq data},
  journal = {Genome Biology},
  year = {2010},
  volume = {11},
  number = {3},
  pages = {R25},
  doi = {10.1186/gb-2010-11-3-r25},
  note = {access: abstract_only (MB-01; INDIRECT); type: peer reviewed}
}

@article{rollerExploitingRRNAOperon2016,
  author = {Roller, Benjamin R. K. and Stoddard, Steven F. and Schmidt, Thomas M.},
  title = {Exploiting rRNA operon copy number to investigate bacterial reproductive strategies},
  journal = {Nature Microbiology},
  year = {2016},
  volume = {1},
  number = {11},
  pages = {16160},
  doi = {10.1038/nmicrobiol.2016.160},
  note = {access: abstract_only (MB-01), abstract_only (MB-02); type: peer reviewed; cited as: MB-02 [10]}
}

@article{rubinInvestigatingImpactStorage2013,
  author = {Rubin, Benjamin E. R. and Gibbons, Sean M. and Kennedy, Suzanne and Hampton-Marcell, Jarrad and Owens, Sarah and Gilbert, Jack A.},
  title = {Investigating the impact of storage conditions on microbial community composition in soil samples},
  journal = {PLOS ONE},
  year = {2013},
  volume = {8},
  number = {7},
  pages = {e70460},
  doi = {10.1371/journal.pone.0070460},
  note = {access: full_text (MB-01); type: peer reviewed}
}

@article{salterReagentLaboratoryContamination2014,
  author = {Salter, Susannah J. and Cox, Michael J. and Turek, Elena M. and Calus, Szymon T. and Cookson, William O. and Moffatt, Miriam F. and Turner, Paul and Parkhill, Julian and Loman, Nicholas J. and Walker, Alan W.},
  title = {Reagent and laboratory contamination can critically impact sequence-based microbiome analyses},
  journal = {BMC Biology},
  year = {2014},
  volume = {12},
  pages = {87},
  doi = {10.1186/s12915-014-0087-z},
  note = {access: full_text (MB-01); type: peer reviewed}
}

@article{schirmerInsightBiasesSequencing2015,
  author = {Schirmer, Melanie and Ijaz, Umer Z. and D'Amore, Rosalinda and Hall, Neil and Sloan, William T. and Quince, Christopher},
  title = {Insight into biases and sequencing errors for amplicon sequencing with the Illumina MiSeq platform},
  journal = {Nucleic Acids Research},
  year = {2015},
  volume = {43},
  number = {6},
  pages = {e37},
  doi = {10.1093/nar/gku1341},
  note = {access: full_text (MB-01); type: peer reviewed}
}

@article{schlossAmpliconSequenceVariants2021,
  author = {Schloss, Patrick D.},
  title = {Amplicon sequence variants artificially split bacterial genomes into separate clusters},
  journal = {mSphere},
  year = {2021},
  volume = {6},
  number = {4},
  pages = {e00191-21},
  doi = {10.1128/mSphere.00191-21},
  note = {access: full_text (MB-01); type: peer reviewed}
}

@article{schlossWasteNotWant2024,
  author = {Schloss, Patrick D.},
  title = {Waste not, want not: revisiting the analysis that called into question the practice of rarefaction},
  journal = {mSphere},
  year = {2024},
  volume = {9},
  number = {1},
  pages = {e00355-23},
  doi = {10.1128/msphere.00355-23},
  note = {access: full_text (MB-01); type: peer reviewed}
}

@article{schlossRarefactionCurrentlyBest2024,
  author = {Schloss, Patrick D.},
  title = {Rarefaction is currently the best approach to control for uneven sequencing effort in amplicon sequence analyses},
  journal = {mSphere},
  year = {2024},
  volume = {9},
  number = {2},
  pages = {e00354-23},
  doi = {10.1128/msphere.00354-23},
  note = {access: full_text (MB-01; re-opened by the synthesis agent; DOI checked); type: peer reviewed}
}

@article{schnellTagJumpsIlluminated2015,
  author = {Schnell, Ida Bærholm and Bohmann, Kristine and Gilbert, M. Thomas P.},
  title = {Tag jumps illuminated: reducing sequence-to-sample misidentifications in metabarcoding studies},
  journal = {Molecular Ecology Resources},
  year = {2015},
  volume = {15},
  number = {6},
  pages = {1289-1303},
  doi = {10.1111/1755-0998.12402},
  note = {access: abstract_only (MB-01; INDIRECT); type: peer reviewed}
}

@article{sheltonTowardQuantitativeMetabarcoding2023,
  author = {Shelton, Andrew Olaf and Gold, Zachary J. and Jensen, Alexander J. and D'Agnese, Erin and Andruszkiewicz Allan, Elizabeth and Van Cise, Amy and Gallego, Ramón and Ramón-Laca, Ana and Garber-Yonts, Maya and Parsons, Kim and Kelly, Ryan P.},
  title = {Toward quantitative metabarcoding},
  journal = {Ecology},
  year = {2023},
  volume = {104},
  number = {2},
  pages = {e3906},
  doi = {10.1002/ecy.3906},
  note = {access: abstract_only (MB-01; INDIRECT); type: peer reviewed}
}

@article{shoemakerMacroecologicalTheoryMicrobial2017,
  author = {Shoemaker, William R. and Locey, Kenneth J. and Lennon, Jay T.},
  title = {A macroecological theory of microbial biodiversity},
  journal = {Nature Ecology & Evolution},
  year = {2017},
  volume = {1},
  number = {5},
  pages = {0107},
  doi = {10.1038/s41559-017-0107},
  note = {access: abstract_only (MB-01; per lab angle; DOI checked by the synthesis agent), abstract_only (MB-02); type: peer reviewed; cited as: MB-02 [70]; conflict in MB-01: its Sources not obtained list says only a web-search engine summary was seen, not used as a finding}
}

@article{silvermanDynamicLinearModels2018,
  author = {Silverman, Justin D. and Durand, Heather K. and Bloom, Rachael J. and Mukherjee, Sayan and David, Lawrence A.},
  title = {Dynamic linear models guide design and analysis of microbiota studies within artificial human guts},
  journal = {Microbiome},
  year = {2018},
  volume = {6},
  pages = {202},
  doi = {10.1186/s40168-018-0584-3},
  note = {access: full_text (MB-01; DOI checked by the synthesis agent); type: peer reviewed}
}

@article{silvermanNaughtAllZeros2020,
  author = {Silverman, Justin D. and Roche, Kimberly and Mukherjee, Sayan and David, Lawrence A.},
  title = {Naught all zeros in sequence count data are the same},
  journal = {Computational and Structural Biotechnology Journal},
  year = {2020},
  volume = {18},
  pages = {2789-2798},
  doi = {10.1016/j.csbj.2020.09.014},
  note = {access: abstract_only (MB-01); type: peer reviewed}
}

@article{silvermanMeasuringMitigatingPCR2021,
  author = {Silverman, Justin D. and Bloom, Rachael J. and Jiang, Sharon and Durand, Heather K. and Dallow, Eric and Mukherjee, Sayan and David, Lawrence A.},
  title = {Measuring and mitigating PCR bias in microbiota datasets},
  journal = {PLOS Computational Biology},
  year = {2021},
  volume = {17},
  number = {7},
  pages = {e1009113},
  doi = {10.1371/journal.pcbi.1009113},
  note = {access: full_text (MB-01; DOI checked by the synthesis agent); type: peer reviewed}
}

@article{sinhaAssessmentVariationMicrobial2017,
  author = {{The Microbiome Quality Control Project Consortium} and Sinha, Rashmi and Abu-Ali, Galeb and Vogtmann, Emily and Fodor, Anthony A. and Ren, Boyu and Amir, Amnon and Schwager, Emma and Crabtree, Jonathan and Ma, Siyuan and Abnet, Christian C. and Knight, Rob and White, Owen and Huttenhower, Curtis},
  title = {Assessment of variation in microbial community amplicon sequencing by the Microbiome Quality Control (MBQC) project consortium},
  journal = {Nature Biotechnology},
  year = {2017},
  volume = {35},
  number = {11},
  pages = {1077-1086},
  doi = {10.1038/nbt.3981},
  note = {access: full_text (MB-01; per bioinformatics angle); type: peer reviewed; author order corrected (critic: MB-01:C-094; Crossref lists the consortium first, the note placed it after Siyuan Ma)}
}

@article{siposEffectPrimerMismatch2007,
  author = {Sipos, Rita and Székely, Anna J. and Palatinszky, Márton and Révész, Sára and Márialigeti, Károly and Nikolausz, Marcell},
  title = {Effect of primer mismatch, annealing temperature and PCR cycle number on 16S rRNA gene-targetting bacterial community analysis},
  journal = {FEMS Microbiology Ecology},
  year = {2007},
  volume = {60},
  number = {2},
  pages = {341-350},
  doi = {10.1111/j.1574-6941.2007.00283.x},
  note = {access: abstract_only (MB-01); type: peer reviewed}
}

@article{smetsMethodSimultaneousMeasurement2016,
  author = {Smets, Wenke and Leff, Jonathan W. and Bradford, Mark A. and McCulley, Rebecca L. and Lebeer, Sarah and Fierer, Noah},
  title = {A method for simultaneous measurement of soil bacterial abundances and community composition via 16S rRNA gene sequencing},
  journal = {Soil Biology and Biochemistry},
  year = {2016},
  volume = {96},
  pages = {145-151},
  doi = {10.1016/j.soilbio.2016.02.003},
  note = {access: abstract_only (MB-01; per lab angle); type: peer reviewed; conflict in MB-01: also in its Sources not obtained list (Crossref no abstract, Europe PMC not indexed)}
}

@article{smithSequenceDepthNot2014,
  author = {Smith, Dylan P. and Peay, Kabir G.},
  title = {Sequence depth, not PCR replication, improves ecological inference from next generation DNA sequencing},
  journal = {PLOS ONE},
  year = {2014},
  volume = {9},
  number = {2},
  pages = {e90234},
  doi = {10.1371/journal.pone.0090234},
  note = {access: full_text (MB-01; INDIRECT, ITS); type: peer reviewed}
}

@article{songPreservationMethodsDiffer2016,
  author = {Song, Se Jin and Amir, Amnon and Metcalf, Jessica L. and Amato, Katherine R. and Xu, Zhenjiang Zech and Humphrey, Greg and Knight, Rob},
  title = {Preservation methods differ in fecal microbiome stability, affecting suitability for field studies},
  journal = {mSystems},
  year = {2016},
  volume = {1},
  number = {3},
  pages = {e00021-16},
  doi = {10.1128/mSystems.00021-16},
  note = {access: full_text (MB-01); type: peer reviewed}
}

@article{stammlerAdjustingMicrobiomeProfiles2016,
  author = {Stämmler, Frank and Gläsner, Joachim and Hiergeist, Andreas and Holler, Ernst and Weber, Daniela and Oefner, Peter J. and Gessner, André and Spang, Rainer},
  title = {Adjusting microbiome profiles for differences in microbial load by spike-in bacteria},
  journal = {Microbiome},
  year = {2016},
  volume = {4},
  pages = {28},
  doi = {10.1186/s40168-016-0175-0},
  note = {access: full_text (MB-01; per lab angle); type: peer reviewed}
}

@article{starke16SRRNAGene2020,
  author = {Starke, Robert and Pylro, Victor Satler and Morais, Daniel Kumazawa},
  title = {16S rRNA gene copy number normalization does not provide more reliable conclusions in metataxonomic surveys},
  journal = {Microbial Ecology},
  year = {2021},
  volume = {81},
  number = {2},
  pages = {535-539},
  doi = {10.1007/s00248-020-01586-7},
  note = {access: full_text (MB-01), full_text (MB-02; year given as 2021; online 2020); type: peer reviewed; cited as: MB-02 [32]}
}

@article{stoddardRrnDBImprovedTools2015,
  author = {Stoddard, Steven F. and Smith, Byron J. and Hein, Robert and Roller, Benjamin R. K. and Schmidt, Thomas M.},
  title = {rrnDB: improved tools for interpreting rRNA gene abundance in bacteria and archaea and a new foundation for future development},
  journal = {Nucleic Acids Research},
  year = {2015},
  volume = {43},
  number = {D1},
  pages = {D593-D598},
  doi = {10.1093/nar/gku1201},
  note = {access: full_text (MB-01), full_text (MB-02; year given as 2015; online 2014); type: peer reviewed database paper; cited as: MB-02 [3]}
}

@article{straubInterpretationsEnvironmentalMicrobial2020,
  author = {Straub, Daniel and Blackwell, Nia and Langarica-Fuentes, Adrian and Peltzer, Alexander and Nahnsen, Sven and Kleindienst, Sara},
  title = {Interpretations of environmental microbial community studies are biased by the selected 16S rRNA (gene) amplicon sequencing pipeline},
  journal = {Frontiers in Microbiology},
  year = {2020},
  volume = {11},
  pages = {550420},
  doi = {10.3389/fmicb.2020.550420},
  note = {access: full_text (MB-01); type: peer reviewed}
}

@article{suzukiBiasCausedTemplate1996,
  author = {Suzuki, Marcelino T. and Giovannoni, Stephen J.},
  title = {Bias caused by template annealing in the amplification of mixtures of 16S rRNA genes by PCR},
  journal = {Applied and Environmental Microbiology},
  year = {1996},
  volume = {62},
  number = {2},
  pages = {625-630},
  doi = {10.1128/aem.62.2.625-630.1996},
  note = {access: abstract_only (MB-01); type: peer reviewed}
}

@article{szeImpactDNAPolymerase2019,
  author = {Sze, Marc A. and Schloss, Patrick D.},
  title = {The impact of DNA polymerase and number of rounds of amplification in PCR on 16S rRNA gene sequence data},
  journal = {mSphere},
  year = {2019},
  volume = {4},
  number = {3},
  pages = {e00163-19},
  doi = {10.1128/mSphere.00163-19},
  note = {access: full_text (MB-01; re-opened by the synthesis agent); type: peer reviewed}
}

@article{thompsonCommunalCatalogueReveals2017,
  author = {Thompson, Luke R. and Sanders, Jon G. and McDonald, Daniel and Amir, Amnon and Ladau, Joshua and Locey, Kenneth J. and Prill, Robert J. and Tripathi, Anupriya and Gibbons, Sean M. and Ackermann, Gail and Navas-Molina, Jose A. and Janssen, Stefan and Kopylova, Evguenia and Vázquez-Baeza, Yoshiki and González, Antonio and Morton, James T. and Mirarab, Siavash and Xu, Zhenjiang Zech and Jiang, Lingjing and Haroon, Mohamed F. and Kanbar, Jad and Zhu, Qiyun and Song, Se Jin and Kosciolek, Tomasz and Bokulich, Nicholas A. and Lefler, Joshua and Brislawn, Colin J. and Humphrey, Gregory and Owens, Sarah M. and Hampton-Marcell, Jarrad and Berg-Lyons, Donna and McKenzie, Valerie and Fierer, Noah and Fuhrman, Jed A. and Clauset, Aaron and Stevens, Rick L. and Shade, Ashley and Pollard, Katherine S. and Goodwin, Kelly D. and Jansson, Janet K. and Gilbert, Jack A. and Knight, Rob and {The Earth Microbiome Project Consortium (consortium members as listed in the Crossref record)}},
  title = {A communal catalogue reveals Earth's multiscale microbial diversity},
  journal = {Nature},
  year = {2017},
  volume = {551},
  number = {7681},
  pages = {457-463},
  doi = {10.1038/nature24621},
  note = {access: full_text (MB-01); type: peer reviewed; incomplete: author (the note truncates the list at the consortium; critic: MB-01:C-095..097, Crossref lists several hundred named members)}
}

@article{thorsenLargescaleBenchmarkingReveals2016,
  author = {Thorsen, Jonathan and Brejnrod, Asker and Mortensen, Martin and Rasmussen, Morten A. and Stokholm, Jakob and Abu Al-Soud, Waleed and Sørensen, Søren and Bisgaard, Hans and Waage, Johannes},
  title = {Large-scale benchmarking reveals false discoveries and count transformation sensitivity in 16S rRNA gene amplicon data analysis methods used in microbiome studies},
  journal = {Microbiome},
  year = {2016},
  volume = {4},
  pages = {62},
  doi = {10.1186/s40168-016-0208-8},
  note = {access: abstract_only (MB-01); type: peer reviewed}
}

@article{tkaczAbsoluteQuantitationMicrobiota2018,
  author = {Tkacz, Andrzej and Hortala, Marion and Poole, Philip S.},
  title = {Absolute quantitation of microbiota abundance in environmental samples},
  journal = {Microbiome},
  year = {2018},
  volume = {6},
  pages = {110},
  doi = {10.1186/s40168-018-0491-7},
  note = {access: full_text (MB-01; per lab angle); type: peer reviewed}
}

@article{tourlousseSyntheticSpikeinStandards2016,
  author = {Tourlousse, Dieter M. and Yoshiike, Satowa and Ohashi, Akiko and Matsukura, Satoko and Noda, Naohiro and Sekiguchi, Yuji},
  title = {Synthetic spike-in standards for high-throughput 16S rRNA gene amplicon sequencing},
  journal = {Nucleic Acids Research},
  year = {2017},
  volume = {45},
  number = {4},
  pages = {e23},
  doi = {10.1093/nar/gkw984},
  note = {access: full_text (MB-01); type: peer reviewed}
}

@article{vandeputteQuantitativeMicrobiomeProfiling2017,
  author = {Vandeputte, Doris and Kathagen, Gunter and D'hoe, Kevin and Vieira-Silva, Sara and Valles-Colomer, Mireia and Sabino, João and Wang, Jun and Tito, Raul Y. and De Commer, Lindsey and Darzi, Youssef and Vermeire, Séverine and Falony, Gwen and Raes, Jeroen},
  title = {Quantitative microbiome profiling links gut community variation to microbial load},
  journal = {Nature},
  year = {2017},
  volume = {551},
  number = {7681},
  pages = {507-511},
  doi = {10.1038/nature24460},
  note = {access: abstract_only (MB-01); type: peer reviewed}
}

@article{vetrovskyVariability16SRRNA2013,
  author = {Větrovský, Tomáš and Baldrian, Petr},
  title = {The variability of the 16S rRNA gene in bacterial genomes and its consequences for bacterial community analyses},
  journal = {PLOS ONE},
  year = {2013},
  volume = {8},
  number = {2},
  pages = {e57923},
  doi = {10.1371/journal.pone.0057923},
  note = {access: full_text (MB-01), full_text (MB-02); type: peer reviewed; cited as: MB-02 [6]}
}

@article{waltersImprovedBacterial16S2016,
  author = {Walters, William and Hyde, Embriette R. and Berg-Lyons, Donna and Ackermann, Gail and Humphrey, Greg and Parada, Alma and Gilbert, Jack A. and Jansson, Janet K. and Caporaso, J. Gregory and Fuhrman, Jed A. and Apprill, Amy and Knight, Rob},
  title = {Improved bacterial 16S rRNA gene (V4 and V4-5) and fungal internal transcribed spacer marker gene primers for microbial community surveys},
  journal = {mSystems},
  year = {2016},
  volume = {1},
  number = {1},
  pages = {e00009-15},
  doi = {10.1128/mSystems.00009-15},
  note = {access: full_text (MB-01); type: peer reviewed}
}

@article{weissNormalizationMicrobialDifferential2017,
  author = {Weiss, Sophie and Xu, Zhenjiang Zech and Peddada, Shyamal and Amir, Amnon and Bittinger, Kyle and Gonzalez, Antonio and Lozupone, Catherine and Zaneveld, Jesse R. and Vázquez-Baeza, Yoshiki and Birmingham, Amanda and Hyde, Embriette R. and Knight, Rob},
  title = {Normalization and microbial differential abundance strategies depend upon data characteristics},
  journal = {Microbiome},
  year = {2017},
  volume = {5},
  pages = {27},
  doi = {10.1186/s40168-017-0237-y},
  note = {access: full_text (MB-01); type: peer reviewed}
}

@article{wenEvaluationReproducibilityAmplicon2017,
  author = {Wen, Chongqing and Wu, Liyou and Qin, Yujia and Van Nostrand, Joy D. and Ning, Daliang and Sun, Bo and Xue, Kai and Liu, Feifei and Deng, Ye and Liang, Yuting and Zhou, Jizhong},
  title = {Evaluation of the reproducibility of amplicon sequencing with Illumina MiSeq platform},
  journal = {PLOS ONE},
  year = {2017},
  volume = {12},
  number = {4},
  pages = {e0176716},
  doi = {10.1371/journal.pone.0176716},
  note = {access: full_text (MB-01); type: peer reviewed}
}

@article{willisRarefactionAlphaDiversity2019,
  author = {Willis, Amy D.},
  title = {Rarefaction, alpha diversity, and statistics},
  journal = {Frontiers in Microbiology},
  year = {2019},
  volume = {10},
  pages = {2407},
  doi = {10.3389/fmicb.2019.02407},
  note = {access: full_text (MB-01); type: peer reviewed perspective}
}

@article{willisEstimatingDiversityFrequency2015,
  author = {Willis, Amy and Bunge, John},
  title = {Estimating diversity via frequency ratios},
  journal = {Biometrics},
  year = {2015},
  volume = {71},
  number = {4},
  pages = {1042-1049},
  doi = {10.1111/biom.12332},
  note = {access: abstract_only (MB-01; makers' claims); type: peer reviewed}
}

@article{willisImprovedDetectionChanges2017,
  author = {Willis, Amy and Bunge, John and Whitman, Thea},
  title = {Improved detection of changes in species richness in high diversity microbial communities},
  journal = {Journal of the Royal Statistical Society Series C: Applied Statistics},
  year = {2017},
  volume = {66},
  number = {5},
  pages = {963-977},
  doi = {10.1111/rssc.12206},
  note = {access: abstract_only (MB-01; makers' claims); type: peer reviewed}
}

@article{willisEstimatingDiversityNetworked2022,
  author = {Willis, Amy D. and Martin, Bryan D.},
  title = {Estimating diversity in networked ecological communities},
  journal = {Biostatistics},
  year = {2022},
  volume = {23},
  number = {1},
  pages = {207-222},
  doi = {10.1093/biostatistics/kxaa015},
  note = {access: abstract_only (MB-01; makers' claims); type: peer reviewed}
}

@article{wirbelRealisticBenchmarkDifferential2024,
  author = {Wirbel, Jakob and Essex, Morgan and Forslund, Sofia Kirke and Zeller, Georg},
  title = {A realistic benchmark for differential abundance testing and confounder adjustment in human microbiome studies},
  journal = {Genome Biology},
  year = {2024},
  volume = {25},
  pages = {247},
  doi = {10.1186/s13059-024-03390-9},
  note = {access: full_text (MB-01); type: peer reviewed}
}

@article{wrightQualityFilteringIllumina2016,
  author = {Wright, Erik Scott and Vetsigian, Kalin Horen},
  title = {Quality filtering of Illumina index reads mitigates sample cross-talk},
  journal = {BMC Genomics},
  year = {2016},
  volume = {17},
  pages = {876},
  doi = {10.1186/s12864-016-3217-x},
  note = {access: full_text (MB-01; INDIRECT); type: peer reviewed}
}

@article{yangComprehensiveEvaluationMicrobial2022,
  author = {Yang, Lu and Chen, Jun},
  title = {A comprehensive evaluation of microbial differential abundance analysis methods: current status and potential solutions},
  journal = {Microbiome},
  year = {2022},
  volume = {10},
  pages = {130},
  doi = {10.1186/s40168-022-01320-0},
  note = {access: full_text (MB-01); type: peer reviewed}
}

@article{yehTaxonDisappearanceMicrobiome2018,
  author = {Yeh, Yi-Chun and Needham, David M. and Sieradzki, Ella T. and Fuhrman, Jed A.},
  title = {Taxon disappearance from microbiome analysis reinforces the value of mock communities as a standard in every sequencing run},
  journal = {mSystems},
  year = {2018},
  volume = {3},
  number = {3},
  pages = {e00023-18},
  doi = {10.1128/mSystems.00023-18},
  note = {access: full_text (MB-01); type: peer reviewed}
}

@article{zembAbsoluteQuantitationMicrobes2020,
  author = {Zemb, Olivier and Achard, Caroline S. and Hamelin, Jérôme and De Almeida, Marie-Léa and Gabinaud, Béatrice and Cauquil, Laurent and Verschuren, Lisanne M. G. and Godon, Jean-Jacques},
  title = {Absolute quantitation of microbes using 16S rRNA gene metabarcoding: a rapid normalization of relative abundances by quantitative PCR targeting a 16S rRNA gene spike-in standard},
  journal = {MicrobiologyOpen},
  year = {2020},
  volume = {9},
  number = {3},
  pages = {e977},
  doi = {10.1002/mbo3.977},
  note = {access: full_text (MB-01); type: peer reviewed}
}

@article{zhouReproducibilityQuantitationAmplicon2011,
  author = {Zhou, Jizhong and Wu, Liyou and Deng, Ye and Zhi, Xiaoyang and Jiang, Yi-Huei and Tu, Qichao and Xie, Jianping and Van Nostrand, Joy D. and He, Zhili and Yang, Yunfeng},
  title = {Reproducibility and quantitation of amplicon sequencing-based detection},
  journal = {The ISME Journal},
  year = {2011},
  volume = {5},
  number = {8},
  pages = {1303-1313},
  doi = {10.1038/ismej.2011.11},
  note = {access: abstract_only (critic: MB-01:C-073..076; the note said full_text, per statistics and bioinformatics angles; its figures 17.2%, 8.2% and 66.7-fold match the abstract) (MB-01), abstract_only (MB-02); type: peer reviewed; cited as: MB-02 [76]}
}

@article{zhouRandomSamplingProcess2013,
  author = {Zhou, Jizhong and Jiang, Yi-Huei and Deng, Ye and Shi, Zhou and Zhou, Benjamin Yamin and Xue, Kai and Wu, Liyou and He, Zhili and Yang, Yunfeng},
  title = {Random sampling process leads to overestimation of beta-diversity of microbial communities},
  journal = {mBio},
  year = {2013},
  volume = {4},
  number = {3},
  pages = {e00324-13},
  doi = {10.1128/mBio.00324-13},
  note = {access: full_text (MB-01); type: peer reviewed}
}

@article{klappenbachRrndbRibosomalRNA2001,
  author = {Klappenbach, Joel A. and Saxman, Paul R. and Cole, James R. and Schmidt, Thomas M.},
  title = {rrndb: the Ribosomal RNA Operon Copy Number Database},
  journal = {Nucleic Acids Research},
  year = {2001},
  volume = {29},
  number = {1},
  pages = {181-184},
  doi = {10.1093/nar/29.1.181},
  note = {access: abstract_only (MB-02); cited as: MB-02 [1]; Crossref lists only the first author, full list from Europe PMC and rrnDB (the note; critic: MB-02:C-095)}
}

@article{leeRrnDBDocumentingNumber2009,
  author = {Lee, Zarraz M.-P. and Bussema III, Carl and Schmidt, Thomas M.},
  title = {rrnDB: documenting the number of rRNA and tRNA genes in bacteria and archaea},
  journal = {Nucleic Acids Research},
  year = {2009},
  volume = {37},
  number = {Database issue},
  pages = {D489-D493},
  doi = {10.1093/nar/gkn689},
  note = {access: abstract_only (MB-02); cited as: MB-02 [2]; Crossref gives C. Bussema without III (critic: MB-02:C-096)}
}

@article{acinasDivergenceRedundancy16S2004,
  author = {Acinas, Silvia G. and Marcelino, Luisa A. and Klepac-Ceraj, Vanja and Polz, Martin F.},
  title = {Divergence and redundancy of 16S rRNA sequences in genomes with multiple rrn operons},
  journal = {Journal of Bacteriology},
  year = {2004},
  volume = {186},
  number = {9},
  pages = {2629-2635},
  doi = {10.1128/JB.186.9.2629-2635.2004},
  note = {access: abstract_only (MB-02); cited as: MB-02 [5]}
}

@article{brewerUnlinkedRRNAGenes2020,
  author = {Brewer, Tess E. and Albertsen, Mads and Edwards, Arwyn and Kirkegaard, Rasmus H. and Rocha, Eduardo P. C. and Fierer, Noah},
  title = {Unlinked rRNA genes are widespread among bacteria and archaea},
  journal = {The ISME Journal},
  year = {2020},
  volume = {14},
  number = {2},
  pages = {597-608},
  doi = {10.1038/s41396-019-0552-3},
  note = {access: abstract_only (MB-02); cited as: MB-02 [7]}
}

@article{sunIntragenomicHeterogeneity16S2013,
  author = {Sun, Dong-Lei and Jiang, Xuan and Wu, Qinglong L. and Zhou, Ning-Yi},
  title = {Intragenomic heterogeneity of 16S rRNA genes causes overestimation of prokaryotic diversity},
  journal = {Applied and Environmental Microbiology},
  year = {2013},
  volume = {79},
  number = {19},
  pages = {5962-5969},
  doi = {10.1128/AEM.01282-13},
  note = {access: abstract_only (MB-02); cited as: MB-02 [8]}
}

@article{pecoraroQuantificationPloidyProteobacteria2011,
  author = {Pecoraro, Vito and Zerulla, Karolin and Lange, Christian and Soppa, Jörg},
  title = {Quantification of ploidy in proteobacteria revealed the existence of monoploid, (mero-)oligoploid and polyploid species},
  journal = {PLoS ONE},
  year = {2011},
  volume = {6},
  number = {1},
  pages = {e16392},
  doi = {10.1371/journal.pone.0016392},
  note = {access: full_text (MB-02); cited as: MB-02 [11]}
}

@article{akerlundAnalysisCellSize1995,
  author = {Akerlund, T. and Nordström, K. and Bernander, R.},
  title = {Analysis of cell size and DNA content in exponentially growing and stationary-phase batch cultures of Escherichia coli},
  journal = {Journal of Bacteriology},
  year = {1995},
  volume = {177},
  number = {23},
  pages = {6791-6797},
  doi = {10.1128/jb.177.23.6791-6797.1995},
  note = {access: abstract_only (MB-02); cited as: MB-02 [12]}
}

@article{bottingerRegulatedPloidyBacillus2018,
  author = {Böttinger, Benjamin and Semmler, Florian and Zerulla, Karolin and Ludt, Katharina and Soppa, Jörg},
  title = {Regulated ploidy of Bacillus subtilis and three new isolates of Bacillus and Paenibacillus},
  journal = {FEMS Microbiology Letters},
  year = {2018},
  volume = {365},
  number = {4},
  pages = {fnx282},
  doi = {10.1093/femsle/fnx282},
  note = {access: abstract_only (MB-02); cited as: MB-02 [13]}
}

@article{breuertRegulatedPolyploidyHalophilic2006,
  author = {Breuert, Sebastian and Allers, Thorsten and Spohn, Gabi and Soppa, Jörg},
  title = {Regulated polyploidy in halophilic archaea},
  journal = {PLoS ONE},
  year = {2006},
  volume = {1},
  number = {1},
  pages = {e92},
  doi = {10.1371/journal.pone.0000092},
  note = {access: abstract_only (MB-02; critic: MB-02:C-069..071, open in PMC, PMC1762399); cited as: MB-02 [14]}
}

@article{hildenbrandGenomeCopyNumbers2011,
  author = {Hildenbrand, Catherina and Stock, Tilmann and Lange, Christian and Rother, Michael and Soppa, Jörg},
  title = {Genome copy numbers and gene conversion in methanogenic archaea},
  journal = {Journal of Bacteriology},
  year = {2011},
  volume = {193},
  number = {3},
  pages = {734-743},
  doi = {10.1128/JB.01016-10},
  note = {access: abstract_only (MB-02; critic: MB-02:C-076, a PMC record exists, PMC3021236); cited as: MB-02 [15]}
}

@article{griesePloidyCyanobacteria2011,
  author = {Griese, Marco and Lange, Christian and Soppa, Jörg},
  title = {Ploidy in cyanobacteria},
  journal = {FEMS Microbiology Letters},
  year = {2011},
  volume = {323},
  number = {2},
  pages = {124-131},
  doi = {10.1111/j.1574-6968.2011.02368.x},
  note = {access: abstract_only (MB-02); cited as: MB-02 [16]}
}

@article{zerullaPloidyLevelSynechocystis2016,
  author = {Zerulla, Karolin and Ludt, Katharina and Soppa, Jörg},
  title = {The ploidy level of Synechocystis sp},
  journal = {PCC 6803 is highly variable and is influenced by growth phase and by chemical and physical external parameters. Microbiology},
  year = {2016},
  volume = {162},
  number = {5},
  pages = {730-739},
  doi = {10.1099/mic.0.000264},
  note = {access: abstract_only (MB-02); cited as: MB-02 [17]}
}

@article{bruckOneAdvantageBeing2023,
  author = {Brück, Patrik and Wasser, Daniel and Soppa, Jörg},
  title = {One advantage of being polyploid: prokaryotes of various phylogenetic groups can grow in the absence of an environmental phosphate source at the expense of their high genome copy numbers},
  journal = {Microorganisms},
  year = {2023},
  volume = {11},
  number = {9},
  pages = {2267},
  doi = {10.3390/microorganisms11092267},
  note = {access: abstract_only (MB-02; critic: MB-02:C-072..074, open in PMC, PMC10536925); cited as: MB-02 [18]}
}

@article{zerullaPolyploidyHaloarchaeaAdvantages2014,
  author = {Zerulla, Karolin and Soppa, Jörg},
  title = {Polyploidy in haloarchaea: advantages for growth and survival},
  journal = {Frontiers in Microbiology},
  year = {2014},
  volume = {5},
  pages = {274},
  doi = {10.3389/fmicb.2014.00274},
  note = {access: abstract_only (MB-02); cited as: MB-02 [19]}
}

@article{couturierReplicationassociatedGeneDosage2006,
  author = {Couturier, Etienne and Rocha, Eduardo P. C.},
  title = {Replication-associated gene dosage effects shape the genomes of fast-growing bacteria but only for transcription and translation genes},
  journal = {Molecular Microbiology},
  year = {2006},
  volume = {59},
  number = {5},
  pages = {1506-1518},
  doi = {10.1111/j.1365-2958.2006.05046.x},
  note = {access: abstract_only (MB-02); cited as: MB-02 [20]}
}

@article{christensenFlowCytometricMeasurements1995,
  author = {Christensen, H. and Olsen, R. A. and Bakken, L. R.},
  title = {Flow cytometric measurements of cell volumes and DNA contents during culture of indigenous soil bacteria},
  journal = {Microbial Ecology},
  year = {1995},
  volume = {29},
  number = {1},
  pages = {49-62},
  doi = {10.1007/BF00217422},
  note = {access: abstract_only (MB-02); cited as: MB-02 [22]; pages 49-62 not confirmed from Crossref (critic: MB-02:C-097)}
}

@article{buttonDeterminationDNAContent2001,
  author = {Button, D. K. and Robertson, Betsy R.},
  title = {Determination of DNA content of aquatic bacteria by flow cytometry},
  journal = {Applied and Environmental Microbiology},
  year = {2001},
  volume = {67},
  number = {4},
  pages = {1636-1645},
  doi = {10.1128/AEM.67.4.1636-1645.2001},
  note = {access: full_text (MB-02; first 100,000 characters); cited as: MB-02 [23]}
}

@article{vaulotGrowthProchlorococcusPhotosynthetic1995,
  author = {Vaulot, Daniel and Marie, Dominique and Olson, Robert J. and Chisholm, Sallie W.},
  title = {Growth of Prochlorococcus, a photosynthetic prokaryote, in the equatorial Pacific Ocean},
  journal = {Science},
  year = {1995},
  volume = {268},
  number = {5216},
  pages = {1480-1482},
  doi = {10.1126/science.268.5216.1480},
  note = {access: abstract_only (MB-02; critic: MB-02:C-078..080, the abstract gives no share of cells); cited as: MB-02 [24]}
}

@article{brownMeasurementBacterialReplication2016,
  author = {Brown, Christopher T. and Olm, Matthew R. and Thomas, Brian C. and Banfield, Jillian F.},
  title = {Measurement of bacterial replication rates in microbial communities},
  journal = {Nature Biotechnology},
  year = {2016},
  volume = {34},
  number = {12},
  pages = {1256-1263},
  doi = {10.1038/nbt.3704},
  note = {access: full_text (MB-02; first 100,000 characters); cited as: MB-02 [25]}
}

@article{koremGrowthDynamicsGut2015,
  author = {Korem, Tal and Zeevi, David and Suez, Jotham and Weinberger, Adina and Avnit-Sagi, Tali and Pompan-Lotan, Maya and Matot, Elad and Jona, Ghil and Harmelin, Alon and Cohen, Nadav and Sirota-Madi, Alexandra and Thaiss, Christoph A. and Pevsner-Fischer, Meirav and Sorek, Rotem and Xavier, Ramnik J. and Elinav, Eran and Segal, Eran},
  title = {Growth dynamics of gut microbiota in health and disease inferred from single metagenomic samples},
  journal = {Science},
  year = {2015},
  volume = {349},
  number = {6252},
  pages = {1101-1106},
  doi = {10.1126/science.aac4812},
  note = {access: abstract_only (MB-02); cited as: MB-02 [26]}
}

@article{farrellyEffectGenomeSize1995,
  author = {Farrelly, V. and Rainey, F. A. and Stackebrandt, E.},
  title = {Effect of genome size and rrn gene copy number on PCR amplification of 16S rRNA genes from a mixture of bacterial species},
  journal = {Applied and Environmental Microbiology},
  year = {1995},
  volume = {61},
  number = {7},
  pages = {2798-2801},
  doi = {10.1128/aem.61.7.2798-2801.1995},
  note = {access: abstract_only (MB-02); cited as: MB-02 [27]}
}

@article{anglyCopyRighterRapidTool2014,
  author = {Angly, Florent E. and Dennis, Paul G. and Skarshewski, Adam and Vanwonterghem, Inka and Hugenholtz, Philip and Tyson, Gene W.},
  title = {CopyRighter: a rapid tool for improving the accuracy of microbial community profiles through lineage-specific gene copy number correction},
  journal = {Microbiome},
  year = {2014},
  volume = {2},
  pages = {11},
  doi = {10.1186/2049-2618-2-11},
  note = {access: abstract_only (MB-02); cited as: MB-02 [29]}
}

@article{perisin16StimatorStatisticalEstimation2016,
  author = {Perisin, Matthew and Vetter, Madlen and Gilbert, Jack A. and Bergelson, Joy},
  title = {16Stimator: statistical estimation of ribosomal gene copy numbers from draft genome assemblies},
  journal = {The ISME Journal},
  year = {2016},
  volume = {10},
  number = {4},
  pages = {1020-1024},
  doi = {10.1038/ismej.2015.161},
  note = {access: abstract_only (MB-02); cited as: MB-02 [34]}
}

@article{lavrinienkoDoesIntraspecificVariation2021,
  author = {Lavrinienko, Anton and Jernfors, Toni and Koskimäki, Janne J. and Pirttilä, Anna Maria and Watts, Phillip C.},
  title = {Does intraspecific variation in rDNA copy number affect analysis of microbial communities?},
  journal = {Trends in Microbiology},
  year = {2021},
  volume = {29},
  number = {1},
  pages = {19-27},
  doi = {10.1016/j.tim.2020.05.019},
  note = {access: abstract_only (MB-02); cited as: MB-02 [36]}
}

@article{soginMicrobialDiversityDeep2006,
  author = {Sogin, Mitchell L. and Morrison, Hilary G. and Huber, Julie A. and Welch, David Mark and Huse, Susan M. and Neal, Phillip R. and Arrieta, Jesus M. and Herndl, Gerhard J.},
  title = {Microbial diversity in the deep sea and the underexplored "rare biosphere"},
  journal = {PNAS},
  year = {2006},
  volume = {103},
  number = {32},
  pages = {12115-12120},
  doi = {10.1073/pnas.0605127103},
  note = {access: abstract_only (MB-02); cited as: MB-02 [38]}
}

@article{pedrosalioRareBacterialBiosphere2012,
  author = {Pedrós-Alió, Carlos},
  title = {The rare bacterial biosphere},
  journal = {Annual Review of Marine Science},
  year = {2012},
  volume = {4},
  pages = {449-466},
  doi = {10.1146/annurev-marine-120710-100948},
  note = {access: abstract_only (MB-02); cited as: MB-02 [39]}
}

@article{lynchEcologyExplorationRare2015,
  author = {Lynch, Michael D. J. and Neufeld, Josh D.},
  title = {Ecology and exploration of the rare biosphere},
  journal = {Nature Reviews Microbiology},
  year = {2015},
  volume = {13},
  number = {4},
  pages = {217-229},
  doi = {10.1038/nrmicro3400},
  note = {access: abstract_only (MB-02); cited as: MB-02 [40]}
}

@article{pascoalMicrobialRareBiosphere2021,
  author = {Pascoal, Francisco and Costa, Rodrigo and Magalhães, Catarina},
  title = {The microbial rare biosphere: current concepts, methods and ecological principles},
  journal = {FEMS Microbiology Ecology},
  year = {2021},
  volume = {97},
  number = {1},
  pages = {fiaa227},
  doi = {10.1093/femsec/fiaa227},
  note = {access: abstract_only (MB-02); cited as: MB-02 [41]}
}

@article{pascoalDefinitionMicrobialRare2025,
  author = {Pascoal, Francisco and Branco, Paula and Torgo, Luís and Costa, Rodrigo and Magalhães, Catarina},
  title = {Definition of the microbial rare biosphere through unsupervised machine learning},
  journal = {Communications Biology},
  year = {2025},
  volume = {8},
  pages = {544},
  doi = {10.1038/s42003-025-07912-4},
  note = {access: full_text (MB-02); cited as: MB-02 [42]}
}

@article{galandEcologyRareMicrobial2009,
  author = {Galand, Pierre E. and Casamayor, Emilio O. and Kirchman, David L. and Lovejoy, Connie},
  title = {Ecology of the rare microbial biosphere of the Arctic Ocean},
  journal = {PNAS},
  year = {2009},
  volume = {106},
  number = {52},
  pages = {22427-22432},
  doi = {10.1073/pnas.0908284106},
  note = {access: full_text (MB-02); cited as: MB-02 [43]}
}

@article{daiIdentifyingKeyTaxonomic2016,
  author = {Dai, Tianjiao and Zhang, Yan and Tang, Yushi and Bai, Yaohui and Tao, Yile and Huang, Bei and Wen, Donghui},
  title = {Identifying the key taxonomic categories that characterize microbial community diversity using full-scale classification: a case study of microbial communities in the sediments of Hangzhou Bay},
  journal = {FEMS Microbiology Ecology},
  year = {2016},
  volume = {92},
  number = {10},
  pages = {fiw150},
  doi = {10.1093/femsec/fiw150},
  note = {access: abstract_only (MB-02); cited as: MB-02 [44]}
}

@article{shadeConditionallyRareTaxa2014,
  author = {Shade, Ashley and Jones, Stuart E. and Caporaso, J. Gregory and Handelsman, Jo and Knight, Rob and Fierer, Noah and Gilbert, Jack A.},
  title = {Conditionally rare taxa disproportionately contribute to temporal changes in microbial diversity},
  journal = {mBio},
  year = {2014},
  volume = {5},
  number = {4},
  pages = {e01371-14},
  doi = {10.1128/mBio.01371-14},
  note = {access: full_text (MB-02; excerpts); cited as: MB-02 [45]}
}

@article{gobetMultivariateCutoffLevel2010,
  author = {Gobet, Angélique and Quince, Christopher and Ramette, Alban},
  title = {Multivariate Cutoff Level Analysis (MultiCoLA) of large community data sets},
  journal = {Nucleic Acids Research},
  year = {2010},
  volume = {38},
  number = {15},
  pages = {e155},
  doi = {10.1093/nar/gkq545},
  note = {access: abstract_only (MB-02); cited as: MB-02 [46]}
}

@article{joussetWhereLessMay2017,
  author = {Jousset, Alexandre and Bienhold, Christina and Chatzinotas, Antonis and Gallien, Laure and Gobet, Angélique and Kurm, Viola and Küsel, Kirsten and Rillig, Matthias C. and Rivett, Damian W. and Salles, Joana F. and van der Heijden, Marcel G. A. and Youssef, Noha H. and Zhang, Xiaowei and Wei, Zhong and Gera Hol, W. H.},
  title = {Where less may be more: how the rare biosphere pulls ecosystems strings},
  journal = {The ISME Journal},
  year = {2017},
  volume = {11},
  number = {4},
  pages = {853-862},
  doi = {10.1038/ismej.2016.174},
  note = {access: full_text (MB-02); cited as: MB-02 [47]}
}

@article{jiaCommunityAssemblyProcesses2018,
  author = {Jia, Xiu and Dini-Andreote, Francisco and Falcão Salles, Joana},
  title = {Community assembly processes of the microbial rare biosphere},
  journal = {Trends in Microbiology},
  year = {2018},
  volume = {26},
  number = {9},
  pages = {738-747},
  doi = {10.1016/j.tim.2018.02.011},
  note = {access: abstract_only (MB-02); cited as: MB-02 [48]}
}

@article{jiaUnravellingInterplayEcological2022,
  author = {Jia, Xiu and Dini-Andreote, Francisco and Falcão Salles, Joana},
  title = {Unravelling the interplay of ecological processes structuring the bacterial rare biosphere},
  journal = {ISME Communications},
  year = {2022},
  volume = {2},
  pages = {96},
  doi = {10.1038/s43705-022-00177-6},
  note = {access: full_text (MB-02); cited as: MB-02 [49]}
}

@article{shadeBeyondVennDiagram2012,
  author = {Shade, Ashley and Handelsman, Jo},
  title = {Beyond the Venn diagram: the hunt for a core microbiome},
  journal = {Environmental Microbiology},
  year = {2012},
  volume = {14},
  number = {1},
  pages = {4-12},
  doi = {10.1111/j.1462-2920.2011.02585.x},
  note = {access: abstract_only (MB-02); cited as: MB-02 [50]}
}

@article{neuDefiningQuantifyingCore2021,
  author = {Neu, Alexander T. and Allen, Eric E. and Roy, Kaustuv},
  title = {Defining and quantifying the core microbiome: challenges and prospects},
  journal = {PNAS},
  year = {2021},
  volume = {118},
  number = {51},
  pages = {e2104429118},
  doi = {10.1073/pnas.2104429118},
  note = {access: full_text (MB-02; first 100,000 characters); cited as: MB-02 [51]}
}

@article{custerComparativeAnalysisCore2023,
  author = {Custer, Gordon F. and Gans, Maya and Diepen, Linda T. A. van and Dini-Andreote, Francisco and Buerkle, C. Alex},
  title = {Comparative analysis of core microbiome assignments: implications for ecological synthesis},
  journal = {mSystems},
  year = {2023},
  volume = {8},
  number = {1},
  pages = {e01066-22},
  doi = {10.1128/msystems.01066-22},
  note = {access: full_text (MB-02; first 100,000 characters); cited as: MB-02 [52]}
}

@article{astudillogarciaEvaluatingCoreMicrobiota2017,
  author = {Astudillo-García, Carmen and Bell, James J. and Webster, Nicole S. and Glasl, Bettina and Jompa, Jamaluddin and Montoya, Jose M. and Taylor, Michael W.},
  title = {Evaluating the core microbiota in complex communities: a systematic investigation},
  journal = {Environmental Microbiology},
  year = {2017},
  volume = {19},
  number = {4},
  pages = {1450-1462},
  doi = {10.1111/1462-2920.13647},
  note = {access: abstract_only (MB-02); cited as: MB-02 [53]}
}

@article{salonenAdultIntestinalCore2012,
  author = {Salonen, A. and Salojärvi, J. and Lahti, L. and de Vos, W. M.},
  title = {The adult intestinal core microbiota is determined by analysis depth and health status},
  journal = {Clinical Microbiology and Infection},
  year = {2012},
  volume = {18},
  number = {Suppl 4},
  pages = {16-20},
  doi = {10.1111/j.1469-0691.2012.03855.x},
  note = {access: abstract_only (MB-02); cited as: MB-02 [54]}
}

@article{riselyApplyingCoreMicrobiome2020,
  author = {Risely, Alice},
  title = {Applying the core microbiome to understand host-microbe systems},
  journal = {Journal of Animal Ecology},
  year = {2020},
  volume = {89},
  number = {7},
  pages = {1549-1558},
  doi = {10.1111/1365-2656.13229},
  note = {access: abstract_only (MB-02); cited as: MB-02 [55]}
}

@article{shadeAbundanceoccupancyDistributionsPrioritize2019,
  author = {Shade, Ashley and Stopnisek, Nejc},
  title = {Abundance-occupancy distributions to prioritize plant core microbiome membership},
  journal = {Current Opinion in Microbiology},
  year = {2019},
  volume = {49},
  pages = {50-58},
  doi = {10.1016/j.mib.2019.09.008},
  note = {access: abstract_only (MB-02); cited as: MB-02 [56]}
}

@article{magurranExplainingExcessRare2003,
  author = {Magurran, Anne E. and Henderson, Peter A.},
  title = {Explaining the excess of rare species in natural species abundance distributions},
  journal = {Nature},
  year = {2003},
  volume = {422},
  number = {6933},
  pages = {714-716},
  doi = {10.1038/nature01547},
  note = {access: abstract_only (MB-02); cited as: MB-02 [57]}
}

@article{gastonAbundanceoccupancyRelationships2000,
  author = {Gaston, Kevin J. and Blackburn, Tim M. and Greenwood, Jeremy J. D. and Gregory, Richard D. and Quinn, Rachel M. and Lawton, John H.},
  title = {Abundance-occupancy relationships},
  journal = {Journal of Applied Ecology},
  year = {2000},
  volume = {37},
  number = {s1},
  pages = {39-59},
  doi = {10.1046/j.1365-2664.2000.00485.x},
  note = {access: abstract_only (MB-02); cited as: MB-02 [58]}
}

@article{delgadobaquerizoGlobalAtlasDominant2018,
  author = {Delgado-Baquerizo, Manuel and Oliverio, Angela M. and Brewer, Tess E. and Benavent-González, Alberto and Eldridge, David J. and Bardgett, Richard D. and Maestre, Fernando T. and Singh, Brajesh K. and Fierer, Noah},
  title = {A global atlas of the dominant bacteria found in soil},
  journal = {Science},
  year = {2018},
  volume = {359},
  number = {6373},
  pages = {320-325},
  doi = {10.1126/science.aap9516},
  note = {access: full_text (MB-02; publisher PDF via NOAA repository); cited as: MB-02 [60]}
}

@article{nemergutGlobalPatternsBiogeography2011,
  author = {Nemergut, Diana R. and Costello, Elizabeth K. and Hamady, Micah and Lozupone, Catherine and Jiang, Lin and Schmidt, Steven K. and Fierer, Noah and Townsend, Alan R. and Cleveland, Cory C. and Stanish, Lee and Knight, Rob},
  title = {Global patterns in the biogeography of bacterial taxa},
  journal = {Environmental Microbiology},
  year = {2011},
  volume = {13},
  number = {1},
  pages = {135-144},
  doi = {10.1111/j.1462-2920.2010.02315.x},
  note = {access: full_text (MB-02; critic: MB-02:C-082..085, its figures could not be verified, Europe PMC returned HTTP 500 and PMC a captcha); cited as: MB-02 [62]}
}

@article{barberanWhyAreMicrobes2014,
  author = {Barberán, Albert and Ramirez, Kelly S. and Leff, Jonathan W. and Bradford, Mark A. and Wall, Diana H. and Fierer, Noah},
  title = {Why are some microbes more ubiquitous than others?},
  journal = {Predicting the habitat breadth of soil bacteria. Ecology Letters},
  year = {2014},
  volume = {17},
  number = {7},
  pages = {794-802},
  doi = {10.1111/ele.12282},
  note = {access: abstract_only (MB-02); cited as: MB-02 [63]}
}

@article{batesExaminingGlobalDistribution2011,
  author = {Bates, Scott T. and Berg-Lyons, Donna and Caporaso, J. Gregory and Walters, William A. and Knight, Rob and Fierer, Noah},
  title = {Examining the global distribution of dominant archaeal populations in soil},
  journal = {The ISME Journal},
  year = {2011},
  volume = {5},
  number = {5},
  pages = {908-917},
  doi = {10.1038/ismej.2010.171},
  note = {access: abstract_only (MB-02); cited as: MB-02 [64]}
}

@article{gansComputationalImprovementsReveal2005,
  author = {Gans, Jason and Wolinsky, Murray and Dunbar, John},
  title = {Computational improvements reveal great bacterial diversity and high metal toxicity in soil},
  journal = {Science},
  year = {2005},
  volume = {309},
  number = {5739},
  pages = {1387-1390},
  doi = {10.1126/science.1112665},
  note = {access: abstract_only (MB-02); cited as: MB-02 [66]}
}

@article{curtisEstimatingProkaryoticDiversity2002,
  author = {Curtis, Thomas P. and Sloan, William T. and Scannell, Jack W.},
  title = {Estimating prokaryotic diversity and its limits},
  journal = {PNAS},
  year = {2002},
  volume = {99},
  number = {16},
  pages = {10494-10499},
  doi = {10.1073/pnas.142680199},
  note = {access: abstract_only (MB-02); cited as: MB-02 [67]}
}

@article{dunbarEmpiricalTheoreticalBacterial2002,
  author = {Dunbar, John and Barns, Susan M. and Ticknor, Lawrence O. and Kuske, Cheryl R.},
  title = {Empirical and theoretical bacterial diversity in four Arizona soils},
  journal = {Applied and Environmental Microbiology},
  year = {2002},
  volume = {68},
  number = {6},
  pages = {3035-3045},
  doi = {10.1128/AEM.68.6.3035-3045.2002},
  note = {access: abstract_only (MB-02); cited as: MB-02 [68]}
}

@article{quinceRationalExplorationMicrobial2008,
  author = {Quince, Christopher and Curtis, Thomas P. and Sloan, William T.},
  title = {The rational exploration of microbial diversity},
  journal = {The ISME Journal},
  year = {2008},
  volume = {2},
  number = {10},
  pages = {997-1006},
  doi = {10.1038/ismej.2008.69},
  note = {access: abstract_only (MB-02); cited as: MB-02 [69]}
}

@article{loceyScalingLawsPredict2016,
  author = {Locey, Kenneth J. and Lennon, Jay T.},
  title = {Scaling laws predict global microbial diversity},
  journal = {PNAS},
  year = {2016},
  volume = {113},
  number = {21},
  pages = {5970-5975},
  doi = {10.1073/pnas.1521291113},
  note = {access: abstract_only (MB-02); cited as: MB-02 [71]}
}

@article{sloanQuantifyingRolesImmigration2006,
  author = {Sloan, William T. and Lunn, Mary and Woodcock, Stephen and Head, Ian M. and Nee, Sean and Curtis, Thomas P.},
  title = {Quantifying the roles of immigration and chance in shaping prokaryote community structure},
  journal = {Environmental Microbiology},
  year = {2006},
  volume = {8},
  number = {4},
  pages = {732-740},
  doi = {10.1111/j.1462-2920.2005.00956.x},
  note = {access: abstract_only (MB-02); cited as: MB-02 [73]}
}

@article{stopnisekPersistentMicrobiomeMembers2021,
  author = {Stopnisek, Nejc and Shade, Ashley},
  title = {Persistent microbiome members in the common bean rhizosphere: an integrated analysis of space, time, and plant genotype},
  journal = {The ISME Journal},
  year = {2021},
  volume = {15},
  number = {9},
  pages = {2708-2722},
  doi = {10.1038/s41396-021-00955-5},
  note = {access: full_text (MB-02); cited as: MB-02 [74]}
}

@article{waltersLargescaleReplicatedField2018,
  author = {Walters, William A. and Jin, Zhao and Youngblut, Nicholas and Wallace, Jason G. and Sutter, Jessica and Zhang, Wei and González-Peña, Antonio and Peiffer, Jason and Koren, Omry and Shi, Qiaojuan and Knight, Rob and Glavina del Rio, Tijana and Tringe, Susannah G. and Buckler, Edward S. and Dangl, Jeffery L. and Ley, Ruth E.},
  title = {Large-scale replicated field study of maize rhizosphere identifies heritable microbes},
  journal = {PNAS},
  year = {2018},
  volume = {115},
  number = {28},
  pages = {7368-7373},
  doi = {10.1073/pnas.1800918115},
  note = {access: abstract_only (MB-02); cited as: MB-02 [75]}
}

@article{howeTacklingSoilDiversity2014,
  author = {Howe, Adina Chuang and Jansson, Janet K. and Malfatti, Stephanie A. and Tringe, Susannah G. and Tiedje, James M. and Brown, C. Titus},
  title = {Tackling soil diversity with the assembly of large, complex metagenomes},
  journal = {PNAS},
  year = {2014},
  volume = {111},
  number = {13},
  pages = {4904-4909},
  doi = {10.1073/pnas.1402564111},
  note = {access: full_text (MB-02); cited as: MB-02 [79]}
}

@article{rodriguezrEstimatingCoverageMetagenomic2014,
  author = {Rodriguez-R, Luis M. and Konstantinidis, Konstantinos T.},
  title = {Estimating coverage in metagenomic data sets and why it matters},
  journal = {The ISME Journal},
  year = {2014},
  volume = {8},
  number = {11},
  pages = {2349-2351},
  doi = {10.1038/ismej.2014.76},
  note = {access: full_text (MB-02); cited as: MB-02 [80]}
}

@article{kuninWrinklesRareBiosphere2010,
  author = {Kunin, Victor and Engelbrektson, Anna and Ochman, Howard and Hugenholtz, Philip},
  title = {Wrinkles in the rare biosphere: pyrosequencing errors can lead to artificial inflation of diversity estimates},
  journal = {Environmental Microbiology},
  year = {2010},
  volume = {12},
  number = {1},
  pages = {118-123},
  doi = {10.1111/j.1462-2920.2009.02051.x},
  note = {access: not_obtained (MB-01; Sources not obtained: abstract and full text not retrieved; issued online 2009), abstract_only (MB-02); cited as: MB-02 [81]; the two notes give different access}
}

@article{huseIroningOutWrinkles2010,
  author = {Huse, Susan M. and Welch, David Mark and Morrison, Hilary G. and Sogin, Mitchell L.},
  title = {Ironing out the wrinkles in the rare biosphere through improved OTU clustering},
  journal = {Environmental Microbiology},
  year = {2010},
  volume = {12},
  number = {7},
  pages = {1889-1898},
  doi = {10.1111/j.1462-2920.2010.02193.x},
  note = {access: abstract_only (MB-02); cited as: MB-02 [82]}
}

@misc{callahanDADA2DocumentationPseudopooling,
  author = {Callahan, Benjamin J.},
  title = {{DADA2 documentation: Pseudo-pooling}},
  url = {https://benjjneb.github.io/dada2/pseudo.html},
  urldate = {2026-10-20},
  note = {access: full_text (MB-01); type: DOCUMENTATION; incomplete: year}
}

@misc{benjjnebConsequencesUsingDada2,
  author = {{benjjneb (DADA2 maintainer) and contributors}},
  title = {{Consequences of using dada2 on NovaSeq data}},
  howpublished = {GitHub issue #791, benjjneb/dada2},
  url = {https://github.com/benjjneb/dada2/issues/791},
  urldate = {2026-10-20},
  note = {access: full_text (MB-01); type: DOCUMENTATION, issue tracker; incomplete: year}
}

@misc{earth16SIlluminaAmplicon,
  author = {{Earth Microbiome Project}},
  title = {{16S Illumina Amplicon Protocol}},
  url = {https://earthmicrobiome.org/protocols-and-standards/16s/},
  urldate = {2026-10-20},
  note = {access: full_text (MB-01); type: PROTOCOL; incomplete: year}
}

@misc{emoryAmplicon16SMetagenomics,
  author = {{Emory Integrated Genomics Core / ECGC}},
  title = {{Amplicon 16S metagenomics (methods description)}},
  url = {https://www.cores.emory.edu/ecgc/_includes/documents/sections/resources/amplicon-16s-metagenomics.pdf},
  urldate = {2026-10-20},
  note = {access: full_text (MB-01); type: PROTOCOL; incomplete: year}
}

@manual{illumina16SMetagenomicSequencing,
  author = {{Illumina, Inc.}},
  title = {{16S Metagenomic Sequencing Library Preparation: Preparing 16S Ribosomal RNA Gene Amplicons for the Illumina MiSeq System}},
  number = {Part # 15044223 Rev. B},
  url = {https://support.illumina.com/documents/documentation/chemistry_documentation/16s/16s-metagenomic-library-prep-guide-15044223-b.pdf},
  urldate = {2026-10-20},
  note = {access: full_text (MB-01; maker's claims); type: DOCUMENTATION; incomplete: year}
}

@misc{illuminaIndexHopping,
  author = {{Illumina, Inc.}},
  title = {{Index hopping}},
  howpublished = {web page},
  url = {https://www.illumina.com/techniques/sequencing/ngs-library-prep/multiplexing/index-hopping.html},
  urldate = {2026-10-20},
  note = {access: full_text (MB-01; maker's claims); type: DOCUMENTATION; incomplete: year}
}

@misc{zymoZymoBIOMICSMicrobialCommunity,
  author = {{Zymo Research}},
  title = {{ZymoBIOMICS Microbial Community Standard (product page)}},
  url = {https://www.zymoresearch.com/products/zymobiomics-microbial-community-standard},
  urldate = {2026-10-20},
  note = {access: full_text (MB-01; maker's claims); type: DOCUMENTATION; not cited: listed in MB-01's references and named among makers' documentation in its D1 access line, cited by no finding; incomplete: year}
}

@misc{schmidtlaboratoryRrnDBReleaseFiles,
  author = {{Schmidt Laboratory, University of Michigan}},
  title = {{rrnDB release files v3.1.227, v4.4.3, v5.0, v5.6 and v5.10 (v5.10 dated 6 June 2025), and About page}},
  url = {https://rrndb.umms.med.umich.edu/static/download/},
  urldate = {2026-10-20},
  note = {access: full_text (MB-02; statistics derived by reviewer); cited as: MB-02 [4]; incomplete: year}
}

@misc{bionumbersAverageNumberRRNA,
  author = {{BioNumbers}},
  title = {{Average number of rRNA genes per genome}},
  howpublished = {BioNumbers entry 102360, citing H. Bremer and P. P. Dennis (1996), in F. C. Neidhardt et al. (eds), Escherichia coli and Salmonella: Cellular and Molecular Biology, 2nd ed., ch. 97, Table 3},
  url = {https://bionumbers.hms.harvard.edu/bionumber.aspx?id=102360},
  note = {access: secondary (MB-02); cited as: MB-02 [21], first of two works in that reference; incomplete: year}
}

@article{miloBioNumbersDatabaseKey2010,
  author = {Milo, Ron and Jorgensen, Paul and Moran, Uri and Weber, Griffin and Springer, Michael},
  title = {{BioNumbers - the database of key numbers in molecular and cell biology}},
  journal = {Nucleic Acids Research},
  year = {2010},
  volume = {38},
  number = {suppl_1},
  pages = {D750-D753},
  doi = {10.1093/nar/gkp889},
  note = {access: secondary (MB-02); cited as: MB-02 [21], the database paper named in that reference; not cited on its own}
}

@article{gaoAccounting16SRRNA2023,
  author = {Gao, Yingnan and Wu, Martin},
  title = {{Accounting for 16S rRNA copy number prediction uncertainty and its implications in bacterial diversity analyses}},
  journal = {ISME Communications},
  year = {2023},
  volume = {3},
  pages = {59},
  doi = {10.1038/s43705-023-00266-0},
  note = {access: full_text (MB-02); cited as: MB-02 [33]}
}

@article{zengIdentifyingBiogeographicPatterns2021,
  author = {Zeng, Quanchao and An, Shaoshan},
  title = {{Identifying the biogeographic patterns of rare and abundant bacterial communities using different primer sets on the Loess Plateau}},
  journal = {Microorganisms},
  year = {2021},
  volume = {9},
  number = {1},
  pages = {139},
  doi = {10.3390/microorganisms9010139},
  note = {access: abstract_only (MB-02); cited as: MB-02 [59]}
}

@article{bickelChosenFewVariations2021,
  author = {Bickel, Samuel and Or, Dani},
  title = {{The chosen few - variations in common and rare soil bacteria across biomes}},
  journal = {The ISME Journal},
  year = {2021},
  volume = {15},
  number = {11},
  pages = {3315-3325},
  doi = {10.1038/s41396-021-00981-3},
  note = {access: full_text (MB-02); cited as: MB-02 [61]}
}

@article{ramirezDetectingMacroecologicalPatterns2017,
  author = {Ramirez},
  journal = {Nature Microbiology},
  year = {2018},
  volume = {3},
  number = {2},
  pages = {189-196},
  doi = {10.1038/s41564-017-0062-x},
  note = {access: abstract_only (MB-02); cited as: MB-02 [65], not used in the body or answers, named in the search record; incomplete: author, title}
}

@article{gohlSystematicImprovementAmplicon2016,
  author = {Gohl, Daryl M and Vangay, Pajau and Garbe, John and MacLean, Allison and Hauge, Adam and Becker, Aaron and Gould, Trevor J and Clayton, Jonathan B and Johnson, Timothy J and Hunter, Ryan and Knights, Dan and Beckman, Kenneth B},
  title = {{Systematic improvement of amplicon marker gene methods for increased accuracy in microbiome studies}},
  journal = {Nature Biotechnology},
  year = {2016},
  volume = {34},
  number = {9},
  pages = {942-949},
  doi = {10.1038/nbt.3601},
  note = {access: not_obtained (MB-01; Europe PMC abstract only, no figures; publisher paywalled; listed three times)}
}

@article{costeaTowardsStandardsHuman2017,
  author = {Costea, Paul I. and Zeller, Georg and Sunagawa, Shinichi and others},
  title = {{Towards standards for human fecal sample processing in metagenomic studies}},
  journal = {Nature Biotechnology},
  year = {2017},
  volume = {35},
  number = {11},
  pages = {1069-1076},
  doi = {10.1038/nbt.3960},
  note = {access: secondary (MB-01; known only through McLaren 2019; also in its Sources not obtained, not fetched); incomplete: author}
}

@article{lauberEffectStorageConditions2010,
  author = {Lauber, Christian L. and Zhou, Nicholas and Gordon, Jeffrey I. and Knight, Rob and Fierer, Noah},
  title = {{Effect of storage conditions on the assessment of bacterial community structure in soil and human-associated samples}},
  journal = {FEMS Microbiology Letters},
  year = {2010},
  volume = {307},
  number = {1},
  pages = {80-86},
  doi = {10.1111/j.1574-6968.2010.01965.x},
  note = {access: secondary (MB-01; known only through Rubin 2013; in its Sources not obtained)}
}

@article{wesolowskaandersenChoiceBacterialDNA2014,
  author = {Wesolowska-Andersen, Agata and Bahl, Martin I. and Carvalho, Vera and Kristiansen, Karsten and Sicheritz-Ponten, Thomas and Gupta, Ramneek and Licht, Tine R.},
  title = {{Choice of bacterial DNA extraction method from fecal material influences community structure as evaluated by metagenomic analysis}},
  journal = {Microbiome},
  year = {2014},
  volume = {2},
  pages = {19},
  doi = {10.1186/2049-2618-2-19},
  note = {access: not_obtained (MB-01; full text retrieved but not searched before scratch cleanup; no findings extracted)}
}

@article{kimOptimizingMethodsDodging2017,
  author = {Kim, Dorothy and Hofstaedter, Casey E. and Zhao, Chunyu and Mattei, Lisa and Tanes, Ceylan and Clarke, Erik and Lauder, Abigail and Sherrill-Mix, Scott and Chehoud, Christel and Kelsen, Judith and Conrad, Máire and Collman, Ronald G. and Baldassano, Robert and Bushman, Frederic D. and Bittinger, Kyle},
  title = {{Optimizing methods and dodging pitfalls in microbiome research}},
  journal = {Microbiome},
  year = {2017},
  volume = {5},
  pages = {52},
  doi = {10.1186/s40168-017-0267-5},
  note = {access: not_obtained (MB-01; full text keyword-searched; review content not reported to avoid secondary duplication)}
}

@misc{rrndbRrnDBCurrentRelease,
  author = {{rrnDB}},
  title = {{rrnDB current release statistics}},
  url = {https://rrndb.umms.med.umich.edu/},
  note = {access: not_obtained (MB-01; WebFetch failed with TLS certificate error); MB-02 reached the same site and derived statistics from its release files (schmidtlaboratoryRrnDBReleaseFiles); incomplete: year}
}

@article{weissTrackingDownSources2014,
  author = {Weiss, Sophie and Amir, Amnon and Hyde, Embriette R. and Metcalf, Jessica L. and Song, Se Jin and Knight, Rob},
  title = {{Tracking down the sources of experimental contamination in microbiome studies}},
  journal = {Genome Biology},
  year = {2014},
  volume = {15},
  pages = {564},
  doi = {10.1186/s13059-014-0564-2},
  note = {access: not_obtained (MB-01; Crossref verified only)}
}

@article{pauvertBioinformaticsMattersAccuracy2019,
  author = {Pauvert, Charlie and Buée, Marc and Laval, Valérie and Edel-Hermann, Véronique and Fauchery, Laure and Gautier, Angélique and Lesur, Isabelle and Vallance, Jessica and Vacher, Corinne},
  title = {{Bioinformatics matters: the accuracy of plant and soil fungal community data is highly dependent on the metabarcoding pipeline}},
  journal = {Fungal Ecology},
  year = {2019},
  volume = {41},
  pages = {23-33},
  doi = {10.1016/j.funeco.2019.03.005},
  note = {access: not_obtained (MB-01; Crossref metadata only; ITS, indirect)}
}

@misc{sinhaIndexSwitchingCauses2017,
  author = {Sinha, Rahul and Stanley, Geoff and Gulati, Gunsagar S. and Ezran, Camille and Travaglini, Kyle J. and Wei, Eric and Chan, Charles K. F. and Nabhan, Ahmad N. and Su, Tianying and Morganti, Rachel M. and Conley, Stephanie D. and Chaib, Hassan and Red-Horse, Kristy and Longaker, Michael T. and Snyder, Michael P. and Krasnow, Mark A. and Weissman, Irving L.},
  title = {{Index switching causes 'spreading-of-signal' among multiplexed samples in Illumina HiSeq 4000 DNA sequencing}},
  howpublished = {bioRxiv 125724},
  year = {2017},
  doi = {10.1101/125724},
  note = {access: not_obtained (MB-01; abstract and full text not retrieved); type: PREPRINT}
}

@article{hakimzadehPilePipelinesOverview2024,
  author = {Hakimzadeh, Ali and Abdala Asbun, Alejandro and Albanese, Davide and Bernard, Maria and Buchner, Dominik and Callahan, Benjamin and Caporaso, J. Gregory and Curd, Emily and Djemiel, Christophe and Brandström Durling, Mikael and Elbrecht, Vasco and Gold, Zachary and Gweon, Hyun S. and Hajibabaei, Mehrdad and Hildebrand, Falk and Mikryukov, Vladimir and Normandeau, Eric and Özkurt, Ezgi and Palmer, Jonathan M. and Pascal, Géraldine and Porter, Teresita M. and Straub, Daniel and Vasar, Martti and Větrovský, Tomáš and Zafeiropoulos, Haris and Anslan, Sten},
  title = {{A pile of pipelines: an overview of the bioinformatics software for metabarcoding data analyses}},
  journal = {Molecular Ecology Resources},
  year = {2024},
  volume = {24},
  number = {5},
  pages = {e13847},
  doi = {10.1111/1755-0998.13847},
  note = {access: not_obtained (MB-01; Crossref only, not read)}
}

@article{sandersMarineBenthicDiversity1968,
  author = {Sanders, Howard L.},
  title = {{Marine benthic diversity: a comparative study}},
  journal = {The American Naturalist},
  year = {1968},
  volume = {102},
  number = {925},
  pages = {243-282},
  doi = {10.1086/282541},
  note = {access: not_obtained (MB-01; known only secondarily via Chao and Jost 2012 and Willis 2019)}
}

@article{hurlbertNonconceptSpeciesDiversity1971,
  author = {Hurlbert, Stuart H.},
  title = {{The nonconcept of species diversity: a critique and alternative parameters}},
  journal = {Ecology},
  year = {1971},
  volume = {52},
  number = {4},
  pages = {577-586},
  doi = {10.2307/1934145},
  note = {access: not_obtained (MB-01; known only secondarily via Chao and Jost 2012 and Willis 2019)}
}

@article{goodPopulationFrequenciesSpecies1953,
  author = {Good, I. J.},
  title = {{The population frequencies of species and the estimation of population parameters}},
  journal = {Biometrika},
  year = {1953},
  volume = {40},
  number = {3-4},
  pages = {237-264},
  doi = {10.1093/biomet/40.3-4.237},
  note = {access: not_obtained (MB-01; Crossref metadata only)}
}

@article{hsiehINEXTRPackage2016,
  author = {Hsieh, T. C. and Ma, K. H. and Chao, Anne},
  title = {{iNEXT: an R package for rarefaction and extrapolation of species diversity (Hill numbers)}},
  journal = {Methods in Ecology and Evolution},
  year = {2016},
  volume = {7},
  number = {12},
  pages = {1451-1456},
  doi = {10.1111/2041-210X.12613},
  note = {access: not_obtained (MB-01; Crossref metadata only)}
}

@article{paulsonDifferentialAbundanceAnalysis2013,
  author = {Paulson, Joseph N. and Stine, O. Colin and Corrada Bravo, Héctor and Pop, Mihai},
  title = {{Differential abundance analysis for microbial marker-gene surveys}},
  journal = {Nature Methods},
  year = {2013},
  volume = {10},
  number = {12},
  pages = {1200-1202},
  doi = {10.1038/nmeth.2658},
  note = {access: not_obtained (MB-01; Europe PMC abstract only, read; full text not obtained)}
}

@article{loveModeratedEstimationFold2014,
  author = {Love, Michael I. and Huber, Wolfgang and Anders, Simon},
  title = {{Moderated estimation of fold change and dispersion for RNA-seq data with DESeq2}},
  journal = {Genome Biology},
  year = {2014},
  volume = {15},
  number = {12},
  pages = {550},
  doi = {10.1186/s13059-014-0550-8},
  note = {access: not_obtained (MB-01; Crossref metadata only)}
}

@incollection{rabinowitzSevenFormsRarity1981,
  author = {Rabinowitz, Deborah},
  title = {{Seven forms of rarity}},
  booktitle = {The Biological Aspects of Rare Plant Conservation},
  editor = {Synge, H.},
  publisher = {Wiley},
  year = {1981},
  pages = {205-217},
  note = {access: secondary (MB-02; used only as described in Jousset et al. 2017; in its Sources not obtained)}
}

@article{wrightCorrelationsIncidenceAbundance1991,
  author = {Wright, David H.},
  title = {{Correlations between incidence and abundance are expected by chance}},
  journal = {Journal of Biogeography},
  year = {1991},
  volume = {18},
  number = {4},
  pages = {463-466},
  doi = {10.2307/2845487},
  note = {access: not_obtained (MB-02; Crossref metadata only); end page 466 not confirmed from Crossref (critic: MB-02:C-098)}
}

@article{holtOccupancyabundanceRelationshipsSpatial2002,
  author = {Holt, Alison R. and Gaston, Kevin J. and He, Fangliang},
  title = {{Occupancy-abundance relationships and spatial distribution: a review}},
  journal = {Basic and Applied Ecology},
  year = {2002},
  volume = {3},
  number = {1},
  pages = {1-13},
  doi = {10.1078/1439-1791-00083},
  note = {access: not_obtained (MB-02; ScienceDirect returned 403)}
}

@article{hanskiDynamicsRegionalDistribution1982,
  author = {Hanski, Ilkka},
  title = {{Dynamics of regional distribution: the core and satellite species hypothesis}},
  journal = {Oikos},
  year = {1982},
  volume = {38},
  number = {2},
  pages = {210-221},
  doi = {10.2307/3544021},
  note = {access: not_obtained (MB-02; Crossref metadata only)}
}

@article{bakkenDNAcontentSoilBacteria1989,
  author = {Bakken, Lars R. and Olsen, Rolf A.},
  title = {{DNA-content of soil bacteria of different cell size}},
  journal = {Soil Biology and Biochemistry},
  year = {1989},
  volume = {21},
  number = {6},
  pages = {789-793},
  doi = {10.1016/0038-0717(89)90172-7},
  note = {access: secondary (MB-02; known only via Christensen et al. 1995 abstract; in its Sources not obtained)}
}

@article{christensenSoilBacterialDNA1993,
  author = {Christensen, Henrik and Bakken, Lars R. and Olsen, Rolf A.},
  title = {{Soil bacterial DNA and biovolume profiles measured by flow-cytometry}},
  journal = {FEMS Microbiology Ecology},
  year = {1993},
  volume = {11},
  number = {3-4},
  pages = {129-140},
  doi = {10.1111/j.1574-6968.1993.tb05804.x},
  note = {access: not_obtained (MB-02); the note gives two venues: FEMS Microbiology Ecology 11(3-4) and FEMS Microbiology Letters 102(3-4), pages 129-140 (Crossref has two records)}
}

@article{soppaPolyploidyCommunityStructure2017,
  author = {Soppa, Jörg},
  title = {{Polyploidy and community structure}},
  journal = {Nature Microbiology},
  year = {2017},
  volume = {2},
  pages = {16261},
  doi = {10.1038/nmicrobiol.2016.261},
  note = {access: not_obtained (MB-02; Europe PMC record has no abstract)}
}

@incollection{bremerModulationChemicalComposition1996,
  author = {Bremer, H. and Dennis, P. P.},
  title = {{Modulation of chemical composition and other parameters of the cell by growth rate}},
  booktitle = {Escherichia coli and Salmonella: Cellular and Molecular Biology},
  editor = {Neidhardt, F. C. and others},
  edition = {2},
  chapter = {97},
  publisher = {ASM Press},
  year = {1996},
  note = {access: secondary (MB-02; via BioNumbers; in its Sources not obtained, chapter itself not reached)}
}

@book{gastonRarity1994,
  author = {Gaston, Kevin J.},
  title = {{Rarity}},
  publisher = {Chapman and Hall},
  address = {London},
  year = {1994},
  note = {access: not_obtained (MB-02; not searched beyond citation trail)}
}

@article{callahanExactSequenceVariants2017,
  author = {Callahan, Benjamin J and McMurdie, Paul J and Holmes, Susan P},
  title = {{Exact sequence variants should replace operational taxonomic units in marker-gene data analysis}},
  journal = {The ISME Journal},
  year = {2017},
  volume = {11},
  number = {12},
  pages = {2639-2643},
  doi = {10.1038/ismej.2017.119},
  note = {access: abstract_only (background; checked on Crossref and Europe PMC, not in the inputs); type: peer reviewed}
}
```
