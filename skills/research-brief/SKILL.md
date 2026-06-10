---
name: research-brief
description: "Write a research brief for a research agent that collects generalisable empirical facts, not project-specific confirmation. Use when the user invokes /research-brief, or asks to prepare/write a research brief, research task, or literature-review brief for an agent to run. Enforces the fact/design split and prevents logical feedback loops where the research confirms the design back to itself."
allowed-tools: [Read, Write, Edit]
---

# research-brief: briefs that collect facts, not confirmation

A research brief tells a research agent what empirical question to answer. The danger it must design around is the **logical feedback loop**: if the brief carries the project's own framing, the agent retrieves sources shaped like the design and reports them as support, so the design appears to confirm itself on its own reflection. That is not evidence.

This skill produces a brief that collects **method-universal empirical facts** which a human then *consumes* into a design decision. The research supplies inputs; it never concludes the design is right.

The output is a two-part artefact: an **AGENT BRIEF** (project-free, the only part the agent sees) and a **ROUTING** note (human-only, holds the project context). Keep them together in the source document; dispatch only the AGENT BRIEF.

---

## The one rule everything serves

> A fact qualifies for a brief only if it would appear in a textbook, review, or benchmark written by someone who has never heard of this project.

If a returned "fact" is true only because of the project's design choices, it is not a fact, it is the design looking in a mirror. Every rule below exists to enforce this line.

---

## The two parts

### Part 1 — AGENT BRIEF (the only thing the agent receives)

Self-contained, project-free, link-free. A stranger with no knowledge of the project could run it and return useful facts. It contains, in order:

1. **Task** — one or two sentences: what to find, and the instruction to collect facts and not endorse any design.
2. **Question** — the empirical question stated in general terms (methods, mechanisms, systems), never scoped to the project's specific case as a way to validate it.
3. **Facts to return** — a bullet list of what counts as a returnable fact. Widen the acceptable systems ("any organism or community", "any field that measures X") so the agent is not steered toward project-shaped sources. Include bounding and negative facts explicitly.
4. **Refuse / out of scope** — the project-shaped questions the agent must refuse. This is where you name the feedback-loop traps and forbid them.
5. **Deliverable** — a literature review with complete references (see below).

### Part 2 — ROUTING (human dispatcher only; never given to the agent)

Holds everything Part 1 must not: which note or decision consumes the verdict, the committed/expected answer, project links, the origin of the question. This is where wikilinks and project names live. Label it clearly so no one pastes it into the agent's prompt.

---

## Hard constraints (check every brief against these)

1. **No project references in the AGENT BRIEF.** No wikilinks, no note names, no "this project", no "our hypothesis", no section numbers. The only acceptable use of the word "project" is in the refusal guard ("do not scope your answer to any specific project").
2. **No predetermined answer in the AGENT BRIEF.** If a design decision is already committed, the agent must not be told what it is. It reports the field's practice neutrally; the human checks it against the committed choice in ROUTING. Telling the agent the answer guarantees confirmation bias.
3. **The expected outcome may be "no evidence exists".** When a claim is currently an inference, say so in the Task and instruct the agent to report "no evidence found" plainly rather than manufacture support from indirect sources. A null result is a valid, often correct, deliverable. The agent must never upgrade an inference to a fact.
4. **Label indirect support as indirect.** If background literature makes a claim plausible but does not test it, the brief must require that it be flagged as indirect, not counted as evidence for the claim.
5. **Deliverable is a literature review with complete references.** Not a bare list. A written synthesis (what the field shows, where the strongest evidence sits, the bounds and failure modes, how cases relate), closing with a justified verdict. Every source needs a complete reference: all authors, full title, venue, year, volume/issue/pages where applicable, and DOI (or stable URL/arXiv ID when none exists). No bare citation keys, no partial entries. Reference list plus in-text markers.
6. **No em or en dashes anywhere.** Use commas, colons, periods, or parentheticals. (Run the prose through clean writing: cut filler, active voice, vary rhythm. If `write-pass` / `deslop` are available, apply them to the Task and Question prose, but keep the bullet structure of the brief intact, since bullets and field labels are correct register for an agent task spec, not slop.)

---

## Template (copy and fill)

```markdown
#### <BriefID>

> [!abstract] AGENT BRIEF (give this verbatim to the research agent)
> **Task:** <what to find, in general terms>. Collect empirical facts. Do not evaluate or endorse any research design. <if the claim is an inference: state the expected null and that reporting "no evidence" plainly is correct.>
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
> **Deliverable: a literature review.** Write a synthesis (not a bare list): what the field shows, where the strongest evidence sits, the bounds and failure modes, how the cases relate. Close with one verdict: **<verdict option A>**, **<option B>**, or **<option C>**, justified by the reviewed evidence<, with any indirect-only support labelled as such>. Every source cited must have a **complete reference**: all authors, full title, venue, year, volume/issue/pages where applicable, and DOI (or stable URL/arXiv ID when none exists). No bare keys, no partial entries. Provide a reference list and in-text markers.

> [!note] ROUTING (human dispatcher only; do NOT give to the agent)
> <which decision/note consumes the verdict; the committed or expected answer; project links; origin of the question.>
```

