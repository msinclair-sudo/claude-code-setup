# Result note template

Write one note per returned brief into the results folder next to the briefs folder. Title the note after the review, not after the brief ID. This file is for the human reader. The workflow returns `{ size, angles, sweepCounts, notObtained, review, critique }`, and every section below is filled from those fields.

Callout choice for the critic block:
- `critique.verdict_supported` is `yes`: use `[!warning]` ("read before citing").
- `partial` or `no`: use `[!danger]`, and put the critic's reformulated verdict at the top of the block.

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
> **Contains**: The returned literature review for <BriefID> of [[<brief note>]], its verdict, reference list, and the adversarial critique of it.
> **Cannot contain**: Design decisions drawn from the review. Those belong in the consuming note named in the brief's ROUTING.

> [!info] Provenance
> Returned <date> by the research-run workflow at size **<quick|standard|deep>**, given the `AGENT BRIEF` of <BriefID> verbatim plus the researcher protocol. ROUTING and DISPATCH were withheld. <Deep: search angles and findings per angle from sweepCounts.> <Search record: routes used and any limits hit, from the review's Search record.>

> [!quote] Verdict as delivered
> **<verdict, one line per part>**

> [!danger] Critic: verdict <partly supported | not supported>
> **Reformulated verdict:** <critique.reformulated_verdict>
> <critique.verdict_assessment>

> [!warning] Adversarial critique, full findings
> **Full-text breaches** (<n>): <critique.abstract_only_claims>
> **Single-source claims** (<n>): <critique.single_source_claims>
> **Reference errors** (<n>): <critique.reference_errors>
> **Coverage gaps** (<n>): <critique.coverage_gaps, each with its named setting or class>
> **Scope drift** (<n>): <critique.scope_drift>
> **Expectation echo:** <critique.expectation_echo>

> [!todo] Stage 2 check
> <Did the ROUTING stage-2 condition fire? Name the gaps that trigger a follow-up brief, or write "not triggered".>

> [!failure] Sources not obtained
> <notObtained: reference, routes tried. None of these supports any claim in the review.>

---

<review body verbatim, with its reference list>
```

Before any reference moves into the bibliography, confirm it against Crossref yourself, even if the critic passed it.
