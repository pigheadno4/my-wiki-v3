---
title: "Adyen Boost Wallet iOS Drop-in guide"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/boost/ios-drop-in"
raw_files:
  - "adyen/docs/payment-methods/boost/ios-drop-in/2026-09-15.md"
tags: [adyen, boost-wallet, ios, drop-in, redirect, online-payments]
---

## Overview

This 2026-09-15 Adyen page describes **Boost Wallet-specific additions** to an existing iOS Drop-in integration, split into Sessions and Advanced flows. It supplies prerequisites and method-addition statements, not a full shopper redirect/return procedure or evidence of an authorized payment. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Sessions route:** The page requires an existing iOS Sessions-flow Drop-in integration using **Checkout API v68 or later** and Boost Wallet added in Customer Area. It says no Boost-specific `/sessions` parameters or Drop-in configuration are needed. These are additions to the base integration, not a waiver of ordinary session creation or merchant setup. (raw lines 25–46)
- **Advanced route:** The Advanced section requires an existing iOS Drop-in integration, Boost Wallet in Customer Area and redirect handling for **`action.type: redirect`**. It says no additional Boost Wallet configuration or `/payments` parameters are needed. It does not separately state the Sessions-row API-version minimum. A redirect action is not a final result, and this page does not document the returned status or webhook lifecycle. (raw lines 54–76)
- **Environment warning:** Both sections say **no Boost Wallet test environment is available** and direct penny testing in the **live environment**. This is a consequential financial-operation warning from the source; it is not an instruction to run a real-money test, evidence of merchant eligibility or proof of a payment outcome. (raw lines 48–52, 78–82)

## Detail locators

- Sessions v68+ and Customer Area prerequisites: raw lines 25–34.
- Sessions no-extra fields/configuration: raw lines 36–46.
- Advanced redirect and Customer Area prerequisites: raw lines 54–64.
- Advanced no-extra configuration/request fields: raw lines 66–76.
- No TEST environment and live penny-test statement: raw lines 48–52, 78–82.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-boost]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/boost/ios-drop-in/2026-09-15|Adyen Boost Wallet iOS Drop-in, 2026-09-15 snapshot]]
