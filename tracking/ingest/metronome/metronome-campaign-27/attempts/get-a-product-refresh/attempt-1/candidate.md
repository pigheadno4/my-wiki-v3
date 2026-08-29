---
title: "Metronome Get a Product API"
type: source
date_ingested: 2026-08-29
original_format: webpage
canonical_url: "https://docs.metronome.com/api-reference/products/get-a-product"
raw_files:
  - "metronome/api-reference/products/get-a-product-2026-08-28.md"
  - "metronome/api-reference/products/get-a-product-2026-07-13.md"
tags: [metronome, api, products, product-history, usage-based-billing]
---

## Overview

This OpenAPI page documents bearer-authenticated `POST /v1/contract-pricing/products/get`, which retrieves one product by ID with metadata and historical-change surfaces. It is a read contract: the page does not create, edit, archive, price, or attach a product to a contract.

## Query-critical facts

- The request uses an `application/json` body referencing `Id`; inside that supplied object, `id` is required and UUID-formatted. The enclosing `requestBody` is not marked `required: true`, so omitted-body behavior is undocumented, and `Id` does not declare `additionalProperties: false`, so unknown-field handling is also undocumented.
- HTTP `200` requires top-level `data`. `ProductListItem` requires UUID `id`, `type`, `initial`, `current`, and `updates`; the five-value type enum is `USAGE`, `SUBSCRIPTION`, `COMPOSITE`, `FIXED`, or `PRO_SERVICE`. The separate product guide documents only four types, so this read schema does not establish `PRO_SERVICE` creation support or behavior.
- Both `initial` and `current` reference a state that requires `name`, `created_at`, and `created_by`; each update requires only `created_at` and `created_by`. Although the operation promises all metadata and historical changes, it defines no update ordering, completeness or retention rule, version identity, omitted-field inheritance, effective-time selection, future-update visibility, archive-event representation, freshness, or read-after-write consistency.
- The broader state and update objects contain fields whose reusable schemas narrow their applicability. Quantity conversion and rounding are explicitly valid only for usage products; pricing and presentation group keys are usage-only and require their combined value superset as one compound billable-metric group key. `include_composite_spend` appears on state and updates but is explicitly composite-only and defaults false; `composite_scope` appears only on state, is feature-annotated, and selects `CUSTOMER` or `CONTRACT`. Field presence in these broad response objects does not make every field valid for every product type or prove create/edit acceptance.
- Optional product custom fields form an arbitrary-key object with string values and carry the `contract_product` annotation. Optional NetSuite item identifiers in state and updates are expressly configuration-dependent. These are response shapes, not proof of configured-key completeness, integration readiness, synchronization, invoice delivery, accounting, or reconciliation.

## Material boundaries

- The only operation-specific non-success response documented is HTTP `404` with an error object requiring string `message`. The page does not distinguish unknown, archived, unauthorized, or otherwise invisible products and does not document other status mappings, archive retrievability, restoration, retention, permissions, rate limits, or caching.
- This POST read falls under the separate [[source-metronome-api-reference-idempotency|API-wide idempotency authority]], but this endpoint raw adds no read-specific retry, concurrency, cache, freshness, another-key, expired-key, or recovery semantics. Identical same-key replay returns the original result and is not evidence of a fresh product view.
- In the 2026-08-28 Get snapshot, `composite_scope` retains feature and SDK-skip annotations while `include_composite_spend` appears without those annotations in both state and update. This source-scoped schema drift corrects the earlier Get summary, but it does not prove general tenant availability and must not be generalized to the separately documented List operation or to mutation schemas.

## Raw-detail coverage map

Use the complete 2026-08-28 raw snapshot for the production server and bearer-security declaration; exact operation ID, payload example, success example, and 404 shape; all required and optional product, state, update, custom-field, NetSuite, composite, usage-conversion, rounding, group-key, and error properties; every enum, format, nullability rule, minimum, feature annotation, and description; and the exact differences from the preserved 2026-07-13 snapshot.

## Related

- Company: [[metronome]]
- Primary concept: [[metronome-products-and-rate-cards]]
- Additional affected concepts: [[metronome-billable-metrics]], [[metronome-custom-fields]], [[metronome-integrations]], [[metronome-api-idempotency]]
- Product semantics: [[source-metronome-guides-implement-metronome-core-concepts-create-products-contracts]]
- Custom-field authority: [[source-metronome-api-reference-custom-fields]]
- API-wide idempotency authority: [[source-metronome-api-reference-idempotency]]

## Raw Sources

- [[raw/metronome/api-reference/products/get-a-product-2026-08-28|2026-08-28 snapshot - product lookup, identity, state and history surfaces, schema applicability, integration fields, and current feature annotations]]
- [[raw/metronome/api-reference/products/get-a-product-2026-07-13|2026-07-13 snapshot - prior product lookup schema preserved for history]]
