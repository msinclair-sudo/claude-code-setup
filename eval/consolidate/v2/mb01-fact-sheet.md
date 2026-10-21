# MB-01 fact sheet: 16S sample to count table, depth and rarefaction

Source: the MB-01 literature review note (vault, Topics/Biology/Research/Results). Critique block lines 1-241 overrides the body. Access labels as the note gives them: FT full text, AB abstract only, SEC secondary, plus PREPRINT / DOCUMENTATION / PROTOCOL where tagged. **[C]** = the critic corrected or weakened this claim. Arithmetic marked "(my arithmetic)" is mine, not the note's.

## 1. Critic corrections

1. **Hornung 2019 controls.** Review: 30%/10% of papers reported negative/positive controls, read as 16S practice. Right: 265 papers in 2018 issues of *Microbiome* and *ISME J* using any high-throughput community sequencing; 30% (79) negative, 10% (27) positive; not 16S-only; single source.
2. **Water and host sampling.** Review: "searched, not found" in 2.1. Right: no angle searched them (the Search record says so). Unsearched.
3. **"Departures at every step."** Right: departures measured at most steps examined; several choices showed little or no effect (PCR replicate pooling, day and lane, cycle number in some studies, soil storage).
4. **Extraction > PCR > sequencing ordering**, rated "strong", "many independent mocks". Right: one 7-taxon vaginal dataset (Brooks 2015 reanalysed by McLaren 2019); contested by Fouhy 2016, qualified by MBQC (specimen type mattered more). Single dataset.
5. **McLaren calibration (Bray-Curtis 0.35 to 0.08).** Review: "in a shotgun dataset". Right: from the Brooks 16S cell mixtures (2 calibration, 69 calibrated samples; 92.6% lower MSE). The Costea shotgun calibration is reported only qualitatively.
6. **Parada 2016 SAR11 (4-10-fold field vs about 2-fold mock).** Review: original 515F/806R. Right: 515F-Y/806R.
7. **Galazzo 2020.** Review: ddPCR vs flow r = 0.50. Right: qPCR vs flow cytometry on faeces, r = -0.50; ddPCR correlated strongly with qPCR.
8. **Reitmeier 2021 50-80% spurious taxa.** Review: "unfiltered". Right: after OTU clustering and singleton removal.
9. **Dyrhovden 2021 "mean Jaccard 0.80".** Right: mean Jaccard *distance* 0.80 (range 0.65-0.87), i.e. high dissimilarity between PCR replicates of negative controls.
10. **Lin 2019.** Review lists r2 0.19 as a failure mode. Right: the authors conclude the internal-standard method "is quantitative" and consistent with flow cytometry; r2 0.19/0.61 could not be verified.
11. **Willis 2019.** Review: "asserted". Right: statistical argument plus a worked simulated example; the review weighed it unevenly against Schloss's simulations.
12. **Sampling explains replicate disagreement** ("moderate", "several soil studies"). Right: one 454 dataset (Zhou 2011/2013, same 24 soils). Wen 2017 (same lab) cuts against it: overlap plateaued at 39% near 30,000 reads, 43.9% at 160,000, not Zhou's predicted 90% at about 60,900; authors invoke "biases other than random sampling" and a run effect. Weak and contested.
13. **Square-root decline of CV with depth.** Single source: one caecal extract, four replicates (Barlow 2020).
14. **"Relative abundance is robust to the pipeline."** Overgeneralised from Nearing 2018, which itself says all pipelines "markedly differed" from the Zymo mock; Straub 2020 reports pipeline-dependent interpretations.
15. **Schirmer 2015 "library prep and primers largest drivers of error profile".** Single source, unflagged in Table 1.
16. **Edgar 2018b/c classifier accuracy and database error.** Single author who develops competing classifiers.
17. **Chimera formation reproducible.** Haas 2011 alone (Sanger and 454).
18. **Klappenbach 2000 (5.5 vs 1.4 copies).** One abstract-only study.
19. **"Mock bias did not transfer to the field."** Parada 2016 abstract, one primer pair, one taxon.
20. **Access labels.** "FT" for Zhou 2011, Kozich 2013, Haegeman 2013, Lin 2019, Kennedy 2014 not confirmable; Zhou 2011's 17.2%, 8.2%, 66.7-fold are abstract figures. Unconfirmable: Zhou 2011's 0.06-5.34% and 13.1%/5.9%, Kozich's 9,913 and 2,454 reads, Haegeman's 26,079/2,880, Lin's r2 values.
21. **Zhou 2013 soil SAD "exponential or inverse gamma".** In supplementary Table S3, not stated in the main text, unverified.
22. **Kembel 2012 lognormal.** Pools ocean and skin; the same paper's simulations assumed lognormal.
23. **EMP copy number about 2.2 offered for water.** Pools free-living (soil, water, sediment) and plant-associated samples.
24. **Merged cases.** Index-misassignment "0.1 to 6%" mixes non-16S libraries and Illumina documentation with 16S data; extraction "consistent on ratio scale" mixes a 16S cell mixture with a secondary shotgun spike-in (Costea 2017).
25. **Uneven labels.** UNBIAS (Edgar 2017b) set aside as single-source while McLaren and Silverman, also single mock designs, are not; Jian 2020's "near-perfect" agreement compares methods sharing a qPCR upstream.
26. **Scope drift.** "Simulations disagree mainly because of different data-generating processes" and "load difference is the likely reason" are the reviewer's readings; the 5.6 summary table mixes makers' claims with measurements.
27. **Coverage-based iNEXT** (verified): in Schloss 2024b all approaches "except for rarefaction and possibly the size-based iNEXT estimates" stayed depth-correlated.
28. **Reference errors** (minor): Frostegard 1999 third author is Vincent Ramisse; consortium positions in MBQC and Brooks; Thompson 2017 list truncated.

