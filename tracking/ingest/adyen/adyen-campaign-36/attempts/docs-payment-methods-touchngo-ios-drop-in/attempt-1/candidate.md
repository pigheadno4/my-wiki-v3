---
title: "Adyen Touch'n Go iOS Drop-in add-on"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/touchngo/ios-drop-in"
raw_files:
  - "adyen/docs/payment-methods/touchngo/ios-drop-in/2026-09-15.md"
tags: [adyen, touchngo, ios, drop-in, online-payments]
---

## Overview

This 2026-09-15 Adyen page is a short **Touch'n Go add-on for an existing iOS Drop-in** integration. It separates Sessions and Advanced base-flow prerequisites and gives method-specific field/configuration and TEST/live setup notes. It does not document the shopper redirect, `/payments/details` return, webhooks or a final payment result on this page. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Base flows and Support setup:** The Sessions tab requires an existing iOS Drop-in Sessions integration; the Advanced tab requires an existing iOS Drop-in Advanced integration. Both tell the merchant to contact Adyen Support to add Touch'n Go in Customer Area before beginning. This is setup guidance, not evidence of enablement for a particular merchant. (raw lines 21–37)
- **API fields and versions:** The page says no additional Touch'n Go fields are required. It routes to `/sessions` as the default with **iOS Drop-in v5.0.0 or later** and to `/payments` for an additional use case. The v5.0.0 qualifier is a **Drop-in version**, not a Checkout API minimum. Optional generic fields are left to the linked endpoint references. (raw lines 39–44)
- **Drop-in configuration:** Both v5.0.0-or-later and v4.x.x tabs say no Touch'n Go-specific Drop-in integration is required. This does not remove the Sessions/Advanced base integration, Support setup or any redirect/result handling described by separate authority. (raw lines 46–54)
- **TEST/live boundary:** The page directs test-payment status checks to the test Customer Area and says live acceptance requires a separate Support request to add Touch'n Go in the **live Customer Area**. The status-list link and setup requirement do not establish that any payment was authorized, captured or settled. (raw lines 56–60)

## Detail locators

- Sessions/Advanced base-flow and Support prerequisites: raw lines 21–37.
- No extra method fields, `/sessions` default and Drop-in v5.0.0 qualifier: raw lines 39–44.
- Version-tab no-specific-configuration statements: raw lines 46–54.
- Separate test-status and live-Support steps: raw lines 56–60.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-touchngo]]
- [[source-adyen-docs-payment-methods-touchngo-ios-component]]
- [[source-adyen-docs-payment-methods-touchngo-api-only]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/touchngo/ios-drop-in/2026-09-15|Adyen Touch'n Go iOS Drop-in, 2026-09-15 snapshot]]
