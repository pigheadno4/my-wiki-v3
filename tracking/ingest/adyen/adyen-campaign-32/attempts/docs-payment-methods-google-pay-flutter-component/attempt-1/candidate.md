---
title: "Adyen Google Pay Flutter Component (historical guide)"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/google-pay/flutter-component"
raw_files:
  - "adyen/docs/payment-methods/google-pay/flutter-component/2026-09-15.md"
tags: [adyen, google-pay, flutter, components, online-payments, historical]
---

## Overview

This [[adyen]] page, last modified and captured **2026-09-15**, describes adding Google Pay to an **existing Flutter Components** integration, with separate **Sessions** and **Advanced** server-side flow tabs. It directs the reader to Google's Android setup instructions and says to add Google Pay in Adyen Customer Area before either path (raw lines 15–39). It belongs under [[adyen-online-payments]]. Component setup and Google-wallet availability do not establish authorization, capture, settlement or present account enablement.

## Key takeaways

- The page says Google Pay needs **no additional fields** in the server `/sessions` request for Sessions or `/payments` request for Advanced, but **does** require additional Google Pay properties in the **client configuration object** (raw lines 41–63). It separately names `googlePayEnvironment` with **test/production** values and shows Adyen component `environment: Environment.test`; those are separate environment settings (raw lines 61–89). Do not infer a live payment merely from switching either example to production.
- Optional configuration includes a field the page labels `merchantAccount` but describes as a **Google Merchant ID**, which it says may be arbitrary in testing and must come from Google Pay & Wallet Console before LIVE (raw line 97). It also lists merchant display information, total-price status, `allowedCardNetworks` and `allowedAuthMethods` (`panOnly` versus `cryptogram3DS`), plus prepaid/credit-card and contact/address options (raw lines 91–110). These are configuration descriptions; network support is delegated to the Google Pay overview, and the page gives no token-processing or recurring-payment procedure.
- **Snippet caveat:** the fenced `js` examples use Dart-like `final` syntax, the first constructor is not closed, and the Google Pay component sample includes `applePayConfiguration: applePayConfiguration` with no separating comma before `shopperLocale` (raw lines 65–89). The optional `assuranceDetailsRequired` description is cut off after “Set to true to require” (raw line 104). The examples and incomplete row cannot be treated as a tested, complete Flutter configuration.
- For Sessions, the page routes to initialize/show the Component after configuration; for Advanced, it routes to required callbacks (raw lines 112–120). It does not give the full callback/payment-result flow here, and displaying the component is not a payment outcome.
- TEST guidance distinguishes the Google test-card suite from a wallet using real cards **mapped to Adyen test cards**, which the page says are not charged (raw lines 122–146). The suite includes FPAN, DPAN **only when testing through native Android and Chrome on Android**, and 3DS2 scenarios; without the suite, the page says **only American Express or Discover** trigger 3DS2 challenge tests (raw lines 128–144). These test conditions do not prove live card/network eligibility or production authorization.
- Before LIVE, the page recommends testing Google's Android API scenarios, then requires an Adyen API credential with **API Clientside Encryption Payments role**, live Customer Area Google Merchant ID configuration, and Google's Android production-deployment steps (raw lines 148–154). It says live Google Pay is available only when the shopper is logged in to Google and has at least one valid Google Pay payment method (raw lines 156–159); those are necessary shopper conditions in this snapshot, not a guarantee of payment success.

## Detail locators

- Existing Flutter Sessions/Advanced integrations, Google Android setup and Customer Area addition: raw lines 15–39.
- No extra server API fields versus required client configuration and separate environments: raw lines 41–89.
- Optional merchant/network/auth/contact settings and incomplete assurance row: raw lines 91–110.
- Sessions initialization and Advanced callback routes: raw lines 112–120.
- Google test-card suite, FPAN/DPAN/3DS conditions, mapped-card route: raw lines 122–146.
- LIVE role, Google Merchant ID/deployment and shopper wallet conditions: raw lines 148–159.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-google-pay]]
- [[source-adyen-docs-payment-methods-google-pay-android-component]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/google-pay/flutter-component/2026-09-15|Full pinned Google Pay Flutter Component guide]]
