---
type: knowledge
title: Reference taxonomies and taxon-name resolution
inputs:
  - TAXRES: PhD/biblion/research/results/taxonomy-classification-and-name-resolution-result.md
refs: PhD/Proposal/Refs/Refs.bib
built: 2026-10-22
status: draft
tags:
  - research
  - knowledge
---

# Reference taxonomies and taxon-name resolution

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
| TAXRES | [[taxonomy-classification-and-name-resolution-result]] | no | numbered | no | no | not run |

## Concepts

### red: relative evolutionary divergence
needs: none
- **red.bg1** The GTDB bacterial taxonomy is built on a concatenated protein phylogeny and normalises taxonomic ranks on the basis of relative evolutionary divergence (RED).
  kind: background · ref: parksStandardizedBacterialTaxonomy2018 · check: DOI 10.1038/nbt.4229 resolves on Crossref; stated in the abstract ("normalizes taxonomic ranks on the basis of relative evolutionary divergence")

### icnp: the International Code of Nomenclature of Prokaryotes
needs: none
- **icnp.bg1** The International Code of Nomenclature of Prokaryotes (ICNP) is the code of nomenclature for prokaryotes; its edition includes lists of conserved and rejected names and rules on the Candidatus concept.
  kind: background · ref: parkerInternationalCodeNomenclature2019 · check: DOI 10.1099/ijsem.0.000778 resolves on Crossref (IJSEM 69(1A):S1–S111, the 2008 revision); stated in the abstract

### gtdb: the Genome Taxonomy Database
needs: red
- **gtdb.1** GTDB classifies by relative evolutionary divergence (RED) from genome similarity, rank-normalised.
  conf: not stated · class: not stated · holds: GTDB as found by a single-pass web search on 2026-06-19 · src: anonHarmonizingProkaryoticNomenclature2022, parksGTDBOngoingCensus2022 · trail: TAXRES §The NCBI-vs-GTDB divergence · from: TAXRES:B-0012, TAXRES:B-0001
- **gtdb.2** GTDB gives a complete, rank-normalised seven-rank classification (species to domain) for all genomes, sourced from NCBI Assembly.
  conf: not stated · class: not stated · holds: GTDB as found by a single-pass web search on 2026-06-19 · src: parksGTDBRelease102026, parksGTDBOngoingCensus2022 · trail: TAXRES §GTDB structure · from: TAXRES:B-0017, TAXRES:B-0001
- **gtdb.3** GTDB release R10-RS226 holds 715,230 bacterial and 17,245 archaeal genomes in 136,646 and 6,968 species clusters; a node at species rank is a genome cluster, not a named type strain alone.
  conf: not stated · class: not stated · holds: release R10-RS226 · src: parksGTDBRelease102026, parksGTDBOngoingCensus2022 · trail: TAXRES §GTDB structure · from: TAXRES:B-0018
- **gtdb.4** GTDB is bulk-downloadable and explicitly tracks consistency against NCBI taxonomy.
  conf: not stated · class: not stated · holds: GTDB as found by a single-pass web search on 2026-06-19 · src: parksGTDBRelease102026, parksGTDBOngoingCensus2022 · trail: TAXRES §GTDB structure · from: TAXRES:B-0019, TAXRES:B-0001

### ncbi-lpsn: NCBI Taxonomy and LPSN
needs: icnp
- **ncbi-lpsn.1** NCBI Taxonomy and LPSN follow the International Code of Nomenclature of Prokaryotes (ICNP).
  conf: not stated · class: not stated · holds: NCBI Taxonomy and LPSN as found by a single-pass web search on 2026-06-19 · src: anonHarmonizingProkaryoticNomenclature2022, parksGTDBOngoingCensus2022 · trail: TAXRES §The NCBI-vs-GTDB divergence · from: TAXRES:B-0012, TAXRES:B-0001

### gtdb-ncbi-divergence: the NCBI-versus-GTDB divergence
needs: gtdb, ncbi-lpsn
- **gtdb-ncbi-divergence.1** GTDB and NCBI Taxonomy / LPSN classify on different bases, so the same organism can get a different lineage.
  conf: not stated · class: not stated · holds: prokaryotes · src: anonHarmonizingProkaryoticNomenclature2022, parksGTDBOngoingCensus2022 · trail: TAXRES §The NCBI-vs-GTDB divergence · from: TAXRES:B-0013, TAXRES:B-0012
