---
tags: [Research, Result]
---

# Harness Model Choice Research Result

> [!abstract] Note Role
> **Contains**: the three returned verdicts, the load-bearing numbers behind them, and what each one does to a design claim in the spec (`skills/harness/ref/spec.md`).
> **Cannot contain**: the design decision itself. Decisions are recorded in the spec; this note is the input a human consumes.

Briefs in `model-choice-research-brief.md`. Three agents, dispatched in
parallel, none told the committed answer.

---

## Verdicts

| brief | verdict |
| --- | --- |
| B1 ephemeral vs persistent workers | direct evidence found for **humans and distributed systems**; **indirect only** for LLM agents |
| B2 tier and effort curves | **partially characterised, with named gaps** |
| B3 context ceilings and compaction | **not grounded** |

---

## What survives as support

**A complete specification up front beats the same information delivered in
pieces, by 39%.** Laban et al. (2025), 15 models, ~200,000 conversations.
Concatenating the pieces back into one instruction recovers 95.1%, so nothing is
lost in the splitting: the loss is caused by incremental arrival itself.
Degradation appears at **two** pieces. Restating everything every turn recovers
only 15 to 20%. This is the strongest result in the set and it is not fixable by
model or effort.

**Removing prior history mitigates self-conditioning.** Sinha et al. (ICLR 2026)
show a persistent worker's own errors compound in its context, that scale does
not fix this, and that explicitly clearing history does.

**A worker revisiting its own output without external verification gets worse.**
Huang et al. (ICLR 2024): accuracy fell in every configuration tested, GPT-3.5 on
CommonSenseQA 75.8 to 38.1. With an oracle available the same procedure improves
things. Verification, not reflection, is what makes revision work.

**Disposable workers plus a strong verifier beat one expensive worker, on cost
and accuracy.** Brown et al., dollar-matched on SWE-bench Lite: five samples from
a cheap model solve 29.6% at about $0.12 per resolved, against Claude 3.5 Sonnet
at 26.7% and about $0.64. Conditional on the verifier: the same pattern fails
where selection rests on three example tests rather than a repository suite.

**Occupancy degrades quality independent of retrieval.** Du et al. (EMNLP 2025)
hold retrieval perfect and mask irrelevant tokens: 13.9 to 85% degradation.

---

## What contradicts a committed choice

**A larger maximum window does not improve behaviour at a given occupancy.**
Liu et al. tested same-family pairs directly, 4K against 16K and 8K against 100K,
and found performance "nearly identical". This is a direct null against the
reasoning that gave leads and the head lead a 1M model.

**Fixed-interval compaction degraded 40.4% of the transitions it caused.**
Li et al. (2026): of 2,495 summarisation calls, 1,009 flipped a correct answer to
wrong. A content-conditioned rule beat the fixed trigger in 11 of 12 settings at
30 to 70% lower cost, and the gain came from the rule rather than the tool.

**No compaction threshold has been established.** No study sweeps a trigger
against quality with enough resolution to locate one. The widely repeated "70 to
80% of window" traces to blog posts. Deployed defaults span 50% to 99%.

**Summarisation is biased against the earliest material**, both in faithfulness
and in content selection. In a plan-then-delegate design the earliest item in a
lead's context is the plan.

**No published measurement exists for running at low effort and retrying
failures at high.** Not from any vendor, not independently. The figures used to
set the current effort table come from a vendor guide that is not publicly
published and has never been reproduced.

**A longer first attempt beat selective recovery** on accuracy and total tokens
together (Dip et al. 2026): tune the initial budget first.

---

## The finding that cuts against the purpose

The change was motivated by token cost. The evidence says the pattern does not
obviously reduce tokens; it moves them.

- In the only controlled head-to-head, bounded-and-discarded workers were 3.7x
  faster to first completed task and produced 5.7x more per session, but **25%
  less per developer-hour**. The session gain came from seven people working in
  parallel. Quality showed **no significant difference** (p = .09).
- That study **explicitly excluded the cost of writing the specifications**. The
  authors say so. The only measurement of that cost anywhere is a single
  industrial data point: **40 engineer-hours** of specification preparation at
  NTT.
- Budget-matched controls erase the multi-agent advantage. Four independent 2026
  studies find that apparent gains vanish once total tokens are held constant,
  and one vendor's own analysis attributes **80% of benchmark variance to token
  spend alone**.
- In production serverless, **20% of pods had a useful life shorter than their
  own startup cost**. The direct analogue is a contract whose briefing costs more
  than its work.

So the specification burden lands on the lead, which is the most expensive worker
in the tree. Whether the total falls is an open empirical question, and the
harness now has the instrument to answer it.

---

## The strict "no questions" form is contradicted

- Workers given ambiguous instructions **with no channel to ask were correct
  about 39% of the time**, so roughly 61% of submitted work was wrong
  (Manam and Quinn 2018, 65 planted ambiguities, 304 workers).
- **46.7% of ambiguities flagged in freshly written specifications were confirmed
  by their own authors**, about 2.6 per specification, in specs the authors
  believed finished.
- 38.3% of SWE-bench Verified samples were flagged as underspecified.
- Interaction on underspecified inputs improves performance **by up to 74%**, and
  Claude Sonnet 4 recovers 89% of its fully-specified score through it. But
  models are unreliable at knowing when to ask: one model showed a **100%
  false-negative rate**, never asking at all (Ambig-SWE, ICLR 2026).

These are not in conflict with the 39% drip-feed penalty. That penalty is about
information withheld and released piecemeal when it could have been given at
once. This is about information the specifier never had. Give everything known up
front, and keep a narrow channel for genuine gaps.

---

## Named gaps

- Nobody has run the LLM version of the controlled head-to-head: same model, same
  tasks, **matched token budget**, fresh briefed workers against one persistent
  worker, with the briefing cost charged to the fresh side.
- No study crosses reasoning effort with specification completeness factorially.
  Two agents reached this independently.
- The specification-writing cost has one data point and no distribution.
