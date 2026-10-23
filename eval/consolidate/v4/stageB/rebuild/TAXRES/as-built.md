---
type: knowledge
title: Reference taxonomies and taxon-name resolution
inputs:
  - TAXRES: PhD/biblion/research/results/taxonomy-classification-and-name-resolution-result.md
refs: PhD/Proposal/Refs/Refs.bib
built: 2026-10-23
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
| TAXRES | [[taxonomy-classification-and-name-resolution-result]] | no | numbered | no | no | fallback (answers and critique; the note has no labelled citations) |

## Concepts

### prokaryote-taxonomies: Prokaryote reference taxonomies (GTDB, NCBI Taxonomy, LPSN)
needs: none
- **prokaryote-taxonomies.1** GTDB classifies by relative evolutionary divergence (RED) from genome similarity, rank-normalised; NCBI Taxonomy and LPSN follow the International Code of Nomenclature of Prokaryotes (ICNP).
  conf: not stated · class: not stated · holds: prokaryotes; a single-pass web-search scout · src: anonHarmonizingProkaryoticNomenclature2022, parksGTDBOngoingCensus2022 · rating: "not adversarially verified" · trail: TAXRES §The NCBI-vs-GTDB divergence · from: TAXRES:B-0008, TAXRES:B-0005
- **prokaryote-taxonomies.2** Because GTDB and NCBI Taxonomy/LPSN classify on different bases, the same organism can get a different lineage.
  conf: not stated · class: not stated · holds: prokaryotes; a single-pass web-search scout · src: anonHarmonizingProkaryoticNomenclature2022, parksGTDBOngoingCensus2022 · rating: "not adversarially verified" · trail: TAXRES §The NCBI-vs-GTDB divergence · from: TAXRES:B-0008, TAXRES:B-0009, TAXRES:B-0005

### phylum-renaming: Phylum renaming and the convergence of names
needs: prokaryote-taxonomies
- **phylum-renaming.1** The phylum renamings Firmicutes to Bacillota and Proteobacteria to Pseudomonadota were controversial.
  conf: not stated · class: not stated · holds: the renamings biblion's tags already use; a single-pass web-search scout · src: anonHarmonizingProkaryoticNomenclature2022 · rating: "not adversarially verified" · trail: TAXRES §The NCBI-vs-GTDB divergence · from: TAXRES:B-0010, TAXRES:B-0005
- **phylum-renaming.2** GTDB made the abrupt switch to the new phylum names in release R08-RS214 (2023).
  conf: not stated · class: not stated · holds: GTDB release R08-RS214; a single-pass web-search scout · src: anonHarmonizingProkaryoticNomenclature2022 · rating: "not adversarially verified" · trail: TAXRES §The NCBI-vs-GTDB divergence · from: TAXRES:B-0010, TAXRES:B-0005
- **phylum-renaming.3** NCBI and LPSN have since adopted the valid phylum names under nomenclatural requirements, not by coordination.
  conf: not stated · class: not stated · holds: NCBI and LPSN, after GTDB's switch; a single-pass web-search scout · src: anonHarmonizingProkaryoticNomenclature2022 · rating: "not adversarially verified" · trail: TAXRES §The NCBI-vs-GTDB divergence · from: TAXRES:B-0010, TAXRES:B-0005
- **phylum-renaming.4** Many microbiologists still use the older phylum names.
  conf: not stated · class: not stated · holds: a single-pass web-search scout · src: anonHarmonizingProkaryoticNomenclature2022 · rating: "not adversarially verified" · trail: TAXRES §The NCBI-vs-GTDB divergence · from: TAXRES:B-0010, TAXRES:B-0011, TAXRES:B-0005
- **phylum-renaming.5** The divergence between GTDB and NCBI Taxonomy/LPSN is active and partly converged: names are converging while the underlying classification basis still differs.
  conf: not stated · class: not stated · holds: prokaryote taxonomies; the provisional single-pass verdict · src: anonHarmonizingProkaryoticNomenclature2022 · rating: "not adversarially verified" · trail: TAXRES §The NCBI-vs-GTDB divergence, §Provisional verdicts · from: TAXRES:A-001, TAXRES:B-0012, TAXRES:B-0005

