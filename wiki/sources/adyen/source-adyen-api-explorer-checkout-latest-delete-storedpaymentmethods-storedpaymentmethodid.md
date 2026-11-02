---
title: "Adyen Checkout API DELETE /storedPaymentMethods/{storedPaymentMethodId}"
type: source
date_ingested: 2026-11-02
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Checkout/latest/delete/storedPaymentMethods/(storedPaymentMethodId)"
raw_files:
  - "adyen/api-explorer/Checkout/latest/delete/storedPaymentMethods/(storedPaymentMethodId)/2026-11-02.md"
tags: [adyen, checkout, tokenization, stored-payment-methods, api-explorer]
---

## Overview

Captured Checkout API Explorer reference for `DELETE /storedPaymentMethods/{storedPaymentMethodId}` on the v72 test server. It deletes the token identified by the path ID; the source says that token can no longer be used with payment requests. This is a stored-payment-method operation, not a payment authorization or funds movement. [[adyen]] [[adyen-tokenization]]

## Key takeaways

- The API credential must have the `API tokenise payment details` role. The required path `storedPaymentMethodId` identifies the token. Required query parameters are `merchantAccount` (the merchant account) and `shopperReference` (the merchant's unique shopper reference). The shopper reference has a minimum length of three characters and must not contain PII such as a name or email address.
- The documented success response is HTTP `204` with no response fields shown. The page instructs readers to inspect the actual response code for request status. It does not specify idempotency, asynchronous propagation timing, failure codes, or a separate payment outcome.
- This 2026-11-02 snapshot shows `https://checkout-test.adyen.com/v72`. The `latest` URL label and test-server reference do not establish current live availability, merchant eligibility, or execution in an account.

## Detail locators

- Purpose, deletion effect and credential role: raw lines 5-11.
- Server and all request parameters: raw lines 13-28.
- Documented success response: raw lines 30-33.

## Related

- [[adyen-tokenization]] — token lifecycle and related source routes.

## Raw Sources

- [[raw/adyen/api-explorer/Checkout/latest/delete/storedPaymentMethods/(storedPaymentMethodId)/2026-11-02|Checkout DELETE stored payment method API Explorer snapshot]]