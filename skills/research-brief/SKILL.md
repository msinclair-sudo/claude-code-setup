---
name: research-brief
description: "Write, size and dispatch a research brief for a research agent that collects generalisable empirical evidence, not project-specific confirmation. Use when the user invokes /research-brief, asks to prepare/write a research brief, research task, or literature-review brief for an agent to run, or asks to run/dispatch an existing brief. Enforces the fact/design split, prevents logical feedback loops where the research confirms the design back to itself, runs a blind framing check before dispatch, and picks the run size (quick, standard, deep) and whether the question needs one stage or two."
allowed-tools: [Read, Write, Edit, Bash]
---

# research-brief: briefs that collect evidence, not confirmation

A research brief tells a research agent what empirical question to investigate. The danger it must design around is the **logical feedback loop**: if the brief carries the project's own framing, the agent retrieves sources shaped like the design and reports them as support, so the design appears to confirm itself on its own reflection. That is not evidence.

Framing does not only travel in project names. It travels in which way a comparison is asked, in which side's background is requested, in what the brief tells the agent to discount, in how the scope is drawn, and in any hint about what the answer will be. This skill guards all of those, and it checks them with a blind reader, not only with a keyword search.

The research supplies evidence; a human consumes it into a design decision. The agent answers open research directions in its own words. It never picks from a menu of verdicts, and it never concludes the design is right.

The output is a three-part artefact kept together in the source document:
- **AGENT BRIEF**: project-free. The only part research agents see.
- **ROUTING**: human-only. Holds the project context, what the decision needs from each direction, the expected answer if there is one, and any stage-2 condition.
- **DISPATCH**: orchestrator-only. Holds run size, search angles and batch order. Its extra instructions reach the agents, so they are checked like the brief.

Dispatch only the AGENT BRIEF (plus any DISPATCH extra instructions) and `references/researcher-protocol.md`.

This skill is often reached mid-conversation, when a topic turns niche. Triage (step 0) is built to be answered from the conversation and the source note alone, without extra reading.

---

## The one rule everything serves

> Evidence qualifies only if it was produced independently of this project: it would exist, and could be found, by someone who has never heard of the project.

Its standing in the field does not matter. A contested result, a single recent study, a preprint or a minority finding qualifies, as long as its standing is reported alongside it. What never qualifies is a "fact" that is true only because of the project's design choices; that is the design looking in a mirror.

---

## The three parts

### Part 1: AGENT BRIEF (the only thing the agent receives)

Self-contained, project-free, link-free. A stranger with no knowledge of the project could run it and return useful evidence. It contains, in order:

1. **Task**: one or two sentences saying what to investigate, the instruction to collect evidence and not evaluate any design, and the **fixed evidence line** (constraint 2), verbatim.
2. **Scope**: the one place the scope is defined. Which systems, settings, interventions and measurement types count as evidence. If a direction uses a narrower or wider scope, the direction says so itself; no other sentence redefines scope.
3. **Directions**: numbered open research directions (D1, D2, ...), each a question the review must answer in its own words. Comparative directions are asked in either direction. Where the literature is expected to hold several distinct cases (named frameworks, measure types, settings), the direction asks for each separately.
4. **Evidence to gather**: a bullet list of what to look for. Widen the acceptable systems ("any organism or community", "any field that measures X"). Request bounding, negative and contrary evidence explicitly, and request background for every side of a comparison, not one. Ask for the nearest precedents: work that meets some but not all of a direction's conditions.
5. **Out of scope**: task limits only. Do not evaluate or endorse any research design; do not scope the answer to any specific project; do not report indirect evidence as direct. Nothing here states a scientific conclusion or tells the agent to discount a kind of evidence.
6. **Deliverable**: a literature review with one answer per direction, access-labelled evidence and complete references (constraint 8).

### Part 2: ROUTING (human dispatcher only; never given to the agent)

Holds everything Part 1 must not:
- which note or decision consumes the review
- the committed or expected answer, if there is one, per direction
- project links and the origin of the question
- for each direction: what the decision needs to know from it, and what kinds of answer would change the decision (the scope check, procedure step 4)
- the stage-2 condition, if the brief has one (see Stages)

