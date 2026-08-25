---
title: "Metronome API Reference: List Products"
type: source
date_ingested: 2026-08-25
original_format: webpage
canonical_url: "https://docs.metronome.com/api-reference/products/list-products.md"
raw_files:
  - "metronome/api-reference/products/list-products-2026-07-13.md"
tags: [metronome, products, api-reference, pagination, product-configuration]
---

## Overview

This API reference documents the bearer-authenticated `POST /v1/contract-pricing/products/list` endpoint for retrieving a paginated organization-wide product catalog. The assigned page is the authority for this list operation's archive filter, cursor envelope, returned product identity and version-state shapes, and optional product configuration; separate pagination and idempotency sources remain authoritative for API-wide continuation and replay behavior.

## Key takeaways

- The endpoint excludes archived products by default. Its optional JSON `archive_filter` accepts `ARCHIVED`, `NOT_ARCHIVED`, or `ALL`; the enclosing `requestBody` is not marked required and the payload schema requires no property.
- Optional query parameters are integer `limit` from `1` through `100` and string `next_page`. HTTP `200` requires a `data` array and a nullable string `next_page`; the separate API-wide pagination authority defines `null` as the terminal cursor.
- Every returned product item requires UUID `id`, `type`, `initial`, `current`, and `updates`. `archived_at` and `custom_fields` are optional. The endpoint says results include complete version history, but it defines neither array-item ordering nor version chronology.
- The returned `type` enum contains `USAGE`, `SUBSCRIPTION`, `COMPOSITE`, `FIXED`, and `PRO_SERVICE`. `PRO_SERVICE` conflicts with the existing product guide's claim that Metronome has four product types and must not be silently omitted or generalized.
- Product states can expose metric, composite, quantity-conversion, rounding, tag, group-key, NetSuite, and feature-gated composite fields. Their presence in a list response does not establish creation, editing, archival, invoice recalculation, or downstream propagation behavior.

## Endpoint contract

| Item | Documented value |
| --- | --- |
| Method and path | `POST /v1/contract-pricing/products/list` |
| Operation ID | `listProducts-v1` |
| Authentication | Top-level HTTP bearer authentication through `bearerAuth` |
| Query inputs | Optional `limit` (`1` to `100`) and optional string `next_page` |
| JSON payload | Optional `archive_filter`: `ARCHIVED`, `NOT_ARCHIVED`, or `ALL`; omission defaults to not archived |
| Success | HTTP `200` with required `data` and required nullable `next_page` |
| Listed endpoint errors | None |

The endpoint defines no path parameter. Bearer authentication is explicit, but this page does not document endpoint-specific token scope, role, permissions, or authorization-failure behavior.

## Request and archive filtering

The operation's `requestBody` contains an `application/json` schema reference and an example, but has no `required: true`. `ListProductsPayload` is an object with no required-property list; its only documented property is `archive_filter`. These are separate boundaries: the page does not establish runtime treatment of a completely omitted body, an empty object, explicit `null`, or an unknown property because neither the wrapper nor payload declares those behaviors and `additionalProperties` is unspecified.

`archive_filter` accepts exactly the three documented enum values. The page says omission defaults to not archived, but does not define whether filtering is evaluated before pagination, how an existing cursor is bound to the filter, how concurrent archival affects traversal, or whether a product archived during traversal can be skipped or repeated.

## Pagination and response envelope

`limit` is optional and accepts integers from `1` through `100`; the page states no default. `next_page` is an optional string cursor indicating where the next page begins. A successful response requires both `data` and `next_page`; `data` is an array of `ProductListItem`, and `next_page` is nullable. The assigned page does not itself define the terminal-cursor rule; the separate [[source-metronome-api-reference-pagination|API-wide pagination source]] says traversal ends when `next_page` is `null`.

Neither source defines this endpoint's result order, cursor lifetime, snapshot consistency, cursor reuse across filter changes, malformed-cursor response, or duplicate and skipped-item behavior while products are edited or archived. The claim that results carry complete configuration and version history does not make every optional field required or establish consistency across a multi-page traversal.

## Product identity, type, and version representations

Each item requires UUID `id`; enum `type`; `initial` and `current` state objects; and an `updates` array. Optional nullable `archived_at` is a date-time, but this page defines no active-state marker, archive reason, restoration behavior, historical visibility guarantee, or relationship between archival and the version arrays. Optional `custom_fields` is a product-entity map described below.

Both `initial` and `current` use `ProductListItemState`, which requires string `name`, date-time `created_at`, and string `created_by`; `starting_at` is optional. Each `ProductListItemUpdate` requires only date-time `created_at` and string `created_by`; its `name`, `starting_at`, and other configuration fields are optional. The endpoint description says the list returns complete version history. It does not define update ordering, the retention horizon encompassed by that claim, whether future-scheduled entries appear or how they should be interpreted, how `current` is selected, whether omitted update fields inherit prior values, the meaning of repeated values, or cross-page consistency while an edit is accepted during pagination. The example shows an updated current name and an update with a later `starting_at`, but does not establish a general chronology rule.

> [!warning] Product-type contradiction
> This response schema includes five product types and adds `PRO_SERVICE`. The existing [[source-metronome-guides-implement-metronome-core-concepts-create-products-contracts|Create Products guide]] and [[metronome-products-and-rate-cards]] concept enumerate only usage, fixed, composite, and subscription products. The sources do not explain whether `PRO_SERVICE` is newly supported, API-only, feature-gated, legacy, or unavailable for creation, so preserve the source-scoped mismatch and verify current creation support before implementation.

