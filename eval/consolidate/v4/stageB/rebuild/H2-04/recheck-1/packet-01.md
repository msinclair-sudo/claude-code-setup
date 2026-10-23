## within-genome-linkage.2 (claim)

No search route found a fraction of total gene-gene covariance attributable to genome membership.

- conf: not stated
- class: search (note: "no search route found one")
- holds: gene co-abundance binning of gut metagenomes; routes as in the note's search record
- src: metahitIdentificationAssemblyGenomes2014 (AB)
- search: searched, not found (note: "no search route found one")
- trail: H2-04 §Linkage within genomes

From the note:

> H2-04:B-0031 [2. Linkage within genomes] The abstract reports no fraction of total gene-gene covariance attributable to genome membership, and no search route found one.
>
> H2-04:I-0003 [2. Linkage within genomes] The clearest measured case that gene covariation across metagenomes is organised by genome membership is co-abundance binning: across 396 human gut metagenomes, genes clustered into 7,381 co-abundance groups, including 741 metagenomic species, from which 238 high-quality genomes were assembled [18, AB; measured; replicated method family].
>
> H2-04:B-0010 [info: Provenance] Routes used: Europe PMC REST keyword and DOI searches, Europe PMC fullTextXML, PMC HTML via WebFetch (some pages were summarised by the fetch tool, marked FT-s), bioRxiv, eScholarship (Piton accepted manuscript), OpenAlex, Unpaywall, Semantic Scholar API, and Crossref for verification.
>

Not found in the cited text (where to look, not what is wrong): holds: in

## association-networks.8 (claim)

Edge meaning in microbial networks is uncertain, and strategies to remove environmental edges have not been systematically compared.

- conf: not stated
- class: assert (marker)
- holds: a theoretical or review paper
- src: faustOpenChallengesMicrobial2021 (FT; asserted)
- trail: H2-04 §Taxon networks

From the note:

> H2-04:I-0011 [3.1 Taxon networks] Theoretical and review papers conclude that co-occurrence is a poor proxy for interaction [3b, AB; asserted; non-microbial], that edge meaning is uncertain and strategies to remove environmental edges have not been systematically compared [9a, FT; asserted], and that correlation almost never gives reliable information on direct biotic interactions in real ecosystems [5, FT-s; asserted].
>
> H2-04:R-0072 [Reference list] PLoS Computational Biology. 2012;8(7):e1002606. doi:10.1371/journal.pcbi.1002606 [FT] [9a] Faust K. Open challenges for microbial network construction and analysis.
>

## association-networks.15 (claim)

Many bacterial aggregations survive a habitat-aware null model, though the authors state they cannot conclusively reject unmodelled environmental preference.

- conf: not stated
- class: not stated
- holds: cosmopolitan bacteria; annotated in the reference list, not cited in the body
- src: pascualgarciaBacteriaDialogSanta2014 (FT)
- trail: H2-04 §Reference list

From the note:

> H2-04:R-0153 [Reference list] Pascual-García et al. [39, FT] find that many bacterial aggregations survive a habitat-aware null model, and state that they cannot conclusively reject unmodelled environmental preference.
>
> H2-04:R-0151 [Reference list] Additional notes on [38] to [41], which are not cited in the body above but inform it.
>
> H2-04:R-0147 [Reference list] Soil Biology and Biochemistry. 2022;169:108604. doi:10.1016/j.soilbio.2022.108604 [FT] [39] Pascual-García A, Tamames J, Bastolla U. Bacteria dialog with Santa Rosalia: Are aggregations of cosmopolitan bacteria mainly explained by habitat filtering or by ecological interactions?
>

## shared-environment.3 (claim)

The one quantitative partition of environmental effects found is for taxa: in a 10-year monthly marine association network of 29,820 edges, four methods classified 8.3% (the intersection of the four) to 24.8%, 25.7% and 84.6% (individual methods) of edges as environmentally driven; in simulation the individual methods removed 38 to 86% of true interactions along with environmental edges, and the intersection approach also removed 25%. It is the only quantitative environmental-share partition for microbial associations; removing it leaves only asserted statements.

- conf: single (marker)
- class: meas/model (marker)
- holds: taxon association edges in one 10-year monthly marine time series; relative abundances with no log-ratio treatment reported in the findings; the share is limited to measured environmental factors; figures rechecked against full text by the reviewer and by the critic
- src: deutschmannDisentanglingEnvironmentalEffects2021 (FT; measured and modelled; single study)
- trail: H2-04 §Shared response, §answers, §critic, §Provenance

