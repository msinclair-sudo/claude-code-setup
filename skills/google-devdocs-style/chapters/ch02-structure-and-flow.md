# Chapter 2: Structure and Flow

**Source pages**: paragraph-structure, sentence-structure, headings, headings-targets, lists, procedures, index

## Core Idea
Readers scan; they don't read every word. Put the most important information first at every level — sentence, paragraph, and page — and state the condition before the instruction so readers can skip what doesn't apply to them.

## Frameworks Introduced

- **Condition before instruction**: Lead with the circumstance, condition, or goal; put the action second.
  - When to use: Any sentence telling the reader to do something.
  - How: "To delete the entire document, click **Delete**" — not "Click **Delete** if you want to delete the entire document."
  - Why it works: The reader who doesn't want to delete the document stops reading at the comma. Instruction-first forces everyone to read the whole sentence to learn it doesn't apply.

- **Task-based vs. conceptual headings**: Match the heading's grammar to the section's content type.
  - How: Task sections take a bare infinitive ("Create an instance"). Conceptual sections take a noun phrase that doesn't start with *-ing* ("Migration to Google Cloud"). Prefix genuinely optional sections with `Optional:` at the *front* — "Optional: Customize your alias," not "Customize your alias (optional)."
  - Mixing both styles in one document is fine; match each heading to its own section.

- **List type selection**: Choose by the nature of the item set, not by appearance.
  - Numbered (`ol`) — sequence is significant: ordered steps, phases, priorities. Nested levels go lowercase letters, then lowercase Roman numerals.
  - Bulleted (`ul`) — no sequence: non-sequential options or examples. Make clear whether every item is required.
  - Description list (`dl`/`dt`/`dd`) — terms each with a definition; use when drawing attention to two or more terms, glossary-style.
  - Description list with bulleted run-in headings (`ul`) — introductory terms each followed by an explanation; use to highlight several concepts or save space.

- **Reference hierarchy**: When this guide is silent, consult sources in a fixed order.
  - How: (1) Project-specific style — including deliberate exceptions to this guide. (2) This style guide. (3) Third-party references by question type: spelling → Merriam-Webster; nontechnical style → *The Chicago Manual of Style*, 17th ed.; technical style → Microsoft Writing Style Guide (but check whether the guidance is Microsoft-product-specific).
  - At any stage, established usage helps — search your organization's existing docs or a corpus like Google Ngram Viewer.

## Key Concepts
- **Bare infinitive**: The plain base form of a verb ("Create"); identical in appearance to the imperative, and the correct opening for task headings.
- **Custom anchor**: A hand-authored `id` on a heading, insulating inbound links from later heading edits.
- **Run-in heading**: A bolded lead term inside a list item, followed by its explanation.
- **Single-step procedure**: A one-action task — formatted as a bullet, never as a numbered list of one.

## Mental Models
- **Treat 5–6 sentences as a smell, not a limit**: A longer paragraph usually signals too many ideas — but a single-idea paragraph may legitimately run long, and a one-sentence paragraph is fine. Never lengthen sentences to reduce sentence count.
- **One `h1` per page, and don't echo it**: If the page title is "Create and start VM instances," the sections are "Create a VM" and "Start a VM" — not a repeat of the title.
- **Anchors outlive headings**: Auto-generated anchors break when heading text changes. Add a custom anchor to anything likely to be linked.

## Reference Tables

| Element | Rule |
|---|---|
| Paragraph alignment | Left-align. Never center, full-justify, or right-align. |
| Line breaks | Never force hard returns inside sentences or paragraphs — they break on resize and at larger text sizes. |
| Multi-paragraph list items | Use `p` elements, not `br`. |
| List introduction | Complete sentence, not a fragment completed by the items. Colon if the list immediately follows; period if other material intervenes. |
| Single-item list | Don't. Use other formatting to set the item off. |
| Anchor text | Lowercase, hyphens between words. |

## Worked Example

Introducing a procedure — the failure is the sentence fragment that the numbered steps complete:

- **Not recommended**: "To customize the buttons:"
- **Recommended**: "To customize the buttons, follow these steps:"
- **Also recommended**: "Customize the buttons:"
- **Also recommended**: "To customize the buttons, do the following:"

A single-step procedure demonstrates the same instinct — resist the numbered-list reflex:

- **Recommended**: A lone bullet — "To clear (flush) the entire log, click **Clear logcat**."
- **Not recommended**: An introductory line "follow this step:" above a numbered list containing exactly one item.

Adding a custom anchor in HTML, so the link target survives a heading rewrite:

```html
<section id="introduction-to-everything">
<h2>Introduction to everything</h2>
...
</section>
```

## Key Takeaways
1. Condition first, instruction second — let readers skip what doesn't apply.
2. Critical information leads the sentence, the paragraph, and the page.
3. Task headings start with a base-form verb; concept headings are noun phrases. Avoid opening any heading with an *-ing* form — it translates inconsistently and inflates character counts. (*Billing*, *Pricing* and similar are acceptable when no alternative exists.)
4. Put `Optional:` at the start of a heading, not in trailing parentheses.
5. Pick list type by whether sequence matters and whether items are terms-with-definitions.
6. Format single-step procedures as a bullet.
7. When the guide is silent, walk the reference hierarchy in order.

## Connects To
- **Ch 1 (Voice and Tone)**: imperative mood in running prose often signals content that belongs in a procedure.
- **Ch 10 (UI and Visuals)**: the list-or-table decision is resolved on the tables page.
- **Ch 9 (Linking and References)**: custom anchors are the target side of cross-referencing.
- **Ch 5 (Formatting and Markup)**: semantic elements (`ol`, `ul`, `dl`) carry the structural meaning described here.
