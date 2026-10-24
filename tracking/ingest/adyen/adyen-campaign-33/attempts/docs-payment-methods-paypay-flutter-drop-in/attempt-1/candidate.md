---
title: "Adyen PayPay Flutter Drop-in guide"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/paypay/flutter-drop-in"
raw_files:
  - "adyen/docs/payment-methods/paypay/flutter-drop-in/2026-09-15.md"
tags: [adyen, paypay, flutter, drop-in, redirect]
---

## Overview

This [[adyen]] guide gives **PayPay-specific additions** to an existing **Flutter Drop-in** integration, separately for Sessions and Advanced server-side flows. It routes the shopper through a redirect, with different TEST simulator and LIVE PayPay-app conditions. It does not itself establish current merchant enablement, a completed shopper return, authorization, capture or settlement. [[adyen-online-payments]]

## Key takeaways

- **Sessions flow:** The page requires an existing Sessions Flutter Drop-in integration, **Checkout API v68 or later**, PayPay added in Customer Area, and existing redirect handling for `action.type: redirect`. It says no additional PayPay-specific `/sessions` parameters or Drop-in configuration are needed. These statements do not waive the main Sessions request/return flow. See raw lines 23–48.
- **Advanced flow:** The page requires an existing Advanced Flutter Drop-in integration, PayPay added in Customer Area, and existing redirect handling for `action.type: redirect`. It says no additional PayPay-specific `/payments` parameters or Drop-in configuration are needed. The Advanced requirement table does **not** restate the Sessions table's v68+ minimum. See raw lines 63–85.
- **TEST versus LIVE:** For TEST, the guide lists `DGFT_AcquirerAccount_Adyen_closedLoop_AUTHFlow` and `DGFT_AcquirerAccount_Adyen_closedLoop_SALEFlow`; the shopper is redirected to a **DGFT simulator**, with no PayPay app needed. It directs merchants to TEST Customer Area Payment list for test status. For LIVE integration, it says an **activated PayPay smartphone app** must be accessed through a **Japan local IP address**. The AUTHFlow/SALEFlow names and simulator redirect do not establish a final authorization or sale outcome. See raw lines 50–61 and 87–98.

> [!warning] Contradiction
> The **Sessions** requirement row labels an existing Sessions Flutter Drop-in integration but links to an **Advanced-flow** URL (raw line 33); the following Sessions redirect and session-creation links point to Sessions-flow URLs (raw lines 35 and 42). Treat that requirement link as mismatched navigation, not a change to the stated Sessions prerequisite.

## Detail locators

- Flow split, Sessions requirement and no-extra-parameters/configuration statements: raw lines 23–48.
- Sessions TEST simulator and LIVE app/Japan-IP conditions: raw lines 50–61.
- Advanced requirement and no-extra-parameters/configuration statements: raw lines 63–85.
- Advanced repeated TEST/LIVE conditions: raw lines 87–98.
- This page does not provide a currency rule, final webhook contract, refund procedure or post-redirect payment lifecycle; use the appropriate linked main guide and specific PayPay overview for those separate questions.

## Related

- [[adyen-online-payments]]
- [[adyen]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/paypay/flutter-drop-in/2026-09-15|Adyen PayPay Flutter Drop-in snapshot]]
