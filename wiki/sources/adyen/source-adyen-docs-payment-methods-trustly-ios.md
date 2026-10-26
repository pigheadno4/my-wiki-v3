---
title: "Adyen Trustly for iOS"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/trustly/ios"
raw_files:
  - "adyen/docs/payment-methods/trustly/ios/2026-09-15.md"
tags: [adyen, trustly, ios, drop-in, components, redirect]
---

## Overview

Adyen's 2026-09-15 Trustly for iOS page is a chooser for adding Trustly to an iOS app. It links an all-in-one Drop-in child guide and a child guide described as using a Redirect Component, then points to general iOS Drop-in and Components **Sessions** guides. See [[adyen]], [[adyen-ios-sdk]], and the separate [[source-adyen-docs-payment-methods-trustly|Trustly overview]].

## Key takeaways

- The Drop-in link describes an all-in-one UI; the Components link says to use a Redirect Component on iOS. These are child-guide routes, not a complete redirect or payment-result procedure (raw lines 19-31).
- Both general integration links on this chooser point to Sessions flow (raw line 33). This page does not state an Advanced route, request fields, SDK minimum, method setup, testing, current eligibility or outcome finality; consult the applicable child and base guides (raw lines 15-33).
- **Related funds warning from the approved Trustly overview, not this chooser:** a successful `AUTHORISATION` webhook means a bank transfer was initiated after checks; Adyen may still not receive funds. The transfer can fail, and the overview says Trustly chargebacks cannot be defended (overview raw lines 38-53). Choosing an iOS integration route does not change that financial boundary.

## Related raw API references

- [[raw/adyen/docs/payment-methods/trustly/ios-drop-in/2026-09-15|Trustly iOS Drop-in child guide (unread navigation)]]
- [[raw/adyen/docs/payment-methods/trustly/ios-component/2026-09-15|Trustly iOS Components child guide (navigation)]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/trustly/ios/2026-09-15|Trustly for iOS chooser (2026-09-15 snapshot)]]
