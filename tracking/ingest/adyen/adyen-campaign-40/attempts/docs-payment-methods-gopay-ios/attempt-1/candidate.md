---
title: "GoPay for iOS"
type: source
date_ingested: 2026-10-26
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/gopay/ios"
raw_files:
  - "adyen/docs/payment-methods/gopay/ios/2026-09-15.md"
tags: [adyen, gopay, ios, drop-in, components, online-payments]
---

## Overview

This 2026-09-15 GoPay iOS page is an **integration chooser**. It routes an iOS app to a Drop-in child guide or a Components child guide using `InstantPaymentComponent`, and links separate iOS Sessions and Advanced base guides for each integration type. It says to create the main integration before adding GoPay. [[adyen]] [[adyen-ios-sdk]] [[adyen-online-payments]]

## Key takeaways

- Select **Drop-in** for the all-in-one iOS UI path; its method-specific instructions are in [[source-adyen-docs-payment-methods-gopay-ios-drop-in]]. See raw lines 19–23.
- Select **Components** for the iOS `InstantPaymentComponent` path; its method-specific instructions are in [[source-adyen-docs-payment-methods-gopay-ios-component]]. See raw lines 25–27.
- The page links four main integration guides: iOS Drop-in Sessions, Components Sessions, Drop-in Advanced and Components Advanced. Those are prerequisites/navigation, not instructions for this method's request fields, redirect handling, tokenization, testing or outcome. See raw lines 29–36.
- This chooser alone does not establish SDK/API version requirements, current GoPay eligibility, an enabled merchant account or an executed payment. Consult the selected child and base guide for those details. See raw lines 15–36.

## Detail locators

- iOS Drop-in and Components child routes: raw lines 19–27.
- Four iOS Sessions/Advanced main-guide links: raw lines 29–36.

## Related

- [[adyen-ios-sdk]] — iOS integration architecture.
- [[adyen-online-payments]] — online payment-method context.
- [[source-adyen-docs-payment-methods-gopay]] — GoPay method overview.
- [[source-adyen-docs-payment-methods-gopay-ios-drop-in]] — iOS Drop-in child.
- [[source-adyen-docs-payment-methods-gopay-ios-component]] — iOS Components child.

## Raw Sources

- [[raw/adyen/docs/payment-methods/gopay/ios/2026-09-15|GoPay iOS chooser, captured 2026-09-15]]
