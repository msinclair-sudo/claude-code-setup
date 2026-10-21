---
type: knowledge
title: Phylogenetic depth of prokaryotic traits and rank-wise environmental structuring
inputs:
  - H1-06: PhD/Proposal/Research/Results/Phylogenetic depth of prokaryotic trait and preference conservation, and how environmental structuring of community composition changes from species to phylum a literature review.md
refs: PhD/Proposal/Refs/Refs.bib
built: 2026-10-22
status: draft
tags:
  - research
  - knowledge
---
# Phylogenetic depth of prokaryotic traits and rank-wise environmental structuring

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
| H1-06 | [[Phylogenetic depth of prokaryotic trait and preference conservation, and how environmental structuring of community composition changes from species to phylum a literature review]] | yes | narrative author-year | no | no | fallback |

## Concepts

### tau-d: consenTRAIT depth of conservation (tau_D)
needs: none
- **tau-d.1** consenTRAIT's tau_D is the mean 16S rRNA distance from the root of clades in which at least 90% of members share a trait.
  conf: not stated · class: not stated · holds: the consenTRAIT method as Martiny et al. 2013 define it; a distance on a tree · src: martinyPhylogeneticConservatismFunctional2013 · trail: H1-06 §1. What is being compared · from: H1-06:B-0021
- **tau-d.2** Depth values from different trees or datasets are not commensurable.
  conf: not stated · class: not stated · holds: stated as a bound on depth estimates, citing Sun et al. 2021 · src: sunPhylogeneticDistributionPolysaccharideDegrading2021 · trail: H1-06 §5. Bounds and failure modes · from: H1-06:B-0153

