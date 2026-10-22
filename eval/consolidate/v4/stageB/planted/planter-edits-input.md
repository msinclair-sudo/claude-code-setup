# Claims to edit, one edit each, of the type named

**Edit type: counter**

## H1-05/averaging.2

Ho and Huang's null permutes taxon labels across the gene-content matrix, which keeps function prevalences and scrambles taxon-function links; it tests variability around a mean community within one environment, not turnover across environments.

- conf: not stated
- class: not stated
- holds: [29], [30]
- src: hoChallengesInterpretingFunctional2025, hoChallengesQuantifyingFunctional2024
- trail: H1-05 §3.2, §critic

From the note:

> Their null permutes taxon labels across the gene-content matrix, which keeps function prevalences and scrambles taxon-function links.
>
> It tests variability around a mean community within one environment, not turnover across environments.
>

**Edit type: counter**

## H2-04/complementarity-overlap.14

Among 20 soil isolates in 40 carbon environments, overlap in carbon use predicted competition (68% for the most similar non-identical pairs) and difference predicted facilitation (Spearman 0.75); this bears on mechanism, not on covariation across samples.

- conf: not stated
- class: meas (marker)
- holds: in vitro, no community profiles; figures checked by the critic against full text
- src: kehePositiveInteractionsCommon2021 (FT; measured; in vitro, no community profiles)
- trail: H2-04 §Complementarity versus overlap, §answers, §critic

From the note:

> Among 20 soil isolates in 40 carbon environments, overlap in carbon use predicted competition (68% for the most similar non-identical pairs) and difference predicted facilitation (Spearman 0.75) [20, FT; measured; in vitro, no community profiles].
>
> Measured in vitro: overlap in carbon use predicts competition (68% of the most similar pairs) and difference predicts facilitation (Spearman 0.75) [20, full text]; antagonism rises with metabolic similarity, with small effect (pseudo-R2 0.015 to 0.032) [28, full text via summary]; competition dominates among tree-hole isolates [10a, abstract].
>
> In vitro results (Kehe 2021: 68%, Spearman 0.75, checked against full text) bear on mechanism, not on covariation across samples.
>
> I checked the main numerical claims against primary text and they hold: Deutschmann 2021 (8.3/24.8/25.7/84.6%; 38 to 86% of true interactions removed), Kishore 2023 (65.4%, 26.8%), Kamneva 2017 (9.84%, 3.81%), Kembel & Cahill 2011 (92 to 98%), Kehe 2021 (68%, Spearman 0.75), Westoby 2021 (pairwise r2 at most 0.0121), Wieczynski 2019 (27%, abstract), Siefert 2015 (25%, 32%), Nielsen 2014 (abstract counts), Freilich 2018 (0.469, 0.527), Tian 2020 (species-pool null).
>

**Edit type: counter**

## H2-01/function-definition.4

The same pattern appears in transcriptomics, where low dimensionality within datasets (Heimberg2016) coexists with unstable higher components across datasets (Lenz2016) and partial transfer across tissue types (Cleary2017).

- conf: not stated
- class: reading (critic: H2-01:C-132)
- holds: transcriptomics (other field)
- src: heimbergLowDimensionalityGene2016 (FT), lenzPrincipalComponentsAnalysis2016 (FT), clearyEfficientGenerationTranscriptomic2017 (FT)
- trail: H2-01 §5. How

From the note:

> The same pattern appears in transcriptomics, where low dimensionality within datasets (Heimberg2016) coexists with unstable higher components across datasets (Lenz2016) and partial transfer across tissue types (Cleary2017).
>
> - Section 5 presents the reviewer's synthesis (coarse and aggregated functions look low-dimensional and stable, fine ones higher-dimensional and taxonomy-linked) as a pattern that measured pieces 'establish'. The dimensionality half is the reviewer's inference.
>

**Edit type: counter**

## H1-RES/pangenome.27

The sub-claim that bacterial species contain both conserved core genomes and large, variable accessory genomes is strongly supported for many taxa but not universal: the evidence shows a continuum from closed pangenomes with minimal accessory fractions (MTBC, *E. amylovora*, *Chlamydia*) to highly open pangenomes with accessory fractions exceeding core size (*E. coli*, *Burkholderia*, *Corallococcus*).

