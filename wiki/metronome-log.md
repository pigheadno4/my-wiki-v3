---
title: "Metronome Collection and Ingest Log"
type: log
tags: [metronome, usage-based-billing, operations]
---

Newest entries appear first. Detailed collection evidence remains under `tracking/collections/metronome/`; ingest evidence remains under `tracking/ingest/metronome/`.

## 2026-07-29 — Metronome Campaign 04 completed

- Result: all five jobs were approved; 5 failed attempts were retained, retried within the three-attempt limit, and no job was rejected.
- Routing: two standard jobs used native GPT-5.6 Terra and three strong jobs used native GPT-5.6 Sol; Sol performed serial full-raw review and canonical promotion for every job.
- Deterministic gates rejected three `.md` fetch URLs used as canonical URLs, one malformed fixed-schema result, and one result with missing quote locations before review.
- Output: five source summaries plus grounded company, concept, reciprocal-source-link, index, and log updates.
- Coverage after campaign: 25 source summaries ingested and 200 documentation pages pending.
- Evaluation: content-complexity routing remained useful, but fixed-schema compliance was not model-tier-specific; keep the existing validator and exact preflight assertions without adding a classifier.
- Evidence: [campaign selection and result](../tracking/ingest/metronome/metronome-campaign-04/selection-review.md), [campaign monitor](../tracking/ingest/metronome/metronome-campaign-04/monitor.md), and [event journal](../tracking/ingest/metronome/metronome-campaign-04/events.jsonl).

## 2026-07-29 — Canonical ingest: scheduled billing-provider changes

- Ingested: [[source-metronome-guides-customers-billing-manage-customers-schedule-billing-provider-change]] from the complete 137-line guide.
- Concept audit: updated [[metronome-customers-and-contracts]], [[metronome-invoicing]], [[metronome-integrations]], and [[metronome-credits-and-commits]] before canonical source creation; no new concept or comparison page was warranted.
- Sol review preserved the service-period start-versus-end timing conflict, the `issued~at` label, invalid JSON in both request examples, external-provider readiness gaps, and the exactly-once finalized-invoice boundary.
- Link reconciliation added reciprocal references from the Stripe invoice integration, prepaid-threshold guide, and contract edit-history source.
- Campaign 04: attempt 1 failed fixed-schema validation, attempt 2 failed quote-location validation, and attempt 3 passed deterministic validation before serial Sol review.
- Coverage after finalization: 25 source summaries ingested and 200 documentation pages pending.
- Evidence: [campaign monitor](../tracking/ingest/metronome/metronome-campaign-04/monitor.md) and [attempt receipt](../tracking/ingest/metronome/metronome-campaign-04/attempts/schedule-billing-provider-change/attempt-3/receipt.json).

## 2026-07-29 — Canonical ingest: Ingest Events API

- Ingested: [[source-metronome-api-reference-usage-ingest-events]] from the complete 293-line API reference.
- Concept audit: updated [[metronome-event-ingestion]] and [[metronome-billable-metrics]] before canonical source creation; no new concept or comparison page was warranted.
- Sol review retained the one-to-100-event schema, four required fields, 128-character transaction ID limit, 34-day backdate and deduplication window, and the missing response, partial-batch, retry, duplicate, future-time, and cutoff semantics.
- Throughput boundary: the endpoint's 100,000-events-per-second support statement remains distinct from the high-volume guide's 110,000 infrastructure-capacity and 5,000 default-account-limit figures.
- Campaign 04: attempt 1 was rejected because the candidate used the `.md` fetch URL as canonical; attempt 2 corrected the canonical URL and passed deterministic validation before serial Sol review.
- Coverage after finalization: 24 source summaries ingested and 201 documentation pages pending.
- Evidence: [campaign monitor](../tracking/ingest/metronome/metronome-campaign-04/monitor.md) and [attempt receipt](../tracking/ingest/metronome/metronome-campaign-04/attempts/ingest-events/attempt-2/receipt.json).

## 2026-07-29 — Canonical ingest: API pagination

