---
title: "MobilePay Android Drop-in | Adyen Docs"
type: source
date_ingested: 2026-10-26
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/mobilepay/android-drop-in"
raw_files:
  - "adyen/docs/payment-methods/mobilepay/android-drop-in/2026-09-15.md"
tags: [adyen, mobilepay, android, drop-in, redirect, payout]
---

## Overview

This [[adyen]] guide gives MobilePay-specific additions to an existing Android Drop-in checkout, separately for Sessions and Advanced server-side flows. The Advanced section explicitly requires handling a redirect action. The page also describes an experimental `/payments` route for a token that can be used in later MobilePay-wallet payouts. It does not establish current merchant eligibility, supported countries or currencies, successful payment authorization, or payout availability. See [[adyen-online-payments]].

## Key takeaways

- **Sessions:** Requires an existing Android Drop-in Sessions integration using Checkout API v68 or later and MobilePay added in Customer Area. It specifies no extra MobilePay `/sessions` parameters or Drop-in configuration. This section does not separately state a redirect-handling requirement; use the linked base Sessions guide for that flow's mechanics. See raw lines 25–46.
- **Advanced:** Requires an existing Android Drop-in Advanced integration, handling `action.type: redirect`, and MobilePay added in Customer Area. It specifies no extra MobilePay configuration or ordinary `/payments` fields, except for the future-payout-token case. No Advanced Checkout API minimum is stated here. See raw lines 85–105.
- **Normal-payment testing:** The guide says MobilePay cannot be tested in the test environment. It directs a live Customer Area request followed by low-amount live payments, then checking the server's `AUTHORISATION` webhook and the live Payment list for status. An intermediate redirect or client completion is not payment-status proof. See raw lines 48–60 and 325–335.
- **Experimental payout token:** The feature is labeled experimental and supported only with `/payments`. The described token-creation request includes `telephoneNumber`, `shopperReference` and `enablePayout: true`, after setting up the recurring lifecycle webhook. The merchant saves `storedPaymentMethodId` from that webhook against `shopperReference`, then uses the token in `counterparty.card.cardIdentification` for a later `/transfers` request. Separate payout-test instructions call for a Vipps MobilePay test app and webhook/transfer checks. See raw lines 62–83 and 291–358.

> [!warning] Payout request examples conflict with prose
> Token-creation prose spells the flag `enablePayout`, while the annotated curl field spells it `enablePayOut`. The Java, PHP, C#, Node, Python and Ruby snippets include `telephoneNumber` but omit `shopperReference` and the flag; the examples also leave method type, currency and return URL blank. The curl example uses a TEST endpoint despite the normal-payment live-only warning. These snippets are not complete working token requests or proof that ordinary MobilePay payments work in TEST. See raw lines 105–288 and 291–301.

## Detail locators

- Sessions prerequisites, no-extra-field and configuration guidance: raw lines 25–46; Advanced prerequisites and request distinction: raw lines 85–105.
- Server-language request examples and placeholders: raw lines 107–288; token webhook example and later transfer field: raw lines 291–323.
- Normal payment and separate experimental payout test guidance: raw lines 48–83 and 325–358. This method-specific page gives no Drop-in initialization code, country/currency matrix, or full base-flow result contract.

## Related

- [[adyen-android-sdk]] — native Drop-in architecture and separately versioned SDK evidence; this page pins no Android SDK version.
- [[adyen-payouts]] — broader payout and transfer context.

## Raw Sources

- [[raw/adyen/docs/payment-methods/mobilepay/android-drop-in/2026-09-15|MobilePay Android Drop-in, 2026-09-15 snapshot]]
