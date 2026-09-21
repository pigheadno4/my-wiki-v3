# Braintree C11 execution notes

Status: COMPLETE. Exact ten-page execution approved2026-09-21.
Runtime start12:02:24Z. All ten hashes and absent raw/canonical owners/targets
verified; C10 complete. Baseline71=55 website+16 GitHub sources.
Three Sol medium workers dispatched for Search Fields, Search Results and
Customer Search. Existing Sol high reviewers are idle; no active prior work.
No code/rule changes, collection, GitHub ingest, commit/push or next campaign.

Worker observations: Fields start marker12:04:29Z was captured after reading,
so not a valid full-duration start; completion12:05:37Z. Customer12:03:59–12:06:29Z;
Results12:04:58–12:07:36Z; Verification Search12:08:10–12:09:26Z.
Four initial format handoffs accepted. Fields/Customer/Results reviews approved
first time and promoted; no correction. Fields reviewer12:06:54–12:07:29Z,
handoff12:07:54Z; Results12:08:27–12:08:59Z, handoff12:09:19Z.
Group A audit dispatched while Verification review and Accept worker continue.

Verification first review12:10:20–12:11:16Z requested only missing local links
for two named navigation-only authorities. Original worker correction12:12:45–
12:13:44Z; targeted review12:15:12–12:15:31Z approved unchanged factual content,
quotes/concept/raw hash. No full retry/rereview. Subsequent dispatch reminds
workers to make retained reference routes clickable; no rule/schema added.

Workers: Accept12:09:36–12:11:00Z; Finalize12:11:28–12:12:33Z;
Find12:14:00–12:15:02Z; Dispute Search12:15:59–12:17:05Z;
Upload12:17:41–12:18:50Z; Remove Evidence12:19:47–12:20:44Z.
All10 initial worker handoffs accepted without format retry. Finalize review
12:13:33–12:14:08Z, handoff12:14:30Z; Upload12:20:15–12:20:49Z approved.
Nine pages now approved/promoted, final Remove review running. Audit A4/4,
C4/4 and B4/4 reported; B had two incorrect concept-section labels in its
report, sent back for narrow report-only correction (no source/content retry).

## Final outcome

Completed2026-09-21T12:26:15Z. Operational elapsed23m51s (1431seconds),
143.1seconds per accepted page.10/10 approved/promoted,9/10 initial content
reviews,10/10 initial format acceptance. Ten full initial reviews and one
bounded targeted rereview; zero full-analysis retry, zero full rereview,
zero coordinator semantic repair. One report-only route-label correction.
Query audit20/20 PASS with no extra selected raw or source repair.14 typed
pages and complete mechanical close passed.81=65 website+16 GitHub summaries;
no new concept. All C11 child assignments returned final results; completed
records alone do not establish release of underlying thread resources.

## Stage observations (UTC; overlapping, not additive)

| Stage | Observed window | Interpretation |
| --- | --- | --- |
| Startup + initial worker pipeline |12:02:24–12:20:44|18m20s from runtime initialization to final worker analysis completion; includes queue/setup/handoffs, not only reading |
| Initial reviewer pipeline |12:06:54–12:22:37|15m43s span to final reported handoff; overlaps workers and audits |
| Bounded correction |12:12:45–12:13:44|59s worker-reported correction window; targeted review12:15:12–12:15:31 adds19s, with queue between |
| Query audit pipeline |12:10:31–12:24:55|14m24s span for five groups, overlapping remaining ingestion |
| Final close tail |12:24:55–12:26:15|1m20s after final reported audit handoff for acceptance/report assembly/runtime close; shared updates/mechanical checks mostly already overlapped audits |

Reviewer observations additionally retained in attempt reviews: Customer12:07:22–
12:08:10; Accept12:12:16–12:12:57; Find12:16:18–12:16:49;
Dispute Search12:18:39–12:19:19; Remove12:21:38–12:22:16,
reported handoff12:22:37. These are self-reported analysis intervals, not
complete task latency or token/cost measurements.

Audit start → analysis end → reported handoff:
A12:10:31 →12:10:58 →12:11:04;
B12:18:47 →12:19:41 →12:19:41 (route-label correction delivered with D);
C12:15:46 →12:17:00 →12:17:15;
D12:21:32 →12:21:49 →12:23:08;
E12:23:21 →12:24:16 →12:24:55.
Delivery to coordinator may follow reported timestamps; do not infer exact
transport delays or sum overlapping role windows. Post-close notes are excluded
from operational elapsed time.

## Practical conclusion

Compared with C10's26m31s, C11 is2m40s (about10.1%) shorter, but the corpus also
fell from920 to777 raw lines and changed page types. This does not isolate the
impact of shorter reports or prove a general speedup. Quality remains9/10 first
reviews and20/20 queries. No repeated full-content retry is driving this run.

Three shared child slots still make worker/reviewer/auditor stages compete;
after initial parallel drafting, most remaining worker jobs were sequential
while other slots reviewed or audited. Completion/report-delivery gaps also
remain (for example D's79seconds after reported analysis, partly overlapping
B's report correction). Do not assign the entire interval to a known runtime
bug without evidence. Keep prompt handoffs and concise reports; prevent the
observed local-link omission in the existing drafting self-check, rather than
adding another gate, validator or monitoring subsystem. Changes to scheduling,
audit sample size or review policy require separate approval.

No raw edits, collection, GitHub ingest, code/rule changes, commit/push or next
campaign. Unrelated concurrent work preserved.