- Ingested: [[source-metronome-api-reference-pagination]] from the complete 61-line API guide.
- Concept audit: no existing concept needed material changes and no standalone concept or comparison page was warranted for this thin API-wide convention.
- Sol review retained the `limit` and `next_page` traversal contract, the recommended 1/50 values and 100 cap, and the undocumented ordering, cursor-lifetime, retry, and endpoint-variation boundaries.
- Campaign 04: attempt 1 was rejected because the candidate used the `.md` fetch URL as canonical; attempt 2 corrected the canonical URL and passed deterministic validation before serial Sol review.
- Coverage after finalization: 23 source summaries ingested and 202 documentation pages pending.
- Evidence: [campaign monitor](../tracking/ingest/metronome/metronome-campaign-04/monitor.md) and [attempt receipt](../tracking/ingest/metronome/metronome-campaign-04/attempts/pagination/attempt-2/receipt.json).

## 2026-07-29 — Canonical ingest: API authentication

- Ingested: [[source-metronome-api-reference-authentication]] from the complete 112-line API guide.
- Concept audit: updated [[metronome-security-principles]] before canonical source creation; no new concept or comparison page was warranted.
- Sol review preserved the distinction between customer bearer tokens with an undocumented expiry and the separate 12-hour engineer credential lifecycle.
- Campaign 04: attempt 1 was rejected because the candidate used the `.md` fetch URL as canonical; attempt 2 corrected the canonical URL and passed deterministic validation before serial Sol review.
- Coverage after finalization: 22 source summaries ingested and 203 documentation pages pending.
- Evidence: [campaign monitor](../tracking/ingest/metronome/metronome-campaign-04/monitor.md) and [attempt receipt](../tracking/ingest/metronome/metronome-campaign-04/attempts/authentication/attempt-2/receipt.json).

## 2026-07-29 — Canonical ingest: prepaid balance thresholds

- Ingested: [[source-metronome-guides-customers-billing-optimize-customer-experience-prepaid-balance-thresholds]] from the complete 269-line guide.
- Concept audit: updated [[metronome-credits-and-commits]], [[metronome-customers-and-contracts]], [[metronome-invoicing]], [[metronome-products-and-rate-cards]], [[metronome-webhooks]], and [[metronome-integrations]] before canonical source creation; no new concept or comparison page was warranted.
- Sol review preserved the source's threshold equality, minimum-field naming, and discount-fraction ambiguities, plus its undocumented concurrency and duplicate-recharge behavior.
- Campaign 04: the strong-tier candidate passed deterministic validation on attempt 1 and then underwent a complete serial Sol reread and promotion review.
- Coverage after finalization: 21 source summaries ingested and 204 documentation pages pending.
- Evidence: [campaign monitor](../tracking/ingest/metronome/metronome-campaign-04/monitor.md) and [attempt receipt](../tracking/ingest/metronome/metronome-campaign-04/attempts/prepaid-balance-thresholds/attempt-1/receipt.json).

## 2026-07-29 — Metronome Campaign 03 completed

- Result: five of five jobs were approved on attempt 1; no job failed, retried, or was rejected.
- Routing: two standard jobs used native GPT-5.6 Terra and three strong jobs used native GPT-5.6 Sol; Sol performed serial full-raw review and canonical promotion for every job.
- Output: five source summaries and grounded updates to existing company and concept pages; no duplicate concept or comparison page was created.
- Quality: preserved the prepaid-guide contradictions, edit-API unknowns, Stripe Tax mapping ambiguity, and explicit missing-information boundaries.
- Coverage after campaign: 20 source summaries ingested and 205 documentation pages pending.
- Evaluation boundary: routing worked for this sample, but full Sol rereads mean the pilot does not establish lower reviewer-token volume.
- Evidence: [campaign monitor](../tracking/ingest/metronome/metronome-campaign-03/monitor.md), [selection and result summary](../tracking/ingest/metronome/metronome-campaign-03/selection-review.md), and [event journal](../tracking/ingest/metronome/metronome-campaign-03/events.jsonl).

## 2026-07-29 — Canonical ingest: Stripe Tax integration

