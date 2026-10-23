## genome-incompleteness.6 (claim)

Incompleteness pushed detected function down in single-source tests of modules, core genes and reference bias, with the size of the effect depending on module and phylum; the evidence is indirect but consistent in direction, and none of it measures the effect on conservation depth.

- conf: single (critic: C-034)
- class: not stated
- holds: KEGG modules (modelled on subsampled complete genomes), core gene families (modelled) and reference genomes, one source each
- src: eisenhoferImpactMicrobialGenome2023, liCriticalAssessmentPangenomic2022, albrightTraitBiasesMicrobial2023
- trail: H1-06 §5. Bounds, §3. Part A2, §Adversarial

From the note:

> H1-06:B-0157 [5. Bounds and failure modes] - Incompleteness pushes detected function down, and the size of the effect depends on module and phylum [9, 10, 11].
>
> H1-06:B-0158 [5. Bounds and failure modes] Its effect on depth estimates themselves has not been measured in any source read.
>
> H1-06:B-0106 [3. Part A2: depth of conservation of genome-encoded metabolic traits] The evidence is indirect but consistent in direction.
>
> H1-06:C-034 [warning: Adversarial critique, full findings] - 'Incompleteness pushes detected function down' (Section 5) is phrased generally. Each quantitative element is SINGLE SOURCE ([9] modules, [10] core genes, [11] reference bias), and none measures the effect on conservation depth, which the review does concede.
>
> H1-06:B-0107 [3. Part A2: depth of conservation of genome-encoded metabolic traits] Going from 70% to 100% completeness raised KEGG module fullness by 15 ± 10% [9] (modelled on subsampled complete genomes, SINGLE SOURCE).
>
> H1-06:B-0110 [3. Part A2: depth of conservation of genome-encoded metabolic traits] Removing 1% of sequence from each genome cut detected core gene families by more than 60% across 17 species; relaxing the core threshold to 90 to 95% eased this [10] (modelled, SINGLE SOURCE).
>

## rankwise-structuring.9 (claim)

Community turnover was stronger at ASV resolution (an 82% drop in similarity over 160 km, against 50 to 60% for clustered or filtered data), but "less variation in community composition could be explained and partitioned for the high-resolution data set", and the rank order of predictors changed. The comparison is of the high-resolution set against clustered and/or rare-taxon-filtered data, by incidence-based variation partitioning.

- conf: not stated
- class: not stated
- holds: soils in the Negev; no ranks, only sequence-identity thresholds; one of the uncontrolled rank-wise studies
- src: baySoilBacterialCommunities2020
- trail: H1-06 §4. Part B, §critic, §References

From the note:

> H1-06:B-0136 [4. Part B: environmental structuring of composition from fine to coarse ranks] In the Negev (ASVs against 97% OTUs only) [25], turnover was stronger at ASV resolution (an 82% drop in similarity over 160 km against 50 to 60% for clustered or filtered data).
>
> H1-06:B-0137 [4. Part B: environmental structuring of composition from fine to coarse ranks] However, "less variation in community composition could be explained and partitioned for the high-resolution data set", and the rank order of predictors changed.
>
> H1-06:C-020 [danger: Critic: verdict partly supported] In full text, Bay compares the high-resolution set against 'filtered ones' (clustered and/or rare-taxon-filtered data) using incidence-based variation partitioning, so the paraphrase reduces a clustering-plus-filtering contrast to clustering alone.
>
> H1-06:R-0151 [References] Soil bacterial communities exhibit strong biogeographic patterns at fine taxonomic resolution. mSystems 5(4): e00540-20. doi:10.1128/mSystems.00540-20
>
> H1-06:B-0023 [1. What is being compared] Rank-wise analyses of community composition use taxonomies, not trees, and the taxonomy differs between studies: Greengenes [23], SILVA or RDP [13, 14, 19], GTDB [5, 6, 8, 12], a curated gyrB taxonomy [24], or no ranks at all, only sequence-identity thresholds [25, 26, 27].
>
> H1-06:B-0162 [5. Bounds and failure modes] The other rank-wise studies are uncontrolled, and two are preprints [24, 29].
>

