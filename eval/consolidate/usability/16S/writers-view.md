# 16S amplicon sequencing from sample to count table: writer's view

> [!abstract] About this view
> What the research found, for writing from. It is generated from the knowledge note `16S amplicon sequencing from sample to count table.md`, which stays the audit version: every claim here is checked there against the research, with its setting, sources and trail. Standing is given in brackets where the research stated one (`repl` replicated, `single` one source, `cont` contested, `unclear`, `mixed` the inputs differ); a claim with no bracket has no standing stated. "Limited by access" means the research says a source was not read in full, not that the evidence is weak.

## What the research found, by question

### MB-01

**D1. What are the steps between a sample and a table of taxon counts, and which choices are made at each? Answer for each step separately: field sampling, preservation and storage; DNA extraction; choice of primers and gene region; PCR conditions, including cycle number; library preparation and sample indexing; sequencing platform and read length; demultiplexing; quality filtering and read merging; error correction or clustering into sequence variants or operational taxonomic units; chimera detection; taxonomic assignment, including classifiers and reference databases; contaminant and negative control handling.**

*Answer to D1, as the critic reformulated it.* **D1: steps and choices**

The body supports the twelve-step description and the alternatives listed for each step. Most of it comes from full-text protocols, documentation and benchmarks; makers' statements are labelled as such. Two corrections. (1) The control-usage figure comes from Hornung 2019, which surveyed 265 papers in the 2018 issues of Microbiome and The ISME Journal that used any high-throughput community sequencing (16S, shotgun, metatranscriptomics, ITS, 18S and others): 30% (79) reported a negative control and 10% (27) a positive control. It is not a 16S-only figure, and it is SINGLE SOURCE. (2) The review contradicts itself about field sampling for water (volume, filter pore size) and host tissue. Section 2.1 says the lab angle searched these through Crossref, Europe PMC and web search; the Search record says no angle searched them. On the review's own record, these choices are unsearched, not 'not found'. How often each choice is made across the field is unmeasured apart from controls.

**D2. At each step in D1, how closely do counts track the sampled community, and what, if anything, departs them from it (for example extraction efficiency, primer mismatch, amplification efficiency, reannealing, 16S rRNA gene copy number, chimeras, index misassignment, sequencing error, clustering or denoising choices, classification error, contamination), by what mechanism and by how much? Report effects on relative abundance and on the number of taxa detected separately, and say for each source whether its effect has been measured as consistent across samples or as varying between them.**

*Answer to D2, as the critic reformulated it.* **D2: departures per step, size and consistency**

Every mock-community study in the body found observed composition departing from known composition (replicated; full text). Departures are measured at most steps, but not at all of them. Field sampling for water and host tissue was not searched. Several choices showed little or no detectable effect: PCR replicate pooling, preparation day and lane, cycle number in some studies, and storage in one soil. For number of taxa detected, inflation by spurious sequences, chimeras, reagent contamination and pipeline choice is replicated across independent mocks and dilution series: 10 to 200-fold excess units (Straub 2020), contaminants rising from 0.1% to 80.1% of reads in a diluted mock (Karstens 2019). For relative abundance, the claim that extraction is the largest step, followed by PCR and then sequencing, rests on one 7-taxon vaginal dataset (Brooks 2015, reanalysed by McLaren 2019). It is contested by Fouhy 2016 (two extraction methods gave very similar data) and qualified by MBQC (specimen type mattered more than extraction). It should be presented as SINGLE DATASET, not as a field-wide ordering. Per-step magnitudes mostly come from one or two small mocks (7 to 20 taxa), often on 454. Consistency across samples: ratio-scale consistency is shown in one 16S cell-mixture dataset and one shotgun spike-in known only secondarily (Costea 2017 via McLaren). Variation between sample types or samples is shown by a field-versus-mock SAR11 bias for the 515F-Y/806R pair (Parada 2016, abstract only), inconsistent cycle effects in four stool samples (Sze and Schloss 2019), extraction yield of 40 to 84% (Zemb 2020) and a 66.7-fold spike-in range (Zhou 2011, abstract). Correction: McLaren's calibration result (Bray-Curtis error from 0.35 to 0.08, 92.6% lower mean squared error) comes from the Brooks 16S cell mixtures, not from a shotgun dataset. Overall: strong qualitatively; moderate for the inflation of taxon counts; weak for per-step relative-abundance magnitudes and for consistency across samples.

**D3. What values of the quantities in this workflow have been measured or reported: PCR cycle numbers and per-cycle amplification efficiencies; the distribution of 16S rRNA gene copy numbers across bacteria and archaea, and in communities from soil, water and hosts, each separately; reads per sample on commonly used platforms, and how much read numbers vary between samples within one sequencing run; the shape of taxon abundance distributions in communities from soil, water and hosts, each separately?**

*Answer to D3, as the critic reformulated it.* **D3: measured values**

