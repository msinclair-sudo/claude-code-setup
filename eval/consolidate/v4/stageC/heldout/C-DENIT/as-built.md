---
type: knowledge
title: Denitrification genes against organism phylogeny, habitat and within-genus variation
inputs:
  - C-DENIT: PhD/Proposal/Research/Results/Denitrification and N2O-reduction genes against organism phylogeny and habitat congruence, habitat association and within-genus variation (literature review).md
refs: PhD/Proposal/Refs/Refs.bib
built: 2026-10-24
status: draft
tags:
  - research
  - knowledge
---
# Denitrification genes against organism phylogeny, habitat and within-genus variation

> [!abstract] Note Role
> **Contains**: what the research in the inputs found, one claim per finding, organised by concept, with the
> standing, conditions and sources the notes give, and links back to where each was verified.
> **Cannot contain**: anything not in the inputs (except background entries, marked), verification (it stays
> in the result notes), or guidance on writing, story or order of telling.
> **Order**: the concepts are listed in one valid ordering of the `needs` graph. It has no narrative meaning;
> other valid orderings are equally correct.

## Inputs
| id | note | critique | citations | standing labels | run record | omission check |
|---|---|---|---|---|---|---|
| C-DENIT | [[Denitrification and N2O-reduction genes against organism phylogeny and habitat congruence, habitat association and within-genus variation (literature review)]] | yes | labelled (access; class; standing) | yes (9 of 22 labels) | no | exact (every labelled sentence, every answer sentence, and the critique) |

## Concepts

### denitrification-genes: the denitrification enzymes and their genes
needs: none
- **denitrification-genes.bg1** Denitrification is a means of energy conservation that uses nitrogen oxides as terminal electron acceptors; its enzymes include two types of respiratory nitrite reductase, nitric oxide reductase and nitrous oxide reductase.
  kind: background · ref: zumftCellBiologyMolecular1997 · check: DOI 10.1128/mmbr.61.4.533-616.1997 resolves on Crossref (Microbiology and Molecular Biology Reviews 61(4): 533-616); both statements are in the abstract (Europe PMC, PMID 9409151)

### evidence-base: the kinds of evidence and how much was read in full
needs: none
- **evidence-base.1** Four kinds of data bear on gene-tree, habitat and within-genus questions, and they rarely overlap: isolate-based PCR surveys from the 2000s that pair amplicons of nirK, nirS, norB, nosZ or narG with 16S rRNA; genome-scale surveys of public assemblies (652 genomes in 2014, about 6973 in the Nir phylogenies of 2024, 61,293 GTDB genomes in 2025); metagenome read placement and MAG studies that assign genes to biomes; and phenotype and genotype studies of strains within one genus that measure gas kinetics.
  conf: not stated · class: not stated · holds: the literature the review covers · src: grafIntergenomicComparisonsHighlight2014, poldPhylogeneticsEnvironmentalDistribution2024, poldDenitrificationCommunityTrait2025 · trail: C-DENIT §1. What · from: C-DENIT:B-0025..0032
- **evidence-base.2** Gene-tree versus organism-tree comparisons come mostly from isolate PCR surveys and genome-scale surveys; habitat associations mostly from genome-scale surveys and metagenome or MAG studies, with habitat assigned from database labels (GOLD, NCBI isolation source), ecoregion by coordinates, or site class; within-genus variation from genome-scale surveys and strain phenotype and genotype studies.
  conf: not stated · class: not stated · holds: the literature the review covers · src: none (the reviewer's synthesis) · trail: C-DENIT §1. What · from: C-DENIT:B-0026..0032
- **evidence-base.3** More of the review's findings rest on abstracts (68) than on full text (58), with one secondary; the synthesis re-opened the full texts of Graf 2014, Pold 2024, Pold 2025, Parsons 2021, Shiina 2014 and Truchon 2023, and other full-text labels come from the search agents.
  conf: not stated · class: not stated · holds: the review's own access count over its findings · src: none (the note's access record) · trail: C-DENIT §Provenance, §Stage 2, §1. What · from: C-DENIT:B-0019, C-DENIT:B-0024, C-DENIT:B-0033, C-DENIT:B-0034

### gene-trees: gene trees against the organism tree, overall
needs: denitrification-genes
- **gene-trees.bg1** A gene tree can differ from the species tree that contains it; the discord can arise from horizontal transfer (including hybridization), lineage sorting, and gene duplication and extinction.
  kind: background · ref: maddisonGeneTreesSpecies1997 · check: DOI 10.1093/sysbio/46.3.523 resolves on Crossref (Systematic Biology 46(3): 523-536); the causes of discord are listed in the abstract (publisher PDF)
- **gene-trees.1** No gene tree tracks the organism tree overall: for the four genes measured with formal or semi-formal comparisons (nirK, nirS, norB, nosZ) the evidence is gene-dependent, method-dependent and mostly qualitative.
  conf: not stated · class: not stated · holds: nirK, nirS, norB and nosZ, the four genes with formal or semi-formal comparisons; the critic's reformulation of the D1 answer · src: none (the reviewer's synthesis, as the critic reformulated it) · trail: C-DENIT §critic, §answers, §8. Answers · from: C-DENIT:C-001, C-DENIT:A-001, C-DENIT:A-004, C-DENIT:A-096
- **gene-trees.2** Quantitative congruence metrics are rare; most statements about gene-tree congruence are qualitative.
  conf: not stated · class: not stated · holds: the congruence literature the review covers · src: none (the reviewer's synthesis) · trail: C-DENIT §answers · from: C-DENIT:A-017, C-DENIT:A-018

### nirk: nirK against the organism tree
needs: gene-trees
- **nirk.1** Among 227 cultivated strains, the nirK phylogeny was incongruent with 16S.
  conf: single (marker) · class: deriv (marker) · holds: 227 cultivated strains, partial amplicons · src: heylenIncidenceNirSNirK2006 (abstract only; derived; single study) · trail: C-DENIT §2.1, §answers · from: C-DENIT:I-0001, C-DENIT:A-005
- **nirk.2** In 43 complete genomes, Jones et al. rejected congruence of nirK with 16S by SH and likelihood tests, and monophyly at family to phylum level was not supported.
  conf: not stated · class: deriv (marker) · holds: 43 complete genomes; the 43-genome figure comes from a search agent and is not in the abstract the synthesis read · src: jonesPhylogeneticAnalysisNitrite2008 (full text per a search agent, abstract checked by me; derived) · trail: C-DENIT §2.1, §Adversarial · limit: access (critic: C-061) · from: C-DENIT:I-0002, C-DENIT:C-060, C-DENIT:C-061, C-DENIT:C-062
- **nirk.3** In 249 genomes, full-length NirK split into two clades with "limited taxonomic coherence": clade I is mainly Alphaproteobacteria, and clade II spans at least nine phyla plus Archaea.
  conf: not stated · class: deriv (marker) · holds: 249 genomes, full-length NirK · src: helenHighlyDiverseNirK2016 (full text per search agent; derived) · trail: C-DENIT §2.1 · from: C-DENIT:B-0038, C-DENIT:B-0039, C-DENIT:I-0003
- **nirk.4** In 652 genomes, the nirK tree showed "no clear correspondence with organismal phylogeny".
  conf: not stated · class: deriv (marker) · holds: Graf 2014's 652 microbial genomes across 18 phyla, which include fungal (Ascomycota) genomes · src: grafIntergenomicComparisonsHighlight2014 (full text, checked; derived) · trail: C-DENIT §2.1, §Adversarial · from: C-DENIT:I-0004, C-DENIT:C-086
- **nirk.5** The introduction of the 2024 Nir survey restates, citing earlier work, that NirS and "particularly NirK" phylogenies are incongruent with 16S.
  conf: not stated · class: not stated · holds: a restatement in Pold 2024's introduction, not its own analysis · src: poldPhylogeneticsEnvironmentalDistribution2024 · trail: C-DENIT §2.1 · from: C-DENIT:B-0040
- **nirk.6** nirK incongruence with 16S is replicated across isolate amplicons (Heylen 2006, abstract only), a formal test on genomes (Jones 2008, which the synthesis did not read; abstract checked) and genome trees judged by eye (Graf 2014, full text; Decleyre 2016, per agent); the review adds the 2024 survey of about 6400 sequences.
  conf: repl (critic: C-001) · class: not stated · holds: partial-amplicon isolates and genome sets of 43, 249 and 652 genomes; often qualitative · src: heylenIncidenceNirSNirK2006 (abstract only), jonesPhylogeneticAnalysisNitrite2008 (abstract checked), grafIntergenomicComparisonsHighlight2014 (full text), helenHighlyDiverseNirK2016 (per agent), poldPhylogeneticsEnvironmentalDistribution2024 · trail: C-DENIT §critic, §answers · rating: "Moderate for nirK" · from: C-DENIT:C-001, C-DENIT:A-005, C-DENIT:A-014

### nirs: nirS against the organism tree
needs: gene-trees
- **nirs.1** Heylen et al. found the nirS phylogeny congruent with 16S at family or genus level, with exceptions.
  conf: not stated · class: not stated · holds: cultivated denitrifiers, partial amplicons · src: heylenIncidenceNirSNirK2006 (abstract only) · trail: C-DENIT §2.2, §answers, §References · from: C-DENIT:B-0048, C-DENIT:A-005, C-DENIT:R-0075
- **nirs.2** Jones et al. found significant topological differences between nirS and 16S trees, and genus-level monophyly was supported only for Paracoccus, Alicycliphilus and Cupriavidus.
  conf: not stated · class: not stated · holds: Jones 2008's genome set · src: jonesPhylogeneticAnalysisNitrite2008 (see access above) · trail: C-DENIT §2.2, §Adversarial · limit: access (critic: C-060) · from: C-DENIT:B-0049, C-DENIT:C-060
- **nirs.3** Graf et al. judged nirS "more congruent to taxonomic affiliation on the phylum level" than nirK and norB.
  conf: not stated · class: not stated · holds: 652 genomes; a qualitative judgement · src: grafIntergenomicComparisonsHighlight2014 (full text, checked) · trail: C-DENIT §2.2, §critic · from: C-DENIT:B-0050, C-DENIT:C-003
- **nirs.4** The literature conflicts on the depth at which nirS congruence holds: family or genus level in one isolate study (Heylen 2006), phylum level in another (Graf 2014), and significant incongruence by topology tests in a third (Jones 2008); the reconciliation gives nirS 7 transfers against 13 speciations, which the review omits.
  conf: cont (note: "the literature conflicts") · class: not stated · holds: three studies of different design and depth, plus one reconciliation · src: heylenIncidenceNirSNirK2006 (abstract), grafIntergenomicComparisonsHighlight2014 (qualitative), jonesPhylogeneticAnalysisNitrite2008, parsonsRadiationNitrogenmetabolizingEnzymes2020 · trail: C-DENIT §2.2, §critic, §answers · from: C-DENIT:B-0052, C-DENIT:C-003, C-DENIT:C-004, C-DENIT:A-019

### nor-types: nitric oxide reductases, by type
needs: gene-trees
- **nor-types.1** cnorB (cNOR) is incongruent with 16S: strains from different classes carried identical cnorB, and nir and norB phylogenies disagreed.
  conf: single (marker) · class: deriv (marker) · holds: cultivated denitrifiers of different classes; only 30% amplification · src: heylenNitricOxideReductase2006 (abstract only; derived; single study, only 30% amplification) · trail: C-DENIT §2.3, §answers · from: C-DENIT:I-0005, C-DENIT:A-005, C-DENIT:R-0076
- **nor-types.2** qnorB (qNOR) separated denitrifiers from non-denitrifiers without finer taxonomic grouping.
  conf: not stated · class: not stated · holds: cultivated denitrifiers · src: heylenNitricOxideReductase2006 · trail: C-DENIT §2.3, §References · from: C-DENIT:B-0053, C-DENIT:R-0076
- **nor-types.3** qnorB also occurs in non-denitrifiers, consistent with NO detoxification.
  conf: not stated · class: not stated · holds: pure cultures and environmental samples · src: brakerNitricOxideReductase2003 (abstract only) · trail: C-DENIT §2.3, §6. Limits, §References · from: C-DENIT:B-0054, C-DENIT:B-0196, C-DENIT:R-0059
- **nor-types.4** The reviewer infers that qnorB presence is a weak marker of respiratory denitrification.
  conf: not stated · class: reading (critic: C-124) · holds: an inference from qnorB's occurrence in non-denitrifiers · src: none (the reviewer's inference) · trail: C-DENIT §2.3, §Adversarial · from: C-DENIT:B-0055, C-DENIT:C-124
- **nor-types.5** NORs arose several times independently from B- and C-family oxygen reductases; bNOR is confined to Bacillales, and sNOR is in most ammonia-oxidising bacteria.
  conf: not stated · class: not stated · holds: bacteria and archaea · src: muraliDiversityEvolutionNitric2024 · trail: C-DENIT §2.3 · from: C-DENIT:B-0056
- **nor-types.6** No congruence test exists for eNOR, sNOR, gNOR, nNOR or bNOR: Murali 2024, the source on these types, contains no gene-tree/species-tree congruence test.
  conf: single (marker) · class: search (note: "Not found by the agents' routes") · holds: the agents' Europe PMC routes and the synthesis's re-reading · src: muraliDiversityEvolutionNitric2024 (full text per search agents; derived; single study) · trail: C-DENIT §2.3, §answers, §Provenance · search: searched, not found (note: "Not found by the agents' routes") · from: C-DENIT:I-0006, C-DENIT:A-022, C-DENIT:B-0017
- **nor-types.7** In the Bacillota, many complete denitrifiers carry two or three NOR types.
  conf: not stated · class: not stated · holds: endospore-forming Bacillota · src: bellDenitrificationGenotypesEndosporeforming2024 (full text per search agent) · trail: C-DENIT §2.3, §References · from: C-DENIT:B-0057, C-DENIT:R-0052

### nosz: nosZ clade I and clade II against the organism tree
needs: gene-trees
- **nosz.1** Jones et al. found that nosZ was the only gene whose topology was not rejected, and only within the nirK-harbouring genome set (P = 0.14, per the search agent).
  conf: single (critic: C-074) · class: not stated · holds: one genome subset of Jones 2008; the P value comes from a search agent and is not in the abstract the synthesis read · src: jonesPhylogeneticAnalysisNitrite2008 (full text per a search agent) · trail: C-DENIT §2.4, §Adversarial · limit: access (critic: C-061) · from: C-DENIT:B-0059, C-DENIT:C-074, C-DENIT:C-061
- **nosz.2** The abstract of Jones 2008 reports substantial differences between gene trees and 16S in the partial-sequence monophyly analyses of all four genes.
  conf: not stated · class: not stated · holds: partial sequences of the four genes · src: jonesPhylogeneticAnalysisNitrite2008 (abstract, checked by the critic) · trail: C-DENIT §critic, §Adversarial · from: C-DENIT:C-006, C-DENIT:C-048, C-DENIT:C-062
- **nosz.3** Jones et al. reported no codon or GC evidence of recent HGT, even where topologies disagreed, and proposed duplication and lineage sorting as alternatives; they caution that structural variants and duplication make HGT hard to separate from other events.
  conf: not stated · class: not stated · holds: Jones 2008's genome set · src: jonesPhylogeneticAnalysisNitrite2008 · trail: C-DENIT §2.4, §5. Background · from: C-DENIT:B-0060, C-DENIT:B-0190
- **nosz.4** nosZ clade I sequences "generally follow the species phylogeny", with Betaproteobacterial sequences grouping among the Alphaproteobacteria as the main exception.
  conf: not stated · class: not stated · holds: clade I nosZ · src: jonesUnaccountedYetAbundant2012 (full text per one agent, abstract per another) · trail: C-DENIT §2.4, §Adversarial · from: C-DENIT:B-0061, C-DENIT:C-067
- **nosz.5** Within pure cultures, 90% of pairs with at least 97% 16S similarity had at least 80% nosZ nucleotide similarity, and congeneric species clustered together.
  conf: single (marker) · class: deriv (marker) · holds: pure cultures; not checked for nosZ clade · src: palmerGenomeDerivedCriteriaAssigning2009 (full text per agent; derived; single study) · trail: C-DENIT §2.4, §Adversarial · from: C-DENIT:I-0009, C-DENIT:C-119
- **nosz.6** The claim that nosZ is the most congruent denitrification gene is repeated secondarily by Intrator 2024, citing Dandie 2007 and Zumft and Körner 2007.
  conf: not stated · class: not stated · holds: a secondary account · src: intratorAquaticNitrousOxide2024 (SECONDARY), dandieAnalysisDenitrificationGenes2007, zumftNitrousOxideReductases2007 · trail: C-DENIT §2.4 · from: C-DENIT:B-0062
- **nosz.7** In potato-field Pseudomonas, nosZ, cnorB and 16S trees were "mostly congruent", with some exceptions; enrichment isolates in the same study were all nosZ+.
  conf: not stated · class: not stated · holds: culturable denitrifying Pseudomonas from potato cropping systems · src: dandieAnalysisDenitrificationGenes2007 (abstract only) · trail: C-DENIT §2.4, §6. Limits · from: C-DENIT:B-0063, C-DENIT:B-0194
