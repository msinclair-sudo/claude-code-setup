# Chapter 10: UI Elements and Visuals

**Source pages**: ui-elements, images, tables

## Core Idea
Describe what the reader is trying to accomplish rather than which widget to poke — task-focused instructions survive UI redesigns. When you do show the interface, crop tightly and never ship an image of text.

## Frameworks Introduced

- **Task over widget**: State instructions in terms of the goal, not the gesture, when practical.
  - Why it works: The reader understands the *purpose* of the step, and the procedure survives UI changes.
  - How: "Refresh the page" and "Expand the **Advanced options** section" beat naming the control.
  - When to reverse it: When guiding the reader through the page *is* the point, or when the UI is unobvious enough that the gesture needs spelling out — then "Click **Refresh**" or "To expand the **Advanced options** section, click the expander arrow." Judge by audience and context.

- **UI element formatting**: Bold every UI element referred to by name — buttons, menus, dialogs, windows, list items, anything with a visible name.
  - How: `b` in HTML, `**` in Markdown. Use `b` rather than `strong` deliberately: `b` draws visual attention, while `strong` claims importance the element doesn't have.
  - Don't use code font for UI elements, unless the element independently meets the code-font criteria — in which case use both code font *and* bold.

- **List or table?**: Decide by how many pieces of data each item carries.
  - One unit per item (language names, steps) → numbered, lettered, or bulleted list.
  - Two related pieces per item (term/definition) → description list, or a table in some contexts.
  - Three or more per item (parameter name, type, description) → table.

- **PII removal must be irreversible**: If a source screenshot contains personally identifying information, cover it with a solid-color overlay at 100% opacity.
  - Why: Blurs, mosaics, and similar image-processing effects can be reversed to recover the original content.
  - When exporting to a layered format (PDF, TIFF), flatten the image so the hidden layer can't be extracted.

## Key Concepts
- **Image map**: A coordinate-overlay hotspot region. Avoid — inaccessible, inconsistently implemented across browsers, unreliable on mobile at different scales, and costly to maintain. Provide a list of text references after the image instead.
- **Alt text, caption, and description**: Three distinct things, not interchangeable. Most images should also be preceded by an introductory sentence.

## Reference Tables

**Image guidelines**

| Topic | Guidance |
|---|---|
| When to use | Only when an image explains something genuinely hard to express in words |
| Screenshots | Be discreet — capture only UIs important to the discussion |
| Text, code, terminal output | Never as images; use real text |
| Diagram format | SVG preferred (stays sharp when zoomed); otherwise PNG |
| Backgrounds | Never transparent — breaks the Devsite lightbox widget |
| Animation | Never animated GIF; use MP4 or similar efficient format |
| Consistency | One OS for all screenshots in a doc set; consistent treatment of drop shadows and framing |
| Cropping | Crop to the relevant region — helps focus and future-proofs against unrelated UI changes |
| Filenames | Descriptive (see Ch 9) |

**Where not to use tables**

- Page layout — use the site's CSS.
- Single-row content, usually — though reference documentation may keep it for layout consistency.
- Single-column content — make it a list.
- Code snippets.
- Long one-dimensional lists split into columns to save space. Tables are for genuinely two-dimensional data: material that makes semantic sense in rows *and* columns.
- The middle of a numbered procedure.

For multi-paragraph table cells, use `p` elements rather than `br` — the same semantic rule that governs list items (Ch 5).

## Worked Example

The task-versus-widget choice, with both columns valid depending on context:

| Task-focused (default) | Widget-focused (when the UI is the point) |
|---|---|
| Refresh the page. | Click **Refresh**. |
| Expand the **Advanced options** section. | To expand the **Advanced options** section, click the expander arrow. |

Note that even the task-focused column bolds the named UI element. The distinction isn't whether you mention the interface — it's whether the instruction is framed around the reader's goal or the mechanics of the control.

The list-or-table decision applied to a parameter set: each parameter carries a name, a data type, and a description — three pieces of related data per item, so it's a table. A list of programming language names carries one piece per item, so it's a bulleted list. A set of term/definition pairs carries two, so it's a description list.

## Key Takeaways
1. Frame instructions around the task; name widgets only when the widget is the point.
2. Bold all named UI elements, using `b` rather than `strong`.
3. Choose list vs. table by pieces-of-data-per-item: one, two, or three-plus.
4. Never use tables for layout, code, or single-column content.
5. Never render text, code, or terminal output as an image.
6. Prefer SVG, then PNG; no transparent backgrounds; no animated GIFs.
7. Cover PII with an opaque overlay and flatten on export — never blur.
8. Replace image maps with text references after the image.

## Connects To
- **Ch 5 (Formatting and Markup)**: bold-for-UI is the primary sanctioned use of bold; `b` vs. `strong` is the semantic-tagging rule.
- **Ch 2 (Structure and Flow)**: the list decision continues the lists guidance.
- **Ch 8 (Accessibility and Inclusion)**: image maps and images-of-text are accessibility failures.
- **Ch 9 (Linking and References)**: image files follow the filename rules.
