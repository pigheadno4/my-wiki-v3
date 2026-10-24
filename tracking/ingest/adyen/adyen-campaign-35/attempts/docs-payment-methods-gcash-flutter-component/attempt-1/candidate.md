---
title: "Adyen GCash Flutter Component"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/gcash/flutter-component"
raw_files:
  - "adyen/docs/payment-methods/gcash/flutter-component/2026-09-15.md"
tags: [adyen, gcash, flutter, components, online-payments, recurring-payments]
---

## Overview

This 2026-09-15 Adyen snapshot gives the **GCash-specific additions** for an existing Flutter Components integration, separated into Sessions and Advanced server-side flows. It is an add-on to the main integration guides, not complete implementation, current eligibility or completed-payment evidence. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Sessions prerequisites:** The page calls for an existing Sessions-flow Flutter Components integration, Checkout API **v68 or later**, handling of a redirect action (`action.type: redirect`), and GCash added in Customer Area. Yet its Integration type link points to an **Advanced-flow Drop-in** URL; the separate redirect and session-creation links point to Sessions-flow Components. Do not treat the mismatched URL as a valid Components base procedure. (raw lines 23–40)
- **Ordinary Sessions additions:** The guide specifies no extra GCash parameters in `/sessions` and no extra GCash Component configuration. That method-specific statement does not waive base integration requirements or the separate recurring-token fields. (raw lines 36–62)
- **Advanced prerequisites and additions:** The Advanced section calls for an existing Advanced-flow Flutter Components integration, redirect handling, and GCash in Customer Area. It says no extra GCash configuration or ordinary `/payments` parameters are needed. Its Integration type link likewise points to **Drop-in**, while its redirect/payment links use Components. The section does not separately assert the Sessions-row API-version minimum; its recurring examples use a v68 TEST endpoint. (raw lines 296–318, 359–379)
- **Recurring token route:** Both flow sections describe recurring GCash transactions. For token creation, `/payments` includes `storePaymentMethod: true` and a unique `shopperReference` of **at least three characters**. Once the initial payment **has settled**, the `recurring.token.created` webhook yields `storedPaymentMethodId`, and the server must be set up to receive recurring-token lifecycle events. A later `/payments` uses that ID, the same shopper reference, `shopperInteraction: ContAuth`, and `recurringProcessingModel: Subscription` for fixed intervals or `UnscheduledCardOnFile` for nonfixed intervals. This is a conditional lifecycle, not evidence that the example payment settled or that a later charge succeeded. (raw lines 48–85, 320–357)
- **TEST/live wording:** The page says “To test successful GCash live payments,” use a real mobile number registered with a GCash account; that wording appears under **Test and go live**, alongside test Customer Area status checks and a separate request in the **live** Customer Area before accepting live payments. Preserve the test/live ambiguity rather than treating a real number or a test check as authorization or live enablement. (raw lines 286–294, 558–566)
- **Example limits:** Recurring request samples use `gcash`, `PHP`, placeholder merchant/shopper IDs and TEST endpoints or library environments. They illustrate request shape; this page does not document a final payment result, capture or settlement for those examples. (raw lines 87–108, 110–139, 359–411)

## Detail locators

- Scope and Sessions requirements, including mismatched base link: raw lines 15–40.
- No-extra-method-parameter/configuration statements: raw lines 38–46 and 310–318.
- Token creation and post-settlement webhook fields: raw lines 48–71 and 320–343.
- Subsequent token-payment fields and examples: raw lines 73–139 and 345–411.
- Advanced Components/Drop-in link mismatch: raw lines 296–306.
- Test/live guidance: raw lines 286–294 and 558–566.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[adyen-tokenization]]
- [[source-adyen-docs-payment-methods-gcash]]
- [[source-adyen-docs-payment-methods-gcash-android-component]]
- [[source-adyen-docs-payment-methods-gcash-ios-component]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/gcash/flutter-component/2026-09-15|Adyen GCash Flutter Component, 2026-09-15 snapshot]]
