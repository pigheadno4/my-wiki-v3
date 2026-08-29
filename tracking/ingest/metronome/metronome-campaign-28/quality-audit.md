# Metronome Campaign 28 quality audit

## Outcome

- Final approval: 5/5 pages.
- First-pass approval: 3/5 pages.
- Full semantic retries: 2 (`list-products-refresh` and `create-a-credit-refresh`).
- Full independent reviews: 7; targeted reviews: 0.
- Rejected jobs: 0; coordinator semantic repairs: 0.
- Fixed query audit: 9/9 PASS; expansion to all five pages was not required.

Final content quality passed, but the campaign did not meet its throughput gates of at least four first-pass approvals and no more than one full semantic retry.

## Fixed query audit

The auditor processed the three manifest-selected source units serially, read each complete trusted raw and approved source package, and checked one factual query, one material boundary or contradiction query, and one exact raw deep-dive route per page.

| Job | Factual answer | Boundary / contradiction | Raw deep dive |
| --- | --- | --- | --- |
| `anrok-refresh` attempt 1 | PASS | PASS | PASS |
| `list-products-refresh` attempt 2 | PASS | PASS | PASS |
| `create-a-credit-refresh` attempt 2 | PASS | PASS | PASS |

The sample preserved Anrok, Stripe, and Metronome responsibility boundaries; List-versus-Get and top-level-versus-history schema scope; exact dollar-cost-versus-quantity-unit semantics; the credit-versus-commit warning contradiction; and API-wide idempotency versus resource-identity boundaries. All three sources resolve to exact path-qualified 2026-08-28 raw snapshots.

## Mechanical close checks

- All five manifest raw SHA-256 values matched the immutable files.
- All five canonical source targets were byte-identical to their approved candidates.
- Each source appeared exactly once in both the company catalog and provider index.
- Eleven touched source and concept pages passed targeted `validate_wiki.py` checks.
- The Metronome capsule validator passed with 310 raw snapshots, 152 source summaries, and 150 raw snapshots without source summaries.
- `git diff --check` passed for campaign-owned wiki and tracking changes.

## Verdict

Campaign 28 is approved for its five canonical source promotions and shared updates, but it fails the planned first-pass and retry-count throughput gates. It is evidence against increasing campaign size under the unchanged brief; it is not evidence that the Minimum Sufficient Source structure or independent review failed to protect quality.