Wikilinks and project names live here.

### Part 3: DISPATCH (orchestrator only)

The size, the triage answers behind it, the search angles for a deep run, any brief-specific extra instructions, and batch order when several briefs are dispatched together. The extra instructions reach the agents, so they obey every AGENT BRIEF constraint and go through the same checks.

---

## Hard constraints (check every brief against these)

1. **No project references in the AGENT BRIEF or extra instructions.** No wikilinks, no note names, no "this project", no "our hypothesis", no section numbers. The only acceptable use of the word "project" is in the out-of-scope guard ("do not scope your answer to any specific project").
2. **No outcome statements of any kind, including nulls.** The brief carries one fixed sentence about outcomes, verbatim, and nothing else:
   > Evidence on these directions may be abundant, sparse, conflicting or absent. Report what you find, whichever it is.

   Forbidden: a direction of result, a likely answer, a pattern of results, and also a lone null ("such evidence may not exist"). A null singled out is an expectation like any other, and in a PhD it is the convenient one, because "not measured" reads as a gap the project fills. Any expectation lives in ROUTING. **Follow-up briefs carry the highest risk**, because whoever writes them already knows the earlier result.
3. **Directions are neutral.**
   - A comparison is asked in either direction: "how does A compare with B, in either direction", never "does A exceed B" or "is A lower than B".
   - Background, bounding and contrary evidence are requested for every side, not just the side the design needs.
   - The design's own novelty wording (the exact combination of conditions the design claims is new) does not set a direction's boundary. Ask for the general quantity, and for the nearest precedents that meet some of the conditions.
