---
title: "Adyen MoMo React Native Drop-in"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/momo-wallet/react-native-drop-in"
raw_files:
  - "adyen/docs/payment-methods/momo-wallet/react-native-drop-in/2026-09-15.md"
tags: [adyen, momo, react-native, drop-in, online-payments, recurring-payments]
---

## Overview

This 2026-09-15 Adyen snapshot describes **MoMo-specific additions** to an existing React Native Drop-in integration, separately for Sessions and Advanced server-side flows. It is a method add-on, not the complete base integration guide, and does not establish current availability, merchant eligibility or a completed payment. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Sessions prerequisites:** The page calls for an existing Sessions-flow React Native Drop-in integration, Checkout API **v68 or later**, redirect handling for `action.type: redirect`, and MoMo added in Customer Area. Its Sessions integration-type row links to an **Advanced-flow** URL while its redirect and session-creation links point to Sessions-flow URLs; follow the flow label and inspect the base guide rather than treating that URL as a Sessions implementation procedure. (raw lines 23–36)
- **Sessions method additions:** No MoMo-specific extra `/sessions` parameters or Drop-in configuration parameters are required for the ordinary payment flow described here. That statement does not remove base integration requirements or the distinct fields needed for recurring-token creation. (raw lines 38–64)
- **Advanced prerequisites and ordinary payment additions:** The Advanced section calls for an existing Advanced-flow React Native Drop-in integration, redirect handling for `action.type: redirect`, and MoMo added in Customer Area. It specifies no additional MoMo configuration or ordinary `/payments` parameters. The section does not separately state the Sessions-row v68-or-later API requirement; its sample uses a v68 test endpoint. (raw lines 299–321, 362–383)
- **Recurring token route:** Both flow sections state that MoMo supports recurring transactions. To create a shopper token, the page specifies `storePaymentMethod: true` and a unique `shopperReference` in `/payments`. After the initial payment **has been settled**, it says the `recurring.token.created` lifecycle webhook supplies `storedPaymentMethodId`; the server must receive that webhook. Later `/payments` requests use that ID with the same shopper reference, `shopperInteraction: ContAuth`, and `recurringProcessingModel: Subscription` for fixed intervals or `UnscheduledCardOnFile` for nonfixed intervals. The token event is conditional on settlement; request examples do not prove an actual settlement or recurring charge. (raw lines 50–87, 323–360)
- **Example qualification:** The prose and JSON/PHP/Node/Python/Ruby examples use `storedPaymentMethodId`, while the Java sample sets `recurringDetailReference` on `DefaultPaymentMethodDetails`. Treat that field discrepancy as unresolved in this captured page; verify against the applicable API/library documentation before using the example. The examples show `VND` and `momo_wallet` but are sample values, not standalone eligibility or outcome proof. (raw lines 79–108, 120–141, 350–381, 403–414)
- **TEST and live boundary:** The page directs testing with the MoMo test app and test credentials, checking test-payment status in Customer Area, and submitting a separate MoMo request in the **live** Customer Area before accepting live payments. Its TEST instructions and request snippets are not evidence that any merchant is enabled or that a payment has succeeded. (raw lines 288–297, 561–570)

## Detail locators

- Page scope and server-side-flow split: raw lines 15–25.
- Sessions requirements, no-extra-parameter/configuration statements: raw lines 29–48.
- Sessions token lifecycle and subsequent-payment fields: raw lines 50–87.
- Advanced requirements and no-extra-configuration/payment-parameter statements: raw lines 299–321.
- Advanced token lifecycle and example-field discrepancy: raw lines 323–360, 403–414.
- Test-app/credential and live Customer Area prerequisites: raw lines 288–297 and 561–570.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[adyen-tokenization]]
- [[source-adyen-docs-payment-methods-momo-wallet]]
- [[source-adyen-docs-payment-methods-momo-wallet-android-component]]
- [[source-adyen-docs-payment-methods-momo-wallet-ios-component]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/momo-wallet/react-native-drop-in/2026-09-15|Adyen MoMo React Native Drop-in, 2026-09-15 snapshot]]