### gtdb-structure: GTDB structure and identifiers
needs: prokaryote-taxonomies
- **gtdb-structure.1** GTDB gives a complete, rank-normalised seven-rank classification (species to domain) for all genomes, sourced from NCBI Assembly.
  conf: not stated · class: not stated · holds: bacterial and archaeal genomes in GTDB; a single-pass web-search scout · src: parksGTDBRelease102026, parksGTDBOngoingCensus2022 · rating: "not adversarially verified" · trail: TAXRES §GTDB structure · from: TAXRES:B-0013, TAXRES:B-0015, TAXRES:B-0005
- **gtdb-structure.2** GTDB release R10-RS226 holds 715,230 bacterial and 17,245 archaeal genomes in 136,646 and 6,968 species clusters respectively.
  conf: not stated · class: not stated · holds: GTDB release R10-RS226; a single-pass web-search scout; the note says to treat every figure as a lead to confirm against the primary source · src: parksGTDBRelease102026, parksGTDBOngoingCensus2022 · rating: "not adversarially verified" · trail: TAXRES §GTDB structure · from: TAXRES:B-0014, TAXRES:B-0015, TAXRES:B-0005, TAXRES:B-0006
- **gtdb-structure.3** In GTDB a node at species rank is a genome cluster, not a named type strain alone.
  conf: not stated · class: not stated · holds: GTDB species clusters; a single-pass web-search scout · src: parksGTDBRelease102026, parksGTDBOngoingCensus2022 · rating: "not adversarially verified" · trail: TAXRES §GTDB structure · from: TAXRES:B-0014, TAXRES:B-0015, TAXRES:B-0005
- **gtdb-structure.4** GTDB is bulk-downloadable and explicitly tracks consistency against NCBI taxonomy.
  conf: not stated · class: not stated · holds: GTDB; a single-pass web-search scout · src: parksGTDBRelease102026, parksGTDBOngoingCensus2022 · rating: "not adversarially verified" · trail: TAXRES §GTDB structure · from: TAXRES:B-0013, TAXRES:B-0015, TAXRES:B-0005

### fungal-repositories: Fungal name repositories
needs: none
- **fungal-repositories.1** Fungi sit under Index Fungorum, MycoBank and Fungal Names, the three recognised fungal repositories; Index Fungorum holds 114,301 names.
  conf: not stated · class: not stated · holds: fungal names; a single-pass web-search scout; the note says to treat every figure as a lead to confirm against the primary source · src: gbifGBIFBackboneTaxonomy, anonSixQuestionsAnswered, silvaPytaxonPythonSoftware2025, anonTaxizeGnrResolve · rating: "not adversarially verified" · trail: TAXRES §The cross-kingdom backbone, §Provisional verdicts · from: TAXRES:A-001, TAXRES:B-0017, TAXRES:B-0018, TAXRES:B-0005, TAXRES:B-0006

### cross-kingdom-backbone: The cross-kingdom backbone (GBIF Backbone, Catalogue of Life)
needs: fungal-repositories
- **cross-kingdom-backbone.1** The GBIF Backbone Taxonomy is a single synthetic cross-kingdom classification (eight kingdoms; Linnaean ranks Kingdom to Species plus subspecies, variety and forma) built by starting from the Catalogue of Life and merging other authorities in priority order.
  conf: not stated · class: not stated · holds: the GBIF Backbone Taxonomy; a single-pass web-search scout · src: gbifGBIFBackboneTaxonomy, anonSixQuestionsAnswered, silvaPytaxonPythonSoftware2025, anonTaxizeGnrResolve · rating: "not adversarially verified" · trail: TAXRES §The cross-kingdom backbone · from: TAXRES:B-0016, TAXRES:B-0018, TAXRES:B-0005
- **cross-kingdom-backbone.2** The GBIF Backbone Taxonomy explicitly cross-walks names between sources.
  conf: not stated · class: not stated · holds: the GBIF Backbone Taxonomy; a single-pass web-search scout · src: gbifGBIFBackboneTaxonomy, anonSixQuestionsAnswered, silvaPytaxonPythonSoftware2025, anonTaxizeGnrResolve · rating: "not adversarially verified" · trail: TAXRES §The cross-kingdom backbone · from: TAXRES:B-0016, TAXRES:B-0018, TAXRES:B-0005
