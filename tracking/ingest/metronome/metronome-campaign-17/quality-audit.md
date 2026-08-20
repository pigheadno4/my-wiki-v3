# Metronome Campaign 17 Post-Repair and Expanded Query-Quality Audit

Audit date: 2026-08-20
Mode: independent repository-read-only audit
Final scope: all five Campaign 17 canonical sources

## Final decision

- `closure_approved: true`
- `expansion_required: false`
- Remaining material defects: none found.

The sole repair from the initial audit is valid, and all fifteen future-query tests now pass. No repository file was edited during this audit.

## Repair verification

The repaired `wiki/concepts/payment-reconciliation-reporting.md` now contains exactly one reciprocal link to `[[source-metronome-guides-reporting-insights-financial-reporting-revenue-recognition-examples]]` under `## Sources`.

Its description — “illustrative billing-data revenue scenarios, sample-key conflicts, and accounting-authority boundary” — is supported by the canonical source and raw CloudNet examples. It adds no amounts, schemas, identifiers, accounting treatments, or platform guarantees beyond those sources. The canonical source still links the concept, so the source↔concept route is now reciprocal in both directions.

## Audit method

For all five pages I checked the canonical source, complete assigned raw snapshot, linked fact-bearing concept sections, company page, and provider index. For the two expanded pages I independently re-read every raw line. I verified canonical facts and material boundaries against raw and relevant existing context, raw SHA-256/path/backlink, fact-bearing reciprocal source↔concept links, and exactly-once company/index listings. Each page was tested against exactly three future-query families: factual retrieval, boundary/contradiction handling, and exact raw deep-dive/navigation.

## 1. make-a-pricing-change

Integrity evidence:

- Canonical source: `wiki/sources/metronome/source-metronome-guides-pricing-packaging-make-pricing-changes-make-a-pricing-change.md`
- Raw: `raw/metronome/guides/pricing-packaging/make-pricing-changes/make-a-pricing-change-2026-07-13.md`
- SHA-256: `167df7747dca0372537d7885442ce30cb798396f367f58cf76f19362d7c284b0`
- Frontmatter path and path-qualified raw backlink are exact.
- Three linked fact-bearing concepts reciprocate; company and index each list the source exactly once.

| Future-query family | Grade | Concrete evidence |
| --- | --- | --- |
| Factual retrieval | **pass** | The source exposes the three rollout scopes and preserves the package flow's `entitled: false` rate, `entitled: true` override, `/v1/contracts/create`, reused `package_alias: "New Customer Pricing"`, and later `starting_at: "2025-01-01T00:00:00.000Z"`. |
| Boundary/contradiction handling | **pass** | It correctly rejects the claimed one-year scheduled increase because both `addRates` entries start `2024-01-01` and differ by dimension and price. It retains the unknown inheritance, precedence, proration, continuity, and edit semantics. |
| Exact raw deep-dive/navigation | **pass** | The exact backlink reaches the endpoint, fields, aliases, timestamps, and individual-customer alternatives; concept, company, and index routing is intact. |

Page total: **3 pass / 0 partial / 0 fail**.

## 2. revenue-recognition-examples

Integrity evidence:

- Canonical source: `wiki/sources/metronome/source-metronome-guides-reporting-insights-financial-reporting-revenue-recognition-examples.md`
- Raw: `raw/metronome/guides/reporting-insights/financial-reporting/revenue-recognition-examples-2026-07-13.md`
- SHA-256: `c2861f1e4d056b07a1105b2ca5443826a9c968f77831f6d08831fb3481c022a2`
- Frontmatter path and path-qualified raw backlink are exact.
- All four linked fact-bearing concepts now reciprocate exactly once, including the repaired `payment-reconciliation-reporting` link; company and index each list the source exactly once.

| Future-query family | Grade | Concrete evidence |
| --- | --- | --- |
| Factual retrieval | **pass** | The source faithfully covers on-demand/free-credit, prepaid purchase/drawdown, prepaid expiration/overage, and postpaid true-up scenarios, including `$459 = $384 + $75`, the `$10,000` balance, first `$900` drawdown, eleven later `$700` deductions plus `$1,400` expiration, and twelve `$800` periods plus `$400` true-up. |
| Boundary/contradiction handling | **pass** | It surfaces schema-header drift, customer-key mismatch, reused IDs, `$75` versus `$150`, `$700` drawdown versus `$800` conclusion, Scenario 2c's `$800` versus `$900` and prepaid/overage conflicts, and Scenario 3's swapped labels and repeated `30011`. It preserves the parent double-count exclusion and denies GAAP/IFRS or close-control authority. |
| Exact raw deep-dive/navigation | **pass** | Canonical-to-raw navigation is exact, and the repaired concept route now supports concept-to-source-to-raw traversal. All four reciprocal concept links and the exactly-once company/index routes pass. |

Page total: **3 pass / 0 partial / 0 fail**.

## 3. edit-or-override-a-contract

Integrity evidence:

- Canonical source: `wiki/sources/metronome/source-metronome-guides-pricing-packaging-make-pricing-changes-edit-or-override-a-contract.md`
- Raw: `raw/metronome/guides/pricing-packaging/make-pricing-changes/edit-or-override-a-contract-2026-07-13.md`
- SHA-256: `ab6257a40cb9857cb21b26e7611b817d26bf95f5c71d04c936d45ec64ac20384`
- Frontmatter path and path-qualified raw backlink are exact.
- Both linked fact-bearing concepts reciprocate; company and index each list the source exactly once.

