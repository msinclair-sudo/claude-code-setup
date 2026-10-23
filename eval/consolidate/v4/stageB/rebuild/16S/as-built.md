---
type: knowledge
title: 16S amplicon sequencing from sample to count table
inputs:
  - MB-01: "Topics/Biology/Research/Results/From sample to count table in 16S rRNA gene amplicon sequencing where counts depart from community composition, what the workflow's quantities measure, and how samples with unequal depth or load are compared. A literature review.md"
  - MB-02: "Topics/Biology/Research/Results/16S rRNA gene copies per genome and per cell, abundance and rarity terms, and abundance in soil. A literature review.md"
refs: PhD/Proposal/Refs/Refs.bib
built: 2026-10-23
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

## Concepts

### workflow: the steps and choices from sample to count table
needs: none
- **workflow.1** Twelve steps from sample to count table are documented, each with named alternatives; the procedural descriptions would not change if any single source were removed.
  conf: not stated · class: not stated · holds: protocols, software documentation and benchmarks, mostly full text; makers' statements labelled as such · src: none (the reviewer's synthesis of protocols, documentation and benchmarks) · trail: MB-01 §answers, §critic, §8. Answers · rating: "Strong for the existence of these choices and the alternatives used" · from: MB-01:A-001, MB-01:A-018, MB-01:A-032, MB-01:A-294, MB-01:C-001, MB-01:C-002
- **workflow.2** Field sampling, preservation and storage choices include freezing or refrigeration, 95% ethanol, FTA cards, OMNIgene Gut, 70% ethanol or no preservative, for various times and temperatures.
  conf: not stated · class: not stated · holds: studies that vary the preservative, the temperature and the duration of storage · src: songPreservationMethodsDiffer2016, rubinInvestigatingImpactStorage2013 · trail: MB-01 §answers, §2.1 · from: MB-01:A-002, MB-01:B-0079
- **workflow.3** DNA extraction choices are the kit, bead-beating intensity, plate or single tube, and whether relic DNA is removed with PMA or DNase.
  conf: not stated · class: not stated · holds: as listed in the answers · src: albertsenBackBasicsInfluence2015, minichQuantifyingUnderstandingWelltowell2019, cariniRelicDNAAbundant2016, lennonHowWhereRelic2018 · trail: MB-01 §answers · from: MB-01:A-004
- **workflow.4** Primer and region choices include V1-V2 through V7-V9 and full length, degenerate variants of 515F and 806R, and PNA clamps against host plastids; in silico surveys cover 175 primers and 512 pairs.
  conf: not stated · class: not stated · holds: as listed in the answers · src: klindworthEvaluationGeneral16S2013, waltersImprovedBacterial16S2016, abellanschneyderPrimerPipelinesParameters2021, fitzpatrickChloroplastSequenceVariation2018 · trail: MB-01 §answers · from: MB-01:A-005, MB-01:A-006
- **workflow.5** PCR choices are the polymerase, cycle number, input amount and single versus pooled replicate reactions.
  conf: not stated · class: not stated · holds: as listed in the answers · src: none (the reviewer's synthesis) · trail: MB-01 §answers · from: MB-01:A-007
- **workflow.6** Library preparation and indexing use one-step fusion, two-step tailed or ligation designs, with single, combinatorial or unique dual indexes.
  conf: not stated · class: not stated · holds: as listed in the answers · src: none (the reviewer's synthesis) · trail: MB-01 §answers · from: MB-01:A-009
- **workflow.7** Platform and read length choices are MiSeq 2x250 or 2x300, HiSeq, NovaSeq, Ion Torrent, 454, or PacBio CCS full length.
  conf: not stated · class: not stated · holds: as listed in the answers · src: none (the reviewer's synthesis) · trail: MB-01 §answers · from: MB-01:A-010
- **workflow.8** Demultiplexing is done with or without filtering on index-read quality.
  conf: not stated · class: not stated · holds: as listed in the answers · src: wrightQualityFilteringIllumina2016 · trail: MB-01 §answers · from: MB-01:A-011
- **workflow.9** Quality filtering and merging set quality, length, expected-error and abundance thresholds, plus the delta-Q rule when merging.
  conf: not stated · class: not stated · holds: as listed in the answers · src: bokulichQualityfilteringVastlyImproves2013, kozichDevelopmentDualindexSequencing2013 · trail: MB-01 §answers · from: MB-01:A-012
- **workflow.10** Error handling uses 97% or 99% OTUs (de novo, closed or open reference) or ASVs from DADA2, Deblur or UNOISE3; DADA2 can process samples independently, pooled or pseudo-pooled.
  conf: not stated · class: not stated · holds: as listed in the answers · src: none (the reviewer's synthesis) · trail: MB-01 §answers · from: MB-01:A-013
- **workflow.11** Chimera detection uses UCHIME, UCHIME2 or ChimeraSlayer.
  conf: not stated · class: not stated · holds: as listed in the answers · src: none (the reviewer's synthesis) · trail: MB-01 §answers · from: MB-01:A-014
- **workflow.12** Taxonomy is assigned with RDP NBC, q2-feature-classifier, SINTAX, IDTAXA or MAPseq against SILVA, Greengenes, RDP or GTDB-type references, optionally with habitat-weighted priors.
  conf: not stated · class: not stated · holds: as listed in the answers · src: kaehlerSpeciesAbundanceInformation2019 · trail: MB-01 §answers · from: MB-01:A-015
- **workflow.13** Contaminants are handled by dropping taxa seen in negative controls, decontam (frequency or prevalence mode), SourceTracker, or relative-abundance cutoffs.
  conf: not stated · class: not stated · holds: as listed in the answers · src: none (the reviewer's synthesis) · trail: MB-01 §answers · from: MB-01:A-016
- **workflow.14** In a survey of 265 papers in the 2018 issues of Microbiome and The ISME Journal that used any high-throughput community sequencing (16S, shotgun, metatranscriptomics, ITS, 18S and others), 30% (79) reported a negative control and 10% (27) a positive control; it is not a 16S-only figure.
  conf: single (critic: MB-01:C-005) · class: meas (marker) · holds: two journals, 2018, all high-throughput community sequencing types, not 16S amplicon practice alone · src: hornungIssuesCurrentStandards2019 (FT; meas; single) · trail: MB-01 §critic, §2.13, §answers · rating: "weak" · from: MB-01:C-004, MB-01:C-005, MB-01:C-132, MB-01:I-0073, MB-01:A-017, MB-01:A-019, MB-01:A-033, MB-01:C-003
- **workflow.15** How often each workflow choice is made across the field is unmeasured apart from controls.
  conf: not stated · class: search (note: "No source found on how often each choice is used across the field") · holds: the usage survey of controls is the only one found · src: hornungIssuesCurrentStandards2019 · trail: MB-01 §answers, §critic · search: searched, not found (note: "No source found on how often each choice is used across the field") · from: MB-01:A-026, MB-01:C-009, MB-01:A-295
- **workflow.16** Field sampling choices for water (volume, filter pore size) and for host tissue are unsearched on the review's own Search record, so no source on their effect was reported.
  conf: not stated · class: search (critic: MB-01:C-008) · holds: water sampling and host tissue sampling; section 2.1 says the lab angle searched preservation and storage terms, the Search record says no angle searched these choices · src: none (the review's search record) · trail: MB-01 §critic, §2.1, §Provenance, §Search record · search: not searched (critic: MB-01:C-008) · from: MB-01:C-006, MB-01:C-007, MB-01:C-008, MB-01:C-012, MB-01:A-027, MB-01:B-0087, MB-01:B-0088, MB-01:B-0018, MB-01:B-0384
- **workflow.17** There is no conflict over what the steps are, but the recommended choice within steps is disputed: quality-filter stringency (Bokulich 2013 versus Kopylova 2016), OTUs versus ASVs (Schloss 2021 versus the ASV developers), and pooled versus single PCR (Marotz 2019 and Smith and Peay 2014 versus the triplicate pooling in the EMP protocol).
  conf: cont (note: "the recommended choice is disputed") · class: not stated · holds: within-step choices · src: bokulichQualityfilteringVastlyImproves2013, kopylovaOpensourceSequenceClustering2016, schlossAmpliconSequenceVariants2021, marotzTriplicatePCRReactions2019, smithSequenceDepthNot2014, earth16SIlluminaAmplicon · trail: MB-01 §answers, §6. Where · from: MB-01:A-020, MB-01:A-021, MB-01:A-022, MB-01:A-023, MB-01:A-024, MB-01:A-025, MB-01:B-0020, MB-01:B-0336

### departure: departure of observed from known composition
needs: workflow
- **departure.bg1** A mock community is a set of microbial strains of known composition, sequenced so that the observed composition can be compared with the known one; mock communities are a tool for validating, optimising and comparing methods for microbial community analysis.
  kind: background · ref: bokulichMockrobiotaPublicResource2016 · check: DOI 10.1128/mSystems.00062-16 resolves on Crossref; the abstract's first sentence names mock communities as a tool for validating, optimizing and comparing bioinformatics methods, and it describes mock community data sets with known species compositions
- **departure.1** Every mock-community study in the body found observed composition departing from known composition; several independent full-text mock and dilution studies show departures.
  conf: repl (critic: MB-01:C-010) · class: meas (marker) · holds: mock-community and dilution studies (Brooks 2015, Fouhy 2016, Pinto and Raskin 2012, D'Amore 2016, Karstens 2019, Silverman 2021, Sze and Schloss 2019) · src: brooksTruthMetagenomicsQuantifying2015 (FT; meas; cont), fouhy16SRRNAGene2016 (FT; meas; repl), pintoPCRBiasesDistort2012 (FT; meas; repl), damoreComprehensiveBenchmarkingStudy2016 (FT; meas; repl), karstensControllingContaminantsLowbiomass2019, silvermanMeasuringMitigatingPCR2021, szeImpactDNAPolymerase2019 · trail: MB-01 §critic, §Adversarial, §1. Overview, §answers · rating: "Strong qualitatively" · from: MB-01:C-010, MB-01:C-145, MB-01:C-146, MB-01:A-034, MB-01:B-0033, MB-01:I-0001, MB-01:A-301, MB-01:C-022, MB-01:A-133
- **departure.2** The size of the bias depends on platform, region, primer, extraction and pipeline.
  conf: mixed (marker) · class: meas (marker) · holds: as stated · src: damoreComprehensiveBenchmarkingStudy2016 (FT; meas; repl), fouhy16SRRNAGene2016 (FT; meas; repl), pintoPCRBiasesDistort2012 (FT; meas; repl), brooksTruthMetagenomicsQuantifying2015 (FT; meas; cont) · trail: MB-01 §1. Overview · from: MB-01:I-0001
- **departure.3** Departures are measured at most steps examined but not at all of them: field sampling for water and host tissue was not searched, and several choices showed little or no detectable effect (PCR replicate pooling, preparation day and lane, cycle number in some studies, and storage in one soil, relative to between-soil differences).
  conf: not stated · class: not stated · holds: the steps the body examined · src: none (the critic's reading of the review's body and search record) · trail: MB-01 §critic, §Adversarial · contrary: not stated · from: MB-01:C-011, MB-01:C-012, MB-01:C-013, MB-01:C-147, MB-01:C-148, MB-01:C-149
- **departure.4** Steps or choices found to matter little include storage relative to between-soil differences, PCR replication and pooling, preparation day and lane, cycle number in some studies, extraction method in one gut mock, relic DNA in one multi-environment study, PNA type for bacterial diversity, OTU versus ESV for broad patterns, rarefaction for beta diversity in real river data, library normalisation relative to metric choice, and operating system for pipeline output.
  conf: not stated · class: not stated · holds: each in the study or studies named for it · src: rubinInvestigatingImpactStorage2013, marotzTriplicatePCRReactions2019, kennedyEvaluatingBiasIlluminabased2014, smithSequenceDepthNot2014, siposEffectPrimerMismatch2007, acinasPCRinducedSequenceArtifacts2005, fouhy16SRRNAGene2016, lennonHowWhereRelic2018, fitzpatrickChloroplastSequenceVariation2018, glassmanBroadscaleEcologicalPatterns2018, chiarelloRankingBiasesChoice2022, thorsenLargescaleBenchmarkingReveals2016, marizzoniComparisonBioinformaticsPipelines2020 · trail: MB-01 §7. Bounds · from: MB-01:B-0344..0355
- **departure.5** Corrections that failed or introduced new errors include copy-number normalisation on mocks, copy-number prediction tools, UNBIAS, removing every taxon seen in negative controls, SourceTracker with undefined sources, stringent filtering, internal standards before correction, ANCOM-BC at small sample sizes, and fitZig.
  conf: not stated · class: not stated · holds: each in the study named for it · src: starke16SRRNAGene2020, loucaCorrecting16SRRNA2018, edgarUNBIASAttemptCorrect2017, karstensControllingContaminantsLowbiomass2019, kopylovaOpensourceSequenceClustering2016, linTowardsQuantitativeMicrobiome2019, wirbelRealisticBenchmarkDifferential2024 · trail: MB-01 §7. Bounds · from: MB-01:B-0356..0365

### sampling-storage: field sampling, preservation and storage
needs: departure
- **sampling-storage.1** Unpreserved faecal samples and samples in 70% ethanol at ambient temperature changed composition by amounts comparable to the differences between individual humans.
  conf: repl (marker) · class: meas (marker) · holds: faeces at ambient temperature · src: songPreservationMethodsDiffer2016 (FT; meas; repl) · trail: MB-01 §2.1, §answers · from: MB-01:I-0004, MB-01:A-038, MB-01:A-036, MB-01:B-0049, MB-01:B-0050, MB-01:A-037
- **sampling-storage.2** Human and dog faeces held at ambient temperature for 8 weeks changed by about as much as technical replicates differ when kept in 95% ethanol, on FTA cards or in OMNIgene Gut.
  conf: not stated · class: not stated · holds: human and dog faeces, 8 weeks at ambient temperature · src: songPreservationMethodsDiffer2016 · trail: MB-01 §2.1 · from: MB-01:B-0080
- **sampling-storage.3** Storage altered taxon frequencies more than presence or absence: weighted UniFrac effects exceeded unweighted, and the number of taxa was affected less.
  conf: not stated · class: not stated · holds: faeces · src: songPreservationMethodsDiffer2016 · trail: MB-01 §2.1, §answers · from: MB-01:B-0081, MB-01:A-037, MB-01:A-039, MB-01:B-0051
- **sampling-storage.4** FTA cards produced a systematic shift that could be detrended, the one storage effect shown to be consistent across samples; for the other preservation methods consistency was not measured.
  conf: not stated · class: not stated · holds: FTA cards and the other preservation methods · src: songPreservationMethodsDiffer2016 · trail: MB-01 §2.1, §answers · from: MB-01:B-0082, MB-01:A-040, MB-01:B-0052
- **sampling-storage.5** Storage changes in a soil were small relative to the differences among more than 500 Earth Microbiome Project soils.
  conf: repl (marker) · class: meas (marker) · holds: a single soil stored, compared with more than 500 EMP soils · src: rubinInvestigatingImpactStorage2013 (FT; meas; repl) · trail: MB-01 §2.1, §answers, §7. Bounds · from: MB-01:I-0005, MB-01:A-041, MB-01:B-0345
- **sampling-storage.6** Storage for 1 to 14 days at room temperature, 4 C or -20 C changed a single soil's community, most at 3 to 7 days and least when frozen.
  conf: not stated · class: not stated · holds: one soil · src: rubinInvestigatingImpactStorage2013 · trail: MB-01 §2.1 · from: MB-01:B-0083
- **sampling-storage.7** In Lauber et al. 2010, as described by Rubin, between-sample variation outweighed storage effects at 1,304 to 3,022 sequences per sample.
  conf: not stated · class: not stated · holds: known only through Rubin et al. 2013's description · src: lauberEffectStorageConditions2010 (SEC) · trail: MB-01 §2.1, §Sources not obtained · limit: access (note: "known only through Rubin's description") · from: MB-01:B-0084, MB-01:R-0012, MB-01:R-0615
- **sampling-storage.8** In one agricultural field, extracting 0.25, 1, 5, 10 or 100 g of soil changed community structure, replicate dispersion and OTU counts; ten-gram extractions gave the highest diversity and the lowest dispersion.
  conf: single (marker) · class: meas (marker) · holds: one agricultural field, soil masses of 0.25 to 100 g · src: pentonSizeMattersAssessing2016 (FT; meas; single) · trail: MB-01 §2.1, §answers · from: MB-01:I-0006, MB-01:B-0085, MB-01:B-0086, MB-01:A-003

### extraction: DNA extraction
needs: departure
- **extraction.1** In McLaren et al.'s reanalysis of Brooks et al.'s 80 cell mixtures of 7 vaginal taxa, the extraction step had a maximum pairwise bias of 36.6-fold and a mean of 5.5-fold, the largest single step in that mock.
  conf: single (critic: MB-01:C-017) · class: deriv/model (marker) · holds: 80 cell mixtures of 7 vaginal taxa, V1-V3, 454; one dataset · src: mclarenConsistentCorrectableBias2019 (FT, re-opened; deriv/model; single dataset) · trail: MB-01 §2.2, §answers, §critic · from: MB-01:I-0007, MB-01:B-0089, MB-01:A-042, MB-01:A-043, MB-01:B-0053, MB-01:C-015, MB-01:C-017
- **extraction.2** In Brooks et al.'s own analysis, median total bias per taxon ranged from -32.6% to +39.1% of true proportion.
  conf: cont (marker) · class: meas (marker) · holds: the Brooks 2015 cell mixtures · src: brooksTruthMetagenomicsQuantifying2015 (FT; meas; cont) · trail: MB-01 §2.2 · from: MB-01:I-0008, MB-01:B-0093, MB-01:I-0007
- **extraction.3** In Brooks et al.'s data, error from bias exceeded 85% in some samples, while technical variation was under 5% for most taxa.
  conf: cont (marker) · class: meas (marker) · holds: the Brooks 2015 cell mixtures · src: brooksTruthMetagenomicsQuantifying2015 (FT; meas; cont) · trail: MB-01 §2.2, §4.4, §answers · from: MB-01:I-0008, MB-01:B-0094, MB-01:A-205, MB-01:B-0254, MB-01:I-0007
- **extraction.4** In Brooks et al.'s data, swapping extraction kits changed Enterococcus by about 50%.
  conf: cont (marker) · class: meas (marker) · holds: the Brooks 2015 cell mixtures · src: brooksTruthMetagenomicsQuantifying2015 (FT; meas; cont) · trail: MB-01 §2.2 · from: MB-01:I-0008, MB-01:B-0095, MB-01:I-0007
- **extraction.5** In activated sludge, harder bead beating increased DNA from Gram-positive bacteria by up to 400%.
  conf: repl (marker) · class: meas (marker) · holds: activated sludge · src: albertsenBackBasicsInfluence2015 (FT; meas; repl) · trail: MB-01 §2.2, §answers · from: MB-01:I-0009, MB-01:A-044, MB-01:B-0054
- **extraction.6** In activated sludge, bead-beating intensity and primer choice had the largest effects of all parameters tested.
  conf: not stated · class: not stated · holds: activated sludge · src: albertsenBackBasicsInfluence2015 · trail: MB-01 §2.2 · from: MB-01:B-0096
- **extraction.7** In a 20-species gut mock, two extraction methods (QIAamp stool kit versus repeat bead beating) gave "very similar" data, and primer and platform mattered more.
  conf: repl (marker) · class: meas (marker) · holds: one 20-species gut mock · src: fouhy16SRRNAGene2016 (FT; meas; repl) · trail: MB-01 §2.2, §answers, §7. Bounds · from: MB-01:B-0097, MB-01:I-0010, MB-01:A-045, MB-01:B-0055, MB-01:B-0349
- **extraction.8** The size of the extraction effect is contested: Fouhy 2016 against Albertsen 2015, Brooks 2015 and MBQC.
  conf: cont (critic: MB-01:C-016) · class: not stated · holds: the studies named · src: fouhy16SRRNAGene2016, albertsenBackBasicsInfluence2015, brooksTruthMetagenomicsQuantifying2015, sinhaAssessmentVariationMicrobial2017 · trail: MB-01 §answers, §6. Where, §critic · from: MB-01:A-117, MB-01:B-0332, MB-01:C-016
- **extraction.9** In the MBQC artificial communities, the largest contributor to inaccuracy was contamination or omission of microbes whose DNA was not extracted; species whose DNA was never extracted were missing.
  conf: not stated · class: not stated · holds: the MBQC artificial communities · src: sinhaAssessmentVariationMicrobial2017 · trail: MB-01 §2.2, §answers · from: MB-01:B-0098, MB-01:A-046, MB-01:B-0055
- **extraction.10** Absolute diversity was not comparable between laboratories even with the same pipeline.
  conf: not stated · class: not stated · holds: the MBQC interlaboratory comparison · src: sinhaAssessmentVariationMicrobial2017 · trail: MB-01 §2.2 · from: MB-01:B-0099, MB-01:I-0011
- **extraction.11** No more than 6% of inoculated lambda DNA was recovered from six soils.
  conf: repl (marker) · class: meas (marker) · holds: six soils; older soil work, indirect and pre-NGS · src: frostegardQuantificationBiasRelated1999 (AB; meas; repl) · trail: MB-01 §2.2 · from: MB-01:I-0014
- **extraction.12** Extraction method changed fingerprint profiles of soil communities.
  conf: repl (marker) · class: meas (marker) · holds: older soil work, indirect and pre-NGS · src: martinlaurentDNAExtractionSoils2001 (AB; meas; repl) · trail: MB-01 §2.2 · from: MB-01:I-0015, MB-01:I-0014
- **extraction.13** Extraction yield varied between samples: a synthetic spike-in quantified before and after extraction recovered 40% to 84%.
  conf: single (marker) · class: meas (marker) · holds: one spike-in study · src: zembAbsoluteQuantitationMicrobes2020 (FT; meas; single) · trail: MB-01 §2.2, §2.14, §5.5, §answers · from: MB-01:I-0016, MB-01:A-050, MB-01:B-0057, MB-01:B-0191, MB-01:B-0319

### relic-dna: relic (extracellular) DNA
needs: extraction
- **relic-dna.1** Across soils, an average 40% of DNA was extracellular or from non-intact cells; removing it with propidium monoazide showed relic DNA inflated richness by up to 55% (more so at high pH, not at all in some soils) and misestimated relative abundances.
  conf: cont (marker) · class: meas (marker) · holds: soils; one study · src: cariniRelicDNAAbundant2016 (AB; meas; cont) · trail: MB-01 §2.2, §answers, MB-02 §D3.3, §answers · from: MB-01:I-0012, MB-01:A-047, MB-01:B-0056, MB-02:B-0270, MB-02:A-109
- **relic-dna.2** Relic DNA averaged 33% across soil, sediment, water and mammalian gut (over 80% in some samples) but had minimal effect on diversity estimates.
  conf: cont (marker) · class: meas (marker) · holds: soil, sediment, water and mammalian gut; one multi-environment study · src: lennonHowWhereRelic2018 (FT; meas; cont) · trail: MB-01 §2.2, §7. Bounds, MB-02 §D3.3 · from: MB-01:I-0013, MB-01:B-0350, MB-02:B-0271
- **relic-dna.3** Models predict that relic DNA biases diversity estimates only when relic and intact abundance distributions differ.
  conf: cont (marker) · class: meas (marker) · holds: Lennon et al.'s models · src: lennonHowWhereRelic2018 (FT; meas; cont) · trail: MB-01 §2.2 · from: MB-01:I-0013
- **relic-dna.4** Whether relic DNA matters is contested: Carini 2016 against Lennon 2018.
  conf: cont (note: "Relic DNA effects conflict") · class: not stated · holds: the two studies named · src: cariniRelicDNAAbundant2016, lennonHowWhereRelic2018 · trail: MB-01 §answers, §6. Where, MB-02 §answers, §D3.3 · from: MB-01:A-118, MB-01:B-0333, MB-01:B-0100, MB-02:A-118, MB-02:B-0269

### primers: primers and gene region
needs: departure
- **primers.1** In silico, 175 primers and 512 pairs differ widely in coverage and phylum spectrum against SILVA 108.
  conf: repl (marker) · class: deriv (marker) · holds: in silico, SILVA 108 · src: klindworthEvaluationGeneral16S2013 (FT; deriv; repl) · trail: MB-01 §2.3 · from: MB-01:I-0017
- **primers.2** In marine samples, V4 primers under-represented SAR11 and over-represented Gammaproteobacteria; the abstract gives the SAR11 bias (about 4 to 10-fold in field samples against about 2-fold in mocks) for the 515F-Y/806R pair, so mock-measured bias understated field bias for this taxon.
  conf: repl (marker) · class: meas (marker) · holds: marine field samples and mocks; one primer pair (515F-Y/806R) and one taxon (SAR11) · src: paradaEveryBaseMatters2016 (AB; meas; repl) · trail: MB-01 §2.3, §2.14, §Adversarial, §critic · from: MB-01:I-0018, MB-01:B-0104, MB-01:B-0105, MB-01:B-0189, MB-01:B-0058, MB-01:A-052, MB-01:C-056, MB-01:C-070, MB-01:C-020, MB-01:C-092, MB-01:A-051
- **primers.3** On marine clone mocks, 515F-Y/926R fit expected composition with r2 = 0.95, against about 0.5 for 515F-Y/806R.
  conf: not stated · class: not stated · holds: marine clone mocks · src: paradaEveryBaseMatters2016 · trail: MB-01 §2.3 · from: MB-01:B-0103
- **primers.4** Even perfectly matched primers showed preferential amplification.
  conf: not stated · class: not stated · holds: marine samples and mocks · src: paradaEveryBaseMatters2016 · trail: MB-01 §2.3 · from: MB-01:B-0106, MB-01:I-0018, MB-01:B-0103
- **primers.5** Adding degeneracy to 515F and 806R improved detection of Thaumarchaeota and SAR11 in stool, soil and built-environment sets without degrading other taxa.
  conf: repl (marker) · class: meas (marker) · holds: stool, soil and built-environment sets · src: waltersImprovedBacterial16S2016 (FT; meas; repl) · trail: MB-01 §2.3, §answers · from: MB-01:I-0019, MB-01:A-055
- **primers.6** In human stool and mocks with seven primer pairs, Verrucomicrobia appeared only with V3-V4, V4, V6-V8 and V7-V9 primers: whole phyla appeared or disappeared with primer choice.
  conf: repl (marker) · class: meas (marker) · holds: human stool and mocks, seven primer pairs · src: abellanschneyderPrimerPipelinesParameters2021 (FT; meas; repl) · trail: MB-01 §2.3, §answers · from: MB-01:I-0020, MB-01:A-054, MB-01:B-0059
- **primers.7** In a gut mock, 55 to 80% of expected species were detected, and 29 to 80% of detected species were misidentified or false hits, depending on primer, platform and extraction.
  conf: not stated · class: not stated · holds: one gut mock · src: fouhy16SRRNAGene2016 · trail: MB-01 §2.3 · from: MB-01:B-0107
- **primers.8** Preferential amplification of a matched template over a mismatched one (63F) rose almost exponentially as annealing temperature went from 47 to 61 C; a perfectly matched primer showed no such effect.
  conf: single (marker) · class: meas (marker) · holds: T-RFLP, pre-NGS · src: siposEffectPrimerMismatch2007 (AB; meas; single; T-RFLP, pre-NGS) · trail: MB-01 §2.3 · from: MB-01:I-0021
- **primers.9** With universal PNA clamps, host plastid reads averaged 23% across 32 plant species but reached 62 to 94% in some lineages.
  conf: single (marker) · class: meas (marker) · holds: 32 plant species · src: fitzpatrickChloroplastSequenceVariation2018 (FT; meas; single) · trail: MB-01 §2.3, §answers · from: MB-01:I-0022, MB-01:A-053, MB-01:B-0059
- **primers.10** A modified PNA clamp cut Asteraceae contamination from 65% to 23% but raised it from 12% to 69% in other species.
  conf: not stated · class: not stated · holds: plant host species · src: fitzpatrickChloroplastSequenceVariation2018 · trail: MB-01 §2.3 · from: MB-01:B-0108, MB-01:I-0022
- **primers.11** PNA type did not detectably change bacterial alpha or beta diversity.
  conf: not stated · class: not stated · holds: plant host species · src: fitzpatrickChloroplastSequenceVariation2018 · trail: MB-01 §2.3, §7. Bounds · from: MB-01:B-0109, MB-01:B-0351, MB-01:I-0022
- **primers.12** The makers of PCR clamps state that clamps enrich microbial sequences "without introducing bias".
  conf: not stated · class: not stated · holds: a makers' claim · src: lundbergPracticalInnovationsHighthroughput2013 (AB; makers' claim) · trail: MB-01 §2.3 · from: MB-01:B-0110
- **primers.13** In silico, 56% of V4 amplicons failed to match their species of origin with confidence, while full-length sequences classified nearly all correctly.
  conf: single (marker) · class: deriv (marker) · holds: in silico · src: johnsonEvaluation16SRRNA2019 (FT; deriv; single) · trail: MB-01 §2.3 · from: MB-01:I-0023

### pcr: PCR conditions, cycle number and per-cycle efficiency
needs: departure, primers
- **pcr.1** Two-template 27F-338R mixtures converged toward 1:1 products regardless of starting ratio; the bias depended strongly on cycle number and fit a kinetic model of product reannealing.
  conf: repl (marker) · class: meas (marker) · holds: two-template mixtures · src: suzukiBiasCausedTemplate1996 (AB; meas; repl) · trail: MB-01 §2.4, §answers · from: MB-01:I-0024, MB-01:A-060, MB-01:B-0062
- **pcr.2** Reproducible over-amplification of specific templates in genomic mixtures was explained largely by primer binding energy, not copy number, and was reduced by higher template concentration, fewer cycles and pooling of reactions.
  conf: repl (marker) · class: meas (marker) · holds: genomic mixtures · src: polzBiasTemplatetoproductRatios1998 (AB; meas; repl) · trail: MB-01 §2.4 · from: MB-01:I-0025
- **pcr.3** In a 20-strain mock, genomic GC content correlated negatively with observed abundance; high-GC templates were also under-represented in Pinto and Raskin 2012.
  conf: not stated · class: not stated · holds: a 20-strain mock; Pinto and Raskin 2012 · src: laursenGenomicGCcontentAffects2017, pintoPCRBiasesDistort2012 · trail: MB-01 §2.4, §answers · from: MB-01:B-0111, MB-01:B-0112, MB-01:A-061, MB-01:B-0063
- **pcr.4** Longer initial denaturation raised the three highest-GC members of a 20-strain mock but did not change overall evenness.
  conf: single (marker) · class: meas (marker) · holds: a 20-strain mock · src: laursenGenomicGCcontentAffects2017 (FT; meas; single) · trail: MB-01 §2.4 · from: MB-01:I-0026, MB-01:B-0111
- **pcr.5** In a gut-isolate mock with primer mismatch removed by pre-amplification, log-ratios changed linearly with cycle number from 10 to 35 cycles.
  conf: single (marker) · class: meas (marker) · holds: one gut-isolate mock, primer mismatch removed · src: silvermanMeasuringMitigatingPCR2021 (FT; meas; single) · trail: MB-01 §2.4, §answers · from: MB-01:I-0027, MB-01:A-059
- **pcr.6** After 35 cycles relative abundances were biased by an average factor of 2.6 per taxon (95% credible set 2.3 to 2.9), and the B. longum to E. faecalis ratio shifted about 16-fold.
  conf: single (note: "single study") · class: not stated · holds: a gut mock with primer mismatch removed · src: silvermanMeasuringMitigatingPCR2021 · trail: MB-01 §2.4, §answers, §critic · from: MB-01:B-0113, MB-01:A-057, MB-01:A-058, MB-01:B-0060, MB-01:C-054, MB-01:A-056
- **pcr.7** In four artificial-gut communities about 19% of taxa were more than 4-fold biased.
  conf: single (note: "single study") · class: not stated · holds: four artificial-gut communities · src: silvermanMeasuringMitigatingPCR2021 · trail: MB-01 §2.4, §answers · from: MB-01:B-0114, MB-01:A-058, MB-01:B-0061
- **pcr.8** PCR-bias calibration corrected composition toward truth in all 10 held-out mocks; the authors note that their mock "ground truth" carried its own bias and that the method sometimes estimated the wrong direction for some taxa.
  conf: not stated · class: not stated · holds: 10 held-out mocks · src: silvermanMeasuringMitigatingPCR2021 · trail: MB-01 §2.4 · from: MB-01:B-0115, MB-01:B-0116
- **pcr.9** PCR bias was consistent per taxon in mocks.
  conf: not stated · class: not stated · holds: mocks · src: silvermanMeasuringMitigatingPCR2021 · trail: MB-01 §answers · from: MB-01:A-064, MB-01:B-0064
- **pcr.10** Sze and Schloss tested five polymerases at 20 to 35 cycles; in the mock, error rate, chimera fraction and deviation from the expected profile all rose with cycle number.
  conf: single (marker) · class: meas (marker) · holds: one mock · src: szeImpactDNAPolymerase2019 (FT, re-opened; meas; single) · trail: MB-01 §2.4 · from: MB-01:I-0028, MB-01:B-0117
- **pcr.11** In stool, the sample explained R2 = 0.79 of variation, cycles 0.044 and polymerase 0.033, and "this bias was inconsistent for human stool samples": cycle-related shifts were inconsistent across stool samples and small next to between-person differences.
  conf: single (marker) · class: meas (marker) · holds: four stool samples · src: szeImpactDNAPolymerase2019 (FT, re-opened; meas; single) · trail: MB-01 §2.4, §2.14, §answers, §critic · from: MB-01:I-0028, MB-01:B-0118, MB-01:A-065, MB-01:B-0065, MB-01:B-0190, MB-01:C-020
- **pcr.12** Template-to-product ratios were little affected by cycle number.
  conf: single (marker) · class: meas (marker) · holds: one study · src: siposEffectPrimerMismatch2007 (AB; meas; single) · trail: MB-01 §2.4 · from: MB-01:I-0029, MB-01:B-0119
- **pcr.13** Clone libraries amplified for different numbers of cycles showed no detectable skew.
  conf: single (marker) · class: meas (marker) · holds: Sanger clone libraries · src: acinasPCRinducedSequenceArtifacts2005 (AB; meas; single; Sanger) · trail: MB-01 §2.4 · from: MB-01:I-0030, MB-01:B-0119
- **pcr.14** 30 versus 35 cycles changed proportions only slightly.
  conf: not stated · class: not stated · holds: one study (Brooks 2015) · src: brooksTruthMetagenomicsQuantifying2015 · trail: MB-01 §2.4, §answers · from: MB-01:B-0120, MB-01:A-062
- **pcr.15** The effect of cycle number conflicts between studies: small effects (Sipos 2007, Acinas 2005, Brooks 2015 at 30 versus 35 cycles) against growing bias (Suzuki 1996, Silverman 2021, the Sze and Schloss 2019 mock), with Sze and Schloss also finding inconsistent effects in stool.
  conf: not stated · class: not stated · holds: mixtures, mocks and stool · src: siposEffectPrimerMismatch2007, acinasPCRinducedSequenceArtifacts2005, brooksTruthMetagenomicsQuantifying2015, suzukiBiasCausedTemplate1996, silvermanMeasuringMitigatingPCR2021, szeImpactDNAPolymerase2019 · trail: MB-01 §answers, §6. Where · from: MB-01:A-062, MB-01:A-116, MB-01:B-0330, MB-01:B-0331, MB-01:B-0064, MB-01:B-0348
- **pcr.16** Low template (0.1 ng versus 5 to 10 ng) increased profile variability in soil and faecal samples; pooling of PCRs, preparation day and lane did not.
  conf: single (marker) · class: meas (marker) · holds: soil and faecal samples · src: kennedyEvaluatingBiasIlluminabased2014 (AB; meas; single) · trail: MB-01 §2.4, §4.3, §answers, §7. Bounds · from: MB-01:I-0031, MB-01:B-0121, MB-01:A-090, MB-01:B-0247, MB-01:B-0346, MB-01:B-0347
- **pcr.17** Single versus triplicate pooled PCRs made no significant difference.
  conf: repl (marker) · class: meas (marker) · holds: one study; an open PMC copy exists, so the abstract-only label understates access · src: marotzTriplicatePCRReactions2019 (AB; meas; repl) · trail: MB-01 §2.4 · from: MB-01:I-0032, MB-01:C-080
- **pcr.18** In fungal ITS, pooling 1 to 16 PCR replicates had no detectable effect on alpha or beta diversity.
  conf: not stated · class: meas (marker) · holds: fungal ITS, indirect for 16S · src: smithSequenceDepthNot2014 (FT; meas; INDIRECT) · trail: MB-01 §2.4 · from: MB-01:I-0033
- **pcr.19** Pooling PCR replicates had no detectable effect, and pooled versus single PCR made no difference at moderate to high input, but replicates split before PCR disagreed strongly at low load.
  conf: not stated · class: not stated · holds: moderate to high input (Kennedy 2014, Marotz 2019, Smith and Peay 2014) against low load (Dyrhovden 2021); no single study tested both conditions · src: kennedyEvaluatingBiasIlluminabased2014, marotzTriplicatePCRReactions2019, smithSequenceDepthNot2014, dyrhovdenManagingContaminationDiverse2021 · trail: MB-01 §answers · from: MB-01:A-212, MB-01:A-220, MB-01:A-221
- **pcr.20** In low-input pools of unique synthetic barcodes, random per-molecule amplification in early cycles was the main source of skew; late-cycle polymerase errors stayed at low copy number, template switching was rare and GC bias minor.
  conf: single (marker) · class: meas (marker) · holds: synthetic barcode pools, non-16S, indirect · src: kebschullSourcesPCRinducedDistortions2015 (FT; meas; single; INDIRECT, non-16S) · trail: MB-01 §2.4, §answers · from: MB-01:B-0122, MB-01:I-0034, MB-01:A-196
- **pcr.21** At low input, early stochastic amplification and dropout affected the detection of taxa.
  conf: not stated · class: not stated · holds: low input; one source indirect · src: kebschullSourcesPCRinducedDistortions2015, dyrhovdenManagingContaminationDiverse2021 · trail: MB-01 §answers · from: MB-01:A-063, MB-01:B-0064
- **pcr.22** Documented protocols use 35 cycles in triplicate 25 uL reactions, pooling 240 ng per sample (EMP protocol, one-step PCR, checked on the live page), or 25 amplicon cycles plus 8 index cycles with 12.5 ng input (Illumina guide, two-step).
  conf: not stated · class: not stated · holds: maker documentation and protocols · src: earth16SIlluminaAmplicon (PROTOCOL), illumina16SMetagenomicSequencing (DOCUMENTATION; maker's claim) · trail: MB-01 §3.1, §2.6, §answers, §critic · rating: "Moderate for documented cycle numbers" · from: MB-01:B-0194, MB-01:B-0128, MB-01:B-0129, MB-01:A-008, MB-01:A-135, MB-01:A-170, MB-01:C-023, MB-01:A-134
- **pcr.23** Experiments used 10 to 35 cycles (Silverman 2021), 15 or 20 to 35 (Sze and Schloss 2019), 20 versus 40 (Salter 2014) and 24 (Laursen 2017).
  conf: not stated · class: not stated · holds: the experimental studies named · src: silvermanMeasuringMitigatingPCR2021, szeImpactDNAPolymerase2019, salterReagentLaboratoryContamination2014, laursenGenomicGCcontentAffects2017 · trail: MB-01 §3.1, §answers · from: MB-01:B-0195, MB-01:A-136
- **pcr.24** Only relative per-cycle efficiencies have been measured: taxon-specific log-ratio changes per cycle that compound to an average 2.6-fold bias after 35 cycles in a gut mock.
  conf: single (note: "single source") · class: not stated · holds: one gut mock · src: silvermanMeasuringMitigatingPCR2021 · trail: MB-01 §3.1, §answers · rating: "Weak for per-cycle efficiencies" · from: MB-01:B-0196, MB-01:B-0197, MB-01:A-137, MB-01:A-138, MB-01:A-171, MB-01:A-185, MB-01:A-132
- **pcr.25** Other per-cycle efficiency values are drawn from beta distributions fitted to eukaryotic eDNA mocks, in a model of amplicons as starting copies x (1 + a_i)^cycles.
  conf: not stated · class: model (marker) · holds: eukaryotic eDNA mocks, indirect · src: kellyUnderstandingPCRProcesses2019 (FT; model; INDIRECT) · trail: MB-01 §3.1, §answers · from: MB-01:I-0078, MB-01:A-139
- **pcr.26** No absolute per-cycle efficiency for universal 16S primers on environmental templates was found.
  conf: not stated · class: search (critic: MB-01:C-113) · holds: the lab angle's routes (Crossref, Europe PMC, web search); the qPCR methods literature was not searched · src: none (a search result) · trail: MB-01 §3.1, §answers, §Search record, §Provenance, §critic · search: not searched (critic: MB-01:C-113) · from: MB-01:B-0198, MB-01:A-140, MB-01:A-304, MB-01:B-0379, MB-01:B-0017, MB-01:C-113, MB-01:C-029


### copy-number: 16S rRNA gene copies per genome
needs: none
- **copy-number.bg1** The 16S rRNA gene, about 1,500 bp long, is present in almost all bacteria, often as a multigene family or in operons, and is the most common genetic marker for bacterial phylogeny and taxonomy.
  kind: background · ref: janda16SRRNAGene2007 · check: DOI 10.1128/JCM.01228-07 resolves on Crossref; stated in the opening paragraph of the full text (PMC2045242)
- **copy-number.1** Bacterial genomes carry 1 to 15 copies of the 16S rRNA gene in every database release and genome survey up to about 2015; the range is consistent across sources, but those sources draw on overlapping NCBI genome sets, so they are not independent replications.
  conf: mixed (inputs: MB-01 repl, MB-02 not stated) · class: deriv (marker) · holds: rrnDB releases (the first: "one to as many as 15 copies"; 2009: 785 bacterial and 69 archaeal strains; 2015: 2,635 bacterial records, 1,383 species), Acinas et al. 2004 and Vetrovsky and Baldrian's 1,690 genomes; sequenced genomes · src: klappenbachRrndbRibosomalRNA2001 (AB), leeRrnDBDocumentingNumber2009 (AB), stoddardRrnDBImprovedTools2015 (FT; deriv; repl), acinasDivergenceRedundancy16S2004 (AB), vetrovskyVariability16SRRNA2013 (FT) · trail: MB-02 §D1.1, §D1.2, §answers, §critic, MB-01 §3.2, §answers · rating: "Strong for the range and the taxon dependence" (critic: MB-02:C-006: consistent across sources, but not independent replications) · from: MB-02:A-001, MB-02:A-009, MB-02:A-017, MB-02:A-126, MB-02:B-0021, MB-02:B-0022, MB-02:B-0023, MB-02:B-0024, MB-02:B-0067, MB-02:B-0068, MB-02:B-0071, MB-02:C-001, MB-02:C-006, MB-01:A-141, MB-01:A-142, MB-01:A-168, MB-01:B-0199, MB-01:B-0200, MB-01:B-0066, MB-01:I-0079, MB-01:A-302, MB-01:C-023
- **copy-number.2** Archaea carry 1 to 4 copies in rrnDB releases up to v5.0 (the 2015 release: 175 archaeal records, 148 species) and 1 to 5 from v5.6, but Acinas et al. 2004 already reported a maximum of five archaeal operons, so the sources conflict on the archaeal maximum.
  conf: cont (critic: MB-02:C-002) · class: deriv (marker) · holds: archaeal genomes, few (148 species in 2015); archaeal maxima of 5 in v5.6 onward include Natronorubrum, Natrinema, Methanococcoides and Methanolobus · src: stoddardRrnDBImprovedTools2015 (FT; deriv; repl), schmidtlaboratoryRrnDBReleaseFiles2025, acinasDivergenceRedundancy16S2004 (AB) · trail: MB-02 §D1.1, §D1.2, §answers, §critic, §Adversarial, MB-01 §3.2, §answers · from: MB-02:A-002, MB-02:A-127, MB-02:B-0042, MB-02:B-0070, MB-02:C-002, MB-02:C-138, MB-01:I-0079, MB-01:A-144
- **copy-number.3** The long-quoted ceiling of 15 is no longer the database maximum: rrnDB v5.6 contains a Photobacterium damselae genome with 21 copies and v5.10 a Mesobacillus maritimus genome with 22, and several Photobacterium and Bacillaceae genomes have 20 to 21; these maxima are the reviewer's own derivation from the release files, and no source checked them against assembly quality.
  conf: not stated · class: deriv (note: "derived by the reviewer") · holds: rrnDB release files v3.1.227 to v5.10, summarised by the reviewer · src: schmidtlaboratoryRrnDBReleaseFiles2025 (FT; statistics derived by reviewer) · trail: MB-02 §D1.1, §answers, §critic, §Adversarial, §Search record · from: MB-02:B-0030, MB-02:B-0031, MB-02:B-0040, MB-02:B-0041, MB-02:B-0043, MB-02:A-011, MB-02:A-018, MB-02:A-130, MB-02:C-007, MB-02:C-141, MB-02:B-0306, MB-02:B-0307
- **copy-number.4** Across rrnDB releases v3.1.227, v4.4.3, v5.0, v5.6 and v5.10, bacterial records rose from 1,297 to 48,053, the record mean from 4.20 (median 3) to 5.52 (median 6), the bacterial range from 1 to 15 to 1 to 22, and the mean of species means from 3.87 to 4.36, while the share of records at one copy fell from 17.5% to 7.5%; the archaeal species mean stayed at 1.66 to 1.73.
  conf: not stated · class: deriv (note: "derived by the reviewer") · holds: the five releases; species grouped by the first two words of the NCBI name, which is approximate · src: schmidtlaboratoryRrnDBReleaseFiles2025 · trail: MB-02 §D1.1 · from: MB-02:B-0031, MB-02:B-0032, MB-02:B-0033, MB-02:B-0034, MB-02:B-0035, MB-02:B-0036, MB-02:B-0037, MB-02:B-0038, MB-02:B-0039
- **copy-number.5** Record-level means rise across releases mainly because of resequencing effort (in v5.10, E. coli contributes 3,902 records, 3,860 at 7 copies; Klebsiella pneumoniae 2,534, mostly 8; Salmonella enterica 1,770, mostly 7), while species-level means move much less (3.9 to 4.4); means therefore differ by counting unit (record mean 5.5 against species mean 4.4 in the same release).
  conf: not stated · class: deriv (note: "derived by the reviewer") · holds: rrnDB releases · src: schmidtlaboratoryRrnDBReleaseFiles2025 · trail: MB-02 §D1.1, §answers · from: MB-02:B-0031, MB-02:B-0044, MB-02:B-0045, MB-02:B-0046, MB-02:A-005, MB-02:A-012
- **copy-number.6** In rrnDB v5.10 the mean of species means is 4.4 (median 4) for bacteria and 1.7 (median 1) for archaea, and 11.3% of bacterial species and 51.6% of archaeal species average one copy.
  conf: not stated · class: deriv (note: "derived") · holds: rrnDB v5.10, species-level summaries · src: schmidtlaboratoryRrnDBReleaseFiles2025 · trail: MB-02 §D1.1, §answers · rating: "Moderate for exact means and shares" · from: MB-02:B-0047, MB-02:A-003, MB-02:A-128, MB-02:A-010
- **copy-number.7** Over 1,690 bacterial genomes (909 species, GenBank 2012; 7,081 16S sequences extracted in silico), copies ranged from 1 to 15 with a mean of 4.2; 15% of genomes carried one copy and 21% two.
  conf: not stated · class: not stated · holds: sequenced genomes, a skewed genome collection · src: vetrovskyVariability16SRRNA2013 (FT) · trail: MB-02 §D1.2, §answers, MB-01 §3.2, §answers · from: MB-02:B-0071, MB-02:A-003, MB-01:B-0202, MB-01:A-143
- **copy-number.8** Mean copy numbers by group in the 1,690 genomes were Acidobacteria 1.0, Alphaproteobacteria 2.2, Deltaproteobacteria 2.7, Actinobacteria 3.1, Betaproteobacteria 3.3, Bacteroidetes 3.5, Firmicutes 5.8 and Gammaproteobacteria 5.8; the Acidobacteria mean rests on 4 genomes from 4 species.
  conf: not stated · class: not stated · holds: sequenced genomes · src: vetrovskyVariability16SRRNA2013 (FT) · trail: MB-02 §D1.2, §answers, §critic, MB-01 §3.2, §answers · from: MB-02:B-0072, MB-02:A-004, MB-02:C-003, MB-02:C-089, MB-01:B-0203, MB-01:A-143
- **copy-number.9** Per-phylum species means in rrnDB v5.10 are Bacillota 6.9 (1,274 species), Pseudomonadota 4.4 (3,050), Bacteroidota 3.8 (662), Actinomycetota 3.5 (1,334), Cyanobacteriota 2.8 (102), Planctomycetota 2.0 (62), Verrucomicrobiota 1.8 (35), Chloroflexota 1.6 (20), Acidobacteriota 1.4 (29), Euryarchaeota 1.9 (332), Thermoproteota 1.0 (65) and Nitrososphaerota 1.1 (18).
  conf: not stated · class: deriv (note: "derived") · holds: rrnDB v5.10, derived · src: schmidtlaboratoryRrnDBReleaseFiles2025 · trail: MB-02 §D1.1, §answers, §critic · from: MB-02:B-0049, MB-02:B-0050, MB-02:B-0051, MB-02:B-0052, MB-02:B-0053, MB-02:B-0054, MB-02:B-0055, MB-02:B-0056, MB-02:B-0057, MB-02:B-0058, MB-02:B-0059, MB-02:B-0060, MB-02:B-0061, MB-02:A-004, MB-02:A-128, MB-02:C-004
- **copy-number.10** Phyla common in soil but poorly represented among genomes (Acidobacteriota, Verrucomicrobiota, Chloroflexota) sit at the low end of copy number on small numbers of species, so these soil-relevant low values are imprecise, and the soil correction example (Acidobacteria 50.1% to 66.0%) depends on them.
  conf: not stated · class: not stated · holds: sequenced genomes of soil-relevant phyla (Acidobacteria 1.0 from 4 genomes; rrnDB v5.10 Acidobacteriota 1.4 from 29 species) · src: schmidtlaboratoryRrnDBReleaseFiles2025, vetrovskyVariability16SRRNA2013 · trail: MB-02 §D1.1, §critic · from: MB-02:B-0062, MB-02:C-003, MB-02:C-004, MB-02:C-005
- **copy-number.11** Copy number depends strongly on taxon: the distribution is right-skewed and strongly taxon-structured, and taxon dependence is the strongest regularity.
  conf: not stated · class: not stated · holds: sequenced genomes · src: vetrovskyVariability16SRRNA2013, schmidtlaboratoryRrnDBReleaseFiles2025 · trail: MB-02 §D1.1, §answers · rating: "Strong for the range and the taxon dependence" · from: MB-02:B-0048, MB-02:A-003, MB-02:A-128, MB-02:A-129, MB-02:A-009
- **copy-number.12** 16S copy number carries a moderate phylogenetic signal (K = 0.48 on 484 taxa).
  conf: not stated · class: not stated · holds: 484 taxa · src: kembelIncorporating16SGene2012 (FT) · trail: MB-02 §D1.2 · from: MB-02:B-0074
- **copy-number.13** Copy number is "strongly linked" to taxonomy across 2,900 genomes, and Archaea are potentially under-represented in amplicon profiles.
  conf: not stated · class: not stated · holds: 2,900 genomes · src: anglyCopyRighterRapidTool2014 (AB) · trail: MB-02 §D1.2 · from: MB-02:B-0075
- **copy-number.14** Copy number was less conserved across taxonomic levels than genome size.
  conf: not stated · class: not stated · holds: 1,690 bacterial genomes · src: vetrovskyVariability16SRRNA2013 (FT) · trail: MB-02 §D1.2 · from: MB-02:B-0073, MB-02:B-0071
- **copy-number.15** Among 301 species with at least two records in the 2015 rrnDB release, 77% had identical counts, 16% differed by one copy and 3% by more than two.
  conf: not stated · class: deriv (note: "measured from genomes; derived class") · holds: rrnDB 2015, species with at least two genome records · src: stoddardRrnDBImprovedTools2015 (FT) · trail: MB-02 §D1.1, §answers · from: MB-02:B-0027, MB-02:A-006, MB-02:B-0024, MB-02:B-0025
- **copy-number.16** Of 1,038 species with at least five genomes in rrnDB v5.10, 44% show some within-species variation in copy number, although the median range is 0.
  conf: not stated · class: deriv (note: "derived") · holds: rrnDB v5.10, derived · src: schmidtlaboratoryRrnDBReleaseFiles2025 · trail: MB-02 §D1.1, §answers · from: MB-02:B-0063, MB-02:B-0064, MB-02:A-006
- **copy-number.17** In the reviewer's reading, part of the within-species variation in rrnDB v5.10 is likely assembly error rather than biology (for example, 18 of 3,902 E. coli records report a single copy); it is not a tested claim.
  conf: not stated · class: reading (note: "In the reviewer's reading") · holds: rrnDB v5.10 · src: none (the reviewer's reading) · trail: MB-02 §D1.1, §answers · from: MB-02:B-0065, MB-02:A-013
- **copy-number.18** The two within-species figures differ: 77% of species identical in 2015 against 44% of well-sampled species showing some variation in v5.10; the 2015 figure used far fewer genomes.
  conf: not stated · class: not stated · holds: rrnDB 2015 against v5.10 · src: stoddardRrnDBImprovedTools2015, schmidtlaboratoryRrnDBReleaseFiles2025 · trail: MB-02 §D1.1, §answers · from: MB-02:A-013, MB-02:B-0066
- **copy-number.19** Copy-number distributions within a family can be bimodal: in Enterobacteriaceae (1 to 9 copies) a low-copy peak is made up of insect symbionts.
  conf: not stated · class: not stated · holds: rrnDB 2015 · src: stoddardRrnDBImprovedTools2015 (FT) · trail: MB-02 §D1.1, MB-01 §3.2 · from: MB-02:B-0025, MB-02:B-0026, MB-01:B-0201
- **copy-number.20** Means over all genomes mislead because some species are over-represented among genomes.
  conf: not stated · class: not stated · holds: rrnDB · src: stoddardRrnDBImprovedTools2015 · trail: MB-01 §3.2 · from: MB-01:B-0201
- **copy-number.21** From rrnDB version 5.0 onward, 16S genes are counted by BLAST against gap-free NCBI assemblies rather than from annotation, so genome records report 16S gene counts only, not operons or 23S counts.
  conf: not stated · class: not stated · holds: rrnDB v5.0 onward (About page) · src: schmidtlaboratoryRrnDBReleaseFiles2025 (FT) · trail: MB-02 §D1.1, §answers · from: MB-02:B-0028, MB-02:B-0029, MB-02:A-008
- **copy-number.22** 16S gene count and operon count diverge where rRNA genes are unlinked: unlinked 16S and 23S genes are common in Deinococcus-Thermus, Chloroflexi and Planctomycetes, and up to 41% of rRNA genes in soil long-read metagenomes were unlinked, against none in human gut.
  conf: single (note: "SINGLE SOURCE for the soil figure") · class: not stated · holds: soil and human-gut long-read metagenomes; the soil figure from one source · src: brewerUnlinkedRRNAGenes2020 (AB) · trail: MB-02 §D1.2, §answers, §Adversarial · from: MB-02:B-0076, MB-02:B-0077, MB-02:B-0078, MB-02:B-0079, MB-02:A-007, MB-02:A-019, MB-02:A-131, MB-02:C-093
- **copy-number.23** Copies within a genome are not always identical: heterogeneity was found in 952 of 2,013 genomes, 87.5% of it below 1% divergence, and the inflation of unique-sequence richness reached 123.7% for full-length genes but was smaller at 97% clustering.
  conf: not stated · class: not stated · holds: 2,013 genomes · src: sunIntragenomicHeterogeneity16S2013 (AB) · trail: MB-02 §D1.2 · from: MB-02:B-0080, MB-02:B-0081, MB-02:B-0082
- **copy-number.24** Up to 15 operons occur in bacteria, with copy numbers up to 7 common and about 40% of organisms carrying one or two operons; a single operon dominated in archaea, with a maximum of five.
  conf: not stated · class: not stated · holds: as stated · src: acinasDivergenceRedundancy16S2004 (AB) · trail: MB-02 §D1.2 · from: MB-02:B-0068, MB-02:B-0069, MB-02:B-0070
- **copy-number.25** Operon redundancy gives an upper bound of about threefold diversity overestimation.
  conf: not stated · class: not stated · holds: Acinas et al.'s estimate · src: acinasDivergenceRedundancy16S2004 (AB) · trail: MB-02 §D1.2 · from: MB-02:B-0083
- **copy-number.26** Copy number tracks ecological strategy: soil isolates that formed colonies quickly averaged 5.5 copies and slow responders 1.4; this rests on one abstract-only study.
  conf: single (critic: MB-01:C-091) · class: meas (marker) · holds: soil isolates; a measured association · src: klappenbachRRNAOperonCopy2000 (AB; meas; repl) · trail: MB-01 §3.2, §answers, §Adversarial, MB-02 §D1.2 · from: MB-01:I-0080, MB-01:A-145, MB-01:B-0204, MB-01:C-091, MB-02:B-0084, MB-02:B-0085, MB-02:B-0087
- **copy-number.27** Maximum growth (reproductive) rate doubles with a doubling of rrn copy number across 1,167 species.
  conf: single (marker) · class: meas (marker) · holds: 1,167 species; a measured association · src: rollerExploitingRRNAOperon2016 (AB; meas; single) · trail: MB-01 §3.2, MB-02 §D1.2 · from: MB-01:I-0081, MB-02:B-0086, MB-02:B-0087
- **copy-number.28** Copy numbers for uncultured lineages without genomes (for example many soil Acidobacteriota, Verrucomicrobiota, Chloroflexota and candidate phyla) are not measured, and genome databases over-represent cultured, clinically and industrially relevant taxa.
  conf: not stated · class: search (note: "are not measured") · holds: genome databases · src: loucaCorrecting16SRRNA2018 · trail: MB-02 §answers · search: not stated · from: MB-02:A-014, MB-02:A-132
- **copy-number.29** No source found measured 16S copy number directly in environmental populations of soil archaea beyond genomes of cultured or enriched Nitrososphaerota.
  conf: not stated · class: search (note: "No source found measured 16S copy number directly") · holds: soil archaea · src: none (a search result) · trail: MB-02 §answers · search: searched, not found (note: "No source found measured 16S copy number directly") · from: MB-02:A-015

### ploidy: genome copies, and 16S copies, per cell
needs: copy-number
- **ploidy.1** In cultures, genome copies per cell range from about one (Caulobacter, Wolinella, crenarchaea) through merodiploid and oligoploid states that depend on growth rate (E. coli, Bacillus, Synechococcus) to tens or hundreds (P. putida, haloarchaea, methanogens, Synechocystis), and depend on taxon, growth rate and growth phase; this general conclusion would survive any single removal.
  conf: not stated · class: meas (note: "All figures below are measured") · holds: cultures · src: pecoraroQuantificationPloidyProteobacteria2011 (FT), hildenbrandGenomeCopyNumbers2011 (AB), breuertRegulatedPolyploidyHalophilic2006 (AB), griesePloidyCyanobacteria2011 (AB), zerullaPloidyLevelSynechocystis2016 (AB), bottingerRegulatedPloidyBacillus2018 (AB) · trail: MB-02 §answers, §critic, §D1.3 · rating: "Strong for cultures" (critic: MB-02:C-014: moderate, not strong; apart from Pecoraro 2011 it rests largely on abstracts and one laboratory's qPCR method) · from: MB-02:A-020, MB-02:A-134, MB-02:A-039, MB-02:A-028, MB-02:C-008, MB-02:C-014, MB-02:C-068, MB-02:B-0090
- **ploidy.2** Most culture ploidy values come from one laboratory's real-time PCR protocol (Soppa group), in several studies cross-checked against Southern blots, flow cytometry or published E. coli values; measurements from other laboratories exist for Azotobacter, Desulfovibrio (9 to 17), Neisseria (3 to 4) and Buchnera (120), with polyploid Deinococcus, Borrelia and rhizobial bacteroids also mentioned, all listed in Pecoraro 2011.
  conf: not stated · class: not stated · holds: cultures · src: pecoraroQuantificationPloidyProteobacteria2011 (FT), bottingerRegulatedPloidyBacillus2018, breuertRegulatedPolyploidyHalophilic2006, hildenbrandGenomeCopyNumbers2011, griesePloidyCyanobacteria2011, zerullaPloidyLevelSynechocystis2016, bruckOneAdvantageBeing2023, zerullaPolyploidyHaloarchaeaAdvantages2014 · trail: MB-02 §D1.3, §answers, §critic, §Adversarial · contrary: one-sided (critic: MB-02:C-131) · from: MB-02:B-0088, MB-02:B-0089, MB-02:A-029, MB-02:A-136, MB-02:C-013, MB-02:C-075, MB-02:C-131
- **ploidy.3** E. coli has 6.8 origins and 1.7 termini per cell at 25 min doubling but 2.5 origins and 1.2 termini at 103 min; this is the only direct origin and terminus count for E. coli at two growth rates.
  conf: not stated · class: meas (note: "All figures below are measured") · holds: E. coli cultures · src: pecoraroQuantificationPloidyProteobacteria2011 (FT) · trail: MB-02 §D1.3, §answers · from: MB-02:B-0090, MB-02:B-0091, MB-02:B-0092, MB-02:A-022, MB-02:A-036, MB-02:B-0088
- **ploidy.4** E. coli stationary-phase batch cultures always contained some multi-chromosome cells, even after days.
  conf: not stated · class: meas (note: "All figures below are measured") · holds: E. coli batch cultures · src: akerlundAnalysisCellSize1995 (AB) · trail: MB-02 §D1.3, §answers · from: MB-02:B-0090, MB-02:B-0093, MB-02:A-024, MB-02:B-0088
- **ploidy.5** Caulobacter crescentus (doubling 93 min) carries about 2.1 genome-equivalents at a mid-chromosome locus, read as monoploid, and Wolinella succinogenes (doubling 96 min) about 0.9, monoploid.
  conf: not stated · class: meas (note: "All figures below are measured") · holds: cultures · src: pecoraroQuantificationPloidyProteobacteria2011 (FT) · trail: MB-02 §D1.3, §answers · from: MB-02:B-0090, MB-02:B-0094, MB-02:B-0095, MB-02:A-021, MB-02:B-0088
- **ploidy.6** Pseudomonas putida (doubling 46 min) carries about 20 origins and 14 termini per cell.
  conf: not stated · class: meas (note: "All figures below are measured") · holds: cultures; the only P. putida value · src: pecoraroQuantificationPloidyProteobacteria2011 (FT) · trail: MB-02 §D1.3, §answers · from: MB-02:B-0090, MB-02:B-0096, MB-02:A-023, MB-02:A-036, MB-02:B-0088
- **ploidy.7** B. subtilis and three soil Bacillus/Paenibacillus isolates are mero-oligoploid in exponential phase (B. subtilis 5.9 origins, 1.2 termini) and down-regulate origins in stationary phase.
  conf: not stated · class: meas (note: "All figures below are measured") · holds: cultures · src: bottingerRegulatedPloidyBacillus2018 (AB) · trail: MB-02 §D1.3, §answers · from: MB-02:B-0090, MB-02:B-0097, MB-02:A-022, MB-02:B-0088
- **ploidy.8** Synechococcus PCC 7942 and WH7803 carry 3 to 4 genome copies in culture.
  conf: not stated · class: meas (note: "All figures below are measured") · holds: cultures · src: griesePloidyCyanobacteria2011 (AB) · trail: MB-02 §D1.3, §answers · from: MB-02:B-0090, MB-02:B-0098, MB-02:A-023, MB-02:B-0088
- **ploidy.9** Synechocystis PCC 6803 carries 218 (exponential) to 58 (stationary) copies in one substrain and about 20 to 4 across six substrains, becoming monoploid only after prolonged phosphate starvation.
  conf: not stated · class: meas (note: "All figures below are measured") · holds: cultures · src: griesePloidyCyanobacteria2011 (AB), zerullaPloidyLevelSynechocystis2016 (AB) · trail: MB-02 §D1.3, §answers · from: MB-02:B-0090, MB-02:B-0099, MB-02:A-023, MB-02:B-0088
- **ploidy.10** Halobacterium salinarum carries 25 (exponential) and 15 (stationary) genome copies, and Haloferax volcanii 18 and 10.
  conf: not stated · class: meas (note: "All figures below are measured") · holds: cultures · src: breuertRegulatedPolyploidyHalophilic2006 (AB) · trail: MB-02 §D1.3, §answers · from: MB-02:B-0090, MB-02:B-0100, MB-02:A-023, MB-02:B-0088
- **ploidy.11** Methanococcus maripaludis carries up to 55 genome copies in exponential phase and about 30 in stationary phase.
  conf: not stated · class: meas (note: "All figures below are measured") · holds: cultures · src: hildenbrandGenomeCopyNumbers2011 (AB) · trail: MB-02 §D1.3, §answers · from: MB-02:B-0090, MB-02:B-0101, MB-02:A-023, MB-02:B-0088
- **ploidy.12** Methanosarcina acetivorans carries 17 genome copies in fast growth and 3 in slow growth.
  conf: not stated · class: meas (note: "All figures below are measured") · holds: cultures · src: hildenbrandGenomeCopyNumbers2011 (AB) · trail: MB-02 §D1.3, §answers · from: MB-02:B-0090, MB-02:B-0102, MB-02:A-023, MB-02:B-0088
- **ploidy.13** Six crenarchaeal species of four genera were all monoploid, whereas none of seven euryarchaeal species was monoploid.
  conf: not stated · class: meas (note: "All figures below are measured") · holds: compiled culture measurements · src: hildenbrandGenomeCopyNumbers2011 (AB) · trail: MB-02 §D1.3, §answers · from: MB-02:B-0090, MB-02:B-0103, MB-02:B-0107, MB-02:A-021, MB-02:C-076, MB-02:B-0088
- **ploidy.14** Zymomonas mobilis, Azotobacter vinelandii and H. salinarum stayed at about five copies in phosphate-starved stationary phase rather than becoming monoploid, whereas Synechocystis went to one copy.
  conf: not stated · class: meas (note: "All figures below are measured") · holds: phosphate-starved stationary cultures · src: bruckOneAdvantageBeing2023 (AB), zerullaPloidyLevelSynechocystis2016 (AB) · trail: MB-02 §D1.3, §answers · from: MB-02:B-0090, MB-02:B-0104, MB-02:A-023, MB-02:A-033, MB-02:B-0088
- **ploidy.15** Only three to four of 11 proteobacterial species with measured ploidy were monoploid, with no correlation to genome size, temperature or lifestyle.
  conf: not stated · class: not stated · holds: 11 proteobacterial species · src: pecoraroQuantificationPloidyProteobacteria2011 (FT) · trail: MB-02 §D1.3 · from: MB-02:B-0105, MB-02:B-0106
- **ploidy.16** Single-cell measurements in H. salinarum showed wide cell-to-cell variation in genome copy number, larger in exponential than in stationary phase; the review read only the abstract, which gives no per-cell shares, although the open full text reports single-cell CLSM and FACS distributions.
  conf: not stated · class: not stated · holds: H. salinarum cultures · src: breuertRegulatedPolyploidyHalophilic2006 (AB) · trail: MB-02 §D1.3, §Adversarial · limit: access (critic: MB-02:C-071) · from: MB-02:B-0108, MB-02:C-069, MB-02:C-070, MB-02:C-071, MB-02:B-0088
- **ploidy.17** Azotobacter vinelandii is reported to rise from about 4 genome copies in exponential phase to about 80 in stationary phase, and Methanosarcina acetivorans from 2.5 to 5; Pecoraro 2011 Table 5 gives A. vinelandii as 1 (up to 8) copies in slow growth and 40 in fast growth, attributed to another laboratory.
  conf: not stated · class: not stated · holds: the A. vinelandii stationary-phase figure is secondary, via the Bruck et al. 2023 full text read by the critic · src: bruckOneAdvantageBeing2023, pecoraroQuantificationPloidyProteobacteria2011 · trail: MB-02 §critic, §Adversarial · from: MB-02:C-011, MB-02:C-012, MB-02:C-064, MB-02:C-072, MB-02:C-073, MB-02:C-102
- **ploidy.18** Genome copy number does not change in one direction with growth phase: most Soppa-group species fall in stationary phase or starvation, but A. vinelandii rises.
  conf: not stated · class: not stated · holds: taxon-specific and sometimes opposite behaviours · src: bruckOneAdvantageBeing2023, pecoraroQuantificationPloidyProteobacteria2011 · trail: MB-02 §critic, §Adversarial · contrary: one-sided (critic: MB-02:C-128) · from: MB-02:C-009, MB-02:C-010, MB-02:C-011, MB-02:C-074, MB-02:C-128, MB-02:C-129, MB-02:C-136
- **ploidy.19** rRNA operons cluster near the replication origin in fast-growing bacteria, and replication-associated gene-dosage effects shape this placement.
  conf: not stated · class: not stated · holds: fast-growing bacteria · src: couturierReplicationassociatedGeneDosage2006 (AB) · trail: MB-02 §D1.3 · from: MB-02:B-0110
- **ploidy.20** That 16S copies per cell scale with origin number more than with genome number is the reviewer's inference from one abstract; no source in the review measures 16S copies per cell against origin number.
  conf: not stated · class: reading (critic: MB-02:C-015) · holds: fast growers · src: couturierReplicationassociatedGeneDosage2006 (AB) · trail: MB-02 §D1.3, §answers, §critic, §Adversarial · from: MB-02:B-0111, MB-02:A-025, MB-02:C-015, MB-02:C-088, MB-02:C-140
- **ploidy.21** For E. coli, rRNA genes per genome equivalent range from about 7.9 to 9.5 across growth rates.
  conf: not stated · class: not stated · holds: E. coli; Bremer and Dennis (1996), Table 3, as reported by BioNumbers · src: miloBioNumbersEntry1023602010 (SEC), bremerModulationChemicalComposition1996 · trail: MB-02 §D1.3, §answers · limit: access (note: "This figure is SECONDARY") · from: MB-02:B-0112, MB-02:B-0113, MB-02:A-025
- **ploidy.22** No source measured 16S copies per cell directly in environmental cells.
  conf: not stated · class: search (note: "No source I found measured 16S copies per cell directly in environmental cells") · holds: environmental cells · src: none (a search result) · trail: MB-02 §D1.3 · search: searched, not found (note: "No source I found measured 16S copies per cell directly in environmental cells") · from: MB-02:B-0114
- **ploidy.23** In environmental samples, evidence on genome copies per cell is indirect and sparse (DNA mass per soil cell, DNA-content populations in seawater, population-average replication indices in groundwater), mostly non-soil and single-study per setting.
  conf: single (note: "single-study per setting") · class: not stated · holds: soil, seawater, groundwater · src: christensenFlowCytometricMeasurements1995, buttonDeterminationDNAContent2001, brownMeasurementBacterialReplication2016 · trail: MB-02 §answers, §critic, §D1.3 · rating: "Weak for environmental samples" · from: MB-02:A-030, MB-02:A-137, MB-02:C-016, MB-02:B-0115
- **ploidy.24** Indigenous soil bacteria extracted from a clay loam contained 1.5 to 15 fg DNA per cell by flow cytometry, most below 4 fg, with an average around 2 fg; larger cells, and cells that grew in soil extract, had more DNA; this confirms earlier work by the same group, and it is the only soil measurement of DNA per cell.
  conf: not stated · class: not stated · holds: one clay loam; Bakken and Olsen 1989 is secondary · src: christensenFlowCytometricMeasurements1995 (AB), bakkenDNAcontentSoilBacteria1989 (SEC) · trail: MB-02 §D1.3, §answers · from: MB-02:B-0116, MB-02:B-0117, MB-02:B-0118, MB-02:A-026, MB-02:A-037
- **ploidy.25** DNA mass per cell cannot separate genome size from copy number, and the two DNA-content populations in seawater could reflect replicating monoploid cells or larger genomes.
  conf: not stated · class: not stated · holds: DNA per cell in soil; DNA-content populations in seawater · src: christensenFlowCytometricMeasurements1995, buttonDeterminationDNAContent2001 · trail: MB-02 §D1.3, §answers · from: MB-02:B-0119, MB-02:A-032
- **ploidy.26** In the reviewer's reading, about 2 fg of DNA is less than one copy of a 4 Mb genome, which suggests many soil cells hold one copy of a small genome; this is inference.
  conf: not stated · class: reading (note: "In the reviewer's reading") · holds: soil · src: none (the reviewer's reading) · trail: MB-02 §D1.3 · from: MB-02:B-0120
- **ploidy.27** A typical seawater sample had a mean of 2.5 fg DNA per cell, in two populations described as 1n and 2n clusters, with 10 to 30% of cells "dim" low-DNA cells.
  conf: not stated · class: not stated · holds: seawater · src: buttonDeterminationDNAContent2001 (FT, first 100,000 characters) · trail: MB-02 §D1.3, §answers · from: MB-02:B-0121, MB-02:A-026
- **ploidy.28** The authors of the seawater study treat increased copy number with growth rate in nature as "likely", an inference rather than a measurement.
  conf: not stated · class: not stated · holds: seawater · src: buttonDeterminationDNAContent2001 · trail: MB-02 §D1.3 · from: MB-02:B-0122, MB-02:B-0121
- **ploidy.29** In the equatorial Pacific, Prochlorococcus DNA replication ran in phase with the light cycle, in the afternoon, with division at night; the abstract gives no share of cells carrying two genomes.
  conf: not stated · class: not stated · holds: Prochlorococcus in the equatorial Pacific; abstract only · src: vaulotGrowthProchlorococcusPhotosynthetic1995 (AB) · trail: MB-02 §D1.3, §Adversarial · limit: access (critic: MB-02:C-080) · from: MB-02:B-0123, MB-02:A-026, MB-02:C-078, MB-02:C-079, MB-02:C-080
- **ploidy.30** In groundwater metagenomes, population-average replication indices (iRep) were mostly low: Candidate Phyla Radiation bacteria had a median iRep of 1.34, and only 16.1% of values exceeded 1.5; the authors interpret an iRep of 1.25 as about a quarter of cells replicating; this is the only environmental replication-index figure.
  conf: not stated · class: not stated · holds: groundwater metagenomes · src: brownMeasurementBacterialReplication2016 (FT, first 100,000 characters) · trail: MB-02 §D1.3, §answers · from: MB-02:B-0124, MB-02:B-0125, MB-02:B-0126, MB-02:A-026, MB-02:A-038
- **ploidy.31** Gut metagenome peak-to-trough ratios track growth rate in culture and in vivo.
  conf: not stated · class: not stated · holds: gut · src: koremGrowthDynamicsGut2015 (AB) · trail: MB-02 §D1.3 · from: MB-02:B-0127
- **ploidy.32** No published replication indices for soil metagenomes were found.
  conf: not stated · class: search (note: "I found no published replication indices for soil metagenomes") · holds: Europe PMC queries combining iRep, peak-to-trough, GRiD or CoPTR with soil; WebSearch on soil iRep, rewetting and permafrost · src: none (a search result) · trail: MB-02 §D1.3, §Provenance, §Search record · search: searched, not found (note: "I found no published replication indices for soil metagenomes") · from: MB-02:B-0128, MB-02:B-0009, MB-02:B-0297
- **ploidy.33** Not measured in the sources found: genome copies per cell for named soil bacterial or archaeal taxa in situ; the share of single-copy cells by taxon in soil, rhizosphere or dormant natural populations; any direct measurement of 16S copies per cell in environmental cells; ploidy of cultured soil Acidobacteriota, Verrucomicrobiota or Nitrososphaerota.
  conf: not stated · class: search (note: "no source found") · holds: soil, rhizosphere and dormant natural populations; for Prochlorococcus, in situ flow cytometric cell-cycle analyses measure by method the taxon-specific share of cells with replicated DNA, and the review read only the abstract · src: vaulotGrowthProchlorococcusPhotosynthetic1995 · trail: MB-02 §answers, §D1.3, §critic · search: searched, not found (note: "no source found") · from: MB-02:A-034, MB-02:A-138, MB-02:B-0129, MB-02:C-017, MB-02:C-018, MB-02:C-019
- **ploidy.34** A search for contrary evidence on culture ploidy values (P. putida copy number by flow cytometry) was run once and found none.
  conf: not stated · class: search (note: "Ploidy contrary evidence searched once") · holds: one WebSearch · src: none (a search result) · trail: MB-02 §Provenance · search: searched, not found (note: "Ploidy contrary evidence searched once") · from: MB-02:B-0011

### copy-number-correction: copy number against read abundance, prediction and correction
needs: copy-number, pcr
- **copy-number-correction.1** Copy number is a property of each taxon rather than a workflow step, but it acts through PCR.
  conf: not stated · class: not stated · holds: as stated · src: none (the reviewer's statement) · trail: MB-01 §2.5 · from: MB-01:B-0123, MB-01:A-066
- **copy-number-correction.2** With equimolar DNA from species pairs, PCR product ratios matched rrn genes per unit DNA for two pairs but deviated for a Bacillus pair.
  conf: not stated · class: meas (note: "measured") · holds: equimolar DNA from species pairs · src: farrellyEffectGenomeSize1995 (AB, measured) · trail: MB-02 §D1.4, §answers · from: MB-02:B-0130, MB-02:A-040
- **copy-number-correction.3** In the 7-taxon vaginal mock, copy number explained about 60% of estimated PCR bias (R2 about 0.60, p about 0.021) but only about 10% of total bias (R2 about 0.10).
  conf: single (note: "SINGLE SOURCE, and only 7 points") · class: deriv (note: "Partial (derived)") · holds: 7 taxa, verified in full text · src: mclarenConsistentCorrectableBias2019 · trail: MB-01 §2.5, §answers · from: MB-01:B-0124, MB-01:B-0125, MB-01:B-0126, MB-01:A-067, MB-01:B-0067
- **copy-number-correction.4** In a forest soil, correcting with copy number and genome size moved Acidobacteria from 50.1% of 16S sequences to an estimated 66.0% of genomes, Actinobacteria from 11.8% to 7.6% and Firmicutes from 3.2% to 1.1%; it is the only soil example of correction size.
  conf: mixed (inputs: MB-01 repl, MB-02 single) · class: deriv (marker) · holds: one forest soil; depends on the low-n Acidobacteria copy-number mean · src: vetrovskyVariability16SRRNA2013 (FT; deriv; repl) · trail: MB-01 §2.5, MB-02 §D1.4, §answers, §critic · from: MB-01:I-0035, MB-02:B-0152, MB-02:B-0153, MB-02:A-045, MB-02:A-059, MB-02:C-005
- **copy-number-correction.5** Phylogenetic copy-number prediction had a leave-one-out error of about one copy.
  conf: not stated · class: not stated · holds: Kembel et al.'s analysis · src: kembelIncorporating16SGene2012 (FT) · trail: MB-02 §D1.4, §answers · from: MB-02:B-0133, MB-02:A-042, MB-02:B-0132
- **copy-number-correction.6** In 100 simulated communities, phylogenetically corrected abundances correlated better with true organism abundance (r = 0.81) than raw gene abundances did (r = 0.70).
  conf: cont (marker) · class: model (marker) · holds: simulated communities · src: kembelIncorporating16SGene2012 (FT; model; cont) · trail: MB-01 §2.5, §answers, MB-02 §D1.4, §answers, §critic · from: MB-01:I-0036, MB-01:A-070, MB-02:B-0134, MB-02:A-043, MB-02:C-021
- **copy-number-correction.7** Copy-number correction moved ear samples to cluster with nostrils rather than feet, but left ocean clustering largely unchanged.
  conf: not stated · class: not stated · holds: human body sites and ocean · src: kembelIncorporating16SGene2012 (FT) · trail: MB-02 §D1.4, §answers · from: MB-02:B-0151, MB-02:A-045
- **copy-number-correction.8** Copy-number prediction is accurate only near sequenced relatives: copy-number autocorrelation fell below 0.5 at about 15% 16S divergence and reached zero at about 30%; the quantitative thresholds rest on one analysis, though the qualitative distance effect is replicated.
  conf: repl (marker) · class: deriv (marker) · holds: about 6,800 genomes · src: loucaCorrecting16SRRNA2018 (FT; deriv; repl) · trail: MB-01 §2.5, §answers, MB-02 §D1.4, §answers · from: MB-01:I-0037, MB-01:A-153, MB-02:B-0135, MB-02:B-0136, MB-02:A-041, MB-02:A-057, MB-02:A-140
- **copy-number-correction.9** The decline of prediction accuracy with distance to sequenced genomes is consistent across four independent analyses, and correction improves fit to simulated truth.
  conf: repl (note: "consistent across four independent analyses") · class: not stated · holds: four independent analyses of genome-based prediction · src: kembelIncorporating16SGene2012, loucaCorrecting16SRRNA2018, edgarUNBIASAttemptCorrect2017, gaoAccounting16SRRNA2023 · trail: MB-02 §answers, §critic · from: MB-02:A-048, MB-02:C-021, MB-02:C-020
- **copy-number-correction.10** About 49% of SILVA OTUs lie more than 15% from a sequenced genome, so copy-number predictions are unreliable for about half of them.
  conf: not stated · class: not stated · holds: SILVA OTUs · src: loucaCorrecting16SRRNA2018 · trail: MB-01 §3.2, MB-02 §D1.4, §answers · from: MB-01:B-0210, MB-02:B-0137, MB-02:A-041, MB-02:A-140
- **copy-number-correction.11** PICRUSt, CopyRighter and PAPRICA sometimes explained under 10% of variance against complete genomes and disagreed with each other (R2 < 0.5) for most of 635 communities, which included soils.
  conf: repl (marker) · class: deriv (marker) · holds: 635 environmental communities, including soils · src: loucaCorrecting16SRRNA2018 (FT; deriv; repl) · trail: MB-01 §2.5, §answers, §7. Bounds, MB-02 §D1.4, §answers · from: MB-01:I-0037, MB-01:A-069, MB-01:B-0358, MB-02:B-0138, MB-02:B-0139, MB-02:A-041
- **copy-number-correction.12** Louca et al. recommend against default copy-number correction unless OTUs are close to sequenced genomes.
  conf: not stated · class: not stated · holds: their analysis · src: loucaCorrecting16SRRNA2018 (FT) · trail: MB-02 §D1.4 · from: MB-02:B-0140
- **copy-number-correction.13** Copy-number prediction precision was about 0.96 at small distances to sequenced genomes, with R2 high, and its uncertainty rose with distance.
  conf: not stated · class: not stated · holds: Gao and Wu's analysis · src: gaoAccounting16SRRNA2023 (FT) · trail: MB-02 §D1.4, §answers · from: MB-02:B-0141, MB-02:A-042
- **copy-number-correction.14** A preprint by the tool's author reports essentially "no meaningful correlation" between 16S read frequencies and species frequencies in mocks.
  conf: single (marker) · class: meas (marker) · holds: mocks; preprint abstract · src: edgarUNBIASAttemptCorrect2017 (AB; PREPRINT; meas; single) · trail: MB-01 §2.14, §answers, MB-02 §D1.4, §answers · from: MB-01:B-0192, MB-01:I-0076, MB-01:A-106, MB-02:B-0142, MB-02:A-044
- **copy-number-correction.15** Correction for copy number and primer mismatch reached r of about 0.6 only in ideal cases, when references were exact, falling to about 0.4 at 97% and about 0.2 at 95% identity.
  conf: single (marker) · class: meas (marker) · holds: mocks; preprint abstract · src: edgarUNBIASAttemptCorrect2017 (AB; PREPRINT; meas; single) · trail: MB-01 §2.14, §7. Bounds, MB-02 §D1.4, §answers · from: MB-01:I-0076, MB-01:B-0359, MB-02:B-0143, MB-02:A-044, MB-02:A-141
- **copy-number-correction.16** Copy numbers can be estimated from draft assemblies by read depth, with a median deviation of 14% against qPCR.
  conf: not stated · class: not stated · holds: draft genome assemblies · src: perisin16StimatorStatisticalEstimation2016 (AB) · trail: MB-02 §D1.4 · from: MB-02:B-0144
- **copy-number-correction.17** Copy-number correction improved agreement with mock communities and metagenomes, changed qPCR totals and diversity estimates, and reclassified twin gut samples from two enterotypes to three.
  conf: not stated · class: not stated · holds: mocks, metagenomes and twin gut samples · src: anglyCopyRighterRapidTool2014 (AB) · trail: MB-02 §D1.4, §answers · from: MB-02:B-0145, MB-02:B-0146, MB-02:A-043, MB-02:A-045
- **copy-number-correction.18** On 10 V4 mock communities (one of eleven excluded; nine genomic DNA mixes and two cloned-gene mixes), uncorrected data fit known composition 7.1% (SE 3.6%) better than copy-number-corrected data; all were DNA-based or cloned-gene mocks.
  conf: repl (marker) · class: meas (marker) · holds: DNA-based and cloned-gene mocks · src: starke16SRRNAGene2020 (FT; meas; repl) · trail: MB-01 §2.5, §answers, MB-02 §D1.4, §answers, §critic · from: MB-01:I-0038, MB-01:A-068, MB-01:B-0068, MB-01:B-0357, MB-02:B-0147, MB-02:A-044, MB-02:A-141, MB-02:C-022, MB-02:C-065
- **copy-number-correction.19** In the reviewer's note, DNA-based mocks already fix genome copies and size, so they test correction against a DNA truth, not a cell truth; part of the conflict over correction reflects what "truth" is (cell-based against DNA-based mocks, simulated against real communities, and closeness to references).
  conf: not stated · class: reading (note: "Reviewer's note") · holds: mock-based tests of correction · src: none (the reviewer's reading) · trail: MB-02 §D1.4, §answers · from: MB-02:B-0148, MB-02:A-051
- **copy-number-correction.20** Copy-number correction changed the most abundant OTU in about 20% of Human Microbiome Project and 31% of Earth Microbiome Project communities, but against predicted, not measured, truth; these are the only figures on how often correction changes the dominant taxon in real communities.
  conf: not stated · class: not stated · holds: HMP and EMP communities · src: gaoAccounting16SRRNA2023 (FT) · trail: MB-02 §D1.4, §answers, §critic · from: MB-02:B-0149, MB-02:A-045, MB-02:A-058, MB-02:A-142, MB-02:C-023
- **copy-number-correction.21** In simulations, copy-number correction raised the chance of identifying the true most abundant OTU from 13% to 65%.
  conf: not stated · class: not stated · holds: simulations · src: gaoAccounting16SRRNA2023 · trail: MB-02 §answers · from: MB-02:A-043
- **copy-number-correction.22** In simulations, correction reduced sample shifts in ordinations but left PERMANOVA variance explained essentially unchanged (5.27 to 19.65% true against 5.27 to 19.82% uncorrected), so correction changes dominant taxa but rarely changes beta-diversity test results.
  conf: not stated · class: not stated · holds: simulations · src: gaoAccounting16SRRNA2023 (FT) · trail: MB-02 §D1.4, §answers, §critic · from: MB-02:B-0150, MB-02:A-052, MB-02:A-142, MB-02:C-024
- **copy-number-correction.23** Whether to correct for copy number is contested: studies recommending routine correction conflict directly with studies recommending against default correction or finding it unhelpful in mocks (in MB-01's terms, Kembel 2012 against Louca 2018, Starke 2021 and McLaren 2019); evidence on whether correction improves real data is mostly from simulations, mocks of few species or non-soil communities, with no soil benchmark.
  conf: cont (note: "Direct conflict between studies recommending routine correction") · class: not stated · holds: simulations, mocks and non-soil communities · src: kembelIncorporating16SGene2012, anglyCopyRighterRapidTool2014, gaoAccounting16SRRNA2023, loucaCorrecting16SRRNA2018, edgarUNBIASAttemptCorrect2017, starke16SRRNAGene2020, mclarenConsistentCorrectableBias2019 · trail: MB-02 §answers, MB-01 §answers, §6. Where, §2.5 · rating: "Moderate" · from: MB-02:A-047, MB-02:A-049, MB-02:A-050, MB-02:A-143, MB-01:A-119, MB-01:B-0334, MB-02:C-132, MB-02:C-133, MB-02:C-134
- **copy-number-correction.24** Intragenomic variants split genomes into several ASVs: 0.58 variants per copy for full-length 16S and 0.25 for V4.
  conf: cont (marker) · class: deriv (marker) · holds: genomes, full-length and V4 · src: schlossAmpliconSequenceVariants2021 (FT; deriv; cont) · trail: MB-01 §2.5, §answers · from: MB-01:I-0039, MB-01:A-071, MB-01:B-0068
- **copy-number-correction.25** Full-length PacBio sequencing recovered intragenomic variants in their expected integral ratios.
  conf: single (marker) · class: meas (marker) · holds: the developer's own test · src: callahanHighthroughputAmpliconSequencing2019 (FT; meas; single; developer) · trail: MB-01 §2.5 · from: MB-01:I-0040
- **copy-number-correction.26** A review asserts that rDNA copy number can change within species in response to environment; the prokaryote evidence for this was not quantified in what was read.
  conf: not stated · class: assert (note: "asserted") · holds: a review · src: lavrinienkoDoesIntraspecificVariation2021 (AB, asserted) · trail: MB-02 §D1.4, §answers · from: MB-02:B-0154, MB-02:B-0155, MB-02:A-055
- **copy-number-correction.27** No soil mock community or soil cell-count benchmark of copy-number correction was found.
  conf: not stated · class: search (note: "No soil mock community or soil cell-count benchmark of copy-number correction was found") · holds: soil · src: none (a search result) · trail: MB-02 §answers, §critic · search: searched, not found (note: "No soil mock community or soil cell-count benchmark of copy-number correction was found") · from: MB-02:A-053, MB-02:C-026
- **copy-number-correction.28** No study was found that combines copy-number correction with per-cell genome copy measurements in a real community; the polyploidy literature asserts that ploidy also biases community analyses.
  conf: not stated · class: search (note: "No study found that combines copy-number correction with per-cell genome copy measurements") · holds: real communities; the polyploidy assertion is from a source not obtained (Soppa 2017) · src: soppaPolyploidyCommunityStructure2017 · trail: MB-02 §answers · search: searched, not found (note: "No study found that combines copy-number correction with per-cell genome copy measurements") · from: MB-02:A-054

### community-copy-number: copy number by environment
needs: copy-number-correction
- **community-copy-number.1** Every environment-level 16S copy number found is predicted from reference genomes, not measured.
  conf: not stated · class: deriv (marker) · holds: environment-level copy numbers · src: thompsonCommunalCatalogueReveals2017 (FT; deriv; single) · trail: MB-01 §3.2, §answers, §8. Answers · from: MB-01:B-0205, MB-01:A-146, MB-01:A-152, MB-01:A-303, MB-01:I-0082
- **community-copy-number.2** Soil had the lowest abundance-weighted copy-number distribution in the Earth Microbiome Project (predicted, not measured).
  conf: single (marker) · class: deriv (marker) · holds: EMP soils; predicted from reference genomes · src: thompsonCommunalCatalogueReveals2017 (FT; deriv; single) · trail: MB-01 §3.2, §answers · from: MB-01:I-0082, MB-01:A-147
- **community-copy-number.3** Predicted average community copy number declines through succession in soil and sediment.
  conf: single (marker) · class: deriv (marker) · holds: soil and sediment succession; predicted · src: nemergutDecreasesAverageBacterial2015 (FT; deriv; single) · trail: MB-01 §3.2, §answers · from: MB-01:I-0083, MB-01:A-148
- **community-copy-number.4** Animal-associated samples have a predicted community copy number of about 3.4, with gut and saliva highest.
  conf: single (critic: MB-01:C-024) · class: not stated · holds: EMP animal-associated samples; predictions from one source · src: thompsonCommunalCatalogueReveals2017 · trail: MB-01 §3.2, §answers, §critic · from: MB-01:B-0206, MB-01:B-0209, MB-01:A-151, MB-01:C-024
- **community-copy-number.5** No separate copy-number value for water was found; the EMP gives about 2.2 for free-living (soil, water, sediment) and plant-associated samples pooled together.
  conf: single (critic: MB-01:C-024) · class: not stated · holds: EMP, free-living and plant-associated samples pooled · src: thompsonCommunalCatalogueReveals2017 · trail: MB-01 §3.2, §answers, §critic, §Adversarial · from: MB-01:B-0207, MB-01:B-0208, MB-01:A-149, MB-01:A-150, MB-01:C-024, MB-01:C-136
- **community-copy-number.6** Environment-level copy number rests entirely on one source, its values are predictions, and they conflict with the finding that such predictions are unreliable for taxa more than about 15% divergent from sequenced genomes.
  conf: single (note: "single source") · class: not stated · holds: EMP predictions · src: thompsonCommunalCatalogueReveals2017, loucaCorrecting16SRRNA2018 · trail: MB-01 §answers, §3.2 · rating: "Weak for environment-level copy number" · from: MB-01:A-169, MB-01:A-177, MB-01:A-183, MB-01:B-0210
- **community-copy-number.7** Measured (not predicted) community-average copy number in soil, water or host samples was not found; community-average copy number from shotgun metagenomes (16S reads normalised to single-copy marker genes) was not searched, so the not-found rests on prediction-only sources.
  conf: not stated · class: search (critic: MB-01:C-112) · holds: soil, water and host samples · src: none (a search result) · trail: MB-01 §answers, §critic, §Adversarial, §Search record, §Provenance · search: not searched (critic: MB-01:C-112) · from: MB-01:A-178, MB-01:B-0017, MB-01:B-0380, MB-01:C-029, MB-01:C-112


### library-sequencing: library preparation, indexing and sequencing error
needs: pcr
- **library-sequencing.1** Across 73 MiSeq datasets, library preparation method and primer choice were the most significant sources of bias, with distinct, motif-linked error patterns; this rests on one study.
  conf: single (marker) · class: meas (marker) · holds: 73 MiSeq datasets · src: schirmerInsightBiasesSequencing2015 (FT; meas; single) · trail: MB-01 §2.6, §answers, §Adversarial · from: MB-01:I-0041, MB-01:A-076, MB-01:A-077, MB-01:B-0071, MB-01:C-088
- **library-sequencing.2** Library design also affected error and chimera rates across four platforms.
  conf: not stated · class: not stated · holds: four platforms · src: damoreComprehensiveBenchmarkingStudy2016 · trail: MB-01 §2.6 · from: MB-01:B-0127
- **library-sequencing.3** Dual-index MiSeq error depended on read overlap.
  conf: repl (marker) · class: meas (marker) · holds: dual-index MiSeq · src: kozichDevelopmentDualindexSequencing2013 (FT; meas; repl) · trail: MB-01 §2.7 · from: MB-01:I-0042
- **library-sequencing.4** Raw V4 MiSeq error rose with cluster density from 0.25% to 1.08%; a delta-Q of 6 cut it to 0.05 to 0.06%, and preclustering to 0.01%.
  conf: not stated · class: not stated · holds: V4 on MiSeq · src: kozichDevelopmentDualindexSequencing2013 · trail: MB-01 §2.7, §answers · from: MB-01:B-0131, MB-01:B-0132, MB-01:A-078, MB-01:B-0071
- **library-sequencing.5** Partially overlapping regions stayed worse: after preclustering, V3-V4 error was 0.10 to 0.21% and V4-V5 0.36 to 0.64%, per the bioinformatics angle.
  conf: not stated · class: not stated · holds: V3-V4 and V4-V5 after preclustering, per the bioinformatics angle · src: kozichDevelopmentDualindexSequencing2013 · trail: MB-01 §2.7 · from: MB-01:B-0133, MB-01:B-0134
- **library-sequencing.6** The lab angle reports V3-V4 and V4-V5 error of 0.24 to 0.37% and 0.58 to 0.87%, read through a fetch-tool summary and probably at an earlier stage of curation.
  conf: not stated · class: not stated · holds: V3-V4 and V4-V5, per the lab angle · src: kozichDevelopmentDualindexSequencing2013 · trail: MB-01 §2.7 · from: MB-01:B-0135
- **library-sequencing.7** PacBio CCS with DADA2 recovered all expected full-length variants in two mocks with no residual errors, by the developers' own account.
  conf: not stated · class: not stated · holds: two mocks; a developer claim · src: callahanHighthroughputAmpliconSequencing2019 (developer claim) · trail: MB-01 §2.7 · from: MB-01:B-0136
- **library-sequencing.8** The DADA2 maintainer states that NovaSeq's binned quality scores break loess smoothing in error learning; at the time of the issue the method had not been tested on NovaSeq data.
  conf: not stated · class: assert (note: "DOCUMENTATION; assert") · holds: DADA2 GitHub issue #791 · src: benjjnebConsequencesUsingDada2 (DOCUMENTATION; assert) · trail: MB-01 §2.7 · from: MB-01:B-0137, MB-01:B-0138

### index-misassignment: demultiplexing and index misassignment
needs: library-sequencing
- **index-misassignment.1** On Illumina GAIIx with non-16S libraries, 0.51 to 0.76% of index pairs were wrong, and 0.06 to 0.43% after index-quality filtering.
  conf: repl (marker) · class: meas (marker) · holds: GAIIx, non-16S libraries, indirect · src: kircherDoubleIndexingOvercomes2012 (FT; meas; repl; INDIRECT) · trail: MB-01 §2.8 · from: MB-01:I-0043
- **index-misassignment.2** On patterned flow cells (HiSeq X, 3000/4000, NovaSeq) with non-16S libraries, 0.2 to 6% of reads were misassigned in every run, about 10-fold less on MiSeq, and unique dual indexes cut 0.89% to 0.13%.
  conf: repl (marker) · class: meas (marker) · holds: non-16S libraries, indirect · src: costelloCharacterizationRemediationSample2018 (FT; meas; repl; INDIRECT) · trail: MB-01 §2.8, §answers · from: MB-01:I-0044, MB-01:A-082
- **index-misassignment.3** Illumina documentation gives 0.1 to 2% index misassignment on patterned flow cells.
  conf: not stated · class: not stated · holds: a maker's claim · src: illuminaIndexHoppingWeb (DOCUMENTATION; maker's claim) · trail: MB-01 §2.8 · from: MB-01:B-0139, MB-01:B-0140
- **index-misassignment.4** On HiSeq 2500 with non-16S amplicons, cross-talk was 0.24%, and 0.03% after index-quality filtering (88% of reads kept).
  conf: single (marker) · class: meas (marker) · holds: HiSeq 2500, non-16S amplicons, indirect · src: wrightQualityFilteringIllumina2016 (FT; meas; single; INDIRECT) · trail: MB-01 §2.8, §answers · from: MB-01:I-0045, MB-01:A-083
- **index-misassignment.5** In 16S data from GAIIx and 11 MiSeq runs, about 2% of reads were misassigned.
  conf: single (marker) · class: meas (marker) · holds: 16S; one preprint abstract · src: edgarUNCROSSFilteringHighfrequency2016 (AB; PREPRINT; meas; single) · trail: MB-01 §2.8, §answers · from: MB-01:I-0046, MB-01:A-084
- **index-misassignment.6** On 16S plates, barcode leakage was negligible.
  conf: single (marker) · class: meas (marker) · holds: 16S plates · src: minichQuantifyingUnderstandingWelltowell2019 (FT; meas; single) · trail: MB-01 §2.8, §answers · from: MB-01:I-0047, MB-01:A-085
- **index-misassignment.7** In eukaryotic 18S data, up to 28.2% of unique sequences were undetectable mistags.
  conf: not stated · class: meas (marker) · holds: eukaryotic 18S, indirect · src: eslingAccurateMultiplexingFiltering2015 (FT; meas; INDIRECT) · trail: MB-01 §2.8 · from: MB-01:I-0048
- **index-misassignment.8** With mammal and arthropod markers, 2.1 to 2.6% of sequences came from tag jumps.
  conf: not stated · class: meas (marker) · holds: mammal and arthropod markers, indirect · src: schnellTagJumpsIlluminated2015 (AB; meas; INDIRECT) · trail: MB-01 §2.8, §answers · from: MB-01:I-0049, MB-01:A-086
- **index-misassignment.9** Index misassignment rates are fractions of reads assigned to the wrong sample; they mainly create false presences of taxa, concentrated where abundant taxa from other samples leak in, and also affect relative abundance.
  conf: not stated · class: not stated · holds: as stated · src: none (the reviewer's synthesis) · trail: MB-01 §2.8, §answers · from: MB-01:B-0141, MB-01:B-0142, MB-01:A-081, MB-01:A-082, MB-01:B-0072
- **index-misassignment.10** Index misassignment rates vary with platform, library type and run.
  conf: not stated · class: not stated · holds: as stated · src: none (the reviewer's synthesis) · trail: MB-01 §2.8, §answers · from: MB-01:B-0143, MB-01:A-087, MB-01:B-0072
- **index-misassignment.11** The 16S-specific evidence on index misassignment is thin: one preprint abstract and one plate study; no 16S-specific measurement of index hopping on patterned flow cells (NovaSeq, NextSeq 2000) was found.
  conf: not stated · class: search (note: "No 16S-specific measurement of index hopping on patterned flow cells (NovaSeq) was found") · holds: the bioinformatics angle's search · src: edgarUNCROSSFilteringHighfrequency2016, minichQuantifyingUnderstandingWelltowell2019 · trail: MB-01 §2.8, §answers, §Search record, §Adversarial · search: searched, not found (note: "No 16S-specific measurement of index hopping on patterned flow cells (NovaSeq) was found") · from: MB-01:B-0144, MB-01:A-122, MB-01:B-0381, MB-01:C-110

### quality-filtering: quality filtering and read merging
needs: library-sequencing
- **quality-filtering.1** On mocks from GAIIx, HiSeq and MiSeq runs, minimum read length, quality threshold and a minimum OTU abundance filter strongly affected alpha diversity and composition; ambiguous bases and bad run length did not.
  conf: repl (marker) · class: meas (marker) · holds: mocks from GAIIx, HiSeq and MiSeq runs · src: bokulichQualityfilteringVastlyImproves2013 (FT; meas; repl) · trail: MB-01 §2.9 · from: MB-01:B-0145, MB-01:I-0050
- **quality-filtering.2** Almost every filtering setting needed an abundance filter of 0.0001 to 0.01% to reach expected taxon counts, and 0.005% is recommended.
  conf: not stated · class: not stated · holds: mocks · src: bokulichQualityfilteringVastlyImproves2013 · trail: MB-01 §2.9 · from: MB-01:B-0146, MB-01:B-0145
- **quality-filtering.3** After quality filtering, weighted UniFrac conclusions were robust and unweighted metrics were sensitive.
  conf: not stated · class: not stated · holds: mocks · src: bokulichQualityfilteringVastlyImproves2013 · trail: MB-01 §2.9 · from: MB-01:B-0147, MB-01:B-0145
- **quality-filtering.4** Stringent UPARSE-style filtering could significantly underestimate abundance and diversity, and newer clusterers produced up to 60% fewer spurious OTUs than UCLUST.
  conf: cont (marker) · class: meas (marker) · holds: Kopylova et al.'s benchmarks · src: kopylovaOpensourceSequenceClustering2016 (FT; meas; cont) · trail: MB-01 §2.9, §7. Bounds · from: MB-01:I-0051, MB-01:B-0362
- **quality-filtering.5** Error correction plus overlapping cut substitution errors by 93% on average.
  conf: not stated · class: not stated · holds: one study · src: schirmerInsightBiasesSequencing2015 · trail: MB-01 §2.9 · from: MB-01:B-0148
- **quality-filtering.6** The USEARCH author reports that most paired-read assemblers compute incorrect posterior quality scores.
  conf: not stated · class: not stated · holds: a developer claim · src: edgarErrorFilteringPair2015 (AB; developer claim) · trail: MB-01 §2.9 · from: MB-01:B-0149

### denoising-clustering: denoising, clustering, OTUs and ASVs
needs: quality-filtering
- **denoising-clustering.1** In an independent benchmark, relative abundances of expected taxa within each mock were similar across DADA2, UNOISE3, Deblur and open-reference OTUs, yet on the Zymo mock all pipelines "markedly differed" from expected composition.
  conf: repl (marker) · class: meas (marker) · holds: mocks, one independent benchmark · src: nearingDenoisingDenoisersIndependent2018 (FT; meas; repl) · trail: MB-01 §2.10, §answers, §Adversarial · from: MB-01:I-0052, MB-01:B-0154, MB-01:A-091, MB-01:A-092, MB-01:B-0074, MB-01:C-087
- **denoising-clustering.2** Counts of units differed widely between pipelines: open-reference clustering gave 453 OTUs on the HMP mock and 8,891 on the Extreme mock; on one soil, DADA2 gave 16,609 ASVs, UNOISE3 11,613, Deblur 8,270 and open-reference 21,297 OTUs; no pipeline recovered every expected sequence.
  conf: not stated · class: not stated · holds: mocks and one soil · src: nearingDenoisingDenoisersIndependent2018 · trail: MB-01 §2.10 · from: MB-01:B-0150, MB-01:B-0151, MB-01:B-0152, MB-01:B-0153
- **denoising-clustering.3** Bacteroides varied from 20.6% to 24.6% across pipelines.
  conf: not stated · class: not stated · holds: one study · src: marizzoniComparisonBioinformaticsPipelines2020 · trail: MB-01 §answers · from: MB-01:A-093, MB-01:B-0075
- **denoising-clustering.4** mothur and QIIME1 returned 10 to 200 times the expected number of sequences, and Faith's PD was overestimated 1.3 to 2.7-fold by QIIME2, 2 to 18-fold by QIIME1 and 3.5 to 29-fold by mothur; pipeline choice biased interpretations.
  conf: repl (marker) · class: meas (marker) · holds: Straub et al.'s benchmark; the authors also built nf-core/ampliseq · src: straubInterpretationsEnvironmentalMicrobial2020 (FT; meas; repl; authors also built nf-core/ampliseq) · trail: MB-01 §2.10, §answers, §Adversarial · from: MB-01:I-0053, MB-01:A-094, MB-01:B-0075, MB-01:C-087
- **denoising-clustering.5** DADA2 had the best sensitivity and UNOISE3 the best balance.
  conf: repl (marker) · class: meas (marker) · holds: mock runs · src: prodanComparingBioinformaticPipelines2020 (FT; meas; repl) · trail: MB-01 §2.10 · from: MB-01:I-0054
- **denoising-clustering.6** QIIME-uclust produced on average 134 one-off and 412 other spurious OTUs.
  conf: not stated · class: not stated · holds: mock runs · src: prodanComparingBioinformaticPipelines2020 · trail: MB-01 §2.10 · from: MB-01:B-0155, MB-01:B-0156
- **denoising-clustering.7** The DADA2 developers report 93 output sequences on a 57-strain mock, against 249 for mothur and 378 for QIIME.
  conf: not stated · class: meas (marker) · holds: one 57-strain mock; a developer claim · src: callahanDADA2HighresolutionSample2016 (FT; meas; developer claim) · trail: MB-01 §2.10 · from: MB-01:I-0055
- **denoising-clustering.8** After OTU clustering and singleton removal, tables were about 50% (mock communities) to 80% (gnotobiotic mice) spurious taxa; the authors propose a 0.25% relative-abundance cutoff.
  conf: single (marker) · class: meas (marker) · holds: mock communities and gnotobiotic mice · src: reitmeierHandlingSpuriousSequences2021 (FT; meas; single) · trail: MB-01 §2.10, §critic, §Adversarial, §answers · from: MB-01:I-0056, MB-01:A-095, MB-01:B-0075, MB-01:C-058, MB-01:C-072
- **denoising-clustering.9** QIIME closed- and open-reference OTUs inflated richness to 1,607 to 5,824 OTUs where about 20 were expected.
  conf: single (note: "SINGLE SOURCE") · class: not stated · holds: mocks · src: edgarAccuracyMicrobialCommunity2017 · trail: MB-01 §2.10 · from: MB-01:B-0157, MB-01:B-0158
- **denoising-clustering.10** In leaf litter, bacterial OTU richness was about half of ESV richness (slope 0.46), but alpha and beta metrics correlated at r > 0.90 and inferences matched.
  conf: cont (marker) · class: meas (marker) · holds: leaf litter · src: glassmanBroadscaleEcologicalPatterns2018 (FT; meas; cont) · trail: MB-01 §2.10 · from: MB-01:I-0058
- **denoising-clustering.11** In 227 freshwater sediment, seston and mussel-gut samples the direction was reversed: ASV richness was about half of OTU richness, and Mollicutes dominated mussel gut by ASVs but were absent from OTU tables; the authors attribute the reversal partly to higher richness in sediment.
  conf: cont (marker) · class: meas (marker) · holds: 227 freshwater sediment, seston and mussel-gut samples · src: chiarelloRankingBiasesChoice2022 (FT; meas; cont) · trail: MB-01 §2.10 · from: MB-01:B-0160, MB-01:I-0059, MB-01:B-0161
- **denoising-clustering.12** The direction of the OTU versus ASV richness difference conflicts between studies (Glassman and Martiny 2018 against Chiarello 2022).
  conf: cont (note: "OTU versus ASV richness (contested)") · class: not stated · holds: the two studies named · src: glassmanBroadscaleEcologicalPatterns2018, chiarelloRankingBiasesChoice2022 · trail: MB-01 §2.10, §answers, §6. Where · from: MB-01:B-0159, MB-01:A-096, MB-01:A-120, MB-01:B-0335
- **denoising-clustering.13** In soil and plant samples, OTUs versus ASVs changed which families were called differentially abundant, mostly families under 0.1% abundance.
  conf: single (marker) · class: meas (marker) · holds: soil and plant samples · src: joosDaringDifferentialMetabarcoding2020 (FT; meas; single) · trail: MB-01 §2.10 · from: MB-01:I-0060
- **denoising-clustering.14** The identity threshold that best matched species was about 99% for full-length 16S and about 100% for V4.
  conf: single (marker) · class: deriv (marker) · holds: an abstract · src: edgarUpdating97Identity2018 (AB; deriv; single) · trail: MB-01 §2.10 · from: MB-01:I-0061
- **denoising-clustering.15** As biomass fell in a dilution series, contaminants made up a growing share of inferred communities under every sequence-inference method; the authors state no inference method alone separates contaminants from true sequences.
  conf: single (marker) · class: meas (marker) · holds: a dilution series · src: carusoPerformanceMicrobiomeSequence2019 (FT; meas; single) · trail: MB-01 §2.10 · from: MB-01:B-0162, MB-01:I-0062
- **denoising-clustering.16** According to its documentation, DADA2's independent per-sample processing needs at least two error-free reads to detect an ASV, and pooling finds more ASVs per sample.
  conf: not stated · class: not stated · holds: DADA2 documentation · src: callahanDADA2DocumentationPseudopooling (DOCUMENTATION) · trail: MB-01 §2.10 · from: MB-01:B-0163, MB-01:B-0164

### chimeras: chimera formation and detection
needs: pcr, denoising-clustering
- **chimeras.1** Chimeras formed reproducibly across independent amplifications of a known mixture; that chimera formation is reproducible rests on this one study, on Sanger and 454 data.
  conf: single (critic: MB-01:C-090) · class: meas (marker) · holds: a known mixture, Sanger and 454 · src: haasChimeric16SRRNA2011 (FT; meas; repl; Sanger and 454) · trail: MB-01 §2.11, §answers, §Adversarial · from: MB-01:I-0063, MB-01:A-075, MB-01:B-0070, MB-01:C-090
- **chimeras.2** Less-abundant species showed chimera rates above 70% on 454, and chimera count correlated with organism abundance (R2 = 0.97) in a staggered mock.
  conf: not stated · class: not stated · holds: 454; a staggered mock · src: haasChimeric16SRRNA2011 · trail: MB-01 §2.11, §answers · from: MB-01:B-0165, MB-01:B-0166, MB-01:A-074, MB-01:B-0070
- **chimeras.3** ChimeraSlayer detected over 87% of simulated chimeras when parents diverged by 4% or more, with a 1.6% false-positive rate, and sensitivity fell for every method as parents became more similar.
  conf: not stated · class: not stated · holds: simulated chimeras · src: haasChimeric16SRRNA2011 · trail: MB-01 §2.11 · from: MB-01:B-0167, MB-01:B-0168
- **chimeras.4** At 30 cycles, chimeras made up 0.9% (Accuprime) to 18.2% (Platinum) of reads, depending on polymerase.
  conf: not stated · class: not stated · holds: 30 cycles; verified in full text · src: szeImpactDNAPolymerase2019 · trail: MB-01 §2.11, §answers · from: MB-01:B-0169, MB-01:A-073, MB-01:B-0069
- **chimeras.5** UCHIME sensitivity was 50 to 87% at 25 or more cycles.
  conf: not stated · class: not stated · holds: 25 or more cycles · src: szeImpactDNAPolymerase2019 · trail: MB-01 §2.11 · from: MB-01:B-0169
- **chimeras.6** UCHIME2's author states that error-free chimera prediction is "impossible in principle".
  conf: not stated · class: not stated · holds: a developer claim in a preprint abstract · src: edgarUCHIME2ImprovedChimera2016 (AB; PREPRINT; developer claim) · trail: MB-01 §2.11 · from: MB-01:B-0170
- **chimeras.7** Chimeras inflate richness and create false novel taxa.
  conf: not stated · class: not stated · holds: as stated in the answers · src: szeImpactDNAPolymerase2019, haasChimeric16SRRNA2011 · trail: MB-01 §answers · from: MB-01:A-072, MB-01:B-0069

### taxonomy: taxonomic assignment and reference databases
needs: denoising-clustering
- **taxonomy.1** Cross-validated by identity to the reference, all tested classifiers were at most 50% accurate on V4; genus accuracy was about 100% at 100% identity and about 50% at 97%, derived from reference sets by one author who also develops competing classifiers.
  conf: single (marker) · class: meas (marker) · holds: V4, reference sets; accuracy depends on distance to reference · src: edgarAccuracyTaxonomyPrediction2018 (FT; meas; single) · trail: MB-01 §2.12, §answers, §Adversarial · from: MB-01:B-0171, MB-01:I-0064, MB-01:A-097, MB-01:B-0076, MB-01:C-089
- **taxonomy.2** Edgar 2018b's author argues that mocks overstate classification accuracy because all their members are named type strains.
  conf: not stated · class: not stated · holds: an argument · src: edgarAccuracyTaxonomyPrediction2018 · trail: MB-01 §2.12, §answers · from: MB-01:B-0172, MB-01:A-099
- **taxonomy.3** On mocks, the q2-feature-classifier methods reached median genus F above 0.8.
  conf: not stated · class: meas (marker) · holds: mocks; a developer claim · src: bokulichOptimizingTaxonomicClassification2018 (FT; meas; developer claim) · trail: MB-01 §2.12, §answers · from: MB-01:I-0065, MB-01:A-099
- **taxonomy.4** Habitat-weighted priors cut species-level classification error from 25% to 14%.
  conf: not stated · class: meas (marker) · holds: a developer claim · src: kaehlerSpeciesAbundanceInformation2019 (FT; meas; developer claim) · trail: MB-01 §2.12 · from: MB-01:I-0066
- **taxonomy.5** IDTAXA over-classified less when the true taxa were absent from the training set.
  conf: not stated · class: meas (marker) · holds: a developer claim; the reference is listed under Murali and cited by the bioinformatics angle · src: muraliIDTAXANovelApproach2018 (FT; meas; developer claim) · trail: MB-01 §2.12 · from: MB-01:I-0067, MB-01:B-0173
- **taxonomy.6** Estimated annotation error in reference databases is about 10% for RDP and about 17% for SILVA v128 and Greengenes 13.5, judged from conflicting labels on identical sequences; this rests on one author who also develops competing classifiers.
  conf: single (marker) · class: deriv (marker) · holds: RDP, SILVA v128, Greengenes 13.5 · src: edgarTaxonomyAnnotationGuide2018 (FT; deriv; single) · trail: MB-01 §2.12, §answers, §Adversarial · from: MB-01:I-0068, MB-01:A-098, MB-01:C-089
- **taxonomy.7** On simulated gut, ocean and soil communities, genus recall was 67 to 80%, and assignments varied by up to 40% between 16S subregions within a pipeline.
  conf: single (marker) · class: model (marker) · holds: simulated gut, ocean and soil communities · src: almeidaBenchmarkingTaxonomicAssignments2018 (FT; model; single) · trail: MB-01 §2.12 · from: MB-01:I-0069
- **taxonomy.8** On V4 mocks, 56 to 88% of predicted genus names were false positives with closed-reference OTUs.
  conf: single (marker) · class: meas (marker) · holds: V4 mocks · src: edgarAccuracyMicrobialCommunity2017 (FT; meas; single) · trail: MB-01 §2.10 · from: MB-01:I-0057, MB-01:B-0076

### contamination: reagent and cross-sample contamination
needs: extraction
- **contamination.1** In a Salmonella bongori dilution series run at three institutes, contaminants dominated by about 10^3 cells, more so at 40 than at 20 cycles, and contaminant profiles differed by kit and laboratory.
  conf: repl (marker) · class: meas (marker) · holds: a dilution series at three institutes · src: salterReagentLaboratoryContamination2014 (FT; meas; repl) · trail: MB-01 §2.13, §answers · from: MB-01:B-0174, MB-01:I-0070, MB-01:A-100, MB-01:B-0078
- **contamination.2** In an 8-member mock diluted 3-fold eight times, contaminant reads rose from 0.1% to 80.1% and ASVs from 18 to 381.
  conf: single (marker) · class: meas (marker) · holds: one diluted 8-member mock · src: karstensControllingContaminantsLowbiomass2019 (FT; meas; single) · trail: MB-01 §2.13, §answers · from: MB-01:I-0071, MB-01:B-0175, MB-01:A-101, MB-01:B-0077
- **contamination.3** Removing every sequence present in the negative control wrongly removed more than 20% of expected sequences, since three of the eight mock ASVs appeared in the control.
  conf: single (marker) · class: meas (marker) · holds: one diluted 8-member mock · src: karstensControllingContaminantsLowbiomass2019 (FT; meas; single) · trail: MB-01 §2.13, §7. Bounds · from: MB-01:I-0071, MB-01:B-0176, MB-01:B-0360
- **contamination.4** decontam's frequency method removed 70 to 90% of contaminants and no expected sequences.
  conf: single (marker) · class: meas (marker) · holds: one diluted 8-member mock · src: karstensControllingContaminantsLowbiomass2019 (FT; meas; single) · trail: MB-01 §2.13 · from: MB-01:I-0071, MB-01:B-0177
- **contamination.5** SourceTracker removed over 98% of contaminants when sources were well defined but failed on over 97% when they were not.
  conf: single (marker) · class: meas (marker) · holds: one diluted 8-member mock · src: karstensControllingContaminantsLowbiomass2019 (FT; meas; single) · trail: MB-01 §2.13, §7. Bounds · from: MB-01:I-0071, MB-01:B-0178, MB-01:B-0361
- **contamination.6** Well-to-well contamination arose mainly at extraction, less at library preparation, mostly into neighbouring wells (rarely up to 10 wells away), and was greatest in low-biomass samples.
  conf: single (marker) · class: meas (marker) · holds: neighbouring wells · src: minichQuantifyingUnderstandingWelltowell2019 (FT; meas; single) · trail: MB-01 §2.13, §answers · from: MB-01:I-0072, MB-01:A-102
- **contamination.7** Contamination varies inversely with biomass and is specific to the kit and laboratory.
  conf: not stated · class: not stated · holds: as stated · src: salterReagentLaboratoryContamination2014, karstensControllingContaminantsLowbiomass2019, minichQuantifyingUnderstandingWelltowell2019 · trail: MB-01 §answers · from: MB-01:A-103, MB-01:B-0077, MB-01:B-0078
- **contamination.8** decontam's makers describe a frequency mode that assumes contaminant DNA is roughly constant across samples.
  conf: not stated · class: not stated · holds: a developer claim · src: davisSimpleStatisticalIdentification2018 (FT; developer claim) · trail: MB-01 §2.13 · from: MB-01:B-0179
- **contamination.9** A review proposes the RIDE checklist for low-biomass studies.
  conf: not stated · class: assert (marker) · holds: a review · src: eisenhoferContaminationLowMicrobial2019 (AB; assert) · trail: MB-01 §2.13 · from: MB-01:I-0074
- **contamination.10** The most abundant spurious taxon in mocks had a median relative abundance of 0.12%.
  conf: not stated · class: not stated · holds: mocks · src: reitmeierHandlingSpuriousSequences2021 · trail: MB-01 §2.13 · from: MB-01:B-0180

### dominant-steps: which steps dominate the departure
needs: extraction, pcr, denoising-clustering, contamination, chimeras
- **dominant-steps.1** The ordering in which DNA extraction is the largest source of relative-abundance error, followed by PCR and then sequencing, rests on one 7-taxon vaginal dataset (Brooks 2015, reanalysed by McLaren 2019), with Albertsen 2015 (sludge, bead beating only) as partial support; it is contested by Fouhy 2016 (two extraction methods gave very similar data) and qualified by MBQC (specimen type mattered more than extraction), and is a single-dataset result, not a field-wide ordering.
  conf: single (critic: MB-01:C-017) · class: not stated · holds: one 7-taxon vaginal dataset, 454 · src: mclarenConsistentCorrectableBias2019, brooksTruthMetagenomicsQuantifying2015, albertsenBackBasicsInfluence2015, fouhy16SRRNAGene2016, sinhaAssessmentVariationMicrobial2017 · trail: MB-01 §critic, §Adversarial, §1. Overview, §answers, §8. Answers · rating: "Strong" (critic: MB-01:C-083: firmer than the access and source base allow) · from: MB-01:C-015, MB-01:C-016, MB-01:C-017, MB-01:C-061, MB-01:C-083, MB-01:C-084, MB-01:A-111, MB-01:A-131, MB-01:A-297, MB-01:B-0035, MB-01:B-0036
- **dominant-steps.2** In the reanalysed 7-taxon cell mixtures, PCR followed extraction (maximum pairwise bias 5.2, mean 2.3), then sequencing and classification (maximum 1.6, mean 1.2).
  conf: single (critic: MB-01:C-017) · class: deriv/model (marker) · holds: 80 cell mixtures of 7 vaginal taxa, V1-V3, 454 · src: mclarenConsistentCorrectableBias2019 (FT, re-opened; deriv/model; single dataset) · trail: MB-01 §2.2 · from: MB-01:I-0007, MB-01:B-0090, MB-01:C-017, MB-01:B-0089
- **dominant-steps.3** In the same cell mixtures, total bias was a maximum of 29.3-fold and a mean of 5.6-fold, smaller than extraction bias alone, which implies partial cancellation between steps.
  conf: single (critic: MB-01:C-017) · class: deriv/model (marker) · holds: 80 cell mixtures of 7 vaginal taxa · src: mclarenConsistentCorrectableBias2019 (FT, re-opened; deriv/model; single dataset) · trail: MB-01 §2.2, §critic · from: MB-01:I-0007, MB-01:B-0091, MB-01:B-0092, MB-01:C-017, MB-01:C-054
- **dominant-steps.4** Across 15 laboratories, variability depended most on specimen type, then DNA extraction, then handling laboratory, then bioinformatics.
  conf: single (marker) · class: meas (marker) · holds: the MBQC interlaboratory study, whole workflow · src: sinhaAssessmentVariationMicrobial2017 (FT; meas; single) · trail: MB-01 §2.2, §answers · from: MB-01:I-0011, MB-01:A-104, MB-01:A-105
- **dominant-steps.5** For the number of taxa detected, inflation by spurious sequences (sequencing error, chimeras, cross-sample leakage, reagent contamination) and by the choice of clustering or denoising is replicated across independent mocks and dilution series: 10 to 200-fold excess units, and contaminants rising from 0.1% to 80.1% of reads in a diluted mock; these can change counts of taxa by one to two orders of magnitude.
  conf: repl (critic: MB-01:C-014) · class: not stated · holds: mocks and dilution series · src: straubInterpretationsEnvironmentalMicrobial2020, karstensControllingContaminantsLowbiomass2019 · trail: MB-01 §critic, §1. Overview, §8. Answers · rating: "Strong" (critic: MB-01:C-022: moderate for the inflation of taxon counts) · from: MB-01:C-014, MB-01:C-022, MB-01:A-298, MB-01:A-111, MB-01:B-0037, MB-01:B-0038
- **dominant-steps.6** Per-step magnitudes of departure mostly come from one or two small mocks (7 to 20 taxa), often on 454 or Ion Torrent.
  conf: not stated · class: not stated · holds: mocks of 7 to 20 taxa · src: none (the reviewer's and critic's account of the evidence base) · trail: MB-01 §answers, §critic · rating: "Magnitudes per step are moderate" (critic: MB-01:C-022: weak for per-step relative-abundance magnitudes) · from: MB-01:A-113, MB-01:C-018, MB-01:C-022, MB-01:A-301

### bias-consistency: whether the departure is consistent across samples
needs: extraction, primers, pcr, copy-number-correction
- **bias-consistency.1** Modelling each step as multiplying taxon abundances by a taxon-specific efficiency, McLaren et al. found that the error in taxon ratios was "consistent across samples", while the error in proportions "varied dramatically in both magnitude and direction", in the one dataset modelled for this question (the vaginal cell mixtures; extraction bias was consistent on the ratio scale within a protocol); bias behaves as a multiplicative factor per taxon that calibration controls can correct.
  conf: single (note: "the one dataset modelled for this question") · class: model (note: "modelled") · holds: 7 taxa mixed as cells and reanalysed · src: mclarenConsistentCorrectableBias2019 (FT, re-opened) · trail: MB-01 §2.14, §2.2, §answers, §Adversarial, MB-02 §D1.4 · contrary: one-sided (critic: MB-01:C-130) · from: MB-01:B-0182, MB-01:B-0183, MB-01:A-107, MB-01:A-108, MB-01:A-299, MB-01:B-0101, MB-01:A-048, MB-01:B-0056, MB-01:C-128, MB-01:C-129, MB-01:C-130, MB-02:B-0131, MB-01:I-0002
- **bias-consistency.2** Six parameters explained almost all systematic error in the cell mixtures, and calibration cut mean Bray-Curtis error from 0.35 to 0.08 (92.6% lower mean squared error); this result comes from the Brooks et al. 2015 16S cell mixtures (2 calibration samples, 69 calibrated samples), not from a shotgun dataset.
  conf: not stated · class: not stated · holds: the Brooks 16S cell mixtures · src: mclarenConsistentCorrectableBias2019 · trail: MB-01 §2.14, §critic, §Adversarial · contrary: one-sided (critic: MB-01:C-131) · from: MB-01:B-0184, MB-01:C-021, MB-01:C-055, MB-01:C-066, MB-01:C-067, MB-01:C-069, MB-01:C-131
- **bias-consistency.3** A 10-species shotgun spike-in across faecal backgrounds also gave a consistent profile on the ratio scale, with protocol H showing up to 2,751-fold maximum pairwise bias; this is known only via McLaren 2019, and its calibration is reported only qualitatively ("removed most of the systematic error").
  conf: not stated · class: not stated · holds: shotgun, faecal backgrounds; secondary and indirect · src: costeaTowardsStandardsHuman2017 (SEC; INDIRECT, shotgun) · trail: MB-01 §2.2, §answers, §Adversarial · limit: access (note: "known only via McLaren 2019") · from: MB-01:B-0102, MB-01:A-049, MB-01:C-068, MB-01:R-0613
- **bias-consistency.4** McLaren et al. list where the ratio model may fail: PCR saturation, taxa aggregated with differing efficiencies, matrix differences between controls and samples, and taxa absent from the controls.
  conf: not stated · class: not stated · holds: their model · src: mclarenConsistentCorrectableBias2019 · trail: MB-01 §2.14 · from: MB-01:B-0185, MB-01:B-0182
- **bias-consistency.5** On the same data, Brooks et al. found significant mixture-blending terms and concluded that one taxon's observed proportion depends on which others are present; the two readings conflict, and McLaren's attributes the apparent dependence to working on the proportion scale.
  conf: cont (note: "The two readings conflict") · class: not stated · holds: the Brooks 2015 cell mixtures · src: brooksTruthMetagenomicsQuantifying2015, mclarenConsistentCorrectableBias2019 · trail: MB-01 §2.14, §answers, §1. Overview, §6. Where · from: MB-01:B-0186, MB-01:B-0187, MB-01:A-109, MB-01:A-115, MB-01:B-0039, MB-01:B-0040, MB-01:B-0329
- **bias-consistency.6** Bias varies between sample types or samples: a field-versus-mock SAR11 bias for the 515F-Y/806R pair (abstract only), inconsistent cycle effects in four stool samples, extraction yield of 40 to 84%, and a 66.7-fold spike-in range (abstract).
  conf: mixed (marker) · class: meas (marker) · holds: field and mock samples, stool samples, spike-ins · src: paradaEveryBaseMatters2016 (AB; meas; repl), szeImpactDNAPolymerase2019 (FT; meas; single), zembAbsoluteQuantitationMicrobes2020, zhouReproducibilityQuantitationAmplicon2011 · trail: MB-01 §critic, §1. Overview, §2.14, §answers, §8. Answers · from: MB-01:C-020, MB-01:I-0003, MB-01:A-110, MB-01:A-300, MB-01:B-0188
- **bias-consistency.7** A 0.1% genomic spike was recovered at 0.06% to 5.34% of reads across soils, a 66.7-fold range; the 66.7-fold figure is in the abstract, and the 0.06 to 5.34% range, which needs the body, could not be confirmed.
  conf: single (marker) · class: meas (marker) · holds: soils, 454 · src: zhouReproducibilityQuantitationAmplicon2011 (AB; meas; single; critic: MB-01:C-075 was "FT per statistics angle; meas; single") · trail: MB-01 §2.14, §5.5, §answers, §Adversarial · limit: access (critic: MB-01:C-076) · from: MB-01:I-0075, MB-01:B-0319, MB-01:A-268, MB-01:C-075, MB-01:C-076
- **bias-consistency.8** Whether mock-derived bias applies to field samples is disputed: Parada 2016 against the calibration claims of McLaren 2019 and Silverman 2021.
  conf: not stated · class: not stated · holds: field samples against calibration claims · src: paradaEveryBaseMatters2016, mclarenConsistentCorrectableBias2019, silvermanMeasuringMitigatingPCR2021 · trail: MB-01 §answers, §6. Where · from: MB-01:A-121, MB-01:B-0337
- **bias-consistency.9** Evidence on whether bias is consistent across samples rests mainly on one reanalysis of 7 taxa, with contrary or limiting field evidence; ratio-scale consistency is shown in one 16S cell-mixture dataset and one shotgun spike-in known only secondarily, and the ratio-consistency claim would weaken substantially without McLaren 2019 and its source data.
  conf: not stated · class: not stated · holds: one 16S cell-mixture dataset and one secondary shotgun spike-in · src: mclarenConsistentCorrectableBias2019, brooksTruthMetagenomicsQuantifying2015, costeaTowardsStandardsHuman2017 · trail: MB-01 §answers, §critic · rating: "weak to moderate" (critic: MB-01:C-022: weak for consistency across samples) · from: MB-01:A-114, MB-01:A-131, MB-01:C-019, MB-01:C-022
- **bias-consistency.10** A review states that PCR-based estimates can deviate by "several orders of magnitude" if extraction, PCR, copy number and analysis errors are ignored.
  conf: not stated · class: assert (marker) · holds: a review · src: bonkPCRbasedQuantificationTaxaspecific2018 (AB; assert) · trail: MB-01 §2.14 · from: MB-01:I-0077
- **bias-consistency.11** No mock study in a soil matrix with known composition was found, and the consistency of extraction bias across real soil or water matrices has not been measured in the sources found; soil evidence comes from spike-ins, dilutions and relic DNA.
  conf: not stated · class: search (note: "No mock study in soil matrix with known composition was found") · holds: soil and water matrices · src: none (a search result) · trail: MB-01 §answers · search: searched, not found (note: "No mock study in soil matrix with known composition was found") · from: MB-01:A-124, MB-01:A-125, MB-01:A-126
- **bias-consistency.12** No archaeal-rich mock was found beyond Pinto and Raskin 2012 and D'Amore 2016.
  conf: not stated · class: search (note: "No archaeal-rich mock was found") · holds: archaeal-rich mocks · src: pintoPCRBiasesDistort2012, damoreComprehensiveBenchmarkingStudy2016 · trail: MB-01 §answers · search: searched, not found (note: "No archaeal-rich mock was found") · from: MB-01:A-123
- **bias-consistency.13** In eukaryotic eDNA, modelling the PCR process, calibrated with mocks, has been used to estimate starting proportions.
  conf: not stated · class: model (marker) · holds: eukaryotic eDNA, indirect; an abstract · src: sheltonTowardQuantitativeMetabarcoding2023 (AB; model; INDIRECT) · trail: MB-01 §5.1 · from: MB-01:I-0111


### reads-per-sample: reads per sample and variation between samples
needs: library-sequencing
- **reads-per-sample.1** The Earth Microbiome Project averaged 80,000 sequences per sample over 27,751 samples and rarefied to 5,000.
  conf: not stated · class: not stated · holds: the EMP survey · src: thompsonCommunalCatalogueReveals2017 · trail: MB-01 §3.3, §answers · from: MB-01:B-0211, MB-01:A-154, MB-01:A-155
- **reads-per-sample.2** In four environments of the EMP, mean prevalence of tag sequences rose with depth up to 50,000, so rarefying to 5,000 under-estimated prevalence.
  conf: not stated · class: not stated · holds: four environments of the EMP · src: thompsonCommunalCatalogueReveals2017 · trail: MB-01 §3.3 · from: MB-01:B-0212, MB-01:B-0211
- **reads-per-sample.3** In one 360-sample MiSeq run, reads averaged 9,913 pairs per sample, with 95% of samples above 2,454; these figures need the paper's body and could not be confirmed.
  conf: not stated · class: not stated · holds: one MiSeq run · src: kozichDevelopmentDualindexSequencing2013 · trail: MB-01 §3.3, §answers, §Adversarial · limit: access (critic: MB-01:C-076) · from: MB-01:B-0213, MB-01:B-0214, MB-01:A-156, MB-01:C-076
- **reads-per-sample.4** A dilution-series run ranged from 40,927 to 251,419 reads per sample.
  conf: not stated · class: not stated · holds: one dilution-series run · src: karstensControllingContaminantsLowbiomass2019 · trail: MB-01 §3.3, §answers · from: MB-01:B-0215, MB-01:A-157
- **reads-per-sample.5** Three mock runs gave 36,464 to 146,653 read pairs.
  conf: not stated · class: not stated · holds: three mock runs · src: prodanComparingBioinformaticPipelines2020 · trail: MB-01 §3.3 · from: MB-01:B-0216
- **reads-per-sample.6** Across 12 public V4 studies, reads per sample varied up to about 100-fold within a study, for example human 10,439 to 422,904 (median 32,452, n = 490), bioethanol 3,690 to 356,027, mice 1,804 to 30,311, soil 46,622 to 58,935 (n = 18) and marine 132,895 to 256,758 (n = 7); these are per-study, not per-run, ranges.
  conf: single (marker) · class: meas (marker) · holds: 12 public V4 studies; per study, not per run · src: schlossRarefactionCurrentlyBest2024 (FT, re-opened; meas; single) · trail: MB-01 §3.3, §answers, §critic · rating: "Moderate for reads per sample per study" · from: MB-01:I-0084, MB-01:B-0217, MB-01:A-158, MB-01:A-172, MB-01:A-184, MB-01:A-302, MB-01:C-023
- **reads-per-sample.7** Schloss attributes the spread of reads per sample to compounding random error when PCR products are pooled.
  conf: not stated · class: not stated · holds: 12 public V4 studies · src: schlossRarefactionCurrentlyBest2024 · trail: MB-01 §3.3 · from: MB-01:B-0218, MB-01:I-0084
- **reads-per-sample.8** Schloss cites studies reporting that sequencing depth correlates positively with biomass despite normalisation; the two primary studies (one on 101 fish species, one on an equivolumetric protocol) are known only secondarily and were not opened.
  conf: not stated · class: not stated · holds: known secondarily via Schloss 2024b · src: schlossRarefactionCurrentlyBest2024 (SEC) · trail: MB-01 §3.3, §Adversarial · limit: access (critic: MB-01:C-111) · from: MB-01:B-0219, MB-01:C-111
- **reads-per-sample.9** The Illumina guide states more than 20 million reads per MiSeq v3 run and more than 100,000 per sample at 96-plex, said to be "sufficient to fully survey the bacterial composition".
  conf: not stated · class: not stated · holds: a maker's claim · src: illumina16SMetagenomicSequencing (maker's claim) · trail: MB-01 §3.3, §answers · from: MB-01:B-0220, MB-01:A-159, MB-01:A-182
- **reads-per-sample.10** A core facility protocol gives about 20 million (v3) and about 16 million (v2) reads per run, with more than 100,000 reads per sample recommended.
  conf: not stated · class: not stated · holds: a protocol, a maker's statement · src: emoryAmplicon16SMetagenomics (PROTOCOL) · trail: MB-01 §3.3, §answers · from: MB-01:B-0221, MB-01:A-159, MB-01:A-182
- **reads-per-sample.11** Median Good's coverage ranged from 89.4% (seagrass) to 99.8% (human), and reaching 95% and 99% coverage required about 3 and 101 times the sequences needed for 90%.
  conf: not stated · class: deriv (note: "(Schloss 2024b) [deriv]") · holds: 12 public V4 studies · src: schlossRarefactionCurrentlyBest2024 (deriv) · trail: MB-01 §3.3 · from: MB-01:B-0222, MB-01:B-0223, MB-01:I-0084
- **reads-per-sample.12** No peer-reviewed coefficient of variation of reads per sample within a run after equimolar pooling was found; web search returned only forum posts.
  conf: not stated · class: search (note: "All three angles searched") · holds: all three search angles · src: none (a search result) · trail: MB-01 §3.3, §answers, §Search record, §Provenance, §critic · rating: "Absent for the within-run coefficient of variation" · search: searched, not found (note: "All three angles searched") · from: MB-01:B-0224, MB-01:B-0225, MB-01:A-160, MB-01:A-173, MB-01:A-178, MB-01:A-304, MB-01:B-0017, MB-01:B-0378, MB-01:C-029

### microbial-load: total microbial load
needs: none
- **microbial-load.1** Microbial load differed up to tenfold among healthy human individuals' faeces.
  conf: repl (marker) · class: meas (marker) · holds: human faeces · src: vandeputteQuantitativeMicrobiomeProfiling2017 (AB; meas; repl) · trail: MB-01 §3.5, §answers · from: MB-01:I-0089, MB-01:A-167, MB-01:C-023
- **microbial-load.2** Prokaryote load in Antarctic seawater differed 27-fold among stations.
  conf: single (marker) · class: meas (marker) · holds: Antarctic seawater · src: linTowardsQuantitativeMicrobiome2019 (FT; meas; single) · trail: MB-01 §3.5, §answers · from: MB-01:I-0090, MB-01:A-167
- **microbial-load.3** Microbial load in the mouse gut spanned more than six orders of magnitude across sites.
  conf: single (marker) · class: meas (marker) · holds: mouse gut sites · src: barlowQuantitativeSequencingFramework2020 (FT; meas; single) · trail: MB-01 §3.5, §answers · from: MB-01:I-0091, MB-01:A-167

### abundance-distribution: shape of taxon abundance distributions
needs: reads-per-sample
- **abundance-distribution.bg1** A species abundance distribution describes how many species in a community are common and how many rare; every community shows a hollow curve, with many rare species and just a few common species.
  kind: background · ref: mcgillSpeciesAbundanceDistributions2007 · check: DOI 10.1111/j.1461-0248.2007.01094.x resolves on Crossref; first sentence of the abstract
- **abundance-distribution.1** For 24 grassland soils, the best-fitting abundance distributions the review reports (exponential or inverse gamma) are in supplementary Table S3; the main text does not state which distributions won, and they were not verified.
  conf: single (marker) · class: model (marker) · holds: 24 grassland soils · src: zhouRandomSamplingProcess2013 (FT; model; single) · trail: MB-01 §3.4, §answers, §critic, §Adversarial · limit: access (critic: MB-01:C-079) · from: MB-01:I-0085, MB-01:A-161, MB-01:A-162, MB-01:A-186, MB-01:C-026, MB-01:C-077, MB-01:C-078, MB-01:C-079
- **abundance-distribution.2** In a Brazil soil, 26,079 reads and 2,880 observed species were fitted equally well by communities of 10^4, 10^5 and 10^6 species, so the tail of the distribution cannot be identified from sample data; these figures rest on a full text that was not openly retrievable and could not be confirmed.
  conf: repl (marker) · class: model (marker) · holds: one Brazil soil · src: haegemanRobustEstimationMicrobial2013 (FT; model; repl) · trail: MB-01 §3.4, §answers, §critic, §Adversarial · limit: access (critic: MB-01:C-028) · from: MB-01:I-0086, MB-01:A-163, MB-01:C-028, MB-01:C-076
- **abundance-distribution.3** After copy-number correction, rank-abundance distributions from ocean and human skin fit a lognormal better, in a single study that pools ocean and skin into one item and whose own simulations assumed a lognormal.
  conf: single (critic: MB-01:C-027) · class: not stated · holds: ocean and human skin, pooled · src: kembelIncorporating16SGene2012 · trail: MB-01 §3.4, §answers, §critic, §Adversarial · from: MB-01:B-0226, MB-01:A-164, MB-01:C-027, MB-01:C-134
- **abundance-distribution.4** Lognormal dynamics best explained microbial abundance distributions across more than 20,000 samples; the abstract gives no per-environment breakdown, so soil is not reported separately.
  conf: single (marker) · class: model (marker) · holds: cross-environment compilation including soils; abstract only · src: shoemakerMacroecologicalTheoryMicrobial2017 (AB; model; single) · trail: MB-01 §3.4, §answers, MB-02 §D3.1, §answers · from: MB-01:I-0087, MB-01:B-0227, MB-01:B-0228, MB-01:A-165, MB-02:B-0236, MB-02:B-0238, MB-02:A-087
- **abundance-distribution.5** A dominance scaling law held across about 35,000 sites.
  conf: not stated · class: not stated · holds: a cross-environment compilation; the abstract does not report soil separately · src: loceyScalingLawsPredict2016 (AB) · trail: MB-02 §D3.1 · from: MB-02:B-0237, MB-02:B-0238, MB-02:B-0236
- **abundance-distribution.6** Mean abundances across taxa were lognormal "for all the data sets considered"; per-biome results are in supplementary figures that were not read.
  conf: single (marker) · class: model (marker) · holds: all the data sets considered; partly re-opened · src: grilliMacroecologicalLawsDescribe2020 (FT, partly re-opened; model; single) · trail: MB-01 §3.4, §answers · from: MB-01:I-0088, MB-01:B-0229, MB-01:A-166
- **abundance-distribution.7** Soil abundance-distribution shape conflicts between exponential or inverse gamma fits and lognormal ones, but these use different fitting targets, so the conflict is only partial; one analysis argues the tail is not identifiable from sample data at all.
  conf: cont (note: "Conflicts") · class: not stated · holds: soil · src: zhouRandomSamplingProcess2013, shoemakerMacroecologicalTheoryMicrobial2017, grilliMacroecologicalLawsDescribe2020, haegemanRobustEstimationMicrobial2013 · trail: MB-01 §answers · from: MB-01:A-175, MB-01:A-176
- **abundance-distribution.8** Abundance-distribution shapes split by environment are weaker than presented, because the field-wide sources do not separate soil, water and host.
  conf: not stated · class: not stated · holds: soil, water and host samples · src: none (the reviewer's and critic's assessment) · trail: MB-01 §answers, §critic, §8. Answers · rating: "Weak for abundance-distribution shapes split by environment" · from: MB-01:A-174, MB-01:A-305, MB-01:C-025
- **abundance-distribution.9** Abundance-distribution shapes reported separately for water and for host-associated 16S data were not found, beyond the copy-correction fits for ocean and skin, although per-biome supplementary figures and an unread full text exist.
  conf: not stated · class: search (note: "no angle located such a breakdown") · holds: water and host-associated 16S data · src: grilliMacroecologicalLawsDescribe2020, shoemakerMacroecologicalTheoryMicrobial2017 · trail: MB-01 §3.4, §answers, §Search record, §Provenance, §critic, §Adversarial · search: searched, not found (note: "no angle located such a breakdown") · from: MB-01:B-0230, MB-01:A-178, MB-01:B-0017, MB-01:B-0385, MB-01:C-029, MB-01:C-114
- **abundance-distribution.10** In bulk-soil global amplicon datasets, a small minority of taxa carries a large share of reads and most taxa are rare; this qualitative shape is replicated across global amplicon datasets and older clone and reassociation studies.
  conf: repl (note: "replicated across global amplicon datasets") · class: not stated · holds: bulk soil, amplicon reads · src: delgadobaquerizoGlobalAtlasDominant2018, bickelChosenFewVariations2021 · trail: MB-02 §critic, §answers · rating: "Moderate for the qualitative shape" · from: MB-02:C-039, MB-02:A-081, MB-02:A-090, MB-02:B-0219
- **abundance-distribution.11** Across 237 soils, per-sample richness ranged from 774 to 2,869 phylotypes, and 511 of 25,224 phylotypes (2%), defined as dominant jointly by abundance (top 10% by share of reads) and ubiquity (present in more than half of the soils), accounted on average for 41% of 16S reads per sample, more than half in arid forests and only about 20% in tropical forests.
  conf: not stated · class: not stated · holds: 237 soils, bulk soil, amplicon reads; per-sample mean · src: delgadobaquerizoGlobalAtlasDominant2018 (FT) · trail: MB-02 §D3.1, §D2.3, §answers, §critic · from: MB-02:B-0220, MB-02:B-0183, MB-02:A-081, MB-02:C-041
- **abundance-distribution.12** Across 844 soils (318 sites, 90-bp V4 ASVs), 0.4% of ASVs were classed common on the globally pooled rank-abundance distribution and held about 58% of pooled relative abundance, while the 99.6% classed rare held 42%.
  conf: not stated · class: not stated · holds: 844 soils, pooled global relative abundance · src: bickelChosenFewVariations2021 (FT) · trail: MB-02 §D3.1, §answers, §critic · from: MB-02:B-0221, MB-02:A-082, MB-02:A-094, MB-02:C-042
- **abundance-distribution.13** The dominant-fraction shares of the two global soil datasets (2% holding about 41% of reads per sample, and 0.4% holding about 58% of pooled relative abundance) use different definitions and denominators and must not be combined.
  conf: not stated · class: not stated · holds: two global soil amplicon datasets · src: delgadobaquerizoGlobalAtlasDominant2018, bickelChosenFewVariations2021 · trail: MB-02 §D3.1, §answers, §critic · from: MB-02:B-0226, MB-02:A-094, MB-02:C-040, MB-02:C-041, MB-02:C-042
- **abundance-distribution.14** Drier soils had more even abundance distributions, and the ratio of rare to common richness declined with rainfall frequency (Pearson r = -0.41, n = 318).
  conf: not stated · class: not stated · holds: 318 sites · src: bickelChosenFewVariations2021 (FT) · trail: MB-02 §D3.1, §answers · from: MB-02:B-0222, MB-02:B-0223, MB-02:A-082
- **abundance-distribution.15** Across 146 soils, archaeal reads averaged 2% of 16S reads (0 to over 10%), and two Thaumarchaeota (then Crenarchaeota) phylotypes made up over 70% of archaeal sequences; this rests on one abstract-only study of 2010-era 454 data.
  conf: single (critic: MB-02:C-044) · class: not stated · holds: 146 soils, 454 · src: batesExaminingGlobalDistribution2011 (AB) · trail: MB-02 §D3.1, §answers, §critic, §Adversarial · from: MB-02:B-0224, MB-02:B-0225, MB-02:A-083, MB-02:A-099, MB-02:C-044, MB-02:C-091
- **abundance-distribution.16** By DNA reassociation kinetics, which measure whole-community DNA rather than reads or cells, a power law described the soil abundance distribution best, implying over a million distinct genomes in a pristine soil, and metal pollution cut diversity by over 99.9%; this is the main contrary result on the shape of the distribution.
  conf: not stated · class: not stated · holds: whole-community DNA; a pristine soil · src: gansComputationalImprovementsReveal2005 (AB) · trail: MB-02 §D3.1, §answers · from: MB-02:B-0233, MB-02:B-0234, MB-02:B-0235, MB-02:A-085, MB-02:A-098
- **abundance-distribution.17** Four Arizona soils were consistent with lognormal null models; small surveys reproduced richness but not composition, and documenting half the species would need 16,284 to 44,000 individuals.
  conf: not stated · class: not stated · holds: clone libraries and models, four Arizona soils · src: dunbarEmpiricalTheoreticalBacterial2002 (AB) · trail: MB-02 §D3.1, §answers · from: MB-02:B-0227, MB-02:B-0228, MB-02:B-0229, MB-02:B-0230, MB-02:A-086
- **abundance-distribution.18** Lognormal-based estimates gave 6,400 to 38,000 taxa per gram of soil.
  conf: not stated · class: model (note: "modelled") · holds: soil · src: curtisEstimatingProkaryoticDiversity2002 (AB) · trail: MB-02 §D3.1, §answers · from: MB-02:B-0231, MB-02:A-086
- **abundance-distribution.19** Soils may need hundreds of times current sampling to reach 90% of taxa, and diversity estimates depend on the distribution assumed.
  conf: not stated · class: not stated · holds: soil · src: quinceRationalExplorationMicrobial2008 (AB) · trail: MB-02 §D3.1, §answers · from: MB-02:B-0232, MB-02:A-086
- **abundance-distribution.20** The functional form of the soil abundance distribution is contested: a power law from reassociation kinetics against a lognormal from clone-library models and large amplicon compilations; it is method-dependent, and most of this evidence is abstract-only or modelled.
  conf: cont (critic: MB-02:C-045) · class: not stated · holds: soil · src: gansComputationalImprovementsReveal2005, curtisEstimatingProkaryoticDiversity2002, dunbarEmpiricalTheoreticalBacterial2002, shoemakerMacroecologicalTheoryMicrobial2017 · trail: MB-02 §answers, §critic · rating: "Weak for the functional form" · from: MB-02:A-091, MB-02:A-093, MB-02:A-149, MB-02:C-045
- **abundance-distribution.21** No soil taxon abundance distribution built from metagenome coverage was found; the search did not cover genome-resolved global soil metagenomes.
  conf: not stated · class: search (critic: MB-02:C-047) · holds: soil metagenomes · src: none (a search result) · trail: MB-02 §D3.1, §answers, §critic, §Adversarial · search: not searched (critic: MB-02:C-047) · from: MB-02:B-0239, MB-02:A-088, MB-02:A-150, MB-02:C-046, MB-02:C-047, MB-02:C-116
- **abundance-distribution.22** Iowa corn and prairie soil metagenomes totalled about 300 Gbp, yet 80% of reads could not be assembled for low coverage, and 48% and 31% of contigs had coverage below 10x.
  conf: not stated · class: not stated · holds: Iowa corn and prairie soils · src: howeTacklingSoilDiversity2014 (FT) · trail: MB-02 §D3.1, §answers · from: MB-02:B-0240, MB-02:B-0241, MB-02:A-088
- **abundance-distribution.23** Tropical soils are among the least-covered communities by Nonpareil estimates.
  conf: not stated · class: not stated · holds: qualitative · src: rodriguezrEstimatingCoverageMetagenomic2014 (FT) · trail: MB-02 §D3.1, §answers · from: MB-02:B-0242, MB-02:A-088
- **abundance-distribution.24** 85% of the amplicon-defined dominant soil phylotypes were also dominant in 123 shotgun soil metagenomes, the only global amplicon-metagenome cross-check.
  conf: not stated · class: not stated · holds: 123 shotgun soil metagenomes · src: delgadobaquerizoGlobalAtlasDominant2018 (FT) · trail: MB-02 §D3.1, §answers · from: MB-02:B-0243, MB-02:A-088, MB-02:A-097
- **abundance-distribution.25** No taxon abundance distribution from cell counts in soil was found; cell-based soil data found concern only total DNA per cell, and taxon-specific cell counts (CARD-FISH or FISH) were not searched beyond abundance-distribution queries, a narrow route.
  conf: not stated · class: search (note: "extended WebSearch on soil species abundance distributions from FISH, flow cytometry, spike-ins and absolute quantification") · holds: soil · src: none (a search result) · trail: MB-02 §D3.1, §answers, §Search record, §critic, §Adversarial · rating: "Absent for cell-count-based distributions in soil" · search: searched, not found (note: "extended WebSearch on soil species abundance distributions from FISH, flow cytometry, spike-ins and absolute quantification") · from: MB-02:B-0244, MB-02:A-089, MB-02:A-092, MB-02:A-150, MB-02:B-0298, MB-02:C-046, MB-02:C-117
- **abundance-distribution.26** Absolute-abundance work multiplies relative abundance by total counts (flow cytometry or qPCR), which converts gene copies but not cells per taxon.
  conf: not stated · class: not stated · holds: non-soil · src: propsAbsoluteQuantificationMicrobial2016 (AB) · trail: MB-02 §D3.1 · from: MB-02:B-0245
- **abundance-distribution.27** Not found as such: copy-number- or ploidy-corrected abundance distributions for soil, metagenome-based taxon abundance distributions reported as a distribution, and rhizosphere-specific abundance distributions.
  conf: not stated · class: search (note: "none found as such") · holds: soil and rhizosphere · src: none (a search result) · trail: MB-02 §answers · search: not stated · from: MB-02:A-095

### count-sampling: sampling from the amplified pool
needs: reads-per-sample, abundance-distribution
- **count-sampling.1** Technical replicates of the same soil DNA amplified with different barcodes shared 17.2 ± 2.3% of OTUs between two replicates and 8.2 ± 2.3% among three on 454; these figures are in the paper's abstract.
  conf: single (marker) · class: meas (marker) · holds: soil technical replicates, 454 · src: zhouReproducibilityQuantitationAmplicon2011 (AB; meas; single; critic: MB-01:C-075 was "FT; meas; single") · trail: MB-01 §4.1, §answers, §Adversarial, MB-02 §D3.3, §answers · from: MB-01:I-0092, MB-01:A-208, MB-01:C-075, MB-02:B-0265, MB-02:A-108
- **count-sampling.2** The paper's discussion gives 13.1% and 5.9% for the replicate overlaps, which differ from its abstract; these values need the body and could not be confirmed.
  conf: not stated · class: not stated · holds: the same soil replicates · src: zhouReproducibilityQuantitationAmplicon2011 · trail: MB-01 §4.1, §Adversarial · limit: access (critic: MB-01:C-076) · from: MB-01:B-0231, MB-01:C-076
- **count-sampling.3** A Poisson random-sampling model of long-tailed abundance distributions predicted the low OTU overlap among soil technical replicates, with no significant difference from the observed values; it modelled the same 24 Oklahoma grassland soils, sequenced on 454, that the replicate study reported, and the low replicate overlap was attributed to random sampling.
  conf: single (critic: MB-01:C-030) · class: model (note: "modelled") · holds: one dataset of 24 Oklahoma grassland soils, 454 · src: zhouRandomSamplingProcess2013 · trail: MB-01 §4.1, §answers, §critic, MB-02 §D3.3 · contrary: one-sided (critic: MB-01:C-123) · from: MB-01:B-0232, MB-01:A-188, MB-01:C-030, MB-01:C-031, MB-01:C-123, MB-02:B-0265
- **count-sampling.4** About 60,900 sequences per replicate were predicted to be needed for 90% OTU overlap.
  conf: single (marker) · class: model (marker) · holds: soil technical replicates · src: zhouRandomSamplingProcess2013 (FT; model; single) · trail: MB-01 §4.1, §answers · from: MB-01:I-0093, MB-01:A-210, MB-01:A-229
- **count-sampling.5** MiSeq replicates from the same laboratory cut against pure sampling: unweighted overlap plateaued at 39% near 30,000 reads (with singletons) and reached only 43.9% at 160,000 reads, far below the predicted 90% at about 60,900; the authors attribute rare-OTU variation to random sampling plus sequencing artefacts, report that "biases other than random sampling" affect unweighted metrics more, and found lower overlap when replicates were sequenced in separate runs.
  conf: not stated · class: not stated · holds: soil, MiSeq, the same laboratory as the 454 study · src: wenEvaluationReproducibilityAmplicon2017 · trail: MB-01 §critic, §Adversarial · from: MB-01:C-032, MB-01:C-033, MB-01:C-034, MB-01:C-035, MB-01:C-120, MB-01:C-121
- **count-sampling.6** That Poisson or multinomial sampling explains replicate disagreement in taxa detected rests on one 454 dataset of 24 Oklahoma soils (modelled twice) and one laboratory, whose MiSeq replicates do not fit the model; it is weak and contested that sampling alone explains replicate disagreement in taxa detected.
  conf: cont (critic: MB-01:C-036) · class: not stated · holds: soil, one dataset and one laboratory · src: zhouReproducibilityQuantitationAmplicon2011, zhouRandomSamplingProcess2013, wenEvaluationReproducibilityAmplicon2017 · trail: MB-01 §critic, §Adversarial, §answers · rating: "Moderate" (critic: MB-01:C-036: weak and contested that sampling alone explains replicate disagreement) · from: MB-01:C-030, MB-01:C-031, MB-01:C-032, MB-01:C-036, MB-01:C-063, MB-01:C-086, MB-01:C-135, MB-01:A-187, MB-01:A-214
- **count-sampling.7** For one caecal extract with four technical replicates, the abundance at which the CV of relative abundance reached 30% fell with the square root of read depth, as Poisson noise would predict.
  conf: single (marker) · class: meas (marker) · holds: one caecal extract, four technical replicates · src: barlowQuantitativeSequencingFramework2020 (FT; meas; single) · trail: MB-01 §4.1, §answers, §critic, §Adversarial · from: MB-01:I-0094, MB-01:A-189, MB-01:A-206, MB-01:C-037, MB-01:C-085
- **count-sampling.8** The assumption that technical replicates are Poisson comes from RNA-seq, where Illumina lane replicates fit a Poisson model with about 0.5% of genes deviating; McMurdie and Holmes adopt it for technical replicates, but it rests on RNA-seq, not on 16S technical replicates.
  conf: not stated · class: meas (marker) · holds: RNA-seq lane replicates, indirect · src: marioniRNAseqAssessmentTechnical2008 (FT; meas; INDIRECT), mcmurdieWasteNotWant2014 · trail: MB-01 §4.1, §answers · from: MB-01:I-0095, MB-01:B-0233, MB-01:A-191
- **count-sampling.9** Each taxon's abundance across communities followed a gamma distribution with variance proportional to the squared mean (Taylor's law with exponent 2); with finite read sampling this predicted each species' occupancy from its mean and variance with no further parameters and reproduced the abundance-occupancy relationship, so absences are attributed mostly to sampling; the text read does not name soil among the biomes.
  conf: single (marker) · class: model (marker) · holds: datasets across biomes; non-soil, nearest precedent · src: grilliMacroecologicalLawsDescribe2020 (FT, partly re-opened; model; single) · trail: MB-01 §3.4, §4.2, §answers, MB-02 §D3.3, §answers · from: MB-01:I-0088, MB-01:B-0236, MB-01:B-0237, MB-01:A-193, MB-02:B-0276, MB-02:B-0277, MB-02:B-0278, MB-02:A-112, MB-02:A-124
- **count-sampling.10** The conflict between sampling as the cause of replicate variation and technical variance beyond counting is partly one of setting and measure (OTU overlap against variance of relative abundance), a caution applied to the technical-variance side but not to the sampling side.
  conf: not stated · class: not stated · holds: OTU overlap against variance of relative abundance · src: zhouRandomSamplingProcess2013, silvermanDynamicLinearModels2018, grilliMacroecologicalLawsDescribe2020, dyrhovdenManagingContaminationDiverse2021 · trail: MB-01 §answers, §6. Where, §Adversarial · contrary: one-sided (critic: MB-01:C-123) · from: MB-01:A-218, MB-01:B-0338, MB-01:C-122, MB-01:C-123

### overdispersion: overdispersed count models
needs: count-sampling
- **overdispersion.1** Between biological samples, human oral plaque counts rejected the multinomial in favour of the Dirichlet-multinomial, with overdispersion theta of 0.047 and 0.054.
  conf: repl (marker) · class: meas (marker) · holds: human oral plaque, biological samples · src: larosaHypothesisTestingPower2012 (FT; meas; repl) · trail: MB-01 §4.2, §answers · from: MB-01:B-0234, MB-01:I-0096, MB-01:A-192
- **overdispersion.2** Every public dataset surveyed showed more variance than Poisson among biological replicates.
  conf: repl (marker) · class: meas (marker) · holds: biological replicates in public datasets · src: mcmurdieWasteNotWant2014 (FT; meas; repl) · trail: MB-01 §4.2, §answers · from: MB-01:I-0097, MB-01:A-192
- **overdispersion.3** Hierarchical Dirichlet-multinomial models detected shifts better than alternatives in simulation.
  conf: single (marker) · class: model (marker) · holds: simulation · src: harrisonDirichletmultinomialModellingOutperforms2020 (AB; model; single) · trail: MB-01 §4.2 · from: MB-01:I-0098
- **overdispersion.4** Beta-binomial and logistic-normal network models relax the multinomial further, by their makers' account.
  conf: not stated · class: not stated · holds: makers' claims · src: martinModelingMicrobialAbundances2020 (AB; makers' claims), willisEstimatingDiversityNetworked2022 (AB; makers' claims) · trail: MB-01 §4.2 · from: MB-01:B-0235
- **overdispersion.5** Dirichlet-multinomial overdispersion has been shown only between biological samples; no study fitting overdispersion to 16S technical replicates at controlled depths was found.
  conf: not stated · class: search (note: "No study fitting overdispersion to 16S technical replicates was found") · holds: the statistics angle's search · src: none (a search result) · trail: MB-01 §4.2, §answers, §critic, §Search record, §Provenance · search: searched, not found (note: "No study fitting overdispersion to 16S technical replicates was found") · from: MB-01:B-0238, MB-01:A-217, MB-01:A-222, MB-01:C-039, MB-01:B-0017, MB-01:B-0382

### technical-variation: processes other than sampling
needs: count-sampling, pcr
- **technical-variation.1** In four artificial-gut vessels sampled hourly with 20 technical replicates per vessel, 76% of observed variation was attributed to technical sources beyond sequence counting; this rests on one study.
  conf: single (marker) · class: model (marker) · holds: four artificial-gut vessels, hourly sampling · src: silvermanDynamicLinearModels2018 (FT; model; single) · trail: MB-01 §4.3, §answers, §critic · from: MB-01:I-0099, MB-01:B-0239, MB-01:A-194, MB-01:A-195, MB-01:A-226, MB-01:C-038
- **technical-variation.2** PCR replicates split before PCR differed strongly while replicates split after PCR were nearly identical; in negative extraction controls, most species appeared in only one of five PCR replicates (mean Jaccard distance 0.80, range 0.65 to 0.87).
  conf: single (marker) · class: meas (marker) · holds: negative extraction controls; low load · src: dyrhovdenManagingContaminationDiverse2021 (FT; meas; single) · trail: MB-01 §4.3, §answers, §critic, §Adversarial · from: MB-01:I-0100, MB-01:A-197, MB-01:A-228, MB-01:C-059, MB-01:C-082
- **technical-variation.3** At a 1:10^5 dilution of a staggered mock, 12 species appeared in only 2 of 4 PCR replicates.
  conf: not stated · class: not stated · holds: a staggered mock · src: dyrhovdenManagingContaminationDiverse2021 · trail: MB-01 §4.3 · from: MB-01:B-0240, MB-01:B-0241
- **technical-variation.4** At low input, library preparation reached its Poisson loading limit, the two rarest taxa dropped out, and contaminants appeared below about 10^4 copies.
  conf: not stated · class: not stated · holds: low input · src: barlowQuantitativeSequencingFramework2020 · trail: MB-01 §4.3, §answers · from: MB-01:B-0242, MB-01:A-202
- **technical-variation.5** Synthetic barcode pools showed the same stochastic early-amplification mechanism.
  conf: not stated · class: not stated · holds: synthetic barcode pools, indirect · src: kebschullSourcesPCRinducedDistortions2015 (INDIRECT) · trail: MB-01 §4.3 · from: MB-01:B-0243, MB-01:B-0240
- **technical-variation.6** One HiSeq run lost an archaeal mock taxon from all samples and shifted others by more than 2-fold, while re-running the same amplicons was normal.
  conf: single (marker) · class: meas (marker) · holds: one HiSeq run · src: yehTaxonDisappearanceMicrobiome2018 (FT; meas; single) · trail: MB-01 §4.3, §answers · from: MB-01:I-0101, MB-01:B-0244, MB-01:A-088, MB-01:A-089, MB-01:A-198, MB-01:B-0073
- **technical-variation.7** A PCR machine with a mis-set annealing temperature produced a batch outlier.
  conf: not stated · class: not stated · holds: a gut mock study · src: silvermanMeasuringMitigatingPCR2021 · trail: MB-01 §4.3, §answers · from: MB-01:B-0245, MB-01:A-198
- **technical-variation.8** Per-strain CV across five runs had a median of 11.8% (range 5.5 to 73.7%), and under-represented strains varied most.
  conf: not stated · class: not stated · holds: a 20-strain mock across five runs · src: laursenGenomicGCcontentAffects2017 · trail: MB-01 §4.3, §answers · from: MB-01:B-0246, MB-01:A-204
- **technical-variation.9** Mean relative abundances were reproducible across two runs and two depths.
  conf: not stated · class: not stated · holds: Pinto and Raskin 2012 · src: pintoPCRBiasesDistort2012 · trail: MB-01 §4.3, §answers · from: MB-01:B-0248, MB-01:A-199
- **technical-variation.10** Interlaboratory differences were substantial.
  conf: not stated · class: not stated · holds: the MBQC interlaboratory study · src: sinhaAssessmentVariationMicrobial2017 · trail: MB-01 §4.3, §answers · from: MB-01:B-0249, MB-01:A-198
- **technical-variation.11** Batch-correction tools exist, and their makers claim they work.
  conf: not stated · class: not stated · holds: makers' claims · src: gibbonsCorrectingBatchEffects2018 (AB), lingBatchEffectsRemoval2022 (AB) · trail: MB-01 §4.3 · from: MB-01:B-0250
- **technical-variation.12** Primer mismatch and low efficiency remove or suppress specific taxa, a non-random dropout.
  conf: not stated · class: not stated · holds: primer studies · src: paradaEveryBaseMatters2016, waltersImprovedBacterial16S2016 · trail: MB-01 §4.3, §answers · from: MB-01:B-0251, MB-01:A-200
- **technical-variation.13** In eDNA simulations with a low-efficiency primer set, a median of 88 of 1,000 taxa were detected after 20 cycles.
  conf: not stated · class: model (note: "[model; INDIRECT]") · holds: eukaryotic eDNA simulations, indirect · src: kellyUnderstandingPCRProcesses2019 (model; INDIRECT) · trail: MB-01 §4.3, §answers · from: MB-01:B-0252, MB-01:A-201
- **technical-variation.14** In simulation, simple count models sufficed across four zero-generating processes, and zero inflation was warranted only under narrow conditions.
  conf: single (marker) · class: model (marker) · holds: simulation · src: silvermanNaughtAllZeros2020 (AB; model; single) · trail: MB-01 §4.3, §answers · from: MB-01:I-0102, MB-01:A-213
- **technical-variation.15** Pseudocounts made tests conservative.
  conf: single (marker) · class: model (marker) · holds: simulation · src: kaulAnalysisMicrobiomeData2017 (AB; model; single) · trail: MB-01 §4.3 · from: MB-01:I-0103
- **technical-variation.16** Schloss asserts that a microbiome zero more likely means true absence, which conflicts with the interpretation of absences as sampling.
  conf: not stated · class: assert (marker) · holds: an assertion · src: schlossWasteNotWant2024 (FT; assert), grilliMacroecologicalLawsDescribe2020 · trail: MB-01 §4.3, §answers, §6. Where · from: MB-01:I-0104, MB-01:A-219, MB-01:B-0343
- **technical-variation.17** Technical variance beyond counting, early stochastic amplification at low load, whole-run taxon loss and primer-driven dropout are measured, but each mostly in a single study.
  conf: single (critic: MB-01:C-038) · class: not stated · holds: single studies (Silverman 2018; Dyrhovden 2021; Yeh 2018) · src: silvermanDynamicLinearModels2018, dyrhovdenManagingContaminationDiverse2021, yehTaxonDisappearanceMicrobiome2018 · trail: MB-01 §answers, §8. Answers, §critic · rating: "Weak on how much non-sampling technical variance there is" · from: MB-01:A-215, MB-01:A-308, MB-01:C-038

### replicate-depth: technical replicates at different read depths
needs: count-sampling
- **replicate-depth.1** In one soil sample, abundance-weighted OTU overlap among technical replicates rose from 56.7% at 2,000 reads to 95.3% at 160,000, and Bray-Curtis among technical replicates was 0.269 against 0.374 among treatment replicates.
  conf: repl (marker) · class: meas (marker) · holds: one soil sample · src: wenEvaluationReproducibilityAmplicon2017 (FT; meas; repl) · trail: MB-01 §4.4, §answers · contrary: one-sided (critic: MB-01:C-120) · from: MB-01:B-0253, MB-01:I-0105, MB-01:A-207, MB-01:C-120
- **replicate-depth.2** On MiSeq, 18 soil extracts shared 33.4% of OTUs between two technical replicates and 20.2% among three, and in one deeply sequenced sample presence/absence overlap rose from 20.7% at 2,000 reads to 43.9% at 160,000, plateauing near 30,000.
  conf: not stated · class: not stated · holds: 18 soil extracts, MiSeq · src: wenEvaluationReproducibilityAmplicon2017 · trail: MB-01 §4.4, §answers · from: MB-01:B-0257, MB-01:B-0258, MB-01:B-0259, MB-01:A-209, MB-01:A-227
- **replicate-depth.3** Greater depth improved replicate agreement in beta diversity for some mocks only.
  conf: not stated · class: not stated · holds: Pinto and Raskin 2012 · src: pintoPCRBiasesDistort2012 · trail: MB-01 §4.4 · from: MB-01:B-0255
- **replicate-depth.4** A preprint reports technical-replicate Jaccard distances of typically about 0.15, and up to 0.71 across runs.
  conf: not stated · class: not stated · holds: a preprint abstract · src: edgarUNBIASAttemptCorrect2017 (AB; PREPRINT) · trail: MB-01 §4.4, §answers · from: MB-01:B-0256, MB-01:A-225
- **replicate-depth.5** In ITS data, OTUs averaging more than 10 reads were detected in nearly all replicates, and replicate dissimilarity (pseudo-beta-diversity) fell markedly with depth.
  conf: not stated · class: not stated · holds: ITS, indirect · src: smithSequenceDepthNot2014 (INDIRECT, ITS) · trail: MB-01 §4.4, §answers · from: MB-01:B-0260, MB-01:A-190, MB-01:A-211
- **replicate-depth.6** Replicate variation affected beta diversity more than alpha diversity, and alpha diversity did not differ among technical replicates.
  conf: not stated · class: not stated · holds: technical replicates · src: zhouReproducibilityQuantitationAmplicon2011, wenEvaluationReproducibilityAmplicon2017 · trail: MB-01 §4.4 · from: MB-01:B-0261, MB-01:B-0262
- **replicate-depth.7** Replicate agreement rises with read depth.
  conf: not stated · class: not stated · holds: the four studies named (Wen 2017; Zhou 2013; Smith and Peay 2014; Barlow 2020) · src: wenEvaluationReproducibilityAmplicon2017, zhouRandomSamplingProcess2013, smithSequenceDepthNot2014, barlowQuantitativeSequencingFramework2020 · trail: MB-01 §answers · rating: "Moderate for the depth dependence of replicate agreement" · contrary: one-sided (critic: MB-01:C-120) · from: MB-01:A-203, MB-01:A-216, MB-01:C-120
- **replicate-depth.8** Not found: a 16S study testing whether technical-replicate variance of relative abundance exceeds multinomial expectation across controlled read depths, and replicate-at-depth studies in water or in host samples other than gut; replicate-at-depth studies are confined to one soil laboratory and one mouse caecum.
  conf: not stated · class: search (note: "statistics angle; Europe PMC and web search") · holds: soil dominates the replicate-at-depth evidence · src: none (a search result) · trail: MB-01 §answers, §critic, §Adversarial · search: searched, not found (note: "statistics angle; Europe PMC and web search") · from: MB-01:A-222, MB-01:C-040, MB-01:C-115


### rarefying: rarefying and rarefaction to a common depth
needs: reads-per-sample, scaling-normalisation, compositional-data
group: depth-normalisation
- **rarefying.1** Rarefaction comes from ecology, traced to Sanders 1968, Hurlbert 1971 and Simberloff 1972, which are known only through Chao and Jost 2012.
  conf: not stated · class: not stated · holds: ecology · src: sandersMarineBenthicDiversity1968 (SEC), hurlbertNonconceptSpeciesDiversity1971 (SEC), simberloff1972 (SEC), chaoCoveragebasedRarefactionExtrapolation2012 · trail: MB-01 §5.1, §References · limit: access (note: "known only through Chao and Jost 2012") · from: MB-01:B-0263, MB-01:R-0614
- **rarefying.2** Gotelli and Colwell argue that individual-based rarefaction allows meaningful comparison and that asymptotic estimators give lower bounds.
  conf: not stated · class: assert (marker) · holds: indirect evidence · src: gotelliQuantifyingBiodiversityProcedures2001 (AB; assert; INDIRECT) · trail: MB-01 §5.1 · from: MB-01:I-0106
- **rarefying.3** Schloss distinguishes "rarefying" (one random subsample) from "rarefaction" (the mean over many subsamples).
  conf: not stated · class: not stated · holds: terminology · src: schlossRarefactionCurrentlyBest2024 · trail: MB-01 §5.2 · from: MB-01:B-0269
- **rarefying.4** Under multinomial-type null models built from 12 V4 datasets, only rarefaction removed the correlation between richness and depth (size-based iNEXT nearly did, except for the small, evenly sequenced marine and soil sets), and when depth was confounded with group only rarefaction and size-based iNEXT held a 5% false-positive rate, with rarefaction giving the highest power; this is the author's conclusion from modelled data.
  conf: not stated · class: model (note: "modelled") · holds: null models from 12 V4 datasets · src: schlossRarefactionCurrentlyBest2024 · trail: MB-01 §5.2, §answers · from: MB-01:B-0270, MB-01:B-0271, MB-01:B-0272, MB-01:A-231, MB-01:A-232
- **rarefying.5** The null model reassigns sequences at random, so samples differ only through multinomial-type sampling; taxon-specific bias, technical variation beyond counting, and differences in load are absent from the simulated truth.
  conf: not stated · class: reading (note: "statistics angle's reading") · holds: the null model (the statistics angle's reading) · src: schlossRarefactionCurrentlyBest2024 · trail: MB-01 §5.2 · from: MB-01:B-0273, MB-01:B-0274, MB-01:B-0275
- **rarefying.6** Repeated rarefying shows that the random variation rarefying introduces grows as rarefied depth shrinks.
  conf: single (marker) · class: meas (marker) · holds: one study · src: cameronEnhancingDiversityAnalysis2021 (FT; meas; single) · trail: MB-01 §5.3, §answers · from: MB-01:I-0125, MB-01:A-248
- **rarefying.7** Whether to rarefy is contested: McMurdie and Holmes 2014 against Schloss 2024a and 2024b, Weiss 2017 and, in part, Hong 2022, with Willis 2019 opposing rarefying for richness; no approach is shown to correct depth, load and taxon-specific bias together.
  conf: cont (critic: MB-01:C-041) · class: not stated · holds: simulations and benchmarks · src: mcmurdieWasteNotWant2014, schlossWasteNotWant2024, schlossRarefactionCurrentlyBest2024, weissNormalizationMicrobialDifferential2017, hongRarefyNotRarefy2022, willisRarefactionAlphaDiversity2019 · trail: MB-01 §answers, §6. Where, §critic, §8. Answers · rating: "Weak to moderate overall" · from: MB-01:A-230, MB-01:A-273, MB-01:A-280, MB-01:A-309, MB-01:B-0339, MB-01:B-0340, MB-01:C-041, MB-01:B-0041
- **rarefying.8** Rarefaction is favoured for alpha and beta diversity under depth confounding in null-model simulations dominated by one author (supported in part by Weiss 2017 for beta and differential abundance); without Schloss 2024b, rarefying would remain contested, with McMurdie and Holmes 2014 as the main benchmark against it.
  conf: not stated · class: not stated · holds: null-model simulations · src: schlossRarefactionCurrentlyBest2024, weissNormalizationMicrobialDifferential2017, mcmurdieWasteNotWant2014 · trail: MB-01 §answers, §8. Answers · from: MB-01:A-310, MB-01:A-290, MB-01:A-291
- **rarefying.9** In the review's summary, rarefying or rarefaction removes depth dependence of alpha and beta diversity under the null and controls false positives under confounding, but loses data and power, adds variance when done once, gave high differential-abundance false-positive rates in one benchmark, is argued to bias richness, and does not touch bias or load; it applies to all three measures and is contested. The summary table mixes makers' claims and simulation results with measured results without a per-cell evidence class.
  conf: not stated · class: not stated · holds: the review's summary by approach · src: schlossRarefactionCurrentlyBest2024, weissNormalizationMicrobialDifferential2017, hongRarefyNotRarefy2022, mcmurdieWasteNotWant2014, willisRarefactionAlphaDiversity2019 · trail: MB-01 §5.6, §Adversarial · from: MB-01:B-0320, MB-01:B-0326, MB-01:C-143
- **rarefying.10** Rarefaction curves display sampling completeness (ecology) and were not benchmarked as a comparison method in the sources found.
  conf: not stated · class: not stated · holds: the review's summary by approach · src: none (the review's summary) · trail: MB-01 §5.6 · from: MB-01:B-0320, MB-01:B-0325
- **rarefying.11** Simulation results on rarefying and its alternatives flip with design choices, as Weiss 2017 and Schloss 2024a both say.
  conf: not stated · class: not stated · holds: simulation benchmarks · src: weissNormalizationMicrobialDifferential2017, schlossWasteNotWant2024, hongRarefyNotRarefy2022 · trail: MB-01 §answers, §Adversarial · from: MB-01:A-284, MB-01:C-142

### scaling-normalisation: scaling normalisations from RNA-seq
needs: rarefying
group: depth-normalisation
- **scaling-normalisation.1** In RNA-seq, total-count scaling can bias differential-expression estimates.
  conf: not stated · class: not stated · holds: RNA-seq, indirect · src: bullardEvaluationStatisticalMethods2010 (AB; INDIRECT) · trail: MB-01 §5.1 · from: MB-01:B-0264
- **scaling-normalisation.2** TMM and DESeq's negative binomial model also come from RNA-seq, and both assume most features are unchanged between conditions.
  conf: not stated · class: not stated · holds: RNA-seq, indirect · src: robinsonScalingNormalizationMethod2010 (AB; INDIRECT), andersDifferentialExpressionAnalysis2010 (AB; INDIRECT), weissNormalizationMicrobialDifferential2017 · trail: MB-01 §5.1 · from: MB-01:B-0265, MB-01:B-0266
- **scaling-normalisation.3** In shotgun gene-abundance data, TMM and RLE performed best.
  conf: not stated · class: not stated · holds: shotgun gene-abundance data, indirect · src: pereiraComparisonNormalizationMethods2018 (AB; INDIRECT, shotgun) · trail: MB-01 §5.1 · from: MB-01:B-0267
- **scaling-normalisation.4** Scaling normalisations used on microbiome data (TMM, RLE, CSS, VST, SRS, Wrench) come from RNA-seq and assume most features do not change, and under Schloss's null model they did not remove depth effects.
  conf: not stated · class: not stated · holds: Schloss's null model · src: bullardEvaluationStatisticalMethods2010, robinsonScalingNormalizationMethod2010, andersDifferentialExpressionAnalysis2010, schlossRarefactionCurrentlyBest2024 · trail: MB-01 §answers · from: MB-01:A-270, MB-01:A-271
- **scaling-normalisation.5** In a simulation, RLE and VST came close to quantitative methods for association tests in a dysbiosis scenario.
  conf: not stated · class: not stated · holds: a simulation, dysbiosis scenario · src: llorensricoBenchmarkingMicrobiomeTransformations2021 · trail: MB-01 §answers · from: MB-01:A-272
- **scaling-normalisation.6** Wrench's makers state that library-size scaling and rarefaction cannot correct compositional bias that is uncorrelated with library size.
  conf: not stated · class: not stated · holds: a makers' claim · src: kumarAnalysisCorrectionCompositional2018 (AB; makers' claim) · trail: MB-01 §5.4 · from: MB-01:B-0307
- **scaling-normalisation.7** SRS's makers claim better reproducibility than rarefying.
  conf: not stated · class: not stated · holds: a makers' claim · src: beuleImprovedNormalizationSpecies2020 (AB) · trail: MB-01 §5.4 · from: MB-01:B-0308
- **scaling-normalisation.8** In the review's summary, scaling methods (TMM, RLE, CSS, VST, SRS, Wrench) show some FDR and power benefits at small n (DESeq2) and come close to quantitative methods in a dysbiosis simulation, but are depth-sensitive for beta and alpha diversity under the null, assume most taxa unchanged, and DESeq2's FDR rises with n and uneven libraries; the summary table mixes evidence classes without a per-cell label.
  conf: not stated · class: not stated · holds: the review's summary by approach; differential abundance and beta diversity · src: weissNormalizationMicrobialDifferential2017, schlossRarefactionCurrentlyBest2024, llorensricoBenchmarkingMicrobiomeTransformations2021 · trail: MB-01 §5.6, §Adversarial · from: MB-01:B-0320, MB-01:B-0328, MB-01:C-143

### compositional-data: compositional data analysis and log-ratios
needs: rarefying
group: depth-normalisation
- **compositional-data.1** A review argues that 16S data are compositions "at all stages" and should be analysed with log-ratios.
  conf: cont (marker) · class: assert (marker) · holds: a review · src: gloorMicrobiomeDatasetsCompositional2017 (AB; assert; cont) · trail: MB-01 §5.1 · from: MB-01:I-0110
- **compositional-data.2** In the review's summary, compositional (log-ratio) approaches give ratio fold changes invariant to load and to multiplicative bias, and ANCOM and ALDEx2 are conservative, but Aitchison distances are depth-sensitive under the null, ANCOM-BC shows type I inflation in some settings, and results are sensitive to pseudocounts; the summary table mixes evidence classes without a per-cell label.
  conf: not stated · class: not stated · holds: the review's summary by approach; differential abundance and beta diversity · src: mclarenConsistentCorrectableBias2019, nearingMicrobiomeDifferentialAbundance2022, schlossRarefactionCurrentlyBest2024, yangComprehensiveEvaluationMicrobial2022, kaulAnalysisMicrobiomeData2017 · trail: MB-01 §5.6, §Adversarial · from: MB-01:B-0320, MB-01:B-0323, MB-01:C-143

### richness: richness and other alpha diversity measures
needs: rarefying, count-sampling, abundance-distribution
- **richness.1** Chao1, ACE, CatchAll, Shannon and Simpson all varied with library size in pyrosequencing data.
  conf: repl (marker) · class: meas (marker) · holds: pyrosequencing data · src: gihringMassivelyParallelRRNA2012 (AB; meas; repl) · trail: MB-01 §5.2 · from: MB-01:I-0112
- **richness.2** In Schloss's null models built from 12 V4 datasets, observed richness, Chao1, ACE, breakaway and SRS-normalised richness all correlated with depth.
  conf: cont (marker) · class: model (marker) · holds: null models from 12 V4 datasets · src: schlossRarefactionCurrentlyBest2024 (FT, re-opened; model; cont) · trail: MB-01 §5.2, §answers · from: MB-01:I-0113, MB-01:A-237
- **richness.3** Shannon was less depth-sensitive and inverse Simpson was not depth-sensitive; Simpson-type indices are robust.
  conf: not stated · class: not stated · holds: Schloss 2024b's null models; Haegeman 2013 · src: schlossRarefactionCurrentlyBest2024, haegemanRobustEstimationMicrobial2013 · trail: MB-01 §5.2, §answers · from: MB-01:B-0268, MB-01:A-242
- **richness.4** The depth dependence of raw and estimator richness is replicated.
  conf: repl (note: "the depth dependence of raw and estimator richness is replicated") · class: not stated · holds: the three studies named · src: gihringMassivelyParallelRRNA2012, schlossRarefactionCurrentlyBest2024, haegemanRobustEstimationMicrobial2013 · trail: MB-01 §answers · from: MB-01:A-274
- **richness.5** In the synthesis agent's re-reading of the full text, coverage-based iNEXT estimates were among those that "showed a strong correlation between richness and the number of sequences", and the text exempts only "rarefaction and possibly the size-based iNEXT estimates"; this is the only microbial amplicon test of coverage-based standardisation found, and beyond it the evidence is non-microbial.
  conf: single (critic: MB-01:C-049) · class: not stated · holds: Schloss 2024b's null models · src: schlossRarefactionCurrentlyBest2024 · trail: MB-01 §5.2, §answers, §critic, §Search record, §8. Answers · from: MB-01:B-0276, MB-01:B-0277, MB-01:B-0278, MB-01:A-236, MB-01:C-049, MB-01:C-050, MB-01:B-0374, MB-01:A-313
- **richness.6** Chao and Jost argue that standardising by sample completeness rather than size gives less biased richness ratios.
  conf: not stated · class: model (marker) · holds: indirect evidence · src: chaoCoveragebasedRarefactionExtrapolation2012 (FT; model; INDIRECT) · trail: MB-01 §5.1, §answers · from: MB-01:I-0107, MB-01:A-234
- **richness.7** Hill-number extrapolation is reliable only to about 2 to 3 times the reference sample size for richness.
  conf: not stated · class: model (marker) · holds: indirect evidence · src: chaoRarefactionExtrapolationHill2014 (FT; model; INDIRECT) · trail: MB-01 §5.1, §answers · from: MB-01:I-0108, MB-01:A-239
- **richness.8** A 2026 test on terrestrial inventories finds coverage-based rarefaction "does not respond predictably" to richness.
  conf: single (marker) · class: model (marker) · holds: terrestrial inventories, non-microbial, abstract only · src: alroyCoveragebasedRarefactionFails2026 (AB; model; single; INDIRECT) · trail: MB-01 §5.1, §answers · from: MB-01:I-0109, MB-01:A-235
- **richness.9** Coverage-based standardisation is disputed: Chao and Jost 2012 against Alroy 2026 (both non-microbial) and the microbial null model in Schloss 2024b.
  conf: not stated · class: not stated · holds: two non-microbial studies and one microbial null model · src: chaoCoveragebasedRarefactionExtrapolation2012, alroyCoveragebasedRarefactionFails2026, schlossRarefactionCurrentlyBest2024 · trail: MB-01 §answers · from: MB-01:A-282
- **richness.10** In the review's summary, coverage-based standardisation compresses richness ratios less than size-based rarefaction (ecology, modelled) but fails on terrestrial inventories and is depth-correlated in a microbial null model.
  conf: not stated · class: not stated · holds: the review's summary by approach; alpha diversity · src: chaoCoveragebasedRarefactionExtrapolation2012, alroyCoveragebasedRarefactionFails2026, schlossRarefactionCurrentlyBest2024 · trail: MB-01 §5.6 · from: MB-01:B-0320, MB-01:B-0322
- **richness.11** No independent microbial benchmark of coverage-based standardisation was found.
  conf: not stated · class: search (note: "An independent microbial benchmark of coverage-based standardisation (statistics angle)") · holds: the statistics angle's search · src: none (a search result) · trail: MB-01 §Search record, §Provenance · search: searched, not found (note: "An independent microbial benchmark of coverage-based standardisation (statistics angle)") · from: MB-01:B-0383, MB-01:B-0377, MB-01:B-0017
- **richness.12** Willis argues that plug-in and rarefied richness are both negatively biased, and that rarefying can create false differences between environments with equal richness but different abundance structures; she recommends estimators with variance estimates compared through measurement-error models, and presents statistical argument plus a worked simulated example.
  conf: cont (marker) · class: not stated (critic: MB-01:C-043) · holds: a perspective · src: willisRarefactionAlphaDiversity2019 (FT; cont; critic: MB-01:C-043 was "FT; assert; cont") · trail: MB-01 §5.2, §answers, §critic, §Adversarial · contrary: one-sided (critic: MB-01:C-126) · from: MB-01:B-0279, MB-01:I-0114, MB-01:A-233, MB-01:C-043, MB-01:C-124, MB-01:C-125, MB-01:C-126
- **richness.13** Breakaway and betta are offered by their makers as estimators with variance estimates.
  conf: not stated · class: not stated · holds: makers' claims · src: willisEstimatingDiversityFrequency2015 (AB; makers' claims), willisImprovedDetectionChanges2017 (AB; makers' claims) · trail: MB-01 §5.2 · from: MB-01:B-0280, MB-01:I-0114
- **richness.14** Breakaway intervals were mostly too wide to be useful, and breakaway stayed correlated with depth.
  conf: not stated · class: not stated · holds: Schloss 2024b's null models · src: schlossRarefactionCurrentlyBest2024 · trail: MB-01 §5.2, §answers · from: MB-01:B-0281, MB-01:A-237
- **richness.15** Sample data carry no information on the rare tail, and Chao's estimator ranked in silico communities wrongly: a community with 20 times fewer species was estimated to have 10 times more.
  conf: not stated · class: not stated · holds: in silico communities · src: haegemanRobustEstimationMicrobial2013 · trail: MB-01 §5.2, §answers · from: MB-01:B-0282, MB-01:B-0283, MB-01:B-0284, MB-01:A-238
- **richness.16** Bounds for Hill numbers of order 2 and above nearly coincide, and the authors recommend Shannon and Simpson over richness.
  conf: repl (marker) · class: model (marker) · holds: Haegeman et al.'s analysis · src: haegemanRobustEstimationMicrobial2013 (FT; model; repl) · trail: MB-01 §5.2 · from: MB-01:I-0115, MB-01:B-0285
- **richness.17** Chao1 and ACE are invalid on ASV tables from algorithms that drop singletons, as DADA2 does by default.
  conf: single (marker) · class: assert (marker) · holds: ASV tables · src: dengNonparametricRichnessEstimators2024 (FT; assert; single) · trail: MB-01 §5.2, §answers · from: MB-01:I-0116, MB-01:A-240
- **richness.18** Spurious OTUs severely inflated Chao1, and removing them severely underestimated Chao1 in uneven communities, while abundance-weighted metrics were little affected.
  conf: not stated · class: not stated · holds: Pinto and Raskin 2012 · src: pintoPCRBiasesDistort2012 · trail: MB-01 §5.2, §answers · from: MB-01:B-0286, MB-01:A-079, MB-01:A-080, MB-01:B-0071
- **richness.19** An abundance filter makes ACE and Chao1 inapplicable.
  conf: not stated · class: not stated · holds: Bokulich et al.'s quality filtering · src: bokulichQualityfilteringVastlyImproves2013 · trail: MB-01 §5.2 · from: MB-01:B-0287
- **richness.20** Spurious singletons inflate richness estimators, and a singleton-replacement estimator for error-inflated data has been proposed.
  conf: single (marker) · class: model (marker) · holds: a proposed estimator · src: chiuEstimatingComparingMicrobial2016 (AB; model; single), pintoPCRBiasesDistort2012 · trail: MB-01 §5.2, §answers · from: MB-01:I-0117, MB-01:A-241
- **richness.21** Multiplicative bias can make an uneven sample look more even, biasing Shannon and inverse Simpson.
  conf: not stated · class: model (note: "(McLaren 2019) [model]") · holds: McLaren et al.'s model · src: mclarenConsistentCorrectableBias2019 (model) · trail: MB-01 §5.2, §answers · from: MB-01:B-0288, MB-01:A-252
- **richness.22** PCR-bias calibration improved Shannon diversity in 7 of 10 mocks.
  conf: not stated · class: not stated · holds: 10 mocks · src: silvermanMeasuringMitigatingPCR2021 · trail: MB-01 §5.2 · from: MB-01:B-0289
- **richness.23** In simulated faecal communities with load varying from 1.9 x 10^9 to 10^13 cells per gram, all 13 transformations reproduced Shannon and Simpson diversity.
  conf: not stated · class: not stated · holds: simulated faecal communities · src: llorensricoBenchmarkingMicrobiomeTransformations2021 · trail: MB-01 §5.2 · from: MB-01:B-0290
- **richness.24** In simulated faecal communities, richness was recovered reliably only by quantitative profiling in a bloom scenario.
  conf: single (marker) · class: model (marker) · holds: simulated faecal communities, bloom scenario · src: llorensricoBenchmarkingMicrobiomeTransformations2021 (FT; model; single) · trail: MB-01 §5.2, §answers · from: MB-01:I-0118, MB-01:A-243, MB-01:B-0290
- **richness.25** In freshwater and sediment 454 data, 5,000 sequences captured Shannon trends and over 80% of Chao1 trends.
  conf: single (marker) · class: meas (marker) · holds: freshwater and sediment, 454 · src: lundinWhichSequencingDepth2012 (AB; meas; single) · trail: MB-01 §5.2 · from: MB-01:I-0119
- **richness.26** In the review's summary, richness estimators give lower bounds and extrapolation to about 2 to 3 times sample size (ecology), but are depth-correlated, have unidentifiable tails, are invalid without singletons and are inflated by spurious singletons.
  conf: not stated · class: not stated · holds: the review's summary by approach; alpha diversity · src: chaoRarefactionExtrapolationHill2014, haegemanRobustEstimationMicrobial2013, dengNonparametricRichnessEstimators2024, schlossRarefactionCurrentlyBest2024 · trail: MB-01 §5.6 · from: MB-01:B-0320, MB-01:B-0327

### beta-diversity: normalisation for beta diversity
needs: rarefying
- **beta-diversity.1** In Schloss's null models, Jaccard and Bray-Curtis computed from raw counts, relative abundances, CSS or SRS, Aitchison distances (four zero-handling variants) and DESeq2 VST Euclidean distances all correlated with depth differences; only rarefaction removed the correlation, and only rarefaction held 5% false positives in PERMANOVA under confounding.
  conf: not stated · class: not stated · holds: null models from 12 V4 datasets · src: schlossRarefactionCurrentlyBest2024 · trail: MB-01 §5.3, §answers · from: MB-01:B-0291, MB-01:B-0292, MB-01:A-244, MB-01:A-245, MB-01:A-251
- **beta-diversity.2** Rarefying clustered samples better for presence/absence metrics, and other normalisations were vulnerable below about 1,000 reads per sample.
  conf: repl (marker) · class: model (marker) · holds: Weiss et al.'s simulations · src: weissNormalizationMicrobialDifferential2017 (FT; model; repl) · trail: MB-01 §5.3 · from: MB-01:I-0120
- **beta-diversity.3** In simulations from Global Patterns, rarefying to the 15th percentile and dropping samples below it reduced clustering accuracy.
  conf: cont (marker) · class: model (marker) · holds: simulations from Global Patterns · src: mcmurdieWasteNotWant2014 (FT; model; cont) · trail: MB-01 §5.3, §answers · from: MB-01:I-0121, MB-01:A-246
- **beta-diversity.4** Schloss identified 11 design choices that disadvantaged rarefying in the McMurdie and Holmes study; notably, low-depth samples were removed only in the rarefied arm.
  conf: single (marker) · class: model (marker) · holds: a re-analysis of McMurdie and Holmes's simulations · src: schlossWasteNotWant2024 (FT; model; single) · trail: MB-01 §5.3, §answers · from: MB-01:B-0293, MB-01:I-0122, MB-01:A-246
- **beta-diversity.5** Proportions and rarefying were the only methods that fully normalised depth, and scaling methods masked differences in common OTUs.
  conf: single (marker) · class: model (marker) · holds: an abstract · src: mcknightMethodsNormalizingMicrobiome2019 (AB; model; single) · trail: MB-01 §5.3, §answers · from: MB-01:I-0123, MB-01:A-249
- **beta-diversity.6** Whether proportions normalise depth for beta diversity conflicts between studies: McKnight 2019 against Schloss 2024b, in which relative-abundance Bray-Curtis stayed depth-sensitive under the null.
  conf: cont (note: "This conflicts with Schloss 2024b") · class: not stated · holds: simulations · src: mcknightMethodsNormalizingMicrobiome2019, schlossRarefactionCurrentlyBest2024 · trail: MB-01 §5.3, §answers, §6. Where · from: MB-01:B-0294, MB-01:A-249, MB-01:A-281, MB-01:B-0341
- **beta-diversity.7** In real river data, rarefying barely changed Bray-Curtis or Jaccard (r > 0.9) and did not change weighted UniFrac.
  conf: not stated · class: not stated · holds: real river data · src: chiarelloRankingBiasesChoice2022 · trail: MB-01 §5.3, §answers · from: MB-01:B-0295, MB-01:B-0296, MB-01:A-247
- **beta-diversity.8** Library-size normalisation had very little effect on beta-diversity separation compared with the choice of distance metric.
  conf: single (marker) · class: meas (marker) · holds: an abstract · src: thorsenLargescaleBenchmarkingReveals2016 (AB; meas; single) · trail: MB-01 §5.3, §answers · from: MB-01:I-0124, MB-01:A-250
- **beta-diversity.9** 1,000 denoised sequences explained 90% of the Bray-Curtis trends seen at 15,000 to 20,000 sequences.
  conf: not stated · class: not stated · holds: freshwater and sediment, 454 · src: lundinWhichSequencingDepth2012 · trail: MB-01 §5.3 · from: MB-01:B-0297, MB-01:I-0119
- **beta-diversity.10** Bray-Curtis was usually the most powerful beta-diversity metric, and metric choice changes power.
  conf: single (marker) · class: meas (marker) · holds: an abstract · src: kersPowerMicrobiomeStudies2022 (AB; meas; single) · trail: MB-01 §5.3 · from: MB-01:I-0126
- **beta-diversity.11** Evidence on how to normalise for beta diversity is contested and simulation-based.
  conf: cont (note: "Beta: contested, simulation-based") · class: not stated · holds: simulations · src: schlossRarefactionCurrentlyBest2024, mcmurdieWasteNotWant2014, weissNormalizationMicrobialDifferential2017 · trail: MB-01 §answers · from: MB-01:A-276

### differential-abundance: tests of which taxa differ in abundance
needs: rarefying, bias-consistency
- **differential-abundance.1** Studies disagree on whether rarefying harms differential-abundance tests.
  conf: cont (note: "Studies disagree on whether rarefying harms differential-abundance tests") · class: not stated · holds: simulations and benchmarks · src: mcmurdieWasteNotWant2014, weissNormalizationMicrobialDifferential2017, hongRarefyNotRarefy2022, yangComprehensiveEvaluationMicrobial2022 · trail: MB-01 §5.4, §answers · from: MB-01:B-0298, MB-01:A-253
- **differential-abundance.2** Rarefied counts and proportions gave high false-positive rates, while DESeq2 and edgeR were near zero.
  conf: not stated · class: not stated · holds: McMurdie and Holmes's simulations · src: mcmurdieWasteNotWant2014 · trail: MB-01 §5.4, §answers · from: MB-01:B-0299, MB-01:A-254
- **differential-abundance.3** Rarefying did not raise FDR for most methods, and lowered it at about 10x group differences in library size, at a cost in sensitivity.
  conf: not stated · class: not stated · holds: Weiss et al.'s simulations · src: weissNormalizationMicrobialDifferential2017 · trail: MB-01 §5.4, §answers · from: MB-01:B-0300, MB-01:B-0301, MB-01:A-255
- **differential-abundance.4** DESeq2's FDR rose with more samples or uneven libraries, and ANCOM alone controlled FDR well.
  conf: not stated · class: not stated · holds: Weiss et al.'s simulations · src: weissNormalizationMicrobialDifferential2017 · trail: MB-01 §5.4, §answers · from: MB-01:B-0302, MB-01:A-258
- **differential-abundance.5** Rarefying followed by permutation controls type I error; the sensitivity loss is negligible when overdispersion is high, and is summarised by a rarefaction efficiency index.
  conf: single (marker) · class: model (marker) · holds: Hong et al.'s analysis · src: hongRarefyNotRarefy2022 (FT; model; single) · trail: MB-01 §5.4, §answers · from: MB-01:I-0127, MB-01:A-256
- **differential-abundance.6** Tests on proportions at a tenfold depth difference had severe type I inflation, which rarefying controlled, and no method was "simultaneously robust, powerful, and flexible"; ANCOM-BC showed type I inflation in some settings.
  conf: repl (marker) · class: model (marker) · holds: Yang and Chen's simulations · src: yangComprehensiveEvaluationMicrobial2022 (FT; model; repl) · trail: MB-01 §5.4, §answers · from: MB-01:I-0128, MB-01:A-257, MB-01:A-260
- **differential-abundance.7** Fourteen differential-abundance methods on 38 datasets gave 0.8% to 40.5% significant ASVs (unfiltered means).
  conf: not stated · class: not stated · holds: 38 real datasets · src: nearingMicrobiomeDifferentialAbundance2022 · trail: MB-01 §5.4, §answers · from: MB-01:B-0303, MB-01:A-264
- **differential-abundance.8** ALDEx2 and ANCOM-II were the most consistent across 38 datasets, and edgeR and LEfSe produced many false positives on random splits.
  conf: single (marker) · class: meas (marker) · holds: 38 real datasets · src: nearingMicrobiomeDifferentialAbundance2022 (FT; meas; single) · trail: MB-01 §5.4, §answers · from: MB-01:I-0129, MB-01:A-259
- **differential-abundance.9** Excess false discoveries were widespread across differential-abundance methods.
  conf: repl (marker) · class: model (marker) · holds: an abstract · src: hawinkelBrokenPromiseMicrobiome2019 (AB; model; repl) · trail: MB-01 §5.4, §answers · from: MB-01:I-0130, MB-01:A-265
- **differential-abundance.10** Methods with the highest false-positive rates had the most power.
  conf: not stated · class: not stated · holds: Thorsen et al.'s benchmark · src: thorsenLargescaleBenchmarkingReveals2016 · trail: MB-01 §5.4 · from: MB-01:B-0304
- **differential-abundance.11** Microbiome-specific methods did not beat RNA-seq methods.
  conf: single (marker) · class: meas (marker) · holds: an abstract · src: calgaroAssessmentStatisticalMethods2020 (AB; meas; single) · trail: MB-01 §5.4 · from: MB-01:I-0131
- **differential-abundance.12** In implanted-signal benchmarks, only linear models, Wilcoxon, t-test, limma and fastANCOM controlled FDR at relatively high sensitivity; fitZig reached an observed FDR of 80%, and ANCOM and ANCOM-BC controlled FDR only at 200 or more samples per group.
  conf: repl (marker) · class: model (marker) · holds: implanted-signal benchmarks · src: wirbelRealisticBenchmarkDifferential2024 (FT; model; repl) · trail: MB-01 §5.4, §answers, §7. Bounds · from: MB-01:I-0132, MB-01:A-260, MB-01:A-263, MB-01:B-0364, MB-01:B-0365
- **differential-abundance.13** Elementary methods on relative abundances (Wilcoxon, linear models) were the most replicable across 53 studies.
  conf: single (marker) · class: meas (marker) · holds: 53 studies; an abstract · src: peltoElementaryMethodsProvide2025 (AB; meas; single) · trail: MB-01 §5.4, §answers · from: MB-01:I-0133, MB-01:A-263
- **differential-abundance.14** Makers claim FDR control for ANCOM-BC and ANCOM, and independent benchmarks disagree in part.
  conf: not stated · class: not stated · holds: makers' claims against independent benchmarks · src: linAnalysisCompositionsMicrobiomes2020 (AB; makers' claims), mandalAnalysisCompositionMicrobiomes2015 (AB; makers' claims), yangComprehensiveEvaluationMicrobial2022, wirbelRealisticBenchmarkDifferential2024 · trail: MB-01 §5.4, §answers · from: MB-01:B-0305, MB-01:B-0306, MB-01:A-283
- **differential-abundance.15** Reference frames make differential rankings invariant to load.
  conf: single (marker) · class: meas (marker) · holds: an abstract · src: mortonEstablishingMicrobialComposition2019 (AB; meas; single) · trail: MB-01 §5.4, §answers · from: MB-01:I-0134, MB-01:A-261
- **differential-abundance.16** Fold changes in taxon ratios are invariant to multiplicative bias; fold changes in proportions are not and can change sign; this bias-invariance of ratio-based methods rests on one source.
  conf: not stated · class: not stated · holds: McLaren et al.'s model · src: mclarenConsistentCorrectableBias2019 · trail: MB-01 §5.4, §answers · from: MB-01:B-0309, MB-01:A-262, MB-01:A-293
- **differential-abundance.17** Proportion-based differential-abundance results err when the community's mean efficiency is associated with the condition.
  conf: single (marker) · class: model (marker) · holds: a preprint abstract · src: mclarenImplicationsTaxonomicBias2022 (AB; PREPRINT; model; single) · trail: MB-01 §5.4, §answers · from: MB-01:I-0135, MB-01:A-262
- **differential-abundance.18** Differential-abundance results show large disagreement between methods and frequent FDR failures, robustly; which method is best is contested.
  conf: cont (note: "Which method is best is contested") · class: not stated · holds: benchmarks on real and simulated data · src: nearingMicrobiomeDifferentialAbundance2022, hawinkelBrokenPromiseMicrobiome2019, yangComprehensiveEvaluationMicrobial2022, wirbelRealisticBenchmarkDifferential2024 · trail: MB-01 §answers, §8. Answers, §critic · from: MB-01:A-277, MB-01:A-278, MB-01:A-311, MB-01:C-041
- **differential-abundance.19** In the review's summary, proportions are simple, and elementary tests on proportions were replicable and FDR-controlling in some benchmarks, but showed severe type I error with large depth differences, depth-sensitive beta diversity, and proportion error that varies with sample composition.
  conf: not stated · class: not stated · holds: the review's summary by approach; differential abundance and beta diversity · src: peltoElementaryMethodsProvide2025, wirbelRealisticBenchmarkDifferential2024, yangComprehensiveEvaluationMicrobial2022, schlossRarefactionCurrentlyBest2024, mclarenConsistentCorrectableBias2019 · trail: MB-01 §5.6, §Adversarial · from: MB-01:B-0320, MB-01:B-0324, MB-01:C-143

### absolute-quantification: absolute quantification of total load
needs: microbial-load, rarefying, bias-consistency
- **absolute-quantification.1** Load measurements (qPCR, flow cytometry, dPCR and spike-ins) change, and can reverse, conclusions drawn from relative data; this is replicated.
  conf: repl (note: "replicated that it changes conclusions") · class: not stated · holds: the four studies named · src: vandeputteQuantitativeMicrobiomeProfiling2017, propsAbsoluteQuantificationMicrobial2016, barlowQuantitativeSequencingFramework2020, tkaczAbsoluteQuantitationMicrobiota2018 · trail: MB-01 §5.5, §answers, §critic · from: MB-01:B-0310, MB-01:A-266, MB-01:A-279, MB-01:C-042
- **absolute-quantification.2** Flow-cytometry quantitative profiling showed the Bacteroides-Prevotella trade-off in relative data to be an artefact, and load drove Crohn's-associated differences.
  conf: not stated · class: not stated · holds: an abstract · src: vandeputteQuantitativeMicrobiomeProfiling2017 (AB) · trail: MB-01 §5.5 · from: MB-01:B-0311
- **absolute-quantification.3** In engineered freshwater, relative enrichment did not imply absolute outgrowth.
  conf: not stated · class: not stated · holds: engineered freshwater; an abstract · src: propsAbsoluteQuantificationMicrobial2016 (AB; engineered freshwater) · trail: MB-01 §5.5 · from: MB-01:B-0312
- **absolute-quantification.4** In soil, absolute abundance could hold steady or rise while relative abundance fell.
  conf: not stated · class: not stated · holds: soil · src: tkaczAbsoluteQuantitationMicrobiota2018 (FT; soil) · trail: MB-01 §5.5 · from: MB-01:B-0313
- **absolute-quantification.5** Spike-in bacteria added before extraction recovered ratios of absolute abundances across mouse faecal dilutions, but the three spike-in species gave different read yields.
  conf: repl (marker) · class: meas (marker) · holds: mouse faecal dilutions · src: stammlerAdjustingMicrobiomeProfiles2016 (FT; meas; repl) · trail: MB-01 §5.5 · from: MB-01:I-0136, MB-01:B-0314
- **absolute-quantification.6** dPCR anchoring gave about 2x extraction accuracy above 8.3 x 10^4 input copies, and absolute but not relative analysis revealed diet effects.
  conf: single (marker) · class: meas (marker) · holds: one study · src: barlowQuantitativeSequencingFramework2020 (FT; meas; single) · trail: MB-01 §5.5 · from: MB-01:I-0137
- **absolute-quantification.7** Soil internal standards tracked PLFA and respiration biomass better than those two measures tracked each other.
  conf: single (marker) · class: meas (marker) · holds: soil; an abstract · src: smetsMethodSimultaneousMeasurement2016 (AB; meas; single) · trail: MB-01 §5.5 · from: MB-01:I-0138
- **absolute-quantification.8** Total 16S qPCR multiplied by relative abundance correlated near-perfectly with taxon-specific qPCR, a comparison of methods that share an upstream (qPCR against qPCR-anchored sequencing) for four taxa.
  conf: single (marker) · class: meas (marker) · holds: four taxa · src: jianQuantitativePCRProvides2020 (FT; meas; single) · trail: MB-01 §5.5, §Adversarial · from: MB-01:I-0139, MB-01:C-127, MB-01:C-106
- **absolute-quantification.9** In simulation, experimental quantitative profiling outperformed computational transformations for associations.
  conf: not stated · class: not stated · holds: simulation · src: llorensricoBenchmarkingMicrobiomeTransformations2021 · trail: MB-01 §5.5 · from: MB-01:B-0315
- **absolute-quantification.10** Absolute quantification addresses differences in load but does not remove taxon-specific extraction and PCR bias.
  conf: not stated · class: not stated · holds: as stated · src: mclarenConsistentCorrectableBias2019, bonkPCRbasedQuantificationTaxaspecific2018 · trail: MB-01 §5.5, §answers, §critic, §8. Answers · from: MB-01:B-0316, MB-01:B-0317, MB-01:A-267, MB-01:A-312, MB-01:C-042
- **absolute-quantification.11** qPCR and sequencing both count extracellular DNA, unlike cell counts.
  conf: not stated · class: not stated · holds: as stated · src: jianQuantitativePCRProvides2020 · trail: MB-01 §5.5 · from: MB-01:B-0318
- **absolute-quantification.12** qPCR and flow cytometry agreed on a whole-cell mock (|r| = 0.967) but gave "highly divergent" profiles for faeces, where qPCR and flow-cytometry enumeration correlated at Pearson r = -0.50; ddPCR correlated strongly with qPCR, and the authors used this to rule out qPCR imprecision as the cause of the divergence.
  conf: single (marker) · class: meas (marker) · holds: a whole-cell mock and faeces · src: galazzoHowCountOur2020 (FT; meas; single) · trail: MB-01 §5.5, §answers, §critic, §Adversarial · from: MB-01:I-0140, MB-01:A-267, MB-01:A-292, MB-01:C-045, MB-01:C-057, MB-01:C-071
- **absolute-quantification.13** Synthetic spike-ins had differing detection efficiencies and small departures from linearity, and correlations were weaker with Taq than with KOD polymerase.
  conf: repl (marker) · class: meas (marker) · holds: synthetic spike-in standards · src: tourlousseSyntheticSpikeinStandards2016 (FT; meas; repl) · trail: MB-01 §5.5 · from: MB-01:I-0141
- **absolute-quantification.14** Seawater internal standards agreed with flow cytometry at r2 = 0.19 until corrections for copy number and particle association (with four outliers removed) raised it to 0.61, and the authors conclude that the internal-standard method is quantitative and consistent with flow cytometry; the r2 figures need the body and could not be verified.
  conf: single (marker) · class: meas (marker) · holds: seawater · src: linTowardsQuantitativeMicrobiome2019 (FT; meas; single) · trail: MB-01 §5.5, §answers, §critic, §Adversarial · limit: access (critic: MB-01:C-076) · contrary: one-sided (critic: MB-01:C-127) · from: MB-01:I-0142, MB-01:A-269, MB-01:B-0363, MB-01:C-046, MB-01:C-047, MB-01:C-048, MB-01:C-076, MB-01:C-081, MB-01:C-127
- **absolute-quantification.15** A review states that internal standards often underperform or fail.
  conf: not stated · class: assert (marker) · holds: a review · src: harrisonQuestAbsoluteAbundance2020 (AB; assert) · trail: MB-01 §5.5 · from: MB-01:I-0143
- **absolute-quantification.16** The agreement between absolute-quantification methods is weak: on qPCR against flow cytometry, Jian 2020 and Galazzo 2020 conflict, and the divergence of the methods rests on Galazzo 2020.
  conf: not stated · class: not stated · holds: the two studies named · src: jianQuantitativePCRProvides2020, galazzoHowCountOur2020 · trail: MB-01 §answers, §6. Where · rating: "weak on the agreement between quantification methods" · from: MB-01:A-279, MB-01:A-283, MB-01:A-292, MB-01:B-0342
- **absolute-quantification.17** In the review's summary, absolute load measurements correct differences in total load and reversals of relative trends, but not taxon-specific bias, extraction-yield variation, or disagreement between qPCR and flow cytometry; they apply to all three measures and are strongest for differential abundance and associations.
  conf: not stated · class: not stated · holds: the review's summary by approach · src: none (the review's summary) · trail: MB-01 §5.6, §Adversarial · from: MB-01:B-0320, MB-01:B-0321, MB-01:C-143
- **absolute-quantification.18** No approach is shown to correct depth, load and taxon-specific bias together: no benchmark builds taxon-specific bias and differences in total load into the simulated truth together, apart from one that simulated faeces without taxon bias; no benchmark in soil or water used measured absolute loads as truth; and no richness correction was tested against known-richness mocks across depths.
  conf: not stated · class: search (note: "Not found: an independent microbial amplicon benchmark of coverage-based standardisation with known truth") · holds: the statistics angle's routes (Europe PMC, Crossref, publisher HTML, author PDFs, web search) and the lab and bioinformatics angles for spike-ins · src: llorensricoBenchmarkingMicrobiomeTransformations2021 · trail: MB-01 §answers, §critic, §Adversarial · search: searched, not found (note: "Not found: an independent microbial amplicon benchmark of coverage-based standardisation with known truth") · from: MB-01:A-230, MB-01:A-285, MB-01:A-286, MB-01:C-051, MB-01:C-118


### rarity-terms: within-sample abundance terms and the rare biosphere
needs: abundance-distribution
- **rarity-terms.1** Three families of definition of abundance and distribution terms are in use and are not interchangeable: within-sample relative-abundance thresholds (0.1% most common for rare, 1% for abundant), occupancy (core, mostly occurrence-only, 30 to 100%), and regional or global classes defined on pooled data; usage is heterogeneous and often unstated, and the usage percentages rest on two surveys.
  conf: not stated · class: not stated · holds: microbial ecology literature; two systematic literature surveys plus reviews · src: pascoalDefinitionMicrobialRare2025, neuDefiningQuantifyingCore2021 · trail: MB-02 §answers, §critic · rating: "Strong on the fact of heterogeneity" · from: MB-02:A-060, MB-02:A-070, MB-02:A-079, MB-02:A-144, MB-02:A-145, MB-02:C-028, MB-02:C-029, MB-02:C-030
- **rarity-terms.2** Within a sample, rare is most often defined as below 0.1% of reads, sometimes below 0.01% or 0.001%, and abundant usually as above 1%; one of the sources cited for these thresholds uses a single rare/common cutoff and does not support "abundant above 1%".
  conf: not stated · class: not stated · holds: within-sample relative abundance · src: lynchEcologyExplorationRare2015, galandEcologyRareMicrobial2009, daiIdentifyingKeyTaxonomic2016, jiaUnravellingInterplayEcological2022 · trail: MB-02 §answers, §critic · from: MB-02:A-061, MB-02:C-031, MB-02:C-032, MB-02:C-065
- **rarity-terms.3** The "rare biosphere" entered usage with deep-sea tag sequencing, which found thousands of low-abundance populations alongside a few dominants.
  conf: not stated · class: not stated · holds: deep sea · src: soginMicrobialDiversityDeep2006 (AB) · trail: MB-02 §D2.1 · from: MB-02:B-0156
- **rarity-terms.4** Reviews describe a few dominant taxa and many rare ones without fixing a threshold.
  conf: not stated · class: not stated · holds: reviews · src: pedrosalioRareBacterialBiosphere2012 (AB), lynchEcologyExplorationRare2015 (AB), pascoalMicrobialRareBiosphere2021 (AB) · trail: MB-02 §D2.1 · from: MB-02:B-0157
- **rarity-terms.5** Rare has been defined as below 0.01% and abundant as above 1% per sample, a cutoff the authors called "much more severe than the <0.1% criteria proposed earlier" and tied to a singleton in the smallest library.
  conf: not stated · class: not stated · holds: per sample · src: galandEcologyRareMicrobial2009 (FT) · trail: MB-02 §D2.1 · from: MB-02:B-0158, MB-02:B-0159, MB-02:B-0160
- **rarity-terms.6** Rare below 0.1% and abundant above 1% were combined with behaviour across samples into six categories: always abundant, conditionally abundant, always rare, conditionally rare, moderate, and conditionally rare or abundant.
  conf: not stated · class: not stated · holds: one study · src: daiIdentifyingKeyTaxonomic2016 (AB) · trail: MB-02 §D2.1, §answers · from: MB-02:B-0161, MB-02:B-0162, MB-02:A-063
- **rarity-terms.7** In a survey of 181 rare-biosphere articles from 2006 to 2024, about 37% gave no clear method or definition; of those with one, about 84% used relative abundance thresholds and about 60% of those a single threshold, about half used 0.1%, and about 70% applied it per sample rather than to the pooled dataset.
  conf: not stated · class: not stated · holds: 181 articles; the only survey of rare-biosphere usage · src: pascoalDefinitionMicrobialRare2025 (FT) · trail: MB-02 §D2.1, §answers · from: MB-02:B-0163, MB-02:B-0164, MB-02:B-0165, MB-02:B-0166, MB-02:B-0167, MB-02:A-062, MB-02:A-079
- **rarity-terms.8** Conditionally rare taxa are defined by a bimodal abundance distribution over time (coefficient of bimodality) together with a maximum relative abundance above 1%; across 42 non-soil time series they made up 1.5 to 28% of membership.
  conf: not stated · class: not stated · holds: 42 non-soil time series · src: shadeConditionallyRareTaxa2014 (FT, excerpts) · trail: MB-02 §D2.2, §answers · from: MB-02:B-0179, MB-02:B-0180, MB-02:B-0181, MB-02:A-063
- **rarity-terms.9** A three-way split into permanently, transiently and conditionally rare taxa has been applied in soil.
  conf: not stated · class: not stated · holds: soil · src: jiaUnravellingInterplayEcological2022 (FT) · trail: MB-02 §D2.2, §answers · from: MB-02:B-0182, MB-02:A-063
- **rarity-terms.10** Across 30 datasets (1,998 samples), rarer taxa better predicted soil community structure; this abstract-level source does not report abundance-occupancy and is not used in the answers.
  conf: not stated · class: not stated · holds: 30 soil datasets; an abstract · src: ramirezDetectingMacroecologicalPatterns2017 (AB) · trail: MB-02 §Search record · from: MB-02:B-0303, MB-02:B-0304
- **rarity-terms.11** No survey was found that tallies definitions specifically within soil studies, or separately for bulk soil and rhizosphere.
  conf: not stated · class: search (note: "No survey found that tallies definitions specifically within soil studies") · holds: soil · src: none (a search result) · trail: MB-02 §answers · search: searched, not found (note: "No survey found that tallies definitions specifically within soil studies") · from: MB-02:A-075
- **rarity-terms.12** No study was found that compares threshold-based rarity classes between amplicon and metagenome data from the same soil samples; the ulrb comparison of amplicon and metagenome units used marine samples.
  conf: not stated · class: search (note: "No study found that compares threshold-based rarity classes") · holds: soil · src: pascoalDefinitionMicrobialRare2025 · trail: MB-02 §answers · search: searched, not found (note: "No study found that compares threshold-based rarity classes") · from: MB-02:A-076
- **rarity-terms.13** Copy-number-corrected rarity thresholds were not found to have been tested.
  conf: not stated · class: search (note: "Copy-number-corrected thresholds were not found to have been tested") · holds: as stated · src: none (a search result) · trail: MB-02 §answers · search: searched, not found (note: "Copy-number-corrected thresholds were not found to have been tested") · from: MB-02:A-077

### core-microbiome: occupancy, prevalence and the core
needs: rarity-terms
- **core-microbiome.1** "Core" is the main occupancy term; it was first framed as the members shared across samples, the overlap of Venn diagrams, with later calls to add persistence and connectivity.
  conf: not stated · class: not stated · holds: core-microbiome literature · src: shadeBeyondVennDiagram2012 (AB) · trail: MB-02 §D2.2 · from: MB-02:B-0168, MB-02:B-0169
- **core-microbiome.2** In a survey of 224 core-microbiome studies, 75.4% defined the core by occurrence only, 4% by relative abundance only and 11.6% by both, with over 18% not stating a method; occurrence cutoffs ran from 30% to 100% of samples (100% most common), and abundance cutoffs in combined methods from 0.1% to 4.5%.
  conf: not stated · class: not stated · holds: 224 studies; the only survey of core usage · src: neuDefiningQuantifyingCore2021 (FT, first 100,000 characters) · trail: MB-02 §D2.2, §answers · from: MB-02:B-0170, MB-02:B-0171, MB-02:B-0172, MB-02:B-0173, MB-02:B-0174, MB-02:B-0175, MB-02:B-0176, MB-02:A-064, MB-02:A-079
- **core-microbiome.3** Citing other work, Neu et al. report that only two OTUs were shared by all of 24 soil locations and none across 51 wastewater plants.
  conf: not stated · class: not stated · holds: soil and wastewater; secondary · src: neuDefiningQuantifyingCore2021 · trail: MB-02 §D2.2 · limit: access (note: "SECONDARY via [51]") · from: MB-02:B-0177
- **core-microbiome.4** Risely distinguishes five kinds of core (common, temporal, ecological, functional, host-adapted) and argues that no one definition captures all.
  conf: not stated · class: not stated · holds: host-microbe systems · src: riselyApplyingCoreMicrobiome2020 (AB) · trail: MB-02 §D2.2 · from: MB-02:B-0178

### regional-terms: regional and global distribution terms
needs: rarity-terms
- **regional-terms.1** In soil, "dominant" has been defined jointly: in the top 10% of phylotypes by share of 16S reads and present in more than half of 237 soils.
  conf: not stated · class: not stated · holds: 237 soils · src: delgadobaquerizoGlobalAtlasDominant2018 (FT) · trail: MB-02 §D2.3, §answers · from: MB-02:B-0183, MB-02:A-065
- **regional-terms.2** "Common" versus "rare" has also been set by a data-driven minimum cross-entropy threshold on the globally pooled rank-abundance distribution, about 0.019% of pooled relative abundance, with prevalence across samples reported separately.
  conf: not stated · class: not stated · holds: 844 global soils · src: bickelChosenFewVariations2021 (FT) · trail: MB-02 §D2.3, §answers · from: MB-02:B-0184, MB-02:B-0185, MB-02:A-065
- **regional-terms.3** Reviews treat habitat specificity and geographic range as microbial rarity axes alongside local abundance.
  conf: not stated · class: not stated · holds: reviews · src: joussetWhereLessMay2017 (FT) · trail: MB-02 §D2.3 · from: MB-02:B-0186
- **regional-terms.4** Terms are used inconsistently: "dominant" sometimes means abundant within a sample and sometimes abundant and ubiquitous, and "common" means high pooled abundance in one study and high occupancy elsewhere.
  conf: not stated · class: not stated · holds: microbial ecology literature · src: delgadobaquerizoGlobalAtlasDominant2018, bickelChosenFewVariations2021 · trail: MB-02 §answers · from: MB-02:A-074

### ecology-frameworks: rarity and occupancy frameworks from general ecology
needs: rarity-terms, core-microbiome
- **ecology-frameworks.1** Rabinowitz (1981) classifies rarity by geographic range, habitat specificity and local abundance; its microbial users state these concepts "can be easily transferred to microbial communities".
  conf: not stated · class: not stated · holds: general ecology; known only secondarily · src: rabinowitzSevenFormsRarity1981 (SEC), joussetWhereLessMay2017 · trail: MB-02 §D2.4, §answers · limit: access (note: "The original was not obtained") · from: MB-02:B-0187, MB-02:B-0188, MB-02:B-0189, MB-02:A-066
- **ecology-frameworks.2** In a 21-year estuarine fish record, persistent and abundant "core" species fitted a lognormal, while infrequent "occasional" species fitted a log series.
  conf: not stated · class: not stated · holds: estuarine fish · src: magurranExplainingExcessRare2003 (AB) · trail: MB-02 §D2.4, §answers · from: MB-02:B-0190, MB-02:A-066
- **ecology-frameworks.3** The same split is reported for rare against abundant Arctic Ocean prokaryotes: log series against lognormal.
  conf: not stated · class: not stated · holds: Arctic Ocean prokaryotes · src: galandEcologyRareMicrobial2009 (FT) · trail: MB-02 §D2.4 · from: MB-02:B-0191
- **ecology-frameworks.4** Positive intraspecific and interspecific abundance-occupancy relationships are general in the British flora and fauna; in general macroecology positive relationships are common and multiple explanations have been tested.
  conf: not stated · class: not stated · holds: British flora and fauna; general macroecology · src: gastonAbundanceoccupancyRelationships2000 (AB) · trail: MB-02 §D2.4, §D3.3, §answers · from: MB-02:B-0192, MB-02:B-0279, MB-02:A-066, MB-02:A-113

### threshold-sensitivity: whether classifications and conclusions hold across thresholds
needs: rarity-terms, core-microbiome
- **threshold-sensitivity.1** In a salt-marsh soil chronosequence (Schiermonnikoog, five stages over 110 years, amplicon ASVs), the rare fraction of reads was 61.6%, 45.7% and 28.4% at cutoffs of 0.2%, 0.1% and 0.05%.
  conf: not stated · class: not stated · holds: one salt-marsh chronosequence · src: jiaUnravellingInterplayEcological2022 (FT) · trail: MB-02 §D2.5, §answers · from: MB-02:B-0193, MB-02:B-0194, MB-02:B-0195, MB-02:A-067, MB-02:A-084
- **threshold-sensitivity.2** As the cutoff tightened, permanently and transiently rare ASVs fell in proportion, conditionally rare ASVs rose, and the relative importance of selection rose, while beta-diversity patterns and the main assembly inference (homogeneous selection for the rare biosphere, variable selection for the common) were reported as similar across cutoffs: classification changed, the qualitative conclusion held; this is the only soil test of threshold sensitivity found.
  conf: single (critic: MB-02:C-037) · class: not stated · holds: one soil test · src: jiaUnravellingInterplayEcological2022 (FT) · trail: MB-02 §D2.5, §answers, §critic · from: MB-02:B-0196, MB-02:B-0197, MB-02:B-0198, MB-02:A-067, MB-02:A-080, MB-02:C-037, MB-02:B-0300
- **threshold-sensitivity.3** In Arctic Ocean data, the biogeography of rare taxa persisted at a 0.001% cutoff.
  conf: not stated · class: not stated · holds: Arctic Ocean · src: galandEcologyRareMicrobial2009 (FT) · trail: MB-02 §D2.5, §answers · from: MB-02:B-0199, MB-02:A-067
- **threshold-sensitivity.4** In coastal sand data, ecological patterns were maintained after removing up to 35 to 40% of rare sequences.
  conf: not stated · class: not stated · holds: coastal sands · src: gobetMultivariateCutoffLevel2010 (AB) · trail: MB-02 §D2.5, §answers · from: MB-02:B-0200, MB-02:A-067
- **threshold-sensitivity.5** In marine samples, the 0.1% per-sample rule gave more rare than abundant ASVs with V4V5 amplicons and the reverse with full-length 16S, and threshold-based classes behaved differently across OTUs, ASVs and metagenomic OTUs, while the unsupervised method gave the same pattern across these.
  conf: not stated · class: not stated · holds: marine samples · src: pascoalDefinitionMicrobialRare2025 (FT) · trail: MB-02 §D2.5, §answers · from: MB-02:B-0201, MB-02:B-0202, MB-02:B-0203, MB-02:A-067
- **threshold-sensitivity.6** Four core methods compared on human faecal (319 samples) and Arabidopsis root (288 samples) data assigned 1.2% to 9.4% of taxa as core, nearly 10-fold apart; 165 to 176 taxa were agreed by all four, which is 13 to 16% of core assignments.
  conf: not stated · class: not stated · holds: human faecal and Arabidopsis root data · src: custerComparativeAnalysisCore2023 (FT, first 100,000 characters) · trail: MB-02 §D2.5, §answers, §critic, §Adversarial · from: MB-02:B-0204, MB-02:B-0205, MB-02:B-0206, MB-02:A-067, MB-02:C-033, MB-02:C-081
- **threshold-sensitivity.7** In the human data, a temporal effect significant in the full dataset was reported as not significant in core-based analyses, but the source's text is internally inconsistent on whether core analyses gained or lost the temporal effect.
  conf: not stated · class: not stated · holds: human data · src: custerComparativeAnalysisCore2023 · trail: MB-02 §D2.5, §answers, §critic · from: MB-02:B-0207, MB-02:A-067, MB-02:C-035
- **threshold-sensitivity.8** Occupancy-based core methods were most accurate in simulations, in one simulation study.
  conf: single (critic: MB-02:C-092) · class: not stated · holds: simulations · src: custerComparativeAnalysisCore2023 · trail: MB-02 §D2.5, §answers, §Adversarial · from: MB-02:B-0208, MB-02:A-068, MB-02:C-092
- **threshold-sensitivity.9** In sponges, core definitions changed alpha and beta diversity in some cases but not conclusions on host specificity, environmental quality or networks, and the authors call the approach "surprisingly robust".
  conf: not stated · class: not stated · holds: sponges · src: astudillogarciaEvaluatingCoreMicrobiota2017 (AB) · trail: MB-02 §D2.5, §answers · from: MB-02:B-0209, MB-02:B-0210, MB-02:A-067
- **threshold-sensitivity.10** In human gut, core size depended mostly on analysis depth and required prevalence.
  conf: not stated · class: not stated · holds: human gut · src: salonenAdultIntestinalCore2012 (AB) · trail: MB-02 §D2.5, §answers · from: MB-02:B-0211, MB-02:A-067
- **threshold-sensitivity.11** On Loess Plateau soils, two primer pairs gave different diversity responses to land use, so rare and abundant classes depend on the primer, not only the cutoff.
  conf: not stated · class: not stated · holds: Loess Plateau soils · src: zengIdentifyingBiogeographicPatterns2021 (AB) · trail: MB-02 §D2.5 · from: MB-02:B-0212
- **threshold-sensitivity.12** Tests of threshold sensitivity point both ways and are each single-system: some report conclusions that hold across thresholds or definitions, others classifications or conclusions that change; these are not strictly contradictory because they test different outputs (membership counts against beta-diversity or assembly inferences).
  conf: single (critic: MB-02:C-036) · class: not stated · holds: one system per test · src: galandEcologyRareMicrobial2009, gobetMultivariateCutoffLevel2010, jiaUnravellingInterplayEcological2022, astudillogarciaEvaluatingCoreMicrobiota2017, pascoalDefinitionMicrobialRare2025, custerComparativeAnalysisCore2023, salonenAdultIntestinalCore2012 · trail: MB-02 §answers, §critic · rating: "Moderate on threshold sensitivity" · from: MB-02:A-071, MB-02:A-072, MB-02:A-073, MB-02:A-146, MB-02:C-036
- **threshold-sensitivity.13** Proposed standards include unsupervised clustering (ulrb), multivariate cutoff analysis (also recommended for rare-biosphere assembly work), abundance-occupancy ranking with a neutral-model fit to prioritise core members, and explicit reporting with explicit spatial and temporal scale of the core, deep sequencing and no rarefying when quantifying the core; no proposed standard was found to be widely adopted.
  conf: not stated · class: not stated · holds: proposals · src: pascoalDefinitionMicrobialRare2025, gobetMultivariateCutoffLevel2010, jiaCommunityAssemblyProcesses2018 (AB), shadeAbundanceoccupancyDistributionsPrioritize2019 (AB), neuDefiningQuantifyingCore2021 · trail: MB-02 §D2.5, §answers · from: MB-02:B-0213, MB-02:B-0214, MB-02:B-0215, MB-02:B-0216, MB-02:B-0217, MB-02:B-0218, MB-02:A-068, MB-02:A-069, MB-02:A-147

### abundance-occupancy: local abundance and occupancy across soils
needs: abundance-distribution, core-microbiome, regional-terms, count-sampling
- **abundance-occupancy.1** In 88 North and South American soils (about 1,500 reads per soil), the ten most abundant OTUs per sample occurred on average in 28% of soils, against 2% for all OTUs; in 27 tropical forest soils within one hectare, the figures were 69% against 8%; these figures could not be verified, and the source's abstract frames the study across Earth's major habitat types, not soils alone.
  conf: not stated · class: not stated · holds: bulk soil · src: nemergutGlobalPatternsBiogeography2011 (FT) · trail: MB-02 §D3.2, §answers, §critic, §Adversarial · limit: access (critic: MB-02:C-084) · from: MB-02:B-0246, MB-02:B-0247, MB-02:B-0248, MB-02:A-101, MB-02:C-066, MB-02:C-067, MB-02:C-082, MB-02:C-083, MB-02:C-084, MB-02:C-085, MB-02:A-123
- **abundance-occupancy.2** Total abundance and the number of soils occupied were significantly and positively related, with no coefficient given; summed abundance rises with occupancy, so the measure is partly built in by construction.
  conf: not stated · class: not stated · holds: bulk soil · src: nemergutGlobalPatternsBiogeography2011 (FT) · trail: MB-02 §D3.2, §answers, §critic, §Adversarial · from: MB-02:B-0249, MB-02:A-101, MB-02:C-050, MB-02:C-125
- **abundance-occupancy.3** The authors note that abundant taxa may simply be easier to detect, and that undersampling could hide intermediate distributions.
  conf: not stated · class: not stated · holds: bulk soil · src: nemergutGlobalPatternsBiogeography2011 · trail: MB-02 §D3.2, §answers · from: MB-02:B-0250, MB-02:A-107
- **abundance-occupancy.4** Across 844 global soils, median prevalence was 0.3 for common taxa and 0.001 for rare taxa; this is a class-level contrast in which the common class is defined on the globally pooled rank-abundance distribution, and pooled abundance rises mechanically with prevalence, so it is a different measure from a taxon-level abundance-occupancy relationship.
  conf: not stated · class: not stated · holds: 844 global soils · src: bickelChosenFewVariations2021 (FT) · trail: MB-02 §D3.2, §answers, §critic, §Adversarial · from: MB-02:B-0251, MB-02:B-0252, MB-02:A-102, MB-02:C-050, MB-02:C-124, MB-02:C-137
- **abundance-occupancy.5** Across about 124,000 taxa in 3.41 km2 of urban park soil, occupancy correlated strongly with environmental range; abundance was not the axis tested.
  conf: not stated · class: not stated · holds: urban park soil · src: barberanWhyAreMicrobes2014 (AB) · trail: MB-02 §D3.2, §answers · from: MB-02:B-0253, MB-02:B-0254, MB-02:A-103
- **abundance-occupancy.6** A global list of dominant soil taxa cannot serve as an independent test of the abundance-occupancy relationship, because dominance there is defined by abundance and ubiquity together.
  conf: not stated · class: not stated · holds: 237 soils · src: delgadobaquerizoGlobalAtlasDominant2018 (FT) · trail: MB-02 §D3.2, §answers · from: MB-02:B-0255, MB-02:A-104
- **abundance-occupancy.7** Soil also holds taxa that are abundant at some times or places and rare elsewhere: 2,197 conditionally rare ASVs alongside 11,838 permanently rare and 8,333 transiently rare ASVs in a soil chronosequence; such taxa cut against a uniform abundance-occupancy relationship.
  conf: not stated · class: not stated · holds: one soil chronosequence · src: jiaUnravellingInterplayEcological2022 (FT), shadeConditionallyRareTaxa2014 · trail: MB-02 §D3.2, §answers · from: MB-02:B-0256, MB-02:A-105, MB-02:A-120
- **abundance-occupancy.8** In the two bulk-soil amplicon studies with figures, more abundant taxa occupy more soils, but the two are not fully independent (one reanalysed compiled datasets including the Earth Microbiome Project, which plausibly overlaps the other's soils), both measures are partly built in by construction, detection limits and neutral or sampling models predict a positive relationship without selection, and no soil test against a sampling null was found; whether a relationship exists beyond sampling, and how strong it is, is unresolved.
  conf: unclear (critic: MB-02:C-053) · class: not stated · holds: bulk soil, amplicon data; the sampling-null evidence is non-soil · src: nemergutGlobalPatternsBiogeography2011, bickelChosenFewVariations2021 · trail: MB-02 §critic, §answers, §Adversarial · rating: "Moderate for the existence of a positive relationship in amplicon data from bulk soil" (critic: MB-02:C-053: unresolved beyond sampling) · contrary: one-sided (critic: MB-02:C-126) · from: MB-02:C-048, MB-02:C-049, MB-02:C-050, MB-02:C-051, MB-02:C-052, MB-02:C-053, MB-02:C-126, MB-02:C-144, MB-02:C-145, MB-02:A-115, MB-02:A-116, MB-02:A-153
- **abundance-occupancy.9** In common bean rhizospheres across four US regions plus a Colombian dataset, 48 bacterial and archaeal taxa were detected in every sample, and fitting a neutral model to the abundance-occupancy distribution, 13.7% of bacterial and archaeal taxa deviated from neutral expectation; samples were rarefied to 31,255 reads, and this rhizosphere figure rests on one study.
  conf: not stated · class: not stated · holds: common bean rhizosphere · src: stopnisekPersistentMicrobiomeMembers2021 (FT) · trail: MB-02 §D3.2, §answers, §critic · from: MB-02:B-0257, MB-02:B-0258, MB-02:B-0259, MB-02:B-0260, MB-02:A-106, MB-02:A-125, MB-02:A-152, MB-02:C-054
- **abundance-occupancy.10** In 4,866 maize rhizosphere samples, seven OTUs were present in all, five of them responsive to host genotype.
  conf: not stated · class: not stated · holds: maize rhizosphere · src: waltersLargescaleReplicatedField2018 (AB) · trail: MB-02 §D3.2, §answers · from: MB-02:B-0261, MB-02:A-106
- **abundance-occupancy.11** In Arabidopsis root data, core size varied 7-fold among methods.
  conf: not stated · class: not stated · holds: Arabidopsis root data · src: custerComparativeAnalysisCore2023 (FT) · trail: MB-02 §D3.2, §answers · from: MB-02:B-0262, MB-02:A-106
- **abundance-occupancy.12** Rhizosphere evidence is limited to core-membership studies of two to three crops, none of which reports an abundance-occupancy correlation coefficient in the passages read; no systematic search for every crop rhizosphere core study was run.
  conf: not stated · class: search (note: "I did not run a systematic search for every crop rhizosphere core study") · holds: rhizosphere · src: stopnisekPersistentMicrobiomeMembers2021, waltersLargescaleReplicatedField2018 · trail: MB-02 §D3.2, §answers, §critic, §Search record · search: not searched (note: "I did not run a systematic search for every crop rhizosphere core study") · from: MB-02:B-0263, MB-02:A-117, MB-02:C-055, MB-02:B-0301
- **abundance-occupancy.13** In the reviewer's argument, low-abundance taxa are often recorded absent when present, which by itself would produce lower occupancy for rarer taxa; the one source behind it (454 pyrosequencing, 24 communities from one Oklahoma warming site) attributes low replicate overlap to random sampling but does not draw the occupancy conclusion.
  conf: not stated · class: reading (critic: MB-02:C-139) · holds: one 454-era study at one site · src: zhouReproducibilityQuantitationAmplicon2011 (AB) · trail: MB-02 §D3.3, §answers, §Adversarial, §critic · from: MB-02:B-0264, MB-02:B-0266, MB-02:A-108, MB-02:C-051, MB-02:C-086, MB-02:C-139
- **abundance-occupancy.14** Pyrosequencing errors inflated rare-tail richness.
  conf: not stated · class: not stated · holds: pyrosequencing · src: kuninWrinklesRareBiosphere2010 (AB) · trail: MB-02 §D3.3, §answers · from: MB-02:B-0267, MB-02:A-110
- **abundance-occupancy.15** Better clustering cut richness by 30 to 60% but did not remove the long tail.
  conf: not stated · class: not stated · holds: one study · src: huseIroningOutWrinkles2010 (AB) · trail: MB-02 §D3.3, §answers · from: MB-02:B-0268, MB-02:A-110
- **abundance-occupancy.16** A global common-rare threshold was robust to using a quarter of the samples.
  conf: not stated · class: not stated · holds: 844 global soils · src: bickelChosenFewVariations2021 (FT) · trail: MB-02 §D3.3, §answers · from: MB-02:B-0272, MB-02:A-111
- **abundance-occupancy.17** A neutral community model with immigration and drift only predicts that abundant taxa occur in more samples, so a positive abundance-occupancy relationship is expected without selection, and its use in the common bean study treats deviations, not the relationship itself, as signal.
  conf: not stated · class: not stated · holds: neutral community model · src: sloanQuantifyingRolesImmigration2006 (AB), stopnisekPersistentMicrobiomeMembers2021 · trail: MB-02 §D3.3, §answers · from: MB-02:B-0273, MB-02:B-0274, MB-02:B-0275, MB-02:A-112
- **abundance-occupancy.18** The same positive relationship is read as ecological signal by some authors and as near-null by others; the reviewer notes this is a difference of interpretation, not of data.
  conf: not stated · class: reading (note: "the reviewer notes this is a difference of interpretation, not of data") · holds: abundance-occupancy studies · src: sloanQuantifyingRolesImmigration2006 · trail: MB-02 §answers · from: MB-02:A-119
- **abundance-occupancy.19** Neutral-model fits in soil exist as many single studies, which were not pooled.
  conf: not stated · class: not stated · holds: soil · src: none (the review's search record) · trail: MB-02 §Provenance, §Search record · from: MB-02:B-0010, MB-02:B-0302
- **abundance-occupancy.20** No soil study was found that tests whether the observed bulk-soil abundance-occupancy relationship exceeds what sampling and detection alone would produce; explicit sampling or occupancy-detection models applied to soil microbes were not searched beyond a neutral-model query.
  conf: not stated · class: search (critic: MB-02:C-119) · holds: bulk soil; a Europe PMC query for abundance-occupancy with soil or rhizosphere (25 hits reviewed by title) and a neutral-model query · src: none (a search result) · trail: MB-02 §D3.3, §answers, §Search record, §Adversarial · search: not searched (critic: MB-02:C-119) · from: MB-02:B-0281, MB-02:A-114, MB-02:B-0299, MB-02:C-119, MB-02:C-121
- **abundance-occupancy.21** None found: abundance-occupancy relationships in soil from cell counts or from metagenomes, copy-number- or ploidy-corrected soil relationships, archaea-specific relationships in soil, or bulk soil and rhizosphere compared within one study.
  conf: not stated · class: search (note: "none found") · holds: soil · src: none (a search result) · trail: MB-02 §D3.3, §answers · search: searched, not found (note: "none found") · from: MB-02:B-0282, MB-02:A-121

## Do not say
- **dns.1** "In 2018, 30% of 16S amplicon studies reported a negative control and 10% a positive control."
  why: The survey covered 265 papers in two journals that used any high-throughput community sequencing (16S, shotgun, metatranscriptomics, ITS, 18S and others), so it is not a 16S-only figure, and it is a single source. · instead: workflow.14 · trail: MB-01 §critic, §Adversarial · from: MB-01:C-004, MB-01:C-005, MB-01:C-132, MB-01:A-017
- **dns.2** "No source was found on how water sampling or host-tissue sampling choices affect composition."
  why: On the review's own Search record no angle searched water or host-tissue sampling choices, so they are unsearched, not "not found"; the review's section 2.1 says the opposite. · instead: workflow.16 · trail: MB-01 §critic, §2.1 · from: MB-01:C-006, MB-01:C-007, MB-01:C-008, MB-01:B-0087, MB-01:A-027
- **dns.3** "Departures from community composition were found at every step of the workflow."
  why: Field sampling for water and host tissue was not searched, and several choices showed no detectable effect, so departures were measured at most steps examined, not at every step. · instead: departure.3 · trail: MB-01 §critic, §Adversarial, §answers · from: MB-01:A-034, MB-01:A-111, MB-01:A-296, MB-01:C-062, MB-01:C-147, MB-01:C-148, MB-01:C-149
- **dns.4** "DNA extraction is the largest source of relative-abundance error, followed by PCR and then sequencing."
  why: The ordering rests on one 7-taxon vaginal dataset (Brooks 2015, reanalysed by McLaren 2019), is contested by Fouhy 2016 and qualified by MBQC, and should be presented as a single dataset, not as a field-wide ordering. · instead: dominant-steps.1 · trail: MB-01 §critic, §Adversarial, §1. Overview · from: MB-01:C-015, MB-01:C-016, MB-01:C-017, MB-01:C-084, MB-01:B-0035, MB-01:A-297
- **dns.5** "Many independent mock studies agree on which steps dominate the error, so the ordering is strongly supported."
  why: The review's own sensitivity note says the ordering rests on McLaren and Brooks, and a "strong" rating is firmer than the access and source base (one re-analysed 454 dataset) allow. · instead: dominant-steps.1 · trail: MB-01 §Adversarial, §answers · from: MB-01:A-111, MB-01:A-112, MB-01:C-061, MB-01:C-083
- **dns.6** "Calibration cut mean Bray-Curtis error from 0.35 to 0.08 in a shotgun dataset."
  why: That calibration result comes from the Brooks et al. 2015 16S cell mixtures; the shotgun calibration is reported only qualitatively. · instead: bias-consistency.2 · trail: MB-01 §2.14, §critic, §Adversarial · from: MB-01:B-0184, MB-01:C-021, MB-01:C-055, MB-01:C-066, MB-01:C-067, MB-01:C-068
- **dns.7** "The original 515F/806R V4 primers under-represented SAR11 about 4 to 10-fold in field samples, against about 2-fold in mocks."
  why: The abstract gives these SAR11 figures for 515F-Y/806R, not for the original 515F-C/806R pair. · instead: primers.2 · trail: MB-01 §2.3, §critic, §Adversarial · from: MB-01:I-0018, MB-01:A-052, MB-01:C-056, MB-01:C-070
- **dns.8** "Bias measured on mock communities does not transfer to field samples."
  why: This rests on one abstract-only study (Parada 2016), for one primer pair (515F-Y/806R) and one taxon (SAR11). · instead: primers.2, bias-consistency.8 · trail: MB-01 §Adversarial · from: MB-01:B-0059, MB-01:C-092
- **dns.9** "ddPCR and flow cytometry correlated at only r = 0.50 on faeces."
  why: The full text reports qPCR against flow-cytometry enumeration on faeces (Pearson r = -0.50), and ddPCR correlated strongly with qPCR. · instead: absolute-quantification.12 · trail: MB-01 §5.5, §critic, §Adversarial · from: MB-01:I-0140, MB-01:C-045, MB-01:C-057, MB-01:C-071
- **dns.10** "Unfiltered OTU tables were 50 to 80% spurious taxa."
  why: The source says the 50 to 80% figure applies after OTU clustering and singleton removal, not to unfiltered tables. · instead: denoising-clustering.8 · trail: MB-01 §2.10, §critic, §Adversarial · from: MB-01:I-0056, MB-01:A-095, MB-01:B-0075, MB-01:C-058, MB-01:C-072
- **dns.11** "PCR replicates of negative controls had a mean Jaccard of 0.80."
  why: The source reports a mean Jaccard distance of 0.80 (range 0.65 to 0.87); without the word "distance" the figure reads as high similarity. · instead: technical-variation.2 · trail: MB-01 §4.3, §critic, §Adversarial · from: MB-01:I-0100, MB-01:C-059, MB-01:C-082
- **dns.12** "Several soil studies show that multinomial or Poisson sampling explains much of the replicate disagreement in taxa detected."
  why: The studies are one 454 dataset of 24 Oklahoma soils (reported and then modelled) and one laboratory, whose MiSeq replicates do not fit the model, so it is weak and contested that sampling alone explains replicate disagreement. · instead: count-sampling.6 · trail: MB-01 §critic, §Adversarial, §answers · from: MB-01:A-187, MB-01:A-214, MB-01:A-306, MB-01:C-036, MB-01:C-063, MB-01:C-086, MB-01:C-135
- **dns.13** "Agreement in relative abundance between technical replicates rises with depth, roughly as a square root."
  why: This rests on one caecal extract with four technical replicates (Barlow 2020), a single source. · instead: count-sampling.7 · trail: MB-01 §8. Answers, §critic, §Adversarial · from: MB-01:A-307, MB-01:C-037, MB-01:C-085
- **dns.14** "Relative abundance is robust to the pipeline; counts of taxa are not."
  why: It generalises from Nearing 2018 (with Marizzoni 2020); Nearing 2018 itself reports that all pipelines "markedly differed" from expected composition on the Zymo mock, and Straub 2020 reports pipeline-dependent interpretations. · instead: denoising-clustering.1, denoising-clustering.4 · trail: MB-01 §2.10, §Adversarial · from: MB-01:I-0052, MB-01:C-087
- **dns.15** "Library preparation and primers are the largest drivers of the error profile."
  why: This rests on Schirmer 2015 alone, and the review's table gives it no single-source flag. · instead: library-sequencing.1 · trail: MB-01 §Adversarial · from: MB-01:B-0071, MB-01:A-077, MB-01:C-088
- **dns.16** "V4 genus accuracy is about 50% at 97% identity, and reference databases carry about 10 to 17% annotation error."
  why: Both figures rest on Edgar 2018b and 2018c, from one author who also develops competing classifiers; the review flags them as single in its text but uses them in its answer without that qualifier. · instead: taxonomy.1, taxonomy.6 · trail: MB-01 §answers, §Adversarial · from: MB-01:A-097, MB-01:A-098, MB-01:C-089
- **dns.17** "Chimera formation is reproducible across amplifications."
  why: This rests on Haas 2011 alone, with Sanger and 454 data. · instead: chimeras.1 · trail: MB-01 §answers, §Adversarial · from: MB-01:A-075, MB-01:C-090
- **dns.18** "Fast-responding soil isolates averaged 5.5 16S copies against 1.4 for slow responders."
  why: Stated as a general finding, it rests on one abstract-only study (Klappenbach 2000). · instead: copy-number.26 · trail: MB-01 §answers, §Adversarial · from: MB-01:A-145, MB-01:C-091
- **dns.19** "The case against rarefying for richness is only an assertion, against modelled simulations in favour of rarefying."
  why: Willis 2019 presents statistical argument plus a worked simulated example; classing it as an assertion against Schloss's modelled simulations understates the evidence against rarefying for richness and applies the evidence class unevenly. · instead: richness.12 · trail: MB-01 §critic, §Adversarial, §answers · from: MB-01:A-233, MB-01:A-275, MB-01:C-043, MB-01:C-044, MB-01:C-064, MB-01:C-124, MB-01:C-125, MB-01:C-126
- **dns.20** "Spike-in totals agreed poorly with flow cytometry (r2 = 0.19), so the internal standards failed."
  why: The review reports only the r2 before correction and omits the authors' conclusion that the internal-standard method is quantitative and consistent with flow cytometry; the r2 figure could not be verified. · instead: absolute-quantification.14 · trail: MB-01 §critic, §Adversarial, §answers · from: MB-01:A-269, MB-01:B-0363, MB-01:C-046, MB-01:C-047, MB-01:C-048, MB-01:C-081, MB-01:C-127
- **dns.21** "In 24 grassland soils, the best-fitting abundance distributions were exponential or inverse gamma."
  why: The best fits are in Zhou 2013's supplementary Table S3; the main text does not state which distributions won, and they were not verified. · instead: abundance-distribution.1 · trail: MB-01 §3.4, §critic, §Adversarial · from: MB-01:I-0085, MB-01:A-162, MB-01:C-026, MB-01:C-077, MB-01:C-078, MB-01:C-079
- **dns.22** "Water and host-associated communities fit a lognormal abundance distribution better."
  why: The "water and hosts" item is a single study (Kembel 2012) that pools ocean and skin into one item, and the same paper's simulations assumed a lognormal, so the separate water and host cases were not answered. · instead: abundance-distribution.3 · trail: MB-01 §critic, §Adversarial · from: MB-01:A-164, MB-01:B-0226, MB-01:C-027, MB-01:C-134
- **dns.23** "Water communities carry about 2.2 16S copies per genome."
  why: The EMP's value of about 2.2 pools free-living (soil, water and sediment) and plant-associated samples, so it is not a value for water. · instead: community-copy-number.5 · trail: MB-01 §Adversarial, §answers · from: MB-01:A-150, MB-01:B-0208, MB-01:C-136
- **dns.24** "Index misassignment moves 0.1 to 6% of 16S reads between samples."
  why: The range merges non-16S genome and exome libraries, Illumina's own documentation, non-16S amplicons and 16S data, without indirect labels. · instead: index-misassignment.2, index-misassignment.5, index-misassignment.11 · trail: MB-01 §Adversarial · from: MB-01:B-0072, MB-01:C-133
- **dns.25** "Extraction bias is consistent across samples on the ratio scale, in cell mixtures and in a shotgun spike-in alike."
  why: A 16S cell-mixture result and a shotgun spike-in result known only secondarily are combined into one finding, mixing measurement types. · instead: bias-consistency.1, bias-consistency.3 · trail: MB-01 §Adversarial · from: MB-01:B-0056, MB-01:A-048, MB-01:A-049, MB-01:C-137
- **dns.26** "Whether the departure is consistent across samples determines whether a fixed correction can work."
  why: That is the reviewer's framing of what matters for analysis design, not a literature finding. · instead: none · trail: MB-01 §2.14, §Adversarial · from: MB-01:B-0181, MB-01:C-138
- **dns.27** "The difference in load is the likely reason pooled and single PCR results disagree."
  why: This is the reviewer's own reconciliation, presented in the answer; no single study tested both conditions, and it is not marked as the reviewer's reading. · instead: pcr.19 · trail: MB-01 §answers, §Adversarial · from: MB-01:A-221, MB-01:C-139, MB-01:C-140, MB-01:C-141
- **dns.28** "Simulations disagree mainly because they build different data-generating processes into the truth."
  why: This is only partly supported (Weiss 2017, Hong 2022 and Schloss 2024a each say results depend on data-generating assumptions) and is phrased as the review's own causal diagnosis. · instead: rarefying.11 · trail: MB-01 §1. Overview, §Adversarial · from: MB-01:B-0042, MB-01:C-142
- **dns.29** "The review's summary table shows which approaches are shown to correct for unequal depth or load."
  why: Its "Shown to correct" cells mix makers' claims and simulation results with measured results without a per-cell evidence class, so it reads closer to a method recommendation than the brief allows. · instead: rarefying.9, scaling-normalisation.8, compositional-data.2, differential-abundance.19, absolute-quantification.17, richness.10, richness.26 · trail: MB-01 §5.6, §Adversarial · from: MB-01:B-0320, MB-01:C-143
- **dns.30** "UNBIAS's pessimistic result is a single-source contrary result, set against the established good fits of calibration."
  why: The pro-correction results it conflicts with (McLaren, Silverman) each also rest on a single mock design and get no matching single-source label at that point. · instead: copy-number-correction.14, bias-consistency.2, pcr.8 · trail: MB-01 §2.14, §Adversarial · from: MB-01:B-0192, MB-01:B-0193, MB-01:C-131
- **dns.31** "Bias is consistent across samples on the ratio scale, and field evidence of inconsistency only limits this."
  why: The ratio-scale result comes from 7 taxa mixed as cells and reanalysed, while field evidence of inconsistency (abstract only, one primer pair) is weighed as limiting; neither side's small-n and access limits are stated symmetrically. · instead: bias-consistency.1, bias-consistency.6 · trail: MB-01 §answers, §Adversarial · from: MB-01:A-108, MB-01:A-114, MB-01:C-128, MB-01:C-129, MB-01:C-130
- **dns.32** "Sampling explains replicate variation, and the 76% of technical variance beyond counting comes from a different setting and measure."
  why: The "different setting and measure" caution is applied to Silverman 2018 but not to the sampling side, whose own contrary evidence in Wen 2017 (an overlap plateau, biases other than random sampling, a run effect) is left out. · instead: count-sampling.5, count-sampling.10, technical-variation.1 · trail: MB-01 §answers, §Adversarial · from: MB-01:A-218, MB-01:C-120, MB-01:C-121, MB-01:C-122, MB-01:C-123
- **dns.33** "Total 16S qPCR multiplied by relative abundance agrees near-perfectly with taxon-specific qPCR, which validates absolute quantification."
  why: The near-perfect correlation is a comparison of methods that share an upstream (qPCR against qPCR-anchored sequencing), so it is not independent agreement. · instead: absolute-quantification.8 · trail: MB-01 §5.5, §Adversarial · from: MB-01:I-0139, MB-01:C-127
- **dns.34** "The figures from Zhou 2011, Kozich 2013, Haegeman 2013 and Lin 2019 were read in full text."
  why: Their full-text labels could not be confirmed as open full text by Europe PMC or PMC; the quoted figures for Zhou 2011 match its abstract and should be labelled abstract-derived, and figures needing the body could not be confirmed. · instead: none · trail: MB-01 §critic, §Adversarial · from: MB-01:C-065, MB-01:C-073, MB-01:C-074, MB-01:C-075, MB-01:C-076
- **dns.35** "Archaea carry 1 to 4 copies of the 16S rRNA gene."
  why: Stated as the whole record, it misses Acinas et al. 2004, which already reports a maximum of five archaeal operons; the review's own sources conflict on the archaeal maximum. · instead: copy-number.2 · trail: MB-02 §critic, §Adversarial · from: MB-02:A-002, MB-02:C-002, MB-02:C-138
- **dns.36** "Acidobacteria average 1.0 16S copies per genome."
  why: Presented beside large-n phyla without its n, the mean rests on 4 genomes from 4 species, and the soil correction example depends on it. · instead: copy-number.8, copy-number.10 · trail: MB-02 §critic, §Adversarial · from: MB-02:A-004, MB-02:C-003, MB-02:C-005, MB-02:C-089
- **dns.37** "The 1 to 15 range of 16S copies per genome is replicated across independent sources."
  why: The range is consistent across sources, but those sources draw on overlapping NCBI genome sets, so they are not independent replications. · instead: copy-number.1 · trail: MB-02 §critic · from: MB-02:A-009, MB-02:C-006
- **dns.38** "Bacterial genomes carry up to 21 or 22 copies of the 16S rRNA gene."
  why: The current maxima are the reviewer's own derivation from rrnDB, with no published check against assembly quality, and the answer leads with them over published values. · instead: copy-number.3 · trail: MB-02 §critic, §Adversarial · from: MB-02:A-001, MB-02:C-007, MB-02:C-141
- **dns.39** "Genome copies per cell usually fall in stationary phase or starvation."
  why: Phrased as a property of prokaryotes, it rests largely on one laboratory's abstracts and folds taxon-specific and sometimes opposite behaviours into one trend; A. vinelandii and M. acetivorans carry more chromosomes in stationary than in exponential phase. · instead: ploidy.18, ploidy.17 · trail: MB-02 §critic, §Adversarial · from: MB-02:A-135, MB-02:C-009, MB-02:C-010, MB-02:C-011, MB-02:C-073, MB-02:C-087, MB-02:C-136
- **dns.40** "Evidence on genome copies per cell is strong for cultures."
  why: Apart from Pecoraro 2011 all ploidy studies were read at abstract level, and the evidence rests largely on one laboratory's qPCR method, so it is moderate, not strong. · instead: ploidy.1, ploidy.2 · trail: MB-02 §critic, §Adversarial · from: MB-02:A-028, MB-02:A-136, MB-02:C-014, MB-02:C-068
- **dns.41** "No direct contradiction of the culture ploidy values was found, and no independent-laboratory measurements were located."
  why: Pecoraro 2011, read in full, lists in its Table 5 A. vinelandii polyploidy (40 copies in fast growth) and several measurements from other laboratories, and Bruck 2023 reports A. vinelandii rising from 4 to 80 copies. · instead: ploidy.2, ploidy.17 · trail: MB-02 §critic, §Adversarial · from: MB-02:A-031, MB-02:B-0109, MB-02:C-063, MB-02:C-064, MB-02:C-075, MB-02:C-130
- **dns.42** "16S copies per cell scale with origin number more than with genome number."
  why: It is the reviewer's inference from one abstract (Couturier and Rocha 2006), presented without a reviewer's-reading label; no source in the review measures 16S copies per cell against origin number. · instead: ploidy.20 · trail: MB-02 §critic, §Adversarial · from: MB-02:A-025, MB-02:B-0111, MB-02:C-015, MB-02:C-088, MB-02:C-140
- **dns.43** "For no natural community has the share of cells with one genome copy versus more than one been reported by taxon."
  why: In situ flow-cytometric cell-cycle analyses of Prochlorococcus are by method taxon-specific measurements of the share of cells with replicated DNA; the review read only the abstract, so the statement is not established. · instead: ploidy.33 · trail: MB-02 §critic, §Adversarial · from: MB-02:A-027, MB-02:B-0129, MB-02:C-017, MB-02:C-018, MB-02:C-106, MB-02:C-107
- **dns.44** "The share of Prochlorococcus cells carrying two genomes changes over the day."
  why: The abstract gives no share; it states only that replication occurred in the afternoon and division at night, so the claim goes beyond the access. · instead: ploidy.29 · trail: MB-02 §D1.3, §Adversarial · from: MB-02:B-0123, MB-02:C-078, MB-02:C-079, MB-02:C-080
- **dns.45** "Eleven DNA-based mock communities fitted 7.1% better without copy-number correction."
  why: The 7.1% was computed on n = 10 mocks; one of the eleven was excluded. · instead: copy-number-correction.18 · trail: MB-02 §critic · from: MB-02:A-044, MB-02:C-022, MB-02:C-065
- **dns.46** "Other biases, such as extraction and primers, are of similar or larger size than copy-number bias and multiply with it."
  why: This rests on McLaren et al. 2019 read at abstract level, and the abstract does not compare their magnitude with copy-number bias. · instead: none · trail: MB-02 §critic, §Adversarial · from: MB-02:A-046, MB-02:C-025, MB-02:C-077, MB-02:C-090
- **dns.47** "Abundant taxa are those above 1% of reads, as in Jia et al. 2022."
  why: Jia et al. 2022 uses a single rare/common cutoff and does not support "abundant above 1%". · instead: rarity-terms.2 · trail: MB-02 §critic · from: MB-02:A-061, MB-02:C-032, MB-02:C-065
- **dns.48** "Only about 1% of taxa were agreed as core by all four methods."
  why: The source gives 165 and 176 taxa as 13% and 15.85% of core assignments; "about 1% of taxa" is the review's own derivation and should be labelled as such. · instead: threshold-sensitivity.6 · trail: MB-02 §critic, §Adversarial · from: MB-02:A-067, MB-02:B-0206, MB-02:C-033, MB-02:C-034, MB-02:C-081
- **dns.49** "In bulk soil, 0.4 to 2% of taxa hold about 41 to 58% of reads."
  why: The figures come from two datasets with different definitions and denominators (2% holding on average 41% of reads per sample under a joint abundance-and-ubiquity definition; 0.4% holding about 58% of pooled global relative abundance), and the body says they must not be combined. · instead: abundance-distribution.11, abundance-distribution.12, abundance-distribution.13 · trail: MB-02 §critic, §Adversarial · from: MB-02:A-148, MB-02:C-043, MB-02:C-060, MB-02:C-135
- **dns.50** "Two phylotypes dominate soil archaea."
  why: Stated as a general finding, it rests on one abstract-only study (Bates et al. 2011) of 2010-era 454 data from 146 soils. · instead: abundance-distribution.15 · trail: MB-02 §Adversarial · from: MB-02:A-148, MB-02:C-091
- **dns.51** "Bulk soil shows a positive abundance-occupancy relationship wherever it has been tested."
  why: "Wherever tested" rests on two partly overlapping datasets whose metrics are partly circular, after a search that reviewed about 25 titles, so it overstates the evidence. · instead: abundance-occupancy.8 · trail: MB-02 §critic, §Adversarial · from: MB-02:A-100, MB-02:A-151, MB-02:C-053, MB-02:C-061, MB-02:C-062, MB-02:C-127
- **dns.52** "Low-abundance taxa are routinely recorded absent where present, which by itself produces lower occupancy for rarer taxa."
  why: Presented as a finding of Zhou et al. 2011, it generalises from one 454 study of 24 communities at one Oklahoma site, and the occupancy conclusion is the reviewer's argument, which Zhou's abstract does not draw. · instead: abundance-occupancy.13 · trail: MB-02 §D3.3, §Adversarial · from: MB-02:B-0266, MB-02:C-086, MB-02:C-139
- **dns.53** "Occupancy-based core methods perform best, an established standard for defining the core."
  why: This rests on one simulation study (Custer et al. 2023) and is listed among proposed standards as if established. · instead: threshold-sensitivity.8 · trail: MB-02 §Adversarial · from: MB-02:A-068, MB-02:C-092
- **dns.54** "Up to 41% of rRNA genes in soil are unlinked."
  why: The soil figure rests on one abstract-only study (Brewer 2020); the body flags this, the answer does not. · instead: copy-number.22 · trail: MB-02 §Adversarial · from: MB-02:A-007, MB-02:C-093
- **dns.55** "Common taxa occur in far more soils than rare taxa, a further abundance-occupancy relationship."
  why: The common class is defined on the globally pooled rank-abundance distribution, pooled abundance rises mechanically with prevalence, and a class-level contrast of median prevalence is a different measure from a taxon-level relationship. · instead: abundance-occupancy.4 · trail: MB-02 §Adversarial · from: MB-02:A-102, MB-02:C-123, MB-02:C-124, MB-02:C-137

## Gaps
- **gap.1** Same-sample comparisons of 16S amplicon data with shotgun metagenomes and with culture-based, microscopy or FISH, or taxon-specific qPCR counts (beyond four taxa in one study) are missing; the only shotgun evidence is Costea 2017, known secondarily via McLaren.
  blocks: bias-consistency, absolute-quantification · origin: critic coverage gap: nearest precedents named in the brief are almost entirely missing (all environments) · search: not stated · from: MB-01:C-105, MB-01:C-106, MB-01:C-107
- **gap.2** Field sampling choices for water (volume filtered, filter pore size, prefiltration, filter storage) and for host tissue (swab, biopsy or lavage; plant tissue surface sterilisation); the review contradicts itself on whether these were searched: its section 2.1 says the lab angle searched preservation and storage terms through Crossref, Europe PMC and web search, while its Search record says no angle searched water-sampling or host-tissue sampling choices.
  blocks: sampling-storage, workflow.16 · origin: critic coverage gap; the note contradicts itself · search: not searched (critic: MB-01:C-108) · from: MB-01:C-108, MB-01:C-006, MB-01:C-007, MB-01:B-0088, MB-01:B-0018
- **gap.3** Long-read platform error and bias on mocks: Nanopore full-length 16S is absent, PacBio full-length evidence is only the developer's own claim, and there are no independent long-read mock benchmarks.
  blocks: library-sequencing · origin: critic coverage gap · search: not stated · from: MB-01:C-109
- **gap.4** 16S-specific index hopping on Illumina patterned flow cells (NovaSeq, NextSeq 2000): the only 16S rate is one preprint abstract.
  blocks: index-misassignment · origin: critic coverage gap; not found · search: searched, not found (note: "16S-specific index hopping on patterned flow cells (bioinformatics angle)") · from: MB-01:C-110, MB-01:B-0381
- **gap.5** Read counts per sample within a run after pooling, and the correlation of library size with biomass; two primary studies on this (101 fish species; an equivolumetric protocol) are known only through Schloss 2024b and were not opened.
  blocks: reads-per-sample, absolute-quantification · origin: critic coverage gap; not found · search: searched, not found (note: "all angles; web search found only forums") · from: MB-01:C-111, MB-01:B-0378
- **gap.6** Community-average 16S copy number measured from shotgun metagenomes (16S reads normalised to single-copy marker genes) in soil, water and host samples.
  blocks: community-copy-number · origin: critic coverage gap · search: not searched (critic: MB-01:C-112) · from: MB-01:C-112, MB-01:B-0380
- **gap.7** Absolute per-cycle amplification efficiency of universal 16S primers on soil, sediment, water and faecal extracts, from the qPCR methods literature (per-reaction efficiency from amplification curves, inhibition in environmental extracts).
  blocks: pcr · origin: critic coverage gap · search: not searched (critic: MB-01:C-113) · from: MB-01:C-113, MB-01:B-0379
- **gap.8** Abundance-distribution shapes by environment: Grilli 2020's per-biome supplementary figures and Shoemaker 2017's full text were not read, so per-environment shapes for water and host samples are absent although the sources exist.
  blocks: abundance-distribution · origin: critic coverage gap · search: not stated · from: MB-01:C-114
- **gap.9** Dirichlet-multinomial or other overdispersion fits to 16S technical replicates, and technical replicates across depths in aquatic, plant and human non-gut samples; replicate-at-depth studies are confined to one soil laboratory and one mouse caecum.
  blocks: overdispersion, replicate-depth · origin: critic coverage gap; not found · search: searched, not found (note: "Overdispersion fitted to 16S technical replicates at controlled depths (statistics angle)") · from: MB-01:C-115, MB-01:B-0382
- **gap.10** Contaminant-removal tools beyond decontam and SourceTracker (for example tools modelling well-to-well leakage), and independent benchmarks of decontam's prevalence mode, for low-biomass samples.
  blocks: contamination · origin: critic coverage gap · search: not stated · from: MB-01:C-116
- **gap.11** Primary-source benchmarks of compositional beta-diversity variants (robust Aitchison, phylogenetic isometric log-ratio) and of scaling methods such as GMPR and ANCOM-BC2; coverage relies on two benchmark papers.
  blocks: beta-diversity, compositional-data, scaling-normalisation · origin: critic coverage gap · search: not stated · from: MB-01:C-117
- **gap.12** Benchmarks of any approach to unequal depth or load in soil or water with measured absolute loads as truth, and known-richness mocks tested across depths.
  blocks: absolute-quantification, richness · origin: critic coverage gap; not found · search: not stated · from: MB-01:C-118
- **gap.13** Archaeal evidence is thin: one archaeal-rich mock, a copy-number range from 148 species, and one run-failure case; archaeal-specific primer bias measured against known composition in archaea-rich environments (marine, sediment, methanogenic reactors) is absent.
  blocks: primers, copy-number · origin: critic coverage gap · search: not stated · from: MB-01:C-119
- **gap.14** A follow-up for MB-01 was triggered and not yet written: several gaps name a workflow step or bias source with no measured magnitude (per-cycle amplification efficiency, community copy number measured from metagenomes, 16S index hopping on patterned flow cells, within-run read-count variation against load, and long-read platform error).
  blocks: pcr, community-copy-number, index-misassignment, reads-per-sample, library-sequencing · origin: the note's stage-2 check · search: not stated · from: MB-01:B-0021, MB-01:B-0022
- **gap.15** Sources MB-01 could not obtain that bear on its questions: a mock-community comparison of one-step against two-step library preparation and cycle number (Gohl 2016, abstract only, no figures), the largest interlaboratory extraction comparison with spike-in (Costea 2017, known only via McLaren 2019), storage effects across soil, faeces and skin (Lauber 2010, known only via Rubin 2013), index switching on HiSeq 4000, and the origins of rarefaction and sample coverage.
  blocks: library-sequencing, extraction, sampling-storage, index-misassignment, rarefying · origin: sources not obtained · search: not stated · src: gohlSystematicImprovementAmplicon2016, costeaTowardsStandardsHuman2017, lauberEffectStorageConditions2010, sinhaIndexSwitchingCauses2017 · from: MB-01:B-0130, MB-01:R-0005, MB-01:R-0009, MB-01:R-0013, MB-01:R-0043, MB-01:R-0617
- **gap.16** MB-01 lists Shoemaker 2017 and Smets 2016 both among its references as read at abstract level ("AB per lab angle") and among its sources not obtained ("only a web-search engine summary seen, not used as a finding"; Crossref with no abstract, Europe PMC not indexed), yet uses both as findings.
  blocks: abundance-distribution.4, absolute-quantification.7 · origin: the note contradicts itself · search: not stated · src: shoemakerMacroecologicalTheoryMicrobial2017, smetsMethodSimultaneousMeasurement2016 · from: MB-01:R-0058, MB-01:R-0063, MB-01:R-0515, MB-01:R-0533
- **gap.17** Polyploidy of soil and plant-associated bacteria measured outside the Soppa laboratory: Azotobacter vinelandii (40 to 80 copies, rising in stationary phase), Deinococcus radiodurans, and endoreduplicated Sinorhizobium bacteroids in nodules (Mergaert et al. 2006).
  blocks: ploidy · origin: critic coverage gap (cultured soil and root-associated bacteria; ploidy by independent laboratories) · search: not stated · from: MB-02:C-102
- **gap.18** Direct measurements of the share of cells at one genome copy against several: classic flow-cytometric chromosome run-out work giving per-cell distributions of 1, 2, 4 and 8 chromosomes (for example Skarstad, Boye and Steen 1986), and Caulobacter swarmer-cell G1 shares.
  blocks: ploidy · origin: critic coverage gap · search: not searched (critic: MB-02:C-103) · from: MB-02:C-103, MB-02:C-104, MB-02:C-105
- **gap.19** In situ cell-cycle analyses of Prochlorococcus and Synechococcus (Vaulot 1995 and successors), which report the fraction of cells in G1 against S/G2 by taxon in natural seawater, were read only at abstract level.
  blocks: ploidy · origin: critic coverage gap (marine picocyanobacteria in situ) · search: not stated · from: MB-02:C-106, MB-02:C-107, MB-02:C-108
- **gap.20** Ploidy of dormant forms (endospores, Streptomyces spores, Azotobacter cysts) and of non-growing small soil cells.
  blocks: ploidy · origin: critic coverage gap; the brief asks for dormant states · search: not stated · from: MB-02:C-109
- **gap.21** In situ growth measures in soil and rhizosphere: qSIP growth rates and growth-rate potential from genomes (for example Chuckran et al. 2025 on rewetted soil; Lopez et al. 2023 on rhizosphere against bulk soil, which also reports, via a cited study, 6.6% more rRNA operons in rhizosphere bacteria).
  blocks: ploidy, community-copy-number · origin: critic coverage gap · search: not searched (critic: MB-02:C-110) · from: MB-02:C-110
- **gap.22** Soil studies using community-weighted rrn copy number (for example succession and rhizosphere-versus-bulk comparisons, Nemergut et al. 2016) and soil absolute quantification (Smets et al. 2016) were not searched for copy-number correction or soil abundance.
  blocks: copy-number-correction, community-copy-number, abundance-distribution · origin: critic coverage gap · search: not searched (critic: MB-02:C-111) · from: MB-02:C-111, MB-02:C-027
- **gap.23** Occupancy-based classification terms: habitat generalist against specialist (Levins niche breadth, for example Szekely and Langenheder 2014), cosmopolitan against endemic, and the microbial core-satellite partition (for example van der Gast et al. 2011).
  blocks: core-microbiome, regional-terms · origin: critic coverage gap; under-covered · search: not stated · from: MB-02:C-038, MB-02:C-112
- **gap.24** The soil literature contrasting abundant and rare subcommunities' distribution ranges and niche breadth across regions (for example Jiao and Lu 2020; Jiao, Chen and Wei 2017), which bears on abundance against occupancy and on threshold usage in soil.
  blocks: abundance-occupancy, rarity-terms · origin: critic coverage gap (regional soil surveys using abundant and rare classes) · search: not searched (critic: MB-02:C-113) · from: MB-02:C-113, MB-02:C-114, MB-02:C-115
- **gap.25** Taxon abundance distributions and occupancy from global genome-resolved or metagenome-based soil datasets (for example Bahram et al. 2018).
  blocks: abundance-distribution, abundance-occupancy · origin: critic coverage gap · search: not searched (critic: MB-02:C-116) · from: MB-02:C-116
- **gap.26** Taxon-specific cell counts in soil (CARD-FISH or FISH phylum or class shares) beyond abundance-distribution queries.
  blocks: abundance-distribution · origin: critic coverage gap · search: not searched (critic: MB-02:C-117) · from: MB-02:C-117
- **gap.27** Non-soil nearest precedents for the shape of the abundance distribution that contradict the lognormal view (for example power-law tails of non-dominant plankton, Ser-Giacomi et al. 2018).
  blocks: abundance-distribution · origin: critic coverage gap (marine plankton metabarcoding) · search: not stated · from: MB-02:C-118
- **gap.28** Explicit sampling or occupancy-detection models applied to bulk-soil microbes (site-occupancy models, gamma-Poisson occupancy predictions on soil data), and whether Grilli 2020's datasets include soil.
  blocks: abundance-occupancy · origin: critic coverage gap · search: not searched (critic: MB-02:C-119) · from: MB-02:C-119, MB-02:C-120, MB-02:C-121
- **gap.29** Technical-replicate detection studies after the 454 era (Illumina, deeper sequencing) in soil, to test whether Zhou 2011's low replicate overlap generalises.
  blocks: count-sampling, abundance-occupancy · origin: critic coverage gap · search: not searched (critic: MB-02:C-122) · from: MB-02:C-122
- **gap.30** A follow-up for MB-02 was triggered and not written: the critic names unsearched per-cell and growth-state evidence for soil (in situ growth measures, ploidy of dormant and sporulated forms, taxon-specific cell counts by CARD-FISH, soil studies weighting communities by rrn copy number), occupancy-based terms and global soil metagenomes, among 13 coverage gaps; the owner decides.
  blocks: ploidy, community-copy-number, abundance-distribution, core-microbiome · origin: the note's stage-2 check · search: not stated · from: MB-02:B-0013, MB-02:B-0014, MB-02:B-0015, MB-02:B-0016, MB-02:B-0017
- **gap.31** The main bulk-soil abundance-occupancy figures (28% against 2%, 69% against 8%) could not be verified by the critic and should be rechecked; the source's abstract frames its analyses across Earth's major habitat types, not soils alone.
  blocks: abundance-occupancy.1 · origin: critic finding · search: not stated · src: nemergutGlobalPatternsBiogeography2011 · from: MB-02:C-082, MB-02:C-083, MB-02:C-084, MB-02:C-085
- **gap.32** The sampling-artefact literature on abundance-occupancy (Wright 1991; Holt et al. 2002) and the polyploidy-and-community-structure argument (Soppa 2017) were not obtained.
  blocks: abundance-occupancy, ploidy · origin: sources not obtained · search: not stated · src: wrightCorrelationsIncidenceAbundance1991, holtOccupancyabundanceRelationshipsSpatial2002, soppaPolyploidyCommunityStructure2017 · from: MB-02:B-0280, MB-02:R-0006, MB-02:R-0009, MB-02:R-0021

## Out of scope
- MB-01:C-052, MB-01:C-053: the critic's overall assessment of the review (no finding)
- MB-01:C-054: the critic's list of sources and figures verified against full text (verification, kept in the result note)
- MB-01:C-060: heading of the critic's list of answer-level over-reach (no finding)
- MB-01:C-093..104: reference corrections and Crossref checks, applied in Sources
- MB-01:C-144: the critic's expectation-echo record of the brief's wording (brief framing, no finding)
- MB-01:A-028..031: routes and access basis of answer D1 (provenance, kept in the result note)
- MB-01:A-127..130: access basis of answer D2 (provenance, kept in the result note)
- MB-01:A-179..181: routes and access basis of answer D3 (provenance, kept in the result note)
- MB-01:A-223, MB-01:A-224: access basis of answer D4 (provenance, kept in the result note)
- MB-01:A-287..289: access basis of answer D5 (provenance, kept in the result note)
- MB-02:C-056..058: the critic's verification record (verification, kept in the result note)
- MB-02:C-059: heading of the critic's list of over-reach (no finding)
- MB-02:C-094..101: reference checks against Crossref, applied in Sources
- MB-02:C-142, MB-02:C-143: the critic's expectation-echo record of the brief's wording (brief framing, no finding)
- MB-02:A-016, MB-02:A-035, MB-02:A-056, MB-02:A-078, MB-02:A-096, MB-02:A-122: access basis of the answers (provenance, kept in the result note)
- MB-02:A-133, MB-02:A-139: access basis of the brief answers (provenance, kept in the result note)
- MB-01:A-035: how the D2 answer is laid out (navigation, no finding)

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
  note = {access: full_text (MB-01); type: peer reviewed; cited as: MB-01 2021}
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

@article{acinasPCRinducedSequenceArtifacts2005,
  author = {Acinas, Silvia G. and Sarma-Rupavtarm, Ramahi and Klepac-Ceraj, Vanja and Polz, Martin F.},
  title = {PCR-induced sequence artifacts and bias: insights from comparison of two 16S rRNA clone libraries constructed from the same sample},
  journal = {Applied and Environmental Microbiology},
  year = {2005},
  volume = {71},
  number = {12},
  pages = {8966-8969},
  doi = {10.1128/AEM.71.12.8966-8969.2005},
  note = {access: abstract_only (MB-01); type: peer reviewed; cited as: MB-01 2005}
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

@article{albertsenBackBasicsInfluence2015,
  author = {Albertsen, Mads and Karst, Søren M. and Ziegler, Anja S. and Kirkegaard, Rasmus H. and Nielsen, Per H.},
  title = {Back to basics: the influence of DNA extraction and primer choice on phylogenetic analysis of activated sludge communities},
  journal = {PLOS ONE},
  year = {2015},
  volume = {10},
  number = {7},
  pages = {e0132783},
  doi = {10.1371/journal.pone.0132783},
  note = {access: full_text (MB-01); type: peer reviewed; cited as: MB-01 2015}
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
  note = {access: full_text (MB-01); type: peer reviewed; cited as: MB-01 2018}
}

@article{alroyCoveragebasedRarefactionFails2026,
  author = {Alroy, John},
  title = {Coverage-based rarefaction fails to quantify relative species richness},
  journal = {Oikos},
  year = {2026},
  pages = {e11607},
  doi = {10.1002/oik.11607},
  note = {access: abstract_only (MB-01); type: peer reviewed; cited as: MB-01 2026; published online 2026-09-14; volume not yet assigned; MB-01 also says: DOI checked on Crossref by the synthesis agent}
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
  note = {access: abstract_only (MB-01); type: peer reviewed; cited as: MB-01 2010}
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

@article{bakkenDNAcontentSoilBacteria1989,
  author = {Bakken, Lars R. and Olsen, Rolf A.},
  title = {DNA-content of soil bacteria of different cell size},
  journal = {Soil Biology and Biochemistry},
  year = {1989},
  volume = {21},
  number = {6},
  pages = {789-793},
  doi = {10.1016/0038-0717(89)90172-7},
  note = {access: not_obtained (MB-02); cited as: MB-02 Bakken and Olsen 1989; known only via Christensen et al. 1995 abstract}
}

@article{barberanWhyAreMicrobes2014,
  author = {Barberán, Albert and Ramirez, Kelly S. and Leff, Jonathan W. and Bradford, Mark A. and Wall, Diana H. and Fierer, Noah},
  title = {Why are some microbes more ubiquitous than others? Predicting the habitat breadth of soil bacteria},
  journal = {Ecology Letters},
  year = {2014},
  volume = {17},
  number = {7},
  pages = {794-802},
  doi = {10.1111/ele.12282},
  note = {access: abstract_only (MB-02); cited as: MB-02 [63]}
}

@article{barlowQuantitativeSequencingFramework2020,
  author = {Barlow, Jacob T. and Bogatyrev, Said R. and Ismagilov, Rustem F.},
  title = {A quantitative sequencing framework for absolute abundance measurements of mucosal and lumenal microbial communities},
  journal = {Nature Communications},
  year = {2020},
  volume = {11},
  pages = {2590},
  doi = {10.1038/s41467-020-16224-6},
  note = {access: full_text (MB-01); type: peer reviewed; cited as: MB-01 2020}
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

@misc{benjjnebConsequencesUsingDada2,
  author = {{benjjneb (DADA2 maintainer) and contributors}},
  title = {Consequences of using dada2 on NovaSeq data. GitHub issue #791, benjjneb/dada2},
  url = {https://github.com/benjjneb/dada2/issues/791},
  note = {access: full_text (MB-01); type: documentation; cited as: MB-01 DADA2 GitHub issue #791; accessed 2026-10-20; issue tracker; incomplete: year}
}

@article{beuleImprovedNormalizationSpecies2020,
  author = {Beule, Lukas and Karlovsky, Petr},
  title = {Improved normalization of species count data in ecology by scaling with ranked subsampling (SRS): application to microbial communities},
  journal = {PeerJ},
  year = {2020},
  volume = {8},
  pages = {e9593},
  doi = {10.7717/peerj.9593},
  note = {access: abstract_only (MB-01); type: peer reviewed; cited as: MB-01 2020}
}

@article{bickelChosenFewVariations2021,
  author = {Bickel, Samuel and Or, Dani},
  title = {The chosen few - variations in common and rare soil bacteria across biomes},
  journal = {The ISME Journal},
  year = {2021},
  volume = {15},
  number = {11},
  pages = {3315-3325},
  doi = {10.1038/s41396-021-00981-3},
  note = {access: full_text (MB-02); cited as: MB-02 [61]}
}

@article{bokulichOptimizingTaxonomicClassification2018,
  author = {Bokulich, Nicholas A. and Kaehler, Benjamin D. and Rideout, Jai Ram and Dillon, Matthew and Bolyen, Evan and Knight, Rob and Huttley, Gavin A. and Caporaso, J. Gregory},
  title = {Optimizing taxonomic classification of marker-gene amplicon sequences with QIIME 2's q2-feature-classifier plugin},
  journal = {Microbiome},
  year = {2018},
  volume = {6},
  pages = {90},
  doi = {10.1186/s40168-018-0470-z},
  note = {access: full_text (MB-01); type: peer reviewed; cited as: MB-01 2018}
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
  note = {access: full_text (MB-01); type: peer reviewed; cited as: MB-01 2013}
}

@article{bonkPCRbasedQuantificationTaxaspecific2018,
  author = {Bonk, Fabian and Popp, Denny and Harms, Hauke and Centler, Florian},
  title = {PCR-based quantification of taxa-specific abundances in microbial communities: quantifying and avoiding common pitfalls},
  journal = {Journal of Microbiological Methods},
  year = {2018},
  volume = {153},
  pages = {139-147},
  doi = {10.1016/j.mimet.2018.09.015},
  note = {access: abstract_only (MB-01); type: peer reviewed review; cited as: MB-01 2018}
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

@incollection{bremerModulationChemicalComposition1996,
  author = {Bremer, H. and Dennis, P. P.},
  title = {Modulation of chemical composition and other parameters of the cell by growth rate},
  booktitle = {Escherichia coli and Salmonella: Cellular and Molecular Biology, 2nd ed., chapter 97},
  editor = {Neidhardt, F. C. and others},
  publisher = {ASM Press},
  year = {1996},
  note = {access: not_obtained (MB-02); cited as: MB-02 Bremer and Dennis 1996; used as secondary via BioNumbers; incomplete: pages}
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
  note = {access: abstract_only (critic MB-02:C-069: open in PMC; not tried) (MB-02); cited as: MB-02 [14]}
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

@article{brooksTruthMetagenomicsQuantifying2015,
  author = {{Vaginal Microbiome Consortium} and Brooks, J. Paul and Edwards, David J. and Harwich, Michael D. Jr and Rivera, Maria C. and Fettweis, Jennifer M. and Serrano, Myrna G. and Reris, Robert A. and Sheth, Nihar U. and Huang, Bernice and Girerd, Philippe and Strauss, Jerome F. 3rd and Jefferson, Kimberly K. and Buck, Gregory A.},
  title = {The truth about metagenomics: quantifying and counteracting bias in 16S rRNA studies},
  journal = {BMC Microbiology},
  year = {2015},
  volume = {15},
  pages = {66},
  doi = {10.1186/s12866-015-0351-6},
  note = {access: full_text (MB-01); type: peer reviewed; cited as: MB-01 2015; title corrected against Crossref by the synthesis agent; critic MB-01:C-098..C-100: title confirmed; Crossref puts the consortium first; MB-01 also says: title corrected against Crossref}
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
  note = {access: full_text (first 100,000 characters) (MB-02); cited as: MB-02 [25]}
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
  note = {access: abstract_only (critic MB-02:C-072: open in PMC; the critic read the full text) (MB-02); cited as: MB-02 [18]}
}

@article{bullardEvaluationStatisticalMethods2010,
  author = {Bullard, James H. and Purdom, Elizabeth and Hansen, Kasper D. and Dudoit, Sandrine},
  title = {Evaluation of statistical methods for normalization and differential expression in mRNA-Seq experiments},
  journal = {BMC Bioinformatics},
  year = {2010},
  volume = {11},
  pages = {94},
  doi = {10.1186/1471-2105-11-94},
  note = {access: abstract_only (MB-01); type: peer reviewed; cited as: MB-01 2010}
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
  note = {access: full_text (first 100,000 characters) (MB-02); cited as: MB-02 [23]}
}

@article{calgaroAssessmentStatisticalMethods2020,
  author = {Calgaro, Matteo and Romualdi, Chiara and Waldron, Levi and Risso, Davide and Vitulo, Nicola},
  title = {Assessment of statistical methods from single cell, bulk RNA-seq, and metagenomics applied to microbiome data},
  journal = {Genome Biology},
  year = {2020},
  volume = {21},
  pages = {191},
  doi = {10.1186/s13059-020-02104-1},
  note = {access: abstract_only (MB-01); type: peer reviewed; cited as: MB-01 2020}
}

@misc{callahanDADA2DocumentationPseudopooling,
  author = {Callahan, Benjamin J.},
  title = {DADA2 documentation: Pseudo-pooling},
  url = {https://benjjneb.github.io/dada2/pseudo.html},
  note = {access: full_text (MB-01); type: documentation; cited as: MB-01 DADA2 pseudo-pooling page; accessed 2026-10-20; incomplete: year}
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
  note = {access: full_text (MB-01); type: peer reviewed; cited as: MB-01 2016}
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
  note = {access: full_text (MB-01); type: peer reviewed; cited as: MB-01 2019}
}

@article{cameronEnhancingDiversityAnalysis2021,
  author = {Cameron, Ellen S. and Schmidt, Philip J. and Tremblay, Benjamin J.-M. and Emelko, Monica B. and Müller, Kirsten M.},
  title = {Enhancing diversity analysis by repeatedly rarefying next generation sequencing data describing microbial communities},
  journal = {Scientific Reports},
  year = {2021},
  volume = {11},
  pages = {22302},
  doi = {10.1038/s41598-021-01636-1},
  note = {access: full_text (MB-01); type: peer reviewed; cited as: MB-01 2021}
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
  note = {access: abstract_only (MB-01), abstract_only (MB-02); type: peer reviewed; cited as: MB-01 2016, MB-02 [77]}
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
  note = {access: full_text (MB-01); type: peer reviewed; cited as: MB-01 2019}
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
  note = {access: full_text (via third-party PDF https://www.davidzeleny.net/wiki/lib/exe/fetch.php/vegecol:materials:chao-jost2012_ecology.pdf, accessed 2026-10-20) (MB-01); type: peer reviewed; cited as: MB-01 2012}
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
  note = {access: full_text (via author PDF https://www.uvm.edu/~ngotelli/manuscriptpdfs/ChaoHill.pdf, accessed 2026-10-20) (MB-01); type: peer reviewed; cited as: MB-01 2014}
}

@article{chiarelloRankingBiasesChoice2022,
  author = {Chiarello, Marlène and McCauley, Mark and Villéger, Sébastien and Jackson, Colin R.},
  title = {Ranking the biases: the choice of OTUs vs. ASVs in 16S rRNA amplicon data analysis has stronger effects on diversity measures than rarefaction and OTU identity threshold},
  journal = {PLOS ONE},
  year = {2022},
  volume = {17},
  number = {2},
  pages = {e0264443},
  doi = {10.1371/journal.pone.0264443},
  note = {access: full_text (MB-01); type: peer reviewed; cited as: MB-01 2022}
}

@article{chiuEstimatingComparingMicrobial2016,
  author = {Chiu, Chun-Huo and Chao, Anne},
  title = {Estimating and comparing microbial diversity in the presence of sequencing errors},
  journal = {PeerJ},
  year = {2016},
  volume = {4},
  pages = {e1634},
  doi = {10.7717/peerj.1634},
  note = {access: abstract_only (MB-01); type: peer reviewed; cited as: MB-01 2016}
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
  note = {access: abstract_only (MB-02); cited as: MB-02 [22]; critic MB-02:C-097: Crossref has no page range; pages 49-62 not confirmed from Crossref}
}

@article{christensenSoilBacterialDNA1993,
  author = {Christensen, Henrik and Bakken, Lars R. and Olsen, Rolf A.},
  title = {Soil bacterial DNA and biovolume profiles measured by flow-cytometry},
  journal = {FEMS Microbiology Ecology 11(3-4):129-140 / FEMS Microbiology Letters 102(3-4):129-140},
  year = {1993},
  pages = {129-140},
  doi = {10.1111/j.1574-6968.1993.tb05804.x},
  note = {access: not_obtained (MB-02); cited as: MB-02 Christensen 1993; Crossref has two records}
}

@article{costeaTowardsStandardsHuman2017,
  author = {Costea, Paul I. and Zeller, Georg and Sunagawa, Shinichi and others},
  title = {Towards standards for human fecal sample processing in metagenomic studies},
  journal = {Nature Biotechnology},
  year = {2017},
  volume = {35},
  number = {11},
  pages = {1069-1076},
  doi = {10.1038/nbt.3960},
  note = {access: not_obtained (MB-01); cited as: MB-01 Costea 2017; known only secondarily via McLaren 2019 (cited as SEC); incomplete: author}
}

@article{costelloCharacterizationRemediationSample2018,
  author = {Costello, Maura and Fleharty, Mark and Abreu, Justin and Farjoun, Yossi and Ferriera, Steven and Holmes, Laurie and Granger, Brian and Green, Lisa and Howd, Tom and Mason, Tamara and Vicente, Gina and Dasilva, Michael and Brodeur, Wendy and DeSmet, Timothy and Dodge, Sheila and Lennon, Niall J. and Gabriel, Stacey},
  title = {Characterization and remediation of sample index swaps by non-redundant dual indexing on massively parallel sequencing platforms},
  journal = {BMC Genomics},
  year = {2018},
  volume = {19},
  pages = {332},
  doi = {10.1186/s12864-018-4703-0},
  note = {access: full_text (MB-01); type: peer reviewed; cited as: MB-01 2018}
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

@article{custerComparativeAnalysisCore2023,
  author = {Custer, Gordon F. and Gans, Maya and van Diepen, Linda T. A. and Dini-Andreote, Francisco and Buerkle, C. Alex},
  title = {Comparative analysis of core microbiome assignments: implications for ecological synthesis},
  journal = {mSystems},
  year = {2023},
  volume = {8},
  number = {1},
  pages = {e01066-22},
  doi = {10.1128/msystems.01066-22},
  note = {access: full_text (first 100,000 characters) (MB-02); cited as: MB-02 [52]}
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

@article{damoreComprehensiveBenchmarkingStudy2016,
  author = {D'Amore, Rosalinda and Ijaz, Umer Zeeshan and Schirmer, Melanie and Kenny, John G. and Gregory, Richard and Darby, Alistair C. and Shakya, Migun and Podar, Mircea and Quince, Christopher and Hall, Neil},
  title = {A comprehensive benchmarking study of protocols and sequencing platforms for 16S rRNA community profiling},
  journal = {BMC Genomics},
  year = {2016},
  volume = {17},
  pages = {55},
  doi = {10.1186/s12864-015-2194-9},
  note = {access: full_text (MB-01); type: peer reviewed; cited as: MB-01 2016}
}

@article{davisSimpleStatisticalIdentification2018,
  author = {Davis, Nicole M. and Proctor, Diana M. and Holmes, Susan P. and Relman, David A. and Callahan, Benjamin J.},
  title = {Simple statistical identification and removal of contaminant sequences in marker-gene and metagenomics data},
  journal = {Microbiome},
  year = {2018},
  volume = {6},
  pages = {226},
  doi = {10.1186/s40168-018-0605-2},
  note = {access: full_text (MB-01); type: peer reviewed; cited as: MB-01 2018}
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
  note = {access: full_text (MB-02); cited as: MB-02 [60]}
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
  note = {access: full_text (MB-01); type: peer reviewed perspective; cited as: MB-01 2024; MB-01 also says: DOI checked by the synthesis agent}
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

@article{dyrhovdenManagingContaminationDiverse2021,
  author = {Dyrhovden, Ruben and Rippin, Martin and Øvrebø, Kjell Kåre and Nygaard, Randi M. and Ulvestad, Elling and Kommedal, Øyvind},
  title = {Managing contamination and diverse bacterial loads in 16S rRNA deep sequencing of clinical samples: implications of the law of small numbers},
  journal = {mBio},
  year = {2021},
  volume = {12},
  number = {3},
  pages = {e00598-21},
  doi = {10.1128/mBio.00598-21},
  note = {access: full_text (MB-01); type: peer reviewed; cited as: MB-01 2021; MB-01 also says: DOI checked by the synthesis agent}
}

@misc{earth16SIlluminaAmplicon,
  author = {{Earth Microbiome Project}},
  title = {16S Illumina Amplicon Protocol},
  url = {https://earthmicrobiome.org/protocols-and-standards/16s/},
  note = {access: full_text (MB-01); type: protocol; cited as: MB-01 EMP protocol; accessed 2026-10-20; incomplete: year}
}

@article{edgarAccuracyMicrobialCommunity2017,
  author = {Edgar, Robert C.},
  title = {Accuracy of microbial community diversity estimated by closed- and open-reference OTUs},
  journal = {PeerJ},
  year = {2017},
  volume = {5},
  pages = {e3889},
  doi = {10.7717/peerj.3889},
  note = {access: full_text (MB-01); type: peer reviewed; cited as: MB-01 2017a}
}

@article{edgarAccuracyTaxonomyPrediction2018,
  author = {Edgar, Robert C.},
  title = {Accuracy of taxonomy prediction for 16S rRNA and fungal ITS sequences},
  journal = {PeerJ},
  year = {2018},
  volume = {6},
  pages = {e4652},
  doi = {10.7717/peerj.4652},
  note = {access: full_text (MB-01); type: peer reviewed; cited as: MB-01 2018b}
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
  note = {access: abstract_only (MB-01); type: peer reviewed; cited as: MB-01 2015}
}

@article{edgarTaxonomyAnnotationGuide2018,
  author = {Edgar, Robert},
  title = {Taxonomy annotation and guide tree errors in 16S rRNA databases},
  journal = {PeerJ},
  year = {2018},
  volume = {6},
  pages = {e5030},
  doi = {10.7717/peerj.5030},
  note = {access: full_text (MB-01); type: peer reviewed; cited as: MB-01 2018c}
}

@misc{edgarUCHIME2ImprovedChimera2016,
  author = {Edgar, Robert C.},
  title = {UCHIME2: improved chimera prediction for amplicon sequencing},
  howpublished = {bioRxiv},
  year = {2016},
  number = {074252},
  doi = {10.1101/074252},
  note = {access: abstract_only (MB-01); type: preprint; cited as: MB-01 2016b}
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
  note = {access: full_text (per bioinformatics angle) (MB-01); type: peer reviewed; cited as: MB-01 2011; not cited: listed in the references, cited nowhere in the text}
}

@misc{edgarUNBIASAttemptCorrect2017,
  author = {Edgar, Robert C.},
  title = {UNBIAS: an attempt to correct abundance bias in 16S sequencing, with limited success},
  howpublished = {bioRxiv},
  year = {2017},
  number = {124149},
  doi = {10.1101/124149},
  note = {access: abstract_only (MB-01), abstract_only (MB-02); type: preprint; cited as: MB-01 2017b, MB-02 [31]; MB-01 also says: DOI checked by the synthesis agent}
}

@misc{edgarUNCROSSFilteringHighfrequency2016,
  author = {Edgar, Robert C.},
  title = {UNCROSS: filtering of high-frequency cross-talk in 16S amplicon reads},
  howpublished = {bioRxiv},
  year = {2016},
  number = {088666},
  doi = {10.1101/088666},
  note = {access: abstract_only (MB-01); type: preprint; cited as: MB-01 2016a}
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
  note = {access: abstract_only (MB-01); type: peer reviewed; cited as: MB-01 2018a}
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
  note = {access: abstract_only (MB-01); type: peer reviewed review; cited as: MB-01 2019}
}

@misc{emoryAmplicon16SMetagenomics,
  author = {{Emory Integrated Genomics Core / ECGC}},
  title = {Amplicon 16S metagenomics (methods description)},
  url = {https://www.cores.emory.edu/ecgc/_includes/documents/sections/resources/amplicon-16s-metagenomics.pdf},
  note = {access: full_text (MB-01); type: protocol; cited as: MB-01 Emory core; accessed 2026-10-20; incomplete: year}
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
  note = {access: full_text (MB-01); type: peer reviewed; cited as: MB-01 2015}
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

@article{fitzpatrickChloroplastSequenceVariation2018,
  author = {Fitzpatrick, Connor R. and Lu-Irving, Patricia and Copeland, Julia and Guttman, David S. and Wang, Pauline W. and Baltrus, David A. and Dlugosch, Katrina M. and Johnson, Marc T. J.},
  title = {Chloroplast sequence variation and the efficacy of peptide nucleic acids for blocking host amplification in plant microbiome studies},
  journal = {Microbiome},
  year = {2018},
  volume = {6},
  pages = {144},
  doi = {10.1186/s40168-018-0534-0},
  note = {access: full_text (MB-01); type: peer reviewed; cited as: MB-01 2018}
}

@article{fouhy16SRRNAGene2016,
  author = {Fouhy, Fiona and Clooney, Adam G. and Stanton, Catherine and Claesson, Marcus J. and Cotter, Paul D.},
  title = {16S rRNA gene sequencing of mock microbial populations: impact of DNA extraction method, primer choice and sequencing platform},
  journal = {BMC Microbiology},
  year = {2016},
  volume = {16},
  pages = {123},
  doi = {10.1186/s12866-016-0738-z},
  note = {access: full_text (MB-01); type: peer reviewed; cited as: MB-01 2016}
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
  note = {access: abstract_only (MB-01); type: peer reviewed; cited as: MB-01 1999; critic MB-01:C-093: Crossref gives Vincent Ramisse (the note had Valérie) and Francoise Le Gall}
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

@article{galazzoHowCountOur2020,
  author = {Galazzo, Gianluca and van Best, Niels and Benedikter, Birke J. and Janssen, Kevin and Bervoets, Liene and Driessen, Christel and Oomen, Melissa and Lucchesi, Mayk and van Eijck, Pascalle H. and Becker, Heike E. F. and Hornef, Mathias W. and Savelkoul, Paul H. and Stassen, Frank R. M. and Wolffs, Petra F. and Penders, John},
  title = {How to count our microbes? The effect of different quantitative microbiome profiling approaches},
  journal = {Frontiers in Cellular and Infection Microbiology},
  year = {2020},
  volume = {10},
  pages = {403},
  doi = {10.3389/fcimb.2020.00403},
  note = {access: full_text (MB-01); type: peer reviewed; cited as: MB-01 2020; MB-01 also says: DOI checked by the synthesis agent}
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

@article{gaoAccounting16SRRNA2023,
  author = {Gao, Yingnan and Wu, Martin},
  title = {Accounting for 16S rRNA copy number prediction uncertainty and its implications in bacterial diversity analyses},
  journal = {ISME Communications},
  year = {2023},
  volume = {3},
  pages = {59},
  doi = {10.1038/s43705-023-00266-0},
  note = {access: full_text (MB-02); cited as: MB-02 [33]}
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

@book{gastonRarity1994,
  author = {Gaston, Kevin J.},
  title = {Rarity},
  publisher = {Chapman and Hall, London},
  year = {1994},
  note = {access: not_obtained (MB-02); cited as: MB-02 Gaston 1994; not searched beyond citation trail}
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
  note = {access: abstract_only (MB-01); type: peer reviewed; cited as: MB-01 2018}
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
  note = {access: abstract_only (MB-01); type: peer reviewed; cited as: MB-01 2012}
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
  note = {access: full_text (MB-01); type: peer reviewed; cited as: MB-01 2018}
}

@article{gloorMicrobiomeDatasetsCompositional2017,
  author = {Gloor, Gregory B. and Macklaim, Jean M. and Pawlowsky-Glahn, Vera and Egozcue, Juan J.},
  title = {Microbiome datasets are compositional: and this is not optional},
  journal = {Frontiers in Microbiology},
  year = {2017},
  volume = {8},
  pages = {2224},
  doi = {10.3389/fmicb.2017.02224},
  note = {access: abstract_only (MB-01); type: peer reviewed mini review; cited as: MB-01 2017}
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

@article{gohlSystematicImprovementAmplicon2016,
  author = {Gohl, Daryl M and Vangay, Pajau and Garbe, John and MacLean, Allison and Hauge, Adam and Becker, Aaron and Gould, Trevor J and Clayton, Jonathan B and Johnson, Timothy J and Hunter, Ryan and Knights, Dan and Beckman, Kenneth B},
  title = {Systematic improvement of amplicon marker gene methods for increased accuracy in microbiome studies},
  journal = {Nature Biotechnology},
  year = {2016},
  volume = {34},
  number = {9},
  pages = {942-949},
  doi = {10.1038/nbt.3601},
  note = {access: not_obtained (MB-01); cited as: MB-01 Gohl 2016; abstract obtained only, no figures}
}

@article{goodPopulationFrequenciesSpecies1953,
  author = {Good, I. J.},
  title = {The population frequencies of species and the estimation of population parameters},
  journal = {Biometrika},
  year = {1953},
  volume = {40},
  number = {3-4},
  pages = {237-264},
  doi = {10.1093/biomet/40.3-4.237},
  note = {access: not_obtained (MB-01); cited as: MB-01 Good 1953}
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
  note = {access: abstract_only (MB-01); type: peer reviewed review; cited as: MB-01 2001}
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

@article{grilliMacroecologicalLawsDescribe2020,
  author = {Grilli, Jacopo},
  title = {Macroecological laws describe variation and diversity in microbial communities},
  journal = {Nature Communications},
  year = {2020},
  volume = {11},
  pages = {4743},
  doi = {10.1038/s41467-020-18529-y},
  note = {access: full_text (partly re-opened by the synthesis agent) (MB-01), full_text (MB-02); type: peer reviewed; cited as: MB-01 2020, MB-02 [72]}
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
  note = {access: full_text (MB-01); type: peer reviewed; cited as: MB-01 2011}
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
  note = {access: full_text (critic MB-01:C-073..C-076: could not be confirmed as open full text) (MB-01); type: peer reviewed; cited as: MB-01 2013}
}

@article{hakimzadehPilePipelinesOverview2024,
  author = {Hakimzadeh, Ali and Abdala Asbun, Alejandro and Albanese, Davide and Bernard, Maria and Buchner, Dominik and Callahan, Benjamin and Caporaso, J. Gregory and Curd, Emily and Djemiel, Christophe and Brandström Durling, Mikael and Elbrecht, Vasco and Gold, Zachary and Gweon, Hyun S. and Hajibabaei, Mehrdad and Hildebrand, Falk and Mikryukov, Vladimir and Normandeau, Eric and Özkurt, Ezgi and Palmer, Jonathan M. and Pascal, Géraldine and Porter, Teresita M. and Straub, Daniel and Vasar, Martti and Větrovský, Tomáš and Zafeiropoulos, Haris and Anslan, Sten},
  title = {A pile of pipelines: an overview of the bioinformatics software for metabarcoding data analyses},
  journal = {Molecular Ecology Resources},
  year = {2024},
  volume = {24},
  number = {5},
  pages = {e13847},
  doi = {10.1111/1755-0998.13847},
  note = {access: not_obtained (MB-01); cited as: MB-01 Hakimzadeh 2024}
}

@article{hanskiDynamicsRegionalDistribution1982,
  author = {Hanski, Ilkka},
  title = {Dynamics of regional distribution: the core and satellite species hypothesis},
  journal = {Oikos},
  year = {1982},
  volume = {38},
  number = {2},
  pages = {210-221},
  doi = {10.2307/3544021},
  note = {access: not_obtained (MB-02); cited as: MB-02 Hanski 1982}
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
  note = {access: abstract_only (MB-01); type: peer reviewed; cited as: MB-01 2020}
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
  note = {access: abstract_only (MB-01); type: peer reviewed review; cited as: MB-01 2021}
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
  note = {access: abstract_only (MB-01); type: peer reviewed; cited as: MB-01 2019}
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
  note = {access: abstract_only (critic MB-02:C-076: a PMC record exists) (MB-02); cited as: MB-02 [15]}
}

@article{holtOccupancyabundanceRelationshipsSpatial2002,
  author = {Holt, Alison R. and Gaston, Kevin J. and He, Fangliang},
  title = {Occupancy-abundance relationships and spatial distribution: a review},
  journal = {Basic and Applied Ecology},
  year = {2002},
  volume = {3},
  number = {1},
  pages = {1-13},
  doi = {10.1078/1439-1791-00083},
  note = {access: not_obtained (MB-02); cited as: MB-02 Holt 2002}
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
  note = {access: full_text (MB-01); type: peer reviewed; cited as: MB-01 2022}
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
  note = {access: full_text (MB-01); type: peer reviewed; cited as: MB-01 2019}
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

@article{hsiehINEXTRPackage2016,
  author = {Hsieh, T. C. and Ma, K. H. and Chao, Anne},
  title = {iNEXT: an R package for rarefaction and extrapolation of species diversity (Hill numbers)},
  journal = {Methods in Ecology and Evolution},
  year = {2016},
  volume = {7},
  number = {12},
  pages = {1451-1456},
  doi = {10.1111/2041-210X.12613},
  note = {access: not_obtained (MB-01); cited as: MB-01 Hsieh 2016 (iNEXT)}
}

@article{hurlbertNonconceptSpeciesDiversity1971,
  author = {Hurlbert, Stuart H.},
  title = {The nonconcept of species diversity: a critique and alternative parameters},
  journal = {Ecology},
  year = {1971},
  volume = {52},
  number = {4},
  pages = {577-586},
  doi = {10.2307/1934145},
  note = {access: not_obtained (MB-01); cited as: MB-01 Hurlbert 1971; known only secondarily via Chao and Jost 2012 and Willis 2019}
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

@manual{illumina16SMetagenomicSequencing,
  author = {{Illumina, Inc.}},
  title = {16S Metagenomic Sequencing Library Preparation: Preparing 16S Ribosomal RNA Gene Amplicons for the Illumina MiSeq System. Part # 15044223 Rev. B},
  url = {https://support.illumina.com/documents/documentation/chemistry_documentation/16s/16s-metagenomic-library-prep-guide-15044223-b.pdf},
  note = {access: full_text (MB-01); type: documentation; cited as: MB-01 Illumina 16S guide; accessed 2026-10-20; maker's claims; incomplete: year}
}

@misc{illuminaIndexHoppingWeb,
  author = {{Illumina, Inc.}},
  title = {Index hopping (web page)},
  url = {https://www.illumina.com/techniques/sequencing/ngs-library-prep/multiplexing/index-hopping.html},
  note = {access: full_text (MB-01); type: documentation; cited as: MB-01 Illumina index-hopping page; accessed 2026-10-20; maker's claims; incomplete: year}
}

@article{jiaCommunityAssemblyProcesses2018,
  author = {Jia, Xiu and Dini-Andreote, Francisco and Salles, Joana Falcão},
  title = {Community assembly processes of the microbial rare biosphere},
  journal = {Trends in Microbiology},
  year = {2018},
  volume = {26},
  number = {9},
  pages = {738-747},
  doi = {10.1016/j.tim.2018.02.011},
  note = {access: abstract_only (MB-02); cited as: MB-02 [48]}
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
  note = {access: full_text (MB-01); type: peer reviewed; cited as: MB-01 2020}
}

@article{jiaUnravellingInterplayEcological2022,
  author = {Jia, Xiu and Dini-Andreote, Francisco and Salles, Joana Falcão},
  title = {Unravelling the interplay of ecological processes structuring the bacterial rare biosphere},
  journal = {ISME Communications},
  year = {2022},
  volume = {2},
  pages = {96},
  doi = {10.1038/s43705-022-00177-6},
  note = {access: full_text (MB-02); cited as: MB-02 [49]}
}

@article{johnsonEvaluation16SRRNA2019,
  author = {Johnson, Jethro S. and Spakowicz, Daniel J. and Hong, Bo-Young and Petersen, Lauren M. and Demkowicz, Patrick and Chen, Lei and Leopold, Shana R. and Hanson, Blake M. and Agresta, Hanako O. and Gerstein, Mark and Sodergren, Erica and Weinstock, George M.},
  title = {Evaluation of 16S rRNA gene sequencing for species and strain-level microbiome analysis},
  journal = {Nature Communications},
  year = {2019},
  volume = {10},
  pages = {5029},
  doi = {10.1038/s41467-019-13036-1},
  note = {access: full_text (MB-01); type: peer reviewed; cited as: MB-01 2019}
}

@article{joosDaringDifferentialMetabarcoding2020,
  author = {Joos, Lisa and Beirinckx, Stien and Haegeman, Annelies and Debode, Jane and Vandecasteele, Bart and Baeyen, Steve and Goormachtig, Sofie and Clement, Lieven and De Tender, Caroline},
  title = {Daring to be differential: metabarcoding analysis of soil and plant-related microbial communities using amplicon sequence variants and operational taxonomical units},
  journal = {BMC Genomics},
  year = {2020},
  volume = {21},
  pages = {733},
  doi = {10.1186/s12864-020-07126-4},
  note = {access: full_text (MB-01); type: peer reviewed; cited as: MB-01 2020}
}

@article{joussetWhereLessMay2017,
  author = {Jousset, Alexandre and Bienhold, Christina and Chatzinotas, Antonis and Gallien, Laure and Gobet, Angélique and Kurm, Viola and Küsel, Kirsten and Rillig, Matthias C. and Rivett, Damian W. and Salles, Joana F. and van der Heijden, Marcel G. A. and Youssef, Noha H. and Zhang, Xiaowei and Wei, Zhong and Hol, W. H. Gera},
  title = {Where less may be more: how the rare biosphere pulls ecosystems strings},
  journal = {The ISME Journal},
  year = {2017},
  volume = {11},
  number = {4},
  pages = {853-862},
  doi = {10.1038/ismej.2016.174},
  note = {access: full_text (MB-02); cited as: MB-02 [47]}
}

@article{kaehlerSpeciesAbundanceInformation2019,
  author = {Kaehler, Benjamin D. and Bokulich, Nicholas A. and McDonald, Daniel and Knight, Rob and Caporaso, J. Gregory and Huttley, Gavin A.},
  title = {Species abundance information improves sequence taxonomy classification accuracy},
  journal = {Nature Communications},
  year = {2019},
  volume = {10},
  pages = {4643},
  doi = {10.1038/s41467-019-12669-6},
  note = {access: full_text (MB-01); type: peer reviewed; cited as: MB-01 2019}
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
  note = {access: full_text (MB-01); type: peer reviewed; cited as: MB-01 2019}
}

@article{kaulAnalysisMicrobiomeData2017,
  author = {Kaul, Abhishek and Mandal, Siddhartha and Davidov, Ori and Peddada, Shyamal D.},
  title = {Analysis of microbiome data in the presence of excess zeros},
  journal = {Frontiers in Microbiology},
  year = {2017},
  volume = {8},
  pages = {2114},
  doi = {10.3389/fmicb.2017.02114},
  note = {access: abstract_only (MB-01); type: peer reviewed; cited as: MB-01 2017}
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
  note = {access: full_text (MB-01); type: peer reviewed; cited as: MB-01 2015}
}

@article{kellyUnderstandingPCRProcesses2019,
  author = {Kelly, Ryan P. and Shelton, Andrew Olaf and Gallego, Ramón},
  title = {Understanding PCR processes to draw meaningful conclusions from environmental DNA studies},
  journal = {Scientific Reports},
  year = {2019},
  volume = {9},
  pages = {12133},
  doi = {10.1038/s41598-019-48546-x},
  note = {access: full_text (MB-01); type: peer reviewed; cited as: MB-01 2019}
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
  note = {access: full_text (MB-01), full_text (MB-02); type: peer reviewed; cited as: MB-01 2012, MB-02 [28]}
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
  note = {access: abstract_only (critic MB-01:C-073: labelled FT per angle; could not be confirmed as open full text) (MB-01); type: peer reviewed; cited as: MB-01 2014}
}

@article{kersPowerMicrobiomeStudies2022,
  author = {Kers, Jannigje Gerdien and Saccenti, Edoardo},
  title = {The power of microbiome studies: some considerations on which alpha and beta metrics to use and how to report results},
  journal = {Frontiers in Microbiology},
  year = {2022},
  volume = {12},
  pages = {796025},
  doi = {10.3389/fmicb.2021.796025},
  note = {access: abstract_only (MB-01); type: peer reviewed; cited as: MB-01 2022}
}

@article{kimOptimizingMethodsDodging2017,
  author = {Kim, Dorothy and Hofstaedter, Casey E. and Zhao, Chunyu and Mattei, Lisa and Tanes, Ceylan and Clarke, Erik and Lauder, Abigail and Sherrill-Mix, Scott and Chehoud, Christel and Kelsen, Judith and Conrad, Máire and Collman, Ronald G. and Baldassano, Robert and Bushman, Frederic D. and Bittinger, Kyle},
  title = {Optimizing methods and dodging pitfalls in microbiome research},
  journal = {Microbiome},
  year = {2017},
  volume = {5},
  pages = {52},
  doi = {10.1186/s40168-017-0267-5},
  note = {access: not_obtained (MB-01); cited as: MB-01 Kim 2017; keyword-searched; review content not reported}
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
  note = {access: full_text (MB-01); type: peer reviewed; cited as: MB-01 2012}
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
  note = {access: abstract_only (MB-01), abstract_only (MB-02); type: peer reviewed; cited as: MB-01 2000, MB-02 [9]}
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
  note = {access: abstract_only (MB-02); cited as: MB-02 [1]; Crossref lists only the first author; full list from Europe PMC and rrnDB}
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
  note = {access: full_text (MB-01); type: peer reviewed; cited as: MB-01 2013}
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
  note = {access: full_text (MB-01); type: peer reviewed; cited as: MB-01 2016}
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

@article{kozichDevelopmentDualindexSequencing2013,
  author = {Kozich, James J. and Westcott, Sarah L. and Baxter, Nielson T. and Highlander, Sarah K. and Schloss, Patrick D.},
  title = {Development of a dual-index sequencing strategy and curation pipeline for analyzing amplicon sequence data on the MiSeq Illumina sequencing platform},
  journal = {Applied and Environmental Microbiology},
  year = {2013},
  volume = {79},
  number = {17},
  pages = {5112-5120},
  doi = {10.1128/AEM.01043-13},
  note = {access: full_text (critic MB-01:C-073..C-076: could not be confirmed as open full text) (MB-01); type: peer reviewed; cited as: MB-01 2013}
}

@article{kumarAnalysisCorrectionCompositional2018,
  author = {Kumar, M. Senthil and Slud, Eric V. and Okrah, Kwame and Hicks, Stephanie C. and Hannenhalli, Sridhar and Corrada Bravo, Héctor},
  title = {Analysis and correction of compositional bias in sparse sequencing count data},
  journal = {BMC Genomics},
  year = {2018},
  volume = {19},
  pages = {799},
  doi = {10.1186/s12864-018-5160-5},
  note = {access: abstract_only (MB-01); type: peer reviewed; cited as: MB-01 2018}
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
  note = {access: abstract_only (MB-02), not_obtained (MB-01); cited as: MB-02 [81], MB-01 Kunin 2010}
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
  note = {access: full_text (MB-01); type: peer reviewed; cited as: MB-01 2012}
}

@article{lauberEffectStorageConditions2010,
  author = {Lauber, Christian L. and Zhou, Nicholas and Gordon, Jeffrey I. and Knight, Rob and Fierer, Noah},
  title = {Effect of storage conditions on the assessment of bacterial community structure in soil and human-associated samples},
  journal = {FEMS Microbiology Letters},
  year = {2010},
  volume = {307},
  number = {1},
  pages = {80-86},
  doi = {10.1111/j.1574-6968.2010.01965.x},
  note = {access: not_obtained (MB-01); cited as: MB-01 Lauber 2010; known only through Rubin 2013 (SEC)}
}

@article{laursenGenomicGCcontentAffects2017,
  author = {Laursen, Martin F. and Dalgaard, Marlene D. and Bahl, Martin I.},
  title = {Genomic GC-content affects the accuracy of 16S rRNA gene sequencing based microbial profiling due to PCR bias},
  journal = {Frontiers in Microbiology},
  year = {2017},
  volume = {8},
  pages = {1934},
  doi = {10.3389/fmicb.2017.01934},
  note = {access: full_text (MB-01); type: peer reviewed; cited as: MB-01 2017; MB-01 also says: corrigendum 2022}
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

@article{leeRrnDBDocumentingNumber2009,
  author = {Lee, Zarraz M.-P. and Bussema, III, Carl and Schmidt, Thomas M.},
  title = {rrnDB: documenting the number of rRNA and tRNA genes in bacteria and archaea},
  journal = {Nucleic Acids Research},
  year = {2009},
  volume = {37},
  number = {Database issue},
  pages = {D489-D493},
  doi = {10.1093/nar/gkn689},
  note = {access: abstract_only (MB-02); cited as: MB-02 [2]; critic MB-02:C-096: Crossref gives C. Bussema without the suffix III}
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
  note = {access: full_text (MB-01), abstract_only (MB-02); type: peer reviewed; cited as: MB-01 2018, MB-02 [78]}
}

@article{linAnalysisCompositionsMicrobiomes2020,
  author = {Lin, Huang and Peddada, Shyamal Das},
  title = {Analysis of compositions of microbiomes with bias correction},
  journal = {Nature Communications},
  year = {2020},
  volume = {11},
  pages = {3514},
  doi = {10.1038/s41467-020-17041-7},
  note = {access: abstract_only (MB-01); type: peer reviewed; cited as: MB-01 2020; MB-01 also says: makers' claims}
}

@article{lingBatchEffectsRemoval2022,
  author = {Ling, Wodan and Lu, Jiuyao and Zhao, Ni and Lulla, Anju and Plantinga, Anna M. and Fu, Weijia and Zhang, Angela and Liu, Hongjiao and Song, Hoseung and Li, Zhigang and Chen, Jun and Randolph, Timothy W. and Koay, Wei Li A. and White, James R. and Launer, Lenore J. and Fodor, Anthony A. and Meyer, Katie A. and Wu, Michael C.},
  title = {Batch effects removal for microbiome data via conditional quantile regression},
  journal = {Nature Communications},
  year = {2022},
  volume = {13},
  pages = {5418},
  doi = {10.1038/s41467-022-33071-9},
  note = {access: abstract_only (MB-01); type: peer reviewed; cited as: MB-01 2022; MB-01 also says: makers' claims}
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
  note = {access: full_text (critic MB-01:C-073..C-076: could not be confirmed as open full text) (MB-01); type: peer reviewed; cited as: MB-01 2019; MB-01 also says: DOI checked by the synthesis agent}
}

@article{llorensricoBenchmarkingMicrobiomeTransformations2021,
  author = {Lloréns-Rico, Verónica and Vieira-Silva, Sara and Gonçalves, Pedro J. and Falony, Gwen and Raes, Jeroen},
  title = {Benchmarking microbiome transformations favors experimental quantitative approaches to address compositionality and sampling depth biases},
  journal = {Nature Communications},
  year = {2021},
  volume = {12},
  pages = {3562},
  doi = {10.1038/s41467-021-23821-6},
  note = {access: full_text (MB-01); type: peer reviewed; cited as: MB-01 2021}
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

@article{loucaCorrecting16SRRNA2018,
  author = {Louca, Stilianos and Doebeli, Michael and Parfrey, Laura Wegener},
  title = {Correcting for 16S rRNA gene copy numbers in microbiome surveys remains an unsolved problem},
  journal = {Microbiome},
  year = {2018},
  volume = {6},
  pages = {41},
  doi = {10.1186/s40168-018-0420-9},
  note = {access: full_text (MB-01), full_text (MB-02); type: peer reviewed; cited as: MB-01 2018, MB-02 [30]}
}

@article{loveModeratedEstimationFold2014,
  author = {Love, Michael I. and Huber, Wolfgang and Anders, Simon},
  title = {Moderated estimation of fold change and dispersion for RNA-seq data with DESeq2},
  journal = {Genome Biology},
  year = {2014},
  volume = {15},
  number = {12},
  pages = {550},
  doi = {10.1186/s13059-014-0550-8},
  note = {access: not_obtained (MB-01); cited as: MB-01 Love 2014 (DESeq2)}
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
  note = {access: abstract_only (MB-01); type: peer reviewed; cited as: MB-01 2013; MB-01 also says: makers' claims}
}

@article{lundinWhichSequencingDepth2012,
  author = {Lundin, Daniel and Severin, Ina and Logue, Jürg Brendan and Östman, Örjan and Andersson, Anders F. and Lindström, Eva S.},
  title = {Which sequencing depth is sufficient to describe patterns in bacterial alpha- and beta-diversity?},
  journal = {Environmental Microbiology Reports},
  year = {2012},
  volume = {4},
  number = {3},
  pages = {367-372},
  doi = {10.1111/j.1758-2229.2012.00345.x},
  note = {access: abstract_only (MB-01); type: peer reviewed; cited as: MB-01 2012}
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

@article{mandalAnalysisCompositionMicrobiomes2015,
  author = {Mandal, Siddhartha and Van Treuren, Will and White, Richard A. and Eggesbø, Merete and Knight, Rob and Peddada, Shyamal D.},
  title = {Analysis of composition of microbiomes: a novel method for studying microbial composition},
  journal = {Microbial Ecology in Health and Disease},
  year = {2015},
  volume = {26},
  pages = {27663},
  doi = {10.3402/mehd.v26.27663},
  note = {access: abstract_only (MB-01); type: peer reviewed; cited as: MB-01 2015; MB-01 also says: makers' claims}
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
  note = {access: full_text (MB-01); type: peer reviewed; cited as: MB-01 2008}
}

@article{marizzoniComparisonBioinformaticsPipelines2020,
  author = {Marizzoni, Moira and Gurry, Thomas and Provasi, Stefania and Greub, Gilbert and Lopizzo, Nicola and Ribaldi, Federica and Festari, Cristina and Mazzelli, Monica and Mombelli, Elisa and Salvatore, Marco and Mirabelli, Peppino and Franzese, Monica and Soricelli, Andrea and Frisoni, Giovanni B. and Cattaneo, Annamaria},
  title = {Comparison of bioinformatics pipelines and operating systems for the analyses of 16S rRNA gene amplicon sequences in human fecal samples},
  journal = {Frontiers in Microbiology},
  year = {2020},
  volume = {11},
  pages = {1262},
  doi = {10.3389/fmicb.2020.01262},
  note = {access: full_text (MB-01); type: peer reviewed; cited as: MB-01 2020}
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
  note = {access: abstract_only (critic MB-01:C-080: an open PMC copy exists) (MB-01); type: peer reviewed; cited as: MB-01 2019}
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
  note = {access: abstract_only (MB-01); type: peer reviewed; cited as: MB-01 2001}
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
  note = {access: abstract_only (MB-01); type: peer reviewed; cited as: MB-01 2020; MB-01 also says: makers' claims}
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
  note = {access: abstract_only (MB-01); type: peer reviewed; cited as: MB-01 2019}
}

@article{mclarenConsistentCorrectableBias2019,
  author = {McLaren, Michael R. and Willis, Amy D. and Callahan, Benjamin J.},
  title = {Consistent and correctable bias in metagenomic sequencing experiments},
  journal = {eLife},
  year = {2019},
  volume = {8},
  pages = {e46923},
  doi = {10.7554/eLife.46923},
  note = {access: full_text (re-opened by the synthesis agent) (MB-01), abstract_only (MB-02); type: peer reviewed; cited as: MB-01 2019, MB-02 [35]}
}

@misc{mclarenImplicationsTaxonomicBias2022,
  author = {McLaren, Michael R. and Nearing, Jacob T. and Willis, Amy D. and Lloyd, Karen G. and Callahan, Benjamin J.},
  title = {Implications of taxonomic bias for microbial differential-abundance analysis},
  howpublished = {bioRxiv},
  year = {2022},
  number = {2022.08.19.504330},
  doi = {10.1101/2022.08.19.504330},
  note = {access: abstract_only (MB-01); type: preprint; cited as: MB-01 2022}
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
  note = {access: full_text (MB-01); type: peer reviewed; cited as: MB-01 2014}
}

@misc{miloBioNumbersEntry1023602010,
  author = {Milo, Ron and Jorgensen, Paul and Moran, Uri and Weber, Griffin and Springer, Michael},
  title = {BioNumbers entry 102360, Average number of rRNA genes per genome, citing H. Bremer and P. P. Dennis (1996), ch. 97, Table 3},
  journal = {Nucleic Acids Research},
  year = {2010},
  volume = {38},
  number = {suppl_1},
  pages = {D750-D753},
  doi = {10.1093/nar/gkp889},
  url = {https://bionumbers.hms.harvard.edu/bionumber.aspx?id=102360},
  note = {access: secondary (MB-02); cited as: MB-02 [21]; database paper: BioNumbers - the database of key numbers in molecular and cell biology}
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
  note = {access: full_text (MB-01); type: peer reviewed; cited as: MB-01 2019}
}

@article{mortonEstablishingMicrobialComposition2019,
  author = {Morton, James T. and Marotz, Clarisse and Washburne, Alex and Silverman, Justin and Zaramela, Livia S. and Edlund, Anna and Zengler, Karsten and Knight, Rob},
  title = {Establishing microbial composition measurement standards with reference frames},
  journal = {Nature Communications},
  year = {2019},
  volume = {10},
  pages = {2719},
  doi = {10.1038/s41467-019-10656-5},
  note = {access: abstract_only (MB-01); type: peer reviewed; cited as: MB-01 2019}
}

@article{muraliIDTAXANovelApproach2018,
  author = {Murali, Adithya and Bhargava, Aniruddha and Wright, Erik S.},
  title = {IDTAXA: a novel approach for accurate taxonomic classification of microbiome sequences},
  journal = {Microbiome},
  year = {2018},
  volume = {6},
  pages = {140},
  doi = {10.1186/s40168-018-0521-5},
  note = {access: full_text (MB-01); type: peer reviewed; cited as: MB-01 2018; MB-01 also says: developer claims}
}

@article{nearingDenoisingDenoisersIndependent2018,
  author = {Nearing, Jacob T. and Douglas, Gavin M. and Comeau, André M. and Langille, Morgan G. I.},
  title = {Denoising the Denoisers: an independent evaluation of microbiome sequence error-correction approaches},
  journal = {PeerJ},
  year = {2018},
  volume = {6},
  pages = {e5364},
  doi = {10.7717/peerj.5364},
  note = {access: full_text (MB-01); type: peer reviewed; cited as: MB-01 2018}
}

@article{nearingMicrobiomeDifferentialAbundance2022,
  author = {Nearing, Jacob T. and Douglas, Gavin M. and Hayes, Molly G. and MacDonald, Jocelyn and Desai, Dhwani K. and Allward, Nicole and Jones, Casey M. A. and Wright, Robyn J. and Dhanani, Akhilesh S. and Comeau, André M. and Langille, Morgan G. I.},
  title = {Microbiome differential abundance methods produce different results across 38 datasets},
  journal = {Nature Communications},
  year = {2022},
  volume = {13},
  pages = {342},
  doi = {10.1038/s41467-022-28034-z},
  note = {access: full_text (MB-01); type: peer reviewed; cited as: MB-01 2022}
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
  note = {access: full_text (MB-01); type: peer reviewed; cited as: MB-01 2016}
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
  note = {access: full_text (critic MB-02:C-084: figures could not be verified) (MB-02); cited as: MB-02 [62]}
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
  note = {access: full_text (first 100,000 characters) (MB-02); cited as: MB-02 [51]}
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
  note = {access: abstract_only (MB-01); type: peer reviewed; cited as: MB-01 2016}
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

@article{paulsonDifferentialAbundanceAnalysis2013,
  author = {Paulson, Joseph N. and Stine, O. Colin and Corrada Bravo, Héctor and Pop, Mihai},
  title = {Differential abundance analysis for microbial marker-gene surveys},
  journal = {Nature Methods},
  year = {2013},
  volume = {10},
  number = {12},
  pages = {1200-1202},
  doi = {10.1038/nmeth.2658},
  note = {access: not_obtained (MB-01); cited as: MB-01 Paulson 2013; Europe PMC abstract only (read); full text not obtained}
}

@article{pauvertBioinformaticsMattersAccuracy2019,
  author = {Pauvert, Charlie and Buée, Marc and Laval, Valérie and Edel-Hermann, Véronique and Fauchery, Laure and Gautier, Angélique and Lesur, Isabelle and Vallance, Jessica and Vacher, Corinne},
  title = {Bioinformatics matters: the accuracy of plant and soil fungal community data is highly dependent on the metabarcoding pipeline},
  journal = {Fungal Ecology},
  year = {2019},
  volume = {41},
  pages = {23-33},
  doi = {10.1016/j.funeco.2019.03.005},
  note = {access: not_obtained (MB-01); cited as: MB-01 Pauvert 2019}
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

@article{peltoElementaryMethodsProvide2025,
  author = {Pelto, Juho and Auranen, Kari and Kujala, Janne V. and Lahti, Leo},
  title = {Elementary methods provide more replicable results in microbial differential abundance analysis},
  journal = {Briefings in Bioinformatics},
  year = {2025},
  volume = {26},
  number = {2},
  pages = {bbaf130},
  doi = {10.1093/bib/bbaf130},
  note = {access: abstract_only (MB-01); type: peer reviewed; cited as: MB-01 2025; MB-01 also says: DOI checked by the synthesis agent}
}

@article{pentonSizeMattersAssessing2016,
  author = {Penton, C. Ryan and Gupta, Vadakattu V. S. R. and Yu, Julian and Tiedje, James M.},
  title = {Size matters: assessing optimum soil sample size for fungal and bacterial community structure analyses using high throughput sequencing of rRNA gene amplicons},
  journal = {Frontiers in Microbiology},
  year = {2016},
  volume = {7},
  pages = {824},
  doi = {10.3389/fmicb.2016.00824},
  note = {access: full_text (MB-01); type: peer reviewed; cited as: MB-01 2016}
}

@article{pereiraComparisonNormalizationMethods2018,
  author = {Buongermino Pereira, Mariana and Wallroth, Mikael and Jonsson, Viktor and Kristiansson, Erik},
  title = {Comparison of normalization methods for the analysis of metagenomic gene abundance data},
  journal = {BMC Genomics},
  year = {2018},
  volume = {19},
  pages = {274},
  doi = {10.1186/s12864-018-4637-6},
  note = {access: abstract_only (MB-01); type: peer reviewed; cited as: MB-01 2018}
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

@article{pintoPCRBiasesDistort2012,
  author = {Pinto, Ameet J. and Raskin, Lutgarde},
  title = {PCR biases distort bacterial and archaeal community structure in pyrosequencing datasets},
  journal = {PLOS ONE},
  year = {2012},
  volume = {7},
  number = {8},
  pages = {e43093},
  doi = {10.1371/journal.pone.0043093},
  note = {access: full_text (MB-01); type: peer reviewed; cited as: MB-01 2012}
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
  note = {access: abstract_only (MB-01); type: peer reviewed; cited as: MB-01 1998}
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
  note = {access: full_text (MB-01); type: peer reviewed; cited as: MB-01 2020}
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
  note = {access: abstract_only (MB-01), abstract_only (MB-02); type: peer reviewed; cited as: MB-01 2017, MB-02 [83]}
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

@incollection{rabinowitzSevenFormsRarity1981,
  author = {Rabinowitz, Deborah},
  title = {Seven forms of rarity},
  booktitle = {The Biological Aspects of Rare Plant Conservation},
  editor = {Synge, H.},
  publisher = {Wiley},
  year = {1981},
  pages = {205-217},
  note = {access: not_obtained (MB-02); cited as: MB-02 Rabinowitz 1981; used only as described in Jousset et al. 2017 (secondary)}
}

@article{ramirezDetectingMacroecologicalPatterns2017,
  author = {Ramirez, Kelly S. and others},
  journal = {Nature Microbiology},
  year = {2018},
  volume = {3},
  number = {2},
  pages = {189-196},
  doi = {10.1038/s41564-017-0062-x},
  note = {access: abstract_only (MB-02); cited as: MB-02 [65]; the note lists it as not used in the body (search record only); incomplete: author, title}
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
  note = {access: full_text (MB-01); type: peer reviewed; cited as: MB-01 2021; MB-01 also says: DOI checked by the synthesis agent}
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

@article{robinsonScalingNormalizationMethod2010,
  author = {Robinson, Mark D. and Oshlack, Alicia},
  title = {A scaling normalization method for differential expression analysis of RNA-seq data},
  journal = {Genome Biology},
  year = {2010},
  volume = {11},
  number = {3},
  pages = {R25},
  doi = {10.1186/gb-2010-11-3-r25},
  note = {access: abstract_only (MB-01); type: peer reviewed; cited as: MB-01 2010}
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

@article{rollerExploitingRRNAOperon2016,
  author = {Roller, Benjamin R. K. and Stoddard, Steven F. and Schmidt, Thomas M.},
  title = {Exploiting rRNA operon copy number to investigate bacterial reproductive strategies},
  journal = {Nature Microbiology},
  year = {2016},
  volume = {1},
  number = {11},
  pages = {16160},
  doi = {10.1038/nmicrobiol.2016.160},
  note = {access: abstract_only (MB-01), abstract_only (MB-02); type: peer reviewed; cited as: MB-01 2016, MB-02 [10]}
}

@misc{rrndbRrnDBCurrentRelease,
  author = {{rrnDB}},
  title = {rrnDB current release statistics},
  url = {https://rrndb.umms.med.umich.edu/},
  note = {access: not_obtained (MB-01); WebFetch failed with TLS certificate error; incomplete: author, year}
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
  note = {access: full_text (MB-01); type: peer reviewed; cited as: MB-01 2013}
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

@article{salterReagentLaboratoryContamination2014,
  author = {Salter, Susannah J. and Cox, Michael J. and Turek, Elena M. and Calus, Szymon T. and Cookson, William O. and Moffatt, Miriam F. and Turner, Paul and Parkhill, Julian and Loman, Nicholas J. and Walker, Alan W.},
  title = {Reagent and laboratory contamination can critically impact sequence-based microbiome analyses},
  journal = {BMC Biology},
  year = {2014},
  volume = {12},
  pages = {87},
  doi = {10.1186/s12915-014-0087-z},
  note = {access: full_text (MB-01); type: peer reviewed; cited as: MB-01 2014}
}

@article{sandersMarineBenthicDiversity1968,
  author = {Sanders, Howard L.},
  title = {Marine benthic diversity: a comparative study},
  journal = {The American Naturalist},
  year = {1968},
  volume = {102},
  number = {925},
  pages = {243-282},
  doi = {10.1086/282541},
  note = {access: not_obtained (MB-01); cited as: MB-01 Sanders 1968; known only secondarily via Chao and Jost 2012 and Willis 2019}
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
  note = {access: full_text (MB-01); type: peer reviewed; cited as: MB-01 2015}
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
  note = {access: full_text (MB-01); type: peer reviewed; cited as: MB-01 2021}
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
  note = {access: full_text (re-opened by the synthesis agent) (MB-01); type: peer reviewed; cited as: MB-01 2024b; MB-01 also says: DOI checked}
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
  note = {access: full_text (MB-01); type: peer reviewed; cited as: MB-01 2024a}
}

@misc{schmidtlaboratoryRrnDBReleaseFiles2025,
  author = {{Schmidt Laboratory, University of Michigan}},
  title = {rrnDB release files v3.1.227, v4.4.3, v5.0, v5.6 and v5.10 (v5.10 dated 6 June 2025), and About page},
  year = {2025},
  url = {https://rrndb.umms.med.umich.edu/static/download/},
  note = {access: full_text (MB-02); cited as: MB-02 [4]; accessed 2026-10-20; statistics derived by the reviewer}
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
  note = {access: abstract_only (MB-01); type: peer reviewed; cited as: MB-01 2015}
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

@article{shadeConditionallyRareTaxa2014,
  author = {Shade, Ashley and Jones, Stuart E. and Caporaso, J. Gregory and Handelsman, Jo and Knight, Rob and Fierer, Noah and Gilbert, Jack A.},
  title = {Conditionally rare taxa disproportionately contribute to temporal changes in microbial diversity},
  journal = {mBio},
  year = {2014},
  volume = {5},
  number = {4},
  pages = {e01371-14},
  doi = {10.1128/mBio.01371-14},
  note = {access: full_text (excerpts) (MB-02); cited as: MB-02 [45]}
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
  note = {access: abstract_only (MB-01); type: peer reviewed; cited as: MB-01 2023}
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
  note = {access: abstract_only (per lab angle) (MB-01), abstract_only (MB-02), not_obtained (MB-01); type: peer reviewed; cited as: MB-01 2017, MB-02 [70]; MB-01 lists it both in its references (abstract only per lab angle) and in Sources not obtained; MB-01 also says: DOI checked by the synthesis agent}
}

@article{silvermanDynamicLinearModels2018,
  author = {Silverman, Justin D. and Durand, Heather K. and Bloom, Rachael J. and Mukherjee, Sayan and David, Lawrence A.},
  title = {Dynamic linear models guide design and analysis of microbiota studies within artificial human guts},
  journal = {Microbiome},
  year = {2018},
  volume = {6},
  pages = {202},
  doi = {10.1186/s40168-018-0584-3},
  note = {access: full_text (MB-01); type: peer reviewed; cited as: MB-01 2018; MB-01 also says: DOI checked by the synthesis agent}
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
  note = {access: full_text (MB-01); type: peer reviewed; cited as: MB-01 2021; MB-01 also says: DOI checked by the synthesis agent}
}

@article{silvermanNaughtAllZeros2020,
  author = {Silverman, Justin D. and Roche, Kimberly and Mukherjee, Sayan and David, Lawrence A.},
  title = {Naught all zeros in sequence count data are the same},
  journal = {Computational and Structural Biotechnology Journal},
  year = {2020},
  volume = {18},
  pages = {2789-2798},
  doi = {10.1016/j.csbj.2020.09.014},
  note = {access: abstract_only (MB-01); type: peer reviewed; cited as: MB-01 2020}
}

@misc{simberloff1972,
  author = {Simberloff},
  year = {1972},
  note = {access: secondary (MB-01); cited as: MB-01 Simberloff 1972; known only through Chao and Jost 2012; incomplete: given name, title, venue, doi}
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
  note = {access: full_text (per bioinformatics angle) (MB-01); type: peer reviewed; cited as: MB-01 2017; critic MB-01:C-094: Crossref lists the consortium first; the note placed it after Siyuan Ma}
}

@misc{sinhaIndexSwitchingCauses2017,
  author = {Sinha, Rahul and Stanley, Geoff and Gulati, Gunsagar S. and Ezran, Camille and Travaglini, Kyle J. and Wei, Eric and Chan, Charles K. F. and Nabhan, Ahmad N. and Su, Tianying and Morganti, Rachel M. and Conley, Stephanie D. and Chaib, Hassan and Red-Horse, Kristy and Longaker, Michael T. and Snyder, Michael P. and Krasnow, Mark A. and Weissman, Irving L.},
  title = {Index switching causes 'spreading-of-signal' among multiplexed samples in Illumina HiSeq 4000 DNA sequencing},
  howpublished = {bioRxiv},
  year = {2017},
  number = {125724},
  doi = {10.1101/125724},
  note = {access: not_obtained (MB-01); cited as: MB-01 Sinha (Rahul) 2017}
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
  note = {access: abstract_only (MB-01); type: peer reviewed; cited as: MB-01 2007}
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

@article{smetsMethodSimultaneousMeasurement2016,
  author = {Smets, Wenke and Leff, Jonathan W. and Bradford, Mark A. and McCulley, Rebecca L. and Lebeer, Sarah and Fierer, Noah},
  title = {A method for simultaneous measurement of soil bacterial abundances and community composition via 16S rRNA gene sequencing},
  journal = {Soil Biology and Biochemistry},
  year = {2016},
  volume = {96},
  pages = {145-151},
  doi = {10.1016/j.soilbio.2016.02.003},
  note = {access: abstract_only (per lab angle) (MB-01), not_obtained (MB-01); type: peer reviewed; cited as: MB-01 2016; MB-01 lists it both in its references (abstract only per lab angle) and in Sources not obtained}
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
  note = {access: full_text (MB-01); type: peer reviewed; cited as: MB-01 2014; MB-01 also says: INDIRECT, ITS}
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

@article{songPreservationMethodsDiffer2016,
  author = {Song, Se Jin and Amir, Amnon and Metcalf, Jessica L. and Amato, Katherine R. and Xu, Zhenjiang Zech and Humphrey, Greg and Knight, Rob},
  title = {Preservation methods differ in fecal microbiome stability, affecting suitability for field studies},
  journal = {mSystems},
  year = {2016},
  volume = {1},
  number = {3},
  pages = {e00021-16},
  doi = {10.1128/mSystems.00021-16},
  note = {access: full_text (MB-01); type: peer reviewed; cited as: MB-01 2016}
}

@article{soppaPolyploidyCommunityStructure2017,
  author = {Soppa, Jörg},
  title = {Polyploidy and community structure},
  journal = {Nature Microbiology},
  year = {2017},
  volume = {2},
  pages = {16261},
  doi = {10.1038/nmicrobiol.2016.261},
  note = {access: not_obtained (MB-02); cited as: MB-02 Soppa 2017}
}

@article{stammlerAdjustingMicrobiomeProfiles2016,
  author = {Stämmler, Frank and Gläsner, Joachim and Hiergeist, Andreas and Holler, Ernst and Weber, Daniela and Oefner, Peter J. and Gessner, André and Spang, Rainer},
  title = {Adjusting microbiome profiles for differences in microbial load by spike-in bacteria},
  journal = {Microbiome},
  year = {2016},
  volume = {4},
  pages = {28},
  doi = {10.1186/s40168-016-0175-0},
  note = {access: full_text (per lab angle) (MB-01); type: peer reviewed; cited as: MB-01 2016}
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
  note = {access: full_text (MB-01), full_text (MB-02); type: peer reviewed; cited as: MB-01 2021, MB-02 [32]}
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
  note = {access: full_text (MB-01), full_text (MB-02); type: peer reviewed database paper; cited as: MB-01 2015, MB-02 [3]}
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

@article{straubInterpretationsEnvironmentalMicrobial2020,
  author = {Straub, Daniel and Blackwell, Nia and Langarica-Fuentes, Adrian and Peltzer, Alexander and Nahnsen, Sven and Kleindienst, Sara},
  title = {Interpretations of environmental microbial community studies are biased by the selected 16S rRNA (gene) amplicon sequencing pipeline},
  journal = {Frontiers in Microbiology},
  year = {2020},
  volume = {11},
  pages = {550420},
  doi = {10.3389/fmicb.2020.550420},
  note = {access: full_text (MB-01); type: peer reviewed; cited as: MB-01 2020}
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

@article{suzukiBiasCausedTemplate1996,
  author = {Suzuki, Marcelino T. and Giovannoni, Stephen J.},
  title = {Bias caused by template annealing in the amplification of mixtures of 16S rRNA genes by PCR},
  journal = {Applied and Environmental Microbiology},
  year = {1996},
  volume = {62},
  number = {2},
  pages = {625-630},
  doi = {10.1128/aem.62.2.625-630.1996},
  note = {access: abstract_only (MB-01); type: peer reviewed; cited as: MB-01 1996}
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
  note = {access: full_text (re-opened by the synthesis agent) (MB-01); type: peer reviewed; cited as: MB-01 2019}
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
  note = {access: full_text (MB-01); type: peer reviewed; cited as: MB-01 2017; author list truncated at the consortium (critic MB-01:C-095..C-097: Crossref lists several hundred consortium members); incomplete: author}
}

@article{thorsenLargescaleBenchmarkingReveals2016,
  author = {Thorsen, Jonathan and Brejnrod, Asker and Mortensen, Martin and Rasmussen, Morten A. and Stokholm, Jakob and Abu Al-Soud, Waleed and Sørensen, Søren and Bisgaard, Hans and Waage, Johannes},
  title = {Large-scale benchmarking reveals false discoveries and count transformation sensitivity in 16S rRNA gene amplicon data analysis methods used in microbiome studies},
  journal = {Microbiome},
  year = {2016},
  volume = {4},
  pages = {62},
  doi = {10.1186/s40168-016-0208-8},
  note = {access: abstract_only (MB-01); type: peer reviewed; cited as: MB-01 2016}
}

@article{tkaczAbsoluteQuantitationMicrobiota2018,
  author = {Tkacz, Andrzej and Hortala, Marion and Poole, Philip S.},
  title = {Absolute quantitation of microbiota abundance in environmental samples},
  journal = {Microbiome},
  year = {2018},
  volume = {6},
  pages = {110},
  doi = {10.1186/s40168-018-0491-7},
  note = {access: full_text (per lab angle) (MB-01); type: peer reviewed; cited as: MB-01 2018}
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
  note = {access: full_text (MB-01); type: peer reviewed; cited as: MB-01 2017}
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
  note = {access: abstract_only (MB-01); type: peer reviewed; cited as: MB-01 2017}
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
  note = {access: abstract_only (MB-02); cited as: MB-02 [24]}
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
  note = {access: full_text (MB-01), full_text (MB-02); type: peer reviewed; cited as: MB-01 2013, MB-02 [6]}
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
  note = {access: full_text (MB-01); type: peer reviewed; cited as: MB-01 2016}
}

@article{waltersLargescaleReplicatedField2018,
  author = {Walters, William A. and Jin, Zhao and Youngblut, Nicholas and Wallace, Jason G. and Sutter, Jessica and Zhang, Wei and González-Peña, Antonio and Peiffer, Jason and Koren, Omry and Shi, Qiaojuan and Knight, Rob and del Rio, Tijana Glavina and Tringe, Susannah G. and Buckler, Edward S. and Dangl, Jeffery L. and Ley, Ruth E.},
  title = {Large-scale replicated field study of maize rhizosphere identifies heritable microbes},
  journal = {PNAS},
  year = {2018},
  volume = {115},
  number = {28},
  pages = {7368-7373},
  doi = {10.1073/pnas.1800918115},
  note = {access: abstract_only (MB-02); cited as: MB-02 [75]}
}

@article{weissNormalizationMicrobialDifferential2017,
  author = {Weiss, Sophie and Xu, Zhenjiang Zech and Peddada, Shyamal and Amir, Amnon and Bittinger, Kyle and Gonzalez, Antonio and Lozupone, Catherine and Zaneveld, Jesse R. and Vázquez-Baeza, Yoshiki and Birmingham, Amanda and Hyde, Embriette R. and Knight, Rob},
  title = {Normalization and microbial differential abundance strategies depend upon data characteristics},
  journal = {Microbiome},
  year = {2017},
  volume = {5},
  pages = {27},
  doi = {10.1186/s40168-017-0237-y},
  note = {access: full_text (MB-01); type: peer reviewed; cited as: MB-01 2017}
}

@article{weissTrackingDownSources2014,
  author = {Weiss, Sophie and Amir, Amnon and Hyde, Embriette R. and Metcalf, Jessica L. and Song, Se Jin and Knight, Rob},
  title = {Tracking down the sources of experimental contamination in microbiome studies},
  journal = {Genome Biology},
  year = {2014},
  volume = {15},
  pages = {564},
  doi = {10.1186/s13059-014-0564-2},
  note = {access: not_obtained (MB-01); cited as: MB-01 Weiss 2014}
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
  note = {access: full_text (MB-01); type: peer reviewed; cited as: MB-01 2017}
}

@article{wesolowskaandersenChoiceBacterialDNA2014,
  author = {Wesolowska-Andersen, Agata and Bahl, Martin I. and Carvalho, Vera and Kristiansen, Karsten and Sicheritz-Ponten, Thomas and Gupta, Ramneek and Licht, Tine R.},
  title = {Choice of bacterial DNA extraction method from fecal material influences community structure as evaluated by metagenomic analysis},
  journal = {Microbiome},
  year = {2014},
  volume = {2},
  pages = {19},
  doi = {10.1186/2049-2618-2-19},
  note = {access: not_obtained (MB-01); cited as: MB-01 Wesolowska-Andersen 2014; full text retrieved but not searched; no findings extracted}
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
  note = {access: abstract_only (MB-01); type: peer reviewed; cited as: MB-01 2015; MB-01 also says: makers' claims}
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
  note = {access: abstract_only (MB-01); type: peer reviewed; cited as: MB-01 2022; MB-01 also says: makers' claims}
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
  note = {access: abstract_only (MB-01); type: peer reviewed; cited as: MB-01 2017; MB-01 also says: makers' claims}
}

@article{willisRarefactionAlphaDiversity2019,
  author = {Willis, Amy D.},
  title = {Rarefaction, alpha diversity, and statistics},
  journal = {Frontiers in Microbiology},
  year = {2019},
  volume = {10},
  pages = {2407},
  doi = {10.3389/fmicb.2019.02407},
  note = {access: full_text (MB-01); type: peer reviewed perspective; cited as: MB-01 2019}
}

@article{wirbelRealisticBenchmarkDifferential2024,
  author = {Wirbel, Jakob and Essex, Morgan and Forslund, Sofia Kirke and Zeller, Georg},
  title = {A realistic benchmark for differential abundance testing and confounder adjustment in human microbiome studies},
  journal = {Genome Biology},
  year = {2024},
  volume = {25},
  pages = {247},
  doi = {10.1186/s13059-024-03390-9},
  note = {access: full_text (MB-01); type: peer reviewed; cited as: MB-01 2024}
}

@article{wrightCorrelationsIncidenceAbundance1991,
  author = {Wright, David H.},
  title = {Correlations between incidence and abundance are expected by chance},
  journal = {Journal of Biogeography},
  year = {1991},
  volume = {18},
  number = {4},
  pages = {463-466},
  doi = {10.2307/2845487},
  note = {access: not_obtained (MB-02); cited as: MB-02 Wright 1991; critic MB-02:C-098: Crossref gives only the start page (463)}
}

@article{wrightQualityFilteringIllumina2016,
  author = {Wright, Erik Scott and Vetsigian, Kalin Horen},
  title = {Quality filtering of Illumina index reads mitigates sample cross-talk},
  journal = {BMC Genomics},
  year = {2016},
  volume = {17},
  pages = {876},
  doi = {10.1186/s12864-016-3217-x},
  note = {access: full_text (MB-01); type: peer reviewed; cited as: MB-01 2016}
}

@article{yangComprehensiveEvaluationMicrobial2022,
  author = {Yang, Lu and Chen, Jun},
  title = {A comprehensive evaluation of microbial differential abundance analysis methods: current status and potential solutions},
  journal = {Microbiome},
  year = {2022},
  volume = {10},
  pages = {130},
  doi = {10.1186/s40168-022-01320-0},
  note = {access: full_text (MB-01); type: peer reviewed; cited as: MB-01 2022}
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
  note = {access: full_text (MB-01); type: peer reviewed; cited as: MB-01 2018}
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
  note = {access: full_text (MB-01); type: peer reviewed; cited as: MB-01 2020}
}

@article{zengIdentifyingBiogeographicPatterns2021,
  author = {Zeng, Quanchao and An, Shaoshan},
  title = {Identifying the biogeographic patterns of rare and abundant bacterial communities using different primer sets on the Loess Plateau},
  journal = {Microorganisms},
  year = {2021},
  volume = {9},
  number = {1},
  pages = {139},
  doi = {10.3390/microorganisms9010139},
  note = {access: abstract_only (MB-02); cited as: MB-02 [59]}
}

@article{zerullaPloidyLevelSynechocystis2016,
  author = {Zerulla, Karolin and Ludt, Katharina and Soppa, Jörg},
  title = {The ploidy level of Synechocystis sp. PCC 6803 is highly variable and is influenced by growth phase and by chemical and physical external parameters},
  journal = {Microbiology},
  year = {2016},
  volume = {162},
  number = {5},
  pages = {730-739},
  doi = {10.1099/mic.0.000264},
  note = {access: abstract_only (MB-02); cited as: MB-02 [17]}
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

@article{zhouRandomSamplingProcess2013,
  author = {Zhou, Jizhong and Jiang, Yi-Huei and Deng, Ye and Shi, Zhou and Zhou, Benjamin Yamin and Xue, Kai and Wu, Liyou and He, Zhili and Yang, Yunfeng},
  title = {Random sampling process leads to overestimation of beta-diversity of microbial communities},
  journal = {mBio},
  year = {2013},
  volume = {4},
  number = {3},
  pages = {e00324-13},
  doi = {10.1128/mBio.00324-13},
  note = {access: full_text (MB-01); type: peer reviewed; cited as: MB-01 2013}
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
  note = {access: abstract_only (critic: MB-01:C-075; the note said full_text, per statistics and bioinformatics angles) (MB-01), abstract_only (MB-02); type: peer reviewed; cited as: MB-01 2011, MB-02 [76]}
}

@misc{zymoZymoBIOMICSMicrobialCommunity,
  author = {{Zymo Research}},
  title = {ZymoBIOMICS Microbial Community Standard (product page)},
  url = {https://www.zymoresearch.com/products/zymobiomics-microbial-community-standard},
  note = {access: full_text (MB-01); type: documentation; cited as: MB-01 Zymo; accessed 2026-10-20; maker's claims; incomplete: year; not cited: named only in the access basis of answer D1}
}

@article{janda16SRRNAGene2007,
  author = {Janda, J. Michael and Abbott, Sharon L.},
  title = {16S rRNA Gene Sequencing for Bacterial Identification in the Diagnostic Laboratory: Pluses, Perils, and Pitfalls},
  journal = {Journal of Clinical Microbiology},
  year = {2007},
  volume = {45},
  number = {9},
  pages = {2761-2764},
  doi = {10.1128/JCM.01228-07},
  note = {background; access: full_text (PMC2045242), checked 2026-10-23; not from the inputs}
}

@article{bokulichMockrobiotaPublicResource2016,
  author = {Bokulich, Nicholas A. and Rideout, Jai Ram and Mercurio, William G. and Shiffer, Arron and Wolfe, Benjamin and Maurice, Corinne F. and Dutton, Rachel J. and Turnbaugh, Peter J. and Knight, Rob and Caporaso, J. Gregory},
  title = {mockrobiota: a Public Resource for Microbiome Bioinformatics Benchmarking},
  journal = {mSystems},
  year = {2016},
  volume = {1},
  number = {5},
  pages = {e00062-16},
  doi = {10.1128/mSystems.00062-16},
  note = {background; access: abstract (Europe PMC), checked 2026-10-23; not from the inputs}
}

@article{mcgillSpeciesAbundanceDistributions2007,
  author = {McGill, Brian J. and Etienne, Rampal S. and Gray, John S. and Alonso, David and Anderson, Marti J. and Benecha, Habtamu Kassa and Dornelas, Maria and Enquist, Brian J. and Green, Jessica L. and He, Fangliang and Hurlbert, Allen H. and Magurran, Anne E. and Marquet, Pablo A. and Maurer, Brian A. and Ostling, Annette and Soykan, Candan U. and Ugland, Karl I. and White, Ethan P.},
  title = {Species abundance distributions: moving beyond single prediction theories to integration within an ecological framework},
  journal = {Ecology Letters},
  year = {2007},
  volume = {10},
  number = {10},
  pages = {995-1015},
  doi = {10.1111/j.1461-0248.2007.01094.x},
  note = {background; access: abstract (Crossref), checked 2026-10-23; not from the inputs}
}
```
