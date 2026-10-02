# Braintree C25 execution and timing investigation

Status: COMPLETE. C25 ran from `2026-10-02T09:16:26Z` to `2026-10-02T10:03:22Z`: **46m56s operational wall clock**. A model/session interruption occurred during execution; three outstanding native roles had no retained active agent or output and were recovered from existing trusted orders. The full wall-clock span must not be presented as uninterrupted model throughput. No reliable exact interruption duration is available.

Ten jobs approved; first full-review pass **7/10**. Ten full reviews and four targeted reviews were accepted, with no second full semantic review. The fixed query audit passed **20/20**. Ten sources total **5,628 `wc -w` words**. One coordinator repair corrected the same malformed catalog marker in company and index; source meaning was unchanged. Typed-page validation passed 18 pages, with exact candidate equality, immutable hashes, reciprocal routes and counts checked. Braintree now has 222 sources: 205 website plus 17 GitHub.

## Earlier campaign evidence

| Campaign | Ten-page closure | First-review pass | Targeted corrections |
| --- | --- | --- | --- |
| C18 | 44m15s | 5/10 | 5 |
| C19 | 39m28s | 7/10 | 3 |
| C20 | 46m05s | 8/10 | 2 |
| C21 | 48m15s | 7/10 | 3 |
| C22 | 54m28s | 3/10 | 7 |
| C23 | 1h41m32s | 5/10 | 5 |
| C24 | 28h59m20s, interrupted and not comparable | 10/10 | 0 |

C23 took 47m04s longer than C22 despite fewer targeted corrections and fewer source words (5,669 versus 6,264). Retry count and source length alone do not explain that increase. Earlier journals lack event timestamps, so exact worker, reviewer, queue and coordinator stage attribution cannot be reconstructed responsibly from those records.

## C25 observed role intervals

Agent-reported UTC intervals include role setup, required reading, analysis and handoff. Concurrent intervals overlap and must not be summed into campaign wall time.

| Job/role | Start UTC | End UTC | Duration |
| --- | --- | --- | --- |
| Webhooks worker A1 | 09:17:06 | 09:20:21 | 3m15s |
| Reference worker A1 | 09:17:54 | 09:20:40 | 2m46s |
| Testing worker A1 | 09:17:52 | 09:20:27 | 2m35s |
| OAuth worker A1 | 09:21:52 | 09:24:36 | 2m44s |
| Webhooks full review | 09:21:00 | 09:24:22 | 3m22s |
| Testing full review | 09:21:49 | 09:23:44 | 1m55s |
| Reference full review | 09:24:23 | 09:27:35 | 3m12s |
| OAuth full review | 09:27:17 | 09:31:12 | 3m55s |
| Webhooks worker A2 | 09:26:25 | 09:27:46 | 1m21s |
| Webhooks targeted review | 09:28:36 | 09:29:21 | 45s |
| Reference worker A2 | 09:28:39 | 09:30:19 | 1m40s |
| Reference targeted review | 09:31:09 | 09:31:48 | 39s |
| OAuth worker A2 | 09:31:53 | 09:32:42 | 49s |
| Merchant API worker A1 | 09:30:11 | 09:32:32 | 2m21s |
| OAuth recovered targeted review | 09:36:05 | 09:38:13 | 2m08s |
| Merchant API recovered full review | 09:36:23 | 09:38:22 | 1m59s |
| Multi-currency recovered worker | 09:37:03 | 09:38:44 | 1m41s |
| OAuth formatting worker A3 | 09:39:59 | 09:41:49 | 1m50s |
| OAuth formatting targeted review | 09:42:27 | 09:42:59 | 32s |
| Multi-currency full review | 09:40:33 | 09:42:51 | 2m18s |
| Server-side worker | 09:39:51 | 09:42:10 | 2m19s |
| Server-side full review | 09:43:56 | 09:46:47 | 2m51s |
| Configuration worker | 09:43:16 | 09:45:09 | 1m53s |
| Configuration full review | 09:46:58 | 09:47:45 | 47s |
| Connect worker | 09:44:18 | 09:46:09 | 1m51s |
| Connect full review | 09:47:45 | 09:49:49 | 2m04s |
| Overview worker | 09:47:06 | 09:49:27 | 2m21s |
| Overview review including bounded clarification | 09:50:29 | 09:54:36 | 4m07s |

## Operational stage windows

