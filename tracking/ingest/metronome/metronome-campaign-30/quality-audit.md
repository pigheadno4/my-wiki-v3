# Metronome Campaign 30 quality audit

## Outcome

- Final approval: 5/5 pages.
- First-pass approval: 3/5 pages.
- Full semantic retries: 2 (`create-a-commit-refresh` and `stripe-invoice-integration-refresh`).
- Evidence-only targeted retries: 0.
- Full independent reviews: 7; targeted reviews: 0.
- Rejected jobs: 0; coordinator semantic repairs: 0.
- Fixed query audit: 9/9 PASS; expansion to all five pages was not required.

Final content quality passed. The campaign missed both throughput gates: at
least four first-pass approvals and no more than one full semantic retry.

## Fixed query audit

The auditor processed the three manifest-selected source units serially and
checked one factual query, one material boundary or contradiction query, and
one exact raw deep-dive route per page.

| Job | Factual answer | Boundary / contradiction | Raw deep dive |
| --- | --- | --- | --- |
| `get-an-invoice-refresh` attempt 1 | PASS | PASS | PASS |
| `create-a-commit-refresh` attempt 2 | PASS | PASS | PASS |
| `customer-controls-refresh` attempt 1 | PASS | PASS | PASS |

The sample preserved immediate-parent invoice schema placement, conditional
commit schedule requirements, payment-at-expiry versus scheduled invoice
generation, explicit customer-control actors, and exact path-qualified raw
deep-dive links with matching SHA-256 values.

## Mechanical close checks

- All five manifest raw SHA-256 values matched the immutable files.
- All five canonical source targets were byte-identical to their approved final candidates.
- Twenty reviewer-approved shared updates appeared exactly once across nine existing concepts.
- Each source remained represented exactly once in the company catalog and provider index.
- Fourteen touched source and concept pages passed targeted `validate_wiki.py` checks.
- The Metronome capsule validator passed with 310 raw snapshots, 152 source summaries, and 140 raw snapshots without source summaries.
- `git diff --check` passed for campaign-owned wiki and tracking changes.

## Verdict

Campaign 30 is approved for its five canonical refreshes and twenty shared
updates. The actor reminder was consistent with Customer Controls passing on
attempt 1, but the added reminders did not improve the overall 3/5 first-pass
rate. Create Commit still lost conditional and timing boundaries, while the
Stripe integration both misattributed documentation authority and proposed
shared claims beyond its selected evidence. Do not scale from this result and
do not add another prompt, checklist, or validator layer.