- **gtdb-ncbi-divergence.2** The phylum renamings Firmicutes to Bacillota and Proteobacteria to Pseudomonadota were controversial.
  conf: not stated · class: not stated · holds: the phylum renamings biblion's tags already use · src: anonHarmonizingProkaryoticNomenclature2022 · trail: TAXRES §The NCBI-vs-GTDB divergence · from: TAXRES:B-0014
- **gtdb-ncbi-divergence.3** GTDB made the abrupt switch to the new phylum names in R08-RS214 (2023).
  conf: not stated · class: not stated · holds: GTDB release R08-RS214 · src: anonHarmonizingProkaryoticNomenclature2022 · trail: TAXRES §The NCBI-vs-GTDB divergence · from: TAXRES:B-0014
- **gtdb-ncbi-divergence.4** NCBI and LPSN have since adopted the valid phylum names, under nomenclatural requirements and not by coordination.
  conf: not stated · class: not stated · holds: the phylum names Bacillota and Pseudomonadota · src: anonHarmonizingProkaryoticNomenclature2022 · trail: TAXRES §The NCBI-vs-GTDB divergence · from: TAXRES:B-0014
- **gtdb-ncbi-divergence.5** Many microbiologists still use the older phylum names.
  conf: not stated · class: not stated · holds: the older names Firmicutes and Proteobacteria · src: anonHarmonizingProkaryoticNomenclature2022 · trail: TAXRES §The NCBI-vs-GTDB divergence · from: TAXRES:B-0015, TAXRES:B-0014
- **gtdb-ncbi-divergence.6** Names are converging while the underlying classification basis still differs: the divergence is active and partly converged.
  conf: not stated · class: reading (note: "So names are converging while the underlying classification basis still differs") · holds: phylum names, GTDB against NCBI Taxonomy / LPSN · src: anonHarmonizingProkaryoticNomenclature2022 · trail: TAXRES §The NCBI-vs-GTDB divergence, §Provisional verdicts · from: TAXRES:B-0016, TAXRES:B-0008

### fungal-repositories: fungal name repositories
needs: none
- **fungal-repositories.1** Index Fungorum, MycoBank and Fungal Names are the three recognised fungal repositories; fungi sit under them.
  conf: not stated · class: not stated · holds: fungi, as found by a single-pass web search on 2026-06-19 · src: gbifGBIFBackboneTaxonomy, gbifSixQuestionsAnswered, silvaPytaxonPythonSoftware2025, ropensciGnrResolveGlobal · trail: TAXRES §The cross-kingdom backbone, §Provisional verdicts · from: TAXRES:B-0021, TAXRES:B-0008, TAXRES:B-0001
- **fungal-repositories.2** Index Fungorum holds 114,301 names.
  conf: not stated · class: not stated · holds: Index Fungorum as it enters the GBIF backbone · src: gbifGBIFBackboneTaxonomy, gbifSixQuestionsAnswered, silvaPytaxonPythonSoftware2025, ropensciGnrResolveGlobal · trail: TAXRES §The cross-kingdom backbone · from: TAXRES:B-0021

### cross-kingdom-backbone: the cross-kingdom backbone (GBIF Backbone and Catalogue of Life)
needs: fungal-repositories
- **cross-kingdom-backbone.1** The GBIF Backbone Taxonomy is a single synthetic cross-kingdom classification (eight kingdoms; Linnaean ranks Kingdom to Species plus subspecies, variety and forma), built by starting from the Catalogue of Life and merging other authorities in priority order.
  conf: not stated · class: not stated · holds: the GBIF Backbone Taxonomy as found by a single-pass web search on 2026-06-19 · src: gbifGBIFBackboneTaxonomy, gbifSixQuestionsAnswered, silvaPytaxonPythonSoftware2025, ropensciGnrResolveGlobal · trail: TAXRES §The cross-kingdom backbone · from: TAXRES:B-0020, TAXRES:B-0001
- **cross-kingdom-backbone.2** The GBIF Backbone Taxonomy explicitly cross-walks names between sources.
  conf: not stated · class: not stated · holds: the GBIF Backbone Taxonomy as found by a single-pass web search on 2026-06-19 · src: gbifGBIFBackboneTaxonomy, gbifSixQuestionsAnswered, silvaPytaxonPythonSoftware2025, ropensciGnrResolveGlobal · trail: TAXRES §The cross-kingdom backbone · from: TAXRES:B-0020, TAXRES:B-0001
