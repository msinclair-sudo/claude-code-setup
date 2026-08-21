# Chapter 9: Linking and References

**Source pages**: cross-references, other-sources, filenames

## Core Idea
Every link is a decision the reader has to make and a chance for them to leave and lose their place. Link selectively, and make the link text itself carry enough meaning to be read out of context.

## Frameworks Introduced

- **Link selectively**: Cross-references should point to genuinely nonessential material that adds understanding.
  - When *not* to link: If you only need to define a term, briefly explain a concept, or give a couple of steps, provide it on the page instead.
  - When to link: When readers need another product's software or standards — link to good documentation elsewhere rather than reproducing it badly.
  - The test: A few sentences of context saves the reader a trip; a full explanation of someone else's product doesn't belong in your docs at all.

- **Descriptive link text**: Use short, unique, descriptive phrases that give context for the destination.
  - Why it works: Screen reader users often jump link to link without the words between, and sighted readers scan for links. "Click here" is meaningless in both modes.
  - Two valid options: (1) match the link text to the destination's page title or heading, or (2) use a descriptive phrase.
  - Sometimes you must rework the surrounding sentence to produce a phrase that makes good link text — do that rather than settling for vague text.
  - When linking to a section on another page whose title matches a title on the source page, add context so the two are distinguishable.

- **Don't copy third-party content**: Copying risks copyright violation — paraphrase and link instead.
  - Applies to text, images, code, logos, and speech.
  - Treat as unsafe to reuse: third-party documentation, websites, books, blogs, videos, images, podcasts; reference sources including dictionaries, encyclopedias, and Wikipedia; open source documentation (licenses vary widely); and GitHub content (per-user licensing). When in doubt, don't.
  - The pattern: link the term to its source and state the definition in your own words.

- **Avoid duplicate links**: Within a page, link a destination once — where it's most useful.
  - Acceptable exceptions: linking to a specific section of another page; a very long page where the duplicates are far apart; or a page with multiple entry points (a procedure section and a troubleshooting section may each need the link).

## Key Concepts
- **Cross-reference**: A link to supplementary information that isn't required to complete the current task.
- **Cognitive load**: The decision cost each link imposes — the reason selectivity matters.

## Reference Tables

**Filename rules**

| Rule | Reason |
|---|---|
| Lowercase | Unix-style systems are case sensitive; `Impersonate-Service-Accounts.html` and `impersonate-service-accounts.html` are two different files |
| Hyphens, not underscores | Search engines read hyphens as word separators; underscores generally aren't recognized, hurting SEO |
| Standard ASCII alphanumerics only | Avoids encoding problems |
| No generic names | `document1.html` tells nobody anything |

| Example | Verdict |
|---|---|
| `avoiding-cliches.jd` | Recommended |
| `avoiding_cliches.jd` | Sometimes OK — only to match a directory already using underscores |
| `avoidingcliches.jd` | Not recommended |
| `avoidingCliches.jd` | Not recommended |
| `avoiding-clichés.jd` | Not recommended — non-ASCII |

Exceptions: if a directory already uses underscores throughout (`lesson_1.jd`, `lesson_2.jd`) and converting isn't feasible, stay consistent and add `lesson_4.jd`. Generated reference documentation may also impose its own naming conventions — those exceptions are fine.

## Worked Example

Handling a third-party definition. The rejected version copies the source's wording verbatim and appends a bare URL; the recommended version links the term and states the meaning freshly:

- **Recommended**: "A [recovery point objective (RPO)](https://en.wikipedia.org/wiki/Disaster_recovery), which is the maximum acceptable length of time during which data might be lost from your app due to a major incident."
- **Not recommended**: The same definition reproduced as a direct quotation with the raw URL in parentheses.

The recommended form does three things at once — it links rather than copies, it uses descriptive link text (the term itself), and it keeps the URL out of the running text.

## Key Takeaways
1. Provide short context on the page instead of linking; save links for genuinely external material.
2. Link text must be meaningful in isolation — page title or descriptive phrase.
3. Rework a sentence if that's what it takes to get good link text.
4. Paraphrase and link third-party content; never copy it.
5. Assume open source and GitHub content is *not* freely reusable unless verified.
6. One link per destination per page, with narrow exceptions.
7. Filenames: lowercase, hyphen-separated, ASCII, specific.

## Connects To
- **Ch 8 (Accessibility and Inclusion)**: descriptive link text is primarily an accessibility requirement.
- **Ch 2 (Structure and Flow)**: custom anchors are the target side of a cross-reference.
- **Ch 4 (Grammar and Usage)**: reference a title in sentence case when the source follows this guide.
- **Ch 3 (Punctuation)**: avoid URLs in running text, particularly at sentence end.