- **cross-kingdom-backbone.3** Fungi enter the GBIF Backbone Taxonomy via Index Fungorum.
  conf: not stated · class: not stated · holds: the GBIF Backbone Taxonomy; a single-pass web-search scout · src: gbifGBIFBackboneTaxonomy, anonSixQuestionsAnswered, silvaPytaxonPythonSoftware2025, anonTaxizeGnrResolve · rating: "not adversarially verified" · trail: TAXRES §The cross-kingdom backbone · from: TAXRES:B-0016, TAXRES:B-0017, TAXRES:B-0018, TAXRES:B-0005
- **cross-kingdom-backbone.4** The GBIF backbone build has been discontinued in favour of the eXtended Catalogue of Life (COL XR), which is now the cross-kingdom backbone to track.
  conf: not stated · class: not stated · holds: the GBIF backbone and the eXtended Catalogue of Life; a single-pass web-search scout · src: gbifGBIFBackboneTaxonomy, anonSixQuestionsAnswered, silvaPytaxonPythonSoftware2025, anonTaxizeGnrResolve · rating: "not adversarially verified" · trail: TAXRES §The cross-kingdom backbone · from: TAXRES:B-0018, TAXRES:B-0005
- **cross-kingdom-backbone.5** The nearest single cross-kingdom backbone is the Catalogue of Life (eXtended), which now drives the GBIF Backbone, but it is coarse.
  conf: not stated · class: not stated · holds: prokaryotes, fungi and plants; the provisional single-pass verdict · src: none (the verdict cites no source) · rating: "not adversarially verified" · trail: TAXRES §Provisional verdicts · from: TAXRES:A-001, TAXRES:B-0005

### single-authority: Whether one authoritative taxonomy covers prokaryotes, fungi and plants
needs: prokaryote-taxonomies, phylum-renaming, fungal-repositories, cross-kingdom-backbone
- **single-authority.1** No single authoritative taxonomy covers prokaryotes, fungi and plants: several must be integrated.
  conf: not stated · class: not stated · holds: prokaryotes, fungi and plants; the provisional single-pass verdict · src: none (the verdict cites no source) · rating: "not adversarially verified" · contrary: not stated · trail: TAXRES §Provisional verdicts · from: TAXRES:A-001, TAXRES:B-0005

### name-resolution: Taxon-name resolution tooling
needs: none
- **name-resolution.1** Documented tooling exists for resolving free-text taxon names, likely stronger than in the gene case: unlike microbial gene normalisation, taxonomic name resolution is a mature, dedicated tooling area (TNRS, GNverifier/Global Names, GBIF fuzzy matching, taxize, Taxamatch, Pytaxon) with a best-practices review.
  conf: not stated · class: not stated · holds: free-text taxon names; the provisional single-pass verdict · src: grenieHarmonizingTaxonNames2023, boyleTaxonomicNameResolution2013, silvaPytaxonPythonSoftware2025, anonTaxizeGnrResolve · rating: "not adversarially verified" · contrary: not stated · trail: TAXRES §Provisional verdicts, §Taxon-name resolution · from: TAXRES:A-002, TAXRES:B-0021, TAXRES:B-0005
- **name-resolution.2** Dedicated name-resolution tools exist with established methods: TNRS (plant names; parsing, fuzzy matching and authority correction; thousands of names per run), Taxamatch (a near/fuzzy matching algorithm), GNverifier/Global Names, taxize `gnr_resolve` (with a `with_context` option that restricts matching to a taxonomic context and avoids cross-group homonyms), GBIF fuzzy matching (`TAXON_MATCH_FUZZY`) and Pytaxon (Python, the GNV API plus fuzzy matching).
  conf: not stated · class: not stated · holds: the tools as documented; a single-pass web-search scout · src: grenieHarmonizingTaxonNames2023, boyleTaxonomicNameResolution2013, silvaPytaxonPythonSoftware2025, anonTaxizeGnrResolve · rating: "not adversarially verified" · trail: TAXRES §Taxon-name resolution · from: TAXRES:B-0019, TAXRES:B-0021, TAXRES:B-0005
- **name-resolution.3** Grenié et al. (2023) is a review of tools, databases and best practices for harmonising taxon names.
  conf: not stated · class: not stated · holds: harmonising taxon names in biodiversity data; a single-pass web-search scout · src: grenieHarmonizingTaxonNames2023 · rating: "not adversarially verified" · trail: TAXRES §Taxon-name resolution · from: TAXRES:B-0020, TAXRES:R-0008, TAXRES:B-0005
