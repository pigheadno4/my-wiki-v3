---
title: "Adyen PaySafeCard for iOS"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/paysafecard/ios"
raw_files:
  - "adyen/docs/payment-methods/paysafecard/ios/2026-09-15.md"
tags: [adyen, paysafecard, ios, drop-in, components]
---

## Overview

This 2026-09-15-captured Adyen page is an iOS integration **router** for PaySafeCard. It links separate iOS Drop-in and Components child guides and four main integration guides for Sessions and Advanced flows. It does not itself specify PaySafeCard request fields, redirect handling, tokenization, or current merchant eligibility. See [[adyen]], [[adyen-online-payments]], and [[source-adyen-docs-payment-methods-paysafecard]] for the method overview and its conditional Customer Data Exchange note.

## Key takeaways

- The iOS Drop-in route is the all-in-one UI choice. The Components route names `InstantPaymentComponent` for PaySafeCard. Follow [[source-adyen-docs-payment-methods-paysafecard-ios-drop-in]] or [[source-adyen-docs-payment-methods-paysafecard-ios-component]] for the respective method-specific instructions. See raw lines 19–27.
- Build the main iOS integration before adding PaySafeCard. This router links Sessions and Advanced base guides for both iOS UI choices. Their presence does not mean the child guides have identical method-specific prerequisites or outcomes. See raw lines 29–36.

## Detail locators

- iOS Drop-in/Components child-guide links and Component name: raw lines 19–27.
- Four Sessions/Advanced main integration routes: raw lines 29–36.

## Related

- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-paysafecard]]
- [[source-adyen-docs-payment-methods-paysafecard-ios-drop-in]]
- [[source-adyen-docs-payment-methods-paysafecard-ios-component]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/paysafecard/ios/2026-09-15|Fully read PaySafeCard iOS router raw]]
