---
name: research-brief
description: "Write, size and dispatch a research brief for a research agent that collects generalisable empirical facts, not project-specific confirmation. Use when the user invokes /research-brief, asks to prepare/write a research brief, research task, or literature-review brief for an agent to run, or asks to run/dispatch an existing brief. Enforces the fact/design split, prevents logical feedback loops where the research confirms the design back to itself, and picks the run size (quick, standard, deep) and whether the question needs one stage or two."
allowed-tools: [Read, Write, Edit, Bash]
---

# research-brief: briefs that collect facts, not confirmation

A research brief tells a research agent what empirical question to answer. The danger it must design around is the **logical feedback loop**: if the brief carries the project's own framing, the agent retrieves sources shaped like the design and reports them as support, so the design appears to confirm itself on its own reflection. That is not evidence.

This skill produces a brief that collects **method-universal empirical facts** which a human then *consumes* into a design decision. The research supplies inputs; it never concludes the design is right.

The output is a three-part artefact kept together in the source document:
- **AGENT BRIEF**: project-free. The only part research agents see.
- **ROUTING**: human-only. Holds the project context, the verdict-to-action map and any stage-2 condition.
- **DISPATCH**: orchestrator-only. Holds run size, search angles and batch order.

Dispatch only the AGENT BRIEF, plus `references/researcher-protocol.md`.

This skill is often reached mid-conversation, when a topic turns niche. Triage (step 0) is built to be answered from the conversation and the source note alone, without extra reading.

---

## The one rule everything serves

> A fact qualifies for a brief only if it would appear in a textbook, review, or benchmark written by someone who has never heard of this project.

If a returned "fact" is true only because of the project's design choices, it is not a fact, it is the design looking in a mirror. Every rule below exists to enforce this line.

---

## The three parts

### Part 1: AGENT BRIEF (the only thing the agent receives)

Self-contained, project-free, link-free. A stranger with no knowledge of the project could run it and return useful facts. It contains, in order:

1. **Task**: one or two sentences saying what to find, with the instruction to collect facts and not endorse any design.
2. **Question**: the empirical question in general terms (methods, mechanisms, systems). Never scope it to the project's own case as a way to validate that case.
3. **Facts to return**: a bullet list of what counts as a returnable fact. Widen the acceptable systems ("any organism or community", "any field that measures X") so the agent is not steered toward project-shaped sources. Include bounding and negative facts explicitly.
4. **Refuse / out of scope**: the project-shaped questions the agent must refuse. Name the feedback-loop traps here and forbid them.
5. **Deliverable**: a literature review with complete references and verdicts built to the verdict rules (constraint 6).

### Part 2: ROUTING (human dispatcher only; never given to the agent)

Holds everything Part 1 must not:
- which note or decision consumes the verdict
- the committed or expected answer
- project links and the origin of the question
- one line per verdict option saying what the consuming decision does if that option returns (the scope check, procedure step 4)
- the stage-2 condition, if the brief has one (see Stages)

Wikilinks and project names live here.

### Part 3: DISPATCH (orchestrator only; never given to the agent)

The size, the triage answers behind it, the search angles for a deep run, any brief-specific extra instructions, and batch order when several briefs are dispatched together. No project facts go here, because the extra instructions reach the agents.

---

## Hard constraints (check every brief against these)