From the note:

> H2-04:I-0030 [5. Shared response to environment] The one quantitative partition found is for taxa: in a 10-year monthly marine network of 29,820 edges, four methods classified 8.3% (intersection) to 24.8%, 25.7% and 84.6% of edges as environmentally driven; in simulation they also removed 38 to 86% of true interactions [7, FT; measured and modelled; single study; figures rechecked by the reviewer against full text].
>
> H2-04:I-0001 [quote: Answers as delivered] Shared environmental response: named as usually the strongest driver of correlation structure [5, full text, asserted], measured as an environment-driven share of taxon edges [7, full text], and modelled as destroying network interpretability [3, abstract].
>
> H2-04:A-020 [quote: Answers as delivered] (1) Taxon association edges, environment-driven versus other, in a 10-year marine time series: 8.3% (intersection of four methods) to 24.8%, 25.7% and 84.6% (individual methods); in simulation the methods removed 38 to 86% of true interactions along with environmental edges [7, full text, rechecked].
>
> H2-04:A-026 [quote: Answers as delivered] Handling of turnover, closure and depth: Deutschmann used relative abundances with no log-ratio treatment reported in the findings; Kamneva used Jaccard presence data; Piton normalised by annotated reads and log(x+1) with no log-ratio treatment and 5 to 15% of reads annotated [23].
>
> H2-04:A-036 [quote: Answers as delivered] *Single-source sensitivity:* Yes.
>
> H2-04:A-037 [quote: Answers as delivered] The only quantitative environmental-share partition for microbial associations is Deutschmann et al. 2021; removing it leaves only asserted statements.
>
> H2-04:C-007 [danger: Critic: answers partly supported] The shared-environment source is asserted (Carr 2019, read only through a tool summary) plus one taxon-level measured partition (Deutschmann 2021).
>
> H2-04:C-011 [danger: Critic: answers partly supported] The Deutschmann figures check out against full text: 8.3% of edges environmentally driven by intersection, 24.8, 25.7 and 84.6% by individual methods, and individual methods removed 38 to 86% of true interactions in simulation.
>
> H2-04:C-012 [danger: Critic: answers partly supported] The review omits that the intersection approach also removed 25%.
>
> H2-04:C-045 [danger: Critic: answers partly supported] I checked the main numerical claims against primary text and they hold: Deutschmann 2021 (8.3/24.8/25.7/84.6%; 38 to 86% of true interactions removed), Kishore 2023 (65.4%, 26.8%), Kamneva 2017 (9.84%, 3.81%), Kembel & Cahill 2011 (92 to 98%), Kehe 2021 (68%, Spearman 0.75), Westoby 2021 (pairwise r2 at most 0.0121), Wieczynski 2019 (27%, abstract), Siefert 2015 (25%, 32%), Nielsen 2014 (abstract counts), Freilich 2018 (0.469, 0.527), Tian 2020 (species-pool null).
>
> H2-04:B-0014 [info: Provenance] Deutschmann 2021 (PMC8620190) and Kembel & Cahill 2011 (PMC3110580) were re-read in full text through Europe PMC, and the 8.3%/24.8%/25.7%/84.6% and 92 to 98% and sign-reversal statements were confirmed.
>
> H2-04:A-021 [quote: Answers as delivered] Reliability is low and the share is method-dependent and limited to measured environmental factors.
>

## aggregation-artefacts.2 (claim)

Standard tests of community-weighted mean versus environment have inflated Type I error that rises as beta diversity falls.

- conf: not stated
- class: model (marker)
- holds: trait ecology; abstract only, via a bioRxiv preprint abstract
- src: zelenyWhichResultsStandard2018 (AB; modelled)
- trail: H2-04 §Artefacts of aggregation

From the note:

> H2-04:I-0035 [7. Artefacts of aggregation, weighting and normalisation] Standard tests of community-weighted mean versus environment have inflated Type I error that rises as beta diversity falls [35, AB; modelled]; the fourth-corner approach is proposed as a remedy [23a, AB].
>
> H2-04:R-0143 [Reference list] Journal of Vegetation Science. 2018;29(6):953-966. doi:10.1111/jvs.12688 [AB, via bioRxiv preprint abstract doi:10.1101/349589] [36] Zelezniak A, Andrejev S, Ponomarova O, Mende DR, Bork P, Patil KR.
>
> H2-04:B-0055 [7. Artefacts of aggregation, weighting and normalisation] Besides closure (section 3), trait ecology documents artefacts specific to aggregating unit-level values into community profiles.
>

