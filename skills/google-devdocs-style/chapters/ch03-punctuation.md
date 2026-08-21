# Chapter 3: Punctuation

**Source pages**: commas, colons, semicolons, periods, dashes, hyphens, ellipses, parentheses, quotation-marks, slashes, possessives

## Core Idea
Punctuation choices are resolved by clarity and by convention, not by taste. Several marks Google treats as near-prohibited (semicolons, ellipses, slashes) — and one it treats as mandatory (the serial comma) — because ambiguity costs more than elegance.

## Frameworks Introduced

- **Serial comma, always**: In a series of three or more items, put a comma before the final *and* or *or*.
  - Why: Omitting it can change the meaning of the sentence. This is a hard rule, not a preference.

- **Hyphenation decision sequence**: Hyphenation depends on location (does the term precede a noun or follow a verb?), interpretation (is it ambiguous unhyphenated?), and convention (some terms are fixed regardless).
  - How: When unsure, check sources in order — (1) the documentation set you're working in, if it has an established convention; (2) this guide's word list; (3) Merriam-Webster.
  - General rule: don't hyphenate between a prefix and the main noun.

- **The parenthesis test**: Many readers skip anything in parentheses, so never put important information there.
  - How: When inclined to use parentheses, check whether commas, dashes, semicolons, or periods would serve. Keep any mid-sentence parenthetical short; if it runs long, use two sentences.
  - Punctuation: a full standalone sentence inside parentheses keeps its period *inside*.

- **When a semicolon is justified**: Avoid them, with three exceptions — joining two closely related independent clauses where a period or comma is weaker; preceding a conjunctive adverb (*therefore*) or phrase (*that is*) joining independent clauses; and separating a series of long or complex items that contain their own internal punctuation.

## Key Concepts
- **Serial (Oxford) comma**: The comma before the final conjunction in a series.
- **Em dash (—)**: Marks a break or interruption in a sentence; no space on either side. Distinct from a hyphen — never substitute `-` or `--` for it.
- **Suspension points**: Ellipses used to signal hesitation. Not used in Google documentation.
- **Coordinating conjunction**: *and*, *but*, *or*, *nor*, *for*, *so*, *yet* — take a comma before them when they join two independent clauses.

## Reference Tables

| Mark | Rule |
|---|---|
| Serial comma | Required in series of three or more. |
| Comma after intro | Generally place a comma after an introductory word or phrase. |
| Colon before a list | Text preceding the colon must stand alone as a complete sentence — "The fields are defined as follows:" not "The fields are:". |
| Word after a colon | Generally lowercase (exceptions on the capitalization page). |
| Semicolon | Avoid; three narrow exceptions above. |
| Em dash | No surrounding spaces. HTML `&mdash;`; macOS `Option+Shift+hyphen`. |
| Ellipsis | Avoid entirely. Acceptable only inside quoted text to elide a portion — never at the start or end of the quote. Omit UI ellipses ("Save …" → click **Save**) unless dropping them confuses. |
| Slash | Avoid except in code. Don't use for alternatives (write *and* or *or*) or in dates. |
| Quotation marks | Straight double quotes and apostrophes. Commas and periods go **inside**. |
| Period after URL | Avoid URLs in text; otherwise recast so the URL isn't sentence-final, or put it on its own line without the period. |

**Possessives**

| Noun type | Form | Example |
|---|---|---|
| Singular (including ending in *s*) | add *'s* | the storage class's quota |
| Plural ending in *s* | add apostrophe only | the models' capabilities |
| Plural not ending in *s* | add *'s* | the people's choice |

If a possessive reads awkwardly, rewrite to avoid it: "Analyze the business data," not "the businesses' data." Don't stack a possessive onto an abbreviation-in-parentheses — write "the rule that the Federal Trade Commission (FTC) issued," not "the Federal Trade Commission's (FTC's) rule." Never use *'s* to form a plural.

## Worked Example

Quotation marks are rare in technical writing. The four situations that warrant them:

| Situation | Example |
|---|---|
| Naming a section you can't link to directly | The technique is described in the section "Deploying containers" of the Containers overview video. |
| Naming a parent document when already linking to a section | The *machine learning (ML) workflow* section of "Introduction to Vertex AI" describes… |
| Directly citing a person, slogan, or motto | Martin Fowler has said, "We are still learning the techniques to write software effectively." |
| Using a term metaphorically — only if not established domain usage | This configuration forms an "island" within the network. |

Full-length works take italics instead; shorter works (articles, episodes) take quotation marks unless they're part of a link.

Parentheses handled three ways, only the first two recommended:

- **Recommended**: Enter a name for the instance—for example, `my-instance-99`.
- **Recommended**: Enter a six-digit hex number (for example, `228B22`), and then click **OK**.
- **Not recommended**: Enter a six-digit hex number (for example, if you want the color forest green, enter `228B22`), and then click **OK**. — the parenthetical has grown into a clause and should become its own sentence.

## Key Takeaways
1. Serial comma is mandatory.
2. The text before a list-introducing colon must be a complete sentence.
3. Avoid semicolons, ellipses, and slashes; each has narrow or zero exceptions.
4. Em dashes take no surrounding spaces and are never spelled with hyphens.
5. Never put important information in parentheses — readers skip them.
6. Commas and periods go inside quotation marks; use straight quotes.
7. For hyphens, check the local doc set, then the word list, then Merriam-Webster.

## Connects To
- **Ch 4 (Grammar and Usage)**: pluralization and capitalization interact with possessives and post-colon casing.
- **Ch 7 (Numbers and Data)**: ranges use en dashes and have their own rules; dates never use slashes.
- **Ch 5 (Formatting and Markup)**: italics vs. quotation marks for titles is a text-formatting decision.
- **word-list.md**: the tiebreaker for individual hyphenation rulings.
