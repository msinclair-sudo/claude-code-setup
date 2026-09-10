---
name: de-densify
description: "Reduce structural density in academic prose. Splits overloaded multi-fact sentences, unpacks buried definitions and long parentheticals, groups flat enumerations, adds synthesis anchors to evidence parades, and batches cross-references. Use when a Results, Discussion, or literature review section is hard to parse on one read, when sentences carry 3+ facts at once, or when the user invokes /de-densify. Runs as Pass 2 of write-pass, after humanizer."
allowed-tools: [Read, Write, Edit]
---

# De-Densify Skill

## Purpose

This skill addresses structural density in academic prose, specifically in Results, Discussion, and literature review sections where data-heavy sentences and evidence parades accumulate faster than the reader can process them. It operates at the **sentence-splitting and document-structure level only**. It does not add restatements, analogies, padding, or breathing-room paragraphs. Run `humanizer` first; run this skill after if structural density problems remain.

## When to use this skill

Use **after** `humanizer` has been applied. This skill handles problems those tools cannot reach:

**Triggers:**
- A sentence contains 3+ distinct facts, numbers, or technical terms simultaneously
- A technical term is defined inside a parenthetical rather than given its own sentence
- A paragraph accumulates 3+ inline cross-references
- A sentence contains a list of 4+ mechanisms, gene names, or technical terms
- Three or more consecutive paragraphs each introduce a different study, dataset, or biological system (evidence parade)
- A multi-section document repeats the same structural arc across 3+ sections

**Do not use when:**
- no trigger above is present. Do not expand to fix a problem that isn't there. (A passing Density score upstream is not on its own a reason to skip: that score asks whether anything is *cuttable*, while this skill fixes prose that is *hard to parse*.)

---

## Hard constraint: add no new content

This skill changes how existing content is arranged. It never adds content.

Do not add a fact, number, name, date, citation, ranking, comparison, superlative, or causal claim that is not already in the source text. If a split or a synthesis anchor seems to need a detail you do not have, ask for it or write a simpler sentence. An unsupported addition is an error, not a stylistic choice.

Watch three moves in particular, because they are the ones that invent:

- **Rankings and superlatives.** "the lowest in the corpus", "the most isolated", "well below the median". A ranking needs every value in the comparison set, and a median needs the whole distribution. If the source gives neither, the claim is invented even when the numbers around it are real.
- **Interpretive glosses.** Explaining what a result *means* or *confirms* while splitting a sentence. Splitting redistributes the existing claim; it does not license a new one.
- **Mechanism.** Explaining *how* something works in order to justify a grouping (Operation 5). If the source lists four mechanisms without describing them, the rewrite lists four mechanisms without describing them.

**Before returning, verify:** every fact, number, ranking, comparison, and causal claim in the output appears in the input. This check is not optional, and it matters most in Results and Discussion sections, where an invented comparison is a research-integrity problem rather than a style problem.

---

## Paragraph size constraint

Paragraphs must contain at least 3 sentences. Never leave inserted connective tissue as a 1-2 sentence orphan. Fold it into an adjacent paragraph or expand it to meet the minimum. There is no target paragraph length; size follows content.

---

## Operations

### Operation 1: Split multi-fact sentences

When a sentence contains 3+ distinct facts (numbers, cluster IDs, metric values, statistical tests), distribute them across separate sentences. Lead with the overall pattern; follow with the evidence in order of interpretive interest.

**Before:**
> The five clusters — quantum computing (conductance 0.020, peripherality 0.846), synthetic chemistry (0.069, 0.915), astrophysics (0.006, 0.884), social sciences (0.098, 0.897), and computer vision (0.110, 0.858) — all had conductance below 0.12 and peripherality above 0.83.

**After:**
> All five clusters showed conductance below 0.12 and peripherality above 0.83. Astrophysics had the lowest conductance of the five (0.006), with peripherality of 0.884. Quantum computing (0.020, 0.846) and social sciences (0.098, 0.897) followed. Synthetic chemistry (0.069, 0.915) and computer vision (0.110, 0.858) had the highest conductance values in the group.

### Operation 2: Unpack inline definitions

When a technical term is defined inside a parenthetical or appositive clause, extract the definition into its own sentence. This gives readers the term before its use, not simultaneously.

