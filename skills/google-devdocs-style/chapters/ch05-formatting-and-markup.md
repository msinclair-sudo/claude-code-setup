# Chapter 5: Formatting and Markup

**Source pages**: text-formatting, semantic-tagging, html-formatting, markdown, italics-terms, highlights, notices, footnotes

## Core Idea
Formatting carries meaning, so choose elements for what they *mean*, not what they *look like*. Bold is reserved almost entirely for UI elements and run-in headings; anything you want merely to look a certain way is a job for CSS.

## Frameworks Introduced

- **Semantic vs. visual markup**: Use HTML elements for their designed purpose; reach for CSS when you want a visual result with no matching semantics.
  - The paired distinctions: `em` means emphasis (use `i` for non-emphasis italics); `strong` means strong importance (use `b` for bold without importance); `br` is only for line breaks that are genuinely part of the content, like poems or addresses — never for spacing.
  - Never use heading elements to style text, or frames/tables for layout.

- **Formatting assignment**: Each visual treatment has a narrow, defined job.
  - **Bold** (`<b>` / `**`) — UI elements and run-in headings, including the lead word of notices. Nothing else.
  - **Italic** (`<i>` / `_`) — new terms on first definition, words-as-words, mathematical variables, titles of full-length works (unless part of a link), and emphasis where the words can't carry it alone.
  - **Code font** — code-related text (see Ch 6).
  - For emphasis, prefer italics over bold or underline — and prefer rewriting over either.

- **Notice selection and restraint**: Notices interrupt the flow to deliver information the reader can't miss — but readers demonstrably skip elements outside their focus.
  - How to decide: Write the content as regular text first, *then* judge whether it needs to be a notice. If unsure, it probably doesn't.
  - Escalation: **Note** — a useful but non-critical aside or tip. **Caution** — proceed carefully. **Warning** — stronger than a caution: don't do this, or this step risks real harm.
  - Never stack notices. Two or more in a row lose their distinctiveness and signal that the content needs reorganizing.

## Key Concepts
- **Words as words**: Referring to a word, phrase, or letter as itself — takes italics, never bold or quotation marks.
- **Run-in heading**: A bolded lead term inside a list item.
- **Semantic tagging**: Marking content by meaning (`cite` for standalone-work titles) rather than appearance. Not available in Markdown.

## Reference Tables

**Markdown conventions**

| Intent | Use | Not |
|---|---|---|
| Bold | `**` | `__` — hard to distinguish in an editor |
| Italic | `_` | `*` — hard to distinguish from bold in source |

**Source file formatting** (follows Google's HTML/CSS Style Guide, except: don't omit optional elements)

| Rule | Value |
|---|---|
| Indentation | Spaces only, never tabs — editors differ and some Markdown features require spaces |
| Indent width | 2 spaces per level |
| Elements/attributes | All lowercase |
| Trailing spaces | None, except where Markdown requires |
| Line length | Break at 80 characters, including `<pre>` blocks |

Line-length exceptions: `meta` elements must stay on one line; long URLs can't be broken without breaking the link — put such a URL on its own line. In older files with a different consistent width, match the file rather than reformatting it. When breaking lines in code, never change the code's meaning — ask someone who knows the language if unsure.

**Markdown vs. HTML**: Either is acceptable. Markdown is easier to write and read in source; HTML is more expressive, especially for semantic tagging, and handles cases like special characters in code. Largely personal preference — but follow whatever your team or template already uses.

## Worked Example

Italics for terms, in the two situations that call for them:

- **New term, defined on the spot**: "A *Clos network* is a kind of multistage circuit switching network." — italics on first mention only, never bold or quotation marks.
- **Words as words**: "To form a possessive of a singular noun, add *'s* to the end of the word."

The semantic choice in practice — same rendered output, different meaning:

```html
<!-- Emphasis: the word matters to the sentence's meaning -->
<p>Do <em>not</em> delete the bucket.</p>

<!-- Italics with no emphasis: a term being introduced -->
<p>A <i>Clos network</i> is a multistage circuit switching network.</p>
```

Both render as italics; only the first claims emphasis. The same split applies to `strong` (importance) versus `b` (bold without importance).

**Footnotes**: avoid them — they're inaccessible and complicate localization. Use a cross-reference, a note, or a parenthetical instead. If genuinely unavoidable, use a superscript number (`<sup>1</sup>`).

## Key Takeaways
1. Pick elements for meaning; use CSS for appearance.
2. Bold is for UI elements and run-in headings — not general emphasis.
3. Italicize new terms on first definition, words-as-words, math variables, and full-length work titles.
4. In Markdown use `**` for bold and `_` for italics, for source legibility.
5. Draft notice content as body text first; promote it only if it earns the interruption.
6. Never place notices back to back — reorganize instead.
7. Spaces not tabs, 2-space indents, 80-character lines.
8. Avoid footnotes; prefer cross-references, notes, or parentheticals.

## Connects To
- **Ch 6 (Code Documentation)**: code font is the third major formatting assignment.
- **Ch 10 (UI and Visuals)**: bold-for-UI-elements originates there.
- **Ch 2 (Structure and Flow)**: run-in headings are a list construct.
- **Ch 8 (Accessibility and Inclusion)**: the case against footnotes is an accessibility argument.
