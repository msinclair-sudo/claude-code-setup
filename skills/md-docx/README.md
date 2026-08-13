---
created: 2026-06-09
tags:
  - Scripts
  - PhD
---
# `_style/` — Markdown ⇄ Word conversion

> [!abstract] Note Role
> **Contains**: How the `_style/` conversion scripts work — `convert.sh` (md→docx), `docx2md.sh` (docx→md), `apa2pandoc.py` (citation matcher), and the shared Pandoc config. Usage, the callout round-trip contract, and the citation-matching rules.
> **Cannot contain**: Project content or proposal prose; per-document settings (those live in each note's YAML frontmatter).

This directory holds the Pandoc pipeline that moves notes between Obsidian Markdown and Word `.docx` for external review, and brings reviewed `.docx` files back into the vault.

## Files

| File | Role |
| --- | --- |
| `convert.sh` | **md → docx.** Wraps Pandoc with `defaults.yaml` + `reference.docx` styling. Normalises callouts so they survive the round trip. |
| `docx2md.sh` | **docx → md.** Pandoc to Obsidian-flavoured Markdown, plus media extraction, wikilink rewriting, callout reconstruction, and APA→Pandoc citation matching. |
| `apa2pandoc.py` | Citation matcher used by `docx2md.sh`. Rewrites APA in-text cites and Zotero hyperlink cites to `[@citekey]` against a `.bib` you supply; strips the rendered reference list. |
| `defaults.yaml` | Pandoc defaults for `convert.sh` (input extensions, `citeproc`, `lang`). `reference-doc` and `csl` are passed on the command line from the skill dir, keeping the file location-independent. |
| `reference.docx` | Word style template — defines heading/body/blockquote styles for the `.docx` output. |
| `apa.csl` | Bundled APA 7th-edition citation style used by `convert.sh`; override per run with `--csl /path/to/style.csl`. |
| `sectionbreak.lua` | Pandoc filter used by `convert.sh`. Converts a Markdown thematic break (`---`) into a Word "next page" section break, replicating the template's page geometry. |

## Usage

```bash
# Markdown -> Word (for sending out)
_style/convert.sh PhD/Proposal/Proposal.md            # -> Proposal.docx
_style/convert.sh input.md custom_name.docx

# Word -> Markdown (bringing a reviewed doc back in)
_style/docx2md.sh Proposal_reviewed.docx                  # -> Proposal_reviewed.md (no citation matching)
_style/docx2md.sh input.docx out.md
_style/docx2md.sh input.docx --bib PhD/Proposal/Refs/Refs.bib   # match APA cites against your .bib
```

`docx2md.sh` does **not** assume a default `.bib` location: point it at your own
reference file with `--bib /path/to/Refs.bib` (or the `BIB` env var). Without one,
citation matching is skipped and APA cites are left untouched.

`convert.sh` styles citations with the bundled **APA 7th-edition** `apa.csl` by
default (resolved from the skill dir, so it works from any directory). A
document's frontmatter `csl:` is overridden by this default; pass
`--csl /path/to/style.csl` (or set `CSL`) to use a different style.

Per-document overrides (`bibliography`, `csl`, `toc`, …) go in the Markdown file's YAML frontmatter, not in these scripts.

### Section breaks

`convert.sh` runs `sectionbreak.lua`, which turns every standalone Markdown
thematic break (`---`) into a Word **"next page" section break**. Because a
paragraph-level `<w:sectPr>` defines the geometry of the section it *ends*,
`convert.sh` extracts `pgSz`/`pgMar` from the active `reference.docx` and feeds
them to the filter (`MDDOCX_PGSZ`/`MDDOCX_PGMAR`) so every section keeps the
same page size and margins. Pandoc has already separated a real `---` break from
YAML frontmatter and setext heading underlines, so only true breaks convert.

The break is **not** recovered on the way back: Pandoc's docx reader discards
section breaks, so `docx2md.sh` cannot re-emit `---`. Re-graft section breaks
from the prior `.md` if you round-trip.

## What `docx2md.sh` does, in order

1. **Pandoc docx → Markdown** — `--wrap=none`, ATX headings, pipe tables, footnotes, `$math$`. Embedded images are extracted to `<output>.media/`.
2. **Callout reconstruction** — see the contract below.
3. **Wikilinks** — internal `[text](note.md)` links become `[[note]]` (or `[[note|text]]`); web/`mailto:`/`#anchor` links are left alone.
4. **Citation matching** (`apa2pandoc.py`) — see below.

## Callouts: the round-trip contract

Pandoc has no native concept of an Obsidian callout, so the two scripts cooperate to preserve them. There are **two callout forms**, both handled:

- **Block callouts** — `> [!warning] Title` followed by `>` body lines.
- **Inline markers** — `[!callout: Author, year]` sitting in running prose (used in this project to flag a reference for pulling example content into the text).

**Going out (`convert.sh`):** a blank `>` line is inserted between a block callout's title and its body. Pandoc would otherwise glue them onto one line; the blank quote line keeps the title as its own blockquote paragraph in the `.docx`. The `[!type]` marker is left as literal text, which is what lets the return trip identify it.

**Coming back (`docx2md.sh`):** the reconstruction pass
- unescapes inline markers (`\[!callout: …\]` → `[!callout: …]`),
- re-forms block callouts: unescapes the `[!type]` marker, splits a glued title/body back apart, and swallows the protective blank `>` line.

> [!important] Stitched callouts are not in the `.docx`
> Callouts added to a note **after** conversion (e.g. reviewer `> [!warning]` comments migrated in by hand) live only in the Markdown. **Re-running `docx2md.sh` on the same `.docx` will not contain them** — it regenerates from the Word file, which never had them. Re-stitch by hand, or diff against the previous `.md` before overwriting.

## Citation matching (`apa2pandoc.py`)

```bash
apa2pandoc.py PhD/Proposal/Refs/Refs.bib < in.md > out.md   # report on stderr
```

Resolves cites to Pandoc keys against the supplied `.bib` by **accent-folded first-author surname + year** (unique for ~all entries in this project). Handles:

- **Plain APA** — `(Averill et al., 2021)`, narrative `Averill et al. (2021)`, multi-cite `(A, 2019; B, 2020)`, `&`/`and`, compound names (`van`, `de`), accents.
- **Zotero hyperlink cites** — Word/Zotero field cites land as links: `#ref-<citekey>` (key read straight from the anchor) or opaque `#X<hash>` (recovered from the visible surname+year).
- **Name-prefix mismatch** — visible `Tatenhove-Pel` vs bib `van Tatenhove-Pel` resolves by surname suffix when unambiguous.

**Reference list** — the rendered bibliography at the bottom of the `.docx` is **stripped** (the Pandoc render plugin regenerates it from the keys), *except* entries whose in-text cite stayed unmatched, which are kept so they can be fixed by hand.

**Unmatched / ambiguous** — left in place, wrapped in an inline `<!-- UNMATCHED: … -->` comment, and listed in the stderr report. Nothing is silently dropped or guessed. The known irreducible case is an author who has two same-year entries in the bib (e.g. `Perretti 2013a/2013b`) — resolve those manually.

## Known limitations

- **Frontmatter + title are lost** on docx→md (Pandoc cannot recover the YAML block or an H1 that lived in a Word title style). Re-graft the header from the previous `.md`.
- **Stitched-in callouts are lost** on re-conversion (see the callout note above).
- These are accepted trade-offs: the affected cases are rare and caught by diffing against the prior `.md`.