## aggregation-artefacts.3 (claim)

The fourth-corner approach is proposed as a remedy for community-weighted mean tests.

- conf: not stated
- class: not stated
- holds: trait ecology; abstract only
- src: peresnetoLinkingTraitVariation2017 (AB)
- trail: H2-04 §Artefacts of aggregation

From the note:

> H2-04:I-0035 [7. Artefacts of aggregation, weighting and normalisation] Standard tests of community-weighted mean versus environment have inflated Type I error that rises as beta diversity falls [35, AB; modelled]; the fourth-corner approach is proposed as a remedy [23a, AB].
>
> H2-04:B-0055 [7. Artefacts of aggregation, weighting and normalisation] Besides closure (section 3), trait ecology documents artefacts specific to aggregating unit-level values into community profiles.
>

## complementarity-overlap.14 (claim)

Antagonism rose with metabolic similarity, with a small effect (pseudo-R2 0.015 to 0.032).

- conf: not stated
- class: meas (marker)
- holds: in vitro bacteria, no community profiles; read through a tool summary
- src: russelAntagonismCorrelatesMetabolic2017 (closer to secondary; measured; critic: C-053 was "FT-s; measured")
- trail: H2-04 §Complementarity versus overlap, §answers

From the note:

> H2-04:I-0026 [4. Complementarity versus overlap among co-occurring organisms] Antagonism rose with metabolic similarity, weakly [28, FT-s; measured].
>
> H2-04:A-043 [quote: Answers as delivered] Measured in vitro: overlap in carbon use predicts competition (68% of the most similar pairs) and difference predicts facilitation (Spearman 0.75) [20, full text]; antagonism rises with metabolic similarity, with small effect (pseudo-R2 0.015 to 0.032) [28, full text via summary]; competition dominates among tree-hole isolates [10a, abstract].
>
> H2-04:B-0046 [4. Complementarity versus overlap among co-occurring organisms] None of these involve community profiles; they bear on mechanism, not on covariation across samples.
>
> H2-04:R-0127 [Reference list] Antagonism correlates with metabolic similarity in diverse bacteria.
>
> H2-04:C-053 [warning: Adversarial critique, full findings] A model's summary of a paper is closer to secondary.
>

## complementarity-overlap.17 (claim)

Whether co-occurrence tracks complementarity is in conflict between Levy & Borenstein 2013 and Zelezniak 2015 with Machado 2021; Machado attributes the difference to scale.

- conf: cont (note: "Conflicts: Levy & Borenstein 2013 versus Zelezniak 2015 and Machado 2021")
- class: model (marker)
- holds: whole-community gut analysis against small-group analyses
- src: levyMetabolicModelingSpecies2013 (closer to secondary; modelled; critic: C-053 was "FT-s; modelled"), zelezniakMetabolicDependenciesDrive2015 (closer to secondary; modelled; critic: C-053 was "FT-s; modelled"), machadoPolarizationMicrobialCommunities2021 (FT; modelled)
- trail: H2-04 §answers, §Complementarity versus overlap

From the note:

