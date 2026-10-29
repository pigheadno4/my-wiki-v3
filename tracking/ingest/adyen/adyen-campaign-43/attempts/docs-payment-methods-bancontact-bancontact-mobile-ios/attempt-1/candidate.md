---
title: "Adyen Bancontact mobile for iOS chooser"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/bancontact/bancontact-mobile/ios"
raw_files:
  - "adyen/docs/payment-methods/bancontact/bancontact-mobile/ios/2026-09-15.md"
tags: [adyen, bancontact, mobile, ios, drop-in, components]
---

## Overview

This Bancontact mobile iOS page, captured 2026-09-15 with a 2019-09-30 last-modified timestamp, is an integration chooser. It routes an iOS app to Bancontact mobile Drop-in or Components child guides and links to base Sessions integrations. It does not itself specify app-switch/QR handling, request fields, payment outcome, test availability or live eligibility. See [[adyen]], [[adyen-online-payments]] and [[adyen-ios-sdk]].

## Key takeaways

- Choose the iOS Bancontact mobile Drop-in child for Adyen's all-in-one UI, or the iOS Components child for a prebuilt Component. The child guides own the actual method setup and flows; this page's labels alone do not establish a supported payment result.
- The final base-guide sentence calls one link 'Android Drop-in', but its URL has `platform=iOS&integration=Drop-in`; its other URL has `platform=iOS&integration=Components`. This is a label/URL mismatch. Use the iOS URL scope and the relevant child guide rather than treating that label as Android guidance.
- This is specifically the Bancontact mobile iOS chooser, not the Bancontact card method or the Android mobile route. The page gives no basis to infer cross-platform parity.

## Detail locators

- Page identity, capture and last-modified metadata: pinned raw lines 1–17.
- Drop-in and Components child-guide links: pinned raw lines 19–27. Mislabeled 'Android Drop-in' link pointing to an iOS Sessions base URL, plus iOS Components URL: line 29.

## Related

- [[adyen-online-payments]] — primary provider method route
- [[adyen-ios-sdk]] — iOS platform context
- [[source-adyen-docs-payment-methods-bancontact-bancontact-mobile-ios-drop-in]] — iOS Drop-in child guide
- [[source-adyen-docs-payment-methods-bancontact-bancontact-mobile-ios-component]] — iOS Components child guide
- [[source-adyen-docs-payment-methods-bancontact]] — parent Bancontact card/mobile distinction

## Raw Sources

- [[raw/adyen/docs/payment-methods/bancontact/bancontact-mobile/ios/2026-09-15|Bancontact mobile iOS chooser, captured 2026-09-15]]
