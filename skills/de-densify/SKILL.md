# De-Densify Skill

## Purpose

This skill addresses structural density in academic prose — specifically in Results, Discussion, and literature review sections where data-heavy sentences and evidence parades accumulate faster than the reader can process them. It operates at the **sentence-splitting and document-structure level only**. It does not add restatements, analogies, padding, or breathing-room paragraphs — those conflict with deslop's density rule and should not be used. Run deslop first; run this skill after if structural density problems remain.

## When to use this skill

Use **after** deslop and humanizer have been applied. This skill handles problems those tools cannot reach:

**Triggers:**
- A sentence contains 3+ distinct facts, numbers, or technical terms simultaneously
- A technical term is defined inside a parenthetical rather than given its own sentence
- A paragraph accumulates 3+ inline cross-references
- A sentence contains a list of 4+ mechanisms, gene names, or technical terms
- Three or more consecutive paragraphs each introduce a different study, dataset, or biological system (evidence parade)
- A multi-section document repeats the same structural arc across 3+ sections

**Do not use when:**
- deslop's density score is already passing — do not expand to fix a problem that isn't there

---

## Paragraph size constraint

Paragraphs must contain at least 3 sentences. Never leave inserted connective tissue as a 1–2 sentence orphan — fold it into an adjacent paragraph or expand it to meet the minimum. There is no target paragraph length; size follows content.

---

## Operations

### Operation 1: Split multi-fact sentences

When a sentence contains 3+ distinct facts (numbers, cluster IDs, metric values, statistical tests), distribute them across separate sentences. Lead with the overall pattern; follow with the evidence in order of interpretive interest.

**Before:**
> The five clusters — quantum computing (conductance 0.020, peripherality 0.846), synthetic chemistry (0.069, 0.915), astrophysics (0.006, 0.884), social sciences (0.098, 0.897), and computer vision (0.110, 0.858) — all had conductance below 0.12 and peripherality above 0.83.

**After:**
> All five far-field clusters showed low conductance and high peripherality, confirming their structural isolation from the core literature. Astrophysics was the most isolated, with the lowest conductance in the corpus (0.006) and peripherality of 0.884. Quantum computing (0.020, 0.846) and social sciences (0.098, 0.897) were similarly detached. Synthetic chemistry and computer vision showed slightly higher conductance (0.069 and 0.110 respectively) but remained well below the corpus median.

### Operation 2: Unpack inline definitions

When a technical term is defined inside a parenthetical or appositive clause, extract the definition into its own sentence. This gives readers the term before its use, not simultaneously.

**Before:**
> Bridge signal (the ratio of reaching edges to total inter-cluster edges) quantifies the proportion of semantically distant citations between two clusters, with values above 0.85 indicating near-complete vocabulary divergence.

**After:**
> Bridge signal quantifies the proportion of semantically distant citations between two clusters. It is computed as the ratio of reaching edges to total inter-cluster edges. Values above 0.85 indicate near-complete vocabulary divergence between the two communities.

### Operation 3: Add signposting sentences

When the logical relationship between consecutive sentences is implicit, add a signposting sentence that makes it explicit. These carry no new data — only connective tissue.

Types (from Hyland's metadiscourse framework):
- **Code glosses:** "In other words," "that is," "specifically"
- **Frame markers:** "The first property is...," "Turning to the second finding..."
- **Transition signals:** "The distinction matters because...," "This pattern reverses when..."

**Before:**
> Conductance measures the ratio of inter-cluster edges to total edges. High conductance indicates poor separation. Low-density clusters may represent heterogeneous groupings. The orphan rate fell to 2.1%.

**After:**
> Conductance measures the ratio of inter-cluster edges to total edges. High values indicate that a cluster connects more to the rest of the network than to itself — a sign of poor separation from its neighbours. A related but distinct signal comes from internal density. Low-density clusters may represent heterogeneous groupings where papers share a broad label but not a coherent research programme. A third structural signal is the orphan rate, which fell to 2.1%.

### Operation 4: Expand parenthetical asides

If a parenthetical aside exceeds 5 words and contains information the reader needs, extract it into its own sentence(s). Short parentheticals (cluster IDs, p-values, single citations) can stay inline.

**Before:**
> The scoring methodology (which operated through an overwrite model in which each scoring act replaced the previous value for all papers it covered, with no averaging or multi-signal resolution) concentrated human effort on the most relevant portion of the corpus.

**After:**
> The scoring methodology concentrated human effort on the most relevant portion of the corpus. It operated through an overwrite model: each scoring act replaced the previous value for all papers it covered. There was no averaging and no multi-signal resolution.

### Operation 5: Unpack enumerations

When a sentence lists 4+ technical terms, mechanisms, or gene names, the sentence may be under the word-count ceiling but still overloaded.

**Three strategies:**

**a) Group by principle** — organise into 2 categories with a bridging phrase:
> Before: "They suppress pathogens through antibiosis, competition for iron, mycoparasitism, and induced systemic resistance."
> After: "Two mechanisms act directly on the pathogen — antibiosis and competition for iron. Two act through the host: mycoparasitism triggers plant defence signalling, and induced systemic resistance primes distal tissues."

