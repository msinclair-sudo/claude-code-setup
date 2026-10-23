# Reference taxonomies and taxon-name resolution: writer's view

> [!abstract] About this view
> What the research found, for writing from. Each claim gives who found it, the setting it holds for, the kind of evidence, its standing where the research stated one, and for an absence whether it was searched for. A claim with no standing given has none stated in the research; "limited by access" means a source was not read in full, which is not the same as weak evidence. Sources are listed at the end. The view is generated from the knowledge note `Reference taxonomies and taxon-name resolution.md`, where every claim is checked against the research.

## What the research found, by question

### TAXRES

**D1. Across microbiology, mycology, and botany, what reference taxonomies organise organisms into ranked hierarchies, how are they structured, how stable are their identifiers and names across releases, where do they conflict (in particular the divergence between phylogenomic, sequence-based prokaryote taxonomy and traditional nomenclatural-code-based naming, including renamed phyla), and what documented, accuracy-reported methods resolve free-text taxon names with their synonyms, authorships, rank heterogeneity, typographic variants, and informal or vernacular names to canonical identifiers?**

*No answer to this question in the research.*

*Answer, as the research gave it; not checked by a second reader.* **(a) Single authoritative taxonomy across prokaryotes, fungi, plants? — MUST INTEGRATE SEVERAL**

Prokaryotes split between **GTDB** (genome-based, RED-normalised) and **NCBI Taxonomy / LPSN** (nomenclatural code), with an active and partly-converged divergence; fungi sit under Index Fungorum / MycoBank / Fungal Names; the nearest single cross-kingdom backbone is the **Catalogue of Life (eXtended)** that now drives the GBIF Backbone, but it is coarse.

*Answer, as the research gave it; not checked by a second reader.* **(b) Evaluated standard for resolving free-text taxon names? — DOCUMENTED TOOLING EXISTS (likely stronger than the gene case)**

