# Chapter 8: Accessibility and Inclusion

**Source pages**: accessibility, inclusive-documentation, translation

## Core Idea
Roughly 15% of the world's population has an accessibility need, and much of this documentation is read by people whose first language isn't English. Writing for those readers — shorter sentences, literal language, semantic structure — measurably improves the document for everyone.

## Frameworks Introduced

- **Write for screen readers, not just eyes**: Assume the document will be heard and navigated by keyboard.
  - How: Verify every part of the page — tabs, form buttons, interactive elements — is reachable by keyboard alone. Actually test with a screen reader; it doubles as a self-editing pass.
  - Consequences for formatting: avoid unnecessary font formatting (screen readers announce text modifications aloud); avoid camel case and all caps (some readers spell out capitals letter by letter, and some languages are unicase); don't rely on punctuation to carry meaning, since not all marks are read — which is a further reason to avoid exclamation marks, question marks, and semicolons.
  - Prefer native HTML elements over custom styles, and use semantic tagging.

- **Heading hierarchy as navigation**: Headings are how many readers move through a page, so the hierarchy must be real.
  - How: Never skip levels — an `h3` follows an `h2`. One level-1 heading for the page title. No empty headings, and none without associated content. To change a heading's *appearance*, use CSS, never a level that misrepresents the structure.

- **The three localization terms**, which are not synonyms:
  - **Localization** — adapting a product and its docs for a specific country, including currencies and units of measurement.
  - **Translation** — converting one language to another; may involve localization, but isn't the same thing.
  - **Internationalization** — designing so that localization is cheap later, such as isolating UI strings in a separate file.

- **Simplify for translation**: Every simplification compounds across languages.
  - Prefer the simple word: *start* over *commence*, *so* over *consequently*, *use* over *utilize* or *leverage* — unless the fancier word carries a genuinely distinct sense.
  - Prefer one word to a phrase: *some* or *many* over *a number of*.
  - Write shorter sentences — under 26 words is the accessibility target. English sentences often expand when translated, so long ones raise cost, delay review, and can break page rendering.
  - Avoid phrasal verbs where a simpler verb exists ("This document uses the following terms," not "makes use of"). Some are unavoidable and fine: *set up*, *log in*, *sign in*.
  - Cap modifier stacking: never more than two nouns modifying another noun. Place *only* immediately before what it modifies — "Request only one token."

## Key Concepts
- **Ableist language**: Words like *crazy*, *insane*, *blind to*, *cripple*, *dumb* used figuratively. Replace with a more accurate term for the actual meaning.
- **Figurative language**: Metaphor and idiom — imprecise, distracting, and hard to translate. Use words in their primary sense; avoid framings like *pets versus cattle* for stateful vs. stateless systems.
- **Unicase**: A writing system with no upper/lower distinction — one reason capitalization can't carry meaning.

## Reference Tables

| Recommended | Not recommended | Why |
|---|---|---|
| person-hours | man-hours | Unnecessarily gendered |
| Build AI that benefits humanity. | …benefits mankind. | Unnecessarily gendered |
| You can continue without a path. | A missing path won't prevent you from continuing. | Double negative; state it positively |
| and | & | Ampersands in headings, text, nav, and TOCs — though `&` is fine in code, in UI element names that use it, and in space-constrained table headings and diagram labels |

## Worked Example

The double-negative rule is the clearest demonstration that accessible phrasing is simply better phrasing:

- **Not recommended**: "A missing path won't prevent you from continuing." — the reader has to resolve a negative noun phrase against a negated verb to extract a positive fact.
- **Recommended**: "You can continue without a path." — same information, one clause, no negation to unwind.

The same instinct drives the ease-of-reading guidance as a set: break up walls of text with paragraphs, headings, and lists; define acronyms on first use and again if reuse is infrequent; keep list items parallel in structure; lead each paragraph with its distinguishing information; and left-align text (never center or full-justify). Avoid "exceptions for exceptions" — nested caveats are the double negative's structural cousin.

If a product has specific accessibility features, document them explicitly. The `gcloud` CLI, for instance, has togglable percentage progress bars and ASCII box rendering — features that only help readers who know they exist.

## Key Takeaways
1. Test with a screen reader and with keyboard-only navigation.
2. Never skip heading levels; use CSS for visual changes, not the wrong heading level.
3. Keep sentences under 26 words; shorter sentences translate better and cost less.
4. Replace ableist and gendered terms with more accurate ones.
5. Avoid metaphor, idiom, and jargon — use words in their primary sense.
6. State things positively; avoid double negatives.
7. Don't force line breaks — they fail at larger text sizes and in resized windows.
8. Write *and*, not *&*, outside code, UI names, and space-constrained labels.

## Connects To
- **Ch 1 (Voice and Tone)**: the push for conversational tone is exactly where figurative language sneaks in.
- **Ch 5 (Formatting and Markup)**: semantic tagging and the case against footnotes are accessibility requirements.
- **Ch 2 (Structure and Flow)**: paragraph breaks, headings, and lists are scannability tools.
- **word-list.md**: per-term rulings, including terms marked "Don't use" for inclusivity reasons.
