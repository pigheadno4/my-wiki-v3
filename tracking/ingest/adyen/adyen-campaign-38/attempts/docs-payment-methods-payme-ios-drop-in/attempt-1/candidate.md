---
title: "PayMe iOS Drop-in integration"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/payme/ios-drop-in"
raw_files:
  - "adyen/docs/payment-methods/payme/ios-drop-in/2026-09-15.md"
tags: [adyen, payme, ios, drop-in, sandbox]
---

## Overview

This 2026-09-15 page describes adding PayMe to an existing Adyen iOS Drop-in integration. It says Drop-in renders PayMe and redirects the shopper to the PayMe app, and covers Sessions and Advanced server-side bases. The page says PayMe is supported from iOS Drop-in 4.0.0. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- Both flow tabs require a built iOS Drop-in integration of the corresponding Sessions or Advanced type and PayMe setup in Customer Area. The separate API-reference wording says `/sessions` is the default with Drop-in v5.0.0 or later; this does not revise the page's broader PayMe support statement of Drop-in v4.0.0 onward. See raw lines 19–49.
- The `/sessions` and `/payments` tables list optional `channel` and `lineItems` fields. The `lineItems.sku` description qualifies it as available with Checkout API v70 and later; that is a field-level condition, not a stated minimum API version for all PayMe iOS Drop-in integrations. See raw lines 51–71.
- The example `/payments` request uses `paymentMethod.type: payme`, `HKD`, `HK`, `channel: iOS`, a return URL and example line items. It is inside a `swift` code fence but contains JavaScript Node API-library code, so it is not a copy-paste Swift implementation. The page sends payment outcome presentation to the main iOS Drop-in guide and states no PayMe-specific Drop-in configuration. See raw lines 73–114.
- The PayMe sandbox does not require the PayMe app. Amount endings `30`/`81`, `77`/`90`, and `40`/`44` simulate Authorised, OfferCancelled (described as expiry after PayMe's default ten minutes), and Error, respectively. These are sandbox fixtures, not evidence of a completed live payment or that a shopper return alone determines outcome. See raw lines 116–126.

## Detail locators

- iOS support, flow-specific prerequisites and `/sessions` version wording: raw lines 19–49.
- Optional request fields and mislabeled example: raw lines 51–108.
- Outcome-route link, no-extra-configuration statement and sandbox simulations: raw lines 110–126.

## Related

- [[adyen-online-payments]] — main online-payments concept.
- [[adyen]] — provider entry.

## Raw Sources

- [[raw/adyen/docs/payment-methods/payme/ios-drop-in/2026-09-15|PayMe iOS Drop-in integration (2026-09-15)]]
