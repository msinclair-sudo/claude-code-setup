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
| `defaults.yaml` | Pandoc defaults for `convert.sh` (input extensions, `reference-doc`, `citeproc`, `lang`). |
| `reference.docx` | Word style template — heading/body/blockquote styles for the `.docx` output. |

## Usage

```bash
SKILL=~/.claude/skills/md-docx

# Markdown -> Word (for sending out)
"$SKILL/convert.sh" input.md                 # -> input.docx
"$SKILL/convert.sh" input.md custom_name.docx

# Word -> Markdown (bringing a reviewed doc back in)
"$SKILL/docx2md.sh" reviewed.docx            # -> reviewed.md
"$SKILL/docx2md.sh" reviewed.docx out.md
```

Per-document overrides (`bibliography`, `csl`, `toc`, …) go in the Markdown
file's YAML frontmatter, not in these scripts.

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
> `docx2md.sh` defaults its `.bib` path to a project-specific location near the
> top of the script. Edit that line, or call `apa2pandoc.py` directly with your
> own `.bib`, when using this outside that project.

## Notes and limitations

- **Callouts** survive the round trip via a cooperating convention between the
  two scripts (a protective blank `>` line and literal `[!type]` markers). See
  `README.md` for the full contract.
- **Frontmatter and the document title are lost** on docx→md (Pandoc cannot
  recover the YAML block or a Word title style). Re-graft the header from the
  previous `.md`.
- **Callouts stitched in after conversion** live only in the Markdown and are
  lost if you re-run `docx2md.sh` on the same `.docx`. Diff against the prior
  `.md` before overwriting.

See `README.md` in this directory for the detailed reference (callout round-trip
contract, full citation-matching rules, and the `docx2md.sh` pipeline order).
