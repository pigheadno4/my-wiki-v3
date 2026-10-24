---
title: "Adyen PayPay React Native Drop-in"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/paypay/react-native-drop-in"
raw_files:
  - "adyen/docs/payment-methods/paypay/react-native-drop-in/2026-09-15.md"
tags: [adyen, paypay, react-native, drop-in, redirect]
---

## Overview

This 2026-09-15 PayPay guide describes **method-specific additions** to an existing React Native Drop-in integration, separately for Sessions and Advanced server flows. It assumes PayPay is added in Adyen Customer Area and that the base integration handles `action.type: redirect`. It does not replace the base flow's server, SDK, redirect-return, status or credential responsibilities, and it does not prove merchant availability or payment completion. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Sessions branch:** the page specifies an existing Sessions React Native Drop-in integration and **Checkout API v68 or later**. It says no PayPay-specific parameters are needed in `/sessions` and no PayPay-specific client configuration is needed. The 'Sessions flow' integration-type link visibly points to an **Advanced-flow** URL, while its redirect and session links point to Sessions; follow the actual flow-specific guide rather than treating that link as an instruction to change flows.
- **Advanced branch:** the page specifies an existing Advanced React Native Drop-in integration with redirect handling and Customer Area setup. It says no additional PayPay-specific client configuration or `/payments` parameters are needed. The base request, payment-method selection, action handling and final-state verification remain governed by the existing integration, which this add-on does not restate. The page lists no separate Advanced-branch API minimum; do not import the Sessions-only v68 statement into it.
- **TEST:** both branches list `DGFT_AcquirerAccount_Adyen_closedLoop_AUTHFlow` and `DGFT_AcquirerAccount_Adyen_closedLoop_SALEFlow` as test acquirer accounts. The page says the shopper is redirected to a DGFT simulator and does not need the PayPay app; it points to Adyen TEST Customer Area payment list for inspecting test transaction status. Simulator completion or a list entry is not live authorization/capture/settlement proof.
- **LIVE:** both branches state that the integration requires access to an **activated PayPay smartphone app through a Japan local IP address**. This condition and the TEST simulator path are distinct; neither establishes a currently eligible merchant, successful redirect return or real payment.

## Detail locators

- Add-on scope and server-flow split: raw lines 19–25. Sessions requirements, v68 gate, redirect and setup: raw lines 29–36. Sessions link mismatch: raw line 33. No method-specific `/sessions`/configuration additions: raw lines 38–48.
- Sessions TEST simulator/accounts and LIVE app/IP condition: raw lines 50–61. Advanced requirements and no method-specific config/payment parameters: raw lines 63–85. Advanced TEST/LIVE repetition: raw lines 87–98.

## Related

- [[adyen-online-payments]] — parent payment-flow and outcome context.
- [[adyen-react-native-sdk]] — cross-platform wrapper, base Sessions/Advanced and native redirect integration context.
- [[source-adyen-docs-payment-methods-paypay]] — PayPay overview; region/currency and capability matrix belong to that separate source.

## Raw Sources

- [[raw/adyen/docs/payment-methods/paypay/react-native-drop-in/2026-09-15|PayPay React Native Drop-in guide, captured 2026-09-15]]
