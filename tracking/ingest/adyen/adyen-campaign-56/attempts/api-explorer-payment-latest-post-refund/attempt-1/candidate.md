---
title: "Adyen Classic Payment API POST /refund (captured v68)"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Payment/latest/post/refund"
raw_files:
  - "adyen/api-explorer/Payment/latest/post/refund/2026-09-15.md"
tags: [adyen, classic-api, payment-api, refunds, api-explorer]
---

## Overview

This 2026-09-15 API Explorer snapshot documents Classic Payment API `POST /refund` at the displayed test `https://pal-test.adyen.com/pal/servlet/Payment/v68` server. It requests a full or partial refund of a previously captured payment and returns a unique request reference. The page marks the endpoint inactive for new integrations, directs new builds to Checkout API `/payments/{paymentPspReference}/refunds`, and advises existing users to contact Adyen about migration. This is a Classic endpoint contract, not the Checkout refunds contract. See [[adyen]] and [[adyen-refunds]].

## Key takeaways

- The payment must have been captured. An authorised but uncaptured payment is directed to cancellation instead. Multiple partial refunds are described as acceptable while their sum stays within the captured amount, subject to method/gateway support; a configurable margin above the captured limit can cover shipping or handling. The request table also says `modificationAmount.value` must be at most the **authorised** amount. These captured-versus-authorised phrasings are not identical; preserve the qualified overview rather than treating the table's bound as proof that uncaptured value can be refunded.
- The request property table marks `merchantAccount`, `modificationAmount` with matching authorisation currency and minor-unit value, and `originalReference` required. `originalReference` is the original payment PSP reference from authorisation; optional `reference` labels this refund modification. The table does not separately state whole-body requiredness.
- HTTP 200 returns a PSP reference for the refund request and a `response` value indicating receipt for processing; the example is `[refund-received]`. Receipt is not completed refund, shopper receipt of funds, or settlement proof. The wider Classic refund guide covers asynchronous result handling.
- The page lists 400 malformed-request, 401 authentication, 403 permission, 422 validation, and 500 server error schemas, with 200/400/401/500 examples. Its optional `originalMerchantReference` description says “to cancel” despite this refund endpoint; do not use that copy to infer a cancellation action.
- The captured `latest` path displays Classic Payment API test v68 only. It does not establish today's latest version, live account eligibility, a real refund, or the linked Checkout endpoint's schema.

## Detail locators

- Captured-payment eligibility, partial-refund qualifications, inactive/migration note, and test server: raw lines 5–23.
- Request schema: lines 27–64; core required fields 31–34 and 49, optional original merchant/reference fields 48 and 54, platform-specific splits 50–62. Request example: 66–79.
- Response 200 acknowledgement and request PSP identity: lines 80–90 and 162–172. Error schemas and examples: 93–160 and 174–209.

## Related

- [[source-adyen-docs-online-payments-classic-integrations-modify-payments-refund]] — broader Classic refund lifecycle and webhook guide.
- [[adyen-refunds]] — provider concept and reciprocal source route.

## Raw Sources

- [[raw/adyen/api-explorer/Payment/latest/post/refund/2026-09-15|Classic Payment API POST /refund snapshot (2026-09-15)]]
