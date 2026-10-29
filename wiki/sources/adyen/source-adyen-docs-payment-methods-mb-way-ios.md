---
title: "Adyen MB WAY for iOS"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/mb-way/ios"
raw_files:
  - "adyen/docs/payment-methods/mb-way/ios/2026-09-15.md"
tags: [adyen, mb-way, ios, drop-in, components]
---

## Overview

This 2026-09-15-captured Adyen page is an iOS integration **router** for MB WAY. It links separate iOS Drop-in and Components child guides and four main integration guides for Sessions and Advanced flows. It does not itself specify request fields, phone-number or App2App conditions, payment outcomes, or account eligibility. See [[adyen]], [[adyen-online-payments]], and [[source-adyen-docs-payment-methods-mb-way]] for the payment-method overview.

## Key takeaways

- The iOS Drop-in route is described as an all-in-one UI solution. The Components route names `MBWayComponent` for iOS. Follow [[source-adyen-docs-payment-methods-mb-way-ios-drop-in]] or [[source-adyen-docs-payment-methods-mb-way-ios-component]] for method-specific setup and flow conditions. See raw lines 19–27.
- Build the main iOS integration first. The page links Sessions and Advanced main guides for both Drop-in and Components; these are navigation routes, not an assertion that each flow has identical MB WAY request or action behavior. See raw lines 29–36.

## Detail locators

- iOS UI choices and child-guide links: raw lines 19–27.
- Sessions/Advanced main integration links for both UIs: raw lines 29–36.

## Related

- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-mb-way]]
- [[source-adyen-docs-payment-methods-mb-way-ios-drop-in]]
- [[source-adyen-docs-payment-methods-mb-way-ios-component]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/mb-way/ios/2026-09-15|Fully read MB WAY iOS router raw]]
