## depth-measures.1 (claim)

consenTRAIT's tau_D is the mean 16S rRNA distance from the root of clades in which at least 90% of members share a trait.

- conf: not stated
- class: not stated
- holds: the consenTRAIT method
- src: martinyPhylogeneticConservatismFunctional2013
- trail: H1-06 §1. What

From the note:

> H1-06:B-0021 [1. What is being compared] Depth of conservation is usually expressed as a distance on a tree: consenTRAIT's tau_D is the mean 16S rRNA distance from the root of clades in which at least 90% of members share a trait [1].
>

## depth-measures.2 (claim)

Phylogenetic signal statistics (Pagel's lambda, Blomberg's K, Moran's I correlograms, D) measure how well a trait tracks the tree without giving one depth.

- conf: not stated
- class: not stated
- holds: the signal statistics used in the sources read
- src: ramonedaBuildingGenomebasedUnderstanding2023, gobernaPredictingMicrobialTraits2016, morrisseyPhylogeneticOrganizationBacterial2016
- trail: H1-06 §1. What

From the note:

> H1-06:B-0022 [1. What is being compared] Phylogenetic signal statistics (Pagel's lambda, Blomberg's K, Moran's I correlograms, D) measure how well a trait tracks the tree without giving one depth [13, 16, 22].
>

Not found in the cited text (where to look, not what is wrong): holds: in

## depth-measures.3 (claim)

Rank-wise analyses of community composition use taxonomies, not trees, and the taxonomy differs between studies: Greengenes, SILVA or RDP, GTDB, a curated gyrB taxonomy, or no ranks at all, only sequence-identity thresholds. Rank labels differ between these taxonomies, and identity thresholds are not ranks.

- conf: not stated
- class: not stated
- holds: the rank-wise and depth studies the review read
- src: luEvaluatingCommunityenvironmentRelationships2016, ramonedaBuildingGenomebasedUnderstanding2023, lennonMappingNicheSpace2012, isobePhylogeneticConservationBacterial2019, lopezmondejarGlobalDistributionCarbohydrate2022, royaltyQuantitativelyPartitioningMicrobial2019, hoffertConstructingPeriodicTable2026, barnumPredictingMicrobialGrowth2024, mayjonadeRelativeEffectsAbiotic2024, baySoilBacterialCommunities2020, quirogaEcologicalAssemblyBacterial2022, schmidtEcologicalConsistencySSU2014
- trail: H1-06 §1. What, §5. Bounds

From the note:

> H1-06:B-0023 [1. What is being compared] Rank-wise analyses of community composition use taxonomies, not trees, and the taxonomy differs between studies: Greengenes [23], SILVA or RDP [13, 14, 19], GTDB [5, 6, 8, 12], a curated gyrB taxonomy [24], or no ranks at all, only sequence-identity thresholds [25, 26, 27].
>
> H1-06:B-0154 [5. Bounds and failure modes] Rank labels differ between Greengenes, SILVA, RDP, GTDB and gyrB taxonomies, and identity thresholds are not ranks.
>

Not found in the cited text (where to look, not what is wrong): holds: review

## depth-measures.4 (claim)

A depth in 16S rRNA distance cannot be converted into a rank.

- conf: not stated
- class: not stated
- holds: depths quoted in 16S rRNA distance
- src: none (the reviewer's synthesis)
- trail: H1-06 §1. What

From the note:

> H1-06:B-0024 [1. What is being compared] Unless stated otherwise, a depth quoted below is in 16S rRNA distance and cannot be converted into a rank.
>

## depth-measures.5 (claim)

Depth values from different trees or datasets are not commensurable.

- conf: not stated
- class: not stated
- holds: tau_D on different trees and genome sets
- src: sunPhylogeneticDistributionPolysaccharideDegrading2021
- trail: H1-06 §5. Bounds

From the note:

> H1-06:B-0153 [5. Bounds and failure modes] - Depth values from different trees or datasets are not commensurable [4].
>

Not found in the cited text (where to look, not what is wrong): holds: genome

## depth-measures.6 (claim)

Much of the apparent disagreement in this literature comes from the two halves of the question using different yardsticks: depth on a tree for traits, and ranks of a taxonomy for community composition.

- conf: not stated
- class: not stated
- holds: the literature the review read
- src: none (the reviewer's synthesis)
- trail: H1-06 §1. What

From the note:

> H1-06:B-0020 [1. What is being compared] The two halves of the question use different yardsticks, and much of the apparent disagreement in this literature comes from that.
>
> H1-06:B-0021 [1. What is being compared] Depth of conservation is usually expressed as a distance on a tree: consenTRAIT's tau_D is the mean 16S rRNA distance from the root of clades in which at least 90% of members share a trait [1].
>
> H1-06:B-0023 [1. What is being compared] Rank-wise analyses of community composition use taxonomies, not trees, and the taxonomy differs between studies: Greengenes [23], SILVA or RDP [13, 14, 19], GTDB [5, 6, 8, 12], a curated gyrB taxonomy [24], or no ranks at all, only sequence-identity thresholds [25, 26, 27].
>

Not found in the cited text (where to look, not what is wrong): holds: review

## environmental-preference.1 (claim)

An environmental "preference" can be (a) a growth optimum measured on isolates, (b) a field optimum inferred from where an ASV is most abundant, or (c) a response to an experimental perturbation; type (c) comes from engineered systems.

- conf: not stated
- class: not stated
- holds: the sources the review read
- src: none (the reviewer's synthesis)
- trail: H1-06 §1. What

From the note:

> H1-06:B-0026 [1. What is being compared] An environmental "preference" can be (a) a growth optimum measured on isolates, (b) a field optimum inferred from where an ASV is most abundant, or (c) a response to an experimental perturbation.
>
> H1-06:B-0027 [1. What is being compared] Type (c) comes from engineered systems and is kept separate below.
>

Not found in the cited text (where to look, not what is wrong): holds: review

## ph-preference.1 (claim)

Phylogenetic signal for pH preference was significant in four of five datasets but weak (Pagel's lambda 0.22 to 0.78), and correlogram Moran's I stayed below 0.25 at every depth, shallow ones included; there is no consenTRAIT-style depth.

- conf: single (critic: C-001)
- class: meas (note: "measured, natural")
- holds: natural soil and freshwater; 4,568 ASVs from five datasets (795 soil and 675 freshwater samples, pH about 3 to 10); pH preference defined as the pH of maximal field abundance; SILVA 138 taxonomy and RAxML trees of 16S; the critic verified lambda and Moran's I in the source
- src: ramonedaBuildingGenomebasedUnderstanding2023
- trail: H1-06 §2. Part A1, §critic, §Verdict as delivered

From the note:

> H1-06:B-0031 [2. Part A1: depth of conservation of environmental preferences] **pH, natural systems.** The strongest natural-system evidence is Ramoneda et al. 2023 [13] (measured, natural).
>
> H1-06:B-0032 [2. Part A1: depth of conservation of environmental preferences] Their data are 4,568 ASVs from five datasets (795 soil and 675 freshwater samples, pH about 3 to 10), with pH preference defined as the pH of maximal field abundance, SILVA 138 taxonomy and RAxML trees of 16S.
>
> H1-06:B-0033 [2. Part A1: depth of conservation of environmental preferences] Phylogenetic signal was significant in four of five datasets but weak (Pagel's lambda 0.22 to 0.78).
>
> H1-06:B-0034 [2. Part A1: depth of conservation of environmental preferences] Correlogram Moran's I stayed below 0.25 at every depth, shallow ones included.
>
> H1-06:A-003 [quote: Verdict as delivered] Natural-system field evidence (Ramoneda 2023, SILVA 138, 16S trees) gives weak signal for pH preference (Pagel's lambda 0.22 to 0.78, Moran's I < 0.25 at all depths), while a preprint (Chakraverti-Wuerthwein 2026) reports strong phylogenetic signal in the loadings of the pH-aligned canonical axis of global topsoil composition.
>
> H1-06:C-001 [danger: Critic: verdict partly supported] **Reformulated verdict:** A1 (environmental preferences): natural systems, measured for pH only, SINGLE SOURCE (Ramoneda et al. 2023).
>
> H1-06:C-002 [danger: Critic: verdict partly supported] Signal is significant in 4 of 5 datasets but weak (Pagel's lambda 0.22 to 0.78, Moran's I < 0.25 at all depths), there is no consenTRAIT-style depth, and families span 3.7 to 4.2 pH units.
>
> H1-06:C-021 [danger: Critic: verdict partly supported] Checks against sources: Ramoneda's lambda, Moran's I, the phylum quote, R2 = 0.21 / MAE 0.93, 6 to 24% GTDB matches and ~35% MAG/SAG all verified.
>

## ph-preference.2 (claim)

ASVs within single families spanned 3.7 to 4.2 pH units: Xanthobacteraceae in soil 4.01 to 8.20 (4.19 units), Chitinophagaceae in freshwater 4.63 to 8.35 (3.72 units).

- conf: not stated
- class: not stated
- holds: natural soil and freshwater datasets of Ramoneda et al. 2023; the critic's reading of the source
- src: ramonedaBuildingGenomebasedUnderstanding2023
- trail: H1-06 §critic, §Adversarial

From the note:

> H1-06:B-0035 [2. Part A1: depth of conservation of environmental preferences] ASVs within single families spanned four or more pH units (Xanthobacteraceae in soil, Chitinophagaceae in freshwater).
>
> H1-06:C-002 [danger: Critic: verdict partly supported] Signal is significant in 4 of 5 datasets but weak (Pagel's lambda 0.22 to 0.78, Moran's I < 0.25 at all depths), there is no consenTRAIT-style depth, and families span 3.7 to 4.2 pH units.
>
> H1-06:C-022 [danger: Critic: verdict partly supported] The family claim is partly wrong: Chitinophagaceae spans 4.63 to 8.35 (3.72 units), not 'four or more pH units'.
>
> H1-06:C-036 [warning: Adversarial critique, full findings] - [13] Ramoneda 2023 body claim: 'ASVs within single families spanned four or more pH units (Xanthobacteraceae in soil, Chitinophagaceae in freshwater)'. The source gives 4.01 to 8.20 (4.19 units) and 4.63 to 8.35 (3.72 units), so Chitinophagaceae does not span four units.
>

## ph-preference.3 (claim)

A phylum-level tendency seen in one dataset (acidophilic Acidobacteria in freshwater) did not recur.

- conf: not stated
- class: meas (note: "measured, natural")
- holds: natural soil and freshwater datasets of Ramoneda et al. 2023
- src: ramonedaBuildingGenomebasedUnderstanding2023
- trail: H1-06 §2. Part A1

From the note:

> H1-06:B-0031 [2. Part A1: depth of conservation of environmental preferences] **pH, natural systems.** The strongest natural-system evidence is Ramoneda et al. 2023 [13] (measured, natural).
>
> H1-06:B-0036 [2. Part A1: depth of conservation of environmental preferences] A phylum-level tendency seen in one dataset (acidophilic Acidobacteria in freshwater) did not recur.
>

Not found in the cited text (where to look, not what is wrong): holds: soil

## ph-preference.4 (claim)

The authors conclude that "phylum-level information provides relatively little insight into bacterial pH preferences" and turn to gene content instead.

- conf: not stated
- class: meas (note: "measured, natural")
- holds: natural soil and freshwater datasets of Ramoneda et al. 2023; the critic verified the phylum quote
- src: ramonedaBuildingGenomebasedUnderstanding2023
- trail: H1-06 §2. Part A1, §critic

From the note:

> H1-06:B-0031 [2. Part A1: depth of conservation of environmental preferences] **pH, natural systems.** The strongest natural-system evidence is Ramoneda et al. 2023 [13] (measured, natural).
>
> H1-06:B-0037 [2. Part A1: depth of conservation of environmental preferences] The authors conclude that "phylum-level information provides relatively little insight into bacterial pH preferences" and turn to gene content instead, where a genome-based model validated on an independent UK dataset reached R2 = 0.21 (MAE 0.93 pH units) [13].
>
> H1-06:C-021 [danger: Critic: verdict partly supported] Checks against sources: Ramoneda's lambda, Moran's I, the phylum quote, R2 = 0.21 / MAE 0.93, 6 to 24% GTDB matches and ~35% MAG/SAG all verified.
>

Not found in the cited text (where to look, not what is wrong): holds: soil; holds: freshwater

## ph-preference.5 (claim)

A genome-based model of pH preference, validated on an independent UK dataset, reached R2 = 0.21 (MAE 0.93 pH units).

- conf: not stated
- class: not stated
- holds: independent UK validation dataset; the critic verified R2 = 0.21 and MAE 0.93
- src: ramonedaBuildingGenomebasedUnderstanding2023
- trail: H1-06 §2. Part A1, §critic

From the note:

> H1-06:B-0037 [2. Part A1: depth of conservation of environmental preferences] The authors conclude that "phylum-level information provides relatively little insight into bacterial pH preferences" and turn to gene content instead, where a genome-based model validated on an independent UK dataset reached R2 = 0.21 (MAE 0.93 pH units) [13].
>
> H1-06:C-021 [danger: Critic: verdict partly supported] Checks against sources: Ramoneda's lambda, Moran's I, the phylum quote, R2 = 0.21 / MAE 0.93, 6 to 24% GTDB matches and ~35% MAG/SAG all verified.
>

## ph-preference.6 (claim)

Only 6 to 24% of ASVs matched a GTDB genome, and about 35% of those genomes were MAGs or SAGs.

- conf: not stated
- class: not stated
- holds: the bound on Ramoneda et al.'s genome-based analysis; the critic verified both figures
- src: ramonedaBuildingGenomebasedUnderstanding2023
- trail: H1-06 §2. Part A1, §critic

From the note:

> H1-06:B-0038 [2. Part A1: depth of conservation of environmental preferences] A bound applies: only 6 to 24% of ASVs matched a GTDB genome, and about 35% of those genomes were MAGs or SAGs.
>
> H1-06:C-021 [danger: Critic: verdict partly supported] Checks against sources: Ramoneda's lambda, Moran's I, the phylum quote, R2 = 0.21 / MAE 0.93, 6 to 24% GTDB matches and ~35% MAG/SAG all verified.
>

Not found in the cited text (where to look, not what is wrong): holds: genome-based

## ph-preference.7 (claim)

In CCA of global topsoil (N = 217) and ocean (N = 125) 16S surveys, OTU loadings on the first canonical direction, which aligns with pH in soil and with depth in the ocean, had strong phylogenetic signal (a modified tau_D and Pagel's lambda); secondary canonical directions had weak or no signal.

- conf: single (note: "SINGLE SOURCE")
- class: meas (note: "measured, natural, preprint")
- holds: natural; a preprint; numeric tau_D values appear only in figures, so the strong-signal claim is qualitative, with no number quoted; the permutation null shuffles sample labels rather than preserving group structure; a canonical loading is not a per-ASV optimum
- src: chakravertiwuerthweinPhylogeneticCoherenceMicrobiome2026
- trail: H1-06 §2. Part A1, §Adversarial, §Verdict as delivered

From the note:

> H1-06:B-0040 [2. Part A1: depth of conservation of environmental preferences] Chakraverti-Wuerthwein et al. 2026 [29] (measured, natural, preprint, SINGLE SOURCE) ran CCA on global topsoil (N = 217) and ocean (N = 125) 16S surveys.
>
> H1-06:B-0041 [2. Part A1: depth of conservation of environmental preferences] They report strong phylogenetic signal (a modified tau_D and Pagel's lambda) in OTU loadings on the first canonical direction, which aligns with pH in soil and with depth in the ocean.
>
> H1-06:B-0042 [2. Part A1: depth of conservation of environmental preferences] Secondary canonical directions had weak or no signal.
>
> H1-06:B-0043 [2. Part A1: depth of conservation of environmental preferences] Numeric tau_D values appear only in figures, and the permutation null shuffles sample labels rather than preserving group structure.
>
> H1-06:B-0044 [2. Part A1: depth of conservation of environmental preferences] The two quantities differ: a canonical loading is not a per-ASV optimum.
>
> H1-06:A-003 [quote: Verdict as delivered] Natural-system field evidence (Ramoneda 2023, SILVA 138, 16S trees) gives weak signal for pH preference (Pagel's lambda 0.22 to 0.78, Moran's I < 0.25 at all depths), while a preprint (Chakraverti-Wuerthwein 2026) reports strong phylogenetic signal in the loadings of the pH-aligned canonical axis of global topsoil composition.
>
> H1-06:C-030 [warning: Adversarial critique, full findings] - Chakraverti-Wuerthwein 2026 [29]: tau_D values 'appear only in figures', so the 'strong phylogenetic signal' claim is qualitative, with no number quoted. It is used in both the A1 and B verdicts.
>

## ph-preference.8 (claim)

The field-optimum and canonical-loading results are not in direct contradiction, but together they show that whether "pH preference" looks phylogenetically structured depends on how the preference is operationalised.

- conf: not stated
- class: reading (note: "Reviewer's reading")
- holds: built from two sources, one a preprint; the critic: a methodological argument that underpins the 'inconsistent' A1 verdict
- src: ramonedaBuildingGenomebasedUnderstanding2023, chakravertiwuerthweinPhylogeneticCoherenceMicrobiome2026
- trail: H1-06 §2. Part A1, §Adversarial

From the note:

> H1-06:B-0044 [2. Part A1: depth of conservation of environmental preferences] The two quantities differ: a canonical loading is not a per-ASV optimum.
>
> H1-06:B-0045 [2. Part A1: depth of conservation of environmental preferences] Reviewer's reading: the two results are not in direct contradiction, but together they show that whether "pH preference" looks phylogenetically structured depends on how the preference is operationalised.
>
> H1-06:C-056 [warning: Adversarial critique, full findings] - The A1 reviewer's reading ('whether pH preference looks phylogenetically structured depends on how the preference is operationalised') is a methodological argument built from two sources, one a preprint. It is labelled, but it underpins the 'inconsistent' A1 verdict.
>

## ph-preference.9 (claim)

The only large natural-system test of pH preference finds weak signal and poor prediction by rank.

- conf: single (critic: C-033)
- class: not stated
- holds: the one large natural-system study of pH preference, in soil and freshwater
- src: ramonedaBuildingGenomebasedUnderstanding2023
- trail: H1-06 §2. Part A1, §Adversarial

From the note:

> H1-06:B-0079 [2. Part A1: depth of conservation of environmental preferences] The only large natural-system test of pH preference finds weak signal and poor prediction by rank [13].
>
> H1-06:B-0032 [2. Part A1: depth of conservation of environmental preferences] Their data are 4,568 ASVs from five datasets (795 soil and 675 freshwater samples, pH about 3 to 10), with pH preference defined as the pH of maximal field abundance, SILVA 138 taxonomy and RAxML trees of 16S.
>
> H1-06:C-033 [warning: Adversarial critique, full findings] - Part A1 synthesis: 'The only large natural-system test of pH preference finds weak signal and poor prediction by rank' is correctly a single study [13], but the A1 verdict then generalises it into a field-level 'inconsistent' label.
>

Not found in the cited text (where to look, not what is wrong): holds: in

## moisture-salinity.1 (claim)

Across seven RDP ranks against permutation nulls, phylum level held 52% of the variance in optimum water potential and 58% in niche breadth, and strain level held 21 to 29% against 58 to 65% expected by chance.

- conf: single (note: "SINGLE SOURCE")
- class: meas (note: "measured, engineered")
- holds: engineered: 23 bacterial and 22 fungal soil isolates respired across a manipulated water-potential gradient (lab isolates, n = 23 bacteria); the authors caution that isolate numbers are small (5 bacterial phyla, 19 genera); the only direct rank-resolved measurement of a moisture optimum found
- src: lennonMappingNicheSpace2012
- trail: H1-06 §2. Part A1, §Verdict as delivered

From the note:

> H1-06:B-0046 [2. Part A1: depth of conservation of environmental preferences] **Moisture, engineered.** Lennon et al. 2012 [14] (measured, engineered) respired 23 bacterial and 22 fungal soil isolates across a manipulated water-potential gradient and partitioned niche parameters across seven RDP ranks against permutation nulls.
>
> H1-06:B-0047 [2. Part A1: depth of conservation of environmental preferences] Phylum level held 52% of the variance in optimum water potential and 58% in niche breadth, and strain level held 21 to 29% against 58 to 65% expected by chance.
>
> H1-06:B-0048 [2. Part A1: depth of conservation of environmental preferences] The authors themselves caution that isolate numbers are small (5 bacterial phyla, 19 genera).
>
> H1-06:B-0049 [2. Part A1: depth of conservation of environmental preferences] This is the only direct rank-resolved measurement of a moisture optimum found.
>
> H1-06:B-0050 [2. Part A1: depth of conservation of environmental preferences] SINGLE SOURCE.
>
> H1-06:A-004 [quote: Verdict as delivered] The coarse-rank result for moisture (52 to 58% of variance at phylum, RDP taxonomy) is engineered (lab isolates, n = 23 bacteria), as is the salinity clustering (reciprocal transplant, Greengenes).
>

## moisture-salinity.2 (claim)

Salinity-preferring phylotypes were phylogenetically clustered both tree-wide and near the tips (freshwater-preferring: SES-PD -3.5, NTI 4.3; saltwater-preferring: SES-PD -5.4, NTI 5.2, p < 0.01); no depth statistic was reported.

- conf: single (note: "SINGLE SOURCE")
- class: meas (note: "measured, engineered")
- holds: engineered: a reciprocal transplant between tidal freshwater and brackish marsh soils; Greengenes 97% OTUs, n = 5 per treatment
- src: morrisseyEvolutionaryHistoryInfluences2015
- trail: H1-06 §2. Part A1, §Verdict as delivered

From the note:

> H1-06:B-0051 [2. Part A1: depth of conservation of environmental preferences] **Salinity, engineered.** In a reciprocal transplant between tidal freshwater and brackish marsh soils (Greengenes 97% OTUs, n = 5 per treatment), salinity-preferring phylotypes were phylogenetically clustered both tree-wide and near the tips.
>
> H1-06:B-0052 [2. Part A1: depth of conservation of environmental preferences] Freshwater-preferring: SES-PD -3.5, NTI 4.3.
>
> H1-06:B-0053 [2. Part A1: depth of conservation of environmental preferences] Saltwater-preferring: SES-PD -5.4, NTI 5.2 (p < 0.01) [15] (measured, engineered, SINGLE SOURCE).
>
> H1-06:B-0055 [2. Part A1: depth of conservation of environmental preferences] No depth statistic was reported.
>
> H1-06:A-004 [quote: Verdict as delivered] The coarse-rank result for moisture (52 to 58% of variance at phylum, RDP taxonomy) is engineered (lab isolates, n = 23 bacteria), as is the salinity clustering (reciprocal transplant, Greengenes).
>

## moisture-salinity.3 (claim)

At class level, Betaproteobacteria were enriched among freshwater-preferring phylotypes and Alpha- and Gammaproteobacteria among saltwater-preferring ones.

- conf: single (note: "SINGLE SOURCE")
- class: meas (note: "measured, engineered")
- holds: engineered: the tidal freshwater and brackish marsh reciprocal transplant
- src: morrisseyEvolutionaryHistoryInfluences2015
- trail: H1-06 §2. Part A1

From the note:

> H1-06:B-0051 [2. Part A1: depth of conservation of environmental preferences] **Salinity, engineered.** In a reciprocal transplant between tidal freshwater and brackish marsh soils (Greengenes 97% OTUs, n = 5 per treatment), salinity-preferring phylotypes were phylogenetically clustered both tree-wide and near the tips.
>
> H1-06:B-0053 [2. Part A1: depth of conservation of environmental preferences] Saltwater-preferring: SES-PD -5.4, NTI 5.2 (p < 0.01) [15] (measured, engineered, SINGLE SOURCE).
>
> H1-06:B-0054 [2. Part A1: depth of conservation of environmental preferences] At class level, Betaproteobacteria were enriched among freshwater-preferring phylotypes and Alpha- and Gammaproteobacteria among saltwater-preferring ones.
>

## moisture-salinity.4 (claim)

Moisture and salinity preferences have not been measured in natural systems: the rank-resolved results are engineered, and the deep-rank moisture result has no natural-system rank-wise counterpart among the sources read.

- conf: not stated
- class: not stated
- search: not stated
- holds: natural systems; the engineered isolate and transplant studies (Lennon 2012, Morrissey and Franklin 2015)
- src: lennonMappingNicheSpace2012, morrisseyEvolutionaryHistoryInfluences2015
- trail: H1-06 §critic, §4. Part B, §5. Bounds

From the note:

> H1-06:C-003 [danger: Critic: verdict partly supported] Moisture and salinity have not been measured in natural systems: the rank-resolved results are engineered (Lennon 2012, Morrissey and Franklin 2015).
>
> H1-06:C-015 [danger: Critic: verdict partly supported] A split A1 verdict fits the body better: pH 'measured, natural, single source, weak signal, no depth'; moisture and salinity 'not measured in natural systems'.
>
> H1-06:B-0152 [4. Part B: environmental structuring of composition from fine to coarse ranks] The deep-rank moisture result [14] rests on engineered isolates and has no natural-system rank-wise counterpart among the sources read.
>
> H1-06:B-0164 [5. Bounds and failure modes] The two coarse-rank optimum results are engineered [14, 15].
>

Not found in the cited text (where to look, not what is wrong): holds: isolate

## temperature-optimum.1 (claim)

Within the phylum Thermotogota (64 genomes), optimal growth temperature has strong signal (Pagel's lambda 0.93), yet ancestral reconstruction places several secondary shifts to mesophily and hyperthermophily, and most of the 68 OGT-associated genes have histories of horizontal transfer: strong signal within a phylum coexists with repeated shifts.

- conf: single (note: "SINGLE SOURCE")
- class: deriv (note: "inferred")
- holds: one phylum, Thermotogota, 64 genomes
- src: farrellBacterialGrowthTemperature2024
- trail: H1-06 §2. Part A1, §Verdict as delivered, §critic

From the note:

> H1-06:B-0056 [2. Part A1: depth of conservation of environmental preferences] **Temperature.** Within the phylum Thermotogota (64 genomes), optimal growth temperature has strong signal (Pagel's lambda 0.93), yet ancestral reconstruction places several secondary shifts to mesophily and hyperthermophily.
>
> H1-06:B-0057 [2. Part A1: depth of conservation of environmental preferences] Most of the 68 OGT-associated genes have histories of horizontal transfer [17] (inferred, SINGLE SOURCE).
>
> H1-06:B-0058 [2. Part A1: depth of conservation of environmental preferences] Strong signal within a phylum therefore coexists with repeated shifts.
>
> H1-06:A-005 [quote: Verdict as delivered] Temperature optimum is strongly signalled within one phylum (Thermotogota, lambda 0.93) yet shifted several times, with horizontally acquired genes.
>
> H1-06:C-004 [danger: Critic: verdict partly supported] Temperature is inferred within one phylum (Farrell).
>

## trait-compilations.1 (claim)

Across 990 traits collated on a SILVA r119 tree, binary, mostly gene-presence, traits had mean -D+1 = 0.93 (98% significant) and continuous traits mean K = 0.16 (74% significant).

- conf: not stated
- class: model (note: "compiled and modelled")
- limit: access (note: "I could not re-open it because the publisher returned a bot challenge")
- holds: a compilation; read in full by one search agent only, so it carries no weight on its own; the critic: still listed in the A1 verdict's evidence classes
- src: gobernaPredictingMicrobialTraits2016
- trail: H1-06 §2. Part A1, §Adversarial

From the note:

> H1-06:B-0059 [2. Part A1: depth of conservation of environmental preferences] **Compilations and models.** Goberna and Verdú 2016 [16] (compiled and modelled) collated 990 traits on a SILVA r119 tree.
>
> H1-06:B-0060 [2. Part A1: depth of conservation of environmental preferences] Binary, mostly gene-presence, traits had mean -D+1 = 0.93 (98% significant).
>
> H1-06:B-0061 [2. Part A1: depth of conservation of environmental preferences] Continuous traits had mean K = 0.16 (74% significant).
>
> H1-06:B-0064 [2. Part A1: depth of conservation of environmental preferences] (One search agent read this paper in full; I could not re-open it because the publisher returned a bot challenge, so it carries no weight on its own.
>
> H1-06:C-029 [warning: Adversarial critique, full findings] - Goberna and Verdu 2016 [16]: the synthesiser could not re-open it but still quotes specific figures (mean -D+1 = 0.93, K = 0.16, 9.9% and 8.6%) and an internal-inconsistency claim. It is labelled as carrying no weight, but it is listed in the A1 verdict's evidence classes.
>

## trait-compilations.2 (claim)

The compilation is internally inconsistent on environmental optima: it lists optimal pH and temperature and moisture niche breadth among "the most conserved continuous traits", and elsewhere places optimal pH, salt tolerance and moisture niche breadth among traits with "moderate signals".

- conf: not stated
- class: not stated
- limit: access (note: "I could not re-open it because the publisher returned a bot challenge")
- holds: 990 traits on a SILVA r119 tree; read in full by one search agent only, carrying no weight on its own
- src: gobernaPredictingMicrobialTraits2016
- trail: H1-06 §2. Part A1, §Adversarial

From the note:

> H1-06:B-0059 [2. Part A1: depth of conservation of environmental preferences] **Compilations and models.** Goberna and Verdú 2016 [16] (compiled and modelled) collated 990 traits on a SILVA r119 tree.
>
> H1-06:B-0062 [2. Part A1: depth of conservation of environmental preferences] The paper is internally inconsistent on environmental optima: it lists optimal pH and temperature and moisture niche breadth among "the most conserved continuous traits", and elsewhere places optimal pH, salt tolerance and moisture niche breadth among traits with "moderate signals".
>
> H1-06:B-0064 [2. Part A1: depth of conservation of environmental preferences] (One search agent read this paper in full; I could not re-open it because the publisher returned a bot challenge, so it carries no weight on its own.
>
> H1-06:C-029 [warning: Adversarial critique, full findings] - Goberna and Verdu 2016 [16]: the synthesiser could not re-open it but still quotes specific figures (mean -D+1 = 0.93, K = 0.16, 9.9% and 8.6%) and an internal-inconsistency claim. It is labelled as carrying no weight, but it is listed in the A1 verdict's evidence classes.
>

## trait-compilations.3 (claim)

Only 9.9% of continuous and 8.6% of binary traits met the compilation's threshold for accurate phylogenetic prediction.

- conf: not stated
- class: model (note: "compiled and modelled")
- limit: access (note: "I could not re-open it because the publisher returned a bot challenge")
- holds: 990 traits on a SILVA r119 tree; read in full by one search agent only
- src: gobernaPredictingMicrobialTraits2016
- trail: H1-06 §2. Part A1

From the note:

> H1-06:B-0059 [2. Part A1: depth of conservation of environmental preferences] **Compilations and models.** Goberna and Verdú 2016 [16] (compiled and modelled) collated 990 traits on a SILVA r119 tree.
>
> H1-06:B-0063 [2. Part A1: depth of conservation of environmental preferences] Only 9.9% of continuous and 8.6% of binary traits met its threshold for accurate phylogenetic prediction.
>
> H1-06:B-0064 [2. Part A1: depth of conservation of environmental preferences] (One search agent read this paper in full; I could not re-open it because the publisher returned a bot challenge, so it carries no weight on its own.
>

## trait-compilations.4 (claim)

Growth optima predicted from amino-acid composition for 15,596 BacDive organisms reached, under family-level holdout, R2 0.73 for temperature, 0.81 for salinity and 0.48 for pH, with 92% balanced accuracy for oxygen tolerance.

- conf: not stated
- class: model (note: "modelled, preprint")
- holds: GTDB r214; a preprint whose publication status is unverified
- src: barnumPredictingMicrobialGrowth2024
- trail: H1-06 §2. Part A1, §Provenance

From the note:

> H1-06:B-0065 [2. Part A1: depth of conservation of environmental preferences] Barnum et al. 2024 [12] (modelled, preprint) predicted growth optima from amino-acid composition for 15,596 BacDive organisms (GTDB r214).
>
> H1-06:B-0066 [2. Part A1: depth of conservation of environmental preferences] Under family-level holdout, R2 was 0.73 for temperature, 0.81 for salinity and 0.48 for pH, with 92% balanced accuracy for oxygen tolerance.
>
> H1-06:B-0016 [info: Provenance] Publication status of the preprints Barnum 2024 and Mayjonade 2024 is unverified.
>

## trait-compilations.5 (claim)

A phylogeny-only comparison model failed at higher-rank holdouts except for oxygen tolerance, which stayed moderately accurate up to order and class.

- conf: not stated
- class: model (note: "modelled, preprint")
- holds: 15,596 BacDive organisms, GTDB r214; a preprint
- src: barnumPredictingMicrobialGrowth2024
- trail: H1-06 §2. Part A1

From the note:

> H1-06:B-0065 [2. Part A1: depth of conservation of environmental preferences] Barnum et al. 2024 [12] (modelled, preprint) predicted growth optima from amino-acid composition for 15,596 BacDive organisms (GTDB r214).
>
> H1-06:B-0067 [2. Part A1: depth of conservation of environmental preferences] A phylogeny-only comparison model failed at higher-rank holdouts except for oxygen tolerance, which stayed moderately accurate up to order and class.
>

## trait-compilations.6 (claim)

Among six genome-inferred traits, oxygen tolerance had much of its variance at deep nodes, often near phylum, but was "not universally conserved at the phylum level".

- conf: single (note: "SINGLE SOURCE for this method")
- class: deriv (note: "inferred")
- holds: 50,745 GTDB genomes
- src: hoffertConstructingPeriodicTable2026
- trail: H1-06 §2. Part A1

From the note:

> H1-06:B-0068 [2. Part A1: depth of conservation of environmental preferences] Among six genome-inferred traits in 50,745 GTDB genomes, oxygen tolerance had much of its variance at deep nodes, often near phylum, but was "not universally conserved at the phylum level" [8] (inferred, SINGLE SOURCE for this method).
>

## perturbation-response-depth.1 (claim)

Responses to N addition across 13 field experiments on five continents were conserved at tau_D 0.016 to 0.020 per location (0.017 merged).

- conf: not stated
- class: not stated
- holds: engineered perturbation responses (N addition); taxonomy RDP on SILVA 128; the authors equate this to roughly genus, but the review's own Section 1 says a 16S depth cannot be converted into a rank (the critic: inconsistent use); the critic verified the figures
- src: isobePhylogeneticConservationBacterial2019
- trail: H1-06 §2. Part A1, §critic, §Adversarial

From the note:

> H1-06:B-0069 [2. Part A1: depth of conservation of environmental preferences] **Perturbation responses (engineered, kept separate).** Responses to N addition across 13 field experiments on five continents were conserved at tau_D 0.016 to 0.020 per location (0.017 merged), which the authors equate to roughly genus (SILVA via RDP) [19].
>
> H1-06:B-0024 [1. What is being compared] Unless stated otherwise, a depth quoted below is in 16S rRNA distance and cannot be converted into a rank.
>
> H1-06:C-023 [danger: Critic: verdict partly supported] For Isobe 2019, tau_D 0.016 to 0.020 per location, 0.017 merged, the 22% correlogram depth, the Gammaproteobacteria/Aquicela example and RDP-on-SILVA 128 were all verified.
>
> H1-06:C-054 [warning: Adversarial critique, full findings] - The equation of tau_D 0.016 to 0.020 with 'roughly genus' is attributed to the authors, but the review's own Section 1 says a 16S depth 'cannot be converted into a rank'. This is inconsistent use.
>

## perturbation-response-depth.2 (claim)

A correlogram on the same N-addition data detected response similarity out to 22% 16S divergence, which the authors note is a less conservative depth metric.

- conf: not stated
- class: not stated
- holds: engineered perturbation responses, 13 N-addition field experiments; the critic verified the 22% correlogram depth
- src: isobePhylogeneticConservationBacterial2019
- trail: H1-06 §2. Part A1, §critic

From the note:

> H1-06:B-0069 [2. Part A1: depth of conservation of environmental preferences] **Perturbation responses (engineered, kept separate).** Responses to N addition across 13 field experiments on five continents were conserved at tau_D 0.016 to 0.020 per location (0.017 merged), which the authors equate to roughly genus (SILVA via RDP) [19].
>
> H1-06:B-0070 [2. Part A1: depth of conservation of environmental preferences] A correlogram on the same data detected response similarity out to 22% 16S divergence, and the authors note that this is a less conservative depth metric.
>
> H1-06:C-023 [danger: Critic: verdict partly supported] For Isobe 2019, tau_D 0.016 to 0.020 per location, 0.017 merged, the 22% correlogram depth, the Gammaproteobacteria/Aquicela example and RDP-on-SILVA 128 were all verified.
>

## perturbation-response-depth.3 (claim)

Warming, drought, elevated CO2, P addition and liming gave tau_D 0.016 to 0.024, with little difference among perturbations, and clades responding to one perturbation rarely responded to another.

- conf: not stated
- class: not stated
- holds: engineered perturbation responses of soil bacteria
- src: isobePhylogeneticConservationSoil2020
- trail: H1-06 §2. Part A1, §References

From the note:

> H1-06:B-0069 [2. Part A1: depth of conservation of environmental preferences] **Perturbation responses (engineered, kept separate).** Responses to N addition across 13 field experiments on five continents were conserved at tau_D 0.016 to 0.020 per location (0.017 merged), which the authors equate to roughly genus (SILVA via RDP) [19].
>
> H1-06:B-0071 [2. Part A1: depth of conservation of environmental preferences] Warming, drought, elevated CO2, P addition and liming gave tau_D 0.016 to 0.024, with little difference among perturbations; clades responding to one perturbation rarely responded to another [20].
>
> H1-06:R-0137 [References] Phylogenetic conservation of soil bacterial responses to simulated global changes.
>

Not found in the cited text (where to look, not what is wrong): holds: bacteria

## perturbation-response-depth.4 (claim)

In leaf litter, only positive bacterial responses were significantly conserved; negative responses were not (drought decrease P = 0.541; N decrease P = 0.763).

- conf: not stated
- class: not stated
- holds: engineered perturbation responses; one litter study
- src: amendMicrobialResponseSimulated2015
- trail: H1-06 §2. Part A1, §5. Bounds

From the note:

> H1-06:B-0069 [2. Part A1: depth of conservation of environmental preferences] **Perturbation responses (engineered, kept separate).** Responses to N addition across 13 field experiments on five continents were conserved at tau_D 0.016 to 0.020 per location (0.017 merged), which the authors equate to roughly genus (SILVA via RDP) [19].
>
> H1-06:B-0072 [2. Part A1: depth of conservation of environmental preferences] In leaf litter, only positive bacterial responses were significantly conserved; negative responses were not (drought decrease P = 0.541; N decrease P = 0.763) [21].
>
> H1-06:B-0160 [5. Bounds and failure modes] Negative responses were not conserved in one litter study [21].
>

## perturbation-response-depth.5 (claim)

Coarse groups can hide opposing finer ones in the N-addition responses: Gammaproteobacteria as a class had no consistent response while one genus within it responded positively, and an order and a family within it responded in opposite directions.

- conf: not stated
- class: not stated
- holds: engineered N-addition experiments (one study); the critic verified the Gammaproteobacteria example
- src: isobePhylogeneticConservationBacterial2019
- trail: H1-06 §2. Part A1, §critic

From the note:

> H1-06:B-0073 [2. Part A1: depth of conservation of environmental preferences] Coarse groups can hide opposing finer ones.
>
> H1-06:B-0074 [2. Part A1: depth of conservation of environmental preferences] Gammaproteobacteria as a class had no consistent response while one genus within it responded positively, and an order and a family within it responded in opposite directions [19].
>
> H1-06:C-023 [danger: Critic: verdict partly supported] For Isobe 2019, tau_D 0.016 to 0.020 per location, 0.017 merged, the 22% correlogram depth, the Gammaproteobacteria/Aquicela example and RDP-on-SILVA 128 were all verified.
>

Not found in the cited text (where to look, not what is wrong): N-addition; holds: engineered; holds: n-addition; holds: experiments

## perturbation-response-depth.6 (claim)

The same N-addition study also reports consistent phylum- and class-level responses: phylum Actinobacteria positive; classes Betaproteobacteria and Deltaproteobacteria negative.

- conf: not stated
- class: not stated
- holds: engineered N-addition experiments; the review leaves this out, citing only the 'coarse hides fine' example
- src: isobePhylogeneticConservationBacterial2019
- trail: H1-06 §critic, §Adversarial

From the note:

> H1-06:C-024 [danger: Critic: verdict partly supported] But Isobe also reports consistent phylum- and class-level responses (Actinobacteria positive; Betaproteobacteria and Deltaproteobacteria negative), which the review leaves out while citing only the 'coarse hides fine' example.
>
> H1-06:C-031 [warning: Adversarial critique, full findings] - Section 5 bullet 'Coarse groups can contain opposing finer responses' is phrased as a general bound, but it rests on one N-addition study [19] plus a time series [28]. [19] also reports consistent coarse-rank responses (phylum Actinobacteria positive; classes Betaproteobacteria and Deltaproteobacteria negative), and the review omits these.
>

Not found in the cited text (where to look, not what is wrong): holds: engineered; holds: experiments

## perturbation-response-depth.7 (claim)

In situ growth measured by qSIP had K 0.38 to 0.54 and lambda 0.96 to 0.98.

- conf: not stated
- class: not stated
- holds: one forest soil; in situ growth, reported among the perturbation responses
- src: morrisseyPhylogeneticOrganizationBacterial2016
- trail: H1-06 §2. Part A1

From the note:

> H1-06:B-0069 [2. Part A1: depth of conservation of environmental preferences] **Perturbation responses (engineered, kept separate).** Responses to N addition across 13 field experiments on five continents were conserved at tau_D 0.016 to 0.020 per location (0.017 merged), which the authors equate to roughly genus (SILVA via RDP) [19].
>
> H1-06:B-0075 [2. Part A1: depth of conservation of environmental preferences] In situ growth measured by qSIP in one forest soil had K 0.38 to 0.54 and lambda 0.96 to 0.98 [22].
>

## perturbation-response-depth.8 (claim)

Within a single 16S OTU (Curtobacterium, minimum 83.2% ANI), the drought response appeared conserved across clades while carbohydrate-use degree and degradation temperature preference varied among clades.

- conf: single (note: "SINGLE SOURCE")
- class: meas (note: "measured, natural")
- holds: one abundant terrestrial bacterium, a single 16S OTU (Curtobacterium); natural
- src: chaseMicrodiversityAbundantTerrestrial2017
- trail: H1-06 §2. Part A1, §References

From the note:

> H1-06:B-0076 [2. Part A1: depth of conservation of environmental preferences] Within a single 16S OTU (Curtobacterium, minimum 83.2% ANI), the drought response appeared conserved across clades while carbohydrate-use degree and degradation temperature preference varied among clades [18] (measured, natural, SINGLE SOURCE).
>
> H1-06:R-0132 [References] Microdiversity of an abundant terrestrial bacterium encompasses extensive variation in ecologically relevant traits. mBio 8(6): e01809-17. doi:10.1128/mBio.01809-17
>

## perturbation-response-depth.9 (claim)

Perturbation responses are a different quantity from environmental optima, and they cluster at tau_D about 0.016 to 0.024 in 16S terms.

- conf: not stated
- class: not stated
- holds: engineered N-addition, global-change and litter experiments; a 16S depth cannot be converted into a rank
- src: isobePhylogeneticConservationBacterial2019, isobePhylogeneticConservationSoil2020, amendMicrobialResponseSimulated2015
- trail: H1-06 §2. Part A1, §1. What

From the note:

> H1-06:B-0080 [2. Part A1: depth of conservation of environmental preferences] Perturbation responses, a different quantity, cluster at roughly genus depth in 16S terms [19, 20, 21].
>
> H1-06:B-0069 [2. Part A1: depth of conservation of environmental preferences] **Perturbation responses (engineered, kept separate).** Responses to N addition across 13 field experiments on five continents were conserved at tau_D 0.016 to 0.020 per location (0.017 merged), which the authors equate to roughly genus (SILVA via RDP) [19].
>
> H1-06:B-0071 [2. Part A1: depth of conservation of environmental preferences] Warming, drought, elevated CO2, P addition and liming gave tau_D 0.016 to 0.024, with little difference among perturbations; clades responding to one perturbation rarely responded to another [20].
>
> H1-06:B-0024 [1. What is being compared] Unless stated otherwise, a depth quoted below is in 16S rRNA distance and cannot be converted into a rank.
>
> H1-06:C-054 [warning: Adversarial critique, full findings] - The equation of tau_D 0.016 to 0.020 with 'roughly genus' is attributed to the authors, but the review's own Section 1 says a 16S depth 'cannot be converted into a rank'. This is inconsistent use.
>

Not found in the cited text (where to look, not what is wrong): holds: global-change

## env-preference-depth.1 (claim)

For environmental preferences in natural systems, depth of conservation is measured for pH only, from a single source (Ramoneda et al. 2023): signal is significant in 4 of 5 datasets but weak, there is no consenTRAIT-style depth, and families span 3.7 to 4.2 pH units. Moisture and salinity have not been measured in natural systems (the rank-resolved results are engineered: Lennon 2012, Morrissey and Franklin 2015), and temperature is inferred within one phylum (Farrell).

- conf: single (critic: C-001)
- class: not stated
- rating: "Measured and inconsistent between methods, taxonomies or datasets" (critic: C-012: A1 over-reaches)
- holds: natural systems; the critic's split verdict: pH measured, natural, single source, weak signal, no depth; moisture and salinity not measured in natural systems
- src: ramonedaBuildingGenomebasedUnderstanding2023, lennonMappingNicheSpace2012, morrisseyEvolutionaryHistoryInfluences2015, farrellBacterialGrowthTemperature2024
- trail: H1-06 §critic, §Verdict as delivered, §6. Verdicts

From the note:

> H1-06:A-001 [quote: Verdict as delivered] Phylogenetic depth of conservation: environmental preferences (pH, moisture, salinity, temperature optima)**: Measured and inconsistent between methods, taxonomies or datasets.
>
> H1-06:A-023 [6. Verdicts] - **A1, environmental preferences:** measured and inconsistent between methods, taxonomies or datasets.
>
> H1-06:C-001 [danger: Critic: verdict partly supported] **Reformulated verdict:** A1 (environmental preferences): natural systems, measured for pH only, SINGLE SOURCE (Ramoneda et al. 2023).
>
> H1-06:C-002 [danger: Critic: verdict partly supported] Signal is significant in 4 of 5 datasets but weak (Pagel's lambda 0.22 to 0.78, Moran's I < 0.25 at all depths), there is no consenTRAIT-style depth, and families span 3.7 to 4.2 pH units.
>
> H1-06:C-003 [danger: Critic: verdict partly supported] Moisture and salinity have not been measured in natural systems: the rank-resolved results are engineered (Lennon 2012, Morrissey and Franklin 2015).
>
> H1-06:C-004 [danger: Critic: verdict partly supported] Temperature is inferred within one phylum (Farrell).
>
> H1-06:C-012 [danger: Critic: verdict partly supported] A1 over-reaches.
>
> H1-06:C-015 [danger: Critic: verdict partly supported] A split A1 verdict fits the body better: pH 'measured, natural, single source, weak signal, no depth'; moisture and salinity 'not measured in natural systems'.
>
> H1-06:C-001 [danger: Critic: verdict partly supported] **Reformulated verdict:** A1 (environmental preferences): natural systems, measured for pH only, SINGLE SOURCE (Ramoneda et al. 2023).
>

## env-preference-depth.2 (claim)

The 'inconsistent' label for environmental preferences emerges only when the natural evidence (one large study with weak signal, plus a preprint on a non-comparable quantity, canonical loadings) is set beside engineered isolate and transplant results.

- conf: not stated
- class: not stated
- holds: the critic's reading of the body; engineered evidence may not carry a natural-system verdict (Common rule 10)
- src: ramonedaBuildingGenomebasedUnderstanding2023, chakravertiwuerthweinPhylogeneticCoherenceMicrobiome2026, lennonMappingNicheSpace2012, morrisseyEvolutionaryHistoryInfluences2015
- trail: H1-06 §critic, §Adversarial

From the note:

> H1-06:C-005 [danger: Critic: verdict partly supported] The 'inconsistent' label only emerges when natural evidence is set beside engineered results or a preprint that measures a different quantity (CCA loadings), so it should not stand as the natural-system verdict.
>
> H1-06:C-013 [danger: Critic: verdict partly supported] The body's own synthesis says natural evidence is one large study (weak signal) plus a preprint on a non-comparable quantity (canonical loadings).
>
> H1-06:C-014 [danger: Critic: verdict partly supported] The inconsistency behind the verdict comes from comparing that natural study with engineered isolate and transplant work (Lennon, Morrissey and Franklin), and Common rule 10 forbids letting engineered evidence carry a natural-system verdict.
>
> H1-06:C-033 [warning: Adversarial critique, full findings] - Part A1 synthesis: 'The only large natural-system test of pH preference finds weak signal and poor prediction by rank' is correctly a single study [13], but the A1 verdict then generalises it into a field-level 'inconsistent' label.
>

## env-preference-depth.3 (claim)

No consenTRAIT depth for any environmental optimum (pH, temperature or moisture) was found.

- conf: not stated
- class: search (note: "Not found by these routes")
- search: searched, not found (note: "Not found by these routes: (1) any consenTRAIT tau_D for pH, temperature or moisture optima")
- holds: routes: Europe PMC REST keyword, DOI and title search plus fullTextXML; the 'consenTRAIT AND OPEN_ACCESS' query (23 hits screened); WebSearch, among others
- src: none (a search result)
- trail: H1-06 §2. Part A1, §Provenance, §Verdict as delivered

From the note:

> H1-06:A-002 [quote: Verdict as delivered] No consenTRAIT-style depth for any environmental optimum was found.
>
> H1-06:B-0028 [2. Part A1: depth of conservation of environmental preferences] **No consenTRAIT depth for any environmental optimum was found.** The frequently repeated statement that pH optimum, soil moisture optimum and habitat association sit in deep clades appears in Martiny et al. 2013 as a discussion claim resting on other studies.
>
> H1-06:B-0008 [info: Provenance] Routes behind every 'not found': Europe PMC REST keyword, DOI and title search plus fullTextXML; the 'consenTRAIT AND OPEN_ACCESS' query (23 hits screened); citing papers of Lu et al. 2016 screened by title; PMC HTML; publisher pages; bioRxiv; the Lennon lab PDF archive; WebSearch on taxonomic sufficiency, taxonomic resolution with explained variation, ecological coherence with ranks, genome completeness with functional inference, and phylogenetic signal of optimal growth temperature.
>
> H1-06:B-0009 [info: Provenance] Not found by these routes: (1) any consenTRAIT tau_D for pH, temperature or moisture optima; (2) any rank-wise composition-environment study, other than Lu 2016, that controls group number and size (Schmidt 2014 controls them, but for identity thresholds and annotation consistency, not ranks); (3) any direct test of how genome incompleteness biases tau_D or signal statistics.
>

## env-preference-depth.4 (claim)

The frequently repeated statement that pH optimum, soil moisture optimum and habitat association sit in deep clades appears in Martiny et al. 2013 as a discussion claim resting on other studies; that paper does not measure any of these. The primary studies it cites were either not obtained (Placella et al. 2012, Philippot et al. 2010) or were read and give a more mixed picture (Lennon et al. 2012).

- conf: not stated
- class: assert (note: "asserted, SECONDARY")
- holds: a secondary discussion statement
- src: martinyPhylogeneticConservatismFunctional2013, placellaRainfallinducedCarbonDioxide2012, philippotEcologicalCoherenceHigh2010, lennonMappingNicheSpace2012
- trail: H1-06 §2. Part A1

From the note:

> H1-06:B-0028 [2. Part A1: depth of conservation of environmental preferences] **No consenTRAIT depth for any environmental optimum was found.** The frequently repeated statement that pH optimum, soil moisture optimum and habitat association sit in deep clades appears in Martiny et al. 2013 as a discussion claim resting on other studies.
>
> H1-06:B-0029 [2. Part A1: depth of conservation of environmental preferences] That paper does not measure any of these (asserted, SECONDARY) [1].
>
> H1-06:B-0030 [2. Part A1: depth of conservation of environmental preferences] The primary studies it cites were either not obtained (Placella et al. 2012, Philippot et al. 2010) or were read and give a more mixed picture (Lennon et al. 2012; see below).
>

## env-preference-depth.5 (claim)

The evidence on environmental preferences does not converge on a single depth. The claim that environmental optima are conserved at deep ranks rests, among full-text sources, on an engineered study of 23 bacterial isolates for moisture and on an asserted secondary statement; natural evidence for environmental optima is thin, and the two coarse-rank optimum results are engineered.

- conf: not stated
- class: not stated
- holds: the sources the review read for Part A1
- src: lennonMappingNicheSpace2012, martinyPhylogeneticConservatismFunctional2013, morrisseyEvolutionaryHistoryInfluences2015
- trail: H1-06 §2. Part A1, §5. Bounds

From the note:

> H1-06:B-0077 [2. Part A1: depth of conservation of environmental preferences] **Synthesis for A1.** The evidence does not converge on a single depth.
>
> H1-06:B-0078 [2. Part A1: depth of conservation of environmental preferences] The claim that environmental optima are conserved at deep ranks rests, among full-text sources, on an engineered study of 23 bacterial isolates for moisture [14] and on an asserted secondary statement [1].
>
> H1-06:B-0163 [5. Bounds and failure modes] - Natural evidence for environmental optima (A1) is thin.
>
> H1-06:B-0164 [5. Bounds and failure modes] The two coarse-rank optimum results are engineered [14, 15].
>

Not found in the cited text (where to look, not what is wrong): holds: review; holds: part

## env-preference-depth.6 (claim)

By evidence class, the Part A1 sources are: measured (Ramoneda; the preprint Chakraverti-Wuerthwein; engineered: Lennon, Morrissey and Franklin), inferred (Farrell), and modelled or compiled (Goberna and Verdu; Barnum, a preprint).

- conf: not stated
- class: not stated
- holds: the critic: Goberna and Verdu was not re-opened by the synthesiser and is labelled as carrying no weight, yet it is listed here
- src: ramonedaBuildingGenomebasedUnderstanding2023, chakravertiwuerthweinPhylogeneticCoherenceMicrobiome2026, lennonMappingNicheSpace2012, morrisseyEvolutionaryHistoryInfluences2015, farrellBacterialGrowthTemperature2024, gobernaPredictingMicrobialTraits2016, barnumPredictingMicrobialGrowth2024
- trail: H1-06 §Verdict as delivered, §Adversarial

From the note:

> H1-06:A-006 [quote: Verdict as delivered] Evidence classes: measured (Ramoneda, preprint Chakraverti-Wuerthwein; engineered Lennon, Morrissey and Franklin), inferred (Farrell), modelled or compiled (Goberna and Verdu; Barnum, preprint).
>
> H1-06:C-029 [warning: Adversarial critique, full findings] - Goberna and Verdu 2016 [16]: the synthesiser could not re-open it but still quotes specific figures (mean -D+1 = 0.93, K = 0.16, 9.9% and 8.6%) and an internal-inconsistency claim. It is labelled as carrying no weight, but it is listed in the A1 verdict's evidence classes.
>

Not found in the cited text (where to look, not what is wrong): Part

## env-preference-depth.7 (claim)

Without Ramoneda et al. 2023, the only natural-system depth evidence left for any environmental preference is a single preprint, and Part A1 would move towards 'not measured in this setting' for natural systems.

- conf: not stated
- class: not stated
- holds: the review's sensitivity analysis
- src: ramonedaBuildingGenomebasedUnderstanding2023, chakravertiwuerthweinPhylogeneticCoherenceMicrobiome2026
- trail: H1-06 §Verdict as delivered, §6. Verdicts

From the note:

> H1-06:A-007 [quote: Verdict as delivered] Would change if one source were removed: yes.
>
> H1-06:A-008 [quote: Verdict as delivered] Without Ramoneda et al. 2023, the only natural-system depth evidence left for any environmental preference is a single preprint, and the part would move towards 'not measured in this setting' for natural systems.
>
> H1-06:A-024 [6. Verdicts] Removing Ramoneda et al. 2023 [13] would leave one natural-system preprint [29], and the verdict would move towards "not measured in this setting" for natural systems.
>

Not found in the cited text (where to look, not what is wrong): A1; holds: review

## metabolic-trait-depth.1 (claim)

The Part A2 depths are inferred from genome annotation, not measured phenotypically, except for the Biolog substrates in Martiny 2013.

- conf: not stated
- class: deriv (note: "inferred from genome annotation")
- holds: genome-encoded metabolic traits
- src: martinyPhylogeneticConservatismFunctional2013
- trail: H1-06 §3. Part A2, §Verdict as delivered

From the note:

> H1-06:B-0081 [3. Part A2: depth of conservation of genome-encoded metabolic traits] All of these results are inferred from genome annotation.
>
> H1-06:A-009 [quote: Verdict as delivered] Phylogenetic depth of conservation: genome-encoded metabolic traits**: Measured and inconsistent between methods, taxonomies or datasets (inferred from genomes, not measured phenotypically, except for the Biolog substrates in Martiny 2013).
>

Not found in the cited text (where to look, not what is wrong): Part; A2

## metabolic-trait-depth.2 (claim)

On 2,229 SEED genomes (26 phyla, 16S trees), 93% of 89 traits were non-randomly distributed.

- conf: not stated
- class: deriv (note: "inferred from genome annotation")
- limit: access (note: "I could not re-open Martiny 2013 (Europe PMC fullTextXML empty)")
- holds: SEED genomes on 16S trees; rests on two independent search-agent readings
- src: martinyPhylogeneticConservatismFunctional2013
- trail: H1-06 §3. Part A2, §Provenance

From the note:

> H1-06:B-0081 [3. Part A2: depth of conservation of genome-encoded metabolic traits] All of these results are inferred from genome annotation.
>
> H1-06:B-0082 [3. Part A2: depth of conservation of genome-encoded metabolic traits] **Ordering by complexity.** On 2,229 SEED genomes (26 phyla, 16S trees), 93% of 89 traits were non-randomly distributed [1].
>
> H1-06:B-0011 [info: Provenance] I could not re-open Martiny 2013 (Europe PMC fullTextXML empty) or Goberna and Verdu 2016 (OUP bot challenge), so the specific trait values from Martiny 2013 rest on two independent search-agent readings, and the two agents transcribed its overall tau_D range differently.
>

## metabolic-trait-depth.3 (claim)

Oxygenic photosynthesis had a median tau_D of about 0.10 to 0.11 (one clade), sulfate reduction 0.039 (20 clusters) and nitrogen fixation about 0.018 (54 clusters).

- conf: not stated
- class: deriv (note: "inferred from genome annotation")
- limit: access (critic: C-028)
- holds: 2,229 SEED genomes, 16S trees; load-bearing in the A2 verdict, but resting on a search agent's transcription that disagrees with another agent on the overall range; the synthesiser could not re-open it and the critic could not obtain it (PMC3603392, not OA)
- src: martinyPhylogeneticConservatismFunctional2013
- trail: H1-06 §3. Part A2, §Adversarial, §critic

From the note:

> H1-06:B-0081 [3. Part A2: depth of conservation of genome-encoded metabolic traits] All of these results are inferred from genome annotation.
>
> H1-06:B-0082 [3. Part A2: depth of conservation of genome-encoded metabolic traits] **Ordering by complexity.** On 2,229 SEED genomes (26 phyla, 16S trees), 93% of 89 traits were non-randomly distributed [1].
>
> H1-06:B-0083 [3. Part A2: depth of conservation of genome-encoded metabolic traits] Oxygenic photosynthesis had a median tau_D of about 0.10 to 0.11 (one clade).
>
> H1-06:B-0084 [3. Part A2: depth of conservation of genome-encoded metabolic traits] Sulfate reduction was 0.039 (20 clusters) and nitrogen fixation about 0.018 (54 clusters).
>
> H1-06:C-007 [danger: Critic: verdict partly supported] This is supported, but the load-bearing Martiny 2013 values were not re-checked by the synthesiser, which records an unresolved transcription discrepancy.
>
> H1-06:C-028 [warning: Adversarial critique, full findings] - Martiny et al. 2013 [1]: the synthesiser states it could not re-open the paper, yet the A2 ordering values (oxygenic photosynthesis 0.10 to 0.11, sulfate reduction 0.039, N fixation 0.018, Biolog < 0.011) are load-bearing in the A2 verdict and rest on a search agent's transcription that disagrees with another agent on the range. The critic could not obtain it via Europe PMC either (PMC3603392, not OA).
>

## metabolic-trait-depth.4 (claim)

Growth on each of 70 carbon substrates (Biolog phenotypes, 738 strains) had tau_D below 0.011.

- conf: not stated
- class: meas (note: "not measured phenotypically, except for the Biolog substrates")
- limit: access (critic: C-028)
- holds: Biolog phenotypes of 738 strains; the paper could not be re-opened by the synthesiser or obtained by the critic
- src: martinyPhylogeneticConservatismFunctional2013
- trail: H1-06 §3. Part A2, §Adversarial

From the note:

> H1-06:B-0085 [3. Part A2: depth of conservation of genome-encoded metabolic traits] Growth on each of 70 carbon substrates (Biolog phenotypes, 738 strains) was below 0.011.
>
> H1-06:A-009 [quote: Verdict as delivered] Phylogenetic depth of conservation: genome-encoded metabolic traits**: Measured and inconsistent between methods, taxonomies or datasets (inferred from genomes, not measured phenotypically, except for the Biolog substrates in Martiny 2013).
>
> H1-06:C-028 [warning: Adversarial critique, full findings] - Martiny et al. 2013 [1]: the synthesiser states it could not re-open the paper, yet the A2 ordering values (oxygenic photosynthesis 0.10 to 0.11, sulfate reduction 0.039, N fixation 0.018, Biolog < 0.011) are load-bearing in the A2 verdict and rest on a search agent's transcription that disagrees with another agent on the range. The critic could not obtain it via Europe PMC either (PMC3603392, not OA).
>

## metabolic-trait-depth.5 (claim)

Martiny et al. report that traits encoded by many genes sit deeper, with aerobic methane oxidation as a stated exception.

- conf: not stated
- class: deriv (note: "inferred from genome annotation")
- limit: access (note: "I could not re-open Martiny 2013 (Europe PMC fullTextXML empty)")
- holds: 2,229 SEED genomes, 16S trees
- src: martinyPhylogeneticConservatismFunctional2013
- trail: H1-06 §3. Part A2

From the note:

> H1-06:B-0081 [3. Part A2: depth of conservation of genome-encoded metabolic traits] All of these results are inferred from genome annotation.
>
> H1-06:B-0082 [3. Part A2: depth of conservation of genome-encoded metabolic traits] **Ordering by complexity.** On 2,229 SEED genomes (26 phyla, 16S trees), 93% of 89 traits were non-randomly distributed [1].
>
> H1-06:B-0086 [3. Part A2: depth of conservation of genome-encoded metabolic traits] The authors report that traits encoded by many genes sit deeper, with aerobic methane oxidation as a stated exception.
>
> H1-06:B-0011 [info: Provenance] I could not re-open Martiny 2013 (Europe PMC fullTextXML empty) or Goberna and Verdu 2016 (OUP bot challenge), so the specific trait values from Martiny 2013 rest on two independent search-agent readings, and the two agents transcribed its overall tau_D range differently.
>

## metabolic-trait-depth.6 (claim)

The two search agents transcribed Martiny et al.'s overall tau_D range differently, 0.0011 to 0.101 quoted directly by one and 0.0029 to 0.11 by the other, and the discrepancy is unresolved.

- conf: not stated
- class: not stated
- limit: access (note: "I could not re-open the paper to resolve this")
- holds: the overall range in Martiny et al. 2013; the specific trait values are the load-bearing ones
- src: martinyPhylogeneticConservatismFunctional2013
- trail: H1-06 §3. Part A2, §critic

From the note:

> H1-06:B-0087 [3. Part A2: depth of conservation of genome-encoded metabolic traits] (The two search agents transcribed the overall range differently, 0.0011 to 0.101 quoted directly by one and 0.0029 to 0.11 by the other.
>
> H1-06:B-0088 [3. Part A2: depth of conservation of genome-encoded metabolic traits] I could not re-open the paper to resolve this, so the specific trait values above are the load-bearing ones.
>
> H1-06:C-007 [danger: Critic: verdict partly supported] This is supported, but the load-bearing Martiny 2013 values were not re-checked by the synthesiser, which records an unresolved transcription discrepancy.
>

Not found in the cited text (where to look, not what is wrong): holds: in

## metabolic-trait-depth.7 (claim)

Single enzymes are shallow: alkaline phosphatase, chitinase and beta-N-acetylglucosaminidase had tau_D 0.0098, 0.0080 and 0.0097, about 98% 16S identity.

- conf: not stated
- class: deriv (note: "inferred from genome annotation")
- holds: 3,058 sequenced prokaryotic genomes
- src: zimmermanMicrodiversityExtracellularEnzyme2013
- trail: H1-06 §3. Part A2, §References

From the note:

> H1-06:B-0081 [3. Part A2: depth of conservation of genome-encoded metabolic traits] All of these results are inferred from genome annotation.
>
> H1-06:B-0089 [3. Part A2: depth of conservation of genome-encoded metabolic traits] Single enzymes are shallow.
>
> H1-06:B-0090 [3. Part A2: depth of conservation of genome-encoded metabolic traits] Alkaline phosphatase, chitinase and beta-N-acetylglucosaminidase had tau_D 0.0098, 0.0080 and 0.0097, about 98% 16S identity, on 3,058 genomes [2].
>
> H1-06:R-0086 [References] Microdiversity of extracellular enzyme genes among sequenced prokaryotic genomes.
>

## metabolic-trait-depth.8 (claim)

Cellulase had tau_D 0.013 and beta-glucosidase 0.034.

- conf: not stated
- class: deriv (note: "inferred from genome annotation")
- holds: 5,123 genomes
- src: berlemontPhylogeneticDistributionPotential2013
- trail: H1-06 §3. Part A2

From the note:

> H1-06:B-0081 [3. Part A2: depth of conservation of genome-encoded metabolic traits] All of these results are inferred from genome annotation.
>
> H1-06:B-0091 [3. Part A2: depth of conservation of genome-encoded metabolic traits] On 5,123 genomes, cellulase had 0.013 and beta-glucosidase 0.034 [3].
>

## metabolic-trait-depth.9 (claim)

CAZyme traits had significant signal in most phyla, with depth varying by phylum (conserved-clade 16S divergence of 3 to 10% in Verrucomicrobiota and 0.1 to 0.5% in Firmicutes_A); beta-glucanases were significant in 73% of phyla tested, against 25% for alpha-glucanases.

- conf: single (note: "SINGLE SOURCE")
- class: deriv (note: "inferred from genome annotation")
- holds: natural; 9,143 high-quality MAGs from the GEM catalogue, GTDB phyla
- src: lopezmondejarGlobalDistributionCarbohydrate2022
- trail: H1-06 §3. Part A2

From the note:

> H1-06:B-0081 [3. Part A2: depth of conservation of genome-encoded metabolic traits] All of these results are inferred from genome annotation.
>
> H1-06:B-0092 [3. Part A2: depth of conservation of genome-encoded metabolic traits] In 9,143 high-quality MAGs from the GEM catalogue (GTDB phyla), CAZyme traits had significant signal in most phyla.
>
> H1-06:B-0093 [3. Part A2: depth of conservation of genome-encoded metabolic traits] Depth varied by phylum, with conserved-clade 16S divergence of 3 to 10% in Verrucomicrobiota and 0.1 to 0.5% in Firmicutes_A.
>
> H1-06:B-0094 [3. Part A2: depth of conservation of genome-encoded metabolic traits] Beta-glucanases were significant in 73% of phyla tested, against 25% for alpha-glucanases [5] (natural, SINGLE SOURCE).
>

Not found in the cited text (where to look, not what is wrong): Firmicutes_A

## metabolic-trait-depth.10 (claim)

The relative ordering of depths replicates across several studies on 16S trees: complex multi-gene pathways are deep (oxygenic photosynthesis about 0.10 to 0.11 16S distance; sulfate reduction 0.039), nitrogen fixation is intermediate (about 0.018), and single enzymes and substrate use are shallow (about 0.008 to 0.034).

- conf: repl (note: "replicates across independent datasets")
- class: deriv (note: "inferred from genomes")
- holds: 16S trees; the critic: supported, but the load-bearing Martiny 2013 values were not re-checked by the synthesiser, which records an unresolved transcription discrepancy
- src: martinyPhylogeneticConservatismFunctional2013, zimmermanMicrodiversityExtracellularEnzyme2013, berlemontPhylogeneticDistributionPotential2013, sunPhylogeneticDistributionPolysaccharideDegrading2021, lopezmondejarGlobalDistributionCarbohydrate2022
- trail: H1-06 §3. Part A2, §Verdict as delivered, §6. Verdicts, §critic

From the note:

> H1-06:A-010 [quote: Verdict as delivered] The relative ordering replicates across several studies on 16S trees: complex multi-gene pathways are deep (oxygenic photosynthesis about 0.10 to 0.11 16S distance; sulfate reduction 0.039), nitrogen fixation is intermediate (about 0.018), and single enzymes and substrate use are shallow (about 0.008 to 0.034).
>
> H1-06:A-026 [6. Verdicts] The ordering by complexity is consistent; the absolute depths are not.
>
> H1-06:B-0114 [3. Part A2: depth of conservation of genome-encoded metabolic traits] **Synthesis for A2.** The ordering from deep complex pathways to shallow single enzymes replicates across independent datasets [1, 2, 3, 4, 5].
>
> H1-06:A-009 [quote: Verdict as delivered] Phylogenetic depth of conservation: genome-encoded metabolic traits**: Measured and inconsistent between methods, taxonomies or datasets (inferred from genomes, not measured phenotypically, except for the Biolog substrates in Martiny 2013).
>
> H1-06:C-006 [danger: Critic: verdict partly supported] A2 (metabolic traits): measured (inferred from genomes) and inconsistent in absolute depth between datasets and trees, while the relative ordering is consistent.
>
> H1-06:C-007 [danger: Critic: verdict partly supported] This is supported, but the load-bearing Martiny 2013 values were not re-checked by the synthesiser, which records an unresolved transcription discrepancy.
>

## depth-dataset-dependence.1 (claim)

In 2,730 marine genomes, chitinase tau_D was 0.0281 on a 16S tree and 0.0444 on a core-gene tree, three to five times Zimmerman's 0.008.

- conf: not stated
- class: not stated
- holds: 2,730 marine genomes; a 16S tree and a core-gene tree
- src: sunPhylogeneticDistributionPolysaccharideDegrading2021, zimmermanMicrodiversityExtracellularEnzyme2013
- trail: H1-06 §3. Part A2, §Verdict as delivered

From the note:

> H1-06:B-0095 [3. Part A2: depth of conservation of genome-encoded metabolic traits] **Dataset and tree dependence.** In 2,730 marine genomes, chitinase tau_D was 0.0281 on a 16S tree and 0.0444 on a core-gene tree [4], three to five times Zimmerman's 0.008 [2].
>
> H1-06:A-011 [quote: Verdict as delivered] Absolute depths for the same trait differ between datasets and trees: chitinase 0.008 (Zimmerman 2013) against 0.028 on a 16S tree and 0.044 on a core-gene tree (Sun 2021).
>

## depth-dataset-dependence.2 (claim)

The authors attribute the difference to a denser sample of trait-positive genomes and state that tau_D values from different trees are not comparable.

- conf: not stated
- class: not stated
- holds: 2,730 marine genomes, 16S and core-gene trees
- src: sunPhylogeneticDistributionPolysaccharideDegrading2021
- trail: H1-06 §3. Part A2

From the note:

> H1-06:B-0095 [3. Part A2: depth of conservation of genome-encoded metabolic traits] **Dataset and tree dependence.** In 2,730 marine genomes, chitinase tau_D was 0.0281 on a 16S tree and 0.0444 on a core-gene tree [4], three to five times Zimmerman's 0.008 [2].
>
> H1-06:B-0096 [3. Part A2: depth of conservation of genome-encoded metabolic traits] The authors attribute the difference to a denser sample of trait-positive genomes and state that tau_D values from different trees are not comparable.
>

## depth-dataset-dependence.3 (claim)

Depending on the enzyme, 13.5 to 100% of trait-positive genomes were singletons; singleton clusters are common.

- conf: not stated
- class: not stated
- holds: 2,730 marine genomes
- src: sunPhylogeneticDistributionPolysaccharideDegrading2021
- trail: H1-06 §3. Part A2, §5. Bounds

From the note:

> H1-06:B-0095 [3. Part A2: depth of conservation of genome-encoded metabolic traits] **Dataset and tree dependence.** In 2,730 marine genomes, chitinase tau_D was 0.0281 on a 16S tree and 0.0444 on a core-gene tree [4], three to five times Zimmerman's 0.008 [2].
>
> H1-06:B-0097 [3. Part A2: depth of conservation of genome-encoded metabolic traits] Depending on the enzyme, 13.5 to 100% of trait-positive genomes were singletons.
>
> H1-06:B-0156 [5. Bounds and failure modes] Singleton clusters are common [4].
>

## depth-dataset-dependence.4 (claim)

Martiny et al. call their estimates "an upper bound for many functions" because many trait carriers sit in clusters of one: tau_D is an upper bound under undersampling, and the original authors call their depths upper bounds because of undersampling.

- conf: not stated
- class: not stated
- holds: consenTRAIT depths on undersampled trees
- src: martinyPhylogeneticConservatismFunctional2013
- trail: H1-06 §3. Part A2, §5. Bounds, §Verdict as delivered

From the note:

> H1-06:B-0098 [3. Part A2: depth of conservation of genome-encoded metabolic traits] Martiny et al. likewise call their estimates "an upper bound for many functions" because many trait carriers sit in clusters of one [1].
>
> H1-06:B-0155 [5. Bounds and failure modes] - tau_D is an upper bound under undersampling [1].
>
> H1-06:A-013 [quote: Verdict as delivered] The original authors call their depths upper bounds because of undersampling.
>

## depth-dataset-dependence.5 (claim)

On gene-content coherence, 44 coherent nodes appeared at 16S distances of 0.03 to 0.25 on a 16S tree but only five deep coherent subtrees on a GTDB 120-protein tree; class Actinobacteria was coherent while the shallower family Enterobacteriaceae was not.

- conf: single (note: "SINGLE SOURCE")
- class: not stated
- holds: a 16S tree against a GTDB 120-protein tree
- src: parrasmoltoAssessmentPhylofunctionalCoherence2021
- trail: H1-06 §3. Part A2, §Verdict as delivered

From the note:

> H1-06:B-0099 [3. Part A2: depth of conservation of genome-encoded metabolic traits] On gene-content coherence, 44 coherent nodes appeared at 16S distances of 0.03 to 0.25 on a 16S tree but only five deep coherent subtrees on a GTDB 120-protein tree [7].
>
> H1-06:B-0100 [3. Part A2: depth of conservation of genome-encoded metabolic traits] Class Actinobacteria was coherent while the shallower family Enterobacteriaceae was not (SINGLE SOURCE).
>
> H1-06:A-012 [quote: Verdict as delivered] Functional coherence nodes also differ between 16S and GTDB 120-protein trees (Parras-Molto 2021), and rank-wise partitioning is non-monotonic (GTDB: phylum 14.6%, order 9.2%, genus 5.5%; Royalty and Steen 2019).
>

## depth-dataset-dependence.6 (claim)

For genome-encoded metabolic traits, depth of conservation is measured (inferred from genomes) and inconsistent in absolute depth between datasets and trees, while the relative ordering is consistent: absolute depths move with genome sampling density and tree choice, and their own authors describe them as upper bounds.

- conf: not stated
- class: deriv (note: "inferred from genomes")
- rating: "Measured and inconsistent between methods, taxonomies or datasets"
- holds: the critic: supported by the body, but the load-bearing Martiny 2013 values were not re-checked by the synthesiser
- src: sunPhylogeneticDistributionPolysaccharideDegrading2021, parrasmoltoAssessmentPhylofunctionalCoherence2021, martinyPhylogeneticConservatismFunctional2013
- trail: H1-06 §critic, §Verdict as delivered, §6. Verdicts, §3. Part A2

From the note:

> H1-06:A-009 [quote: Verdict as delivered] Phylogenetic depth of conservation: genome-encoded metabolic traits**: Measured and inconsistent between methods, taxonomies or datasets (inferred from genomes, not measured phenotypically, except for the Biolog substrates in Martiny 2013).
>
> H1-06:A-025 [6. Verdicts] - **A2, genome-encoded metabolic traits:** measured and inconsistent between methods, taxonomies or datasets (inferred).
>
> H1-06:A-026 [6. Verdicts] The ordering by complexity is consistent; the absolute depths are not.
>
> H1-06:B-0115 [3. Part A2: depth of conservation of genome-encoded metabolic traits] Absolute depths for the same trait do not: they move with genome sampling density and tree choice [4, 7], and their own authors describe them as upper bounds [1].
>
> H1-06:C-006 [danger: Critic: verdict partly supported] A2 (metabolic traits): measured (inferred from genomes) and inconsistent in absolute depth between datasets and trees, while the relative ordering is consistent.
>
> H1-06:C-007 [danger: Critic: verdict partly supported] This is supported, but the load-bearing Martiny 2013 values were not re-checked by the synthesiser, which records an unresolved transcription discrepancy.
>
> H1-06:C-011 [danger: Critic: verdict partly supported] A2 and B are broadly supported by the body.
>

## depth-dataset-dependence.7 (claim)

The 'inconsistent' label for metabolic traits rests mainly on Sun et al. 2021 (dataset and tree dependence of the same trait) together with Parras-Moltó et al. 2021; without Sun, 'measured, with depths, methods and taxonomy stated' would be defensible for the ordering.

- conf: not stated
- class: not stated
- holds: the review's sensitivity analysis
- src: sunPhylogeneticDistributionPolysaccharideDegrading2021, parrasmoltoAssessmentPhylofunctionalCoherence2021
- trail: H1-06 §Verdict as delivered, §6. Verdicts

From the note:

> H1-06:A-014 [quote: Verdict as delivered] Would change if one source were removed: the 'inconsistent' label rests mainly on Sun et al. 2021 (dataset and tree dependence of the same trait) together with Parras-Molto et al. 2021.
>
> H1-06:A-015 [quote: Verdict as delivered] Without Sun, 'measured, with depths, methods and taxonomy stated' would be defensible for the ordering.
>
> H1-06:A-027 [6. Verdicts] The inconsistency label leans chiefly on Sun et al. 2021 [4], with Parras-Moltó et al. 2021 [7].
>

Not found in the cited text (where to look, not what is wrong): holds: review

