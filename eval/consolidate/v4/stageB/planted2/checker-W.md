# Faithfulness check: prompt for a fresh agent

Give a fresh agent this prompt and one packet from `kn.py packets --hints` (each claim or do-not-say entry beside
the note text it says it came from, and the words a script could not find there). It sees no other part of the
knowledge note and no sources. It checks copying, not truth: the research already verified the sources.

After the builder fixes the faults, a different fresh agent re-checks the fixed entries with the same prompt
(`kn.py packets <note> <dir> --only <ids> --hints`). The builder never grades its own corrections, and never sees
the packets or their hints: it gets only the verdict lines.

---

You are checking that entries in a knowledge note were copied faithfully from research result notes. Each entry
below is followed by the sentences of the result note it was built from (quoted, with their inventory IDs). Do
not open sources, search, or judge whether the research is right. Judge only whether the entry says what its
quoted text says.

For every entry, return one line: `<id>: ok` or `<id>: <fault>: <one sentence>`, where fault is one of:

- `stronger`: the entry is firmer than its text: standing raised, a hedge dropped, scope widened (one setting
  stated as general), a single study stated as a pattern.
- `conf`: `conf`, `class` or `limit` gives a value its text does not state (a standing inferred from tone, the
  basis quoted does not say it, or `limit: access` where the text gives no access reason; abstract only, not obtained, second-hand and "not read
  in the original" are access reasons). `not stated` is always
  acceptable.
- `numbers`: a figure differs from its text, lost its definition or denominator, or figures from different
  sources were combined.
- `absent`: the entry says something its quoted text does not contain.
- `critic`: the quoted critique corrects the claim, or a source's label in `src`, and the entry keeps the
  uncorrected version.
- `merged`: two cases the text keeps apart are folded into one entry.
- `holds`: the setting in `holds` is missing or differs from the text.

Be strict and literal. An entry may leave out detail its text gives: a second example, another member of a list, a
figure it does not use. That is ok. Leaving out a qualifier is not leaving out detail. Dropping a scope ("in one
soil", "in this model", "on mocks"), a hedge ("may", "suggests"), a condition or a denominator makes the claim
stronger, and is `stronger`. So is dropping a "but not …" or a contrary finding its text gives. An entry may not
add anything its text does not say, including a setting that narrows the claim: an added setting is `holds`,
anything else added is `absent`. A claim restricted to fewer of the cases its text covers (the text says soils and
sediments, the entry says soils) is ok. Fields must agree with each other: a label in `src` that contradicts `conf`
is `conf`.

Under some entries, "Not found in the cited text" lists words or numbers a script could not find in the quoted
text. They show where to look, not what is wrong. A paraphrase, another word form, an abbreviation spelled out, or
a word that adds nothing is fine. Judge, as always, whether the entry says anything its cited text does not support.
An entry with no hint gets the same care as one with hints: the script cannot see what an entry leaves out.

Under some claims, "In the cited text, not in the entry" lists hedge, negation, contrast and scope words ("may",
"not", "but", "only", "by this corpus") from the quoted text that the entry does not carry, each with the words after
it. If the dropped words limit what the entry still says, the entry is `stronger`. If they qualify only a detail the
entry left out, it is ok.

Citekeys in `src` are identifiers, not claims: a key may carry another year (an existing bibliography's key is
kept), so judge the labels beside a key, never the key itself. End with a count of each fault.
