# Patterns and Techniques

Reusable methods from the guide. Each is a procedure you can run, not a rule to memorize.

## The Jargon Filter
**When to use**: Any specialized or figurative term.
**How**: Ask in order — (1) Can you write around it? (2) Is there a more specific replacement? (3) Used once → define in plain language with the term parenthesized, or link a trusted definition. (4) Used throughout → gloss briefly on first reference. (5) In a command or code sample → use only in direct reference to the code item, in code font.
**Trade-offs**: Some jargon carries real SEO value because readers search for it. This filters rather than bans — but terms marked "Don't use" in the word list get replaced regardless.

## The Excessive-Claim Test
**When to use**: Any statement about performance, cost, security, or a competitor.
**How**: Would a reader be unable to verify it? Would one incident falsify it? Could it read as subjective or disparaging? Judge against what may be true in the *future*, not just today.
**Trade-offs**: Hedged phrasing ("helps with security") is weaker marketing but survives contact with reality. Cite sources when making specific performance claims.

## Condition Before Instruction
**When to use**: Every sentence telling the reader to act.
**How**: Lead with the circumstance, condition, or goal; put the action second. "To delete the entire document, click **Delete**."
**Trade-offs**: Slightly longer sentences, but readers who don't need the step can stop at the comma.

## The Auxiliary Verb Decision
**When to use**: Any sentence where you're tempted to write *should*.
**How**: Decide whether the action is required (*must* or an imperative), recommended (*We recommend…*), or optional (*can*); whether an outcome is expected (state it) or possible (*might*/*can*).
**Trade-offs**: Forces a judgment the writer may have been avoiding — which is the point. *should* is acceptable only for generally recognized practices.

## Notice Triage
**When to use**: Before offsetting anything as a Note, Caution, or Warning.
**How**: Write the content as ordinary body text first. Then decide whether it earns the interruption. Escalate by severity: Note (useful aside) → Caution (proceed carefully) → Warning (don't do this / risk of harm).
**Trade-offs**: Readers skip elements outside their focus, and stacked notices lose distinctiveness. Two notices in a row means the content needs reorganizing, not more notices.

## Screen Reader Self-Edit
**When to use**: Before publishing any substantial page.
**How**: Navigate the page with the keyboard alone; then run a screen reader over it. Check that heading levels don't skip, that link text means something out of context, and that meaning survives without punctuation.
**Trade-offs**: Takes real time, but doubles as a general editing pass — it surfaces vague link text and broken hierarchy that visual review misses.

## Translation Simplification Pass
**When to use**: Any document that may be translated or read by non-native English speakers.
**How**: Replace fancy words with simple ones (*use* not *utilize*); collapse phrases to single words (*many* not *a number of*); split sentences over ~26 words; remove phrasal verbs where a simple verb exists; cap noun-modifier stacks at two; move *only* next to what it modifies.
**Trade-offs**: None worth the name — shorter sentences also reduce translation cost and review time.

## The List-or-Table Decision
**When to use**: Presenting a set of similarly structured items.
**How**: Count the pieces of data per item — one → bulleted/numbered list; two → description list (or table in some contexts); three or more → table.
**Trade-offs**: Tables are for genuinely two-dimensional data. Never use one to column-split a long one-dimensional list, and avoid tables inside numbered procedures.

## Click-to-Copy Construction
**When to use**: Any command example the reader will copy.
**How**: Include only runnable code plus placeholder variables. Strip syntax notation — `[]`, `|`, `{}`, `...` — since those break the command if pasted. Link to the full command reference for the exhaustive argument list; include the fewest optional arguments that accomplish the task.
**Trade-offs**: You can't show optionality inline, which is exactly why the reference link is mandatory.

## Irreversible PII Redaction
**When to use**: Any screenshot containing personal or identifying data.
**How**: Cover with a solid-color overlay at 100% opacity. Flatten on export to layered formats (PDF, TIFF).
**Trade-offs**: None. Blur and mosaic effects are reversible and must never be used for this.

## Timeless Rewrite
**When to use**: Product documentation (not release notes or blog posts).
**How**: Delete *now*, *new*, *currently*, *at present*, *as of this writing*, *eventually*. Describe how the product works today, without comparing to past versions or hinting at future ones.
**Trade-offs**: Loses the ability to signal recency — which is the goal. Time-based words stay legitimate in time-stamped content and in state-change descriptions ("goes offline soon after…").
