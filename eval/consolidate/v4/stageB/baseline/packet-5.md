# Faithfulness check: 60 entries

## H2-04/genome-linkage.6 (claim)

No source was found that quantifies the effect of contamination on measured within-genome linkage.

- conf: not stated
- class: search (critic: H2-04:C-089)
- holds: the review's search routes; the critic names MAG contamination and chimerism work not covered
- src: none (a search result)
- trail: H2-04 §Linkage within genomes, §Adversarial critique

From the note:

> - gap: Contamination and chimerism in MAGs that bear on measured within-genome linkage (e.g., Shaiber & Eren 2019 mBio on composite MAGs; GUNC chimerism estimates; CheckM). The review says no source was found.; setting_or_class: Genome-resolved metagenomics; MAG quality; direction: D1 cautions on linkage
>

## H1-02/dns.5 (do not say)

"The main mechanism was therefore mis-binning among co-occurring relatives, not a failure to sequence."

- why: the critic: the reviewer's inference, which over-reads the source; the low-identity share of missed genes is attributed to sequence divergence or assembly errors, and mis-binned genes were only part of those without homologs
- instead: same-sample-isolate.4, same-sample-isolate.5, same-sample-isolate.6
- trail: H1-02 §2.1, §critic, §Adversarial critique

From the note:

> The main mechanism was therefore mis-binning among co-occurring relatives, not a failure to sequence.
>
> (iii) The claim that 'the main mechanism was therefore mis-binning' over-reads [1].
>
> - Section 2.1 states 'The main mechanism was therefore mis-binning among co-occurring relatives'.
>
> That is the reviewer's inference.
>
> [1] attributes low-identity missed genes to sequence differences from the isolate or to assembly errors, so part of the 'loss' may be biology and not recovery.
>

## H2-01/heldout-study.7 (claim)

Shared pathway members, strong common factors and a lenient threshold make the 59% replication an optimistic reading of transfer.

