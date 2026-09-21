# Braintree C03 execution notes

Status: COMPLETE. Started 2026-09-19T12:28:57Z; completed 2026-09-19T12:51:36Z.
Operational wall time: 22m39s, excluding this post-close report finalization.
Five exact manifest jobs approved. All pinned hashes verified and source targets
absent before initialization. Existing source count baseline: 26.
Initial three Sol medium worker dispatches confirmed individually; three dynamic
child slots, independent Sol high review, coordinator-only canonical writes.
No commit/push, GitHub ingest, collection or next campaign authorized.

Role timings and closure results will be recorded here from observed events;
overlapping intervals are not summed as wall time.

| Role | Start UTC | End UTC | Duration |
| --- | --- | --- | --- |
| Settlement worker | 12:29:35 | 12:32:42 | 3m07s |
| Authorization overview worker | 12:30:01 | 12:33:31 | 3m30s |
| Generate worker | 12:30:23 | 12:32:44 | 2m21s |
| Settlement initial review | 12:33:43 | 12:35:35 | 1m52s |
| Authorization initial review | 12:36:34 | 12:38:38 | 2m04s |
| Client-token guide worker | 12:37:06 | 12:39:24 | 2m18s |
| Void initial review | 12:37:25 | 12:39:02 | 1m37s |
| Client-token guide initial review | 12:40:23 | 12:42:10 | 1m47s |
| Query audit A | 12:39:27 | 12:41:26 | 1m59s |

Three first candidates passed runtime validation. Settlement/Generate reviews
started, then Void worker filled the worker reserve while Authorization waited
for review capacity. No batch barrier or extra validation mechanism.

Generate reviewer reported 12:35:58–12:36:15Z; Void worker reported
12:35:25–12:36:04Z. These short reported windows followed earlier dispatches;
retain as reported observations, not reliable end-to-end role latency.
Settlement and Generate promoted by 12:37:39Z; Authorization and Void promoted
after 12:39:02Z. Four first reviews approved without correction. Final token
review dispatched while the Settlement/Generate query audit runs.

All five initial reviews approved, zero retries. Audit A: 4/4 PASS, no extra raw
reads or repairs; analysis ended 12:41:21Z and report handed off five seconds later.
Final source promoted after token review; audit B dispatched for six questions.
Company/index aggregate changed source count to 31 (15 website + 16 GitHub).

Company/index aggregation completed by 12:44:04Z. One mechanical close pass
verified candidate/receipt equality, five unchanged raw hashes, canonical URLs,
raw ownership, exact reciprocal concept updates, single catalog entries, count31,
and nine typed pages; git diff --check passed. Validation took 0.64s.
No additional semantic review was initiated by the coordinator.

## Final audit finding and bounded correction

The statement above describes the pre-audit-close position, not the final result.
Audit B ran 12:43:39–12:46:50Z (3m11s; analysis ended 12:45:53Z).
All six fixed page-scoped questions passed, but two additional completely read
raws exposed a material upstream qualification: the Node Void page broadly
names PayPal settlement-pending eligibility; related Control Panel/status pages
limit it to certain PayPal transactions and identify multiple partial settlements.
Consequently ten query passes were not treated as sufficient for zero-repair close.

Coordinator fully read the primary and both supplemental conflict authorities.
Original independent reviewer approved the minimal warning, supplemental factual
raw references and narrower concept route at 12:48:34–12:50:40Z (2m06s).
Exact approved snippets, hashes and rationale are retained in quality-audit.md.
No worker retry or repeated full primary-page analysis was required. Initial
receipt/candidate/review are preserved; canonical Void source intentionally differs
only by the separately approved post-audit patch. The other four remain exact
candidate matches. Supplemental raws are conflict evidence, not two new standalone
ingestion jobs; do not count raw-reference coverage as full standalone ingestion.

The affected source/concept alone were revalidated after correction, including
exact patch equality and two supplemental hashes. No whole-suite or campaign-wide
semantic replay. Runtime closes with coordinator_repairs=1 to expose this repair;
its built-in full/targeted counters cover initial job reviews, not the separate
post-audit narrow review documented here.

## Outcome and time interpretation

- First-pass initial reviews: 5/5; five complete primary-source reviews, zero
  worker retries; one additional narrow post-audit independent review/repair.
- Final fixed questions: 10/10 PASS. Two extra raw reads per reviewing role were
  needed for the discovered conflict; no unrelated source expansion.
- Five sources added, two existing concepts updated, no new concepts; 31 total
  cumulative source summaries (15 website +16 GitHub). All primary raw hashes
  unchanged. No collection, GitHub ingest, commit, push or next campaign.
- Start → all initial approvals: 13m13s (through 12:42:10Z).
- Initial approvals → company/index aggregation confirmed: 1m54s; audit B overlapped.
- Aggregation → audit B handoff: 2m46s.
- Audit B handoff → corrected closure: 4m46s (includes 2m06s narrow review).
- Audit A overlapped the initial review phase; its report handoff took 5s after
  analysis, versus audit B's 57s. Mechanical aggregate validation took 0.64s.
- C02 was 20m07s; C03 is 22m39s despite 5/5 initial approval. No speedup claimed:
  C03's cross-document finding and correction absorbed the saved retry time.
  Focus the next improvement on reducing dispatch/handoff gaps and keeping
  page-local eligibility claims visibly scoped; do not add blanket full reads
  of neighboring documents, another review tier or more validators.
