# Stage A: lint rules and scoring, fixed before any scoring (2026-10-22)

Change 1 of `../plan.md` (revision 2, approved). These definitions, the lists beside this file and
`score_lint.py` are committed before the first scoring run. After it, only mechanical bugs (parsing, paths) may
be fixed, each recorded in `results.md` with its numbers before and after. Rules, lists and thresholds are not
tuned.

## Inputs

- **The notes:** the 14 notes as built under v3, before any fix: `../../v3/as-built/` (16S, H2-01, TSL, CB1,
  CB2, NFERT) and `../../heldout/as-built/` (H2-04, H1-05, H1-02, H1-06, GHOST, CB3, TAXRES, H1-RES).
- **The inventories:** rebuilt with kn.py's `detect()` (the v3 code, unchanged) from the result notes named in
  each note's frontmatter, under the vault root
  `/mnt/a/Obsidian Vault/Michael.md`.
- **Ground truth:** the first-pass checker verdicts only:
  - `../../v3/verdicts/`: MB-packets-01-04 and 05-08 (16S), H2-01, TSL, CB1-LIMING, CB2-RRNA, NFERT;
  - `../../heldout/verdicts/<ID>.md`.

  A verdict line is `<id>: ok` or `<id>: <kind>[, <kind>]: <reason>`.
- **Entries scored:** claims and do-not-say entries, the ones the checker judged.

**The cited text** of an entry is the text of every inventory item in its `from` field, plus every critique item it
names in `conf`, `class`, `limit` or `src`: what the checker saw (kn.py `entry_refs`).

## Normalisation (both rules)

- Curly quotes become straight quotes; unicode dashes and minus signs become `-`; `*` and backticks are removed.
- Thousands separators are removed (`1,304` → `1304`). A possessive `'s` is removed.
- Text is lower-cased for matching.
- **Words** are runs of letters and digits, keeping inner `.`, `-` and `'` (`16s`, `r2`, `0.77`, `taxonomy-inferred`).
- **Stemming:** for word matching, a final `ing`, `ed`, `es` or `s` is stripped when at least three letters remain.
  The same stripping is applied to the cited text.
- **Hyphenated compounds:** a compound is found if the compound is in the cited text, or every part of it is.

## R1: numbers and names

**Tokens** taken from an entry's statement, and from a do-not-say entry's `why`:
- **Numbers:** digits with optional decimal part, separators and `%` (`0.77`, `9.3%`). A range (`1-15`,
  `81-86%`) gives one token per end.
- **`[n]` markers:** each number inside square brackets that hold only numbers, commas, spaces and dashes; a range
  is expanded (`[28-31]` → 28, 29, 30, 31).
- **Capitalised words** that do not start a sentence (not the first word, nor the first after `. `, `! `, `? ` or
  an opening quote or bracket at the start), minus `capitalised-common.txt`. All-caps acronyms count as
  capitalised words.
- **Quoted phrases:** text inside double quotes, three or more characters.

**A token is satisfied when:**
- **a number** occurs as a number in the cited text. A numeral 0 to 20 is also satisfied by its English word
  ("seven" for 7), because notes write small numbers both ways.
- **a `[n]` marker** occurs inside a bracket marker in the cited text, ranges expanded.
- **a capitalised word** occurs as a word in the cited text (case-insensitive, stemmed), or equals a surname, or a
  word of a surname, of an author of a source in the entry's `src`. Authors are taken from the note's BibTeX block
  with kn.py's `parse_bib`, `surname` and `fold`.
- **a year** (a number from 1800 to 2099) is satisfied as a number, or by the `year` of a source in `src`.
- **a quoted phrase** is a substring of the normalised cited text.

**R1 flags** an entry with at least one unsatisfied token.

## R2: the `holds` word rule (three variants)

Over the words of the `holds` field, normalised as above. An entry with no `holds` (do-not-say entries) is never
flagged.
- **R2-full:** every word except those in `connectives.txt`.
- **R2-content:** every word except those in `stopwords.txt`, which contains `connectives.txt`.
- **R2-setting:** only setting-type terms: capitalised tokens (in the original case, at any position), numbers,
  tokens containing a digit or a hyphen, and words in `setting-lexicon.txt` (stemmed).

A word is satisfied when its stem occurs among the stemmed words of the cited text, or, for a compound, the
compound or all its parts occur. **R2 flags** an entry with at least one unsatisfied word.

## Scoring

For each rule and variant, against the first-pass verdicts:

| | R1 | R2 (each variant) |
|---|---|---|
| Faults it is scored against | `absent` and `numbers` | `holds` |
| True positive | flagged, and the checker gave one of those kinds | flagged, and the checker gave `holds` |
| False negative | the checker gave one of those kinds; not flagged | the checker gave `holds`; not flagged |
| False positive | flagged, and the checker passed the entry (`ok`) | the same, with CB3 left out |
| Reported apart | flagged, and the checker faulted it for another kind | the same |

- **Catch rate** = true positives / (true positives + false negatives).
- **False-positive rate** = false positives / entries the checker passed. All 14 notes for R1. For R2, all but
  CB3, whose checker passed added settings that the other checkers faulted (heldout/results.md). CB3's R2 numbers
  are reported separately.

## Thresholds and the decision rule (copied from plan.md, unchanged)

| Rule | Adopted if the catch rate is at least | and the false-positive rate at most |
|---|---|---|
| R1 | 40% | 3% |
| R2 (each variant) | 60% | 5% |

- R1 is adopted if it passes.
- Of the R2 variants that pass both thresholds, the one with the highest catch rate is adopted (a tie goes to the
  one that flags fewer entries).
- If none passes, the fallbacks are R2-content, then R2-setting, then dropping R2. If R2 is dropped, R1 alone is
  kept and `holds` is left to the checker under change 5.
- A missed threshold is reported with its numbers; the owner decides at gate A.

## The false-positive sample (information only; does not affect adoption)

- **The sample:** with seed 20261023, `random.Random(seed).sample` draws up to 30 of R1's false positives and up
  to 30 of R2-full's. Each R2 entry is tagged with the variants that also flag it.
- **Packets:** one per family. Each entry shows its fields, its cited text and the tokens the lint could not find.
- **The judges:** one fresh read-only agent per family, using change 5's checker wording, classifies each entry
  as a lint error (the entry is faithful; the lint is wrong), a checker miss (the entry adds something its text
  does not say), or unclear.
- **Output:** `fp-sample.md`.
