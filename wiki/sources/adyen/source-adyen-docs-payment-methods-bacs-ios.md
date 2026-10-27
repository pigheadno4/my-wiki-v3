---
title: "Adyen BACS Direct Debit for iOS"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/bacs/ios"
raw_files:
  - "adyen/docs/payment-methods/bacs/ios/2026-09-15.md"
tags: [adyen, bacs, direct-debit, ios, navigation]
---

## Overview

Adyen's 2026-09-15 BACS Direct Debit iOS page is an integration chooser. It routes an iOS app to the Drop-in or `BACSDirectDebitComponent` child guide and points to general iOS Sessions and Advanced base integrations. It does not itself specify BACS request fields, mandates, tokenization, action handling or a payment outcome. See [[adyen]] and [[adyen-ios-sdk]].

## Key takeaways

- The Drop-in route is labeled an all-in-one UI solution for adding BACS Direct Debit to an iOS app; the Components route names `BACSDirectDebitComponent` (raw lines 19-27). The linked children, not this chooser, own method-specific setup and behavior.
- The page says to create the main integration before adding BACS and links four base routes: iOS Drop-in and Components, each with Sessions and Advanced flow (raw lines 29-36). Those links are navigation, not proof that a specific account or BACS child flow is enabled or that a debit has cleared.
- For method-level Direct Debit Instruction, processing delay, advance-notice and chargeback conditions, follow [[source-adyen-docs-payment-methods-bacs]]; this chooser contains none of those operational terms.

## Related raw API references

- [[raw/adyen/docs/payment-methods/bacs/ios-drop-in/2026-09-15|BACS iOS Drop-in child guide (unread navigation)]]
- [[raw/adyen/docs/payment-methods/bacs/ios-component/2026-09-15|BACS iOS Component child guide (unread navigation)]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/bacs/ios/2026-09-15|BACS Direct Debit iOS chooser (2026-09-15 snapshot)]]
