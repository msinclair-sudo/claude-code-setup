---
name: write-pass
description: "Three-pass prose elevation workflow for scientific manuscripts. Runs deslop → humanizer → de-densify in sequence on any section of text. Use when the user invokes /write-pass or asks to elevate, polish, or run a writing pass on scientific prose."
allowed-tools: [Read, Write, Edit]
---

# Write-Pass: Scientific Prose Elevation

A sequential three-pass workflow that elevates already-drafted scientific prose to publication grade. It does not draft, it does not add new content or claims. It operates on text you give it.

**Pass order is fixed. Do not skip or reorder.**

---

## When to use

Invoke with `/write-pass` followed by the text to elevate, or paste the text and ask for a writing pass. Apply to any section of a scientific manuscript.

---

## The three passes

### Pass 1 — Deslop (AI-tell removal)

Strip AI vocabulary, formulaic structures, and machine-pattern tells. This pass cuts; it does not add.

**Core rules:**
1. Cut filler phrases — throat-clearing openers, emphasis crutches, business jargon, meta-commentary
2. Break formulaic structures — binary contrasts ("Not X. Y."), dramatic fragmentation, self-posed rhetorical questions, anaphora/tricolon abuse
3. Eliminate AI tropes — "quietly," "delve," "serves as," false ranges, superficial participle analyses ("highlighting its importance"), grandiose stakes inflation, invented concept labels
4. Use active voice with named actors — "we" for your own work, specific authors instead of "researchers have shown"
5. Be specific — no vague declaratives, no lazy extremes, no vague attributions. Domain terminology is fine; business buzzwords and AI vocabulary are not
6. Vary rhythm — mix sentence lengths, end paragraphs differently, no em dashes, no stacked short fragments for manufactured emphasis
7. Trust readers — no hand-holding, no "Let's break this down," no fractal summaries
8. Cut formatting tells — no bold-first bullets, no unicode arrows, no em dashes, no "In conclusion...", no "Despite these challenges..." formulas
9. Do not dilute — one point per section, do not restate the same argument repeatedly

**Quick checks before moving to Pass 2:**
- Heavy adverbs or -ly words? Cut.
- Passive voice? Find the actor, make them subject.
- "Not X, it's Y" contrasts? State Y directly.
- Em dash anywhere? Remove — comma, period, or parenthetical instead.
- Vague declarative? Name the specific implication.
- Tricolon? Use two items or one.
- "Despite these challenges..." formula? Rewrite.
- Bold-first bullet pattern? Remove bold leads.

**Score on each dimension (1–10):**

| Dimension | Question |
|-----------|----------|
| Directness | Statements or announcements? |
| Rhythm | Varied or metronomic? |
| Trust | Respects reader intelligence? |
| Authenticity | Sounds like a specific human wrote it? |
| Density | Anything cuttable? |

Below 35/50: revise Pass 1 before proceeding.

**Reference files for Pass 1** (in `~/.claude/skills/deslop/references/`):
- `phrases.md` — phrases to remove or replace
- `structures.md` — structural patterns to avoid
- `tropes.md` — full AI trope catalog
- `examples.md` — before/after transformations

---

### Pass 2 — Humanize (pattern removal + voice)

Run after Pass 1. Catch any remaining AI signals deslop missed, then apply the self-audit.

**30 patterns to check** (grouped):

*Content:* significance inflation, notability name-dropping, superficial -ing analyses, promotional language, vague attributions, formulaic "challenges" sections

*Language:* AI vocabulary words (additionally, crucial, delve, tapestry, vibrant, underscore, showcase, pivotal, landscape, testament, interplay), copula avoidance ("serves as," "stands as"), negative parallelisms, rule of three, synonym cycling, false ranges, passive voice with hidden actor

*Style:* em dashes (hard cut — none in the final text), boldface overuse, inline-header lists, title case headings, emojis, curly quotes, hyphenated word pairs in predicate position, persuasive authority tropes ("at its core," "what really matters"), signposting announcements ("Let's dive in"), fragmented headers, diff-anchored writing

*Communication:* chatbot artifacts ("I hope this helps"), knowledge-cutoff disclaimers, sycophantic tone

*Filler:* filler phrases ("In order to" → "To"), excessive hedging, generic positive conclusions

**Self-audit (do this before delivering Pass 2 output):**
Ask: "What makes this still obviously AI-generated?" Answer in 2–3 bullet points, then revise to address them. The final output must contain no em or en dashes.

**Voice calibration (optional):** If the user provides a sample of their own writing, analyse sentence length patterns, word choice level, paragraph openings, and punctuation habits before rewriting. Match their voice, not a generic "clean" voice.

**For scientific prose specifically:** Neutral and plain is the correct register. Do not inject first-person opinions or casual asides unless the section (e.g., a cover letter or blog post) calls for it. Maintain appropriate formality.

---

### Pass 3 — De-densify (structural density)

Run after Pass 2. Only apply operations that are actually triggered — do not expand prose that deslop already scored as passing on density. This pass splits and restructures; it does not add padding or restatements.

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

**Stop condition:** Stop when a reader in the same broad field can read each paragraph once and extract the main point. Deslop's density rule takes precedence — do not expand prose that doesn't need it.

---

## Workflow summary

```
Input: draft section of scientific prose

Pass 1 — Deslop
  → Score (1–10) on Directness, Rhythm, Trust, Authenticity, Density
  → Must reach ≥35/50 before proceeding

Pass 2 — Humanize
  → Self-audit: "what's still AI here?"
  → Revise until no em dashes remain and audit bullets are resolved

Pass 3 — De-densify
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