- **name-resolution.4** The grounding step has off-the-shelf, reviewed options.
  conf: not stated · class: not stated · holds: grounding free-text taxon names; a single-pass web-search scout · src: grenieHarmonizingTaxonNames2023, boyleTaxonomicNameResolution2013, silvaPytaxonPythonSoftware2025, anonTaxizeGnrResolve · rating: "not adversarially verified" · trail: TAXRES §Taxon-name resolution · from: TAXRES:B-0021, TAXRES:B-0005
- **name-resolution.5** The matching problem (synonyms, fuzzy matching of misspellings, homonyms via context) is largely handled.
  conf: not stated · class: not stated · holds: resolving free-text taxon names; the provisional single-pass verdict · src: none (the verdict cites no source) · rating: "not adversarially verified" · trail: TAXRES §Provisional verdicts · from: TAXRES:A-003, TAXRES:B-0005
- **name-resolution.6** The name-resolution tools are documented as effective, but specific precision/recall figures, including match rates for GNverifier, GBIF and TNRS on prokaryote and mixed-kingdom names, were not captured in this pass.
  conf: not stated · class: search (note: "specific precision/recall figures were not captured this pass") · holds: GNverifier, GBIF and TNRS on prokaryote and mixed-kingdom names; a single-pass web-search scout · src: none (an absence in the scout's searches) · search: not stated · trail: TAXRES §Provisional verdicts, §What still needs · from: TAXRES:A-004, TAXRES:B-0025

### authority-choice: The choice of authority
needs: name-resolution, single-authority
- **authority-choice.1** The unsolved part of taxon-name resolution is a curation choice (which authority's lineage to adopt), not a matching failure.
  conf: not stated · class: not stated · holds: resolving free-text taxon names; the provisional single-pass verdict · src: none (the verdict cites no source) · rating: "not adversarially verified" · trail: TAXRES §Provisional verdicts · from: TAXRES:A-003, TAXRES:B-0005
- **authority-choice.2** The taxonomy case inverts the gene case in one helpful way: name resolution is the easy part (mature tooling), and the hard part is the authority choice.
  conf: not stated · class: not stated · holds: the taxonomy case against the gene case; provisional and not committed · src: none (the reviewer's reading) · trail: TAXRES §What this means · from: TAXRES:B-0022

### informal-labels: Informal labels in the data
needs: name-resolution
- **informal-labels.1** Informal labels in the data (`AMF`, `Asgard`, `A21b`) almost certainly have no canonical taxon, confirming a review-queue residual as on the gene side.
  conf: not stated · class: not stated · holds: informal labels in the data; listed among what still needs confirming · src: none (no source cited) · trail: TAXRES §What still needs · from: TAXRES:B-0027

### design-hypothesis: A backbone arrangement to test
needs: authority-choice, gtdb-structure, phylum-renaming, cross-kingdom-backbone, fungal-repositories, name-resolution
- **design-hypothesis.1** A natural shape to test: pick GTDB as the prokaryote backbone (genome-based, and it matches the GTDB-style phylum tags already in the data), keep NCBI Taxonomy as the cross-domain taxid spine and fallback, route host plants and fungi through the Catalogue of Life/GBIF (with Index Fungorum/MycoBank for fungi), and ground free-text tags with GNverifier or GBIF matching.
  conf: not stated · class: reading (note: "This is a hypothesis for a future decision note, not a commitment") · holds: the data; provisional, not committed · src: none (the reviewer's hypothesis) · trail: TAXRES §What this means · from: TAXRES:B-0023, TAXRES:B-0024

## Do not say
- **dns.1** "These taxonomy findings are verified."
  why: The findings come from four direct web searches, not the deep-research harness, so they are not adversarially verified, and the note says to treat every figure as a lead to confirm against the primary source. · instead: gap.1 · trail: TAXRES §This is a single-pass scout · from: TAXRES:B-0005, TAXRES:B-0006, TAXRES:B-0007, TAXRES:B-0004
- **dns.2** "The project uses GTDB as its prokaryote backbone, NCBI Taxonomy as its taxid spine and the Catalogue of Life/GBIF for host plants and fungi."
  why: The note gives this arrangement as a hypothesis for a future decision note, not a commitment. · instead: design-hypothesis.1 · trail: TAXRES §What this means · from: TAXRES:B-0023, TAXRES:B-0024

## Gaps
- **gap.1** The scout's findings were never checked by a second reader or verified: its verdicts rest on the GTDB/NCBI divergence, the coarse Catalogue of Life backbone and the maturity of name-resolution tooling, and its figures (GTDB R10-RS226's 715,230 bacterial and 17,245 archaeal genomes in 136,646 and 6,968 species clusters; Index Fungorum's 114,301 names) are leads to confirm against the primary sources; harness verification of all of it on the same brief is still to be done.
  blocks: single-authority, name-resolution, gtdb-structure, fungal-repositories · origin: no critique; the note is a single-pass scout from four direct web searches, not adversarially verified · search: not stated · trail: TAXRES §This is a single-pass scout, §What still needs · from: TAXRES:A-001, TAXRES:A-002, TAXRES:B-0005, TAXRES:B-0006, TAXRES:B-0014, TAXRES:B-0017, TAXRES:B-0028
- **gap.2** Match-rate figures (precision and recall) for GNverifier, GBIF and TNRS on prokaryote and mixed-kingdom names.
  blocks: name-resolution, authority-choice · origin: listed by the note as still needing confirmation; specific precision/recall not captured · search: not stated · trail: TAXRES §What still needs · from: TAXRES:B-0025, TAXRES:A-004
- **gap.3** How complete the GTDB-to-NCBI identifier mapping is, and the exact lineage disagreements beyond phylum names.
  blocks: gtdb-structure, phylum-renaming · origin: listed by the note as still needing confirmation · search: not stated · trail: TAXRES §What still needs · from: TAXRES:B-0026
- **gap.4** Whether the informal labels in the data (`AMF`, `Asgard`, `A21b`) indeed have no canonical taxon.
  blocks: informal-labels · origin: listed by the note as still needing confirmation · search: not stated · trail: TAXRES §What still needs · from: TAXRES:B-0027

## Out of scope

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
  note = {access: not stated; cited as: TAXRES [1]; PMC9239268; listed under "References (single-pass, unverified)"; incomplete: author, pages}
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
  note = {access: not stated; cited as: TAXRES [2]; listed under "References (single-pass, unverified)"; incomplete: author, doi}
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
  note = {access: not stated; cited as: TAXRES [3]; PMC8728215; listed under "References (single-pass, unverified)"; incomplete: author}
}
@misc{gbifGBIFBackboneTaxonomy,
  author = {{GBIF Secretariat}},
  title = {GBIF Backbone Taxonomy},
  url = {https://www.gbif.org/dataset/d7dddbf4-2cf0-4f39-9b2a-bb099caae36c},
  note = {access: not stated; cited as: TAXRES [4] (first of two works); listed under "References (single-pass, unverified)"; incomplete: year}
}
@misc{anonSixQuestionsAnswered,
  title = {Six questions answered about the GBIF Backbone Taxonomy},
  howpublished = {GBIF Data Blog},
  url = {https://data-blog.gbif.org/post/gbif-backbone-taxonomy/},
  note = {access: not stated; cited as: TAXRES [4] (second of two works); listed under "References (single-pass, unverified)"; incomplete: author, year}
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
  note = {access: not stated; type: review (the note: "a review of tools, databases, and best practices"); cited as: TAXRES [5]; listed under "References (single-pass, unverified)"; incomplete: author}
}
@article{boyleTaxonomicNameResolution2013,
  author = {Boyle, B. and Hopkins, N. and Lu, Z. and others},
  title = {The taxonomic name resolution service: an online tool for automated standardization of plant names},
  journal = {BMC Bioinformatics},
  volume = {14},
  pages = {16},
  year = {2013},
  doi = {10.1186/1471-2105-14-16},
  note = {access: not stated; cited as: TAXRES [6]; PMC3554605; listed under "References (single-pass, unverified)"; incomplete: author}
}
@misc{silvaPytaxonPythonSoftware2025,
  author = {da Silva and others},
  title = {Pytaxon: a Python software for resolving and correcting taxonomic names in biodiversity data},
  year = {2025},
  note = {access: not stated; cited as: TAXRES [7] (first of two works); PMC11736304; listed under "References (single-pass, unverified)"; incomplete: author, journal, doi}
}
@misc{anonTaxizeGnrResolve,
  title = {taxize gnr_resolve (Global Names Resolver)},
  publisher = {rOpenSci},
  url = {https://rdrr.io/cran/taxize/man/gnr_resolve.html},
  note = {access: not stated; cited as: TAXRES [7] (second of two works); listed under "References (single-pass, unverified)"; incomplete: author, year}
}
```
