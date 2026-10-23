# Recovery artefacts in the gene content of metagenome-assembled genomes: writer's view

> [!abstract] About this view
> What the research found, for writing from. Each claim gives who found it, the setting it holds for, the kind of evidence, its standing where the research stated one, and for an absence whether it was searched for. A claim with no standing given has none stated in the research; "limited by access" means a source was not read in full, which is not the same as weak evidence. Sources are listed at the end. The view is generated from the knowledge note `Recovery artefacts in the gene content of metagenome-assembled genomes.md`, where every claim is checked against the research.

## What the research found, by question

### H1-02

**D1. When genomes of one species or genus recovered by metagenomic binning from different samples differ in annotated gene or pathway content, how much of the difference has been shown to arise from recovery: incompleteness, contamination, failure to assemble variable or mobile regions, or differing annotation coverage? Does the size of such artefacts vary systematically with sample properties such as community diversity, sequencing effort or study of origin?**

*Answer, as corrected by a second reader.*

Part A: MEASURED AND MATERIAL, but only in natural human gut and, from a single source, coastal marine samples. In gut, one isolate-referenced study found that MAGs estimated about 95% complete held about 77% of population core genes and 50% of variable genes (n = 8 E. coli pairs; SINGLE SOURCE (Meziti et al. 2021); (Li and Yin 2022) reuses its data). Separately, contamination of a reference pangenome produced false differential gene prevalence between sample groups (SINGLE SOURCE (Majernik et al. 2025); the calls come from read mapping to UHGG, not from comparing recovered genomes). In marine samples, short-read MAGs carried about 9% fewer predicted genes than long-read MAGs at equal CheckM completeness (SINGLE SOURCE (Orellana et al. 2023); 4 samples; short-read libraries had about 3 times more sequenced bases, so read technology and depth are confounded). No filter has been validated on real samples as removing the artefact. Soil and sediment: NOT MEASURED IN THIS SETTING. Part B, human gut: NOT MEASURED for gene or pathway content. Proxies (chimerism rate (Orakov et al. 2021), aligned fraction (Almeida et al. 2021), ribosomal-protein absence by catalogue (Mise and Iwasaki 2022)) differ between catalogues, but catalogue is confounded with pipeline and sample set, and the review's own Section 4 says these are not gene-content measures. The depth null (Kim et al. 2026) is an unquantified sentence from one benchmark, and it is unclear which datasets it covers. Part B, marine: MEASURED for read technology only, SINGLE SOURCE (Orellana et al. 2023), confounded with depth. NOT MEASURED for diversity or depth. Part B, soil and sediment: NOT MEASURED IN THIS SETTING, with indirect recovery-quality evidence only. One bounding fact across soil, seawater and gut (ribosomal-protein contigs assembled well regardless of environment, three depths and two assemblers (Mise and Iwasaki 2022)) was omitted. Engineered systems and simulations: as stated, and they do not answer the natural-sample question.

*Answer, as the research gave it; a second reader reviewed it and left it as given.* **5. Verdicts**

