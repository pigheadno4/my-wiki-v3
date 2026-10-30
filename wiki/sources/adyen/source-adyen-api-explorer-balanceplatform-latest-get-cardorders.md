---
title: "Adyen Balance Platform API v2: List card orders"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform/latest/get/cardorders"
raw_files:
  - "adyen/api-explorer/balanceplatform/latest/get/cardorders/2026-09-15.md"
tags: [adyen, issuing, balance-platform, card-orders, api]
---

## Overview

Captured API Explorer reference for `GET /cardorders` in the Balance Platform API, with the test server shown at `https://balanceplatform-api-test.adyen.com/bcl/v2`. It returns a paginated list of card orders. This is a card-order lookup, not card creation, manufacturing confirmation, payment authorization, or funds movement. See [[adyen]] and [[adyen-issuing]].

## Key takeaways

- All listed query parameters are optional. `limit` defaults to 10 and `offset` to 0; the reference also offers service-center, creation/lock-time, card-manufacturer, status, and card-order-ID filters. The timestamp filters specify ISO 8601; `serviceCenter` is case-sensitive.
- The 200 response documents optional `cardOrders` and required `hasNext`/`hasPrevious` page indicators. A card order can expose its identifier, manufacturing-profile identifier, service center, dates, and status. The table describes `Open` and `Closed`; its success example instead uses lowercase `closed`. Do not infer a canonical status casing from this capture.
- The `endDate` field is for manual closure; the reference says card orders automatically close by the end of their creation day. `lockDate` denotes the start of processing and `closedDate` its end. These field descriptions do not prove that any particular order was manufactured or delivered.
- The reference lists 401 authentication, 403 permission, 422 validation, and 500 server errors. Its generic 422 and 500 JSON examples describe payment-instrument changes/creation, so they are not evidence of card-order-specific validation or failure behavior. No particular required role or live availability is established here.

## Detail locators

- Query parameters, optionality, defaults, and filters: pinned raw, `## Parameters` → `### Query parameters`, lines 12–27.
- Success schema, date meanings, status, and page indicators: `## Responses` → `### 200 Success`, lines 29–47.
- Error meanings and schemas: `## Responses`, lines 50–127. Example/schema mismatches: `## Response examples`, lines 129–204.

## Related

- [[adyen-issuing]] — card-program context.
- [[adyen-platforms]] — balance-platform context.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform/latest/get/cardorders/2026-09-15|Captured GET /cardorders API Explorer reference (2026-09-15)]]
