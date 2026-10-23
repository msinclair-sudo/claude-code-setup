# Findings E: session text (tokens = bytes/4; local calibration says real tokens ~1.5x: 2.65 B/token)

Headline
1. Since 2026-10-06 every SessionStart orientation exceeds Claude Code's 10,000-byte hook limit (629/630 startups since 10-07). The model gets a 2 KB preview; scope, `next` line, reviewer ponytail never arrive (ponytail 0/92). Sessions run `harness whoami` by Bash (743 calls, median 16.8 KB), repeating the 17 KB scope already in their spawn prompt. Dropping scope from whoami: ~4.5k tok per spawned session, ~185k tok/day.
2. mark --done still says SendMessage lead (291 sent) though doorbell rang since obs 91. Stop hook "present it" block fired 772 times; each forces a turn re-reading median 186k cached tokens; only 16% ended in mark --done.
3. spec.md / why.md never Read (0 in 997 sessions). Cost is skill text at every start: Reports/Research sections unused; prose restating what CLI prints. ~1-1.3k tok per lead/lane skill load.

Method: hook text the model sees = jsonl `rendered` field (attachment.type hook_success for SessionStart/UserPromptSubmit; hook_additional_context for PostToolUse mail; hook_blocking_error for Stop). Stop exit-0 stdout and PostToolUse hook_success have no rendered field -> never reach model. Over 10,000 B Claude Code saves output to tool-results/hook-*-stdout.txt and shows "Preview (first 2KB)"; largest shown whole was exactly 10,000 B. 997 transcripts 10-02..10-23; mail doorbell/<node>/delivered.jsonl 6,515 msgs.

## Startup by role (bytes)
| role | sessions | spawn prompt | SessionStart whoami produced->seen | skills loaded | whoami by Bash | harness text seen median | first-turn ctx |
|---|---|---|---|---|---|---|---|
| lane (harness, upward) | 588 | 17.2K (scope 17.0K) | 17.8K->2.2K (persisted 99% since 10-07) | 6.8K median (upward only 44%) | 16.5K in 579 | 41.9K ~10.5k tok | 66k tok |
| lead (+downward) | 163 | 17.2K | 18.0K->2.1K | 31.9K | 18.4K in 142 | 59.6K ~14.9k tok | 67k |
| reviewer (+reviewer, ponytail) | 92 | 18.3K | 22.0K->2.4K (ponytail 0/92) | 26.5K + ponytail-review 5.1K per mark T.review | 21.8K in 82 | 67.0K ~16.7k tok | 66k |
| rank 0 | 2 files | 0.1K | 16.7K->2.0K | 85.5K over 8 loads | 16.6K | 104K | 76k |
| intermediary | 93 | sys prompt 34.2K (skill 14.6K, voice 1.2K, scope 18.1K) | - | - | - | 34.9K ~8.7k tok | 21k |
| documenter | 58 | sys prompt 49.4K (skill 9.7K, voice 1.2K, two writing skills 19.9K, scope 18.1K) | | | | 50.2K ~12.6k tok | 23k |
| design | 1 | 18.0K | | | | | 22k |
hook-subagent injects ~3.4K ponytail into reviewer subagents. Non-harness: CLAUDE.md+MEMORY 57-66K, skill listing 30K, MCP/tools ~18K. spec.md: 0 Reads; 27 grep/sed calls in ~20 sessions (72K). why.md never.

## Per turn hook text seen
| | all 5,941 turns | since 10-17 (919) | 10-23 (76) |
| median/p90/max | 667/2,202/18,146 B | 573/1,778/7,194 | 777/1,625/4,515 |
| any hook text | 77% | 82% | 80% |
| hook-orient | 69%, 621 B | 77%, 533 | 72%, 683 |
| hook-stop blocks | 26%, 666 B | 21%, 759 | 26%, 759 |
| mail PostToolUse | 12%, 822 B | 13%, 677 | 5% |
| per node-day median/p90/max | 16.3K/75K/413K | 9.8K/33K/72K | |
Wakes 3,448 x 747 B (harness 158 B + CC wrapper ~590). 1,747 forced Stop turns re-read median 186k cached tokens each: 375M cache-read tokens.
Top repeats: 5,121 "They are marked read: act on them now, or say on the record why not." (harness-mail render():227, 348K); ~736 present-it Stop block (cmd_hook_stop 5244-5260, ~470K); 4,690 "Doorbell — N message(s)"; 1,120 TaskCreate line (gone 10-22); ~1,000 rank-0 sweep counts (queue_items 4365, 95K).

## Mail
6,515 delivered, 3.67 MB (~919k tok), 23 nodes; node-day median 29 msgs/9K, p90 111, max 345. dev_dag 91/day, main 62, dev 60. Free text by sessions 3,870 (3.0 MB, 81% of bytes, median 550 B, p90 1.6K); test queue 1,064; presentation templates 812; halt/resume 323; harness 298; intermediary 152. Templates: presented 'T' (cmd_mark 5743-5773) ~717; check of H (testq_ring 9082) 630; owed (owed_ring 4500) 116; ask_to 19926 152; wake_text 25591 3,448.

