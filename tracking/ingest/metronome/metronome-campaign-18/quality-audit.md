# Metronome Campaign 18 Query-Quality Audit

Audit date: 2026-08-21
Mode: independent repository-read-only close audit
Fixed semantic sample: `list-pricing-units`, `release-external-payment-gate-threshold-commit`, `list-plans`

## Final decision

- `closure_approved: true`
- `expansion_required: false`
- Material defects: none found
- Repository files edited by this audit: none

All nine fixed future-query tests pass. The complete five-page mechanical close sample also passes: immutable raw hashes match the approved manifest, each canonical source is byte-equal to its approved candidate, exact raw frontmatter/backlinks are present, company and provider-index entries occur exactly once, and every approved fact-bearing concept target reciprocally cites its source.

## Audit method

For each of the three fixed audit jobs, I independently read the complete raw snapshot, canonical source, relevant fact-bearing concepts, `wiki/companies/metronome.md`, and `wiki/metronome-index.md`. I tested three query families per page: factual retrieval; safe treatment of boundaries, unknowns, and contradictions; and exact raw deep-dive/navigation.

Across all five Campaign 18 jobs I additionally verified:

- raw SHA-256 against the immutable manifest;
- canonical source byte equality with the reviewer-approved `candidate.md`;
- exact `canonical_url`, exact `raw_files` entry, and one path-qualified raw backlink;
- exactly one source wikilink in the company page and exactly one in the provider index;
- all seven approved fact-bearing reciprocal concept targets.

The Metronome capsule validator passes with `225 raw`, `112 sources`, and `119 raw pages without source summaries`. A direct targeted `validate_wiki.py` invocation found no issue in the audited sources, concepts, or company page; it reported only the provider index's established no-frontmatter format. That format predates Campaign 18, does not affect routing or query quality, and is not treated as a material Campaign 18 defect.

## 1. list-pricing-units

Integrity evidence:

- Canonical source: `wiki/sources/metronome/source-metronome-api-reference-settings-list-pricing-units.md`
- Raw: `raw/metronome/api-reference/settings/list-pricing-units-2026-07-13.md`
- SHA-256: `455c833fa65b8c698b1b431c13d55bd6a5ecb297dfb4c41b4d3cb7c81321eab1`
- Canonical source equals approved candidate byte-for-byte.
- Exact frontmatter raw path, canonical URL, and path-qualified raw backlink pass.
- The fact-bearing currency/pricing-unit concept reciprocates; company and index each list the source exactly once.

| Future-query family | Grade | Concrete evidence |
| --- | --- | --- |
| Factual retrieval | **pass** | The source directly returns `GET /v1/credit-types/list`, bearer authentication, optional `limit` and `next_page`, inclusive limit bounds 1–100, required top-level `data` and nullable `next_page`, optional-by-schema item properties, and the fixed `USD (cents)` ID `2714e483-4ff1-48e4-9e25-ac732e8f24f2`. |
| Boundary/unknown/contradiction-safe retrieval | **pass** | It does not turn the two-item example into an exhaustive inventory or guaranteed ordering, does not claim that item properties are required, and explicitly leaves non-USD denomination, custom-unit precision/rounding, cursor lifetime/defaults, identifier stability, errors, mutation, and propagation undocumented. It also keeps the unexplained `credit-types` versus pricing-unit terminology unresolved. |
| Exact raw deep-dive/navigation | **pass** | Source-to-raw navigation reaches the exact OpenAPI snapshot and example. The currency concept routes back to the source, while the linked products/rate-cards concept remains contextual navigation rather than an unsupported additional fact claim. Company and provider-index routes are intact. |

Page total: **3 pass / 0 partial / 0 fail**.

## 2. release-external-payment-gate-threshold-commit

Integrity evidence:

- Canonical source: `wiki/sources/metronome/source-metronome-api-reference-credits-and-commits-release-external-payment-gate-threshold-commit.md`
- Raw: `raw/metronome/api-reference/credits-and-commits/release-external-payment-gate-threshold-commit-2026-07-13.md`
- SHA-256: `d71b3d777b07ad270a327b71418430604aaf53d74ca684e16db2442140883938`
- Canonical source equals approved candidate byte-for-byte.
- Exact frontmatter raw path, canonical URL, and path-qualified raw backlink pass.
- The spend-threshold, credits/commits, and webhook fact-bearing concepts reciprocate; company and index each list the source exactly once. API idempotency is correctly retained as broader contextual navigation, not endpoint-specific proof.