4. **Out of scope limits the task, never the evidence.** It may forbid evaluating designs and scoping to a project. It may not state a published conclusion as a rule ("do not treat X as evidence of Y"), rule out a kind of evidence, or tell the agent how to read a result. If an interpretive caution is needed, write it as a reporting duty that applies both ways ("report what null-model analyses conclude, whichever way they point").
5. **Scope is stated once.** The Scope field is the definition. Task, directions and evidence bullets refer to it and do not restate it in other words. A direction with a different scope says which studies enter it.
6. **Label indirect support as indirect.** Background that makes a claim plausible without testing it is flagged as indirect and never counted as direct evidence. An inference is never upgraded to a fact.
7. **Keep distinct cases apart.** When a direction covers several things the literature may treat differently (named frameworks, measurement types such as whole-community sequencing against single-gene assays, settings, scales), the review answers for each separately. A large literature on one case must not answer for another.
8. **Deliverable is a literature review with access-labelled, complete references.**
   - A synthesis (what the field shows, where the strongest evidence sits, where it conflicts, the bounds and failure modes, how cases relate) that closes with **one answer per direction, in the reviewer's own words**: what the evidence shows, how strong it is, where it conflicts, which cases or settings have not been measured, and what access the answer rests on.
   - **Use what is available, and say what it was.** Every source carries an access level: full text, abstract only, or secondary (known only through another source's description). Abstract-only and secondary sources may be used; each claim that rests on them is labelled, and each answer states how much of it rests on full text.
   - Every source needs a complete reference: all authors, full title, venue, year, volume/issue/pages where applicable, and DOI (or stable URL/arXiv ID). No bare keys, no partial entries. Sources named in the brief itself are identified this fully too, so the agent finds the right paper.
   - **A "not found" names the search routes used and any limits hit.**
9. **No em or en dashes anywhere in the AGENT BRIEF or extra instructions.** Use commas, colons, periods, or parentheticals. Run the Task and Directions prose through clean writing (`humanizer` if available), but keep the field labels; they are correct register for an agent task spec.

---

## Template (copy and fill)

```markdown
#### <BriefID>

> [!abstract] AGENT BRIEF (give this verbatim to the research agent)
> **Task:** <what to investigate, in general terms>. Collect empirical evidence. Do not evaluate or endorse any research design. Evidence on these directions may be abundant, sparse, conflicting or absent. Report what you find, whichever it is.
>
> **Scope:** <systems, settings, interventions and measurement types that count; the only place scope is defined>.
>
> **Directions:**
> - **D1.** <open question at the level of methods/mechanisms/systems; comparisons asked in either direction>
> - **D2.** <...; if it covers several named cases, "for each of <case>, <case>, separately">
>
> **Evidence to gather** (<widen the acceptable systems/fields>):
> - <evidence type 1>
> - <background for each side of any comparison>
> - <bounding, negative and contrary evidence: limits, failures, results that cut against the obvious reading>
> - <nearest precedents: work meeting some but not all of a direction's conditions>
>
> **Out of scope:** do not evaluate or endorse any research design, and do not scope your answer to any specific project. Do not report indirect evidence as direct.
>
> **Deliverable: a literature review.** Write a synthesis (not a bare list): what the field shows, where the strongest evidence sits, where it conflicts, the bounds and failure modes, how the cases relate. Close with one answer per direction, in your own words: what the evidence shows, how strong it is, where it conflicts, which cases or settings have not been measured, and what access it rests on. Keep distinct cases apart. Label every source's access (full text, abstract only, or secondary) and label indirect support. Every "not found" names the search routes used. Every source cited must have a **complete reference**: all authors, full title, venue, year, volume/issue/pages where applicable, and DOI (or stable URL/arXiv ID). Provide a reference list and in-text markers.

> [!note] ROUTING (human dispatcher only; do NOT give to the agent)
> <which decision/note consumes the review; project links; origin.>
> **D1:** decision needs <what>. Expected: <answer or none>. Changes the decision if <kinds of answer>.
> **D2:** <...>
> **Stage 2:** <none | "if the critic's coverage gaps name <kind of gap>, write a targeted follow-up brief on those, sized separately">

> [!example] DISPATCH (orchestrator only; extra instructions reach the agent)
> **Size:** <quick | standard | deep>. Triage: <n> directions; <practice | evidence>; <cited/limitation/design | not cited>; vocabularies: <list>.
> **Angles** (deep only): <name: vocabulary>; <name: vocabulary>; <...>
> **Extra instructions:** <brief-specific, project-free, or none>
> **Batch order:** <none | runs after <BriefID>>
> **Preflight:** <date run; guesses vs ROUTING; changes made>
```

(Callout syntax is for Obsidian/markdown notes. In a plain prompt, headed `AGENT BRIEF`, `ROUTING` and `DISPATCH` blocks work the same way. What matters is the split, not the callout.)

---

## Procedure

0. **Triage.** Answer the four questions below and tell the user the result in one line, for example "Deep: three directions, three vocabularies, feeds a limitation". If the user downgrades, record it in DISPATCH.
1. **Find the real empirical question.** Read the open point in its source note. Strip it down to the method-universal core: what is true about the method/mechanism/field regardless of this project? If you cannot state it without naming the project, or without the design's own novelty wording, you have not found the empirical question yet.
2. **Write any expectation into ROUTING first.** If you think the answer will be a null, a direction, or a pattern, write it down in ROUTING now. Writing it down is what keeps it out of the brief.
3. **Write the AGENT BRIEF** from the template. Define scope once. Ask comparisons both ways. Request background and contrary evidence for every side. Ask for nearest precedents. Keep the out-of-scope block to task limits.
4. **Write the ROUTING, and run the scope check.** For each direction, write what the decision needs from it and what kinds of answer would change the decision. If no plausible answer to a direction would change anything, drop it. If the decision needs something no direction asks, add a direction. If a direction answers a different claim from the one the decision needs, rewrite it (a direction asking "can the input be omitted" when the claim is "less of the input is lost" fails here). Add the stage-2 condition if Stages calls for one.
5. **Write the DISPATCH** from the triage. The direction count in the triage line must equal the number of directions in the brief.
6. **Verify (do not skip).** Run all three checks below: lint, consistency, blind preflight. A brief that fails any of them is not ready.
7. **After any revision, re-run every check on the whole brief.** Revisions create new faults: a threshold added to one clause and not its counterpart, a direction split without splitting its answer, scope narrowed in one sentence and not another. Checking only the edited line misses them.
8. **Run it** (see Dispatch), then **write the result note** from `references/result-note-template.md` and check the stage-2 condition against the critique.

---

## Triage and run sizes

Four questions, answerable from the conversation and the source note:

1. **How many directions, and do they share a search space?** Directions that share a search space go in one brief. Directions that need different literatures go in separate briefs, dispatched as a batch.
2. **What kind of question?** *Practice*: what exists, what the field uses. *Evidence*: has it been measured, does a result hold in a given regime. An evidence question can end in "not found", and "not found" is only as good as the search breadth behind it.
3. **Where does the answer go?** Into a citation, a limitation statement or a design decision, or nowhere in the document (orientation only)?
4. **How many vocabulary communities publish on it?** List them: groups of researchers who study the phenomenon under different names, journals and review series. A distributed pathway, for example, is "cross-feeding" to microbial ecologists and "incomplete dechlorination" to bioremediation engineers. Each community becomes a search angle. Compare your list with the communities the preflight reader names.

| Size | Shape | Agents | Choose when |
|---|---|---|---|
| **quick** | researcher | 1 | not cited anywhere, and a practice question, in one vocabulary. Also a stage-1 vocabulary scout. |
| **standard** | researcher, then critic | 2 | anything cited that is not deep |
| **deep** | one search agent per vocabulary (2 or 3), then synthesis, then critic | 4 to 5 | two or more vocabularies, and either an evidence question or an answer that feeds a limitation or design decision |

- **Anything that will be cited is at least standard.** The critic is the stage that catches unsupported answers, mislabelled access, missed settings and wrong references; a quick run's output is not citable until critiqued.
- **Split deep angles by vocabulary community, not by direction.** Direction splits search the same community several times and miss the one that uses different words.
- **Calibration against past briefs:**
  - A fertiliser-emissions sourcing brief was cited, but was a practice question in one vocabulary: standard.
  - A set-size-bias regime check is an evidence question across ontology similarity and missing-data statistics: deep with two angles.
  - A distributed-pathway transfer brief is an evidence question across microbial ecology, syntrophy, bioremediation and marine carbon cycling, and feeds a limitation: deep with three angles.

---

## Stages

A **stage** is a brief written after reading an earlier brief's result.

- **One stage** when the directions can be fully written now, in the vocabulary their literature uses.
- **Plan two stages** when:
  - the right directions depend on vocabulary or landscape not yet known. Stage 1 is then a quick scout ("what terms, measures and review series does this field use"), and stage 2 is the real brief.
  - the size is deep and some directions may come back thin. The critic's coverage gaps are then the likely trigger for a targeted follow-up.
- **Write stage 2 into ROUTING as a condition on the critique**, never as an expected result: "if the critic's coverage gaps name specific settings or classes, write a follow-up brief on those". The workflow returns `critique.coverage_gaps` with each gap's setting named, so the check is mechanical.
- **Follow-up briefs stand alone.** They assume no earlier brief, name the gap settings neutrally, and never say what earlier results found or what the new settings are expected to show (constraint 2).
- **Re-scoping is not a stage.** If a result shows a direction was aimed wrong, that is a failed scope check (procedure step 4); fix the check habit, not just the brief.

---

## Verification (run before dispatching any brief)

Three checks. The lint catches vocabulary; the consistency pass catches internal contradictions; the blind preflight catches framing, which neither of the others can see. Past briefs passed a strict lint and still carried the design's claim in the direction of the Question, in the wording of the refusal, and in the boundary of what counted.

### Check 1: lint

Extract the AGENT BRIEF blocks and the DISPATCH extra-instruction lines, and prove they are clean. Adjust the file path.

```bash
FILE="path/to/your/briefs.md"
TMP="${CLAUDE_JOB_DIR:-${TMPDIR:-/tmp}}/ab.$$.txt"
# AGENT BRIEF callout blocks (stop at ROUTING or DISPATCH), plus DISPATCH extra instructions
awk '/> \[!abstract\] AGENT BRIEF/{f=1} /> \[!note\] ROUTING|> \[!example\] DISPATCH/{f=0} f' "$FILE" > "$TMP"
grep -E '^> \*\*Extra instructions:\*\*' "$FILE" >> "$TMP"
FIXED='Evidence on these directions may be abundant, sparse, conflicting or absent. Report what you find, whichever it is.'

echo "=== (1) project leakage (want: 0 wikilinks, 0 self-references) ==="
grep -c '\[\[' "$TMP"; echo "^ wikilinks (must be 0)"
grep -ciE 'this project|our hypothesis|this study|our design' "$TMP"; echo "^ self-references (must be 0)"
grep -niE 'project' "$TMP" | grep -viE 'any specific project|a specific project' || echo "  (no stray 'project' uses)"

echo "=== (2) dashes (want: none) ==="
grep -nE '—|–' "$TMP" && echo "DASHES FOUND ^ remove them" || echo "clean"

echo "=== (3) fixed evidence line (want: one per brief) ==="
echo "briefs: $(grep -c 'AGENT BRIEF' "$TMP")  fixed lines: $(grep -cF "$FIXED" "$TMP")"

echo "=== (4) outcome language, nulls included (want: none outside the fixed line) ==="
grep -vF "$FIXED" "$TMP" | grep -noiE '[^.]*(expect|likely|unlikely|probabl|anticipat|may not exist|no (direct )?evidence|point(s|ing)? (toward|in)|should (show|find|confirm)|we think)[^.]*' || echo "  (none)"

echo "=== (5) one-way comparisons (inspect every hit) ==="
grep -noiE '[^.]*((better|worse|more|less|lower|higher|greater|smaller|faster|slower) than|exceed|outperform|superior|inferior)[^.]*' "$TMP" || echo "  (none)"

echo "=== (6) out-of-scope rules about evidence (inspect every hit) ==="
grep -niE 'out of scope' "$TMP" | grep -iE 'as evidence (of|for)|do not (treat|count|accept|interpret)|ignore|discount' || echo "  (none)"

rm -f "$TMP"
```

Checks 1 to 4 must pass outright. Check 5 hits may stay only when the comparison is explicitly two-way ("higher or lower than", "in either direction"). Check 6 hits fail constraint 4 unless they forbid reporting indirect evidence as direct.

### Check 2: consistency (by eye, whole brief)

- Scope is defined once, in the Scope field, and no other sentence redefines it. Any direction with a different scope says which studies enter it.
- Every comparison asks for background and contrary evidence on each side.
- Any threshold, condition or qualifier applied to one side of a comparison is applied to the other.
- Every direction that covers several named cases or measurement types asks for each separately.
- Every source named in the brief carries a full reference.
- The DISPATCH triage direction count equals the number of directions.
- The ROUTING has a line per direction.

### Check 3: blind preflight

A fresh agent reads the brief exactly as a research agent would receive it (the AGENT BRIEF plus DISPATCH extra instructions, nothing else) and reports what it can infer. Run it with the Workflow tool, `scriptPath` as in Dispatch, and `args`:

```json
{ "mode": "preflight", "brief": "<AGENT BRIEF text>", "extra": ["<DISPATCH extra instructions>"] }
```

It returns `inferred_design`, `inferred_hoped_answers` (per direction), `loaded_wording`, `one_sided_requests`, `evidence_rules_in_refusal`, `scope_inconsistencies`, `nearest_precedent_risk` and `communities`. Compare against ROUTING:

- If `inferred_design` recovers the design's claim, or an `inferred_hoped_answers` entry matches ROUTING's expected answer, the brief leaks. Find the wording the reader cites and rewrite it.
- Every `loaded_wording`, `one_sided_requests`, `evidence_rules_in_refusal` and `scope_inconsistencies` item is fixed or explicitly justified in DISPATCH.
- Any community in `communities` that is missing from the DISPATCH angles is either added or recorded as deliberately excluded.

Record the result in the DISPATCH **Preflight** line. After fixing anything, re-run all three checks (procedure step 7).

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
3. **Batches:** run each brief as its own workflow call. Independent briefs can run concurrently; briefs with a batch order wait for their predecessor.
4. **On return,** write the result note from `references/result-note-template.md`. If `critique.answers_supported` is `partial` or `no`, lead with the critic's reformulated answers. Report the access basis (`accessCounts` for deep runs, each answer's `access_basis` otherwise). Then check the ROUTING stage-2 condition against `critique.coverage_gaps` and tell the user whether it fired.
5. **Reading the answers against ROUTING** is where the human's expectation meets the evidence. Read the critic's block and the access counts before the answers, and note in the consuming decision where the evidence rests on abstracts or secondary accounts.

