---
title: "Adyen EPS for iOS integration chooser"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/eps/ios"
raw_files:
  - "adyen/docs/payment-methods/eps/ios/2026-09-15.md"
tags: [adyen, eps, ios, integration-guide, online-payments]
---

## Overview

A short **iOS integration chooser** for EPS. It routes an iOS app to either [EPS iOS Drop-in](https://docs.adyen.com/payment-methods/eps/ios-drop-in), described as an all-in-one UI, or [EPS iOS Components](https://docs.adyen.com/payment-methods/eps/ios-component), described as using `EPSComponent`. It says to create the main integration before adding EPS. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- The page links four base-guide combinations: iOS Drop-in with Sessions, iOS Components with Sessions, iOS Drop-in with Advanced, and iOS Components with Advanced. Select the UI route and server-side flow before reading the corresponding child guide. See raw lines 19–36.
- This chooser itself provides no request fields, SDK/version prerequisite, bank redirect action/result handling, tokenization, capture/refund, test conditions or merchant eligibility. Use the child guide and EPS overview for those claims; the links are navigation, not evidence of a completed integration or payment. See raw lines 15–36.

## Detail locators

- Drop-in versus `EPSComponent` route descriptions: raw lines 19–27.
- Main integration prerequisite and four Sessions/Advanced base-guide links: raw lines 29–36.

## Related

- [[source-adyen-docs-payment-methods-eps]] — EPS method overview and bank-redirect context
- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/eps/ios/2026-09-15|EPS iOS chooser documentation capture (2026-09-15)]]
