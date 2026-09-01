---
title: "Metronome API Reference: Create a Credit Grant"
type: source
date_ingested: 2026-09-01
original_format: webpage
canonical_url: "https://docs.metronome.com/api-reference/credit-grants/create-a-credit-grant"
raw_files:
  - "metronome/api-reference/credit-grants/create-a-credit-grant-2026-07-13.md"
tags: [metronome, api, credit-grants, plans, contracts, idempotency]
---

## Overview

This reference documents bearer-authenticated `POST /v1/credits/createGrant`, which creates a customer credit grant on Metronome's deprecated Plans surface. Metronome directs new clients to Contracts, but this page does not identify a replacement operation or define a Plan-grant-to-Contract-credit mapping.

## Key takeaways

- Within a supplied JSON payload, `customer_id`, `grant_amount`, `name`, `expires_at`, `paid_amount`, and `priority` are required. Both amount objects require a numeric `amount` and pricing-unit `credit_type_id`; despite their property descriptions saying the pricing unit defaults to USD cents when not passed, the schema still marks each nested `credit_type_id` required. The enclosing `requestBody` is not marked required, and top-level `additionalProperties` behavior is unspecified, so omitted-body and unknown-field behavior remain undocumented.
- `effective_at` makes the grant apply only to usage or charges dated on or after that timestamp, while required `expires_at` is exclusive. Optional `product_ids` narrows applicability; omission applies the credits to charges for all products, and array order controls application order across invoice line items. The page does not define priority ordering, timestamp validation, empty-product-array behavior, or balance and ledger propagation timing.
- `name` is described as appearing on invoices. Optional `invoice_date` schedules an invoice for `paid_amount`, but the page does not establish invoice state, delivery, collection, payment, tax, accounting, refund, or downstream-provider effects.
- Optional `uniqueness_key` is 1-128 characters and rejects reuse with HTTP `409` without creating a new record. Optional rollover settings are opt-in beta and can cap rollover by a 0-1 fraction or a fixed amount; the page does not define rollover execution timing, source-grant state, atomicity, recovery, or visibility.
- HTTP `200` requires top-level `data`, whose referenced object requires UUID `id`. No other endpoint response, error catalog, read-after-write guarantee, concurrency ordering, partial-failure recovery, or current grant/balance/invoice state is documented.

## Retry, migration, and authority boundaries

The separate API-wide authority says all POST endpoints accept `Idempotency-Key`. Only after a request begins execution—after validation and without a pre-execution concurrent-request conflict—is its result persisted; identical same-key parameters replay that original result, changed parameters return HTTP `409`, keys remain for at least 24 hours, and HTTP `500` results can be cached. This request-result replay is distinct from the endpoint's resource-level `uniqueness_key` and must not be treated as a fresh grant, balance, ledger, invoice, or propagation read. The endpoint adds no guarantee for another or expired key, concurrent mutations, recovery after an ambiguous failure, or migration to Contracts.

## Raw-detail coverage map

The exact raw page preserves the complete request example; required and optional payload properties; customer, amount, pricing-unit, display, timing, priority, reason, type, product, rollover, and custom-field schemas; the `data.id` response placement; uniqueness-key bounds and conflict text; rollover beta annotation, variants, enums, and numeric bounds; server, bearer-security, tag descriptions, and OpenAPI component definitions. Use the linked API-wide idempotency source for execution-admission, replay, retention, cached-error, and retry guidance; use current Contract authorities for Contract credit creation or editing rather than inferring a replacement from this deprecated page.

## Related

- Company: [[metronome]]
- Primary concepts: [[metronome-credits-and-commits]], [[metronome-customers-and-contracts]], [[metronome-products-and-rate-cards]], [[metronome-api-idempotency]]
- Supporting concepts: [[metronome-currencies-and-custom-pricing-units]], [[metronome-invoicing]]
- Related source: [[source-metronome-api-reference-idempotency]]

## Raw Sources

- [[raw/metronome/api-reference/credit-grants/create-a-credit-grant-2026-07-13|2026-07-13 snapshot - complete deprecated Plans credit-grant creation request, response, applicability, uniqueness, and rollover schema]]
