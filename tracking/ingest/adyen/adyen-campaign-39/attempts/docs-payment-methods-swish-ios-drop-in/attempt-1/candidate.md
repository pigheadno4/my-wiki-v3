---
title: "Adyen Swish iOS Drop-in integration guide"
type: source
date_ingested: 2026-10-26
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/swish/ios-drop-in"
raw_files:
  - "adyen/docs/payment-methods/swish/ios-drop-in/2026-09-15.md"
tags: [adyen, swish, ios, drop-in, qr]
---

## Overview

This 2026-09-15 Adyen page gives Swish-specific additions to an existing iOS Drop-in integration for Sessions and Advanced server-side flows. It covers Customer Area setup, Advanced `qr` action handling, TEST simulator guidance and a separate LIVE request. It relies on the main iOS Drop-in guides for the full payment flow; the snapshot does not establish current merchant enablement or a completed live payment, capture or settlement. See [[adyen]], [[adyen-online-payments]] and [[source-adyen-docs-payment-methods-swish]].

## Key takeaways

- Sessions requires an existing iOS Drop-in Sessions integration using Checkout API v68 or later and Swish added in Customer Area. It says no Swish-specific `/sessions` parameters or Drop-in configuration are needed. The section does not separately state an action-type requirement.
- Advanced requires an existing iOS Drop-in Advanced integration, handling the additional `action.type: qr` action, and Swish added in Customer Area. It says no Swish-specific `/payments` parameters or Drop-in configuration are needed. Its action-handling link points to a `handle-the-redirect` anchor despite the explicit `qr` action type; the link label should not be read as a redirect response. The Advanced section does not state a Checkout API minimum.
- In TEST, the page says a Swish payment is authorised within 15 seconds and refusal scenarios can be simulated by placing a Merchant Swish Simulator error code, for example `FF08`, in `shopperStatement`. It directs merchants to inspect TEST payment status in Customer Area. This 15-second statement concerns the documented TEST flow, not a live or refused-payment guarantee. For LIVE acceptance, submit a separate Swish request in the live Customer Area. Neither a simulated result nor request submission proves capture or settlement.

## Detail locators

- Scope and Sessions prerequisites, no-extra-parameter and no-extra-configuration statements: pinned raw lines 15–46.
- Sessions TEST simulator, status and LIVE request: pinned raw lines 48–56.
- Advanced prerequisites and `qr` action versus redirect-anchor link: pinned raw lines 58–68. No-extra-configuration and no-extra-parameter statements: lines 70–80. Advanced TEST/LIVE guidance: lines 82–90.

## Related

- [[adyen-online-payments]] — main concept and payment-state context
- [[source-adyen-docs-payment-methods-swish]] — method overview and separate region/feature scope

## Raw Sources

- [[raw/adyen/docs/payment-methods/swish/ios-drop-in/2026-09-15|Swish iOS Drop-in guide, 2026-09-15]]
