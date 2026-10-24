---
title: "Adyen Apple Pay iOS Drop-in integration"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/apple-pay/ios-drop-in"
raw_files:
  - "adyen/docs/payment-methods/apple-pay/ios-drop-in/2026-09-15.md"
tags: [adyen, apple-pay, ios, drop-in, online-payments]
---

## Overview

This [[adyen]] Apple Pay guide, last modified 2023-02-26 and captured 2026-09-15, adds Apple Pay to an existing **iOS Drop-in** integration. It distinguishes Sessions `/sessions` and Advanced `/payments`, gives versioned native configuration, and points to recurring tokenization and TEST/LIVE setup. See [[adyen-online-payments]]. Configuration and test instructions are not evidence of current wallet/account enablement or a completed authorization, capture or settlement. See raw lines 15–50 and 163–175.

## Key takeaways

- Both routes require an existing iOS Drop-in integration of the selected flow, Apple Pay set up with the merchant's **own certificate**, and Apple Pay added in Customer Area. The guide names the **API Clientside Encryption Payments role** specifically for processing live Apple Pay payments. It says no additional Apple Pay API fields are needed; `/sessions` is the default with Drop-in v5.0.0+, while `/payments` is for an additional use case. These are flow and role prerequisites, not evidence of live enablement. See raw lines 21–50.
- Native Drop-in **v5.3.0+** configuration lists an Apple `PKPaymentRequest` and `merchantIdentifier`; its Swift snippet, however, initializes `applePay` with `paymentRequest` only, leaving the listed merchant identifier absent from the shown call. **v5.0.0–v5.2.0** lists `merchantIdentifier` and shows a `payment` argument. The **v4.10.0-or-earlier** section lists merchant identifier, payment amount/currency/country and summary items; its example creates a `payment` value but does not pass it into the displayed `ApplePayComponent.Configuration` initializer. These examples are version-specific illustrations, not complete validated implementations. See raw lines 52–129.
- For iOS Drop-in v5.0.0+, optional settings include required/prefilled contacts, shipping, country-limited issuing cards, coupon information and `applicationData` signed into the resulting `PKPaymentToken`. `allowOnboarding: true` lets a shopper add a card when none are present or supported; its stated default is false, in which case Apple Pay is not displayed without wallet cards. `PKRecurringPaymentRequest` is marked required for recurring payments. The page says v4.x has no additional optional configuration. See raw lines 131–155.
- Recurring requires `PKRecurringPaymentRequest` when configuring Apple Pay; actual recurring payment setup goes to the separate create-token and subsequent-token-transaction guides. This page does not establish consent capture, token creation, network-token provisioning, or a successful subsequent payment; do not infer those from a configured request. See raw lines 157–161 and [[adyen-tokenization]].
- The testing section points to Apple's test cards and sandbox instructions, and to Customer Area's TEST payment list for status. Going live repeats the credential role requirement and says to set up Apple Pay on the Apple Developer account for the **live merchant identifier**. Test status and live setup steps do not show current production acceptance or payment lifecycle completion. See raw lines 163–175.

## Detail locators

- **Sessions/Advanced prerequisites, own-certificate and live credential-role scopes:** raw lines 21–50.
- **Versioned Drop-in Apple Pay configuration and sample discrepancies:** raw lines 52–129.
- **Optional v5+ fields, onboarding behavior and v4 scope:** raw lines 131–155.
- **Recurring handoff, testing and live merchant-identifier setup:** raw lines 157–175.

## Related

- [[adyen-online-payments]]
- [[adyen-tokenization]]
- [[source-adyen-docs-payment-methods-apple-pay]]
- [[source-adyen-docs-payment-methods-apple-pay-apple-pay-certificate-ios]]
- [[source-adyen-docs-payment-methods-apple-pay-handle-apple-pay-errors]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/apple-pay/ios-drop-in/2026-09-15|Apple Pay iOS Drop-in — captured 2026-09-15]]
