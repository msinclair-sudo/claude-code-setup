# Usability test: writer's view against raw result notes (protocol, written before results)

Does a knowledge note give a writer something usable? For three topics, a writer agent writes the same
standalone piece twice: once from the writer's view only (`kn.py view`, commit 66d17ef), once from the raw
result note or notes only. A baseline: no writing guidance, and the writing skill comes later.

## Topics

| Topic | Knowledge note | Run type | Raw input | Writer's view |
|---|---|---|---|---|
| 16S | 16S amplicon sequencing from sample to count table | deep + standard, critiqued, large (410 claims) | MB-01 + MB-02 (42,837 words) | 22,371 words |
| TSL | Term specificity and multi-level labelling | biblion harness, partly verified (a Refuted section) | the TSL note (1,790 words) | 2,084 words |
| NFERT | Synthetic nitrogen fertiliser and soil microbial nitrogen cycling | uncritiqued | the NFERT note (2,440 words) | 2,273 words |

TSL is the only harness run among the six development notes, so it fills the "standard or harness" slot
although it is not a soil or microbiology topic. The only standard run, MB-02, is already part of the 16S set.

## Writers

Six fresh agents. Each sees one folder holding only its input. Same prompt for all six, the topic line differing
by topic only:

> Write a standalone piece of about 1,200 words on <topic>. The readers are scientifically literate but outside
> the field (for example, a researcher in a neighbouring discipline). The piece must stand alone: your reader has
> not seen the material you are given and cannot ask you about it. Your only source is the material in <folder>.
> Read all of it and use nothing else: no web, no other files. Save the piece as piece.md. Then, in a separate
> file notes.md, list (1) anything you wanted to say or needed for the piece and could not find in the material,
> and (2) anything in the material that was hard to use.

Topic lines: 16S "16S rRNA gene amplicon sequencing: how a sample becomes a table of taxon counts, how far those
counts can be trusted, and how samples are compared"; TSL "how methods that label groups of documents decide how
specific a term is, and how they order terms from general to specific"; NFERT "synthetic nitrogen fertiliser:
the energy and emissions of making it, and whether soil microbes can reduce how much of it is needed".

## Checks, per topic

- **Fact-check, each piece separately**, by a fresh agent with the full knowledge note (the audit version) and
  nothing else: every statement in the piece is supported, overstated (firmer, wider or more general than the
  entry), unsupported (in no entry), or a do-not-say violation; numbers checked against the entries. The checker
  is not told which input the piece was written from.
- **Blind comparison**, by one fresh agent per topic: the two pieces labelled A and B by `random.Random(20261023)`
  (one draw per topic, in the order 16S, TSL, NFERT), with the research questions the research asked as the scope.
  It compares coverage of the important points, clarity, and anything missing or wrong, and says which it would
  rather give a reader and why. It is not told how the pieces were made.
- **Gaps**: each writer's notes, and for the view writers what the view did not give them.

Reported per topic and across the three. The six pieces are kept for the owner to read.
