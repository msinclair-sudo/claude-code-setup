# Blind fact-check, 2026-10-20

A fresh subagent saw only `claims.yaml` and `sim.py` (and the web for the cited papers); never a storyboard or render.

- c1-c8, c10: supported. c10 nuance noted: Gotelli and Colwell warn that standardising by samples and by individuals "may produce very different results".
- **c9: inaccurate as first written** ("95% of 200 subsamples fall between 208 and 228"). The 2.5th and 97.5th percentiles are exactly 208 and 228, and draws tie on those values, so 194 of 200 (97%) fall inside. Rewritten: "the middle 95% of 200 subsamples span 208 to 228 taxa".
- c11: supported; "showed" made exact as "showed in simulations".
- Bibliographic details of all three papers match Crossref.

This is the error the check exists for: a percentile range stated as a coverage share, the kind of slip that reads as right on a polished slide.

# Blind fact-check of the metabarcoding tier 4, 2026-10-20

Same rules: the reader saw only `t4/claims.yaml` and `pipeline.py`, plus the cited papers.

- Supported: m1, m2, m4, m5, m9-m14, m16, c10, c11.
- **m3 overstated:** "carried by every bacterium" is in neither source (Caporaso et al. support the marker role). Now "a gene that bacteria carry"; rrnDB backs "one or more copies" per genome.
- **m6 wrong mechanism:** Suzuki and Giovannoni (1996) found reannealing pulling template ratios toward 1:1, with one primer pair; not per-template efficiency differences. The model's efficiencies are now labelled as the model's, and the paper is cited only for "PCR can distort template ratios".
- **m7:** arithmetic slip in the source line (1.95^25 is 17.8 million, not 17.6).
- **m8 slightly overstated:** McLaren et al. show a consistent multiplier *for a fixed protocol*; the claim now says so.
- **m15 number:** the 2.5th percentile is 58.975; `int()` truncated it to 58. Rounded, 59: "between 59 and 68". pipeline.py and sim.py now round.

Lesson for the skill: a citation can be right about the paper and wrong about the mechanism; the blind check opened the full text and caught it.
