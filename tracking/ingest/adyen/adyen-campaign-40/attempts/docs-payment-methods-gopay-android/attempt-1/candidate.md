---
title: "Adyen GoPay for Android integration chooser"
type: source
date_ingested: 2026-10-26
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/gopay/android"
raw_files:
  - "adyen/docs/payment-methods/gopay/android/2026-09-15.md"
tags: [adyen, gopay, android, drop-in, components]
---

## Overview

This 2026-09-15 Adyen page is an **Android integration chooser** for GoPay. It routes to Android Drop-in or Android Components child guides and to the corresponding Sessions and Advanced main integration guides. It does not specify request fields, eligibility, redirect completion, tokenization or final payment outcome; those belong to the linked guides. This captured route does not prove current enablement or a successful payment. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- The Drop-in route is described as Adyen's all-in-one UI solution for adding GoPay to an Android app; implementation details are delegated to the Android Drop-in child page. (raw lines 19–23)
- The Components route names `InstantPaymentComponent` for handling the redirect to GoPay; the Components child page provides actual flow requirements and result handling. This chooser alone does not establish a completed redirect or authorization. (raw lines 25–27)
- The page says to build the main integration before adding GoPay and links four Android base routes: Drop-in Sessions, Components Sessions, Drop-in Advanced and Components Advanced. A route list does not assert that every child flow shares the same prerequisites or is enabled for a given merchant. (raw lines 29–36)

## Detail locators

- Android identity and child integration choices: pinned raw lines 15–27.
- Four main Sessions/Advanced Drop-in/Components guides: pinned raw lines 29–36.

## Related

- [[adyen-online-payments]] — provider integration context
- [[source-adyen-docs-payment-methods-gopay-android-drop-in]] — Android Drop-in implementation
- [[source-adyen-docs-payment-methods-gopay-android-component]] — Android Components implementation
- [[source-adyen-docs-payment-methods-gopay]] — GoPay method overview

## Raw Sources

- [[raw/adyen/docs/payment-methods/gopay/android/2026-09-15|GoPay Android chooser, 2026-09-15]]
