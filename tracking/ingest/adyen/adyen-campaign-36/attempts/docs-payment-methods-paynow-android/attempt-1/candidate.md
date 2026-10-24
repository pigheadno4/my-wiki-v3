---
title: "Adyen PayNow for Android integration chooser"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/paynow/android"
raw_files:
  - "adyen/docs/payment-methods/paynow/android/2026-09-15.md"
tags: [adyen, paynow, android, navigation]
---

## Overview

This [[adyen]] **PayNow for Android** page is an integration chooser. It links a PayNow **Android Drop-in** child guide and an **Android Components** child guide naming `InstantPaymentComponent`, then links main Android Sessions and Advanced guides for each UI path. Its brief Components label says “handle the redirect to PayNow”; that label is not an `action.type` contract. The linked Android Component guide separately describes an Advanced `qrCode` action. This chooser itself supplies no QR payload, app-switch procedure, version requirement, test-money warning, merchant setup or payment outcome. [[adyen-online-payments]]

## Key takeaways

- **Method-specific children:** Drop-in is described as an all-in-one UI solution; the Components route names `InstantPaymentComponent` and describes a redirect to PayNow. The separate child guide is needed for action handling; its Advanced requirement uses `qrCode`, so do not translate this chooser's plain-language “redirect” into an API action type. See pinned raw lines 19–27; related Android Component raw line 144.
- **Main integration first:** The See also section says to create the main integration before adding PayNow and links Android Drop-in/Components under both Sessions and Advanced. Their requirements, banking-app testing implications and final-status behavior are not on this page. See pinned raw lines 29–36.

## Detail locators

- PayNow Android Drop-in and Components child links: raw lines 19–27.
- Main Android Sessions/Advanced routes: raw lines 29–36.
- Related child action-type distinction: `raw/adyen/docs/payment-methods/paynow/android-component/2026-09-15.md` line 144.

## Related

- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-paynow-android-component]]
- [[adyen]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/paynow/android/2026-09-15|Adyen PayNow Android chooser snapshot]]