- Ingested: [[source-metronome-integrations-tax-integrations-stripe-tax]] from the complete 184-line guide.
- Concept audit: updated [[stripe-tax]], [[metronome-invoicing]], [[metronome-integrations]], [[metronome-products-and-rate-cards]], and [[metronome-credits-and-commits]]; no duplicate tax concept or comparison page was warranted.
- Sol review retained the Metronome/Stripe responsibility boundary, address and tax-code prerequisites, many-to-one product mapping, finalization timing, threshold override, and the `Product` versus `ContractProduct` and all-tax-provider scope cautions.
- Campaign 03 routing: the strong-tier Sol worker candidate passed deterministic validation and serial full-raw Sol coordinator review on attempt 1.
- Coverage after finalization: 20 source summaries ingested and 205 documentation pages pending.
- Evidence: [campaign monitor](../tracking/ingest/metronome/metronome-campaign-03/monitor.md) and [attempt receipt](../tracking/ingest/metronome/metronome-campaign-03/attempts/stripe-tax/attempt-1/receipt.json).

## 2026-07-29 — Canonical ingest: Edit a Commit API

- Ingested: [[source-metronome-api-reference-credits-and-commits-edit-a-commit]] from the complete 457-line API reference.
- Concept audit: updated [[metronome-credits-and-commits]], [[metronome-customers-and-contracts]], [[metronome-invoicing]], and [[metronome-products-and-rate-cards]]; no endpoint-specific concept or comparison page was warranted.
- Sol review retained schedule add/update/remove requirements, finalized and voided invoice restrictions, selector exclusivity, hierarchy variants, and the undocumented response-ID, `product_id`, proration, error, and null/omission boundaries.
- Campaign 03 routing: the strong-tier Sol worker candidate passed deterministic validation and serial full-raw Sol coordinator review on attempt 1.
- Coverage after finalization: 19 source summaries ingested and 206 documentation pages pending.
- Evidence: [campaign monitor](../tracking/ingest/metronome/metronome-campaign-03/monitor.md) and [attempt receipt](../tracking/ingest/metronome/metronome-campaign-03/attempts/edit-a-commit/attempt-1/receipt.json).

## 2026-07-29 — Canonical ingest: credits and commits guide

- Ingested: [[source-metronome-guides-pricing-packaging-apply-credits-and-commits-create-a-pre-paid-commit]] from the complete 459-line guide.
- Concept audit: updated [[metronome-credits-and-commits]], [[metronome-customers-and-contracts]], [[metronome-products-and-rate-cards]], [[metronome-invoicing]], and [[metronome-usage-based-billing]]; no duplicate concept or comparison page was warranted.
- Sol review preserved contradictions in the guide's prepaid amount, recurring-example JSON, signup/upgrade dates, and `rollover_fraction` representation, with a reciprocal warning on the create-contract API source.
- Campaign 03 routing: the strong-tier Sol worker candidate passed deterministic validation and serial full-raw Sol coordinator review on attempt 1.
- Coverage after finalization: 18 source summaries ingested and 207 documentation pages pending.
- Evidence: [campaign monitor](../tracking/ingest/metronome/metronome-campaign-03/monitor.md) and [attempt receipt](../tracking/ingest/metronome/metronome-campaign-03/attempts/create-pre-paid-commit/attempt-1/receipt.json).

## 2026-07-29 — Canonical ingest: dashboard first-invoice quickstart

- Ingested: [[source-metronome-guides-get-started-metronome-dashboard-quickstart]] from the complete 248-line dashboard guide.
- Concept audit: updated the existing event-ingestion, billable-metric, product/rate-card, customer/contract, invoicing, and webhook concepts; no dashboard-only concept or comparison page was warranted.
- Sol review retained the 2,000-property limit, immutable metric settings, group-key dependencies, Sandbox-only test-event rules, 34-day timestamp window, and invoice/provider boundary.
- Campaign 03 routing: the standard-tier Terra candidate passed deterministic validation and serial full-raw Sol review on attempt 1.
- Coverage after finalization: 17 source summaries ingested and 208 documentation pages pending.
- Evidence: [campaign monitor](../tracking/ingest/metronome/metronome-campaign-03/monitor.md) and [attempt receipt](../tracking/ingest/metronome/metronome-campaign-03/attempts/metronome-dashboard-quickstart/attempt-1/receipt.json).

## 2026-07-29 — Canonical ingest: data export overview