| Future-query family | Grade | Concrete evidence |
| --- | --- | --- |
| Factual retrieval | **pass** | The source exposes `POST /v1/contracts/commits/threshold-billing/release`, the `payment_gate.external_initiate` correlation flow, required payload properties `workflow_id` and `outcome`, UUID formatting, accepted `paid`, `PAID`, `failed`, and `FAILED` values, and the sole documented bare `200` response. |
| Boundary/unknown/contradiction-safe retrieval | **pass** | It preserves the OpenAPI nuance that the payload schema requires both properties while the `requestBody` object itself is not marked required. It does not invent omitted-body behavior, error contracts, workflow expiry or cardinality, replay safety, conflicting-outcome handling, ordering, atomicity, recovery, or downstream balance/ledger/invoice/webhook visibility. It also keeps webhook delivery retry, payment retry, and retry of this POST distinct. |
| Exact raw deep-dive/navigation | **pass** | The exact raw backlink reaches the operation prose and complete payload enum. Reciprocal concept routes support query traversal from payment gating, commit lifecycle, or webhook correlation back through this source to the immutable raw snapshot. |

Page total: **3 pass / 0 partial / 0 fail**.

## 3. list-plans

Integrity evidence:

- Canonical source: `wiki/sources/metronome/source-metronome-api-reference-plans-list-plans.md`
- Raw: `raw/metronome/api-reference/plans/list-plans-2026-07-13.md`
- SHA-256: `4ce4c0e36644804bdaa93e069feb7125010a19241685f68fcad3f3a98e580722`
- Canonical source equals approved candidate byte-for-byte.
- Exact frontmatter raw path, canonical URL, and path-qualified raw backlink pass.
- The customers/contracts fact-bearing concept reciprocates; company and index each list the source exactly once.

| Future-query family | Grade | Concrete evidence |
| --- | --- | --- |
| Factual retrieval | **pass** | The source directly provides bearer-authenticated `GET /v1/plans`, optional `limit` and `next_page`, inclusive limit bounds 1–100, required response fields `data` and nullable `next_page`, required Plan fields `id`, `name`, and `description`, and optional string-valued `custom_fields`. |
| Boundary/unknown/contradiction-safe retrieval | **pass** | It accurately labels Plans deprecated and preserves the instruction that new clients use Contracts, but does not convert that into endpoint removal or unavailability. It does not invent a replacement Contracts route, Plan-to-Contract identity/schema mapping, migration procedure, removal date, ordering, cursor lifetime, errors, scopes, or compatibility guarantee. |
| Exact raw deep-dive/navigation | **pass** | The path-qualified raw link reaches the exact `/openapi.plans.json` snapshot, server/path composition, response schema, and examples. The customers/contracts concept links back to the source, and company/index discovery is exactly once. |

Page total: **3 pass / 0 partial / 0 fail**.

## Complete five-page mechanical verification

| Job | Raw hash | Canonical = approved candidate | Exact raw path/backlink | Company exactly once | Index exactly once | Fact-bearing reciprocity |
| --- | --- | --- | --- | --- | --- | --- |
| `list-pricing-units` | pass | pass | pass | pass | pass | pass |
| `archive-a-rate-card` | pass | pass | pass | pass | pass | pass |
| `list-plans` | pass | pass | pass | pass | pass | pass |
| `release-external-payment-gate-threshold-commit` | pass | pass | pass | pass | pass | pass |
| `get-an-invoice-pdf` | pass | pass | pass | pass | pass | pass |

Approved fact-bearing reciprocal concept targets checked: `metronome-currencies-and-custom-pricing-units`, `metronome-products-and-rate-cards`, `metronome-customers-and-contracts`, `metronome-spend-threshold-billing`, `metronome-credits-and-commits`, `metronome-webhooks`, and `metronome-invoicing` — **7 of 7 pass**.

## Final totals

| Measure | Total |
| --- | ---: |
| Fixed semantic pages audited | 3 |
| Query-family tests | 9 |
| Pass | 9 |
| Partial | 0 |
| Fail | 0 |
| Raw SHA checks passed | 5 of 5 |
| Canonical-to-approved-candidate equality checks passed | 5 of 5 |
| Exact raw path/backlink checks passed | 5 of 5 |
| Company exactly-once listings passed | 5 of 5 |
| Provider-index exactly-once listings passed | 5 of 5 |
| Fact-bearing reciprocal concept targets passed | 7 of 7 |

Final result: `closure_approved=true`; `expansion_required=false`.
