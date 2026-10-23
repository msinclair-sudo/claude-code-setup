---
type: knowledge
title: Phylogenetic depth of prokaryotic traits and rank-wise environmental structuring
inputs:
  - H1-06: PhD/Proposal/Research/Results/Phylogenetic depth of prokaryotic trait and preference conservation, and how environmental structuring of community composition changes from species to phylum a literature review.md
refs: PhD/Proposal/Refs/Refs.bib
built: 2026-10-23
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

### depth-measures: How depth of conservation and phylogenetic signal are expressed
needs: none

- **depth-measures.bg1** Pagel's lambda is a measure of phylogenetic correlation that normally varies between 0 (phylogenetic independence) and 1 (traits covary in direct proportion to shared evolutionary history).
  kind: background · ref: freckletonPhylogeneticAnalysisComparative2002 · check: DOI 10.1086/343873 resolves on Crossref; stated in the abstract (Europe PMC record)
- **depth-measures.bg2** Blomberg's K is a descriptive statistic that allows valid comparisons of the amount of phylogenetic signal across traits; K below one means less signal than expected.
  kind: background · ref: blombergTestingPhylogeneticSignal2003 · check: DOI 10.1111/j.0014-3820.2003.tb00285.x resolves on Crossref; stated in the abstract (Europe PMC record)
- **depth-measures.1** consenTRAIT's tau_D is the mean 16S rRNA distance from the root of clades in which at least 90% of members share a trait.
  conf: not stated · class: not stated · holds: the consenTRAIT method · src: martinyPhylogeneticConservatismFunctional2013 · trail: H1-06 §1. What · from: H1-06:B-0021
