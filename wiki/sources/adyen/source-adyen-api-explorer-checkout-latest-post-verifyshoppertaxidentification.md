---
title: "Adyen Checkout API v72 POST /verifyShopperTaxIdentification"
type: source
date_ingested: 2026-11-02
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Checkout/latest/post/verifyShopperTaxIdentification"
raw_files:
  - "adyen/api-explorer/Checkout/latest/post/verifyShopperTaxIdentification/2026-11-02.md"
tags: [adyen, checkout-api, online-payments, tax-identification]
---

## Overview

This 2026-11-02 capture is [[adyen]]'s Checkout API v72 TEST reference for `POST /verifyShopperTaxIdentification`. The endpoint submits a shopper's tax identification for verification where collecting and verifying tax information is required for regulatory compliance. On successful verification, it returns an opaque token for submission in `/payments`. The listed server is `https://checkout-test.adyen.com/v72`; the `latest` URL does not establish current version, live availability or merchant eligibility.

## Key takeaways

- The request-body table marks `merchantAccount`, `shopperReference` and `shopperTaxIdentification` **Yes**, along with nested `taxCountryCode`, `taxIdentificationNumber` and `taxIdentificationType`. `shopperReference` is the merchant's unique shopper reference, binds verification to that shopper context, and must exclude PII such as name or email. The table gives required *properties*; it does not separately state whole-body requiredness (raw lines 12–22).
- Initially only `IN` is supported for `taxCountryCode` and `PAN` for `taxIdentificationType`. No default, numeric limit or idempotency contract is specified in this captured endpoint page (raw lines 19–22).
- HTTP `200 Success` says the request succeeded, while `result` is optional and may, for example, be `valid` or `invalid`. Optional fields include `reason`, `reasonCode`, `taxVerificationReference`, a masked `verifiedShopperTaxIdentification` object and `verifiedShopperTaxIdentificationToken`. The token represents successful verification and is required in `/payments`; a 200 response alone does not establish a valid result or guarantee a token (raw lines 24–40).
- The page lists 400 request-reading, 401 authentication, 403 permissions, 422 validation and 500 server errors, with their response fields at raw lines 43–105. It specifies no deletion, propagation, asynchronous outcome, reversal or downstream payment result contract. Verification and token handoff do not themselves establish payment authorization, capture, settlement or live eligibility.

## Detail locators

- Purpose, endpoint and TEST v72 server: raw lines 5–10.
- Request identities, required property markers and initial country/type scope: raw lines 12–22.
- Success response, optional result and token: raw lines 24–40.
- Error status descriptions and schemas: raw lines 43–105.

## Related

- [[adyen-online-payments]] — Checkout API integration context.

## Raw Sources

- [[raw/adyen/api-explorer/Checkout/latest/post/verifyShopperTaxIdentification/2026-11-02|POST /verifyShopperTaxIdentification reference, captured 2026-11-02]]