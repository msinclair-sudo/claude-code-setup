---
name: biblion
description: Work with a biblion project three ways — query the existing corpus (papers + citation graph + precomputed semantic embeddings + a coded concept spine + environmental sample measurements) through its read-only MCP server; ingest NEW literature for a topic by constructing boolean Semantic Scholar searches and running biblion's search→enrich pipeline; or grow the ENVIRONMENTAL sample pool by reading the coverage report and driving the discovery loop. Use when finding/surfacing similar or related papers, exploring topic structure, traversing the citation graph, slicing papers by measured environmental conditions (pH, temperature, nitrogen), checking where sample coverage is thin, sourcing/pulling new papers or new BioSamples, or registering/relocating the biblion MCP server. When asked to "search a topic", first clarify scope. Triggers: "biblion", "related/similar papers", "citation graph", "find/source new literature", "search papers on", "what pH range", "environmental gradient", "sample coverage", "more samples", "register the biblion mcp".
---

# biblion — corpus query, literature ingest, and sample acquisition

biblion stores each project as a SQLite database (a paper per row, plus a
citation graph) under a data dir, enriched with **precomputed** semantic
neighbours, a **coded concept spine** (`structure_nodes` / `structure_edges` /
`structure_attachments`), and — where environmental data has been harvested — a
layer of **physical samples with measured conditions** (`sample_measurements`,
`dataset_samples`).

This skill does three things:

1. registers and drives biblion's read-only **MCP server** to query the existing
   corpus (bounded, never writes);
2. drives the `biblion` CLI **search→enrich** pipeline to ingest new literature;
3. drives the **environmental sample acquisition loop** — read the coverage
   report, then fill the holes it names.

Which one applies is decided by the scope question below.

## First, when asked to "search for a topic": clarify scope

"Search biblion for <topic>" is ambiguous. **Before doing anything, if the
prompt has not already specified the scope, ask the user which of these they
want** (present it as the first response):

1. **Search the current database(s)** — read-only query of what's *already
   ingested* (this skill). Instant, no writes, no API calls. Finds nothing that
   hasn't been imported yet; semantic search needs an `embedded` project.
2. **Get new literature** — *ingest*: search Semantic Scholar for the topic and
   pull NEW papers into a biblion DB, then enrich. This **writes**, runs through
   the single-writer daemon, takes minutes, and uses the API keys in `~/.env`.
   See **Get new literature (ingest pathway)** below — it uses the `biblion` CLI,
   not the MCP tools.
3. **Both** — query what's already there, then fetch fresh literature to fill the
   gaps, and report what was already known vs. newly pulled.