- conf: not stated
- class: reading (note: "Cautions (reviewer's reading)")
- holds: Chen2020; the critic: the review applies this caution to the replication result but not to the temporal stability or the between-cohort comparison
- src: none (the reviewer's reading of Chen2020)
- trail: H2-01 §answers, §3.2, §critic

From the note:

> Shared pathway members, strong common factors and a lenient threshold make this an optimistic reading of transfer.
>
> Cautions (reviewer's reading): MetaCyc pathways share reactions and contributing species, so pathway-pathway co-abundance partly reflects shared members. 43,355 of about 58,653 possible pathway pairs were significant in at least one cohort, which points to strong common factors that would make replication easy.
>
> "Replicated at P < 0.05" with n = 77 is a lenient bar.
>
> - Chen2020: the review applies the 'lenient bar, strong common factors, shared members' caution to the replication result (59%), which argues against easy transfer.
>

Not found in the cited text (where to look, not what is wrong): holds: between-cohort

## H2-01/function-definition.5 (claim)

Failure modes to expect in this literature: dimension estimates dominated by a mean profile; a genome-size axis that is partly technical; covariation between gene sets that share members; per-sample correlation metrics that ignore across-sample variance; comparisons of tables at different granularity; covariation inherited from imputation (plant traits); and replication judged against lenient thresholds with strong common factors (Chen2020).

- conf: not stated
- class: not stated
- holds: the literature reviewed for all three directions
- src: none (the reviewer's synthesis)
- trail: H2-01 §5. How

From the note:

> Failure modes a reader should expect in this literature: dimension estimates dominated by a mean profile; a genome-size axis that is partly technical; covariation between gene sets that share members; per-sample correlation metrics that ignore across-sample variance; comparisons of tables at different granularity; covariation inherited from imputation (plant traits); and replication judged against lenient thresholds with strong common factors (Chen2020).
>

Not found in the cited text (where to look, not what is wrong): holds: reviewed

## 16S/taxonomic-assignment.2 (claim)

Cross-validated by identity to the reference, all tested classifiers were at most 50% accurate on V4: genus accuracy was about 100% at 100% identity and about 50% at 97%; the author argues that mocks overstate accuracy because all their members are named type strains. This rests on one author, who also develops competing classifiers.

- conf: single (marker)
- class: meas (marker)
- holds: reference sets; accuracy depends on distance to reference
- src: edgarAccuracyTaxonomyPrediction2018 (FT; meas; single)
- trail: MB-01 §2.12, §answers, §2. Steps, §Adversarial

From the note:

> **Accuracy.** Cross-validated by identity to the reference, all tested classifiers were at most 50% accurate on V4.
>
> Genus accuracy was about 100% at 100% identity and about 50% at 97% (Edgar 2018b) [FT; meas; single].
>
> The author argues that mocks overstate accuracy because all their members are named type strains.
>
> Taxa and labels: V4 genus accuracy was about 50% at 97% identity to the reference (Edgar 2018b, derived from reference sets).
>
> | Classification | n/a | V4 genus accuracy about 50% at 97% identity. 56 to 88% false genus names with closed reference | Depends on distance to reference | Edgar 2018b; Edgar 2017a |
>
> - Section 2.12: V4 genus accuracy of about 50% at 97% identity and 10 to 17% database annotation error rest on Edgar 2018b and 2018c, from one author who also develops competing classifiers. Flagged single in the text but used in the D2 answer without that qualifier.
>

## H2-01/levels-within.14 (claim)

Whether the greater stability of function levels is biological rather than processing-driven is weakly supported: none of the studies controls for normalisation, aggregation and granularity together.

- conf: not stated
- class: not stated
- holds: same-habitat studies of case A
- src: none (the reviewer's synthesis)
- trail: H2-01 §answers
- rating: "weak for the claim that the stability is biological rather than processing-driven"

From the note:

> *Strength:* Moderate for the direction as reported, weak for the claim that the stability is biological rather than processing-driven.
>
> Several independent studies agree, but none controls for normalisation, aggregation and granularity together..
>

Not found in the cited text (where to look, not what is wrong): holds: same-habitat

## NFERT/free-living-fixation.1 (claim)

Free-living and associative diazotrophs are ubiquitous and do fix nitrogen, but their measured contribution in cereal systems is modest, and engineering cereals to fix their own nitrogen remains unrealised.

- conf: not stated
- class: not stated
- holds: cereal systems
- src: ladhaBiologicalNitrogenFixation2022
- trail: NFERT §The weak channel

From the note:

> Free-living and associative diazotrophs are ubiquitous and do fix nitrogen, but their measured contribution in cereal systems is modest, and engineering cereals to fix their own nitrogen remains unrealised (Ladha et al. 2022).
>

## H2-01/dimension-comparison.1 (claim)

The low dimension estimates (Jiang2012, Piton2023's two leading axes, Heimberg2016) and the higher ones (Fahimipour2020 across genomes, Lenz2016 across datasets, Piton's remaining half of variance) largely reflect different objects (samples against genomes) and different criteria (within-dataset variance against cross-dataset stability), not direct contradiction on the same data.

- conf: not stated
- class: not stated
- holds: the sources of D1, which differ in object (taxa as rows, or non-microbial samples, for the related work)
- src: jiangFunctionalBiogeographyOcean2012, pitonLifeHistoryStrategies2023, heimbergLowDimensionalityGene2016, fahimipourMappingBacterialMetabolic2020a, lenzPrincipalComponentsAnalysis2016
- trail: H2-01 §answers, §2.4

From the note:

> *Conflicts:* Low (Jiang2012, Piton2023's two leading axes, Heimberg2016) against higher (Fahimipour2020 across genomes; Lenz2016 across datasets; Piton's remaining half of variance).
>
> These largely reflect different objects (samples against genomes) and different criteria (within-dataset variance against cross-dataset stability), not direct contradiction on the same data..
>
> These are different objects (taxa as rows, or non-microbial samples) and are reported as related work.
>

Not found in the cited text (where to look, not what is wrong): holds: d1; holds: in

## CB2/dns.3 (do not say)

"MAG-only clusters share 93% 16S identity against 99.8% for RefSeq" (Hiseni et al.) as an established figure.

- why: the note: the same caveat applies (no methods section)
- instead: catalogue-recovery.7
- trail: CB2-RRNA §1. Measured recovery

From the note:

> Hiseni et al. also report that 97.5%-ANI clusters composed purely of MAGs share on average 93% 16S identity, while clusters of complete RefSeq genomes share 99.8% — an anomaly for a gene that conserved, and their argument that the 16S sequences MAGs *do* carry are often wrong.
>
> Same caveat applies.
>

Not found in the cited text (where to look, not what is wrong): "MAG-only clusters share 93% 16S identity against 99.8% for RefSeq"

## TAXRES/gtdb-ncbi-divergence.1 (claim)

GTDB and NCBI Taxonomy / LPSN classify on different bases, so the same organism can get a different lineage.

- conf: not stated
- class: not stated
- holds: prokaryotes
- src: anonHarmonizingProkaryoticNomenclature2022, parksGTDBOngoingCensus2022
- trail: TAXRES §The NCBI-vs-GTDB divergence

From the note:

> Different bases, so the same organism can get a different lineage.
>
> - **GTDB** classifies by **relative evolutionary divergence (RED)** from genome similarity, rank-normalised; **NCBI Taxonomy and LPSN** follow the International Code of Nomenclature of Prokaryotes (ICNP).
>

## H2-01/cwm.5 (claim)

Abundance-weighted and unweighted trait moments disagreed in sign, significance or both for 71% of forest trait-climate results.

- conf: not stated
- class: not stated
- holds: forest plots worldwide
- src: wieczynskiClimateShapesShifts2018 (AB)
- trail: H2-01 §4.4

From the note:

> - Weighting changes level comparisons: abundance-weighted and unweighted trait moments disagreed in sign, significance or both for 71% of forest trait-climate results [Wieczynski2019; AB], and CWM accuracy depended on trait coverage of the community [Borgy2017; AB].
>

Not found in the cited text (where to look, not what is wrong): holds: plots

## CB3/dns.3 (do not say)

"About 5% of global emissions, whether counted as soil N2O, all N2O or emissions outside the farm gate."

- why: the note says the three near-5% boundaries "are not interchangeable"
- instead: five-percent.2
- trail: CB3-AG-EMISSIONS §Verdict: which boundary

From the note:

> **No boundary in the current authoritative literature produces exactly five per cent for agriculture, and none produces it for agricultural soils.** Three boundaries land close enough that a "roughly 5%" claim could have originated from any of them, and they are not interchangeable:
>

Not found in the cited text (where to look, not what is wrong): "About 5% of global emissions, whether counted as soil N2O, all N2O or emissions outside the farm gate."

## 16S/extraction.2 (claim)

In McLaren's reanalysis of Brooks's 80 cell mixtures of 7 vaginal taxa (V1-V3, 454), the extraction step had a maximum pairwise bias of 36.6-fold and a mean of 5.5-fold, PCR a maximum of 5.2 and a mean of 2.3, and sequencing plus classification a maximum of 1.6 and a mean of 1.2; total bias in the cell mixtures was a maximum of 29.3-fold and a mean of 5.6-fold.

- conf: single (marker)
- class: deriv/model (marker)
- holds: one dataset, 7 vaginal taxa as cell mixtures, V1-V3 on 454 (Brooks 2015 data); figures checked against the full text by the synthesis agent and the critic
- src: mclarenConsistentCorrectableBias2019 (FT, re-opened; deriv/model; single dataset), brooksTruthMetagenomicsQuantifying2015
- trail: MB-01 §2.2, §answers, §critic

From the note:

> **Magnitude in a defined mock.** McLaren et al. reanalysed Brooks et al.'s 80 cell mixtures of 7 vaginal taxa (V1-V3, 454) (McLaren 2019) [FT, re-opened; deriv/model; single dataset].
>
> The extraction step had a maximum pairwise bias of 36.6-fold and a mean of 5.5-fold.
>
> PCR followed (max 5.2, mean 2.3), then sequencing and classification (max 1.6, mean 1.2).
>
> Total bias in cell mixtures was a maximum of 29.3-fold and a mean of 5.6-fold.
>
> RA: the largest single step in a 7-taxon vaginal mock.
>
> Maximum pairwise bias was 36.6-fold and the mean 5.5-fold (McLaren 2019 reanalysis of Brooks 2015; derived).
>
> | Extraction | Largest single step in a 7-taxon mock (max 36.6-fold, mean 5.5-fold pairwise).
>
> Verified against full text: McLaren 2019 per-step bias table (36.6 and 29.3 max, 5.5 and 5.6 mean), Silverman 2021 (2.6-fold, about 19% of taxa more than 4-fold, mis-set annealing machine), Sze and Schloss 2019 (R2 0.79, 0.044, 0.033; chimera rates 0.9 to 18.2%), Schloss 2024b (Table 1 read ranges, coverage-based iNEXT passage, Good's coverage 89.4 to 99.8%), Karstens 2019, Fitzpatrick 2018, Thompson 2017, Song 2016, Starke 2021, Louca 2018, Laursen 2017, Wen 2017, Weiss 2017, Nearing 2018 and 2022, Wirbel 2024, Zemb 2020, Glassman 2018, Chiarello 2022, Stoddard 2015, Vetrovsky 2013, Kembel 2012, Hornung 2019, Lennon 2018, Barlow 2020 and Dyrhovden 2021.
>

## H1-02/sample-dependence.10 (claim)

In sediment, dependence was not measured in this setting: the only data are MAG yield against depth in one estuarine data set and habitat-level yield for coastal sediments, and nothing was found on content artefacts.

- conf: not stated
- class: search (critic: C-012)
- holds: natural sediment; MAG yield only
- src: royaltyTheoreticalSimulationBasedInvestigation2019, sereikaGenomeresolvedLongreadSequencing2025
- trail: H1-02 §critic, §Verdict as delivered, §5. Verdicts, §3.4

From the note:

> Part B, soil and sediment: NOT MEASURED IN THIS SETTING, with indirect recovery-quality evidence only.
>
> Dependence on sample properties: sediment (natural)**: NOT MEASURED IN THIS SETTING.
>
> The only data are MAG yield against depth in one estuarine data set [16] and habitat-level yield for coastal sediments [17].
>
> - Sediment: **not measured in this setting** (yield only [16, 17]).
>
> Nothing was found on content artefacts.
>

## 16S/intragenomic-variation.1 (claim)

Intragenomic variants split genomes into several ASVs: 0.58 variants per copy for full-length 16S and 0.25 for V4.

- conf: cont (marker)
- class: deriv (marker)
- holds: genome-based analysis
- src: schlossAmpliconSequenceVariants2021 (FT; deriv; cont)
- trail: MB-01 §2.5, §answers

From the note:

> **Effect on taxa detected.** Intragenomic variants split genomes into several ASVs: 0.58 variants per copy for full-length 16S and 0.25 for V4 (Schloss 2021) [FT; deriv; cont].
>
> Taxa: ASVs split genomes into 0.25 variants per copy on average for V4 (Schloss 2021, derived).
>
> Correction did not improve fit to 10 mocks | ASVs split genomes (V4 0.25 variants per copy) | Correction accuracy varies with divergence from sequenced genomes | McLaren 2019; Starke 2021; Louca 2018; Schloss 2021 |
>

Not found in the cited text (where to look, not what is wrong): holds: genome-based

## GHOST/joint-reconstruction.1 (claim)

"Attribute-missing graph" methods jointly reconstruct attributes and update structure via alternating optimisation (EGS), rather than fixed mean/zero imputation on a static graph.

- conf: not stated
- class: not stated
- holds: a method description; no setting given
- src: chenLearningAttributeMissingGraphs2022, songDynamicGraphStructure2025
- rating: "Confidence: high (3-0 / 2-1)"
- trail: GHOST §1. Strategies

From the note:

> - **Dynamic / joint reconstruction.** "Attribute-missing graph" methods that jointly reconstruct attributes *and* update structure via alternating optimisation (EGS), rather than fixed mean/zero imputation on a static graph [R3, R4].
>
> *Confidence: high (3-0 / 2-1).*
>

## CB2/mimag-hq.1 (claim)

The MIMAG high-quality bar requires 5S, 16S and 23S rRNA plus ≥18 tRNAs on top of ≥90% completeness and ≤5% contamination.

- conf: not stated
- class: not stated
- holds: the standard as applied in the catalogue papers the review cites
- src: bowersMinimumInformationSingle2017
- trail: CB2-RRNA §1. Measured recovery

From the note:

> The most reliable figures come from catalogue papers that report how many of their genomes clear the MIMAG high-quality bar, which requires 5S, 16S and 23S rRNA plus ≥18 tRNAs on top of ≥90% completeness and ≤5% contamination [Bowers et al. 2017, as applied in the sources below].
>

Not found in the cited text (where to look, not what is wrong): holds: review

## 16S/copy-number.21 (claim)

Copy number tracks ecological strategy: soil isolates that formed colonies quickly averaged 5.5 copies and slow responders 1.4.

- conf: single (critic: MB-01:C-091)
- class: meas (marker)
- holds: soil isolates; one abstract-only study; MB-02 calls it a measured association, cited as context
- src: klappenbachRRNAOperonCopy2000 (AB; meas; repl)
- trail: MB-01 §3.2, §answers, §Adversarial, MB-02 §D1.2

From the note:

> - Copy number tracks ecological strategy.
>
> Fast-colonising soil isolates averaged 5.5 copies against 1.4 for slow responders (Klappenbach 2000) [AB; meas; repl].
>
> Fast-responding soil isolates averaged 5.5 copies against 1.4 for slow responders (Klappenbach 2000, abstract).
>
> - D3 answer: 'Fast-responding soil isolates averaged 5.5 copies against 1.4' rests on one abstract-only study (Klappenbach 2000).
>
> Copy number also tracks life history.
>
> Soil isolates that formed colonies quickly averaged 5.5 copies and slow responders 1.4 [9, AB].
>
> These are measured associations, cited here only as context for which soil taxa sit at which end of the range.
>

Not found in the cited text (where to look, not what is wrong): holds: mb-02

## H1-RES/n-cycle-hgt.15 (claim)

Jones et al. (2008): codon usage and G+C content analyses showed no evidence for recent HGT of any denitrification gene, and the close proximity of denitrification gene copies in several genomes suggested duplication rather than horizontal acquisition; HGT cannot be ruled out, but gene duplication and divergence and lineage sorting may have influenced each denitrification gene differently.

- conf: not stated
- class: not stated
- holds: denitrification genes in the genomes analysed
- src: jones2008
- trail: H1-RES §Counter-Evidence: Vertical

From the note:

> Codon usage and G+C content analyses showed no evidence for recent HGT of any denitrification genes, and the close proximity of denitrification gene copies in several genomes suggested duplication rather than horizontal acquisition [13].
>
> The study concluded that while HGT cannot be ruled out, alternative processes such as gene duplication/divergence and lineage sorting may have differently influenced the evolution of each denitrification gene [13].
>

## H1-02/sequencing-depth.4 (claim)

One estuarine sediment rarefaction gave a lag of 3.7 Gbp and the lowest maximum MAG yield.

- conf: not stated
- class: not stated
- holds: natural sediment, one data set; MAG yield
- src: royaltyTheoreticalSimulationBasedInvestigation2019
- trail: H1-02 §3.4

From the note:

> The only evidence is one estuarine sediment rarefaction (MAG yield; lag 3.7 Gbp, lowest maximum yield) [16] and habitat-level yield for coastal sediments [17].
>

## CB3/five-percent.7 (claim)

A figure near 5% is three to eight times smaller than any of those, and can only belong to a soils- or N2O-specific boundary.

- conf: not stated
- class: not stated
- holds: the ranges in five-percent.6
- src: none (the reviewer's synthesis)
- trail: CB3-AG-EMISSIONS §Verdict: which boundary

From the note:

> A figure near 5% is three to eight times smaller than any of those, and can only belong to a soils- or N2O-specific boundary.
>

Not found in the cited text (where to look, not what is wrong): holds: in; holds: five-percent.6

## NFERT/manufacturing-energy.3 (claim)

Energy requirements fell from about 55 GJ per tonne of ammonia in the 1950s to the high-20s today.

- conf: not stated
- class: not stated
- holds: the 1950s to the present
- src: tunaTechnoEconomicAssessment2014
- trail: NFERT §Energy per unit

From the note:

> The historical trajectory is steep: requirements fell from about 55 GJ per tonne in the 1950s to the high-20s today (Tunå et al. 2014).
>

## CB1/consumption.9 (claim)

Of more than 200,000 UK soil analyses collated for 2013/14, about 40% of arable soils were below the recommended pH 6.5 and 57% of grassland soils below pH 6.0.

- conf: not stated
- class: not stated
- holds: UK soil tests, 2013/14
- src: gouldingSoilAcidificationImportance2016
- trail: CB1-LIMING §2. Consumption

From the note:

> The stated cause is economic — "although a short-term saving, reducing or omitting the application of lime to correct acidity risks significant economic loss" — and the consequence shows in soil tests: of more than 200,000 analyses collated for 2013/14, about 40% of arable soils were below the recommended pH 6.5 and 57% of grassland soils below pH 6.0 [7].
>

Not found in the cited text (where to look, not what is wrong): UK; holds: uk

## H1-06/temperature-preference.1 (claim)

Within the phylum Thermotogota, optimal growth temperature has strong phylogenetic signal (Pagel's lambda 0.93), yet ancestral reconstruction places several secondary shifts to mesophily and hyperthermophily.

- conf: not stated
- class: deriv (critic: C-004)
- holds: 64 Thermotogota genomes; within one phylum
- src: farrellBacterialGrowthTemperature2024
- trail: H1-06 §2. Part A1, §answers, §critic

From the note:

> **Temperature.** Within the phylum Thermotogota (64 genomes), optimal growth temperature has strong signal (Pagel's lambda 0.93), yet ancestral reconstruction places several secondary shifts to mesophily and hyperthermophily.
>
> Temperature optimum is strongly signalled within one phylum (Thermotogota, lambda 0.93) yet shifted several times, with horizontally acquired genes.
>
> Temperature is inferred within one phylum (Farrell).
>

## CB3/synthetic-fertiliser.5 (claim)

An author correction to Menegat et al. 2022 exists but concerns figure axis labels and a supplementary table, not the headline.

- conf: not stated
- class: not stated
- holds: the correction's abstract or publisher metadata
- src: menegatAuthorCorrectionGreenhouse2022 (abstract or publisher metadata)
- trail: CB3-AG-EMISSIONS §Boundary D

From the note:

> (Abstract read only; an author correction exists but concerns figure axis labels and a supplementary table, not the headline [13a].)
>

## H1-RES/taxonomy-function.7 (claim)

Whether taxonomy predicts nitrogen-cycle functions depends on the gene and clade: for nosZ, particularly in nirK-harbouring organisms, taxonomy is a reasonable proxy for gene presence and phylogenetic relationships; for core nif genes (NifHDKEN) in clades with conserved operons and congruent phylogenies it is a strong predictor of nitrogen-fixation capacity; for nirK and norB it is a poor predictor because of extensive HGT and habitat-based clustering; and in *Paenibacillus* and free-living *Bradyrhizobium*, horizontal acquisition of functional modules decouples nitrogen-fixation capacity from core genome phylogeny.

- conf: not stated
- class: not stated
- holds: the Sub-claim 3 genes and clades
- src: jones2008, hirsch1995, heylen2006, garbeva2007, heylen2007, tao2021, xie2014
- trail: H1-RES §Gene-Specific

From the note:

> The implications for using taxonomy to predict nitrogen-cycle functions depend on the specific gene and clade.
>
> For nosZ, particularly in nirK-harboring organisms, taxonomy provides a reasonable proxy for gene presence and phylogenetic relationships [13].
>
> For core nif genes (NifHDKEN) in clades with conserved operons and congruent phylogenies, taxonomy is a strong predictor of nitrogen-fixation capacity [18].
>
> However, for nirK and norB, taxonomy is a poor predictor due to extensive HGT and habitat-based clustering [2] [7] [16].
>
> For nif genes in taxa like *Paenibacillus* and free-living *Bradyrhizobium*, horizontal acquisition of functional modules means that nitrogen-fixation capacity is decoupled from core genome phylogeny [6] [9].
>

Not found in the cited text (where to look, not what is wrong): holds: sub-claim; holds: 3

## 16S/taxonomic-assignment.3 (claim)

On mocks, the q2-feature-classifier methods reached median genus F above 0.8.

- conf: not stated
- class: meas (marker)
- holds: mocks; developer claim
- src: bokulichOptimizingTaxonomicClassification2018 (FT; meas; developer claim)
- trail: MB-01 §2.12, §answers

From the note:

> On mocks, the q2-feature-classifier methods reached median genus F above 0.8 (Bokulich 2018) [FT; meas; developer claim].
>
> On mocks, genus median F exceeded 0.8 (Bokulich 2018); Edgar 2018b argues that mocks overstate accuracy.
>

## H1-05/dns.6 (do not say)

"Aggregation alone lowers functional variability, so 'function lower' is not by itself evidence of redundancy", as a methodological point bearing on every soil study, or "Ho and Huang show analytically and by simulation" with a 'Moderate' rating.

- why: it rests on Ho and Huang [29][30] only and is modelled; the 'Moderate' firmness rests on a summary of the preprint, the published version having been read as abstract only (access)
- instead: averaging.1, averaging.10
- trail: H1-05 §Adversarial critique

From the note:

> Moderate as a methodological point, but single source: Ho and Huang [29][30] show analytically and by simulation that aggregation alone lowers functional variability, so 'function lower than taxonomy' is not by itself evidence of redundancy or selection.
>
> - [29] Cell Systems version: abstract only, yet the D3 answer says the method 'shows analytically and by simulation' and rates it 'Moderate'. That firmness rests on a summary of the preprint.
>
> - D3: 'aggregation alone lowers functional variability, so function lower is not by itself evidence of redundancy' is framed as a methodological point bearing on every soil study. It rests on Ho and Huang [29][30] only, and is modelled.
>

Not found in the cited text (where to look, not what is wrong): "Aggregation alone lowers functional variability, so 'function lower' is not by itself evidence of redundancy"; "Ho and Huang show analytically and by simulation"

## H1-06/taxonomies.1 (claim)

Rank-wise analyses of community composition use taxonomies, not trees, and the taxonomy differs between studies: Greengenes, SILVA or RDP, GTDB, a curated gyrB taxonomy, or no ranks at all, only sequence-identity thresholds.

- conf: not stated
- class: not stated
- holds: the studies the review read: Greengenes (Lu 2016); SILVA or RDP (Ramoneda 2023, Lennon 2012, Isobe 2019); GTDB (López-Mondéjar 2022, Royalty and Steen 2019, Hoffert 2026, Barnum 2024); gyrB (Mayjonade 2024); identity thresholds only (Bay 2020, Quiroga 2022, Schmidt 2014)
- src: luEvaluatingCommunityenvironmentRelationships2016, ramonedaBuildingGenomebasedUnderstanding2023, lennonMappingNicheSpace2012, isobePhylogeneticConservationBacterial2019, lopezmondejarGlobalDistributionCarbohydrate2022, royaltyQuantitativelyPartitioningMicrobial2019, hoffertConstructingPeriodicTable2026, barnumPredictingMicrobialGrowth2024, mayjonadeRelativeEffectsAbiotic2024, baySoilBacterialCommunities2020, quirogaEcologicalAssemblyBacterial2022, schmidtEcologicalConsistencySSU2014
- trail: H1-06 §1. What is being compared

From the note:

> Rank-wise analyses of community composition use taxonomies, not trees, and the taxonomy differs between studies: Greengenes [23], SILVA or RDP [13, 14, 19], GTDB [5, 6, 8, 12], a curated gyrB taxonomy [24], or no ranks at all, only sequence-identity thresholds [25, 26, 27].
>

Not found in the cited text (where to look, not what is wrong): holds: review; holds: lu; holds: 2016; holds: ramoneda; holds: 2023; holds: lennon; holds: 2012; holds: isobe; holds: 2019; holds: lópez-mondéjar; holds: 2022; holds: royalty; holds: steen; holds: hoffert; holds: 2026; holds: barnum; holds: 2024; holds: mayjonade; holds: bay; holds: 2020; holds: quiroga; holds: schmidt; holds: 2014

## H1-02/artefact-size.3 (claim)

The first layer of the question, how far recovery changes the called gene or pathway content of a recovered genome, has direct measurements, although few.

- conf: not stated
- class: not stated
- holds: incompleteness, contamination, failure to assemble or bin variable and mobile regions, uneven annotation
- src: none (the reviewer's synthesis)
- trail: H1-02 §1. Scope

From the note:

> The first asks how far recovery (incompleteness, contamination, failure to assemble or bin variable and mobile regions, uneven annotation) changes the called gene or pathway content of a recovered genome.
>
> The first layer has direct measurements, although few.
>

## H2-04/dns.22 (do not say)

The community axes of Piton 2023 as identical to isolate-based trait axes.

- why: Piton's own caveat and the asserted compression of community-average rRNA copy number variance cut against reading the qualitative agreement as axis identity
- instead: axis-agreement.2, axis-agreement.6
- trail: H2-04 §answers

From the note:

> Piton's own caveat and the asserted compression of community-average rRNA copy number variance relative to isolates [23, asserted] cut against reading the qualitative agreement as axis identity..
>

Not found in the cited text (where to look, not what is wrong): 2023

## 16S/sampling-model.1 (claim)

A Poisson random-sampling model of long-tailed abundance distributions predicted the low OTU overlap among soil technical replicates with no significant difference from the observed values, and about 60,900 sequences per replicate would be needed for 90% overlap.

- conf: single (marker)
- class: model (marker)
- holds: Zhou 2011's 24 Oklahoma grassland soils on 454; the predicted reads for 90% overlap rest on Zhou 2013
- src: zhouRandomSamplingProcess2013 (FT; model; single)
- trail: MB-01 §4.1, §answers

From the note:

> A Poisson random-sampling model predicted these overlaps with no significant difference from the observed values.
>
> About 60,900 sequences per replicate would be needed for 90% overlap (Zhou 2013) [FT; model; single].
>
> **sampling explains much of the replicate variation in taxa detected; extra-sampling variation is real but measured in few studies**: Sampling from the amplified pool.
>
> Poisson or multinomial sampling of long-tailed abundance distributions predicted the low OTU overlap seen among soil technical replicates, with no significant difference from the observed values (Zhou 2013, modelled; 454).
>
> About 60,900 reads were predicted to be needed for 90% overlap (Zhou 2013).
>
> The predicted reads for 90% overlap rest on Zhou 2013.
>

Not found in the cited text (where to look, not what is wrong): holds: 2011; holds: 24; holds: oklahoma; holds: grassland

## CB3/synthetic-fertiliser.4 (claim)

Menegat et al. 2022: "the synthetic N fertiliser supply chain was responsible for estimated emissions of 1.13 GtCO2e in 2018, representing 10.6% of agricultural emissions and 2.1% of global GHG emissions", with production 38.8%, field emissions 58.6% and transportation 2.6%.

- conf: not stated
- class: not stated
- holds: whole synthetic N supply chain; 2018; CO2 + N2O
- src: menegatGreenhouseGasEmissions2022 (Abstract read only)
- trail: CB3-AG-EMISSIONS §Boundary D, §No adversarial pass
- limit: access (note: "note where the review itself says it read only an abstract")

From the note:

> - Whole synthetic N supply chain, Menegat et al. 2022: "the synthetic N fertiliser supply chain was responsible for estimated emissions of **1.13 GtCO2e in 2018, representing 10.6% of agricultural emissions and 2.1% of global GHG emissions**.
>
> Synthetic N fertiliser production accounted for 38.8% ... field emissions 58.6% ... transportation 2.6%" [13].
>
> (Abstract read only; an author correction exists but concerns figure axis labels and a supplementary table, not the headline [13a].)
>
> | 25 | Synthetic N fertiliser, whole supply chain | 2.1% | 1.13 Gt CO2e | 2018 | CO2 + N2O | Menegat et al. 2022 [13] | abstract only |
>
> Treat the numbers as unconfirmed until spot-checked against the primary text, and note where the review itself says it read only an abstract.
>

## H1-RES/accessory-function.23 (claim)

A large fraction of accessory content represents structural variation, selfish genetic elements, or genes whose function cannot be inferred from sequence alone.

- conf: not stated
- class: reading (note: "This pattern suggests")
- holds: inferred from the counter-evidence
- src: none (the reviewer's inference)
- trail: H1-RES §Assessment: Context

From the note:

> This pattern suggests that a large fraction of accessory content represents structural variation, selfish genetic elements, or genes whose function cannot be inferred from sequence alone.
>

Not found in the cited text (where to look, not what is wrong): holds: counter-evidence

## 16S/absolute-quantification.11 (claim)

qPCR and sequencing both count extracellular DNA, unlike cell counts.

- conf: not stated
- class: not stated
- holds: Jian 2020
- src: jianQuantitativePCRProvides2020
- trail: MB-01 §5.5

From the note:

> - qPCR and sequencing both count extracellular DNA, unlike cell counts (Jian 2020).
>

## H1-02/annotation-coverage.1 (claim)

UHGG core genes had KEGG annotation for a median of 69% of genes, while accessory genes had significantly more unknowns.

- conf: not stated
- class: meas (note: "These are measured, gut only")
- holds: human gut only
- src: almeidaUnifiedCatalog2042020
- trail: H1-02 §3.6

From the note:

> UHGG core genes had KEGG annotation for a median of 69% of genes, while accessory genes had significantly more unknowns [10].
>
> These are measured, gut only.
>

Not found in the cited text (where to look, not what is wrong): holds: human

## TAXRES/name-resolution.1 (claim)

Unlike microbial gene normalisation, taxonomic name resolution is a mature, dedicated tooling area (TNRS, GNverifier / Global Names, GBIF fuzzy matching, taxize, Taxamatch, Pytaxon) with a best-practices review: documented tooling exists, likely stronger than in the gene case.

- conf: not stated
- class: not stated
- holds: the review's provisional, single-pass verdict; the gene case is a separate research result
- src: none (the verdict cites nothing; the tools are cited under the findings)
- trail: TAXRES §Provisional verdicts

From the note:

> **(b) Evaluated standard for resolving free-text taxon names? — DOCUMENTED TOOLING EXISTS (likely stronger than the gene case).** Unlike microbial gene normalisation, taxonomic name resolution is a **mature, dedicated tooling area** (TNRS, GNverifier/Global Names, GBIF fuzzy matching, `taxize`, Taxamatch, Pytaxon) with a best-practices review.
>

Not found in the cited text (where to look, not what is wrong): holds: single-pass

## 16S/dns.36 (do not say)

"Independent replication of the ploidy values by other groups was not located."

- why: the paper read in full (Pecoraro 2011) lists independent measurements (Azotobacter, Desulfovibrio, Neisseria, Buchnera, Deinococcus, Borrelia, rhizobial bacteroids)
- instead: ploidy.9
- trail: MB-02 §Adversarial

From the note:

> - Pecoraro et al. 2011 [11] was read in full, but its Table 5 (A. vinelandii 40 copies in fast growth; Desulfovibrio 9 to 17; Neisseria 3 to 4; Buchnera 120) and its mention of polyploid Deinococcus, Borrelia and rhizobial bacteroids are not reported. The review then says independent-laboratory measurements were 'not located'.
>
> - D1(b): the review notes the absence of independent replication of Soppa-group values, yet does not report the independent measurements listed in the paper it read in full. The search for independent evidence was weaker than the reporting of the main lab's results.
>
> I found no independent group's measurement contradicting these values, but I also did not find independent replication of most of them.
>

Not found in the cited text (where to look, not what is wrong): "Independent replication of the ploidy values by other groups was not located."; Azotobacter

## NFERT/dns.4 (do not say)

The review's weak support for substitution given as an answer on nitrogen-use efficiency (whether microbial cycling governs how much applied nitrogen is lost).

- why: the integration read: Q2 answered the substitution question, and so reported a null against a claim the proposal does not make; the efficiency/loss question was not researched
- instead: none
- trail: NFERT §Integration read

From the note:

> **Q2 answered the wrong question.** The brief asked whether microbial cycling **reduces synthetic input** (a *substitution* question), and the review correctly found that weakly supported: only deliberate legume/rhizobia fixation cleanly displaces fertiliser; the resident free-living community doing so is INDIRECT (free-living fixation modest, inoculants measure yield not input-reduction, mineralisation rarely meets demand; no source isolates the microbial term from confounders).
>
> **But the proposal's actual claim is about N-use EFFICIENCY, not substitution.** ¶36 says the N cycle "governs how efficiently that fertiliser is used and how much is lost as nitrous oxide" — i.e. efficient microbial cycling means *less of the applied nitrogen is wasted / lost* (to leaching, to N₂O), not that biological fixation *replaces* the fertiliser.
>
> The review's framing chased substitution and so reported a null against a claim the proposal does not actually make.
>

## H1-RES/pangenome.16 (claim)

Pangenome openness is not universal.

- conf: not stated
- class: not stated
- holds: the counter-evidence in pangenome.17 to pangenome.24
- src: none (the reviewer's synthesis)
- trail: H1-RES §Counter-Evidence: Taxa

From the note:

> Substantial counter-evidence demonstrates that pangenome openness is not universal.
>

Not found in the cited text (where to look, not what is wrong): holds: in; holds: pangenome.17; holds: pangenome.24

## H1-06/metabolic-depth.7 (claim)

Martiny et al. report that traits encoded by many genes sit deeper, with aerobic methane oxidation as a stated exception.

- conf: not stated
- class: not stated
- holds: the 89 traits on SEED genomes
- src: martinyPhylogeneticConservatismFunctional2013
- trail: H1-06 §3. Part A2, §Provenance
- limit: access (note: "I could not re-open Martiny 2013 (Europe PMC fullTextXML empty)")

From the note:

> **Ordering by complexity.** On 2,229 SEED genomes (26 phyla, 16S trees), 93% of 89 traits were non-randomly distributed [1].
>
> The authors report that traits encoded by many genes sit deeper, with aerobic methane oxidation as a stated exception.
>
> I could not re-open Martiny 2013 (Europe PMC fullTextXML empty) or Goberna and Verdu 2016 (OUP bot challenge), so the specific trait values from Martiny 2013 rest on two independent search-agent readings, and the two agents transcribed its overall tau_D range differently.
>

## 16S/intragenomic-variation.2 (claim)

Full-length PacBio sequencing recovered intragenomic variants in their expected integral ratios.

- conf: single (marker)
- class: meas (marker)
- holds: developer study
- src: callahanHighthroughputAmpliconSequencing2019 (FT; meas; single; developer)
- trail: MB-01 §2.5

From the note:

> Full-length PacBio sequencing recovered intragenomic variants in their expected integral ratios (Callahan 2019) [FT; meas; single; developer].
>

## H2-04/covariance-partition.4 (claim)

Every microbial partition found is a single study with its own denominator, so the shares cannot be pooled.

- conf: single (note: "single study")
- class: not stated
- holds: the microbial partitions of case D1(b)
- src: none (the review's assessment of its sources)
- trail: H2-04 §answers, §critic
- rating: "Weak"

From the note:

> *Strength:* Weak.
>
> Every microbial partition is a single study with a different denominator, so the shares cannot be pooled.
>
> Strength weak; every microbial share is a single study with its own denominator.
>

Not found in the cited text (where to look, not what is wrong): holds: d1

## H2-04/dns.7 (do not say)

"Growth rate, genome size and cell size are near-independent (r2 at most 0.012)", without the paper's qualifications.

- why: the review omits the weak nonlinearity (about 6% of variance) and the habitat contribution (about 11%) that the paper reports, which qualify near-independence
- instead: genome-level-axes.1
- trail: H2-04 §critic, §Adversarial critique

From the note:

> Genome-level reference axes exist (growth rate, genome size and cell size near-independent, r2 at most 0.012 [33, full text]; genome-size-dependent reversal of trait relations across about 18,000 genomes [2a, abstract]).
>
> The review omits the weak nonlinearity (about 6% of variance) and the habitat effects (about 11%) that the paper reports.
>
> - Westoby 2021 (FT): 'r2 at most 0.012' is correct for pairwise correlations (maximum 0.0121, genome size versus cell diameter). The review omits the paper's reported 6% nonlinearity and roughly 11% habitat contribution, which qualify 'near-independent'.
>

Not found in the cited text (where to look, not what is wrong): "Growth rate, genome size and cell size are near-independent (r2 at most 0.012)"

## 16S/richness-estimators.2 (claim)

Hill-number extrapolation is reliable only to about 2 to 3 times the reference sample size for richness.

- conf: not stated
- class: model (marker)
- holds: ecology, labelled INDIRECT
- src: chaoRarefactionExtrapolationHill2014 (FT; model; INDIRECT)
- trail: MB-01 §5.1, §answers

From the note:

> Hill-number extrapolation is reliable only to about 2 to 3 times the reference sample size for richness (Chao 2014) [FT; model; INDIRECT].
>
> Extrapolation is reliable only to about 2-3 times the sample size (Chao 2014, indirect).
>

## H2-01/trait-dimension.3 (claim)

In simulations, species number mattered only below about 100 to 200 species, and dropping half the traits lost much quality.

- conf: not stated
- class: model (note: "In simulations")
- holds: simulated species-by-trait matrices
- src: mouillotDimensionalityStructureSpecies2021 (FT)
- trail: H2-01 §2.4

From the note:

> In simulations, species number mattered only below about 100 to 200 species, and dropping half the traits lost much quality.
>
> How dimension depends on feature number, feature correlation and sample count has only been measured in species trait databases (median 4 or 6 axes depending on the rule, rising with number of traits, falling with trait correlation, and sensitive to species number only below about 100 to 200 [Mouillot2021]).
>

Not found in the cited text (where to look, not what is wrong): holds: simulated; holds: species-by-trait

## H1-02/contaminated-pangenome.1 (claim)

In a cirrhosis case-control gut cohort re-analysed with UHGG/MIDAS2 pangenomes, 33 (38%) of 86 Lachnospiraceae genes that differed in prevalence between cases and controls were probable contaminants from disease-associated genera; the differential calls come from read mapping to a partly contaminated reference pangenome, not from comparing recovered genomes.

- conf: single (critic: C-003)
- class: not stated
- holds: one cirrhosis cohort and one family, Lachnospiraceae (the critic); natural human gut; false differential prevalence, not content differences between genomes recovered from different samples
- src: majernikSmallAmountsMisassembly2025
- trail: H1-02 §2.2, §critic, §Adversarial critique

From the note:

> Majernik et al. [22] re-analysed a cirrhosis case-control gut cohort with UHGG/MIDAS2 pangenomes.
>
> Of 86 Lachnospiraceae genes that differed in prevalence between cases and controls, 33 (38%) were probable contaminants from disease-associated genera.
>
> Separately, contamination of a reference pangenome produced false differential gene prevalence between sample groups (SINGLE SOURCE [22]; the calls come from read mapping to UHGG, not from comparing recovered genomes).
>
> [22] measures false differential prevalence from reads mapped to a contaminated reference pangenome, not content differences between genomes recovered from different samples.
>
> - Contamination-driven false gene associations (38%, 33/86) come from one cirrhosis cohort and one family, Lachnospiraceae [22]. The quick re-run on Bacteroides thetaiotaomicron was 30 genes in the same data set.
>
> The differential calls come from MIDAS2 read mapping to a reference pangenome that was partly contaminated.
>

Not found in the cited text (where to look, not what is wrong): holds: human

## H1-02/core-genome-inference.1 (claim)

Simulations of core-genome inference give larger numbers than real comparisons because they strip sequence at random.

- conf: not stated
- class: not stated
- holds: simulated incompleteness
- src: none (the reviewer's synthesis)
- trail: H1-02 §2.5

From the note:

> Simulations of core-genome inference give larger numbers because they strip sequence at random.
>

Not found in the cited text (where to look, not what is wrong): holds: simulated

## CB2/binning.1 (claim)

Song et al. state that multiple 16S copies "result in unusually high read-depth information" for the contig carrying them, which together with "atypical nucleotide composition, hinders its correct binning with the rest of the genome"; Gruber-Vodicka et al. make the same point.

- conf: not stated
- class: not stated
- holds: coverage-based binning, binning-side
- src: songMarkerMAGLinkingMetagenomeassembled2022, grubervodickaPhyloFlashRapidSmallsubunit2020
- trail: CB2-RRNA §3. The mechanism

From the note:

> **Copy number defeats coverage-based binning.** Song et al. state the binning half explicitly: multiple 16S copies "result in unusually high read-depth information" for the contig carrying them, which together with "atypical nucleotide composition, hinders its correct binning with the rest of the genome".
>
> Gruber-Vodicka et al. make the same point.
>

Not found in the cited text (where to look, not what is wrong): holds: binning-side

## H1-05/functional-unit.7 (claim)

For ectomycorrhizal fungi, turnover appeared at the level of gene sequence variants but not of gene-family abundance.

- conf: not stated
- class: not stated
- holds: ectomycorrhizal fungal communities across a precipitation gradient [20]; targeted gene families; abstract only
- src: pellitierPotentialFunctionalDivergence2024 (AB)
- trail: H1-05 §2, §answers

From the note:

> For ectomycorrhizal fungi, turnover appeared at the level of gene sequence variants but not gene-family abundance [20] (abstract only).
>
> Ectomycorrhizal turnover appeared in gene sequence variants but not gene-family abundance [20] [AB].
>

Not found in the cited text (where to look, not what is wrong): holds: fungal

## 16S/abundance-occupancy.8 (claim)

Core assignments in an Arabidopsis root dataset varied 7-fold among methods.

- conf: not stated
- class: not stated
- holds: Arabidopsis root data, 288 samples
- src: custerComparativeAnalysisCore2023 (FT)
- trail: MB-02 §D3.2, §answers

From the note:

> - **Arabidopsis root data** [52, FT]: core size varied 7-fold among methods.
>
> Rhizosphere: in common bean rhizospheres across four US regions plus Colombia, 48 bacterial and archaeal taxa occurred in all samples, and 13.7% of bacterial and archaeal taxa deviated from a neutral abundance-occupancy expectation [74]; in 4,866 maize rhizosphere samples, seven OTUs were present in all samples [75]; core assignments in an Arabidopsis root dataset varied 7-fold among methods [52].
>

Not found in the cited text (where to look, not what is wrong): holds: 288

## TSL/information-content.1 (claim)

Information content IC(c) = −log P(c) in an is-a taxonomy (Resnik 1995/1999): general concepts have high P and low IC (root P = 1, IC = 0); specific concepts have low P and high IC.

- conf: not stated
- class: not stated
- holds: is-a taxonomies with corpus probabilities
- src: resnikUsingInformationContent1995, resnikSemanticSimilarityTaxonomy1999
- trail: TSL §Verdict, §1. Specificity signals
- rating: "Confidence: high (3-0)"

From the note:

> The strongest, most direct primary evidence establishes two foundational, mutually consistent signals: **collection df / idf** (lower df = more specific) [S1] and **information content IC(c) = −log P(c)** in an is-a taxonomy, where corpus probability is monotonic up the hierarchy so altitude maps directly onto generality [S2].
>
> - **Information content IC(c) = −log P(c)** [S2] — Resnik (1995/1999): general concepts have high P, low IC (root P=1, IC=0); specific concepts low P, high IC.
>
> *Confidence: high (3-0).* Caveat: needs a unified root; WordNet has none naturally.
>

## H2-01/covariation-stability.4 (claim)

Among the entities involved in variable co-abundances, 84% of 304 pathways and also 76% of 100 species differed in level between cohorts.

- conf: single (critic: H2-01:C-082)
- class: not stated
- holds: four human gut cohorts
- src: chenGutMicrobialCoabundance2020 (FT, re-checked)
- trail: H2-01 §4.4, §critic

From the note:

> Of the 304 pathways involved in variable co-abundances, 84% also differed in abundance level between cohorts.
>
> The closest microbial evidence is single-habitat: across four human gut cohorts differing in disease state, 64.3% of pathway co-abundances varied in strength against 38.6% of species co-abundances, and 84% of pathways in variable co-abundances also differed in level [Chen2020].
>
> Among the entities involved in variable co-abundances, 84% of 304 pathways and also 76% of 100 species differed in level.
>
> (4) The D3 case D reading of Chen2020 omits the matching species result (76% level differences) and applies the lenient-threshold and power caution to replication but not to the between-cohort variability comparison or the temporal-stability figure.
>
> One study, one habitat, one heterogeneity test.
>

## H1-05/averaging.3 (claim)

On bromeliad data, the label-shuffling null found no evidence of functional selection, so the bromeliad pattern is consistent with averaging.

- conf: not stated
- class: not stated
- holds: a reanalysis of the bromeliad communities of [33]
- src: hoChallengesInterpretingFunctional2025, hoChallengesQuantifyingFunctional2024, loucaHighTaxonomicVariability2016
- trail: H1-05 §3.2, §answers

From the note:

> - Bromeliad data: no evidence of functional selection.
>
> Other habitats: the same null found no functional selection in bromeliad communities (reanalysing [33]) and found apparent selection in HMP stool to be artifactual under restricted shuffles [29][30].
>
> Ho and Huang [29] find the bromeliad pattern consistent with averaging.
>

## 16S/dns.3 (do not say)

"Extraction is the largest step for relative-abundance error, then PCR, then sequencing" as a field-wide ordering, rated strong and backed by "many independent mock studies".

- why: one 7-taxon vaginal dataset (Brooks 2015 reanalysed by McLaren 2019); contested by Fouhy 2016 and qualified by MBQC; the review's own single-source sensitivity says the ordering rests on McLaren and Brooks
- instead: workflow-bias.4
- trail: MB-01 §critic, §Adversarial

From the note:

> For relative abundance, the claim that extraction is the largest step, followed by PCR and then sequencing, rests on one 7-taxon vaginal dataset (Brooks 2015, reanalysed by McLaren 2019).
>
> It is contested by Fouhy 2016 (two extraction methods gave very similar data) and qualified by MBQC (specimen type mattered more than extraction).
>
> It should be presented as SINGLE DATASET, not as a field-wide ordering.
>
> D2 calls the step ordering 'strong' and backed by 'many independent mock studies', while its own sensitivity note says the ordering rests on McLaren/Brooks.
>
> - D2 'strength' field: rated 'Strong ... for the ordering', which is firmer than the access and source base allow (one re-analysed 454 dataset), as the review's own single_source_sensitivity field concedes.
>
> *Strength:* Strong that every step distorts composition, and for the ordering in which spurious taxa and contamination dominate richness error while extraction and PCR dominate relative-abundance error.
>
> Many independent mock studies agree.
>

Not found in the cited text (where to look, not what is wrong): "Extraction is the largest step for relative-abundance error, then PCR, then sequencing"

## H2-01/neighbouring-transfer.2 (claim)

Inference-level agreement of metagenome prediction tools was reasonable in human datasets and much lower in non-human and soil datasets.

- conf: not stated
- class: not stated
- holds: human, non-human and soil datasets
- src: sunInferenceBasedAccuracyMetagenome2020 (FT)
- trail: H2-01 §3.3

From the note:

> Sun et al. (2020) showed that the per-sample Spearman metric is almost insensitive to permuting genes across samples, and that inference-level agreement was reasonable in human datasets and much lower in non-human and soil datasets [Sun2020; FT].
>

## CB2/catalogue-recovery.5 (claim)

The Nayfach catalogue's mean completeness is 83% with mean contamination 1.3%, and the paper names "problems assembling the 16S rRNA locus" as one reason new species' MAGs came out less complete than known ones.

- conf: not stated
- class: not stated
- holds: the GEM catalogue
- src: nayfachGenomicCatalogEarths2020
- trail: CB2-RRNA §1. Measured recovery

From the note:

> The Nayfach catalogue's mean completeness is 83% with mean contamination 1.3%, and the paper names "problems assembling the 16S rRNA locus" as one reason new species' MAGs came out less complete than known ones.
>

Not found in the cited text (where to look, not what is wrong): holds: gem

## H1-02/same-sample-isolate.9 (claim)

The authors conclude that the quality of MAGs may often be worse than estimated.

- conf: not stated
- class: not stated
- holds: the authors' conclusion from the eight E. coli pairs
- src: mezitiReliabilityMetagenomeassembledGenomes2021
- trail: H1-02 §2.1

From the note:

> The authors conclude that "the quality of MAGs may often be worse than estimated".
>

## H1-05/contrast-size.2 (claim)

In a single-site precipitation experiment, ±30% precipitation slightly decreased and ±60% strongly increased the within-treatment dispersion (PERMDISP) of taxa, genes, proteins and enzyme activities alike, and neither taxonomy nor function showed a directional PERMANOVA shift.

- conf: not stated
- class: meas (marker)
- holds: one steppe site, two magnitudes of precipitation change [22]; within-treatment dispersion, not turnover across environments; the study does not compare the two turnovers' magnitudes, so it bears only indirectly on the ordering
- src: xuDistinctivePatternMechanism2022 (FT, rechecked; measured)
- trail: H1-05 §1.4, §critic, §answers

From the note:

> The nearest is a single-site precipitation experiment [22] [FT, rechecked; measured].
>
> There, ±30% precipitation slightly decreased and ±60% strongly increased within-treatment dispersion (PERMDISP) of taxa, genes, proteins and enzyme activities alike.
>
> Gene, protein and enzyme dissimilarities were Mantel-correlated with taxonomic dissimilarity, and neither taxonomy nor function showed a directional PERMANOVA shift.
>
> The one soil study that varied contrast size within a site [22] found that functional dispersion tracked taxonomic dispersion at both levels (a small decrease at ±30% precipitation, a large increase at ±60%) and did not find a change in ordering.
>
> [22] tests within-treatment dispersion under two magnitudes of precipitation change.
>
> Neither taxonomy nor function shifted directionally there, and the study does not compare the two turnovers' magnitudes, so it bears only indirectly on D1.
>
> It measures within-treatment dispersion with no directional shift in either community, and it does not compare magnitudes, so it is indirect and should be labelled so.
>

Not found in the cited text (where to look, not what is wrong): holds: steppe

## TSL/df-idf.1 (claim)

Collection df / idf is the seminal specificity signal (Spärck Jones 1972): terms are weighted by collection frequency so that matches on rarer, more specific terms count for more; specificity is inversely related to df (lower df = more specific).

- conf: not stated
- class: not stated
- holds: term weighting over a document collection for retrieval; not a definition of semantic specificity (df-idf.2)
- src: sparckjonesStatisticalInterpretationTerm1972
- trail: TSL §Verdict, §1. Specificity signals
- rating: "Confidence: high (3-0)"

From the note:

> The strongest, most direct primary evidence establishes two foundational, mutually consistent signals: **collection df / idf** (lower df = more specific) [S1] and **information content IC(c) = −log P(c)** in an is-a taxonomy, where corpus probability is monotonic up the hierarchy so altitude maps directly onto generality [S2].
>
> - **Collection df / idf** [S1] — *the* seminal specificity signal (Spärck Jones 1972): weight terms by collection frequency so matches on rarer, more specific terms count for more.
>
> Specificity inversely related to df.
>
> *Confidence: high (3-0).* Caveat: df is a *frequency proxy*, not a definition of semantic specificity — the "specificity = term use not meaning" framing was **refuted** (0-3); low df from typos/OCR/identifiers does not imply true specificity.
>

Not found in the cited text (where to look, not what is wrong): holds: df-idf.2

