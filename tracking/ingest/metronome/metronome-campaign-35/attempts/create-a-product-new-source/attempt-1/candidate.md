---
title: "Metronome API: Create a Product"
type: source
date_ingested: 2026-09-01
canonical_url: "https://docs.metronome.com/api-reference/products/create-a-product"
original_format: webpage
raw_files:
  - "metronome/api-reference/products/create-a-product-2026-08-28.md"
tags: [metronome, api, products, pricing, invoicing]
---

## Overview

Bearer-authenticated `POST /v1/contract-pricing/products/create` creates a Metronome product and returns its UUID under `data.id`. Metronome describes a product as an individual offering and the basic unit of an invoice line item; its meaningful `name` is displayed on customer invoices.

## Query-critical facts

- Within a supplied JSON payload, `name` and `type` are schema-required. The enclosing OpenAPI `requestBody` is not marked required, so omitted-body behavior is not established. The payload schema also does not declare `additionalProperties: false`, so unknown-field rejection must not be inferred.
- The creation enum includes upper- and lowercase forms of `FIXED`, `USAGE`, `COMPOSITE`, and `SUBSCRIPTION`, plus `PROFESSIONAL_SERVICE` and `PRO_SERVICE` forms that carry client-group annotations. Schema exposure does not establish universal tenant availability.
- `billable_metric_id` is described as required for a `USAGE` product. Both `composite_product_ids` and `composite_tags` are described as required for a `COMPOSITE` product, although none of these conditional fields appears in the payload schema's top-level `required` array; the page does not reconcile description-level and schema-level enforcement.
- For SQL billable metrics, `sql_breakdown_granularity` defaults to `service_period`, while `hour` is recommended for most use cases; the setting has no effect on streaming billable metrics. Usage-only pricing and presentation group keys must together fit one compound group key on the billable metric.
- Optional usage-product quantity conversion requires a factor and multiply/divide operation when supplied; optional quantity rounding requires a method and nonnegative decimal places. `custom_fields` is an object whose arbitrary property values are strings.
- HTTP `200` requires `data`, whose referenced `Id` object requires UUID `id`. HTTP `400` uses a generic error with required string `message`; neither response documents a complete created-product state.

## Material boundaries

- Product creation does not itself assign a price, add the product to a rate card or contract, or establish that an invoice will adopt it. The invoice-line role and displayed name describe catalog meaning and presentation when the product is used, not downstream pricing or invoice propagation.
- The response does not establish product-name uniqueness, duplicate handling, read-after-write visibility, propagation timing, rate-card adoption, contract adoption, invoice adoption, or recovery after a partial or ambiguous failure.
- The create schema's professional-service values and client-group annotations must be preserved alongside the existing guide-level four-type catalog; do not infer that annotated values are generally enabled.
- The separate API-wide [[source-metronome-api-reference-idempotency|POST idempotency authority]] applies only after a provided-key request begins execution, meaning validation passed and no pre-execution concurrent-request conflict prevented execution. After that admission point, identical same-key parameters replay the persisted original result and changed parameters return HTTP `409`; validation failures and pre-execution conflicts are not established cached results. This endpoint adds no product-specific uniqueness, retry, concurrency, visibility, propagation, or ambiguous-failure recovery guarantee.

## Raw detail coverage

The complete raw reference preserves the production server and bearer scheme; exact operation and example payload; full product-type enum and client-group annotations; configuration-dependent NetSuite and refund fields; conditional usage and composite fields; SQL breakdown defaults; composite scope, beta, and nested-spend options; tags; pricing and presentation group keys; nested quantity conversion and rounding schemas; the open string-valued custom-field map; and complete success and generic error schemas. Use the exact raw page below for those details rather than treating this routing source as a closed payload catalog.

## Related

- Company: [[metronome]]
- Primary concepts: [[metronome-products-and-rate-cards]], [[metronome-billable-metrics]], [[metronome-invoicing]], [[metronome-custom-fields]], [[metronome-api-idempotency]]
- Related sources: [[source-metronome-guides-implement-metronome-core-concepts-create-products-contracts]], [[source-metronome-api-reference-custom-fields]], [[source-metronome-api-reference-idempotency]]

## Raw Sources

- [[raw/metronome/api-reference/products/create-a-product-2026-08-28|2026-08-28 snapshot - complete create operation, payload schemas, response envelope, and errors]]