**Before:**
> Bridge signal (the ratio of reaching edges to total inter-cluster edges) quantifies the proportion of semantically distant citations between two clusters, with values above 0.85 indicating near-complete vocabulary divergence.

**After:**
> Bridge signal quantifies the proportion of semantically distant citations between two clusters. It is computed as the ratio of reaching edges to total inter-cluster edges. Values above 0.85 indicate near-complete vocabulary divergence between the two communities.

### Operation 3: Add signposting sentences

When the logical relationship between consecutive sentences is implicit, add a signposting sentence that makes it explicit. These carry no new data, only connective tissue.

Types (from Hyland's metadiscourse framework):
- **Code glosses:** "In other words," "that is," "specifically"
- **Frame markers:** "The first property is...," "Turning to the second finding..."
- **Transition signals:** "The distinction matters because...," "This pattern reverses when..."

**Before:**
> Conductance measures the ratio of inter-cluster edges to total edges. High conductance indicates poor separation. Low-density clusters may represent heterogeneous groupings. The orphan rate fell to 2.1%.

**After:**
> Conductance measures the ratio of inter-cluster edges to total edges. High values therefore indicate that a cluster connects more to the rest of the network than to itself, which is what makes high conductance a sign of poor separation. Internal density is a separate measure: clusters low on it may represent heterogeneous groupings. The orphan rate fell to 2.1%.

### Operation 4: Expand parenthetical asides

If a parenthetical aside exceeds 5 words and contains information the reader needs, extract it into its own sentence(s). Short parentheticals (cluster IDs, p-values, single citations) can stay inline.

**Before:**
> The scoring methodology (which operated through an overwrite model in which each scoring act replaced the previous value for all papers it covered, with no averaging or multi-signal resolution) concentrated human effort on the most relevant portion of the corpus.

**After:**
> The scoring methodology concentrated human effort on the most relevant portion of the corpus. It operated through an overwrite model: each scoring act replaced the previous value for all papers it covered. There was no averaging and no multi-signal resolution.

### Operation 5: Unpack enumerations

When a sentence lists 4+ technical terms, mechanisms, or gene names, the sentence may be under the word-count ceiling but still overloaded.

**Three strategies:**

**a) Group by principle.** Organise into categories with a bridging phrase. Use the split the literature actually uses, and do not add mechanism detail the source does not give:
> Before: "They suppress pathogens through antibiosis, competition for iron, mycoparasitism, and induced systemic resistance."
> After: "Three of these mechanisms act directly on the pathogen: antibiosis, competition for iron, and mycoparasitism. The fourth, induced systemic resistance, acts through the host."

**Do not force a symmetric split.** These four mechanisms partition 3+1, not 2+2. A tidy 2+2 grouping here would have to move mycoparasitism to the host-mediated side, which is wrong: mycoparasitism is direct antagonism of one fungus by another. If the categories come out uneven, say so; the grouping must be a real taxonomy, not a pleasing shape.

**b) Lead with the count, follow with the list:**
> "Four mechanisms contribute to pathogen suppression. Antibiosis and iron competition act directly on the pathogen. Mycoparasitism and induced systemic resistance act through the host."

**c) Distribute at a maximum of 2 new terms per sentence.**

**Exemption:** Gene name lists serving as evidence catalogues (e.g., *nifHDK*, *acdS*, *phoD*) can stay compressed when the reader is expected to scan rather than absorb each one.

### Operation 6: Synthesis anchors (evidence parades)

When 3+ consecutive paragraphs each introduce a different study, dataset, or biological system, insert a synthesis anchor after every 2 to 3 studies. A synthesis anchor does not introduce new evidence. It names the pattern accumulating across the studies just described, explains why it matters, and orients the reader toward what comes next.

A synthesis anchor answers: "What do these studies, taken together, show that no individual study shows?"

**Verify before asserting.** A synthesis anchor states a pattern, and a pattern stated flatly is a claim. "Each study stopped at gene cataloguing" and "none proceeded to" are universal claims over the set: to write one you must have checked every study in scope. If you have not, scope it to what you did read ("in the studies reviewed here") or do not make the claim. One counterexample from a reviewer discredits the paragraph and the section around it.