- conf: not stated
- class: not stated
- holds: the taxa reviewed in Sub-claim 1
- src: none (the reviewer's synthesis)
- trail: H1-RES §Taxon-Dependence
- rating: "strongly supported for many taxa but not universal"

From the note:

> The sub-claim that bacterial species contain both conserved core genomes and large, variable accessory genomes is strongly supported for many taxa but not universal.
>
> The evidence demonstrates a continuum from closed pangenomes with minimal accessory fractions (MTBC, *E. amylovora*, *Chlamydia*) to highly open pangenomes with accessory fractions exceeding core size (*E. coli*, *Burkholderia*, *Corallococcus*).
>

**Edit type: counter**

## 16S/abundance-occupancy.12

The same positive abundance-occupancy observation is read as ecological signal by some authors and as near-null by others; the reviewer notes this is a difference of interpretation, not of data.

- conf: not stated
- class: reading (note: "the reviewer notes this is a difference of interpretation")
- holds: neutral-model fits
- src: sloanQuantifyingRolesImmigration2006
- trail: MB-02 §answers

From the note:

> Neutral-model fits imply a positive relationship is expected without selection [73], so the same observation is read as ecological signal by some authors and as near-null by others; the reviewer notes this is a difference of interpretation, not of data.
>

**Edit type: counter**

## GHOST/missingness-degradation.6

At 99% missing on Cora, PaGNN sits at ~58%: low, but not the catastrophic collapse of GCNMF.

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

**Edit type: counter**

## GHOST/contamination.2

Song et al. argue, by molecular-graph analogy, that severe missingness "can alter the semantic information of the graph, leading to changes in the graph structure", which is why they update structure jointly; this is a theoretical / motivational statement, not a measured demonstration.

- conf: not stated
- class: assert (note: "theoretical/motivational statement")
- holds: a motivational argument by analogy to molecular graphs; no measurement
- src: songDynamicGraphStructure2025 (indirect and motivational)
- rating: "verification vote 2-1"
- trail: GHOST §3. Contamination

From the note:

> **No controlled head-to-head was found.** The only support is *indirect and motivational*: Song et al. argue (by molecular-graph analogy) that severe missingness "can alter the semantic information of the graph, leading to changes in the graph structure," which is why they update structure jointly [R4].
>
> This is a theoretical/motivational statement (verification vote 2-1), **not** a measured demonstration that featureless nodes distort feature-bearing nodes' clusters.
>
> Cite as indirect only.
>

**Edit type: counter**

## H1-02/sample-dependence.2

In the human gut, dependence on sample properties was not measured for gene or pathway content; proxies (chimerism rate, aligned fraction, ribosomal-protein absence by catalogue) differ between catalogues, but catalogue is confounded with pipeline and sample set, and these are not gene-content measures.

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

**Edit type: counter**

## TSL/altitude-ordering.8

The altitude-axis evidence (Joho & Sanderson; Yang & Callan; Resnik) is over WordNet / taxonomies: sound for those, indirect for descriptive cluster-label ordering; the verdict's altitude claim rests on principled monotonicity (IC) plus indirect empirical support.

- conf: not stated
- class: not stated
- holds: WordNet and taxonomies; not descriptive cluster labels
- src: johoDocumentFrequencyTerm2007, yangMetricbasedFrameworkAutomatic2009, resnikUsingInformationContent1995, resnikSemanticSimilarityTaxonomy1999
- trail: TSL §Standing caveats

From the note:

> The altitude-axis evidence (Joho & Sanderson; Yang & Callan; Resnik) is over WordNet/taxonomies — sound for those, *indirect* for descriptive cluster-label ordering.
>
> The verdict's altitude claim therefore rests on principled monotonicity (IC) plus indirect empirical support, with the direct label-ordering head-to-head genuinely absent.
>

**Edit type: counter**

## H1-06/rankwise-structuring.12

By preserving topology, Lu's null holds the count of groups per level and the number of fine taxa per group fixed; it does not hold abundance evenness among groups fixed.

- conf: not stated
- class: reading (note: "Reviewer's reading")
- holds: Lu 2016's null; the critic calls the evenness caveat appropriate
- src: luEvaluatingCommunityenvironmentRelationships2016
- trail: H1-06 §4. Part B, §critic

From the note:

> Reviewer's reading: by preserving topology, the null holds the count of groups per level and the number of fine taxa per group fixed.
>
> It does not hold abundance evenness among groups fixed.
>
> Abundance evenness among groups was not controlled.
>
> The review's own caveat about evenness is appropriate.
>

**Edit type: counter**

## CB1/dissolution-pathway.5

Hamilton et al.'s own paired measurements were not one-sided: under their no-till treatment sink strength tended positive, while "on average, liming is neither a consistent source nor a sink for CO₂."

- conf: not stated
- class: meas (note: "paired measurements")
- holds: Hamilton et al.'s treatments, including no-till
- src: hamiltonEvidenceCarbonSequestration2007
- trail: CB1-LIMING §5. Where the numbers

From the note:

> Their own paired measurements were not one-sided — under their no-till treatment sink strength tended positive, while "on average, liming is neither a consistent source nor a sink for CO₂."
>

**Edit type: counter**

## H1-02/filters-corrections.6

mOTUpan was checked against a few closed Prochlorococcus genomes plus bootstraps, and its authors state that genes hard to assemble or bin leave an inevitable underestimate of the accessory genomes.

- conf: not stated
- class: not stated
- holds: a few closed Prochlorococcus genomes
- src: buckMOTUpanRobustBayesian2022
- trail: H1-02 §2.7

From the note:

> CELEBRIMBOR [19] was validated on simulations, and the authors state that non-random loss violates its missing-at-random assumption. mOTUpan [14] was checked against a few closed Prochlorococcus genomes plus bootstraps, and its authors state that genes hard to assemble or bin leave "an inevitable underestimate of the accessory genomes".
>

**Edit type: counter**

## CB2/depth-axis.3

Sequencing depth is measured only as simulated per-genome coverage in targeted-assembly benchmarks, not as library depth in a real assemble-and-bin pipeline counting rRNA in MAGs: the depth axis is unmeasured for rRNA-in-MAG recovery in real data.

- conf: not stated
- class: search (note: "which I could not find anywhere")
- holds: the reviewer's searches
- src: pericardMATAMReconstructionPhylogenetic2018, philipMETASEEDNovelApproach2024
- trail: CB2-RRNA §Verdict, §5. What is measured, §Verdict on the second

From the note:

> Sequencing depth is measured, but only as simulated per-genome coverage in targeted-assembly benchmarks — not as library depth in a real assemble-and-bin pipeline counting rRNA in MAGs.
>
> Sequencing depth is directly measured, but only as simulated per-genome coverage in targeted-assembly benchmarks (Pericard et al.'s 2×–50× series; Philip et al.'s read-pair floor) — not as library depth in a real assemble-and-bin pipeline counting rRNA in MAGs, which I could not find anywhere.
>
> What nobody I found has done: subsample a *real* metagenome to a depth series, run a standard assemble-and-bin pipeline at each depth, and count how many MAGs carry a 16S gene.
>
> So: the depth axis is measured for targeted 16S reconstruction in simulation, and unmeasured for rRNA-in-MAG recovery in real data.
>

**Edit type: counter**

## 16S/abundance-distribution.7

The soil SAD shape is in partial conflict: exponential or inverse gamma (Zhou 2013) against lognormal (Shoemaker 2017; Grilli 2020); these use different fitting targets, and Haegeman 2013 argues the tail is not identifiable from sample data at all.

- conf: cont (note: "the conflict is only partial")
- class: not stated
- holds: different fitting targets
- src: zhouRandomSamplingProcess2013, shoemakerMacroecologicalTheoryMicrobial2017, grilliMacroecologicalLawsDescribe2020, haegemanRobustEstimationMicrobial2013
- trail: MB-01 §answers

From the note:

> *Conflicts:* Soil SAD shape: exponential or inverse gamma (Zhou 2013) versus lognormal (Shoemaker 2017; Grilli 2020).
>
> These use different fitting targets, so the conflict is only partial; Haegeman 2013 argues the tail is not identifiable from sample data at all.
>

**Edit type: counter**

## 16S/abundance-occupancy.4

In the two bulk-soil amplicon studies with figures (Bickel and Or 2021; Nemergut 2011), more abundant taxa occupy more soils, but the two are not fully independent (Bickel and Or reanalysed compiled datasets including the Earth Microbiome Project, which plausibly overlaps Nemergut's soils), and both measures are partly built in by construction: "total abundance" summed across samples and "common" defined on the pooled rank-abundance distribution both rise with occupancy. Whether a relationship exists beyond sampling, and how strong it is, is unresolved.

- conf: unclear (critic: MB-02:C-053)
- class: not stated
- holds: bulk-soil amplicon data; the search behind it reviewed about 25 titles
- src: bickelChosenFewVariations2021, nemergutGlobalPatternsBiogeography2011
- trail: MB-02 §critic, §Adversarial, §answers

From the note:

> **D3 (b) abundance-occupancy in soil**: In the two bulk-soil amplicon studies with figures [61,62], more abundant taxa occupy more soils.
>
> These are not fully independent: Bickel and Or reanalysed compiled datasets including the Earth Microbiome Project, which plausibly overlaps the soils Nemergut used.
>
> Both measures are partly built in by construction. 'Total abundance' summed across samples, and 'common' defined on the pooled rank-abundance distribution, both rise with occupancy, the same circularity the review flags only for Delgado-Baquerizo 2018.
>
> So whether a relationship exists beyond sampling, and how strong it is, is unresolved; 'wherever tested' overstates a search that reviewed about 25 titles.
>
> - D3(b): the circularity caution (dominance defined by abundance and ubiquity, so it cannot test the relationship) is applied to Delgado-Baquerizo 2018 but not to Bickel and Or 2021.
>
> Their common class is defined on the globally pooled rank-abundance distribution, and pooled abundance rises mechanically with prevalence.
>
> Nor is it applied to Nemergut 2011's 'total abundance versus number of soils occupied', where summed abundance also rises with occupancy.
>
> The supporting side is held to a lower bar.
>
> *Strength:* Moderate for the existence of a positive relationship in amplicon data from bulk soil (two independent studies with numbers, consistent with general macroecology).
>
> *Single-source sensitivity:* Removing Nemergut et al. 2011 [62] leaves one quantitative bulk-soil figure (Bickel and Or [61]).
>

**Edit type: setting**

## CB3/food-system.10

FAOSTAT's own share is falling and has been revised: Analytical Brief 94 reports 16.2 Gt CO2eq for 2022 against a global total of 53.5 Gt, i.e. 29.7%, "below 30 percent for the first time on record", down from 38% in 2000.

- conf: not stated
- class: not stated
- holds: 2022; FAOSTAT; global total 53.5 Gt
- src: faoGreenhouseGasEmissions2024
- trail: CB3-AG-EMISSIONS §Boundary A

From the note:

> **FAOSTAT's own share is falling and has been revised.** Analytical Brief 94 reports 16.2 Gt CO2eq for 2022 against a global total of 53.5 Gt, i.e. **29.7%**, "below 30 percent for the first time on record", down from 38% in 2000 [6].
>

**Edit type: setting**

## NFERT/manufacturing-co2.3

A process-optimisation study citing a global mix that includes coal reports about 2.8 t CO₂ per tonne of ammonia.

- conf: not stated
- class: not stated
- holds: a global plant mix including coal
- src: demirhanSustainableAmmoniaProduction2019
- trail: NFERT §Carbon dioxide per unit

From the note:

> A process-optimisation study citing a global mix that includes coal reports about 2.8 t CO₂ per tonne (Demirhan et al. 2019).
>

**Edit type: setting**

## TAXRES/gtdb.4

GTDB is bulk-downloadable and explicitly tracks consistency against NCBI taxonomy.

- conf: not stated
- class: not stated
- holds: GTDB as found by a single-pass web search on 2026-06-19
- src: parksGTDBRelease102026, parksGTDBOngoingCensus2022
- trail: TAXRES §GTDB structure

From the note:

> It is bulk-downloadable and explicitly tracks consistency against NCBI taxonomy.
>
> Searched 2026-06-19 across four angles: NCBI-vs-GTDB divergence, taxon-name resolution tools, GTDB structure/identifiers, and the GBIF/Catalogue-of-Life cross-kingdom backbone.
>

**Edit type: setting**

## H2-04/plant-axis-analogues.5

The one quantitative cross-level agreement measure found is eigenvector angles and eigenvalue ratios with permutation tests, used to show that including intraspecific variation rotates leaf trait axes.

- conf: not stated
- class: not stated
- holds: leaf trait spaces, within- versus across-species
- src: puglielliIntraspecificVariabilityLeaf2024 (abstract), puglielliQuantifyingInfluenceIntraspecific2025 (full text)
- trail: H2-04 §Genome-level versus community-level, §answers

From the note:

> The one quantitative cross-level agreement measure found is eigenvector angles and eigenvalue ratios with permutation tests, used to show that including intraspecific variation rotates leaf trait axes [24a abstract; 24b full text].
>
> (iii) Within-species versus across-species: Anderegg (abstract), Osnas (full text), Puglielli (eigenvector angles).
>

**Edit type: setting**

## H1-02/filters-corrections.8

None of the completeness-model corrections was validated against ground truth on natural-sample MAGs with real, non-random gaps, and the search found no correction so validated.

- conf: not stated
- class: search (critic: C-103)
- holds: routes: Europe PMC and WebSearch on mOTUpan, CELEBRIMBOR, MetaPathPredict, completeness bias correction and missing-at-random pangenome correction; the critic: supported by the named search routes and the authors' own stated assumptions
- src: eisenhoferImpactMicrobialGenome2023, hellewellCELEBRIMBORCoreAccessory2024, buckMOTUpanRobustBayesian2022, gellermcgrathPredictingMetabolicModules2024
- trail: H1-02 §2.7, §Search record, §Adversarial critique

From the note:

> None of these was validated against ground truth on natural-sample MAGs with real, non-random gaps.
>
> (2) A completeness or missingness correction validated on natural-sample MAGs with non-random gaps against ground truth.
>
> Routes: Europe PMC and WebSearch on mOTUpan, CELEBRIMBOR, MetaPathPredict, completeness bias correction, and missing-at-random pangenome correction.
>
> That corrections are not validated on real natural-sample MAGs is supported by the named search routes and the authors' own stated assumptions (CELEBRIMBOR, mOTUpan).
>

**Edit type: setting**

## H1-06/trait-compilations.4

Only 9.9% of continuous and 8.6% of binary traits met Goberna and Verdú's threshold for accurate phylogenetic prediction.

- conf: not stated
- class: not stated
- holds: 990 traits, SILVA r119 tree
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

**Edit type: setting**

## H1-02/chimerism.3

CheckM and GUNC contamination estimates correlated at r = 0.2.

- conf: not stated
- class: meas (note: "measured; natural")
- holds: natural MAG catalogues
- src: orakovGUNCDetectionChimerism2021
- trail: H1-02 §2.2

From the note:

> CheckM and GUNC contamination estimates correlated at r = 0.2 (measured; natural).
>

**Edit type: setting**

## H1-05/averaging.6

In HMP stool, apparent functional selection disappeared under restricted shuffles, so it was artifactual.

- conf: not stated
- class: not stated
- holds: HMP stool data [29][30]
- src: hoChallengesInterpretingFunctional2025, hoChallengesQuantifyingFunctional2024
- trail: H1-05 §3.2, §answers

From the note:

> - HMP stool: apparent selection disappeared under restricted shuffles.
>
> Other habitats: the same null found no functional selection in bromeliad communities (reanalysing [33]) and found apparent selection in HMP stool to be artifactual under restricted shuffles [29][30].
>

**Edit type: standing**

## 16S/core-microbiome.4

In common bean rhizospheres across four US regions plus a Colombian dataset, 48 bacterial and archaeal taxa were detected in every sample; fitting a neutral model to the abundance-occupancy distribution, 13.7% of bacterial and archaeal taxa deviated from neutral expectation; samples were rarefied to 31,255 reads.

- conf: not stated
- class: not stated
- holds: common bean rhizosphere; the rhizosphere neutral-deviation figure rests on this study alone; checked by the critic
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

**Edit type: standing**

## 16S/abundance-occupancy.14

No soil study was found that tests whether the observed bulk-soil abundance-occupancy relationship exceeds what sampling and detection alone would produce, so the share attributable to biology is unknown; none was found from cell counts or metagenomes, none specific to archaea, none comparing bulk soil and rhizosphere within one study, and none that is copy-number- or ploidy-corrected.

- conf: unclear (note: "the share attributable to biology is unknown")
- class: search (note: "No soil study was found")
- holds: Europe PMC query for abundance-occupancy with soil or rhizosphere and bacteria or archaea (25 hits reviewed by title, mostly core-microbiome applications); Europe PMC query for the neutral community model with bulk soil and rhizosphere
- src: none (a statement about what the search found)
- trail: MB-02 §D3.3, §answers, §critic, §Search record
- rating: "Weak for its interpretation"

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

**Edit type: standing**

## TSL/frequency-bucketing.1

Threshold bucketing is corpus-structure-dependent and unstable under heavy tails: the same 1% relative cutoff produced a 9.3% vocabulary reduction (few long documents) vs 74.1% (many short documents), and cutoffs above 4% can empty a short-text vocabulary.

- conf: single (note: "Primary evidence is one simulated-LDA study")
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

**Edit type: standing**

## CB3/n2o.6

Tian et al. 2020 gave agriculture 3.8 (2.5–5.8) Tg N yr−1 for 2007–2016 out of 7.3 (4.2–11.4) Tg N anthropogenic.

- conf: not stated
- class: not stated
- holds: 2007–2016
- src: tianComprehensiveQuantificationGlobal2020 (abstract, Table 1, methods)
- trail: CB3-AG-EMISSIONS §Boundary D

From the note:

> The 2020 predecessor gave agriculture 3.8 (2.5–5.8) Tg N yr−1 for 2007–2016 out of 7.3 (4.2–11.4) Tg N anthropogenic [7].
>

**Edit type: standing**

## 16S/pcr-efficiency.1

Documented protocols use 35 cycles in triplicate 25 uL reactions, pooling 240 ng per sample (EMP protocol, one-step), or 25 amplicon cycles plus 8 index cycles with 12.5 ng input (Illumina guide, two-step).

- conf: not stated
- class: not stated
- holds: makers' protocol and documentation; the critic checked the EMP protocol's 35 cycles in triplicate and 240 ng pooling on the live page
- src: earth16SIlluminaAmplicon (PROTOCOL), illumina16SMetagenomicSequencing (DOCUMENTATION; maker's claim)
- trail: MB-01 §3.1, §2.6, §answers, §critic
- rating: "Moderate for documented cycle numbers"

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

**Edit type: standing**

## NFERT/emission-share.4

The full synthetic-N supply chain is larger because it adds field and transport emissions: Menegat et al. (2022) estimate 1.13 Gt CO₂-equivalent for 2018, equal to 10.6% of agricultural emissions and 2.1% of global emissions.

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

**Edit type: standing**

## H2-01/neighbouring-transfer.6

In the E. coli pangenome, accessory-gene presence was predicted from other accessory genes on held-out random genomes; after filtering and removing phylogenetic signal, 16.7% of families were predictable at F1 ≥ 0.9 against a chance rate of about 1 to 1.7%.

- conf: single (marker)
- class: not stated
- holds: one species pangenome, held-out genomes
- src: beavanContingencyRepeatabilityPredictability2023 (FT; SINGLE SOURCE)
- trail: H2-01 §3.3

From the note:

> - **Gene co-occurrence across genomes.** In the E. coli pangenome, accessory-gene presence was predicted from other accessory genes on held-out random genomes; after filtering and removing phylogenetic signal, 16.7% of families were predictable at F1 ≥ 0.9 against a chance rate of about 1 to 1.7% [Beavan2024; FT; SINGLE SOURCE].
>
> Neighbouring microbial evidence concerns other quantities: taxon-to-function mappings transfer less well as reference coverage of the target habitat falls [Langille2013; Sun2020]; functional-profile classifiers transfer across studies at AUROC 0.70 to 0.89 in human gut [Wirbel2019]; gene co-occurrence across genomes predicts held-out genomes and held-out phyla, with predictability varying by phylum [Beavan2024; KonnoIwasaki2023].
>

**Edit type: standing**

## 16S/workflow-bias.7

Across 15 laboratories, variability depended most on specimen type, then DNA extraction, then handling laboratory, then bioinformatics; interlaboratory differences were substantial, and absolute diversity was not comparable between laboratories even with the same pipeline.

- conf: single (marker)
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

**Edit type: number**

## H2-01/levels-within.6

During vermicomposting, taxonomic turnover was about twelve times functional turnover.

- conf: not stated
- class: not stated
- holds: vermicomposting over time; no non-earthworm control
- src: airaFasterTurnoverTaxonomic2026 (AB; no non-earthworm control)
- trail: H2-01 §4.1

From the note:

> - Vermicomposting over time: taxonomic turnover about twelve times functional turnover [Aira2026; AB; no non-earthworm control].
>

**Edit type: number**

## H1-02/read-technology.5

Long-read activated-sludge MAGs carried full rRNA operons in 91.3% of cases.

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

**Edit type: number**

## H1-06/ph-preference.4

ASVs within single families spanned 3.7 to 4.2 pH units: Xanthobacteraceae in soil 4.01 to 8.20 (4.19 units), Chitinophagaceae in freshwater 4.63 to 8.35 (3.72 units).

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

**Edit type: number**

## H1-RES/accessory-function.5

Antarctic *Arthrobacter* strains (36 isolates) harboured 11 plasmids of 8.4 to 90.6 kb encoding UV protection and heavy metal resistance, 10 carrying conjugation modules; the plasmids showed limited similarity to mesophilic *Arthrobacter* plasmids, indicating novel replicons adapted to Antarctic conditions.

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

**Edit type: number**

## H1-RES/accessory-function.9

In *Pseudomonas* at a hexachlorocyclohexane (HCH) dumpsite, metabolic pathways were enriched strain-specifically, with an intact mobile class-I integron (3,552 bp) encoding dihydrofolate reductase in strain RL associated with a Tnp21-like transposon (95% identity); metagenomes from pond sediment and HCH-contaminated soils showed in situ enrichment of an integron-associated transposase gene (TnpA6100) with increasing HCH contamination (0.7 to 450 mg HCH g⁻¹ of soil).

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

**Edit type: number**

## 16S/quality-filtering.3

Stringent UPARSE-style filtering could significantly underestimate abundance and diversity, and newer clusterers produced up to 60% fewer spurious OTUs than UCLUST.

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

**Edit type: number**

## H2-01/neighbouring-transfer.1

PICRUSt accuracy fell with distance to the nearest reference genome (NSTI), across all samples (r = −0.4) and within each habitat (r = −0.25 to −0.82); accuracy was high in soils (0.81) and low in a hypersaline mat (reported 0.25, mean NSTI 0.23).

- conf: not stated
- class: meas (marker)
- holds: 16S-based prediction of metagenome functions across habitats
- src: langillePredictiveFunctionalProfiling2013 (FT; measured)
- trail: H2-01 §3.3

From the note:

> - **Taxon-to-function mappings transferred across habitats.** PICRUSt accuracy fell with distance to the nearest reference genome (NSTI), across all samples (r = −0.4) and within each habitat (r = −0.25 to −0.82); accuracy was high in soils (0.81) and low in a hypersaline mat (reported 0.25, mean NSTI 0.23) [Langille2013; FT; measured].
>

**Edit type: number**

## H1-RES/redundancy.14

Several soil metagenomic and gradient studies report strong correlations between taxonomic and functional beta diversity, implying limited redundancy for certain functions or across certain gradients; this counter-evidence tends to arise across strong environmental contrasts (biome type, precipitation extremes, contamination), where selection shapes taxa and functions in parallel.

- conf: not stated
- class: not stated
- holds: the four counter-evidence studies
- src: fiererCrossbiomeMetagenomicAnalyses2012, tripathiTrendsTaxonomicFunctional2017, liangTaxonomicFunctionalBiogeography2024, renComparisonMicrobialTaxonomic2016
- trail: H1-RES §Soil counter-evidence

From the note:

> - **Covariation** Several well-cited soil metagenomic and gradient studies report strong correlations between taxonomic and functional beta diversity, implying limited redundancy for certain functions or across certain environmental gradients [8] [9] [10] [11].
>
> - **Context dependence** Counter-evidence often arises across strong environmental contrasts (biome type, precipitation extremes, contamination), where selection shapes both taxa and functions in parallel [8] [9] [11].
>

**Edit type: hedge**

## TAXRES/gtdb-ncbi-divergence.5

Many microbiologists still use the older phylum names.

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

**Edit type: hedge**

## H1-06/moisture-preference.4

Lennon et al. 2012 is the only direct rank-resolved measurement of a moisture optimum the review found.

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

**Edit type: hedge**

## H2-01/other-field-transfer.11

In other fields covariation transfers partly, and each quantitative result is a single study.

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

**Edit type: hedge**

## 16S/abundance-distribution.21

Tropical soils are among the least-covered communities by Nonpareil estimates.

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

**Edit type: hedge**

## H2-04/complementarity-overlap.11

Pairwise metabolic models predict that cooperative potential peaks at moderate overlap.

- conf: not stated
- class: model (marker)
- holds: pairwise models
- src: freilichCompetitiveCooperativeMetabolic2011 (AB; modelled)
- trail: H2-04 §Complementarity versus overlap

From the note:

> Pairwise models predict cooperative potential peaks at moderate overlap [10c, AB; modelled], and costless secretions create broad cross-feeding opportunities [24d, AB; modelled].
>

**Edit type: hedge**

## TAXRES/name-resolution.5

The matching problem (synonyms, fuzzy matching of misspellings, homonyms via context) is largely handled; the unsolved part is a curation choice, which authority's lineage to adopt, not a matching failure: name resolution is the easy part and the authority choice the hard part.

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

**Edit type: hedge**

## 16S/abundance-distribution.25

Not found for soil: metagenome-based taxon abundance distributions reported as a distribution, copy-number- or ploidy-corrected abundance distributions, and rhizosphere-specific abundance distributions.

- conf: not stated
- class: search (note: "none found as such")
- holds: MB-02's searches
- src: none (a statement about what the search found)
- trail: MB-02 §answers

From the note:

> *Not measured:* Cell-count-based taxon abundance distributions in soil; metagenome-based taxon abundance distributions (marker-gene or genome coverage) in soil reported as a distribution; copy-number- or ploidy-corrected abundance distributions for soil; rhizosphere-specific abundance distributions (none found as such).
>

**Edit type: hedge**

## 16S/workflow-bias.5

Per-step magnitudes mostly come from one or two small mocks (7 to 20 taxa), often on 454 or Ion Torrent.

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

**Edit type: hedge**

## TSL/phrase-and-multilingual-tail.1

The review has no surviving claims on single-word vs multi-word phrase selection, or on stopword / multilingual handling at the rare-term tail (brief item 5); these are unanswered by this corpus.

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

**Edit type: hedge**

## H2-01/direct-dimension.12

Cluster number is not an intrinsic-dimension estimate; the three KO clusters are reported only as a nearest precedent.

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

**Edit type: hedge**

## H2-01/gene-set-aggregation.1

In HMP gut samples, single-copy-gene normalisation raised pathway coefficients of variation relative to relative normalisation.

- conf: single (note: "SINGLE SOURCE for this set of quantities")
- class: not stated
- holds: HMP gut samples, KEGG pathways
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

**Edit type: hedge**

## 16S/rarefying.6

In Weiss 2017, rarefying clustered samples better for presence/absence metrics, and other normalisations were vulnerable below about 1,000 reads per sample.

- conf: repl (marker)
- class: model (marker)
- holds: simulations
- src: weissNormalizationMicrobialDifferential2017 (FT; model; repl)
- trail: MB-01 §5.3

From the note:

> In Weiss 2017, rarefying clustered samples better for presence/absence metrics, and other normalisations were vulnerable below about 1,000 reads per sample (Weiss 2017) [FT; model; repl].
>

**Edit type: hedge**

## 16S/ploidy.4

Growth-rate-dependent merodiploidy: E. coli has 6.8 origins and 1.7 termini per cell at 25 min doubling but 2.5 origins and 1.2 termini at 103 min; B. subtilis (5.9 origins, 1.2 termini) and three soil Bacillus and Paenibacillus isolates are mero-oligoploid in exponential phase and down-regulate origins in stationary phase.

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

**Edit type: hedge**

## H1-RES/pangenome.20

In *Erwinia amylovora*, comparative analysis of 12 strains revealed a pangenome with approximately 89% conserved core genes.

- conf: not stated
- class: not stated
- holds: 12 *E. amylovora* strains
- src: none (cited only as SC1 [44]; the note gives no reference list)
- trail: H1-RES §Counter-Evidence: Taxa

From the note:

> Other pathogens with restricted accessory fractions include *Erwinia amylovora*, where comparative analysis of 12 strains revealed a pangenome with approximately 89% conserved core genes [44].
>

**Edit type: hedge**

## 16S/zeros.1

In simulation, simple count models sufficed across four zero-generating processes, and zero inflation was warranted only under narrow conditions.

- conf: single (marker)
- class: model (marker)
- holds: simulation; abstract only
- src: silvermanNaughtAllZeros2020 (AB; model; single)
- trail: MB-01 §4.3, §answers

From the note:

> **Zeros.** In simulation, simple count models sufficed across four zero-generating processes, and zero inflation was warranted only under narrow conditions (Silverman 2020) [AB; model; single].
>
> Zero-inflated models were warranted only under narrow conditions (Silverman 2020, abstract).
>

**Edit type: hedge**

## H1-06/metabolic-depth.3

Oxygenic photosynthesis had a median tau_D of about 0.10 to 0.11 (one clade).

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

**Edit type: hedge**

## H2-01/compositional-closure.1

Correlation is not a valid association measure for relative data; proportionality is offered instead.

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

**Edit type: hedge**

## H1-RES/pangenome.6

In 30 *E. coli* genomes core genes accounted for about 50% of total genes, with approximately 146 strain-specific genes per strain.

- conf: not stated
- class: not stated
- holds: 30 *E. coli* genomes
- src: none (cited only as SC1 [29]; the note gives no reference list)
- trail: H1-RES §Confirming Evidence Across

From the note:

> Analysis of 30 *E. coli* genomes found core genes accounted for about 50% of total genes, with approximately 146 strain-specific genes per strain [29].
>

**Edit type: hedge**

## 16S/technical-variation.10

Batch-correction tools exist, and their makers claim they work.

- conf: not stated
- class: not stated
- holds: makers' claims; abstracts only
- src: gibbonsCorrectingBatchEffects2018 (AB), lingBatchEffectsRemoval2022 (AB)
- trail: MB-01 §4.3

From the note:

> - Batch-correction tools exist; their makers claim they work (Gibbons 2018; Ling 2022) [AB].
>

**Edit type: hedge**

## 16S/primers.12

The makers of PCR clamps state that clamps enrich microbial sequences "without introducing bias".

- conf: not stated
- class: not stated
- holds: a maker's claim; abstract only
- src: lundbergPracticalInnovationsHighthroughput2013 (AB; makers' claim)
- trail: MB-01 §2.3

From the note:

> The makers of PCR clamps state that clamps enrich microbial sequences "without introducing bias" (Lundberg 2013) [AB; makers' claim].
>