**Part A: measured and material** (natural human gut and marine). The loss of variable and mobile genes, and contamination-driven gains, were measured directly (Meziti et al. 2021; Orellana et al. 2023; Majernik et al. 2025) and persist through completeness filters (Eisenhofer et al. 2023; Mise and Iwasaki 2022; Orakov et al. 2021; Majernik et al. 2025). The filters tested on real samples (Meziti et al. 2021; Li and Yin 2022) reduce the artefact in small gut E. coli sets and were not shown to remove it. For soils and sediments the setting has **not been measured** at gene-content level. Berg et al. (Berg et al. 2025) is indirect support. **Part B:** - Human gut: **measured and systematic** for study of origin (pipeline) (Mise and Iwasaki 2022; Orakov et al. 2021; Almeida et al. 2021). Not measured for diversity. Chimerism was reported as not correlated with depth (Kim et al. 2026) (single source, no ground truth). - Marine: **measured and systematic** for read technology (Orellana et al. 2023) (SINGLE SOURCE for gene content; (Mise and Iwasaki 2022) indirect). Not measured for diversity or depth. - Soil: **not measured in this setting**. There is indirect evidence that recovery quality varies systematically with diversity, depth, habitat and binner (Sereika et al. 2025; Berg et al. 2025; Kim et al. 2026; Johansen et al. 2025; Pan et al. 2022). - Sediment: **not measured in this setting** (yield only (Royalty and Steen 2019; Sereika et al. 2025)). - Engineered systems and simulations: systematic effects of strain diversity and read technology (Meyer et al. 2022; Sereika et al. 2022; Singleton et al. 2021; Rocha et al. 2024), with one null for close relatives (Maguire et al. 2020). These do not answer the natural-sample question. **Sensitivity to single sources.** Removing Meziti et al. (Meziti et al. 2021) would leave Part A as "measured and material" on (Majernik et al. 2025) and (Orellana et al. 2023), but would remove the only natural same-sample isolate comparison and every figure for missed core and variable genes ( (Li and Yin 2022) reuses (Meziti et al. 2021)'s data). Removing Orellana et al. (Orellana et al. 2023) would change the marine Part B verdict to "not measured" for gene content, and marine Part A would then rest on (Mise and Iwasaki 2022) alone. Removing Orakov et al. (Orakov et al. 2021) would leave the gut study-of-origin verdict on (Almeida et al. 2021) (aligned sequence, not genes) and (Mise and Iwasaki 2022), which is weaker but still systematic. Removing Kim et al. (Kim et al. 2026) would remove the only negative result on depth. No Part B verdict in soil or sediment depends on any single source, because none reaches gene content.

## Concepts

In an order where each concept comes after the ones it builds on; the order means nothing more.

### Recovery of genomes from metagenomes and what it can change

- Under the MIMAG standard, a high-quality draft metagenome-assembled genome is more than 90% complete with less than 5% contamination and carries the 23S, 16S and 5S rRNA genes and at least 18 tRNAs; a medium-quality draft is at least 50% complete with less than 10% contamination. (Bowers et al. 2017)
  Background, not from the research.
- Direct measurements exist of how far recovery (incompleteness, contamination, failure to assemble or bin variable and mobile regions, uneven annotation) changes the called gene or pathway content of a recovered genome, although they are few. (the reviewer's synthesis)
  Holds for: the review's reading of the literature its search found on recovered genomes.
- Whether the size of that change depends on properties of the sample has almost no measurements expressed in gene content; what exists are measurements of recovery quality, MAG yield and chimerism rates, which are proxies. (the reviewer's synthesis)
  Holds for: the review's reading of the literature its search found; the review labels the proxies as such.
- In the review's search, one natural-sample study compared MAGs with isolate genomes of the same lineage from the same sample at gene level (Meziti et al.: eight E. coli pairs from human stool); a second study reused five of those pairs, so it is not independent. This is a statement about the search, not a structural fact of the literature: it omits SAG-referenced comparisons (Alneberg et al. 2018). (Meziti et al. 2021; Li and Yin 2022; Alneberg and others 2018)
  Holds for: natural samples; comparisons against same-sample isolate genomes of the same lineage at gene level; SAG-referenced comparisons not covered.
  Evidence: a search result.
  The research does not say whether this was searched for.

### Completeness and contamination estimates and how far they track true recovery

Builds on: Recovery of genomes from metagenomes and what it can change.

- CheckM estimates the completeness and contamination of a genome from a set of marker genes specific to the genome's position in a reference genome tree, rather than from a few markers shared by all bacteria or archaea. (Parks et al. 2015)
  Background, not from the research.
- CheckM simulations found systematic overestimation of completeness under non-redundant contamination, and plasmids and phage were invisible to the estimates. (Parks et al. 2015)
  Holds for: CheckM's own simulations.
  Evidence: modelled.
- In Meziti et al., true recovery of the population's genes was on average 16.9% lower than the MiGA completeness estimate and 20.4% lower than the CheckM estimate: two average shortfalls against two estimators, not a range. (Meziti et al. 2021)
  Holds for: natural human gut; MaxBin 2.0 MAGs against isolate genomes from the same diarrhoeal stool samples; E. coli, n = 8 pairs.
  Evidence: measured; a single source.
- The text of Meziti et al. gives MiGA completeness of its MAGs as 81.1% to 95.5%. (Meziti et al. 2021)
  Holds for: Meziti et al.'s MaxBin 2.0 MAGs from diarrhoeal stool samples; the critic's reading of the paper.
- Meziti et al. conclude that "the quality of MAGs may often be worse than estimated". (Meziti et al. 2021)
  Holds for: one species in one low-diversity host environment (MAGs and isolates from the same diarrhoeal stool samples).
  Evidence: a single source.
- CheckM and GUNC contamination estimates correlated at r = 0.2. (Orakov et al. 2021)
  Holds for: natural samples, in Orakov et al.'s study of GUNC on CheckM-prefiltered MAG catalogues.
  Evidence: measured.
- In an illustrative analysis, GTDB MAGs estimated 99.89% and 93.59% complete covered about 80% and 60% of same-species references; the authors state that habitat, strain and pipeline are confounded. (Pellegrinetti et al. 2026)
  Holds for: an opinion article; not used for any verdict, used for context only; the search agents disagreed on whether it was usable; the note's reference list reports its content while its not-obtained list says it was seen only as a search snippet.
  Evidence: limited by access (a source was not read in full; not the same as weak evidence).

### Gene content lost in recovery (missed core, variable and mobile genes)

Builds on: Recovery of genomes from metagenomes and what it can change, Completeness and contamination estimates and how far they track true recovery.

- MAGs with completeness estimates near 95% captured only 77% of the population core genes and 50% of the variable genes, on average, against isolate genomes from the same samples. (Meziti et al. 2021)
  Holds for: natural human gut; MaxBin 2.0 MAGs against isolate genomes from the same diarrhoeal stool samples; one species (E. coli), n = 8 pairs, metagenomes 0.21 to 2.8 Gbp; one low-diversity host environment; Li and Yin reuse its data, so they are not independent of it.
  Evidence: measured; a single source.
- Population core genes missed by the MAG ranged from 11.31% to 34.7% (mean 24.84%), and population-variable genes missed from 13.63% to 69.56% (mean 50.17%). (Meziti et al. 2021)
  Holds for: natural human gut; MAGs against isolate genomes from the same diarrhoeal stool samples; one species, n = 8 pairs.
  Evidence: measured; a single source.
- Genes with low-identity matches plus genes that had been assembled but binned into other Enterobacteriaceae MAGs made up more than 95% of the missed genes. The paper attributes the low-identity share to sequence divergence from the isolate or to assembly errors, so part of the "loss" may be biology and not recovery; mis-binned genes were 16% to 71% (core) and 64% to 71% (variable) of those without homologs. (Meziti et al. 2021)
  Holds for: Meziti et al.; natural human gut (diarrhoeal stool); E. coli MAG-isolate pairs, n = 8.
  Evidence: a single source.
- When five of Meziti et al.'s E. coli MAGs, or their paired isolates, were mixed with complete genomes, the MAGs lost about 25% of core genes at a 100% core threshold. (Li and Yin 2022)
  Holds for: natural; n = 5 real pairs from human stool, reused from Meziti et al., so not independent of it; the critic: if the 25% comes from Supp. Fig. S14 rather than a main-text statement, it is a full-text breach, and the review should quote the main-text sentence or drop the figure.
  Evidence: measured; limited by access (a source was not read in full; not the same as weak evidence).
- In curated MAGs compared with ten isolate genomes from the same cultures, genomes at 10x coverage or more had over 90% of their sequence recovered (85% at 11x; about 40% at 3.9x). (Nelson et al. 2020)
  Holds for: engineered: two laboratory enrichment consortia.
  Evidence: measured.
- Regions not binned were enriched in repeats, atypical composition, rRNAs, tRNAs, transposases and genes of unknown function, and two plasmids were missed entirely. (Nelson et al. 2020)
  Holds for: engineered: curated MAGs from two laboratory enrichment consortia against ten isolate genomes from the same cultures.
  Evidence: measured.
- Nelson et al. conclude that reconstructions above 90% completeness "are likely to effectively represent organismal function", while uneven plasmid distribution "can lead to incorrect inferences"; the review counts the conclusion as a bounding fact, but an engineered one. (Nelson et al. 2020)
  Holds for: engineered: two laboratory enrichment consortia.
  Evidence: measured.
- A companion analysis of Tara Oceans MAGs, inferred from composition statistics against unrelated RefSeq genomes, found lower repeat content in MAGs, consistent with the same exclusion operating in natural marine data. (Nelson et al. 2020)
  Holds for: natural marine (Tara Oceans MAGs); against unrelated RefSeq genomes, not isolates from the same samples.
  Evidence: derived.
- Across 12 assembler and binner combinations, 82% to 94% of chromosomes were recovered, against 38% to 44% of genomic islands and 1% to 29% of plasmids. (Maguire et al. 2020)
  Holds for: a simulated 30-genome short-read metagenome.
  Evidence: modelled.
- No plasmid-borne AMR or virulence gene was binned correctly. (Maguire et al. 2020)
  Holds for: a simulated 30-genome short-read metagenome.
  Evidence: modelled.
- Most binners lose plasmids. (Meyer et al. 2022)
  Holds for: the CAMI II benchmark.
  Evidence: modelled.
- Checked against a PacBio HiFi assembly of the same system, only 24 of 614 long-read bins had at least half their 1 kb segments fully recovered by short reads, while 490 had at least half not recovered. (Berg et al. 2025)
  Holds for: natural soil: one biocrust community, one site; the reference is long-read bins, not isolates; the review's only natural soil evidence.
  Evidence: measured.
- Segments missed by short-read assembly were low-coverage or came from populations with high sequence variation, and they were enriched in mobile-element and defence functions; the authors conclude that short-read metagenomes "can possibly underestimate the diversity of these genome regions". (Berg et al. 2025)
  Holds for: natural soil: one biocrust community, one site; short-read assemblies against a PacBio HiFi assembly of the same system.
  Evidence: measured.
- The soil short-read loss of variable regions concerns assembly, not the gene content of binned genomes compared across samples, so it is indirect support only for soils. (Berg et al. 2025)
  Holds for: one natural biocrust soil.
- Transposase copies fell at the breakpoints of short-read assemblies of P. copri. (Moss et al. 2020)
  Holds for: qualitative only; given in the reference list and not cited in the body for any figure.

### Content gained in recovery (contamination and chimerism)

Builds on: Recovery of genomes from metagenomes and what it can change, Completeness and contamination estimates and how far they track true recovery.

- MAG-specific genes were 2.35% to 26.41% of MAG gene content (mean 14.42%). (Meziti et al. 2021)
  Holds for: natural human gut; MaxBin 2.0 MAGs against isolate genomes from the same diarrhoeal stool samples; one species in one low-diversity host environment.
  Evidence: a single source.
- Sequence not classified as Enterobacteriaceae averaged 4.4% of the MAGs, above the MiGA contamination estimates (0.9% to 2.7%). (Meziti et al. 2021)
  Holds for: natural human gut; MaxBin 2.0 MAGs from diarrhoeal stool samples; one species in one low-diversity host environment.
  Evidence: a single source.
- Of 86 Lachnospiraceae genes that differed in prevalence between cirrhosis cases and controls, 33 (38%) were probable contaminants from disease-associated genera. (Majernik et al. 2025)
  Holds for: natural human gut; one cirrhosis case-control cohort re-analysed with UHGG/MIDAS2 pangenomes; one family, Lachnospiraceae; the differential calls come from MIDAS2 read mapping to a reference pangenome that was partly contaminated, not from comparing genomes recovered from different samples.
  Evidence: measured; a single source.
- Twenty-six of the 33 contaminant genes came from single assemblies with a mean CheckM contamination of 0.22%, and GUNC flagged none of them: the contaminants sat below 5% CheckM contamination. (Majernik et al. 2025)
  Holds for: natural human gut; one cirrhosis case-control cohort (UHGG/MIDAS2 pangenomes); the critic confirms the figure in full text.
- In the Lachnospira eligens pangenome, 22% of accessory genes had lineage-discordant annotation, against 7.6% when only isolate-derived genes were counted. (Majernik et al. 2025)
  Holds for: natural human gut; one study, one disease contrast (a cirrhosis case-control cohort, UHGG/MIDAS2 pangenomes).
  Evidence: measured; a single source.
- A quick re-run on Bacteroides thetaiotaomicron gave 30 genes in the same data set. (Majernik et al. 2025)
  Holds for: the same cirrhosis cohort data set; the critic's reading of the paper.
- Contamination of a reference pangenome produced false differential gene prevalence between sample groups; the calls come from read mapping to UHGG, not from comparing recovered genomes. (Majernik et al. 2025)
  Holds for: natural human gut; one cirrhosis cohort; MIDAS2 read mapping to a partly contaminated reference pangenome.
  Evidence: a single source.
- After refinement of a composite Saccharibacteria MAG, a pangenome built with other Saccharibacteria genomes gained seven times as many single-copy core genes. (Shaiber and Eren 2019)
  Holds for: natural; co-assembled oral plaque metagenomes; three MAGs; a letter.
  Evidence: measured.
- GUNC flagged 15.1% to 29.9% of CheckM-prefiltered human gut MAG catalogues as chimeric at genus level or above. (Orakov et al. 2021)
  Holds for: natural human gut MAG catalogues; the study measures chimerism, not called gene content; the critic: not re-opened at synthesis, resting on agent reads.
  Evidence: measured.
- In the multi-habitat GMGC set, GUNC flagged 9.4% of MIMAG high-quality MAGs and 20.5% of genomes passing CheckM's contamination threshold of under 5%. (Orakov et al. 2021)
  Holds for: natural, multi-habitat (GMGC); chimerism, not called gene content.
  Evidence: measured.
- In one chimerism survey (Orakov et al.) and one species-level case study (Majernik et al.), genomes that passed the contamination filters in use still carried chimeric or contaminant material. (Orakov et al. 2021; Majernik et al. 2025)
  Holds for: human gut and the multi-habitat GMGC set (Orakov et al.); one cirrhosis cohort, Lachnospiraceae (Majernik et al.).

### Gene classes lost selectively (ribosomal protein genes, CRISPR arrays, transposases)

Builds on: Gene content lost in recovery (missed core, variable and mobile genes).

- Core ribosomal protein genes "could be missing in more than 20-40% of near-complete" MAGs in four of five short-read catalogues (seawater, human gut, chicken gut, rice phyllosphere). (Mise and Iwasaki 2022)
  Holds for: natural; more than 190,000 MAGs; short-read catalogues; the critic confirms the figure in full text.
  Evidence: measured.
- The ribosomal-protein deficit was absent from the GEM catalogue and from long-read or hybrid MAGs. (Mise and Iwasaki 2022)
  Holds for: natural; more than 190,000 MAGs across catalogues.
  Evidence: measured.
- Raw reads carried the ribosomal protein genes, and single-amplified genomes did not show the deficit, so the authors locate the loss at tetranucleotide-based binning. (Mise and Iwasaki 2022)
  Holds for: natural; MAG catalogues with their raw reads and single-amplified genomes.
  Evidence: measured.
- Against phylogenetically close RefSeq genomes (not the same strains), CRISPR arrays and transposases were depleted in MAGs above 90% completeness, while glycolysis genes were not. (Mise and Iwasaki 2022)
  Holds for: natural MAGs above 90% completeness; the reference is close RefSeq genomes, not the same strains.
  Evidence: measured.
- The artefact is gene-class specific and passes a completeness filter, across seawater, gut, chicken gut and phyllosphere catalogues. (Mise and Iwasaki 2022)
  Holds for: natural short-read MAG catalogues; the review's conclusion from Mise and Iwasaki.
- When 11 soil, seawater and gut metagenomes were assembled at three depths with two assemblers, contigs carrying ribosomal-protein genes were longer "regardless of environmental origins of samples, sequencing depths, and assemblers", and soil gave the shortest contigs. The review left this bounding fact out and cites Mise and Iwasaki only for gut and seawater. (Mise and Iwasaki 2022)
  Holds for: natural agricultural and paddy soil, seawater and gut metagenomes; assembly of a specific gene class; the critic's reading of the paper.
- The ribosomal-protein deficit was absent in Planctomycetota, Verrucomicrobiota and Acidobacteriota. (Mise and Iwasaki 2022)
  Holds for: the soil, seawater and gut metagenomes Mise and Iwasaki assembled; the critic's reading of the paper.

### Short against long reads on the same DNA

Builds on: Gene content lost in recovery (missed core, variable and mobile genes), Completeness and contamination estimates and how far they track true recovery.

- In MAG pairs sharing 99% ANI or more from the same DNA extracts, the PacBio HiFi MAG carried more predicted genes than the Illumina MAG (median 1,872 against 1,704, p < 0.05) and was longer (1.98 against 1.85 Mbp), while CheckM completeness and contamination did not differ. (Orellana et al. 2023)
  Holds for: natural coastal marine; North Sea DNA extracts, 4 samples, one time series; the number of pairs is given only in a figure; short-read libraries had about 3 times more sequenced bases, so read technology and depth are confounded.
  Evidence: measured; a single source.
- A 16S rRNA gene was present in 88% of long-read MAGs and 23% of short-read MAGs. (Orellana et al. 2023)
  Holds for: natural coastal marine; the same North Sea DNA extracts sequenced with Illumina and PacBio HiFi.
  Evidence: measured; a single source.
- Short-read MAGs carried about 9% fewer predicted genes than long-read MAGs at equal CheckM completeness, a difference invisible to completeness estimates. Short-read libraries had about 3 times more sequenced bases (about 36 Gbp per sample for Illumina against 12 Gbp for PacBio), so read technology and depth are confounded. (Orellana et al. 2023)
  Holds for: natural coastal marine; 4 North Sea samples, one time series.
  Evidence: a single source.

### Genome incompleteness and pathway (module) completeness

Builds on: Completeness and contamination estimates and how far they track true recovery.

- A rise in CheckM completeness from 70% to 100% was associated with a 15 ± 10% increase in DRAM KEGG module fullness, and the association held above 90% completeness. (Eisenhofer et al. 2023)
  Holds for: 11,842 GTDB genomes, a cross-genome regression; the search agents disagreed on its class (measured versus inferred), and the review treats it as a measured association with an inferred causal reading; the note lists it among the sources re-verified in full text, while the critic says it rests on agent reads.
  Evidence: measured.
- The association of module fullness with completeness differed by phylum and metabolic domain, with nucleotide metabolism and secondary-metabolite biosynthesis most affected. (Eisenhofer et al. 2023)
  Holds for: 11,842 GTDB genomes; DRAM KEGG modules.
  Evidence: measured.
- Because the association is a cross-genome correlation, lineage biology is not fully separated from recovery artefact. (Eisenhofer et al. 2023)
  Holds for: the regression of module fullness on completeness across GTDB genomes.
  Evidence: the reviewer's reading.
- Random contig subsampling of MAGs from an eight-species mock community shifted functional profiles in proportion to the subsampling. (Eisenhofer et al. 2023)
  Holds for: engineered: an eight-species mock community; random, not real, gaps.
  Evidence: modelled.

### Pangenome core and accessory inference from MAGs

Builds on: Gene content lost in recovery (missed core, variable and mobile genes), Content gained in recovery (contamination and chimerism).

- A bacterial species can be described by a pan-genome: a core genome shared by all isolates plus a dispensable genome of partially shared and strain-specific genes. (Tettelin et al. 2005)
  Background, not from the research.
- Simulated random incompleteness of 1% left only about 36% of strict core families, and contamination inflated the cloud genome; the authors state that random removal "may overestimate" core loss. Simulations of core-genome inference give larger numbers because they strip sequence at random. (Li and Yin 2022)
  Holds for: simulations of core-genome inference with sequence removed at random.
  Evidence: modelled.
- Unadjusted core counts were near zero at a 95% core threshold in a test on 500 E. coli assemblies with completeness drawn from MGnify. (Hellewell et al. 2024)
  Holds for: 500 E. coli assemblies with completeness drawn from MGnify (CELEBRIMBOR's test).
  Evidence: modelled.
- Fragmentation of isolate draft assemblies inflates accessory genomes about tenfold in some tools. (Tonkin-Hill et al. 2020)
  Holds for: isolate draft assemblies, not MAGs; the result does not transfer directly.
- Dereplication at 96.5% gANI removed 2,228 of 9,175 auxiliary gene clusters in 46 Microcystis MAGs. (Evans and Denef 2020)
  Holds for: 46 Microcystis MAGs; a downstream processing step, not a recovery artefact; read in full by one agent and noted only for completeness; no verdict rests on it; the note's not-obtained list calls it an opinion piece, excluded.

### Coarse comparisons of MAGs with isolates that bound the losses

Builds on: Gene content lost in recovery (missed core, variable and mobile genes).

- GEM states that MAG sizes matched isolate genomes of the same species, "indicating no major loss of gene content", with one exception, a composite Sinorhizobium MAG. (Nayfach et al. 2021)
  Holds for: the GEM catalogue; an author assertion resting on genome size, not gene-by-gene comparison.
  Evidence: asserted; limited by access and by the evidence.
- Near-complete gut MAGs had lengths similar to isolates of the same OTU, and KEGG annotations were concordant per OTU (n = 665); only 14.5% of the MAGs met MIMAG high quality, mostly because rRNA genes were missing. (Nayfach et al. 2019)
  Holds for: natural human gut; aggregated comparisons across different strains; the critic: not re-opened at synthesis, resting on search-agent reads with no cross-agent confirmation.
  Evidence: derived.
- 36 MAGs were almost identical by ANI to 18 isolates from the same samples; identity metrics do not test accessory content. (Pasolli et al. 2019)
  Holds for: human microbiome samples (Pasolli et al.); ANI only; the critic: not re-opened at synthesis, resting on search-agent reads.
- In 55 of 78 human-microbiome species, MAG and GenBank persistent genomes differed by less than 1.2-fold and shared 90% of content; in the other 23 species, MAG persistent genomes held 60% of the GenBank set. Shell differences mix biology with recovery. (Gautreau et al. 2020)
  Holds for: natural, human microbiome; MAGs against GenBank genomes, not same-sample isolates; the critic: an unverified second-hand figure, resting on search-agent reads with no cross-agent confirmation.
  Evidence: measured.
- These bounds are coarse (genome size, ANI, per-OTU annotation overlap) and do not contradict the gene-level losses in Meziti et al.'s comparison with isolate genomes from the same samples, which fall on variable and mobile genes that length and ANI do not register. (the reviewer's synthesis)
  Holds for: the coarse bounding facts set against the gene-level losses in one isolate comparison; the critic: correctly labelled, but used to discount the bounding evidence in favour of Meziti et al. without a source saying so.
  Evidence: the reviewer's reading.
  A second reader found the search for contrary evidence one-sided.

### Filters and corrections, and their validation on real samples

Builds on: Gene content lost in recovery (missed core, variable and mobile genes), Content gained in recovery (contamination and chimerism), Completeness and contamination estimates and how far they track true recovery, Genome incompleteness and pathway (module) completeness, Pangenome core and accessory inference from MAGs.

- A minimum contig length of 1 kb reduced contamination and non-shared genes in real stool MAGs, with small completeness costs; it was not shown to recover missed genes. (Meziti et al. 2021)
  Holds for: real stool samples, n = 8 (gut E. coli pairs).
- A relaxed core threshold (90%) reduced core loss in five real E. coli pairs. (Li and Yin 2022)
  Holds for: real samples, n = 5, gut.
- The contig-length filter and the relaxed core threshold, tested on real data, reduced the artefact without removing it. (Meziti et al. 2021; Li and Yin 2022)
  Holds for: only n = 8 and n = 5 gut E. coli pairs.
- No filter has been validated on real samples as removing the artefact. (the reviewer's synthesis)
  Holds for: the filters tested on real samples, in small gut E. coli sets.
  The research does not say whether this was searched for.
- Eisenhofer's completeness-model correction (a GLM) was validated on mock-community subsamples and over-corrected some genomes. (Eisenhofer et al. 2023)
  Holds for: mock-community subsamples, not natural-sample MAGs.
- CELEBRIMBOR was validated on simulations, and its authors state that non-random loss violates its missing-at-random assumption. (Hellewell et al. 2024)
  Holds for: simulations.
- mOTUpan was checked against a few closed Prochlorococcus genomes plus bootstraps, and its authors state that genes hard to assemble or bin leave "an inevitable underestimate of the accessory genomes". (Buck et al. 2022)
  Holds for: a few closed Prochlorococcus genomes plus bootstraps.
- MetaPathPredict was tested on random annotation downsampling only. (Geller-McGrath et al. 2024)
  Holds for: random annotation downsampling.
- No completeness or missingness correction has been validated against ground truth on natural-sample MAGs with real, non-random gaps. (Eisenhofer et al. 2023; Buck et al. 2022; Geller-McGrath et al. 2024; Hellewell et al. 2024)
  Holds for: Eisenhofer's GLM, CELEBRIMBOR, mOTUpan and MetaPathPredict, and the review's search for others; the critic: supported by the named search routes and the authors' own stated assumptions (CELEBRIMBOR, mOTUpan).
  Evidence: a search result.
  Searched for and not found.
- Artefacts persist above completeness thresholds: module fullness bias above 90%; ribosomal-protein, CRISPR and transposase deficits above 90%; chimerism in MIMAG high-quality sets; contaminant genes below the 5% contamination threshold. No source showed that a completeness threshold removes the problem. (Eisenhofer et al. 2023; Mise and Iwasaki 2022; Orakov et al. 2021; Majernik et al. 2025)
  Holds for: module fullness, ribosomal-protein and mobile-gene deficits, chimerism and contaminant genes, each from one source; the critic: the ribosomal-protein and contaminant figures have direct support in full text, while the module-fullness and chimerism sources rest on agent reads.
  The research does not say whether this was searched for.
- Gene-to-species correlation filtering classified contaminants with AUROC 0.97 on real gut data, judged against BLAST rather than ground truth. (Majernik et al. 2025)
  Holds for: real gut data (the cirrhosis cohort); the comparison is BLAST, not ground truth.

### Annotation coverage of recovered genes

Builds on: Recovery of genomes from metagenomes and what it can change.

- UHGG core genes had KEGG annotation for a median of 69% of genes, while accessory genes had significantly more unknowns. (Almeida et al. 2021)
  Holds for: human gut only (UHGG).
  Evidence: measured.
- Orthology-based GO coverage in an infant gut catalogue was 12%, and it favoured Gammaproteobacteria. (Maranga et al. 2023)
  Holds for: one infant gut catalogue; the critic: not re-opened at synthesis, resting on search-agent reads.
  Evidence: measured.
- No source measured how annotation coverage differs between samples or environments for the same lineage. (a search result)
  Holds for: the review's search; one route only.
  Evidence: a search result.
  Searched for and not found.

### How large recovery artefacts in gene or pathway content are (Part A)

Builds on: Gene content lost in recovery (missed core, variable and mobile genes), Content gained in recovery (contamination and chimerism), Short against long reads on the same DNA, Gene classes lost selectively (ribosomal protein genes, CRISPR arrays, transposases).

- Recovery artefacts in the gene or pathway content of related recovered genomes have been measured and are material, but only in natural human gut and, from a single source, coastal marine samples. Part A for gut rests on one isolate-comparison study (n = 8, one species) plus one mechanism-adjacent study; the loss of variable and mobile genes, and contamination-driven gains, were measured directly in those sources. (Meziti et al. 2021; Orellana et al. 2023; Majernik et al. 2025)
  Holds for: natural human gut (same-sample isolate pairs, n = 8 E. coli pairs; contamination of differential gene calls) and natural coastal marine (read-technology gene-count difference at equal estimated completeness); the critic: each of the three direct sources is single-source and has caveats the verdict leaves out.
  Evidence: a single source; rated "MEASURED AND MATERIAL" by the research; a second reader disputes this: only in natural human gut and, from a single source, coastal marine samples.
- Effect sizes are not commensurable across the three direct sources: the isolate comparison reports percentages of population core or variable genes, the read-technology study a median gene count, and the contamination study a fraction of differentially prevalent genes; they are reported separately and not pooled. (Meziti et al. 2021; Orellana et al. 2023; Majernik et al. 2025)
  Holds for: the three direct natural-sample sources: same-sample isolate pairs, contamination-driven differential gene calls and matched read-technology pairs.
- Each of the three direct sources is single in its setting: two are human gut and one is coastal marine, and they measure different things. (Meziti et al. 2021; Orellana et al. 2023; Majernik et al. 2025)
  Holds for: same-sample isolate pairs and contamination-driven differential gene calls (human gut); matched read-technology pairs (coastal marine).
  Evidence: a single source.
- Removing Meziti et al. would leave Part A as "measured and material" on the contamination and read-technology sources, but would remove the only natural same-sample isolate comparison and every figure for missed core and variable genes, since Li and Yin reuse its data. (Meziti et al. 2021; Li and Yin 2022; Orellana et al. 2023; Majernik et al. 2025)
  Holds for: the review's sensitivity analysis.

### Whether artefact size depends on sample properties (Part B)

Builds on: How large recovery artefacts in gene or pathway content are (Part A).

- Part B is the weakest area for gene content: the sample-property dependence that has been measured concerns yield, completeness, chimerism or assembled fraction, not gene content. (the reviewer's synthesis)
  Holds for: all sample types in the review.
- No study was found measuring how gene-content artefacts between conspecific MAGs scale with community diversity or depth across samples. (a search result)
  Holds for: the review's search.
  Evidence: a search result.
  Searched for and not found.

### Human gut (natural)

Builds on: Whether artefact size depends on sample properties (Part B), Content gained in recovery (contamination and chimerism), Gene classes lost selectively (ribosomal protein genes, CRISPR arrays, transposases).

- In the human gut, dependence of gene or pathway content artefacts on sample properties has not been measured. Proxies (chimerism rate, aligned fraction, ribosomal-protein absence by catalogue) differ between catalogues, but catalogue is confounded with pipeline and sample set, and the review's own Section 4 says these are not gene-content measures: the body supports "not measured for gene content, indirect proxy evidence varies by catalogue". (Mise and Iwasaki 2022; Orakov et al. 2021; Almeida et al. 2021)
  Holds for: natural human gut; none of the three catalogue sources measures artefact size in gene content against a study variable with sample set held constant, apart from aligned fraction, which is split by quality tier.
  Evidence: rated "MEASURED AND SYSTEMATIC for study of origin (pipeline)" by the research; a second reader disputes this: NOT MEASURED for gene or pathway content.
  Searched for and not found.
- For the same 1,554 gut samples binned by three studies, conspecific genomes had a median aligned fraction of 94.5% at 90% completeness or more and 86.6% at medium quality, so different pipelines applied to identical reads disagreed on roughly 5% to 13% of aligned sequence, with the gap set by quality tier. (Almeida et al. 2021)
  Holds for: natural human gut; aligned sequence, not genes; reported by quality tier, not by study.
  Evidence: measured.
- Chimerism in CheckM-prefiltered gut catalogues ranged from 15.1% to 29.9% by study, about twofold between studies; study of origin is confounded with pipeline and sample set. (Orakov et al. 2021)
  Holds for: natural human gut MAG catalogues; chimerism, not gene content.
- Ribosomal-protein-gene absence was present or absent depending on the catalogue. (Mise and Iwasaki 2022)
  Holds for: natural gut MAG catalogues; catalogue is confounded with pipeline and sample set.
- GUNC-flagged chimerism varied by binner, and Kim et al. state that it "did not correlate with sequencing depth": an unquantified sentence from one benchmark, with no reported statistic, figure panel or stated dataset range, and it is unclear which datasets it covers; the chimerism figures shown are gut datasets. It is the only negative result on depth and has no ground truth. (Kim et al. 2026)
  Holds for: real gut datasets (the chimerism figures shown); one benchmark of binning tools.
  Evidence: asserted; a single source.
- Dependence of gene-content artefacts on community diversity and sequencing depth has not been measured in the gut: no gut study measured how gene-content artefacts scale with community diversity. (a search result)
  Holds for: natural human gut.
  Evidence: a search result.
  Searched for and not found.

### Marine and seawater (natural)

Builds on: Whether artefact size depends on sample properties (Part B), Short against long reads on the same DNA, Gene classes lost selectively (ribosomal protein genes, CRISPR arrays, transposases).

- In marine samples, dependence of gene content on a sample property has been measured for read technology only, in a single source, and confounded with depth: one study of 4 samples. (Orellana et al. 2023)
  Holds for: natural coastal marine; 4 North Sea samples, one time series.
  Evidence: a single source; rated "MEASURED AND SYSTEMATIC for read technology" by the research; a second reader disputes this: 'systematic' is too strong for n = 1 study.
- In marine samples, dependence of gene content on diversity or depth has not been measured; the evidence covers MAG yield only. (Royalty and Steen 2019)
  Holds for: natural marine and seawater.
  Evidence: a search result.
  Searched for and not found.
- In one rarefied surface-ocean data set, MAG yield followed a Gompertz curve (lag 1.2 Gbp) and declined above about 25 Gbp. (Royalty and Steen 2019)
  Holds for: one surface-ocean data set; yield, not content.
- The ribosomal-protein deficit disappeared in long-read catalogues, which supports the read-technology dependence across catalogues rather than in matched samples. (Mise and Iwasaki 2022)
  Holds for: a cross-catalogue comparison, not matched samples; indirect for gene content.
- Removing Orellana et al. would change the marine Part B verdict to "not measured" for gene content, and marine Part A would then rest on Mise and Iwasaki alone. (Mise and Iwasaki 2022; Orellana et al. 2023)
  Holds for: the review's sensitivity analysis.

### Soils and sediments (natural)

Builds on: Whether artefact size depends on sample properties (Part B), Gene content lost in recovery (missed core, variable and mobile genes).

- For soils and sediments, a gene-content comparison between related recovered genomes and a closed or isolate reference has not been measured in the sources found. The critic: the search missed relevant data (Alneberg et al. 2018, a MAG-against-SAG comparison; Mise and Iwasaki's own soil assemblies), so the absence reflects the search more than the literature, and it echoes the absence the brief expected. (a search result)
  Holds for: natural soils, sediments and other high-diversity environments; routes: WebSearch and Europe PMC title and abstract queries on MAG against isolate same sample, and long-read sediment comparisons; the closest hit (mangrove long-read, 2023) reported no gene-content difference.
  Evidence: a search result; rated "NOT MEASURED" by the research.
  Searched for and not found.
- In soil, gene or pathway content of related recovered genomes has not been measured; there is indirect recovery-quality evidence only. (a search result)
  Holds for: natural soil; none of the soil studies measures the gene or pathway content of related genomes recovered from different soil samples.
  Evidence: a search result; rated "NOT MEASURED IN THIS SETTING" by the research.
  Searched for and not found.
- Recovery (assembly fraction, MAG yield, bin quality) in soil depends systematically on diversity, depth, habitat and binner, and short-read assembly loss tracks within-sample coverage and population sequence variation. (Sereika et al. 2025; Berg et al. 2025; Kim et al. 2026; Johansen et al. 2025; Pan et al. 2022)
  Holds for: natural soils; recovery quality, not gene content; the critic: several of the figures behind it are unverified second-hand figures, resting on search-agent reads.
  Evidence: measured.
- Danish agricultural soils sequenced to a mean depth of 107 Gb reached 73% Nonpareil coverage in the less diverse clay field against 47% in sandy fields, and reads assembled into contigs longer than 2 kb were 57% (clay) against 27% (sandy); co-assembly raised both. (Johansen et al. 2025)
  Holds for: natural Danish agricultural soils; the critic: not re-opened at synthesis, an unverified second-hand figure resting on search-agent reads.
  Evidence: measured.
- Agricultural soils had the lowest assembled fraction and MAG yield, and coastal samples still yielded more MAGs after depth normalisation. (Sereika et al. 2025)
  Holds for: natural terrestrial habitats, long-read sequencing; n = 3 + 3 for the depth-normalised comparison; the critic: not re-opened at synthesis.
  Evidence: measured.
- Rarefaction gave the longest MAG-yield lag for maize soil (6.1 Gbp). (Royalty and Steen 2019)
  Holds for: one maize soil data set, rarefied; yield, not content.
  Evidence: measured.
- Most binners struggled to recover high-quality soil genomes at depths comparable to gut and ocean. (Kim et al. 2026)
  Holds for: natural soil, gut and ocean data in one benchmark of binning tools.
  Evidence: measured.
- SemiBin's gains over other binners were largest in soil. (Pan et al. 2022)
  Holds for: microbiome datasets across different environments; the critic: not re-opened at synthesis.
  Evidence: measured.
- For sediments, the only evidence is one estuarine sediment rarefaction (MAG yield; lag 3.7 Gbp, lowest maximum yield) and habitat-level yield for coastal sediments; nothing was found on content artefacts. (Royalty and Steen 2019; Sereika et al. 2025)
  Holds for: natural sediments; MAG yield only; the critic: deep-sea, freshwater and estuarine sediment long-read against short-read comparisons, and sediment SAG-MAG comparisons, were not searched by name.
  Evidence: a search result; rated "NOT MEASURED IN THIS SETTING" by the research.
  Searched for and not found.
- A long-read mangrove sediment study compares MAG counts and collinearity between Illumina, PacBio and hybrid assemblies and reports no gene-content difference. (Zhang et al. 2023)
  Holds for: mangrove sediments; full text obtained but not used as a finding; the critic: the review did not report its gene-content statements.
- No Part B verdict in soil or sediment depends on any single source, because none reaches gene content. (the reviewer's synthesis)
  Holds for: the review's sensitivity analysis.

### Engineered systems and simulations (kept separate)

Builds on: Whether artefact size depends on sample properties (Part B), Gene content lost in recovery (missed core, variable and mobile genes).

- Mean bin completeness fell from 36.9% (marine gold-standard assembly) to 18.2% under high strain diversity, and to 5.2% on MEGAHIT assemblies; genomes with close relatives assembled far worse, and strain diversity degraded completeness and purity. (Meyer et al. 2022)
  Holds for: the CAMI II benchmark.
  Evidence: modelled.
- No clear effect of close relatives was found in a 30-genome community. (Maguire et al. 2020)
  Holds for: one low-complexity simulation (30 genomes).
  Evidence: modelled.
- Completeness correlated with depth at ρ = 0.20 and with taxonomic complexity at ρ = −0.55. (Kim et al. 2026)
  Holds for: Kim et al.'s simulations.
  Evidence: modelled.
- Depth effects on true-positive recovery reversed between pipelines around 60 million reads: depth effects are pipeline-dependent. (Rocha et al. 2024)
  Holds for: simulations of 69 microbial communities; the critic: not re-opened at synthesis.
  Evidence: modelled.
- In one anaerobic digester sample, long reads gave far more high-quality, less fragmented MAGs, and microdiversity increased fragmentation. (Sereika et al. 2022)
  Holds for: engineered; one anaerobic digester sample.
- Long-read activated-sludge MAGs carried full rRNA operons in 91.3% of cases. (Singleton et al. 2021)
  Holds for: engineered; activated sludge.
- In engineered bioreactors, read technology changes contiguity and rRNA recovery. (Sereika et al. 2022; Singleton et al. 2021)
  Holds for: one anaerobic digester sample and activated sludge.
- Multi-sample binning identified 22% to 30% more potential ARG hosts than single-sample binning, so processing mode alone changes how many genomes carry an annotated trait. (Han et al. 2025)
  Holds for: real marine, cheese, gut and sludge data; the critic: an unverified second-hand figure, resting on search-agent reads with no cross-agent confirmation.
  Evidence: measured.
- In simulations and engineered systems, strain diversity and read technology have systematic effects, with one null for close relatives; these do not answer the question for natural samples. (Maguire et al. 2020; Meyer et al. 2022; Sereika et al. 2022; Singleton et al. 2021; Rocha et al. 2024)
  Holds for: simulations and engineered bioreactors; the critic accepts this verdict as stated.
  Evidence: rated "MEASURED AND SYSTEMATIC in simulations" by the research.

## Do not say

Wordings the research itself says are wrong or overstated, each with the reason and what to say instead.

- Do not write: "Meziti et al. found true recovery 16.9% to 20.4% below the completeness estimates."
  Why: The two figures are not a range: they are average shortfalls against two estimators, 16.9% against MiGA and 20.4% against CheckM.
  Say instead: In Meziti et al., true recovery of the population's genes was on average 16.9% lower than the MiGA completeness estimate and 20.4% lower than the CheckM estimate: two average shortfalls against two estimators, not a range. (Meziti et al. 2021)
  Holds for: natural human gut; MaxBin 2.0 MAGs against isolate genomes from the same diarrhoeal stool samples; E. coli, n = 8 pairs.
  Evidence: measured; a single source.
- Do not write: "The MAGs had CheckM/MiGA completeness estimates of 81.1% to 97.2%."
  Why: The range mixes estimator columns; the paper's text gives MiGA MAG completeness as 81.1% to 95.5%.
  Say instead: The text of Meziti et al. gives MiGA completeness of its MAGs as 81.1% to 95.5%. (Meziti et al. 2021)
  Holds for: Meziti et al.'s MaxBin 2.0 MAGs from diarrhoeal stool samples; the critic's reading of the paper.
- Do not write: "The main mechanism of gene loss in MAGs was mis-binning among co-occurring relatives, not a failure to sequence."
  Why: That is the reviewer's inference and over-reads the paper, which attributes the low-identity share of missed genes to sequence divergence from the isolate or to assembly errors, so part of the loss may be biology and not recovery.
  Say instead: Genes with low-identity matches plus genes that had been assembled but binned into other Enterobacteriaceae MAGs made up more than 95% of the missed genes. The paper attributes the low-identity share to sequence divergence from the isolate or to assembly errors, so part of the "loss" may be biology and not recovery; mis-binned genes were 16% to 71% (core) and 64% to 71% (variable) of those without homologs. (Meziti et al. 2021)
  Holds for: Meziti et al.; natural human gut (diarrhoeal stool); E. coli MAG-isolate pairs, n = 8.
  Evidence: a single source.
- Do not write: "Contamination produced apparent content differences between sample groups of recovered genomes."
  Why: The differential calls come from MIDAS2 read mapping to a reference pangenome that was partly contaminated; they are not content differences between genomes recovered from different samples.
  Say instead: Contamination of a reference pangenome produced false differential gene prevalence between sample groups; the calls come from read mapping to UHGG, not from comparing recovered genomes. (Majernik et al. 2025)
  Holds for: natural human gut; one cirrhosis cohort; MIDAS2 read mapping to a partly contaminated reference pangenome.
  Evidence: a single source.
- Do not write: "The contamination filters in common use leave chimeric material in place."
  Why: It generalises to the filters in common use from one chimerism survey plus one species-level case study.
  Say instead: In one chimerism survey (Orakov et al.) and one species-level case study (Majernik et al.), genomes that passed the contamination filters in use still carried chimeric or contaminant material. (Orakov et al. 2021; Majernik et al. 2025)
  Holds for: human gut and the multi-habitat GMGC set (Orakov et al.); one cirrhosis cohort, Lachnospiraceae (Majernik et al.).
- Do not write: "A gene-count difference of about 9% between short- and long-read MAGs depended on read technology."
  Why: It omits the paper's reported 3-fold difference in sequenced bases between platforms and attributes the effect to technology alone; read technology and depth are confounded.
  Say instead: Short-read MAGs carried about 9% fewer predicted genes than long-read MAGs at equal CheckM completeness, a difference invisible to completeness estimates. Short-read libraries had about 3 times more sequenced bases (about 36 Gbp per sample for Illumina against 12 Gbp for PacBio), so read technology and depth are confounded. (Orellana et al. 2023)
  Holds for: natural coastal marine; 4 North Sea samples, one time series.
  Evidence: a single source.
- Do not write: "Three natural-sample sources that do not depend on each other establish that recovery produces material content differences."
  Why: The three sources measure different things in two environments, and each is single in its setting; together they do not establish a field-level finding.
  Say instead: Recovery artefacts in the gene or pathway content of related recovered genomes have been measured and are material, but only in natural human gut and, from a single source, coastal marine samples. Part A for gut rests on one isolate-comparison study (n = 8, one species) plus one mechanism-adjacent study; the loss of variable and mobile genes, and contamination-driven gains, were measured directly in those sources. (Meziti et al. 2021; Orellana et al. 2023; Majernik et al. 2025)
  Holds for: natural human gut (same-sample isolate pairs, n = 8 E. coli pairs; contamination of differential gene calls) and natural coastal marine (read-technology gene-count difference at equal estimated completeness); the critic: each of the three direct sources is single-source and has caveats the verdict leaves out.
  Evidence: a single source; rated "MEASURED AND MATERIAL" by the research; a second reader disputes this: only in natural human gut and, from a single source, coastal marine samples.
  Say instead: Each of the three direct sources is single in its setting: two are human gut and one is coastal marine, and they measure different things. (Meziti et al. 2021; Orellana et al. 2023; Majernik et al. 2025)
  Holds for: same-sample isolate pairs and contamination-driven differential gene calls (human gut); matched read-technology pairs (coastal marine).
  Evidence: a single source.
- Do not write: "Only one natural-sample study has ever compared MAGs with isolate genomes of the same lineage from the same sample at gene level."
  Why: The review frames it as a structural fact of the literature, but it is a statement about the search, and it omits SAG-referenced comparisons (Alneberg et al. 2018).
  Say instead: In the review's search, one natural-sample study compared MAGs with isolate genomes of the same lineage from the same sample at gene level (Meziti et al.: eight E. coli pairs from human stool); a second study reused five of those pairs, so it is not independent. This is a statement about the search, not a structural fact of the literature: it omits SAG-referenced comparisons (Alneberg et al. 2018). (Meziti et al. 2021; Li and Yin 2022; Alneberg and others 2018)
  Holds for: natural samples; comparisons against same-sample isolate genomes of the same lineage at gene level; SAG-referenced comparisons not covered.
  Evidence: a search result.
  The research does not say whether this was searched for.
- Do not write: "In the human gut, gene-content artefacts are measured and systematic for study of origin (pipeline)."
  Why: The verdict contradicts the review's own Section 4, which says the measured dependence concerns yield, completeness, chimerism or assembled fraction, not gene content; study of origin is confounded with pipeline and sample set, and aligned fraction is reported by quality tier, not by study.
  Say instead: In the human gut, dependence of gene or pathway content artefacts on sample properties has not been measured. Proxies (chimerism rate, aligned fraction, ribosomal-protein absence by catalogue) differ between catalogues, but catalogue is confounded with pipeline and sample set, and the review's own Section 4 says these are not gene-content measures: the body supports "not measured for gene content, indirect proxy evidence varies by catalogue". (Mise and Iwasaki 2022; Orakov et al. 2021; Almeida et al. 2021)
  Holds for: natural human gut; none of the three catalogue sources measures artefact size in gene content against a study variable with sample set held constant, apart from aligned fraction, which is split by quality tier.
  Evidence: rated "MEASURED AND SYSTEMATIC for study of origin (pipeline)" by the research; a second reader disputes this: NOT MEASURED for gene or pathway content.
  Searched for and not found.
- Do not write: "Without Orakov et al., the gut study-of-origin verdict would still be systematic on aligned sequence and ribosomal-protein absence."
  Why: It rests on the gut verdict 'measured and systematic for study of origin', which the critic corrects to not measured for gene content, with indirect proxy evidence varying by catalogue.
  Say instead: In the human gut, dependence of gene or pathway content artefacts on sample properties has not been measured. Proxies (chimerism rate, aligned fraction, ribosomal-protein absence by catalogue) differ between catalogues, but catalogue is confounded with pipeline and sample set, and the review's own Section 4 says these are not gene-content measures: the body supports "not measured for gene content, indirect proxy evidence varies by catalogue". (Mise and Iwasaki 2022; Orakov et al. 2021; Almeida et al. 2021)
  Holds for: natural human gut; none of the three catalogue sources measures artefact size in gene content against a study variable with sample set held constant, apart from aligned fraction, which is split by quality tier.
  Evidence: rated "MEASURED AND SYSTEMATIC for study of origin (pipeline)" by the research; a second reader disputes this: NOT MEASURED for gene or pathway content.
  Searched for and not found.
- Do not write: "GUNC-estimated chimerism did not correlate with depth across real gut, ocean and soil samples."
  Why: The statement is one unquantified sentence in Kim et al. with no reported statistic; the review extends it to real gut, ocean and soil samples, but the chimerism figures shown are gut datasets.
  Say instead: GUNC-flagged chimerism varied by binner, and Kim et al. state that it "did not correlate with sequencing depth": an unquantified sentence from one benchmark, with no reported statistic, figure panel or stated dataset range, and it is unclear which datasets it covers; the chimerism figures shown are gut datasets. It is the only negative result on depth and has no ground truth. (Kim et al. 2026)
  Holds for: real gut datasets (the chimerism figures shown); one benchmark of binning tools.
  Evidence: asserted; a single source.
- Do not write: "Kim et al. measured that chimerism does not correlate with sequencing depth."
  Why: The depth-chimerism statement is a sentence with no statistic, figure panel or stated dataset range: it is asserted-class evidence that the review tagged as a measured negative result.
  Say instead: GUNC-flagged chimerism varied by binner, and Kim et al. state that it "did not correlate with sequencing depth": an unquantified sentence from one benchmark, with no reported statistic, figure panel or stated dataset range, and it is unclear which datasets it covers; the chimerism figures shown are gut datasets. It is the only negative result on depth and has no ground truth. (Kim et al. 2026)
  Holds for: real gut datasets (the chimerism figures shown); one benchmark of binning tools.
  Evidence: asserted; a single source.
- Do not write: "In marine samples, gene-content artefacts are measured and systematic for read technology."
  Why: It rests on one study of 4 North Sea samples, one time series, with a depth confound, so 'systematic' is too strong for n = 1 study.
  Say instead: In marine samples, dependence of gene content on a sample property has been measured for read technology only, in a single source, and confounded with depth: one study of 4 samples. (Orellana et al. 2023)
  Holds for: natural coastal marine; 4 North Sea samples, one time series.
  Evidence: a single source; rated "MEASURED AND SYSTEMATIC for read technology" by the research; a second reader disputes this: 'systematic' is too strong for n = 1 study.
- Do not write: "GEM measured no major loss of gene content in its MAGs."
  Why: 'No major loss of gene content' is an author assertion: the underlying Supp. Fig. 2 was not read, so the claim is asserted, not measured.
  Say instead: GEM states that MAG sizes matched isolate genomes of the same species, "indicating no major loss of gene content", with one exception, a composite Sinorhizobium MAG. (Nayfach et al. 2021)
  Holds for: the GEM catalogue; an author assertion resting on genome size, not gene-by-gene comparison.
  Evidence: asserted; limited by access and by the evidence.
- Do not write: "The gene-content losses measured in gut MAGs also apply to soil MAGs."
  Why: The review warns that the gut findings should not be transferred to soil: the setting differs in diversity, coverage and microdiversity, and the direction and size of the difference are unmeasured.
  Say instead: In soil, gene or pathway content of related recovered genomes has not been measured; there is indirect recovery-quality evidence only. (a search result)
  Holds for: natural soil; none of the soil studies measures the gene or pathway content of related genomes recovered from different soil samples.
  Evidence: a search result; rated "NOT MEASURED IN THIS SETTING" by the research.
  Searched for and not found.

## Gaps

What the research did not establish.

- Genomes from the same natural sample compared with a non-isolate reference: single-amplified genomes against MAGs, for gene-content overlap. The review treats isolates as the only same-sample reference; Alneberg et al. 2018 aligns SAG-MAG pairs from the same station in brackish Baltic Sea bacterioplankton and reports gene-content overlap and 16S presence. Follow-up: search 'SAG MAG comparison same sample gene content' in marine, freshwater and soil. (Alneberg and others 2018)
  The research does not say whether this was searched for.
- Whether ribosomal-protein and other gene-class recovery depends on depth in soil: re-read Mise and Iwasaki's Fig. 3 and Supp. Fig. S1 for soil and depth, and check whether any other study reports gene-class recovery against depth in soil. (Mise and Iwasaki 2022)
  The research does not say whether this was searched for.
- Annotation-coverage bias across lineages, for novel and understudied phyla typical of soils and sediments (Lobb et al. 2020), and studies of KEGG or Pfam annotation rate against phylogenetic novelty in soil MAG catalogues; the review's treatment of differing annotation coverage is gut only. (Lobb et al. 2020)
  The research does not say whether this was searched for.
- Long-read or HiFi against short-read MAG content in a complex natural host-associated community (sheep and ruminant gut): Bickhart et al. 2022 was not obtained, and an author manuscript may exist; rumen HiFi MAG studies for plasmid and mobile-element content differences. (Bickhart et al. 2022)
  The research does not say whether this was searched for.
- Freshwater and lake natural samples, and hypersaline salterns, are absent from both parts: Puente-Sánchez et al. and Conrad et al. (hypersaline Salinibacter pangenomes) were not obtained. Follow-up: retry full text, and search 'MAG pangenome accessory genes freshwater isolate comparison'. (Conrad et al. 2022; Puente-Sanchez et al. 2023)
  The research does not say whether this was searched for.
- How microdiversity or strain heterogeneity in natural samples, measured per population (for example inStrain nucleotide diversity), changes the MAG gene content recovered across samples; only CAMI simulations and Berg et al. touch it. Follow-up: the strain-resolved and population-genomics literature (inStrain, StrainPhlAn, DESMAN, STRONG) for recovered accessory-gene loss against population nucleotide diversity.
  The research does not say whether this was searched for.
- Sediments have only yield data: deep-sea, freshwater and estuarine sediment long-read against short-read comparisons, and sediment SAG-MAG comparisons, are needed; the mangrove study's gene-content statements were not reported. Follow-up: 'sediment long-read metagenome MAG gene content short-read comparison'; 'subseafloor SAG MAG'. (Zhang et al. 2023)
  Not searched for.
- Proximity-ligation (Hi-C) binning evaluations of plasmid and mobile-element assignment on natural samples (gut, rumen, soil, wastewater), which directly address failure to bin mobile regions, against shotgun-only binning.
  The research does not say whether this was searched for.
- A follow-up brief on soil and sediment recovery artefacts, sized separately: the routing condition was triggered because the coverage gaps name sample types without direct measurement, and the soil and sediment 'not measured' verdict echoes the brief's expected absence, is partly search-limited, and so reflects the search more than the literature.
  The research does not say whether this was searched for.
- Whether Li and Yin's 25% core-gene loss in real pairs is stated in the main text or only in Supp. Fig. S14, which no agent read. (Li and Yin 2022)
  The research does not say whether this was searched for.
- Supplementary materials and sources not read: GEM Supp. Fig. 2, Supp. Table 3 and Supplementary Note; UHGG and Pasolli et al. (Table S2, Fig. 7); Nayfach et al. 2019 Extended Data Fig. 3f; Hellewell et al. 2024 Supp. Fig. S6; CAMI I and CheckM2. (Nayfach et al. 2021; Hellewell et al. 2024; Nayfach et al. 2019; Pasolli et al. 2019; Sczyrba and others 2017; Chklovski et al. 2023)
  The research does not say whether this was searched for.
- Figures not re-opened at synthesis and resting on search-agent reads with no cross-agent confirmation, including the Han 22% to 30% ARG-host figure, Johansen's 57% against 27% and 73% against 47%, and Gautreau's 55 of 78 species; several carry weight in the soil Part B indirect evidence. (Gautreau et al. 2020; Johansen et al. 2025; Han et al. 2025)
  The research does not say whether this was searched for.
- Which datasets Kim et al.'s depth-chimerism null covers, and whether it has a statistic. (Kim et al. 2026)
  The research does not say whether this was searched for.
- How gene-content artefacts between conspecific MAGs scale with community diversity or depth across natural samples, in any environment.
  Searched for and not found.
- A completeness or missingness correction validated on natural-sample MAGs with non-random gaps against ground truth.
  Searched for and not found.
- A soil or sediment study comparing gene content of MAGs with isolate or closed genomes of the same lineage.
  Searched for and not found.

## References

- Almeida, Alexandre; Nayfach, Stephen; Boland, Miguel; Strozzi, Francesco; Beracochea, Martin; Shi, Zhou Jason; Pollard, Katherine S.; Sakharova, Ekaterina; Parks, Donovan H.; Hugenholtz, Philip; Segata, Nicola; Kyrpides, Nikos C.; Finn, Robert D. (2021). A unified catalog of 204,938 reference genomes from the human gut microbiome. Nature Biotechnology 39(1): 105--114. https://doi.org/10.1038/s41587-020-0603-3
- Alneberg, J.; others (2018). Genomes from uncultivated prokaryotes: a comparison of metagenome-assembled and single-amplified genomes. Microbiome 6: 173. https://doi.org/10.1186/s40168-018-0550-0
- Berg, Maureen; Reiter, Taylor; Emerson, Joanne; Brown, C. Titus; Roux, Simon (2025). Comparison of short-read and long-read metagenome assemblies in a natural soil community highlights systematic bias in recovery of high-diversity populations. NAR Genomics and Bioinformatics 7(4): lqaf163. https://doi.org/10.1093/nargab/lqaf163
- Bickhart, Derek M.; Kolmogorov, Mikhail; Tseng, Elizabeth; Portik, Daniel M.; Korobeynikov, Anton; Tolstoganov, Ivan; Uritskiy, Gherman; Liachko, Ivan; Sullivan, Shawn T.; Shin, Sung Bong; Zorea, Alvah; Andreu, Victoria Pascal; Panke-Buisse, Kevin; Medema, Marnix H.; Mizrahi, Itzhak; Pevzner, Pavel A.; Smith, Timothy P. L. (2022). Generating lineage-resolved, complete metagenome-assembled genomes from complex microbial communities. Nature Biotechnology 40: 711--719. https://doi.org/10.1038/s41587-021-01130-z
- Bowers, Robert M.; Kyrpides, Nikos C.; Stepanauskas, Ramunas; others (2017). Minimum information about a single amplified genome (MISAG) and a metagenome-assembled genome (MIMAG) of bacteria and archaea. Nature Biotechnology 35(8): 725--731. https://doi.org/10.1038/nbt.3893
- Buck, Moritz; Mehrshad, Maliheh; Bertilsson, Stefan (2022). mOTUpan: a robust Bayesian approach to leverage metagenome-assembled genomes for core-genome estimation. NAR Genomics and Bioinformatics 4(3): lqac060. https://doi.org/10.1093/nargab/lqac060
- Chklovski, Alex; Parks, Donovan H.; Woodcroft, Ben J.; Tyson, Gene W. (2023). CheckM2: a rapid, scalable and accurate tool for assessing microbial genome quality using machine learning. Nature Methods 20(8): 1203--1212. https://doi.org/10.1038/s41592-023-01940-w
- Conrad, Roth E.; Viver, Tomeu; Gago, Juan F.; Hatt, Janet K.; Venter, Stephanus N.; Rossello-Mora, Ramon; Konstantinidis, Konstantinos T. (2022). Toward quantifying the adaptive role of bacterial pangenomes during environmental perturbations. The ISME Journal 16(5): 1222--1234. https://doi.org/10.1038/s41396-021-01149-9
- Eisenhofer, Raphael; Odriozola, Inaki; Alberdi, Antton (2023). Impact of microbial genome completeness on metagenomic functional inference. ISME Communications 3(1): 12. https://doi.org/10.1038/s43705-023-00221-z
- Evans, Jacob T.; Denef, Vincent J. (2020). To Dereplicate or Not To Dereplicate?. mSphere 5(3): e00971-19. https://doi.org/10.1128/mSphere.00971-19
- Gautreau, Guillaume; Bazin, Adelme; Gachet, Mathieu; Planel, Remi; Burlot, Laura; Dubois, Mathieu; Perrin, Amandine; Medigue, Claudine; Calteau, Alexandra; Cruveiller, Stephane; Matias, Catherine; Ambroise, Christophe; Rocha, Eduardo P. C.; Vallenet, David (2020). PPanGGOLiN: Depicting microbial diversity via a partitioned pangenome graph. PLOS Computational Biology 16(3): e1007732. https://doi.org/10.1371/journal.pcbi.1007732
- Geller-McGrath, David; Konwar, Kishori M.; Edgcomb, Virginia P.; Pachiadaki, Maria; Roddy, Jack W.; Wheeler, Travis J.; McDermott, Jason E. (2024). Predicting metabolic modules in incomplete bacterial genomes with MetaPathPredict. eLife 13: e85749. https://doi.org/10.7554/eLife.85749
- Han, Haitao; Wang, Ziye; Zhu, Shanfeng (2025). Benchmarking metagenomic binning tools on real datasets across sequencing platforms and binning modes. Nature Communications 16(1): 2865. https://doi.org/10.1038/s41467-025-57957-6
- Hellewell, Joel; Horsfield, Samuel T.; von Wachsmann, Johanna; Gurbich, Tatiana A.; Finn, Robert D.; Iqbal, Zamin; Roberts, Leah W.; Lees, John A. (2024). CELEBRIMBOR: core and accessory genes from metagenomes. Bioinformatics 40(9): btae542. https://doi.org/10.1093/bioinformatics/btae542
- Johansen, Pi Lrke; Chatzigiannidou, Ioanna; Berzina, Lelde; Kristiansen, Karsten; Brix, Susanne (2025). Unveiling soil microbial diversity through ultra-deep short-read metagenomic sequencing and co-assembly. iMeta 4(5): e70075. https://doi.org/10.1002/imt2.70075
- Kim, Jungyeon; Kim, Nayeon; Cha, Jun Hyung; Ma, Junyeong; Lee, Insuk (2026). Comprehensive benchmarking of metagenomic binning tools reveals key factors for improved genome recovery. Nature Communications 17: 3467. https://doi.org/10.1038/s41467-026-71521-w
- Li, Tang; Yin, Yanbin (2022). Critical assessment of pan-genomic analysis of metagenome-assembled genomes. Briefings in Bioinformatics 23(6): bbac413. https://doi.org/10.1093/bib/bbac413
- Lobb, B.; Tremblay, B. J.-M.; Moreno-Hagelsieb, G.; Doxey, A. C. (2020). An assessment of genome annotation coverage across the bacterial tree of life. Microbial Genomics 6(3). https://doi.org/10.1099/mgen.0.000341
- Maguire, Finlay; Jia, Baofeng; Gray, Kristen L.; Lau, Wing Yin Venus; Beiko, Robert G.; Brinkman, Fiona S. L. (2020). Metagenome-assembled genome binning methods with short reads disproportionately fail for plasmids and genomic Islands. Microbial Genomics 6(10): e000436. https://doi.org/10.1099/mgen.0.000436
- Majernik, Stephanie N.; Beaver, Larry; Bradley, Patrick H. (2025). Small amounts of misassembly can have disproportionate effects on pangenome-based metagenomic analyses. mSphere 10(5): e00857-24. https://doi.org/10.1128/msphere.00857-24
- Maranga, Mary; Szczerbiak, Pawel; Bezshapkin, Valentyn; Gligorijevic, Vladimir; Chandler, Chris; Bonneau, Richard; Xavier, Ramnik J.; Vatanen, Tommi; Kosciolek, Tomasz (2023). Comprehensive Functional Annotation of Metagenomes and Microbial Genomes Using a Deep Learning-Based Method. mSystems 8(2): e01178-22. https://doi.org/10.1128/msystems.01178-22
- Meyer, Fernando; Fritz, Adrian; Deng, Zhi-Luo; Koslicki, David; Lesker, Till Robin; Gurevich, Alexey; Robertson, Gary; Alser, Mohammed; Antipov, Dmitry; Beghini, Francesco; Bertrand, Denis; Brito, Jaqueline J.; Brown, C. Titus; Buchmann, Jan; Buluc, Aydin; Chen, Bo; Chikhi, Rayan; Clausen, Philip T. L. C.; Cristian, Alexandru; Dabrowski, Piotr Wojciech; Darling, Aaron E.; Egan, Rob; Eskin, Eleazar; Georganas, Evangelos; Goltsman, Eugene; Gray, Melissa A.; Hansen, Lars Hestbjerg; Hofmeyr, Steven; Huang, Pingqin; Irber, Luiz; Jia, Huijue; Jrgensen, Tue Sparholt; Kieser, Silas D.; Klemetsen, Terje; Kola, Axel; Kolmogorov, Mikhail; Korobeynikov, Anton; Kwan, Jason; LaPierre, Nathan; Lemaitre, Claire; Li, Chenhao; Limasset, Antoine; Malcher-Miranda, Fabio; Mangul, Serghei; Marcelino, Vanessa R.; Marchet, Camille; Marijon, Pierre; Meleshko, Dmitry; Mende, Daniel R.; Milanese, Alessio; Nagarajan, Niranjan; Nissen, Jakob; Nurk, Sergey; Oliker, Leonid; Paoli, Lucas; Peterlongo, Pierre; Piro, Vitor C.; Porter, Jacob S.; Rasmussen, Simon; Rees, Evan R.; Reinert, Knut; Renard, Bernhard; Robertsen, Espen Mikal; Rosen, Gail L.; Ruscheweyh, Hans-Joachim; Sarwal, Varuni; Segata, Nicola; Seiler, Enrico; Shi, Lizhen; Sun, Fengzhu; Sunagawa, Shinichi; Srensen, Sren Johannes; Thomas, Ashleigh; Tong, Chengxuan; Trajkovski, Mirko; Tremblay, Julien; Uritskiy, Gherman; Vicedomini, Riccardo; Wang, Zhengyang; Wang, Ziye; Wang, Zhong; Warren, Andrew; Willassen, Nils Peder; Yelick, Katherine; You, Ronghui; Zeller, Georg; Zhao, Zhengqiao; Zhu, Shanfeng; Zhu, Jie; Garrido-Oter, Ruben; Gastmeier, Petra; Hacquard, Stephane; Haussler, Susanne; Khaledi, Ariane; Maechler, Friederike; Mesny, Fantin; Radutoiu, Simona; Schulze-Lefert, Paul; Smit, Nathiana; Strowig, Till; Bremges, Andreas; Sczyrba, Alexander; McHardy, Alice Carolyn (2022). Critical Assessment of Metagenome Interpretation: the second round of challenges. Nature Methods 19(4): 429--440. https://doi.org/10.1038/s41592-022-01431-4
- Meziti, Alexandra; Rodriguez-R, Luis M.; Hatt, Janet K.; Pena-Gonzalez, Angela; Levy, Karen; Konstantinidis, Konstantinos T. (2021). The Reliability of Metagenome-Assembled Genomes (MAGs) in Representing Natural Populations: Insights from Comparing MAGs against Isolate Genomes Derived from the Same Fecal Sample. Applied and Environmental Microbiology 87(6): e02593-20. https://doi.org/10.1128/AEM.02593-20
- Mise, Kazumori; Iwasaki, Wataru (2022). Unexpected absence of ribosomal protein genes from metagenome-assembled genomes. ISME Communications 2(1): 118. https://doi.org/10.1038/s43705-022-00204-6
- Moss, Eli L.; Maghini, Dylan G.; Bhatt, Ami S. (2020). Complete, closed bacterial genomes from microbiomes using nanopore sequencing. Nature Biotechnology 38(6): 701--707. https://doi.org/10.1038/s41587-020-0422-6
- Nayfach, Stephen; Roux, Simon; Seshadri, Rekha; Udwary, Daniel; Varghese, Neha; Schulz, Frederik; Wu, Dongying; Paez-Espino, David; Chen, I-Min; Huntemann, Marcel; Palaniappan, Krishna; Ladau, Joshua; Mukherjee, Supratim; Reddy, T. B. K.; Nielsen, Torben; Kirton, Edward; Faria, Jose P.; Edirisinghe, Janaka N.; Henry, Christopher S.; Jungbluth, Sean P.; Chivian, Dylan; Dehal, Paramvir; Wood-Charlson, Elisha M.; Arkin, Adam P.; Tringe, Susannah G.; Visel, Axel; IMG/M Data Consortium; Abreu, Helena; Acinas, Silvia G.; Allen, Eric; Allen, Michelle A.; Alteio, Lauren V.; Andersen, Gary; Anesio, Alexandre M.; Attwood, Graeme; Avila-Magana, Viridiana; Badis, Yacine; Bailey, Jake; Baker, Brett; Baldrian, Petr; Barton, Hazel A.; Beck, David A. C.; Becraft, Eric D.; Beller, Harry R.; Beman, J. Michael; Bernier-Latmani, Rizlan; Berry, Timothy D.; Bertagnolli, Anthony; Bertilsson, Stefan; Bhatnagar, Jennifer M.; Bird, Jordan T.; Blanchard, Jeffrey L.; Blumer-Schuette, Sara E.; Bohannan, Brendan; Borton, Mikayla A.; Brady, Allyson; Brawley, Susan H.; Brodie, Juliet; Brown, Steven; Brum, Jennifer R.; Brune, Andreas; Bryant, Donald A.; Buchan, Alison; Buckley, Daniel H.; Buongiorno, Joy; Cadillo-Quiroz, Hinsby; Caffrey, Sean M.; Campbell, Ashley N.; Campbell, Barbara; Carr, Stephanie; Carroll, JoLynn; Cary, S. Craig; Cates, Anna M.; Cattolico, Rose Ann; Cavicchioli, Ricardo; Chistoserdova, Ludmila; Coleman, Maureen L.; Constant, Philippe; Conway, Jonathan M.; Mac Cormack, Walter P.; Crowe, Sean; Crump, Byron; Currie, Cameron; Daly, Rebecca; DeAngelis, Kristen M.; Denef, Vincent; Denman, Stuart E.; Desta, Adey; Dionisi, Hebe; Dodsworth, Jeremy; Dombrowski, Nina; Donohue, Timothy; Dopson, Mark; Driscoll, Timothy; Dunfield, Peter; Dupont, Christopher L.; Dynarski, Katherine A.; Edgcomb, Virginia; Edwards, Elizabeth A.; Elshahed, Mostafa S.; Figueroa, Israel; Flood, Beverly; Fortney, Nathaniel; Fortunato, Caroline S.; Francis, Christopher; Gachon, Claire M. M.; Garcia, Sarahi L.; Gazitua, Maria C.; Gentry, Terry; Gerwick, Lena; Gharechahi, Javad; Girguis, Peter; Gladden, John; Gradoville, Mary; Grasby, Stephen E.; Gravuer, Kelly; Grettenberger, Christen L.; Gruninger, Robert J.; Guo, Jiarong; Habteselassie, Mussie Y.; Hallam, Steven J.; Hatzenpichler, Roland; Hausmann, Bela; Hazen, Terry C.; Hedlund, Brian; Henny, Cynthia; Herfort, Lydie; Hernandez, Maria; Hershey, Olivia S.; Hess, Matthias; Hollister, Emily B.; Hug, Laura A.; Hunt, Dana; Jansson, Janet; Jarett, Jessica; Kadnikov, Vitaly V.; Kelly, Charlene; Kelly, Robert; Kelly, William; Kerfeld, Cheryl A.; Kimbrel, Jeff; Klassen, Jonathan L.; Konstantinidis, Konstantinos T.; Lee, Laura L.; Li, Wen-Jun; Loder, Andrew J.; Loy, Alexander; Lozada, Mariana; MacGregor, Barbara; Magnabosco, Cara; Maria da Silva, Aline; McKay, R. Michael; McMahon, Katherine; McSweeney, Chris S.; Medina, Monica; Meredith, Laura; Mizzi, Jessica; Mock, Thomas; Momper, Lily; Moran, Mary Ann; Morgan-Lang, Connor; Moser, Duane; Muyzer, Gerard; Myrold, David; Nash, Maisie; Nesb, Camilla L.; Neumann, Anthony P.; Neumann, Rebecca B.; Noguera, Daniel; Northen, Trent; Norton, Jeanette; Nowinski, Brent; Nusslein, Klaus; O'Malley, Michelle A.; Oliveira, Rafael S.; Maia de Oliveira, Valeria; Onstott, Tullis; Osvatic, Jay; Ouyang, Yang; Pachiadaki, Maria; Parnell, Jacob; Partida-Martinez, Laila P.; Peay, Kabir G.; Pelletier, Dale; Peng, Xuefeng; Pester, Michael; Pett-Ridge, Jennifer; Peura, Sari; Pjevac, Petra; Plominsky, Alvaro M.; Poehlein, Anja; Pope, Phillip B.; Ravin, Nikolai; Redmond, Molly C.; Reiss, Rebecca; Rich, Virginia; Rinke, Christian; Rodrigues, Jorge L. Mazza; Rodriguez-Reillo, William; Rossmassler, Karen; Sackett, Joshua; Salekdeh, Ghasem Hosseini; Saleska, Scott; Scarborough, Matthew; Schachtman, Daniel; Schadt, Christopher W.; Schrenk, Matthew; Sczyrba, Alexander; Sengupta, Aditi; Setubal, Joao C.; Shade, Ashley; Sharp, Christine; Sherman, David H.; Shubenkova, Olga V.; Sierra-Garcia, Isabel Natalia; Simister, Rachel; Simon, Holly; Sjoling, Sara; Slonczewski, Joan; Correa de Souza, Rafael Soares; Spear, John R.; Stegen, James C.; Stepanauskas, Ramunas; Stewart, Frank; Suen, Garret; Sullivan, Matthew; Sumner, Dawn; Swan, Brandon K.; Swingley, Wesley; Tarn, Jonathan; Taylor, Gordon T.; Teeling, Hanno; Tekere, Memory; Teske, Andreas; Thomas, Torsten; Thrash, Cameron; Tiedje, James; Ting, Claire S.; Tully, Benjamin; Tyson, Gene; Ulloa, Osvlado; Valentine, David L.; Van Goethem, Marc W.; VanderGheynst, Jean; Verbeke, Tobin J.; Vollmers, John; Vuillemin, Aurele; Waldo, Nicholas B.; Walsh, David A.; Weimer, Bart C.; Whitman, Thea; van der Wielen, Paul; Wilkins, Michael; Williams, Timothy J.; Woodcroft, Ben; Woolet, Jamie; Wrighton, Kelly; Ye, Jun; Young, Erica B.; Youssef, Noha H.; Yu, Feiqiao Brian; Zemskaya, Tamara I.; Ziels, Ryan; Woyke, Tanja; Mouncey, Nigel J.; Ivanova, Natalia N.; Kyrpides, Nikos C.; Eloe-Fadrosh, Emiley A. (2021). A genomic catalog of Earth's microbiomes. Nature Biotechnology 39(4): 499--509. https://doi.org/10.1038/s41587-020-0718-6
- Nayfach, Stephen; Shi, Zhou Jason; Seshadri, Rekha; Pollard, Katherine S.; Kyrpides, Nikos C. (2019). New insights from uncultivated genomes of the global human gut microbiome. Nature 568(7753): 505--510. https://doi.org/10.1038/s41586-019-1058-x
- Nelson, William C.; Tully, Benjamin J.; Mobberley, Jennifer M. (2020). Biases in genome reconstruction from metagenomic data. PeerJ 8: e10119. https://doi.org/10.7717/peerj.10119
- Orakov, Askarbek; Fullam, Anthony; Coelho, Luis Pedro; Khedkar, Supriya; Szklarczyk, Damian; Mende, Daniel R.; Schmidt, Thomas S. B.; Bork, Peer (2021). GUNC: detection of chimerism and contamination in prokaryotic genomes. Genome Biology 22(1): 178. https://doi.org/10.1186/s13059-021-02393-0
- Orellana, Luis H.; Kruger, Karen; Sidhu, Chandni; Amann, Rudolf (2023). Comparing genomes recovered from time-series metagenomes using long- and short-read sequencing technologies. Microbiome 11(1): 105. https://doi.org/10.1186/s40168-023-01557-3
- Pan, Shaojun; Zhu, Chengkai; Zhao, Xing-Ming; Coelho, Luis Pedro (2022). A deep siamese neural network improves metagenome-assembled genomes in microbiome datasets across different environments. Nature Communications 13(1): 2326. https://doi.org/10.1038/s41467-022-29843-y
- Parks, Donovan H.; Imelfort, Michael; Skennerton, Connor T.; Hugenholtz, Philip; Tyson, Gene W. (2015). CheckM: assessing the quality of microbial genomes recovered from isolates, single cells, and metagenomes. Genome Research 25(7): 1043--1055. https://doi.org/10.1101/gr.186072.114
- Pasolli, Edoardo; Asnicar, Francesco; Manara, Serena; Zolfo, Moreno; Karcher, Nicolai; Armanini, Federica; Beghini, Francesco; Manghi, Paolo; Tett, Adrian; Ghensi, Paolo; Collado, Maria Carmen; Rice, Benjamin L.; DuLong, Casey; Morgan, Xochitl C.; Golden, Christopher D.; Quince, Christopher; Huttenhower, Curtis; Segata, Nicola (2019). Extensive Unexplored Human Microbiome Diversity Revealed by Over 150,000 Genomes from Metagenomes Spanning Age, Geography, and Lifestyle. Cell 176(3): 649--662.e20. https://doi.org/10.1016/j.cell.2019.01.001
- Pellegrinetti, Thierry Alexandre; Molligan, Joshua; Mendes, Lucas William; Pedrinho, Alexandre; Perez-Lopez, Edel (2026). Rethinking metagenome-assembled genome completeness: are we truly recovering complete genomes?. Frontiers in Microbiology 17: 1884628. https://doi.org/10.3389/fmicb.2026.1884628
- Puente-Sanchez, Fernando; Hoetzinger, Matthias; Buck, Moritz; Bertilsson, Stefan (2023). Exploring environmental intra-species diversity through non-redundant pangenome assemblies. Molecular Ecology Resources. https://doi.org/10.1111/1755-0998.13826
- Rocha, Ulisses; Kasmanas, Jonas Coelho; Toscan, Rodolfo; Sanches, Danilo S.; Magnusdottir, Stefania; Saraiva, Joao Pedro (2024). Simulation of 69 microbial communities indicates sequencing depth and false positives are major drivers of bias in prokaryotic metagenome-assembled genome recovery. PLOS Computational Biology 20(10): e1012530. https://doi.org/10.1371/journal.pcbi.1012530
- Royalty, Taylor M.; Steen, Andrew D. (2019). Theoretical and Simulation-Based Investigation of the Relationship between Sequencing Effort, Microbial Community Richness, and Diversity in Binning Metagenome-Assembled Genomes. mSystems 4(5): e00384-19. https://doi.org/10.1128/mSystems.00384-19
- Sczyrba, Alexander; others (2017). Critical Assessment of Metagenome Interpretation: a benchmark of metagenomics software. Nature Methods 14(11): 1063--1071. https://doi.org/10.1038/nmeth.4458
- Sereika, Mantas; Kirkegaard, Rasmus Hansen; Karst, Sren Michael; Michaelsen, Thomas Yssing; Srensen, Emil Aarre; Wollenberg, Rasmus Dam; Albertsen, Mads (2022). Oxford Nanopore R10.4 long-read sequencing enables the generation of near-finished bacterial genomes from pure cultures and metagenomes without short-read or reference polishing. Nature Methods 19(7): 823--826. https://doi.org/10.1038/s41592-022-01539-7
- Sereika, Mantas; Mussig, Aaron James; Jiang, Chenjing; Knudsen, Kalinka Sand; Jensen, Thomas Bygh Nymann; Petriglieri, Francesca; Yang, Yu; Jrgensen, Vibeke Rudkjbing; Delogu, Francesco; Srensen, Emil Aarre; Nielsen, Per Halkjr; Singleton, Caitlin Margaret; Hugenholtz, Philip; Albertsen, Mads (2025). Genome-resolved long-read sequencing expands known microbial diversity across terrestrial habitats. Nature Microbiology 10(8): 2018--2030. https://doi.org/10.1038/s41564-025-02062-z
- Shaiber, Alon; Eren, A. Murat (2019). Composite Metagenome-Assembled Genomes Reduce the Quality of Public Genome Repositories. mBio 10(3): e00725-19. https://doi.org/10.1128/mBio.00725-19
- Singleton, Caitlin M.; Petriglieri, Francesca; Kristensen, Jannie M.; Kirkegaard, Rasmus H.; Michaelsen, Thomas Y.; Andersen, Martin H.; Kondrotaite, Zivile; Karst, Sren M.; Dueholm, Morten S.; Nielsen, Per H.; Albertsen, Mads (2021). Connecting structure to function with the recovery of over 1000 high-quality metagenome-assembled genomes from activated sludge using long-read sequencing. Nature Communications 12(1): 2009. https://doi.org/10.1038/s41467-021-22203-2
- Tettelin, Herve; Masignani, Vega; Cieslewicz, Michael J.; others (2005). Genome analysis of multiple pathogenic isolates of Streptococcus agalactiae: Implications for the microbial pan-genome. Proceedings of the National Academy of Sciences 102(39): 13950--13955. https://doi.org/10.1073/pnas.0506758102
- Tonkin-Hill, Gerry; MacAlasdair, Neil; Ruis, Christopher; Weimann, Aaron; Horesh, Gal; Lees, John A.; Gladstone, Rebecca A.; Lo, Stephanie; Beaudoin, Christopher; Floto, R. Andres; Frost, Simon D. W.; Corander, Jukka; Bentley, Stephen D.; Parkhill, Julian (2020). Producing polished prokaryotic pangenomes with the Panaroo pipeline. Genome Biology 21(1): 180. https://doi.org/10.1186/s13059-020-02090-4
- Zhang, Zhi-Feng; Liu, Li-Rui; Pan, Yue-Ping; Pan, Jie; Li, Meng (2023). Long-read assembled metagenomic approaches improve our understanding on metabolic potentials of microbial community in mangrove sediments. Microbiome 11: 188. https://doi.org/10.1186/s40168-023-01630-x
