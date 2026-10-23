# Faithfulness check: 60 entries

## H1-05/other-habitats.9 (claim)

Across 148 trait datasets, which include diatoms and fungi but no bacteria, mean Mantel r along space was 0.254 taxonomic vs 0.115 functional, with about 31 of 148 datasets reversed.

- conf: not stated
- class: not stated
- holds: [48]; datasets including diatoms and fungi, no bacteria
- src: gracorozaDistanceDecay22022 (FT via agents)
- trail: H1-05 §1.6, §critic

From the note:

> - Non-microbial, 148 trait datasets: mean Mantel r along space 0.254 taxonomic vs 0.115 functional, with about 31 of 148 datasets reversed [48] [FT via agents].
>
> Evidence on non-soil systems: [48] includes diatoms and fungi but no bacteria, so it is not 'non-microbial'.
>
> - [48] is labelled 'FT via agents' but is openly available (PMC9322010). Its characterisation as 'non-microbial' is wrong: it includes diatoms and fungi (it lacks bacteria).
>
> - [48] is labelled 'non-microbial' but includes diatoms and fungi. That blurs the microbial vs non-microbial split the review uses.
>

## 16S/primers.2 (claim)

In silico, 175 primers and 512 pairs differ widely in coverage and phylum spectrum against SILVA 108.

- conf: repl (marker)
- class: deriv (marker)
- holds: in silico against SILVA 108
- src: klindworthEvaluationGeneral16S2013 (FT; deriv; repl)
- trail: MB-01 §2.3, §answers

From the note:

> **Primer coverage.** In silico, 175 primers and 512 pairs differ widely in coverage and phylum spectrum against SILVA 108 (Klindworth 2013) [FT; deriv; repl].
>
> Primers and region: in silico surveys cover 175 primers and 512 pairs (Klindworth 2013).
>

## 16S/ploidy.13 (claim)

That 16S copies per cell scale with origin number more than with genome number in fast growers is the reviewer's inference from one abstract; no source in the review measures 16S copies per cell against origin number.

- conf: not stated
- class: reading (critic: MB-02:C-140)
- holds: inference from Couturier and Rocha 2006 (abstract only)
- src: couturierReplicationassociatedGeneDosage2006 (AB)
- trail: MB-02 §D1.3, §answers, §critic, §Adversarial

From the note:

> In fast growers, origin number is therefore the better guide to 16S dosage than genome number.
>
> Because rRNA operons sit near the origin in fast growers [20], 16S copies per cell scale with origin number more than with genome number; E. coli has about 7.9 to 9.5 rRNA genes per genome equivalent across growth rates (secondary, Bremer and Dennis via BioNumbers [21]).
>
> The claim that 16S copies per cell scale with origin number is the reviewer's inference from an abstract [20]; no source in the review measures it.
>
> - D1(b): 'Because rRNA operons sit near the origin in fast growers, 16S copies per cell scale with origin number more than with genome number' rests on one abstract (Couturier and Rocha 2006 [20]) plus reviewer inference. No source in the review measures 16S copies per cell against origin number.
>
> - D1.3 and the D1(b) answer: '16S copies per cell scale with origin number more than with genome number' is the reviewer's inference from Couturier and Rocha's abstract, presented without a 'reviewer's reading' label.
>

## 16S/differential-abundance.4 (claim)

Microbiome-specific methods did not beat RNA-seq methods.

- conf: single (marker)
- class: meas (marker)
- holds: abstract only
- src: calgaroAssessmentStatisticalMethods2020 (AB; meas; single)
- trail: MB-01 §5.4

From the note:

> Microbiome-specific methods did not beat RNA-seq methods (Calgaro 2020) [AB; meas; single].
>

## H2-04/gene-level-networks.5 (claim)

Gene-level networks controlling for within-genome linkage were not found.

- conf: not stated
- class: search (note: "were not found")
- holds: the routes of case D1(a)
- src: none (a search result)
- trail: H2-04 §answers

From the note:

> Gene-level networks controlling for within-genome linkage were not found.
>

Not found in the cited text (where to look, not what is wrong): holds: d1

## H1-06/ph-preference.10 (claim)

