# The knowledge note: format

One markdown note per research set, in a `Knowledge` folder beside the `Results` folder (same case as its
sibling: `knowledge` beside `results`). Fixed line grammar so `kn.py lint` can check it and write
`<note>.index.json` for scripts. Fields inside an entry are separated by ` · ` (space, middle dot, space).

## Frontmatter

```yaml
---
type: knowledge
title: 16S amplicon sequencing from sample to count table
inputs:
  - MB-01: Topics/Biology/Research/Results/From sample to count table ... A literature review.md
  - MB-02: Topics/Biology/Research/Results/16S rRNA gene copies per genome ... A literature review.md
refs: PhD/Proposal/Refs/Refs.bib
built: 2026-10-21
status: draft
tags:
  - research
  - knowledge
---
```

- `inputs`: one `ID: path` per result note, the path relative to the vault root. The ID is the brief ID the note
  names (MB-01); `kn.py detect` proposes one when it finds none.
- `refs` (optional): an existing bibliography. A source whose DOI is in it keeps its key there.

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

## The inventory

`kn.py detect --inventory` lists two kinds of item for each input:

- **Required** (the omission check): critique items `C-nnn`; answer sentences `A-nnn`; and, when the note labels
  its citations, every labelled sentence `I-nnnn`. A bullet whose only label ends it is one item: the label
  covers the bullet. Each must appear in some entry's `from`, or in Out of scope. A sentence repeated word for
  word is required once.
- **Body addresses** `B-nnnn`: every other sentence of the note, callouts included (the references and the
  critique are not), each occurrence its own address, so a repeated line can be cited where it stands. Not
  required, but they are how an entry built from the body says where it came from.

## Concepts

```markdown
### copy-number: 16S rRNA gene copies per genome
needs: genome16s
- **copy-number.1** Bacterial genomes carry 1 to 15 copies of the 16S rRNA gene and archaeal genomes 1 to 4.
  conf: not stated · class: meas (note: "measured from genomes") · holds: sequenced genomes in rrnDB (2015 release); the critic: consistent across sources, but the sources draw on overlapping NCBI genome sets, so not independent replications · src: stoddardRrnDBImprovedTools2015 (FT), vetrovskyVariability16SRRNA2013 (FT) · trail: MB-02 §D1.1, §D1.2 · from: MB-02:A-002, MB-02:C-006

(Not `repl`: the note says "consistent across sources", and its critic says the sources are not independent. When
the words and the critic pull apart, the critic wins; when the critic gives no value from the table, `not stated`.)
```

- **A concept** is a thing the claims are about: a quantity, a step, a term, a method. ID: lower case, hyphens.
  Take them from the terms and headings the notes use, one per thing a claim is about. A concept may have no claims
  yet, when a gap blocks it, or only a background entry.
- **`needs:`** the concepts a reader must already have to understand this concept's claims (`needs: none` for
  a root). The graph is the artefact. Where concepts need each other (copy number and relative abundance;
  compositionality and rarefying), give each the same `group: <name>` line and keep them next to each other.
  A group is only for concepts that need each other; lint checks both ways. Put a claim in the concept it is
  about; whether two concepts need each other follows from what they are, not from where a claim was put.
- **File order:** any order in which every concept comes after what it needs (members of a group together).

## Claims

`- **<concept>.<n>** <statement>` then one indented line of fields.

