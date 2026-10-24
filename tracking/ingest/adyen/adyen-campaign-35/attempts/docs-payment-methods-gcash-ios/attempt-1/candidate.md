---
title: "Adyen GCash for iOS integration chooser"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/gcash/ios"
raw_files:
  - "adyen/docs/payment-methods/gcash/ios/2026-09-15.md"
tags: [adyen, gcash, ios, navigation]
---

## Overview

This [[adyen]] GCash for iOS page is an **integration chooser**. It routes to separate GCash **iOS Drop-in** and **iOS Components** guides, and to main iOS **Sessions** and **Advanced** integration guides for each UI route. The Components label names `InstantPaymentComponent`, but this page provides no component setup, SDK/API versions, merchant eligibility, transaction-status contract or evidence of a completed payment. [[adyen-online-payments]]

## Key takeaways

- **Method-specific children:** Drop-in is described as an all-in-one UI solution; the Components route says to use `InstantPaymentComponent` for GCash in an iOS app. These statements are navigation labels for separate child guides, not full implementation instructions. See raw lines 19–27.
- **Main integration first:** The page directs readers to create the main integration before adding GCash, and links iOS Drop-in and Components guides for both Sessions and Advanced flows. Flow requirements, callback behavior and outcomes belong to those guides, not this chooser. See raw lines 29–36.

## Detail locators

- GCash iOS Drop-in and Components child links: raw lines 19–27.
- Main Sessions/Advanced integration routes: raw lines 29–36.

## Related

- [[adyen-online-payments]]
- [[adyen]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/gcash/ios/2026-09-15|Adyen GCash iOS chooser snapshot]]
