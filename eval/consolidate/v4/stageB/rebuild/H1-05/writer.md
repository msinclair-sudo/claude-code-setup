# Functional and taxonomic turnover in soil microbial communities: writer's view

> [!abstract] About this view
> What the research found, for writing from. Each claim gives who found it, the setting it holds for, the kind of evidence, its standing where the research stated one, and for an absence whether it was searched for. A claim with no standing given has none stated in the research; "limited by access" means a source was not read in full, which is not the same as weak evidence. Sources are listed at the end. The view is generated from the knowledge note `Functional and taxonomic turnover in soil microbial communities.md`, where every claim is checked against the research.

## What the research found, by question

### H1-05

**D1. How do turnover in functional profiles and turnover in taxonomic composition compare across soils, in either direction, and does the comparison change with the size of the environmental contrast, in either direction?**

*Answer, as corrected by a second reader.* **D1, soil, DNA-measured functional profiles**

Positive covariation of functional and taxonomic dissimilarity is shown in three soil datasets at strong contrasts (Fierer et al. 2012) (Leff et al. 2015) (Chen et al. 2022) (numbers confirmed against full text: Mantel r 0.76 and 0.82 (Fierer et al. 2012); rho 0.87 (Leff et al. 2015); r2 0.2831 over 356,090 pairs from 845 MG-RAST metagenomes (Chen et al. 2022)). These datasets are not independent in lineage: (Fierer et al. 2012) and (Leff et al. 2015) come from one group, and (Chen et al. 2022) pools MG-RAST submissions that may include (Fierer et al. 2012). Covariation says nothing about which turnover is larger. The one large soil magnitude comparison (Chen et al. 2022) finds functional similarity higher than taxonomic, and it does so at a strong (global) contrast. So the review's statement that 'function lower' holds under a strong contrast only in marine (van der Loos et al. 2025), 'unlike the soil cross-biome result (Fierer et al. 2012)', is wrong: (Fierer et al. 2012) did not compare magnitudes, and (Chen et al. 2022) is a strong-contrast soil case of function lower. Single-site 'function lower' results (Igwe and Afkhami 2026) (Pan et al. 2014) (Yang et al. 2021) (Souza et al. 2015) (Sauma-Sanchez et al. 2024) mostly set a significant test against a non-significant one. The reverse ordering rests on two GeoChip studies from one group (Gao et al. 2021) (Ma et al. 2017) (one abstract only) plus a reviewer's reading of (Shen et al. 2016). Platform (GeoChip vs shotgun), group and contrast size are confounded, so no dependence on contrast size can be read off. (Xu et al. 2022) tests within-treatment dispersion under two magnitudes of precipitation change. Neither taxonomy nor function shifted directionally there, and the study does not compare the two turnovers' magnitudes, so it bears only indirectly on D1. Evidence on non-soil systems: (Graco-Roza et al. 2022) includes diatoms and fungi but no bacteria, so it is not 'non-microbial'.

**D2. How does the comparison depend on the functional unit, the annotation scheme and the dissimilarity measure, including whether the ordering between the two changes with any of them?**

*Answer, as corrected by a second reader.* **D2, soil**

Single-study evidence only. In (Chen et al. 2022), functional similarity exceeded taxonomic similarity at SEED levels 1 and 2 against all five taxonomic ranks. The ordering therefore did not reverse at any combination tested. That the 'gap widens' with aggregation is the reviewer's inference, not a result the authors state. (Chen et al. 2022) explicitly chose SEED over KO, COG and NOG, so finer units were not tested. (Xu et al. 2022) reports that Mash all-read and assembled-gene within-treatment dissimilarities patterned like annotated-read dissimilarity. (Gu et al. 2025) shows that the choice of statistic (distance-decay slope vs dispersion) changed the functional conclusion. The taxonomic side is also measured differently across studies (16S amplicon in (Fierer et al. 2012) (Leff et al. 2015) (Gao et al. 2021); read-based RefSeq in (Chen et al. 2022); MAG in (van der Loos et al. 2025)), and this is not kept apart. No soil study was found that compares dissimilarity measures or transforms for the ordering. Outside soil, (Galand et al. 2018) (marine, single study) shows coupling strength depends on the annotation scheme.

**D3. What have null models of any kind (for example based on aggregation, abundance structure, phylogeny, traits or environmental filtering) and other tests concluded about any difference between functional and taxonomic turnover, whatever they concluded? Report soil results and results from other habitats separately.**

*Answer, as corrected by a second reader.* **D3, soil**

No field-soil null model testing the functional-taxonomic difference was found by the review's routes. Ho and Huang's label-shuffling null (Ho and Huang 2025) (Ho and Huang 2024) is the only direct microbial test. It operates on functions inferred through a gene-content matrix (FAPROTAX-style groups or genome annotations), not on shotgun-measured profiles. It tests variability around a mean community within one environment, not turnover across environments. So its soil-derived in vitro result (glucose medium, Goldford data) is indirect for D3 soil and belongs to the marker-inferred case. Its aggregation argument is modelled and single source. The published body text was not read, and the preprint was read only as a fetch summary. (Zhang et al. 2025) applies separate assembly nulls to taxonomy and to gene sets in wetland soil and sediment. It does not test the difference itself. (Graco-Roza et al. 2022) (148 datasets including diatoms and fungi, no bacteria) finds most functional decay consistent with a name-randomization null (13 of 148 deviated along space: 3 faster, 10 slower). (Swenson et al. 2011) finds faster-than-null functional turnover in trees.

## Concepts

In an order where each concept comes after the ones it builds on; the order means nothing more.

### what turnover and "function" mean in these comparisons

- The distance-based test of homogeneity of multivariate dispersions (PERMDISP) compares the spread of groups of samples, measured with any dissimilarity measure, as distances to the group centroid or spatial median; it is a multivariate extension of Levene's test. (Anderson 2006)
  Background, not from the research.