| Field | What goes in it |
|---|---|
| `conf` | the standing the note gives this claim: `repl`, `single`, `cont`, `unclear`, `mixed` (labelled sources disagree), or `not stated`, with its basis in brackets |
| `class` | `meas`, `deriv`, `model`, `assert` (two joined by `/`), `reading` (the reviewer's own reading or inference, said to be so), `search` (a statement about what the review's search found or did not find), or `not stated`; with its basis |
| `holds` | the setting it comes from (system, measurement, scale, n, range) and what it was not shown for, in the note's terms |
| `src` | citekeys from Sources, comma-separated, each optionally followed by the note's labels for it in brackets: `mclarenConsistentCorrectableBias2019 (FT; single)`, `(AB; INDIRECT)`. Where the critic corrected a label, the corrected one, marked: `(AB; meas; single; critic: MB-01:C-019 was "FT; meas; repl")`. `none (<reason>)` when the note cites nothing for it: `none (the reviewer's synthesis)` |
| `trail` | where the note verified it: `<ID> §<start of a heading or callout title>`, more after commas (`MB-01 §2.2, §2.14`); `§critic` and `§answers` reach those blocks |
| `from` | the inventory items it comes from and accounts for: `MB-01:I-0012`, `MB-01:B-0340`, ranges `MB-01:I-0012..0015`, critique items `MB-01:C-004`. Never empty |
| `rating` (optional) | the note's own grade for this claim, in its words and in quotes: `rating: "Moderate"`, `rating: "Confidence: high (3-0)"`, `rating: "well established"` |
| `limit` (optional) | `access`, or `access and evidence`, with its basis: the note says the claim's standing or verification is limited because a source was not accessed (abstract only, not obtained, known only second-hand or "not read in the original", a figure not confirmable from the text read). Only when the note gives that reason |

All but `rating` and `limit` are required, and none may be empty.

**Basis** for `conf`, `class` and `limit` (required unless `not stated`):
- `(marker)`: read from the citation labels (`[FT; meas; repl]`) of a note with labelled citations.
- `(critic: C-012)`: the critic's finding about this claim; it overrides the marker and the review. With more than
  one input, give the ID: `(critic: MB-01:C-012)`.
- `(note: "exact words")`: the note says it in words about this claim.
- `(inputs: MB-01 repl, MB-02 single)`, with `mixed`: two inputs give the same claim different standings.

**Everything quoted sits in the entry's own text.** A quoted basis, a `rating`, and a label's `was "..."` must be
words from the items in the entry's `from` (or the critique items it names), because that is all the checker
sees. If the words are in a neighbouring sentence, add that sentence to `from`. The same goes for `holds`: the
setting comes from the cited sentences, or the sentence it comes from is cited. Lint checks the quotes; the
checker checks `holds`.

A label covers the sentence it is in, not its neighbours: another sentence about the same source has its own
label or none. The exception is a bullet whose only label ends it: the label covers the bullet, and detection
makes the bullet one item. `src` shows a source's labels as the critic left them: where the critic corrects a
source's access, class or standing as cited for this claim, `src` gives the corrected label, then
`critic: <item>` and the note's original label as `was "..."`. Where the critic corrects the claim and not the
source's label, the label stays and `conf` carries the correction. The same finding in two inputs is one claim
with both trails and both `from` items.

**Which words count.** A standing is stated only by words like these, said of this claim:

| conf | The note says |
|---|---|
| `repl` | replicated, consistent across independent studies, converge, several independent |
| `single` | single source, single study, one study, one dataset, only test, one laboratory |
| `cont` | contested, disputed, conflicting, disagree, contradicted by |
| `unclear` | unclear, unsettled, poorly constrained, cannot tell, unknown |

Grades on another scale ("Moderate", "Weak", "well established", "Confidence: high (3-0)", "ESTABLISHED BUT
QUALIFIED") are not a standing: copy them into `rating` and leave `conf` as the table allows.

**Never infer a standing.** If the note gives none for a claim, write `not stated`, even when the prose sounds
confident or names several studies. Counting studies, judging a journal or reading tone is re-rating.

**Class.** A benchmark on simulated data is `model`; one on measured data, mock communities included, is `meas`.
A method the note describes ("by construction", "a Monte Carlo study") is a basis when quoted.

**Statements:**
- One finding per claim, in the form the evidence supports: where the critic corrected or narrowed a claim, the
  claim is the corrected version, and the uncorrected one goes to Do not say.
- Figures keep their own definition and denominator. Don't combine figures from different sources yourself. A
  range or total the note itself gives is the note's claim: keep it as a claim, with `holds` naming the sources
  it spans, beside the claims for each source.
- Words and facts come from the note. No examples, explanations or numbers that are not in it.
- A "not found" can be a claim (`class: search`, the routes in `holds`) as well as a gap.
- Access and directness (`INDIRECT`, abstract only, "single-pass extraction") go with the source in `src`, in the
  note's own words.
- **Not accessed is not weak.** "Not confirmable, the source was not accessed" is a different finding from "not
  supported". Where the note or its critic says a claim was downgraded, left unverified or called unsupported
  because of access, keep that reason: `limit: access (critic: C-020)`, and in a do-not-say entry's `why`. Where
  it gives both reasons, `limit: access and evidence`. Where it gives no reason, write nothing: never infer that
  a weak claim is weak because of access.
- Don't trim: every finding the note reports becomes a claim, whether it is in the answers or only in the body,
  however minor or off the apparent topic. Choosing what to use is the writing stage's job.

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
- **dns.3** "Extraction is the largest source of bias, then PCR, then sequencing."
  why: one 7-taxon dataset (Brooks 2015 reanalysed by McLaren 2019); Fouhy 2016 found two extraction methods very similar; MBQC put specimen type first · instead: bias.2 · trail: MB-01 §critic · from: MB-01:C-045
```

