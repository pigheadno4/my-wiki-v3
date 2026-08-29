---
title: "Create a credit"
type: source
date_ingested: 2026-08-29
original_format: webpage
canonical_url: "https://docs.metronome.com/api-reference/credits-and-commits/create-a-credit"
raw_files:
  - "metronome/api-reference/credits-and-commits/create-a-credit-2026-08-28.md"
  - "metronome/api-reference/credits-and-commits/create-a-credit-2026-07-13.md"
tags: [metronome, credits-and-commits, customer-credits, api]
---

## Overview

This API reference documents bearer-authenticated `POST /v1/contracts/customerCredits/create`, which creates a customer-level spending allowance or free credit balance for use across all or selected customer contracts. Metronome recommends contract create or edit for most credits and positions this endpoint for customer-level, cross-contract use. It returns the created resource's UUID but does not establish balance visibility, invoice correction, refund, external accounts-receivable, or accounting effects.

## Query-critical facts

- The enclosing OpenAPI `requestBody` is not marked required. Within a supplied `CreateCustomerCreditPayload`, `customer_id`, `priority`, `product_id`, and `access_schedule` are required; this does not establish omitted-body runtime behavior. The payload and its schedule, specifier, and exclusion objects do not declare `additionalProperties`, so unknown-field behavior remains undocumented; only the pricing-group, presentation-group, and `custom_fields` maps explicitly allow arbitrary string-valued properties.
- `access_schedule` requires `schedule_items`, and each item requires numeric `amount`, inclusive RFC 3339 `starting_at`, and exclusive RFC 3339 `ending_before`. Optional, feature-gated `access_type` makes `SPEND` deduct the dollar cost of usage and `QUANTITY` deduct the number of units used, defaulting to `SPEND` when omitted; the schema also marks it `x-stainless-skip: true`, so this page does not establish generated-client exposure. Optional `credit_type_id` independently defaults to USD cents. The page defines no `minItems`, amount bounds, precision, or rounding; schedule ordering or overlap; non-USD or custom-unit compatibility; quantity denomination; conversion; mixed-mode priority; or invoice and ledger representation.
- `applicable_contract_ids` scopes the credit to selected contracts; omission applies it to all contracts, while the prose also calls an empty value cross-contract. The UUID `product_id` is required even when eligible usage is unrestricted.
- Eligible usage can use direct product IDs or tags, or `specifiers`; the direct selectors cannot be combined with `specifiers`. The direct-selector descriptions say omitting both means all products, while `specifiers` are permitted only in that same absence and require at least one matching condition. The page does not reconcile those statements. A specifier can require one product, all listed tags, and string-valued group maps; it is excluded when its inclusion criteria and any exclusion entry match, with all tags inside that entry required.
- Lower numeric priority is consumed first, and equal-priority contract-level credits or commits precede customer-level ones. This is endpoint-local guidance, not a complete ordering algorithm; it does not override the dedicated priority authority's rollover, balance-type, applicability, cost-basis, and schedule tie-breakers.
- HTTP `200` requires `data.id`, a UUID identifying the created resource. The operation lists generic `400` and `404` error objects requiring only `message`; separately, optional 1-128 character `uniqueness_key` prevents another credit or commit from being created with a used key and documents HTTP `409`, which is absent from the operation response map.

## Identity, lifecycle, and retry boundaries

The endpoint's `uniqueness_key` is a resource-creation identity guard, not request-result replay. The separate API-wide [[source-metronome-api-reference-idempotency|idempotency authority]] applies `Idempotency-Key` to all POST endpoints: identical same-key parameters replay the original result, changed parameters return `409`, retention is at least 24 hours, and a cached result can be `500`. Neither authority defines the two keys' interaction or precedence, customer-credit uniqueness-key scope or release, failed-attempt consumption, concurrent creation, expired- or different-header-key behavior, or recovery after an ambiguous or cached failure.

The operation creates a customer credit and returns its UUID. It does not define initial ledger state, read-after-write visibility, update, archive, deletion, reversal, expiry processing, notification or webhook delivery, invoice finalization effects, downstream-provider propagation, refunds, tax, payment, settlement, external A/R, revenue recognition, partial failure, or transaction boundaries. Optional `name` is described as displayed on invoices, while `description` is UI/API-only and not exposed to end customers; no artifact, state, or propagation guarantee follows.

> [!warning] Documentation ambiguities
> The page's new warning says this credit endpoint should be used only for cross-contract or enterprise-wide **commits**, while the operation, payload, and response create a credit; it does not establish that the endpoint creates commits. Separately, the direct-selector all-products wording conflicts with the permitted `specifiers` path and remains unresolved.

## Raw-detail coverage map

| Raw detail category | Exact raw coverage |
| --- | --- |
| Purpose and scope | Customer-level onboarding, allowance, migration, selected-contract and cross-contract use cases; preferred contract create/edit alternative; priority and finance guidance |
| Request and success envelopes | Bearer scheme, operation path, request example, request-body wrapper, payload required list, HTTP `200` data envelope and UUID ID |
| Access and applicability | Complete access-schedule, spend/quantity mode, credit-type, contract selector, direct product selector, specifier, group-map, and exclusion schemas |
| Optional metadata and integration fields | Invoice name, UI/API description, NetSuite and Salesforce IDs, contract-credit custom fields, rate type, and exact field annotations |
| Errors and identity | Generic `400`/`404` schemas, uniqueness-key length and duplicate-creation `409`, and the omission of that `409` from the response map |

## Related

- Company: [[metronome]]
- Primary concepts: [[metronome-credits-and-commits]], [[metronome-customers-and-contracts]], [[metronome-products-and-rate-cards]], [[metronome-api-idempotency]]
- Secondary concepts: [[metronome-currencies-and-custom-pricing-units]], [[metronome-custom-fields]], [[metronome-invoicing]]
- Related sources: [[source-metronome-guides-pricing-packaging-apply-credits-and-commits-prioritization-rules]], [[source-metronome-api-reference-contracts-create-a-contract]], [[source-metronome-api-reference-contracts-edit-a-contract]], [[source-metronome-api-reference-idempotency]], [[source-metronome-api-reference-status-codes]]

## Raw Sources

- [[raw/metronome/api-reference/credits-and-commits/create-a-credit-2026-08-28|2026-08-28 snapshot - customer-credit purpose, spend-or-quantity access mode, required payload, applicability, identity, response, and errors]]
- [[raw/metronome/api-reference/credits-and-commits/create-a-credit-2026-07-13|2026-07-13 snapshot - prior customer-credit creation, schedule, applicability, priority, response, and error schema]]
