# Metronome Campaign 33 quality audit

## Outcome

- Final approval: 5/5 new source pages.
- First-pass approval: 2/5 pages.
- Full semantic retries: 4 attempts beyond the first pass (`create-historical-invoices-new-source` once, `get-subscription-seats-history-new-source` once, and `create-alert-specifiers-new-source` twice).
- Full independent reviews: 9; targeted reviews: 0.
- Rejected jobs: 0; coordinator semantic repairs: 0.
- Fixed query audit: 9/9 PASS; expansion to all five pages was not required.

Final content quality passed. The campaign missed all planned throughput gates:
at least four first-pass approvals, no more than one full semantic retry, and
completion within 45 minutes.

## Fixed query audit

The auditor processed the three immutable manifest-selected source units and
checked one factual query, one material boundary or contradiction query, and
one exact raw deep-dive route per page.

| Job | Factual answer | Boundary / contradiction | Raw deep dive |
| --- | --- | --- | --- |
| `create-historical-invoices-new-source` attempt 2 | PASS | PASS | PASS |
| `create-alert-specifiers-new-source` attempt 3 | PASS | PASS | PASS |
| `update-a-billable-metric-new-source` attempt 1 | PASS | PASS | PASS |

The sample preserved preview versus creation and migration-guide versus
OpenAPI authority, customer and promotion blast radius plus uniqueness,
currency, idempotency, and status-response contradictions, and name-only
metric mutation versus replacement and PUT retry boundaries. All three
path-qualified raw links and SHA-256 values matched.

## Mechanical close checks

- All five manifest raw SHA-256 values matched the immutable files.
- All five canonical source targets were byte-identical to their approved final candidates.
- Twenty-eight reviewer-approved shared updates appeared exactly once across twelve existing concepts.
- Each new source appeared exactly once in the company catalog and provider index.
- Touched source, concept, company, and log pages passed targeted `validate_wiki.py` checks.
- The Metronome capsule validator passed with 310 raw snapshots, 167 source summaries, and 125 raw snapshots without source summaries.
- `git diff --check` passed for campaign-owned wiki and tracking changes.

## Verdict

Campaign 33 is approved for five new sources and twenty-eight shared updates.
It reduced the never-ingested canonical planning set from 70 to 65 pages. The
five-page mixed-risk structure preserved useful coverage pressure but did not
improve first-pass quality or elapsed time. Do not add another scheduler,
registry, validator, or monitoring layer; the measured bottleneck remains
complete semantic authority and contradiction discovery during per-page work.
