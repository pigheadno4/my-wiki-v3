---
title: "Adyen GCash Android integration chooser"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/gcash/android"
raw_files:
  - "adyen/docs/payment-methods/gcash/android/2026-09-15.md"
tags: [adyen, gcash, android, drop-in, components, online-payments]
---

## Overview

This 2026-09-15 Adyen page is a **navigation chooser** for adding GCash to an Android app. It routes to GCash Android Drop-in or Components child guides and to the corresponding main Android Sessions/Advanced integration guides. It contains no complete setup procedure, API/SDK version requirement, merchant-eligibility rule or payment outcome. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Method route:** The Drop-in option is described as Adyen's all-in-one UI solution for adding GCash to Android. The Components option describes `InstantPaymentComponent` as handling the redirect to GCash. These are chooser descriptions; implementation details and exact prerequisites belong to the linked child guides. (raw lines 19–27)
- **Base guides:** The page tells readers to create the main integration before adding GCash, then links Android Drop-in and Android Components for both Sessions and Advanced flows. It does not itself establish how to handle redirect return, call `/sessions` or `/payments`, set up tokens, test, or assess an asynchronous outcome. (raw lines 29–36)

## Detail locators

- GCash Android purpose and channel chooser: raw lines 15–27.
- Main Sessions and Advanced integration routes: raw lines 29–36.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-gcash-android-drop-in]]
- [[source-adyen-docs-payment-methods-gcash-android-component]]
- [[source-adyen-docs-payment-methods-gcash]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/gcash/android/2026-09-15|Adyen GCash for Android chooser, 2026-09-15 snapshot]]
