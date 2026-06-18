---
name: sentence-prose
description: "Knowledge base from \"The Science of Scientific Writing\" by George D. Gopen & Judith A. Swan (American Scientist, 1990). Use when applying reader-expectation principles for sentence-level clarity — topic position, stress position, subject-verb separation, old/new information, locating the action — revising dense scientific prose, or studying the article's frameworks."
allowed-tools:
  - Read
  - Grep
argument-hint: [topic, principle name, or chapter number]
---

# The Science of Scientific Writing
**Authors**: George D. Gopen & Judith A. Swan | **Source**: *American Scientist* (1990) | **Pages**: ~16 | **Chapters**: 7 | **Generated**: 2026-06-18

The foundational article on **reader-expectation theory**: clarity comes not from simpler words but from placing information where readers structurally expect it. Sentence-level companion to the `schimel-science-writing` skill (which covers story structure and the larger argument).

## How to Use This Skill

- **Without arguments** — load the core principles below for reference
- **With a topic** — ask about `stress position`, `topic position`, `subject-verb`, `old/new information`, `locating the action`, `logical gaps`; I read the relevant chapter
- **With a chapter** — ask for `ch04`; I load that file
- **Browse** — ask "what chapters do you have?" for the full index

When you ask about a topic not in Core Principles below, I read the relevant chapter file before answering.

---

## Core Principles & Mental Models

**The master idea**: Readers interpret prose from its *structure* before its content. They hold fixed expectations about *where* each kind of information belongs. Satisfy those expectations and the reader's energy goes to meaning; violate them and it's spent unravelling the sentence. "Improving the writing actually improves the thinking" — structural revision repeatedly exposes gaps in the science itself.

**The sentence map** (the single most useful model):
```
[ TOPIC POSITION ......... STRESS POSITION ]
  old info / whose story     new info to emphasize
  "first things first"       "save the best for last"
        verb arrives early, carrying the ACTION
```

**The seven principles** (the article's closing synthesis — use as a revision checklist):
1. **Follow a grammatical subject as soon as possible with its verb.** A long subject-verb gap reads as an interruption that demotes whatever sits inside it. (ch02)
2. **Place the new information you want emphasized in the stress position** — the point of syntactic closure (sentence end, or before a colon/semicolon). "Save the best for last." (ch03)
3. **Place the person/thing whose story the sentence tells in the topic position** (its start). Readers assume the sentence is about whoever shows up first. (ch04)
4. **Place old, backward-linking information in the topic position** for linkage and context. Misplaced old/new info is the #1 problem in professional writing. (ch04)
5. **Articulate the action of every clause in its verb** — not buried in a noun or left to a limp *is/are*. (ch06)
6. **Provide context before asking the reader to consider anything new.** (ch01, ch07)
7. **Make the structural emphasis coincide with the substantive emphasis** — stress what actually matters. (ch07)

**Key reframes**:
- **"Too long" redefined**: a sentence is too long when it has *more candidates for stress than stress positions available* — NOT past any word count (the mythical 29). 10-word sentences can be impenetrable; 100-word sentences can flow. (ch03)
- **Active vs. passive is not a rule**: choose whichever keeps the paragraph's continuing subject in the topic position. "Pollen is dispersed by bees" is *superior* in a paragraph about pollen. (ch04)
- **Principles, not rules**: there is no algorithm for good writing. The best stylists violate expectations deliberately — but only against a background of mostly satisfying them. (ch07)
- **Old vs. new information**: old = already in this discourse (→ topic position); new = first appearance (→ stress position when emphasis-worthy). The middle of every sentence holds both. (ch04)

**Core diagnostics**:
- **Topic-string test**: read only the sentence openings of a paragraph — if they don't tell one coherent story, the focus is drifting. (ch04)
- **Verb test**: read only the verbs — if they don't convey the action, the actions are misplaced. (ch06)
- **Stress→topic hand-off**: new info stressed in one sentence should resurface as old info in the next; a dropped thread marks a logical gap to write in. (ch05)

---

## Chapter Index

| # | Title | Key Frameworks |
|---|-------|----------------|
| [ch01](chapters/ch01-reader-expectations-and-context.md) | Writing with the Reader in Mind | reader-expectation methodology, substance↔structure, units of discourse |
| [ch02](chapters/ch02-subject-verb-separation.md) | Subject-Verb Separation | keep subject+verb close, syntactic resolution |
| [ch03](chapters/ch03-the-stress-position.md) | The Stress Position | stress position, syntactic closure, "too long" redefined |
| [ch04](chapters/ch04-the-topic-position.md) | The Topic Position | topic position, old/new information, whose story |
| [ch05](chapters/ch05-perceiving-logical-gaps.md) | Perceiving Logical Gaps | gap detection, stress→topic hand-off, flag words |
| [ch06](chapters/ch06-locating-the-action.md) | Locating the Action | action in the verb, the verb test, consistent actor |
| [ch07](chapters/ch07-writing-and-the-scientific-process.md) | Writing & the Scientific Process | seven principles, principles-not-rules, skillful violation |

## Topic Index

- **Action / verbs** → ch06
- **Active vs. passive voice** → ch04
- **Context before content** → ch01, ch07
- **Flag words ("both")** → ch05
- **Logical gaps** → ch05
- **New information** → ch04, ch03
- **Old information** → ch04
- **Principles vs. rules** → ch07
- **Reader expectations (methodology)** → ch01
- **Sentence length / "too long"** → ch03
- **Seven principles (summary)** → ch07
- **Stress position** → ch03
- **Subject-verb separation** → ch02
- **Substance ↔ structure** → ch01, ch07
- **Syntactic closure** → ch03
- **Topic position** → ch04
- **Topic-string test** → ch04
- **Units of discourse** → ch01
- **Verb test** → ch06
- **Whose story** → ch04

## Supporting Files

- [glossary.md](glossary.md) — all key terms with definitions
- [patterns.md](patterns.md) — the revision techniques (diagnostic + fix)
- [cheatsheet.md](cheatsheet.md) — sentence map, seven-principle checklist, decision rules, tells & smells

---

## Scope & Limits

Covers the 1990 article only. For larger-scale story structure, openings, the knowledge gap, and proposal/paper architecture, use the complementary `schimel-science-writing` skill. For applying these principles to your own draft, combine with the `write-pass` / `deslop` / `humanizer` skills.
