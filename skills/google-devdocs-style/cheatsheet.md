# Cheatsheet

Decision rules and hard values. For term-by-term rulings see [word-list.md](word-list.md); for definitions see [glossary.md](glossary.md).

## Obligation verbs — the single highest-value table

| Meaning | Write | Never write |
|---|---|---|
| Required | *must*, or an imperative | *should* |
| Recommended | *We recommend…* / *Google recommends…* | *should* (except for widely recognized practices) |
| Optional | *can* | *should* |
| Expected outcome | state it: "returns 10 items" | *should return* |
| Possible outcome | *might* / *can* | *should* |

## Formatting assignments

| Treatment | Reserved for |
|---|---|
| **Bold** (`b`, `**`) | UI element names; run-in headings; notice lead words. Nothing else. |
| *Italic* (`i`, `_`) | New terms on first definition; words-as-words; math variables; full-length work titles; last-resort emphasis |
| `Code font` | Anything entered verbatim: attributes, classes, commands, output, data types, filenames, DB elements |

Emphasis ladder: rewrite first → italics if you must → never bold, never underline.

## Hard numeric values

| Thing | Value |
|---|---|
| Sentence length target | < 26 words |
| Paragraph length smell | > 5–6 sentences (not a hard cap) |
| Line length | 80 characters |
| Indentation | 2 spaces, never tabs |
| API sample code at page top | ~5–20 lines |
| Noun modifiers stacked | max 2 |
| Example phone numbers | 800-555-0100 … 800-555-0199 |

## Tells and smells

- Writing *should* → you haven't decided whether it's required, recommended, or optional.
- Two notices in a row → the content needs reorganizing.
- A one-item numbered list → make it a bullet.
- A one-column table → make it a list.
- Adding *by you* to fix passive voice → recast the sentence instead.
- Reaching for parentheses → try commas, dashes, or a second sentence; readers skip parentheses.
- *now*, *new*, *currently* in product docs → delete; the sentence is almost always better without them.
- A heading starting with an *-ing* word → recast as a base-form verb or noun phrase.
- Imperative commands buried in running prose → probably wants to be a numbered procedure.
- Bare *this* or *these* → add the noun.

## Punctuation quick rules

- Serial comma: **always**.
- Semicolons, ellipses, slashes: **avoid** (narrow exceptions only; slashes OK in code).
- Em dash: no surrounding spaces; never `-` or `--`.
- Commas and periods: **inside** quotation marks.
- Colon before a list: preceding text must stand alone as a sentence.
- Straight quotes and apostrophes, never curly.

## Number formatting

- Spell out: zero–nine, all ordinals, any sentence-initial number.
- `64&nbsp;GB` — nonbreaking space between value and unit.
- No space: `$10`, `65%`, `180°`. Temperature: `98.6&nbsp;&deg;F`.
- Dates: spell out months and weekdays; never slashes.
- Times: 12-hour default, `3 PM` / `3:45 PM`, ranges `5-10 minutes`.

## Heading decision

| Section type | Form | Example |
|---|---|---|
| Task | bare infinitive | Create an instance |
| Concept | noun phrase, no *-ing* start | Migration to Google Cloud |
| Optional section | `Optional:` prefix, at the front | Optional: Customize your alias |

All headings: sentence case, no terminal period, one `h1` per page, never skip a level.

## List or table?

| Data per item | Use |
|---|---|
| 1 | Bulleted or numbered list |
| 2 | Description list (sometimes a table) |
| 3+ | Table |

## When the guide is silent

1. Project-specific style
2. This guide
3. Third party — spelling: Merriam-Webster (first spelling listed) · nontechnical: Chicago Manual of Style 17th ed. · technical: Microsoft Writing Style Guide

Then check established usage in your own doc set or a corpus like Google Ngram Viewer.

## Legal / safety non-negotiables

- Example domains: `example.com`/`.org`/`.net`, or `altostrat.com`, `examplepetstore.com`, `cymbalgroup.com`, `myownpersonaldomain.com`.
- Never a real domain, email, name, or phone number.
- PII in screenshots: opaque overlay, then flatten. Never blur.
- Trademarks modify nouns — never nouns, verbs, plurals, or possessives.
- Never copy third-party content — paraphrase and link. Assume OSS and GitHub content is *not* reusable.
