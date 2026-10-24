---
title: "Adyen Samsung Pay API-only integration"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/samsung-pay/samsung-pay-api"
raw_files:
  - "adyen/docs/payment-methods/samsung-pay/samsung-pay-api/2026-09-15.md"
tags: [adyen, samsung-pay, wallet, api-only, online-payments]
---

## Overview

This 2026-09-15 Adyen guide describes accepting Samsung Pay through an **existing API-only integration** with a merchant-built payment form. It delegates Samsung-side enablement to a separate guide and Samsung Pay SDK documentation, then describes sending the SDK token to Adyen's Checkout `/payments` endpoint. The page does not document merchant decryption, key custody, a PCI level or token cryptography. It is not proof of current wallet/account eligibility or a successful live payment. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- Before the method-specific flow, the guide says to have an API-only integration and add Samsung Pay in the **test Customer Area**. Preparation is to request a CSR from Adyen, create a Samsung Pay Developer account, set Adyen as payment gateway, integrate the Samsung Pay SDK, and ask Adyen Support to configure compatible **Visa, Mastercard, Maestro, Amex and Discover** schemes on the merchant account. These are setup actions, not proof they occurred or that every scheme is enabled. (raw lines 21–34)
- Show Samsung Pay when its app is available on the shopper's device. Optional `/paymentMethods` discovery takes a supported `countryCode` and `amount.currency`; `GB`/`GBP` are examples, and the response identifies `paymentMethod.type: samsungpay`. This does not establish universal region/currency or device support. (raw lines 36–47)
- When the shopper selects Samsung Pay, obtain tokenized payment information from the Samsung SDK. The merchant **server** sends `paymentMethod.type: samsungpay` and `paymentMethod.samsungPayToken` in `/payments`. The token is the **complete base64-encoded SDK payload**, not just `3DS.data`. The page does not instruct merchants to decrypt it; CSR/gateway/SDK detail is in linked setup materials rather than specified here. (raw lines 49–58)
- The sample API result has `resultCode: Authorised`, but the page's result table also describes `Error` with a `refusalReason` and bank `Refused`. Present the actual response code to the shopper; the illustrated response is not a real authorization, capture, settlement or card-network result. (raw lines 361–385)
- Samsung provides testing guidance, and TEST payment status can be checked in test Customer Area. The guide separately requires a **request for Samsung Pay in live Customer Area before live acceptance**. TEST configuration, sample tokens and response bodies do not establish LIVE method approval or processing. (raw lines 387–393)

## Example qualifications

- The curl snippet targets TEST Checkout API **v68** and includes rendered `{hint:...}` markup in a field name. API-library examples use distinct dated versions and TEST settings, with an additional live endpoint prefix noted for LIVE. The Go comment says v10.4.0 while import paths use `/v9/`. These snippets are illustrative, not a complete verified production request. (raw lines 60–359, especially 63–78 and 230–239)
- The page does not state an API-version minimum, a merchant-side decrypt/PCI classification, or capture/settlement behavior. Do not infer those from the v68 example endpoint, the token payload, or the `Authorised` sample. (raw lines 21–26, 49–78, 361–393)

## Detail locators

- Prerequisites, account/CSR/gateway/SDK/network setup: raw lines 21–34.
- Device check, discovery and server token handoff: raw lines 36–58.
- TEST request/library examples: raw lines 60–359.
- Result codes and test/live boundary: raw lines 361–393.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-samsung-pay]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/samsung-pay/samsung-pay-api/2026-09-15|Adyen Samsung Pay API-only guide, 2026-09-15 snapshot]]
