---
title: "Adyen Google Pay for Android integration chooser"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/google-pay/android"
raw_files:
  - "adyen/docs/payment-methods/google-pay/android/2026-09-15.md"
tags: [adyen, google-pay, android, integration-chooser, online-payments]
---

## Overview

This 2026-09-15 Adyen **Android Google Pay chooser** links to separate **Android Drop-in** and **Android Component** add-on guides, and to the base Android Sessions/Advanced integration guides. It is navigation for choosing a route after a main integration exists. It does not itself give SDK/API versions, merchant or Google setup, wallet-token handling, a redirect implementation, TEST/LIVE conditions, current method eligibility, or payment outcomes. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- The page presents two Android app routes: **Drop-in**, described as an all-in-one UI solution, and **Components**, described using `GooglePayComponent` with a redirect to Google Pay. These are child-guide labels, not a complete component lifecycle or evidence of an executed redirect. (raw lines 19–27)
- It instructs readers to build the main integration first and links all four base combinations: Android Drop-in/Components with Sessions, and Android Drop-in/Components with Advanced. The page does not choose a flow for the merchant or state that the child guides have identical prerequisites. (raw lines 29–36)
- Follow the selected child guide for actual prerequisites, version gates, configuration, Google account/device/card scope, TEST/LIVE setup and authorization-result handling. A route from this chooser is not proof of wallet availability, shopper authentication, payment authorization, capture or settlement. (raw lines 19–36)

## Detail locators

- Android purpose and child-guide choices: raw lines 15–27.
- Main Sessions/Advanced integration navigation: raw lines 29–36.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-google-pay-android-drop-in]]
- [[source-adyen-docs-payment-methods-google-pay-android-component]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/google-pay/android/2026-09-15|Adyen Google Pay Android chooser, 2026-09-15 snapshot]]
