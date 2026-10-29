---
title: "Adyen PayPo for iOS"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/paypo/ios"
raw_files:
  - "adyen/docs/payment-methods/paypo/ios/2026-09-15.md"
tags: [adyen, paypo, ios, drop-in, components]
---

## Overview

This 2026-09-15-captured Adyen page is an iOS integration **router** for PayPo. It links separate iOS Drop-in and Components guides, plus Sessions and Advanced main integration guides for each UI. It does not itself specify payment fields, redirect handling, capture rules, or current merchant eligibility. See [[adyen]], [[adyen-online-payments]], and [[source-adyen-docs-payment-methods-paypo]] for the payment-method overview.

## Key takeaways

- Choose iOS Drop-in for the all-in-one UI or follow the iOS Components child guide for a Component integration. The Components description literally says “Use the None”; that is a broken/placeholder component name, not an SDK symbol to implement. See raw lines 19–27 and the child routes [[source-adyen-docs-payment-methods-paypo-ios-drop-in]] and [[source-adyen-docs-payment-methods-paypo-ios-component]].
- Build the main iOS integration before adding PayPo. The page links Sessions and Advanced base guides for both Drop-in and Components. The chosen child guide owns PayPo-specific requirements and outcomes; the router's links alone do not establish a working payment flow. See raw lines 29–36.

## Detail locators

- Drop-in and Components child-guide links and malformed `None` description: raw lines 19–27.
- Four iOS base-integration routes: raw lines 29–36.

## Related

- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-paypo]]
- [[source-adyen-docs-payment-methods-paypo-ios-drop-in]]
- [[source-adyen-docs-payment-methods-paypo-ios-component]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/paypo/ios/2026-09-15|Fully read PayPo iOS router raw]]