In global topsoil (N = 217) and ocean (N = 125) 16S surveys analysed by CCA, OTU loadings on the first canonical direction, which aligns with pH in soil and with depth in the ocean, have strong phylogenetic signal (a modified tau_D and Pagel's lambda); this is a different quantity from a per-ASV pH optimum.

- conf: single (note: "SINGLE SOURCE")
- class: meas (note: "measured, natural, preprint")
- holds: global topsoil and ocean surveys; canonical loadings, not optima; the critic: qualitative, with no number quoted, since tau_D values "appear only in figures"
- src: chakravertiwuerthweinPhylogeneticCoherenceMicrobiome2026 (measured, natural, preprint, SINGLE SOURCE)
- trail: H1-06 §2. Part A1, §answers, §critic

From the note:

> One preprint points the other way on a different quantity.
>
> Chakraverti-Wuerthwein et al. 2026 [29] (measured, natural, preprint, SINGLE SOURCE) ran CCA on global topsoil (N = 217) and ocean (N = 125) 16S surveys.
>
> They report strong phylogenetic signal (a modified tau_D and Pagel's lambda) in OTU loadings on the first canonical direction, which aligns with pH in soil and with depth in the ocean.
>
> Natural-system field evidence (Ramoneda 2023, SILVA 138, 16S trees) gives weak signal for pH preference (Pagel's lambda 0.22 to 0.78, Moran's I < 0.25 at all depths), while a preprint (Chakraverti-Wuerthwein 2026) reports strong phylogenetic signal in the loadings of the pH-aligned canonical axis of global topsoil composition.
>
> - Chakraverti-Wuerthwein 2026 [29]: tau_D values 'appear only in figures', so the 'strong phylogenetic signal' claim is qualitative, with no number quoted. It is used in both the A1 and B verdicts.
>

## 16S/copy-number-correction.13 (claim)

A preprint by the tool's author reports essentially no correlation ("no meaningful correlation") between 16S read and species frequencies in mocks; correction for copy number and primer mismatch reached r of about 0.6 only in ideal cases (exact references), falling to about 0.4 at 97% and about 0.2 at 95% identity.

- conf: single (marker)
- class: meas (marker)
- holds: mocks; preprint abstract only; MB-01 sets it aside as a single-source contrary result, which its critic says applies a single-source label to one side only, since the pro-correction results it conflicts with (McLaren, Silverman) each also rest on a single mock design
- src: edgarUNBIASAttemptCorrect2017 (AB; PREPRINT; meas; single)
- trail: MB-01 §2.14, §7. Bounds, §answers, §Adversarial, MB-02 §D1.4, §answers

From the note:

> **Strong pessimistic claim.** A preprint by the tool's author reports essentially no correlation between 16S read and species frequencies in mocks.
>
> Correction for copy number and primer mismatch reached r of about 0.6 only in ideal cases (Edgar 2017b, UNBIAS) [AB; PREPRINT; meas; single].
>
> An abstract-only preprint reports essentially no correlation between read and species frequencies (Edgar 2017b, UNBIAS).
>
> It conflicts with the good fits obtained by Brooks, McLaren and Silverman and is reported as a single-source contrary result.
>
> - UNBIAS (Edgar 2017b);
>
> - Section 2.14 labels Edgar 2017b (UNBIAS) a 'strong pessimistic claim' and sets it aside as a single-source contrary result. The pro-correction results it conflicts with (McLaren, Silverman) each also rest on a single mock design and get no matching single-source label at that point.
>
> - **Edgar 2017** [31, AB, preprint]: read frequencies in mocks had "no meaningful correlation" with species frequencies.
>
> Correction reached r of about 0.6 when references were exact, falling to about 0.4 at 97% and about 0.2 at 95% identity.
>
> Against this, eleven DNA-based mock communities fitted 7.1% better without correction [32], and one preprint found read frequencies uncorrelated with species frequencies in mocks and correction reaching only r about 0.6, falling to about 0.2 at 95% reference identity [31].
>
> Only the anti-correction preprint is flagged for its standing.
>

Not found in the cited text (where to look, not what is wrong): holds: mb-01

## 16S/primers.1 (claim)

Primer and region choices include V1-V2 through V7-V9 and full length, degenerate variants of 515F and 806R, and PNA clamps against host plastids.

- conf: not stated
- class: not stated
- holds: the primer studies below
- src: waltersImprovedBacterial16S2016, abellanschneyderPrimerPipelinesParameters2021, fitzpatrickChloroplastSequenceVariation2018
- trail: MB-01 §answers

From the note:

> Choices include V1-V2 through V7-V9 and full length, degenerate variants of 515F and 806R, and PNA clamps against host plastids (Walters 2016; Abellan-Schneyder 2021; Fitzpatrick 2018).
>

## H1-06/uncontrolled-rank-studies.10 (claim)

Apart from the one controlled reanalysis, the rank-wise studies are uncontrolled, and two are preprints.

- conf: not stated
- class: not stated
- holds: Mayjonade 2024 and Chakraverti-Wuerthwein 2026 are the preprints
- src: mayjonadeRelativeEffectsAbiotic2024, chakravertiwuerthweinPhylogeneticCoherenceMicrobiome2026
- trail: H1-06 §5. Bounds and failure modes

From the note:

> The other rank-wise studies are uncontrolled, and two are preprints [24, 29].
>

Not found in the cited text (where to look, not what is wrong): holds: mayjonade; holds: 2024; holds: chakraverti-wuerthwein; holds: 2026

## H1-02/gene-class-loss.6 (claim)

In 11 soil, seawater and gut metagenomes assembled at three depths with two assemblers, contigs carrying ribosomal-protein genes were longer regardless of environmental origins of samples, sequencing depths, and assemblers.

- conf: not stated
- class: not stated
- holds: the critic's reading of the full text; a bounding fact relevant to soil and depth that the review omitted, citing the source only for gut and seawater
- src: miseUnexpectedAbsenceRibosomal2022
- trail: H1-02 §critic, §Adversarial critique

From the note:

> One bounding fact across soil, seawater and gut (ribosomal-protein contigs assembled well regardless of environment, three depths and two assemblers [6]) was omitted.
>
> - gap: Mise and Iwasaki [6] assembled 11 soil, seawater and gut metagenomes at three depths with two assemblers.
>
> Contigs carrying ribosomal-protein genes were longer 'regardless of environmental origins of samples, sequencing depths, and assemblers'.
>
> This is a bounding fact relevant to Part B soil and depth, but the review cites [6] only for gut and seawater.; setting_or_class: Agricultural and paddy soil metagenomes; depth dependence of assembly of specific gene classes; brief_bullet: Re-read [6] Fig. 3 and Supp.
>

## H1-05/redundancy.6 (claim)

The review counts as against or complicating redundancy: coupling holds when all genes are used [31]; functional dispersion tracks taxonomic dispersion [22]; decoupling vanishes at species resolution within groups [11]; averaging alone reproduces lower functional variability [29][30]; function is more responsive under some weak contrasts [5][15].

- conf: not stated
- class: not stated
- holds: the review's classification of its sources
- src: galandStrongLinkMarine2018, xuDistinctivePatternMechanism2022, liuReciprocalChangesDominant2023, hoChallengesInterpretingFunctional2025, hoChallengesQuantifyingFunctional2024, gaoLongtermWarmingMediterraneantype2021, maDivergentTaxonomicFunctional2017
- trail: H1-05 §3.4, §answers

From the note:

> - **Against or complicating:**
>
> - Functional dispersion tracks taxonomic dispersion [22].
>
> - Decoupling vanishes at species resolution within groups [11].
>
> - Averaging alone reproduces lower functional variability [29][30].
>
> - Function is more responsive under some weak contrasts [5][15].
>
> Against or complicating, [11][22][31][29].
>

Not found in the cited text (where to look, not what is wrong): holds: review; holds: its

## NFERT/emission-share.6 (claim)

The full nitrogen-fertiliser life cycle including manure is larger still: Gao and Cabrera Serrenho (2023) put production and use at about 5% of global greenhouse-gas emissions, roughly two-thirds occurring after deployment and one-third during production.

- conf: not stated
- class: not stated
- holds: full N-fertiliser life cycle, manure included
- src: gaoGreenhouseGasEmissions2023
- trail: NFERT §Share of emissions

From the note:

> The full nitrogen-fertiliser life cycle including manure is larger still.
>
> Gao and Cabrera Serrenho (2023) put production and use at about 5% of global greenhouse-gas emissions, with roughly two-thirds occurring after deployment and one-third during production.
>

Not found in the cited text (where to look, not what is wrong): holds: n-fertiliser

## CB2/depth-axis.4 (claim)

The closest work is Haryono et al., who show MAG quality tracking normalised coverage decile by decile, but their quality axis there is the completeness/contamination classification, not rRNA presence.

- conf: not stated
- class: not stated
- holds: tropical activated sludge; completeness/contamination, not rRNA
- src: haryonoRecoveryHighQuality2022
- trail: CB2-RRNA §5. What is measured

From the note:

> The closest is Haryono et al., who show MAG quality tracking normalised coverage decile by decile — but their quality axis there is the completeness/contamination classification, not rRNA presence.
>

Not found in the cited text (where to look, not what is wrong): holds: tropical; holds: sludge

## 16S/abundance-distribution.1 (claim)

In 24 Oklahoma grassland soils, the best-fitting abundance distributions were exponential or inverse gamma; these best fits are in the paper's supplementary Table S3, the main text does not state which distributions won, and they were not verified.

- conf: single (marker)
- class: model (marker)
- holds: 24 grassland soils, 454 data; soil SAD shape rests on Zhou 2013 and Haegeman 2013
- limit: access (critic: MB-01:C-079)
- src: zhouRandomSamplingProcess2013 (FT; model; single)
- trail: MB-01 §3.4, §answers, §critic, §Adversarial

From the note:

> - In 24 grassland soils, the best-fitting distributions were exponential or inverse gamma (Zhou 2013) [FT; model; single].
>
> Shape of abundance distributions.
>
> Soil: exponential or inverse-gamma fits to 24 grassland soils (Zhou 2013, modelled).
>
> Soil SAD shape rests on Zhou 2013 and Haegeman 2013.
>
> (2) Abundance-distribution shapes split by environment are weaker than presented.
>
> The soil 'exponential or inverse gamma' best fits are in Zhou 2013's supplementary Table S3; the main text does not state them and they were not verified.
>
> - Zhou 2013 (FT): 'in 24 grassland soils, the best-fitting distributions were exponential or inverse gamma'.
>
> The best-fit results are in supplementary Table S3; the main text does not state which distributions won.
>
> The claim rests on unread or unshown supplementary material.
>

Not found in the cited text (where to look, not what is wrong): Oklahoma; holds: 454

## TSL/frequency-bucketing.3 (claim)

No reviewed source benchmarks discrete bands for ordering labels.

- conf: not stated
- class: search (note: "No reviewed source benchmarks discrete bands")
- holds: the sources the review found
- src: none (a statement about what the review found)
- trail: TSL §Verdict

From the note:

> No reviewed source benchmarks discrete bands for *ordering* labels; log binning is only a *proposed* mitigation for distribution analysis [S7b], not validated for label banding.
>

## CB3/food-system.16 (claim)

A search for published criticism or formal comment disputing the EDGAR-FOOD "one third" figure or its land-use attribution found none; the qualifications on that figure come from its own authors and from boundary comparisons (Tubiello, OWID), not from an adversarial literature.

- conf: not stated
- class: search (note: "found none")
- holds: the review's search by web search, direct page fetch, and where available the biblion corpus and Scholar Gateway semantic search
- src: none (a search result)
- trail: CB3-AG-EMISSIONS §Bounding and negative facts

From the note:

> - **Absence of evidence.** I searched specifically for published criticism or formal comment disputing the EDGAR-FOOD "one third" figure or its land-use attribution and **found none**.
>
> The qualifications on that figure come from its own authors and from boundary comparisons (Tubiello, OWID), not from an adversarial literature.
>
> Sources: web search, direct page fetch, and where available the biblion corpus and Scholar Gateway semantic search.
>

Not found in the cited text (where to look, not what is wrong): holds: review

## H1-RES/capacity-expression.11 (claim)

Multiple high-profile studies document taxa that are metagenomically abundant yet transcriptionally or translationally inactive, and show that many ecosystem- or disease-relevant signals are detectable only at the RNA or protein level.

- conf: repl (note: "Consistent qualitative patterns")
- class: not stated
- holds: human gut and disease cohorts, murine inflammation, ocean and soil enzymes
- src: franzosaRelatingMetatranscriptomeMetagenome2014, schirmer2018, heintzbuschart2016, galata2021, jovel2022, zhao2024, wang2024
- trail: H1-RES §Quantitative synthesis

From the note:

> - **Consistent qualitative patterns** Multiple high-profile studies document taxa that are metagenomically abundant yet transcriptionally or translationally inactive, and they show that many ecosystem- or disease-relevant signals are detectable only at the RNA or protein level [2] [3] [4] [5] [6] [7].
>

Not found in the cited text (where to look, not what is wrong): holds: human; holds: gut; holds: murine; holds: ocean; holds: soil

## H1-06/dns.6 (do not say)

"The rise in explained variance from otu97 to about otu94 and genus matches where perturbation responses cluster (tau_D about 0.017 to 0.02, about genus)."

- why: links a natural-system composition result to engineered perturbation-response depths, breaking the natural/engineered separation (Common rule 10); a correspondence the sources do not test
- instead: ab-relation.1
- trail: H1-06 §critic

From the note:

> - 'Relation to Part A (reviewer's reading)' links a natural-system composition result (Lu 2016, otu97-to-genus rise) to engineered perturbation-response depths (Isobe 2019, 2020, tau_D ~0.017, 'about genus'), which breaks Common rule 10's natural/engineered separation. It is labelled reviewer's reading, but it presents a correspondence the sources do not test.
>

Not found in the cited text (where to look, not what is wrong): 0.02; "The rise in explained variance from otu97 to about otu94 and genus matches where perturbation responses cluster (tau_D about 0.017 to 0.02, about genus)."

## CB1/ghg-balance.2 (claim)

Gibbons et al., working on UK livestock farms, reported that liming to pH 6.0 as recommended reduced N₂O emissions and nitrate leaching, but that in CO₂-C equivalents "the GHG emissions from liming were about four times those saved by reducing N₂O emissions."

- conf: not stated
- class: not stated
- holds: UK livestock farms, liming to pH 6.0
- src: gibbonsSustainableNutrientManagement2014 (second-hand, described by Goulding), gouldingSoilAcidificationImportance2016
- trail: CB1-LIMING §5. Where the numbers
- limit: access (note: "I did not read the Gibbons paper in the original")

From the note:

> Against that, Gibbons et al., working on UK livestock farms, reported that liming to pH 6.0 as recommended reduced N₂O emissions and nitrate leaching, but that in CO₂-C equivalents "the GHG emissions from liming were about four times those saved by reducing N₂O emissions" [19, described to me by Goulding at 7].
>
> I am not adjudicating that; the scopes, baselines and emission factors differ and I did not read the Gibbons paper in the original.
>

## H2-01/direct-dimension.5 (claim)

In 128 soil metagenomes, the first four multiple co-inertia axes captured 29%, 21%, 16% and 10% of variation; this is the only variance-explained figure for a microbial functional profile.

- conf: single (critic: H2-01:C-009)
- class: not stated
- holds: global topsoil set; KEGG, eggNOG, SEED, CAZy and genomic-trait tables, relative abundance normalised by annotated bacterial reads, log(x+1), z-scored
- src: pitonLifeHistoryStrategies2023 (FT per trait-ecology angle, not re-checked by the reviewer, critic: H2-01:C-064)
- trail: H2-01 §2.1, §answers

From the note:

> - **Soil, community-aggregated traits, co-inertia.** In 128 soil metagenomes (global topsoil set) with KEGG, eggNOG, SEED, CAZy and genomic-trait tables (relative abundance normalised by annotated bacterial reads, log(x+1), z-scored), the first four multiple co-inertia axes captured 29%, 21%, 16% and 10% of variation.
>
> In 128 soils, two co-inertia axes carried 29% and 21% of variation and the next two 16% and 10% [Piton2023].
>
> Removing Piton2023 leaves no variance-explained figure for a microbial functional profile.
>
> All three direct microbial estimates (Jiang2012, Piton2023, Flinkstrom2024) are single studies fitted and scored on the same samples.
>
> - D1 access_basis says 'Mostly full text', but the synthesis re-opened only Chen2020 and Manor2017. Piton2023 (the only variance-explained figure), Mouillot2021 (the only measured dependence of dimension on feature and sample count), Nayfach2015, HMP2012 and Tian2020 are full text 'per angle' and were not re-checked, even though they are named as single points of failure.
>

## CB2/depth-axis.5 (claim)

Coverage of an organism is not the same variable as depth of a library; the two are only loosely coupled through community evenness.

- conf: not stated
- class: not stated
- holds: stated by the reviewer
- src: none (the reviewer's statement)
- trail: CB2-RRNA §5. What is measured

From the note:

> Coverage of an *organism* is not the same variable as depth of a *library*, and the two are only loosely coupled through community evenness.
>

## 16S/dns.43 (do not say)

"Occupancy-based core methods performed best" as an established standard.

- why: rests on one simulation study (Custer 2023)
- instead: term-sensitivity.7
- trail: MB-02 §Adversarial

From the note:

> - D2: 'Occupancy-based core methods performed best' rests on one simulation study (Custer et al. 2023 [52]) and is listed among proposed standards as if established.
>

## H2-01/genome-size.3 (claim)

Species abundance explained 74% of average-genome-size variation across HMP samples.

- conf: not stated
- class: meas (marker)
- holds: HMP samples
- src: nayfachAverageGenomeSize2015 (FT per metagenomics angle, AB per statistics angle, not re-checked by the reviewer, critic: H2-01:C-064; measured)
- trail: H2-01 §2.3

From the note:

> Species abundance explained 74% of average-genome-size variation across HMP samples, and genome-size variation makes genes at equal per-cell copy number look variable and hides real per-cell variation [Nayfach2015; FT per metagenomics angle, AB per statistics angle; measured].
>
> - D1 access_basis says 'Mostly full text', but the synthesis re-opened only Chen2020 and Manor2017. Piton2023 (the only variance-explained figure), Mouillot2021 (the only measured dependence of dimension on feature and sample count), Nayfach2015, HMP2012 and Tian2020 are full text 'per angle' and were not re-checked, even though they are named as single points of failure.
>

## TSL/minimum-support.3 (claim)

About 30% of the vocabulary is removable without qualitative topic loss, independent of the pruning criterion (df, tf or TF-IDF).

- conf: single (note: "single simulated-corpus LDA study")
- class: model (note: "simulated-LDA Monte Carlo study")
- holds: LDA on simulated corpora (Bystrov et al.); not shown on real corpora or non-LDA pipelines (gap.2)
- src: bystrovAnalysingImpactRemoving2023
- trail: TSL §4. Minimum-support, §Open Questions, §Standing caveats

From the note:

> - **Standard conventions** [S8]: drop frequency-1 (Blei et al. 2003); <0.5–1% of docs (Denny & Spirling 2018); >99% as stopwords (Grimmer & Stewart 2013; Maier et al. 2018). ~30% of vocabulary removable without qualitative topic loss, independent of criterion (df, tf, or TF-IDF).
>
> *Confidence: high (3-0).* Caveats: conventions, not optima; evidence is a **single simulated-corpus LDA study**; two claims that aggressive pruning is uniformly safe were **refuted** (0-3).
>
> **Real-corpus replication:** do the bucketing instabilities (9.3% vs 74.1%) and ~30%-removable findings hold on *real* corpora and non-LDA pipelines (e.g. BERTopic c-TF-IDF)?
>
> Primary evidence is one simulated-LDA study.
>
> The bucketing/pruning evidence leans heavily on one simulated-LDA Monte Carlo study (Bystrov et al.).
>

Not found in the cited text (where to look, not what is wrong): holds: gap.2

## H1-06/salinity-preference.3 (claim)

Morrissey and Franklin reported no depth statistic for salinity preference.

- conf: not stated
- class: not stated
- holds: the same reciprocal transplant
- src: morrisseyEvolutionaryHistoryInfluences2015
- trail: H1-06 §2. Part A1

From the note:

> No depth statistic was reported.
>

## 16S/rarefying.16 (claim)

Rarefying is contested: McMurdie and Holmes 2014 against Schloss 2024a and 2024b, Weiss 2017 and Hong 2022 (partial), with Willis 2019 opposing it for richness; beta-diversity results are contested and simulation-based, and simulation results flip with design choices, as Weiss 2017 and Schloss 2024a both say.

- conf: cont (note: "contested")
- class: model (note: "simulation-based")
- holds: simulations
- src: mcmurdieWasteNotWant2014, schlossWasteNotWant2024, schlossRarefactionCurrentlyBest2024, weissNormalizationMicrobialDifferential2017, hongRarefyNotRarefy2022, willisRarefactionAlphaDiversity2019
- trail: MB-01 §answers, §6. Where

From the note:

> *Conflicts:* Rarefying: McMurdie and Holmes 2014 versus Schloss 2024a and 2024b, Weiss 2017 and Hong 2022 (partial), with Willis 2019 opposing it for richness.
>
> Beta: contested, simulation-based.
>
> Simulation results flip with design choices; Weiss 2017 and Schloss 2024a both say so.
>
> Rarefying: McMurdie and Holmes 2014 versus Schloss 2024a and 2024b, Weiss 2017 and Hong 2022.
>
> Willis 2019 opposes rarefying for richness.
>

## H1-05/covariation.2 (claim)

Across 16 soils from cold desert, hot desert, forest, grassland and tundra, Bray-Curtis dissimilarity of MG-RAST/SEED gene profiles correlated with 16S Bray-Curtis (Mantel r = 0.76) and with unweighted UniFrac (r = 0.82).

- conf: not stated
- class: meas (marker)
- holds: 16 soils; only 13 to 23% of reads annotatable; desert and non-desert samples separated almost completely (ANOSIM R about 0.97 to 0.98)
- src: fiererCrossbiomeMetagenomicAnalyses2012 (FT, figures confirmed by the critic via PMC; measured; critic: H1-05:C-052, H1-05:C-053 was "FT, via search agents; measured")
- trail: H1-05 §1.1, §Adversarial critique

From the note:

> Across 16 soils from cold desert, hot desert, forest, grassland and tundra, Bray-Curtis dissimilarity of MG-RAST/SEED gene profiles correlated with 16S Bray-Curtis (Mantel r = 0.76) and unweighted UniFrac (r = 0.82) [1] [FT, via search agents; measured].
>
> Only 13 to 23% of reads were annotatable, and desert and non-desert samples separated almost completely (ANOSIM R about 0.97 to 0.98).
>
> - [1] and [2] are labelled 'FT via search agents', not rechecked by the reviewer.
>
> This critic confirmed the figures via PMC3535587 and PMC4568213, so the label can be upgraded.
>

## NFERT/emission-share.7 (claim)

Gao and Cabrera Serrenho report that manure emits about 23 t CO₂-equivalent per tonne of N, some 1.9 times an average synthetic fertiliser, because much of its nitrogen is lost.

- conf: not stated
- class: not stated
- holds: manure against an average synthetic fertiliser
- src: gaoGreenhouseGasEmissions2023
- trail: NFERT §Share of emissions

From the note:

> They identify nitrogen-use efficiency as the single most effective mitigation lever, and report that manure emits about 23 t CO₂-equivalent per tonne of N, some 1.9 times an average synthetic fertiliser, because much of its nitrogen is lost.
>

## H1-06/dns.2 (do not say)

"ASVs within single families spanned four or more pH units (Xanthobacteraceae in soil, Chitinophagaceae in freshwater)."

- why: the source gives Chitinophagaceae 4.63 to 8.35 (3.72 units), so it does not span four units
- instead: ph-preference.4
- trail: H1-06 §critic

From the note:

> ASVs within single families spanned four or more pH units (Xanthobacteraceae in soil, Chitinophagaceae in freshwater).
>
> The family claim is partly wrong: Chitinophagaceae spans 4.63 to 8.35 (3.72 units), not 'four or more pH units'.
>
> - [13] Ramoneda 2023 body claim: 'ASVs within single families spanned four or more pH units (Xanthobacteraceae in soil, Chitinophagaceae in freshwater)'. The source gives 4.01 to 8.20 (4.19 units) and 4.63 to 8.35 (3.72 units), so Chitinophagaceae does not span four units.
>

## TSL/altitude-ordering.7 (claim)

No controlled head-to-head exists comparing collection df vs class df vs IC for ordering descriptive cluster labels general→specific; the closest tests (Joho & Sanderson; Yang & Callan) are over WordNet / taxonomy induction, indirect for the label-ordering task.

- conf: not stated
- class: search (note: "no controlled head-to-head exists")
- holds: the sources the review found; the closest tests are WordNet and taxonomy induction
- src: johoDocumentFrequencyTerm2007, yangMetricbasedFrameworkAutomatic2009
- trail: TSL §Verdict, §Open Questions

From the note:

> **The most important negative result:** **no controlled head-to-head exists** comparing collection df vs class df vs IC for *ordering descriptive cluster labels* general→specific.
>
> The closest tests [S4, S5] are over WordNet / taxonomy induction — indirect for the label-ordering task.
>
> **Head-to-head (the core gap):** has any benchmark compared collection df vs class df (c-TF-IDF) vs IC for *ordering cluster labels* general→specific?
>
> Appears **not done**; closest tests are WordNet/taxonomy induction (indirect).
>

Not found in the cited text (where to look, not what is wrong): holds: review

## CB3/co2-accounting.1 (claim)

The CO2 accounting method (bookkeeping models versus national inventories/FAOSTAT) moves AFOLU between 13% and 21% of global emissions; AR6 states this directly.

- conf: not stated
- class: not stated
- holds: AFOLU, 2010–2019, IPCC AR6 WGIII Ch. 7
- src: nabuursAgricultureForestryOther2022
- trail: CB3-AG-EMISSIONS §Where the major sources differ

From the note:

> **CO2 accounting method** (bookkeeping models vs national inventories/FAOSTAT).
>
> AR6 states this directly: it moves AFOLU between 13% and 21% [1].
>

Not found in the cited text (where to look, not what is wrong): holds: 2010-2019; holds: ipcc; holds: wgiii; holds: ch; holds: 7

## H2-04/dns.6 (do not say)

"Moderate for the pattern that whole-community co-occurrence associates with overlap, replicated across independent groups but with weak effects."

- why: the overlap side rests on co-occurrence inference, which is method-dependent and poorly validated, with no error rate applied to it; the critic grades it weak to moderate
- instead: complementarity-overlap.5, complementarity-overlap.19
- trail: H2-04 §critic, §Adversarial critique

From the note:

> *Strength:* Moderate for the pattern that whole-community co-occurrence associates with overlap, replicated across independent groups but with weak effects.
>
> Strength: weak to moderate for overlap, weak for complementarity.
>
> - D1(c): the overlap side is rated moderate and 'replicated across independent groups', although it rests on co-occurrence inference.
>
> Section 3 of the review shows that inference to be method-dependent (31.5% shared edges) and poorly validated.
>
> The complementarity side's genome-derived auxotrophy caution is quantified (43.4 to 75.5% sensitivity), but no equivalent error rate is applied to the co-occurrence side when the strength ratings are set.
>

## CB3/food-system.12 (claim)

Poore & Nemecek 2018 sit lower because the boundary is narrower: "Today's food supply chain creates ~13.7 billion metric tons of carbon dioxide equivalents (CO2eq), 26% of anthropogenic GHG emissions"; their accounting stops at retail and excludes consumer cooking and waste.

- conf: not stated
- class: not stated
- holds: food supply chain to retail, food only; ~2010 baseline; CO2, CH4, N2O
- src: pooreReducingFoodS2018 (accepted manuscript, headline results)
- trail: CB3-AG-EMISSIONS §Boundary A

From the note:

> **Poore & Nemecek 2018** sit deliberately lower because the boundary is narrower: "Today's food supply chain creates ~13.7 billion metric tons of carbon dioxide equivalents (CO2eq), **26%** of anthropogenic GHG emissions.
>
> Their accounting stops at retail and excludes consumer cooking and waste.
>
> | 7 | Food supply chain to retail, food only | 26% | 13.7 Gt CO2eq | ~2010 baseline | CO2, CH4, N2O | Poore & Nemecek 2018 [10] | not stated in headline |
>

## 16S/ploidy.18 (claim)

In the reviewer's reading, about 2 fg of DNA is less than one copy of a 4 Mb genome, which suggests many soil cells hold one copy of a small genome; the note marks this as inference.

- conf: not stated
- class: reading (note: "In the reviewer's reading")
- holds: the clay-loam DNA-per-cell average
- src: christensenFlowCytometricMeasurements1995
- trail: MB-02 §D1.3

From the note:

> In the reviewer's reading, about 2 fg is less than one copy of a 4 Mb genome, which suggests many soil cells hold one copy of a small genome, but this is inference.
>

Not found in the cited text (where to look, not what is wrong): holds: clay-loam; holds: dna-per-cell

## CB1/emission-factor.12 (claim)

The EPA applies ±15% to the activity data and models the fraction of lime dissolved by nitric versus carbonic acid and the leached bicarbonate fraction as triangular distributions "between ranges of zero and 100 percent of the estimates"; its Monte Carlo result puts 2020 emissions "between -0.26 and 4.73 MMT CO₂ Eq. at the 95 percent confidence level," 111% below to 97% above the point estimate.

- conf: not stated
- class: model (note: "Its Monte Carlo result")
- holds: US national inventory, 2020
- src: usLimingCRFSource2022
- trail: CB1-LIMING §4. Carbon dioxide

From the note:

> **The inventory's own uncertainty range straddles zero.** EPA applies ±15% to the activity data, and models the fraction of lime dissolved by nitric versus carbonic acid and the leached bicarbonate fraction as triangular distributions "between ranges of zero and 100 percent of the estimates.
>
> Its Monte Carlo result: 2020 emissions "between -0.26 and 4.73 MMT CO₂ Eq. at the 95 percent confidence level," a range of 111% below to 97% above the point estimate.
>

Not found in the cited text (where to look, not what is wrong): holds: us

## H1-05/non-dna-function.1 (claim)

Across North America, soil fungi showed endemism with convergent enzyme activity; this is a non-DNA case and indirect for DNA profiles.

- conf: not stated
- class: not stated
- holds: North American soil mycobiome [21]; enzyme activity
- src: talbotEndemismFunctionalConvergence2014 (AB)
- trail: H1-05 §1.2

From the note:

> - Non-DNA function: fungal endemism with convergent enzyme activity across North America [21] [AB].
>
> This is a labelled non-DNA case and indirect for DNA profiles.
>

Not found in the cited text (where to look, not what is wrong): holds: american; holds: soil

## CB1/lime-requirement.13 (claim)

At a bulk density of 1 g/cm³ and 20 cm depth, 0.2–23.9 cmolc/kg converts one-for-one to t CaCO₃/ha: a two-order-of-magnitude range, which the reviewer calls the honest answer to "what is a typical rate."

- conf: not stated
- class: deriv (note: "converts one-for-one")
- holds: the reviewer's conversion at an assumed bulk density of 1 g/cm³ and 20 cm depth
- src: none (the reviewer's conversion of lime-requirement.12)
- trail: CB1-LIMING §1. Application rates

From the note:

> Their compiled incubation datasets span lime requirements of 0.2–23.9 cmolc/kg, which at a bulk density of 1 g/cm³ and 20 cm depth converts one-for-one to t CaCO₃/ha.
>
> That is a two-order-of-magnitude range, and it is the honest answer to "what is a typical rate."
>

## H1-02/gene-class-loss.4 (claim)

Against phylogenetically close RefSeq genomes (not the same strains), CRISPR arrays and transposases were depleted in MAGs above 90% completeness, while glycolysis genes were not.

- conf: not stated
- class: meas (note: "measured; natural")
- holds: reference genomes not the same strains
- src: miseUnexpectedAbsenceRibosomal2022
- trail: H1-02 §2.2

From the note:

> Against phylogenetically close RefSeq genomes (not the same strains), CRISPR arrays and transposases were depleted in MAGs above 90% completeness, while glycolysis genes were not (measured; natural).
>

## H1-06/uncontrolled-rank-studies.2 (claim)

At 160 natural sites in southwest France, habitat category explained little composition variance at any level, and it peaked at class (PERMANOVA R2: phylum 3.7%, class 6.3%, ASV 2.7%).

- conf: not stated
- class: not stated
- holds: natural sites, gyrB taxonomy, preprint; group numbers not controlled
- src: mayjonadeRelativeEffectsAbiotic2024 (preprint)
- trail: H1-06 §4. Part B, §answers

From the note:

> **Uncontrolled studies across ranks.** At 160 natural sites in southwest France (gyrB taxonomy, preprint) [24], habitat category explained little composition variance at any level.
>
> It peaked at class (PERMANOVA R2: phylum 3.7%, class 6.3%, ASV 2.7%).
>
> Uncontrolled studies agree in part and conflict in part: habitat R2 peaked at class and physicochemical associations were most frequent at phylum (Mayjonade 2024 preprint, gyrB taxonomy); 97% OTUs explained more composition variance than ASVs (Bay 2020); a pH-aligned composition axis stayed stable across ranks (Chakraverti-Wuerthwein 2026 preprint); seasonal niches were absent at class level (Auladell 2022, time series, not a spatial environment gradient).
>

## H1-05/averaging.9 (claim)

Between the bioRxiv 2024 and Cell Systems 2025 versions, the title changed and the second confound was renamed from "bias toward environment-independent beneficial functions" to correlations between functions and taxonomic abundances handled by an "extended null model"; the abstract conclusions are otherwise consistent, and the published body was not reached.

- conf: not stated
- class: not stated
- holds: [29], [30]; abstracts and a fetch summary of the preprint
- src: hoChallengesInterpretingFunctional2025, hoChallengesQuantifyingFunctional2024
- trail: H1-05 §3.2, §4, §answers

From the note:

> Between versions, the second confound was renamed from "bias toward environment-independent beneficial functions" to correlations between functions and taxonomic abundances handled by an "extended null model".
>
> The published body was not reached.
>
> | Ho and Huang [29][30] | bioRxiv 2024 to Cell Systems 2025 | Title changed; second confound reworded; abstract conclusions otherwise consistent; body not compared |
>
> How the published Cell Systems 'extended null model' differs in body text from the preprint (not reached)..
>

## NFERT/free-living-fixation.2 (claim)

Their support for a reduced fertiliser requirement is indirect: the fixed quantities are rarely large enough to displace a defined fertiliser rate at constant yield.

- conf: not stated
- class: not stated
- holds: cereal systems, constant yield
- src: ladhaBiologicalNitrogenFixation2022 (INDIRECT)
- trail: NFERT §The weak channel, §Verdicts

From the note:

> Their support for a reduced requirement is INDIRECT: the fixed quantities are rarely large enough to displace a defined fertiliser rate at constant yield.
>
> The inoculant evidence measures yield gain rather than input reduction at constant yield (INDIRECT; Schütz et al. 2018), free-living fixation is modest (INDIRECT; Ladha et al. 2022), and mineralisation rarely meets high-yield demand (St. Luce et al. 2011).
>

Not found in the cited text (where to look, not what is wrong): holds: cereal

## CB3/dns.6 (do not say)

"The 13–21% range for AFOLU reflects statistical uncertainty."

- why: the note: the spread is not statistical noise but two different CO2 accounting methods
- instead: afolu.2, co2-accounting.1
- trail: CB3-AG-EMISSIONS §Boundary B

From the note:

> The spread is not statistical noise — it is two different CO2 accounting methods: 11.9 ± 4.4 GtCO2eq of a total 55.9 ± 6.1 GtCO2eq gives 21% using bookkeeping models for the CO2 component, but "When using FAOSTAT/NGHGIs CO2 flux data, then the contribution of AFOLU to total emissions amounts to 13% of global emissions" [1, §7.2.1].
>

Not found in the cited text (where to look, not what is wrong): "The 13-21% range for AFOLU reflects statistical uncertainty."

## CB1/consumption.3 (claim)

About 1% of 1.5 billion tonnes is arithmetically about 15 Mt.

- conf: not stated
- class: deriv (note: "arithmetically")
- holds: the reviewer's arithmetic on the USGS share
- src: none (the reviewer's arithmetic)
- trail: CB1-LIMING §2. Consumption

From the note:

> USGS reports that about 1% of the 1.5 billion tonnes of crushed stone produced in the US in 2024 went to agricultural uses [3], which is arithmetically about 15 Mt — and earlier editions put the share at 2%.
>

## CB1/measured-emissions.3 (claim)

Rousset et al., applying two carbonate liming products to an acidic sandy loam under winter rye, found soil pH rose from 5.7 to about 7.0, yield rose from 320 to over 400 g/m², and soil CO₂ emissions fell by approximately 40% for both materials; they conclude that "the IPCC principles, predicting increased CO₂ emissions from lime-derived C, may need to be re-examined in the future."

- conf: not stated
- class: meas (note: "field study")
- holds: an acidic sandy loam under winter rye, over one rye growing period
- src: roussetSurprisingMinimisationCO22024 (abstract or structured summary only)
- trail: CB1-LIMING §5. Where the numbers, §6. What is well established

From the note:

> Rousset et al., applying two carbonate liming products to an acidic sandy loam under winter rye, found soil pH rose from 5.7 to about 7.0, yield rose from 320 to over 400 g/m², and soil CO₂ emissions *fell* by approximately 40% for both materials; they conclude that "the IPCC principles, predicting increased CO₂ emissions from lime-derived C, may need to be re-examined in the future" [13].
>
> Poorly constrained: the actual emission factor, which measured values put anywhere from 0.026 to 0.12 Mg C/Mg [1, 5, 12], with at least one field study finding a net *reduction* in soil CO₂ after liming [13].
>
> **Read as abstract or structured summary only**: Wang et al. (2021) [11]; Cho et al. (2019) [12]; Rousset et al. (2024) [13]; Silva et al. (2025) [14]; Holland et al. (2018) [15]; Aramburu Merlos et al. (2023), where I read the full text but used only its framing [16]; Li et al. (2024), where numbers came from an automated extraction of the full article rather than a line-by-line read [17].
>

## H2-01/genome-size.1 (claim)

Relative (sum-to-one) normalisation introduces a sample-level factor shared by all genes.

- conf: not stated
- class: not stated
- holds: relatively normalised functional profiles
- src: none (the note cites no source for this sentence)
- trail: H2-01 §2.3

From the note:

> - **Normalisation and genome size.** Relative (sum-to-one) normalisation introduces a sample-level factor shared by all genes.
>

## NFERT/inoculants.1 (claim)

Microbial inoculants raise yield inconsistently: the largest meta-analysis, spanning 171 field studies, found yield responses of +8.5% in continental climates, +10.0% in oceanic, +14.9% in tropical and +20.0% in dry climates, with effects described as often inconsistent and dependent on soil phosphorus and climate.

- conf: not stated
- class: not stated
- holds: 171 field studies, by climate
- src: schutzImprovingCropYield2018
- trail: NFERT §The weak channel

From the note:

> Microbial inoculants raise yield inconsistently.
>
> The largest meta-analysis, spanning 171 field studies, found yield responses of +8.5% in continental climates, +10.0% in oceanic, +14.9% in tropical, and +20.0% in dry climates, with effects described as often inconsistent and dependent on soil phosphorus and climate (Schütz et al. 2018).
>

## 16S/ploidy.8 (claim)

Copy number does not always fall in stationary phase: Azotobacter vinelandii is reported to rise from about 4 copies in exponential phase to about 80 in stationary phase, and M. acetivorans from 2.5 to 5 (Bruck 2023 full text, secondary via the critic); Pecoraro 2011 Table 5 gives A. vinelandii as 1 (up to 8) copies in slow growth and 40 in fast growth, attributed to another laboratory.

- conf: not stated
- class: not stated
- holds: cultures; reported by the critic from full texts the review did not use (Bruck 2023 labelled AB, Pecoraro Table 5 not reported)
- src: bruckOneAdvantageBeing2023 (AB), pecoraroQuantificationPloidyProteobacteria2011 (FT)
- trail: MB-02 §critic, §Adversarial

From the note:

> Most Soppa-group species fall in stationary phase or starvation.
>
> The soil diazotroph Azotobacter vinelandii, however, is reported to rise from about 4 copies in exponential phase to about 80 in stationary phase (SECONDARY, via Bruck et al. 2023 full text).
>
> Pecoraro et al. 2011 Table 5 [FT] gives A. vinelandii as 1 (up to 8) copies in slow growth and 40 in fast growth, attributed to another laboratory.
>
> Bruck 2023, open in PMC but labelled abstract only, reports A. vinelandii rising from 4 to 80 copies from exponential to stationary phase, against the review's 'copies usually fall' framing.
>
> - Bruck et al. 2023 [18] is open in PMC (PMC10536925) but labelled AB.
>
> Its full text reports that A. vinelandii and M. acetivorans carry more chromosomes in stationary than in exponential phase (4 versus 80; 2.5 versus 5).
>
> That contradicts the review's framing and was missed.
>
> - D1(b): the review reports down-regulation of ploidy in stationary phase and starvation in detail.
>
> Contrary cases, ploidy rising in stationary phase (A. vinelandii; M. acetivorans in slow growth), are omitted, though they appear in a source read in full (Pecoraro Table 5) and in an open full text (Bruck 2023).
>

Not found in the cited text (where to look, not what is wrong): holds: cultures

## CB2/dns.6 (do not say)

Fan et al.'s adequate recovery generalised to Illumina-length reads in a complex environment.

- why: the note: "I would not generalise it to Illumina-length reads in a complex environment, and no later work I found does"
- instead: targeted-reconstruction.7
- trail: CB2-RRNA §4. Bounding facts

From the note:

> Read length there was ~350 nt and the community was low-complexity relative to soil; I would not generalise it to Illumina-length reads in a complex environment, and no later work I found does.
>

## H2-04/within-between-partition.1 (claim)

Species trait covariation split into among-community and within-community components shows strong among-community covariation and weak within-community covariation in California woody plants.

- conf: not stated
- class: not stated
- holds: California woody plants; non-microbial; species traits
- src: ackerlyTraitbasedApproachCommunity2007 (abstract)
- trail: H2-04 §Within-unit versus between-unit, §answers, §critic

From the note:

> (4) Trait-ecology analogues (labelled non-microbial): species trait covariation split into among-community and within-community components, with strong among-community covariation and weak within-community covariation in California woody plants [1, abstract], and in grasslands 92 to 98% of trait variance within communities, a sign reversal of the SLA and specific root length correlation between the two components, and phylogenetic signal in within-community components only [16, full text, rechecked].
>
> The plant partitions (Ackerly & Cornwell abstract; Kembel & Cahill full text, 92 to 98% within communities) are non-microbial and concern species traits.
>
> (ii) Within-community versus among-community components: Kembel & Cahill (full text) and Ackerly & Cornwell (abstract).
>

## GHOST/missingness-degradation.5 (claim)

At 99% missing on Cora, GCNMF reaches 34.54% accuracy; GCNMF is the strategy that fails badly under high missingness.

- conf: repl (note: "confirmed by two independent papers")
- class: not stated
- holds: Cora, 99% missing; homophilous + sparse + MCAR
- src: rossiUnreasonableEffectivenessFeature2022, leiSelfsupervisedGuidedHypergraph2023
- rating: "Confidence: high (3-0 / 2-1)"
- trail: GHOST §2. Degradation, §1. Strategies

From the note:

> - Contrast at 99% missing on Cora: propagation ~78–79% vs **GCNMF 34.54%** — the latter confirmed by two independent papers [R1, R2].
>
> This is the strategy that fails badly under high missingness (below).
>
> *Confidence: high (3-0 / 2-1).*
>
> **Caveat carried on every number above:** homophilous + sparse + MCAR, and mostly author-reported.
>

## 16S/read-depth.1 (claim)

The Earth Microbiome Project averaged 80,000 sequences per sample over 27,751 samples and rarefied to 5,000; in four environments, mean prevalence of tag sequences rose with depth up to 50,000, so 5,000 under-estimated prevalence.

- conf: not stated
- class: not stated
- holds: EMP
- src: thompsonCommunalCatalogueReveals2017
- trail: MB-01 §3.3, §answers

From the note:

> **Large survey.** The EMP averaged 80,000 sequences per sample over 27,751 samples and rarefied to 5,000 (Thompson 2017).
>
> In four environments, mean prevalence of tag sequences rose with depth up to 50,000, so 5,000 under-estimated prevalence.
>
> Reads per sample.
>
> The EMP averaged 80,000 per sample over 27,751 samples (Thompson 2017).
>

Not found in the cited text (where to look, not what is wrong): Earth; Microbiome; Project

## H1-06/ph-preference.3 (claim)

Correlogram Moran's I for pH preference stayed below 0.25 at every depth, shallow ones included.

- conf: single (critic: C-001)
- class: meas (critic: C-001)
- holds: the same five datasets; natural systems
- src: ramonedaBuildingGenomebasedUnderstanding2023
- trail: H1-06 §2. Part A1, §answers, §critic

From the note:

> Correlogram Moran's I stayed below 0.25 at every depth, shallow ones included.
>
> Natural-system field evidence (Ramoneda 2023, SILVA 138, 16S trees) gives weak signal for pH preference (Pagel's lambda 0.22 to 0.78, Moran's I < 0.25 at all depths), while a preprint (Chakraverti-Wuerthwein 2026) reports strong phylogenetic signal in the loadings of the pH-aligned canonical axis of global topsoil composition.
>
> **Reformulated verdict:** A1 (environmental preferences): natural systems, measured for pH only, SINGLE SOURCE (Ramoneda et al. 2023).
>
> Signal is significant in 4 of 5 datasets but weak (Pagel's lambda 0.22 to 0.78, Moran's I < 0.25 at all depths), there is no consenTRAIT-style depth, and families span 3.7 to 4.2 pH units.
>
> Checks against sources: Ramoneda's lambda, Moran's I, the phylum quote, R2 = 0.21 / MAE 0.93, 6 to 24% GTDB matches and ~35% MAG/SAG all verified.
>

## CB1/ghg-balance.1 (claim)

Wang et al., meta-analysing 1,570 observations from 121 field studies, find that liming raises crop yield by 36.3%, increases SOC stocks by 4.51% annually, and cuts soil N₂O by 21.3% and paddy CH₄ by 19.0%, giving a global GHG benefit of 633–749 Tg CO₂-eq/yr, offset by 624–656 Tg CO₂/yr from mining, transport, application and dissolution, so that "the overall GHG balance is likely neutral."

- conf: not stated
- class: not stated
- holds: 1,570 observations from 121 field studies, scaled globally
- src: wangPotentialBenefitsLiming2021 (abstract or structured summary only)
- trail: CB1-LIMING §5. Where the numbers

From the note:

> **The whole-system balance is disputed, and the disagreement is large.** Wang et al., meta-analysing 1,570 observations from 121 field studies, find liming raises crop yield by 36.3%, increases SOC stocks by 4.51% annually, cuts soil N₂O by 21.3% and paddy CH₄ by 19.0%, giving a global GHG benefit of 633–749 Tg CO₂-eq/yr — offset by 624–656 Tg CO₂/yr from mining, transport, application and dissolution, so that "the overall GHG balance is likely neutral" [11].
>
> **Read as abstract or structured summary only**: Wang et al. (2021) [11]; Cho et al. (2019) [12]; Rousset et al. (2024) [13]; Silva et al. (2025) [14]; Holland et al. (2018) [15]; Aramburu Merlos et al. (2023), where I read the full text but used only its framing [16]; Li et al. (2024), where numbers came from an automated extraction of the full article rather than a line-by-line read [17].
>

## H1-RES/pangenome.3 (claim)

Multiple studies across phylogenetically diverse bacteria and fungi have corroborated substantial accessory fractions and open pangenomes.

- conf: not stated
- class: not stated
- holds: the studies the section goes on to list
- src: none (the reviewer's synthesis)
- trail: H1-RES §Confirming Evidence Across

From the note:

> Multiple studies across phylogenetically diverse bacteria and fungi have corroborated substantial accessory fractions and open pangenomes.
>

## H1-RES/pangenome.5 (claim)

In *Escherichia coli*, pangenome analyses have consistently documented large accessory fractions: one study of 2,377 complete genomes identified 2,398 core genes and 5,182 accessory genes, and another of 1,324 genomes estimated the pangenome at approximately 25,000 gene families with a stable softcore of approximately 3,000 gene families.

- conf: repl (note: "consistently documented")
- class: not stated
- holds: *E. coli*; 2,377 complete genomes and 1,324 genomes
- src: none (cited only as SC1 [14] and [35]; the note gives no reference list)
- trail: H1-RES §Confirming Evidence Across

From the note:

> In *Escherichia coli*, pangenome analyses have consistently documented large accessory fractions: one study of 2,377 complete genomes identified 2,398 core genes and 5,182 accessory genes [14], while another analysis of 1,324 genomes estimated the pangenome at approximately 25,000 gene families with a stable softcore of approximately 3,000 gene families [35].
>

## H1-06/uncontrolled-rank-studies.8 (claim)

In an 11-year coastal time series, seasonal niches were coherent for some genera and families, but classes (Alphaproteobacteria, Gammaproteobacteria, Bacteroidia) were non-seasonal when aggregated.

- conf: not stated
- class: not stated
- holds: a time series, not a spatial environment gradient; aggregation used random 80% ASV subsets, but group number was not equalised
- src: auladellSeasonalNicheDifferentiation2021
- trail: H1-06 §4. Part B, §answers

From the note:

> In an 11-year coastal time series [28], seasonal niches were coherent for some genera and families, but classes (Alphaproteobacteria, Gammaproteobacteria, Bacteroidia) were non-seasonal when aggregated; within at least three genera, niche similarity fell with 16S divergence.
>
> Aggregation used random 80% ASV subsets, but group number was not equalised.
>
> Uncontrolled studies agree in part and conflict in part: habitat R2 peaked at class and physicochemical associations were most frequent at phylum (Mayjonade 2024 preprint, gyrB taxonomy); 97% OTUs explained more composition variance than ASVs (Bay 2020); a pH-aligned composition axis stayed stable across ranks (Chakraverti-Wuerthwein 2026 preprint); seasonal niches were absent at class level (Auladell 2022, time series, not a spatial environment gradient).
>

## 16S/pcr.6 (claim)

In a gut-isolate mock with primer mismatch removed by pre-amplification, log-ratios changed linearly with cycle number from 10 to 35 cycles; after 35 cycles relative abundances were biased by an average factor of 2.6 (95% credible set 2.3 to 2.9), and the B. longum to E. faecalis ratio shifted about 16-fold.

- conf: single (marker)
- class: meas (marker)
- holds: one gut-isolate mock, 10 to 35 cycles, primer mismatch removed; the per-cycle bias magnitude rests on this study alone
- src: silvermanMeasuringMitigatingPCR2021 (FT; meas; single)
- trail: MB-01 §2.4, §answers, §critic

From the note:

> **Magnitude per cycle.** In a gut-isolate mock with primer mismatch removed by pre-amplification, log-ratios changed linearly with cycle number from 10 to 35 cycles (Silverman 2021) [FT; meas; single].
>
> After 35 cycles relative abundances were biased by an average factor of 2.6 (95% credible set 2.3 to 2.9), and the B. longum to E. faecalis ratio shifted about 16-fold.
>
> RA: with primer mismatch removed, bias averaged a factor of 2.6 per taxon after 35 cycles in a gut mock.
>
> Bias grew log-linearly with cycle number.
>
> | PCR, cycles | Average 2.6-fold per taxon at 35 cycles.
>
> The per-cycle PCR bias magnitude rests on Silverman 2021 alone.
>
> Verified against full text: McLaren 2019 per-step bias table (36.6 and 29.3 max, 5.5 and 5.6 mean), Silverman 2021 (2.6-fold, about 19% of taxa more than 4-fold, mis-set annealing machine), Sze and Schloss 2019 (R2 0.79, 0.044, 0.033; chimera rates 0.9 to 18.2%), Schloss 2024b (Table 1 read ranges, coverage-based iNEXT passage, Good's coverage 89.4 to 99.8%), Karstens 2019, Fitzpatrick 2018, Thompson 2017, Song 2016, Starke 2021, Louca 2018, Laursen 2017, Wen 2017, Weiss 2017, Nearing 2018 and 2022, Wirbel 2024, Zemb 2020, Glassman 2018, Chiarello 2022, Stoddard 2015, Vetrovsky 2013, Kembel 2012, Hornung 2019, Lennon 2018, Barlow 2020 and Dyrhovden 2021.
>

## CB3/dns.2 (do not say)

"Agricultural soils produce 5% of global greenhouse gas emissions."

- why: the note's verdict: no boundary produces five per cent for agricultural soils; published estimates range from about 1.5% to 4.1%
- instead: soils.8, five-percent.3
- trail: CB3-AG-EMISSIONS §Verdict

From the note:

> **No boundary in the current authoritative literature produces five per cent for agriculture, and none produces it for agricultural soils.**
>
> The review's honest statement of the evidence: published estimates of N₂O from agricultural soils as a share of global GHG range from about **1.5% to 4.1%**, depending on the category, database and metric.
>

Not found in the cited text (where to look, not what is wrong): "Agricultural soils produce 5% of global greenhouse gas emissions."

## H1-05/dns.5 (do not say)

"Functional similarity exceeded taxonomic similarity at SEED levels 1 and 2, so the gap widens as functions are aggregated."

- why: that the gap widens is the reviewer's inference from [3] alone, phrased as a finding; Chen states only that the ordering held at all levels
- instead: functional-unit.2
- trail: H1-05 §critic, §Adversarial critique

From the note:

> Functional similarity exceeded taxonomic similarity at SEED levels 1 and 2 against all five taxonomic ranks, so the gap widens as functions are aggregated.
>
> That the 'gap widens' with aggregation is the reviewer's inference, not a result the authors state.
>
> (5) In D2, 'the gap widens as functions are aggregated' is an inference.
>
> Chen states only that the ordering held at all levels.
>
> - D2: 'the gap widens as functions are aggregated' rests on [3] alone, is the reviewer's inference (Chen states only that function had higher similarity at Levels 1 and 2 against all five ranks), and is phrased as a finding.
>

Not found in the cited text (where to look, not what is wrong): "Functional similarity exceeded taxonomic similarity at SEED levels 1 and 2, so the gap widens as functions are aggregated."

## H1-02/bounding-comparisons.7 (claim)

These bounds are coarse (genome size, ANI, per-OTU annotation overlap) and do not contradict the gene-level losses in Meziti et al., which fall on variable and mobile genes that length and ANI do not register.

- conf: not stated
- class: reading (note: "Reviewer's reading")
- holds: the bounding comparisons above; the critic: correctly labelled, but used to discount the bounding evidence in favour of Meziti et al. without a source saying so
- src: none (the reviewer's synthesis)
- trail: H1-02 §2.6, §Adversarial critique

From the note:

> Reviewer's reading: these bounds are coarse (genome size, ANI, per-OTU annotation overlap) and do not contradict the gene-level losses in [1], which fall on variable and mobile genes that length and ANI do not register.
>
> - 'Reviewer's reading: these bounds are coarse ... and do not contradict the gene-level losses' is correctly labelled. But it is used to discount the bounding evidence in favour of [1] without a source saying so.
>

Not found in the cited text (where to look, not what is wrong): Meziti; holds: meziti