- Ingested: [[source-metronome-guides-reporting-insights-data-export-overview]] from the complete 134-line guide.
- Concept audit: updated [[metronome-reporting-and-analytics]] with destination scope, delivery cadence, freshness, and append-only object-storage semantics; no duplicate concept or comparison page was warranted.
- Sol review confirmed the one-destination boundary, table-specific timing, at-least-once deduplication responsibility, and the absence of a stated retention period.
- Campaign 03 routing: the standard-tier Terra candidate passed deterministic validation and serial full-raw Sol review on attempt 1.
- Coverage after finalization: 16 source summaries ingested and 209 documentation pages pending.
- Evidence: [campaign monitor](../tracking/ingest/metronome/metronome-campaign-03/monitor.md) and [attempt receipt](../tracking/ingest/metronome/metronome-campaign-03/attempts/data-export-overview/attempt-1/receipt.json).

## 2026-07-29 — Campaign 02 query-quality audit

- Scope: an independent reviewer checked all five source pages against all 1,442 raw lines using 15 core, boundary, and trap questions.
- Initial result: 13 pass, 1 partial, and 1 fail. The hard failure omitted the contract-level multi-account `billing_provider_configuration_id` and lookup route; the soft partial omitted the equivalent 6.6-million-events-per-minute throughput figure.
- Resolution: Sol repaired the source and related concepts. Final result: 15 pass, 0 partial, and 0 fail.
- Architecture boundary: no new coordinator machinery, schema, retry behavior, or parallel-ingest abstraction was added.
- Evidence: [Campaign 02 quality audit](../tracking/ingest/metronome/metronome-campaign-02/quality-audit.md).

## 2026-07-28 — Metronome Campaign 02 completed

- Result: five of five jobs were approved on attempt 1; no job failed, retried, or was rejected.
- Execution: three native GPT-5.6 Terra workers produced bounded candidates and suggestions, while Sol performed serial full-raw review, concept audit, canonical promotion, shared-file reconciliation, and final approval.
- Output: five source summaries, two new concepts, and grounded updates to four existing concepts.
- Coverage after campaign: 15 source summaries ingested and 210 documentation pages pending.
- Evidence: [campaign monitor](../tracking/ingest/metronome/metronome-campaign-02/monitor.md), [selection and result summary](../tracking/ingest/metronome/metronome-campaign-02/selection-review.md), and [event journal](../tracking/ingest/metronome/metronome-campaign-02/events.jsonl).

## 2026-07-28 — Canonical ingest: Create a commit API

- Ingested: [[source-metronome-api-reference-credits-and-commits-create-a-commit]] from the complete 605-line API reference.
- Concept audit: updated [[metronome-credits-and-commits]]; no endpoint-specific concept or comparison page was warranted.
- Sol review retained conditional prepaid/postpaid invoice rules, cross-contract scope, targeting semantics, priority ties, gated fields, and the generic recurring-schedule versus postpaid single-item ambiguity.
- Terra/Sol campaign: attempt 1 passed deterministic candidate validation and serial Sol review after bounded canonical repair.
- Coverage after finalization: 15 source summaries ingested and 210 documentation pages pending.
- Evidence: [campaign monitor](../tracking/ingest/metronome/metronome-campaign-02/monitor.md) and [attempt receipt](../tracking/ingest/metronome/metronome-campaign-02/attempts/create-commit/attempt-1/receipt.json).

## 2026-07-28 — Canonical ingest: Stripe invoice integration

- Ingested: [[source-metronome-integrations-invoice-integrations-stripe]] from the complete 331-line guide.
- Concept audit: updated [[metronome-invoicing]] and [[metronome-integrations]]; no new concept or cross-provider comparison page was warranted.
- Sol review restored multi-account routing, non-retroactive activation, payment-gated product mapping, account-level setting boundaries, Stripe-side payment timing, and representation limits omitted by the worker draft.
- Terra/Sol campaign: attempt 1 passed deterministic candidate validation and serial Sol review after canonical repair.
- Coverage after finalization: 14 source summaries ingested and 211 documentation pages pending.
- Evidence: [campaign monitor](../tracking/ingest/metronome/metronome-campaign-02/monitor.md) and [attempt receipt](../tracking/ingest/metronome/metronome-campaign-02/attempts/stripe-invoice-integration/attempt-1/receipt.json).

## 2026-07-28 — Canonical ingest: enterprise commitment model

