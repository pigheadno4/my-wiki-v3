---
title: "Adyen Apple Pay Flutter Component integration"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/apple-pay/flutter-component"
raw_files:
  - "adyen/docs/payment-methods/apple-pay/flutter-component/2026-09-15.md"
tags: [adyen, apple-pay, flutter, components, online-payments]
---

## Overview

This [[adyen]] page, modified and captured 2026-09-15, describes adding Apple Pay to an existing **Flutter Components** integration through either Sessions `/sessions` or Advanced `/payments`. It covers own-certificate prerequisites, Flutter-side component configuration, TEST and live setup. See [[adyen-online-payments]]. It is configuration guidance, not proof of current Apple Pay availability or an authorized, captured or settled payment. See raw lines 15–53 and 124–136.

## Key takeaways

- Both branches require an existing Components integration of the chosen flow, Apple Pay set up with the merchant's **own iOS certificate**, and Apple Pay added in Customer Area. The **API Clientside Encryption Payments role** is named for live processing. The linked [[source-adyen-docs-payment-methods-apple-pay-apple-pay-certificate-ios|iOS certificate guide]] separately instructs enabling Apple Pay capability in the app and describes Apple merchant identifiers, Adyen's payment-processing certificate upload/decryption role, and separate test/live identifiers (related raw lines 33–40, 66–87). Those native setup steps are related-guide authority, not execution evidence from this Flutter page. See primary raw lines 21–41 and 132–136.
- Apple Pay adds no extra server fields to the selected `/sessions` or `/payments` request according to this page; it points to separate server-side Apple Pay error handling. Its Sessions/Advanced prerequisite links contain a literal encoded `{{getParameter('platform')}}` template instead of a resolved Flutter platform in raw lines 29 and 38, while the API-reference and later component links do include `platform=Flutter` (raw lines 47–63, 116–122). Use the explicit Flutter routes rather than assuming the templated links resolve. See raw lines 43–63.
- Flutter client configuration lists `merchantID` and `merchantName` for `ApplePayConfiguration`; the displayed constructor uses `merchantId` casing. It then passes that object to `ApplePayComponentConfiguration` alongside environment, client key and country code, with optional locale and amount. The second example omits a comma after `applePayConfiguration: applePayConfiguration` before `shopperLocale`, and both Dart-shaped examples are fenced `js`. Treat them as illustrative, not verified compilable code or live-environment instructions. Sessions then initializes/shows the Component; Advanced adds required callbacks through its linked flow. See raw lines 55–94 and 116–122.
- Optional configuration includes `allowOnboarding` (false by default, hiding Apple Pay when no wallet card exists), summary items, billing/shipping contacts, application data, supported issuing countries and merchant capability. The table says the last `applePaySummaryItems` entry must equal the `amount` in a `/payments` request; it does not explain an equivalent Sessions comparison. This guide contains no dedicated recurring-payment setup, `PKRecurringPaymentRequest`, token or consent flow. The summary-items description alone does not establish recurring support or a stored/network token. See raw lines 96–114.
- TEST guidance points to Apple test cards and checking a test payment in Customer Area. Live guidance repeats the credential role and directs Apple Pay setup for a **live merchant identifier** on the Apple Developer account. These are setup/status instructions, not confirmation of merchant entitlement, live enablement, authorization, capture or settlement. See raw lines 124–136.

## Detail locators

- **Flow-specific prerequisites, own iOS certificate, API role and malformed prerequisite links:** raw lines 21–53.
- **Flutter configuration, property casing, snippet syntax and Sessions/Advanced client handoff:** raw lines 55–94, 116–122.
- **Optional fields, summary-item amount condition and onboarding default:** raw lines 96–114.
- **TEST and live setup:** raw lines 124–136.

## Related

- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-apple-pay]]
- [[source-adyen-docs-payment-methods-apple-pay-apple-pay-certificate-ios]]
- [[source-adyen-docs-payment-methods-apple-pay-handle-apple-pay-errors]]
- [[adyen-tokenization]]

## Related raw API references

- [[raw/adyen/docs/payment-methods/apple-pay/apple-pay-certificate/ios/2026-09-15|iOS own-certificate guide]] — referenced for native Apple Pay capability and certificate roles; this page's pinned raw is below.

## Raw Sources

- [[raw/adyen/docs/payment-methods/apple-pay/flutter-component/2026-09-15|Apple Pay Flutter Component — captured 2026-09-15]]
