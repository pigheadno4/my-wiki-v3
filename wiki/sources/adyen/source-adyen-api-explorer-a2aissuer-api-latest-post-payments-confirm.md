---
title: "Adyen A2A Issuer API v1: confirm payment"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/a2aissuer-api/latest/post/payments/confirm"
raw_files:
  - "adyen/api-explorer/a2aissuer-api/latest/post/payments/confirm/2026-09-15.md"
tags: [adyen, business-accounts, a2a, ideal, sca]
---

## Overview

This 2026-09-15 API Explorer snapshot documents A2A Issuer API v1 `POST /payments/confirm` on test and live balance-platform hosts. It confirms an account-to-account payment using Strong Customer Authentication (SCA), with two calls around a user challenge. The linked Business Accounts iDEAL guide supplies the integration context; this is not a merchant Checkout API authorization or an Issuing card-payment endpoint. [[adyen]] [[adyen-business-accounts]]

## Key takeaways

- The page says to call confirm first to initiate SCA and receive a `WWW-Authenticate` header, then call it again after the user completes the challenge with an updated header. The second response supplies a URL guiding the user to a success or failure page (raw lines 7–16). The header parameter table nevertheless marks `WWW-Authenticate` optional; do not turn that table into a universally required header on both calls (raw lines 28–31). The linked iDEAL integration guide describes SDK output and a 10-minute challenge window separately.
- The request body requires `balanceAccountId` for the account from which funds should be subtracted and `token`, the payment identifier returned by payment details. The example supplies both; it does not include the header or demonstrate a completed SCA exchange (raw lines 34–48).
- HTTP 200 is labeled a succeeded request. Its `links` response object is required, but `links.cancel` and `links.success` are optional; each nested `href` is marked required when that branch object is present. The response example contains only `links.success.href` (raw lines 49–61, 139–152). A redirect URL or request success is not independent proof of funds movement or recipient receipt.
- Listed errors are 400 malformed request, 401 invalid credential/permissions, 422 validation, and 500 server error. The 401 example says the user needs SCA, so the generic 401 description and that example have different scopes; do not reduce every 401 to one cause. The 422 examples include invalid challenge, invalid or expired token, final-state payment, payment-method error, missing/invalid fields, and unknown balance account. A final-state error says this request cannot process that payment, not what the final outcome was (raw lines 64–138, 154–301).
- This captured operation does not state that a 200 response proves settlement, a booked debit, beneficiary credit, or bank receipt. It gives no retry-safety or idempotency contract; the final-state/expired examples caution against assuming another confirm can be repeated safely (raw lines 195–226).

## Detail locators

- Two-call SCA sequence, redirect boundary and v1 hosts: raw lines 5–25.
- Optional header; required request body and example: raw lines 26–48.
- 200 response requiredness and conditional link fields: raw lines 49–61; example lines 139–152.
- Error schemas: raw lines 64–138. Error examples and exact codes: raw lines 154–301.

## Related

- [[adyen-business-accounts]] — product/account context and reciprocal route.
- [[source-adyen-docs-business-accounts-send-funds-ideal-integration]] — separate iDEAL A2A issuer flow, SCA SDK timing and redirect requirements.
- [[source-adyen-docs-business-accounts-how-sca-works]] — separate Business Accounts SCA challenge guidance.

## Raw Sources

- [[raw/adyen/api-explorer/a2aissuer-api/latest/post/payments/confirm/2026-09-15|A2A Issuer confirm-payment API capture]]
