# Stage C usability re-test: protocol (written before any writer runs)

The criteria are in `../heldout/criteria.md` and the topics in `topics.md` (seed 20261041). v4 is frozen, with
skill content as at b59851f. Twelve pieces: for each topic, raw 1 and raw 2 (the result note) and view 1 and view 2
(`kn.py view` of the frozen-v4 knowledge note).

## Topics

| Topic | Name |
|---|---|
| T1 | Held-out prediction of community profiles from environment |
| T2 | Featureless nodes in graph-diffusion fusion |
| T3 | Stepwise denitrification in constraint-based metabolic models |

- **T1:** C-PREDICT, critiqued (category 4), about 12,200 words raw.
- **T2:** C-GHOSTFUS, harness (category 7), about 3,900 words raw.
- **T3:** C-STEPDEN, uncritiqued (category 6), about 3,200 words raw.

Each topic line below is written from the note's own research questions, with no project names.
- **T1:** "predicting the make-up of ecological communities, microbial ones especially, from environmental
  conditions at sites not used to build the model: whether profiles of taxa or profiles of genes and traits are
  predicted better, how predictability changes with taxonomic or functional resolution, and what makes such
  prediction succeed or fail"
- **T2:** "what happens when graph-diffusion methods, which spread node features across a graph, must handle
  nodes that have no features of their own: whether filling them in preserves the links they carry, how the share
  of such nodes affects reliability, and how they interact with a denoising step"
- **T3:** "how constraint-based (flux balance) metabolic models represent denitrification step by step, whether
  they report nitrous oxide (N2O) as a distinct output, and how this compares with kinetic and trait-based models"

## Writers (12 fresh agents)

Each writer has one folder in the job's scratch space, named by its piece (`T<k>-<n><L>`), holding only its input.
The prompt is v3's (`../../../usability/protocol.md`) word for word, with only the topic line and the folder
differing:

> Write a standalone piece of about 1,200 words on <topic>. The readers are scientifically literate but outside
> the field (for example, a researcher in a neighbouring discipline). The piece must stand alone: your reader has
> not seen the material you are given and cannot ask you about it. Your only source is the material in <folder>.
> Read all of it and use nothing else: no web, no other files. Save the piece as piece.md. Then, in a separate
> file notes.md, list (1) anything you wanted to say or needed for the piece and could not find in the material,
> and (2) anything in the material that was hard to use.

## Fact-checks (12 fresh agents)

Each fact-checker gets one piece under its letter name and the full knowledge note (the audit version, the vault
note), and nothing else. It is not told which input the piece came from. It classes every statement in the piece:
- supported;
- overstated (firmer, wider or more general than the entry);
- number wrong;
- unsupported (in no entry);
- do-not-say violation;
- absence stated as fact (an untested or unknown point given without whether it was searched for);
- access overreach (a finding the note marks as read only in abstract, or known second-hand, interpreted beyond
  what its authors state);
- illustration (the writer's own example or analogy, which asserts nothing about the research).

It writes `<piece>.factcheck.md`: one line per statement, with its class and the entry IDs, then the counts.

## Blind readers (6 fresh agents, one per pair)

Each blind reader gets:
- the pair's two pieces, as `T<k>-<n>A` and `T<k>-<n>B`;
- the topic line, as the scope;
- Part A of the marking scheme (`marking-scheme.md`) with its anchors, and its rules.

It follows those rules:
- grade each piece on its own first;
- choose the lower score when between two anchors;
- quote every error;
- judge accuracy with its own knowledge, opening no other file.

It writes a Part A sheet for each piece (`<piece>.blind.md`, in the scheme's sheet format, Part A only, with the
errors quoted), then the per-pair sheet (`T<k>-pair<n>.blind.md`: preferred, confidence, why). It is not told how
the pieces were made.

## Order and blinding

- The key (`ab-key.sealed.md`) is written by script before any writer runs, and it is not opened until the owner
  has graded.
- Writers run by folder name.
- Pieces are collected under their letter names.
- Fact-checkers and blind readers see only letter names.
- Each topic is one session (C3 to C5), 15 minutes apart. C6 compiles results by letter and copies the owner's
  packet to `temp/stage-C/` in the vault.

## Amendment (2026-10-24, during C4)

In T2, three writers saved `piece.md` to their shared working directory before moving it, and one left it there; v3's prompt does not say where to save. Each file was traced by its writer's report and its title, and moved to its own folder before collection. All four T2 pieces are distinct; T2-2A had kept its final version in a side folder.

From T3, one logistics line follows the unchanged prompt: "Save both files in that folder." It changes nothing about the content asked for.