1. **No project references in the AGENT BRIEF.** No wikilinks, no note names, no "this project", no "our hypothesis", no section numbers. The only acceptable use of the word "project" is in the refusal guard ("do not scope your answer to any specific project").
2. **No outcome in the AGENT BRIEF except a null.** The only permitted statement about what the research will find is a null: that the evidence may not exist, and that reporting "no evidence found" plainly is correct. Everything else is forbidden: a direction ("expected to point in opposite directions"), a likely verdict ("the likely outcome is that X is established only for Y"), a pattern of results, or naming one verdict option as expected. The agent reports the field neutrally; the human checks it against the committed choice in ROUTING. **Follow-up briefs carry the highest risk**, because whoever writes them already knows the earlier result and what the new settings "should" show. Keep that knowledge in ROUTING.
3. **A null is a valid outcome.** When a claim is currently an inference, say so in the Task and instruct the agent to report "no evidence found" plainly rather than manufacture support from indirect sources. The agent must never upgrade an inference to a fact.
4. **Label indirect support as indirect.** If background literature makes a claim plausible but does not test it, the brief must require that it be flagged as indirect, not counted as evidence for the claim.
5. **Deliverable is a literature review with complete, full-text-backed references.**
   - Write a synthesis (what the field shows, where the strongest evidence sits, the bounds and failure modes, how cases relate) that closes with a justified verdict.
   - Every source needs a complete reference: all authors, full title, venue, year, volume/issue/pages where applicable, and DOI (or stable URL/arXiv ID). No bare keys, no partial entries. Give a reference list and in-text markers.
   - **Abstract-only sources are not evidence:** list them as not obtained; they may not support any claim, figure or verdict.
   - **A "not found" must name the search routes used and any limits hit.**
6. **Verdicts are built to be honest.**
   - **Compound briefs** (two or more settings, domains or systems) get one verdict per part, each from its own option set. Never one paired verdict; that is how one well-measured part and one unmeasured part end up called a "disagreement".
   - **Every option set separates** measured-and-positive, measured-and-negative (or unreliable), and **not measured in this setting**. Absence of measurement is its own outcome, never folded into either of the others.
7. **No em or en dashes anywhere in the AGENT BRIEF.** Use commas, colons, periods, or parentheticals. Run the Task and Question prose through clean writing (`humanizer` if available), but keep the bullet structure and field labels; they are correct register for an agent task spec.

---

## Template (copy and fill)

```markdown
#### <BriefID>

> [!abstract] AGENT BRIEF (give this verbatim to the research agent)
> **Task:** <what to find, in general terms>. Collect empirical facts. Do not evaluate or endorse any research design. <only if the claim is an inference: the evidence may not exist; if so, report that plainly.>
>
> **Question:** <the empirical question, stated at the level of methods/mechanisms/systems, not scoped to a specific project's case as validation>.
>
> **Facts to return** (<widen the acceptable systems/fields>):
> - <fact type 1>
> - <fact type 2>
> - <bounding and negative facts: reviews/benchmarks stating the thing has NOT been done, or its limits>
>
> **Refuse / out of scope:** <the project-shaped questions to refuse>. Do not argue that any approach is justified. <if relevant: do not infer the claim from indirect literature and report it as supported.> Report what the literature has and has not shown, with its limits.
>
> **Deliverable: a literature review.** Write a synthesis (not a bare list): what the field shows, where the strongest evidence sits, the bounds and failure modes, how the cases relate. Close with <one verdict | one verdict per part: <part A>, <part B>>, each one of: **<measured and positive>**, **<measured and negative or unreliable>**, or **<not measured in this setting>**, justified by the reviewed evidence, with indirect-only support labelled. Sources read only as abstracts are listed as not obtained and support nothing. Every "not found" names the search routes used. Every source cited must have a **complete reference**: all authors, full title, venue, year, volume/issue/pages where applicable, and DOI (or stable URL/arXiv ID). No bare keys, no partial entries. Provide a reference list and in-text markers.

> [!note] ROUTING (human dispatcher only; do NOT give to the agent)
> <which decision/note consumes the verdict; the committed or expected answer; project links; origin.>
> **If verdict is** <option A> → <what the decision does>. <option B> → <...>. <option C> → <...>.
> **Stage 2:** <none | "if the critic's coverage gaps name <kind of gap>, write a targeted follow-up brief on those, sized separately">

> [!example] DISPATCH (orchestrator only; do NOT give to the agent)
> **Size:** <quick | standard | deep>. Triage: <verdicts>; <practice | evidence>; <cited/limitation/design | not cited>; vocabularies: <list>.
> **Angles** (deep only): <name: vocabulary>; <name: vocabulary>; <...>
> **Extra instructions:** <brief-specific, project-free, or none>
> **Batch order:** <none | runs after <BriefID>>
```

