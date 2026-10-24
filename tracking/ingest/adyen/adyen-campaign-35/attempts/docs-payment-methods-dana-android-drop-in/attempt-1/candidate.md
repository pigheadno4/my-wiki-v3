---
title: "DANA Android Drop-in integration"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/dana/android-drop-in"
raw_files:
  - "adyen/docs/payment-methods/dana/android-drop-in/2026-09-15.md"
tags: [adyen, dana, android, drop-in, recurring]
---

## Overview

This 2026-09-15 Adyen guide describes adding **DANA** to an existing **Android Drop-in** integration through Sessions or Advanced flow. It covers method-specific request/configuration scope, a separate recurring-token sequence, and TEST/live directions. The page documents steps and examples, not an observed authorization, settlement, token charge or live-account approval. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Sessions base:** the page requires an existing Sessions-flow Android Drop-in integration using **Checkout API v68 or later** and DANA added in Customer Area. It says no DANA-specific `/sessions` parameters or Drop-in configuration are needed for the ordinary flow. The Sessions prerequisite table does **not** separately state a redirect-handling row; follow the linked base integration for its action handling rather than inferring a method exception. (raw lines 25–46)
- **Advanced base:** the page requires an existing Advanced-flow Android Drop-in integration, handling `action.type: redirect`, and DANA added in Customer Area. It says no DANA-specific configuration or ordinary `/payments` parameters are needed. The Advanced section gives no stated Checkout API minimum; its v68 curl sample below is an example version, not a universal Advanced floor. (raw lines 298–318, 359–380)
- **Conditional recurring route in both sections:** token creation uses `/payments` with `storePaymentMethod: true` and a unique `shopperReference`. Only **when the initial payment has settled** does the page say a `recurring.token.created` webhook supplies `shopperReference`, initial-payment `eventId` and `storedPaymentMethodId`; the server must be ready for token lifecycle webhooks. Later token payments use `paymentMethod.storedPaymentMethodId`, the same shopper reference, `shopperInteraction: ContAuth`, and `Subscription` for fixed intervals or `UnscheduledCardOnFile` for non-fixed contracts. Those conditional recurring fields qualify the ordinary no-extra-parameter claims. (raw lines 48–85, 320–357)
- **Example boundaries:** the recurring request examples use `dana`, IDR, TEST-oriented environments and placeholder credentials/IDs; the Java example amount is IDR 15000 while most other examples use IDR 1000. They demonstrate request shapes, not a returned success state, token creation or supported minimum transaction amount. (raw lines 87–284, 359–556)
- **TEST/LIVE wording:** under “Test and go live,” the page says testing **successful DANA live payments** requires a real mobile number registered to a DANA account. It also directs readers to a **test** Customer Area status list and Support for testing issues, then requires a separate request in **live** Customer Area before live acceptance. This mixed wording does not establish a successful TEST payment or prove live access. (raw lines 286–296, 558–566)

## Detail locators

- Sessions prerequisites and base request/configuration statements: raw lines 25–46.
- Sessions recurring token lifecycle and later request fields: raw lines 48–85.
- Sessions request examples and test/live directions: raw lines 87–296.
- Advanced prerequisites and base no-extra-parameter statements: raw lines 298–318.
- Advanced recurring lifecycle and examples: raw lines 320–556.
- Advanced test/live directions: raw lines 558–566.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-dana]]
- [[adyen-tokenization]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/dana/android-drop-in/2026-09-15|Adyen DANA Android Drop-in, 2026-09-15 snapshot]]
