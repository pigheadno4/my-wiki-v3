---
title: "Metronome API: Get a Rate Card"
type: source
date_ingested: 2026-09-07
original_format: webpage
canonical_url: "https://docs.metronome.com/api-reference/rate-cards/get-a-rate-card"
raw_files:
  - "metronome/api-reference/rate-cards/get-a-rate-card-2026-07-13.md"
tags: [metronome, api-reference, rate-cards, pricing-catalog]
---

## Overview

This API reference documents bearer-authenticated `POST /v1/contract-pricing/rate-cards/get`, which retrieves one rate card by ID. It is the evidence route for the card's identifying metadata, creation metadata, credit type and conversions, aliases, and custom fields.

## Retrieval boundary

> [!warning] This endpoint does not return rates
> The operation returns rate-card details, not the rates on the card. The page directs rate queries to the dedicated `getRates` or `getRateSchedule` operations; their contents were not used as evidence for this source.

A successful `200` response requires a top-level `data` property referencing `RateCard`. That schema requires `id`, `name`, `created_at`, and `created_by`; its other documented detail categories remain in the raw schema rather than being reconstructed here. The operation also lists a `404` response for a resource that was not found.

## Raw detail locators

- Method, path, operation ID, bearer authentication, and media type: OpenAPI `security` and `paths./v1/contract-pricing/rate-cards/get.post`.
- Request identity and requiredness: `paths./v1/contract-pricing/rate-cards/get.post.requestBody` and `components.schemas.Id`. The `Id` schema requires UUID `id`, while the enclosing `requestBody` is not marked required; omitted-body behavior is not documented.
- Success envelope and example: `paths./v1/contract-pricing/rate-cards/get.post.responses.200`.
- Required metadata and optional description, credit-type conversion, alias, and custom-field shapes: `components.schemas.RateCard`, `CreditType`, `CreditTypeConversion`, `RateCardAlias`, and `CustomField`.
- Not-found response: `components.responses.NotFound` and `components.schemas.Error`.

## Related

- Company: [[metronome]]
- Main concept: [[metronome-products-and-rate-cards]]

## Raw Sources

- [[raw/metronome/api-reference/rate-cards/get-a-rate-card-2026-07-13|2026-07-13 snapshot - rate-card metadata retrieval, response boundary, and OpenAPI schemas]]