(Callout syntax is for Obsidian/markdown notes. In a plain prompt, headed `AGENT BRIEF`, `ROUTING` and `DISPATCH` blocks work the same way. What matters is the split, not the callout.)

---

## Procedure

0. **Triage.** Answer the four questions below and tell the user the result in one line, for example "Deep: one verdict, three vocabularies, feeds a limitation". If the user downgrades, record it in DISPATCH.
1. **Find the real empirical question.** Read the open point in its source note. Strip it down to the method-universal core: what is true about the method/mechanism/field regardless of this project? That core is the Question. If you cannot state it without naming the project, you have not found the empirical question yet.
2. **Decide honestly whether a null is likely.** Is this a "find what exists" question, or a claim that is currently an inference with likely no direct evidence? If the latter, build the null into the Task. Put any other expectation in ROUTING, never in the brief.
3. **Write the AGENT BRIEF** from the template. Widen the acceptable systems. Write the refusal guard to name the specific feedback-loop traps for this question. Build the verdict options to constraint 6.
4. **Write the ROUTING, and run the scope check.** For each verdict option, write what the consuming decision does if it returns. If two options lead to the same action, or an option answers a different claim from the one the decision needs, the Question is aimed wrong: rewrite it before dispatch. (A brief that asks "can the input be omitted" when the claim is "less of the input is lost" fails here.) Add the stage-2 condition if Stages calls for one.
5. **Write the DISPATCH** from the triage.
6. **Verify (do not skip).** Run the checks below. A brief that fails any of them is not ready.
7. **Clean the prose.** Remove every em/en dash; tighten the Task and Question. Keep bullets and field labels.
8. **Run it** (see Dispatch), then **write the result note** from `references/result-note-template.md` and check the stage-2 condition against the critique.

---

## Triage and run sizes

Four questions, answerable from the conversation and the source note:

1. **How many independent verdicts?** One brief per verdict. Combine parts in one brief only when they share a search space, and then give one verdict per part. Independent briefs go out as a batch.
2. **What kind of question?** *Practice*: what exists, what the field uses. *Evidence*: has it been measured, does evidence exist, does a result hold in a given regime. An evidence question can end in "not found", and "not found" is only as good as the search breadth behind it.
3. **Where does the verdict go?** Into a citation, a limitation statement or a design decision, or nowhere in the document (orientation only)?
4. **How many vocabulary communities publish on it?** List them: groups of researchers who study the phenomenon under different names, journals and review series. A distributed pathway, for example, is "cross-feeding" to microbial ecologists and "incomplete dechlorination" to bioremediation engineers. Each community becomes a search angle.

| Size | Shape | Agents | Choose when |
|---|---|---|---|
| **quick** | researcher | 1 | not cited anywhere, and a practice question, in one vocabulary. Also a stage-1 vocabulary scout. |
| **standard** | researcher, then critic | 2 | anything cited that is not deep |
| **deep** | one search agent per vocabulary (2 or 3), then synthesis, then critic | 4 to 5 | two or more vocabularies, and either an evidence question or a verdict that feeds a limitation or design decision |

- **Anything that will be cited is at least standard.** The critic is the stage that catches unsupported verdicts, missed settings and wrong references; a quick run's output is not citable until critiqued.
- **Split deep angles by vocabulary community, not by sub-question.** Sub-question splits search the same community three times and miss the one that uses different words.
- **Calibration against past briefs:**
  - A fertiliser-emissions fact sourcing brief was cited, but was a practice question in one vocabulary: standard.
  - A set-size-bias regime check is an evidence question across ontology similarity and missing-data statistics: deep with two angles.
  - A distributed-pathway transfer brief is an evidence question across microbial ecology, syntrophy, bioremediation and marine carbon cycling, and feeds a limitation: deep with three angles.

