---
title: "Adyen Afterpay for Android"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/afterpaytouch/android"
raw_files:
  - "adyen/docs/payment-methods/afterpaytouch/android/2026-09-15.md"
tags: [adyen, afterpay, android, drop-in, components, online-payments]
---

## Overview

This captured [[adyen]] page is an **Android integration chooser** for Afterpay. It routes to method-specific Android Drop-in and Components guides, then to main Android Sessions and Advanced integration guides. Its Components label names `InstantPaymentComponent` for the redirect. It does not itself specify request fields, SDK/API versions, capture terms, merchant enablement, return handling or a payment result. [[adyen-online-payments]]

## Key takeaways

- **Method-specific routes:** The Drop-in link describes Adyen's all-in-one UI for an Android app. The Components link describes `InstantPaymentComponent` as handling the redirect to Afterpay. These labels point to child guides and do not, alone, specify their full setup or response contract (raw lines 19–27).
- **Base integration first:** The See also section says to create the main integration before adding Afterpay, linking Android Drop-in and Components with both Sessions and Advanced flows (raw lines 29–36).
- **Evidence boundary:** Choose the child guide for the actual UI route and the main guide for the base flow. This chooser has no transaction-level evidence or statement that a specific merchant can accept Afterpay.

## Detail locators

- Page identity and Android method choices: pinned raw lines 15–27.
- Main Sessions/Advanced integration route list: pinned raw lines 29–36.

## Related

- [[adyen-online-payments]] — online payment architecture and method routes.
- [[source-adyen-docs-payment-methods-afterpaytouch-android-drop-in]] — Android Drop-in method-specific guide.
- [[source-adyen-docs-payment-methods-afterpaytouch-android-component]] — Android Components method-specific guide.

## Raw Sources

- [[raw/adyen/docs/payment-methods/afterpaytouch/android/2026-09-15|Afterpay for Android chooser, captured 2026-09-15]]
