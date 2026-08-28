# Metronome Campaign 26 Quality Audit

## Outcome

- Fixed audit sample: `edit-a-contract-refresh`, `database-reference-refresh`, and `token-billing`.
- Query result: 3/3 pages and 9/9 checks passed.
- Expansion: not required; factual retrieval, material boundaries, exact raw navigation, and primary reciprocal links all passed.

## Fixed query audit

| Page | Factual retrieval | Boundary or contradiction | Exact raw deep dive |
| --- | --- | --- | --- |
| `edit-a-contract-refresh` | Pass — retrieves mixed contract mutation scope, required payload identities, invoice and recurring-grant effects, payment-gated subscription access, spend-versus-quantity balances, and threshold charge initiation. | Pass — preserves omitted-body and unknown-field behavior, mixed-edit atomicity and recovery, response-ID ambiguity, the uniqueness-key authority conflict, and the provider-transition conflict. | Pass — `Raw Sources` links newest-first to the exact path-qualified 2026-08-28 and retained 2026-07-13 snapshots. |
| `database-reference-refresh` | Pass — routes table families, row grains, snapshots, effective records, and the 2026-08-28 schema changes without copying the field catalog. | Pass — separates `contracts_commits` from the broader `contracts_balances` domain and preserves the commit-specific `cost_basis` wording as an unresolved credit-row schema-context ambiguity. | Pass — `Raw Sources` links newest-first to the exact path-qualified 2026-08-28 and retained 2026-07-13 references. |
| `token-billing` | Pass — retrieves private-preview access, managed AI rate-card creation, markup behavior, custom-unit and package flow, and token-event mapping. | Pass — distinguishes new-model addition from future provider-price refresh, rejects non-USD fiat inference, separates event transaction identity from API-wide POST idempotency, and preserves operational unknowns. | Pass — the coverage map and `Raw Sources` link to the exact path-qualified 2026-08-28 snapshot. |

## Mechanical integrity

- All five raw SHA-256 values match the approved manifest.
- All five canonical source files are byte-identical to their reviewer-approved candidates.
- Each promoted source appears exactly once in `wiki/companies/metronome.md` and `wiki/metronome-index.md`.
- All 20 reviewer-approved shared updates across 15 concept targets are present; primary fact routes and reciprocal source links pass their focused checks.
- Targeted wiki validation passed for 21 source, concept, and company files.
- Capsule validation exited successfully and reports 310 immutable raw snapshots, 152 source summaries, and 160 raw snapshots without source summaries.
- `git diff --check` passed. The full unit suite was intentionally skipped because Campaign 26 changed documentation and tracking evidence only, not code, rules, or validators.

## Verdict

Campaign 26 passes real-source promotion quality for all five pages. The Minimum Sufficient Source format remains suitable for refreshed mutation, schema, integration, concept-guide, and new Token Billing pages; exact schemas and walkthrough details remain navigable in immutable raw snapshots.
