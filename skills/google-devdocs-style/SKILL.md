---
name: google-devdocs-style
description: "Knowledge base from the Google developer documentation style guide (Google, 2026 edition). Use when applying Google's editorial rules for technical writing — voice and tone, active voice, punctuation, code formatting, API reference, accessibility, inclusive language, timeless documentation — or when looking up a specific term ruling."
allowed-tools:
  - Read
  - Grep
argument-hint: [topic, rule, term, or chapter number]
---

# Google Developer Documentation Style Guide
**Publisher**: Google | **Source pages**: 69 | **Chapters**: 12 | **Generated**: 2026-08-18
**Origin**: <https://developers.google.com/style>

## How to Use This Skill

- **Without arguments** — load the core rules below
- **With a topic** — ask about `passive voice`, `notices`, `placeholders`; I read the relevant chapter
- **With a specific word** — ask "is *allowlist* OK?"; I grep [word-list.md](word-list.md), which holds Google's per-term rulings verbatim
- **With a chapter** — ask for `ch06`
- **To edit prose** — give me text and ask for a style pass; I apply the rules below and cite the chapter for each change

For anything not covered below, I read the relevant chapter file before answering.

---

## Core Rules

**Voice.** Write as a knowledgeable friend who understands what the developer is trying to do. Conversational, not frivolous; never pedantic. Readers are usually in a hurry, looking for one thing.

**Active voice.** Make the doer the grammatical subject. If fixing a passive sentence requires adding *by you*, recast it instead. Passive is legitimate only to emphasize an object ("The file is saved"), to de-emphasize a blamed actor ("Over 50 conflicts were found"), or when the actor genuinely doesn't matter.

**Second person.** *You* = the reader. *User* = the user of the software your reader is building. Never blur them. Use the imperative for instructions.

**Present tense.** Reserve *will* for genuinely later events. Never use future tense to describe a coming release, and never pre-announce unreleased features.

**Condition before instruction.** "To delete the entire document, click **Delete**" — not the reverse. Readers who don't need the step stop at the comma.

**Replace *should*.** It's ambiguous — the reader can't tell if the action is required or optional. Decide: required → *must* or an imperative; recommended → *We recommend…*; optional → *can*; possible outcome → *might*. (*should* is acceptable only for widely recognized practices like "You should use a strong password.")

**Timeless documentation.** Delete *now*, *new*, *currently*, *at present*, *eventually* from product docs. Document how the product works today — not what changed, not what's coming. These words stay fine in release notes and blog posts.

**Excessive claims.** Avoid *best*, *simplest*, *fastest*, *never*, *always*. Prefer "helps with security" over "prevents" — the hedged version survives an incident. Cite sources for specific performance numbers. Judge every claim against what might be true in the future.

**Sentence case** for all titles and headings, with no terminal period. Task headings start with a base-form verb ("Create an instance"); concept headings are noun phrases ("Migration to Google Cloud"). Never open a heading with an *-ing* word. Put `Optional:` at the front.

**Formatting is meaning.** Bold (`b`, `**`) is for UI element names and run-in headings — not general emphasis. Italics (`i`, `_`) mark new terms on first definition, words-as-words, math variables, and full-length work titles. Code font marks anything entered verbatim. For emphasis, rewrite first; use italics only if you must; never bold or underline. Choose HTML elements for meaning and CSS for appearance — `em` is emphasis, `i` is non-emphasis italics; `strong` is importance, `b` is visual attention.

**Serial comma always.** Avoid semicolons, ellipses, and slashes. Em dashes take no surrounding spaces. Commas and periods go inside quotation marks.

**Accessibility.** Keep sentences under 26 words. Never skip heading levels. Link text must be meaningful read in isolation — screen reader users jump link to link. State things positively ("You can continue without a path," not "A missing path won't prevent you from continuing"). Avoid ableist and gendered terms, metaphor, and idiom. Don't force line breaks.

**Jargon filter.** Before keeping a specialized term: can you write around it? Replace it with something more specific? Used once → define in place. Used throughout → gloss on first reference. In a command → code font, direct reference only.

**Code.** Code font signals verbatim entry and marks its boundaries. Keep `[]`, `|`, `{}`, `...` out of click-to-copy examples — they break the command when pasted. Name placeholders descriptively in uppercase (`PROJECT_ID`). Mark omitted code with a language-appropriate comment, never `...`. Reference method descriptions take third-person verbs ("Creates a new task").

**Legal.** Example domains only (`example.com`, `altostrat.com`, `cymbalgroup.com`). Never a real domain, email, name, or phone number. Trademarks modify nouns — never nouns, verbs, plurals, or possessives. Never copy third-party content; paraphrase and link. Redact PII with an opaque overlay, never a blur.

**When this guide is silent**: project-specific style → this guide → Merriam-Webster (spelling), Chicago Manual of Style 17th ed. (nontechnical), Microsoft Writing Style Guide (technical).

**Break the rules** when doing so serves your readers — Google says so explicitly.

---

## Chapter Index