The body supports the values given: documented cycle numbers (the EMP protocol's 35 cycles in triplicate and 240 ng pooling were checked on the live page), copy-number ranges across genomes, per-study and per-run read ranges, and microbial-load ranges. Caveats. (1) Environment-level copy numbers (ACN about 2.2 for free-living and plant-associated samples, about 3.4 for animal-associated, soil lowest) are predictions from one source (Thompson 2017); the review flags this. (2) Abundance-distribution shapes split by environment are weaker than presented. The soil 'exponential or inverse gamma' best fits are in Zhou 2013's supplementary Table S3; the main text does not state them and they were not verified. The 'water and hosts' item is a single study (Kembel 2012) that pools ocean and skin into one item; the same paper's simulations assumed a lognormal. Haegeman 2013's Brazil-soil figures rest on a full text that was not openly retrievable. Absent: measured community copy number, a within-run read-count coefficient of variation, absolute per-cycle efficiencies, and per-environment abundance-distribution shapes for water and for host samples.

**D4. Which processes generate the read count of each taxon in a sample, and how well do models describe them? Cover sampling from the pool of amplified molecules (multinomial, Dirichlet multinomial and other overdispersed models) and processes other than sampling (stochastic early amplification, run and batch effects, non-random dropout), each separately, and report what technical replicates at different read depths show about the variability of relative abundances and of the number of taxa detected.**

*Answer to D4, as the critic reformulated it.* **D4: count-generating processes and replicate variability**

The evidence that Poisson or multinomial sampling explains replicate disagreement in taxa detected comes from one dataset. Zhou 2013 modelled the same 24 Oklahoma grassland soils, sequenced on 454, that Zhou 2011 reported. Wen 2017 is from the same laboratory. Wen 2017's MiSeq replicates cut against pure sampling. Zhou 2013 predicted about 60,900 reads for 90% OTU overlap, but in Wen 2017 unweighted overlap plateaued at 39% near 30,000 reads (with singletons) and reached only 43.9% at 160,000 reads. Wen's authors attribute rare-OTU variation to random sampling plus sequencing artefacts, report that 'biases other than random sampling' affect unweighted metrics more, and found lower overlap when replicates were sequenced in separate runs (a run effect). So: weak and contested that sampling alone explains replicate disagreement in taxa detected. The square-root decline of the CV of relative abundance with depth comes from one caecal extract (Barlow 2020, SINGLE SOURCE). Technical variance beyond counting (76% of variation at hourly sampling in artificial guts, Silverman 2018), early stochastic amplification at low load (Dyrhovden 2021) and whole-run taxon loss (Yeh 2018) are each single studies. Dirichlet-multinomial overdispersion has been shown only between biological samples, not among technical replicates. Water and non-gut host replicate-at-depth data are absent.

**D5. How do approaches to comparing samples with unequal read numbers or total loads compare, in either direction: absolute quantification of total load (qPCR, flow cytometry, spike-ins); coverage-based standardisation; compositional (log-ratio) approaches; proportions; rarefaction curves; rarefying to a common depth; richness estimators and extrapolation; scaling and normalisation methods? Answer separately for richness and other alpha diversity measures, for between-sample (beta) diversity, and for tests of which taxa differ in abundance, and for each approach say what it has been shown to correct and what it has not.**

*Answer to D5, as the critic reformulated it.* **D5: comparing samples with unequal depth or load**

The body supports 'contested' for rarefying, proportions and differential-abundance methods. It supports that absolute quantification changes conclusions but does not remove taxon-specific bias. Corrections. (1) Willis 2019 is labelled 'asserted', but it presents statistical argument plus a worked simulated example. Calling it an assertion against Schloss's 'modelled' simulations understates the evidence against rarefying for richness. (2) Galazzo 2020: the r = -0.50 correlation on faeces is between qPCR and flow cytometry, not ddPCR and flow. ddPCR correlated strongly with qPCR, and the authors used this to rule out qPCR imprecision as the cause of the divergence. (3) Lin 2019: the authors conclude that the internal-standard method is quantitative and consistent with flow cytometry. The review reports only r2 = 0.19 before correction and does not give the authors' conclusion (Common rule 6). That figure could not be verified here. Coverage-based standardisation has one microbial test (the Schloss 2024b null model, verified: all approaches 'except for rarefaction and possibly the size-based iNEXT estimates' remained depth-correlated). Beyond that, the evidence is non-microbial. Benchmarks that build taxon-specific bias and load differences into the simulated truth together are absent, apart from Llorens-Rico 2021, which simulated faeces without taxon bias.

### MB-02

**D1. How many copies of the 16S rRNA gene do bacterial and archaeal genomes carry: the range, the distribution, and how it varies across taxa, according to current and earlier database releases and genome studies? Give 16S gene counts and ribosomal operon counts as each source reports them. Separately, how many 16S gene copies does a cell carry, given its number of genome copies: what measurements of genome copies per cell exist, in cultures and in environmental samples, including the share of cells at one genome copy and at more than one, in fast-growing, slow-growing and dormant states? What do studies relating 16S copy number to read-based abundance report, including copy-number prediction and correction methods, their measured accuracy, and whether correction changes ecological conclusions?**

*Answer to D1 (a), as the critic reformulated it.* **D1 (a) 16S copies per genome**

Mostly supported as written, with three corrections. (1) The archaeal ceiling is not 4 until v5.0: Acinas et al. 2004 already report a maximum of five archaeal operons, so the review's own sources conflict on the archaeal maximum, and the review does not flag this. (2) The 'Acidobacteria 1.0' mean from Vetrovsky and Baldrian rests on 4 genomes from 4 species (their Table 1). The rrnDB v5.10 figure of 1.4 rests on 29 species. These soil-relevant low values are imprecise, and the soil correction example (Acidobacteria 50.1% to 66.0%) depends on them. (3) The 1 to 15 range is consistent across sources, but those sources draw on overlapping NCBI genome sets, so they are not independent replications. The current maxima of 21 to 22 and the current shares remain the reviewer's own derivation from rrnDB, with no published check against assembly quality.

*Answer to D1 (b), as the critic reformulated it.* **D1 (b) genome and 16S copies per cell**

In cultures, genome copies per cell range from about one (Caulobacter, Wolinella, crenarchaea) to tens or hundreds (P. putida, haloarchaea, methanogens, Synechocystis), and depend on growth rate and phase. Copy number does not change in one direction with growth phase. Most Soppa-group species fall in stationary phase or starvation. The soil diazotroph Azotobacter vinelandii, however, is reported to rise from about 4 copies in exponential phase to about 80 in stationary phase (SECONDARY, via Bruck et al. 2023 full text). Pecoraro et al. 2011 Table 5 gives A. vinelandii as 1 (up to 8) copies in slow growth and 40 in fast growth, attributed to another laboratory. Several non-Soppa measurements exist: Azotobacter, Desulfovibrio, Neisseria and Deinococcus, all listed in Pecoraro 2011. Evidence is moderate, not strong: apart from Pecoraro 2011 it rests largely on abstracts and on one laboratory's qPCR method. The claim that 16S copies per cell scale with origin number is the reviewer's inference from an abstract; no source in the review measures it. In natural communities, evidence is indirect and sparse (soil DNA mass per cell, seawater DNA-content populations, groundwater iRep). Flow cytometric cell-cycle analyses of Prochlorococcus in situ are by method taxon-specific measurements of the share of cells with replicated DNA. The review read only the abstract, so its statement that no such share exists for any natural community is not established. Nothing comparable was found for soil.

*Answer to D1 (c), as the critic reformulated it.* **D1 (c) copy number versus reads; correction**

Supported, with corrections. Prediction accuracy declines with distance to sequenced genomes, and correction improves fit to simulated truth. In Starke et al. 2021, uncorrected data fitted 7.1% better on n = 10 mocks (one of the eleven was excluded); all were DNA-based or cloned-gene mocks. Correction changes the identity of the dominant OTU in about 20 to 31% of HMP and EMP communities, but against predicted, not measured, truth. It barely changes PERMANOVA in simulations. The statement that extraction and primer biases are 'of similar or larger size' than copy-number bias is not supported by the McLaren abstract. No soil benchmark was found. The soil literature on community-weighted rrn copy number (for example succession and rhizosphere-versus-bulk comparisons) was not searched.

**D2. How do microbial ecologists define and use terms for the abundance and distribution of taxa, such as abundant, rare, dominant, common, prevalent and core, and related terms? Report separately definitions based on relative abundance within one sample, on occupancy or prevalence across samples or sites, and on regional or global distribution; the thresholds used (for example relative abundance cutoffs) and whether classifications and conclusions hold or change across thresholds; frameworks from general ecology that classify kinds of rarity; proposed standard definitions; and how usage compares across studies.**

*Answer to D2, as the critic reformulated it.* **D2 definitions and thresholds**

Supported in substance. Three families of definition are in use: within-sample thresholds (0.1% most common for rare), occupancy (core, mostly occurrence-only) and pooled or global classes. Usage is heterogeneous and often unstated (two surveys). Three corrections. (1) Jia et al. 2022 uses a single rare/common cutoff and does not support 'abundant above 1%'. (2) Custer et al. 2023 report that 165 to 176 taxa were agreed by all four methods, which is 13 to 16% of core assignments. The review's 'about 1% of taxa' is its own derivation and should be labelled as such. (3) Custer's text is internally inconsistent on whether core analyses gained or lost the temporal effect. Tests of threshold sensitivity point both ways and are each single-system. The single soil test (Jia 2022) found that classifications shift with the cutoff and that the relative importance of selection rose as the cutoff tightened, while the qualitative assembly conclusion held. Occupancy-based terms from general and microbial ecology (generalist/specialist by niche breadth, cosmopolitan/endemic, core/satellite) are under-covered.

**D3. In soil bacterial and archaeal communities, how is abundance distributed among taxa, and how does a taxon's local abundance relate to its occupancy across soils? Report figures from cell counts, amplicon reads and metagenomes separately, and how sampling effort, sequencing depth and detection affect the observed distributions and relationships, including null model analyses.**

*Answer to D3 (a), as the critic reformulated it.* **D3 (a) soil abundance distributions by measurement**

Amplicon reads, bulk soil: in the global datasets found, a small minority of taxa carries a large share of reads. The two figures must be kept apart. In Delgado-Baquerizo et al. 2018, 2% of phylotypes, defined jointly by abundance and ubiquity, accounted on average for 41% of reads per sample. In Bickel and Or 2021, 0.4% of ASVs, classed common on the globally pooled rank-abundance distribution, held about 58% of pooled relative abundance. The review's answer pools these into '0.4 to 2% hold 41 to 58%', contradicting its own body. Two phylotypes made up more than 70% of archaeal sequences across 146 soils (one study, abstract only). The functional form (lognormal versus power law) is contested, and most of that evidence is abstract-only or modelled. No soil taxon abundance distributions were found from cell counts or from metagenome coverage. The search did not cover genome-resolved global soil metagenomes (for example Bahram et al. 2018) or CARD-FISH phylum-level cell shares in soil.

*Answer to D3 (b), as the critic reformulated it.* **D3 (b) abundance-occupancy in soil**

In the two bulk-soil amplicon studies with figures, more abundant taxa occupy more soils. These are not fully independent: Bickel and Or reanalysed compiled datasets including the Earth Microbiome Project, which plausibly overlaps the soils Nemergut used. Both measures are partly built in by construction. 'Total abundance' summed across samples, and 'common' defined on the pooled rank-abundance distribution, both rise with occupancy, the same circularity the review flags only for Delgado-Baquerizo 2018. Detection limits and neutral or sampling models predict a positive relationship without selection. No soil test against a sampling null was found. So whether a relationship exists beyond sampling, and how strong it is, is unresolved; 'wherever tested' overstates a search that reviewed about 25 titles. Rhizosphere evidence covers core membership in bean and maize, with 13.7% of bean bacterial and archaeal taxa deviating from a neutral curve. No rhizosphere correlation coefficients were found.

## Concepts

In an order where each concept comes after the ones it builds on; the order means nothing more.

### the steps from sample to count table and the choices at each

- Twelve steps between a sample and a table of taxon counts are documented, each with named alternatives; what the steps are is not in conflict, while the recommended choice within a step is disputed.
- How often each choice is made across the field is unmeasured, apart from the use of controls.

### field sampling, preservation, storage and sample mass

Builds on: the steps from sample to count table and the choices at each.

- Studies vary the preservative (none, 70% or 95% ethanol, FTA cards, OMNIgene Gut, freezing or refrigeration), the temperature and the duration of storage.
- Human and dog faeces held at ambient temperature for 8 weeks changed by about as much as technical replicates differ when kept in 95% ethanol, on FTA cards or in OMNIgene Gut; unpreserved samples and 70% ethanol changed by amounts comparable to differences between individual humans. *(repl)*
- Storage altered taxon frequencies more than presence or absence: weighted UniFrac effects exceeded unweighted, and the number of taxa detected was affected less.
- FTA cards produced a systematic shift that could be detrended, the one storage effect shown to be consistent across samples; for the other preservation methods consistency was not measured.
- Storage of a single soil for 1 to 14 days at room temperature, 4 C or -20 C changed its community, most at 3 to 7 days and least when frozen; these changes were small relative to differences among more than 500 Earth Microbiome Project soils. *(repl)*
- In one agricultural field, extracting 0.25, 1, 5, 10 or 100 g of soil changed community structure, replicate dispersion and OTU counts; 10 g extractions gave the highest diversity and the lowest dispersion. *(single)*
- Field sampling choices for water (volume filtered, filter pore size) and for host tissue were not searched by any angle: they are unsearched, not "not found".

### DNA extraction

Builds on: the steps from sample to count table and the choices at each.

- Extraction choices include the kit, bead-beating intensity, plate or single tube, and whether relic DNA is removed with PMA or DNase.
- In McLaren's reanalysis of Brooks's 80 cell mixtures of 7 vaginal taxa (V1-V3, 454), the extraction step had a maximum pairwise bias of 36.6-fold and a mean of 5.5-fold, PCR a maximum of 5.2 and a mean of 2.3, and sequencing plus classification a maximum of 1.6 and a mean of 1.2; total bias in the cell mixtures was a maximum of 29.3-fold and a mean of 5.6-fold. *(single)*
- Total bias in the cell mixtures is smaller than extraction bias alone, which the note says implies partial cancellation between steps.
- In the same data, Brooks et al. reported median total bias per taxon from -32.6% to +39.1% of true proportion, error from bias above 85% in some samples while technical variation was under 5% for most taxa, and a change of about 50% in Enterococcus when extraction kits were swapped.
- In activated sludge, bead-beating intensity and primer choice had the largest effects of all parameters tested; harder bead beating increased DNA from Gram-positive bacteria by up to 400%. *(repl)*
- In a 20-species gut mock, two extraction methods (QIAamp stool kit versus repeat bead beating) gave "very similar" data; primer and platform mattered more. *(repl)*
- Taxa whose DNA was never extracted were missing: in the MBQC artificial communities the largest contributor to inaccuracy was contamination or omission of microbes whose DNA was not extracted.
- No more than 6% of inoculated lambda DNA was recovered from six soils. *(repl)*
- Extraction method changed soil fingerprint profiles. *(repl)*
- Extraction yield varied between samples: a synthetic spike-in quantified before and after extraction was recovered at 40% to 84%. *(single)*
- The consistency of extraction bias across real soil or water matrices has not been measured, and no mock study in a soil matrix with known composition was found; soil evidence comes from spike-ins, dilutions and relic DNA.

### relic (extracellular) DNA

Builds on: DNA extraction.

- Across soils, an average 40% of DNA was extracellular or from non-intact cells; removing it with propidium monoazide showed relic DNA inflated richness by up to 55%, more so at high pH and not at all in some soils, and misestimated relative abundances. *(cont)*
- Relic DNA averaged 33% (over 80% in some samples) across soil, sediment, water and mammalian gut but had minimal effect on diversity estimates; models predict bias only when relic and intact abundance distributions differ. *(cont)*
- Whether relic DNA distorts diversity estimates is contested: Carini 2016 against Lennon 2018. *(cont)*

### primers and gene region

Builds on: the steps from sample to count table and the choices at each.

- Primer and region choices include V1-V2 through V7-V9 and full length, degenerate variants of 515F and 806R, and PNA clamps against host plastids.
- In silico, 175 primers and 512 pairs differ widely in coverage and phylum spectrum against SILVA 108. *(repl)*
- In marine samples, primer bias under-represented SAR11 and over-represented Gammaproteobacteria; the SAR11 bias figures belong to the 515F-Y/806R pair, not the original 515F-C/806R V4 primers to which the review attributes them. *(repl)*
- For the 515F-Y/806R pair, SAR11 was under-represented about 4 to 10-fold in marine field samples but only about 2-fold in mocks, so mock-measured bias understated field bias for this taxon; this rests on one abstract, one primer pair and one taxon. *(single)*
- On marine clone mocks, 515F-Y/926R fit expected composition with r2 = 0.95, against about 0.5 for 515F-Y/806R, and even perfectly matched primers showed preferential amplification.
- Adding degeneracy to 515F and 806R improved detection of Thaumarchaeota (archaea) and SAR11 in stool, soil and built-environment sets without degrading other taxa. *(repl)*
- Whole phyla appeared or disappeared with primer choice: in human stool and mocks with seven primer pairs, Verrucomicrobia appeared only with V3-V4, V4, V6-V8 and V7-V9 primers. *(repl)*
- In a gut mock, 55 to 80% of expected species were detected, and 29 to 80% of detected species were misidentified or false hits, depending on primer, platform and extraction.
- Preferential amplification of a matched template over a mismatched one (63F) rose almost exponentially as annealing temperature went from 47 to 61 C; a perfectly matched primer showed no such effect. *(single)*
- With universal PNA clamps, host plastid reads averaged 23% across 32 plant species (plant roots) but reached 62 to 94% in some lineages. *(single)*
- A modified PNA clamp cut Asteraceae plastid contamination from 65% to 23% but raised it from 12% to 69% in other species, and PNA type did not detectably change bacterial alpha or beta diversity.
- The makers of PCR clamps state that clamps enrich microbial sequences "without introducing bias".
- In silico, 56% of V4 amplicons failed to match their species of origin with confidence, while full-length sequences classified nearly all correctly. *(single)*

### PCR conditions, cycle number and template amount

Builds on: primers and gene region.

- PCR choices include the polymerase, cycle number, input amount and single versus pooled replicate reactions.
- Two-template 27F-338R mixtures converged toward 1:1 products regardless of starting ratio; the bias depended strongly on cycle number and fit a kinetic model of product reannealing. *(repl)*
- Reproducible over-amplification of specific templates in genomic mixtures was explained largely by primer binding energy, not copy number, and was reduced by higher template concentration, fewer cycles and pooling of reactions. *(repl)*
- In a 20-strain mock, genomic GC content correlated negatively with observed abundance; longer initial denaturation raised the three highest-GC members but did not change overall evenness. *(single)*
- High-GC templates were also under-represented in Pinto and Raskin 2012.
- In a gut-isolate mock with primer mismatch removed by pre-amplification, log-ratios changed linearly with cycle number from 10 to 35 cycles; after 35 cycles relative abundances were biased by an average factor of 2.6 (95% credible set 2.3 to 2.9), and the B. longum to E. faecalis ratio shifted about 16-fold. *(single)*
- In four artificial-gut communities about 19% of taxa were more than 4-fold biased. *(single)*
- PCR bias was consistent per taxon in the mocks, and calibration corrected composition toward truth in all 10 held-out mocks; the authors note that their mock "ground truth" carried its own bias and that the method sometimes estimated the wrong direction for some taxa.
- Sze and Schloss tested five polymerases at 20 to 35 cycles: in the mock, error rate, chimera fraction and deviation from the expected profile all rose with cycle number; in stool, the sample explained R2 = 0.79 of variation, cycles 0.044 and polymerase 0.033, and "this bias was inconsistent for human stool samples". *(single)*
- Several studies found cycle number mattered little: template-to-product ratios were little affected by cycle number (Sipos 2007); clone libraries amplified for different numbers of cycles showed no detectable skew (Acinas 2005); 30 versus 35 cycles changed proportions only slightly (Brooks 2015). *(single)*
- The effect of cycle number is in conflict: small effects (Sipos 2007; Acinas 2005; Brooks 2015) against growing bias (Suzuki 1996; Silverman 2021; Sze and Schloss 2019 mock).
- Low template (0.1 ng versus 5 to 10 ng) increased profile variability in soil and faecal samples; pooling of PCRs, preparation day and lane did not. *(single)*
- Single versus triplicate pooled PCRs made no significant difference. *(repl)*
- In fungal ITS, pooling 1 to 16 PCR replicates had no detectable effect on alpha or beta diversity.
- Pooled versus single PCR is a disputed choice: Marotz 2019 and Smith and Peay 2014 against the triplicate pooling in the EMP protocol.

### PCR cycle numbers and per-cycle amplification efficiency

Builds on: PCR conditions, cycle number and template amount.

- Documented protocols use 35 cycles in triplicate 25 uL reactions, pooling 240 ng per sample (EMP protocol, one-step), or 25 amplicon cycles plus 8 index cycles with 12.5 ng input (Illumina guide, two-step).
- Experiments span 10 to 35 cycles (Silverman 2021), 15 or 20 to 35 (Sze and Schloss 2019), 20 versus 40 (Salter 2014) and 24 (Laursen 2017).
- Only relative per-cycle efficiencies have been measured: Silverman 2021 estimated taxon-specific log-ratio changes per cycle, which compound to an average 2.6-fold bias after 35 cycles in a gut mock. *(single)*
- Kelly 2019 drew efficiencies from beta distributions fitted to eukaryotic eDNA mocks and modelled amplicons as starting copies x (1 + a_i)^cycles.
- No absolute per-cycle efficiency for universal 16S primers on environmental templates was found.
- In eukaryotic eDNA work, the PCR process has been modelled, calibrated with mocks, to estimate starting proportions.

### 16S rRNA gene copies per genome

- Bacterial genomes carry 1 to about 15 copies of the 16S rRNA gene in every database release and genome survey to about 2015: the first rrnDB release ("can vary from one to as many as 15 copies"), the 2009 release (785 bacterial and 69 archaeal strains) and the 2015 release, Acinas 2004 and Vetrovsky and Baldrian 2013.
- The 2015 rrnDB release held 2,635 bacterial records (1,383 species) and 175 archaeal records (148 species): bacteria 1 to 15 copies, archaea 1 to 4. *(repl)*
- Copy-number distributions within a family can be bimodal (Enterobacteriaceae 1 to 9, with a low-copy peak made up of insect symbionts), and means over all genomes mislead because some species are over-represented.
- Among 301 species with at least two genome records in rrnDB (Stoddard 2015), 77% had identical copy counts, 16% differed by one copy and 3% by more than two.
- From version 5.0 onward, rrnDB counts 16S genes by BLAST against gap-free NCBI assemblies rather than from annotation, so its genome records report 16S gene counts only, not operons or 23S counts.
- In the reviewer's summary of the rrnDB release files, bacterial records and ranges were: v3.1.227, 1,297 records, 1 to 15, record mean 4.20 (median 3), 17.5% of records at one copy, mean of species means 3.87, archaea 1 to 4 (species mean 1.66); v4.4.3, 2,700, 1 to 15, 4.20 (4), 15.6%, 3.92, archaea 1 to 4 (1.66); v5.0, 5,856, 1 to 16, 4.60 (4), 13.3%, 4.04, archaea 1 to 4 (1.72); v5.6, 15,462, 1 to 21, 5.04 (5), 9.3%, 4.26, archaea 1 to 5 (1.66); v5.10, 48,053, 1 to 22, 5.52 (6), 7.5%, 4.36, archaea 1 to 5 (1.73).
- The long-quoted bacterial ceiling of 15 is no longer the database maximum: rrnDB v5.6 contains a Photobacterium damselae genome with 21 copies and v5.10 a Mesobacillus maritimus genome with 22, and several Photobacterium and Bacillaceae genomes have 20 to 21; no source checked whether these extremes survive scrutiny of assembly quality.
- Archaea carry 1 to 4 copies in rrnDB up to v5.0 and 1 to 5 from v5.6 (Natronorubrum, Natrinema, Methanococcoides, Methanolobus and others); Acinas et al. 2004 already reported a maximum of five archaeal operons, so the review's sources conflict on the archaeal maximum. *(cont)*
- Record-level means rise across rrnDB releases (4.2 in v3.1.227 to 5.5 in v5.10) mainly because of resequencing effort: in v5.10 E. coli contributes 3,902 records (3,860 at 7 copies), Klebsiella pneumoniae 2,534 (mostly 8) and Salmonella enterica 1,770 (mostly 7); species-level means move much less (3.9 to 4.4).
- In rrnDB v5.10 the mean of species means is 4.4 (median 4) for bacteria and 1.7 (median 1) for archaea, and 11.3% of bacterial species and 51.6% of archaeal species average one copy.
- Across 1,690 bacterial genomes (7,081 16S sequences extracted in silico; 909 species, GenBank 2012), copy number ranged from 1 to 15 with a mean of 4.2; 15% of genomes carried one copy and 21% two; phylum and class means were Acidobacteria 1.0, Alphaproteobacteria 2.2, Deltaproteobacteria 2.7, Actinobacteria 3.1, Betaproteobacteria 3.3, Bacteroidetes 3.5, Firmicutes 5.8 and Gammaproteobacteria 5.8.
- Copy number was less conserved across taxonomic levels than genome size.
- The Acidobacteria mean of 1.0 rests on 4 genomes from 4 species, and the rrnDB v5.10 Acidobacteriota mean of 1.4 on 29 species; these soil-relevant low values are imprecise.
- Taxon dependence is the strongest regularity: per-phylum species means in rrnDB v5.10 are Bacillota 6.9 (1,274 species), Pseudomonadota 4.4 (3,050), Bacteroidota 3.8 (662), Actinomycetota 3.5 (1,334), Cyanobacteriota 2.8 (102), Planctomycetota 2.0 (62), Verrucomicrobiota 1.8 (35), Chloroflexota 1.6 (20), Acidobacteriota 1.4 (29), Euryarchaeota 1.9 (332), Thermoproteota 1.0 (65) and Nitrososphaerota 1.1 (18).
- Phyla common in soil but poorly represented among genomes (Acidobacteriota, Verrucomicrobiota, Chloroflexota) sit at the low end of copy number, on small numbers of species.
- Within species, rrnDB v5.10 is less uniform than the 2015 release: of 1,038 species with at least five genomes, 44% show some variation, although the median range is 0; the 2015 figure of 77% identical used far fewer genomes.
- In the reviewer's reading, part of the within-species variation in rrnDB v5.10 is likely assembly error rather than biology: for example, 18 of 3,902 E. coli records report a single copy.
- Acinas et al. 2004 found up to 15 operons in bacteria, with copy numbers up to 7 common and about 40% of organisms having one or two operons; a single operon dominated in archaea.
- 16S copy number shows moderate phylogenetic signal (K = 0.48 on 484 taxa), and copy number is "strongly linked" to taxonomy across 2,900 genomes, with Archaea potentially under-represented in amplicon profiles.
- 16S gene count and operon count diverge where rRNA genes are unlinked: unlinked 16S and 23S genes are common in Deinococcus-Thermus, Chloroflexi and Planctomycetes, and up to 41% of rRNA genes in soil long-read metagenomes were unlinked, against none in human gut. *(single)*
- Copy number tracks ecological strategy: soil isolates that formed colonies quickly averaged 5.5 copies and slow responders 1.4. *(single)*
- Maximum reproductive rate doubles with a doubling of rrn copy number across 1,167 species. *(single)*
- Copy numbers for uncultured lineages without genomes (for example many soil Acidobacteriota, Verrucomicrobiota, Chloroflexota and candidate phyla) are not measured, genome databases over-represent cultured, clinically and industrially relevant taxa, and no source measured 16S copy number directly in environmental populations of soil archaea beyond genomes of cultured or enriched Nitrososphaerota; the archaeal copy-number distribution beyond its 1 to 4 range was not found.

### genome copies, and hence 16S copies, per cell

Builds on: 16S rRNA gene copies per genome.

- In cultures, genome copies per cell range from about one (Caulobacter, Wolinella, crenarchaea) to tens or hundreds (P. putida, haloarchaea, methanogens, Synechocystis) and depend on taxon, growth rate and phase; copy number does not change in one direction with growth phase.
- Most direct measurements of genome copies per cell come from one laboratory's real-time PCR protocol (Soppa group), in several studies cross-checked against Southern blots, flow cytometry or published E. coli values. *(single)*
- Monoploid examples: Caulobacter crescentus (about 2.1 genome-equivalents at a mid-chromosome locus at 93 min doubling, consistent with one chromosome plus replication), Wolinella succinogenes (about 0.9 at 96 min) and six crenarchaeal species of four genera.
- Growth-rate-dependent merodiploidy: E. coli has 6.8 origins and 1.7 termini per cell at 25 min doubling but 2.5 origins and 1.2 termini at 103 min; B. subtilis (5.9 origins, 1.2 termini) and three soil Bacillus and Paenibacillus isolates are mero-oligoploid in exponential phase and down-regulate origins in stationary phase.
- Polyploids: Pseudomonas putida about 20 origins and 14 termini (46 min doubling); Synechococcus PCC 7942 and WH7803 3 to 4 copies; Synechocystis PCC 6803 218 (exponential) to 58 (stationary) in one substrain and about 20 to 4 across six substrains; Halobacterium salinarum 25 to 15 and Haloferax volcanii 18 to 10 (exponential to stationary); Methanococcus maripaludis up to 55 (exponential) and about 30 (stationary); Methanosarcina acetivorans 17 (fast) and 3 (slow growth).
- Under phosphate starvation, polyploid down-regulation stops at about five copies in Zymomonas mobilis, Azotobacter vinelandii and H. salinarum rather than reaching monoploidy, but goes to one copy in Synechocystis after prolonged phosphate starvation.
- E. coli stationary-phase batch cultures always contained some multi-chromosome cells, even after days.
- Copy number does not always fall in stationary phase: Azotobacter vinelandii is reported to rise from about 4 copies in exponential phase to about 80 in stationary phase, and M. acetivorans from 2.5 to 5 (Bruck 2023 full text, secondary via the critic); Pecoraro 2011 Table 5 gives A. vinelandii as 1 (up to 8) copies in slow growth and 40 in fast growth, attributed to another laboratory.
- Measurements outside the Soppa laboratory exist and are listed in Pecoraro 2011: Azotobacter (40 copies in fast growth), Desulfovibrio (9 to 17), Neisseria (3 to 4), Buchnera (120), and polyploid Deinococcus, Borrelia and rhizobial bacteroids.
- Pecoraro et al. found only three to four of 11 proteobacterial species with measured ploidy to be monoploid, with no correlation to genome size, temperature or lifestyle; Hildenbrand et al. found none of seven euryarchaeal species monoploid, against all six crenarchaeal species.
- Single-cell measurements in H. salinarum showed wide cell-to-cell variation in genome copy number, larger in exponential than in stationary phase; the review read only the abstract, which gives no per-cell shares, although the open full text reports single-cell CLSM and FACS distributions. *(limited by access)*
- rRNA operons cluster near the replication origin in fast-growing bacteria, and gene-dosage effects shape this placement.
- That 16S copies per cell scale with origin number more than with genome number in fast growers is the reviewer's inference from one abstract; no source in the review measures 16S copies per cell against origin number.
- For E. coli, rRNA genes per genome equivalent range from about 7.9 to 9.5 across growth rates.
- No source measured 16S copies per cell directly in environmental cells, and in environmental samples the evidence on genome copies per cell is indirect and sparse: DNA mass per cell in soil, DNA-content populations in seawater and population-average replication indices in groundwater.
- Indigenous soil bacteria extracted from a clay loam contained 1.5 to 15 fg DNA per cell by flow cytometry, most below 4 fg, with an average around 2 fg; larger cells, and cells that grew in soil extract, had more DNA. This confirms earlier work by the same group (Bakken and Olsen 1989).
- DNA mass per cell cannot separate genome size from copy number.
- In the reviewer's reading, about 2 fg of DNA is less than one copy of a 4 Mb genome, which suggests many soil cells hold one copy of a small genome; the note marks this as inference.
- A typical seawater sample had a mean of 2.5 fg DNA per cell, in two populations described as 1n and 2n clusters, with 10 to 30% low-DNA "dim" cells; the two populations could reflect replicating monoploid cells or larger genomes, and the authors treat increased copy number with growth rate in nature as "likely", an inference rather than a measurement.
- In Prochlorococcus in the equatorial Pacific, DNA replication occurred in the afternoon, in phase with the light cycle, and division at night; the abstract read gives no share of cells. *(limited by access)*
- Flow cytometric cell-cycle analyses of Prochlorococcus (and Synechococcus) in situ are by method taxon-specific measurements of the share of cells with replicated DNA (G1 versus S/G2), so the review's statement that no such share exists for any natural community is not established; nothing comparable was found for soil. *(limited by access)*
- In groundwater metagenomes, population-average replication indices (iRep) were mostly low: Candidate Phyla Radiation bacteria had a median iRep of 1.34, and only 16.1% of values exceeded 1.5; the authors interpret an iRep of 1.25 as about a quarter of cells replicating.
- Gut metagenome peak-to-trough ratios track growth rate in culture and in vivo.
- Not found: genome copies per cell for named soil bacterial or archaeal taxa in situ; the share of single-copy cells in soil, rhizosphere or dormant natural populations; any direct measurement of 16S copies per cell in environmental cells; ploidy of cultured soil Acidobacteriota, Verrucomicrobiota or Nitrososphaerota; replication indices (iRep or peak-to-trough) for soil metagenomes.
- That no natural community has a taxon-specific measurement of the share of cells by genome copy number is not established: in situ flow cytometric cell-cycle analyses of Prochlorococcus are by method taxon-specific measurements of the share of cells with replicated DNA, and the review read only their abstract. Nothing comparable was found for soil. *(limited by access)*

### 16S copy number and read-based abundance; prediction and correction

Builds on: 16S rRNA gene copies per genome, PCR conditions, cycle number and template amount.

- Copy number is a property of each taxon rather than a workflow step, but it acts through PCR.
- With equimolar DNA from species pairs, PCR product ratios matched rrn genes per unit DNA for two pairs but deviated for a Bacillus pair.
- Copy-number prediction is accurate only near sequenced relatives: copy-number autocorrelation fell below 0.5 at about 15% 16S divergence and reached zero at about 30%; about 49% of SILVA OTUs are more than 15% from a sequenced genome; PICRUSt, CopyRighter and PAPRICA sometimes explained under 10% of variance against complete genomes and disagreed with each other (R2 below 0.5) for most of 635 communities, which included soils; the authors recommend against default correction unless OTUs are close to sequenced genomes. *(repl)*
- The distance-dependence of prediction accuracy is consistent across four independent analyses (Kembel 2012, Louca 2018, Edgar 2017, Gao and Wu 2023). *(repl)*
- Phylogenetic copy-number prediction had a leave-one-out error of about one copy, and in 100 simulated communities correction raised the correlation with true organism abundance from r = 0.70 to 0.81. *(cont)*
- In Kembel's data, correction moved ear samples to cluster with nostrils rather than feet but left ocean clustering largely unchanged.
- Gao and Wu report a prediction precision of about 0.96 at small distances, with uncertainty rising with distance; correction raised the chance of identifying the true most abundant OTU from 13% to 65% in simulations.
- Correction improves fit to simulated truth (Kembel 2012; Gao and Wu 2023).
- Correction changed the identity of the most abundant OTU in about 20% of Human Microbiome Project and 31% of Earth Microbiome Project communities, but against predicted, not measured, truth; in simulations it reduced sample shifts in ordinations but left PERMANOVA variance explained essentially unchanged (5.27 to 19.65% true versus 5.27 to 19.82% uncorrected).
- CopyRighter's correction improved agreement with mock communities and metagenomes, changed qPCR totals and diversity estimates, and reclassified twin gut samples from two enterotypes to three.
- On 10 V4 mock communities, uncorrected data fit known composition 7.1% (SE 3.6%) better than copy-number-corrected data; one of the eleven mocks was excluded, and all were DNA-based (nine genomic DNA mixes) or cloned-gene mocks. *(repl)*
- Copy number explained about 60% of the estimated PCR bias (R2 about 0.60, p about 0.021) but only about 10% of total bias across 7 taxa. *(single)*
- A preprint by the tool's author reports essentially no correlation ("no meaningful correlation") between 16S read and species frequencies in mocks; correction for copy number and primer mismatch reached r of about 0.6 only in ideal cases (exact references), falling to about 0.4 at 97% and about 0.2 at 95% identity. *(single)*
- Copy numbers can be estimated from draft assemblies by read depth, with a median deviation of 14% against qPCR.
- Applying copy-number (and genome-size) correction to a forest soil changed Acidobacteria from 50.1% of 16S sequences to an estimated 66.0% of genomes, Actinobacteria from 11.8% to 7.6% and Firmicutes from 3.2% to 1.1%; this is the only soil example of correction size, and it depends on the imprecise low Acidobacteria copy-number mean. *(single)*
- Whether copy-number correction helps is in conflict: studies recommending routine correction (Kembel 2012; Angly 2014; Gao and Wu 2023) against studies recommending against default correction or finding it unhelpful in mocks (Louca 2018; Edgar 2017; Starke 2021; McLaren 2019 in MB-01's list); part of the conflict reflects differences in what "truth" is (cell-based versus DNA-based mocks, simulated versus real communities, closeness to references), and correction changing dominant taxa but not beta-diversity test results lets both camps' observations hold together. *(cont)*
- Sequencing bias behaves as a consistent multiplicative factor per taxon, which can be corrected with calibration controls (McLaren 2019 abstract); the abstract does not compare the size of extraction and primer biases with copy-number bias. *(limited by access)*
- No soil mock community or soil cell-count benchmark of copy-number correction was found; the soil literature on community-weighted rrn copy number was not searched.
- No study was found that combines copy-number correction with per-cell genome copy measurements (ploidy) in a real community; the polyploidy literature asserts that ploidy also biases community analyses (Soppa 2017, not obtained).
- A review asserts that rDNA copy number can change within species in response to environment; the prokaryote evidence for this was not quantified in what the reviewer read.

### average 16S copy number of communities by environment

Builds on: 16S rRNA gene copies per genome, 16S copy number and read-based abundance; prediction and correction.

- Every environment-level copy-number value found is predicted from reference genomes, not measured: soil had the lowest abundance-weighted copy-number distribution in the Earth Microbiome Project; the EMP groups free-living (soil, water, sediment) and plant-associated samples together at about 2.2, with no separate value for water; animal-associated samples are predicted at about 3.4, with gut and saliva highest. *(single)*
- Predicted community copy number declines through succession in soil and sediment. *(single)*
- The environment-level copy-number predictions conflict with Louca 2018's finding that such predictions are inaccurate beyond about 15% divergence from a sequenced genome.
- Measured (not predicted) community-average copy number in soil, water or host samples, and a separate value for water, were not found; community-average copy number from shotgun metagenomes was not searched, so this rests on prediction-only sources.

### library preparation and sample indexing

Builds on: PCR conditions, cycle number and template amount.

- Library preparation and indexing choices include one-step fusion, two-step tailed or ligation designs, and single, combinatorial or unique dual indexes.
- Across 73 MiSeq datasets, library preparation method and primer choice were the most significant sources of bias, with distinct, motif-linked error patterns; this rests on Schirmer 2015 alone. *(single)*
- Library design also affected error and chimera rates across four platforms.
- A mock-community comparison of one-step versus two-step library preparation (Gohl 2016) was not obtained in full.

### sequencing platform and read length

Builds on: library preparation and sample indexing.

- Platform and read-length choices include MiSeq 2x250 or 2x300, HiSeq, NovaSeq, Ion Torrent, 454, and PacBio CCS full length.
- Dual-index MiSeq error depended on read overlap: raw V4 error rose with cluster density from 0.25% to 1.08%, a delta-Q of 6 cut it to 0.05 to 0.06% and preclustering to 0.01%, and partially overlapping regions stayed worse. *(repl)*
- After preclustering, V3-V4 error was 0.10 to 0.21% and V4-V5 0.36 to 0.64% per the bioinformatics angle; the lab angle reports 0.24 to 0.37% and 0.58 to 0.87%, read through a fetch-tool summary, probably at an earlier stage of curation.
- PacBio CCS with DADA2 recovered all expected full-length variants in two mocks with no residual errors; this is the developers' own claim, with no independent long-read mock benchmark.
- The DADA2 maintainer states that NovaSeq's binned quality scores break loess smoothing in error learning; at the time of the issue the method had not been tested on NovaSeq data.

### demultiplexing and index misassignment

Builds on: library preparation and sample indexing.

- Demultiplexing is done with or without filtering on index-read quality.
- On Illumina GAIIx with non-16S libraries, 0.51 to 0.76% of index pairs were wrong, falling to 0.06 to 0.43% after index-quality filtering. *(repl)*
- On patterned flow cells (HiSeq X, 3000/4000, NovaSeq) with non-16S genome and exome libraries, 0.2 to 6% of reads were misassigned in every run, about 10-fold less on MiSeq, and unique dual indexes cut 0.89% to 0.13%. *(repl)*
- Illumina's documentation gives 0.1 to 2% index hopping on patterned flow cells.
- On HiSeq 2500 with non-16S amplicons, cross-talk was 0.24%, falling to 0.03% after index-quality filtering, which kept 88% of reads. *(single)*
- In 16S data from GAIIx and 11 MiSeq runs, about 2% of reads were misassigned. *(single)*
- Barcode leakage between 16S plate wells was negligible. *(single)*
- In eukaryotic 18S data, up to 28.2% of unique sequences were undetectable mistags.
- With mammal and arthropod markers, 2.1 to 2.6% of sequences came from tag jumps.
- Index misassignment rates are fractions of reads assigned to the wrong sample; they mainly create false presences of taxa, concentrated where abundant taxa from other samples leak in, and they vary with platform, library type and run. The 16S-specific evidence is thin: one preprint abstract and one plate study.
- No 16S-specific measurement of index hopping on patterned flow cells (NovaSeq, NextSeq 2000) was found; the 16S rate is one preprint abstract.

### quality filtering, read merging and error correction

Builds on: sequencing platform and read length.

- Quality filtering and merging choices include quality, length, expected-error and abundance thresholds, plus the delta-Q rule when merging.
- On mocks from GAIIx, HiSeq and MiSeq runs, minimum read length, quality threshold and a minimum OTU abundance filter strongly affected alpha diversity and composition, while ambiguous bases and bad run length did not; almost every setting needed an abundance filter of 0.0001 to 0.01% to reach expected taxon counts (0.005% recommended), and weighted UniFrac conclusions were robust while unweighted metrics were sensitive. *(repl)*
- Stringent UPARSE-style filtering could significantly underestimate abundance and diversity, and newer clusterers produced up to 60% fewer spurious OTUs than UCLUST. *(cont)*
- Quality-filter stringency is disputed: Bokulich 2013 against Kopylova 2016.
- Error correction plus read overlapping cut substitution errors by 93% on average.
- The USEARCH author reports that most paired-read assemblers compute incorrect posterior quality scores.

### error correction, denoising and clustering into OTUs or ASVs

Builds on: quality filtering, read merging and error correction.

- An operational taxonomic unit (OTU) is a cluster of sequencing reads that differ by less than a fixed dissimilarity threshold; an amplicon sequence variant (ASV) is a sequence variant resolved exactly, down to single-nucleotide differences, by methods that control sequencing errors. *(background, not from the research)*
- Error-handling choices are 97% or 99% OTUs (de novo, closed or open reference) or ASVs from DADA2, Deblur or UNOISE3; DADA2 can process samples independently, pooled or pseudo-pooled.
- In an independent benchmark, relative abundances of expected taxa within each mock were similar across DADA2, UNOISE3, Deblur and open-reference OTUs, while counts of units differed widely: open-reference clustering gave 453 OTUs on the HMP mock and 8,891 on the Extreme mock, and on one soil DADA2 gave 16,609 ASVs, UNOISE3 11,613, Deblur 8,270 and open-reference 21,297 OTUs; no pipeline recovered every expected sequence, and on the Zymo mock all pipelines "markedly differed" from expected composition. *(repl)*
- Bacteroides varied from 20.6% to 24.6% across pipelines, and operating system mattered little for pipeline output.
- mothur and QIIME1 returned 10 to 200 times the expected number of sequences, and Faith's PD was overestimated 1.3 to 2.7-fold by QIIME2, 2 to 18-fold by QIIME1 and 3.5 to 29-fold by mothur; the authors report pipeline-dependent interpretations. *(repl)*
- DADA2 had the best sensitivity and UNOISE3 the best balance, while QIIME-uclust produced on average 134 one-off and 412 other spurious OTUs. *(repl)*
- The DADA2 developers report 93 output sequences on a 57-strain mock, against 249 for mothur and 378 for QIIME.
- After OTU clustering and singleton removal, tables contained approximately 50% (mock communities) to 80% (gnotobiotic mice) spurious taxa; the authors propose a 0.25% relative-abundance cutoff, and the most abundant spurious taxon in mocks had a median relative abundance of 0.12%. *(single)*
- QIIME closed- and open-reference OTUs inflated richness to 1,607 to 5,824 OTUs where about 20 were expected, and on V4 mocks 56 to 88% of predicted genus names were false positives. *(single)*
- In leaf litter, bacterial OTU richness was about half of ESV richness (slope 0.46), but alpha and beta metrics correlated at r > 0.90 and inferences matched, so OTU versus ESV mattered little for broad patterns. *(cont)*
- In 227 freshwater sediment, seston and mussel-gut samples the direction was reversed: ASV richness was about half of OTU richness, and Mollicutes dominated mussel gut by ASVs but were absent from OTU tables; the authors attribute the reversal partly to higher richness in sediment. *(cont)*
- The direction of the OTU versus ASV richness difference conflicts between studies (Glassman and Martiny 2018 against Chiarello 2022), and OTUs versus ASVs is a disputed choice (Schloss 2021 against the ASV developers). *(cont)*
- In soil and plant samples, OTUs versus ASVs changed which families were called differentially abundant, mostly families under 0.1% abundance. *(single)*
- The identity threshold that best matched species was about 99% for full-length 16S and about 100% for V4. *(single)*
- According to the DADA2 documentation, independent per-sample processing needs at least two error-free reads to detect an ASV, and pooling finds more ASVs per sample.

### variation among 16S copies within a genome

Builds on: 16S rRNA gene copies per genome, error correction, denoising and clustering into OTUs or ASVs.

- Intragenomic variants split genomes into several ASVs: 0.58 variants per copy for full-length 16S and 0.25 for V4. *(cont)*
- Full-length PacBio sequencing recovered intragenomic variants in their expected integral ratios. *(single)*
- Copies within a genome are not always identical: heterogeneity was found in 952 of 2,013 genomes, 87.5% of it below 1% divergence; inflation of unique-sequence richness reached 123.7% for full-length genes but was smaller at 97% clustering.
- Acinas et al. estimated an upper bound of about threefold diversity overestimation from operon redundancy.

### chimera formation and detection

Builds on: PCR conditions, cycle number and template amount, error correction, denoising and clustering into OTUs or ASVs.

- Chimera detection choices are UCHIME, UCHIME2 or ChimeraSlayer.
- Chimeras formed reproducibly across independent amplifications of a known mixture; less-abundant species showed chimera rates above 70%, and chimera count correlated with organism abundance (R2 = 0.97) in a staggered mock; the reproducibility rests on this one study. *(single)*
- Chimeras inflate richness and create false novel taxa; at 30 cycles they made up 0.9% (Accuprime) to 18.2% (Platinum) of reads depending on polymerase, and UCHIME sensitivity was 50 to 87% at 25 or more cycles.
- ChimeraSlayer detected over 87% of simulated chimeras when parents diverged by 4% or more, with a 1.6% false-positive rate, and sensitivity fell for every method as parents became more similar.
- UCHIME2's author states error-free chimera prediction is "impossible in principle".

### taxonomic assignment, classifiers and reference databases

Builds on: error correction, denoising and clustering into OTUs or ASVs.

- Taxonomy choices are RDP NBC, q2-feature-classifier, SINTAX, IDTAXA or MAPseq, against SILVA, Greengenes, RDP or GTDB-type references, optionally with habitat-weighted priors.
- Cross-validated by identity to the reference, all tested classifiers were at most 50% accurate on V4: genus accuracy was about 100% at 100% identity and about 50% at 97%; the author argues that mocks overstate accuracy because all their members are named type strains. This rests on one author, who also develops competing classifiers. *(single)*
- On mocks, the q2-feature-classifier methods reached median genus F above 0.8.
- Habitat-weighted priors cut species-level error from 25% to 14%.
- IDTAXA over-classified less when the true taxa were absent from the training set.
- Estimated annotation error is about 10% for RDP and about 17% for SILVA v128 and Greengenes 13.5, judged from conflicting labels on identical sequences. *(single)*
- On simulated gut, ocean and soil communities, genus recall was 67 to 80% and assignments varied by up to 40% between 16S subregions within a pipeline. *(single)*

### contaminants and negative controls

Builds on: DNA extraction.

- Contaminant-handling choices are dropping taxa seen in negative controls, decontam (frequency or prevalence mode), SourceTracker, or relative-abundance cutoffs.
- In a Salmonella bongori dilution series run at three institutes, contaminants dominated by about 10^3 input cells, more so at 40 than at 20 cycles, and profiles differed by kit and laboratory. *(repl)*
- In an 8-member mock diluted 3-fold eight times, contaminant reads rose from 0.1% to 80.1% and ASVs from 18 to 381; removing every sequence present in the negative control wrongly removed more than 20% of expected sequences, since three of the eight mock ASVs appeared in the control; decontam's frequency method removed 70 to 90% of contaminants and no expected sequences; SourceTracker removed over 98% when sources were well defined but failed on over 97% when they were not. *(single)*
- Well-to-well contamination arose mainly at extraction, less at library preparation, mostly into neighbouring wells (rarely up to 10 wells away), and was greatest in low-biomass samples. *(single)*
- Contamination varies inversely with biomass and is specific to the kit and laboratory.
- As biomass fell in a dilution series, contaminants made up a growing share of inferred communities under every sequence-inference method; the authors state no inference method alone separates contaminants from true sequences. *(single)*
- decontam's makers describe a frequency mode that assumes contaminant DNA is roughly constant across samples.
- Hornung 2019 surveyed 265 papers in the 2018 issues of Microbiome and The ISME Journal that used any high-throughput community sequencing (16S, shotgun, metatranscriptomics, ITS, 18S, virome, long-read and others): 30% (79) reported a negative control and 10% (27) a positive control. It is not a 16S-only figure, and it is a single source. *(single)*
- A review proposes the RIDE checklist.

### departure of observed from known composition across the whole workflow

Builds on: DNA extraction, PCR conditions, cycle number and template amount, error correction, denoising and clustering into OTUs or ASVs, contaminants and negative controls.

- Every mock-community study in the body found observed composition departing from known composition, and the size of the bias depends on platform, region, primer, extraction and pipeline. *(repl)*
- Departures were measured at most steps examined, but not at all of them: field sampling for water and host tissue was not searched, and several choices showed little or no detectable effect (PCR replicate pooling, preparation day and lane, cycle number in some studies, storage in one soil).
- For the number of taxa detected, inflation by spurious sequences (sequencing error, chimeras, cross-sample leakage), reagent contamination and the choice of clustering or denoising is replicated across independent mocks and dilution series, changing counts of taxa by one to two orders of magnitude: for example 10 to 200-fold excess units (Straub 2020) and contaminants rising from 0.1% to 80.1% of reads in a diluted mock (Karstens 2019). *(repl)*
- For relative abundance, the ordering in which extraction is the largest step, followed by PCR and then sequencing, rests on one 7-taxon vaginal dataset (Brooks 2015 reanalysed by McLaren 2019), with Albertsen 2015 (sludge, bead beating only) as partial support; it is contested by Fouhy 2016 (two extraction methods gave very similar data) and qualified by MBQC (specimen type mattered more than extraction), and is a single-dataset result, not a field-wide ordering. Fold errors of 2 to 30 or more between taxon pairs are reported. *(single)*
- Per-step magnitudes mostly come from one or two small mocks (7 to 20 taxa), often on 454 or Ion Torrent.
- The size of the extraction effect is in conflict: Fouhy 2016 against Albertsen 2015, Brooks 2015 and MBQC.
- Across 15 laboratories, variability depended most on specimen type, then DNA extraction, then handling laboratory, then bioinformatics; interlaboratory differences were substantial, and absolute diversity was not comparable between laboratories even with the same pipeline. *(single)*
- A review states that PCR-based estimates can deviate by "several orders of magnitude" if extraction, PCR, copy number and analysis errors are ignored.
- Archaeal evidence is thin: one archaeal-rich mock (Pinto and Raskin 2012), a copy-number range from 148 species, and one run-failure case (Yeh 2018); archaeal-specific primer bias measured against known composition is absent.
- Apart from McLaren 2019 and its source data (Brooks 2015), on which the per-step decomposition and ratio consistency rest, and Silverman 2021, on which the per-cycle PCR bias magnitude rests, removing any other single source would not change the answer.

### whether the departure is consistent across samples

Builds on: departure of observed from known composition across the whole workflow.

- McLaren et al. modelled each step as multiplying taxon abundances by a taxon-specific efficiency; under this model the error in taxon ratios was "consistent across samples", while the error in proportions "varied dramatically in both magnitude and direction". *(single)*
- Six parameters explained almost all systematic error in the cell mixtures, and calibration from control mixtures cut mean Bray-Curtis error from 0.35 to 0.08 (92.6% lower mean squared error) in the Brooks 16S cell mixtures (2 calibration samples, 69 calibrated samples); the Costea shotgun calibration is reported only qualitatively ("removed most of the systematic error").
- The authors list where the multiplicative model may fail: PCR saturation, taxa aggregated with differing efficiencies, matrix differences between controls and samples, and taxa absent from the controls.
- Brooks et al. found significant mixture-blending terms on the same data and concluded that one taxon's observed proportion depends on which others are present; the two readings conflict, and McLaren's attributes the apparent dependence to working on the proportion scale. *(cont)*
- On the ratio scale, extraction bias was consistent across samples within a protocol in the vaginal mock: ratio-scale consistency is shown in one 16S cell-mixture dataset. *(single)*
- A 10-species shotgun spike-in also gave a consistent profile across faecal backgrounds, with protocol H showing up to 2,751-fold maximum pairwise bias; this is shotgun, not 16S, known only via McLaren 2019, and a different measurement type from the 16S cell-mixture result.
- Variation of bias between sample types or samples is shown by the field-versus-mock SAR11 bias for 515F-Y/806R (Parada 2016, abstract only), inconsistent cycle effects in four stool samples (Sze and Schloss 2019), extraction yield of 40 to 84% (Zemb 2020) and a 66.7-fold spike-in recovery range (Zhou 2011, abstract).
- A 0.1% genomic spike was recovered at 0.06% to 5.34% of reads across soils, a 66.7-fold range; the 66.7-fold figure is in the abstract, the 0.06 to 5.34% range needs the body and could not be confirmed. *(single; limited by access)*
- Whether mock-derived bias applies to field samples is in conflict: Parada 2016 against calibration claims (McLaren 2019; Silverman 2021). Neither side's small-n and access limits are stated symmetrically in the review's strength line.
- Evidence on whether bias is consistent across samples is weak: it rests mainly on one reanalysis of 7 taxa, with contrary or limiting field evidence.

### total microbial load

- Microbial load differs up to tenfold among healthy human faeces. *(repl)*
- Prokaryote load differed 27-fold among Antarctic seawater stations. *(single)*
- Microbial load differed by more than six orders of magnitude across mouse gut sites. *(single)*

### reads per sample and variation in depth between samples

Builds on: sequencing platform and read length.

- The Earth Microbiome Project averaged 80,000 sequences per sample over 27,751 samples and rarefied to 5,000; in four environments, mean prevalence of tag sequences rose with depth up to 50,000, so 5,000 under-estimated prevalence.
- In one 360-sample MiSeq run, reads averaged 9,913 pairs per sample, with 95% of samples above 2,454. *(limited by access)*
- A dilution-series run ranged from 40,927 to 251,419 reads per sample, and three mock runs gave 36,464 to 146,653 read pairs.
- Across 12 public V4 studies, reads per sample varied up to about 100-fold within a study: human 10,439 to 422,904 (median 32,452, n = 490), bioethanol 3,690 to 356,027, mice 1,804 to 30,311, soil 46,622 to 58,935 (n = 18), marine 132,895 to 256,758 (n = 7). These are per study, not per run. *(single)*
- Schloss attributes the within-study spread to compounding random error when PCR products are pooled, and cites studies reporting that depth correlates positively with biomass despite normalisation (known only through Schloss).
- Makers claim more than 20 million reads per MiSeq v3 run and more than 100,000 per sample at 96-plex, said to be "sufficient to fully survey the bacterial composition"; a core facility gives about 20 million (v3) and about 16 million (v2) reads per run, with more than 100,000 per sample recommended.
- Median Good's coverage ranged from 89.4% (seagrass) to 99.8% (human), and reaching 95% and 99% coverage required about 3 and 101 times the sequences needed for 90%.
- No peer-reviewed coefficient of variation of reads per sample within a run after equimolar pooling was found; all three angles searched, and web search returned only forum posts.

### how abundance is distributed among taxa (species abundance distributions)

- In 24 Oklahoma grassland soils, the best-fitting abundance distributions were exponential or inverse gamma; these best fits are in the paper's supplementary Table S3, the main text does not state which distributions won, and they were not verified. *(single; limited by access)*
- In one Brazilian soil, 26,079 reads and 2,880 observed species were fitted equally well by communities of 10^4, 10^5 and 10^6 species, so the tail cannot be identified from sample data. *(repl; limited by access)*
- After copy-number correction, rank-abundance distributions from human skin and ocean fit a lognormal better; this single study pools ocean and skin into one item, and the same paper's simulations assumed a lognormal. *(single)*
- Lognormal dynamics best explained microbial abundance distributions across more than 20,000 samples; the abstract gives no per-environment breakdown, and soils are included but not reported separately. *(single)*
- A dominance scaling law held across about 35,000 sites.
- Mean abundances across taxa were lognormal "for all the data sets considered", and each taxon's abundance across communities was gamma-distributed with variance proportional to the squared mean; per-biome results are in supplementary figures that were not read. *(single)*
- The soil SAD shape is in partial conflict: exponential or inverse gamma (Zhou 2013) against lognormal (Shoemaker 2017; Grilli 2020); these use different fitting targets, and Haegeman 2013 argues the tail is not identifiable from sample data at all. *(cont)*
- Abundance-distribution shapes reported separately for water and for host-associated 16S data were not found beyond the copy-correction fits in Kembel 2012, although per-biome supplementary figures (Grilli 2020) and Shoemaker 2017's full text exist and were not read.
- In bulk-soil amplicon data from the global datasets found, a small minority of taxa carries a large share of reads, and most taxa are rare. *(repl)*
- Across 237 soils, per-sample richness ranged from 774 to 2,869 phylotypes, and 511 of 25,224 phylotypes (2%), defined as dominant jointly by abundance and ubiquity, accounted on average for 41% of 16S reads per sample: more than half in arid forests and only about 20% in tropical forests.
- Across 844 soils (318 sites, 90-bp V4 ASVs), 0.4% of ASVs, classed common on the globally pooled rank-abundance distribution, held about 58% of pooled relative abundance, and the 99.6% classed rare held 42%; drier soils had more even distributions, and the ratio of rare to common richness declined with rainfall frequency (Pearson r = -0.41, n = 318).
- The two dominant-share figures must be kept apart: about 41% for a top-10%-and-ubiquitous definition (per-sample mean) and about 58% for the 0.4% common class (pooled global relative abundance) use different definitions and denominators and are not comparable.
- Across 146 soils, archaeal reads averaged 2% of 16S reads (0 to over 10%), and two Thaumarchaeota (then Crenarchaeota) phylotypes made up over 70% of archaeal sequences. *(single)*
- Four Arizona soils were consistent with lognormal null models; small surveys reproduced richness but not composition, and documenting half the species would need 16,284 to 44,000 individuals.
- Lognormal-based estimates gave 6,400 to 38,000 taxa per gram of soil.
- Soils may need hundreds of times current sampling to reach 90% of taxa, and diversity estimates depend on the distribution assumed.
- DNA reassociation kinetics, which measure whole-community DNA rather than reads or cells, were best fitted by a power law, implying over a million distinct genomes in a pristine soil; metal pollution cut diversity by over 99.9%. This is the main contrary result on the shape of the distribution, and removing it removes the power-law side of the conflict.
- The functional form of the soil abundance distribution (lognormal versus power law) is contested and method-dependent: power law from reassociation kinetics against lognormal from clone-library models and large amplicon compilations; most of that evidence is abstract-only or modelled. *(cont)*
- No soil taxon abundance distribution built from metagenome coverage was found.
- Iowa corn and prairie soil metagenomes totalled about 300 Gbp, yet 80% of reads could not be assembled for low coverage, and 48% and 31% of contigs had coverage below 10x.
- Tropical soils are among the least-covered communities by Nonpareil estimates.
- 85% of the amplicon-defined dominant soil phylotypes were also dominant in 123 shotgun soil metagenomes; this is the only global amplicon-metagenome cross-check.
- No taxon abundance distribution from cell counts in soil was found; the cell-based soil data found concern only total DNA per cell, and the search route for cell counts was narrow.
- Absolute-abundance work multiplies relative abundance by total counts (flow cytometry or qPCR), which converts gene copies but not cells per taxon.
- Not found for soil: metagenome-based taxon abundance distributions reported as a distribution, copy-number- or ploidy-corrected abundance distributions, and rhizosphere-specific abundance distributions.

### sampling from the pool of amplified molecules (Poisson and multinomial models)

Builds on: reads per sample and variation in depth between samples, how abundance is distributed among taxa (species abundance distributions), technical replicates at different read depths.

- A Poisson random-sampling model of long-tailed abundance distributions predicted the low OTU overlap among soil technical replicates with no significant difference from the observed values, and about 60,900 sequences per replicate would be needed for 90% overlap. *(single)*
- The evidence that Poisson or multinomial sampling explains replicate disagreement in taxa detected comes from one dataset and one laboratory: Zhou 2013 modelled the same 24 Oklahoma grassland soils, sequenced on 454, that Zhou 2011 reported, and Wen 2017 is from the same laboratory; Wen 2017's MiSeq replicates cut against pure sampling. That sampling alone explains replicate disagreement in taxa detected is weak and contested. *(cont)*
- Zhou 2013 predicted about 60,900 reads for 90% OTU overlap, but in Wen 2017 unweighted overlap plateaued at 39% near 30,000 reads (with singletons) and reached only 43.9% at 160,000 reads; Wen's authors attribute rare-OTU variation to random sampling plus sequencing artefacts and report that "biases other than random sampling" affect unweighted metrics more.
- The sampling account (Zhou 2013) and technical variance beyond counting (Silverman 2018, 76%) differ in setting and in measure (OTU overlap versus variance of relative abundance); the review holds only the beyond-counting side to that caution, while the sampling side's own counter-evidence is left out.
- For one caecal extract, the abundance at which the CV of a taxon's relative abundance between technical replicates reached 30% fell with the square root of read depth, as Poisson noise would predict; this rests on one caecal extract with four technical replicates. *(single)*
- The "technical replicates are Poisson" assumption comes from RNA-seq: Illumina lane replicates fit a Poisson model, with about 0.5% of genes deviating; McMurdie and Holmes adopt it for technical replicates, so it rests on RNA-seq, not on 16S technical replicates.
- Each taxon's abundance across communities followed a gamma distribution (Taylor's law with exponent 2); treating absences as Poisson sampling at each sample's depth predicted occupancy from mean abundance and variance with no further parameters, and the model reproduced the abundance-occupancy relationship, so the author attributes absences mostly to sampling. The text read does not name soil among the biomes.

### technical replicates at different read depths

Builds on: sampling from the pool of amplified molecules (Poisson and multinomial models), reads per sample and variation in depth between samples.

- Technical replicates of the same soil DNA amplified with different barcodes shared 17.2 ± 2.3% of OTUs between two replicates and 8.2 ± 2.3% among three on 454, attributed to random sampling; the paper's discussion gives 13.1% and 5.9%, which differ from its abstract. *(single; limited by access)*
- In one soil sample, abundance-weighted OTU overlap among technical replicates rose from 56.7% at 2,000 reads to 95.3% at 160,000, and Bray-Curtis among technical replicates was 0.269 against 0.374 among treatment replicates. *(repl)*
- On MiSeq, 18 soil extracts shared 33.4% of OTUs between two replicates and 20.2% among three; in one deeply sequenced sample, presence/absence overlap rose from 20.7% at 2,000 reads to 43.9% at 160,000, plateauing near 30,000. Overlap was lower when replicates were sequenced in separate runs.
- Alpha diversity did not differ among technical replicates (Wen 2017), and replicate variation affected beta diversity more than alpha diversity (Zhou 2011).
- Greater depth improved replicate agreement in beta diversity for some mocks only.
- A preprint reports replicate Jaccard distances of typically about 0.15, and up to 0.71 across runs.
- In fungal ITS, OTUs averaging more than 10 reads were detected in nearly all replicates, and replicate dissimilarity (pseudo-beta-diversity) fell markedly with depth.
- Pooling PCR replicates had no detectable effect at moderate to high input (Smith and Peay 2014; Marotz 2019, abstract; Kennedy 2014, abstract), but replicates split before PCR disagreed strongly at low load (Dyrhovden 2021).
- That the difference in load is the likely reason for the pooled-versus-single PCR contrast is the reviewer's own reconciliation; no single study tested both conditions.
- The depth dependence of replicate agreement is rated moderate (Wen 2017; Zhou 2013; Smith and Peay 2014; Barlow 2020).
- Not found: a 16S study testing whether technical-replicate variance of relative abundance exceeds multinomial expectation across controlled read depths, and replicate-at-depth studies in water or host samples other than gut; replicate-at-depth studies are confined to one soil laboratory (Zhou, Wen) and one mouse caecum (Barlow).

### overdispersed count models (Dirichlet-multinomial and others)

Builds on: sampling from the pool of amplified molecules (Poisson and multinomial models).

- Human oral plaque counts rejected the multinomial in favour of the Dirichlet-multinomial, with overdispersion theta of 0.047 and 0.054. *(repl)*
- Every public dataset surveyed showed more variance than Poisson among biological replicates. *(repl)*
- Hierarchical Dirichlet-multinomial models detected shifts better than alternatives in simulation. *(single)*
- Beta-binomial and logistic-normal network models relax the multinomial further, according to their makers.
- Dirichlet-multinomial overdispersion has been shown only between biological samples, not among technical replicates: no study fitting overdispersion to 16S technical replicates was found.

### processes other than sampling (early amplification, runs and batches, dropout)

Builds on: sampling from the pool of amplified molecules (Poisson and multinomial models), PCR conditions, cycle number and template amount.

- In four artificial-gut vessels sampled hourly with 20 technical replicates per vessel, 76% of observed variation was attributed to technical sources beyond sequence counting. *(single)*
- Replicates split before PCR differed strongly while replicates split after PCR were nearly identical; in negative extraction controls, most species appeared in only one of five PCR replicates, with a mean Jaccard distance of 0.80 (range 0.65 to 0.87). *(single)*
- At 1:10^5 dilution of a staggered mock, 12 species appeared in only 2 of 4 PCR replicates.
- At low input, library preparation reached its Poisson loading limit, the two rarest taxa dropped out, and contaminants appeared below about 10^4 input copies.
- In low-input pools of unique synthetic barcodes, random per-molecule amplification in early cycles was the main source of skew; late-cycle polymerase errors stayed at low copy number, template switching was rare and GC bias minor; at low input, early stochastic amplification and dropout affected detection. *(single)*
- One HiSeq run lost an archaeal mock taxon from all samples and shifted others by more than 2-fold, while re-running the same amplicons was normal. *(single)*
- A PCR machine with a mis-set annealing temperature produced a batch outlier.
- Per-strain CV across five runs had a median of 11.8% (range 5.5 to 73.7%), and under-represented strains varied most.
- Mean relative abundances were reproducible across two runs and two depths.
- Batch-correction tools exist, and their makers claim they work.
- Primer mismatch and low efficiency remove or suppress specific taxa (non-random dropout); in eDNA simulations with a low-efficiency primer set, a median of 88 of 1,000 taxa were detected after 20 cycles.
- Technical variance beyond counting, early stochastic amplification at low load, run failures and primer-driven dropout are measured, but each mostly in a single study. *(single)*

### zeros in count tables

Builds on: sampling from the pool of amplified molecules (Poisson and multinomial models).

- In simulation, simple count models sufficed across four zero-generating processes, and zero inflation was warranted only under narrow conditions. *(single)*
- Pseudocounts made tests conservative. *(single)*
- Schloss asserts that a microbiome zero more likely means true absence, which conflicts with Grilli 2020's sampling interpretation.

### richness and other alpha diversity measures under unequal depth

Builds on: reads per sample and variation in depth between samples.

- Chao1, ACE, CatchAll, Shannon and Simpson all varied with library size in pyrosequencing data. *(repl)*
- In Schloss's null models built from 12 V4 datasets, observed richness, Chao1, ACE, breakaway and SRS-normalised richness all correlated with depth; Shannon was less depth-sensitive and inverse Simpson was not depth-sensitive. *(cont)*
- The depth dependence of raw and estimator richness is replicated (Gihring 2012; Schloss 2024b; Haegeman 2013). *(repl)*
- Multiplicative bias can make an uneven sample look more even, biasing Shannon and inverse Simpson.
- PCR-bias calibration improved Shannon in 7 of 10 mocks.
- In simulated faecal communities with load varying from 1.9 x 10^9 to 10^13 cells per gram, all 13 transformations reproduced Shannon and Simpson, but richness was recovered reliably only by quantitative profiling in a bloom scenario. *(single)*
- In freshwater and sediment 454 data, 5,000 sequences captured Shannon trends and over 80% of Chao1 trends. *(single)*

### between-sample (beta) diversity under unequal depth

Builds on: reads per sample and variation in depth between samples.

- Proportions and rarefying were the only methods that fully normalised depth, and scaling methods masked differences in common OTUs. *(single)*
- Whether proportions suffice for beta diversity is in conflict: McKnight 2019 against Schloss 2024b, in which relative-abundance Bray-Curtis stayed depth-sensitive under the null. *(cont)*
- Library-size normalisation had very little effect on beta-diversity separation compared with the choice of distance metric. *(single)*
- Bray-Curtis was usually the most powerful metric, and metric choice changes power. *(single)*
- 1,000 denoised sequences explained 90% of the Bray-Curtis trends seen at 15,000 to 20,000.

### rarefying and rarefaction to a common depth

Builds on: reads per sample and variation in depth between samples, richness and other alpha diversity measures under unequal depth, between-sample (beta) diversity under unequal depth.

- Rarefaction comes from ecology, traced to Sanders 1968, Hurlbert 1971 and Simberloff 1972; Gotelli and Colwell argue that individual-based rarefaction allows meaningful comparison and that asymptotic estimators give lower bounds; rarefaction curves are a display of sampling completeness and were not benchmarked as a comparison method in the sources found.
- Schloss distinguishes "rarefying" (one random subsample) from "rarefaction" (the mean over many subsamples). In his null models built from 12 V4 datasets, only repeated rarefaction removed the correlation between richness and depth; size-based iNEXT nearly did, except for the small, evenly sequenced marine and soil sets; when depth was confounded with group, only rarefaction and size-based iNEXT held a 5% false-positive rate, and rarefaction gave the highest power.
- In Schloss's null models, Jaccard and Bray-Curtis computed from raw counts, relative abundances, CSS or SRS, as well as Aitchison distances (four zero-handling variants) and DESeq2 VST Euclidean distances, all correlated with depth differences; only rarefaction removed the correlation, and only rarefaction held 5% false positives in PERMANOVA under confounding.
- The null model reassigns sequences at random, so samples differ only through multinomial-type sampling; taxon-specific bias, technical variation beyond counting and differences in load are absent from the simulated truth.
- The claim that only rarefaction removes the depth dependence of alpha and beta diversity under confounding rests on Schloss 2024b (supported in part by Weiss 2017 for beta and differential abundance); removing Schloss 2024b would leave rarefying contested, with McMurdie and Holmes 2014 as the main benchmark against it.
- In Weiss 2017, rarefying clustered samples better for presence/absence metrics, and other normalisations were vulnerable below about 1,000 reads per sample. *(repl)*
- In simulations from Global Patterns, rarefying to the 15th percentile and dropping samples below it reduced clustering accuracy. *(cont)*
- Schloss identified 11 design choices that disadvantaged rarefying in McMurdie and Holmes 2014; notably, low-depth samples were removed only in the rarefied arm. *(single)*
- In real river data, rarefying barely changed Bray-Curtis or Jaccard (r > 0.9) and did not change weighted UniFrac.
- Repeated rarefying shows that the random variation rarefying introduces grows as rarefied depth shrinks. *(single)*
- Willis argues that plug-in and rarefied richness are both negatively biased and that rarefying can create false differences between environments with equal richness but different abundance structures; she recommends estimators with variance estimates compared through measurement-error models. The paper gives statistical argument plus a worked simulated example, not assertion alone. *(cont)*
- Breakaway and betta are offered by their makers as estimators with variance estimates; Schloss 2024b found breakaway intervals mostly too wide to be useful.
- Studies disagree on whether rarefying harms differential-abundance tests: rarefied counts and proportions gave high false-positive rates with DESeq2 and edgeR near zero (McMurdie and Holmes 2014); rarefying did not raise FDR for most methods and lowered it at about 10x group differences in library size, at a cost in sensitivity (Weiss 2017). *(cont)*
- Rarefying followed by permutation controls type I error; the sensitivity loss is negligible when overdispersion is high, and is summarised by a rarefaction efficiency index. *(single)*
- With a tenfold depth difference, tests on proportions had severe type I inflation, which rarefying controlled; no method was "simultaneously robust, powerful, and flexible". *(repl)*
- Rarefying is contested: McMurdie and Holmes 2014 against Schloss 2024a and 2024b, Weiss 2017 and Hong 2022 (partial), with Willis 2019 opposing it for richness; beta-diversity results are contested and simulation-based, and simulation results flip with design choices, as Weiss 2017 and Schloss 2024a both say. *(cont)*
- That simulations disagree because they build different data-generating processes into the truth is partly supported (Weiss 2017, Hong 2022 and Schloss 2024a each say results depend on data-generating assumptions) and is the review's own causal diagnosis.

### coverage-based standardisation

Builds on: richness and other alpha diversity measures under unequal depth, rarefying and rarefaction to a common depth.

- Chao and Jost argue that standardising by sample completeness rather than size gives less biased richness ratios.
- A 2026 test on terrestrial inventories finds that coverage-based rarefaction "does not respond predictably" to richness. *(single)*
- In Schloss 2024b's null models, coverage-based iNEXT estimates were among those that "showed a strong correlation between richness and the number of sequences"; the text exempts "rarefaction and possibly the size-based iNEXT estimates". This is the only microbial amplicon test of coverage-based standardisation found; beyond it the evidence is non-microbial. *(single)*
- Coverage-based standardisation is in conflict: Chao and Jost 2012 against Alroy 2026 (both non-microbial) and the microbial null model in Schloss 2024b; an independent microbial amplicon benchmark of coverage-based standardisation with known truth was not found.

### richness estimators and extrapolation

Builds on: richness and other alpha diversity measures under unequal depth.

- Sample data carry no information on the rare tail: Chao's estimator ranked in silico communities wrongly (a community with 20 times fewer species was estimated to have 10 times more), and bounds for Hill numbers of order 2 and above nearly coincide; the authors recommend Shannon and Simpson over richness. *(repl)*
- Hill-number extrapolation is reliable only to about 2 to 3 times the reference sample size for richness.
- Chao1 and ACE are invalid on ASV tables from algorithms that drop singletons, as DADA2 does by default. *(single)*
- Spurious OTUs severely inflated Chao1, and removing them severely underestimated Chao1 in uneven communities, while abundance-weighted metrics were little affected.
- An abundance filter makes ACE and Chao1 inapplicable.
- A singleton-replacement estimator for error-inflated data has been proposed. *(single)*

### compositional (log-ratio) approaches

Builds on: reads per sample and variation in depth between samples.

- A review argues that 16S data are compositions "at all stages" and should be analysed with log-ratios. *(cont)*
- Aitchison (log-ratio) distances were depth-sensitive under Schloss's null model.
- Fold changes in taxon ratios are invariant to multiplicative bias, while fold changes in proportions are not and can change sign; the bias-invariance of ratio-based methods rests on McLaren 2019.
- Proportion-based differential-abundance results err when the community's mean efficiency is associated with the condition. *(single)*
- Reference frames make differential rankings invariant to load. *(single)*

### scaling and normalisation methods

Builds on: reads per sample and variation in depth between samples.

- Total-count scaling can bias differential-expression estimates in RNA-seq; TMM and DESeq's negative binomial model also come from RNA-seq, and both assume most features are unchanged between conditions.
- In shotgun gene-abundance data, TMM and RLE performed best.
- Under Schloss's null model, scaling normalisations (TMM, RLE, CSS, VST, SRS, Wrench) did not remove depth effects, while in the Llorens-Rico 2021 simulation RLE and VST came close to quantitative methods for association tests in a dysbiosis scenario.
- Wrench's makers state that library-size scaling and rarefaction cannot correct compositional bias that is uncorrelated with library size, and SRS's makers claim better reproducibility than rarefying.

### tests of which taxa differ in abundance

Builds on: rarefying and rarefaction to a common depth, compositional (log-ratio) approaches, scaling and normalisation methods.

- Fourteen differential-abundance methods on 38 datasets gave 0.8% to 40.5% significant ASVs (unfiltered means); ALDEx2 and ANCOM-II were the most consistent, and edgeR and LEfSe produced many false positives on random splits. *(single)*
- Excess false discoveries were widespread across methods. *(repl)*
- Methods with the highest false-positive rates had the most power.
- Microbiome-specific methods did not beat RNA-seq methods. *(single)*
- In implanted-signal benchmarks, only linear models, Wilcoxon, t-test, limma and fastANCOM controlled FDR at relatively high sensitivity; fitZig reached an observed FDR of 80%, and ANCOM and ANCOM-BC controlled FDR only at 200 or more samples per group. *(repl)*
- Elementary methods on relative abundances (Wilcoxon, linear models) were the most replicable across 53 studies. *(single)*
- ANCOM had the best FDR control in Weiss 2017, while DESeq2's FDR rose with more samples or uneven libraries.
- Makers claim FDR control for ANCOM-BC and ANCOM; independent benchmarks disagree in part, with ANCOM-BC showing type I inflation in some settings (Yang and Chen 2022) and controlling FDR only at 200 or more samples per group (Wirbel 2024).
- Differential-abundance methods disagree widely and FDR failures are common, which is robustly shown (Nearing 2022; Hawinkel 2019; Yang and Chen 2022; Wirbel 2024); which method is best is contested. *(cont)*

### absolute quantification of total load (qPCR, flow cytometry, dPCR, spike-ins)

Builds on: total microbial load, departure of observed from known composition across the whole workflow.

- Load measurements change conclusions drawn from relative data: qPCR, flow cytometry, dPCR and spike-ins can reverse relative-abundance conclusions; this is replicated. *(repl)*
- Flow-cytometry quantitative profiling showed the Bacteroides-Prevotella trade-off in relative data to be an artefact, and load drove Crohn's-associated differences.
- Relative enrichment did not imply absolute outgrowth.
- Absolute abundance could hold steady or rise while relative abundance fell.
- Spike-in bacteria added before extraction recovered ratios of absolute abundances across mouse faecal dilutions, although the three spike-in species gave different read yields. *(repl)*
- dPCR anchoring gave about 2x extraction accuracy above 8.3 x 10^4 input copies, and absolute but not relative analysis revealed diet effects. *(single)*
- Soil internal standards tracked PLFA and respiration biomass better than those two measures tracked each other. *(single)*
- Total 16S qPCR multiplied by relative abundance correlated near-perfectly with taxon-specific qPCR, a comparison of methods that share an upstream (qPCR versus qPCR-anchored sequencing), on four taxa. *(single)*
- In simulation, experimental quantitative profiling outperformed computational transformations for associations.
- Absolute quantification does not correct taxon-specific extraction and PCR bias.
- qPCR and sequencing both count extracellular DNA, unlike cell counts.
- qPCR and flow cytometry agreed on a whole-cell mock (|r| = 0.967) but gave "highly divergent" profiles for faeces, where qPCR against flow-cytometry enumeration correlated at Pearson r = -0.50; ddPCR correlated strongly with qPCR, which the authors used to rule out qPCR imprecision as the cause of the divergence. The divergence rests on this one study. *(single)*
- Synthetic spike-ins had differing detection efficiencies and small departures from linearity, and correlations were weaker with Taq than with KOD polymerase. *(repl)*
- Seawater internal standards agreed with flow cytometry at r2 = 0.19 until corrections for copy number and particle association (with four outliers removed) raised it to 0.61; the authors conclude that the method "provided results consistent with ... total bacterial counts by flow cytometry" and "is quantitative". *(single; limited by access)*
- A review states that internal standards often underperform or fail.
- Agreement between absolute-quantification methods is weak and in conflict (Jian 2020 against Galazzo 2020).
- No approach to comparing samples with unequal depth or load is shown to correct depth, load and taxon-specific bias together; benchmarks that build taxon-specific bias and load differences into the simulated truth together are absent apart from Llorens-Rico 2021 (simulated faeces without taxon bias), and no benchmark used measured absolute loads in soil or water as truth or tested richness corrections against known-richness mocks across depths.

### within-sample abundance terms (rare, abundant, conditionally rare) and rarity frameworks

Builds on: how abundance is distributed among taxa (species abundance distributions).

- The "rare biosphere" entered usage with deep-sea tag sequencing, which found thousands of low-abundance populations alongside a few dominants; reviews describe a few dominant taxa and many rare ones without fixing a threshold.
- Three families of definition are in use and are not interchangeable: within-sample relative-abundance thresholds (0.1% most common for rare), occupancy or prevalence across samples (core, mostly occurrence-only) and regional or global (pooled) classes; usage is heterogeneous and often unstated, from two systematic surveys.
- Within-sample thresholds: rare is most often below 0.1% of reads per sample, sometimes below 0.01% or 0.001%, and abundant is usually above 1% (Lynch and Neufeld 2015, Galand 2009, Dai 2016); Jia et al. 2022 uses a single rare/common cutoff and does not support "abundant above 1%".
- Galand et al. 2009 set rare below 0.01% and abundant above 1% per sample, calling the 0.01% cutoff "much more severe than the <0.1% criteria proposed earlier" and tying it to a singleton in the smallest library.
- Dai et al. 2016 set rare below 0.1% and abundant above 1%, with six categories combining these thresholds with behaviour across samples: always abundant, conditionally abundant, always rare, conditionally rare, moderate, and conditionally rare or abundant.
- A survey of 181 rare-biosphere articles from 2006 to 2024 found that about 37% gave no clear method; of those with a method, about 84% used relative abundance thresholds, about 60% of those used a single threshold, and about half used 0.1%, about 70% of them per sample rather than on the pooled dataset.
- Conditionally rare taxa are defined by a bimodal abundance distribution over time (coefficient of bimodality) together with a maximum relative abundance above 1%; across 42 non-soil time series they made up 1.5 to 28% of membership. A three-way split into permanently, transiently and conditionally rare taxa has been applied in soil.
- From general ecology, rarity is classed along local abundance, habitat specificity and geographic range (Rabinowitz 1981), whose concepts the authors of a microbial review say "can be easily transferred to microbial communities"; reviews treat habitat specificity and geographic range as microbial rarity axes alongside local abundance.
- In a 21-year estuarine fish record, persistent and abundant "core" species fitted a lognormal while infrequent "occasional" species fitted a log series, and Galand et al. report the same split for rare versus abundant Arctic Ocean prokaryotes.
- No survey was found that tallies definitions within soil studies or separately for bulk soil and rhizosphere; no study compares threshold-based rarity classes between amplicon and metagenome data from the same soil samples; copy-number-corrected thresholds were not found to have been tested.

### regional and global distribution terms (dominant, common)

Builds on: within-sample abundance terms (rare, abundant, conditionally rare) and rarity frameworks.

- In soil, "dominant" has been defined jointly: in the top 10% of phylotypes by share of 16S reads and present in more than half of 237 soils.
- "Common" versus "rare" has also been set by a data-driven minimum cross-entropy threshold on the globally pooled rank-abundance distribution, about 0.019%, with prevalence across samples reported separately; the threshold was robust to using a quarter of the samples.
- Terms are used inconsistently: "dominant" sometimes means abundant within a sample and sometimes abundant and ubiquitous; "common" means high pooled abundance in Bickel and Or 2021 and high occupancy elsewhere.

### occupancy terms (core, prevalence)

Builds on: local abundance against occupancy across soils, and the role of sampling and detection, within-sample abundance terms (rare, abundant, conditionally rare) and rarity frameworks.

- "Core" is the main occupancy term: it was first framed as the members shared across samples, the overlap of Venn diagrams, with later calls to add persistence and connectivity; Risely distinguishes five kinds of core (common, temporal, ecological, functional, host-adapted) and argues that no one definition captures all.
- A survey of 224 core-microbiome studies found that 75.4% used occurrence only, 4% relative abundance only and 11.6% combined the two, with over 18% not stating a method; occurrence cutoffs ranged from 30% to 100% of samples (100% most common) and, in combined methods, abundance cutoffs from 0.1% to 4.5%.
- Neu et al. report, citing other work, that only two OTUs were shared by all of 24 soil locations and none across 51 wastewater plants.
- In common bean rhizospheres across four US regions plus a Colombian dataset, 48 bacterial and archaeal taxa were detected in every sample; fitting a neutral model to the abundance-occupancy distribution, 13.7% of bacterial and archaeal taxa deviated from neutral expectation; samples were rarefied to 31,255 reads.
- In 4,866 maize rhizosphere samples, seven OTUs were present in all, five of them responsive to host genotype.
- Rhizosphere evidence on abundance and occupancy is limited to core-membership studies of two to three crops, and none of these rhizosphere studies reports an abundance-occupancy correlation coefficient in the passages read.
- Abundance-occupancy ranking with a neutral-model fit has been proposed to prioritise core members.

### local abundance against occupancy across soils, and the role of sampling and detection

Builds on: occupancy terms (core, prevalence), regional and global distribution terms (dominant, common), how abundance is distributed among taxa (species abundance distributions), sampling from the pool of amplified molecules (Poisson and multinomial models), technical replicates at different read depths.

- In 88 North and South American soils (about 1,500 reads per soil), the ten most abundant OTUs per sample occurred on average in 28% of soils, against 2% for all OTUs; in 27 tropical forest soils within one hectare the figures were 69% against 8%; total abundance and occupancy were significantly and positively related, with no coefficient given. These figures could not be verified by the critic, and the abstract frames the study across Earth's major habitat types, not soils alone. *(limited by access)*
- Nemergut's authors note that abundant taxa may simply be easier to detect, and that undersampling could hide intermediate distributions.
- Across 844 global soils, median prevalence was 0.3 for common taxa and 0.001 for rare taxa; this is a class-level contrast, a different measure from Nemergut's taxon-level relationship.
- In the two bulk-soil amplicon studies with figures (Bickel and Or 2021; Nemergut 2011), more abundant taxa occupy more soils, but the two are not fully independent (Bickel and Or reanalysed compiled datasets including the Earth Microbiome Project, which plausibly overlaps Nemergut's soils), and both measures are partly built in by construction: "total abundance" summed across samples and "common" defined on the pooled rank-abundance distribution both rise with occupancy. Whether a relationship exists beyond sampling, and how strong it is, is unresolved. *(unclear)*
- The global "dominant" list cannot test the abundance-occupancy relationship, because dominance there is defined by abundance and ubiquity together.
- Across about 124,000 taxa in 3.41 km2 of urban park soil, occupancy correlated strongly with environmental range; abundance was not the axis tested.
- Soil also holds taxa that are abundant at some times or places and rare elsewhere: a salt-marsh chronosequence had 2,197 conditionally rare ASVs alongside 11,838 permanently rare and 8,333 transiently rare ASVs; such conditionally rare taxa are locally abundant but occupy few samples, cutting against a uniform relationship.
- Core assignments in an Arabidopsis root dataset varied 7-fold among methods.
- Low-abundance taxa are often recorded absent when present, because technical replicate soil libraries shared only 17.2% (two replicates) and 8.2% (three) of OTUs: this occupancy conclusion is the reviewer's argument, generalised from one 454-era study at one site whose abstract attributes the low overlap to random sampling but does not draw the occupancy conclusion. *(single)*
- Pyrosequencing errors inflated rare-tail richness; better clustering cut richness by 30 to 60% but did not remove the long tail.
- A neutral community model with immigration and drift only predicts that abundant taxa occur in more samples, so a positive abundance-occupancy relationship is expected without selection; its use in the bean rhizosphere treats deviations, not the relationship itself, as signal. Detection limits and neutral or sampling models predict a positive relationship without selection.
- The same positive abundance-occupancy observation is read as ecological signal by some authors and as near-null by others; the reviewer notes this is a difference of interpretation, not of data.
- In general macroecology, positive intraspecific and interspecific abundance-occupancy relationships are common (general in the British flora and fauna), and multiple explanations have been tested; the sampling-artefact literature (Wright 1991; Holt et al. 2002) was not obtained.
- No soil study was found that tests whether the observed bulk-soil abundance-occupancy relationship exceeds what sampling and detection alone would produce, so the share attributable to biology is unknown; none was found from cell counts or metagenomes, none specific to archaea, none comparing bulk soil and rhizosphere within one study, and none that is copy-number- or ploidy-corrected. *(unclear)*
- Rarer taxa better predicted soil community structure across 30 datasets (1,998 samples); the study does not report abundance-occupancy and is not used in the review's answers.
- The review's positive abundance-occupancy answer is its own reading of Bickel and Or 2021, Nemergut 2011 and general macroecology, not an echo of the brief, which states no expected direction.

### whether classifications and conclusions hold across thresholds and definitions

Builds on: within-sample abundance terms (rare, abundant, conditionally rare) and rarity frameworks, occupancy terms (core, prevalence).

- In a soil salt-marsh chronosequence (five stages over 110 years, amplicon ASVs), the rare fraction of reads was 61.6%, 45.7% and 28.4% at cutoffs of 0.2%, 0.1% and 0.05%; as the cutoff tightened, permanently and transiently rare ASVs fell in proportion and conditionally rare ASVs rose, and the relative importance of selection rose, while beta-diversity patterns and the main assembly inference (homogeneous selection for the rare biosphere, variable selection for the common) were reported as similar across cutoffs. This is the only soil test of threshold sensitivity found.
- In Arctic Ocean data, the biogeography of rare taxa persisted at a 0.001% cutoff.
- In coastal sands, ecological patterns were maintained after removing up to 35 to 40% of rare sequences.
- In marine samples, the 0.1% per-sample rule gave more rare than abundant ASVs with V4V5 amplicons and the reverse with full-length 16S, and threshold-based classes behaved differently across OTUs, ASVs and metagenomic OTUs, while the unsupervised method (ulrb) gave the same pattern across these.
- Four core-microbiome methods compared on human faecal (319 samples) and Arabidopsis root (288 samples) data assigned 1.2% to 9.4% of taxa as core (nearly 10-fold), and 165 to 176 taxa were agreed by all four methods, which is 13 to 16% of core assignments; the review's "about 1% of taxa" is its own derivation.
- In the human data of the core-method comparison, the review reports that a temporal effect significant in the full dataset was not significant in core-based analyses (a changed PERMANOVA conclusion); Custer's text is internally inconsistent on whether core analyses gained or lost the temporal effect. *(unclear)*
- Occupancy-based core methods were most accurate in simulations; this rests on one simulation study. *(single)*
- In sponges, core definitions changed alpha and beta diversity in some cases but not conclusions on host specificity, environmental quality or networks; the authors call the approach "surprisingly robust".
- In the human gut, core size depended mostly on analysis depth and required prevalence.
- In Loess Plateau soils, two primer pairs gave different diversity responses to land use, so rare and abundant classes depend on the primer, not only the cutoff.
- Tests of threshold sensitivity point both ways and are each single-system: some report conclusions that hold across thresholds or definitions (Jia 2022, Galand 2009, Gobet 2010, Astudillo-Garcia 2017) while others report classifications or conclusions that change (Pascoal 2025, Custer 2023, Salonen 2012); these are not strictly contradictory because they test different outputs (membership counts versus beta-diversity or assembly inferences).
- Proposed standards include unsupervised classification (ulrb), multivariate cutoff analysis (also recommended for rare-biosphere assembly work), abundance-occupancy ranking with neutral-model deviations for cores, and explicit reporting with explicit spatial and temporal scale of the core, deep sequencing and no rarefying when quantifying the core; no proposed standard was found to be widely adopted.

## Do not say

Wordings the research itself says are wrong or overstated.

- "No source found on the effect of water sampling choices (volume, filter pore size) or host tissue sampling."
  Why: on the review's own Search record no angle searched these choices; they are unsearched, not "not found"
  Say instead: Field sampling choices for water (volume filtered, filter pore size) and for host tissue were not searched by any angle: they are unsearched, not "not found".
- "Departures occur at every step."
  Why: field sampling for water and host tissue was not searched, and several choices showed no detectable effect; departures were measured at most steps examined
  Say instead: Departures were measured at most steps examined, but not at all of them: field sampling for water and host tissue was not searched, and several choices showed little or no detectable effect (PCR replicate pooling, preparation day and lane, cycle number in some studies, storage in one soil).
- "Extraction is the largest step for relative-abundance error, then PCR, then sequencing" as a field-wide ordering, rated strong and backed by "many independent mock studies".
  Why: one 7-taxon vaginal dataset (Brooks 2015 reanalysed by McLaren 2019); contested by Fouhy 2016 and qualified by MBQC; the review's own single-source sensitivity says the ordering rests on McLaren and Brooks
  Say instead: For relative abundance, the ordering in which extraction is the largest step, followed by PCR and then sequencing, rests on one 7-taxon vaginal dataset (Brooks 2015 reanalysed by McLaren 2019), with Albertsen 2015 (sludge, bead beating only) as partial support; it is contested by Fouhy 2016 (two extraction methods gave very similar data) and qualified by MBQC (specimen type mattered more than extraction), and is a single-dataset result, not a field-wide ordering. Fold errors of 2 to 30 or more between taxon pairs are reported.
- "The largest measured distortions in relative abundance arise from taxon-specific efficiencies at DNA extraction and PCR" as a property of the field.
  Why: rests on one 7-taxon dataset, with Albertsen 2015 as partial support; contradicted by Fouhy 2016 and qualified by MBQC
  Say instead: For relative abundance, the ordering in which extraction is the largest step, followed by PCR and then sequencing, rests on one 7-taxon vaginal dataset (Brooks 2015 reanalysed by McLaren 2019), with Albertsen 2015 (sludge, bead beating only) as partial support; it is contested by Fouhy 2016 (two extraction methods gave very similar data) and qualified by MBQC (specimen type mattered more than extraction), and is a single-dataset result, not a field-wide ordering. Fold errors of 2 to 30 or more between taxon pairs are reported.
- "Calibration cut mean Bray-Curtis error from 0.35 to 0.08 in a shotgun dataset."
  Why: the full text places this in the Brooks 2015 16S cell mixtures; the Costea shotgun calibration is reported only qualitatively
  Say instead: Six parameters explained almost all systematic error in the cell mixtures, and calibration from control mixtures cut mean Bray-Curtis error from 0.35 to 0.08 (92.6% lower mean squared error) in the Brooks 16S cell mixtures (2 calibration samples, 69 calibrated samples); the Costea shotgun calibration is reported only qualitatively ("removed most of the systematic error").
- "The original 515F/806R V4 primers under-represented SAR11 by about 4 to 10-fold in field samples but only about 2-fold in mocks."
  Why: the abstract gives these figures for 515F-Y/806R, not the original 515F-C/806R
  Say instead: For the 515F-Y/806R pair, SAR11 was under-represented about 4 to 10-fold in marine field samples but only about 2-fold in mocks, so mock-measured bias understated field bias for this taxon; this rests on one abstract, one primer pair and one taxon.
- "Mock bias did not transfer to the field" as a general result.
  Why: rests on one abstract-only study, for one primer pair (515F-Y/806R) and one taxon (SAR11)
  Say instead: For the 515F-Y/806R pair, SAR11 was under-represented about 4 to 10-fold in marine field samples but only about 2-fold in mocks, so mock-measured bias understated field bias for this taxon; this rests on one abstract, one primer pair and one taxon.
- "ddPCR versus flow cytometry correlated at only r = 0.50" (Galazzo 2020).
  Why: the full text reports qPCR versus flow-cytometry enumeration on faeces (Pearson r = -0.50); ddPCR correlated strongly with qPCR
  Say instead: qPCR and flow cytometry agreed on a whole-cell mock (|r| = 0.967) but gave "highly divergent" profiles for faeces, where qPCR against flow-cytometry enumeration correlated at Pearson r = -0.50; ddPCR correlated strongly with qPCR, which the authors used to rule out qPCR imprecision as the cause of the divergence. The divergence rests on this one study.
- "Unfiltered OTU tables were 50 to 80% spurious taxa."
  Why: the source says after OTU clustering and singleton removal
  Say instead: After OTU clustering and singleton removal, tables contained approximately 50% (mock communities) to 80% (gnotobiotic mice) spurious taxa; the authors propose a 0.25% relative-abundance cutoff, and the most abundant spurious taxon in mocks had a median relative abundance of 0.12%.
- "Mean Jaccard 0.80" for PCR replicates of negative extraction controls.
  Why: the source reports a mean Jaccard distance of 0.80; without "distance" the figure reads as high similarity
  Say instead: Replicates split before PCR differed strongly while replicates split after PCR were nearly identical; in negative extraction controls, most species appeared in only one of five PCR replicates, with a mean Jaccard distance of 0.80 (range 0.65 to 0.87).
- "30% of 16S amplicon papers report a negative control and 10% a positive control."
  Why: Hornung 2019's rates cover all high-throughput community sequencing types in two journals, not 16S only, and are a single source
  Say instead: Hornung 2019 surveyed 265 papers in the 2018 issues of Microbiome and The ISME Journal that used any high-throughput community sequencing (16S, shotgun, metatranscriptomics, ITS, 18S, virome, long-read and others): 30% (79) reported a negative control and 10% (27) a positive control. It is not a 16S-only figure, and it is a single source.
- "Multinomial or Poisson sampling explains much replicate disagreement in taxa detected", rated moderate "from several soil studies".
  Why: one 454 dataset of 24 Oklahoma soils and one laboratory; Wen 2017 does not fit the model, and its contrary depth plateau is missing
  Say instead: The evidence that Poisson or multinomial sampling explains replicate disagreement in taxa detected comes from one dataset and one laboratory: Zhou 2013 modelled the same 24 Oklahoma grassland soils, sequenced on 454, that Zhou 2011 reported, and Wen 2017 is from the same laboratory; Wen 2017's MiSeq replicates cut against pure sampling. That sampling alone explains replicate disagreement in taxa detected is weak and contested. / Zhou 2013 predicted about 60,900 reads for 90% OTU overlap, but in Wen 2017 unweighted overlap plateaued at 39% near 30,000 reads (with singletons) and reached only 43.9% at 160,000 reads; Wen's authors attribute rare-OTU variation to random sampling plus sequencing artefacts and report that "biases other than random sampling" affect unweighted metrics more.
- "Agreement in relative abundance rises with depth, roughly as a square root" as a general result.
  Why: rests on one caecal extract with four technical replicates (Barlow 2020)
  Say instead: For one caecal extract, the abundance at which the CV of a taxon's relative abundance between technical replicates reached 30% fell with the square root of read depth, as Poisson noise would predict; this rests on one caecal extract with four technical replicates.
- "Relative abundance is robust to the pipeline; counts of taxa are not."
  Why: generalises from Nearing 2018 (with Marizzoni 2020); Nearing 2018 itself reports that all pipelines markedly differed from expected composition on the Zymo mock, and Straub 2020 reports pipeline-dependent interpretations
  Say instead: In an independent benchmark, relative abundances of expected taxa within each mock were similar across DADA2, UNOISE3, Deblur and open-reference OTUs, while counts of units differed widely: open-reference clustering gave 453 OTUs on the HMP mock and 8,891 on the Extreme mock, and on one soil DADA2 gave 16,609 ASVs, UNOISE3 11,613, Deblur 8,270 and open-reference 21,297 OTUs; no pipeline recovered every expected sequence, and on the Zymo mock all pipelines "markedly differed" from expected composition. / mothur and QIIME1 returned 10 to 200 times the expected number of sequences, and Faith's PD was overestimated 1.3 to 2.7-fold by QIIME2, 2 to 18-fold by QIIME1 and 3.5 to 29-fold by mothur; the authors report pipeline-dependent interpretations.
- "Library preparation and primers are the largest drivers of error profile" without a single-source flag.
  Why: rests on Schirmer 2015 alone
  Say instead: Across 73 MiSeq datasets, library preparation method and primer choice were the most significant sources of bias, with distinct, motif-linked error patterns; this rests on Schirmer 2015 alone.
- "V4 genus accuracy is about 50% at 97% identity and reference databases carry 10 to 17% annotation error" without the single-source qualifier.
  Why: rests on Edgar 2018b and 2018c, from one author who also develops competing classifiers; flagged single in the text but used in the D2 answer without that qualifier
  Say instead: Cross-validated by identity to the reference, all tested classifiers were at most 50% accurate on V4: genus accuracy was about 100% at 100% identity and about 50% at 97%; the author argues that mocks overstate accuracy because all their members are named type strains. This rests on one author, who also develops competing classifiers. / Estimated annotation error is about 10% for RDP and about 17% for SILVA v128 and Greengenes 13.5, judged from conflicting labels on identical sequences.
- "Chimera formation is reproducible across amplifications" as an established consistency.
  Why: rests on Haas 2011 (Sanger and 454) alone
  Say instead: Chimeras formed reproducibly across independent amplifications of a known mixture; less-abundant species showed chimera rates above 70%, and chimera count correlated with organism abundance (R2 = 0.97) in a staggered mock; the reproducibility rests on this one study.
- "Fast-responding soil isolates average 5.5 copies against 1.4" as a general result.
  Why: rests on one abstract-only study (Klappenbach 2000)
  Say instead: Copy number tracks ecological strategy: soil isolates that formed colonies quickly averaged 5.5 copies and slow responders 1.4.
- "Willis 2019 is an assertion", and rarefying for richness is "contested by an assertion".
  Why: the paper gives statistical argument plus a worked simulated example; calling it an assertion against Schloss's modelled simulations understates the evidence against rarefying for richness
  Say instead: Willis argues that plug-in and rarefied richness are both negatively biased and that rarefying can create false differences between environments with equal richness but different abundance structures; she recommends estimators with variance estimates compared through measurement-error models. The paper gives statistical argument plus a worked simulated example, not assertion alone.
- "Spike-in totals agreed poorly with flow cytometry (r2 0.19)" (Lin 2019) as a failure without the authors' conclusion.
  Why: the authors conclude the internal-standard method is quantitative and consistent with flow cytometry; the review omits this (Common rule 6), and the r2 figure could not be verified
  Say instead: Seawater internal standards agreed with flow cytometry at r2 = 0.19 until corrections for copy number and particle association (with four outliers removed) raised it to 0.61; the authors conclude that the method "provided results consistent with ... total bacterial counts by flow cytometry" and "is quantitative".
- "The difference in load is the likely reason" for the pooled-versus-single PCR contrast, as a finding.
  Why: the reviewer's own reconciliation, untested and not marked as the reviewer's reading
  Say instead: That the difference in load is the likely reason for the pooled-versus-single PCR contrast is the reviewer's own reconciliation; no single study tested both conditions.
- "This determines whether a fixed correction can work" (whether bias is consistent across samples).
  Why: the reviewer's framing of what matters for analysis design, not a literature finding
- "Simulations disagree mainly because they build different data-generating processes into the truth" as an established finding.
  Why: only partly supported; phrased as the review's own causal diagnosis
  Say instead: That simulations disagree because they build different data-generating processes into the truth is partly supported (Weiss 2017, Hong 2022 and Schloss 2024a each say results depend on data-generating assumptions) and is the review's own causal diagnosis.
- The section 5.6 "Shown to correct" column as measured results.
  Why: its cells mix makers' claims and simulation results with measured results without per-cell evidence class, so it reads closer to a method recommendation than the brief allows
- "0.1 to 6% of reads move between samples" as a 16S index-misassignment rate.
  Why: the Table 1 row merges non-16S genome and exome libraries, Illumina's documentation, non-16S amplicons and 16S data without INDIRECT labels
  Say instead: Index misassignment rates are fractions of reads assigned to the wrong sample; they mainly create false presences of taxa, concentrated where abundant taxa from other samples leak in, and they vary with platform, library type and run. The 16S-specific evidence is thin: one preprint abstract and one plate study.
- "Water and hosts: copy-corrected rank-abundance data fit a lognormal" as one answer for both.
  Why: one study (Kembel 2012) pooling ocean and human skin into one item; the brief's separate water and host cases are folded together, and the paper's simulations assumed a lognormal
  Say instead: After copy-number correction, rank-abundance distributions from human skin and ocean fit a lognormal better; this single study pools ocean and skin into one item, and the same paper's simulations assumed a lognormal.
- "About 2.2" as the community copy number of water.
  Why: the EMP value pools free-living (soil, water, sediment) and plant-associated samples
  Say instead: Every environment-level copy-number value found is predicted from reference genomes, not measured: soil had the lowest abundance-weighted copy-number distribution in the Earth Microbiome Project; the EMP groups free-living (soil, water, sediment) and plant-associated samples together at about 2.2, with no separate value for water; animal-associated samples are predicted at about 3.4, with gut and saliva highest.
- Extraction bias is "consistent on the ratio scale" as one finding from a 16S cell mixture and a shotgun spike-in.
  Why: combines a 16S cell-mixture result and a secondary shotgun spike-in result, mixing measurement types
  Say instead: On the ratio scale, extraction bias was consistent across samples within a protocol in the vaginal mock: ratio-scale consistency is shown in one 16S cell-mixture dataset. / A 10-species shotgun spike-in also gave a consistent profile across faecal backgrounds, with protocol H showing up to 2,751-fold maximum pairwise bias; this is shotgun, not 16S, known only via McLaren 2019, and a different measurement type from the 16S cell-mixture result.
- Edgar 2017b (UNBIAS) as a "strong pessimistic claim" set aside as a single-source contrary result, while the pro-correction results stand unlabelled.
  Why: McLaren and Silverman each also rest on a single mock design and get no matching single-source label
  Say instead: A preprint by the tool's author reports essentially no correlation ("no meaningful correlation") between 16S read and species frequencies in mocks; correction for copy number and primer mismatch reached r of about 0.6 only in ideal cases (exact references), falling to about 0.4 at 97% and about 0.2 at 95% identity.
- "16S technical replicates are Poisson."
  Why: the note warns that the assumption rests on RNA-seq lane replicates, not on 16S technical replicates
  Say instead: The "technical replicates are Poisson" assumption comes from RNA-seq: Illumina lane replicates fit a Poisson model, with about 0.5% of genes deviating; McMurdie and Holmes adopt it for technical replicates, so it rests on RNA-seq, not on 16S technical replicates.
- "In bulk-soil amplicon data, 0.4 to 2% of taxa hold about 41 to 58% of reads."
  Why: pools a per-sample mean under a joint abundance-and-ubiquity definition (2%, 41%) with pooled global relative abundance (0.4%, 58%); the body says these must not be combined
  Say instead: The two dominant-share figures must be kept apart: about 41% for a top-10%-and-ubiquitous definition (per-sample mean) and about 58% for the 0.4% common class (pooled global relative abundance) use different definitions and denominators and are not comparable.
- "Bulk soil shows a positive abundance-occupancy relationship wherever tested."
  Why: two partly overlapping datasets whose metrics are partly circular; the search reviewed about 25 titles; the circularity caution was applied only to Delgado-Baquerizo
  Say instead: In the two bulk-soil amplicon studies with figures (Bickel and Or 2021; Nemergut 2011), more abundant taxa occupy more soils, but the two are not fully independent (Bickel and Or reanalysed compiled datasets including the Earth Microbiome Project, which plausibly overlaps Nemergut's soils), and both measures are partly built in by construction: "total abundance" summed across samples and "common" defined on the pooled rank-abundance distribution both rise with occupancy. Whether a relationship exists beyond sampling, and how strong it is, is unresolved.
- "Genome copies usually fall in stationary phase or starvation" as a property of prokaryotes.
  Why: rests largely on one laboratory's abstracts; folds taxon-specific and sometimes opposite behaviours into one trend; ploidy rises in stationary phase in A. vinelandii, and in M. acetivorans in slow growth
  Say instead: In cultures, genome copies per cell range from about one (Caulobacter, Wolinella, crenarchaea) to tens or hundreds (P. putida, haloarchaea, methanogens, Synechocystis) and depend on taxon, growth rate and phase; copy number does not change in one direction with growth phase. / Copy number does not always fall in stationary phase: Azotobacter vinelandii is reported to rise from about 4 copies in exponential phase to about 80 in stationary phase, and M. acetivorans from 2.5 to 5 (Bruck 2023 full text, secondary via the critic); Pecoraro 2011 Table 5 gives A. vinelandii as 1 (up to 8) copies in slow growth and 40 in fast growth, attributed to another laboratory.
- "No direct contradictions found" for the ploidy values.
  Why: Pecoraro 2011 Table 5, read in full, and Bruck 2023, an open full text, report contrary cases
  Say instead: Copy number does not always fall in stationary phase: Azotobacter vinelandii is reported to rise from about 4 copies in exponential phase to about 80 in stationary phase, and M. acetivorans from 2.5 to 5 (Bruck 2023 full text, secondary via the critic); Pecoraro 2011 Table 5 gives A. vinelandii as 1 (up to 8) copies in slow growth and 40 in fast growth, attributed to another laboratory. / Measurements outside the Soppa laboratory exist and are listed in Pecoraro 2011: Azotobacter (40 copies in fast growth), Desulfovibrio (9 to 17), Neisseria (3 to 4), Buchnera (120), and polyploid Deinococcus, Borrelia and rhizobial bacteroids.
- "Evidence on genome copies per cell is strong for cultures."
  Why: apart from Pecoraro 2011 all ploidy studies were read at abstract level and rest largely on one laboratory's qPCR method; moderate, not strong
  Say instead: In cultures, genome copies per cell range from about one (Caulobacter, Wolinella, crenarchaea) to tens or hundreds (P. putida, haloarchaea, methanogens, Synechocystis) and depend on taxon, growth rate and phase; copy number does not change in one direction with growth phase.
- "Independent replication of the ploidy values by other groups was not located."
  Why: the paper read in full (Pecoraro 2011) lists independent measurements (Azotobacter, Desulfovibrio, Neisseria, Buchnera, Deinococcus, Borrelia, rhizobial bacteroids)
  Say instead: Measurements outside the Soppa laboratory exist and are listed in Pecoraro 2011: Azotobacter (40 copies in fast growth), Desulfovibrio (9 to 17), Neisseria (3 to 4), Buchnera (120), and polyploid Deinococcus, Borrelia and rhizobial bacteroids.
- "16S copies per cell scale with origin number more than with genome number" as a finding.
  Why: the reviewer's inference from one abstract (Couturier and Rocha 2006), not labelled as such; no source measures it
  Say instead: That 16S copies per cell scale with origin number more than with genome number in fast growers is the reviewer's inference from one abstract; no source in the review measures 16S copies per cell against origin number.
- "In Prochlorococcus the share of cells carrying two genomes changes over the day."
  Why: the abstract read gives no share; it states only that replication occurred in the afternoon and division at night
  Say instead: In Prochlorococcus in the equatorial Pacific, DNA replication occurred in the afternoon, in phase with the light cycle, and division at night; the abstract read gives no share of cells.
- "No source reports, for any natural community, the share of cells carrying one genome copy versus more than one, by taxon" as established.
  Why: in situ flow cytometric cell-cycle analyses of Prochlorococcus are taxon-specific measurements of the share of cells with replicated DNA; the review read only the abstract
  Say instead: Flow cytometric cell-cycle analyses of Prochlorococcus (and Synechococcus) in situ are by method taxon-specific measurements of the share of cells with replicated DNA (G1 versus S/G2), so the review's statement that no such share exists for any natural community is not established; nothing comparable was found for soil. / That no natural community has a taxon-specific measurement of the share of cells by genome copy number is not established: in situ flow cytometric cell-cycle analyses of Prochlorococcus are by method taxon-specific measurements of the share of cells with replicated DNA, and the review read only their abstract. Nothing comparable was found for soil.
- "Other biases (extraction, primers) are of similar or larger size than copy-number bias and multiply with it" (McLaren 2019).
  Why: the McLaren abstract, the only part read, does not compare their magnitude with copy-number bias
  Say instead: Sequencing bias behaves as a consistent multiplicative factor per taxon, which can be corrected with calibration controls (McLaren 2019 abstract); the abstract does not compare the size of extraction and primer biases with copy-number bias.
- "Abundant is usually above 1%", citing Jia et al. 2022.
  Why: Jia 2022 uses a single rare/common cutoff and does not support "abundant above 1%"
  Say instead: Within-sample thresholds: rare is most often below 0.1% of reads per sample, sometimes below 0.01% or 0.001%, and abundant is usually above 1% (Lynch and Neufeld 2015, Galand 2009, Dai 2016); Jia et al. 2022 uses a single rare/common cutoff and does not support "abundant above 1%".
- "Only about 1% of taxa were agreed by all four core methods" as Custer's figure.
  Why: the source gives 165 and 176 taxa as 13% and 15.85% of core assignments; "about 1%" is the reviewer's derivation and should carry a derived label
  Say instead: Four core-microbiome methods compared on human faecal (319 samples) and Arabidopsis root (288 samples) data assigned 1.2% to 9.4% of taxa as core (nearly 10-fold), and 165 to 176 taxa were agreed by all four methods, which is 13 to 16% of core assignments; the review's "about 1% of taxa" is its own derivation.
- "Occupancy-based core methods performed best" as an established standard.
  Why: rests on one simulation study (Custer 2023)
  Say instead: Occupancy-based core methods were most accurate in simulations; this rests on one simulation study.
- "Two phylotypes dominate soil archaea" as a general finding.
  Why: rests on one abstract-only study (Bates 2011, 2010-era 454 data, 146 soils)
  Say instead: Across 146 soils, archaeal reads averaged 2% of 16S reads (0 to over 10%), and two Thaumarchaeota (then Crenarchaeota) phylotypes made up over 70% of archaeal sequences.
- "Low-abundance taxa are routinely recorded absent where present, which by itself produces lower occupancy for rarer taxa" as a finding of Zhou 2011.
  Why: generalises from one 454-era study at one site, and the second clause is the reviewer's inference, not drawn in Zhou's abstract
  Say instead: Low-abundance taxa are often recorded absent when present, because technical replicate soil libraries shared only 17.2% (two replicates) and 8.2% (three) of OTUs: this occupancy conclusion is the reviewer's argument, generalised from one 454-era study at one site whose abstract attributes the low overlap to random sampling but does not draw the occupancy conclusion.
- "Archaea carry 1 to 4 copies (to v5.0)" as the whole record.
  Why: Acinas et al. 2004 already report a maximum of five archaeal operons; the review's sources conflict and it does not flag this
  Say instead: Archaea carry 1 to 4 copies in rrnDB up to v5.0 and 1 to 5 from v5.6 (Natronorubrum, Natrinema, Methanococcoides, Methanolobus and others); Acinas et al. 2004 already reported a maximum of five archaeal operons, so the review's sources conflict on the archaeal maximum.
- "Acidobacteria average 1.0 copies" presented alongside large-n phyla without the n.
  Why: the mean rests on 4 genomes from 4 species, and the soil correction example depends on it
  Say instead: The Acidobacteria mean of 1.0 rests on 4 genomes from 4 species, and the rrnDB v5.10 Acidobacteriota mean of 1.4 on 29 species; these soil-relevant low values are imprecise.
- "Up to 41% of rRNA genes in soil are unlinked" without the single-source flag.
  Why: rests on Brewer 2020 alone (abstract only); the body flags this, the answer does not
  Say instead: 16S gene count and operon count diverge where rRNA genes are unlinked: unlinked 16S and 23S genes are common in Deinococcus-Thermus, Chloroflexi and Planctomycetes, and up to 41% of rRNA genes in soil long-read metagenomes were unlinked, against none in human gut.
- "The 1 to 15 range is consistent across independent sources" (replicated).
  Why: the sources draw on overlapping NCBI genome sets, so they are not independent replications
  Say instead: Bacterial genomes carry 1 to about 15 copies of the 16S rRNA gene in every database release and genome survey to about 2015: the first rrnDB release ("can vary from one to as many as 15 copies"), the 2009 release (785 bacterial and 69 archaeal strains) and the 2015 release, Acinas 2004 and Vetrovsky and Baldrian 2013.
- "Eleven DNA-based mock communities fitted 7.1% better without correction."
  Why: Starke 2021 computed its 7.1% on n = 10 mocks; one of the eleven was excluded
  Say instead: On 10 V4 mock communities, uncorrected data fit known composition 7.1% (SE 3.6%) better than copy-number-corrected data; one of the eleven mocks was excluded, and all were DNA-based (nine genomic DNA mixes) or cloned-gene mocks.

## Gaps

What the research did not establish.

- Same-sample comparisons of 16S amplicon data with shotgun metagenomic, culture-based, microscopy/FISH or taxon-specific qPCR measurements (nearest precedents named in the brief); the only shotgun evidence is Costea 2017, known secondarily via McLaren.
- Field sampling and preservation choices for water (volume filtered, filter pore size, prefiltration, filter storage) and for host tissue (swab versus biopsy versus lavage, plant tissue surface sterilisation): unsearched on the review's own Search record.
- The note contradicts itself on field sampling for water and host tissue: section 2.1 says "The lab angle searched preservation and storage terms through Crossref, Europe PMC and web search", while the Search record says "Water-sampling and host-tissue sampling choices (not searched by any angle)".
- Long-read platforms: Nanopore (ONT) full-length 16S is absent, PacBio full-length evidence is only the developer's own claim, and there are no independent long-read mock benchmarks.
- 16S-specific index hopping on Illumina patterned flow cells (NovaSeq, NextSeq 2000); the 16S rate is one preprint abstract.
- Within-run read-count variation per sample after pooling, and the correlation of library size with biomass; Schloss 2024b cites two primary studies on this (Minich et al. 2022 on 101 fish species; Cruz et al. 2021 on an equivolumetric protocol), known only secondarily and not opened.
- Measured community-average 16S copy number by environment, for example from shotgun metagenomes (16S reads normalised to single-copy marker genes): not searched, so "not found" rests on prediction-only sources.
- Absolute per-cycle amplification efficiency of universal 16S primers on soil, sediment, water and faecal extracts: the qPCR methods literature (per-reaction efficiency from amplification curves, inhibition in environmental extracts) was not searched.
- Species abundance distributions in marine and freshwater and in host-associated 16S datasets: Grilli 2020's per-biome supplementary figures and Shoemaker 2017's full text were not read.
- Dirichlet-multinomial or overdispersion fits to 16S technical replicates, and technical replicates across depths in aquatic, plant and human non-gut samples.
- Contaminant-removal tools beyond decontam and SourceTracker (for example tools modelling well-to-well leakage), and independent benchmarks of decontam's prevalence mode.
- Compositional beta-diversity variants (robust Aitchison, phylogenetic isometric log-ratio) and microbiome scaling methods such as GMPR and ANCOM-BC2, benchmarked from primary sources; coverage relies on Yang and Chen 2022 and Llorens-Rico 2021.
- Any D5 approach benchmarked in soil or water with measured absolute loads as truth, and a known-richness mock tested across depths.
- Archaea-rich environments (marine, sediment, methanogenic reactors): archaeal-specific primer bias against known composition is absent.
- An independent microbial amplicon benchmark of coverage-based standardisation with known truth.
- MB-01's stage 2 check is triggered: a follow-up brief targeting per-cycle efficiency, metagenome-measured community copy number, 16S index hopping on patterned flow cells, within-run read-count variation against load and long-read platform error is not yet written.
- MB-01's two angles report different Kozich 2013 error rates after preclustering for partially overlapping regions (V3-V4 0.10 to 0.21% and V4-V5 0.36 to 0.64%, against 0.24 to 0.37% and 0.58 to 0.87%).
- Zhou 2011's discussion gives replicate OTU overlaps of 13.1% and 5.9%, which differ from its abstract's 17.2% and 8.2%; the discussion values could not be confirmed.
- Polyploidy of cultured soil and plant-associated bacteria measured outside the Soppa laboratory: Azotobacter vinelandii (40 to 80 copies, rising in stationary phase), Deinococcus radiodurans, and endoreduplicated Sinorhizobium bacteroids in nodules (Mergaert et al. 2006).
- Single-cell genome-copy distributions in cultures (classic flow-cytometric chromosome run-out work giving per-cell distributions of 1, 2, 4 and 8 chromosomes, for example Skarstad, Boye and Steen 1986, and Caulobacter swarmer-cell G1 shares): the direct measurements of the share of cells at one genome copy versus several, not searched.
- In situ taxon-specific DNA-content distributions of marine picocyanobacteria (Prochlorococcus and Synechococcus cell-cycle analyses, Vaulot 1995 and successors), read only at abstract level.
- Ploidy of dormant and sporulated forms (endospores, Streptomyces spores, Azotobacter cysts) and of non-growing small soil cells.
- In situ growth state of soil taxa: qSIP growth rates and soil and rhizosphere growth-rate potential from genomes (Chuckran et al. 2025 on rewetted soil; Lopez et al. 2023 on rhizosphere versus bulk soil, which also reports 6.6% more rRNA operons in rhizosphere bacteria via a cited study); no replication indices for soil metagenomes were found.
- Soil studies using community-weighted rrn copy number (for example Nemergut et al. 2016 on succession) and soil absolute quantification (for example Smets et al. 2016), not searched for MB-02's copy-number or soil-abundance answers.
- Occupancy-based classification terms: habitat generalist versus specialist (Levins niche breadth, for example Szekely and Langenheder 2014), cosmopolitan versus endemic, and the microbial core-satellite partition (for example van der Gast et al. 2011).
- The soil literature contrasting abundant and rare subcommunities' distribution ranges and niche breadth across regions (for example Jiao and Lu 2020; Jiao, Chen and Wei 2017), which bears on abundance versus occupancy and on threshold usage in soil.
- Global genome-resolved or metagenome-based soil datasets (for example Bahram et al. 2018, used by Bickel and Or) examined for taxon abundance distributions or occupancy.
- Taxon-specific cell counts in soil (CARD-FISH or FISH phylum or class shares): not searched beyond SAD-specific queries.
- Non-soil nearest precedents for the shape of the abundance distribution that contradict the lognormal view (for example power-law tails of non-dominant plankton, Ser-Giacomi et al. 2018).
- Explicit sampling or occupancy-detection models applied to soil microbes (site-occupancy models, or gamma-Poisson occupancy predictions on soil data), and whether Grilli 2020's datasets include soil.
- Technical-replicate detection studies after the 454 era (Illumina, deeper sequencing) in soil, to test whether Zhou 2011's low overlap generalises.
- MB-02's stage 2 check is triggered: the critic names unsearched per-cell and growth-state evidence for soil; the follow-up brief is not written, and the owner decides.
- MB-02's D3(a) answer contradicts its body: the answer says "a small fraction of taxa (0.4 to 2% by the two definitions) holds about 41 to 58% of reads", while the body says "The dominant shares in [60] and [61] use different definitions and denominators and are not combined here".
- Custer 2023's text is internally inconsistent on whether core analyses gained or lost the temporal effect in the human data.
- Nemergut 2011's bulk-soil figures (28% against 2%, 69% against 8%) could not be verified and should be rechecked.
- The high rrnDB maxima (21 to 22 copies in bacteria) and the current shares have no published check against assembly quality.
- A mean copy figure in Pei et al. 2010 (2.22 ± 0.81) whose meaning was unclear from the abstract; not used.
