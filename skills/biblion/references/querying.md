# Querying biblion — moved

The query guide is no longer bundled with this skill. Read the live copy:

```
$BIBLION_HOME/docs-site/querying.md
```

(also served at `127.0.0.1:8010/docs` when the stack is up, and published from
`docs-site/` in the biblion repo.)

## Why this file is a pointer now

The bundled copy pointed at `$BIBLION_HOME/docs/querying.md` as its source of
truth — a path that no longer exists — and "re-copy if the schema changes" never
happened. It drifted into being wrong rather than merely old, which is worse: a
stale schema reference reads as authoritative. At the point it was retired it:

- documented `biblion_compound_search`, a tool the MCP server no longer registers;
- presented precomputed **clusters** as a live query surface, after they were
  dropped as one (they survive only as UI scratch);
- described the **reader extraction catalogue** (`cat_entities`, `cat_relations`,
  `entity_cooccurrence`, `relation_consensus`) as the corpus's concept layer, after
  that layer was retired and its rows dropped;
- said nothing at all about the two layers a current corpus is mostly made of — the
  **coded spine** (`structure_nodes` / `structure_edges` / `structure_attachments`,
  `paper_entities`) and the **environmental sample layer** (`sample_measurements`,
  `sample_paper_link`, `dataset_samples`).

One guide, in the repo, versioned with the schema it describes. Do not re-bundle a
copy here.
