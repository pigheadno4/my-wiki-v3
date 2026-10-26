---
title: "Adyen Swish Web Drop-in"
type: source
date_ingested: 2026-10-26
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/swish/web-drop-in"
raw_files:
  - "adyen/docs/payment-methods/swish/web-drop-in/2026-09-15.md"
tags: [adyen, swish, web, drop-in, online-payments]
---

## Overview

Adyen's 2026-09-15 Swish Web Drop-in page describes Swish-specific additions to an existing Web Drop-in integration, with separate Sessions and Advanced server-side flows. It points to the main integration guides for general steps. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- For Sessions, the page requires existing Web Drop-in Sessions, Checkout API v68 or later, and Swish added in Customer Area. It says no additional `/sessions` parameters are needed. Importing `Swish` individually alongside `AdyenCheckout` and `Dropin` is optional and presented as a tree-shaking performance optimization, not a prerequisite.
- For Advanced, the page requires existing Web Drop-in Advanced, Swish added in Customer Area, and handling the additional `action.type: qr` action. It says no additional `/payments` parameters are needed and likewise describes individual `Swish` import as optional.
- For test-environment Swish payments, the page says authorization occurs within 15 seconds and directs the merchant to the test Customer Area payment list for status. It says refusal scenarios can be simulated with a Merchant Swish Simulator code such as `FF08` in `shopperStatement`. This test statement does not establish live authorization timing or any completed payment in this snapshot.
- Live acceptance requires a separate Swish request in live Customer Area. The Advanced requirement row's main-guide URL contains an encoded template expression instead of a resolved platform value; its action-handling link points to a `#handle-the-redirect` anchor, although the stated action is `qr`. Neither link discrepancy changes the page's QR action text. The page has no country/currency eligibility table or settlement proof.

## Detail locators

- Sessions requirements, no-extra-`/sessions` statement and optional import: raw lines 25-53.
- Sessions test/simulator guidance and live request: raw lines 55-63.
- Advanced requirements, unresolved platform URL and QR action with redirect anchor: raw lines 65-75.
- Advanced optional import and no-extra-`/payments` statement: raw lines 77-93.
- Repeated Advanced test/simulator/live guidance: raw lines 95-103.

## Raw Sources

- [[raw/adyen/docs/payment-methods/swish/web-drop-in/2026-09-15|Swish Web Drop-in (2026-09-15 snapshot)]]