Skip the question only if the user already made the scope explicit (e.g. "search
*the existing* PhD_proposal DB", or "*pull new* papers on X"). Default to nothing
— do not silently assume "query only".

A request about **samples, measured conditions, or coverage** ("do we have enough
pH data", "get more nitrogen samples") is a fourth path and needs no scope
question — go to **Environmental samples** below.

## Configuration — the one secure place

The real values live in the **global `~/.env`** (chmod 600, outside any git
repo), shared with the other skills and the biblion daemon. `config.sh` (sibling
of this file) only *sources* that env and supplies fallback defaults, so no
machine paths or secrets are committed inside the skill. It reads, separately:
- `BIBLION_HOME` — where biblion's **code** lives. The server file
  `biblion/mcp_server.py` is run **directly from here** (by path), so this dir is
  the real source of the code even if the interpreter also has biblion installed.
- `BIBLION_PYTHON` — an interpreter with biblion's **deps** (`pip install 'biblion[mcp]'`).
- `BIBLION_DATA_DIR` — where the project DBs live (`<name>/<name>.db`).
- `BIBLION_TRANSPORT` (`stdio` default | `http`) and `BIBLION_HTTP_URL`.

To **relocate biblion** (e.g. into a managed skills dev location) or rotate keys:
edit those values in `~/.env` (NOT `config.sh`), then re-run
`scripts/check.sh && scripts/register.sh`. Override the env path with
`BIBLION_GLOBAL_ENV` if it lives elsewhere. Nothing in the skill hardcodes a path.

## Setup (one-time, and after any relocation)

```bash
bash scripts/check.sh        # verify code imports, deps present, data dir has projects
bash scripts/register.sh     # register the MCP at user scope (stdio by default)
# then restart Claude Code (or run /mcp) so the biblion_* tools load
```

- `register.sh` uses `claude mcp add` at **user scope** — the tools are then
  available in every session. It is idempotent (re-running re-registers cleanly).
- `scripts/unregister.sh` removes the registration.
- **http instead of stdio:** set `BIBLION_TRANSPORT=http` in `~/.env`, bring up
  the server (`biblion up`, or `docker compose up -d mcp` in `BIBLION_HOME`), then
  re-run `register.sh`. It registers `BIBLION_HTTP_URL` instead of launching a
  subprocess.

## Tools

Every tool takes a `database` argument — the **project name** (e.g.
`PhD_proposal`); list options first with `biblion_list_databases`. If a tool you
expected is missing, your client is holding a stale registration — re-run
`register.sh` and restart. The server's own module docstring is the authority on
what is registered.

| Tool | Use it to… |
|---|---|
| `biblion_list_databases` | see which projects exist + whether they're `embedded` |
| `biblion_describe_schema` | get tables, columns, and query notes for a project |
| `biblion_find_papers` | lexical title/abstract search |
| `biblion_semantic_search` | free-text → papers nearest a question/topic by MEANING; ranks in the **raw 768-d** SPECTER2 space |
| `biblion_similar_papers` | papers nearest a given paper; reads neighbours precomputed in **PCA-100** — a *different* space from the line above, so don't compare their distances |
| `biblion_paper_citations` | a paper's references or citers (citation graph) |
| `biblion_gradient_entities` | which concepts occur along a measured environmental gradient (e.g. organisms in acidic soil) |
| `biblion_coverage_gaps` | where environmental coverage is thin, and whether each hole needs **acquisition** or **recovery** |
| `biblion_entity_hierarchy` | browse the concept vocabulary as a tree |
| `biblion_query_sql` | run any custom **read-only** SQL (the escape hatch) |
| `biblion_entity_threads` | **RETIRED LAYER.** Threads papers over the old reader extraction catalogue (`cat_entities` / `cat_relations`). On a current corpus it returns 0 rows with a note. Do not build a workflow on it. |

**`biblion_compound_search` no longer exists** — it was removed with the reader
layer. If you see it offered, the registration is stale.

## Search the current database — build a reading list

When scope = "search the current database(s)" (and the final step after enrich
finishes for "get new literature" / "both"). Selection rests on **two precomputed
surfaces — never on clusters, never on citation counts**:

- **Proximity ("what is near this?")** — the semantic embedding layer:
  `biblion_semantic_search` (free-text question → nearest papers, no anchor paper
  needed), `biblion_similar_papers` and the `paper_neighbors` hop (paper →
  related). Faithful continuous cosine distance, not a hard label.
- **Themes ("what concepts group these papers?")** — the **coded spine**:
  `paper_entities` joined to `structure_nodes`, browsable with
  `biblion_entity_hierarchy` and sliceable by measured condition with
  `biblion_gradient_entities`. These are *coded* concepts (CURIE-keyed: `ENVO:`,
  `NCBITaxon:`, `MIXS:`, `GO:`), not free-text labels, so they join cleanly to the
  sample layer.

  This **replaces the old reader entity/relation graph**. `cat_entities`,
  `cat_relations`, `entity_cooccurrence` and `relation_consensus` were retired; on
  a current corpus they are absent or empty. An empty result from any of them
  means *the layer is gone*, not that the corpus has no concepts — do not report
  it as a finding. Two `cat_`-prefixed tables are **not** that layer and are
  live: `catalogue_provenance` (sample→publication routing) and `cat_entity_refs`.

Citation in-degree is a **secondary, clearly-bounded** signal (roots only): in a
young corpus it is sparse and back-biased toward a few old reviews, so a
citation-ranked "top-N" misses most of the field. The goal is a *reasoned,
coverage-aware set of interest papers* chosen with whole-corpus awareness, then
full-text-ingested and tagged. (Steps 0 and 8 write; steps 1–7 are read-only.)

0. **Embedding is mandatory — no paper is "of interest" before it.** Check
   `biblion_list_databases`; if the project is `embedded: false`, embed it first:
   `biblion advanced snapshot` → `biblion advanced embedding` (the `[embed]` GPU
   job → builds `paper_vectors` / `paper_neighbors`). Do **not** fall back to a
   citation-only shortcut.
1. **Read the map before selecting — coverage, then themes.**
   - **Coverage.** The embedded set is the seeds plus their citation-bridged
     neighbours (a node with edges to ≥2 seeds is folded in); papers the search
     never found and that aren't bridged are **deliberately** out of scope, not a
     gap to fill. Report map size first so the basis is legible:
     ```sql
     SELECT
      (SELECT COUNT(*) FROM papers WHERE tombstone=0)                AS papers_total,
      (SELECT COUNT(*) FROM papers WHERE tombstone=0 AND is_seed=1)  AS seeds,
      (SELECT COUNT(DISTINCT paper_id) FROM paper_neighbors)         AS embedded;  -- the map
     ```
   - **Theme inventory (the map's content).** Read what the corpus is *about*
     from the coded spine:
     ```sql
     -- top coded concepts by how many papers carry them
     SELECT n.entity_type, n.label, n.node_uid, COUNT(DISTINCT pe.paper_id) AS papers
     FROM paper_entities pe JOIN structure_nodes n ON n.node_uid = pe.code
     GROUP BY pe.code ORDER BY papers DESC LIMIT 40;
     -- specific associations (npmi ranks specific over frequent-hub co-occurrence)
     SELECT a_uid, b_uid, papers, ROUND(npmi,3) AS npmi
     FROM structure_cooccurrence WHERE papers >= 2 ORDER BY npmi DESC LIMIT 40;
     ```
     `biblion_entity_hierarchy` browses the same vocabulary as a tree.
2. **Anchor — question first, then strings.** Turn the user's questions/terms into
   entry points: `biblion_semantic_search` on each question phrase (meaning-based,
   no anchor paper needed) and `biblion_find_papers` / `biblion_query_sql` for
   exact terms. For a question about **conditions** ("which studies found X in
   acidic soil"), `biblion_gradient_entities` is the direct route — it slices the
   sample layer by measured value and returns the concepts that occur there.
3. **Related literature (meaning, not strings).** Expand each anchor two ways:
   - **Semantic hop** — `biblion_similar_papers` / the `paper_neighbors` hop, ranked
     by `distance` (lower = closer); the keyword→expand form (`MIN(distance)` over
     anchors, `space='semantic'`) catches papers a keyword search would miss.
   - **Concept thread** — papers sharing a coded concept:
     ```sql
     SELECT pe2.paper_id, COUNT(*) AS shared
     FROM paper_entities pe1 JOIN paper_entities pe2 ON pe2.code = pe1.code
     WHERE pe1.paper_id = ? AND pe2.paper_id != pe1.paper_id
     GROUP BY pe2.paper_id HAVING shared >= 2 ORDER BY shared DESC LIMIT 30;
     ```
4. **Centrality — two signals, treated separately (never conflated).**
   - **Citation in-degree** (`biblion_paper_citations`, most-cited-within-corpus,
     co-citation) → the field's **intellectual roots**. *Strongly publication-time
     biased*: in-corpus citations only flow backward, so a paper from the last
     ~2–3 years structurally cannot have accrued them. Read a raw "most-cited" list
     as *founding works*, never as present importance.
   - **Semantic centrality** = reverse-nearest-neighbour in-degree in
     `paper_neighbors` (how many papers list X as a neighbour, `space='semantic'`)
     → the corpus's **current centre of mass**, and it is **time-free**. Its own
     bias: it rewards dense regions and generic reviews, so check the top hits
     aren't off-topic bleed.
   - Optional third view: **age-normalised citation rate** surfaces recent *risers*
     neither raw measure catches.
   Do **not** average these into one score — present roots, current-centre, and
   risers apart.
5. **Theme coverage.** For breadth across the field, cover the corpus's **themes**.
   Take the on-topic concepts from the step-1 inventory as coverage axes and pull
   representative papers for each — the concept-thread query above, or
   `biblion_semantic_search` on the theme phrase. This is how the set gains breadth
   instead of piling onto the dense semantic centre.
6. **Off-centre & outliers — the semantic frontier, sampled on purpose.** Don't
   only read the dense centre (it self-confirms what the search already surfaced):
   ```sql
   SELECT p.id, ROUND(MIN(n.distance),3) AS nearest, p.year, p.title
   FROM papers p JOIN paper_neighbors n ON n.paper_id = p.id
   WHERE n.space='semantic' GROUP BY p.id ORDER BY nearest DESC LIMIT 30;
   ```
   Plus **low semantic centrality** (bottom of the reverse-NN count) and **rare
   coded concepts** (carried by 1–2 papers). Deliberately include some, and reason
   about each (off-topic bleed vs genuinely novel work).
7. **Synthesise the interest set — coverage-aware.** Combine theme coverage (the
   primary axis) with semantic closeness, citation centrality (debiased per step 4)
   and frontier interest. Carry each paper's `doi`, `is_open_access`,
   `pubmed_central_id`. Present the set **grouped by theme**.

The steps below run **after** the interest set exists.

8. **Pull full text into the database — do NOT bulk-read.** Run
   `biblion fulltext --ids <interest ids>` (or `--tag <t>`; `--seeds` / `--all`).
   It pulls open-access full text from **several equal sources, tried in order
   until one yields text** — PMC OA JATS (NCBI `efetch db=pmc`), then an OA PDF
   resolved from the DOI via OpenAlex/Unpaywall (extracted with `pdftotext`), then
   the CORE aggregator — stores it in `paper_fulltext`, and **tags the row
   `full-text`**. All sources are treated identically; the trying-order is
   operational, not a quality ranking. `--sources pmc,oa-pdf,core` restricts the
   set. Idempotent (`--force` refetches; `--dry-run` / `--limit`).
   - **Per-theme guarantee** — walk each theme's ranked papers most-relevant first
     and `biblion fulltext --ids` the top one that resolves, falling to the next
     when a pick has no retrievable text. This keeps a theme from being lost
     because its most-central paper is paywalled.
   - *Populates and tags* — **not** an instruction to read every paper. Read an
     individual full text inline only when the user asks.
   - Why the command, not `WebFetch`: it goes through OA APIs and primes publisher
     landing pages (many bot-block a bare GET). A paper no source can serve stays
     **abstract-only** (untagged).
9. **Visualise** — the explorer (`biblion up`, then `127.0.0.1:8010`) shows the 3D
   map, the concept browser, the sample map and the measured-property panels.

**Before writing SQL**, read `$BIBLION_HOME/docs-site/querying.md` — the current
schema, copy-paste recipes and the gotchas that matter:
- three vector spaces: `paper_neighbors` `space='semantic'` is for similarity;
  `paper_vectors` `pre`/`post` are UMAP **layout**, not distance.
- the coded spine is CURIE-keyed; `structure_edges.is_primary = 1` is the browse
  tree, the rest of the edges are the DAG truth.
- use `tombstone = 0` and the `citations_canonical` view; **bound** graph
  self-joins (subset + LIMIT) or they time out.
- `sample_measurements` joins to papers through `sample_paper_link`, whose
  `relation` lane is `deposited` / `used` / `unknown` — an unfiltered join mixes
  data a paper produced with data it merely reused.

## Environmental samples — reading coverage, and growing it

The corpus carries **physical samples** (BioSamples) with measured conditions.
This layer is what makes "which studies actually measured acidic soil" answerable.

**Reading it:**
- `biblion_gradient_entities` — concepts occurring in a measured band, e.g.
  `measurement='MIXS:ph', max_value=5.5`. Note it takes the **code** (`MIXS:ph`).
- `sample_measurements` (sample, code, value, unit, `independence_weight`) is the
  browsable value layer; `dataset_sample_attrs` is the **raw** BioSample layer
  underneath it, including values that never made it through.
- Always read `kind` with `kind_src`: `organism-inferred` is a guess off free text,
  and `kind='ambiguous'` means two sourced claims contradict — distinct from
  `unknown` (no evidence). Never arbitrate a conflict by taking the higher rung.

**Before proposing that anyone fetch more samples, run `biblion_coverage_gaps`.**
A thin property has two possible causes that look identical in a sample count:

- **`recover`** — the samples are already held and their values were REFUSED, most
  often a bare number with no unit, which biblion flags rather than guessing.
  Acquiring more would buy data already in hand.
- **`acquire`** — the samples genuinely don't carry the value. Only new samples help.

An `acquire` row with an **empty `profiles` list** means nothing currently hunts
for that property — the fix is a new profile in
`biblion/enrich/sample_discovery.py`, not another run of an existing sweep. Read
`notes` too: an unresolvable biome, a code the spine has never seen, or a property
with no unit spec each produce a number that looks like zero coverage and isn't.

The target itself lives in `dataset_env_curation.json` (`coverage_target`) — edit
the deployed copy at `~/biblion-data/curation/` to change what counts as coverage,
then copy it back into the repo to make it permanent.

**Filling an `acquire` hole — the order is required and silent when wrong:**

```bash
biblion advanced discover-samples --goal <name> --online   # or --profile <p>
biblion advanced route-samples                             # attribute to publications
biblion advanced entity-tree --online     # EAV -> spine; needs Redis + a live writer
#   ...wait for the structure lanes to drain...
biblion advanced measurements             # rebuild sample_measurements
```

**Goals vs profiles.** A `--profile` is one of nine hardcoded biome sweeps that keeps a
sample carrying **any one** of a property list. A `--goal` is declared in the curation
file's `sample_goals` block and keeps a sample only if it carries a value from **every**
required group (`[["ph"], ["tot_nitro","nitrate","ammonium"], …]` — OR within, AND
between). Use a goal when you want samples that are *complete*, a profile when you want
biome coverage. The run reports which group the rejects missed, which is the number that
says whether a goal is well-formed or just too strict.

Two things about goals that are easy to get wrong:

- **A declared `kind` is not a filter.** BioSample does not record the assay, so a goal
  saying `"kind": "metagenome"` states intent; whether the samples really are
  metagenomes is settled afterwards by `sample_kind`. Check it, don't assume it.
- **NCBI's count over-promises.** The query matches on attribute *names*, so a record
  that declares `ph` and fills it with the literal string `"missing"` is counted. On a
  600-record sample of one goal the real yield was 66%, and it was bimodal per
  submission batch rather than uniform — so sample across the result set, not from the
  first page.

Out of order nothing errors — the derived layer just reads half-applied
attachments and reports numbers that are quietly wrong. `biblion advanced
spine-rebuild` runs the whole chain in the right order and is the safe default;
the compose `spine` service runs it on a loop. `discover-samples` and
`entity-tree --online` hit the network and need the API keys in `~/.env`.

**Publication-side growth** is a separate lever: many discovered studies have a
publication not yet in the corpus. `biblion advanced referrals --rebuild` ranks
them, `--acquire-top N` seeds them into the ingest pipeline.

## Get new literature (ingest pathway)

When scope resolves to "get new literature" (or the ingest half of "both").
Mechanism: `biblion search <searches/*.json>` pushes S2 hits to the cache →
`biblion enrich` drains them into SQLite and fills metadata/abstracts/citations
→ optional `biblion hop` snowballs citations. This **writes** (single-writer
daemon) and uses the S2 key in `~/.env`. Run from `BIBLION_HOME` via the
`biblion` CLI — the MCP tools are read-only and play no part here.

**Claude constructs the queries — the user does not write boolean strings.**

1. **Collect questions/themes** from the user (natural language). Ask for them if
   not already given.
2. **Construct the boolean queries.** For each theme build one query string
   `(facetA1 OR facetA2 OR …) AND (facetB1 OR …) AND (…)`, where each AND-group
   is a *facet* (a concept) and each OR-list is that facet's *synonyms/variants*.
   This is the quantitative, factorial style of
   `data/inputs/searches/microalgae.json`, not hand-picked phrases. Give each query
   a stable `id` and a human `title`. Rules the parser imposes: terms ≤3 chars are
   dropped; multiword terms are auto-quoted as phrases; trailing `*` wildcards are
   stripped; **`NOT` is silently removed** (S2 ignores it — don't rely on
   exclusions). **Show the constructed queries to the user for review before
   running.**
3. **Pick the degree** (the knob that sets how hard the APIs are hit):
   - `--mode simplify` → **1** S2 call per query. Cheap, shallow, good for many.
   - `--mode expand` → **factorial**: the Cartesian product of the OR-groups.
   - **Before running `expand`, compute and show** the sub-query count per query
     and the total, plus the rough pull `≈ total sub-queries × --sub-limit` papers
     (pre-dedup), so the blow-up is visible up front.
   - `--sub-limit` = papers per sub-query (default 100); optional `--year-min` /
     `--year-max`.
4. **Pick the target project** — an existing DB or a new one (`biblion init`);
   set it as the current project / `BIBLION_DB`.
5. **Write** the set to `data/inputs/searches/<name>.json` (the `{"queries":
   [{id,title,query}]}` shape).
6. **Submit the search and monitor the pull to completion.**
   `biblion search data/inputs/searches/<name>.json --mode <…> --sub-limit <…>`.
   This call **blocks**: it transiently spawns the merge writer/resolver, pages
   the S2 hits, drains them into SQLite, and flags `is_seed=1`. Launch it as a
   **background** process and **wait for it to finish**, surfacing its
   per-sub-query progress. It is resumable — per-query Redis checkpoints skip
   completed sub-queries; `--force` re-runs them. Do **not** start enrich until
   the search process has exited 0.
7. **Then enrich, and wait for it to finish.** `biblion enrich --exit-when-idle`
   (from `BIBLION_HOME`, same `BIBLION_DB`) — a daemon supervisor that drains and
   **exits 0 on its own** once all work is cleared, printing `all work cleared`.
   Optionally run `biblion hop` first to snowball citations from the seeds. Treat
   it like `search`: background, and wait for the exit.
   - **Set-and-forget alternative:** drop `--exit-when-idle` and it runs forever —
     monitor with `biblion qc` / `biblion health`, stop with SIGTERM.

Note: newly ingested papers are **not** semantically searchable until the separate
**GPU embedding** job runs.

## Scope

This skill drives biblion's **query** tools (read-only MCP), the **search →
enrich** ingest pathway, the **embedding** prerequisite for selection, **full-text
acquisition + tagging**, and the **environmental sample acquisition loop** — all
via the `biblion` CLI. The embedding step needs the `[embed]` GPU environment and
is heavy (minutes). Out of scope: standing up the docker-compose stack by hand
(use `biblion up`), and the reader package (`biblion_reader/`), which no longer
feeds biblion.
