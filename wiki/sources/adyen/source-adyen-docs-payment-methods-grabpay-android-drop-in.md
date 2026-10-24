---
title: "GrabPay Android Drop-in integration"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/grabpay/android-drop-in"
raw_files:
  - "adyen/docs/payment-methods/grabpay/android-drop-in/2026-09-15.md"
tags: [adyen, grabpay, android, drop-in, online-payments]
---

## Overview

This 2026-09-15 guide explains how to add GrabPay to an existing Android Drop-in integration for the v5.0.0 guide path, with separate Sessions and Advanced server-side flows. Earlier versions are routed to a different guide. This page is method-specific setup documentation, not a record of a successful payment. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Versioned prerequisites:** both Sessions and Advanced tabs require an existing Android Drop-in integration at minimum version 5.0.0 and GrabPay added in Customer Area. The page labels itself for v5.0.0, released in October 2023, and links earlier versions elsewhere; it does not state a higher SDK or Checkout API minimum. (raw lines 19–39)
- **Flow additions:** the Sessions tab says no GrabPay-specific fields are required on `/sessions`; the Advanced tab says the same for `/payments`. Neither tab requires extra GrabPay Drop-in configuration. The page then points Sessions to creating the checkout session and Advanced to launching and showing Drop-in in the linked main integration guides. These are page-specific add-ons, not complete request contracts or outcome procedures. (raw lines 41–67)
- **Test and live gates:** the page says to contact Adyen Support for test wallet credentials, log in to Grab in a simulator using the registered phone number and received one-time password, and check test payment status in Customer Area. For live acceptance, it says to request GrabPay in the live Customer Area. Documented setup and a status-check location do not demonstrate actual test or live transaction success. (raw lines 69–78)
- **Scope limit:** this v5 guide does not distinguish GrabPay Wallet from PayLater, specify supported countries/currencies, or describe shopper return, webhook finalization, tokenization, capture or refund behavior. Its See also links are navigation, not authority for those details. (raw lines 15–85)

## Detail locators

- v5.0.0 guide scope and earlier-version route: raw lines 19–21.
- Sessions and Advanced Android Drop-in requirements: raw lines 23–39.
- Request fields, Drop-in configuration and flow continuations: raw lines 41–67.
- Test credentials, simulator, status location and live request: raw lines 69–78.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-grabpay-android-drop-in-earlier-versions|Earlier-version Android Drop-in guide]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/grabpay/android-drop-in/2026-09-15|Adyen GrabPay Android Drop-in guide, 2026-09-15 snapshot]]
