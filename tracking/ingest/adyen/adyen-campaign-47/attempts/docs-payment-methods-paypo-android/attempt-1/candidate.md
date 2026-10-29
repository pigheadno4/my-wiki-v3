---
title: "PayPo Android integration chooser"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/paypo/android"
raw_files:
  - "adyen/docs/payment-methods/paypo/android/2026-09-15.md"
tags: [adyen, paypo, android, drop-in, components]
---

## Overview

This 2026-09-15-captured PayPo Android page is an **integration chooser**. It routes Android merchants to PayPo Drop-in or Components instructions and to the main Android Sessions/Advanced guides. It does not itself specify request fields, component versions, capture behavior, merchant eligibility, or successful live processing. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- **Drop-in** is described as an all-in-one UI solution for adding PayPo to an Android app; the page links the PayPo Android Drop-in child guide (raw lines 19–23).
- **Components** links the PayPo Android Component child guide and says to use `InstantPaymentComponent` for the redirect to PayPo. This chooser labels the component route but does not give its setup or action-handling procedure (raw lines 25–27).
- The “See also” section says to create the main integration first and links **Android Drop-in** and **Android Components**, each with **Sessions** and **Advanced** server-side flows. Follow the selected base guide and method child together (raw lines 29–36).

## Detail locators

- Drop-in versus Components chooser: raw `### How do you want to integrate?` lines 19–27.
- Main integration prerequisites and four flow/UI routes: raw `## See also` lines 29–36.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-paypo-android-drop-in]]
- [[source-adyen-docs-payment-methods-paypo-android-component]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/paypo/android/2026-09-15|PayPo Android chooser, captured 2026-09-15]]
