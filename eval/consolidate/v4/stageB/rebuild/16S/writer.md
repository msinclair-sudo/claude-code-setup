# 16S amplicon sequencing from sample to count table: writer's view

> [!abstract] About this view
> What the research found, for writing from. Each claim gives who found it, the setting it holds for, the kind of evidence, its standing where the research stated one, and for an absence whether it was searched for. A claim with no standing given has none stated in the research; "limited by access" means a source was not read in full, which is not the same as weak evidence. Sources are listed at the end. The view is generated from the knowledge note `16S amplicon sequencing from sample to count table.md`, where every claim is checked against the research.

## What the research found, by question

### MB-01

**D1. What are the steps between a sample and a table of taxon counts, and which choices are made at each? Answer for each step separately: field sampling, preservation and storage; DNA extraction; choice of primers and gene region; PCR conditions, including cycle number; library preparation and sample indexing; sequencing platform and read length; demultiplexing; quality filtering and read merging; error correction or clustering into sequence variants or operational taxonomic units; chimera detection; taxonomic assignment, including classifiers and reference databases; contaminant and negative control handling.**

*Answer, as corrected by a second reader.* **D1: steps and choices**

The body supports the twelve-step description and the alternatives listed for each step. Most of it comes from full-text protocols, documentation and benchmarks; makers' statements are labelled as such. Two corrections. (1) The control-usage figure comes from Hornung 2019, which surveyed 265 papers in the 2018 issues of Microbiome and The ISME Journal that used any high-throughput community sequencing (16S, shotgun, metatranscriptomics, ITS, 18S and others): 30% (79) reported a negative control and 10% (27) a positive control. It is not a 16S-only figure, and it is SINGLE SOURCE. (2) The review contradicts itself about field sampling for water (volume, filter pore size) and host tissue. Section 2.1 says the lab angle searched these through Crossref, Europe PMC and web search; the Search record says no angle searched them. On the review's own record, these choices are unsearched, not 'not found'. How often each choice is made across the field is unmeasured apart from controls.

**D2. At each step in D1, how closely do counts track the sampled community, and what, if anything, departs them from it (for example extraction efficiency, primer mismatch, amplification efficiency, reannealing, 16S rRNA gene copy number, chimeras, index misassignment, sequencing error, clustering or denoising choices, classification error, contamination), by what mechanism and by how much? Report effects on relative abundance and on the number of taxa detected separately, and say for each source whether its effect has been measured as consistent across samples or as varying between them.**

*Answer, as corrected by a second reader.* **D2: departures per step, size and consistency**

Every mock-community study in the body found observed composition departing from known composition (replicated; full text). Departures are measured at most steps, but not at all of them. Field sampling for water and host tissue was not searched. Several choices showed little or no detectable effect: PCR replicate pooling, preparation day and lane, cycle number in some studies, and storage in one soil. For number of taxa detected, inflation by spurious sequences, chimeras, reagent contamination and pipeline choice is replicated across independent mocks and dilution series: 10 to 200-fold excess units (Straub 2020), contaminants rising from 0.1% to 80.1% of reads in a diluted mock (Karstens 2019). For relative abundance, the claim that extraction is the largest step, followed by PCR and then sequencing, rests on one 7-taxon vaginal dataset (Brooks 2015, reanalysed by McLaren 2019). It is contested by Fouhy 2016 (two extraction methods gave very similar data) and qualified by MBQC (specimen type mattered more than extraction). It should be presented as SINGLE DATASET, not as a field-wide ordering. Per-step magnitudes mostly come from one or two small mocks (7 to 20 taxa), often on 454. Consistency across samples: ratio-scale consistency is shown in one 16S cell-mixture dataset and one shotgun spike-in known only secondarily (Costea 2017 via McLaren). Variation between sample types or samples is shown by a field-versus-mock SAR11 bias for the 515F-Y/806R pair (Parada 2016, abstract only), inconsistent cycle effects in four stool samples (Sze and Schloss 2019), extraction yield of 40 to 84% (Zemb 2020) and a 66.7-fold spike-in range (Zhou 2011, abstract). Correction: McLaren's calibration result (Bray-Curtis error from 0.35 to 0.08, 92.6% lower mean squared error) comes from the Brooks 16S cell mixtures, not from a shotgun dataset. Overall: strong qualitatively; moderate for the inflation of taxon counts; weak for per-step relative-abundance magnitudes and for consistency across samples.

**D3. What values of the quantities in this workflow have been measured or reported: PCR cycle numbers and per-cycle amplification efficiencies; the distribution of 16S rRNA gene copy numbers across bacteria and archaea, and in communities from soil, water and hosts, each separately; reads per sample on commonly used platforms, and how much read numbers vary between samples within one sequencing run; the shape of taxon abundance distributions in communities from soil, water and hosts, each separately?**

*Answer, as corrected by a second reader.* **D3: measured values**

