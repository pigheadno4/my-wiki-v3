---
title: "Adyen WeChat Pay in-app payments overview"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/wechat-pay/wechat-pay-in-app-payments"
raw_files:
  - "adyen/docs/payment-methods/wechat-pay/wechat-pay-in-app-payments/2026-09-15.md"
tags: [adyen, wechat-pay, mobile-app, wallets, online-payments]
---

## Overview

This [[adyen]] WeChat Pay in-app overview, captured 2026-09-15, describes a mobile-app payment that switches the shopper to the WeChat app for verification and then returns them to the merchant app. It points to Android Drop-in or Component integration and a merchant-built WeChat mobile-SDK route, with separate iOS, Android and API-only child guides. See [[adyen-online-payments]]. This overview is a historical channel and capability snapshot, not proof of merchant enablement or an actual payment outcome. See raw lines 15–21 and 29–47.

## Key takeaways

- The stated starting point is the merchant's mobile app. The page says an existing Android Drop-in or Component integration can be used, or the integration can be built with WeChat mobile SDKs. The shopper is switched into the WeChat app to verify the payment and returned to the merchant app when the payment is completed; the merchant can then present a result. An app return by itself is not an independently verified authorization, capture or settlement record. See raw lines 17–21.
- The historical matrix labels the method a wallet with `Redirect (App switch)` flow, `International` country/region scope, and AUD, CAD, CNY, EUR, GBP, HKD, JPY, NZD, SGD and USD. It marks recurring and chargebacks unavailable, while marking refunds and partial refunds available. These marks do not establish a given merchant account's eligibility or supply a refund procedure. See raw lines 25–27.
- The iOS, Android and API-only entries are navigation to child guides. This page supplies no provider registration steps, platform SDK or device-version minimum, request fields, webhook contract, or final-result verification procedure; use the relevant child guide for implementation conditions. Do not extend this mobile-app route to ordinary mobile-browser, desktop QR, or Mini Program payments. See raw lines 29–47 and [[source-adyen-docs-payment-methods-wechat-pay]].

## Detail locators

- Mobile-app integration choices and WeChat app-switch description: raw lines 17–21.
- Method, currency and feature matrix: raw lines 25–27.
- iOS, Android and API-only child routes: raw lines 29–47.

## Related

- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-wechat-pay]]

## Related raw API references

- [[raw/adyen/docs/payment-methods/wechat-pay/wechat-pay-in-app-payments/ios/2026-09-15|WeChat Pay iOS in-app child guide]] — linked route; its implementation conditions require separate evidence.
- [[raw/adyen/docs/payment-methods/wechat-pay/wechat-pay-in-app-payments/android/2026-09-15|WeChat Pay Android in-app child guide]] — linked route; its implementation conditions require separate evidence.
- [[raw/adyen/docs/payment-methods/wechat-pay/wechat-pay-in-app-payments/api-only/2026-09-15|WeChat Pay in-app API-only child guide]] — linked route; its implementation conditions require separate evidence.

## Raw Sources

- [[raw/adyen/docs/payment-methods/wechat-pay/wechat-pay-in-app-payments/2026-09-15|WeChat Pay in-app payments — captured 2026-09-15]]
