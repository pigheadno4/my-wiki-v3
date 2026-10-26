---
title: "Adyen MobilePay iOS integration chooser"
type: source
date_ingested: 2026-10-26
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/mobilepay/ios"
raw_files:
  - "adyen/docs/payment-methods/mobilepay/ios/2026-09-15.md"
tags: [adyen, mobilepay, ios, drop-in, components]
---

## Overview

This 2026-09-15 Adyen iOS page is a chooser for adding MobilePay to an iOS app. It routes to a Drop-in child guide and an `InstantPaymentComponent` child guide, and it links the main iOS Sessions and Advanced integration guides for both UI choices. It supplies no method-specific request fields, API or SDK version, eligibility, outcome, payout, or live setup rule; consult the child and main guides for those details. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- Choose the iOS Drop-in guide for Adyen's all-in-one UI route or the iOS Components guide for `InstantPaymentComponent`. These are navigation options, not evidence that the two integrations are interchangeable.
- The page says to create the main integration first and links four main routes: iOS Drop-in Sessions, iOS Components Sessions, iOS Drop-in Advanced, and iOS Components Advanced. It does not itself establish payment behavior, merchant eligibility or a completed payment.

## Detail locators

- Drop-in and Components child-guide choices: pinned raw lines 19–27.
- Main-integration prerequisite and four flow/UI links: pinned raw lines 29–36.

## Related

- [[adyen-online-payments]] — provider concept and source route
- [[source-adyen-docs-payment-methods-mobilepay-ios-drop-in]] — iOS Drop-in child guide; separate authority for its setup and behavior
- [[source-adyen-docs-payment-methods-mobilepay-ios-component]] — iOS Components child guide; separate authority for its setup and behavior

## Raw Sources

- [[raw/adyen/docs/payment-methods/mobilepay/ios/2026-09-15|MobilePay iOS chooser, 2026-09-15]]