Unlike microbial gene normalisation, taxonomic name resolution is a **mature, dedicated tooling area** (TNRS, GNverifier/Global Names, GBIF fuzzy matching, `taxize`, Taxamatch, Pytaxon) with a best-practices review. The *matching* problem (synonyms, fuzzy/misspelling, homonyms via context) is largely handled; the unsolved part is a **curation choice** (which authority's lineage to adopt), not a matching failure. *Caveat:* specific precision/recall figures were not captured this pass.

## Concepts

In an order where each concept comes after the ones it builds on; the order means nothing more.

### Prokaryote reference taxonomies (GTDB, NCBI Taxonomy, LPSN)

- GTDB classifies by relative evolutionary divergence (RED) from genome similarity, rank-normalised; NCBI Taxonomy and LPSN follow the International Code of Nomenclature of Prokaryotes (ICNP). (Harmonizing Prokaryotic Nomenclature: Fi 2022; Parks et al. 2022)
  Holds for: prokaryotes; a single-pass web-search scout.
  Evidence: rated "not adversarially verified" by the research.
- Because GTDB and NCBI Taxonomy/LPSN classify on different bases, the same organism can get a different lineage. (Harmonizing Prokaryotic Nomenclature: Fi 2022; Parks et al. 2022)
  Holds for: prokaryotes; a single-pass web-search scout.
  Evidence: rated "not adversarially verified" by the research.

### Phylum renaming and the convergence of names

Builds on: Prokaryote reference taxonomies (GTDB, NCBI Taxonomy, LPSN).

- The phylum renamings Firmicutes to Bacillota and Proteobacteria to Pseudomonadota were controversial. (Harmonizing Prokaryotic Nomenclature: Fi 2022)
  Holds for: the renamings biblion's tags already use; a single-pass web-search scout.
  Evidence: rated "not adversarially verified" by the research.
- GTDB made the abrupt switch to the new phylum names in release R08-RS214 (2023). (Harmonizing Prokaryotic Nomenclature: Fi 2022)
  Holds for: GTDB release R08-RS214; a single-pass web-search scout.
  Evidence: rated "not adversarially verified" by the research.
- NCBI and LPSN have since adopted the valid phylum names under nomenclatural requirements, not by coordination. (Harmonizing Prokaryotic Nomenclature: Fi 2022)
  Holds for: NCBI and LPSN, after GTDB's switch; a single-pass web-search scout.
  Evidence: rated "not adversarially verified" by the research.
- Many microbiologists still use the older phylum names. (Harmonizing Prokaryotic Nomenclature: Fi 2022)
  Holds for: a single-pass web-search scout.
  Evidence: rated "not adversarially verified" by the research.
- The divergence between GTDB and NCBI Taxonomy/LPSN is active and partly converged: names are converging while the underlying classification basis still differs. (Harmonizing Prokaryotic Nomenclature: Fi 2022)
  Holds for: prokaryote taxonomies; the provisional single-pass verdict.
  Evidence: rated "not adversarially verified" by the research.

### GTDB structure and identifiers

Builds on: Prokaryote reference taxonomies (GTDB, NCBI Taxonomy, LPSN).

- GTDB gives a complete, rank-normalised seven-rank classification (species to domain) for all genomes, sourced from NCBI Assembly. (Parks and others 2026; Parks et al. 2022)
  Holds for: bacterial and archaeal genomes in GTDB; a single-pass web-search scout.
  Evidence: rated "not adversarially verified" by the research.
- GTDB release R10-RS226 holds 715,230 bacterial and 17,245 archaeal genomes in 136,646 and 6,968 species clusters respectively. (Parks and others 2026; Parks et al. 2022)
  Holds for: GTDB release R10-RS226; a single-pass web-search scout; the note says to treat every figure as a lead to confirm against the primary source.
  Evidence: rated "not adversarially verified" by the research.
- In GTDB a node at species rank is a genome cluster, not a named type strain alone. (Parks and others 2026; Parks et al. 2022)
  Holds for: GTDB species clusters; a single-pass web-search scout.
  Evidence: rated "not adversarially verified" by the research.
- GTDB is bulk-downloadable and explicitly tracks consistency against NCBI taxonomy. (Parks and others 2026; Parks et al. 2022)
  Holds for: GTDB; a single-pass web-search scout.
  Evidence: rated "not adversarially verified" by the research.

### Fungal name repositories

- Fungi sit under Index Fungorum, MycoBank and Fungal Names, the three recognised fungal repositories; fungi enter the GBIF Backbone Taxonomy via Index Fungorum, given there with 114,301 names. (GBIF n.d.; Six questions answered about the GBIF Ba n.d.; Silva and others 2025; taxize gnr_resolve (Global Names Resolve n.d.)
  Holds for: fungal names; a single-pass web-search scout; the note says to treat every figure as a lead to confirm against the primary source.
  Evidence: rated "not adversarially verified" by the research.

### The cross-kingdom backbone (GBIF Backbone, Catalogue of Life)

Builds on: Fungal name repositories.

- The GBIF Backbone Taxonomy is a single synthetic cross-kingdom classification (eight kingdoms; Linnaean ranks Kingdom to Species plus subspecies, variety and forma) built by starting from the Catalogue of Life and merging other authorities in priority order. (GBIF n.d.; Six questions answered about the GBIF Ba n.d.; Silva and others 2025; taxize gnr_resolve (Global Names Resolve n.d.)
  Holds for: the GBIF Backbone Taxonomy; a single-pass web-search scout.
  Evidence: rated "not adversarially verified" by the research.
- The GBIF Backbone Taxonomy explicitly cross-walks names between sources. (GBIF n.d.; Six questions answered about the GBIF Ba n.d.; Silva and others 2025; taxize gnr_resolve (Global Names Resolve n.d.)
  Holds for: the GBIF Backbone Taxonomy; a single-pass web-search scout.
  Evidence: rated "not adversarially verified" by the research.
- Fungi enter the GBIF Backbone Taxonomy via Index Fungorum. (GBIF n.d.; Six questions answered about the GBIF Ba n.d.; Silva and others 2025; taxize gnr_resolve (Global Names Resolve n.d.)
  Holds for: the GBIF Backbone Taxonomy; a single-pass web-search scout.
  Evidence: rated "not adversarially verified" by the research.
- The GBIF backbone build has been discontinued in favour of the eXtended Catalogue of Life (COL XR), which is now the cross-kingdom backbone to track. (GBIF n.d.; Six questions answered about the GBIF Ba n.d.; Silva and others 2025; taxize gnr_resolve (Global Names Resolve n.d.)
  Holds for: the GBIF backbone and the eXtended Catalogue of Life; a single-pass web-search scout.
  Evidence: rated "not adversarially verified" by the research.
- The nearest single cross-kingdom backbone is the Catalogue of Life (eXtended), which now drives the GBIF Backbone, but it is coarse. (the verdict cites no source)
  Holds for: prokaryotes, fungi and plants; the provisional single-pass verdict.
  Evidence: rated "not adversarially verified" by the research.

### Whether one authoritative taxonomy covers prokaryotes, fungi and plants

Builds on: Prokaryote reference taxonomies (GTDB, NCBI Taxonomy, LPSN), Phylum renaming and the convergence of names, Fungal name repositories, The cross-kingdom backbone (GBIF Backbone, Catalogue of Life).

- No single authoritative taxonomy covers prokaryotes, fungi and plants: several must be integrated. (the verdict cites no source)
  Holds for: prokaryotes, fungi and plants; the provisional single-pass verdict.
  Evidence: rated "not adversarially verified" by the research.
  The research does not say whether contrary evidence was searched for.

### Taxon-name resolution tooling

- Documented tooling exists for resolving free-text taxon names, likely stronger than in the gene case: unlike microbial gene normalisation, taxonomic name resolution is a mature, dedicated tooling area (TNRS, GNverifier/Global Names, GBIF fuzzy matching, taxize, Taxamatch, Pytaxon) with a best-practices review. (Grenie et al. 2023; Boyle et al. 2013; Silva and others 2025; taxize gnr_resolve (Global Names Resolve n.d.)
  Holds for: free-text taxon names; the provisional single-pass verdict.
  Evidence: rated "not adversarially verified" by the research.
  The research does not say whether contrary evidence was searched for.
- Dedicated name-resolution tools exist with established methods: TNRS (plant names; parsing, fuzzy matching and authority correction; thousands of names per run), Taxamatch (a near/fuzzy matching algorithm), GNverifier/Global Names, taxize `gnr_resolve` (with a `with_context` option that restricts matching to a taxonomic context and avoids cross-group homonyms), GBIF fuzzy matching (`TAXON_MATCH_FUZZY`) and Pytaxon (Python, the GNV API plus fuzzy matching). (Grenie et al. 2023; Boyle et al. 2013; Silva and others 2025; taxize gnr_resolve (Global Names Resolve n.d.)
  Holds for: the tools as documented; a single-pass web-search scout.
  Evidence: rated "not adversarially verified" by the research.
- Grenié et al. (2023) is a review of tools, databases and best practices for harmonising taxon names. (Grenie et al. 2023)
  Holds for: harmonising taxon names in biodiversity data; a single-pass web-search scout.
  Evidence: rated "not adversarially verified" by the research.
- The grounding step has off-the-shelf, reviewed options. (Grenie et al. 2023; Boyle et al. 2013; Silva and others 2025; taxize gnr_resolve (Global Names Resolve n.d.)
  Holds for: grounding free-text taxon names; a single-pass web-search scout.
  Evidence: rated "not adversarially verified" by the research.
- The matching problem (synonyms, fuzzy matching of misspellings, homonyms via context) is largely handled. (the verdict cites no source)
  Holds for: resolving free-text taxon names; the provisional single-pass verdict.
  Evidence: rated "not adversarially verified" by the research.
- The name-resolution tools are documented as effective, but specific precision/recall figures, including match rates for GNverifier, GBIF and TNRS on prokaryote and mixed-kingdom names, were not captured in this pass. (an absence in the scout's searches)
  Holds for: GNverifier, GBIF and TNRS on prokaryote and mixed-kingdom names; a single-pass web-search scout.
  Evidence: a search result.
  The research does not say whether this was searched for.

### The choice of authority

Builds on: Taxon-name resolution tooling, Whether one authoritative taxonomy covers prokaryotes, fungi and plants.

- The unsolved part of taxon-name resolution is a curation choice (which authority's lineage to adopt), not a matching failure. (the verdict cites no source)
  Holds for: resolving free-text taxon names; the provisional single-pass verdict.
  Evidence: rated "not adversarially verified" by the research.
- The taxonomy case inverts the gene case in one helpful way: name resolution is the easy part (mature tooling), and the hard part is the authority choice. (the reviewer's reading)
  Holds for: the taxonomy case against the gene case; provisional and not committed.

### Informal labels in the data

Builds on: Taxon-name resolution tooling.

- Informal labels in the data (`AMF`, `Asgard`, `A21b`) almost certainly have no canonical taxon, confirming a review-queue residual as on the gene side. (no source cited)
  Holds for: informal labels in the data; listed among what still needs confirming.

### A backbone arrangement to test

Builds on: The choice of authority, GTDB structure and identifiers, Phylum renaming and the convergence of names, The cross-kingdom backbone (GBIF Backbone, Catalogue of Life), Fungal name repositories, Taxon-name resolution tooling.

- A natural shape to test: pick GTDB as the prokaryote backbone (genome-based, and it matches the GTDB-style phylum tags already in the data), keep NCBI Taxonomy as the cross-domain taxid spine and fallback, route host plants and fungi through the Catalogue of Life/GBIF (with Index Fungorum/MycoBank for fungi), and ground free-text tags with GNverifier or GBIF matching. (the reviewer's hypothesis)
  Holds for: the data; provisional, not committed.
  Evidence: the reviewer's reading.

## Do not say

Wordings the research itself says are wrong or overstated, each with the reason and what to say instead.

- Do not write: "These taxonomy findings are verified."
  Why: The findings come from four direct web searches, not the deep-research harness, so they are not adversarially verified, and the note says to treat every figure as a lead to confirm against the primary source.
  Say instead: The scout's findings were never checked by a second reader or verified: its verdicts rest on the GTDB/NCBI divergence, the coarse Catalogue of Life backbone and the maturity of name-resolution tooling, and its figures (GTDB R10-RS226's 715,230 bacterial and 17,245 archaeal genomes in 136,646 and 6,968 species clusters; Index Fungorum's 114,301 names) are leads to confirm against the primary sources; harness verification of all of it on the same brief is still to be done.
  The research does not say whether this was searched for.
- Do not write: "The project uses GTDB as its prokaryote backbone, NCBI Taxonomy as its taxid spine and the Catalogue of Life/GBIF for host plants and fungi."
  Why: The note gives this arrangement as a hypothesis for a future decision note, not a commitment.
  Say instead: A natural shape to test: pick GTDB as the prokaryote backbone (genome-based, and it matches the GTDB-style phylum tags already in the data), keep NCBI Taxonomy as the cross-domain taxid spine and fallback, route host plants and fungi through the Catalogue of Life/GBIF (with Index Fungorum/MycoBank for fungi), and ground free-text tags with GNverifier or GBIF matching. (the reviewer's hypothesis)
  Holds for: the data; provisional, not committed.
  Evidence: the reviewer's reading.

## Gaps

What the research did not establish.

- The scout's findings were never checked by a second reader or verified: its verdicts rest on the GTDB/NCBI divergence, the coarse Catalogue of Life backbone and the maturity of name-resolution tooling, and its figures (GTDB R10-RS226's 715,230 bacterial and 17,245 archaeal genomes in 136,646 and 6,968 species clusters; Index Fungorum's 114,301 names) are leads to confirm against the primary sources; harness verification of all of it on the same brief is still to be done.
  The research does not say whether this was searched for.
- Match-rate figures (precision and recall) for GNverifier, GBIF and TNRS on prokaryote and mixed-kingdom names.
  The research does not say whether this was searched for.
- How complete the GTDB-to-NCBI identifier mapping is, and the exact lineage disagreements beyond phylum names.
  The research does not say whether this was searched for.
- Whether the informal labels in the data (`AMF`, `Asgard`, `A21b`) indeed have no canonical taxon.
  The research does not say whether this was searched for.

## References

- Anonymous (2022). Harmonizing Prokaryotic Nomenclature: Fixing the Fuss over Phylum Name Flipping. mBio 13(3). https://doi.org/10.1128/mbio.00970-22
- Anonymous (n.d.). Six questions answered about the GBIF Backbone Taxonomy. GBIF Data Blog. https://data-blog.gbif.org/post/gbif-backbone-taxonomy/
- Anonymous (n.d.). taxize gnr_resolve (Global Names Resolver). rOpenSci. https://rdrr.io/cran/taxize/man/gnr_resolve.html
- Boyle, B.; Hopkins, N.; Lu, Z.; others (2013). The taxonomic name resolution service: an online tool for automated standardization of plant names. BMC Bioinformatics 14: 16. https://doi.org/10.1186/1471-2105-14-16
- da Silva; others (2025). Pytaxon: a Python software for resolving and correcting taxonomic names in biodiversity data.
- GBIF Secretariat (n.d.). GBIF Backbone Taxonomy. https://www.gbif.org/dataset/d7dddbf4-2cf0-4f39-9b2a-bb099caae36c
- Grenie, M.; Berti, E.; Carvajal-Quintero, J.; others (2023). Harmonizing taxon names in biodiversity data: a review of tools, databases and best practices. Methods in Ecology and Evolution 14(1): 12. https://doi.org/10.1111/2041-210X.13802
- Parks, D. H.; Chuvochina, M.; Rinke, C.; others (2022). GTDB: an ongoing census of bacterial and archaeal diversity through a phylogenetically consistent, rank normalized and complete genome-based taxonomy. Nucleic Acids Research 50(D1): D785. https://doi.org/10.1093/nar/gkab776
- Parks, D. H.; others (2026). GTDB release 10: a complete and systematic taxonomy. Nucleic Acids Research 54(D1): D743. https://academic.oup.com/nar/article/54/D1/D743/8296754
