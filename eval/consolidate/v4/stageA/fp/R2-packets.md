# False-positive sample, R2: 30 of 846 (seed 20261023)

## H2-01 transfer-dependencies.1 (claim)

There is no direct conflict on the same quantity: reproduction is high in some tests (Subramanian 81%; Chen reductive TCA 94.7%) and low in others (Cleary cross-type drop; pooled networks in Pierson; sign reversals across scales in plant traits).

- conf: not stated
- class: not stated
- holds: tests of different quantities in different fields
- src: subramanianNextGenerationConnectivity2017 (FT), chenGutMicrobialCoabundance2020 (FT), clearyEfficientGenerationTranscriptomic2017 (FT), piersonSharingSpecificityCoexpression2015 (FT), andereggWithinspeciesPatternsChallenge2018 (AB)
- trail: H2-01 §answers

**Lint could not find:** quantities fields (also flagged by: content, setting)

Cited text (`from` and named critique):

> *Conflicts:* No direct conflict on the same quantity.
>
> Reproduction is high in some tests (Subramanian 81%; Chen reductive TCA 94.7%) and low in others (Cleary cross-type drop; pooled networks in Pierson; sign reversals across scales in plant traits [Anderegg2018]); the differences track how different the target is from the training data..
>

## GHOST low-variance-defect.2 (claim)

The low-variance defect bounds, but does not refute, propagation: the high-variance channels do the work.

