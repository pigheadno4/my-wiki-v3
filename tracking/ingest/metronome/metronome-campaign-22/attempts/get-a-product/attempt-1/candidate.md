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

This API reference documents the bearer-authenticated `POST /v1/contract-pricing/products/get` read on `https://api.metronome.com`. It accepts a product UUID in a JSON payload and returns one product under a required `data` envelope, including required initial, current, and update-history surfaces. It is useful for catalog configuration and history queries, but it does not create, edit, archive, price, or associate a product with a contract.

## Request and requiredness

The operation's `requestBody` defines `application/json` content referencing `Id`, but the enclosing body is not marked `required: true`. Inside `Id`, `id` is required and formatted as a UUID. Omitted-body runtime behavior is therefore undocumented; the schema also does not set top-level `additionalProperties`, so this page does not establish unknown-field handling.

The route contains no path parameter, and the operation defines no query parameter. The page does not document endpoint-specific token scopes, field-level permissions, rate limits, request caching, or validation-error mapping.

## Success envelope and product identity

HTTP `200` requires top-level `data`. The referenced `ProductListItem` requires UUID `id`, string `type`, `initial`, `current`, and an `updates` array. Its type enum is `USAGE`, `SUBSCRIPTION`, `COMPOSITE`, `FIXED`, or `PRO_SERVICE`; this page does not define the behavior of any type, and `PRO_SERVICE` should not inherit semantics from the four types explained by the separate product guide.

`archived_at` is optional, nullable, and date-time formatted. The endpoint provides no description for the field, so its presence, null value, or omission does not establish archive timing, retrievability rules, restoration support, retention, or effects on historical invoices and contracts.

## Configuration and history surface

The operation description says the result includes all metadata and historical changes, and the response requires `initial`, `current`, and `updates`. The page does not define update ordering, completeness, version identity, effective-time selection, whether future-effective changes can appear as current, whether archive events belong in `updates`, or freshness and read-after-write guarantees. Treat the three surfaces as the documented representation, not as a replayable audit log contract.

Each `ProductListItemUpdate` requires only `created_at` and `created_by` in its own schema. Optional fields shown in the selected portion include `name`, `starting_at`, UUID-formatted `billable_metric_id`, `quantity_conversion`, and `quantity_rounding`. The endpoint does not define whether omitted update properties mean unchanged, cleared, unavailable, or redacted values.

For usage products, `quantity_conversion` is nullable; a non-null object requires numeric `conversion_factor` and an `operation` from the explicitly enumerated lower- or uppercase multiply/divide values. The page supplies no minimum, non-zero rule, precision, overflow, or general case-normalization contract for the factor or operation. `quantity_rounding` is likewise nullable and usage-only; a non-null object requires a listed lower- or uppercase rounding method plus numeric `decimal_places` with minimum zero, while maximum precision and runtime validation errors remain unspecified.

The reusable pricing- and presentation-group-key schemas are string arrays for usage products. A pricing group key determines pricing per key value, whereas a presentation group key groups usage line items on invoices. Both descriptions require the superset of pricing and presentation values to be configured as one compound group key on the billable metric; this read does not return or validate that metric's group-key definition.

## Custom fields and errors

`ProductListItem.custom_fields` is optional and references an object with arbitrary property names whose values are strings; the field is annotated for entity `contract_product`. This endpoint establishes only that response shape. The separate custom-fields authority owns persistence, configured-key, uniqueness, export, and invoice-propagation behavior; this page adds no key or value limits, ordering, redaction, permission, availability, or freshness rules.

The only operation-specific non-success response documented is HTTP `404`, using the shared not-found response whose JSON `Error` requires a string `message`. The page does not distinguish an unknown product from an archived, unauthorized, or otherwise invisible product and does not document `400`, `401`, `403`, `409`, `429`, or `5xx` behavior.

## POST-read idempotency boundary

This endpoint page does not mention `Idempotency-Key` or define endpoint-specific retry, concurrency, cached-error, or recovery behavior. Because the read uses POST, the separate [[source-metronome-api-reference-idempotency|API-wide idempotency authority]] remains the source for same-key result replay and conflict behavior. A replayed result from that separate contract must not be treated as proof of a fresh product read.

## Related

- Company: [[metronome]]
- Concepts: [[metronome-products-and-rate-cards]], [[metronome-billable-metrics]], [[metronome-custom-fields]], [[metronome-api-idempotency]]
- Product semantics: [[source-metronome-guides-implement-metronome-core-concepts-create-products-contracts]]
- API convention: [[source-metronome-api-reference-idempotency]]

## Raw Sources

- [[raw/metronome/api-reference/products/get-a-product-2026-07-13|2026-07-13 snapshot - single-product retrieval, history envelope, usage configuration, custom fields, and read boundaries]]