- **depth-measures.2** Phylogenetic signal statistics (Pagel's lambda, Blomberg's K, Moran's I correlograms, D) measure how well a trait tracks the tree without giving one depth.
  conf: not stated · class: not stated · holds: the signal statistics used in the sources read · src: ramonedaBuildingGenomebasedUnderstanding2023, gobernaPredictingMicrobialTraits2016, morrisseyPhylogeneticOrganizationBacterial2016 · trail: H1-06 §1. What · from: H1-06:B-0022
- **depth-measures.3** Rank-wise analyses of community composition use taxonomies, not trees, and the taxonomy differs between studies: Greengenes, SILVA or RDP, GTDB, a curated gyrB taxonomy, or no ranks at all, only sequence-identity thresholds. Rank labels differ between these taxonomies, and identity thresholds are not ranks.
  conf: not stated · class: not stated · holds: the rank-wise and depth studies the review read · src: luEvaluatingCommunityenvironmentRelationships2016, ramonedaBuildingGenomebasedUnderstanding2023, lennonMappingNicheSpace2012, isobePhylogeneticConservationBacterial2019, lopezmondejarGlobalDistributionCarbohydrate2022, royaltyQuantitativelyPartitioningMicrobial2019, hoffertConstructingPeriodicTable2026, barnumPredictingMicrobialGrowth2024, mayjonadeRelativeEffectsAbiotic2024, baySoilBacterialCommunities2020, quirogaEcologicalAssemblyBacterial2022, schmidtEcologicalConsistencySSU2014 · trail: H1-06 §1. What, §5. Bounds · from: H1-06:B-0023, H1-06:B-0154
- **depth-measures.4** A depth in 16S rRNA distance cannot be converted into a rank.
  conf: not stated · class: not stated · holds: depths quoted in 16S rRNA distance · src: none (the reviewer's synthesis) · trail: H1-06 §1. What · from: H1-06:B-0024
- **depth-measures.5** Depth values from different trees or datasets are not commensurable.
  conf: not stated · class: not stated · holds: tau_D on different trees and genome sets · src: sunPhylogeneticDistributionPolysaccharideDegrading2021 · trail: H1-06 §5. Bounds · from: H1-06:B-0153
- **depth-measures.6** Much of the apparent disagreement in this literature comes from the two halves of the question using different yardsticks: depth on a tree for traits, and ranks of a taxonomy for community composition.
  conf: not stated · class: not stated · holds: the literature the review read · src: none (the reviewer's synthesis) · trail: H1-06 §1. What · from: H1-06:B-0020, H1-06:B-0021, H1-06:B-0023

### environmental-preference: What an environmental preference is
needs: none

- **environmental-preference.1** An environmental "preference" can be (a) a growth optimum measured on isolates, (b) a field optimum inferred from where an ASV is most abundant, or (c) a response to an experimental perturbation; type (c) comes from engineered systems.
  conf: not stated · class: not stated · holds: the sources the review read · src: none (the reviewer's synthesis) · trail: H1-06 §1. What · from: H1-06:B-0026, H1-06:B-0027

### ph-preference: pH preference in natural systems
needs: depth-measures, environmental-preference

- **ph-preference.1** Phylogenetic signal for pH preference was significant in four of five datasets but weak (Pagel's lambda 0.22 to 0.78), and correlogram Moran's I stayed below 0.25 at every depth, shallow ones included; there is no consenTRAIT-style depth.
  conf: single (critic: C-001) · class: meas (note: "measured, natural") · holds: natural soil and freshwater; 4,568 ASVs from five datasets (795 soil and 675 freshwater samples, pH about 3 to 10); pH preference defined as the pH of maximal field abundance; SILVA 138 taxonomy and RAxML trees of 16S; the critic verified lambda and Moran's I in the source · src: ramonedaBuildingGenomebasedUnderstanding2023 · trail: H1-06 §2. Part A1, §critic, §Verdict as delivered · from: H1-06:B-0031..0034, H1-06:A-003, H1-06:C-001, H1-06:C-002, H1-06:C-021
- **ph-preference.2** ASVs within single families spanned 3.7 to 4.2 pH units: Xanthobacteraceae in soil 4.01 to 8.20 (4.19 units), Chitinophagaceae in freshwater 4.63 to 8.35 (3.72 units).
  conf: not stated · class: not stated · holds: natural soil and freshwater datasets of Ramoneda et al. 2023; the critic's reading of the source · src: ramonedaBuildingGenomebasedUnderstanding2023 · trail: H1-06 §critic, §Adversarial · from: H1-06:B-0035, H1-06:C-002, H1-06:C-022, H1-06:C-036
- **ph-preference.3** A phylum-level tendency seen in one dataset (acidophilic Acidobacteria in freshwater) did not recur.
  conf: not stated · class: meas (note: "measured, natural") · holds: natural soil and freshwater datasets of Ramoneda et al. 2023 · src: ramonedaBuildingGenomebasedUnderstanding2023 · trail: H1-06 §2. Part A1 · from: H1-06:B-0031, H1-06:B-0036, H1-06:B-0032
- **ph-preference.4** The authors conclude that "phylum-level information provides relatively little insight into bacterial pH preferences" and turn to gene content instead.
  conf: not stated · class: meas (note: "measured, natural") · holds: natural soil and freshwater datasets of Ramoneda et al. 2023; the critic verified the phylum quote · src: ramonedaBuildingGenomebasedUnderstanding2023 · trail: H1-06 §2. Part A1, §critic · from: H1-06:B-0031, H1-06:B-0037, H1-06:C-021, H1-06:B-0032
- **ph-preference.5** A genome-based model of pH preference, validated on an independent UK dataset, reached R2 = 0.21 (MAE 0.93 pH units).
  conf: not stated · class: not stated · holds: independent UK validation dataset; the critic verified R2 = 0.21 and MAE 0.93 · src: ramonedaBuildingGenomebasedUnderstanding2023 · trail: H1-06 §2. Part A1, §critic · from: H1-06:B-0037, H1-06:C-021
- **ph-preference.6** Only 6 to 24% of ASVs matched a GTDB genome, and about 35% of those genomes were MAGs or SAGs.
  conf: not stated · class: not stated · holds: the bound on Ramoneda et al.'s genome-based analysis; the critic verified both figures · src: ramonedaBuildingGenomebasedUnderstanding2023 · trail: H1-06 §2. Part A1, §critic · from: H1-06:B-0038, H1-06:C-021
- **ph-preference.7** In CCA of global topsoil (N = 217) and ocean (N = 125) 16S surveys, OTU loadings on the first canonical direction, which aligns with pH in soil and with depth in the ocean, had strong phylogenetic signal (a modified tau_D and Pagel's lambda); secondary canonical directions had weak or no signal.
  conf: single (note: "SINGLE SOURCE") · class: meas (note: "measured, natural, preprint") · holds: natural; a preprint; numeric tau_D values appear only in figures, so the strong-signal claim is qualitative, with no number quoted; the permutation null shuffles sample labels rather than preserving group structure; a canonical loading is not a per-ASV optimum · src: chakravertiwuerthweinPhylogeneticCoherenceMicrobiome2026 · trail: H1-06 §2. Part A1, §Adversarial, §Verdict as delivered · from: H1-06:B-0040..0044, H1-06:A-003, H1-06:C-030
- **ph-preference.8** The field-optimum and canonical-loading results are not in direct contradiction, but together they show that whether "pH preference" looks phylogenetically structured depends on how the preference is operationalised.
  conf: not stated · class: reading (note: "Reviewer's reading") · holds: built from two sources, one a preprint; the critic: a methodological argument that underpins the 'inconsistent' A1 verdict · src: ramonedaBuildingGenomebasedUnderstanding2023, chakravertiwuerthweinPhylogeneticCoherenceMicrobiome2026 · trail: H1-06 §2. Part A1, §Adversarial · from: H1-06:B-0044, H1-06:B-0045, H1-06:C-056
- **ph-preference.9** The only large natural-system test of pH preference finds weak signal and poor prediction by rank.
  conf: single (critic: C-033) · class: not stated · holds: the one large natural-system study of pH preference, in soil and freshwater · src: ramonedaBuildingGenomebasedUnderstanding2023 · trail: H1-06 §2. Part A1, §Adversarial · from: H1-06:B-0079, H1-06:B-0032, H1-06:C-033

### moisture-salinity: Moisture and salinity preferences (engineered)
needs: depth-measures, environmental-preference

- **moisture-salinity.1** Across seven RDP ranks against permutation nulls, phylum level held 52% of the variance in optimum water potential and 58% in niche breadth, and strain level held 21 to 29% against 58 to 65% expected by chance.
  conf: single (note: "SINGLE SOURCE") · class: meas (note: "measured, engineered") · holds: engineered: 23 bacterial and 22 fungal soil isolates respired across a manipulated water-potential gradient (lab isolates, n = 23 bacteria); the authors caution that isolate numbers are small (5 bacterial phyla, 19 genera); the only direct rank-resolved measurement of a moisture optimum found · src: lennonMappingNicheSpace2012 · trail: H1-06 §2. Part A1, §Verdict as delivered · from: H1-06:B-0046..0050, H1-06:A-004
- **moisture-salinity.2** Salinity-preferring phylotypes were phylogenetically clustered both tree-wide and near the tips (freshwater-preferring: SES-PD -3.5, NTI 4.3; saltwater-preferring: SES-PD -5.4, NTI 5.2, p < 0.01); no depth statistic was reported.
  conf: single (note: "SINGLE SOURCE") · class: meas (note: "measured, engineered") · holds: engineered: a reciprocal transplant between tidal freshwater and brackish marsh soils; Greengenes 97% OTUs, n = 5 per treatment · src: morrisseyEvolutionaryHistoryInfluences2015 · trail: H1-06 §2. Part A1, §Verdict as delivered · from: H1-06:B-0051..0053, H1-06:B-0055, H1-06:A-004
- **moisture-salinity.3** At class level, Betaproteobacteria were enriched among freshwater-preferring phylotypes and Alpha- and Gammaproteobacteria among saltwater-preferring ones.
  conf: single (note: "SINGLE SOURCE") · class: meas (note: "measured, engineered") · holds: engineered: the tidal freshwater and brackish marsh reciprocal transplant · src: morrisseyEvolutionaryHistoryInfluences2015 · trail: H1-06 §2. Part A1 · from: H1-06:B-0051, H1-06:B-0053, H1-06:B-0054
- **moisture-salinity.4** Moisture and salinity preferences have not been measured in natural systems: the rank-resolved results are engineered, and the deep-rank moisture result has no natural-system rank-wise counterpart among the sources read.
  conf: not stated · class: not stated · search: not stated · holds: natural systems; the engineered isolate and transplant studies (Lennon 2012, Morrissey and Franklin 2015) · src: lennonMappingNicheSpace2012, morrisseyEvolutionaryHistoryInfluences2015 · trail: H1-06 §critic, §4. Part B, §5. Bounds · from: H1-06:C-003, H1-06:C-015, H1-06:B-0152, H1-06:B-0164, H1-06:C-014

### temperature-optimum: Temperature optimum
needs: depth-measures, environmental-preference

- **temperature-optimum.1** Within the phylum Thermotogota (64 genomes), optimal growth temperature has strong signal (Pagel's lambda 0.93), yet ancestral reconstruction places several secondary shifts to mesophily and hyperthermophily, and most of the 68 OGT-associated genes have histories of horizontal transfer: strong signal within a phylum coexists with repeated shifts.
  conf: single (note: "SINGLE SOURCE") · class: deriv (note: "inferred") · holds: one phylum, Thermotogota, 64 genomes · src: farrellBacterialGrowthTemperature2024 · trail: H1-06 §2. Part A1, §Verdict as delivered, §critic · from: H1-06:B-0056..0058, H1-06:A-005, H1-06:C-004

### trait-compilations: Compilations and models of traits and growth optima
needs: depth-measures, environmental-preference

- **trait-compilations.1** Across 990 traits collated on a SILVA r119 tree, binary, mostly gene-presence, traits had mean -D+1 = 0.93 (98% significant) and continuous traits mean K = 0.16 (74% significant).
  conf: not stated · class: model (note: "compiled and modelled") · limit: access (note: "I could not re-open it because the publisher returned a bot challenge") · holds: a compilation; read in full by one search agent only, so it carries no weight on its own; the critic: still listed in the A1 verdict's evidence classes · src: gobernaPredictingMicrobialTraits2016 · trail: H1-06 §2. Part A1, §Adversarial · from: H1-06:B-0059..0061, H1-06:B-0064, H1-06:C-029
- **trait-compilations.2** The compilation is internally inconsistent on environmental optima: it lists optimal pH and temperature and moisture niche breadth among "the most conserved continuous traits", and elsewhere places optimal pH, salt tolerance and moisture niche breadth among traits with "moderate signals".
  conf: not stated · class: not stated · limit: access (note: "I could not re-open it because the publisher returned a bot challenge") · holds: 990 traits on a SILVA r119 tree; read in full by one search agent only, carrying no weight on its own · src: gobernaPredictingMicrobialTraits2016 · trail: H1-06 §2. Part A1, §Adversarial · from: H1-06:B-0059, H1-06:B-0062, H1-06:B-0064, H1-06:C-029
- **trait-compilations.3** Only 9.9% of continuous and 8.6% of binary traits met the compilation's threshold for accurate phylogenetic prediction.
  conf: not stated · class: model (note: "compiled and modelled") · limit: access (note: "I could not re-open it because the publisher returned a bot challenge") · holds: 990 traits on a SILVA r119 tree; read in full by one search agent only · src: gobernaPredictingMicrobialTraits2016 · trail: H1-06 §2. Part A1 · from: H1-06:B-0059, H1-06:B-0063, H1-06:B-0064
- **trait-compilations.4** Growth optima predicted from amino-acid composition for 15,596 BacDive organisms reached, under family-level holdout, R2 0.73 for temperature, 0.81 for salinity and 0.48 for pH, with 92% balanced accuracy for oxygen tolerance.
  conf: not stated · class: model (note: "modelled, preprint") · holds: GTDB r214; a preprint whose publication status is unverified · src: barnumPredictingMicrobialGrowth2024 · trail: H1-06 §2. Part A1, §Provenance · from: H1-06:B-0065, H1-06:B-0066, H1-06:B-0016
- **trait-compilations.5** A phylogeny-only comparison model failed at higher-rank holdouts except for oxygen tolerance, which stayed moderately accurate up to order and class.
  conf: not stated · class: model (note: "modelled, preprint") · holds: 15,596 BacDive organisms, GTDB r214; a preprint · src: barnumPredictingMicrobialGrowth2024 · trail: H1-06 §2. Part A1 · from: H1-06:B-0065, H1-06:B-0067
- **trait-compilations.6** Among six genome-inferred traits, oxygen tolerance had much of its variance at deep nodes, often near phylum, but was "not universally conserved at the phylum level".
  conf: single (note: "SINGLE SOURCE for this method") · class: deriv (note: "inferred") · holds: 50,745 GTDB genomes · src: hoffertConstructingPeriodicTable2026 · trail: H1-06 §2. Part A1 · from: H1-06:B-0068

### perturbation-response-depth: Depth of responses to experimental perturbations (engineered, kept separate)
needs: depth-measures, environmental-preference

- **perturbation-response-depth.1** Responses to N addition across 13 field experiments on five continents were conserved at tau_D 0.016 to 0.020 per location (0.017 merged).
  conf: not stated · class: not stated · holds: engineered perturbation responses (N addition); taxonomy RDP on SILVA 128; the authors equate this to roughly genus, but the review's own Section 1 says a 16S depth cannot be converted into a rank (the critic: inconsistent use); the critic verified the figures · src: isobePhylogeneticConservationBacterial2019 · trail: H1-06 §2. Part A1, §critic, §Adversarial · from: H1-06:B-0069, H1-06:B-0024, H1-06:C-023, H1-06:C-054
- **perturbation-response-depth.2** A correlogram on the same N-addition data detected response similarity out to 22% 16S divergence, which the authors note is a less conservative depth metric.
  conf: not stated · class: not stated · holds: engineered perturbation responses, 13 N-addition field experiments; the critic verified the 22% correlogram depth · src: isobePhylogeneticConservationBacterial2019 · trail: H1-06 §2. Part A1, §critic · from: H1-06:B-0069, H1-06:B-0070, H1-06:C-023
- **perturbation-response-depth.3** Warming, drought, elevated CO2, P addition and liming gave tau_D 0.016 to 0.024, with little difference among perturbations, and clades responding to one perturbation rarely responded to another.
  conf: not stated · class: not stated · holds: engineered perturbation responses of soil bacteria · src: isobePhylogeneticConservationSoil2020 · trail: H1-06 §2. Part A1, §References · from: H1-06:B-0069, H1-06:B-0071, H1-06:R-0137
- **perturbation-response-depth.4** In leaf litter, only positive bacterial responses were significantly conserved; negative responses were not (drought decrease P = 0.541; N decrease P = 0.763).
  conf: not stated · class: not stated · holds: engineered perturbation responses; one litter study · src: amendMicrobialResponseSimulated2015 · trail: H1-06 §2. Part A1, §5. Bounds · from: H1-06:B-0069, H1-06:B-0072, H1-06:B-0160
- **perturbation-response-depth.5** Coarse groups can hide opposing finer ones in the N-addition responses: Gammaproteobacteria as a class had no consistent response while one genus within it responded positively, and an order and a family within it responded in opposite directions.
  conf: not stated · class: not stated · holds: engineered N-addition experiments (one study); the critic verified the Gammaproteobacteria example · src: isobePhylogeneticConservationBacterial2019 · trail: H1-06 §2. Part A1, §critic · from: H1-06:B-0073, H1-06:B-0074, H1-06:C-023, H1-06:B-0069
- **perturbation-response-depth.6** The same N-addition study also reports consistent phylum- and class-level responses: phylum Actinobacteria positive; classes Betaproteobacteria and Deltaproteobacteria negative.
  conf: not stated · class: not stated · holds: engineered N-addition experiments; the review leaves this out, citing only the 'coarse hides fine' example · src: isobePhylogeneticConservationBacterial2019 · trail: H1-06 §critic, §Adversarial · from: H1-06:C-024, H1-06:C-031, H1-06:B-0069
- **perturbation-response-depth.7** In situ growth measured by qSIP had K 0.38 to 0.54 and lambda 0.96 to 0.98.
  conf: not stated · class: not stated · holds: one forest soil; in situ growth, reported among the perturbation responses · src: morrisseyPhylogeneticOrganizationBacterial2016 · trail: H1-06 §2. Part A1 · from: H1-06:B-0069, H1-06:B-0075
- **perturbation-response-depth.8** Within a single 16S OTU (Curtobacterium, minimum 83.2% ANI), the drought response appeared conserved across clades while carbohydrate-use degree and degradation temperature preference varied among clades.
  conf: single (note: "SINGLE SOURCE") · class: meas (note: "measured, natural") · holds: one abundant terrestrial bacterium, a single 16S OTU (Curtobacterium); natural · src: chaseMicrodiversityAbundantTerrestrial2017 · trail: H1-06 §2. Part A1, §References · from: H1-06:B-0076, H1-06:R-0132
- **perturbation-response-depth.9** Perturbation responses are a different quantity from environmental optima; in 16S terms they cluster at tau_D 0.016 to 0.020 per location for N addition (0.017 merged) and at 0.016 to 0.024 for warming, drought, elevated CO2, P addition and liming, which the review calls roughly genus depth.
  conf: not stated · class: not stated · holds: engineered N-addition and global-change experiments; the review also cites a litter study, which gives no tau_D (only positive responses were significantly conserved); the critic: equating these depths with roughly genus is inconsistent with the review's own statement that a 16S depth cannot be converted into a rank · src: isobePhylogeneticConservationBacterial2019, isobePhylogeneticConservationSoil2020, amendMicrobialResponseSimulated2015 · trail: H1-06 §2. Part A1, §1. What · from: H1-06:B-0080, H1-06:B-0069, H1-06:B-0071, H1-06:B-0024, H1-06:C-054, H1-06:B-0072

### env-preference-depth: Depth of conservation of environmental preferences, overall (Part A1)
needs: ph-preference, moisture-salinity, temperature-optimum, trait-compilations, perturbation-response-depth

- **env-preference-depth.1** For environmental preferences in natural systems, depth of conservation is measured for pH only, from a single source (Ramoneda et al. 2023): signal is significant in 4 of 5 datasets but weak, there is no consenTRAIT-style depth, and families span 3.7 to 4.2 pH units. Moisture and salinity have not been measured in natural systems (the rank-resolved results are engineered: Lennon 2012, Morrissey and Franklin 2015), and temperature is inferred within one phylum (Farrell).
  conf: single (critic: C-001) · class: not stated · rating: "Measured and inconsistent between methods, taxonomies or datasets" (critic: C-012: A1 over-reaches) · holds: natural systems; the critic's split verdict: pH measured, natural, single source, weak signal, no depth; moisture and salinity not measured in natural systems · src: ramonedaBuildingGenomebasedUnderstanding2023, lennonMappingNicheSpace2012, morrisseyEvolutionaryHistoryInfluences2015, farrellBacterialGrowthTemperature2024 · trail: H1-06 §critic, §Verdict as delivered, §6. Verdicts · from: H1-06:A-001, H1-06:A-023, H1-06:C-001..004, H1-06:C-012, H1-06:C-015
- **env-preference-depth.2** The 'inconsistent' label for environmental preferences only emerges when natural evidence is set beside engineered results or a preprint that measures a different quantity (CCA loadings). The body's own synthesis says the natural evidence is one large study (weak signal) plus a preprint on a non-comparable quantity (canonical loadings), and the inconsistency behind the verdict comes from comparing that natural study with engineered isolate and transplant work.
  conf: not stated · class: not stated · holds: the critic's reading of the body; engineered evidence may not carry a natural-system verdict (Common rule 10) · src: ramonedaBuildingGenomebasedUnderstanding2023, chakravertiwuerthweinPhylogeneticCoherenceMicrobiome2026, lennonMappingNicheSpace2012, morrisseyEvolutionaryHistoryInfluences2015 · trail: H1-06 §critic, §Adversarial · from: H1-06:C-005, H1-06:C-013, H1-06:C-014, H1-06:C-033
- **env-preference-depth.3** No consenTRAIT depth for any environmental optimum (pH, temperature or moisture) was found.
  conf: not stated · class: search (note: "Not found by these routes") · search: searched, not found (note: "Not found by these routes: (1) any consenTRAIT tau_D for pH, temperature or moisture optima") · holds: routes: Europe PMC REST keyword, DOI and title search plus fullTextXML; the 'consenTRAIT AND OPEN_ACCESS' query (23 hits screened); WebSearch, among others · src: none (a search result) · trail: H1-06 §2. Part A1, §Provenance, §Verdict as delivered · from: H1-06:A-002, H1-06:B-0028, H1-06:B-0008, H1-06:B-0009
- **env-preference-depth.4** The frequently repeated statement that pH optimum, soil moisture optimum and habitat association sit in deep clades appears in Martiny et al. 2013 as a discussion claim resting on other studies; that paper does not measure any of these. The primary studies it cites were either not obtained (Placella et al. 2012, Philippot et al. 2010) or were read and give a more mixed picture (Lennon et al. 2012).
  conf: not stated · class: assert (note: "asserted, SECONDARY") · holds: a secondary discussion statement · src: martinyPhylogeneticConservatismFunctional2013, placellaRainfallinducedCarbonDioxide2012, philippotEcologicalCoherenceHigh2010, lennonMappingNicheSpace2012 · trail: H1-06 §2. Part A1 · from: H1-06:B-0028..0030
- **env-preference-depth.5** The evidence on environmental preferences does not converge on a single depth. The claim that environmental optima are conserved at deep ranks rests, among full-text sources, on an engineered study of 23 bacterial isolates for moisture and on an asserted secondary statement; natural evidence for environmental optima is thin, and the two coarse-rank optimum results are engineered.
  conf: not stated · class: not stated · holds: the sources the review read for Part A1 · src: lennonMappingNicheSpace2012, martinyPhylogeneticConservatismFunctional2013, morrisseyEvolutionaryHistoryInfluences2015 · trail: H1-06 §2. Part A1, §5. Bounds · from: H1-06:B-0077, H1-06:B-0078, H1-06:B-0163, H1-06:B-0164
- **env-preference-depth.6** By evidence class, the Part A1 sources are: measured (Ramoneda; the preprint Chakraverti-Wuerthwein; engineered: Lennon, Morrissey and Franklin), inferred (Farrell), and modelled or compiled (Goberna and Verdu; Barnum, a preprint).
  conf: not stated · class: not stated · holds: the critic: Goberna and Verdu was not re-opened by the synthesiser and is labelled as carrying no weight, yet it is listed here · src: ramonedaBuildingGenomebasedUnderstanding2023, chakravertiwuerthweinPhylogeneticCoherenceMicrobiome2026, lennonMappingNicheSpace2012, morrisseyEvolutionaryHistoryInfluences2015, farrellBacterialGrowthTemperature2024, gobernaPredictingMicrobialTraits2016, barnumPredictingMicrobialGrowth2024 · trail: H1-06 §Verdict as delivered, §Adversarial · from: H1-06:A-006, H1-06:C-029
- **env-preference-depth.7** Without Ramoneda et al. 2023, the only natural-system depth evidence left for any environmental preference is a single preprint, and Part A1 would move towards 'not measured in this setting' for natural systems.
  conf: not stated · class: not stated · holds: the review's sensitivity analysis · src: ramonedaBuildingGenomebasedUnderstanding2023, chakravertiwuerthweinPhylogeneticCoherenceMicrobiome2026 · trail: H1-06 §Verdict as delivered, §6. Verdicts · from: H1-06:A-007, H1-06:A-008, H1-06:A-024

### metabolic-trait-depth: Depth of conservation of genome-encoded metabolic traits (Part A2)
needs: depth-measures

- **metabolic-trait-depth.1** The Part A2 depths are inferred from genome annotation, not measured phenotypically, except for the Biolog substrates in Martiny 2013.
  conf: not stated · class: deriv (note: "inferred from genome annotation") · holds: genome-encoded metabolic traits · src: martinyPhylogeneticConservatismFunctional2013 · trail: H1-06 §3. Part A2, §Verdict as delivered · from: H1-06:B-0081, H1-06:A-009
- **metabolic-trait-depth.2** On 2,229 SEED genomes (26 phyla, 16S trees), 93% of 89 traits were non-randomly distributed.
  conf: not stated · class: deriv (note: "inferred from genome annotation") · limit: access (note: "I could not re-open Martiny 2013 (Europe PMC fullTextXML empty)") · holds: SEED genomes on 16S trees; rests on two independent search-agent readings · src: martinyPhylogeneticConservatismFunctional2013 · trail: H1-06 §3. Part A2, §Provenance · from: H1-06:B-0081, H1-06:B-0082, H1-06:B-0011
- **metabolic-trait-depth.3** Oxygenic photosynthesis had a median tau_D of about 0.10 to 0.11 (one clade), sulfate reduction 0.039 (20 clusters) and nitrogen fixation about 0.018 (54 clusters).
  conf: not stated · class: deriv (note: "inferred from genome annotation") · limit: access (critic: C-028) · holds: 2,229 SEED genomes, 16S trees; load-bearing in the A2 verdict, but resting on a search agent's transcription that disagrees with another agent on the overall range; the synthesiser could not re-open it and the critic could not obtain it (PMC3603392, not OA) · src: martinyPhylogeneticConservatismFunctional2013 · trail: H1-06 §3. Part A2, §Adversarial, §critic · from: H1-06:B-0081..0084, H1-06:C-007, H1-06:C-028
- **metabolic-trait-depth.4** Growth on each of 70 carbon substrates (Biolog phenotypes, 738 strains) had tau_D below 0.011.
  conf: not stated · class: meas (note: "not measured phenotypically, except for the Biolog substrates") · limit: access (critic: C-028) · holds: Biolog phenotypes of 738 strains; the paper could not be re-opened by the synthesiser or obtained by the critic · src: martinyPhylogeneticConservatismFunctional2013 · trail: H1-06 §3. Part A2, §Adversarial · from: H1-06:B-0085, H1-06:A-009, H1-06:C-028
- **metabolic-trait-depth.5** Martiny et al. report that traits encoded by many genes sit deeper, with aerobic methane oxidation as a stated exception.
  conf: not stated · class: deriv (note: "inferred from genome annotation") · limit: access (note: "I could not re-open Martiny 2013 (Europe PMC fullTextXML empty)") · holds: 2,229 SEED genomes, 16S trees · src: martinyPhylogeneticConservatismFunctional2013 · trail: H1-06 §3. Part A2 · from: H1-06:B-0081, H1-06:B-0082, H1-06:B-0086, H1-06:B-0011
- **metabolic-trait-depth.6** The two search agents transcribed Martiny et al.'s overall tau_D range differently, 0.0011 to 0.101 quoted directly by one and 0.0029 to 0.11 by the other, and the discrepancy is unresolved.
  conf: not stated · class: not stated · limit: access (note: "I could not re-open the paper to resolve this") · holds: the overall range in Martiny et al. 2013; the specific trait values are the load-bearing ones · src: martinyPhylogeneticConservatismFunctional2013 · trail: H1-06 §3. Part A2, §critic · from: H1-06:B-0087, H1-06:B-0088, H1-06:C-007
- **metabolic-trait-depth.7** Single enzymes are shallow: alkaline phosphatase, chitinase and beta-N-acetylglucosaminidase had tau_D 0.0098, 0.0080 and 0.0097, about 98% 16S identity.
  conf: not stated · class: deriv (note: "inferred from genome annotation") · holds: 3,058 sequenced prokaryotic genomes · src: zimmermanMicrodiversityExtracellularEnzyme2013 · trail: H1-06 §3. Part A2, §References · from: H1-06:B-0081, H1-06:B-0089, H1-06:B-0090, H1-06:R-0086
- **metabolic-trait-depth.8** Cellulase had tau_D 0.013 and beta-glucosidase 0.034.
  conf: not stated · class: deriv (note: "inferred from genome annotation") · holds: 5,123 genomes · src: berlemontPhylogeneticDistributionPotential2013 · trail: H1-06 §3. Part A2 · from: H1-06:B-0081, H1-06:B-0091
- **metabolic-trait-depth.9** CAZyme traits had significant signal in most phyla, with depth varying by phylum (conserved-clade 16S divergence of 3 to 10% in Verrucomicrobiota and 0.1 to 0.5% in Firmicutes_A); beta-glucanases were significant in 73% of phyla tested, against 25% for alpha-glucanases.
  conf: single (note: "SINGLE SOURCE") · class: deriv (note: "inferred from genome annotation") · holds: natural; 9,143 high-quality MAGs from the GEM catalogue, GTDB phyla · src: lopezmondejarGlobalDistributionCarbohydrate2022 · trail: H1-06 §3. Part A2 · from: H1-06:B-0081, H1-06:B-0092..0094
- **metabolic-trait-depth.10** The relative ordering of depths replicates across several studies on 16S trees: complex multi-gene pathways are deep (oxygenic photosynthesis about 0.10 to 0.11 16S distance; sulfate reduction 0.039), nitrogen fixation is intermediate (about 0.018), and single enzymes and substrate use are shallow (about 0.008 to 0.034).
  conf: repl (note: "replicates across independent datasets") · class: deriv (note: "inferred from genomes") · holds: 16S trees; the critic: supported, but the load-bearing Martiny 2013 values were not re-checked by the synthesiser, which records an unresolved transcription discrepancy · src: martinyPhylogeneticConservatismFunctional2013, zimmermanMicrodiversityExtracellularEnzyme2013, berlemontPhylogeneticDistributionPotential2013, sunPhylogeneticDistributionPolysaccharideDegrading2021, lopezmondejarGlobalDistributionCarbohydrate2022 · trail: H1-06 §3. Part A2, §Verdict as delivered, §6. Verdicts, §critic · from: H1-06:A-010, H1-06:A-026, H1-06:B-0114, H1-06:A-009, H1-06:C-006, H1-06:C-007

### depth-dataset-dependence: Dependence of absolute depths on genome sampling and tree
needs: metabolic-trait-depth

- **depth-dataset-dependence.1** In 2,730 marine genomes, chitinase tau_D was 0.0281 on a 16S tree and 0.0444 on a core-gene tree, three to five times Zimmerman's 0.008.
  conf: not stated · class: not stated · holds: 2,730 marine genomes; a 16S tree and a core-gene tree · src: sunPhylogeneticDistributionPolysaccharideDegrading2021, zimmermanMicrodiversityExtracellularEnzyme2013 · trail: H1-06 §3. Part A2, §Verdict as delivered · from: H1-06:B-0095, H1-06:A-011
- **depth-dataset-dependence.2** The authors attribute the difference to a denser sample of trait-positive genomes and state that tau_D values from different trees are not comparable.
  conf: not stated · class: not stated · holds: 2,730 marine genomes, 16S and core-gene trees · src: sunPhylogeneticDistributionPolysaccharideDegrading2021 · trail: H1-06 §3. Part A2 · from: H1-06:B-0095, H1-06:B-0096
- **depth-dataset-dependence.3** Depending on the enzyme, 13.5 to 100% of trait-positive genomes were singletons; singleton clusters are common.
  conf: not stated · class: not stated · holds: 2,730 marine genomes · src: sunPhylogeneticDistributionPolysaccharideDegrading2021 · trail: H1-06 §3. Part A2, §5. Bounds · from: H1-06:B-0095, H1-06:B-0097, H1-06:B-0156
- **depth-dataset-dependence.4** Martiny et al. call their estimates "an upper bound for many functions" because many trait carriers sit in clusters of one: tau_D is an upper bound under undersampling, and the original authors call their depths upper bounds because of undersampling.
  conf: not stated · class: not stated · holds: consenTRAIT depths on undersampled trees · src: martinyPhylogeneticConservatismFunctional2013 · trail: H1-06 §3. Part A2, §5. Bounds, §Verdict as delivered · from: H1-06:B-0098, H1-06:B-0155, H1-06:A-013
- **depth-dataset-dependence.5** On gene-content coherence, 44 coherent nodes appeared at 16S distances of 0.03 to 0.25 on a 16S tree but only five deep coherent subtrees on a GTDB 120-protein tree; class Actinobacteria was coherent while the shallower family Enterobacteriaceae was not.
  conf: single (note: "SINGLE SOURCE") · class: not stated · holds: a 16S tree against a GTDB 120-protein tree · src: parrasmoltoAssessmentPhylofunctionalCoherence2021 · trail: H1-06 §3. Part A2, §Verdict as delivered · from: H1-06:B-0099, H1-06:B-0100, H1-06:A-012
- **depth-dataset-dependence.6** For genome-encoded metabolic traits, depth of conservation is measured (inferred from genomes) and inconsistent in absolute depth between datasets and trees, while the relative ordering is consistent: absolute depths move with genome sampling density and tree choice, and their own authors describe them as upper bounds.
  conf: not stated · class: deriv (note: "inferred from genomes") · rating: "Measured and inconsistent between methods, taxonomies or datasets" · holds: the critic: supported by the body, but the load-bearing Martiny 2013 values were not re-checked by the synthesiser · src: sunPhylogeneticDistributionPolysaccharideDegrading2021, parrasmoltoAssessmentPhylofunctionalCoherence2021, martinyPhylogeneticConservatismFunctional2013 · trail: H1-06 §critic, §Verdict as delivered, §6. Verdicts, §3. Part A2 · from: H1-06:A-009, H1-06:A-025, H1-06:A-026, H1-06:B-0115, H1-06:C-006, H1-06:C-007, H1-06:C-011
- **depth-dataset-dependence.7** The 'inconsistent' label for metabolic traits rests mainly on Sun et al. 2021 (dataset and tree dependence of the same trait) together with Parras-Moltó et al. 2021; without Sun, 'measured, with depths, methods and taxonomy stated' would be defensible for the ordering.
  conf: not stated · class: not stated · holds: the review's sensitivity analysis · src: sunPhylogeneticDistributionPolysaccharideDegrading2021, parrasmoltoAssessmentPhylofunctionalCoherence2021 · trail: H1-06 §Verdict as delivered, §6. Verdicts · from: H1-06:A-014, H1-06:A-015, H1-06:A-027

### rank-partitioning: Partitioning genomic traits among taxonomic ranks
needs: depth-measures

- **rank-partitioning.1** With GTDB ranks, ranks together explained 41.4% of the variance in 25 COG categories normalised for genome size: domain 3.2%, phylum 14.6%, class 4.1%, order 9.2%, family 4.8%, genus 5.5%; the contribution is non-monotonic across ranks.
  conf: single (critic: C-035) · class: not stated · holds: 13,735 lineages, GTDB ranks; the critic: correctly flagged single source in the body, but it carries weight in the A2 verdict without that flag · src: royaltyQuantitativelyPartitioningMicrobial2019 · trail: H1-06 §3. Part A2, §Adversarial · from: H1-06:B-0101, H1-06:B-0102, H1-06:C-035, H1-06:A-012
- **rank-partitioning.2** Apparent within-phylum variability rose with the number of lineages sampled and levelled off after about 100 genomes, so undersampled phyla look falsely uniform.
  conf: single (note: "SINGLE SOURCE") · class: not stated · holds: 13,735 lineages, GTDB ranks, COG categories · src: royaltyQuantitativelyPartitioningMicrobial2019 · trail: H1-06 §3. Part A2 · from: H1-06:B-0101, H1-06:B-0103
- **rank-partitioning.3** Autotrophy and maximum growth rate had weaker signal than oxygen tolerance and GC content, and at least 25% of variance in four traits fell at a single split.
  conf: not stated · class: not stated · holds: 50,745 GTDB genomes · src: hoffertConstructingPeriodicTable2026 · trail: H1-06 §3. Part A2 · from: H1-06:B-0104

### genome-incompleteness: Genome incompleteness and conservation estimates
needs: metabolic-trait-depth

- **genome-incompleteness.1** No study found tests directly how genome incompleteness biases tau_D or signal statistics; its effect on depth estimates themselves has not been measured in any source read.
  conf: not stated · class: search (note: "Not found by these routes") · search: searched, not found (note: "(3) any direct test of how genome incompleteness biases tau_D or signal statistics") · holds: the review's search, whose routes are listed in the note's provenance (including WebSearch on genome completeness with functional inference); the critic: the routes behind this not-found are not named in the body · src: none (a search result) · trail: H1-06 §3. Part A2, §5. Bounds, §Provenance, §Adversarial · from: H1-06:B-0105, H1-06:B-0158, H1-06:B-0008, H1-06:B-0009, H1-06:C-051
- **genome-incompleteness.2** Going from 70% to 100% completeness raised KEGG module fullness by 15 ± 10%; the bias was positive for 94% of 195 modules, persisted above 90% completeness, and was largest in Proteobacteria and in modules with few steps.
  conf: single (note: "SINGLE SOURCE") · class: model (note: "modelled on subsampled complete genomes") · holds: subsampled complete genomes · src: eisenhoferImpactMicrobialGenome2023 · trail: H1-06 §3. Part A2 · from: H1-06:B-0107, H1-06:B-0108
- **genome-incompleteness.3** Subsampling a complete Pseudomonas aeruginosa genome to 70% moved its functional profile towards Bacillus subtilis.
  conf: not stated · class: model (note: "modelled on subsampled complete genomes") · holds: one complete genome, subsampled · src: eisenhoferImpactMicrobialGenome2023 · trail: H1-06 §3. Part A2 · from: H1-06:B-0107, H1-06:B-0109
- **genome-incompleteness.4** Removing 1% of sequence from each genome cut detected core gene families by more than 60% across 17 species; relaxing the core threshold to 90 to 95% eased this.
  conf: single (note: "SINGLE SOURCE") · class: model (note: "modelled") · holds: 17 species; modelled · src: liCriticalAssessmentPangenomic2022 · trail: H1-06 §3. Part A2 · from: H1-06:B-0110
- **genome-incompleteness.5** For 116,884 MAGs against RefSeq, raw gene detection rates fell below model-corrected prevalences, and most KEGG orthologs were biased between culture-heavy and MAG references.
  conf: single (critic: C-034) · class: not stated · holds: MAGs against RefSeq references · src: albrightTraitBiasesMicrobial2023 · trail: H1-06 §3. Part A2, §Adversarial · from: H1-06:B-0111, H1-06:C-034
- **genome-incompleteness.6** Incompleteness pushed detected function down in single-source tests of modules, core genes and reference bias, with the size of the effect depending on module and phylum; the evidence is indirect but consistent in direction, and none of it measures the effect on conservation depth.
  conf: single (critic: C-034) · class: not stated · holds: KEGG modules (modelled on subsampled complete genomes), core gene families (modelled) and reference genomes, one source each · src: eisenhoferImpactMicrobialGenome2023, liCriticalAssessmentPangenomic2022, albrightTraitBiasesMicrobial2023 · trail: H1-06 §5. Bounds, §3. Part A2, §Adversarial · from: H1-06:B-0157, H1-06:B-0158, H1-06:B-0106, H1-06:C-034, H1-06:B-0107, H1-06:B-0110
- **genome-incompleteness.7** Consensus-threshold methods such as consenTRAIT (90% sharing) are exposed to false absences, which would fragment clades and push depth estimates shallower.
  conf: not stated · class: reading (note: "Reviewer's reading, not tested by any source") · holds: untested by any source; the critic: appropriately labelled as untested, but then echoed in Section 5 as a bound · src: none (the reviewer's synthesis) · trail: H1-06 §3. Part A2, §Adversarial · from: H1-06:B-0112, H1-06:C-055
- **genome-incompleteness.8** Amino-acid-based optimum predictions stayed stable down to 10% completeness for oxygen, temperature and salinity, while pH error reached 0.4 units.
  conf: not stated · class: not stated · holds: a preprint · src: barnumPredictingMicrobialGrowth2024 · trail: H1-06 §3. Part A2 · from: H1-06:B-0113

### group-size-control: Controlling group number and size across ranks
needs: depth-measures

- **group-size-control.1** Lu et al. handled group number and group size with a null that "shuffled linkages between fine-taxa and broad-taxa level by level (remaining topology)", using 100 random linkage maps (tip-label shuffling for UniFrac); under this null, explained variance "remained constant or slightly decreased" with rank.
  conf: not stated · class: not stated · limit: access (critic: C-017) · holds: the eight soil and seawater datasets Lu et al. reanalysed; the critic could not obtain the Methods and Results (nature.com paywall; not open access), so the null-model description rests on the search agent's reading; the note's provenance says the synthesiser re-opened cached full text for the null model · src: luEvaluatingCommunityenvironmentRelationships2016 · trail: H1-06 §4. Part B, §critic, §Adversarial, §Provenance · from: H1-06:B-0116, H1-06:B-0125, H1-06:B-0126, H1-06:B-0010, H1-06:C-017, H1-06:C-025..027
- **group-size-control.2** By preserving topology, the null holds the count of groups per level and the number of fine taxa per group fixed; it does not hold abundance evenness among groups fixed.
  conf: not stated · class: reading (note: "Reviewer's reading") · holds: Lu et al.'s topology-preserving null; the critic: the caveat about evenness is appropriate, and abundance evenness among groups was not controlled · src: luEvaluatingCommunityenvironmentRelationships2016 · trail: H1-06 §4. Part B, §critic · from: H1-06:B-0129, H1-06:B-0130, H1-06:C-010, H1-06:C-018
- **group-size-control.3** No rank-wise composition-environment study other than Lu 2016 was found that controls group number and size; Schmidt 2014 controls them, but for identity thresholds and annotation consistency, not ranks.
  conf: not stated · class: search (note: "Not found by these routes") · search: searched, not found (note: "(2) any rank-wise composition-environment study, other than Lu 2016, that controls group number and size") · holds: routes include citing papers of Lu et al. 2016 screened by title, and WebSearch on taxonomic sufficiency, taxonomic resolution with explained variation and ecological coherence with ranks · src: none (a search result) · trail: H1-06 §Provenance · from: H1-06:B-0008, H1-06:B-0009

### rankwise-structuring: Environmental structuring of community composition from fine to coarse ranks (Part B)
needs: group-size-control

- **rankwise-structuring.1** Across eight reanalysed datasets, environment-explained variance of Bray-Curtis composition (db-RDA adjusted R2) "either increased or remained constant with broadening taxonomic resolution from species to order or even phylum level".
  conf: single (critic: C-008) · class: meas (note: "measured, natural") · holds: natural; four surface soils (n = 40 to 580) and four seawater datasets; closed-reference Greengenes 13_8 with copy-number correction, composition aggregated from otu97 to otu70 and from species to phylum; the critic confirmed this abstract sentence · src: luEvaluatingCommunityenvironmentRelationships2016 · trail: H1-06 §4. Part B, §critic, §Verdict as delivered · from: H1-06:B-0116..0119, H1-06:C-016, H1-06:A-017
- **rankwise-structuring.2** In all four soils, R2 rose up to class (otu82 to otu76) and fell at phylum, with at least a 50% R2 increase from otu97 to otu94; pH was the strongest single variable.
  conf: single (critic: C-008) · class: meas (note: "measured, natural") · limit: access (critic: C-017) · holds: four surface soils, Greengenes 13_8; the critic: the soil class-peak details rest on the search agent's reading, since the critic could confirm only the abstract · src: luEvaluatingCommunityenvironmentRelationships2016 · trail: H1-06 §4. Part B, §critic, §Adversarial · from: H1-06:B-0116, H1-06:B-0117, H1-06:B-0121, H1-06:A-018, H1-06:C-008, H1-06:C-017, H1-06:C-025
- **rankwise-structuring.3** In seawater the shape varied by dataset: peaks at intermediate ranks (Tara surface and DCM), flat from species to order then a drop at class and phylum (English Channel time series), and a continuous rise to phylum (East China Sea shelf).
  conf: single (critic: C-008) · class: meas (note: "measured, natural") · limit: access (critic: C-026) · holds: four seawater datasets; the critic could confirm only the abstract, not the per-dataset seawater shapes · src: luEvaluatingCommunityenvironmentRelationships2016 · trail: H1-06 §4. Part B, §Adversarial · from: H1-06:B-0116, H1-06:B-0120, H1-06:B-0122..0124, H1-06:A-019, H1-06:C-008, H1-06:C-025, H1-06:C-026
- **rankwise-structuring.4** In soils, the observed genus-to-class R2 was significantly above the topology-preserving shuffle null, which itself gave constant or slightly falling R2; the authors read the rise as phylogenetic niche conservatism.
  conf: single (critic: C-008) · class: meas (note: "measured, natural") · limit: access (critic: C-017) · holds: four surface soils; the critic could not obtain the Methods and Results · src: luEvaluatingCommunityenvironmentRelationships2016 · trail: H1-06 §4. Part B, §Verdict as delivered, §critic · from: H1-06:B-0116, H1-06:B-0127, H1-06:B-0128, H1-06:A-020, H1-06:C-008, H1-06:C-017
- **rankwise-structuring.5** Environmental structuring of community composition across ranks has been measured with group number (and member count) controlled, in a single source, conditional on that paper's null design: explained variance rises or stays constant from species to order, with dataset-specific falls at class or phylum (in soils it peaks at class and declines at phylum; in seawater the pattern varies by dataset); abundance evenness among groups was not controlled.
  conf: single (critic: C-008) · class: not stated · rating: "Measured with group number and size controlled, SINGLE SOURCE" (critic: C-008: conditional on that paper's null design, which could not be re-verified) · limit: access (critic: C-008) · holds: natural; 4 soil and 4 seawater datasets; Greengenes 13_8 ranks and OTU thresholds from 97% to 70%; the critic: the review departs from the brief's expectation that such evidence may not exist, plausibly, but on one source whose control design was not independently re-verified · src: luEvaluatingCommunityenvironmentRelationships2016 · trail: H1-06 §Verdict as delivered, §6. Verdicts, §critic, §Adversarial · from: H1-06:A-016, H1-06:A-028, H1-06:A-029, H1-06:C-008..011, H1-06:C-057..061, H1-06:B-0131, H1-06:B-0161
- **rankwise-structuring.6** Without Lu et al. 2016, the Part B verdict falls to 'measured without controlling group number and size'.
  conf: not stated · class: not stated · holds: the review's sensitivity analysis · src: luEvaluatingCommunityenvironmentRelationships2016 · trail: H1-06 §Verdict as delivered, §6. Verdicts · from: H1-06:A-022, H1-06:A-030
- **rankwise-structuring.7** Across 160 natural sites, habitat category explained little composition variance at any level and peaked at class (PERMANOVA R2: phylum 3.7%, class 6.3%, ASV 2.7%).
  conf: not stated · class: not stated · holds: soils at 160 natural sites in southwest France; gyrB taxonomy; a preprint; group numbers ranged from 18 phyla to 769 ASVs and were not controlled · src: mayjonadeRelativeEffectsAbiotic2024 · trail: H1-06 §4. Part B, §Verdict as delivered, §References · from: H1-06:B-0132, H1-06:B-0133, H1-06:B-0135, H1-06:A-021, H1-06:R-0149
- **rankwise-structuring.8** The share of individual groups significantly associated with soil physicochemistry fell from 59% at phylum to 30.2% at ASV, while plant-community associations rose from 19.7% to 48.7%.
  conf: not stated · class: not stated · holds: 160 natural sites in southwest France; gyrB taxonomy; a preprint; group numbers not controlled · src: mayjonadeRelativeEffectsAbiotic2024 · trail: H1-06 §4. Part B · from: H1-06:B-0132, H1-06:B-0134, H1-06:B-0135
- **rankwise-structuring.9** Community turnover was stronger at ASV resolution (an 82% drop in similarity over 160 km, against 50 to 60% for clustered or filtered data), but "less variation in community composition could be explained and partitioned for the high-resolution data set", and the rank order of predictors changed. The comparison is of the high-resolution set against clustered and/or rare-taxon-filtered data, by incidence-based variation partitioning.
  conf: not stated · class: not stated · holds: soils in the Negev; no ranks, only sequence-identity thresholds; one of the uncontrolled rank-wise studies · src: baySoilBacterialCommunities2020 · trail: H1-06 §4. Part B, §critic, §References · from: H1-06:B-0136, H1-06:B-0137, H1-06:C-020, H1-06:R-0151, H1-06:B-0023, H1-06:B-0162, H1-06:A-021
- **rankwise-structuring.10** The pH-aligned first canonical axis stayed stable when OTUs were summed to genus, family and higher, while secondary axes were incoherent across resolutions.
  conf: not stated · class: not stated · holds: a global preprint on topsoil (N = 217) and ocean (N = 125) 16S surveys; the null there does not preserve group structure; tau_D values appear only in figures · src: chakravertiwuerthweinPhylogeneticCoherenceMicrobiome2026 · trail: H1-06 §4. Part B, §2. Part A1, §Adversarial · from: H1-06:B-0139, H1-06:B-0140, H1-06:B-0040, H1-06:C-030
- **rankwise-structuring.11** In an 11-year coastal time series, seasonal niches were coherent for some genera and families, but classes (Alphaproteobacteria, Gammaproteobacteria, Bacteroidia) were non-seasonal when aggregated; within at least three genera, niche similarity fell with 16S divergence.
  conf: not stated · class: not stated · holds: marine bacteria in an 11-year coastal time series, not a spatial environment gradient; aggregation used random 80% ASV subsets, but group number was not equalised · src: auladellSeasonalNicheDifferentiation2021 · trail: H1-06 §4. Part B, §Verdict as delivered, §References · from: H1-06:B-0141, H1-06:B-0142, H1-06:A-021, H1-06:R-0159
- **rankwise-structuring.12** The rank-wise studies other than Lu et al. 2016 are uncontrolled for group number and size, and two are preprints; they agree in part and conflict in part with it.
  conf: not stated · class: not stated · holds: Mayjonade 2024, Bay 2020, Chakraverti-Wuerthwein 2026 and Auladell 2022 · src: mayjonadeRelativeEffectsAbiotic2024, baySoilBacterialCommunities2020, chakravertiwuerthweinPhylogeneticCoherenceMicrobiome2026, auladellSeasonalNicheDifferentiation2021 · trail: H1-06 §5. Bounds, §Verdict as delivered · from: H1-06:B-0161, H1-06:B-0162, H1-06:A-021
- **rankwise-structuring.13** The rise in explained variance from otu97 to otu94 rests on Lu et al. 2016 alone: Bay et al. compare ASVs against clustered and/or filtered data, a different step, although its direction matches.
  conf: single (critic: C-032) · class: not stated · holds: the otu97-to-otu94 and genus rise in soils · src: luEvaluatingCommunityenvironmentRelationships2016, baySoilBacterialCommunities2020 · trail: H1-06 §4. Part B, §Adversarial · from: H1-06:B-0138, H1-06:C-032, H1-06:B-0121

### adjacent-metrics: Rank-wise metrics other than composition-environment R2
needs: rankwise-structuring

- **adjacent-metrics.1** pH explained more of betaNTI (phylogenetic turnover, not composition) at ASV level (R2 0.20) than at OTU97 (0.08).
  conf: not stated · class: not stated · holds: Antarctic wetlands; unit counts uncontrolled · src: quirogaEcologicalAssemblyBacterial2022 · trail: H1-06 §4. Part B · from: H1-06:B-0143, H1-06:B-0144
- **adjacent-metrics.2** Abundance-occupancy relationships were weakest at species and roughly constant from genus to phylum.
  conf: not stated · class: not stated · holds: marine bacterioplankton in an estuary · src: izabelshenAbundanceOccupancyRelationshipsAlong2021 · trail: H1-06 §4. Part B, §References · from: H1-06:B-0143, H1-06:B-0145, H1-06:R-0164
- **adjacent-metrics.3** Across about one million full-length 16S sequences, the ecological consistency of habitat annotations, scored against random partitions with the same cluster count and size distribution, generally fell as OTU thresholds became stricter (finer) for complete and average linkage; single linkage behaved differently.
  conf: not stated · class: deriv (note: "inferred, identity thresholds only, not ranks") · holds: identity thresholds only, not ranks; the design controls group number and size, but the response is annotation consistency, not environment-explained composition · src: schmidtEcologicalConsistencySSU2014 · trail: H1-06 §4. Part B · from: H1-06:B-0146..0148

### rank-depth-relation: How rank-wise structuring relates to trait depth
needs: rankwise-structuring, perturbation-response-depth, ph-preference, moisture-salinity

- **rank-depth-relation.1** The rise in explained variance from otu97 to about otu94 and genus matches where perturbation responses cluster (tau_D about 0.017 to 0.02), and the fall at phylum in soils and the class-level incoherence in a time series match the weak within-phylum pH signal and the opposing responses inside coarse groups.
  conf: not stated · class: reading (note: "reviewer's reading") · holds: the critic: it links a natural-system composition result to engineered perturbation-response depths, breaking the natural/engineered separation, and presents a correspondence the sources do not test · src: luEvaluatingCommunityenvironmentRelationships2016, isobePhylogeneticConservationBacterial2019, isobePhylogeneticConservationSoil2020, auladellSeasonalNicheDifferentiation2021, ramonedaBuildingGenomebasedUnderstanding2023 · trail: H1-06 §4. Part B, §Adversarial · from: H1-06:B-0149, H1-06:B-0150, H1-06:C-053
- **rank-depth-relation.2** None of the studies links composition structure to genome content, and an association between environment and composition at a rank is not evidence about the genomes of that rank.
  conf: not stated · class: not stated · holds: the rank-wise composition studies the review read · src: none (the reviewer's synthesis) · trail: H1-06 §4. Part B · from: H1-06:B-0151

## Do not say

- **dns.1** "Environmental preferences are measured and inconsistent between methods, taxonomies or datasets in natural systems."
  why: The A1 verdict over-reaches: the inconsistency only emerges when the one natural study is set beside engineered results or a preprint that measures a different quantity, so it should not stand as the natural-system verdict, and engineered evidence may not carry a natural-system verdict. · instead: env-preference-depth.1, env-preference-depth.2 · trail: H1-06 §critic, §Adversarial · from: H1-06:A-001, H1-06:A-023, H1-06:C-005, H1-06:C-012, H1-06:C-014, H1-06:C-033
- **dns.2** "ASVs within single families spanned four or more pH units, in Xanthobacteraceae in soil and Chitinophagaceae in freshwater."
  why: The family claim is partly wrong: Chitinophagaceae spans 4.63 to 8.35, 3.72 units, so it does not span four units. · instead: ph-preference.2 · trail: H1-06 §critic, §Adversarial · from: H1-06:B-0035, H1-06:C-022, H1-06:C-036
- **dns.3** "pH optimum, soil moisture optimum and habitat association are conserved in deep clades."
  why: The statement appears in Martiny et al. 2013 as a discussion claim resting on other studies, and that paper does not measure any of these. · instead: env-preference-depth.4, env-preference-depth.5 · trail: H1-06 §2. Part A1 · from: H1-06:B-0028, H1-06:B-0029
- **dns.4** "Perturbation responses are conserved at about genus level."
  why: The equation of tau_D 0.016 to 0.020 with roughly genus is attributed to the authors, but the review's own Section 1 says a 16S depth cannot be converted into a rank. · instead: perturbation-response-depth.1, perturbation-response-depth.9 · trail: H1-06 §Adversarial · from: H1-06:B-0080, H1-06:C-054
- **dns.5** "Coarse taxonomic groups contain opposing finer responses."
  why: It is phrased as a general bound but rests on one N-addition study plus a time series, and that N-addition study also reports consistent coarse-rank responses (phylum Actinobacteria positive; classes Betaproteobacteria and Deltaproteobacteria negative). · instead: perturbation-response-depth.5, perturbation-response-depth.6 · trail: H1-06 §Adversarial, §critic · from: H1-06:B-0159, H1-06:C-024, H1-06:C-031
- **dns.6** "Genome incompleteness pushes detected function down."
  why: It is phrased generally, but each quantitative element is single source (modules, core genes, reference bias), and none measures the effect on conservation depth. · instead: genome-incompleteness.6 · trail: H1-06 §Adversarial · from: H1-06:B-0157, H1-06:C-034
- **dns.7** "Genome incompleteness makes consenTRAIT depth estimates shallower."
  why: That consensus-threshold methods would push depth estimates shallower under incompleteness is the reviewer's untested reading, echoed in Section 5 as a bound. · instead: genome-incompleteness.7, genome-incompleteness.1 · trail: H1-06 §Adversarial · from: H1-06:B-0112, H1-06:C-055
- **dns.8** "Rank-wise partitioning of genomic traits is non-monotonic."
  why: The Royalty and Steen rank partition is a single source, correctly flagged in the body, but it carries weight in the A2 verdict without that flag. · instead: rank-partitioning.1 · trail: H1-06 §Adversarial · from: H1-06:A-012, H1-06:C-035
- **dns.9** "97% OTUs explained more composition variance than ASVs."
  why: Bay et al. compare the high-resolution set against filtered ones (clustered and/or rare-taxon-filtered data) using incidence-based variation partitioning, so the paraphrase reduces a clustering-plus-filtering contrast to clustering alone. · instead: rankwise-structuring.9 · trail: H1-06 §critic · from: H1-06:A-021, H1-06:C-019, H1-06:C-020
- **dns.10** "The rise in explained variance from otu97 to otu94 is replicated across studies."
  why: The rise rests on Lu 2016 alone; the other study cited for it compares ASVs against clustered and/or filtered data, a different step. · instead: rankwise-structuring.13 · trail: H1-06 §Adversarial · from: H1-06:B-0149, H1-06:C-032
- **dns.11** "Rank-wise structuring of composition corresponds to the depth at which perturbation responses are conserved, at about genus."
  why: It links a natural-system composition result to engineered perturbation-response depths, which breaks the natural/engineered separation, and presents a correspondence the sources do not test. · instead: rank-depth-relation.1 · trail: H1-06 §Adversarial · from: H1-06:B-0149, H1-06:C-053

## Gaps

- **gap.1** A large-scale study of community conservatism across microbial phyla and environments, from the von Mering group, which may directly address rank-wise environmental coherence with null partitions (Malfertheiner, Tackmann, Rodrigues, von Mering, bioRxiv; appears published January 2026, open access).
  blocks: rankwise-structuring, group-size-control · origin: critic coverage gap; recorded by the stage-2 check for a human to weigh · search: not stated · src: malfertheinerCommunityConservatismWidespread2024 · from: H1-06:C-045, H1-06:B-0019
- **gap.2** Archaeal results: every depth and rank-wise result is bacterial, although the brief says any prokaryote (for example Thaumarchaeota/Nitrososphaeria pH and ammonia-oxidiser niche depth; halophilic and thermophilic archaea).
  blocks: env-preference-depth, metabolic-trait-depth, rankwise-structuring · origin: critic coverage gap · search: not stated · from: H1-06:C-046, H1-06:B-0019
- **gap.3** Marine cyanobacterial ecotypes, where light and temperature optima are measured on isolates and mapped onto a phylogeny against field distributions: the classic natural-system case for depth of environmental preference (Prochlorococcus and Synechococcus; Johnson et al. 2006; Martiny, Tai and others 2009).
  blocks: env-preference-depth · origin: critic coverage gap · search: not stated · src: johnson2006, martiny2009 · from: H1-06:C-047, H1-06:B-0019
- **gap.4** Trait databases compiling isolate growth optima (pH, temperature, salinity, oxygen) with phylogenetic signal statistics, other than the preprint Barnum and the non-re-opened Goberna (Madin et al. 2020; BacDive-based signal analyses; Sauer and Wang 2019).
  blocks: trait-compilations, env-preference-depth · origin: critic coverage gap · search: not stated · src: madin2020, sauer2019 · from: H1-06:C-048, H1-06:B-0019
- **gap.5** Habitat-preference coherence across 16S clusters from global sequence-habitat compilations, other than Schmidt 2014 (Chaffron et al. 2010; Tamames et al. 2016; Auguet, Barberan and Casamayor 2010, archaeal habitat preference).
  blocks: adjacent-metrics, rankwise-structuring · origin: critic coverage gap · search: not stated · src: chaffron2010, tamames2016, auguet2010 · from: H1-06:C-049
- **gap.6** Soil moisture optimum in natural systems: only an engineered isolate study was read; natural rewetting and drought field studies were not obtained (Placella, Evans and Wallenstein), and no alternative routes are named, such as author repositories or eScholarship for UC-affiliated authors.
  blocks: moisture-salinity, env-preference-depth · origin: critic coverage gap; sources not obtained · search: not stated · src: placellaRainfallinducedCarbonDioxide2012, evansClimateChangeAlters2013 · from: H1-06:C-050, H1-06:B-0019
- **gap.7** A direct test of how genome incompleteness biases tau_D or phylogenetic signal, for example in MAG-based consenTRAIT or signal analyses (GEM catalogue, GTDB MAG-inclusive trees).
  blocks: genome-incompleteness · origin: not found in the review's search; critic coverage gap, which also says the routes behind the not-found are not named in the body · search: searched, not found (note: "(3) any direct test of how genome incompleteness biases tau_D or signal statistics") · from: H1-06:C-051, H1-06:B-0009, H1-06:B-0019
- **gap.8** Rank-wise community-environment results under GTDB against SILVA or Greengenes for the same analysis (db-RDA or PERMANOVA re-run under alternative taxonomies): only the metabolic-coherence comparison of Parras-Moltó is given.
  blocks: rankwise-structuring · origin: critic coverage gap · search: not stated · from: H1-06:C-052
- **gap.9** Martiny et al. 2013's trait values and overall tau_D range: not re-checked at synthesis or by the critic, with an unresolved transcription discrepancy between the two search agents.
  blocks: metabolic-trait-depth · origin: critic full-text breach; source not re-opened (Europe PMC fullTextXML empty; not OA) · search: not stated · src: martinyPhylogeneticConservatismFunctional2013 · from: H1-06:C-028, H1-06:B-0011, H1-06:B-0087, H1-06:B-0088
- **gap.10** Whether Lu et al. 2016's null holds group number and member count fixed, and its soil class peak, 50% otu97-to-otu94 rise and per-dataset seawater shapes: the critic could confirm only the abstract.
  blocks: group-size-control, rankwise-structuring · origin: critic full-text breach; Methods and Results paywalled · search: not stated · src: luEvaluatingCommunityenvironmentRelationships2016 · from: H1-06:C-025..027, H1-06:C-060
- **gap.11** Goberna and Verdu 2016's figures and internal-inconsistency claim, read in full by one agent only and not re-opened.
  blocks: trait-compilations · origin: critic full-text breach; publisher bot challenge · search: not stated · src: gobernaPredictingMicrobialTraits2016 · from: H1-06:C-029, H1-06:B-0012
- **gap.12** Numeric tau_D values for the canonical-axis signal in Chakraverti-Wuerthwein et al. 2026, which appear only in figures.
  blocks: ph-preference, rankwise-structuring · origin: critic full-text breach · search: not stated · src: chakravertiwuerthweinPhylogeneticCoherenceMicrobiome2026 · from: H1-06:C-030
- **gap.13** A rank-wise composition-environment study other than Lu 2016 that controls group number and size.
  blocks: rankwise-structuring · origin: not found in the review's search · search: searched, not found (note: "(2) any rank-wise composition-environment study, other than Lu 2016, that controls group number and size") · from: H1-06:B-0009
- **gap.14** A consenTRAIT tau_D for pH, temperature or moisture optima.
  blocks: env-preference-depth · origin: not found in the review's search · search: searched, not found (note: "(1) any consenTRAIT tau_D for pH, temperature or moisture optima") · from: H1-06:B-0009
- **gap.15** Publication status of the preprints Barnum 2024 and Mayjonade 2024.
  blocks: trait-compilations, rankwise-structuring · origin: unverified at synthesis · search: not stated · src: barnumPredictingMicrobialGrowth2024, mayjonadeRelativeEffectsAbiotic2024 · from: H1-06:B-0016
- **gap.16** A rank-wise study that controls abundance evenness among groups as well as group number and size.
  blocks: group-size-control · origin: the review's own caveat on Lu et al.'s null, endorsed by the critic · search: not stated · from: H1-06:B-0130, H1-06:C-010, H1-06:C-018

## Out of scope

- H1-06:C-037..044: reference corrections and Crossref checks, applied in Sources

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
  note = {access: full_text (two independent search-agent readings; not re-opened at synthesis, Europe PMC fullTextXML empty; the critic could not obtain it either); cited as: H1-06 [1]; the critic: Crossref issued date 2012-12-13 (online), print 2013}
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
  note = {access: full_text (search agents' reads); cited as: H1-06 [2]}
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
  note = {access: full_text (search agents' reads); cited as: H1-06 [3]}
}
@article{sunPhylogeneticDistributionPolysaccharideDegrading2021,
  author = {Sun, Zhong-Zhi and Ji, Bo-Wen and Zheng, Ning and Wang, Meng and Cao, Ye and Wan, Lu and Li, Yi-Song and Rong, Jin-Cheng and He, Hai-Lun and Chen, Xiu-Lan and Zhang, Yu-Zhong and Xie, Bin-Bin},
  title = {Phylogenetic distribution of polysaccharide-degrading enzymes in marine bacteria},
  journal = {Frontiers in Microbiology},
  year = {2021},
  volume = {12},
  pages = {658620},
  doi = {10.3389/fmicb.2021.658620},
  note = {access: full_text (search agents' reads); cited as: H1-06 [4]}
}
@article{lopezmondejarGlobalDistributionCarbohydrate2022,
  author = {López-Mondéjar, Rubén and Tláskal, Vojtěch and da Rocha, Ulisses Nunes and Baldrian, Petr},
  title = {Global distribution of carbohydrate utilization potential in the prokaryotic tree of life},
  journal = {mSystems},
  year = {2022},
  volume = {7},
  number = {6},
  pages = {e00829-22},
  doi = {10.1128/msystems.00829-22},
  note = {access: full_text (search agents' reads); cited as: H1-06 [5]}
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
  note = {access: full_text (search agents' reads); cited as: H1-06 [6]; erratum mSphere 4(5): e00637-19 replaces Table S2 only}
}
@article{royalty2019,
  author = {Royalty, Taylor M. and Steen, Andrew D.},
  journal = {mSphere},
  year = {2019},
  volume = {4},
  number = {5},
  pages = {e00637-19},
  doi = {10.1128/mSphere.00637-19},
  note = {access: not stated; erratum to H1-06 [6], replacing Table S2 only, verified by the critic; not cited; incomplete: title}
}
@article{parrasmoltoAssessmentPhylofunctionalCoherence2021,
  author = {Parras-Moltó, Marcos and Aguirre de Cárcer, Daniel},
  title = {Assessment of phylo-functional coherence along the bacterial phylogeny and taxonomy},
  journal = {Scientific Reports},
  year = {2021},
  volume = {11},
  number = {1},
  pages = {8299},
  doi = {10.1038/s41598-021-87909-1},
  note = {access: full_text (search agents' reads); cited as: H1-06 [7]}
}
@article{hoffertConstructingPeriodicTable2026,
  author = {Hoffert, Michael and Gorman, Evan and Lladser, Manuel E. and Fierer, Noah},
  title = {Constructing a "periodic table" of bacteria to map diversity in trait space},
  journal = {The ISME Journal},
  year = {2026},
  volume = {20},
  number = {1},
  pages = {wraf289},
  doi = {10.1093/ismejo/wraf289},
  note = {access: full_text (search agents' reads); cited as: H1-06 [8]}
}
@article{eisenhoferImpactMicrobialGenome2023,
  author = {Eisenhofer, Raphael and Odriozola, Iñaki and Alberdi, Antton},
  title = {Impact of microbial genome completeness on metagenomic functional inference},
  journal = {ISME Communications},
  year = {2023},
  volume = {3},
  number = {1},
  pages = {12},
  doi = {10.1038/s43705-023-00221-z},
  note = {access: full_text (search agents' reads); cited as: H1-06 [9]}
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
  note = {access: full_text (search agents' reads); cited as: H1-06 [10]}
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
  note = {access: full_text (search agents' reads); cited as: H1-06 [11]}
}
@misc{barnumPredictingMicrobialGrowth2024,
  author = {Barnum, Tyler P. and Crits-Christoph, Alexander and Molla, Michael and Carini, Paul and Lee, Henry H. and Ostrov, Nili},
  title = {Predicting microbial growth conditions from amino acid composition},
  howpublished = {bioRxiv 2024.03.22.586313},
  year = {2024},
  doi = {10.1101/2024.03.22.586313},
  note = {access: full_text (read as preprint, version posted 22 March 2024); type: preprint, not peer reviewed; publication status unverified; cited as: H1-06 [12]}
}
@article{ramonedaBuildingGenomebasedUnderstanding2023,
  author = {Ramoneda, Josep and Stallard-Olivera, Elias and Hoffert, Michael and Winfrey, Claire C. and Stadler, Masumi and Niño-García, Juan Pablo and Fierer, Noah},
  title = {Building a genome-based understanding of bacterial pH preferences},
  journal = {Science Advances},
  year = {2023},
  volume = {9},
  number = {17},
  pages = {eadf8998},
  doi = {10.1126/sciadv.adf8998},
  note = {access: full_text (re-opened from cache at synthesis); cited as: H1-06 [13]}
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
  note = {access: full_text (re-opened from cache at synthesis); cited as: H1-06 [14]; the note gives Schoolmaster, Donald R., Jr.; Crossref has no Jr. suffix (critic C-040)}
}
@article{morrisseyEvolutionaryHistoryInfluences2015,
  author = {Morrissey, Ember M. and Franklin, Rima B.},
  title = {Evolutionary history influences the salinity preference of bacterial taxa in wetland soils},
  journal = {Frontiers in Microbiology},
  year = {2015},
  volume = {6},
  pages = {1013},
  doi = {10.3389/fmicb.2015.01013},
  note = {access: full_text (search agents' reads); cited as: H1-06 [15]}
}
@article{gobernaPredictingMicrobialTraits2016,
  author = {Goberna, Marta and Verdú, Miguel},
  title = {Predicting microbial traits with phylogenies},
  journal = {The ISME Journal},
  year = {2016},
  volume = {10},
  number = {4},
  pages = {959--967},
  doi = {10.1038/ismej.2015.171},
  note = {access: full_text (read in full by one search agent only; not re-opened at synthesis, publisher bot challenge); cited as: H1-06 [16]; also listed under Sources not obtained, a conflict between the note's lists; the critic: Crossref online 2015}
}
@article{farrellBacterialGrowthTemperature2024,
  author = {Farrell, Anne A. and Nesbø, Camilla L. and Zhaxybayeva, Olga},
  title = {Bacterial growth temperature as a horizontally acquired polygenic trait},
  journal = {Genome Biology and Evolution},
  year = {2025},
  volume = {17},
  number = {1},
  pages = {evae277},
  doi = {10.1093/gbe/evae277},
  note = {access: full_text (search agents' reads); cited as: H1-06 [17]; issued online 2024-12-26, volume 17 of 2025}
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
  note = {access: full_text (search agents' reads); cited as: H1-06 [18]}
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
  note = {access: full_text (search agents' reads; figures verified by the critic); cited as: H1-06 [19]}
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
  note = {access: full_text (search agents' reads); cited as: H1-06 [20]}
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
  note = {access: full_text (search agents' reads); cited as: H1-06 [21]; the not-obtained list heads an entry "Amend et al. 2016 and Placella-type drought or rewetting studies", a possible conflict between the note's lists}
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
  note = {access: full_text (search agents' reads); cited as: H1-06 [22]}
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
  note = {access: full_text (re-opened from cache at synthesis; the critic could confirm only the abstract, nature.com paywall, PMC5148199 not open access); cited as: H1-06 [23]}
}
@misc{mayjonadeRelativeEffectsAbiotic2024,
  author = {Mayjonade, Baptiste and Zamar, Rémy and Carrere, Sébastien and Roux, Fabrice},
  title = {The relative effects of abiotic and biotic factors in explaining the structure of soil bacterial communities at diverse taxonomic levels},
  howpublished = {bioRxiv 2024.10.29.620845},
  year = {2024},
  doi = {10.1101/2024.10.29.620845},
  note = {access: full_text (read as preprint, version posted 3 November 2024; re-opened from cache at synthesis); type: preprint, not peer reviewed; publication status unverified; cited as: H1-06 [24]}
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
  note = {access: full_text (re-opened from cache at synthesis; read in full by the critic); cited as: H1-06 [25]}
}
@article{quirogaEcologicalAssemblyBacterial2022,
  author = {Quiroga, María V. and Valverde, Angel and Mataloni, Gabriela and Casa, Valeria and Stegen, James C. and Cowan, Don},
  title = {The ecological assembly of bacterial communities in Antarctic wetlands varies across levels of phylogenetic resolution},
  journal = {Environmental Microbiology},
  year = {2022},
  volume = {24},
  number = {8},
  pages = {3486--3499},
  doi = {10.1111/1462-2920.15912},
  note = {access: full_text (re-opened from cache at synthesis); cited as: H1-06 [26]}
}
@article{schmidtEcologicalConsistencySSU2014,
  author = {Schmidt, Thomas S. B. and Matias Rodrigues, João F. and von Mering, Christian},
  title = {Ecological consistency of SSU rRNA-based operational taxonomic units at a global scale},
  journal = {PLoS Computational Biology},
  year = {2014},
  volume = {10},
  number = {4},
  pages = {e1003594},
  doi = {10.1371/journal.pcbi.1003594},
  note = {access: full_text (search agents' reads); cited as: H1-06 [27]}
}
@article{auladellSeasonalNicheDifferentiation2021,
  author = {Auladell, Adrià and Barberán, Albert and Logares, Ramiro and Garcés, Esther and Gasol, Josep M. and Ferrera, Isabel},
  title = {Seasonal niche differentiation among closely related marine bacteria},
  journal = {The ISME Journal},
  year = {2022},
  volume = {16},
  number = {1},
  pages = {178--189},
  doi = {10.1038/s41396-021-01053-2},
  note = {access: full_text (search agents' reads); cited as: H1-06 [28]; the critic: Crossref online 2021-07-20}
}
@misc{chakravertiwuerthweinPhylogeneticCoherenceMicrobiome2026,
  author = {Chakraverti-Wuerthwein, Milena S. and Domenig, Alissa and Kuehn, Seppe},
  title = {Phylogenetic coherence in microbiome composition across environmental gradients},
  howpublished = {bioRxiv 2026.06.07.730742},
  year = {2026},
  doi = {10.64898/2026.06.07.730742},
  note = {access: full_text (read as preprint v1, posted 11 June 2026); type: preprint, not peer reviewed; cited as: H1-06 [29]}
}
@article{izabelshenAbundanceOccupancyRelationshipsAlong2021,
  author = {Izabel-Shen, Dandan and Höger, Anna-Lena and Jürgens, Klaus},
  title = {Abundance-occupancy relationships along taxonomic ranks reveal a consistency of niche differentiation in marine bacterioplankton with distinct lifestyles},
  journal = {Frontiers in Microbiology},
  year = {2021},
  volume = {12},
  pages = {690712},
  doi = {10.3389/fmicb.2021.690712},
  note = {access: full_text (published version); cited as: H1-06 [30]}
}
@misc{izabelshenAbundanceoccupancyRelationshipsAlong2021,
  author = {Izabel-Shen, Dandan and others},
  howpublished = {bioRxiv},
  year = {2021},
  doi = {10.1101/2021.04.09.439152},
  note = {access: full_text (read by one search agent); type: preprint of H1-06 [30]; not cited; incomplete: title, author}
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
  note = {access: not_obtained (Europe PMC not OA; PMC reCAPTCHA; pnas.org 403)}
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
  note = {access: not_obtained (Europe PMC no OA; web search showed only the abstract)}
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
  note = {access: not_obtained (Europe PMC not OA; web search; author site not followed within budget)}
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
  note = {access: not_obtained (paywalled; Unpaywall, Notre Dame PDF 403, OSTI refused)}
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
  note = {access: not_obtained (Europe PMC metadata only); listed twice under Sources not obtained}
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
  note = {access: not_obtained (Europe PMC metadata only)}
}
@article{barberanWhyAreMicrobes2014,
  author = {Barberán, Albert and Ramirez, Kelly S. and Leff, Jonathan W. and Bradford, Mark A. and Wall, Diana H. and Fierer, Noah},
  title = {Why are some microbes more ubiquitous than others? Predicting the habitat breadth of soil bacteria},
  journal = {Ecology Letters},
  year = {2014},
  volume = {17},
  number = {7},
  pages = {794--802},
  doi = {10.1111/ele.12282},
  note = {access: not_obtained (Europe PMC metadata only)}
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
  note = {access: not_obtained (Europe PMC not OA; OSTI timeout and refused)}
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
  note = {access: not_obtained (Europe PMC fullTextXML empty; ASM 403)}
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
  note = {access: not_obtained (nature.com auth redirect); author list not verified; incomplete: author}
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
  note = {access: not_obtained (Europe PMC metadata only, no PMCID)}
}
@article{nelsonGlobalBiogeographyMicrobial2016,
  author = {Nelson, Michaeline B. and Martiny, Adam C. and Martiny, Jennifer B. H.},
  title = {Global biogeography of microbial nitrogen-cycling traits in soil},
  journal = {PNAS},
  year = {2016},
  volume = {113},
  number = {29},
  pages = {8033--8040},
  doi = {10.1073/pnas.1601070113},
  note = {access: not_obtained (Europe PMC fullTextXML for PMC4961168 empty)}
}
@misc{graf2014,
  author = {Graf and others},
  year = {2014},
  note = {access: not stated; excluded at synthesis (nosZ depth on gene trees, not organismal); not cited; incomplete: author, title, journal, volume, pages, doi}
}
@misc{malfertheinerCommunityConservatismWidespread2024,
  author = {Malfertheiner and Tackmann and Rodrigues and von Mering},
  title = {Community conservatism is widespread throughout microbial phyla and environments},
  howpublished = {bioRxiv},
  year = {2024},
  doi = {10.1101/2024.11.06.622256},
  note = {access: not stated; named in the critic's coverage gap; appears published January 2026, open access; not cited by the review; incomplete: author given names}
}
@article{johnson2006,
  author = {Johnson and others},
  journal = {Science},
  year = {2006},
  note = {access: not stated; named in the critic's coverage gap on Prochlorococcus and Synechococcus ecotypes; not cited by the review; incomplete: author, title, volume, pages, doi}
}
@article{martiny2009,
  author = {Martiny and Tai and others},
  journal = {PNAS},
  year = {2009},
  note = {access: not stated; named in the critic's coverage gap (taxonomic resolution and biogeography); not cited by the review; incomplete: author, title, volume, pages, doi}
}
@article{madin2020,
  author = {Madin and others},
  journal = {Scientific Data},
  year = {2020},
  note = {access: not stated; named in the critic's coverage gap (trait synthesis); not cited by the review; incomplete: author, title, volume, pages, doi}
}
@misc{sauer2019,
  author = {Sauer and Wang},
  year = {2019},
  note = {access: not stated; named in the critic's coverage gap (thermal traits); not cited by the review; incomplete: author, title, journal, volume, pages, doi}
}
@article{chaffron2010,
  author = {Chaffron and others},
  journal = {Genome Research},
  year = {2010},
  note = {access: not stated; named in the critic's coverage gap; not cited by the review; incomplete: author, title, volume, pages, doi}
}
@misc{tamames2016,
  author = {Tamames and others},
  year = {2016},
  note = {access: not stated; named in the critic's coverage gap (environmental distribution of prokaryotic taxa); not cited by the review; incomplete: author, title, journal, volume, pages, doi}
}
@article{auguet2010,
  author = {Auguet and Barberan and Casamayor},
  journal = {The ISME Journal},
  year = {2010},
  note = {access: not stated; named in the critic's coverage gap (archaeal habitat preference); not cited by the review; incomplete: author given names, title, volume, pages, doi}
}
@article{freckletonPhylogeneticAnalysisComparative2002,
  author = {Freckleton, R. P. and Harvey, P. H. and Pagel, M.},
  title = {Phylogenetic Analysis and Comparative Data: A Test and Review of Evidence},
  journal = {The American Naturalist},
  year = {2002},
  volume = {160},
  number = {6},
  pages = {712--726},
  doi = {10.1086/343873},
  note = {background (depth-measures); not from the inputs}
}
@article{blombergTestingPhylogeneticSignal2003,
  author = {Blomberg, Simon P. and Garland, Theodore and Ives, Anthony R.},
  title = {Testing for phylogenetic signal in comparative data: behavioral traits are more labile},
  journal = {Evolution},
  year = {2003},
  volume = {57},
  number = {4},
  pages = {717--745},
  doi = {10.1111/j.0014-3820.2003.tb00285.x},
  note = {background (depth-measures); not from the inputs}
}
```
