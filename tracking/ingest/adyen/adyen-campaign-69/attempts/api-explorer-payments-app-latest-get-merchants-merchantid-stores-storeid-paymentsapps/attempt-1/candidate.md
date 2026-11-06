---
title: "List store Payments App instances"
type: source
date_ingested: 2026-11-07
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/payments-app/latest/get/merchants/(merchantId)/stores/(storeId)/paymentsApps"
raw_files:
  - "adyen/api-explorer/payments-app/latest/get/merchants/(merchantId)/stores/(storeId)/paymentsApps/2026-11-07.md"
tags: [adyen, payments-app, mobile-pos, api-explorer]
---

## Overview

Captured Payments App API v1 GET reference for listing Payments App instances under a specified merchant account and store. It concerns the separate Android Payments App, not an app installed on an Adyen terminal. See [[adyen]] and [[adyen-mobile-pos]].

## Key takeaways

- The path requires `merchantId` (merchant account identifier) and `storeId` (store identifier). The API credential needs the Adyen Payments App role. Captured live and test servers are `management-live.adyen.com/v1` and `management-test.adyen.com/v1`.
- Optional `offset` and `limit` paginate the list. Optional comma-separated `statuses` filters by `BOARDING`, `BOARDED`, or `REVOKED`; without a status value, the list returns all statuses. The raw gives no numeric pagination limits or default values.
- A 200 response has a required `paymentsApps` array. Each listed instance has required `installationId`, `merchantAccountCode`, and `status`; `merchantStoreCode` is optional. These are instance readback fields, not boarding-token or payment results.
- The reference lists 400, 401, 403, 422, and 500 error responses. A successful list read does not establish current account eligibility, a newly completed boarding transition, payment authorization, capture or settlement. This dated reference gives no propagation timing or revocation reversal contract.

## Detail locators

- Operation, role and v1 test/live servers: raw lines 5–19.
- Path and optional query parameters, including status values: raw lines 21–35.
- 200 response fields and requiredness: raw lines 37–49.
- Error response schemas: raw lines 52–144.

## Related

- [[adyen-mobile-pos]] — mobile-device Payments App context.
- [[source-adyen-api-explorer-payments-app-latest-overview]] — Payments App API v1 endpoint index.

## Raw Sources

- [[raw/adyen/api-explorer/payments-app/latest/get/merchants/(merchantId)/stores/(storeId)/paymentsApps/2026-11-07|Store Payments Apps GET reference, captured 2026-11-07]]