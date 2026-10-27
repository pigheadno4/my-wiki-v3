---
title: "ACH Direct Debit for iOS | Adyen Docs"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/ach-direct-debit/ios"
raw_files:
  - "adyen/docs/payment-methods/ach-direct-debit/ios/2026-09-15.md"
tags: [adyen, ach-direct-debit, ios, drop-in, components, integration-chooser]
---

## Overview

This 2026-09-15 page is an ACH Direct Debit **iOS integration chooser**, not a payment-request or outcome guide. It routes an existing iOS app toward ACH iOS Drop-in or the `ACHDirectDebitComponent` child guide, and separately points to the main iOS Sessions/Advanced integration guides that must be followed before adding ACH (raw lines 15–36).

## Key takeaways

- Choose the all-in-one [[source-adyen-docs-payment-methods-ach-direct-debit-ios-drop-in|iOS Drop-in guide]] or the [[source-adyen-docs-payment-methods-ach-direct-debit-ios-component|iOS Components guide]] using `ACHDirectDebitComponent`; these are distinct UI paths, and this chooser states no request fields, SDK minimum, method activation or payment lifecycle requirements (raw lines 19–27).
- The page links four base paths: iOS Drop-in with Sessions, iOS Components with Sessions, iOS Drop-in with Advanced, and iOS Components with Advanced. It says to create the main integration before adding ACH. Read the selected child and base flow for implementation specifics; the directory links alone do not prove merchant enablement, bank-account validation, authorization or settlement (raw lines 29–36).
- The related [[source-adyen-docs-payment-methods-ach-direct-debit|ACH overview]] supplies method-level prerequisites and risks: US business-entity requirement, consumer account validation, correct SEC code and signed mandate, no real-time authorization, reversals and nondefendable chargebacks. Those are overview claims, not instructions supplied by this chooser (overview raw lines 23–29, 35–74). The 2026-09-15 snapshot does not establish current availability or payment success (this raw lines 2, 11).

## Detail locators

- Purpose and iOS Drop-in/Components choices: raw lines 15–27.
- Four main Sessions/Advanced iOS route links and prerequisite wording: raw lines 29–36.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-ach-direct-debit|ACH overview (method-level eligibility and risk)]]
- [[source-adyen-docs-payment-methods-ach-direct-debit-ios-drop-in|iOS Drop-in child guide]]
- [[source-adyen-docs-payment-methods-ach-direct-debit-ios-component|iOS Components child guide]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/ach-direct-debit/ios/2026-09-15|ACH Direct Debit for iOS, fetched 2026-09-15]]
