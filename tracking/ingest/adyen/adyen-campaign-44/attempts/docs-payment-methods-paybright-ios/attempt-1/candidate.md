---
title: "Adyen PayBright iOS integration chooser"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/paybright/ios"
raw_files:
  - "adyen/docs/payment-methods/paybright/ios/2026-09-15.md"
tags: [adyen, paybright, ios, drop-in, components]
---

## Overview

This [[adyen]] page is a short **iOS route chooser** for PayBright. It links to an all-in-one Drop-in guide and a Redirect Component guide, plus general iOS Sessions integration pages. It explicitly says PayBright was acquired by Affirm and **Adyen will not accept new PayBright integrations** (raw line 19). Use [[adyen-online-payments]] and [[source-adyen-docs-payment-methods-paybright]] for the product scope; this chooser does not itself establish live availability or a completed payment.

## Key takeaways

- **Integration boundary:** The page points to PayBright iOS Drop-in for an all-in-one UI and iOS Components for a Redirect Component (raw lines 21–33). Its final line points to general iOS Sessions Drop-in and Components guides (raw line 35). These links select implementation documentation; they do not provide request fields, SDK version, shopper-return handling, outcome, capture or refund behavior.
- **No-new-integration warning:** The acquisition and no-new-PayBright-integrations statement applies even though the page still describes how to add PayBright to an iOS app (raw lines 15–19). The child guides describe existing integration flows; a link here is not authorization to onboard a new PayBright integration.

## Detail locators

- Page identity and restriction: pinned raw lines 15–19.
- PayBright Drop-in and Redirect Component routes: pinned raw lines 21–33.
- General iOS Sessions guide routes: pinned raw line 35.

## Related

- [[adyen-online-payments]] — provider online-payment context.
- [[source-adyen-docs-payment-methods-paybright]] — CA/CAD redirect BNPL overview and no-new-integration restriction.
- [[source-adyen-docs-payment-methods-paybright-ios-drop-in]] — child Drop-in implementation guide.
- [[source-adyen-docs-payment-methods-paybright-ios-component]] — child Redirect Component implementation guide.

## Raw Sources

- [[raw/adyen/docs/payment-methods/paybright/ios/2026-09-15|PayBright iOS chooser, captured 2026-09-15]]
