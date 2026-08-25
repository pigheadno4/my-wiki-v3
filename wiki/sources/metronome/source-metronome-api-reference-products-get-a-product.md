---
title: "Metronome Get a Product API"
type: source
date_ingested: 2026-08-25
original_format: webpage
canonical_url: "https://docs.metronome.com/api-reference/products/get-a-product.md"
raw_files:
  - "metronome/api-reference/products/get-a-product-2026-07-13.md"
tags: [metronome, api, products, product-history, usage-based-billing]
---

## Overview

This API reference documents the globally bearer-secured `POST /v1/contract-pricing/products/get` operation on `https://api.metronome.com`. It retrieves one product by ID and returns required identity, type, initial state, current state, and update-history surfaces under a required `data` envelope. It is a read contract; the page does not create, edit, archive, price, or associate a product with a contract.

## Request and requiredness

The operation's `requestBody` defines `application/json` content referencing `Id`, but the enclosing body is not marked `required: true`. Inside `Id`, `id` is required and formatted as a UUID. Omitted-body runtime behavior is therefore undocumented. The `Id` schema also does not specify `additionalProperties`, so this page does not establish unknown-field handling.

The route contains no path parameter, and the operation defines no query parameter. The page does not document endpoint-specific token scopes, field-level permissions, rate limits, request caching, or validation-error mapping.

## Success envelope and product identity

HTTP `200` requires top-level `data`. The referenced `ProductListItem` requires UUID `id`, string `type`, `initial`, `current`, and an `updates` array. Its type enum is `USAGE`, `SUBSCRIPTION`, `COMPOSITE`, `FIXED`, or `PRO_SERVICE`; this endpoint does not define the behavior of any type. The separate product guide explains four types but not `PRO_SERVICE`, so its semantics must not be inferred here.

`archived_at` is optional, nullable, and date-time formatted. The endpoint provides no description for the field, so presence, null, or omission does not establish archive timing, retrievability, restoration, retention, or historical invoice and contract effects.

## Initial, current, and update state

Both required `initial` and `current` reference `ProductListItemState`. That state requires `name`, date-time `created_at`, and string `created_by`; other fields are optional in the schema. In particular, state `billable_metric_id` is only typed as a string, whereas `ProductListItemUpdate.billable_metric_id` is a UUID-formatted string. The state can also expose optional `starting_at`, quantity conversion and rounding, composite and general tags, pricing and presentation group keys, `exclude_free_usage`, and a configuration-dependent `is_refundable`. Their presence does not establish validation, applicability to every product type, or availability for every client.

Each `ProductListItemUpdate` requires only date-time `created_at` and string `created_by`; its other fields are optional. The page does not say whether omitted update properties mean unchanged, cleared, unavailable, or redacted. Although the description says the product includes all metadata and historical changes, the endpoint does not define update ordering, completeness, version identity, effective-time selection, future-effective visibility, archive-event representation, freshness, or read-after-write behavior. Treat `initial`, `current`, and `updates` as the documented representation, not a replayable audit-log guarantee.

## Composite-product state

State can expose optional UUID-array `composite_product_ids` and string-array `composite_tags`. The state-only `composite_scope` is a feature-gated selector with values `CUSTOMER` or `CONTRACT`, described as determining what spend contributes to the charge. `include_composite_spend` is also feature-gated, applies only to composite products, defaults to false, and when true permits spend from other composite products; it appears on state and update schemas. The page does not define validation, recursion, cycle handling, precedence, calculation order, historical replay, or general availability for these fields.

## Usage configuration and billable-metric boundary

For usage products, `quantity_conversion` is nullable; when non-null it requires numeric `conversion_factor` and an operation from the explicitly enumerated lower- or uppercase multiply/divide values. The page supplies no minimum, non-zero rule, precision, overflow, or general case-normalization contract. `quantity_rounding` is likewise nullable and usage-only; when non-null it requires a listed lower- or uppercase rounding method plus numeric `decimal_places` with minimum zero, while maximum precision and runtime validation errors remain unspecified.

The reusable pricing- and presentation-group-key schemas are string arrays for usage products. A pricing group key determines pricing per key value, while a presentation group key groups usage invoice lines. Both descriptions require the superset of pricing and presentation values to be configured as one compound group key on the billable metric. This product read does not return or validate the metric definition, and the unformatted state `billable_metric_id` must not be silently normalized to the update schema's UUID format.

## NetSuite and custom-field boundaries

Both state and update schemas can expose `netsuite_internal_item_id` and `netsuite_overage_item_id` as strings whose availability depends on the client's configuration. Their presence does not establish mapping correctness, integration readiness, synchronization, delivery, accounting, or reconciliation behavior.

`ProductListItem.custom_fields` is optional and references an object with arbitrary property names whose values are strings; the field carries `x-cf-entity: contract_product`. This endpoint establishes only that response shape. The separate [[source-metronome-api-reference-custom-fields|custom-fields authority]] establishes configured entity scope, persistence, uniqueness, export visibility, and Product-to-invoice-line propagation. Its Product terminology is not reconciled here with this endpoint's `contract_product` annotation. This read adds no key or value limits, ordering, redaction, permissions, availability, or freshness rules.

## Errors and POST-read idempotency boundary

The only operation-specific non-success response documented is HTTP `404`, using the shared not-found response whose JSON `Error` requires a string `message`. The page does not distinguish an unknown product from an archived, unauthorized, or otherwise invisible product and does not document `400`, `401`, `403`, `409`, `429`, or `5xx` behavior.

This endpoint page does not mention `Idempotency-Key` or define endpoint-specific retry, concurrency, cache, freshness, or recovery behavior. Because the read uses POST, the separate [[source-metronome-api-reference-idempotency|API-wide idempotency authority]] remains authoritative: it documents identical-parameter same-key replay, changed-parameter conflict, at-least-24-hour retention, and cached errors. Those guarantees are not established by this endpoint raw. Returning the original keyed result is not evidence of a fresh product read.

## Related

- Company: [[metronome]]
- Concepts: [[metronome-products-and-rate-cards]], [[metronome-billable-metrics]], [[metronome-custom-fields]], [[metronome-integrations]], [[metronome-api-idempotency]]
- Product semantics: [[source-metronome-guides-implement-metronome-core-concepts-create-products-contracts]]
- Custom-field authority: [[source-metronome-api-reference-custom-fields]]
- API-wide idempotency authority: [[source-metronome-api-reference-idempotency]]

## Raw Sources

- [[raw/metronome/api-reference/products/get-a-product-2026-07-13|2026-07-13 snapshot - single-product retrieval, full state and update schemas, composite and usage configuration, integration fields, custom fields, and read boundaries]]