- Ingested: [[source-metronome-guides-pricing-packaging-billing-model-guides-enterprise-commit]] from the complete 267-line guide.
- Concept audit: created [[metronome-credits-and-commits]] and updated [[metronome-products-and-rate-cards]] and [[metronome-customers-and-contracts]]; no comparison page was warranted.
- Sol review preserved two source-document inconsistencies: `product` versus the API reference's `product_id`, and an upsell described as a commitment but implemented as a scheduled charge.
- Terra/Sol campaign: attempt 1 passed deterministic candidate validation and serial Sol review after canonical repair.
- Coverage after finalization: 13 source summaries ingested and 212 documentation pages pending.
- Evidence: [campaign monitor](../tracking/ingest/metronome/metronome-campaign-02/monitor.md) and [attempt receipt](../tracking/ingest/metronome/metronome-campaign-02/attempts/enterprise-commit/attempt-1/receipt.json).

## 2026-07-28 — Canonical ingest: Metronome Stripe App

- Ingested: [[source-metronome-guides-get-started-stripe-marketplace-app]] from the complete 154-line guide.
- Concept audit: created [[metronome-integrations]] and updated [[metronome-customers-and-contracts]]; no comparison page was warranted.
- Terra/Sol campaign: attempt 1 passed deterministic candidate validation and serial Sol review.
- Coverage after finalization: 12 source summaries ingested and 213 documentation pages pending.
- Evidence: [campaign monitor](../tracking/ingest/metronome/metronome-campaign-02/monitor.md) and [attempt receipt](../tracking/ingest/metronome/metronome-campaign-02/attempts/stripe-marketplace-app/attempt-1/receipt.json).

## 2026-07-28 — Canonical ingest: usage events at scale

- Ingested: [[source-metronome-guides-events-high-volume-ingestion]] from the complete 85-line guide.
- Concept audit: updated [[metronome-event-ingestion]] with throughput, batching, observability, and recovery boundaries; no new concept or comparison page was warranted.
- Terra/Sol campaign: attempt 1 passed deterministic candidate validation and serial Sol review.
- Coverage after finalization: 11 source summaries ingested and 214 documentation pages pending.
- Evidence: [campaign monitor](../tracking/ingest/metronome/metronome-campaign-02/monitor.md) and [attempt receipt](../tracking/ingest/metronome/metronome-campaign-02/attempts/high-volume-ingestion/attempt-1/receipt.json).

## 2026-07-28 — Minimum promotion pilot closed

- Result: all five jobs were approved and promoted; no job failed or was rejected.
- Boundary correction: future campaign jobs retain their canonical URL, and the coordinator now rejects candidate pages that omit or change it or use a filename-only raw backlink.
- Scope: this closes `metronome-minimum-pilot-01`; it does not authorize bulk ingest or bypass serial Sol review.
- Evidence: [campaign monitor](../tracking/ingest/metronome/metronome-minimum-pilot-01/monitor.md) and [event journal](../tracking/ingest/metronome/metronome-minimum-pilot-01/events.jsonl).

## 2026-07-28 — Canonical ingest: security principles

- Ingested: [[source-metronome-guides-platform-configuration-security-principles]] from the complete 29-line guide.
- Concept audit: created [[metronome-security-principles]] before canonical source promotion; no comparison page was warranted.
- Terra/Sol dry run: attempt 1 reached `review_approved`; canonical promotion retained the four grounded security claims and added the required canonical URL and path-qualified raw backlink.
- Coverage after finalization: 10 source summaries ingested and 215 documentation pages pending.
- Evidence: [campaign monitor](../tracking/ingest/metronome/metronome-minimum-pilot-01/monitor.md) and [approved attempt receipt](../tracking/ingest/metronome/metronome-minimum-pilot-01/attempts/security-principles/attempt-1/receipt.json).

## 2026-07-28 — Canonical ingest: setup webhooks

- Ingested: [[source-metronome-guides-platform-configuration-setup-webhooks]] from the complete 870-line guide.
- Concept audit: created [[metronome-webhooks]] before canonical source promotion; no comparison page was warranted.
- Terra/Sol dry run: attempt 1 reached `review_approved`; canonical promotion retained the grounded delivery and verification rules and added the required canonical URL and path-qualified raw backlink.
- Coverage after finalization: 9 source summaries ingested and 216 documentation pages pending.
- Evidence: [campaign monitor](../tracking/ingest/metronome/metronome-minimum-pilot-01/monitor.md) and [approved attempt receipt](../tracking/ingest/metronome/metronome-minimum-pilot-01/attempts/setup-webhooks/attempt-1/receipt.json).

