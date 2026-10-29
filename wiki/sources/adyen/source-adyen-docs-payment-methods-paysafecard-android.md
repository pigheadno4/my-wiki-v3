---
title: "PaySafeCard for Android"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/paysafecard/android"
raw_files:
  - "adyen/docs/payment-methods/paysafecard/android/2026-09-15.md"
tags: [adyen, paysafecard, android, payments]
---

## Overview

This 2026-09-15 page is the Android integration chooser for PaySafeCard. It routes to method-specific Drop-in and Components guides, then to main Android integrations for Sessions and Advanced flow. It does not itself supply a complete payment implementation or prove current account enablement. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- The **Drop-in** route is `/payment-methods/paysafecard/android-drop-in`, described as an all-in-one Android UI solution; its captured child guide is [[source-adyen-docs-payment-methods-paysafecard-android-drop-in]]. See raw lines 19–23.
- The **Components** route is `/payment-methods/paysafecard/android-component`, described as using `InstantPaymentComponent` to handle the redirect to PaySafeCard; its captured child guide is [[source-adyen-docs-payment-methods-paysafecard-android-component]]. See raw lines 25–27.
- The page instructs readers to build the main integration first and lists Android Drop-in and Components base guides for both Sessions and Advanced flows. These links route to other guides; this chooser does not define their request fields or full action lifecycle. See raw lines 29–36.

> [!warning] Captured flow labels
> This Android chooser explicitly says its Components route handles a **redirect** (raw line 27), whereas the linked [[source-adyen-docs-payment-methods-paysafecard|PaySafeCard overview]] labels the method's payment flow **Direct** in its capability table (overview raw lines 25–27). Preserve the two captured labels; this page does not establish which describes current behavior.

## Detail locators

- Android method-specific chooser: raw **How do you want to integrate?**, lines 19–27.
- Base Android Sessions/Advanced routes: raw **See also**, lines 29–36.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-paysafecard]]
- [[source-adyen-docs-payment-methods-paysafecard-android-drop-in]]
- [[source-adyen-docs-payment-methods-paysafecard-android-component]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/paysafecard/android/2026-09-15|PaySafeCard for Android, captured 2026-09-15]]
