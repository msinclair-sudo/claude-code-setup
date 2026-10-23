## covariation-transfer.5 (claim)

MetaCyc pathways share reactions and contributing species, so pathway-pathway co-abundance partly reflects shared members; 43,355 of about 58,653 possible pathway pairs were significant in at least one cohort, which points to strong common factors that would make replication easy; and "replicated at P < 0.05" with n = 77 is a lenient bar, so the 59% is an optimistic reading of transfer.

- conf: not stated
- class: reading (note: "Cautions (reviewer's reading)")
- holds: the IBD replication test
- src: chenGutMicrobialCoabundance2020
- trail: H2-01 §3.2, §answers

From the note:

> H2-01:B-0108 [3.2 Held-out study, same habitat (microbial, direct)] Cautions (reviewer's reading): MetaCyc pathways share reactions and contributing species, so pathway-pathway co-abundance partly reflects shared members. 43,355 of about 58,653 possible pathway pairs were significant in at least one cohort, which points to strong common factors that would make replication easy.
>
> H2-01:B-0109 [3.2 Held-out study, same habitat (microbial, direct)] "Replicated at P < 0.05" with n = 77 is a lenient bar.
>
> H2-01:A-034 [quote: Answers as delivered] Shared pathway members, strong common factors and a lenient threshold make this an optimistic reading of transfer.
>

Not found in the cited text (where to look, not what is wrong): 59; holds: ibd

## covariation-transfer.6 (claim)

No held-out test has used presence/absence profiles or compared annotation schemes.

- conf: not stated
- class: search (note: "Not measured")
- holds: microbial functional profiles in a held-out design
- src: none (a statement of what was not measured)
- search: not stated
- trail: H2-01 §answers

From the note:

> H2-01:A-047 [quote: Answers as delivered] *Not measured:* Any microbial test withholding a whole habitat.
>
> H2-01:A-049 [quote: Answers as delivered] Any test with presence/absence profiles, or comparing annotation schemes, in a held-out design.
>

## covariation-transfer.7 (claim)

No held-out test has been made in soils, oceans or other non-human habitats at all.

- conf: not stated
- class: search (note: "Not measured")
- holds: held-out tests of microbial functional profiles
- src: none (a statement of what was not measured)
- search: not stated
- trail: H2-01 §answers

From the note:

> H2-01:A-047 [quote: Answers as delivered] *Not measured:* Any microbial test withholding a whole habitat.
>
> H2-01:A-050 [quote: Answers as delivered] Held-out tests in soils, oceans or other non-human habitats at all..
>

## neighbouring-transfer.1 (claim)

PICRUSt accuracy fell with distance to the nearest reference genome (NSTI), across all samples (r = −0.4) and within each habitat (r = −0.25 to −0.82); accuracy was high in soils (0.81) and low in a hypersaline mat (reported 0.25, mean NSTI 0.23).

- conf: not stated
- class: meas (marker)
- holds: a genome-derived taxon-to-gene mapping transferred across habitats, not covariation among functions
- src: langillePredictiveFunctionalProfiling2013 (FT; measured)
- trail: H2-01 §3.3

From the note:

> H2-01:I-0019 [3.3 Neighbouring microbial tests (different quantity, labelled)] - **Taxon-to-function mappings transferred across habitats.** PICRUSt accuracy fell with distance to the nearest reference genome (NSTI), across all samples (r = −0.4) and within each habitat (r = −0.25 to −0.82); accuracy was high in soils (0.81) and low in a hypersaline mat (reported 0.25, mean NSTI 0.23) [Langille2013; FT; measured].
>
> H2-01:B-0112 [3.3 Neighbouring microbial tests (different quantity, labelled)] These transfer a genome-derived taxon-to-gene mapping, not covariation among functions.
>

## neighbouring-transfer.2 (claim)

The per-sample Spearman metric is almost insensitive to permuting genes across samples, and inference-level agreement of metagenome prediction tools was reasonable in human datasets and much lower in non-human and soil datasets.

- conf: not stated
- class: not stated
- holds: human, non-human and soil datasets; a taxon-to-gene mapping, not covariation among functions
- src: sunInferenceBasedAccuracyMetagenome2020 (FT)
- trail: H2-01 §3.3

From the note:

> H2-01:R-0231 [Reference list] Inference-based accuracy of metagenome prediction tools varies across sample types and functional categories.
>
> H2-01:B-0111 [3.3 Neighbouring microbial tests (different quantity, labelled)] Sun et al. (2020) showed that the per-sample Spearman metric is almost insensitive to permuting genes across samples, and that inference-level agreement was reasonable in human datasets and much lower in non-human and soil datasets [Sun2020; FT].
>
> H2-01:B-0112 [3.3 Neighbouring microbial tests (different quantity, labelled)] These transfer a genome-derived taxon-to-gene mapping, not covariation among functions.
>

## neighbouring-transfer.3 (claim)

These mapping results suggest that taxon-to-function mappings transfer less well as reference coverage of the target habitat falls.

- conf: not stated
- class: not stated
- holds: taxon-to-function mappings, a quantity other than function-function covariation
- src: langillePredictiveFunctionalProfiling2013, sunInferenceBasedAccuracyMetagenome2020
- trail: H2-01 §3.3, §answers

From the note:

> H2-01:B-0113 [3.3 Neighbouring microbial tests (different quantity, labelled)] They do suggest that transfer depends on reference coverage of the target habitat.
>
> H2-01:A-035 [quote: Answers as delivered] Neighbouring microbial evidence concerns other quantities: taxon-to-function mappings transfer less well as reference coverage of the target habitat falls [Langille2013; Sun2020]; functional-profile classifiers transfer across studies at AUROC 0.70 to 0.89 in human gut [Wirbel2019]; gene co-occurrence across genomes predicts held-out genomes and held-out phyla, with predictability varying by phylum [Beavan2024; KonnoIwasaki2023].
>

## neighbouring-transfer.4 (claim)

Colorectal cancer classifiers on eggNOG groups gave AUROC 0.70 to 0.81 study-to-study and 0.78 to 0.89 leave-one-study-out, similar to species-level classifiers.

- conf: not stated
- class: meas (marker)
- holds: human gut only; a classifier, not a covariance structure
- src: wirbelMetaanalysisFecalMetagenomes2019 (FT; measured)
- trail: H2-01 §3.3, §answers

From the note:

> H2-01:I-0020 [3.3 Neighbouring microbial tests (different quantity, labelled)] - **Supervised models on functional profiles across studies.** Colorectal cancer classifiers on eggNOG groups gave AUROC 0.70 to 0.81 study-to-study and 0.78 to 0.89 leave-one-study-out, similar to species-level classifiers [Wirbel2019; FT; measured].
>
> H2-01:B-0114 [3.3 Neighbouring microbial tests (different quantity, labelled)] Human gut only; a classifier, not a covariance structure.
>
> H2-01:A-035 [quote: Answers as delivered] Neighbouring microbial evidence concerns other quantities: taxon-to-function mappings transfer less well as reference coverage of the target habitat falls [Langille2013; Sun2020]; functional-profile classifiers transfer across studies at AUROC 0.70 to 0.89 in human gut [Wirbel2019]; gene co-occurrence across genomes predicts held-out genomes and held-out phyla, with predictability varying by phylum [Beavan2024; KonnoIwasaki2023].
>

## neighbouring-transfer.5 (claim)

In the E. coli pangenome, accessory-gene presence was predicted from other accessory genes on held-out random genomes; after filtering and removing phylogenetic signal, 16.7% of families were predictable at F1 ≥ 0.9 against a chance rate of about 1 to 1.7%.

- conf: single (marker)
- class: not stated
- holds: gene co-occurrence across genomes of the E. coli pangenome, not across samples
- src: beavanContingencyRepeatabilityPredictability2023 (FT; SINGLE SOURCE)
- trail: H2-01 §3.3, §answers

From the note:

> H2-01:I-0021 [3.3 Neighbouring microbial tests (different quantity, labelled)] - **Gene co-occurrence across genomes.** In the E. coli pangenome, accessory-gene presence was predicted from other accessory genes on held-out random genomes; after filtering and removing phylogenetic signal, 16.7% of families were predictable at F1 ≥ 0.9 against a chance rate of about 1 to 1.7% [Beavan2024; FT; SINGLE SOURCE].
>
> H2-01:A-035 [quote: Answers as delivered] Neighbouring microbial evidence concerns other quantities: taxon-to-function mappings transfer less well as reference coverage of the target habitat falls [Langille2013; Sun2020]; functional-profile classifiers transfer across studies at AUROC 0.70 to 0.89 in human gut [Wirbel2019]; gene co-occurrence across genomes predicts held-out genomes and held-out phyla, with predictability varying by phylum [Beavan2024; KonnoIwasaki2023].
>

## neighbouring-transfer.6 (claim)

Across about 3,000 genomes, gene gain and loss in metabolic pathways was predictable in a hold-one-phylum-out test for each of the 10 largest phyla, with predictability differing significantly among phyla.

- conf: single (marker)
- class: model (marker)
- holds: about 3,000 bacterial genomes; phylogenetic gene gain/loss prediction in metabolic pathways
- src: konnoMachineLearningEnables2023 (FT; modelled; SINGLE SOURCE)
- trail: H2-01 §3.3, §answers

From the note:

> H2-01:R-0159 [Reference list] Machine learning enables prediction of metabolic system evolution in bacteria.
>
> H2-01:C-017 [danger: Critic: answers partly supported] It pools different quantities: covariance or dictionary transfer (Cleary2017, Pierson2015), taxon-to-gene mapping accuracy (Langille2013 NSTI), and phylogenetic gene gain/loss prediction (KonnoIwasaki2023).
>
> H2-01:I-0022 [3.3 Neighbouring microbial tests (different quantity, labelled)] Across about 3,000 genomes, gene gain and loss in metabolic pathways was predictable in a hold-one-phylum-out test for each of the 10 largest phyla, with predictability differing significantly among phyla [KonnoIwasaki2023; FT; modelled; SINGLE SOURCE].
>
> H2-01:A-035 [quote: Answers as delivered] Neighbouring microbial evidence concerns other quantities: taxon-to-function mappings transfer less well as reference coverage of the target habitat falls [Langille2013; Sun2020]; functional-profile classifiers transfer across studies at AUROC 0.70 to 0.89 in human gut [Wirbel2019]; gene co-occurrence across genomes predicts held-out genomes and held-out phyla, with predictability varying by phylum [Beavan2024; KonnoIwasaki2023].
>

Not found in the cited text (where to look, not what is wrong): holds: bacterial

## neighbouring-transfer.7 (claim)

Gene content predicted MAG niche position along Baltic Sea gradients better than phylogeny under genome-level cross-validation.

- conf: not stated
- class: not stated
- holds: Baltic Sea metagenome-assembled genomes
- src: alnebergEcosystemwideMetagenomicBinning2020 (FT)
- trail: H2-01 §3.3

From the note:

> H2-01:B-0115 [3.3 Neighbouring microbial tests (different quantity, labelled)] Gene content predicted MAG niche position along Baltic Sea gradients better than phylogeny under genome-level cross-validation [Alneberg2020; FT].
>

Not found in the cited text (where to look, not what is wrong): holds: metagenome-assembled

## neighbouring-transfer.8 (claim)

Phylogenetic-profile co-occurrence recovered same-pathway enzyme pairs better than homology, in a benchmark partly circular with KEGG membership.

- conf: not stated
- class: not stated
- holds: a benchmark partly circular with KEGG membership
- src: chungAssemblingBacterialPuzzles2024 (AB)
- trail: H2-01 §3.3

From the note:

> H2-01:B-0116 [3.3 Neighbouring microbial tests (different quantity, labelled)] Phylogenetic-profile co-occurrence recovered same-pathway enzyme pairs better than homology [Chung2024; AB], a benchmark partly circular with KEGG membership.
>

## neighbouring-transfer.9 (claim)

A low-dimensional gene-to-function map transferred from strains to communities for denitrification.

- conf: not stated
- class: not stated
- holds: denitrification
- src: gowdaGenomicStructurePredicts2022 (AB)
- trail: H2-01 §3.3

From the note:

> H2-01:B-0117 [3.3 Neighbouring microbial tests (different quantity, labelled)] - **A low-dimensional gene-to-function map transferred from strains to communities** for denitrification [Gowda2022; AB].
>

## neighbouring-transfer.10 (claim)

Five "generalizable" enterosignatures were found from 5,230 gut metagenomes; what "generalizable" means (the held-out design) was not read.

- conf: not stated
- class: not stated
- holds: human gut metagenomes; taxonomic low-rank structure
- src: friouxEnterosignaturesDefineCommon2023 (AB)
- limit: access (note: "was not read")
- trail: H2-01 §3.3

From the note:

> H2-01:R-0132 [Reference list] Enterosignatures define common bacterial guilds in the human gut microbiome.
>
> H2-01:B-0118 [3.3 Neighbouring microbial tests (different quantity, labelled)] - **Taxonomic low-rank structure.** Five "generalizable" enterosignatures from 5,230 gut metagenomes [Frioux2023; AB].
>
> H2-01:B-0119 [3.3 Neighbouring microbial tests (different quantity, labelled)] The meaning of "generalizable" (held-out design) was not read.
>

## other-field-transfer.1 (claim)

Sparse module dictionaries learned on 5% of samples of a TCGA tumour type gave about 87% recovery (Spearman, SMAF) within the same tumour type, and a dictionary from a different tumour type gave 68% on average, with related tumour types doing better; these figures are Spearman recovery of expression from 25 simulated random composite measurements through the dictionary (compressed sensing, m = 25, g = 5,000), not a direct covariance-reproduction score.

- conf: single (marker)
- class: meas (marker)
- holds: TCGA tumour types, transcriptomics; a withheld tissue type, the closest other-field analogue of a withheld habitat; the authors warn a dictionary is biased when training data do not represent the test data
- src: clearyEfficientGenerationTranscriptomic2017 (FT; measured; SINGLE SOURCE)
- trail: H2-01 §3.4, §answers, §critic, §Adversarial

From the note:

> H2-01:B-0170 [5. How the cases relate, and failure modes] The same pattern appears in transcriptomics, where low dimensionality within datasets (Heimberg2016) coexists with unstable higher components across datasets (Lenz2016) and partial transfer across tissue types (Cleary2017).
>
> H2-01:B-0120 [3.4 Held-out tests in other fields] - **Withheld tissue type (the closest analogue of a withheld habitat).** Sparse module dictionaries learned on 5% of samples recovered held-out profiles of the same TCGA tumour type at about 87% (Spearman, SMAF).
>
> H2-01:I-0023 [3.4 Held-out tests in other fields] A dictionary from a different tumour type gave 68% on average, and related tumour types did better [Cleary2017; FT; measured; SINGLE SOURCE].
>
> H2-01:B-0121 [3.4 Held-out tests in other fields] The authors warn that a dictionary is biased when training data do not represent the test data.
>
> H2-01:A-037 [quote: Answers as delivered] Module dictionaries went from about 87% recovery within a tumour type to 68% across types, better for related types [Cleary2017].
>
> H2-01:A-054 [quote: Answers as delivered] Removing Cleary2017 leaves no other-field test that withholds a biologically distinct group (the closest analogue of a habitat)..
>
> H2-01:C-019 [danger: Critic: answers partly supported] Cleary2017's 87% to 68% is recovery of expression from 25 random composite measurements through a learned dictionary (compressed sensing).
>
> H2-01:C-020 [danger: Critic: answers partly supported] It is not a direct covariance-reproduction score, and the answer should say so.
>
> H2-01:C-063 [warning: Adversarial critique, full findings] - Cleary2017: the 87% to 68% figures are correct, but the review describes them as dictionaries that 'recovered held-out profiles'.
>
> H2-01:C-064 [warning: Adversarial critique, full findings] They are Spearman recovery from 25 simulated random composite measurements through the dictionary (compressed sensing, m = 25, g = 5,000).
>
> H2-01:C-065 [warning: Adversarial critique, full findings] The answer states the transfer more directly than the full text supports.
>

## other-field-transfer.2 (claim)

A linear model from about 1,000 landmark genes, trained on GEO microarrays, inferred 81% of non-measured transcripts well in independent GTEx RNA-seq (8,555 samples); about 19% were not well inferred.

- conf: single (marker)
- class: meas (marker)
- holds: transcriptomics; a withheld study and platform
- src: subramanianNextGenerationConnectivity2017 (FT; measured; SINGLE SOURCE)
- trail: H2-01 §3.4, §answers

From the note:

> H2-01:I-0024 [3.4 Held-out tests in other fields] - **Withheld study and platform.** A linear model from about 1,000 landmark genes, trained on GEO microarrays, inferred 81% of non-measured transcripts well in independent GTEx RNA-seq (8,555 samples); about 19% were not well inferred [Subramanian2017; FT; measured; SINGLE SOURCE].
>
> H2-01:A-038 [quote: Answers as delivered] A landmark model inferred 81% of genes well in an independent study and platform [Subramanian2017].
>

## other-field-transfer.3 (claim)

A single co-expression network fitted to all 35 GTEx tissues pooled had held-out likelihood so low it was dropped from the comparison; per-tissue networks did better, and sharing between related tissues did better again, so pooled networks represented individual tissues poorly.

- conf: single (critic: C-121)
- class: meas (marker)
- holds: 35 GTEx human tissues; samples, not tissues, were withheld
- src: piersonSharingSpecificityCoexpression2015 (FT; measured; SINGLE SOURCE; critic: C-121 was "FT; measured")
- trail: H2-01 §3.4, §answers, §Adversarial

From the note:

> H2-01:R-0204 [Reference list] Sharing and specificity of co-expression networks across 35 human tissues.
>
> H2-01:I-0025 [3.4 Held-out tests in other fields] - **Pooled versus tissue-specific covariance, held-out samples within tissue.** A single network fitted to all 35 GTEx tissues pooled had held-out likelihood so low it was dropped from the comparison; per-tissue networks did better, and sharing between related tissues did better again [Pierson2015; FT; measured].
>
> H2-01:B-0122 [3.4 Held-out tests in other fields] Samples, not tissues, were withheld.
>
> H2-01:A-039 [quote: Answers as delivered] Pooled co-expression networks represented individual tissues poorly [Pierson2015].
>
> H2-01:C-119 [warning: Adversarial critique, full findings] - SINGLE SOURCE flags are applied unevenly.
>
> H2-01:C-121 [warning: Adversarial critique, full findings] Heimberg2016 (low dimension) and Pierson2015 (pooled networks poor) carry the same weight from one study and are not flagged.
>

## other-field-transfer.4 (claim)

Individual co-expression networks predicted GO membership with mean AUROC 0.60 (bulk) and 0.56 (single cell), aggregating 163 networks reached 0.73 (bulk), and sample size did not predict performance, so individual co-expression networks replicate modestly.

- conf: not stated
- class: meas (marker)
- holds: co-expression networks, bulk and single-cell expression
- src: crowExploitingSinglecellExpression2016 (FT; measured)
- trail: H2-01 §3.4, §answers

From the note:

> H2-01:I-0026 [3.4 Held-out tests in other fields] - **Replicability of co-expression.** Individual co-expression networks predicted GO membership with mean AUROC 0.60 (bulk) and 0.56 (single cell); aggregating 163 networks reached 0.73 (bulk). Sample size did not predict performance [Crow2016; FT; measured].
>
> H2-01:A-040 [quote: Answers as delivered] Individual co-expression networks replicate modestly [Crow2016].
>

## other-field-transfer.5 (claim)

A latent space learned on recount2 was concordant with dataset-specific models in rare-disease studies, with broader training capturing more pathways.

- conf: not stated
- class: not stated
- holds: transcriptomics, rare-disease studies; qualitative
- src: taroniMultiPLIERTransferLearning2019 (FT; qualitative)
- trail: H2-01 §3.4

From the note:

> H2-01:R-0240 [Reference list] MultiPLIER: a transfer learning framework for transcriptomics reveals systemic features of rare disease.
>
> H2-01:B-0123 [3.4 Held-out tests in other fields] - **Latent spaces transferred to new studies.** A latent space learned on recount2 was concordant with dataset-specific models in rare-disease studies, with broader training capturing more pathways [Taroni2019; FT; qualitative]. projectR tests whether a pattern is shared by projection [SteinOBrien2019; FT; framework, no failure rate].
>

## other-field-transfer.6 (claim)

projectR tests whether a pattern is shared by projection; it is a framework and reports no failure rate.

- conf: not stated
- class: not stated
- holds: a projection framework for transfer learning across cellular measurements
- src: steinobrienDecomposingCellIdentity2019 (FT; framework, no failure rate)
- trail: H2-01 §3.4

From the note:

> H2-01:R-0225 [Reference list] Decomposing cell identity for transfer learning across cellular measurements, platforms, tissues, and species.
>
> H2-01:B-0123 [3.4 Held-out tests in other fields] - **Latent spaces transferred to new studies.** A latent space learned on recount2 was concordant with dataset-specific models in rare-disease studies, with broader training capturing more pathways [Taroni2019; FT; qualitative]. projectR tests whether a pattern is shared by projection [SteinOBrien2019; FT; framework, no failure rate].
>

## other-field-transfer.7 (claim)

Global leaf-economics correlations may not hold at local scales, since correlation strength only bounds how differently traits can vary across scales.

- conf: not stated
- class: not stated
- holds: plant leaf traits; transfer across scale, not across habitat
- src: messierTraitVariationIntegration2016 (AB)
- trail: H2-01 §3.4

From the note:

> H2-01:B-0124 [3.4 Held-out tests in other fields] - **Plant traits across scales.** Global leaf-economics correlations may not hold at local scales, since correlation strength only bounds how differently traits can vary across scales [Messier2017; AB].
>
> H2-01:B-0126 [3.4 Held-out tests in other fields] These are transfers across scale or taxonomic level, not across habitat.
>

## other-field-transfer.8 (claim)

Some leaf-trait correlations reverse sign within species compared with across species.

- conf: not stated
- class: not stated
- holds: plant leaf traits; transfer across taxonomic level, not across habitat
- src: andereggWithinspeciesPatternsChallenge2018 (AB)
- trail: H2-01 §3.4

From the note:

> H2-01:B-0125 [3.4 Held-out tests in other fields] Some leaf-trait correlations reverse sign within species compared with across species [Anderegg2018; AB].
>
> H2-01:B-0126 [3.4 Held-out tests in other fields] These are transfers across scale or taxonomic level, not across habitat.
>

Not found in the cited text (where to look, not what is wrong): holds: plant

## other-field-transfer.9 (claim)

In other fields, covariation transfers partly, each result from a single study.

- conf: single (critic: C-015)
- class: not stated
- holds: transcriptomics and other fields, not microbial
- src: clearyEfficientGenerationTranscriptomic2017, subramanianNextGenerationConnectivity2017, piersonSharingSpecificityCoexpression2015, crowExploitingSinglecellExpression2016
- rating: "Moderate for partial transfer in transcriptomics, but that is another field and each quantitative result is a single study"
- trail: H2-01 §answers, §critic

From the note:

> H2-01:A-036 [quote: Answers as delivered] Other fields: covariation transfers partly.
>
> H2-01:A-044 [quote: Answers as delivered] Moderate for partial transfer in transcriptomics, but that is another field and each quantitative result is a single study..
>
> H2-01:C-015 [danger: Critic: answers partly supported] Other fields show partial transfer, each result from a single study.
>

## other-field-transfer.10 (claim)

There is no direct conflict on the same quantity: reproduction is high in some tests (Subramanian's 81%; Chen's reductive TCA cycle at 94.7%) and low in others (Cleary's cross-type drop; pooled networks in Pierson; sign reversals across scales in plant traits).

- conf: not stated
- class: not stated
- holds: the held-out tests across fields
- src: subramanianNextGenerationConnectivity2017, chenGutMicrobialCoabundance2020, clearyEfficientGenerationTranscriptomic2017, piersonSharingSpecificityCoexpression2015, andereggWithinspeciesPatternsChallenge2018
- trail: H2-01 §answers

From the note:

> H2-01:A-045 [quote: Answers as delivered] *Conflicts:* No direct conflict on the same quantity.
>
> H2-01:A-046 [quote: Answers as delivered] Reproduction is high in some tests (Subramanian 81%; Chen reductive TCA 94.7%) and low in others (Cleary cross-type drop; pooled networks in Pierson; sign reversals across scales in plant traits [Anderegg2018]); the differences track how different the target is from the training data..
>

Not found in the cited text (where to look, not what is wrong): holds: held-out; holds: fields

## transfer-dependence.1 (claim)

The review's synthesis is that, across the other-field and neighbouring evidence, transfer depends on the similarity of the training set to the target (related tumour types; related tissues; NSTI; phylum differences), the breadth of the training set, and the fraction of the target that is shared mean structure against target-specific signal; the critic holds that this pools incommensurable tests of different quantities (covariance or dictionary transfer, taxon-to-gene mapping accuracy, per-sample accuracy metrics, phylogenetic gene gain/loss prediction) and is the reviewer's synthesis, not a finding.

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

## levels-within-habitat.1 (claim)

Within a habitat where taxonomy turns over, several studies report function levels more stable than taxonomic composition (HMP pathways against organisms; bromeliad microcosms; macroalgal host COGs against species; soil microcosm functional groups; vermicomposting turnover rates), two in full text and three resting on abstracts; the direction is best described as reported by several studies but dependent on processing, with direct measured contrary evidence in human gut and coastal ocean.

- conf: not stated
- class: not stated
- holds: habitat held roughly fixed; none of the studies controls for normalisation, aggregation and granularity together
- src: theStructureFunctionDiversity2012 (FT), burkeBacterialCommunityAssembly2011 (FT), loucaHighTaxonomicVariability2016 (AB), shanAnnotationfreeDiscoveryFunctional2023 (AB), airaFasterTurnoverTaxonomic2026 (AB), manorRevisedComputationalMetagenomic2017, galandStrongLinkMarine2018 (AB)
- rating: "Moderate for the direction as reported, weak for the claim that the stability is biological rather than processing-driven"
- contrary: one-sided (critic: C-123)
- trail: H2-01 §4.1, §answers, §6. Answers, §critic, §Adversarial

From the note:

> H2-01:B-0131 [4.1 Function levels against taxonomic composition, habitat held roughly constant, taxonomy turns over] This is the best-covered cell, and the evidence mostly says levels are more stable than composition, with serious cautions.
>
> H2-01:A-055 [quote: Answers as delivered] **D3 case A: function levels against taxonomic composition, habitat roughly fixed, taxonomy turns over**: Most measured studies report function levels more stable than taxonomic composition: HMP pathways against organisms [HMP2012], bromeliad microcosms [Louca2016b, abstract], macroalgal host COGs against species [Burke2011], soil microcosm functional groups [Shan2023, abstract], vermicomposting turnover rates [Aira2026, abstract].
>
> H2-01:A-057 [quote: Answers as delivered] This pattern depends on processing and annotation.
>
> H2-01:A-061 [quote: Answers as delivered] *Strength:* Moderate for the direction as reported, weak for the claim that the stability is biological rather than processing-driven.
>
> H2-01:A-062 [quote: Answers as delivered] Several independent studies agree, but none controls for normalisation, aggregation and granularity together..
>
> H2-01:A-063 [quote: Answers as delivered] *Conflicts:* Galand2018 (and the processing studies Manor2017, Nayfach2015) against HMP2012, Louca2016b, Burke2011..
>
> H2-01:A-113 [6. Answers by direction] **D3.** Levels versus composition within a habitat: levels mostly more stable, but processing-sensitive.
>
> H2-01:C-021 [danger: Critic: answers partly supported] - **D3 case A (levels vs composition, habitat fixed)**: Several studies report function levels more stable than composition.
>
> H2-01:C-022 [danger: Critic: answers partly supported] Two are full text (HMP2012, Burke2011); three rest on abstracts (Louca2016b, Shan2023, Aira2026).
>
> H2-01:C-023 [danger: Critic: answers partly supported] Contrary same-habitat evidence exists and is measured in full text, not only in the abstract-only Galand2018.
>
> H2-01:C-027 [danger: Critic: answers partly supported] The direction is best described as reported by several studies but dependent on processing, with direct measured contrary evidence in human gut (Manor2017) and coastal ocean (Galand2018, abstract).
>
> H2-01:C-122 [warning: Adversarial critique, full findings] - D3 case A: processing cautions are applied to the 'levels stable' studies, which is appropriate.
>
> H2-01:C-123 [warning: Adversarial critique, full findings] But Manor2017's direct measured counter-result (revised functional profiles as host-specific as strain taxonomy) is used only as a caution, not as contrary evidence, and Galand2018 (abstract) is presented as the only contrary result.
>
> H2-01:C-124 [warning: Adversarial critique, full findings] Contrary evidence is under-weighted relative to its access.
>
> H2-01:C-123 [warning: Adversarial critique, full findings] But Manor2017's direct measured counter-result (revised functional profiles as host-specific as strain taxonomy) is used only as a caution, not as contrary evidence, and Galand2018 (abstract) is presented as the only contrary result.
>

## levels-within-habitat.2 (claim)

Bromeliad tank microcosms showed similar functional-group structure across replicates and highly variable taxonomy within groups.

- conf: not stated
- class: meas (marker)
- holds: bromeliad tank microcosms
- src: loucaHighTaxonomicVariability2016 (AB; measured)
- trail: H2-01 §4.1

From the note:

> H2-01:I-0028 [4.1 Function levels against taxonomic composition, habitat held roughly constant, taxonomy turns over] - Bromeliad tank microcosms: similar functional-group structure across replicates, highly variable taxonomy within groups [Louca2016b; AB; measured].
>

## levels-within-habitat.3 (claim)

On a macroalgal host, species composition was about 15% similar against 70% similarity in COG composition; the contrast compares a species table with a coarser COG table, and the taxonomic figure is from an earlier study.

- conf: not stated
- class: meas (marker)
- holds: bacterial communities on a macroalgal host
- src: burkeBacterialCommunityAssembly2011 (FT; measured)
- trail: H2-01 §4.1

From the note:

> H2-01:R-0091 [Reference list] Bacterial community assembly based on functional genes rather than species.
>
> H2-01:I-0029 [4.1 Function levels against taxonomic composition, habitat held roughly constant, taxonomy turns over] - A macroalgal host: about 15% similarity in species composition against 70% in COG composition [Burke2011; FT; measured].
>
> H2-01:B-0132 [4.1 Function levels against taxonomic composition, habitat held roughly constant, taxonomy turns over] The contrast compares a species table with a coarser COG table, and the taxonomic figure is from an earlier study.
>

## levels-within-habitat.4 (claim)

In replicate soil microcosms, annotation-free functional groups were stable in summed abundance despite large variation in species composition.

- conf: not stated
- class: not stated
- holds: replicate soil microcosms
- src: shanAnnotationfreeDiscoveryFunctional2023 (AB)
- trail: H2-01 §4.1

From the note:

> H2-01:B-0133 [4.1 Function levels against taxonomic composition, habitat held roughly constant, taxonomy turns over] - Replicate soil microcosms: annotation-free functional groups stable in summed abundance despite large variation in species composition [Shan2023; AB].
>

## levels-within-habitat.5 (claim)

During vermicomposting, taxonomic turnover over time was about twelve times functional turnover.

- conf: not stated
- class: not stated
- holds: vermicomposting over time; no non-earthworm control
- src: airaFasterTurnoverTaxonomic2026 (AB; no non-earthworm control)
- trail: H2-01 §4.1

From the note:

> H2-01:B-0134 [4.1 Function levels against taxonomic composition, habitat held roughly constant, taxonomy turns over] - Vermicomposting over time: taxonomic turnover about twelve times functional turnover [Aira2026; AB; no non-earthworm control].
>

## levels-within-habitat.6 (claim)

A model found taxa-function robustness higher in gut than in vaginal communities, so how far function tracks taxonomy may itself vary by habitat.

- conf: single (critic: C-082)
- class: model (marker)
- holds: one modelled, abstract-only study comparing gut and vaginal communities
- src: engTaxafunctionRobustnessMicrobial2018 (AB; modelled)
- trail: H2-01 §4.1, §answers, §Adversarial

From the note:

> H2-01:I-0030 [4.1 Function levels against taxonomic composition, habitat held roughly constant, taxonomy turns over] - A model: taxa-function robustness higher in gut than vaginal communities, so how far function tracks taxonomy is itself habitat-dependent [EngBorenstein2018; AB; modelled].
>
> H2-01:A-060 [quote: Answers as delivered] How far function tracks taxonomy may itself vary by habitat [EngBorenstein2018, modelled].
>
> H2-01:C-082 [warning: Adversarial critique, full findings] - D3 case A: 'How far function tracks taxonomy may itself vary by habitat [EngBorenstein2018]'. One modelled, abstract-only study comparing gut and vaginal communities.
>

## levels-within-habitat.7 (claim)

Within the human gut, how consistently genera carry metabolic modules differs among genera, and module-derived redundancy was lower in the Bacteroides enterotype.

- conf: not stated
- class: not stated
- holds: human gut
- src: vieirasilvaSpeciesfunctionRelationshipsShape2016 (AB)
- trail: H2-01 §4.1

From the note:

> H2-01:B-0135 [4.1 Function levels against taxonomic composition, habitat held roughly constant, taxonomy turns over] - Within the human gut, how consistently genera carry metabolic modules differs among genera, and module-derived redundancy was lower in the Bacteroides enterotype [VieiraSilva2016; AB].
>

## levels-within-habitat.8 (claim)

In a coastal Mediterranean time series, Galand et al. (2018) report a strong taxonomy-function link when function is measured from all reads or all predicted genes, and weaker links with annotated orthologues or taxonomy-inferred functions, and conclude that this challenges functional redundancy; the abstract is explicit that using all reads, not annotated genes, was essential.

- conf: not stated
- class: not stated
- holds: coastal Mediterranean time series; the reported R² values came from an automated summary and are not used
- src: galandStrongLinkMarine2018 (AB)
- limit: access (note: "so it stays abstract only and its R2 values are not used")
- trail: H2-01 §4.1, §answers, §Provenance

From the note:

> H2-01:B-0138 [4.1 Function levels against taxonomic composition, habitat held roughly constant, taxonomy turns over] Galand et al. (2018), in a coastal Mediterranean time series, report a strong taxonomy-function link when function is measured from all reads or all predicted genes, weaker links with annotated orthologues or taxonomy-inferred functions, and conclude that this challenges functional redundancy [Galand2018; AB for me; the reported R² values came from an automated summary and are not used].
>
> H2-01:B-0139 [4.1 Function levels against taxonomic composition, habitat held roughly constant, taxonomy turns over] The abstract is explicit that using all reads, not annotated genes, was essential.
>
> H2-01:A-059 [quote: Answers as delivered] In a coastal time series, taxonomy and function were strongly linked when function was measured from all reads rather than annotated orthologues [Galand2018, abstract].
>
> H2-01:B-0015 [info: Provenance] Attempts to reach Galand2018 full text (PMC6155072 via E-utilities returned front matter only; Europe PMC fullTextXML returned an empty record) failed, so it stays abstract only and its R2 values are not used.
>

## levels-within-habitat.9 (claim)

Revised processing (MUSiCC normalisation, filtering of prevalent families, non-uniform mapping) gave functional profiles that identified hosts as well as strain-level taxonomic markers did: a direct, measured same-habitat counter-result to functional stability.

- conf: not stated
- class: meas (critic: C-123)
- holds: human gut; verified against full text by the critic
- src: manorRevisedComputationalMetagenomic2017 (FT, re-checked)
- trail: H2-01 §critic, §Adversarial

From the note:

> H2-01:C-023 [danger: Critic: answers partly supported] Contrary same-habitat evidence exists and is measured in full text, not only in the abstract-only Galand2018.
>
> H2-01:C-024 [danger: Critic: answers partly supported] Manor2017 (verified) found that revised processing (MUSiCC normalisation, filtering of prevalent families, non-uniform mapping) gave functional profiles that identified hosts as well as strain-level taxonomic markers did.
>
> H2-01:C-027 [danger: Critic: answers partly supported] The direction is best described as reported by several studies but dependent on processing, with direct measured contrary evidence in human gut (Manor2017) and coastal ocean (Galand2018, abstract).
>
> H2-01:C-051 [danger: Critic: answers partly supported] It is not: Manor2017's full text directly measures that revised functional profiles identify hosts as well as strain-level taxonomy does.
>
> H2-01:C-123 [warning: Adversarial critique, full findings] But Manor2017's direct measured counter-result (revised functional profiles as host-specific as strain taxonomy) is used only as a caution, not as contrary evidence, and Galand2018 (abstract) is presented as the only contrary result.
>

## levels-within-habitat.10 (claim)

The counter-evidence within a habitat is methodological and applies to every study above: relative normalisation and pathway aggregation reduce apparent functional variability, genome size creates both spurious variability and spurious stability, and a dominant mean profile makes profiles look alike, so the "levels stable, taxonomy variable" pattern depends on processing and annotation scheme.

- conf: not stated
- class: not stated
- holds: same-habitat comparisons of function levels and taxonomic composition
- src: manorRevisedComputationalMetagenomic2017 (FT, re-checked), nayfachAverageGenomeSize2015, manorMUSiCCMarkerGenes2015, sunInferenceBasedAccuracyMetagenome2020
- trail: H2-01 §4.1, §answers

From the note:

> H2-01:B-0136 [4.1 Function levels against taxonomic composition, habitat held roughly constant, taxonomy turns over] The counter-evidence here is methodological, and it applies to every item above.
>
> H2-01:B-0137 [4.1 Function levels against taxonomic composition, habitat held roughly constant, taxonomy turns over] Relative normalisation and pathway aggregation reduce apparent functional variability [Manor2017; FT, re-checked]; genome size creates both spurious variability and spurious stability [Nayfach2015; Manor2015]; a dominant mean profile makes profiles look alike [Sun2020]; comparing a fine taxonomic table with a coarse functional table favours functional stability by construction (reviewer's reading, applied equally to Burke2011 and Ramírez-Flandes2019).
>
> H2-01:B-0140 [4.1 Function levels against taxonomic composition, habitat held roughly constant, taxonomy turns over] So the "levels stable, taxonomy variable" pattern depends on annotation scheme.
>
> H2-01:A-057 [quote: Answers as delivered] This pattern depends on processing and annotation.
>
> H2-01:A-058 [quote: Answers as delivered] Relative normalisation and KEGG aggregation reduce functional variability [Manor2017], genome size makes stable genes look variable and variable genes look stable [Nayfach2015], a shared mean profile makes profiles look alike [Sun2020], and comparing fine taxonomy with coarse function favours functional stability by construction (reviewer's reading).
>

Not found in the cited text (where to look, not what is wrong): holds: same-habitat

## levels-within-habitat.11 (claim)

Comparing a fine taxonomic table with a coarse functional table favours functional stability by construction, which applies equally to Burke2011 and Ramírez-Flandes2019.

- conf: not stated
- class: reading (note: "reviewer's reading")
- holds: comparisons of tables at different granularity
- src: burkeBacterialCommunityAssembly2011, ramirezflandesRedoxTraitsCharacterize2019
- trail: H2-01 §4.1, §answers

From the note:

> H2-01:B-0137 [4.1 Function levels against taxonomic composition, habitat held roughly constant, taxonomy turns over] Relative normalisation and pathway aggregation reduce apparent functional variability [Manor2017; FT, re-checked]; genome size creates both spurious variability and spurious stability [Nayfach2015; Manor2015]; a dominant mean profile makes profiles look alike [Sun2020]; comparing a fine taxonomic table with a coarse functional table favours functional stability by construction (reviewer's reading, applied equally to Burke2011 and Ramírez-Flandes2019).
>
> H2-01:A-058 [quote: Answers as delivered] Relative normalisation and KEGG aggregation reduce functional variability [Manor2017], genome size makes stable genes look variable and variable genes look stable [Nayfach2015], a shared mean profile makes profiles look alike [Sun2020], and comparing fine taxonomy with coarse function favours functional stability by construction (reviewer's reading).
>

## levels-within-habitat.12 (claim)

Same-habitat comparisons using marker-normalised, unaggregated or all-read functional profiles alongside taxonomy at matched resolution have not been measured, nor have non-human habitats beyond a few microcosm and marine examples; none of the studies controls for normalisation, aggregation and granularity together.

- conf: not stated
- class: search (note: "Not measured")
- holds: function levels against taxonomic composition within a habitat
- src: none (a statement of what was not measured)
- search: not stated
- trail: H2-01 §answers

From the note:

> H2-01:A-062 [quote: Answers as delivered] Several independent studies agree, but none controls for normalisation, aggregation and granularity together..
>
> H2-01:A-064 [quote: Answers as delivered] *Not measured:* Same-habitat comparisons using marker-normalised, unaggregated or all-read functional profiles alongside taxonomy at matched resolution; non-human habitats beyond a few microcosm and marine examples..
>

## levels-across-habitats.1 (claim)

Across habitats where taxonomy turns over, whether function tracks taxonomic composition is contested and incommensurable: the coupled and decoupled results use different function definitions (all reads or gene categories against taxonomy-derived groups) and different comparisons (distance-matrix correlation against variance partitioning), and cannot be pooled; the answer depends on annotation and resolution.

- conf: cont (critic: C-028)
- class: not stated
- holds: several measured studies in each direction, not commensurable, several single studies or abstract only
- src: fiererCrossbiomeMetagenomicAnalyses2012, salazarGeneExpressionChanges2019, loucaDecouplingFunctionTaxonomy2016, nelsonGlobalBiogeographyMicrobial2016
- rating: "Weak to moderate"
- trail: H2-01 §4.2, §answers, §6. Answers, §critic

From the note:

> H2-01:B-0141 [4.2 Function levels against taxonomic composition, across habitats where taxonomy turns over] Here the direction is contested.
>
> H2-01:B-0149 [4.2 Function levels against taxonomic composition, across habitats where taxonomy turns over] Reviewer's reading: "coupled" and "decoupled" results use different function definitions (all reads or gene categories against taxonomy-derived groups) and different comparisons (distance-matrix correlation against variance partitioning), and cannot be pooled.
>
> H2-01:A-069 [quote: Answers as delivered] **D3 case B: function levels against taxonomic composition, across habitats where taxonomy turns over; and case C: habitat changes while taxonomy does not**: Case B is contested.
>
> H2-01:A-073 [quote: Answers as delivered] The coupled and decoupled results use different function definitions and different statistics and cannot be pooled.
>
> H2-01:A-075 [quote: Answers as delivered] *Strength:* Weak to moderate.
>
> H2-01:A-076 [quote: Answers as delivered] Case B has several measured studies in each direction, but they are not commensurable and several are single studies or abstract only.
>
> H2-01:A-078 [quote: Answers as delivered] *Conflicts:* Fierer2012 and Salazar2019 (coupled) against Louca2016a and Nelson2016 (decoupled).
>
> H2-01:A-114 [6. Answers by direction] Across habitats: contested, dependent on annotation and resolution.
>
> H2-01:C-028 [danger: Critic: answers partly supported] - **D3 case B/C (levels vs composition across habitats; taxonomy fixed)**: Case B is contested and incommensurable, as stated.
>

## levels-across-habitats.2 (claim)

Across 16 soils from five biomes, functional and taxonomic Bray-Curtis distances correlated (Mantel r = 0.76; with unweighted UniFrac, 0.82).

- conf: not stated
- class: meas (marker)
- holds: 16 soils from five biomes; small n; the coupled side of case B, which without this study would rest on one global ocean statement
- src: fiererCrossbiomeMetagenomicAnalyses2012 (FT per trait-ecology angle; measured; small n)
- limit: access (critic: C-061)
- trail: H2-01 §4.2, §answers, §critic, §Adversarial, §Provenance

From the note:

> H2-01:I-0031 [4.2 Function levels against taxonomic composition, across habitats where taxonomy turns over] - Coupled: across 16 soils from five biomes, functional and taxonomic Bray-Curtis distances correlated (Mantel r = 0.76; with unweighted UniFrac, 0.82) [Fierer2012; FT per trait-ecology angle; measured; small n].
>
> H2-01:A-070 [quote: Answers as delivered] Coupling: functional and taxonomic beta diversity correlated across five soil biomes (Mantel r 0.76 to 0.82, n = 16) [Fierer2012], and in the global ocean taxonomic composition 'largely shapes' gene functional content [Salazar2019].
>
> H2-01:A-086 [quote: Answers as delivered] Removing Fierer2012 would leave the coupled side resting on Salazar2019's global statement..
>
> H2-01:C-032 [danger: Critic: answers partly supported] The coupled side's key figures (Fierer2012 Mantel r) were read in full text by only one angle and were not re-checked.
>
> H2-01:C-061 [warning: Adversarial critique, full findings] - Fierer2012's Mantel r of 0.76 and 0.82 are load-bearing for the coupled side of D3 case B. They were read in full text by one search angle only, other angles had the abstract, and the reviewer did not re-open the paper. The efetch of PMC3535587 returned no body text.
>
> H2-01:B-0016 [info: Provenance] Nelson2016 and Fierer2012 PMC E-utilities returns contained only the abstract; their full-text labels rest on the search angles' reading.
>

## levels-across-habitats.3 (claim)

In Tara Oceans, OG-level metagenomic and metatranscriptomic differentiation tracked taxonomic differentiation along latitude, and the authors conclude that "on a global scale, taxonomic composition largely shapes the composition of gene functional content".

- conf: not stated
- class: meas (marker)
- holds: global ocean (Tara Oceans); the critic: taxonomic and OG profiles come from the same reads and share compositional structure, which the review does not note
- src: salazarGeneExpressionChanges2019 (FT; measured)
- contrary: one-sided (critic: C-125)
- trail: H2-01 §4.2, §answers, §Adversarial

From the note:

> H2-01:I-0032 [4.2 Function levels against taxonomic composition, across habitats where taxonomy turns over] In Tara Oceans, OG-level metagenomic and metatranscriptomic differentiation tracked taxonomic differentiation along latitude, and the authors conclude that "on a global scale, taxonomic composition largely shapes the composition of gene functional content" [Salazar2019; FT; measured].
>
> H2-01:A-070 [quote: Answers as delivered] Coupling: functional and taxonomic beta diversity correlated across five soil biomes (Mantel r 0.76 to 0.82, n = 16) [Fierer2012], and in the global ocean taxonomic composition 'largely shapes' gene functional content [Salazar2019].
>
> H2-01:C-125 [warning: Adversarial critique, full findings] - D3 case B: small n is flagged for Fierer2012 (n = 16), but Salazar2019's 'largely shapes' conclusion is taken at the authors' word. There is no note that taxonomic and OG profiles come from the same reads and share compositional structure, a caution the review applies to functional profiles elsewhere.
>

## levels-across-habitats.4 (claim)

A CCA on phylogenetic composition agreed with functional trends across GOS.

- conf: not stated
- class: not stated
- holds: GOS ocean metagenomes
- src: raesTowardMolecularTraitbased2011 (FT)
- trail: H2-01 §4.2

From the note:

> H2-01:B-0142 [4.2 Function levels against taxonomic composition, across habitats where taxonomy turns over] A CCA on phylogenetic composition agreed with functional trends across GOS [Raes2011; FT].
>

Not found in the cited text (where to look, not what is wrong): holds: ocean

## levels-across-habitats.5 (claim)

Across 247 metagenomes from 18 biomes, function separated biomes more strongly than taxonomy: oxidoreductase profiles gave PERMANOVA F = 12.5 and all 6,789 KOs F = 10.7, against 1.8 for 4,011 species and 2.8 at fourth taxonomic rank, and functional and taxonomic diversity rankings of biomes did not correspond; the feature sets differ in size and sparsity, so the F statistics are not commensurable.

- conf: single (marker)
- class: meas (marker)
- holds: 247 metagenomes from 18 biomes; bears on which separates habitats more, a different question from coupling
- src: ramirezflandesRedoxTraitsCharacterize2019 (FT; measured; SINGLE SOURCE)
- trail: H2-01 §4.2, §answers

From the note:

> H2-01:B-0143 [4.2 Function levels against taxonomic composition, across habitats where taxonomy turns over] - Function separates habitats more than taxonomy: across 247 metagenomes from 18 biomes, oxidoreductase profiles gave PERMANOVA F = 12.5 and all 6,789 KOs F = 10.7, against 1.8 for 4,011 species and 2.8 at fourth taxonomic rank.
>
> H2-01:I-0033 [4.2 Function levels against taxonomic composition, across habitats where taxonomy turns over] Functional and taxonomic diversity rankings of biomes did not correspond [RamirezFlandes2019; FT; measured; SINGLE SOURCE].
>
> H2-01:B-0144 [4.2 Function levels against taxonomic composition, across habitats where taxonomy turns over] The feature sets differ in size and sparsity, so the F statistics are not commensurable.
>
> H2-01:A-071 [quote: Answers as delivered] Function separates biomes more strongly than taxonomy (PERMANOVA F 10.7 to 12.5 for functions against 1.8 to 2.8 for taxonomy across 18 biomes) [RamirezFlandes2019], but the feature sets differ in size and sparsity.
>
> H2-01:A-079 [quote: Answers as delivered] RamirezFlandes2019 bears on which separates habitats more, a different question from coupling..
>

## levels-across-habitats.6 (claim)

Nine biomes were strongly discriminated by metabolic profiles.

- conf: not stated
- class: not stated
- holds: metagenomes from nine biomes
- src: dinsdaleFunctionalMetagenomicProfiling2008 (AB)
- trail: H2-01 §4.2

From the note:

> H2-01:B-0145 [4.2 Function levels against taxonomic composition, across habitats where taxonomy turns over] Nine biomes were strongly discriminated by metabolic profiles [Dinsdale2008; AB].
>

## levels-across-habitats.7 (claim)

In the global ocean, environment strongly shaped functional-group distribution and weakly shaped taxonomy within groups, "roughly independent axes of variation".

- conf: not stated
- class: deriv (marker)
- holds: global ocean; derived, because functional groups were assigned from taxonomy; one of the two studies on the decoupled side of case B
- src: loucaDecouplingFunctionTaxonomy2016 (AB; derived, because functional groups were assigned from taxonomy)
- trail: H2-01 §4.2, §answers, §critic

From the note:

> H2-01:I-0034 [4.2 Function levels against taxonomic composition, across habitats where taxonomy turns over] - Decoupled: in the global ocean, environment strongly shaped functional-group distribution and weakly shaped taxonomy within groups, "roughly independent axes of variation" [Louca2016a; AB; derived, because functional groups were assigned from taxonomy].
>
> H2-01:I-0001 [quote: Answers as delivered] Decoupling: in the ocean, environment shapes functional-group distribution while taxonomy within groups varies independently [Louca2016a, abstract, derived from taxonomy]; soil N-pathway frequencies follow habitat and soil chemistry while taxonomy within N groups is poorly predicted [Nelson2016].
>
> H2-01:A-085 [quote: Answers as delivered] *Single-source sensitivity:* Removing Louca2016a (abstract only, derived) would leave the decoupled side resting on Nelson2016 alone.
>
> H2-01:C-030 [danger: Critic: answers partly supported] The decoupled side rests on Louca2016a (abstract only, taxonomy-derived function) and Nelson2016, which was read only through an automated summary with figures not re-verified.
>

## levels-across-habitats.8 (claim)

Soil nitrogen-pathway frequencies were explained by habitat and soil C and N, while taxonomy within N functional groups was poorly predicted by environment.

- conf: not stated
- class: not stated
- holds: soils; one of the two studies on the decoupled side of case B
- src: nelsonGlobalBiogeographyMicrobial2016 (SEC/unverified; critic: C-059 was "FT via an automated summary; figures not re-verified")
- limit: access (critic: C-058)
- trail: H2-01 §4.2, §answers, §critic, §Adversarial

From the note:

> H2-01:B-0146 [4.2 Function levels against taxonomic composition, across habitats where taxonomy turns over] Soil nitrogen-pathway frequencies were explained by habitat and soil C and N, while taxonomy within N functional groups was poorly predicted by environment [Nelson2016; FT via an automated summary; figures not re-verified].
>
> H2-01:I-0001 [quote: Answers as delivered] Decoupling: in the ocean, environment shapes functional-group distribution while taxonomy within groups varies independently [Louca2016a, abstract, derived from taxonomy]; soil N-pathway frequencies follow habitat and soil chemistry while taxonomy within N groups is poorly predicted [Nelson2016].
>
> H2-01:C-029 [danger: Critic: answers partly supported] The access labelling needs correcting.
>
> H2-01:C-030 [danger: Critic: answers partly supported] The decoupled side rests on Louca2016a (abstract only, taxonomy-derived function) and Nelson2016, which was read only through an automated summary with figures not re-verified.
>
> H2-01:C-031 [danger: Critic: answers partly supported] That is not full-text access, yet the answer lists it under 'Full text'.
>
> H2-01:C-056 [warning: Adversarial critique, full findings] - Nelson2016 is listed under 'Full text' in the D3 case B access_basis.
>
> H2-01:C-057 [warning: Adversarial critique, full findings] The reference list says 'FT via automated summary of the PMC page; figures not re-verified'.
>
> H2-01:C-058 [warning: Adversarial critique, full findings] A machine summary is not a full-text reading, and this source carries the decoupled side of case B (the answer says removing Louca2016a would leave that side resting on Nelson2016 alone).
>
> H2-01:C-059 [warning: Adversarial critique, full findings] It should be labelled SECONDARY/unverified.
>
> H2-01:C-060 [warning: Adversarial critique, full findings] I could not reach PMC4961168 full text via NCBI efetch (only a header was returned).
>
> H2-01:C-058 [warning: Adversarial critique, full findings] A machine summary is not a full-text reading, and this source carries the decoupled side of case B (the answer says removing Louca2016a would leave that side resting on Nelson2016 alone).
>
> H2-01:C-059 [warning: Adversarial critique, full findings] It should be labelled SECONDARY/unverified.
>

## levels-across-habitats.9 (claim)

At 95%-identity gene resolution, most genes were specific to one of 14 habitats.

- conf: not stated
- class: not stated
- holds: prokaryotic genes at 95% identity across 14 habitats
- src: coelhoTowardsBiogeographyProkaryotic2021 (AB)
- trail: H2-01 §4.2

From the note:

> H2-01:R-0103 [Reference list] Towards the biogeography of prokaryotic genes.
>
> H2-01:B-0147 [4.2 Function levels against taxonomic composition, across habitats where taxonomy turns over] - Resolution: at 95%-identity gene resolution, most genes were specific to one of 14 habitats [Coelho2022; AB]; at the level of core OG functions, more than 73% of ocean core-function abundance was shared with the human gut [Sunagawa2015; AB].
>

## levels-across-habitats.10 (claim)

At the level of core OG functions, more than 73% of ocean core-function abundance was shared with the human gut.

- conf: not stated
- class: not stated
- holds: ocean and human gut metagenomes
- src: sunagawaStructureFunctionGlobal2015 (AB)
- trail: H2-01 §4.2

From the note:

> H2-01:B-0147 [4.2 Function levels against taxonomic composition, across habitats where taxonomy turns over] - Resolution: at 95%-identity gene resolution, most genes were specific to one of 14 habitats [Coelho2022; AB]; at the level of core OG functions, more than 73% of ocean core-function abundance was shared with the human gut [Sunagawa2015; AB].
>

## levels-across-habitats.11 (claim)

Resolution decides much of the coupling question: the same data can support turnover or constancy depending on resolution.

- conf: not stated
- class: not stated
- holds: comparisons of function and taxonomy across habitats
- src: coelhoTowardsBiogeographyProkaryotic2021, sunagawaStructureFunctionGlobal2015
- trail: H2-01 §4.2, §answers

From the note:

> H2-01:B-0148 [4.2 Function levels against taxonomic composition, across habitats where taxonomy turns over] The same data can support turnover or constancy depending on resolution.
>
> H2-01:A-072 [quote: Answers as delivered] Resolution decides much of this: most 95%-identity genes are habitat-specific [Coelho2022, abstract], while more than 73% of ocean core-function abundance is shared with human gut [Sunagawa2015, abstract].
>

## levels-across-habitats.12 (claim)

Case B has not been measured with taxonomy and function at matched resolution and matched feature counts, or with marker-normalised functional profiles.

- conf: not stated
- class: search (note: "Not measured")
- holds: function levels against taxonomic composition across habitats
- src: none (a statement of what was not measured)
- search: not stated
- trail: H2-01 §answers

From the note:

> H2-01:A-080 [quote: Answers as delivered] *Not measured:* Case C entirely.
>
> H2-01:A-081 [quote: Answers as delivered] Case B with taxonomy and function at matched resolution and matched feature counts.
>
> H2-01:A-082 [quote: Answers as delivered] Case B with marker-normalised functional profiles..
>

## taxonomy-fixed.1 (claim)

No microbial metagenomic study was found that holds taxonomy fixed while habitat varies and compares function levels.

- conf: not stated
- class: search (note: "Not found by these routes")
- holds: the review's search routes; the critic: transplant, common-garden and single-lineage-across-habitat designs are not listed among the routes searched
- src: none (a search result)
- search: searched, not found (note: "Not found by these routes")
- rating: "Case C: absent"
- trail: H2-01 §4.3, §Provenance, §answers, §critic

From the note:

> H2-01:B-0150 [4.3 Function levels against composition, where habitat changes but taxonomy does not] No microbial metagenomic study was found that holds taxonomy fixed while habitat varies and compares function levels.
>
> H2-01:B-0018 [info: Provenance] Not found by these routes: any microbial test withholding a habitat when scoring functional covariation; any microbial cross-habitat comparison of covariation stability against level and composition stability; any microbial study of how dimension estimates change with normalisation, sparsity, presence/absence, overlapping gene sets or sample size; any study holding taxonomy fixed while habitat varies.
>
> H2-01:A-074 [quote: Answers as delivered] Case C: no microbial study found that holds taxonomy fixed while habitat changes and compares function levels.
>
> H2-01:A-077 [quote: Answers as delivered] Case C: absent..
>
> H2-01:A-080 [quote: Answers as delivered] *Not measured:* Case C entirely.
>
> H2-01:C-033 [danger: Critic: answers partly supported] Case C: no microbial study found on the named routes.
>
> H2-01:C-034 [danger: Critic: answers partly supported] Transplant, common-garden and single-lineage-across-habitat designs are not listed among the routes searched.
>

Not found in the cited text (where to look, not what is wrong): holds: review

## taxonomy-fixed.2 (claim)

Salazar et al. (2019) separate regulatory change (metatranscriptome) from community turnover in the ocean; per the search agent's reading, turnover dominated at global scale. This is the nearest item to case C and concerns expression, not gene content.

- conf: not stated
- class: not stated
- holds: global ocean metatranscriptomes
- src: salazarGeneExpressionChanges2019
- trail: H2-01 §4.3

From the note:

> H2-01:B-0151 [4.3 Function levels against composition, where habitat changes but taxonomy does not] Salazar et al. (2019) separate regulatory change (metatranscriptome) from community turnover in the ocean; per the search agent's reading, turnover dominated at global scale.
>
> H2-01:B-0152 [4.3 Function levels against composition, where habitat changes but taxonomy does not] That is the nearest item and concerns expression, not gene content.
>

## covariation-stability.1 (claim)

No microbial study was found that compares the between-habitat stability of function-function covariation with that of function levels or taxonomic composition.

- conf: not stated
- class: search (note: "Not found by these routes")
- holds: microbial metagenomes; search routes as for withheld habitats
- src: none (a search result)
- search: searched, not found (note: "Not found by these routes")
- rating: "Absent for the microbial cross-habitat case"
- trail: H2-01 §1. What, §Provenance, §answers, §6. Answers, §critic

From the note:

> H2-01:B-0038 [1. What the literature covers, and what it does not] No study was found that compared the between-habitat stability of function-function covariation with the stability of function levels and of taxonomic composition in microbial metagenomes.
>
> H2-01:B-0018 [info: Provenance] Not found by these routes: any microbial test withholding a habitat when scoring functional covariation; any microbial cross-habitat comparison of covariation stability against level and composition stability; any microbial study of how dimension estimates change with normalisation, sparsity, presence/absence, overlapping gene sets or sample size; any study holding taxonomy fixed while habitat varies.
>
> H2-01:A-087 [quote: Answers as delivered] **D3 case D: covariation among functions against function levels and taxonomic composition, across habitats (including temporal stability of covariation)**: No microbial study was found that compares the between-habitat stability of function-function covariation with that of function levels or taxonomic composition (search routes as for D2).
>
> H2-01:A-094 [quote: Answers as delivered] *Strength:* Absent for the microbial cross-habitat case.
>
> H2-01:A-099 [quote: Answers as delivered] *Not measured:* Microbial cross-habitat comparison of covariation stability against level stability and composition stability; the case where taxonomy does not turn over; covariation in presence/absence profiles; comparison corrected for shared gene-set members..
>
> H2-01:A-117 [6. Answers by direction] No microbial cross-habitat comparison was found.
>
> H2-01:C-035 [danger: Critic: answers partly supported] - **D3 case D (covariation vs levels and composition)**: No microbial cross-habitat comparison was found.
>

## covariation-stability.2 (claim)

Across four human gut cohorts that differ in disease state and population (IBD, obesity, two population cohorts), 64.3% of pathway co-abundances and 38.6% of species co-abundances differed in strength (Cochran's Q, FDR < 0.05): in this setting pathway covariation was less stable across cohorts than species covariation. This compares functional covariation with taxonomic covariation, not with taxonomic composition, and the cohorts differ in disease state and population, not habitat.

- conf: single (critic: C-080)
- class: not stated
- holds: one human gut study, one heterogeneity test; the closest microbial evidence and the only microbial measurement of functional covariation stability; shared-member and common-factor cautions apply; the critic: heterogeneity tests have more power for stronger and more numerous correlations, and pathway correlations are stronger and more numerous, so easier to detect as heterogeneous
- src: chenGutMicrobialCoabundance2020 (FT, re-checked)
- rating: "Weak (one study) for the microbial between-cohort case"
- contrary: one-sided (critic: C-116)
- trail: H2-01 §4.4, §1. What, §answers, §6. Answers, §critic, §Adversarial

From the note:

> H2-01:B-0039 [1. What the literature covers, and what it does not] The closest microbial evidence is a between-cohort, single-habitat (human gut) study [Chen2020].
>
> H2-01:B-0153 [4.4 Covariation among functions against levels and composition] **Microbial, direct but single-habitat.** In four human gut cohorts, 64.3% of pathway co-abundances varied significantly in strength between cohorts, against 38.6% of species co-abundances [Chen2020; FT, re-checked].
>
> H2-01:B-0155 [4.4 Covariation among functions against levels and composition] So in this setting pathway covariation was *less* stable across cohorts than species covariation, and variable covariation usually co-occurred with variable levels.
>
> H2-01:B-0156 [4.4 Covariation among functions against levels and composition] This compares functional covariation with *taxonomic covariation*, not with taxonomic composition itself.
>
> H2-01:B-0157 [4.4 Covariation among functions against levels and composition] The cohorts differ by disease state, not habitat.
>
> H2-01:B-0158 [4.4 Covariation among functions against levels and composition] Shared-member and common-factor cautions apply (Section 3.2).
>
> H2-01:A-088 [quote: Answers as delivered] The closest microbial evidence is single-habitat: across four human gut cohorts differing in disease state, 64.3% of pathway co-abundances varied in strength against 38.6% of species co-abundances, and 84% of pathways in variable co-abundances also differed in level [Chen2020].
>
> H2-01:A-089 [quote: Answers as delivered] In that setting functional covariation was less stable than taxonomic covariation (not composition itself), and changes in covariation usually came with changes in levels.
>
> H2-01:A-095 [quote: Answers as delivered] Weak (one study) for the microbial between-cohort case.
>
> H2-01:A-102 [quote: Answers as delivered] Removing Chen2020 leaves no microbial measurement of functional covariation stability at all.
>
> H2-01:A-115 [6. Answers by direction] Covariation versus the others: one microbial single-habitat study found pathway covariation less stable than species covariation and linked to level differences.
>
> H2-01:C-036 [danger: Critic: answers partly supported] In one human gut study (Chen2020, verified), 64.3% of pathway co-abundances and 38.6% of species co-abundances differed in strength across four cohorts (Cochran's Q, FDR < 0.05).
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
> H2-01:C-080 [warning: Adversarial critique, full findings] One study, one habitat, one heterogeneity test.
>

## covariation-stability.3 (claim)

Among the entities involved in variable co-abundances across the four gut cohorts, 84% of 304 pathways and also 76% of 100 species differed in level; the review reported only the pathway figure, which makes the pathway result look more distinctive than it is.

- conf: not stated
- class: not stated
- holds: four human gut cohorts differing in disease state
- src: chenGutMicrobialCoabundance2020 (FT, re-checked)
- contrary: one-sided (critic: C-118)
- trail: H2-01 §4.4, §answers, §critic, §Adversarial

From the note:

> H2-01:B-0154 [4.4 Covariation among functions against levels and composition] Of the 304 pathways involved in variable co-abundances, 84% also differed in abundance level between cohorts.
>
> H2-01:A-088 [quote: Answers as delivered] The closest microbial evidence is single-habitat: across four human gut cohorts differing in disease state, 64.3% of pathway co-abundances varied in strength against 38.6% of species co-abundances, and 84% of pathways in variable co-abundances also differed in level [Chen2020].
>
> H2-01:A-089 [quote: Answers as delivered] In that setting functional covariation was less stable than taxonomic covariation (not composition itself), and changes in covariation usually came with changes in levels.
>
> H2-01:C-037 [danger: Critic: answers partly supported] Among the entities involved in variable co-abundances, 84% of 304 pathways and also 76% of 100 species differed in level.
>
> H2-01:C-038 [danger: Critic: answers partly supported] The review reports only the pathway figure.
>
> H2-01:C-055 [danger: Critic: answers partly supported] (4) The D3 case D reading of Chen2020 omits the matching species result (76% level differences) and applies the lenient-threshold and power caution to replication but not to the between-cohort variability comparison or the temporal-stability figure.
>
> H2-01:C-118 [warning: Adversarial critique, full findings] - Chen2020 levels-covariation link: the review reports that 84% of 304 pathways in variable co-abundances also differed in level. It omits the matching full-text figure that 76% of 100 species also did, so the pathway result looks more distinctive than it is.
>

## covariation-stability.4 (claim)

Outside that study, covariation among microbial functions has only been fitted on pooled cross-habitat data, not compared between habitats; none of the pooled studies measures whether the covariation differs by habitat.

- conf: not stated
- class: not stated
- holds: microbial functional covariation
- src: nelsonGlobalBiogeographyMicrobial2016, salazarGeneExpressionChanges2019, gianoulisQuantifyingEnvironmentalAdaptation2009, barberanExplorationCommunityTraits2011
- trail: H2-01 §4.4, §answers

From the note:

> H2-01:B-0160 [4.4 Covariation among functions against levels and composition] **Microbial, pooled only.** Covariation among functions has otherwise been fitted on pooled cross-habitat data, not compared between habitats: N-pathway frequencies "overwhelmingly positively correlated" across 365 soils from 10 habitat types [Nelson2016]; co-abundance and co-expression of ocean OGs predicting shared KEGG membership [Salazar2019; fitted and scored on the same samples; partly circular]; covariation of amino-acid transport and cofactor synthesis in GOS [Gianoulis2009; AB]; covariation among community genomic traits, some possibly technical in origin [Barberan2012; AB].
>
> H2-01:B-0161 [4.4 Covariation among functions against levels and composition] None of these measures whether the covariation differs by habitat.
>
> H2-01:A-091 [quote: Answers as delivered] Elsewhere functional covariation has only been fitted on pooled cross-habitat data [Nelson2016; Salazar2019; Gianoulis2009].
>

## covariation-stability.5 (claim)

Soil nitrogen-pathway frequencies were "overwhelmingly positively correlated" across 365 soils from 10 habitat types.

- conf: not stated
- class: not stated
- holds: 365 soils from 10 habitat types, pooled
- src: nelsonGlobalBiogeographyMicrobial2016
- trail: H2-01 §4.4

From the note:

> H2-01:B-0160 [4.4 Covariation among functions against levels and composition] **Microbial, pooled only.** Covariation among functions has otherwise been fitted on pooled cross-habitat data, not compared between habitats: N-pathway frequencies "overwhelmingly positively correlated" across 365 soils from 10 habitat types [Nelson2016]; co-abundance and co-expression of ocean OGs predicting shared KEGG membership [Salazar2019; fitted and scored on the same samples; partly circular]; covariation of amino-acid transport and cofactor synthesis in GOS [Gianoulis2009; AB]; covariation among community genomic traits, some possibly technical in origin [Barberan2012; AB].
>

## covariation-stability.6 (claim)

Co-abundance and co-expression of ocean OGs predicted shared KEGG membership, fitted and scored on the same samples and partly circular.

- conf: not stated
- class: not stated
- holds: global ocean, pooled; fitted and scored on the same samples
- src: salazarGeneExpressionChanges2019 (fitted and scored on the same samples; partly circular)
- trail: H2-01 §4.4

From the note:

> H2-01:R-0216 [Reference list] Gene expression changes and community turnover differentially shape the global ocean metatranscriptome.
>
> H2-01:B-0160 [4.4 Covariation among functions against levels and composition] **Microbial, pooled only.** Covariation among functions has otherwise been fitted on pooled cross-habitat data, not compared between habitats: N-pathway frequencies "overwhelmingly positively correlated" across 365 soils from 10 habitat types [Nelson2016]; co-abundance and co-expression of ocean OGs predicting shared KEGG membership [Salazar2019; fitted and scored on the same samples; partly circular]; covariation of amino-acid transport and cofactor synthesis in GOS [Gianoulis2009; AB]; covariation among community genomic traits, some possibly technical in origin [Barberan2012; AB].
>

## covariation-stability.7 (claim)

Amino-acid transport and cofactor synthesis covaried in GOS metagenomes.

- conf: not stated
- class: not stated
- holds: GOS ocean metagenomes, pooled
- src: gianoulisQuantifyingEnvironmentalAdaptation2009 (AB)
- trail: H2-01 §4.4

From the note:

> H2-01:B-0160 [4.4 Covariation among functions against levels and composition] **Microbial, pooled only.** Covariation among functions has otherwise been fitted on pooled cross-habitat data, not compared between habitats: N-pathway frequencies "overwhelmingly positively correlated" across 365 soils from 10 habitat types [Nelson2016]; co-abundance and co-expression of ocean OGs predicting shared KEGG membership [Salazar2019; fitted and scored on the same samples; partly circular]; covariation of amino-acid transport and cofactor synthesis in GOS [Gianoulis2009; AB]; covariation among community genomic traits, some possibly technical in origin [Barberan2012; AB].
>

## covariation-stability.8 (claim)

Community genomic traits covaried in microbial metagenomes, some of the covariation possibly technical in origin.

- conf: not stated
- class: not stated
- holds: microbial metagenomes, pooled
- src: barberanExplorationCommunityTraits2011 (AB)
- trail: H2-01 §4.4

From the note:

> H2-01:B-0160 [4.4 Covariation among functions against levels and composition] **Microbial, pooled only.** Covariation among functions has otherwise been fitted on pooled cross-habitat data, not compared between habitats: N-pathway frequencies "overwhelmingly positively correlated" across 365 soils from 10 habitat types [Nelson2016]; co-abundance and co-expression of ocean OGs predicting shared KEGG membership [Salazar2019; fitted and scored on the same samples; partly circular]; covariation of amino-acid transport and cofactor synthesis in GOS [Gianoulis2009; AB]; covariation among community genomic traits, some possibly technical in origin [Barberan2012; AB].
>

## covariation-stability.9 (claim)

Community-weighted plant traits across 1.1 million plots showed the same two covariation axes as species-level traits, "unexpected" per the authors, while climate and soil explained only 10.8 to 14.0% of CWM variation: covariation more stable than levels.

- conf: single (marker)
- class: meas (marker)
- holds: plant communities (other field); the only large-scale case of covariation more stable than levels
- src: bruelheideGlobalTraitenvironmentRelationships2018 (FT; measured; SINGLE SOURCE)
- trail: H2-01 §4.4, §answers, §Adversarial

From the note:

> H2-01:B-0162 [4.4 Covariation among functions against levels and composition] **Plant traits (other field, both directions).**
>
> H2-01:I-0035 [4.4 Covariation among functions against levels and composition] - Covariation more stable than levels: community-weighted plant traits across 1.1 million plots showed the same two covariation axes as species-level traits, "unexpected" per the authors, while climate and soil explained only 10.8 to 14.0% of CWM variation [Bruelheide2018; FT; measured; SINGLE SOURCE].
>
> H2-01:A-092 [quote: Answers as delivered] In plant traits the evidence runs both ways: CWM covariation axes matched species-level axes worldwide while CWM levels varied under similar environments [Bruelheide2018]; trait networks and bivariate slopes changed with climate [FloresMoreno2019; Wright2005]; and along an aridity gradient a trait covariance changed more systematically than level-type diversity [DwyerLaughlin2017].
>
> H2-01:A-103 [quote: Answers as delivered] Removing Bruelheide2018 removes the only large-scale case of covariation more stable than levels..
>
> H2-01:C-120 [warning: Adversarial critique, full findings] Lenz2016 (higher dimension) and Bruelheide2018 (covariation stable) are flagged.
>

## covariation-stability.10 (claim)

Precision-matrix plant trait networks differed among climate regions in density and modularity, with some edges present everywhere and others region-specific.

- conf: not stated
- class: not stated
- holds: plant traits (other field); heavy imputation
- src: floresmorenoRobustnessTraitConnections2019 (FT; heavy imputation)
- trail: H2-01 §4.4, §answers

From the note:

> H2-01:B-0162 [4.4 Covariation among functions against levels and composition] **Plant traits (other field, both directions).**
>
> H2-01:I-0036 [4.4 Covariation among functions against levels and composition] - Covariation changes with conditions: precision-matrix trait networks differed among climate regions in density and modularity, with some edges present everywhere and others region-specific [FloresMoreno2019; FT; heavy imputation]; leaf-economic slopes shifted with climate [Wright2005; AB]; along an aridity gradient, a height-seed mass covariance strengthened while level-type functional diversity was poorly explained by aridity [DwyerLaughlin2017; AB; SINGLE SOURCE].
>
> H2-01:A-092 [quote: Answers as delivered] In plant traits the evidence runs both ways: CWM covariation axes matched species-level axes worldwide while CWM levels varied under similar environments [Bruelheide2018]; trait networks and bivariate slopes changed with climate [FloresMoreno2019; Wright2005]; and along an aridity gradient a trait covariance changed more systematically than level-type diversity [DwyerLaughlin2017].
>

