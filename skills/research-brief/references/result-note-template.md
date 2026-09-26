# Result note template

Write one note per returned brief into the results folder next to the briefs folder. Title the note after the review, not after the brief ID. This file is for the human reader. The workflow returns `{ mode, size, angles, sweepCounts, accessCounts, notObtained, review, critique }`, and every section below is filled from those fields.

Callout choice for the critic block:
- `critique.answers_supported` is `yes`: use `[!warning]` ("read before citing").
- `partial` or `no`: use `[!danger]`, and put the critic's reformulated answers at the top of the block.

The critic block and the access basis come before the answers on purpose: read how far the evidence reaches before reading what it says.

```markdown
---
created: <YYYY-MM-DD>
updated: <YYYY-MM-DD>
tags:
  - PhD
  - Research
  - Result
---
# <Review title>

> [!abstract] Note Role
> **Contains**: The returned literature review for <BriefID> of [[<brief note>]], its answers, reference list, and the adversarial critique of it.
> **Cannot contain**: Design decisions drawn from the review. Those belong in the consuming note named in the brief's ROUTING.

> [!info] Provenance
> Returned <date> by the research-run workflow at size **<quick|standard|deep>**, given the `AGENT BRIEF` of <BriefID> verbatim plus the researcher protocol. ROUTING was withheld. Preflight: <date and outcome, from DISPATCH>. <Deep: search angles and findings per angle from sweepCounts.> <Search record: routes used and any limits hit, from the review's Search record.>
> **Access:** <deep: accessCounts, as full text n / abstract only n / secondary n. Otherwise: summarise review.answers[].access_basis.>

> [!danger] Critic: answers <partly supported | not supported>
> **Reformulated answers:** <critique.reformulated_answers, one line per direction>
> <critique.answers_assessment>

> [!warning] Adversarial critique, full findings
> **Access errors** (<n>): <critique.access_errors>
> **Single-source claims** (<n>): <critique.single_source_claims>
> **Reference errors** (<n>): <critique.reference_errors>
> **Coverage gaps** (<n>): <critique.coverage_gaps, each with its named setting or class>
> **One-sided handling** (<n>): <critique.one_sided_handling>
> **Merged cases** (<n>): <critique.merged_cases>
> **Scope drift** (<n>): <critique.scope_drift>
> **Expectation echo:** <critique.expectation_echo>

> [!quote] Answers as delivered
> **D1** <case if any>: <answer>. *Strength:* <strength>. *Conflicts:* <conflicts>. *Not measured:* <not_measured>. *Access:* <access_basis>. *Single-source sensitivity:* <single_source_sensitivity>.
> **D2** <...>

> [!todo] Stage 2 check
> <Did the ROUTING stage-2 condition fire? Name the gaps that trigger a follow-up brief, or write "not triggered".>

> [!failure] Sources not obtained
> <notObtained: reference, routes tried. Nothing beyond a citation was reachable for these; none supports any claim in the review.>

---

<review body verbatim, with its access labels and reference list>
```

Before any reference moves into the bibliography, confirm it against Crossref yourself, even if the critic passed it. Before citing a claim, check its access label: a claim resting on an abstract or a secondary account is cited as such, or its full text is obtained first.
