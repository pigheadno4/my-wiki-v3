# Metronome Campaign 36 retrospective

## Result

- Started: `2026-09-01T12:51:00Z`
- Completed: `2026-09-01T14:03:11Z`
- Elapsed: 4,331 seconds (72 minutes 11 seconds)
- Final approval: 5/5
- First-pass approval: 1/5
- Worker attempts: 9
- Full reviews: 9
- Targeted reviews: 0
- Review waivers: 0
- Coordinator semantic repairs: 0

All five sources passed final review and promotion checks. The fixed three-page candidate audit passed 9/9, and raw hashes, approved candidate content, exact raw backlinks, reciprocal routes, shared updates, catalog counts, wiki validation, and capsule validation passed.

## What worked

- The risk gate failed closed. The fixed custom-field sample exposed material visibility-scope and pagination-authority boundaries, was routed to `review_required`, and released no review waiver.
- All provisional pages consequently received independent full review; no candidate was promoted from an untested waiver path.
- One package-association page passed its first review. Four other pages were corrected once and then approved; no job exhausted the three-attempt limit.
- The immutable three-page audit found no remaining material candidate defect, and the coordinator performed no semantic repair during promotion.
- Canonical source, shared concept, company, index, and log writes remained coordinator-owned.

## What cost time

- The fixed sample was not actually low risk after its complete raw read. Its unresolved caller-visible scope and endpoint-versus-global pagination conflict immediately made it ineligible for sampled approval.
- The other provisional pages also contained material routing triggers. Package association and offset-notification listing required contract, migration, pagination, lifecycle, delivery, or idempotency boundaries that a title-and-metadata selection pass could not safely exclude.
- Four first attempts needed page-specific semantic corrections: current credit-route and ordering boundaries, same-customer ownership and cached-error recovery, custom-field visibility and pagination conflict, and offset-list cursor and limit conflict.
- Nine complete reviews remained the dominant cost. Because the gate released no waiver, Campaign 36 added routing machinery without reducing review work and finished well above the 35-minute observational target.

## Gate assessment

- PASS: 5/5 final approval, no rejection, no coordinator semantic repair, 9/9 candidate audit, exact evidence and reciprocal-link checks, and fail-closed handling.
- FAIL: the fixed sample did not remain `sample_eligible`; zero of three provisional pages received a waiver versus the required two; elapsed time was 72 minutes 11 seconds versus the 35-minute target.

The pilot therefore validates the safety of the fail-closed path, not the throughput value of risk-gated review.

## Recommendation

Keep the five promoted sources and their approved shared updates, but do not adopt this sample-waiver policy for production or another PSP from Campaign 36. Retain complete independent review under the current workflow unless a separately approved small pilot tests a materially simpler selection rule. Do not add a risk registry, classifier agent, scheduler layer, or migration based on this result.
