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

This reference documents bearer-authenticated `POST /v1/credits/createGrant`, which creates a customer credit grant on Metronome's deprecated Plans surface. Metronome directs new clients to Contracts but does not identify a one-to-one replacement. Current authorities separately document customer-level `POST /v1/contracts/customerCredits/create` and recommend contract create or edit for most credits; the current contract operations are `POST /v1/contracts/create` and `POST /v2/contracts/edit`.

## Key takeaways

- Within a supplied JSON payload, `customer_id`, `grant_amount`, `name`, `expires_at`, `paid_amount`, and `priority` are required. Both amount objects require numeric `amount` and pricing-unit `credit_type_id`; despite their property descriptions saying the pricing unit defaults to USD cents when not passed, each nested schema marks `credit_type_id` required. The enclosing `requestBody` is not marked required, and top-level `additionalProperties` behavior is unspecified, so omitted-body and unknown-field behavior remain undocumented.
- `effective_at` makes the grant apply only to usage or charges dated on or after that timestamp, while required `expires_at` is exclusive. Optional `product_ids` narrows applicability; omission applies credits to charges for all products, and supplied array order controls application across invoice line items. The required numeric `priority` has no ordering explanation here. These legacy rules must not be imported as the current Contract balance or invoice-line ordering algorithm: the dedicated prioritization authority orders current balances by balance type and additional tie-breakers, and orders eligible invoice lines by product type, start date, unit price, and name.
- `name` is described as appearing on invoices. Optional `invoice_date` is the date to issue an invoice for `paid_amount`, but the page does not establish invoice state, line placement beyond its legacy `product_ids` statement, finalization, delivery, collection, payment, tax, accounting, refund, downstream-provider effects, or propagation timing.
- Optional `uniqueness_key` is 1-128 characters and rejects reuse with HTTP `409` without creating a new record. The separate legacy void-grant authority documents `release_uniqueness_key: true` as resetting this grant key for reuse, qualifying the API-wide page's statement that release is available only for Alerts; release timing, concurrency, visibility, rollback, and interaction with the request-header key remain undefined. Optional rollover settings are opt-in beta and can cap a successor grant by a 0-1 fraction or a fixed amount, without defining execution timing, source-grant state, atomicity, recovery, or visibility.
- HTTP `200` requires top-level `data`, whose referenced object requires UUID `id`. No other endpoint response, error catalog, read-after-write guarantee, concurrency ordering, partial-failure recovery, or current grant, balance, ledger, or invoice state is documented.

## Current Contracts route and migration boundary

The independently documented current customer-level route is `POST /v1/contracts/customerCredits/create`, which can scope a credit across selected or all customer contracts; its authority recommends `POST /v1/contracts/create` or `POST /v2/contracts/edit` for most credits. Those current sources use different request models and applicability and prioritization semantics. Neither they nor this deprecated page establish a one-to-one replacement for `POST /v1/credits/createGrant`, a grant-to-credit or grant-to-contract identity mapping, a field mapping, a migration procedure, compatibility period, or removal date.

## Retry, uniqueness, and failure boundaries

The API-wide authority says all POST endpoints accept `Idempotency-Key`. A result is persisted only after the request begins execution, meaning validation passed and no pre-execution concurrent-request conflict prevented execution; identical same-key parameters then replay the original result, changed parameters return HTTP `409`, and retention is at least 24 hours. An admitted HTTP `500` can be cached and replayed again under the same key. Metronome recommends investigating system state and deciding whether to resolve manually or retry, while the separate status-code page advises checking for partial creation after `5XX` and then retrying with a different key. Those instructions are in tension and do not make another key universally safe. Request-result replay is distinct from the endpoint's resource-level `uniqueness_key` and is not a fresh grant, balance, ledger, invoice, or propagation read; the endpoint adds no safe recovery sequence for another, absent, or expired header key, concurrent mutations, or an ambiguous failure.

## Raw-detail coverage map

The exact raw page preserves the complete request example; request-body wrapper; required and optional payload properties; customer, granted and paid amount, pricing-unit, display, timing, priority, reason, type, product, rollover, and custom-field schemas; the `data.id` response placement; uniqueness-key bounds and conflict text; rollover beta annotation, variants, enums, and numeric bounds; server, bearer-security, tag descriptions, and OpenAPI component definitions. Use the linked current credit and contract sources for current routes, the prioritization source for current balance and invoice-line ordering, the void-grant source for grant-key release, and the API-wide idempotency and status-code sources for admitted-result replay and failure guidance; none of those sources turns this deprecated schema into a current Contract mapping.

## Related

- Company: [[metronome]]
- Primary concepts: [[metronome-credits-and-commits]], [[metronome-customers-and-contracts]], [[metronome-products-and-rate-cards]], [[metronome-currencies-and-custom-pricing-units]], [[metronome-invoicing]], [[metronome-api-idempotency]]
- Current credit and contract sources: [[source-metronome-api-reference-credits-and-commits-create-a-credit]], [[source-metronome-api-reference-contracts-create-a-contract]], [[source-metronome-api-reference-contracts-edit-a-contract]]
- Ordering and lifecycle sources: [[source-metronome-guides-pricing-packaging-apply-credits-and-commits-prioritization-rules]], [[source-metronome-api-reference-credit-grants-void-a-credit-grant]]
- Retry sources: [[source-metronome-api-reference-idempotency]], [[source-metronome-api-reference-status-codes]]

## Raw Sources

- [[raw/metronome/api-reference/credit-grants/create-a-credit-grant-2026-07-13|2026-07-13 snapshot - complete deprecated Plans credit-grant creation request, response, applicability, uniqueness, and rollover schema]]
