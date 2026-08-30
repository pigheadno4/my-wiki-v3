# Metronome Campaign 29 quality audit

## Outcome

- Final approval: 5/5 pages.
- First-pass approval: 3/5 pages.
- Full semantic retries: 1 (`role-based-access-rbac-refresh`).
- Evidence-only targeted retries: 1 (`in-app-reporting-refresh`).
- Full independent reviews: 6; targeted reviews: 1.
- Rejected jobs: 0; coordinator semantic repairs: 0.
- Fixed query audit: 9/9 PASS; expansion to all five pages was not required.

Final content quality passed. The campaign met its limit of no more than one
full semantic retry, but missed the throughput gate of at least four first-pass
approvals.

## Fixed query audit

The auditor processed the three manifest-selected source units serially and
checked one factual query, one material boundary or contradiction query, and
one exact raw deep-dive route per page.

| Job | Factual answer | Boundary / contradiction | Raw deep dive |
| --- | --- | --- | --- |
| `list-invoices-refresh` attempt 1 | PASS | PASS | PASS |
| `edit-a-commit-refresh` attempt 1 | PASS | PASS | PASS |
| `avalara-refresh` attempt 1 | PASS | PASS | PASS |

The sample preserved immediate-parent schema placement, List-versus-Get and
top-level-versus-nested invoice scope, exact financial-unit unknowns,
endpoint-local versus API-wide idempotency authority, and the Metronome,
Stripe, and Avalara responsibility boundary. All three canonical sources
resolve to exact path-qualified 2026-08-28 raw snapshots.

## Mechanical close checks

- All five manifest raw SHA-256 values matched the immutable files.
- All five canonical source targets were byte-identical to their approved final candidates.
- Each source remained represented exactly once in the company catalog and provider index.
- Thirteen touched source and concept pages passed targeted `validate_wiki.py` checks.
- The Metronome capsule validator passed with 310 raw snapshots, 152 source summaries, and 145 raw snapshots without source summaries.
- `git diff --check` passed for campaign-owned wiki and tracking changes.

Two initial reviewer result files included provenance fields that the
controller already derives from its registered assignments. Removing those
two temporary fields was a fixed-schema normalization only; verdicts,
reasoning, shared decisions, candidates, and canonical content were unchanged.

## Verdict

Campaign 29 is approved for its five canonical refreshes and nine shared
updates. The two campaign-local API reminders worked on both API controls,
which passed attempt 1. The overall first-pass gate still failed because one
reporting page had incomplete quote coverage and the RBAC guide omitted its
source-defined intended actors. Do not increase campaign size from this result.