---

## Worked example (a brief that passes)

> [!abstract] AGENT BRIEF (give this verbatim to the research agent)
> **Task:** Investigate how two kinds of predictive model compare in accuracy when the system they predict is spatially structured. Collect empirical evidence. Do not evaluate or endorse any research design. Evidence on these directions may be abundant, sparse, conflicting or absent. Report what you find, whichever it is.
>
> **Scope:** predictive models of any biological, ecological or environmental system, evaluated on data where the system's structure (spatial, compositional or network) varies. Both simulation benchmarks and field data count.
>
> **Directions:**
> - **D1.** How does the prediction error of models that explicitly represent mechanism M compare with that of models using only aggregate features, in either direction, as the system moves from uniform to structured?
> - **D2.** When mechanistic models assume the system is uniform and it is not, how are their predictions affected: magnitude, direction and conditions?
> - **D3.** When aggregate-feature models are applied to structured systems, how are their predictions affected: magnitude, direction and conditions?
>
> **Evidence to gather** (any organism, community or field that predicts structured systems):
> - Studies comparing the two model types on the same system, with accuracy reported against structure.
> - Background on the known strengths and failure modes of each model type under structure.
> - Nearest precedents: comparisons of the two types that do not vary structure, and structure studies that test only one type.
> - Bounding and contrary results: settings where either type's usual advantage failed to appear.
>
> **Out of scope:** do not evaluate or endorse any research design, and do not scope your answer to any specific project. Do not report indirect evidence as direct.
>
> **Deliverable: a literature review.** Write a synthesis (not a bare list): what the field shows, where the strongest evidence sits, where it conflicts, the bounds and failure modes, how the cases relate. Close with one answer per direction, in your own words: what the evidence shows, how strong it is, where it conflicts, which cases or settings have not been measured, and what access it rests on. Keep distinct cases apart. Label every source's access (full text, abstract only, or secondary) and label indirect support. Every "not found" names the search routes used. Every source cited must have a **complete reference**: all authors, full title, venue, year, volume/issue/pages where applicable, and DOI (or stable URL/arXiv ID). Provide a reference list and in-text markers.

