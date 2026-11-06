---
title: "Adyen Payments App instance authentication revocation"
type: source
date_ingested: 2026-11-07
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/payments-app/latest/post/merchants/(merchantId)/paymentsApps/(installationId)/revoke"
raw_files:
  - "adyen/api-explorer/payments-app/latest/post/merchants/(merchantId)/paymentsApps/(installationId)/revoke/2026-11-07.md"
tags: [adyen, payments-app, mobile-pos, api-explorer]
---

## Overview

Captured Payments App API `POST /merchants/{merchantId}/paymentsApps/{installationId}/revoke` reference for revoking authentication of a Payments App instance identified by its device installation ID and merchant account. The description says this revokes the instance's authentication for both merchant accounts and stores. This is an authentication-management operation, not a payment or app-installation result. See [[adyen]] and [[adyen-mobile-pos]].

## Key takeaways

- The path requires `merchantId` (merchant account identifier) and `installationId` (the Payments App instance identifier on a device). The API credential must have the Adyen Payments App role.
- The captured test and live servers are `https://management-test.adyen.com/v1` and `https://management-live.adyen.com/v1`. The reference specifies no request body, query parameters, idempotency rule, default, limit, or response fields for success.
- HTTP 200 says the request succeeded. The page does not specify revocation propagation timing, a reversal path, resulting app state, or an asynchronous notification. It does not establish payment authorization, capture, settlement, or a bank receipt.
- Documented failures are HTTP 400 (request problem), 401 (authentication required), and 500 (server could not process the request). The error-body fields are optional at the top level; consult the raw schema for the conditional `invalidFields` members.

## Detail locators

- Operation identity, effect, and role: raw lines 5–11.
- Test/live v1 servers: raw lines 13–19.
- Required path identifiers: raw lines 21–27.
- Success and error responses: raw lines 29–89.

## Related

- [[adyen-mobile-pos]] — separate Android Payments App route.
- [[adyen]] — provider index.

## Raw Sources

- [[raw/adyen/api-explorer/payments-app/latest/post/merchants/(merchantId)/paymentsApps/(installationId)/revoke/2026-11-07|Payments App revoke operation, captured 2026-11-07]]
