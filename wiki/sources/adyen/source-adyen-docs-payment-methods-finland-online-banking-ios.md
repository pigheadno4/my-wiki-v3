---
title: "Online banking Finland for iOS"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/finland-online-banking/ios"
raw_files:
  - "adyen/docs/payment-methods/finland-online-banking/ios/2026-09-15.md"
tags: [adyen, finland-online-banking, ios, integration-chooser]
---

## Overview

This 2026-09-15-captured Adyen page is an **iOS integration chooser** for Online banking Finland. It routes developers to method-specific Drop-in and Components guides and to four main iOS Sessions/Advanced integration guides. It does not itself provide request fields, SDK or API minimums, issuer handling, payment status, or evidence of current merchant enablement. See [[adyen]], [[adyen-online-payments]], and the separate method overview [[source-adyen-docs-payment-methods-finland-online-banking]] for Paytrail, FI/EUR and capability context with its own bank-selection/refund-note qualifications.

## Key takeaways

- **Drop-in route:** the chooser links /payment-methods/finland-online-banking/ios-drop-in and describes it as an all-in-one iOS UI solution (raw lines 19–23). The captured child is [[source-adyen-docs-payment-methods-finland-online-banking-ios-drop-in]]; this chooser does not state that child's setup or redirect requirements.
- **Components route:** the chooser links /payment-methods/finland-online-banking/ios-component and says to use InstantPaymentComponent for Online banking Finland in an iOS app (raw lines 25–27). The captured child is [[source-adyen-docs-payment-methods-finland-online-banking-ios-component]]; its implementation details belong to that guide.
- **Main integration first:** the See also section says to create the main integration before adding the method, then links iOS Drop-in and Components guides for both Sessions and Advanced flows (raw lines 29–36). These are navigation routes, not evidence that a particular flow, version or merchant setup has already succeeded.

## Detail locators

- iOS Drop-in and Components choices: raw How do you want to integrate?, lines 19–27.
- Main iOS Sessions and Advanced integration routes: raw See also, lines 29–36.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-finland-online-banking]]
- [[source-adyen-docs-payment-methods-finland-online-banking-ios-drop-in]]
- [[source-adyen-docs-payment-methods-finland-online-banking-ios-component]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/finland-online-banking/ios/2026-09-15|Online banking Finland iOS chooser, captured 2026-09-15]]
