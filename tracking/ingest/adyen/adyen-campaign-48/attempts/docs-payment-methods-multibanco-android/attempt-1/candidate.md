---
title: "Multibanco for Android integration chooser"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/multibanco/android"
raw_files:
  - "adyen/docs/payment-methods/multibanco/android/2026-09-15.md"
tags: [adyen, multibanco, android, integration-router]
---

## Overview

This 2026-09-15-captured Adyen page is the **Android integration chooser** for Multibanco. It routes to Android Drop-in or Android Components, then to the corresponding Sessions or Advanced base guides. It does not itself specify payment request fields, voucher handling, test setup or live eligibility. See [[adyen]], [[adyen-online-payments]], and the [[source-adyen-docs-payment-methods-multibanco|Multibanco overview]] for method context.

## Key takeaways

- The **Drop-in** route is described as Adyen's all-in-one UI solution for adding Multibanco to an Android app. Follow [[source-adyen-docs-payment-methods-multibanco-android-drop-in]] for method-specific Sessions/Advanced details, including the voucher action and test-offer promotion (raw lines 19–23).
- The **Components** route says to use `InstantPaymentComponent` to handle the redirect to Multibanco. Follow [[source-adyen-docs-payment-methods-multibanco-android-component]] for the actual component, flow and voucher-action details. The chooser's “redirect” wording is a route description; it does not establish a separate API action type or prove a completed payment (raw lines 25–27).
- The **See also** list points to the main Android Drop-in and Components guides for both Sessions and Advanced flows. It explicitly says to create the main integration before adding Multibanco. This page is navigation, not a complete implementation recipe (raw lines 29–36).
- The separate [[source-adyen-docs-payment-methods-multibanco|method overview]] explains the PT/EUR voucher journey: a shopper receives a voucher and later pays at an ATM or through online banking. Voucher issue is not payment completion (overview pinned raw lines 23–36).

## Detail locators

- Android chooser and Drop-in route: raw lines 15–23.
- Components and `InstantPaymentComponent` route: raw lines 25–27.
- Sessions/Advanced base-guide links and prerequisite main integration: raw lines 29–36.
- Method-level voucher lifecycle and PT/EUR: [[source-adyen-docs-payment-methods-multibanco]] and its pinned raw lines 23–36; this entry's raw_files remains chooser-only.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-multibanco]]
- [[source-adyen-docs-payment-methods-multibanco-android-drop-in]]
- [[source-adyen-docs-payment-methods-multibanco-android-component]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/multibanco/android/2026-09-15|Multibanco Android chooser, captured 2026-09-15]]
