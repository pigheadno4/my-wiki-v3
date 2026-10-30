---
title: "Adyen Payment API POST /cancelOrRefund"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Payment/latest/post/cancelOrRefund"
raw_files:
  - "adyen/api-explorer/Payment/latest/post/cancelOrRefund/2026-09-15.md"
tags: [adyen, payment-api, classic, cancellation, refund]
---

## Overview

This 2026-09-15-captured [[adyen]] Payment API reference documents Classic `POST /cancelOrRefund` on the listed `pal-test.adyen.com/pal/servlet/Payment/v68` test server. It requests cancellation before capture or refund after capture when capture state is uncertain. The page marks the endpoint inactive and unsupported for new integrations; it directs new builds to Checkout API `/payments/{paymentPspReference}/reversals` and existing users to contact Adyen about migration. That Checkout link is navigation, not evidence of its request or response contract.

## Key takeaways

- Do not use this endpoint for payments with multiple partial captures or Adyen for Platforms split data supplied at payment or capture. The page instead directs users to check capture state and make the corresponding Classic `/refund` or `/cancel` call.
- The request body requires `merchantAccount` and `originalReference`, the original payment's PSP reference from its authorization response or notification. `reference` is an optional modification reference. Other conditional fields are in the raw schema.
- The 200 response includes a *modification-request* `pspReference` and `response`, which indicates receipt for processing; the example is `[cancelOrRefund-received]`. This is not proof that cancellation or refund finished. The original payment reference and new modification reference have different roles.
- The page lists 400, 401, 403, 422 and 500 error tables; its response examples cover 400, 401 and 500. Example errors do not establish a complete endpoint-specific error catalog.

## Detail locators

- Lifecycle, exclusions, inactivity, migration and v68 server: raw lines 5–28.
- Request schema and example: raw lines 30–69.
- 200 acknowledgement and error tables: raw lines 70–150; examples: 152–199.

## Related

- [[adyen-online-payments]] — Classic integration and modification routes.

## Raw Sources

- [[raw/adyen/api-explorer/Payment/latest/post/cancelOrRefund/2026-09-15|Payment API POST /cancelOrRefund, captured 2026-09-15]]
