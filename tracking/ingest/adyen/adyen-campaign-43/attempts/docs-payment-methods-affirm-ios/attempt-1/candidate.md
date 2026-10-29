---
title: "Adyen Affirm for iOS chooser"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/affirm/ios"
raw_files:
  - "adyen/docs/payment-methods/affirm/ios/2026-09-15.md"
tags: [adyen, affirm, ios, drop-in, components, redirect]
---

## Overview

This 2026-09-15 Affirm iOS page is an integration chooser for an iOS app. It offers a Drop-in child guide and a Components child guide, then points to the iOS Sessions base integrations. The Components description names the Redirect Component for the Affirm redirect. It does not provide the request fields, financing choices, capture deadline, outcome handling, refund rules, eligibility or live setup itself; consult the child guides and [[source-adyen-docs-payment-methods-affirm|Affirm overview]] for those topics. See [[adyen]], [[adyen-online-payments]] and [[adyen-ios-sdk]].

## Key takeaways

- Choose the iOS Drop-in child for an all-in-one UI or the iOS Components child for a Redirect Component that handles the redirect to Affirm. Those are navigation descriptions, not a complete integration or proof that a payment succeeds.
- The page links to iOS Drop-in and Components Sessions base guides for more information. It does not say that Advanced flow is unavailable; the child guides own flow-specific conditions and required fields.
- The captured guide is iOS-specific. It does not establish current merchant or shopper eligibility, production credentials, financing approval, authorisation, capture or settlement.

## Detail locators

- Identity, capture date and iOS scope: pinned raw lines 1–17. Drop-in and Redirect Component child links: lines 19–27. iOS Sessions base-guide links: line 29.

## Related

- [[adyen-online-payments]] — primary provider integration route
- [[adyen-ios-sdk]] — iOS platform context
- [[source-adyen-docs-payment-methods-affirm]] — method and financing overview
- [[source-adyen-docs-payment-methods-affirm-ios-drop-in]] — iOS Drop-in child guide
- [[source-adyen-docs-payment-methods-affirm-ios-component]] — iOS Components child guide

## Raw Sources

- [[raw/adyen/docs/payment-methods/affirm/ios/2026-09-15|Affirm iOS chooser, captured 2026-09-15]]