- **cross-kingdom-backbone.3** Fungi enter the GBIF backbone via Index Fungorum.
  conf: not stated · class: not stated · holds: the GBIF Backbone Taxonomy · src: gbifGBIFBackboneTaxonomy, gbifSixQuestionsAnswered, silvaPytaxonPythonSoftware2025, ropensciGnrResolveGlobal · trail: TAXRES §The cross-kingdom backbone · from: TAXRES:B-0021
- **cross-kingdom-backbone.4** The GBIF backbone build has been discontinued in favour of the eXtended Catalogue of Life (COL XR), which is now the cross-kingdom backbone to track.
  conf: not stated · class: not stated · holds: as found by a single-pass web search on 2026-06-19 · src: gbifGBIFBackboneTaxonomy, gbifSixQuestionsAnswered, silvaPytaxonPythonSoftware2025, ropensciGnrResolveGlobal · trail: TAXRES §The cross-kingdom backbone · from: TAXRES:B-0022, TAXRES:B-0001
- **cross-kingdom-backbone.5** The nearest single cross-kingdom backbone is the Catalogue of Life (eXtended), which now drives the GBIF Backbone, but it is coarse.
  conf: not stated · class: not stated · holds: prokaryotes, fungi and plants; the note does not say in what way it is coarse · src: none (the verdict cites nothing) · trail: TAXRES §Provisional verdicts · from: TAXRES:B-0008

### taxonomy-integration: whether one authoritative taxonomy covers prokaryotes, fungi and plants
needs: gtdb-ncbi-divergence, fungal-repositories, cross-kingdom-backbone
- **taxonomy-integration.1** No single authoritative taxonomy covers prokaryotes, fungi and plants; several must be integrated: prokaryotes split between GTDB and NCBI Taxonomy / LPSN, fungi sit under Index Fungorum / MycoBank / Fungal Names, and the nearest single cross-kingdom backbone is coarse.
  conf: not stated · class: not stated · holds: the review's provisional, single-pass verdict on prokaryotes, fungi and plants · src: none (the verdict cites nothing) · trail: TAXRES §Provisional verdicts · from: TAXRES:B-0008

### name-resolution: resolving free-text taxon names
needs: gtdb-ncbi-divergence
- **name-resolution.1** Unlike microbial gene normalisation, taxonomic name resolution is a mature, dedicated tooling area (TNRS, GNverifier / Global Names, GBIF fuzzy matching, taxize, Taxamatch, Pytaxon) with a best-practices review: documented tooling exists, likely stronger than in the gene case.
  conf: not stated · class: not stated · holds: the review's provisional, single-pass verdict; the gene case is a separate research result · src: none (the verdict cites nothing; the tools are cited under the findings) · trail: TAXRES §Provisional verdicts · from: TAXRES:B-0009
- **name-resolution.2** Dedicated tools exist with established methods: TNRS (plant names; parsing, fuzzy matching and authority correction; thousands of names per run), Taxamatch (a near / fuzzy matching algorithm), GNverifier / Global Names, taxize `gnr_resolve` (with a `with_context` option to restrict to a taxonomic context and avoid cross-group homonyms), GBIF fuzzy matching (`TAXON_MATCH_FUZZY`), and Pytaxon (Python, GNV API and fuzzy matching).
  conf: not stated · class: not stated · holds: tools as found by a single-pass web search on 2026-06-19; no match-rate figures captured · src: grenieHarmonizingTaxonNames2023, boyleTaxonomicNameResolution2013, silvaPytaxonPythonSoftware2025, ropensciGnrResolveGlobal · trail: TAXRES §Taxon-name resolution · from: TAXRES:B-0023, TAXRES:B-0001
- **name-resolution.3** Grenié et al. (2023) is a review of tools, databases and best practices for harmonising taxon names.
  conf: not stated · class: not stated · holds: the note gives no setting · src: grenieHarmonizingTaxonNames2023 · trail: TAXRES §Taxon-name resolution · from: TAXRES:B-0024
- **name-resolution.4** The grounding step for free-text taxon names has off-the-shelf, reviewed options.
  conf: not stated · class: reading (note: "So the grounding step has off-the-shelf, reviewed options") · holds: the review's reading of the tools it found · src: grenieHarmonizingTaxonNames2023, boyleTaxonomicNameResolution2013, silvaPytaxonPythonSoftware2025, ropensciGnrResolveGlobal · trail: TAXRES §Taxon-name resolution · from: TAXRES:B-0025
