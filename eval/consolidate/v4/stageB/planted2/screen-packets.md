# Screening packet: 200 claims

## 16S/term-sensitivity.7

Occupancy-based core methods were most accurate in simulations; this rests on one simulation study.

- conf: single (critic: MB-02:C-092)
- class: model (note: "in simulations")
- holds: one simulation study
- src: custerComparativeAnalysisCore2023
- trail: MB-02 §D2.5, §Adversarial

From the note:

> Occupancy-based methods were most accurate in simulations.
>
> - D2: 'Occupancy-based core methods performed best' rests on one simulation study (Custer et al. 2023 [52]) and is listed among proposed standards as if established.
>

## 16S/abundance-distribution.24

Absolute-abundance work multiplies relative abundance by total counts (flow cytometry or qPCR), which converts gene copies but not cells per taxon.

- conf: not stated
- class: not stated
- holds: non-soil; abstract only
- src: propsAbsoluteQuantificationMicrobial2016 (AB)
- trail: MB-02 §D3.1

From the note:

> Absolute-abundance work multiplies relative abundance by total counts (flow cytometry or qPCR) [83, AB, non-soil], which converts gene copies but not cells per taxon.
>

## 16S/zeros.2

Pseudocounts made tests conservative.

- conf: single (marker)
- class: model (marker)
- holds: abstract only
- src: kaulAnalysisMicrobiomeData2017 (AB; model; single)
- trail: MB-01 §4.3

From the note:

> Pseudocounts made tests conservative (Kaul 2017) [AB; model; single].
>

## 16S/coverage-standardisation.3

In Schloss 2024b's null models, coverage-based iNEXT estimates were among those that "showed a strong correlation between richness and the number of sequences"; the text exempts "rarefaction and possibly the size-based iNEXT estimates". This is the only microbial amplicon test of coverage-based standardisation found; beyond it the evidence is non-microbial.

- conf: single (critic: MB-01:C-049)
- class: model (note: "null models")
- holds: Schloss's null models; the synthesis agent's re-reading of the full text, verified by the critic
- src: schlossRarefactionCurrentlyBest2024 (FT, re-opened)
- trail: MB-01 §5.2, §answers, §critic, §Search record

From the note:

> - **Coverage-based iNEXT.** In the synthesis agent's re-reading of the full text, coverage-based iNEXT estimates were among those that "showed a strong correlation between richness and the number of sequences".
>
> The text exempts "rarefaction and possibly the size-based iNEXT estimates".
>
> This is the only microbial amplicon test of coverage-based standardisation found.
>
> In Schloss 2024b's null models the coverage-based iNEXT estimates stayed correlated with depth (the synthesis agent's reading of the full text).
>
> One correction resulted: the Schloss 2024b passage shows coverage-based iNEXT estimates remained correlated with depth.
>
> Coverage-based standardisation has one microbial test (the Schloss 2024b null model, verified: all approaches 'except for rarefaction and possibly the size-based iNEXT estimates' remained depth-correlated).
>
> Beyond that, the evidence is non-microbial.
>
> Coverage-based standardisation has almost no microbial benchmark.
>

## 16S/abundance-distribution.2

In one Brazilian soil, 26,079 reads and 2,880 observed species were fitted equally well by communities of 10^4, 10^5 and 10^6 species, so the tail cannot be identified from sample data.

- conf: repl (marker)
- class: model (marker)
- holds: one Brazilian soil; the full text was not openly retrievable and these figures could not be confirmed
- limit: access (critic: MB-01:C-028)
- src: haegemanRobustEstimationMicrobial2013 (FT; model; repl)
- trail: MB-01 §3.4, §answers, §critic

From the note:

> - In the Brazil soil, 26,079 reads and 2,880 observed species were fitted equally well by communities of 10^4, 10^5 and 10^6 species, so the tail cannot be identified from sample data (Haegeman 2013) [FT; model; repl].
>
> One Brazilian soil was fitted equally well by communities of 10^4, 10^5 and 10^6 species, so the tail cannot be identified from the data (Haegeman 2013).
>
> Haegeman 2013's Brazil-soil figures rest on a full text that was not openly retrievable.
>

## 16S/scaling-normalisation.4

Wrench's makers state that library-size scaling and rarefaction cannot correct compositional bias that is uncorrelated with library size, and SRS's makers claim better reproducibility than rarefying.

- conf: not stated
- class: not stated
- holds: makers' claims; abstracts only
- src: kumarAnalysisCorrectionCompositional2018 (AB; makers' claim), beuleImprovedNormalizationSpecies2020 (AB)
- trail: MB-01 §5.4

From the note:

> Wrench's makers state that library-size scaling and rarefaction cannot correct compositional bias that is uncorrelated with library size (Kumar 2018) [AB; makers' claim].
>
> SRS's makers claim better reproducibility than rarefying (Beule 2020) [AB].
>

## 16S/technical-variation.6

One HiSeq run lost an archaeal mock taxon from all samples and shifted others by more than 2-fold, while re-running the same amplicons was normal.

- conf: single (marker)
- class: meas (marker)
- holds: one run, one mock
- src: yehTaxonDisappearanceMicrobiome2018 (FT; meas; single)
- trail: MB-01 §4.3, §2. Steps, §answers

From the note:

> - One HiSeq run lost an archaeal mock taxon from all samples and shifted others by more than 2-fold. Re-running the same amplicons was normal (Yeh 2018) [FT; meas; single].
>
> **Run and batch effects.**
>
> Run effects.
>
> One HiSeq run lost an archaeal mock taxon and shifted others by more than 2-fold (Yeh 2018, single source).
>
> Run and batch effects: whole-run taxon loss (Yeh 2018, single source); a mis-set PCR machine produced a batch outlier (Silverman 2021); between-laboratory effects (MBQC).
>
> | Run | One run lost an archaeal mock taxon and shifted others more than 2-fold | Taxon loss | Varies between runs | Yeh 2018 |
>

## 16S/copy-number-correction.15

Applying copy-number (and genome-size) correction to a forest soil changed Acidobacteria from 50.1% of 16S sequences to an estimated 66.0% of genomes, Actinobacteria from 11.8% to 7.6% and Firmicutes from 3.2% to 1.1%; this is the only soil example of correction size, and it depends on the imprecise low Acidobacteria copy-number mean.

- conf: single (note: "SINGLE SOURCE for soil")
- class: deriv (marker)
- holds: one forest soil
- src: vetrovskyVariability16SRRNA2013 (FT; deriv; repl)
- trail: MB-01 §2.5, MB-02 §D1.4, §answers, §critic

From the note:

> **Effect on proportions.** Applying copy-number correction to forest soil changed Acidobacteria from 50.1% of sequences to an estimated 66.0% of genomes, and Firmicutes from 3.2% to 1.1% (Vetrovsky and Baldrian 2013) [FT; deriv; repl].
>
> - **Soil.** In a forest soil, correcting with copy number and genome size moved Acidobacteria from 50.1% of 16S sequences to an estimated 66.0% of genomes, Actinobacteria from 11.8% to 7.6% and Firmicutes from 3.2% to 1.1% [6, FT, derived].
>
> This is SINGLE SOURCE for soil.
>
> Effects on ecological conclusions are mixed: correction changed the most abundant OTU in about 20% (human) and 31% (Earth Microbiome Project) of communities but left PERMANOVA variance explained essentially unchanged [33]; it changed human body-site clustering but not ocean clustering [28]; it changed enterotype number from two to three [29]; in a forest soil example Acidobacteria rose from 50.1% of sequences to an estimated 66.0% of genomes [6].
>
> The only soil example of correction size rests on Vetrovsky and Baldrian 2013 [6].
>
> These soil-relevant low values are imprecise, and the soil correction example (Acidobacteria 50.1% to 66.0%) depends on them.
>

## 16S/global-classes.1

In soil, "dominant" has been defined jointly: in the top 10% of phylotypes by share of 16S reads and present in more than half of 237 soils.

- conf: not stated
- class: not stated
- holds: 237 soils, global
- src: delgadobaquerizoGlobalAtlasDominant2018 (FT)
- trail: MB-02 §D2.3, §answers

From the note:

> In soil, "dominant" has been defined jointly: in the top 10% of phylotypes by share of 16S reads and present in more than half of 237 soils [60, FT].
>
> (3) Regional or global distribution: 'dominant' soil phylotypes were defined as both in the top 10% by reads and present in over half of 237 sites [60]; 'common' versus 'rare' was set by a data-driven global threshold (about 0.019% of pooled relative abundance) [61].
>

## 16S/absolute-quantification.13

Synthetic spike-ins had differing detection efficiencies and small departures from linearity, and correlations were weaker with Taq than with KOD polymerase.

- conf: repl (marker)
- class: meas (marker)
- holds: synthetic 16S spike-ins
- src: tourlousseSyntheticSpikeinStandards2016 (FT; meas; repl)
- trail: MB-01 §5.5

From the note:

> - Synthetic spike-ins had differing detection efficiencies and small departures from linearity. Correlations were weaker with Taq than with KOD polymerase (Tourlousse 2017) [FT; meas; repl].
>

## 16S/read-depth.8

No peer-reviewed coefficient of variation of reads per sample within a run after equimolar pooling was found; all three angles searched, and web search returned only forum posts.

- conf: not stated
- class: search (note: "All three angles searched")
- holds: all three angles; web search
- src: none (a statement about what the search found)
- trail: MB-01 §3.3, §answers, §Search record

From the note:

> **Not found.** No peer-reviewed coefficient of variation of reads per sample within a run after equimolar pooling.
>
> All three angles searched; web search returned only forum posts.
>
> No peer-reviewed coefficient of variation of reads within a run after equimolar pooling was found.
>
> Absent for the within-run coefficient of variation.
>
> Absolute per-cycle efficiencies and the within-run read CV were not found.
>
> - Within-run read-count CV after equimolar pooling (all angles; web search found only forums).
>
> Not found by any route: within-run CV of reads per sample; absolute per-cycle 16S efficiencies; measured (not predicted) community copy number by environment; 16S-specific index hopping on patterned flow cells; overdispersion fitted to 16S technical replicates; an independent microbial benchmark of coverage-based standardisation; abundance-distribution shapes reported separately for water and host.
>

## 16S/denoising-clustering.8

QIIME closed- and open-reference OTUs inflated richness to 1,607 to 5,824 OTUs where about 20 were expected, and on V4 mocks 56 to 88% of predicted genus names were false positives.

- conf: single (marker)
- class: meas (marker)
- holds: V4 mocks; single source
- src: edgarAccuracyMicrobialCommunity2017 (FT; meas; single)
- trail: MB-01 §2.10, §2. Steps

From the note:

> **Closed and open reference.** QIIME closed- and open-reference OTUs inflated richness to 1,607 to 5,824 OTUs where about 20 were expected.
>
> On V4 mocks, 56 to 88% of predicted genus names were false positives (Edgar 2017a) [FT; meas; single].
>
> SINGLE SOURCE.
>
> | Classification | n/a | V4 genus accuracy about 50% at 97% identity. 56 to 88% false genus names with closed reference | Depends on distance to reference | Edgar 2018b; Edgar 2017a |
>

## 16S/denoising-clustering.1

Error-handling choices are 97% or 99% OTUs (de novo, closed or open reference) or ASVs from DADA2, Deblur or UNOISE3; DADA2 can process samples independently, pooled or pseudo-pooled.

- conf: not stated
- class: not stated
- holds: documentation and benchmarks
- src: callahanDADA2DocumentationPseudopooling
- trail: MB-01 §answers

From the note:

> Error handling: 97% or 99% OTUs (de novo, closed or open reference), or ASVs from DADA2, Deblur or UNOISE3; DADA2 can process samples independently, pooled or pseudo-pooled.
>

## 16S/abundance-distribution.17

DNA reassociation kinetics, which measure whole-community DNA rather than reads or cells, were best fitted by a power law, implying over a million distinct genomes in a pristine soil; metal pollution cut diversity by over 99.9%. This is the main contrary result on the shape of the distribution, and removing it removes the power-law side of the conflict.

- conf: not stated
- class: not stated
- holds: whole-community DNA; abstract only
- src: gansComputationalImprovementsReveal2005 (AB)
- trail: MB-02 §D3.1, §answers

From the note:

> **DNA reassociation kinetics.** This measures whole-community DNA, neither reads nor cells.
>
> A power law fitted best, implying over a million distinct genomes in a pristine soil; metal pollution cut diversity by over 99.9% [66, AB].
>
> This is the main contrary result on the shape of the distribution.
>
> DNA reassociation kinetics (whole community DNA, not reads or cells): a power law best described the abundance distribution, with over one million genomes in a pristine soil [66].
>
> Removing Gans et al. 2005 [66] removes the power-law side of the functional-form conflict.
>

## 16S/absolute-quantification.10

Absolute quantification does not correct taxon-specific extraction and PCR bias.

- conf: not stated
- class: not stated
- holds: McLaren 2019 and Bonk 2018
- src: mclarenConsistentCorrectableBias2019, bonkPCRbasedQuantificationTaxaspecific2018
- trail: MB-01 §5.5, §answers, §8. Answers, §critic

From the note:

> **What it does not correct, and failure modes.**
>
> - Taxon-specific extraction and PCR bias remain (McLaren 2019; Bonk 2018).
>
> They do not correct taxon-specific extraction and PCR bias. qPCR and flow cytometry diverged on faeces (Galazzo 2020, single source).
>
> Absolute quantification addresses differences in load but not taxon-specific bias, and its methods disagree with each other.
>
> It supports that absolute quantification changes conclusions but does not remove taxon-specific bias.
>

## 16S/quality-filtering.6

The USEARCH author reports that most paired-read assemblers compute incorrect posterior quality scores.

- conf: not stated
- class: not stated
- holds: developer claim; abstract only
- src: edgarErrorFilteringPair2015 (AB; developer claim)
- trail: MB-01 §2.9

From the note:

> The USEARCH author reports that most paired-read assemblers compute incorrect posterior quality scores (Edgar and Flyvbjerg 2015) [AB; developer claim].
>

## 16S/ploidy.11

Single-cell measurements in H. salinarum showed wide cell-to-cell variation in genome copy number, larger in exponential than in stationary phase; the review read only the abstract, which gives no per-cell shares, although the open full text reports single-cell CLSM and FACS distributions.

- conf: not stated
- class: not stated
- holds: H. salinarum cultures
- limit: access (critic: MB-02:C-071)
- src: breuertRegulatedPolyploidyHalophilic2006 (AB)
- trail: MB-02 §D1.3, §Adversarial

From the note:

> Single-cell measurements in H. salinarum showed wide cell-to-cell variation in copy number, larger in exponential than in stationary phase [14, AB]; the abstract gives no per-cell shares.
>
> - Breuert et al. 2006 [14] is open in PMC (PMC1762399; Europe PMC fullTextXML works) but labelled AB.
>
> Its full text reports single-cell CLSM and FACS distributions of genome copy number in H. salinarum, which bear directly on the brief's 'share of cells' question.
>
> The review states that 'the abstract gives no per-cell shares' without trying the full text.
>

## 16S/core-microbiome.5

In 4,866 maize rhizosphere samples, seven OTUs were present in all, five of them responsive to host genotype.

- conf: not stated
- class: not stated
- holds: maize rhizosphere; abstract only
- src: waltersLargescaleReplicatedField2018 (AB)
- trail: MB-02 §D3.2, §answers

From the note:

> - **Maize** [75, AB]: in 4,866 samples, seven OTUs were present in all, five of them responsive to host genotype.
>
> Rhizosphere: in common bean rhizospheres across four US regions plus Colombia, 48 bacterial and archaeal taxa occurred in all samples, and 13.7% of bacterial and archaeal taxa deviated from a neutral abundance-occupancy expectation [74]; in 4,866 maize rhizosphere samples, seven OTUs were present in all samples [75]; core assignments in an Arabidopsis root dataset varied 7-fold among methods [52].
>

## 16S/coverage-standardisation.4

Coverage-based standardisation is in conflict: Chao and Jost 2012 against Alroy 2026 (both non-microbial) and the microbial null model in Schloss 2024b; an independent microbial amplicon benchmark of coverage-based standardisation with known truth was not found.

- conf: not stated
- class: search (note: "An independent microbial benchmark of coverage-based standardisation (statistics angle)")
- holds: statistics angle
- src: chaoCoveragebasedRarefactionExtrapolation2012, alroyCoveragebasedRarefactionFails2026, schlossRarefactionCurrentlyBest2024
- trail: MB-01 §answers, §Search record

From the note:

> Coverage-based standardisation: Chao and Jost 2012 versus Alroy 2026 (both non-microbial) and the microbial null model in Schloss 2024b.
>
> - An independent microbial benchmark of coverage-based standardisation (statistics angle).
>
> *Not measured:* Not found: an independent microbial amplicon benchmark of coverage-based standardisation with known truth; any D5 benchmark that includes taxon-specific bias and differences in total load in the simulated truth together, apart from Llorens-Rico 2021 (simulated faeces, no taxon bias); benchmarks in soil or water with measured absolute loads used as truth; tests of richness corrections against known-richness mocks across depths.
>

## 16S/relic-dna.2

Relic DNA averaged 33% (over 80% in some samples) across soil, sediment, water and mammalian gut but had minimal effect on diversity estimates; models predict bias only when relic and intact abundance distributions differ.

- conf: cont (marker)
- class: meas (marker)
- holds: soil, sediment, water and mammalian gut
- src: lennonHowWhereRelic2018 (FT; meas; cont)
- trail: MB-01 §2.2, §7. Bounds, MB-02 §D3.3

From the note:

> - Relic DNA averaged 33% across soil, sediment, water and mammalian gut but had minimal effect on diversity estimates. Models predict bias only when relic and intact abundance distributions differ (Lennon 2018) [FT; meas; cont].
>
> - relic DNA in one multi-environment study (Lennon 2018);
>
> - Lennon et al. 2018 [78, AB]: across soil, sediment, water and gut, relic DNA averaged 33% (over 80% in some samples) but had minimal effect on diversity estimates.
>

## 16S/bias-consistency.10

Evidence on whether bias is consistent across samples is weak: it rests mainly on one reanalysis of 7 taxa, with contrary or limiting field evidence.

- conf: not stated
- class: not stated
- holds: the evidence above
- src: none (the review's and critic's rating of the evidence)
- trail: MB-01 §answers, §8. Answers, §critic
- rating: "weak for consistency"

From the note:

> Evidence on whether bias is consistent across samples is weak to moderate: it rests mainly on one reanalysis of 7 taxa, with contrary or limiting field evidence.
>
> Strong qualitatively, moderate for magnitudes, weak for consistency.
>
> Overall: strong qualitatively; moderate for the inflation of taxon counts; weak for per-step relative-abundance magnitudes and for consistency across samples.
>

## 16S/coverage-standardisation.2

A 2026 test on terrestrial inventories finds that coverage-based rarefaction "does not respond predictably" to richness.

- conf: single (marker)
- class: model (marker)
- holds: terrestrial (non-microbial) inventories; abstract only; labelled INDIRECT
- src: alroyCoveragebasedRarefactionFails2026 (AB; model; single; INDIRECT)
- trail: MB-01 §5.1, §answers

From the note:

> A 2026 test on terrestrial inventories finds coverage-based rarefaction "does not respond predictably" to richness (Alroy 2026) [AB; model; single; INDIRECT].
>
> Alroy 2026 (abstract, non-microbial) finds it fails on terrestrial inventories.
>

## 16S/beta-diversity.1

Proportions and rarefying were the only methods that fully normalised depth, and scaling methods masked differences in common OTUs.

- conf: single (marker)
- class: model (marker)
- holds: abstract only
- src: mcknightMethodsNormalizingMicrobiome2019 (AB; model; single)
- trail: MB-01 §5.3, §answers

From the note:

> **Proportions.** Proportions and rarefying were the only methods that fully normalised depth; scaling methods masked differences in common OTUs (McKnight 2019) [AB; model; single].
>
> Beta diversity.
>
> Proportions: accurate for community comparisons according to McKnight 2019 (abstract), but still depth-sensitive under Schloss's null.
>

## 16S/copy-number.7

The long-quoted bacterial ceiling of 15 is no longer the database maximum: rrnDB v5.6 contains a Photobacterium damselae genome with 21 copies and v5.10 a Mesobacillus maritimus genome with 22, and several Photobacterium and Bacillaceae genomes have 20 to 21; no source checked whether these extremes survive scrutiny of assembly quality.

- conf: not stated
- class: deriv (critic: MB-02:C-007)
- holds: rrnDB v5.6 and v5.10; the reviewer's own derivation from rrnDB, with no published check against assembly quality; the critic: acceptable as labelled derived, but the answer leads with these computations over published values
- src: schmidtlaboratoryRrnDBReleaseFiles (FT; statistics derived by reviewer)
- trail: MB-02 §D1.1, §answers, §critic, §Adversarial

From the note:

