# Metronome Campaign 10 Independent Query-Quality Audit

Date: 2026-08-01
Repository: `/Users/tengtao/Development/wiki-v2`
Repository writes: none

## Decision

overall_decision: **approve**

expansion_required: **false**

The three immutable audit jobs passed all nine realistic future-query tests. No material partial or fail was found, so the audit stops at the predetermined sample.

| Result | Pages | Queries |
| --- | ---: | ---: |
| Pass | 3 | 9 |
| Partial | 0 | 0 |
| Fail | 0 | 0 |

Materiality rule: a partial or fail is material when an answer-critical fact, boundary, contradiction, raw link, or required reciprocal fact citation is absent or incorrect. Cosmetic wording and navigation-only concept links are not material.

Mechanical evidence:

- All three raw SHA-256 values match the manifest.
- All three promoted sources are byte-for-byte identical to their final reviewer-approved candidates.
- Canonical URLs, `raw_files`, and path-qualified Raw Sources links match the manifest and resolve.
- `python3 scripts/validate_wiki.py` passed for the three sources and eleven linked concepts: 14 files, no issues.
- Each source occurs exactly once in the Metronome provider index and company catalog.

## 1. `workato-connector` — pass (3/3)

Traceability:

- Raw SHA-256: `12b7d512419d74b31334bb091e1462ce41a164cfd5fff855b075fd960f9ce499`.
- Approved candidate/promoted source SHA-256: `b7545984ffef96c79ad94538a58636d886b68838d696fb72ae0f2949fa29cf80`.
- The fact-bearing `metronome-integrations` concept cites the source reciprocally and preserves the per-environment and capability boundaries. The provider index and company catalog both route to the page.

| Future query | Audit dimension | Result | Evidence and assessment |
| --- | --- | --- | --- |
| How do I connect Workato to Metronome, what workflows are illustrated, and do environments share a connection? | Retrieval | **Pass** | Source lines 14–20 retain the SDK-like connector role, third-party invoicing, customer and contract provisioning, install/token/connection sequence, and one connection per Metronome environment. |
| Does this page prove connector action coverage, token permissions, triggers, mappings, retries, errors, or token rotation? | Factual completeness / boundaries | **Pass** | Source line 24 explicitly lists these unknowns and does not inflate an SDK-like connector into complete endpoint coverage or operational guarantees. |
| Can a reader inspect the exact four setup steps, connector URL, token-authorization route, and environment note? | Raw-backlink deep dive | **Pass** | Source line 33 reaches the exact 28-line raw snapshot, which preserves the external connector URL, authorization link, ordered steps, and environment note. |

Specific defects: none.

## 2. `production-checklist` — pass (3/3)

Traceability:

- Raw SHA-256: `b65117c3c1f7847ad97e02d3b3bea9dd5b11dbd7cc45fc8e1cbef9f7733e7e9a`.
- Approved candidate/promoted source SHA-256: `a62d6f1e7e28863d6f957b1309d24e29c06a2190a0f33a53efad53f56730d835`.
- All five fact-bearing concepts cite the source reciprocally: `metronome-event-ingestion`, `metronome-invoicing`, `metronome-security-principles`, `metronome-webhooks`, and `metronome-reporting-and-analytics`. The other linked concepts are onward context only.

| Future query | Audit dimension | Result | Evidence and assessment |
| --- | --- | --- | --- |
| What should a team verify before taking a Metronome billing integration live? | Retrieval | **Pass** | Source lines 14–22 and 24–42 preserve metering, pricing, customer/contract, invoice, production-token, webhook, monitoring, export, end-to-end, and rollback checks without presenting the list as certification. |
| Are `properties` globally required, is backdating limited to 14 days, does the 5xx/429/4xx policy define outbound webhook behavior, and does one dry run guarantee billing or payment correctness? | Factual completeness / boundaries | **Pass** | Source lines 28, 32, 34, 38, and 42–49 preserve the `properties` contradiction, distinguish 14-day test coverage from the 34-day ingest window, leave retry direction/ownership unresolved, and reject payment, delivery, audit, export, and rollback guarantees. |
| Can a reader recover the complete checklist and continue to authoritative ingest, authentication, webhook, and export material? | Raw-backlink deep dive | **Pass** | Source line 59 reaches the exact 189-line raw checklist. Source lines 53–55 route to eleven concepts and six dedicated sources, while fact-bearing concepts retain the source-specific readiness boundaries. |

Specific defects: none.

## 3. `segment-integration` — pass (3/3)

Traceability:

- Raw SHA-256: `e40b344b8ac5ff29c4875474fba52fcd55eac53613ecae7a3c7c6c96289f6048`.
- Approved candidate/promoted source SHA-256: `08f06a8e4f00906afb518e5fb5a7c58ed8deef9cf1ef34d74d5ac9a8a9ae4693`.
- The two fact-bearing concepts, `metronome-event-ingestion` and `metronome-integrations`, cite the source reciprocally. `metronome-api-idempotency` and `metronome-customers-and-contracts` are navigation-only here; no Campaign 10 Segment fact was merged into those pages.

| Future query | Audit dimension | Result | Evidence and assessment |
| --- | --- | --- | --- |
| How do I configure Segment's Metronome destination, which fields must be mapped, what is the default transaction ID, and how do conditional actions work? | Retrieval | **Pass** | Source lines 18–21 and 23–37 retain destination setup, all five explicit mappings, RFC 3339 timestamp, `messageId` default with manual override, and conditional Destination Actions whose “subscriptions” are routing rules rather than billing subscriptions. |
| Does Segment make `properties` required for direct `/ingest`, guarantee permanent exactly-once processing, define customer alias mapping, or inherit direct-ingest batching/retry limits? | Factual completeness / boundaries | **Pass** | Source lines 27–44 scope `properties` to the adapter, preserve the separate 34-day duplicate window, mark customer identity resolution unknown, and reject unsupported managed-delivery, retry, ordering, batching, and observability guarantees. |
| Can a reader verify the exact text and worked example, including whether the image-only mapping expressions are recoverable? | Raw-backlink deep dive | **Pass** | Source line 54 reaches the exact 78-line raw snapshot. Source line 31 correctly records that the worked event is textual but the resulting mapping is image-only, preventing reconstruction of unsupported expressions while preserving the raw evidence boundary. |

Specific defects: none.

## Overall conclusion

Campaign 10 passes the fixed independent query-quality sample: **9/9 queries pass, 0 partial, 0 fail**. Retrieval is direct, answer-critical contradictions and unknowns are explicit, exact raw snapshots are reachable, and reciprocal concept citations are present wherever Campaign 10 contributed durable facts.

`expansion_required: false`
