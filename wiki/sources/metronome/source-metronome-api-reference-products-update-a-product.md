---
title: "Metronome API: Update a Product"
type: source
date_ingested: 2026-09-09
canonical_url: "https://docs.metronome.com/api-reference/products/update-a-product"
original_format: webpage
raw_files:
  - "metronome/api-reference/products/update-a-product-2026-08-28.md"
tags: [metronome, api, products, product-lifecycle, effective-dating]
---

## Overview

Bearer-authenticated `POST /v1/contract-pricing/products/update` schedules configuration changes for an existing Metronome product. The page says the operation maintains billing continuity for active customers, accepts future or retroactive effective times, and returns the updated product ID on success.

## Query-critical facts

- In a supplied JSON payload, `product_id` and `starting_at` are required properties. `product_id` is a UUID, while `starting_at` is a date-time that must fall on an hour boundary. A future timestamp schedules the update; a past timestamp makes it retroactive.
- Product type is immutable. If the type is wrong, the documented route is to create a replacement product and archive the original.
- The payload can update product presentation, metric, grouping, conversion, rounding, composite, tag, refundability, SQL-breakdown, and configuration-dependent integration settings. Use the exact `components.schemas.UpdateProductListItemPayload` locator in the raw page for availability, defaults, qualifications, and nested schemas rather than treating this summary as a field inventory.
- HTTP `200` places the returned identifier at `data.id`. The operation also lists generic HTTP `400` and `404` responses; it does not provide a propagation status, updated Product representation, or endpoint-specific recovery contract.

## Material warnings and boundaries

> [!warning] Product type requires replacement, not mutation
> This endpoint cannot change product type. Creating a replacement and archiving the original does not by itself establish identity, rate, contract, invoice, or reporting continuity between the two products.

> [!warning] Pricing-description boundary
> The operation description says it can modify "pricing rules," but `UpdateProductListItemPayload` exposes no price or rate property. Do not use this page as authority that the endpoint edits rate-card prices; follow the dedicated rate-card operations for price changes.

> [!info] Retroactive-effect boundary
> The page permits a past `starting_at`, but it does not define recalculation of draft or finalized invoices, late usage, credits, commits, exports, or downstream systems. The billing-continuity statement should not be expanded into a guarantee about those historical or propagated outcomes.

The enclosing OpenAPI `requestBody` is not marked required, and the payload schema does not declare a closed-object policy. Do not infer omitted-body or unknown-field runtime behavior.

## Raw-detail coverage map

- **Operation and result:** the complete raw page contains the production server, bearer security, POST path, operation ID, example request, `data.id` success placement, and generic error schemas.
- **Payload detail:** `components.schemas.UpdateProductListItemPayload` contains the required-property list and all optional fields, product-type qualifications, defaults, feature/configuration qualifications, group-key rules, and nested conversion and rounding schemas.

## Related

- Company: [[metronome]]
- Primary concept: [[metronome-products-and-rate-cards]]
- Supporting concepts: [[metronome-billable-metrics]], [[metronome-invoicing]]
- Related sources: [[source-metronome-api-reference-products-create-a-product]], [[source-metronome-api-reference-products-archive-a-product]], [[source-metronome-api-reference-products-get-a-product]], [[source-metronome-api-reference-products-list-products]]

## Raw Sources

- [[raw/metronome/api-reference/products/update-a-product-2026-08-28|2026-08-28 snapshot - complete product-update operation, payload and nested schemas, response envelope, and errors]]
