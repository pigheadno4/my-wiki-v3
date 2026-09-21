# Braintree C09 execution notes

Status: COMPLETE. Exact manifest approved on 2026-09-20.
Operational closure15:12:53–15:25:33Z:12m40s. First worker handoffs5/5 and first
independent content reviews5/5 passed. No retries, full/targeted rereviews,
coordinator semantic repairs or post-audit repairs. Query audit10/10 PASS.
Runtime start15:12:53Z. All raw hashes, absent targets and canonical ownership
rechecked; C08 closed. Baseline56 sources:40 website plus16 GitHub.
Initial native Sol medium workers confirmed for Plan Update/Create/Find, each
with persisted trusted order. No startup capacity rejection. Three dynamic child
slots, different Sol high first reviewers, coordinator-only repository writes.
No collection/raw edits, GitHub ingestion, code/rule changes, commit/push or
following campaign authorized. Role observations may overlap.

| Role | Reported UTC start | End |
| --- | --- | --- |
| Plan Update worker | 15:13:31 | 15:15:07 |
| Plan Create worker | 15:13:57 | 15:15:55 |
| Plan Find worker | 15:14:46 | 15:15:35 |

Three initial receipts accepted without format repair. Update/Find reviews live;
idle Create worker reused for Add-on All with a new persisted order/identity.
Reported late starts do not include all dispatch/setup latency.

Add-on All worker15:16:44–15:17:49Z; Discount All15:18:27–15:19:24Z.
All five receipts accepted on attempt1, zero format corrections. Update review
reported15:16:31–15:17:57Z, approved then promoted. Find approved/promoted;
Create/Add-on/Discount reviews run next with independent identities.

Find final evaluation15:17:42–15:18:40Z; Create review15:19:01–15:20:15Z;
Add-on All final evaluation15:19:43–15:20:51Z. All approved first time. Four sources
promoted, Audit A dispatched immediately after Create joined Update. No corrections
or expanded reads requested. These reported evaluation windows may omit setup.

Discount review15:20:33–15:21:31Z approved. Final source promoted and Audit B
dispatched before aggregate edits. All five content reviews approved on attempt1.
By15:23:36Z aggregate and single mechanical close passed: exact five candidates,
hashes/canonical identities, unique owners/catalogs, approved reciprocal routes,
count61 and8 typed pages (5sources,1concept,company,log). git diff --check passed.
Audit A start15:21:18Z, analysis end15:22:36Z, handoff15:23:18Z:4/4 PASS, no extra
selected evidence or repair. Its pending-catalog note is resolved by aggregation.

Audit B start15:22:59Z, analysis end15:23:45Z, artifact handoff15:24:47Z:
6/6 PASS, no extra selected evidence or repair. Report inspected and campaign
closed15:25:33Z. Website sources45 +GitHub16 =61 cumulative source summaries.

## Stage observations

| Stage | Observed UTC window | Duration/window |
| --- | --- | --- |
| Initialization to final worker handoff | 15:12:53–15:19:24 | 6m31s |
| First-review observations, overlapping workers | 15:16:31–15:21:31 | 5m00s |
| Audit A analysis/report | 15:21:18–15:23:18 | 2m00s |
| Audit B analysis/report | 15:22:59–15:24:47 | 1m48s |
| Final promotion/aggregation/check | after15:21:31, done15:23:36 | at most2m05s |
| Last artifact handoff to closure | 15:24:47–15:25:33 | 46s |

Windows overlap, are not additive compute totals, and may exclude role setup or
message-delivery time. C09 is essentially unchanged from C08's12m41s despite694
logical raw lines versus175. This is encouraging observational evidence for the
retrieval-granularity approach on longer example-heavy pages, not a controlled
causal benchmark. No parameter inventory or new validation process was added.
Both longer Plan sources passed first review with required prerequisite and
destructive omission warnings preserved. Audit A reporting tail42s and B62s remain
visible, but do not justify new monitoring machinery or relaxed evidence checks.

All five canonical sources equal approved candidates. One existing concept got
five reciprocal routes. Raw unchanged. No collection, GitHub ingest, code/rule
changes, commit/push or automatic next campaign. Existing unrelated changes preserved.