> Three things follow from the table.
>
> First, the long-quoted ceiling of 15 is no longer the database maximum: v5.6 contains a Photobacterium damselae genome with 21 copies, and v5.10 a Mesobacillus maritimus genome with 22.
>
> Several Photobacterium and Bacillaceae genomes have 20 to 21.
>
> No source I found checked whether these extremes survive scrutiny of assembly quality.
>
> *Conflicts:* Maximum value: 15 in every source to about 2015 versus 21 to 22 in rrnDB v5.6 to v5.10; the high values were not checked against assembly quality by any source found.
>
> The current maxima (21 to 22 bacteria, 5 archaea) and the current means and shares rest on the reviewer's derivation from rrnDB alone; removing rrnDB [4] would leave the older 1 to 15 range.
>
> The new maxima and the current shares rest on the reviewer's derivation from rrnDB alone.
>
> The current maxima of 21 to 22 and the current shares remain the reviewer's own derivation from rrnDB, with no published check against assembly quality.
>
> - D1.1: the current rrnDB maxima, means and shares that headline the D1(a) answer are the reviewer's own computations. They are labelled derived, which is acceptable, but the answer leads with them over published values.
>

## 16S/sampling-storage.5

Storage of a single soil for 1 to 14 days at room temperature, 4 C or -20 C changed its community, most at 3 to 7 days and least when frozen; these changes were small relative to differences among more than 500 Earth Microbiome Project soils.

- conf: repl (marker)
- class: meas (marker)
- holds: one soil, 1 to 14 days, three temperatures, compared with more than 500 EMP soils; not shown for other soils
- src: rubinInvestigatingImpactStorage2013 (FT; meas; repl), lauberEffectStorageConditions2010 (SEC)
- trail: MB-01 §2.1, §answers, §7. Bounds

From the note:

> **Soil.** Storage for 1 to 14 days at room temperature, 4 C or -20 C changed a single soil's community, most at 3 to 7 days and least when frozen.
>
> These changes were small relative to differences among more than 500 Earth Microbiome Project soils (Rubin 2013) [FT; meas; repl].
>
> In soil, storage effects were small compared with differences between soils (Rubin 2013; single soil).
>
> - storage, relative to between-soil differences (Rubin 2013);
>
> Lauber et al. 2010 is known only through Rubin's description (SEC; see Sources not obtained).
>

## 16S/abundance-distribution.8

Abundance-distribution shapes reported separately for water and for host-associated 16S data were not found beyond the copy-correction fits in Kembel 2012, although per-biome supplementary figures (Grilli 2020) and Shoemaker 2017's full text exist and were not read.

- conf: not stated
- class: search (note: "no angle located such a breakdown")
- holds: all angles
- src: kembelIncorporating16SGene2012, grilliMacroecologicalLawsDescribe2020, shoemakerMacroecologicalTheoryMicrobial2017
- trail: MB-01 §3.4, §answers, §8. Answers, §Search record, §Adversarial
- rating: "Weak for abundance-distribution shapes split by environment"

From the note:

> **Not found.** Abundance-distribution shapes reported separately for water and for host-associated 16S data, beyond the copy-correction fits in Kembel 2012.
>
> - Abundance-distribution shapes split by water and host (no angle located such a breakdown).
>
> Weak for abundance-distribution shapes split by environment, because the field-wide sources do not separate soil, water and host.
>
> Abundance-distribution shapes are mostly not split by environment.
>
> - gap: Abundance-distribution shapes by environment. Grilli 2020's per-biome supplementary figures and Shoemaker 2017's full text were not read, so per-environment shapes for water and host samples are absent although the sources exist.; setting_or_class: Species abundance distributions in marine/freshwater and host-associated 16S datasets; direction: D3
>

## 16S/technical-variation.3

At 1:10^5 dilution of a staggered mock, 12 species appeared in only 2 of 4 PCR replicates.

- conf: not stated
- class: not stated
- holds: Dyrhovden's staggered mock
- src: dyrhovdenManagingContaminationDiverse2021
- trail: MB-01 §4.3

From the note:

> - At 1:10^5 dilution of a staggered mock, 12 species appeared in only 2 of 4 PCR replicates.
>

## 16S/pcr.8

PCR bias was consistent per taxon in the mocks, and calibration corrected composition toward truth in all 10 held-out mocks; the authors note that their mock "ground truth" carried its own bias and that the method sometimes estimated the wrong direction for some taxa.

- conf: not stated
- class: not stated
- holds: Silverman's gut-isolate mocks
- src: silvermanMeasuringMitigatingPCR2021
- trail: MB-01 §2.4, §answers

From the note:

> Calibration corrected composition toward truth in all 10 held-out mocks.
>
> The authors note that their mock "ground truth" carried its own bias and that the method sometimes estimated the wrong direction for some taxa.
>
> Consistency: consistent per taxon in mocks (Silverman 2021).
>
> Cycle effect small in some studies | Low-input stochastic dropout | Consistent per taxon in mocks.
>

## 16S/copy-number-correction.5

Phylogenetic copy-number prediction had a leave-one-out error of about one copy, and in 100 simulated communities correction raised the correlation with true organism abundance from r = 0.70 to 0.81.

- conf: cont (marker)
- class: model (marker)
- holds: simulated communities; figures checked by MB-02's critic
- src: kembelIncorporating16SGene2012 (FT; model; cont)
- trail: MB-01 §2.5, §answers, MB-02 §D1.4, §answers, §critic

From the note:

> - **Supportive (modelled).** In simulations, phylogenetically corrected abundances correlated better with true organism abundance (r = 0.81) than raw gene abundances did (r = 0.70) (Kembel 2012) [FT; model; cont].
>
> Simulation favours correction (Kembel 2012, modelled).
>
> - **Kembel et al. 2012** [28, FT]: leave-one-out error was about one copy.
>
> In 100 simulated communities, correction raised the correlation with true abundance from r = 0.70 to 0.81.
>
> Within that limit, phylogenetic predictions are informative: leave-one-out error about one copy [28], R2 high and precision about 0.96 at small distances with uncertainty growing with distance [33].
>
> Correction improved agreement with simulated truth (r from 0.70 to 0.81) [28], with mock communities and metagenomes [29], and the chance of identifying the true most abundant OTU (13% to 65% in simulations) [33].
>
> These all matched: Pecoraro 2011 (E. coli 6.8/2.5 origins, P. putida 20/14, Caulobacter 2.1, Wolinella 0.9), Louca 2018 (15%/30% autocorrelation, 49% of SILVA OTUs, 635 communities including soil), Gao and Wu 2023 (0.96 precision, 20%/31%, 13% to 65%), Kembel 2012 (r 0.70 to 0.81, K = 0.48), Vetrovsky 2013 (mean 4.2, 15%/21%, Acidobacteria 50.1% to 66.0%), Bickel and Or 2021 (0.4%, 0.019%, prevalence 0.3 vs 0.001), Jia 2022 (61.59/45.65/28.36%, ASV counts), Custer 2023 (1.21 to 9.42%), Pascoal 2025 (181 articles, 37%, 84%, V4V5 versus full-length reversal) and Stopnisek and Shade 2021 (48 taxa, 13.7%, rarefied to 31,255 reads).
>

## 16S/primers.4

For the 515F-Y/806R pair, SAR11 was under-represented about 4 to 10-fold in marine field samples but only about 2-fold in mocks, so mock-measured bias understated field bias for this taxon; this rests on one abstract, one primer pair and one taxon.

- conf: single (critic: MB-01:C-092)
- class: meas (marker)
- holds: marine field samples and marine clone mocks; one primer pair (515F-Y/806R) and one taxon (SAR11); abstract only
- src: paradaEveryBaseMatters2016 (AB; meas; repl)
- trail: MB-01 §2.3, §2.14, §critic, §Adversarial

From the note:

> (b) The Parada 2016 SAR11 4-10-fold versus 2-fold figures are attributed to the original 515F/806R pair; the abstract gives them for 515F-Y/806R.
>
> - Parada 2016 (AB): the abstract gives the SAR11 bias (about 4 to 10-fold in field samples versus about 2-fold in mocks) for 515F-Y/806R, not for the original 515F-C/806R. The review attributes it to 'the original 515F/806R V4 primers' in section 2.3, Table 1 and the D2 answer.
>
> - D2 Table 1: 'Mock bias did not transfer to the field' rests on Parada 2016 (abstract only), for one primer pair (515F-Y/806R) and one taxon (SAR11).
>
> Variation between sample types or samples is shown by a field-versus-mock SAR11 bias for the 515F-Y/806R pair (Parada 2016, abstract only), inconsistent cycle effects in four stool samples (Sze and Schloss 2019), extraction yield of 40 to 84% (Zemb 2020) and a 66.7-fold spike-in range (Zhou 2011, abstract).
>
> Bias against SAR11 was about 4 to 10-fold in field samples but only about 2-fold in mocks.
>
> So mock-measured bias understated field bias for this taxon.
>
> | Primers, region | SAR11 under-represented about 4 to 10-fold in the field vs about 2-fold in mocks.
>
> - Mock-measured SAR11 bias of about 2-fold became about 4 to 10-fold in field samples (Parada 2016).
>
> Field and stool studies show bias that does not carry over from mocks (Parada 2016) [AB; meas; repl] or that varies between samples (Sze and Schloss 2019) [FT; meas; single].
>
> Primers and region.
>
> RA: the original V4 primers under-represented SAR11 by about 4-10 fold in marine field samples but only about 2-fold in mocks (Parada 2016, abstract), so this bias was not consistent between mock and field.
>

## 16S/copy-number.18

Acinas et al. 2004 found up to 15 operons in bacteria, with copy numbers up to 7 common and about 40% of organisms having one or two operons; a single operon dominated in archaea.

- conf: not stated
- class: not stated
- holds: genome survey; abstract only
- src: acinasDivergenceRedundancy16S2004 (AB)
- trail: MB-02 §D1.2

From the note:

> - **Acinas et al. 2004** [5, AB]: up to 15 operons in bacteria, with copy numbers up to 7 common.
>
> About 40% of organisms had one or two operons.
>
> A single operon dominated in archaea, with a maximum of five.
>

## 16S/extraction.1

Extraction choices include the kit, bead-beating intensity, plate or single tube, and whether relic DNA is removed with PMA or DNase.

- conf: not stated
- class: not stated
- holds: the extraction studies below
- src: albertsenBackBasicsInfluence2015, minichQuantifyingUnderstandingWelltowell2019, cariniRelicDNAAbundant2016, lennonHowWhereRelic2018
- trail: MB-01 §answers

From the note:

> DNA extraction: kit, bead-beating intensity, plate or single tube, and whether relic DNA is removed with PMA or DNase (Albertsen 2015; Minich 2019; Carini 2016; Lennon 2018).
>

## 16S/scaling-normalisation.1

Total-count scaling can bias differential-expression estimates in RNA-seq; TMM and DESeq's negative binomial model also come from RNA-seq, and both assume most features are unchanged between conditions.

- conf: not stated
- class: not stated
- holds: RNA-seq, labelled INDIRECT; abstracts only
- src: bullardEvaluationStatisticalMethods2010 (AB; INDIRECT), robinsonScalingNormalizationMethod2010 (AB; INDIRECT), andersDifferentialExpressionAnalysis2010 (AB; INDIRECT), weissNormalizationMicrobialDifferential2017
- trail: MB-01 §5.1, §answers

From the note:

> **Scaling normalisation.** Total-count scaling can bias differential-expression estimates in RNA-seq (Bullard 2010) [AB; INDIRECT].
>
> TMM (Robinson and Oshlack 2010) and DESeq's negative binomial model (Anders and Huber 2010) also come from RNA-seq [AB; INDIRECT].
>
> Weiss 2017 notes that both assume most features are unchanged between conditions.
>
> Scaling normalisations (TMM, RLE, CSS, VST, SRS, Wrench) come from RNA-seq (Bullard 2010; Robinson and Oshlack 2010; Anders and Huber 2010, indirect) and assume most features do not change.
>

## 16S/copy-number.13

The Acidobacteria mean of 1.0 rests on 4 genomes from 4 species, and the rrnDB v5.10 Acidobacteriota mean of 1.4 on 29 species; these soil-relevant low values are imprecise.

- conf: not stated
- class: not stated
- holds: Vetrovsky and Baldrian's Table 1 and rrnDB v5.10
- src: vetrovskyVariability16SRRNA2013, schmidtlaboratoryRrnDBReleaseFiles
- trail: MB-02 §critic, §Adversarial, §D1.1

From the note:

> (2) The 'Acidobacteria 1.0' mean from Vetrovsky and Baldrian [6, FT] rests on 4 genomes from 4 species (their Table 1).
>
> The rrnDB v5.10 figure of 1.4 rests on 29 species.
>
> These soil-relevant low values are imprecise, and the soil correction example (Acidobacteria 50.1% to 66.0%) depends on them.
>
> - D1(a): per-phylum means for Acidobacteria (1.0 from 4 genomes in [6]) are presented alongside large-n phyla without the n. The soil correction example rests on this.
>
> - Acidobacteriota 1.4 (29)
>

## 16S/differential-abundance.1

Fourteen differential-abundance methods on 38 datasets gave 0.8% to 40.5% significant ASVs (unfiltered means); ALDEx2 and ANCOM-II were the most consistent, and edgeR and LEfSe produced many false positives on random splits.

- conf: single (marker)
- class: meas (marker)
- holds: 38 real datasets
- src: nearingMicrobiomeDifferentialAbundance2022 (FT; meas; single)
- trail: MB-01 §5.4, §answers

From the note:

> **Agreement among methods on real data.** Fourteen methods on 38 datasets gave 0.8% to 40.5% significant ASVs (unfiltered means).
>
> ALDEx2 and ANCOM-II were the most consistent. edgeR and LEfSe produced many false positives on random splits (Nearing 2022) [FT; meas; single].
>
> Differential abundance.
>
> ALDEx2 and ANCOM-II were the most consistent across 38 datasets (Nearing 2022).
>
> The 14 methods gave 0.8% to 40.5% significant ASVs on the same data (Nearing 2022).
>

## 16S/intragenomic-variation.4

Acinas et al. estimated an upper bound of about threefold diversity overestimation from operon redundancy.

- conf: not stated
- class: not stated
- holds: abstract only
- src: acinasDivergenceRedundancy16S2004 (AB)
- trail: MB-02 §D1.2

From the note:

> Acinas et al. estimated an upper bound of about threefold diversity overestimation from operon redundancy [5, AB].
>

## 16S/primers.10

With universal PNA clamps, host plastid reads averaged 23% across 32 plant species (plant roots) but reached 62 to 94% in some lineages.

- conf: single (marker)
- class: meas (marker)
- holds: 32 plant species
- src: fitzpatrickChloroplastSequenceVariation2018 (FT; meas; single)
- trail: MB-01 §2.3, §answers

From the note:

> **Host-associated plant samples.** With universal PNA clamps, host plastid reads averaged 23% across 32 plant species but reached 62 to 94% in some lineages (Fitzpatrick 2018) [FT; meas; single].
>
> Host plastid reads averaged 23% of reads in plant roots and reached 62-94% in some plant lineages (Fitzpatrick 2018).
>

## 16S/rare-biosphere.9

In a 21-year estuarine fish record, persistent and abundant "core" species fitted a lognormal while infrequent "occasional" species fitted a log series, and Galand et al. report the same split for rare versus abundant Arctic Ocean prokaryotes.

- conf: not stated
- class: not stated
- holds: estuarine fish (abstract only) and Arctic Ocean prokaryotes
- src: magurranExplainingExcessRare2003 (AB), galandEcologyRareMicrobial2009 (FT)
- trail: MB-02 §D2.4, §answers

From the note:

> - **Magurran and Henderson (2003).** In a 21-year estuarine fish record, persistent and abundant "core" species fitted a lognormal, while infrequent "occasional" species fitted a log series [57, AB].
>
> Galand et al. report the same split for rare versus abundant Arctic Ocean prokaryotes (log series versus lognormal) [43, FT].
>
> From general ecology, rarity is classed along local abundance, habitat specificity and geographic range (Rabinowitz 1981, secondary via [47]), core versus occasional species are separated by persistence [57], and abundance and occupancy are usually positively related [58].
>

## 16S/overdispersion.1

Human oral plaque counts rejected the multinomial in favour of the Dirichlet-multinomial, with overdispersion theta of 0.047 and 0.054.

- conf: repl (marker)
- class: meas (marker)
- holds: oral plaque, between biological samples
- src: larosaHypothesisTestingPower2012 (FT; meas; repl)
- trail: MB-01 §4.2, §answers

From the note:

> **Between biological samples.**
>
> - Human oral plaque counts rejected the multinomial in favour of the Dirichlet-multinomial, with overdispersion theta of 0.047 and 0.054 (La Rosa 2012) [FT; meas; repl].
>
> Between biological samples, Dirichlet-multinomial beats multinomial (La Rosa 2012, theta about 0.05 in oral plaque), and public datasets are overdispersed relative to Poisson (McMurdie and Holmes 2014).
>

## 16S/ploidy.21

Flow cytometric cell-cycle analyses of Prochlorococcus (and Synechococcus) in situ are by method taxon-specific measurements of the share of cells with replicated DNA (G1 versus S/G2), so the review's statement that no such share exists for any natural community is not established; nothing comparable was found for soil.

- conf: not stated
- class: not stated
- holds: marine picocyanobacteria in situ; read only at abstract level by the review
- limit: access (critic: MB-02:C-018)
- src: vaulotGrowthProchlorococcusPhotosynthetic1995 (AB)
- trail: MB-02 §critic, §Adversarial

From the note:

> Flow cytometric cell-cycle analyses of Prochlorococcus in situ [24] are by method taxon-specific measurements of the share of cells with replicated DNA.
>
> The review read only the abstract, so its statement that no such share exists for any natural community is not established.
>
> Nothing comparable was found for soil.
>
> - In situ cell-cycle analyses of Prochlorococcus and Synechococcus (Vaulot 1995 and successors) report the fraction of cells in G1 versus S/G2 by taxon in natural seawater.
>
> They were read only at abstract level, and the review asserts that no such share exists for any natural community.
>

## 16S/copy-number-correction.9

Correction changed the identity of the most abundant OTU in about 20% of Human Microbiome Project and 31% of Earth Microbiome Project communities, but against predicted, not measured, truth; in simulations it reduced sample shifts in ordinations but left PERMANOVA variance explained essentially unchanged (5.27 to 19.65% true versus 5.27 to 19.82% uncorrected).

- conf: not stated
- class: not stated
- holds: HMP and EMP communities and simulations; the only figures on how often correction changes the dominant taxon in real communities
- src: gaoAccounting16SRRNA2023 (FT)
- trail: MB-02 §D1.4, §answers, §critic

From the note:

> - **Dominant taxa and ordinations.** Correction changed the most abundant OTU in about 20% of Human Microbiome Project communities and 31% of Earth Microbiome Project communities [33, FT].
>
> In simulations it reduced sample shifts in ordinations but left PERMANOVA variance explained essentially unchanged (5.27 to 19.65% true versus 5.27 to 19.82% uncorrected).
>
> Effects on ecological conclusions are mixed: correction changed the most abundant OTU in about 20% (human) and 31% (Earth Microbiome Project) of communities but left PERMANOVA variance explained essentially unchanged [33]; it changed human body-site clustering but not ocean clustering [28]; it changed enterotype number from two to three [29]; in a forest soil example Acidobacteria rose from 50.1% of sequences to an estimated 66.0% of genomes [6].
>
> Gao and Wu also report that correction changes dominant taxa but not beta-diversity test results, so both camps' observations can hold together.
>
> The only figures on how often correction changes the dominant taxon in real communities rest on Gao and Wu 2023 [33].
>
> It changes dominant taxa often (20 to 31%) but rarely changes beta-diversity test results [33].
>
> Correction changes the identity of the dominant OTU in about 20 to 31% of HMP and EMP communities, but against predicted, not measured, truth.
>
> It barely changes PERMANOVA in simulations [33].
>

## 16S/denoising-clustering.7

After OTU clustering and singleton removal, tables contained approximately 50% (mock communities) to 80% (gnotobiotic mice) spurious taxa; the authors propose a 0.25% relative-abundance cutoff, and the most abundant spurious taxon in mocks had a median relative abundance of 0.12%.

- conf: single (marker)
- class: meas (marker)
- holds: mocks and gnotobiotic mice
- src: reitmeierHandlingSpuriousSequences2021 (FT; meas; single)
- trail: MB-01 §2.10, §2.13, §critic, §Adversarial

From the note:

> - Unfiltered OTU tables were about 50% (mocks) to 80% (gnotobiotic mice) spurious taxa. The authors propose a 0.25% relative-abundance cutoff (Reitmeier 2021) [FT; meas; single].
>
> Unfiltered tables were 50-80% spurious taxa (Reitmeier 2021).
>
> **Spurious-taxon threshold.** The most abundant spurious taxon in mocks had a median relative abundance of 0.12% (Reitmeier 2021).
>
> (d) Reitmeier 2021's 50 to 80% spurious taxa is described as 'unfiltered'; the source says after OTU clustering and singleton removal.
>
> - Reitmeier 2021 (FT): the D2 answer and section 2.10 call the 50 to 80% spurious-taxa figure 'unfiltered'. The source says 'OTU clustering and singleton removal ... delivered approximately 50% (mock communities) to 80% (gnotobiotic mice) spurious taxa'.
>

