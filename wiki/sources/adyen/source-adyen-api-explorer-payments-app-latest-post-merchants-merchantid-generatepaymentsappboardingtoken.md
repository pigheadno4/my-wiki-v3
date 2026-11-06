---
title: "Adyen Payments App v1 merchant boarding-token creation"
type: source
date_ingested: 2026-11-07
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/payments-app/latest/post/merchants/(merchantId)/generatePaymentsAppBoardingToken"
raw_files:
  - "adyen/api-explorer/payments-app/latest/post/merchants/(merchantId)/generatePaymentsAppBoardingToken/2026-11-07.md"
tags: [adyen, payments-app, mobile-pos, boarding-token, api-explorer]
---

## Overview

This 2026-11-07-captured Payments App API `latest` reference documents `POST /merchants/{merchantId}/generatePaymentsAppBoardingToken` on the v1 management Test and Live servers. It creates a boarding token for a Payments App instance's `boardingRequestToken` under the merchant account identified by the path. See [[adyen]] and [[adyen-mobile-pos]].

## Key takeaways

- The caller's API credential must have the Adyen Payments App role. `merchantId` is the required merchant-account path identifier; `boardingRequestToken` is required in the request body.
- `subMerchantData` is optional. If supplied, its table marks `displayName`, `id`, `mcc`, and `name` required within that object; the remaining listed sub-merchant properties are optional. The reference states no defaults or value limits.
- A `200` response returns `boardingToken`, which allows the Payments App to board, and `installationId`, the unique identifier of that app instance. Token creation/readback does not establish that the app has boarded, that an installation has authenticated, or that any payment occurred.
- The captured page documents `400`, `401`, `403`, `422`, and `500` errors. It provides no token lifetime, idempotency rule, deletion or revocation effect, propagation timing, asynchronous review or activation sequence, failure reversal, or payment/financial result. The `latest` label and listed Live server do not establish current account eligibility.

## Detail locators

- Endpoint purpose, caller role and v1 Test/Live servers: raw lines 5–19.
- Merchant path and request-body fields, including optional parent versus nested required properties: raw lines 21–45.
- Success fields: raw lines 47–56.
- Error status meanings and optional problem-body fields: raw lines 59–151.

## Related

- [[adyen-mobile-pos]] — Android Payments App route.
- [[adyen]] — provider page.

## Raw Sources

- [[raw/adyen/api-explorer/payments-app/latest/post/merchants/(merchantId)/generatePaymentsAppBoardingToken/2026-11-07|Merchant-level Payments App boarding-token POST, captured 2026-11-07]]
