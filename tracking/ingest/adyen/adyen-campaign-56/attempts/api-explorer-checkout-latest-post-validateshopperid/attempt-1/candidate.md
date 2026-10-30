---
title: "Adyen Checkout API v72 POST /validateShopperId"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Checkout/latest/post/validateShopperId"
raw_files:
  - "adyen/api-explorer/Checkout/latest/post/validateShopperId/2026-09-15.md"
tags: [adyen, checkout-api, online-payments, shopper-validation]
---

## Overview

This 2026-09-15 capture is the Checkout API **v72** reference for `POST /validateShopperId`, described as validating a shopper ID. It belongs to [[adyen]]'s [[adyen-online-payments]] API. Its listed server is `https://checkout-test.adyen.com/v72`; the `latest` URL does not establish a later current version or live availability.

## Key takeaways

- The request-body table marks `merchantAccount`, `paymentMethod`, and nested `paymentMethod.type` **Yes**. It marks `shopperEmail`, `shopperIP`, and `shopperReference` **No** (raw lines 12–22). This table identifies required *properties*; the page does not separately state whether the whole body is required.
- The title and summary say “shopper Id”/`shopperId`, while the shown request table has optional `shopperReference` and no `shopperId` field (lines 5–7, 17–22). The captured reference does not explain that mismatch or define the identity-validation mechanism; use its field table as the locator rather than assuming `shopperReference` is mandatory.
- A `200 Success` means the request succeeded. Its optional response fields are `reason` and `result`; the latter's description gives `valid`, `invalid`, and `unknown` as examples (lines 24–33). A 200 alone does not assert `valid`, payment authorization, or general identity verification. The page also lists 400 request-reading, 401 authentication, 403 permission, 422 request-validation, and 500 server errors (lines 36–98).

## Detail locators

- Method, summary, captured test server: raw lines 5–10.
- Request property table and requiredness: raw lines 12–22.
- Success and error response tables: raw lines 24–98.

## Related

- [[adyen-online-payments]] — provider concept and online integration context.

## Raw Sources

- [[raw/adyen/api-explorer/Checkout/latest/post/validateShopperId/2026-09-15|POST /validateShopperId reference, captured 2026-09-15]]