Critic's overall grade for D2: strong qualitatively; moderate for inflation of taxon counts; weak for per-step relative-abundance magnitudes and for consistency across samples.

## 2. Per step

**Sampling and storage**
- Unpreserved or 70%-ethanol faeces at ambient temperature for 8 weeks shifted as much as between-person differences; 95% ethanol, FTA, OMNIgene about technical-replicate level. Song 2016, 10.1128/mSystems.00021-16, FT: "comparable to differences between individual humans".
- Soil storage (1-14 days, RT/4 C/-20 C) changed one soil, most at 3-7 days, least frozen, small next to >500 EMP soils. Rubin 2013, 10.1371/journal.pone.0070460, FT.
- Soil mass extracted (0.25-100 g) changed structure and OTU counts; 10 g gave highest diversity, lowest dispersion. Penton 2016, 10.3389/fmicb.2016.00824, FT; single source.
- Water and host-tissue sampling: unsearched. [C]

**DNA extraction**
- In a 7-taxon mock, extraction was the largest step: max 36.6-fold, mean 5.5-fold pairwise bias. McLaren 2019, 10.7554/eLife.46923, FT (re-opened). [C: single dataset, not field-wide]
- Harder bead beating raised Gram-positive DNA by up to 400% in activated sludge. Albertsen 2015, 10.1371/journal.pone.0132783, FT.
- Contrary: two gut extraction methods gave "very similar" data. Fouhy 2016, 10.1186/s12866-016-0738-z, FT.
- Extraction yield of a spike-in varied 40-84% between samples. Zemb 2020, 10.1002/mbo3.977, FT.
- Soil relic DNA averaged 40% of DNA, inflating richness by up to 55% (Carini 2016, 10.1038/nmicrobiol.2016.242, AB), versus minimal effect across soil, sediment, water, gut (Lennon 2018, 10.1128/mBio.00637-18, FT). Contested.

**Primers and region**
- 175 primers and 512 pairs "differ widely in coverage and phylum spectrum". Klindworth 2013, 10.1093/nar/gks808, FT.
- SAR11 bias about 4-10-fold in marine field samples vs about 2-fold in mocks, for 515F-Y/806R. Parada 2016, 10.1111/1462-2920.13023, AB. [C: primer pair corrected; one taxon]
- Added degeneracy improved Thaumarchaeota and SAR11 detection in stool, soil and built-environment sets. Walters 2016, 10.1128/mSystems.00009-15, FT.

