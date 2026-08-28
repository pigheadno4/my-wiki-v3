---
title: "Metronome Token Billing"
type: source
date_ingested: 2026-08-28
original_format: webpage
canonical_url: "https://docs.metronome.com/guides/pricing-packaging/billing-model-guides/token-billing"
raw_files:
  - "metronome/guides/pricing-packaging/billing-model-guides/token-billing-2026-08-28.md"
tags: [metronome, token-billing, ai, usage-based-billing, rate-cards, pricing]
---

## Overview

This private-preview guide describes Metronome's managed Token Billing workflow for passing LLM-token costs to customers with a markup. It connects managed AI products and rates on a rate card to optional custom pricing units and package allowances, customer contracts, and token-usage events.

## Query-critical facts

- Token Billing is in private preview and requires access through Metronome support or the waitlist.
- Enabling managed AI-provider pricing on a rate card lets an operator select models and enter markup percentages. Metronome then creates the managed AI billable metrics, products, and rates rather than requiring those objects to be created separately.
- Token Billing does not support non-USD fiat because the documented provider prices are denominated in USD. A merchant may instead price in a custom unit by defining a USD-to-custom-unit conversion; the custom unit is not another fiat-currency path.
- The rate card's default markup applies when newly released models are added automatically. Automatic rate-card repricing after a provider changes an existing model's underlying price is described only as coming soon, so this page does not establish that behavior today.
- The worked credit-based plan uses a Package to combine a monthly custom-unit allocation with the rate card, then provisioning by package creates a customer-specific contract. The guide also points to payment-gated incremental credits and contract overrides as optional extensions.
- Usage events use `event_type: token-billing`; token counts are separated into input, cached input, output, and cache-write properties, while `model` and `provider` select the applicable rate. The guide instructs operators to confirm in Events that an event matched a billable metric; submission alone is not documented as proof of rating or billing.

## Material boundaries and unknowns

- This is a product workflow and worked example, not a complete schema or operational contract for metric creation, pricing calculations, package or contract provisioning, event validation, rating, invoicing, or recovery. The complete UI steps, API and SDK examples, field names, and token-type details remain in raw.
- The documented automation covers adding newly released models at the configured default markup. The page does not define catalog-update latency, model removal or renaming, fallback behavior, rate effective time, precision or rounding, provider-cost verification, margin guarantees, or reconciliation after either model or provider-price changes.
- The contract-create and ingest examples are POST operations and omit `Idempotency-Key`. The separate API-wide authority applies that header to POST requests, while usage `transaction_id` is a distinct ingest-deduplication mechanism; this guide adds no endpoint-specific retry, concurrency, partial-success, or ambiguous-failure recovery guarantee.
- The fictional Designr amounts, identifiers, models, markup, and credit allocation are illustrative. They do not establish recommended economics, provider availability, or a runnable production configuration.

## Raw-detail coverage map

| Detail category | Exact evidence route |
| --- | --- |
| Private-preview access, use case, and managed rate-card setup in USD or a custom pricing unit | [[raw/metronome/guides/pricing-packaging/billing-model-guides/token-billing-2026-08-28|complete raw snapshot]] |
| Model selection, default and per-model markups, conversion setup, and model/token-type rate verification | [[raw/metronome/guides/pricing-packaging/billing-model-guides/token-billing-2026-08-28|complete raw snapshot]] |
| Package allowance, contract provisioning examples across SDKs, incremental-credit route, and overrides | [[raw/metronome/guides/pricing-packaging/billing-model-guides/token-billing-2026-08-28|complete raw snapshot]] |
| Event payloads across SDKs, token property meanings and support note, metric-match check, and model-update boundary | [[raw/metronome/guides/pricing-packaging/billing-model-guides/token-billing-2026-08-28|complete raw snapshot]] |

## Related

- Company: [[metronome]]
- Primary concepts: [[metronome-token-billing]], [[metronome-products-and-rate-cards]], [[metronome-billable-metrics]], [[metronome-event-ingestion]]
- Secondary concepts: [[metronome-currencies-and-custom-pricing-units]], [[metronome-packages-and-aliases]], [[metronome-customers-and-contracts]], [[metronome-api-idempotency]]
- Related sources: [[source-metronome-api-reference-idempotency]], [[source-metronome-api-reference-usage-ingest-events]], [[source-metronome-guides-implement-metronome-core-concepts-packages-overview]]

## Raw Sources

- [[raw/metronome/guides/pricing-packaging/billing-model-guides/token-billing-2026-08-28|2026-08-28 snapshot - private-preview managed token pricing, markup and custom-unit setup, package provisioning, token-event tracking, and model-update boundary]]
