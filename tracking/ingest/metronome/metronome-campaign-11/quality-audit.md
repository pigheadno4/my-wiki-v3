# Metronome Campaign 11 Independent Query-Quality Audit

Date: 2026-08-01
Repository: `/Users/tengtao/Development/wiki-v2`
Repository writes: none

## Decision

overall_decision: **approve**

expansion_required: **false**

The three immutable audit jobs passed all nine realistic future-query tests. No material semantic partial or fail was found, so the audit does not expand to the other seven pages. The original close check found stale body-level counts on the Metronome company page; a bounded mechanical repair and recheck verified the exact repaired values of 90 ingested and 135 pending. Those values now agree with the canonical source corpus, company frontmatter and source catalog, provider index, and prior capsule-validator result. The three-page semantic and nine-query audit was not rerun.

| Result | Pages | Queries |
| --- | ---: | ---: |
| Pass | 3 | 9 |
| Partial | 0 | 0 |
| Fail | 0 | 0 |

Materiality rule: a query partial or fail is material when an answer-critical fact, boundary, contradiction, raw link, or required reciprocal fact citation is absent or incorrect. Cosmetic wording and navigation-only concept links are not material. Mechanical catalog and count defects are full-campaign close gates, but do not by themselves expand the three-page semantic sample.

## Identity and link checks

| Audit job | Raw SHA-256 | Approved candidate/promoted source SHA-256 | Candidate = source | Raw deep link | Required reciprocal concept citations |
| --- | --- | --- | --- | --- | --- |
| `plans-shared-notifications` | `6df588128566f8fc0ae1f979da31313ce2e73fec83e3fc7781f795f871d5605c` | `cbea412aed8a3c7cdfa972053a075a28a33ca94b8cb7b57e1ded33780c14b506` | Yes | Resolves to the manifest raw path | `metronome-alerts-and-notifications` cites the source; `metronome-customers-and-contracts` is navigation-only. |
| `in-app-reporting` | `2b0aacc8bcf12478480762506a6484347b6bf4015a63077af03c3b6e37c5d886` | `3ecf4d496790a0787c8b5c18a7a2fa499f2d32e27960fc23a7671c37bcf713d3` | Yes | Resolves to the manifest raw path | `metronome-reporting-and-analytics` cites the source. |
| `reconcile-data` | `4b1ea7a4112883d7d3ece76485a3e2f6b13fb34aef301cb7c4221ed4255c2ab2` | `b0503b407135b3a7be5fa1af85f7ac77c174fc57d7d18fd585bfe01f06b495a7` | Yes | Resolves to the manifest raw path | `metronome-reporting-and-analytics` and `payment-reconciliation-reporting` cite the source; `metronome-customers-and-contracts` and `metronome-invoicing` are navigation-only. |

Additional checks:

- All three raw SHA-256 values match the immutable manifest.
- Each promoted source is byte-for-byte identical to the final reviewer-approved attempt candidate.
- Each approved receipt names the manifest raw path and hash, embeds the candidate source page, and has an approved full review with no required changes.
- Canonical URLs and `raw_files` values match the manifest, and the path-qualified Raw Sources links resolve.
- All source-to-concept wikilinks resolve. Each concept that received a durable Campaign 11 fact cites the contributing source reciprocally.
- `python3 scripts/validate_wiki.py` passed for the three sampled sources, five linked concepts, and Metronome company page: 9 files, no issues. The provider index is intentionally a non-frontmatter router and was checked mechanically rather than passed to that page validator.
- `python3 scripts/validate_metronome_capsule.py` reports 225 raw pages, 90 source summaries, and 135 pending ingest.

## All-ten company and provider-index check

This is a mechanical reverse-catalog audit only; the seven nonsampled source pages did not receive an additional semantic read.