## 16S/pcr.14

In fungal ITS, pooling 1 to 16 PCR replicates had no detectable effect on alpha or beta diversity.

- conf: not stated
- class: meas (marker)
- holds: fungal ITS, labelled INDIRECT
- src: smithSequenceDepthNot2014 (FT; meas; INDIRECT)
- trail: MB-01 §2.4

From the note:

> - In fungal ITS, pooling 1 to 16 PCR replicates had no detectable effect on alpha or beta diversity (Smith and Peay 2014) [FT; meas; INDIRECT].
>

## 16S/chimeras.1

Chimera detection choices are UCHIME, UCHIME2 or ChimeraSlayer.

- conf: not stated
- class: not stated
- holds: software documentation
- src: edgarUCHIMEImprovesSensitivity2011, edgarUCHIME2ImprovedChimera2016
- trail: MB-01 §answers

From the note:

> Chimera detection: UCHIME, UCHIME2 or ChimeraSlayer.
>

## 16S/pcr.15

Pooled versus single PCR is a disputed choice: Marotz 2019 and Smith and Peay 2014 against the triplicate pooling in the EMP protocol.

- conf: not stated
- class: not stated
- holds: listed among the disputed choices within steps
- src: marotzTriplicatePCRReactions2019, smithSequenceDepthNot2014, earth16SIlluminaAmplicon
- trail: MB-01 §answers

From the note:

> Pooled versus single PCR: Marotz 2019 and Smith and Peay 2014 versus the triplicate pooling in the EMP protocol.
>

## 16S/sampling-storage.4

FTA cards produced a systematic shift that could be detrended, the one storage effect shown to be consistent across samples; for the other preservation methods consistency was not measured.

- conf: not stated
- class: not stated
- holds: faeces (Song 2016)
- src: songPreservationMethodsDiffer2016
- trail: MB-01 §2.1, §answers

From the note:

> FTA cards produced a systematic shift that could be detrended, which is the one storage effect shown to be consistent across samples.
>
> Consistency: FTA cards gave a systematic shift that could be removed; for the other methods consistency was not measured.
>
> Soil storage shifts are small relative to between-soil differences | Smaller | FTA cards: systematic, removable shift.
>
> Otherwise not measured | Song 2016; Rubin 2013 |
>

## 16S/rare-biosphere.8

From general ecology, rarity is classed along local abundance, habitat specificity and geographic range (Rabinowitz 1981), whose concepts the authors of a microbial review say "can be easily transferred to microbial communities"; reviews treat habitat specificity and geographic range as microbial rarity axes alongside local abundance.

- conf: not stated
- class: not stated
- holds: Rabinowitz known only secondarily via Jousset 2017; the original was not obtained
- src: rabinowitzSevenFormsRarity1981 (SEC), joussetWhereLessMay2017 (FT)
- trail: MB-02 §D2.4, §D2.3, §answers

From the note:

> - **Rabinowitz (1981).** Classifies rarity by geographic range, habitat specificity and local abundance.
>
> SECONDARY via [47], whose authors state these concepts "can be easily transferred to microbial communities".
>
> The original was not obtained.
>
> Reviews treat habitat specificity and geographic range as microbial rarity axes alongside local abundance [47, FT].
>
> From general ecology, rarity is classed along local abundance, habitat specificity and geographic range (Rabinowitz 1981, secondary via [47]), core versus occasional species are separated by persistence [57], and abundance and occupancy are usually positively related [58].
>

## 16S/compositional-analysis.4

Proportion-based differential-abundance results err when the community's mean efficiency is associated with the condition.

- conf: single (marker)
- class: model (marker)
- holds: preprint abstract
- src: mclarenImplicationsTaxonomicBias2022 (AB; PREPRINT; model; single)
- trail: MB-01 §5.4, §answers

From the note:

> Proportion-based differential-abundance results err when the community's mean efficiency is associated with the condition (McLaren 2022) [AB; PREPRINT; model; single].
>
> Ratio-based analyses are invariant to multiplicative bias, whereas proportion-based ones are biased when community mean efficiency tracks the condition (McLaren 2019; McLaren 2022 preprint).
>

## 16S/abundance-occupancy.2

Nemergut's authors note that abundant taxa may simply be easier to detect, and that undersampling could hide intermediate distributions.

- conf: not stated
- class: not stated
- holds: the same study
- src: nemergutGlobalPatternsBiogeography2011
- trail: MB-02 §D3.2, §answers

From the note:

> - The authors note that abundant taxa may simply be easier to detect, and that undersampling could hide intermediate distributions.
>
> Sampling and detection: the authors of [62] note abundant taxa may simply be easier to detect.
>

## 16S/sequencing-platform.1

Platform and read-length choices include MiSeq 2x250 or 2x300, HiSeq, NovaSeq, Ion Torrent, 454, and PacBio CCS full length.