The body supports the values given: documented cycle numbers (the EMP protocol's 35 cycles in triplicate and 240 ng pooling were checked on the live page), copy-number ranges across genomes, per-study and per-run read ranges, and microbial-load ranges. Caveats. (1) Environment-level copy numbers (ACN about 2.2 for free-living and plant-associated samples, about 3.4 for animal-associated, soil lowest) are predictions from one source (Thompson 2017); the review flags this. (2) Abundance-distribution shapes split by environment are weaker than presented. The soil 'exponential or inverse gamma' best fits are in Zhou 2013's supplementary Table S3; the main text does not state them and they were not verified. The 'water and hosts' item is a single study (Kembel 2012) that pools ocean and skin into one item; the same paper's simulations assumed a lognormal. Haegeman 2013's Brazil-soil figures rest on a full text that was not openly retrievable. Absent: measured community copy number, a within-run read-count coefficient of variation, absolute per-cycle efficiencies, and per-environment abundance-distribution shapes for water and for host samples.

**D4. Which processes generate the read count of each taxon in a sample, and how well do models describe them? Cover sampling from the pool of amplified molecules (multinomial, Dirichlet multinomial and other overdispersed models) and processes other than sampling (stochastic early amplification, run and batch effects, non-random dropout), each separately, and report what technical replicates at different read depths show about the variability of relative abundances and of the number of taxa detected.**

*Answer, as corrected by a second reader.* **D4: count-generating processes and replicate variability**

The evidence that Poisson or multinomial sampling explains replicate disagreement in taxa detected comes from one dataset. Zhou 2013 modelled the same 24 Oklahoma grassland soils, sequenced on 454, that Zhou 2011 reported. Wen 2017 is from the same laboratory. Wen 2017's MiSeq replicates cut against pure sampling. Zhou 2013 predicted about 60,900 reads for 90% OTU overlap, but in Wen 2017 unweighted overlap plateaued at 39% near 30,000 reads (with singletons) and reached only 43.9% at 160,000 reads. Wen's authors attribute rare-OTU variation to random sampling plus sequencing artefacts, report that 'biases other than random sampling' affect unweighted metrics more, and found lower overlap when replicates were sequenced in separate runs (a run effect). So: weak and contested that sampling alone explains replicate disagreement in taxa detected. The square-root decline of the CV of relative abundance with depth comes from one caecal extract (Barlow 2020, SINGLE SOURCE). Technical variance beyond counting (76% of variation at hourly sampling in artificial guts, Silverman 2018), early stochastic amplification at low load (Dyrhovden 2021) and whole-run taxon loss (Yeh 2018) are each single studies. Dirichlet-multinomial overdispersion has been shown only between biological samples, not among technical replicates. Water and non-gut host replicate-at-depth data are absent.

**D5. How do approaches to comparing samples with unequal read numbers or total loads compare, in either direction: absolute quantification of total load (qPCR, flow cytometry, spike-ins); coverage-based standardisation; compositional (log-ratio) approaches; proportions; rarefaction curves; rarefying to a common depth; richness estimators and extrapolation; scaling and normalisation methods? Answer separately for richness and other alpha diversity measures, for between-sample (beta) diversity, and for tests of which taxa differ in abundance, and for each approach say what it has been shown to correct and what it has not.**

*Answer, as corrected by a second reader.* **D5: comparing samples with unequal depth or load**

The body supports 'contested' for rarefying, proportions and differential-abundance methods. It supports that absolute quantification changes conclusions but does not remove taxon-specific bias. Corrections. (1) Willis 2019 is labelled 'asserted', but it presents statistical argument plus a worked simulated example. Calling it an assertion against Schloss's 'modelled' simulations understates the evidence against rarefying for richness. (2) Galazzo 2020: the r = -0.50 correlation on faeces is between qPCR and flow cytometry, not ddPCR and flow. ddPCR correlated strongly with qPCR, and the authors used this to rule out qPCR imprecision as the cause of the divergence. (3) Lin 2019: the authors conclude that the internal-standard method is quantitative and consistent with flow cytometry. The review reports only r2 = 0.19 before correction and does not give the authors' conclusion (Common rule 6). That figure could not be verified here. Coverage-based standardisation has one microbial test (the Schloss 2024b null model, verified: all approaches 'except for rarefaction and possibly the size-based iNEXT estimates' remained depth-correlated). Beyond that, the evidence is non-microbial. Benchmarks that build taxon-specific bias and load differences into the simulated truth together are absent, apart from Llorens-Rico 2021, which simulated faeces without taxon bias.

### MB-02

**D1. How many copies of the 16S rRNA gene do bacterial and archaeal genomes carry: the range, the distribution, and how it varies across taxa, according to current and earlier database releases and genome studies? Give 16S gene counts and ribosomal operon counts as each source reports them. Separately, how many 16S gene copies does a cell carry, given its number of genome copies: what measurements of genome copies per cell exist, in cultures and in environmental samples, including the share of cells at one genome copy and at more than one, in fast-growing, slow-growing and dormant states? What do studies relating 16S copy number to read-based abundance report, including copy-number prediction and correction methods, their measured accuracy, and whether correction changes ecological conclusions?**

*Answer, as corrected by a second reader.* **D1 (a) 16S copies per genome**

Mostly supported as written, with three corrections. (1) The archaeal ceiling is not 4 until v5.0: Acinas et al. 2004 (Acinas et al. 2004) already report a maximum of five archaeal operons, so the review's own sources conflict on the archaeal maximum, and the review does not flag this. (2) The 'Acidobacteria 1.0' mean from Vetrovsky and Baldrian (Vetrovsky and Baldrian 2013) rests on 4 genomes from 4 species (their Table 1). The rrnDB v5.10 figure of 1.4 rests on 29 species. These soil-relevant low values are imprecise, and the soil correction example (Acidobacteria 50.1% to 66.0%) depends on them. (3) The 1 to 15 range is consistent across sources, but those sources draw on overlapping NCBI genome sets, so they are not independent replications. The current maxima of 21 to 22 and the current shares remain the reviewer's own derivation from rrnDB, with no published check against assembly quality.

*Answer, as corrected by a second reader.* **D1 (b) genome and 16S copies per cell**

In cultures, genome copies per cell range from about one (Caulobacter, Wolinella, crenarchaea) to tens or hundreds (P. putida, haloarchaea, methanogens, Synechocystis), and depend on growth rate and phase. Copy number does not change in one direction with growth phase. Most Soppa-group species fall in stationary phase or starvation. The soil diazotroph Azotobacter vinelandii, however, is reported to rise from about 4 copies in exponential phase to about 80 in stationary phase (SECONDARY, via Bruck et al. 2023 full text). Pecoraro et al. 2011 Table 5 gives A. vinelandii as 1 (up to 8) copies in slow growth and 40 in fast growth, attributed to another laboratory. Several non-Soppa measurements exist: Azotobacter, Desulfovibrio, Neisseria and Deinococcus, all listed in Pecoraro 2011. Evidence is moderate, not strong: apart from Pecoraro 2011 it rests largely on abstracts and on one laboratory's qPCR method. The claim that 16S copies per cell scale with origin number is the reviewer's inference from an abstract (Couturier and Rocha 2006); no source in the review measures it. In natural communities, evidence is indirect and sparse (soil DNA mass per cell, seawater DNA-content populations, groundwater iRep). Flow cytometric cell-cycle analyses of Prochlorococcus in situ (Vaulot et al. 1995) are by method taxon-specific measurements of the share of cells with replicated DNA. The review read only the abstract, so its statement that no such share exists for any natural community is not established. Nothing comparable was found for soil.

*Answer, as corrected by a second reader.* **D1 (c) copy number versus reads; correction**

Supported, with corrections. Prediction accuracy declines with distance to sequenced genomes (Louca et al. 2018), and correction improves fit to simulated truth (Kembel et al. 2012; Gao and Wu 2023). In Starke et al. 2021, uncorrected data fitted 7.1% better on n = 10 mocks (one of the eleven was excluded); all were DNA-based or cloned-gene mocks. Correction changes the identity of the dominant OTU in about 20 to 31% of HMP and EMP communities, but against predicted, not measured, truth. It barely changes PERMANOVA in simulations (Gao and Wu 2023). The statement that extraction and primer biases are 'of similar or larger size' than copy-number bias is not supported by the McLaren abstract (McLaren et al. 2019). No soil benchmark was found. The soil literature on community-weighted rrn copy number (for example succession and rhizosphere-versus-bulk comparisons) was not searched.

**D2. How do microbial ecologists define and use terms for the abundance and distribution of taxa, such as abundant, rare, dominant, common, prevalent and core, and related terms? Report separately definitions based on relative abundance within one sample, on occupancy or prevalence across samples or sites, and on regional or global distribution; the thresholds used (for example relative abundance cutoffs) and whether classifications and conclusions hold or change across thresholds; frameworks from general ecology that classify kinds of rarity; proposed standard definitions; and how usage compares across studies.**

*Answer, as corrected by a second reader.* **D2 definitions and thresholds**

Supported in substance. Three families of definition are in use: within-sample thresholds (0.1% most common for rare), occupancy (core, mostly occurrence-only) and pooled or global classes. Usage is heterogeneous and often unstated (two surveys (Pascoal et al. 2025; Neu et al. 2021)). Three corrections. (1) Jia et al. 2022 (Jia et al. 2022) uses a single rare/common cutoff and does not support 'abundant above 1%'. (2) Custer et al. 2023 report that 165 to 176 taxa were agreed by all four methods, which is 13 to 16% of core assignments. The review's 'about 1% of taxa' is its own derivation and should be labelled as such. (3) Custer's text is internally inconsistent on whether core analyses gained or lost the temporal effect. Tests of threshold sensitivity point both ways and are each single-system. The single soil test (Jia 2022) found that classifications shift with the cutoff and that the relative importance of selection rose as the cutoff tightened, while the qualitative assembly conclusion held. Occupancy-based terms from general and microbial ecology (generalist/specialist by niche breadth, cosmopolitan/endemic, core/satellite) are under-covered.

**D3. In soil bacterial and archaeal communities, how is abundance distributed among taxa, and how does a taxon's local abundance relate to its occupancy across soils? Report figures from cell counts, amplicon reads and metagenomes separately, and how sampling effort, sequencing depth and detection affect the observed distributions and relationships, including null model analyses.**

*Answer, as corrected by a second reader.* **D3 (a) soil abundance distributions by measurement**

Amplicon reads, bulk soil: in the global datasets found, a small minority of taxa carries a large share of reads. The two figures must be kept apart. In Delgado-Baquerizo et al. 2018, 2% of phylotypes, defined jointly by abundance and ubiquity, accounted on average for 41% of reads per sample. In Bickel and Or 2021, 0.4% of ASVs, classed common on the globally pooled rank-abundance distribution, held about 58% of pooled relative abundance. The review's answer pools these into '0.4 to 2% hold 41 to 58%', contradicting its own body. Two phylotypes made up more than 70% of archaeal sequences across 146 soils (one study, abstract only). The functional form (lognormal versus power law) is contested, and most of that evidence is abstract-only or modelled. No soil taxon abundance distributions were found from cell counts or from metagenome coverage. The search did not cover genome-resolved global soil metagenomes (for example Bahram et al. 2018) or CARD-FISH phylum-level cell shares in soil.

*Answer, as corrected by a second reader.* **D3 (b) abundance-occupancy in soil**

In the two bulk-soil amplicon studies with figures (Bickel and Or 2021; Nemergut et al. 2011), more abundant taxa occupy more soils. These are not fully independent: Bickel and Or reanalysed compiled datasets including the Earth Microbiome Project, which plausibly overlaps the soils Nemergut used. Both measures are partly built in by construction. 'Total abundance' summed across samples, and 'common' defined on the pooled rank-abundance distribution, both rise with occupancy, the same circularity the review flags only for Delgado-Baquerizo 2018. Detection limits and neutral or sampling models predict a positive relationship without selection. No soil test against a sampling null was found. So whether a relationship exists beyond sampling, and how strong it is, is unresolved; 'wherever tested' overstates a search that reviewed about 25 titles. Rhizosphere evidence covers core membership in bean and maize, with 13.7% of bean bacterial and archaeal taxa deviating from a neutral curve. No rhizosphere correlation coefficients were found.

## Concepts

In an order where each concept comes after the ones it builds on; the order means nothing more.

### the steps and choices from sample to count table

- Twelve steps from sample to count table are documented, each with named alternatives; the procedural descriptions would not change if any single source were removed. (the reviewer's synthesis of protocols, documentation and benchmarks)
  Holds for: protocols, software documentation and benchmarks, mostly full text; makers' statements labelled as such.
  Evidence: rated "Strong for the existence of these choices and the alternatives used" by the research.
- Field sampling, preservation and storage choices include freezing or refrigeration, 95% ethanol, FTA cards, OMNIgene Gut, 70% ethanol or no preservative, for various times and temperatures. (Rubin et al. 2013; Song et al. 2016)
  Holds for: studies that vary the preservative, the temperature and the duration of storage.
- DNA extraction choices are the kit, bead-beating intensity, plate or single tube, and whether relic DNA is removed with PMA or DNase. (Albertsen et al. 2015; Carini et al. 2016; Lennon et al. 2018; Minich et al. 2019)
  Holds for: as listed in the answers.
- Primer and region choices include V1-V2 through V7-V9 and full length, degenerate variants of 515F and 806R, and PNA clamps against host plastids; in silico surveys cover 175 primers and 512 pairs. (Abellan-Schneyder et al. 2021; Fitzpatrick et al. 2018; Klindworth et al. 2013; Walters et al. 2016)
  Holds for: as listed in the answers.
- PCR choices are the polymerase, cycle number, input amount and single versus pooled replicate reactions. (the reviewer's synthesis)
  Holds for: as listed in the answers.
- Library preparation and indexing use one-step fusion, two-step tailed or ligation designs, with single, combinatorial or unique dual indexes. (the reviewer's synthesis)
  Holds for: as listed in the answers.
- Platform and read length choices are MiSeq 2x250 or 2x300, HiSeq, NovaSeq, Ion Torrent, 454, or PacBio CCS full length. (the reviewer's synthesis)
  Holds for: as listed in the answers.
- Demultiplexing is done with or without filtering on index-read quality. (Wright and Vetsigian 2016)
  Holds for: as listed in the answers.
- Quality filtering and merging set quality, length, expected-error and abundance thresholds, plus the delta-Q rule when merging. (Bokulich et al. 2013; Kozich et al. 2013)
  Holds for: as listed in the answers.
- Error handling uses 97% or 99% OTUs (de novo, closed or open reference) or ASVs from DADA2, Deblur or UNOISE3; DADA2 can process samples independently, pooled or pseudo-pooled. (the reviewer's synthesis)
  Holds for: as listed in the answers.
- Chimera detection uses UCHIME, UCHIME2 or ChimeraSlayer. (the reviewer's synthesis)
  Holds for: as listed in the answers.
- Taxonomy is assigned with RDP NBC, q2-feature-classifier, SINTAX, IDTAXA or MAPseq against SILVA, Greengenes, RDP or GTDB-type references, optionally with habitat-weighted priors. (Kaehler et al. 2019)
  Holds for: as listed in the answers.
- Contaminants are handled by dropping taxa seen in negative controls, decontam (frequency or prevalence mode), SourceTracker, or relative-abundance cutoffs. (the reviewer's synthesis)
  Holds for: as listed in the answers.
- In a survey of 265 papers in the 2018 issues of Microbiome and The ISME Journal that used any high-throughput community sequencing (16S, shotgun, metatranscriptomics, ITS, 18S and others), 30% (79) reported a negative control and 10% (27) a positive control; it is not a 16S-only figure. (Hornung et al. 2019)
  Holds for: two journals, 2018, all high-throughput community sequencing types, not 16S amplicon practice alone.
  Evidence: measured; a single source; rated "weak" by the research.
- How often each workflow choice is made across the field is unmeasured apart from controls. (Hornung et al. 2019)
  Holds for: the usage survey of controls is the only one found.
  Evidence: a search result.
  Searched for and not found.
- Field sampling choices for water (volume, filter pore size) and for host tissue are unsearched on the review's own Search record, so no source on their effect was reported. (the review's search record)
  Holds for: water sampling and host tissue sampling; section 2.1 says the lab angle searched preservation and storage terms, the Search record says no angle searched these choices.
  Evidence: a search result.
  Not searched for.
- There is no conflict over what the steps are, but the recommended choice within steps is disputed: quality-filter stringency (Bokulich 2013 versus Kopylova 2016), OTUs versus ASVs (Schloss 2021 versus the ASV developers), and pooled versus single PCR (Marotz 2019 and Smith and Peay 2014 versus the triplicate pooling in the EMP protocol). (Bokulich et al. 2013; Earth n.d.; Kopylova et al. 2016; Marotz et al. 2019; Schloss 2021; Smith and Peay 2014)
  Holds for: within-step choices.
  Evidence: contested.

### departure of observed from known composition

Builds on: the steps and choices from sample to count table.

- A mock community is a set of microbial strains of known composition, sequenced so that the observed composition can be compared with the known one; mock communities are a tool for validating, optimising and comparing methods for microbial community analysis. (Bokulich et al. 2016)
  Background, not from the research.
- Every mock-community study in the body found observed composition departing from known composition; several independent full-text mock and dilution studies show departures. (Vaginal et al. 2015; D'Amore et al. 2016; Fouhy et al. 2016; Karstens et al. 2019; Pinto and Raskin 2012; Silverman et al. 2021; Sze and Schloss 2019)
  Holds for: mock-community and dilution studies (Brooks 2015, Fouhy 2016, Pinto and Raskin 2012, D'Amore 2016, Karstens 2019, Silverman 2021, Sze and Schloss 2019).
  Evidence: measured; replicated; rated "Strong qualitatively" by the research.
- The size of the bias depends on platform, region, primer, extraction and pipeline. (Vaginal et al. 2015; D'Amore et al. 2016; Fouhy et al. 2016; Pinto and Raskin 2012)
  Holds for: as stated.
  Evidence: measured; the sources differ.
- Departures are measured at most steps examined but not at all of them: field sampling for water and host tissue was not searched, and several choices showed little or no detectable effect (PCR replicate pooling, preparation day and lane, cycle number in some studies, and storage in one soil, relative to between-soil differences). (the critic's reading of the review's body and search record)
  Holds for: the steps the body examined.
  The research does not say whether contrary evidence was searched for.
- Steps or choices found to matter little include storage relative to between-soil differences, PCR replication and pooling, preparation day and lane, cycle number in some studies, extraction method in one gut mock, relic DNA in one multi-environment study, PNA type for bacterial diversity, OTU versus ESV for broad patterns, rarefaction for beta diversity in real river data, library normalisation relative to metric choice, and operating system for pipeline output. (Acinas et al. 2005; Chiarello et al. 2022; Fitzpatrick et al. 2018; Fouhy et al. 2016; Glassman and Martiny 2018; Kennedy et al. 2014; Lennon et al. 2018; Marizzoni et al. 2020; Marotz et al. 2019; Rubin et al. 2013; Sipos et al. 2007; Smith and Peay 2014; Thorsen et al. 2016)
  Holds for: each in the study or studies named for it.
- Corrections that failed or introduced new errors include copy-number normalisation on mocks, copy-number prediction tools, UNBIAS, removing every taxon seen in negative controls, SourceTracker with undefined sources, stringent filtering, internal standards before correction, ANCOM-BC at small sample sizes, and fitZig. (Edgar 2017; Karstens et al. 2019; Kopylova et al. 2016; Lin et al. 2019; Louca et al. 2018; Starke et al. 2021; Wirbel et al. 2024)
  Holds for: each in the study named for it.

### field sampling, preservation and storage

Builds on: departure of observed from known composition.

- Unpreserved faecal samples and samples in 70% ethanol at ambient temperature changed composition by amounts comparable to the differences between individual humans. (Song et al. 2016)
  Holds for: faeces at ambient temperature.
  Evidence: measured; replicated.
- Human and dog faeces held at ambient temperature for 8 weeks changed by about as much as technical replicates differ when kept in 95% ethanol, on FTA cards or in OMNIgene Gut. (Song et al. 2016)
  Holds for: human and dog faeces, 8 weeks at ambient temperature.
- Storage altered taxon frequencies more than presence or absence: weighted UniFrac effects exceeded unweighted, and the number of taxa was affected less. (Song et al. 2016)
  Holds for: faeces.
- FTA cards produced a systematic shift that could be detrended, the one storage effect shown to be consistent across samples; for the other preservation methods consistency was not measured. (Song et al. 2016)
  Holds for: FTA cards and the other preservation methods.
- Storage changes in a soil were small relative to the differences among more than 500 Earth Microbiome Project soils. (Rubin et al. 2013)
  Holds for: a single soil stored, compared with more than 500 EMP soils.
  Evidence: measured; replicated.
- Storage for 1 to 14 days at room temperature, 4 C or -20 C changed a single soil's community, most at 3 to 7 days and least when frozen. (Rubin et al. 2013)
  Holds for: one soil.
- In Lauber et al. 2010, as described by Rubin, between-sample variation outweighed storage effects at 1,304 to 3,022 sequences per sample. (Lauber et al. 2010)
  Holds for: known only through Rubin et al. 2013's description.
  Evidence: limited by access (a source was not read in full; not the same as weak evidence).
- In one agricultural field, extracting 0.25, 1, 5, 10 or 100 g of soil changed community structure, replicate dispersion and OTU counts; ten-gram extractions gave the highest diversity and the lowest dispersion. (Penton et al. 2016)
  Holds for: one agricultural field, soil masses of 0.25 to 100 g.
  Evidence: measured; a single source.

### DNA extraction

Builds on: departure of observed from known composition.

- In McLaren et al.'s reanalysis of Brooks et al.'s 80 cell mixtures of 7 vaginal taxa, the extraction step had a maximum pairwise bias of 36.6-fold and a mean of 5.5-fold, the largest single step in that mock. (McLaren et al. 2019)
  Holds for: 80 cell mixtures of 7 vaginal taxa, V1-V3, 454; one dataset.
  Evidence: derived and modelled; a single source.
- In Brooks et al.'s own analysis, median total bias per taxon ranged from -32.6% to +39.1% of true proportion. (Vaginal et al. 2015)
  Holds for: the Brooks 2015 cell mixtures.
  Evidence: measured; contested.
- In Brooks et al.'s data, error from bias exceeded 85% in some samples, while technical variation was under 5% for most taxa. (Vaginal et al. 2015)
  Holds for: the Brooks 2015 cell mixtures.
  Evidence: measured; contested.
- In Brooks et al.'s data, swapping extraction kits changed Enterococcus by about 50%. (Vaginal et al. 2015)
  Holds for: the Brooks 2015 cell mixtures.
  Evidence: measured; contested.
- In activated sludge, harder bead beating increased DNA from Gram-positive bacteria by up to 400%. (Albertsen et al. 2015)
  Holds for: activated sludge.
  Evidence: measured; replicated.
- In activated sludge, bead-beating intensity and primer choice had the largest effects of all parameters tested. (Albertsen et al. 2015)
  Holds for: activated sludge.
- In a 20-species gut mock, two extraction methods (QIAamp stool kit versus repeat bead beating) gave "very similar" data, and primer and platform mattered more. (Fouhy et al. 2016)
  Holds for: one 20-species gut mock.
  Evidence: measured; replicated.
- The size of the extraction effect is contested: the review sets Fouhy 2016 (two extraction methods gave very similar data) against Albertsen 2015, Brooks 2015 and MBQC, and the critic counts the claim that, for relative abundance, extraction is the largest step, followed by PCR and then sequencing, as contested by Fouhy 2016 and qualified by MBQC (specimen type mattered more than extraction). (Albertsen et al. 2015; Vaginal et al. 2015; Fouhy et al. 2016; The et al. 2017)
  Holds for: the studies named.
  Evidence: contested.
- In the MBQC artificial communities, the largest contributor to inaccuracy was contamination or omission of microbes whose DNA was not extracted; species whose DNA was never extracted were missing. (The et al. 2017)
  Holds for: the MBQC artificial communities.
- Absolute diversity was not comparable between laboratories even with the same pipeline. (The et al. 2017)
  Holds for: the MBQC interlaboratory comparison.
- No more than 6% of inoculated lambda DNA was recovered from six soils. (Frostegard et al. 1999)
  Holds for: six soils; older soil work, indirect and pre-NGS.
  Evidence: measured; replicated.
- Extraction method changed fingerprint profiles of soil communities. (Martin-Laurent et al. 2001)
  Holds for: older soil work, indirect and pre-NGS.
  Evidence: measured; replicated.
- Extraction yield varied between samples: a synthetic spike-in quantified before and after extraction recovered 40% to 84%. (Zemb et al. 2020)
  Holds for: one spike-in study.
  Evidence: measured; a single source.

### relic (extracellular) DNA

Builds on: DNA extraction.

- Across soils, an average 40% of DNA was extracellular or from non-intact cells; removing it with propidium monoazide showed relic DNA inflated richness by up to 55% (more so at high pH, not at all in some soils) and misestimated relative abundances. (Carini et al. 2016)
  Holds for: soils; one study.
  Evidence: measured; contested.
- Relic DNA averaged 33% across soil, sediment, water and mammalian gut (over 80% in some samples) but had minimal effect on diversity estimates. (Lennon et al. 2018)
  Holds for: soil, sediment, water and mammalian gut; one multi-environment study.
  Evidence: measured; contested.
- Models predict that relic DNA biases diversity estimates only when relic and intact abundance distributions differ. (Lennon et al. 2018)
  Holds for: Lennon et al.'s models.
  Evidence: measured; contested.
- Whether relic DNA matters is contested: Carini 2016 against Lennon 2018. (Carini et al. 2016; Lennon et al. 2018)
  Holds for: the two studies named.
  Evidence: contested.

### primers and gene region

Builds on: departure of observed from known composition.

- In silico, 175 primers and 512 pairs differ widely in coverage and phylum spectrum against SILVA 108. (Klindworth et al. 2013)
  Holds for: in silico, SILVA 108.
  Evidence: derived; replicated.
- In marine samples, the review attributes under-representation of SAR11 and over-representation of Gammaproteobacteria to the original 515F/806R V4 primers, but the abstract gives the SAR11 bias (about 4 to 10-fold in field samples against about 2-fold in mocks) for the 515F-Y/806R pair, so mock-measured bias understated field bias for this taxon. (Parada et al. 2016)
  Holds for: marine field samples and mocks; one primer pair (515F-Y/806R) and one taxon (SAR11).
  Evidence: measured; replicated.
- On marine clone mocks, 515F-Y/926R fit expected composition with r2 = 0.95, against about 0.5 for 515F-Y/806R. (Parada et al. 2016)
  Holds for: marine clone mocks.
- Even perfectly matched primers showed preferential amplification. (Parada et al. 2016)
  Holds for: marine samples and mocks.
- Adding degeneracy to 515F and 806R improved detection of Thaumarchaeota and SAR11 in stool, soil and built-environment sets without degrading other taxa. (Walters et al. 2016)
  Holds for: stool, soil and built-environment sets.
  Evidence: measured; replicated.
- In human stool and mocks with seven primer pairs, Verrucomicrobia appeared only with V3-V4, V4, V6-V8 and V7-V9 primers: whole phyla appeared or disappeared with primer choice. (Abellan-Schneyder et al. 2021)
  Holds for: human stool and mocks, seven primer pairs.
  Evidence: measured; replicated.
- In a gut mock, 55 to 80% of expected species were detected, and 29 to 80% of detected species were misidentified or false hits, depending on primer, platform and extraction. (Fouhy et al. 2016)
  Holds for: one gut mock.
- Preferential amplification of a matched template over a mismatched one (63F) rose almost exponentially as annealing temperature went from 47 to 61 C; a perfectly matched primer showed no such effect. (Sipos et al. 2007)
  Holds for: T-RFLP, pre-NGS.
  Evidence: measured; a single source.
- With universal PNA clamps, host plastid reads averaged 23% across 32 plant species but reached 62 to 94% in some lineages. (Fitzpatrick et al. 2018)
  Holds for: 32 plant species.
  Evidence: measured; a single source.
- A modified PNA clamp cut Asteraceae contamination from 65% to 23% but raised it from 12% to 69% in other species. (Fitzpatrick et al. 2018)
  Holds for: plant host species.
- PNA type did not detectably change bacterial alpha or beta diversity. (Fitzpatrick et al. 2018)
  Holds for: plant host species.
- The makers of PCR clamps state that clamps enrich microbial sequences "without introducing bias". (Lundberg et al. 2013)
  Holds for: a makers' claim.
- In silico, 56% of V4 amplicons failed to match their species of origin with confidence, while full-length sequences classified nearly all correctly. (Johnson et al. 2019)
  Holds for: in silico.
  Evidence: derived; a single source.

### PCR conditions, cycle number and per-cycle efficiency

Builds on: departure of observed from known composition, primers and gene region.

- Two-template 27F-338R mixtures converged toward 1:1 products regardless of starting ratio; the bias depended strongly on cycle number and fit a kinetic model of product reannealing. (Suzuki and Giovannoni 1996)
  Holds for: two-template mixtures.
  Evidence: measured; replicated.
- Reproducible over-amplification of specific templates in genomic mixtures was explained largely by primer binding energy, not copy number, and was reduced by higher template concentration, fewer cycles and pooling of reactions. (Polz and Cavanaugh 1998)
  Holds for: genomic mixtures.
  Evidence: measured; replicated.
- In a 20-strain mock, genomic GC content correlated negatively with observed abundance; high-GC templates were also under-represented in Pinto and Raskin 2012. (Laursen et al. 2017; Pinto and Raskin 2012)
  Holds for: a 20-strain mock; Pinto and Raskin 2012.
- Longer initial denaturation raised the three highest-GC members of a 20-strain mock but did not change overall evenness. (Laursen et al. 2017)
  Holds for: a 20-strain mock.
  Evidence: measured; a single source.
- In a gut-isolate mock with primer mismatch removed by pre-amplification, log-ratios changed linearly with cycle number from 10 to 35 cycles. (Silverman et al. 2021)
  Holds for: one gut-isolate mock, primer mismatch removed.
  Evidence: measured; a single source.
- After 35 cycles relative abundances were biased by an average factor of 2.6 per taxon (95% credible set 2.3 to 2.9), and the B. longum to E. faecalis ratio shifted about 16-fold. (Silverman et al. 2021)
  Holds for: a gut mock with primer mismatch removed.
  Evidence: a single source.
- In four artificial-gut communities about 19% of taxa were more than 4-fold biased. (Silverman et al. 2021)
  Holds for: four artificial-gut communities.
  Evidence: a single source.
- PCR-bias calibration corrected composition toward truth in all 10 held-out mocks; the authors note that their mock "ground truth" carried its own bias and that the method sometimes estimated the wrong direction for some taxa. (Silverman et al. 2021)
  Holds for: 10 held-out mocks.
- PCR bias was consistent per taxon in mocks. (Silverman et al. 2021)
  Holds for: mocks.
- Sze and Schloss tested five polymerases at 20 to 35 cycles; in the mock, error rate, chimera fraction and deviation from the expected profile all rose with cycle number. (Sze and Schloss 2019)
  Holds for: one mock.
  Evidence: measured; a single source.
- In stool, the sample explained R2 = 0.79 of variation, cycles 0.044 and polymerase 0.033, and "this bias was inconsistent for human stool samples": cycle-related shifts were inconsistent across stool samples and small next to between-person differences. (Sze and Schloss 2019)
  Holds for: four stool samples.
  Evidence: measured; a single source.
- Template-to-product ratios were little affected by cycle number. (Sipos et al. 2007)
  Holds for: one study.
  Evidence: measured; a single source.
- Clone libraries amplified for different numbers of cycles showed no detectable skew. (Acinas et al. 2005)
  Holds for: Sanger clone libraries.
  Evidence: measured; a single source.
- 30 versus 35 cycles changed proportions only slightly. (Vaginal et al. 2015)
  Holds for: one study (Brooks 2015).
- The effect of cycle number conflicts between studies: small effects (Sipos 2007, Acinas 2005, Brooks 2015 at 30 versus 35 cycles) against growing bias (Suzuki 1996, Silverman 2021, the Sze and Schloss 2019 mock), with Sze and Schloss also finding inconsistent effects in stool. (Acinas et al. 2005; Vaginal et al. 2015; Silverman et al. 2021; Sipos et al. 2007; Suzuki and Giovannoni 1996; Sze and Schloss 2019)
  Holds for: the studies named, including the Sze and Schloss 2019 mock and stool.
- Low template (0.1 ng versus 5 to 10 ng) increased profile variability in soil and faecal samples; pooling of PCRs, preparation day and lane did not. (Kennedy et al. 2014)
  Holds for: soil and faecal samples.
  Evidence: measured; a single source.
- Single versus triplicate pooled PCRs made no significant difference. (Marotz et al. 2019)
  Holds for: one study; an open PMC copy exists, so the abstract-only label understates access.
  Evidence: measured; replicated.
- In fungal ITS, pooling 1 to 16 PCR replicates had no detectable effect on alpha or beta diversity. (Smith and Peay 2014)
  Holds for: fungal ITS, indirect for 16S.
  Evidence: measured.
- Pooling PCR replicates had no detectable effect, and pooled versus single PCR made no difference at moderate to high input, but replicates split before PCR disagreed strongly at low load. (Dyrhovden et al. 2021; Kennedy et al. 2014; Marotz et al. 2019; Smith and Peay 2014)
  Holds for: moderate to high input (Kennedy 2014, Marotz 2019, Smith and Peay 2014) against low load (Dyrhovden 2021); no single study tested both conditions.
- In low-input pools of unique synthetic barcodes, random per-molecule amplification in early cycles was the main source of skew; late-cycle polymerase errors stayed at low copy number, template switching was rare and GC bias minor. (Kebschull and Zador 2015)
  Holds for: synthetic barcode pools, non-16S, indirect.
  Evidence: measured; a single source.
- At low input, early stochastic amplification and dropout affected the detection of taxa. (Dyrhovden et al. 2021; Kebschull and Zador 2015)
  Holds for: low input; one source indirect.
- Documented protocols use 35 cycles in triplicate 25 uL reactions, pooling 240 ng per sample (EMP protocol, one-step PCR, checked on the live page), or 25 amplicon cycles plus 8 index cycles with 12.5 ng input (Illumina guide, two-step). (Earth n.d.; Illumina n.d.)
  Holds for: maker documentation and protocols.
  Evidence: rated "Moderate for documented cycle numbers" by the research.
- Experiments used 10 to 35 cycles (Silverman 2021), 15 or 20 to 35 (Sze and Schloss 2019), 20 versus 40 (Salter 2014) and 24 (Laursen 2017). (Laursen et al. 2017; Salter et al. 2014; Silverman et al. 2021; Sze and Schloss 2019)
  Holds for: the experimental studies named.
- Only relative per-cycle efficiencies have been measured: taxon-specific log-ratio changes per cycle that compound to an average 2.6-fold bias after 35 cycles in a gut mock. (Silverman et al. 2021)
  Holds for: one gut mock.
  Evidence: a single source; rated "Weak for per-cycle efficiencies" by the research.
- Other per-cycle efficiency values are drawn from beta distributions fitted to eukaryotic eDNA mocks, in a model of amplicons as starting copies x (1 + a_i)^cycles. (Kelly et al. 2019)
  Holds for: eukaryotic eDNA mocks, indirect.
  Evidence: modelled.
- No absolute per-cycle efficiency for universal 16S primers on environmental templates was found. (a search result)
  Holds for: the lab angle's routes (Crossref, Europe PMC, web search); the qPCR methods literature was not searched.
  Evidence: search (note: "was found by the lab angle (Crossref, Europe PMC, web search)").
  Searched, not found (note: "was found by the lab angle (crossref, europe pmc, web search)").

### 16S rRNA gene copies per genome

- The 16S rRNA gene, about 1,500 bp long, is present in almost all bacteria, often as a multigene family or in operons, and is the most common genetic marker for bacterial phylogeny and taxonomy. (Janda and Abbott 2007)
  Background, not from the research.
- Bacterial genomes carry 1 to 15 copies of the 16S rRNA gene in every database release and genome survey up to about 2015; the range is consistent across sources, but those sources draw on overlapping NCBI genome sets, so they are not independent replications. (Acinas et al. 2004; Klappenbach et al. 2001; Lee et al. 2009; Stoddard et al. 2015; Vetrovsky and Baldrian 2013)
  Holds for: rrnDB releases (the first: "one to as many as 15 copies"; 2009: 785 bacterial and 69 archaeal strains; 2015: 2,635 bacterial records, 1,383 species), Acinas et al. 2004 and Vetrovsky and Baldrian's 1,690 genomes; sequenced genomes.
  Evidence: derived; the sources differ; rated "Strong for the range and the taxon dependence" by the research; a second reader disputes this: consistent across sources, but not independent replications.
- Archaea carry 1 to 4 copies in rrnDB releases up to v5.0 (the 2015 release: 175 archaeal records, 148 species) and 1 to 5 from v5.6, but Acinas et al. 2004 already reported a maximum of five archaeal operons, so the sources conflict on the archaeal maximum. (Acinas et al. 2004; Schmidt Laboratory 2025; Stoddard et al. 2015)
  Holds for: archaeal genomes, few (148 species in 2015); archaeal maxima of 5 in v5.6 onward include Natronorubrum, Natrinema, Methanococcoides and Methanolobus.
  Evidence: derived; contested.
- The long-quoted ceiling of 15 is no longer the database maximum: rrnDB v5.6 contains a Photobacterium damselae genome with 21 copies and v5.10 a Mesobacillus maritimus genome with 22, and several Photobacterium and Bacillaceae genomes have 20 to 21; these maxima are the reviewer's own derivation from the release files, and no source checked them against assembly quality. (Schmidt Laboratory 2025)
  Holds for: rrnDB release files v3.1.227 to v5.10, summarised by the reviewer.
  Evidence: derived.
- Across rrnDB releases v3.1.227, v4.4.3, v5.0, v5.6 and v5.10, bacterial records rose from 1,297 to 48,053, the record mean from 4.20 (median 3) to 5.52 (median 6), the bacterial range from 1 to 15 to 1 to 22, and the mean of species means from 3.87 to 4.36, while the share of records at one copy fell from 17.5% to 7.5%; the archaeal species mean stayed at 1.66 to 1.73. (Schmidt Laboratory 2025)
  Holds for: the five releases; species grouped by the first two words of the NCBI name, which is approximate.
  Evidence: derived.
- Record-level means rise across releases mainly because of resequencing effort (in v5.10, E. coli contributes 3,902 records, 3,860 at 7 copies; Klebsiella pneumoniae 2,534, mostly 8; Salmonella enterica 1,770, mostly 7), while species-level means move much less (3.9 to 4.4); means therefore differ by counting unit (record mean 5.5 against species mean 4.4 in the same release). (Schmidt Laboratory 2025)
  Holds for: rrnDB releases.
  Evidence: derived.
- In rrnDB v5.10 the mean of species means is 4.4 (median 4) for bacteria and 1.7 (median 1) for archaea, and 11.3% of bacterial species and 51.6% of archaeal species average one copy. (Schmidt Laboratory 2025)
  Holds for: rrnDB v5.10, species-level summaries.
  Evidence: derived; rated "Moderate for exact means and shares" by the research.
- Over 1,690 bacterial genomes (909 species, GenBank 2012; 7,081 16S sequences extracted in silico), copies ranged from 1 to 15 with a mean of 4.2; 15% of genomes carried one copy and 21% two. (Vetrovsky and Baldrian 2013)
  Holds for: sequenced genomes, a skewed genome collection.
- Mean copy numbers by group in the 1,690 genomes were Acidobacteria 1.0, Alphaproteobacteria 2.2, Deltaproteobacteria 2.7, Actinobacteria 3.1, Betaproteobacteria 3.3, Bacteroidetes 3.5, Firmicutes 5.8 and Gammaproteobacteria 5.8; the Acidobacteria mean rests on 4 genomes from 4 species. (Vetrovsky and Baldrian 2013)
  Holds for: sequenced genomes.
- Per-phylum species means in rrnDB v5.10 are Bacillota 6.9 (1,274 species), Pseudomonadota 4.4 (3,050), Bacteroidota 3.8 (662), Actinomycetota 3.5 (1,334), Cyanobacteriota 2.8 (102), Planctomycetota 2.0 (62), Verrucomicrobiota 1.8 (35), Chloroflexota 1.6 (20), Acidobacteriota 1.4 (29), Euryarchaeota 1.9 (332), Thermoproteota 1.0 (65) and Nitrososphaerota 1.1 (18). (Schmidt Laboratory 2025)
  Holds for: rrnDB v5.10, derived.
  Evidence: derived.
- Phyla common in soil but poorly represented among genomes (Acidobacteriota, Verrucomicrobiota, Chloroflexota) sit at the low end of copy number on small numbers of species, so these soil-relevant low values are imprecise, and the soil correction example (Acidobacteria 50.1% to 66.0%) depends on them. (Schmidt Laboratory 2025; Vetrovsky and Baldrian 2013)
  Holds for: sequenced genomes of soil-relevant phyla (Acidobacteria 1.0 from 4 genomes; rrnDB v5.10 Acidobacteriota 1.4 from 29 species).
- Copy number depends strongly on taxon: the distribution is right-skewed and strongly taxon-structured, and taxon dependence is the strongest regularity. (Schmidt Laboratory 2025; Vetrovsky and Baldrian 2013)
  Holds for: sequenced genomes.
  Evidence: rated "Strong for the range and the taxon dependence" by the research.
- 16S copy number carries a moderate phylogenetic signal (K = 0.48 on 484 taxa). (Kembel et al. 2012)
  Holds for: 484 taxa.
- Copy number is "strongly linked" to taxonomy across 2,900 genomes, and Archaea are potentially under-represented in amplicon profiles. (Angly et al. 2014)
  Holds for: 2,900 genomes.
- Copy number was less conserved across taxonomic levels than genome size. (Vetrovsky and Baldrian 2013)
  Holds for: 1,690 bacterial genomes.
- Among 301 species with at least two records in the 2015 rrnDB release, 77% had identical counts, 16% differed by one copy and 3% by more than two. (Stoddard et al. 2015)
  Holds for: rrnDB 2015, species with at least two genome records.
  Evidence: derived.
- Of 1,038 species with at least five genomes in rrnDB v5.10, 44% show some within-species variation in copy number, although the median range is 0. (Schmidt Laboratory 2025)
  Holds for: rrnDB v5.10, derived.
  Evidence: derived.
- In the reviewer's reading, part of the within-species variation in rrnDB v5.10 is likely assembly error rather than biology (for example, 18 of 3,902 E. coli records report a single copy); it is not a tested claim. (the reviewer's reading)
  Holds for: rrnDB v5.10.
  Evidence: the reviewer's reading.
- The two within-species figures differ: 77% of species identical in 2015 against 44% of well-sampled species showing some variation in v5.10; the 2015 figure used far fewer genomes. (Schmidt Laboratory 2025; Stoddard et al. 2015)
  Holds for: rrnDB 2015 against v5.10.
- Copy-number distributions within a family can be bimodal: in Enterobacteriaceae (1 to 9 copies) a low-copy peak is made up of insect symbionts. (Stoddard et al. 2015)
  Holds for: rrnDB 2015.
- Means over all genomes mislead because some species are over-represented among genomes. (Stoddard et al. 2015)
  Holds for: rrnDB.
- From rrnDB version 5.0 onward, 16S genes are counted by BLAST against gap-free NCBI assemblies rather than from annotation, so genome records report 16S gene counts only, not operons or 23S counts. (Schmidt Laboratory 2025)
  Holds for: rrnDB v5.0 onward (About page).
- 16S gene count and operon count diverge where rRNA genes are unlinked: unlinked 16S and 23S genes are common in Deinococcus-Thermus, Chloroflexi and Planctomycetes, and up to 41% of rRNA genes in soil long-read metagenomes were unlinked, against none in human gut. (Brewer et al. 2020)
  Holds for: soil and human-gut long-read metagenomes; the soil figure from one source.
  Evidence: a single source.
- Copies within a genome are not always identical: heterogeneity was found in 952 of 2,013 genomes, 87.5% of it below 1% divergence, and the inflation of unique-sequence richness reached 123.7% for full-length genes but was smaller at 97% clustering. (Sun et al. 2013)
  Holds for: 2,013 genomes.
- Up to 15 operons occur in bacteria, with copy numbers up to 7 common and about 40% of organisms carrying one or two operons; a single operon dominated in archaea, with a maximum of five. (Acinas et al. 2004)
  Holds for: as stated.
- Operon redundancy gives an upper bound of about threefold diversity overestimation. (Acinas et al. 2004)
  Holds for: Acinas et al.'s estimate.
- Copy number tracks ecological strategy: soil isolates that formed colonies quickly averaged 5.5 copies and slow responders 1.4; this rests on one abstract-only study. (Klappenbach et al. 2000)
  Holds for: soil isolates; a measured association.
  Evidence: measured; a single source.
- Maximum growth (reproductive) rate doubles with a doubling of rrn copy number across 1,167 species. (Roller et al. 2016)
  Holds for: 1,167 species; a measured association.
  Evidence: measured; a single source.
- Copy numbers for uncultured lineages without genomes (for example many soil Acidobacteriota, Verrucomicrobiota, Chloroflexota and candidate phyla) are not measured, and genome databases over-represent cultured, clinically and industrially relevant taxa. (Louca et al. 2018)
  Holds for: genome databases.
  Evidence: a search result.
  The research does not say whether this was searched for.
- No source found measured 16S copy number directly in environmental populations of soil archaea beyond genomes of cultured or enriched Nitrososphaerota. (a search result)
  Holds for: soil archaea.
  Evidence: a search result.
  Searched for and not found.

### genome copies, and 16S copies, per cell

Builds on: 16S rRNA gene copies per genome.

- In cultures, genome copies per cell range from about one (Caulobacter, Wolinella, crenarchaea) through merodiploid and oligoploid states that depend on growth rate (E. coli, Bacillus, Synechococcus) to tens or hundreds (P. putida, haloarchaea, methanogens, Synechocystis), and depend on taxon, growth rate and growth phase; this general conclusion would survive any single removal. (Bottinger et al. 2018; Breuert et al. 2006; Griese et al. 2011; Hildenbrand et al. 2011; Pecoraro et al. 2011; Zerulla et al. 2016)
  Holds for: cultures.
  Evidence: measured; rated "Strong for cultures" by the research; a second reader disputes this: moderate, not strong; apart from Pecoraro 2011 it rests largely on abstracts and one laboratory's qPCR method.
- Most culture ploidy values come from one laboratory's real-time PCR protocol (Soppa group), in several studies cross-checked against Southern blots, flow cytometry or published E. coli values; measurements from other laboratories exist for Azotobacter, Desulfovibrio (9 to 17), Neisseria (3 to 4) and Buchnera (120), with polyploid Deinococcus, Borrelia and rhizobial bacteroids also mentioned, all listed in Pecoraro 2011. (Bottinger et al. 2018; Breuert et al. 2006; Bruck et al. 2023; Griese et al. 2011; Hildenbrand et al. 2011; Pecoraro et al. 2011; Zerulla et al. 2016; Zerulla and Soppa 2014)
  Holds for: cultures.
  A second reader found the search for contrary evidence one-sided.
- E. coli has 6.8 origins and 1.7 termini per cell at 25 min doubling but 2.5 origins and 1.2 termini at 103 min; removing this source would remove the only direct origin and terminus counts for E. coli at two growth rates. (Pecoraro et al. 2011)
  Holds for: E. coli cultures.
  Evidence: measured.
- E. coli stationary-phase batch cultures always contained some multi-chromosome cells, even after days. (Akerlund et al. 1995)
  Holds for: E. coli batch cultures.
  Evidence: measured.
- Caulobacter crescentus (doubling 93 min) carries about 2.1 genome-equivalents at a mid-chromosome locus, read as monoploid, and Wolinella succinogenes (doubling 96 min) about 0.9, monoploid. (Pecoraro et al. 2011)
  Holds for: cultures.
  Evidence: measured.
- Pseudomonas putida (doubling 46 min) carries about 20 origins and 14 termini per cell. (Pecoraro et al. 2011)
  Holds for: cultures; the only P. putida value.
  Evidence: measured.
- B. subtilis and three soil Bacillus/Paenibacillus isolates are mero-oligoploid in exponential phase (B. subtilis 5.9 origins, 1.2 termini) and down-regulate origins in stationary phase. (Bottinger et al. 2018)
  Holds for: cultures.
  Evidence: measured.
- Synechococcus PCC 7942 and WH7803 carry 3 to 4 genome copies in culture. (Griese et al. 2011)
  Holds for: cultures.
  Evidence: measured.
- Synechocystis PCC 6803 carries 218 (exponential) to 58 (stationary) copies in one substrain and about 20 to 4 across six substrains, becoming monoploid only after prolonged phosphate starvation. (Griese et al. 2011; Zerulla et al. 2016)
  Holds for: cultures.
  Evidence: measured.
- Halobacterium salinarum carries 25 (exponential) and 15 (stationary) genome copies, and Haloferax volcanii 18 and 10. (Breuert et al. 2006)
  Holds for: cultures.
  Evidence: measured.
- Methanococcus maripaludis carries up to 55 genome copies in exponential phase and about 30 in stationary phase. (Hildenbrand et al. 2011)
  Holds for: cultures.
  Evidence: measured.
- Methanosarcina acetivorans carries 17 genome copies in fast growth and 3 in slow growth. (Hildenbrand et al. 2011)
  Holds for: cultures.
  Evidence: measured.
- Six crenarchaeal species of four genera were all monoploid, whereas none of seven euryarchaeal species was monoploid. (Hildenbrand et al. 2011)
  Holds for: compiled culture measurements.
  Evidence: measured.
- Zymomonas mobilis, Azotobacter vinelandii and H. salinarum stayed at about five copies in phosphate-starved stationary phase rather than becoming monoploid, whereas Synechocystis went to one copy. (Bruck et al. 2023; Zerulla et al. 2016)
  Holds for: phosphate-starved stationary cultures.
  Evidence: measured.
- Only three to four of 11 proteobacterial species with measured ploidy were monoploid, with no correlation to genome size, temperature or lifestyle. (Pecoraro et al. 2011)
  Holds for: 11 proteobacterial species.
- Single-cell measurements in H. salinarum showed wide cell-to-cell variation in genome copy number, larger in exponential than in stationary phase; the review read only the abstract, which gives no per-cell shares, although the open full text reports single-cell CLSM and FACS distributions. (Breuert et al. 2006)
  Holds for: H. salinarum cultures.
  Evidence: limited by access (a source was not read in full; not the same as weak evidence).
- Azotobacter vinelandii is reported to rise from about 4 genome copies in exponential phase to about 80 in stationary phase, and Methanosarcina acetivorans from 2.5 to 5; Pecoraro 2011 Table 5 gives A. vinelandii as 1 (up to 8) copies in slow growth and 40 in fast growth, attributed to another laboratory. (Bruck et al. 2023; Pecoraro et al. 2011)
  Holds for: the A. vinelandii stationary-phase figure is secondary, via the Bruck et al. 2023 full text read by the critic.
- Genome copy number does not change in one direction with growth phase: most Soppa-group species fall in stationary phase or starvation, but A. vinelandii is reported to rise (secondary, via the Bruck et al. 2023 full text). (Bruck et al. 2023; Pecoraro et al. 2011)
  Holds for: taxon-specific and sometimes opposite behaviours.
  A second reader found the search for contrary evidence one-sided.
- rRNA operons cluster near the replication origin in fast-growing bacteria, and replication-associated gene-dosage effects shape this placement. (Couturier and Rocha 2006)
  Holds for: fast-growing bacteria.
- That 16S copies per cell scale with origin number more than with genome number is the reviewer's inference from one abstract; no source in the review measures 16S copies per cell against origin number. (Couturier and Rocha 2006)
  Holds for: fast growers.
  Evidence: the reviewer's reading.
- For E. coli, rRNA genes per genome equivalent range from about 7.9 to 9.5 across growth rates. (Bremer and Dennis 1996; Milo et al. 2010)
  Holds for: E. coli; Bremer and Dennis (1996), Table 3, as reported by BioNumbers.
  Evidence: limited by access (a source was not read in full; not the same as weak evidence).
- No source the reviewer found measured 16S copies per cell directly in environmental cells. (a search result)
  Holds for: environmental cells.
  Evidence: a search result.
  Searched for and not found.
- In environmental samples, evidence on genome copies per cell is indirect and sparse (DNA mass per soil cell, DNA-content populations in seawater, population-average replication indices in groundwater), mostly non-soil and single-study per setting. (Brown et al. 2016; Button and Robertson 2001; Christensen et al. 1995)
  Holds for: soil, seawater, groundwater.
  Evidence: a single source; rated "Weak for environmental samples" by the research.
- Indigenous soil bacteria extracted from a clay loam contained 1.5 to 15 fg DNA per cell by flow cytometry, most below 4 fg, with an average around 2 fg; larger cells, and cells that grew in soil extract, had more DNA; this confirms earlier work by the same group, and it is the only soil measurement of DNA per cell. (Bakken and Olsen 1989; Christensen et al. 1995)
  Holds for: one clay loam; Bakken and Olsen 1989 is secondary.
- DNA mass per cell cannot separate genome size from copy number, and the two DNA-content populations in seawater could reflect replicating monoploid cells or larger genomes. (Button and Robertson 2001; Christensen et al. 1995)
  Holds for: DNA per cell in soil; DNA-content populations in seawater.
- In the reviewer's reading, about 2 fg of DNA is less than one copy of a 4 Mb genome, which suggests many soil cells hold one copy of a small genome; this is inference. (the reviewer's reading)
  Holds for: soil.
  Evidence: the reviewer's reading.
- A typical seawater sample had a mean of 2.5 fg DNA per cell, in two populations described as 1n and 2n clusters, with 10 to 30% of cells "dim" low-DNA cells. (Button and Robertson 2001)
  Holds for: seawater.
- The authors of the seawater study treat increased copy number with growth rate in nature as "likely", an inference rather than a measurement. (Button and Robertson 2001)
  Holds for: seawater.
- In the equatorial Pacific, Prochlorococcus DNA replication ran in phase with the light cycle, in the afternoon, with division at night; the abstract gives no share of cells carrying two genomes. (Vaulot et al. 1995)
  Holds for: Prochlorococcus in the equatorial Pacific; abstract only.
  Evidence: limited by access (a source was not read in full; not the same as weak evidence).
- In groundwater metagenomes, population-average replication indices (iRep) were mostly low: Candidate Phyla Radiation bacteria had a median iRep of 1.34, and only 16.1% of values exceeded 1.5; the authors interpret an iRep of 1.25 as about a quarter of cells replicating; this is the only environmental replication-index figure. (Brown et al. 2016)
  Holds for: groundwater metagenomes.
- Gut metagenome peak-to-trough ratios track growth rate in culture and in vivo. (Korem et al. 2015)
  Holds for: gut.
- No published replication indices for soil metagenomes were found. (a search result)
  Holds for: Europe PMC queries combining iRep, peak-to-trough, GRiD or CoPTR with soil; WebSearch on soil iRep, rewetting and permafrost.
  Evidence: a search result.
  Searched for and not found.
- Not measured in the sources found: genome copies per cell for named soil bacterial or archaeal taxa in situ; the share of single-copy cells by taxon in soil, rhizosphere or dormant natural populations; any direct measurement of 16S copies per cell in environmental cells; ploidy of cultured soil Acidobacteriota, Verrucomicrobiota or Nitrososphaerota. (Vaulot et al. 1995)
  Holds for: soil, rhizosphere and dormant natural populations; for Prochlorococcus, in situ flow cytometric cell-cycle analyses measure by method the taxon-specific share of cells with replicated DNA, and the review read only the abstract.
  Evidence: a search result.
  Searched for and not found.
- A search for contrary evidence on culture ploidy values (P. putida copy number by flow cytometry) was run once and found none. (a search result)
  Holds for: one WebSearch.
  Evidence: a search result.
  Searched for and not found.

### copy number against read abundance, prediction and correction

Builds on: 16S rRNA gene copies per genome, PCR conditions, cycle number and per-cycle efficiency.

- Copy number is a property of each taxon rather than a workflow step, but it acts through PCR. (the reviewer's statement)
  Holds for: as stated.
- With equimolar DNA from species pairs, PCR product ratios matched rrn genes per unit DNA for two pairs but deviated for a Bacillus pair. (Farrelly et al. 1995)
  Holds for: equimolar DNA from species pairs.
  Evidence: measured.
- In the 7-taxon vaginal mock, copy number explained about 60% of estimated PCR bias (R2 about 0.60, p about 0.021) but only about 10% of total bias (R2 about 0.10). (McLaren et al. 2019)
  Holds for: 7 taxa, verified in full text.
  Evidence: deriv (note: "Partial (derived)"); a single source.
- In a forest soil, correcting with copy number and genome size moved Acidobacteria from 50.1% of 16S sequences to an estimated 66.0% of genomes, Actinobacteria from 11.8% to 7.6% and Firmicutes from 3.2% to 1.1%; it is the only soil example of correction size. (Vetrovsky and Baldrian 2013)
  Holds for: one forest soil; depends on soil-relevant low copy-number values that are imprecise.
  Evidence: derived; the sources differ.
- Phylogenetic copy-number prediction had a leave-one-out error of about one copy. (Kembel et al. 2012)
  Holds for: Kembel et al.'s analysis.
- In 100 simulated communities, phylogenetically corrected abundances correlated better with true organism abundance (r = 0.81) than raw gene abundances did (r = 0.70). (Kembel et al. 2012)
  Holds for: simulated communities.
  Evidence: modelled; contested.
- Copy-number correction moved ear samples to cluster with nostrils rather than feet, but left ocean clustering largely unchanged. (Kembel et al. 2012)
  Holds for: human body sites and ocean.
- Copy-number prediction is accurate only near sequenced relatives: copy-number autocorrelation fell below 0.5 at about 15% 16S divergence and reached zero at about 30%; the quantitative thresholds rest on one analysis, though the qualitative distance effect is replicated. (Louca et al. 2018)
  Holds for: about 6,800 genomes.
  Evidence: derived; replicated.
- The decline of prediction accuracy with distance to sequenced genomes is consistent across four independent analyses, and correction improves fit to simulated truth. (Edgar 2017; Gao and Wu 2023; Kembel et al. 2012; Louca et al. 2018)
  Holds for: four independent analyses of genome-based prediction.
  Evidence: replicated.
- About 49% of SILVA OTUs lie more than 15% from a sequenced genome, so copy-number predictions are unreliable for about half of them. (Louca et al. 2018)
  Holds for: SILVA OTUs.
- PICRUSt, CopyRighter and PAPRICA sometimes explained under 10% of variance against complete genomes and disagreed with each other (R2 < 0.5) for most of 635 communities, which included soils. (Louca et al. 2018)
  Holds for: 635 environmental communities, including soils.
  Evidence: derived; replicated.
- Louca et al. recommend against default copy-number correction unless OTUs are close to sequenced genomes. (Louca et al. 2018)
  Holds for: their analysis.
- Copy-number prediction precision was about 0.96 at small distances to sequenced genomes, with R2 high, and its uncertainty rose with distance. (Gao and Wu 2023)
  Holds for: Gao and Wu's analysis.
- A preprint by the tool's author reports essentially "no meaningful correlation" between 16S read frequencies and species frequencies in mocks. (Edgar 2017)
  Holds for: mocks; preprint abstract.
  Evidence: measured; a single source.
- Correction for copy number and primer mismatch reached r of about 0.6 only in ideal cases, when references were exact, falling to about 0.4 at 97% and about 0.2 at 95% identity. (Edgar 2017)
  Holds for: mocks; preprint abstract.
  Evidence: measured; a single source.
- Copy numbers can be estimated from draft assemblies by read depth, with a median deviation of 14% against qPCR. (Perisin et al. 2016)
  Holds for: draft genome assemblies.
- Copy-number correction improved agreement with mock communities and metagenomes, changed qPCR totals and diversity estimates, and reclassified twin gut samples from two enterotypes to three. (Angly et al. 2014)
  Holds for: mocks, metagenomes and twin gut samples.
- On 10 V4 mock communities (one of eleven excluded; nine genomic DNA mixes and two cloned-gene mixes), uncorrected data fit known composition 7.1% (SE 3.6%) better than copy-number-corrected data; all were DNA-based or cloned-gene mocks. (Starke et al. 2021)
  Holds for: DNA-based and cloned-gene mocks.
  Evidence: measured; replicated.
- In the reviewer's note, DNA-based mocks already fix genome copies and size, so they test correction against a DNA truth, not a cell truth; part of the conflict over correction reflects what "truth" is (cell-based against DNA-based mocks, simulated against real communities, and closeness to references). (the reviewer's reading)
  Holds for: mock-based tests of correction.
  Evidence: the reviewer's reading.
- Copy-number correction changed the most abundant OTU in about 20% of Human Microbiome Project and 31% of Earth Microbiome Project communities, but against predicted, not measured, truth; these are the only figures on how often correction changes the dominant taxon in real communities. (Gao and Wu 2023)
  Holds for: HMP and EMP communities.
- In simulations, copy-number correction raised the chance of identifying the true most abundant OTU from 13% to 65%. (Gao and Wu 2023)
  Holds for: simulations.
- In simulations, correction reduced sample shifts in ordinations but left PERMANOVA variance explained essentially unchanged (5.27 to 19.65% true against 5.27 to 19.82% uncorrected), so correction changes dominant taxa but rarely changes beta-diversity test results. (Gao and Wu 2023)
  Holds for: simulations.
- Whether to correct for copy number is contested: studies recommending routine correction conflict directly with studies recommending against default correction or finding it unhelpful in mocks (in MB-01's terms, Kembel 2012 against Louca 2018, Starke 2021 and McLaren 2019); evidence on whether correction improves real data is mostly from simulations, mocks of few species or non-soil communities, with no soil benchmark. (Angly et al. 2014; Edgar 2017; Gao and Wu 2023; Kembel et al. 2012; Louca et al. 2018; McLaren et al. 2019; Starke et al. 2021)
  Holds for: simulations, mocks and non-soil communities.
  Evidence: contested; rated "Moderate" by the research.
- Intragenomic variants split genomes into several ASVs: 0.58 variants per copy for full-length 16S and 0.25 for V4. (Schloss 2021)
  Holds for: genomes, full-length and V4.
  Evidence: derived; contested.
- Full-length PacBio sequencing recovered intragenomic variants in their expected integral ratios. (Callahan et al. 2019)
  Holds for: the developer's own test.
  Evidence: measured; a single source.
- A review asserts that rDNA copy number can change within species in response to environment; the prokaryote evidence for this was not quantified in what was read. (Lavrinienko et al. 2021)
  Holds for: a review.
  Evidence: asserted.
- No soil mock community or soil cell-count benchmark of copy-number correction was found. (a search result)
  Holds for: soil.
  Evidence: a search result.
  Searched for and not found.
- No study was found that combines copy-number correction with per-cell genome copy measurements in a real community; the polyploidy literature asserts that ploidy also biases community analyses. (Soppa 2017)
  Holds for: real communities; the polyploidy assertion is from a source not obtained (Soppa 2017).
  Evidence: a search result.
  Searched for and not found.

### copy number by environment

Builds on: copy number against read abundance, prediction and correction.

- Every environment-level 16S copy number found is predicted from reference genomes, not measured. (Thompson et al. 2017)
  Holds for: environment-level copy numbers.
  Evidence: derived.
- Soil had the lowest abundance-weighted copy-number distribution in the Earth Microbiome Project (predicted, not measured). (Thompson et al. 2017)
  Holds for: EMP soils; predicted from reference genomes.
  Evidence: derived; a single source.
- Predicted average community copy number declines through succession in soil and sediment. (Nemergut et al. 2016)
  Holds for: soil and sediment succession; predicted.
  Evidence: derived; a single source.
- Animal-associated samples have a predicted community copy number of about 3.4, with gut and saliva highest. (Thompson et al. 2017)
  Holds for: animal-associated samples; predictions from one source.
  Evidence: a single source.
- No separate copy-number value for water was found; the EMP gives a predicted value of about 2.2 for free-living (soil, water, sediment) and plant-associated samples pooled together. (Thompson et al. 2017)
  Holds for: EMP, free-living and plant-associated samples pooled.
  Evidence: a single source.
- Environment-level copy number rests entirely on one source, its values are predictions, and they conflict with the finding that such predictions are unreliable for taxa more than about 15% divergent from sequenced genomes. (Louca et al. 2018; Thompson et al. 2017)
  Holds for: environment-level predictions.
  Evidence: a single source; rated "Weak for environment-level copy number" by the research.
- Measured (not predicted) community-average copy number in soil, water or host samples was not found; community-average copy number from shotgun metagenomes (16S reads normalised to single-copy marker genes) was not searched, so the not-found rests on prediction-only sources. (a search result)
  Holds for: soil, water and host samples.
  Evidence: a search result.
  Not searched for.

### library preparation, indexing and sequencing error

Builds on: PCR conditions, cycle number and per-cycle efficiency.

- Across 73 MiSeq datasets, library preparation method and primer choice were the most significant sources of bias, with distinct, motif-linked error patterns; this rests on one study. (Schirmer et al. 2015)
  Holds for: 73 MiSeq datasets.
  Evidence: measured; a single source.
- Library design also affected error and chimera rates across four platforms. (D'Amore et al. 2016)
  Holds for: four platforms.
- Dual-index MiSeq error depended on read overlap. (Kozich et al. 2013)
  Holds for: dual-index MiSeq.
  Evidence: measured; replicated.
- Raw V4 MiSeq error rose with cluster density from 0.25% to 1.08%; a delta-Q of 6 cut it to 0.05 to 0.06%, and preclustering to 0.01%. (Kozich et al. 2013)
  Holds for: V4 on MiSeq.
- Partially overlapping regions stayed worse: after preclustering, V3-V4 error was 0.10 to 0.21% and V4-V5 0.36 to 0.64%, per the bioinformatics angle. (Kozich et al. 2013)
  Holds for: V3-V4 and V4-V5 after preclustering, per the bioinformatics angle.
- Against the bioinformatics angle's figures (V3-V4 0.10 to 0.21% and V4-V5 0.36 to 0.64% after preclustering), the lab angle reports 0.24 to 0.37% and 0.58 to 0.87%, read through a fetch-tool summary and probably at an earlier stage of curation. (Kozich et al. 2013)
  Holds for: per the lab angle.
- PacBio CCS with DADA2 recovered all expected full-length variants in two mocks with no residual errors, by the developers' own account. (Callahan et al. 2019)
  Holds for: two mocks; a developer claim.
- The DADA2 maintainer states that NovaSeq's binned quality scores break loess smoothing in error learning; at the time of the issue the method had not been tested on NovaSeq data. (benjjneb and contributors n.d.)
  Holds for: DADA2 GitHub issue #791.
  Evidence: asserted.

### demultiplexing and index misassignment

Builds on: library preparation, indexing and sequencing error.

- On Illumina GAIIx with non-16S libraries, 0.51 to 0.76% of index pairs were wrong, and 0.06 to 0.43% after index-quality filtering. (Kircher et al. 2012)
  Holds for: GAIIx, non-16S libraries, indirect.
  Evidence: measured; replicated.
- On patterned flow cells (HiSeq X, 3000/4000, NovaSeq) with non-16S libraries, 0.2 to 6% of reads were misassigned in every run, about 10-fold less on MiSeq, and unique dual indexes cut 0.89% to 0.13%. (Costello et al. 2018)
  Holds for: non-16S libraries, indirect.
  Evidence: measured; replicated.
- Illumina documentation gives 0.1 to 2% index misassignment on patterned flow cells. (Illumina n.d.)
  Holds for: a maker's claim.
- On HiSeq 2500 with non-16S amplicons, cross-talk was 0.24%, and 0.03% after index-quality filtering (88% of reads kept). (Wright and Vetsigian 2016)
  Holds for: HiSeq 2500, non-16S amplicons, indirect.
  Evidence: measured; a single source.
- In 16S data from GAIIx and 11 MiSeq runs, about 2% of reads were misassigned. (Edgar 2016)
  Holds for: 16S; one preprint abstract.
  Evidence: measured; a single source.
- On 16S plates, barcode leakage was negligible. (Minich et al. 2019)
  Holds for: 16S plates.
  Evidence: measured; a single source.
- In eukaryotic 18S data, up to 28.2% of unique sequences were undetectable mistags. (Esling et al. 2015)
  Holds for: eukaryotic 18S, indirect.
  Evidence: measured.
- With mammal and arthropod markers, 2.1 to 2.6% of sequences came from tag jumps. (Schnell et al. 2015)
  Holds for: mammal and arthropod markers, indirect.
  Evidence: measured.
- Index misassignment rates are fractions of reads assigned to the wrong sample; they mainly create false presences of taxa, concentrated where abundant taxa from other samples leak in, and also affect relative abundance. (the reviewer's synthesis)
  Holds for: as stated.
- Index misassignment rates vary with platform, library type and run. (the reviewer's synthesis)
  Holds for: as stated.
- The 16S-specific evidence on index misassignment is thin: one preprint abstract and one plate study; no 16S-specific measurement of index hopping on patterned flow cells (NovaSeq, NextSeq 2000) was found. (Edgar 2016; Minich et al. 2019)
  Holds for: the bioinformatics angle's search.
  Evidence: search (note: "No 16S-specific measurement of index hopping on patterned flow cells (NovaSeq) was found").
  Searched, not found (note: "no 16s-specific measurement of index hopping on patterned flow cells (novaseq) was found").

### quality filtering and read merging

Builds on: library preparation, indexing and sequencing error.

- On mocks from GAIIx, HiSeq and MiSeq runs, minimum read length, quality threshold and a minimum OTU abundance filter strongly affected alpha diversity and composition; ambiguous bases and bad run length did not. (Bokulich et al. 2013)
  Holds for: mocks from GAIIx, HiSeq and MiSeq runs.
  Evidence: measured; replicated.
- Almost every filtering setting needed an abundance filter of 0.0001 to 0.01% to reach expected taxon counts, and 0.005% is recommended. (Bokulich et al. 2013)
  Holds for: mocks.
- Weighted UniFrac conclusions were robust and unweighted metrics were sensitive. (Bokulich et al. 2013)
  Holds for: mocks.
- Stringent UPARSE-style filtering could significantly underestimate abundance and diversity, and newer clusterers produced up to 60% fewer spurious OTUs than UCLUST. (Kopylova et al. 2016)
  Holds for: Kopylova et al.'s benchmarks.
  Evidence: measured; contested.
- Error correction plus overlapping cut substitution errors by 93% on average. (Schirmer et al. 2015)
  Holds for: one study.
- The USEARCH author reports that most paired-read assemblers compute incorrect posterior quality scores. (Edgar and Flyvbjerg 2015)
  Holds for: a developer claim.

### denoising, clustering, OTUs and ASVs

Builds on: quality filtering and read merging.

- In an independent benchmark, relative abundances of expected taxa within each mock were similar across DADA2, UNOISE3, Deblur and open-reference OTUs, yet on the Zymo mock all pipelines "markedly differed" from expected composition. (Nearing et al. 2018)
  Holds for: mocks, one independent benchmark.
  Evidence: measured; replicated.
- Counts of units differed widely between pipelines: open-reference clustering gave 453 OTUs on the HMP mock and 8,891 on the Extreme mock; on one soil, DADA2 gave 16,609 ASVs, UNOISE3 11,613, Deblur 8,270 and open-reference 21,297 OTUs; no pipeline recovered every expected sequence. (Nearing et al. 2018)
  Holds for: mocks and one soil.
- Bacteroides varied from 20.6% to 24.6% across pipelines. (Marizzoni et al. 2020)
  Holds for: one study.
- mothur and QIIME1 returned 10 to 200 times the expected number of sequences, and Faith's PD was overestimated 1.3 to 2.7-fold by QIIME2, 2 to 18-fold by QIIME1 and 3.5 to 29-fold by mothur; the study reports pipeline-dependent interpretations. (Straub et al. 2020)
  Holds for: Straub et al.'s benchmark; the authors also built nf-core/ampliseq.
  Evidence: measured; replicated.
- DADA2 had the best sensitivity and UNOISE3 the best balance. (Prodan et al. 2020)
  Holds for: one study.
  Evidence: measured; replicated.
- QIIME-uclust produced on average 134 one-off and 412 other spurious OTUs. (Prodan et al. 2020)
  Holds for: one study.
- The DADA2 developers report 93 output sequences on a 57-strain mock, against 249 for mothur and 378 for QIIME. (Callahan et al. 2016)
  Holds for: one 57-strain mock; a developer claim.
  Evidence: measured.
- After OTU clustering and singleton removal, tables were about 50% (mock communities) to 80% (gnotobiotic mice) spurious taxa; the authors propose a 0.25% relative-abundance cutoff. (Reitmeier et al. 2021)
  Holds for: mock communities and gnotobiotic mice.
  Evidence: measured; a single source.
- QIIME closed- and open-reference OTUs inflated richness to 1,607 to 5,824 OTUs where about 20 were expected. (Edgar 2017)
  Holds for: where about 20 OTUs were expected.
  Evidence: a single source.
- In leaf litter, bacterial OTU richness was about half of ESV richness (slope 0.46), but alpha and beta metrics correlated at r > 0.90 and inferences matched. (Glassman and Martiny 2018)
  Holds for: leaf litter.
  Evidence: measured; contested.
- In 227 freshwater sediment, seston and mussel-gut samples the direction was reversed: ASV richness was about half of OTU richness, and Mollicutes dominated mussel gut by ASVs but were absent from OTU tables; the authors attribute the reversal partly to higher richness in sediment. (Chiarello et al. 2022)
  Holds for: 227 freshwater sediment, seston and mussel-gut samples.
  Evidence: measured; contested.
- The direction of the OTU versus ASV richness difference conflicts between studies (Glassman and Martiny 2018 against Chiarello 2022). (Chiarello et al. 2022; Glassman and Martiny 2018)
  Holds for: the two studies named.
- In soil and plant samples, OTUs versus ASVs changed which families were called differentially abundant, mostly families under 0.1% abundance. (Joos et al. 2020)
  Holds for: soil and plant samples.
  Evidence: measured; a single source.
- The identity threshold that best matched species was about 99% for full-length 16S and about 100% for V4. (Edgar 2018)
  Holds for: an abstract.
  Evidence: derived; a single source.
- As biomass fell in a dilution series, contaminants made up a growing share of inferred communities under every sequence-inference method; the authors state no inference method alone separates contaminants from true sequences. (Caruso et al. 2019)
  Holds for: a dilution series.
  Evidence: measured; a single source.
- According to its documentation, DADA2's independent per-sample processing needs at least two error-free reads to detect an ASV, and pooling finds more ASVs per sample. (Callahan n.d.)
  Holds for: DADA2 documentation.

### chimera formation and detection

Builds on: PCR conditions, cycle number and per-cycle efficiency, denoising, clustering, OTUs and ASVs.

- Chimeras formed reproducibly across independent amplifications of a known mixture; that chimera formation is reproducible rests on this one study, on Sanger and 454 data. (Haas et al. 2011)
  Holds for: a known mixture, Sanger and 454.
  Evidence: measured; a single source.
- Less-abundant species showed chimera rates above 70% on 454, and chimera count correlated with organism abundance (R2 = 0.97) in a staggered mock. (Haas et al. 2011)
  Holds for: 454; a staggered mock.
- ChimeraSlayer detected over 87% of simulated chimeras when parents diverged by 4% or more, with a 1.6% false-positive rate, and sensitivity fell for every method as parents became more similar. (Haas et al. 2011)
  Holds for: simulated chimeras.
- At 30 cycles, chimeras made up 0.9% (Accuprime) to 18.2% (Platinum) of reads, depending on polymerase. (Sze and Schloss 2019)
  Holds for: 30 cycles; verified.
- UCHIME sensitivity was 50 to 87% at 25 or more cycles. (Sze and Schloss 2019)
  Holds for: 25 or more cycles.
- UCHIME2's author states that error-free chimera prediction is "impossible in principle". (Edgar 2016)
  Holds for: a developer claim in a preprint abstract.
- Chimeras inflate richness and create false novel taxa. (Haas et al. 2011; Sze and Schloss 2019)
  Holds for: as stated in the answers.

### taxonomic assignment and reference databases

Builds on: denoising, clustering, OTUs and ASVs.

- Cross-validated by identity to the reference, all tested classifiers were at most 50% accurate on V4; genus accuracy was about 100% at 100% identity and about 50% at 97%, derived from reference sets by one author who also develops competing classifiers. (Edgar 2018)
  Holds for: V4, reference sets; accuracy depends on distance to reference.
  Evidence: measured; a single source.
- Edgar 2018b's author argues that mocks overstate classification accuracy because all their members are named type strains. (Edgar 2018)
  Holds for: an argument.
- On mocks, the q2-feature-classifier methods reached median genus F above 0.8. (Bokulich et al. 2018)
  Holds for: mocks; a developer claim.
  Evidence: measured.
- Habitat-weighted priors cut species-level classification error from 25% to 14%. (Kaehler et al. 2019)
  Holds for: a developer claim.
  Evidence: measured.
- IDTAXA over-classified less when the true taxa were absent from the training set. (Murali et al. 2018)
  Holds for: a developer claim; the reference is listed under Murali and cited by the bioinformatics angle.
  Evidence: measured.
- Estimated annotation error in reference databases is about 10% for RDP and about 17% for SILVA v128 and Greengenes 13.5, judged from conflicting labels on identical sequences; this rests on one author who also develops competing classifiers. (Edgar 2018)
  Holds for: RDP, SILVA v128, Greengenes 13.5.
  Evidence: derived; a single source.
- On simulated gut, ocean and soil communities, genus recall was 67 to 80%, and assignments varied by up to 40% between 16S subregions within a pipeline. (Almeida et al. 2018)
  Holds for: simulated gut, ocean and soil communities.
  Evidence: modelled; a single source.
- On V4 mocks, 56 to 88% of predicted genus names were false positives with closed-reference OTUs. (Edgar 2017)
  Holds for: V4 mocks.
  Evidence: measured; a single source.

### reagent and cross-sample contamination

Builds on: DNA extraction.

- In a Salmonella bongori dilution series run at three institutes, contaminants dominated by about 10^3 cells, more so at 40 than at 20 cycles, and contaminant profiles differed by kit and laboratory. (Salter et al. 2014)
  Holds for: a dilution series at three institutes.
  Evidence: measured; replicated.
- In an 8-member mock diluted 3-fold eight times, contaminant reads rose from 0.1% to 80.1% and ASVs from 18 to 381. (Karstens et al. 2019)
  Holds for: one diluted 8-member mock.
  Evidence: measured; a single source.
- Removing every sequence present in the negative control wrongly removed more than 20% of expected sequences, since three of the eight mock ASVs appeared in the control. (Karstens et al. 2019)
  Holds for: one diluted 8-member mock.
  Evidence: measured; a single source.
- decontam's frequency method removed 70 to 90% of contaminants and no expected sequences. (Karstens et al. 2019)
  Holds for: one diluted 8-member mock.
  Evidence: measured; a single source.
- SourceTracker removed over 98% of contaminants when sources were well defined but failed on over 97% when they were not. (Karstens et al. 2019)
  Holds for: one diluted 8-member mock.
  Evidence: measured; a single source.
- Well-to-well contamination arose mainly at extraction, less at library preparation, mostly into neighbouring wells (rarely up to 10 wells away), and was greatest in low-biomass samples. (Minich et al. 2019)
  Holds for: well-to-well contamination.
  Evidence: measured; a single source.
- Contamination varies inversely with biomass and is specific to the kit and laboratory. (Karstens et al. 2019; Minich et al. 2019; Salter et al. 2014)
  Holds for: as stated.
- decontam's makers describe a frequency mode that assumes contaminant DNA is roughly constant across samples. (Davis et al. 2018)
  Holds for: a developer claim.
- A review proposes the RIDE checklist. (Eisenhofer et al. 2019)
  Holds for: a review.
  Evidence: asserted.
- The most abundant spurious taxon in mocks had a median relative abundance of 0.12%. (Reitmeier et al. 2021)
  Holds for: mocks.

### which steps dominate the departure

Builds on: DNA extraction, PCR conditions, cycle number and per-cycle efficiency, denoising, clustering, OTUs and ASVs, reagent and cross-sample contamination, chimera formation and detection.

- The ordering in which DNA extraction is the largest source of relative-abundance error, followed by PCR and then sequencing, rests on one 7-taxon vaginal dataset (Brooks 2015, reanalysed by McLaren 2019), with Albertsen 2015 (sludge, bead beating only) as partial support; it is contested by Fouhy 2016 (two extraction methods gave very similar data) and qualified by MBQC (specimen type mattered more than extraction), and is a single-dataset result, not a field-wide ordering. (Albertsen et al. 2015; Vaginal et al. 2015; Fouhy et al. 2016; McLaren et al. 2019; The et al. 2017)
  Holds for: one 7-taxon vaginal dataset, 454.
  Evidence: a single source; rated "Strong" by the research; a second reader disputes this: firmer than the access and source base allow.
- In the reanalysed 7-taxon cell mixtures, PCR followed extraction (maximum pairwise bias 5.2, mean 2.3), then sequencing and classification (maximum 1.6, mean 1.2). (McLaren et al. 2019)
  Holds for: 80 cell mixtures of 7 vaginal taxa, V1-V3, 454.
  Evidence: derived and modelled; a single source.
- In the same cell mixtures, total bias was a maximum of 29.3-fold and a mean of 5.6-fold, smaller than extraction bias alone, which implies partial cancellation between steps. (McLaren et al. 2019)
  Holds for: 80 cell mixtures of 7 vaginal taxa.
  Evidence: derived and modelled; a single source.
- Across 15 laboratories, variability depended most on specimen type, then DNA extraction, then handling laboratory, then bioinformatics. (The et al. 2017)
  Holds for: the MBQC interlaboratory study, whole workflow.
  Evidence: measured; a single source.
- For the number of taxa detected, inflation by spurious sequences (sequencing error, chimeras, cross-sample leakage, reagent contamination) and by the choice of clustering or denoising is replicated across independent mocks and dilution series: 10 to 200-fold excess units, and contaminants rising from 0.1% to 80.1% of reads in a diluted mock; these can change counts of taxa by one to two orders of magnitude. (Karstens et al. 2019; Straub et al. 2020)
  Holds for: mocks and dilution series.
  Evidence: replicated; rated "Strong" by the research; a second reader disputes this: moderate for the inflation of taxon counts.
- Per-step magnitudes of departure mostly come from one or two small mocks (7 to 20 taxa), often on 454 or Ion Torrent. (the reviewer's and critic's account of the evidence base)
  Holds for: mocks of 7 to 20 taxa.
  Evidence: rated "Magnitudes per step are moderate" by the research; a second reader disputes this: weak for per-step relative-abundance magnitudes.

### whether the departure is consistent across samples

Builds on: DNA extraction, primers and gene region, PCR conditions, cycle number and per-cycle efficiency, copy number against read abundance, prediction and correction.

- Modelling each step as multiplying taxon abundances by a taxon-specific efficiency, McLaren et al. found that the error in taxon ratios was "consistent across samples", while the error in proportions "varied dramatically in both magnitude and direction", in the one dataset modelled for this question (the vaginal cell mixtures; extraction bias was consistent on the ratio scale within a protocol); an abstract-level source cited in the second review describes bias in sequencing measurements as a consistent multiplicative factor per taxon that calibration controls can correct, while field evidence of inconsistency (Parada, abstract only, one primer pair) is weighed as limiting. (McLaren et al. 2019)
  Holds for: 7 taxa mixed as cells and reanalysed.
  Evidence: modelled; a single source.
  A second reader found the search for contrary evidence one-sided.
- Six parameters explained almost all systematic error in the cell mixtures, and calibration cut mean Bray-Curtis error from 0.35 to 0.08 (92.6% lower mean squared error); this result comes from the Brooks et al. 2015 16S cell mixtures (2 calibration samples, 69 calibrated samples), not from a shotgun dataset. (McLaren et al. 2019)
  Holds for: the Brooks 16S cell mixtures.
  A second reader found the search for contrary evidence one-sided.
- A 10-species shotgun spike-in across faecal backgrounds also gave a consistent profile on the ratio scale, with protocol H showing up to 2,751-fold maximum pairwise bias; this is known only via McLaren 2019, and its calibration is reported only qualitatively ("removed most of the systematic error"). (Costea et al. 2017)
  Holds for: shotgun, faecal backgrounds; secondary and indirect.
  Evidence: limited by access (a source was not read in full; not the same as weak evidence).
- McLaren et al. list where the ratio model may fail: PCR saturation, taxa aggregated with differing efficiencies, matrix differences between controls and samples, and taxa absent from the controls. (McLaren et al. 2019)
  Holds for: their model.
- On the same data, Brooks et al. found significant mixture-blending terms and concluded that one taxon's observed proportion depends on which others are present; the two readings conflict, and McLaren's attributes the apparent dependence to working on the proportion scale. (Vaginal et al. 2015; McLaren et al. 2019)
  Holds for: the Brooks 2015 cell mixtures.
  Evidence: contested.
- Bias varies between sample types or samples: a field-versus-mock SAR11 bias for the 515F-Y/806R pair (abstract only), inconsistent cycle effects in four stool samples, extraction yield of 40 to 84%, and a 66.7-fold spike-in range (abstract). (Parada et al. 2016; Sze and Schloss 2019; Zemb et al. 2020; Zhou et al. 2011)
  Holds for: field and mock samples, stool samples, spike-ins.
  Evidence: measured; the sources differ.
- A 0.1% genomic spike was recovered at 0.06% to 5.34% of reads across soils, a 66.7-fold range; the 66.7-fold figure is in the abstract, and the 0.06 to 5.34% range, which needs the body, could not be confirmed. (Zhou et al. 2011)
  Holds for: soils.
  Evidence: measured; a single source; limited by access (a source was not read in full; not the same as weak evidence).
- Whether mock-derived bias applies to field samples is disputed: Parada 2016 against the calibration claims of McLaren 2019 and Silverman 2021. (McLaren et al. 2019; Parada et al. 2016; Silverman et al. 2021)
  Holds for: field samples against calibration claims.
- Evidence on whether bias is consistent across samples rests mainly on one reanalysis of 7 taxa, with contrary or limiting field evidence; ratio-scale consistency is shown in one 16S cell-mixture dataset and one shotgun spike-in known only secondarily, and the ratio-consistency claim would weaken substantially without McLaren 2019 and its source data. (Vaginal et al. 2015; Costea et al. 2017; McLaren et al. 2019)
  Holds for: one 16S cell-mixture dataset and one secondary shotgun spike-in.
  Evidence: rated "weak to moderate" by the research; a second reader disputes this: weak for consistency across samples.
- A review states that PCR-based estimates can deviate by "several orders of magnitude" if extraction, PCR, copy number and analysis errors are ignored. (Bonk et al. 2018)
  Holds for: a review.
  Evidence: asserted.
- No mock study in a soil matrix with known composition was found, and the consistency of extraction bias across real soil or water matrices has not been measured in the sources found; soil evidence comes from spike-ins, dilutions and relic DNA. (a search result)
  Holds for: soil and water matrices.
  Evidence: a search result.
  Searched for and not found.
- No archaeal-rich mock was found beyond Pinto and Raskin 2012 and D'Amore 2016. (D'Amore et al. 2016; Pinto and Raskin 2012)
  Holds for: archaeal-rich mocks.
  Evidence: a search result.
  Searched for and not found.
- In eukaryotic eDNA, modelling the PCR process, calibrated with mocks, has been used to estimate starting proportions. (Shelton et al. 2023)
  Holds for: eukaryotic eDNA, indirect; an abstract.
  Evidence: modelled.

### reads per sample and variation between samples

Builds on: library preparation, indexing and sequencing error.

- The Earth Microbiome Project averaged 80,000 sequences per sample over 27,751 samples and rarefied to 5,000. (Thompson et al. 2017)
  Holds for: the EMP survey.
- In four environments of the EMP, mean prevalence of tag sequences rose with depth up to 50,000, so rarefying to 5,000 under-estimated prevalence. (Thompson et al. 2017)
  Holds for: four environments of the EMP.
- In one 360-sample MiSeq run, reads averaged 9,913 pairs per sample, with 95% of samples above 2,454; these figures need the paper's body and could not be confirmed. (Kozich et al. 2013)
  Holds for: one MiSeq run.
  Evidence: limited by access (a source was not read in full; not the same as weak evidence).
- A dilution-series run ranged from 40,927 to 251,419 reads per sample. (Karstens et al. 2019)
  Holds for: one dilution-series run.
- Three mock runs gave 36,464 to 146,653 read pairs. (Prodan et al. 2020)
  Holds for: three mock runs.
- Across 12 public V4 studies, reads per sample varied up to about 100-fold within a study, for example human 10,439 to 422,904 (median 32,452, n = 490), bioethanol 3,690 to 356,027, mice 1,804 to 30,311, soil 46,622 to 58,935 (n = 18) and marine 132,895 to 256,758 (n = 7); these are per-study, not per-run, ranges. (Schloss 2024)
  Holds for: 12 public V4 studies; per study, not per run.
  Evidence: measured; a single source; rated "Moderate for reads per sample per study" by the research.
- Schloss attributes the spread of reads per sample to compounding random error when PCR products are pooled. (Schloss 2024)
  Holds for: 12 public V4 studies.
- Schloss cites studies reporting that sequencing depth correlates positively with biomass despite normalisation; the two primary studies (one on 101 fish species, one on an equivolumetric protocol) are known only secondarily and were not opened. (Schloss 2024)
  Holds for: known secondarily via Schloss 2024b.
  Evidence: limited by access (a source was not read in full; not the same as weak evidence).
- The Illumina guide states more than 20 million reads per MiSeq v3 run and more than 100,000 per sample at 96-plex, said to be "sufficient to fully survey the bacterial composition". (Illumina n.d.)
  Holds for: a maker's claim.
- A core facility protocol gives about 20 million (v3) and about 16 million (v2) reads per run, with more than 100,000 reads per sample recommended. (Emory n.d.)
  Holds for: a protocol, a maker's statement.
- Median Good's coverage ranged from 89.4% (seagrass) to 99.8% (human), and reaching 95% and 99% coverage required about 3 and 101 times the sequences needed for 90%. (Schloss 2024)
  Holds for: 12 public V4 studies.
  Evidence: deriv (note: "(Schloss 2024b) [deriv]").
- No peer-reviewed coefficient of variation of reads per sample within a run after equimolar pooling was found; web search returned only forum posts. (a search result)
  Holds for: all three search angles.
  Evidence: a search result; rated "Absent for the within-run coefficient of variation" by the research.
  Searched for and not found.

### total microbial load

- Microbial load differed up to tenfold among healthy human individuals' faeces. (Vandeputte et al. 2017)
  Holds for: human faeces.
  Evidence: measured; replicated.
- Prokaryote load in Antarctic seawater differed 27-fold among stations. (Lin et al. 2019)
  Holds for: Antarctic seawater.
  Evidence: measured; a single source.
- Microbial load in the mouse gut spanned more than six orders of magnitude across sites. (Barlow et al. 2020)
  Holds for: mouse gut sites.
  Evidence: measured; a single source.

### shape of taxon abundance distributions

Builds on: reads per sample and variation between samples.

- A species abundance distribution describes how many species in a community are common and how many rare; every community shows a hollow curve, with many rare species and just a few common species. (McGill et al. 2007)
  Background, not from the research.
- For 24 grassland soils, the best-fitting abundance distributions the review reports (exponential or inverse gamma) are in supplementary Table S3; the main text does not state which distributions won, and they were not verified. (Zhou et al. 2013)
  Holds for: 24 grassland soils.
  Evidence: modelled; a single source; limited by access (a source was not read in full; not the same as weak evidence).
- In a Brazil soil, 26,079 reads and 2,880 observed species were fitted equally well by communities of 10^4, 10^5 and 10^6 species, so the tail of the distribution cannot be identified from sample data; these figures rest on a full text that was not openly retrievable and could not be confirmed. (Haegeman et al. 2013)
  Holds for: one Brazil soil.
  Evidence: modelled; replicated; limited by access (a source was not read in full; not the same as weak evidence).
- After copy-number correction, rank-abundance distributions from ocean and human skin fit a lognormal better, in a single study that pools ocean and skin into one item and whose own simulations assumed a lognormal. (Kembel et al. 2012)
  Holds for: ocean and human skin, pooled.
  Evidence: a single source.
- Lognormal dynamics best explained microbial abundance distributions across more than 20,000 samples; the abstract gives no per-environment breakdown, so soil is not reported separately. (Shoemaker et al. 2017)
  Holds for: cross-environment compilation including soils; abstract only.
  Evidence: modelled; a single source.
- A dominance scaling law held across about 35,000 sites. (Locey and Lennon 2016)
  Holds for: a cross-environment compilation; the abstract does not report soil separately.
- Mean abundances across taxa were lognormal "for all the data sets considered"; per-biome results are in supplementary figures that were not read. (Grilli 2020)
  Holds for: all the data sets considered; partly re-opened.
  Evidence: modelled; a single source.
- Soil abundance-distribution shape conflicts between exponential or inverse gamma fits and lognormal ones, but these use different fitting targets, so the conflict is only partial; one analysis argues the tail is not identifiable from sample data at all. (Grilli 2020; Haegeman et al. 2013; Shoemaker et al. 2017; Zhou et al. 2013)
  Holds for: soil.
  Evidence: contested.
- Abundance-distribution shapes split by environment are weaker than presented, because the field-wide sources do not separate soil, water and host. (the reviewer's and critic's assessment)
  Holds for: soil, water and host samples.
  Evidence: rated "Weak for abundance-distribution shapes split by environment" by the research.
- Abundance-distribution shapes reported separately for water and for host-associated 16S data were not found, beyond the copy-correction fits for ocean and skin, although per-biome supplementary figures and an unread full text exist. (Grilli 2020; Shoemaker et al. 2017)
  Holds for: water and host-associated 16S data.
  Evidence: a search result.
  Searched for and not found.
- In bulk-soil global amplicon datasets, a small minority of taxa carries a large share of reads and most taxa are rare; this qualitative shape is replicated across global amplicon datasets and older clone and reassociation studies. (Bickel and Or 2021; Delgado-Baquerizo et al. 2018)
  Holds for: bulk soil, amplicon reads.
  Evidence: replicated; rated "Moderate for the qualitative shape" by the research.
- Across 237 soils, per-sample richness ranged from 774 to 2,869 phylotypes, and 511 of 25,224 phylotypes (2%), defined as dominant jointly by abundance (top 10% by share of reads) and ubiquity (present in more than half of the soils), accounted on average for 41% of 16S reads per sample, more than half in arid forests and only about 20% in tropical forests. (Delgado-Baquerizo et al. 2018)
  Holds for: 237 soils, bulk soil, amplicon reads; per-sample mean.
- Across 844 soils (318 sites, 90-bp V4 ASVs), 0.4% of ASVs were classed common on the globally pooled rank-abundance distribution and held about 58% of pooled relative abundance, while the 99.6% classed rare held 42%. (Bickel and Or 2021)
  Holds for: 844 soils, pooled global relative abundance.
- The dominant-fraction shares of the two global soil datasets (2% holding about 41% of reads per sample, and 0.4% holding about 58% of pooled relative abundance) use different definitions and denominators and must not be combined. (Bickel and Or 2021; Delgado-Baquerizo et al. 2018)
  Holds for: two global soil amplicon datasets.
- Drier soils had more even abundance distributions, and the ratio of rare to common richness declined with rainfall frequency (Pearson r = -0.41, n = 318). (Bickel and Or 2021)
  Holds for: 318 sites.
- Across 146 soils, archaeal reads averaged 2% of 16S reads (0 to over 10%), and two Thaumarchaeota (then Crenarchaeota) phylotypes made up over 70% of archaeal sequences; this rests on one abstract-only study of 2010-era 454 data. (Bates et al. 2011)
  Holds for: 146 soils, 454.
  Evidence: a single source.
- By DNA reassociation kinetics, which measure whole-community DNA rather than reads or cells, a power law described the soil abundance distribution best, implying over a million distinct genomes in a pristine soil, and metal pollution cut diversity by over 99.9%; this is the main contrary result on the shape of the distribution. (Gans et al. 2005)
  Holds for: whole-community DNA; a pristine soil.
- Four Arizona soils were consistent with lognormal null models; small surveys reproduced richness but not composition, and documenting half the species would need 16,284 to 44,000 individuals. (Dunbar et al. 2002)
  Holds for: clone libraries and models, four Arizona soils.
- Lognormal-based estimates gave 6,400 to 38,000 taxa per gram of soil. (Curtis et al. 2002)
  Holds for: soil.
  Evidence: modelled.
- Soils may need hundreds of times current sampling to reach 90% of taxa, and diversity estimates depend on the distribution assumed. (Quince et al. 2008)
  Holds for: soil.
- The functional form of the abundance distribution (lognormal against power law) is contested: a power law from reassociation kinetics against a lognormal from clone-library models and large amplicon compilations; it is method-dependent, and most of this evidence is abstract-only or modelled. (Curtis et al. 2002; Dunbar et al. 2002; Gans et al. 2005; Shoemaker et al. 2017)
  Holds for: the studies cited.
  Evidence: contested; rated "Weak for the functional form" by the research.
- No soil taxon abundance distribution built from metagenome coverage was found; the search did not cover genome-resolved global soil metagenomes. (a search result)
  Holds for: soil metagenomes.
  Evidence: a search result.
  Not searched for.
- Iowa corn and prairie soil metagenomes totalled about 300 Gbp, yet 80% of reads could not be assembled for low coverage, and 48% and 31% of contigs had coverage below 10x. (Howe et al. 2014)
  Holds for: Iowa corn and prairie soils.
- Tropical soils are among the least-covered communities by Nonpareil estimates. (Rodriguez-R and Konstantinidis 2014)
  Holds for: qualitative.
- 85% of the amplicon-defined dominant soil phylotypes were also dominant in 123 shotgun soil metagenomes, the only global amplicon-metagenome cross-check. (Delgado-Baquerizo et al. 2018)
  Holds for: 123 shotgun soil metagenomes.
- No taxon abundance distribution from cell counts in soil was found; cell-based soil data found concern only total DNA per cell, and taxon-specific cell counts (CARD-FISH or FISH) were not searched beyond abundance-distribution queries, a narrow route. (a search result)
  Holds for: soil.
  Evidence: a search result; rated "Absent for cell-count-based distributions in soil" by the research.
  Searched for and not found.
- Absolute-abundance work multiplies relative abundance by total counts (flow cytometry or qPCR), which converts gene copies but not cells per taxon. (Props et al. 2017)
  Holds for: non-soil.
- Not found as such: copy-number- or ploidy-corrected abundance distributions for soil, metagenome-based taxon abundance distributions reported as a distribution, and rhizosphere-specific abundance distributions. (a search result)
  Holds for: soil and rhizosphere.
  Evidence: a search result.
  The research does not say whether this was searched for.

### sampling from the amplified pool

Builds on: reads per sample and variation between samples, shape of taxon abundance distributions.

- Technical replicates of the same soil DNA amplified with different barcodes shared 17.2 ± 2.3% of OTUs between two replicates and 8.2 ± 2.3% among three on 454; these figures are in the paper's abstract. (Zhou et al. 2011)
  Holds for: soil technical replicates, 454.
  Evidence: measured; a single source.
- The paper's discussion gives 13.1% and 5.9% for the replicate overlaps, which differ from its abstract; these values need the body and could not be confirmed. (Zhou et al. 2011)
  Holds for: soil technical replicates, 454.
  Evidence: limited by access (a source was not read in full; not the same as weak evidence).
- A Poisson random-sampling model of long-tailed abundance distributions predicted the low OTU overlap among soil technical replicates, with no significant difference from the observed values; it modelled the same 24 Oklahoma grassland soils, sequenced on 454, that the replicate study reported, and the low replicate overlap was attributed to random sampling. (Zhou et al. 2013)
  Holds for: one dataset of 24 Oklahoma grassland soils, 454.
  Evidence: modelled; a single source.
  A second reader found the search for contrary evidence one-sided.
- About 60,900 sequences per replicate were predicted to be needed for 90% OTU overlap. (Zhou et al. 2013)
  Holds for: the soil technical replicates.
  Evidence: modelled; a single source.
- MiSeq replicates from the same laboratory cut against pure sampling: unweighted overlap plateaued at 39% near 30,000 reads (with singletons) and reached only 43.9% at 160,000 reads, far below the predicted 90% at about 60,900; the authors attribute rare-OTU variation to random sampling plus sequencing artefacts, report that "biases other than random sampling" affect unweighted metrics more, and found lower overlap when replicates were sequenced in separate runs. (Wen et al. 2017)
  Holds for: MiSeq replicates from the same laboratory.
- That Poisson or multinomial sampling explains replicate disagreement in taxa detected rests on one 454 dataset of 24 Oklahoma soils (reported by Zhou 2011 and modelled by Zhou 2013) and one laboratory, whose Wen 2017 study does not fit the model; it is weak and contested that sampling alone explains replicate disagreement in taxa detected. (Wen et al. 2017; Zhou et al. 2013; Zhou et al. 2011)
  Holds for: soil, one dataset and one laboratory.
  Evidence: contested; rated "Moderate" by the research; a second reader disputes this: weak and contested that sampling alone explains replicate disagreement.
- For one caecal extract with four technical replicates, the abundance at which the CV of relative abundance reached 30% fell with the square root of read depth, as Poisson noise would predict. (Barlow et al. 2020)
  Holds for: one caecal extract, four technical replicates.
  Evidence: measured; a single source.
- The assumption that technical replicates are Poisson comes from RNA-seq, where Illumina lane replicates fit a Poisson model with about 0.5% of genes deviating; McMurdie and Holmes adopt it for technical replicates, but it rests on RNA-seq, not on 16S technical replicates. (Marioni et al. 2008; McMurdie and Holmes 2014)
  Holds for: RNA-seq lane replicates, indirect.
  Evidence: measured.
- Each taxon's abundance across communities followed a gamma distribution with variance proportional to the squared mean (Taylor's law with exponent 2); with finite read sampling this predicted each species' occupancy from its mean and variance with no further parameters and reproduced the abundance-occupancy relationship, so absences are attributed mostly to sampling; the text read does not name soil among the biomes. (Grilli 2020)
  Holds for: datasets across biomes; non-soil, nearest precedent.
  Evidence: modelled; a single source.
- The conflict between sampling as the cause of replicate variation and technical variance beyond counting is partly one of setting and measure (OTU overlap against variance of relative abundance), a caution applied to the technical-variance side but not to the sampling side. (Dyrhovden et al. 2021; Grilli 2020; Silverman et al. 2018; Zhou et al. 2013)
  Holds for: OTU overlap against variance of relative abundance.
  A second reader found the search for contrary evidence one-sided.

### overdispersed count models

Builds on: sampling from the amplified pool.

- Between biological samples, human oral plaque counts rejected the multinomial in favour of the Dirichlet-multinomial, with overdispersion theta of 0.047 and 0.054. (La Rosa et al. 2012)
  Holds for: human oral plaque, biological samples.
  Evidence: measured; replicated.
- Every public dataset surveyed showed more variance than Poisson among biological replicates. (McMurdie and Holmes 2014)
  Holds for: biological replicates in public datasets.
  Evidence: measured; replicated.
- Hierarchical Dirichlet-multinomial models detected shifts better than alternatives in simulation. (Harrison et al. 2020)
  Holds for: simulation.
  Evidence: modelled; a single source.
- Beta-binomial and logistic-normal network models relax the multinomial further, by their makers' account. (Martin et al. 2020; Willis and Martin 2022)
  Holds for: makers' claims.
- Dirichlet-multinomial overdispersion has been shown only between biological samples; no study fitting overdispersion to 16S technical replicates at controlled depths was found. (a search result)
  Holds for: the statistics angle's search.
  Evidence: a search result.
  Searched for and not found.

### processes other than sampling

Builds on: sampling from the amplified pool, PCR conditions, cycle number and per-cycle efficiency.

- In four artificial-gut vessels sampled hourly with 20 technical replicates per vessel, 76% of observed variation was attributed to technical sources beyond sequence counting; this rests on one study. (Silverman et al. 2018)
  Holds for: four artificial-gut vessels, hourly sampling.
  Evidence: modelled; a single source.
- PCR replicates split before PCR differed strongly while replicates split after PCR were nearly identical; in negative extraction controls, most species appeared in only one of five PCR replicates (mean Jaccard distance 0.80, range 0.65 to 0.87). (Dyrhovden et al. 2021)
  Holds for: negative extraction controls; low load.
  Evidence: measured; a single source.
- At a 1:10^5 dilution of a staggered mock, 12 species appeared in only 2 of 4 PCR replicates. (Dyrhovden et al. 2021)
  Holds for: a staggered mock.
- At low input, library preparation reached its Poisson loading limit, the two rarest taxa dropped out, and contaminants appeared below about 10^4 copies. (Barlow et al. 2020)
  Holds for: low input.
- Synthetic barcode pools showed the same stochastic early-amplification mechanism. (Kebschull and Zador 2015)
  Holds for: synthetic barcode pools, indirect.
- One HiSeq run lost an archaeal mock taxon from all samples and shifted others by more than 2-fold, while re-running the same amplicons was normal. (Yeh et al. 2018)
  Holds for: one HiSeq run.
  Evidence: measured; a single source.
- A PCR machine with a mis-set annealing temperature produced a batch outlier. (Silverman et al. 2021)
  Holds for: one study.
- Per-strain CV across five runs had a median of 11.8% (range 5.5 to 73.7%), and under-represented strains varied most. (Laursen et al. 2017)
  Holds for: five runs.
- Mean relative abundances were reproducible across two runs and two depths. (Pinto and Raskin 2012)
  Holds for: Pinto and Raskin 2012.
- Interlaboratory differences were substantial. (The et al. 2017)
  Holds for: the MBQC interlaboratory study.
- Batch-correction tools exist, and their makers claim they work. (Gibbons et al. 2018; Ling et al. 2022)
  Holds for: makers' claims.
- Primer mismatch and low efficiency remove or suppress specific taxa, a non-random dropout. (Parada et al. 2016; Walters et al. 2016)
  Holds for: primer studies.
- In eDNA simulations with a low-efficiency primer set, a median of 88 of 1,000 taxa were detected after 20 cycles. (Kelly et al. 2019)
  Holds for: eDNA simulations, indirect.
  Evidence: modelled.
- In simulation, simple count models sufficed across four zero-generating processes, and zero inflation was warranted only under narrow conditions. (Silverman et al. 2020)
  Holds for: simulation.
  Evidence: modelled; a single source.
- Pseudocounts made tests conservative. (Kaul et al. 2017)
  Holds for: an abstract.
  Evidence: modelled; a single source.
- Schloss asserts that a microbiome zero more likely means true absence, which conflicts with the interpretation of absences as sampling. (Grilli 2020; Schloss 2024)
  Holds for: an assertion.
  Evidence: asserted.
- Technical variance beyond counting, early stochastic amplification at low load, whole-run taxon loss and primer-driven dropout are measured, but each mostly in a single study. (Dyrhovden et al. 2021; Silverman et al. 2018; Yeh et al. 2018)
  Holds for: single studies (Silverman 2018; Dyrhovden 2021; Yeh 2018).
  Evidence: a single source; rated "Weak on how much non-sampling technical variance there is" by the research.

### technical replicates at different read depths

Builds on: sampling from the amplified pool.

- In one soil sample, abundance-weighted OTU overlap among technical replicates rose from 56.7% at 2,000 reads to 95.3% at 160,000, and Bray-Curtis among technical replicates was 0.269 against 0.374 among treatment replicates. (Wen et al. 2017)
  Holds for: one soil sample.
  Evidence: measured; replicated.
  A second reader found the search for contrary evidence one-sided.
- On MiSeq, 18 soil extracts shared 33.4% of OTUs between two technical replicates and 20.2% among three, and in one deeply sequenced sample presence/absence overlap rose from 20.7% at 2,000 reads to 43.9% at 160,000, plateauing near 30,000. (Wen et al. 2017)
  Holds for: 18 soil extracts, MiSeq.
- Greater depth improved replicate agreement in beta diversity for some mocks only. (Pinto and Raskin 2012)
  Holds for: Pinto and Raskin 2012.
- A preprint reports technical-replicate Jaccard distances of typically about 0.15, and up to 0.71 across runs. (Edgar 2017)
  Holds for: a preprint abstract.
- In ITS data, OTUs averaging more than 10 reads were detected in nearly all replicates, and replicate dissimilarity (pseudo-beta-diversity) fell markedly with depth. (Smith and Peay 2014)
  Holds for: ITS, indirect.
- Replicate variation affected beta diversity more than alpha diversity in one study (Zhou 2011), and in another alpha diversity did not differ among technical replicates (Wen 2017). (Wen et al. 2017; Zhou et al. 2011)
  Holds for: technical replicates.
- Replicate agreement rises with read depth. (Barlow et al. 2020; Smith and Peay 2014; Wen et al. 2017; Zhou et al. 2013)
  Holds for: the four studies named (Wen 2017; Zhou 2013; Smith and Peay 2014; Barlow 2020).
  Evidence: rated "Moderate for the depth dependence of replicate agreement" by the research.
  A second reader found the search for contrary evidence one-sided.
- Not found: a 16S study testing whether technical-replicate variance of relative abundance exceeds multinomial expectation across controlled read depths, and replicate-at-depth studies in water or in host samples other than gut; replicate-at-depth studies are confined to one soil laboratory and one mouse caecum. (a search result)
  Holds for: soil dominates the replicate-at-depth evidence.
  Evidence: a search result.
  Searched for and not found.

### rarefying and rarefaction to a common depth

Builds on: reads per sample and variation between samples, scaling normalisations from RNA-seq, compositional data analysis and log-ratios.

- Rarefaction comes from ecology, traced to Sanders 1968, Hurlbert 1971 and Simberloff 1972, which are known only through Chao and Jost 2012. (Chao and Jost 2012; Hurlbert 1971; Sanders 1968; Simberloff 1972)
  Holds for: ecology.
  Evidence: limited by access (a source was not read in full; not the same as weak evidence).
- Gotelli and Colwell argue that individual-based rarefaction allows meaningful comparison and that asymptotic estimators give lower bounds. (Gotelli and Colwell 2001)
  Holds for: indirect evidence.
  Evidence: asserted.
- Schloss distinguishes "rarefying" (one random subsample) from "rarefaction" (the mean over many subsamples). (Schloss 2024)
  Holds for: terminology.
- Under multinomial-type null models built from 12 V4 datasets, only rarefaction removed the correlation between richness and depth (size-based iNEXT nearly did, except for the small, evenly sequenced marine and soil sets), and when depth was confounded with group only rarefaction and size-based iNEXT held a 5% false-positive rate, with rarefaction giving the highest power; this is the author's conclusion from modelled data. (Schloss 2024)
  Holds for: null models from 12 V4 datasets.
  Evidence: modelled.
- The null model reassigns sequences at random, so samples differ only through multinomial-type sampling; taxon-specific bias, technical variation beyond counting, and differences in load are absent from the simulated truth. (Schloss 2024)
  Holds for: the null model (the statistics angle's reading).
  Evidence: the reviewer's reading.
- Repeated rarefying shows that the random variation rarefying introduces grows as rarefied depth shrinks. (Cameron et al. 2021)
  Holds for: one study.
  Evidence: measured; a single source.
- Whether to rarefy is contested: McMurdie and Holmes 2014 against Schloss 2024a and 2024b, Weiss 2017 and, in part, Hong 2022, with Willis 2019 opposing rarefying for richness; no approach is shown to correct depth, load and taxon-specific bias together. (Hong et al. 2022; McMurdie and Holmes 2014; Schloss 2024; Schloss 2024; Weiss et al. 2017; Willis 2019)
  Holds for: answers depend on the simulation design.
  Evidence: contested; rated "Weak to moderate overall" by the research.
- Rarefaction is favoured for alpha and beta diversity under depth confounding in null-model simulations dominated by one author (supported in part by Weiss 2017 for beta and differential abundance); without Schloss 2024b, rarefying would remain contested, with McMurdie and Holmes 2014 as the main benchmark against it. (McMurdie and Holmes 2014; Schloss 2024; Weiss et al. 2017)
  Holds for: null-model simulations.
- In the review's summary, rarefying or rarefaction removes depth dependence of alpha and beta diversity under the null and controls false positives under confounding, but loses data and power, adds variance when done once, gave high differential-abundance false-positive rates in one benchmark, is argued to bias richness, and does not touch bias or load; it applies to all three measures and is contested. The summary table mixes makers' claims and simulation results with measured results without a per-cell evidence class. (Hong et al. 2022; McMurdie and Holmes 2014; Schloss 2024; Weiss et al. 2017; Willis 2019)
  Holds for: the review's summary by approach.
- Rarefaction curves display sampling completeness (ecology) and were not benchmarked as a comparison method in the sources found. (the review's summary)
  Holds for: the review's summary by approach.
- Simulation results on rarefying and its alternatives flip with design choices, as Weiss 2017 and Schloss 2024a both say. (Hong et al. 2022; Schloss 2024; Weiss et al. 2017)
  Holds for: simulation benchmarks.

### scaling normalisations from RNA-seq

Builds on: rarefying and rarefaction to a common depth.

- In RNA-seq, total-count scaling can bias differential-expression estimates. (Bullard et al. 2010)
  Holds for: RNA-seq, indirect.
- TMM and DESeq's negative binomial model also come from RNA-seq, and both assume most features are unchanged between conditions. (Anders and Huber 2010; Robinson and Oshlack 2010; Weiss et al. 2017)
  Holds for: RNA-seq, indirect.
- In shotgun gene-abundance data, TMM and RLE performed best. (Buongermino Pereira et al. 2018)
  Holds for: shotgun gene-abundance data, indirect.
- Scaling normalisations used on microbiome data (TMM, RLE, CSS, VST, SRS, Wrench) come from RNA-seq (indirect evidence) and assume most features do not change, and under Schloss's null model they did not remove depth effects. (Anders and Huber 2010; Bullard et al. 2010; Robinson and Oshlack 2010; Schloss 2024)
  Holds for: Schloss's null model; RNA-seq origins indirect.
- In a simulation, RLE and VST came close to quantitative methods for association tests in a dysbiosis scenario. (Llorens-Rico et al. 2021)
  Holds for: a simulation, dysbiosis scenario.
- Wrench's makers state that library-size scaling and rarefaction cannot correct compositional bias that is uncorrelated with library size. (Kumar et al. 2018)
  Holds for: a makers' claim.
- SRS's makers claim better reproducibility than rarefying. (Beule and Karlovsky 2020)
  Holds for: a makers' claim.
- In the review's summary, scaling methods (TMM, RLE, CSS, VST, SRS, Wrench) show some FDR and power benefits at small n (DESeq2) and come close to quantitative methods in a dysbiosis simulation, but are depth-sensitive for beta and alpha diversity under the null, assume most taxa unchanged, and DESeq2's FDR rises with n and uneven libraries; the summary table mixes evidence classes without a per-cell label. (Llorens-Rico et al. 2021; Schloss 2024; Weiss et al. 2017)
  Holds for: the review's summary by approach; differential abundance and beta diversity.

### compositional data analysis and log-ratios

Builds on: rarefying and rarefaction to a common depth.

- A review argues that 16S data are compositions "at all stages" and should be analysed with log-ratios. (Gloor et al. 2017)
  Holds for: a review.
  Evidence: asserted; contested.
- In the review's summary, compositional (log-ratio) approaches give ratio fold changes invariant to load and to multiplicative bias, and ANCOM and ALDEx2 are conservative, but Aitchison distances are depth-sensitive under the null, ANCOM-BC shows type I inflation in some settings, and results are sensitive to pseudocounts; the summary table mixes evidence classes without a per-cell label. (Kaul et al. 2017; McLaren et al. 2019; Nearing et al. 2022; Schloss 2024; Yang and Chen 2022)
  Holds for: the review's summary by approach; differential abundance and beta diversity.

### richness and other alpha diversity measures

Builds on: rarefying and rarefaction to a common depth, sampling from the amplified pool, shape of taxon abundance distributions.

- Chao1, ACE, CatchAll, Shannon and Simpson all varied with library size in pyrosequencing data. (Gihring et al. 2012)
  Holds for: pyrosequencing data.
  Evidence: measured; replicated.
- In Schloss's null models built from 12 V4 datasets, observed richness, Chao1, ACE, breakaway and SRS-normalised richness all correlated with depth. (Schloss 2024)
  Holds for: null models from 12 V4 datasets.
  Evidence: modelled; contested.
- Shannon was less depth-sensitive and inverse Simpson was not depth-sensitive; Simpson-type indices are robust. (Haegeman et al. 2013; Schloss 2024)
  Holds for: the two studies named.
- The depth dependence of raw and estimator richness is replicated. (Gihring et al. 2012; Haegeman et al. 2013; Schloss 2024)
  Holds for: the three studies named.
  Evidence: replicated.
- In the synthesis agent's re-reading of the full text, coverage-based iNEXT estimates were among those that "showed a strong correlation between richness and the number of sequences", and the text exempts only "rarefaction and possibly the size-based iNEXT estimates"; this is the only microbial amplicon test of coverage-based standardisation found, and beyond it the evidence is non-microbial. (Schloss 2024)
  Holds for: Schloss 2024b's null models.
  Evidence: a single source.
- Chao and Jost argue that standardising by sample completeness rather than size gives less biased richness ratios. (Chao and Jost 2012)
  Holds for: indirect evidence.
  Evidence: modelled.
- Hill-number extrapolation is reliable only to about 2 to 3 times the reference sample size for richness. (Chao et al. 2014)
  Holds for: indirect evidence.
  Evidence: modelled.
- A 2026 test on terrestrial inventories finds coverage-based rarefaction "does not respond predictably" to richness. (Alroy 2026)
  Holds for: terrestrial inventories, non-microbial, abstract only.
  Evidence: modelled; a single source.
- Coverage-based standardisation is disputed: Chao and Jost 2012 against Alroy 2026 (both non-microbial) and the microbial null model in Schloss 2024b. (Alroy 2026; Chao and Jost 2012; Schloss 2024)
  Holds for: two non-microbial studies and one microbial null model.
- In the review's summary, coverage-based standardisation compresses richness ratios less than size-based rarefaction (ecology, modelled) but fails on terrestrial inventories and is depth-correlated in a microbial null model. (Alroy 2026; Chao and Jost 2012; Schloss 2024)
  Holds for: the review's summary by approach; alpha diversity.
- No independent microbial benchmark of coverage-based standardisation was found. (a search result)
  Holds for: the statistics angle's search.
  Evidence: search (note: "An independent microbial benchmark of coverage-based standardisation (statistics angle)").
  Searched, not found (note: "an independent microbial benchmark of coverage-based standardisation (statistics angle)").
- Willis argues that plug-in and rarefied richness are both negatively biased, and that rarefying can create false differences between environments with equal richness but different abundance structures; she recommends estimators with variance estimates compared through measurement-error models, and presents statistical argument plus a worked simulated example. (Willis 2019)
  Holds for: one paper.
  Evidence: contested.
  A second reader found the search for contrary evidence one-sided.
- Breakaway and betta are offered by their makers as estimators with variance estimates. (Willis and Bunge 2015; Willis et al. 2017)
  Holds for: makers' claims.
- Breakaway intervals were mostly too wide to be useful, and breakaway stayed correlated with depth. (Schloss 2024)
  Holds for: one study.
- Sample data carry no information on the rare tail, and Chao's estimator ranked in silico communities wrongly: a community with 20 times fewer species was estimated to have 10 times more. (Haegeman et al. 2013)
  Holds for: in silico communities.
- Bounds for Hill numbers of order 2 and above nearly coincide, and the authors recommend Shannon and Simpson over richness. (Haegeman et al. 2013)
  Holds for: Haegeman et al.'s analysis.
  Evidence: modelled; replicated.
- Chao1 and ACE are invalid on ASV tables from algorithms that drop singletons, as DADA2 does by default. (Deng et al. 2024)
  Holds for: ASV tables.
  Evidence: asserted; a single source.
- Spurious OTUs severely inflated Chao1, and removing them severely underestimated Chao1 in uneven communities, while abundance-weighted metrics were little affected. (Pinto and Raskin 2012)
  Holds for: Pinto and Raskin 2012.
- An abundance filter makes ACE and Chao1 inapplicable. (Bokulich et al. 2013)
  Holds for: Bokulich et al.'s quality filtering.
- Spurious singletons inflate richness estimators, and a singleton-replacement estimator for error-inflated data has been proposed. (Chiu and Chao 2016; Pinto and Raskin 2012)
  Holds for: a proposed estimator.
  Evidence: modelled; a single source.
- Multiplicative bias can make an uneven sample look more even, biasing Shannon and inverse Simpson. (McLaren et al. 2019)
  Holds for: McLaren et al.'s model.
  Evidence: model (note: "(McLaren 2019) [model]").
- PCR-bias calibration improved Shannon diversity in 7 of 10 mocks. (Silverman et al. 2021)
  Holds for: 10 mocks.
- In simulated faecal communities with load varying from 1.9 x 10^9 to 10^13 cells per gram, all 13 transformations reproduced Shannon and Simpson diversity. (Llorens-Rico et al. 2021)
  Holds for: simulated faecal communities.
- In simulated faecal communities, richness was recovered reliably only by quantitative profiling in a bloom scenario. (Llorens-Rico et al. 2021)
  Holds for: simulated faecal communities, bloom scenario.
  Evidence: modelled; a single source.
- In freshwater and sediment 454 data, 5,000 sequences captured Shannon trends and over 80% of Chao1 trends. (Lundin et al. 2012)
  Holds for: freshwater and sediment, 454.
  Evidence: measured; a single source.
- In the review's summary, richness estimators give lower bounds and extrapolation to about 2 to 3 times sample size (ecology), but are depth-correlated, have unidentifiable tails, are invalid without singletons and are inflated by spurious singletons. (Chao et al. 2014; Deng et al. 2024; Haegeman et al. 2013; Schloss 2024)
  Holds for: the review's summary by approach; alpha diversity.

### normalisation for beta diversity

Builds on: rarefying and rarefaction to a common depth.

- In Schloss's null models, Jaccard and Bray-Curtis computed from raw counts, relative abundances, CSS or SRS, Aitchison distances (four zero-handling variants) and DESeq2 VST Euclidean distances all correlated with depth differences; only rarefaction removed the correlation, and only rarefaction held 5% false positives in PERMANOVA under confounding. (Schloss 2024)
  Holds for: Schloss's null models.
- Rarefying clustered samples better for presence/absence metrics, and other normalisations were vulnerable below about 1,000 reads per sample. (Weiss et al. 2017)
  Holds for: Weiss 2017, modelled.
  Evidence: modelled; replicated.
- In simulations from Global Patterns, rarefying to the 15th percentile and dropping samples below it reduced clustering accuracy. (McMurdie and Holmes 2014)
  Holds for: simulations from Global Patterns.
  Evidence: modelled; contested.
- Schloss identified 11 design choices that disadvantaged rarefying in the McMurdie and Holmes study; notably, low-depth samples were removed only in the rarefied arm. (Schloss 2024)
  Holds for: a re-analysis of the McMurdie and Holmes study.
  Evidence: modelled; a single source.
- Proportions and rarefying were the only methods that fully normalised depth, and scaling methods masked differences in common OTUs; under Schloss's null, proportions were still depth-sensitive. (McKnight et al. 2019)
  Holds for: an abstract.
  Evidence: modelled; a single source.
- Whether proportions normalise depth for beta diversity conflicts between studies: McKnight 2019 against Schloss 2024b, in which relative-abundance Bray-Curtis stayed depth-sensitive under the null. (McKnight et al. 2019; Schloss 2024)
  Holds for: the two studies named.
  Evidence: contested.
- In real river data, rarefying barely changed Bray-Curtis or Jaccard (r > 0.9) and did not change weighted UniFrac. (Chiarello et al. 2022)
  Holds for: real river data.
- Library-size normalisation had very little effect on beta-diversity separation compared with the choice of distance metric. (Thorsen et al. 2016)
  Holds for: an abstract.
  Evidence: measured; a single source.
- 1,000 denoised sequences explained 90% of the Bray-Curtis trends seen at 15,000 to 20,000 sequences. (Lundin et al. 2012)
  Holds for: freshwater and sediment, 454.
- Bray-Curtis was usually the most powerful beta-diversity metric, and metric choice changes power. (Kers and Saccenti 2022)
  Holds for: an abstract.
  Evidence: measured; a single source.
- Evidence on how to normalise for beta diversity is contested and simulation-based. (McMurdie and Holmes 2014; Schloss 2024; Weiss et al. 2017)
  Holds for: simulations.
  Evidence: contested.

### tests of which taxa differ in abundance

Builds on: rarefying and rarefaction to a common depth, whether the departure is consistent across samples.

- Studies disagree on whether rarefying harms differential-abundance tests. (Hong et al. 2022; McMurdie and Holmes 2014; Weiss et al. 2017; Yang and Chen 2022)
  Holds for: the studies named.
  Evidence: contested.
- Rarefied counts and proportions gave high false-positive rates, while DESeq2 and edgeR were near zero. (McMurdie and Holmes 2014)
  Holds for: McMurdie and Holmes 2014.
- Rarefying did not raise FDR for most methods, and lowered it at about 10x group differences in library size, at a cost in sensitivity. (Weiss et al. 2017)
  Holds for: Weiss 2017.
- DESeq2's FDR rose with more samples or uneven libraries, and ANCOM alone controlled FDR well. (Weiss et al. 2017)
  Holds for: Weiss 2017.
- Rarefying followed by permutation controls type I error; the sensitivity loss is negligible when overdispersion is high, and is summarised by a rarefaction efficiency index. (Hong et al. 2022)
  Holds for: Hong et al.'s analysis.
  Evidence: modelled; a single source.
- Tests on proportions at a tenfold depth difference had severe type I inflation, which rarefying controlled, and no method was "simultaneously robust, powerful, and flexible"; ANCOM-BC showed type I inflation in some settings. (Yang and Chen 2022)
  Holds for: Yang and Chen 2022, modelled.
  Evidence: modelled; replicated.
- Fourteen differential-abundance methods on 38 datasets gave 0.8% to 40.5% significant ASVs (unfiltered means). (Nearing et al. 2022)
  Holds for: 38 real datasets.
- ALDEx2 and ANCOM-II were the most consistent across 38 datasets, and edgeR and LEfSe produced many false positives on random splits. (Nearing et al. 2022)
  Holds for: 38 real datasets.
  Evidence: measured; a single source.
- Excess false discoveries were widespread across differential-abundance methods. (Hawinkel et al. 2019)
  Holds for: an abstract.
  Evidence: modelled; replicated.
- Methods with the highest false-positive rates had the most power. (Thorsen et al. 2016)
  Holds for: Thorsen et al.'s benchmark.
- Microbiome-specific methods did not beat RNA-seq methods. (Calgaro et al. 2020)
  Holds for: an abstract.
  Evidence: measured; a single source.
- In implanted-signal benchmarks, only linear models, Wilcoxon, t-test, limma and fastANCOM controlled FDR at relatively high sensitivity; fitZig reached an observed FDR of 80%, and ANCOM and ANCOM-BC controlled FDR only at 200 or more samples per group. (Wirbel et al. 2024)
  Holds for: implanted-signal benchmarks.
  Evidence: modelled; replicated.
- Elementary methods on relative abundances (Wilcoxon, linear models) were the most replicable across 53 studies. (Pelto et al. 2025)
  Holds for: 53 studies; an abstract.
  Evidence: measured; a single source.
- Makers claim FDR control for ANCOM-BC and ANCOM, and independent benchmarks disagree in part. (Lin and Peddada 2020; Mandal et al. 2015; Wirbel et al. 2024; Yang and Chen 2022)
  Holds for: makers' claims against independent benchmarks.
- Reference frames make differential rankings invariant to load. (Morton et al. 2019)
  Holds for: an abstract.
  Evidence: measured; a single source.
- Fold changes in taxon ratios are invariant to multiplicative bias; fold changes in proportions are not and can change sign; this bias-invariance of ratio-based methods rests on one source. (McLaren et al. 2019)
  Holds for: one source (McLaren 2019).
- Proportion-based differential-abundance results err when the community's mean efficiency is associated with the condition. (McLaren et al. 2022)
  Holds for: a preprint abstract.
  Evidence: modelled; a single source.
- Differential-abundance results show large disagreement between methods and frequent FDR failures, robustly; which method is best is contested. (Hawinkel et al. 2019; Nearing et al. 2022; Wirbel et al. 2024; Yang and Chen 2022)
  Holds for: the four benchmarks named.
  Evidence: contested.
- In the review's summary, proportions are simple, and elementary tests on proportions were replicable and FDR-controlling in some benchmarks, but showed severe type I error with large depth differences, depth-sensitive beta diversity, and proportion error that varies with sample composition. (McLaren et al. 2019; Pelto et al. 2025; Schloss 2024; Wirbel et al. 2024; Yang and Chen 2022)
  Holds for: the review's summary by approach; differential abundance and beta diversity.

### absolute quantification of total load

Builds on: total microbial load, rarefying and rarefaction to a common depth, whether the departure is consistent across samples.

- Load measurements (qPCR, flow cytometry, dPCR and spike-ins) change, and can reverse, conclusions drawn from relative data; this is replicated. (Barlow et al. 2020; Props et al. 2017; Tkacz et al. 2018; Vandeputte et al. 2017)
  Holds for: the four studies named.
  Evidence: replicated.
- Flow-cytometry quantitative profiling showed the Bacteroides-Prevotella trade-off in relative data to be an artefact, and load drove Crohn's-associated differences. (Vandeputte et al. 2017)
  Holds for: an abstract.
- In engineered freshwater, relative enrichment did not imply absolute outgrowth. (Props et al. 2017)
  Holds for: engineered freshwater; an abstract.
- In soil, absolute abundance could hold steady or rise while relative abundance fell. (Tkacz et al. 2018)
  Holds for: soil.
- Spike-in bacteria added before extraction recovered ratios of absolute abundances across mouse faecal dilutions, but the three spike-in species gave different read yields. (Stammler et al. 2016)
  Holds for: mouse faecal dilutions.
  Evidence: measured; replicated.
- dPCR anchoring gave about 2x extraction accuracy above 8.3 x 10^4 input copies, and absolute but not relative analysis revealed diet effects. (Barlow et al. 2020)
  Holds for: one study.
  Evidence: measured; a single source.
- Soil internal standards tracked PLFA and respiration biomass better than those two measures tracked each other. (Smets et al. 2016)
  Holds for: soil; an abstract.
  Evidence: measured; a single source.
- Total 16S qPCR multiplied by relative abundance correlated near-perfectly with taxon-specific qPCR, a comparison of methods that share an upstream (qPCR against qPCR-anchored sequencing) for four taxa. (Jian et al. 2020)
  Holds for: four taxa.
  Evidence: measured; a single source.
- In simulation, experimental quantitative profiling outperformed computational transformations for associations. (Llorens-Rico et al. 2021)
  Holds for: simulation.
- Absolute quantification addresses differences in load but does not remove taxon-specific extraction and PCR bias. (Bonk et al. 2018; McLaren et al. 2019)
  Holds for: as stated.
- qPCR and sequencing both count extracellular DNA, unlike cell counts. (Jian et al. 2020)
  Holds for: as stated.
- qPCR and flow cytometry agreed on a whole-cell mock (|r| = 0.967) but gave "highly divergent" profiles for faeces, where qPCR and flow-cytometry enumeration correlated at Pearson r = -0.50; ddPCR correlated strongly with qPCR, and the authors used this to rule out qPCR imprecision as the cause of the divergence. (Galazzo et al. 2020)
  Holds for: a whole-cell mock and faeces.
  Evidence: measured; a single source.
- Synthetic spike-ins had differing detection efficiencies and small departures from linearity, and correlations were weaker with Taq than with KOD polymerase. (Tourlousse et al. 2017)
  Holds for: synthetic spike-in standards.
  Evidence: measured; replicated.
- Seawater internal standards agreed with flow cytometry at r2 = 0.19 until corrections for copy number and particle association (with four outliers removed) raised it to 0.61, and the authors conclude that the internal-standard method is quantitative and consistent with flow cytometry; the r2 figures need the body and could not be verified. (Lin et al. 2019)
  Holds for: seawater.
  Evidence: measured; a single source; limited by access (a source was not read in full; not the same as weak evidence).
  A second reader found the search for contrary evidence one-sided.
- A review states that internal standards often underperform or fail. (Harrison et al. 2021)
  Holds for: a review.
  Evidence: asserted.
- The evidence on agreement between absolute-quantification methods is weak: on qPCR against flow cytometry, Jian 2020 and Galazzo 2020 conflict, and the divergence of the methods rests on Galazzo 2020. (Galazzo et al. 2020; Jian et al. 2020)
  Holds for: the two studies named.
  Evidence: rated "weak on the agreement between quantification methods" by the research.
- In the review's summary, absolute load measurements correct differences in total load and reversals of relative trends, but not taxon-specific bias, extraction-yield variation, or disagreement between qPCR and flow cytometry; they apply to all three measures and are strongest for differential abundance and associations. (the review's summary)
  Holds for: the review's summary by approach.
- No approach is shown to correct depth, load and taxon-specific bias together: no benchmark builds taxon-specific bias and differences in total load into the simulated truth together, apart from one that simulated faeces without taxon bias; no benchmark in soil or water used measured absolute loads as truth; and no richness correction was tested against known-richness mocks across depths. (Llorens-Rico et al. 2021)
  Holds for: the statistics angle's routes (Europe PMC, Crossref, publisher HTML, author PDFs, web search) and the lab and bioinformatics angles for spike-ins.
  Evidence: a search result.
  Searched for and not found.

### within-sample abundance terms and the rare biosphere

Builds on: shape of taxon abundance distributions.

- Three families of definition of abundance and distribution terms are in use and are not interchangeable: within-sample relative-abundance thresholds (0.1% most common for rare, 1% for abundant), occupancy (core, mostly occurrence-only, 30 to 100%), and regional or global classes defined on pooled data; usage is heterogeneous and often unstated, and the usage percentages rest on two surveys. (Neu et al. 2021; Pascoal et al. 2025)
  Holds for: microbial ecology literature; two systematic literature surveys plus reviews.
  Evidence: rated "Strong on the fact of heterogeneity" by the research.
- Within a sample, rare is most often defined as below 0.1% of reads, sometimes below 0.01% or 0.001%, and abundant usually as above 1%; one of the sources cited for these thresholds uses a single rare/common cutoff and does not support "abundant above 1%". (Dai et al. 2016; Galand et al. 2009; Jia et al. 2022; Lynch and Neufeld 2015)
  Holds for: within-sample relative abundance.
- The "rare biosphere" entered usage with deep-sea tag sequencing, which found thousands of low-abundance populations alongside a few dominants. (Sogin et al. 2006)
  Holds for: deep sea.
- Reviews describe a few dominant taxa and many rare ones without fixing a threshold. (Lynch and Neufeld 2015; Pascoal et al. 2021; Pedros-Alio 2012)
  Holds for: reviews.
- Rare has been defined as below 0.01% and abundant as above 1% per sample, a cutoff the authors called "much more severe than the <0.1% criteria proposed earlier" and tied to a singleton in the smallest library. (Galand et al. 2009)
  Holds for: per sample.
- Rare below 0.1% and abundant above 1% were combined with behaviour across samples into six categories: always abundant, conditionally abundant, always rare, conditionally rare, moderate, and conditionally rare or abundant. (Dai et al. 2016)
  Holds for: one study.
- In a survey of 181 rare-biosphere articles from 2006 to 2024, about 37% gave no clear method or definition; of those with one, about 84% used relative abundance thresholds and about 60% of those a single threshold, about half used 0.1%, and about 70% applied it per sample rather than to the pooled dataset. (Pascoal et al. 2025)
  Holds for: 181 articles; the most systematic usage survey.
- Conditionally rare taxa are defined by a bimodal abundance distribution over time (coefficient of bimodality) together with a maximum relative abundance above 1%; across 42 non-soil time series they made up 1.5 to 28% of membership. (Shade et al. 2014)
  Holds for: 42 non-soil time series.
- A three-way split into permanently, transiently and conditionally rare taxa has been applied in soil. (Jia et al. 2022)
  Holds for: soil.
- Across 30 datasets (1,998 samples), rarer taxa better predicted soil community structure; this abstract-level source does not report abundance-occupancy and is not used in the answers. (Ramirez and others 2018)
  Holds for: 30 soil datasets; an abstract.
- No survey was found that tallies definitions specifically within soil studies, or separately for bulk soil and rhizosphere. (a search result)
  Holds for: soil.
  Evidence: a search result.
  Searched for and not found.
- No study was found that compares threshold-based rarity classes between amplicon and metagenome data from the same soil samples; the ulrb comparison of amplicon and metagenome units used marine samples. (Pascoal et al. 2025)
  Holds for: soil.
  Evidence: a search result.
  Searched for and not found.
- Copy-number-corrected rarity thresholds were not found to have been tested. (a search result)
  Holds for: as stated.
  Evidence: a search result.
  Searched for and not found.

### occupancy, prevalence and the core

Builds on: within-sample abundance terms and the rare biosphere.

- "Core" is the main occupancy term; it was first framed as the members shared across samples, the overlap of Venn diagrams, with later calls to add persistence and connectivity. (Shade and Handelsman 2012)
  Holds for: core-microbiome literature.
- In a survey of 224 core-microbiome studies, 75.4% defined the core by occurrence only, 4% by relative abundance only and 11.6% by both, with over 18% not stating a method; occurrence cutoffs ran from 30% to 100% of samples (100% most common), and abundance cutoffs in combined methods from 0.1% to 4.5%. (Neu et al. 2021)
  Holds for: 224 studies; the only survey of core usage.
- Citing other work, Neu et al. report that only two OTUs were shared by all of 24 soil locations and none across 51 wastewater plants. (Neu et al. 2021)
  Holds for: soil and wastewater; secondary.
  Evidence: limited by access (a source was not read in full; not the same as weak evidence).
- Risely distinguishes five kinds of core (common, temporal, ecological, functional, host-adapted) and argues that no one definition captures all. (Risely 2020)
  Holds for: a review.

### regional and global distribution terms

Builds on: within-sample abundance terms and the rare biosphere.

- In soil, "dominant" has been defined jointly: in the top 10% of phylotypes by share of 16S reads and present in more than half of 237 soils. (Delgado-Baquerizo et al. 2018)
  Holds for: 237 soils.
- "Common" versus "rare" has also been set by a data-driven minimum cross-entropy threshold on the globally pooled rank-abundance distribution, about 0.019% of pooled relative abundance, with prevalence across samples reported separately. (Bickel and Or 2021)
  Holds for: the globally pooled rank-abundance distribution.
- Reviews treat habitat specificity and geographic range as microbial rarity axes alongside local abundance. (Jousset et al. 2017)
  Holds for: reviews.
- Terms are used inconsistently: "dominant" sometimes means abundant within a sample and sometimes abundant and ubiquitous, and "common" means high pooled abundance in one study and high occupancy elsewhere. (Bickel and Or 2021; Delgado-Baquerizo et al. 2018)
  Holds for: microbial ecology literature.

### rarity and occupancy frameworks from general ecology

Builds on: within-sample abundance terms and the rare biosphere, occupancy, prevalence and the core.

- Rabinowitz (1981) classifies rarity by geographic range, habitat specificity and local abundance; its microbial users state these concepts "can be easily transferred to microbial communities". (Jousset et al. 2017; Rabinowitz 1981)
  Holds for: general ecology; known only secondarily.
  Evidence: limited by access (a source was not read in full; not the same as weak evidence).
- In a 21-year estuarine fish record, persistent and abundant "core" species fitted a lognormal, while infrequent "occasional" species fitted a log series. (Magurran and Henderson 2003)
  Holds for: estuarine fish.
- The same split is reported for rare against abundant Arctic Ocean prokaryotes: log series against lognormal. (Galand et al. 2009)
  Holds for: Arctic Ocean prokaryotes.
- Positive intraspecific and interspecific abundance-occupancy relationships are general in the British flora and fauna; in general macroecology positive relationships are common and multiple explanations have been tested. (Gaston et al. 2000)
  Holds for: British flora and fauna; general macroecology.

### whether classifications and conclusions hold across thresholds

Builds on: within-sample abundance terms and the rare biosphere, occupancy, prevalence and the core.

- In a salt-marsh soil chronosequence (Schiermonnikoog, five stages over 110 years, amplicon ASVs), the rare fraction of reads was 61.6%, 45.7% and 28.4% at cutoffs of 0.2%, 0.1% and 0.05%. (Jia et al. 2022)
  Holds for: one salt-marsh chronosequence.
- As the cutoff tightened, permanently and transiently rare ASVs fell in proportion, conditionally rare ASVs rose, and the relative importance of selection rose, while beta-diversity patterns and the main assembly inference (homogeneous selection for the rare biosphere, variable selection for the common) were reported as similar across cutoffs: classification changed, the qualitative conclusion held; this is the only soil test of threshold sensitivity found. (Jia et al. 2022)
  Holds for: one soil test.
  Evidence: a single source.
- In Arctic Ocean data, the biogeography of rare taxa persisted at a 0.001% cutoff. (Galand et al. 2009)
  Holds for: Arctic Ocean.
- In coastal sand data, ecological patterns were maintained after removing up to 35 to 40% of rare sequences. (Gobet et al. 2010)
  Holds for: coastal sands.
- In marine samples, the 0.1% per-sample rule gave more rare than abundant ASVs with V4V5 amplicons and the reverse with full-length 16S, and threshold-based classes behaved differently across OTUs, ASVs and metagenomic OTUs, while the unsupervised method gave the same pattern across these. (Pascoal et al. 2025)
  Holds for: marine samples.
- Four core methods compared on human faecal (319 samples) and Arabidopsis root (288 samples) data assigned 1.2% to 9.4% of taxa as core, nearly 10-fold apart; 165 to 176 taxa were agreed by all four, which is 13 to 16% of core assignments. (Custer et al. 2023)
  Holds for: human faecal and Arabidopsis root data.
- In the human data, a temporal effect significant in the full dataset was reported as not significant in core-based analyses, but the source's text is internally inconsistent on whether core analyses gained or lost the temporal effect. (Custer et al. 2023)
  Holds for: human data.
- Occupancy-based core methods were most accurate in simulations, in one simulation study. (Custer et al. 2023)
  Holds for: simulations.
  Evidence: a single source.
- In sponges, core definitions changed alpha and beta diversity in some cases but not conclusions on host specificity, environmental quality or networks, and the authors call the approach "surprisingly robust". (Astudillo-Garcia et al. 2017)
  Holds for: sponges.
- In human gut, core size depended mostly on analysis depth and required prevalence. (Salonen et al. 2012)
  Holds for: human gut.
- On Loess Plateau soils, two primer pairs gave different diversity responses to land use, so rare and abundant classes depend on the primer, not only the cutoff. (Zeng and An 2021)
  Holds for: Loess Plateau soils.
- Tests of threshold sensitivity point both ways and are each single-system: some report conclusions that hold across thresholds or definitions, others classifications or conclusions that change; these are not strictly contradictory because they test different outputs (membership counts against beta-diversity or assembly inferences). (Astudillo-Garcia et al. 2017; Custer et al. 2023; Galand et al. 2009; Gobet et al. 2010; Jia et al. 2022; Pascoal et al. 2025; Salonen et al. 2012)
  Holds for: one system per test.
  Evidence: a single source; rated "Moderate on threshold sensitivity" by the research.
- Proposed standards include unsupervised clustering (ulrb), multivariate cutoff analysis (also recommended for rare-biosphere assembly work), abundance-occupancy ranking with a neutral-model fit to prioritise core members, and explicit reporting with explicit spatial and temporal scale of the core, deep sequencing and no rarefying when quantifying the core; no proposed standard was found to be widely adopted. (Gobet et al. 2010; Jia et al. 2018; Neu et al. 2021; Pascoal et al. 2025; Shade and Stopnisek 2019)
  Holds for: proposals.

### local abundance and occupancy across soils

Builds on: shape of taxon abundance distributions, occupancy, prevalence and the core, regional and global distribution terms, sampling from the amplified pool.

- In 88 North and South American soils (about 1,500 reads per soil), the ten most abundant OTUs per sample occurred on average in 28% of soils, against 2% for all OTUs; in 27 tropical forest soils within one hectare, the figures were 69% against 8%; these figures could not be verified, and the source's abstract frames the study across Earth's major habitat types, not soils alone. (Nemergut et al. 2011)
  Holds for: bulk soil.
  Evidence: limited by access (a source was not read in full; not the same as weak evidence).
- Total abundance and the number of soils occupied were significantly and positively related, with no coefficient given; summed abundance rises with occupancy, so the measure is partly built in by construction. (Nemergut et al. 2011)
  Holds for: 88 American soils; 27 tropical forest soils.
- The authors note that abundant taxa may simply be easier to detect, and that undersampling could hide intermediate distributions. (Nemergut et al. 2011)
  Holds for: soils.
- Across 844 global soils, median prevalence was 0.3 for common taxa and 0.001 for rare taxa; this is a class-level contrast in which the common class is defined on the globally pooled rank-abundance distribution, and pooled abundance rises mechanically with prevalence, so it is a different measure from a taxon-level abundance-occupancy relationship. (Bickel and Or 2021)
  Holds for: 844 global soils.
- Across about 124,000 taxa in 3.41 km2 of urban park soil, occupancy correlated strongly with environmental range; abundance was not the axis tested. (Barberan et al. 2014)
  Holds for: urban park soil.
- A global list of dominant soil taxa cannot serve as an independent test of the abundance-occupancy relationship, because dominance there is defined by abundance and ubiquity together. (Delgado-Baquerizo et al. 2018)
  Holds for: the global dominant list.
- Soil also holds taxa that are abundant at some times or places and rare elsewhere: 2,197 conditionally rare ASVs alongside 11,838 permanently rare and 8,333 transiently rare ASVs in a soil chronosequence; such taxa cut against a uniform abundance-occupancy relationship. (Jia et al. 2022; Shade et al. 2014)
  Holds for: one soil chronosequence.
- In the two bulk-soil amplicon studies with figures, more abundant taxa occupy more soils, but the two are not fully independent (one reanalysed compiled datasets including the Earth Microbiome Project, which plausibly overlaps the other's soils), both measures are partly built in by construction, detection limits (a single 454-era study at one site) and neutral or sampling models predict a positive relationship without selection, and no soil test against a sampling null was found; whether a relationship exists beyond sampling, and how strong it is, is unresolved. (Bickel and Or 2021; Nemergut et al. 2011)
  Holds for: bulk soil, amplicon data; the sampling-null evidence is non-soil.
  Evidence: unclear; rated "Moderate for the existence of a positive relationship in amplicon data from bulk soil" by the research; a second reader disputes this: unresolved beyond sampling.
  A second reader found the search for contrary evidence one-sided.
- In common bean rhizospheres across four US regions plus a Colombian dataset, 48 bacterial and archaeal taxa were detected in every sample, and fitting a neutral model to the abundance-occupancy distribution, 13.7% of bacterial and archaeal taxa deviated from neutral expectation; samples were rarefied to 31,255 reads, and this rhizosphere figure rests on one study. (Stopnisek and Shade 2021)
  Holds for: common bean rhizosphere.
- In 4,866 maize rhizosphere samples, seven OTUs were present in all, five of them responsive to host genotype. (Walters et al. 2018)
  Holds for: maize rhizosphere.
- In Arabidopsis root data, core size varied 7-fold among methods. (Custer et al. 2023)
  Holds for: Arabidopsis root data.
- Rhizosphere evidence is limited to core-membership studies of two to three crops, none of which reports an abundance-occupancy correlation coefficient in the passages read; no systematic search for every crop rhizosphere core study was run. (Stopnisek and Shade 2021; Walters et al. 2018)
  Holds for: rhizosphere.
  Evidence: a search result.
  Not searched for.
- In the reviewer's argument, low-abundance taxa are often recorded absent when present, which by itself would produce lower occupancy for rarer taxa; the one source behind it (454 pyrosequencing, 24 communities from one Oklahoma warming site) attributes low replicate overlap to random sampling but does not draw the occupancy conclusion. (Zhou et al. 2011)
  Holds for: one 454-era study at one site.
  Evidence: the reviewer's reading.
- Pyrosequencing errors inflated rare-tail richness. (Kunin et al. 2010)
  Holds for: pyrosequencing.
- Better clustering cut richness by 30 to 60% but did not remove the long tail. (Huse et al. 2010)
  Holds for: one study.
- A global common-rare threshold was robust to using a quarter of the samples. (Bickel and Or 2021)
  Holds for: as stated.
- A neutral community model with immigration and drift only predicts that abundant taxa occur in more samples, so a positive abundance-occupancy relationship is expected without selection, and its use in the common bean study treats deviations, not the relationship itself, as signal. (Sloan et al. 2006; Stopnisek and Shade 2021)
  Holds for: neutral community model.
- The same positive relationship is read as ecological signal by some authors and as near-null by others; the reviewer notes this is a difference of interpretation, not of data. (Sloan et al. 2006)
  Holds for: abundance-occupancy studies.
  Evidence: the reviewer's reading.
- Neutral-model fits in soil exist as many single studies, which were not pooled. (the review's search record)
  Holds for: soil.
- No soil study was found that tests whether the observed bulk-soil abundance-occupancy relationship exceeds what sampling and detection alone would produce; explicit sampling or occupancy-detection models applied to soil microbes were not searched beyond a neutral-model query. (a search result)
  Holds for: bulk soil; a Europe PMC query for abundance-occupancy with soil or rhizosphere (25 hits reviewed by title) and a neutral-model query.
  Evidence: a search result.
  Not searched for.
- None found: abundance-occupancy relationships in soil from cell counts or from metagenomes, copy-number- or ploidy-corrected soil relationships, archaea-specific relationships in soil, or bulk soil and rhizosphere compared within one study. (a search result)
  Holds for: soil.
  Evidence: a search result.
  Searched for and not found.

## Do not say

Wordings the research itself says are wrong or overstated, each with the reason and what to say instead.

- Do not write: "In 2018, 30% of 16S amplicon studies reported a negative control and 10% a positive control."
  Why: The survey covered 265 papers in two journals that used any high-throughput community sequencing (16S, shotgun, metatranscriptomics, ITS, 18S and others), so it is not a 16S-only figure, and it is a single source.
  Say instead: In a survey of 265 papers in the 2018 issues of Microbiome and The ISME Journal that used any high-throughput community sequencing (16S, shotgun, metatranscriptomics, ITS, 18S and others), 30% (79) reported a negative control and 10% (27) a positive control; it is not a 16S-only figure. (Hornung et al. 2019)
  Holds for: two journals, 2018, all high-throughput community sequencing types, not 16S amplicon practice alone.
  Evidence: measured; a single source; rated "weak" by the research.
- Do not write: "No source was found on how water sampling or host-tissue sampling choices affect composition."
  Why: On the review's own Search record no angle searched water or host-tissue sampling choices, so they are unsearched, not "not found"; the review's section 2.1 says the opposite.
  Say instead: Field sampling choices for water (volume, filter pore size) and for host tissue are unsearched on the review's own Search record, so no source on their effect was reported. (the review's search record)
  Holds for: water sampling and host tissue sampling; section 2.1 says the lab angle searched preservation and storage terms, the Search record says no angle searched these choices.
  Evidence: a search result.
  Not searched for.
- Do not write: "Departures from community composition were found at every step of the workflow."
  Why: Field sampling for water and host tissue was not searched, and several choices showed no detectable effect, so departures were measured at most steps examined, not at every step.
  Say instead: Departures are measured at most steps examined but not at all of them: field sampling for water and host tissue was not searched, and several choices showed little or no detectable effect (PCR replicate pooling, preparation day and lane, cycle number in some studies, and storage in one soil, relative to between-soil differences). (the critic's reading of the review's body and search record)
  Holds for: the steps the body examined.
  The research does not say whether contrary evidence was searched for.
- Do not write: "DNA extraction is the largest source of relative-abundance error, followed by PCR and then sequencing."
  Why: The ordering rests on one 7-taxon vaginal dataset (Brooks 2015, reanalysed by McLaren 2019), is contested by Fouhy 2016 and qualified by MBQC, and should be presented as a single dataset, not as a field-wide ordering.
  Say instead: The ordering in which DNA extraction is the largest source of relative-abundance error, followed by PCR and then sequencing, rests on one 7-taxon vaginal dataset (Brooks 2015, reanalysed by McLaren 2019), with Albertsen 2015 (sludge, bead beating only) as partial support; it is contested by Fouhy 2016 (two extraction methods gave very similar data) and qualified by MBQC (specimen type mattered more than extraction), and is a single-dataset result, not a field-wide ordering. (Albertsen et al. 2015; Vaginal et al. 2015; Fouhy et al. 2016; McLaren et al. 2019; The et al. 2017)
  Holds for: one 7-taxon vaginal dataset, 454.
  Evidence: a single source; rated "Strong" by the research; a second reader disputes this: firmer than the access and source base allow.
- Do not write: "Many independent mock studies agree on which steps dominate the error, so the ordering is strongly supported."
  Why: The review's own sensitivity note says the ordering rests on McLaren and Brooks, and a "strong" rating is firmer than the access and source base (one re-analysed 454 dataset) allow.
  Say instead: The ordering in which DNA extraction is the largest source of relative-abundance error, followed by PCR and then sequencing, rests on one 7-taxon vaginal dataset (Brooks 2015, reanalysed by McLaren 2019), with Albertsen 2015 (sludge, bead beating only) as partial support; it is contested by Fouhy 2016 (two extraction methods gave very similar data) and qualified by MBQC (specimen type mattered more than extraction), and is a single-dataset result, not a field-wide ordering. (Albertsen et al. 2015; Vaginal et al. 2015; Fouhy et al. 2016; McLaren et al. 2019; The et al. 2017)
  Holds for: one 7-taxon vaginal dataset, 454.
  Evidence: a single source; rated "Strong" by the research; a second reader disputes this: firmer than the access and source base allow.
- Do not write: "Calibration cut mean Bray-Curtis error from 0.35 to 0.08 in a shotgun dataset."
  Why: That calibration result comes from the Brooks et al. 2015 16S cell mixtures; the shotgun calibration is reported only qualitatively.
  Say instead: Six parameters explained almost all systematic error in the cell mixtures, and calibration cut mean Bray-Curtis error from 0.35 to 0.08 (92.6% lower mean squared error); this result comes from the Brooks et al. 2015 16S cell mixtures (2 calibration samples, 69 calibrated samples), not from a shotgun dataset. (McLaren et al. 2019)
  Holds for: the Brooks 16S cell mixtures.
  A second reader found the search for contrary evidence one-sided.
- Do not write: "The original 515F/806R V4 primers under-represented SAR11 about 4 to 10-fold in field samples, against about 2-fold in mocks."
  Why: The abstract gives these SAR11 figures for 515F-Y/806R, not for the original 515F-C/806R pair.
  Say instead: In marine samples, the review attributes under-representation of SAR11 and over-representation of Gammaproteobacteria to the original 515F/806R V4 primers, but the abstract gives the SAR11 bias (about 4 to 10-fold in field samples against about 2-fold in mocks) for the 515F-Y/806R pair, so mock-measured bias understated field bias for this taxon. (Parada et al. 2016)
  Holds for: marine field samples and mocks; one primer pair (515F-Y/806R) and one taxon (SAR11).
  Evidence: measured; replicated.
- Do not write: "Bias measured on mock communities does not transfer to field samples."
  Why: This rests on one abstract-only study (Parada 2016), for one primer pair (515F-Y/806R) and one taxon (SAR11).
  Say instead: In marine samples, the review attributes under-representation of SAR11 and over-representation of Gammaproteobacteria to the original 515F/806R V4 primers, but the abstract gives the SAR11 bias (about 4 to 10-fold in field samples against about 2-fold in mocks) for the 515F-Y/806R pair, so mock-measured bias understated field bias for this taxon. (Parada et al. 2016)
  Holds for: marine field samples and mocks; one primer pair (515F-Y/806R) and one taxon (SAR11).
  Evidence: measured; replicated.
  Say instead: Whether mock-derived bias applies to field samples is disputed: Parada 2016 against the calibration claims of McLaren 2019 and Silverman 2021. (McLaren et al. 2019; Parada et al. 2016; Silverman et al. 2021)
  Holds for: field samples against calibration claims.
- Do not write: "ddPCR and flow cytometry correlated at only r = 0.50 on faeces."
  Why: The full text reports qPCR against flow-cytometry enumeration on faeces (Pearson r = -0.50), and ddPCR correlated strongly with qPCR.
  Say instead: qPCR and flow cytometry agreed on a whole-cell mock (|r| = 0.967) but gave "highly divergent" profiles for faeces, where qPCR and flow-cytometry enumeration correlated at Pearson r = -0.50; ddPCR correlated strongly with qPCR, and the authors used this to rule out qPCR imprecision as the cause of the divergence. (Galazzo et al. 2020)
  Holds for: a whole-cell mock and faeces.
  Evidence: measured; a single source.
- Do not write: "Unfiltered OTU tables were 50 to 80% spurious taxa."
  Why: The source says the 50 to 80% figure applies after OTU clustering and singleton removal, not to unfiltered tables.
  Say instead: After OTU clustering and singleton removal, tables were about 50% (mock communities) to 80% (gnotobiotic mice) spurious taxa; the authors propose a 0.25% relative-abundance cutoff. (Reitmeier et al. 2021)
  Holds for: mock communities and gnotobiotic mice.
  Evidence: measured; a single source.
- Do not write: "PCR replicates of negative controls had a mean Jaccard of 0.80."
  Why: The source reports a mean Jaccard distance of 0.80 (range 0.65 to 0.87); without the word "distance" the figure reads as high similarity.
  Say instead: PCR replicates split before PCR differed strongly while replicates split after PCR were nearly identical; in negative extraction controls, most species appeared in only one of five PCR replicates (mean Jaccard distance 0.80, range 0.65 to 0.87). (Dyrhovden et al. 2021)
  Holds for: negative extraction controls; low load.
  Evidence: measured; a single source.
- Do not write: "Several soil studies show that multinomial or Poisson sampling explains much of the replicate disagreement in taxa detected."
  Why: The studies are one 454 dataset of 24 Oklahoma soils (reported and then modelled) and one laboratory, whose Wen 2017 study does not fit the model, so it is weak and contested that sampling alone explains replicate disagreement.
  Say instead: That Poisson or multinomial sampling explains replicate disagreement in taxa detected rests on one 454 dataset of 24 Oklahoma soils (reported by Zhou 2011 and modelled by Zhou 2013) and one laboratory, whose Wen 2017 study does not fit the model; it is weak and contested that sampling alone explains replicate disagreement in taxa detected. (Wen et al. 2017; Zhou et al. 2013; Zhou et al. 2011)
  Holds for: soil, one dataset and one laboratory.
  Evidence: contested; rated "Moderate" by the research; a second reader disputes this: weak and contested that sampling alone explains replicate disagreement.
- Do not write: "Agreement in relative abundance between technical replicates rises with depth, roughly as a square root."
  Why: This rests on one caecal extract with four technical replicates (Barlow 2020), a single source.
  Say instead: For one caecal extract with four technical replicates, the abundance at which the CV of relative abundance reached 30% fell with the square root of read depth, as Poisson noise would predict. (Barlow et al. 2020)
  Holds for: one caecal extract, four technical replicates.
  Evidence: measured; a single source.
- Do not write: "Relative abundance is robust to the pipeline; counts of taxa are not."
  Why: It generalises from Nearing 2018 (with Marizzoni 2020); Nearing 2018 itself reports that all pipelines "markedly differed" from expected composition on the Zymo mock, and Straub 2020 reports pipeline-dependent interpretations.
  Say instead: In an independent benchmark, relative abundances of expected taxa within each mock were similar across DADA2, UNOISE3, Deblur and open-reference OTUs, yet on the Zymo mock all pipelines "markedly differed" from expected composition. (Nearing et al. 2018)
  Holds for: mocks, one independent benchmark.
  Evidence: measured; replicated.
  Say instead: mothur and QIIME1 returned 10 to 200 times the expected number of sequences, and Faith's PD was overestimated 1.3 to 2.7-fold by QIIME2, 2 to 18-fold by QIIME1 and 3.5 to 29-fold by mothur; the study reports pipeline-dependent interpretations. (Straub et al. 2020)
  Holds for: Straub et al.'s benchmark; the authors also built nf-core/ampliseq.
  Evidence: measured; replicated.
- Do not write: "Library preparation and primers are the largest drivers of the error profile."
  Why: This rests on Schirmer 2015 alone, and the review's table gives it no single-source flag.
  Say instead: Across 73 MiSeq datasets, library preparation method and primer choice were the most significant sources of bias, with distinct, motif-linked error patterns; this rests on one study. (Schirmer et al. 2015)
  Holds for: 73 MiSeq datasets.
  Evidence: measured; a single source.
- Do not write: "V4 genus accuracy is about 50% at 97% identity, and reference databases carry about 10 to 17% annotation error."
  Why: Both figures rest on Edgar 2018b and 2018c, from one author who also develops competing classifiers; the review flags them as single in its text but uses them in its answer without that qualifier.
  Say instead: Cross-validated by identity to the reference, all tested classifiers were at most 50% accurate on V4; genus accuracy was about 100% at 100% identity and about 50% at 97%, derived from reference sets by one author who also develops competing classifiers. (Edgar 2018)
  Holds for: V4, reference sets; accuracy depends on distance to reference.
  Evidence: measured; a single source.
  Say instead: Estimated annotation error in reference databases is about 10% for RDP and about 17% for SILVA v128 and Greengenes 13.5, judged from conflicting labels on identical sequences; this rests on one author who also develops competing classifiers. (Edgar 2018)
  Holds for: RDP, SILVA v128, Greengenes 13.5.
  Evidence: derived; a single source.
- Do not write: "Chimera formation is reproducible across amplifications."
  Why: This rests on Haas 2011 alone, with Sanger and 454 data.
  Say instead: Chimeras formed reproducibly across independent amplifications of a known mixture; that chimera formation is reproducible rests on this one study, on Sanger and 454 data. (Haas et al. 2011)
  Holds for: a known mixture, Sanger and 454.
  Evidence: measured; a single source.
- Do not write: "Fast-responding soil isolates averaged 5.5 16S copies against 1.4 for slow responders."
  Why: Stated as a general finding, it rests on one abstract-only study (Klappenbach 2000).
  Say instead: Copy number tracks ecological strategy: soil isolates that formed colonies quickly averaged 5.5 copies and slow responders 1.4; this rests on one abstract-only study. (Klappenbach et al. 2000)
  Holds for: soil isolates; a measured association.
  Evidence: measured; a single source.
- Do not write: "The case against rarefying for richness is only an assertion, against modelled simulations in favour of rarefying."
  Why: Willis 2019 presents statistical argument plus a worked simulated example; classing it as an assertion against Schloss's modelled simulations understates the evidence against rarefying for richness and applies the evidence class unevenly.
  Say instead: Willis argues that plug-in and rarefied richness are both negatively biased, and that rarefying can create false differences between environments with equal richness but different abundance structures; she recommends estimators with variance estimates compared through measurement-error models, and presents statistical argument plus a worked simulated example. (Willis 2019)
  Holds for: one paper.
  Evidence: contested.
  A second reader found the search for contrary evidence one-sided.
- Do not write: "Spike-in totals agreed poorly with flow cytometry (r2 = 0.19), so the internal standards failed."
  Why: The review reports only the r2 before correction and omits the authors' conclusion that the internal-standard method is quantitative and consistent with flow cytometry; the r2 figure could not be verified.
  Say instead: Seawater internal standards agreed with flow cytometry at r2 = 0.19 until corrections for copy number and particle association (with four outliers removed) raised it to 0.61, and the authors conclude that the internal-standard method is quantitative and consistent with flow cytometry; the r2 figures need the body and could not be verified. (Lin et al. 2019)
  Holds for: seawater.
  Evidence: measured; a single source; limited by access (a source was not read in full; not the same as weak evidence).
  A second reader found the search for contrary evidence one-sided.
- Do not write: "In 24 grassland soils, the best-fitting abundance distributions were exponential or inverse gamma."
  Why: The best fits are in Zhou 2013's supplementary Table S3; the main text does not state which distributions won, and they were not verified.
  Say instead: For 24 grassland soils, the best-fitting abundance distributions the review reports (exponential or inverse gamma) are in supplementary Table S3; the main text does not state which distributions won, and they were not verified. (Zhou et al. 2013)
  Holds for: 24 grassland soils.
  Evidence: modelled; a single source; limited by access (a source was not read in full; not the same as weak evidence).
- Do not write: "Water and host-associated communities fit a lognormal abundance distribution better."
  Why: The "water and hosts" item is a single study (Kembel 2012) that pools ocean and skin into one item, and the same paper's simulations assumed a lognormal, so the separate water and host cases were not answered.
  Say instead: After copy-number correction, rank-abundance distributions from ocean and human skin fit a lognormal better, in a single study that pools ocean and skin into one item and whose own simulations assumed a lognormal. (Kembel et al. 2012)
  Holds for: ocean and human skin, pooled.
  Evidence: a single source.
- Do not write: "Water communities carry about 2.2 16S copies per genome."
  Why: The EMP's value of about 2.2 pools free-living (soil, water and sediment) and plant-associated samples, so it is not a value for water.
  Say instead: No separate copy-number value for water was found; the EMP gives a predicted value of about 2.2 for free-living (soil, water, sediment) and plant-associated samples pooled together. (Thompson et al. 2017)
  Holds for: EMP, free-living and plant-associated samples pooled.
  Evidence: a single source.
- Do not write: "Index misassignment moves 0.1 to 6% of 16S reads between samples."
  Why: The range merges non-16S genome and exome libraries, Illumina's own documentation, non-16S amplicons and 16S data, without indirect labels.
  Say instead: On patterned flow cells (HiSeq X, 3000/4000, NovaSeq) with non-16S libraries, 0.2 to 6% of reads were misassigned in every run, about 10-fold less on MiSeq, and unique dual indexes cut 0.89% to 0.13%. (Costello et al. 2018)
  Holds for: non-16S libraries, indirect.
  Evidence: measured; replicated.
  Say instead: In 16S data from GAIIx and 11 MiSeq runs, about 2% of reads were misassigned. (Edgar 2016)
  Holds for: 16S; one preprint abstract.
  Evidence: measured; a single source.
  Say instead: The 16S-specific evidence on index misassignment is thin: one preprint abstract and one plate study; no 16S-specific measurement of index hopping on patterned flow cells (NovaSeq, NextSeq 2000) was found. (Edgar 2016; Minich et al. 2019)
  Holds for: the bioinformatics angle's search.
  Evidence: search (note: "No 16S-specific measurement of index hopping on patterned flow cells (NovaSeq) was found").
  Searched, not found (note: "no 16s-specific measurement of index hopping on patterned flow cells (novaseq) was found").
- Do not write: "Extraction bias is consistent across samples on the ratio scale, in cell mixtures and in a shotgun spike-in alike."
  Why: A 16S cell-mixture result and a shotgun spike-in result known only secondarily are combined into one finding, mixing measurement types.
  Say instead: Modelling each step as multiplying taxon abundances by a taxon-specific efficiency, McLaren et al. found that the error in taxon ratios was "consistent across samples", while the error in proportions "varied dramatically in both magnitude and direction", in the one dataset modelled for this question (the vaginal cell mixtures; extraction bias was consistent on the ratio scale within a protocol); an abstract-level source cited in the second review describes bias in sequencing measurements as a consistent multiplicative factor per taxon that calibration controls can correct, while field evidence of inconsistency (Parada, abstract only, one primer pair) is weighed as limiting. (McLaren et al. 2019)
  Holds for: 7 taxa mixed as cells and reanalysed.
  Evidence: modelled; a single source.
  A second reader found the search for contrary evidence one-sided.
  Say instead: A 10-species shotgun spike-in across faecal backgrounds also gave a consistent profile on the ratio scale, with protocol H showing up to 2,751-fold maximum pairwise bias; this is known only via McLaren 2019, and its calibration is reported only qualitatively ("removed most of the systematic error"). (Costea et al. 2017)
  Holds for: shotgun, faecal backgrounds; secondary and indirect.
  Evidence: limited by access (a source was not read in full; not the same as weak evidence).
- Do not write: "Whether the departure is consistent across samples determines whether a fixed correction can work."
  Why: That is the reviewer's framing of what matters for analysis design, not a literature finding.
- Do not write: "The difference in load is the likely reason pooled and single PCR results disagree."
  Why: This is the reviewer's own reconciliation, presented in the answer; no single study tested both conditions, and it is not marked as the reviewer's reading.
  Say instead: Pooling PCR replicates had no detectable effect, and pooled versus single PCR made no difference at moderate to high input, but replicates split before PCR disagreed strongly at low load. (Dyrhovden et al. 2021; Kennedy et al. 2014; Marotz et al. 2019; Smith and Peay 2014)
  Holds for: moderate to high input (Kennedy 2014, Marotz 2019, Smith and Peay 2014) against low load (Dyrhovden 2021); no single study tested both conditions.
- Do not write: "Simulations disagree mainly because they build different data-generating processes into the truth."
  Why: This is only partly supported (Weiss 2017, Hong 2022 and Schloss 2024a each say results depend on data-generating assumptions) and is phrased as the review's own causal diagnosis.
  Say instead: Simulation results on rarefying and its alternatives flip with design choices, as Weiss 2017 and Schloss 2024a both say. (Hong et al. 2022; Schloss 2024; Weiss et al. 2017)
  Holds for: simulation benchmarks.
- Do not write: "The review's summary table shows which approaches are shown to correct for unequal depth or load."
  Why: Its "Shown to correct" cells mix makers' claims and simulation results with measured results without a per-cell evidence class, so it reads closer to a method recommendation than the brief allows.
  Say instead: In the review's summary, rarefying or rarefaction removes depth dependence of alpha and beta diversity under the null and controls false positives under confounding, but loses data and power, adds variance when done once, gave high differential-abundance false-positive rates in one benchmark, is argued to bias richness, and does not touch bias or load; it applies to all three measures and is contested. The summary table mixes makers' claims and simulation results with measured results without a per-cell evidence class. (Hong et al. 2022; McMurdie and Holmes 2014; Schloss 2024; Weiss et al. 2017; Willis 2019)
  Holds for: the review's summary by approach.
  Say instead: In the review's summary, scaling methods (TMM, RLE, CSS, VST, SRS, Wrench) show some FDR and power benefits at small n (DESeq2) and come close to quantitative methods in a dysbiosis simulation, but are depth-sensitive for beta and alpha diversity under the null, assume most taxa unchanged, and DESeq2's FDR rises with n and uneven libraries; the summary table mixes evidence classes without a per-cell label. (Llorens-Rico et al. 2021; Schloss 2024; Weiss et al. 2017)
  Holds for: the review's summary by approach; differential abundance and beta diversity.
  Say instead: In the review's summary, compositional (log-ratio) approaches give ratio fold changes invariant to load and to multiplicative bias, and ANCOM and ALDEx2 are conservative, but Aitchison distances are depth-sensitive under the null, ANCOM-BC shows type I inflation in some settings, and results are sensitive to pseudocounts; the summary table mixes evidence classes without a per-cell label. (Kaul et al. 2017; McLaren et al. 2019; Nearing et al. 2022; Schloss 2024; Yang and Chen 2022)
  Holds for: the review's summary by approach; differential abundance and beta diversity.
  Say instead: In the review's summary, proportions are simple, and elementary tests on proportions were replicable and FDR-controlling in some benchmarks, but showed severe type I error with large depth differences, depth-sensitive beta diversity, and proportion error that varies with sample composition. (McLaren et al. 2019; Pelto et al. 2025; Schloss 2024; Wirbel et al. 2024; Yang and Chen 2022)
  Holds for: the review's summary by approach; differential abundance and beta diversity.
  Say instead: In the review's summary, absolute load measurements correct differences in total load and reversals of relative trends, but not taxon-specific bias, extraction-yield variation, or disagreement between qPCR and flow cytometry; they apply to all three measures and are strongest for differential abundance and associations. (the review's summary)
  Holds for: the review's summary by approach.
  Say instead: In the review's summary, coverage-based standardisation compresses richness ratios less than size-based rarefaction (ecology, modelled) but fails on terrestrial inventories and is depth-correlated in a microbial null model. (Alroy 2026; Chao and Jost 2012; Schloss 2024)
  Holds for: the review's summary by approach; alpha diversity.
  Say instead: In the review's summary, richness estimators give lower bounds and extrapolation to about 2 to 3 times sample size (ecology), but are depth-correlated, have unidentifiable tails, are invalid without singletons and are inflated by spurious singletons. (Chao et al. 2014; Deng et al. 2024; Haegeman et al. 2013; Schloss 2024)
  Holds for: the review's summary by approach; alpha diversity.
- Do not write: "UNBIAS's pessimistic result is a single-source contrary result, set against the established good fits of calibration."
  Why: The pro-correction results it conflicts with (McLaren, Silverman) each also rest on a single mock design and get no matching single-source label at that point.
  Say instead: A preprint by the tool's author reports essentially "no meaningful correlation" between 16S read frequencies and species frequencies in mocks. (Edgar 2017)
  Holds for: mocks; preprint abstract.
  Evidence: measured; a single source.
  Say instead: Six parameters explained almost all systematic error in the cell mixtures, and calibration cut mean Bray-Curtis error from 0.35 to 0.08 (92.6% lower mean squared error); this result comes from the Brooks et al. 2015 16S cell mixtures (2 calibration samples, 69 calibrated samples), not from a shotgun dataset. (McLaren et al. 2019)
  Holds for: the Brooks 16S cell mixtures.
  A second reader found the search for contrary evidence one-sided.
  Say instead: PCR-bias calibration corrected composition toward truth in all 10 held-out mocks; the authors note that their mock "ground truth" carried its own bias and that the method sometimes estimated the wrong direction for some taxa. (Silverman et al. 2021)
  Holds for: 10 held-out mocks.
- Do not write: "Bias is consistent across samples on the ratio scale, and field evidence of inconsistency only limits this."
  Why: The ratio-scale result comes from 7 taxa mixed as cells and reanalysed, while field evidence of inconsistency (abstract only, one primer pair) is weighed as limiting; neither side's small-n and access limits are stated symmetrically.
  Say instead: Modelling each step as multiplying taxon abundances by a taxon-specific efficiency, McLaren et al. found that the error in taxon ratios was "consistent across samples", while the error in proportions "varied dramatically in both magnitude and direction", in the one dataset modelled for this question (the vaginal cell mixtures; extraction bias was consistent on the ratio scale within a protocol); an abstract-level source cited in the second review describes bias in sequencing measurements as a consistent multiplicative factor per taxon that calibration controls can correct, while field evidence of inconsistency (Parada, abstract only, one primer pair) is weighed as limiting. (McLaren et al. 2019)
  Holds for: 7 taxa mixed as cells and reanalysed.
  Evidence: modelled; a single source.
  A second reader found the search for contrary evidence one-sided.
  Say instead: Bias varies between sample types or samples: a field-versus-mock SAR11 bias for the 515F-Y/806R pair (abstract only), inconsistent cycle effects in four stool samples, extraction yield of 40 to 84%, and a 66.7-fold spike-in range (abstract). (Parada et al. 2016; Sze and Schloss 2019; Zemb et al. 2020; Zhou et al. 2011)
  Holds for: field and mock samples, stool samples, spike-ins.
  Evidence: measured; the sources differ.
- Do not write: "Sampling explains replicate variation, and the 76% of technical variance beyond counting comes from a different setting and measure."
  Why: The "different setting and measure" caution is applied to Silverman 2018 but not to the sampling side, whose own contrary evidence in Wen 2017 (an overlap plateau, biases other than random sampling, a run effect) is left out.
  Say instead: MiSeq replicates from the same laboratory cut against pure sampling: unweighted overlap plateaued at 39% near 30,000 reads (with singletons) and reached only 43.9% at 160,000 reads, far below the predicted 90% at about 60,900; the authors attribute rare-OTU variation to random sampling plus sequencing artefacts, report that "biases other than random sampling" affect unweighted metrics more, and found lower overlap when replicates were sequenced in separate runs. (Wen et al. 2017)
  Holds for: MiSeq replicates from the same laboratory.
  Say instead: The conflict between sampling as the cause of replicate variation and technical variance beyond counting is partly one of setting and measure (OTU overlap against variance of relative abundance), a caution applied to the technical-variance side but not to the sampling side. (Dyrhovden et al. 2021; Grilli 2020; Silverman et al. 2018; Zhou et al. 2013)
  Holds for: OTU overlap against variance of relative abundance.
  A second reader found the search for contrary evidence one-sided.
  Say instead: In four artificial-gut vessels sampled hourly with 20 technical replicates per vessel, 76% of observed variation was attributed to technical sources beyond sequence counting; this rests on one study. (Silverman et al. 2018)
  Holds for: four artificial-gut vessels, hourly sampling.
  Evidence: modelled; a single source.
- Do not write: "Total 16S qPCR multiplied by relative abundance agrees near-perfectly with taxon-specific qPCR, which validates absolute quantification."
  Why: The near-perfect correlation is a comparison of methods that share an upstream (qPCR against qPCR-anchored sequencing), so it is not independent agreement.
  Say instead: Total 16S qPCR multiplied by relative abundance correlated near-perfectly with taxon-specific qPCR, a comparison of methods that share an upstream (qPCR against qPCR-anchored sequencing) for four taxa. (Jian et al. 2020)
  Holds for: four taxa.
  Evidence: measured; a single source.
- Do not write: "The figures from Zhou 2011, Kozich 2013, Haegeman 2013 and Lin 2019 were read in full text."
  Why: Their full-text labels could not be confirmed as open full text by Europe PMC or PMC; the quoted figures for Zhou 2011 match its abstract and should be labelled abstract-derived, and figures needing the body could not be confirmed.
- Do not write: "Archaea carry 1 to 4 copies of the 16S rRNA gene."
  Why: Stated as the whole record, it misses Acinas et al. 2004, which already reports a maximum of five archaeal operons; the review's own sources conflict on the archaeal maximum.
  Say instead: Archaea carry 1 to 4 copies in rrnDB releases up to v5.0 (the 2015 release: 175 archaeal records, 148 species) and 1 to 5 from v5.6, but Acinas et al. 2004 already reported a maximum of five archaeal operons, so the sources conflict on the archaeal maximum. (Acinas et al. 2004; Schmidt Laboratory 2025; Stoddard et al. 2015)
  Holds for: archaeal genomes, few (148 species in 2015); archaeal maxima of 5 in v5.6 onward include Natronorubrum, Natrinema, Methanococcoides and Methanolobus.
  Evidence: derived; contested.
- Do not write: "Acidobacteria average 1.0 16S copies per genome."
  Why: Presented beside large-n phyla without its n, the mean rests on 4 genomes from 4 species, and the soil correction example depends on it.
  Say instead: Mean copy numbers by group in the 1,690 genomes were Acidobacteria 1.0, Alphaproteobacteria 2.2, Deltaproteobacteria 2.7, Actinobacteria 3.1, Betaproteobacteria 3.3, Bacteroidetes 3.5, Firmicutes 5.8 and Gammaproteobacteria 5.8; the Acidobacteria mean rests on 4 genomes from 4 species. (Vetrovsky and Baldrian 2013)
  Holds for: sequenced genomes.
  Say instead: Phyla common in soil but poorly represented among genomes (Acidobacteriota, Verrucomicrobiota, Chloroflexota) sit at the low end of copy number on small numbers of species, so these soil-relevant low values are imprecise, and the soil correction example (Acidobacteria 50.1% to 66.0%) depends on them. (Schmidt Laboratory 2025; Vetrovsky and Baldrian 2013)
  Holds for: sequenced genomes of soil-relevant phyla (Acidobacteria 1.0 from 4 genomes; rrnDB v5.10 Acidobacteriota 1.4 from 29 species).
- Do not write: "The 1 to 15 range of 16S copies per genome is replicated across independent sources."
  Why: The range is consistent across sources, but those sources draw on overlapping NCBI genome sets, so they are not independent replications.
  Say instead: Bacterial genomes carry 1 to 15 copies of the 16S rRNA gene in every database release and genome survey up to about 2015; the range is consistent across sources, but those sources draw on overlapping NCBI genome sets, so they are not independent replications. (Acinas et al. 2004; Klappenbach et al. 2001; Lee et al. 2009; Stoddard et al. 2015; Vetrovsky and Baldrian 2013)
  Holds for: rrnDB releases (the first: "one to as many as 15 copies"; 2009: 785 bacterial and 69 archaeal strains; 2015: 2,635 bacterial records, 1,383 species), Acinas et al. 2004 and Vetrovsky and Baldrian's 1,690 genomes; sequenced genomes.
  Evidence: derived; the sources differ; rated "Strong for the range and the taxon dependence" by the research; a second reader disputes this: consistent across sources, but not independent replications.
- Do not write: "Bacterial genomes carry up to 21 or 22 copies of the 16S rRNA gene."
  Why: The current maxima are the reviewer's own derivation from rrnDB, with no published check against assembly quality, and the answer leads with them over published values.
  Say instead: The long-quoted ceiling of 15 is no longer the database maximum: rrnDB v5.6 contains a Photobacterium damselae genome with 21 copies and v5.10 a Mesobacillus maritimus genome with 22, and several Photobacterium and Bacillaceae genomes have 20 to 21; these maxima are the reviewer's own derivation from the release files, and no source checked them against assembly quality. (Schmidt Laboratory 2025)
  Holds for: rrnDB release files v3.1.227 to v5.10, summarised by the reviewer.
  Evidence: derived.
- Do not write: "Genome copies per cell usually fall in stationary phase or starvation."
  Why: Phrased as a property of prokaryotes, it rests largely on one laboratory's abstracts and folds taxon-specific and sometimes opposite behaviours into one trend; A. vinelandii and M. acetivorans carry more chromosomes in stationary than in exponential phase.
  Say instead: Genome copy number does not change in one direction with growth phase: most Soppa-group species fall in stationary phase or starvation, but A. vinelandii is reported to rise (secondary, via the Bruck et al. 2023 full text). (Bruck et al. 2023; Pecoraro et al. 2011)
  Holds for: taxon-specific and sometimes opposite behaviours.
  A second reader found the search for contrary evidence one-sided.
  Say instead: Azotobacter vinelandii is reported to rise from about 4 genome copies in exponential phase to about 80 in stationary phase, and Methanosarcina acetivorans from 2.5 to 5; Pecoraro 2011 Table 5 gives A. vinelandii as 1 (up to 8) copies in slow growth and 40 in fast growth, attributed to another laboratory. (Bruck et al. 2023; Pecoraro et al. 2011)
  Holds for: the A. vinelandii stationary-phase figure is secondary, via the Bruck et al. 2023 full text read by the critic.
- Do not write: "Evidence on genome copies per cell is strong for cultures."
  Why: Apart from Pecoraro 2011 all ploidy studies were read at abstract level, and the evidence rests largely on one laboratory's qPCR method, so it is moderate, not strong.
  Say instead: In cultures, genome copies per cell range from about one (Caulobacter, Wolinella, crenarchaea) through merodiploid and oligoploid states that depend on growth rate (E. coli, Bacillus, Synechococcus) to tens or hundreds (P. putida, haloarchaea, methanogens, Synechocystis), and depend on taxon, growth rate and growth phase; this general conclusion would survive any single removal. (Bottinger et al. 2018; Breuert et al. 2006; Griese et al. 2011; Hildenbrand et al. 2011; Pecoraro et al. 2011; Zerulla et al. 2016)
  Holds for: cultures.
  Evidence: measured; rated "Strong for cultures" by the research; a second reader disputes this: moderate, not strong; apart from Pecoraro 2011 it rests largely on abstracts and one laboratory's qPCR method.
  Say instead: Most culture ploidy values come from one laboratory's real-time PCR protocol (Soppa group), in several studies cross-checked against Southern blots, flow cytometry or published E. coli values; measurements from other laboratories exist for Azotobacter, Desulfovibrio (9 to 17), Neisseria (3 to 4) and Buchnera (120), with polyploid Deinococcus, Borrelia and rhizobial bacteroids also mentioned, all listed in Pecoraro 2011. (Bottinger et al. 2018; Breuert et al. 2006; Bruck et al. 2023; Griese et al. 2011; Hildenbrand et al. 2011; Pecoraro et al. 2011; Zerulla et al. 2016; Zerulla and Soppa 2014)
  Holds for: cultures.
  A second reader found the search for contrary evidence one-sided.
- Do not write: "No direct contradiction of the culture ploidy values was found, and no independent-laboratory measurements were located."
  Why: Pecoraro 2011, read in full, lists in its Table 5 A. vinelandii polyploidy (40 copies in fast growth) and several measurements from other laboratories, and Bruck 2023 reports A. vinelandii rising from 4 to 80 copies.
  Say instead: Most culture ploidy values come from one laboratory's real-time PCR protocol (Soppa group), in several studies cross-checked against Southern blots, flow cytometry or published E. coli values; measurements from other laboratories exist for Azotobacter, Desulfovibrio (9 to 17), Neisseria (3 to 4) and Buchnera (120), with polyploid Deinococcus, Borrelia and rhizobial bacteroids also mentioned, all listed in Pecoraro 2011. (Bottinger et al. 2018; Breuert et al. 2006; Bruck et al. 2023; Griese et al. 2011; Hildenbrand et al. 2011; Pecoraro et al. 2011; Zerulla et al. 2016; Zerulla and Soppa 2014)
  Holds for: cultures.
  A second reader found the search for contrary evidence one-sided.
  Say instead: Azotobacter vinelandii is reported to rise from about 4 genome copies in exponential phase to about 80 in stationary phase, and Methanosarcina acetivorans from 2.5 to 5; Pecoraro 2011 Table 5 gives A. vinelandii as 1 (up to 8) copies in slow growth and 40 in fast growth, attributed to another laboratory. (Bruck et al. 2023; Pecoraro et al. 2011)
  Holds for: the A. vinelandii stationary-phase figure is secondary, via the Bruck et al. 2023 full text read by the critic.
- Do not write: "16S copies per cell scale with origin number more than with genome number."
  Why: It is the reviewer's inference from one abstract (Couturier and Rocha 2006), presented without a reviewer's-reading label; no source in the review measures 16S copies per cell against origin number.
  Say instead: That 16S copies per cell scale with origin number more than with genome number is the reviewer's inference from one abstract; no source in the review measures 16S copies per cell against origin number. (Couturier and Rocha 2006)
  Holds for: fast growers.
  Evidence: the reviewer's reading.
- Do not write: "For no natural community has the share of cells with one genome copy versus more than one been reported by taxon."
  Why: In situ flow-cytometric cell-cycle analyses of Prochlorococcus are by method taxon-specific measurements of the share of cells with replicated DNA; the review read only the abstract, so the statement is not established.
  Say instead: Not measured in the sources found: genome copies per cell for named soil bacterial or archaeal taxa in situ; the share of single-copy cells by taxon in soil, rhizosphere or dormant natural populations; any direct measurement of 16S copies per cell in environmental cells; ploidy of cultured soil Acidobacteriota, Verrucomicrobiota or Nitrososphaerota. (Vaulot et al. 1995)
  Holds for: soil, rhizosphere and dormant natural populations; for Prochlorococcus, in situ flow cytometric cell-cycle analyses measure by method the taxon-specific share of cells with replicated DNA, and the review read only the abstract.
  Evidence: a search result.
  Searched for and not found.
- Do not write: "The share of Prochlorococcus cells carrying two genomes changes over the day."
  Why: The abstract gives no share; it states only that replication occurred in the afternoon and division at night, so the claim goes beyond the access.
  Say instead: In the equatorial Pacific, Prochlorococcus DNA replication ran in phase with the light cycle, in the afternoon, with division at night; the abstract gives no share of cells carrying two genomes. (Vaulot et al. 1995)
  Holds for: Prochlorococcus in the equatorial Pacific; abstract only.
  Evidence: limited by access (a source was not read in full; not the same as weak evidence).
- Do not write: "Eleven DNA-based mock communities fitted 7.1% better without copy-number correction."
  Why: The 7.1% was computed on n = 10 mocks; one of the eleven was excluded.
  Say instead: On 10 V4 mock communities (one of eleven excluded; nine genomic DNA mixes and two cloned-gene mixes), uncorrected data fit known composition 7.1% (SE 3.6%) better than copy-number-corrected data; all were DNA-based or cloned-gene mocks. (Starke et al. 2021)
  Holds for: DNA-based and cloned-gene mocks.
  Evidence: measured; replicated.
- Do not write: "Other biases, such as extraction and primers, are of similar or larger size than copy-number bias and multiply with it."
  Why: This rests on McLaren et al. 2019 read at abstract level, and the abstract does not compare their magnitude with copy-number bias.
- Do not write: "Abundant taxa are those above 1% of reads, as in Jia et al. 2022."
  Why: Jia et al. 2022 uses a single rare/common cutoff and does not support "abundant above 1%".
  Say instead: Within a sample, rare is most often defined as below 0.1% of reads, sometimes below 0.01% or 0.001%, and abundant usually as above 1%; one of the sources cited for these thresholds uses a single rare/common cutoff and does not support "abundant above 1%". (Dai et al. 2016; Galand et al. 2009; Jia et al. 2022; Lynch and Neufeld 2015)
  Holds for: within-sample relative abundance.
- Do not write: "Only about 1% of taxa were agreed as core by all four methods."
  Why: The source gives 165 and 176 taxa as 13% and 15.85% of core assignments; "about 1% of taxa" is the review's own derivation and should be labelled as such.
  Say instead: Four core methods compared on human faecal (319 samples) and Arabidopsis root (288 samples) data assigned 1.2% to 9.4% of taxa as core, nearly 10-fold apart; 165 to 176 taxa were agreed by all four, which is 13 to 16% of core assignments. (Custer et al. 2023)
  Holds for: human faecal and Arabidopsis root data.
- Do not write: "In bulk soil, 0.4 to 2% of taxa hold about 41 to 58% of reads."
  Why: The figures come from two datasets with different definitions and denominators (2% holding on average 41% of reads per sample under a joint abundance-and-ubiquity definition; 0.4% holding about 58% of pooled global relative abundance), and the body says they must not be combined.
  Say instead: Across 237 soils, per-sample richness ranged from 774 to 2,869 phylotypes, and 511 of 25,224 phylotypes (2%), defined as dominant jointly by abundance (top 10% by share of reads) and ubiquity (present in more than half of the soils), accounted on average for 41% of 16S reads per sample, more than half in arid forests and only about 20% in tropical forests. (Delgado-Baquerizo et al. 2018)
  Holds for: 237 soils, bulk soil, amplicon reads; per-sample mean.
  Say instead: Across 844 soils (318 sites, 90-bp V4 ASVs), 0.4% of ASVs were classed common on the globally pooled rank-abundance distribution and held about 58% of pooled relative abundance, while the 99.6% classed rare held 42%. (Bickel and Or 2021)
  Holds for: 844 soils, pooled global relative abundance.
  Say instead: The dominant-fraction shares of the two global soil datasets (2% holding about 41% of reads per sample, and 0.4% holding about 58% of pooled relative abundance) use different definitions and denominators and must not be combined. (Bickel and Or 2021; Delgado-Baquerizo et al. 2018)
  Holds for: two global soil amplicon datasets.
- Do not write: "Two phylotypes dominate soil archaea."
  Why: Stated as a general finding, it rests on one abstract-only study (Bates et al. 2011) of 2010-era 454 data from 146 soils.
  Say instead: Across 146 soils, archaeal reads averaged 2% of 16S reads (0 to over 10%), and two Thaumarchaeota (then Crenarchaeota) phylotypes made up over 70% of archaeal sequences; this rests on one abstract-only study of 2010-era 454 data. (Bates et al. 2011)
  Holds for: 146 soils, 454.
  Evidence: a single source.
- Do not write: "Bulk soil shows a positive abundance-occupancy relationship wherever it has been tested."
  Why: "Wherever tested" rests on two partly overlapping datasets whose metrics are partly circular, after a search that reviewed about 25 titles, so it overstates the evidence.
  Say instead: In the two bulk-soil amplicon studies with figures, more abundant taxa occupy more soils, but the two are not fully independent (one reanalysed compiled datasets including the Earth Microbiome Project, which plausibly overlaps the other's soils), both measures are partly built in by construction, detection limits (a single 454-era study at one site) and neutral or sampling models predict a positive relationship without selection, and no soil test against a sampling null was found; whether a relationship exists beyond sampling, and how strong it is, is unresolved. (Bickel and Or 2021; Nemergut et al. 2011)
  Holds for: bulk soil, amplicon data; the sampling-null evidence is non-soil.
  Evidence: unclear; rated "Moderate for the existence of a positive relationship in amplicon data from bulk soil" by the research; a second reader disputes this: unresolved beyond sampling.
  A second reader found the search for contrary evidence one-sided.
- Do not write: "Low-abundance taxa are routinely recorded absent where present, which by itself produces lower occupancy for rarer taxa."
  Why: Presented as a finding of Zhou et al. 2011, it generalises from one 454 study of 24 communities at one Oklahoma site, and the occupancy conclusion is the reviewer's argument, which Zhou's abstract does not draw.
  Say instead: In the reviewer's argument, low-abundance taxa are often recorded absent when present, which by itself would produce lower occupancy for rarer taxa; the one source behind it (454 pyrosequencing, 24 communities from one Oklahoma warming site) attributes low replicate overlap to random sampling but does not draw the occupancy conclusion. (Zhou et al. 2011)
  Holds for: one 454-era study at one site.
  Evidence: the reviewer's reading.
- Do not write: "Occupancy-based core methods perform best, an established standard for defining the core."
  Why: This rests on one simulation study (Custer et al. 2023) and is listed among proposed standards as if established.
  Say instead: Occupancy-based core methods were most accurate in simulations, in one simulation study. (Custer et al. 2023)
  Holds for: simulations.
  Evidence: a single source.
- Do not write: "Up to 41% of rRNA genes in soil are unlinked."
  Why: The soil figure rests on one abstract-only study (Brewer 2020); the body flags this, the answer does not.
  Say instead: 16S gene count and operon count diverge where rRNA genes are unlinked: unlinked 16S and 23S genes are common in Deinococcus-Thermus, Chloroflexi and Planctomycetes, and up to 41% of rRNA genes in soil long-read metagenomes were unlinked, against none in human gut. (Brewer et al. 2020)
  Holds for: soil and human-gut long-read metagenomes; the soil figure from one source.
  Evidence: a single source.
- Do not write: "Common taxa occur in far more soils than rare taxa, a further abundance-occupancy relationship."
  Why: The common class is defined on the globally pooled rank-abundance distribution, pooled abundance rises mechanically with prevalence, and a class-level contrast of median prevalence is a different measure from a taxon-level relationship.
  Say instead: Across 844 global soils, median prevalence was 0.3 for common taxa and 0.001 for rare taxa; this is a class-level contrast in which the common class is defined on the globally pooled rank-abundance distribution, and pooled abundance rises mechanically with prevalence, so it is a different measure from a taxon-level abundance-occupancy relationship. (Bickel and Or 2021)
  Holds for: 844 global soils.

## Gaps

What the research did not establish.

- Same-sample comparisons of 16S amplicon data with shotgun metagenomes and with culture-based, microscopy or FISH, or taxon-specific qPCR counts (beyond four taxa in one study) are missing; the only shotgun evidence is Costea 2017, known secondarily via McLaren.
  The research does not say whether this was searched for.
- Field sampling choices for water (volume filtered, filter pore size, prefiltration, filter storage) and for host tissue (swab, biopsy or lavage; plant tissue surface sterilisation); the review contradicts itself on whether these were searched: its section 2.1 says the lab angle searched preservation and storage terms through Crossref, Europe PMC and web search, while its Search record says no angle searched water-sampling or host-tissue sampling choices.
  Not searched for.
- Long-read platform error and bias on mocks: Nanopore full-length 16S is absent, PacBio full-length evidence is only the developer's own claim, and there are no independent long-read mock benchmarks.
  The research does not say whether this was searched for.
- 16S-specific index hopping on Illumina patterned flow cells (NovaSeq, NextSeq 2000): the only 16S rate is one preprint abstract.
  Searched, not found (note: "16s-specific index hopping on patterned flow cells (bioinformatics angle)").
- Read counts per sample within a run after pooling, and the correlation of library size with biomass; two primary studies on this (101 fish species; an equivolumetric protocol) are known only through Schloss 2024b and were not opened.
  Searched for and not found.
- Community-average 16S copy number measured from shotgun metagenomes (16S reads normalised to single-copy marker genes) in soil, water and host samples.
  Not searched for.
- Absolute per-cycle amplification efficiency of universal 16S primers on soil, sediment, water and faecal extracts, from the qPCR methods literature (per-reaction efficiency from amplification curves, inhibition in environmental extracts).
  Not searched for.
- Abundance-distribution shapes by environment: Grilli 2020's per-biome supplementary figures and Shoemaker 2017's full text were not read, so per-environment shapes for water and host samples are absent although the sources exist.
  The research does not say whether this was searched for.
- Dirichlet-multinomial or other overdispersion fits to 16S technical replicates, and technical replicates across depths in aquatic, plant and human non-gut samples; replicate-at-depth studies are confined to one soil laboratory and one mouse caecum.
  Searched, not found (note: "overdispersion fitted to 16s technical replicates at controlled depths (statistics angle)").
- Contaminant-removal tools beyond decontam and SourceTracker (for example tools modelling well-to-well leakage), and independent benchmarks of decontam's prevalence mode, for low-biomass samples.
  The research does not say whether this was searched for.
- Primary-source benchmarks of compositional beta-diversity variants (robust Aitchison, phylogenetic isometric log-ratio) and of scaling methods such as GMPR and ANCOM-BC2; coverage relies on two benchmark papers.
  The research does not say whether this was searched for.
- Benchmarks of any approach to unequal depth or load in soil or water with measured absolute loads as truth, and known-richness mocks tested across depths.
  The research does not say whether this was searched for.
- Archaeal evidence is thin: one archaeal-rich mock, a copy-number range from 148 species, and one run-failure case; archaeal-specific primer bias measured against known composition in archaea-rich environments (marine, sediment, methanogenic reactors) is absent.
  The research does not say whether this was searched for.
- A follow-up for MB-01 was triggered and not yet written: several gaps name a workflow step or bias source with no measured magnitude (per-cycle amplification efficiency, community copy number measured from metagenomes, 16S index hopping on patterned flow cells, within-run read-count variation against load, and long-read platform error).
  The research does not say whether this was searched for.
- Sources MB-01 could not obtain that bear on its questions: a mock-community comparison of one-step against two-step library preparation and cycle number (Gohl 2016, abstract only, no figures), the largest interlaboratory extraction comparison with spike-in (Costea 2017, known only via McLaren 2019), storage effects across soil, faeces and skin (Lauber 2010, known only via Rubin 2013), index switching on HiSeq 4000, and the origins of rarefaction and sample coverage. (Costea et al. 2017; Gohl et al. 2016; Lauber et al. 2010; Sinha et al. 2017)
  The research does not say whether this was searched for.
- MB-01 lists Shoemaker 2017 and Smets 2016 both among its references as read at abstract level ("AB per lab angle") and among its sources not obtained ("only a web-search engine summary seen, not used as a finding"; Crossref with no abstract, Europe PMC not indexed), yet uses both as findings. (Shoemaker et al. 2017; Smets et al. 2016)
  The research does not say whether this was searched for.
- Polyploidy of soil and plant-associated bacteria measured outside the Soppa laboratory: Azotobacter vinelandii (40 to 80 copies, rising in stationary phase), Deinococcus radiodurans, and endoreduplicated Sinorhizobium bacteroids in nodules (Mergaert et al. 2006).
  The research does not say whether this was searched for.
- Direct measurements of the share of cells at one genome copy against several: classic flow-cytometric chromosome run-out work giving per-cell distributions of 1, 2, 4 and 8 chromosomes (for example Skarstad, Boye and Steen 1986), and Caulobacter swarmer-cell G1 shares.
  Not searched for.
- In situ cell-cycle analyses of Prochlorococcus and Synechococcus (Vaulot 1995 and successors), which report the fraction of cells in G1 against S/G2 by taxon in natural seawater, were read only at abstract level.
  The research does not say whether this was searched for.
- Ploidy of dormant forms (endospores, Streptomyces spores, Azotobacter cysts) and of non-growing small soil cells.
  The research does not say whether this was searched for.
- In situ growth measures in soil and rhizosphere: qSIP growth rates and growth-rate potential from genomes (for example Chuckran et al. 2025 on rewetted soil; Lopez et al. 2023 on rhizosphere against bulk soil, which also reports, via a cited study, 6.6% more rRNA operons in rhizosphere bacteria).
  Not searched for.
- Soil studies using community-weighted rrn copy number (for example succession and rhizosphere-versus-bulk comparisons, Nemergut et al. 2016) and soil absolute quantification (Smets et al. 2016) were not searched for copy-number correction or soil abundance.
  Not searched for.
- Occupancy-based classification terms: habitat generalist against specialist (Levins niche breadth, for example Szekely and Langenheder 2014), cosmopolitan against endemic, and the microbial core-satellite partition (for example van der Gast et al. 2011).
  The research does not say whether this was searched for.
- The soil literature contrasting abundant and rare subcommunities' distribution ranges and niche breadth across regions (for example Jiao and Lu 2020; Jiao, Chen and Wei 2017), which bears on abundance against occupancy and on threshold usage in soil.
  Not searched for.
- Taxon abundance distributions and occupancy from global genome-resolved or metagenome-based soil datasets (for example Bahram et al. 2018).
  Not searched for.
- Taxon-specific cell counts in soil (CARD-FISH or FISH phylum or class shares) beyond abundance-distribution queries.
  Not searched for.
- Non-soil nearest precedents for the shape of the abundance distribution that contradict the lognormal view (for example power-law tails of non-dominant plankton, Ser-Giacomi et al. 2018).
  The research does not say whether this was searched for.
- Explicit sampling or occupancy-detection models applied to bulk-soil microbes (site-occupancy models, gamma-Poisson occupancy predictions on soil data), and whether Grilli 2020's datasets include soil.
  Not searched for.
- Technical-replicate detection studies after the 454 era (Illumina, deeper sequencing) in soil, to test whether Zhou 2011's low replicate overlap generalises.
  Not searched for.
- A follow-up for MB-02 was triggered and not written: the critic names unsearched per-cell and growth-state evidence for soil (in situ growth measures, ploidy of dormant and sporulated forms, taxon-specific cell counts by CARD-FISH, soil studies weighting communities by rrn copy number), occupancy-based terms and global soil metagenomes, among 13 coverage gaps; the owner decides.
  The research does not say whether this was searched for.
- The main bulk-soil abundance-occupancy figures (28% against 2%, 69% against 8%) could not be verified by the critic and should be rechecked; the source's abstract frames its analyses across Earth's major habitat types, not soils alone. (Nemergut et al. 2011)
  The research does not say whether this was searched for.
- The sampling-artefact literature on abundance-occupancy (Wright 1991; Holt et al. 2002) and the polyploidy-and-community-structure argument (Soppa 2017) were not obtained. (Holt et al. 2002; Soppa 2017; Wright 1991)
  The research does not say whether this was searched for.

## References

- Abellan-Schneyder, Isabel; Matchado, Monica S.; Reitmeier, Sandra; Sommer, Alina; Sewald, Zeno; Baumbach, Jan; List, Markus; Neuhaus, Klaus (2021). Primer, pipelines, parameters: issues in 16S rRNA gene sequencing. mSphere 6(1): e01202-20. https://doi.org/10.1128/mSphere.01202-20
- Acinas, Silvia G.; Marcelino, Luisa A.; Klepac-Ceraj, Vanja; Polz, Martin F. (2004). Divergence and redundancy of 16S rRNA sequences in genomes with multiple rrn operons. Journal of Bacteriology 186(9): 2629-2635. https://doi.org/10.1128/JB.186.9.2629-2635.2004
- Acinas, Silvia G.; Sarma-Rupavtarm, Ramahi; Klepac-Ceraj, Vanja; Polz, Martin F. (2005). PCR-induced sequence artifacts and bias: insights from comparison of two 16S rRNA clone libraries constructed from the same sample. Applied and Environmental Microbiology 71(12): 8966-8969. https://doi.org/10.1128/AEM.71.12.8966-8969.2005
- Akerlund, T.; Nordstrom, K.; Bernander, R. (1995). Analysis of cell size and DNA content in exponentially growing and stationary-phase batch cultures of Escherichia coli. Journal of Bacteriology 177(23): 6791-6797. https://doi.org/10.1128/jb.177.23.6791-6797.1995
- Albertsen, Mads; Karst, Sren M.; Ziegler, Anja S.; Kirkegaard, Rasmus H.; Nielsen, Per H. (2015). Back to basics: the influence of DNA extraction and primer choice on phylogenetic analysis of activated sludge communities. PLOS ONE 10(7): e0132783. https://doi.org/10.1371/journal.pone.0132783
- Almeida, Alexandre; Mitchell, Alex L.; Tarkowska, Aleksandra; Finn, Robert D. (2018). Benchmarking taxonomic assignments based on 16S rRNA gene profiling of the microbiota from commonly sampled environments. GigaScience 7(5): giy054. https://doi.org/10.1093/gigascience/giy054
- Alroy, John (2026). Coverage-based rarefaction fails to quantify relative species richness. Oikos: e11607. https://doi.org/10.1002/oik.11607
- Anders, Simon; Huber, Wolfgang (2010). Differential expression analysis for sequence count data. Genome Biology 11(10): R106. https://doi.org/10.1186/gb-2010-11-10-r106
- Angly, Florent E.; Dennis, Paul G.; Skarshewski, Adam; Vanwonterghem, Inka; Hugenholtz, Philip; Tyson, Gene W. (2014). CopyRighter: a rapid tool for improving the accuracy of microbial community profiles through lineage-specific gene copy number correction. Microbiome 2: 11. https://doi.org/10.1186/2049-2618-2-11
- Astudillo-Garcia, Carmen; Bell, James J.; Webster, Nicole S.; Glasl, Bettina; Jompa, Jamaluddin; Montoya, Jose M.; Taylor, Michael W. (2017). Evaluating the core microbiota in complex communities: a systematic investigation. Environmental Microbiology 19(4): 1450-1462. https://doi.org/10.1111/1462-2920.13647
- Bakken, Lars R.; Olsen, Rolf A. (1989). DNA-content of soil bacteria of different cell size. Soil Biology and Biochemistry 21(6): 789-793. https://doi.org/10.1016/0038-0717(89)90172-7
- Barberan, Albert; Ramirez, Kelly S.; Leff, Jonathan W.; Bradford, Mark A.; Wall, Diana H.; Fierer, Noah (2014). Why are some microbes more ubiquitous than others? Predicting the habitat breadth of soil bacteria. Ecology Letters 17(7): 794-802. https://doi.org/10.1111/ele.12282
- Barlow, Jacob T.; Bogatyrev, Said R.; Ismagilov, Rustem F. (2020). A quantitative sequencing framework for absolute abundance measurements of mucosal and lumenal microbial communities. Nature Communications 11: 2590. https://doi.org/10.1038/s41467-020-16224-6
- Bates, Scott T.; Berg-Lyons, Donna; Caporaso, J. Gregory; Walters, William A.; Knight, Rob; Fierer, Noah (2011). Examining the global distribution of dominant archaeal populations in soil. The ISME Journal 5(5): 908-917. https://doi.org/10.1038/ismej.2010.171
- benjjneb (DADA2 maintainer); contributors (n.d.). Consequences of using dada2 on NovaSeq data. GitHub issue #791, benjjneb/dada2. https://github.com/benjjneb/dada2/issues/791
- Beule, Lukas; Karlovsky, Petr (2020). Improved normalization of species count data in ecology by scaling with ranked subsampling (SRS): application to microbial communities. PeerJ 8: e9593. https://doi.org/10.7717/peerj.9593
- Bickel, Samuel; Or, Dani (2021). The chosen few - variations in common and rare soil bacteria across biomes. The ISME Journal 15(11): 3315-3325. https://doi.org/10.1038/s41396-021-00981-3
- Bokulich, Nicholas A.; Kaehler, Benjamin D.; Rideout, Jai Ram; Dillon, Matthew; Bolyen, Evan; Knight, Rob; Huttley, Gavin A.; Caporaso, J. Gregory (2018). Optimizing taxonomic classification of marker-gene amplicon sequences with QIIME 2's q2-feature-classifier plugin. Microbiome 6: 90. https://doi.org/10.1186/s40168-018-0470-z
- Bokulich, Nicholas A.; Rideout, Jai Ram; Mercurio, William G.; Shiffer, Arron; Wolfe, Benjamin; Maurice, Corinne F.; Dutton, Rachel J.; Turnbaugh, Peter J.; Knight, Rob; Caporaso, J. Gregory (2016). mockrobiota: a Public Resource for Microbiome Bioinformatics Benchmarking. mSystems 1(5): e00062-16. https://doi.org/10.1128/mSystems.00062-16
- Bokulich, Nicholas A.; Subramanian, Sathish; Faith, Jeremiah J.; Gevers, Dirk; Gordon, Jeffrey I.; Knight, Rob; Mills, David A.; Caporaso, J. Gregory (2013). Quality-filtering vastly improves diversity estimates from Illumina amplicon sequencing. Nature Methods 10(1): 57-59. https://doi.org/10.1038/nmeth.2276
- Bonk, Fabian; Popp, Denny; Harms, Hauke; Centler, Florian (2018). PCR-based quantification of taxa-specific abundances in microbial communities: quantifying and avoiding common pitfalls. Journal of Microbiological Methods 153: 139-147. https://doi.org/10.1016/j.mimet.2018.09.015
- Bottinger, Benjamin; Semmler, Florian; Zerulla, Karolin; Ludt, Katharina; Soppa, Jorg (2018). Regulated ploidy of Bacillus subtilis and three new isolates of Bacillus and Paenibacillus. FEMS Microbiology Letters 365(4): fnx282. https://doi.org/10.1093/femsle/fnx282
- Bremer, H.; Dennis, P. P. (1996). Modulation of chemical composition and other parameters of the cell by growth rate. Escherichia coli and Salmonella: Cellular and Molecular Biology, 2nd ed., chapter 97.
- Breuert, Sebastian; Allers, Thorsten; Spohn, Gabi; Soppa, Jorg (2006). Regulated polyploidy in halophilic archaea. PLoS ONE 1(1): e92. https://doi.org/10.1371/journal.pone.0000092
- Brewer, Tess E.; Albertsen, Mads; Edwards, Arwyn; Kirkegaard, Rasmus H.; Rocha, Eduardo P. C.; Fierer, Noah (2020). Unlinked rRNA genes are widespread among bacteria and archaea. The ISME Journal 14(2): 597-608. https://doi.org/10.1038/s41396-019-0552-3
- Brown, Christopher T.; Olm, Matthew R.; Thomas, Brian C.; Banfield, Jillian F. (2016). Measurement of bacterial replication rates in microbial communities. Nature Biotechnology 34(12): 1256-1263. https://doi.org/10.1038/nbt.3704
- Bruck, Patrik; Wasser, Daniel; Soppa, Jorg (2023). One advantage of being polyploid: prokaryotes of various phylogenetic groups can grow in the absence of an environmental phosphate source at the expense of their high genome copy numbers. Microorganisms 11(9): 2267. https://doi.org/10.3390/microorganisms11092267
- Bullard, James H.; Purdom, Elizabeth; Hansen, Kasper D.; Dudoit, Sandrine (2010). Evaluation of statistical methods for normalization and differential expression in mRNA-Seq experiments. BMC Bioinformatics 11: 94. https://doi.org/10.1186/1471-2105-11-94
- Buongermino Pereira, Mariana; Wallroth, Mikael; Jonsson, Viktor; Kristiansson, Erik (2018). Comparison of normalization methods for the analysis of metagenomic gene abundance data. BMC Genomics 19: 274. https://doi.org/10.1186/s12864-018-4637-6
- Button, D. K.; Robertson, Betsy R. (2001). Determination of DNA content of aquatic bacteria by flow cytometry. Applied and Environmental Microbiology 67(4): 1636-1645. https://doi.org/10.1128/AEM.67.4.1636-1645.2001
- Calgaro, Matteo; Romualdi, Chiara; Waldron, Levi; Risso, Davide; Vitulo, Nicola (2020). Assessment of statistical methods from single cell, bulk RNA-seq, and metagenomics applied to microbiome data. Genome Biology 21: 191. https://doi.org/10.1186/s13059-020-02104-1
- Callahan, Benjamin J. (n.d.). DADA2 documentation: Pseudo-pooling. https://benjjneb.github.io/dada2/pseudo.html
- Callahan, Benjamin J.; McMurdie, Paul J.; Rosen, Michael J.; Han, Andrew W.; Johnson, Amy Jo A.; Holmes, Susan P. (2016). DADA2: High-resolution sample inference from Illumina amplicon data. Nature Methods 13(7): 581-583. https://doi.org/10.1038/nmeth.3869
- Callahan, Benjamin J.; Wong, Joan; Heiner, Cheryl; Oh, Steve; Theriot, Casey M.; Gulati, Ajay S.; McGill, Sarah K.; Dougherty, Michael K. (2019). High-throughput amplicon sequencing of the full-length 16S rRNA gene with single-nucleotide resolution. Nucleic Acids Research 47(18): e103. https://doi.org/10.1093/nar/gkz569
- Cameron, Ellen S.; Schmidt, Philip J.; Tremblay, Benjamin J.-M.; Emelko, Monica B.; Muller, Kirsten M. (2021). Enhancing diversity analysis by repeatedly rarefying next generation sequencing data describing microbial communities. Scientific Reports 11: 22302. https://doi.org/10.1038/s41598-021-01636-1
- Carini, Paul; Marsden, Patrick J.; Leff, Jonathan W.; Morgan, Emily E.; Strickland, Michael S.; Fierer, Noah (2016). Relic DNA is abundant in soil and obscures estimates of soil microbial diversity. Nature Microbiology 2(3): 16242. https://doi.org/10.1038/nmicrobiol.2016.242
- Caruso, Vincent; Song, Xubo; Asquith, Mark; Karstens, Lisa (2019). Performance of microbiome sequence inference methods in environments with varying biomass. mSystems 4(1): e00163-18. https://doi.org/10.1128/mSystems.00163-18
- Chao, Anne; Gotelli, Nicholas J.; Hsieh, T. C.; Sander, Elizabeth L.; Ma, K. H.; Colwell, Robert K.; Ellison, Aaron M. (2014). Rarefaction and extrapolation with Hill numbers: a framework for sampling and estimation in species diversity studies. Ecological Monographs 84(1): 45-67. https://doi.org/10.1890/13-0133.1
- Chao, Anne; Jost, Lou (2012). Coverage-based rarefaction and extrapolation: standardizing samples by completeness rather than size. Ecology 93(12): 2533-2547. https://doi.org/10.1890/11-1952.1
- Chiarello, Marlene; McCauley, Mark; Villeger, Sebastien; Jackson, Colin R. (2022). Ranking the biases: the choice of OTUs vs. ASVs in 16S rRNA amplicon data analysis has stronger effects on diversity measures than rarefaction and OTU identity threshold. PLOS ONE 17(2): e0264443. https://doi.org/10.1371/journal.pone.0264443
- Chiu, Chun-Huo; Chao, Anne (2016). Estimating and comparing microbial diversity in the presence of sequencing errors. PeerJ 4: e1634. https://doi.org/10.7717/peerj.1634
- Christensen, H.; Olsen, R. A.; Bakken, L. R. (1995). Flow cytometric measurements of cell volumes and DNA contents during culture of indigenous soil bacteria. Microbial Ecology 29(1): 49-62. https://doi.org/10.1007/BF00217422
- Costea, Paul I.; Zeller, Georg; Sunagawa, Shinichi; others (2017). Towards standards for human fecal sample processing in metagenomic studies. Nature Biotechnology 35(11): 1069-1076. https://doi.org/10.1038/nbt.3960
- Costello, Maura; Fleharty, Mark; Abreu, Justin; Farjoun, Yossi; Ferriera, Steven; Holmes, Laurie; Granger, Brian; Green, Lisa; Howd, Tom; Mason, Tamara; Vicente, Gina; Dasilva, Michael; Brodeur, Wendy; DeSmet, Timothy; Dodge, Sheila; Lennon, Niall J.; Gabriel, Stacey (2018). Characterization and remediation of sample index swaps by non-redundant dual indexing on massively parallel sequencing platforms. BMC Genomics 19: 332. https://doi.org/10.1186/s12864-018-4703-0
- Couturier, Etienne; Rocha, Eduardo P. C. (2006). Replication-associated gene dosage effects shape the genomes of fast-growing bacteria but only for transcription and translation genes. Molecular Microbiology 59(5): 1506-1518. https://doi.org/10.1111/j.1365-2958.2006.05046.x
- Curtis, Thomas P.; Sloan, William T.; Scannell, Jack W. (2002). Estimating prokaryotic diversity and its limits. PNAS 99(16): 10494-10499. https://doi.org/10.1073/pnas.142680199
- Custer, Gordon F.; Gans, Maya; van Diepen, Linda T. A.; Dini-Andreote, Francisco; Buerkle, C. Alex (2023). Comparative analysis of core microbiome assignments: implications for ecological synthesis. mSystems 8(1): e01066-22. https://doi.org/10.1128/msystems.01066-22
- D'Amore, Rosalinda; Ijaz, Umer Zeeshan; Schirmer, Melanie; Kenny, John G.; Gregory, Richard; Darby, Alistair C.; Shakya, Migun; Podar, Mircea; Quince, Christopher; Hall, Neil (2016). A comprehensive benchmarking study of protocols and sequencing platforms for 16S rRNA community profiling. BMC Genomics 17: 55. https://doi.org/10.1186/s12864-015-2194-9
- Dai, Tianjiao; Zhang, Yan; Tang, Yushi; Bai, Yaohui; Tao, Yile; Huang, Bei; Wen, Donghui (2016). Identifying the key taxonomic categories that characterize microbial community diversity using full-scale classification: a case study of microbial communities in the sediments of Hangzhou Bay. FEMS Microbiology Ecology 92(10): fiw150. https://doi.org/10.1093/femsec/fiw150
- Davis, Nicole M.; Proctor, Diana M.; Holmes, Susan P.; Relman, David A.; Callahan, Benjamin J. (2018). Simple statistical identification and removal of contaminant sequences in marker-gene and metagenomics data. Microbiome 6: 226. https://doi.org/10.1186/s40168-018-0605-2
- Delgado-Baquerizo, Manuel; Oliverio, Angela M.; Brewer, Tess E.; Benavent-Gonzalez, Alberto; Eldridge, David J.; Bardgett, Richard D.; Maestre, Fernando T.; Singh, Brajesh K.; Fierer, Noah (2018). A global atlas of the dominant bacteria found in soil. Science 359(6373): 320-325. https://doi.org/10.1126/science.aap9516
- Deng, Yongcui; Umbach, Alexander K.; Neufeld, Josh D. (2024). Nonparametric richness estimators Chao1 and ACE must not be used with amplicon sequence variant data. The ISME Journal 18(1): wrae106. https://doi.org/10.1093/ismejo/wrae106
- Dunbar, John; Barns, Susan M.; Ticknor, Lawrence O.; Kuske, Cheryl R. (2002). Empirical and theoretical bacterial diversity in four Arizona soils. Applied and Environmental Microbiology 68(6): 3035-3045. https://doi.org/10.1128/AEM.68.6.3035-3045.2002
- Dyrhovden, Ruben; Rippin, Martin; vreb, Kjell Kare; Nygaard, Randi M.; Ulvestad, Elling; Kommedal, yvind (2021). Managing contamination and diverse bacterial loads in 16S rRNA deep sequencing of clinical samples: implications of the law of small numbers. mBio 12(3): e00598-21. https://doi.org/10.1128/mBio.00598-21
- Earth Microbiome Project (n.d.). 16S Illumina Amplicon Protocol. https://earthmicrobiome.org/protocols-and-standards/16s/
- Edgar, Robert (2018). Taxonomy annotation and guide tree errors in 16S rRNA databases. PeerJ 6: e5030. https://doi.org/10.7717/peerj.5030
- Edgar, Robert C. (2016). UCHIME2: improved chimera prediction for amplicon sequencing. bioRxiv (074252). https://doi.org/10.1101/074252
- Edgar, Robert C. (2016). UNCROSS: filtering of high-frequency cross-talk in 16S amplicon reads. bioRxiv (088666). https://doi.org/10.1101/088666
- Edgar, Robert C. (2017). Accuracy of microbial community diversity estimated by closed- and open-reference OTUs. PeerJ 5: e3889. https://doi.org/10.7717/peerj.3889
- Edgar, Robert C. (2017). UNBIAS: an attempt to correct abundance bias in 16S sequencing, with limited success. bioRxiv (124149). https://doi.org/10.1101/124149
- Edgar, Robert C. (2018). Accuracy of taxonomy prediction for 16S rRNA and fungal ITS sequences. PeerJ 6: e4652. https://doi.org/10.7717/peerj.4652
- Edgar, Robert C. (2018). Updating the 97% identity threshold for 16S ribosomal RNA OTUs. Bioinformatics 34(14): 2371-2375. https://doi.org/10.1093/bioinformatics/bty113
- Edgar, Robert C.; Flyvbjerg, Henrik (2015). Error filtering, pair assembly and error correction for next-generation sequencing reads. Bioinformatics 31(21): 3476-3482. https://doi.org/10.1093/bioinformatics/btv401
- Eisenhofer, Raphael; Minich, Jeremiah J.; Marotz, Clarisse; Cooper, Alan; Knight, Rob; Weyrich, Laura S. (2019). Contamination in low microbial biomass microbiome studies: issues and recommendations. Trends in Microbiology 27(2): 105-117. https://doi.org/10.1016/j.tim.2018.11.003
- Emory Integrated Genomics Core / ECGC (n.d.). Amplicon 16S metagenomics (methods description). https://www.cores.emory.edu/ecgc/_includes/documents/sections/resources/amplicon-16s-metagenomics.pdf
- Esling, Philippe; Lejzerowicz, Franck; Pawlowski, Jan (2015). Accurate multiplexing and filtering for high-throughput amplicon-sequencing. Nucleic Acids Research 43(5): 2513-2524. https://doi.org/10.1093/nar/gkv107
- Farrelly, V.; Rainey, F. A.; Stackebrandt, E. (1995). Effect of genome size and rrn gene copy number on PCR amplification of 16S rRNA genes from a mixture of bacterial species. Applied and Environmental Microbiology 61(7): 2798-2801. https://doi.org/10.1128/aem.61.7.2798-2801.1995
- Fitzpatrick, Connor R.; Lu-Irving, Patricia; Copeland, Julia; Guttman, David S.; Wang, Pauline W.; Baltrus, David A.; Dlugosch, Katrina M.; Johnson, Marc T. J. (2018). Chloroplast sequence variation and the efficacy of peptide nucleic acids for blocking host amplification in plant microbiome studies. Microbiome 6: 144. https://doi.org/10.1186/s40168-018-0534-0
- Fouhy, Fiona; Clooney, Adam G.; Stanton, Catherine; Claesson, Marcus J.; Cotter, Paul D. (2016). 16S rRNA gene sequencing of mock microbial populations: impact of DNA extraction method, primer choice and sequencing platform. BMC Microbiology 16: 123. https://doi.org/10.1186/s12866-016-0738-z
- Frostegard, Asa; Courtois, Sophie; Ramisse, Vincent; Clerc, Sylvie; Bernillon, Dominique; Le Gall, Francoise; Jeannin, Pascale; Nesme, Xavier; Simonet, Pascal (1999). Quantification of bias related to the extraction of DNA directly from soils. Applied and Environmental Microbiology 65(12): 5409-5420. https://doi.org/10.1128/AEM.65.12.5409-5420.1999
- Galand, Pierre E.; Casamayor, Emilio O.; Kirchman, David L.; Lovejoy, Connie (2009). Ecology of the rare microbial biosphere of the Arctic Ocean. PNAS 106(52): 22427-22432. https://doi.org/10.1073/pnas.0908284106
- Galazzo, Gianluca; van Best, Niels; Benedikter, Birke J.; Janssen, Kevin; Bervoets, Liene; Driessen, Christel; Oomen, Melissa; Lucchesi, Mayk; van Eijck, Pascalle H.; Becker, Heike E. F.; Hornef, Mathias W.; Savelkoul, Paul H.; Stassen, Frank R. M.; Wolffs, Petra F.; Penders, John (2020). How to count our microbes? The effect of different quantitative microbiome profiling approaches. Frontiers in Cellular and Infection Microbiology 10: 403. https://doi.org/10.3389/fcimb.2020.00403
- Gans, Jason; Wolinsky, Murray; Dunbar, John (2005). Computational improvements reveal great bacterial diversity and high metal toxicity in soil. Science 309(5739): 1387-1390. https://doi.org/10.1126/science.1112665
- Gao, Yingnan; Wu, Martin (2023). Accounting for 16S rRNA copy number prediction uncertainty and its implications in bacterial diversity analyses. ISME Communications 3: 59. https://doi.org/10.1038/s43705-023-00266-0
- Gaston, Kevin J.; Blackburn, Tim M.; Greenwood, Jeremy J. D.; Gregory, Richard D.; Quinn, Rachel M.; Lawton, John H. (2000). Abundance-occupancy relationships. Journal of Applied Ecology 37(s1): 39-59. https://doi.org/10.1046/j.1365-2664.2000.00485.x
- Gibbons, Sean M.; Duvallet, Claire; Alm, Eric J. (2018). Correcting for batch effects in case-control microbiome studies. PLOS Computational Biology 14(4): e1006102. https://doi.org/10.1371/journal.pcbi.1006102
- Gihring, Thomas M.; Green, Stefan J.; Schadt, Christopher W. (2012). Massively parallel rRNA gene sequencing exacerbates the potential for biased community diversity comparisons due to variable library sizes. Environmental Microbiology 14(2): 285-290. https://doi.org/10.1111/j.1462-2920.2011.02550.x
- Glassman, Sydney I.; Martiny, Jennifer B. H. (2018). Broadscale ecological patterns are robust to use of exact sequence variants versus operational taxonomic units. mSphere 3(4): e00148-18. https://doi.org/10.1128/mSphere.00148-18
- Gloor, Gregory B.; Macklaim, Jean M.; Pawlowsky-Glahn, Vera; Egozcue, Juan J. (2017). Microbiome datasets are compositional: and this is not optional. Frontiers in Microbiology 8: 2224. https://doi.org/10.3389/fmicb.2017.02224
- Gobet, Angelique; Quince, Christopher; Ramette, Alban (2010). Multivariate Cutoff Level Analysis (MultiCoLA) of large community data sets. Nucleic Acids Research 38(15): e155. https://doi.org/10.1093/nar/gkq545
- Gohl, Daryl M; Vangay, Pajau; Garbe, John; MacLean, Allison; Hauge, Adam; Becker, Aaron; Gould, Trevor J; Clayton, Jonathan B; Johnson, Timothy J; Hunter, Ryan; Knights, Dan; Beckman, Kenneth B (2016). Systematic improvement of amplicon marker gene methods for increased accuracy in microbiome studies. Nature Biotechnology 34(9): 942-949. https://doi.org/10.1038/nbt.3601
- Gotelli, Nicholas J.; Colwell, Robert K. (2001). Quantifying biodiversity: procedures and pitfalls in the measurement and comparison of species richness. Ecology Letters 4(4): 379-391. https://doi.org/10.1046/j.1461-0248.2001.00230.x
- Griese, Marco; Lange, Christian; Soppa, Jorg (2011). Ploidy in cyanobacteria. FEMS Microbiology Letters 323(2): 124-131. https://doi.org/10.1111/j.1574-6968.2011.02368.x
- Grilli, Jacopo (2020). Macroecological laws describe variation and diversity in microbial communities. Nature Communications 11: 4743. https://doi.org/10.1038/s41467-020-18529-y
- Haas, Brian J.; Gevers, Dirk; Earl, Ashlee M.; Feldgarden, Mike; Ward, Doyle V.; Giannoukos, Georgia; Ciulla, Dawn; Tabbaa, Diana; Highlander, Sarah K.; Sodergren, Erica; Methe, Barbara; DeSantis, Todd Z.; The Human Microbiome Consortium; Petrosino, Joseph F.; Knight, Rob; Birren, Bruce W. (2011). Chimeric 16S rRNA sequence formation and detection in Sanger and 454-pyrosequenced PCR amplicons. Genome Research 21(3): 494-504. https://doi.org/10.1101/gr.112730.110
- Haegeman, Bart; Hamelin, Jerome; Moriarty, John; Neal, Peter; Dushoff, Jonathan; Weitz, Joshua S. (2013). Robust estimation of microbial diversity in theory and in practice. The ISME Journal 7(6): 1092-1101. https://doi.org/10.1038/ismej.2013.10
- Harrison, Joshua G.; Calder, W. John; Shastry, Vivaswat; Buerkle, C. Alex (2020). Dirichlet-multinomial modelling outperforms alternatives for analysis of microbiome and other ecological count data. Molecular Ecology Resources 20(2): 481-497. https://doi.org/10.1111/1755-0998.13128
- Harrison, Joshua G.; Calder, W. John; Shuman, Bryan; Buerkle, C. Alex (2021). The quest for absolute abundance: the use of internal standards for DNA-based community ecology. Molecular Ecology Resources 21(1): 30-43. https://doi.org/10.1111/1755-0998.13247
- Hawinkel, Stijn; Mattiello, Federico; Bijnens, Luc; Thas, Olivier (2019). A broken promise: microbiome differential abundance methods do not control the false discovery rate. Briefings in Bioinformatics 20(1): 210-221. https://doi.org/10.1093/bib/bbx104
- Hildenbrand, Catherina; Stock, Tilmann; Lange, Christian; Rother, Michael; Soppa, Jorg (2011). Genome copy numbers and gene conversion in methanogenic archaea. Journal of Bacteriology 193(3): 734-743. https://doi.org/10.1128/JB.01016-10
- Holt, Alison R.; Gaston, Kevin J.; He, Fangliang (2002). Occupancy-abundance relationships and spatial distribution: a review. Basic and Applied Ecology 3(1): 1-13. https://doi.org/10.1078/1439-1791-00083
- Hong, Johnny; Karaoz, Ulas; de Valpine, Perry; Fithian, William (2022). To rarefy or not to rarefy: robustness and efficiency trade-offs of rarefying microbiome data. Bioinformatics 38(9): 2389-2396. https://doi.org/10.1093/bioinformatics/btac127
- Hornung, Bastian V. H.; Zwittink, Romy D.; Kuijper, Ed J. (2019). Issues and current standards of controls in microbiome research. FEMS Microbiology Ecology 95(5): fiz045. https://doi.org/10.1093/femsec/fiz045
- Howe, Adina Chuang; Jansson, Janet K.; Malfatti, Stephanie A.; Tringe, Susannah G.; Tiedje, James M.; Brown, C. Titus (2014). Tackling soil diversity with the assembly of large, complex metagenomes. PNAS 111(13): 4904-4909. https://doi.org/10.1073/pnas.1402564111
- Hurlbert, Stuart H. (1971). The nonconcept of species diversity: a critique and alternative parameters. Ecology 52(4): 577-586. https://doi.org/10.2307/1934145
- Huse, Susan M.; Welch, David Mark; Morrison, Hilary G.; Sogin, Mitchell L. (2010). Ironing out the wrinkles in the rare biosphere through improved OTU clustering. Environmental Microbiology 12(7): 1889-1898. https://doi.org/10.1111/j.1462-2920.2010.02193.x
- Illumina, Inc. (n.d.). 16S Metagenomic Sequencing Library Preparation: Preparing 16S Ribosomal RNA Gene Amplicons for the Illumina MiSeq System. Part # 15044223 Rev. B. https://support.illumina.com/documents/documentation/chemistry_documentation/16s/16s-metagenomic-library-prep-guide-15044223-b.pdf
- Illumina, Inc. (n.d.). Index hopping (web page). https://www.illumina.com/techniques/sequencing/ngs-library-prep/multiplexing/index-hopping.html
- Janda, J. Michael; Abbott, Sharon L. (2007). 16S rRNA Gene Sequencing for Bacterial Identification in the Diagnostic Laboratory: Pluses, Perils, and Pitfalls. Journal of Clinical Microbiology 45(9): 2761-2764. https://doi.org/10.1128/JCM.01228-07
- Jia, Xiu; Dini-Andreote, Francisco; Salles, Joana Falcao (2018). Community assembly processes of the microbial rare biosphere. Trends in Microbiology 26(9): 738-747. https://doi.org/10.1016/j.tim.2018.02.011
- Jia, Xiu; Dini-Andreote, Francisco; Salles, Joana Falcao (2022). Unravelling the interplay of ecological processes structuring the bacterial rare biosphere. ISME Communications 2: 96. https://doi.org/10.1038/s43705-022-00177-6
- Jian, Ching; Luukkonen, Panu; Yki-Jarvinen, Hannele; Salonen, Anne; Korpela, Katri (2020). Quantitative PCR provides a simple and accessible method for quantitative microbiota profiling. PLOS ONE 15(1): e0227285. https://doi.org/10.1371/journal.pone.0227285
- Johnson, Jethro S.; Spakowicz, Daniel J.; Hong, Bo-Young; Petersen, Lauren M.; Demkowicz, Patrick; Chen, Lei; Leopold, Shana R.; Hanson, Blake M.; Agresta, Hanako O.; Gerstein, Mark; Sodergren, Erica; Weinstock, George M. (2019). Evaluation of 16S rRNA gene sequencing for species and strain-level microbiome analysis. Nature Communications 10: 5029. https://doi.org/10.1038/s41467-019-13036-1
- Joos, Lisa; Beirinckx, Stien; Haegeman, Annelies; Debode, Jane; Vandecasteele, Bart; Baeyen, Steve; Goormachtig, Sofie; Clement, Lieven; De Tender, Caroline (2020). Daring to be differential: metabarcoding analysis of soil and plant-related microbial communities using amplicon sequence variants and operational taxonomical units. BMC Genomics 21: 733. https://doi.org/10.1186/s12864-020-07126-4
- Jousset, Alexandre; Bienhold, Christina; Chatzinotas, Antonis; Gallien, Laure; Gobet, Angelique; Kurm, Viola; Kusel, Kirsten; Rillig, Matthias C.; Rivett, Damian W.; Salles, Joana F.; van der Heijden, Marcel G. A.; Youssef, Noha H.; Zhang, Xiaowei; Wei, Zhong; Hol, W. H. Gera (2017). Where less may be more: how the rare biosphere pulls ecosystems strings. The ISME Journal 11(4): 853-862. https://doi.org/10.1038/ismej.2016.174
- Kaehler, Benjamin D.; Bokulich, Nicholas A.; McDonald, Daniel; Knight, Rob; Caporaso, J. Gregory; Huttley, Gavin A. (2019). Species abundance information improves sequence taxonomy classification accuracy. Nature Communications 10: 4643. https://doi.org/10.1038/s41467-019-12669-6
- Karstens, Lisa; Asquith, Mark; Davin, Sean; Fair, Damien; Gregory, W. Thomas; Wolfe, Alan J.; Braun, Jonathan; McWeeney, Shannon (2019). Controlling for contaminants in low-biomass 16S rRNA gene sequencing experiments. mSystems 4(4): e00290-19. https://doi.org/10.1128/mSystems.00290-19
- Kaul, Abhishek; Mandal, Siddhartha; Davidov, Ori; Peddada, Shyamal D. (2017). Analysis of microbiome data in the presence of excess zeros. Frontiers in Microbiology 8: 2114. https://doi.org/10.3389/fmicb.2017.02114
- Kebschull, Justus M.; Zador, Anthony M. (2015). Sources of PCR-induced distortions in high-throughput sequencing data sets. Nucleic Acids Research 43(21): e143. https://doi.org/10.1093/nar/gkv717
- Kelly, Ryan P.; Shelton, Andrew Olaf; Gallego, Ramon (2019). Understanding PCR processes to draw meaningful conclusions from environmental DNA studies. Scientific Reports 9: 12133. https://doi.org/10.1038/s41598-019-48546-x
- Kembel, Steven W.; Wu, Martin; Eisen, Jonathan A.; Green, Jessica L. (2012). Incorporating 16S gene copy number information improves estimates of microbial diversity and abundance. PLOS Computational Biology 8(10): e1002743. https://doi.org/10.1371/journal.pcbi.1002743
- Kennedy, Katherine; Hall, Michael W.; Lynch, Michael D. J.; Moreno-Hagelsieb, Gabriel; Neufeld, Josh D. (2014). Evaluating bias of Illumina-based bacterial 16S rRNA gene profiles. Applied and Environmental Microbiology 80(18): 5717-5722. https://doi.org/10.1128/AEM.01451-14
- Kers, Jannigje Gerdien; Saccenti, Edoardo (2022). The power of microbiome studies: some considerations on which alpha and beta metrics to use and how to report results. Frontiers in Microbiology 12: 796025. https://doi.org/10.3389/fmicb.2021.796025
- Kircher, Martin; Sawyer, Susanna; Meyer, Matthias (2012). Double indexing overcomes inaccuracies in multiplex sequencing on the Illumina platform. Nucleic Acids Research 40(1): e3. https://doi.org/10.1093/nar/gkr771
- Klappenbach, Joel A.; Dunbar, John M.; Schmidt, Thomas M. (2000). rRNA operon copy number reflects ecological strategies of bacteria. Applied and Environmental Microbiology 66(4): 1328-1333. https://doi.org/10.1128/AEM.66.4.1328-1333.2000
- Klappenbach, Joel A.; Saxman, Paul R.; Cole, James R.; Schmidt, Thomas M. (2001). rrndb: the Ribosomal RNA Operon Copy Number Database. Nucleic Acids Research 29(1): 181-184. https://doi.org/10.1093/nar/29.1.181
- Klindworth, Anna; Pruesse, Elmar; Schweer, Timmy; Peplies, Jorg; Quast, Christian; Horn, Matthias; Glockner, Frank Oliver (2013). Evaluation of general 16S ribosomal RNA gene PCR primers for classical and next-generation sequencing-based diversity studies. Nucleic Acids Research 41(1): e1. https://doi.org/10.1093/nar/gks808
- Kopylova, Evguenia; Navas-Molina, Jose A.; Mercier, Celine; Xu, Zhenjiang Zech; Mahe, Frederic; He, Yan; Zhou, Hong-Wei; Rognes, Torbjrn; Caporaso, J. Gregory; Knight, Rob (2016). Open-source sequence clustering methods improve the state of the art. mSystems 1(1): e00003-15. https://doi.org/10.1128/mSystems.00003-15
- Korem, Tal; Zeevi, David; Suez, Jotham; Weinberger, Adina; Avnit-Sagi, Tali; Pompan-Lotan, Maya; Matot, Elad; Jona, Ghil; Harmelin, Alon; Cohen, Nadav; Sirota-Madi, Alexandra; Thaiss, Christoph A.; Pevsner-Fischer, Meirav; Sorek, Rotem; Xavier, Ramnik J.; Elinav, Eran; Segal, Eran (2015). Growth dynamics of gut microbiota in health and disease inferred from single metagenomic samples. Science 349(6252): 1101-1106. https://doi.org/10.1126/science.aac4812
- Kozich, James J.; Westcott, Sarah L.; Baxter, Nielson T.; Highlander, Sarah K.; Schloss, Patrick D. (2013). Development of a dual-index sequencing strategy and curation pipeline for analyzing amplicon sequence data on the MiSeq Illumina sequencing platform. Applied and Environmental Microbiology 79(17): 5112-5120. https://doi.org/10.1128/AEM.01043-13
- Kumar, M. Senthil; Slud, Eric V.; Okrah, Kwame; Hicks, Stephanie C.; Hannenhalli, Sridhar; Corrada Bravo, Hector (2018). Analysis and correction of compositional bias in sparse sequencing count data. BMC Genomics 19: 799. https://doi.org/10.1186/s12864-018-5160-5
- Kunin, Victor; Engelbrektson, Anna; Ochman, Howard; Hugenholtz, Philip (2010). Wrinkles in the rare biosphere: pyrosequencing errors can lead to artificial inflation of diversity estimates. Environmental Microbiology 12(1): 118-123. https://doi.org/10.1111/j.1462-2920.2009.02051.x
- La Rosa, Patricio S.; Brooks, J. Paul; Deych, Elena; Boone, Edward L.; Edwards, David J.; Wang, Qin; Sodergren, Erica; Weinstock, George; Shannon, William D. (2012). Hypothesis testing and power calculations for taxonomic-based human microbiome data. PLOS ONE 7(12): e52078. https://doi.org/10.1371/journal.pone.0052078
- Lauber, Christian L.; Zhou, Nicholas; Gordon, Jeffrey I.; Knight, Rob; Fierer, Noah (2010). Effect of storage conditions on the assessment of bacterial community structure in soil and human-associated samples. FEMS Microbiology Letters 307(1): 80-86. https://doi.org/10.1111/j.1574-6968.2010.01965.x
- Laursen, Martin F.; Dalgaard, Marlene D.; Bahl, Martin I. (2017). Genomic GC-content affects the accuracy of 16S rRNA gene sequencing based microbial profiling due to PCR bias. Frontiers in Microbiology 8: 1934. https://doi.org/10.3389/fmicb.2017.01934
- Lavrinienko, Anton; Jernfors, Toni; Koskimaki, Janne J.; Pirttila, Anna Maria; Watts, Phillip C. (2021). Does intraspecific variation in rDNA copy number affect analysis of microbial communities?. Trends in Microbiology 29(1): 19-27. https://doi.org/10.1016/j.tim.2020.05.019
- Lee, Zarraz M.-P.; Bussema, III, Carl; Schmidt, Thomas M. (2009). rrnDB: documenting the number of rRNA and tRNA genes in bacteria and archaea. Nucleic Acids Research 37(Database issue): D489-D493. https://doi.org/10.1093/nar/gkn689
- Lennon, Jay T.; Muscarella, Mario E.; Placella, Sarah A.; Lehmkuhl, Brent K. (2018). How, when, and where relic DNA affects microbial diversity. mBio 9(3): e00637-18. https://doi.org/10.1128/mBio.00637-18
- Lin, Huang; Peddada, Shyamal Das (2020). Analysis of compositions of microbiomes with bias correction. Nature Communications 11: 3514. https://doi.org/10.1038/s41467-020-17041-7
- Lin, Yajuan; Gifford, Scott; Ducklow, Hugh; Schofield, Oscar; Cassar, Nicolas (2019). Towards quantitative microbiome community profiling using internal standards. Applied and Environmental Microbiology 85(5): e02634-18. https://doi.org/10.1128/AEM.02634-18
- Ling, Wodan; Lu, Jiuyao; Zhao, Ni; Lulla, Anju; Plantinga, Anna M.; Fu, Weijia; Zhang, Angela; Liu, Hongjiao; Song, Hoseung; Li, Zhigang; Chen, Jun; Randolph, Timothy W.; Koay, Wei Li A.; White, James R.; Launer, Lenore J.; Fodor, Anthony A.; Meyer, Katie A.; Wu, Michael C. (2022). Batch effects removal for microbiome data via conditional quantile regression. Nature Communications 13: 5418. https://doi.org/10.1038/s41467-022-33071-9
- Llorens-Rico, Veronica; Vieira-Silva, Sara; Goncalves, Pedro J.; Falony, Gwen; Raes, Jeroen (2021). Benchmarking microbiome transformations favors experimental quantitative approaches to address compositionality and sampling depth biases. Nature Communications 12: 3562. https://doi.org/10.1038/s41467-021-23821-6
- Locey, Kenneth J.; Lennon, Jay T. (2016). Scaling laws predict global microbial diversity. PNAS 113(21): 5970-5975. https://doi.org/10.1073/pnas.1521291113
- Louca, Stilianos; Doebeli, Michael; Parfrey, Laura Wegener (2018). Correcting for 16S rRNA gene copy numbers in microbiome surveys remains an unsolved problem. Microbiome 6: 41. https://doi.org/10.1186/s40168-018-0420-9
- Lundberg, Derek S.; Yourstone, Scott; Mieczkowski, Piotr; Jones, Corbin D.; Dangl, Jeffery L. (2013). Practical innovations for high-throughput amplicon sequencing. Nature Methods 10(10): 999-1002. https://doi.org/10.1038/nmeth.2634
- Lundin, Daniel; Severin, Ina; Logue, Jurg Brendan; Ostman, Orjan; Andersson, Anders F.; Lindstrom, Eva S. (2012). Which sequencing depth is sufficient to describe patterns in bacterial alpha- and beta-diversity?. Environmental Microbiology Reports 4(3): 367-372. https://doi.org/10.1111/j.1758-2229.2012.00345.x
- Lynch, Michael D. J.; Neufeld, Josh D. (2015). Ecology and exploration of the rare biosphere. Nature Reviews Microbiology 13(4): 217-229. https://doi.org/10.1038/nrmicro3400
- Magurran, Anne E.; Henderson, Peter A. (2003). Explaining the excess of rare species in natural species abundance distributions. Nature 422(6933): 714-716. https://doi.org/10.1038/nature01547
- Mandal, Siddhartha; Van Treuren, Will; White, Richard A.; Eggesb, Merete; Knight, Rob; Peddada, Shyamal D. (2015). Analysis of composition of microbiomes: a novel method for studying microbial composition. Microbial Ecology in Health and Disease 26: 27663. https://doi.org/10.3402/mehd.v26.27663
- Marioni, John C.; Mason, Christopher E.; Mane, Shrikant M.; Stephens, Matthew; Gilad, Yoav (2008). RNA-seq: an assessment of technical reproducibility and comparison with gene expression arrays. Genome Research 18(9): 1509-1517. https://doi.org/10.1101/gr.079558.108
- Marizzoni, Moira; Gurry, Thomas; Provasi, Stefania; Greub, Gilbert; Lopizzo, Nicola; Ribaldi, Federica; Festari, Cristina; Mazzelli, Monica; Mombelli, Elisa; Salvatore, Marco; Mirabelli, Peppino; Franzese, Monica; Soricelli, Andrea; Frisoni, Giovanni B.; Cattaneo, Annamaria (2020). Comparison of bioinformatics pipelines and operating systems for the analyses of 16S rRNA gene amplicon sequences in human fecal samples. Frontiers in Microbiology 11: 1262. https://doi.org/10.3389/fmicb.2020.01262
- Marotz, Clarisse; Sharma, Amnon; Humphrey, Greg; Gottel, Neil; Daum, Christopher; Gilbert, Jack A.; Eloe-Fadrosh, Emiley; Knight, Rob (2019). Triplicate PCR reactions for 16S rRNA gene amplicon sequencing are unnecessary. BioTechniques 67(1): 29-32. https://doi.org/10.2144/btn-2018-0192
- Martin, Bryan D.; Witten, Daniela; Willis, Amy D. (2020). Modeling microbial abundances and dysbiosis with beta-binomial regression. The Annals of Applied Statistics 14(1): 94-115. https://doi.org/10.1214/19-AOAS1283
- Martin-Laurent, Fabrice; Philippot, Laurent; Hallet, Sabine; Chaussod, Remi; Germon, Jean-Claude; Soulas, Guy; Catroux, Gerard (2001). DNA extraction from soils: old bias for new microbial diversity analysis methods. Applied and Environmental Microbiology 67(5): 2354-2359. https://doi.org/10.1128/AEM.67.5.2354-2359.2001
- McGill, Brian J.; Etienne, Rampal S.; Gray, John S.; Alonso, David; Anderson, Marti J.; Benecha, Habtamu Kassa; Dornelas, Maria; Enquist, Brian J.; Green, Jessica L.; He, Fangliang; Hurlbert, Allen H.; Magurran, Anne E.; Marquet, Pablo A.; Maurer, Brian A.; Ostling, Annette; Soykan, Candan U.; Ugland, Karl I.; White, Ethan P. (2007). Species abundance distributions: moving beyond single prediction theories to integration within an ecological framework. Ecology Letters 10(10): 995-1015. https://doi.org/10.1111/j.1461-0248.2007.01094.x
- McKnight, Donald T.; Huerlimann, Roger; Bower, Deborah S.; Schwarzkopf, Lin; Alford, Ross A.; Zenger, Kyall R. (2019). Methods for normalizing microbiome data: an ecological perspective. Methods in Ecology and Evolution 10(3): 389-400. https://doi.org/10.1111/2041-210X.13115
- McLaren, Michael R.; Nearing, Jacob T.; Willis, Amy D.; Lloyd, Karen G.; Callahan, Benjamin J. (2022). Implications of taxonomic bias for microbial differential-abundance analysis. bioRxiv (2022.08.19.504330). https://doi.org/10.1101/2022.08.19.504330
- McLaren, Michael R.; Willis, Amy D.; Callahan, Benjamin J. (2019). Consistent and correctable bias in metagenomic sequencing experiments. eLife 8: e46923. https://doi.org/10.7554/eLife.46923
- McMurdie, Paul J.; Holmes, Susan (2014). Waste not, want not: why rarefying microbiome data is inadmissible. PLOS Computational Biology 10(4): e1003531. https://doi.org/10.1371/journal.pcbi.1003531
- Milo, Ron; Jorgensen, Paul; Moran, Uri; Weber, Griffin; Springer, Michael (2010). BioNumbers entry 102360, Average number of rRNA genes per genome, citing H. Bremer and P. P. Dennis (1996), ch. 97, Table 3. Nucleic Acids Research 38(suppl_1): D750-D753. https://doi.org/10.1093/nar/gkp889
- Minich, Jeremiah J.; Sanders, Jon G.; Amir, Amnon; Humphrey, Greg; Gilbert, Jack A.; Knight, Rob (2019). Quantifying and understanding well-to-well contamination in microbiome research. mSystems 4(4): e00186-19. https://doi.org/10.1128/mSystems.00186-19
- Morton, James T.; Marotz, Clarisse; Washburne, Alex; Silverman, Justin; Zaramela, Livia S.; Edlund, Anna; Zengler, Karsten; Knight, Rob (2019). Establishing microbial composition measurement standards with reference frames. Nature Communications 10: 2719. https://doi.org/10.1038/s41467-019-10656-5
- Murali, Adithya; Bhargava, Aniruddha; Wright, Erik S. (2018). IDTAXA: a novel approach for accurate taxonomic classification of microbiome sequences. Microbiome 6: 140. https://doi.org/10.1186/s40168-018-0521-5
- Nearing, Jacob T.; Douglas, Gavin M.; Comeau, Andre M.; Langille, Morgan G. I. (2018). Denoising the Denoisers: an independent evaluation of microbiome sequence error-correction approaches. PeerJ 6: e5364. https://doi.org/10.7717/peerj.5364
- Nearing, Jacob T.; Douglas, Gavin M.; Hayes, Molly G.; MacDonald, Jocelyn; Desai, Dhwani K.; Allward, Nicole; Jones, Casey M. A.; Wright, Robyn J.; Dhanani, Akhilesh S.; Comeau, Andre M.; Langille, Morgan G. I. (2022). Microbiome differential abundance methods produce different results across 38 datasets. Nature Communications 13: 342. https://doi.org/10.1038/s41467-022-28034-z
- Nemergut, Diana R.; Costello, Elizabeth K.; Hamady, Micah; Lozupone, Catherine; Jiang, Lin; Schmidt, Steven K.; Fierer, Noah; Townsend, Alan R.; Cleveland, Cory C.; Stanish, Lee; Knight, Rob (2011). Global patterns in the biogeography of bacterial taxa. Environmental Microbiology 13(1): 135-144. https://doi.org/10.1111/j.1462-2920.2010.02315.x
- Nemergut, Diana R.; Knelman, Joseph E.; Ferrenberg, Scott; Bilinski, Teresa; Melbourne, Brett; Jiang, Lin; Violle, Cyrille; Darcy, John L.; Prest, Tiffany; Schmidt, Steven K.; Townsend, Alan R. (2016). Decreases in average bacterial community rRNA operon copy number during succession. The ISME Journal 10(5): 1147-1156. https://doi.org/10.1038/ismej.2015.191
- Neu, Alexander T.; Allen, Eric E.; Roy, Kaustuv (2021). Defining and quantifying the core microbiome: challenges and prospects. PNAS 118(51): e2104429118. https://doi.org/10.1073/pnas.2104429118
- Parada, Alma E.; Needham, David M.; Fuhrman, Jed A. (2016). Every base matters: assessing small subunit rRNA primers for marine microbiomes with mock communities, time series and global field samples. Environmental Microbiology 18(5): 1403-1414. https://doi.org/10.1111/1462-2920.13023
- Pascoal, Francisco; Branco, Paula; Torgo, Luis; Costa, Rodrigo; Magalhaes, Catarina (2025). Definition of the microbial rare biosphere through unsupervised machine learning. Communications Biology 8: 544. https://doi.org/10.1038/s42003-025-07912-4
- Pascoal, Francisco; Costa, Rodrigo; Magalhaes, Catarina (2021). The microbial rare biosphere: current concepts, methods and ecological principles. FEMS Microbiology Ecology 97(1): fiaa227. https://doi.org/10.1093/femsec/fiaa227
- Pecoraro, Vito; Zerulla, Karolin; Lange, Christian; Soppa, Jorg (2011). Quantification of ploidy in proteobacteria revealed the existence of monoploid, (mero-)oligoploid and polyploid species. PLoS ONE 6(1): e16392. https://doi.org/10.1371/journal.pone.0016392
- Pedros-Alio, Carlos (2012). The rare bacterial biosphere. Annual Review of Marine Science 4: 449-466. https://doi.org/10.1146/annurev-marine-120710-100948
- Pelto, Juho; Auranen, Kari; Kujala, Janne V.; Lahti, Leo (2025). Elementary methods provide more replicable results in microbial differential abundance analysis. Briefings in Bioinformatics 26(2): bbaf130. https://doi.org/10.1093/bib/bbaf130
- Penton, C. Ryan; Gupta, Vadakattu V. S. R.; Yu, Julian; Tiedje, James M. (2016). Size matters: assessing optimum soil sample size for fungal and bacterial community structure analyses using high throughput sequencing of rRNA gene amplicons. Frontiers in Microbiology 7: 824. https://doi.org/10.3389/fmicb.2016.00824
- Perisin, Matthew; Vetter, Madlen; Gilbert, Jack A.; Bergelson, Joy (2016). 16Stimator: statistical estimation of ribosomal gene copy numbers from draft genome assemblies. The ISME Journal 10(4): 1020-1024. https://doi.org/10.1038/ismej.2015.161
- Pinto, Ameet J.; Raskin, Lutgarde (2012). PCR biases distort bacterial and archaeal community structure in pyrosequencing datasets. PLOS ONE 7(8): e43093. https://doi.org/10.1371/journal.pone.0043093
- Polz, Martin F.; Cavanaugh, Colleen M. (1998). Bias in template-to-product ratios in multitemplate PCR. Applied and Environmental Microbiology 64(10): 3724-3730. https://doi.org/10.1128/AEM.64.10.3724-3730.1998
- Prodan, Andrei; Tremaroli, Valentina; Brolin, Harald; Zwinderman, Aeilko H.; Nieuwdorp, Max; Levin, Evgeni (2020). Comparing bioinformatic pipelines for microbial 16S rRNA amplicon sequencing. PLOS ONE 15(1): e0227434. https://doi.org/10.1371/journal.pone.0227434
- Props, Ruben; Kerckhof, Frederiek-Maarten; Rubbens, Peter; De Vrieze, Jo; Hernandez Sanabria, Emma; Waegeman, Willem; Monsieurs, Pieter; Hammes, Frederik; Boon, Nico (2017). Absolute quantification of microbial taxon abundances. The ISME Journal 11(2): 584-587. https://doi.org/10.1038/ismej.2016.117
- Quince, Christopher; Curtis, Thomas P.; Sloan, William T. (2008). The rational exploration of microbial diversity. The ISME Journal 2(10): 997-1006. https://doi.org/10.1038/ismej.2008.69
- Rabinowitz, Deborah (1981). Seven forms of rarity. The Biological Aspects of Rare Plant Conservation: 205-217.
- Ramirez, Kelly S.; others (2018). Nature Microbiology 3(2): 189-196. https://doi.org/10.1038/s41564-017-0062-x
- Reitmeier, Sandra; Hitch, Thomas C. A.; Treichel, Nicole; Fikas, Nikolaos; Hausmann, Bela; Ramer-Tait, Amanda E.; Neuhaus, Klaus; Berry, David; Haller, Dirk; Lagkouvardos, Ilias; Clavel, Thomas (2021). Handling of spurious sequences affects the outcome of high-throughput 16S rRNA gene amplicon profiling. ISME Communications 1(1): 31. https://doi.org/10.1038/s43705-021-00033-z
- Risely, Alice (2020). Applying the core microbiome to understand host-microbe systems. Journal of Animal Ecology 89(7): 1549-1558. https://doi.org/10.1111/1365-2656.13229
- Robinson, Mark D.; Oshlack, Alicia (2010). A scaling normalization method for differential expression analysis of RNA-seq data. Genome Biology 11(3): R25. https://doi.org/10.1186/gb-2010-11-3-r25
- Rodriguez-R, Luis M.; Konstantinidis, Konstantinos T. (2014). Estimating coverage in metagenomic data sets and why it matters. The ISME Journal 8(11): 2349-2351. https://doi.org/10.1038/ismej.2014.76
- Roller, Benjamin R. K.; Stoddard, Steven F.; Schmidt, Thomas M. (2016). Exploiting rRNA operon copy number to investigate bacterial reproductive strategies. Nature Microbiology 1(11): 16160. https://doi.org/10.1038/nmicrobiol.2016.160
- Rubin, Benjamin E. R.; Gibbons, Sean M.; Kennedy, Suzanne; Hampton-Marcell, Jarrad; Owens, Sarah; Gilbert, Jack A. (2013). Investigating the impact of storage conditions on microbial community composition in soil samples. PLOS ONE 8(7): e70460. https://doi.org/10.1371/journal.pone.0070460
- Salonen, A.; Salojarvi, J.; Lahti, L.; de Vos, W. M. (2012). The adult intestinal core microbiota is determined by analysis depth and health status. Clinical Microbiology and Infection 18(Suppl 4): 16-20. https://doi.org/10.1111/j.1469-0691.2012.03855.x
- Salter, Susannah J.; Cox, Michael J.; Turek, Elena M.; Calus, Szymon T.; Cookson, William O.; Moffatt, Miriam F.; Turner, Paul; Parkhill, Julian; Loman, Nicholas J.; Walker, Alan W. (2014). Reagent and laboratory contamination can critically impact sequence-based microbiome analyses. BMC Biology 12: 87. https://doi.org/10.1186/s12915-014-0087-z
- Sanders, Howard L. (1968). Marine benthic diversity: a comparative study. The American Naturalist 102(925): 243-282. https://doi.org/10.1086/282541
- Schirmer, Melanie; Ijaz, Umer Z.; D'Amore, Rosalinda; Hall, Neil; Sloan, William T.; Quince, Christopher (2015). Insight into biases and sequencing errors for amplicon sequencing with the Illumina MiSeq platform. Nucleic Acids Research 43(6): e37. https://doi.org/10.1093/nar/gku1341
- Schloss, Patrick D. (2021). Amplicon sequence variants artificially split bacterial genomes into separate clusters. mSphere 6(4): e00191-21. https://doi.org/10.1128/mSphere.00191-21
- Schloss, Patrick D. (2024). Rarefaction is currently the best approach to control for uneven sequencing effort in amplicon sequence analyses. mSphere 9(2): e00354-23. https://doi.org/10.1128/msphere.00354-23
- Schloss, Patrick D. (2024). Waste not, want not: revisiting the analysis that called into question the practice of rarefaction. mSphere 9(1): e00355-23. https://doi.org/10.1128/msphere.00355-23
- Schmidt Laboratory, University of Michigan (2025). rrnDB release files v3.1.227, v4.4.3, v5.0, v5.6 and v5.10 (v5.10 dated 6 June 2025), and About page. https://rrndb.umms.med.umich.edu/static/download/
- Schnell, Ida Brholm; Bohmann, Kristine; Gilbert, M. Thomas P. (2015). Tag jumps illuminated: reducing sequence-to-sample misidentifications in metabarcoding studies. Molecular Ecology Resources 15(6): 1289-1303. https://doi.org/10.1111/1755-0998.12402
- Shade, Ashley; Handelsman, Jo (2012). Beyond the Venn diagram: the hunt for a core microbiome. Environmental Microbiology 14(1): 4-12. https://doi.org/10.1111/j.1462-2920.2011.02585.x
- Shade, Ashley; Jones, Stuart E.; Caporaso, J. Gregory; Handelsman, Jo; Knight, Rob; Fierer, Noah; Gilbert, Jack A. (2014). Conditionally rare taxa disproportionately contribute to temporal changes in microbial diversity. mBio 5(4): e01371-14. https://doi.org/10.1128/mBio.01371-14
- Shade, Ashley; Stopnisek, Nejc (2019). Abundance-occupancy distributions to prioritize plant core microbiome membership. Current Opinion in Microbiology 49: 50-58. https://doi.org/10.1016/j.mib.2019.09.008
- Shelton, Andrew Olaf; Gold, Zachary J.; Jensen, Alexander J.; D'Agnese, Erin; Andruszkiewicz Allan, Elizabeth; Van Cise, Amy; Gallego, Ramon; Ramon-Laca, Ana; Garber-Yonts, Maya; Parsons, Kim; Kelly, Ryan P. (2023). Toward quantitative metabarcoding. Ecology 104(2): e3906. https://doi.org/10.1002/ecy.3906
- Shoemaker, William R.; Locey, Kenneth J.; Lennon, Jay T. (2017). A macroecological theory of microbial biodiversity. Nature Ecology & Evolution 1(5): 0107. https://doi.org/10.1038/s41559-017-0107
- Silverman, Justin D.; Bloom, Rachael J.; Jiang, Sharon; Durand, Heather K.; Dallow, Eric; Mukherjee, Sayan; David, Lawrence A. (2021). Measuring and mitigating PCR bias in microbiota datasets. PLOS Computational Biology 17(7): e1009113. https://doi.org/10.1371/journal.pcbi.1009113
- Silverman, Justin D.; Durand, Heather K.; Bloom, Rachael J.; Mukherjee, Sayan; David, Lawrence A. (2018). Dynamic linear models guide design and analysis of microbiota studies within artificial human guts. Microbiome 6: 202. https://doi.org/10.1186/s40168-018-0584-3
- Silverman, Justin D.; Roche, Kimberly; Mukherjee, Sayan; David, Lawrence A. (2020). Naught all zeros in sequence count data are the same. Computational and Structural Biotechnology Journal 18: 2789-2798. https://doi.org/10.1016/j.csbj.2020.09.014
- Simberloff (1972).
- Sinha, Rahul; Stanley, Geoff; Gulati, Gunsagar S.; Ezran, Camille; Travaglini, Kyle J.; Wei, Eric; Chan, Charles K. F.; Nabhan, Ahmad N.; Su, Tianying; Morganti, Rachel M.; Conley, Stephanie D.; Chaib, Hassan; Red-Horse, Kristy; Longaker, Michael T.; Snyder, Michael P.; Krasnow, Mark A.; Weissman, Irving L. (2017). Index switching causes 'spreading-of-signal' among multiplexed samples in Illumina HiSeq 4000 DNA sequencing. bioRxiv (125724). https://doi.org/10.1101/125724
- Sipos, Rita; Szekely, Anna J.; Palatinszky, Marton; Revesz, Sara; Marialigeti, Karoly; Nikolausz, Marcell (2007). Effect of primer mismatch, annealing temperature and PCR cycle number on 16S rRNA gene-targetting bacterial community analysis. FEMS Microbiology Ecology 60(2): 341-350. https://doi.org/10.1111/j.1574-6941.2007.00283.x
- Sloan, William T.; Lunn, Mary; Woodcock, Stephen; Head, Ian M.; Nee, Sean; Curtis, Thomas P. (2006). Quantifying the roles of immigration and chance in shaping prokaryote community structure. Environmental Microbiology 8(4): 732-740. https://doi.org/10.1111/j.1462-2920.2005.00956.x
- Smets, Wenke; Leff, Jonathan W.; Bradford, Mark A.; McCulley, Rebecca L.; Lebeer, Sarah; Fierer, Noah (2016). A method for simultaneous measurement of soil bacterial abundances and community composition via 16S rRNA gene sequencing. Soil Biology and Biochemistry 96: 145-151. https://doi.org/10.1016/j.soilbio.2016.02.003
- Smith, Dylan P.; Peay, Kabir G. (2014). Sequence depth, not PCR replication, improves ecological inference from next generation DNA sequencing. PLOS ONE 9(2): e90234. https://doi.org/10.1371/journal.pone.0090234
- Sogin, Mitchell L.; Morrison, Hilary G.; Huber, Julie A.; Welch, David Mark; Huse, Susan M.; Neal, Phillip R.; Arrieta, Jesus M.; Herndl, Gerhard J. (2006). Microbial diversity in the deep sea and the underexplored "rare biosphere". PNAS 103(32): 12115-12120. https://doi.org/10.1073/pnas.0605127103
- Song, Se Jin; Amir, Amnon; Metcalf, Jessica L.; Amato, Katherine R.; Xu, Zhenjiang Zech; Humphrey, Greg; Knight, Rob (2016). Preservation methods differ in fecal microbiome stability, affecting suitability for field studies. mSystems 1(3): e00021-16. https://doi.org/10.1128/mSystems.00021-16
- Soppa, Jorg (2017). Polyploidy and community structure. Nature Microbiology 2: 16261. https://doi.org/10.1038/nmicrobiol.2016.261
- Stammler, Frank; Glasner, Joachim; Hiergeist, Andreas; Holler, Ernst; Weber, Daniela; Oefner, Peter J.; Gessner, Andre; Spang, Rainer (2016). Adjusting microbiome profiles for differences in microbial load by spike-in bacteria. Microbiome 4: 28. https://doi.org/10.1186/s40168-016-0175-0
- Starke, Robert; Pylro, Victor Satler; Morais, Daniel Kumazawa (2021). 16S rRNA gene copy number normalization does not provide more reliable conclusions in metataxonomic surveys. Microbial Ecology 81(2): 535-539. https://doi.org/10.1007/s00248-020-01586-7
- Stoddard, Steven F.; Smith, Byron J.; Hein, Robert; Roller, Benjamin R. K.; Schmidt, Thomas M. (2015). rrnDB: improved tools for interpreting rRNA gene abundance in bacteria and archaea and a new foundation for future development. Nucleic Acids Research 43(D1): D593-D598. https://doi.org/10.1093/nar/gku1201
- Stopnisek, Nejc; Shade, Ashley (2021). Persistent microbiome members in the common bean rhizosphere: an integrated analysis of space, time, and plant genotype. The ISME Journal 15(9): 2708-2722. https://doi.org/10.1038/s41396-021-00955-5
- Straub, Daniel; Blackwell, Nia; Langarica-Fuentes, Adrian; Peltzer, Alexander; Nahnsen, Sven; Kleindienst, Sara (2020). Interpretations of environmental microbial community studies are biased by the selected 16S rRNA (gene) amplicon sequencing pipeline. Frontiers in Microbiology 11: 550420. https://doi.org/10.3389/fmicb.2020.550420
- Sun, Dong-Lei; Jiang, Xuan; Wu, Qinglong L.; Zhou, Ning-Yi (2013). Intragenomic heterogeneity of 16S rRNA genes causes overestimation of prokaryotic diversity. Applied and Environmental Microbiology 79(19): 5962-5969. https://doi.org/10.1128/AEM.01282-13
- Suzuki, Marcelino T.; Giovannoni, Stephen J. (1996). Bias caused by template annealing in the amplification of mixtures of 16S rRNA genes by PCR. Applied and Environmental Microbiology 62(2): 625-630. https://doi.org/10.1128/aem.62.2.625-630.1996
- Sze, Marc A.; Schloss, Patrick D. (2019). The impact of DNA polymerase and number of rounds of amplification in PCR on 16S rRNA gene sequence data. mSphere 4(3): e00163-19. https://doi.org/10.1128/mSphere.00163-19
- The Microbiome Quality Control Project Consortium; Sinha, Rashmi; Abu-Ali, Galeb; Vogtmann, Emily; Fodor, Anthony A.; Ren, Boyu; Amir, Amnon; Schwager, Emma; Crabtree, Jonathan; Ma, Siyuan; Abnet, Christian C.; Knight, Rob; White, Owen; Huttenhower, Curtis (2017). Assessment of variation in microbial community amplicon sequencing by the Microbiome Quality Control (MBQC) project consortium. Nature Biotechnology 35(11): 1077-1086. https://doi.org/10.1038/nbt.3981
- Thompson, Luke R.; Sanders, Jon G.; McDonald, Daniel; Amir, Amnon; Ladau, Joshua; Locey, Kenneth J.; Prill, Robert J.; Tripathi, Anupriya; Gibbons, Sean M.; Ackermann, Gail; Navas-Molina, Jose A.; Janssen, Stefan; Kopylova, Evguenia; Vazquez-Baeza, Yoshiki; Gonzalez, Antonio; Morton, James T.; Mirarab, Siavash; Xu, Zhenjiang Zech; Jiang, Lingjing; Haroon, Mohamed F.; Kanbar, Jad; Zhu, Qiyun; Song, Se Jin; Kosciolek, Tomasz; Bokulich, Nicholas A.; Lefler, Joshua; Brislawn, Colin J.; Humphrey, Gregory; Owens, Sarah M.; Hampton-Marcell, Jarrad; Berg-Lyons, Donna; McKenzie, Valerie; Fierer, Noah; Fuhrman, Jed A.; Clauset, Aaron; Stevens, Rick L.; Shade, Ashley; Pollard, Katherine S.; Goodwin, Kelly D.; Jansson, Janet K.; Gilbert, Jack A.; Knight, Rob; The Earth Microbiome Project Consortium (consortium members as listed in the Crossref record) (2017). A communal catalogue reveals Earth's multiscale microbial diversity. Nature 551(7681): 457-463. https://doi.org/10.1038/nature24621
- Thorsen, Jonathan; Brejnrod, Asker; Mortensen, Martin; Rasmussen, Morten A.; Stokholm, Jakob; Abu Al-Soud, Waleed; Srensen, Sren; Bisgaard, Hans; Waage, Johannes (2016). Large-scale benchmarking reveals false discoveries and count transformation sensitivity in 16S rRNA gene amplicon data analysis methods used in microbiome studies. Microbiome 4: 62. https://doi.org/10.1186/s40168-016-0208-8
- Tkacz, Andrzej; Hortala, Marion; Poole, Philip S. (2018). Absolute quantitation of microbiota abundance in environmental samples. Microbiome 6: 110. https://doi.org/10.1186/s40168-018-0491-7
- Tourlousse, Dieter M.; Yoshiike, Satowa; Ohashi, Akiko; Matsukura, Satoko; Noda, Naohiro; Sekiguchi, Yuji (2017). Synthetic spike-in standards for high-throughput 16S rRNA gene amplicon sequencing. Nucleic Acids Research 45(4): e23. https://doi.org/10.1093/nar/gkw984
- Vaginal Microbiome Consortium; Brooks, J. Paul; Edwards, David J.; Harwich, Michael D. Jr; Rivera, Maria C.; Fettweis, Jennifer M.; Serrano, Myrna G.; Reris, Robert A.; Sheth, Nihar U.; Huang, Bernice; Girerd, Philippe; Strauss, Jerome F. 3rd; Jefferson, Kimberly K.; Buck, Gregory A. (2015). The truth about metagenomics: quantifying and counteracting bias in 16S rRNA studies. BMC Microbiology 15: 66. https://doi.org/10.1186/s12866-015-0351-6
- Vandeputte, Doris; Kathagen, Gunter; D'hoe, Kevin; Vieira-Silva, Sara; Valles-Colomer, Mireia; Sabino, Joao; Wang, Jun; Tito, Raul Y.; De Commer, Lindsey; Darzi, Youssef; Vermeire, Severine; Falony, Gwen; Raes, Jeroen (2017). Quantitative microbiome profiling links gut community variation to microbial load. Nature 551(7681): 507-511. https://doi.org/10.1038/nature24460
- Vaulot, Daniel; Marie, Dominique; Olson, Robert J.; Chisholm, Sallie W. (1995). Growth of Prochlorococcus, a photosynthetic prokaryote, in the equatorial Pacific Ocean. Science 268(5216): 1480-1482. https://doi.org/10.1126/science.268.5216.1480
- Vetrovsky, Tomas; Baldrian, Petr (2013). The variability of the 16S rRNA gene in bacterial genomes and its consequences for bacterial community analyses. PLOS ONE 8(2): e57923. https://doi.org/10.1371/journal.pone.0057923
- Walters, William A.; Jin, Zhao; Youngblut, Nicholas; Wallace, Jason G.; Sutter, Jessica; Zhang, Wei; Gonzalez-Pena, Antonio; Peiffer, Jason; Koren, Omry; Shi, Qiaojuan; Knight, Rob; del Rio, Tijana Glavina; Tringe, Susannah G.; Buckler, Edward S.; Dangl, Jeffery L.; Ley, Ruth E. (2018). Large-scale replicated field study of maize rhizosphere identifies heritable microbes. PNAS 115(28): 7368-7373. https://doi.org/10.1073/pnas.1800918115
- Walters, William; Hyde, Embriette R.; Berg-Lyons, Donna; Ackermann, Gail; Humphrey, Greg; Parada, Alma; Gilbert, Jack A.; Jansson, Janet K.; Caporaso, J. Gregory; Fuhrman, Jed A.; Apprill, Amy; Knight, Rob (2016). Improved bacterial 16S rRNA gene (V4 and V4-5) and fungal internal transcribed spacer marker gene primers for microbial community surveys. mSystems 1(1): e00009-15. https://doi.org/10.1128/mSystems.00009-15
- Weiss, Sophie; Xu, Zhenjiang Zech; Peddada, Shyamal; Amir, Amnon; Bittinger, Kyle; Gonzalez, Antonio; Lozupone, Catherine; Zaneveld, Jesse R.; Vazquez-Baeza, Yoshiki; Birmingham, Amanda; Hyde, Embriette R.; Knight, Rob (2017). Normalization and microbial differential abundance strategies depend upon data characteristics. Microbiome 5: 27. https://doi.org/10.1186/s40168-017-0237-y
- Wen, Chongqing; Wu, Liyou; Qin, Yujia; Van Nostrand, Joy D.; Ning, Daliang; Sun, Bo; Xue, Kai; Liu, Feifei; Deng, Ye; Liang, Yuting; Zhou, Jizhong (2017). Evaluation of the reproducibility of amplicon sequencing with Illumina MiSeq platform. PLOS ONE 12(4): e0176716. https://doi.org/10.1371/journal.pone.0176716
- Willis, Amy D. (2019). Rarefaction, alpha diversity, and statistics. Frontiers in Microbiology 10: 2407. https://doi.org/10.3389/fmicb.2019.02407
- Willis, Amy D.; Martin, Bryan D. (2022). Estimating diversity in networked ecological communities. Biostatistics 23(1): 207-222. https://doi.org/10.1093/biostatistics/kxaa015
- Willis, Amy; Bunge, John (2015). Estimating diversity via frequency ratios. Biometrics 71(4): 1042-1049. https://doi.org/10.1111/biom.12332
- Willis, Amy; Bunge, John; Whitman, Thea (2017). Improved detection of changes in species richness in high diversity microbial communities. Journal of the Royal Statistical Society Series C: Applied Statistics 66(5): 963-977. https://doi.org/10.1111/rssc.12206
- Wirbel, Jakob; Essex, Morgan; Forslund, Sofia Kirke; Zeller, Georg (2024). A realistic benchmark for differential abundance testing and confounder adjustment in human microbiome studies. Genome Biology 25: 247. https://doi.org/10.1186/s13059-024-03390-9
- Wright, David H. (1991). Correlations between incidence and abundance are expected by chance. Journal of Biogeography 18(4): 463-466. https://doi.org/10.2307/2845487
- Wright, Erik Scott; Vetsigian, Kalin Horen (2016). Quality filtering of Illumina index reads mitigates sample cross-talk. BMC Genomics 17: 876. https://doi.org/10.1186/s12864-016-3217-x
- Yang, Lu; Chen, Jun (2022). A comprehensive evaluation of microbial differential abundance analysis methods: current status and potential solutions. Microbiome 10: 130. https://doi.org/10.1186/s40168-022-01320-0
- Yeh, Yi-Chun; Needham, David M.; Sieradzki, Ella T.; Fuhrman, Jed A. (2018). Taxon disappearance from microbiome analysis reinforces the value of mock communities as a standard in every sequencing run. mSystems 3(3): e00023-18. https://doi.org/10.1128/mSystems.00023-18
- Zemb, Olivier; Achard, Caroline S.; Hamelin, Jerome; De Almeida, Marie-Lea; Gabinaud, Beatrice; Cauquil, Laurent; Verschuren, Lisanne M. G.; Godon, Jean-Jacques (2020). Absolute quantitation of microbes using 16S rRNA gene metabarcoding: a rapid normalization of relative abundances by quantitative PCR targeting a 16S rRNA gene spike-in standard. MicrobiologyOpen 9(3): e977. https://doi.org/10.1002/mbo3.977
- Zeng, Quanchao; An, Shaoshan (2021). Identifying the biogeographic patterns of rare and abundant bacterial communities using different primer sets on the Loess Plateau. Microorganisms 9(1): 139. https://doi.org/10.3390/microorganisms9010139
- Zerulla, Karolin; Ludt, Katharina; Soppa, Jorg (2016). The ploidy level of Synechocystis sp. PCC 6803 is highly variable and is influenced by growth phase and by chemical and physical external parameters. Microbiology 162(5): 730-739. https://doi.org/10.1099/mic.0.000264
- Zerulla, Karolin; Soppa, Jorg (2014). Polyploidy in haloarchaea: advantages for growth and survival. Frontiers in Microbiology 5: 274. https://doi.org/10.3389/fmicb.2014.00274
- Zhou, Jizhong; Jiang, Yi-Huei; Deng, Ye; Shi, Zhou; Zhou, Benjamin Yamin; Xue, Kai; Wu, Liyou; He, Zhili; Yang, Yunfeng (2013). Random sampling process leads to overestimation of beta-diversity of microbial communities. mBio 4(3): e00324-13. https://doi.org/10.1128/mBio.00324-13
- Zhou, Jizhong; Wu, Liyou; Deng, Ye; Zhi, Xiaoyang; Jiang, Yi-Huei; Tu, Qichao; Xie, Jianping; Van Nostrand, Joy D.; He, Zhili; Yang, Yunfeng (2011). Reproducibility and quantitation of amplicon sequencing-based detection. The ISME Journal 5(8): 1303-1313. https://doi.org/10.1038/ismej.2011.11
