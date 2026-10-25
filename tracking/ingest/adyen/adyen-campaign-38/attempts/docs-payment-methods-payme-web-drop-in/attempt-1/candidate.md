---
title: "Adyen PayMe Web Drop-in integration guide"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/payme/web-drop-in"
raw_files:
  - "adyen/docs/payment-methods/payme/web-drop-in/2026-09-15.md"
tags: [adyen, payme, web, drop-in, qr, redirect]
---

## Overview

This 2026-09-15 Adyen guide adds PayMe to an existing Web Drop-in integration. Drop-in shows a QR code for desktop/laptop shoppers and redirects mobile-browser shoppers to the PayMe app; the page instructs integrators to implement both device flows. It states PayMe support from Web Drop-in 5.56.0. The guide's TEST examples and simulator results are not proof of a real or live payment. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- For Sessions or Advanced, the page requires the corresponding existing Web Drop-in flow and PayMe added in the Customer Area. For Web Drop-in v6, it shows importing `AdyenCheckout` and `PayMe`. Its API reference calls `/sessions` the default with Drop-in v5.0.0 or later and presents `/payments` for an additional use case; this generic default/version statement does not supersede the PayMe-specific 5.56.0 minimum.
- The API-reference tables for both endpoints list `channel` to distinguish desktop/laptop/mobile and `lineItems` subfields, including `lineItems.sku` only with Checkout API v70+. Their “Required” cells are blank; do not turn those listed fields into required PayMe properties. See the pinned raw for quantity, length, and amount bounds.
- The desktop and mobile example sections both show TEST `/payments` requests with `paymentMethod.type: payme` and HK/HKD example values. The mobile curl sample uses `channel: Web`, while its Node sample uses the literal `Web/iOS/Android`; that difference and the sample's platform label should not be normalized into a single verified mobile channel value. The samples also use string `"1"` for quantity although the table describes quantity as a number. No PayMe-specific Drop-in configuration step is stated. The page points to the main Web Drop-in guide for obtaining and showing the payment outcome.
- The PayMe sandbox can test without the PayMe app. Amount endings 30/81 simulate `Authorised`, 77/90 simulate `OfferCancelled` after PayMe's stated default ten-minute expiry, and 40/44 simulate `Error` when creating the request. These are simulator outcomes only.

## Detail locators

- QR/app routing and PayMe-specific Drop-in minimum: pinned raw lines 19–30; flow prerequisites: lines 32–48; v6 import: lines 50–56.
- Endpoint choice and parameter tables: lines 58–86; desktop/mobile TEST request examples and sample conflict: lines 88–226; outcome-guide route and configuration: lines 228–232.
- Sandbox testing and result table: lines 234–244.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-payme]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/payme/web-drop-in/2026-09-15|PayMe Web Drop-in, 2026-09-15]]
