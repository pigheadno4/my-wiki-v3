---
title: "Adyen Classic API gift-card payments"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments/classic-integrations/classic-api-integration/classic-gift-cards"
raw_files:
  - "adyen/docs/online-payments/classic-integrations/classic-api-integration/classic-gift-cards/2026-09-15.md"
tags: [adyen, online-payments, classic-api, gift-cards, stored-value]
---

## Overview

This 2026-09-15 snapshot explains gift-card payment requests for an **existing API-only Classic Payment API integration**. The `/authorise` endpoint is marked inactive and unsupported for new integrations; Adyen directs new builds to Checkout API and existing users to contact Adyen about migration. The page metadata says last modified in 2021. Its named Givex, SVS, Fiserv/ValueLink and local-provider support is dated documentation, not proof of current provider, merchant-account, card, currency or transaction eligibility.

## Key takeaways

- This Classic route processes **gift-card payments** using `/authorise`. The guide names Givex, SVS, Fiserv (formerly ValueLink), and some local gift-card providers, while saying the latter support payment processing but no other transactions. It sends issuing, balance checks and deactivation as separate stored-value operations to the JSON-only Stored Value API. See the opening section and `Next steps`.
- The payment request supplies amount currency/value in minor units, gift-card expiry and number, a merchant payment reference, and `selectedBrand`; cardholder name and PIN/security code (`card.cvc`) are optional in this page's field list. The JSON/SOAP examples show additional context such as `merchantAccount` but do not establish every field's requiredness. See `Make a payment`, request fields and examples.
- A Classic `/authorise` request with `amount.value` **0** returns `additionalData.currentBalanceValue`, a remaining-balance field. Treat this as the page's specific zero-value response behavior, distinct from redeeming a nonzero amount or from the separate Stored Value API balance-check route. Do not infer a successful payment from a balance field. See `Make a payment`, amount bullet, and `Next steps`.
- For a payment response, `resultCode` communicates the payment result, `pspReference` identifies the payment, and `authCode` holds an authorization code only when the payment is successfully authorized; otherwise `authCode` is empty. The shown `Authorised` JSON is an example, not a guaranteed outcome. See `Response` and its link to other possible `/authorise` response codes.

## Detail locators

- `Make a payment`, field list and JSON/SOAP examples: request shape, minor units, optional fields, gift-card brand and merchant-account example.
- `Response`: conditional `resultCode`, `pspReference`, `authCode`, sample successful response, and Payment API response-reference link.
- `Next steps`: Stored Value API route for other gift-card operations, including separate balance-check guidance.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[adyen-pos-gift-cards]] — distinct in-person Terminal API scope

## Raw Sources

- [[raw/adyen/docs/online-payments/classic-integrations/classic-api-integration/classic-gift-cards/2026-09-15|Adyen Classic gift-card guide, 2026-09-15 snapshot]]