- Turnover here means between-sample dissimilarity. "Function" in the soil literature means several different things: shotgun reads annotated to SEED, KEGG or eggNOG; GeoChip probe arrays; gene-family counts from assemblies or MAGs; profiles inferred from 16S (PICRUSt, FAPROTAX); and, in two cases, measured enzyme activity or protein. (the reviewer's definitions)
  Holds for: the soil literature reviewed.

### covariation of functional and taxonomic dissimilarity

Builds on: what turnover and "function" mean in these comparisons.

- Across 16 soils from cold desert, hot desert, forest, grassland and tundra, Bray-Curtis dissimilarity of MG-RAST/SEED gene profiles correlated with 16S Bray-Curtis (Mantel r = 0.76) and with unweighted UniFrac (r = 0.82); only 13 to 23% of reads were annotatable, and desert and non-desert samples separated almost completely (ANOSIM R about 0.97 to 0.98). (Fierer et al. 2012)
  Holds for: 16 soils at a strong cross-biome contrast; figures confirmed against full text by the critic.
  Evidence: measured.
- On the reviewer's reading, not the authors', a single dominant desert/non-desert split drives both matrices in the 16-soil study, so the correlation may say more about that split than about fine-scale coupling; the critic adds that the authors made a parallel caveat for alpha diversity (the correlations were not significant without the cold-desert soils). (Fierer et al. 2012)
  Holds for: 16 soils, dominated by a desert/non-desert split.
  Evidence: the reviewer's reading.
- The authors of Fierer 2012 conclude that functional redundancy 'is not so pervasive as to obscure' the taxonomy-function relationship. (Fierer et al. 2012)
  Holds for: Fierer 2012.
- Across six NutNet grassland sites, functional-gene and bacterial dissimilarity correlated with rho = 0.87, mostly between sites; within-site N and P additions shifted both. (Leff et al. 2015)
  Holds for: six NutNet grassland sites; figures confirmed against full text by the critic.
  Evidence: measured.
- In 845 pooled public soil metagenomes (356,090 pairs), pairwise functional and taxonomic Bray-Curtis similarities correlated (r2 = 0.2831). (Chen et al. 2022)
  Holds for: 845 pooled MG-RAST soil metagenomes; rechecked against full text by the reviewer and the critic.
  Evidence: measured.
- At one site under coal-fire heating, metagenome and amplicon ordinations were concordant (Procrustes 0.802, m2 = 0.357), alongside stable functional similarity, so 'stable function' and 'covariation' coexist in one dataset. (Barnett and Shade 2025)
  Holds for: one site; a preprint read via a fetch summary.
- Across soils, functional and taxonomic dissimilarity are usually positively correlated; the clearest cases come from strong cross-biome or between-site contrasts (Mantel r 0.76 to 0.82 across 16 soils; Spearman rho 0.87 across 6 NutNet sites; r2 0.28 across 845 pooled metagenomes), and strong contrasts give covariation. (Fierer et al. 2012; Leff et al. 2015; Chen et al. 2022)
  Holds for: three soil datasets at strong contrasts, all using Bray-Curtis on annotated profiles and correlation-type tests; none used a null model; the critic: not independent in lineage, as two come from one group and the third pools MG-RAST submissions that may include the first.
  Evidence: measured; rated "Moderate for covariation at strong contrasts" by the research; a second reader disputes this: these datasets are not independent in lineage.

### which turnover is larger, functional or taxonomic

Builds on: covariation of functional and taxonomic dissimilarity.

- Covariation and "function less variable" are compatible: covariation says nothing about which turnover is larger, because a correlation between dissimilarity matrices says nothing about their relative magnitudes; two soil datasets report both. (Chen et al. 2022; Barnett and Shade 2025)
  Holds for: the 845 pooled soil metagenomes and the coal-fire site.
- In the global pooled dataset, functional Bray-Curtis similarity ranged 44 to 99% and taxonomic 9 to 100% (paired t = 67.5); climate plus soil explained 16.3% of taxonomic and 13.5% of functional variation (DistLM). The authors call this strong evidence for functional redundancy. It is the one large soil magnitude comparison, and it finds functional similarity higher than taxonomic at a strong (global) contrast; removing it would leave the 'function lower' ordering resting on small single-site studies and significance contrasts. (Chen et al. 2022)
  Holds for: 845 pooled public soil metagenomes; the profiles pool assembled and unassembled MG-RAST submissions from many studies; SEED level 3 (1,135 functions) compared with RefSeq genus (1,113 taxa); nothing tests whether a lower functional dissimilarity is expected from aggregation alone; figures checked against full text by the reviewer and the critic.
  Evidence: a single source.
- Between serpentine and non-serpentine site pairs, bacterial composition differed (PERMANOVA R2 = 0.061, P = 0.004) while eggNOG functional composition did not (R2 = 0.027, P = 0.391); the authors conclude redundancy, and note that specialized functions such as siderophore biosynthesis did differ. (Igwe and Afkhami 2026)
  Holds for: serpentine and non-serpentine soil pairs; residual df 19 against 16; figures rechecked by the reviewer and the critic.
  Evidence: measured.
- On the reviewer's reading, the serpentine result is a significant test set against a non-significant one, on datasets of different size after QC (the functional dataset is smaller): site pairs explained about 56% of variation in both functional (non-significant, F(19,16)) and bacterial (significant) composition, which suggests limited power on the functional side rather than an absence of structure. (Igwe and Afkhami 2026)
  Holds for: serpentine and non-serpentine soil pairs.
  Evidence: the reviewer's reading.
- Along a latitudinal forest gradient in China, bacterial Bray-Curtis showed strong distance decay, while GeoChip function (summarized as DCA axes, not pairwise dissimilarity) was "highly convergent"; the two turnovers are not on a common basis. (Zhang et al. 2016)
  Holds for: natural broadleaf forest along a latitudinal gradient in China; GeoChip function against bacterial Bray-Curtis.
- Under coal-fire disturbance, OTU similarity to reference rose as soils cooled, while KO similarity stayed high throughout (stable KO similarity during fire-disturbance recovery); MAG-based redundancy rose with disturbance, which the authors attribute to lower diversity and smaller genomes. (Barnett and Shade 2025)
  Holds for: one coal-fire site; a preprint with no published version found, read via a fetch summary.
- No fertilizer effect on functional profiles after 54 years, despite taxonomic shifts. (Pan et al. 2014)
  Holds for: long-term N, P, K and NPK fertilization of grassland soil, 54 years; abstract only.
- Stable functional potential across a 1 to 30 C peat incubation while taxonomy changed. (Yang et al. 2021)
  Holds for: peat incubation; abstract only.
- Taxonomic differences "far greater" than SEED functional differences under tillage and rotation, with the two measured in different papers. (Souza et al. 2015)
  Holds for: a soil under different tillage and crop-management (rotation) regimes; abstract only; a cross-paper comparison.
- Similar functional capacities in arid and hyperarid saline drylands despite structural differences. (Sauma-Sanchez et al. 2024)
  Holds for: arid and hyperarid saline drylands; only the abstract and methods closely read, so abstract-level for its result claim.
- Under high Hg, little change in C and N genes but a significant shift in predicted-gene beta diversity. (Frey et al. 2022)
  Holds for: long-term mercury contamination of soils (high Hg); abstract only.
- After aromatic pollution in a microcosm, taxonomic diversity fell and gene-pool diversity rose (alpha diversity, not turnover). (Kato et al. 2015)
  Holds for: a microcosm; alpha, not turnover; abstract only.
- Fungal endemism with convergent enzyme activity across North America: a non-DNA case, indirect for DNA profiles. (Talbot et al. 2014)
  Holds for: soil fungi across North America; measured enzyme activity, not DNA; abstract only.
- With marker-inferred function, ZnO dose separated taxa but not PICRUSt-type predicted functions. (Dinesh et al. 2023)
  Holds for: soil polluted with nano ZnO, by dose; function inferred from the same 16S data, so not independent of taxonomy; abstract only.
  Evidence: derived.
- Along an alpine gradient, PICRUSt2 function was redundant and tracked phylogenetic more than taxonomic dissimilarity. (Li et al. 2024)
  Holds for: an alpine altitudinal gradient; function inferred from the same 16S data, so not independent of taxonomy.
  Evidence: derived.
- After 14 years of moderate warming (0.8 to 2.0 C), 16S composition did not differ while GeoChip functional-gene composition did (Adonis, ANOSIM, MRPP, P < 0.05), with n = 4 per treatment; the authors conclude that functional potential is more sensitive than taxonomy. Plant and abiotic variables were unchanged, so the contrast was weak. (Gao et al. 2021)
  Holds for: one long-term warming site in a Mediterranean-type grassland, n = 4 per treatment, GeoChip against 16S; n and the three tests checked by the critic.
  Evidence: measured.
- Under aeolian erosion and deposition, soil nutrients correlated with functional but not taxonomic structure (Mantel). (Ma et al. 2017)
  Holds for: field simulation of aeolian soil erosion and deposition; GeoChip; abstract only.
- Along the Changbai elevation gradient, functional-gene distance decay (r = 0.708) was stronger than bacterial (r = 0.409) on the reviewer's reading; the authors describe the patterns as similar, with different drivers (pH for taxa, DOC for genes), and the two r values come from different platforms (16S against GeoChip) and are not on a common scale. (Shen et al. 2016)
  Holds for: Changbai elevation gradient.
  Evidence: the reviewer's reading.
- Lower functional than taxonomic turnover is the most common reported ordering in soil but rests on weak comparisons: none of the 'function lower' soil studies compares the two turnovers on a common test with a null, and the single-site 'function lower' results mostly set a significant test against a non-significant one. (Chen et al. 2022; Igwe and Afkhami 2026; Pan et al. 2014; Yang et al. 2021; Souza et al. 2015; Sauma-Sanchez et al. 2024)
  Holds for: soil, DNA-measured functional profiles.
  Evidence: rated "Weak for the ordering" by the research.
- The reverse ordering (function responds where taxonomy does not) is reported under weak contrasts and rests on two GeoChip studies from one group (one abstract only) plus a reviewer's reading of a third; removing the warming study would leave only the abstract-only study and that reading. (Gao et al. 2021; Shen et al. 2016; Ma et al. 2017)
  Holds for: 14 years of moderate warming (n = 4 per treatment), erosion and deposition, and possibly an elevation gradient; platforms differ; the critic: the power-asymmetry critique made against the serpentine study is not applied to the warming study (n = 4, significant functional against non-significant taxonomic).
  Evidence: rated "Weak for the reverse ordering" by the research.
  A second reader found the search for contrary evidence one-sided.
- In soil, function more responsive (the 14-year warming and erosion studies) is in conflict with function less responsive (the serpentine, fertilizer, peat, tillage and dryland studies), all at single sites or weak or moderate contrasts. (Igwe and Afkhami 2026; Gao et al. 2021; Pan et al. 2014; Yang et al. 2021; Ma et al. 2017; Souza et al. 2015; Sauma-Sanchez et al. 2024)
  Holds for: single sites or weak or moderate contrasts.

### dependence of the comparison on the size of the environmental contrast

Builds on: covariation of functional and taxonomic dissimilarity, which turnover is larger, functional or taxonomic.

- No soil study was found that tests (or plots) how the functional-taxonomic gap scales with environmental distance; systematic comparisons across a graded range of environmental distances were not measured. (a search result)
  Holds for: soil.
  Evidence: a search result.
  Searched for and not found.
- In a single-site precipitation experiment, ±30% precipitation slightly decreased and ±60% strongly increased within-treatment dispersion (PERMDISP) of taxa, genes, proteins and enzyme activities alike; gene, protein and enzyme dissimilarities were Mantel-correlated with taxonomic dissimilarity, and neither taxonomy nor function showed a directional PERMANOVA shift. The authors conclude that "taxonomic stochasticity translated into functional stochasticity", not redundancy. (Xu et al. 2022)
  Holds for: one Eurasian steppe site under two magnitudes of precipitation change; within-treatment dispersion, not a comparison of the two turnovers' magnitudes, so indirect for the ordering question; the ±30% decrease in function confirmed by the critic.
  Evidence: measured.
- At weak single-site contrasts the ordering has gone both ways (function lower in the serpentine, 54-year fertilizer and tillage studies; function higher in the 14-year warming and erosion studies); cross-study comparison of contrast size is confounded by platform (GeoChip against shotgun), group, sample size and test, so no dependence on contrast size can be read off. (Igwe and Afkhami 2026; Gao et al. 2021; Pan et al. 2014; Ma et al. 2017; Souza et al. 2015)
  Holds for: soil; strong contrasts give covariation, weak single-site contrasts give both orderings.
- On the reviewer's synthesis, the reverse ordering appears only in GeoChip or single-site weak-contrast studies, so platform, contrast size and sample size are entangled; the magnitude comparison is the claim that most needs a null, and in soil it has none. (the reviewer's synthesis)
  Holds for: soil; mostly labelled as the reviewer's reading.
  Evidence: the reviewer's reading.
- Along a latitudinal gradient, taxonomic dissimilarity explains almost none of functional variation, while in the precipitation experiment function tracks taxonomy under both contrast sizes: the review lists these as in conflict. (Zhang et al. 2016; Xu et al. 2022)
  Holds for: a latitudinal forest gradient against one precipitation experiment.
  Evidence: contested.

### chronosequences and drivers, the nearest precedents

Builds on: what turnover and "function" mean in these comparisons.

- Over 143 years of grassland restoration, bacterial richness falls while SEED functional richness expands (alpha diversity; no paired turnover comparison). (Goodall et al. 2026)
  Holds for: grassland restoration chronosequence; alpha, not turnover; the preprint's "profound functional decoupling" was softened to "a decoupling" in the published version.
- Along Swedish succession, taxonomic diversity falls while C, N and P gene diversity rises, with PICRUSt2 used for the redundancy analyses (alpha diversity; no paired turnover comparison). (Sveen et al. 2025)
  Holds for: Swedish successional chronosequence; alpha, not turnover; the preprint's "causal link" was softened to "the link" in the published version.
- Global N-cycling pathway frequencies track habitat and soil C and N much better than the genera that encode them; this contrasts drivers, not turnovers, so it is indirect. (Nelson et al. 2016)
  Holds for: global soils; N-cycling traits.

### functional against taxonomic turnover outside soil

Builds on: covariation of functional and taxonomic dissimilarity, which turnover is larger, functional or taxonomic.

- On algal surfaces, taxonomic similarity was 15% against 70% COG similarity. (Burke et al. 2011)
  Holds for: algal surfaces; read via a fetch summary.
- In the Ulva microbiome across a 2000 km, 5 to 35 PSU salinity gradient, salinity explained R2 = 0.70 of taxonomic and 0.17 of KO-based functional variation (envfit), although 23 KEGG modules still shifted: function stays lower under a strong contrast. (van der Loos et al. 2025)
  Holds for: Ulva microbiome; one study, MAG-based taxonomy; envfit figures checked by the critic; the only strong-contrast case outside soil; soil has not tested function lower at a strong contrast with a common metric.
  Evidence: a single source.
- In a coastal Mediterranean time series, all-gene similarity tracked 16S similarity closely (R2 = 0.77); the authors reject strict redundancy. (Galand et al. 2018)
  Holds for: one marine time series; its full-text XML returned empty to the reviewer, so it rests on the agents' reading.
- In subsurface sediments, taxa CVs were about 10 times those of gene groups of similar mean abundance: taxa were about an order of magnitude more variable than gene groups at every KEGG level and EC, after abundance matching. (Soufi et al. 2024)
  Holds for: Oregon coastal subsurface sediments.
- In bromeliads, functional-group structure was stable while within-group taxonomy varied. (Louca et al. 2017)
  Holds for: bromeliad communities; abstract only.
- In the global ocean, with FAPROTAX (derived) functional groups, environment strongly shapes functional groups but weakly shapes within-group taxonomy. (Louca et al. 2016)
  Holds for: global ocean; FAPROTAX-derived function; abstract only.
  Evidence: deriv (note: "Global ocean, FAPROTAX (derived)").
