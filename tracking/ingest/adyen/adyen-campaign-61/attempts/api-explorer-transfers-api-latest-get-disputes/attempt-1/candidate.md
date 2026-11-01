---
title: "Adyen Transfers API v4: GET /disputes"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/transfers-api/latest/get/disputes"
raw_files:
  - "adyen/api-explorer/transfers-api/latest/get/disputes/2026-09-15.md"
tags: [adyen, platforms, transfers-api, disputes]
---

## Overview

This 2026-09-15 API Explorer reference documents Transfers API `GET /disputes` on the listed `/btl/api/v4` TEST and live servers. It returns raised disputes matching query parameters. The page describes cursor-based pagination with next and previous links where applicable, while separately listing an optional `offset` query parameter; it does not explain their interaction. This is a platform Transfers API dispute-list read, distinct from money-transfer resource reads and from dispute-defense actions in another API family. [[adyen]] [[adyen-platforms]]

## Key takeaways

- All six listed query parameters are optional: `limit` (default 100, maximum 500 items per page), `offset` (number of items to skip), ISO 8601 `createdSince`/`createdUntil` inclusive time bounds, `paymentInstrument` ID, and `status`. The listed status filter values are `draft`, `submitted`, `closed`, `won`, `chargeback`, and `secondPresentment`.
- The 200 section says the request succeeded but supplies no success response-body fields or example. Do not infer dispute item identifiers, cursor token format, link syntax, or resolution outcomes from this page. A retrieved status is a listed dispute state, not a defense or financial result for a particular case.
- The page documents 401 for authentication required, 403 for insufficient permissions, and 422 for request validation error. Each error body table has optional top-level problem fields and optional `invalidFields`; if an `invalidFields` item is present, its `message`, `name`, and `value` are marked required.

## Detail locators

- Purpose, pagination statement and v4 TEST/live servers: raw lines 5–17.
- Query parameters, defaults, limits, time bounds and status enum: raw `## Parameters` → `### Query parameters`, lines 19–29.
- Success statement without response schema: raw lines 31–35.
- 401, 403 and 422 error descriptions and body tables: raw lines 37–91.

## Related

- [[adyen-platforms]] — modern platform context.
- [[source-adyen-api-explorer-transfers-api-latest-overview]] — Transfers API catalog and family scope.

## Raw Sources

- [[raw/adyen/api-explorer/transfers-api/latest/get/disputes/2026-09-15|Transfers API GET /disputes (2026-09-15)]]
