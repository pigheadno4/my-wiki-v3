---
title: "Update the rate card products order"
type: source
date_ingested: 2026-09-13
original_format: webpage
canonical_url: "https://docs.metronome.com/api-reference/rate-cards/update-the-rate-card-products-order"
raw_files:
  - "metronome/api-reference/rate-cards/update-the-rate-card-products-order-2026-07-13.md"
tags: [metronome, api-reference, rate-cards, products, invoice-presentation]
---

## Overview

This API reference documents bearer-authenticated `POST /v1/contract-pricing/rate-cards/moveRateCardProducts`, which changes the invoice-presentation order of selected products on a rate card by moving them relative to their current locations. Each requested destination is a zero-based position.

## Query-critical behavior and qualifications

- Within a supplied JSON payload, `rate_card_id` and `product_moves` are required properties. Each move requires a `product_id` and numeric `position`; the position has a minimum of zero.
- The enclosing OpenAPI `requestBody` is not marked required, so this page does not establish omitted-body runtime behavior.
- HTTP `200` requires top-level `data` referencing the generic `components.schemas.Id`. The example repeats the rate-card UUID at `data.id`, but the generic schema does not label the identifier's semantic object.

## API and raw-detail locators

- **Operation and authentication:** `## OpenAPI` -> document-level `security` -> `bearerAuth`, and `paths./v1/contract-pricing/rate-cards/moveRateCardProducts.post` for the method, path, purpose, and operation ID.
- **Move request:** `components.schemas.MoveRateCardProductsPayload` documents the required rate-card selector and move array; its item schema documents required `product_id` and zero-based `position`.
- **Response placement:** `paths./v1/contract-pricing/rate-cards/moveRateCardProducts.post.responses.200.content.application/json.schema` requires top-level `data` and references `components.schemas.Id`.

## Related

- Company: [[metronome]]
- Main concept: [[metronome-products-and-rate-cards]]

## Raw Sources

- [[raw/metronome/api-reference/rate-cards/update-the-rate-card-products-order-2026-07-13|2026-07-13 snapshot - relative rate-card product moves, invoice presentation effect, request schema, and response route]]