**What a synthesis anchor IS:**
- "Across these systems, the same pattern recurs: taxonomic abundance does not predict functional gene content."
- "Each study stopped at gene cataloguing. None proceeded to metabolic reconstruction. The capability gap sits at the end of all of them, in the same place each time."

**What a synthesis anchor is NOT:**
- "Together, these studies demonstrate the value of the approach." (Empty: doesn't name the pattern)
- "These findings are consistent with the pipeline's predictions." (Vague: which prediction, and how?)

Synthesis anchor content can alternatively be folded into the closing sentences of the preceding study paragraph if the combined paragraph stays under 15 sentences.

### Operation 7: Arc-break paragraphs

When a document contains 3+ major sections following the same structural arc (setup → evidence → conclusion), insert an arc-break paragraph at each section transition. This paragraph does not summarise the section just completed. It names what *changes* between the previous section and the upcoming one, foregrounding the difference before the reader enters the new section. Both halves of that contrast must already be established in the two sections it sits between. If the comparison is not already on the page, an arc-break is not the place to introduce it.

**Before (hard section break):**
> [End of §3] ...All three studies stop at MAG-level gene cataloguing without proceeding to metabolic reconstruction.
>
> ## 4. Nutrient cycling and the widest gap in the corpus
>
> The bridge signal between crop fertilisation research and MAG-based methods measured 0.94...

**After (arc-break inserted):**
> [End of §3] ...All three studies stop at MAG-level gene cataloguing without proceeding to metabolic reconstruction.
>
> ## 4. Nutrient cycling and the widest gap in the corpus
>
> Section 3 closed on studies that stop at gene cataloguing. Nutrient cycling inverts that arrangement: here the bridge signal is at its widest, and the genome-resolved work is correspondingly thinner.
>
> The bridge signal between crop fertilisation research and MAG-based methods measured 0.94...

### Operation 8: Batch cross-references

When a paragraph accumulates 3+ inline section cross-references, consolidate into a terminal note. Keep at most 1 inline reference, the one the reader genuinely needs to follow the current sentence.

**Before:**
> The companion planting effect connects disease suppression (§2.1) to resistome dynamics (§5.3) through shared community restructuring. The proposed mechanism (see §6.4) is testable at genome resolution. The ARG host attribution used in that study (§5.4) relied on correlation rather than co-localisation.

**After:**
> The companion planting effect connects disease suppression to resistome dynamics through shared community restructuring. The proposed mechanism is testable at genome resolution. The ARG host attribution used in that study relied on correlation rather than co-localisation. (Cross-references: §2.1 disease suppression foundations; §5.3 resistome methods; §5.4 ARG annotation; §6.4 manure nexus.)

---

## Workflow

Apply in this order, but only the steps that are actually needed:

0. **Section-level scan first.** Does the section have 3+ consecutive study paragraphs? Does it repeat the same arc across 3+ major sections? If yes, apply Operations 6 and 7 before sentence-level work.
1. **Flag multi-fact sentences**: sentences with 3+ data items (Op 1).
2. **Flag buried definitions**: terms defined in parentheticals (Op 2).
3. **Flag implicit transitions**: consecutive sentences with no connective tissue (Op 3).
4. **Flag long parentheticals**: asides over 5 words (Op 4).
5. **Flag flat enumerations**: lists of 4+ terms (Op 5).
6. **Batch cross-references** if 3+ appear in one paragraph (Op 8).

## Stop condition

Stop when every triggered operation has been applied and no trigger remains. That is the operative stop: the trigger list is what starts this skill and what ends it.

Do not keep going on a general sense that the prose could read more easily. You cannot judge that reliably about text you have just written, and an expanding pass with no countable stop condition does not stop. If you believe more work is needed but no trigger fires, say so and leave the text alone.

## What this skill does NOT do

- It does not add breathing-room paragraphs, restatements, or analogies.
- It does not vary rhythm at the sentence level. `humanizer` owns that (§6, §7).
- It does not convert nominalisations. `humanizer` owns that via its active-voice rules (§11).
- It does not cut content.
- It does not add new findings, interpretations, or claims.
- It does not introduce em dashes. (The one em dash pair remaining in this file is inside Operation 1's *Before* text, where it is part of the fault being demonstrated. Leave it.)
