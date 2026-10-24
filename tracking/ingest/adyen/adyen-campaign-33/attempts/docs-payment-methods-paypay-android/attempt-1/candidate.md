---
title: "PayPay for Android"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/paypay/android"
raw_files:
  - "adyen/docs/payment-methods/paypay/android/2026-09-15.md"
tags: [adyen, paypay, android, navigation, online-payments]
---

## Overview

This 2026-09-15 Adyen Android page is a **navigation chooser** for adding PayPay to an Android app. It links method-specific Android Drop-in and Components guides and main Android Sessions/Advanced integration guides. It describes the Component option as using `InstantPaymentComponent` for the PayPay redirect, but does not provide that implementation or a payment result. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- The method-specific choices are **Android Drop-in**, described as an all-in-one UI solution, and **Android Components**, whose short description says `InstantPaymentComponent` handles the redirect to PayPay. This is a chooser description; the linked child guide owns concrete prerequisites and behavior. (raw lines 19–27)
- The page says to create the main integration before adding PayPay. It links separate Android Drop-in and Components main guides for both **Sessions** and **Advanced** flows. These are route labels and do not set an API/SDK version or establish the detailed return/outcome flow on this page. (raw lines 29–36)
- Listing these routes does not demonstrate a merchant's current PayPay eligibility, live configuration, shopper authorization, capture, settlement or refund. (raw lines 15–36)

## Detail locators

- Android Drop-in/Components chooser and `InstantPaymentComponent` description: raw lines 19–27.
- Main Android Sessions/Advanced integration routes: raw lines 29–36.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-paypay]]
- [[source-adyen-docs-payment-methods-paypay-android-drop-in]]
- [[source-adyen-docs-payment-methods-paypay-android-component]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/paypay/android/2026-09-15|Adyen PayPay for Android, 2026-09-15 snapshot]]
