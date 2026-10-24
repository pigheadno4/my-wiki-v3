---
title: "Adyen PayPay Android Drop-in"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/paypay/android-drop-in"
raw_files:
  - "adyen/docs/payment-methods/paypay/android-drop-in/2026-09-15.md"
tags: [adyen, paypay, android, drop-in, redirect]
---

## Overview

This 2026-09-15 PayPay page gives **method-specific additions** for existing Android Drop-in integrations in either Sessions or Advanced server flow. The prerequisite is adding PayPay in Adyen Customer Area. The page does not replace the corresponding base Android integration's server request, action/return, SDK and final-result handling, and does not establish live merchant eligibility or payment completion. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Sessions:** requires an existing Android Sessions Drop-in integration and **Checkout API v68 or later**. It says there are no additional PayPay-specific `/sessions` request parameters or client configuration parameters. The Sessions branch does not separately list a redirect-handling requirement, although its TEST description says the shopper is redirected to a simulator; keep that distinct from the Advanced branch's explicit `action.type: redirect` prerequisite.
- **Advanced:** requires an existing Android Advanced Drop-in integration, `action.type: redirect` handling and PayPay Customer Area setup. It says no additional PayPay-specific configuration or `/payments` request parameters. Its section does not state a separate Checkout API version minimum, so the Sessions-only v68 gate should not be applied to it without independent authority. In both branches 'no additional' concerns this method add-on, not all fields or server work in the base flow.
- **TEST:** each branch names `DGFT_AcquirerAccount_Adyen_closedLoop_AUTHFlow` and `DGFT_AcquirerAccount_Adyen_closedLoop_SALEFlow` as acquirer accounts in the TEST environment. The shopper is redirected to a DGFT simulator and does not need the PayPay app; the page points to Adyen TEST Customer Area's Payment list for inspecting test status. Neither a simulator path nor a displayed status proves a live authorization, capture or settlement.
- **LIVE:** each branch says the integration must access an **activated PayPay smartphone app through a Japan local IP address**. The LIVE gate is distinct from the TEST simulator and is not evidence that a particular device/account/merchant currently qualifies or has completed a payment.

## Detail locators

- Add-on scope and server-flow split: raw lines 19–25. Sessions integration/API v68 gate and Customer Area step: raw lines 29–34. No PayPay-specific Sessions request/configuration additions: raw lines 36–46.
- Sessions TEST acquirer/simulator/status and LIVE condition: raw lines 48–61. Advanced integration, redirect and Customer Area prerequisites: raw lines 63–71. No PayPay-specific Advanced configuration/payment fields: raw lines 73–83. Advanced TEST/LIVE repetition: raw lines 85–96.

## Related

- [[adyen-online-payments]] — parent server-flow and outcome context.
- [[adyen-android-sdk]] — native Android Drop-in and action-handling context.
- [[source-adyen-docs-payment-methods-paypay]] — PayPay overview for separate country/currency and capability matrix.

## Raw Sources

- [[raw/adyen/docs/payment-methods/paypay/android-drop-in/2026-09-15|PayPay Android Drop-in guide, captured 2026-09-15]]
