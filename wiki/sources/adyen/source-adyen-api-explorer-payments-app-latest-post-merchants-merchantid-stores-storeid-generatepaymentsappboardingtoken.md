---
title: "Payments App API v1: create a store-level boarding token"
type: source
date_ingested: 2026-11-07
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/payments-app/latest/post/merchants/(merchantId)/stores/(storeId)/generatePaymentsAppBoardingToken"
raw_files:
  - "adyen/api-explorer/payments-app/latest/post/merchants/(merchantId)/stores/(storeId)/generatePaymentsAppBoardingToken/2026-11-07.md"
tags: [adyen, payments-app, mobile-pos, boarding-token, api-reference]
---

## Overview

This captured Payments App API v1 reference describes `POST /merchants/{merchantId}/stores/{storeId}/generatePaymentsAppBoardingToken`. It creates a boarding token for a Payments App instance's `boardingRequestToken` at the merchant account and store named in the path. The API credential needs the Adyen Payments App role. The reference lists separate live and test Management hosts. See [[adyen]] and [[adyen-mobile-pos]].

## Key takeaways

- Both path identifiers and the `boardingRequestToken` request-body field are marked required. `subMerchantData` is optional; if supplied, its nested `displayName`, `id`, `mcc`, and `name` fields are marked required.
- A 200 response contains `boardingToken`, which allows the Payments App to board, and `installationId`, the Payments App instance identifier. Creation of a token does not itself document completed installation, authorization, or a payment.
- The reference lists 400, 401, 403, 422 and 500 responses. It states no token lifetime, idempotency behavior, or later boarding status in this endpoint's contract.

## Detail locators

- Purpose, role, and live/test base URLs: raw lines 5–19.
- Path and request-body fields: raw lines 21–46.
- Success response: raw lines 48–57.
- Error response codes and optional error-body fields: raw lines 60–152.

## Related

- [[adyen-mobile-pos]] — Android Payments App route and related Mobile POS evidence.

## Raw Sources

- [[raw/adyen/api-explorer/payments-app/latest/post/merchants/(merchantId)/stores/(storeId)/generatePaymentsAppBoardingToken/2026-11-07|Payments App API v1 store-level boarding-token endpoint (2026-11-07)]]