> H2-04:A-049 [quote: Answers as delivered] *Conflicts:* Levy & Borenstein 2013 versus Zelezniak 2015 and Machado 2021 on whether co-occurrence tracks complementarity; Machado attributes the difference to scale.
>
> H2-04:I-0018 [4. Complementarity versus overlap among co-occurring organisms] Across 154 gut species, co-occurrence correlated with modelled metabolic competition (rho = 0.211) and negatively with modelled complementarity (rho = -0.193); effects weak; profiles mapped to the same reference genomes [17, FT-s; modelled].
>
> H2-04:I-0021 [4. Complementarity versus overlap among co-occurring organisms] At the level of small co-occurring groups (pairs to quadruplets, >800 communities), modelled resource overlap was barely distinguishable from random while modelled metabolic interaction potential was elevated [36, FT-s; modelled].
>
> H2-04:I-0022 [4. Complementarity versus overlap among co-occurring organisms] Co-occurring groups of up to 40 species polarised into cooperative groups (small genomes, auxotrophies) and competitive groups (large genomes, overlapping requirements, mainly soils); the authors attribute the difference from Levy & Borenstein to scale [19, FT; modelled].
>
> H2-04:A-040 [quote: Answers as delivered] Derived and modelled whole-community analyses find overlap: co-occurring lineages have more similar pathway content and genome size than chance, beyond phylogeny [4, full text]; positive HMP associations are enriched for functional similarity and negative ones for dissimilarity [9, full text]; gut co-occurrence correlates with modelled competition (rho = 0.211) and negatively with modelled complementarity (rho = -0.193) [17, full text via summary]; human microbiome samples have higher functional redundancy than random draws from the species pool [30, full text].
>
> H2-04:A-041 [quote: Answers as delivered] Modelled small-group analyses find complementarity: co-occurring pairs to quadruplets have elevated metabolic interaction potential and resource overlap barely above random [36, full text via summary], and co-occurring groups polarise into cooperative (small genomes, auxotrophies) and competitive (large genomes, soils) types [19, full text].
>
> H2-04:C-053 [warning: Adversarial critique, full findings] A model's summary of a paper is closer to secondary.
>
> H2-04:C-053 [warning: Adversarial critique, full findings] A model's summary of a paper is closer to secondary.
>

## complementarity-overlap.20 (claim)

The evidence on complementarity versus overlap splits by scale and by evidence class: at whole-community scale, co-occurrence is associated with genome similarity (overlap), with weak effects; modelled small-group analyses find complementarity.

