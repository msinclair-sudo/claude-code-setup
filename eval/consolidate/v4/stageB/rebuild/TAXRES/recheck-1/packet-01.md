## gtdb-structure.1 (claim)

GTDB gives a complete, rank-normalised seven-rank classification (species to domain) for all genomes, sourced from NCBI Assembly.

- conf: not stated
- class: not stated
- holds: bacterial and archaeal genomes in GTDB; a single-pass web-search scout
- src: parksGTDBRelease102026, parksGTDBOngoingCensus2022
- rating: "not adversarially verified"
- trail: TAXRES §GTDB structure

From the note:

> TAXRES:B-0013 [GTDB structure and identifiers] GTDB gives a **complete, rank-normalised seven-rank classification** (species to domain) for all genomes, sourced from NCBI Assembly.
>
> TAXRES:B-0014 [GTDB structure and identifiers] Release R10-RS226: 715,230 bacterial + 17,245 archaeal genomes in 136,646 + 6,968 **species clusters** (a node at species rank is a genome cluster, not a named type strain alone).
>
> TAXRES:B-0015 [GTDB structure and identifiers] It is bulk-downloadable and explicitly tracks consistency against NCBI taxonomy.
>
> TAXRES:B-0005 [warning: This is a single-pass scout, not a verified review] These findings come from four direct web searches, NOT the `deep-research` harness, so they are **not** adversarially verified and carry no 3-vote confidence.
>

Not found in the cited text (where to look, not what is wrong): holds: single-pass

## fungal-repositories.1 (claim)

Fungi sit under Index Fungorum, MycoBank and Fungal Names, the three recognised fungal repositories; fungi enter the GBIF Backbone Taxonomy via Index Fungorum, given there with 114,301 names.

- conf: not stated
- class: not stated
- holds: fungal names; a single-pass web-search scout; the note says to treat every figure as a lead to confirm against the primary source
- src: gbifGBIFBackboneTaxonomy, anonSixQuestionsAnswered, silvaPytaxonPythonSoftware2025, anonTaxizeGnrResolve
- rating: "not adversarially verified"
- trail: TAXRES §The cross-kingdom backbone, §Provisional verdicts

From the note:

> TAXRES:A-001 [Provisional verdicts (single-pass)] **(a) Single authoritative taxonomy across prokaryotes, fungi, plants? — MUST INTEGRATE SEVERAL.** Prokaryotes split between **GTDB** (genome-based, RED-normalised) and **NCBI Taxonomy / LPSN** (nomenclatural code), with an active and partly-converged divergence; fungi sit under Index Fungorum / MycoBank / Fungal Names; the nearest single cross-kingdom backbone is the **Catalogue of Life (eXtended)** that now drives the GBIF Backbone, but it is coarse.
>
> TAXRES:B-0016 [The cross-kingdom backbone] The **GBIF Backbone Taxonomy** is a single synthetic cross-kingdom classification (eight kingdoms; Linnaean ranks Kingdom to Species plus subspecies/variety/forma) built by starting from the **Catalogue of Life** and merging other authorities in priority order, and it explicitly **cross-walks names between sources**.
>
> TAXRES:B-0017 [The cross-kingdom backbone] Fungi enter via **Index Fungorum** (114,301 names; one of three recognised fungal repositories with MycoBank and Fungal Names).
>
> TAXRES:B-0018 [The cross-kingdom backbone] Note: the GBIF backbone build has been **discontinued in favour of the eXtended Catalogue of Life (COL XR)**, which is now the cross-kingdom backbone to track.
>
> TAXRES:B-0005 [warning: This is a single-pass scout, not a verified review] These findings come from four direct web searches, NOT the `deep-research` harness, so they are **not** adversarially verified and carry no 3-vote confidence.
>
> TAXRES:B-0006 [warning: This is a single-pass scout, not a verified review] Treat every figure as a lead to confirm against the primary source.
>

Not found in the cited text (where to look, not what is wrong): holds: single-pass

## name-resolution.4 (claim)

The grounding step has off-the-shelf, reviewed options.

- conf: not stated
- class: not stated
- holds: grounding free-text taxon names; a single-pass web-search scout
- src: grenieHarmonizingTaxonNames2023, boyleTaxonomicNameResolution2013, silvaPytaxonPythonSoftware2025, anonTaxizeGnrResolve
- rating: "not adversarially verified"
- trail: TAXRES §Taxon-name resolution

From the note:

> TAXRES:B-0021 [Taxon-name resolution is a mature tooling area] So the grounding step has off-the-shelf, reviewed options.
>
> TAXRES:A-002 [Provisional verdicts (single-pass)] **(b) Evaluated standard for resolving free-text taxon names? — DOCUMENTED TOOLING EXISTS (likely stronger than the gene case).** Unlike microbial gene normalisation, taxonomic name resolution is a **mature, dedicated tooling area** (TNRS, GNverifier/Global Names, GBIF fuzzy matching, `taxize`, Taxamatch, Pytaxon) with a best-practices review.
>
> TAXRES:B-0005 [warning: This is a single-pass scout, not a verified review] These findings come from four direct web searches, NOT the `deep-research` harness, so they are **not** adversarially verified and carry no 3-vote confidence.
>

Not found in the cited text (where to look, not what is wrong): holds: single-pass

## name-resolution.5 (claim)

The matching problem (synonyms, fuzzy matching of misspellings, homonyms via context) is largely handled.

- conf: not stated
- class: not stated
- holds: resolving free-text taxon names; the provisional single-pass verdict
- src: none (the verdict cites no source)
- rating: "not adversarially verified"
- trail: TAXRES §Provisional verdicts

From the note:

> TAXRES:A-003 [Provisional verdicts (single-pass)] The *matching* problem (synonyms, fuzzy/misspelling, homonyms via context) is largely handled; the unsolved part is a **curation choice** (which authority's lineage to adopt), not a matching failure.
>
> TAXRES:A-002 [Provisional verdicts (single-pass)] **(b) Evaluated standard for resolving free-text taxon names? — DOCUMENTED TOOLING EXISTS (likely stronger than the gene case).** Unlike microbial gene normalisation, taxonomic name resolution is a **mature, dedicated tooling area** (TNRS, GNverifier/Global Names, GBIF fuzzy matching, `taxize`, Taxamatch, Pytaxon) with a best-practices review.
>
> TAXRES:B-0005 [warning: This is a single-pass scout, not a verified review] These findings come from four direct web searches, NOT the `deep-research` harness, so they are **not** adversarially verified and carry no 3-vote confidence.
>

Not found in the cited text (where to look, not what is wrong): holds: single-pass

## name-resolution.6 (claim)

The name-resolution tools are documented as effective, but specific precision/recall figures, including match rates for GNverifier, GBIF and TNRS on prokaryote and mixed-kingdom names, were not captured in this pass.

- conf: not stated
- class: search (note: "specific precision/recall figures were not captured this pass")
- holds: GNverifier, GBIF and TNRS on prokaryote and mixed-kingdom names; a single-pass web-search scout
- src: none (an absence in the scout's searches)
- search: not stated
- trail: TAXRES §Provisional verdicts, §What still needs

From the note:

> TAXRES:A-004 [Provisional verdicts (single-pass)] *Caveat:* specific precision/recall figures were not captured this pass.
>
> TAXRES:B-0025 [What still needs confirming] - **Match-rate figures** for GNverifier / GBIF / TNRS on prokaryote and mixed-kingdom names (the tools are documented effective; specific precision/recall not captured here).
>
> TAXRES:B-0005 [warning: This is a single-pass scout, not a verified review] These findings come from four direct web searches, NOT the `deep-research` harness, so they are **not** adversarially verified and carry no 3-vote confidence.
>

Not found in the cited text (where to look, not what is wrong): holds: single-pass

## authority-choice.1 (claim)

The unsolved part of taxon-name resolution is a curation choice (which authority's lineage to adopt), not a matching failure.

- conf: not stated
- class: not stated
- holds: resolving free-text taxon names; the provisional single-pass verdict
- src: none (the verdict cites no source)
- rating: "not adversarially verified"
- trail: TAXRES §Provisional verdicts

From the note:

> TAXRES:A-003 [Provisional verdicts (single-pass)] The *matching* problem (synonyms, fuzzy/misspelling, homonyms via context) is largely handled; the unsolved part is a **curation choice** (which authority's lineage to adopt), not a matching failure.
>
> TAXRES:A-002 [Provisional verdicts (single-pass)] **(b) Evaluated standard for resolving free-text taxon names? — DOCUMENTED TOOLING EXISTS (likely stronger than the gene case).** Unlike microbial gene normalisation, taxonomic name resolution is a **mature, dedicated tooling area** (TNRS, GNverifier/Global Names, GBIF fuzzy matching, `taxize`, Taxamatch, Pytaxon) with a best-practices review.
>
> TAXRES:B-0005 [warning: This is a single-pass scout, not a verified review] These findings come from four direct web searches, NOT the `deep-research` harness, so they are **not** adversarially verified and carry no 3-vote confidence.
>

Not found in the cited text (where to look, not what is wrong): holds: single-pass

