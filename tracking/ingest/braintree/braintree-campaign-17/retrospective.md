# Braintree C17 execution notes

Status: COMPLETE. Exact ten-page manifest approved 2026-09-26.
Runtime started `2026-09-26T13:31:52Z`. Preflight verified all ten pinned
hashes and canonical URLs, absent source ownership and targets, C16 closure,
the 131-source baseline, and three available native child slots. Initial
workers received Audit Webhooks, Transaction-Level Fee Report and Reporting
Overview. Timing windows may overlap and must not be summed. C17 approval
does not authorize raw edits, collection, GitHub ingest, code/rule changes,
commit, push or C18 preparation.

Runtime completed `2026-09-27T07:50:58Z` with two coordinator-repaired
sources. The 18h19m06s wall-clock span includes a model-usage-limit
interruption between 2026-09-26 and 2026-09-27; it is not a valid measure of
steady-state ten-page ingest speed. The journal does not timestamp every
worker/reviewer stage, so no narrower stage-time estimate is claimed.

Ten sources passed independent review and were promoted. There were ten full
initial semantic reviews (Webhooks first received one on worker attempt 2),
five targeted retry reviews, one invalid Webhooks worker status handoff and
sixteen worker starts overall. Five initial full reviews requested bounded
quote/route corrections; no page required another full semantic review.
Five audit groups answered twenty fixed questions. A/B found one upstream
country-eligibility contradiction; a narrow independent review approved the
paired warning and provenance patch on Reporting Overview and Fee Report.
The other eight canonical sources equal final approved candidates. Company
and index aggregation happened once; website count rose 115→125, total
source count 131→141. See `quality-audit.md` and `query-audit-a.md` through
`query-audit-e.md` for the close evidence.

The main throughput lesson is to enforce the exact handoff status/key schema
before submitting it to the runtime, and to check cross-page eligibility
claims during the existing gap sweep. No new registry, scheduler or validation
layer was added. C17 stops here; commit/push and any next campaign require
separate approval.
