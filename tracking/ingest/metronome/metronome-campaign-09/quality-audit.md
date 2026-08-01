# Metronome Campaign 09 Independent Query-Quality Audit

Date: 2026-08-01
Repository: `/Users/tengtao/Development/wiki-v2`
Repository writes: none

## Decision

overall_decision: **approve**

expansion_required: **false**

The three immutable Campaign 09 audit jobs passed all nine future-query tests. No material partial or fail was found, so the audit stops at the predetermined sample and does not expand to the other campaign pages.

| Result | Pages | Queries |
| --- | ---: | ---: |
| Pass | 3 | 9 |
| Partial | 0 | 0 |
| Fail | 0 | 0 |

Materiality rule: a partial or fail is material when an answer-critical fact, boundary, contradiction, raw link, or required reciprocal fact citation is absent or incorrect. Cosmetic wording is not material.

Mechanical evidence:

- All three raw SHA-256 values match the manifest.
- All three promoted sources are byte-for-byte identical to their final reviewer-approved candidates.
- All canonical URLs, `raw_files` entries, and path-qualified Raw Sources links match the manifest and resolve.
- `python3 scripts/validate_wiki.py` passed for the three sources and nine related concepts: 12 files, no issues.
- Each source occurs exactly once in the Metronome provider index and company catalog.

## 1. `guides-home` — pass (3/3)

Traceability:

- Raw SHA-256: `c0e56629644cd181e7deb54cb6af94c7c806298739c131d34468f18d45ac49dc`.
- Approved candidate/promoted source SHA-256: `ddc4e5f46f6e49d76c8aff4c7014b38cf15deb24a5d9d49bdea3a334aa5caba9`.
- Raw lines 11–22 contain only the introductory routing statement and four cards. Source lines 14–24 preserve the four routes and explicitly bound the page as navigation rather than implementation evidence.
- Source line 34 links directly to the exact raw snapshot. Its company, concept, and two already-ingested guide routes are useful navigation. The concept links carry no new fact beyond this navigation-only page, so reciprocal fact citations are not required.

| Future query | Audit dimension | Result | Evidence and assessment |
| --- | --- | --- | --- |
| Which billing-model guides does this Metronome landing page offer? | Retrieval | **Pass** | Source lines 18–20 retain all four raw cards from raw lines 16–22: pay-as-you-go, enterprise commits, subscriptions with usage, and pre-paid credits. |
| Does this page prove how any model is configured, available, billed, limited, or moved through its lifecycle? | Factual completeness / boundaries | **Pass** | Source lines 14, 20, and 24 explicitly reject those unsupported conclusions. The raw page contains only card labels and routes, so no implementation behavior is inferred. |
| Can a future reader recover the exact card labels and destination paths, then continue to deeper implementation material? | Raw-backlink deep dive | **Pass** | Source line 34 resolves to the exact 23-line raw snapshot, which preserves all four `href` paths. Source lines 28–30 route onward to Metronome, three relevant concepts, and the already-promoted PayGo and enterprise-commit guides. |

Specific defects: none.

## 2. `reset-threshold-notification` — pass (3/3)

Traceability:

- Raw SHA-256: `c25a9c284ee921af560595ff488771555905e4db2e067e311b7931bd59b9735a`.
- Approved candidate/promoted source SHA-256: `9297f1e724c5d22f25b0eaa9c63da3980df8a04aaad5005b5bb212811b4bede5`.
- Source line 81 links directly to the exact raw snapshot. The fact-bearing `metronome-alerts-and-notifications` concept cites the source reciprocally at concept line 47 and preserves its reset semantics at lines 20–22. `metronome-webhooks` and `metronome-customers-and-contracts` are onward context only, so no reciprocal reset-fact citation is required there.

| Future query | Audit dimension | Result | Evidence and assessment |
| --- | --- | --- | --- |
| How do I reset one threshold notification, what identifiers are required, and what does success mean? | Retrieval | **Pass** | Source lines 14–21 and 43–52 retain `POST /v1/customer-alerts/reset`, bearer authentication, JSON media type, required UUID `customer_id` and `alert_id`, immediate reset initiation, asynchronous reassessment, and bodyless `200`. These map to raw lines 11–28 and 105–185. |
| Does `200` mean evaluation finished or guarantee a webhook, and may I safely retry a timeout or assume eligibility, ordering, errors, rate limits, or idempotency? | Factual completeness / boundaries | **Pass** | Source lines 25–41 and 54–71 separate initiation from completion, preserve “may” for webhooks, enumerate state and eligibility unknowns, and reject unsupported retry/idempotency/concurrency guarantees. It also records the OpenAPI ambiguity that the payload properties are required while `requestBody` itself lacks `required: true`. |
| Can a future reader verify the exact OpenAPI operation and continue into alert lifecycle and webhook-delivery semantics? | Raw-backlink deep dive | **Pass** | Source line 81 reaches the exact 187-line raw/OpenAPI snapshot. Source lines 73–77 route to the fact-bearing alerts concept plus the dedicated notification, customer-control, and webhook sources without treating those pages as evidence for undocumented reset behavior. |

Specific defects: none.

## 3. `send-usage-events` — pass (3/3)

Traceability:

- Raw SHA-256: `5fdd07cf1b27bb098d4facfe48a50a3043623e2476475d20d0a3965b0f4fba56`.
- Approved candidate/promoted source SHA-256: `7d324e38107f334ed40d376f158a93aace1e247113c1c6e0954ac2a3dffa66da`.
- Source line 67 links directly to the exact raw snapshot.
- All four fact-bearing concepts cite the source reciprocally: `metronome-event-ingestion` line 76, `metronome-api-idempotency` line 39, `metronome-billable-metrics` line 68, and `metronome-customers-and-contracts` line 114.

| Future query | Audit dimension | Result | Evidence and assessment |
| --- | --- | --- | --- |
| What fields should a Metronome usage event contain, how are customers and timestamps interpreted, and how should direct-ingest failures be retried? | Retrieval | **Pass** | Source lines 18–22 and 24–42 retain the four required string fields, optional properties, customer ID/alias attribution, RFC 3339 and future-time boundary, string-property recommendation, reliable queue, network/`5xx` retry-until-`200`, exponential `429` backoff, and DLQ handling for other `4xx`. These map to raw lines 19–77. |
| Is `transaction_id` permanently unique, are retries safe with new IDs, and does the guide define exact duplicate-window edges, batch/schema limits, historical age, ordering, Segment retries, or provisioning guarantees? | Factual completeness / boundaries | **Pass** | Source lines 26–40 and 46–57 retain the 34-day acceptance-relative boundary, constrain retry safety to preserved IDs, flag the heartbeat wording tension, and enumerate all missing limits and guarantees. No unsupported global-idempotency, permanent-uniqueness, or API-schema inference is needed. |
| Can a future reader inspect the heartbeat algorithm and schema-change warning, then reach endpoint, idempotency, metric, high-volume, and customer-attribution authorities? | Raw-backlink deep dive | **Pass** | Source line 67 reaches raw lines 96–123, including the deterministic minute-bucket ID, two-or-more heartbeat recommendation, metric-breakage warning, and asynchronous customer-creation guidance. Source lines 59–63 route to five dedicated sources and four reciprocal concepts. |

Specific defects: none.

## Overall audit conclusion

Campaign 09 passes the independent fixed query-quality sample: **9/9 queries pass, 0 partial, 0 fail**. Answers are retrievable from the promoted sources, important omissions are expressed as boundaries rather than filled by inference, exact raw snapshots are reachable for deep dives, and fact-bearing concept citations are reciprocal where applicable.

`expansion_required: false`