- **nosz.8** The case that nosZ (clade I in practice) is the most 16S-congruent denitrification gene rests on one non-rejection within one of Jones 2008's genome subsets; the rest is qualitative (Graf 2014; Palmer 2009, per agent; Jones 2013, conflicting access labels) or a secondary review statement (Intrator 2024 citing Dandie 2007 and Zumft and Körner 2007).
  conf: single (critic: C-074) · class: not stated · holds: topology tests and qualitative comparisons (Jones 2008; Graf 2014; Jones 2013; Palmer 2009); Jones 2008 read in full only by a search agent · src: jonesPhylogeneticAnalysisNitrite2008, grafIntergenomicComparisonsHighlight2014, palmerGenomeDerivedCriteriaAssigning2009 (per agent), jonesUnaccountedYetAbundant2012 (conflicting access labels), intratorAquaticNitrousOxide2024 (secondary) · trail: C-DENIT §critic, §Adversarial, §answers · rating: "Moderate for nirS and nosZ clade I being relatively more congruent" (critic: C-061: rests on a search agent's figures that the synthesis could not verify) · contrary: one-sided (critic: C-111) · from: C-DENIT:C-005, C-DENIT:C-007, C-DENIT:C-047, C-DENIT:C-074, C-DENIT:C-111, C-DENIT:A-015, C-DENIT:B-0058
- **nosz.9** nosZ congruence statements from the pre-2012 literature concern clade I in practice, since clade II was recognised only in 2012 and 2013; Intrator 2024's congruence discussion and Palmer 2009's nosZ data were not checked for clade.
  conf: not stated · class: not stated · holds: the pre-2012 nosZ literature · src: intratorAquaticNitrousOxide2024, palmerGenomeDerivedCriteriaAssigning2009 · trail: C-DENIT §2.4, §Adversarial · from: C-DENIT:B-0058, C-DENIT:C-119
- **nosz.10** A nosZ-bearing Bacillus isolate with two nosZ copies was divergent from its relatives.
  conf: not stated · class: not stated · holds: closely related soil Bacillus isolates harbouring nosZ · src: jonesPhenotypicGenotypicHeterogeneity2011 (abstract only) · trail: C-DENIT §2.4, §References · from: C-DENIT:B-0068, C-DENIT:R-0087
- **nosz.11** nosZ clade II spans 13 bacterial and 2 archaeal phyla in genomes of 2012, and 56% of clade II genomes lacked other denitrification genes.
  conf: not stated · class: not stated · holds: genomes available in 2012 · src: sanfordUnexpectedNondenitrifierNitrous2012 (full text per one agent) · trail: C-DENIT §2.4 · from: C-DENIT:B-0071
- **nosz.12** No study found measured nosZ clade II congruence separately from clade I.
  conf: not stated · class: search (note: "any separate clade II nosZ congruence analysis") · holds: the agents' Europe PMC routes (keyword, title and author queries) and the synthesis's re-reading · src: none (a search result) · trail: C-DENIT §2.4, §Provenance, §answers · search: searched, not found (note: "any separate clade II nosZ congruence analysis") · from: C-DENIT:B-0072, C-DENIT:B-0017, C-DENIT:A-023

### narg-napa: narG and napA against the organism tree
needs: gene-trees
- **narg-napa.1** There is little genome-era evidence on narG and napA congruence; paralogous narG copies within a genome cluster apart.
  conf: not stated · class: not stated · holds: genome-era studies · src: none (the sentences cite no source) · trail: C-DENIT §2.5 · from: C-DENIT:B-0073, C-DENIT:B-0074
- **narg-napa.2** Codon and oligonucleotide bias did not reveal recent narG HGT, and species of one genus mostly clustered together.
  conf: not stated · class: deriv (marker) · holds: genome-derived narG sequences · src: palmerGenomeDerivedCriteriaAssigning2009 (full text per agent; derived) · trail: C-DENIT §2.5 · from: C-DENIT:I-0014
- **narg-napa.3** In 32 fluorescent Pseudomonas strains, narG and nosZ RFLP similarity did not correlate with 16S similarity, and both genes clustered in one ribogroup.
  conf: single (marker) · class: meas (marker) · holds: 32 fluorescent Pseudomonas strains; RFLP, within a genus · src: delormeComparativeGeneticDiversity2003 (full text per one agent; measured; single study) · trail: C-DENIT §2.5, §4. D3 · from: C-DENIT:I-0015, C-DENIT:B-0174
- **narg-napa.4** In Alteromonas, narGHI was inferred in the genus ancestor, with later losses coinciding with C and energy gene gains.
  conf: not stated · class: model (marker) · holds: the genus Alteromonas · src: changAlteromonasNitratireducensSp2025 (abstract only; modelled) · trail: C-DENIT §2.5, §4. D3 · from: C-DENIT:I-0016, C-DENIT:B-0181
- **narg-napa.5** A marine MAG study could not separate narG and napA reliably and pooled them, a methodological bound on gene-specific reporting.
  conf: not stated · class: not stated · holds: one marine MAG study, of transiently and permanently anoxic systems · src: hexterDenitrificationModularityEnvironmental2026 (full text per agent) · trail: C-DENIT §2.5, §3.1 · from: C-DENIT:B-0077, C-DENIT:B-0127
- **narg-napa.6** There is no genome-era gene-tree versus species-tree congruence metric for napA, or for narG outside the reconciliation (Parsons 2021) and a within-genus RFLP study (Delorme 2003).
  conf: not stated · class: search (note: "By the agents' Europe PMC routes and my re-reading") · holds: the agents' Europe PMC routes and the synthesis's re-reading · src: parsonsRadiationNitrogenmetabolizingEnzymes2020, delormeComparativeGeneticDiversity2003 · trail: C-DENIT §answers · rating: "Weak for NOR types beyond cNOR and qNOR, and for narG and napA" · search: searched, not found (note: "By the agents' Europe PMC routes and my re-reading") · from: C-DENIT:A-021, C-DENIT:A-016

### eukaryotic: eukaryotic homologues (the labelled eukaryotic case)
needs: gene-trees
- **eukaryotic.1** Fungal and protist nirK homologues group with prokaryotic nirK, which the authors read as a protomitochondrial origin.
  conf: not stated · class: not stated · holds: fungal and protist nirK · src: kimEukaryoticINirK2009 (abstract only) · trail: C-DENIT §2.7 · from: C-DENIT:B-0091
- **eukaryotic.2** Foraminiferal denitrification genes are highly conserved across 10 species, with an ancient acquisition inferred.
  conf: not stated · class: not stated · holds: 10 foraminiferal species · src: woehleNovelEukaryoticDenitrification2018 (abstract only), woehleDenitrificationForaminiferaHas2022 (abstract only) · trail: C-DENIT §2.7 · from: C-DENIT:B-0092
- **eukaryotic.3** Eukaryotic NirK is polyphyletic, falling in clades 1b and 1g.
  conf: not stated · class: not stated · holds: the 2024 Nir phylogenies · src: poldPhylogeneticsEnvironmentalDistribution2024 (checked) · trail: C-DENIT §2.7 · from: C-DENIT:B-0093
- **eukaryotic.4** Reconciliation across more than 700 fungal genomes inferred 2 to 5 times more duplications, losses and transfers for p450nor than for napA or nirK.
  conf: not stated · class: model (marker) · holds: more than 700 fungal genomes · src: higginsPhylogenomicsRevealDynamic2018 (abstract only; modelled) · trail: C-DENIT §2.3 · from: C-DENIT:I-0007
- **eukaryotic.5** For the eukaryotic homologues there are only origin inferences (Kim 2009; Woehle 2018, 2022; Higgins 2018 on P450nor); none reports a congruence metric.
  conf: not stated · class: search (note: "By the agents' Europe PMC routes and my re-reading") · holds: the agents' Europe PMC routes and the synthesis's re-reading · src: kimEukaryoticINirK2009, woehleNovelEukaryoticDenitrification2018, woehleDenitrificationForaminiferaHas2022, higginsPhylogenomicsRevealDynamic2018 · trail: C-DENIT §2.7, §answers · search: searched, not found (note: "By the agents' Europe PMC routes and my re-reading") · from: C-DENIT:B-0094, C-DENIT:A-025, C-DENIT:A-021
- **eukaryotic.6** Against habitat, the eukaryotic homologues have only descriptive notes, such as fungal nirK being occasionally abundant in the marine water column.
  conf: not stated · class: not stated · holds: the 2024 Nir survey · src: poldPhylogeneticsEnvironmentalDistribution2024 · trail: C-DENIT §answers · search: not stated · from: C-DENIT:A-060

### nir-trait-signal: functional and ecological signal on the Nir gene trees
needs: gene-trees
- **nir-trait-signal.1** The 2024 Nir survey did not compute a single congruence index; it built a 16-ribosomal-protein organism tree and ran phylogenetic Mantel tests constrained by it, which test trait signal on the gene tree, not a gene-tree/species-tree distance.
  conf: not stated · class: not stated · holds: about 6973 Nir-bearing genomes · src: poldPhylogeneticsEnvironmentalDistribution2024 (full text, checked) · trail: C-DENIT §2.1, §answers · from: C-DENIT:B-0041, C-DENIT:B-0042, C-DENIT:B-0046, C-DENIT:A-012, C-DENIT:B-0027
- **nir-trait-signal.2** NirK sequence dissimilarity correlated with KEGG gene-content dissimilarity beyond organism history (r = 0.388 for orthologues and 0.359 for pathways; P < 0.001), and several redox traits were more clustered on the NirK tree than on the organism tree.
  conf: not stated · class: not stated · holds: phylogenetic Mantel tests constrained by a 16-ribosomal-protein tree · src: poldPhylogeneticsEnvironmentalDistribution2024 · trail: C-DENIT §2.1 · from: C-DENIT:B-0043, C-DENIT:B-0044
- **nir-trait-signal.3** NirS dissimilarity also carried functional signal beyond the organism tree (phylogenetic Mantel r = 0.21 and 0.26).
  conf: not stated · class: not stated · holds: a genome set larger than the earlier ones · src: poldPhylogeneticsEnvironmentalDistribution2024 (full text, checked) · trail: C-DENIT §2.2 · from: C-DENIT:B-0051
- **nir-trait-signal.4** Nir trees carry functional-trait signal beyond the organism tree (phylogenetic Mantel r 0.21 to 0.39), and the authors conclude that Nir evolution is associated with both niche and organismal phylogeny, and that Nir phylogenies "recapitulate ecology distinctly from the corresponding organismal phylogeny".
  conf: single (marker) · class: deriv (marker) · holds: the range spans the NirS and NirK Mantel values of one study · src: poldPhylogeneticsEnvironmentalDistribution2024 (derived; single study) · trail: C-DENIT §2.1, §answers · from: C-DENIT:B-0045, C-DENIT:A-013

### reconciliation: the one genome-scale reconciliation
needs: gene-trees
- **reconciliation.1** The one genome-scale reconciliation (Parsons 2021, AnGST with fixed penalties) used a species tree of 308 genomes, but its gene searches ran on 254 bacterial and archaeal genomes, with gene counts from 10 (nirK) to 37 (napA): nirK 10, nirS 16, norB 36, nosZ 21, narG 34 and napA 37 genes.
  conf: single (critic: C-083) · class: not stated · holds: fixed penalties; the per-gene counts as the synthesis confirmed them · src: parsonsRadiationNitrogenmetabolizingEnzymes2020 (full text, checked) · trail: C-DENIT §Adversarial, §Provenance · from: C-DENIT:C-085, C-DENIT:C-083, C-DENIT:B-0015, C-DENIT:C-002
- **reconciliation.2** The reconciliation gives nirK 4 transfers against 9 speciations and nirS 7 against 13, both lower transfer-to-speciation ratios than nosZ (13 against 5) and norB (26 against 13); nirK has the lowest ratio of the four genes, from only 10 nirK genes.
  conf: single (critic: C-083) · class: not stated · holds: Parsons 2021 Table 3, fixed penalties, gene searches in 254 prokaryotic genomes · src: parsonsRadiationNitrogenmetabolizingEnzymes2020 (full text) · trail: C-DENIT §critic, §Adversarial, §answers · from: C-DENIT:C-002, C-DENIT:C-044, C-DENIT:C-113, C-DENIT:A-006
- **reconciliation.3** Reconciliation gave nosZ 13 transfers against 5 speciations (CIR clock; the same under UGAM), from only 21 nosZ genes.
  conf: single (marker) · class: model (marker) · holds: phylum-spread taxon sampling; 21 nosZ genes · src: parsonsRadiationNitrogenmetabolizingEnzymes2020 (full text, checked; modelled; single study) · trail: C-DENIT §2.4, §critic · from: C-DENIT:B-0065, C-DENIT:I-0010, C-DENIT:C-008, C-DENIT:B-0066
- **reconciliation.4** Parsons et al. inferred 26 transfers against 13 speciations for norB across bacteria, with norB not split by NOR type.
  conf: single (critic: C-083) · class: model (marker) · holds: norB not split by NOR type, so not comparable gene for gene with cnorB or qnorB results · src: parsonsRadiationNitrogenmetabolizingEnzymes2020 (full text, checked; modelled) · trail: C-DENIT §2.3, §Adversarial · from: C-DENIT:I-0008, C-DENIT:C-120
- **reconciliation.5** Reconciliation gave narG 15 transfers against 29 speciations and napA 13 against 46.
  conf: single (critic: C-083) · class: not stated · holds: the same reconciliation, with fixed penalties · src: parsonsRadiationNitrogenmetabolizingEnzymes2020 (checked) · trail: C-DENIT §2.5, §2.4 · from: C-DENIT:B-0075, C-DENIT:B-0066
- **reconciliation.6** The event counts depend on fixed penalties (HGT 3, duplication 2, loss 1) and on phylum-spread taxon sampling, and the method is deep-time.
  conf: not stated · class: not stated · holds: Parsons 2021 · src: parsonsRadiationNitrogenmetabolizingEnzymes2020 · trail: C-DENIT §2.4 · from: C-DENIT:B-0066
- **reconciliation.7** Removing Parsons 2021 removes the only direct conflict on nosZ and the only per-gene transfer counts for narG and napA.
  conf: not stated · class: reading (note: "Single-source sensitivity") · holds: the D1 evidence base · src: none (the reviewer's sensitivity reading) · trail: C-DENIT §answers · from: C-DENIT:A-030

### gene-ranking: the relative congruence ranking of the genes
needs: nirk, nirs, nosz, reconciliation
- **gene-ranking.1** The relative ranking of genes by congruence (nosZ most, nirS between, nirK least) is contested rather than established, and method-dependent: the reconciliation reverses the topology-test ranking at both ends, for nirK as well as for nosZ.
  conf: cont (critic: C-010) · class: not stated · holds: topology tests and qualitative comparisons (genus to phylum depth) against one deep reconciliation · src: jonesPhylogeneticAnalysisNitrite2008, grafIntergenomicComparisonsHighlight2014, parsonsRadiationNitrogenmetabolizingEnzymes2020 · trail: C-DENIT §critic, §Adversarial, §answers, §8. Answers · contrary: one-sided (critic: C-112) · from: C-DENIT:C-010, C-DENIT:C-045, C-DENIT:C-046, C-DENIT:C-112, C-DENIT:C-114, C-DENIT:A-008, C-DENIT:A-002, C-DENIT:A-003, C-DENIT:A-007, C-DENIT:A-097, C-DENIT:B-0047, C-DENIT:B-0204
- **gene-ranking.2** Without Jones 2008, which the synthesis never read, the nosZ-first ranking has no formal test behind it; the relative ranking (nosZ > nirS > nirK) would rest on qualitative statements (Graf 2014; Heylen 2006) and a secondary account (Intrator 2024).
  conf: not stated · class: reading (note: "Removing Jones 2008 leaves the relative ranking") · holds: the D1 evidence base · src: none (the reviewer's and the critic's sensitivity reading) · trail: C-DENIT §critic, §answers · from: C-DENIT:C-012, C-DENIT:A-031
- **gene-ranking.3** The reviewer reads the topology tests, the reconciliation over the tree of life and the island mobility within genera as measuring different things at different depths, so that both sets of results can hold and the two are not directly comparable; the critic finds this framing softens a genuine conflict in the literature.
  conf: not stated · class: reading (critic: C-126) · holds: deep reconciliation on phylum-spread sampling against genus-to-phylum monophyly tests · src: none (the reviewer's reading) · trail: C-DENIT §2.4, §answers, §Adversarial · from: C-DENIT:B-0069, C-DENIT:A-008, C-DENIT:C-126

### estimate-moderators: what moves the congruence estimates
needs: gene-trees
- **estimate-moderators.1** Congruence estimates depend on method (Jones 2008 found no codon or GC signal of recent HGT even where topologies disagreed), on genome set, on paralogy and on reference tree.
  conf: not stated · class: not stated · holds: the congruence studies the review covers · src: jonesPhylogeneticAnalysisNitrite2008 · trail: C-DENIT §answers, §2.6 · from: C-DENIT:A-011
- **estimate-moderators.2** Estimates move with genome set, paralogy, method and depth, but no study varies these systematically; no study has measured nosZ congruence as a function of depth on one genome set, and none of the methods (topology tests, monophyly posteriors, the Fritz-Purvis D, consenTRAIT, phylogenetic Mantel tests, reconciliation), which each measure something different, has been applied across all genes on one genome set.
  conf: not stated · class: search (note: "no study varies these systematically") · holds: the congruence studies the review covers · src: none (the reviewer's synthesis) · trail: C-DENIT §8. Answers, §2.4, §2.6 · search: not stated · from: C-DENIT:A-098, C-DENIT:B-0070, C-DENIT:B-0083, C-DENIT:B-0084
- **estimate-moderators.3** Reported nirK and nirS co-occurrence went from none (2010, per a search agent's secondary note) to 10 of 652 genomes (Graf 2014) to 5.3% of assemblies (Pold 2024), a difference of orders of magnitude between genome sets.
  conf: not stated · class: not stated · holds: three genome sets of different size and date · src: grafIntergenomicComparisonsHighlight2014, poldPhylogeneticsEnvironmentalDistribution2024 · trail: C-DENIT §2.6, §answers, §7. Cross · from: C-DENIT:B-0078, C-DENIT:A-020, C-DENIT:B-0205
- **estimate-moderators.4** The authors of the 2024 Nir survey say multiple Nir copies are 5 to 10 times more common than earlier estimates.
  conf: single (critic: C-078) · class: not stated · holds: the 2024 Nir survey's assemblies · src: poldPhylogeneticsEnvironmentalDistribution2024 · trail: C-DENIT §2.6, §Adversarial · from: C-DENIT:B-0079, C-DENIT:C-078
- **estimate-moderators.5** 16% of NirS-bearing assemblies carry more than one nirS, 85% of them from different clades, and 10% of NirK-bearing assemblies carry more than one nirK, 44% cross-clade.
  conf: not stated · class: not stated · holds: the 2024 Nir survey's assemblies; checked in the text, supplements not read · src: poldPhylogeneticsEnvironmentalDistribution2024 (checked in the text, supplements not read) · trail: C-DENIT §2.6 · from: C-DENIT:B-0080
- **estimate-moderators.6** None of the older congruence studies describes how multi-copy genomes were handled, as far as the abstracts show; Graf 2014 took the longest 16S copy per genome.
  conf: not stated · class: not stated · holds: isolate-era and early genome congruence studies, read mostly at the abstract · src: grafIntergenomicComparisonsHighlight2014 · trail: C-DENIT §2.6 · limit: access (note: "as far as the abstracts show") · search: not stated · from: C-DENIT:B-0081, C-DENIT:B-0082
- **estimate-moderators.7** The reference tree differs between studies: 16S in isolate-era work, 16 ribosomal proteins in Pold 2024 and Parsons 2021, and GTDB in Pold 2025.
  conf: not stated · class: not stated · holds: the studies named · src: poldPhylogeneticsEnvironmentalDistribution2024, parsonsRadiationNitrogenmetabolizingEnzymes2020, poldDenitrificationCommunityTrait2025 · trail: C-DENIT §2.6 · from: C-DENIT:B-0085
- **estimate-moderators.8** nosZ presence is clumped on both nir trees (D = 0.335 on nirK and 0.431 on nirS; non-random and non-Brownian) and more conserved on nirS (tau_D about 0.08) than on nirK.
  conf: not stated · class: not stated · holds: 652 genomes; co-inheritance, the nearest precedent to a congruence measure · src: grafIntergenomicComparisonsHighlight2014 (checked) · trail: C-DENIT §2.6 · from: C-DENIT:B-0086
- **estimate-moderators.9** The comparable nrfA tree was congruent with the organism tree at class level, with named exceptions.
  conf: not stated · class: not stated · holds: nitrate ammonifiers, a comparator outside the review's scope · src: saghaiPhyloecologyNitrateAmmonifiers2023 (full text per agent) · trail: C-DENIT §2.6 · from: C-DENIT:B-0087
- **estimate-moderators.10** The main texts of Martiny 2013 and Goberna and Verdú 2016 do not report denitrification-step conservatism; their supplements were not checked.
  conf: not stated · class: not stated · holds: trait-conservatism frameworks, indirect for the question; read through a summarising tool, which is not a reading of the full text · src: martinyPhylogeneticConservatismFunctional2013 (abstract only; indirect; critic: C-065 was "full text via summarising tool; indirect"), gobernaPredictingMicrobialTraits2016 (abstract only; indirect; critic: C-065 was "full text via summarising tool; indirect") · trail: C-DENIT §2.6, §Adversarial · limit: access (critic: C-066) · from: C-DENIT:B-0088, C-DENIT:C-063, C-DENIT:C-064, C-DENIT:C-065, C-DENIT:C-066
- **estimate-moderators.11** Albright 2019 (more than 6000 genomes) reports incomplete N pathways in 39% of species; whether it computed per-step trait depth could not be checked.
  conf: not stated · class: not stated · holds: more than 6000 bacterial and archaeal genomes; indirect · src: albrightComparativeGenomicsNitrogen2018 (abstract only; indirect) · trail: C-DENIT §2.6, §References · limit: access (note: "could not be checked") · from: C-DENIT:B-0089, C-DENIT:B-0090, C-DENIT:R-0047

### gene-transfer: vertical inheritance and transfer, per gene
needs: gene-trees
- **gene-transfer.1** At shallow depth, three genera or species complexes show the nos cluster as a mobile or islanded element: Bradyrhizobium (Shiina 2014), Castellaniella (Goff 2024) and the Ralstonia complex (Truchon 2023); this measures genomic context, not gene-tree versus species-tree fit.
  conf: not stated · class: not stated · holds: within genera; the Bradyrhizobium evidence is secondary · src: shiinaRelationshipSoilType2014 (secondary; critic: C-009), goffGenomicEnvironmentalControls2024, truchonPlantPathogenicIRalstonia2023 · trail: C-DENIT §answers, §2.4, §critic, §Adversarial · from: C-DENIT:A-009, C-DENIT:B-0067, C-DENIT:C-009, C-DENIT:C-123
- **gene-transfer.2** In soybean bradyrhizobia, the USDA110 nos cluster position corresponds to a genomic island flanking trnS-GGA in USDA6; in Shiina 2014 this is a citation of earlier genome comparisons (their ref. 17).
  conf: not stated · class: deriv (marker) · holds: the USDA110 and USDA6 genomes, known through Shiina 2014's citation (their ref. 17) · src: shiinaRelationshipSoilType2014 (SECONDARY; derived; critic: C-058 was "full text, checked; derived") · trail: C-DENIT §2.4, §Adversarial · from: C-DENIT:I-0011, C-DENIT:C-057, C-DENIT:C-058, C-DENIT:C-059
- **gene-transfer.3** In Castellaniella, the nos locus beside an arginine tRNA is replaced by a copper-resistance island in four strains; the Castellaniella NosZ is clade II.
  conf: not stated · class: meas (marker) · holds: four Castellaniella strains from an anthropogenically disturbed subsurface · src: goffGenomicEnvironmentalControls2024 (full text per agent; measured) · trail: C-DENIT §2.4, §critic, §References · from: C-DENIT:I-0012, C-DENIT:C-035, C-DENIT:R-0070
- **gene-transfer.4** In the Ralstonia complex, the nos cluster sits near phylotype-specific IS remnants in different genomic locations, and nos presence is "highly variable" across Betaproteobacteria.
  conf: not stated · class: deriv (marker) · holds: the Ralstonia solanacearum species complex · src: truchonPlantPathogenicIRalstonia2023 (full text, checked; derived) · trail: C-DENIT §2.4 · from: C-DENIT:I-0013
- **gene-transfer.5** T. thermophilus shows laboratory conjugative transfer of the nar-nir-nor island among strains, and the island is lost under aerobic culture.
  conf: single (critic: C-081) · class: not stated · holds: T. thermophilus in the laboratory · src: alvarezLateralTransferDenitrification2011 (abstract), alvarezTransferableDenitrificationCapability2014 (abstract) · trail: C-DENIT §answers, §4. D3, §Adversarial · limit: access (critic: C-073) · from: C-DENIT:A-010, C-DENIT:B-0167, C-DENIT:C-081, C-DENIT:C-073, C-DENIT:A-086
- **gene-transfer.6** Mobile-element context is reported for the nos cluster (Bradyrhizobium, Castellaniella, Ralstonia, haloarchaeal plasmids), for nir-nor in Azospirillum, and for nar and nos on haloarchaeal plasmids.
  conf: not stated · class: not stated · holds: the genera named · src: shiinaRelationshipSoilType2014, goffGenomicEnvironmentalControls2024, truchonPlantPathogenicIRalstonia2023, mirallesrobledilloDistributionDenitrificationHaloarchaea2021, jangPotentiallyMobileDenitrification2019 · trail: C-DENIT §5. Background · from: C-DENIT:B-0188
- **gene-transfer.7** Evidence for vertical descent includes nosZ clade I topology (Jones 2008; Jones 2013), narG, nirS and norB in the Thermales (Jiao 2022), and narGHI in Alteromonas (Chang 2025).
  conf: not stated · class: not stated · holds: the lineages named · src: jonesPhylogeneticAnalysisNitrite2008, jonesUnaccountedYetAbundant2012, jiaoComparativeGenomicAnalysis2022, changAlteromonasNitratireducensSp2025 · trail: C-DENIT §5. Background · from: C-DENIT:B-0189
- **gene-transfer.8** In Thermus (23 or 24 strains), narG, nirS and norB were inferred to be vertically inherited from the Thermales ancestor, while nirK arrived by two HGT events.
  conf: not stated · class: not stated · holds: genus level, ancestral reconstruction · src: jiaoComparativeGenomicAnalysis2022 (abstract only) · trail: C-DENIT §2.5, §4. D3, §critic · limit: access (critic: C-073) · from: C-DENIT:B-0076, C-DENIT:B-0168, C-DENIT:C-037
- **gene-transfer.9** In Thermus, vertical inheritance of narG, nirS and norB with nirK HGT at genus level (Jiao 2022) stands against lateral transfer of the whole island among T. thermophilus strains (Alvarez 2011); the reviewer reads these as operating at different depths, so that both may hold.
  conf: cont (note: "Conflicts") · class: reading (note: "These operate at different depths and may both hold") · holds: genus level against strains of one species · src: jiaoComparativeGenomicAnalysis2022 (abstract), alvarezLateralTransferDenitrification2011 · trail: C-DENIT §answers · from: C-DENIT:A-085, C-DENIT:A-086, C-DENIT:A-087
- **gene-transfer.10** Mobile elements are proposed for Castellaniella (an insertion at the nos locus, causality not tested), shown possible in the laboratory for T. thermophilus, and inferred for Azospirillum; none of these shows mobility accounting for the natural distribution of gene combinations, and in Thermus the genus-level study infers vertical inheritance for most genes.
  conf: not stated · class: not stated · holds: Castellaniella, T. thermophilus and Azospirillum · src: goffGenomicEnvironmentalControls2024, alvarezLateralTransferDenitrification2011 (abstract), jangPotentiallyMobileDenitrification2019, jiaoComparativeGenomicAnalysis2022 · trail: C-DENIT §critic · from: C-DENIT:C-035, C-DENIT:C-036, C-DENIT:C-053
- **gene-transfer.11** One metagenome study reports lower HGT frequency for nirS-type than nirK-type communities, with the method not visible.
  conf: single (marker) · class: not stated · holds: denitrifying communities from metagenomes · src: mingInsightsEvolutionaryEcological2024 (abstract only; SINGLE SOURCE) · trail: C-DENIT §5. Background, §Adversarial · from: C-DENIT:I-0022, C-DENIT:C-082
- **gene-transfer.12** The cause of gene-tree incongruence is disputed: HGT (Heylen 2006; Alvarez 2011; Jang 2019) against duplication and lineage sorting (Jones 2008; the Intrator 2025 discussion); Jang 2019 describes phylogeny alone as "circumstantial evidence".
  conf: cont (note: "Conflicts") · class: not stated · holds: the studies named · src: heylenIncidenceNirSNirK2006, alvarezLateralTransferDenitrification2011, jangPotentiallyMobileDenitrification2019, jonesPhylogeneticAnalysisNitrite2008, intratorAquaticCoppercontainingNitrite2025 · trail: C-DENIT §answers, §5. Background · from: C-DENIT:A-019, C-DENIT:A-020, C-DENIT:B-0190

### primer-bias: primer bias as a generator of habitat patterns
needs: denitrification-genes
- **primer-bias.1** None of 35 published and 121 new nirS and nirK primers was an optimal universal pair, and performance differed across habitats on 47 metagenomes, so primer choice alone changes apparent habitat patterns.
  conf: not stated · class: meas (marker) · holds: 47 metagenomes · src: bonillarossoDesignEvaluationPrimers2016 (abstract only; measured) · trail: C-DENIT §3.3, §answers · from: C-DENIT:I-0021, C-DENIT:A-041
- **primer-bias.2** Broader primers found terrestrial nirK and nirS 2 to 6 times more abundant.
  conf: not stated · class: not stated · holds: terrestrial environments · src: weiHigherDiversityAbundance2015 (abstract only) · trail: C-DENIT §3.3 · from: C-DENIT:B-0149
- **primer-bias.3** Nearly half of 227 confirmed denitrifiers gave no nir amplicon, and 70% gave no norB amplicon.
  conf: not stated · class: not stated · holds: cultivated denitrifiers · src: heylenIncidenceNirSNirK2006, heylenNitricOxideReductase2006 · trail: C-DENIT §3.3 · from: C-DENIT:B-0150
- **primer-bias.4** Clade II nosZ and clade II nirK were missed by earlier primers.
  conf: not stated · class: not stated · holds: earlier primers · src: sanfordUnexpectedNondenitrifierNitrous2012, jonesUnaccountedYetAbundant2012, helenHighlyDiverseNirK2016 · trail: C-DENIT §3.3 · from: C-DENIT:B-0151
- **primer-bias.5** Every primer-based habitat result is bounded by primer bias.
  conf: not stated · class: not stated · holds: the primer-based habitat studies the review covers · src: none (the reviewer's synthesis) · trail: C-DENIT §3.3 · from: C-DENIT:B-0152

### habitat-uncontrolled: genes against habitat, without taxonomic or sampling controls
needs: denitrification-genes, primer-bias
- **habitat-uncontrolled.1** Without controls, habitat structure is reported for several genes (nirK, nirS, nosZ clades, NOR types) and for gene combinations, but most of it rests on single studies or on abstract-only, primer-based work; it is replicated only in the loose sense that different genes in different datasets show some structure, and no single gene-habitat association has been replicated across independent data types.
  conf: single (critic: C-050) · class: not stated · holds: amplicon or primer data, metagenome read placement, genome label tests and MAG community modularity; alongside a null result (Horn 2006) and a failure to reproduce earlier primer results (Pold 2024) · src: none (the reviewer's synthesis, as the critic reformulated it) · trail: C-DENIT §critic, §Adversarial, §answers, §8. Answers · rating: "Uncontrolled associations: moderate and replicated" (critic: C-049: in practice each gene-habitat claim rests on one study) · contrary: one-sided (critic: C-116) · from: C-DENIT:C-013, C-DENIT:C-021, C-DENIT:C-022, C-DENIT:C-049, C-DENIT:C-050, C-DENIT:C-116, C-DENIT:A-032, C-DENIT:A-033, C-DENIT:A-049, C-DENIT:A-102
- **habitat-uncontrolled.2** Each uncontrolled association has confounds: primer bias, uneven sampling, single-label habitat metadata, and habitat-taxon confounding.
  conf: not stated · class: not stated · holds: the uncontrolled habitat studies · src: none (the reviewer's synthesis) · trail: C-DENIT §answers · from: C-DENIT:A-050
- **habitat-uncontrolled.3** That habitat and taxonomy are visibly confounded in Graf 2014's genomes, because animal-host genomes are largely pathogens, is the reviewer's reading; Graf 2014 does not state it.
  conf: not stated · class: reading (critic: C-070) · holds: Graf 2014's animal-host genomes · src: none (the reviewer's reading) · trail: C-DENIT §3.1, §Adversarial · from: C-DENIT:B-0100, C-DENIT:C-069, C-DENIT:C-070, C-DENIT:C-071, C-DENIT:C-125
- **habitat-uncontrolled.4** Across 626 genomes with GOLD or NCBI habitat labels in eight categories plus "multiple", denitrification gene-combination types were non-random across habitats (chi-square = 136, P < 0.001); this is the main genome test and the only one.
  conf: single (critic: C-075) · class: not stated · holds: 626 genomes with single GOLD or NCBI labels; prokaryotes pooled with fungal genomes · src: grafIntergenomicComparisonsHighlight2014 (full text, checked) · trail: C-DENIT §3.1, §critic, §Adversarial · from: C-DENIT:B-0095, C-DENIT:A-034, C-DENIT:C-014, C-DENIT:C-075, C-DENIT:C-015
- **habitat-uncontrolled.5** In that test, K-types were over-represented in animal-host organisms, S-types in soil and extreme habitats, KS, KSZ and SZ types in wastewater, SZ also in "multiple habitats", and Z-only types in marine habitats; a freshwater SZ over-representation was not found in the text.
  conf: single (critic: C-075) · class: deriv (marker) · holds: 626 genomes with GOLD or NCBI habitat labels, fungal genomes included · src: grafIntergenomicComparisonsHighlight2014 (full text, checked; derived) · trail: C-DENIT §3.1, §Provenance, §answers · from: C-DENIT:B-0096, C-DENIT:B-0097, C-DENIT:I-0017, C-DENIT:A-035, C-DENIT:B-0014, C-DENIT:C-118
- **habitat-uncontrolled.6** Graf 2014's 652-genome set and its gene-combination versus habitat test include fungal (Ascomycota) genomes, whose nirK and P450nor are the eukaryotic case, so prokaryotes and eukaryotes are pooled in it.
  conf: not stated · class: not stated · holds: Graf 2014, Ascomycota rows in its Table 1 · src: grafIntergenomicComparisonsHighlight2014 · trail: C-DENIT §critic, §Adversarial · from: C-DENIT:C-015, C-DENIT:C-051, C-DENIT:C-118
- **habitat-uncontrolled.7** Graf 2014's habitat test did not control for taxonomy, which was tested separately and was also non-random at phylum, class and order.
  conf: not stated · class: not stated · holds: Graf 2014's genomes · src: grafIntergenomicComparisonsHighlight2014 · trail: C-DENIT §3.1, §answers · from: C-DENIT:B-0098, C-DENIT:A-036
- **habitat-uncontrolled.8** Graf 2014's statement that the GOLD data "does not provide enough data or detail to confirm these hypotheses" refers to specific hypotheses from other studies about nirS dominance and habitat filtering in marine systems, not to its own chi-square habitat result.
  conf: not stated · class: not stated · holds: Graf 2014, as read in full text by the critic · src: grafIntergenomicComparisonsHighlight2014 (full text) · trail: C-DENIT §3.1, §critic, §Adversarial · from: C-DENIT:B-0099, C-DENIT:C-016, C-DENIT:C-068
- **habitat-uncontrolled.9** Across 4082 metagenomes, NirK and NirS clades differed in biome prevalence: median nirK per Gb was 19 times that of nirS in terrestrial biomes, and nirS was relatively more abundant in engineered biomes, vents, sea floor, hot springs and marshes.
  conf: not stated · class: meas (marker) · holds: habitat assigned by ecoregion from coordinates (terrestrial, croplands kept separate), latitude band (marine) or author description (freshwater); placement sensitivity 76% for nirK and 93% for nirS; no taxonomic control; biome sampling uneven · src: poldPhylogeneticsEnvironmentalDistribution2024 (checked; measured) · trail: C-DENIT §3.1, §critic, §answers · contrary: one-sided (critic: C-115) · from: C-DENIT:B-0101..0105, C-DENIT:A-036, C-DENIT:C-017, C-DENIT:C-115
- **habitat-uncontrolled.10** Earlier primer-based relations (nirK diversity with pH, nirS diversity with ammonium, nirS more environment-sensitive) were not reproduced in metagenomes, and the authors attribute the earlier results to primers capturing only NirK clade 1a; primer-based and metagenome results on nirK and nirS environmental drivers conflict.
  conf: cont (note: "Conflicts") · class: not stated · holds: 4082 metagenomes against earlier amplicon studies · src: poldPhylogeneticsEnvironmentalDistribution2024 · trail: C-DENIT §3.1, §answers, §7. Cross · from: C-DENIT:B-0106, C-DENIT:A-040, C-DENIT:A-053, C-DENIT:B-0208
- **habitat-uncontrolled.11** Across 3991 metagenomes, nosZ clade II exceeded clade I in nearly all biomes; random-forest models on soil and Australian marine subsets explained less than half the variance, except for the nosZ I minus II difference in soils.
  conf: not stated · class: meas (marker) · holds: 3991 metagenomes; no taxonomic control; biome sampling uneven · src: poldDenitrificationCommunityTrait2025 (checked; measured) · trail: C-DENIT §3.1, §answers · contrary: one-sided (critic: C-115) · from: C-DENIT:B-0107, C-DENIT:B-0108, C-DENIT:A-036, C-DENIT:C-115, C-DENIT:C-017
- **habitat-uncontrolled.12** Marine nosZ datasets were dominated by clade II.
  conf: not stated · class: not stated · holds: marine systems · src: bertagnolliNondenitrifierNitrousOxide2020 (abstract only) · trail: C-DENIT §3.1, §answers · from: C-DENIT:B-0109, C-DENIT:A-036
- **habitat-uncontrolled.13** In the Bacillota, complete denitrifiers always carried clade II nosZ.
  conf: not stated · class: not stated · holds: endospore-forming Bacillota (class Bacilli, 17 genera) · src: bellDenitrificationGenotypesEndosporeforming2024 · trail: C-DENIT §3.1, §4. D3, §References · from: C-DENIT:B-0110, C-DENIT:B-0180, C-DENIT:R-0052
- **habitat-uncontrolled.14** The clade of nosZ in complete denitrifiers conflicts between datasets: mostly clade I across global genomes (Pold 2025, 74% against 26%, with clade II complete in 80% of Pseudomonadota and 94% of Aquificota; Graf 2014) against a majority of clade II in marine anoxic MAGs (Hexter 2026) and in the Bacillota (Bell 2024); these rest on different taxon and habitat mixes, and the 74% against 26% figure is ambiguous as to its denominator.
  conf: cont (note: "Conflicts") · class: not stated · holds: global genomes against marine anoxic MAGs and Bacillota genomes · src: poldDenitrificationCommunityTrait2025, grafIntergenomicComparisonsHighlight2014, hexterDenitrificationModularityEnvironmental2026, bellDenitrificationGenotypesEndosporeforming2024 · trail: C-DENIT §answers, §7. Cross, §Adversarial · from: C-DENIT:A-053, C-DENIT:A-054, C-DENIT:B-0206, C-DENIT:B-0207, C-DENIT:C-072
- **habitat-uncontrolled.15** Global nirS and nirK community similarity tracked salinity (UniFrac); the authors caution that non-random phylogenetic patterns are hard to attribute to niche or neutral processes.
  conf: not stated · class: deriv (marker) · holds: primer-based global and local community data · src: jonesEcologicalEvolutionaryFactors2010 (abstract only; derived) · trail: C-DENIT §3.1, §answers, §critic, §References · limit: access (critic: C-073) · from: C-DENIT:B-0111, C-DENIT:I-0018, C-DENIT:A-036, C-DENIT:C-018, C-DENIT:R-0086
- **habitat-uncontrolled.16** Aquatic nirK OTUs mostly came from one source, and archaeal nirK split sharply by salinity; about 70% of sequences, mainly terrestrial clusters, were removed before analysis.
  conf: not stated · class: not stated · holds: aquatic nirK fragment data (70 to 277 bp regions) with NCBI source labels · src: intratorAquaticCoppercontainingNitrite2025 (full text per agent) · trail: C-DENIT §3.1, §answers, §6. Limits · from: C-DENIT:B-0112, C-DENIT:B-0113, C-DENIT:A-037, C-DENIT:B-0199, C-DENIT:B-0201
- **habitat-uncontrolled.17** Aquatic nosZ showed "strong habitat separation between clades", with 76% and 59% of OMZ archetypes confined to one OMZ.
  conf: not stated · class: not stated · holds: aquatic nosZ fragment data (70 to 277 bp regions) with NCBI source labels · src: intratorAquaticNitrousOxide2024 (full text per agent, read at introduction level by one agent) · trail: C-DENIT §3.1, §6. Limits · from: C-DENIT:B-0114, C-DENIT:B-0199, C-DENIT:B-0201
- **habitat-uncontrolled.18** Neither aquatic study corrects for sampling effort per habitat or for primer origin; single-source OTUs are expected when habitats are unevenly sampled, so these figures do not separate habitat specificity from sampling, and the same caution applies to Graf 2014's categories.
  conf: not stated · class: reading (note: "Reviewer's reading, from one search agent") · holds: Intrator 2024 and 2025, and Graf 2014 · src: intratorAquaticNitrousOxide2024, intratorAquaticCoppercontainingNitrite2025, grafIntergenomicComparisonsHighlight2014 · trail: C-DENIT §3.1 · from: C-DENIT:B-0115, C-DENIT:B-0116, C-DENIT:B-0117, C-DENIT:B-0113, C-DENIT:B-0114
- **habitat-uncontrolled.19** nirK sequences were "significantly more similar to nirK sequences from the same habitat than to nirK sequences retrieved from highly related taxa"; the test, and whether the isolation campaign was controlled, are not visible.
  conf: single (critic: C-076) · class: not stated · holds: isolate-level, cultivated denitrifiers · src: heylenIncidenceNirSNirK2006 (abstract only) · trail: C-DENIT §3.1, §answers · limit: access (critic: C-073) · from: C-DENIT:B-0118, C-DENIT:B-0119, C-DENIT:A-038, C-DENIT:C-076
- **habitat-uncontrolled.20** Site-pair clone libraries go both ways: nirS subclusters matched two marine sediment sites, nosZ differed between native and cultivated soils, and nirK and nirS assemblages differed between upland and wetland forest soils.
  conf: not stated · class: not stated · holds: site-pair clone libraries, primer-limited · src: brakerNitriteReductaseGenes2000 (abstract only), stresNitrousOxideReductase2004 (abstract only), priemeDiversityNitriteReductase2002 (abstract only) · trail: C-DENIT §3.1 · from: C-DENIT:B-0120, C-DENIT:B-0122
- **habitat-uncontrolled.21** nosZ from earthworm gut and soil were phylogenetically indistinguishable, with 1 of 182 gut sequences not grouping with soil sequences.
  conf: not stated · class: not stated · holds: earthworm gut against soil; a primer-limited clone library · src: hornNitrousOxideReductase2006 (abstract only) · trail: C-DENIT §3.1, §answers, §critic · limit: access (critic: C-073) · from: C-DENIT:B-0121, C-DENIT:B-0122, C-DENIT:A-039, C-DENIT:C-020
- **habitat-uncontrolled.22** Habitat separation of nosZ (the site-pair studies; Intrator 2024) stands against no separation (gut against soil, Horn 2006).
  conf: cont (note: "Conflicts") · class: not stated · holds: site-pair studies and Intrator 2024 against gut versus soil · src: brakerNitriteReductaseGenes2000, stresNitrousOxideReductase2004, priemeDiversityNitriteReductase2002, intratorAquaticNitrousOxide2024, hornNitrousOxideReductase2006 · trail: C-DENIT §answers, §7. Cross, §3.1 · from: C-DENIT:A-053, C-DENIT:A-055, C-DENIT:B-0209, C-DENIT:B-0120
- **habitat-uncontrolled.23** For NOR types there is a single descriptive habitat statement: gNOR occurs predominantly in organisms from sulfidic environments, and eNOR is common in hypersaline ones.
  conf: single (critic: C-077) · class: deriv (marker) · holds: bacteria and archaea in the Murali 2024 dataset, whose habitat assignments (Dataset S7) were not read · src: muraliDiversityEvolutionNitric2024 (derived; single study) · trail: C-DENIT §3.1, §critic, §answers · limit: access (critic: C-077) · from: C-DENIT:B-0123, C-DENIT:A-037, C-DENIT:A-059, C-DENIT:C-019, C-DENIT:C-077, C-DENIT:R-0105
- **habitat-uncontrolled.24** In 516 MAGs from 107 WWTPs, napA sequences and genomic contexts differed between partial and complete denitrifiers; this is within one habitat type and bears on metabolic niche, not habitat, and it is the only napA evidence against habitat.
  conf: not stated · class: not stated · holds: wastewater treatment plants only · src: liMetabolicNicheDifferentiation2027 (abstract only) · trail: C-DENIT §3.1, §answers · from: C-DENIT:B-0124, C-DENIT:B-0125, C-DENIT:A-058
- **habitat-uncontrolled.25** Denitrification modularity differed between transiently and permanently anoxic marine systems.
  conf: not stated · class: not stated · holds: marine MAGs from transiently and permanently anoxic systems · src: hexterDenitrificationModularityEnvironmental2026 (full text per agent) · trail: C-DENIT §3.1, §2.5 · from: C-DENIT:B-0127, C-DENIT:B-0077
- **habitat-uncontrolled.26** In oxygen deficient zones (ODZs) partial denitrifiers dominate, and MAGs of one genus ranged from nor-only in the oxycline to nearly complete in the ODZ core.
  conf: not stated · class: not stated · holds: global oxygen deficient zones, from the oxycline to the core · src: zhangPartitioningDenitrificationPathway2023 (full text per agent) · trail: C-DENIT §3.1, §References · from: C-DENIT:B-0128, C-DENIT:R-0137
- **habitat-uncontrolled.27** Tundra soil types differed in their truncated-pathway denitrifier communities.
  conf: not stated · class: not stated · holds: tundra soils · src: pessiIndepthCharacterizationDenitrifier2022 (abstract only) · trail: C-DENIT §3.1 · from: C-DENIT:B-0129
- **habitat-uncontrolled.28** Mesocosms of four coastal sediment habitats differed in nosZ composition.
  conf: not stated · class: not stated · holds: coastal sediment mesocosms · src: wittorfHabitatDiversityType2020 (abstract only) · trail: C-DENIT §3.1 · from: C-DENIT:B-0130
- **habitat-uncontrolled.29** On one farm, nosZ clade I and II communities differed in phylogenetic structure along edaphic gradients.
  conf: not stated · class: not stated · holds: one farm; within one habitat, the nearest precedent · src: juhansonSpatialPhyloecologicalAnalyses2017 (abstract only) · trail: C-DENIT §3.1 · from: C-DENIT:B-0131
- **habitat-uncontrolled.30** Nelson 2016's taxon-habitat null stands against habitat-specific taxa in tundra MAGs (Pessi 2022) and ODZ MAGs (Zhang 2023); these are different habitats and scales.
  conf: cont (note: "Conflicts") · class: not stated · holds: soil metagenomes against tundra and ODZ MAGs · src: nelsonGlobalBiogeographyMicrobial2016, pessiIndepthCharacterizationDenitrifier2022, zhangPartitioningDenitrificationPathway2023 · trail: C-DENIT §answers · from: C-DENIT:A-053, C-DENIT:A-056
- **habitat-uncontrolled.31** For genome gene combinations against habitat, Graf 2014 is the only test; removing it leaves only metagenome and amplicon evidence.
  conf: not stated · class: reading (note: "Single-source sensitivity") · holds: the D2 evidence base · src: none (the reviewer's sensitivity reading) · trail: C-DENIT §answers · from: C-DENIT:A-064
- **habitat-uncontrolled.32** napA, narG and the eukaryotic homologues are essentially unmeasured against habitat: the narG evidence is one within-order result (Ghaly 2026) and the napA evidence one WWTP study.
  conf: not stated · class: not stated · holds: the habitat studies the review covers · src: ghalyAgricultureAltersProtein2026, liMetabolicNicheDifferentiation2027 · trail: C-DENIT §critic, §Adversarial · search: not stated · from: C-DENIT:C-020, C-DENIT:C-099

### habitat-controlled: genes against habitat, with taxonomic or sampling controls
needs: habitat-uncontrolled
- **habitat-controlled.bg1** Blomberg's K is a descriptive statistic of phylogenetic signal, the tendency for related species to resemble each other; K less than one means less signal than expected under a Brownian motion model of evolution.
  kind: background · ref: blombergTestingPhylogeneticSignal2003 · check: DOI 10.1111/j.0014-3820.2003.tb00285.x resolves on Crossref (Evolution 57(4): 717-745); the definition of phylogenetic signal, the statistic K and "K was less than one" as less signal than expected under Brownian motion are in the abstract (Europe PMC, PMID 12778543)
- **habitat-controlled.1** No study found fits gene presence or sequence against habitat with a phylogenetic regression, a phylogenetically constrained permutation or stratification by lineage, for any denitrification gene; the controlled question is unmeasured for every gene.
  conf: not stated · class: search (note: "No study found fits gene presence or sequence against habitat") · holds: Europe PMC keyword searches for phylogenetic logistic regression, phyloglm and phylogenetic signal combined with denitrification genes, and the synthesis's full-text checks · src: none (a search result) · trail: C-DENIT §3.2, §answers, §critic, §Provenance · rating: "Controlled associations: very weak" · search: searched, not found (note: "No study found fits gene presence or sequence against habitat") · from: C-DENIT:B-0132, C-DENIT:A-042, C-DENIT:A-051, C-DENIT:A-057, C-DENIT:A-103, C-DENIT:C-023, C-DENIT:C-024, C-DENIT:B-0017
- **habitat-controlled.2** No habitat test controls sampling effort per habitat in sequence-database compilations.
  conf: not stated · class: search (note: "By Europe PMC keyword searches") · holds: the same keyword searches and full-text checks · src: none (a search result) · trail: C-DENIT §answers · search: searched, not found (note: "By Europe PMC keyword searches") · from: C-DENIT:A-058, C-DENIT:A-057
- **habitat-controlled.3** There are two partial precedents, one abstract-only, and neither separates habitat from lineage.
  conf: not stated · class: not stated · holds: Ghaly 2026 and Shiina 2014 · src: ghalyAgricultureAltersProtein2026, shiinaRelationshipSoilType2014 · trail: C-DENIT §critic, §answers, §8. Answers · from: C-DENIT:C-025, C-DENIT:A-052, C-DENIT:A-104, C-DENIT:C-026, C-DENIT:C-027
- **habitat-controlled.4** Across more than 2500 soil metagenomes, diversifying selection on narG was higher in agricultural than in natural soils, specifically in Burkholderiales; restricting to one order is a partial taxonomic control, and the abstract does not say whether sampling effort was balanced.
  conf: single (marker) · class: deriv (marker) · holds: soil metagenomes; within-order resolution; the answers call it positive selection · src: ghalyAgricultureAltersProtein2026 (abstract only; derived; SINGLE SOURCE) · trail: C-DENIT §3.2, §answers, §critic · from: C-DENIT:I-0019, C-DENIT:B-0134, C-DENIT:B-0135, C-DENIT:A-043, C-DENIT:C-026, C-DENIT:C-079
- **habitat-controlled.5** Of 1556 bradyrhizobial nodule isolates from 32 Japanese soils, the 11 soils dominated by nosZ- isolates were all Andosols and the 17 dominated by nosZ+ isolates were mainly alluvial soils (chi-square P < 0.05); nosZ- dominance correlated with total C, total N and phosphate absorption coefficient.
  conf: single (marker) · class: meas (marker) · holds: PCR-typed nodule isolates of indigenous soybean bradyrhizobia; ITS primers designed for B. japonicum, which the authors note biases recovery · src: shiinaRelationshipSoilType2014 (full text, checked; measured; SINGLE SOURCE) · trail: C-DENIT §3.2, §answers · from: C-DENIT:B-0136, C-DENIT:B-0139, C-DENIT:A-072, C-DENIT:I-0020, C-DENIT:A-044, C-DENIT:A-083, C-DENIT:R-0123
- **habitat-controlled.6** In the same isolates all 125 typed nosZ+ isolates fell in cluster BJ1 (now B. diazoefficiens), and 92 of 112 nosZ- isolates (82%) fell in BJ2 (B. japonicum sensu stricto), all of which were nosZ-; so the habitat association is carried by a lineage split close to a species boundary, taxonomy was not controlled, and the habitat signal is carried by lineage.
  conf: single (marker) · class: meas (marker) · holds: indigenous soybean bradyrhizobia of 32 Japanese soils; the only formal habitat test below genus level · src: shiinaRelationshipSoilType2014 (full text, checked; measured; SINGLE SOURCE) · trail: C-DENIT §3.2, §answers, §critic, §Provenance · from: C-DENIT:I-0020, C-DENIT:B-0137, C-DENIT:A-044, C-DENIT:A-045, C-DENIT:C-027, C-DENIT:B-0015, C-DENIT:B-0136, C-DENIT:A-072, C-DENIT:R-0123
- **habitat-controlled.7** The authors of the Andosol study discuss unknown "determinants for soil adaptation" in the core genome.
  conf: not stated · class: not stated · holds: soybean bradyrhizobia · src: shiinaRelationshipSoilType2014 · trail: C-DENIT §3.2 · from: C-DENIT:B-0138
- **habitat-controlled.8** In 365 soil metagenomes (10 habitat categories), habitat, soil C and soil N largely explained pathway frequencies, but "the dominant genera encoding a pathway were generally similar among habitat types", and the authors could not identify major drivers of functional-group taxonomy; denitrification is treated as a pathway, not per gene, so the result concerns pathways, not genes, and cannot serve as a control.
  conf: single (critic: C-080) · class: not stated · holds: soil metagenomes; a community-level contrary result on the taxon side; the reported ~12% explained variance and R2 = 0.58 are unverified · src: nelsonGlobalBiogeographyMicrobial2016 (abstract quote verified by a search agent) · trail: C-DENIT §3.2, §answers, §critic · limit: access (note: "full text read via a summarising tool, so the reported ~12% explained variance and R2 = 0.58 are unverified") · contrary: one-sided (critic: C-116) · from: C-DENIT:B-0140, C-DENIT:B-0141, C-DENIT:B-0142, C-DENIT:A-046, C-DENIT:A-047, C-DENIT:A-105, C-DENIT:C-028, C-DENIT:C-029, C-DENIT:C-080
- **habitat-controlled.9** Pold 2025 tested residual phylogenetic signal in genome-trait regressions (Blomberg's K < 1 "in all instances (P < 0.05)") and so omitted phylogenetic random effects; the sentence does not make clear whether P refers to a test against K = 0 or K = 1, one search agent reads it as detectable sub-Brownian signal, and either way it is a check on trait regressions, not on habitat associations.
  conf: not stated · class: not stated · holds: genome-trait regressions over GTDB genomes · src: poldDenitrificationCommunityTrait2025 (checked) · trail: C-DENIT §3.2, §answers, §critic · from: C-DENIT:B-0143..0146, C-DENIT:A-048, C-DENIT:C-030, C-DENIT:B-0085
- **habitat-controlled.10** Pold 2024's phylogenetically constrained Mantel tests relate Nir sequence to gene content, not to habitat, so they are indirect for gene-habitat questions.
  conf: not stated · class: not stated · holds: the 2024 Nir survey · src: poldPhylogeneticsEnvironmentalDistribution2024 · trail: C-DENIT §3.2 · from: C-DENIT:B-0147, C-DENIT:B-0148
- **habitat-controlled.11** For the controlled case, removing Shiina 2014 or Ghaly 2026 leaves one partial case, and removing Nelson 2016 removes the only contrary result on the taxon side.
  conf: not stated · class: reading (note: "Single-source sensitivity") · holds: the D2 evidence base · src: none (the reviewer's sensitivity reading) · trail: C-DENIT §answers · from: C-DENIT:A-064, C-DENIT:A-065, C-DENIT:A-066

### within-genus: gene combinations within one species or genus
needs: denitrification-genes, gene-transfer
- **within-genus.1** Variation in gene combinations below genus level is documented in each of the genera the review covers, but these genera were located by searches aimed at known variable taxa, so the review cannot say how common within-genus uniformity is.
  conf: not stated · class: not stated · holds: the genera the review covers, found by targeted searches · src: none (the reviewer's synthesis, as the critic reformulated it) · trail: C-DENIT §critic, §Adversarial, §answers · contrary: one-sided (critic: C-117) · from: C-DENIT:C-031, C-DENIT:C-032, C-DENIT:C-055, C-DENIT:C-117, C-DENIT:A-067
- **within-genus.2** Some genes are near-invariant within these same taxa: nar, aniA and nor are near-universal in Ralstonia, and narG is in 23 of 24 Thermus strains.
  conf: not stated · class: not stated · holds: the Ralstonia species complex and the genus Thermus · src: truchonPlantPathogenicIRalstonia2023, jiaoComparativeGenomicAnalysis2022 · trail: C-DENIT §critic, §Adversarial · from: C-DENIT:C-033, C-DENIT:C-117
- **within-genus.3** Variation in which genes are present is documented at species level (the T. thermophilus nar-nir-nor island; B. japonicum sensu lato nosZ; Castellaniella ASV-level nos loss; P. stutzeri strains carrying both nirS and nirK), at species-complex level (Ralstonia) and at genus level (Neisseria nos and nar; Thermus nirK, nirS and norB with no nosZ; Stutzerimonas narG and nirK; Bradyrhizobium 11 complete and 129 partial of 181 strains; haloarchaeal families; Alteromonas narG loss).
  conf: not stated · class: not stated · holds: the taxa named · src: alvarezLateralTransferDenitrification2011, shiinaRelationshipSoilType2014, goffGenomicEnvironmentalControls2024, wittorfExpressionNirKNirS2018, truchonPlantPathogenicIRalstonia2023, barthBiochemicalGenomicAnalysis2009, jiaoComparativeGenomicAnalysis2022, menestreauDistinctDenitrificationPhenotypes2026, buenodemesquitaHighStrainlevelDiversity2025, mirallesrobledilloDistributionDenitrificationHaloarchaea2021, changAlteromonasNitratireducensSp2025 · trail: C-DENIT §answers · from: C-DENIT:A-070
- **within-genus.4** In the Ralstonia solanacearum species complex (51 genomes), nos is present in all phylotype I and 10 of 11 phylotype III genomes and in none of phylotypes II and IV; phylotype (lineage) accounts for nos, the gas phenotype matched (25 of 25 phylotype I and III strains made N2, 0 of 43 of II and IV), and lifestyle was constant (all xylem pathogens).
  conf: not stated · class: not stated · holds: 51 genomes of one species complex · src: truchonPlantPathogenicIRalstonia2023 (full text, checked) · trail: C-DENIT §4. D3, §critic, §answers · from: C-DENIT:B-0154..0159, C-DENIT:C-034, C-DENIT:A-071, C-DENIT:A-108
- **within-genus.5** Removing Truchon 2023 removes the cleanest case of lineage explaining gene presence.
  conf: not stated · class: reading (note: "Removing Truchon 2023 removes the cleanest lineage-explains-presence case") · holds: the D3 evidence base · src: none (the reviewer's sensitivity reading) · trail: C-DENIT §answers · from: C-DENIT:A-095
- **within-genus.6** Lineage accounts for nosZ presence largely in Japanese soybean bradyrhizobia: soil type and C, N and phosphate absorption were associated with nosZ, but lineage (BJ1 against BJ2) nearly coincides with it.
  conf: not stated · class: not stated · holds: 1556 PCR-typed isolates · src: shiinaRelationshipSoilType2014 (full text, checked) · trail: C-DENIT §4. D3, §critic · from: C-DENIT:B-0160, C-DENIT:C-034, C-DENIT:A-108, C-DENIT:A-083
- **within-genus.7** In 60 strains of B. japonicum and B. elkanii, gene composition (nap, nir, nor, nos) correlated with phylogenetic group, with exceptions attributed to rearrangement.
  conf: not stated · class: not stated · holds: 60 soybean bradyrhizobia strains · src: sameshimasaitoCorrelationDenitrifyingCapability2006 (abstract) · trail: C-DENIT §4. D3, §answers · limit: access (critic: C-073) · from: C-DENIT:B-0161, C-DENIT:A-071
- **within-genus.8** In a flooding experiment, nosZ conferred a competitive advantage on B. diazoefficiens.
  conf: not stated · class: not stated · holds: an experiment · src: saekiEffectFloodingLt2017 (abstract) · trail: C-DENIT §4. D3, §answers · limit: access (critic: C-073) · from: C-DENIT:B-0162, C-DENIT:A-075
- **within-genus.9** In 15 B. ottawaense isolates, a difference in N2O reduction was attributed to nosZ expression, not to the NosZ sequence.
  conf: not stated · class: not stated · holds: 15 isolates · src: wasaiharaDiversityLtI2020 (abstract), wasaiharaBradyrhizobiumOttawaenseEfficiently2023 (abstract) · trail: C-DENIT §4. D3 · from: C-DENIT:B-0163
- **within-genus.10** In 181 Bradyrhizobium genomes from across Australia, 11 had complete and 129 partial denitrification gene sets; strain composition related to environment, but denitrification gene content was not tested against it, and only 2 of 181 assemblies had plasmids, a risk of false absence.
  conf: not stated · class: not stated · holds: 181 genomes from Australian soils · src: buenodemesquitaHighStrainlevelDiversity2025 (full text per agent) · trail: C-DENIT §4. D3, §answers, §6. Limits · from: C-DENIT:B-0164, C-DENIT:B-0165, C-DENIT:A-080, C-DENIT:B-0195
- **within-genus.11** In Castellaniella (14 genomes), nos was lost in ASV1 strains and narGHI was absent in one MAG; a mobile-element insertion carrying copper resistance replaced nos at its locus, co-occurring with lower site abundance and metal tolerance; causality was proposed, not tested.
  conf: not stated · class: not stated · holds: 14 genomes from one disturbed subsurface site · src: goffGenomicEnvironmentalControls2024 (full text per agent) · trail: C-DENIT §4. D3, §answers · from: C-DENIT:B-0166, C-DENIT:A-073
- **within-genus.12** In Thermus (23 or 24 strains), narG is in 23 of 24, nirS in 14, nirK in 9, norB in 14 and nosZ in none; phenotypes were inconsistent within three species, and spring physicochemical variables were recorded but not tested.
  conf: not stated · class: not stated · holds: 23 or 24 Thermus strains from geothermal spring sediments and adjacent soils in southwest China; spring chemistry · src: jiaoComparativeGenomicAnalysis2022 (abstract), mefferdIncompleteDenitrificationPhenotypes2022 (full text per agent) · trail: C-DENIT §4. D3, §answers · from: C-DENIT:B-0168, C-DENIT:B-0169, C-DENIT:A-079, C-DENIT:R-0099
- **within-genus.13** In Neisseria (12 species or biovars), nar occurs only in N. mucosa and nos only in commensals, and aniA carries frameshifts in 32% of N. meningitidis; pathogenic against commensal lifestyle was related to nos descriptively.
  conf: not stated · class: not stated · holds: 12 Neisseria species or biovars · src: barthBiochemicalGenomicAnalysis2009 (full text per one agent) · trail: C-DENIT §4. D3, §answers, §6. Limits · from: C-DENIT:B-0170, C-DENIT:A-074, C-DENIT:B-0198
- **within-genus.14** In Stutzerimonas (18 strains; 314 genomes for nirK), narG is in 16 of 18 strains and nirK in 7 of 18 (111 of 314 genomes); MLSA phylogeny showed limited congruence with nitrite-accumulation phenotype, narG presence, nirS clade, nirTB and dnrE accounted for part of it, a dnrE knockout did not shift phenotype as predicted, and isolation source was not analysed.
  conf: not stated · class: not stated · holds: 18 strains and 314 genomes · src: menestreauDistinctDenitrificationPhenotypes2026 (full text per agent) · trail: C-DENIT §4. D3, §answers · from: C-DENIT:B-0171, C-DENIT:A-078
- **within-genus.15** In two P. stutzeri strains carrying both nirS and nirK, the genes were differentially expressed, which was attributed to gene arrangement.
  conf: not stated · class: not stated · holds: two strains · src: wittorfExpressionNirKNirS2018 (abstract) · trail: C-DENIT §4. D3 · from: C-DENIT:B-0172
- **within-genus.16** In 8 Thauera strains, denitrification regulatory phenotype did not correlate with phylogeny (16S and functional genes).
  conf: not stated · class: not stated · holds: 8 strains; a phenotype, not gene presence · src: liuStrainsGenusI2013 (abstract) · trail: C-DENIT §4. D3, §answers · limit: access (critic: C-073) · from: C-DENIT:B-0173, C-DENIT:A-077
- **within-genus.17** In Azospirillum (41 isolates from one paddy; nirK in 37, nirS in 4), nir-nor sits on a composite transposon, and HGT from close relatives was inferred.
  conf: not stated · class: not stated · holds: one paddy field · src: jangPotentiallyMobileDenitrification2019 (full text per agent) · trail: C-DENIT §4. D3 · from: C-DENIT:B-0175
- **within-genus.18** In commercial Sinorhizobium (alfalfa) inoculants nos was lost, and domestication was related to the loss descriptively.
  conf: not stated · class: not stated · holds: commercial alfalfa inoculants · src: brambillaAbsenceNitrousOxide2018 (abstract) · trail: C-DENIT §4. D3, §answers, §References · from: C-DENIT:B-0176, C-DENIT:A-076, C-DENIT:R-0060
- **within-genus.19** Among haloarchaea, analysed by family because genera were too sparse, 12% are complete and 58% partial denitrifiers; families differ, a soda-lake lifestyle was suggested but not tested, and nar and nos sit on plasmids.
  conf: not stated · class: not stated · holds: haloarchaeal families · src: mirallesrobledilloDistributionDenitrificationHaloarchaea2021 (full text per agent) · trail: C-DENIT §4. D3 · from: C-DENIT:B-0177
- **within-genus.20** Of three Haloferax species, only H. mediterranei consistently reduced to N2.
  conf: not stated · class: not stated · holds: three species; a phenotype · src: torregrosacrespoDenitrifyingHaloarchaeaGenus2018 (abstract) · trail: C-DENIT §4. D3 · from: C-DENIT:B-0178
- **within-genus.21** In Bacillus (180 strains; 14 isolates), the choice of assay acceptor and donor changed detection, and the pH effect exceeded genotypic variation.
  conf: not stated · class: not stated · holds: 180 Bacillus strains and 14 closely related soil Bacillus isolates harbouring nosZ; phenotypes · src: verbaendertDenitrificationCommonFeature2011 (abstract), jonesPhenotypicGenotypicHeterogeneity2011 (abstract) · trail: C-DENIT §4. D3, §answers · from: C-DENIT:B-0179, C-DENIT:A-081, C-DENIT:R-0087
- **within-genus.22** In the Bacillota (class Bacilli, 17 genera), with their NOR types and clade II nosZ, 11 genomes would be misclassified with KO annotation only.
  conf: not stated · class: not stated · holds: endospore-forming Bacillota genomes · src: bellDenitrificationGenotypesEndosporeforming2024 (full text per agent) · trail: C-DENIT §4. D3, §6. Limits · from: C-DENIT:B-0180, C-DENIT:B-0195
- **within-genus.23** Habitat was formally tested once below genus level (Shiina 2014), and there it is confounded with lineage; removing that study leaves the within-genus habitat question answered only descriptively (Neisseria, Castellaniella, Sinorhizobium).
  conf: single (critic: C-038) · class: not stated · holds: soybean bradyrhizobia · src: shiinaRelationshipSoilType2014 · trail: C-DENIT §critic, §answers, §8. Answers · from: C-DENIT:C-038, C-DENIT:A-094, C-DENIT:A-111
- **within-genus.24** The other variables related to gene combinations (lifestyle in Neisseria, domestication in Sinorhizobium, metals in Castellaniella) are descriptive associations.
  conf: not stated · class: not stated · holds: Neisseria, Sinorhizobium and Castellaniella · src: barthBiochemicalGenomicAnalysis2009, brambillaAbsenceNitrousOxide2018, goffGenomicEnvironmentalControls2024 · trail: C-DENIT §critic, §8. Answers · from: C-DENIT:C-039, C-DENIT:A-112
- **within-genus.25** Phenotype studies (Thauera, Stutzerimonas, Bacillus, Haloferax) measure a different thing from gene presence: lineage explains gene combination in Ralstonia and soybean Bradyrhizobium, but phylogeny did not account for phenotype in Thauera and only partly in Stutzerimonas, and these are not strictly the same measurement.
  conf: not stated · class: not stated · holds: the phenotype and gene-presence studies named · src: liuStrainsGenusI2013, menestreauDistinctDenitrificationPhenotypes2026, verbaendertDenitrificationCommonFeature2011, torregrosacrespoDenitrifyingHaloarchaeaGenus2018 · trail: C-DENIT §critic, §answers, §8. Answers · from: C-DENIT:C-040, C-DENIT:A-069, C-DENIT:A-085, C-DENIT:A-110
- **within-genus.26** Each within-genus case is a single study, usually of 8 to 51 genomes (except Shiina's 1556 PCR-typed isolates and Bueno de Mesquita's 181); explanatory tests are rare, mostly descriptive, and seldom separate lineage from habitat.
  conf: single (critic: C-041) · class: not stated · holds: the within-genus studies the review covers · src: none (the reviewer's synthesis) · trail: C-DENIT §critic, §answers, §8. Answers · rating: "Weak to moderate" · from: C-DENIT:C-041, C-DENIT:A-082, C-DENIT:A-083, C-DENIT:A-084, C-DENIT:A-113
- **within-genus.27** No pangenome-scale single-species study relates denitrification gene combinations to isolation habitat with a formal test, and none controls for lineage.
  conf: not stated · class: search (note: "By the search agents' genus-specific Europe PMC searches") · holds: genus-specific Europe PMC searches (Bradyrhizobium, Pseudomonas and Stutzerimonas, Halomonas, Thauera, Paracoccus, Rhodanobacter, Neisseria, Shewanella, Sinorhizobium, Achromobacter, Cupriavidus, Thermus, Bacillus) · src: none (a search result) · trail: C-DENIT §answers, §Provenance · search: searched, not found (note: "By the search agents' genus-specific Europe PMC searches") · from: C-DENIT:A-088, C-DENIT:B-0017
- **within-genus.28** There is no within-genus study of NOR types other than Bell 2024 (Bacillota), and no within-genus analysis for nosZ clade II carriers besides the Bacillota and Castellaniella cases.
  conf: not stated · class: search (note: "By the search agents' genus-specific Europe PMC searches") · holds: the same genus-specific searches · src: bellDenitrificationGenotypesEndosporeforming2024, goffGenomicEnvironmentalControls2024 · trail: C-DENIT §answers · search: searched, not found (note: "By the search agents' genus-specific Europe PMC searches") · from: C-DENIT:A-089, C-DENIT:A-090, C-DENIT:A-088

### genotype-phenotype: gene content against denitrification phenotype
needs: within-genus
- **genotype-phenotype.1** Lycus et al. isolated 176 strains from soils of pH 3.7 and 7.4; genomes confirmed most truncations, but "phenotypes cannot be predicted solely from genetic potential".
  conf: not stated · class: not stated · holds: soil isolates; details such as nosZ-carrying Rhodanobacter not reducing N2O and a ~23% mismatch come via a summarising fetch and are unverified · src: lycusPhenotypicGenotypicRichness2017 (abstract quote verified) · trail: C-DENIT §4. D3, §answers, §6. Limits · limit: access (note: "come via a summarising fetch and are unverified") · from: C-DENIT:B-0182, C-DENIT:B-0183, C-DENIT:B-0184, C-DENIT:A-081, C-DENIT:A-092, C-DENIT:B-0198
- **genotype-phenotype.2** In another soil set, N-oxide production was "not always predicted by the genetic potential".
  conf: not stated · class: not stated · holds: soil bacteria · src: rocoModularityNitrogenoxideReducing2016 (abstract only) · trail: C-DENIT §4. D3, §answers · from: C-DENIT:B-0185, C-DENIT:A-081
- **genotype-phenotype.3** These results bound any inference from gene combinations to function within a genus.
  conf: not stated · class: not stated · holds: within a genus · src: none (the reviewer's synthesis) · trail: C-DENIT §4. D3 · from: C-DENIT:B-0186

### limits: detection, sampling and metadata limits
needs: denitrification-genes
- **limits.1** Complete denitrifiers were 29% of isolate genomes against 17% of MAGs in the same filtered set, and the authors attribute this to fast laboratory growth.
  conf: single (critic: C-084) · class: not stated · holds: GTDB isolate genomes and MAGs after quality filtering (80% completeness, 5% contamination) · src: poldDenitrificationCommunityTrait2025 (checked) · trail: C-DENIT §6. Limits, §Adversarial · from: C-DENIT:B-0191, C-DENIT:C-084, C-DENIT:C-105, C-DENIT:B-0085
- **limits.2** The reviewer adds that the isolate-against-MAG figure is equally consistent with false absence in MAGs.
  conf: not stated · class: reading (critic: C-127) · holds: the same genome set · src: none (the reviewer's alternative) · trail: C-DENIT §6. Limits, §Adversarial · from: C-DENIT:B-0192, C-DENIT:C-127
- **limits.3** Isolate-era congruence studies used cultured organisms only.
  conf: not stated · class: not stated · holds: the isolate-era congruence studies · src: none (the reviewer's synthesis) · trail: C-DENIT §6. Limits · from: C-DENIT:B-0193
- **limits.4** Sources of false absence include incomplete MAGs, unassembled plasmids, NOR types missing from KO annotation, restricted NOR search sets (Graf 2014 searched only cnorB, qnorB and P450nor), primer failure and assay-dependent phenotypes.
  conf: not stated · class: not stated · holds: the studies named · src: buenodemesquitaHighStrainlevelDiversity2025, bellDenitrificationGenotypesEndosporeforming2024, grafIntergenomicComparisonsHighlight2014, verbaendertDenitrificationCommonFeature2011 · trail: C-DENIT §6. Limits · from: C-DENIT:B-0195
- **limits.5** Sources of false presence include qnorB in non-denitrifiers and genes present but not functional (frameshifts in Neisseria aniA; non-reducing nosZ carriers, an unverified detail); Pold 2025 excluded nor-only genomes as likely detoxifiers.
  conf: not stated · class: not stated · holds: the studies named · src: brakerNitricOxideReductase2003, poldDenitrificationCommunityTrait2025, barthBiochemicalGenomicAnalysis2009, lycusPhenotypicGenotypicRichness2017 (unverified detail) · trail: C-DENIT §6. Limits · from: C-DENIT:B-0196, C-DENIT:B-0197, C-DENIT:B-0198
- **limits.6** Habitat metadata are coarse: GOLD single labels (Graf 2014), NCBI source labels (Intrator 2024, 2025), ecoregion by coordinates (Pold 2024, 2025), and gridded covariates at 0.01 to 4 degree resolution (Nelson 2016, via a summarising tool).
  conf: not stated · class: not stated · holds: the studies named · src: grafIntergenomicComparisonsHighlight2014, intratorAquaticNitrousOxide2024, intratorAquaticCoppercontainingNitrite2025, poldPhylogeneticsEnvironmentalDistribution2024, poldDenitrificationCommunityTrait2025, nelsonGlobalBiogeographyMicrobial2016 (via summarising tool) · trail: C-DENIT §6. Limits · from: C-DENIT:B-0199
- **limits.7** Gene trees carry artefacts: in Graf 2014 bootstrap support above 70% held at only 48% of nirK nodes and 63 to 66% of other nodes; 25% of NirK sequences fell in a poorly supported region (Pold 2024); and Intrator 2024 and 2025 used short fragments (70 to 277 bp regions).
  conf: not stated · class: not stated · holds: the studies named · src: grafIntergenomicComparisonsHighlight2014, poldPhylogeneticsEnvironmentalDistribution2024, intratorAquaticNitrousOxide2024, intratorAquaticCoppercontainingNitrite2025 · trail: C-DENIT §6. Limits · from: C-DENIT:B-0200, C-DENIT:B-0201
- **limits.8** Sampling is sparse: Parsons 2021 had 10 nirK and 21 nosZ genes (species tree of 308 genomes, gene searches on 254), and Graf 2014 could not test below order for small cell counts.
  conf: not stated · class: not stated · holds: the studies named · src: parsonsRadiationNitrogenmetabolizingEnzymes2020, grafIntergenomicComparisonsHighlight2014 · trail: C-DENIT §6. Limits, §Adversarial · from: C-DENIT:B-0202, C-DENIT:B-0203, C-DENIT:C-085
- **limits.9** Genome-quality thresholds differ between studies: Pold 2024 used a 90% completeness and 5% contamination filter (80% for eukaryotes), and Pold 2025 used 80% and 5%; the review does not state them.
  conf: not stated · class: not stated · holds: the two Pold studies, verified by the critic · src: poldPhylogeneticsEnvironmentalDistribution2024, poldDenitrificationCommunityTrait2025 · trail: C-DENIT §Adversarial · from: C-DENIT:C-105

## Do not say
- **dns.1** "nirK is the least congruent denitrification gene, consistently across datasets."
  why: The only reconciliation (Parsons 2021) gives nirK the lowest transfer-to-speciation ratio of the four genes (4:9), so it contradicts the ranking at the nirK end, and the review did not call this a conflict; the answers state this point more firmly than the evidence supports. · instead: gene-ranking.1, nirk.6, reconciliation.2 · trail: C-DENIT §critic, §8. Answers · from: C-DENIT:C-042, C-DENIT:C-043, C-DENIT:C-044, C-DENIT:C-045, C-DENIT:C-046, C-DENIT:A-005, C-DENIT:A-096, C-DENIT:B-0037
- **dns.2** "nosZ is the most 16S-congruent denitrification gene under formal tests."
  why: The claim rests on one non-rejection (P = 0.14, per a search agent) in the nirK-genome subset of Jones 2008, a paper the synthesis agent never read, whose abstract reports substantial differences in its partial-sequence monophyly analyses of all four genes; the other support is qualitative or secondary. · instead: nosz.8, nosz.2, gene-ranking.1 · trail: C-DENIT §critic · from: C-DENIT:C-047, C-DENIT:C-048, C-DENIT:C-074, C-DENIT:A-096
- **dns.3** "Denitrification genes show moderate and replicated habitat associations."
  why: Each gene-habitat claim rests on one study, many abstract-only and primer-based; the answer pools amplicon or primer data, metagenome read placement, genome label tests and MAG community modularity into a single judgement, and no single gene-habitat association has been replicated across independent data types. · instead: habitat-uncontrolled.1 · trail: C-DENIT §critic, §Adversarial · from: C-DENIT:C-049, C-DENIT:C-050, C-DENIT:C-122, C-DENIT:A-106
- **dns.4** "Mobile elements account for the gene combinations in Castellaniella, Thermus and Azospirillum."
  why: The review's own table says causality was not tested in Castellaniella, shows only laboratory transferability in Thermus and an inference in Azospirillum, and in Thermus the genus-level study infers vertical inheritance for most genes. · instead: gene-transfer.10 · trail: C-DENIT §critic, §8. Answers · from: C-DENIT:C-052, C-DENIT:C-053, C-DENIT:A-068, C-DENIT:A-109
- **dns.5** "Gene combinations vary below genus level in every genus examined."
  why: This follows from searches targeted at variable genera; it is not a property of genera in general, and invariance within the same taxa is in the table but was not treated as a result. · instead: within-genus.1, within-genus.2 · trail: C-DENIT §critic, §8. Answers · from: C-DENIT:C-054, C-DENIT:C-055, C-DENIT:A-107
- **dns.6** "K-types are over-represented in animal-host prokaryotes in Graf 2014's 652 prokaryotic genomes."
  why: Graf 2014's 652 microbial genomes include fungal (Ascomycota) genomes, whose nirK and P450nor are the labelled eukaryotic case, and the review folds them into the prokaryotic result without labelling them. · instead: habitat-uncontrolled.6, habitat-uncontrolled.5 · trail: C-DENIT §Adversarial · from: C-DENIT:C-086, C-DENIT:C-118
- **dns.7** "Graf 2014 cautioned that the GOLD data were not detailed enough to confirm its habitat test."
  why: In the full text that statement is about specific hypotheses from other studies (nirS dominance and habitat filtering in marine systems), not about the authors' whole habitat test. · instead: habitat-uncontrolled.8 · trail: C-DENIT §Adversarial · from: C-DENIT:C-068, C-DENIT:C-016
- **dns.8** "Graf 2014 found habitat and taxonomy confounded, because animal-host genomes are largely pathogens."
  why: Graf does not state this; it is the reviewer's argument, written into the description of Graf's results. · instead: habitat-uncontrolled.3 · trail: C-DENIT §Adversarial · from: C-DENIT:C-069, C-DENIT:C-070, C-DENIT:C-125, C-DENIT:A-050
- **dns.9** "qnorB presence is a weak marker of respiratory denitrification."
  why: This is the reviewer's inference, presented as a finding. · instead: nor-types.4 · trail: C-DENIT §Adversarial · from: C-DENIT:C-124
- **dns.10** "Complete denitrifiers carry clade I nosZ in 74% of cases and clade II in 26%."
  why: The 74% against 26% figure is ambiguous in the full text: it could be the share of complete denitrifiers carrying each clade, or the fraction of each clade's carriers that are complete denitrifiers, and the review set it against Hexter 2026 and Bell 2024 without resolving the denominator. · instead: habitat-uncontrolled.14 · trail: C-DENIT §Adversarial · from: C-DENIT:C-072
- **dns.11** "Shiina 2014 shows that the USDA110 nos cluster sits in a genomic island."
  why: In Shiina 2014's full text this is a citation of earlier genome comparisons, so the evidence is secondary, yet the D1 answer uses it as one of three direct cases of nos mobility. · instead: gene-transfer.2 · trail: C-DENIT §Adversarial · from: C-DENIT:C-057, C-DENIT:C-058, C-DENIT:C-059
- **dns.12** "Parsons 2021 reconciled 308 genomes with 10 to 36 gene copies per gene."
  why: In the full text the species tree has 308 genomes, but the gene searches ran on 254 bacterial and archaeal genomes, and gene counts run from 10 (nirK) to 37 (napA). · instead: reconciliation.1 · trail: C-DENIT §Adversarial, §answers · from: C-DENIT:C-085, C-DENIT:A-006
- **dns.13** "Direct experimental transfer has been shown only for the Thermus nar, nir and nor island."
  why: This rests on one abstract-only study (Alvarez 2011) and is phrased as a property of the literature, with no search routes named. · instead: gene-transfer.5 · trail: C-DENIT §Adversarial · from: C-DENIT:B-0187, C-DENIT:C-081
- **dns.14** "Topology tests and the reconciliation are not directly comparable, so their nosZ results do not conflict."
  why: The reviewer's reading that both can hold is labelled, but it then shapes the D1 conflicts framing ('not directly comparable'), which softens a genuine conflict in the literature. · instead: gene-ranking.1, gene-ranking.3 · trail: C-DENIT §Adversarial · from: C-DENIT:C-126, C-DENIT:A-008
- **dns.15** "Pre-2012 nosZ congruence results are, as a fact, results for nosZ clade I."
  why: Equating them is reasonable, but Intrator 2024's congruence discussion and Palmer 2009's nosZ data were not checked for clade, and the answer states the equation as fact. · instead: nosz.9 · trail: C-DENIT §Adversarial · from: C-DENIT:C-119
- **dns.16** "Parsons 2021's norB transfer counts apply to cnorB and qnorB as measured by Heylen 2007."
  why: Parsons 2021's norB is not split by NOR type, yet the review sets it against cnorB and qnorB results from Heylen 2007 as if the same gene. · instead: reconciliation.4, nor-types.1 · trail: C-DENIT §Adversarial · from: C-DENIT:C-120
- **dns.17** "Phenotype studies in Thauera, Stutzerimonas, Bacillus and Haloferax show what accounts for variation in gene combinations."
  why: These phenotype results measure a different thing from gene presence; the review acknowledges this in its conflicts note but not in the answer summary. · instead: within-genus.25 · trail: C-DENIT §Adversarial, §critic · from: C-DENIT:C-121, C-DENIT:C-040
- **dns.18** "The nos-cluster islands in Bradyrhizobium, Castellaniella and Ralstonia, and the Thermus laboratory transfer, measure gene-tree incongruence."
  why: They measure genomic context and transferability, not gene-tree against species-tree fit, though the D1 answer places them alongside tree-congruence measures. · instead: gene-transfer.1 · trail: C-DENIT §Adversarial · from: C-DENIT:C-123
- **dns.19** "Lineage accounts for gene presence in soybean bradyrhizobia, and Thauera and earthworm-gut nosZ give null results."
  why: Many D3 table entries and D2 statements rest on abstracts (Sameshima-Saito 2006, Liu 2013, Horn 2006 among them), and the abstract-only access does not support categorical wording such as 'lineage accounts for' and 'null'. · instead: within-genus.6, within-genus.7, within-genus.16, habitat-uncontrolled.21 · trail: C-DENIT §Adversarial · from: C-DENIT:C-073
- **dns.20** "Martiny 2013 and Goberna and Verdú 2016 were read in full and report no denitrification-step conservatism."
  why: They were read through a summarising tool, which is not a reading of the full text, and their labels support a negative claim. · instead: estimate-moderators.10 · trail: C-DENIT §Adversarial · from: C-DENIT:C-063, C-DENIT:C-064, C-DENIT:C-066

## Gaps
- **gap.1** Plasmid- and megaplasmid-borne denitrification clusters as background on transfer: Cupriavidus necator H16 (denitrification genes on megaplasmid pHG1) and Sinorhizobium meliloti (nap, nir, nor and nos on pSymA), as replicon-location evidence for HGT per gene in Burkholderiales and Rhizobiales.
  blocks: gene-transfer · origin: critic coverage gap; not covered in the review's background section · search: not stated · from: C-DENIT:C-098
- **gap.2** Environmental narG and napA surveys against habitat (narG and napA qPCR or amplicon studies across soils and sediments, for example by the Philippot group); the review has no narG habitat evidence apart from Ghaly 2026, and napA only in one WWTP study.
  blocks: habitat-uncontrolled · origin: critic coverage gap; stage 2 check triggered a follow-up brief · search: not stated · from: C-DENIT:C-099, C-DENIT:B-0021
- **gap.3** Large MAG catalogues with habitat metadata (GEM or OceanDNA-type catalogues, Tara Oceans MAGs) tested for denitrification gene presence against habitat with phylogenetic control; the absence is claimed but the search routes named are keyword searches only.
  blocks: habitat-controlled · origin: critic coverage gap; stage 2 check triggered a follow-up brief · search: searched, not found (critic: C-100) · from: C-DENIT:C-100, C-DENIT:B-0021
- **gap.4** Congruence of nosZ clade II with organism phylogeny, especially in non-denitrifier N2O reducers (Bacteroidota, Anaeromyxobacter, Gemmatimonadota); Hallin 2018 is listed as background only, and Sanford 2012 was not examined for a tree comparison.
  blocks: nosz · origin: critic coverage gap; stage 2 check triggered a follow-up brief · search: not searched (critic: C-103) · src: hallinGenomicsEcologyNovel2018, sanfordUnexpectedNondenitrifierNitrous2012 · from: C-DENIT:C-101, C-DENIT:C-102, C-DENIT:C-103, C-DENIT:B-0021
- **gap.5** Paralogy and multi-copy handling in the older congruence studies: known multi-copy cases (two active nirS copies in a Thauera strain; two nosZ copies in Bacillus) were not collected systematically, and how paralogues were handled in each congruence study is not reported.
  blocks: estimate-moderators · origin: critic coverage gap; the brief asked for it · search: not stated · from: C-DENIT:C-104
- **gap.6** Genome completeness criteria per study, requested by the brief, are reported only sporadically.
  blocks: estimate-moderators · origin: critic coverage gap · search: not stated · from: C-DENIT:C-105
- **gap.7** Function-from-16S prediction accuracy for denitrification genes (PICRUSt-type or NSTI benchmarks, Goberna and Verdú trait predictions, Louca 2016), indirect evidence on phylogenetic conservatism per gene, listed as not obtained or not checked.
  blocks: gene-trees · origin: critic coverage gap · search: not stated · src: gobernaPredictingMicrobialTraits2016, loucaDecouplingFunctionTaxonomy2016 · from: C-DENIT:C-106
- **gap.8** Within-species pangenome studies in model denitrifiers: Pseudomonas stutzeri genomovars (Lalucat 2006 not obtained), the Paracoccus pangenome (a 2023 PLoS ONE six-type-strain pangenome), the Pseudomonas aeruginosa and P. fluorescens groups, Achromobacter and Shewanella; named as searched, but the results are not reported.
  blocks: within-genus · origin: critic coverage gap; stage 2 check triggered a follow-up brief · search: not stated · src: lalucatBiologyPseudomonasStutzeri2006 · from: C-DENIT:C-107, C-DENIT:B-0021
- **gap.9** Clinical and host-associated species with large genome sets (Neisseria meningitidis aniA and norB across thousands of genomes, Pseudomonas aeruginosa nir and nos, Campylobacterota), where within-species variation could be related to isolation source with lineage control; the stage 2 check excludes this under the clinical-scope rule, except for any general pattern it establishes.
  blocks: within-genus · origin: critic coverage gap, excluded from the follow-up by the stage 2 check · search: not stated · from: C-DENIT:C-108, C-DENIT:B-0023
- **gap.10** Archaeal denitrifiers other than haloarchaea (Pyrobaculum, Thermoproteota nirK and nor) and ammonia-oxidising archaea nirK, for congruence and habitat.
  blocks: gene-trees, habitat-uncontrolled · origin: critic coverage gap; stage 2 check triggered a follow-up brief · search: not stated · from: C-DENIT:C-109, C-DENIT:B-0021
- **gap.11** Fungal denitrification genes against habitat (P450nor and fungal nirK distributions by ecological niche); the eukaryotic case is covered only for origin.
  blocks: eukaryotic · origin: critic coverage gap; stage 2 check triggered a follow-up brief · search: not stated · from: C-DENIT:C-110, C-DENIT:B-0021
- **gap.12** The stage 2 check was triggered: the critic's gaps name a nosZ clade, lineage groups, and habitats and data types not searched, so a targeted follow-up brief on these is to be written, sized separately.
  blocks: none · origin: the note's stage 2 check (ROUTING condition met) · search: not stated · from: C-DENIT:B-0020, C-DENIT:B-0021, C-DENIT:B-0022
- **gap.13** Jones 2008, the main formal congruence test, was read in full by one search agent only; the synthesis reached only its abstract (OUP blocked, no Europe PMC copy), so the 43-genome and P = 0.14 figures that the D1 strength statement and its sensitivity note rest on are unverified.
  blocks: nosz, gene-ranking · origin: a source not obtained that matters · search: not stated · src: jonesPhylogeneticAnalysisNitrite2008 · from: C-DENIT:C-060, C-DENIT:B-0016, C-DENIT:B-0035, C-DENIT:B-0036, C-DENIT:A-027, C-DENIT:A-101, C-DENIT:R-0013, C-DENIT:R-0028, C-DENIT:R-0038, C-DENIT:R-0039
- **gap.14** Full texts in parseable form of Nelson 2016 and Lycus 2017, and the supplementary tables of Pold 2024 (copy counts, S4, S6), Pold 2025 (Supplementary Table 1), Murali 2024 (Dataset S7), Martiny 2013 and Goberna and Verdú 2016 (trait lists), were not obtained.
  blocks: habitat-controlled, genotype-phenotype, habitat-uncontrolled, estimate-moderators · origin: sources not obtained that matter · search: not stated · src: nelsonGlobalBiogeographyMicrobial2016, lycusPhenotypicGenotypicRichness2017, poldPhylogeneticsEnvironmentalDistribution2024, poldDenitrificationCommunityTrait2025, muraliDiversityEvolutionNitric2024, martinyPhylogeneticConservatismFunctional2013, gobernaPredictingMicrobialTraits2016 · from: C-DENIT:R-0041, C-DENIT:R-0042, C-DENIT:R-0043, C-DENIT:R-0046, C-DENIT:R-0025, C-DENIT:R-0026, C-DENIT:R-0027, C-DENIT:R-0030, C-DENIT:A-062, C-DENIT:A-092
- **gap.15** Full texts of the abstract-only primary studies behind much of the habitat and within-genus evidence were not obtained: Heylen 2006 and 2007, Jones and Hallin 2010, Juhanson 2017, Wittorf 2016 and Ming 2024 (Europe PMC abstract only; Wiley and Nature not attempted).
  blocks: habitat-uncontrolled, within-genus · origin: sources not obtained that matter · search: not stated · src: heylenIncidenceNirSNirK2006, heylenNitricOxideReductase2006, jonesEcologicalEvolutionaryFactors2010, juhansonSpatialPhyloecologicalAnalyses2017, wittorf2016, mingInsightsEvolutionaryEcological2024 · from: C-DENIT:R-0017, C-DENIT:R-0021, C-DENIT:R-0022, C-DENIT:R-0044, C-DENIT:C-073
- **gap.16** The full text of Albright 2019 (more than 6000 genomes) was not obtained, so whether it computed per-step trait depth could not be checked.
  blocks: estimate-moderators · origin: a source not obtained that matters · search: not stated · src: albrightComparativeGenomicsNitrogen2018 · from: C-DENIT:R-0012, C-DENIT:R-0014, C-DENIT:R-0015, C-DENIT:R-0016, C-DENIT:R-0029, C-DENIT:R-0040, C-DENIT:B-0090
- **gap.17** The denominator of Pold 2025's 74% against 26% clade split is unresolved, so the clade of nosZ in complete denitrifiers cannot be compared across datasets.
  blocks: habitat-uncontrolled.14 · origin: critic access error, unresolved · search: not stated · src: poldDenitrificationCommunityTrait2025 · from: C-DENIT:C-072
- **gap.18** The note's lists contradict each other on two sources: Delorme 2003 is cited as "full text per one agent" in the body but listed under Sources not obtained as a "citation from memory; not verified" known "only via citation in Intrator et al. 2024"; Saghaï 2023 is cited as "full text per agent" but listed as "seen only as a citation in Pold et al. 2025".
  blocks: narg-napa.3, estimate-moderators.9 · origin: a note that contradicts itself · search: not stated · src: delormeComparativeGeneticDiversity2003, saghaiPhyloecologyNitrateAmmonifiers2023 · from: C-DENIT:I-0015, C-DENIT:B-0087, C-DENIT:R-0005, C-DENIT:R-0006, C-DENIT:R-0023, C-DENIT:R-0024
- **gap.19** Unmeasured for congruence: napA and narG apart from the reconciliation and one RFLP study; any NOR type other than cNOR and qNOR; nosZ clade II separately; congruence against completeness thresholds, habitat-balanced sampling or depth on one genome set; and eukaryotic homologues, where only origin inferences exist.
  blocks: narg-napa, nor-types, nosz, eukaryotic, estimate-moderators · origin: the note's not-measured results and the critic's unmeasured list · search: searched, not found (note: "By the agents' Europe PMC routes and my re-reading") · from: C-DENIT:C-011, C-DENIT:A-021, C-DENIT:A-024, C-DENIT:A-099
- **gap.20** Other sources were known only as citations or from memory and not obtained: Shan 2021 (nosZ diversity and N2O), Lalucat 2006 (Pseudomonas stutzeri), studies of nosZ presence and absence across Bradyrhizobium strains (Sánchez, Minamisawa and others; Siqueira 2017), Hallin 2018, Philippot 2002, Zumft and Körner 2007 and Louca 2016; the note says none supports any claim in the review.
  blocks: none · origin: sources not obtained · search: not stated · src: shanBeyondDenitrificationRole2021, lalucatBiologyPseudomonasStutzeri2006, sanchezStudiesNosZPresence, siqueira2017, hallinGenomicsEcologyNovel2018, philippotDenitrifyingGenesBacterial2002, zumftNitrousOxideReductases2007, loucaDecouplingFunctionTaxonomy2016 · from: C-DENIT:R-0001..0011, C-DENIT:R-0018..0020, C-DENIT:R-0031..0037, C-DENIT:R-0045
- **gap.21** napA, narG and NOR types beyond cNOR and qNOR against habitat, and the eukaryotic homologues against habitat, are essentially unmeasured.
  blocks: habitat-uncontrolled · origin: the note's not-measured results and the critic's reformulated D2 answer · search: not stated · from: C-DENIT:C-020, C-DENIT:A-058, C-DENIT:A-059, C-DENIT:A-060

## Out of scope
- C-DENIT:C-087..097: reference corrections and checks (online years, initials, inverted Crossref names, issue date, DOIs resolving), applied in Sources
- C-DENIT:C-056: the critic's list of figures it verified in full text (verification record, kept in the result note)
- C-DENIT:C-128..130: expectation echo (the brief's neutrality; provenance of the critique, not a finding)
- C-DENIT:A-026..029: access basis of the D1 answer (provenance, applied in Sources)
- C-DENIT:A-061..063: access basis of the D2 answer (provenance, applied in Sources)
- C-DENIT:A-091..093: access basis of the D3 answer (provenance, applied in Sources)
- C-DENIT:A-100: access mix of the D1 summary (provenance, applied in Sources)

## Sources
```bibtex
@article{albrightComparativeGenomicsNitrogen2018,
  author = {Albright, MBN and Timalsina, B and Martiny, JBH and Dunbar, J},
  title = {Comparative genomics of nitrogen cycling pathways in bacteria and archaea},
  journal = {Microbial Ecology},
  year = {2019},
  volume = {77},
  number = {3},
  pages = {597-606},
  doi = {10.1007/s00248-018-1239-4},
  note = {access: abstract_only (full text not obtained: Springer login redirect, OSTI timeout, no PMC copy); cited as: C-DENIT [Albright2019]; year: 2019 (online 2018)}
}

@article{alvarezLateralTransferDenitrification2011,
  author = {Alvarez, L and Bricio, C and Gómez, MJ and Berenguer, J},
  title = {Lateral transfer of the denitrification pathway genes among Thermus thermophilus strains},
  journal = {Applied and Environmental Microbiology},
  year = {2011},
  volume = {77},
  number = {4},
  pages = {1352-1358},
  doi = {10.1128/AEM.02048-10},
  note = {access: abstract_only; cited as: C-DENIT [Alvarez2011]}
}

@article{alvarezTransferableDenitrificationCapability2014,
  author = {Alvarez, L and Bricio, C and Blesa, A and Hidalgo, A and Berenguer, J},
  title = {Transferable denitrification capability of Thermus thermophilus},
  journal = {Applied and Environmental Microbiology},
  year = {2014},
  volume = {80},
  number = {1},
  pages = {19-28},
  doi = {10.1128/AEM.02594-13},
  note = {access: abstract_only; cited as: C-DENIT [Alvarez2014]}
}

@article{barthBiochemicalGenomicAnalysis2009,
  author = {Barth, KR and Isabella, VM and Clark, VL},
  title = {Biochemical and genomic analysis of the denitrification pathway within the genus Neisseria},
  journal = {Microbiology},
  year = {2009},
  volume = {155},
  number = {12},
  pages = {4093-4103},
  doi = {10.1099/mic.0.032961-0},
  note = {access: full_text (per one agent); cited as: C-DENIT [Barth2009]}
}

@article{bellDenitrificationGenotypesEndosporeforming2024,
  author = {Bell, Emma and Chen, Jianwei and Richardson, William D L and Fustic, Milovan and Hubert, Casey R J},
  title = {Denitrification genotypes of endospore-forming Bacillota},
  journal = {ISME Communications},
  year = {2024},
  volume = {4},
  number = {1},
  pages = {ycae107},
  doi = {10.1093/ismeco/ycae107},
  note = {access: full_text (per search agent); cited as: C-DENIT [Bell2024]}
}

@article{bertagnolliNondenitrifierNitrousOxide2020,
  author = {Bertagnolli, AD and Konstantinidis, KT and Stewart, FJ},
  title = {Non-denitrifier nitrous oxide reductases dominate marine biomes},
  journal = {Environmental Microbiology Reports},
  year = {2020},
  volume = {12},
  number = {6},
  pages = {681-692},
  doi = {10.1111/1758-2229.12879},
  note = {access: abstract_only; cited as: C-DENIT [Bertagnolli2020]}
}

@article{bonillarossoDesignEvaluationPrimers2016,
  author = {Bonilla-Rosso, G and Wittorf, L and Jones, CM and Hallin, S},
  title = {Design and evaluation of primers targeting genes encoding NO-forming nitrite reductases: implications for ecological inference of denitrifying communities},
  journal = {Scientific Reports},
  year = {2016},
  volume = {6},
  pages = {39208},
  doi = {10.1038/srep39208},
  note = {access: abstract_only; cited as: C-DENIT [BonillaRosso2016]}
}

@article{brakerNitriteReductaseGenes2000,
  author = {Braker, G and Zhou, J and Wu, L and Devol, AH and Tiedje, JM},
  title = {Nitrite reductase genes (nirK and nirS) as functional markers to investigate diversity of denitrifying bacteria in Pacific Northwest marine sediment communities},
  journal = {Applied and Environmental Microbiology},
  year = {2000},
  volume = {66},
  number = {5},
  pages = {2096-2104},
  doi = {10.1128/AEM.66.5.2096-2104.2000},
  note = {access: abstract_only; cited as: C-DENIT [Braker2000]}
}

@article{brakerNitricOxideReductase2003,
  author = {Braker, G and Tiedje, JM},
  title = {Nitric oxide reductase (norB) genes from pure cultures and environmental samples},
  journal = {Applied and Environmental Microbiology},
  year = {2003},
  volume = {69},
  number = {6},
  pages = {3476-3483},
  doi = {10.1128/AEM.69.6.3476-3483.2003},
  note = {access: abstract_only; cited as: C-DENIT [BrakerTiedje2003]}
}

@article{brambillaAbsenceNitrousOxide2018,
  author = {Brambilla, S and Frare, R and Soto, G and Jozefkowicz, C and Ayub, N},
  title = {Absence of the nitrous oxide reductase gene cluster in commercial alfalfa inoculants is probably due to the extensive loss of genes during rhizobial domestication},
  journal = {Microbial Ecology},
  year = {2018},
  volume = {76},
  number = {2},
  pages = {299-302},
  doi = {10.1007/s00248-018-1145-9},
  note = {access: abstract_only; cited as: C-DENIT [Brambilla2018]}
}

@article{buenodemesquitaHighStrainlevelDiversity2025,
  author = {Bueno de Mesquita, Clifton P and Olm, Matthew R and Bissett, Andrew and Fierer, Noah},
  title = {High strain-level diversity of Bradyrhizobium across Australian soils},
  journal = {The ISME Journal},
  year = {2025},
  volume = {19},
  number = {1},
  pages = {wraf222},
  doi = {10.1093/ismejo/wraf222},
  note = {access: full_text (per agent); cited as: C-DENIT [BuenoDeMesquita2025]}
}

@article{changAlteromonasNitratireducensSp2025,
  author = {Chang, Ying-Li and Li, Jia-Xi and Wang, Xing-Chen and Li, Yang and Cao, Yun-Fei and Duan, Xiang-Wen and Sun, Cong and Chen, Can and Xu, Lin},
  title = {Alteromonas nitratireducens sp. nov., a novel nitrate-reducing bacterium isolated from marine sediments, and the evolution of nitrate-reducing genes in the genus Alteromonas},
  journal = {Microorganisms},
  year = {2025},
  volume = {13},
  number = {8},
  pages = {1888},
  doi = {10.3390/microorganisms13081888},
  note = {access: abstract_only; cited as: C-DENIT [Chang2025]}
}

@article{dandieAnalysisDenitrificationGenes2007,
  author = {Dandie, CE and Burton, DL and Zebarth, BJ and Trevors, JT and Goyer, C},
  title = {Analysis of denitrification genes and comparison of nosZ, cnorB and 16S rDNA from culturable denitrifying bacteria in potato cropping systems},
  journal = {Systematic and Applied Microbiology},
  year = {2007},
  volume = {30},
  number = {2},
  pages = {128-138},
  doi = {10.1016/j.syapm.2006.05.002},
  note = {access: abstract_only; cited as: C-DENIT [Dandie2007]}
}

@article{helenHighlyDiverseNirK2016,
  author = {Decleyre, H and Heylen, K and Tytgat, B and Willems, A},
  title = {Highly diverse nirK genes comprise two major clades that harbour ammonium-producing denitrifiers},
  journal = {BMC Genomics},
  year = {2016},
  volume = {17},
  pages = {155},
  doi = {10.1186/s12864-016-2465-0},
  note = {access: full_text (per search agent); cited as: C-DENIT [Decleyre2016]; Crossref name fields inverted}
}

@article{delormeComparativeGeneticDiversity2003,
  author = {Delorme, S and Philippot, L and Edel-Hermann, V and Deulvot, C and Mougel, C and Lemanceau, P},
  title = {Comparative genetic diversity of the narG, nosZ, and 16S rRNA genes in fluorescent pseudomonads},
  journal = {Applied and Environmental Microbiology},
  year = {2003},
  volume = {69},
  number = {2},
  pages = {1004-1012},
  doi = {10.1128/AEM.69.2.1004-1012.2003},
  note = {access: full_text (per one agent); conflict: the note's Sources not obtained also lists it (citation from memory; not verified; known only via citation in Intrator et al. 2024); cited as: C-DENIT [Delorme2003]}
}

@article{ghalyAgricultureAltersProtein2026,
  author = {Ghaly, Timothy M and Shah, Bhumika S and Coleman, Nicholas V and Elbourne, Liam DH and Le Roux, Johannes J and Gillings, Michael R and Paulsen, Ian T and Tetu, Sasha G},
  title = {Agriculture alters protein evolution of respiratory nitrate reductase in soil bacteria at a global scale},
  journal = {Environmental Research},
  year = {2026},
  volume = {300},
  pages = {124428},
  doi = {10.1016/j.envres.2026.124428},
  note = {access: abstract_only; cited as: C-DENIT [Ghaly2026]}
}

@article{gobernaPredictingMicrobialTraits2016,
  author = {Goberna, M and Verdú, M},
  title = {Predicting microbial traits with phylogenies},
  journal = {The ISME Journal},
  year = {2016},
  volume = {10},
  number = {4},
  pages = {959-967},
  doi = {10.1038/ismej.2015.171},
  note = {access: abstract_only (critic: C-DENIT:C-063..065; the note said full text via summarising tool); supplements not checked; cited as: C-DENIT [GobernaVerdu2016]}
}

@article{goffGenomicEnvironmentalControls2024,
  author = {Goff, Jennifer L and Szink, Elizabeth G and Durrence, Konnor L and Lui, Lauren M and Nielsen, Torben N and Kuehl, Jennifer V and Hunt, Kristopher A and Chandonia, John-Marc and Huang, Jiawen and Thorgersen, Michael P and Poole, Farris L and Stahl, David A and Chakraborty, Romy and Deutschbauer, Adam M and Arkin, Adam P and Adams, Michael W W},
  title = {Genomic and environmental controls on Castellaniella biogeography in an anthropogenically disturbed subsurface},
  journal = {Environmental Microbiome},
  year = {2024},
  volume = {19},
  pages = {26},
  doi = {10.1186/s40793-024-00570-9},
  note = {access: full_text (per agent); cited as: C-DENIT [Goff2024]}
}

@article{grafIntergenomicComparisonsHighlight2014,
  author = {Graf, DRH and Jones, CM and Hallin, S},
  title = {Intergenomic comparisons highlight modularity of the denitrification pathway and underpin the importance of community structure for N2O emissions},
  journal = {PLoS ONE},
  year = {2014},
  volume = {9},
  number = {12},
  pages = {e114118},
  doi = {10.1371/journal.pone.0114118},
  note = {access: full_text (checked by the synthesis); cited as: C-DENIT [Graf2014]}
}

@article{hallinGenomicsEcologyNovel2018,
  author = {Hallin, S and Philippot, L and Löffler, FE and Sanford, RA and Jones, CM},
  title = {Genomics and ecology of novel N2O-reducing microorganisms},
  journal = {Trends in Microbiology},
  year = {2018},
  volume = {26},
  number = {1},
  pages = {43-55},
  doi = {10.1016/j.tim.2017.07.003},
  note = {access: not_obtained (identified via Europe PMC author search; not fetched); not cited (background only; not cited for any finding); cited as: C-DENIT [Hallin2018]; background only; not cited for any finding}
}

@article{hexterDenitrificationModularityEnvironmental2026,
  author = {Hexter, J Catherine and Tang, Weiyi and Fortin, Samantha G and Jayakumar, Amal and Ward, Bess B},
  title = {Denitrification modularity and its environmental controls in transiently versus permanently anoxic marine systems},
  journal = {Environmental Microbiology},
  year = {2026},
  volume = {28},
  number = {8},
  pages = {e70407},
  doi = {10.1111/1462-2920.70407},
  note = {access: full_text (per agent); cited as: C-DENIT [Hexter2026]}
}

@article{heylenIncidenceNirSNirK2006,
  author = {Heylen, K and Gevers, D and Vanparys, B and Wittebolle, L and Geets, J and Boon, N and De Vos, P},
  title = {The incidence of nirS and nirK and their genetic heterogeneity in cultivated denitrifiers},
  journal = {Environmental Microbiology},
  year = {2006},
  volume = {8},
  number = {11},
  pages = {2012-2021},
  doi = {10.1111/j.1462-2920.2006.01081.x},
  note = {access: abstract_only; cited as: C-DENIT [Heylen2006]}
}

@article{heylenNitricOxideReductase2006,
  author = {Heylen, K and Vanparys, B and Gevers, D and Wittebolle, L and Boon, N and De Vos, P},
  title = {Nitric oxide reductase (norB) gene sequence analysis reveals discrepancies with nitrite reductase (nir) gene phylogeny in cultivated denitrifiers},
  journal = {Environmental Microbiology},
  year = {2007},
  volume = {9},
  number = {4},
  pages = {1072-1077},
  doi = {10.1111/j.1462-2920.2006.01194.x},
  note = {access: abstract_only; cited as: C-DENIT [Heylen2007]}
}

@article{higginsPhylogenomicsRevealDynamic2018,
  author = {Higgins, SA and Schadt, CW and Matheny, PB and Löffler, FE},
  title = {Phylogenomics reveal the dynamic evolution of fungal nitric oxide reductases and their relationship to secondary metabolism},
  journal = {Genome Biology and Evolution},
  year = {2018},
  volume = {10},
  number = {9},
  pages = {2474-2489},
  doi = {10.1093/gbe/evy187},
  note = {access: abstract_only; cited as: C-DENIT [Higgins2018]}
}

@article{hornNitrousOxideReductase2006,
  author = {Horn, MA and Drake, HL and Schramm, A},
  title = {Nitrous oxide reductase genes (nosZ) of denitrifying microbial populations in soil and the earthworm gut are phylogenetically similar},
  journal = {Applied and Environmental Microbiology},
  year = {2006},
  volume = {72},
  number = {2},
  pages = {1019-1026},
  doi = {10.1128/AEM.72.2.1019-1026.2006},
  note = {access: abstract_only; cited as: C-DENIT [Horn2006]}
}

@article{intratorAquaticNitrousOxide2024,
  author = {Intrator, N and Jayakumar, A and Ward, BB},
  title = {Aquatic nitrous oxide reductase gene (nosZ) phylogeny and environmental distribution},
  journal = {Frontiers in Microbiology},
  year = {2024},
  volume = {15},
  pages = {1407573},
  doi = {10.3389/fmicb.2024.1407573},
  note = {access: full_text (per agent, read at introduction level by one agent); cited as: C-DENIT [Intrator2024]}
}

@article{intratorAquaticCoppercontainingNitrite2025,
  author = {Intrator, Naomi and Ward, Bess B},
  title = {Aquatic copper-containing nitrite reductase gene (nirK) phylogeny and environmental distribution},
  journal = {Frontiers in Microbiology},
  year = {2025},
  volume = {16},
  pages = {1635656},
  doi = {10.3389/fmicb.2025.1635656},
  note = {access: full_text (per agent); cited as: C-DENIT [Intrator2025]}
}

@article{jangPotentiallyMobileDenitrification2019,
  author = {Jang, J and Sakai, Y and Senoo, K and Ishii, S},
  title = {Potentially mobile denitrification genes identified in Azospirillum sp. strain TSH58},
  journal = {Applied and Environmental Microbiology},
  year = {2019},
  volume = {85},
  number = {2},
  pages = {e02474-18},
  doi = {10.1128/AEM.02474-18},
  note = {access: full_text (per agent); cited as: C-DENIT [Jang2019]}
}

@article{jiaoComparativeGenomicAnalysis2022,
  author = {Jiao, J-Y and Lian, Z-H and Li, M-M and Salam, N and Zhou, E-M and Liu, L and Ming, H and Nie, G and Shu, W and Zhao, G and Hedlund, BP and Li, W-J},
  title = {Comparative genomic analysis of Thermus provides insights into the evolutionary history of an incomplete denitrification pathway},
  journal = {mLife},
  year = {2022},
  volume = {1},
  number = {2},
  pages = {198-209},
  doi = {10.1002/mlf2.12009},
  note = {access: abstract_only; cited as: C-DENIT [Jiao2022]}
}

@article{jonesPhylogeneticAnalysisNitrite2008,
  author = {Jones, Christopher M and Stres, Blaž and Rosenquist, Magnus and Hallin, Sara},
  title = {Phylogenetic analysis of nitrite, nitric oxide, and nitrous oxide respiratory enzymes reveal a complex evolutionary history for denitrification},
  journal = {Molecular Biology and Evolution},
  year = {2008},
  volume = {25},
  number = {9},
  pages = {1955-1966},
  doi = {10.1093/molbev/msn146},
  note = {access: abstract_only (the synthesis reached only the abstract; full text per one search agent); cited as: C-DENIT [Jones2008]}
}

@article{jonesEcologicalEvolutionaryFactors2010,
  author = {Jones, CM and Hallin, S},
  title = {Ecological and evolutionary factors underlying global and local assembly of denitrifier communities},
  journal = {The ISME Journal},
  year = {2010},
  volume = {4},
  number = {5},
  pages = {633-641},
  doi = {10.1038/ismej.2009.152},
  note = {access: abstract_only; cited as: C-DENIT [JonesHallin2010]}
}

@article{jonesPhenotypicGenotypicHeterogeneity2011,
  author = {Jones, CM and Welsh, A and Throbäck, IN and Dörsch, P and Bakken, LR and Hallin, S},
  title = {Phenotypic and genotypic heterogeneity among closely related soil-borne N2- and N2O-producing Bacillus isolates harboring the nosZ gene},
  journal = {FEMS Microbiology Ecology},
  year = {2011},
  volume = {76},
  number = {3},
  pages = {541-552},
  doi = {10.1111/j.1574-6941.2011.01071.x},
  note = {access: abstract_only; cited as: C-DENIT [Jones2011]}
}

@article{jonesUnaccountedYetAbundant2012,
  author = {Jones, CM and Graf, DRH and Bru, D and Philippot, L and Hallin, S},
  title = {The unaccounted yet abundant nitrous oxide-reducing microbial community: a potential nitrous oxide sink},
  journal = {The ISME Journal},
  year = {2013},
  volume = {7},
  number = {2},
  pages = {417-426},
  doi = {10.1038/ismej.2012.125},
  note = {access: full_text (per one agent), abstract_only (per another): conflicting labels; cited as: C-DENIT [Jones2013]}
}

@article{juhansonSpatialPhyloecologicalAnalyses2017,
  author = {Juhanson, J and Hallin, S and Söderström, M and Stenberg, M and Jones, CM},
  title = {Spatial and phyloecological analyses of nosZ genes underscore niche differentiation amongst terrestrial N2O reducing communities},
  journal = {Soil Biology and Biochemistry},
  year = {2017},
  volume = {115},
  pages = {82-91},
  doi = {10.1016/j.soilbio.2017.08.013},
  note = {access: abstract_only; cited as: C-DENIT [Juhanson2017]}
}

@article{kimEukaryoticINirK2009,
  author = {Kim, S-W and Fushinobu, S and Zhou, S and Wakagi, T and Shoun, H},
  title = {Eukaryotic nirK genes encoding copper-containing nitrite reductase: originating from the protomitochondrion?},
  journal = {Applied and Environmental Microbiology},
  year = {2009},
  volume = {75},
  number = {9},
  pages = {2652-2658},
  doi = {10.1128/AEM.02536-08},
  note = {access: abstract_only; cited as: C-DENIT [Kim2009]}
}

@article{liMetabolicNicheDifferentiation2027,
  author = {Li, Jiapeng and Zuo, Xiaotian and Qiu, Linqing and Meng, Fangang},
  title = {Metabolic niche differentiation and napA evolution stabilize partial denitrification in wastewater ecosystems},
  journal = {Water Research},
  year = {2026},
  volume = {308},
  pages = {126810},
  doi = {10.1016/j.watres.2026.126810},
  note = {access: abstract_only; cited as: C-DENIT [Li2026]; year: 2026 (issue dated January 2027 in Crossref; online 2026)}
}

@article{liuStrainsGenusI2013,
  author = {Liu, B and Mao, Y and Bergaust, L and Bakken, LR and Frostegård, Å},
  title = {Strains in the genus Thauera exhibit remarkably different denitrification regulatory phenotypes},
  journal = {Environmental Microbiology},
  year = {2013},
  volume = {15},
  number = {10},
  pages = {2816-2828},
  doi = {10.1111/1462-2920.12142},
  note = {access: abstract_only; cited as: C-DENIT [Liu2013]}
}

@article{lycusPhenotypicGenotypicRichness2017,
  author = {Lycus, P and Bøthun, KL and Bergaust, L and Shapleigh, JP and Bakken, LR and Frostegård, Å},
  title = {Phenotypic and genotypic richness of denitrifiers revealed by a novel isolation strategy},
  journal = {The ISME Journal},
  year = {2017},
  volume = {11},
  number = {10},
  pages = {2219-2232},
  doi = {10.1038/ismej.2017.82},
  note = {access: abstract_only (critic: C-DENIT:C-063..065; the note said read via a summarising tool; abstract quote verified); cited as: C-DENIT [Lycus2017]}
}

@article{martinyPhylogeneticConservatismFunctional2013,
  author = {Martiny, AC and Treseder, K and Pusch, G},
  title = {Phylogenetic conservatism of functional traits in microorganisms},
  journal = {The ISME Journal},
  year = {2013},
  volume = {7},
  number = {4},
  pages = {830-838},
  doi = {10.1038/ismej.2012.160},
  note = {access: abstract_only (critic: C-DENIT:C-063..065; the note said full text via summarising tool); supplements not checked; cited as: C-DENIT [Martiny2013]}
}

@article{mefferdIncompleteDenitrificationPhenotypes2022,
  author = {Mefferd, Chrisabelle C and Zhou, Enmin and Seymour, Cale O and Bernardo, Noel A and Srivastava, Shreya and Bengtson, Amanda J and Jiao, Jian-Yu and Dong, Hailiang and Li, Wen-Jun and Hedlund, Brian P},
  title = {Incomplete denitrification phenotypes in diverse Thermus species from diverse geothermal spring sediments and adjacent soils in southwest China},
  journal = {Extremophiles},
  year = {2022},
  volume = {26},
  number = {2},
  pages = {23},
  doi = {10.1007/s00792-022-01272-1},
  note = {access: full_text (per agent); cited as: C-DENIT [Mefferd2022]}
}

@article{menestreauDistinctDenitrificationPhenotypes2026,
  author = {Menestreau, Martin and Milligan, Daniel A and Sennett, Louise B and Bergaust, Linda and Bakken, Lars R and Rowley, Gary and Kjos, Morten and Shapleigh, James P and Frostegård, Åsa},
  title = {Distinct denitrification phenotypes in closely related bacteria: clues to understanding variations in nitrite accumulation among Stutzerimonas strains},
  journal = {Environmental Microbiology},
  year = {2026},
  volume = {28},
  number = {4},
  pages = {e70275},
  doi = {10.1111/1462-2920.70275},
  note = {access: full_text (per agent); cited as: C-DENIT [Menestreau2026]}
}

@article{mingInsightsEvolutionaryEcological2024,
  author = {Ming, Yuzhen and Abdullah Al, Mamun and Zhang, Dandan and Zhu, Wengen and Liu, Huanping and Cai, Lanlan and Yu, Xiaoli and Wu, Kun and Niu, Mingyang and Zeng, Qinglu and He, Zhili and Yan, Qingyun},
  title = {Insights into the evolutionary and ecological adaption strategies of nirS- and nirK-type denitrifying communities},
  journal = {Molecular Ecology},
  year = {2024},
  volume = {33},
  number = {18},
  pages = {e17507},
  doi = {10.1111/mec.17507},
  note = {access: abstract_only; cited as: C-DENIT [Ming2024]}
}

@article{mirallesrobledilloDistributionDenitrificationHaloarchaea2021,
  author = {Miralles-Robledillo, JM and Bernabeu, E and Giani, M and Martínez-Serna, E and Martínez-Espinosa, RM and Pire, C},
  title = {Distribution of denitrification among haloarchaea: a comprehensive study},
  journal = {Microorganisms},
  year = {2021},
  volume = {9},
  number = {8},
  pages = {1669},
  doi = {10.3390/microorganisms9081669},
  note = {access: full_text (per agent); cited as: C-DENIT [MirallesRobledillo2021]}
}

@article{muraliDiversityEvolutionNitric2024,
  author = {Murali, R and Pace, LA and Sanford, RA and Ward, LM and Lynes, MM and Hatzenpichler, R and Lingappa, UF and Fischer, WW and Gennis, RB and Hemp, J},
  title = {Diversity and evolution of nitric oxide reduction in bacteria and archaea},
  journal = {Proceedings of the National Academy of Sciences USA},
  year = {2024},
  volume = {121},
  number = {26},
  pages = {e2316422121},
  doi = {10.1073/pnas.2316422121},
  note = {access: full_text (per search agents; main text; Dataset S7 not read); cited as: C-DENIT [Murali2024]}
}

@article{nelsonGlobalBiogeographyMicrobial2016,
  author = {Nelson, MB and Martiny, AC and Martiny, JBH},
  title = {Global biogeography of microbial nitrogen-cycling traits in soil},
  journal = {Proceedings of the National Academy of Sciences USA},
  year = {2016},
  volume = {113},
  number = {29},
  pages = {8033-8040},
  doi = {10.1073/pnas.1601070113},
  note = {access: abstract_only (critic: C-DENIT:C-063..065; the note said read through a summarising tool; abstract quote verified); cited as: C-DENIT [Nelson2016]}
}

@article{palmerGenomeDerivedCriteriaAssigning2009,
  author = {Palmer, Katharina and Drake, Harold L and Horn, Marcus A},
  title = {Genome-derived criteria for assigning environmental narG and nosZ sequences to operational taxonomic units of nitrate reducers},
  journal = {Applied and Environmental Microbiology},
  year = {2009},
  volume = {75},
  number = {15},
  pages = {5170-5174},
  doi = {10.1128/AEM.00254-09},
  note = {access: full_text (per agent); cited as: C-DENIT [Palmer2009]}
}

@article{parsonsRadiationNitrogenmetabolizingEnzymes2020,
  author = {Parsons, Chris and Stüeken, Eva E and Rosen, Caleb J and Mateos, Katherine and Anderson, Rika E},
  title = {Radiation of nitrogen-metabolizing enzymes across the tree of life tracks environmental transitions in Earth history},
  journal = {Geobiology},
  year = {2021},
  volume = {19},
  number = {1},
  pages = {18-34},
  doi = {10.1111/gbi.12419},
  note = {access: full_text (checked by the synthesis); cited as: C-DENIT [Parsons2021]; year: 2021 (online 2020)}
}

@article{pessiIndepthCharacterizationDenitrifier2022,
  author = {Pessi, IS and Viitamäki, S and Virkkala, A-M and Eronen-Rasimus, E and Delmont, TO and Marushchak, ME and Luoto, M and Hultman, J},
  title = {In-depth characterization of denitrifier communities across different soil ecosystems in the tundra},
  journal = {Environmental Microbiome},
  year = {2022},
  volume = {17},
  pages = {30},
  doi = {10.1186/s40793-022-00424-2},
  note = {access: abstract_only; cited as: C-DENIT [Pessi2022]}
}

@article{poldPhylogeneticsEnvironmentalDistribution2024,
  author = {Pold, G and Bonilla-Rosso, G and Saghaï, A and Strous, M and Jones, CM and Hallin, S},
  title = {Phylogenetics and environmental distribution of nitric oxide-forming nitrite reductases reveal their distinct functional and ecological roles},
  journal = {ISME Communications},
  year = {2024},
  volume = {4},
  number = {1},
  pages = {ycae020},
  doi = {10.1093/ismeco/ycae020},
  note = {access: full_text (checked by the synthesis; supplements not read); cited as: C-DENIT [Pold2024]}
}

@article{poldDenitrificationCommunityTrait2025,
  author = {Pold, G and Saghaï, A and Jones, CM and Hallin, S},
  title = {Denitrification is a community trait with partial pathways dominating across microbial genomes and biomes},
  journal = {Nature Communications},
  year = {2025},
  volume = {16},
  pages = {9495},
  doi = {10.1038/s41467-025-65319-5},
  note = {access: full_text (checked by the synthesis); cited as: C-DENIT [Pold2025]}
}

@article{priemeDiversityNitriteReductase2002,
  author = {Priemé, A and Braker, G and Tiedje, JM},
  title = {Diversity of nitrite reductase (nirK and nirS) gene fragments in forested upland and wetland soils},
  journal = {Applied and Environmental Microbiology},
  year = {2002},
  volume = {68},
  number = {4},
  pages = {1893-1900},
  doi = {10.1128/AEM.68.4.1893-1900.2002},
  note = {access: abstract_only; cited as: C-DENIT [Prieme2002]}
}

@article{rocoModularityNitrogenoxideReducing2016,
  author = {Roco, CA and Bergaust, LL and Bakken, LR and Yavitt, JB and Shapleigh, JP},
  title = {Modularity of nitrogen-oxide reducing soil bacteria: linking phenotype to genotype},
  journal = {Environmental Microbiology},
  year = {2017},
  volume = {19},
  number = {6},
  pages = {2507-2519},
  doi = {10.1111/1462-2920.13250},
  note = {access: abstract_only; cited as: C-DENIT [Roco2017]; year: 2017 (online 2016)}
}

@article{saekiEffectFloodingLt2017,
  author = {Saeki, Y and Nakamura, M and Mason, MLT and Yano, T and Shiro, S and Sameshima-Saito, R and Itakura, M and Minamisawa, K and Yamamoto, A},
  title = {Effect of flooding and the nosZ gene in bradyrhizobia on bradyrhizobial community structure in the soil},
  journal = {Microbes and Environments},
  year = {2017},
  volume = {32},
  number = {2},
  pages = {154-163},
  doi = {10.1264/jsme2.ME16132},
  note = {access: abstract_only; cited as: C-DENIT [Saeki2017]}
}

@article{saghaiPhyloecologyNitrateAmmonifiers2023,
  author = {Saghaï, A and Pold, G and Jones, CM and Hallin, S},
  title = {Phyloecology of nitrate ammonifiers and their importance relative to denitrifiers in global terrestrial biomes},
  journal = {Nature Communications},
  year = {2023},
  volume = {14},
  pages = {8249},
  doi = {10.1038/s41467-023-44022-3},
  note = {access: full_text (per agent); conflict: the note's Sources not obtained also lists it (seen only as a citation in Pold et al. 2025; not fetched); cited as: C-DENIT [Saghai2023]}
}

@article{sameshimasaitoCorrelationDenitrifyingCapability2006,
  author = {Sameshima-Saito, R and Chiba, K and Minamisawa, K},
  title = {Correlation of denitrifying capability with the existence of nap, nir, nor and nos genes in diverse strains of soybean bradyrhizobia},
  journal = {Microbes and Environments},
  year = {2006},
  volume = {21},
  number = {3},
  pages = {174-184},
  doi = {10.1264/jsme2.21.174},
  note = {access: abstract_only; cited as: C-DENIT [SameshimaSaito2006]}
}

@article{sanfordUnexpectedNondenitrifierNitrous2012,
  author = {Sanford, RA and Wagner, DD and Wu, Q and Chee-Sanford, JC and Thomas, SH and Cruz-García, C and Rodríguez, G and Massol-Deyá, A and Krishnani, KK and Ritalahti, KM and Nissen, S and Konstantinidis, KT and Löffler, FE},
  title = {Unexpected nondenitrifier nitrous oxide reductase gene diversity and abundance in soils},
  journal = {Proceedings of the National Academy of Sciences USA},
  year = {2012},
  volume = {109},
  number = {48},
  pages = {19709-19714},
  doi = {10.1073/pnas.1211238109},
  note = {access: full_text (per one agent); cited as: C-DENIT [Sanford2012]}
}

@article{shiinaRelationshipSoilType2014,
  author = {Shiina, Yoko and Itakura, Manabu and Choi, Hyunseok and Saeki, Yuichi and Hayatsu, Masahito and Minamisawa, Kiwamu},
  title = {Relationship between soil type and N2O reductase genotype (nosZ) of indigenous soybean bradyrhizobia: nosZ-minus populations are dominant in Andosols},
  journal = {Microbes and Environments},
  year = {2014},
  volume = {29},
  number = {4},
  pages = {420-426},
  doi = {10.1264/jsme2.ME14130},
  note = {access: full_text (checked by the synthesis); secondary for the genomic-island statement (critic: C-DENIT:C-058); cited as: C-DENIT [Shiina2014]}
}

@article{stresNitrousOxideReductase2004,
  author = {Stres, B and Mahne, I and Avguštin, G and Tiedje, JM},
  title = {Nitrous oxide reductase (nosZ) gene fragments differ between native and cultivated Michigan soils},
  journal = {Applied and Environmental Microbiology},
  year = {2004},
  volume = {70},
  number = {1},
  pages = {301-309},
  doi = {10.1128/AEM.70.1.301-309.2004},
  note = {access: abstract_only; cited as: C-DENIT [Stres2004]}
}

@article{torregrosacrespoDenitrifyingHaloarchaeaGenus2018,
  author = {Torregrosa-Crespo, J and Pire, C and Martínez-Espinosa, RM and Bergaust, L},
  title = {Denitrifying haloarchaea within the genus Haloferax display divergent respiratory phenotypes, with implications for their release of nitrogenous gases},
  journal = {Environmental Microbiology},
  year = {2019},
  volume = {21},
  number = {1},
  pages = {427-436},
  doi = {10.1111/1462-2920.14474},
  note = {access: abstract_only; cited as: C-DENIT [TorregrosaCrespo2019]}
}

@article{truchonPlantPathogenicIRalstonia2023,
  author = {Truchon, Alicia N and Dalsing, Beth L and Khokhani, Devanshi and MacIntyre, April and McDonald, Bradon R and Ailloud, Florent and Klassen, Jonathan and Gonzalez-Orta, Enid T and Currie, Cameron and Prior, Philippe and Lowe-Power, Tiffany M and Allen, Caitilyn},
  title = {Plant-pathogenic Ralstonia phylotypes evolved divergent respiratory strategies and behaviors to thrive in xylem},
  journal = {mBio},
  year = {2023},
  volume = {14},
  number = {1},
  pages = {e03188-22},
  doi = {10.1128/mbio.03188-22},
  note = {access: full_text (checked by the synthesis); cited as: C-DENIT [Truchon2023]}
}

@article{verbaendertDenitrificationCommonFeature2011,
  author = {Verbaendert, I and Boon, N and De Vos, P and Heylen, K},
  title = {Denitrification is a common feature among members of the genus Bacillus},
  journal = {Systematic and Applied Microbiology},
  year = {2011},
  volume = {34},
  number = {5},
  pages = {385-391},
  doi = {10.1016/j.syapm.2011.02.003},
  note = {access: abstract_only; cited as: C-DENIT [Verbaendert2011]}
}

@article{wasaiharaDiversityLtI2020,
  author = {Wasai-Hara, S and Hara, S and Morikawa, T and Sugawara, M and Takami, H and Yoneda, J and Tokunaga, T and Minamisawa, K},
  title = {Diversity of Bradyrhizobium in non-leguminous sorghum plants: B. ottawaense isolates unique in genes for N2O reductase and lack of the type VI secretion system},
  journal = {Microbes and Environments},
  year = {2020},
  volume = {35},
  number = {1},
  pages = {ME19102},
  doi = {10.1264/jsme2.ME19102},
  note = {access: abstract_only; cited as: C-DENIT [WasaiHara2020]}
}

@article{wasaiharaBradyrhizobiumOttawaenseEfficiently2023,
  author = {Wasai-Hara, S and Itakura, M and Fernandes Siqueira, A and Takemoto, D and Sugawara, M and Mitsui, H and Sato, S and Inagaki, N and Yamazaki, T and Imaizumi-Anraku, H and Shimoda, Y and Minamisawa, K},
  title = {Bradyrhizobium ottawaense efficiently reduces nitrous oxide through high nosZ gene expression},
  journal = {Scientific Reports},
  year = {2023},
  volume = {13},
  pages = {18862},
  doi = {10.1038/s41598-023-46019-w},
  note = {access: abstract_only; cited as: C-DENIT [WasaiHara2023]}
}

@article{weiHigherDiversityAbundance2015,
  author = {Wei, W and Isobe, K and Nishizawa, T and Zhu, L and Shiratori, Y and Ohte, N and Koba, K and Otsuka, S and Senoo, K},
  title = {Higher diversity and abundance of denitrifying microorganisms in environments than considered previously},
  journal = {The ISME Journal},
  year = {2015},
  volume = {9},
  number = {9},
  pages = {1954-1965},
  doi = {10.1038/ismej.2015.9},
  note = {access: abstract_only; cited as: C-DENIT [Wei2015]}
}

@article{wittorfExpressionNirKNirS2018,
  author = {Wittorf, L and Jones, CM and Bonilla-Rosso, G and Hallin, S},
  title = {Expression of nirK and nirS genes in two strains of Pseudomonas stutzeri harbouring both types of NO-forming nitrite reductases},
  journal = {Research in Microbiology},
  year = {2018},
  volume = {169},
  number = {6},
  pages = {343-347},
  doi = {10.1016/j.resmic.2018.04.010},
  note = {access: abstract_only; cited as: C-DENIT [Wittorf2018]}
}

@article{wittorfHabitatDiversityType2020,
  author = {Wittorf, L and Roger, F and Alsterberg, C and Gamfeldt, L and Hulth, S and Sundbäck, K and Jones, CM and Hallin, S},
  title = {Habitat diversity and type govern potential nitrogen loss by denitrification in coastal sediments and differences in ecosystem-level diversities of disparate N2O reducing communities},
  journal = {FEMS Microbiology Ecology},
  year = {2020},
  volume = {96},
  number = {9},
  pages = {fiaa091},
  doi = {10.1093/femsec/fiaa091},
  note = {access: abstract_only; cited as: C-DENIT [Wittorf2020]}
}

@article{woehleNovelEukaryoticDenitrification2018,
  author = {Woehle, C and Roy, A-S and Glock, N and Wein, T and Weissenbach, J and Rosenstiel, P and Hiebenthal, C and Michels, J and Schönfeld, J and Dagan, T},
  title = {A novel eukaryotic denitrification pathway in foraminifera},
  journal = {Current Biology},
  year = {2018},
  volume = {28},
  number = {16},
  pages = {2536-2543.e5},
  doi = {10.1016/j.cub.2018.06.027},
  note = {access: abstract_only; cited as: C-DENIT [Woehle2018]}
}

@article{woehleDenitrificationForaminiferaHas2022,
  author = {Woehle, C and Roy, A-S and Glock, N and Michels, J and Wein, T and Weissenbach, J and Romero, D and Hiebenthal, C and Gorb, SN and Schönfeld, J and Dagan, T},
  title = {Denitrification in foraminifera has an ancient origin and is complemented by associated bacteria},
  journal = {Proceedings of the National Academy of Sciences USA},
  year = {2022},
  volume = {119},
  number = {25},
  pages = {e2200198119},
  doi = {10.1073/pnas.2200198119},
  note = {access: abstract_only; cited as: C-DENIT [Woehle2022]}
}

@article{zhangPartitioningDenitrificationPathway2023,
  author = {Zhang, IH and Sun, X and Jayakumar, A and Fortin, SG and Ward, BB and Babbin, AR},
  title = {Partitioning of the denitrification pathway and other nitrite metabolisms within global oxygen deficient zones},
  journal = {ISME Communications},
  year = {2023},
  volume = {3},
  number = {1},
  pages = {76},
  doi = {10.1038/s43705-023-00284-y},
  note = {access: full_text (per agent); cited as: C-DENIT [Zhang2023]}
}

@article{shanBeyondDenitrificationRole2021,
  author = {Shan, J and Sanford, RA and Chee-Sanford, J and Ooi, SK and Löffler, FE and Konstantinidis, KT and Yang, WH},
  title = {Beyond denitrification: the role of microbial diversity in controlling nitrous oxide reduction and soil nitrous oxide emissions},
  journal = {Global Change Biology},
  year = {2021},
  note = {access: not_obtained (recalled from memory; not searched, search budget spent on primary studies; DOI not verified); not cited; incomplete: volume, number, pages, doi; cited as: C-DENIT Sources not obtained}
}

@article{lalucatBiologyPseudomonasStutzeri2006,
  author = {Lalucat, J and Bennasar, A and Bosch, R and García-Valdés, E and Palleroni, NJ},
  title = {Biology of Pseudomonas stutzeri},
  journal = {Microbiology and Molecular Biology Reviews},
  year = {2006},
  volume = {70},
  pages = {510-547},
  note = {access: not_obtained (recalled; not searched; DOI not verified); not cited; incomplete: number, doi; cited as: C-DENIT Sources not obtained}
}

@misc{sanchezStudiesNosZPresence,
  author = {Sánchez, C and Minamisawa, K and others},
  title = {Studies of nosZ presence and absence across Bradyrhizobium japonicum / B. elkanii / B. diazoefficiens strains},
  note = {access: not_obtained (Europe PMC title search on Bradyrhizobium AND nosZ returned only related items; not fetched; not verified); not cited; incomplete: year, title (the note describes the works, it does not name one), journal, doi; the note names Siqueira et al. 2017 as an example, entered separately; cited as: C-DENIT Sources not obtained}
}

@article{siqueira2017,
  author = {Siqueira, A and others},
  journal = {Microbes and Environments},
  year = {2017},
  note = {access: not_obtained (named only as an example in the Sánchez and Minamisawa entry of Sources not obtained; not verified); not cited; incomplete: authors, title, volume, pages, doi; cited as: C-DENIT Sources not obtained}
}

@article{wittorf2016,
  author = {Wittorf, L and others},
  journal = {Environmental Microbiology Reports},
  year = {2016},
  volume = {8},
  pages = {486-492},
  note = {access: not_obtained (full text; Europe PMC abstract only); not cited; incomplete: authors, title, number, doi; cited as: C-DENIT Sources not obtained}
}

@article{philippotDenitrifyingGenesBacterial2002,
  author = {Philippot, L},
  title = {Denitrifying genes in bacterial and archaeal genomes},
  journal = {Biochimica et Biophysica Acta},
  year = {2002},
  volume = {1577},
  pages = {355-376},
  note = {access: not_obtained (seen only as a citation in Decleyre et al. 2016; not searched further); not cited; incomplete: number, doi; cited as: C-DENIT Sources not obtained}
}

@incollection{zumftNitrousOxideReductases2007,
  author = {Zumft, WG and Körner, H},
  title = {Nitrous oxide reductases},
  booktitle = {Biology of the Nitrogen Cycle},
  editor = {Bothe, H and Ferguson, SJ and Newton, WE},
  publisher = {Elsevier},
  year = {2007},
  note = {access: not_obtained (known only via citation in Intrator et al. 2024); cited secondarily via Intrator 2024; incomplete: pages, doi; cited as: C-DENIT Sources not obtained, and in the body as Zumft and Körner 2007}
}

@article{loucaDecouplingFunctionTaxonomy2016,
  author = {Louca, S and Parfrey, LW and Doebeli, M},
  title = {Decoupling function and taxonomy in the global ocean microbiome},
  journal = {Science},
  year = {2016},
  volume = {353},
  pages = {1272-1277},
  note = {access: not_obtained (citation from memory; not verified; Europe PMC title search returned unrelated items); not cited in the review body (named in a critic coverage gap); incomplete: number, doi; cited as: C-DENIT Sources not obtained}
}

@misc{roothans2025,
  author = {Roothans},
  year = {2025},
  note = {access: not stated; listed only in the provenance's Crossref check of 18 DOIs (Roothans 2025); not in the reference list and cited nowhere; incomplete: authors, title, journal, volume, pages, doi; cited as: C-DENIT Provenance}
}

@article{zumftCellBiologyMolecular1997,
  author = {Zumft, WG},
  title = {Cell biology and molecular basis of denitrification},
  journal = {Microbiology and Molecular Biology Reviews},
  year = {1997},
  volume = {61},
  number = {4},
  pages = {533-616},
  doi = {10.1128/mmbr.61.4.533-616.1997},
  note = {background; type: review; access: abstract checked (Europe PMC, PMID 9409151)}
}

@article{maddisonGeneTreesSpecies1997,
  author = {Maddison, Wayne P},
  title = {Gene trees in species trees},
  journal = {Systematic Biology},
  year = {1997},
  volume = {46},
  number = {3},
  pages = {523-536},
  doi = {10.1093/sysbio/46.3.523},
  note = {background; type: defining paper; access: abstract checked (publisher PDF)}
}

@article{blombergTestingPhylogeneticSignal2003,
  author = {Blomberg, Simon P and Garland, Theodore and Ives, Anthony R},
  title = {Testing for phylogenetic signal in comparative data: behavioral traits are more labile},
  journal = {Evolution},
  year = {2003},
  volume = {57},
  number = {4},
  pages = {717-745},
  doi = {10.1111/j.0014-3820.2003.tb00285.x},
  note = {background; type: defining paper; access: abstract checked (Europe PMC, PMID 12778543)}
}
```
