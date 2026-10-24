---
title: "Adyen Apple Pay iOS Component guide"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/apple-pay/ios-component"
raw_files:
  - "adyen/docs/payment-methods/apple-pay/ios-component/2026-09-15.md"
tags: [adyen, apple-pay, ios, components, online-payments, tokenization]
---

## Overview

This [[adyen]] guide, last modified 2023-02-26 and captured 2026-09-15, describes adding Apple Pay to an **existing iOS Components** checkout. It separates Sessions `/sessions` from Advanced `/payments` and gives version-specific **client** Apple Pay Component configuration; the underlying payment flow and live setup remain separate. See [[adyen-online-payments]]. The captured guide does not establish current Apple Pay, issuer, country or merchant availability, certificate state, authorization, capture or settlement. See raw lines 15–50.

## Key takeaways

- Both flows require Apple Pay setup using the merchant's **own iOS certificate** and Apple Pay added in Customer Area. The **API Clientside Encryption Payments role** is stated specifically for live processing. `/sessions` is the default for iOS Components v5.0.0+, while `/payments` is framed as an additional use case. The page says Apple Pay adds no method-specific request fields; this does not remove the underlying flow's request requirements. See raw lines 21–50 and [[source-adyen-docs-payment-methods-apple-pay-apple-pay-certificate-ios|iOS certificate guide]].
- For **v5.3.0+**, the configuration section names `paymentRequest` (`PKPaymentRequest`) and `merchantIdentifier`; its Swift sample builds `ApplePayComponent.Configuration(paymentRequest:)` and does not explicitly pass a merchant identifier, so do not treat that sample alone as a complete explanation of the table. For **v5.0.0–v5.2.0**, it shows `ApplePayPayment` and `merchantIdentifier`. The **v4.x.x** section specifically says Components v4.10.0 or earlier and uses a different `summaryItems`/`merchantIdentifier` pattern, but its final line assigns the configuration to `dropInConfiguration.applePay` despite this being a Component guide. These are versioned examples, not a single interchangeable recipe. See raw lines 52–147.
- For v5.0.0+, optional settings include billing/shipping contacts and methods, supported card-issue countries, coupon fields, signed `applicationData` and `allowOnboarding`. The page says `allowOnboarding` defaults to false; turning it on lets a shopper add a wallet card when none or none supported, while the default hides Apple Pay when no wallet card exists. These are UI/configuration conditions, not live payment enablement. See raw lines 149–168.
- The guide says recurring Apple Pay requires `PKRecurringPaymentRequest` in Component configuration **and** a token created before subsequent recurring transactions. The linked tokenization guides own shopper permission, server request and token lifecycle detail; this page does not demonstrate consent, token creation or a later charge. See raw lines 169–179 and [[adyen-tokenization]].
- Testing uses Apple's test cards and a test Customer Area lookup. For live payments the guide again calls for the API Clientside Encryption Payments role and Apple Pay set up on the merchant's Apple Developer account for its live merchant identifier. Its error link is a separate guide. A configured Component or test lookup is not an authorization or funds movement result. See raw lines 181–200.

## Detail locators

- **Sessions versus Advanced prerequisites and live role:** raw lines 21–41.
- **Base API request scope and separate error route:** raw lines 43–50.
- **Versioned client setup and snippet discrepancies:** raw lines 52–147; v5.3.0+ table/sample at 58–80 and v4.10.0-or-earlier Drop-in assignment at 112–147.
- **Optional wallet/card/onboarding/coupon controls:** raw lines 149–173.
- **Recurring request/token boundary and TEST/LIVE preparation:** raw lines 175–200.

## Related

- [[adyen-online-payments]]
- [[adyen-tokenization]]
- [[source-adyen-docs-payment-methods-apple-pay-apple-pay-certificate-ios]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/apple-pay/ios-component/2026-09-15|Apple Pay iOS Component guide — captured 2026-09-15]]
