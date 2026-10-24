---
title: "Boost Wallet iOS Component"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/boost/ios-component"
raw_files:
  - "adyen/docs/payment-methods/boost/ios-component/2026-09-15.md"
tags: [adyen, boost, wallet, ios, components, online-payments]
---

## Overview

This 2026-09-15 guide describes adding Boost Wallet to an existing Adyen iOS Components integration, with separate Sessions and Advanced server-side flows. Its method-specific steps concern redirect handling and `InstantPaymentComponent` initialization, not an observed payment outcome. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Sessions flow:** requires an existing iOS Components Sessions integration, Checkout API v68 or later, redirect action handling, and Boost Wallet added in Customer Area. The guide says no additional `/sessions` parameters or Boost-specific Component configuration are needed. Its Swift example looks up `molpay_boost` in the session payment methods, assigns the session as delegate and initiates payment. This is example setup, not evidence that the method is available to a particular merchant or that payment completed. (raw lines 25–69)
- **Advanced flow:** requires an existing iOS Components Advanced integration according to the requirement label, redirect action handling, and Customer Area setup. It says no extra Boost configuration or `/payments` parameters. Its example again uses `InstantPaymentComponent` and `molpay_boost`, with `self` as delegate. The requirement's base-guide link points to `integration=Drop-in` even though this page and its redirect/payment links specify Components; the inconsistency is not resolved here. The page states no SDK minimum for this flow. (raw lines 76–119)
- **Environment limit:** for both flows, the page explicitly says no Boost Wallet test environment is available and describes penny tests in LIVE. This historical statement is not permission or evidence to run a financial test, nor proof of current production enablement. (raw lines 72–74, 121–123)
- **Outcome limit:** selecting the method, calling `initiatePayment()`, or handling a redirect does not prove authorization, capture or settlement. This method-specific page does not spell out a final status or webhook sequence. (raw lines 25–123)

## Detail locators

- Sessions prerequisites, parameters and configuration: raw lines 29–48.
- Sessions `InstantPaymentComponent`, `molpay_boost` and session delegate example: raw lines 50–69.
- Advanced prerequisites and mismatched Drop-in base-guide link: raw lines 80–86.
- Advanced Component initialization, delegate and payment parameters: raw lines 88–119.
- No-test-environment statement: raw lines 72–74, 121–123.

## Related

- [[adyen]]
- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/boost/ios-component/2026-09-15|Adyen Boost Wallet iOS Component guide, 2026-09-15 snapshot]]