- **name-resolution.5** The matching problem (synonyms, fuzzy matching of misspellings, homonyms via context) is largely handled; the unsolved part is a curation choice, which authority's lineage to adopt, not a matching failure: name resolution is the easy part and the authority choice the hard part.
  conf: not stated · class: not stated · holds: the review's provisional, single-pass verdict · src: none (the reviewer's synthesis) · trail: TAXRES §Provisional verdicts, §What this means · from: TAXRES:B-0010, TAXRES:B-0026
- **name-resolution.6** Specific precision / recall (match-rate) figures for the tools were not captured; the tools are documented effective.
  conf: not stated · class: search (note: "specific precision/recall figures were not captured this pass") · holds: four direct web searches on 2026-06-19 · src: none (a search result) · trail: TAXRES §Provisional verdicts, §What still needs confirming · from: TAXRES:B-0011, TAXRES:B-0029, TAXRES:B-0001

### informal-labels: informal labels with no canonical taxon
needs: name-resolution
- **informal-labels.1** Informal labels in the data (`AMF`, `Asgard`, `A21b`) almost certainly have no canonical taxon, confirming a review-queue residual as on the gene side.
  conf: not stated · class: not stated · holds: biblion's data; listed by the note among what still needs confirming · src: none (the note cites nothing for it) · trail: TAXRES §What still needs confirming · from: TAXRES:B-0031

## Do not say

- **dns.1** These findings as adversarially verified, or as carrying a 3-vote confidence.
  why: the note says they come from four direct web searches, "not adversarially verified and carry no 3-vote confidence", and that every figure is a lead to confirm against the primary source · instead: none · trail: TAXRES §This is a single-pass scout · from: TAXRES:B-0005, TAXRES:B-0006, TAXRES:B-0007

## Gaps

- **gap.1** Never checked by a second reader: the note has no critique, and every figure its verdicts rest on is unverified (GTDB R10-RS226: 715,230 bacterial and 17,245 archaeal genomes in 136,646 and 6,968 species clusters; Index Fungorum: 114,301 names; the GBIF backbone's eight kingdoms; GTDB's switch in R08-RS214, 2023). The note itself calls for harness verification of all of it on the same brief.
  blocks: gtdb, gtdb-ncbi-divergence, fungal-repositories, cross-kingdom-backbone, taxonomy-integration, name-resolution · origin: no critique; the note's single-pass warning; a follow-up the note calls for · from: TAXRES:B-0005, TAXRES:B-0006, TAXRES:B-0018, TAXRES:B-0021, TAXRES:B-0032
- **gap.2** Match-rate (precision / recall) figures for GNverifier, GBIF and TNRS on prokaryote and mixed-kingdom names.
  blocks: name-resolution · origin: not captured this pass · from: TAXRES:B-0011, TAXRES:B-0029
- **gap.3** The completeness of the GTDB-to-NCBI identifier mapping, and the exact lineage disagreements beyond phylum names.
  blocks: gtdb-ncbi-divergence · origin: what still needs confirming · from: TAXRES:B-0030
- **gap.4** Whether the informal labels in the data (`AMF`, `Asgard`, `A21b`) have any canonical taxon.
  blocks: informal-labels · origin: what still needs confirming · from: TAXRES:B-0031
- **gap.5** A plant reference taxonomy: the note's role names the plant reference taxonomies among its contents, but its findings name none beyond TNRS (plant names) and the cross-kingdom backbone.
  blocks: taxonomy-integration · origin: a concept with no claim behind it · from: TAXRES:B-0002, TAXRES:B-0008, TAXRES:B-0023

## Out of scope

- TAXRES:B-0027, TAXRES:B-0028: a design hypothesis for a future decision note (routing, not a finding)

## Sources

