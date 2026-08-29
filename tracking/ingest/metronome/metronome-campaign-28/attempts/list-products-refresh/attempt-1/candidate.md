---
title: "Metronome List Products API"
type: source
date_ingested: 2026-08-29
original_format: webpage
canonical_url: "https://docs.metronome.com/api-reference/products/list-products"
raw_files:
  - "metronome/api-reference/products/list-products-2026-08-28.md"
  - "metronome/api-reference/products/list-products-2026-07-13.md"
tags: [metronome, api, products, pagination, product-history]
---

## Overview

This OpenAPI page documents bearer-authenticated `POST /v1/contract-pricing/products/list`, which returns a cursor-paginated organization-wide product catalog with archive filtering, product identity, current and historical state surfaces, and optional configuration. It is the authority for this List operation; the separate Get and mutation pages retain their own request, response, feature-annotation, and lifecycle contracts.

## Query-critical facts

- The endpoint excludes archived products by default. `archive_filter` accepts `ARCHIVED`, `NOT_ARCHIVED`, or `ALL`, and omission of that property defaults to not archived. The enclosing `requestBody` is not marked `required: true`, while the referenced object has no required properties; omitted-body runtime behavior remains undocumented, an empty supplied object matches the documented property-requiredness, and unknown-field behavior is not established because `additionalProperties` is unspecified.
- Optional query parameters are integer `limit` from `1` through `100` and string `next_page`. HTTP `200` requires both a `data` array and nullable string `next_page`; the separate API-wide pagination source defines `null` as the terminal cursor.
- Every listed product requires UUID `id`, `type`, `initial`, `current`, and an `updates` array. Initial and current state require `name`, `created_at`, and `created_by`, whereas each update requires only `created_at` and `created_by`. The page promises complete version history but defines no update ordering, retention horizon, omitted-field inheritance, future-update visibility, current-state selection, or cross-page consistency.
- The response enum contains `USAGE`, `SUBSCRIPTION`, `COMPOSITE`, `FIXED`, and `PRO_SERVICE`. The product guide documents only four types, so this List response does not establish whether `PRO_SERVICE` is creatable, API-only, feature-gated, legacy, or otherwise supported by mutation flows.
- Product state and update objects can expose metric, composite, quantity-conversion, rounding, tag, group-key, NetSuite, and custom-field surfaces. Quantity conversion and rounding are explicitly usage-only; pricing and presentation group keys are usage-only and require their combined value superset as one compound billable-metric group key. These response fields do not prove create/edit acceptance, product-type applicability beyond their own annotations, or downstream billing behavior.
- In the 2026-08-28 List snapshot, `include_composite_spend` appears on state and update without the earlier feature and SDK-skip annotations; it remains composite-only and defaults false. `composite_scope` remains state-only, selects `CUSTOMER` or `CONTRACT`, and retains feature and SDK-skip annotations. This List-specific drift does not establish general tenant availability and must not be generalized to the separate Get or mutation schemas.

## Material boundaries

- Only HTTP `200` is listed. The page does not define endpoint-specific authorization failures, invalid-body or cursor errors, rate limits, result ordering, cursor lifetime, snapshot consistency, freshness, read-after-write behavior, or duplicate and skipped-item behavior during concurrent product edits or archival.
- The API-wide `Idempotency-Key` authority applies to all POST endpoints: identical same-key parameters replay the original result, changed parameters conflict, retention is at least 24 hours, and the cached result can be HTTP `500`. This List page adds no endpoint-specific retry or cache semantics; replaying an original list result is not evidence of a fresh catalog.
- Optional custom fields are an arbitrary-key string map annotated for `contract_product`, and NetSuite item identifiers are configuration-dependent. Their presence in this response does not establish configured-field completeness, mapping validity, synchronization, invoice delivery, accounting, settlement, or reconciliation.

> [!warning] Product-type contradiction
> The List schema exposes five product types including `PRO_SERVICE`, while the product guide enumerates only usage, fixed, composite, and subscription products. Preserve the source-scoped mismatch and verify current creation support rather than treating either schema as authority for the other.

## Raw-detail coverage map

- **Operation and traversal:** the production server, bearer-security declaration, operation ID, archive-filter example and enum, query parameters, success envelope, and pagination cursor are in the current raw page.
- **Product identity and history:** the complete required and optional product, initial/current state, and update schemas, plus the success example and history claim, are in the current raw page.
- **Type-specific configuration:** all metric, composite, quantity conversion, rounding, tagging, group-key, feature-annotation, format, nullability, enum, and numeric-constraint details are in the current raw page.
- **Metadata and integration surfaces:** the custom-field map and configuration-dependent NetSuite identifiers are in the current raw page; dedicated custom-field and integration sources remain authoritative for behavior beyond this response shape.
- **Schema history:** the retained 2026-07-13 snapshot preserves the earlier List-specific feature and SDK-skip annotations on `include_composite_spend`; do not use the neighboring Get schema as a substitute for either List snapshot.

## Related

- Company: [[metronome]]
- Primary concept: [[metronome-products-and-rate-cards]]
- Additional affected concepts: [[metronome-billable-metrics]], [[metronome-custom-fields]], [[metronome-integrations]], [[metronome-api-idempotency]]
- Product context: [[source-metronome-guides-implement-metronome-core-concepts-create-products-contracts]]
- API-wide authorities: [[source-metronome-api-reference-pagination]], [[source-metronome-api-reference-idempotency]]
- Separate Get contract: [[source-metronome-api-reference-products-get-a-product]]

## Raw Sources

- [[raw/metronome/api-reference/products/list-products-2026-08-28|2026-08-28 snapshot - product catalog filtering, pagination, identity, history surfaces, and current List schema annotations]]
- [[raw/metronome/api-reference/products/list-products-2026-07-13|2026-07-13 snapshot - prior List schema preserved for annotation history]]