**PCR**
- With mismatch removed, log-ratios changed linearly with cycle number (10-35); after 35 cycles average bias factor 2.6 (95% credible 2.3-2.9); about 19% of taxa >4-fold off. Silverman 2021, 10.1371/journal.pcbi.1009113, FT; single source (verified by critic).
- Two-template mixtures "converged toward 1:1" regardless of start (reannealing). Suzuki 1996, 10.1128/aem.62.2.625-630.1996, AB.
- GC content correlated negatively with observed abundance. Laursen 2017, 10.3389/fmicb.2017.01934, FT.
- In stool, sample explained R2 0.79, cycles 0.044, polymerase 0.033; "this bias was inconsistent for human stool samples". Sze 2019, 10.1128/mSphere.00163-19, FT (re-opened).
- Bounding: 30 vs 35 cycles "changed proportions only slightly" (Brooks 2015, 10.1186/s12866-015-0351-6, FT); single vs triplicate PCR no significant difference (Marotz 2019, 10.2144/btn-2018-0192, AB).

**Copy number**
- Bacteria 1-15 copies, archaea 1-4 (from only 148 species). Stoddard 2015, 10.1093/nar/gku1201, FT.
- Correction in forest soil moved Acidobacteria from 50.1% of sequences to 66.0% of genomes; Firmicutes 3.2% to 1.1%. Vetrovsky 2013, 10.1371/journal.pone.0057923, FT.
- Copy number explained about 60% of PCR bias but about 10% of total bias (7 taxa). McLaren 2019, FT; single source.
- Correction made fit worse: uncorrected data fit 10 V4 mocks 7.1% better. Starke 2021, 10.1007/s00248-020-01586-7, FT.
- Predictions accurate only within about 15% divergence of a sequenced genome; about 49% of SILVA-tree OTUs exceed that. Louca 2018, 10.1186/s40168-018-0420-9, FT.