| Window | UTC observations | Wall span | Interpretation |
| --- | --- | --- | --- |
| Initialization through last review handoff | 09:16:26–09:54:36 | 38m10s | Includes setup, parallel role work, retries, dispatch, interleaved promotion and interruption/recovery; not pure model execution |
| Last-source promotion and aggregate navigation | 09:55:01–09:56:08 | 1m07s | One company/count/index update; concept/source promotion already overlapped role work |
| Fixed query audit dispatch through final handoff | 09:56:08–10:01:47 | 5m39s | Five groups in three dynamic slots; all 20 questions retained |
| Final reports/logs, mechanical validation and runtime close | 10:01:47–10:03:22 | 1m35s | 18-page validation itself took under one second |

These are observed overlapping operational windows, not an additive per-job CPU accounting. The 25-second gap before final-source promotion is included in campaign wall time. Post-close retrospective writing is excluded from operational closure. Final audit reports took 12–51 seconds after analysis-end across the five groups; this is a smaller remaining opportunity than role setup and reading.

## Measured overhead and current findings

The five required instruction files total 6,725 `wc -w` words: CLAUDE.md 1,617; ingest.md 2,100; Braintree rule 579; adopted Metronome contract 2,156; C25 dispatch contract 273. Ten initial workers and ten reviewers therefore load approximately 134,500 instruction words before raw/candidate/context reading, assuming each follows the assigned full reads. Some C25 raws contain only 194–503 words. This is a demonstrated input-volume overhead, not a measured causal estimate of latency or billed tokens.

First-pass failures observed so far concern a reversed webhook setup condition, OAuth scope count/classification and downloadable-software modality, and a missing OAuth permission boundary/navigation route. Their bounded corrections use targeted review. The OAuth A2 correction introduced a literal backslash-n between two list entries, causing a purely mechanical third attempt. These findings support focusing on retained assertion precision and cheap formatting checks; they do not justify a new audit layer or automatic reviewer waiver.

The coordinator also issued two unsuccessful initial scheduler calls before checking the existing assignment syntax. Those calls changed no state. Review dispatch initially named a nonexistent worker-result.json; the runtime actually persists receipt.json. Reviewers recovered from the accepted receipt, but that avoidable handoff confusion should be removed from future role prompts.

An Overview reviewer initially treated the absence of a separate Grant API quote as a blocker to a verified navigation label. The coordinator fully read the disputed short raw and asked for a bounded reassessment under the existing retrieval contract. The reviewer confirmed no misleading answer or broken route and approved without another worker attempt. This is evidence of review-standard drift, not a worker fact error; 3–5 grounding quotes must not become an exhaustive quote-per-navigation-label requirement.

## Conclusions and smallest next changes

C25 is 54m36s faster than C23 and 7m32s faster than C22, while near C20/C21. Different selections and interruptions prevent attributing that difference to one method. The earlier records cannot establish why C23 took 1h41m32s, so do not claim a reconstructed stage-level root cause.

The C25 evidence supports two next changes for separate rule approval: (1) consolidate the 6,725-word repeated setup into one shorter canonical role entry, with coordinator-owned general schema/governance reading and explicit worker/reviewer essentials; remove stale Metronome-specific preflight and the wrong handoff filename from dispatch instructions; (2) allow narrow, deterministic formatting normalization before accepted handoff, preserving meaning and recorded diff, so a literal newline/list-marker issue does not consume a model retry. Keep existing semantic subject/condition/action checks and independent initial review, and state that verified navigation labels need no exhaustive extra quote. No new scheduler, registry, audit layer or monitoring schema is needed.

Catalog consolidation and final validation are already small; broadening their automation is lower priority. Query-audit reporting can be shortened further, but its observed 5m39s window does not explain the majority of this campaign. No code/rule change, commit, push or new campaign was performed by this investigation.

## Separately approved follow-up implementation

After C25 closure, the user approved the two simplifications. `rules/ingest-roles.md`
now consolidates delegated worker/reviewer instructions into 955 words; coordinator
retains full governance/provider reading and supplies concise scope notes. This
reduces the prior 6,725-word mandatory instruction bundle by about 86%, excluding
trusted order/provider notes. Reading routers and runtime preflight use this entry.

The existing handoff normalizes only malformed wikilink list markers and literal
newline separators between eligible list entries. It retains original submitted
receipt and diff on a repair, keeps the accepted candidate/receipt/suggestions
consistent, and consumes no extra attempt. Protected code/quoted/frontmatter text,
extracted quotes, metadata and raw remain untouched. Verified navigation labels do
not require exhaustive individual quotes. Historical C25 attempts remain unchanged;
this implementation is for future separately approved campaigns.