- conf: not stated
- class: deriv/model (note: "Derived and modelled whole-community analyses find overlap")
- holds: whole-community co-occurrence (Chaffron from its abstract, Faust, Kamneva's genome-content similarity index) against modelled small groups; both sides depend on co-occurrence inference
- src: chaffronGlobalNetworkCoexisting2010 (abstract), faustMicrobialCooccurrenceRelationships2012, kamnevaGenomeCompositionPhylogeny2017
- rating: "Moderate for the pattern that whole-community co-occurrence associates with overlap" (critic: C-025: weak to moderate for overlap, weak for complementarity)
- contrary: one-sided (critic: C-096)
- trail: H2-04 §answers, §critic, §Complementarity versus overlap

From the note:

> H2-04:A-039 [quote: Answers as delivered] **D1, case (c): complementarity versus redundancy (functional overlap) among co-occurring organisms**: The evidence splits by scale and by evidence class.
>
> H2-04:A-040 [quote: Answers as delivered] Derived and modelled whole-community analyses find overlap: co-occurring lineages have more similar pathway content and genome size than chance, beyond phylogeny [4, full text]; positive HMP associations are enriched for functional similarity and negative ones for dissimilarity [9, full text]; gut co-occurrence correlates with modelled competition (rho = 0.211) and negatively with modelled complementarity (rho = -0.193) [17, full text via summary]; human microbiome samples have higher functional redundancy than random draws from the species pool [30, full text].
>
> H2-04:A-041 [quote: Answers as delivered] Modelled small-group analyses find complementarity: co-occurring pairs to quadruplets have elevated metabolic interaction potential and resource overlap barely above random [36, full text via summary], and co-occurring groups polarise into cooperative (small genomes, auxotrophies) and competitive (large genomes, soils) types [19, full text].
>
> H2-04:A-046 [quote: Answers as delivered] *Strength:* Moderate for the pattern that whole-community co-occurrence associates with overlap, replicated across independent groups but with weak effects.
>
> H2-04:B-0041 [4. Complementarity versus overlap among co-occurring organisms] This is where the empirical work is densest, and it pulls in two directions depending on scale and evidence class.
>
> H2-04:B-0042 [4. Complementarity versus overlap among co-occurring organisms] Overlap (redundancy, shared niche).
>
> H2-04:B-0043 [4. Complementarity versus overlap among co-occurring organisms] Complementarity (division of labour).
>
> H2-04:C-017 [danger: Critic: answers partly supported] - **D1, case (c): complementarity versus overlap among co-occurring organisms**: Partly supported.
>
> H2-04:C-018 [danger: Critic: answers partly supported] At whole-community scale, co-occurrence is associated with genome similarity (Chaffron abstract; Faust; Kamneva's genome-content similarity index).
>
> H2-04:C-025 [danger: Critic: answers partly supported] Strength: weak to moderate for overlap, weak for complementarity.
>
> H2-04:C-096 [warning: Adversarial critique, full findings] - D1(c): the overlap side is rated moderate and 'replicated across independent groups', although it rests on co-occurrence inference.
>
> H2-04:C-026 [danger: Critic: answers partly supported] Both sides depend on co-occurrence inference, which section 3 of the review shows to be unreliable.
>

Not found in the cited text (where to look, not what is wrong): holds: its

## covariation-sources.6 (claim)

No study found names all five sources for the same function-by-sample table.

- conf: not stated
- class: search (note: "No study found that names all five sources for the same function-by-sample table")
- holds: routes: Europe PMC REST keyword searches, Crossref, OpenAlex, PMC full text, three independent search angles (complementarity, co-occurrence, trait ecology); WebSearch and Scholar Gateway unavailable
- src: none (a search result)
- search: searched, not found (note: "No study found that names all five sources for the same function-by-sample table")
- trail: H2-04 §answers, §Adversarial critique

From the note:

> H2-04:A-009 [quote: Answers as delivered] *Not measured:* No study found that names all five sources for the same function-by-sample table.
>
> H2-04:A-011 [quote: Answers as delivered] Search routes: Europe PMC REST keyword searches, Crossref, OpenAlex, PMC full text, three independent search angles (complementarity, co-occurrence, trait ecology); WebSearch and Scholar Gateway unavailable..
>
> H2-04:C-113 [warning: Adversarial critique, full findings] The review's main absence claims (no function-level partition, no formal axis comparison) are its own search results, with routes named.
>

## trait-partitions.1 (claim)

The only measured covariance partitions found are within-unit versus between-unit partitions in trait ecology (plants, non-microbial).

- conf: not stated
- class: search (note: "These are the only measured covariance partitions found")
- holds: non-microbial; species traits, not gene content
- src: none (a search result)
- search: searched, not found (note: "These are the only measured covariance partitions found")
- trail: H2-04 §Within-unit versus between-unit

From the note:

> H2-04:B-0058 [8. Within-unit versus between-unit partitions in trait ecology (labelled non-microbial)] These are the only measured covariance partitions found.
>
> H2-04:A-029 [quote: Answers as delivered] The plant partitions are measured and partly replicated but concern species traits, not gene content..
>
> H2-04:C-014 [danger: Critic: answers partly supported] The plant partitions (Ackerly & Cornwell abstract; Kembel & Cahill full text, 92 to 98% within communities) are non-microbial and concern species traits.
>
> H2-04:B-0059 [8. Within-unit versus between-unit partitions in trait ecology (labelled non-microbial)] In California woody plants, among-community (beta) components of four traits covaried strongly along a moisture gradient while within-community (alpha) components were largely uncorrelated [1, AB].
>

## trait-partitions.4 (claim)

In plants, Ackerly & Cornwell find among-community covariation dominant while Kembel & Cahill find correlations among species means driven by the within-community component; these are different systems and are not contradictory in the strict sense.

- conf: not stated
- class: not stated
- holds: California woody plants against Alberta grasslands
- src: ackerlyTraitbasedApproachCommunity2007 (abstract), kembelIndependentEvolutionLeaf2011 (full text)
- trail: H2-04 §answers

From the note:

> H2-04:A-031 [quote: Answers as delivered] In plants, Ackerly & Cornwell find among-community covariation dominant while Kembel & Cahill find correlations among species means driven by the within-community component; these are different systems and are not contradictory in the strict sense..
>
> H2-04:B-0059 [8. Within-unit versus between-unit partitions in trait ecology (labelled non-microbial)] In California woody plants, among-community (beta) components of four traits covaried strongly along a moisture gradient while within-community (alpha) components were largely uncorrelated [1, AB].
>
> H2-04:B-0060 [8. Within-unit versus between-unit partitions in trait ecology (labelled non-microbial)] In Alberta grasslands (76 species, 27 communities), 92 to 98% of trait variance was within communities, and SLA and specific root length correlated positively within and negatively among communities [16, FT; rechecked].
>

## covariation-partition.1 (claim)

No study found partitions covariation among functions in community profiles into within-genome linkage, organism co-occurrence, shared environment, shared ancestry and artefact shares; the partitions that exist are of other quantities.

- conf: not stated
- class: search (note: "No study found partitions covariation among functions in community profiles")
- holds: metagenomic or genome-derived community profiles; routes as for the sources, plus Europe PMC queries on community-aggregated traits with covariation and trade-off terms and on strain-level versus taxonomic turnover; the critic: the headline absence is stated with appropriate restraint
- src: none (a search result)
- rating: "Weak" (critic: C-009: Supported)
- search: searched, not found (note: "No study found partitions covariation among functions in community profiles")
- trail: H2-04 §answers, §critic, §Provenance

From the note:

> H2-04:A-018 [quote: Answers as delivered] **D1, case (b): partitions of covariation among sources, with shares and reliability**: No study found partitions covariation among functions in community profiles into within-genome linkage, organism co-occurrence, shared environment, shared ancestry and artefact shares.
>
> H2-04:A-019 [quote: Answers as delivered] The partitions that exist are of other quantities.
>
> H2-04:A-027 [quote: Answers as delivered] *Strength:* Weak.
>
> H2-04:A-033 [quote: Answers as delivered] Routes as in case (a); also Europe PMC queries on community-aggregated traits with covariation and trade-off terms, and on strain-level versus taxonomic turnover..
>
> H2-04:C-009 [danger: Critic: answers partly supported] - **D1, case (b): partitions with shares and reliability**: Supported.
>
> H2-04:C-010 [danger: Critic: answers partly supported] No partition of function-by-function covariance in community profiles was found.
>
> H2-04:C-044 [danger: Critic: answers partly supported] The answers are mostly supported by the body, and the headline absences for D1(b) and D2(a) are stated with appropriate restraint.
>
> H2-04:B-0017 [info: Provenance] Not found through any route: (1) a partition of function-by-function covariance in community profiles into within-genome linkage, co-occurrence, environment, ancestry and artefact shares; (2) a gene or KO co-occurrence network that removes within-genome linkage; (3) a formal agreement statistic between genome-level and community-level functional axes in any microbial system; (4) a microbial application of turnover versus within-taxon decomposition to functional profiles; (5) animal trait analogues of within- versus between-unit covariance partitions (not specifically searched); (6) any quantification of contamination effects on measured within-genome linkage.
>
> H2-04:A-032 [quote: Answers as delivered] *Not measured:* Any partition of function-by-function covariance in metagenomic or genome-derived community profiles; any microbial analogue of the Leps-type turnover versus within-taxon decomposition (Leps et al. 2011 itself not obtained).
>

## covariation-partition.6 (claim)

On the reviewer's reading, trait ecology has the partitioning machinery and shows that within-unit and between-unit covariation can differ in sign and in cause; it has not been applied to metagenomic function in any study found.

- conf: not stated
- class: reading (critic: C-109)
- holds: trait ecology; metagenomic function
- src: none (the reviewer's synthesis)
- trail: H2-04 §How the cases relate

From the note:

> H2-04:B-0075 [10. How the cases relate] Trait ecology has the partitioning machinery and shows that within-unit and between-unit covariation can differ in sign and in cause; it has not been applied to metagenomic function in any study found.
>
> H2-04:C-109 [warning: Adversarial critique, full findings] - Section 10 ('approached from two sides that do not meet') is the reviewer's synthesis argument. It is reasonable but unlabelled as the reviewer's reading.
>

## genome-community-axes.3 (claim)

The same paper asserts that community-average rRNA copy number varies less than isolate values, a compression that would change loadings between levels; this and the authors' own caveat cut against reading the qualitative agreement as axis identity.

- conf: not stated
- class: assert (marker)
- holds: soil metagenomes against isolates
- src: pitonLifeHistoryStrategies2023 (asserted)
- trail: H2-04 §Genome-level versus community-level, §answers

From the note:

> H2-04:B-0065 [9. Genome-level versus community-level functional axes (D2)] The same paper asserts that community-average rRNA copy number varies less than isolate values [23, asserted], a compression that would change loadings between levels.
>
> H2-04:A-066 [quote: Answers as delivered] Piton's own caveat and the asserted compression of community-average rRNA copy number variance relative to isolates [23, asserted] cut against reading the qualitative agreement as axis identity..
>
> H2-04:I-0038 [9. Genome-level versus community-level functional axes (D2)] Piton et al. obtained community axes from 128 soil metagenomes (29% and 21% of variance on the first two), the first a streamlined-to-expanded-genome axis, described as consistent with isolate-based axes without a test, and cautioned that community-aggregated patterns do not inform on within-organism trade-offs [23, FT; measured; single study; profiles independent of isolate genomes; read-based annotation of 5 to 15% of reads; no log-ratio treatment].
>

## genome-community-axes.10 (claim)

Functional shifts decomposed into taxon contributions show that the contributing taxa vary markedly between functions.

- conf: not stated
- class: not stated
- holds: human microbiome; abstract only; annotated in the reference list, not cited in the body
- src: manorSystematicCharacterizationAnalysis2017 (AB)
- trail: H2-04 §Reference list

From the note:

> H2-04:R-0154 [Reference list] Manor & Borenstein [40, AB] decompose functional shifts into taxon contributions and find that the contributing taxa vary markedly between functions.
>
> H2-04:R-0151 [Reference list] Additional notes on [38] to [41], which are not cited in the body above but inform it.
>
> H2-04:R-0148 [Reference list] BMC Microbiology. 2014;14(1):284. doi:10.1186/s12866-014-0284-5 [FT] [40] Manor O, Borenstein E. Systematic characterization and analysis of the taxonomic drivers of functional shifts in the human microbiome.
>

## plant-cross-level-axes.10 (claim)

Not measured: quantitative agreement statistics for species-level versus community-mean axes at global scale.

- conf: not stated
- class: search (note: "Not measured: Quantitative agreement statistics")
- holds: plants, global scale
- src: none (a search result)
- search: not stated
- trail: H2-04 §answers

From the note:

> H2-04:A-079 [quote: Answers as delivered] *Not measured:* Quantitative agreement statistics for species-level versus community-mean axes at global scale.
>
> H2-04:A-071 [quote: Answers as delivered] **D2, case (b): trait-ecology analogues (plants), labelled non-microbial**: Plant ecology has made the comparison, with mixed results.
>

## dns.6 (do not say)

"Linkage is not uniform across functions: for sequential redox pathways, within-genome linkage is weak and pathway completion is distributed across organisms."

- why: This generalises from one aquifer study (Anantharaman 2016) to a class of functions.
- instead: within-genome-linkage.3
- trail: H2-04 §Adversarial critique, §Linkage within genomes

From the note:

> H2-04:B-0032 [2. Linkage within genomes] Linkage is not uniform across functions.
>
> H2-04:B-0033 [2. Linkage within genomes] For such functions, within-genome linkage is weak and pathway completion is distributed across organisms.
>
> H2-04:C-066 [warning: Adversarial critique, full findings] - Section 2 'For such functions, within-genome linkage is weak and pathway completion is distributed across organisms' generalises from one aquifer study (Anantharaman 2016) to a class of functions.
>
> H2-04:I-0004 [2. Linkage within genomes] In 2,540 aquifer genomes, most organisms carried one step of sequential redox pathways, few carried two, and very few three or more; the authors argue incompleteness does not explain this [3a, FT; derived; single study; community composition and genomes from the same metagenomes].
>

Not found in the cited text (where to look, not what is wrong): "Linkage is not uniform across functions: for sequential redox pathways, within-genome linkage is weak and pathway completion is distributed across organisms."

## dns.12 (do not say)

"Plant ecology has compared species-level and community-level axes with mixed results: Bruelheide 2018 finds agreement at global scale, against the disagreement or sign reversal of Kembel & Cahill 2011, Anderegg 2018 and Osnas 2018."

- why: This folds three distinct partitions into one comparison; sign reversals from within-species and within-community partitions do not answer the species-versus-community-mean comparison, for which the only evidence is Bruelheide's single abstract, and it reports agreement.
- instead: plant-cross-level-axes.8
- trail: H2-04 §answers, §critic, §Adversarial critique

From the note:

> H2-04:A-071 [quote: Answers as delivered] **D2, case (b): trait-ecology analogues (plants), labelled non-microbial**: Plant ecology has made the comparison, with mixed results.
>
> H2-04:A-077 [quote: Answers as delivered] *Conflicts:* Bruelheide 2018 (agreement at global scale) versus Kembel & Cahill 2011, Anderegg 2018 and Osnas 2018 (disagreement or sign reversal at local or within-species scale).
>
> H2-04:C-036 [danger: Critic: answers partly supported] Three different partitions are merged here and should be kept apart.
>
> H2-04:C-041 [danger: Critic: answers partly supported] Evidence that cross-level structure can differ comes from (ii) and (iii), not from the species-versus-community-mean comparison D2 is closest to.
>
> H2-04:C-049 [danger: Critic: answers partly supported] (4) D2(b) merges three different partitions.
>
> H2-04:C-101 [warning: Adversarial critique, full findings] - D2(b) folds three distinct partitions into one answer: species-level versus community-mean axes (Bruelheide), within-community versus among-community components (Kembel & Cahill, Ackerly & Cornwell), and within-species versus across-species (Anderegg, Osnas, Puglielli).
>
> H2-04:C-103 [warning: Adversarial critique, full findings] Evidence of sign reversal from within-species partitions does not answer the species-versus-community-mean comparison closest to D2.
>
> H2-04:C-037 [danger: Critic: answers partly supported] (i) Species-level trade-offs versus community-mean axes: Bruelheide 2018, abstract only; it states agreement qualitatively and itself notes the prior expectation of decoupling.
>
> H2-04:C-042 [danger: Critic: answers partly supported] For (i), the only evidence is a single abstract, and it reports agreement.
>

Not found in the cited text (where to look, not what is wrong): "Plant ecology has compared species-level and community-level axes with mixed results: Bruelheide 2018 finds agreement at global scale, against the disagreement or sign reversal of Kembel & Cahill 2011, Anderegg 2018 and Osnas 2018."

## dns.13 (do not say)

"That cross-level axis agreement can reverse in sign is replicated across independent plant datasets."

- why: The 'replicated across independent plant datasets' strength mixes partition types (within-community versus among-community and within-species versus across-species).
- instead: plant-cross-level-axes.9
- trail: H2-04 §Adversarial critique

From the note:

> H2-04:C-069 [warning: Adversarial critique, full findings] - The positive cross-level agreement in plants rests on Bruelheide 2018 (abstract only). The review flags this in sensitivity, but D2(b) strength still reads 'replicated across independent plant datasets' for the disagreement side, which mixes partition types.
>
> H2-04:A-075 [quote: Answers as delivered] *Strength:* Moderate that cross-level axis agreement is not guaranteed and can reverse in sign, replicated across independent plant datasets.
>
> H2-04:C-038 [danger: Critic: answers partly supported] (ii) Within-community versus among-community components: Kembel & Cahill (full text) and Ackerly & Cornwell (abstract).
>
> H2-04:C-039 [danger: Critic: answers partly supported] (iii) Within-species versus across-species: Anderegg (abstract), Osnas (full text), Puglielli (eigenvector angles).
>
> H2-04:C-041 [danger: Critic: answers partly supported] Evidence that cross-level structure can differ comes from (ii) and (iii), not from the species-versus-community-mean comparison D2 is closest to.
>

Not found in the cited text (where to look, not what is wrong): "That cross-level axis agreement can reverse in sign is replicated across independent plant datasets."

## dns.16 (do not say)

"Growth rate, genome size and cell size are independent dimensions: pairwise r2 is at most 0.012."

- why: The pairwise values are right, but the paper also reports a weak nonlinearity (about 6% of variance) and habitat effects (about 11%), which qualify 'near-independent'; the review omits them.
- instead: genome-community-axes.5
- trail: H2-04 §critic, §Adversarial critique

From the note:

> H2-04:C-033 [danger: Critic: answers partly supported] The review omits the weak nonlinearity (about 6% of variance) and the habitat effects (about 11%) that the paper reports.
>
> H2-04:C-062 [warning: Adversarial critique, full findings] - Westoby 2021 (FT): 'r2 at most 0.012' is correct for pairwise correlations (maximum 0.0121, genome size versus cell diameter). The review omits the paper's reported 6% nonlinearity and roughly 11% habitat contribution, which qualify 'near-independent'.
>
> H2-04:B-0067 [9. Genome-level versus community-level functional axes (D2)] Genome-level axes on their own: growth rate, genome size and cell size are near-independent (r2 at most 0.012) [33, FT]; trait relations reverse above about 5 Mb [2a, AB]; growth-related genome traits are strongly correlated and have been used to read metagenomes [33a, AB].
>

Not found in the cited text (where to look, not what is wrong): "Growth rate, genome size and cell size are independent dimensions: pairwise r2 is at most 0.012."

