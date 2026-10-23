# Sources of functional covariation and cross-level functional axes: writer's view

> [!abstract] About this view
> What the research found, for writing from. Each claim gives who found it, the setting it holds for, the kind of evidence, its standing where the research stated one, and for an absence whether it was searched for. A claim with no standing given has none stated in the research; "limited by access" means a source was not read in full, which is not the same as weak evidence. Sources are listed at the end. The view is generated from the knowledge note `Sources of functional covariation and cross-level functional axes.md`, where every claim is checked against the research.

## What the research found, by question

### H2-04

**D1. What sources of covariation among functions in community profiles have been identified (linkage within genomes, co-occurrence of different organisms, shared responses of functions to environment, shared ancestry, and compositional, normalisation or annotation artefacts), and where studies partitioned covariation among such sources, what shares did they find and how reliable were the partitions?**

*Answer, as corrected by a second reader.* **D1, case (a): sources of covariation identified**

Supported with corrections. Each of the five sources is named somewhere, but almost always for taxa, not for function-by-sample tables. Within-genome linkage at gene level rests on one abstract (Nielsen 2014: 7,381 co-abundance groups, 741 MGS, 396 gut metagenomes; no covariance share). Remove Fierer et al. 2014 (Fierer et al. 2014) from the list of co-occurrence network studies: its abstract is a community-aggregated-traits perspective, not a network study. The 'annotation reference choice' figure (65.4%, Kishore 2023, checked against full text) is the 16S taxonomy database's share of variance among taxon networks. It says nothing directly about functional annotation schemes, so it is indirect for function profiles. The shared-environment source is asserted (Carr 2019, read only through a tool summary) plus one taxon-level measured partition (Deutschmann 2021). Strength: moderate for existence at the taxon level, weak or indirect at the function level.

*Answer, as corrected by a second reader.* **D1, case (b): partitions with shares and reliability**

Supported. No partition of function-by-function covariance in community profiles was found. The Deutschmann figures check out against full text: 8.3% of edges environmentally driven by intersection, 24.8, 25.7 and 84.6% by individual methods, and individual methods removed 38 to 86% of true interactions in simulation. The review omits that the intersection approach also removed 25%. Kamneva's figures also check out (9.84% phylogeny; 3.81% added by genomic indices). The plant partitions (Ackerly & Cornwell abstract; Kembel & Cahill full text, 92 to 98% within communities) are non-microbial and concern species traits. They are a different partition from within-species versus between-species (Siefert). Strength weak; every microbial share is a single study with its own denominator.

*Answer, as corrected by a second reader.* **D1, case (c): complementarity versus overlap among co-occurring organisms**