| Campaign 11 source | Canonical source exists | Metronome company entries | Provider-index entries |
| --- | --- | ---: | ---: |
| `source-metronome-plans-shared-endpoints-notifications` | Yes | 1 | 1 |
| `source-metronome-plans-shared-endpoints-invoices` | Yes | 1 | 1 |
| `source-metronome-guides-reporting-insights-financial-reporting-reconcile-data` | Yes | 1 | 1 |
| `source-metronome-api-reference-invoices-void-an-invoice` | Yes | 1 | 1 |
| `source-metronome-guides-reporting-insights-financial-reporting-revenue-recognition` | Yes | 1 | 1 |
| `source-metronome-api-reference-notifications-list-system-notification-event-types` | Yes | 1 | 1 |
| `source-metronome-api-reference-invoices-regenerate-an-invoice` | Yes | 1 | 1 |
| `source-metronome-integrations-invoice-integrations-custom-invoice-integrations` | Yes | 1 | 1 |
| `source-metronome-api-reference-invoices-add-a-one-time-charge` | Yes | 1 | 1 |
| `source-metronome-guides-reporting-insights-in-app-reporting` | Yes | 1 | 1 |

Aggregate mechanical counts:

- Canonical Metronome source files: 90.
- Metronome company `## Sources` entries: 90; frontmatter `source_count`: 90.
- Provider-index `## Sources` entries: 90; coverage-table ingested count: 90; pending count: 135.
- Bounded repair recheck: the company page's `## Knowledge status` section now says `Ingested source summaries: 90` and `Documentation pages pending ingest: 135`. The company frontmatter count, company source-link count, provider-index count, and canonical Metronome source-file count are all 90.

## 1. `plans-shared-notifications` - pass (3/3)

Traceability:

- Raw SHA-256: `6df588128566f8fc0ae1f979da31313ce2e73fec83e3fc7781f795f871d5605c`.
- Approved candidate/promoted source SHA-256: `cbea412aed8a3c7cdfa972053a075a28a33ca94b8cb7b57e1ded33780c14b506`.
- The fact-bearing `metronome-alerts-and-notifications` concept preserves the shared surface and entity-difference boundary and cites the source reciprocally. `metronome-customers-and-contracts` is onward context only.

| Future query | Audit dimension | Result | Evidence and assessment |
| --- | --- | --- | --- |
| Which Metronome alert routes are shared by Plans and Contracts, what does each do, and which `alert_type` values are listed for plans? | Retrieval | **Pass** | Canonical source lines 18-20 and 23-44 preserve all five route labels and purposes, the entity-dependent parameter warning, and all four plan alert types. |
| Can I treat these route labels as complete versioned API contracts or assume Plan and Contract requests and responses are interchangeable? | Factual completeness / boundaries | **Pass** | Source lines 21, 33, and 44-50 explicitly withhold methods, version prefixes, schemas, entity-specific fields, threshold semantics, and catalog completeness; line 48 distinguishes the navigation-level reset label from `POST /v1/customer-alerts/reset`. |
| Can a reader inspect the exact upstream snapshot and continue to the dedicated reset and notification-lifecycle documentation? | Raw-backlink deep dive | **Pass** | Source lines 55-60 route to both dedicated sources and the exact 36-line path-qualified raw snapshot. |

Specific semantic defects: none.

## 2. `in-app-reporting` - pass (3/3)

Traceability:

- Raw SHA-256: `2b0aacc8bcf12478480762506a6484347b6bf4015a63077af03c3b6e37c5d886`.
- Approved candidate/promoted source SHA-256: `3ecf4d496790a0787c8b5c18a7a2fa499f2d32e27960fc23a7671c37bcf713d3`.
- The fact-bearing `metronome-reporting-and-analytics` concept preserves report access, delivery/freshness separation, dashboard methodology, and limits and cites the source reciprocally.

