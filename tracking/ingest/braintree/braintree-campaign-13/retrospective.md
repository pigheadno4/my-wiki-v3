# Braintree C13 execution notes

Status: COMPLETE. Exact ten-page manifest execution approved2026-09-21.
Runtime start13:19:27Z. All10 hashes and absent raw/canonical/source ownership
rechecked; C12 complete. Baseline91=75 website+16 GitHub sources. Three Sol
medium workers started on Create, Update and Search after trusted orders were
persisted. Existing Sol high review roles are idle and reusable.

Scope remains documentation-only: no raw edits, collection, GitHub ingest,
code/rule changes, commit/push or next campaign. Three dynamic child slots
include workers, reviewers and query auditors. Record actual timings here;
overlapping execution windows are not additive.

First three worker handoffs accepted without format retry. Update worker
13:20:16–13:23:28Z; Create13:20:20–13:24:04Z; Search13:21:13–13:25:01Z.
Update full review13:24:40–13:26:09Z (handoff13:26:35); Create13:25:04–13:26:29Z
(handoff13:26:44); Search13:27:41–13:28:22Z (handoff13:28:53), all approved.
Group A query audit13:27:49–13:28:45Z (handoff13:29:20),4/4 PASS.
Partial Settlement worker13:25:41–13:28:14Z read extra ordinary Settlement
authority for a material availability conflict; additional authority read,
not a retry. Adjust Authorization worker13:28:51–13:30:12Z. These windows
overlap; no claim that their sum is total elapsed.

Partial Settlement first review13:30:14–13:31:30Z (handoff13:32:12)
requested bounded quote grounding and reciprocal conflict warning. Runtime
accepts only primary-raw quotes and concept-prefixed suggestion targets; no
schema/code changes made. Supporting quote+locator retained in existing
warnings field; separate reciprocal-warning artifact approved by original
reviewer and saved beside attempt2. Worker correction13:33:49–13:35:38;
targeted review13:36:31–13:36:52 (handoff13:37:31) approved. Candidate unchanged.
Coordinator applied the exact reviewer-approved warning to the existing
ordinary-settlement source, without rewriting its other content. This is one
bounded reviewed source repair, not an unreviewed semantic intervention.

Adjust review13:30:53–13:31:31Z (handoff13:31:44) approved. Clone worker
13:30:39–13:31:57; review13:33:08–13:33:39 (handoff13:33:53), approved.
Hold worker13:32:47–13:33:57; review13:34:56–13:35:15 (handoff13:35:42), approved.
Group C audit13:35:03–13:35:10 (handoff13:35:43),4/4 PASS.
Release worker13:36:09–13:37:49; Cancel worker13:36:53–13:38:04.

Line Item worker13:38:51–13:40:08Z; full review13:41:14–13:41:37
(handoff13:41:57), approved. Release review13:38:43–13:39:13
(handoff13:39:29); Cancel13:40:24–13:40:53 (handoff13:41:06), approved.
Group B audit13:38:18–13:40:22 (handoff13:41:05),4/4 PASS.

All10 pages approved and aggregate catalogs updated by approximately13:43Z.
Mechanical close found one placeholder-regex false positive in Line Item:
the retained warning phrase `Do not fill in the missing words` matched FILL IN.
Canonical text alone changed to `Do not reconstruct the missing words`.
Approved candidate/receipt remain immutable; equality validation allows exactly
this recorded substitution and no other difference. No semantic re-review or
validator change. Count this and the reviewed reciprocal warning as two bounded
coordinator repairs, neither an unreviewed semantic expansion.

Close checks passed after that precise correction:10 approved sources,
primary raw hashes/canonical URLs/quotes, unique primary owners, explicit
supporting evidence, approved concept routes, required and reciprocal links,
duplicate-free new catalog entries,101=85 website+16 GitHub,15 typed files
(10 new sources,2 concepts,company/log and1 existing warning target).


## Final result and stage timing

Closed2026-09-21T13:44:17Z; total24m50s (1490s),149s per promoted page
as a wall-clock allocation, not model latency.10/10 approved;20/20 queries
PASS. First-pass content9/10;1 targeted correction,zero full retry reviews.

| Stage | Observed UTC window | Interpretation |
| --- | --- | --- |
| Setup/first verified worker start |13:19:27–13:20:16|49s |
| Worker production incl bounded correction |13:20:16–13:40:08|19m52s overlapping dispatch/review/queue window |
| Independent review |13:24:40–13:41:57|17m17s overlapping window;10full+1targeted |
| Query audit |13:27:49–13:43:19|15m30s overlapping window;5groups/20questions |
| Final promotion/aggregate/mechanical checks |approximately13:42–13:43:26|About1m26s; earlier promotion was incremental |
| Last audit handoff to runtime close |13:43:19–13:44:17|58s acceptance/report/closure |

Windows overlap; do not add them. C12 was26m55s; C13 is2m05s shorter
(about7.7%), despite1418 versus700 logical raw lines. This single run does
not prove a causal speedup. Actual agent-start and result-delivery gaps remain,
and the supporting-conflict issue added one bounded correction. Keep immediate
handoff/dispatch and concise reports; no new monitoring, schemas or validators.

The primary/supporting quote restriction was detected before the corrected
handoff reached runtime; no format failure or extra attempt was introduced.
An attempted message to an evicted reviewer hit the thread limit while three
roles were active; it was delivered with that reviewer's later followup after
capacity freed. No duplicate agent or job was created.

No raw changes, collection, GitHub ingest, commit/push or next campaign by C13.
All workers, reviewers and auditors returned. Existing unrelated changes and
concurrent Stripe task commits were preserved.
