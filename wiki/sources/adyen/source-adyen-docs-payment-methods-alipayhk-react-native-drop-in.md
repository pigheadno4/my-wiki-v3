---
title: "Adyen Alipay HK React Native Drop-in"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/alipayhk/react-native-drop-in"
raw_files:
  - "adyen/docs/payment-methods/alipayhk/react-native-drop-in/2026-09-15.md"
tags: [adyen, alipayhk, react-native, drop-in, online-payments]
---

## Overview

This [[adyen]] guide, modified and captured 2026-09-15, adds Alipay HK to an existing **React Native Drop-in** integration under Sessions or Advanced. It covers `action.type: redirect`, method-specific request/configuration absence and TEST/live Customer Area steps. See [[adyen-online-payments]] and [[source-adyen-docs-payment-methods-alipayhk|Alipay HK overview]] for the separate HK/HKD overview matrix (related raw lines 23–29). It does not demonstrate a completed redirect return, final authorization, capture or settlement. See primary raw lines 15–36 and 62–96.

## Key takeaways

- **Sessions:** the existing React Native Drop-in flow is described as Sessions, requires **Checkout API v68 or later**, `action.type: redirect` handling and Alipay HK added in Customer Area. The integration-type link in this Sessions row incorrectly points to an **Advanced-flow** URL, while the redirect and payment-session links point to Sessions. Follow the stated Sessions flow and resolved Sessions links. The v68+ gate is stated in this branch only; the Advanced table below has no API minimum. See raw lines 25–42 and 62–72.
- The Sessions branch says no *additional Alipay HK-specific* `/sessions` parameters or Drop-in configuration parameters are needed. The Advanced branch likewise says no extra Alipay HK configuration or `/payments` parameters. These statements assume the base integration and redirect handling are already implemented; they do not waive required base fields, client state or server callbacks. See raw lines 38–48 and 74–84.
- **Advanced:** the existing React Native Drop-in Advanced flow must handle `action.type: redirect` and have Alipay HK added in Customer Area. This page does not detail the shopper's return, `/payments/details`, synchronous result interpretation or a final webhook; those belong to the main integration/outcome guides. See raw lines 62–84.
- Both branches print an AlipayHK **TEST credential table** and a TEST Customer Area payment-list route, then say a request for AlipayHK in **live Customer Area** is required before accepting live payments. The presence of test credentials or a submitted live request does not show current merchant enablement, an executed test, authorization, capture or settlement. See raw lines 50–60 and 86–96.

## Detail locators

- **Sessions requirement, mismatched link, v68+ and redirect:** raw lines 25–36.
- **Sessions/Advanced Alipay HK-specific request and configuration scope:** raw lines 38–48, 74–84.
- **Advanced requirements and redirect:** raw lines 62–72.
- **Published TEST credentials, payment-list route and live request:** raw lines 50–60, 86–96.

## Related

- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-alipayhk]]
- [[adyen-payment-testing]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/alipayhk/react-native-drop-in/2026-09-15|Alipay HK React Native Drop-in — captured 2026-09-15]]