## CLI output (Bash tool_result)
whoami 743 calls median 16.8K p90 19.4K total 9.3 MB (17.5% of all harness output); brief 1,665 3.1K/9.9K 6.8 MB; note 1,943 0.6K/10.2K 6.7 MB; check 1,825 0.7K/2.1K; ask 1,776 140 B (--show 3.1K); mark 1,034 0.9K (--done 1.0-1.2K); pairs 728 1.0K/5.4K; test 1,275 0.5K. All harness Bash output 53 MB (~13.3M tok).
Overlap: verbatim small (<=686 B skill-spec 10-word runs). sync-spec.sh checks only no own spec copy + pointer. Cost is restatement, not copy-paste.

## Findings
1. whoami prints 17 KB scope every start; CC cuts to 2 KB preview; session pays again by Bash. where 1622-1653, 1770-1775; harness SKILL.md:13-20, :87; templates/compact-instructions.md last line; harness-reviewer SKILL.md:11. cut: drop scope_block from whoami -> one line "scope in your first prompt; harness charter --full"; orientation <10 KB (~1K lane, ~4.5K reviewer); skill step 1 + compact template: "orientation above; rerun only if missing". saves ~4.5k tok/spawned session, ~185k tok/day, a tool call. guarded: none pins whoami scope; test_every_first_prompt_carries_it unaffected. log owner 10-06, 172. risk owner's call. evidence: 629/630 persisted-output previews; PONYTAIL MODE ACTIVE 92 produced, 0 delivered; 21 Reads of saved hook file.
2. BUG SessionStart records all orientation items told though model saw 2 KB (1762-1768). cut: #1, meanwhile don't record from hook call (log 202 rule). risk unsure. evidence: queue/next, decide/blocked, owner/report/research lines after the scope cut in 629 deliveries, still marked told. (= A#5)
3. mark --done SendMessage block superseded (5847-5865; ring 5765-5773; harness-upward SKILL.md:147 contradicts :145). cut: delete block + skill bullet; collapse closing prose to one line. saves ~160 tok/--done (753) + duplicate message (median 370 tok; 291 sent). guarded: tests stub lead_address (8309, 8457, 8915). log 91. risk safe. (= B#2)
4. Stop "present it" block fires most turn ends of a lane waiting on its check; doesn't name --after-check (5244-5260). cut: two lines naming `harness mark T --done --after-check`; owner: skip when a check of HEAD queued/running. saves ~550 B/block (772) + forced turns. guarded: test_the_stop_hook_counts_a_catch_up_as_no_work_and_a_split_task_as_nothing_to_present. log 169,196. risk safe (text), owner (skip). evidence: 123/772 -> mark --done; next tools harness test 129, check --report 34, test --log 20, Monitor 17, blocked --help 35.
5. Reports/Research skill sections unused: upward 155-189 (2,773 B), downward 173-203 (1,916 B), root 89-97 (1,257 B). cut: two lines pointing to --help + spec T20/T21 (spec 481, 510). saves ~690/480/310 tok per load, ~20k tok/day. risk owner's call.
6. Checks/Reviewing sections restate CLI output: upward 121-140 (3,763 B), downward 130-138 (3,606 B). cut: keep pre-act rules; drop glosses printed by check/refusals; fault counting/keep glob to spec I5. saves ~620/600 tok per load. log 81,118,119,131,205/206. risk owner's call.
7. Every spawned lane gets all 12 charter features (11.3 K) (scope_block 11918-11965, 11701). cut: members/reviewers get full text of their briefs' features, one line per other. saves ~2.4k tok per member/reviewer spawn, ~90k tok/day. guarded: test_the_scope_block_is_the_charter_in_full_then_the_docs, test_every_first_prompt_carries_it. owner 10-06 ruling. risk owner's call. scope 18.1K = purpose 1.3K + features 11.3K + docs index 5.3K.
8. "They are marked read: act on them now…" after every delivery (harness-mail:227). delete. saves ~87k tok total, ~5k/day. guarded: DoorbellHooks.test_only_mail_that_asks_for_something_holds_the_turn_open (counts ==1). log 134. risk owner's call.
9. Free-text rings 81% of mail bytes; ring has no length cap (26181-26203). cut: refuse >~600 chars -> note --add (like CHAT_CAP). saves ~295k tok total (halve), ~16k/day. risk owner's call. median 550 B, p90 1.6K, max 8.3K.
10. Wake text repeats the prompt hook (25588-25592). cut: "harness ringer: mail for {node} (from …)". saves ~95k tok total. log 134. risk safe.
11. Documenter prompt embeds two writing skills (DOCUMENTER_WRITING 24218, ~25205-25209). cut: name skills, load via Skill tool. saves ~5k tok/run (58 runs). risk owner's call.
12. Log/obs numbers in 43 session-facing literals (e.g. 4500, 5772, 489, 740, 1056, 3315, 7049); 1,219 occurrences. strip from printed strings. risk safe. (= D#17)
13. ask_to rings restate the whole question every time (19926). drop after first ring. ~6k tok total. risk safe.

Not read / not sure: root/intermediary/documenter/reporter skills sized not read; rank 0 only 2 transcripts. 56% of members never load harness-upward though whoami lists it. biblion2 CLAUDE.md 39K + MEMORY 16K largest startup cost (project's). 30K skill listing: can claude --bg limit it? harness waiting prints a SendMessage (16545-16551) — less clearly superseded. Pre-10-22 figures include removed text. Scripts: e_survey, e_peek, e_startup, e_firstctx, e_prompts, e_turns, e_upscount, e_promptkinds, e_mail, e_where, e_cliout, e_samples, e_stopeffect, e_sendmsg, e_overlap, e_sections, e_provenance, e_specgrep, e_logtext (.py) in job tmp.
