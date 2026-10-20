# Design rules and how far the evidence goes

From two literature reviews kept in the owner's vault (`Apps/Research/Results/`): **EX** = how explanations are made and understood (deep run, critiqued); **FD** = how models are directed to make visual output (quick run, not critiqued). Effect sizes are Hedges' g or Cohen's d. "Secondary" means known through one overview of meta-analyses, not read in the original. Treat **moderate, secondary** as the ceiling for any rule here.

## Choosing the format
| Rule | Evidence | Strength |
|---|---|---|
| Animate only a change that must be understood | Animation beat static pictures by g ≈ 0.23 on average; 0.34-0.65 when features of change had to be learned, 0.04 otherwise | three meta-analyses agree on the average; conditions from one (EX) |
| Animate only for system-paced viewing | The animation advantage was significant only when system-paced (0.31); not significant at any level of learner control (it vanishes, it does not reverse) | one meta-analysis (EX) |
| Self-paced data reading: static or small multiples | Small multiples were more accurate and faster for self-paced analysis; animation was fastest only in a narrated presentation; viewers lost track of moving points | one lab study and a phone replication (EX) |
| Uncertainty: show outcomes, not just error bars | Hypothetical outcome plots beat static error bars for judging uncertainty | two crowdsourced studies, abstracts only (EX) |
| Interactive: the default view carries the message | About 85% of readers used central interactive content, about 5% a slider, fewer on mobile | one telemetry study (EX) |
| Predict before reveal, if anything is interactive | Asking readers to predict before seeing data reduced recall error | one study, full text (EX) |
| Liking is not learning | Fluent delivery raised judged learning, not learning; animation induced an illusion of understanding; a misconception-laden explainer left viewers as confident as a correct one | several single studies; a pattern, not a pooled result (EX) |

## Designing the steps
| Rule | Evidence | Strength |
|---|---|---|
| Segment, and let the designer set the segments | g = 0.34; designer-made 0.41 vs learner-made 0.20 | one meta-analysis, secondary (EX) |
| Signal what to look at | g = 0.43 | moderate, secondary (EX) |
| Put words beside their picture; time narration to it | spatial g = 0.63, temporal g = 0.78 | moderate, secondary (EX) |
| Remove decoration that stays on screen | removing persistent seductive details helped (0.43); transient ones did not matter (0.12, ns) | one meta-analysis, secondary (EX) |
| Speak words that sit beside a picture | modality effect 0.38, 0.20 after bias adjustment | one meta-analysis, secondary (EX) |
| Keep each spoken segment short | long, complex narration did worse than written text; shortening it restored the effect | one author pair, abstracts (EX). The 35-word cap is our heuristic |
| Captions on: they help, especially for second-language listeners | adding on-screen text to narration helped (0.29); same-language captions for L2 viewers 0.99 | one meta-analysis each, secondary (EX) |
| Never speed playback up | costs mild at 1.4-1.5×, larger at 2× | two meta-analyses read as abstracts (EX) |
| A chart title steers which message is read | misaligned titles biased recall | one group, abstracts (EX) |
| Animated transitions between chart views: use sparingly; no staggering | transitions helped tracking except for stacked bars (24 adults); staggering negligible or negative | single studies (EX) |

## Voice
| Rule | Evidence | Strength |
|---|---|---|
| A modern neural voice is acceptable for learning | small studies mostly found no learning difference from a human voice; older engines carried a measurable cost | mostly abstracts, several from one group (EX) |
| Expect lower social and trust ratings than a human voice | several studies | (EX) |
| Speaking rate 150-170 wpm | YouTube norm only; no comprehension evidence | heuristic |

## Making it with a model
| Rule | Evidence | Strength |
|---|---|---|
| Plan before building | removing the planner in a code-to-video pipeline cut aesthetics from 79 to 38 | one preprint (FD) |
| Check with tools, not by looking | external checks (renderer errors, DOM geometry, verification programs) outperformed self-inspection; VLMs detected overflow poorly; a model's self-critique degraded over iterations | several single studies (FD) |
| Stop after 1-3 fix rounds | most gain came in round one; more rounds degraded code | several studies (FD) |
| Look up the API after a render error | retrieving API documentation after a Manim render error raised render success | one preprint (FD) |
| Place animation objects on a grid | an anchor grid plus occupancy table cut overlap and occlusion | one preprint (FD) |
| Prefer matplotlib to seaborn for generated charts | GPT-4 invalid-code rate 3.29% vs 25.41% | one benchmark (FD) |
| Watch for slide overflow above all | text overflow and wrapping were 53% of slide penalties | one preprint (FD) |
| Model-written accuracy checks are weak; ground claims in sources | a model judge correlated 0.14 with humans on accuracy; LLM summaries overgeneralised findings (OR 4.85) | single studies (EX) |

## What nobody has measured
Expert audiences; narrated slides against animation for a method; labels on depictions ("illustrative", "schematic"); real against illustrative depictions; neural TTS listening effort. Rules here that touch these are judgement, not evidence.
