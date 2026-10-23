# Findings F: ask_* family, harness 18673-20109

Headline
1. ask_verify refuses good briefs: path regex has no space so every /mnt/a/OneDrive - Charles Sturt University/... path is cut to University/...; http://127.0.0.1:8791 read as a file; quote check compares against json.dumps (escapes non-ASCII). Intermediaries resubmit 14-section briefs repeatedly.
2. ask --show = 63% of ask output (1.05 MB over 189 calls; median 3.1K, p90 13.8K, max 30K): reprints intermediary's messages beside TLDRs, full history, the task's brief.
3. No shadowing: _now/_save are the only defs, but 76 inline strftime and 111 non-atomic write_text(json.dumps) copies; transcript tail-reader copied 6x; 7 close verbs each write own close.

1. BUG _REF_LINE 19339 (used 19431-19436): char class [\w./~-] has no space; URL host:port read as file. cut: backticked form with spaces first, skip matches after //. ~20 refused briefs seen. guarded: AskEvidence2.test_references_must_exist (relative only). risk safe. evidence: "checked: University/PhD/apps/biblion2-dev/loader/reduction.py:N is not there" x6, "//127.0.0.1:8791 is not there" x4.
2. BUG quote_ok 19421-19423, _session_corpus 19364: json.dumps escapes non-ASCII so quotes with em dashes/curly quotes never match. cut: ensure_ascii=False or join strings. 31 quote faults in 42 unique refusals (some share). guarded: test_quotes_must_be_read_and_yes_needs_a_place (ASCII); _session_corpus NOT RUN. risk safe. verified by hand.
3. ask --show reprints everything (ask_show 20022-20097). cut: fold TLDR'd entries; drop history lines; task-brief half behind a flag. saves ~40-60% of 1.05 MB. guarded: none (NOT RUN). risk owner's call (intermediary skill:238).
4. Transcript tail-reader copied 6x: _transcript_recs 18810; turn_end_at 117-131, stop_cause 414-428, session_model 3555-3566, context_size 3580-3593, turn_texts 5268-5281; _tail 6433 exists; _rec_text/_is_tool_result re-inlined in turn_texts 5285-5292. saves ~40 lines. risk safe. log 97,122/125.
5. _now/_save (18723-18732) used 92 times before definition; 76 inline strftime, 111 non-atomic JSON writes (os.replace only in _save); bypasses ask_next_id 18789, ask_drop 19733. cut: move up near die; _now everywhere; GUI-polled writes via _save. risk safe (_now), unsure (all writes).
6. Seven close verbs each own close (19597-19637, 19638-19692, 19712-19753, 19770-19843); 10 copies of ASK_OPEN guard; not-a-node tuple 4x (19685, 19828, 20201, 20310). cut: _ask_close + one guard. saves ~40-50 lines. guarded: AskEvidence tests, done.jsonl/withdrawn.jsonl tests (4506, 7101). log 101b,108,166. risk owner's call (spec:444). three representations of closed.
7. BUG ask_drop 19729-19742 writes ruling without question/ruled_at/asker_node -> "ruled None  None" in brief (15273) and ask_show (20087); broad except prints "no task to mark" after marking. risk safe.
8. BUG --reject (19747) and --drop (19712) skip ASK_OPEN check: overwrite returned/done stub unseen by asker. risk safe.
9. BUG ask_merge 19610-19637 discards source thread, runs, chain, brief (only history line; evidence moved). 6 live uses. risk unsure.
10. TLDRs after the fact cost ~300 intermediary calls (ask_tldr 19884-19903; nag 20055-20056): ask --entry 302 vs --msg 246. cut: --msg --tldr or GUI first sentence. risk owner's call.
11. imask notice keyed on len(thread) (ask_notices 19990-19995) -> repeats on every thread message. cut: key on asking entry index. guarded test 5815. risk safe.
12. Every owner event reaches node twice: ring (ask_accept 19684-19688, ask_done 19828-19840, ask_to 19927) + orientation notice (19969-20007). log 108. risk owner's call.
13. intermediary_live 20100-20109 dead. (= C6, D7)
14. Dead states/fields: ASK_CLOSED 18677 ("accepted"/"merged" never written); merged_into/returned_why None init (19224, 18680); stale comments 19943-19944 ("seven sections" are 14). saves ~6 lines. risk safe.
15. ask_next_id scan 18766-18805 + owner_done 19755-19769 superseded by log-164 seq file. cut: backfill ask-seq.json once (biblion2 has no owner key; done.jsonl 28). saves ~25 lines. log 164,189. risk owner's call.
16. ask_show re-renders brief (20066-20096 vs 15255-15275; rulings block identical). cut: render_brief(); ProjCtx exists. saves ~20 lines. risk safe.
17. pdir->repo lookup recoded at 592, 3643, 18741, 19385, 19696, 20379, 21551, 25216 (+7 in GUI); ask_projects loop copied 3640-3645; ask_to reads tree.json inline (ask_tree 19693). cut: pdir_repo(). saves ~15 lines. risk safe.
18. Logs written never read: runs.jsonl 19140-19142, withdrawn.jsonl 19796-19799. guarded: tests 5759, 4506, 7101, spec 444. risk owner's call.
19. Caps inconsistent: question <=200 (19190, 19500) vs section 300 (18688); ask_reply 2000 vs CHAT_CAP 4000; TLDR cap twice (19874-19876, 19893-19898). ask_amend NOT RUN (53 live). risk safe.
20. BUG ask_notices 19985-20007: one bad ask file stops all later notices for the node (try outside loop). risk safe.
21. GUI copies ASK_OPEN/ASK_OWNERS (gui 137-138) and asks walk (784-790). (= D12)

Not read: cmd_ask, ask_idle, intermediary prompt. ask --idle output small (134 B median); cost is processes. Log 164(a) ordered runs not found in ask_add_runs. Missing tests: ask_show (301 live), ask_amend (53), _session_corpus, ask_chain doorbell branch 18961-18980. ask_chain/parse_ask_brief long but justified. _save fixed .tmp name: concurrent save race possible.
