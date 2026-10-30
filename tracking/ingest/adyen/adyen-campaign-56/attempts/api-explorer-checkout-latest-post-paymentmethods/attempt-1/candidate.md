---
title: "Adyen Checkout API v72 POST /paymentMethods"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Checkout/latest/post/paymentMethods"
raw_files:
  - "adyen/api-explorer/Checkout/latest/post/paymentMethods/2026-09-14.md"
tags: [adyen, checkout, api, payment-methods]
---

## Overview

Captured API Explorer reference for Checkout API **v72** `POST /paymentMethods` on the test server. It retrieves payment methods available for the supplied transaction context, such as amount, country and currency. This is method discovery, not a payment creation, authorization, capture or settlement result. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- `merchantAccount` is the only top-level request property marked required in this captured schema. The basic request example contains just that property. The page does not separately label the entire request body as required.
- Optional context and filters include `amount` (currency and minor-unit value are required within that object), `countryCode`, `channel` (iOS, Android or Web platform filtering), `allowedPaymentMethods`, `blockedPaymentMethods`, `store` and `storeFiltrationMode`. `store` is described as required for platform-model Adyen for Platforms integrations. `shopperReference` is described as required for recurring payments and must exclude shopper PII.
- The 200 response schema has optional `paymentMethods` and `storedPaymentMethods` arrays. Entries can include method codes, localized names, input details, issuers, apps and stored-method identifiers/recurring support. Supplying `shopperReference` appears in the include-stored example; the example does not guarantee stored methods.
- The page's test-server URL is `https://checkout-test.adyen.com/v72`; the path segment `latest` in its canonical URL does not establish the current latest API version or live endpoint. Its long response examples are illustrative and do not prove a merchant's enabled methods or shopper eligibility.
- Documented failure classes are 400 (request parsing), 401 (authentication), 403 (permission), 422 (validation) and 500 (server processing). The 422 example says “Return URL is missing,” while no `returnUrl` appears in this endpoint's request table; treat that as an example, not a general `/paymentMethods` requirement.

## Detail locators

- Raw lines 9–53: server, header and complete request property table, including conditional browser/3DS, shopper contact and platform/store notes.
- Raw lines 55–88: basic, filtered and include-stored request examples.
- Raw lines 89–146: 200 response schema, nested method/input/issuer/app fields and stored-method fields.
- Raw lines 149–216 and 1992–2053: error schemas and illustrative error responses.
- Raw lines 218–1990: three illustrative success response bodies; method catalogs here are examples.

## Related

- [[adyen-online-payments]] — provider online-payments concept and source route.

## Raw Sources

- [[raw/adyen/api-explorer/Checkout/latest/post/paymentMethods/2026-09-14|Captured Checkout API v72 POST /paymentMethods reference]]