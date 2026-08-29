# Metronome Campaign 27 quality audit

## Outcome

- Final approval: 5/5 pages.
- First-pass approval: 4/5 pages.
- Full semantic retries: 1 (`authentication-refresh`).
- Full independent reviews: 6; targeted reviews: 0.
- Rejected jobs: 0; coordinator semantic repairs: 0.
- Fixed query audit: 9/9 PASS; expansion to all five pages was not required.

## Fixed query audit

The auditor processed the three manifest-selected source units serially, read
each complete trusted raw and approved source package, and checked one factual
query, one material boundary or contradiction query, and one exact raw deep-
dive route per page.

| Job | Factual answer | Boundary / contradiction | Raw deep dive |
| --- | --- | --- | --- |
| `authentication-refresh` attempt 2 | PASS | PASS | PASS |
| `custom-invoice-integrations-refresh` attempt 1 | PASS | PASS | PASS |
| `get-a-product-refresh` attempt 1 | PASS | PASS | PASS |

The sample preserved the customer-token versus engineer-credential lifetime
boundary, authentication UI and permission-model conflicts, external invoice
delivery and reconciliation unknowns, and Get-only schema annotation scope.
All three sources route detailed answers to exact path-qualified 2026-08-28
raw snapshots.

## Mechanical close checks

- All five manifest raw SHA-256 values matched the immutable files.
- All five canonical source targets were byte-identical to their approved
  candidates.
- Each source appeared exactly once in both the company catalog and provider
  index.
- Twelve touched source, concept, and company pages passed targeted
  `validate_wiki.py` checks.
- The Metronome capsule validator passed with 310 raw snapshots, 152 source
  summaries, and 155 raw snapshots without source summaries.
- `git diff --check` passed for campaign-owned wiki and tracking changes.

`wiki/metronome-index.md` retains its established no-frontmatter format, so it
is checked by the provider capsule validator and exact-entry/count checks
rather than the generic page validator. Campaign 27 did not introduce or
repair that baseline convention.

## Verdict

Campaign 27 passed its quality and first-pass gates. The bounded worker brief
improved first-pass behavior across a short guide, API overview, mutation,
integration guide, and schema-heavy read page without weakening complete raw
reads or independent per-page review.