- During vermicomposting, PICRUSt2 turnover was about 12 times slower than taxonomic turnover. (Aira et al. 2026)
  Holds for: vermicomposting; PICRUSt2-inferred function.
  Evidence: derived.
- Across 148 trait datasets, mean Mantel r along space was 0.254 taxonomic against 0.115 functional, with about 31 of 148 datasets reversed. (Graco-Roza et al. 2022)
  Holds for: 148 datasets including diatoms and fungi but no bacteria, so not 'non-microbial'; Mantel values checked by the critic; the critic's 13 deviating datasets are deviations from the randomization null, a different count from these reversals.
- In European fish, functional beta diversity is below taxonomic, driven by turnover. (Villeger et al. 2013)
  Holds for: European fish assemblages; abstract only.
- Yet in European fish, functional homogenization over time exceeded taxonomic homogenization six-fold. (Villeger et al. 2014)
  Holds for: European fish assemblages; abstract only.
- Outside soil, marine and host-associated studies mostly report lower functional turnover, including under a strong 2000 km salinity contrast and on algal surfaces, while a marine time series finds tight coupling; this mixes FAPROTAX-derived, abstract-only and single-time-series evidence, and the only strong-contrast case is the Ulva study across 2000 km of salinity. (Galand et al. 2018; Louca et al. 2016; Louca et al. 2017; Burke et al. 2011; van der Loos et al. 2025)
  Holds for: marine and host-associated systems, kept separate from soil.
- Non-bacterial communities (148 datasets including diatoms and fungi; European fish) show lower functional decay on average, but with many reversals. (Graco-Roza et al. 2022; Villeger et al. 2013; Villeger et al. 2014)
  Holds for: non-bacterial communities.

### dependence of the comparison on functional unit, annotation, platform and metric

Builds on: which turnover is larger, functional or taxonomic, what turnover and "function" mean in these comparisons.

- In the 845 pooled soil metagenomes, functional similarity exceeded taxonomic similarity at SEED levels 1 and 2 against all five taxonomic ranks, so the ordering did not reverse at any combination tested; the authors say coarser levels are more conserved, and state only that the ordering held at all levels. It is the only soil evidence on annotation level. (Chen et al. 2022)
  Holds for: 845 metagenomes (Chen 2022); SEED levels; rechecked by the reviewer.
  Evidence: a single source.
- Finer functional units (KO, gene clusters) were not tested in that study, which explicitly chose SEED over KO, COG and NOG, so whether the ordering can reverse at fine resolution is open. (Chen et al. 2022)
  Holds for: the global pooled soil metagenomes.
- In one soil experiment, dissimilarity from all reads including unannotated ones (Mash) and from assembled genes gave within-treatment patterns similar to annotated-read dissimilarity, so in that case the annotation did not change the result. (Xu et al. 2022)
  Holds for: one Eurasian steppe precipitation experiment; within-treatment dispersion; rechecked by the reviewer.
  Evidence: a single source.
- In a marine time series, the functional-taxonomic correlation fell from R2 0.77 (all genes) to 0.58 (KEGG) to 0.16 (FAPROTAX/PICRUSt, taxonomy-inferred functions): coupling strength depends on the annotation scheme. Removing this study removes the main direct evidence for that. (Galand et al. 2018)
  Holds for: marine, one time series.
  Evidence: a single source; rated "Moderate for the general point, outside soil, that annotation scheme changes the strength of coupling" by the research.
- The marine time series finds that restricting to annotated genes weakens the coupling (all-read coupling is strongest), while the soil precipitation experiment finds all-read and annotated dissimilarity behave alike; the two use different measures (regression of similarities against within-treatment dispersion) and habitats, so they do not directly contradict. (Xu et al. 2022; Galand et al. 2018)
  Holds for: marine water against one soil experiment.
- Unknown-function genes are prevalent in fine-textured, higher-pH soils and are often mobile-element associated, so the unannotated fraction can vary along soil gradients (with soil properties): indirect support for an annotation-bias critique, not a demonstration of its effect on turnover. (Holland-Moritz et al. 2021)
  Holds for: soils; a preprint, abstract only.
- On the same 27 paired steppe and cropland soils, the dispersion-based analysis found KEGG gene assemblages homogenized in cropland at local and regional scales while bacterial taxa were homogenized only locally, whereas an earlier distance-decay-slope analysis of the same data had found greater KEGG functional turnover in cropland: the choice of turnover statistic changed the functional conclusion. (Gu et al. 2025)
  Holds for: 27 paired steppe and cropland soils; the only soil case where metric choice reversed a conclusion; rechecked by the reviewer.
  Evidence: a single source.
- No soil study compared Bray-Curtis with Aitchison or Jaccard (dissimilarity measures or transforms) for the functional-taxonomic ordering. (a search result)
  Holds for: soil; searches by both agents (soil agent queries); the critic: compositional comparisons reported as not found without naming the routes.
  Evidence: a search result.
  Searched, not found (note: "no soil study compared bray-curtis with aitchison or jaccard for the functional-taxonomic ordering (searches by both agents)").
- For ectomycorrhizal fungi, turnover appeared at the level of gene sequence variants but not gene-family abundance. (Pellitier et al. 2024)
  Holds for: ectomycorrhizal fungal communities across a precipitation gradient; targeted gene families; abstract only.
- Within one grazing and P-addition grassland site, species-level resolution within functional groups gave strong taxon-function consistency (Procrustes) and removed an apparent decoupling; the authors attribute stable function to reciprocal changes in two dominant species rather than redundancy. (Liu et al. 2023)
  Holds for: one grassland site under grazing and P addition.
- In anaerobic digesters, taxonomic convergence depended on taxonomic rank: inoculum identity was recoverable at genus but less at phylum level. (Jourdain et al. 2026)
  Holds for: anaerobic digestion communities, outside soil; abstract only.
- In lake enrichments, redundancy was higher with EC grouping than with KO. (Le Moigne et al. 2026)
  Holds for: lake enrichments, outside soil.
- The 845 pooled soil metagenomes and the subsurface sediments both find functional variability lower at every annotation level tested, so no reversal of ordering by unit was found in either. (Chen et al. 2022; Soufi et al. 2024)
  Holds for: soil SEED levels; sediment KEGG levels and EC.
- The taxonomic side is also measured differently across studies (16S amplicon in the 16-soil, NutNet and 14-year warming studies; read-based RefSeq in the 845 pooled metagenomes; MAG in the Ulva study), and this is not kept apart. (Fierer et al. 2012; Leff et al. 2015; Chen et al. 2022; Gao et al. 2021; van der Loos et al. 2025)
  Holds for: the soil and Ulva studies named.
- Platform differs across studies: GeoChip probes a few thousand preselected known genes, whose detection depends on hybridisation thresholds, while shotgun annotation typically covers a minority of reads (13 to 23% in the 16-soil study). (Fierer et al. 2012)
  Holds for: GeoChip against shotgun platforms.
- On the reviewer's observation, GeoChip underlies the three soil studies where function was as or more responsive and shotgun annotation underlies most "function lower" results; the reviewer found no study that ran both on the same soils for this comparison, so platform and result are confounded across the literature. This is not a tested result; it is drawn from three papers, two of them from one group (Zhou/Yang), and the answer on soil ordering leans on it. (Gao et al. 2021; Shen et al. 2016; Ma et al. 2017)
  Holds for: soil.
  Evidence: the reviewer's reading.
- Average genome size biases gene-abundance comparisons; it shifts with N and P addition and with heating in soil. (Leff et al. 2015; Nayfach and Pollard 2015; Barnett and Shade 2025)
  Holds for: the bias shown in human gut only; abstract only; in soil, shifts with N and P addition (NutNet) and with heating (coal fire).
- The effect of genome size on the functional-taxonomic turnover comparison was not tested in any study found. (a search result)
  Holds for: soil.
  Evidence: a search result.
  Searched for and not found.
- In soil, the comparison depends on functional unit, annotation and metric, but soil evidence for ordering reversals is thin: single-study evidence only, each soil claim resting on one study. (Chen et al. 2022; Xu et al. 2022; Gu et al. 2025)
  Holds for: soil.
  Evidence: a single source; rated "Weak for soil" by the research; a second reader disputes this: single-study evidence only.
- Not measured in soil: the ordering across dissimilarity measures, compositional (log-ratio) transforms, KO vs COG vs pangenome clusters vs MAG-resolved traits, rarefaction depth, relic-DNA removal and genome-size normalization; no reversal of ordering by any of these factors was found in soil because none was tested. (a search result)
  Holds for: soil.
  Evidence: a search result.
  The research does not say whether this was searched for.

### Ho and Huang's averaging argument and label-shuffling null

Builds on: which turnover is larger, functional or taxonomic.

- Converting taxon abundances to function abundances through a gene-content matrix sums over many taxa, so functional variability falls by statistical averaging even without any selection; the published abstract keeps this conclusion. 'Function lower than taxonomy' is therefore not by itself evidence of redundancy or selection. (Ho and Huang 2025; Ho and Huang 2024)
  Holds for: functions inferred through a gene-content matrix (FAPROTAX-style groups or genome annotations), not shotgun-measured profiles; the preprint read only as a fetch summary and the published body not read.
  Evidence: modelled; a single source; rated "Moderate as a methodological point, but single source" by the research; a second reader disputes this: that firmness rests on a summary of the preprint; limited by access (a source was not read in full; not the same as weak evidence).
- Their null permutes taxon labels across the gene-content matrix, which keeps function prevalences and scrambles taxon-function links. (Ho and Huang 2024)
  Holds for: functions inferred through a gene-content matrix.
- For soil- and leaf-derived communities grown in vitro on glucose (Goldford data), functional distance was significantly below the shuffles (functional variability lower than expected), which the authors read as selection for metabolic function. (Ho and Huang 2025; Goldford et al. 2018; Ho and Huang 2024)
  Holds for: in vitro, a single glucose medium; variability around a mean community within one environment; functions inferred through a gene-content matrix, so indirect for field soil and belonging to the marker-inferred case.
- The same null found no evidence of functional selection in bromeliad data (reanalysing the bromeliad study of stable functional-group structure), and found apparent selection in HMP stool to be artifactual: it disappeared under restricted shuffles. (Ho and Huang 2025; Louca et al. 2017; Ho and Huang 2024)
  Holds for: bromeliad communities and HMP stool.
- In gut communities in vitro, the null found selection with metabolomics-based groupings. (Ho and Huang 2024)
  Holds for: gut communities in vitro.
- Ho and Huang's label-shuffling null is the only direct microbial test of the functional-taxonomic difference, and the only soil-derived (in vitro) null result; it operates on functions inferred from taxa through a gene-content matrix (the logic of PICRUSt/FAPROTAX), not on shotgun-measured profiles, and tests variability around a mean community within one environment, not turnover across environments. Without it, the answer would rest on non-microbial and indirect microbial nulls. (Ho and Huang 2025; Ho and Huang 2024)
  Holds for: microbial data; marker-inferred function; within-environment dispersion.
  Evidence: a single source.
  A second reader found the search for contrary evidence one-sided.
