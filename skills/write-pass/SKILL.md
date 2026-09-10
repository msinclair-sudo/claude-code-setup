---
name: write-pass
description: "Two-pass prose elevation workflow for scientific manuscripts. Runs humanizer → de-densify in sequence on any section of text. Use when the user invokes /write-pass or asks to elevate, polish, deslop, de-AI, or run a writing pass on scientific prose, manuscripts, abstracts, cover letters, grant narratives, or discussion sections."
allowed-tools: [Read, Write, Edit]
---

# Write-Pass: Scientific Prose Elevation

A sequential two-pass workflow that elevates already-drafted scientific prose to publication grade. It does not draft, it does not add new content or claims. It operates on text you give it.

**Pass order is fixed. Do not skip or reorder.**

---

## When to use

Invoke with `/write-pass` followed by the text to elevate, or paste the text and ask for a writing pass. Apply to any section of a scientific manuscript.

---

## The two passes

### Pass 1 — Humanize (AI-tell removal + voice)

Load the `humanizer` skill and follow it. This pass cuts; it does not add. Tell it this is **embedded mode**: it should return only the final text, since Pass 2 consumes the output rather than the user.

The patterns are ordered strongest first. Sections 1 to 5 justify an edit on a single sighting; anything marked *weak alone* needs corroborating tells in the same passage before you act on it. That gating matters here, because scientific prose legitimately contains hedges, passives, and hyphenated compounds that are not AI tells.

**Act on one sighting (§1–§5):** not-X-but-Y contrasts, one-line closers and dramatic fragments, sayings that sound deep ("at its core," "what really matters"), staged run-ups ("Let's dive in"), and arguing with no one.

**Structural and inflation tells (§6–§18):** forced triads, repeated sentence openings, dashes as the universal connector, stacked qualifiers, hyphenated pairs, hidden actors, synonym cycling (§11a), false ranges (§11b), AI vocabulary, inflated significance, vague connection, shallow -ing riders, sales language, borrowed authority, and copula avoidance ("serves as," "stands as").

**Formatting and leftovers (§19–§25):** decorative bold, decorative headings, curly quotes, chatbot residue, knowledge-limit disclaimers, headings restated in the first sentence, and writing about the previous version.

**Hard constraints for this pass:**
- No em or en dashes in the output.
- Add no fact, name, number, date, quote, or citation that is not in the source. If a sentence needs a detail you do not have, ask rather than invent. This is non-negotiable in a manuscript.
- Check that the rewrite did not drop a claim, a ranking, or a simultaneity claim. Shape edits under §6, §9, and §19 lose those most often.

**Cold re-read (mandatory — do not skip):**
Tells survive rewrites. Reading your own fresh output, you are anchored on the choices you just made and will read past them. This step is the independent second look that catches what the first reading missed, so treat it as real work rather than a checklist tick.

Set the draft aside and re-read it cold, as if you had not written it. Ask: "What still sounds AI-generated?" Answer in 2–3 bullet points, revise to address them, then search specifically for the five tells that most often survive a rewrite: a not-X-but-Y contrast, a one-line closer, a dash, a triad, a bold label.

**Score before handing off (1–10 each):**

| Dimension | Question |
|-----------|----------|
| Directness | Statements or announcements? |
| Rhythm | Varied or metronomic? |
| Trust | Respects reader intelligence? |
| Authenticity | Sounds like a specific human wrote it? |
| Density | Anything cuttable? |

Below 35/50: revise this pass before proceeding. **Carry the Density score forward** — Pass 2 gates on it and must not expand prose that already passes.

**Voice calibration (optional):** If the user provides a sample of their own writing, analyse sentence length patterns, word choice level, paragraph openings, and punctuation habits before rewriting. Match their voice, not a generic "clean" voice.

**For scientific prose specifically:** Neutral and plain is the correct register. Do not inject first-person opinions or casual asides unless the section (e.g., a cover letter or blog post) calls for it. Maintain appropriate formality.

---

### Pass 2 — De-densify (structural density)

Run after Pass 1. This pass splits and restructures; it does not add padding or restatements.

**Gate:** The Density score asks whether anything is *cuttable*; this pass fixes prose that is *hard to parse*. Those are different faults, and a passing Density score does not by itself mean this pass is unnecessary. Run it only when a listed trigger is actually present, and apply only the operations those triggers fire. If nothing triggers, skip the pass and say so.

**Section-level scan first:** Before sentence-level work, check whether the section has 3+ consecutive study paragraphs (evidence parade) or 3+ major sections following the same arc. If yes, apply Operations 6 and 7 first.

**Operations (apply only those triggered):**

**Op 1 — Split multi-fact sentences**
When a sentence contains 3+ distinct facts, numbers, or technical terms, distribute across separate sentences. Lead with the overall pattern; follow with evidence in order of interpretive interest.

**Op 2 — Unpack inline definitions**
When a technical term is defined inside a parenthetical, extract the definition into its own sentence.

**Op 3 — Add signposting sentences**
When the logical relationship between consecutive sentences is implicit, add a connective sentence. Types: code glosses ("In other words"), frame markers ("The first property is..."), transition signals ("The distinction matters because..."). These carry no new data.

**Op 4 — Expand parenthetical asides**
If a parenthetical aside exceeds 5 words and contains information the reader needs, extract it into its own sentence(s). Short parentheticals (cluster IDs, p-values, single citations) stay inline.

**Op 5 — Unpack enumerations**
When a sentence lists 4+ technical terms or mechanisms: group by principle (2 categories × 2 items), lead with the count then the list, or distribute at 2 new terms per sentence. Exemption: gene name catalogues meant for scanning can stay compressed.

**Op 6 — Synthesis anchors** *(evidence parades only)*
After every 2–3 consecutive study-summary paragraphs, insert a synthesis anchor: a paragraph that names the accumulating pattern, explains why it matters, and orients the reader toward what comes next. It introduces no new evidence. A synthesis anchor answers: "What do these studies together show that no individual study shows?"

**Op 7 — Arc-break paragraphs** *(multi-section documents only)*
At each transition between major sections following the same arc, insert a paragraph that names what *changes* in the upcoming section — not a summary of the section just finished.

**Op 8 — Batch cross-references**
If a paragraph has 3+ inline section references, keep the one the reader needs and consolidate the rest into a terminal note.

**Paragraph constraint:** No inserted content may be left as a 1–2 sentence orphan paragraph. Fold it into an adjacent paragraph or expand to 3+ sentences.

**Stop condition:** Stop when a reader in the same broad field can read each paragraph once and extract the main point. Do not expand prose that doesn't need it; an untriggered operation is not an improvement.

---

## Workflow summary

```
Input: draft section of scientific prose

Pass 1 — Humanize
  → Apply humanizer in embedded mode (strongest-first, weak-alone gating)
  → Cold re-read: "what's still AI here?" Revise.
  → Score (1–10) on Directness, Rhythm, Trust, Authenticity, Density
  → Must reach ≥35/50 before proceeding; carry Density forward

Pass 2 — De-densify
  → Skip unless a listed trigger is present
  → Section scan first (evidence parades, arc repetition)
  → Apply only triggered operations
  → Stop when one-read comprehension is achieved

Output: elevated prose, ready for submission
```

---

## What this workflow does NOT do

- It does not draft. Give it finished prose.
- It does not add new findings, interpretations, or citations.
- It does not pad. Every structural change must serve comprehension.
- It does not introduce em dashes at any pass.