---

## Stages

A **stage** is a brief written after reading an earlier brief's result.

- **One stage** when the Question can be fully written now, in the vocabulary its literature uses.
- **Plan two stages** when:
  - the right Question depends on vocabulary or landscape not yet known. Stage 1 is then a quick scout ("what terms, measures and review series does this field use"), and stage 2 is the real brief.
  - the size is deep and the verdict may be "not found" or "not measured". The critic's coverage gaps are then the likely trigger for a targeted follow-up.
- **Write stage 2 into ROUTING as a condition on the critique**, never as an expected result: "if the critic's coverage gaps name specific settings or classes, write a follow-up brief on those". The workflow returns `critique.coverage_gaps` with each gap's setting named, so the check is mechanical.
- **Follow-up briefs stand alone.** They assume no earlier brief, name the gap settings neutrally, and never say what earlier results found or what the new settings are expected to show (constraint 2).
- **Re-scoping is not a stage.** If a result shows the Question was aimed wrong, that is a failed scope check (procedure step 4); fix the check habit, not just the brief.

---

## Dispatch

Running a brief uses the workflow shipped with this skill, `workflows/research-run.js`. Invoking this skill to run a brief is the user's opt-in to that workflow, but state the size line first so they can downgrade.

1. Read `references/researcher-protocol.md` (installed copy: `~/.claude/skills/research-brief/references/researcher-protocol.md`).
2. Call the Workflow tool with `scriptPath` set to the absolute path of the installed `~/.claude/skills/research-brief/workflows/research-run.js`, and `args` as a JSON object (not a string):
   - `brief`: the AGENT BRIEF text only, callout markers stripped. Never ROUTING or DISPATCH.
   - `protocol`: the full protocol text.
   - `size`: `quick`, `standard` or `deep`.
   - `angles`: for deep, `[{ "name": "...", "vocabulary": "..." }]`, from DISPATCH.
   - `extra`: the DISPATCH extra instructions, as a list of strings (may be empty).
   - `verdictOptions`: optional list of the option strings, to pin the synthesis to them.
3. **Batches:** run each brief as its own workflow call. Independent briefs can run concurrently; briefs with a batch order wait for their predecessor.
4. **On return,** write the result note from `references/result-note-template.md`. If `critique.verdict_supported` is `partial` or `no`, lead with the reformulated verdict. Then check the ROUTING stage-2 condition against `critique.coverage_gaps` and tell the user whether it fired.

---

## Verification (run before dispatching any brief)

Extract just the AGENT BRIEF blocks and prove they are clean. Adjust the file path.

```bash
FILE="path/to/your/briefs.md"
TMP="${CLAUDE_JOB_DIR:-${TMPDIR:-/tmp}}/ab.$$.txt"
# Pull only the AGENT BRIEF callout blocks (stop at ROUTING or DISPATCH)
awk '/> \[!abstract\] AGENT BRIEF/{f=1} /> \[!note\] ROUTING|> \[!example\] DISPATCH/{f=0} f' "$FILE" > "$TMP"

echo "=== (1) project leakage (want: 0 wikilinks, 0 self-references) ==="
grep -c '\[\[' "$TMP"; echo "^ wikilinks (must be 0)"
grep -ciE 'this project|our hypothesis|this study' "$TMP"; echo "^ self-references (must be 0)"
# 'project' alone is allowed ONLY in the refusal guard ("any specific project"); inspect any hit:
grep -niE 'project' "$TMP" | grep -viE 'any specific project|a specific project' || echo "  (no stray 'project' uses)"

echo "=== (2) dashes (want: none) ==="
grep -nE '—|–' "$TMP" && echo "DASHES FOUND ^ remove them" || echo "clean"

echo "=== (3) stated outcomes (inspect every hit) ==="
grep -noiE '[^.]*(expect|likely|anticipat|point(s|ing)? (toward|in)|should (show|find|confirm)|we think)[^.]*' "$TMP" || echo "  (no outcome language)"

rm -f "$TMP"
```

