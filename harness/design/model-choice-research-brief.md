---
tags: [Research, Brief]
---

# Harness Model Choice Research Brief

> [!abstract] Note Role
> **Contains**: project-free AGENT BRIEFs staged for research agents, plus the human-only ROUTING that records which decision consumes each verdict.
> **Cannot contain**: the design itself, the committed answer inside any AGENT BRIEF, or returned results. Results go to a Result note; the design lives in the spec (`skills/harness/ref/spec.md`).

Three briefs, dispatched in parallel. Each asks a method-universal question. None
of them names the design, and none is told the answer.

---

#### B1 — ephemeral versus persistent delegates

> [!abstract] AGENT BRIEF (give this verbatim to the research agent)
> **Task:** Find what has been measured about delegating bounded subtasks to short lived workers that start with empty context and terminate on completion, compared with long lived workers that persist across many subtasks. Collect empirical facts. Do not evaluate or endorse any system design. If the comparison has not been measured directly, report that plainly rather than assembling support from indirect sources.
>
> **Question:** In multi step automated work, how does cost and task success differ between a worker given one bounded task with a complete specification and then discarded, and a worker that persists and accumulates state across many tasks? Under what conditions does each pattern fail?
>
> **Facts to return** (any field that measures delegated or distributed automated work: software agents, distributed systems, crowdsourcing, human task decomposition, operations research):
> - Measured cost or token differences between fresh context workers and persistent workers on comparable workloads.
> - Measured quality or success rate differences, and the direction of the effect.
> - The overhead of specifying a task completely enough that the worker needs no clarification, including any measured rate at which such specifications turn out to be incomplete.
> - Failure modes specific to each pattern. For discarded workers, what is lost when context is not retained. For persistent workers, what accumulates and what it costs.
> - Bounding and negative facts: reviews or benchmarks reporting that the comparison has not been run, or that the difference was not significant.
>
> **Refuse / out of scope:** do not argue that either pattern is correct, and do not scope your answer to any specific project. Do not infer the comparison from literature that studies only one pattern and report it as a measured difference. Report what has and has not been shown, with limits.
>
> **Deliverable: a literature review.** Write a synthesis, not a list: what the field shows, where the strongest evidence sits, the bounds and failure modes, how the cases relate. Close with one verdict: **direct comparative evidence found**, **only indirect evidence**, or **no evidence exists**, justified by the reviewed evidence, with indirect only support labelled as such. Every source needs a complete reference: all authors, full title, venue, year, volume, issue and pages where applicable, and a DOI or stable URL or arXiv identifier. No bare keys. Reference list plus in text markers.

> [!note] ROUTING (human dispatcher only; do NOT give to the agent)
> Consumed by a decision on whether to add a second class of worker that runs once and terminates. Expected answer is that the direct comparison is thin and mostly vendor reported. A null verdict is useful: it keeps the choice a design judgement rather than a cited fact. Feeds the spec (`skills/harness/ref/spec.md`) at R6 and R13.

---

#### B2 — capability tier and reasoning effort for fully specified work

> [!abstract] AGENT BRIEF (give this verbatim to the research agent)
> **Task:** Find what has been measured about how task success varies with model capability tier and with reasoning effort or thinking budget, specifically when the worker receives a complete specification up front and cannot ask clarifying questions. Collect empirical facts. Do not endorse any configuration.
>
> **Question:** For automated software tasks, how does measured success rate change across capability tiers and across reasoning effort settings? Does the shape of that curve depend on whether the task was fully specified in advance, on task length, and on whether the output is independently reviewed?
>
> **Facts to return** (any published benchmark, vendor evaluation, or independent study; software engineering benchmarks, agentic tool use benchmarks, and general reasoning benchmarks all count):
> - Measured success rate against cost across capability tiers on the same task set.
> - Measured effect of reasoning effort or thinking budget within one model, with the size of the quality change and the size of the cost change.
> - Whether the effort curve is steeper for long horizon or agentic work than for short or well specified work, with figures.
> - Any measurement of the retry pattern: running at a low setting and rerunning only failures at a higher one, versus running everything at the higher setting.
> - Bounding and negative facts: workloads where a higher tier or higher effort bought nothing measurable, and any reported ceiling effects.
>
> **Refuse / out of scope:** do not recommend a model for any particular use, and do not scope your answer to any specific project. Do not treat a vendor claim as independently verified unless an independent evaluation reproduced it, and say which is which. Report the limits of each benchmark, including whether it measures cost per attempt or cost per completed task.
>
> **Deliverable: a literature review.** Synthesise what is measured, where the evidence is strongest, and how benchmarks disagree. Close with one verdict: **the curves are well characterised**, **partially characterised with named gaps**, or **not characterised**, justified by the reviewed evidence. Every source needs a complete reference: all authors, full title, venue, year, volume, issue and pages where applicable, and a DOI or stable URL or arXiv identifier. No bare keys. Reference list plus in text markers.

> [!note] ROUTING (human dispatcher only; do NOT give to the agent)
> Consumed by the per role model and effort table. The committed answer is currently a high capability model at medium effort for workers and high for the coordinator, drawn from one vendor guide. This brief exists because that is a single source. Feeds the spec (`skills/harness/ref/spec.md`) at R12.

---

#### B3 — context ceilings and when to compact

> [!abstract] AGENT BRIEF (give this verbatim to the research agent)
> **Task:** Find what has been measured about how output quality changes as occupied context grows, and about summarising or discarding earlier context at a threshold rather than running to a larger window. Collect empirical facts. Do not endorse any threshold.
>
> **Question:** How does task performance vary with the amount of context actually occupied, independent of the maximum the system allows? What is measured about compaction, summarisation, or eviction: when it helps, when it loses information that later turns out to be needed, and what it costs?
>
> **Facts to return** (long context evaluation, retrieval augmented generation, dialogue systems, summarisation, and any field that measures degradation with input length):
> - Measured degradation curves as occupied context grows, including position effects within the window.
> - Whether a larger maximum window improves results at a given occupancy, or only permits higher occupancy.
> - Measured effects of summarising or evicting earlier context: quality change, cost change, and the rate at which discarded material is later needed.
> - Any measured guidance on where to trigger compaction, and whether the trigger point has been studied rather than assumed.
> - Bounding and negative facts: studies finding no degradation over a range, or finding compaction cost more than it saved.
>
> **Refuse / out of scope:** do not recommend a threshold, and do not scope your answer to any specific project. Distinguish measurements of retrieval accuracy from measurements of generation quality, since they degrade differently. Do not present a vendor stated window size as evidence about quality at that size.
>
> **Deliverable: a literature review.** Synthesise the degradation evidence, the compaction evidence, and where they conflict. Close with one verdict: **thresholds are empirically grounded**, **grounded only for retrieval and not for generation**, or **not grounded**, justified by the reviewed evidence. Every source needs a complete reference: all authors, full title, venue, year, volume, issue and pages where applicable, and a DOI or stable URL or arXiv identifier. No bare keys. Reference list plus in text markers.

> [!note] ROUTING (human dispatcher only; do NOT give to the agent)
> Consumed by a decision to cap coordinator context and compact early, and to give the top coordinator the largest window. The proposed ceiling is a round number chosen by judgement, not measurement, which is exactly what this brief must not be told. Feeds the spec (`skills/harness/ref/spec.md`) at R12 and I10.
