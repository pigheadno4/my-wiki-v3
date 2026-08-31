# Metronome Campaign 32 quality audit

## Outcome

- Final approval: 5/5 new source pages.
- First-pass approval: 2/5 pages.
- Full semantic retries: 2 attempts beyond the first pass (`archive-billable-metric-new-source` and `guarantee-zero-overages-new-source` once each).
- Full independent reviews: 7; targeted reviews: 1.
- Rejected jobs: 0; coordinator semantic repairs: 0.
- Fixed query audit: 9/9 PASS; expansion to all five pages was not required.

Final content quality passed. The campaign missed both planned throughput gates:
at least four first-pass approvals and no more than one full semantic retry.

## Fixed query audit

The auditor processed the three immutable manifest-selected source units and
checked one factual query, one material boundary or contradiction query, and
one exact raw deep-dive route per page.

| Job | Factual answer | Boundary / contradiction | Raw deep dive |
| --- | --- | --- | --- |
| `list-invoice-breakdowns-new-source` attempt 1 | PASS | PASS | PASS |
| `guarantee-zero-overages-new-source` attempt 2 | PASS | PASS | PASS |
| `create-or-update-customer-ingest-aliases-new-source` attempt 2 | PASS | PASS | PASS |

The sample preserved mutable-breakdown versus finalized-invoice tension,
zero-rate billing versus merchant-owned access control and denomination
conflict, and full alias replacement versus undocumented propagation. All
three path-qualified raw links and SHA-256 values matched.

## Mechanical close checks

- All five manifest raw SHA-256 values matched the immutable files.
- All five canonical source targets were byte-identical to their approved final candidates.
- Thirty-eight reviewer-approved shared updates appeared exactly once across thirteen existing concepts.
- Each new source appeared exactly once in the company catalog and provider index.
- Touched source, concept, company, and log pages passed targeted `validate_wiki.py` checks.
- The Metronome capsule validator passed with 310 raw snapshots, 162 source summaries, and 130 raw snapshots without source summaries.
- `git diff --check` passed for campaign-owned wiki and tracking changes.

## Verdict

Campaign 32 is approved for five new sources and thirty-eight shared updates.
It reduced the never-ingested canonical planning set from 75 to 70 pages. The
less conflict-dense selection did not improve throughput: three pages still
needed correction, although the alias page safely used a targeted retry. Do
not add another process layer in response; the measured bottleneck remains
semantic first-pass completeness on mutation and boundary-heavy pages.
