## processing-effects.4 (claim)

In soils, genome size tracked the ratio of polysaccharide-decomposition to biomass-synthesis genes across 2,650 genomes and a continental survey.

- conf: not stated
- class: not stated
- holds: soil bacteria; 2,650 genomes and a continental survey
- src: wuGlobalRelationshipGenome2025 (AB)
- trail: H2-01 §2.3

From the note:

> H2-01:R-0258 [Reference list] A global relationship between genome size and encoded carbon metabolic strategies of soil bacteria.
>
> H2-01:B-0068 [2.3 How processing choices move the estimate] In soils, genome size tracked the ratio of polysaccharide-decomposition to biomass-synthesis genes across 2,650 genomes and a continental survey [Wu2025; AB].
>

## dimension-elsewhere.10 (claim)

The trait gap-filling method BHPMF imputes from trait-trait correlations.

- conf: not stated
- class: not stated
- holds: plant trait gap-filling
- src: schrodtScpBHPMFScp2015 (AB)
- trail: H2-01 §2.4

From the note:

> H2-01:B-0093 [2.4 Dimensionality elsewhere: genomes, trait databases, transcriptomes] Two components explain 74% of six key plant traits across 2,214 species [SEC, via Bruelheide2018]; with 17 gap-filled traits across more than 20,000 species, PC1 33%, PC2 15%, PC3 9.4% [Joswig2022; FT].
>
> H2-01:B-0094 [2.4 Dimensionality elsewhere: genomes, trait databases, transcriptomes] The gap-filling (BHPMF) imputes from trait-trait correlations [Schrodt2015; AB], so covariation in imputed matrices is partly built in (reviewer's reading).
>

## dimension-elsewhere.11 (claim)

Because BHPMF imputes from trait-trait correlations, covariation in imputed trait matrices is partly built in.

- conf: not stated
- class: reading (note: "reviewer's reading")
- holds: gap-filled plant trait matrices
- src: schrodtScpBHPMFScp2015
- trail: H2-01 §2.4

From the note:

> H2-01:B-0093 [2.4 Dimensionality elsewhere: genomes, trait databases, transcriptomes] Two components explain 74% of six key plant traits across 2,214 species [SEC, via Bruelheide2018]; with 17 gap-filled traits across more than 20,000 species, PC1 33%, PC2 15%, PC3 9.4% [Joswig2022; FT].
>
> H2-01:B-0094 [2.4 Dimensionality elsewhere: genomes, trait databases, transcriptomes] The gap-filling (BHPMF) imputes from trait-trait correlations [Schrodt2015; AB], so covariation in imputed matrices is partly built in (reviewer's reading).
>

## covariation-transfer.5 (claim)

MetaCyc pathways share reactions and contributing species, so pathway-pathway co-abundance partly reflects shared members; 43,355 of about 58,653 possible pathway pairs were significant in at least one cohort, which points to strong common factors that would make replication easy; and "replicated at P < 0.05" with n = 77 is a lenient bar, so the 59% is an optimistic reading of transfer.

- conf: not stated
- class: reading (note: "Cautions (reviewer's reading)")
- holds: the IBD replication test
- src: chenGutMicrobialCoabundance2020
- trail: H2-01 §3.2, §answers

From the note:

> H2-01:A-033 [quote: Answers as delivered] Pathway co-abundances from an IBD gut cohort partly reproduced in an independent IBD cohort (59.0% of 37,106 at P < 0.05; species 25.4%), with the low species rate attributed to power [Chen2020].
>
> H2-01:B-0108 [3.2 Held-out study, same habitat (microbial, direct)] Cautions (reviewer's reading): MetaCyc pathways share reactions and contributing species, so pathway-pathway co-abundance partly reflects shared members. 43,355 of about 58,653 possible pathway pairs were significant in at least one cohort, which points to strong common factors that would make replication easy.
>
> H2-01:B-0109 [3.2 Held-out study, same habitat (microbial, direct)] "Replicated at P < 0.05" with n = 77 is a lenient bar.
>
> H2-01:A-034 [quote: Answers as delivered] Shared pathway members, strong common factors and a lenient threshold make this an optimistic reading of transfer.
>

## transfer-dependence.1 (claim)

The review's synthesis is that, across the other-field and neighbouring evidence, transfer appears to depend on the similarity of the training set to the target (related tumour types; related tissues; NSTI; phylum differences), the breadth of the training set, and the fraction of the target that is shared mean structure against target-specific signal; the critic holds that this pools incommensurable tests of different quantities (covariance or dictionary transfer, taxon-to-gene mapping accuracy, per-sample accuracy metrics, phylogenetic gene gain/loss prediction) and is the reviewer's synthesis, not a finding.

- conf: not stated
- class: reading (critic: C-018)
- holds: each dependency rests on one to three sources measuring different quantities, breadth on one qualitative study alone; none of these dependencies has been measured for microbial function-function covariation across habitats
- src: none (the reviewer's synthesis)
- trail: H2-01 §3.5, §answers, §critic, §Adversarial

From the note:

> H2-01:B-0127 [3.5 What transfer appears to depend on] Across the other-field and neighbouring evidence, three dependencies recur, each from few sources: similarity of the training set to the target (Cleary2017 related tumour types; Pierson2015 related tissues; Langille2013 NSTI; KonnoIwasaki2023 phylum differences); breadth of the training set (Taroni2019); and the fraction of the target that is shared mean structure versus target-specific signal (Lenz2016; Sun2020).
>
> H2-01:B-0128 [3.5 What transfer appears to depend on] None of these has been measured for microbial function-function covariation across habitats.
>
> H2-01:A-041 [quote: Answers as delivered] Across fields, transfer appears to depend on similarity between training and target, breadth of training, and how much of the target is shared mean structure; each dependency rests on one to three sources.
>
> H2-01:A-046 [quote: Answers as delivered] Reproduction is high in some tests (Subramanian 81%; Chen reductive TCA 94.7%) and low in others (Cleary cross-type drop; pooled networks in Pierson; sign reversals across scales in plant traits [Anderegg2018]); the differences track how different the target is from the training data..
>
> H2-01:C-016 [danger: Critic: answers partly supported] The body does not support the cross-field sentence 'transfer appears to depend on similarity between training and target, breadth of training, and shared mean structure' as a finding.
>
> H2-01:C-017 [danger: Critic: answers partly supported] It pools different quantities: covariance or dictionary transfer (Cleary2017, Pierson2015), taxon-to-gene mapping accuracy (Langille2013 NSTI), and phylogenetic gene gain/loss prediction (KonnoIwasaki2023).
>
> H2-01:C-018 [danger: Critic: answers partly supported] It should be labelled the reviewer's synthesis across incommensurable tests.
>
> H2-01:C-054 [danger: Critic: answers partly supported] (3) D2's cross-field dependency statement pools incommensurable transfer tests.
>
> H2-01:C-075 [warning: Adversarial critique, full findings] - D2 answer: 'Across fields, transfer appears to depend on similarity between training and target, breadth of training, and how much of the target is shared mean structure'. Breadth rests on Taroni2019 alone (qualitative), and each dependency rests on one to three sources measuring different quantities.
>
> H2-01:C-126 [warning: Adversarial critique, full findings] - D2 answer and Section 3.5 fold four different quantities into one set of transfer dependencies: covariance and dictionary transfer across tumour types or tissues (Cleary2017, Pierson2015), taxon-to-gene mapping accuracy against reference distance (Langille2013), per-sample accuracy metrics (Sun2020), and phylogenetic gene gain/loss prediction (KonnoIwasaki2023).
>
> H2-01:C-018 [danger: Critic: answers partly supported] It should be labelled the reviewer's synthesis across incommensurable tests.
>

## covariation-stability.13 (claim)

A review reports plant trait-network topology shifting along resource gradients.

- conf: not stated
- class: assert (marker)
- holds: plant trait networks (other field)
- src: hePlantTraitNetworks2020 (AB; asserted)
- trail: H2-01 §4.4

From the note:

> H2-01:B-0162 [4.4 Covariation among functions against levels and composition] **Plant traits (other field, both directions).**
>
> H2-01:I-0037 [4.4 Covariation among functions against levels and composition] A review reports trait-network topology shifting along resource gradients [He2020; AB; asserted].
>

## dns.1 (do not say)

"Microbial functional profiles are dominated by a shared mean, while across genomes metabolic content is high-dimensional."

- why: The evidence is a per-sample accuracy metric under permutation and descriptive HMP statements from human-associated and a few soil datasets, not a decomposition of a sample-by-function matrix, and the sentence merges sample-level functional profiles, genome-level presence/absence and a per-sample accuracy metric into one characterisation of "functional profiles".
- instead: shared-mean-profile.4, dimension-elsewhere.1
- trail: H2-01 §critic, §Adversarial

From the note:

> H2-01:C-005 [danger: Critic: answers partly supported] Neither is a decomposition that measures how much of a sample-by-function matrix is a mean profile, and both come from human-associated and a few soil datasets.
>
> H2-01:A-108 [6. Answers by direction] Profiles appear dominated by a shared mean, and across genomes metabolic content is high-dimensional.
>
> H2-01:C-002 [danger: Critic: answers partly supported] First, the closing summary line 'Profiles appear dominated by a shared mean' goes further than the evidence.
>
> H2-01:C-052 [danger: Critic: answers partly supported] (2) The D1 and Section 5 summaries turn a per-sample accuracy metric and HMP descriptive statements into 'profiles dominated by a shared mean'.
>
> H2-01:C-074 [warning: Adversarial critique, full findings] - D1 final summary (Section 6): 'Profiles appear dominated by a shared mean'. This generalises Sun2020 (a per-sample Spearman accuracy metric under permutation) and HMP2012 (human body sites) to functional profiles in general.
>
> H2-01:C-128 [warning: Adversarial critique, full findings] - D1 Section 6 merges sample-level functional profiles (Jiang, Piton, Flinkstrom), genome-level presence/absence (Fahimipour) and a per-sample accuracy metric (Sun2020) into a single characterisation of 'functional profiles'.
>

Not found in the cited text (where to look, not what is wrong): "Microbial functional profiles are dominated by a shared mean, while across genomes metabolic content is high-dimensional."

## dns.2 (do not say)

"Across genomes, metabolic presence/absence is high-dimensional, with dozens to hundreds of coordinates."

- why: This rests on one modelled study (diffusion maps across genera) and is phrased as a property of genomes in general.
- instead: dimension-elsewhere.1
- trail: H2-01 §critic, §Adversarial

From the note:

> H2-01:I-0013 [2.4 Dimensionality elsewhere: genomes, trait databases, transcriptomes] - **Across bacterial genomes.** Diffusion maps on presence/absence of 7,769 substrate-product traits across 2,621 genera found no single low-dimensional space but crossing low-dimensional manifolds with "dozens or possibly hundreds of meaningful coordinates" [Fahimipour2020; FT; modelled; SINGLE SOURCE].
>
> H2-01:A-011 [quote: Answers as delivered] Across genomes, metabolic presence/absence is high-dimensional (dozens to hundreds of coordinates [Fahimipour2020]).
>
> H2-01:C-007 [danger: Critic: answers partly supported] Second, 'across genomes, metabolic presence/absence is high-dimensional' rests on one modelled study (Fahimipour2020), and 'low dimensionality holds for leading components within datasets' rests on one study (Heimberg2016).
>
> H2-01:C-070 [warning: Adversarial critique, full findings] - D1 answer: 'Across genomes, metabolic presence/absence is high-dimensional (dozens to hundreds of coordinates)'. This rests on Fahimipour2020 alone (modelled, diffusion maps) and is phrased as a property of genomes in general.
>

Not found in the cited text (where to look, not what is wrong): "Across genomes, metabolic presence/absence is high-dimensional, with dozens to hundreds of coordinates."

## dns.7 (do not say)

"Galand et al. (2018) is the only direct same-habitat result contrary to function levels being more stable than taxonomic composition."

- why: Manor and Borenstein's full text (2017) directly measures that revised functional profiles identify hosts as well as strain-level taxonomy does, so contrary same-habitat evidence also exists in full text, and Galand et al. (2018) is abstract only.
- instead: levels-within-habitat.1, levels-within-habitat.9
- trail: H2-01 §critic

From the note:

> H2-01:C-021 [danger: Critic: answers partly supported] - **D3 case A (levels vs composition, habitat fixed)**: Several studies report function levels more stable than composition.
>
> H2-01:C-023 [danger: Critic: answers partly supported] Contrary same-habitat evidence exists and is measured in full text, not only in the abstract-only Galand2018.
>
> H2-01:B-0072 [2.3 How processing choices move the estimate] - **Aggregation into gene sets that share members.** I re-checked Manor and Borenstein (2017) [FT].
>
> H2-01:A-068 [quote: Answers as delivered] Removing Galand2018 removes the only direct same-habitat contrary result, which is abstract only..
>
> H2-01:C-026 [danger: Critic: answers partly supported] The single-source sensitivity statement that Galand2018 is 'the only direct same-habitat contrary result' is therefore wrong.
>
> H2-01:C-050 [danger: Critic: answers partly supported] (1) D3 case A calls Galand2018 the only direct same-habitat contrary result.
>
> H2-01:C-051 [danger: Critic: answers partly supported] It is not: Manor2017's full text directly measures that revised functional profiles identify hosts as well as strain-level taxonomy does.
>

Not found in the cited text (where to look, not what is wrong): 2018; "Galand et al. (2018) is the only direct same-habitat result contrary to function levels being more stable than taxonomic composition."; Galand

## dns.9 (do not say)

"Across habitats, functional covariation was less stable than taxonomic covariation."

- why: The finding is from one human gut study with one heterogeneity test, whose cohorts differ in disease state and population, not habitat; it compares pathway covariation with species covariation, not with composition; and heterogeneity tests have more power for the stronger, more numerous pathway correlations.
- instead: covariation-stability.2
- trail: H2-01 §critic, §Adversarial

From the note:

> H2-01:C-036 [danger: Critic: answers partly supported] In one human gut study (Chen2020, verified), 64.3% of pathway co-abundances and 38.6% of species co-abundances differed in strength across four cohorts (Cochran's Q, FDR < 0.05).
>
> H2-01:A-089 [quote: Answers as delivered] In that setting functional covariation was less stable than taxonomic covariation (not composition itself), and changes in covariation usually came with changes in levels.
>
> H2-01:C-039 [danger: Critic: answers partly supported] The comparison contrasts pathway covariation with species covariation, not with composition.
>
> H2-01:C-040 [danger: Critic: answers partly supported] The cohorts differ in disease state and population, not habitat.
>
> H2-01:C-041 [danger: Critic: answers partly supported] Heterogeneity tests have more power for stronger and more numerous correlations, and that caution is not applied.
>
> H2-01:C-079 [warning: Adversarial critique, full findings] - D3 case D: 'In that setting functional covariation was less stable than taxonomic covariation'.
>
> H2-01:C-080 [warning: Adversarial critique, full findings] One study, one habitat, one heterogeneity test.
>
> H2-01:C-081 [warning: Adversarial critique, full findings] It is correctly scoped in the structured answer, but Section 6 states it without the power caveat.
>
> H2-01:C-116 [warning: Adversarial critique, full findings] Nor does it apply a power caution to the 64.3% against 38.6% heterogeneity comparison, where pathway correlations are stronger and more numerous and so easier to detect as heterogeneous.
>
> H2-01:C-127 [warning: Adversarial critique, full findings] - D3 case D uses cohorts that differ in disease state and population (IBD, obesity, two population cohorts) as the closest stand-in for habitat. The review flags this in the body, but the Section 6 summary loses the qualifier on what the variability is being compared against (species covariation, not composition).
>

Not found in the cited text (where to look, not what is wrong): "Across habitats, functional covariation was less stable than taxonomic covariation."

