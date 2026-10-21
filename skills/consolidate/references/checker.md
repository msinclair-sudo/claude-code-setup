# Faithfulness check: prompt for a fresh agent

Give a fresh agent this prompt and one packet from `kn.py packets` (each claim or do-not-say entry beside the
note text it says it came from). It sees no other part of the knowledge note and no sources. It checks copying,
not truth: the research already verified the sources.

---

You are checking that entries in a knowledge note were copied faithfully from research result notes. Each entry
below is followed by the sentences of the result note it was built from (quoted, with their inventory IDs). Do
not open sources, search, or judge whether the research is right. Judge only whether the entry says what its
quoted text says.

For every entry, return one line: `<id>: ok` or `<id>: <fault>: <one sentence>`, where fault is one of:

- `stronger`: the entry is firmer than its text: standing raised, a hedge dropped, scope widened (one setting
  stated as general), a single study stated as a pattern.
- `conf`: `conf` or `class` gives a value its text does not state (a standing inferred from tone, or the basis
  quoted does not say it). `not stated` is always acceptable.
- `numbers`: a figure differs from its text, lost its definition or denominator, or figures from different
  sources were combined.
- `absent`: the entry says something its quoted text does not contain.
- `critic`: the quoted critique corrects the claim and the entry keeps the uncorrected version.
- `merged`: two cases the text keeps apart are folded into one entry.
- `holds`: the setting in `holds` is missing or differs from the text.

Be strict and literal. An entry that is narrower or weaker than its text is ok. End with a count of each fault.
