---
name: md-docx
description: "Convert Markdown to Word .docx and back using Pandoc, preserving Obsidian callouts across the round trip and matching APA in-text citations to BibTeX keys. Use when the user wants to turn a Markdown note into a styled Word document for external review, bring a reviewed .docx back into Markdown, or invokes /md-docx. Requires pandoc."
allowed-tools: [Bash, Read, Edit]
---

# md-docx: Markdown ⇄ Word conversion

A Pandoc pipeline that moves documents between Markdown and Word `.docx` for
external review and back. It styles the `.docx` from a Word template, preserves
Obsidian callouts through the round trip, and rewrites APA citations to Pandoc
`[@citekey]` form against a `.bib` file.

**Requires `pandoc` on PATH.** Citation matching also needs a BibTeX file.

## Files

| File | Role |
| --- | --- |
| `convert.sh` | **md → docx.** Pandoc + `defaults.yaml` + `reference.docx` styling. Normalises callouts so they survive the round trip. |
| `docx2md.sh` | **docx → md.** Pandoc to Obsidian-flavoured Markdown, plus media extraction, wikilink rewriting, callout reconstruction, and APA→Pandoc citation matching. |
| `apa2pandoc.py` | Citation matcher used by `docx2md.sh`. Rewrites APA in-text and Zotero hyperlink cites to `[@citekey]` against a `.bib`; strips the rendered reference list. |
| `defaults.yaml` | Pandoc defaults for `convert.sh` (input extensions, `citeproc`, `lang`). `reference-doc` and `csl` are passed on the command line from the skill dir, so the file is location-independent. |
| `reference.docx` | Word style template — heading/body/blockquote styles for the `.docx` output. |
| `apa.csl` | Bundled APA 7th-edition citation style. `convert.sh` uses it by default; override with `--csl /path/to/style.csl`. |
| `sectionbreak.lua` | Pandoc filter used by `convert.sh`. Turns a Markdown thematic break (`---`) into a Word "next page" section break, carrying the template's page geometry. |

## Usage

```bash
SKILL=~/.claude/skills/md-docx

# Markdown -> Word (for sending out)
"$SKILL/convert.sh" input.md                          # -> input.docx (APA 7th citations)
"$SKILL/convert.sh" input.md custom_name.docx
"$SKILL/convert.sh" input.md --csl /path/to/style.csl # use a different citation style

# Word -> Markdown (bringing a reviewed doc back in)
"$SKILL/docx2md.sh" reviewed.docx                          # -> reviewed.md (no citation matching)
"$SKILL/docx2md.sh" reviewed.docx out.md
"$SKILL/docx2md.sh" reviewed.docx --bib /path/to/Refs.bib  # match APA cites against your .bib
```

The skill is self-contained and runs from any directory: `reference.docx`,
`apa.csl`, and `defaults.yaml` are all resolved from the skill folder. Citations
default to the bundled **APA 7th edition** style (`apa.csl`) — a document's
frontmatter `csl:` is overridden by this default, so a stale path like
`.pandoc/apa.csl` no longer matters. Per-document `bibliography`/`toc` overrides
still go in the Markdown frontmatter.

## Citation matching

```bash
"$SKILL/apa2pandoc.py" /path/to/Refs.bib < in.md > out.md   # report on stderr
```

Resolves cites by accent-folded first-author surname + year against the `.bib`.
Handles plain APA (`(Averill et al., 2021)`, narrative, multi-cite), Zotero
hyperlink cites, and name-prefix mismatches. Unmatched cites are left in place
wrapped in `<!-- UNMATCHED: … -->` and listed on stderr — nothing is guessed or
silently dropped.

> [!note] BibTeX path
> `docx2md.sh` does **not** assume any default `.bib` location. Point it at your
> own reference file with `--bib /path/to/Refs.bib` (or set the `BIB` env var).
> Without one, citation matching is skipped and APA cites are left untouched.
> You can also call `apa2pandoc.py` directly with your own `.bib`.

## Notes and limitations

- **Callouts** survive the round trip via a cooperating convention between the
  two scripts (a protective blank `>` line and literal `[!type]` markers). See
  `README.md` for the full contract.
- **`---` becomes a Word section break** (next page) on md→docx via
  `sectionbreak.lua`. Pandoc's parser already tells a real thematic break apart
  from YAML frontmatter and setext heading underlines, so only standalone `---`
  lines are converted. The break is **not** recovered as `---` on docx→md —
  Pandoc's reader discards Word section breaks — so re-graft them from the prior
  `.md` if you round-trip.
- **Frontmatter and the document title are lost** on docx→md (Pandoc cannot
  recover the YAML block or a Word title style). Re-graft the header from the
  previous `.md`.
- **Callouts stitched in after conversion** live only in the Markdown and are
  lost if you re-run `docx2md.sh` on the same `.docx`. Diff against the prior
  `.md` before overwriting.

See `README.md` in this directory for the detailed reference (callout round-trip
contract, full citation-matching rules, and the `docx2md.sh` pipeline order).
