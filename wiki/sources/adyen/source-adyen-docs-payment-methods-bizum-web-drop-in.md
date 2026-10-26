---
title: "Adyen Bizum Web Drop-in integration guide"
type: source
date_ingested: 2026-10-26
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/bizum/web-drop-in"
raw_files:
  - "adyen/docs/payment-methods/bizum/web-drop-in/2026-09-15.md"
tags: [adyen, bizum, web, drop-in, redirect]
---

## Overview

This 2026-09-15 Adyen guide describes Bizum-specific additions to an existing Web Drop-in integration, separately for Sessions and Advanced flows. It covers activation and Customer Area setup, flow-specific payment requests, redirect handling, optional imports, and sandbox testing. It is a method add-on, so the linked main integration guides own the complete payment flow. This snapshot and its examples do not establish current merchant eligibility or a live payment outcome. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- Sessions requires an existing Sessions Web Drop-in integration, Checkout API v68 or later, redirect handling for `action.type: redirect`, Bizum activation to obtain a MID and Terminal ID, and adding Bizum in Customer Area. The Bizum-specific `/sessions` addition is a unique `reference` of 4–125 upper/lowercase alphanumeric characters. The page's printed regex ends with an extra `)` and should not be copied as a validated expression. The Sessions example's `YOUR_PAYMENT_REFERENCE` and Advanced example's `YOUR_ORDER_NUMBER` contain underscores, contrary to the alphanumeric rule; neither placeholder is a validated reference value. Its TEST `/v71/sessions` example uses `EUR`, `ES`, and an app-scheme `returnUrl`; these are example values, not a general country/currency or Web return-URL rule.
- Advanced requires an existing Advanced Web Drop-in integration, redirect handling, the same activation and Customer Area setup, and the same `reference` addition to `/payments`. This section does not state a Checkout API minimum. The TEST `/v72/payments` example sends `paymentMethod.type: bizum`; the response section shows `resultCode: RedirectShopper` and `action.type: redirect` with POST redirect data. This is an intermediate redirect response, not proof of authorization, capture or settlement.
- In either flow, an individual `Redirect` import from `@adyen/adyen-web` is optional for tree shaking. It is not stated as a Web SDK minimum.
- For sandbox testing, the page says to use `telephoneNumber` 700 000 000 and gives amount-based outcomes: below 10 authorized, above 15 refused. It does not specify the interval from 10 through 15. Inspect TEST payment status in Customer Area; these fixtures do not establish live behavior.

## Detail locators

- Scope and Sessions prerequisites: pinned raw lines 15–37; `/sessions` reference table and TEST example: lines 39–69. The table's regex has an unmatched closing parenthesis at line 47.
- Optional Sessions import and TEST outcomes: pinned raw lines 334–361.
- Advanced prerequisites and optional import: pinned raw lines 363–386; `/payments` reference table, example and redirect response: lines 388–731. The Advanced prerequisite URL at line 371 contains an unresolved encoded template token; use the explicit Advanced Web Drop-in wording, not the malformed hyperlink, to identify scope.
- Advanced TEST outcomes and Customer Area route: pinned raw lines 733–748.

## Related

- [[adyen-online-payments]] — main concept and integration architecture
- [[source-adyen-docs-payment-methods-bizum]] — method overview; separate authority for method-level eligibility and lifecycle

## Raw Sources

- [[raw/adyen/docs/payment-methods/bizum/web-drop-in/2026-09-15|Bizum Web Drop-in guide, 2026-09-15]]
