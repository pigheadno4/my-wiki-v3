---
title: "Metronome API: List Rate Cards"
type: source
date_ingested: 2026-09-08
original_format: webpage
canonical_url: "https://docs.metronome.com/api-reference/rate-cards/list-rate-cards"
raw_files:
  - "metronome/api-reference/rate-cards/list-rate-cards-2026-07-13.md"
tags: [metronome, api-reference, rate-cards, pricing-catalog, pagination]
---

## Overview

This API reference documents bearer-authenticated `POST /v1/contract-pricing/rate-cards/list`, which lists rate-card catalog metadata such as IDs, names, descriptions, aliases, and other details. It is the discovery route for finding rate cards before using the separate rate or rate-schedule operations to inspect their actual rates.

## Retrieval boundary

> [!warning] This operation does not return the rates on each card
> The page directs actual-rate inspection to the separate `getRates` or `getRateSchedule` endpoints. Their contents were not used as evidence for this source.

The optional query parameter `limit` accepts 1 through 100 results, and optional `next_page` supplies the cursor where the next page should start. A successful `200` response requires top-level `data` and `next_page` fields: `data` is an array of `RateCard` objects, while `next_page` is a nullable string.

## Raw detail locators

- Method, path, operation ID, bearer authentication, request media type, and empty request example: OpenAPI `security` and `paths./v1/contract-pricing/rate-cards/list.post`.
- Query pagination controls: `components.parameters.PageLimit` and `components.parameters.NextPage`.
- Success envelope and response example: `paths./v1/contract-pricing/rate-cards/list.post.responses.200`.
- Required rate-card metadata and optional descriptions, credit types and conversions, aliases, and custom fields: `components.schemas.RateCard`, `CreditType`, `CreditTypeConversion`, `RateCardAlias`, and `CustomField`.

## Related

- Company: [[metronome]]
- Main concept: [[metronome-products-and-rate-cards]]

## Raw Sources

- [[raw/metronome/api-reference/rate-cards/list-rate-cards-2026-07-13|2026-07-13 snapshot - rate-card catalog listing, pagination, response envelope, and schemas]]
