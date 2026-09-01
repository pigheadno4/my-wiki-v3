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

Bearer-authenticated `POST /v1/contract-pricing/products/create` creates a Metronome product. HTTP `200` requires `data` referencing a generic `Id` object with required UUID `id`, but the schema does not explicitly identify that value as the created Product resource. Metronome describes a product as an individual offering and the basic unit of an invoice line item; its meaningful name appears on customer invoices when the product is used.

## Query-critical facts

- Within a supplied JSON payload, `name` and `type` are schema-required. The enclosing OpenAPI `requestBody` is not marked required, so omitted-body behavior is not established. The payload schema also does not declare `additionalProperties: false`, so unknown-field rejection must not be inferred.
- The create request accepts upper- and lowercase forms of `FIXED`, `USAGE`, `COMPOSITE`, and `SUBSCRIPTION`, plus client-annotated `PROFESSIONAL_SERVICE` and `PRO_SERVICE` forms. Current [[source-metronome-api-reference-products-get-a-product|Get]] and [[source-metronome-api-reference-products-list-products|List]] responses expose only uppercase `USAGE`, `SUBSCRIPTION`, `COMPOSITE`, `FIXED`, and `PRO_SERVICE`, while the [[source-metronome-guides-implement-metronome-core-concepts-create-products-contracts|product guide]] documents four types. These surfaces do not establish response spelling, round-trip normalization, creation support, or general tenant availability for either professional-service label.
- `billable_metric_id` is described as required for a `USAGE` product. Both `composite_product_ids` and `composite_tags` are described as required for a `COMPOSITE` product, although none appears in the payload schema's top-level required array. The product guide instead says applicable composite products can be selected by product ID or product tag. The sources do not establish whether runtime validation requires both arrays, either array, or at least one selector.
- Nullable `quantity_conversion` and `quantity_rounding` are usage-only. Only a supplied non-null conversion object requires `conversion_factor` plus `operation`, and only a supplied non-null rounding object requires `rounding_method` plus `decimal_places`; a supplied `null` does not trigger those nested required lists.
- The create schema says SQL `sql_breakdown_granularity` defaults to `service_period` and recommends `hour`, whereas the current [[source-metronome-guides-implement-metronome-core-concepts-billable-metrics-sql-editor|SQL Editor authority]] says `hour` is the default and `service period` is optional. That guide also shows that the choice changes when cost is incurred, which rate applies, and whether a credit or commit covers the final instant. Current Product Get/List schemas do not expose this field, so they do not establish how to read back or verify the selected value.
- The optional `custom_fields` input is an open string-valued map without an entity annotation. The dedicated [[source-metronome-api-reference-custom-fields|custom-fields authority]] says configured values can be set during object creation, persist and are returned through app, API, and export surfaces, and a Product value propagates to its associated invoice line. The [[source-metronome-api-reference-custom-fields-create-a-custom-field-key|create-key authority]] separately exposes both `product` and `contract_product`, while Product Get/List annotate returned maps as `contract_product`; those names are not reconciled.

## Material boundaries and contradictions

> [!warning] Product-type and composite-selector contracts disagree
> Preserve the create enum, Get/List response enum, four-type guide, create-schema composite descriptions, and guide's ID-or-tag selection as source-scoped surfaces. Do not normalize them into one undocumented runtime contract.

> [!warning] SQL granularity defaults disagree
> The create schema says `service_period` is the default, while the SQL Editor guide says `hour` is the default. Neither source resolves the conflict, and Product Get/List do not expose a read-back field.

- Product creation does not itself assign a price, attach the product to a rate card or contract, or prove invoice adoption. Custom-field propagation applies after a configured value exists and is associated with a product; it does not establish destination precedence, timing, draft-versus-finalized behavior, retroactivity, update or deletion propagation, provider acceptance, payment, tax, accounting, or reconciliation.
- The response does not establish that generic `data.id` is Product identity, product-name uniqueness, duplicate handling, read-after-write visibility, propagation timing, rate-card or contract adoption, invoice adoption, or endpoint-specific recovery after a partial or ambiguous failure.
- The separate API-wide [[source-metronome-api-reference-idempotency|POST idempotency authority]] persists a provided-key result only after execution begins, meaning validation passed and no pre-execution concurrent-request conflict prevented execution. An admitted result is retained for at least 24 hours, may be HTTP `500`, and identical same-key parameters replay that cached result; changed parameters return HTTP `409`. After a cached or ambiguous failure, investigate system state rather than assuming a changed key is safe. Validation failures and pre-execution conflicts are not established cached results, and no-key, another-key, expired-key, product uniqueness, concurrency ordering, propagation, visibility, and endpoint-specific recovery remain unknown.

## Raw-detail coverage map

| Detail category | Exact evidence route |
| --- | --- |
| Method, bearer security, operation description, example payload, success envelope, generic error, and response-identity shape | [[raw/metronome/api-reference/products/create-a-product-2026-08-28|complete create-operation raw]] |
| Full create enum, client annotations, conditional USAGE and COMPOSITE fields, composite scope and beta options, tags, NetSuite and refund fields | [[raw/metronome/api-reference/products/create-a-product-2026-08-28|complete create-operation raw]] |
| SQL granularity wording, pricing and presentation group keys, quantity conversion and rounding schemas, nullability, enums, and numeric minimum | [[raw/metronome/api-reference/products/create-a-product-2026-08-28|complete create-operation raw]] |
| Open string-valued custom-field input and complete schema-requiredness versus description-level requiredness | [[raw/metronome/api-reference/products/create-a-product-2026-08-28|complete create-operation raw]] |

## Related

- Company: [[metronome]]
- Primary concepts: [[metronome-products-and-rate-cards]], [[metronome-billable-metrics]], [[metronome-custom-fields]], [[metronome-invoicing]], [[metronome-api-idempotency]]
- Product authorities: [[source-metronome-guides-implement-metronome-core-concepts-create-products-contracts]], [[source-metronome-api-reference-products-get-a-product]], [[source-metronome-api-reference-products-list-products]]
- SQL authority: [[source-metronome-guides-implement-metronome-core-concepts-billable-metrics-sql-editor]]
- Custom-field authorities: [[source-metronome-api-reference-custom-fields]], [[source-metronome-api-reference-custom-fields-create-a-custom-field-key]]
- Retry authority: [[source-metronome-api-reference-idempotency]]

## Raw Sources

- [[raw/metronome/api-reference/products/create-a-product-2026-08-28|2026-08-28 snapshot - complete create operation, payload schemas, response envelope, and errors]]
