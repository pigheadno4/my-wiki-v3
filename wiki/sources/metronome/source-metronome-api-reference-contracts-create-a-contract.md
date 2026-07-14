---
title: "Metronome API: Create a Contract"
type: source
date_ingested: 2026-07-14
canonical_url: "https://docs.metronome.com/api-reference/contracts/create-a-contract"
original_format: webpage
raw_files:
  - "metronome/api-reference/contracts/create-a-contract-2026-07-13.md"
tags: [metronome, api, contracts, commits, subscriptions]
---

## Overview

`POST /v1/contracts/create` creates the billing agreement that connects a customer to products, pricing, discounts, access periods, and billing configuration. The OpenAPI request has only two unconditionally required top-level fields—`customer_id` and inclusive `starting_at`—but exposes many optional, nested component families. Use the retained raw reference for exact schemas, enums, conditional requirements, and response objects.

## Endpoint contract

| Item | Documented value |
| --- | --- |
| Method and path | `POST /v1/contracts/create` |
| Operation ID | `createContract-v1` |
| Required top-level request fields | `customer_id`, `starting_at` |
| Contract end | Optional `ending_before`, exclusive |
| Success | `200`, with `data` containing a `CreateContractResponse` |
| Listed error responses | `400` bad request and `404` not found |

The `uniqueness_key` component separately says that reusing a key prevents creation and fails with `409`; that status is not included in the operation response block, so clients should not treat the response list as exhaustive for duplicate protection.

## Request-family map

| Family | Purpose and important boundary |
| --- | --- |
| Package or rate card | Select a package, rate-card ID, or time-resolved alias. `package_id` permits only customer/start/package/uniqueness/transition/custom-field inputs and is mutually exclusive with `package_alias`. |
| Term and statements | Define inclusive start, exclusive end, statement frequency/anchor, and optional deferred invoice generation for historical imports. |
| Commits and credits | Model prepaid/postpaid obligations or allowances with schedules, applicability, priority, rollover, and optional recurrence. Nested required fields vary by type. |
| Overrides | Apply effective-dated overwrite, multiplier, or tiered behavior to products, tags, or specifiers; targeting modes are mutually constrained. |
| Charges and subscriptions | Add scheduled charges or recurring subscription charges. Subscription quantity requirements depend on quantity-management mode. |
| Routing and hierarchy | Route concurrent-contract usage with `usage_filter` and configure parent/child payer and invoice-consolidation behavior. |
| Billing controls | Select billing/revenue integrations, spend thresholds, prepaid-balance thresholds, and spend trackers where enabled. |

Some request fields are explicitly gated by client configuration or feature flags. Their presence in the schema does not prove availability for every account.

## Important conditional rules

### Commits, credits, and applicability

A commit requires `type` and `product_id`; its access/invoice schedule rules differ for prepaid and postpaid forms. A credit requires `product_id` and `access_schedule`. Product IDs/tags and boolean-style specifiers scope balance drawdown, but specifiers cannot be combined with the product-ID/tag applicability fields. Rollover fractions must be between 0 and 1.

### Usage statement schedule

The schedule input requires frequency and supports monthly, quarterly, annual, and weekly values. The day defaults to the first of the month when omitted; a custom date requires `billing_anchor_date`. `invoice_generation_starting_at` can defer automatic usage invoices when historical invoices will be imported separately.

### Subscriptions

Each subscription requires `subscription_rate`, `collection_schedule`, and `proration`. The subscription rate itself requires billing frequency and a subscription-product ID that matches an existing rate-card rate. Quantity-only mode requires nonnegative `initial_quantity`; seat-based mode requires `seat_config` and uses event/group-key-compatible seat identifiers. Billing-cycle configuration can anchor the cycle and place charges on usage or scheduled invoices.

### Scheduled-charge consolidation

`scheduled_charges_on_usage_invoices: ALL` consolidates eligible scheduled and commit charges when their timestamp matches the usage invoice end. The schema states that this setting cannot be modified after contract creation.

### Thresholds and hierarchy

Spend and prepaid-balance threshold configurations have their own required enablement, amount, commit, and payment-gate fields. Hierarchy inputs can select the payer and whether child statements consolidate or remain separate; exact parent/child requirements live in the nested schemas.

The descriptive prose calls the prepaid trigger `prepaid_balance_configuration`, while `CreateContractPayload` names the field `prepaid_balance_threshold_configuration`. This source follows the request schema name.

## Lifecycle and scope

The prose points to separate edit and edit-history endpoints after creation and says customers may have concurrent contracts routed by usage filters. This page does not define those endpoints' request/response contracts. Likewise, its large response schema and ledger unions are reference material, not evidence that every optional request family is required or available to every client.

## Change history

- 2026-07-14: Initial ingest from the 2026-07-13 collection snapshot; Sol added package restrictions, feature-gating, conditional subscription rules, response-list caveat, immutable consolidation behavior, and an explicit prose/schema naming caveat.

## Related

- Company: [[metronome]]
- Concept: [[metronome-customers-and-contracts]]
- Related concepts: [[metronome-products-and-rate-cards]], [[metronome-usage-based-billing]], [[metronome-invoicing]]

## Raw Sources

- [[raw/metronome/api-reference/contracts/create-a-contract-2026-07-13|2026-07-13 snapshot - complete request, response, nested schemas, and examples]]
