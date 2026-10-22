# Faithfulness check: 91 claims

## H2-01/neighbouring-transfer.1

PICRUSt accuracy fell with distance to the nearest reference genome (NSTI), across all samples (r = −0.4) and within each habitat (r = −0.25 to −0.82); accuracy was high in soils (0.87) and low in a hypersaline mat (reported 0.25, mean NSTI 0.23).

- conf: not stated
- class: meas (marker)
- holds: 16S-based prediction of metagenome functions across habitats
- src: langillePredictiveFunctionalProfiling2013 (FT; measured)
- trail: H2-01 §3.3

From the note:

> - **Taxon-to-function mappings transferred across habitats.** PICRUSt accuracy fell with distance to the nearest reference genome (NSTI), across all samples (r = −0.4) and within each habitat (r = −0.25 to −0.82); accuracy was high in soils (0.81) and low in a hypersaline mat (reported 0.25, mean NSTI 0.23) [Langille2013; FT; measured].
>

Not found in the cited text (where to look, not what is wrong): 0.87; holds: 16s-based; holds: metagenome

## H2-01/other-field-transfer.11

In other fields covariation transfers, and each quantitative result is a single study.

- conf: single (critic: H2-01:C-015)
- class: not stated
- holds: transcriptomics; another field from microbial functional profiles
- src: clearyEfficientGenerationTranscriptomic2017 (FT), subramanianNextGenerationConnectivity2017 (FT), piersonSharingSpecificityCoexpression2015 (FT), crowExploitingSinglecellExpression2016 (FT)
- trail: H2-01 §answers, §critic
- rating: "Moderate for partial transfer in transcriptomics"

From the note:

> Other fields: covariation transfers partly.
>
> Moderate for partial transfer in transcriptomics, but that is another field and each quantitative result is a single study..
>
> Other fields show partial transfer, each result from a single study.
>

## H2-01/levels-within.6

During vermicomposting, taxonomic turnover was about ten times functional turnover.

- conf: not stated
- class: not stated
- holds: vermicomposting over time; no non-earthworm control
- src: airaFasterTurnoverTaxonomic2026 (AB; no non-earthworm control)
- trail: H2-01 §4.1

From the note:

> - Vermicomposting over time: taxonomic turnover about twelve times functional turnover [Aira2026; AB; no non-earthworm control].
>

## CB3/n2o.5

Tian et al. 2024: "Agricultural emissions contributed 74% of total anthropogenic emissions in the 2010s, with 56% from direct agricultural emissions and 18% from indirect emissions".

- conf: not stated
- class: not stated
- holds: anthropogenic N2O, 2010s
- src: tianGlobalNitrousOxide2024
- trail: CB3-AG-EMISSIONS §Boundary D

From the note:

> "Agricultural emissions contributed **74%** of total anthropogenic emissions in the 2010s, with 56% from direct agricultural emissions and 18% from indirect emissions" [8].
>

Not found in the cited text (where to look, not what is wrong): holds: n2o

## H1-RES/redundancy.13

Ren et al. (2016): along a heavy-metal contamination gradient, functional and phylogenetic beta-diversities were significantly correlated and many resistance genes derived from specific taxa, linking functional shifts to taxonomic changes.

- conf: not stated
- class: not stated
- holds: a heavy-metal contamination gradient
- src: renComparisonMicrobialTaxonomic2016
- trail: H1-RES §Soil counter-evidence

From the note:

> |  Comparison of microbial taxonomic and functional shift pattern along contamination gradient, Youhua Ren et al., 2016  | Functional and phylogenetic beta-diversities were significantly correlated along a heavy-metal contamination gradient, and many resistance genes derived from specific taxa, linking functional shifts to taxonomic changes in contaminated sites [11].  |
>

## TSL/frequency-bucketing.1

Threshold bucketing is corpus-structure-dependent and unstable under heavy tails: the same 1% relative cutoff produced a 9.3% vocabulary reduction (few long documents) vs 74.1% (many short documents), and cutoffs above 4% can empty a short-text vocabulary.

- conf: repl (marker)
- class: model (note: "simulated-LDA study")
- holds: LDA on simulated corpora; not shown on real corpora or non-LDA pipelines (gap.2)
- src: bystrovAnalysingImpactRemoving2023
- trail: TSL §Verdict, §3. Frequency bucketing, §Open Questions
- rating: "Confidence: high (3-0)"

From the note:

> **Discrete frequency banding is shown to be unstable under heavy tails** — the same relative cutoff produced 9.3% vs 74.1% vocabulary reduction across corpora, and cutoffs >4% can empty a short-text vocabulary [S7].
>
> - **Threshold bucketing is corpus-structure-dependent and unstable** [S7]: same 1% cutoff → 9.3% reduction (few long docs) vs 74.1% (many short docs); >4% empties short-text vocabularies.
>
> *Confidence: high (3-0).*
>
> **Real-corpus replication:** do the bucketing instabilities (9.3% vs 74.1%) and ~30%-removable findings hold on *real* corpora and non-LDA pipelines (e.g. BERTopic c-TF-IDF)?
>
> Primary evidence is one simulated-LDA study.
>

Not found in the cited text (where to look, not what is wrong): holds: gap.2

## H2-01/other-field-transfer.9

Some leaf-trait correlations reverse sign within species compared with across species.

- conf: not stated
- class: not stated
- holds: plant leaf traits, within against across species
- src: andereggWithinspeciesPatternsChallenge2018 (AB)
- trail: H2-01 §3.4

From the note:

> Some leaf-trait correlations reverse sign within species compared with across species [Anderegg2018; AB].
>

Not found in the cited text (where to look, not what is wrong): holds: plant

## H1-RES/accessory-function.1

In *Pseudomonas bharatica* CSV86T, isolated from aromatic-contaminated soil, comparative genomics revealed three genomic islands over 50 kb: ICEnahCSV86 carrying the naphthalene catabolic (nah-sal) cluster, PBGI-1 carrying Co-Zn-Cd (czc) efflux genes, and PBGI-2 as a mixed-function element; ICEnahCSV86 was conjugatively transferred to *Stenotrophomonas maltophilia* CSV89 at a frequency of 7 × 10⁻⁸ per donor cell.

- conf: not stated
- class: not stated
- holds: one strain from aromatic-contaminated soil; one recipient strain
- src: none (cited only as SC2 [2]; the note gives no reference list)
- trail: H1-RES §Sub-claim 2
- rating: "The strongest quantitative link between accessory genetic content and habitat-specific function"

From the note:

> The strongest quantitative link between accessory genetic content and habitat-specific function comes from *Pseudomonas bharatica* CSV86T, isolated from aromatic-contaminated soil.
>
> Comparative genomic analysis revealed three genomic islands exceeding 50 kb: ICEnahCSV86 harboring the naphthalene catabolic (nah-sal) cluster, PBGI-1 carrying Co-Zn-Cd (czc) efflux genes, and PBGI-2 as a mixed-function element [2].
>
> ICEnahCSV86 was conjugatively transferred to *Stenotrophomonas maltophilia* CSV89 at a frequency of 7 × 10⁻⁸ per donor cell, demonstrating both functional relevance and mobility [2].
>

## 16S/abundance-occupancy.14

No soil study was found that tests whether the observed bulk-soil abundance-occupancy relationship exceeds what sampling and detection alone would produce, so the share attributable to biology is unknown; none was found from cell counts or metagenomes, none specific to archaea, none comparing bulk soil and rhizosphere within one study, and none that is copy-number- or ploidy-corrected.

- conf: unclear (note: "the share attributable to biology is unknown")
- class: search (note: "No soil study was found")
- holds: Europe PMC query for abundance-occupancy with soil or rhizosphere and bacteria or archaea (25 hits reviewed by title, mostly core-microbiome applications); Europe PMC query for the neutral community model with bulk soil and rhizosphere
- src: none (a statement about what the search found)
- trail: MB-02 §D3.3, §answers, §critic, §Search record
- rating: "Moderate for its interpretation"

From the note:

> I found no soil study that tests whether the observed bulk-soil abundance-occupancy relationship exceeds a sampling or detection null.
>
> I also found none from cell counts or metagenomes, none specific to archaea, and none comparing bulk and rhizosphere within one study.
>
> No soil study was found that tests whether the observed bulk-soil relationship exceeds what sampling and detection alone would produce.
>
> *Not measured:* Abundance-occupancy relationships in soil from cell counts or from metagenomes (none found); copy-number- or ploidy-corrected soil relationships (none found); explicit sampling or detection null models (for example Poisson or gamma sampling as in [72], or occupancy-detection models) applied to bulk soil (none found); archaea-specific abundance-occupancy relationships in soil (none found); bulk soil versus rhizosphere compared within one study for this relationship (none found).
>
> Neutral and sampling models predict a positive relationship by themselves [72,73], and no soil test against a sampling null was found, so the share attributable to biology is unknown.
>
> No soil test against a sampling null was found.
>
> - **Soil abundance-occupancy tests against sampling nulls**: Europe PMC query for abundance-occupancy with soil or rhizosphere and bacteria or archaea (25 hits reviewed by title, mostly core-microbiome applications); Europe PMC query for the neutral community model with bulk soil and rhizosphere.
>
> Weak for its interpretation, because the main soil evidence does not separate biology from detection, and the sampling-null evidence comes from non-soil data.
>

## H1-02/chimerism.3

CheckM and GUNC contamination estimates correlated at r = 0.2.

- conf: not stated
- class: meas (note: "measured; natural")
- holds: natural MAG catalogues (CheckM-prefiltered human gut catalogues and the multi-habitat GMGC set)
- src: orakovGUNCDetectionChimerism2021
- trail: H1-02 §2.2

