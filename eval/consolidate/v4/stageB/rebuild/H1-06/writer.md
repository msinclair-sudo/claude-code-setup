# Phylogenetic depth of prokaryotic traits and rank-wise environmental structuring: writer's view

> [!abstract] About this view
> What the research found, for writing from. Each claim gives who found it, the setting it holds for, the kind of evidence, its standing where the research stated one, and for an absence whether it was searched for. A claim with no standing given has none stated in the research; "limited by access" means a source was not read in full, which is not the same as weak evidence. Sources are listed at the end. The view is generated from the knowledge note `Phylogenetic depth of prokaryotic traits and rank-wise environmental structuring.md`, where every claim is checked against the research.

## What the research found, by question

### H1-06

**D1. At what phylogenetic depth are prokaryotic environmental preferences (for example to pH or moisture) and genome-encoded metabolic traits conserved, and does environmental structuring of community composition persist when organisms are grouped at progressively coarser ranks from species to phylum?**

*Answer, as corrected by a second reader.*

A1 (environmental preferences): natural systems, measured for pH only, SINGLE SOURCE (Ramoneda et al. 2023). Signal is significant in 4 of 5 datasets but weak (Pagel's lambda 0.22 to 0.78, Moran's I < 0.25 at all depths), there is no consenTRAIT-style depth, and families span 3.7 to 4.2 pH units. Moisture and salinity have not been measured in natural systems: the rank-resolved results are engineered (Lennon 2012, Morrissey and Franklin 2015). Temperature is inferred within one phylum (Farrell). The 'inconsistent' label only emerges when natural evidence is set beside engineered results or a preprint that measures a different quantity (CCA loadings), so it should not stand as the natural-system verdict. A2 (metabolic traits): measured (inferred from genomes) and inconsistent in absolute depth between datasets and trees, while the relative ordering is consistent. This is supported, but the load-bearing Martiny 2013 values were not re-checked by the synthesiser, which records an unresolved transcription discrepancy. B: measured with group number (and member count) controlled, SINGLE SOURCE (Lu et al. 2016), and conditional on that paper's null design, which could not be re-verified here (paywalled; only the abstract was confirmed). Direction: explained variance rises or stays constant from species to order, with dataset-specific falls at class or phylum. Abundance evenness among groups was not controlled.

*Answer, as the research gave it; a second reader reviewed it and left it as given.* **6. Verdicts**

- **A1, environmental preferences:** measured and inconsistent between methods, taxonomies or datasets. Removing Ramoneda et al. 2023 (Ramoneda et al. 2023) would leave one natural-system preprint (Chakraverti-Wuerthwein et al. 2026), and the verdict would move towards "not measured in this setting" for natural systems. - **A2, genome-encoded metabolic traits:** measured and inconsistent between methods, taxonomies or datasets (inferred). The ordering by complexity is consistent; the absolute depths are not. The inconsistency label leans chiefly on Sun et al. 2021 (Sun et al. 2021), with Parras-Moltó et al. 2021 (Parras-Molto and Aguirre de Carcer 2021). - **B, rank-wise environmental structuring:** measured with group number and size controlled, SINGLE SOURCE, Lu et al. 2016 (Lu et al. 2016). Direction: explained variance increases or stays constant from species to order; in soils it peaks at class and declines at phylum; in seawater the pattern varies by dataset. Removing Lu et al. 2016 drops the verdict to "measured without controlling group number and size".

## Concepts

In an order where each concept comes after the ones it builds on; the order means nothing more.

### How depth of conservation and phylogenetic signal are expressed

- Pagel's lambda is a measure of phylogenetic correlation that normally varies between 0 (phylogenetic independence) and 1 (traits covary in direct proportion to shared evolutionary history). (Freckleton et al. 2002)
  Background, not from the research.
- Blomberg's K is a descriptive statistic that allows valid comparisons of the amount of phylogenetic signal across traits; K below one means less signal than expected. (Blomberg et al. 2003)
  Background, not from the research.
- consenTRAIT's tau_D is the mean 16S rRNA distance from the root of clades in which at least 90% of members share a trait. (Martiny et al. 2013)
  Holds for: the consenTRAIT method.
