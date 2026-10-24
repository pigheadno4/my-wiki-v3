---
title: "Adyen Alipay HK for Android integration routes"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/alipayhk/android"
raw_files:
  - "adyen/docs/payment-methods/alipayhk/android/2026-09-15.md"
tags: [adyen, alipayhk, android, navigation]
---

## Overview

This [[adyen]] **Alipay HK for Android** page is an integration chooser. It links an Android **Drop-in** guide and an **InstantPaymentComponent** guide, then points to main Android Sessions and Advanced flow guides for both Drop-in and Components. The page does not state child-guide SDK/API versions, setup requirements, test/live eligibility or a completed payment result. [[adyen-online-payments]]

## Key takeaways

- **Drop-in route:** It links `/payment-methods/alipayhk/android-drop-in` as an all-in-one UI option for adding Alipay HK to an Android app. See raw lines 19–23.
- **Component route:** It links `/payment-methods/alipayhk/android-component` and describes `InstantPaymentComponent` as handling the redirect to Alipay HK. The linked guide supplies implementation behavior; this chooser does not describe a full redirect return or payment outcome. See raw lines 25–27.
- **Main integration first:** The See also section says to create the main integration before adding Alipay HK, with separate Android Drop-in/Components links for Sessions and Advanced flows. These are navigation routes, not evidence that each child path has identical prerequisites. See raw lines 29–36.

## Related

- [[adyen-online-payments]]
- [[adyen-android-sdk]]
- [[source-adyen-docs-payment-methods-alipayhk-android-drop-in]]
- [[source-adyen-docs-payment-methods-alipayhk-android-component]]
- [[adyen]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/alipayhk/android/2026-09-15|Adyen Alipay HK for Android chooser]]
