---
title: "Set the rate card products order"
type: source
date_ingested: 2026-09-13
original_format: webpage
canonical_url: "https://docs.metronome.com/api-reference/rate-cards/set-the-rate-card-products-order"
raw_files:
  - "metronome/api-reference/rate-cards/set-the-rate-card-products-order-2026-07-13.md"
tags: [metronome, api-reference, rate-cards, products, invoice-presentation]
---

## Overview

This API reference documents bearer-authenticated `POST /v1/contract-pricing/rate-cards/setRateCardProductsOrder`, which sets a rate card's product sequence for how those products appear on customer invoices. The documented effect is invoice presentation order; this page does not describe changing product prices or rate schedules.

## Query-critical behavior and warning

- Within a supplied JSON payload, `rate_card_id` and `product_order` are required properties. The target is a rate-card UUID, and `product_order` is an ordered array of product UUIDs.
- HTTP `200` places `data` at the top level and routes its shape to the generic `components.schemas.Id` response schema.

> [!warning] Omitted-product behavior is undocumented
> The page does not say where rate-card products omitted from `product_order` appear or whether the request must enumerate every product on the card. Do not infer append, preservation, removal, or rejection behavior from this schema.

## API and raw-detail locators

- **Operation and authentication:** `## OpenAPI` -> document-level `security` -> `bearerAuth`, and `paths` -> `/v1/contract-pricing/rate-cards/setRateCardProductsOrder` -> `post`.
- **Request target and order:** `components.schemas.SetRateCardProductsOrderPayload` documents the required `rate_card_id` and `product_order` payload properties and their UUID shapes. The enclosing `requestBody` is not marked required; this page does not establish omitted-body runtime behavior.
- **Response placement:** `paths./v1/contract-pricing/rate-cards/setRateCardProductsOrder.post.responses.200.content.application/json.schema` requires top-level `data` and references `components.schemas.Id`.

## Related

- Company: [[metronome]]
- Main concept: [[metronome-products-and-rate-cards]]

## Raw Sources

- [[raw/metronome/api-reference/rate-cards/set-the-rate-card-products-order-2026-07-13|2026-07-13 snapshot - rate-card product ordering for invoice presentation, request target, and response schema]]
