## rank-partitioning.1 (claim)

With GTDB ranks, ranks together explained 41.4% of the variance in 25 COG categories normalised for genome size: domain 3.2%, phylum 14.6%, class 4.1%, order 9.2%, family 4.8%, genus 5.5%; the contribution is non-monotonic across ranks.

- conf: single (critic: C-035)
- class: not stated
- holds: 13,735 lineages, GTDB ranks; the critic: correctly flagged single source in the body, but it carries weight in the A2 verdict without that flag
- src: royaltyQuantitativelyPartitioningMicrobial2019
- trail: H1-06 §3. Part A2, §Adversarial

From the note:

> H1-06:B-0101 [3. Part A2: depth of conservation of genome-encoded metabolic traits] **Rank partitioning.** With GTDB ranks, 13,735 lineages and 25 COG categories normalised for genome size, ranks together explained 41.4% of variance: domain 3.2%, phylum 14.6%, class 4.1%, order 9.2%, family 4.8%, genus 5.5% [6] (SINGLE SOURCE).
>
> H1-06:B-0102 [3. Part A2: depth of conservation of genome-encoded metabolic traits] The contribution is non-monotonic across ranks.
>
> H1-06:C-035 [warning: Adversarial critique, full findings] - The Royalty and Steen rank partition (phylum 14.6%, order 9.2%, genus 5.5%) is cited in the A2 verdict as showing that 'rank-wise partitioning is non-monotonic'. It is correctly flagged SINGLE SOURCE in the body but carries weight in the verdict without that flag.
>
> H1-06:A-012 [quote: Verdict as delivered] Functional coherence nodes also differ between 16S and GTDB 120-protein trees (Parras-Molto 2021), and rank-wise partitioning is non-monotonic (GTDB: phylum 14.6%, order 9.2%, genus 5.5%; Royalty and Steen 2019).
>

## rank-partitioning.2 (claim)

Apparent within-phylum variability rose with the number of lineages sampled and levelled off after about 100 genomes, so undersampled phyla look falsely uniform.

- conf: single (note: "SINGLE SOURCE")
- class: not stated
- holds: 13,735 lineages, GTDB ranks, COG categories
- src: royaltyQuantitativelyPartitioningMicrobial2019
- trail: H1-06 §3. Part A2

From the note:

> H1-06:B-0101 [3. Part A2: depth of conservation of genome-encoded metabolic traits] **Rank partitioning.** With GTDB ranks, 13,735 lineages and 25 COG categories normalised for genome size, ranks together explained 41.4% of variance: domain 3.2%, phylum 14.6%, class 4.1%, order 9.2%, family 4.8%, genus 5.5% [6] (SINGLE SOURCE).
>
> H1-06:B-0103 [3. Part A2: depth of conservation of genome-encoded metabolic traits] Apparent within-phylum variability rose with the number of lineages sampled and levelled off after about 100 genomes, so undersampled phyla look falsely uniform.
>

## rank-partitioning.3 (claim)

Autotrophy and maximum growth rate had weaker signal than oxygen tolerance and GC content, and at least 25% of variance in four traits fell at a single split.

- conf: not stated
- class: not stated
- holds: 50,745 GTDB genomes
- src: hoffertConstructingPeriodicTable2026
- trail: H1-06 §3. Part A2

From the note:

> H1-06:B-0104 [3. Part A2: depth of conservation of genome-encoded metabolic traits] Across 50,745 GTDB genomes, autotrophy and maximum growth rate had weaker signal than oxygen tolerance and GC content, and at least 25% of variance in four traits fell at a single split [8].
>

## genome-incompleteness.1 (claim)

No study found tests directly how genome incompleteness biases tau_D or signal statistics; its effect on depth estimates themselves has not been measured in any source read.

- conf: not stated
- class: search (note: "Not found by these routes")
- search: searched, not found (note: "(3) any direct test of how genome incompleteness biases tau_D or signal statistics")
- holds: the review's search, whose routes are listed in the note's provenance (including WebSearch on genome completeness with functional inference); the critic: the routes behind this not-found are not named in the body
- src: none (a search result)
- trail: H1-06 §3. Part A2, §5. Bounds, §Provenance, §Adversarial

From the note:

> H1-06:B-0105 [3. Part A2: depth of conservation of genome-encoded metabolic traits] **Genome incompleteness.** No study found tests directly how incompleteness biases tau_D or signal statistics.
>
> H1-06:B-0158 [5. Bounds and failure modes] Its effect on depth estimates themselves has not been measured in any source read.
>
> H1-06:B-0008 [info: Provenance] Routes behind every 'not found': Europe PMC REST keyword, DOI and title search plus fullTextXML; the 'consenTRAIT AND OPEN_ACCESS' query (23 hits screened); citing papers of Lu et al. 2016 screened by title; PMC HTML; publisher pages; bioRxiv; the Lennon lab PDF archive; WebSearch on taxonomic sufficiency, taxonomic resolution with explained variation, ecological coherence with ranks, genome completeness with functional inference, and phylogenetic signal of optimal growth temperature.
>
> H1-06:B-0009 [info: Provenance] Not found by these routes: (1) any consenTRAIT tau_D for pH, temperature or moisture optima; (2) any rank-wise composition-environment study, other than Lu 2016, that controls group number and size (Schmidt 2014 controls them, but for identity thresholds and annotation consistency, not ranks); (3) any direct test of how genome incompleteness biases tau_D or signal statistics.
>
> H1-06:C-051 [warning: Adversarial critique, full findings] - gap: No study found that directly tests how genome incompleteness biases tau_D or phylogenetic signal. The search routes behind this 'not found' are not named in the body, which Common rule 7 requires.; setting_or_class: MAG-based consenTRAIT or signal analyses (e.g. GEM catalogue, GTDB MAG-inclusive trees); brief_bullet: How incompleteness of genomes changes conservation estimates
>

Not found in the cited text (where to look, not what is wrong): holds: review

## genome-incompleteness.2 (claim)

Going from 70% to 100% completeness raised KEGG module fullness by 15 ± 10%; the bias was positive for 94% of 195 modules, persisted above 90% completeness, and was largest in Proteobacteria and in modules with few steps.

- conf: single (note: "SINGLE SOURCE")
- class: model (note: "modelled on subsampled complete genomes")
- holds: subsampled complete genomes
- src: eisenhoferImpactMicrobialGenome2023
- trail: H1-06 §3. Part A2

From the note:

> H1-06:B-0107 [3. Part A2: depth of conservation of genome-encoded metabolic traits] Going from 70% to 100% completeness raised KEGG module fullness by 15 ± 10% [9] (modelled on subsampled complete genomes, SINGLE SOURCE).
>
> H1-06:B-0108 [3. Part A2: depth of conservation of genome-encoded metabolic traits] The bias was positive for 94% of 195 modules, persisted above 90% completeness, and was largest in Proteobacteria and in modules with few steps.
>

## genome-incompleteness.3 (claim)

Subsampling a complete Pseudomonas aeruginosa genome to 70% moved its functional profile towards Bacillus subtilis.

- conf: not stated
- class: model (note: "modelled on subsampled complete genomes")
- holds: one complete genome, subsampled
- src: eisenhoferImpactMicrobialGenome2023
- trail: H1-06 §3. Part A2

From the note:

> H1-06:B-0107 [3. Part A2: depth of conservation of genome-encoded metabolic traits] Going from 70% to 100% completeness raised KEGG module fullness by 15 ± 10% [9] (modelled on subsampled complete genomes, SINGLE SOURCE).
>
> H1-06:B-0109 [3. Part A2: depth of conservation of genome-encoded metabolic traits] Subsampling a complete Pseudomonas aeruginosa genome to 70% moved its functional profile towards Bacillus subtilis.
>

## genome-incompleteness.4 (claim)

Removing 1% of sequence from each genome cut detected core gene families by more than 60% across 17 species; relaxing the core threshold to 90 to 95% eased this.

- conf: single (note: "SINGLE SOURCE")
- class: model (note: "modelled")
- holds: 17 species; modelled
- src: liCriticalAssessmentPangenomic2022
- trail: H1-06 §3. Part A2

From the note:

> H1-06:B-0110 [3. Part A2: depth of conservation of genome-encoded metabolic traits] Removing 1% of sequence from each genome cut detected core gene families by more than 60% across 17 species; relaxing the core threshold to 90 to 95% eased this [10] (modelled, SINGLE SOURCE).
>

## genome-incompleteness.5 (claim)

For 116,884 MAGs against RefSeq, raw gene detection rates fell below model-corrected prevalences, and most KEGG orthologs were biased between culture-heavy and MAG references.

- conf: single (critic: C-034)
- class: not stated
- holds: MAGs against RefSeq references
- src: albrightTraitBiasesMicrobial2023
- trail: H1-06 §3. Part A2, §Adversarial

From the note:

> H1-06:B-0111 [3. Part A2: depth of conservation of genome-encoded metabolic traits] For 116,884 MAGs against RefSeq, raw gene detection rates fell below model-corrected prevalences, and most KEGG orthologs were biased between culture-heavy and MAG references [11].
>
> H1-06:C-034 [warning: Adversarial critique, full findings] - 'Incompleteness pushes detected function down' (Section 5) is phrased generally. Each quantitative element is SINGLE SOURCE ([9] modules, [10] core genes, [11] reference bias), and none measures the effect on conservation depth, which the review does concede.
>

## genome-incompleteness.6 (claim)

Incompleteness pushed detected function down in single-source tests of modules, core genes and reference bias, with the size of the effect depending on module and phylum; the evidence is indirect but consistent in direction, and none of it measures the effect on conservation depth.

- conf: single (critic: C-034)
- class: not stated
- holds: KEGG modules, core gene families and reference genomes, one source each
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

Not found in the cited text (where to look, not what is wrong): holds: kegg

## genome-incompleteness.7 (claim)

Consensus-threshold methods such as consenTRAIT (90% sharing) are exposed to false absences, which would fragment clades and push depth estimates shallower.