(Callout syntax above is for Obsidian/markdown notes. In a plain prompt, two headed blocks — `AGENT BRIEF` and `ROUTING` — work the same way. What matters is the split, not the callout.)

---

## Procedure

1. **Find the real empirical question.** Read the open point in its source note. Strip it down to the method-universal core: what is true about the method/mechanism/field regardless of this project? That core is the Question. If you cannot state it without naming the project, you have not found the empirical question yet.
2. **Decide the expected outcome honestly.** Is this a "find what exists" question, or a claim that is currently an inference with likely no direct evidence? If the latter, build the null into the Task so the agent is not pressured to manufacture support.
3. **Write the AGENT BRIEF** from the template. Widen the acceptable systems. Write the refusal guard to name the specific feedback-loop traps for this question.
4. **Write the ROUTING** with everything the brief had to exclude: the consuming decision, the committed/expected answer, project links.
5. **Verify (do not skip).** Run the two automated checks below. A brief that fails either is not ready.
6. **Clean the prose.** Remove every em/en dash; tighten the Task and Question. Keep bullets and field labels.

---

## Verification (run before dispatching any brief)

Extract just the AGENT BRIEF blocks and prove they are clean. Adjust the file path.

```bash
FILE="path/to/your/briefs.md"
# Pull only the AGENT BRIEF callout blocks (stop at ROUTING)
awk '/> \[!abstract\] AGENT BRIEF/{f=1} /> \[!note\] ROUTING/{f=0} f' "$FILE" > /tmp/ab.txt

echo "=== (1) project leakage in AGENT BRIEFs (want: 0 wikilinks, 0 project-name hits) ==="
grep -c '\[\[' /tmp/ab.txt; echo "^ wikilinks (must be 0)"
grep -ciE 'this project|our hypothesis|this study' /tmp/ab.txt; echo "^ self-references (must be 0)"
# 'project' alone is allowed ONLY in the refusal guard ("any specific project"); inspect any hit:
grep -niE 'project' /tmp/ab.txt | grep -viE 'any specific project|a specific project' || echo "  (no stray 'project' uses)"

echo "=== (2) dashes anywhere in the briefs (want: none) ==="
grep -nE '—|–' /tmp/ab.txt && echo "DASHES FOUND ^ remove them" || echo "clean"
```

Both checks must pass: zero wikilinks, zero self-references, zero dashes. The only permitted "project" mentions are the generic refusal guard.

---

## Worked example (a brief that passes)

> [!abstract] AGENT BRIEF (give this verbatim to the research agent)
> **Task:** Find whether the published literature contains any direct, head-to-head empirical comparison of two predictor types under a given structural condition. The expected outcome is that no such direct evidence exists. If so, report that plainly and do not manufacture support from indirect sources. Collect empirical facts.
>
> **Question:** When system X is structured rather than uniform, how does prediction error behave for (a) models that explicitly represent mechanism M and (b) models that use only aggregate features? Is there a controlled benchmark comparing them as structure varies?
>
> **Facts to return:**
> - Any study that directly compares the two model types on the same structured system, reporting how each one's accuracy changes with structure. This is the primary target and is likely rare or absent.
> - How the uniform assumption biases the mechanistic models: magnitude, direction, conditions.
> - The general finding that <related background>. **Label this as INDIRECT background, not evidence for the head-to-head claim.**
>
> **Refuse / out of scope:** do not answer whether any specific approach is "defensible". Gather only whether general head-to-head evidence exists. **Do not infer the comparative claim from the indirect literature and report it as supported.** If no direct benchmark exists, the correct answer is that no head-to-head evidence exists.
>
> **Deliverable: a literature review.** Synthesise what direct comparisons exist if any, what the uniform assumption biases and by how much, and which findings are direct versus indirect. Close with one verdict: **direct evidence found**, **only indirect evidence**, or **no evidence exists**, justified by the reviewed evidence, with any indirect-only support labelled. Complete references for every source (all authors, title, venue, year, volume/issue/pages, DOI or stable ID); reference list plus in-text markers.

> [!note] ROUTING (human dispatcher only; do NOT give to the agent)
> A "no direct evidence" verdict keeps claim C an inference that the project's own experiment must test, never a cited fact. Feeds [[the relevant design note]]. The agent must not upgrade an inference to a fact.

Notice: the AGENT BRIEF names no project, no note, no committed answer, and bakes in the honest null. The ROUTING carries all of that. That separation is the whole skill.

---

## What this skill does NOT do

- It does not run the research. It writes the brief that a research agent runs.
- It does not let the agent reach a design conclusion. The verdict is an input; a human decides.
- It does not accept project framing inside the AGENT BRIEF. If a brief needs a project detail to make sense, that detail belongs in ROUTING, or the Question is not yet general enough.
