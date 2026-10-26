---
title: "Adyen Swish Web Component"
type: source
date_ingested: 2026-10-26
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/swish/web-component"
raw_files:
  - "adyen/docs/payment-methods/swish/web-component/2026-09-15.md"
tags: [adyen, swish, web, components, online-payments]
---

## Overview

Adyen's 2026-09-15 Swish Web Component page gives Swish-specific additions to an existing Web Components integration, separately for Sessions and Advanced server-side flows. General integration steps remain in the linked main guides. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- For Sessions, the page requires an existing Web Components Sessions integration, Checkout API v68 or later, and Swish added in Customer Area. It says no additional `/sessions` parameters or Swish-specific Component configuration are needed. It imports `Swish` from `@adyen/adyen-web` and initializes a `Swish` Component with the checkout instance.
- For Advanced, the page requires an existing Web Components Advanced integration, Swish added in Customer Area, and handling the additional `action.type: qr` action. It imports and initializes the same `Swish` Component and says no additional `/payments` parameters are needed. The action row links to a main-guide URL ending in `#handle-the-redirect`, but the row itself names a QR action; the anchor does not turn the stated action into a redirect.
- For test-environment Swish payments, the page says authorization occurs within 15 seconds and directs the merchant to Customer Area's payment list for status. It says refusal scenarios can be simulated by putting a Merchant Swish Simulator error code such as `FF08` in `shopperStatement`. That is test guidance, not a live authorization-time guarantee or evidence of any specific payment execution.
- Live acceptance requires a separate Swish request in live Customer Area. The page does not supply a Swish country/currency eligibility table, settlement outcome, or live payment proof.

## Detail locators

- Sessions requirements, no-extra-`/sessions` statement, import and initialization: raw lines 25-75.
- Sessions test authorization, simulator and live request: raw lines 77-83.
- Advanced requirements and `qr` action with redirect-anchor mismatch: raw lines 85-93.
- Advanced import, initialization and no-extra-`/payments` statement: raw lines 95-127.
- Repeated Advanced test/simulator/live guidance: raw lines 129-135.

## Raw Sources

- [[raw/adyen/docs/payment-methods/swish/web-component/2026-09-15|Swish Web Component (2026-09-15 snapshot)]]
