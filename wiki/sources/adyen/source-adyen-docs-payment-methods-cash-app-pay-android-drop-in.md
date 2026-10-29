---
title: "Cash App Pay Android Drop-in integration"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/cash-app-pay/android-drop-in"
raw_files:
  - "adyen/docs/payment-methods/cash-app-pay/android-drop-in/2026-09-15.md"
tags: [adyen, cash-app-pay, android, drop-in, payment-results]
---

## Overview

This 2026-09-15-captured Adyen page adds **Cash App Pay** to an existing **Android Drop-in** integration. It is explicitly for **v5.0.0**, released in October 2023, and routes earlier versions to a separate guide. It covers Sessions and Advanced setup, payment-result handling, tokenization at overview level, and test/live steps. Cash App Pay is distinct from Cash App Afterpay. This page is not a complete base integration, proof of current account entitlement, or evidence of a live payment. See [[adyen]], [[adyen-online-payments]], and the [[source-adyen-docs-payment-methods-cash-app-pay|method overview]] for its separate captured US/USD capability context.

## Key takeaways

- **Version and prerequisites:** For both Sessions and Advanced, the page requires an existing Android Drop-in integration at **v5.0.0 or later** and Cash App Pay added in Customer Area. It directs users of earlier versions to the separate earlier-versions guide. The page does not state a minimum Checkout API version. [Raw: lines 14–36]
- **Method-specific add-on:** Cash App Pay needs no additional fields for the /sessions or /payments request and no additional Drop-in configuration in the corresponding flow. These are method-specific additions to an existing base integration, not permission to omit base request or Drop-in setup. Sessions then creates the checkout session; Advanced launches Drop-in. [Raw: lines 38–64]
- **Outcome handling:** Use the /payments/details response resultCode to show the shopper a result, and receive payment outcome asynchronously by webhook. **Received** says the shopper completed the payment step but the final result is not known; inform the shopper that payment is pending and wait for the AUTHORISATION webhook update. **Authorised** is successful according to the table, but manual capture still needs a separate capture. **Cancelled**, **Error**, and **Refused** have different shopper guidance; Error and Refused point to refusalReason for diagnosis. Do not treat Received as authorization or Authorised as completed manual capture. [Raw: lines 66–78]
- **Stored details and environments:** The guide says Cash App Pay supports tokenization for future recurring/card-on-file payments and says shopper permission at token creation can bypass shopper approval for later uses. It **strongly recommends** explicit permission, and transparency about recurring schedule and amount. This section gives no Android token-creation request recipe. Testing uses the test environment and Cash App Pay magic values; live use requires adding Cash App Pay in the live Customer Area. The test instruction is not proof of a real transaction or current live setup. [Raw: lines 80–90]

## Detail locators

- Page/version scope, both server-flow prerequisites: pinned raw lines 14–36.
- No extra method request fields/configuration and base-flow navigation: pinned raw lines 38–64.
- /payments/details, asynchronous webhook and resultCode table: pinned raw lines 66–78.
- Tokenization and permission guidance, test/live setup: pinned raw lines 80–90.
- Method-level US/USD capability and conditional adjustment/chargeback context: [[source-adyen-docs-payment-methods-cash-app-pay]] and its pinned raw; this entry's raw_files remains child-only.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-cash-app-pay]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/cash-app-pay/android-drop-in/2026-09-15|Cash App Pay Android Drop-in guide, captured 2026-09-15]]
