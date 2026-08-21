# Chapter 6: Code Documentation

**Source pages**: code-in-text, code-samples, code-syntax, api-reference-comments, placeholders, reference-verbs, format-examples

## Core Idea
Code font is a signal, not decoration: it tells the reader "this is meant to be entered verbatim" and marks exactly where the enterable text starts and stops. Everything else in this chapter follows from making that boundary unambiguous.

## Frameworks Introduced

- **Code font as a boundary marker**: Apply code font to anything code-related in running prose.
  - Why it works: It signals verbatim entry, shows the boundaries of what to type, and separates the entity from surrounding prose.
  - How: HTML `code` element; Markdown backticks.
  - Applies to: attribute names and values, class names, command output, command-line utility names (`gcloud`, `kubectl`, `bq`), data types, database elements (row/column names), filenames, and similar entities.

- **Click-to-copy discipline**: A copyable command example should run as-is after the reader substitutes placeholders.
  - How: Include only runnable code and placeholder variables. Keep out syntax notation — square brackets, pipes, braces, and ellipses — because those characters break the command if the reader doesn't strip them first.
  - Corollary: If a code block contains an omission, don't format it as click-to-copy.

- **Placeholder construction**: Placeholders stand for values the reader must replace (or, in example output, values that simply vary).
  - How: Give each a descriptive uppercase name — `PROJECT_ID`, not a generic stand-in. Avoid a single *x* or a run of *x*'s, except where a run of *x*'s is the domain standard (HTTP status codes like `4xx`).
  - Formatting: Inline in HTML, wrap in the `var` element.
  - Note: In example output, a placeholder like `HTTP_RESPONSE_CODE` marks a varying value the reader isn't expected to set.

- **Third-person verbs in reference docs**: Describe what the method *does*, not what the developer would use it to do.
  - How: "`tasks.insert`: Creates a new task on the specified task list" — not "Create a new task."
  - The whole distinction is the trailing *-s*, and it applies to the main method description.

- **Example placement**: Match the introduction to the example's length and position.
  - Short-to-medium at sentence end: set off with a comma, parentheses, or em dash — "Choose a strong encryption algorithm, such as AES-256." Avoid a semicolon for this.
  - Short, mid-sentence: keep it brief, set off with dashes, commas, or parentheses.
  - Longer: make it its own sentence, using *for example* as an adverb.

## Key Concepts
- **Placeholder**: A named stand-in for a reader-supplied or varying value.
- **Click-to-copy**: A code block the reader copies whole — so it must contain nothing that needs deleting.
- **Document comment**: The source-code comment from which API reference is generated.

## Reference Tables

**Code sample formatting**

| Rule | Value |
|---|---|
| Indentation | Follow the relevant language's code style guide — usually spaces, two per level, though some contexts use four or tabs |
| Line wrap | 80 characters; fewer if readers may use narrow windows or print |
| Block markup | HTML `pre`; Markdown indent every line four spaces |
| Omitted code | A comment in the sample's own language — never `...` or an ellipsis character |

**API reference requirements** — a description is *mandatory* for:
- Every class, interface, struct, and comparable member (including C++ union types)
- Every constant, field, enum, and typedef
- Every method — plus each parameter, the return value, and any exceptions thrown

**Extremely strong suggestions** (adapt per language):
- A ~5–20 line code sample at the top of each class or interface page
- All API names, classes, methods, constants, and parameters in code font, each linked to its reference page
- String literals in code font inside double quotation marks (`"wrap_content"`)
- Class-name spelling matching the code exactly, capitals and all (`ActionBar`)
- Never pluralize a class name — write `Intent` objects or `Activity` instances, not `Intents`

## Worked Example

Documenting a command-line command well, per the best practices:

> To connect to the instance, use the [`gcloud compute ssh` command](https://cloud.google.com/sdk/gcloud/reference/compute/ssh):
> ```
> gcloud compute ssh
> ```

Three things are happening: an inline link to the full command reference, a minimal argument set (rely on the reference for the exhaustive list), and a clean copyable line. Choose the fewest optional arguments that still complete the task in the recommended way.

Introducing examples, contrasting the recommended and rejected forms:

| Recommended | Not recommended |
|---|---|
| Choose a strong encryption algorithm, such as AES-256. | Enter a name for the instance, for example, `my-instance-99`. |
| You can monitor various metrics—for example, CPU utilization, storage capacity, and active connections. | Specify the region for deployment; for example, `us-central1`. |
| Enter a six-digit hex number (for example, `228B22`), and then click **OK**. | Enter a six-digit hex number (for example, if you want the color forest green, enter `228B22`), and then click **OK**. |

The failures are a comma-spliced trailing example, a semicolon used to introduce, and a parenthetical that grew into a full clause.

## Key Takeaways
1. Code font marks verbatim-entry text and its exact boundaries.
2. Keep bracket/pipe/brace/ellipsis notation out of click-to-copy examples.
3. Name placeholders descriptively in uppercase; avoid bare *x* runs outside domain conventions.
4. Mark omitted code with a language-appropriate comment, never `...`.
5. Wrap samples at 80 characters and follow the language's own style guide for indentation.
6. Reference method descriptions take third-person verbs (*Creates*, not *Create*).
7. API reference must document every class, constant, and method — including parameters, returns, and exceptions.
8. Link commands to their full reference and keep inline examples minimal.

## Connects To
- **Ch 5 (Formatting and Markup)**: code font is the third formatting assignment alongside bold and italic.
- **Ch 2 (Structure and Flow)**: commands in a task sequence belong in a numbered procedure.
- **Ch 3 (Punctuation)**: the ban on `...` for omissions is part of the wider ellipsis rule.
- **Ch 11 (Naming and Legal)**: class and product name pluralization rules overlap.