- Between the preprint and the published version, the second confound was renamed from "bias toward environment-independent beneficial functions" to correlations between functions and taxonomic abundances handled by an "extended null model"; the title changed and the abstract conclusions are otherwise consistent; the published body, and so how the extended null model differs in body text, was not reached. (Ho and Huang 2025; Ho and Huang 2024)
  Holds for: bioRxiv 2024 against Cell Systems 2025.
  Evidence: limited by access (a source was not read in full; not the same as weak evidence).
- The averaging null has not been applied to field soil; on the reviewer's application of it, it bears on every "function lower" soil result, none of which controls for averaging. (the reviewer's application of the null to other studies)
  Holds for: the soil 'redundancy' studies (the 845 pooled metagenomes, serpentine, latitudinal forest, coal-fire, fertilizer and dryland studies); acceptable if kept labelled.
  Evidence: the reviewer's reading.
- The same null gives opposite answers in two systems: in vitro soil communities show selection, the bromeliad pattern is consistent with averaging. (Ho and Huang 2025)
  Holds for: in vitro soil-derived communities against bromeliads.
  Evidence: contested.

### null models of the functional-taxonomic comparison, in soil and elsewhere

Builds on: which turnover is larger, functional or taxonomic, Ho and Huang's averaging argument and label-shuffling null.

- No field-soil study was found that applies a null model (taxon-label shuffling of a gene-content matrix, trait randomization, phylogenetic null) to the difference between functional and taxonomic turnover, in shotgun, GeoChip, RNA or protein profiles; nulls across environmental-contrast sizes in soil were not measured either. (a search result)
  Holds for: field soil; both search agents looked, using Europe PMC boolean queries on soil, metagenome or GeoChip combined with null, shuffle, randomization, NST or betaNTI; the critic: appropriately worded as a search result.
  Evidence: a search result; rated "Weak for soil, where the evidence is absent for field metagenomes and single-study for in vitro soil-derived communities" by the research.
  Searched for and not found.
- Soil nulls found target taxonomic assembly only: SES of taxonomic beta in the precipitation experiment, iCAMP in the dryland study. (Xu et al. 2022; Sauma-Sanchez et al. 2024)
  Holds for: soil.
- In a Tibetan wetland spanning sediment, rhizosphere and bulk soils along salinity, separate null-model analyses put the deterministic share at 32.39% for taxonomy and 45.78%, 43.79% and 48.19% for methane, N and S gene composition (43.8 to 48.2% for function against 32.4%), which the authors read as the environment selecting function rather than taxa; the study does not test the difference itself, and removing it would remove the only soil-inclusive null comparison of functional and taxonomic determinism. (Zhang et al. 2025)
  Holds for: a Tibetan plateau saline-alkaline wetland, sediment and soil pooled; separate nulls on taxonomy and gene sets; the null framework was not named in the text the agent read; a different class of null from Ho and Huang's.
  Evidence: derived.
- A simulated 72% species loss in global metagenomes produced limited change in functional categories; this is a resampling construction, not a field comparison. (Chen et al. 2021)
  Holds for: global soil metagenomes; resampling; abstract only.
  Evidence: modelled.
- In lake enrichments, 80.2% of community pairs matched a taxon-shuffling null for between-community redundancy; communities were also less functionally dissimilar than random GTDB genome sets, read as selection plus shared pool origin. (Le Moigne et al. 2026)
  Holds for: lake enrichments.
- In bioreactors, taxa and genes assembled differently under a null; the preprint said stochasticity was more important for genes, driven by rare genes, while the published abstract drops this and stresses determinism under disturbance. (Santillan et al. 2020; Santillan et al. 2019)
  Holds for: mesocosm-scale bioreactors under press disturbance; abstract only for both versions.
- In contaminated sediments, functional and phylogenetic beta diversity correlated, with the null applied to taxonomy only. (Ren et al. 2016)
  Holds for: sediments along a contamination gradient; abstract only.
- Network nulls on gut gene-content networks and gut proteome networks show redundancy arises from nested gene sharing; this bears only indirectly on between-sample turnover. (Tian et al. 2020; Li et al. 2023)
  Holds for: human gut microbiome, DNA and protein (ultra-deep metaproteomics).
- Across 148 datasets, species-name randomization found functional decay "random given taxonomic decay" in most (13 deviated along space, 3 faster and 10 slower; 11 along environment, all but one faster); the authors note that hypervolume Sørensen gives lower taxonomic than functional similarity by construction for communities sharing no species. This gives independent support, outside bacteria, that most functional turnover is predictable from taxonomic turnover under a randomization null. (Graco-Roza et al. 2022)
  Holds for: 148 datasets including diatoms and fungi, no bacteria; deviating counts checked by the critic.
- Tropical trees along elevation turned over functionally faster than a trait-randomization null predicts. (Swenson et al. 2011)
  Holds for: tropical trees along an elevational gradient; read via a fetch summary.
- The 148-dataset synthesis (mostly null-consistent) and the tropical trees (faster than null) disagree. (Graco-Roza et al. 2022; Swenson et al. 2011)
  Holds for: non-microbial systems in the review's words; the critic: the 148-dataset synthesis includes diatoms and fungi but no bacteria.
  Evidence: contested.
- Louca et al. conclude that non-neutral processes shape within-function taxonomy and redundancy, while Ho and Huang find the bromeliad pattern consistent with averaging; the Louca originals were not reached in full text, so what their tests controlled for is known only from abstracts and from Ho and Huang's description. (Ho and Huang 2025; Louca et al. 2017; Louca et al. 2018)
  Holds for: bromeliad communities; the Louca studies known from abstracts.
  Evidence: contested; limited by access (a source was not read in full; not the same as weak evidence).
- On the reviewer's synthesis, non-microbial syntheses show that lower average functional decay can coexist with most datasets being null-consistent, the same caution Ho and Huang raise for microbes. (Graco-Roza et al. 2022)
  Holds for: the 148-dataset synthesis.
  Evidence: the reviewer's reading.

### functional redundancy as an explanation: for, against, critiques

Builds on: which turnover is larger, functional or taxonomic, Ho and Huang's averaging argument and label-shuffling null, null models of the functional-taxonomic comparison, in soil and elsewhere.

- Arguments for functional redundancy (asserted or measured without nulls) come, in soil, from the 845 pooled metagenomes and the serpentine, latitudinal forest, fertilizer, tillage and dryland studies, and elsewhere from the bromeliad, algal-surface, Ulva and sediment studies and a perspective. (Chen et al. 2022; Igwe and Afkhami 2026; Zhang et al. 2016; Pan et al. 2014; Souza et al. 2015; Sauma-Sanchez et al. 2024; Louca et al. 2017; Louca et al. 2018; Burke et al. 2011; van der Loos et al. 2025; Soufi et al. 2024)
  Holds for: asserted or measured without nulls.
- A perspective argues that redundancy and within-function variability are emergent properties of open systems, not drift. (Louca et al. 2018)
  Holds for: a perspective; abstract only.
  Evidence: asserted.
- Against or complicating redundancy: coupling holds when all genes are used (the marine time series); functional dispersion tracks taxonomic dispersion (the precipitation experiment); decoupling vanishes at species resolution within groups (one grassland site); averaging alone reproduces lower functional variability (Ho and Huang); function is more responsive under some weak contrasts (the 14-year warming and erosion studies). Fierer 2012, whose authors conclude that functional redundancy 'is not so pervasive as to obscure' the taxonomy-function relationship, is listed only as an annotation-fraction critique, not among these. (Gao et al. 2021; Liu et al. 2023; Ma et al. 2017; Xu et al. 2022; Ho and Huang 2025; Galand et al. 2018; Ho and Huang 2024)
  Holds for: soil and marine.
  A second reader found the search for contrary evidence one-sided.