### signal-statistics: phylogenetic signal statistics
needs: none
- **signal-statistics.1** Phylogenetic signal statistics (Pagel's lambda, Blomberg's K, Moran's I correlograms, D) measure how well a trait tracks the tree without giving one depth.
  conf: not stated · class: not stated · holds: as used by Ramoneda 2023, Goberna and Verdú 2016 and Morrissey 2016 · src: ramonedaBuildingGenomebasedUnderstanding2023, gobernaPredictingMicrobialTraits2016, morrisseyPhylogeneticOrganizationBacterial2016 · trail: H1-06 §1. What is being compared · from: H1-06:B-0022
- **signal-statistics.bg1** Pagel's lambda is a measure of phylogenetic correlation that normally varies between 0 (phylogenetic independence) and 1 (traits covary in direct proportion to their shared evolutionary history).
  kind: background · ref: freckletonPhylogeneticAnalysisComparative2002 · check: DOI 10.1086/343873 resolves on Crossref; stated in the abstract (lambda "introduced by Pagel (1999)")
- **signal-statistics.bg2** Blomberg's K is a descriptive statistic of the amount of phylogenetic signal in a continuous trait, comparable across traits and trees; K below one means less signal than expected from the tree under a Brownian motion model of evolution.
  kind: background · ref: blombergTestingPhylogeneticSignal2003 · check: DOI 10.1111/j.0014-3820.2003.tb00285.x resolves on Crossref; stated in the abstract (Europe PMC, PMID 12778543)

### taxonomies: taxonomies and identity thresholds used for ranks
needs: none
- **taxonomies.1** Rank-wise analyses of community composition use taxonomies, not trees, and the taxonomy differs between studies: Greengenes, SILVA or RDP, GTDB, a curated gyrB taxonomy, or no ranks at all, only sequence-identity thresholds.
  conf: not stated · class: not stated · holds: the studies the review read: Greengenes (Lu 2016); SILVA or RDP (Ramoneda 2023, Lennon 2012, Isobe 2019); GTDB (López-Mondéjar 2022, Royalty and Steen 2019, Hoffert 2026, Barnum 2024); gyrB (Mayjonade 2024); identity thresholds only (Bay 2020, Quiroga 2022, Schmidt 2014) · src: luEvaluatingCommunityenvironmentRelationships2016, ramonedaBuildingGenomebasedUnderstanding2023, lennonMappingNicheSpace2012, isobePhylogeneticConservationBacterial2019, lopezmondejarGlobalDistributionCarbohydrate2022, royaltyQuantitativelyPartitioningMicrobial2019, hoffertConstructingPeriodicTable2026, barnumPredictingMicrobialGrowth2024, mayjonadeRelativeEffectsAbiotic2024, baySoilBacterialCommunities2020, quirogaEcologicalAssemblyBacterial2022, schmidtEcologicalConsistencySSU2014 · trail: H1-06 §1. What is being compared · from: H1-06:B-0023

### preference-types: kinds of environmental preference
needs: none
- **preference-types.1** An environmental "preference" can be (a) a growth optimum measured on isolates, (b) a field optimum inferred from where an ASV is most abundant, or (c) a response to an experimental perturbation; type (c) comes from engineered systems.
  conf: not stated · class: not stated · holds: the distinction the review keeps throughout; type (c) kept separate from the others · src: none (the reviewer's synthesis) · trail: H1-06 §1. What is being compared · from: H1-06:B-0025..0027

### yardsticks: depth on trees against ranks in taxonomies
needs: tau-d, signal-statistics, taxonomies
- **yardsticks.1** The two halves of the question use different yardsticks (distances on a tree and ranks in a taxonomy), and much of the apparent disagreement in this literature comes from that.
  conf: not stated · class: not stated · holds: the depth literature (tau_D and signal statistics on trees) against the rank-wise composition literature (taxonomies) · src: none (the reviewer's synthesis) · trail: H1-06 §1. What is being compared · from: H1-06:B-0020
- **yardsticks.2** Unless stated otherwise, a depth quoted in the review is in 16S rRNA distance and cannot be converted into a rank.
  conf: not stated · class: not stated · holds: every depth the review quotes · src: none (the reviewer's statement) · trail: H1-06 §1. What is being compared · from: H1-06:B-0024
- **yardsticks.3** Rank labels differ between Greengenes, SILVA, RDP, GTDB and gyrB taxonomies, and identity thresholds are not ranks.
  conf: not stated · class: not stated · holds: stated as a bound on all rank-wise results · src: none (the reviewer's statement) · trail: H1-06 §5. Bounds and failure modes · from: H1-06:B-0154

### ph-preference: phylogenetic signal of pH preference
needs: signal-statistics, tau-d, preference-types, taxonomies
- **ph-preference.1** The strongest natural-system evidence on pH preference is Ramoneda et al. 2023: 4,568 ASVs from five datasets (795 soil and 675 freshwater samples, pH about 3 to 10), with pH preference defined as the pH of maximal field abundance, SILVA 138 taxonomy and RAxML trees of 16S.
  conf: not stated · class: meas (note: "measured, natural") · holds: natural soil and freshwater samples; pH preference as a field optimum · src: ramonedaBuildingGenomebasedUnderstanding2023 (measured, natural) · trail: H1-06 §2. Part A1 · from: H1-06:B-0031..0032
- **ph-preference.2** Phylogenetic signal in pH preference was significant in four of five datasets but weak (Pagel's lambda 0.22 to 0.78).
  conf: single (critic: C-001) · class: meas (critic: C-001) · holds: 4,568 ASVs from five soil and freshwater datasets, SILVA 138, RAxML 16S trees; natural systems · src: ramonedaBuildingGenomebasedUnderstanding2023 · trail: H1-06 §2. Part A1, §answers, §critic · from: H1-06:B-0032, H1-06:B-0033, H1-06:A-003, H1-06:C-001, H1-06:C-002, H1-06:C-021
- **ph-preference.3** Correlogram Moran's I for pH preference stayed below 0.25 at every depth, shallow ones included.
  conf: single (critic: C-001) · class: meas (critic: C-001) · holds: the same five datasets; natural systems · src: ramonedaBuildingGenomebasedUnderstanding2023 · trail: H1-06 §2. Part A1, §answers, §critic · from: H1-06:B-0034, H1-06:A-003, H1-06:C-001, H1-06:C-002, H1-06:C-021
- **ph-preference.4** ASVs within single families spanned 3.7 to 4.2 pH units: Xanthobacteraceae in soil 4.01 to 8.20 (4.19 units), Chitinophagaceae in freshwater 4.63 to 8.35 (3.72 units).
  conf: single (critic: C-001) · class: meas (critic: C-001) · holds: Ramoneda's soil and freshwater datasets; the figures are the critic's reading of the source, which corrects the review's "four or more pH units" · src: ramonedaBuildingGenomebasedUnderstanding2023 · trail: H1-06 §2. Part A1, §critic · from: H1-06:C-001, H1-06:C-002, H1-06:C-022, H1-06:C-036
- **ph-preference.5** A phylum-level tendency in pH preference seen in one dataset (acidophilic Acidobacteria in freshwater) did not recur in the others.
  conf: not stated · class: not stated · holds: Ramoneda's five datasets · src: ramonedaBuildingGenomebasedUnderstanding2023 · trail: H1-06 §2. Part A1 · from: H1-06:B-0036
- **ph-preference.6** Ramoneda et al. conclude that "phylum-level information provides relatively little insight into bacterial pH preferences".
  conf: not stated · class: not stated · holds: the authors' conclusion from their five datasets; the critic verified the quote · src: ramonedaBuildingGenomebasedUnderstanding2023 · trail: H1-06 §2. Part A1, §critic · from: H1-06:B-0037, H1-06:C-021
- **ph-preference.7** A genome-based model of pH preference, validated on an independent UK dataset, reached R2 = 0.21 (MAE 0.93 pH units).
  conf: not stated · class: not stated · holds: gene content, not phylogeny, as predictor; one independent UK validation dataset · src: ramonedaBuildingGenomebasedUnderstanding2023 · trail: H1-06 §2. Part A1, §critic · from: H1-06:B-0037, H1-06:C-021
- **ph-preference.8** Only 6 to 24% of Ramoneda's ASVs matched a GTDB genome, and about 35% of those genomes were MAGs or SAGs.
  conf: not stated · class: not stated · holds: a bound on the genome-based analysis · src: ramonedaBuildingGenomebasedUnderstanding2023 · trail: H1-06 §2. Part A1, §critic · from: H1-06:B-0038, H1-06:C-021
- **ph-preference.9** The only large natural-system test of pH preference finds weak signal and poor prediction by rank.
  conf: single (critic: C-033) · class: not stated · holds: Ramoneda et al. 2023, natural soil and freshwater datasets · src: ramonedaBuildingGenomebasedUnderstanding2023 · trail: H1-06 §2. Part A1, §critic · from: H1-06:B-0079, H1-06:C-033
- **ph-preference.10** In global topsoil (N = 217) and ocean (N = 125) 16S surveys analysed by CCA, OTU loadings on the first canonical direction, which aligns with pH in soil and with depth in the ocean, have strong phylogenetic signal (a modified tau_D and Pagel's lambda); this is a different quantity from a per-ASV pH optimum.
  conf: single (note: "SINGLE SOURCE") · class: meas (note: "measured, natural, preprint") · holds: global topsoil and ocean surveys; canonical loadings, not optima; the critic: qualitative, with no number quoted, since tau_D values "appear only in figures" · src: chakravertiwuerthweinPhylogeneticCoherenceMicrobiome2026 (measured, natural, preprint, SINGLE SOURCE) · trail: H1-06 §2. Part A1, §answers, §critic · from: H1-06:B-0039..0041, H1-06:A-003, H1-06:C-030
- **ph-preference.11** In the same CCA, secondary canonical directions had weak or no phylogenetic signal.
  conf: not stated · class: not stated · holds: global topsoil and ocean 16S surveys · src: chakravertiwuerthweinPhylogeneticCoherenceMicrobiome2026 · trail: H1-06 §2. Part A1 · from: H1-06:B-0040, H1-06:B-0042
- **ph-preference.12** In Chakraverti-Wuerthwein et al., numeric tau_D values appear only in figures, and the permutation null shuffles sample labels rather than preserving group structure.
  conf: not stated · class: not stated · holds: the preprint's reporting and null design · src: chakravertiwuerthweinPhylogeneticCoherenceMicrobiome2026 · trail: H1-06 §2. Part A1, §critic · from: H1-06:B-0043, H1-06:C-030
- **ph-preference.13** A canonical loading is not a per-ASV optimum, so the Ramoneda and Chakraverti-Wuerthwein results measure different quantities.
  conf: not stated · class: not stated · holds: the two pH studies · src: none (the reviewer's statement) · trail: H1-06 §2. Part A1 · from: H1-06:B-0044
- **ph-preference.14** The two pH results are not in direct contradiction, but together they show that whether "pH preference" looks phylogenetically structured depends on how the preference is operationalised.
  conf: not stated · class: reading (note: "Reviewer's reading") · holds: built from two sources, one a preprint (the critic) · src: ramonedaBuildingGenomebasedUnderstanding2023, chakravertiwuerthweinPhylogeneticCoherenceMicrobiome2026 · trail: H1-06 §2. Part A1, §critic · from: H1-06:B-0045, H1-06:C-056

### moisture-preference: rank-wise structure of the moisture optimum
needs: preference-types, taxonomies
- **moisture-preference.1** In 23 bacterial and 22 fungal soil isolates respired across a manipulated water-potential gradient, phylum level held 52% of the variance in optimum water potential and 58% in niche breadth.
  conf: single (note: "SINGLE SOURCE") · class: meas (note: "measured, engineered") · holds: lab isolates (engineered); niche parameters partitioned across seven RDP ranks against permutation nulls · src: lennonMappingNicheSpace2012 (measured, engineered) · trail: H1-06 §2. Part A1, §answers · from: H1-06:B-0046..0047, H1-06:B-0050, H1-06:A-004
- **moisture-preference.2** In the same isolates, strain level held 21 to 29% of the variance in moisture niche parameters against 58 to 65% expected by chance.
  conf: not stated · class: not stated · holds: 23 bacterial and 22 fungal soil isolates, seven RDP ranks, permutation nulls · src: lennonMappingNicheSpace2012 · trail: H1-06 §2. Part A1 · from: H1-06:B-0046, H1-06:B-0047
- **moisture-preference.3** Lennon et al. themselves caution that their isolate numbers are small (5 bacterial phyla, 19 genera).
  conf: not stated · class: not stated · holds: the bacterial isolates of Lennon 2012 · src: lennonMappingNicheSpace2012 · trail: H1-06 §2. Part A1 · from: H1-06:B-0048
- **moisture-preference.4** Lennon et al. 2012 is the only direct rank-resolved measurement of a moisture optimum the review found.
  conf: single (note: "SINGLE SOURCE") · class: search (note: "the only direct rank-resolved measurement of a moisture optimum found") · holds: the search routes in the note's provenance · src: lennonMappingNicheSpace2012 · trail: H1-06 §2. Part A1 · from: H1-06:B-0049, H1-06:B-0050

### salinity-preference: phylogenetic clustering of salinity preference
needs: preference-types, taxonomies
- **salinity-preference.1** In a reciprocal transplant between tidal freshwater and brackish marsh soils, salinity-preferring phylotypes were phylogenetically clustered both tree-wide and near the tips: freshwater-preferring SES-PD -3.5, NTI 4.3; saltwater-preferring SES-PD -5.4, NTI 5.2 (p < 0.01).
  conf: single (note: "SINGLE SOURCE") · class: meas (note: "measured, engineered") · holds: reciprocal transplant (engineered), Greengenes 97% OTUs, n = 5 per treatment · src: morrisseyEvolutionaryHistoryInfluences2015 (measured, engineered, SINGLE SOURCE) · trail: H1-06 §2. Part A1, §answers · from: H1-06:B-0051..0053, H1-06:A-004
- **salinity-preference.2** At class level, Betaproteobacteria were enriched among freshwater-preferring phylotypes and Alpha- and Gammaproteobacteria among saltwater-preferring ones.
  conf: not stated · class: not stated · holds: the same reciprocal transplant · src: morrisseyEvolutionaryHistoryInfluences2015 · trail: H1-06 §2. Part A1 · from: H1-06:B-0054
- **salinity-preference.3** Morrissey and Franklin reported no depth statistic for salinity preference.
  conf: not stated · class: not stated · holds: the same reciprocal transplant · src: morrisseyEvolutionaryHistoryInfluences2015 · trail: H1-06 §2. Part A1 · from: H1-06:B-0055

### temperature-preference: phylogenetic signal of optimal growth temperature
needs: signal-statistics, preference-types
- **temperature-preference.1** Within the phylum Thermotogota, optimal growth temperature has strong phylogenetic signal (Pagel's lambda 0.93), yet ancestral reconstruction places several secondary shifts to mesophily and hyperthermophily.
  conf: not stated · class: deriv (critic: C-004) · holds: 64 Thermotogota genomes; within one phylum · src: farrellBacterialGrowthTemperature2024 · trail: H1-06 §2. Part A1, §answers, §critic · from: H1-06:B-0056, H1-06:A-005, H1-06:C-004
- **temperature-preference.2** Most of the 68 genes associated with optimal growth temperature in Thermotogota have histories of horizontal transfer.
  conf: single (note: "SINGLE SOURCE") · class: deriv (note: "inferred") · holds: 64 Thermotogota genomes · src: farrellBacterialGrowthTemperature2024 (inferred, SINGLE SOURCE) · trail: H1-06 §2. Part A1, §answers · from: H1-06:B-0056, H1-06:B-0057, H1-06:A-005
- **temperature-preference.3** Strong phylogenetic signal in growth temperature within a phylum coexists with repeated shifts.
  conf: not stated · class: not stated · holds: Thermotogota only · src: farrellBacterialGrowthTemperature2024 · trail: H1-06 §2. Part A1 · from: H1-06:B-0056, H1-06:B-0058

### trait-compilations: trait compilations and genome-based predictions of optima
needs: signal-statistics, preference-types
- **trait-compilations.1** Across 990 microbial traits collated on a SILVA r119 tree, binary, mostly gene-presence, traits had mean -D+1 = 0.93 (98% significant).
  conf: not stated · class: deriv/model (note: "compiled and modelled") · holds: Goberna and Verdú's compilation · src: gobernaPredictingMicrobialTraits2016 (compiled and modelled) · trail: H1-06 §2. Part A1, §critic · from: H1-06:B-0059, H1-06:B-0060, H1-06:B-0064, H1-06:C-029 · limit: access (note: "I could not re-open it because the publisher returned a bot challenge, so it carries no weight on its own")
- **trait-compilations.2** In the same compilation, continuous traits had mean K = 0.16 (74% significant).
  conf: not stated · class: deriv/model (note: "compiled and modelled") · holds: 990 traits, SILVA r119 tree · src: gobernaPredictingMicrobialTraits2016 · trail: H1-06 §2. Part A1, §critic · from: H1-06:B-0059, H1-06:B-0061, H1-06:B-0064, H1-06:C-029 · limit: access (note: "I could not re-open it because the publisher returned a bot challenge, so it carries no weight on its own")
- **trait-compilations.3** Goberna and Verdú 2016 is internally inconsistent on environmental optima: it lists optimal pH and temperature and moisture niche breadth among "the most conserved continuous traits", and elsewhere places optimal pH, salt tolerance and moisture niche breadth among traits with "moderate signals".
  conf: not stated · class: not stated · holds: one search agent's full reading of the paper · src: gobernaPredictingMicrobialTraits2016 · trail: H1-06 §2. Part A1, §critic · from: H1-06:B-0062, H1-06:B-0064, H1-06:C-029 · limit: access (note: "I could not re-open it because the publisher returned a bot challenge, so it carries no weight on its own")
- **trait-compilations.4** Only 9.9% of continuous and 8.6% of binary traits met Goberna and Verdú's threshold for accurate phylogenetic prediction.
  conf: not stated · class: not stated · holds: 990 traits, SILVA r119 tree · src: gobernaPredictingMicrobialTraits2016 · trail: H1-06 §2. Part A1, §critic · from: H1-06:B-0059, H1-06:B-0063, H1-06:B-0064, H1-06:C-029 · limit: access (note: "I could not re-open it because the publisher returned a bot challenge, so it carries no weight on its own")
- **trait-compilations.5** Growth optima predicted from amino-acid composition for 15,596 BacDive organisms reached, under family-level holdout, R2 0.73 for temperature, 0.81 for salinity and 0.48 for pH, with 92% balanced accuracy for oxygen tolerance.
  conf: not stated · class: model (note: "modelled, preprint") · holds: BacDive organisms, GTDB r214; family-level holdout · src: barnumPredictingMicrobialGrowth2024 (modelled, preprint) · trail: H1-06 §2. Part A1 · from: H1-06:B-0065, H1-06:B-0066
- **trait-compilations.6** A phylogeny-only comparison model failed at higher-rank holdouts except for oxygen tolerance, which stayed moderately accurate up to order and class.
  conf: not stated · class: not stated · holds: Barnum et al.'s BacDive organisms · src: barnumPredictingMicrobialGrowth2024 · trail: H1-06 §2. Part A1 · from: H1-06:B-0065, H1-06:B-0067
- **trait-compilations.7** Among six genome-inferred traits in 50,745 GTDB genomes, oxygen tolerance had much of its variance at deep nodes, often near phylum, but was "not universally conserved at the phylum level".
  conf: single (note: "SINGLE SOURCE for this method") · class: deriv (note: "inferred") · holds: GTDB genomes; traits inferred from genomes · src: hoffertConstructingPeriodicTable2026 (inferred, SINGLE SOURCE for this method) · trail: H1-06 §2. Part A1 · from: H1-06:B-0068

### perturbation-response: phylogenetic depth of responses to perturbations
needs: tau-d, signal-statistics, preference-types, taxonomies
- **perturbation-response.1** Bacterial responses to N addition across 13 field experiments on five continents were conserved at tau_D 0.016 to 0.020 per location (0.017 merged).
  conf: not stated · class: not stated · holds: N-addition field experiments (perturbation responses, kept separate as engineered); SILVA via RDP; the critic verified the values · src: isobePhylogeneticConservationBacterial2019 · trail: H1-06 §2. Part A1, §critic · from: H1-06:B-0069, H1-06:C-023
- **perturbation-response.2** Isobe et al. 2019 equate tau_D 0.016 to 0.020 to roughly genus (SILVA via RDP).
  conf: not stated · class: not stated · holds: the authors' equation; the critic: the review's own Section 1 says a 16S depth "cannot be converted into a rank" · src: isobePhylogeneticConservationBacterial2019 · trail: H1-06 §2. Part A1, §critic · from: H1-06:B-0069, H1-06:C-023, H1-06:C-054
- **perturbation-response.3** A correlogram on the same N-addition data detected response similarity out to 22% 16S divergence, which the authors note is a less conservative depth metric.
  conf: not stated · class: not stated · holds: the 13 N-addition experiments · src: isobePhylogeneticConservationBacterial2019 · trail: H1-06 §2. Part A1, §critic · from: H1-06:B-0070, H1-06:C-023
- **perturbation-response.4** In the N-addition data, Gammaproteobacteria as a class had no consistent response while one genus within it responded positively, and an order and a family within it responded in opposite directions.
  conf: not stated · class: not stated · holds: the 13 N-addition experiments; the critic names the genus Aquicela and verified the example · src: isobePhylogeneticConservationBacterial2019 · trail: H1-06 §2. Part A1, §critic · from: H1-06:B-0073, H1-06:B-0074, H1-06:C-023
- **perturbation-response.5** The same N-addition study also reports consistent phylum- and class-level responses: phylum Actinobacteria positive, classes Betaproteobacteria and Deltaproteobacteria negative.
  conf: not stated · class: not stated · holds: the 13 N-addition experiments; reported by the critic, left out of the review · src: isobePhylogeneticConservationBacterial2019 · trail: H1-06 §critic · from: H1-06:C-024, H1-06:C-031
- **perturbation-response.6** Warming, drought, elevated CO2, P addition and liming gave tau_D 0.016 to 0.024, with little difference among perturbations.
  conf: not stated · class: not stated · holds: soil perturbation experiments · src: isobePhylogeneticConservationSoil2020 · trail: H1-06 §2. Part A1 · from: H1-06:B-0071
- **perturbation-response.7** Clades responding to one perturbation rarely responded to another.
  conf: not stated · class: not stated · holds: warming, drought, elevated CO2, P addition and liming · src: isobePhylogeneticConservationSoil2020 · trail: H1-06 §2. Part A1 · from: H1-06:B-0071
- **perturbation-response.8** In leaf litter, only positive bacterial responses were significantly conserved; negative responses were not (drought decrease P = 0.541; N decrease P = 0.763).
  conf: not stated · class: not stated · holds: leaf litter, drought and N perturbations · src: amendMicrobialResponseSimulated2015 · trail: H1-06 §2. Part A1, §5. Bounds and failure modes · from: H1-06:B-0072, H1-06:B-0160
- **perturbation-response.9** In situ growth measured by qSIP in one forest soil had Blomberg's K 0.38 to 0.54 and Pagel's lambda 0.96 to 0.98.
  conf: not stated · class: not stated · holds: one forest soil · src: morrisseyPhylogeneticOrganizationBacterial2016 · trail: H1-06 §2. Part A1 · from: H1-06:B-0075
- **perturbation-response.10** Within a single 16S OTU (Curtobacterium, minimum 83.2% ANI), the drought response appeared conserved across clades while carbohydrate-use degree and degradation temperature preference varied among clades.
  conf: single (note: "SINGLE SOURCE") · class: meas (note: "measured, natural") · holds: one 16S OTU of Curtobacterium · src: chaseMicrodiversityAbundantTerrestrial2017 (measured, natural, SINGLE SOURCE) · trail: H1-06 §2. Part A1 · from: H1-06:B-0076

### a1-environmental-preferences: depth of conservation of environmental preferences overall
needs: ph-preference, moisture-preference, salinity-preference, temperature-preference, trait-compilations, perturbation-response, tau-d
- **a1-environmental-preferences.1** No consenTRAIT depth (tau_D) for any environmental optimum (pH, temperature or moisture) was found.
  conf: not stated · class: search (note: "No consenTRAIT depth for any environmental optimum was found") · holds: the routes the provenance names: Europe PMC REST keyword, DOI and title search plus fullTextXML; the 'consenTRAIT AND OPEN_ACCESS' query (23 hits screened); citing papers of Lu et al. 2016; PMC HTML; publisher pages; bioRxiv; the Lennon lab PDF archive; WebSearch on several phrasings · src: none (a search result) · trail: H1-06 §2. Part A1, §answers, §Provenance · from: H1-06:B-0028, H1-06:A-002, H1-06:B-0008, H1-06:B-0009, H1-06:C-002
- **a1-environmental-preferences.2** The frequently repeated statement that pH optimum, soil moisture optimum and habitat association sit in deep clades appears in Martiny et al. 2013 as a discussion claim resting on other studies; that paper does not measure any of these.
  conf: not stated · class: assert (note: "asserted, SECONDARY") · holds: Martiny et al. 2013's discussion · src: martinyPhylogeneticConservatismFunctional2013 (asserted, SECONDARY) · trail: H1-06 §2. Part A1 · from: H1-06:B-0028, H1-06:B-0029
- **a1-environmental-preferences.3** The primary studies Martiny et al. 2013 cite for deep-clade environmental preferences were either not obtained (Placella et al. 2012, Philippot et al. 2010) or were read and give a more mixed picture (Lennon et al. 2012).
  conf: not stated · class: not stated · holds: the primary studies behind the deep-clade statement · src: placellaRainfallinducedCarbonDioxide2012 (not obtained), philippotEcologicalCoherenceHigh2010 (not obtained), lennonMappingNicheSpace2012 · trail: H1-06 §2. Part A1 · from: H1-06:B-0030
- **a1-environmental-preferences.4** Among full-text sources, the claim that environmental optima are conserved at deep ranks rests on an engineered study of 23 bacterial isolates for moisture and on an asserted secondary statement.
  conf: not stated · class: not stated · holds: Lennon 2012 (engineered isolates) and Martiny 2013 (asserted, secondary) · src: lennonMappingNicheSpace2012, martinyPhylogeneticConservatismFunctional2013 · trail: H1-06 §2. Part A1 · from: H1-06:B-0078
- **a1-environmental-preferences.5** The evidence on environmental preferences does not converge on a single depth.
  conf: not stated · class: not stated · holds: all A1 evidence, natural, engineered and modelled together; the critic: the 'inconsistent' label only emerges when natural evidence is set beside engineered results or a preprint that measures a different quantity · src: none (the reviewer's synthesis) · trail: H1-06 §2. Part A1, §critic · from: H1-06:B-0077, H1-06:C-005
- **a1-environmental-preferences.6** In natural systems, depth of conservation of environmental preferences has been measured for pH only, in a single source (Ramoneda et al. 2023): signal is significant in 4 of 5 datasets but weak (Pagel's lambda 0.22 to 0.78, Moran's I < 0.25 at all depths), there is no consenTRAIT-style depth, and families span 3.7 to 4.2 pH units.
  conf: single (critic: C-001) · class: meas (critic: C-001) · holds: natural soil and freshwater datasets; the natural evidence is one large study (weak signal) plus a preprint on a non-comparable quantity (canonical loadings) · src: ramonedaBuildingGenomebasedUnderstanding2023 · trail: H1-06 §critic, §answers · from: H1-06:C-001, H1-06:C-002, H1-06:C-013, H1-06:C-015, H1-06:A-003 · rating: "measured, natural, single source, weak signal, no depth"
- **a1-environmental-preferences.7** Moisture and salinity preferences have not been measured in natural systems: the rank-resolved results are engineered (Lennon 2012, lab isolates, n = 23 bacteria; Morrissey and Franklin 2015, reciprocal transplant), and the deep-rank moisture result has no natural-system rank-wise counterpart among the sources read.
  conf: not stated · class: search (note: "has no natural-system rank-wise counterpart among the sources read") · holds: the sources the review read; the two coarse-rank optimum results are engineered · src: lennonMappingNicheSpace2012, morrisseyEvolutionaryHistoryInfluences2015 · trail: H1-06 §critic, §answers, §4. Part B, §5. Bounds and failure modes · from: H1-06:C-003, H1-06:C-015, H1-06:A-004, H1-06:B-0152, H1-06:B-0164 · rating: "not measured in natural systems"
- **a1-environmental-preferences.8** Natural evidence for environmental optima is thin.
  conf: not stated · class: not stated · holds: A1 as a whole · src: none (the reviewer's synthesis) · trail: H1-06 §5. Bounds and failure modes · from: H1-06:B-0163
- **a1-environmental-preferences.9** Without Ramoneda et al. 2023, the only natural-system depth evidence left for any environmental preference is a single preprint, and the A1 verdict would move towards 'not measured in this setting' for natural systems.
  conf: not stated · class: not stated · holds: the sensitivity of the A1 verdict to one source; the remaining preprint is Chakraverti-Wuerthwein 2026 · src: ramonedaBuildingGenomebasedUnderstanding2023, chakravertiwuerthweinPhylogeneticCoherenceMicrobiome2026 · trail: H1-06 §answers, §6. Verdicts · from: H1-06:A-007, H1-06:A-008, H1-06:A-024

### metabolic-depth: depth of conservation of genome-encoded metabolic traits
needs: tau-d, taxonomies
- **metabolic-depth.1** Depth results for metabolic traits are inferred from genome annotation, not measured phenotypically, except for the Biolog substrates in Martiny 2013.
  conf: not stated · class: deriv (note: "inferred from genomes") · holds: all A2 sources · src: martinyPhylogeneticConservatismFunctional2013 · trail: H1-06 §3. Part A2, §answers · from: H1-06:B-0081, H1-06:A-009
- **metabolic-depth.2** On 2,229 SEED genomes (26 phyla, 16S trees), 93% of 89 traits were non-randomly distributed.
  conf: not stated · class: not stated · holds: SEED genomes, 16S trees · src: martinyPhylogeneticConservatismFunctional2013 · trail: H1-06 §3. Part A2, §Provenance, §critic · from: H1-06:B-0082, H1-06:B-0011, H1-06:C-028 · limit: access (note: "I could not re-open Martiny 2013 (Europe PMC fullTextXML empty)")
- **metabolic-depth.3** Oxygenic photosynthesis had a median tau_D of about 0.10 to 0.11 (one clade).
  conf: not stated · class: not stated · holds: 2,229 SEED genomes, 16S trees; the value rests on search-agent transcription · src: martinyPhylogeneticConservatismFunctional2013 · trail: H1-06 §3. Part A2, §Provenance, §critic · from: H1-06:B-0082, H1-06:B-0083, H1-06:B-0011, H1-06:C-028 · limit: access (critic: C-028)
- **metabolic-depth.4** Sulfate reduction had a tau_D of 0.039 (20 clusters).
  conf: not stated · class: not stated · holds: 2,229 SEED genomes, 16S trees; the value rests on search-agent transcription · src: martinyPhylogeneticConservatismFunctional2013 · trail: H1-06 §3. Part A2, §Provenance, §critic · from: H1-06:B-0082, H1-06:B-0084, H1-06:B-0011, H1-06:C-028 · limit: access (critic: C-028)
- **metabolic-depth.5** Nitrogen fixation had a tau_D of about 0.018 (54 clusters).
  conf: not stated · class: not stated · holds: 2,229 SEED genomes, 16S trees; the value rests on search-agent transcription · src: martinyPhylogeneticConservatismFunctional2013 · trail: H1-06 §3. Part A2, §Provenance, §critic · from: H1-06:B-0082, H1-06:B-0084, H1-06:B-0011, H1-06:C-028 · limit: access (critic: C-028)
- **metabolic-depth.6** Growth on each of 70 carbon substrates (Biolog phenotypes, 738 strains) had a tau_D below 0.011.
  conf: not stated · class: not stated · holds: 738 strains with Biolog phenotypes; the value rests on search-agent transcription · src: martinyPhylogeneticConservatismFunctional2013 · trail: H1-06 §3. Part A2, §Provenance, §critic · from: H1-06:B-0085, H1-06:B-0011, H1-06:C-028 · limit: access (critic: C-028)
- **metabolic-depth.7** Martiny et al. report that traits encoded by many genes sit deeper, with aerobic methane oxidation as a stated exception.
  conf: not stated · class: not stated · holds: the 89 traits on SEED genomes · src: martinyPhylogeneticConservatismFunctional2013 · trail: H1-06 §3. Part A2, §Provenance · from: H1-06:B-0082, H1-06:B-0086, H1-06:B-0011 · limit: access (note: "I could not re-open Martiny 2013 (Europe PMC fullTextXML empty)")
- **metabolic-depth.8** Single enzymes are shallow: alkaline phosphatase, chitinase and beta-N-acetylglucosaminidase had tau_D 0.0098, 0.0080 and 0.0097, about 98% 16S identity.
  conf: not stated · class: not stated · holds: 3,058 genomes · src: zimmermanMicrodiversityExtracellularEnzyme2013 · trail: H1-06 §3. Part A2 · from: H1-06:B-0089, H1-06:B-0090
- **metabolic-depth.9** On 5,123 genomes, cellulase had a tau_D of 0.013 and beta-glucosidase 0.034.
  conf: not stated · class: not stated · holds: 5,123 genomes · src: berlemontPhylogeneticDistributionPotential2013 · trail: H1-06 §3. Part A2 · from: H1-06:B-0091
- **metabolic-depth.10** In 9,143 high-quality MAGs from the GEM catalogue, CAZyme traits had significant phylogenetic signal in most phyla, and depth varied by phylum, with conserved-clade 16S divergence of 3 to 10% in Verrucomicrobiota and 0.1 to 0.5% in Firmicutes_A.
  conf: not stated · class: not stated · holds: GEM catalogue MAGs, GTDB phyla · src: lopezmondejarGlobalDistributionCarbohydrate2022 · trail: H1-06 §3. Part A2 · from: H1-06:B-0092, H1-06:B-0093
- **metabolic-depth.11** Beta-glucanases had significant signal in 73% of phyla tested, against 25% for alpha-glucanases.
  conf: single (note: "SINGLE SOURCE") · class: not stated · holds: 9,143 GEM catalogue MAGs, GTDB phyla; natural · src: lopezmondejarGlobalDistributionCarbohydrate2022 (natural, SINGLE SOURCE) · trail: H1-06 §3. Part A2 · from: H1-06:B-0092, H1-06:B-0094
- **metabolic-depth.12** The relative ordering of metabolic-trait depth replicates across independent datasets on 16S trees: complex multi-gene pathways are deep (oxygenic photosynthesis about 0.10 to 0.11 16S distance; sulfate reduction 0.039), nitrogen fixation is intermediate (about 0.018), and single enzymes and substrate use are shallow (about 0.008 to 0.034).
  conf: repl (note: "replicates across independent datasets") · class: deriv (note: "inferred from genomes") · holds: 16S trees; the range 0.008 to 0.034 is the note's, spanning Martiny 2013, Zimmerman 2013 and Berlemont 2013; the critic: the relative ordering is consistent, but the load-bearing Martiny 2013 values were not re-checked by the synthesiser · src: martinyPhylogeneticConservatismFunctional2013, zimmermanMicrodiversityExtracellularEnzyme2013, berlemontPhylogeneticDistributionPotential2013, sunPhylogeneticDistributionPolysaccharideDegrading2021, lopezmondejarGlobalDistributionCarbohydrate2022 · trail: H1-06 §3. Part A2, §answers, §critic · from: H1-06:B-0114, H1-06:A-009, H1-06:A-010, H1-06:A-026, H1-06:C-006, H1-06:C-007, H1-06:C-028 · limit: access (critic: C-028)

### depth-dependence: dependence of depth estimates on dataset and tree
needs: tau-d, metabolic-depth
- **depth-dependence.1** In 2,730 marine genomes, chitinase tau_D was 0.0281 on a 16S tree and 0.0444 on a core-gene tree, three to five times Zimmerman's 0.008.
  conf: not stated · class: not stated · holds: marine genomes (Sun 2021) against Zimmerman's 3,058 genomes · src: sunPhylogeneticDistributionPolysaccharideDegrading2021, zimmermanMicrodiversityExtracellularEnzyme2013 · trail: H1-06 §3. Part A2, §answers · from: H1-06:B-0095, H1-06:A-011
- **depth-dependence.2** Sun et al. attribute the difference from Zimmerman to a denser sample of trait-positive genomes and state that tau_D values from different trees are not comparable.
  conf: not stated · class: not stated · holds: the authors' attribution · src: sunPhylogeneticDistributionPolysaccharideDegrading2021 · trail: H1-06 §3. Part A2 · from: H1-06:B-0096
- **depth-dependence.3** Depending on the enzyme, 13.5 to 100% of trait-positive genomes were singletons; singleton clusters are common.
  conf: not stated · class: not stated · holds: Sun's 2,730 marine genomes · src: sunPhylogeneticDistributionPolysaccharideDegrading2021 · trail: H1-06 §3. Part A2, §5. Bounds and failure modes · from: H1-06:B-0095, H1-06:B-0097, H1-06:B-0156
- **depth-dependence.4** Martiny et al. call their estimates "an upper bound for many functions" because many trait carriers sit in clusters of one; tau_D is an upper bound under undersampling.
  conf: not stated · class: not stated · holds: the original authors' statement about their own depths · src: martinyPhylogeneticConservatismFunctional2013 · trail: H1-06 §3. Part A2, §5. Bounds and failure modes, §answers · from: H1-06:B-0098, H1-06:B-0155, H1-06:A-013
- **depth-dependence.5** On gene-content coherence, 44 coherent nodes appeared at 16S distances of 0.03 to 0.25 on a 16S tree but only five deep coherent subtrees on a GTDB 120-protein tree.
  conf: not stated · class: not stated · holds: a 16S tree against a GTDB 120-protein tree · src: parrasmoltoAssessmentPhylofunctionalCoherence2021 · trail: H1-06 §3. Part A2, §answers · from: H1-06:B-0099, H1-06:A-012
- **depth-dependence.6** Class Actinobacteria was functionally coherent while the shallower family Enterobacteriaceae was not.
  conf: single (note: "SINGLE SOURCE") · class: not stated · holds: Parras-Moltó's gene-content coherence analysis · src: parrasmoltoAssessmentPhylofunctionalCoherence2021 · trail: H1-06 §3. Part A2 · from: H1-06:B-0100
- **depth-dependence.7** Absolute depths for the same trait do not replicate: they move with genome sampling density and tree choice, and their own authors describe them as upper bounds.
  conf: not stated · class: not stated · holds: Sun 2021 and Parras-Moltó 2021 for sampling and tree; Martiny 2013 for the upper bound · src: sunPhylogeneticDistributionPolysaccharideDegrading2021, parrasmoltoAssessmentPhylofunctionalCoherence2021, martinyPhylogeneticConservatismFunctional2013 · trail: H1-06 §3. Part A2, §critic · from: H1-06:B-0115, H1-06:C-006

### rank-partitioning: partitioning of genomic traits among ranks
needs: taxonomies
- **rank-partitioning.1** With GTDB ranks, 13,735 lineages and 25 COG categories normalised for genome size, ranks together explained 41.4% of variance: domain 3.2%, phylum 14.6%, class 4.1%, order 9.2%, family 4.8%, genus 5.5%.
  conf: single (note: "SINGLE SOURCE") · class: not stated · holds: GTDB ranks, COG categories · src: royaltyQuantitativelyPartitioningMicrobial2019 (SINGLE SOURCE) · trail: H1-06 §3. Part A2, §answers, §critic · from: H1-06:B-0101, H1-06:A-012, H1-06:C-035
- **rank-partitioning.2** The contribution of ranks to genomic trait variance is non-monotonic across ranks.
  conf: single (critic: C-035) · class: not stated · holds: Royalty and Steen's GTDB partition only · src: royaltyQuantitativelyPartitioningMicrobial2019 · trail: H1-06 §3. Part A2, §critic · from: H1-06:B-0102, H1-06:C-035
- **rank-partitioning.3** Apparent within-phylum variability rose with the number of lineages sampled and levelled off after about 100 genomes, so undersampled phyla look falsely uniform.
  conf: not stated · class: not stated · holds: Royalty and Steen's GTDB lineages · src: royaltyQuantitativelyPartitioningMicrobial2019 · trail: H1-06 §3. Part A2 · from: H1-06:B-0103
- **rank-partitioning.4** Across 50,745 GTDB genomes, autotrophy and maximum growth rate had weaker phylogenetic signal than oxygen tolerance and GC content, and at least 25% of variance in four traits fell at a single split.
  conf: not stated · class: not stated · holds: GTDB genomes, six genome-inferred traits · src: hoffertConstructingPeriodicTable2026 · trail: H1-06 §3. Part A2 · from: H1-06:B-0104

### a2-metabolic-traits: depth of conservation of metabolic traits overall
needs: metabolic-depth, depth-dependence, rank-partitioning
- **a2-metabolic-traits.1** Depth of conservation of genome-encoded metabolic traits is measured (inferred from genomes) and inconsistent in absolute depth between datasets and trees, while the relative ordering is consistent.
  conf: not stated · class: deriv (critic: C-006) · holds: genome annotation on 16S and GTDB trees; the critic: supported, but the load-bearing Martiny 2013 values were not re-checked by the synthesiser, which records an unresolved transcription discrepancy · src: martinyPhylogeneticConservatismFunctional2013, sunPhylogeneticDistributionPolysaccharideDegrading2021, parrasmoltoAssessmentPhylofunctionalCoherence2021 · trail: H1-06 §critic, §answers, §6. Verdicts · from: H1-06:C-006, H1-06:C-007, H1-06:C-011, H1-06:C-028, H1-06:A-025, H1-06:A-026 · rating: "measured and inconsistent between methods, taxonomies or datasets (inferred)" · limit: access (critic: C-028)
- **a2-metabolic-traits.2** The 'inconsistent' label for metabolic traits rests mainly on Sun et al. 2021 (dataset and tree dependence of the same trait) together with Parras-Moltó et al. 2021; without Sun, 'measured, with depths, methods and taxonomy stated' would be defensible for the ordering.
  conf: not stated · class: not stated · holds: the sensitivity of the A2 verdict to one source · src: sunPhylogeneticDistributionPolysaccharideDegrading2021, parrasmoltoAssessmentPhylofunctionalCoherence2021 · trail: H1-06 §answers, §6. Verdicts · from: H1-06:A-014, H1-06:A-015, H1-06:A-027

### genome-incompleteness: effect of genome incompleteness on detected function and conservation estimates
needs: tau-d, signal-statistics
- **genome-incompleteness.1** No study was found that directly tests how genome incompleteness biases tau_D or phylogenetic signal statistics; its effect on depth estimates themselves has not been measured in any source read.
  conf: not stated · class: search (note: "No study found tests directly how incompleteness biases tau_D or signal statistics") · holds: the provenance lists routes behind every 'not found'; the critic: the routes behind this 'not found' are not named in the body · src: none (a search result) · trail: H1-06 §3. Part A2, §5. Bounds and failure modes, §Provenance, §critic · from: H1-06:B-0105, H1-06:B-0158, H1-06:B-0009, H1-06:C-051
- **genome-incompleteness.2** The evidence on incompleteness is indirect but consistent in direction.
  conf: not stated · class: not stated · holds: Eisenhofer 2023, Li and Yin 2022, Albright and Louca 2023; the critic: each quantitative element is SINGLE SOURCE · src: eisenhoferImpactMicrobialGenome2023, liCriticalAssessmentPangenomic2022, albrightTraitBiasesMicrobial2023 · trail: H1-06 §3. Part A2, §critic · from: H1-06:B-0106, H1-06:C-034
- **genome-incompleteness.3** Going from 70% to 100% genome completeness raised KEGG module fullness by 15 ± 10%.
  conf: single (note: "SINGLE SOURCE") · class: model (note: "modelled on subsampled complete genomes") · holds: subsampled complete genomes · src: eisenhoferImpactMicrobialGenome2023 (modelled on subsampled complete genomes, SINGLE SOURCE) · trail: H1-06 §3. Part A2 · from: H1-06:B-0107
- **genome-incompleteness.4** The completeness bias in module fullness was positive for 94% of 195 modules, persisted above 90% completeness, and was largest in Proteobacteria and in modules with few steps.
  conf: not stated · class: not stated · holds: Eisenhofer's subsampled complete genomes · src: eisenhoferImpactMicrobialGenome2023 · trail: H1-06 §3. Part A2 · from: H1-06:B-0107, H1-06:B-0108
- **genome-incompleteness.5** Subsampling a complete Pseudomonas aeruginosa genome to 70% moved its functional profile towards Bacillus subtilis.
  conf: not stated · class: not stated · holds: one subsampled genome · src: eisenhoferImpactMicrobialGenome2023 · trail: H1-06 §3. Part A2 · from: H1-06:B-0109
- **genome-incompleteness.6** Removing 1% of sequence from each genome cut detected core gene families by more than 60% across 17 species; relaxing the core threshold to 90 to 95% eased this.
  conf: single (note: "SINGLE SOURCE") · class: model (note: "modelled") · holds: 17 species · src: liCriticalAssessmentPangenomic2022 (modelled, SINGLE SOURCE) · trail: H1-06 §3. Part A2 · from: H1-06:B-0110
- **genome-incompleteness.7** For 116,884 MAGs against RefSeq, raw gene detection rates fell below model-corrected prevalences, and most KEGG orthologs were biased between culture-heavy and MAG references.
  conf: single (critic: C-034) · class: not stated · holds: MAGs against RefSeq · src: albrightTraitBiasesMicrobial2023 · trail: H1-06 §3. Part A2, §critic · from: H1-06:B-0111, H1-06:C-034
- **genome-incompleteness.8** In three single-source studies (KEGG modules, core genes, reference bias), incompleteness lowers detected function, by an amount that depends on module and phylum; none of them measures the effect on conservation depth.
  conf: single (critic: C-034) · class: not stated · holds: Eisenhofer 2023, Li and Yin 2022, Albright and Louca 2023 · src: eisenhoferImpactMicrobialGenome2023, liCriticalAssessmentPangenomic2022, albrightTraitBiasesMicrobial2023 · trail: H1-06 §5. Bounds and failure modes, §critic · from: H1-06:B-0157, H1-06:C-034
- **genome-incompleteness.9** Consensus-threshold methods such as consenTRAIT (90% sharing) are exposed to false absences, which would fragment clades and push depth estimates shallower; no source tests this.
  conf: not stated · class: reading (note: "Reviewer's reading, not tested by any source") · holds: an untested reading · src: none (the reviewer's reading) · trail: H1-06 §3. Part A2, §critic · from: H1-06:B-0112, H1-06:C-055
- **genome-incompleteness.10** Amino-acid-based optimum predictions stayed stable down to 10% completeness for oxygen, temperature and salinity, while pH error reached 0.4 units.
  conf: not stated · class: not stated · holds: Barnum et al.'s BacDive organisms; preprint · src: barnumPredictingMicrobialGrowth2024 (preprint) · trail: H1-06 §3. Part A2 · from: H1-06:B-0113

### rankwise-structuring: environmental structuring of composition from fine to coarse ranks, with group number and size controlled
needs: taxonomies
- **rankwise-structuring.bg1** Distance-based redundancy analysis (db-RDA) runs a redundancy analysis on the principal coordinates of a distance matrix among samples (Bray-Curtis or another distance), so that the variance in multispecies composition explained by explanatory variables can be tested by permutation.
  kind: background · ref: legendreDistancebasedRedundancyAnalysis1999 · check: DOI 10.1890/0012-9615(1999)069[0001:DBRATM]2.0.CO;2 resolves on Crossref; stated in the abstract (OpenAlex)
- **rankwise-structuring.1** Across eight reanalysed datasets (four surface soils and four seawater), environment-explained variance of composition "either increased or remained constant with broadening taxonomic resolution from species to order or even phylum level".
  conf: not stated · class: meas (note: "measured, natural") · holds: closed-reference Greengenes 13_8 with copy-number correction; composition aggregated from otu97 to otu70 and from species to phylum; db-RDA adjusted R2 of Bray-Curtis composition; soils n = 40 to 580; the critic confirmed the quoted abstract sentence · src: luEvaluatingCommunityenvironmentRelationships2016 (measured, natural) · trail: H1-06 §4. Part B, §answers, §critic · from: H1-06:B-0116..0119, H1-06:A-017, H1-06:A-029, H1-06:C-009, H1-06:C-016
- **rankwise-structuring.2** In all four soils, environment-explained R2 rose up to class (otu82 to otu76) and fell at phylum.
  conf: not stated · class: not stated · holds: four surface soils, Greengenes 13_8 · src: luEvaluatingCommunityenvironmentRelationships2016 · trail: H1-06 §4. Part B, §answers, §critic · from: H1-06:B-0121, H1-06:A-018, H1-06:C-017 · limit: access (critic: C-017)
- **rankwise-structuring.3** In soils, R2 rose by at least 50% from otu97 to otu94.
  conf: not stated · class: not stated · holds: four surface soils · src: luEvaluatingCommunityenvironmentRelationships2016 · trail: H1-06 §4. Part B, §critic · from: H1-06:B-0121, H1-06:C-025, H1-06:C-026 · limit: access (critic: C-026)
- **rankwise-structuring.4** In the soils, pH was the strongest single environmental variable.
  conf: not stated · class: not stated · holds: four surface soils · src: luEvaluatingCommunityenvironmentRelationships2016 · trail: H1-06 §4. Part B · from: H1-06:B-0121
- **rankwise-structuring.5** In Tara surface and DCM seawater, environment-explained R2 peaked at intermediate ranks.
  conf: not stated · class: not stated · holds: two seawater datasets · src: luEvaluatingCommunityenvironmentRelationships2016 · trail: H1-06 §4. Part B, §answers, §critic · from: H1-06:B-0122, H1-06:A-019, H1-06:C-025, H1-06:C-026 · limit: access (critic: C-026)
- **rankwise-structuring.6** In the English Channel time series, environment-explained R2 was flat from species to order, then dropped at class and phylum.
  conf: not stated · class: not stated · holds: one seawater time series · src: luEvaluatingCommunityenvironmentRelationships2016 · trail: H1-06 §4. Part B, §answers, §critic · from: H1-06:B-0123, H1-06:A-019, H1-06:C-025, H1-06:C-026 · limit: access (critic: C-026)
- **rankwise-structuring.7** On the East China Sea shelf, environment-explained R2 rose continuously to phylum.
  conf: not stated · class: not stated · holds: one seawater dataset · src: luEvaluatingCommunityenvironmentRelationships2016 · trail: H1-06 §4. Part B, §answers, §critic · from: H1-06:B-0124, H1-06:A-019, H1-06:C-025, H1-06:C-026 · limit: access (critic: C-026)
- **rankwise-structuring.8** Lu et al. handled group number and group size with a null that "shuffled linkages between fine-taxa and broad-taxa level by level (remaining topology)", using 100 random linkage maps (tip-label shuffling for UniFrac).
  conf: not stated · class: not stated · holds: the null design of Lu 2016 as the search agent read it · src: luEvaluatingCommunityenvironmentRelationships2016 · trail: H1-06 §4. Part B, §critic · from: H1-06:B-0125, H1-06:C-017, H1-06:C-025 · limit: access (critic: C-017)
- **rankwise-structuring.9** Under the topology-preserving shuffle null, explained variance "remained constant or slightly decreased" with rank.
  conf: not stated · class: not stated · holds: the eight datasets of Lu 2016 · src: luEvaluatingCommunityenvironmentRelationships2016 · trail: H1-06 §4. Part B, §answers, §critic · from: H1-06:B-0126, H1-06:A-020, H1-06:C-017 · limit: access (critic: C-017)
- **rankwise-structuring.10** In soils, the observed genus-to-class R2 was significantly above the null.
  conf: not stated · class: not stated · holds: four surface soils · src: luEvaluatingCommunityenvironmentRelationships2016 · trail: H1-06 §4. Part B, §answers, §critic · from: H1-06:B-0127, H1-06:A-020, H1-06:C-017 · limit: access (critic: C-017)
- **rankwise-structuring.11** Lu et al. read the rise in explained variance with rank as phylogenetic niche conservatism.
  conf: not stated · class: not stated · holds: the authors' interpretation · src: luEvaluatingCommunityenvironmentRelationships2016 · trail: H1-06 §4. Part B · from: H1-06:B-0128
- **rankwise-structuring.12** By preserving topology, Lu's null holds the count of groups per level and the number of fine taxa per group fixed; it does not hold abundance evenness among groups fixed.
  conf: not stated · class: reading (note: "Reviewer's reading") · holds: Lu 2016's null; the critic calls the evenness caveat appropriate · src: luEvaluatingCommunityenvironmentRelationships2016 · trail: H1-06 §4. Part B, §critic · from: H1-06:B-0129, H1-06:B-0130, H1-06:C-010, H1-06:C-018
- **rankwise-structuring.13** Environmental structuring of composition from fine to coarse ranks has been measured with group number (and member count) controlled in a single source (Lu et al. 2016), conditional on that paper's null design, which the critic could not re-verify; abundance evenness among groups was not controlled.
  conf: single (critic: C-008) · class: meas (note: "measured, natural") · holds: Lu 2016's four soil and four seawater datasets; the critic confirmed only the abstract; the departure from the brief's expected 'not measured' verdict rests on one source whose control design was not independently re-verified · src: luEvaluatingCommunityenvironmentRelationships2016 (measured, natural) · trail: H1-06 §critic, §answers, §4. Part B, §5. Bounds and failure modes · from: H1-06:C-008, H1-06:C-010, H1-06:C-011, H1-06:C-060, H1-06:C-061, H1-06:A-016, H1-06:A-028, H1-06:B-0116, H1-06:B-0131, H1-06:B-0161 · rating: "measured with group number (and member count) controlled, SINGLE SOURCE" · limit: access (critic: C-008)
- **rankwise-structuring.14** Without Lu et al. 2016 the rank-wise verdict falls to 'measured without controlling group number and size'.
  conf: not stated · class: not stated · holds: the sensitivity of the B verdict to one source · src: luEvaluatingCommunityenvironmentRelationships2016 · trail: H1-06 §answers, §6. Verdicts · from: H1-06:B-0017, H1-06:A-022, H1-06:A-030

### uncontrolled-rank-studies: rank-wise structuring without control of group number and size
needs: taxonomies, rankwise-structuring
- **uncontrolled-rank-studies.1** Studies across ranks that do not control group number and size agree in part and conflict in part with the controlled study.
  conf: not stated · class: not stated · holds: Mayjonade 2024 (preprint), Bay 2020, Chakraverti-Wuerthwein 2026 (preprint), Auladell 2022 · src: mayjonadeRelativeEffectsAbiotic2024, baySoilBacterialCommunities2020, chakravertiwuerthweinPhylogeneticCoherenceMicrobiome2026, auladellSeasonalNicheDifferentiation2021 · trail: H1-06 §answers · from: H1-06:A-021
- **uncontrolled-rank-studies.2** At 160 natural sites in southwest France, habitat category explained little composition variance at any level, and it peaked at class (PERMANOVA R2: phylum 3.7%, class 6.3%, ASV 2.7%).
  conf: not stated · class: not stated · holds: natural sites, gyrB taxonomy, preprint; group numbers not controlled · src: mayjonadeRelativeEffectsAbiotic2024 (preprint) · trail: H1-06 §4. Part B, §answers · from: H1-06:B-0132, H1-06:B-0133, H1-06:A-021
- **uncontrolled-rank-studies.3** In the same sites, the share of individual groups significantly associated with soil physicochemistry fell from 59% at phylum to 30.2% at ASV, while plant-community associations rose from 19.7% to 48.7%.
  conf: not stated · class: not stated · holds: 160 natural sites, gyrB taxonomy · src: mayjonadeRelativeEffectsAbiotic2024 · trail: H1-06 §4. Part B, §answers · from: H1-06:B-0132, H1-06:B-0134, H1-06:A-021
- **uncontrolled-rank-studies.4** In Mayjonade et al., group numbers ranged from 18 phyla to 769 ASVs and were not controlled.
  conf: not stated · class: not stated · holds: 160 natural sites, gyrB taxonomy · src: mayjonadeRelativeEffectsAbiotic2024 · trail: H1-06 §4. Part B · from: H1-06:B-0135
- **uncontrolled-rank-studies.5** In the Negev, turnover was stronger at ASV resolution (an 82% drop in similarity over 160 km against 50 to 60% for clustered or filtered data).
  conf: not stated · class: not stated · holds: ASVs against 97% OTUs only, no ranks · src: baySoilBacterialCommunities2020 · trail: H1-06 §4. Part B · from: H1-06:B-0136
- **uncontrolled-rank-studies.6** In the Negev, "less variation in community composition could be explained and partitioned for the high-resolution data set" than for the filtered ones (clustered and/or rare-taxon-filtered data), and the rank order of predictors changed.
  conf: not stated · class: not stated · holds: incidence-based variation partitioning; the contrast is clustering plus filtering, not clustering alone (the critic) · src: baySoilBacterialCommunities2020 · trail: H1-06 §4. Part B, §critic · from: H1-06:B-0137, H1-06:C-019, H1-06:C-020
- **uncontrolled-rank-studies.7** In global topsoil and ocean surveys, the pH-aligned first canonical axis stayed stable when OTUs were summed to genus, family and higher, while secondary axes were incoherent across resolutions.
  conf: not stated · class: not stated · holds: preprint; the null there does not preserve group structure · src: chakravertiwuerthweinPhylogeneticCoherenceMicrobiome2026 · trail: H1-06 §4. Part B, §answers · from: H1-06:B-0139, H1-06:B-0140, H1-06:A-021
- **uncontrolled-rank-studies.8** In an 11-year coastal time series, seasonal niches were coherent for some genera and families, but classes (Alphaproteobacteria, Gammaproteobacteria, Bacteroidia) were non-seasonal when aggregated.
  conf: not stated · class: not stated · holds: a time series, not a spatial environment gradient; aggregation used random 80% ASV subsets, but group number was not equalised · src: auladellSeasonalNicheDifferentiation2021 · trail: H1-06 §4. Part B, §answers · from: H1-06:B-0141, H1-06:B-0142, H1-06:A-021
- **uncontrolled-rank-studies.9** Within at least three genera in the coastal time series, seasonal niche similarity fell with 16S divergence.
  conf: not stated · class: not stated · holds: the 11-year coastal time series · src: auladellSeasonalNicheDifferentiation2021 · trail: H1-06 §4. Part B · from: H1-06:B-0141
- **uncontrolled-rank-studies.10** Apart from the one controlled reanalysis, the rank-wise studies are uncontrolled, and two are preprints.
  conf: not stated · class: not stated · holds: Mayjonade 2024 and Chakraverti-Wuerthwein 2026 are the preprints · src: mayjonadeRelativeEffectsAbiotic2024, chakravertiwuerthweinPhylogeneticCoherenceMicrobiome2026 · trail: H1-06 §5. Bounds and failure modes · from: H1-06:B-0162

### adjacent-metrics: rank-wise results on metrics other than composition-environment R2
needs: taxonomies, rankwise-structuring
- **adjacent-metrics.1** In Antarctic wetlands, pH explained more of betaNTI (phylogenetic turnover, not composition) at ASV level (R2 0.20) than at OTU97 (0.08).
  conf: not stated · class: not stated · holds: Antarctic wetlands; unit counts uncontrolled; a metric that measures something other than composition-environment R2 · src: quirogaEcologicalAssemblyBacterial2022 · trail: H1-06 §4. Part B · from: H1-06:B-0143, H1-06:B-0144
- **adjacent-metrics.2** Abundance-occupancy relationships in an estuary were weakest at species and roughly constant from genus to phylum.
  conf: not stated · class: not stated · holds: one estuary · src: izabelshenAbundanceOccupancyRelationshipsAlong2021 · trail: H1-06 §4. Part B · from: H1-06:B-0145
- **adjacent-metrics.3** Across about one million full-length 16S sequences, the ecological consistency of habitat annotations, scored against random partitions with the same cluster count and size distribution, generally fell as OTU thresholds became stricter (finer) for complete and average linkage; single linkage behaved differently.
  conf: not stated · class: deriv (note: "inferred, identity thresholds only, not ranks") · holds: identity thresholds, not ranks; the design controls group number and size, but the response is annotation consistency, not environment-explained composition · src: schmidtEcologicalConsistencySSU2014 (inferred, identity thresholds only, not ranks) · trail: H1-06 §4. Part B · from: H1-06:B-0146..0148

### ab-relation: relation between trait depth and rank-wise structuring
needs: rankwise-structuring, uncontrolled-rank-studies, perturbation-response, ph-preference
- **ab-relation.1** No source tests a correspondence between the rise in composition-environment R2 from otu97 to genus (natural systems) and the depths at which perturbation responses cluster (engineered).
  conf: not stated · class: not stated · holds: the critic's assessment of the review's 'Relation to Part A' reading · src: luEvaluatingCommunityenvironmentRelationships2016, isobePhylogeneticConservationBacterial2019, isobePhylogeneticConservationSoil2020 · trail: H1-06 §critic · from: H1-06:C-053
- **ab-relation.2** The fall in explained variance at phylum in soils and the class-level incoherence in a time series match the weak within-phylum pH signal and the opposing responses inside coarse groups.
  conf: not stated · class: reading (note: "reviewer's reading") · holds: Lu 2016 and Auladell 2022 (natural composition) set beside Ramoneda 2023 and Isobe 2019 · src: luEvaluatingCommunityenvironmentRelationships2016, auladellSeasonalNicheDifferentiation2021, ramonedaBuildingGenomebasedUnderstanding2023, isobePhylogeneticConservationBacterial2019 · trail: H1-06 §4. Part B · from: H1-06:B-0149, H1-06:B-0150
- **ab-relation.3** None of the studies links composition structure to genome content.
  conf: not stated · class: search (note: "None of the studies links composition structure to genome content") · holds: the sources the review read · src: none (a search result) · trail: H1-06 §4. Part B · from: H1-06:B-0151

## Do not say
- **dns.1** "Environmental preferences (pH, moisture, salinity, temperature optima): measured and inconsistent between methods, taxonomies or datasets", as the natural-system verdict.
  why: the 'inconsistent' label only emerges when natural evidence (one large study, weak signal) is set beside engineered isolate and transplant work or a preprint on a non-comparable quantity (canonical loadings); Common rule 10 forbids letting engineered evidence carry a natural-system verdict; the A1 reviewer's reading behind it is built from two sources, one a preprint · instead: a1-environmental-preferences.6, a1-environmental-preferences.7, temperature-preference.1 · trail: H1-06 §critic · from: H1-06:A-001, H1-06:A-023, H1-06:C-005, H1-06:C-012, H1-06:C-013, H1-06:C-014, H1-06:C-033, H1-06:C-056
- **dns.2** "ASVs within single families spanned four or more pH units (Xanthobacteraceae in soil, Chitinophagaceae in freshwater)."
  why: the source gives Chitinophagaceae 4.63 to 8.35 (3.72 units), so it does not span four units · instead: ph-preference.4 · trail: H1-06 §critic · from: H1-06:B-0035, H1-06:C-022, H1-06:C-036
- **dns.3** "97% OTUs explained more composition variance than ASVs (Bay 2020)."
  why: Bay compares the high-resolution set against clustered and/or rare-taxon-filtered data with incidence-based variation partitioning; the paraphrase reduces a clustering-plus-filtering contrast to clustering alone · instead: uncontrolled-rank-studies.6 · trail: H1-06 §critic · from: H1-06:A-021, H1-06:C-019, H1-06:C-020
- **dns.4** "Coarse groups can contain opposing finer responses", as a general bound.
  why: it rests on one N-addition study plus a time series, and the N-addition study also reports consistent coarse-rank responses · instead: perturbation-response.4, perturbation-response.5, uncontrolled-rank-studies.8 · trail: H1-06 §critic · from: H1-06:B-0159, H1-06:C-031
- **dns.5** "The rise in explained variance from otu97 to about otu94 and genus [23, 25]", as a pattern replicated across Lu 2016 and Bay 2020.
  why: Bay 2020 compares ASVs against clustered and/or filtered data, a different step; the rise itself rests on Lu 2016 alone · instead: rankwise-structuring.3, uncontrolled-rank-studies.6 · trail: H1-06 §critic · from: H1-06:B-0138, H1-06:C-032
- **dns.6** "The rise in explained variance from otu97 to about otu94 and genus matches where perturbation responses cluster (tau_D about 0.017 to 0.02, about genus)."
  why: links a natural-system composition result to engineered perturbation-response depths, breaking the natural/engineered separation (Common rule 10); a correspondence the sources do not test · instead: ab-relation.1 · trail: H1-06 §critic · from: H1-06:C-053
- **dns.7** "Perturbation responses, a different quantity, cluster at roughly genus depth in 16S terms."
  why: the equation of tau_D 0.016 to 0.020 with 'roughly genus' is the Isobe authors'; the review's own Section 1 says a 16S depth "cannot be converted into a rank" · instead: perturbation-response.1, perturbation-response.2, perturbation-response.6 · trail: H1-06 §critic · from: H1-06:B-0080, H1-06:C-054
- **dns.8** "Incompleteness pushes detected function down", as a general statement.
  why: each quantitative element is SINGLE SOURCE (modules, core genes, reference bias), and none measures the effect on conservation depth · instead: genome-incompleteness.8 · trail: H1-06 §critic · from: H1-06:C-034
- **dns.9** That consensus-threshold methods push depth estimates shallower under incompleteness, stated as a bound.
  why: it is the reviewer's reading, labelled as untested, then echoed in Section 5 as a bound · instead: genome-incompleteness.9 · trail: H1-06 §critic · from: H1-06:C-055
- **dns.10** "Rank-wise partitioning is non-monotonic (GTDB: phylum 14.6%, order 9.2%, genus 5.5%)", without the SINGLE SOURCE flag.
  why: the partition is Royalty and Steen's alone; flagged SINGLE SOURCE in the body, it carries weight in the A2 verdict without that flag · instead: rank-partitioning.1, rank-partitioning.2 · trail: H1-06 §critic · from: H1-06:A-012, H1-06:C-035
- **dns.11** "Measured with group number and size controlled", for rank-wise structuring, without its conditions.
  why: it is a single source and conditional on Lu 2016's null design, which the critic could not re-verify (paywalled; only the abstract was confirmed); abundance evenness among groups was not controlled · instead: rankwise-structuring.13 · trail: H1-06 §critic · from: H1-06:C-008, H1-06:C-027
- **dns.12** "pH optimum, soil moisture optimum and habitat association sit in deep clades."
  why: in Martiny et al. 2013 this is a discussion claim resting on other studies, asserted and secondary; that paper does not measure any of these · instead: a1-environmental-preferences.2, a1-environmental-preferences.4 · trail: H1-06 §2. Part A1 · from: H1-06:B-0028, H1-06:B-0029
- **dns.13** An association between environment and composition at a rank, read as evidence about the genomes of that rank.
  why: the note: "an association between environment and composition at a rank is not evidence about the genomes of that rank" · instead: ab-relation.3 · trail: H1-06 §4. Part B · from: H1-06:B-0151
- **dns.14** The strong phylogenetic signal in Chakraverti-Wuerthwein et al. 2026, read as signal in pH optima.
  why: the note: "a canonical loading is not a per-ASV optimum" · instead: ph-preference.10, ph-preference.13 · trail: H1-06 §2. Part A1 · from: H1-06:B-0044
- **dns.15** Goberna and Verdú 2016's figures (mean -D+1 = 0.93, K = 0.16, 9.9% and 8.6%) as evidence in the A1 verdict.
  why: the synthesiser could not re-open the paper and labels it as carrying no weight, yet it is listed in the A1 verdict's evidence classes · instead: trait-compilations.1, trait-compilations.2, trait-compilations.3, trait-compilations.4 · trail: H1-06 §critic, §answers · from: H1-06:A-006, H1-06:C-029

## Gaps
- **gap.1** A large-scale study of 'community conservatism' across microbial phyla and environments, from the group that wrote Schmidt 2014 (Malfertheiner, Tackmann, Rodrigues, von Mering, bioRxiv 10.1101/2024.11.06.622256), is not cited; it may directly address rank-wise environmental coherence with null partitions.
  blocks: rankwise-structuring, uncontrolled-rank-studies · origin: critic coverage gap · from: H1-06:C-045
- **gap.2** No archaeal results: every depth and rank-wise result is bacterial (for example Thaumarchaeota/Nitrososphaeria pH and ammonia-oxidiser niche depth; halophilic and thermophilic archaea).
  blocks: a1-environmental-preferences, a2-metabolic-traits, rankwise-structuring · origin: critic coverage gap · from: H1-06:C-046
- **gap.3** Marine cyanobacterial ecotypes (Prochlorococcus and Synechococcus), where light and temperature optima are measured on isolates and mapped onto a phylogeny against field distributions, are absent; the critic calls this the classic natural-system case for depth of environmental preference.
  blocks: a1-environmental-preferences, temperature-preference · origin: critic coverage gap · from: H1-06:C-047
- **gap.4** Trait databases compiling isolate growth optima (pH, temperature, salinity, oxygen) with phylogenetic signal statistics, other than the preprint Barnum and the non-re-opened Goberna (the critic names Madin et al. 2020, BacDive-based analyses, Sauer and Wang 2019).
  blocks: trait-compilations, a1-environmental-preferences · origin: critic coverage gap · from: H1-06:C-048
- **gap.5** Habitat-preference coherence across 16S clusters from global sequence-habitat compilations, other than Schmidt 2014 (the critic names Chaffron et al. 2010, Tamames et al. 2016, Auguet, Barberán and Casamayor 2010).
  blocks: adjacent-metrics, rankwise-structuring · origin: critic coverage gap · from: H1-06:C-049
- **gap.6** Soil moisture optimum in natural systems: only an engineered isolate study was read; natural rewetting and drought field studies were not obtained (Placella, Evans and Wallenstein), and no alternative routes are named.
  blocks: moisture-preference, a1-environmental-preferences · origin: critic coverage gap; sources not obtained · src: placellaRainfallinducedCarbonDioxide2012, evansClimateChangeAlters2013 · from: H1-06:C-050
- **gap.7** How genome incompleteness biases tau_D or phylogenetic signal has not been tested by any study found; the critic says the search routes behind this 'not found' are not named in the body, while the provenance lists routes behind every 'not found'.
  blocks: genome-incompleteness, tau-d · origin: critic coverage gap; "not found" result · from: H1-06:C-051, H1-06:B-0009
- **gap.8** Rank-wise results under GTDB against SILVA/Greengenes for the same community-environment analysis (db-RDA/PERMANOVA re-run under alternative taxonomies); only the metabolic-coherence comparison (Parras-Moltó) is given.
  blocks: rankwise-structuring, taxonomies · origin: critic coverage gap · from: H1-06:C-052
- **gap.9** The overall tau_D range of Martiny et al. 2013 was transcribed differently by the two search agents (0.0011 to 0.101 against 0.0029 to 0.11) and is unresolved; the load-bearing trait values were not re-checked by the synthesiser or the critic, neither of whom could open the paper.
  blocks: metabolic-depth.2, metabolic-depth.3, metabolic-depth.4, metabolic-depth.5, metabolic-depth.6, metabolic-depth.12, a2-metabolic-traits.1 · origin: unresolved transcription discrepancy; source not re-opened · src: martinyPhylogeneticConservatismFunctional2013 · from: H1-06:B-0087, H1-06:B-0088, H1-06:C-007, H1-06:C-028
- **gap.10** The Methods and Results of Lu et al. 2016 (the null model, the soil class peak, the 50% rise from otu97 to otu94, the per-dataset seawater shapes) were not re-verified by the critic, who could confirm only the abstract. The note disagrees with itself on access: the provenance says the synthesiser "re-opened cached full text for Lu 2016 (null model, soil peak at class, significance above the null, 50% rise from otu97 to otu94)", while the critic says "the review does not say whether the synthesiser re-opened the full text".
  blocks: rankwise-structuring · origin: critic full-text breach; a note that contradicts itself · src: luEvaluatingCommunityenvironmentRelationships2016 · from: H1-06:B-0010, H1-06:C-017, H1-06:C-025..0027, H1-06:C-060
- **gap.11** No rank-wise study controls abundance evenness among groups.
  blocks: rankwise-structuring · origin: the review's own caveat, endorsed by the critic · from: H1-06:B-0130, H1-06:C-010, H1-06:C-018
- **gap.12** No consenTRAIT tau_D for pH, temperature or moisture optima was found.
  blocks: a1-environmental-preferences, ph-preference, moisture-preference, temperature-preference · origin: "not found" result · from: H1-06:B-0009, H1-06:B-0028
- **gap.13** No rank-wise composition-environment study other than Lu 2016 that controls group number and size was found (Schmidt 2014 controls them, but for identity thresholds and annotation consistency, not ranks).
  blocks: rankwise-structuring · origin: "not found" result · from: H1-06:B-0009
- **gap.14** The primary studies behind the deep-clade statement in Martiny et al. 2013 were not obtained (Placella et al. 2012, Philippot et al. 2010).
  blocks: a1-environmental-preferences · origin: sources not obtained that matter · src: placellaRainfallinducedCarbonDioxide2012, philippotEcologicalCoherenceHigh2010 · from: H1-06:B-0030
- **gap.15** Goberna and Verdú 2016 was read in full by one search agent only and could not be re-opened. The note disagrees with itself on it: the body cites it with figures, while the Sources not obtained callout lists it under the header "None of these supports any claim in the review".
  blocks: trait-compilations · origin: a note that contradicts itself; source not re-opened · src: gobernaPredictingMicrobialTraits2016 · from: H1-06:B-0012, H1-06:B-0064, H1-06:C-029
- **gap.16** No study links rank-wise composition structure to genome content.
  blocks: ab-relation · origin: "not found" result · from: H1-06:B-0151
- **gap.17** The publication status of the preprints Barnum 2024 and Mayjonade 2024 is unverified.
  blocks: trait-compilations, uncontrolled-rank-studies · origin: the note's provenance · src: barnumPredictingMicrobialGrowth2024, mayjonadeRelativeEffectsAbiotic2024 · from: H1-06:B-0016

## Out of scope
- H1-06:C-037..0044: reference corrections and reference checks, applied in Sources
- H1-06:C-057..0059: the brief's stated expectation for Part B and whether the review repeats it (provenance of the run, not a finding)
- H1-06:A-006: the A1 verdict's list of evidence classes by source (each claim carries its own class; the critic's objection to it is dns.15)

## Sources
```bibtex
@article{martinyPhylogeneticConservatismFunctional2013,
  author = {Martiny, Adam C. and Treseder, Kathleen and Pusch, Gordon},
  title = {Phylogenetic conservatism of functional traits in microorganisms},
  journal = {The ISME Journal},
  year = {2013},
  volume = {7},
  number = {4},
  pages = {830--838},
  doi = {10.1038/ismej.2012.160},
  note = {access: not stated (the synthesiser "could not re-open Martiny 2013 (Europe PMC fullTextXML empty)"; its trait values "rest on two independent search-agent readings"); online 2012-12-13, print 2013 (critic: H1-06:C-037); cited as: H1-06 [1]}
}

@article{zimmermanMicrodiversityExtracellularEnzyme2013,
  author = {Zimmerman, Amy E. and Martiny, Adam C. and Allison, Steven D.},
  title = {Microdiversity of extracellular enzyme genes among sequenced prokaryotic genomes},
  journal = {The ISME Journal},
  year = {2013},
  volume = {7},
  number = {6},
  pages = {1187--1199},
  doi = {10.1038/ismej.2012.176},
  note = {access: not stated; cited as: H1-06 [2]}
}

@article{berlemontPhylogeneticDistributionPotential2013,
  author = {Berlemont, Renaud and Martiny, Adam C.},
  title = {Phylogenetic distribution of potential cellulases in bacteria},
  journal = {Applied and Environmental Microbiology},
  year = {2013},
  volume = {79},
  number = {5},
  pages = {1545--1554},
  doi = {10.1128/AEM.03305-12},
  note = {access: not stated; cited as: H1-06 [3]}
}

@article{sunPhylogeneticDistributionPolysaccharideDegrading2021,
  author = {Sun, Zhong-Zhi and Ji, Bo-Wen and Zheng, Ning and Wang, Meng and Cao, Ye and Wan, Lu and Li, Yi-Song and Rong, Jin-Cheng and He, Hai-Lun and Chen, Xiu-Lan and Zhang, Yu-Zhong and Xie, Bin-Bin},
  title = {Phylogenetic distribution of polysaccharide-degrading enzymes in marine bacteria},
  journal = {Frontiers in Microbiology},
  year = {2021},
  volume = {12},
  pages = {658620},
  doi = {10.3389/fmicb.2021.658620},
  note = {access: not stated; cited as: H1-06 [4]}
}

@article{lopezmondejarGlobalDistributionCarbohydrate2022,
  author = {L{\'o}pez-Mond{\'e}jar, Rub{\'e}n and Tl{\'a}skal, Vojt{\v{e}}ch and da Rocha, Ulisses Nunes and Baldrian, Petr},
  title = {Global distribution of carbohydrate utilization potential in the prokaryotic tree of life},
  journal = {mSystems},
  year = {2022},
  volume = {7},
  number = {6},
  pages = {e00829-22},
  doi = {10.1128/msystems.00829-22},
  note = {access: not stated; cited as: H1-06 [5]}
}

@article{royaltyQuantitativelyPartitioningMicrobial2019,
  author = {Royalty, Taylor M. and Steen, Andrew D.},
  title = {Quantitatively partitioning microbial genomic traits among taxonomic ranks across the microbial tree of life},
  journal = {mSphere},
  year = {2019},
  volume = {4},
  number = {4},
  pages = {e00446-19},
  doi = {10.1128/mSphere.00446-19},
  note = {access: not stated; erratum: mSphere 4(5): e00637-19, doi:10.1128/mSphere.00637-19 (replaces Table S2 only; the critic verified it, H1-06:C-042); cited as: H1-06 [6]}
}

@article{parrasmoltoAssessmentPhylofunctionalCoherence2021,
  author = {Parras-Molt{\'o}, Marcos and Aguirre de C{\'a}rcer, Daniel},
  title = {Assessment of phylo-functional coherence along the bacterial phylogeny and taxonomy},
  journal = {Scientific Reports},
  year = {2021},
  volume = {11},
  number = {1},
  pages = {8299},
  doi = {10.1038/s41598-021-87909-1},
  note = {access: not stated; cited as: H1-06 [7]}
}

@article{hoffertConstructingPeriodicTable2026,
  author = {Hoffert, Michael and Gorman, Evan and Lladser, Manuel E. and Fierer, Noah},
  title = {Constructing a ``periodic table'' of bacteria to map diversity in trait space},
  journal = {The ISME Journal},
  year = {2026},
  volume = {20},
  number = {1},
  pages = {wraf289},
  doi = {10.1093/ismejo/wraf289},
  note = {access: not stated; cited as: H1-06 [8]}
}

@article{eisenhoferImpactMicrobialGenome2023,
  author = {Eisenhofer, Raphael and Odriozola, I{\~n}aki and Alberdi, Antton},
  title = {Impact of microbial genome completeness on metagenomic functional inference},
  journal = {ISME Communications},
  year = {2023},
  volume = {3},
  number = {1},
  pages = {12},
  doi = {10.1038/s43705-023-00221-z},
  note = {access: not stated; cited as: H1-06 [9]}
}

@article{liCriticalAssessmentPangenomic2022,
  author = {Li, Tang and Yin, Yanbin},
  title = {Critical assessment of pan-genomic analysis of metagenome-assembled genomes},
  journal = {Briefings in Bioinformatics},
  year = {2022},
  volume = {23},
  number = {6},
  pages = {bbac413},
  doi = {10.1093/bib/bbac413},
  note = {access: not stated; cited as: H1-06 [10]}
}

@article{albrightTraitBiasesMicrobial2023,
  author = {Albright, Sage and Louca, Stilianos},
  title = {Trait biases in microbial reference genomes},
  journal = {Scientific Data},
  year = {2023},
  volume = {10},
  number = {1},
  pages = {84},
  doi = {10.1038/s41597-023-01994-7},
  note = {access: not stated; cited as: H1-06 [11]}
}

@article{barnumPredictingMicrobialGrowth2024,
  author = {Barnum, Tyler P. and Crits-Christoph, Alexander and Molla, Michael and Carini, Paul and Lee, Henry H. and Ostrov, Nili},
  title = {Predicting microbial growth conditions from amino acid composition},
  journal = {bioRxiv},
  year = {2024},
  pages = {2024.03.22.586313},
  doi = {10.1101/2024.03.22.586313},
  note = {access: not stated (read as preprint, version posted 22 March 2024); type: preprint, not peer reviewed; publication status unverified (the note); incomplete: volume, number; cited as: H1-06 [12]}
}

@article{ramonedaBuildingGenomebasedUnderstanding2023,
  author = {Ramoneda, Josep and Stallard-Olivera, Elias and Hoffert, Michael and Winfrey, Claire C. and Stadler, Masumi and Ni{\~n}o-Garc{\'i}a, Juan Pablo and Fierer, Noah},
  title = {Building a genome-based understanding of bacterial pH preferences},
  journal = {Science Advances},
  year = {2023},
  volume = {9},
  number = {17},
  pages = {eadf8998},
  doi = {10.1126/sciadv.adf8998},
  note = {access: full_text (the synthesiser "re-opened cached full text"); cited as: H1-06 [13]}
}

@article{lennonMappingNicheSpace2012,
  author = {Lennon, Jay T. and Aanderud, Zachary T. and Lehmkuhl, B. K. and Schoolmaster, Donald R.},
  title = {Mapping the niche space of soil microorganisms using taxonomy and traits},
  journal = {Ecology},
  year = {2012},
  volume = {93},
  number = {8},
  pages = {1867--1879},
  doi = {10.1890/11-1745.1},
  note = {access: full_text (the synthesiser "re-opened cached full text"); author: the note gives "Schoolmaster, Donald R., Jr."; Crossref has no "Jr." (critic: H1-06:C-040); cited as: H1-06 [14]}
}

@article{morrisseyEvolutionaryHistoryInfluences2015,
  author = {Morrissey, Ember M. and Franklin, Rima B.},
  title = {Evolutionary history influences the salinity preference of bacterial taxa in wetland soils},
  journal = {Frontiers in Microbiology},
  year = {2015},
  volume = {6},
  pages = {1013},
  doi = {10.3389/fmicb.2015.01013},
  note = {access: not stated; cited as: H1-06 [15]}
}

@article{gobernaPredictingMicrobialTraits2016,
  author = {Goberna, Marta and Verd{\'u}, Miguel},
  title = {Predicting microbial traits with phylogenies},
  journal = {The ISME Journal},
  year = {2016},
  volume = {10},
  number = {4},
  pages = {959--967},
  doi = {10.1038/ismej.2015.171},
  note = {access: full_text ("read in full by one agent only"; the synthesiser could not re-open it, "OUP bot challenge"); conflict: also listed under Sources not obtained in the note's callout, whose header says none of those sources "supports any claim in the review", while the body cites it with figures; online 2015, cited 2016 (critic: H1-06:C-038); cited as: H1-06 [16]}
}

@article{farrellBacterialGrowthTemperature2024,
  author = {Farrell, Anne A. and Nesb{\o}, Camilla L. and Zhaxybayeva, Olga},
  title = {Bacterial growth temperature as a horizontally acquired polygenic trait},
  journal = {Genome Biology and Evolution},
  year = {2025},
  volume = {17},
  number = {1},
  pages = {evae277},
  doi = {10.1093/gbe/evae277},
  note = {access: not stated; online 2024-12-26, cited 2025 (critic: H1-06:C-038); cited as: H1-06 [17]}
}

@article{chaseMicrodiversityAbundantTerrestrial2017,
  author = {Chase, Alexander B. and Karaoz, Ulas and Brodie, Eoin L. and Gomez-Lunar, Zulema and Martiny, Adam C. and Martiny, Jennifer B. H.},
  title = {Microdiversity of an abundant terrestrial bacterium encompasses extensive variation in ecologically relevant traits},
  journal = {mBio},
  year = {2017},
  volume = {8},
  number = {6},
  pages = {e01809-17},
  doi = {10.1128/mBio.01809-17},
  note = {access: not stated; cited as: H1-06 [18]}
}

@article{isobePhylogeneticConservationBacterial2019,
  author = {Isobe, Kazuo and Allison, Steven D. and Khalili, Banafshe and Martiny, Adam C. and Martiny, Jennifer B. H.},
  title = {Phylogenetic conservation of bacterial responses to soil nitrogen addition across continents},
  journal = {Nature Communications},
  year = {2019},
  volume = {10},
  number = {1},
  pages = {2499},
  doi = {10.1038/s41467-019-10390-y},
  note = {access: not stated; cited as: H1-06 [19]}
}

@article{isobePhylogeneticConservationSoil2020,
  author = {Isobe, Kazuo and Bouskill, Nicholas J. and Brodie, Eoin L. and Sudderth, Erika A. and Martiny, Jennifer B. H.},
  title = {Phylogenetic conservation of soil bacterial responses to simulated global changes},
  journal = {Philosophical Transactions of the Royal Society B},
  year = {2020},
  volume = {375},
  number = {1798},
  pages = {20190242},
  doi = {10.1098/rstb.2019.0242},
  note = {access: not stated; cited as: H1-06 [20]}
}

@article{amendMicrobialResponseSimulated2015,
  author = {Amend, Anthony S. and Martiny, Adam C. and Allison, Steven D. and Berlemont, Renaud and Goulden, Michael L. and Lu, Ying and Treseder, Kathleen K. and Weihe, Claudia and Martiny, Jennifer B. H.},
  title = {Microbial response to simulated global change is phylogenetically conserved and linked with functional potential},
  journal = {The ISME Journal},
  year = {2016},
  volume = {10},
  number = {1},
  pages = {109--118},
  doi = {10.1038/ismej.2015.96},
  note = {access: not stated; conflict: the Sources not obtained callout heads one item "Amend et al. 2016 and Placella-type drought or rewetting studies:" before giving the Evans and Wallenstein 2014 reference, while the body cites Amend 2016 as [21]; cited as: H1-06 [21]}
}

@article{morrisseyPhylogeneticOrganizationBacterial2016,
  author = {Morrissey, Ember M. and Mau, Rebecca L. and Schwartz, Egbert and Caporaso, J. Gregory and Dijkstra, Paul and van Gestel, Natasja and Koch, Benjamin J. and Liu, Cindy M. and Hayer, Michaela and McHugh, Theresa A. and Marks, Jane C. and Price, Lance B. and Hungate, Bruce A.},
  title = {Phylogenetic organization of bacterial activity},
  journal = {The ISME Journal},
  year = {2016},
  volume = {10},
  number = {9},
  pages = {2336--2340},
  doi = {10.1038/ismej.2016.28},
  note = {access: not stated; cited as: H1-06 [22]}
}

@article{luEvaluatingCommunityenvironmentRelationships2016,
  author = {Lu, Hsiao-Pei and Yeh, Yi-Chun and Sastri, Akash R. and Shiah, Fuh-Kwo and Gong, Gwo-Ching and Hsieh, Chih-hao},
  title = {Evaluating community-environment relationships along fine to broad taxonomic resolutions reveals evolutionary forces underlying community assembly},
  journal = {The ISME Journal},
  year = {2016},
  volume = {10},
  number = {12},
  pages = {2867--2878},
  doi = {10.1038/ismej.2016.78},
  note = {access: full_text (the synthesiser "re-opened cached full text"; the critic could confirm only the abstract, H1-06:C-017, C-026); cited as: H1-06 [23]}
}

@article{mayjonadeRelativeEffectsAbiotic2024,
  author = {Mayjonade, Baptiste and Zamar, R{\'e}my and Carrere, S{\'e}bastien and Roux, Fabrice},
  title = {The relative effects of abiotic and biotic factors in explaining the structure of soil bacterial communities at diverse taxonomic levels},
  journal = {bioRxiv},
  year = {2024},
  pages = {2024.10.29.620845},
  doi = {10.1101/2024.10.29.620845},
  note = {access: full_text (the synthesiser "re-opened cached full text"; read as preprint, version posted 3 November 2024); type: preprint, not peer reviewed; publication status unverified (the note); incomplete: volume, number; cited as: H1-06 [24]}
}

@article{baySoilBacterialCommunities2020,
  author = {Bay, Sean K. and McGeoch, Melodie A. and Gillor, Osnat and Wieler, Nimrod and Palmer, David J. and Baker, David J. and Chown, Steven L. and Greening, Chris},
  title = {Soil bacterial communities exhibit strong biogeographic patterns at fine taxonomic resolution},
  journal = {mSystems},
  year = {2020},
  volume = {5},
  number = {4},
  pages = {e00540-20},
  doi = {10.1128/mSystems.00540-20},
  note = {access: full_text (the synthesiser "re-opened cached full text"); cited as: H1-06 [25]}
}

@article{quirogaEcologicalAssemblyBacterial2022,
  author = {Quiroga, Mar{\'i}a V. and Valverde, Angel and Mataloni, Gabriela and Casa, Valeria and Stegen, James C. and Cowan, Don},
  title = {The ecological assembly of bacterial communities in Antarctic wetlands varies across levels of phylogenetic resolution},
  journal = {Environmental Microbiology},
  year = {2022},
  volume = {24},
  number = {8},
  pages = {3486--3499},
  doi = {10.1111/1462-2920.15912},
  note = {access: full_text (the synthesiser "re-opened cached full text"); cited as: H1-06 [26]}
}

@article{schmidtEcologicalConsistencySSU2014,
  author = {Schmidt, Thomas S. B. and Matias Rodrigues, Jo{\~a}o F. and von Mering, Christian},
  title = {Ecological consistency of SSU rRNA-based operational taxonomic units at a global scale},
  journal = {PLoS Computational Biology},
  year = {2014},
  volume = {10},
  number = {4},
  pages = {e1003594},
  doi = {10.1371/journal.pcbi.1003594},
  note = {access: not stated; cited as: H1-06 [27]}
}

@article{auladellSeasonalNicheDifferentiation2021,
  author = {Auladell, Adri{\`a} and Barber{\'a}n, Albert and Logares, Ramiro and Garc{\'e}s, Esther and Gasol, Josep M. and Ferrera, Isabel},
  title = {Seasonal niche differentiation among closely related marine bacteria},
  journal = {The ISME Journal},
  year = {2022},
  volume = {16},
  number = {1},
  pages = {178--189},
  doi = {10.1038/s41396-021-01053-2},
  note = {access: not stated; online 2021-07-20, cited 2022 (critic: H1-06:C-038); cited as: H1-06 [28]}
}

@article{chakravertiwuerthweinPhylogeneticCoherenceMicrobiome2026,
  author = {Chakraverti-Wuerthwein, Milena S. and Domenig, Alissa and Kuehn, Seppe},
  title = {Phylogenetic coherence in microbiome composition across environmental gradients},
  journal = {bioRxiv},
  year = {2026},
  pages = {2026.06.07.730742},
  doi = {10.64898/2026.06.07.730742},
  note = {access: not stated (read as preprint v1, posted 11 June 2026); type: preprint, not peer reviewed; incomplete: volume, number; cited as: H1-06 [29]}
}

@article{izabelshenAbundanceOccupancyRelationshipsAlong2021,
  author = {Izabel-Shen, Dandan and H{\"o}ger, Anna-Lena and J{\"u}rgens, Klaus},
  title = {Abundance-occupancy relationships along taxonomic ranks reveal a consistency of niche differentiation in marine bacterioplankton with distinct lifestyles},
  journal = {Frontiers in Microbiology},
  year = {2021},
  volume = {12},
  pages = {690712},
  doi = {10.3389/fmicb.2021.690712},
  note = {access: not stated (published version; a bioRxiv preprint, doi:10.1101/2021.04.09.439152, was also read by one search agent); cited as: H1-06 [30]}
}

@article{placellaRainfallinducedCarbonDioxide2012,
  author = {Placella, Sarah A. and Brodie, Eoin L. and Firestone, Mary K.},
  title = {Rainfall-induced carbon dioxide pulses result from sequential resuscitation of phylogenetically clustered microbial groups},
  journal = {Proceedings of the National Academy of Sciences},
  year = {2012},
  volume = {109},
  number = {27},
  pages = {10931--10936},
  doi = {10.1073/pnas.1204306109},
  note = {access: not_obtained (routes: Europe PMC, PMC (reCAPTCHA), pnas.org (HTTP 403)); cited as: H1-06 Sources not obtained}
}

@article{philippotEcologicalCoherenceHigh2010,
  author = {Philippot, Laurent and Andersson, Siv G. E. and Battin, Tom J. and Prosser, James I. and Schimel, Joshua P. and Whitman, William B. and Hallin, Sara},
  title = {The ecological coherence of high bacterial taxonomic ranks},
  journal = {Nature Reviews Microbiology},
  year = {2010},
  volume = {8},
  number = {7},
  pages = {523--529},
  doi = {10.1038/nrmicro2367},
  note = {access: not_obtained (search results showed only the abstract); cited as: H1-06 Sources not obtained}
}

@article{yehElevationalPatternsHierarchical2019,
  author = {Yeh, Chih-Fu and Soininen, Janne and Teittinen, Anette and Wang, Jianjun},
  title = {Elevational patterns and hierarchical determinants of biodiversity across microbial taxonomic scales},
  journal = {Molecular Ecology},
  year = {2019},
  volume = {28},
  number = {1},
  pages = {86--99},
  doi = {10.1111/mec.14935},
  note = {access: not_obtained; not cited; cited as: H1-06 Sources not obtained}
}

@article{martinyMicrobiomesLightTraits2015,
  author = {Martiny, Jennifer B. H. and Jones, Stuart E. and Lennon, Jay T. and Martiny, Adam C.},
  title = {Microbiomes in light of traits: A phylogenetic perspective},
  journal = {Science},
  year = {2015},
  volume = {350},
  number = {6261},
  pages = {aac9323},
  doi = {10.1126/science.aac9323},
  note = {access: not_obtained (paywalled); not cited; cited as: H1-06 Sources not obtained}
}

@article{evansClimateChangeAlters2013,
  author = {Evans, Sarah E. and Wallenstein, Matthew D.},
  title = {Climate change alters ecological strategies of soil bacteria},
  journal = {Ecology Letters},
  year = {2014},
  volume = {17},
  number = {2},
  pages = {155--164},
  doi = {10.1111/ele.12206},
  note = {access: not_obtained (Europe PMC metadata only); not cited in the body (named in the critic's moisture gap, H1-06:C-050); listed twice in the Sources not obtained callout; cited as: H1-06 Sources not obtained}
}

@article{oliverioIdentifyingMicrobialTaxa2016,
  author = {Oliverio, Angela M. and Bradford, Mark A. and Fierer, Noah},
  title = {Identifying the microbial taxa that consistently respond to soil warming across time and space},
  journal = {Global Change Biology},
  year = {2017},
  volume = {23},
  number = {5},
  pages = {2117--2129},
  doi = {10.1111/gcb.13557},
  note = {access: not_obtained (Europe PMC metadata only); not cited; cited as: H1-06 Sources not obtained}
}

@article{barberanWhyAreMicrobes2014,
  author = {Barber{\'a}n, Albert and Ramirez, Kelly S. and Leff, Jonathan W. and Bradford, Mark A. and Wall, Diana H. and Fierer, Noah},
  title = {Why are some microbes more ubiquitous than others? Predicting the habitat breadth of soil bacteria},
  journal = {Ecology Letters},
  year = {2014},
  volume = {17},
  number = {7},
  pages = {794--802},
  doi = {10.1111/ele.12282},
  note = {access: not_obtained (Europe PMC metadata only); not cited; cited as: H1-06 Sources not obtained}
}

@article{morrisseyEvolutionaryHistoryConstrains2019,
  author = {Morrissey, Ember M. and Mau, Rebecca L. and Hayer, Michaela and Liu, Xiao-Jun Allen and Schwartz, Egbert and Dijkstra, Paul and Koch, Benjamin J. and Allen, Kara and Blazewicz, Steven J. and Hofmockel, Kirsten and Pett-Ridge, Jennifer and Hungate, Bruce A.},
  title = {Evolutionary history constrains microbial traits across environmental variation},
  journal = {Nature Ecology \& Evolution},
  year = {2019},
  volume = {3},
  number = {7},
  pages = {1064--1069},
  doi = {10.1038/s41559-019-0918-y},
  note = {access: not_obtained (Europe PMC not OA; OSTI timeout, refused); not cited; cited as: H1-06 Sources not obtained}
}

@article{hermansBacteriaEmergingIndicators2017,
  author = {Hermans, Syrie M. and Buckley, Hannah L. and Case, Bradley S. and Curran-Cournane, Fiona and Taylor, Matthew and Lear, Gavin},
  title = {Bacteria as emerging indicators of soil condition},
  journal = {Applied and Environmental Microbiology},
  year = {2017},
  volume = {83},
  number = {1},
  pages = {e02826-16},
  doi = {10.1128/AEM.02826-16},
  note = {access: not_obtained (Europe PMC fullTextXML empty, journals.asm.org HTTP 403); not cited; cited as: H1-06 Sources not obtained}
}

@article{walkupPredictivePowerPhylogeny2023,
  author = {Walkup, Jeth and Dang, Chansotheary and Mau, Rebecca L. and others},
  title = {The predictive power of phylogeny on growth rates in soil bacterial communities},
  journal = {ISME Communications},
  year = {2023},
  volume = {3},
  number = {1},
  pages = {73},
  doi = {10.1038/s43705-023-00281-1},
  note = {access: not_obtained (nature.com auth redirect); not cited; incomplete: author (the note: author list not verified; critic: H1-06:C-043); cited as: H1-06 Sources not obtained}
}

@article{albrightComparativeGenomicsNitrogen2018,
  author = {Albright, Michaeline B. N. and Timalsina, Bipana and Martiny, Jennifer B. H. and Dunbar, John},
  title = {Comparative genomics of nitrogen cycling pathways in bacteria and archaea},
  journal = {Microbial Ecology},
  year = {2019},
  volume = {77},
  number = {3},
  pages = {597--606},
  doi = {10.1007/s00248-018-1239-4},
  note = {access: not_obtained (Europe PMC metadata only); not cited; cited as: H1-06 Sources not obtained}
}

@article{nelsonGlobalBiogeographyMicrobial2016,
  author = {Nelson, Michaeline B. and Martiny, Adam C. and Martiny, Jennifer B. H.},
  title = {Global biogeography of microbial nitrogen-cycling traits in soil},
  journal = {Proceedings of the National Academy of Sciences},
  year = {2016},
  volume = {113},
  number = {29},
  pages = {8033--8040},
  doi = {10.1073/pnas.1601070113},
  note = {access: not_obtained (Europe PMC fullTextXML for PMC4961168 empty); not cited; cited as: H1-06 Sources not obtained}
}

@article{freckletonPhylogeneticAnalysisComparative2002,
  author = {Freckleton, R. P. and Harvey, P. H. and Pagel, M.},
  title = {Phylogenetic analysis and comparative data: A test and review of evidence},
  journal = {The American Naturalist},
  year = {2002},
  volume = {160},
  number = {6},
  pages = {712--726},
  doi = {10.1086/343873},
  note = {background; access: abstract_only (checked on Crossref and OpenAlex)}
}

@article{blombergTestingPhylogeneticSignal2003,
  author = {Blomberg, Simon P. and Garland, Theodore and Ives, Anthony R.},
  title = {Testing for phylogenetic signal in comparative data: Behavioral traits are more labile},
  journal = {Evolution},
  year = {2003},
  volume = {57},
  number = {4},
  pages = {717--745},
  doi = {10.1111/j.0014-3820.2003.tb00285.x},
  note = {background; access: abstract_only (checked on Crossref and Europe PMC)}
}

@article{legendreDistancebasedRedundancyAnalysis1999,
  author = {Legendre, Pierre and Anderson, Marti J.},
  title = {Distance-based redundancy analysis: Testing multispecies responses in multifactorial ecological experiments},
  journal = {Ecological Monographs},
  year = {1999},
  volume = {69},
  number = {1},
  pages = {1--24},
  doi = {10.1890/0012-9615(1999)069[0001:DBRATM]2.0.CO;2},
  note = {background; access: abstract_only (checked on Crossref and OpenAlex)}
}
```
