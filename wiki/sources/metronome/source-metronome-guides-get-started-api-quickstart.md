---
title: "Metronome API Quickstart"
type: source
date_ingested: 2026-08-27
canonical_url: "https://docs.metronome.com/guides/get-started/api-quickstart.md"
original_format: webpage
raw_files:
  - "metronome/guides/get-started/api-quickstart-2026-07-13.md"
tags: [metronome, api, usage-based-billing, event-ingestion, billable-metrics, rate-cards, contracts, invoicing]
---

## Overview

This guide is a sandbox onboarding route from an application usage schema to a first Metronome draft invoice. It shows the principal data flow: an application sends identified customer usage; billable metrics aggregate it; products and a shared rate card define presentation and price; a customer contract supplies customer-specific billing terms; and Metronome rates matching events into invoices, with an optional billing provider handling downstream collection.

## Query-critical facts

- The bearer token selects the environment: sandbox tokens access only sandbox data and production tokens only production data. The quickstart requires a sandbox account and token and does not make a sandbox setup production-ready.
- The programmatic onboarding order is billable metric, product, rate card and rates, customer, then contract; events follow. The contract links customer and rate card, while the event-to-invoice path depends on exact agreement among event type, metric filters and group keys, product group-key assignment, dimensional rate values, and customer identity.
- Event design is an early decision point. `transaction_id`, `customer_id`, `event_type`, and `timestamp` are required by this guide; customer identity may be the Metronome UUID or a configured ingest alias; timestamps may be backdated up to 34 days and future timestamps are rejected; property values should be strings, and the guide states a 2,000-property maximum.
- The worked event-schema and `/v1/ingest` payloads use March 9, 2026 timestamps, but this page was fetched July 13, 2026 and says events older than 34 days are rejected. Callers must replace the examples' `timestamp` values with current, non-future timestamps inside the rolling 34-day window, and use unique transaction IDs, for the walkthrough events to reach usage calculations and the draft invoice.
- Billable-metric group keys must be selected before creation for any dimension that may drive pricing or invoice display. The guide says group keys, property filters, and aggregation settings cannot later be changed; streaming group-key properties must also have an existence property filter. Product pricing and presentation keys must be subsets of the metric's group keys.
- A customer can be created with application-owned ingest aliases. A contract can generate Metronome-visible invoices without a billing provider; Stripe delivery is optional and requires the separate account and customer configuration described by the Stripe integration authority.
- HTTP `200` from `/v1/ingest` means acceptance, but the response can contain per-event errors. Stored events may still fail to enter usage calculations when no billable metric matches, and a matched event may fail to rate when its pricing-group values do not match a rate-card entry. Transaction-ID search and the Events dashboard are diagnostic views, not proof of complete billing or collection.
- The quickstart's invoice outcome is a draft that accumulates usage, followed by a stated 24-hour end-of-period grace period and finalization. Its optional Stripe route is described as pushing the invoice about one hour after finalization, while payment status and collection remain with the billing provider.

## Material boundaries

> [!warning] Stale worked event timestamps
> The raw snapshot was fetched on July 13, 2026, but its event-schema and ingest examples use March 9, 2026 timestamps. Those timestamps were already outside the page's stated 34-day backdating window at collection time. Copying the payloads literally therefore cannot complete the advertised first-invoice path: substitute current, non-future in-window timestamps before ingestion, and keep transaction IDs unique.

- The curl payloads are a worked onboarding path, not complete API request, response, validation, error, concurrency, or recovery contracts. Every shown REST operation is a POST; the separate API-wide [[source-metronome-api-reference-idempotency|idempotency authority]] says `Idempotency-Key` applies to all POST endpoints, but the quickstart examples omit that header and establish no endpoint-specific retry or ambiguous-failure recovery behavior. Event `transaction_id` deduplication is a distinct ingest mechanism.
- The shared-rate-card recommendation and pricing examples do not define propagation timing, grandfathering, override precedence, missing-dimensional-rate fallback, retroactive recalculation, or invoice correction. Dedicated product, rate-card, contract, and invoice authorities remain controlling.
- The guide's approximate batching throughput, dashboard timing, draft visibility, and Stripe-delivery timing are onboarding statements, not service-level, provider-acceptance, payment, settlement, tax, accounting, reconciliation, or production-readiness guarantees.

## Raw-detail coverage map

Use the complete raw page for the core-object diagram and definitions; prerequisites and token environment behavior; the event payload, its stale March 9, 2026 example timestamps and required substitution with current non-future timestamps inside the stated 34-day window, required fields, common event patterns, property guidance, and 2,000-property limit; both streaming and SQL metric examples, aggregation choices, group-key table, and immutability warning; product types, conversions, and product payload; rate-card creation, rate entries, dimensional and tiered pricing, custom pricing units, and commit-rate examples; customer alias and contract payloads; optional Stripe configuration; batched event payload, stated throughput, acceptance and rating diagnostics, troubleshooting; and the draft-to-provider invoice walkthrough and next-step routes. Dedicated API references remain authoritative for complete schemas, error catalogs, idempotency, and operational guarantees.

## Related

- Company: [[metronome]]
- Primary concepts: [[metronome-usage-based-billing]], [[metronome-event-ingestion]], [[metronome-billable-metrics]], [[metronome-products-and-rate-cards]], [[metronome-customers-and-contracts]], [[metronome-invoicing]], [[metronome-api-idempotency]]
- Secondary concept: [[metronome-packages-and-aliases]]
- Related sources: [[source-metronome-api-reference-idempotency]], [[source-metronome-guides-get-started-metronome-dashboard-quickstart]], [[source-metronome-integrations-invoice-integrations-stripe]]

## Raw Sources

- [[raw/metronome/guides/get-started/api-quickstart-2026-07-13|2026-07-13 snapshot - complete API onboarding flow, stale event timestamps and 34-day boundary, payload examples, rating diagnostics, invoice verification, and integration limits]]
