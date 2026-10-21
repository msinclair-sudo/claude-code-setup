# Research workflow

How a brief becomes a critiqued literature review and a result note. Written up from the runs of 2026-10-20
(EX-01, MB-01, NP-01, MB-02) as the baseline to improve on. The workflow verifies; later stages (consolidation,
writing) use its output and do not verify again.

## Stages

| # | Stage | Who | Reads | Writes |
|---|---|---|---|---|
| 0 | Triage | main session | the question, its source note | size line (quick, standard, deep), vocabularies |
| 1 | Brief | main session | triage, source note | `Briefs/<slug>.md`: AGENT BRIEF, ROUTING, DISPATCH |
| 2 | Brief checks | main session, blind reader | the brief | revised brief, DISPATCH preflight line |
| 3 | Search | one agent per angle (deep only) | AGENT BRIEF, protocol, angle | findings records |
| 4 | Review | synthesis (deep) or researcher (quick, standard) | brief, protocol, findings | answers, review body, BibTeX references |
| 5 | Critique | critic (standard, deep) | brief, protocol, review | critique |
| 6 | Result note | main session | the workflow's return | `Results/<title>.md`: **the output** |
| 7 | Stage-2 check | main session | critique, ROUTING | a follow-up brief, or "not triggered" |
| 8 | Run record (optional) | main session | the workflow's return | `Results/<title>.run.json` beside the note |

Stages 3 to 5 are one call of `workflows/research-run.js`. Notes are filed in the vault by topic:
`Topics/<Subject>/Research/{Briefs,Results}` for subject matter, `Apps/Research/...` for tooling.

What each agent sees:

| Agent | AGENT BRIEF | DISPATCH extra | ROUTING | protocol | findings | review | sources, web |
|---|---|---|---|---|---|---|---|
| preflight reader | yes | yes | no | no | no | no | no |
| search agent | yes | yes | no | yes | own angle | no | yes |
| synthesis or researcher | yes | yes | no | yes | all angles | writes it | yes |
| critic | yes | yes | no | yes | no | yes | yes, and Crossref |

## 0. Triage

Four questions from the conversation and the source note (SKILL.md, Triage): how many directions and whether
they share a search space; practice or evidence; where the answer goes; which vocabulary communities publish
on it. They set the size:

| Size | Agents | Used for | 2026-10-20 runs |
|---|---|---|---|
| quick | researcher | not cited; practice; one vocabulary; a stage-1 scout | FD-01 |
| standard | researcher, critic | anything cited that is not deep | NP-01, MB-02 |
| deep | 2 or 3 search agents, synthesis, critic | two or more vocabularies, and an evidence question or a design input | EX-01, MB-01 |

## 1. Brief

One `#### <BriefID>` block with three callouts (SKILL.md template): the AGENT BRIEF (project-free, the only
part agents see), ROUTING (the consuming decision, expectations, the stage-2 condition) and DISPATCH (size,
angles, extra instructions, batch order, preflight line).

## 2. Brief checks

Lint, consistency by eye, and the blind preflight (`research-run` with `mode: "preflight"`), repeated until no
inferred hoped answer matches ROUTING. Residuals accepted go in the preflight line. 2026-10-20: EX-01 five
readings, MB-01 one, NP-01 and MB-02 three each, FD-01 two.

## 3. Search (deep only)

One agent per angle, in parallel, blind to each other, each returning findings records (`FINDINGS_SCHEMA`):
direction, claim, reference (BibTeX), access, quote or figure, evidence class, setting, standing, and the flags
single source, bounding or contrary, nearest precedent; plus sources not obtained and a search record. MB-01
produced 207 records, EX-01 188. Quick and standard runs have no search stage and produce none.

## 4. Review

Deep: the synthesis agent writes the review from every angle's findings and re-opens the sources that carry an
answer. Quick and standard: one researcher searches, reads and writes. Both return (`REVIEW_SCHEMA`) one answer
per direction (answer, strength, conflicts, not measured, access basis, single-source sensitivity), the review
body, sources not obtained and a search record.

Citations follow the researcher protocol: rule 3a for in-text citations (numbered or APA, each followed by
`[access; class; standing]` and any flags; standing is never left out) and rule 3b for references (one
`bibtex` block, complete entries, citekeys `auth.lower + shorttitle(3,3) + year`, `note = {access: ...}`; sources
not obtained in a second block). Notes from before 2026-10-21 use other conventions and are not relabelled.

## 5. Critique (standard and deep)

A fresh critic checks load-bearing claims against the sources and every reference against Crossref, and returns
(`CRITIQUE_SCHEMA`): whether the answers are supported (yes, partial, no), the reformulated answers the body
supports, an assessment, and itemised single-source claims, access errors, reference errors, coverage gaps (each
naming its setting), one-sided handling, merged cases, scope drift and expectation echo.

The critic corrects but does not edit: the body stays verbatim, and the corrections stand beside it. Applying
them to the claims is consolidation's job. All four critiqued runs of 2026-10-20 came back `partial`.

## 6. Result note

The note is the run's output and the only thing downstream may depend on. Written from the return using
`references/result-note-template.md`: frontmatter (`tags: [research, result, <subject>]`), Note Role,
Provenance, the critic block (reformulated answers first when `partial` or `no`), the full critique, answers as
delivered, the stage-2 check, sources not obtained (BibTeX), and the review body verbatim with its BibTeX
references. The critic block and the access basis come before the answers so that a reader sees how far the
evidence reaches before what it says.

## 7. Stage-2 check

The ROUTING condition is tested against `critique.coverage_gaps`. If it fires, a follow-up brief is written on
the named gaps: standalone, sized separately, never stating what earlier runs found. Batches run one at a time
with 15 minutes between runs.

## 8. Run record (optional)

`<note title>.run.json` beside the note: the workflow's return as an audit trail. Nothing downstream may require
it. Shape: `brief_id`, `run_id`, `date`, `size`, `angles`, `extra`, `agent_brief` (never ROUTING or DISPATCH),
`findings` (each with an `id`, `F-<angle>-<nnn>` in return order, and its `angle`), `not_obtained` (de-duplicated
by DOI, `from` naming the stages that listed it), `review`, `critique`, `access_counts`. The two deep runs of
2026-10-20 (EX-01, MB-01) have records rebuilt from their session transcripts; the standard and quick runs have
none, since they produce no findings records.
