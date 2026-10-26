---
title: "Adyen Vipps Android integration chooser"
type: source
date_ingested: 2026-10-26
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/vipps/android"
raw_files:
  - "adyen/docs/payment-methods/vipps/android/2026-09-15.md"
tags: [adyen, vipps, android, drop-in, components, redirect]
---

## Overview

This 2026-09-15 Adyen Android page is a chooser for adding Vipps to an Android app. It routes to a Drop-in child guide or an `InstantPaymentComponent` child guide described as handling the redirect to Vipps, and it lists main Android Sessions and Advanced guides for both UI options. It gives navigation, not method-specific request fields, version, merchant eligibility, redirect execution, payment outcome or live setup rules; consult the child and main guides for those details. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- Choose Android Drop-in for Adyen's all-in-one UI or Android Components for the `InstantPaymentComponent` redirect route. These labels do not establish interchangeable integration behavior.
- The page says to create the main integration first and links Android Drop-in Sessions, Android Components Sessions, Android Drop-in Advanced and Android Components Advanced guides. The chooser does not itself prove current enablement or a completed payment.

## Detail locators

- Drop-in and Components child choices: pinned raw lines 19–27.
- Main-integration prerequisite and four flow/UI guide links: pinned raw lines 29–36.

## Related

- [[adyen-online-payments]] — provider concept and source route
- [[source-adyen-docs-payment-methods-vipps-android-drop-in]] — Android Drop-in child guide; separate authority for its setup and behavior
- [[source-adyen-docs-payment-methods-vipps-android-component]] — Android Components child guide; separate authority for its setup and behavior

## Raw Sources

- [[raw/adyen/docs/payment-methods/vipps/android/2026-09-15|Vipps Android chooser, 2026-09-15]]