**b) Lead with the count, follow with the list:**
> "Four mechanisms contribute to pathogen suppression. Antibiosis and iron competition act directly on the pathogen. Mycoparasitism and induced systemic resistance act through the host."

**c) Distribute at a maximum of 2 new terms per sentence.**

**Exemption:** Gene name lists serving as evidence catalogues (e.g., *nifHDK*, *acdS*, *phoD*) can stay compressed when the reader is expected to scan rather than absorb each one.

### Operation 6: Synthesis anchors (evidence parades)

When 3+ consecutive paragraphs each introduce a different study, dataset, or biological system, insert a synthesis anchor after every 2–3 studies. A synthesis anchor does not introduce new evidence — it names the pattern accumulating across the studies just described, explains why it matters, and orients the reader toward what comes next.

A synthesis anchor answers: "What do these studies, taken together, show that no individual study shows?"

**What a synthesis anchor IS:**
- "Across these systems, the same pattern recurs: taxonomic abundance does not predict functional gene content."
- "Each study stopped at gene cataloguing. None proceeded to metabolic reconstruction. The capability gap is not between studies — it is at the end of all of them."

**What a synthesis anchor is NOT:**
- "Together, these studies demonstrate the value of the approach." (Empty — doesn't name the pattern)
- "These findings are consistent with the pipeline's predictions." (Vague — which prediction, and how?)

Synthesis anchor content can alternatively be folded into the closing sentences of the preceding study paragraph if the combined paragraph stays under 15 sentences.

### Operation 7: Arc-break paragraphs

When a document contains 3+ major sections following the same structural arc (setup → evidence → conclusion), insert an arc-break paragraph at each section transition. This paragraph does not summarise the section just completed. It names what *changes* between the previous section and the upcoming one — foregrounding the difference before the reader enters the new section.

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
> Stress biology showed the narrowest gap in the corpus — three genome-resolved papers exist, and the bridge signal is lower than any other dimension. Nutrient cycling inverts this pattern. The bridge signal is the highest, and the reading finds correspondingly less genome-resolved work.
>
> The bridge signal between crop fertilisation research and MAG-based methods measured 0.94...

### Operation 8: Batch cross-references

When a paragraph accumulates 3+ inline section cross-references, consolidate into a terminal note. Keep at most 1 inline reference — the one the reader genuinely needs to follow the current sentence.

**Before:**
> The companion planting effect connects disease suppression (§2.1) to resistome dynamics (§5.3) through shared community restructuring. The proposed mechanism (see §6.4) is testable at genome resolution. The ARG host attribution used in that study (§5.4) relied on correlation rather than co-localisation.

**After:**
> The companion planting effect connects disease suppression to resistome dynamics through shared community restructuring. The proposed mechanism is testable at genome resolution. The ARG host attribution used in that study relied on correlation rather than co-localisation. (Cross-references: §2.1 disease suppression foundations; §5.3 resistome methods; §5.4 ARG annotation; §6.4 manure nexus.)

---

## Workflow

Apply in this order, but only the steps that are actually needed:

0. **Section-level scan first.** Does the section have 3+ consecutive study paragraphs? Does it repeat the same arc across 3+ major sections? If yes, apply Operations 6 and 7 before sentence-level work.
1. **Flag multi-fact sentences** — sentences with 3+ data items (Op 1).
2. **Flag buried definitions** — terms defined in parentheticals (Op 2).
3. **Flag implicit transitions** — consecutive sentences with no connective tissue (Op 3).
4. **Flag long parentheticals** — asides over 5 words (Op 4).
5. **Flag flat enumerations** — lists of 4+ terms (Op 5).
6. **Batch cross-references** if 3+ appear in one paragraph (Op 8).

## Stop condition

Stop when a reader in the same broad field can read each paragraph once and extract the main point without re-reading. Do not expand further — deslop's density rule takes precedence over any impulse to add more scaffolding.

## What this skill does NOT do

- It does not add breathing-room paragraphs, restatements, or analogies — those conflict with deslop.
- It does not vary rhythm at the sentence level — deslop owns that.
- It does not convert nominalisations — deslop owns that via active voice rules.
- It does not cut content.
- It does not add new findings, interpretations, or claims.
- It does not introduce em dashes.
