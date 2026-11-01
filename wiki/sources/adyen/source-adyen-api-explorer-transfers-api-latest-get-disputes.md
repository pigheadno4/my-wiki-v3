---
title: "Adyen Raise disputes API v4: GET /disputes (transfers-api URL)"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/transfers-api/latest/get/disputes"
raw_files:
  - "adyen/api-explorer/transfers-api/latest/get/disputes/2026-09-15.md"
tags: [adyen, issuing, disputes, api-explorer]
---

## Overview

This 2026-09-15 API Explorer reference documents `GET /disputes` at a `transfers-api` URL and the listed `/btl/api/v4` TEST and live bases. The separately captured [[source-adyen-api-explorer-transfers-api-latest-overview|companion overview]] identifies this route as part of **Raise disputes API v4**, an Issuing API for disputes on Adyen-issued-card transactions and fraud reports. The URL segment is retained exactly as captured; it does not make this a funds-movement Transfers API operation. This endpoint returns raised disputes matching query parameters. [[adyen]] [[adyen-issuing]]

## Key takeaways

- The endpoint page says pagination is cursor based, with next and previous links when applicable, while also listing an optional `offset` query parameter; it does not explain their interaction. All six listed query parameters are optional: `limit` (default 100, maximum 500 items per page), `offset` (number of items to skip), ISO 8601 `createdSince`/`createdUntil` inclusive time bounds, `paymentInstrument` ID, and `status`. The listed status filter values are `draft`, `submitted`, `closed`, `won`, `chargeback`, and `secondPresentment`.
- The 200 section says the request succeeded but supplies no success response-body fields or example. Do not infer dispute item identifiers, cursor token format, link syntax, or resolution outcomes from this page. A list read is not proof of a particular dispute outcome or financial result.
- The page documents 401 for authentication required, 403 for insufficient permissions, and 422 for request validation error. Each error body table has optional top-level problem fields and optional `invalidFields`; if an `invalidFields` item is present, its `message`, `name`, and `value` are marked required.

## Detail locators

- Purpose, pagination statement and v4 TEST/live servers: assigned raw lines 5–17. The companion Raise disputes API identity and Issuing purpose are in [[source-adyen-api-explorer-transfers-api-latest-overview]], whose raw lines 5–7 and 49–61 list this GET route.
- Query parameters, defaults, limits, time bounds and status enum: assigned raw `## Parameters` → `### Query parameters`, lines 19–29.
- Success statement without response schema: assigned raw lines 31–35.
- 401, 403 and 422 error descriptions and body tables: assigned raw lines 37–91.

## Related

- [[adyen-issuing]] — issued-card dispute context.
- [[source-adyen-api-explorer-transfers-api-latest-overview]] — companion Raise disputes API v4 catalog captured at the same `transfers-api` URL family.

## Raw Sources

- [[raw/adyen/api-explorer/transfers-api/latest/get/disputes/2026-09-15|Raise disputes API GET /disputes at transfers-api URL (2026-09-15)]]
