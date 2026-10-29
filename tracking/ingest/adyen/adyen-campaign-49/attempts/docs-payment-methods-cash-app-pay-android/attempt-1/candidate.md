---
title: "Cash App Pay for Android integration chooser"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/cash-app-pay/android"
raw_files:
  - "adyen/docs/payment-methods/cash-app-pay/android/2026-09-15.md"
tags: [adyen, cash-app-pay, android, integration-router]
---

## Overview

This Cash App Pay Android page, captured on 2026-09-15 and marked last modified 2019-09-30 in the raw, is an **integration chooser**. It links Android Drop-in and Components child guides and two Sessions base-guide routes. It concerns **Cash App Pay**, a distinct payment method from Cash App Afterpay. The chooser does not itself establish request fields, SDK/version requirements, result finality, tokenization consent, current account eligibility or a successful payment. See [[adyen]], [[adyen-online-payments]] and the [[source-adyen-docs-payment-methods-cash-app-pay|method overview]].

## Key takeaways

- The **Drop-in** path is described as Adyen's all-in-one UI for Cash App Pay on Android. Follow [[source-adyen-docs-payment-methods-cash-app-pay-android-drop-in]] for method-specific prerequisites, Sessions/Advanced additions and asynchronous result handling; the chooser's link alone does not supply those rules (raw lines 19–23).
- The **Components** path is described as a prebuilt Component for rendering Cash App Pay in an Android app. Follow [[source-adyen-docs-payment-methods-cash-app-pay-android-component]] for the Component's version and flow details (raw lines 25–27).
- The page's final line routes to **Android Drop-in or Components Sessions-flow base guides**. It does not list Advanced base-guide links, although the approved method-specific child guides cover Advanced as well; this chooser's limited navigation should not be mistaken for an Advanced-flow exclusion (raw line 29).
- The separate [[source-adyen-docs-payment-methods-cash-app-pay|Cash App Pay overview]] describes the method's **US/USD wallet** scope and conditional adjustment/chargeback information. The child guides supply payment-result and tokenization details. This chooser does not resolve those financial or finality conditions (overview pinned raw lines 23–44).

## Detail locators

- Cash App Pay Android identity and chooser: raw lines 15–19.
- Drop-in child route: raw lines 21–23.
- Components child route: raw lines 25–27.
- Sessions base-guide routes only: raw line 29.
- Method-level wallet, US/USD and conditional financial context: [[source-adyen-docs-payment-methods-cash-app-pay]] and its pinned raw lines 23–44; this entry's raw_files remains chooser-only.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-cash-app-pay]]
- [[source-adyen-docs-payment-methods-cash-app-pay-android-drop-in]]
- [[source-adyen-docs-payment-methods-cash-app-pay-android-component]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/cash-app-pay/android/2026-09-15|Cash App Pay Android chooser, captured 2026-09-15]]