| Future query | Audit dimension | Result | Evidence and assessment |
| --- | --- | --- | --- |
| How are Metronome standard and custom in-app reports enabled, triggered, delivered, and timed, and what standard reports are available? | Retrieval | **Pass** | Source lines 18-20 and 24-48 preserve Solutions Architect enablement, paid custom-report scope, the full seven-report catalog, date-filtered app triggering, cron as a custom option, email/CSV delivery, one-to-ten-hour generation, once-daily report data, and possible stale reruns. |
| How does the Committed & Run Rate ARR Dashboard calculate committed ARR, run-rate ARR, movements, GRR/NRR, and logo status, and what defaults and caveats matter? | Factual completeness | **Pass** | Source lines 56-88 preserve both annualization models, the trailing completed-month behavior, newer/churned-customer treatment, movement and retention formulas, logo classifications, material filter defaults, finalized-invoice and contract scope, day proration, and non-USD limitation. |
| Does the report freshness window prove dashboard latency, do custom-report CSVs inherit Data Export semantics, and can the exact methodology be recovered? | Boundary / raw-backlink deep dive | **Pass** | Source lines 48, 52-54, and 90-104 separate generated reports, beta app dashboards, Data Export, and merchant-built API dashboards; they reject inherited cadence, row-grain, append-only, at-least-once, measurable real-time, permissions, and accounting guarantees, then link the exact 177-line raw snapshot. |

Specific semantic defects: none.

## 3. `reconcile-data` - pass (3/3)

Traceability:

- Raw SHA-256: `4b1ea7a4112883d7d3ece76485a3e2f6b13fb34aef301cb7c4221ed4255c2ab2`.
- Approved candidate/promoted source SHA-256: `b0503b407135b3a7be5fa1af85f7ac77c174fc57d7d18fd585bfe01f06b495a7`.
- The fact-bearing `metronome-reporting-and-analytics` and `payment-reconciliation-reporting` concepts preserve the billing-data-versus-settlement boundary and cite the source reciprocally. The customer/contract and invoicing links are onward context only.

| Future query | Audit dimension | Result | Evidence and assessment |
| --- | --- | --- | --- |
| What reconciliation workflow does Metronome recommend across Salesforce, Metronome, Stripe, and a warehouse, and how are records matched? | Retrieval | **Pass** | Source lines 14-28 preserve Data Export as the bulk path, lower-latency API list access, the worked system roles, and custom-field foreign-key mapping such as an SFDC opportunity ID for contract terms. |
| Are the SQL snippets complete Salesforce/Stripe reconciliation controls, proof of payment or settlement, or guarantees of export completeness and accounting correctness? | Factual completeness / boundaries | **Pass** | Source lines 18, 22, and 30-40 state that the snippets retrieve only Metronome-side snapshots and one latest finalized invoice, omit the external joins, matching key, fields, tolerances, mismatch process, pagination, and sign-off, and retain destination-specific export limits. The generic concept also explicitly excludes proof of payment, settlement, or money movement. |
| Can a reader recover the exact contract, commit, override, and finalized-invoice queries and verify the API alternative's stated limits? | Raw-backlink deep dive | **Pass** | Source lines 32-38 summarize the three max-snapshot patterns, latest `FINALIZED` invoice selection, and lower-latency list-endpoint alternative without inventing latency or completeness guarantees; lines 47-51 route to pagination context and the exact 111-line raw snapshot containing the SQL. |

Specific semantic defects: none.

## Findings and disposition

1. **The sole close defect is repaired.** A bounded mechanical recheck confirmed the company body's exact values of 90 ingested and 135 pending, plus 90 canonical source files, 90 company source links, company `source_count: 90`, 90 provider-index source links, and provider-index coverage values of 90 ingested and 135 pending. No semantic sample was rerun.
2. No sampled source, raw-identity, promotion-identity, raw-deep-link, source-to-concept, or required reciprocal concept-link defect was found.
3. No duplicate or missing company/provider-index entry was found among the ten Campaign 11 sources.

## Overall conclusion

Campaign 11's fixed independent semantic sample passes: **3/3 pages and 9/9 queries pass, 0 partial, 0 fail**. `expansion_required: false` because there is no material query partial or fail and no semantic expansion to all ten is needed. The bounded mechanical recheck confirms that the sole company-count defect is repaired and all checked counts agree. The overall verdict is **approve**.

`expansion_required: false`
