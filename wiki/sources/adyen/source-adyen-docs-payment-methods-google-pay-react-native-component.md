---
title: "Adyen Google Pay React Native Component integration"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/google-pay/react-native-component"
raw_files:
  - "adyen/docs/payment-methods/google-pay/react-native-component/2026-09-15.md"
tags: [adyen, google-pay, react-native, components, online-payments]
---

## Overview

This [[adyen]] page, modified and captured 2026-09-15, describes adding Google Pay to an existing React Native Component integration. Its implementation details are Android-facing: a Google Pay sheet, potential 3D Secure redirect and Android activity-result handoff. It covers optional wallet configuration, tokenization navigation and TEST/LIVE setup. See [[adyen-online-payments]]. The guide is a setup snapshot, not evidence of current account/device eligibility or a successful authorization, capture or settlement. See raw lines 15–47 and 71–113.

## Key takeaways

- The prerequisite is an existing React Native Component integration, Google's Google Pay setup steps for Android and Google Pay added in Adyen Customer Area. When the shopper selects Google Pay, the Component presents a wallet card-choice sheet; for a selected card needing 3D Secure, it also handles redirecting to another site for verification. These are client-flow statements, not Adyen payment-outcome claims. The guide says no extra Google Pay fields are required for the server `/payments` request; optional payment fields remain in the API reference. See raw lines 15–33.
- The Android activity must pass `onActivityResult` data to `AdyenCheckout.handleActivityResult(requestCode, resultCode, data)`. The shown block is fenced `kotlin` but uses Java-shaped `@Override`, semicolons and method syntax; treat it as an illustrative activity integration, not a verified paste-ready Kotlin implementation. The page states no React Native package/SDK minimum version. See raw lines 35–47.
- Optional `AdyenCheckout` configuration covers Google `merchantAccount` (described here as a **Google Merchant ID**, defaulting to the corresponding `brands` value from `/paymentMethods`), `allowedCardNetworks`, `allowedAuthMethods`, price status, prepaid/credit-card allowance, billing/email/shipping requirements and `existingPaymentMethodRequired`. The table distinguishes `PAN_ONLY` Google-account cards from `CRYPTOGRAM_3DS` Android device-token cards; these returned-data descriptions do not establish that the merchant may handle raw PAN, bypass PCI duties, or has a successful network token charge. See raw lines 49–66.
- The `googlePayEnvironment` row's possible-values prose lists **WalletConstants.ENVIRONMENT_TEST for both test and live**, while its default follows the `AdyenCheckout` environment. This is a source inconsistency; do not use its duplicated value as a verified live configuration. See raw line 67.
- For recurring Google Pay, this page directs the reader to create a shopper token and then make later token transactions through separate [[adyen-tokenization]] guides. It does not specify consent mechanics or show token creation or a later charge. See raw lines 71–74.
- Testing describes a Google wallet enrolled in the test-card suite, including FPAN, DPAN (only through native Android or Chrome on Android) and 3DS2 scenarios, or a wallet with real cards mapped to Adyen test cards without a charge. Outside the test-card suite, it specifies American Express or Discover for the described 3DS2 challenge tests. The TEST payment list is a status-check route, not proof that a real card was charged. See raw lines 76–100.
- Before live use, the page recommends live scenario testing and directs a live **API Clientside Encryption Payments role**, Google Merchant ID configuration in live Customer Area and Google's Android production deployment steps. It says live Google Pay availability also depends on the shopper being logged in to Google and having a valid payment method. These instructions do not establish completed merchant approval or actual live payment success. See raw lines 102–113.

## Detail locators

- **Component prerequisites, shopper sheet/3DS redirect and server field boundary:** raw lines 15–33.
- **Android `onActivityResult` code:** raw lines 35–47.
- **Optional provider settings, auth methods, defaults and duplicated environment enum:** raw lines 49–69.
- **Recurring navigation, TEST card choices and live gates:** raw lines 71–113.

## Related

- [[adyen-online-payments]]
- [[adyen-tokenization]]
- [[source-adyen-docs-payment-methods-google-pay]]
- [[source-adyen-docs-payment-methods-google-pay-android-component]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/google-pay/react-native-component/2026-09-15|Google Pay React Native Component — captured 2026-09-15]]
