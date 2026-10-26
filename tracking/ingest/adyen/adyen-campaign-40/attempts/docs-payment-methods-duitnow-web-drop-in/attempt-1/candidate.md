---
title: "Adyen DuitNow Web Drop-in guide"
type: source
date_ingested: 2026-10-26
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/duitnow/web-drop-in"
raw_files:
  - "adyen/docs/payment-methods/duitnow/web-drop-in/2026-09-15.md"
tags: [adyen, duitnow, web, drop-in, sessions, advanced]
---

## Overview

This 2026-09-15 captured Adyen page explains how to add DuitNow to an existing Web Drop-in integration, with separate Sessions and Advanced server-side prerequisite routes. It is a short method add-on, not a full payment flow or evidence of current enablement or a completed payment. See [[adyen]], [[adyen-online-payments]] and [[source-adyen-docs-payment-methods-duitnow]] for the QR-only method overview.

## Key takeaways

- The Sessions tab requires an existing Sessions Web Drop-in integration; the Advanced tab requires an existing Advanced Web Drop-in integration. Both tell the merchant to contact Adyen Support to add DuitNow in Customer Area before beginning. The page gives no method-specific server request fields and no DuitNow-specific Drop-in configuration.
- For Web Drop-in v6, the page shows an import of `AdyenCheckout` and `DuitNow` from `@adyen/adyen-web`. This import is version-scoped; it is not an iOS or Android instruction. The API reference says no additional DuitNow fields are needed. It calls `/sessions` the default with Drop-in v5.0.0 or later and points to `/payments` for an additional use case; it does not give a new universal Checkout API minimum or a complete Advanced handoff here.
- The test/live section says to use real payment details and small amounts, check test-payment status in Customer Area, and contact Support to add DuitNow in the live Customer Area. It does not state a QR action structure, expiry, shopper completion sequence, webhook result mapping, or successful test/live outcome. Follow the linked base integration and payment-method authority for those details.

## Detail locators

- Purpose, Sessions/Advanced prerequisites and Support setup: pinned raw lines 15–37.
- Web Drop-in v6 import: pinned raw lines 39–45.
- No-extra-fields API reference, `/sessions` v5.0.0 default and additional-use-case `/payments` route: pinned raw lines 47–52.
- No DuitNow-specific Drop-in configuration: pinned raw lines 54–56; test and live setup: lines 58–64.

## Related

- [[adyen-online-payments]] — main concept and Web integration routes
- [[source-adyen-docs-payment-methods-duitnow]] — DuitNow method overview

## Raw Sources

- [[raw/adyen/docs/payment-methods/duitnow/web-drop-in/2026-09-15|DuitNow Web Drop-in guide, 2026-09-15]]
