---
title: "Metronome Collection and Ingest Log"
type: log
tags: [metronome, usage-based-billing, operations]
---

Newest entries appear first. Detailed collection evidence remains under `tracking/collections/metronome/`; ingest evidence remains under `tracking/ingest/metronome/`.

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