## Returned configuration boundaries

State and update entries can expose `billable_metric_id`, composite product IDs and tags, tags, quantity conversion and rounding, pricing and presentation group keys, NetSuite item IDs, `is_refundable`, `exclude_free_usage`, and `include_composite_spend`. The `netsuite_internal_item_id` and `netsuite_overage_item_id` fields state that their availability depends on the client configuration; this page does not define mapping semantics, external-item validation, freshness, propagation, synchronization, invoice delivery, or reconciliation. Initial/current states can also expose `composite_scope` as `CUSTOMER` or `CONTRACT`; that field and `include_composite_spend` carry feature annotations and SDK-skip metadata. Their appearance in the schema does not prove general tenant availability, mutability, invoice effects, or create-request acceptance.

The initial/current state's `billable_metric_id` is a string without a UUID format annotation, while the update schema annotates the same-named field as UUID. This schema difference does not prove that the runtime identifiers have different formats. Composite-product ID arrays are UUID-formatted; the page gives no minimum size, duplicate rule, cycle rule, existence check, or behavior for archived referenced products.

`quantity_conversion` is nullable and described as optional and valid only for usage products. When an object is supplied, it requires numeric `conversion_factor` and enum `operation`, which accepts lower- and uppercase multiply or divide spellings; optional `name` is a string. The schema gives no positive, nonzero, precision, or maximum constraint for the factor and does not promise general case normalization.

`quantity_rounding` is likewise nullable, optional, and usage-only. When supplied, it requires `rounding_method` and numeric `decimal_places`; the method enum admits lower- and uppercase round-up, round-down, and round-half-up spellings, and decimal places has minimum `0` but no integer or upper-bound constraint. The endpoint does not define ordering when both conversion and rounding are present.

Pricing and presentation group keys are arrays of strings documented only for usage products. The pricing key selects pricing per key value, while the presentation key groups usage line items on invoices; the combined set of both must exist as one compound group key on the billable metric. The page does not define array non-emptiness, duplicates, ordering, missing event dimensions, metric validation errors, cardinality, or rate fallback. Those product-side response facts complement rather than replace the metric-design authorities.

## Custom fields

Optional product `custom_fields` references an object explicitly permitting arbitrary property names with string values and is annotated as the `contract_product` entity. The response schema does not define key or value length, entry limits, ordering, visibility, redaction, configured-key absence, freshness, or whether every product custom field is returned. Listing the map does not mutate it or establish product-to-invoice-line propagation; that broader behavior remains owned by the dedicated [[source-metronome-api-reference-custom-fields|custom-fields authority]].

## Errors, idempotency, consistency, and lifecycle unknowns

Only HTTP `200` is listed. This page provides no endpoint-specific `400`, `401`, `403`, `404`, `409`, `429`, or `5xx` response, error envelope, rate limit, timeout, cache header, retry instruction, or recovery procedure. It also does not define authorization scope, default page size, ordering, freshness, read-after-write behavior, snapshot consistency, or audit history.

The separate [[source-metronome-api-reference-idempotency|API-wide idempotency authority]] says `Idempotency-Key` applies to all POST endpoints: identical parameters with the same key return the original result, changed parameters return HTTP `409`, retention is at least 24 hours, and a cached result can be HTTP `500`. This list endpoint neither repeats nor narrows that contract. Replaying an original list result is not proof of a fresh product inventory; the sources do not define how a key relates to query parameters, archive filters, cursors, concurrent edits, expired keys, or recovery from a cached error on this read-only POST operation.

A returned product representation does not create, edit, archive, restore, price, entitle, invoice, export, or reconcile a product. The page does not document update atomicity, history retention, propagation to contracts or rate cards, recalculation of draft or finalized invoices, webhook emission, payment or tax effects, external-system delivery, accounting, settlement, or reconciliation.

## Contradiction check

The five-value product enum is a direct source-scoped contradiction with the four-type product guide and existing concept. No other direct contradiction was found when schema requiredness is preserved: the list response's optional fields do not negate the guide's behavioral claims, and the group-key and quantity-configuration descriptions align with existing product and billable-metric authorities. The initial/current `billable_metric_id` format difference and the example's version timestamps are unresolved schema and example ambiguities rather than proof of different identifier types or chronological semantics.

## Related

- Company: [[metronome]]
- Concepts: [[metronome-products-and-rate-cards]], [[metronome-billable-metrics]], [[metronome-custom-fields]], [[metronome-integrations]], [[metronome-api-idempotency]], [[metronome-security-principles]]
- Product context: [[source-metronome-guides-implement-metronome-core-concepts-create-products-contracts]], [[source-metronome-guides-implement-metronome-core-concepts-create-billable-metrics]]
- API context: [[source-metronome-api-reference-pagination]], [[source-metronome-api-reference-authentication]], [[source-metronome-api-reference-status-codes]], [[source-metronome-api-reference-idempotency]]

## Raw Sources

- [[raw/metronome/api-reference/products/list-products-2026-07-13|2026-07-13 snapshot — product collection filtering, pagination, version-state, and configuration schema]]