## 2026-07-28 — Canonical ingest: Get Contract Edit History API

- Ingested: [[source-metronome-api-reference-contracts-get-contract-edit-history]] from the complete 2,672-line API reference.
- Concept audit: updated [[metronome-customers-and-contracts]]; no endpoint-specific concept or comparison page was warranted.
- Terra/Sol dry run: attempt 1 reached `review_approved`; canonical promotion retained the grounded audit scope and added the required canonical URL and path-qualified raw backlink.
- Coverage after finalization: 8 source summaries ingested and 217 documentation pages pending.
- Evidence: [campaign monitor](../tracking/ingest/metronome/metronome-minimum-pilot-01/monitor.md) and [approved attempt receipt](../tracking/ingest/metronome/metronome-minimum-pilot-01/attempts/get-contract-edit-history/attempt-1/receipt.json).

## 2026-07-28 — Canonical ingest: Preview Events API

- Ingested: [[source-metronome-api-reference-invoices-preview-events]] from the complete 1,020-line API reference.
- Concept audit: updated [[metronome-event-ingestion]], [[metronome-invoicing]], and [[metronome-usage-based-billing]]; no new concept or comparison page was warranted.
- Terra/Sol dry run: attempt 1 reached `review_approved`; canonical promotion retained the grounded API constraints and added the required canonical URL and path-qualified raw backlink.
- Coverage after finalization: 7 source summaries ingested and 218 documentation pages pending.
- Evidence: [campaign monitor](../tracking/ingest/metronome/metronome-minimum-pilot-01/monitor.md) and [approved attempt receipt](../tracking/ingest/metronome/metronome-minimum-pilot-01/attempts/preview-events/attempt-1/receipt.json).

## 2026-07-28 — Canonical ingest: design usage events

- Ingested: [[source-metronome-guides-events-design-usage-events]] from the complete 88-line guide.
- Concept audit: updated [[metronome-event-ingestion]] and [[metronome-billable-metrics]]; no new concept or comparison page was warranted.
- Terra/Sol dry run: attempt 1 was returned because its log suggestion targeted `wiki/log.md`; attempt 2 corrected the destination to `wiki/metronome-log.md` and passed serial Sol review.
- Coverage after finalization: 6 source summaries ingested and 219 documentation pages pending.
- Evidence: [campaign monitor](../tracking/ingest/metronome/metronome-minimum-pilot-01/monitor.md) and [approved attempt receipt](../tracking/ingest/metronome/metronome-minimum-pilot-01/attempts/design-usage-events/attempt-2/receipt.json).

## 2026-07-14 — Luna/Sol five-page pilot concluded

- Decision: `scale_with_changes`; Luna is approved only as a constrained draft/evidence worker, with Sol remaining mandatory for concepts, contradictions, shared state, promotion, and final approval.
- Results: 5 accepted cases, 7 Luna attempts, 23 recorded Sol repairs, 59 coordinator repair minutes, and 4 production sources added.
- Independent review: agreed with `scale_with_changes`, found retry-regression and evidence/accounting gaps, and identified two additional SDK example inconsistencies now preserved on the canonical source.
- Coverage remains: 5 source summaries ingested and 220 documentation pages pending.
- Report: [Metronome GPT-5.6 Luna five-page pilot](../tracking/ingest/metronome/pilot/luna-sol-five-page-pilot-report.md).

## 2026-07-14 — Luna/Sol pilot: create-contract API

- Ingested: [[source-metronome-api-reference-contracts-create-a-contract]] from the complete 4,561-line endpoint reference.
- Concept audit: updated [[metronome-customers-and-contracts]] before promoting the canonical source; no endpoint-specific concept was created.
- Luna result: passed on attempt 1 with four exact quotes and a correct raw deep-dive link.
- Sol review: added package-mode restrictions, account/feature-gated field boundaries, conditional subscription quantity rules, immutable charge-consolidation behavior, and the `409` versus listed-response caveat.
- Coverage after finalization: 5 source summaries ingested and 220 documentation pages pending.
- Evidence: [worker run](../tracking/ingest/metronome/pilot/runs/pilot-create-contract-luna/) and [final receipt](../tracking/ingest/metronome/pilot/receipts/pilot-create-contract-luna-final.json).