**Library prep and indexing**
- Library prep and primer choice were the most significant bias sources across 73 MiSeq datasets. Schirmer 2015, 10.1093/nar/gku1341, FT. [C: single source]
- Two-step design: 25 amplicon + 8 index cycles, 12.5 ng input (Illumina 16S guide, DOCUMENTATION, maker's claim); EMP one-step 35 cycles in triplicate, 240 ng pooled (EMP protocol, PROTOCOL).
- Well-to-well contamination arose mainly at extraction, less at library prep, mostly into neighbouring wells. Minich 2019, 10.1128/mSystems.00186-19, FT.

**Sequencing**
- Within one study, reads per sample varied up to about 100-fold; Schloss attributes it to "compounding random error when PCR products are pooled". Schloss 2024b, 10.1128/msphere.00354-23, FT (re-opened).
- Schloss cites studies where depth correlates positively with biomass despite normalisation. Schloss 2024b, SEC (primaries not opened). [C: flagged as gap]
- Raw MiSeq V4 error rose with cluster density, 0.25% to 1.08%. Kozich 2013, 10.1128/AEM.01043-13, FT. [C: FT unconfirmable]

**Demultiplexing and index misassignment**
- Patterned flow cells: 0.2-6% in every run, about 10-fold lower on MiSeq; unique dual indexes cut 0.89% to 0.13%. Costello 2018, 10.1186/s12864-018-4703-0, FT, INDIRECT (non-16S).
- 16S, GAIIx and 11 MiSeq runs: about 2% of reads. Edgar 2016a, 10.1101/088666, AB, PREPRINT.
- 16S plates: barcode leakage negligible. Minich 2019, FT.
- Misassignment "mainly create[s] false presences of taxa". Review synthesis. [C: rate row merges non-16S sources]

**Quality filtering and merging**
- Min length, quality threshold and abundance filter strongly affected alpha diversity and composition; 0.005% abundance filter recommended. Bokulich 2013, 10.1038/nmeth.2276, FT.
- Contrary: stringent UPARSE-style filtering "could significantly underestimate abundance and diversity". Kopylova 2016, 10.1128/mSystems.00003-15, FT.

**Denoising and clustering**
- Expected-taxon relative abundances similar across DADA2, UNOISE3, Deblur, open-ref; counts of units differed widely. Nearing 2018, 10.7717/peerj.5364, FT. [C: overgeneralised; Zymo mock "markedly differed"]
- mothur and QIIME1 returned 10-200 times the expected number of sequences. Straub 2020, 10.3389/fmicb.2020.550420, FT.
- About 50% (mocks) to 80% (gnotobiotic mice) spurious taxa after OTU clustering and singleton removal. Reitmeier 2021, 10.1038/s43705-021-00033-z, FT. [C: not "unfiltered"]
- OTU vs ASV richness direction conflicts: OTU about half of ESV in leaf litter (Glassman 2018, 10.1128/mSphere.00148-18, FT) vs ASV about half of OTU in sediments (Chiarello 2022, 10.1371/journal.pone.0264443, FT).

**Chimeras**
- At 30 cycles, 0.9% (Accuprime) to 18.2% (Platinum) chimeric; UCHIME sensitivity 50-87% at 25+ cycles. Sze 2019, FT (verified).
- Less-abundant species showed chimera rates above 70%; formation reproducible across amplifications. Haas 2011, 10.1101/gr.112730.110, FT. [C: sole source for reproducibility; 454/Sanger]
- Error-free chimera prediction "impossible in principle". Edgar 2016b, 10.1101/074252, AB, PREPRINT, developer claim.

**Taxonomic assignment**
- V4 genus accuracy about 100% at 100% identity to reference, about 50% at 97%. Edgar 2018b, 10.7717/peerj.4652, FT. [C: single author]
- Mocks: q2-feature-classifier median genus F > 0.8. Bokulich 2018, 10.1186/s40168-018-0470-z, FT, developer claim. Edgar argues mocks overstate accuracy (named type strains).
- Annotation error about 10% RDP, about 17% SILVA v128 and Greengenes 13.5. Edgar 2018c, 10.7717/peerj.5030, FT. [C: single author]

**Contaminants and negative controls**
- Contaminants dominated by about 10^3 input cells, more at 40 than 20 cycles; kit- and lab-specific. Salter 2014, 10.1186/s12915-014-0087-z, FT.
- Diluted mock: contaminant reads 0.1% to 80.1%, ASVs 18 to 381; deleting everything seen in the negative control removed >20% of true sequences; decontam frequency mode removed 70-90% of contaminants. Karstens 2019, 10.1128/mSystems.00290-19, FT.
- Controls reported in 30% (negative) and 10% (positive) of papers. Hornung 2019, 10.1093/femsec/fiz045, FT. [C: all sequencing types, two journals]

## 3. Numbers usable as simulation parameters

- **PCR cycles.** 35 (EMP, PROTOCOL); 25 + 8 index (Illumina guide, DOCUMENTATION); experiments 10-35 (Silverman 2021, FT), 15/20-35 (Sze 2019, FT), 20 vs 40 (Salter 2014, FT), 24 (Laursen 2017, FT).
- **Per-cycle efficiency.** No absolute per-cycle efficiency for 16S primers on environmental templates found (lab angle; critic: qPCR kinetics literature not searched). Relative only: Silverman 2021 *inferred* taxon-specific log-ratio slopes per cycle from a mock run at several cycle numbers (FT, single); average 2.6-fold after 35 cycles, one pair (B. longum : E. faecalis) about 16-fold. Illustrative only (my arithmetic): 2.6^(1/35) ≈ 1.028, about 3% relative efficiency difference per cycle; 16^(1/35) ≈ 1.08. Kelly 2019 (10.1038/s41598-019-48546-x, FT, INDIRECT eukaryotic eDNA) drew efficiencies from beta distributions fitted to mocks, model starting copies × (1 + a_i)^cycles.
- **Copy number.** 1-15 bacteria, 1-4 archaea (Stoddard 2015, FT). Mean 4.2 over 1,690 genomes; phylum means Acidobacteria 1.0, Actinobacteria 3.1, Bacteroidetes 3.5, Firmicutes 5.8 (Vetrovsky 2013, FT; genome collection skewed). No median given. Community averages, predicted only: about 2.2 free-living + plant, about 3.4 animal-associated, soil lowest (Thompson 2017, 10.1038/nature24621, FT, single) [C: 2.2 is not a water value]. Fast soil colonisers 5.5 vs slow 1.4 (Klappenbach 2000, 10.1128/AEM.66.4.1328-1333.2000, AB) [C]. Stoddard warns that means mislead.
- **Reads per sample.** EMP mean 80,000 over 27,751 samples, rarefied to 5,000 (Thompson 2017, FT). One 360-sample MiSeq run: mean 9,913 pairs, 95% above 2,454 (Kozich 2013) [C: unconfirmable]. Within-study ranges, Schloss 2024b (FT, per study not per run), fold spread my arithmetic: human 10,439-422,904 (median 32,452, n = 490; about 41×), bioethanol 3,690-356,027 (about 96×), mice 1,804-30,311 (about 17×), soil 46,622-58,935 (n = 18; about 1.3×), marine 132,895-256,758 (n = 7; about 1.9×). Karstens 2019 run 40,927-251,419 (about 6×). Prodan 2020 (10.1371/journal.pone.0227434, FT) three mock runs 36,464-146,653 pairs. Makers: >20 million per MiSeq v3 run, >100,000 per sample at 96-plex (DOCUMENTATION). **No within-run CV after equimolar pooling found.**
- **Abundance distributions.** Mean abundances lognormal "for all the data sets considered"; each taxon's abundance across communities gamma, variance ∝ mean² (Grilli 2020, 10.1038/s41467-020-18529-y, FT partly re-opened). Lognormal across >20,000 samples (Shoemaker 2017, 10.1038/s41559-017-0107, AB). Soil: exponential or inverse gamma in 24 grassland soils (Zhou 2013, 10.1128/mBio.00324-13, FT) [C: supplementary, unverified]. Brazil soil, 26,079 reads and 2,880 species, fitted equally by 10^4, 10^5, 10^6 species (Haegeman 2013, 10.1038/ismej.2013.10, FT) [C: unconfirmable]. Between-sample overdispersion: Dirichlet-multinomial theta 0.047 and 0.054, oral plaque (La Rosa 2012, 10.1371/journal.pone.0052078, FT).
- **Index misassignment.** 0.2-6% patterned flow cells, about 10× lower MiSeq (Costello 2018, FT, INDIRECT); 0.1-2% (Illumina page, DOCUMENTATION); 0.51-0.76% GAIIx (Kircher 2012, 10.1093/nar/gkr771, FT, INDIRECT); 0.24%, 0.03% after index-quality filtering (Wright 2016, 10.1186/s12864-016-3217-x, FT, INDIRECT); about 2% 16S (Edgar 2016a, AB, PREPRINT); negligible on 16S plates (Minich 2019, FT).
- **Chimeras.** 0.9-18.2% of reads at 30 cycles by polymerase (Sze 2019, FT); >70% for rare species, 454 (Haas 2011, FT).
- **Soil taxa counts.** One soil: DADA2 16,609 ASVs, UNOISE3 11,613, Deblur 8,270, open-reference 21,297 OTUs (Nearing 2018, FT). Soil technical replicates shared 17.2% of OTUs (two) and 8.2% (three) on 454 (Zhou 2011, 10.1038/ismej.2011.11, AB-derived [C]); 33.4% and 20.2% on MiSeq (Wen 2017, 10.1371/journal.pone.0176716, FT).
- **Other.** Microbial load: up to 10× among healthy faeces (Vandeputte 2017, 10.1038/nature24460, AB); 27× among Antarctic seawater stations (Lin 2019, 10.1128/AEM.02634-18, FT [C]); >6 orders of magnitude across mouse gut sites (Barlow 2020, 10.1038/s41467-020-16224-6, FT). Spike recovery 0.06-5.34% for a 0.1% spike across soils, 66.7× (Zhou 2011) [C: 66.7× is in the abstract; the 0.06-5.34% range is not confirmable]. Per-strain CV across five runs median 11.8% (5.5-73.7%) (Laursen 2017, FT).

## 4. Depth, richness and rarefaction

**Observed richness rises with depth.** Chao1, ACE, CatchAll, Shannon, Simpson all varied with library size (Gihring 2012, 10.1111/j.1462-2920.2011.02550.x, AB). Observed richness, Chao1, ACE, breakaway, SRS-normalised richness all correlated with depth; Shannon less so; inverse Simpson not (Schloss 2024b, FT, modelled). Soil replicate presence/absence overlap rose from 20.7% at 2,000 reads to 43.9% at 160,000 (Wen 2017, FT). Reaching 95% and 99% Good's coverage took about 3× and 101× the reads needed for 90% (Schloss 2024b).

**Alpha diversity.** Schloss separates *rarefying* (one subsample) from *rarefaction* (mean over many). In his null models only rarefaction removed the depth correlation and held 5% false positives when depth was confounded with group; it also had the highest power (Schloss 2024b). Caveat from the review: the null model reassigns sequences at random, so taxon bias, technical variance beyond counting and load are absent from the truth. Against: Willis 2019 (10.3389/fmicb.2019.02407, FT) argues rarefied and plug-in richness are both negatively biased and rarefying can create false differences between equally rich environments with different abundance structures [C: argument plus simulated example, not assertion]. Richness tails cannot be identified from sample data; Chao's estimator ranked a community with 20× fewer species as having 10× more (Haegeman 2013). Chao1 and ACE invalid on singleton-free ASV tables (Deng 2024, 10.1093/ismejo/wrae106, FT). Multiplicative bias can make uneven samples look more even (McLaren 2019, modelled).

**Beta diversity.** For: Jaccard and Bray-Curtis from raw counts, proportions, CSS, SRS, Aitchison (four zero-handling variants) and VST all stayed depth-correlated; only rarefaction removed it and held 5% PERMANOVA false positives (Schloss 2024b). Rarefying clustered better for presence/absence metrics; other normalisations vulnerable below about 1,000 reads (Weiss 2017, 10.1186/s40168-017-0237-y, FT). Against: rarefying to the 15th percentile reduced clustering accuracy (McMurdie and Holmes 2014, 10.1371/journal.pcbi.1003531, FT); Schloss 2024a (10.1128/msphere.00355-23, FT) lists 11 design choices disadvantaging rarefying, notably low-depth samples removed only in the rarefied arm. Real data: rarefying barely changed Bray-Curtis/Jaccard (r > 0.9) (Chiarello 2022); metric choice mattered more than normalisation (Thorsen 2016, 10.1186/s40168-016-0208-8, AB). Rarefying once adds variance that grows as rarefied depth shrinks (Cameron 2021, 10.1038/s41598-021-01636-1, FT).

**Differential abundance.** Rarefied counts and proportions gave high false positives; DESeq2 and edgeR near zero (McMurdie and Holmes 2014). Rarefying did not raise FDR for most methods and lowered it at about 10× library-size differences, at a sensitivity cost (Weiss 2017). Rarefying plus permutation controls type I error (Hong 2022, 10.1093/bioinformatics/btac127, FT). At tenfold depth differences, proportion tests had severe type I inflation that rarefying controlled; no method "simultaneously robust, powerful, and flexible" (Yang and Chen 2022, 10.1186/s40168-022-01320-0, FT). Fourteen methods on 38 datasets gave 0.8% to 40.5% significant ASVs (Nearing 2022, 10.1038/s41467-022-28034-z, FT).

**What rarefying cannot correct.** It "does not touch bias or load" (review summary table). Wrench's makers: library-size scaling and rarefaction cannot correct compositional bias uncorrelated with library size (Kumar 2018, 10.1186/s12864-018-5160-5, AB). Fold changes in proportions are not invariant to multiplicative bias and can change sign; ratios are invariant (McLaren 2019). Proportion-based DA errs when community mean efficiency tracks the condition (McLaren 2022, 10.1101/2022.08.19.504330, AB, PREPRINT). PCR bias and copy number act before sequencing, so equalising depth leaves them in place.

**Alternatives, kept separate.**
- *Coverage-based rarefaction:* argued less biased for richness ratios in ecology (Chao and Jost 2012, 10.1890/11-1952.1, FT, INDIRECT); extrapolation reliable to about 2-3× sample size (Chao 2014, 10.1890/13-0133.1, FT, INDIRECT); "does not respond predictably" on terrestrial inventories (Alroy 2026, 10.1002/oik.11607, AB, INDIRECT); stayed depth-correlated in the only microbial test (Schloss 2024b) [C: verified].
- *Repeated rarefaction:* Schloss's "rarefaction" (above); Cameron 2021.
- *Log-ratio / compositional:* data are compositions "at all stages" (Gloor 2017, 10.3389/fmicb.2017.02224, AB). The note does not name CLR. Aitchison distances stayed depth-sensitive under Schloss's null. ALDEx2 and ANCOM-II most consistent (Nearing 2022). Reference frames make rankings invariant to load (Morton 2019, 10.1038/s41467-019-10656-5, AB).
- *Absolute load (spike-ins, qPCR, flow, dPCR):* reversed relative trends in faeces (Vandeputte 2017, AB); absolute abundance held or rose while relative fell, in soil (Tkacz 2018, 10.1186/s40168-018-0491-7, FT); total 16S qPCR × relative abundance matched taxon qPCR (Jian 2020, 10.1371/journal.pone.0227285, FT) [C: shared upstream]. Limits: taxon-specific bias remains (McLaren 2019); qPCR and flow diverged on faeces (Galazzo 2020, 10.3389/fcimb.2020.00403, FT) [C]; spike-in yield 40-84% (Zemb 2020); synthetic spike-ins differ in detection efficiency (Tourlousse 2017, 10.1093/nar/gkw984, FT). In simulation, experimental quantitative profiling beat computational transformations (Llorens-Rico 2021, 10.1038/s41467-021-23821-6, FT).

## 5. Where the evidence conflicts / not measured

**Conflicts**
- Bias composition-dependent (Brooks 2015) vs ratio-consistent (McLaren 2019), same data.
- Cycle number: small effect (Sipos 2007, Acinas 2005, Brooks 2015) vs growing bias (Suzuki 1996, Silverman 2021, Sze 2019 mock).
- Extraction size: Fouhy 2016 vs Albertsen 2015, McLaren/Brooks.
- Copy-number correction: Kembel 2012 (modelled) vs Starke 2021, Louca 2018, McLaren 2019.
- Mock bias transfers to field: Parada 2016 vs calibration claims.
- Replicate variation from sampling (Zhou 2013, Grilli 2020) vs technical variance beyond counting (Silverman 2018, 76%; Wen 2017; Dyrhovden 2021).
- Rarefying: McMurdie and Holmes 2014 vs Schloss 2024a/b, Weiss 2017, Hong 2022; Willis 2019 against for richness. Proportions for beta: McKnight 2019 vs Schloss 2024b.

**Not measured / not found**
- Absolute per-cycle 16S efficiency on environmental templates.
- Within-run CV of reads per sample after equimolar pooling.
- Measured (not predicted) community copy number in any environment.
- 16S-specific index hopping on patterned flow cells.
- Overdispersion fitted to 16S technical replicates.
- Independent microbial benchmark of coverage-based standardisation.
- Any D5 benchmark with taxon bias and load differences both in the simulated truth (Llorens-Rico 2021 had load but no taxon bias); no soil or water benchmark with measured loads as truth; no known-richness mock across depths.
- No soil-matrix mock of known composition; extraction-bias consistency across real soils unmeasured.
- Water and host sampling choices: unsearched.

## 6. Claims an explainer should not make

1. **"PCR bias is consistent across samples, so it cancels."** Ratio-scale consistency rests on one 7-taxon dataset; proportion error "varied dramatically in both magnitude and direction" even there (McLaren 2019); stool showed inconsistent cycle effects (Sze 2019); mock SAR11 bias understated field bias (Parada 2016).
2. **"Extraction is the biggest distortion, then PCR, then sequencing."** Single dataset; Fouhy 2016 contrary; MBQC ranks specimen type first. [C]
3. **"Rarefying fixes unequal depth."** At most it removes depth dependence under a pure-sampling null model; it does nothing for PCR bias, copy number, compositionality or load, and its merits for richness and DA remain contested. Also keep rarefying (one draw) and rarefaction (averaged) apart.
4. **"Correcting for 16S copy number recovers true cell proportions."** Correction made mock fits worse (Starke 2021); predictions fail beyond about 15% divergence, which covers about half of OTUs (Louca 2018); copy number explained about 10% of total bias (McLaren 2019).