- conf: not stated
- class: not stated
- holds: the review's reading of R5 and R6
- src: none (the reviewer's synthesis)
- trail: GHOST §5. Bounding

**Lint could not find:** review reading r5 r6 (also flagged by: content, setting)

Cited text (`from` and named critique):

> Bounds, does not refute, the strategy: the high-variance channels do the work.
>

## 16S ploidy.3 (claim)

Monoploid examples: Caulobacter crescentus (about 2.1 genome-equivalents at a mid-chromosome locus at 93 min doubling, consistent with one chromosome plus replication), Wolinella succinogenes (about 0.9 at 96 min) and six crenarchaeal species of four genera.

- conf: not stated
- class: meas (note: "All figures below are measured")
- holds: cultures; Pecoraro 2011 full text (checked by the critic), Hildenbrand 2011 abstract only
- src: pecoraroQuantificationPloidyProteobacteria2011 (FT), hildenbrandGenomeCopyNumbers2011 (AB)
- trail: MB-02 §D1.3, §answers, §critic

**Lint could not find:** cultures text checked critic hildenbrand abstract (also flagged by: content, setting)

Cited text (`from` and named critique):

> All figures below are measured.
>
> | Caulobacter crescentus | doubling 93 min | 2.1 at mid-chromosome locus, read as monoploid | [11, FT] |
>
> | Wolinella succinogenes | doubling 96 min | 0.9, monoploid | [11, FT] |
>
> | Six crenarchaeal species (4 genera) | compiled | all monoploid | [15, AB] |
>
> Monoploid examples: Caulobacter crescentus (about 2.1 genome-equivalents at a mid-chromosome locus, consistent with one chromosome plus replication) and Wolinella succinogenes (about 0.9) [11]; six crenarchaeal species of four genera were monoploid [15].
>
> These all matched: Pecoraro 2011 (E. coli 6.8/2.5 origins, P. putida 20/14, Caulobacter 2.1, Wolinella 0.9), Louca 2018 (15%/30% autocorrelation, 49% of SILVA OTUs, 635 communities including soil), Gao and Wu 2023 (0.96 precision, 20%/31%, 13% to 65%), Kembel 2012 (r 0.70 to 0.81, K = 0.48), Vetrovsky 2013 (mean 4.2, 15%/21%, Acidobacteria 50.1% to 66.0%), Bickel and Or 2021 (0.4%, 0.019%, prevalence 0.3 vs 0.001), Jia 2022 (61.59/45.65/28.36%, ASV counts), Custer 2023 (1.21 to 9.42%), Pascoal 2025 (181 articles, 37%, 84%, V4V5 versus full-length reversal) and Stopnisek and Shade 2021 (48 taxa, 13.7%, rarefied to 31,255 reads).
>

## H2-01 other-field-transfer.1 (claim)

Sparse module dictionaries learned on 5% of samples recovered expression of the same TCGA tumour type at about 87% (Spearman, SMAF), and a dictionary from a different tumour type gave 68% on average, related tumour types doing better; this is recovery of expression from 25 random composite measurements through a learned dictionary (compressed sensing), not a direct covariance-reproduction score.

- conf: single (marker)
- class: meas (marker)
- holds: TCGA tumour types (other field); simulated random composite measurements, m = 25, g = 5,000; the only other-field test found that withholds a biologically distinct group (the closest analogue of a habitat)
- src: clearyEfficientGenerationTranscriptomic2017 (FT; measured; SINGLE SOURCE)
- trail: H2-01 §3.4, §critic, §answers

**Lint could not find:** found (also flagged by: content)

Cited text (`from` and named critique):

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

## H2-01 shared-mean.5 (claim)

Whether a dimension estimate is taken before or after centring on the mean profile will change it.

- conf: not stated
- class: not stated
- holds: dimension estimates of functional profiles
- src: none (the reviewer's statement)
- trail: H2-01 §2.2

**Lint could not find:** estimates functional profiles (also flagged by: content)

Cited text (`from` and named critique):

> Whether a dimension estimate is taken before or after centring on this mean will change it.
>

## H1-05 averaging.6 (claim)

In HMP stool, apparent functional selection disappeared under restricted shuffles, so it was artifactual.

- conf: not stated
- class: not stated
- holds: HMP stool data [29][30]
- src: hoChallengesInterpretingFunctional2025, hoChallengesQuantifyingFunctional2024
- trail: H1-05 §3.2, §answers

**Lint could not find:** data (also flagged by: content)

Cited text (`from` and named critique):

> - HMP stool: apparent selection disappeared under restricted shuffles.
>
> Other habitats: the same null found no functional selection in bromeliad communities (reanalysing [33]) and found apparent selection in HMP stool to be artifactual under restricted shuffles [29][30].
>

## CB1 dissolution-pathway.4 (claim)

Liming is carbon negative where dissolution is driven by carbonic acid and the bicarbonate is exported to groundwater and rivers, and carbon positive where strong acids, chiefly nitric acid from nitrification of fertiliser N, do the dissolving; the sign of the flux is a function of nitrogen management and hydrology, not a property of the lime.

- conf: not stated
- class: not stated
- holds: the reviewer's statement of Hamilton et al.'s condition (dissolution-pathway.3)
- src: hamiltonEvidenceCarbonSequestration2007
- trail: CB1-LIMING §5. Where the numbers

**Lint could not find:** reviewer statement hamilton et al dissolution-pathway.3 (also flagged by: content, setting)

Cited text (`from` and named critique):

> The condition is explicit and mechanistic: "As nitrate concentrations increased in infiltrating waters, lime switched from a net CO₂ sink to a source, implying nitrification as a major acidifying process" [6].
>
> Liming is carbon negative where dissolution is driven by carbonic acid and the bicarbonate is exported to groundwater and rivers; it is carbon positive where strong acids, chiefly nitric acid from nitrification of fertiliser N, do the dissolving.
>
> That makes the sign of the flux a function of nitrogen management and hydrology, not a property of the lime.
>

## H2-01 genome-dimension.3 (claim)

Fahimipour2020 and Westoby2021 are not in conflict, because they describe different trait sets; together they bound any claim that "microbial function" has one dimensionality.

- conf: not stated
- class: not stated
- holds: genome-level trait sets
- src: none (the reviewer's statement)
- trail: H2-01 §2.4

**Lint could not find:** genome-level (also flagged by: content, setting)

Cited text (`from` and named critique):

> These two are not in conflict: they describe different trait sets.
>
> Together they bound any claim that "microbial function" has one dimensionality.
>

## H1-RES pangenome.26 (claim)

Free-living and soil-associated bacteria exhibit expanded pangenomes with high accessory content, indicating that environmental versatility requires maintaining large gene reservoirs.

- conf: not stated
- class: not stated
- holds: as pangenome.14
- src: none (cited only as SC1 [37]; the note gives no reference list)
- trail: H1-RES §Taxon-Dependence

**Lint could not find:** pangenome.14 (also flagged by: content, setting)

Cited text (`from` and named critique):

> However, free-living and soil-associated bacteria exhibit expanded pangenomes with high accessory content, indicating that environmental versatility requires maintaining large gene reservoirs [37].
>

## CB1 lime-resource.4 (claim)

USGS flags localised shortages near urban and industrialised areas driven by zoning and land-development competition, which push new quarries away from population centres and raise delivered prices: planning and land-use pressure, presented by USGS as a price driver, not a reserve limitation.

- conf: not stated
- class: not stated
- holds: urban and industrialised areas (US)
- src: willettStoneCrushed2025
- trail: CB1-LIMING §2. Consumption, §Verdict on the scarcity

**Lint could not find:** us (also flagged by: setting)

Cited text (`from` and named critique):

> USGS separately flags localised shortages near urban and industrialised areas driven by zoning and land-development competition, which pushes new quarries away from population centres and raises delivered prices — a siting and logistics problem, not a depletion problem [3].
>
> USGS notes shortages in urban and industrialised areas driven by zoning and land-development competition, pushing quarries further from demand [3] — that is planning and land-use pressure, and USGS presents it as a price driver, not a reserve limitation.
>

## H1-06 rankwise-structuring.10 (claim)

In soils, the observed genus-to-class R2 was significantly above the null.

- conf: not stated
- class: not stated
- holds: four surface soils
- src: luEvaluatingCommunityenvironmentRelationships2016
- trail: H1-06 §4. Part B, §answers, §critic
- limit: access (critic: C-017)

**Lint could not find:** four surface (also flagged by: content)

Cited text (`from` and named critique):

> In soils the observed genus-to-class R2 was significantly above the null.
>
> A topology-preserving shuffle null gave constant or slightly falling R2, and in soils the observed genus-to-class R2 was significantly above that null.
>
> I could not obtain the Methods and Results (nature.com paywall; PMC5148199 is not open access), so the null-model description and the soil class-peak details rest on the search agent's reading.
>

## TSL information-content.1 (claim)

Information content IC(c) = −log P(c) in an is-a taxonomy (Resnik 1995/1999): general concepts have high P and low IC (root P = 1, IC = 0); specific concepts have low P and high IC.

- conf: not stated
- class: not stated
- holds: is-a taxonomies with corpus probabilities
- src: resnikUsingInformationContent1995, resnikSemanticSimilarityTaxonomy1999
- trail: TSL §Verdict, §1. Specificity signals
- rating: "Confidence: high (3-0)"

**Lint could not find:** taxonomies probabilities (also flagged by: content)

Cited text (`from` and named critique):

> The strongest, most direct primary evidence establishes two foundational, mutually consistent signals: **collection df / idf** (lower df = more specific) [S1] and **information content IC(c) = −log P(c)** in an is-a taxonomy, where corpus probability is monotonic up the hierarchy so altitude maps directly onto generality [S2].
>
> - **Information content IC(c) = −log P(c)** [S2] — Resnik (1995/1999): general concepts have high P, low IC (root P=1, IC=0); specific concepts low P, high IC.
>
> *Confidence: high (3-0).* Caveat: needs a unified root; WordNet has none naturally.
>

## 16S copy-number.6 (claim)

In the reviewer's summary of the rrnDB release files, bacterial records and ranges were: v3.1.227, 1,297 records, 1 to 15, record mean 4.20 (median 3), 17.5% of records at one copy, mean of species means 3.87, archaea 1 to 4 (species mean 1.66); v4.4.3, 2,700, 1 to 15, 4.20 (4), 15.6%, 3.92, archaea 1 to 4 (1.66); v5.0, 5,856, 1 to 16, 4.60 (4), 13.3%, 4.04, archaea 1 to 4 (1.72); v5.6, 15,462, 1 to 21, 5.04 (5), 9.3%, 4.26, archaea 1 to 5 (1.66); v5.10, 48,053, 1 to 22, 5.52 (6), 7.5%, 4.36, archaea 1 to 5 (1.73).

- conf: not stated
- class: deriv (note: "derived by the reviewer")
- holds: release files downloaded and summarised by the reviewer (v5.10 dated June 2025, 48,077 bacterial and 623 archaeal records per the home page); species grouped by the first two words of the NCBI name, which is approximate
- src: schmidtlaboratoryRrnDBReleaseFiles (FT; statistics derived by reviewer)
- trail: MB-02 §D1.1, §Search record

**Lint could not find:** dated (also flagged by: content)

Cited text (`from` and named critique):

> I downloaded the release files for v3.1.227, v4.4.3, v5.0, v5.6 and v5.10 (June 2025, the current release; 48,077 bacterial and 623 archaeal records per the home page) and summarised them [4].
>
> These figures are **derived by the reviewer** from the database.
>
> Species were grouped by the first two words of the NCBI name, which is approximate.
>
> | Release | Bacterial records | Range | Record mean (median) | Share of records at 1 copy | Mean of species means | Archaeal range | Archaeal species mean |
>
> | 3.1.227 | 1,297 | 1 to 15 | 4.20 (3) | 17.5% | 3.87 | 1 to 4 | 1.66 |
>
> | 4.4.3 | 2,700 | 1 to 15 | 4.20 (4) | 15.6% | 3.92 | 1 to 4 | 1.66 |
>
> | 5.0 | 5,856 | 1 to 16 | 4.60 (4) | 13.3% | 4.04 | 1 to 4 | 1.72 |
>
> | 5.6 | 15,462 | 1 to 21 | 5.04 (5) | 9.3% | 4.26 | 1 to 5 | 1.66 |
>
> | 5.10 | 48,053 | 1 to 22 | 5.52 (6) | 7.5% | 4.36 | 1 to 5 | 1.73 |
>
> - The rrnDB statistics are the reviewer's own computation from the release files.
>
> Species grouping was by the first two words of the NCBI name.
>

## H1-05 non-dna-function.1 (claim)

Across North America, soil fungi showed endemism with convergent enzyme activity; this is a non-DNA case and indirect for DNA profiles.

- conf: not stated
- class: not stated
- holds: North American soil mycobiome [21]; enzyme activity
- src: talbotEndemismFunctionalConvergence2014 (AB)
- trail: H1-05 §1.2

**Lint could not find:** american soil mycobiome (also flagged by: content, setting)

Cited text (`from` and named critique):

> - Non-DNA function: fungal endemism with convergent enzyme activity across North America [21] [AB].
>
> This is a labelled non-DNA case and indirect for DNA profiles.
>

## 16S pcr.14 (claim)

In fungal ITS, pooling 1 to 16 PCR replicates had no detectable effect on alpha or beta diversity.

- conf: not stated
- class: meas (marker)
- holds: fungal ITS, labelled INDIRECT
- src: smithSequenceDepthNot2014 (FT; meas; INDIRECT)
- trail: MB-01 §2.4

**Lint could not find:** labelled (also flagged by: content)

Cited text (`from` and named critique):

> - In fungal ITS, pooling 1 to 16 PCR replicates had no detectable effect on alpha or beta diversity (Smith and Peay 2014) [FT; meas; INDIRECT].
>

## H1-06 uncontrolled-rank-studies.2 (claim)

At 160 natural sites in southwest France, habitat category explained little composition variance at any level, and it peaked at class (PERMANOVA R2: phylum 3.7%, class 6.3%, ASV 2.7%).

- conf: not stated
- class: not stated
- holds: natural sites, gyrB taxonomy, preprint; group numbers not controlled
- src: mayjonadeRelativeEffectsAbiotic2024 (preprint)
- trail: H1-06 §4. Part B, §answers

**Lint could not find:** group numbers controlled (also flagged by: content)

Cited text (`from` and named critique):

> **Uncontrolled studies across ranks.** At 160 natural sites in southwest France (gyrB taxonomy, preprint) [24], habitat category explained little composition variance at any level.
>
> It peaked at class (PERMANOVA R2: phylum 3.7%, class 6.3%, ASV 2.7%).
>
> Uncontrolled studies agree in part and conflict in part: habitat R2 peaked at class and physicochemical associations were most frequent at phylum (Mayjonade 2024 preprint, gyrB taxonomy); 97% OTUs explained more composition variance than ASVs (Bay 2020); a pH-aligned composition axis stayed stable across ranks (Chakraverti-Wuerthwein 2026 preprint); seasonal niches were absent at class level (Auladell 2022, time series, not a spatial environment gradient).
>

## H2-01 heldout-habitat.1 (claim)

No study was found that fitted covariation among microbial functions (a covariance or correlation matrix, a factorisation, a network, or a regression of some functions on others) in a set of habitats and scored it on a withheld habitat; this is a statement about the routes used, not that the literature lacks such a study.

- conf: not stated
- class: search (note: "No study was found that fitted covariation among functions")
- holds: three search angles via Europe PMC, PubMed and PMC E-utilities, Crossref, Semantic Scholar, OpenAlex, Unpaywall and known literature; WebSearch and Scholar Gateway unavailable; no test of function-function covariance (as opposed to taxon-to-function mappings or classifiers) across habitats either
- src: none (a search result)
- trail: H2-01 §3.1, §answers, §critic
- rating: "Absent for the withheld-habitat microbial case"

**Lint could not find:** either (also flagged by: )

Cited text (`from` and named critique):

> Answered per case: withheld habitat (microbial), withheld study within a habitat (microbial), other fields**: Withheld habitat, microbial functional covariation: not found.
>
> The three search angles used Europe PMC, PubMed and PMC E-utilities, Crossref, Semantic Scholar, OpenAlex, Unpaywall and known literature (WebSearch and Scholar Gateway unavailable).
>
> *Strength:* Absent for the withheld-habitat microbial case.
>
> *Not measured:* Any microbial test withholding a whole habitat.
>
> Any test of function-function covariance (as opposed to taxon-to-function mappings or classifiers) across habitats.
>
> **D2.** No held-out-habitat test of microbial functional covariation was found.
>
> Across three independent search angles, no study was found that estimated covariation among microbial functions in some habitats and scored it on a habitat left out of the estimate (search routes in the Search record).
>
> No study was found that fitted covariation among functions (a covariance or correlation matrix, a factorisation, a network, or a regression of some functions on others) in a set of habitats and scored it on a withheld habitat.
>
> The three search angles used Europe PMC, PubMed and PMC E-utilities, Crossref, Semantic Scholar, OpenAlex and known literature (see Search record); WebSearch and Scholar Gateway were unavailable.
>
> This is a statement about those routes, not a statement that the literature lacks such a study.
>
> Not found by these routes: any microbial test withholding a habitat when scoring functional covariation; any microbial cross-habitat comparison of covariation stability against level and composition stability; any microbial study of how dimension estimates change with normalisation, sparsity, presence/absence, overlapping gene sets or sample size; any study holding taxonomy fixed while habitat varies.
>
> - **D2**: Withheld habitat, microbial function-function covariation: none found on the routes named.
>

## H2-01 compositional-closure.1 (claim)

Correlation is not a valid association measure for relative data; proportionality is offered instead.

- conf: not stated
- class: not stated
- holds: relative data in general (other field)
- src: lovellProportionalityValidAlternative2015 (AB; other field)
- trail: H2-01 §2.3

**Lint could not find:** general (also flagged by: content, setting)

Cited text (`from` and named critique):

> - **Compositional closure.** Correlation is not a valid association measure for relative data; proportionality is offered instead [Lovell2015; AB; other field].
>
> What is measured is that these choices change across-sample variance and covariance: marker-gene normalisation raises pathway variability, and uniform mapping of shared KOs and KEGG aggregation lower it [Manor2017]; naive mapping inflates pathway counts [YeDoak2009]; relative data distort correlation [Lovell2015].
>

## H1-RES redundancy.9 (claim)

The soil redundancy evidence spans metagenomics, GeoChip, predictive functional profiling and experimental manipulations, and tends to emphasise broad metabolic categories or potential gene abundances rather than measured process rates; almost all of it concerns potential rather than measured process rates.

- conf: not stated
- class: not stated
- holds: the soil redundancy studies
- src: chenFunctionalRedundancySoil2022, chenAssessmentBacterialCommunities2016, mendesSoilBorneMicrobiomeLinking2015, chenStableSoilMicrobial2021, wuNonsynchronousStructuralFunctional2019
- trail: H1-RES §Soil redundancy evidence, §Assessment: redundancy

**Lint could not find:** soil redundancy studies (also flagged by: content, setting)

Cited text (`from` and named critique):

> - **Scope** Evidence spans metagenomics, GeoChip, predictive functional profiling, and experimental manipulations, and tends to emphasize broad metabolic categories or potential gene abundances rather than measured process rates [1] [4] [5] [6] [7].
>
> Two further qualifications come straight from the corpus.
>
> First, almost all of this evidence concerns *potential* (gene abundances, predicted KEGG categories) rather than measured process rates, which keeps it on the capacity side of the scope boundary and defers realised-function confirmation to the Aim 4 assays.
>

## TAXRES name-resolution.2 (claim)

Dedicated tools exist with established methods: TNRS (plant names; parsing, fuzzy matching and authority correction; thousands of names per run), Taxamatch (a near / fuzzy matching algorithm), GNverifier / Global Names, taxize `gnr_resolve` (with a `with_context` option to restrict to a taxonomic context and avoid cross-group homonyms), GBIF fuzzy matching (`TAXON_MATCH_FUZZY`), and Pytaxon (Python, GNV API and fuzzy matching).

- conf: not stated
- class: not stated
- holds: tools as found by a single-pass web search on 2026-06-19; no match-rate figures captured
- src: grenieHarmonizingTaxonNames2023, boyleTaxonomicNameResolution2013, silvaPytaxonPythonSoftware2025, ropensciGnrResolveGlobal
- trail: TAXRES §Taxon-name resolution

**Lint could not find:** found single-pass web match-rate figures captured (also flagged by: content, setting)

Cited text (`from` and named critique):

> Dedicated tools exist with established methods: **TNRS** (plant names, parsing + fuzzy + authority correction, thousands of names per run), **Taxamatch** (a near/fuzzy matching algorithm), **GNverifier / Global Names**, **`taxize` `gnr_resolve`** (with a `with_context` option to restrict to a taxonomic context and avoid cross-group homonyms), **GBIF fuzzy matching** (`TAXON_MATCH_FUZZY`), and **Pytaxon** (Python, GNV API + fuzzy).
>
> Searched 2026-06-19 across four angles: NCBI-vs-GTDB divergence, taxon-name resolution tools, GTDB structure/identifiers, and the GBIF/Catalogue-of-Life cross-kingdom backbone.
>

## H1-06 a1-environmental-preferences.9 (claim)

Without Ramoneda et al. 2023, the only natural-system depth evidence left for any environmental preference is a single preprint, and the A1 verdict would move towards 'not measured in this setting' for natural systems.

- conf: not stated
- class: not stated
- holds: the sensitivity of the A1 verdict to one source; the remaining preprint is Chakraverti-Wuerthwein 2026
- src: ramonedaBuildingGenomebasedUnderstanding2023, chakravertiwuerthweinPhylogeneticCoherenceMicrobiome2026
- trail: H1-06 §answers, §6. Verdicts

**Lint could not find:** sensitivity a1 remaining chakraverti-wuerthwein 2026 (also flagged by: content, setting)

Cited text (`from` and named critique):

> Would change if one source were removed: yes.
>
> Without Ramoneda et al. 2023, the only natural-system depth evidence left for any environmental preference is a single preprint, and the part would move towards 'not measured in this setting' for natural systems.
>
> Removing Ramoneda et al. 2023 [13] would leave one natural-system preprint [29], and the verdict would move towards "not measured in this setting" for natural systems.
>

## 16S technical-variation.7 (claim)

A PCR machine with a mis-set annealing temperature produced a batch outlier.

- conf: not stated
- class: not stated
- holds: Silverman 2021; checked by the critic
- src: silvermanMeasuringMitigatingPCR2021
- trail: MB-01 §4.3, §answers, §critic

**Lint could not find:** checked critic (also flagged by: content)

Cited text (`from` and named critique):

> - A PCR machine with a mis-set annealing temperature produced a batch outlier (Silverman 2021).
>
> Run and batch effects: whole-run taxon loss (Yeh 2018, single source); a mis-set PCR machine produced a batch outlier (Silverman 2021); between-laboratory effects (MBQC).
>
> Verified against full text: McLaren 2019 per-step bias table (36.6 and 29.3 max, 5.5 and 5.6 mean), Silverman 2021 (2.6-fold, about 19% of taxa more than 4-fold, mis-set annealing machine), Sze and Schloss 2019 (R2 0.79, 0.044, 0.033; chimera rates 0.9 to 18.2%), Schloss 2024b (Table 1 read ranges, coverage-based iNEXT passage, Good's coverage 89.4 to 99.8%), Karstens 2019, Fitzpatrick 2018, Thompson 2017, Song 2016, Starke 2021, Louca 2018, Laursen 2017, Wen 2017, Weiss 2017, Nearing 2018 and 2022, Wirbel 2024, Zemb 2020, Glassman 2018, Chiarello 2022, Stoddard 2015, Vetrovsky 2013, Kembel 2012, Hornung 2019, Lennon 2018, Barlow 2020 and Dyrhovden 2021.
>

## H1-06 ab-relation.1 (claim)

No source tests a correspondence between the rise in composition-environment R2 from otu97 to genus (natural systems) and the depths at which perturbation responses cluster (engineered).

- conf: not stated
- class: not stated
- holds: the critic's assessment of the review's 'Relation to Part A' reading
- src: luEvaluatingCommunityenvironmentRelationships2016, isobePhylogeneticConservationBacterial2019, isobePhylogeneticConservationSoil2020
- trail: H1-06 §critic

**Lint could not find:** critic assessment review (also flagged by: content, setting)

Cited text (`from` and named critique):

> - 'Relation to Part A (reviewer's reading)' links a natural-system composition result (Lu 2016, otu97-to-genus rise) to engineered perturbation-response depths (Isobe 2019, 2020, tau_D ~0.017, 'about genus'), which breaks Common rule 10's natural/engineered separation. It is labelled reviewer's reading, but it presents a correspondence the sources do not test.
>

## H2-04 plant-axis-analogues.6 (claim)

Three different partitions are involved and are kept apart: (i) species-level trade-offs versus community-mean axes (Bruelheide 2018); (ii) within-community versus among-community components (Kembel & Cahill, Ackerly & Cornwell); (iii) within-species versus across-species (Anderegg, Osnas, Puglielli). Evidence that cross-level structure can differ, and can reverse in sign, comes from (ii) and (iii), not from the species-versus-community-mean comparison D2 is closest to; for (i) the only evidence is a single abstract, and it reports agreement.

- conf: not stated
- class: not stated
- holds: plant trait ecology; the review rates the disagreement side as replicated across independent plant datasets, and the critic says that mixes partition types
- src: bruelheideGlobalTraitenvironmentRelationships2018, kembelIndependentEvolutionLeaf2011, ackerlyTraitbasedApproachCommunity2007, andereggWithinspeciesPatternsChallenge2018, osnasDivergentDriversLeaf2018, puglielliIntraspecificVariabilityLeaf2024, puglielliQuantifyingInfluenceIntraspecific2025
- trail: H2-04 §critic, §Adversarial critique, §answers
- rating: "Moderate"

**Lint could not find:** trait ecology rates critic says (also flagged by: content)

Cited text (`from` and named critique):

> Three different partitions are merged here and should be kept apart.
>
> (i) Species-level trade-offs versus community-mean axes: Bruelheide 2018, abstract only; it states agreement qualitatively and itself notes the prior expectation of decoupling.
>
> (ii) Within-community versus among-community components: Kembel & Cahill (full text) and Ackerly & Cornwell (abstract).
>
> (iii) Within-species versus across-species: Anderegg (abstract), Osnas (full text), Puglielli (eigenvector angles).
>
> Evidence that cross-level structure can differ comes from (ii) and (iii), not from the species-versus-community-mean comparison D2 is closest to.
>
> For (i), the only evidence is a single abstract, and it reports agreement.
>
> - The positive cross-level agreement in plants rests on Bruelheide 2018 (abstract only). The review flags this in sensitivity, but D2(b) strength still reads 'replicated across independent plant datasets' for the disagreement side, which mixes partition types.
>
> *Strength:* Moderate that cross-level axis agreement is not guaranteed and can reverse in sign, replicated across independent plant datasets.
>

## H1-02 community-diversity.1 (claim)

In CAMI II, mean bin completeness fell from 36.9% (marine gold-standard assembly) to 18.2% under high strain diversity, and to 5.2% on MEGAHIT assemblies.

- conf: not stated
- class: model (note: "in simulations")
- holds: CAMI II simulated data
- src: meyerCriticalAssessmentMetagenome2022
- trail: H1-02 §3.5, §Verdict as delivered

**Lint could not find:** simulated data (also flagged by: content, setting)

Cited text (`from` and named critique):

> In CAMI II [7], mean bin completeness fell from 36.9% (marine gold-standard assembly) to 18.2% under high strain diversity, and to 5.2% on MEGAHIT assemblies.
>
> Dependence on sample properties: engineered systems and simulations (kept separate)**: MEASURED AND SYSTEMATIC in simulations (strain diversity degrades completeness and purity [7]; depth effects are pipeline-dependent [34]).
>

## H1-06 rank-partitioning.4 (claim)

Across 50,745 GTDB genomes, autotrophy and maximum growth rate had weaker phylogenetic signal than oxygen tolerance and GC content, and at least 25% of variance in four traits fell at a single split.

- conf: not stated
- class: not stated
- holds: GTDB genomes, six genome-inferred traits
- src: hoffertConstructingPeriodicTable2026
- trail: H1-06 §3. Part A2

**Lint could not find:** six genome-inferred (also flagged by: content, setting)

Cited text (`from` and named critique):

> Across 50,745 GTDB genomes, autotrophy and maximum growth rate had weaker signal than oxygen tolerance and GC content, and at least 25% of variance in four traits fell at a single split [8].
>

## H2-04 covariance-partition.4 (claim)

Every microbial partition found is a single study with its own denominator, so the shares cannot be pooled.

- conf: single (note: "single study")
- class: not stated
- holds: the microbial partitions of case D1(b)
- src: none (the review's assessment of its sources)
- trail: H2-04 §answers, §critic
- rating: "Weak"

**Lint could not find:** case d1 b (also flagged by: content, setting)

Cited text (`from` and named critique):

> *Strength:* Weak.
>
> Every microbial partition is a single study with a different denominator, so the shares cannot be pooled.
>
> Strength weak; every microbial share is a single study with its own denominator.
>

## H1-02 sequencing-depth.2 (claim)

Rarefying one surface-ocean data set, MAG yield followed a Gompertz curve (lag 1.2 Gbp) and declined above about 25 Gbp.

- conf: not stated
- class: not stated
- holds: natural marine, one data set; concerns yield, not content
- src: royaltyTheoreticalSimulationBasedInvestigation2019
- trail: H1-02 §3.2, §Verdict as delivered

**Lint could not find:** natural marine (also flagged by: content, setting)

Cited text (`from` and named critique):

> For depth, Royalty and Steen [16] rarefied one surface-ocean data set: MAG yield followed a Gompertz curve (lag 1.2 Gbp) and declined above about 25 Gbp.
>
> That result concerns yield, not content.
>
> The evidence covers MAG yield only [16].
>

## H1-06 uncontrolled-rank-studies.4 (claim)

In Mayjonade et al., group numbers ranged from 18 phyla to 769 ASVs and were not controlled.

- conf: not stated
- class: not stated
- holds: 160 natural sites, gyrB taxonomy
- src: mayjonadeRelativeEffectsAbiotic2024
- trail: H1-06 §4. Part B

**Lint could not find:** 160 natural sites gyrb taxonomy (also flagged by: content, setting)

Cited text (`from` and named critique):

> Group numbers ranged from 18 phyla to 769 ASVs and were not controlled.
>

## H1-05 averaging.12 (claim)

In the 148-dataset synthesis, lower average functional decay coexists with most datasets being null-consistent, the same caution Ho and Huang raise for microbes.

- conf: not stated
- class: not stated
- holds: [48] (diatoms and fungi included, no bacteria)
- src: gracorozaDistanceDecay22022, hoChallengesInterpretingFunctional2025, hoChallengesQuantifyingFunctional2024
- trail: H1-05 §5

**Lint could not find:** diatoms fungi included bacteria (also flagged by: content, setting)

Cited text (`from` and named critique):

> Non-microbial syntheses show that lower average functional decay can coexist with most datasets being null-consistent [48], which is the same caution Ho and Huang raise for microbes.
>

