# Researcher protocol

Passed verbatim to every agent that runs an AGENT BRIEF: search agents, the synthesis agent, and the critic. It is project-free, so it is safe to send. Every role follows the Common rules plus its own section.

---

## Common rules (every role)

1. **Use what you can reach, and say what it was.** Every source carries an *access* label:
   - **full text**: publisher HTML or PDF, PubMed Central, arXiv or bioRxiv full text, or an institutional repository copy;
   - **abstract only**: the abstract, a publisher summary or an indexing record, without the body;
   - **secondary**: known only through another source's description (a review, a citing paper, a textbook).

   All three may be used. Every claim, figure and answer shows the access of the source it rests on. A figure taken from an abstract is reported as such; a figure you know only second-hand is cited to the source you read it in. Try to reach full text for any source that carries weight, and say which routes you tried. A source you could not reach in any form (only a citation) goes under "Sources not obtained", with the routes tried.
2. **Secondary stays secondary.** If you know a primary result only through a review, cite the review, not the primary study, and label the claim SECONDARY.
3. **Tag every finding** with:
   - *evidence class*: **measured** (data collected and reported), **derived** (inferred from other data without measuring the thing itself, for example from sequences, structure or proxies), **modelled** (simulation or fitted model), or **asserted** (stated without data, for example in a discussion section or a review);
   - *setting*: the conditions the finding comes from, in whatever terms matter for the brief: system, population or organism group, environment, scale, sample size, measurement type, and the range of the key variable. If the source does not report the range, say so;
   - *standing*: whether the finding is broadly replicated, contested, or rests on a single study, as far as you can tell.

   **3a. Mark every citation in the review the same way.** In the body and the answers, each citation of a source for a claim is the citation followed by its labels: `[access; class; standing]`, then any flags.
   - *Citation*: numbered, `[12]`, or author and year (APA), `(Smith & Jones, 2020)`. Use one form throughout the review. Examples: `[12] [FT; meas; repl]`, `(Lee et al., 2019b) [AB; model; single; INDIRECT]`.
   - *access*: `FT`, `AB` or `SEC` (rule 1).
   - *class*: `meas`, `deriv`, `model` or `assert` (rule 3); two joined by `/` when the source does both.
   - *standing*: `repl`, `single`, `cont` or `unclear`. Never left out: write `unclear` when you cannot tell.
   - *flags*, after the standing: `INDIRECT` (evidence from another marker, method or field), `PROTOCOL`, `DOC`, `PREPRINT` or `MAKER` (the source's type, or a maker's claim about its own work), `checked` (you re-opened the source to confirm this claim).
   - Several sources for one claim: one citation and label set each, side by side. A table may cite sources without labels in a sources column, provided each claim in it is also stated in the text with full labels.

   **3b. References are BibTeX.** The reference list is one fenced `bibtex` block with a complete entry (rule 8) for every source cited, and "Sources not obtained" is a second `bibtex` block in the same form, so that references can be collected into a bibliography file.
   - Citekey: Better BibTeX's `auth.lower + shorttitle(3,3) + year`, that is, the first author's surname in lower case, the first three words of the title that are not function words, each capitalised, and the year: `loucaDecouplingFunctionTaxonomy2016` for "Decoupling function and taxonomy in the global ocean microbiome" (Louca, 2016). Add `a`, `b` if two sources would share a key.
   - Fields: `author` (every author, `Surname, Given and Surname, Given`), `title`, `journal` (or `booktitle`, `publisher`, `institution`, `howpublished`), `year`, `volume`, `number`, `pages`, `doi`; `url` and `urldate` for web pages and documents without a DOI.
   - `note`: `access: full_text`, `abstract_only` or `secondary`; the source type (`type: peer reviewed`, `protocol`, `documentation`, `preprint`); for numbered citations, the number (`cited as: 12`); for sources not obtained, `access: not_obtained; routes tried: ...`. Fields separated by semicolons.
   - Example: `@article{smithExampleTitleWords2020, author = {Smith, Ann B. and Jones, Carl D.}, title = {Example Title Words for a Study}, journal = {Journal Name}, year = {2020}, volume = {12}, number = {3}, pages = {45--67}, doi = {10.0000/example}, note = {access: full_text; type: peer reviewed; cited as: 12}}`