- Critiques of redundancy readings are reported by ground: aggregation or averaging (Ho and Huang; modelled plus reanalysis); annotation fraction and bias (13 to 23% annotated in the 16-soil study; the marine time series); unannotated genes varying with soil (indirect); genome size (shown in human gut, with soil shifts under N and P addition and heating; indirect); asymmetric power or sample size between the functional and taxonomic tests (the serpentine study; the reviewer's reading); and marker-inferred function being circular (the ZnO, alpine PICRUSt2 and vermicomposting studies), with weak coupling of inferred to measured profiles in the marine time series. (Fierer et al. 2012; Leff et al. 2015; Igwe and Afkhami 2026; Dinesh et al. 2023; Li et al. 2024; Ho and Huang 2025; Galand et al. 2018; Aira et al. 2026; Nayfach and Pollard 2015; Barnett and Shade 2025; Holland-Moritz et al. 2021; Ho and Huang 2024)
  Holds for: soil and other habitats.
- No study was found that examines relic DNA, compositionality or sequencing depth for this comparison; these were not searched in depth by either agent, so the absence is weakly established. (a search result)
  Holds for: the functional-taxonomic comparison; the critic: soil studies exist on the effect of relic DNA on taxonomic beta diversity, and depth and annotation-rate effects were not searched.
  Evidence: a search result.
  Not searched for.
- The review's lean towards 'function lower is not evidence of redundancy' rests on Ho and Huang (modelled, single source) and Graco-Roza (non-bacterial); it is not simply echoed from the brief. (Ho and Huang 2025; Graco-Roza et al. 2022; Ho and Huang 2024)
  Holds for: the review's overall reading.
  Evidence: a single source.

## Do not say

Wordings the research itself says are wrong or overstated, each with the reason and what to say instead.

- Do not write: "Unlike the soil cross-biome result, marine function stays lower even under a strong contrast."
  Why: The soil cross-biome study made no magnitude comparison, and the 845 pooled soil metagenomes are themselves a strong-contrast soil case of function lower; the contrast treats a correlation result and a magnitude result as the same kind of finding.
  Say instead: In the Ulva microbiome across a 2000 km, 5 to 35 PSU salinity gradient, salinity explained R2 = 0.70 of taxonomic and 0.17 of KO-based functional variation (envfit), although 23 KEGG modules still shifted: function stays lower under a strong contrast. (van der Loos et al. 2025)
  Holds for: Ulva microbiome; one study, MAG-based taxonomy; envfit figures checked by the critic; the only strong-contrast case outside soil; soil has not tested function lower at a strong contrast with a common metric.
  Evidence: a single source.
  Say instead: In the global pooled dataset, functional Bray-Curtis similarity ranged 44 to 99% and taxonomic 9 to 100% (paired t = 67.5); climate plus soil explained 16.3% of taxonomic and 13.5% of functional variation (DistLM). The authors call this strong evidence for functional redundancy. It is the one large soil magnitude comparison, and it finds functional similarity higher than taxonomic at a strong (global) contrast; removing it would leave the 'function lower' ordering resting on small single-site studies and significance contrasts. (Chen et al. 2022)
  Holds for: 845 pooled public soil metagenomes; the profiles pool assembled and unassembled MG-RAST submissions from many studies; SEED level 3 (1,135 functions) compared with RefSeq genus (1,113 taxa); nothing tests whether a lower functional dissimilarity is expected from aggregation alone; figures checked against full text by the reviewer and the critic.
  Evidence: a single source.
- Do not write: "Three independent soil datasets show that functional and taxonomic dissimilarity covary."
  Why: The three datasets are not independent in lineage: two come from one group, and the third pools MG-RAST submissions that may include the first.
  Say instead: Across soils, functional and taxonomic dissimilarity are usually positively correlated; the clearest cases come from strong cross-biome or between-site contrasts (Mantel r 0.76 to 0.82 across 16 soils; Spearman rho 0.87 across 6 NutNet sites; r2 0.28 across 845 pooled metagenomes), and strong contrasts give covariation. (Fierer et al. 2012; Leff et al. 2015; Chen et al. 2022)
  Holds for: three soil datasets at strong contrasts, all using Bray-Curtis on annotated profiles and correlation-type tests; none used a null model; the critic: not independent in lineage, as two come from one group and the third pools MG-RAST submissions that may include the first.
  Evidence: measured; rated "Moderate for covariation at strong contrasts" by the research; a second reader disputes this: these datasets are not independent in lineage.
- Do not write: "Xu et al. 2022 is the only within-site test of how contrast size changes the functional-taxonomic comparison."
  Why: It measures within-treatment dispersion with no directional shift in either community and does not compare the two turnovers' magnitudes, so it bears only indirectly on the question and should be labelled indirect.
  Say instead: In a single-site precipitation experiment, ±30% precipitation slightly decreased and ±60% strongly increased within-treatment dispersion (PERMDISP) of taxa, genes, proteins and enzyme activities alike; gene, protein and enzyme dissimilarities were Mantel-correlated with taxonomic dissimilarity, and neither taxonomy nor function showed a directional PERMANOVA shift. The authors conclude that "taxonomic stochasticity translated into functional stochasticity", not redundancy. (Xu et al. 2022)
  Holds for: one Eurasian steppe site under two magnitudes of precipitation change; within-treatment dispersion, not a comparison of the two turnovers' magnitudes, so indirect for the ordering question; the ±30% decrease in function confirmed by the critic.
  Evidence: measured.
- Do not write: "Ho and Huang's null is the direct microbial test of the functional-taxonomic difference."
  Why: It works on functions inferred from taxonomy through a gene-content matrix and on variability within one environment; the review does not label it as marker-inferred or as dispersion rather than cross-environment turnover.
  Say instead: Ho and Huang's label-shuffling null is the only direct microbial test of the functional-taxonomic difference, and the only soil-derived (in vitro) null result; it operates on functions inferred from taxa through a gene-content matrix (the logic of PICRUSt/FAPROTAX), not on shotgun-measured profiles, and tests variability around a mean community within one environment, not turnover across environments. Without it, the answer would rest on non-microbial and indirect microbial nulls. (Ho and Huang 2025; Ho and Huang 2024)
  Holds for: microbial data; marker-inferred function; within-environment dispersion.
  Evidence: a single source.
  A second reader found the search for contrary evidence one-sided.
- Do not write: "In soil, the functional-taxonomic gap widens as functions are aggregated."
  Why: This is the reviewer's inference from one study, phrased as a finding; the authors state only that functional similarity was higher at SEED levels 1 and 2 against all five taxonomic ranks.
  Say instead: In the 845 pooled soil metagenomes, functional similarity exceeded taxonomic similarity at SEED levels 1 and 2 against all five taxonomic ranks, so the ordering did not reverse at any combination tested; the authors say coarser levels are more conserved, and state only that the ordering held at all levels. It is the only soil evidence on annotation level. (Chen et al. 2022)
  Holds for: 845 metagenomes (Chen 2022); SEED levels; rechecked by the reviewer.
  Evidence: a single source.
- Do not write: "Aggregation alone lowers functional variability, so in every soil study 'function lower' is not evidence of redundancy."
  Why: This is framed as a methodological point bearing on every soil study, but it rests on Ho and Huang alone and is modelled.
  Say instead: Converting taxon abundances to function abundances through a gene-content matrix sums over many taxa, so functional variability falls by statistical averaging even without any selection; the published abstract keeps this conclusion. 'Function lower than taxonomy' is therefore not by itself evidence of redundancy or selection. (Ho and Huang 2025; Ho and Huang 2024)
  Holds for: functions inferred through a gene-content matrix (FAPROTAX-style groups or genome annotations), not shotgun-measured profiles; the preprint read only as a fetch summary and the published body not read.
  Evidence: modelled; a single source; rated "Moderate as a methodological point, but single source" by the research; a second reader disputes this: that firmness rests on a summary of the preprint; limited by access (a source was not read in full; not the same as weak evidence).
  Say instead: The averaging null has not been applied to field soil; on the reviewer's application of it, it bears on every "function lower" soil result, none of which controls for averaging. (the reviewer's application of the null to other studies)
  Holds for: the soil 'redundancy' studies (the 845 pooled metagenomes, serpentine, latitudinal forest, coal-fire, fertilizer and dryland studies); acceptable if kept labelled.
  Evidence: the reviewer's reading.
- Do not write: "GeoChip underlies the soil studies where function was as or more responsive, so the reverse ordering is a platform effect."
  Why: It is the reviewer's cross-study observation, drawn from three papers, two of them from one group (Zhou/Yang), and not a tested result.
  Say instead: On the reviewer's observation, GeoChip underlies the three soil studies where function was as or more responsive and shotgun annotation underlies most "function lower" results; the reviewer found no study that ran both on the same soils for this comparison, so platform and result are confounded across the literature. This is not a tested result; it is drawn from three papers, two of them from one group (Zhou/Yang), and the answer on soil ordering leans on it. (Gao et al. 2021; Shen et al. 2016; Ma et al. 2017)
  Holds for: soil.
  Evidence: the reviewer's reading.
- Do not write: "Marine and host-associated studies mostly report lower functional turnover."
  Why: This mixes FAPROTAX-derived, abstract-only and single-time-series evidence; the only strong-contrast case is one study with MAG-based taxonomy.
  Say instead: Outside soil, marine and host-associated studies mostly report lower functional turnover, including under a strong 2000 km salinity contrast and on algal surfaces, while a marine time series finds tight coupling; this mixes FAPROTAX-derived, abstract-only and single-time-series evidence, and the only strong-contrast case is the Ulva study across 2000 km of salinity. (Galand et al. 2018; Louca et al. 2016; Louca et al. 2017; Burke et al. 2011; van der Loos et al. 2025)
  Holds for: marine and host-associated systems, kept separate from soil.
- Do not write: "The choice of metric reverses the functional-taxonomic conclusion."
  Why: This rests on one study (27 paired steppe and cropland soils), flagged in the sensitivity note but stated generally in the review.
  Say instead: On the same 27 paired steppe and cropland soils, the dispersion-based analysis found KEGG gene assemblages homogenized in cropland at local and regional scales while bacterial taxa were homogenized only locally, whereas an earlier distance-decay-slope analysis of the same data had found greater KEGG functional turnover in cropland: the choice of turnover statistic changed the functional conclusion. (Gu et al. 2025)
  Holds for: 27 paired steppe and cropland soils; the only soil case where metric choice reversed a conclusion; rechecked by the reviewer.
  Evidence: a single source.
- Do not write: "Graco-Roza et al. 2022 is a non-microbial synthesis."
  Why: It includes diatoms and fungi (it lacks bacteria), so calling it non-microbial is wrong and blurs the microbial against non-microbial split.
  Say instead: Across 148 trait datasets, mean Mantel r along space was 0.254 taxonomic against 0.115 functional, with about 31 of 148 datasets reversed. (Graco-Roza et al. 2022)
  Holds for: 148 datasets including diatoms and fungi but no bacteria, so not 'non-microbial'; Mantel values checked by the critic; the critic's 13 deviating datasets are deviations from the randomization null, a different count from these reversals.
- Do not write: "In soil, separate assembly nulls show function is more deterministic than taxonomy."
  Why: The wetland study pools sediment and soil, uses separate nulls on taxonomy and gene sets, and does not test the difference itself.
  Say instead: In a Tibetan wetland spanning sediment, rhizosphere and bulk soils along salinity, separate null-model analyses put the deterministic share at 32.39% for taxonomy and 45.78%, 43.79% and 48.19% for methane, N and S gene composition (43.8 to 48.2% for function against 32.4%), which the authors read as the environment selecting function rather than taxa; the study does not test the difference itself, and removing it would remove the only soil-inclusive null comparison of functional and taxonomic determinism. (Zhang et al. 2025)
  Holds for: a Tibetan plateau saline-alkaline wetland, sediment and soil pooled; separate nulls on taxonomy and gene sets; the null framework was not named in the text the agent read; a different class of null from Ho and Huang's.
  Evidence: derived.
- Do not write: "Ho and Huang's null shows selection for metabolic function in soil communities."
  Why: The soil result comes from a single in vitro glucose medium, on functions inferred through a gene-content matrix and variability within one environment, so it is indirect for field soil.
  Say instead: For soil- and leaf-derived communities grown in vitro on glucose (Goldford data), functional distance was significantly below the shuffles (functional variability lower than expected), which the authors read as selection for metabolic function. (Ho and Huang 2025; Goldford et al. 2018; Ho and Huang 2024)
  Holds for: in vitro, a single glucose medium; variability around a mean community within one environment; functions inferred through a gene-content matrix, so indirect for field soil and belonging to the marker-inferred case.
- Do not write: "Ho and Huang's preprint, Barnett and Shade, Burke and Swenson were read in full text."
  Why: They were read through fetch summaries, which are not a full-text reading, so they should be labelled secondary or abstract-level unless the text was read.
- Do not write: "The dryland study's 'function lower' result was read in full text."
  Why: Only its abstract and methods were read, so it is abstract-level for its result claim.
  Say instead: Similar functional capacities in arid and hyperarid saline drylands despite structural differences. (Sauma-Sanchez et al. 2024)
  Holds for: arid and hyperarid saline drylands; only the abstract and methods closely read, so abstract-level for its result claim.
- Do not write: "Between serpentine and non-serpentine soils, functional turnover is lower than taxonomic turnover."
  Why: The result sets a significant test against a non-significant one on datasets of different size after QC, which suggests limited power on the functional side rather than an absence of structure.
  Say instead: Between serpentine and non-serpentine site pairs, bacterial composition differed (PERMANOVA R2 = 0.061, P = 0.004) while eggNOG functional composition did not (R2 = 0.027, P = 0.391); the authors conclude redundancy, and note that specialized functions such as siderophore biosynthesis did differ. (Igwe and Afkhami 2026)
  Holds for: serpentine and non-serpentine soil pairs; residual df 19 against 16; figures rechecked by the reviewer and the critic.
  Evidence: measured.
  Say instead: On the reviewer's reading, the serpentine result is a significant test set against a non-significant one, on datasets of different size after QC (the functional dataset is smaller): site pairs explained about 56% of variation in both functional (non-significant, F(19,16)) and bacterial (significant) composition, which suggests limited power on the functional side rather than an absence of structure. (Igwe and Afkhami 2026)
  Holds for: serpentine and non-serpentine soil pairs.
  Evidence: the reviewer's reading.