Partly supported. At whole-community scale, co-occurrence is associated with genome similarity (Chaffron abstract; Faust; Kamneva's genome-content similarity index). But Kamneva's combined model makes both metabolic competition (p = 0.71) and metabolic complementarity (p = 0.14) non-significant once phylogeny and genome content similarity are included. So the only reanalysis undercuts Levy & Borenstein's modelled competition signal as well as its complementarity signal. The review reports only the complementarity half. Tian 2020 measures within-sample redundancy against a species-pool null, not pairwise co-occurrence, and should be kept as a separate case. Small-group complementarity rests on one method family (Zelezniak 2015, Machado 2021), and the Zelezniak figures were read only through a tool summary. In vitro results (Kehe 2021: 68%, Spearman 0.75, checked against full text) bear on mechanism, not on covariation across samples. Strength: weak to moderate for overlap, weak for complementarity. Both sides depend on co-occurrence inference, which section 3 of the review shows to be unreliable.

**D2. Where the main axes of functional variation among genomes have been compared with those among community profiles, how do they compare, and by what measure of agreement?**

*Answer, as corrected by a second reader.* **D2, case (a): microbial genome-level versus community-level axes**

Supported. No formal axis-agreement statistic was found. Piton 2023 is the nearest precedent. Its abstract says the two community trait dimensions 'support previous theoretical and isolate-based studies', but the specific figures (29%, 21%, R2 0.64, R2 0.32, 5 to 15% of reads annotated) could not be independently rechecked in this critique. Gralka rests on a tool summary of a preprint. Westoby 2021's pairwise r2 values (maximum 0.0121) are confirmed. The review omits the weak nonlinearity (about 6% of variance) and the habitat effects (about 11%) that the paper reports. Strength: absent as direct evidence.

*Answer, as corrected by a second reader.* **D2, case (b): plant analogues**

Partly supported. Three different partitions are merged here and should be kept apart. (i) Species-level trade-offs versus community-mean axes: Bruelheide 2018, abstract only; it states agreement qualitatively and itself notes the prior expectation of decoupling. (ii) Within-community versus among-community components: Kembel & Cahill (full text) and Ackerly & Cornwell (abstract). (iii) Within-species versus across-species: Anderegg (abstract), Osnas (full text), Puglielli (eigenvector angles). Dong 2020 is about trait-environment responses, not axis reversal. Evidence that cross-level structure can differ comes from (ii) and (iii), not from the species-versus-community-mean comparison D2 is closest to. For (i), the only evidence is a single abstract, and it reports agreement. Animal, quantitative-genetic (G-matrix versus divergence) and morphometric (static versus evolutionary allometry) analogues were not searched.

## Concepts

In an order where each concept comes after the ones it builds on; the order means nothing more.

### linkage of genes within genomes

- Gene covariation across metagenomes is organised by genome membership in gene co-abundance binning: across 396 human gut metagenomes, genes clustered into 7,381 co-abundance groups, including 741 metagenomic species, from which 238 high-quality genomes were assembled; no share of total gene covariation attributable to genome membership is reported. (MetaHIT et al. 2014)
  Holds for: 396 human gut metagenomes; read in the abstract only; the within-genome-linkage evidence at gene level rests on this one abstract; the counts were checked against the abstract by the critic.
  Evidence: measured; a single source.
- No search route found a fraction of total gene-gene covariance attributable to genome membership. (MetaHIT et al. 2014)
  Holds for: gene co-abundance binning of gut metagenomes; routes as in the note's search record.
  Evidence: a search result.
  Searched for and not found.
- In 2,540 aquifer genomes, most organisms carried one step of sequential redox pathways, few carried two, and very few three or more; the authors argue incompleteness does not explain this (stepwise division of redox pathways across aquifer genomes). (Anantharaman et al. 2016)
  Holds for: one aquifer system; community composition and genomes from the same metagenomes; the critic: one aquifer study, not evidence for a class of functions.
  Evidence: derived; a single source.
- Genome incompleteness produces false gene absences: predicted auxotrophies correlate negatively with genome completeness. (Starke et al. 2023)
  Holds for: amino acid auxotrophies predicted from human gut bacterial genomes, as a caution on measured linkage.
- Annotation gaps produce apparent pathway holes: 9 of 11 amino-acid gaps in 10 genera were filled by unannotated enzymes, so predicted auxotrophies are often annotation gaps. (Price et al. 2018)
  Holds for: amino-acid biosynthesis pathway gaps in 10 bacterial genera; abstract only.
  Evidence: measured.
- Horizontal transfer is 25-fold more frequent among human-associated bacteria than among ecologically diverse non-human isolates, and is structured by shared habitat. (Smillie et al. 2011)
  Holds for: human-associated bacteria against ecologically diverse non-human isolates; abstract only; the critic: one study, used in the answers as a general caution on the overlap side.
  Evidence: derived; a single source.
- No source found quantifies contamination effects on measured within-genome linkage specifically. (a search result)
  Holds for: routes as in the note's search record.
  Evidence: a search result.
  Searched for and not found.

### co-occurrence and association networks, and what their edges indicate

Builds on: shared response to environment.

- Microbiome datasets generated by high-throughput sequencing (16S rRNA gene amplicons, metagenomes, metatranscriptomes) are compositional, because the instrument imposes an arbitrary total on each sample. (Gloor et al. 2017)
  Background, not from the research.
- Taxon association (co-occurrence) networks are built in quantity, but benchmarks limit what their edges can indicate. (Barberan et al. 2012; Faust et al. 2012; Levy and Borenstein 2013)
  Holds for: taxon networks, not functions; the critic removed Fierer et al. 2014 from the list of network studies (a community-aggregated-traits perspective, not a network study).
- Eight correlation tools run on the same simulated data shared on average 31.5% of edges; constraining totals produced incorrect edges for most tools, worst below an effective species number of about 13; the best precision for sparse Lotka-Volterra relations was 0.2. (Weiss et al. 2016)
  Holds for: simulated data; the critic could not retrieve the PMC XML, so these figures are unverified in the critique.
  Evidence: modelled; replicated; limited by access (a source was not read in full; not the same as weak evidence).
- Closure alone can flip correlation signs; on HMP data, standard correlation was estimated to give about 3 spurious edges per true one, relative to SparCC as the reference and not relative to known truth. (Friedman and Alm 2012)
  Holds for: HMP data; SparCC as reference; abstract only.
  Evidence: modelled.
- Whether compositionally aware methods remove closure artefacts is a conflict: they beat other methods in their own benchmarks, but in an independent population-dynamics simulation they did no better than Pearson correlation, and recovered competition better than predator-prey relations; the conflict is not resolved. (Hirano and Takemoto 2019; Kurtz et al. 2015)
  Holds for: the methods' own benchmarks (abstract) against one independent simulation.
  Evidence: contested.
- Direct validation of network edges is thin: two gut species pairs from a network were co-cultured and behaved as the edges predicted (n = 2). (Das et al. 2018)
  Holds for: two human gut bacterial species pairs from a network, co-cultured in vitro.
  Evidence: measured; a single source.
- In a non-microbial rocky-intertidal system, a co-occurrence network matched an independently resolved interaction network at about chance (sensitivity 0.469, specificity 0.527). (Freilich et al. 2018)
  Holds for: rocky intertidal, non-microbial; abstract only; figures checked by the critic.
  Evidence: measured.
- Theoretical and review papers conclude that co-occurrence is a poor proxy for interaction (co-occurrence is not interaction). (Blanchet et al. 2020)
  Holds for: non-microbial; abstract only.
  Evidence: asserted.
- Edge meaning in microbial networks is uncertain, and strategies to remove environmental edges have not been systematically compared. (Faust 2021)
  Holds for: a theoretical or review paper.
  Evidence: asserted.
- Correlation almost never gives reliable information on direct biotic interactions in real ecosystems. (Carr et al. 2019)
  Holds for: a theoretical or review paper; read through a web-fetch tool summary (FT-s).
  Evidence: asserted.
- In macroecology, joint species distribution models cannot separate environment from interaction. (Poggiato et al. 2021)
  Holds for: macroecology; abstract only.
  Evidence: derived.
- Residual correlations of joint species distribution models depend on prevalence. (Zurell et al. 2018)
  Holds for: macroecology; abstract only.
  Evidence: modelled.
- Metacommunity disturbance alone can generate associations between non-interacting species. (Calcagno et al. 2021)
  Holds for: macroecology; a preprint; abstract only.
  Evidence: modelled.
- Among taxon co-occurrence networks inferred from amplicon data, the 16S reference (taxonomy) database contributed 65.4% of the variance among inferred networks and OTU processing 26.8%; this concerns taxonomic, not functional, annotation, so it is indirect for function profiles. (Kishore et al. 2023)
  Holds for: taxon networks (16S); the annotation-artefact magnitude rests on this study alone; figures checked against full text by the critic; says nothing directly about functional annotation schemes.
  Evidence: measured; a single source.
- Edge sets from Spearman, SparCC and GLASSO overlap only partly on the same soil data; citing theory, environmental filtering is expected to dominate as sampling-unit scale grows. (Guseva et al. 2022)
  Holds for: soil data; a source not cited in the review's body but annotated in its reference list.
- Many bacterial aggregations survive a habitat-aware null model, though the authors state they cannot conclusively reject unmodelled environmental preference. (Pascual-Garcia et al. 2014)
  Holds for: cosmopolitan bacteria; annotated in the reference list, not cited in the body.
- FlashWeave conditions on metadata to separate direct from indirect associations, with simulation-only evaluation. (Tackmann et al. 2019)
  Holds for: simulation only; annotated in the reference list, not cited in the body.

### shared response to environment

Builds on: co-occurrence and association networks, and what their edges indicate.

- Environmental heterogeneity is argued to be usually the strongest driver of correlation structure; named as such, the shared-environment source is asserted. (Carr et al. 2019)
  Holds for: asserted; read only through a tool summary.
  Evidence: asserted; a single source.
- Simulation shows co-occurrence networks lose interpretability when habitat filtering is significant (modelled as destroying network interpretability). (Berry and Widder 2014)
  Holds for: simulation; abstract only.
  Evidence: modelled.
- The one quantitative partition of environmental effects found is for taxa: in a 10-year monthly marine association network of 29,820 edges, four methods classified 8.3% (the intersection of the four) to 24.8%, 25.7% and 84.6% (individual methods) of edges as environmentally driven; in simulation the individual methods removed 38 to 86% of true interactions along with environmental edges, and the intersection approach also removed 25%. It is the only quantitative environmental-share partition for microbial associations; removing it leaves only asserted statements. (Deutschmann et al. 2021)
  Holds for: taxon association edges in one 10-year monthly marine time series; relative abundances with no log-ratio treatment reported in the findings; the share is limited to measured environmental factors; figures rechecked against full text by the reviewer and by the critic.
  Evidence: measured and modelled; a single source.
- The environment-driven share of association edges is method-dependent: the methods disagree by an order of magnitude (8.3% to 84.6%), and reliability is low. (Deutschmann et al. 2021)
  Holds for: one marine time series; share limited to measured environmental factors.
  Evidence: measured and modelled; a single source.
- Tara Oceans authors conclude that environment is an incomplete predictor of community structure; the numbers were not reached. (Lima-Mendez et al. 2015)
  Holds for: the global plankton interactome (Tara Oceans); abstract only.
  Evidence: limited by access (a source was not read in full; not the same as weak evidence).
- For functions, ocean functional groups track environment strongly while taxonomy within groups does not; the functional groups are assigned from taxonomy, so they are not independent of composition. (Louca et al. 2016)
  Holds for: the global ocean microbiome; functional groups assigned from taxonomy; abstract only.
  Evidence: derived; contested.
- Enrichment communities converge in function and in family-level taxonomy under a given carbon source. (Goldford et al. 2018)
  Holds for: enrichment communities; the cross-feeding mechanism modelled; abstract only.
  Evidence: measured.
- A consumer-resource model reproduces survey-level patterns from shared environments. (Marsland et al. 2020)
  Holds for: a model; abstract only.
  Evidence: modelled.

### networks built among functions (genes, KOs)

Builds on: co-occurrence and association networks, and what their edges indicate, linkage of genes within genomes.

- GeoChip functional-gene networks in grassland soil differed between ambient and elevated CO2, and their links were interpreted as interactions among populations carrying the genes. (Zhou et al. 2010)
  Holds for: grassland soil; profiles independent of any genome set; one of the two studies that build networks among functions directly; gene-level network interpretation rests on this and one preprint.
  Evidence: measured; a single source; rated "Weak for gene-level (as opposed to taxon-level) covariation" by the research.
- A KO co-occurrence network from a decade of monthly marine metagenomes found vitamin metabolism the most connected pathway. (Arandia-Gorostidi et al. 2025)
  Holds for: monthly marine metagenomes over a decade; a preprint; MAGs from the same metagenomes; read through a tool summary.
  Evidence: measured; a single source; rated "Weak for gene-level (as opposed to taxon-level) covariation" by the research.
- On the reviewer's reading, neither gene-level network study separates genes that covary because they share a genome, nor corrects for closure, nor conditions on environment; their authors conclude interaction, which the reviewer cannot confirm from the reported analyses. (Arandia-Gorostidi et al. 2025; Zhou et al. 2010)
  Holds for: the GeoChip and KO networks.
  Evidence: the reviewer's reading.
- Gene-level (gene or KO) co-occurrence networks controlling for within-genome linkage were not found. (a search result)
  Holds for: routes: Europe PMC REST keyword searches, Crossref, OpenAlex, PMC full text, three independent search angles; WebSearch and Scholar Gateway unavailable.
  Evidence: a search result.
  Searched for and not found.

### shared ancestry (phylogeny) of the organisms carrying functions

Builds on: co-occurrence and association networks, and what their edges indicate.

- Phylogeny is the largest single predictor of pairwise co-occurrence among the indices tested. (Kamneva 2017)
  Holds for: one study, which reuses Levy & Borenstein's gut data and tested only four genomic indices.
  Evidence: a single source.
- Co-occurring and positively associated taxa are phylogenetically close and functionally similar. (Chaffron et al. 2010; Faust et al. 2012)
  Holds for: taxa.
- At the community level, distance on the first two genomic trait axes correlated with UniFrac distance (R2 = 0.32; 0.46 below median genome size, 0.15 above). (Piton et al. 2023)
  Holds for: community-level genomic trait axes from 128 soil metagenomes; the critic could not recheck R2 = 0.32 (open copies returned HTML).
  Evidence: limited by access (a source was not read in full; not the same as weak evidence).
- All 11 genomic traits across about 18,000 genomes carry phylogenetic signal. (Beier et al. 2022)
  Holds for: about 18,000 prokaryote genomes; abstract only.

### artefacts of aggregating unit-level values into community profiles

- A community-aggregated trait value is the species' trait values weighted according to the relative abundance of the species in the community. (Garnier et al. 2004)
  Background, not from the research.
- Community means of randomly assigned species attributes correlate with each other and with richness through repeated co-occurrence alone, with variance explained rising with co-occurrence: aggregation of unit-level values produces correlations among community means. (Hawkins et al. 2017)
  Holds for: trait ecology, non-microbial; abstract only.
  Evidence: modelled.
- Standard tests of community-weighted mean versus environment have inflated Type I error that rises as beta diversity falls. (Zeleny 2018)
  Holds for: trait ecology; abstract only, via a bioRxiv preprint abstract.
  Evidence: modelled.
- The fourth-corner approach is proposed as a remedy for community-weighted mean tests. (Peres-Neto et al. 2017)
  Holds for: trait ecology; abstract only.
- Abundance-weighted versus species-weighted aggregation changed the sign of 27% of significant trait-climate results. (Wieczynski et al. 2019)
  Holds for: trait ecology (trait-climate results); abstract only; the figure checked against the abstract by the critic.
  Evidence: measured; a single source.
- In metagenomes, inter-trait relations among community traits have been proposed as indicators of processing artefacts. (Barberan et al. 2012)
  Holds for: microbial metagenomes; abstract only.
- Annotation coverage differs systematically between metagenome sample groups, with more unannotated genes in bare desert soils. (Chen et al. 2021)
  Holds for: soil communities in an arid ecosystem, including bare desert soils; abstract only.
- No microbial study found tests the Hawkins-type aggregation artefact on functional profiles. (a search result)
  Holds for: routes in the note's search record.
  Evidence: a search result.
  Searched for and not found.

### complementarity versus functional overlap (redundancy) among co-occurring organisms

Builds on: co-occurrence and association networks, and what their edges indicate, shared ancestry (phylogeny) of the organisms carrying functions, linkage of genes within genomes.

- Co-occurring 16S lineages mapped to complete genomes had more similar pathway content and genome size than random pairs, beyond phylogeny; the authors read this as competition or habitat sharing rather than cooperation. (Chaffron et al. 2010)
  Holds for: profiles independent of genomes; the critic: 'beyond phylogeny' is not stated in the abstract and the full text could not be reached, so it is unverified, and the review took it at face value.
  Evidence: derived; limited by access (a source was not read in full; not the same as weak evidence).
  A second reader found the search for contrary evidence one-sided.
- In HMP data, positive associations were enriched for phylogenetic and functional similarity, and negative ones for the inverse (dissimilarity). (Faust et al. 2012)
  Holds for: Human Microbiome Project data.
  Evidence: derived.
- Across 154 gut species, co-occurrence correlated with modelled metabolic competition (rho = 0.211) and negatively with modelled complementarity (rho = -0.193); the effects are weak. (Levy and Borenstein 2013)
  Holds for: 154 gut species of the human microbiome; profiles mapped to the same reference genomes; read through a tool summary; the critic could not recheck the rho values (PMC text not retrievable).
  Evidence: modelled; limited by access (a source was not read in full; not the same as weak evidence).
- A reanalysis of the same gut data found phylogeny alone explained 9.84% of pairwise co-occurrence variance and all genomic indices together about 3.81% more; in its combined model both metabolic competition (coefficient -0.013, p = 0.71) and metabolic complementarity (p = 0.14) were non-significant once phylogeny and genome content similarity were included. (Kamneva 2017)
  Holds for: Levy & Borenstein's gut data, so not independent of that study; four genomic indices; figures checked against full text by the critic.
  Evidence: derived.
- So the only reanalysis undercuts Levy & Borenstein's modelled competition (overlap) signal as well as its complementarity signal, which weakens the overlap side; the review reported only the complementarity half. (Kamneva 2017; Levy and Borenstein 2013)
  Holds for: the gut data of Levy & Borenstein and its reanalysis by Kamneva.
  A second reader found the search for contrary evidence one-sided.
- Human microbiome samples had higher functional redundancy than random draws from the body-site species pool; this measures within-sample redundancy against a species-pool null, not pairwise co-occurrence, and is a separate case from the co-occurrence and genome-similarity studies. (Tian et al. 2020)
  Holds for: human microbiome body sites; profiles computed from the same reference genomes, with a reference-free replication; the species-pool null checked by the critic.
  Evidence: derived.
- At the level of small co-occurring groups (pairs to quadruplets, more than 800 communities), modelled resource overlap was barely distinguishable from random while modelled metabolic interaction potential was elevated. (Zelezniak et al. 2015)
  Holds for: modelled; more than 800 communities; the figures read only through a tool summary.
  Evidence: modelled; limited by access (a source was not read in full; not the same as weak evidence).
- Co-occurring groups of up to 40 species polarised into cooperative groups (small genomes, auxotrophies) and competitive groups (large genomes, overlapping requirements, mainly soils); the authors attribute the difference from Levy & Borenstein to scale. The study reanalyses the Chaffron 16S collection. (Machado et al. 2021)
  Holds for: modelled; groups of up to 40 species.
  Evidence: modelled.
- Complementarity among small co-occurring groups rests on one method family: Zelezniak 2015 and Machado 2021 share authors and framework (SMETANA) and count as one line of evidence; removing these Patil group papers would remove nearly all support for complementarity among co-occurring organisms in natural surveys. (Machado et al. 2021; Zelezniak et al. 2015)
  Holds for: modelled small-group analyses; the Zelezniak figures read only through a tool summary.
  Evidence: modelled; a single source; rated "Weak for complementarity at the small-group scale" by the research.
- Pairwise metabolic models predict that cooperative potential peaks at moderate overlap. (Freilich et al. 2011)
  Holds for: modelled; abstract only.
  Evidence: modelled.
- Costless metabolic secretions create broad cross-feeding opportunities. (Pacheco et al. 2019)
  Holds for: modelled; abstract only.
  Evidence: modelled.
- The Black Queen hypothesis predicts complementary gene content for leaky functions. (Morris et al. 2012)
  Holds for: a hypothesis; abstract only.
  Evidence: asserted.
- Among 20 soil isolates in 40 carbon environments, overlap in carbon use predicted competition (68% for the most similar non-identical pairs) and difference predicted facilitation (Spearman 0.75). (Kehe et al. 2021)
  Holds for: in vitro, no community profiles; bears on mechanism, not on covariation across samples; figures checked against full text by the critic.
  Evidence: measured.
- Antagonism rose with metabolic similarity, with a small effect (pseudo-R2 0.015 to 0.032). (Russel et al. 2017)
  Holds for: in vitro bacteria, no community profiles; read through a tool summary.
  Evidence: measured.
- Among tree-hole isolates, most pairwise interactions were net negative (competition dominates). (Foster and Bell 2012)
  Holds for: culturable tree-hole isolates in a single environment; in vitro; abstract only.
  Evidence: measured.
- In vitro results conflict: Kehe 2021 finds positive interactions common, while Foster & Bell 2012 find competition dominant (in a single environment). (Foster and Bell 2012; Kehe et al. 2021)
  Holds for: in vitro isolates; Foster & Bell in a single environment.
  Evidence: measured; contested.
- Whether co-occurrence tracks complementarity is in conflict between Levy & Borenstein 2013 and Zelezniak 2015 with Machado 2021; Machado attributes the difference to scale. (Levy and Borenstein 2013; Machado et al. 2021; Zelezniak et al. 2015)
  Holds for: whole-community gut analysis against small-group analyses.
  Evidence: modelled; contested.
- The complementarity readings rest on genome-derived auxotrophies, whose sensitivity against 36 strains with known auxotrophies was 75.5% (gapseq) and 43.4% (AGORA2) and falls with genome incompleteness, and on annotation gaps. (Price et al. 2018; Starke et al. 2023)
  Holds for: 36 strains with known auxotrophies; modelled with measured validation.
  Evidence: modelled.
- Cautions apply to both sides: the overlap readings rest on co-occurrence inference, which carries the network artefacts and is method-dependent (31.5% shared edges) and poorly validated; the complementarity side's auxotrophy caution is quantified (43.4 to 75.5% sensitivity), but no equivalent error rate is applied to the co-occurrence side when the strength ratings are set; both sides mostly analyse only taxa mappable to reference genomes. (the reviewer's synthesis and the critic's finding)
  Holds for: both sides of the complementarity-overlap question.
  A second reader found the search for contrary evidence one-sided.
- The evidence on complementarity versus overlap splits by scale and by evidence class: at whole-community scale, co-occurrence is associated with genome similarity (overlap), with weak effects; modelled small-group analyses find complementarity. (Chaffron et al. 2010; Faust et al. 2012; Kamneva 2017)
  Holds for: whole-community co-occurrence (Chaffron from its abstract, Faust, Kamneva's genome-content similarity index) against modelled small groups; both sides depend on co-occurrence inference.
  Evidence: derived and modelled; rated "Moderate for the pattern that whole-community co-occurrence associates with overlap" by the research; a second reader disputes this: weak to moderate for overlap, weak for complementarity.
  A second reader found the search for contrary evidence one-sided.
- Removing Chaffron et al. 2010 would leave the overlap pattern supported by Faust 2012, Levy & Borenstein 2013 and Tian 2020. (Faust et al. 2012; Levy and Borenstein 2013; Tian et al. 2020)
  Holds for: the review's single-source sensitivity; the critic: Tian measures within-sample redundancy against a species-pool null, which lowers the bar for replication on the overlap side.
- Not measured: complementarity or overlap measured with community profiles built independently of the genomes analysed and at the gene level; validation of any network edge against measured interactions beyond two species pairs (Das 2018). (Das et al. 2018)
  Holds for: routes as for the sources of covariation (Europe PMC REST keyword searches, Crossref, OpenAlex, PMC full text, three search angles).
  Evidence: search (note: "Routes as in case (a)").
  Searched, not found (note: "routes as in case (a)").
- Cautions on the overlap side: co-occurrence is not interaction, and horizontal transfer is concentrated among co-habitants, which can generate shared gene content without shared ancestry. (Blanchet et al. 2020; Carr et al. 2019; Smillie et al. 2011)
  Holds for: the horizontal-transfer caution rests on one abstract (Smillie 2011) used as a general caution.

### the sources of covariation among functions across community samples

Builds on: linkage of genes within genomes, co-occurrence and association networks, and what their edges indicate, shared response to environment, shared ancestry (phylogeny) of the organisms carrying functions, artefacts of aggregating unit-level values into community profiles.

- Two functions can rise and fall together across community samples because they sit in the same genomes, because different organisms carrying them co-occur, because both respond to the same environmental gradient, because their carriers share ancestry, or because the covariation is manufactured by closure, normalisation, annotation or aggregation. Each of the five sources is named in the literature, by largely separate communities, and almost always for taxa, not for function-by-sample tables. (the reviewer's synthesis of the sources below)
  Holds for: identified mostly for taxa; existence at the taxon level, weak or indirect at the function level.
  Evidence: rated "Moderate for the existence of each source" by the research; a second reader disputes this: moderate for existence at the taxon level, weak or indirect at the function level.
- The existence of closure, method dependence and shared ancestry as sources of covariation is replicated across independent groups, at the taxon level. (the reviewer's synthesis of the sources below)
  Holds for: taxon-level work; the critic narrows the standing to existence at the taxon level.
  Evidence: replicated; rated "Moderate for the existence of each source" by the research; a second reader disputes this: moderate for existence at the taxon level, weak or indirect at the function level.
- The shared-environment source is asserted (Carr 2019, read only through a tool summary) plus one taxon-level measured partition (Deutschmann 2021): much of the environment argument is asserted (perspectives) rather than measured. (Carr et al. 2019; Deutschmann et al. 2021)
  Holds for: taxon-level.
  Evidence: assert (note: "Much of the environment argument is asserted (perspectives) rather than measured"); a single source.
- The existence claims for the sources survive the removal of any one source. (the reviewer's sensitivity check)
  Holds for: the review's single-source sensitivity.
- The artefact sources named are compositional closure, method disagreement (31.5% shared edges), annotation reference choice (65.4% of network variance, for the 16S taxonomy database in taxon networks), weighting choices (27% of sign changes in trait ecology), and aggregation of unit-level values that produces correlations among community means through repeated co-occurrence alone (modelled). (Friedman and Alm 2012; Hawkins et al. 2017; Kishore et al. 2023; Weiss et al. 2016; Wieczynski et al. 2019)
  Holds for: taxon networks and trait ecology; the 65.4% is indirect for function profiles.
- No study found names all five sources for the same function-by-sample table. (a search result)
  Holds for: routes: Europe PMC REST keyword searches, Crossref, OpenAlex, PMC full text, three independent search angles (complementarity, co-occurrence, trait ecology); WebSearch and Scholar Gateway unavailable.
  Evidence: a search result.
  Searched for and not found.
- On the reviewer's reading, microbial work has characterised each covariation source separately, and for taxa; the functional-profile question has been approached from two sides that do not meet: gene-level networks that do not separate sources, and genome-mapped co-occurrence studies that relate pairwise genome similarity to co-occurrence but do not partition covariance among functions. (the reviewer's synthesis)
  Holds for: the review's synthesis argument, unlabelled in the review as the reviewer's reading.
  Evidence: the reviewer's reading.

### within-unit versus between-unit partitions in trait ecology (non-microbial)

- The only measured covariance partitions found are within-unit versus between-unit partitions in trait ecology (plants, non-microbial). (a search result)
  Holds for: non-microbial; species traits, not gene content.
  Evidence: a search result.
  Searched for and not found.
- In California woody plants, the among-community (beta) components of four traits covaried strongly along a moisture gradient while the within-community (alpha) components were largely uncorrelated. (Ackerly and Cornwell 2007)
  Holds for: California woody plants, non-microbial; species traits; abstract only.
- In Alberta grasslands (76 species, 27 communities), 92 to 98% of trait variance was within communities; SLA and specific root length correlated positively within communities and negatively among communities (a sign reversal between the two components); phylogenetic signal was present in nearly all within-community trait components and none of the among-community components; correlations among species means are driven by the within-community component. (Kembel and Cahill 2011)
  Holds for: Alberta grasslands, non-microbial; species traits; rechecked against full text by the reviewer and checked by the critic; removing it would remove the only full-text among-versus-within-community sign reversal.
  Evidence: a single source.
- In plants, Ackerly & Cornwell find among-community covariation dominant while Kembel & Cahill find correlations among species means driven by the within-community component; these are different systems and are not contradictory in the strict sense. (Ackerly and Cornwell 2007; Kembel and Cahill 2011)
  Holds for: California woody plants against Alberta grasslands.
- Along a 705-species Australian transect, leaf traits varied almost independently among species but shifted jointly across sites with temperature, vapour pressure deficit and pH; within-species contributions to geographic variation were under 10% for leaf area and over 90% for chi. (Dong et al. 2020)
  Holds for: Australian transect, 705 species; abstract only; the critic: about trait-environment responses, not axis reversal.
- Plot-level LMA and LDMC showed virtually no variance despite high species turnover. (Messier et al. 2010)
  Holds for: plants; abstract only.
- Intraspecific variation made up 25% of within-community and 32% of among-community trait variance on average across 629 plant communities; this is a variance partition, not a covariance partition, and a within-species versus between-species partition, which differs from the within-community versus among-community partitions. (Siefert et al. 2015)
  Holds for: 629 plant communities; abstract only; figures checked by the critic.
- Frameworks for these partitions include T-statistics and HMSC joint models. (Ovaskainen et al. 2017; Violle et al. 2012)
  Holds for: trait ecology; abstract only.
- A scale-dependent trade-off framework holds that within-species constraints often do not apply across species, and vice versa. (Agrawal 2020)
  Holds for: a framework for organismal biology; abstract only.
  Evidence: asserted.
- The plant partitions are measured and partly replicated but concern species traits, not gene content. (Ackerly and Cornwell 2007; Kembel and Cahill 2011)
  Holds for: plants, non-microbial.
  Evidence: measured.

### partitions of covariation among the sources, with shares and reliability

Builds on: the sources of covariation among functions across community samples, within-unit versus between-unit partitions in trait ecology (non-microbial).

- No study found partitions covariation among functions in community profiles into within-genome linkage, organism co-occurrence, shared environment, shared ancestry and artefact shares; the partitions that exist are of other quantities. (a search result)
  Holds for: metagenomic or genome-derived community profiles; routes as for the sources, plus Europe PMC queries on community-aggregated traits with covariation and trade-off terms and on strain-level versus taxonomic turnover; the critic: the headline absence is stated with appropriate restraint.
  Evidence: a search result; rated "Weak" by the research; a second reader disputes this: Supported.
  Searched for and not found.
- For pairwise co-occurrence of gut taxa, phylogeny explains 9.84% and genomic indices add about 3.81%, so most variance is unexplained; the analysis used Jaccard presence data. (Kamneva 2017)
  Holds for: gut taxa (Levy & Borenstein's data); Jaccard presence data.
  Evidence: derived.
- Handling of turnover, closure and depth in the partitions that exist: Deutschmann used relative abundances with no log-ratio treatment reported in the findings; Kamneva used Jaccard presence data; Piton normalised by annotated reads and log(x+1), with no log-ratio treatment and 5 to 15% of reads annotated. (Deutschmann et al. 2021; Kamneva 2017; Piton et al. 2023)
  Holds for: the three microbial studies; the critic could not recheck Piton's 5 to 15% figure (open copies returned HTML).
  Evidence: limited by access (a source was not read in full; not the same as weak evidence).
- Every microbial partition is a single study with its own (different) denominator, so the shares cannot be pooled. (Deutschmann et al. 2021; Kishore et al. 2023; Kamneva 2017)
  Holds for: the Deutschmann, Kamneva and Kishore partitions.
  Evidence: a single source; rated "Weak" by the research.
- Not measured: any partition of function-by-function covariance in metagenomic or genome-derived community profiles, and any microbial analogue of the Leps-type turnover versus within-taxon decomposition (Leps et al. 2011 itself not obtained). (Leps et al. 2011)
  Holds for: routes as for the sources, plus Europe PMC queries on community-aggregated traits with covariation and trade-off terms, and on strain-level versus taxonomic turnover.
  Evidence: a search result.
  Searched for and not found.
- On the reviewer's reading, trait ecology has the partitioning machinery and shows that within-unit and between-unit covariation can differ in sign and in cause; it has not been applied to metagenomic function in any study found. (the reviewer's synthesis)
  Holds for: trait ecology; metagenomic function.
  Evidence: the reviewer's reading.

### genome-level versus community-level functional axes (microbial)

Builds on: artefacts of aggregating unit-level values into community profiles.

- No study found compares the main axes of functional variation among genomes with those among community profiles using a formal agreement measure (eigenvector angle, Procrustes, congruence coefficient); so no conflicts were found, because no quantitative comparison exists. Not measured: every microbial habitat for a formal axis comparison, and comparisons where community profiles are built from the same genomes versus measured independently. (a search result)
  Holds for: microbial systems; routes: Europe PMC queries on community-aggregated traits, metagenome trait axes and genome-level trait trade-offs, citation follow-up from Piton 2023 and Westoby 2021, three independent search angles; the critic: the headline absence is stated with appropriate restraint.
  Evidence: a search result; rated "Absent as direct evidence" by the research; a second reader disputes this: Supported.
  Searched for and not found.
- The nearest precedent: across 128 soil metagenomes, the first two co-inertia axes captured 29% and 21% of community genomic trait variation, the first running from streamlined to large, metabolically expanded genomes (average genome size R2 = 0.64); the authors say this is consistent with isolate-based trait axes without testing it (the abstract says the two dimensions 'support previous theoretical and isolate-based studies'), and state that community-aggregated patterns 'do not directly inform on the within-organism tradeoffs'. Removing this study leaves only the Gralka enrichment-community comparison as a microbial precedent. (Piton et al. 2023)
  Holds for: 128 soil metagenomes; profiles metagenomic and independent of the isolate genomes; read-based annotation of 5 to 15% of reads; no log-ratio treatment; the critic could not recheck the figures (open copies returned HTML; the abstract confirms only the qualitative claim).
  Evidence: measured; a single source; limited by access (a source was not read in full; not the same as weak evidence).
- The same paper asserts that community-average rRNA copy number varies less than isolate values, a compression that would change loadings between levels; this and the authors' own caveat cut against reading the qualitative agreement as axis identity. (Piton et al. 2023)
  Holds for: soil metagenomes against isolates.
  Evidence: asserted.
- A genome-level sugar-versus-acid catabolic axis derived from 186 isolates was carried to enrichment communities, finding the corresponding GC signature (lower GC in sugar-enriched communities, p < 1e-5): qualitative agreement with no axis statistic. (Gralka et al. 2022; Gralka et al. 2023)
  Holds for: 186 isolates and enrichment communities; the preprint read through a tool summary of full text, the published version abstract only.
  Evidence: limited by access (a source was not read in full; not the same as weak evidence).
- Across bacteria and archaea, growth rate, genome size and cell size are near-independent: pairwise r2 is at most 0.012 (maximum 0.0121, genome size versus cell diameter); the paper also reports a weak nonlinearity (about 6% of variance) and habitat effects (about 11%), which qualify 'near-independent'. (Westoby et al. 2021)
  Holds for: genome-level reference axes; pairwise values confirmed against full text by the critic.
- Across about 18,000 genomes, trait relations reverse with genome size, above about 5 Mb. (Beier et al. 2022)
  Holds for: about 18,000 prokaryote genomes; abstract only, though the critic notes a PMC full text exists (PMC9634001) and is load-bearing as a genome-level reference axis.
- Growth-related genome traits are strongly correlated and have been used to read metagenomes. (Vieira-Silva and Rocha 2010)
  Holds for: genomes and metagenomes; abstract only.
- Community-only functional axes exist: NMF of ocean metagenome protein families, without a genome-level comparison. (Jiang et al. 2012)
  Holds for: ocean metagenomes; abstract only.
- By modelling on profiles built from the same genomes, how genes are distributed across genomes (functional redundancy) governs how community functional profiles respond to taxonomic perturbation (predicted versus observed shifts r = 0.86, n = 8): a modelled, indirect link. (Eng and Borenstein 2018)
  Holds for: profiles built from the same genomes; modelled; the critic could not recheck r = 0.86, n = 8.
  Evidence: modelled.
- Functional shifts decomposed into taxon contributions show that the contributing taxa vary markedly between functions. (Manor and Borenstein 2017)
  Holds for: human microbiome; abstract only; annotated in the reference list, not cited in the body.
- The nearest microbial precedents for a genome-level versus community-level axis comparison are single studies with qualitative comparisons. (Gralka et al. 2022; Piton et al. 2023)
  Holds for: Piton 2023 and the Gralka enrichment communities.
  Evidence: a single source; rated "Absent as direct evidence" by the research.

### species-level versus community-level trait axes in plants (non-microbial analogues)

Builds on: within-unit versus between-unit partitions in trait ecology (non-microbial).

- The two main community-mean trait axes across more than 1.1 million plots (stature, resource acquisitiveness) 'reflect the trade-offs at the species level'; the community means are computed from the same species' database trait values, so not independent, and the abstract gives no agreement statistic; the paper itself notes the prior expectation of decoupling. The positive-agreement reading rests on this study alone; removing it leaves only disagreement or sign-reversal cases. (Bruelheide et al. 2018)
  Holds for: plant communities, more than 1.1 million plots; abstract only; species-level trade-offs versus community-mean axes.
  Evidence: a single source; rated "Weak for the positive agreement claim, which rests on one abstract" by the research.
- The species-level reference axes are the two-dimensional global spectrum of plant form and function and the leaf economics spectrum. (Diaz et al. 2016; Wright et al. 2004)
  Holds for: plants; abstract only.
- Some leaf-economics correlations reverse sign within versus across species. (Anderegg et al. 2018)
  Holds for: plants; within-species versus across-species; abstract only.
- Area-based leaf traits scale with LMA within species but not across species, for different mechanistic reasons (mass-proportional versus area-proportional variation within versus across species). (Osnas et al. 2018)
  Holds for: plants; within-species versus across-species.
- Correlation strength only bounds how dissimilar cross-scale trait structures can be. (Messier et al. 2017)
  Holds for: the leaf economic spectrum across scales, including local scales; abstract only.
- That correlation strength only bounds cross-scale dissimilarity may reconcile the global agreement with the local or within-species disagreements, on the reviewer's reading. (Messier et al. 2017)
  Holds for: the reviewer's reading, labelled as such; the critic: acceptable, and no research-design evaluation was found.
  Evidence: the reviewer's reading.
- The one quantitative cross-level agreement measure found is eigenvector angles and eigenvalue ratios with permutation tests, used to show that including intraspecific variation rotates leaf trait axes. (Puglielli et al. 2024; Puglielli et al. 2025)
  Holds for: plant leaf traits; within-species versus across-species.
- The plant analogues are three different partitions, kept apart: (i) species-level trade-offs versus community-mean axes (Bruelheide 2018, abstract only, which states agreement qualitatively); (ii) within-community versus among-community components (Kembel & Cahill, full text; Ackerly & Cornwell, abstract); (iii) within-species versus across-species (Anderegg, abstract; Osnas, full text; Puglielli, eigenvector angles). Evidence that cross-level structure can differ comes from (ii) and (iii), not from the species-versus-community-mean comparison closest to the genome-versus-community question; for (i) the only evidence is a single abstract, and it reports agreement. (Ackerly and Cornwell 2007; Anderegg et al. 2018; Bruelheide et al. 2018; Kembel and Cahill 2011; Osnas et al. 2018; Puglielli et al. 2024; Puglielli et al. 2025)
  Holds for: plants, non-microbial.
  Evidence: rated "Partly supported" by the research; a second reader disputes this: three different partitions are merged and should be kept apart.
- In plants, cross-level axis agreement is not guaranteed and can reverse in sign, in within-community versus among-community and within-species versus across-species partitions. (Anderegg et al. 2018; Kembel and Cahill 2011; Osnas et al. 2018)
  Holds for: plant datasets; the critic: the review's 'replicated across independent plant datasets' mixes partition types.
  Evidence: rated "Moderate that cross-level axis agreement is not guaranteed and can reverse in sign" by the research; a second reader disputes this: the replication across independent plant datasets mixes partition types.
- Not measured: quantitative agreement statistics for species-level versus community-mean axes at global scale. (a search result)
  Holds for: plants, global scale.
  Evidence: a search result.
  The research does not say whether this was searched for.
- Animal trait analogues (and quantitative-genetic and morphometric analogues) of within- versus between-unit covariance partitions were not searched; the review reports animal analogues as not found in the routes used. (a search result)
  Holds for: animal trait ecology; quantitative genetics (G-matrix versus divergence); morphometrics (static versus evolutionary allometry).
  Evidence: a search result.
  Not searched for.
- Over 150 grassland plots, the first principal component across guild-level slow-fast axes explained 25% of combined variation, but no species-level versus community-level axis comparison was found in the paper, and the note did not enter it as a finding. (Neyret et al. 2024)
  Holds for: 150 grassland plots; listed under the note's sources not obtained, though its full text XML was obtained and grepped.

## Do not say

Wordings the research itself says are wrong or overstated, each with the reason and what to say instead.

- Do not write: "Taxon co-occurrence networks have been built in quantity (Barberán 2012; Faust 2012; Fierer et al. 2014)."
  Why: Fierer, Barberán & Laughlin 2014 is a community-aggregated-traits perspective, not a co-occurrence network study; the citation is misattributed, although its metadata is correct.
  Say instead: Taxon association (co-occurrence) networks are built in quantity, but benchmarks limit what their edges can indicate. (Barberan et al. 2012; Faust et al. 2012; Levy and Borenstein 2013)
  Holds for: taxon networks, not functions; the critic removed Fierer et al. 2014 from the list of network studies (a community-aggregated-traits perspective, not a network study).
- Do not write: "Annotation dominates pipelines: annotation reference choice accounts for 65.4% of the variance in function profiles."
  Why: The 65.4% is the 16S taxonomy database's share of variance among taxon networks (Kishore 2023 alone); it concerns taxonomic, not functional, annotation and says nothing directly about functional annotation schemes.
  Say instead: Among taxon co-occurrence networks inferred from amplicon data, the 16S reference (taxonomy) database contributed 65.4% of the variance among inferred networks and OTU processing 26.8%; this concerns taxonomic, not functional, annotation, so it is indirect for function profiles. (Kishore et al. 2023)
  Holds for: taxon networks (16S); the annotation-artefact magnitude rests on this study alone; figures checked against full text by the critic; says nothing directly about functional annotation schemes.
  Evidence: measured; a single source.
- Do not write: "Kamneva's reanalysis found complementarity non-significant once phylogeny is included, while the competition signal stands."
  Why: The same combined model makes metabolic competition non-significant too (coefficient -0.013, p = 0.71); only the result against complementarity was carried into the review, so the overlap side escaped the same reanalysis.
  Say instead: A reanalysis of the same gut data found phylogeny alone explained 9.84% of pairwise co-occurrence variance and all genomic indices together about 3.81% more; in its combined model both metabolic competition (coefficient -0.013, p = 0.71) and metabolic complementarity (p = 0.14) were non-significant once phylogeny and genome content similarity were included. (Kamneva 2017)
  Holds for: Levy & Borenstein's gut data, so not independent of that study; four genomic indices; figures checked against full text by the critic.
  Evidence: derived.
  Say instead: So the only reanalysis undercuts Levy & Borenstein's modelled competition (overlap) signal as well as its complementarity signal, which weakens the overlap side; the review reported only the complementarity half. (Kamneva 2017; Levy and Borenstein 2013)
  Holds for: the gut data of Levy & Borenstein and its reanalysis by Kamneva.
  A second reader found the search for contrary evidence one-sided.
- Do not write: "That whole-community co-occurrence associates with functional overlap is replicated across independent groups, at moderate strength."
  Why: The overlap side rests on co-occurrence inference, which the review itself shows to be method-dependent (31.5% shared edges) and poorly validated; the critic rates it weak to moderate.
  Say instead: The evidence on complementarity versus overlap splits by scale and by evidence class: at whole-community scale, co-occurrence is associated with genome similarity (overlap), with weak effects; modelled small-group analyses find complementarity. (Chaffron et al. 2010; Faust et al. 2012; Kamneva 2017)
  Holds for: whole-community co-occurrence (Chaffron from its abstract, Faust, Kamneva's genome-content similarity index) against modelled small groups; both sides depend on co-occurrence inference.
  Evidence: derived and modelled; rated "Moderate for the pattern that whole-community co-occurrence associates with overlap" by the research; a second reader disputes this: weak to moderate for overlap, weak for complementarity.
  A second reader found the search for contrary evidence one-sided.
- Do not write: "Tian 2020 replicates the co-occurrence pattern of functional overlap."
  Why: Tian 2020 measures within-sample redundancy against a species-pool null, not pairwise co-occurrence; counting it as replication lowers the bar on the overlap side.
  Say instead: Human microbiome samples had higher functional redundancy than random draws from the body-site species pool; this measures within-sample redundancy against a species-pool null, not pairwise co-occurrence, and is a separate case from the co-occurrence and genome-similarity studies. (Tian et al. 2020)
  Holds for: human microbiome body sites; profiles computed from the same reference genomes, with a reference-free replication; the species-pool null checked by the critic.
  Evidence: derived.
- Do not write: "Linkage is not uniform across functions: for sequential redox pathways, within-genome linkage is weak and pathway completion is distributed across organisms."
  Why: This generalises from one aquifer study (Anantharaman 2016) to a class of functions.
  Say instead: In 2,540 aquifer genomes, most organisms carried one step of sequential redox pathways, few carried two, and very few three or more; the authors argue incompleteness does not explain this (stepwise division of redox pathways across aquifer genomes). (Anantharaman et al. 2016)
  Holds for: one aquifer system; community composition and genomes from the same metagenomes; the critic: one aquifer study, not evidence for a class of functions.
  Evidence: derived; a single source.
- Do not write: "Horizontal transfer, concentrated among co-habitants, is a general caution on readings of functional overlap."
  Why: The 25-fold figure and its structuring by habitat rest on one abstract (Smillie 2011), yet the answers use it as a general caution on the overlap side.
  Say instead: Horizontal transfer is 25-fold more frequent among human-associated bacteria than among ecologically diverse non-human isolates, and is structured by shared habitat. (Smillie et al. 2011)
  Holds for: human-associated bacteria against ecologically diverse non-human isolates; abstract only; the critic: one study, used in the answers as a general caution on the overlap side.
  Evidence: derived; a single source.
  Say instead: Cautions on the overlap side: co-occurrence is not interaction, and horizontal transfer is concentrated among co-habitants, which can generate shared gene content without shared ancestry. (Blanchet et al. 2020; Carr et al. 2019; Smillie et al. 2011)
  Holds for: the horizontal-transfer caution rests on one abstract (Smillie 2011) used as a general caution.
- Do not write: "Environmental heterogeneity is usually the strongest driver of correlation structure."
  Why: This rests on Carr 2019 alone, which asserts it and was read only through a tool summary; the one measured partition (Deutschmann 2021) is for taxa.
  Say instead: Environmental heterogeneity is argued to be usually the strongest driver of correlation structure; named as such, the shared-environment source is asserted. (Carr et al. 2019)
  Holds for: asserted; read only through a tool summary.
  Evidence: asserted; a single source.
  Say instead: The one quantitative partition of environmental effects found is for taxa: in a 10-year monthly marine association network of 29,820 edges, four methods classified 8.3% (the intersection of the four) to 24.8%, 25.7% and 84.6% (individual methods) of edges as environmentally driven; in simulation the individual methods removed 38 to 86% of true interactions along with environmental edges, and the intersection approach also removed 25%. It is the only quantitative environmental-share partition for microbial associations; removing it leaves only asserted statements. (Deutschmann et al. 2021)
  Holds for: taxon association edges in one 10-year monthly marine time series; relative abundances with no log-ratio treatment reported in the findings; the share is limited to measured environmental factors; figures rechecked against full text by the reviewer and by the critic.
  Evidence: measured and modelled; a single source.
- Do not write: "Phylogeny is the largest single predictor of pairwise co-occurrence."
  Why: This rests on Kamneva 2017 alone, which reuses Levy & Borenstein's gut data and tested only four genomic indices.
  Say instead: Phylogeny is the largest single predictor of pairwise co-occurrence among the indices tested. (Kamneva 2017)
  Holds for: one study, which reuses Levy & Borenstein's gut data and tested only four genomic indices.
  Evidence: a single source.
- Do not write: "The literature rarely names more than two sources of covariation in the same study."
  Why: The review asserts this without a source; it is the reviewer's generalisation presented as a property of the field.
  Say instead: Two functions can rise and fall together across community samples because they sit in the same genomes, because different organisms carrying them co-occur, because both respond to the same environmental gradient, because their carriers share ancestry, or because the covariation is manufactured by closure, normalisation, annotation or aggregation. Each of the five sources is named in the literature, by largely separate communities, and almost always for taxa, not for function-by-sample tables. (the reviewer's synthesis of the sources below)
  Holds for: identified mostly for taxa; existence at the taxon level, weak or indirect at the function level.
  Evidence: rated "Moderate for the existence of each source" by the research; a second reader disputes this: moderate for existence at the taxon level, weak or indirect at the function level.
- Do not write: "The functional-profile question has been approached from two sides that do not meet."
  Why: This is the reviewer's synthesis argument, reasonable but not labelled as the reviewer's reading in the review; stated as a finding it presents a reading as evidence.
  Say instead: On the reviewer's reading, microbial work has characterised each covariation source separately, and for taxa; the functional-profile question has been approached from two sides that do not meet: gene-level networks that do not separate sources, and genome-mapped co-occurrence studies that relate pairwise genome similarity to co-occurrence but do not partition covariance among functions. (the reviewer's synthesis)
  Holds for: the review's synthesis argument, unlabelled in the review as the reviewer's reading.
  Evidence: the reviewer's reading.
- Do not write: "Plant ecology has compared species-level and community-level axes with mixed results: Bruelheide 2018 finds agreement at global scale, against the disagreement or sign reversal of Kembel & Cahill 2011, Anderegg 2018 and Osnas 2018."
  Why: This folds three distinct partitions into one comparison; sign reversals from within-species and within-community partitions do not answer the species-versus-community-mean comparison, for which the only evidence is Bruelheide's single abstract, and it reports agreement.
  Say instead: The plant analogues are three different partitions, kept apart: (i) species-level trade-offs versus community-mean axes (Bruelheide 2018, abstract only, which states agreement qualitatively); (ii) within-community versus among-community components (Kembel & Cahill, full text; Ackerly & Cornwell, abstract); (iii) within-species versus across-species (Anderegg, abstract; Osnas, full text; Puglielli, eigenvector angles). Evidence that cross-level structure can differ comes from (ii) and (iii), not from the species-versus-community-mean comparison closest to the genome-versus-community question; for (i) the only evidence is a single abstract, and it reports agreement. (Ackerly and Cornwell 2007; Anderegg et al. 2018; Bruelheide et al. 2018; Kembel and Cahill 2011; Osnas et al. 2018; Puglielli et al. 2024; Puglielli et al. 2025)
  Holds for: plants, non-microbial.
  Evidence: rated "Partly supported" by the research; a second reader disputes this: three different partitions are merged and should be kept apart.
- Do not write: "That cross-level axis agreement can reverse in sign is replicated across independent plant datasets."
  Why: The 'replicated across independent plant datasets' strength mixes partition types (within-community versus among-community and within-species versus across-species).
  Say instead: In plants, cross-level axis agreement is not guaranteed and can reverse in sign, in within-community versus among-community and within-species versus across-species partitions. (Anderegg et al. 2018; Kembel and Cahill 2011; Osnas et al. 2018)
  Holds for: plant datasets; the critic: the review's 'replicated across independent plant datasets' mixes partition types.
  Evidence: rated "Moderate that cross-level axis agreement is not guaranteed and can reverse in sign" by the research; a second reader disputes this: the replication across independent plant datasets mixes partition types.
- Do not write: "Dong 2020 shows trait axes reversing between levels."
  Why: Dong 2020 is about trait-environment responses (variation along gradients), not about axis reversal or an axis comparison.
  Say instead: Along a 705-species Australian transect, leaf traits varied almost independently among species but shifted jointly across sites with temperature, vapour pressure deficit and pH; within-species contributions to geographic variation were under 10% for leaf area and over 90% for chi. (Dong et al. 2020)
  Holds for: Australian transect, 705 species; abstract only; the critic: about trait-environment responses, not axis reversal.
- Do not write: "Intraspecific variation accounts for 25% of within-community and 32% of among-community trait covariance."
  Why: The Siefert figures are a variance partition, not a covariance partition, and a within-species versus between-species partition, which differs from the within-community versus among-community partitions beside which the answer lists it.
  Say instead: Intraspecific variation made up 25% of within-community and 32% of among-community trait variance on average across 629 plant communities; this is a variance partition, not a covariance partition, and a within-species versus between-species partition, which differs from the within-community versus among-community partitions. (Siefert et al. 2015)
  Holds for: 629 plant communities; abstract only; figures checked by the critic.
- Do not write: "Growth rate, genome size and cell size are near-independent (r2 at most 0.012)."
  Why: The pairwise values are right, but the paper also reports a weak nonlinearity (about 6% of variance) and habitat effects (about 11%), which qualify 'near-independent'; the review states 'near-independent' without them.
  Say instead: Across bacteria and archaea, growth rate, genome size and cell size are near-independent: pairwise r2 is at most 0.012 (maximum 0.0121, genome size versus cell diameter); the paper also reports a weak nonlinearity (about 6% of variance) and habitat effects (about 11%), which qualify 'near-independent'. (Westoby et al. 2021)
  Holds for: genome-level reference axes; pairwise values confirmed against full text by the critic.
- Do not write: "In simulation, only the individual methods removed true interactions (38 to 86%)."
  Why: The review omits that the intersection approach also removed 25% of true interactions.
  Say instead: The one quantitative partition of environmental effects found is for taxa: in a 10-year monthly marine association network of 29,820 edges, four methods classified 8.3% (the intersection of the four) to 24.8%, 25.7% and 84.6% (individual methods) of edges as environmentally driven; in simulation the individual methods removed 38 to 86% of true interactions along with environmental edges, and the intersection approach also removed 25%. It is the only quantitative environmental-share partition for microbial associations; removing it leaves only asserted statements. (Deutschmann et al. 2021)
  Holds for: taxon association edges in one 10-year monthly marine time series; relative abundances with no log-ratio treatment reported in the findings; the share is limited to measured environmental factors; figures rechecked against full text by the reviewer and by the critic.
  Evidence: measured and modelled; a single source.
- Do not write: "Zelezniak 2015, Levy & Borenstein 2013, Russel 2017, Carr 2019, Arandia-Gorostidi 2025 and the Gralka preprint were read in full text."
  Why: They were read through web-fetch tool summaries ('FT-s'), which are not one of the protocol's access categories and are closer to secondary; the review's own legend says their quotes are to be rechecked.
- Do not write: "Gene-level networks show interactions among the populations carrying the genes."
  Why: That is their authors' conclusion; the reviewer cannot confirm it from the reported analyses, which neither separate genes that share a genome, nor correct for closure, nor condition on environment.
  Say instead: On the reviewer's reading, neither gene-level network study separates genes that covary because they share a genome, nor corrects for closure, nor conditions on environment; their authors conclude interaction, which the reviewer cannot confirm from the reported analyses. (Arandia-Gorostidi et al. 2025; Zhou et al. 2010)
  Holds for: the GeoChip and KO networks.
  Evidence: the reviewer's reading.
- Do not write: "In vitro interaction studies show how functions covary across community samples."
  Why: None of these studies involve community profiles; they bear on mechanism, not on covariation across samples.
  Say instead: Among 20 soil isolates in 40 carbon environments, overlap in carbon use predicted competition (68% for the most similar non-identical pairs) and difference predicted facilitation (Spearman 0.75). (Kehe et al. 2021)
  Holds for: in vitro, no community profiles; bears on mechanism, not on covariation across samples; figures checked against full text by the critic.
  Evidence: measured.
- Do not write: "Zelezniak 2015 and Machado 2021 independently show complementarity among co-occurring groups."
  Why: The two papers share authors and framework and should be counted as one line of evidence; the Zelezniak figures were read only through a tool summary.
  Say instead: Complementarity among small co-occurring groups rests on one method family: Zelezniak 2015 and Machado 2021 share authors and framework (SMETANA) and count as one line of evidence; removing these Patil group papers would remove nearly all support for complementarity among co-occurring organisms in natural surveys. (Machado et al. 2021; Zelezniak et al. 2015)
  Holds for: modelled small-group analyses; the Zelezniak figures read only through a tool summary.
  Evidence: modelled; a single source; rated "Weak for complementarity at the small-group scale" by the research.
- Do not write: "Community-level genomic trait axes in soil are the same as the isolate-based genome-level axes (Piton 2023)."
  Why: The authors say the community axes are consistent with isolate-based axes without testing it, and their own caveat and the asserted compression of community-average rRNA copy number cut against reading the qualitative agreement as axis identity.
  Say instead: The nearest precedent: across 128 soil metagenomes, the first two co-inertia axes captured 29% and 21% of community genomic trait variation, the first running from streamlined to large, metabolically expanded genomes (average genome size R2 = 0.64); the authors say this is consistent with isolate-based trait axes without testing it (the abstract says the two dimensions 'support previous theoretical and isolate-based studies'), and state that community-aggregated patterns 'do not directly inform on the within-organism tradeoffs'. Removing this study leaves only the Gralka enrichment-community comparison as a microbial precedent. (Piton et al. 2023)
  Holds for: 128 soil metagenomes; profiles metagenomic and independent of the isolate genomes; read-based annotation of 5 to 15% of reads; no log-ratio treatment; the critic could not recheck the figures (open copies returned HTML; the abstract confirms only the qualitative claim).
  Evidence: measured; a single source; limited by access (a source was not read in full; not the same as weak evidence).
  Say instead: The same paper asserts that community-average rRNA copy number varies less than isolate values, a compression that would change loadings between levels; this and the authors' own caveat cut against reading the qualitative agreement as axis identity. (Piton et al. 2023)
  Holds for: soil metagenomes against isolates.
  Evidence: asserted.
- Do not write: "The plant results show how genome-level and community-level functional axes relate in microbes."
  Why: Transferring the plant results to microbes would be an inference, not evidence.
- Do not write: "Taxon co-occurrence networks show that co-occurrence of organisms is a source of covariation among functions."
  Why: Taxon (16S) co-occurrence networks are a different measurement type standing in for function-level covariation, which the review only partly acknowledges.
  Say instead: Two functions can rise and fall together across community samples because they sit in the same genomes, because different organisms carrying them co-occur, because both respond to the same environmental gradient, because their carriers share ancestry, or because the covariation is manufactured by closure, normalisation, annotation or aggregation. Each of the five sources is named in the literature, by largely separate communities, and almost always for taxa, not for function-by-sample tables. (the reviewer's synthesis of the sources below)
  Holds for: identified mostly for taxa; existence at the taxon level, weak or indirect at the function level.
  Evidence: rated "Moderate for the existence of each source" by the research; a second reader disputes this: moderate for existence at the taxon level, weak or indirect at the function level.
  Say instead: Taxon association (co-occurrence) networks are built in quantity, but benchmarks limit what their edges can indicate. (Barberan et al. 2012; Faust et al. 2012; Levy and Borenstein 2013)
  Holds for: taxon networks, not functions; the critic removed Fierer et al. 2014 from the list of network studies (a community-aggregated-traits perspective, not a network study).
- Do not write: "Compositionally aware methods remove closure artefacts."
  Why: Their own papers say yes, but an independent simulation found they did no better than Pearson correlation; the review calls this a genuine conflict that is not resolved.
  Say instead: Whether compositionally aware methods remove closure artefacts is a conflict: they beat other methods in their own benchmarks, but in an independent population-dynamics simulation they did no better than Pearson correlation, and recovered competition better than predator-prey relations; the conflict is not resolved. (Hirano and Takemoto 2019; Kurtz et al. 2015)
  Holds for: the methods' own benchmarks (abstract) against one independent simulation.
  Evidence: contested.
- Do not write: "Gene co-abundance binning gives replicated evidence that gene covariation across metagenomes is structured by genome membership."
  Why: Within-genome linkage at gene level rests on one abstract (Nielsen 2014: 7,381 co-abundance groups, 741 metagenomic species, 396 gut metagenomes), which reports no covariance share.
  Say instead: Gene covariation across metagenomes is organised by genome membership in gene co-abundance binning: across 396 human gut metagenomes, genes clustered into 7,381 co-abundance groups, including 741 metagenomic species, from which 238 high-quality genomes were assembled; no share of total gene covariation attributable to genome membership is reported. (MetaHIT et al. 2014)
  Holds for: 396 human gut metagenomes; read in the abstract only; the within-genome-linkage evidence at gene level rests on this one abstract; the counts were checked against the abstract by the critic.
  Evidence: measured; a single source.
- Do not write: "Ackerly & Cornwell and Kembel & Cahill contradict each other on whether among-community or within-community covariation dominates."
  Why: They are different systems and, in the review's words, not contradictory in the strict sense.
  Say instead: In plants, Ackerly & Cornwell find among-community covariation dominant while Kembel & Cahill find correlations among species means driven by the within-community component; these are different systems and are not contradictory in the strict sense. (Ackerly and Cornwell 2007; Kembel and Cahill 2011)
  Holds for: California woody plants against Alberta grasslands.

## Gaps

What the research did not establish.

- Phylogenetic profiling of gene co-occurrence across genomes, and pangenome gene co-occurrence or avoidance (the Pellegrini et al. 1999 lineage; pangenome co-occurrence tools such as Coinfinder), an explicit related-work item in the brief on which the review contains nothing, not even a not-found with routes.
  Not searched for.
- Partition of community functional variation into taxonomic turnover versus within-taxon change for metagenomic or metatranscriptomic function profiles; Salazar et al. 2019 (Cell), separating gene-expression change from community turnover in the ocean metatranscriptome, is the obvious candidate.
  The research does not say whether this was searched for.
- Covariation of functions or pathways with environment across metagenomes using function-level data rather than taxa (e.g., Gianoulis et al. 2009 PNAS canonical correlation of pathways with ocean environment; Raes et al. 2011 Mol Syst Biol; Fierer et al. 2012 PNAS cross-biome soil metagenomes).
  The research does not say whether this was searched for.
- Normalisation and sequencing-depth handling for gene-abundance profiles: average genome size correction, single-copy-gene normalisation (e.g., MUSiCC, Manor & Borenstein 2015), and comparisons of normalisation methods for metagenomic gene abundances (e.g., Pereira et al. 2018 BMC Genomics); the artefact section covers only closure in taxon data.
  The research does not say whether this was searched for.
- Functional annotation-scheme artefacts (KEGG versus COG versus eggNOG or Pfam, annotation rate differences between samples); the only magnitude given is for a 16S taxonomy database.
  The research does not say whether this was searched for.
- Contamination and chimerism in MAGs that bear on measured within-genome linkage (e.g., Shaiber & Eren 2019 mBio on composite MAGs; GUNC chimerism estimates; CheckM); the review says no source was found that quantifies contamination effects on linkage.
  Searched for and not found.
- Gene co-abundance binning beyond one abstract (e.g., Qin et al. 2012 metagenomic linkage groups; MSPminer; CONCOCT and other differential-coverage binning); none was checked for reported shares of gene covariance explained by bin membership.
  The research does not say whether this was searched for.
- Community profiles predicted from reference genomes versus measured metagenomes (PICRUSt, Langille 2013; PICRUSt2, Douglas 2020; Tax4Fun), which report agreement statistics between genome-built and independently measured function profiles; this bears on the brief's requirement that profiles be built from the same genomes or measured independently.
  The research does not say whether this was searched for.
- Within-unit versus between-unit covariance comparisons in evolutionary quantitative genetics and morphometrics, where formal agreement measures (Krzanowski subspace comparison, vector correlations, random skewers) were developed: G-matrix versus among-population divergence (Schluter 1996 'lines of least resistance'), static versus evolutionary allometry.
  Not searched for.
- Animal trait ecology analogues (e.g., fish, birds, invertebrates: community-weighted means versus species-level trait axes), reported as not found with no routes named beyond the general list.
  Not searched for.
- Taxonomy-function coupling across samples measured with Procrustes or Mantel between taxonomic and functional ordinations (e.g., HMP 2012; Burke et al. 2011 PNAS on Ulva-associated communities assembled by function), the nearest precedents for an ordination agreement measure.
  The research does not say whether this was searched for.
- Genome-level structure of gene content, such as the nestedness of the genome-content network (Tian 2020, cited only for redundancy), not related to community-level axes.
  The research does not say whether this was searched for.
- The stage-2 check was triggered: a targeted follow-up brief on phylogenetic profiling, subspace comparison methods and turnover decompositions, sized separately, because the critic's gaps name partition methods and fields not searched (phylogenetic profiling and pangenome gene co-occurrence; G-matrix and subspace comparison; turnover against within-taxon decomposition; gene co-abundance binning beyond Nielsen 2014; and artefact gaps in gene-abundance normalisation, annotation-scheme effects, MAG chimerism and PICRUSt-type agreement).
  Not searched for.
- A partition of function-by-function covariance in community profiles into within-genome linkage, co-occurrence, environment, ancestry and artefact shares.
  Searched for and not found.
- A formal agreement statistic between genome-level and community-level functional axes in any microbial system, with community profiles built from the same genomes and measured independently.
  Searched for and not found.
- A gene or KO co-occurrence network that removes within-genome linkage.
  Searched for and not found.
- A microbial application of the turnover versus within-taxon (Leps-type) decomposition to functional profiles; Leps et al. 2011 itself was not obtained. (Leps et al. 2011)
  Searched for and not found.
- Quantitative agreement statistics for species-level versus community-mean trait axes at global scale.
  The research does not say whether this was searched for.
- Quotes and figures read only through web-fetch tool summaries need rechecking in the original: Levy & Borenstein 2013, Zelezniak 2015, Russel 2017, Carr 2019, Arandia-Gorostidi 2025 and the Gralka preprint; the synthesis agent did not re-open them.
  The research does not say whether this was searched for.
- Figures the critic could not verify for access reasons: Chaffron 2010's 'beyond phylogeny' (not in the abstract; full text blocked), Piton 2023's 29%, 21%, R2 = 0.64, R2 = 0.32 and 5 to 15% of reads annotated (open copies returned HTML), Weiss 2016's 31.5% shared edges, precision 0.2 and effective species about 13 (PMC XML not retrievable), and Eng & Borenstein's r = 0.86, n = 8 and Levy & Borenstein's rho values.
  The research does not say whether this was searched for.
- Beier 2022, load-bearing as a genome-level reference axis, was read in the abstract only, although a PMC full text exists (PMC9634001). (Beier et al. 2022)
  The research does not say whether this was searched for.
- The note contradicts itself on its sources not obtained: the list says nothing beyond a citation was reachable for them and none supports any claim in the review, yet Blanchet 2020, Freilich 2011, Freilich 2018, Goldford 2018 and Lima-Mendez 2015 are also in the reference list as abstract-only sources and are cited in the body; for Lima-Mendez the body says the numbers were not reached. (Blanchet et al. 2020; Freilich et al. 2018; Freilich et al. 2011; Goldford et al. 2018; Lima-Mendez et al. 2015)
  The research does not say whether this was searched for.

## References

- Ackerly, D. D.; Cornwell, W. K. (2007). A trait-based approach to community assembly: partitioning of species trait values into within- and among-community components. Ecology Letters 10(2): 135--145. https://doi.org/10.1111/j.1461-0248.2006.01006.x
- Agrawal, A. A. (2020). A scale-dependent framework for trade-offs, syndromes, and specialization in organismal biology. Ecology 101(2): e02924. https://doi.org/10.1002/ecy.2924
- Anantharaman, K.; Brown, C. T.; Hug, L. A.; Sharon, I.; Castelle, C. J.; Probst, A. J.; Thomas, B. C.; Singh, A.; Wilkins, M. J.; Karaoz, U.; Brodie, E. L.; Williams, K. H.; Hubbard, S. S.; Banfield, J. F. (2016). Thousands of microbial genomes shed light on interconnected biogeochemical processes in an aquifer system. Nature Communications 7: 13219. https://doi.org/10.1038/ncomms13219
- Anderegg, L. D. L.; Berner, L. T.; Badgley, G.; Sethi, M. L.; Law, B. E.; HilleRisLambers, J. (2018). Within-species patterns challenge our understanding of the leaf economics spectrum. Ecology Letters 21(5): 734--744. https://doi.org/10.1111/ele.12945
- Arandia-Gorostidi, N.; Montiel, L.; Latorre, F.; Balague, V.; Gasol, J. M.; Simo, R.; Giner, C. R.; Logares, R. (2025). Metagenomic-based network analysis reveals the importance of vitamin cross-feeding in marine microbial assemblages. bioRxiv. https://doi.org/10.1101/2025.08.08.668683
- Barberan, A.; Bates, S. T.; Casamayor, E. O.; Fierer, N. (2012). Using network analysis to explore co-occurrence patterns in soil microbial communities. The ISME Journal 6(2): 343--351. https://doi.org/10.1038/ismej.2011.119
- Barberan, A.; Fernandez-Guerra, A.; Bohannan, B. J. M.; Casamayor, E. O. (2012). Exploration of community traits as ecological markers in microbial metagenomes. Molecular Ecology 21(8): 1909--1917. https://doi.org/10.1111/j.1365-294X.2011.05383.x
- Beier, S.; Werner, J.; Bouvier, T.; Mouquet, N.; Violle, C. (2022). Trait-trait relationships and tradeoffs vary with genome size in prokaryotes. Frontiers in Microbiology 13: 985216. https://doi.org/10.3389/fmicb.2022.985216
- Berry, D.; Widder, S. (2014). Deciphering microbial interactions and detecting keystone species with co-occurrence networks. Frontiers in Microbiology 5: 219. https://doi.org/10.3389/fmicb.2014.00219
- Blanchet, F. G.; Cazelles, K.; Gravel, D. (2020). Co-occurrence is not evidence of ecological interactions. Ecology Letters 23(7): 1050--1063. https://doi.org/10.1111/ele.13525
- Bruelheide, H.; Dengler, J.; Purschke, O.; Lenoir, J.; Jimenez-Alfaro, B.; Hennekens, S. M.; Botta-Dukat, Z.; Chytry, M.; Field, R.; Jansen, F.; Kattge, J.; Pillar, V. D.; Schrodt, F.; Mahecha, M. D.; Peet, R. K.; Sandel, B.; van Bodegom, P.; Altman, J.; Alvarez-Davila, E.; Arfin Khan, M. A. S.; Attorre, F.; Aubin, I.; Baraloto, C.; Barroso, J. G.; Bauters, M.; Bergmeier, E.; Biurrun, I.; Bjorkman, A. D.; Blonder, B.; Carni, A.; Cayuela, L.; Cerny, T.; Cornelissen, J. H. C.; Craven, D.; Dainese, M.; Derroire, G.; De Sanctis, M.; Diaz, S.; Dolezal, J.; Farfan-Rios, W.; Feldpausch, T. R.; Fenton, N. J.; Garnier, E.; Guerin, G. R.; Gutierrez, A. G.; Haider, S.; Hattab, T.; Henry, G.; Herault, B.; Higuchi, P.; Holzel, N.; Homeier, J.; Jentsch, A.; Jurgens, N.; Kacki, Z.; Karger, D. N.; Kessler, M.; Kleyer, M.; Knollova, I.; Korolyuk, A. Y.; Kuhn, I.; Laughlin, D. C.; Lens, F.; Loos, J.; Louault, F.; Lyubenova, M. I.; Malhi, Y.; Marceno, C.; Mencuccini, M.; Muller, J. V.; Munzinger, J.; Myers-Smith, I. H.; Neill, D. A.; Niinemets U; Orwin, K. H.; Ozinga, W. A.; Penuelas, J.; Perez-Haase, A.; Petrik, P.; Phillips, O. L.; Partel, M.; Reich, P. B.; Romermann, C.; Rodrigues, A. V.; Sabatini, F. M.; Sardans, J.; Schmidt, M.; Seidler, G.; Silva Espejo, J. E.; Silveira, M.; Smyth, A.; Sporbert, M.; Svenning, J. C.; Tang, Z.; Thomas, R.; Tsiripidis, I.; Vassilev, K.; Violle, C.; Virtanen, R.; Weiher, E.; Welk, E.; Wesche, K.; Winter, M.; Wirth, C.; Jandt, U. (2018). Global trait-environment relationships of plant communities. Nature Ecology & Evolution 2(12): 1906--1917. https://doi.org/10.1038/s41559-018-0699-8
- Calcagno, V.; Cunniffe, N.; Hamelin, F. M. (2021). Metacommunity dynamics and the detection of species associations in co-occurrence analyses: why patch disturbance matters. bioRxiv. https://doi.org/10.1101/2021.06.14.448327
- Carr, A.; Diener, C.; Baliga, N. S.; Gibbons, S. M. (2019). Use and abuse of correlation analyses in microbial ecology. The ISME Journal 13(11): 2647--2655. https://doi.org/10.1038/s41396-019-0459-z
- Chaffron, S.; Rehrauer, H.; Pernthaler, J.; von Mering, C. (2010). A global network of coexisting microbes from environmental and whole-genome sequence data. Genome Research 20(7): 947--959. https://doi.org/10.1101/gr.104521.109
- Chen, Y.; Neilson, J. W.; Kushwaha, P.; Maier, R. M.; Barberan, A. (2021). Life-history strategies of soil microbial communities in an arid ecosystem. The ISME Journal 15(3): 649--657. https://doi.org/10.1038/s41396-020-00803-y
- Das, P.; Ji, B.; Kovatcheva-Datchary, P.; Backhed, F.; Nielsen, J. (2018). In vitro co-cultures of human gut bacterial species as predicted from co-occurrence network analysis. PLOS ONE 13(3): e0195161. https://doi.org/10.1371/journal.pone.0195161
- Deutschmann, I. M.; Lima-Mendez, G.; Krabberd, A. K.; Raes, J.; Vallina, S. M.; Faust, K.; Logares, R. (2021). Disentangling environmental effects in microbial association networks. Microbiome 9(1): 232. https://doi.org/10.1186/s40168-021-01141-7
- Diaz, S.; Kattge, J.; Cornelissen, J. H. C.; Wright, I. J.; Lavorel, S.; Dray, S.; Reu, B.; Kleyer, M.; Wirth, C.; Prentice, I. C.; Garnier, E.; Bonisch, G.; Westoby, M.; Poorter, H.; Reich, P. B.; Moles, A. T.; Dickie, J.; Gillison, A. N.; Zanne, A. E.; Chave, J.; Wright, S. J.; Sheremet'ev, S. N.; Jactel, H.; Baraloto, C.; Cerabolini, B.; Pierce, S.; Shipley, B.; Kirkup, D.; Casanoves, F.; Joswig, J. S.; Gunther, A.; Falczuk, V.; Ruger, N.; Mahecha, M. D.; Gorne, L. D. (2016). The global spectrum of plant form and function. Nature 529(7585): 167--171. https://doi.org/10.1038/nature16489
- Dong, N.; Prentice, I. C.; Wright, I. J.; Evans, B. J.; Togashi, H. F.; Caddy-Retalic, S.; McInerney, F. A.; Sparrow, B.; Leitch, E.; Lowe, A. J. (2020). Components of leaf-trait variation along environmental gradients. New Phytologist 228(1): 82--94. https://doi.org/10.1111/nph.16558
- Eng, A.; Borenstein, E. (2018). Taxa-function robustness in microbial communities. Microbiome 6(1): 45. https://doi.org/10.1186/s40168-018-0425-4
- Faust, K. (2021). Open challenges for microbial network construction and analysis. The ISME Journal 15(11): 3111--3118. https://doi.org/10.1038/s41396-021-01027-4
- Faust, K.; Sathirapongsasuti, J. F.; Izard, J.; Segata, N.; Gevers, D.; Raes, J.; Huttenhower, C. (2012). Microbial co-occurrence relationships in the human microbiome. PLoS Computational Biology 8(7): e1002606. https://doi.org/10.1371/journal.pcbi.1002606
- Fierer, N.; Barberan, A.; Laughlin, D. C. (2014). Seeing the forest for the genes: using metagenomics to infer the aggregated traits of microbial communities. Frontiers in Microbiology 5: 614. https://doi.org/10.3389/fmicb.2014.00614
- Foster, K. R.; Bell, T. (2012). Competition, not cooperation, dominates interactions among culturable microbial species. Current Biology 22(19): 1845--1850. https://doi.org/10.1016/j.cub.2012.08.005
- Freilich, M. A.; Wieters, E.; Broitman, B. R.; Marquet, P. A.; Navarrete, S. A. (2018). Species co-occurrence networks: Can they reveal trophic and non-trophic interactions in ecological communities?. Ecology 99(3): 690--699. https://doi.org/10.1002/ecy.2142
- Freilich, S.; Zarecki, R.; Eilam, O.; Shtifman Segal, Ella; Henry, C. S.; Kupiec, M.; Gophna, U.; Sharan, R.; Ruppin, E. (2011). Competitive and cooperative metabolic interactions in bacterial communities. Nature Communications 2: 589. https://doi.org/10.1038/ncomms1597
- Friedman, J.; Alm, E. J. (2012). Inferring correlation networks from genomic survey data. PLoS Computational Biology 8(9): e1002687. https://doi.org/10.1371/journal.pcbi.1002687
- Garnier, Eric; Cortez, Jacques; Billes, Georges; Navas, Marie-Laure; Roumet, Catherine; Debussche, Max; Laurent, Gerard; Blanchard, Alain; Aubry, David; Bellmann, Astrid; Neill, Cathy; Toussaint, Jean-Patrick (2004). Plant Functional Markers Capture Ecosystem Properties During Secondary Succession. Ecology 85(9): 2630--2637. https://doi.org/10.1890/03-0799
- Gloor, Gregory B.; Macklaim, Jean M.; Pawlowsky-Glahn, Vera; Egozcue, Juan J. (2017). Microbiome Datasets Are Compositional: And This Is Not Optional. Frontiers in Microbiology 8: 2224. https://doi.org/10.3389/fmicb.2017.02224
- Goldford, J. E.; Lu, N.; Bajic, D.; Estrela, S.; Tikhonov, M.; Sanchez-Gorostiaga, A.; Segre, D.; Mehta, P.; Sanchez, A. (2018). Emergent simplicity in microbial community assembly. Science 361(6401): 469--474. https://doi.org/10.1126/science.aat1168
- Gralka, M.; Pollak, S.; Cordero, O. X. (2022). Fundamental metabolic strategies of heterotrophic bacteria. bioRxiv. https://doi.org/10.1101/2022.08.04.502823
- Gralka, M.; Pollak, S.; Cordero, O. X. (2023). Genome content predicts the carbon catabolic preferences of heterotrophic bacteria. Nature Microbiology 8(10): 1799--1808. https://doi.org/10.1038/s41564-023-01458-z
- Guseva, K.; Darcy, S.; Simon, E.; Alteio, L. V.; Montesinos-Navarro, A.; Kaiser, C. (2022). From diversity to complexity: Microbial networks in soils. Soil Biology and Biochemistry 169: 108604. https://doi.org/10.1016/j.soilbio.2022.108604
- Hawkins, B. A.; Leroy, B.; Rodriguez MA; Singer, A.; Vilela, B.; Villalobos, F.; Wang, X.; Zeleny, D. (2017). Structural bias in aggregated species-level variables driven by repeated species co-occurrences: a pervasive problem in community and assemblage data. Journal of Biogeography 44(6): 1199--1211. https://doi.org/10.1111/jbi.12953
- Hirano, H.; Takemoto, K. (2019). Difficulty in inferring microbial community structure based on co-occurrence network approaches. BMC Bioinformatics 20(1): 329. https://doi.org/10.1186/s12859-019-2915-1
- Jiang, X.; Langille, M. G. I.; Neches, R. Y.; Elliot, M.; Levin, S. A.; Eisen, J. A.; Weitz, J. S.; Dushoff, J. (2012). Functional biogeography of ocean microbes revealed through non-negative matrix factorization. PLoS ONE 7(9): e43866. https://doi.org/10.1371/journal.pone.0043866
- Kamneva, O. K. (2017). Genome composition and phylogeny of microbes predict their co-occurrence in the environment. PLOS Computational Biology 13(2): e1005366. https://doi.org/10.1371/journal.pcbi.1005366
- Kehe, J.; Ortiz, A.; Kulesa, A.; Gore, J.; Blainey, P. C.; Friedman, J. (2021). Positive interactions are common among culturable bacteria. Science Advances 7(45): eabi7159. https://doi.org/10.1126/sciadv.abi7159
- Kembel, S. W.; Cahill, J. F. (2011). Independent evolution of leaf and root traits within and among temperate grassland plant communities. PLoS ONE 6(6): e19992. https://doi.org/10.1371/journal.pone.0019992
- Kishore, D.; Birzu, G.; Hu, Z.; DeLisi, C.; Korolev, K. S.; Segre, D. (2023). Inferring microbial co-occurrence networks from amplicon data: a systematic evaluation. mSystems 8(4): e00961--22. https://doi.org/10.1128/msystems.00961-22
- Kurtz, Z. D.; Muller, C. L.; Miraldi, E. R.; Littman, D. R.; Blaser, M. J.; Bonneau, R. A. (2015). Sparse and compositionally robust inference of microbial ecological networks. PLOS Computational Biology 11(5): e1004226. https://doi.org/10.1371/journal.pcbi.1004226
- Leps, J.; de Bello, F.; Smilauer, P.; Dolezal, J. (2011). Community trait response to environment: disentangling species turnover vs intraspecific trait variability effects. Ecography 34(5): 856--863. https://doi.org/10.1111/j.1600-0587.2010.06904.x
- Levy, R.; Borenstein, E. (2013). Metabolic modeling of species interaction in the human microbiome elucidates community-level assembly rules. Proceedings of the National Academy of Sciences of the United States of America 110(31): 12804--12809. https://doi.org/10.1073/pnas.1300926110
- Lima-Mendez, G.; Faust, K.; Henry, N.; Decelle, J.; Colin, S.; Carcillo, F.; Chaffron, S.; Ignacio-Espinosa, J. C.; Roux, S.; Vincent, F.; Bittner, L.; Darzi, Y.; Wang, J.; Audic, S.; Berline, L.; Bontempi, G.; Cabello, A. M.; Coppola, L.; Cornejo-Castillo, F. M.; d'Ovidio, F.; De Meester, L.; Ferrera, I.; Garet-Delmas, M. J.; Guidi, L.; Lara, E.; Pesant, S.; Royo-Llonch, M.; Salazar, G.; Sanchez, P.; Sebastian, M.; Souffreau, C.; Dimier, C.; Picheral, M.; Searson, S.; Kandels-Lewis, S.; Tara Oceans coordinators; Gorsky, G.; Not, F.; Ogata, H.; Speich, S.; Stemmann, L.; Weissenbach, J.; Wincker, P.; Acinas, S. G.; Sunagawa, S.; Bork, P.; Sullivan, M. B.; Karsenti, E.; Bowler, C.; de Vargas, C.; Raes, J. (2015). Determinants of community structure in the global plankton interactome. Science 348(6237): 1262073. https://doi.org/10.1126/science.1262073
- Louca, S.; Parfrey, L. W.; Doebeli, M. (2016). Decoupling function and taxonomy in the global ocean microbiome. Science 353(6305): 1272--1277. https://doi.org/10.1126/science.aaf4507
- Machado, D.; Maistrenko, O. M.; Andrejev, S.; Kim, Y.; Bork, P.; Patil, Kaustubh R.; Patil, Kiran R. (2021). Polarization of microbial communities between competitive and cooperative metabolism. Nature Ecology & Evolution 5(2): 195--203. https://doi.org/10.1038/s41559-020-01353-4
- Manor, O.; Borenstein, E. (2017). Systematic characterization and analysis of the taxonomic drivers of functional shifts in the human microbiome. Cell Host & Microbe 21(2): 254--267. https://doi.org/10.1016/j.chom.2016.12.014
- Marsland, R.; Cui, W.; Mehta, P. (2020). A minimal model for microbial biodiversity can reproduce experimentally observed ecological patterns. Scientific Reports 10(1): 3308. https://doi.org/10.1038/s41598-020-60130-2
- Messier, J.; McGill, B. J.; Enquist, B. J.; Lechowicz, M. J. (2017). Trait variation and integration across scales: is the leaf economic spectrum present at local scales?. Ecography 40(6): 685--697. https://doi.org/10.1111/ecog.02006
- Messier, J.; McGill, B. J.; Lechowicz, M. J. (2010). How do traits vary across ecological scales? A case for trait-based ecology. Ecology Letters 13(7): 838--848. https://doi.org/10.1111/j.1461-0248.2010.01476.x
- MetaHIT Consortium; Nielsen, H. B.; Almeida, M.; Juncker, A. S.; Rasmussen, S.; Li, J.; Sunagawa, S.; Plichta, D. R.; Gautier, L.; Pedersen, A. G.; Le Chatelier, E.; Pelletier, E.; Bonde, I.; Nielsen, T.; Manichanh, C.; Arumugam, M.; Batto, J. M.; Quintanilha dos Santos, M. B.; Blom, N.; Borruel, N.; Burgdorf, K. S.; Boumezbeur, F.; Casellas, F.; Dore, J.; Dworzynski, P.; Guarner, F.; Hansen, T.; Hildebrand, F.; Kaas, R. S.; Kennedy, S.; Kristiansen, K.; Kultima, J. R.; Leonard, P.; Levenez, F.; Lund, O.; Moumen, B.; Le Paslier, D.; Pons, N.; Pedersen, O.; Prifti, E.; Qin, J.; Raes, J.; Srensen, S.; Tap, J.; Tims, S.; Ussery, D. W.; Yamada, T.; Renault, P.; Sicheritz-Ponten, T.; Bork, P.; Wang, J.; Brunak, S.; Ehrlich, S. D. (2014). Identification and assembly of genomes and genetic elements in complex metagenomic samples without using reference genomes. Nature Biotechnology 32(8): 822--828. https://doi.org/10.1038/nbt.2939
- Morris, J. J.; Lenski, R. E.; Zinser, E. R. (2012). The Black Queen Hypothesis: evolution of dependencies through adaptive gene loss. mBio 3(2): e00036--12. https://doi.org/10.1128/mBio.00036-12
- Neyret, M.; Le Provost, G.; Boesing, A. L. (2024). A slow-fast trait continuum at the whole community level in relation to land-use intensification. Nature Communications 15: 1251. https://doi.org/10.1038/s41467-024-45113-5
- Osnas, J. L. D.; Katabuchi, M.; Kitajima, K.; Wright, S. J.; Reich, P. B.; Van Bael, S. A.; Kraft, N. J. B.; Samaniego, M. J.; Pacala, S. W.; Lichstein, J. W. (2018). Divergent drivers of leaf trait variation within species, among species, and among functional groups. Proceedings of the National Academy of Sciences of the United States of America 115(21): 5480--5485. https://doi.org/10.1073/pnas.1803989115
- Ovaskainen, O.; Tikhonov, G.; Norberg, A.; Blanchet, F. G.; Duan, L.; Dunson, D.; Roslin, T.; Abrego, N. (2017). How to make more out of community data? A conceptual framework and its implementation as models and software. Ecology Letters 20(5): 561--576. https://doi.org/10.1111/ele.12757
- Pacheco, A. R.; Moel, M.; Segre, D. (2019). Costless metabolic secretions as drivers of interspecies interactions in microbial ecosystems. Nature Communications 10(1): 103. https://doi.org/10.1038/s41467-018-07946-9
- Pascual-Garcia, A.; Tamames, J.; Bastolla, U. (2014). Bacteria dialog with Santa Rosalia: Are aggregations of cosmopolitan bacteria mainly explained by habitat filtering or by ecological interactions?. BMC Microbiology 14(1): 284. https://doi.org/10.1186/s12866-014-0284-5
- Peres-Neto, P. R.; Dray, S.; ter Braak, C. J. F. (2017). Linking trait variation to the environment: critical issues with community-weighted mean correlation resolved by the fourth-corner approach. Ecography 40(7): 806--816. https://doi.org/10.1111/ecog.02302
- Piton, G.; Allison, S. D.; Bahram, M.; Hildebrand, F.; Martiny, J. B. H.; Treseder, K. K.; Martiny, A. C. (2023). Life history strategies of soil bacterial communities across global terrestrial biomes. Nature Microbiology 8(11): 2093--2102. https://doi.org/10.1038/s41564-023-01465-0
- Poggiato, G.; Munkemuller, T.; Bystrova, D.; Arbel, J.; Clark, J. S.; Thuiller, W. (2021). On the interpretations of joint modeling in community ecology. Trends in Ecology & Evolution 36(5): 391--401. https://doi.org/10.1016/j.tree.2021.01.002
- Price, M. N.; Zane, G. M.; Kuehl, J. V.; Melnyk, R. A.; Wall, J. D.; Deutschbauer, A. M.; Arkin, A. P. (2018). Filling gaps in bacterial amino acid biosynthesis pathways with high-throughput genetics. PLOS Genetics 14(1): e1007147. https://doi.org/10.1371/journal.pgen.1007147
- Puglielli, G.; Bricca, A.; Chelli, S.; Petruzzellis, F.; Acosta, A. T. R.; Bacaro, G.; Beccari, E.; Bernardo, L.; Bonari, G.; Bolpagni, R.; Boscutti, F.; Calvia, G.; Campetella, G.; Cancellieri, L.; Canullo, R.; Carbognani, M.; Carboni, M.; Carranza, M. L.; Castellani, M. B.; Ciccarelli, D.; Coppi, A.; Cutini, M.; Dalla Vecchia, A.; Dalle Fratte, M.; de Francesco, M. C.; De Frenne, P.; De Sanctis, M.; de Simone, L.; Di Cecco, V.; Fanelli, G.; Farris, E.; Ferrara, A.; Fenu, G.; Filibeck, G.; Gasperini, C.; Gargano, D.; Kindermann, E.; La Bella, G.; Lastrucci, L.; Lazzaro, L.; Maccherini, S.; Marignani, M.; Mugnai, M.; Naselli-Flores, L.; Passalacqua, N. G.; Pavanetto, N.; Petraglia, A.; Rota, F.; Santoianni, L. A.; Schettino, A.; Selvi, F.; Stanisci, A.; Trotta, G.; Vangansbeke, P.; Varricchione, M.; Vuerich, M.; Wellstein, C.; Tordoni, E. (2024). Intraspecific variability of leaf form and function across habitat types. Ecology Letters 27(3): e14396. https://doi.org/10.1111/ele.14396
- Puglielli, G.; Carmona, C. P.; Bissi, A.; Tordoni, E. (2025). Quantifying the influence of intraspecific variability in trait spaces. npj Biodiversity 4: 36. https://doi.org/10.1038/s44185-025-00101-w
- Russel, J.; Rder, H. L.; Madsen, J. S.; Burmlle, M.; Srensen, S. J. (2017). Antagonism correlates with metabolic similarity in diverse bacteria. Proceedings of the National Academy of Sciences of the United States of America 114(40): 10684--10688. https://doi.org/10.1073/pnas.1706016114
- Siefert, A.; Violle, C.; Chalmandrier, L.; Albert, C. H.; Taudiere, A.; Fajardo, A.; Aarssen, L. W.; Baraloto, C.; Carlucci, M. B.; Cianciaruso, M. V.; Dantas, V. L.; de Bello, F.; Duarte, L. D. S.; Fonseca, C. R.; Freschet, G. T.; Gaucherand, S.; Gross, N.; Hikosaka, K.; Jackson, B.; Jung, V.; Kamiyama, C.; Katabuchi, M.; Kembel, S. W.; Kichenin, E.; Kraft, N. J. B.; Lagerstrom, A.; Le Bagousse-Pinguet, Y.; Li, Y.; Mason, N.; Messier, J.; Nakashizuka, T.; Overton, J. M.; Peltzer, D. A.; Perez-Ramos, I. M.; Pillar, V. D.; Prentice, H. C.; Richardson, S.; Sasaki, T.; Schamp, B. S.; Schob, C.; Shipley, B.; Sundqvist, M.; Sykes, M. T.; Vandewalle, M.; Wardle, D. A. (2015). A global meta-analysis of the relative extent of intraspecific trait variation in plant communities. Ecology Letters 18(12): 1406--1419. https://doi.org/10.1111/ele.12508
- Smillie, C. S.; Smith, M. B.; Friedman, J.; Cordero, O. X.; David, L. A.; Alm, E. J. (2011). Ecology drives a global network of gene exchange connecting the human microbiome. Nature 480(7376): 241--244. https://doi.org/10.1038/nature10571
- Starke, S.; Harris, D. M. M.; Zimmermann, J.; Schuchardt, S.; Oumari, M.; Frank, D.; Bang, C.; Rosenstiel, P.; Schreiber, S.; Frey, N.; Franke, A.; Aden, K.; Waschina, S. (2023). Amino acid auxotrophies in human gut bacteria are linked to higher microbiome diversity and long-term stability. The ISME Journal 17(12): 2370--2380. https://doi.org/10.1038/s41396-023-01537-3
- Tackmann, J.; Matias Rodrigues, J. F.; von Mering, C. (2019). Rapid inference of direct interactions in large-scale ecological networks from heterogeneous microbial sequencing data. Cell Systems 9(3): 286--296.e8. https://doi.org/10.1016/j.cels.2019.08.002
- Tian, L.; Wang, X. W.; Wu, A. K.; Fan, Y.; Friedman, J.; Dahlin, A.; Waldor, M. K.; Weinstock, G. M.; Weiss, S. T.; Liu, Y. Y. (2020). Deciphering functional redundancy in the human microbiome. Nature Communications 11(1): 6217. https://doi.org/10.1038/s41467-020-19940-1
- Vieira-Silva, S.; Rocha, E. P. C. (2010). The systemic imprint of growth and its uses in ecological (meta)genomics. PLoS Genetics 6(1): e1000808. https://doi.org/10.1371/journal.pgen.1000808
- Violle, C.; Enquist, B. J.; McGill, B. J.; Jiang, L.; Albert, C. H.; Hulshof, C.; Jung, V.; Messier, J. (2012). The return of the variance: intraspecific variability in community ecology. Trends in Ecology & Evolution 27(4): 244--252. https://doi.org/10.1016/j.tree.2011.11.014
- Weiss, S.; Van Treuren, W.; Lozupone, C.; Faust, K.; Friedman, J.; Deng, Y.; Xia, L. C.; Xu, Z. Z.; Ursell, L.; Alm, E. J.; Birmingham, A.; Cram, J. A.; Fuhrman, J. A.; Raes, J.; Sun, F.; Zhou, J.; Knight, R. (2016). Correlation detection strategies in microbial data sets vary widely in sensitivity and precision. The ISME Journal 10(7): 1669--1681. https://doi.org/10.1038/ismej.2015.235
- Westoby, M.; Nielsen, D. A.; Gillings, M. R.; Litchman, E.; Madin, J. S.; Paulsen, I. T.; Tetu, S. G. (2021). Cell size, genome size, and maximum growth rate are near-independent dimensions of ecological variation across bacteria and archaea. Ecology and Evolution 11(9): 3956--3976. https://doi.org/10.1002/ece3.7290
- Wieczynski, D. J.; Boyle, B.; Buzzard, V.; Duran, S. M.; Henderson, A. N.; Hulshof, C. M.; Kerkhoff, A. J.; McCarthy, M. C.; Michaletz, S. T.; Swenson, N. G.; Asner, G. P.; Bentley, L. P.; Enquist, B. J.; Savage, V. M. (2019). Climate shapes and shifts functional biodiversity in forests worldwide. Proceedings of the National Academy of Sciences of the United States of America 116(2): 587--592. https://doi.org/10.1073/pnas.1813723116
- Wright, I. J.; Reich, P. B.; Westoby, M.; Ackerly, D. D.; Baruch, Z.; Bongers, F.; Cavender-Bares, J.; Chapin, T.; Cornelissen, J. H. C.; Diemer, M.; Flexas, J.; Garnier, E.; Groom, P. K.; Gulias, J.; Hikosaka, K.; Lamont, B. B.; Lee, T.; Lee, W.; Lusk, C.; Midgley, J. J.; Navas, M. L.; Niinemets U; Oleksyn, J.; Osada, N.; Poorter, H.; Poot, P.; Prior, L.; Pyankov, V. I.; Roumet, C.; Thomas, S. C.; Tjoelker, M. G.; Veneklaas, E. J.; Villar, R. (2004). The worldwide leaf economics spectrum. Nature 428(6985): 821--827. https://doi.org/10.1038/nature02403
- Zeleny, D. (2018). Which results of the standard test for community-weighted mean approach are too optimistic?. Journal of Vegetation Science 29(6): 953--966. https://doi.org/10.1111/jvs.12688
- Zelezniak, A.; Andrejev, S.; Ponomarova, O.; Mende, D. R.; Bork, P.; Patil, K. R. (2015). Metabolic dependencies drive species co-occurrence in diverse microbial communities. Proceedings of the National Academy of Sciences of the United States of America 112(20): 6449--6454. https://doi.org/10.1073/pnas.1421834112
- Zhou, J.; Deng, Y.; Luo, F.; He, Z.; Tu, Q.; Zhi, X. (2010). Functional molecular ecological networks. mBio 1(4): e00169--10. https://doi.org/10.1128/mBio.00169-10
- Zurell, D.; Pollock, L. J.; Thuiller, W. (2018). Do joint species distribution models reliably detect interspecific interactions from co-occurrence data in homogenous environments?. Ecography 41(11): 1812--1819. https://doi.org/10.1111/ecog.03315