- conf: not stated
- class: not stated
- holds: protocols and benchmarks
- src: none (the reviewer's list of choices)
- trail: MB-01 §answers

From the note:

> Platform and read length: MiSeq 2x250 or 2x300, HiSeq, NovaSeq, Ion Torrent, 454, or PacBio CCS full length.
>

## CB1/measured-emissions.2

Cho et al. state that the IPCC assumption that all carbonate C is released "appears unlikely based on current knowledge of the very low solubility of CaCO₃ and carbonate transport through soil."

- conf: not stated
- class: not stated
- holds: Cho et al.'s framing
- src: choEvaluationCarbonDioxide2019 (abstract or structured summary only)
- trail: CB1-LIMING §5. Where the numbers

From the note:

> Their framing is direct: the IPCC assumption that all carbonate C is released "appears unlikely based on current knowledge of the very low solubility of CaCO₃ and carbonate transport through soil.
>
> **Read as abstract or structured summary only**: Wang et al. (2021) [11]; Cho et al. (2019) [12]; Rousset et al. (2024) [13]; Silva et al. (2025) [14]; Holland et al. (2018) [15]; Aramburu Merlos et al. (2023), where I read the full text but used only its framing [16]; Li et al. (2024), where numbers came from an automated extraction of the full article rather than a line-by-line read [17].
>

## CB1/ghg-balance.5

Carbonate lime is itself a carbon dioxide source of contested magnitude.

- conf: cont (note: "a carbon dioxide source of contested magnitude")
- class: not stated
- holds: the review's sections 4 and 5
- src: none (the review's summary of sections 4 and 5)
- trail: CB1-LIMING §Verdict, §Verdict on the scarcity

From the note:

> What the literature does support: lime is bulky, transport dominates its delivered cost, and it is itself a carbon dioxide source of contested magnitude.
>
> What the literature does support is that carbonate lime is bulky, that transport dominates its delivered cost, that its supply chains fail badly in some regions, and that it is itself a carbon dioxide source of contested magnitude.
>

## CB1/delivered-cost.4

Oumer et al. report that a private supplier won a bid to supply core limestone at 47 ETB per cubic metre, equivalent to 5.5 ETB per quintal; average transport cost of finished ag-lime to kebeles was 163 ETB/Qt in Oromia, SNNP and Sidama and 60 ETB/Qt in east Gojjam, with unloading at 10 ETB/Qt and transporter margins of 27–57 ETB/Qt; distance-based rates ran 0.30–0.75 ETB/Qt/km.

- conf: not stated
- class: not stated
- holds: Ethiopia
- src: oumerAgriculturalLimeValue2023
- trail: CB1-LIMING §3. Energy and transport

From the note:

> **The clearest published cost breakdown showing transport dominance is Ethiopian.** Oumer et al. report that a private supplier won a bid to supply core limestone at 47 ETB per cubic metre, equivalent to 5.5 ETB per quintal.
>
> Average transport cost of finished ag-lime to kebeles was 163 ETB/Qt in Oromia, SNNP and Sidama, and 60 ETB/Qt in east Gojjam, with unloading at 10 ETB/Qt and transporter margins of 27–57 ETB/Qt; distance-based rates ran 0.30–0.75 ETB/Qt/km [8].
>

## CB1/consumption.12

The nearest thing to a global-scale quantification is a counterfactual: Wang et al., assuming all acid agricultural soils worldwide were limed periodically, estimate an additional CO₂ release of about 624–656 Tg CO₂/yr from lime mining, transport, application and dissolution combined. That bounds the scale of a fully limed world; it does not describe current practice.

- conf: not stated
- class: model (note: "a counterfactual")
- holds: all acid agricultural soils worldwide limed periodically; not current practice
- src: wangPotentialBenefitsLiming2021 (abstract or structured summary only)
- trail: CB1-LIMING §2. Consumption

From the note:

> The nearest thing to a global-scale quantification is a counterfactual.
>
> Wang et al., assuming all acid agricultural soils worldwide were limed periodically, estimate an additional CO₂ release of about 624–656 Tg CO₂/yr from lime mining, transport, application and dissolution combined [11].
>
> That bounds the scale of a fully limed world; it does not describe current practice.
>
> **Read as abstract or structured summary only**: Wang et al. (2021) [11]; Cho et al. (2019) [12]; Rousset et al. (2024) [13]; Silva et al. (2025) [14]; Holland et al. (2018) [15]; Aramburu Merlos et al. (2023), where I read the full text but used only its framing [16]; Li et al. (2024), where numbers came from an automated extraction of the full article rather than a line-by-line read [17].
>

## CB1/application-frequency.5

The reviewer found no systematic survey establishing the five-year interval.

- conf: not stated
- class: search (note: "I found no systematic survey establishing it")
- holds: the reviewer's searches
- src: none (a statement about what the review found)
- trail: CB1-LIMING §1. Application rates

From the note:

> A five-year interval is therefore common across two very different systems, but I found no systematic survey establishing it.
>

## CB1/ghg-balance.4

The soil-carbon term, which drives much of the difference between these balances, is itself unsettled.

- conf: unclear (note: "is itself unsettled")
- class: not stated
- holds: the soil-carbon term of the whole-system balance
- src: hollandLimingImpactsSoils2018, paradeloNetEffectLiming2015
- trail: CB1-LIMING §5. Where the numbers

From the note:

> The soil-carbon term, which drives much of the difference, is itself unsettled.
>

## CB1/dissolution-pathway.3

"As nitrate concentrations increased in infiltrating waters, lime switched from a net CO₂ sink to a source, implying nitrification as a major acidifying process."

- conf: not stated
- class: not stated
- holds: infiltrating waters in Hamilton et al.'s study
- src: hamiltonEvidenceCarbonSequestration2007
- trail: CB1-LIMING §5. Where the numbers

From the note:

> The condition is explicit and mechanistic: "As nitrate concentrations increased in infiltrating waters, lime switched from a net CO₂ sink to a source, implying nitrification as a major acidifying process" [6].
>

## CB1/nitrification-acidity.1

The acidity being corrected can be tied to nitrogen input: about 3.6 kg CaCO₃ balances the Ca²⁺ lost with nitrate per kg of ammonium-N nitrified (roughly 180 kg CaCO₃ per 50 kg NH₄-N), while neutralising the acid actually formed by nitrifying 50 kg NH₄-N requires about 360 kg CaCO₃.

- conf: not stated
- class: not stated
- holds: two ways of counting the lime needed per unit of ammonium-N nitrified, as given by Goulding (UK review)
- src: gouldingSoilAcidificationImportance2016
- trail: CB1-LIMING §1. Application rates

From the note:

> Second, the acidity being corrected can be tied to nitrogen input: about 3.6 kg CaCO₃ balances the Ca²⁺ lost with nitrate per kg of ammonium-N nitrified, roughly 180 kg CaCO₃ per 50 kg NH₄-N, while neutralising the acid actually formed by nitrifying 50 kg NH₄-N requires about 360 kg CaCO₃ [7].
>

## CB1/lime-access.2

The Ethiopian case study locates the failure in the value chain, not in the deposits: the binding constraints it identifies are demand creation, warehousing, power interruptions, procurement processes, transport, and the absence of a quality standard beyond calcium carbonate equivalence.

- conf: not stated
- class: not stated
- holds: Ethiopia
- src: oumerAgriculturalLimeValue2023
- trail: CB1-LIMING §2. Consumption, §Verdict on the scarcity

From the note:

> But the Ethiopian case study of that same problem locates the failure in the value chain, not in the deposits [8].
>
> The binding constraints they identify are demand creation, warehousing, power interruptions, procurement processes, transport, and the absence of a quality standard beyond calcium carbonate equivalence.
>

## CB1/soil-carbon.2

Paradelo et al. reviewed the literature and found that on balance liming increased soil C content, mostly because it increased yields and therefore residue returns.

- conf: not stated
- class: not stated
- holds: a literature review, as described by Goulding
- src: paradeloNetEffectLiming2015 (second-hand, described by Goulding), gouldingSoilAcidificationImportance2016
- trail: CB1-LIMING §5. Where the numbers

From the note:

> Paradelo et al. reviewed the literature and found that on balance liming increased soil C content, mostly because it increased yields and therefore residue returns [20, described by Goulding at 7].
>
> **Cited second-hand, flagged in text**: West and Marland (2002) [18], whose energy figure I took from West and McBride's quotation of it; Gibbons et al. (2014) [19] and Paradelo et al. (2015) [20], both described to me by Goulding (2016).
>

## CB1/scarcity-claim.7

Two observations could be read as consistent with scarcity but do not evidence it: USGS's urban shortages are planning and land-use pressure, and Beerling et al.'s reliance on existing crushed-limestone infrastructure implies a mature, large-scale extractive industry, which cuts against scarcity rather than for it.

- conf: not stated
- class: reading (note: "Indirect support, labelled as such")
- holds: indirect evidence
- src: willettStoneCrushed2025, beerlingPotentialLargescaleCO22020
- trail: CB1-LIMING §Verdict on the scarcity

From the note:

> **Indirect support, labelled as such.** Two observations could be read as *consistent with* scarcity but do not evidence it.
>
> USGS notes shortages in urban and industrialised areas driven by zoning and land-development competition, pushing quarries further from demand [3] — that is planning and land-use pressure, and USGS presents it as a price driver, not a reserve limitation.
>
> And Beerling et al.'s reliance on existing crushed-limestone infrastructure to argue enhanced weathering is deployable [9] implies a mature, large-scale extractive industry, which cuts against scarcity rather than for it.
>

## CB1/application-frequency.2

West and McBride adopt "a conservative application rate of 5 Mg crushed rock per hectare every 5 years," annualised to about 1 Mg/ha/yr, for their US calculation.

- conf: not stated
- class: not stated
- holds: an assumption in a US calculation
- src: westContributionAgriculturalLime2005
- trail: CB1-LIMING §1. Application rates

From the note:

> West and McBride adopt "a conservative application rate of 5 Mg crushed rock per hectare every 5 years," annualised to about 1 Mg/ha/yr, for their US calculation [5].
>

## CB1/delivered-cost.1

The Beerling et al. preprint gives 2020 US values: transport cost of $0.07/t-km by road and $0.028/t-km by rail, road emissions around 50 g CO₂/t-km and rail around 15 g CO₂/t-km, spreading energy of 21 kWh/t rock giving about 0.005 t CO₂/t spread, and a spreading cost of $5.5 per ton "based on the 2020 values for lime spreading in the United States."

- conf: not stated
- class: not stated
- holds: United States, 2020 values
- src: beerlingTransformingUS2023
- trail: CB1-LIMING §3. Energy and transport

From the note:

> For transport and spreading, the Beerling et al. preprint gives 2020 US values: transport cost of $0.07/t-km by road and $0.028/t-km by rail, road emissions around 50 g CO₂/t-km and rail around 15 g CO₂/t-km, spreading energy of 21 kWh/t rock giving about 0.005 t CO₂/t spread, and a spreading cost of $5.5 per ton "based on the 2020 values for lime spreading in the United States" [10].
>

## CB1/emission-factor.5

The stated uncertainty is one-sided: "The uncertainty is -50% based on approximations suggesting emissions may be less than half of the maximum value, which is the current factor value (West and McBride, 2005) (Note: uncertainties can not exceed the emission factors because these value represent the absolute maximum emissions associated with liming)." The default is a ceiling, and the guidelines say so.

- conf: not stated
- class: not stated
- holds: IPCC 2006 Tier 1
- src: dekleinChapter11N2O2006
- trail: CB1-LIMING §4. Carbon dioxide, §6. What is well established
- rating: "Well established"

From the note:

> **The stated uncertainty is one-sided and unusual.** The guidelines say: "The uncertainty is -50% based on approximations suggesting emissions may be less than half of the maximum value, which is the current factor value (West and McBride, 2005) (Note: uncertainties can not exceed the emission factors because these value represent the absolute maximum emissions associated with liming)" [1].
>
> The default is a ceiling, and the guidelines say so.
>
> Well established: the lime requirement grid for temperate soils, and its strong non-linearity with starting pH and buffering capacity [7].
>
> The IPCC Tier 1 method, its default factors, and their status as a stated maximum with a one-sided −50% uncertainty that the 2019 Refinement left untouched [1, 2].
>

## CB2/marker-gap.1

In SMAG, 3,641 MAGs were high quality with rRNA, and a further 5,184 MAGs reached ≥90% completeness and <5% contamination but failed on "the absence of all rRNA genes or less than 18 tRNAs".

- conf: not stated
- class: not stated
- holds: soil (SMAG)
- src: maGenomicCatalogueSoil2023
- trail: CB2-RRNA §2. Side by side

From the note:

> - **Soil (SMAG).** 3,641 MAGs were high quality *with* rRNA; a further 5,184 MAGs reached ≥90% completeness and <5% contamination but failed on "the absence of all rRNA genes or less than 18 tRNAs".
>

## CB2/targeted-reconstruction.5

All methods handled genes sharing <90% identity with their nearest neighbour, but "performances significantly dropped" for paralogous copies around 99% identity, where EMIRGE and REAGO merged reads from distinct paralogs into single erroneous sequences.

- conf: not stated
- class: not stated
- holds: the MATAM paper's benchmark
- src: pericardMATAMReconstructionPhylogenetic2018
- trail: CB2-RRNA §4. Bounding facts

From the note:

> The authors note that all methods handled genes sharing <90% identity with their nearest neighbour, and that "performances significantly dropped" for paralogous copies around 99% identity, where EMIRGE and REAGO merged reads from distinct paralogs into single erroneous sequences.
>

## CB2/marker-gap.4

In UHGG, 3,207 of 4,644 species representatives were >90% complete and <5% contaminated; 573 additionally had 5S/16S/23S plus ≥18 tRNAs, and only 38 of those 573 were MAGs. The paper attributes this to the rRNA operon being "a problematic region to assemble from short-read metagenomic datasets".

- conf: not stated
- class: not stated
- holds: human gut species representatives
- src: almeidaUnifiedCatalog2042020
- trail: CB2-RRNA §2. Side by side

From the note:

> - **Human gut (UHGG).** 3,207 of 4,644 species representatives were >90% complete and <5% contaminated; 573 additionally had 5S/16S/23S plus ≥18 tRNAs — and only 38 of those 573 were MAGs.
>
> The paper attributes this to the rRNA operon being "a problematic region to assemble from short-read metagenomic datasets".
>

## CB2/depth-axis.2

Philip et al. report a coverage floor: "we need more than 10 read pairs, and in most cases more then 40, to be able to reconstruct a 16S with some substantial length".

- conf: not stated
- class: not stated
- holds: METASEED reconstruction
- src: philipMETASEEDNovelApproach2024 (single-pass extraction)
- trail: CB2-RRNA §5. What is measured

From the note:

> Philip et al. report the coverage floor from the other side: "we need more than 10 read pairs, and in most cases more then 40, to be able to reconstruct a 16S with some substantial length" (single-pass extraction).
>

## CB2/recovery-variation.1

Of the four axes of variation in rRNA recovery, direct evidence was found for three (read length and sequencing technology, assembler choice, sequencing depth) and none for the fourth (study of origin); the four have very different evidentiary status.

- conf: not stated
- class: not stated
- holds: the literature the reviewer searched
- src: none (the review's verdict over sections 2 to 5)
- trail: CB2-RRNA §Verdict, §5. What is measured, §Verdict on the second

From the note:

> **Direct evidence found for three of the four axes; for study of origin, NO EVIDENCE EXISTS.**
>
> **Direct evidence found — for three of the four axes; no evidence exists for the fourth.**
>
> This is the second target of the brief, and the four axes it names have very different evidentiary status.
>

## CB2/targeted-reconstruction.1

Targeted tools recover far more than general assembly: Yuan et al. benchmarked generic assemblers against targeted ones.

- conf: not stated
- class: not stated
- holds: Yuan et al.'s simulated and synthetic sets (targeted-reconstruction.2, .3)
- src: yuanReconstructing16SRRNA2015
- trail: CB2-RRNA §4. Bounding facts

From the note:

> **Targeted tools recover far more than general assembly.** Yuan et al. benchmarked generic assemblers against targeted ones.
>

## CB2/linking-tools.1

Linking tools recover part but not most of the gap: MarkerMAG, on benchmark datasets at 100% linking accuracy, recovered 88.2% (15/17 MAGs, low-complexity MBARC-26), 53.5% (23/43, medium) and 46.7% (14/30, high complexity); on real data the improvement over baseline ranged from 1.1-fold (macroalgae) to 14.2-fold (pig gut).

- conf: not stated
- class: not stated
- holds: benchmark datasets of three complexities; real data from macroalgae to pig gut
- src: songMarkerMAGLinkingMetagenomeassembled2022 (single-pass extraction of the article HTML)
- trail: CB2-RRNA §4. Bounding facts

From the note:

> **Linking tools recover part but not most of the gap.** MarkerMAG, on benchmark datasets at 100% linking accuracy, recovered 88.2% (15/17 MAGs, low-complexity MBARC-26), 53.5% (23/43, medium) and 46.7% (14/30, high complexity); on real data the improvement over baseline ranged from 1.1-fold (macroalgae) to 14.2-fold (pig gut).
>
> These figures come from a single-pass extraction of the article HTML.
>

## CB2/read-length-axis.6

The published version of Overholt et al. adds an ONT-only assembly and reports in the abstract that the ONT-only MAGs had a probability of containing rRNA genes "3× higher than either of the other methods."

- conf: not stated
- class: not stated
- holds: aquifer samples; the published version's abstract
- src: overholtInclusionOxfordNanopore2020
- trail: CB2-RRNA §5. What is measured

From the note:

> The published version adds an ONT-only assembly and reports in the abstract that the ONT-only MAGs had a probability of containing rRNA genes "3× higher than either of the other methods.
>

## CB3/food-system.2

IPCC SRCCL (2019) gave 21–37% of total net anthropogenic GHG emissions for the food system, 2007–2016, medium confidence.

- conf: not stated
- class: not stated
- holds: 2007–2016; CO2, CH4 and N2O
- src: ipccSummaryPolicymakers2019 (section A.3 and its footnotes)
- trail: CB3-AG-EMISSIONS §Boundary A, §Table of candidate shares
- rating: "medium confidence"

From the note:

> **IPCC SRCCL (2019)** gave **21–37%** of total net anthropogenic GHG emissions for 2007–2016, *medium confidence*, and disaggregated it: "Emissions within farm gate and from agricultural land expansion contributing to the global food system represent 16–27% of total anthropogenic emissions (medium confidence).
>
> | 2 | Food system, incl. all supply chain | 21–37% | — | 2007–2016 | CO2, CH4, N2O | IPCC SRCCL SPM A.3 [2] | *medium confidence* |
>

## CB3/food-system.13

Poore & Nemecek 2018: "A further 2.8 billion metric tons of CO2eq (5%) are caused by nonfood agriculture and other drivers of deforestation".

- conf: not stated
- class: not stated
- holds: non-food agriculture and other deforestation drivers; ~2010 baseline
- src: pooreReducingFoodS2018
- trail: CB3-AG-EMISSIONS §Boundary A

From the note:

> A further 2.8 billion metric tons of CO2eq (**5%**) are caused by nonfood agriculture and other drivers of deforestation" [10].
>
> | 8 | Non-food agriculture + other deforestation drivers | 5% | 2.8 Gt CO2eq | as above | as above | Poore & Nemecek 2018 [10] | not stated |
>

## CB3/gwp-metric.4

Lynch et al. do not offer a replacement share; the criticism attacks the aggregation, not the inventory.

- conf: not stated
- class: not stated
- holds: Lynch et al. 2021 as the review read it
- src: lynchAgricultureSContribution2021
- trail: CB3-AG-EMISSIONS §Bounding and negative facts

From the note:

> They do not offer a replacement *share*; the criticism attacks the aggregation, not the inventory.
>

## CB3/five-percent.2

Three boundaries land close enough that a "roughly 5%" claim could have originated from any of them, and they are not interchangeable: N2O from agricultural soils at 4.1% (Climate Watch/WRI 2016 via Our World in Data, which the review calls its own weakest-supported number, one unverified secondary presentation); all anthropogenic N2O across every sector at ~4.7%; and emissions outside the farm gate at 5–10%.

- conf: not stated
- class: not stated
- holds: Climate Watch/WRI via OWID (2016), AR6 WGIII Ch. 7 Table 7.1 (2010–2019), SRCCL A.3.6 (2007–2016)
- src: ritchieSectorSectorWhere2020, nabuursAgricultureForestryOther2022, ipccSummaryPolicymakers2019
- trail: CB3-AG-EMISSIONS §Verdict, §Verdict: which boundary

From the note:

> Three boundaries land close enough that a “roughly 5%” claim could have originated from any: N₂O from agricultural soils at 4.1% (Climate Watch/WRI 2016 via Our World in Data — the review calls this its own weakest-supported number, one unverified secondary presentation); all anthropogenic N₂O across every sector at ~4.7%; and emissions outside the farm gate at 5–10%.
>
> **No boundary in the current authoritative literature produces exactly five per cent for agriculture, and none produces it for agricultural soils.** Three boundaries land close enough that a "roughly 5%" claim could have originated from any of them, and they are not interchangeable:
>

## CB3/accounting-boundary.2

Gas coverage differs between sources: SRCCL's 23% AFOLU figure covers only CO2, CH4 and N2O, while EDGAR-FOOD and FAOSTAT include F-gases.

- conf: not stated
- class: not stated
- holds: SRCCL footnote 21; EDGAR-FOOD (Crippa et al. 2021) and FAOSTAT (Tubiello et al. 2022)
- src: ipccSummaryPolicymakers2019, crippaFoodSystemsResponsible2021, tubielloPrePostproductionProcesses2022
- trail: CB3-AG-EMISSIONS §Where the major sources differ

From the note:

> **Gas coverage.** SRCCL's 23% covers only CO2, CH4 and N2O [2, fn 21]; EDGAR-FOOD and FAOSTAT include F-gases [3, 4].
>

## CB3/five-percent.5

Emissions outside the farm gate (5–10%, SRCCL) and non-food agriculture plus other deforestation drivers (5%, Poore & Nemecek) are both exactly 5% at one end, and both are about something else entirely: supply chains and non-food crops.

- conf: not stated
- class: not stated
- holds: SRCCL A.3.6 (2007–2016); Poore & Nemecek 2018
- src: ipccSummaryPolicymakers2019, pooreReducingFoodS2018
- trail: CB3-AG-EMISSIONS §Verdict: which boundary

From the note:

> **Emissions outside the farm gate: 5–10%**, SRCCL [2]; and **non-food agriculture plus other deforestation drivers: 5%**, Poore & Nemecek [10].
>
> Both are exactly 5% at one end, and both are about something else entirely — supply chains and non-food crops.
>

## CB3/n2o.2

All anthropogenic N2O, every sector, is 2.6 / 55.9 = ~4.7% of all anthropogenic GHG in 2010–2019 (the review's arithmetic from Table 7.1); it includes fossil fuel, industry, waste and biomass burning N2O, not just agriculture.

- conf: not stated
- class: deriv (note: "My arithmetic")
- holds: all sectors; 2010–2019; AR6 GWP100; ±1.5 Gt and 60% uncertainty on N2O
- src: nabuursAgricultureForestryOther2022 (the review's arithmetic on its figures)
- trail: CB3-AG-EMISSIONS §Boundary D, §Verdict: which boundary

From the note:

> *My arithmetic:* 2.6 / 55.9 = **4.7%** of all anthropogenic GHG in 2010–2019.
>
> **All anthropogenic nitrous oxide, every sector: ~4.7%** of 2010–2019 global GHG [1, my arithmetic from Table 7.1].
>
> If a "5%" claim is really about N2O rather than about soils, this is what it matches — but it includes fossil fuel, industry, waste and biomass burning N2O, not just agriculture.
>
> | 20 | Total anthropogenic N2O, all sectors | ~4.7% *(my arithmetic)* | 2.6 GtCO2-eq | 2010–2019 | N2O; AR6 GWP100 | AR6 WGIII Ch.7 Table 7.1 [1] | ±1.5 Gt; 60% on N2O |
>

## CB3/co2-accounting.2

The AR6 Figure 7.3 caption warns that AFOLU CO2 from bookkeeping models "is not directly comparable to LULUCF in NGHGIs".

- conf: not stated
- class: not stated
- holds: AFOLU CO2 versus NGHGI LULUCF, AR6 WGIII Ch. 7 Figure 7.3 caption
- src: nabuursAgricultureForestryOther2022
- trail: CB3-AG-EMISSIONS §Where the major sources differ, §Bounding and negative facts

From the note:

> The Figure 7.3 caption warns that AFOLU CO2 from bookkeeping models "is *not directly comparable to LULUCF in NGHGIs*" [1].
>
> AR6 Figure 7.3 caption, on AFOLU CO2 vs NGHGI LULUCF, as quoted above [1].
>

## CB3/soils.6

Climate Watch/WRI, as presented by Our World in Data for 2016, gives "Agricultural soils (4.1%)": nitrous oxide produced when synthetic nitrogen fertilizers are applied to soils, including emissions from agricultural soils for all agricultural products (food for direct human consumption, animal feed, biofuels, and other non-food crops).

- conf: single (note: "single-source")
- class: not stated
- holds: inventory category (3.D-equivalent); 2016; GWP100; no uncertainty statement; one secondary presentation, not verified against the primary dataset
- src: ritchieSectorSectorWhere2020 (secondary presentation, unverified against the underlying dataset)
- trail: CB3-AG-EMISSIONS §Boundary D, §What this review does, §Verdict: which boundary
- rating: "the weakest-supported number in this review"
- limit: access (note: "which I could verify only as presented by Our World in Data")

From the note:

> **Agricultural soils as an inventory category.** Climate Watch/WRI, as presented by Our World in Data for 2016, gives "**Agricultural soils (4.1%)**: nitrous oxide — a strong greenhouse gas — is produced when synthetic nitrogen fertilizers are applied to soils.
>
> This includes emissions from agricultural soils for all agricultural products — including food for direct human consumption, animal feed, biofuels, and other non-food crops" [11].
>
> **Single source, secondary presentation, unverified against the underlying dataset.**
>
> **One important caution up front.** A single number appears only once in this review and carries real weight in the verdict — the Climate Watch/WRI "agricultural soils 4.1%" figure, which I could verify only as presented by Our World in Data [11], not in the Climate Watch dataset itself.
>
> That claim's support is **thin and single-source**, and I flag it as such wherever it appears.
>
> **Nitrous oxide from agricultural soils (inventory category 3.D-equivalent): 4.1%**, Climate Watch/WRI for 2016, as presented by Our World in Data [11].
>
> It is also the weakest-supported number in this review: one secondary presentation, no uncertainty statement, not verified against the primary dataset.
>
> The 4.1% end rests on a single unverified source.
>
> | 21 | **Agricultural soils (inventory category)** | **4.1%** | — | 2016 | GWP100 | Climate Watch/WRI via OWID [11] | **none given; single source** |
>

## CB3/food-system.1

The food-system boundary is the broadest: farm-gate production, plus land-use change attributed to agriculture, plus everything up- and downstream (fertiliser manufacture, processing, packaging, transport, retail, household cooking, food waste disposal).

- conf: not stated
- class: not stated
- holds: the review's definition of Boundary A
- src: none (the reviewer's definition)
- trail: CB3-AG-EMISSIONS §Boundary A

From the note:

> This is the broadest boundary: farm-gate production, plus land-use change attributed to agriculture, plus everything up- and downstream (fertiliser manufacture, processing, packaging, transport, retail, household cooking, food waste disposal).
>

## CB3/livestock.2

FAO's 2023 assessment lowered the livestock figure again, to about 6.2 Gt CO2eq for 2015, ~12% of anthropogenic emissions.

- conf: not stated
- class: not stated
- holds: livestock agrifood systems; 2015; GLEAM
- src: faoPathwaysTowardsLower2023 (retrieved via FAO's own press summary and repository listing; reported as secondary)
- trail: CB3-AG-EMISSIONS §Boundary C

From the note:

> FAO's 2023 assessment lowered it again to about 6.2 Gt CO2eq for 2015, ~12% of anthropogenic emissions [17].
>
> | 19 | Livestock agrifood systems | ~12% | 6.2 Gt CO2eq | 2015 | GLEAM | FAO 2023 [17] | not retrieved |
>

## GHOST/missingness-degradation.1

On homophilous, sparse-feature graphs under MCAR missingness, diffusion / propagation imputation (Feature Propagation and variants) reconstructs entirely-missing node features from observed neighbours and degrades only marginally, ~2–4% relative node-classification accuracy at 99% missing, while model-internal imputation (GCNMF) collapses to ~35% on the same benchmark.

- conf: repl (note: "The single most replicated empirical result")
- class: meas (note: "empirical result")
- holds: only the homophilous-sparse-MCAR-scoped version survived verification (the critic, against R7); the ~2–4% range is the note's own, spanning R1 and R2
- src: rossiUnreasonableEffectivenessFeature2022, leiSelfsupervisedGuidedHypergraph2023, chenLearningAttributeMissingGraphs2022
- trail: GHOST §Verdict, §critic

From the note:

> The single most replicated empirical result is that diffusion/propagation imputation (Feature Propagation and variants) reconstructs entirely-missing node features from observed neighbours and degrades only marginally — ~2–4% relative node-classification accuracy at 99% missing — while model-internal imputation (GCNMF) collapses to ~35% on the same benchmark [R1, R2, R3].
>
> - ✗ **"FP robustness (~4% at 99% missing) is a general fact."** Vote 1-2. The *unscoped* version fails; only the homophilous-sparse-MCAR-scoped version survives [R1, contra R7].
>

## GHOST/benchmark-regime.3

The dominance of propagation on standard benchmarks may be an artefact of the benchmarks, not a regime-general property.

- conf: not stated
- class: reading (note: "so the dominance of propagation on standard benchmarks may be an artifact")
- holds: the review's inference from R7's result on sparse benchmarks
- src: ferriniRethinkingGNNsMissing2026
- trail: GHOST §Verdict

From the note:

> **A 2026 result proves the benchmark itself hides the differences.** High feature sparsity provably bounds the information loss from missingness, "making all models appear robust and preventing a meaningful comparison" — so the dominance of propagation on standard benchmarks may be an artifact, not a regime-general property [R7].
>

## GHOST/feature-propagation.3

FP outperformed prior missing-feature methods on its seven benchmarks.

- conf: not stated
- class: not stated
- holds: seven benchmarks, 2022; homophilous + sparse + MCAR, and mostly author-reported
- src: rossiUnreasonableEffectivenessFeature2022
- trail: GHOST §2. Degradation

From the note:

> - FP: on average ~4% relative node-classification accuracy drop at **99% missing** across seven benchmarks; it outperformed prior missing-feature methods on those benchmarks [R1].
>
> **Caveat carried on every number above:** homophilous + sparse + MCAR, and mostly author-reported.
>

## GHOST/missingness-degradation.7

EGS degrades gently against a PAGNN baseline: on Cora from 5% to 75% missing, the baseline goes from 81.36 to 74.05 and EGS from 84.77 to 82.13.

- conf: not stated
- class: not stated
- holds: Cora, 5% to 75% missing; self-reported by the method's authors
- src: songDynamicGraphStructure2025 (self-reported)
- rating: "Confidence: high."
- trail: GHOST §2. Degradation

From the note:

> - EGS degrades gently vs a PAGNN baseline (Cora, 5%→75% missing: baseline 81.36→74.05; EGS 84.77→82.13) — self-reported [R4].
>
> *Confidence: high.*
>
> **Caveat carried on every number above:** homophilous + sparse + MCAR, and mostly author-reported.
>

## H1-02/artefact-size.2

The three direct sources measure different things in two environments (two human gut, one coastal marine), and their effect sizes are not commensurable: percentages of population core or variable genes, a median gene count, and a fraction of differentially prevalent genes; they are reported separately and not pooled.

- conf: single (note: "All three direct sources are SINGLE SOURCE in their setting")
- class: not stated
- holds: Meziti et al., Orellana et al., Majernik et al.; each single in its setting (the critic)
- src: mezitiReliabilityMetagenomeassembledGenomes2021, orellanaComparingGenomesRecovered2023, majernikSmallAmountsMisassembly2025
- trail: H1-02 §4. Where, §Adversarial critique

From the note:

> All three direct sources are SINGLE SOURCE in their setting.
>
> Two are human gut and one is coastal marine.
>
> Effect sizes are not commensurable across them: [1] reports percentages of population core or variable genes, [12] reports a median gene count, and [22] reports a fraction of differentially prevalent genes.
>
> They are reported separately here and not pooled.
>
> They measure different things in two environments, and each is single in its setting.
>

## H1-02/artefact-size.5

One natural biocrust soil shows systematic short-read assembly loss of variable regions, which is indirect support only for soil.

- conf: not stated
- class: not stated
- holds: one natural biocrust soil; assembly loss, not gene content of recovered genomes
- src: bergComparisonShortreadLongread2025
- trail: H1-02 §Verdict as delivered, §5. Verdicts

From the note:

> One natural biocrust soil shows systematic short-read assembly loss of variable regions [26], which is indirect support only.
>
> Berg et al. [26] is indirect support.
>

## H1-02/sequencing-depth.5

In simulations, completeness correlated with depth at ρ = 0.20.

- conf: not stated
- class: model (note: "modelled")
- holds: Kim et al.'s simulations
- src: kimComprehensiveBenchmarkingMetagenomic2026
- trail: H1-02 §3.5

From the note:

> Kim et al.'s simulations [27] gave completeness correlations of ρ = 0.20 with depth and ρ = −0.55 with taxonomic complexity (modelled).
>

## H1-02/chimerism.1

GUNC flagged 15.1% to 29.9% of CheckM-prefiltered human gut MAG catalogues as chimeric at genus level or above, the rate ranging by study.

- conf: not stated
- class: not stated
- holds: natural human gut catalogues; the study measures chimerism, not called gene content; the critic: study of origin is confounded with pipeline and sample set, and the source rests on agent reads
- src: orakovGUNCDetectionChimerism2021
- trail: H1-02 §2.2, §3.1, §critic, §Adversarial critique

From the note:

> Orakov et al. [9] found that GUNC flagged 15.1% to 29.9% of CheckM-prefiltered human gut MAG catalogues as chimeric at genus level or above.
>
> The study measures chimerism, not called gene content.
>
> Chimerism in CheckM-prefiltered catalogues ranged from 15.1% to 29.9% by study [9].
>
> In [9], study of origin is confounded with pipeline and sample set.
>
> [3] and [9] rest on agent reads.
>

## H1-02/same-sample-isolate.5

The paper attributes the low-identity share of missed genes to sequence divergence from the isolate or to assembly errors, so part of the loss may be biology and not recovery.

- conf: not stated
- class: not stated
- holds: the critic's reading of the full text of Meziti et al.
- src: mezitiReliabilityMetagenomeassembledGenomes2021
- trail: H1-02 §critic, §Adversarial critique

From the note:

> The low-identity share of missed genes is attributed to sequence divergence from the isolate or to assembly errors.
>
> [1] attributes low-identity missed genes to sequence differences from the isolate or to assembly errors, so part of the 'loss' may be biology and not recovery.
>

## H1-02/artefact-size.6

Removing Meziti et al. would leave Part A as measured and material on Majernik et al. and Orellana et al., but would remove the only natural same-sample isolate comparison and every figure for missed core and variable genes, since Li and Yin reuse its data.

- conf: not stated
- class: not stated
- holds: the review's sensitivity analysis
- src: mezitiReliabilityMetagenomeassembledGenomes2021, majernikSmallAmountsMisassembly2025, orellanaComparingGenomesRecovered2023, liCriticalAssessmentPangenomic2022
- trail: H1-02 §5. Verdicts

From the note:

> **Sensitivity to single sources.** Removing Meziti et al. [1] would leave Part A as "measured and material" on [22] and [12], but would remove the only natural same-sample isolate comparison and every figure for missed core and variable genes ([2] reuses [1]'s data).
>

## H1-02/contaminated-pangenome.4

A quick re-run on Bacteroides thetaiotaomicron in the same data set gave 30 genes.

- conf: single (critic: C-054)
- class: not stated
- holds: the same cirrhosis data set
- src: majernikSmallAmountsMisassembly2025
- trail: H1-02 §Adversarial critique

From the note:

> - Contamination-driven false gene associations (38%, 33/86) come from one cirrhosis cohort and one family, Lachnospiraceae [22]. The quick re-run on Bacteroides thetaiotaomicron was 30 genes in the same data set.
>

## H1-02/sample-dependence.3

In the human gut, dependence on community diversity and sequencing depth was not measured for gene content, and no study measuring how gene-content artefacts between conspecific MAGs scale with community diversity or depth across samples was found.

- conf: not stated
- class: search (note: "Routes: WebSearch and Europe PMC on sequencing effort")
- holds: routes: WebSearch and Europe PMC on sequencing effort against binning, batch or study effects in MAG catalogues, and soil MAG against depth
- src: none (a search result)
- trail: H1-02 §Verdict as delivered, §5. Verdicts, §3.1, §Search record

From the note:

> Dependence on community diversity and sequencing depth: NOT MEASURED for gene content in the gut.
>
> Not measured for diversity.
>
> No gut study measured how gene-content artefacts scale with community diversity.
>
> (3) Any study measuring how gene-content artefacts between conspecific MAGs scale with community diversity or depth across samples.
>
> Routes: WebSearch and Europe PMC on sequencing effort against binning, batch or study effects in MAG catalogues, and soil MAG against depth.
>

## H1-02/sequencing-depth.6

Depth effects on true-positive recovery reversed between pipelines around 60 million reads.

- conf: not stated
- class: model (note: "modelled")
- holds: simulated communities
- src: rochaSimulation69Microbial2024
- trail: H1-02 §3.5

From the note:

> Rocha et al. [34] found that depth effects on true-positive recovery reversed between pipelines around 60 million reads (modelled).
>

## H1-02/mobile-region-loss.5

In a simulated 30-genome short-read metagenome, across 12 assembler and binner combinations, 82% to 94% of chromosomes were recovered, against 38% to 44% of genomic islands and 1% to 29% of plasmids.

- conf: not stated
- class: model (note: "simulated a 30-genome short-read metagenome")
- holds: one simulated 30-genome community
- src: maguireMetagenomeAssembledGenomeBinning2020
- trail: H1-02 §2.4

From the note:

> Maguire et al. [4] simulated a 30-genome short-read metagenome.
>
> Across 12 assembler and binner combinations, 82% to 94% of chromosomes were recovered, against 38% to 44% of genomic islands and 1% to 29% of plasmids.
>

## H1-02/core-genome-inference.3

The authors state that random removal may overestimate core loss.

- conf: not stated
- class: not stated
- holds: Li and Yin's simulations
- src: liCriticalAssessmentPangenomic2022
- trail: H1-02 §2.5

From the note:

> The authors state that random removal "may overestimate" core loss.
>

## H1-02/mobile-region-loss.1

Comparing curated MAGs from two laboratory enrichment consortia with ten isolate genomes from the same cultures, genomes at 10x coverage or more had over 90% of their sequence recovered (85% at 11x; about 40% at 3.9x).

- conf: not stated
- class: not stated
- holds: engineered, two laboratory enrichment consortia
- src: nelsonBiasesGenomeReconstruction2020
- trail: H1-02 §2.4

From the note:

> Nelson et al. [5] compared curated MAGs from two laboratory enrichment consortia with ten isolate genomes from the same cultures.
>
> Genomes at 10x coverage or more had over 90% of their sequence recovered (85% at 11x; about 40% at 3.9x).
>

## H1-02/sample-dependence.7

In soil, dependence of the gene or pathway content of related recovered genomes on sample properties was not measured in this setting, and there is indirect recovery-quality evidence only; none of the soil evidence measures the gene or pathway content of related genomes recovered from different soil samples.

- conf: not stated
- class: search (critic: C-012)
- holds: natural soil
- src: none (a search result)
- trail: H1-02 §critic, §Verdict as delivered, §5. Verdicts, §3.3

From the note:

> Part B, soil and sediment: NOT MEASURED IN THIS SETTING, with indirect recovery-quality evidence only.
>
> Dependence on sample properties: soil (natural)**: NOT MEASURED IN THIS SETTING for gene or pathway content of related recovered genomes.
>
> - Soil: **not measured in this setting**.
>
> None of it measures the gene or pathway content of related genomes recovered from different soil samples.
>

## H1-02/filters-corrections.5

CELEBRIMBOR was validated on simulations, and the authors state that non-random loss violates its missing-at-random assumption.

- conf: not stated
- class: not stated
- holds: simulations
- src: hellewellCELEBRIMBORCoreAccessory2024
- trail: H1-02 §2.7

From the note:

> CELEBRIMBOR [19] was validated on simulations, and the authors state that non-random loss violates its missing-at-random assumption. mOTUpan [14] was checked against a few closed Prochlorococcus genomes plus bootstraps, and its authors state that genes hard to assemble or bin leave "an inevitable underestimate of the accessory genomes".
>

## H1-02/mobile-region-loss.8

In a natural biocrust soil community, short-read assemblies were checked against a PacBio HiFi assembly of the same system: of 614 long-read bins, only 24 had at least half their 1 kb segments fully recovered by short reads, while 490 had at least half not recovered.

- conf: not stated
- class: not stated
- holds: one site; the reference is long-read bins, not isolates; concerns assembly, not the gene content of binned genomes compared across samples
- src: bergComparisonShortreadLongread2025
- trail: H1-02 §2.4

From the note:

> Berg et al. [26] provide the only natural soil evidence.
>
> In a biocrust community, short-read assemblies were checked against a PacBio HiFi assembly of the same system.
>
> Of 614 long-read bins, only 24 had at least half their 1 kb segments fully recovered by short reads, while 490 had at least half not recovered.
>
> The authors conclude that short-read metagenomes "can possibly underestimate the diversity of these genome regions" (measured; natural; one site; the reference is long-read bins, not isolates).
>
> This concerns assembly, not the gene content of binned genomes compared across samples.
>

## H1-05/measurement-artefacts.2

In soil, the ordering has not been measured across dissimilarity measures, compositional (log-ratio) transforms, KO vs COG vs pangenome clusters vs MAG-resolved traits, rarefaction depth, relic-DNA removal or genome-size normalization, so no reversal of ordering by any of these was found because none was tested.

- conf: not stated
- class: search (note: "none was tested")
- holds: soil
- src: none (a search result)
- trail: H1-05 §answers

From the note:

> *Not measured:* Soil: ordering across dissimilarity measures, compositional (log-ratio) transforms, KO vs COG vs pangenome clusters vs MAG-resolved traits, rarefaction depth, relic-DNA removal, and genome-size normalization (Nayfach [47] shows the bias in human gut only; soil genome-size shifts are reported in [2] and [8] but not tested for their effect on turnover).
>
> No reversal of ordering by any of these factors was found in soil because none was tested..
>

## H1-05/ordering.24

The reverse ordering (function responds where taxonomy does not) rests on two GeoChip studies from one group [5][15], one abstract only, plus a reviewer's reading of [6]; removing [5] would leave it supported only by the abstract-only [15] and the reading of [6].

- conf: not stated
- class: not stated
- holds: weak contrasts: 14 years of moderate warming [5], erosion and deposition [15], an elevation gradient [6]; n = 4 per treatment in [5]; platforms differ
- src: gaoLongtermWarmingMediterraneantype2021, maDivergentTaxonomicFunctional2017, shenDramaticIncreasesSoil2016
- trail: H1-05 §critic, §answers
- rating: "Weak for the reverse ordering"

From the note:

> The reverse ordering rests on two GeoChip studies from one group [5][15] (one abstract only) plus a reviewer's reading of [6].
>
> The reverse ordering is reported under weak contrasts.
>
> Weak for the reverse ordering (n = 4 per treatment in [5]; platforms differ)..
>
> Removing Gao et al. 2021 [5] would leave the reverse ordering supported only by an abstract-only study [15] and a reviewer's reading of [6].
>

## H1-05/redundancy.1

The review counts as arguments for redundancy (asserted or measured without nulls) [3][4][7][13][18][24] in soil and [33][35][36][37] elsewhere; the answers list [3][4][7][33][34].

- conf: not stated
- class: not stated
- holds: the review's classification of its sources
- src: chenFunctionalRedundancySoil2022, igweRedundancyMaintainsMicrobial2026, zhangSoilBacterialEndemism2016, panImpactLongtermN2014, souzaMetagenomicAnalysisReveals2015, saumasanchezFunctionalRedundancyBuffers2024, loucaHighTaxonomicVariability2016, burkeBacterialCommunityAssembly2011, vanderloosLowFunctionalChange2025, soufiTaxonomicVariabilityFunctional2024, loucaFunctionFunctionalRedundancy2018
- trail: H1-05 §3.4, §answers

From the note:

> - **For** (asserted or measured without nulls): [3][4][7][13][18][24] in soil.
>
> [33][35][36][37] elsewhere.
>
> Arguments on redundancy: for, [3][4][7][33][34].
>

## H1-05/marker-inferred.3

Soil PICRUSt2-inferred profiles are not independent of taxonomy: the ZnO and alpine studies infer function from the same 16S data, so they are not independent tests, and they report either decoupling [25] or functional dissimilarity closer to phylogenetic than to taxonomic dissimilarity [26].

- conf: not stated
- class: not stated
- holds: marker-inferred function in soil
- src: dineshSoilPollutedNano2023, liAsynchronousPatternsSoil2024
- trail: H1-05 §1.2, §answers

From the note:

> Both infer function from the same 16S data, so they are not independent tests.
>
> Soil PICRUSt2-inferred profiles are not independent of taxonomy, and such studies report either decoupling [25] or functional dissimilarity closer to phylogenetic than to taxonomic dissimilarity [26].
>

## H1-05/contrast-size.3

Across studies, strong contrasts [1][2] give covariation, while weak single-site contrasts give both orderings.

- conf: not stated
- class: not stated
- holds: cross-study comparison of soil studies
- src: fiererCrossbiomeMetagenomicAnalyses2012, leffConsistentResponsesSoil2015
- trail: H1-05 §1.4, §answers

From the note:

> Across studies, strong contrasts [1][2] give covariation.
>
> On contrast size: covariation is shown mainly at strong contrasts.
>

## H1-05/other-habitats.7

During vermicomposting, PICRUSt2 turnover was about 12 times slower than taxonomic turnover.

- conf: not stated
- class: deriv (marker)
- holds: vermicomposting [45]; PICRUSt2-inferred function
- src: airaFasterTurnoverTaxonomic2026 (FT via agents; derived)
- trail: H1-05 §1.6

From the note:

> - Vermicomposting: PICRUSt2 turnover about 12 times slower than taxonomic turnover [45] [FT via agents; derived].
>

## H1-05/ordering.1

Covariation says nothing about which turnover is larger: a correlation between dissimilarity matrices says nothing about their relative magnitudes, so covariation and "function less variable" are compatible.

- conf: not stated
- class: not stated
- holds: the critic's and the reviewer's reasoning about correlation-type tests
- src: none (the critic's and the reviewer's reasoning)
- trail: H1-05 §critic, §5

From the note:

> Covariation says nothing about which turnover is larger.
>
> Covariation and "function less variable" are compatible.
>

## H1-05/functional-unit.6

In lake enrichments, redundancy was higher with EC grouping than with KO.

- conf: not stated
- class: not stated
- holds: lake enrichment communities [38]
- src: lemoigneLinkingStochasticAssembly2026 (FT via agents)
- trail: H1-05 §2, §answers

From the note:

> In lake enrichments, redundancy was higher with EC grouping than with KO [38].
>
> Outside soil, inoculum identity was recoverable at genus but less at phylum level [44] [AB], and lake-enrichment redundancy was higher with EC than KO grouping [38] [FT via agents].
>

## H1-05/functional-unit.2

In the global soil metagenome comparison, functional similarity exceeded taxonomic similarity at SEED levels 1 and 2 against all five taxonomic ranks, so the ordering did not reverse at any combination tested.

- conf: single (critic: H1-05:C-012)
- class: not stated
- holds: [3], the only soil study reporting the comparison at several annotation levels; removing it leaves no soil evidence on annotation level
- src: chenFunctionalRedundancySoil2022 (FT, rechecked)
- trail: H1-05 §critic, §2, §answers

From the note:

> In [3], functional similarity exceeded taxonomic similarity at SEED levels 1 and 2 against all five taxonomic ranks.
>
> The ordering therefore did not reverse at any combination tested.
>
> - **Annotation level.** In [3], functional similarity exceeded taxonomic similarity at SEED levels 1 and 2 against all five taxonomic ranks [FT, rechecked].
>
> Other habitats: the strength of coupling depends on the annotation scheme.**: Soil: one study reports the comparison at several annotation levels [3].
>
> [3] and [37] both find functional variability lower at every annotation level tested, so no reversal of ordering by unit was found in either..
>
> *Single-source sensitivity:* Removing Chen et al. 2022 [3] leaves no soil evidence on annotation level.
>
> - **D2, soil**: Single-study evidence only.
>

## H1-05/chronosequence.4

Between the bioRxiv and ISME J 2026 versions of the restoration study, "profound functional decoupling" was softened to "a decoupling", and the driver taxa were named differently.

- conf: not stated
- class: not stated
- holds: [9]
- src: goodallTaxonomicFilteringAccompanies2026
- trail: H1-05 §4

From the note:

> | Goodall et al. [9] | bioRxiv to ISME J 2026 | "profound functional decoupling" softened to "a decoupling"; driver taxa named differently |
>

## H1-05/functional-unit.3

The authors of the global comparison say coarser levels are more conserved.

- conf: not stated
- class: not stated
- holds: [3]
- src: chenFunctionalRedundancySoil2022
- trail: H1-05 §2

From the note:

> The authors say coarser levels are more conserved.
>

## H1-05/null-model.1

No field-soil study was found that applies a null model (taxon-label shuffling of a gene-content matrix, trait randomization, phylogenetic null) to the difference between functional and taxonomic turnover.

- conf: not stated
- class: search (note: "No field-soil study was found")
- holds: both search agents' Europe PMC boolean queries on soil, metagenome or GeoChip combined with null, shuffle, randomization, NST or betaNTI; the critic finds the absence appropriately worded as a search result
- src: none (a search result)
- trail: H1-05 §3.1, §answers, §critic
- rating: "Weak for soil"

From the note:

> No field-soil study was found that applies a null model to the difference between functional and taxonomic turnover.
>
> Both search agents looked, using Europe PMC boolean queries on soil, metagenome or GeoChip combined with null, shuffle, randomization, NST or betaNTI.
>
> **D3, soil field metagenomes: no null model found testing the functional-taxonomic difference.
>
> Other habitats and in vitro: nulls give system-dependent answers, from 'consistent with averaging' to 'selection on function'.**: Soil, field: the searches found no field-soil study that applies a null model (taxon-label shuffling of a gene-content matrix, trait randomization, phylogenetic null) to the difference between functional and taxonomic turnover.
>
> - **D3, soil**: No field-soil null model testing the functional-taxonomic difference was found by the review's routes.
>
> The D3 soil-absence claim is appropriately worded as a search result.
>
> *Strength:* Weak for soil, where the evidence is absent for field metagenomes and single-study for in vitro soil-derived communities.
>

## H1-05/contrast-size.1

No soil study was found that tests or plots how the functional-taxonomic gap scales with environmental distance; systematic comparisons across a graded range of environmental distances were not measured.

- conf: not stated
- class: search (note: "No soil study was found")
- holds: the review's searches
- src: none (a search result)
- trail: H1-05 §1.4, §answers

From the note:

> No soil study was found that tests how the functional-taxonomic gap scales with environmental distance.
>
> Systematic comparisons across a graded range of environmental distances.
>
> No soil study was found that plots the functional-taxonomic gap against environmental distance.
>

## H1-05/other-habitats.11

In European fish, functional homogenization over time exceeded taxonomic homogenization six-fold.

- conf: not stated
- class: not stated
- holds: European fish assemblages [51]
- src: villegerFunctionalHomogenizationExceeds2014 (AB)
- trail: H1-05 §1.6

From the note:

> Yet functional homogenization over time exceeded taxonomic homogenization six-fold [51] [AB].
>

## H1-06/rankwise-structuring.14

Without Lu et al. 2016 the rank-wise verdict falls to 'measured without controlling group number and size'.

- conf: not stated
- class: not stated
- holds: the sensitivity of the B verdict to one source
- src: luEvaluatingCommunityenvironmentRelationships2016
- trail: H1-06 §answers, §6. Verdicts

From the note:

> Would change if one source were removed: yes.
>
> Without Lu et al. 2016 the verdict falls to 'measured without controlling group number and size'.
>
> Removing Lu et al. 2016 drops the verdict to "measured without controlling group number and size".
>

## H1-06/a1-environmental-preferences.1

No consenTRAIT depth (tau_D) for any environmental optimum (pH, temperature or moisture) was found.

- conf: not stated
- class: search (note: "No consenTRAIT depth for any environmental optimum was found")
- holds: the routes the provenance names: Europe PMC REST keyword, DOI and title search plus fullTextXML; the 'consenTRAIT AND OPEN_ACCESS' query (23 hits screened); citing papers of Lu et al. 2016; PMC HTML; publisher pages; bioRxiv; the Lennon lab PDF archive; WebSearch on several phrasings
- src: none (a search result)
- trail: H1-06 §2. Part A1, §answers, §Provenance

From the note:

> **No consenTRAIT depth for any environmental optimum was found.** The frequently repeated statement that pH optimum, soil moisture optimum and habitat association sit in deep clades appears in Martiny et al. 2013 as a discussion claim resting on other studies.
>
> No consenTRAIT-style depth for any environmental optimum was found.
>
> Routes behind every 'not found': Europe PMC REST keyword, DOI and title search plus fullTextXML; the 'consenTRAIT AND OPEN_ACCESS' query (23 hits screened); citing papers of Lu et al. 2016 screened by title; PMC HTML; publisher pages; bioRxiv; the Lennon lab PDF archive; WebSearch on taxonomic sufficiency, taxonomic resolution with explained variation, ecological coherence with ranks, genome completeness with functional inference, and phylogenetic signal of optimal growth temperature.
>
> Not found by these routes: (1) any consenTRAIT tau_D for pH, temperature or moisture optima; (2) any rank-wise composition-environment study, other than Lu 2016, that controls group number and size (Schmidt 2014 controls them, but for identity thresholds and annotation consistency, not ranks); (3) any direct test of how genome incompleteness biases tau_D or signal statistics.
>
> Signal is significant in 4 of 5 datasets but weak (Pagel's lambda 0.22 to 0.78, Moran's I < 0.25 at all depths), there is no consenTRAIT-style depth, and families span 3.7 to 4.2 pH units.
>

## H1-06/tau-d.1

consenTRAIT's tau_D is the mean 16S rRNA distance from the root of clades in which at least 90% of members share a trait.

- conf: not stated
- class: not stated
- holds: the consenTRAIT method as Martiny et al. 2013 define it; a distance on a tree
- src: martinyPhylogeneticConservatismFunctional2013
- trail: H1-06 §1. What is being compared

From the note:

> Depth of conservation is usually expressed as a distance on a tree: consenTRAIT's tau_D is the mean 16S rRNA distance from the root of clades in which at least 90% of members share a trait [1].
>

## H1-06/perturbation-response.9

In situ growth measured by qSIP in one forest soil had Blomberg's K 0.38 to 0.54 and Pagel's lambda 0.96 to 0.98.

- conf: not stated
- class: not stated
- holds: one forest soil
- src: morrisseyPhylogeneticOrganizationBacterial2016
- trail: H1-06 §2. Part A1

From the note:

> In situ growth measured by qSIP in one forest soil had K 0.38 to 0.54 and lambda 0.96 to 0.98 [22].
>

## H1-06/adjacent-metrics.1

In Antarctic wetlands, pH explained more of betaNTI (phylogenetic turnover, not composition) at ASV level (R2 0.20) than at OTU97 (0.08).

- conf: not stated
- class: not stated
- holds: Antarctic wetlands; unit counts uncontrolled; a metric that measures something other than composition-environment R2
- src: quirogaEcologicalAssemblyBacterial2022
- trail: H1-06 §4. Part B

From the note:

> **Adjacent metrics (not composition-environment R2).** Two metrics give a different picture because they measure something else.
>
> In Antarctic wetlands, pH explained more of betaNTI (phylogenetic turnover, not composition) at ASV level (R2 0.20) than at OTU97 (0.08), with unit counts uncontrolled [26].
>

## H1-06/metabolic-depth.8

Single enzymes are shallow: alkaline phosphatase, chitinase and beta-N-acetylglucosaminidase had tau_D 0.0098, 0.0080 and 0.0097, about 98% 16S identity.

- conf: not stated
- class: not stated
- holds: 3,058 genomes
- src: zimmermanMicrodiversityExtracellularEnzyme2013
- trail: H1-06 §3. Part A2

From the note:

> Single enzymes are shallow.
>
> Alkaline phosphatase, chitinase and beta-N-acetylglucosaminidase had tau_D 0.0098, 0.0080 and 0.0097, about 98% 16S identity, on 3,058 genomes [2].
>

## H1-06/depth-dependence.6

Class Actinobacteria was functionally coherent while the shallower family Enterobacteriaceae was not.

- conf: single (note: "SINGLE SOURCE")
- class: not stated
- holds: Parras-Moltó's gene-content coherence analysis
- src: parrasmoltoAssessmentPhylofunctionalCoherence2021
- trail: H1-06 §3. Part A2

From the note:

> Class Actinobacteria was coherent while the shallower family Enterobacteriaceae was not (SINGLE SOURCE).
>

## H1-06/genome-incompleteness.7

For 116,884 MAGs against RefSeq, raw gene detection rates fell below model-corrected prevalences, and most KEGG orthologs were biased between culture-heavy and MAG references.

- conf: single (critic: C-034)
- class: not stated
- holds: MAGs against RefSeq
- src: albrightTraitBiasesMicrobial2023
- trail: H1-06 §3. Part A2, §critic

From the note:

> For 116,884 MAGs against RefSeq, raw gene detection rates fell below model-corrected prevalences, and most KEGG orthologs were biased between culture-heavy and MAG references [11].
>
> - 'Incompleteness pushes detected function down' (Section 5) is phrased generally. Each quantitative element is SINGLE SOURCE ([9] modules, [10] core genes, [11] reference bias), and none measures the effect on conservation depth, which the review does concede.
>

## H1-06/ab-relation.2

The fall in explained variance at phylum in soils and the class-level incoherence in a time series match the weak within-phylum pH signal and the opposing responses inside coarse groups.

- conf: not stated
- class: reading (note: "reviewer's reading")
- holds: Lu 2016 and Auladell 2022 (natural composition) set beside Ramoneda 2023 and Isobe 2019
- src: luEvaluatingCommunityenvironmentRelationships2016, auladellSeasonalNicheDifferentiation2021, ramonedaBuildingGenomebasedUnderstanding2023, isobePhylogeneticConservationBacterial2019
- trail: H1-06 §4. Part B

From the note:

> **Relation to Part A (reviewer's reading).** The rise in explained variance from otu97 to about otu94 and genus [23, 25] matches where perturbation responses cluster (tau_D about 0.017 to 0.02, about genus) [19, 20].
>
> The fall at phylum in soils [23] and the class-level incoherence in a time series [28] match the weak within-phylum pH signal [13] and the opposing responses inside coarse groups [19].
>

## H1-06/metabolic-depth.4

Sulfate reduction had a tau_D of 0.039 (20 clusters).

- conf: not stated
- class: not stated
- holds: 2,229 SEED genomes, 16S trees; the value rests on search-agent transcription
- src: martinyPhylogeneticConservatismFunctional2013
- trail: H1-06 §3. Part A2, §Provenance, §critic
- limit: access (critic: C-028)

From the note:

> **Ordering by complexity.** On 2,229 SEED genomes (26 phyla, 16S trees), 93% of 89 traits were non-randomly distributed [1].
>
> Sulfate reduction was 0.039 (20 clusters) and nitrogen fixation about 0.018 (54 clusters).
>
> I could not re-open Martiny 2013 (Europe PMC fullTextXML empty) or Goberna and Verdu 2016 (OUP bot challenge), so the specific trait values from Martiny 2013 rest on two independent search-agent readings, and the two agents transcribed its overall tau_D range differently.
>
> - Martiny et al. 2013 [1]: the synthesiser states it could not re-open the paper, yet the A2 ordering values (oxygenic photosynthesis 0.10 to 0.11, sulfate reduction 0.039, N fixation 0.018, Biolog < 0.011) are load-bearing in the A2 verdict and rest on a search agent's transcription that disagrees with another agent on the range. The critic could not obtain it via Europe PMC either (PMC3603392, not OA).
>

## H1-06/ph-preference.5

A phylum-level tendency in pH preference seen in one dataset (acidophilic Acidobacteria in freshwater) did not recur in the others.

- conf: not stated
- class: not stated
- holds: Ramoneda's five datasets
- src: ramonedaBuildingGenomebasedUnderstanding2023
- trail: H1-06 §2. Part A1

From the note:

> A phylum-level tendency seen in one dataset (acidophilic Acidobacteria in freshwater) did not recur.
>

## H1-06/trait-compilations.5

Growth optima predicted from amino-acid composition for 15,596 BacDive organisms reached, under family-level holdout, R2 0.73 for temperature, 0.81 for salinity and 0.48 for pH, with 92% balanced accuracy for oxygen tolerance.

- conf: not stated
- class: model (note: "modelled, preprint")
- holds: BacDive organisms, GTDB r214; family-level holdout
- src: barnumPredictingMicrobialGrowth2024 (modelled, preprint)
- trail: H1-06 §2. Part A1

From the note:

> Barnum et al. 2024 [12] (modelled, preprint) predicted growth optima from amino-acid composition for 15,596 BacDive organisms (GTDB r214).
>
> Under family-level holdout, R2 was 0.73 for temperature, 0.81 for salinity and 0.48 for pH, with 92% balanced accuracy for oxygen tolerance.
>

## H1-06/a1-environmental-preferences.3

The primary studies Martiny et al. 2013 cite for deep-clade environmental preferences were either not obtained (Placella et al. 2012, Philippot et al. 2010) or were read and give a more mixed picture (Lennon et al. 2012).

- conf: not stated
- class: not stated
- holds: the primary studies behind the deep-clade statement
- src: placellaRainfallinducedCarbonDioxide2012 (not obtained), philippotEcologicalCoherenceHigh2010 (not obtained), lennonMappingNicheSpace2012
- trail: H1-06 §2. Part A1

From the note:

> The primary studies it cites were either not obtained (Placella et al. 2012, Philippot et al. 2010) or were read and give a more mixed picture (Lennon et al. 2012; see below).
>

## H1-06/uncontrolled-rank-studies.9

Within at least three genera in the coastal time series, seasonal niche similarity fell with 16S divergence.

- conf: not stated
- class: not stated
- holds: the 11-year coastal time series
- src: auladellSeasonalNicheDifferentiation2021
- trail: H1-06 §4. Part B

From the note:

> In an 11-year coastal time series [28], seasonal niches were coherent for some genera and families, but classes (Alphaproteobacteria, Gammaproteobacteria, Bacteroidia) were non-seasonal when aggregated; within at least three genera, niche similarity fell with 16S divergence.
>

## H1-06/uncontrolled-rank-studies.1

Studies across ranks that do not control group number and size agree in part and conflict in part with the controlled study.

- conf: not stated
- class: not stated
- holds: Mayjonade 2024 (preprint), Bay 2020, Chakraverti-Wuerthwein 2026 (preprint), Auladell 2022
- src: mayjonadeRelativeEffectsAbiotic2024, baySoilBacterialCommunities2020, chakravertiwuerthweinPhylogeneticCoherenceMicrobiome2026, auladellSeasonalNicheDifferentiation2021
- trail: H1-06 §answers

From the note:

> Uncontrolled studies agree in part and conflict in part: habitat R2 peaked at class and physicochemical associations were most frequent at phylum (Mayjonade 2024 preprint, gyrB taxonomy); 97% OTUs explained more composition variance than ASVs (Bay 2020); a pH-aligned composition axis stayed stable across ranks (Chakraverti-Wuerthwein 2026 preprint); seasonal niches were absent at class level (Auladell 2022, time series, not a spatial environment gradient).
>

## H1-06/rankwise-structuring.11

Lu et al. read the rise in explained variance with rank as phylogenetic niche conservatism.

- conf: not stated
- class: not stated
- holds: the authors' interpretation
- src: luEvaluatingCommunityenvironmentRelationships2016
- trail: H1-06 §4. Part B

From the note:

> The authors read the rise as phylogenetic niche conservatism.
>

## H1-06/rankwise-structuring.3

In soils, R2 rose by at least 50% from otu97 to otu94.

- conf: not stated
- class: not stated
- holds: four surface soils
- src: luEvaluatingCommunityenvironmentRelationships2016
- trail: H1-06 §4. Part B, §critic
- limit: access (critic: C-026)

From the note:

> - Soils: R2 rose up to class (otu82 to otu76) and fell at phylum, with at least a 50% R2 increase from otu97 to otu94. pH was the strongest single variable.
>
> - Lu et al. 2016 [23]: the synthesiser presents the null model ('shuffled linkages ... remaining topology', 100 random linkage maps), the soil class peak, the '>= 50% R2 increase otu97 to otu94' and the per-dataset seawater shapes as verified.
>
> The critic could only confirm the abstract (nature.com paywalled; PMC5148199 flagged not open access).
>

## H1-06/depth-dependence.1

In 2,730 marine genomes, chitinase tau_D was 0.0281 on a 16S tree and 0.0444 on a core-gene tree, three to five times Zimmerman's 0.008.

- conf: not stated
- class: not stated
- holds: marine genomes (Sun 2021) against Zimmerman's 3,058 genomes
- src: sunPhylogeneticDistributionPolysaccharideDegrading2021, zimmermanMicrodiversityExtracellularEnzyme2013
- trail: H1-06 §3. Part A2, §answers

From the note:

> **Dataset and tree dependence.** In 2,730 marine genomes, chitinase tau_D was 0.0281 on a 16S tree and 0.0444 on a core-gene tree [4], three to five times Zimmerman's 0.008 [2].
>
> Absolute depths for the same trait differ between datasets and trees: chitinase 0.008 (Zimmerman 2013) against 0.028 on a 16S tree and 0.044 on a core-gene tree (Sun 2021).
>

## H1-RES/capacity-expression.9

Zhao et al. (2024), across ocean, soil and human gut enzymes, found decoupling between predicted secreted enzyme genes and detected transcripts and proteins, driven by substrate availability and environmental filtering.

- conf: not stated
- class: not stated
- holds: ocean, soil and human gut
- src: zhao2024
- trail: H1-RES §Other key multi-omics

From the note:

> | Zhao et al. 2024 | Metagenomes + metatranscriptomes + metaproteomes (ocean, soil, human gut enzymes) | Cross-ecosystem multi-omics showed decoupling between predicted secreted enzyme genes and detected transcripts/proteins, driven by substrate availability and environmental filtering [6]. |
>

## H1-RES/redundancy.11

Tripathi et al. (2017): distinct taxonomic and functional communities were observed across precipitation zones in Israel, with lower functional diversity in arid environments, showing coordinated taxonomic and functional shifts with climate.

- conf: not stated
- class: not stated
- holds: a precipitation gradient in Israel
- src: tripathiTrendsTaxonomicFunctional2017
- trail: H1-RES §Soil counter-evidence

From the note:

> |  Trends in taxonomic and functional composition of soil microbiome along a precipitation gradient in Israel, Binu M.
>
> Tripathi et al., 2017  | Distinct taxonomic and functional communities were observed across precipitation zones; functional diversity was lower in arid environments, demonstrating coordinated taxonomic and functional shifts with climate [9].  |
>

## H1-RES/taxonomy-function.1

Pangenome structure is strongly taxon-dependent, which bears on treating functional capacity as a stable cross-environment unit.

- conf: not stated
- class: not stated
- holds: the Sub-claim 1 taxa
- src: none (the reviewer's synthesis)
- trail: H1-RES §Taxon-Dependence

From the note:

> The counter-evidence reveals that pangenome structure is strongly taxon-dependent, with important implications for treating functional capacity as a stable cross-environment unit.
>

## H1-RES/redundancy.3

Bao et al. (2020): although taxonomic composition of straw-degrading bacteria was highly variable across sites, their metabolic (functional) composition was conserved across experimental sites.

- conf: not stated
- class: not stated
- holds: straw-degrading bacteria at the experimental sites
- src: baoFunctionalCommunityComposition2020
- trail: H1-RES §Soil redundancy evidence

From the note:

> |  Functional community composition has less environmental variability than taxonomic composition in straw-degrading bacteria, Yuanyuan Bao et al., 2020  | Although taxonomic composition was highly variable across sites, metabolic (functional) composition of straw-degrading bacteria was conserved across experimental sites, indicating lower functional variability than taxonomic variability [3].  |
>
> Chen et al. (2022) found taxonomies more distinct than functional potentials across 17 climate zones [1]; Bao et al. (2020) found metabolic composition of straw-degraders conserved across sites where taxonomy was highly variable [3]; and the strongest single statistic, Chen et al. (2021), reported a ~72% loss of taxonomic richness with only limited change in functional-category abundances [6].
>

## H1-RES/accessory-function.26

The sub-claim that accessory genomes encode niche-adaptive functions is supported but requires qualification: accessory genomes do carry habitat-linked metabolic and stress-response genes, particularly in contaminated and extreme environments where selection is strong, but a substantial fraction of accessory content is mobile genetic elements, hypothetical proteins and poorly characterised genes without obvious metabolic functions; functional accessory genes must be distinguished from mobile element noise, and the strength of the accessory-niche link depends on environmental context, selective pressure and the mobile element classes involved.

- conf: not stated
- class: not stated
- holds: the Sub-claim 2 studies
- src: none (the reviewer's synthesis)
- trail: H1-RES §Assessment: Context
- rating: "supported but requires qualification"

From the note:

> The sub-claim that accessory genomes encode niche-adaptive functions is supported but requires qualification.
>
> Accessory genomes do carry habitat-linked metabolic and stress-response genes, particularly in contaminated and extreme environments where selection is strong.
>
> However, a substantial fraction of accessory content consists of mobile genetic elements, hypothetical proteins, and poorly characterized genes that do not provide obvious metabolic functions.
>
> Researchers must distinguish functional accessory genes from mobile element noise, and the strength of the accessory-niche link depends on environmental context, selective pressure, and the specific mobile element classes involved.
>

## H1-RES/pangenome.24

The proportion of species-level accessory genes per genome varies from 0% in *Chlamydia* to 30–33% in *Alphaproteobacteria*, *Gammaproteobacteria* and *Clostridia*.

- conf: not stated
- class: not stated
- holds: the taxa named
- src: none (cited only as SC1 [49]; the note gives no reference list)
- trail: H1-RES §Counter-Evidence: Taxa

From the note:

> The proportion of species-level accessory genes per genome varies from 0% in *Chlamydia* to 30–33% in *Alphaproteobacteria*, *Gammaproteobacteria*, and *Clostridia* [49].
>

## H1-RES/pangenome.11

The nitrogen-fixing *Rhizobiales* pangenome (12 symbionts) contained 37,364 total loci with only 700 core genes, representing 10.2% of single genomes.

- conf: not stated
- class: not stated
- holds: 12 *Rhizobiales* symbionts
- src: none (cited only as SC1 [7]; the note gives no reference list)
- trail: H1-RES §Confirming Evidence Across

From the note:

> The nitrogen-fixing *Rhizobiales* pangenome (12 symbionts) contained 37,364 total loci with only 700 core genes, representing 10.2% of single genomes [7].
>

## H1-RES/n-cycle-hgt.8

Garbeva et al. (2007) detected nirK and norB in *Nitrosospira* species, with phylogenetic analysis suggesting lateral transfer of these denitrification genes into ammonia-oxidising bacteria; in some strains they were not phylogenetically distinct from classical denitrifiers and appeared less conserved than 16S rRNA or amoA genes.

- conf: not stated
- class: not stated
- holds: *Nitrosospira* species
- src: garbeva2007
- trail: H1-RES §Multi-Level HGT

From the note:

> Garbeva et al. (2007) detected nirK and norB in *Nitrosospira* species, with phylogenetic analysis suggesting lateral transfer of these denitrification genes into ammonia-oxidizing bacteria [7].
>
> The nirK and norB sequences from some *Nitrosospira* strains were not phylogenetically distinct from classical denitrifiers, and these genes appeared less conserved than 16S rRNA or amoA genes [7].
>

## H1-RES/n-cycle-hgt.13

Anand & Chanway (2013), in *Paenibacillus polymyxa* strain P2b-2R, found phylogenetic analyses suggesting nifH was transmitted horizontally and nifD vertically, a gene-specific pattern within the same operon.

- conf: not stated
- class: not stated
- holds: one strain
- src: anand2013
- trail: H1-RES §Counter-Evidence: Vertical

From the note:

> Anand & Chanway (2013) analyzed *Paenibacillus polymyxa* strain P2b-2R and found that phylogenetic analyses suggested nifH was transmitted horizontally while nifD was transmitted vertically, indicating gene-specific evolutionary patterns within the same operon [20].
>

## H1-RES/pangenome.19

The MTBC accessory genome is a product of genome reduction, showing lineage-specific and independent deletions rather than gene acquisition; the closed structure reflects MTBC's clonal evolution, absence of horizontal gene transfer and limited accessory genome.

- conf: not stated
- class: not stated
- holds: MTBC
- src: none (cited only as SC1 [12], [13], [17], [27], [39], [48], [57] and [45]; the note gives no reference list)
- trail: H1-RES §Counter-Evidence: Taxa

From the note:

> The MTBC accessory genome is a product of genome reduction showing lineage-specific and independent deletions rather than gene acquisition [12] [13] [17] [27] [39] [48] [57].
>
> This closed pangenome structure reflects MTBC's clonal evolution, absence of horizontal gene transfer, and limited accessory genome [45].
>

## H1-RES/pangenome.8

Fungal pathogens also exhibit substantial accessory genomes.

- conf: not stated
- class: not stated
- holds: stated without a citation or a fungal example
- src: none (the note cites nothing for it)
- trail: H1-RES §Confirming Evidence Across

From the note:

> Beyond bacteria, fungal pathogens also exhibit substantial accessory genomes.
>

## H1-RES/capacity-expression.10

Wang et al. (2024), pairing gene- and protein-level redundancy measures in the gut, found selective expression of proteins that cannot be inferred from genomic presence alone, distinguishing ecological niche proteins from metabolic essentials.

- conf: not stated
- class: not stated
- holds: gut
- src: wang2024
- trail: H1-RES §Other key multi-omics

From the note:

> | Wang et al. 2024 | Metagenomics + metaproteomics (gut) | Pairing gene- and protein-level redundancy measures showed selective expression of proteins that cannot be inferred from genomic presence alone, distinguishing ecological niche proteins from metabolic essentials [7]. |
>

## H1-RES/redundancy.16

The counter-evidence bounds soil redundancy rather than overturning it: function and taxonomy are reported to covary closely where environments differ most strongly (across biomes, precipitation extremes and contamination gradients), so redundancy is real within moderate environmental ranges but appears to weaken as environmental contrast grows, with selection then shaping taxa and functions together.

- conf: not stated
- class: reading (note: "Synthesis written from the eleven studies tabulated above")
- holds: the eleven soil studies; the synthesis was written manually, not by the research round
- src: fiererCrossbiomeMetagenomicAnalyses2012, tripathiTrendsTaxonomicFunctional2017, renComparisonMicrobialTaxonomic2016
- trail: H1-RES §Assessment: redundancy

From the note:

> *(Synthesis written from the eleven studies tabulated above; the round did not reach this synthesis itself.)*
>
> The counter-evidence does not overturn this but bounds it, and the bound matters for this project specifically.
>
> Function and taxonomy are reported to covary closely precisely where environments differ most strongly: across whole biomes (Fierer et al., 2012 [8]), across precipitation extremes (Tripathi et al., 2017 [9]), and along contamination gradients (Ren et al., 2016 [11]).
>
> In other words, redundancy is real within moderate environmental ranges but appears to weaken as the environmental contrast grows, with selection then shaping taxa and functions together.
>

## H1-RES/capacity-expression.4

Metagenomic presence alone can overestimate which functions are actively expressed in situ.

- conf: not stated
- class: not stated
- holds: human gut, from the DNA–RNA mismatches in Franzosa et al.
- src: franzosaRelatingMetatranscriptomeMetagenome2014
- trail: H1-RES §Representative study example

From the note:

> - **Implication** These quantitative DNA–RNA mismatches demonstrate that using metagenomic presence alone can overestimate which functions are actively expressed in situ [1].
>

## H1-RES/accessory-function.20

In *Arthrobacter* strains from varying depths of a sediment core, the pangenome had a notably open and volatile accessory genome.

- conf: not stated
- class: not stated
- holds: one sediment core
- src: none (cited only as SC2 [21]; the note gives no reference list)
- trail: H1-RES §Counter-Evidence: Accessory

From the note:

> In *Arthrobacter* strains from varying depths of a sediment core, the pangenome revealed a notably open and volatile accessory genome [21].
>

## H1-RES/capacity-expression.1

Franzosa et al. (2014), comparing metagenomes and metatranscriptomes of the human gut, is a widely cited demonstration that genomic potential can overstate realised function, with explicit quantitative evidence for mismatch between DNA-level gene abundance and RNA-level expression.

- conf: not stated
- class: not stated
- holds: human gut
- src: franzosaRelatingMetatranscriptomeMetagenome2014
- trail: H1-RES §Representative study example

From the note:

> This section highlights a widely cited empirical demonstration that genomic potential can overstate realised function by comparing metagenomes to metatranscriptomes in the human gut.
>
> The study provides explicit quantitative evidence for widespread mismatch between DNA-level gene abundance and RNA-level expression.
>
> - **Paper** Relating the metatranscriptome and metagenome of the human gut, Eric A.
>
> Franzosa et al., 2014, [1].
>

## H1-RES/pangenome.2

Mathematical extrapolation indicated that the gene reservoir available to the *S. agalactiae* pangenome is vast, with unique genes continuing to be identified even after sequencing hundreds of genomes, defining an open pangenome; this demonstration provided the conceptual framework for subsequent pangenome research.

- conf: not stated
- class: model (note: "Mathematical extrapolation")
- holds: *S. agalactiae*, extrapolated from the sequenced strains
- src: tettelin2005
- trail: H1-RES §Sub-claim 1

From the note:

> Mathematical extrapolation indicated that the gene reservoir available for inclusion in the *S. agalactiae* pangenome is vast, with unique genes continuing to be identified even after sequencing hundreds of genomes, defining an open pangenome [2].
>
> This quantitative demonstration of substantial accessory fractions and ongoing gene discovery provided the conceptual framework for subsequent pangenome research.
>

## H2-01/levels-across.9

In the global ocean, environment strongly shaped functional-group distribution and weakly shaped taxonomy within groups, "roughly independent axes of variation".

- conf: not stated
- class: deriv (marker)
- holds: global ocean; functional groups assigned from taxonomy; removing it would leave the decoupled side resting on Nelson2016 alone
- src: loucaDecouplingFunctionTaxonomy2016 (AB; derived, because functional groups were assigned from taxonomy)
- trail: H2-01 §4.2, §answers

From the note:

> - Decoupled: in the global ocean, environment strongly shaped functional-group distribution and weakly shaped taxonomy within groups, "roughly independent axes of variation" [Louca2016a; AB; derived, because functional groups were assigned from taxonomy].
>
> Decoupling: in the ocean, environment shapes functional-group distribution while taxonomy within groups varies independently [Louca2016a, abstract, derived from taxonomy]; soil N-pathway frequencies follow habitat and soil chemistry while taxonomy within N groups is poorly predicted [Nelson2016].
>
> *Single-source sensitivity:* Removing Louca2016a (abstract only, derived) would leave the decoupled side resting on Nelson2016 alone.
>
> The decoupled side rests on Louca2016a (abstract only, taxonomy-derived function) and Nelson2016, which was read only through an automated summary with figures not re-verified.
>

## H2-01/trait-dimension.4

Mouillot2021 is the only source found that measures how a dimension estimate depends on the number of features, feature correlation and sample count, and it concerns species-level traits, not sample-level profiles.

- conf: single (note: "This is the only source found that measures how a dimension estimate depends on the number of features")
- class: search (note: "This is the only source found")
- holds: species-by-trait matrices; the empirical dependence of rank on p/n rests on it alone; full text per angle, not re-checked by the reviewer (the critic)
- src: mouillotDimensionalityStructureSpecies2021 (FT)
- trail: H2-01 §2.4, §answers, §critic

From the note:

> This is the only source found that measures how a dimension estimate depends on the number of features, feature correlation and sample count.
>
> It concerns species-level traits, not sample-level profiles.
>
> The dependence on feature number and sample count rests on one species-trait study from another setting..
>
> Removing Mouillot2021 leaves no measured dependence of dimension on feature count or sample count.
>
> The only source measuring how dimension estimates depend on feature number, feature correlation and sample count is from species trait databases.
>
> The dependence on feature count and sample count is measured only for species-by-trait matrices (Mouillot2021, read by a search agent and not re-opened by the reviewer).
>
> - D1 access_basis says 'Mostly full text', but the synthesis re-opened only Chen2020 and Manor2017. Piton2023 (the only variance-explained figure), Mouillot2021 (the only measured dependence of dimension on feature and sample count), Nayfach2015, HMP2012 and Tian2020 are full text 'per angle' and were not re-checked, even though they are named as single points of failure.
>
> The empirical dependence of rank on p/n is left to Mouillot2021 alone.; setting_or_class: Microbiome compositional PCA and NMF rank selection; sample-size subsampling; direction: D1
>

## H2-01/other-field-transfer.5

Individual co-expression networks predicted GO membership with mean AUROC 0.60 (bulk) and 0.56 (single cell); aggregating 163 networks reached 0.73 (bulk); sample size did not predict performance.

- conf: single (critic: H2-01:C-015)
- class: meas (marker)
- holds: co-expression replicability (other field)
- src: crowExploitingSinglecellExpression2016 (FT; measured)
- trail: H2-01 §3.4, §critic

From the note:

> - **Replicability of co-expression.** Individual co-expression networks predicted GO membership with mean AUROC 0.60 (bulk) and 0.56 (single cell); aggregating 163 networks reached 0.73 (bulk). Sample size did not predict performance [Crow2016; FT; measured].
>
> Individual co-expression networks replicate modestly [Crow2016].
>
> Other fields show partial transfer, each result from a single study.
>

## H2-01/processing-dimension.1

No microbial study was found that re-estimated the dimension of functional profiles under different normalisations, sparsity filters, presence/absence against abundance, overlapping against non-overlapping gene sets, or sample sizes, and none uses a formal rank-selection rule (parallel analysis, cross-validated PCA or NMF, a random-matrix threshold) with stated n and p while testing processing.

- conf: not stated
- class: search (note: "No microbial study re-estimated dimension under different normalisation, sparsity filters, presence/absence against abundance, or sample size")
- holds: three search angles via Europe PMC REST, NCBI E-utilities, Crossref, Unpaywall, OpenAlex, Semantic Scholar, WebFetch of PMC pages and repository PDFs; WebSearch and Scholar Gateway unavailable
- src: none (a search result)
- trail: H2-01 §answers, §2.3, §Provenance

From the note:

> No microbial study re-estimated dimension under different normalisation, sparsity filters, presence/absence against abundance, or sample size.
>
> *Not measured:* No microbial estimate with a formal rank rule and stated n and p tested against normalisation, sparsity filtering, presence/absence against abundance, overlapping against non-overlapping gene sets, or subsampled sample size.
>
> None tests sensitivity to normalisation, sparsity, presence against abundance, or sample size.
>
> None uses a formal rank-selection rule (parallel analysis, cross-validated PCA or NMF, a random-matrix threshold) with stated n and p *and* tests how the estimate changes with processing.
>
> No study was found that re-estimated the dimension of functional profiles under different normalisations, sparsity filters, presence/absence against abundance, or sample sizes.
>
> All three had WebSearch unavailable (budget exhausted), and Scholar Gateway failed with an identity error.
>
> Routes used across angles: Europe PMC REST (until HTTP 503), NCBI E-utilities (PubMed esearch/efetch, PMC efetch full text), Crossref, Unpaywall, OpenAlex (until daily budget exhausted), Semantic Scholar (one query, then HTTP 429), WebFetch of PMC pages, and repository PDFs (UAB, Archimer, eScholarship, MTAK).
>
> Not found by these routes: any microbial test withholding a habitat when scoring functional covariation; any microbial cross-habitat comparison of covariation stability against level and composition stability; any microbial study of how dimension estimates change with normalisation, sparsity, presence/absence, overlapping gene sets or sample size; any study holding taxonomy fixed while habitat varies.
>
> No microbial study tested sensitivity to normalisation, sparsity, presence/absence against abundance, overlapping gene sets or sample size.
>

## H2-01/functional-profile.2

Trait ecology supplies community-weighted means (CWMs) and species-by-trait matrices, mostly from plants.

- conf: not stated
- class: not stated
- holds: the review's account of the three bodies of work that bear on the brief
- src: none (the reviewer's account of the literature)
- trail: H2-01 §1. What

From the note:

> Three bodies of work bear on the brief.
>
> Trait ecology supplies community-weighted means (CWMs) and species-by-trait matrices, mostly from plants.
>

## H2-01/covariation-stability.10

Community genomic traits covaried, some possibly for technical reasons.

- conf: not stated
- class: not stated
- holds: microbial metagenomes, pooled
- src: barberanExplorationCommunityTraits2011 (AB)
- trail: H2-01 §4.4

From the note:

> **Microbial, pooled only.** Covariation among functions has otherwise been fitted on pooled cross-habitat data, not compared between habitats: N-pathway frequencies "overwhelmingly positively correlated" across 365 soils from 10 habitat types [Nelson2016]; co-abundance and co-expression of ocean OGs predicting shared KEGG membership [Salazar2019; fitted and scored on the same samples; partly circular]; covariation of amino-acid transport and cofactor synthesis in GOS [Gianoulis2009; AB]; covariation among community genomic traits, some possibly technical in origin [Barberan2012; AB].
>

## H2-01/direct-dimension.8

Piton2023's authors warn that community-aggregated covariation does not show within-organism trade-offs.

- conf: not stated
- class: not stated
- holds: community-aggregated functional tables of 128 soils
- src: pitonLifeHistoryStrategies2023 (FT)
- trail: H2-01 §2.1

From the note:

> They also warn that community-aggregated covariation does not show within-organism trade-offs, and that only 5 to 15% of reads were annotated, with annotation coverage falling as genome size rose.
>

## H2-01/covariation-stability.12

Community-weighted plant traits across 1.1 million plots showed the same two covariation axes as species-level traits, "unexpected" per the authors, while climate and soil explained only 10.8 to 14.0% of CWM variation.

- conf: single (marker)
- class: meas (marker)
- holds: plant communities worldwide; removing it removes the only large-scale case of covariation more stable than levels
- src: bruelheideGlobalTraitenvironmentRelationships2018 (FT; measured; SINGLE SOURCE)
- trail: H2-01 §4.4, §answers

From the note:

> - Covariation more stable than levels: community-weighted plant traits across 1.1 million plots showed the same two covariation axes as species-level traits, "unexpected" per the authors, while climate and soil explained only 10.8 to 14.0% of CWM variation [Bruelheide2018; FT; measured; SINGLE SOURCE].
>
> In plant traits the evidence runs both ways: CWM covariation axes matched species-level axes worldwide while CWM levels varied under similar environments [Bruelheide2018]; trait networks and bivariate slopes changed with climate [FloresMoreno2019; Wright2005]; and along an aridity gradient a trait covariance changed more systematically than level-type diversity [DwyerLaughlin2017].
>
> Removing Bruelheide2018 removes the only large-scale case of covariation more stable than levels..
>
> Lenz2016 (higher dimension) and Bruelheide2018 (covariation stable) are flagged.
>

## H2-01/levels-within.12

In a coastal Mediterranean time series, the taxonomy-function link was strong when function was measured from all reads or all predicted genes and weaker with annotated orthologues or taxonomy-inferred functions; the authors conclude that this challenges functional redundancy, and the abstract is explicit that using all reads, not annotated genes, was essential.

- conf: not stated
- class: not stated
- holds: one coastal Mediterranean time series
- src: galandStrongLinkMarine2018 (AB for me; the reported R² values came from an automated summary and are not used)
- trail: H2-01 §4.1, §Provenance
- limit: access (note: "it stays abstract only and its R2 values are not used")

From the note:

> Galand et al. (2018), in a coastal Mediterranean time series, report a strong taxonomy-function link when function is measured from all reads or all predicted genes, weaker links with annotated orthologues or taxonomy-inferred functions, and conclude that this challenges functional redundancy [Galand2018; AB for me; the reported R² values came from an automated summary and are not used].
>
> The abstract is explicit that using all reads, not annotated genes, was essential.
>
> In a coastal time series, taxonomy and function were strongly linked when function was measured from all reads rather than annotated orthologues [Galand2018, abstract].
>
> Attempts to reach Galand2018 full text (PMC6155072 via E-utilities returned front matter only; Europe PMC fullTextXML returned an empty record) failed, so it stays abstract only and its R2 values are not used.
>

## H2-01/shared-mean.6

No microbial study was found that reports a dimension estimate both before and after centring on the mean profile.

- conf: not stated
- class: search (note: "No microbial study found reports both")
- holds: the routes in the search record
- src: none (a search result)
- trail: H2-01 §2.2

From the note:

> Whether a dimension estimate is taken before or after centring on this mean will change it.
>
> No microbial study found reports both.
>

## H2-01/trait-dimension.9

Covariation in imputed trait matrices is partly built in.

- conf: not stated
- class: reading (note: "so covariation in imputed matrices is partly built in (reviewer's reading)")
- holds: gap-filled plant trait matrices
- src: none (the reviewer's reading)
- trail: H2-01 §2.4

From the note:

> The gap-filling (BHPMF) imputes from trait-trait correlations [Schrodt2015; AB], so covariation in imputed matrices is partly built in (reviewer's reading).
>

## H2-01/expression-dimension.4

PCA of expression compendia depended on the fraction of samples carrying a signal.

- conf: single (marker)
- class: meas (marker)
- holds: heterogeneous expression compendia
- src: lenzPrincipalComponentsAnalysis2016 (FT; measured; SINGLE SOURCE)
- trail: H2-01 §2.4

From the note:

> PCA depended on the fraction of samples carrying a signal [Lenz2016; FT; measured; SINGLE SOURCE].
>

## H2-01/temporal-covariation.2

No trait-ecology study of temporal CWM covariation was found, and the statement names no routes.

- conf: not stated
- class: search (note: "No trait-ecology study of temporal CWM covariation was found")
- holds: no routes named (the critic)
- src: none (a search result)
- trail: H2-01 §4.5, §critic

From the note:

> No trait-ecology study of temporal CWM covariation was found.
>
> - gap: Temporal stability of functional covariation beyond one IBD cohort. Microbial time series with metagenomes or metatranscriptomes and plant CWM time series were not searched, and 'No trait-ecology study of temporal CWM covariation was found' names no routes.; setting_or_class: Longitudinal metagenome and metatranscriptome series (human gut longitudinal cohorts, marine time-series stations); repeated-survey CWM data; direction: D3
>

## H2-01/dimension-estimate.2

Each direct microbial estimate (Jiang2012, Piton2023, Flinkstrom2024) is a single study, and all are fitted and scored on the same samples.

- conf: single (critic: H2-01:C-009)
- class: not stated
- holds: microbial sample-by-function matrices
- src: jiangFunctionalBiogeographyOcean2012 (FT), pitonLifeHistoryStrategies2023 (FT), flinkstromMetagenomicClusteringLinks2024 (FT)
- trail: H2-01 §critic, §answers

From the note:

> Each direct estimate is a single study, and all are fitted and scored on the same samples.
>
> All three direct microbial estimates (Jiang2012, Piton2023, Flinkstrom2024) are single studies fitted and scored on the same samples.
>

## H2-01/gene-set-aggregation.8

In transcriptomics, pathways sharing genes shift each other's significance ("crosstalk").

- conf: not stated
- class: not stated
- holds: pathway analysis of expression data (other field)
- src: donatoAnalysisCorrectionCrosstalk2013 (AB; other field)
- trail: H2-01 §2.3

From the note:

> In transcriptomics, pathways sharing genes shift each other's significance ("crosstalk") [Donato2013; AB; other field].
>

## H2-01/levels-within.4

On a macroalgal host, similarity was about 15% in species composition against 70% in COG composition; the contrast compares a species table with a coarser COG table, and the taxonomic figure is from an earlier study.

- conf: not stated
- class: meas (marker)
- holds: one macroalgal host
- src: burkeBacterialCommunityAssembly2011 (FT; measured)
- trail: H2-01 §4.1

From the note:

> - A macroalgal host: about 15% similarity in species composition against 70% in COG composition [Burke2011; FT; measured].
>
> The contrast compares a species table with a coarser COG table, and the taxonomic figure is from an earlier study.
>

## H2-01/transfer-dependencies.2

That transfer depends on similarity between training and target, breadth of training, and how much of the target is shared mean structure is the reviewer's synthesis across incommensurable tests; it pools covariance or dictionary transfer (Cleary2017, Pierson2015), taxon-to-gene mapping accuracy (Langille2013 NSTI), per-sample accuracy metrics (Sun2020) and phylogenetic gene gain/loss prediction (KonnoIwasaki2023); breadth rests on Taroni2019 alone (qualitative), and each dependency rests on one to three sources measuring different quantities.

- conf: not stated
- class: reading (critic: H2-01:C-018)
- holds: other-field and neighbouring microbial tests; none of these dependencies has been measured for microbial function-function covariation across habitats
- src: clearyEfficientGenerationTranscriptomic2017 (FT), piersonSharingSpecificityCoexpression2015 (FT), langillePredictiveFunctionalProfiling2013 (FT), sunInferenceBasedAccuracyMetagenome2020 (FT), konnoMachineLearningEnables2023 (FT), taroniMultiPLIERTransferLearning2019 (FT), lenzPrincipalComponentsAnalysis2016 (FT)
- trail: H2-01 §3.5, §critic, §answers

From the note:

> Across fields, transfer appears to depend on similarity between training and target, breadth of training, and how much of the target is shared mean structure; each dependency rests on one to three sources.
>
> Reproduction is high in some tests (Subramanian 81%; Chen reductive TCA 94.7%) and low in others (Cleary cross-type drop; pooled networks in Pierson; sign reversals across scales in plant traits [Anderegg2018]); the differences track how different the target is from the training data..
>
> Other fields show partial transfer that falls with dissimilarity between training and target (87% to 68% across tumour types; 81% of genes across studies; pooled networks poor for individual tissues).
>
> Across the other-field and neighbouring evidence, three dependencies recur, each from few sources: similarity of the training set to the target (Cleary2017 related tumour types; Pierson2015 related tissues; Langille2013 NSTI; KonnoIwasaki2023 phylum differences); breadth of the training set (Taroni2019); and the fraction of the target that is shared mean structure versus target-specific signal (Lenz2016; Sun2020).
>
> None of these has been measured for microbial function-function covariation across habitats.
>
> The body does not support the cross-field sentence 'transfer appears to depend on similarity between training and target, breadth of training, and shared mean structure' as a finding.
>
> It pools different quantities: covariance or dictionary transfer (Cleary2017, Pierson2015), taxon-to-gene mapping accuracy (Langille2013 NSTI), and phylogenetic gene gain/loss prediction (KonnoIwasaki2023).
>
> It should be labelled the reviewer's synthesis across incommensurable tests.
>
> (3) D2's cross-field dependency statement pools incommensurable transfer tests.
>
> - D2 answer: 'Across fields, transfer appears to depend on similarity between training and target, breadth of training, and how much of the target is shared mean structure'. Breadth rests on Taroni2019 alone (qualitative), and each dependency rests on one to three sources measuring different quantities.
>
> - D2 answer and Section 3.5 fold four different quantities into one set of transfer dependencies: covariance and dictionary transfer across tumour types or tissues (Cleary2017, Pierson2015), taxon-to-gene mapping accuracy against reference distance (Langille2013), per-sample accuracy metrics (Sun2020), and phylogenetic gene gain/loss prediction (KonnoIwasaki2023).
>

## H2-01/taxonomy-fixed.2

Salazar2019 separate regulatory change (metatranscriptome) from community turnover in the ocean, and per the search agent's reading turnover dominated at global scale; this concerns expression, not gene content.

- conf: not stated
- class: not stated
- holds: global ocean, metatranscriptomes
- src: salazarGeneExpressionChanges2019 (FT)
- trail: H2-01 §4.3

From the note:

> Salazar et al. (2019) separate regulatory change (metatranscriptome) from community turnover in the ocean; per the search agent's reading, turnover dominated at global scale.
>
> That is the nearest item and concerns expression, not gene content.
>

## H2-01/transfer-dependencies.1

There is no direct conflict on the same quantity: reproduction is high in some tests (Subramanian 81%; Chen reductive TCA 94.7%) and low in others (Cleary cross-type drop; pooled networks in Pierson; sign reversals across scales in plant traits).

- conf: not stated
- class: not stated
- holds: tests of different quantities in different fields
- src: subramanianNextGenerationConnectivity2017 (FT), chenGutMicrobialCoabundance2020 (FT), clearyEfficientGenerationTranscriptomic2017 (FT), piersonSharingSpecificityCoexpression2015 (FT), andereggWithinspeciesPatternsChallenge2018 (AB)
- trail: H2-01 §answers

From the note:

> *Conflicts:* No direct conflict on the same quantity.
>
> Reproduction is high in some tests (Subramanian 81%; Chen reductive TCA 94.7%) and low in others (Cleary cross-type drop; pooled networks in Pierson; sign reversals across scales in plant traits [Anderegg2018]); the differences track how different the target is from the training data..
>

## H2-01/other-field-transfer.1

Sparse module dictionaries learned on 5% of samples recovered expression of the same TCGA tumour type at about 87% (Spearman, SMAF), and a dictionary from a different tumour type gave 68% on average, related tumour types doing better; this is recovery of expression from 25 random composite measurements through a learned dictionary (compressed sensing), not a direct covariance-reproduction score.

- conf: single (marker)
- class: meas (marker)
- holds: TCGA tumour types (other field); simulated random composite measurements, m = 25, g = 5,000; the only other-field test found that withholds a biologically distinct group (the closest analogue of a habitat)
- src: clearyEfficientGenerationTranscriptomic2017 (FT; measured; SINGLE SOURCE)
- trail: H2-01 §3.4, §critic, §answers

From the note:

> - **Withheld tissue type (the closest analogue of a withheld habitat).** Sparse module dictionaries learned on 5% of samples recovered held-out profiles of the same TCGA tumour type at about 87% (Spearman, SMAF).
>
> A dictionary from a different tumour type gave 68% on average, and related tumour types did better [Cleary2017; FT; measured; SINGLE SOURCE].
>
> Module dictionaries went from about 87% recovery within a tumour type to 68% across types, better for related types [Cleary2017].
>
> Removing Cleary2017 leaves no other-field test that withholds a biologically distinct group (the closest analogue of a habitat)..
>
> Cleary2017's 87% to 68% is recovery of expression from 25 random composite measurements through a learned dictionary (compressed sensing).
>
> It is not a direct covariance-reproduction score, and the answer should say so.
>
> - Cleary2017: the 87% to 68% figures are correct, but the review describes them as dictionaries that 'recovered held-out profiles'.
>
> They are Spearman recovery from 25 simulated random composite measurements through the dictionary (compressed sensing, m = 25, g = 5,000).
>
> The answer states the transfer more directly than the full text supports.
>

## H2-01/covariation-stability.15

Along an aridity gradient, a height-seed mass covariance strengthened while level-type functional diversity was poorly explained by aridity.

- conf: single (marker)
- class: not stated
- holds: one aridity gradient
- src: dwyerConstraintsTraitCombinations2017 (AB; SINGLE SOURCE)
- trail: H2-01 §4.4

From the note:

> - Covariation changes with conditions: precision-matrix trait networks differed among climate regions in density and modularity, with some edges present everywhere and others region-specific [FloresMoreno2019; FT; heavy imputation]; leaf-economic slopes shifted with climate [Wright2005; AB]; along an aridity gradient, a height-seed mass covariance strengthened while level-type functional diversity was poorly explained by aridity [DwyerLaughlin2017; AB; SINGLE SOURCE].
>
> In plant traits the evidence runs both ways: CWM covariation axes matched species-level axes worldwide while CWM levels varied under similar environments [Bruelheide2018]; trait networks and bivariate slopes changed with climate [FloresMoreno2019; Wright2005]; and along an aridity gradient a trait covariance changed more systematically than level-type diversity [DwyerLaughlin2017].
>

## H2-01/trait-dimension.8

The BHPMF gap-filling imputes from trait-trait correlations.

- conf: not stated
- class: not stated
- holds: plant trait gap-filling
- src: schrodtScpBHPMFScp2015 (AB)
- trail: H2-01 §2.4

From the note:

> The gap-filling (BHPMF) imputes from trait-trait correlations [Schrodt2015; AB], so covariation in imputed matrices is partly built in (reviewer's reading).
>

## H2-01/gene-set-aggregation.9

None of the processing studies measures a covariance matrix between overlapping gene sets.

- conf: not stated
- class: not stated
- holds: Manor2017, YeDoak2009, Donato2013
- src: none (the reviewer's statement)
- trail: H2-01 §2.3

From the note:

> None of these measures a covariance matrix between overlapping gene sets.
>

## H2-04/shared-environment.6

Enrichment communities converge in function and in family-level taxonomy under a given carbon source.

- conf: not stated
- class: meas (marker)
- holds: enrichment communities; the cross-feeding mechanism modelled
- src: goldfordEmergentSimplicityMicrobial2018 (AB; measured, with the cross-feeding mechanism modelled)
- trail: H2-04 §Shared response to environment

From the note:

> Enrichment communities converge in function and family-level taxonomy under a given carbon source [11b, AB; measured, with the cross-feeding mechanism modelled].
>

## H2-04/aggregation-artefacts.4

Abundance-weighted versus species-weighted aggregation changed the sign of 27% of significant trait-climate results.

- conf: single (marker)
- class: meas (marker)
- holds: trait ecology (trait-climate results); figure checked by the critic against the abstract
- src: wieczynskiClimateShapesShifts2018 (AB; measured; single study)
- trail: H2-04 §Artefacts of aggregation, §critic

From the note:

> Abundance-weighted versus species-weighted aggregation changed the sign of 27% of significant trait-climate results [32, AB; measured; single study].
>
> Artefacts: compositional closure [8 abstract; 31 full text], method disagreement (31.5% shared edges) [31], annotation reference choice (65.4% of network variance) [13, full text], weighting choices (27% of sign changes in trait ecology) [32, abstract], and aggregation of unit-level values that produces correlations among community means through repeated co-occurrence alone [12, abstract, modelled].
>
> I checked the main numerical claims against primary text and they hold: Deutschmann 2021 (8.3/24.8/25.7/84.6%; 38 to 86% of true interactions removed), Kishore 2023 (65.4%, 26.8%), Kamneva 2017 (9.84%, 3.81%), Kembel & Cahill 2011 (92 to 98%), Kehe 2021 (68%, Spearman 0.75), Westoby 2021 (pairwise r2 at most 0.0121), Wieczynski 2019 (27%, abstract), Siefert 2015 (25%, 32%), Nielsen 2014 (abstract counts), Freilich 2018 (0.469, 0.527), Tian 2020 (species-pool null).
>

## H2-04/axis-agreement.4

By modelling on profiles built from the same genomes, how genes are distributed across genomes (functional redundancy) governs how community functional profiles respond to taxonomic perturbation (predicted versus observed shifts r = 0.86, n = 8): a modelled, indirect link.

- conf: not stated
- class: model (marker)
- holds: profiles built from the same genomes; n = 8; the critic: r = 0.86 could not be rechecked
- src: engTaxafunctionRobustnessMicrobial2018 (FT; modelled; indirect)
- trail: H2-04 §Genome-level versus community-level, §answers, §Adversarial critique
- limit: access (critic: H2-04:C-063)

From the note:

> Eng & Borenstein show, by modelling on profiles built from the same genomes, that gene distribution across genomes governs how community functional profiles respond to taxonomic perturbation (predicted versus observed shifts r = 0.86, n = 8) [8a, FT; modelled; indirect].
>
> Eng & Borenstein show that how genes are distributed across genomes (functional redundancy) governs how community functional profiles respond to taxonomic perturbation, a modelled indirect link [8a, full text].
>
> - Eng & Borenstein 2018 'r = 0.86, n = 8' and Levy & Borenstein 'rho = 0.211 / -0.193' could not be rechecked (Levy PMC text not retrievable). The Levy values rest on a tool summary.
>

## H2-04/within-between-partition.9

The plant partitions are measured and partly replicated, but concern species traits, not gene content.

- conf: not stated
- class: meas (note: "The plant partitions are measured")
- holds: plant trait ecology
- src: none (the review's assessment of the plant sources)
- trail: H2-04 §answers

From the note:

> The plant partitions are measured and partly replicated but concern species traits, not gene content..
>

## H2-04/association-networks.12

Metacommunity disturbance alone can generate associations between non-interacting species.

- conf: not stated
- class: model (marker)
- holds: macroecology; a preprint
- src: calcagnoMetacommunityDynamicsDetection2021 (AB; modelled; preprint)
- trail: H2-04 §Taxon networks

From the note:

> In macroecology, joint species distribution models cannot separate environment from interaction [24c, AB; derived], residual correlations depend on prevalence [37, AB; modelled], and metacommunity disturbance alone can generate associations between non-interacting species [4a, AB; modelled; preprint].
>

## H2-04/covariation-sources.2

No study was found that names all five sources for the same function-by-sample table.

- conf: not stated
- class: search (note: "No study found")
- holds: routes: Europe PMC REST keyword searches, Crossref, OpenAlex, PMC full text, three independent search angles (complementarity, co-occurrence, trait ecology); WebSearch and Scholar Gateway unavailable
- src: none (a search result)
- trail: H2-04 §answers

From the note:

> *Not measured:* No study found that names all five sources for the same function-by-sample table.
>
> Search routes: Europe PMC REST keyword searches, Crossref, OpenAlex, PMC full text, three independent search angles (complementarity, co-occurrence, trait ecology); WebSearch and Scholar Gateway unavailable..
>

## H2-04/genome-linkage.2

In 2,540 aquifer genomes, most organisms carried one step of sequential redox pathways, few carried two, and very few three or more (a stepwise division of redox pathways across genomes); the authors argue incompleteness does not explain this.

- conf: single (marker)
- class: deriv (marker)
- holds: one aquifer system; community composition and genomes from the same metagenomes; the critic: one aquifer study, not a class of functions
- src: anantharamanThousandsMicrobialGenomes2016 (FT; derived; single study)
- trail: H2-04 §Linkage within genomes, §answers, §Adversarial critique

From the note:

> In 2,540 aquifer genomes, most organisms carried one step of sequential redox pathways, few carried two, and very few three or more; the authors argue incompleteness does not explain this [3a, FT; derived; single study; community composition and genomes from the same metagenomes].
>
> Derived genome-resolved evidence shows stepwise division of redox pathways across aquifer genomes [3a, full text].
>
> - Section 2 'For such functions, within-genome linkage is weak and pathway completion is distributed across organisms' generalises from one aquifer study (Anantharaman 2016) to a class of functions.
>

## H2-04/covariation-sources.4

The claims that each source exists survive removal of any one source.

- conf: not stated
- class: not stated
- holds: the review's single-source sensitivity check for case D1(a)
- src: none (the review's sensitivity check)
- trail: H2-04 §answers

From the note:

> *Single-source sensitivity:* The existence claims survive removal of any one source.
>

## H2-04/shared-environment.5

Ocean functional groups track environment strongly while taxonomy within groups does not; the functional groups are assigned from taxonomy, so they are not independent of composition.

- conf: cont (marker)
- class: deriv (marker)
- holds: the global ocean
- src: loucaDecouplingFunctionTaxonomy2016 (AB; derived; functional groups assigned from taxonomy, so not independent of composition; contested)
- trail: H2-04 §Shared response to environment

From the note:

> For functions, ocean functional groups track environment strongly while taxonomy within groups does not [18b, AB; derived; functional groups assigned from taxonomy, so not independent of composition; contested].
>

## H2-04/within-between-partition.5

Ackerly & Cornwell find among-community covariation dominant, while Kembel & Cahill find correlations among species means driven by the within-community component; these are different systems.

- conf: not stated
- class: not stated
- holds: California woody plants versus grasslands
- src: ackerlyTraitbasedApproachCommunity2007, kembelIndependentEvolutionLeaf2011
- trail: H2-04 §answers

From the note:

> In plants, Ackerly & Cornwell find among-community covariation dominant while Kembel & Cahill find correlations among species means driven by the within-community component; these are different systems and are not contradictory in the strict sense..
>

## H2-04/complementarity-overlap.18

The complementarity readings rest on genome-derived auxotrophies, whose sensitivity against 36 strains with known auxotrophies was 75.5% (gapseq) and 43.4% (AGORA2), and on annotation gaps.

- conf: not stated
- class: model (marker)
- holds: modelled with measured validation, 36 strains
- src: starkeAminoAcidAuxotrophies2023 (FT; modelled with measured validation), priceFillingGapsBacterial2018
- trail: H2-04 §Complementarity versus overlap, §answers, §Adversarial critique

From the note:

> The complementarity readings rest on genome-derived auxotrophies, whose sensitivity against 36 strains with known auxotrophies was 75.5% (gapseq) and 43.4% (AGORA2) [29, FT; modelled with measured validation], and on annotation gaps [25].
>
> Cautions on the complementarity side: predicted auxotrophies are often annotation gaps [25, abstract]; model auxotrophy sensitivity is 43.4 to 75.5% and falls with genome incompleteness [29, full text].
>
> The complementarity side's genome-derived auxotrophy caution is quantified (43.4 to 75.5% sensitivity), but no equivalent error rate is applied to the co-occurrence side when the strength ratings are set.
>

## H2-04/shared-ancestry.1

Phylogeny is the largest single predictor of pairwise co-occurrence among the indices tested.

- conf: single (critic: H2-04:C-065)
- class: not stated
- holds: pairwise co-occurrence of gut taxa; four genomic indices tested; the data of Levy & Borenstein reused
- src: kamnevaGenomeCompositionPhylogeny2017 (FT)
- trail: H2-04 §Shared ancestry, §answers, §Adversarial critique

From the note:

> Shared ancestry: co-occurring and positively associated taxa are phylogenetically close and functionally similar [4, 9, full text]; phylogeny is the largest single predictor of pairwise co-occurrence [14, full text]; community-level genomic trait distance tracks UniFrac distance (R2 = 0.32) [23, full text].
>
> - D1(a) and section 6 'Phylogeny is the largest single predictor of pairwise co-occurrence' rests on Kamneva 2017, which reuses Levy & Borenstein's gut data and tested only four genomic indices.
>

## NFERT/symbiotic-fixation.1

Legumes in symbiosis with rhizobia are the largest biological nitrogen input to cropping systems, and their effect on fertiliser demand is documented.

- conf: not stated
- class: not stated
- holds: cropping systems
- src: ladhaBiologicalNitrogenFixation2022
- trail: NFERT §The strong, direct channel

From the note:

> Legumes in symbiosis with rhizobia are the largest biological nitrogen input to cropping systems, and their effect on fertiliser demand is documented (Ladha et al. 2022).
>

## NFERT/symbiotic-fixation.4

The fraction of legume nitrogen derived from fixation varies enormously, from a few percent to nearly all, depending on species, soil mineral nitrogen and competition.

- conf: not stated
- class: not stated
- holds: legumes across species and soils
- src: angladeRelationshipsEstimatingN22015, ladhaBiologicalNitrogenFixation2022
- trail: NFERT §The strong, direct channel

From the note:

> Two qualifications bound even this channel.
>
> The fraction of legume nitrogen derived from fixation varies enormously, from a few percent to nearly all, depending on species, soil mineral nitrogen, and competition (Anglade et al. 2015; Ladha et al. 2022).
>

## NFERT/mineralisation.2

Quantifying soil nitrogen supply can improve fertiliser-use efficiency and trim rates, but the lever is the measured soil supply, not a demonstrated property of microbial-community efficiency.

- conf: not stated
- class: not stated
- holds: stated by the reviewer after St. Luce et al.
- src: stluceNitrogenDynamicsIndices2011
- trail: NFERT §The weak channel

From the note:

> Quantifying soil nitrogen supply can improve fertiliser-use efficiency and trim rates, but the lever is the measured soil supply, not a demonstrated property of microbial-community efficiency.
>

## NFERT/manufacturing-energy.1

Modern natural-gas plants need roughly 28 GJ per tonne of ammonia.

- conf: not stated
- class: not stated
- holds: modern natural-gas plants
- src: tockThermoEnvironomicEvaluation2015, demirhanSustainableAmmoniaProduction2019
- trail: NFERT §Energy per unit

From the note:

> Modern natural-gas plants need roughly 28 GJ per tonne of ammonia (Tock et al. 2015; Demirhan et al. 2019).
>

## NFERT/symbiotic-fixation.2

In an organic legume-based rotation in Europe, 87% of total nitrogen inputs came from fixation, and the rotation matched conventional productivity at a surplus of only 21 kg N per hectare per year against 40 to 100 for fertilised systems.

- conf: not stated
- class: not stated
- holds: an organic legume-based rotation in Europe
- src: angladeRelationshipsEstimatingN22015
- trail: NFERT §The strong, direct channel

From the note:

> In an organic legume-based rotation in Europe, 87% of total nitrogen inputs came from fixation, and the rotation matched conventional productivity at a surplus of only 21 kg N per hectare per year against 40 to 100 for fertilised systems (Anglade et al. 2015).
>

## NFERT/emission-share.3

Independent process studies place ammonia manufacture at roughly 1% to 1.8% of global greenhouse-gas emissions.

- conf: not stated
- class: not stated
- holds: ammonia manufacture
- src: tunaTechnoEconomicAssessment2014, demirhanSustainableAmmoniaProduction2019, tockThermoEnvironomicEvaluation2015
- trail: NFERT §Share of emissions

From the note:

> Independent process studies place ammonia manufacture at roughly 1% to 1.8% of global greenhouse-gas emissions (Tunå et al. 2014; Demirhan et al. 2019; Tock et al. 2015).
>

## TAXRES/informal-labels.1

Informal labels in the data (`AMF`, `Asgard`, `A21b`) almost certainly have no canonical taxon, confirming a review-queue residual as on the gene side.

- conf: not stated
- class: not stated
- holds: biblion's data; listed by the note among what still needs confirming
- src: none (the note cites nothing for it)
- trail: TAXRES §What still needs confirming

From the note:

> - **Informal labels** in the data (`AMF`, `Asgard`, `A21b`) almost certainly have no canonical taxon, confirming a review-queue residual as on the gene side.
>

## TAXRES/cross-kingdom-backbone.4

The GBIF backbone build has been discontinued in favour of the eXtended Catalogue of Life (COL XR), which is now the cross-kingdom backbone to track.

- conf: not stated
- class: not stated
- holds: as found by a single-pass web search on 2026-06-19
- src: gbifGBIFBackboneTaxonomy, gbifSixQuestionsAnswered, silvaPytaxonPythonSoftware2025, ropensciGnrResolveGlobal
- trail: TAXRES §The cross-kingdom backbone

From the note:

> Note: the GBIF backbone build has been **discontinued in favour of the eXtended Catalogue of Life (COL XR)**, which is now the cross-kingdom backbone to track.
>
> Searched 2026-06-19 across four angles: NCBI-vs-GTDB divergence, taxon-name resolution tools, GTDB structure/identifiers, and the GBIF/Catalogue-of-Life cross-kingdom backbone.
>

## TAXRES/gtdb-ncbi-divergence.3

GTDB made the abrupt switch to the new phylum names in R08-RS214 (2023).

- conf: not stated
- class: not stated
- holds: GTDB release R08-RS214
- src: anonHarmonizingProkaryoticNomenclature2022
- trail: TAXRES §The NCBI-vs-GTDB divergence

From the note:

> - The phylum renamings biblion's tags already use (`Firmicutes` to **Bacillota**, `Proteobacteria` to **Pseudomonadota**) were controversial; GTDB made the abrupt switch in R08-RS214 (2023), and **NCBI and LPSN have since adopted the valid names** under nomenclatural requirements, not by coordination.
>

## TAXRES/cross-kingdom-backbone.3

Fungi enter the GBIF backbone via Index Fungorum.

- conf: not stated
- class: not stated
- holds: the GBIF Backbone Taxonomy
- src: gbifGBIFBackboneTaxonomy, gbifSixQuestionsAnswered, silvaPytaxonPythonSoftware2025, ropensciGnrResolveGlobal
- trail: TAXRES §The cross-kingdom backbone

From the note:

> Fungi enter via **Index Fungorum** (114,301 names; one of three recognised fungal repositories with MycoBank and Fungal Names).
>

## TSL/c-tf-idf.1

c-TF-IDF (BERTopic, Grootendorst 2022) treats each cluster as one document, L1-normalises tf for cluster size, and down-weights via log(1 + A/f_t).

- conf: not stated
- class: not stated
- holds: BERTopic's class-based TF-IDF procedure, as described in the paper and its documentation
- src: grootendorstBERTopicNeuralTopic2022, anonCTFIDFDocumentation
- trail: TSL §1. Specificity signals
- rating: "Confidence: high (3-0)"

From the note:

> - **Class/group df — c-TF-IDF** [S3] — BERTopic (Grootendorst 2022): treat each cluster as one document, L1-normalise tf for cluster size, down-weight via log(1 + A/f_t).
>
> *Confidence: high (3-0).*
>

## TSL/altitude-ordering.5

df is a good specificity signal but a weak altitude discriminator across the full range.

- conf: not stated
- class: not stated
- holds: the review's conclusion from the WordNet figures (altitude-ordering.3, .4)
- src: none (the reviewer's conclusion from altitude-ordering.3 and .4)
- trail: TSL §Verdict

From the note:

> So df is a good *specificity* signal but a weak *altitude discriminator* across the full range.
>

## TSL/altitude-ordering.6

One taxonomy-induction framework (Yang & Callan 2009) abandons a single fixed altitude signal and learns a separate information function per abstraction level: different feature sets win at different levels (co-occurrence alone for abstract L2–L3; contextual + co-occurrence + pattern + syntactic for concrete L4–L6), so no single fixed signal serves all altitudes.

- conf: not stated
- class: not stated
- holds: is-a taxonomy induction, not cluster-label ordering
- src: yangMetricbasedFrameworkAutomatic2009 (Indirect)
- trail: TSL §Verdict, §2. How multi-level
- rating: "Confidence: high (3-0)"

From the note:

> One taxonomy-induction framework [S5] abandons a single fixed altitude signal entirely, learning a separate information function per abstraction level.
>
> - **Learned, per-level information functions** [S5]: Yang & Callan (2009) found different feature sets win at different abstraction levels (co-occurrence alone for abstract L2–L3; contextual+co-occurrence+pattern+syntactic for concrete L4–L6) — i.e. no single fixed signal serves all altitudes.
>
> *Confidence: high (3-0).
>
> Indirect:* this is is-a taxonomy induction, not cluster-label ordering.
>

## TSL/altitude-ordering.3

Collection df reliably orders terms by specificity only at the specific end: ~74% accuracy overall on WordNet parent-child pairs, ~74–83% at the bottom two WordNet levels, degrading to ~55–68%, near-random, for general terms.

- conf: single (note: "the only direct empirical test")
- class: not stated
- holds: WordNet parent-child pairs; the bottom two levels vs general terms; not shown for cluster labels (altitude-ordering.8)
- src: johoDocumentFrequencyTerm2007
- trail: TSL §Verdict, §2. How multi-level
- rating: "Confidence: high (3-0)"

From the note:

> The qualification is decisive and comes from the only direct empirical test: **collection df reliably orders terms by specificity only at the specific end** (~74–83% accuracy at the bottom two WordNet levels) and **degrades to ~55–68% — near-random — for general terms** [S4].
>
> - **Collection df works only at the specific end** [S4]: ~74% overall on WordNet parent-child pairs, reliable only at the bottom two levels, ~55–68% for general terms.
>
> *Confidence: high (3-0).* This is the key bounding fact tempering §1.
>

