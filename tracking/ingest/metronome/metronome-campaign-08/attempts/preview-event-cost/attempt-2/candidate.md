---
title: "Preview event costs"
type: source
date_ingested: 2026-07-31
canonical_url: "https://docs.metronome.com/guides/customers-billing/optimize-customer-experience/preview-event-cost"
original_format: webpage
raw_files:
  - "metronome/guides/customers-billing/optimize-customer-experience/preview-event-cost-2026-07-13.md"
tags: [metronome, event-preview, usage-events, pricing, contracts, draft-invoices]
---

## Overview

Metronome's Preview Events endpoint simulates how proposed usage events would affect a customer's invoices under the customer's contract configuration without processing or billing those events. The guide positions it for pre-action cost estimates, budget planning, and what-if analysis, while documenting merge and replace modes, draft-invoice-shaped responses, transaction-ID handling, an 8-requests-per-second client limit, and exclusion of SQL-based billable metrics.

## Key takeaways

- Preview is a calculation path, not event ingestion or billing: the source says the submitted events are neither processed nor billed.
- The calculation evaluates the customer's contract and can reflect tiered pricing, commits and credits, free allotments, and multiple products. It does not establish compatibility with every contract or pricing feature.
- `merge` combines the preview events with existing usage in the billing period for incremental impact; `replace` ignores existing usage and evaluates only the proposed events.
- The response uses draft invoice records with totals and line items. Customers with multiple active contracts receive a separate preview invoice for each contract rather than one consolidated result.
- The endpoint is limited to 8 requests per second per client, is not intended to validate every event in real time, and rejects a preview with HTTP 400 when the evaluated customer invoice contains SQL-based billable metrics.
- The guide and the dedicated API reference conflict on duplicate transaction IDs inside one request: this guide says they are deduplicated, while the API source says they cause an error.

## Contract and pricing evaluation

The guide says preview events are evaluated against the customer's actual contract configuration. Its documented pricing cases include volume tiers and transitions, commit and credit coverage versus overage, included free usage, and costs spanning multiple products. These bullets explain intended calculation inputs but do not define pricing precedence, balance-snapshot timing, contract-version consistency, effective-dated changes, unsupported price types, or whether every optional contract feature participates.

When a customer has multiple active contracts, the endpoint returns separate invoice records keyed by contract ID. The page does not explain event-to-contract routing, whether one event can affect several contracts, how usage filters are applied, or whether the results share one atomic configuration snapshot.

## Preview modes

`merge` mode combines proposed events with the customer's existing billing-period usage. The guide's free-allotment example starts at 99 of 100 included calls and previews five more, producing one additional free call and four billable calls.

`replace` mode ignores existing usage and evaluates only the preview events for a clean-slate scenario. The page does not say that replace mode ignores contract terms, commits, credits, or free allotments; it says only that existing usage is ignored. It also does not define the default mode in this guide, so callers should use the dedicated API reference for request defaults.

## Request and response boundary

The basic request posts an `events` array and explicit mode to `POST /v1/customers/{customer_id}/previewEvents`. Its example event supplies `event_type`, `timestamp`, and string-valued properties but no `transaction_id`. The guide does not define full field requiredness, batch-size limits, timestamp bounds, property types, authentication scope, or general validation errors.

The response is an array of draft-invoice-shaped objects containing a contract ID, period timestamps, credit type, `DRAFT` status, total, billable status, and line items with product, quantity, unit-price, and other presentation fields. Because the endpoint is explicitly a simulation that does not process or bill the events, the response must not be treated as a finalized, delivered, collectible, or necessarily persisted invoice. The guide does not define preview-record retention, whether returned IDs can be retrieved later, payment status, downstream delivery, tax behavior, or revenue-recognition effects.

> [!warning] Example quantity and arithmetic mismatch
> The request says it previews 100 compute hours, but the response shows quantity `10` and unit price `4900`; its only displayed line item has total `0` while the invoice total is `49000`. The page supplies no conversion, additional line, credit application, or other explanation that reconciles these values. Treat the response as a structural illustration, not an authoritative pricing calculation.

The shortened multiple-contract response contains JavaScript-style comments and is likewise illustrative rather than valid JSON.

## Transaction-ID behavior

The guide says identical `transaction_id` values within the same preview request are deduplicated against each other and that IDs matching `/ingest` events from the prior 34 days are also deduplicated. It does not define the resulting response, whether a duplicate is silently omitted, whether payload differences matter, the exact 34-day boundary, or whether submitting a preview transaction ID reserves or persists that ID for later preview or ingest calls.

> [!warning] Documentation contradiction
> This guide says duplicate `transaction_id` values in one preview request are deduplicated. The existing dedicated Preview Events API source says duplicate IDs in the same request cause an error. Verify current endpoint behavior before relying on either same-request rule. Both sources agree that preview IDs are checked against ingested events from the preceding 34 days.

## Performance and limitations

The guide documents an 8 RPS limit per client and says the endpoint is unsuitable for real-time validation of every event. It recommends caching repeated calculations and batching multiple proposed events, but does not define cache validity, maximum batch size, client identity, rate-limit headers, retry behavior, concurrency, latency, or freshness. Relevant pricing properties must be included, and both modes should be tested during development.

If SQL-based billable metrics are present on the customer invoice being evaluated, the endpoint returns HTTP 400. The page does not define whether one SQL metric excludes all active contracts, how the affected invoice is selected, the error body, mixed streaming/SQL behavior, or a fallback calculation path.

## Related

- Company: [[metronome]]
- Concepts: [[metronome-invoicing]], [[metronome-event-ingestion]], [[metronome-usage-based-billing]], [[metronome-products-and-rate-cards]], [[metronome-customers-and-contracts]], [[metronome-billable-metrics]]
- Related source: [[source-metronome-api-reference-invoices-preview-events]]

## Raw Sources

- [[raw/metronome/guides/customers-billing/optimize-customer-experience/preview-event-cost-2026-07-13|2026-07-13 snapshot — cost-preview modes, contract pricing, draft response, deduplication, and limits]]
