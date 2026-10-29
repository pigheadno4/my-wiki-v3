---
title: "Adyen Alma React Native Drop-in"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/alma/react-native-drop-in"
raw_files:
  - "adyen/docs/payment-methods/alma/react-native-drop-in/2026-09-15.md"
tags: [adyen, alma, react-native, drop-in, online-payments, installments]
---

## Overview

This captured [[adyen]] guide adds Alma to an **existing React Native Drop-in** integration. It divides method-specific additions between Sessions and Advanced server-side flows, including request fields, redirect handling and test/live setup. Its FR/EUR payloads and Advanced redirect response are examples, not live eligibility or payment-result evidence. [[adyen-online-payments]]

## Key takeaways

- **Prerequisites and link mismatch:** Sessions requires an existing React Native Drop-in Sessions flow, Checkout API v68 or later, redirect handling for `action.type: redirect`, and Alma added in Customer Area. The Sessions requirement's link labelled “Sessions flow React Native Drop-in integration” points to an `advanced-flow` URL, while its redirect and session-creation links point to Sessions. Advanced requires an existing Advanced Drop-in flow, redirect handling and Customer Area setup; its table does not repeat the v68 minimum (raw lines 25–42, 99–109). The mismatched Sessions link does not change the section's flow identity.
- **Additional fields and requiredness:** The Sessions `/sessions` table lists `telephoneNumber`, `shopperEmail`, `billingAddress` and `deliveryAddress`, all with blank Required cells. The Advanced `/payments` table repeats them and adds `additionalData.alma.installments_count`, likewise with blank Required status: set to `3` or `4` to determine installment count or omit to let the shopper choose. Do not promote blank table cells or example values to universal requirements (raw lines 40–84, 119–168).
- **Drop-in configuration:** Both sections explicitly say no additional Alma configuration parameters are needed (raw lines 87–91, 111–115).
- **Redirect and return examples:** The Advanced response example uses `resultCode: RedirectShopper` and `action.type: redirect`; this is an intermediate action, not completed authorization or settlement. The Sessions example uses a custom-scheme `returnUrl`, whereas Advanced shows HTTPS; the examples do not state a flow-specific URL-scheme rule (raw lines 65–67, 145–148, 171–185).
- **Test/live gate:** The page routes test-payment status checks to Customer Area and says to submit a request for Alma in live Customer Area before accepting live payments (raw lines 93–97, 187–191).

## Detail locators

- Add-on identity, Sessions prerequisites and link mismatch: pinned raw lines 15–36.
- Sessions additional fields, FR/EUR request example, no-extra-config and test/live: pinned raw lines 38–97.
- Advanced requirements, field table, optional installments and examples: pinned raw lines 99–185.
- Advanced test status and live request: pinned raw lines 187–191.

## Related

- [[adyen-online-payments]] — online payment architecture and method routes.
- [[source-adyen-docs-payment-methods-alma]] — Alma method overview.

## Raw Sources

- [[raw/adyen/docs/payment-methods/alma/react-native-drop-in/2026-09-15|Alma React Native Drop-in, captured 2026-09-15]]