IDs `dns.<n>`. Wordings that the inputs themselves say are wrong or overstated, and nothing else:
- the review's wording where the critic corrected it (single-source claims phrased as the field's, pooled
  figures, merged cases, the reviewer's reading presented as a finding);
- claims the note reports as refuted or killed in verification;
- misconceptions or wordings the note itself warns against.

`from` points to the item that says so. Without such an item there is no do-not-say entry: judging a claim
overstated yourself is re-rating. Where a note contradicts itself (a verdict and its body disagree), that is a
gap, quoting both. `instead`: the entries to use, or `none`. A dispute in the field is not a do-not-say entry:
"whether to rarefy is disputed" is a claim (`conf: cont`), and its one-sided versions are the do-not-say entries.

## Gaps

```markdown
- **gap.2** Reads per sample within a run, and their relation to sample load.
  blocks: depth · origin: critic coverage gap; two primary studies known only through Schloss 2024b · from: MB-01:C-071
```

IDs `gap.<n>`. What the research did not establish and a later stage may need: critic coverage gaps, "not found"
and "unsearched" results, sources not obtained that matter, a concept with no claim behind it, a note that
contradicts itself, a follow-up the note's stage-2 check called for. A gap may cite the sources it names in
`src`. A note with no critique gets one gap naming
the figures its answers rest on: they were never checked by a second reader. `blocks`: the concepts or entries
waiting on it. These go back to research; consolidation never fills them.

## Out of scope

```markdown
- MB-01:C-030..034: reference corrections, applied in Sources
- MB-02:A-151, MB-02:A-152: access basis of the answers (provenance, kept in the result note)
- AB-01:A-016: the review's choice among the brief's options (routing, not a finding)
```

Required inventory items that are not findings, each range with its reason: provenance, search records, routing,
corrections applied in Sources, an owner's annotation. Body addresses need not be listed here.

## Sources

One fenced `bibtex` block: every source the inputs list, cited or not, and the sources not obtained, so the
block can be collected into the bibliography.

- Transcribe the references the notes give into BibTeX. Never look a reference up (the one exception is a
  background entry's reference): missing fields stay missing and the `note` says `incomplete: <fields>`. Apply the
  critic's reference corrections. A reference that names several works becomes one entry per work.
- Keys: `python3 scripts/kn.py citekey --author "<BibTeX author>" --title "<title>" --year <year> --doi <doi>
  --refs "<vault>/<refs>"`. It returns the key the source already has in `refs`, or the vault's rule
  (`auth.lower + shorttitle(3,3) + year`, as `PhD/Proposal/.hb/websearch/build_bibs.py` applies it). Lint warns
  when a key differs. Add `a`, `b` when two sources would share a key.
- `note = {access: full_text (MB-01), abstract_only (MB-02); type: peer reviewed; cited as: MB-02 [3]}`. Access
  is `full_text`, `abstract_only`, `secondary`, `not_obtained` or `not stated` (the note gives none), followed by
  the note's own words in brackets when it says more ("full_text (single-pass extraction)"). Where the critic
  corrects a source's access, the corrected value, with the critic item: `abstract_only (critic: MB-01:C-020;
  the note said full_text)`. `type` only when the note says it. `not cited` for a source
  the note lists but cites nowhere; `background` for a background reference; a conflict between the note's lists
  (a source both used and "not obtained") is recorded here.
