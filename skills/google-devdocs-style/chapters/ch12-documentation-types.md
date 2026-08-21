# Chapter 12: Documentation Types and Stance

**Source pages**: prescriptive-documentation, timeless-documentation

## Core Idea
Take a position and write it so it stays true. Prescriptive documentation recommends a path instead of listing options; timeless documentation describes how the product works now, without anchoring to a moment or assuming knowledge of past versions.

## Frameworks Introduced

- **Prescriptive (opinionated) documentation**: Tell readers what to do rather than enumerating choices. When a goal involves multiple approaches or products, recommend a path.
  - What it changes: **Purpose and structure** — the document states a clear, specific purpose and its headings serve that purpose. **Scenarios and procedures** — reflect the use cases most likely relevant to readers. **Sample commands** — provide the commands and arguments that accomplish the most common use case.
  - Typical form: best-practice documents are usually prescriptive.

- **Auxiliary verb selection**: Choose the verb that matches the actual obligation — and generally avoid *should*.
  - Why avoid *should*: It implies recommended-but-optional, leaving readers unsure whether to act.
  - To resolve it, decide whether the action is *required* vs. *optional*, the outcome *expected* vs. *possible*, the state *actual* vs. *recommended*.

- **Timeless documentation**: Document the current version, not the change history or the roadmap.
  - Why it works: Reduces maintenance, and stops assuming the reader knows earlier versions.
  - Avoid: *now*, *new*, *currently*, *at present*, *as of this writing*, *eventually* — words that make the text inaccurate or meaningless once time passes, and that can prematurely disclose plans.
  - Legitimate exceptions: time-stamped content — press releases, blog posts, release notes — where *new* is accurate ("Dataflow includes several new features"). Also fine in procedural content marking a state change: "The VM goes offline soon after you send the shutdown command."

## Key Concepts
- **Prescriptive / opinionated documentation**: Recommends one way to accomplish a task rather than presenting options.
- **Timeless documentation**: Text free of temporal anchors and version-comparison framing.

## Reference Tables

**Auxiliary verb decision table**

| Situation | Use | Example |
|---|---|---|
| Action is required | *must*, or a clear imperative | "Do the following before you continue." |
| Action is recommended | *We recommend…* / *Google recommends…* | *should* is acceptable only for generally recognized practices: "You should use a strong password." |
| Action is optional | *can* | "You can also use approach B to solve the same problem." |
| Outcome is expected | describe it directly | "The process returns 10 items." |
| Outcome is possible | *might* or *can* | "The process can take about 30 minutes." |

**Timeless rewrites**

| Recommended | Not recommended |
|---|---|
| These subcommands let you interact with HTTP load balancing. | These **new** subcommands let you… |
| The following command-line options aren't supported: | …aren't **currently** supported: |
| The emulator supports the following filters: | The emulator **now** supports… |

## Worked Example

The three rewrites above share one mechanism: deleting the temporal word costs nothing and removes a maintenance liability. "These new subcommands" is accurate for perhaps one release cycle; "These subcommands" stays accurate indefinitely, and no reader was ever helped by the word *new* in a reference page.

Applying the auxiliary-verb table to a single ambiguous sentence — "You should configure a service account before deploying" — forces a decision the writer was avoiding:

- If deployment *fails* without it: "You **must** configure a service account before you deploy."
- If it's a widely recognized good practice: "**We recommend** configuring a service account before you deploy."
- If it's genuinely one option among several: "You **can** configure a service account before you deploy."

The original sentence let the writer skip that judgment; each rewrite makes the obligation legible to the reader.

## Key Takeaways
1. Recommend a path; don't enumerate every option.
2. Replace *should* with *must*, *We recommend*, or *can* after deciding the actual obligation.
3. Use *might* or *can* for possible outcomes; state expected outcomes plainly.
4. Document the current version — not what changed, not what's coming.
5. Strip *now*, *new*, *currently*, *at present*, *eventually* from product documentation.
6. Time-based words are fine in release notes, blog posts, and state-change descriptions.

## Connects To
- **Ch 1 (Voice and Tone)**: present tense and the ban on documenting future features are the sentence-level expression of timelessness.
- **Ch 6 (Code Documentation)**: prescriptive sample commands use the fewest optional arguments.
- **Ch 2 (Structure and Flow)**: a clear document purpose drives heading choices.
