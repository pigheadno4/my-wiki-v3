# Metronome Campaign 23 Quality Audit

## Outcome

- Fixed audit sample: `void-a-credit-grant`, `get-a-contract-v2`, and `packages-overview`.
- Result: 3/3 pages and 9/9 queries passed.
- Expansion: not required; no sampled query was partial or failed, and no primary reciprocal link was missing.

## Fixed query audit

| Page | Factual retrieval | Boundary or contradiction | Exact raw deep dive |
| --- | --- | --- | --- |
| `void-a-credit-grant` | Pass — the source retrieves the optional purchase-invoice void and uniqueness-key release effects. | Pass — it preserves omitted/false, eligibility, downstream, payment/refund, atomicity, visibility, concurrency, and rollback unknowns, plus the Plans-to-Contracts boundary. | Pass — `Raw Sources` links to the exact path-qualified 2026-07-13 raw snapshot. |
| `get-a-contract-v2` | Pass — the source retrieves `as_of_date`, optional balance and ledger expansion, and incomplete embedded commit/credit collections. | Pass — it separates historical contract configuration from undocumented historical-balance semantics and preserves the POST idempotency freshness boundary. | Pass — `Raw Sources` links to the exact path-qualified 2026-07-13 raw snapshot for the complete schema and examples. |
| `packages-overview` | Pass — the source retrieves customer-agnostic package terms, restricted package-based contract provisioning, immutable versions, and effective-dated aliases. | Pass — it does not infer existing-contract rewrites, alias overlap resolution, boundary-time selection, rollback, or later rate-card propagation. | Pass — `Raw Sources` links to the exact path-qualified 2026-07-13 raw snapshot for package, provisioning, alias, and custom-field detail. |

## Mechanical integrity

- All five current raw SHA-256 values match the approved manifest.
- All five canonical source files are byte-identical to their reviewer-approved candidates.
- Each promoted source appears exactly once in `wiki/companies/metronome.md` and `wiki/metronome-index.md`.
- All reviewer-approved primary concept routes have a reciprocal source link; the optional package custom-fields route was also applied.
- Capsule validation reports 225 raw pages, 137 source summaries, and 94 raw pages without source summaries.
- Targeted wiki validation passed for five sources, all Metronome concepts, the company page, and the log: 26 files, no issues.
- `wiki/metronome-index.md` was checked directly for counts and exactly-once entries because provider indexes intentionally do not use YAML frontmatter.
- The full unit suite passed: 737 tests in 119.193 seconds.
- `git diff --check` passed.

## Verdict

Campaign 23 passes the bounded Minimum Sufficient Source quality gate. The concise sources answer query-critical facts and material boundaries while retaining exact routes to immutable raw detail. No sixth page or cross-provider conclusion is part of this audit.