```bibtex
@article{anonHarmonizingProkaryoticNomenclature2022,
  title = {Harmonizing Prokaryotic Nomenclature: Fixing the Fuss over Phylum Name Flipping},
  journal = {mBio},
  volume = {13},
  number = {3},
  year = {2022},
  doi = {10.1128/mbio.00970-22},
  url = {https://journals.asm.org/doi/10.1128/mbio.00970-22},
  note = {access: not stated; cited as: TAXRES [1]; PMC9239268; the note's list is headed "single-pass, unverified"; incomplete: author, pages}
}

@article{parksGTDBRelease102026,
  author = {Parks, D. H. and others},
  title = {GTDB release 10: a complete and systematic taxonomy},
  journal = {Nucleic Acids Research},
  volume = {54},
  number = {D1},
  pages = {D743},
  year = {2026},
  url = {https://academic.oup.com/nar/article/54/D1/D743/8296754},
  note = {access: not stated; cited as: TAXRES [2]; the note's list is headed "single-pass, unverified"; incomplete: author, doi}
}

@article{parksGTDBOngoingCensus2022,
  author = {Parks, D. H. and Chuvochina, M. and Rinke, C. and others},
  title = {GTDB: an ongoing census of bacterial and archaeal diversity through a phylogenetically consistent, rank normalized and complete genome-based taxonomy},
  journal = {Nucleic Acids Research},
  volume = {50},
  number = {D1},
  pages = {D785},
  year = {2022},
  doi = {10.1093/nar/gkab776},
  note = {access: not stated; cited as: TAXRES [3]; PMC8728215; the note's list is headed "single-pass, unverified"; incomplete: author}
}

@misc{gbifGBIFBackboneTaxonomy,
  author = {{GBIF Secretariat}},
  title = {GBIF Backbone Taxonomy},
  url = {https://www.gbif.org/dataset/d7dddbf4-2cf0-4f39-9b2a-bb099caae36c},
  note = {access: not stated; cited as: TAXRES [4] (first of two works); the note's list is headed "single-pass, unverified"; incomplete: year}
}

@misc{gbifSixQuestionsAnswered,
  author = {{GBIF Secretariat}},
  title = {Six questions answered about the GBIF Backbone Taxonomy},
  howpublished = {GBIF Data Blog},
  url = {https://data-blog.gbif.org/post/gbif-backbone-taxonomy/},
  note = {access: not stated; cited as: TAXRES [4] (second of two works; the note gives no author of its own); the note's list is headed "single-pass, unverified"; incomplete: author, year}
}

@article{grenieHarmonizingTaxonNames2023,
  author = {Grenié, M. and Berti, E. and Carvajal-Quintero, J. and others},
  title = {Harmonizing taxon names in biodiversity data: a review of tools, databases and best practices},
  journal = {Methods in Ecology and Evolution},
  volume = {14},
  number = {1},
  pages = {12},
  year = {2023},
  doi = {10.1111/2041-210X.13802},
  note = {access: not stated; cited as: TAXRES [5]; the note's list is headed "single-pass, unverified"; incomplete: author}
}

@article{boyleTaxonomicNameResolution2013,
  author = {Boyle, B. and Hopkins, N. and Lu, Z. and others},
  title = {The taxonomic name resolution service: an online tool for automated standardization of plant names},
  journal = {BMC Bioinformatics},
  volume = {14},
  pages = {16},
  year = {2013},
  doi = {10.1186/1471-2105-14-16},
  note = {access: not stated; cited as: TAXRES [6]; PMC3554605; the note's list is headed "single-pass, unverified"; incomplete: author}
}

@article{silvaPytaxonPythonSoftware2025,
  author = {da Silva and others},
  title = {Pytaxon: a Python software for resolving and correcting taxonomic names in biodiversity data},
  year = {2025},
  note = {access: not stated; cited as: TAXRES [7] (first of two works); PMC11736304; the note's list is headed "single-pass, unverified"; incomplete: author, journal, volume, pages, doi}
}

@misc{ropensciGnrResolveGlobal,
  author = {{rOpenSci}},
  title = {gnr_resolve (Global Names Resolver), in taxize},
  url = {https://rdrr.io/cran/taxize/man/gnr_resolve.html},
  note = {access: not stated; cited as: TAXRES [7] (second of two works); the note's list is headed "single-pass, unverified"; incomplete: year}
}

@article{parksStandardizedBacterialTaxonomy2018,
  author = {Parks, Donovan H. and Chuvochina, Maria and Waite, David W. and Rinke, Christian and Skarshewski, Adam and Chaumeil, Pierre-Alain and Hugenholtz, Philip},
  title = {A standardized bacterial taxonomy based on genome phylogeny substantially revises the tree of life},
  journal = {Nature Biotechnology},
  volume = {36},
  number = {10},
  pages = {996--1004},
  year = {2018},
  doi = {10.1038/nbt.4229},
  note = {background}
}

@article{parkerInternationalCodeNomenclature2019,
  author = {Parker, C. and Tindall, B. and Garrity, G.},
  title = {International Code of Nomenclature of Prokaryotes: Prokaryotic Code (2008 Revision)},
  journal = {International Journal of Systematic and Evolutionary Microbiology},
  volume = {69},
  number = {1A},
  pages = {S1--S111},
  year = {2019},
  doi = {10.1099/ijsem.0.000778},
  note = {background}
}
```
