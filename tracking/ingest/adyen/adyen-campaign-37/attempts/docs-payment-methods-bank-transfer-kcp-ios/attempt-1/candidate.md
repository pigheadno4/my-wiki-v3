---
title: "Adyen Bank Transfer via KCP for iOS chooser"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/bank-transfer-kcp/ios"
raw_files:
  - "adyen/docs/payment-methods/bank-transfer-kcp/ios/2026-09-15.md"
tags: [adyen, kcp, bank-transfer, ios, navigation]
---

## Overview

This [[adyen]] page is an **iOS integration chooser** for Bank Transfer via KCP. It links method-specific Drop-in and Components guides and four main iOS integration routes. See [[adyen-online-payments]] and [[adyen-ios-sdk]]. It is a 2026-09-15 navigation snapshot, not current merchant-eligibility or payment-outcome evidence.

## Key takeaways

- The page labels **Drop-in** as an all-in-one UI route and **Components** as an `InstantPaymentComponent` route for iOS. These descriptions identify linked guides; they do not define the Component constructor, method identifier, redirect callback, certificate authorization or settlement steps. See raw lines 19–27.
- It says to create the **main integration before adding KCP bank transfer**, and links iOS Drop-in and iOS Components main guides for both **Sessions** and **Advanced** flows. The chooser does not pick a flow, state an SDK/Checkout API version, or give method-specific setup requirements. See raw lines 29–36.
- Country/currency eligibility, KCP test-credential availability, Customer Area setup, Public Identification Certificate responsibilities, redirect details and final bank-transfer status are not specified here. Those questions require the pinned overview or relevant child guide, not extrapolation from these links. See complete raw lines 15–36.

## Detail locators

- **Method-specific Drop-in/Components links:** raw lines 19–27.
- **Main integration prerequisite and four flow links:** raw lines 29–36.

## Related

- [[adyen-online-payments]]
- [[adyen-ios-sdk]]
- [[source-adyen-docs-payment-methods-bank-transfer-kcp]]

## Related raw API references

- [[raw/adyen/docs/payment-methods/bank-transfer-kcp/ios-drop-in/2026-09-15|KCP iOS Drop-in guide]] — linked child; behavior separate.
- [[raw/adyen/docs/payment-methods/bank-transfer-kcp/ios-component/2026-09-15|KCP iOS Components guide]] — linked child; behavior separate.

## Raw Sources

- [[raw/adyen/docs/payment-methods/bank-transfer-kcp/ios/2026-09-15|KCP iOS chooser — captured 2026-09-15]]
