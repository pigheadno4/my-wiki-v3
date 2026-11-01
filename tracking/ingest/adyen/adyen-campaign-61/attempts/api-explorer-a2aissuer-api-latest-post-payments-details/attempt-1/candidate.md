---
title: "Adyen A2A Issuer API v1: Retrieve payment details"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/a2aissuer-api/latest/post/payments/details"
raw_files:
  - "adyen/api-explorer/a2aissuer-api/latest/post/payments/details/2026-09-15.md"
tags: [adyen, business-accounts, a2a, issuer-api, payments]
---

## Overview

This 2026-09-15-captured A2A Issuer API **v1** reference defines `POST /payments/details` on separate test and live balance-platform hosts. It retrieves an **open** A2A payment's details, which the integrator must show the user, and an Adyen-generated payment token needed for a later confirm or cancel call. It is an issuer-side Business Accounts payment-information step, separate from merchant Checkout `/payments/details` and from payment confirmation or funds movement. [[adyen-business-accounts]] [[adyen]]

## Key takeaways

- The request body requires `method`, payment-method-generated `payload`, and `source`. The payload is obtained from that source; listed source values are `qr`, `redirect`, and `pushNotification`. The iDEAL example uses `method: ideal` and `source: redirect` with a redirect URL payload; it is an example, not a general payload format for every method/source. See [[raw/adyen/api-explorer/a2aissuer-api/latest/post/payments/details/2026-09-15|raw lines 17–35]].
- HTTP 200 requires `details` and `token`. The details must be shown before user confirmation or cancellation and require amount (`currency`, integer minor-unit `value`), recipient `counterparty` (`accountHolder` and `accountIdentification` objects), payment-method-generated `description`, and `expiresAt`. The token identifies this payment for the separate confirm/cancel operations. The field table does not specify nested properties of those two counterparty objects; the example shows `fullName` and an IBAN. See [[raw/adyen/api-explorer/a2aissuer-api/latest/post/payments/details/2026-09-15|raw lines 36–53 and 112–138]].
- The response distinguishes malformed/unexpected-format HTTP 400, validation HTTP 422, and unrecoverable HTTP 500. Error-body parent fields are optional; if `invalidFields` entries are present, their `message`, `name`, and `value` are marked required within each entry. The examples include 422 codes for expired/unavailable payment (`1069_004`), final-state payment (`1069_005`), payment-method unprocessable entity (`1069_006`), and invalid/missing fields (`29_001`); 500 examples include internal and payment-method errors. These examples do not define retry safety or a recovery procedure. See [[raw/adyen/api-explorer/a2aissuer-api/latest/post/payments/details/2026-09-15|raw lines 56–110 and 140–229]].
- The operation's 200 response is successful **retrieval** of an open payment, not user approval, SCA completion, confirm/cancel execution, settlement, or recipient receipt. The separate [[source-adyen-docs-business-accounts-send-funds-ideal-integration|iDEAL A2A integration guide]] describes the platform's later user display and SCA/confirmation flow; its around-15-minute token statement is guide-specific, not an expiry duration specified in this API field table.

## Detail locators

- Versioned test/live servers and required request fields: [[raw/adyen/api-explorer/a2aissuer-api/latest/post/payments/details/2026-09-15|raw lines 5–24]].
- iDEAL redirect request example and 200 success schema: [[raw/adyen/api-explorer/a2aissuer-api/latest/post/payments/details/2026-09-15|raw lines 26–53]].
- 400/422/500 error schemas: [[raw/adyen/api-explorer/a2aissuer-api/latest/post/payments/details/2026-09-15|raw lines 56–110]].
- Success and error response examples: [[raw/adyen/api-explorer/a2aissuer-api/latest/post/payments/details/2026-09-15|raw lines 112–229]].

## Related

- [[adyen-business-accounts]] — issuer-side Business Accounts context.
- [[source-adyen-docs-business-accounts-send-funds-ideal-integration]] — separately sourced iDEAL A2A user and confirmation flow.
- [[adyen]] — provider context.

## Raw Sources

- [[raw/adyen/api-explorer/a2aissuer-api/latest/post/payments/details/2026-09-15|A2A Issuer payment-details API reference (captured 2026-09-15)]]