> [!note] ROUTING (human dispatcher only; do NOT give to the agent)
> Feeds [[the relevant design note]].
> **D1:** decision needs whether claim C (mechanistic models degrade less under structure) has direct support. Expected: no direct comparison exists. Changes the decision if a direct comparison exists in either direction: cite it, and drop claim C if it points the other way.
> **D2, D3:** decision needs the size of each type's bias for the limitation statement. Expected: none. Changes the limitation's wording in proportion to what is reported.
> **Stage 2:** if the critic's coverage gaps name a field that benchmarks the two model types under another name, write a follow-up brief on that field.

> [!example] DISPATCH (orchestrator only; extra instructions reach the agent)
> **Size:** deep. Triage: 3 directions; evidence question; feeds a design note; vocabularies: mechanistic modelling, machine-learning benchmarking, spatial ecology.
> **Angles:** mechanistic: process-based and constraint-based model validation; ml: predictive benchmark and out-of-distribution evaluation; spatial: spatially structured ecosystem prediction.
> **Extra instructions:** none.
> **Preflight:** reader recovered "comparing model types under structure" but no hoped-for direction; added D3 after it flagged background requested for the mechanistic side only.

Notice:
- The AGENT BRIEF names no project and no expected answer. The expectation (a null) sits in ROUTING, not in the brief.
- D1 is asked in either direction, and D2 and D3 give each model type the same treatment.
- There are no verdict options. ROUTING says what kinds of answer would change the decision; the agent never sees them.

That separation is the whole skill.

---

## What this skill does NOT do

- It does not let the agent reach a design conclusion. The answers are evidence; a human decides.
- It does not accept project framing inside the AGENT BRIEF. If a brief needs a project detail to make sense, that detail belongs in ROUTING, or the direction is not yet general enough.
- It does not hide weak access. Evidence the agents could only see as an abstract or a secondary account is used and labelled, and a "not found" is a statement about the search routes used.
