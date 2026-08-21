# Chapter 1: Voice and Tone

**Source pages**: voice, tone, person, pronouns, contractions, anthropomorphism, jargon, excessive-claims, philosophy, future, tense

## Core Idea
Write as a knowledgeable friend who understands what the developer is trying to do — conversational but not chatty, precise but not pedantic. The reader is usually in a hurry and looking for one specific thing.

## Frameworks Introduced

- **Active voice by default**: Make the doer the grammatical subject.
  - When to use: Nearly always. Passive hides *who acts*, leaving readers unsure whether they, the server, or an end user is responsible.
  - How: Recast so the actor leads — "Send a query to the service," not "The service is queried."
  - Legitimate exceptions: emphasizing the object over the action ("The file is saved"); de-emphasizing a blamed actor ("Over 50 conflicts were found" beats "You created over 50 conflicts"); or when the actor genuinely doesn't matter.
  - Why it works: Adding *by you* to fix passive produces worse prose than recasting. If you need *by*, recast instead.

- **Second person for the reader, third for the software**: Address the reader as *you*; reserve *user* for the user of the software your reader is building.
  - When to use: Every document. The distinction matters most in API docs.
  - How: State facts about programming elements in third person; switch to *you* when telling the reader to act. Use the imperative for instructions — the *you* is implied.
  - Watch for: Imperative text buried in running prose. If you're issuing a sequence of commands, it probably belongs in a numbered procedure.

- **The jargon decision sequence**: Five questions, in order, before allowing a specialized term.
  - How: (1) Can you write around it? (2) Can you replace it with a more specific term? (3) Used once — define in plain language with the term in parentheses, or link a trusted definition. (4) Used throughout — gloss briefly on first reference. (5) In a command or code sample — use it only in direct reference to the code item, formatted as code.
  - Why it works: Jargon is figurative by nature, so it translates badly and gates comprehension on group membership. But some jargon carries real SEO value — readers search for it — so this is a filter, not a ban.

- **Excessive-claim test**: An assertion is an excessive claim if it (a) states performance or cost the reader can't verify, (b) states security that a single incident would falsify, or (c) could read as subjective or disparaging about a third party.
  - How: Judge against what might be true *in the future*, not just today. Cite sources for specific performance numbers. Prefer "helps with security" or "designed for security" over "prevents" — those survive an incident.
  - Avoid: *best*, *simplest*, *fastest*, *never*, *always*; use *ensure* and *guarantee* only when the thing is genuinely guaranteed.

## Key Concepts
- **Anthropomorphism**: Attributing human qualities to software or hardware — a Delimiter *specifies*, it doesn't *tell*; a PC *detects*, it doesn't *see*.
- **Excessive claim**: An unverifiable, falsifiable, or disparaging assertion about performance, cost, or security.
- **Jargon**: Specialized, often figurative terminology meaningful only inside a specific group — including vague overloaded terms like *solution*, *support*, *workload*.
- **Singular *they***: The gender-neutral pronoun of record; long-established in English usage.
- **Antecedent**: The noun a pronoun replaces; ambiguity here is the most common pronoun failure.

## Mental Models
- **Think of tone as a three-point scale**: too informal / just right / too formal. The target is the middle column — "This API lets you collect data about what your users like."
- **Use the "what am I trying to say?" reset**: When a sentence resists you, step back and answer that question plainly. The spoken answer is usually the sentence you wanted.
- **Read it aloud**: If a sentence is awkward or confusing when spoken, it's probably worth recasting. Not every sentence must sound natural spoken — these are written documents — but the awkward ones are signal.
- **Treat negation contractions as a safety feature**: Readers scanning a page miss a standalone *not*; *don't* is much harder to misread as *do*.

## Anti-patterns
- **Placeholder politeness**: *please* in instructions overdoes it — "click **View**," not "please click **View**."
- **Hedge phrases**: *please note*, *at this time* add length without meaning.
- **Difficulty minimizers**: *simply*, *easy*, *quickly*, *it's that simple* in a procedure — they insult the reader who is stuck.
- **Nonstandard contractions**: invented forms like *guides're*, or three-word stacks like *mightn't've*.
- **Bare demonstratives**: "Set this to true" — follow *this*/*these* with a noun: "Set this value to true."
- **Gendered generics**: *he/she*, *(s)he*, and similar punctuation tricks; use singular *they*.
- **Hypothetical *would***: "The server would then remove you" — use present tense.
- **Future features**: Don't pre-announce anything without legal approval.
- **Monotonous sentence openings**: every sentence starting *You can* or *To do*.
- **Also avoid**: exclamation points, pop-culture references, internet abbreviations (*tl;dr*, *ymmv*), figurative and ableist language, *let's* phrasing, and forced wackiness.

## Worked Example

Google's tone calibration, showing the same content at three registers:

| Too informal | Just about right | Too formal |
|---|---|---|
| Dude! This API is totally awesome! | This API lets you collect data about what your users like. | The API documented by this page may enable the acquisition of information pertaining to user preferences. |
| Then—BOOM—just garbage-collect, and you're golden. | To clean up, call the `collectGarbage` method. | Please note that completion of the task requires the following prerequisite: executing an automated memory management function. |

The middle column names the concrete action and the exact method. The left column buries it in personality; the right column buries it in nominalization.

Applying the excessive-claim test to a performance statement:

- **Fails**: "Our product is faster than ExampleCorp's product." — unverifiable, comparative, and possibly false after their next release.
- **Passes**: "Our product distributes datasets and computation in memory across a cluster, and therefore it can be faster for this scenario than ExampleCorporation's product. For more information, see Performance comparison." — mechanism stated, scenario scoped, source cited.

## Key Takeaways
1. Default to active voice; if fixing passive requires *by you*, recast the sentence instead.
2. *You* = the reader. *User* = the user of the software the reader is building. Never blur them.
3. Use present tense for general behavior; reserve *will* for genuinely later events (async delivery, next backup run).
4. Prefer contractions, especially negative ones — *don't* is scannable in a way *do not* isn't.
5. Run specialized terms through the five jargon questions before keeping them.
6. Write claims that stay true over the document's lifespan; "helps with security" survives an incident that "prevents" doesn't.
7. Software doesn't see, think, want, or know. Pick a precise verb.

## Connects To
- **Ch 8 (Accessibility and Inclusion)**: figurative language, ableist idiom, and global-audience concerns extend the jargon and anthropomorphism rules.
- **Ch 12 (Documentation Types)**: timeless documentation is the structural counterpart to present tense and the ban on future features.
- **Ch 2 (Structure and Flow)**: imperative mood in running text is often a signal that content belongs in a numbered procedure.
- **word-list.md**: the authoritative per-term rulings, including which jargon is marked "Don't use."
