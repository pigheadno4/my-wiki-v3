---
title: "Boost Wallet for iOS"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/boost/ios"
raw_files:
  - "adyen/docs/payment-methods/boost/ios/2026-09-15.md"
tags: [adyen, boost, ios, wallet, integration-navigation]
---

## Overview

Adyen's 2026-09-15 Boost Wallet iOS page is a **navigation chooser** for adding Boost Wallet to an iOS app. It routes to a Drop-in child guide or an `InstantPaymentComponent` child guide, and to the iOS Sessions/Advanced base integration guides. It gives no request schema, country/currency eligibility rule, testing procedure, or payment outcome itself. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- The Drop-in route is described as an all-in-one UI solution; the Components route names `InstantPaymentComponent`. These are choices of child guides, not proof that either route is configured for a merchant. [Raw lines 19–27]
- The page instructs readers to create the main integration before adding Boost Wallet and lists iOS Drop-in and Components guides for both Sessions and Advanced flows. Child pages provide method-specific implementation details; this chooser alone does not state their version requirements, redirect/action behavior, test/live availability, or final result handling. [Raw lines 29–36]

## Related

- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-boost-ios-drop-in]] — child Drop-in guide; navigate for its own evidence.
- [[source-adyen-docs-payment-methods-boost-ios-component]] — child Components guide; navigate for its own evidence.

## Raw Sources

- [[raw/adyen/docs/payment-methods/boost/ios/2026-09-15|Boost Wallet for iOS (2026-09-15)]]