- Do not write: "Along the Changbai elevation gradient, functional turnover is stronger than taxonomic turnover."
  Why: That is the reviewer's reading; the authors describe the patterns as similar, and the two r values come from different platforms and are not on a common scale.
  Say instead: Along the Changbai elevation gradient, functional-gene distance decay (r = 0.708) was stronger than bacterial (r = 0.409) on the reviewer's reading; the authors describe the patterns as similar, with different drivers (pH for taxa, DOC for genes), and the two r values come from different platforms (16S against GeoChip) and are not on a common scale. (Shen et al. 2016)
  Holds for: Changbai elevation gradient.
  Evidence: the reviewer's reading.
- Do not write: "The ZnO and alpine PICRUSt studies are two independent tests of soil functional redundancy."
  Why: Both infer function from the same 16S data, so they are not independent tests.
  Say instead: With marker-inferred function, ZnO dose separated taxa but not PICRUSt-type predicted functions. (Dinesh et al. 2023)
  Holds for: soil polluted with nano ZnO, by dose; function inferred from the same 16S data, so not independent of taxonomy; abstract only.
  Evidence: derived.
  Say instead: Along an alpine gradient, PICRUSt2 function was redundant and tracked phylogenetic more than taxonomic dissimilarity. (Li et al. 2024)
  Holds for: an alpine altitudinal gradient; function inferred from the same 16S data, so not independent of taxonomy.
  Evidence: derived.
- Do not write: "Chronosequences show functional and taxonomic turnover diverging."
  Why: The chronosequence papers report alpha diversity moving in opposite directions, but no paired turnover comparison.
  Say instead: Over 143 years of grassland restoration, bacterial richness falls while SEED functional richness expands (alpha diversity; no paired turnover comparison). (Goodall et al. 2026)
  Holds for: grassland restoration chronosequence; alpha, not turnover; the preprint's "profound functional decoupling" was softened to "a decoupling" in the published version.
  Say instead: Along Swedish succession, taxonomic diversity falls while C, N and P gene diversity rises, with PICRUSt2 used for the redundancy analyses (alpha diversity; no paired turnover comparison). (Sveen et al. 2025)
  Holds for: Swedish successional chronosequence; alpha, not turnover; the preprint's "causal link" was softened to "the link" in the published version.
- Do not write: "Within-treatment dispersion results answer how turnover across environments compares."
  Why: The precipitation experiment's PERMDISP within treatments and Ho and Huang's distance from the mean community in one medium are within-environment dispersion, used without an indirect label to answer questions about turnover across environments.
  Say instead: In a single-site precipitation experiment, ±30% precipitation slightly decreased and ±60% strongly increased within-treatment dispersion (PERMDISP) of taxa, genes, proteins and enzyme activities alike; gene, protein and enzyme dissimilarities were Mantel-correlated with taxonomic dissimilarity, and neither taxonomy nor function showed a directional PERMANOVA shift. The authors conclude that "taxonomic stochasticity translated into functional stochasticity", not redundancy. (Xu et al. 2022)
  Holds for: one Eurasian steppe site under two magnitudes of precipitation change; within-treatment dispersion, not a comparison of the two turnovers' magnitudes, so indirect for the ordering question; the ±30% decrease in function confirmed by the critic.
  Evidence: measured.
  Say instead: Ho and Huang's label-shuffling null is the only direct microbial test of the functional-taxonomic difference, and the only soil-derived (in vitro) null result; it operates on functions inferred from taxa through a gene-content matrix (the logic of PICRUSt/FAPROTAX), not on shotgun-measured profiles, and tests variability around a mean community within one environment, not turnover across environments. Without it, the answer would rest on non-microbial and indirect microbial nulls. (Ho and Huang 2025; Ho and Huang 2024)
  Holds for: microbial data; marker-inferred function; within-environment dispersion.
  Evidence: a single source.
  A second reader found the search for contrary evidence one-sided.
- Do not write: "In soil, the unannotated fraction biases functional turnover."
  Why: That unknown-function genes vary with soil properties is indirect support for an annotation-bias critique, not a demonstration of its effect on turnover.
  Say instead: Unknown-function genes are prevalent in fine-textured, higher-pH soils and are often mobile-element associated, so the unannotated fraction can vary along soil gradients (with soil properties): indirect support for an annotation-bias critique, not a demonstration of its effect on turnover. (Holland-Moritz et al. 2021)
  Holds for: soils; a preprint, abstract only.
- Do not write: "Global N-cycling pathways turn over less than the genera that encode them."
  Why: The study contrasts drivers, not turnovers, so it is indirect for the comparison.
  Say instead: Global N-cycling pathway frequencies track habitat and soil C and N much better than the genera that encode them; this contrasts drivers, not turnovers, so it is indirect. (Nelson et al. 2016)
  Holds for: global soils; N-cycling traits.
- Do not write: "A marine time series and a soil experiment contradict each other on whether annotation matters."
  Why: They use different measures (regression of similarities against within-treatment dispersion) and habitats, so in the review's words they do not directly contradict.
  Say instead: The marine time series finds that restricting to annotated genes weakens the coupling (all-read coupling is strongest), while the soil precipitation experiment finds all-read and annotated dissimilarity behave alike; the two use different measures (regression of similarities against within-treatment dispersion) and habitats, so they do not directly contradict. (Xu et al. 2022; Galand et al. 2018)
  Holds for: marine water against one soil experiment.

## Gaps

What the research did not establish.

- Bahram et al. 2018 (Nature 560:233-237), the largest paired metabarcoding plus metagenome global topsoil set (shotgun plus amplicon on the same samples), was not read beyond an abstract; the publisher was not tried; the stage-2 check says it should be read in full by hand. (Bahram et al. 2018)
  The research does not say whether this was searched for.
- Relic DNA: soil studies exist on its effect on taxonomic beta diversity (Carini et al. 2016 Nat Microbiol; Lennon et al. 2018 mBio; mBio 2020), indirect evidence for the taxonomic side of the comparison that the review does not cite while reporting relic-DNA critiques as not found.
  Not searched for.
- Sequencing depth and annotation-rate effects on functional-profile dissimilarity (for example the comparative-metagenomics normalization literature beyond Nayfach 2015); compositional (Aitchison, CLR) comparisons were reported as not found without naming the routes.
  Not searched for.
- Soil metatranscriptome (and protein) turnover compared with taxonomic turnover: no study reported, the only non-DNA soil case being the precipitation experiment's metaproteome dispersion; forest-soil and rhizosphere metatranscriptome studies were not searched specifically.
  Not searched for.
- Recent soil chronosequence metagenome studies (Greenlandic glacial chronosequence, FEMS Microbiol Ecol 2026; ecosystem retrogression, mLife 2026; ISME Commun 2026) not assessed for paired turnover comparisons; chronosequences with a head-to-head beta comparison were not measured.
  The research does not say whether this was searched for.
- Chen et al. 2021a (water metagenomes, function-taxonomy similarity r2 0.3344, function lower), cited within the global soil study, is not reported under other habitats.
  The research does not say whether this was searched for.
- The taxonomic side's measurement type (16S amplicon, read-based RefSeq, MAG) is not tabulated per study, although it plausibly affects the ordering.
  The research does not say whether this was searched for.
- Fungal shotgun turnover comparisons beyond the ectomycorrhizal and mycobiome studies; archaeal and protist functional turnover in soil are not addressed.
  The research does not say whether this was searched for.
- A per-study table giving measurement type, functional unit, annotation, dissimilarity measure and contrast, as the brief's evidence-to-gather bullet requires; these attributes are scattered through the text.
  The research does not say whether this was searched for.
- The stage-2 check was triggered: write a follow-up brief, sized separately, on the habitat classes with shotgun results not assessed (soil chronosequence metagenomes, soil metatranscriptomes, fungal, archaeal and protist functional turnover, aquatic MG-RAST comparisons) and on the per-study measurement table, with methodological gaps on both sides (relic DNA on the taxonomic side; depth, annotation rate and compositional measures on the functional side); no new null-model family with direct soil results was named.
  The research does not say whether this was searched for.
- The published Ho and Huang (Cell Systems 2025) body text was not read, and the preprint was read only as a fetch summary, although the bioRxiv full text is openly reachable; how the published 'extended null model' differs from the preprint is unknown. (Ho and Huang 2025; Ho and Huang 2024)
  The research does not say whether this was searched for.
- A label-shuffling, trait or phylogenetic null applied to field-soil shotgun, GeoChip, RNA or protein profiles, testing whether functional turnover is lower than expected given taxonomic turnover, including across environmental-contrast sizes.
  Searched for and not found.
- A soil test of how the functional-taxonomic gap scales with environmental distance.
  Searched for and not found.
- Soil tests of the ordering across dissimilarity measures, compositional transforms, functional units (KO, COG, pangenome clusters, MAG-resolved traits), rarefaction depth, relic-DNA removal and genome-size normalization.
  The research does not say whether this was searched for.
- The Louca et al. originals (2016 Science; 2016/2017 and 2018 Nat Ecol Evol) and Villéger et al. 2013 were not reached in full text, so what the Louca tests controlled for is known only from abstracts and from Ho and Huang's description. (Louca et al. 2016; Louca et al. 2017; Louca et al. 2018; Villeger et al. 2013)
  The research does not say whether this was searched for.
- The marine time-series (Galand 2018) figures rest on the agents' reading: its full-text XML returned empty to the reviewer. (Galand et al. 2018)
  The research does not say whether this was searched for.
- The note contradicts itself on its sources not obtained: the list says nothing beyond a citation was reachable for them and none supports any claim in the review, yet it records abstracts obtained or used for several of them (Bahram 2018, Fierer 2013, the Louca studies, Villéger 2013), and the Ho and Huang Cell Systems and Louca abstracts are cited in the review.
  The research does not say whether this was searched for.

## References