- Phylogenetic signal statistics (Pagel's lambda, Blomberg's K, Moran's I correlograms, D) measure how well a trait tracks the tree without giving one depth. (Ramoneda et al. 2023; Goberna and Verdu 2016; Morrissey et al. 2016)
  Holds for: the signal statistics used in the sources read.
- Rank-wise analyses of community composition use taxonomies, not trees, and the taxonomy differs between studies: Greengenes, SILVA or RDP, GTDB, a curated gyrB taxonomy, or no ranks at all, only sequence-identity thresholds. Rank labels differ between these taxonomies, and identity thresholds are not ranks. (Lopez-Mondejar et al. 2022; Royalty and Steen 2019; Hoffert et al. 2026; Barnum et al. 2024; Ramoneda et al. 2023; Lennon et al. 2012; Isobe et al. 2019; Lu et al. 2016; Mayjonade et al. 2024; Bay et al. 2020; Quiroga et al. 2022; Schmidt et al. 2014)
  Holds for: the rank-wise and depth studies the review read.
- A depth in 16S rRNA distance cannot be converted into a rank. (the reviewer's synthesis)
  Holds for: depths quoted in 16S rRNA distance.
- Depth values from different trees or datasets are not commensurable. (Sun et al. 2021)
  Holds for: tau_D on different trees and genome sets.
- Much of the apparent disagreement in this literature comes from the two halves of the question using different yardsticks: depth on a tree for traits, and ranks of a taxonomy for community composition. (the reviewer's synthesis)
  Holds for: the literature the review read.

### What an environmental preference is

- An environmental "preference" can be (a) a growth optimum measured on isolates, (b) a field optimum inferred from where an ASV is most abundant, or (c) a response to an experimental perturbation; type (c) comes from engineered systems. (the reviewer's synthesis)
  Holds for: the sources the review read.

### pH preference in natural systems

Builds on: How depth of conservation and phylogenetic signal are expressed, What an environmental preference is.

- Phylogenetic signal for pH preference was significant in four of five datasets but weak (Pagel's lambda 0.22 to 0.78), and correlogram Moran's I stayed below 0.25 at every depth, shallow ones included; there is no consenTRAIT-style depth. (Ramoneda et al. 2023)
  Holds for: natural soil and freshwater; 4,568 ASVs from five datasets (795 soil and 675 freshwater samples, pH about 3 to 10); pH preference defined as the pH of maximal field abundance; SILVA 138 taxonomy and RAxML trees of 16S; the critic verified lambda and Moran's I in the source.
  Evidence: measured; a single source.
- ASVs within single families spanned 3.7 to 4.2 pH units: Xanthobacteraceae in soil 4.01 to 8.20 (4.19 units), Chitinophagaceae in freshwater 4.63 to 8.35 (3.72 units). (Ramoneda et al. 2023)
  Holds for: natural soil and freshwater datasets of Ramoneda et al. 2023; the critic's reading of the source.
- A phylum-level tendency seen in one dataset (acidophilic Acidobacteria in freshwater) did not recur. (Ramoneda et al. 2023)
  Holds for: natural soil and freshwater datasets of Ramoneda et al. 2023.
  Evidence: measured.
- The authors conclude that "phylum-level information provides relatively little insight into bacterial pH preferences" and turn to gene content instead. (Ramoneda et al. 2023)
  Holds for: natural soil and freshwater datasets of Ramoneda et al. 2023; the critic verified the phylum quote.
  Evidence: measured.
- A genome-based model of pH preference, validated on an independent UK dataset, reached R2 = 0.21 (MAE 0.93 pH units). (Ramoneda et al. 2023)
  Holds for: independent UK validation dataset; the critic verified R2 = 0.21 and MAE 0.93.
- Only 6 to 24% of ASVs matched a GTDB genome, and about 35% of those genomes were MAGs or SAGs. (Ramoneda et al. 2023)
  Holds for: the bound on Ramoneda et al.'s genome-based analysis; the critic verified both figures.
- In CCA of global topsoil (N = 217) and ocean (N = 125) 16S surveys, OTU loadings on the first canonical direction, which aligns with pH in soil and with depth in the ocean, had strong phylogenetic signal (a modified tau_D and Pagel's lambda); secondary canonical directions had weak or no signal. (Chakraverti-Wuerthwein et al. 2026)
  Holds for: natural; a preprint; numeric tau_D values appear only in figures, so the strong-signal claim is qualitative, with no number quoted; the permutation null shuffles sample labels rather than preserving group structure; a canonical loading is not a per-ASV optimum.
  Evidence: measured; a single source.
- The field-optimum and canonical-loading results are not in direct contradiction, but together they show that whether "pH preference" looks phylogenetically structured depends on how the preference is operationalised. (Ramoneda et al. 2023; Chakraverti-Wuerthwein et al. 2026)
  Holds for: built from two sources, one a preprint; the critic: a methodological argument that underpins the 'inconsistent' A1 verdict.
  Evidence: the reviewer's reading.
- The only large natural-system test of pH preference finds weak signal and poor prediction by rank. (Ramoneda et al. 2023)
  Holds for: the one large natural-system study of pH preference, in soil and freshwater.
  Evidence: a single source.

### Moisture and salinity preferences (engineered)

Builds on: How depth of conservation and phylogenetic signal are expressed, What an environmental preference is.

- Across seven RDP ranks against permutation nulls, phylum level held 52% of the variance in optimum water potential and 58% in niche breadth, and strain level held 21 to 29% against 58 to 65% expected by chance. (Lennon et al. 2012)
  Holds for: engineered: 23 bacterial and 22 fungal soil isolates respired across a manipulated water-potential gradient (lab isolates, n = 23 bacteria); the authors caution that isolate numbers are small (5 bacterial phyla, 19 genera); the only direct rank-resolved measurement of a moisture optimum found.
  Evidence: measured; a single source.
- Salinity-preferring phylotypes were phylogenetically clustered both tree-wide and near the tips (freshwater-preferring: SES-PD -3.5, NTI 4.3; saltwater-preferring: SES-PD -5.4, NTI 5.2, p < 0.01); no depth statistic was reported. (Morrissey and Franklin 2015)
  Holds for: engineered: a reciprocal transplant between tidal freshwater and brackish marsh soils; Greengenes 97% OTUs, n = 5 per treatment.
  Evidence: measured; a single source.
- At class level, Betaproteobacteria were enriched among freshwater-preferring phylotypes and Alpha- and Gammaproteobacteria among saltwater-preferring ones. (Morrissey and Franklin 2015)
  Holds for: engineered: the tidal freshwater and brackish marsh reciprocal transplant.
  Evidence: measured; a single source.
- Moisture and salinity preferences have not been measured in natural systems: the rank-resolved results are engineered, and the deep-rank moisture result has no natural-system rank-wise counterpart among the sources read. (Lennon et al. 2012; Morrissey and Franklin 2015)
  Holds for: natural systems; the engineered isolate and transplant studies (Lennon 2012, Morrissey and Franklin 2015).
  The research does not say whether this was searched for.

### Temperature optimum

Builds on: How depth of conservation and phylogenetic signal are expressed, What an environmental preference is.

- Within the phylum Thermotogota (64 genomes), optimal growth temperature has strong signal (Pagel's lambda 0.93), yet ancestral reconstruction places several secondary shifts to mesophily and hyperthermophily, and most of the 68 OGT-associated genes have histories of horizontal transfer: strong signal within a phylum coexists with repeated shifts. (Farrell et al. 2025)
  Holds for: one phylum, Thermotogota, 64 genomes.
  Evidence: derived; a single source.

### Compilations and models of traits and growth optima

Builds on: How depth of conservation and phylogenetic signal are expressed, What an environmental preference is.

- Across 990 traits collated on a SILVA r119 tree, binary, mostly gene-presence, traits had mean -D+1 = 0.93 (98% significant) and continuous traits mean K = 0.16 (74% significant). (Goberna and Verdu 2016)
  Holds for: a compilation; read in full by one search agent only, so it carries no weight on its own; the critic: still listed in the A1 verdict's evidence classes.
  Evidence: modelled; limited by access (a source was not read in full; not the same as weak evidence).
- The compilation is internally inconsistent on environmental optima: it lists optimal pH and temperature and moisture niche breadth among "the most conserved continuous traits", and elsewhere places optimal pH, salt tolerance and moisture niche breadth among traits with "moderate signals". (Goberna and Verdu 2016)
  Holds for: 990 traits on a SILVA r119 tree; read in full by one search agent only, carrying no weight on its own.
  Evidence: limited by access (a source was not read in full; not the same as weak evidence).
- Only 9.9% of continuous and 8.6% of binary traits met the compilation's threshold for accurate phylogenetic prediction. (Goberna and Verdu 2016)
  Holds for: 990 traits on a SILVA r119 tree; read in full by one search agent only.
  Evidence: modelled; limited by access (a source was not read in full; not the same as weak evidence).
- Growth optima predicted from amino-acid composition for 15,596 BacDive organisms reached, under family-level holdout, R2 0.73 for temperature, 0.81 for salinity and 0.48 for pH, with 92% balanced accuracy for oxygen tolerance. (Barnum et al. 2024)
  Holds for: GTDB r214; a preprint whose publication status is unverified.
  Evidence: modelled.
- A phylogeny-only comparison model failed at higher-rank holdouts except for oxygen tolerance, which stayed moderately accurate up to order and class. (Barnum et al. 2024)
  Holds for: 15,596 BacDive organisms, GTDB r214; a preprint.
  Evidence: modelled.
- Among six genome-inferred traits, oxygen tolerance had much of its variance at deep nodes, often near phylum, but was "not universally conserved at the phylum level". (Hoffert et al. 2026)
  Holds for: 50,745 GTDB genomes.
  Evidence: derived; a single source.

### Depth of responses to experimental perturbations (engineered, kept separate)

Builds on: How depth of conservation and phylogenetic signal are expressed, What an environmental preference is.

- Responses to N addition across 13 field experiments on five continents were conserved at tau_D 0.016 to 0.020 per location (0.017 merged). (Isobe et al. 2019)
  Holds for: engineered perturbation responses (N addition); taxonomy RDP on SILVA 128; the authors equate this to roughly genus, but the review's own Section 1 says a 16S depth cannot be converted into a rank (the critic: inconsistent use); the critic verified the figures.
- A correlogram on the same N-addition data detected response similarity out to 22% 16S divergence, which the authors note is a less conservative depth metric. (Isobe et al. 2019)
  Holds for: engineered perturbation responses, 13 N-addition field experiments; the critic verified the 22% correlogram depth.
- Warming, drought, elevated CO2, P addition and liming gave tau_D 0.016 to 0.024, with little difference among perturbations, and clades responding to one perturbation rarely responded to another. (Isobe et al. 2020)
  Holds for: engineered perturbation responses of soil bacteria.
- In leaf litter, only positive bacterial responses were significantly conserved; negative responses were not (drought decrease P = 0.541; N decrease P = 0.763). (Amend et al. 2016)
  Holds for: engineered perturbation responses; one litter study.
- Coarse groups can hide opposing finer ones in the N-addition responses: Gammaproteobacteria as a class had no consistent response while one genus within it responded positively, and an order and a family within it responded in opposite directions. (Isobe et al. 2019)
  Holds for: engineered N-addition experiments (one study); the critic verified the Gammaproteobacteria example.
- The same N-addition study also reports consistent phylum- and class-level responses: phylum Actinobacteria positive; classes Betaproteobacteria and Deltaproteobacteria negative. (Isobe et al. 2019)
  Holds for: engineered N-addition experiments; the review leaves this out, citing only the 'coarse hides fine' example.
- In situ growth measured by qSIP had K 0.38 to 0.54 and lambda 0.96 to 0.98. (Morrissey et al. 2016)
  Holds for: one forest soil; in situ growth, reported among the perturbation responses.
- Within a single 16S OTU (Curtobacterium, minimum 83.2% ANI), the drought response appeared conserved across clades while carbohydrate-use degree and degradation temperature preference varied among clades. (Chase et al. 2017)
  Holds for: one abundant terrestrial bacterium, a single 16S OTU (Curtobacterium); natural.
  Evidence: measured; a single source.
- Perturbation responses are a different quantity from environmental optima; in 16S terms they cluster at tau_D 0.016 to 0.020 per location for N addition (0.017 merged) and at 0.016 to 0.024 for warming, drought, elevated CO2, P addition and liming, which the review calls roughly genus depth. (Isobe et al. 2019; Isobe et al. 2020; Amend et al. 2016)
  Holds for: engineered N-addition and global-change experiments; the review also cites a litter study, which gives no tau_D (only positive responses were significantly conserved); the critic: equating these depths with roughly genus is inconsistent with the review's own statement that a 16S depth cannot be converted into a rank.

### Depth of conservation of environmental preferences, overall (Part A1)

Builds on: pH preference in natural systems, Moisture and salinity preferences (engineered), Temperature optimum, Compilations and models of traits and growth optima, Depth of responses to experimental perturbations (engineered, kept separate).

- For environmental preferences in natural systems, depth of conservation is measured for pH only, from a single source (Ramoneda et al. 2023): signal is significant in 4 of 5 datasets but weak, there is no consenTRAIT-style depth, and families span 3.7 to 4.2 pH units. Moisture and salinity have not been measured in natural systems (the rank-resolved results are engineered: Lennon 2012, Morrissey and Franklin 2015), and temperature is inferred within one phylum (Farrell). (Ramoneda et al. 2023; Lennon et al. 2012; Morrissey and Franklin 2015; Farrell et al. 2025)
  Holds for: natural systems; the critic's split verdict: pH measured, natural, single source, weak signal, no depth; moisture and salinity not measured in natural systems.
  Evidence: a single source; rated "Measured and inconsistent between methods, taxonomies or datasets" by the research; a second reader disputes this: A1 over-reaches.
- The 'inconsistent' label for environmental preferences only emerges when natural evidence is set beside engineered results or a preprint that measures a different quantity (CCA loadings). The body's own synthesis says the natural evidence is one large study (weak signal) plus a preprint on a non-comparable quantity (canonical loadings), and the inconsistency behind the verdict comes from comparing that natural study with engineered isolate and transplant work. (Ramoneda et al. 2023; Lennon et al. 2012; Morrissey and Franklin 2015; Chakraverti-Wuerthwein et al. 2026)
  Holds for: the critic's reading of the body; engineered evidence may not carry a natural-system verdict (Common rule 10).
- No consenTRAIT depth for any environmental optimum (pH, temperature or moisture) was found. (a search result)
  Holds for: routes: Europe PMC REST keyword, DOI and title search plus fullTextXML; the 'consenTRAIT AND OPEN_ACCESS' query (23 hits screened); WebSearch, among others.
  Evidence: a search result.
  Searched, not found (note: "not found by these routes: (1) any consentrait tau_d for ph, temperature or moisture optima").
- The frequently repeated statement that pH optimum, soil moisture optimum and habitat association sit in deep clades appears in Martiny et al. 2013 as a discussion claim resting on other studies; that paper does not measure any of these. The primary studies it cites were either not obtained (Placella et al. 2012, Philippot et al. 2010) or were read and give a more mixed picture (Lennon et al. 2012). (Martiny et al. 2013; Lennon et al. 2012; Placella et al. 2012; Philippot et al. 2010)
  Holds for: a secondary discussion statement.
  Evidence: asserted.
- The evidence on environmental preferences does not converge on a single depth. The claim that environmental optima are conserved at deep ranks rests, among full-text sources, on an engineered study of 23 bacterial isolates for moisture and on an asserted secondary statement; natural evidence for environmental optima is thin, and the two coarse-rank optimum results are engineered. (Martiny et al. 2013; Lennon et al. 2012; Morrissey and Franklin 2015)
  Holds for: the sources the review read for Part A1.
- By evidence class, the Part A1 sources are: measured (Ramoneda; the preprint Chakraverti-Wuerthwein; engineered: Lennon, Morrissey and Franklin), inferred (Farrell), and modelled or compiled (Goberna and Verdu; Barnum, a preprint). (Barnum et al. 2024; Ramoneda et al. 2023; Lennon et al. 2012; Morrissey and Franklin 2015; Goberna and Verdu 2016; Farrell et al. 2025; Chakraverti-Wuerthwein et al. 2026)
  Holds for: the critic: Goberna and Verdu was not re-opened by the synthesiser and is labelled as carrying no weight, yet it is listed here.
- Without Ramoneda et al. 2023, the only natural-system depth evidence left for any environmental preference is a single preprint, and Part A1 would move towards 'not measured in this setting' for natural systems. (Ramoneda et al. 2023; Chakraverti-Wuerthwein et al. 2026)
  Holds for: the review's sensitivity analysis.

### Depth of conservation of genome-encoded metabolic traits (Part A2)

Builds on: How depth of conservation and phylogenetic signal are expressed.

- The Part A2 depths are inferred from genome annotation, not measured phenotypically, except for the Biolog substrates in Martiny 2013. (Martiny et al. 2013)
  Holds for: genome-encoded metabolic traits.
  Evidence: derived.
- On 2,229 SEED genomes (26 phyla, 16S trees), 93% of 89 traits were non-randomly distributed. (Martiny et al. 2013)
  Holds for: SEED genomes on 16S trees; rests on two independent search-agent readings.
  Evidence: derived; limited by access (a source was not read in full; not the same as weak evidence).
- Oxygenic photosynthesis had a median tau_D of about 0.10 to 0.11 (one clade), sulfate reduction 0.039 (20 clusters) and nitrogen fixation about 0.018 (54 clusters). (Martiny et al. 2013)
  Holds for: 2,229 SEED genomes, 16S trees; load-bearing in the A2 verdict, but resting on a search agent's transcription that disagrees with another agent on the overall range; the synthesiser could not re-open it and the critic could not obtain it (PMC3603392, not OA).
  Evidence: derived; limited by access (a source was not read in full; not the same as weak evidence).
- Growth on each of 70 carbon substrates (Biolog phenotypes, 738 strains) had tau_D below 0.011. (Martiny et al. 2013)
  Holds for: Biolog phenotypes of 738 strains; the paper could not be re-opened by the synthesiser or obtained by the critic.
  Evidence: measured; limited by access (a source was not read in full; not the same as weak evidence).
- Martiny et al. report that traits encoded by many genes sit deeper, with aerobic methane oxidation as a stated exception. (Martiny et al. 2013)
  Holds for: 2,229 SEED genomes, 16S trees.
  Evidence: derived; limited by access (a source was not read in full; not the same as weak evidence).
- The two search agents transcribed Martiny et al.'s overall tau_D range differently, 0.0011 to 0.101 quoted directly by one and 0.0029 to 0.11 by the other, and the discrepancy is unresolved. (Martiny et al. 2013)
  Holds for: the overall range in Martiny et al. 2013; the specific trait values are the load-bearing ones.
  Evidence: limited by access (a source was not read in full; not the same as weak evidence).
- Single enzymes are shallow: alkaline phosphatase, chitinase and beta-N-acetylglucosaminidase had tau_D 0.0098, 0.0080 and 0.0097, about 98% 16S identity. (Zimmerman et al. 2013)
  Holds for: 3,058 sequenced prokaryotic genomes.
  Evidence: derived.
- Cellulase had tau_D 0.013 and beta-glucosidase 0.034. (Berlemont and Martiny 2013)
  Holds for: 5,123 genomes.
  Evidence: derived.
- CAZyme traits had significant signal in most phyla, with depth varying by phylum (conserved-clade 16S divergence of 3 to 10% in Verrucomicrobiota and 0.1 to 0.5% in Firmicutes_A); beta-glucanases were significant in 73% of phyla tested, against 25% for alpha-glucanases. (Lopez-Mondejar et al. 2022)
  Holds for: natural; 9,143 high-quality MAGs from the GEM catalogue, GTDB phyla.
  Evidence: derived; a single source.
- The relative ordering of depths replicates across several studies on 16S trees: complex multi-gene pathways are deep (oxygenic photosynthesis about 0.10 to 0.11 16S distance; sulfate reduction 0.039), nitrogen fixation is intermediate (about 0.018), and single enzymes and substrate use are shallow (about 0.008 to 0.034). (Martiny et al. 2013; Zimmerman et al. 2013; Berlemont and Martiny 2013; Sun et al. 2021; Lopez-Mondejar et al. 2022)
  Holds for: 16S trees; the critic: supported, but the load-bearing Martiny 2013 values were not re-checked by the synthesiser, which records an unresolved transcription discrepancy.
  Evidence: derived; replicated.

### Dependence of absolute depths on genome sampling and tree

Builds on: Depth of conservation of genome-encoded metabolic traits (Part A2).

- In 2,730 marine genomes, chitinase tau_D was 0.0281 on a 16S tree and 0.0444 on a core-gene tree, three to five times Zimmerman's 0.008. (Zimmerman et al. 2013; Sun et al. 2021)
  Holds for: 2,730 marine genomes; a 16S tree and a core-gene tree.
- The authors attribute the difference to a denser sample of trait-positive genomes and state that tau_D values from different trees are not comparable. (Sun et al. 2021)
  Holds for: 2,730 marine genomes, 16S and core-gene trees.
- Depending on the enzyme, 13.5 to 100% of trait-positive genomes were singletons; singleton clusters are common. (Sun et al. 2021)
  Holds for: 2,730 marine genomes.
- Martiny et al. call their estimates "an upper bound for many functions" because many trait carriers sit in clusters of one: tau_D is an upper bound under undersampling, and the original authors call their depths upper bounds because of undersampling. (Martiny et al. 2013)
  Holds for: consenTRAIT depths on undersampled trees.
- On gene-content coherence, 44 coherent nodes appeared at 16S distances of 0.03 to 0.25 on a 16S tree but only five deep coherent subtrees on a GTDB 120-protein tree; class Actinobacteria was coherent while the shallower family Enterobacteriaceae was not. (Parras-Molto and Aguirre de Carcer 2021)
  Holds for: a 16S tree against a GTDB 120-protein tree.
  Evidence: a single source.
- For genome-encoded metabolic traits, depth of conservation is measured (inferred from genomes) and inconsistent in absolute depth between datasets and trees, while the relative ordering is consistent: absolute depths move with genome sampling density and tree choice, and their own authors describe them as upper bounds. (Martiny et al. 2013; Sun et al. 2021; Parras-Molto and Aguirre de Carcer 2021)
  Holds for: the critic: supported by the body, but the load-bearing Martiny 2013 values were not re-checked by the synthesiser.
  Evidence: derived; rated "Measured and inconsistent between methods, taxonomies or datasets" by the research.
- The 'inconsistent' label for metabolic traits rests mainly on Sun et al. 2021 (dataset and tree dependence of the same trait) together with Parras-Moltó et al. 2021; without Sun, 'measured, with depths, methods and taxonomy stated' would be defensible for the ordering. (Sun et al. 2021; Parras-Molto and Aguirre de Carcer 2021)
  Holds for: the review's sensitivity analysis.

### Partitioning genomic traits among taxonomic ranks

Builds on: How depth of conservation and phylogenetic signal are expressed.

- With GTDB ranks, ranks together explained 41.4% of the variance in 25 COG categories normalised for genome size: domain 3.2%, phylum 14.6%, class 4.1%, order 9.2%, family 4.8%, genus 5.5%; the contribution is non-monotonic across ranks. (Royalty and Steen 2019)
  Holds for: 13,735 lineages, GTDB ranks; the critic: correctly flagged single source in the body, but it carries weight in the A2 verdict without that flag.
  Evidence: a single source.
- Apparent within-phylum variability rose with the number of lineages sampled and levelled off after about 100 genomes, so undersampled phyla look falsely uniform. (Royalty and Steen 2019)
  Holds for: 13,735 lineages, GTDB ranks, COG categories.
  Evidence: a single source.
- Autotrophy and maximum growth rate had weaker signal than oxygen tolerance and GC content, and at least 25% of variance in four traits fell at a single split. (Hoffert et al. 2026)
  Holds for: 50,745 GTDB genomes.

### Genome incompleteness and conservation estimates

Builds on: Depth of conservation of genome-encoded metabolic traits (Part A2).

- No study found tests directly how genome incompleteness biases tau_D or signal statistics; its effect on depth estimates themselves has not been measured in any source read. (a search result)
  Holds for: the review's search, whose routes are listed in the note's provenance (including WebSearch on genome completeness with functional inference); the critic: the routes behind this not-found are not named in the body.
  Evidence: a search result.
  Searched, not found (note: "(3) any direct test of how genome incompleteness biases tau_d or signal statistics").
- Going from 70% to 100% completeness raised KEGG module fullness by 15 ± 10%; the bias was positive for 94% of 195 modules, persisted above 90% completeness, and was largest in Proteobacteria and in modules with few steps. (Eisenhofer et al. 2023)
  Holds for: subsampled complete genomes.
  Evidence: modelled; a single source.
- Subsampling a complete Pseudomonas aeruginosa genome to 70% moved its functional profile towards Bacillus subtilis. (Eisenhofer et al. 2023)
  Holds for: one complete genome, subsampled.
  Evidence: modelled.
- Removing 1% of sequence from each genome cut detected core gene families by more than 60% across 17 species; relaxing the core threshold to 90 to 95% eased this. (Li and Yin 2022)
  Holds for: 17 species; modelled.
  Evidence: modelled; a single source.
- For 116,884 MAGs against RefSeq, raw gene detection rates fell below model-corrected prevalences, and most KEGG orthologs were biased between culture-heavy and MAG references. (Albright and Louca 2023)
  Holds for: MAGs against RefSeq references.
  Evidence: a single source.
- Incompleteness pushed detected function down in single-source tests of modules, core genes and reference bias, with the size of the effect depending on module and phylum; the evidence is indirect but consistent in direction, and none of it measures the effect on conservation depth. (Eisenhofer et al. 2023; Li and Yin 2022; Albright and Louca 2023)
  Holds for: KEGG modules (modelled on subsampled complete genomes), core gene families (modelled) and reference genomes, one source each.
  Evidence: a single source.
- Consensus-threshold methods such as consenTRAIT (90% sharing) are exposed to false absences, which would fragment clades and push depth estimates shallower. (the reviewer's synthesis)
  Holds for: untested by any source; the critic: appropriately labelled as untested, but then echoed in Section 5 as a bound.
  Evidence: the reviewer's reading.
- Amino-acid-based optimum predictions stayed stable down to 10% completeness for oxygen, temperature and salinity, while pH error reached 0.4 units. (Barnum et al. 2024)
  Holds for: a preprint.

### Controlling group number and size across ranks

Builds on: How depth of conservation and phylogenetic signal are expressed.

- Lu et al. handled group number and group size with a null that "shuffled linkages between fine-taxa and broad-taxa level by level (remaining topology)", using 100 random linkage maps (tip-label shuffling for UniFrac); under this null, explained variance "remained constant or slightly decreased" with rank. (Lu et al. 2016)
  Holds for: the eight soil and seawater datasets Lu et al. reanalysed; the critic could not obtain the Methods and Results (nature.com paywall; not open access), so the null-model description rests on the search agent's reading; the note's provenance says the synthesiser re-opened cached full text for the null model.
  Evidence: limited by access (a source was not read in full; not the same as weak evidence).
- By preserving topology, the null holds the count of groups per level and the number of fine taxa per group fixed; it does not hold abundance evenness among groups fixed. (Lu et al. 2016)
  Holds for: Lu et al.'s topology-preserving null; the critic: the caveat about evenness is appropriate, and abundance evenness among groups was not controlled.
  Evidence: the reviewer's reading.
- No rank-wise composition-environment study other than Lu 2016 was found that controls group number and size; Schmidt 2014 controls them, but for identity thresholds and annotation consistency, not ranks. (a search result)
  Holds for: routes include citing papers of Lu et al. 2016 screened by title, and WebSearch on taxonomic sufficiency, taxonomic resolution with explained variation and ecological coherence with ranks.
  Evidence: a search result.
  Searched, not found (note: "(2) any rank-wise composition-environment study, other than lu 2016, that controls group number and size").

### Environmental structuring of community composition from fine to coarse ranks (Part B)

Builds on: Controlling group number and size across ranks.

- Across eight reanalysed datasets, environment-explained variance of Bray-Curtis composition (db-RDA adjusted R2) "either increased or remained constant with broadening taxonomic resolution from species to order or even phylum level". (Lu et al. 2016)
  Holds for: natural; four surface soils (n = 40 to 580) and four seawater datasets; closed-reference Greengenes 13_8 with copy-number correction, composition aggregated from otu97 to otu70 and from species to phylum; the critic confirmed this abstract sentence.
  Evidence: measured; a single source.
- In all four soils, R2 rose up to class (otu82 to otu76) and fell at phylum, with at least a 50% R2 increase from otu97 to otu94; pH was the strongest single variable. (Lu et al. 2016)
  Holds for: four surface soils, Greengenes 13_8; the critic: the soil class-peak details rest on the search agent's reading, since the critic could confirm only the abstract.
  Evidence: measured; a single source; limited by access (a source was not read in full; not the same as weak evidence).
- In seawater the shape varied by dataset: peaks at intermediate ranks (Tara surface and DCM), flat from species to order then a drop at class and phylum (English Channel time series), and a continuous rise to phylum (East China Sea shelf). (Lu et al. 2016)
  Holds for: four seawater datasets; the critic could confirm only the abstract, not the per-dataset seawater shapes.
  Evidence: measured; a single source; limited by access (a source was not read in full; not the same as weak evidence).
- In soils, the observed genus-to-class R2 was significantly above the topology-preserving shuffle null, which itself gave constant or slightly falling R2; the authors read the rise as phylogenetic niche conservatism. (Lu et al. 2016)
  Holds for: four surface soils; the critic could not obtain the Methods and Results.
  Evidence: measured; a single source; limited by access (a source was not read in full; not the same as weak evidence).
- Environmental structuring of community composition across ranks has been measured with group number (and member count) controlled, in a single source, conditional on that paper's null design: explained variance rises or stays constant from species to order, with dataset-specific falls at class or phylum (in soils it peaks at class and declines at phylum; in seawater the pattern varies by dataset); abundance evenness among groups was not controlled. (Lu et al. 2016)
  Holds for: natural; 4 soil and 4 seawater datasets; Greengenes 13_8 ranks and OTU thresholds from 97% to 70%; the critic: the review departs from the brief's expectation that such evidence may not exist, plausibly, but on one source whose control design was not independently re-verified.
  Evidence: a single source; rated "Measured with group number and size controlled, SINGLE SOURCE" by the research; a second reader disputes this: conditional on that paper's null design, which could not be re-verified; limited by access (a source was not read in full; not the same as weak evidence).
- Without Lu et al. 2016, the Part B verdict falls to 'measured without controlling group number and size'. (Lu et al. 2016)
  Holds for: the review's sensitivity analysis.
- Across 160 natural sites, habitat category explained little composition variance at any level and peaked at class (PERMANOVA R2: phylum 3.7%, class 6.3%, ASV 2.7%). (Mayjonade et al. 2024)
  Holds for: soils at 160 natural sites in southwest France; gyrB taxonomy; a preprint; group numbers ranged from 18 phyla to 769 ASVs and were not controlled.
- The share of individual groups significantly associated with soil physicochemistry fell from 59% at phylum to 30.2% at ASV, while plant-community associations rose from 19.7% to 48.7%. (Mayjonade et al. 2024)
  Holds for: 160 natural sites in southwest France; gyrB taxonomy; a preprint; group numbers not controlled.
- Community turnover was stronger at ASV resolution (an 82% drop in similarity over 160 km, against 50 to 60% for clustered or filtered data), but "less variation in community composition could be explained and partitioned for the high-resolution data set", and the rank order of predictors changed. The comparison is of the high-resolution set against clustered and/or rare-taxon-filtered data, by incidence-based variation partitioning. (Bay et al. 2020)
  Holds for: soils in the Negev; no ranks, only sequence-identity thresholds; one of the uncontrolled rank-wise studies.
- The pH-aligned first canonical axis stayed stable when OTUs were summed to genus, family and higher, while secondary axes were incoherent across resolutions. (Chakraverti-Wuerthwein et al. 2026)
  Holds for: a global preprint on topsoil (N = 217) and ocean (N = 125) 16S surveys; the null there does not preserve group structure; tau_D values appear only in figures.
- In an 11-year coastal time series, seasonal niches were coherent for some genera and families, but classes (Alphaproteobacteria, Gammaproteobacteria, Bacteroidia) were non-seasonal when aggregated; within at least three genera, niche similarity fell with 16S divergence. (Auladell et al. 2022)
  Holds for: marine bacteria in an 11-year coastal time series, not a spatial environment gradient; aggregation used random 80% ASV subsets, but group number was not equalised.
- The rank-wise studies other than Lu et al. 2016 are uncontrolled for group number and size, and two are preprints; they agree in part and conflict in part with it. (Mayjonade et al. 2024; Bay et al. 2020; Auladell et al. 2022; Chakraverti-Wuerthwein et al. 2026)
  Holds for: Mayjonade 2024, Bay 2020, Chakraverti-Wuerthwein 2026 and Auladell 2022.
- The rise in explained variance from otu97 to otu94 rests on Lu et al. 2016 alone: Bay et al. compare ASVs against clustered and/or filtered data, a different step, although its direction matches. (Lu et al. 2016; Bay et al. 2020)
  Holds for: the otu97-to-otu94 and genus rise in soils.
  Evidence: a single source.

### Rank-wise metrics other than composition-environment R2

Builds on: Environmental structuring of community composition from fine to coarse ranks (Part B).

- pH explained more of betaNTI (phylogenetic turnover, not composition) at ASV level (R2 0.20) than at OTU97 (0.08). (Quiroga et al. 2022)
  Holds for: Antarctic wetlands; unit counts uncontrolled.
- Abundance-occupancy relationships were weakest at species and roughly constant from genus to phylum. (Izabel-Shen et al. 2021)
  Holds for: marine bacterioplankton in an estuary.
- Across about one million full-length 16S sequences, the ecological consistency of habitat annotations, scored against random partitions with the same cluster count and size distribution, generally fell as OTU thresholds became stricter (finer) for complete and average linkage; single linkage behaved differently. (Schmidt et al. 2014)
  Holds for: identity thresholds only, not ranks; the design controls group number and size, but the response is annotation consistency, not environment-explained composition.
  Evidence: derived.

### How rank-wise structuring relates to trait depth

Builds on: Environmental structuring of community composition from fine to coarse ranks (Part B), Depth of responses to experimental perturbations (engineered, kept separate), pH preference in natural systems, Moisture and salinity preferences (engineered).

- The rise in explained variance from otu97 to about otu94 and genus matches where perturbation responses cluster (tau_D about 0.017 to 0.02), and the fall at phylum in soils and the class-level incoherence in a time series match the weak within-phylum pH signal and the opposing responses inside coarse groups. (Ramoneda et al. 2023; Isobe et al. 2019; Isobe et al. 2020; Lu et al. 2016; Auladell et al. 2022)
  Holds for: the critic: it links a natural-system composition result to engineered perturbation-response depths, breaking the natural/engineered separation, and presents a correspondence the sources do not test.
  Evidence: the reviewer's reading.
- None of the studies links composition structure to genome content, and an association between environment and composition at a rank is not evidence about the genomes of that rank. (the reviewer's synthesis)
  Holds for: the rank-wise composition studies the review read.

## Do not say

Wordings the research itself says are wrong or overstated, each with the reason and what to say instead.

- Do not write: "Environmental preferences are measured and inconsistent between methods, taxonomies or datasets in natural systems."
  Why: The A1 verdict over-reaches: the inconsistency only emerges when the one natural study is set beside engineered results or a preprint that measures a different quantity, so it should not stand as the natural-system verdict, and engineered evidence may not carry a natural-system verdict.
  Say instead: For environmental preferences in natural systems, depth of conservation is measured for pH only, from a single source (Ramoneda et al. 2023): signal is significant in 4 of 5 datasets but weak, there is no consenTRAIT-style depth, and families span 3.7 to 4.2 pH units. Moisture and salinity have not been measured in natural systems (the rank-resolved results are engineered: Lennon 2012, Morrissey and Franklin 2015), and temperature is inferred within one phylum (Farrell). (Ramoneda et al. 2023; Lennon et al. 2012; Morrissey and Franklin 2015; Farrell et al. 2025)
  Holds for: natural systems; the critic's split verdict: pH measured, natural, single source, weak signal, no depth; moisture and salinity not measured in natural systems.
  Evidence: a single source; rated "Measured and inconsistent between methods, taxonomies or datasets" by the research; a second reader disputes this: A1 over-reaches.
  Say instead: The 'inconsistent' label for environmental preferences only emerges when natural evidence is set beside engineered results or a preprint that measures a different quantity (CCA loadings). The body's own synthesis says the natural evidence is one large study (weak signal) plus a preprint on a non-comparable quantity (canonical loadings), and the inconsistency behind the verdict comes from comparing that natural study with engineered isolate and transplant work. (Ramoneda et al. 2023; Lennon et al. 2012; Morrissey and Franklin 2015; Chakraverti-Wuerthwein et al. 2026)
  Holds for: the critic's reading of the body; engineered evidence may not carry a natural-system verdict (Common rule 10).
- Do not write: "ASVs within single families spanned four or more pH units, in Xanthobacteraceae in soil and Chitinophagaceae in freshwater."
  Why: The family claim is partly wrong: Chitinophagaceae spans 4.63 to 8.35, 3.72 units, so it does not span four units.
  Say instead: ASVs within single families spanned 3.7 to 4.2 pH units: Xanthobacteraceae in soil 4.01 to 8.20 (4.19 units), Chitinophagaceae in freshwater 4.63 to 8.35 (3.72 units). (Ramoneda et al. 2023)
  Holds for: natural soil and freshwater datasets of Ramoneda et al. 2023; the critic's reading of the source.
- Do not write: "pH optimum, soil moisture optimum and habitat association are conserved in deep clades."
  Why: The statement appears in Martiny et al. 2013 as a discussion claim resting on other studies, and that paper does not measure any of these.
  Say instead: The frequently repeated statement that pH optimum, soil moisture optimum and habitat association sit in deep clades appears in Martiny et al. 2013 as a discussion claim resting on other studies; that paper does not measure any of these. The primary studies it cites were either not obtained (Placella et al. 2012, Philippot et al. 2010) or were read and give a more mixed picture (Lennon et al. 2012). (Martiny et al. 2013; Lennon et al. 2012; Placella et al. 2012; Philippot et al. 2010)
  Holds for: a secondary discussion statement.
  Evidence: asserted.
  Say instead: The evidence on environmental preferences does not converge on a single depth. The claim that environmental optima are conserved at deep ranks rests, among full-text sources, on an engineered study of 23 bacterial isolates for moisture and on an asserted secondary statement; natural evidence for environmental optima is thin, and the two coarse-rank optimum results are engineered. (Martiny et al. 2013; Lennon et al. 2012; Morrissey and Franklin 2015)
  Holds for: the sources the review read for Part A1.
- Do not write: "Perturbation responses are conserved at about genus level."
  Why: The equation of tau_D 0.016 to 0.020 with roughly genus is attributed to the authors, but the review's own Section 1 says a 16S depth cannot be converted into a rank.
  Say instead: Responses to N addition across 13 field experiments on five continents were conserved at tau_D 0.016 to 0.020 per location (0.017 merged). (Isobe et al. 2019)
  Holds for: engineered perturbation responses (N addition); taxonomy RDP on SILVA 128; the authors equate this to roughly genus, but the review's own Section 1 says a 16S depth cannot be converted into a rank (the critic: inconsistent use); the critic verified the figures.
  Say instead: Perturbation responses are a different quantity from environmental optima; in 16S terms they cluster at tau_D 0.016 to 0.020 per location for N addition (0.017 merged) and at 0.016 to 0.024 for warming, drought, elevated CO2, P addition and liming, which the review calls roughly genus depth. (Isobe et al. 2019; Isobe et al. 2020; Amend et al. 2016)
  Holds for: engineered N-addition and global-change experiments; the review also cites a litter study, which gives no tau_D (only positive responses were significantly conserved); the critic: equating these depths with roughly genus is inconsistent with the review's own statement that a 16S depth cannot be converted into a rank.
- Do not write: "Coarse taxonomic groups contain opposing finer responses."
  Why: It is phrased as a general bound but rests on one N-addition study plus a time series, and that N-addition study also reports consistent coarse-rank responses (phylum Actinobacteria positive; classes Betaproteobacteria and Deltaproteobacteria negative).
  Say instead: Coarse groups can hide opposing finer ones in the N-addition responses: Gammaproteobacteria as a class had no consistent response while one genus within it responded positively, and an order and a family within it responded in opposite directions. (Isobe et al. 2019)
  Holds for: engineered N-addition experiments (one study); the critic verified the Gammaproteobacteria example.
  Say instead: The same N-addition study also reports consistent phylum- and class-level responses: phylum Actinobacteria positive; classes Betaproteobacteria and Deltaproteobacteria negative. (Isobe et al. 2019)
  Holds for: engineered N-addition experiments; the review leaves this out, citing only the 'coarse hides fine' example.
- Do not write: "Genome incompleteness pushes detected function down."
  Why: It is phrased generally, but each quantitative element is single source (modules, core genes, reference bias), and none measures the effect on conservation depth.
  Say instead: Incompleteness pushed detected function down in single-source tests of modules, core genes and reference bias, with the size of the effect depending on module and phylum; the evidence is indirect but consistent in direction, and none of it measures the effect on conservation depth. (Eisenhofer et al. 2023; Li and Yin 2022; Albright and Louca 2023)
  Holds for: KEGG modules (modelled on subsampled complete genomes), core gene families (modelled) and reference genomes, one source each.
  Evidence: a single source.
- Do not write: "Genome incompleteness makes consenTRAIT depth estimates shallower."
  Why: That consensus-threshold methods would push depth estimates shallower under incompleteness is the reviewer's untested reading, echoed in Section 5 as a bound.
  Say instead: Consensus-threshold methods such as consenTRAIT (90% sharing) are exposed to false absences, which would fragment clades and push depth estimates shallower. (the reviewer's synthesis)
  Holds for: untested by any source; the critic: appropriately labelled as untested, but then echoed in Section 5 as a bound.
  Evidence: the reviewer's reading.
  Say instead: No study found tests directly how genome incompleteness biases tau_D or signal statistics; its effect on depth estimates themselves has not been measured in any source read. (a search result)
  Holds for: the review's search, whose routes are listed in the note's provenance (including WebSearch on genome completeness with functional inference); the critic: the routes behind this not-found are not named in the body.
  Evidence: a search result.
  Searched, not found (note: "(3) any direct test of how genome incompleteness biases tau_d or signal statistics").
- Do not write: "Rank-wise partitioning of genomic traits is non-monotonic."
  Why: The Royalty and Steen rank partition is a single source, correctly flagged in the body, but it carries weight in the A2 verdict without that flag.
  Say instead: With GTDB ranks, ranks together explained 41.4% of the variance in 25 COG categories normalised for genome size: domain 3.2%, phylum 14.6%, class 4.1%, order 9.2%, family 4.8%, genus 5.5%; the contribution is non-monotonic across ranks. (Royalty and Steen 2019)
  Holds for: 13,735 lineages, GTDB ranks; the critic: correctly flagged single source in the body, but it carries weight in the A2 verdict without that flag.
  Evidence: a single source.
- Do not write: "97% OTUs explained more composition variance than ASVs."
  Why: Bay et al. compare the high-resolution set against filtered ones (clustered and/or rare-taxon-filtered data) using incidence-based variation partitioning, so the paraphrase reduces a clustering-plus-filtering contrast to clustering alone.
  Say instead: Community turnover was stronger at ASV resolution (an 82% drop in similarity over 160 km, against 50 to 60% for clustered or filtered data), but "less variation in community composition could be explained and partitioned for the high-resolution data set", and the rank order of predictors changed. The comparison is of the high-resolution set against clustered and/or rare-taxon-filtered data, by incidence-based variation partitioning. (Bay et al. 2020)
  Holds for: soils in the Negev; no ranks, only sequence-identity thresholds; one of the uncontrolled rank-wise studies.
- Do not write: "The rise in explained variance from otu97 to otu94 is replicated across studies."
  Why: The rise rests on Lu 2016 alone; the other study cited for it compares ASVs against clustered and/or filtered data, a different step.
  Say instead: The rise in explained variance from otu97 to otu94 rests on Lu et al. 2016 alone: Bay et al. compare ASVs against clustered and/or filtered data, a different step, although its direction matches. (Lu et al. 2016; Bay et al. 2020)
  Holds for: the otu97-to-otu94 and genus rise in soils.
  Evidence: a single source.
- Do not write: "Rank-wise structuring of composition corresponds to the depth at which perturbation responses are conserved, at about genus."
  Why: It links a natural-system composition result to engineered perturbation-response depths, which breaks the natural/engineered separation, and presents a correspondence the sources do not test.
  Say instead: The rise in explained variance from otu97 to about otu94 and genus matches where perturbation responses cluster (tau_D about 0.017 to 0.02), and the fall at phylum in soils and the class-level incoherence in a time series match the weak within-phylum pH signal and the opposing responses inside coarse groups. (Ramoneda et al. 2023; Isobe et al. 2019; Isobe et al. 2020; Lu et al. 2016; Auladell et al. 2022)
  Holds for: the critic: it links a natural-system composition result to engineered perturbation-response depths, breaking the natural/engineered separation, and presents a correspondence the sources do not test.
  Evidence: the reviewer's reading.

## Gaps

What the research did not establish.

- A large-scale study of community conservatism across microbial phyla and environments, from the von Mering group, which may directly address rank-wise environmental coherence with null partitions (Malfertheiner, Tackmann, Rodrigues, von Mering, bioRxiv; appears published January 2026, open access). (Malfertheiner et al. 2024)
  The research does not say whether this was searched for.
- Archaeal results: every depth and rank-wise result is bacterial, although the brief says any prokaryote (for example Thaumarchaeota/Nitrososphaeria pH and ammonia-oxidiser niche depth; halophilic and thermophilic archaea).
  The research does not say whether this was searched for.
- Marine cyanobacterial ecotypes, where light and temperature optima are measured on isolates and mapped onto a phylogeny against field distributions: the classic natural-system case for depth of environmental preference (Prochlorococcus and Synechococcus; Johnson et al. 2006; Martiny, Tai and others 2009). (Johnson and others 2006; Martiny et al. 2009)
  The research does not say whether this was searched for.
- Trait databases compiling isolate growth optima (pH, temperature, salinity, oxygen) with phylogenetic signal statistics, other than the preprint Barnum and the non-re-opened Goberna (Madin et al. 2020; BacDive-based signal analyses; Sauer and Wang 2019). (Madin and others 2020; Sauer and Wang 2019)
  The research does not say whether this was searched for.
- Habitat-preference coherence across 16S clusters from global sequence-habitat compilations, other than Schmidt 2014 (Chaffron et al. 2010; Tamames et al. 2016; Auguet, Barberan and Casamayor 2010, archaeal habitat preference). (Chaffron and others 2010; Tamames and others 2016; Auguet et al. 2010)
  The research does not say whether this was searched for.
- Soil moisture optimum in natural systems: only an engineered isolate study was read; natural rewetting and drought field studies were not obtained (Placella, Evans and Wallenstein), and no alternative routes are named, such as author repositories or eScholarship for UC-affiliated authors. (Placella et al. 2012; Evans and Wallenstein 2014)
  The research does not say whether this was searched for.
- A direct test of how genome incompleteness biases tau_D or phylogenetic signal, for example in MAG-based consenTRAIT or signal analyses (GEM catalogue, GTDB MAG-inclusive trees).
  Searched, not found (note: "(3) any direct test of how genome incompleteness biases tau_d or signal statistics").
- Rank-wise community-environment results under GTDB against SILVA or Greengenes for the same analysis (db-RDA or PERMANOVA re-run under alternative taxonomies): only the metabolic-coherence comparison of Parras-Moltó is given.
  The research does not say whether this was searched for.
- Martiny et al. 2013's trait values and overall tau_D range: not re-checked at synthesis or by the critic, with an unresolved transcription discrepancy between the two search agents. (Martiny et al. 2013)
  The research does not say whether this was searched for.
- Whether Lu et al. 2016's null holds group number and member count fixed, and its soil class peak, 50% otu97-to-otu94 rise and per-dataset seawater shapes: the critic could confirm only the abstract. (Lu et al. 2016)
  The research does not say whether this was searched for.
- Goberna and Verdu 2016's figures and internal-inconsistency claim, read in full by one agent only and not re-opened. (Goberna and Verdu 2016)
  The research does not say whether this was searched for.
- Numeric tau_D values for the canonical-axis signal in Chakraverti-Wuerthwein et al. 2026, which appear only in figures. (Chakraverti-Wuerthwein et al. 2026)
  The research does not say whether this was searched for.
- A rank-wise composition-environment study other than Lu 2016 that controls group number and size.
  Searched, not found (note: "(2) any rank-wise composition-environment study, other than lu 2016, that controls group number and size").
- A consenTRAIT tau_D for pH, temperature or moisture optima.
  Searched, not found (note: "(1) any consentrait tau_d for ph, temperature or moisture optima").
- Publication status of the preprints Barnum 2024 and Mayjonade 2024. (Barnum et al. 2024; Mayjonade et al. 2024)
  The research does not say whether this was searched for.
- A rank-wise study that controls abundance evenness among groups as well as group number and size.
  The research does not say whether this was searched for.

## References

- Albright, Sage; Louca, Stilianos (2023). Trait biases in microbial reference genomes. Scientific Data 10(1): 84. https://doi.org/10.1038/s41597-023-01994-7
- Amend, Anthony S.; Martiny, Adam C.; Allison, Steven D.; Berlemont, Renaud; Goulden, Michael L.; Lu, Ying; Treseder, Kathleen K.; Weihe, Claudia; Martiny, Jennifer B. H. (2016). Microbial response to simulated global change is phylogenetically conserved and linked with functional potential. The ISME Journal 10(1): 109--118. https://doi.org/10.1038/ismej.2015.96
- Auguet; Barberan; Casamayor (2010). The ISME Journal.
- Auladell, Adria; Barberan, Albert; Logares, Ramiro; Garces, Esther; Gasol, Josep M.; Ferrera, Isabel (2022). Seasonal niche differentiation among closely related marine bacteria. The ISME Journal 16(1): 178--189. https://doi.org/10.1038/s41396-021-01053-2
- Barnum, Tyler P.; Crits-Christoph, Alexander; Molla, Michael; Carini, Paul; Lee, Henry H.; Ostrov, Nili (2024). Predicting microbial growth conditions from amino acid composition. bioRxiv 2024.03.22.586313. https://doi.org/10.1101/2024.03.22.586313
- Bay, Sean K.; McGeoch, Melodie A.; Gillor, Osnat; Wieler, Nimrod; Palmer, David J.; Baker, David J.; Chown, Steven L.; Greening, Chris (2020). Soil bacterial communities exhibit strong biogeographic patterns at fine taxonomic resolution. mSystems 5(4): e00540-20. https://doi.org/10.1128/mSystems.00540-20
- Berlemont, Renaud; Martiny, Adam C. (2013). Phylogenetic distribution of potential cellulases in bacteria. Applied and Environmental Microbiology 79(5): 1545--1554. https://doi.org/10.1128/AEM.03305-12
- Blomberg, Simon P.; Garland, Theodore; Ives, Anthony R. (2003). Testing for phylogenetic signal in comparative data: behavioral traits are more labile. Evolution 57(4): 717--745. https://doi.org/10.1111/j.0014-3820.2003.tb00285.x
- Chaffron; others (2010). Genome Research.
- Chakraverti-Wuerthwein, Milena S.; Domenig, Alissa; Kuehn, Seppe (2026). Phylogenetic coherence in microbiome composition across environmental gradients. bioRxiv 2026.06.07.730742. https://doi.org/10.64898/2026.06.07.730742
- Chase, Alexander B.; Karaoz, Ulas; Brodie, Eoin L.; Gomez-Lunar, Zulema; Martiny, Adam C.; Martiny, Jennifer B. H. (2017). Microdiversity of an abundant terrestrial bacterium encompasses extensive variation in ecologically relevant traits. mBio 8(6): e01809-17. https://doi.org/10.1128/mBio.01809-17
- Eisenhofer, Raphael; Odriozola, Inaki; Alberdi, Antton (2023). Impact of microbial genome completeness on metagenomic functional inference. ISME Communications 3(1): 12. https://doi.org/10.1038/s43705-023-00221-z
- Evans, Sarah E.; Wallenstein, Matthew D. (2014). Climate change alters ecological strategies of soil bacteria. Ecology Letters 17(2): 155--164. https://doi.org/10.1111/ele.12206
- Farrell, Anne A.; Nesb, Camilla L.; Zhaxybayeva, Olga (2025). Bacterial growth temperature as a horizontally acquired polygenic trait. Genome Biology and Evolution 17(1): evae277. https://doi.org/10.1093/gbe/evae277
- Freckleton, R. P.; Harvey, P. H.; Pagel, M. (2002). Phylogenetic Analysis and Comparative Data: A Test and Review of Evidence. The American Naturalist 160(6): 712--726. https://doi.org/10.1086/343873
- Goberna, Marta; Verdu, Miguel (2016). Predicting microbial traits with phylogenies. The ISME Journal 10(4): 959--967. https://doi.org/10.1038/ismej.2015.171
- Hoffert, Michael; Gorman, Evan; Lladser, Manuel E.; Fierer, Noah (2026). Constructing a "periodic table" of bacteria to map diversity in trait space. The ISME Journal 20(1): wraf289. https://doi.org/10.1093/ismejo/wraf289
- Isobe, Kazuo; Allison, Steven D.; Khalili, Banafshe; Martiny, Adam C.; Martiny, Jennifer B. H. (2019). Phylogenetic conservation of bacterial responses to soil nitrogen addition across continents. Nature Communications 10(1): 2499. https://doi.org/10.1038/s41467-019-10390-y
- Isobe, Kazuo; Bouskill, Nicholas J.; Brodie, Eoin L.; Sudderth, Erika A.; Martiny, Jennifer B. H. (2020). Phylogenetic conservation of soil bacterial responses to simulated global changes. Philosophical Transactions of the Royal Society B 375(1798): 20190242. https://doi.org/10.1098/rstb.2019.0242
- Izabel-Shen, Dandan; Hoger, Anna-Lena; Jurgens, Klaus (2021). Abundance-occupancy relationships along taxonomic ranks reveal a consistency of niche differentiation in marine bacterioplankton with distinct lifestyles. Frontiers in Microbiology 12: 690712. https://doi.org/10.3389/fmicb.2021.690712
- Johnson; others (2006). Science.
- Lennon, Jay T.; Aanderud, Zachary T.; Lehmkuhl, B. K.; Schoolmaster, Donald R. (2012). Mapping the niche space of soil microorganisms using taxonomy and traits. Ecology 93(8): 1867--1879. https://doi.org/10.1890/11-1745.1
- Li, Tang; Yin, Yanbin (2022). Critical assessment of pan-genomic analysis of metagenome-assembled genomes. Briefings in Bioinformatics 23(6): bbac413. https://doi.org/10.1093/bib/bbac413
- Lopez-Mondejar, Ruben; Tlaskal, Vojtech; da Rocha, Ulisses Nunes; Baldrian, Petr (2022). Global distribution of carbohydrate utilization potential in the prokaryotic tree of life. mSystems 7(6): e00829-22. https://doi.org/10.1128/msystems.00829-22
- Lu, Hsiao-Pei; Yeh, Yi-Chun; Sastri, Akash R.; Shiah, Fuh-Kwo; Gong, Gwo-Ching; Hsieh, Chih-hao (2016). Evaluating community-environment relationships along fine to broad taxonomic resolutions reveals evolutionary forces underlying community assembly. The ISME Journal 10(12): 2867--2878. https://doi.org/10.1038/ismej.2016.78
- Madin; others (2020). Scientific Data.
- Malfertheiner; Tackmann; Rodrigues; von Mering (2024). Community conservatism is widespread throughout microbial phyla and environments. bioRxiv. https://doi.org/10.1101/2024.11.06.622256
- Martiny, Adam C.; Treseder, Kathleen; Pusch, Gordon (2013). Phylogenetic conservatism of functional traits in microorganisms. The ISME Journal 7(4): 830--838. https://doi.org/10.1038/ismej.2012.160
- Martiny; Tai; others (2009). PNAS.
- Mayjonade, Baptiste; Zamar, Remy; Carrere, Sebastien; Roux, Fabrice (2024). The relative effects of abiotic and biotic factors in explaining the structure of soil bacterial communities at diverse taxonomic levels. bioRxiv 2024.10.29.620845. https://doi.org/10.1101/2024.10.29.620845
- Morrissey, Ember M.; Franklin, Rima B. (2015). Evolutionary history influences the salinity preference of bacterial taxa in wetland soils. Frontiers in Microbiology 6: 1013. https://doi.org/10.3389/fmicb.2015.01013
- Morrissey, Ember M.; Mau, Rebecca L.; Schwartz, Egbert; Caporaso, J. Gregory; Dijkstra, Paul; van Gestel, Natasja; Koch, Benjamin J.; Liu, Cindy M.; Hayer, Michaela; McHugh, Theresa A.; Marks, Jane C.; Price, Lance B.; Hungate, Bruce A. (2016). Phylogenetic organization of bacterial activity. The ISME Journal 10(9): 2336--2340. https://doi.org/10.1038/ismej.2016.28
- Parras-Molto, Marcos; Aguirre de Carcer, Daniel (2021). Assessment of phylo-functional coherence along the bacterial phylogeny and taxonomy. Scientific Reports 11(1): 8299. https://doi.org/10.1038/s41598-021-87909-1
- Philippot, Laurent; Andersson, Siv G. E.; Battin, Tom J.; Prosser, James I.; Schimel, Joshua P.; Whitman, William B.; Hallin, Sara (2010). The ecological coherence of high bacterial taxonomic ranks. Nature Reviews Microbiology 8(7): 523--529. https://doi.org/10.1038/nrmicro2367
- Placella, Sarah A.; Brodie, Eoin L.; Firestone, Mary K. (2012). Rainfall-induced carbon dioxide pulses result from sequential resuscitation of phylogenetically clustered microbial groups. Proceedings of the National Academy of Sciences 109(27): 10931--10936. https://doi.org/10.1073/pnas.1204306109
- Quiroga, Maria V.; Valverde, Angel; Mataloni, Gabriela; Casa, Valeria; Stegen, James C.; Cowan, Don (2022). The ecological assembly of bacterial communities in Antarctic wetlands varies across levels of phylogenetic resolution. Environmental Microbiology 24(8): 3486--3499. https://doi.org/10.1111/1462-2920.15912
- Ramoneda, Josep; Stallard-Olivera, Elias; Hoffert, Michael; Winfrey, Claire C.; Stadler, Masumi; Nino-Garcia, Juan Pablo; Fierer, Noah (2023). Building a genome-based understanding of bacterial pH preferences. Science Advances 9(17): eadf8998. https://doi.org/10.1126/sciadv.adf8998
- Royalty, Taylor M.; Steen, Andrew D. (2019). Quantitatively partitioning microbial genomic traits among taxonomic ranks across the microbial tree of life. mSphere 4(4): e00446-19. https://doi.org/10.1128/mSphere.00446-19
- Sauer; Wang (2019).
- Schmidt, Thomas S. B.; Matias Rodrigues, Joao F.; von Mering, Christian (2014). Ecological consistency of SSU rRNA-based operational taxonomic units at a global scale. PLoS Computational Biology 10(4): e1003594. https://doi.org/10.1371/journal.pcbi.1003594
- Sun, Zhong-Zhi; Ji, Bo-Wen; Zheng, Ning; Wang, Meng; Cao, Ye; Wan, Lu; Li, Yi-Song; Rong, Jin-Cheng; He, Hai-Lun; Chen, Xiu-Lan; Zhang, Yu-Zhong; Xie, Bin-Bin (2021). Phylogenetic distribution of polysaccharide-degrading enzymes in marine bacteria. Frontiers in Microbiology 12: 658620. https://doi.org/10.3389/fmicb.2021.658620
- Tamames; others (2016).
- Zimmerman, Amy E.; Martiny, Adam C.; Allison, Steven D. (2013). Microdiversity of extracellular enzyme genes among sequenced prokaryotic genomes. The ISME Journal 7(6): 1187--1199. https://doi.org/10.1038/ismej.2012.176
