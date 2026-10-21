---
name: consolidate
description: Turn research result notes (literature reviews with references, and any critique of them) into one knowledge note per research set - claims organised by concept with their standing, conditions, sources and trail back to the verification, plus a do-not-say list, gaps for research and BibTeX sources - so a writer never has to dig through verification trails. Use when the user invokes /consolidate, or asks to consolidate, distil or prepare research results for writing. Works on any result note in the vault, whatever its citation style; no new searching or re-verification.
---

# consolidate: research results into a knowledge note

The research workflow verifies; this step makes its output usable. It reads result notes as they are and writes
one knowledge note per research set. The writer reads the knowledge note and never the result notes. Nothing is
searched and nothing is verified again: where the research is missing or weak, that becomes a gap for research.

**Why it exists:** a writer using MB-01 and MB-02 (2026-10-20) had to read each claim in three versions (body,
answers, critic's reformulation; only the last was right), apply 28 critic corrections by hand because the
critic corrects beside the body and never in it, and gather one concept from five places in two notes.

## Input

Any result note with a review body and references. Everything else is detected, not required:

| Detected | Effect |
|---|---|
| a critique | applied: its corrections win over the body and the answers |
| labelled citations (an access label with a standing: `[FT; meas; repl]`, research-brief rule 3a, or `[Key; FT; measured; SINGLE SOURCE]`) | `conf` and `class` read from the labels; exact omission check over every labelled sentence, the answers and the critique |
| no labels | claims read as written; `conf: not stated` wherever the note gives no standing in words; omission check falls back to the answers plus the critique |
| a section of refuted claims | read as critique: its items become do-not-say entries |
| a `run.json` sidecar | reported; nothing requires it |

`kn.py detect` reports all of this, and the knowledge note's Inputs table records it.

## Output

`<...>/Knowledge/<topic>.md` beside the `Results` folder (matching its case), and `<topic>.index.json` (written by lint, for
scripts and later fact-checks). Format: `references/format.md`. One note per research set, reused by every piece
written from it. It covers everything the research found: never trim.

## Procedure

1. **Detect.** For each input: `python3 scripts/kn.py detect "<note>" --id <ID> --inventory <tmp>/<ID>.md`. The
   inventory lists the required items (every one must be accounted for) and gives every other sentence of the
   note an address, so that every entry can say where it came from.
2. **Read** each note whole, the critique first, then the answers, then the body.
3. **Sources.** Transcribe the references into one BibTeX block (`format.md`, Sources); never look one up. Make
   each key with `kn.py citekey`, giving `--refs` the vault's bibliography so sources already in it keep their key.
4. **Concepts and claims.** Name the concepts; give each its `needs`; write a claim for every finding, in the
   corrected form where the critic corrected it, with every field filled. Group concepts that need each other.
5. **Do not say, gaps, out of scope.** Wordings the inputs say are wrong; what research must still answer;
   required items that are not findings, with reasons.
6. **Background** (optional): for a concept the claims rely on that no input defines, add a background entry with
   one standard reference and its check. This is the only step that may use the web: to find and check that
   one reference, and nothing else.
7. **Lint** until clean: `python3 scripts/kn.py lint "<knowledge note>"`. It checks the fields, the sources, the
   trails, the `needs` graph and groups, the quoted bases, the Inputs table against detection, and omission
   (every inventory item accounted for).
8. **Faithfulness check.** `python3 scripts/kn.py packets "<knowledge note>" <tmp>/packets`, then one fresh agent
   per packet with `references/checker.md`. Fix every fault and lint again. Then a fresh agent that made none of
   the fixes re-checks the fixed entries: `kn.py packets "<knowledge note>" <tmp>/recheck --only <ids>`. Repeat
   until the re-check finds nothing; never grade your own corrections.

Each check the inputs allow is run, and the Inputs table says which ran.

## Hard rules

- **Never infer a standing.** `conf` comes from a label, the critic or the note's own words, quoted; otherwise
  `not stated`. Quote only words from the sentences the entry cites in `from`.
- **Not accessed is not weak.** Where the note says a claim is limited because a source was not accessed, keep
  that reason (`limit: access`); where it does not say, add nothing.
- **The critic wins.** Its corrections become the claims; the wording it corrected goes to Do not say.
- **Only the inputs say what not to say.** A do-not-say entry rests on the critic, a refutation or the note's own
  warning. Without a critic, overstatements you notice are not yours to flag: the note gets a gap saying it was
  never checked by a second reader.
- **Nothing new.** No searching (except one reference per background entry), no re-verification, no facts or
  figures that are not in the inputs, no combining figures from different sources (a range the note itself gives
  stays, as the note's claim).
- **No writing guidance.** No story, order of telling, emphasis, audience or style. The concept order is one
  valid ordering of the `needs` graph and means nothing more.
- **Gaps go back to research.** A missing or weak finding is a gap, never filled here.
- **Keep the result notes as they are.** The knowledge note links to them; it never edits them.