- Aira, Manuel; Perez-Losada, Marcos; Crandall, Keith A.; Dominguez, Jorge (2026). Faster turnover of taxonomic over functional bacterial composition during vermicomposting indicates increasing functional redundancy. PLOS One 21(7): e0354276. https://doi.org/10.1371/journal.pone.0354276
- Anderson, Marti J. (2006). Distance-Based Tests for Homogeneity of Multivariate Dispersions. Biometrics 62(1): 245--253. https://doi.org/10.1111/j.1541-0420.2005.00440.x
- Bahram, Mohammad; Hildebrand, Falk; Forslund, S. K.; others (2018). Structure and function of the global topsoil microbiome. Nature 560(7717): 233--237. https://doi.org/10.1038/s41586-018-0386-6
- Barnett, Samuel E.; Shade, Ashley (2025). Disturbance increases soil microbiome functional redundancy but decreases capacity for insurance via winnowed environmental responsiveness. bioRxiv. https://doi.org/10.1101/2025.09.19.677300
- Burke, Catherine; Steinberg, Peter; Rusch, Doug; Kjelleberg, Staffan; Thomas, Torsten (2011). Bacterial community assembly based on functional genes rather than species. Proceedings of the National Academy of Sciences 108(34): 14288--14293. https://doi.org/10.1073/pnas.1101591108
- Chen, Huaihai; Ma, Kayan; Huang, Yu; Yao, Zhiyuan; Chu, Chengjin (2021). Stable soil microbial functional structure responding to biodiversity loss based on metagenomic evidences. Frontiers in Microbiology 12: 716764. https://doi.org/10.3389/fmicb.2021.716764
- Chen, Huaihai; Ma, Kayan; Lu, Caiyan; Fu, Qi; Qiu, Yingbo; Zhao, Jiayi; Huang, Yu; Yang, Yuchun; Schadt, Christopher W.; Chen, Hao (2022). Functional redundancy in soil microbial community based on metagenomics across the globe. Frontiers in Microbiology 13: 878978. https://doi.org/10.3389/fmicb.2022.878978
- Dinesh, R.; Sreena, C.P.; Sheeja, T.E.; Kumar, I.P. Vijesh; Praveena, R.; Charles, Sona; Srinivasan, V.; Jayarajan, K.; Sajith, V.; Subila, K.P.; Haritha, P. (2023). Soil polluted with nano ZnO reveals unstable bacterial communities and decoupling of taxonomic and functional diversities. Science of the Total Environment 889: 164285. https://doi.org/10.1016/j.scitotenv.2023.164285
- Fierer, Noah; Leff, Jonathan W.; Adams, Byron J.; Nielsen, Uffe N.; Bates, Scott Thomas; Lauber, Christian L.; Owens, Sarah; Gilbert, Jack A.; Wall, Diana H.; Caporaso, J. Gregory (2012). Cross-biome metagenomic analyses of soil microbial communities and their functional attributes. Proceedings of the National Academy of Sciences 109(52): 21390--21395. https://doi.org/10.1073/pnas.1215210110
- Frey, Beat; Rast, Basil M.; Qi, Weihong; Stierli, Beat; Brunner, Ivano (2022). Long-term mercury contamination does not affect the microbial gene potential for C and N cycling in soils but enhances detoxification gene abundance. Frontiers in Microbiology 13: 1034138. https://doi.org/10.3389/fmicb.2022.1034138
- Galand, Pierre E.; Pereira, Olivier; Hochart, Corentin; Auguet, Jean Christophe; Debroas, Didier (2018). A strong link between marine microbial community composition and function challenges the idea of functional redundancy. The ISME Journal 12(10): 2470--2478. https://doi.org/10.1038/s41396-018-0158-1
- Gao, Ying; Ding, Junjun; Yuan, Mengting; Chiariello, Nona; Docherty, Kathryn; Field, Chris; Gao, Qun; Gu, Baohua; Gutknecht, Jessica; Hungate, Bruce A.; Le Roux, Xavier; Niboyet, Audrey; Qi, Qi; Shi, Zhou; Zhou, Jizhong; Yang, Yunfeng (2021). Long-term warming in a Mediterranean-type grassland affects soil bacterial functional potential but not bacterial taxonomic composition. npj Biofilms and Microbiomes 7(1): 17. https://doi.org/10.1038/s41522-021-00187-7
- Goldford, Joshua E.; Lu, Nanxi; Bajic, Djordje; Estrela, Sylvie; Tikhonov, Mikhail; Sanchez-Gorostiaga, Alicia; Segre, Daniel; Mehta, Pankaj; Sanchez, Alvaro (2018). Emergent simplicity in microbial community assembly. Science 361(6401): 469--474. https://doi.org/10.1126/science.aat1168
- Goodall, Tim; Busi, Susheel Bhanu; Jones, Briony; Thorpe, Amy; Griffiths, Robert I; Redhead, John; Hulmes, Lucy; Hulmes, Sarah; Ridding, Lucy; Peyton, Jodey; Pereira, Gloria; Gweon, Hyun Soon; Read, Daniel S; Pywell, Richard (2026). Taxonomic filtering accompanies functional expansion during long-term soil restoration. The ISME Journal 20(1): wrag131. https://doi.org/10.1093/ismejo/wrag131
- Graco-Roza, Caio; Aarnio, Sonja; Abrego, Nerea; Acosta, Alicia T. R.; Alahuhta, Janne; Altman, Jan; Angiolini, Claudia; Aroviita, Jukka; Attorre, Fabio; Baastrup-Spohr, Lars; Barrera-Alba, Jose J.; Belmaker, Jonathan; Biurrun, Idoia; Bonari, Gianmaria; Bruelheide, Helge; Burrascano, Sabina; Carboni, Marta; Cardoso, Pedro; Carvalho, Jose C.; Castaldelli, Giuseppe; Christensen, Morten; Correa, Gilsineia; Dembicz, Iwona; Dengler, Jurgen; Dolezal, Jiri; Domingos, Patricia; Eros, Tibor; Ferreira, Carlos E. L.; Filibeck, Goffredo; Floeter, Sergio R.; Friedlander, Alan M.; Gammal, Johanna; Gavioli, Anna; Gossner, Martin M.; Granot, Itai; Guarino, Riccardo; Gustafsson, Camilla; Hayden, Brian; He, Siwen; Heilmann-Clausen, Jacob; Heino, Jani; Hunter, John T.; Huszar, Vera L. M.; Janisova, Monika; Jyrkankallio-Mikkola, Jenny; Kahilainen, Kimmo K.; Kemppinen, Julia; Kozub, ukasz; Kruk, Carla; Kulbiki, Michel; Kuzemko, Anna; le Roux, Peter Christiaan; Lehikoinen, Aleksi; de Lima, Domenica Teixeira; Lopez-Urrutia, Angel; Lukacs, Balazs A.; Luoto, Miska; Mammola, Stefano; Marinho, Marcelo M.; Menezes, Luciana S.; Milardi, Marco; Miranda, Marcela; Moser, Gleyci A. O.; Mueller, Joerg; Niittynen, Pekka; Norkko, Alf; Nowak, Arkadiusz; Ometto, Jean P.; Ovaskainen, Otso; Overbeck, Gerhard E.; Pacheco, Felipe S.; Pajunen, Virpi; Palpurina, Salza; Picazo, Felix; Campos, Juan Antonio; Rodil, Ivan F.; Sabatini, Francesco M.; Salingre, Shira; De Sanctis, Michele; Segura, Angel M.; da Silva, Lucia H. S.; Stevanovic, Zora D.; Swacha, Grzegorz; Teittinen, Anette; Tolonen, Kimmo T.; Tsiripidis, Ioannis; Virta, Leena; Wang, Beixin; Wang, Jianjun; Weisser, Wolfgang; Xu, Yuan; Soininen, Janne (2022). Distance decay 2.0: A global synthesis of taxonomic and functional turnover in ecological communities. Global Ecology and Biogeography 31(7): 1399--1421. https://doi.org/10.1111/geb.13513
- Gu, Haidong; Liu, Zhuxiu; Liu, Song; Hu, Xiaojing; Yu, Zhenhua; Li, Yansheng; Li, Lujun; Sui, Yueyu; Jin, Jian; Liu, Xiaobing; Jia, Zhongjun; Sun, Lei; Adams, Jonathan M; van der Heijden, Marcel G A; Liu, Junjie; Wang, Guanghua (2025). Land conversion to cropland homogenizes variation in soil biota, gene assemblages, and ecological strategies on local and regional scales. The ISME Journal 19(1): wraf264. https://doi.org/10.1093/ismejo/wraf264
- Ho, Po-Yi; Huang, Kerwyn Casey (2024). Challenges in quantifying functional redundancy and selection in microbial communities. bioRxiv. https://doi.org/10.1101/2024.03.26.586891
- Ho, Po-Yi; Huang, Kerwyn Casey (2025). Challenges in interpreting functional redundancy and quantifying functional selection in microbial communities. Cell Systems 16(8): 101350. https://doi.org/10.1016/j.cels.2025.101350
- Holland-Moritz, Hannah; Vanni, Chiara; Fernandez-Guerra, Antonio; Bissett, Andrew; Fierer, Noah (2021). An ecological perspective on microbial genes of unknown function in soil. bioRxiv. https://doi.org/10.1101/2021.12.02.470747
- Igwe, Alexandria N.; Afkhami, Michelle E. (2026). Redundancy maintains microbial ecosystem functional potential despite taxonomic shifts between serpentine and nonserpentine soils. Microbial Genomics 12(9). https://doi.org/10.1099/mgen.0.001835
- Jourdain, Lisa; Leininger, Aaron; Pacheco, Alan R; Gu, Wenyu (2026). Environmental selection constrains metabolic network architecture despite taxonomic turnover in anaerobic digestion communities. The ISME Journal 20(1): wrag145. https://doi.org/10.1093/ismejo/wrag145
- Kato, Hiromi; Mori, Hiroshi; Maruyama, Fumito; Toyoda, Atsushi; Oshima, Kenshiro; Endo, Ryo; Fuchu, Genki; Miyakoshi, Masatoshi; Dozono, Ayumi; Ohtsubo, Yoshiyuki; Nagata, Yuji; Hattori, Masahira; Fujiyama, Asao; Kurokawa, Ken; Tsuda, Masataka (2015). Time-series metagenomic analysis reveals robustness of soil microbiome against chemical disturbance. DNA Research 22(6): 413--424. https://doi.org/10.1093/dnares/dsv023
- Le Moigne, Alizee; Andrei, Adrian-Stefan; Pernthaler, Jakob (2026). Linking stochastic assembly to functional potential, redundancy, and trait patterns in bacterial communities. Microbiome 14(1): 201. https://doi.org/10.1186/s40168-026-02442-5
- Leff, Jonathan W.; Jones, Stuart E.; Prober, Suzanne M.; Barberan, Albert; Borer, Elizabeth T.; Firn, Jennifer L.; Harpole, W. Stanley; Hobbie, Sarah E.; Hofmockel, Kirsten S.; Knops, Johannes M. H.; McCulley, Rebecca L.; Pierre, Kimberly La; Risch, Anita C.; Seabloom, Eric W.; Schutz, Martin; Steenbock, Christopher; Stevens, Carly J.; Fierer, Noah (2015). Consistent responses of soil microbial communities to elevated nutrient inputs in grasslands across the globe. Proceedings of the National Academy of Sciences 112(35): 10967--10972. https://doi.org/10.1073/pnas.1508382112
- Li, Leyuan; Wang, Tong; Ning, Zhibin; Zhang, Xu; Butcher, James; Serrana, Joeselle M.; Simopoulos, Caitlin M. A.; Mayne, Janice; Stintzi, Alain; Mack, David R.; Liu, Yang-Yu; Figeys, Daniel (2023). Revealing proteome-level functional redundancy in the human gut microbiome using ultra-deep metaproteomics. Nature Communications 14(1): 3428. https://doi.org/10.1038/s41467-023-39149-2
- Li, Xianping; Li, Teng; Li, Huixin (2024). Asynchronous patterns in soil bacterial diversity and functional potentials along an alpine altitudinal gradient. Frontiers in Microbiology 15: 1428815. https://doi.org/10.3389/fmicb.2024.1428815
- Liu, Huaiqiang; Li, Frank Yonghong; Liu, Jiayue; Shi, Chunjun; Tang, Kuanyan; Yang, Qianhui; Liu, Yu; Fu, Qiang; Gao, Xiaotian; Wang, Ning; Guo, Wei (2023). The reciprocal changes in dominant species with complete metabolic functions explain the decoupling phenomenon of microbial taxonomic and functional composition in a grassland. Frontiers in Microbiology 14: 1113157. https://doi.org/10.3389/fmicb.2023.1113157
- Louca, Stilianos; Jacques, Saulo M. S.; Pires, Aliny P. F.; Leal, Juliana S.; Srivastava, Diane S.; Parfrey, Laura Wegener; Farjalla, Vinicius F.; Doebeli, Michael (2017). High taxonomic variability despite stable functional structure across microbial communities. Nature Ecology & Evolution 1(1): 1--12. https://doi.org/10.1038/s41559-016-0015
- Louca, Stilianos; Parfrey, Laura Wegener; Doebeli, Michael (2016). Decoupling function and taxonomy in the global ocean microbiome. Science 353(6305): 1272--1277. https://doi.org/10.1126/science.aaf4507
- Louca, Stilianos; Polz, Martin F.; Mazel, Florent; Albright, Michaeline B. N.; Huber, Julie A.; O'Connor, Mary I.; Ackermann, Martin; Hahn, Aria S.; Srivastava, Diane S.; Crowe, Sean A.; Doebeli, Michael; Parfrey, Laura Wegener (2018). Function and functional redundancy in microbial systems. Nature Ecology & Evolution 2(6): 936--943. https://doi.org/10.1038/s41559-018-0519-1
- Ma, Xingyu; Zhao, Cancan; Gao, Ying; Liu, Bin; Wang, Tengxu; Yuan, Tong; Hale, Lauren; Nostrand, Joy D. Van; Wan, Shiqiang; Zhou, Jizhong; Yang, Yunfeng (2017). Divergent taxonomic and functional responses of microbial communities to field simulation of aeolian soil erosion and deposition. Molecular Ecology 26(16): 4186--4196. https://doi.org/10.1111/mec.14194
- Nayfach, Stephen; Pollard, Katherine S (2015). Average genome size estimation improves comparative metagenomics and sheds light on the functional ecology of the human microbiome. Genome Biology 16(1): 51. https://doi.org/10.1186/s13059-015-0611-7
- Nelson, Michaeline B.; Martiny, Adam C.; Martiny, Jennifer B. H. (2016). Global biogeography of microbial nitrogen-cycling traits in soil. Proceedings of the National Academy of Sciences 113(29): 8033--8040. https://doi.org/10.1073/pnas.1601070113
- Pan, Yao; Cassman, Noriko; de Hollander, Mattias; Mendes, Lucas W.; Korevaar, Hein; Geerts, Rob H.E.M.; van Veen, Johannes A.; Kuramae, Eiko E. (2014). Impact of long-term N, P, K, and NPK fertilization on the composition and potential functions of the bacterial community in grassland soil. FEMS Microbiology Ecology 90(1): 195--205. https://doi.org/10.1111/1574-6941.12384
- Pellitier, Peter T; Nuland, Michael Van; Salamov, Asaf; Grigoriev, Igor V; Peay, Kabir G (2024). Potential for functional divergence in ectomycorrhizal fungal communities across a precipitation gradient. ISME Communications 4(1): ycae031. https://doi.org/10.1093/ismeco/ycae031
- Ren, Youhua; Niu, Jiaojiao; Huang, Wenkun; Peng, Deliang; Xiao, Yunhua; Zhang, Xian; Liang, Yili; Liu, Xueduan; Yin, Huaqun (2016). Comparison of microbial taxonomic and functional shift pattern along contamination gradient. BMC Microbiology 16(1): 110. https://doi.org/10.1186/s12866-016-0731-6
- Santillan, Ezequiel; Constancias, Florentin; Wuertz, Stefan (2019). Press disturbance alters community structure and assembly mechanisms of bacterial taxa and functional genes in mesocosm-scale bioreactors. bioRxiv. https://doi.org/10.1101/805788
- Santillan, Ezequiel; Constancias, Florentin; Wuertz, Stefan (2020). Press disturbance alters community structure and assembly mechanisms of bacterial taxa and functional genes in mesocosm-scale bioreactors. mSystems 5(4): e00471--20. https://doi.org/10.1128/mSystems.00471-20
- Sauma-Sanchez, Tomas; Alcorta, Jaime; Tamayo-Leiva, Javier; Diez, Beatriz; Bezuidenhout, Hugo; Cowan, Don A; Ramond, Jean-Baptiste (2024). Functional redundancy buffers the effect of poly-extreme environmental conditions on southern African dryland soil microbial communities. FEMS Microbiology Ecology 100(12): fiae157. https://doi.org/10.1093/femsec/fiae157
- Shen, Congcong; Shi, Yu; Ni, Yingying; Deng, Ye; Nostrand, Joy D. Van; He, Zhili; Zhou, Jizhong; Chu, Haiyan (2016). Dramatic increases of soil microbial functional gene diversity at the treeline ecotone of Changbai Mountain. Frontiers in Microbiology 7: 1184. https://doi.org/10.3389/fmicb.2016.01184
- Soufi, Hengameh H.; Porch, Robert; Korchagina, Masha V.; Abrams, Joseph A.; Schnider, Jared S.; Carr, Ben D.; Williams, Mark A.; Louca, Stilianos (2024). Taxonomic variability and functional stability across Oregon coastal subsurface microbiomes. Communications Biology 7(1): 1663. https://doi.org/10.1038/s42003-024-07384-y
- Souza, Renata Carolini; Hungria, Mariangela; Cantao, Mauricio Egidio; Vasconcelos, Ana Tereza Ribeiro; Nogueira, Marco Antonio; Vicente, Vania Aparecida (2015). Metagenomic analysis reveals microbial functional redundancies and specificities in a soil under different tillage and crop-management regimes. Applied Soil Ecology 86: 106--112. https://doi.org/10.1016/j.apsoil.2014.10.010
- Sveen, Tord Ranheim; Viketoft, Maria; Bengtsson, Jan; Strengbom, Joachim; Lejoly, Justine; Buegger, Franz; Pritsch, Karin; Fritscher, Joachim; Hildebrand, Falk; Osburn, Ernest; Hannula, S. Emilia; Bahram, Mo (2025). Functional diversity of soil microbial communities increases with ecosystem development. Nature Communications 16(1): 10408. https://doi.org/10.1038/s41467-025-66544-8
- Swenson, Nathan G.; Anglada-Cordero, Pedro; Barone, John A. (2011). Deterministic tropical tree community turnover: evidence from patterns of functional beta diversity along an elevational gradient. Proceedings of the Royal Society B: Biological Sciences 278(1707): 877--884. https://doi.org/10.1098/rspb.2010.1369
- Talbot, Jennifer M.; Bruns, Thomas D.; Taylor, John W.; Smith, Dylan P.; Branco, Sara; Glassman, Sydney I.; Erlandson, Sonya; Vilgalys, Rytas; Liao, Hui-Ling; Smith, Matthew E.; Peay, Kabir G. (2014). Endemism and functional convergence across the North American soil mycobiome. Proceedings of the National Academy of Sciences 111(17): 6341--6346. https://doi.org/10.1073/pnas.1402584111
- Tian, Liang; Wang, Xu-Wen; Wu, Ang-Kun; Fan, Yuhang; Friedman, Jonathan; Dahlin, Amber; Waldor, Matthew K.; Weinstock, George M.; Weiss, Scott T.; Liu, Yang-Yu (2020). Deciphering functional redundancy in the human microbiome. Nature Communications 11(1): 6217. https://doi.org/10.1038/s41467-020-19940-1
- van der Loos, Luna M.; Steinhagen, Sophie; Stock, Willem; Weinberger, Florian; D'hondt, Sofie; Willems, Anne; De Clerck, Olivier (2025). Low functional change despite high taxonomic turnover characterizes the Ulva microbiome across a 2000-km salinity gradient. Science Advances 11(3): eadr6070. https://doi.org/10.1126/sciadv.adr6070
- Villeger, Sebastien; Grenouillet, Gael; Brosse, Sebastien (2013). Decomposing functional -diversity reveals that low functional -diversity is driven by low functional turnover in European fish assemblages. Global Ecology and Biogeography 22(6): 671--681. https://doi.org/10.1111/geb.12021
- Villeger, Sebastien; Grenouillet, Gael; Brosse, Sebastien (2014). Functional homogenization exceeds taxonomic homogenization among European fish assemblages. Global Ecology and Biogeography 23(12): 1450--1460. https://doi.org/10.1111/geb.12226
- Xu, Minjie; Zhu, Xunzhi; Chen, Shiping; Pang, Shuang; Liu, Wei; Gao, Lili; Yang, Wei; Li, Tingting; Zhang, Yuhan; Luo, Chun; He, Dandan; Wang, Zhiping; Fan, Yi; Han, Xingguo; Zhang, Ximei (2022). Distinctive pattern and mechanism of precipitation changes affecting soil microbial assemblages in the Eurasian steppe. iScience 25(3): 103893. https://doi.org/10.1016/j.isci.2022.103893
- Yang, Sizhong; Liebner, Susanne; Svenning, Mette Marianne; Tveit, Alexander Tsdal (2021). Decoupling of microbial community dynamics and functions in Arctic peat soil exposed to short term warming. Molecular Ecology 30(20): 5094--5104. https://doi.org/10.1111/mec.16118
- Zhang, Hongjie; Zhao, Dayong; Wu, Qinglong L.; Zeng, Jin (2025). Environment selected microbial function rather than taxonomic species in a plateau saline-alkaline wetland. Applied and Environmental Microbiology 91(7): e02206--24. https://doi.org/10.1128/aem.02206-24
- Zhang, Yuguang; Cong, Jing; Lu, Hui; Deng, Ye; Liu, Xiao; Zhou, Jizhong; Li, Diqiang (2016). Soil bacterial endemism and potential functional redundancy in natural broadleaf forest along a latitudinal gradient. Scientific Reports 6: 28819. https://doi.org/10.1038/srep28819
