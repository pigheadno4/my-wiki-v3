---
title: "Payments App API: list merchant Payments App instances"
type: source
date_ingested: 2026-11-07
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/payments-app/latest/get/merchants/(merchantId)/paymentsApps"
raw_files:
  - "adyen/api-explorer/payments-app/latest/get/merchants/(merchantId)/paymentsApps/2026-11-07.md"
tags: [adyen, payments-app, mobile-pos, api-explorer]
---

## Overview

This 2026-11-07 snapshot of the Payments App API v1 `GET /merchants/{merchantId}/paymentsApps` reference lists Payments App instances for the merchant account identified by the required path `merchantId`. The API credential needs the Adyen Payments App role. The captured servers are `management-test.adyen.com/v1` and `management-live.adyen.com/v1`. See [[adyen]] and [[adyen-mobile-pos]].

## Key takeaways

- Optional `offset` skips items and `limit` sets the number to return; the reference gives no defaults or maxima. Optional comma-separated `statuses` accepts one or more of `BOARDING`, `BOARDED`, and `REVOKED`; with no value, the list includes all statuses.
- A 200 response has a required `paymentsApps` array. Each listed instance has required `installationId`, `merchantAccountCode`, and `status`; `merchantStoreCode` is optional. The installation ID identifies an app instance, while the merchant ID identifies the account in the request path.
- This is an inventory read. Listed status is a snapshot, not proof of completed boarding, current eligibility, successful authentication, payment authorization, or settlement. The captured reference does not specify status transition timing or pagination totals.

## Detail locators

- Path and query parameters, including status filter: pinned raw lines 21–34.
- 200 response object and field requiredness: pinned raw lines 36–48.
- 400, 401, 403, 422, and 500 errors and their optional problem fields: pinned raw lines 51–143.

## Related

- [[adyen-mobile-pos]] — Android Payments app within the separate mobile POS routes.
- [[source-adyen-api-explorer-payments-app-latest-overview]] — Payments App API v1 endpoint index.

## Raw Sources

- [[raw/adyen/api-explorer/payments-app/latest/get/merchants/(merchantId)/paymentsApps/2026-11-07|Payments App merchant-list API Explorer snapshot]]