- conf: not stated
- class: reading (note: "Reviewer's reading, not tested by any source")
- holds: untested by any source; the critic: appropriately labelled as untested, but then echoed in Section 5 as a bound
- src: none (the reviewer's synthesis)
- trail: H1-06 §3. Part A2, §Adversarial

From the note:

> H1-06:B-0112 [3. Part A2: depth of conservation of genome-encoded metabolic traits] Reviewer's reading, not tested by any source: consensus-threshold methods such as consenTRAIT (90% sharing) are exposed to false absences, which would fragment clades and push depth estimates shallower.
>
> H1-06:C-055 [warning: Adversarial critique, full findings] - The reviewer's reading that consensus-threshold methods would push depth estimates shallower under incompleteness is labelled as untested, which is appropriate, but it is then echoed in Section 5 as a bound.
>

## genome-incompleteness.8 (claim)

Amino-acid-based optimum predictions stayed stable down to 10% completeness for oxygen, temperature and salinity, while pH error reached 0.4 units.

- conf: not stated
- class: not stated
- holds: a preprint
- src: barnumPredictingMicrobialGrowth2024
- trail: H1-06 §3. Part A2

From the note:

> H1-06:B-0113 [3. Part A2: depth of conservation of genome-encoded metabolic traits] Barnum et al. report amino-acid-based optimum predictions stable down to 10% completeness for oxygen, temperature and salinity, while pH error reached 0.4 units [12] (preprint).
>

## group-size-control.1 (claim)

Lu et al. handled group number and group size with a null that "shuffled linkages between fine-taxa and broad-taxa level by level (remaining topology)", using 100 random linkage maps (tip-label shuffling for UniFrac); under this null, explained variance "remained constant or slightly decreased" with rank.

- conf: not stated
- class: not stated
- limit: access (critic: C-017)
- holds: the eight soil and seawater datasets Lu et al. reanalysed; the critic could not obtain the Methods and Results (nature.com paywall; not open access), so the null-model description rests on the search agent's reading; the note's provenance says the synthesiser re-opened cached full text for the null model
- src: luEvaluatingCommunityenvironmentRelationships2016
- trail: H1-06 §4. Part B, §critic, §Adversarial, §Provenance

From the note:

> H1-06:B-0116 [4. Part B: environmental structuring of composition from fine to coarse ranks] **The one controlled study.** Lu et al. 2016 [23] (measured, natural) reanalysed eight datasets: four surface soils (n = 40 to 580) and four seawater.
>
> H1-06:B-0125 [4. Part B: environmental structuring of composition from fine to coarse ranks] Group number and group size were handled by a null that "shuffled linkages between fine-taxa and broad-taxa level by level (remaining topology)", using 100 random linkage maps (tip-label shuffling for UniFrac).
>
> H1-06:B-0126 [4. Part B: environmental structuring of composition from fine to coarse ranks] Under this null, explained variance "remained constant or slightly decreased" with rank.
>
> H1-06:B-0010 [info: Provenance] Synthesis checks: I re-opened cached full text for Lu 2016 (null model, soil peak at class, significance above the null, 50% rise from otu97 to otu94), Ramoneda 2023 (lambda, Moran's I, phylum-level quote), Lennon 2012, Bay 2020 (confirmed that ASV-level data explain less composition variance than clustered data; both search agents' statements are correct), Mayjonade 2024 and Quiroga 2022.
>
> H1-06:C-017 [danger: Critic: verdict partly supported] I could not obtain the Methods and Results (nature.com paywall; PMC5148199 is not open access), so the null-model description and the soil class-peak details rest on the search agent's reading.
>
> H1-06:C-025 [warning: Adversarial critique, full findings] - Lu et al. 2016 [23]: the synthesiser presents the null model ('shuffled linkages ... remaining topology', 100 random linkage maps), the soil class peak, the '>= 50% R2 increase otu97 to otu94' and the per-dataset seawater shapes as verified.
>
> H1-06:C-026 [warning: Adversarial critique, full findings] The critic could only confirm the abstract (nature.com paywalled; PMC5148199 flagged not open access).
>
> H1-06:C-027 [warning: Adversarial critique, full findings] These details are load-bearing for the B verdict ('group number and size controlled'), and the review does not say whether the synthesiser re-opened the full text.
>

## group-size-control.2 (claim)

By preserving topology, the null holds the count of groups per level and the number of fine taxa per group fixed; it does not hold abundance evenness among groups fixed.

- conf: not stated
- class: reading (note: "Reviewer's reading")
- holds: Lu et al.'s topology-preserving null; the critic: the caveat about evenness is appropriate, and abundance evenness among groups was not controlled
- src: luEvaluatingCommunityenvironmentRelationships2016
- trail: H1-06 §4. Part B, §critic

From the note:

> H1-06:B-0129 [4. Part B: environmental structuring of composition from fine to coarse ranks] Reviewer's reading: by preserving topology, the null holds the count of groups per level and the number of fine taxa per group fixed.
>
> H1-06:B-0130 [4. Part B: environmental structuring of composition from fine to coarse ranks] It does not hold abundance evenness among groups fixed.
>
> H1-06:C-010 [danger: Critic: verdict partly supported] Abundance evenness among groups was not controlled.
>
> H1-06:C-018 [danger: Critic: verdict partly supported] The review's own caveat about evenness is appropriate.
>

Not found in the cited text (where to look, not what is wrong): holds: lu

## group-size-control.3 (claim)

No rank-wise composition-environment study other than Lu 2016 was found that controls group number and size; Schmidt 2014 controls them, but for identity thresholds and annotation consistency, not ranks.

- conf: not stated
- class: search (note: "Not found by these routes")
- search: searched, not found (note: "(2) any rank-wise composition-environment study, other than Lu 2016, that controls group number and size")
- holds: routes include citing papers of Lu et al. 2016 screened by title, and WebSearch on taxonomic sufficiency, taxonomic resolution with explained variation and ecological coherence with ranks
- src: none (a search result)
- trail: H1-06 §Provenance

From the note:

> H1-06:B-0008 [info: Provenance] Routes behind every 'not found': Europe PMC REST keyword, DOI and title search plus fullTextXML; the 'consenTRAIT AND OPEN_ACCESS' query (23 hits screened); citing papers of Lu et al. 2016 screened by title; PMC HTML; publisher pages; bioRxiv; the Lennon lab PDF archive; WebSearch on taxonomic sufficiency, taxonomic resolution with explained variation, ecological coherence with ranks, genome completeness with functional inference, and phylogenetic signal of optimal growth temperature.
>
> H1-06:B-0009 [info: Provenance] Not found by these routes: (1) any consenTRAIT tau_D for pH, temperature or moisture optima; (2) any rank-wise composition-environment study, other than Lu 2016, that controls group number and size (Schmidt 2014 controls them, but for identity thresholds and annotation consistency, not ranks); (3) any direct test of how genome incompleteness biases tau_D or signal statistics.
>

## rankwise-structuring.1 (claim)

Across eight reanalysed datasets, environment-explained variance of Bray-Curtis composition (db-RDA adjusted R2) "either increased or remained constant with broadening taxonomic resolution from species to order or even phylum level".

- conf: single (critic: C-008)
- class: meas (note: "measured, natural")
- holds: natural; four surface soils (n = 40 to 580) and four seawater datasets; closed-reference Greengenes 13_8 with copy-number correction, composition aggregated from otu97 to otu70 and from species to phylum; the critic confirmed this abstract sentence
- src: luEvaluatingCommunityenvironmentRelationships2016
- trail: H1-06 §4. Part B, §critic, §Verdict as delivered

From the note:

> H1-06:B-0116 [4. Part B: environmental structuring of composition from fine to coarse ranks] **The one controlled study.** Lu et al. 2016 [23] (measured, natural) reanalysed eight datasets: four surface soils (n = 40 to 580) and four seawater.
>
> H1-06:B-0117 [4. Part B: environmental structuring of composition from fine to coarse ranks] They used closed-reference Greengenes 13_8 with copy-number correction and aggregated composition from otu97 to otu70 and from species to phylum.
>
> H1-06:B-0118 [4. Part B: environmental structuring of composition from fine to coarse ranks] At every level they computed the environment-explained variance of Bray-Curtis composition (db-RDA adjusted R2).
>
> H1-06:B-0119 [4. Part B: environmental structuring of composition from fine to coarse ranks] Across all eight cases this "either increased or remained constant with broadening taxonomic resolution from species to order or even phylum level".
>
> H1-06:C-016 [danger: Critic: verdict partly supported] For B, I confirmed the quoted abstract sentence from Lu 2016 ('either increased or remained constant ... from species to order or even phylum level').
>
> H1-06:A-017 [quote: Verdict as delivered] Direction: environment-explained composition variance (db-RDA adjusted R2) rose or stayed constant from species towards order.
>
> H1-06:C-008 [danger: Critic: verdict partly supported] B: measured with group number (and member count) controlled, SINGLE SOURCE (Lu et al. 2016), and conditional on that paper's null design, which could not be re-verified here (paywalled; only the abstract was confirmed).
>

## rankwise-structuring.2 (claim)

In all four soils, R2 rose up to class (otu82 to otu76) and fell at phylum, with at least a 50% R2 increase from otu97 to otu94; pH was the strongest single variable.

- conf: single (critic: C-008)
- class: meas (note: "measured, natural")
- limit: access (critic: C-017)
- holds: four surface soils, Greengenes 13_8; the critic: the soil class-peak details rest on the search agent's reading, since the critic could confirm only the abstract
- src: luEvaluatingCommunityenvironmentRelationships2016
- trail: H1-06 §4. Part B, §critic, §Adversarial

From the note:

> H1-06:B-0116 [4. Part B: environmental structuring of composition from fine to coarse ranks] **The one controlled study.** Lu et al. 2016 [23] (measured, natural) reanalysed eight datasets: four surface soils (n = 40 to 580) and four seawater.
>
> H1-06:B-0117 [4. Part B: environmental structuring of composition from fine to coarse ranks] They used closed-reference Greengenes 13_8 with copy-number correction and aggregated composition from otu97 to otu70 and from species to phylum.
>
> H1-06:B-0121 [4. Part B: environmental structuring of composition from fine to coarse ranks] - Soils: R2 rose up to class (otu82 to otu76) and fell at phylum, with at least a 50% R2 increase from otu97 to otu94. pH was the strongest single variable.
>
> H1-06:A-018 [quote: Verdict as delivered] In all four soils it rose to class and then fell at phylum.
>
> H1-06:C-008 [danger: Critic: verdict partly supported] B: measured with group number (and member count) controlled, SINGLE SOURCE (Lu et al. 2016), and conditional on that paper's null design, which could not be re-verified here (paywalled; only the abstract was confirmed).
>
> H1-06:C-017 [danger: Critic: verdict partly supported] I could not obtain the Methods and Results (nature.com paywall; PMC5148199 is not open access), so the null-model description and the soil class-peak details rest on the search agent's reading.
>
> H1-06:C-025 [warning: Adversarial critique, full findings] - Lu et al. 2016 [23]: the synthesiser presents the null model ('shuffled linkages ... remaining topology', 100 random linkage maps), the soil class peak, the '>= 50% R2 increase otu97 to otu94' and the per-dataset seawater shapes as verified.
>

## rankwise-structuring.3 (claim)

In seawater the shape varied by dataset: peaks at intermediate ranks (Tara surface and DCM), flat from species to order then a drop at class and phylum (English Channel time series), and a continuous rise to phylum (East China Sea shelf).

- conf: single (critic: C-008)
- class: meas (note: "measured, natural")
- limit: access (critic: C-026)
- holds: four seawater datasets; the critic could confirm only the abstract, not the per-dataset seawater shapes
- src: luEvaluatingCommunityenvironmentRelationships2016
- trail: H1-06 §4. Part B, §Adversarial

From the note:

> H1-06:B-0116 [4. Part B: environmental structuring of composition from fine to coarse ranks] **The one controlled study.** Lu et al. 2016 [23] (measured, natural) reanalysed eight datasets: four surface soils (n = 40 to 580) and four seawater.
>
> H1-06:B-0120 [4. Part B: environmental structuring of composition from fine to coarse ranks] The shape varied by system:
>
> H1-06:B-0122 [4. Part B: environmental structuring of composition from fine to coarse ranks] - Tara surface and DCM: peaks at intermediate ranks.
>
> H1-06:B-0123 [4. Part B: environmental structuring of composition from fine to coarse ranks] - English Channel time series: flat from species to order, then a drop at class and phylum.
>
> H1-06:B-0124 [4. Part B: environmental structuring of composition from fine to coarse ranks] - East China Sea shelf: a continuous rise to phylum.
>
> H1-06:A-019 [quote: Verdict as delivered] In seawater it peaked at intermediate ranks (two datasets), was flat and then dropped at class and phylum (one), or rose continuously to phylum (one).
>
> H1-06:C-008 [danger: Critic: verdict partly supported] B: measured with group number (and member count) controlled, SINGLE SOURCE (Lu et al. 2016), and conditional on that paper's null design, which could not be re-verified here (paywalled; only the abstract was confirmed).
>
> H1-06:C-025 [warning: Adversarial critique, full findings] - Lu et al. 2016 [23]: the synthesiser presents the null model ('shuffled linkages ... remaining topology', 100 random linkage maps), the soil class peak, the '>= 50% R2 increase otu97 to otu94' and the per-dataset seawater shapes as verified.
>
> H1-06:C-026 [warning: Adversarial critique, full findings] The critic could only confirm the abstract (nature.com paywalled; PMC5148199 flagged not open access).
>

## rankwise-structuring.4 (claim)

In soils, the observed genus-to-class R2 was significantly above the topology-preserving shuffle null, which itself gave constant or slightly falling R2; the authors read the rise as phylogenetic niche conservatism.

- conf: single (critic: C-008)
- class: meas (note: "measured, natural")
- limit: access (critic: C-017)
- holds: four surface soils; the critic could not obtain the Methods and Results
- src: luEvaluatingCommunityenvironmentRelationships2016
- trail: H1-06 §4. Part B, §Verdict as delivered, §critic

From the note:

> H1-06:B-0116 [4. Part B: environmental structuring of composition from fine to coarse ranks] **The one controlled study.** Lu et al. 2016 [23] (measured, natural) reanalysed eight datasets: four surface soils (n = 40 to 580) and four seawater.
>
> H1-06:B-0127 [4. Part B: environmental structuring of composition from fine to coarse ranks] In soils the observed genus-to-class R2 was significantly above the null.
>
> H1-06:B-0128 [4. Part B: environmental structuring of composition from fine to coarse ranks] The authors read the rise as phylogenetic niche conservatism.
>
> H1-06:A-020 [quote: Verdict as delivered] A topology-preserving shuffle null gave constant or slightly falling R2, and in soils the observed genus-to-class R2 was significantly above that null.
>
> H1-06:C-008 [danger: Critic: verdict partly supported] B: measured with group number (and member count) controlled, SINGLE SOURCE (Lu et al. 2016), and conditional on that paper's null design, which could not be re-verified here (paywalled; only the abstract was confirmed).
>
> H1-06:C-017 [danger: Critic: verdict partly supported] I could not obtain the Methods and Results (nature.com paywall; PMC5148199 is not open access), so the null-model description and the soil class-peak details rest on the search agent's reading.
>

## rankwise-structuring.5 (claim)

Environmental structuring of community composition across ranks has been measured with group number (and member count) controlled, in a single source, conditional on that paper's null design: explained variance rises or stays constant from species to order, with dataset-specific falls at class or phylum (in soils it peaks at class and declines at phylum; in seawater the pattern varies by dataset); abundance evenness among groups was not controlled.

- conf: single (critic: C-008)
- class: not stated
- rating: "Measured with group number and size controlled, SINGLE SOURCE" (critic: C-008: conditional on that paper's null design, which could not be re-verified)
- limit: access (critic: C-008)
- holds: natural; 4 soil and 4 seawater datasets; Greengenes 13_8 ranks and OTU thresholds from 97% to 70%; the critic: the review departs from the brief's expectation that such evidence may not exist, plausibly, but on one source whose control design was not independently re-verified
- src: luEvaluatingCommunityenvironmentRelationships2016
- trail: H1-06 §Verdict as delivered, §6. Verdicts, §critic, §Adversarial

From the note:

> H1-06:A-016 [quote: Verdict as delivered] **B. Change in environmental structuring of community composition from fine to coarse ranks**: Measured with group number and size controlled, SINGLE SOURCE (Lu et al. 2016; natural; 4 soil and 4 seawater datasets; Greengenes 13_8 ranks and OTU thresholds from 97% to 70%).
>
> H1-06:A-028 [6. Verdicts] - **B, rank-wise environmental structuring:** measured with group number and size controlled, SINGLE SOURCE, Lu et al. 2016 [23].
>
> H1-06:A-029 [6. Verdicts] Direction: explained variance increases or stays constant from species to order; in soils it peaks at class and declines at phylum; in seawater the pattern varies by dataset.
>
> H1-06:C-008 [danger: Critic: verdict partly supported] B: measured with group number (and member count) controlled, SINGLE SOURCE (Lu et al. 2016), and conditional on that paper's null design, which could not be re-verified here (paywalled; only the abstract was confirmed).
>
> H1-06:C-009 [danger: Critic: verdict partly supported] Direction: explained variance rises or stays constant from species to order, with dataset-specific falls at class or phylum.
>
> H1-06:C-010 [danger: Critic: verdict partly supported] Abundance evenness among groups was not controlled.
>
> H1-06:C-011 [danger: Critic: verdict partly supported] A2 and B are broadly supported by the body.
>
> H1-06:C-057 [warning: Adversarial critique, full findings] **Expectation echo:** brief_states_expectation: True brief_wording: 'Direct evidence for rank-wise structuring with group size controlled may not exist.
>
> H1-06:C-058 [warning: Adversarial critique, full findings] If so, report that plainly.
>
> H1-06:C-059 [warning: Adversarial critique, full findings] This implies a Part B verdict of 'not measured in this setting'. review_repeats_it: False independent_support: The review departs from the expected verdict, citing Lu et al. 2016's topology-preserving shuffle null.
>
> H1-06:C-060 [warning: Adversarial critique, full findings] The critic confirmed Lu's abstract-level result but could not access the Methods to verify that the null holds group number and member count fixed.
>
> H1-06:C-061 [warning: Adversarial critique, full findings] The departure is therefore plausible but rests on one source whose control design was not independently re-verified, and abundance evenness is not controlled by the review's own account.
>
> H1-06:B-0131 [4. Part B: environmental structuring of composition from fine to coarse ranks] This study is SINGLE SOURCE for the controlled design.
>
> H1-06:B-0161 [5. Bounds and failure modes] - Part B rests on a single controlled reanalysis [23].
>
> H1-06:C-008 [danger: Critic: verdict partly supported] B: measured with group number (and member count) controlled, SINGLE SOURCE (Lu et al. 2016), and conditional on that paper's null design, which could not be re-verified here (paywalled; only the abstract was confirmed).
>
> H1-06:C-008 [danger: Critic: verdict partly supported] B: measured with group number (and member count) controlled, SINGLE SOURCE (Lu et al. 2016), and conditional on that paper's null design, which could not be re-verified here (paywalled; only the abstract was confirmed).
>
> H1-06:C-008 [danger: Critic: verdict partly supported] B: measured with group number (and member count) controlled, SINGLE SOURCE (Lu et al. 2016), and conditional on that paper's null design, which could not be re-verified here (paywalled; only the abstract was confirmed).
>

## rankwise-structuring.6 (claim)

Without Lu et al. 2016, the Part B verdict falls to 'measured without controlling group number and size'.

- conf: not stated
- class: not stated
- holds: the review's sensitivity analysis
- src: luEvaluatingCommunityenvironmentRelationships2016
- trail: H1-06 §Verdict as delivered, §6. Verdicts

From the note:

> H1-06:A-022 [quote: Verdict as delivered] Without Lu et al. 2016 the verdict falls to 'measured without controlling group number and size'.
>
> H1-06:A-030 [6. Verdicts] Removing Lu et al. 2016 drops the verdict to "measured without controlling group number and size".
>

Not found in the cited text (where to look, not what is wrong): Part; holds: review

## rankwise-structuring.7 (claim)

Across 160 natural sites, habitat category explained little composition variance at any level and peaked at class (PERMANOVA R2: phylum 3.7%, class 6.3%, ASV 2.7%).

- conf: not stated
- class: not stated
- holds: soils at 160 natural sites in southwest France; gyrB taxonomy; a preprint; group numbers ranged from 18 phyla to 769 ASVs and were not controlled
- src: mayjonadeRelativeEffectsAbiotic2024
- trail: H1-06 §4. Part B, §Verdict as delivered, §References

From the note:

> H1-06:B-0132 [4. Part B: environmental structuring of composition from fine to coarse ranks] **Uncontrolled studies across ranks.** At 160 natural sites in southwest France (gyrB taxonomy, preprint) [24], habitat category explained little composition variance at any level.
>
> H1-06:B-0133 [4. Part B: environmental structuring of composition from fine to coarse ranks] It peaked at class (PERMANOVA R2: phylum 3.7%, class 6.3%, ASV 2.7%).
>
> H1-06:B-0135 [4. Part B: environmental structuring of composition from fine to coarse ranks] Group numbers ranged from 18 phyla to 769 ASVs and were not controlled.
>
> H1-06:A-021 [quote: Verdict as delivered] Uncontrolled studies agree in part and conflict in part: habitat R2 peaked at class and physicochemical associations were most frequent at phylum (Mayjonade 2024 preprint, gyrB taxonomy); 97% OTUs explained more composition variance than ASVs (Bay 2020); a pH-aligned composition axis stayed stable across ranks (Chakraverti-Wuerthwein 2026 preprint); seasonal niches were absent at class level (Auladell 2022, time series, not a spatial environment gradient).
>
> H1-06:R-0149 [References] The relative effects of abiotic and biotic factors in explaining the structure of soil bacterial communities at diverse taxonomic levels. bioRxiv 2024.10.29.620845 (preprint, version posted 3 November 2024; read as preprint, not peer reviewed). doi:10.1101/2024.10.29.620845
>

## rankwise-structuring.8 (claim)

The share of individual groups significantly associated with soil physicochemistry fell from 59% at phylum to 30.2% at ASV, while plant-community associations rose from 19.7% to 48.7%.

- conf: not stated
- class: not stated
- holds: 160 natural sites in southwest France; gyrB taxonomy; a preprint; group numbers not controlled
- src: mayjonadeRelativeEffectsAbiotic2024
- trail: H1-06 §4. Part B

From the note:

> H1-06:B-0132 [4. Part B: environmental structuring of composition from fine to coarse ranks] **Uncontrolled studies across ranks.** At 160 natural sites in southwest France (gyrB taxonomy, preprint) [24], habitat category explained little composition variance at any level.
>
> H1-06:B-0134 [4. Part B: environmental structuring of composition from fine to coarse ranks] The share of individual groups significantly associated with soil physicochemistry fell from 59% at phylum to 30.2% at ASV, while plant-community associations rose from 19.7% to 48.7%.
>
> H1-06:B-0135 [4. Part B: environmental structuring of composition from fine to coarse ranks] Group numbers ranged from 18 phyla to 769 ASVs and were not controlled.
>

## rankwise-structuring.9 (claim)

Community turnover was stronger at ASV resolution (an 82% drop in similarity over 160 km, against 50 to 60% for clustered or filtered data), but "less variation in community composition could be explained and partitioned for the high-resolution data set", and the rank order of predictors changed. The comparison is of the high-resolution set against clustered and/or rare-taxon-filtered data, by incidence-based variation partitioning.

- conf: not stated
- class: not stated
- holds: soils in the Negev; ASVs against 97% OTUs only, no ranks; group numbers not controlled
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

## rankwise-structuring.10 (claim)

The pH-aligned first canonical axis stayed stable when OTUs were summed to genus, family and higher, while secondary axes were incoherent across resolutions.

- conf: not stated
- class: not stated
- holds: a global preprint on topsoil (N = 217) and ocean (N = 125) 16S surveys; the null there does not preserve group structure; tau_D values appear only in figures
- src: chakravertiwuerthweinPhylogeneticCoherenceMicrobiome2026
- trail: H1-06 §4. Part B, §2. Part A1, §Adversarial

From the note:

> H1-06:B-0139 [4. Part B: environmental structuring of composition from fine to coarse ranks] In a global preprint [29], the pH-aligned first canonical axis stayed stable when OTUs were summed to genus, family and higher, while secondary axes were incoherent across resolutions.
>
> H1-06:B-0140 [4. Part B: environmental structuring of composition from fine to coarse ranks] The null there does not preserve group structure.
>
> H1-06:B-0040 [2. Part A1: depth of conservation of environmental preferences] Chakraverti-Wuerthwein et al. 2026 [29] (measured, natural, preprint, SINGLE SOURCE) ran CCA on global topsoil (N = 217) and ocean (N = 125) 16S surveys.
>
> H1-06:C-030 [warning: Adversarial critique, full findings] - Chakraverti-Wuerthwein 2026 [29]: tau_D values 'appear only in figures', so the 'strong phylogenetic signal' claim is qualitative, with no number quoted. It is used in both the A1 and B verdicts.
>

## rankwise-structuring.11 (claim)

In an 11-year coastal time series, seasonal niches were coherent for some genera and families, but classes (Alphaproteobacteria, Gammaproteobacteria, Bacteroidia) were non-seasonal when aggregated; within at least three genera, niche similarity fell with 16S divergence.

- conf: not stated
- class: not stated
- holds: marine bacteria in an 11-year coastal time series, not a spatial environment gradient; aggregation used random 80% ASV subsets, but group number was not equalised
- src: auladellSeasonalNicheDifferentiation2021
- trail: H1-06 §4. Part B, §Verdict as delivered, §References

From the note:

> H1-06:B-0141 [4. Part B: environmental structuring of composition from fine to coarse ranks] In an 11-year coastal time series [28], seasonal niches were coherent for some genera and families, but classes (Alphaproteobacteria, Gammaproteobacteria, Bacteroidia) were non-seasonal when aggregated; within at least three genera, niche similarity fell with 16S divergence.
>
> H1-06:B-0142 [4. Part B: environmental structuring of composition from fine to coarse ranks] Aggregation used random 80% ASV subsets, but group number was not equalised.
>
> H1-06:A-021 [quote: Verdict as delivered] Uncontrolled studies agree in part and conflict in part: habitat R2 peaked at class and physicochemical associations were most frequent at phylum (Mayjonade 2024 preprint, gyrB taxonomy); 97% OTUs explained more composition variance than ASVs (Bay 2020); a pH-aligned composition axis stayed stable across ranks (Chakraverti-Wuerthwein 2026 preprint); seasonal niches were absent at class level (Auladell 2022, time series, not a spatial environment gradient).
>
> H1-06:R-0159 [References] Seasonal niche differentiation among closely related marine bacteria.
>

## rankwise-structuring.12 (claim)

The rank-wise studies other than Lu et al. 2016 are uncontrolled for group number and size, and two are preprints; they agree in part and conflict in part with it.

- conf: not stated
- class: not stated
- holds: Mayjonade 2024, Bay 2020, Chakraverti-Wuerthwein 2026 and Auladell 2022
- src: mayjonadeRelativeEffectsAbiotic2024, baySoilBacterialCommunities2020, chakravertiwuerthweinPhylogeneticCoherenceMicrobiome2026, auladellSeasonalNicheDifferentiation2021
- trail: H1-06 §5. Bounds, §Verdict as delivered

From the note:

> H1-06:B-0161 [5. Bounds and failure modes] - Part B rests on a single controlled reanalysis [23].
>
> H1-06:B-0162 [5. Bounds and failure modes] The other rank-wise studies are uncontrolled, and two are preprints [24, 29].
>
> H1-06:A-021 [quote: Verdict as delivered] Uncontrolled studies agree in part and conflict in part: habitat R2 peaked at class and physicochemical associations were most frequent at phylum (Mayjonade 2024 preprint, gyrB taxonomy); 97% OTUs explained more composition variance than ASVs (Bay 2020); a pH-aligned composition axis stayed stable across ranks (Chakraverti-Wuerthwein 2026 preprint); seasonal niches were absent at class level (Auladell 2022, time series, not a spatial environment gradient).
>

Not found in the cited text (where to look, not what is wrong): 2016; Lu

## rankwise-structuring.13 (claim)

The rise in explained variance from otu97 to otu94 rests on Lu et al. 2016 alone: Bay et al. compare ASVs against clustered and/or filtered data, a different step, although its direction matches.

- conf: single (critic: C-032)
- class: not stated
- holds: the otu97-to-otu94 and genus rise in soils
- src: luEvaluatingCommunityenvironmentRelationships2016, baySoilBacterialCommunities2020
- trail: H1-06 §4. Part B, §Adversarial

From the note:

> H1-06:B-0138 [4. Part B: environmental structuring of composition from fine to coarse ranks] The direction matches Lu's otu97-to-otu94 rise.
>
> H1-06:C-032 [warning: Adversarial critique, full findings] - 'Relation to Part A' treats the otu97-to-otu94/genus rise as a replicated pattern across [23, 25], but [25] compares ASVs against clustered and/or filtered data, a different step. The rise itself rests on Lu 2016 alone.
>

Not found in the cited text (where to look, not what is wrong): holds: in; holds: soils

## adjacent-metrics.1 (claim)

pH explained more of betaNTI (phylogenetic turnover, not composition) at ASV level (R2 0.20) than at OTU97 (0.08).

- conf: not stated
- class: not stated
- holds: Antarctic wetlands; unit counts uncontrolled
- src: quirogaEcologicalAssemblyBacterial2022
- trail: H1-06 §4. Part B

From the note:

> H1-06:B-0143 [4. Part B: environmental structuring of composition from fine to coarse ranks] **Adjacent metrics (not composition-environment R2).** Two metrics give a different picture because they measure something else.
>
> H1-06:B-0144 [4. Part B: environmental structuring of composition from fine to coarse ranks] In Antarctic wetlands, pH explained more of betaNTI (phylogenetic turnover, not composition) at ASV level (R2 0.20) than at OTU97 (0.08), with unit counts uncontrolled [26].
>

## adjacent-metrics.2 (claim)

Abundance-occupancy relationships were weakest at species and roughly constant from genus to phylum.

- conf: not stated
- class: not stated
- holds: marine bacterioplankton in an estuary
- src: izabelshenAbundanceOccupancyRelationshipsAlong2021
- trail: H1-06 §4. Part B, §References

From the note:

> H1-06:B-0143 [4. Part B: environmental structuring of composition from fine to coarse ranks] **Adjacent metrics (not composition-environment R2).** Two metrics give a different picture because they measure something else.
>
> H1-06:B-0145 [4. Part B: environmental structuring of composition from fine to coarse ranks] Abundance-occupancy relationships in an estuary were weakest at species and roughly constant from genus to phylum [30].
>
> H1-06:R-0164 [References] Abundance-occupancy relationships along taxonomic ranks reveal a consistency of niche differentiation in marine bacterioplankton with distinct lifestyles.
>

## adjacent-metrics.3 (claim)

Across about one million full-length 16S sequences, the ecological consistency of habitat annotations, scored against random partitions with the same cluster count and size distribution, generally fell as OTU thresholds became stricter (finer) for complete and average linkage; single linkage behaved differently.

- conf: not stated
- class: deriv (note: "inferred, identity thresholds only, not ranks")
- holds: identity thresholds only, not ranks; the design controls group number and size, but the response is annotation consistency, not environment-explained composition
- src: schmidtEcologicalConsistencySSU2014
- trail: H1-06 §4. Part B

From the note:

> H1-06:B-0146 [4. Part B: environmental structuring of composition from fine to coarse ranks] Across about one million full-length 16S sequences, the ecological consistency of habitat annotations was scored against random partitions with the same cluster count and size distribution.
>
> H1-06:B-0147 [4. Part B: environmental structuring of composition from fine to coarse ranks] It generally fell as OTU thresholds became stricter, i.e. finer, for complete and average linkage; single linkage behaved differently [27] (inferred, identity thresholds only, not ranks).
>
> H1-06:B-0148 [4. Part B: environmental structuring of composition from fine to coarse ranks] That design controls group number and size, but the response is annotation consistency, not environment-explained composition.
>

## rank-depth-relation.1 (claim)

The rise in explained variance from otu97 to about otu94 and genus matches where perturbation responses cluster (tau_D about 0.017 to 0.02), and the fall at phylum in soils and the class-level incoherence in a time series match the weak within-phylum pH signal and the opposing responses inside coarse groups.

- conf: not stated
- class: reading (note: "reviewer's reading")
- holds: the critic: it links a natural-system composition result to engineered perturbation-response depths, breaking the natural/engineered separation, and presents a correspondence the sources do not test
- src: luEvaluatingCommunityenvironmentRelationships2016, isobePhylogeneticConservationBacterial2019, isobePhylogeneticConservationSoil2020, auladellSeasonalNicheDifferentiation2021, ramonedaBuildingGenomebasedUnderstanding2023
- trail: H1-06 §4. Part B, §Adversarial

From the note:

> H1-06:B-0149 [4. Part B: environmental structuring of composition from fine to coarse ranks] **Relation to Part A (reviewer's reading).** The rise in explained variance from otu97 to about otu94 and genus [23, 25] matches where perturbation responses cluster (tau_D about 0.017 to 0.02, about genus) [19, 20].
>
> H1-06:B-0150 [4. Part B: environmental structuring of composition from fine to coarse ranks] The fall at phylum in soils [23] and the class-level incoherence in a time series [28] match the weak within-phylum pH signal [13] and the opposing responses inside coarse groups [19].
>
> H1-06:C-053 [warning: Adversarial critique, full findings] - 'Relation to Part A (reviewer's reading)' links a natural-system composition result (Lu 2016, otu97-to-genus rise) to engineered perturbation-response depths (Isobe 2019, 2020, tau_D ~0.017, 'about genus'), which breaks Common rule 10's natural/engineered separation. It is labelled reviewer's reading, but it presents a correspondence the sources do not test.
>

## rank-depth-relation.2 (claim)

None of the studies links composition structure to genome content, and an association between environment and composition at a rank is not evidence about the genomes of that rank.

- conf: not stated
- class: not stated
- holds: the rank-wise composition studies the review read
- src: none (the reviewer's synthesis)
- trail: H1-06 §4. Part B

From the note:

> H1-06:B-0151 [4. Part B: environmental structuring of composition from fine to coarse ranks] None of the studies links composition structure to genome content, and an association between environment and composition at a rank is not evidence about the genomes of that rank.
>

Not found in the cited text (where to look, not what is wrong): holds: rank-wise; holds: review

## dns.1 (do not say)

"Environmental preferences are measured and inconsistent between methods, taxonomies or datasets in natural systems."

- why: The A1 verdict over-reaches: the inconsistency only emerges when the one natural study is set beside engineered results or a preprint that measures a different quantity, so it should not stand as the natural-system verdict, and engineered evidence may not carry a natural-system verdict.
- instead: env-preference-depth.1, env-preference-depth.2
- trail: H1-06 §critic, §Adversarial

From the note:

> H1-06:A-001 [quote: Verdict as delivered] Phylogenetic depth of conservation: environmental preferences (pH, moisture, salinity, temperature optima)**: Measured and inconsistent between methods, taxonomies or datasets.
>
> H1-06:A-023 [6. Verdicts] - **A1, environmental preferences:** measured and inconsistent between methods, taxonomies or datasets.
>
> H1-06:C-005 [danger: Critic: verdict partly supported] The 'inconsistent' label only emerges when natural evidence is set beside engineered results or a preprint that measures a different quantity (CCA loadings), so it should not stand as the natural-system verdict.
>
> H1-06:C-012 [danger: Critic: verdict partly supported] A1 over-reaches.
>
> H1-06:C-014 [danger: Critic: verdict partly supported] The inconsistency behind the verdict comes from comparing that natural study with engineered isolate and transplant work (Lennon, Morrissey and Franklin), and Common rule 10 forbids letting engineered evidence carry a natural-system verdict.
>
> H1-06:C-033 [warning: Adversarial critique, full findings] - Part A1 synthesis: 'The only large natural-system test of pH preference finds weak signal and poor prediction by rank' is correctly a single study [13], but the A1 verdict then generalises it into a field-level 'inconsistent' label.
>

Not found in the cited text (where to look, not what is wrong): "Environmental preferences are measured and inconsistent between methods, taxonomies or datasets in natural systems."

## dns.2 (do not say)

"ASVs within single families spanned four or more pH units, in Xanthobacteraceae in soil and Chitinophagaceae in freshwater."

- why: The family claim is partly wrong: Chitinophagaceae spans 4.63 to 8.35, 3.72 units, so it does not span four units.
- instead: ph-preference.2
- trail: H1-06 §critic, §Adversarial

From the note:

> H1-06:B-0035 [2. Part A1: depth of conservation of environmental preferences] ASVs within single families spanned four or more pH units (Xanthobacteraceae in soil, Chitinophagaceae in freshwater).
>
> H1-06:C-022 [danger: Critic: verdict partly supported] The family claim is partly wrong: Chitinophagaceae spans 4.63 to 8.35 (3.72 units), not 'four or more pH units'.
>
> H1-06:C-036 [warning: Adversarial critique, full findings] - [13] Ramoneda 2023 body claim: 'ASVs within single families spanned four or more pH units (Xanthobacteraceae in soil, Chitinophagaceae in freshwater)'. The source gives 4.01 to 8.20 (4.19 units) and 4.63 to 8.35 (3.72 units), so Chitinophagaceae does not span four units.
>

Not found in the cited text (where to look, not what is wrong): "ASVs within single families spanned four or more pH units, in Xanthobacteraceae in soil and Chitinophagaceae in freshwater."

## dns.3 (do not say)

"pH optimum, soil moisture optimum and habitat association are conserved in deep clades."

- why: The statement appears in Martiny et al. 2013 as a discussion claim resting on other studies, and that paper does not measure any of these.
- instead: env-preference-depth.4, env-preference-depth.5
- trail: H1-06 §2. Part A1

From the note:

> H1-06:B-0028 [2. Part A1: depth of conservation of environmental preferences] **No consenTRAIT depth for any environmental optimum was found.** The frequently repeated statement that pH optimum, soil moisture optimum and habitat association sit in deep clades appears in Martiny et al. 2013 as a discussion claim resting on other studies.
>
> H1-06:B-0029 [2. Part A1: depth of conservation of environmental preferences] That paper does not measure any of these (asserted, SECONDARY) [1].
>

Not found in the cited text (where to look, not what is wrong): "pH optimum, soil moisture optimum and habitat association are conserved in deep clades."

## dns.4 (do not say)

"Perturbation responses are conserved at about genus level."

- why: The equation of tau_D 0.016 to 0.020 with roughly genus is attributed to the authors, but the review's own Section 1 says a 16S depth cannot be converted into a rank.
- instead: perturbation-response-depth.1, perturbation-response-depth.9
- trail: H1-06 §Adversarial

From the note:

> H1-06:B-0080 [2. Part A1: depth of conservation of environmental preferences] Perturbation responses, a different quantity, cluster at roughly genus depth in 16S terms [19, 20, 21].
>
> H1-06:C-054 [warning: Adversarial critique, full findings] - The equation of tau_D 0.016 to 0.020 with 'roughly genus' is attributed to the authors, but the review's own Section 1 says a 16S depth 'cannot be converted into a rank'. This is inconsistent use.
>

Not found in the cited text (where to look, not what is wrong): "Perturbation responses are conserved at about genus level."

## dns.5 (do not say)

"Coarse taxonomic groups contain opposing finer responses."

- why: It is phrased as a general bound but rests on one N-addition study plus a time series, and that N-addition study also reports consistent coarse-rank responses (phylum Actinobacteria positive; classes Betaproteobacteria and Deltaproteobacteria negative).
- instead: perturbation-response-depth.5, perturbation-response-depth.6
- trail: H1-06 §Adversarial, §critic

From the note:

> H1-06:B-0159 [5. Bounds and failure modes] - Coarse groups can contain opposing finer responses [19, 28].
>
> H1-06:C-024 [danger: Critic: verdict partly supported] But Isobe also reports consistent phylum- and class-level responses (Actinobacteria positive; Betaproteobacteria and Deltaproteobacteria negative), which the review leaves out while citing only the 'coarse hides fine' example.
>
> H1-06:C-031 [warning: Adversarial critique, full findings] - Section 5 bullet 'Coarse groups can contain opposing finer responses' is phrased as a general bound, but it rests on one N-addition study [19] plus a time series [28]. [19] also reports consistent coarse-rank responses (phylum Actinobacteria positive; classes Betaproteobacteria and Deltaproteobacteria negative), and the review omits these.
>

Not found in the cited text (where to look, not what is wrong): "Coarse taxonomic groups contain opposing finer responses."

## dns.6 (do not say)

"Genome incompleteness pushes detected function down."

- why: It is phrased generally, but each quantitative element is single source (modules, core genes, reference bias), and none measures the effect on conservation depth.
- instead: genome-incompleteness.6
- trail: H1-06 §Adversarial

From the note:

> H1-06:B-0157 [5. Bounds and failure modes] - Incompleteness pushes detected function down, and the size of the effect depends on module and phylum [9, 10, 11].
>
> H1-06:C-034 [warning: Adversarial critique, full findings] - 'Incompleteness pushes detected function down' (Section 5) is phrased generally. Each quantitative element is SINGLE SOURCE ([9] modules, [10] core genes, [11] reference bias), and none measures the effect on conservation depth, which the review does concede.
>

Not found in the cited text (where to look, not what is wrong): "Genome incompleteness pushes detected function down."

## dns.7 (do not say)

"Genome incompleteness makes consenTRAIT depth estimates shallower."

- why: That consensus-threshold methods would push depth estimates shallower under incompleteness is the reviewer's untested reading, echoed in Section 5 as a bound.
- instead: genome-incompleteness.7, genome-incompleteness.1
- trail: H1-06 §Adversarial

From the note:

> H1-06:B-0112 [3. Part A2: depth of conservation of genome-encoded metabolic traits] Reviewer's reading, not tested by any source: consensus-threshold methods such as consenTRAIT (90% sharing) are exposed to false absences, which would fragment clades and push depth estimates shallower.
>
> H1-06:C-055 [warning: Adversarial critique, full findings] - The reviewer's reading that consensus-threshold methods would push depth estimates shallower under incompleteness is labelled as untested, which is appropriate, but it is then echoed in Section 5 as a bound.
>

Not found in the cited text (where to look, not what is wrong): "Genome incompleteness makes consenTRAIT depth estimates shallower."

## dns.8 (do not say)

"Rank-wise partitioning of genomic traits is non-monotonic."

- why: The Royalty and Steen rank partition is a single source, correctly flagged in the body, but it carries weight in the A2 verdict without that flag.
- instead: rank-partitioning.1
- trail: H1-06 §Adversarial

From the note:

> H1-06:A-012 [quote: Verdict as delivered] Functional coherence nodes also differ between 16S and GTDB 120-protein trees (Parras-Molto 2021), and rank-wise partitioning is non-monotonic (GTDB: phylum 14.6%, order 9.2%, genus 5.5%; Royalty and Steen 2019).
>
> H1-06:C-035 [warning: Adversarial critique, full findings] - The Royalty and Steen rank partition (phylum 14.6%, order 9.2%, genus 5.5%) is cited in the A2 verdict as showing that 'rank-wise partitioning is non-monotonic'. It is correctly flagged SINGLE SOURCE in the body but carries weight in the verdict without that flag.
>

Not found in the cited text (where to look, not what is wrong): "Rank-wise partitioning of genomic traits is non-monotonic."

## dns.9 (do not say)

"97% OTUs explained more composition variance than ASVs."

- why: Bay et al. compare the high-resolution set against filtered ones (clustered and/or rare-taxon-filtered data) using incidence-based variation partitioning, so the paraphrase reduces a clustering-plus-filtering contrast to clustering alone.
- instead: rankwise-structuring.9
- trail: H1-06 §critic

From the note:

> H1-06:A-021 [quote: Verdict as delivered] Uncontrolled studies agree in part and conflict in part: habitat R2 peaked at class and physicochemical associations were most frequent at phylum (Mayjonade 2024 preprint, gyrB taxonomy); 97% OTUs explained more composition variance than ASVs (Bay 2020); a pH-aligned composition axis stayed stable across ranks (Chakraverti-Wuerthwein 2026 preprint); seasonal niches were absent at class level (Auladell 2022, time series, not a spatial environment gradient).
>
> H1-06:C-019 [danger: Critic: verdict partly supported] The B verdict text also paraphrases Bay 2020 as '97% OTUs explained more composition variance than ASVs'.
>
> H1-06:C-020 [danger: Critic: verdict partly supported] In full text, Bay compares the high-resolution set against 'filtered ones' (clustered and/or rare-taxon-filtered data) using incidence-based variation partitioning, so the paraphrase reduces a clustering-plus-filtering contrast to clustering alone.
>

## dns.10 (do not say)

"The rise in explained variance from otu97 to otu94 is replicated across studies."

- why: The rise rests on Lu 2016 alone; the other study cited for it compares ASVs against clustered and/or filtered data, a different step.
- instead: rankwise-structuring.13
- trail: H1-06 §Adversarial

From the note:

> H1-06:B-0149 [4. Part B: environmental structuring of composition from fine to coarse ranks] **Relation to Part A (reviewer's reading).** The rise in explained variance from otu97 to about otu94 and genus [23, 25] matches where perturbation responses cluster (tau_D about 0.017 to 0.02, about genus) [19, 20].
>
> H1-06:C-032 [warning: Adversarial critique, full findings] - 'Relation to Part A' treats the otu97-to-otu94/genus rise as a replicated pattern across [23, 25], but [25] compares ASVs against clustered and/or filtered data, a different step. The rise itself rests on Lu 2016 alone.
>

Not found in the cited text (where to look, not what is wrong): "The rise in explained variance from otu97 to otu94 is replicated across studies."

## dns.11 (do not say)

"Rank-wise structuring of composition corresponds to the depth at which perturbation responses are conserved, at about genus."

- why: It links a natural-system composition result to engineered perturbation-response depths, which breaks the natural/engineered separation, and presents a correspondence the sources do not test.
- instead: rank-depth-relation.1
- trail: H1-06 §Adversarial

From the note:

> H1-06:B-0149 [4. Part B: environmental structuring of composition from fine to coarse ranks] **Relation to Part A (reviewer's reading).** The rise in explained variance from otu97 to about otu94 and genus [23, 25] matches where perturbation responses cluster (tau_D about 0.017 to 0.02, about genus) [19, 20].
>
> H1-06:C-053 [warning: Adversarial critique, full findings] - 'Relation to Part A (reviewer's reading)' links a natural-system composition result (Lu 2016, otu97-to-genus rise) to engineered perturbation-response depths (Isobe 2019, 2020, tau_D ~0.017, 'about genus'), which breaks Common rule 10's natural/engineered separation. It is labelled reviewer's reading, but it presents a correspondence the sources do not test.
>

Not found in the cited text (where to look, not what is wrong): "Rank-wise structuring of composition corresponds to the depth at which perturbation responses are conserved, at about genus."