| # | Title | Key Topics |
|---|-------|------------|
| [ch01](chapters/ch01-voice-and-tone.md) | Voice and Tone | active voice, second person, tense, jargon, excessive claims, anthropomorphism |
| [ch02](chapters/ch02-structure-and-flow.md) | Structure and Flow | condition-before-instruction, headings, lists, procedures, reference hierarchy |
| [ch03](chapters/ch03-punctuation.md) | Punctuation | serial comma, colons, semicolons, dashes, hyphens, quotes, possessives |
| [ch04](chapters/ch04-grammar-and-usage.md) | Grammar and Usage | articles, prepositions, agreement, capitalization, abbreviations |
| [ch05](chapters/ch05-formatting-and-markup.md) | Formatting and Markup | bold/italic/code assignments, semantic tagging, notices, Markdown vs. HTML |
| [ch06](chapters/ch06-code-documentation.md) | Code Documentation | code font, code samples, placeholders, click-to-copy, API reference |
| [ch07](chapters/ch07-numbers-and-data.md) | Numbers and Data | number spelling, units, dates, times, math notation, phone numbers |
| [ch08](chapters/ch08-accessibility-and-inclusion.md) | Accessibility and Inclusion | screen readers, heading hierarchy, ableist language, translation |
| [ch09](chapters/ch09-linking-and-references.md) | Linking and References | link selectivity, descriptive link text, third-party content, filenames |
| [ch10](chapters/ch10-ui-and-visuals.md) | UI Elements and Visuals | task-over-widget, UI bolding, images, tables, PII redaction |
| [ch11](chapters/ch11-naming-and-legal.md) | Naming, Trademarks, Legal | product capitalization, trademark usage, example domains |
| [ch12](chapters/ch12-documentation-types.md) | Documentation Types and Stance | prescriptive writing, obligation verbs, timeless documentation |

## Topic Index

- **Abbreviations** → ch04 · **Accessibility** → ch08 · **Active voice** → ch01 · **Alt text** → ch10
- **Anchors** → ch02 · **Anthropomorphism** → ch01 · **API reference** → ch06 · **Articles** → ch04
- **Bold** → ch05, ch10 · **Capitalization** → ch04, ch11 · **Click-to-copy** → ch06 · **Code font** → ch06
- **Code samples** → ch06 · **Commands** → ch06 · **Commas** → ch03 · **Contractions** → ch01
- **Cross-references** → ch09 · **Dashes** → ch03 · **Dates and times** → ch07 · **Ellipses** → ch03
- **Example domains** → ch11 · **Excessive claims** → ch01 · **Figurative language** → ch08
- **Filenames** → ch09 · **Footnotes** → ch05 · **Future features** → ch01, ch12 · **Gendered language** → ch08
- **Headings** → ch02, ch04, ch08 · **Hyphens** → ch03 · **Images** → ch10 · **Inclusive language** → ch08
- **Italics** → ch05 · **Jargon** → ch01 · **Line length** → ch05 · **Link text** → ch09
- **Lists** → ch02, ch10 · **Localization** → ch08 · **Markdown vs. HTML** → ch05 · **Math notation** → ch07
- **Notices** → ch05 · **Numbers** → ch07 · **Parentheses** → ch03 · **Passive voice** → ch01
- **Person (you/we)** → ch01 · **Phone numbers** → ch07 · **PII** → ch10, ch11 · **Placeholders** → ch06
- **Prescriptive writing** → ch12 · **Procedures** → ch02 · **Product names** → ch11 · **Pronouns** → ch01, ch08
- **Punctuation** → ch03 · **Screen readers** → ch08 · **Semantic tagging** → ch05 · **Semicolons** → ch03
- **Sentence case** → ch04 · **Serial comma** → ch03 · ***should*** → ch12 · **Tables** → ch10
- **Tense** → ch01 · **Third-party content** → ch09 · **Timeless documentation** → ch12 · **Tone** → ch01
- **Trademarks** → ch11 · **Translation** → ch08 · **UI elements** → ch10 · **Units of measure** → ch07
- **Word rulings** → [word-list.md](word-list.md)

## Supporting Files

- [cheatsheet.md](cheatsheet.md) — decision tables, hard values, and tells/smells
- [patterns.md](patterns.md) — reusable techniques (jargon filter, excessive-claim test, notice triage…)
- [glossary.md](glossary.md) — terms the guide defines, with chapter references
- [word-list.md](word-list.md) — **verbatim** per-term rulings from Google; grep this for specific words

---

## Scope & Limits

Covers the 69 guidance pages of the style guide as downloaded 2026-08-18. Excludes the changelog page (dated release notes, no reusable guidance).

This is Google's house style for *developer documentation*. Some rules are Google-specific (product name capitalization, reserved example domains) and some conflict with other style guides — Google mandates the serial comma and sentence-case headings where others don't. For a different organization, treat project-specific style as the higher authority, which is what the guide's own reference hierarchy prescribes.

The word list is Google's per-term reference preserved as-is for lookup; its rulings sometimes update, so check the live page for contested terms.
