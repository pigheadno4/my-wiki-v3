---
title: "Clearpay for iOS | Adyen Docs"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/clearpay/ios"
raw_files:
  - "adyen/docs/payment-methods/clearpay/ios/2026-09-15.md"
tags: [adyen, clearpay, ios, navigation]
---

## Overview

This 2026-09-15-captured [[adyen]] page is an **iOS integration chooser** for Clearpay. It links the iOS Drop-in and Components child guides and four main iOS integration guides. The linked [[source-adyen-docs-payment-methods-clearpay]] overview supplies the GB/GBP product and regional-brand scope; this chooser itself does not state request fields, merchant eligibility or a payment outcome. See [[adyen-online-payments]].

## Key takeaways

- **Child routes:** Drop-in is described as the all-in-one UI solution for an iOS app. Components points to the `InstantPaymentComponent` route. Select and read the child guide for its own server-flow, request, redirect and lifecycle conditions (raw lines 19–27).
- **Base integration first:** The page says to create the main integration before adding Clearpay, and links iOS Drop-in and Components guides for both **Sessions** and **Advanced** flows (raw lines 29–36). These links are navigation, not a statement that the two Clearpay child guides have identical prerequisites or that the method is enabled for a merchant.
- The chooser does not identify country/currency or recurring support on this page. Use the linked Clearpay overview for product scope and the chosen child guide for implementation specifics.

## Detail locators

- Purpose and child Drop-in/Components routes: pinned raw `# Clearpay for iOS` and `### How do you want to integrate?`, lines 15–27.
- Main integration prerequisite and iOS Sessions/Advanced base routes: pinned raw `## See also`, lines 29–36.

## Related

- [[adyen-online-payments]] — provider checkout context.
- [[source-adyen-docs-payment-methods-clearpay]] — GB/GBP product and regional-brand overview.
- [[source-adyen-docs-payment-methods-clearpay-ios-drop-in]] — iOS Drop-in add-on.
- [[source-adyen-docs-payment-methods-clearpay-ios-component]] — iOS Components add-on.

## Raw Sources

- [[raw/adyen/docs/payment-methods/clearpay/ios/2026-09-15|Clearpay iOS chooser, captured 2026-09-15]]