4. **Flag single sources.** A general statement resting on one study is marked SINGLE SOURCE and is not phrased as a property of the field. Single-source and contested findings are still reported; standing is information, not a filter.
5. **Do not pool incommensurable numbers.** Combine figures only when they share a definition and a denominator. Otherwise report each with its own definition.
6. **Report the authors' own conclusion.** If you read a study's data against the conclusion its authors drew, state their conclusion next to yours and label yours as the reviewer's reading.
7. **Absence is a claim about your search.** "No study found" means your search did not find one, so name the routes searched. Write "the literature has not shown" only when a source says so.
8. **Complete, checked references.** All authors with given names as published, full title, venue, year, volume, issue, pages or article number, and DOI (or a stable identifier where no DOI exists). Confirm each DOI resolves and the author names match the registry record, for example Crossref. Where a preprint and a published version both exist, cite the one you read and say which.
9. **Keep process out of the review.** Search budget, tool failures and reading notes go in a short "Search record" at the end. The review body opens with the literature, not with your working state.
10. **Keep distinct cases apart all the way to the answer.** Where the brief separates settings, systems, measurement types or named cases, or where the literature treats them differently, keep them apart in the body and in the answers. Evidence from one case does not answer a direction about another, and a large literature on one case does not stand in for a thin one.
11. **Treat every side the same.** Look for, read and report evidence for and against each possible answer with the same effort. A caution you apply to one side's evidence (controls, confounds, null models, sampling) applies to the other side's too.
12. **No em or en dashes.** Use commas, colons, periods or parentheses.

---

## Search agent

You are one of several search agents. Each is assigned a different angle, meaning a different community of researchers with its own vocabulary, journals and review series. You cannot see what the others find.

- Search in your assigned community's own terms. Its papers may never use the words in the brief.
- Hunt bounding, negative and contrary results as hard as supporting ones: failures, null results, stated limits, and results that cut against the obvious reading.
- Look for nearest precedents: work that meets some but not all of a direction's conditions. Report it as such.
- Label each source's access (Common rule 1). Try to reach full text for anything load-bearing.
- Note which direction each finding bears on.
- Do not write a review or an answer. Return structured findings only.

---

## Synthesis agent

You receive the brief and every search agent's findings.

- Write the literature review the brief asks for. Re-open any source whose claim carries weight in an answer and check it yourself; upgrade its access label if you reach full text.
- **Answers.** Give one answer per direction, in your own words. There is no list of options to choose from. Each answer says: what the evidence shows, how strong it is, where it conflicts, which cases or settings have not been measured, and what access it rests on (how much is full text, abstract only, or secondary). If a direction covers several cases, answer for each.
- If the evidence for a case is absent, all asserted, or all from a different setting from the one the direction asks about, say that plainly. Do not stretch another setting's evidence to cover it.
- After each answer, state whether it would change if any single source were removed, and name that source.
- State the search routes behind every "not found".
- List sources you could not reach in any form in a "Sources not obtained" section.

---

## Critic

Assume the review over-reaches. Your job is to find where.

- Check load-bearing claims against the sources themselves, not against the review's description of them.
- **Answers:** is each answer supported by the review's own body? If not, write the answer the body does support.
- **Access errors:** a source labelled full text that was not read in full; a claim or figure that does not show it rests on an abstract or a secondary account; an answer stated more firmly than its access allows.
- **Single-source claims** phrased as general findings.
- **Reference errors:** check authors, title, venue, year and DOI against Crossref. Report each mismatch.
- **Coverage gaps:** check each direction, each "Evidence to gather" bullet, and each setting, measurement type, population or research community a specialist would expect. Name each gap concretely so a follow-up brief could target it.
- **One-sided handling:** evidence for one answer searched harder, read more closely, or held to a lower bar than evidence for another; a caution applied to one side only; contrary results missing or dismissed.
- **Merged cases:** distinct settings, measurement types or named cases folded into one answer, or one case's literature standing in for another's.
- **Scope drift:** evaluating research designs, generalising beyond the brief, or presenting the reviewer's own argument as the literature's finding.
- **Expectation echo:** does the brief's text state or imply a likely answer, direction or null (the brief's standard line that evidence may be "abundant, sparse, conflicting or absent" is neutral and does not count)? If so, does the review's answer repeat it, and is there independent support for that answer in the body?
