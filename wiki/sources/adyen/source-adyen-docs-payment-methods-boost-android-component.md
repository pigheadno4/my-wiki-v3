---
title: "Adyen Boost Wallet Android Component guide"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/boost/android-component"
raw_files:
  - "adyen/docs/payment-methods/boost/android-component/2026-09-15.md"
tags: [adyen, boost-wallet, android, components, redirects, online-payments]
---

## Overview

This [[adyen]] Boost Wallet Android Components add-on, captured 2026-09-15, supplies method-specific setup for **existing** Sessions or Advanced Android Components integrations. It uses the `InstantPaymentComponent` with `molpay_boost`, requires redirect handling and says there is no Boost Wallet test environment. See [[adyen-online-payments]] and [[adyen-android-sdk]]. It is not a complete base integration, live-merchant eligibility proof, or payment-outcome evidence. See raw lines 15–36, 75–125 and 132–140.

## Key takeaways

- **Sessions:** The page requires an existing Sessions Android Components integration, Checkout API **v68 or later**, `action.type: redirect` handling, and Boost Wallet added in Customer Area. The base `/sessions` request and Boost-specific Component configuration need no additional parameters. Compose and non-Compose imports use the `instant` module; Compose also shows `components-compose`. The version is a `YOUR_VERSION` placeholder, not a published minimum Android SDK version. See raw lines 25–77.
- **Component selection:** For Sessions, the example gets `molpay_boost` from the checkout session and creates `InstantPaymentComponent` in Compose or a view; for Advanced, it looks for `molpay_boost` in `/paymentMethods` and uses the same Component class. These examples demonstrate selection and UI attachment, not a complete request/return/result lifecycle. See raw lines 75–125 and 171–226.
- **Advanced:** The page requires an existing Advanced Android Components integration, additional-action redirect handling, and Boost Wallet added in Customer Area. It says no extra Boost-specific configuration or ordinary `/payments` parameters are needed. These are method-add-on statements, not a claim that the base payment request has no required fields. See raw lines 132–175 and 228–232.
- **Testing boundary:** Both flow sections say **no Boost Wallet test environment is available** and direct live-environment penny tests. That guidance does not establish live-account approval, current availability, successful authorization/capture/settlement, or a safe test transaction for any given merchant. The page gives no country/currency matrix, recurring-token procedure or final-result webhook contract; use separate authority before making those claims. See raw lines 128–130 and 234–236.

## Detail locators

- Sessions requirements, request/configuration and imports: raw lines 25–71.
- Sessions `InstantPaymentComponent` examples: raw lines 73–125.
- Advanced requirements, imports and Component examples: raw lines 132–226.
- Advanced ordinary `/payments` add-on statement: raw lines 228–232.
- No-TEST-environment guidance: raw lines 128–130 and 234–236.

## Related

- [[adyen-online-payments]]
- [[adyen-android-sdk]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/boost/android-component/2026-09-15|Boost Wallet Android Component — captured 2026-09-15]]