Checks 1 and 2 must pass outright: zero wikilinks, zero self-references, zero dashes. The only permitted "project" mentions are the generic refusal guard.

Check 3 needs judgement. A hit may stay **only if it is a null**: the evidence may not exist, no such study is expected, report absence plainly. A hit that names a direction, a pattern of results, or one of the verdict options fails constraint 2; move it to ROUTING.

Also confirm by eye:
- each part of a compound brief has its own verdict;
- each option set has a "not measured in this setting" option;
- the ROUTING has a verdict-to-action line per option.

---

## Worked example (a brief that passes)

> [!abstract] AGENT BRIEF (give this verbatim to the research agent)
> **Task:** Find whether the published literature contains any direct, head-to-head empirical comparison of two predictor types under a given structural condition. Such direct evidence may not exist. If so, report that plainly and do not manufacture support from indirect sources. Collect empirical facts.
>
> **Question:** When system X is structured rather than uniform, how does prediction error behave for (a) models that explicitly represent mechanism M and (b) models that use only aggregate features? Is there a controlled benchmark comparing them as structure varies?
>
> **Facts to return:**
> - Any study that directly compares the two model types on the same structured system, reporting how each one's accuracy changes with structure. This is the primary target.
> - How the uniform assumption biases the mechanistic models: magnitude, direction, conditions.
> - The general finding that <related background>. **Label this as INDIRECT background, not evidence for the head-to-head claim.**
>
> **Refuse / out of scope:** do not answer whether any specific approach is "defensible". Gather only whether general head-to-head evidence exists. **Do not infer the comparative claim from the indirect literature and report it as supported.** If no direct benchmark exists, the correct answer is that no head-to-head evidence exists.
>
> **Deliverable: a literature review.** Synthesise what direct comparisons exist if any, what the uniform assumption biases and by how much, and which findings are direct versus indirect. Close with one verdict: **direct comparative evidence found**, **only indirect evidence**, or **no comparison has been measured**, justified by the reviewed evidence, with any indirect-only support labelled. Sources read only as abstracts are listed as not obtained and support nothing. Every "not found" names the search routes used. Complete references for every source (all authors, title, venue, year, volume/issue/pages, DOI or stable ID); reference list plus in-text markers.

> [!note] ROUTING (human dispatcher only; do NOT give to the agent)
> Feeds [[the relevant design note]]. Expected: no direct comparison exists.
> **If verdict is** direct evidence found → cite it and state claim C as supported. Only indirect → claim C stays an inference, background cited as indirect. Not measured → claim C stays an inference the project's own experiment must test, never a cited fact.
> **Stage 2:** if the critic's coverage gaps name a field that benchmarks the two model types under another name, write a follow-up brief on that field.

> [!example] DISPATCH (orchestrator only; do NOT give to the agent)
> **Size:** deep. Triage: one verdict; evidence question; feeds a design note; vocabularies: mechanistic modelling, machine-learning benchmarking, spatial ecology.
> **Angles:** mechanistic: process-based and constraint-based model validation; ml: predictive benchmark and out-of-distribution evaluation; spatial: spatially structured ecosystem prediction.
> **Extra instructions:** none.

Notice:
- The AGENT BRIEF names no project, no note and no committed answer, and states only the null.
- The expectation, the verdict-to-action map and the stage-2 condition all live in ROUTING.
- The size and angles live in DISPATCH.

That separation is the whole skill.

---

## What this skill does NOT do

- It does not let the agent reach a design conclusion. The verdict is an input; a human decides.
- It does not accept project framing inside the AGENT BRIEF. If a brief needs a project detail to make sense, that detail belongs in ROUTING, or the Question is not yet general enough.
- It does not fix search reach. Sources the agents cannot read in full are reported as not obtained, and a "not found" is a statement about the search routes used.