From the note:

> CheckM and GUNC contamination estimates correlated at r = 0.2 (measured; natural).
>

Not found in the cited text (where to look, not what is wrong): holds: mag; holds: checkm-prefiltered; holds: human; holds: gut; holds: multi-habitat; holds: gmgc

## TSL/frequency-bucketing.2

The evidence favours continuous scoring: idf, IC and c-TF-IDF weights are all continuous.

- conf: not stated
- class: not stated
- holds: the specificity signals reviewed
- src: none (the reviewer's synthesis)
- trail: TSL §Verdict

From the note:

> **Continuous vs discrete:** the evidence favours **continuous scoring** (idf, IC, c-TF-IDF weights are all continuous).
>

Not found in the cited text (where to look, not what is wrong): holds: reviewed

## GHOST/missingness-degradation.6

At 99% missing on Cora, PaGNN sits at a low ~58%.

- conf: not stated
- class: not stated
- holds: Cora, 99% missing; homophilous + sparse + MCAR, and mostly author-reported
- src: chenLearningAttributeMissingGraphs2022
- rating: "Confidence: high (3-0 / 2-1)"
- trail: GHOST §2. Degradation

From the note:

> - Contrast at 99% missing on Cora: propagation ~78–79% vs **GCNMF 34.54%** — the latter confirmed by two independent papers [R1, R2].
>
> PaGNN sits at ~58% — low, but not the catastrophic collapse of GCNMF [R3].
>
> *Confidence: high (3-0 / 2-1).*
>
> **Caveat carried on every number above:** homophilous + sparse + MCAR, and mostly author-reported.
>

## 16S/rarefying.6

In Weiss 2017, rarefying clustered samples better for presence/absence metrics, and other normalisations were vulnerable.

- conf: repl (marker)
- class: model (marker)
- holds: simulations
- src: weissNormalizationMicrobialDifferential2017 (FT; model; repl)
- trail: MB-01 §5.3

From the note:

> In Weiss 2017, rarefying clustered samples better for presence/absence metrics, and other normalisations were vulnerable below about 1,000 reads per sample (Weiss 2017) [FT; model; repl].
>

Not found in the cited text (where to look, not what is wrong): holds: simulations

## CB1/supply-chain-emissions.2

Converting at 44/12, 36 kg C/t is about 132 kg CO₂ per tonne delivered.

- conf: not stated
- class: deriv (note: "Converting at 44/12")
- holds: the reviewer's conversion of supply-chain-emissions.1
- src: none (the reviewer's conversion)
- trail: CB1-LIMING §3. Energy and transport

From the note:

> Converting at 44/12, 36 kg C/t is about 132 kg CO₂ per tonne delivered.
>

Not found in the cited text (where to look, not what is wrong): holds: supply-chain-emissions.1

## H2-01/neighbouring-transfer.5

Colorectal cancer classifiers on eggNOG groups gave AUROC 0.70 to 0.81 study-to-study and 0.78 to 0.89 leave-one-study-out, similar to species-level classifiers.

- conf: not stated
- class: meas (marker)
- holds: human gut only; a classifier, not a covariance structure
- src: wirbelMetaanalysisFecalMetagenomes2019 (FT; measured)
- trail: H2-01 §3.3

From the note:

> - **Supervised models on functional profiles across studies.** Colorectal cancer classifiers on eggNOG groups gave AUROC 0.70 to 0.81 study-to-study and 0.78 to 0.89 leave-one-study-out, similar to species-level classifiers [Wirbel2019; FT; measured].
>
> Human gut only; a classifier, not a covariance structure.
>
> Neighbouring microbial evidence concerns other quantities: taxon-to-function mappings transfer less well as reference coverage of the target habitat falls [Langille2013; Sun2020]; functional-profile classifiers transfer across studies at AUROC 0.70 to 0.89 in human gut [Wirbel2019]; gene co-occurrence across genomes predicts held-out genomes and held-out phyla, with predictability varying by phylum [Beavan2024; KonnoIwasaki2023].
>

## NFERT/emission-share.4

The full synthetic-N supply chain is larger because it adds field and transport emissions: studies put it at 1.13 Gt CO₂-equivalent for 2018, equal to 10.6% of agricultural emissions and 2.1% of global emissions.

- conf: not stated
- class: not stated
- holds: synthetic-N supply chain, 2018
- src: menegatGreenhouseGasEmissions2022
- trail: NFERT §Share of emissions

From the note:

> The full synthetic-N supply chain is larger because it adds field and transport emissions.
>
> Menegat et al. (2022) estimate 1.13 Gt CO₂-equivalent for 2018, equal to 10.6% of agricultural emissions and 2.1% of global emissions.
>

## H1-06/metabolic-depth.3

Oxygenic photosynthesis had a median tau_D of about 0.10 to 0.11.

- conf: not stated
- class: not stated
- holds: 2,229 SEED genomes, 16S trees; the value rests on search-agent transcription
- src: martinyPhylogeneticConservatismFunctional2013
- trail: H1-06 §3. Part A2, §Provenance, §critic
- limit: access (critic: C-028)

From the note:

> **Ordering by complexity.** On 2,229 SEED genomes (26 phyla, 16S trees), 93% of 89 traits were non-randomly distributed [1].
>
> Oxygenic photosynthesis had a median tau_D of about 0.10 to 0.11 (one clade).
>
> I could not re-open Martiny 2013 (Europe PMC fullTextXML empty) or Goberna and Verdu 2016 (OUP bot challenge), so the specific trait values from Martiny 2013 rest on two independent search-agent readings, and the two agents transcribed its overall tau_D range differently.
>
> - Martiny et al. 2013 [1]: the synthesiser states it could not re-open the paper, yet the A2 ordering values (oxygenic photosynthesis 0.10 to 0.11, sulfate reduction 0.039, N fixation 0.018, Biolog < 0.011) are load-bearing in the A2 verdict and rest on a search agent's transcription that disagrees with another agent on the range. The critic could not obtain it via Europe PMC either (PMC3603392, not OA).
>

## 16S/abundance-distribution.21

Tropical soils are the least-covered communities by Nonpareil estimates.

- conf: not stated
- class: not stated
- holds: qualitative
- src: rodriguezrEstimatingCoverageMetagenomic2014 (FT, qualitative)
- trail: MB-02 §D3.1, §answers

From the note:

> - Tropical soils are among the least-covered communities by Nonpareil estimates [80, FT, qualitative].
>
> Metagenomes: no taxon abundance distribution for soil from metagenomes was found; what was found is that soil metagenomes are far from saturated (80% of about 300 Gbp of Iowa soil reads could not be assembled for low coverage; 48% and 31% of contigs below 10x) [79], soils sit among the least covered communities [80], and 85% of amplicon-defined dominant phylotypes were also dominant in 123 shotgun metagenomes [60].
>

## H1-02/pipeline.3

GUNC-flagged chimerism in real samples varied by binner.

- conf: not stated
- class: not stated
- holds: real samples; the chimerism figures shown are gut datasets (the critic)
- src: kimComprehensiveBenchmarkingMetagenomic2026
- trail: H1-02 §3.1, §critic

From the note:

> Kim et al. [27] found that GUNC-flagged chimerism in real gut, ocean and soil samples varied by binner and "did not correlate with sequencing depth".
>
> The review extends it to 'real gut, ocean and soil samples', but the chimerism figures shown are gut datasets.
>

## 16S/workflow-bias.5

Per-step magnitudes come from one or two small mocks (7 to 20 taxa), often on 454 or Ion Torrent.

- conf: not stated
- class: not stated
- holds: the step-wise evidence in the review
- src: none (the critic's and the review's summary of the mock studies)
- trail: MB-01 §critic, §answers

From the note:

> Per-step magnitudes mostly come from one or two small mocks (7 to 20 taxa), often on 454.
>
> Magnitudes per step are moderate: most come from one or two mocks of 7-20 taxa, often on 454 or Ion Torrent.
>

Not found in the cited text (where to look, not what is wrong): holds: step-wise; holds: in; holds: review

## TAXRES/gtdb-ncbi-divergence.5

Microbiologists still use the older phylum names.

- conf: not stated
- class: not stated
- holds: the older names Firmicutes and Proteobacteria
- src: anonHarmonizingProkaryoticNomenclature2022
- trail: TAXRES §The NCBI-vs-GTDB divergence

From the note:

> Many microbiologists still use the older names.
>
> - The phylum renamings biblion's tags already use (`Firmicutes` to **Bacillota**, `Proteobacteria` to **Pseudomonadota**) were controversial; GTDB made the abrupt switch in R08-RS214 (2023), and **NCBI and LPSN have since adopted the valid names** under nomenclatural requirements, not by coordination.
>

## 16S/contamination.5

Contamination varies inversely with biomass and is specific to the kit and laboratory.

- conf: not stated
- class: not stated
- holds: Salter 2014, Karstens 2019, Minich 2019
- src: salterReagentLaboratoryContamination2014, karstensControllingContaminantsLowbiomass2019, minichQuantifyingUnderstandingWelltowell2019
- trail: MB-01 §answers, §2. Steps

From the note:

> Consistency: varies inversely with biomass and is specific to the kit and laboratory.
>
> Kit- and lab-specific | Salter 2014; Karstens 2019; Minich 2019 |
>

## H1-06/genome-incompleteness.5

Subsampling a complete Pseudomonas aeruginosa genome to 70% moved its functional profile towards Bacillus subtilis.

- conf: not stated
- class: not stated
- holds: one subsampled genome
- src: eisenhoferImpactMicrobialGenome2023
- trail: H1-06 §3. Part A2

From the note:

> Subsampling a complete Pseudomonas aeruginosa genome to 70% moved its functional profile towards Bacillus subtilis.
>

## H2-01/compositional-closure.1

Correlation is not a valid association measure; proportionality is offered instead.

- conf: not stated
- class: not stated
- holds: relative data in general (other field)
- src: lovellProportionalityValidAlternative2015 (AB; other field)
- trail: H2-01 §2.3

From the note:

> - **Compositional closure.** Correlation is not a valid association measure for relative data; proportionality is offered instead [Lovell2015; AB; other field].
>
> What is measured is that these choices change across-sample variance and covariance: marker-gene normalisation raises pathway variability, and uniform mapping of shared KOs and KEGG aggregation lower it [Manor2017]; naive mapping inflates pathway counts [YeDoak2009]; relative data distort correlation [Lovell2015].
>

Not found in the cited text (where to look, not what is wrong): holds: in

## 16S/contamination.1

Contaminant-handling choices are dropping taxa seen in negative controls, decontam (frequency or prevalence mode), SourceTracker, or relative-abundance cutoffs.

- conf: not stated
- class: not stated
- holds: the contaminant studies below
- src: davisSimpleStatisticalIdentification2018, karstensControllingContaminantsLowbiomass2019
- trail: MB-01 §answers

From the note:

> Contaminants: dropping taxa seen in negative controls, decontam (frequency or prevalence mode), SourceTracker, or relative-abundance cutoffs.
>

## 16S/abundance-occupancy.12

The same positive abundance-occupancy observation is read as ecological signal by some authors; the reviewer notes this is a matter of interpretation, not of data.

- conf: not stated
- class: reading (note: "the reviewer notes this is a difference of interpretation")
- holds: neutral-model fits
- src: sloanQuantifyingRolesImmigration2006
- trail: MB-02 §answers

From the note:

> Neutral-model fits imply a positive relationship is expected without selection [73], so the same observation is read as ecological signal by some authors and as near-null by others; the reviewer notes this is a difference of interpretation, not of data.
>

## CB1/dissolution-pathway.5

In Hamilton et al.'s own paired measurements, sink strength tended positive under their no-till treatment.

- conf: not stated
- class: meas (note: "paired measurements")
- holds: Hamilton et al.'s treatments, including no-till
- src: hamiltonEvidenceCarbonSequestration2007
- trail: CB1-LIMING §5. Where the numbers

From the note:

> Their own paired measurements were not one-sided — under their no-till treatment sink strength tended positive, while "on average, liming is neither a consistent source nor a sink for CO₂."
>

Not found in the cited text (where to look, not what is wrong): holds: hamilton

## 16S/primers.12

PCR clamps enrich microbial sequences "without introducing bias".

- conf: not stated
- class: not stated
- holds: abstract only
- src: lundbergPracticalInnovationsHighthroughput2013 (AB; makers' claim)
- trail: MB-01 §2.3

From the note:

> The makers of PCR clamps state that clamps enrich microbial sequences "without introducing bias" (Lundberg 2013) [AB; makers' claim].
>

## H1-RES/pangenome.6

In *E. coli* core genes account for about 50% of total genes, with approximately 146 strain-specific genes per strain.

- conf: not stated
- class: not stated
- holds: *E. coli*
- src: none (cited only as SC1 [29]; the note gives no reference list)
- trail: H1-RES §Confirming Evidence Across

From the note:

> Analysis of 30 *E. coli* genomes found core genes accounted for about 50% of total genes, with approximately 146 strain-specific genes per strain [29].
>

## 16S/quality-filtering.1

Quality filtering and merging choices include quality, length, expected-error and abundance thresholds, plus the delta-Q rule when merging.

- conf: not stated
- class: not stated
- holds: Bokulich 2013 and Kozich 2013
- src: bokulichQualityfilteringVastlyImproves2013, kozichDevelopmentDualindexSequencing2013
- trail: MB-01 §answers

From the note:

> Quality filtering and merging: quality, length, expected-error and abundance thresholds, plus the delta-Q rule when merging (Bokulich 2013; Kozich 2013).
>

## NFERT/haber-bosch.1

Ammonia synthesis runs through the Haber-Bosch process, which fixes atmospheric N₂ with hydrogen at high temperature and pressure; most of the energy and almost all of the carbon enter upstream, when hydrogen is stripped from natural gas or coal by steam reforming.

- conf: not stated
- class: not stated
- holds: ammonia manufacture from natural gas or coal
- src: none (the reviewer's account; no source cited)
- trail: NFERT §Energy per unit

From the note:

> Ammonia synthesis runs through the Haber-Bosch process, which fixes atmospheric N₂ with hydrogen at high temperature and pressure.
>
> Most of the energy and almost all of the carbon enter upstream, when hydrogen is stripped from natural gas or coal by steam reforming.
>

## 16S/ploidy.14

For E. coli, rRNA genes per genome equivalent range from about 7.9 to 9.5 across growth rates.

- conf: not stated
- class: not stated
- holds: E. coli; secondary, Bremer and Dennis (1996) Table 3 as reported by BioNumbers
- src: bremerModulationChemicalComposition1996 (SEC), bionumbersAverageNumberRRNA (SEC)
- trail: MB-02 §D1.3, §answers

From the note:

> For E. coli, rRNA genes per genome equivalent range from about 7.9 to 9.5 across growth rates.
>
> This figure is SECONDARY: Bremer and Dennis (1996), Table 3, as reported by BioNumbers [21].
>
> Because rRNA operons sit near the origin in fast growers [20], 16S copies per cell scale with origin number more than with genome number; E. coli has about 7.9 to 9.5 rRNA genes per genome equivalent across growth rates (secondary, Bremer and Dennis via BioNumbers [21]).
>

## H2-01/direct-dimension.12

Cluster number is not an intrinsic-dimension estimate; the three KO clusters are reported as a precedent.

- conf: not stated
- class: not stated
- holds: Flinkstrom2024
- src: none (the reviewer's statement on Flinkstrom2024)
- trail: H2-01 §2.1

From the note:

> Cluster number is not an intrinsic-dimension estimate, and it is reported here as a nearest precedent only.
>
> Across 6,539 metagenomes, KO profiles formed three clusters [Flinkstrom2024], which is not a dimension estimate.
>

## 16S/technical-variation.10

Batch-correction tools exist, and they work.

- conf: not stated
- class: not stated
- holds: abstracts only
- src: gibbonsCorrectingBatchEffects2018 (AB), lingBatchEffectsRemoval2022 (AB)
- trail: MB-01 §4.3

From the note:

> - Batch-correction tools exist; their makers claim they work (Gibbons 2018; Ling 2022) [AB].
>

## H2-01/gene-set-aggregation.1

Single-copy-gene normalisation raised pathway coefficients of variation relative to relative normalisation.

- conf: single (note: "SINGLE SOURCE for this set of quantities")
- class: not stated
- holds: KEGG pathways
- src: manorRevisedComputationalMetagenomic2017 (FT, re-checked by the reviewer)
- trail: H2-01 §2.3

From the note:

> - **Aggregation into gene sets that share members.** I re-checked Manor and Borenstein (2017) [FT].
>
> In HMP gut samples, single-copy-gene normalisation raised pathway coefficients of variation relative to relative normalisation.
>
> The authors conclude that reported functional uniformity is partly a processing artefact [SINGLE SOURCE for this set of quantities].
>
> What is measured is that these choices change across-sample variance and covariance: marker-gene normalisation raises pathway variability, and uniform mapping of shared KOs and KEGG aggregation lower it [Manor2017]; naive mapping inflates pathway counts [YeDoak2009]; relative data distort correlation [Lovell2015].
>

## H2-04/complementarity-overlap.12

Costless metabolic secretions create broad cross-feeding opportunities.

- conf: not stated
- class: model (marker)
- holds: models
- src: pachecoCostlessMetabolicSecretions2019 (AB; modelled)
- trail: H2-04 §Complementarity versus overlap

From the note:

> Pairwise models predict cooperative potential peaks at moderate overlap [10c, AB; modelled], and costless secretions create broad cross-feeding opportunities [24d, AB; modelled].
>

## H1-RES/accessory-function.19

Among nine *Vibrio alginolyticus* isolates from the Kiel-Fjord, approximately 90% of genomic variation was encoded on MGEs, poorly characterised, and proteins involved in horizontal gene transfer (transposases, integrases, transferases, recombinases) were extensively represented in the accessory genome.

- conf: not stated
- class: not stated
- holds: nine isolates from one fjord
- src: none (cited only as SC2 [23]; the note gives no reference list)
- trail: H1-RES §Counter-Evidence: Accessory, §Assessment: Context

From the note:

> Analysis of *Vibrio alginolyticus* isolates from the Kiel-Fjord revealed that approximately 90% of genomic variation among nine isolates was encoded on MGEs [23].
>
> Proteins involved in horizontal gene transfer (transposases, integrases, transferases, recombinases) were extensively represented in the accessory genome [23].
>
> In *V. alginolyticus*, ~90% of variation was on MGEs but poorly characterized [23].
>

## H1-06/moisture-preference.1

In 23 bacterial and 22 fungal soil isolates respired across a manipulated water-potential gradient, phylum level held 52% of the variance in optimum water potential and 58% in niche breadth.

- conf: single (note: "SINGLE SOURCE")
- class: meas (note: "measured, engineered")
- holds: lab isolates (engineered); niche parameters partitioned across seven RDP ranks against permutation nulls
- src: lennonMappingNicheSpace2012 (measured, engineered)
- trail: H1-06 §2. Part A1, §answers

From the note:

> **Moisture, engineered.** Lennon et al. 2012 [14] (measured, engineered) respired 23 bacterial and 22 fungal soil isolates across a manipulated water-potential gradient and partitioned niche parameters across seven RDP ranks against permutation nulls.
>
> Phylum level held 52% of the variance in optimum water potential and 58% in niche breadth, and strain level held 21 to 29% against 58 to 65% expected by chance.
>
> SINGLE SOURCE.
>
> The coarse-rank result for moisture (52 to 58% of variance at phylum, RDP taxonomy) is engineered (lab isolates, n = 23 bacteria), as is the salinity clustering (reciprocal transplant, Greengenes).
>

## 16S/ploidy.1

In cultures, genome copies per cell range from about one (Caulobacter, Wolinella, crenarchaea) to tens or hundreds (P. putida, haloarchaea, methanogens, Synechocystis) and depend on taxon, growth rate and phase; copy number does not change in one direction with growth phase.

- conf: not stated
- class: not stated
- holds: cultures; apart from Pecoraro 2011 the evidence rests largely on abstracts and on one laboratory's qPCR method
- src: pecoraroQuantificationPloidyProteobacteria2011 (FT), hildenbrandGenomeCopyNumbers2011 (AB), breuertRegulatedPolyploidyHalophilic2006 (AB), griesePloidyCyanobacteria2011 (AB), zerullaPloidyLevelSynechocystis2016 (AB)
- trail: MB-02 §D1.3, §answers, §critic
- rating: "Evidence is moderate, not strong"

From the note:

> **D1 (b) genome and 16S copies per cell**: In cultures, genome copies per cell range from about one (Caulobacter, Wolinella, crenarchaea) to tens or hundreds (P. putida, haloarchaea, methanogens, Synechocystis), and depend on growth rate and phase.
>
> Copy number does not change in one direction with growth phase.
>
> Evidence is moderate, not strong: apart from Pecoraro 2011 it rests largely on abstracts and on one laboratory's qPCR method.
>
> **D1, case (b): genome copies, and hence 16S copies, per cell (cultures and environmental samples)**: In cultures, genome copies per cell range from about one to several hundred and depend on taxon and growth state.
>
> **D1 (b), copies per cell.** In culture, genome copies per cell run from one (Caulobacter, Wolinella, crenarchaea) through merodiploid and oligoploid states that depend on growth rate (E. coli, Bacillus, Synechococcus) to tens or hundreds (P. putida, haloarchaea, methanogens, Synechocystis).
>
> The general conclusion that ploidy varies by taxon and growth phase would survive any single removal.
>

## TAXRES/name-resolution.5

The matching problem (synonyms, fuzzy matching of misspellings, homonyms via context) is handled; the unsolved part is a curation choice, which authority's lineage to adopt, not a matching failure: name resolution is the easy part and the authority choice the hard part.

- conf: not stated
- class: not stated
- holds: the review's provisional, single-pass verdict
- src: none (the reviewer's synthesis)
- trail: TAXRES §Provisional verdicts, §What this means

From the note:

> The *matching* problem (synonyms, fuzzy/misspelling, homonyms via context) is largely handled; the unsolved part is a **curation choice** (which authority's lineage to adopt), not a matching failure.
>
> The taxonomy case **inverts the gene case in one helpful way**: name resolution is the *easy* part (mature tooling), and the *hard* part is the authority choice.
>

Not found in the cited text (where to look, not what is wrong): holds: review; holds: single-pass

## H2-04/plant-axis-analogues.5

The one quantitative cross-level agreement measure found is eigenvector angles and eigenvalue ratios with permutation tests, used to show that including intraspecific variation rotates leaf trait axes.

- conf: not stated
- class: not stated
- holds: leaf trait spaces across habitat types, within- versus across-species
- src: puglielliIntraspecificVariabilityLeaf2024 (abstract), puglielliQuantifyingInfluenceIntraspecific2025 (full text)
- trail: H2-04 §Genome-level versus community-level, §answers

From the note:

> The one quantitative cross-level agreement measure found is eigenvector angles and eigenvalue ratios with permutation tests, used to show that including intraspecific variation rotates leaf trait axes [24a abstract; 24b full text].
>
> (iii) Within-species versus across-species: Anderegg (abstract), Osnas (full text), Puglielli (eigenvector angles).
>

## 16S/technical-replicates.5

Greater depth improved replicate agreement in beta diversity for some mocks only.

- conf: not stated
- class: not stated
- holds: Pinto and Raskin's mocks
- src: pintoPCRBiasesDistort2012
- trail: MB-01 §4.4

From the note:

> - Greater depth improved replicate agreement in beta diversity for some mocks only (Pinto and Raskin 2012).
>

## H1-RES/capacity-expression.5

Schirmer et al. (2018), in metagenomes and metatranscriptomes from a human IBD cohort, found species-specific transcriptional biases: some taxa were metagenomically abundant but transcriptionally inactive (for example *Dialister invisus*), and disease-relevant signals were often stronger or only detectable at the RNA level.

- conf: not stated
- class: not stated
- holds: human IBD cohort
- src: schirmer2018
- trail: H1-RES §Other key multi-omics

From the note:

> | Schirmer et al. 2018 | Metagenomes + metatranscriptomes (human IBD cohort) | Species-specific transcriptional biases; some taxa were metagenomically abundant but transcriptionally inactive (example Dialister invisus), and disease-relevant signals were often stronger or only detectable at the RNA level [2]. |
>

## H2-04/covariance-partition.3

Handling of turnover, closure and depth in the microbial partitions: Deutschmann used relative abundances with no log-ratio treatment reported in the findings; Kamneva used Jaccard presence data; Piton normalised by annotated reads and log(x+1), with no log-ratio treatment and 5 to 15% of reads annotated.

- conf: not stated
- class: not stated
- holds: the three microbial studies; the critic: the 5 to 15% figure could not be rechecked
- src: deutschmannDisentanglingEnvironmentalEffects2021, kamnevaGenomeCompositionPhylogeny2017, pitonLifeHistoryStrategies2023
- trail: H2-04 §answers, §Adversarial critique

From the note:

> Handling of turnover, closure and depth: Deutschmann used relative abundances with no log-ratio treatment reported in the findings; Kamneva used Jaccard presence data; Piton normalised by annotated reads and log(x+1) with no log-ratio treatment and 5 to 15% of reads annotated [23].
>
> The numbers 29%, 21%, R2 = 0.64, R2 = 0.32 and 5 to 15% of reads annotated could not be rechecked (eScholarship and HAL returned HTML; the OSTI attempt timed out).
>

## CB3/food-system.5

Crippa et al. 2021 (EDGAR-FOOD): food systems emitted 18 Gt CO2e in 2015, 34% of total GHG, with a stated 95% confidence interval of 14–22 Gt CO2e; CO2, CH4, N2O and F-gases, aggregated with AR5 GWP100.

- conf: not stated
- class: not stated
- holds: 2015; EDGAR-FOOD database; four gases; AR5 GWP100 (CH4 = 28, N2O = 265)
- src: crippaFoodSystemsResponsible2021 (abstract, methods, metric statements)
- trail: CB3-AG-EMISSIONS §Boundary A

From the note:

> **Crippa et al. 2021 (EDGAR-FOOD)**: 18 Gt CO2e in 2015, **34%** of total GHG, with a stated 95% confidence interval of 14–22 Gt CO2e.
>
> CO2, CH4, N2O and F-gases, aggregated with AR5 GWP100 (CH4 = 28, N2O = 265) [3].
>
> | 3 | Food system (EDGAR-FOOD) | 34% | 18 Gt CO2e | 2015 | 4 gases; AR5 GWP100 | Crippa et al. 2021 [3] | 95% CI 14–22 Gt |
>

## 16S/ploidy.4

Growth-rate-dependent merodiploidy: E. coli has 6.8 origins and 1.7 termini per cell at 25 min doubling but 2.5 origins and 1.2 termini at 103 min; B. subtilis (5.9 origins, 1.2 termini) and three soil Bacillus and Paenibacillus isolates are mero-oligoploid and down-regulate origins in stationary phase.

- conf: not stated
- class: meas (note: "All figures below are measured")
- holds: cultures; Pecoraro 2011 is the only direct origin and terminus count for E. coli at two growth rates
- src: pecoraroQuantificationPloidyProteobacteria2011 (FT), bottingerRegulatedPloidyBacillus2018 (AB)
- trail: MB-02 §D1.3, §answers

From the note:

> All figures below are measured.
>
> | E. coli (Gammaproteobacteria) | doubling 25 min / 103 min | origins 6.8 / 2.5; termini 1.7 / 1.2 | [11, FT] |
>
> | Bacillus subtilis and 3 soil Bacillus/Paenibacillus isolates | exponential / stationary | B. subtilis 5.9 origins, 1.2 termini; origins down-regulated in stationary phase | [13, AB] |
>
> Growth-rate-dependent merodiploidy: E. coli has 6.8 origins and 1.7 termini per cell at 25 min doubling but 2.5 origins and 1.2 termini at 103 min [11]; B. subtilis and three soil Bacillus/Paenibacillus isolates are mero-oligoploid in exponential phase (B. subtilis 5.9 origins, 1.2 termini) and down-regulate origins in stationary phase [13].
>
> *Single-source sensitivity:* Removing Pecoraro et al. 2011 [11] would remove the only direct origin and terminus counts for E. coli at two growth rates and the P. putida value.
>

Not found in the cited text (where to look, not what is wrong): holds: cultures

## 16S/abundance-distribution.25

Not found for soil: metagenome-based taxon abundance distributions, copy-number- or ploidy-corrected abundance distributions, and rhizosphere-specific abundance distributions.

- conf: not stated
- class: search (note: "none found as such")
- holds: MB-02's searches
- src: none (a statement about what the search found)
- trail: MB-02 §answers

From the note:

> *Not measured:* Cell-count-based taxon abundance distributions in soil; metagenome-based taxon abundance distributions (marker-gene or genome coverage) in soil reported as a distribution; copy-number- or ploidy-corrected abundance distributions for soil; rhizosphere-specific abundance distributions (none found as such).
>

Not found in the cited text (where to look, not what is wrong): holds: mb-02

## 16S/beta-diversity.4

Bray-Curtis was usually the most powerful metric, and metric choice changes power.

- conf: single (marker)
- class: meas (marker)
- holds: abstract only
- src: kersPowerMicrobiomeStudies2022 (AB; meas; single)
- trail: MB-01 §5.3

From the note:

> Bray-Curtis was usually the most powerful metric, and metric choice changes power (Kers and Saccenti 2022) [AB; meas; single].
>

## TSL/phrase-and-multilingual-tail.1

The review has no surviving claims on single-word vs multi-word phrase selection, or on stopword / multilingual handling at the rare-term tail (brief item 5); these are unanswered.

- conf: not stated
- class: search (note: "no surviving claims")
- holds: the review's source set
- src: none (no evidence collected)
- trail: TSL §5. Not covered

From the note:

> Single-word vs multi-word phrase selection, and stopword/multilingual handling at the rare-term tail (brief item 5) — **no surviving claims**.
>
> Treat as unanswered by this corpus.
>

Not found in the cited text (where to look, not what is wrong): holds: review

## CB1/consumption.1

The US EPA inventory reports minerals applied to soils of 9.9 Mt limestone and 1.0 Mt dolomite in 2020, down from 19.0 and 2.4 Mt in 1990.

- conf: not stated
- class: not stated
- holds: US national inventory, 1990 and 2020
- src: usLimingCRFSource2022
- trail: CB1-LIMING §2. Consumption

From the note:

> **Consumption figures disagree with each other inside a single country.** The US EPA inventory reports minerals applied to soils of 9.9 Mt limestone and 1.0 Mt dolomite in 2020, down from 19.0 and 2.4 Mt in 1990 [4].
>

## 16S/pcr-efficiency.1

Documented protocols use 35 cycles in triplicate 25 uL reactions, pooling 240 ng per sample (EMP protocol, one-step), or 25 amplicon cycles plus 8 index cycles with 12.5 ng input (Illumina guide, two-step).

- conf: not stated
- class: not stated
- holds: makers' protocol and documentation; the critic checked the EMP protocol's 35 cycles in triplicate and 240 ng pooling on the live page
- src: earth16SIlluminaAmplicon (PROTOCOL), illumina16SMetagenomicSequencing (DOCUMENTATION; maker's claim)
- trail: MB-01 §3.1, §2.6, §answers, §critic
- rating: "Strong for documented cycle numbers"

From the note:

> **Cycle numbers.** Documented protocols use 35 cycles in triplicate 25 uL reactions, pooling 240 ng per sample (EMP protocol, accessed 2026-10-20) [PROTOCOL], or 25 amplicon cycles plus 8 index cycles (Illumina guide) [DOCUMENTATION].
>
> The Illumina guide's two-step design uses 25 amplicon cycles and 8 index cycles with 12.5 ng input (Illumina 16S guide) [DOCUMENTATION; maker's claim].
>
> The EMP protocol uses a one-step 35-cycle PCR in triplicate (EMP protocol) [PROTOCOL].
>
> Documented protocols use 35 cycles (EMP) or 25 plus 8 index cycles (Illumina guide).
>
> **values reported for some quantities; several missing**: PCR cycle numbers.
>
> Documented protocols use 35 cycles (EMP protocol, triplicate reactions) and 25 amplicon cycles plus 8 index cycles (Illumina guide; maker documentation).
>
> - **D3: measured values**: The body supports the values given: documented cycle numbers (the EMP protocol's 35 cycles in triplicate and 240 ng pooling were checked on the live page), copy-number ranges across genomes, per-study and per-run read ranges, and microbial-load ranges.
>
> Moderate for documented cycle numbers.
>

## 16S/core-microbiome.4

In common bean rhizospheres across four US regions plus a Colombian dataset, 48 bacterial and archaeal taxa were detected in every sample; fitting a neutral model to the abundance-occupancy distribution, 13.7% of bacterial and archaeal taxa deviated from neutral expectation; samples were rarefied to 31,255 reads.

- conf: not stated
- class: not stated
- holds: common bean rhizosphere; the rhizosphere neutral-deviation figure is consistent across rhizosphere studies; checked by the critic
- src: stopnisekPersistentMicrobiomeMembers2021 (FT)
- trail: MB-02 §D3.2, §answers, §critic

From the note:

> **Rhizosphere (kept separate).**
>
> - **Common bean** [74, FT]: across four US regions plus a Colombian dataset, 48 bacterial and archaeal taxa were detected in every sample.
>
> Fitting a neutral model to the abundance-occupancy distribution, 13.7% of bacterial and archaeal taxa deviated from neutral expectation.
>
> Samples were rarefied to 31,255 reads.
>
> Rhizosphere: in common bean rhizospheres across four US regions plus Colombia, 48 bacterial and archaeal taxa occurred in all samples, and 13.7% of bacterial and archaeal taxa deviated from a neutral abundance-occupancy expectation [74]; in 4,866 maize rhizosphere samples, seven OTUs were present in all samples [75]; core assignments in an Arabidopsis root dataset varied 7-fold among methods [52].
>
> The rhizosphere neutral-deviation figure rests on Stopnisek and Shade 2021 [74] alone.
>
> Rhizosphere studies show taxa present in all samples and about 14% deviating from a neutral curve [74,75].
>
> Rhizosphere evidence covers core membership in bean and maize, with 13.7% of bean bacterial and archaeal taxa deviating from a neutral curve.
>
> These all matched: Pecoraro 2011 (E. coli 6.8/2.5 origins, P. putida 20/14, Caulobacter 2.1, Wolinella 0.9), Louca 2018 (15%/30% autocorrelation, 49% of SILVA OTUs, 635 communities including soil), Gao and Wu 2023 (0.96 precision, 20%/31%, 13% to 65%), Kembel 2012 (r 0.70 to 0.81, K = 0.48), Vetrovsky 2013 (mean 4.2, 15%/21%, Acidobacteria 50.1% to 66.0%), Bickel and Or 2021 (0.4%, 0.019%, prevalence 0.3 vs 0.001), Jia 2022 (61.59/45.65/28.36%, ASV counts), Custer 2023 (1.21 to 9.42%), Pascoal 2025 (181 articles, 37%, 84%, V4V5 versus full-length reversal) and Stopnisek and Shade 2021 (48 taxa, 13.7%, rarefied to 31,255 reads).
>

## 16S/zeros.1

Simple count models sufficed across four zero-generating processes, and zero inflation was warranted only under narrow conditions.

- conf: single (marker)
- class: model (marker)
- holds: abstract only
- src: silvermanNaughtAllZeros2020 (AB; model; single)
- trail: MB-01 §4.3, §answers

From the note:

> **Zeros.** In simulation, simple count models sufficed across four zero-generating processes, and zero inflation was warranted only under narrow conditions (Silverman 2020) [AB; model; single].
>
> Zero-inflated models were warranted only under narrow conditions (Silverman 2020, abstract).
>

## NFERT/manufacturing-co2.3

A process-optimisation study citing a global mix that includes coal reports about 2.8 t CO₂ per tonne of ammonia.

- conf: not stated
- class: not stated
- holds: a global plant mix including coal; cradle-to-gate manufacturing, excluding field N₂O
- src: demirhanSustainableAmmoniaProduction2019
- trail: NFERT §Carbon dioxide per unit

From the note:

> A process-optimisation study citing a global mix that includes coal reports about 2.8 t CO₂ per tonne (Demirhan et al. 2019).
>

Not found in the cited text (where to look, not what is wrong): holds: plant; holds: cradle-to-gate; holds: field; holds: n₂o

## H1-06/depth-dependence.4

Martiny et al. call their estimates "an upper bound for many functions" because many trait carriers sit in clusters of one; tau_D is an upper bound under undersampling.

- conf: not stated
- class: not stated
- holds: the original authors' statement about their own depths
- src: martinyPhylogeneticConservatismFunctional2013
- trail: H1-06 §3. Part A2, §5. Bounds and failure modes, §answers

From the note:

> Martiny et al. likewise call their estimates "an upper bound for many functions" because many trait carriers sit in clusters of one [1].
>
> - tau_D is an upper bound under undersampling [1].
>
> The original authors call their depths upper bounds because of undersampling.
>

## H1-05/genome-size.1

Average genome size biases gene-abundance comparisons.

- conf: not stated
- class: not stated
- holds: human gut only [47]
- src: nayfachAverageGenomeSize2015 (AB; human gut)
- trail: H1-05 §2

From the note:

> - **Genome size.** Average genome size biases gene-abundance comparisons [47] [AB; human gut].
>
> - Genome size: [47], with soil shifts in [2][8] (indirect).
>

## H1-RES/pangenome.27

The sub-claim that bacterial species contain both conserved core genomes and large, variable accessory genomes is strongly supported for many taxa: the evidence shows a continuum from closed pangenomes with minimal accessory fractions (MTBC, *E. amylovora*, *Chlamydia*) to highly open pangenomes with accessory fractions exceeding core size (*E. coli*, *Burkholderia*, *Corallococcus*).

- conf: not stated
- class: not stated
- holds: the taxa reviewed in Sub-claim 1
- src: none (the reviewer's synthesis)
- trail: H1-RES §Taxon-Dependence
- rating: "strongly supported for many taxa"

From the note:

> The sub-claim that bacterial species contain both conserved core genomes and large, variable accessory genomes is strongly supported for many taxa but not universal.
>
> The evidence demonstrates a continuum from closed pangenomes with minimal accessory fractions (MTBC, *E. amylovora*, *Chlamydia*) to highly open pangenomes with accessory fractions exceeding core size (*E. coli*, *Burkholderia*, *Corallococcus*).
>

Not found in the cited text (where to look, not what is wrong): holds: reviewed; holds: in; holds: 1

## GHOST/missingness-degradation.4

At 99% missing on Cora, propagation reaches ~78–79% accuracy.

- conf: not stated
- class: not stated
- holds: Cora, 99% missing; homophilous + sparse + MCAR, and mostly author-reported
- src: rossiUnreasonableEffectivenessFeature2022, leiSelfsupervisedGuidedHypergraph2023
- rating: "Confidence: high (3-0 / 2-1)"
- trail: GHOST §2. Degradation

From the note:

> - Contrast at 99% missing on Cora: propagation ~78–79% vs **GCNMF 34.54%** — the latter confirmed by two independent papers [R1, R2].
>
> *Confidence: high (3-0 / 2-1).*
>
> **Caveat carried on every number above:** homophilous + sparse + MCAR, and mostly author-reported.
>

## 16S/workflow-bias.7

Across 15 laboratories, variability depended most on specimen type, then DNA extraction, then handling laboratory, then bioinformatics; interlaboratory differences were substantial, and absolute diversity was not comparable between laboratories even with the same pipeline.

- conf: repl (marker)
- class: meas (marker)
- holds: MBQC, 15 laboratories
- src: sinhaAssessmentVariationMicrobial2017 (FT; meas; single)
- trail: MB-01 §2.2, §4.3, §answers

From the note:

> **Interlaboratory.** Across 15 laboratories, variability depended most on specimen type, then DNA extraction, then handling laboratory, then bioinformatics (Sinha 2017, MBQC) [FT; meas; single].
>
> Whole workflow.
>
> Across 15 laboratories, specimen type mattered most, then extraction, then laboratory and bioinformatics (MBQC).
>
> Absolute diversity was not comparable between laboratories even with the same pipeline.
>
> - Interlaboratory differences were substantial (MBQC).
>

## H1-06/a1-environmental-preferences.8

Natural evidence for environmental optima is thin.

- conf: not stated
- class: not stated
- holds: A1 as a whole
- src: none (the reviewer's synthesis)
- trail: H1-06 §5. Bounds and failure modes

From the note:

> - Natural evidence for environmental optima (A1) is thin.
>

## H1-06/ph-preference.4

ASVs within single families spanned 3.8 to 4.2 pH units: Xanthobacteraceae in soil 4.01 to 8.20 (4.19 units), Chitinophagaceae in freshwater 4.53 to 8.35 (3.82 units).

- conf: single (critic: C-001)
- class: meas (critic: C-001)
- holds: Ramoneda's soil and freshwater datasets; the figures are the critic's reading of the source, which corrects the review's "four or more pH units"
- src: ramonedaBuildingGenomebasedUnderstanding2023
- trail: H1-06 §2. Part A1, §critic

From the note:

> **Reformulated verdict:** A1 (environmental preferences): natural systems, measured for pH only, SINGLE SOURCE (Ramoneda et al. 2023).
>
> Signal is significant in 4 of 5 datasets but weak (Pagel's lambda 0.22 to 0.78, Moran's I < 0.25 at all depths), there is no consenTRAIT-style depth, and families span 3.7 to 4.2 pH units.
>
> The family claim is partly wrong: Chitinophagaceae spans 4.63 to 8.35 (3.72 units), not 'four or more pH units'.
>
> - [13] Ramoneda 2023 body claim: 'ASVs within single families spanned four or more pH units (Xanthobacteraceae in soil, Chitinophagaceae in freshwater)'. The source gives 4.01 to 8.20 (4.19 units) and 4.63 to 8.35 (3.72 units), so Chitinophagaceae does not span four units.
>

Not found in the cited text (where to look, not what is wrong): 3.8; 4.53; 3.82; holds: review

## H1-06/genome-incompleteness.1

No study was found that directly tests how genome incompleteness biases tau_D or phylogenetic signal statistics; its effect on depth estimates themselves has not been measured in any source read.

- conf: not stated
- class: search (note: "No study found tests directly how incompleteness biases tau_D or signal statistics")
- holds: the provenance lists routes behind every 'not found'; the critic: the routes behind this 'not found' are not named in the body
- src: none (a search result)
- trail: H1-06 §3. Part A2, §5. Bounds and failure modes, §Provenance, §critic

From the note:

> **Genome incompleteness.** No study found tests directly how incompleteness biases tau_D or signal statistics.
>
> Its effect on depth estimates themselves has not been measured in any source read.
>
> Not found by these routes: (1) any consenTRAIT tau_D for pH, temperature or moisture optima; (2) any rank-wise composition-environment study, other than Lu 2016, that controls group number and size (Schmidt 2014 controls them, but for identity thresholds and annotation consistency, not ranks); (3) any direct test of how genome incompleteness biases tau_D or signal statistics.
>
> - gap: No study found that directly tests how genome incompleteness biases tau_D or phylogenetic signal. The search routes behind this 'not found' are not named in the body, which Common rule 7 requires.; setting_or_class: MAG-based consenTRAIT or signal analyses (e.g. GEM catalogue, GTDB MAG-inclusive trees); brief_bullet: How incompleteness of genomes changes conservation estimates
>

## TAXRES/gtdb.4

GTDB is bulk-downloadable and explicitly tracks consistency against NCBI taxonomy.

- conf: not stated
- class: not stated
- holds: GTDB release R10-RS226, as found by a single-pass web search on 2026-06-19
- src: parksGTDBRelease102026, parksGTDBOngoingCensus2022
- trail: TAXRES §GTDB structure

From the note:

> It is bulk-downloadable and explicitly tracks consistency against NCBI taxonomy.
>
> Searched 2026-06-19 across four angles: NCBI-vs-GTDB divergence, taxon-name resolution tools, GTDB structure/identifiers, and the GBIF/Catalogue-of-Life cross-kingdom backbone.
>

Not found in the cited text (where to look, not what is wrong): holds: r10-rs226; holds: single-pass

## H2-01/shared-mean.2

Per-sample Spearman correlations between predicted and measured KEGG gene profiles (0.53 to 0.87) barely changed when each gene's abundance was permuted across samples (soil example: 0.85 unpermuted, 0.84 permuted); the per-sample metric is almost insensitive to permuting genes across samples.

- conf: not stated
- class: meas (marker)
- holds: metagenome prediction tools scored per sample, across human, non-human and soil datasets
- src: sunInferenceBasedAccuracyMetagenome2020 (FT; measured)
- trail: H2-01 §2.2, §3.3

From the note:

> First, per-sample Spearman correlations between predicted and measured KEGG gene profiles (0.53 to 0.87) barely changed when each gene's abundance was permuted across samples (soil example: 0.85 unpermuted, 0.84 permuted) [Sun2020; FT; measured].
>
> Sun et al. (2020) showed that the per-sample Spearman metric is almost insensitive to permuting genes across samples, and that inference-level agreement was reasonable in human datasets and much lower in non-human and soil datasets [Sun2020; FT].
>
> Sun2020 shows that a per-sample prediction-accuracy metric barely changes when genes are permuted across samples.
>

Not found in the cited text (where to look, not what is wrong): holds: metagenome

## H1-RES/pangenome.20

In *Erwinia amylovora*, comparative analysis revealed a pangenome with approximately 89% conserved core genes.

- conf: not stated
- class: not stated
- holds: *E. amylovora*
- src: none (cited only as SC1 [44]; the note gives no reference list)
- trail: H1-RES §Counter-Evidence: Taxa

From the note:

> Other pathogens with restricted accessory fractions include *Erwinia amylovora*, where comparative analysis of 12 strains revealed a pangenome with approximately 89% conserved core genes [44].
>

## H2-01/levels-across.8

Nine biomes were strongly discriminated by metabolic profiles.

- conf: not stated
- class: not stated
- holds: nine biomes
- src: dinsdaleFunctionalMetagenomicProfiling2008 (AB)
- trail: H2-01 §4.2

From the note:

> Nine biomes were strongly discriminated by metabolic profiles [Dinsdale2008; AB].
>

## H1-RES/accessory-function.9

In *Pseudomonas* at a hexachlorocyclohexane (HCH) dumpsite, metabolic pathways were enriched strain-specifically, with an intact mobile class-I integron (3,552 bp) encoding dihydrofolate reductase in strain RL associated with a Tnp21-like transposon (97% identity); metagenomes from pond sediment and HCH-contaminated soils showed in situ enrichment of an integron-associated transposase gene (TnpA6100) with increasing HCH contamination (0.7 to 450 mg HCH g⁻¹ of soil).

- conf: not stated
- class: not stated
- holds: one HCH dumpsite; pond sediment and HCH-contaminated soils
- src: none (cited only as SC2 [9]; the note gives no reference list)
- trail: H1-RES §Confirming Evidence: Accessory

From the note:

> Pangenome analysis of *Pseudomonas* at a hexachlorocyclohexane (HCH) dumpsite revealed strain-specific enrichment of metabolic pathways, with an intact mobile class-I integron (3,552 bp) encoding dihydrofolate reductase detected in strain RL and associated with a Tnp21-like transposon (95% identity) [9].
>
> Metagenomics data from pond sediment and HCH-contaminated soils revealed in situ enrichment of integron-associated transposase gene (TnpA6100) across increasing HCH contamination (0.7 to 450 mg HCH g⁻¹ of soil) [9].
>

Not found in the cited text (where to look, not what is wrong): 97

## H1-02/read-technology.5

Long-read activated-sludge MAGs carried full rRNA operons in 93.1% of cases.

- conf: not stated
- class: not stated
- holds: engineered (activated sludge)
- src: singletonConnectingStructureFunction2021
- trail: H1-02 §3.5, §Verdict as delivered

From the note:

> Long-read activated-sludge MAGs carried full rRNA operons in 91.3% of cases [30].
>
> Both are engineered.
>
> In engineered bioreactors, read technology changes contiguity and rRNA recovery [29, 30].
>

Not found in the cited text (where to look, not what is wrong): 93.1

## CB2/catalogue-recovery.3

UHGG: of 4,644 human-gut species representatives, 573 carried the full rRNA set, of which 38 are MAGs (535 are isolates).

- conf: not stated
- class: not stated
- holds: human gut species representatives
- src: almeidaUnifiedCatalog2042020
- trail: CB2-RRNA §1. Measured recovery

From the note:

> | Catalogue / dataset | Environment | Genomes | Carrying the full rRNA set | Source |
>
> | UHGG | human gut | 4,644 species representatives | 573 total, of which **38 are MAGs** (535 are isolates) | Almeida et al. 2021 |
>

## H2-04/complementarity-overlap.11

Cooperative metabolic potential between pairs of organisms peaks at moderate overlap.

- conf: not stated
- class: model (marker)
- holds: pairwise models
- src: freilichCompetitiveCooperativeMetabolic2011 (AB; modelled)
- trail: H2-04 §Complementarity versus overlap

From the note:

> Pairwise models predict cooperative potential peaks at moderate overlap [10c, AB; modelled], and costless secretions create broad cross-feeding opportunities [24d, AB; modelled].
>

## 16S/quality-filtering.3

Stringent UPARSE-style filtering could significantly underestimate abundance and diversity, and newer clusterers produced up to 50% fewer spurious OTUs than UCLUST.

- conf: cont (marker)
- class: meas (marker)
- holds: Kopylova 2016 benchmark
- src: kopylovaOpensourceSequenceClustering2016 (FT; meas; cont)
- trail: MB-01 §2.9, §7. Bounds

From the note:

> **Contrary.** Stringent UPARSE-style filtering could significantly underestimate abundance and diversity, and newer clusterers produced up to 60% fewer spurious OTUs than UCLUST (Kopylova 2016) [FT; meas; cont].
>
> - stringent filtering (Kopylova 2016);
>

Not found in the cited text (where to look, not what is wrong): 50

## 16S/abundance-distribution.15

Lognormal-based estimates gave 6,400 to 38,000 taxa per gram of soil.

- conf: not stated
- class: model (note: "modelled")
- holds: abstract only
- src: curtisEstimatingProkaryoticDiversity2002 (AB)
- trail: MB-02 §D3.1, §answers

From the note:

> - **Curtis et al. 2002** [67, AB]: lognormal-based estimates gave 6,400 to 38,000 taxa per gram (modelled).
>
> Clone libraries and models: lognormal null models were consistent with four Arizona soils and showed that small surveys reproduce richness but not composition [68]; lognormal-based estimates gave 6,400 to 38,000 taxa per gram of soil [67]; diversity estimates depend on the assumed distribution [69].
>

## CB1/lime-requirement.1

Rates are set by a lime requirement calculation, not by a standard dose, and the spread across soil types is wide enough that any single number misleads.

- conf: not stated
- class: not stated
- holds: the rates reviewed in the note's section 1
- src: none (the reviewer's synthesis of section 1)
- trail: CB1-LIMING §1. Application rates

From the note:

> Rates are set by a lime requirement calculation, not by a standard dose, and the spread across soil types is wide enough that any single number misleads.
>

Not found in the cited text (where to look, not what is wrong): holds: reviewed; holds: in; holds: 1

## CB3/gwp-metric.1

EDGAR-FOOD and FAOSTAT aggregate with AR5 GWP100 (CH4 = 28, N2O = 265); AR6 uses AR6 GWP100 with climate–carbon feedbacks (CH4 = 27, N2O = 273).

- conf: not stated
- class: not stated
- holds: EDGAR-FOOD (Crippa et al. 2021), FAOSTAT (Tubiello et al. 2022), IPCC AR6 WGIII Ch. 7 Table 7.1 footnote g
- src: crippaFoodSystemsResponsible2021, tubielloPrePostproductionProcesses2022, nabuursAgricultureForestryOther2022
- trail: CB3-AG-EMISSIONS §Where the major sources differ, §Boundary B

From the note:

> **Metric.** EDGAR-FOOD and FAOSTAT use AR5 GWP100 (CH4 = 28, N2O = 265) [3, 4]; AR6 uses AR6 GWP100 with feedbacks (CH4 = 27, N2O = 273) [1].
>
> CO2, CH4, N2O and F-gases, aggregated with AR5 GWP100 (CH4 = 28, N2O = 265) [3].
>
> Metric: AR6 GWP100 with climate–carbon feedbacks (CH4 = 27, N2O = 273) [1, Table 7.1 footnote g].
>

Not found in the cited text (where to look, not what is wrong): holds: crippa; holds: 2021; holds: tubiello; holds: 2022; holds: ipcc; holds: wgiii; holds: ch; holds: 7

## H1-06/trait-compilations.4

Only 9.9% of continuous and 8.6% of binary traits met Goberna and Verdú's threshold for accurate phylogenetic prediction.

- conf: not stated
- class: not stated
- holds: 990 traits, SILVA r119 tree; binary traits mostly gene presence
- src: gobernaPredictingMicrobialTraits2016
- trail: H1-06 §2. Part A1, §critic
- limit: access (note: "I could not re-open it because the publisher returned a bot challenge, so it carries no weight on its own")

From the note:

> **Compilations and models.** Goberna and Verdú 2016 [16] (compiled and modelled) collated 990 traits on a SILVA r119 tree.
>
> Only 9.9% of continuous and 8.6% of binary traits met its threshold for accurate phylogenetic prediction.
>
> (One search agent read this paper in full; I could not re-open it because the publisher returned a bot challenge, so it carries no weight on its own.
>
> - Goberna and Verdu 2016 [16]: the synthesiser could not re-open it but still quotes specific figures (mean -D+1 = 0.93, K = 0.16, 9.9% and 8.6%) and an internal-inconsistency claim. It is labelled as carrying no weight, but it is listed in the A1 verdict's evidence classes.
>

## 16S/abundance-distribution.7

The soil SAD shape is in partial conflict: exponential or inverse gamma (Zhou 2013) against lognormal (Shoemaker 2017; Grilli 2020); these use different fitting targets.

- conf: cont (note: "the conflict is only partial")
- class: not stated
- holds: different fitting targets
- src: zhouRandomSamplingProcess2013, shoemakerMacroecologicalTheoryMicrobial2017, grilliMacroecologicalLawsDescribe2020
- trail: MB-01 §answers

From the note:

> *Conflicts:* Soil SAD shape: exponential or inverse gamma (Zhou 2013) versus lognormal (Shoemaker 2017; Grilli 2020).
>
> These use different fitting targets, so the conflict is only partial; Haegeman 2013 argues the tail is not identifiable from sample data at all.
>

## CB1/application-frequency.3

Once the full recommended rate is applied, the Ethiopian value-chain study reports, "it can benefit farmers for up to five years".

- conf: not stated
- class: not stated
- holds: Ethiopia
- src: oumerAgriculturalLimeValue2023
- trail: CB1-LIMING §1. Application rates

From the note:

> The Ethiopian value-chain study reports that about 20 quintals (2 t) of lime per hectare is the average requirement, and that once the full recommended rate is applied "it can benefit farmers for up to five years" [8].
>

Not found in the cited text (where to look, not what is wrong): holds: ethiopia

## 16S/pcr.13

Single versus triplicate pooled PCRs made no significant difference.

- conf: repl (marker)
- class: meas (marker)
- holds: abstract only; the critic notes an open PMC copy exists, so the AB label understates rather than overstates access
- src: marotzTriplicatePCRReactions2019 (AB; meas; repl)
- trail: MB-01 §2.4, §Adversarial

From the note:

> - Single versus triplicate pooled PCRs made no significant difference (Marotz 2019) [AB; meas; repl].
>
> - Marotz 2019: labelled AB, but an open PMC copy exists (PMC7030937). The label understates rather than overstates access.
>

## 16S/term-sensitivity.10

In Loess Plateau soils, two primer pairs gave different diversity responses to land use, so rare and abundant classes depend on the primer, not only the cutoff.

- conf: not stated
- class: not stated
- holds: Loess Plateau soils; abstract only
- src: zengIdentifyingBiogeographicPatterns2021 (AB)
- trail: MB-02 §D2.5

From the note:

> - **Loess Plateau soils** [59, AB]: two primer pairs gave different diversity responses to land use, so rare and abundant classes depend on the primer, not only the cutoff.
>

## 16S/pcr.2

Two-template 27F-338R mixtures converged toward 1:1 products regardless of starting ratio; the bias depended strongly on cycle number and fit a kinetic model of product reannealing.

- conf: repl (marker)
- class: meas (marker)
- holds: two-template mixtures; abstract only
- src: suzukiBiasCausedTemplate1996 (AB; meas; repl)
- trail: MB-01 §2.4, §answers

From the note:

> - **Reannealing.** Two-template 27F-338R mixtures converged toward 1:1 products regardless of starting ratio. The bias depended strongly on cycle number and fit a kinetic model of product reannealing (Suzuki and Giovannoni 1996) [AB; meas; repl].
>
> Template reannealing pushed two-template mixtures toward 1:1 (Suzuki and Giovannoni 1996, abstract).
>
> Reannealing pushes mixtures toward 1:1.
>

## H2-01/gene-set-aggregation.10

That shared members inflate pathway-pathway covariance, and so lower apparent dimension, is the reviewer's inference.

- conf: not stated
- class: reading (note: "is the reviewer's inference")
- holds: pathway profiles built from shared KOs
- src: none (the reviewer's inference)
- trail: H2-01 §2.3

From the note:

> The implication that shared members inflate pathway-pathway covariance, and so lower apparent dimension, is the reviewer's inference.
>

Not found in the cited text (where to look, not what is wrong): holds: kos

## H1-02/sample-dependence.2

In the human gut, dependence on sample properties was not measured for gene or pathway content; proxies (chimerism rate, aligned fraction, ribosomal-protein absence by catalogue) differ between catalogues.

- conf: not stated
- class: search (critic: C-007)
- holds: natural human gut; the body supports not measured for gene content, with indirect proxy evidence that varies by catalogue (the critic)
- src: orakovGUNCDetectionChimerism2021, almeidaUnifiedCatalog2042020, miseUnexpectedAbsenceRibosomal2022
- trail: H1-02 §critic, §Adversarial critique

From the note:

> Part B, human gut: NOT MEASURED for gene or pathway content.
>
> Proxies (chimerism rate [9], aligned fraction [10], ribosomal-protein absence by catalogue [6]) differ between catalogues, but catalogue is confounded with pipeline and sample set, and the review's own Section 4 says these are not gene-content measures.
>
> The Part B gut verdict ('measured and systematic for study of origin') contradicts the review's own Section 4, which says the measured dependence 'concerns yield, completeness, chimerism or assembled fraction', not gene content.
>
> The body therefore supports 'not measured for gene content, indirect proxy evidence varies by catalogue'.
>
> - The Part B gut verdict relabels pipeline or catalogue differences as 'study of origin' dependence of gene-content artefacts. That is a reviewer construction: none of [6], [9] or [10] measures artefact size in gene content against a study variable with sample set held constant, apart from [10]'s aligned fraction, which is split by quality tier.
>

## H1-06/moisture-preference.4

Lennon et al. 2012 is the only direct rank-resolved measurement of a moisture optimum.

- conf: single (note: "SINGLE SOURCE")
- class: search (note: "the only direct rank-resolved measurement of a moisture optimum found")
- holds: the search routes in the note's provenance
- src: lennonMappingNicheSpace2012
- trail: H1-06 §2. Part A1

From the note:

> This is the only direct rank-resolved measurement of a moisture optimum found.
>
> SINGLE SOURCE.
>

Not found in the cited text (where to look, not what is wrong): holds: in

## H1-05/averaging.6

In HMP stool, apparent functional selection disappeared under restricted shuffles, so it was artifactual.

- conf: not stated
- class: not stated
- holds: HMP stool data [29][30]; functions inferred through a gene-content matrix
- src: hoChallengesInterpretingFunctional2025, hoChallengesQuantifyingFunctional2024
- trail: H1-05 §3.2, §answers

From the note:

> - HMP stool: apparent selection disappeared under restricted shuffles.
>
> Other habitats: the same null found no functional selection in bromeliad communities (reanalysing [33]) and found apparent selection in HMP stool to be artifactual under restricted shuffles [29][30].
>

Not found in the cited text (where to look, not what is wrong): holds: gene-content

## H2-04/aggregation-artefacts.2

Standard tests of community-weighted mean versus environment have inflated Type I error that rises as beta diversity falls.

- conf: not stated
- class: model (marker)
- holds: trait ecology
- src: zelenyWhichResultsStandard2018 (AB; modelled)
- trail: H2-04 §Artefacts of aggregation

From the note:

> Standard tests of community-weighted mean versus environment have inflated Type I error that rises as beta diversity falls [35, AB; modelled]; the fourth-corner approach is proposed as a remedy [23a, AB].
>

## H1-05/chronosequence.2

Over 143 years of grassland restoration, bacterial richness falls while SEED functional richness expands.

- conf: not stated
- class: not stated
- holds: a grassland restoration chronosequence [9]; alpha diversity
- src: goodallTaxonomicFilteringAccompanies2026 (FT via agents)
- trail: H1-05 §1.5

From the note:

> Examples: bacterial richness falls while SEED functional richness expands over 143 years of grassland restoration [9]; taxonomic diversity falls while C, N and P gene diversity rises along Swedish succession, with PICRUSt2 used for the redundancy analyses [10] [both FT via agents].
>

## GHOST/feature-propagation.1

Feature Propagation (FP) minimises Dirichlet energy, giving a diffusion-type PDE on the graph whose discretisation reconstructs missing features from observed neighbours: a simple, fast, scalable algorithm.

- conf: not stated
- class: not stated
- holds: its motivating setting is the partially-attributed / cold-start case ("age and gender available only for a small subset of users")
- src: rossiUnreasonableEffectivenessFeature2022
- rating: "Confidence: high (3-0)"
- trail: GHOST §1. Strategies

From the note:

> - **Neighbour feature propagation / diffusion imputation.** Feature Propagation (FP) minimises Dirichlet energy, giving a diffusion-type PDE on the graph whose discretisation reconstructs missing features from observed neighbours — a simple, fast, scalable algorithm.
>
> Its motivating setting is explicitly the partially-attributed / cold-start case ("age and gender available only for a small subset of users") [R1].
>
> *Confidence: high (3-0).*
>

## H1-RES/accessory-function.5

Antarctic *Arthrobacter* strains (36 isolates) harboured 11 plasmids of 8.4 to 98.6 kb encoding UV protection and heavy metal resistance, 10 carrying conjugation modules; the plasmids showed limited similarity to mesophilic *Arthrobacter* plasmids, indicating novel replicons adapted to Antarctic conditions.

- conf: not stated
- class: not stated
- holds: 36 psychrotolerant Antarctic isolates
- src: none (cited only as SC2 [10]; the note gives no reference list)
- trail: H1-RES §Confirming Evidence: Accessory

From the note:

> Antarctic *Arthrobacter* strains (36 isolates) harbored 11 plasmids ranging from 8.4 to 90.6 kb encoding UV protection, heavy metal resistance, with 10 carrying conjugation modules [10].
>
> Plasmids from these psychrotolerant strains showed limited similarity to mesophilic *Arthrobacter* plasmids, indicating novel replicons adapted to Antarctic conditions [10].
>

Not found in the cited text (where to look, not what is wrong): 98.6

## CB3/n2o.6

Global N₂O budgets give agriculture 3.8 (2.5–5.8) Tg N yr−1 for 2007–2016 out of 7.3 (4.2–11.4) Tg N anthropogenic.

- conf: not stated
- class: not stated
- holds: 2007–2016
- src: tianComprehensiveQuantificationGlobal2020 (abstract, Table 1, methods)
- trail: CB3-AG-EMISSIONS §Boundary D

From the note:

> The 2020 predecessor gave agriculture 3.8 (2.5–5.8) Tg N yr−1 for 2007–2016 out of 7.3 (4.2–11.4) Tg N anthropogenic [7].
>

Not found in the cited text (where to look, not what is wrong): N₂O

## CB3/food-system.10

FAOSTAT's own share is falling and has been revised: Analytical Brief 94 reports 16.2 Gt CO2eq for 2022 against a global total of 53.5 Gt, i.e. 29.7%, "below 30 percent for the first time on record", down from 38% in 2000.

- conf: not stated
- class: not stated
- holds: 2022; FAOSTAT agrifood systems, four gases, AR5 GWP100; global total 53.5 Gt
- src: faoGreenhouseGasEmissions2024
- trail: CB3-AG-EMISSIONS §Boundary A

From the note:

> **FAOSTAT's own share is falling and has been revised.** Analytical Brief 94 reports 16.2 Gt CO2eq for 2022 against a global total of 53.5 Gt, i.e. **29.7%**, "below 30 percent for the first time on record", down from 38% in 2000 [6].
>

Not found in the cited text (where to look, not what is wrong): holds: ar5; holds: gwp100

## H2-01/neighbouring-transfer.6

In the E. coli pangenome, accessory-gene presence was predicted from other accessory genes on held-out random genomes; after filtering and removing phylogenetic signal, 16.7% of families were predictable at F1 ≥ 0.9 against a chance rate of about 1 to 1.7%.

- conf: repl (marker)
- class: not stated
- holds: one species pangenome, held-out genomes
- src: beavanContingencyRepeatabilityPredictability2023 (FT; SINGLE SOURCE)
- trail: H2-01 §3.3

From the note:

> - **Gene co-occurrence across genomes.** In the E. coli pangenome, accessory-gene presence was predicted from other accessory genes on held-out random genomes; after filtering and removing phylogenetic signal, 16.7% of families were predictable at F1 ≥ 0.9 against a chance rate of about 1 to 1.7% [Beavan2024; FT; SINGLE SOURCE].
>
> Neighbouring microbial evidence concerns other quantities: taxon-to-function mappings transfer less well as reference coverage of the target habitat falls [Langille2013; Sun2020]; functional-profile classifiers transfer across studies at AUROC 0.70 to 0.89 in human gut [Wirbel2019]; gene co-occurrence across genomes predicts held-out genomes and held-out phyla, with predictability varying by phylum [Beavan2024; KonnoIwasaki2023].
>