| Future-query family | Grade | Concrete evidence |
| --- | --- | --- |
| Factual retrieval | **pass** | The source accurately distinguishes multiplier, overwrite, and tiered overrides; entitlement enablement; AND-within/OR-across specifiers; dimensional and presentation targeting; tiers; and precedence. |
| Boundary/contradiction handling | **pass** | It retains the all-pricing-group-values versus subset conflict, overwrite/tag prohibition, unresolved tier behavior, non-stacking limits, and invoice-entitlement versus application-authorization boundary. |
| Exact raw deep-dive/navigation | **pass** | The exact raw route exposes all payloads and proves that every worked request uses `POST /v1/contracts/create`; the page does not establish an existing-contract edit operation or `editContract` compatibility. |

Page total: **3 pass / 0 partial / 0 fail**.

## 4. data-export-cookbook

Integrity evidence:

- Canonical source: `wiki/sources/metronome/source-metronome-guides-reporting-insights-data-export-cookbook.md`
- Complete raw: `raw/metronome/guides/reporting-insights/data-export/cookbook-2026-07-13.md` (264 lines)
- SHA-256: `ff238507fbef397ef328228d6ea56fca4ce04d7ee203743aa47556ee175963d8`
- Frontmatter path and path-qualified raw backlink are exact.
- The approved fact-bearing shared update targets `metronome-reporting-and-analytics`; that concept reciprocally links the source exactly once. The other named concepts are taxonomy/context routes rather than Campaign 17 fact-bearing shared updates and were not given synthetic reciprocal claims.
- Company and index each list the source exactly once.

| Future-query family | Grade | Concrete evidence |
| --- | --- | --- |
| Factual retrieval | **pass** | The source accurately catalogs customer/event counts; finalized and draft invoice totals; table-global snapshot filters; ID-plus-snapshot breakdown joins; the two `PRODUCTION` filters; negative-line exclusion; archived contracts; descending override order; future-ending rate-card entries; active webhook alerts; and alert-history grouping. |
| Boundary/contradiction handling | **pass** | It preserves all material production-use boundaries: non-breakdown queries are not environment-scoped; object-storage delivery is append-only and at-least-once and requires latest-row resolution per primary key; a global maximum snapshot is neither deduplication nor per-object completeness; `DRAFT_INCOMPLETE` can be counted while null totals are ignored by `SUM`; “Finalized Invoices” SQL lacks a status predicate despite `VOID`; “last week” lacks a date filter; the six-column detail query groups only two; the rate-card query omits start/null-end/version grain; and `total/100` is not a universal currency conversion. |
| Exact raw deep-dive/navigation | **pass** | The exact backlink reaches every SQL statement and table reference. The canonical source separates raw cookbook behavior from the overview, database-reference, and currency authorities, and the fact-bearing reporting concept reciprocates exactly once. |

Page total: **3 pass / 0 partial / 0 fail**.

## 5. edit-contract

Integrity evidence:

- Canonical source: `wiki/sources/metronome/source-metronome-guides-pricing-packaging-make-pricing-changes-edit-contract.md`
- Complete raw: `raw/metronome/guides/pricing-packaging/make-pricing-changes/edit-contract-2026-07-13.md` (329 lines)
- SHA-256: `c15529eca1213a59666840f54d1648a2292360cdaf6ea6ec4428461b378b5786`
- Frontmatter path and path-qualified raw backlink are exact.
- All three linked fact-bearing concepts — customers/contracts, credits/commits, and invoicing — reciprocally link the source exactly once.
- Company and index each list the source exactly once.

| Future-query family | Grade | Concrete evidence |
| --- | --- | --- |
| Factual retrieval | **pass** | The source accurately captures immediate draft recalculation, finalized-invoice immutability unless voided and regenerated, the `$100,000` to `$200,000` commit edit, access amount `20000000`, incremental invoice amount `10000000`, `2027-01-01` access end, `2025-07-01` invoice timestamp, two-product applicability, supported edit families, history/full-state/audit surfaces, and rollover/archive guardrails. |
| Boundary/contradiction handling | **pass** | It preserves the `updateEndDate` versus `updateContractEndDate` conflict and the unresolved `created_at` versus edit-record `timestamp` used for `as_of_date`. It does not invent numeric units, array merge semantics, permissions, errors, idempotency, concurrency, atomicity, proration, cutoff inclusivity, or downstream payment/tax effects. It also distinguishes unchanged finalized invoices from regeneration under current state. |
| Exact raw deep-dive/navigation | **pass** | The exact raw route exposes both `/v2/contracts/edit` payloads, history records, historical-state example, supported operations, and every lifecycle guardrail. All three fact-bearing concepts reciprocate and company/index routing is exactly once. |

Page total: **3 pass / 0 partial / 0 fail**.

## Final totals

| Measure | Total |
| --- | ---: |
| Campaign 17 canonical pages audited | 5 |
| Query-family tests | 15 |
| Pass | 15 |
| Partial | 0 |
| Fail | 0 |
| Raw SHA/path/backlink checks passed | 5 of 5 |
| Company exactly-once listings passed | 5 of 5 |
| Provider-index exactly-once listings passed | 5 of 5 |
| Fact-bearing reciprocal concept links passed | 13 of 13 |
| Repair checks passed | 1 of 1 |

Final result: `closure_approved=true`; `expansion_required=false`.
