# Chapter 4: Grammar and Usage

**Source pages**: articles, prepositions, pluralization, plurals-parentheses, capitalization, abbreviations

## Core Idea
Grammar decisions here are driven by translation and comprehension, not by traditional prescriptive rules. Google keeps articles that terser style guides drop, and explicitly rejects the folk rule against sentence-final prepositions.

## Frameworks Introduced

- **Keep articles, always**: Include *a*, *an*, and *the* — including in headings and titles, where brevity tempts you to drop them.
  - Why it works: Articles aid comprehension and translation. "Create a VM instance" beats "Create VM instance."

- **Sentence case for titles and headings**: Capitalize only the first word, the first word after a colon in a subheading, and proper nouns or terms with fixed capitalization. No period at the end of a title or heading.
  - Referencing rule: When citing a title from a document that follows this guide, use sentence case *even if the original uses title case* — so the reference still matches once that title is updated. Retain original capitalization only for works that don't follow this guide.

- **The speaking test for abbreviations**: Unsure whether a short form is an abbreviation or just a short word? Say it aloud in a sentence.
  - How: If you speak it as a word ("This is a demo version of the product"), treat it as a word — no period. *app*, *demo*, and *sync* are short versions, not abbreviations.

- **Optional plurals: pick one**: Never write *key(s)*, *child(ren)*, or *port(s)*. Choose singular or plural, stay consistent, and use *one or more* when you genuinely must signal both.

## Key Concepts
- **Acronym**: Formed from initial letters and pronounced as a word (*NATO*, *scuba*).
- **Initialism**: Formed from initial letters, pronounced letter by letter (*CIA*, *FYI*). The acronym/initialism distinction rarely matters — *acronym* covers both in most contexts.
- **Shortened word**: Part of a word or phrase, sometimes with a trailing period (*Dr.*, *etc.*, *min*).
- **Sentence case**: Only the first word and proper nouns capitalized.

## Reference Tables

| Rule | Guidance |
|---|---|
| Sentence-final prepositions | Allowed. Place prepositions where they read most naturally — "the language you're interacting with" beats "the language with which you're interacting." |
| Unnecessary capitals | Before capitalizing, ask why. Don't capitalize by reflex. |
| Capitalization as meaning | Never rely on it. A reader new to the domain won't catch *Pod* vs. *pod*. |
| All-uppercase | Only in official names, always-caps abbreviations, or when referring to all-caps code. |
| Camel case | Only in official names or when referring to camel-case code. |
| Plural via *'s* | Never — it collides with possessives and contractions. |
| After *one or more* | Use a plural noun. |

## Worked Example

Subject–verb agreement fails most often when the subject is long or compound. The head noun governs the verb, not the nearest noun:

- **Recommended**: "Confirm that the number of entries listed in the directory **is** accurate." — the subject is *number*, not *entries*.
- **Not recommended**: "The efficiency of algorithms that process data sets **depend** on memory allocation." — the subject is *efficiency*, so it should be *depends*.

With compound subjects, *and* takes a plural while *or* agrees with the nearer element:

- **Recommended**: "The request payload and header information **are** logged for debugging."
- **Recommended**: "Either the API keys or service account **wasn't** authenticated."
- **Not recommended**: "User authentication and authorization **is** processed…" — two subjects joined by *and* require *are*.

Removing optional-plural parentheses usually improves the sentence rather than merely fixing it:

| Recommended | Not recommended |
|---|---|
| To find your API key, visit the **Credentials** page. | To find your API key(s), visit the **Credentials** page. |
| The value of the parent depends on the values of its children. | The value(s) of its child(ren). |
| A physical linecard can contain one or more ports. | A physical linecard can contain port(s). |

## Key Takeaways
1. Never drop articles for brevity — not even in headings.
2. Ending a sentence with a preposition is fine; readability governs.
3. Sentence case for all titles and headings, with no terminal period.
4. Reference titles in sentence case when the source follows this guide.
5. Don't encode meaning in capitalization alone.
6. Resolve *key(s)*-style constructions by choosing one form or using *one or more*.
7. Check agreement against the true head of a long subject.

## Connects To
- **Ch 1 (Voice and Tone)**: contractions are the fourth abbreviation category and follow their own rules.
- **Ch 3 (Punctuation)**: possessives and post-colon capitalization overlap directly.
- **Ch 11 (Naming and Legal)**: product names have their own capitalization and article rules.
- **Ch 8 (Accessibility and Inclusion)**: keeping articles is part of writing for a global audience.
