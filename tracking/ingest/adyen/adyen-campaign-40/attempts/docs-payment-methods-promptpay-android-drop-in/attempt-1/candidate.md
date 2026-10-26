---
title: "Adyen PromptPay Android Drop-in guide"
type: source
date_ingested: 2026-10-26
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/promptpay/android-drop-in"
raw_files:
  - "adyen/docs/payment-methods/promptpay/android-drop-in/2026-09-15.md"
tags: [adyen, promptpay, android, drop-in, sessions, advanced]
---

## Overview

This 2026-09-15 Adyen page describes adding PromptPay to an existing **Android Drop-in** integration in Sessions or Advanced server-side flow. It covers method setup, extra-field and configuration requirements, and test/live routing. It does not describe the PromptPay QR action, shopper completion, expiry or webhook outcome sequence; use the linked main integration and method-specific evidence for those details. This captured page does not prove present account enablement or an executed payment. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- **Prerequisites:** Sessions requires an existing Android Drop-in Sessions integration; Advanced requires the corresponding Advanced integration. Both requirements tables say to add PromptPay in Customer Area before beginning. They do not state an Android SDK or Checkout API minimum here. (raw lines 21–37)
- **Method additions:** PromptPay requires no additional `/sessions` fields in Sessions or `/payments` fields in Advanced, and no additional Drop-in configuration in either flow. This is limited to PromptPay-specific additions, not a waiver of the main flow's ordinary request/configuration requirements. (raw lines 39–57)
- **Testing and live gate:** the page instructs testing with real payment details and small amounts and checking status in the TEST Customer Area. To accept live PromptPay, it says contact Support to add the method in the **live** Customer Area. These are instructions, not evidence of a test payment or live enablement. (raw lines 59–65)

## Detail locators

- Android Drop-in identity and Sessions/Advanced setup: pinned raw lines 15–37.
- No PromptPay-specific API fields or Drop-in configuration: pinned raw lines 39–57.
- TEST guidance, LIVE Support gate and main-guide/webhook navigation: pinned raw lines 59–71.

## Related

- [[adyen-online-payments]] — main provider integration and outcome context
- [[source-adyen-docs-payment-methods-promptpay]] — method overview and QR scope

## Raw Sources

- [[raw/adyen/docs/payment-methods/promptpay/android-drop-in/2026-09-15|PromptPay Android Drop-in guide, 2026-09-15]]