## 2026-07-14 — Luna/Sol pilot: data-export database reference

- Ingested: [[source-metronome-guides-reporting-insights-data-export-database-reference]] from the complete 1,600-line schema reference.
- Concept audit: created [[metronome-reporting-and-analytics]] before promoting the canonical source.
- Luna result: passed on attempt 1 with four exact quotes and a correct raw deep-dive link.
- Sol review: elevated the all-columns-nullable warning, added row-grain and time/version navigation, clarified the commits-table scope, and narrowed the Private Beta wording to the note's actual invoicing statement.
- Coverage after finalization: 4 source summaries ingested and 221 documentation pages pending.
- Evidence: [worker run](../tracking/ingest/metronome/pilot/runs/pilot-database-reference-luna/) and [final receipt](../tracking/ingest/metronome/pilot/receipts/pilot-database-reference-luna-final.json).

## 2026-07-14 — Luna/Sol pilot: developer SDK walkthrough

- Ingested: [[source-metronome-guides-get-started-developer-sdks]] from the complete 944-line guide.
- Concept audit: created [[metronome-event-ingestion]], [[metronome-billable-metrics]], [[metronome-products-and-rate-cards]], and [[metronome-customers-and-contracts]] from the planned taxonomy; no separate SDK concept was warranted.
- Luna result: passed on attempt 1 with five exact quotes and a correct raw deep-dive link.
- Sol review: restored the 34-day event window, the future-event metric boundary, pricing/effective-period rules, and two language-example caveats; no external platform contradiction was found.
- Coverage after finalization: 3 source summaries ingested and 222 documentation pages pending.
- Evidence: [worker run](../tracking/ingest/metronome/pilot/runs/pilot-developer-sdks-luna/) and [final receipt](../tracking/ingest/metronome/pilot/receipts/pilot-developer-sdks-luna-final.json).

## 2026-07-14 — Luna/Sol pilot: invoicing overview

- Ingested: [[source-metronome-guides-invoices-overview]] from the complete 31-line overview.
- Concept: created [[metronome-invoicing]] after the mandatory concept audit.
- Luna result: attempt 1 failed exact-line grounding after using unsupported invoice-state content; attempt 2 passed with five exact quotes.
- Sol review: consolidated four proposed sub-concepts into one planned invoicing concept and tightened the ASC 606 wording; no contradiction was found.
- Coverage after finalization: 2 source summaries ingested and 223 documentation pages pending.
- Evidence: [worker run](../tracking/ingest/metronome/pilot/runs/pilot-invoices-overview-luna/) and [final receipt](../tracking/ingest/metronome/pilot/receipts/pilot-invoices-overview-luna-final.json).

## 2026-07-14 — Strong-model baseline ingest

- Ingested: [[source-metronome-guides-get-started-home]] from the complete 140-line documentation landing page.
- Concept: created [[metronome-usage-based-billing]] after the mandatory concept audit.
- Worker role: `strong_baseline`; worker commit `e9a90d0` touched only its leased source and concept files.
- Coverage after finalization: 1 source summary ingested and 224 documentation pages pending.
- Validation: exact grounding quotes, write ownership, focused wiki validation, capsule reconciliation, and the full test suite passed.
- Receipt: [pilot-home-baseline.json](../tracking/ingest/metronome/pilot/receipts/pilot-home-baseline.json).

## 2026-07-13 — Initial English documentation collection

- Collected corpus: 225 English canonical documentation pages and 2 OpenAPI artifacts.
- Result: 222 new items, 5 unchanged smoke-test items, and 0 failures.
- Discovery reconciliation: 208 pages in both discovery sources and 17 additional English sitemap-only pages.
- Ingest status: not started; all 225 documentation pages remain pending.
- Evidence: [collection status](../tracking/collections/metronome/collection-status.md), [run manifest](../tracking/collections/metronome/runs/2026-07-13T100930-manifest.md), and [detailed JSONL run record](../tracking/collections/metronome/runs/2026-07-13T100930.jsonl).

## Related

- [[metronome-index]]
- [[metronome]]
