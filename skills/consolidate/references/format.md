# The knowledge note: format

One markdown note per research set, beside the results: `<...>/Research/Knowledge/<topic>.md`. Fixed line
grammar so `kn.py lint` can check it and write `<note>.index.json` for scripts. Fields inside an entry are
separated by ` · ` (space, middle dot, space).

## Frontmatter

```yaml
---
type: knowledge
title: 16S amplicon sequencing from sample to count table
inputs:
  - MB-01: Topics/Biology/Research/Results/From sample to count table ... A literature review.md
  - MB-02: Topics/Biology/Research/Results/16S rRNA gene copies per genome ... A literature review.md
built: 2026-10-21
status: draft
tags:
  - research
  - knowledge
---
```

`inputs`: one `ID: path` per result note, the path relative to the vault root. The ID is the brief ID the note
names (MB-01); `kn.py detect` proposes one when it finds none.

## Sections, in this order

```markdown
# <title>

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
| MB-01 | [[From sample to count table ...]] | yes | labelled (access; class; standing) | yes (130) | yes | exact |

## Concepts
### <concept>: <name>
...
## Do not say
## Gaps
## Out of scope
## Sources
```

The Inputs row copies what `kn.py detect` printed; lint compares them. A blank section keeps its heading.

## Concepts

```markdown
### copy-number: 16S rRNA gene copies per genome
needs: genome16s
- **copy-number.1** Bacterial genomes carry 1 to 15 copies of the 16S rRNA gene and archaeal genomes 1 to 4.
  conf: repl (note: "consistent across sources") · class: meas (note: "measured from genomes") · holds: sequenced genomes in rrnDB (2015 release); the sources draw on overlapping NCBI genome sets · src: stoddardRrnDBImprovedTools2015, vetrovskyVariability16SRRNA2013 · trail: MB-02 §D1.1, §D1.2 · from: MB-02:A-002, MB-02:C-001..003
```

- **A concept** is a thing the claims are about: a quantity, a step, a term, a method. ID: lower case, hyphens.
- **`needs:`** the concepts a reader must already have to understand this concept's claims (`needs: none` for
  a root). The graph is the artefact. Where concepts need each other (copy number and relative abundance;
  compositionality and rarefying), give each the same `group: <name>` line and keep them next to each other.
  A group is only for concepts that need each other; lint checks both ways.
- **File order:** any order in which every concept comes after what it needs (members of a group together).

## Claims

`- **<concept>.<n>** <statement>` then one indented line of fields. All six fields are required.

| Field | What goes in it |
|---|---|
| `conf` | the standing the note gives this claim: `repl`, `single`, `cont`, `unclear`, `mixed` (labelled sources disagree), or `not stated`, with its basis in brackets |
| `class` | `meas`, `deriv`, `model`, `assert` (two joined by `/`), or `not stated`, with its basis |
| `holds` | the setting it comes from (system, measurement, scale, n, range) and what it was not shown for, in the note's terms |
| `src` | citekeys from Sources, comma-separated; with labelled citations each may carry its own standing: `mclarenConsistentCorrectableBias2019 (single)` |
| `trail` | where the note verified it: `<ID> §<start of a heading>`, more after commas (`MB-01 §2.2, §2.14`); `§critic` and `§answers` reach those blocks |
| `from` | the inventory items it accounts for: `MB-01:I-0012`, ranges `MB-01:I-0012..0015`, critique items `MB-01:C-004` |

**Basis** for `conf` and `class` (required unless `not stated`):
- `(marker)`: read from the citation labels (`[FT; meas; repl]`) of a note with labelled citations.
- `(critic: C-012)`: the critic's finding about this claim; it overrides the marker and the review.
- `(note: "exact words")`: the note says it in words about this claim ("SINGLE SOURCE", "replicated across
  independent mocks", "contested"). Lint checks the words are in the note.

**Never infer a standing.** If the note gives none for a claim, write `not stated`, even when the prose sounds
confident or names several studies. Counting studies, judging a journal or reading tone is re-rating.

**Statements:**
- One finding per claim, in the form the evidence supports: where the critic corrected or narrowed a claim, the
  claim is the corrected version, and the uncorrected one goes to Do not say if it would mislead.
- Figures keep their own definition and denominator. Never combine figures from different sources into one
  number or range.
- Words and facts come from the note. No examples, explanations or numbers that are not in it.
- Don't trim: every finding the note reports becomes a claim, however minor or off the apparent topic.
  Choosing what to use is the writing stage's job.

## Background entries

For textbook facts a reader needs and the inputs use without supporting (what the 16S rRNA gene is). They do
not need a research run; they get a lighter check.

```markdown
- **genome16s.bg1** The 16S rRNA gene encodes the RNA of the small ribosomal subunit and is present in all bacteria and archaea.
  kind: background · ref: woeseBacterialEvolution1987 · check: DOI resolves on Crossref; stated in the abstract
```

- Inside the concept it serves; ID `<concept>.bg<n>`.
- One standard reference: a textbook, a review, or the defining paper. Its BibTeX `note` includes `background`.
- `check`: how it was checked (the DOI or URL resolves, and where in the reference the statement is).
- Only for facts that are not in dispute. Anything the piece would argue for, or that the field contests, is a
  gap for research, not background.

## Do not say

```markdown
- **x.3** "Extraction is the largest source of bias, then PCR, then sequencing."
  why: one 7-taxon dataset (Brooks 2015 reanalysed by McLaren 2019); Fouhy 2016 found two extraction methods very similar; MBQC put specimen type first · instead: bias.2 · trail: MB-01 §critic · from: MB-01:C-045
```

Statements that are wrong or overstated as phrased: the review's uncorrected wording where the critic corrected
it; a single-source claim phrased as a property of the field; pooled figures; merged cases; the reviewer's
reading presented as a finding; misconceptions the note names. `instead`: the entries to use, or `none`.
A dispute in the field is not a do-not-say entry: "whether to rarefy is disputed" is a claim (`conf: cont`),
and its one-sided versions are the do-not-say entries.

## Gaps

```markdown
- **gap.2** Reads per sample within a run, and their relation to sample load.
  blocks: depth · origin: critic coverage gap; two primary studies known only through Schloss 2024b · from: MB-01:C-071
```

What the research did not establish and a later stage may need: critic coverage gaps, "not found" and
"unsearched" results, sources not obtained that matter, a concept with no claim behind it, an uncritiqued note's
load-bearing figures. `blocks`: the concepts or entries waiting on it. These go back to research; consolidation
never fills them.

## Out of scope

```markdown
- MB-01:C-030..034: reference corrections, applied in Sources
- MB-02:A-151, MB-02:A-152: access basis of the answers (provenance, kept in the result note)
```

Inventory items that are not findings, each range with its reason.

## Sources

One fenced `bibtex` block: every source cited by an entry, and the sources not obtained.

- Transcribe the references the notes give into BibTeX. Never look a reference up: missing fields stay missing
  and the `note` says `incomplete: <fields>`. Apply the critic's reference corrections.
- Citekey: `auth.lower + shorttitle(3,3) + year` (the vault's `PhD/Proposal/Refs/Citation Key Format.md`):
  `loucaDecouplingFunctionTaxonomy2016`. The same source in two notes is one entry.
- `note = {access: full_text (MB-01), abstract_only (MB-02); type: peer reviewed; cited as: MB-02 [3]}`;
  `access: not_obtained` for those; `background` for background references.
