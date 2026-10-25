---
title: "PayMe Android Drop-in integration"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/payme/android-drop-in"
raw_files:
  - "adyen/docs/payment-methods/payme/android-drop-in/2026-09-15.md"
tags: [adyen, payme, android, drop-in, redirect, online-payments]
---

## Overview

This 2026-09-15-captured guide describes adding PayMe to an existing Android Drop-in payment form. Drop-in presents PayMe and hands the shopper to the PayMe app to complete the payment; the server-side request, returned redirect action, and later payment outcome are distinct stages. The page documents an integration pattern and sandbox simulations, not an observed live authorization or settlement. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Prerequisites and scope:** the guide states support begins at Android Drop-in 4.0.0 and requires an existing **Advanced flow** Drop-in integration plus PayMe added in Customer Area. Its opening and outcome links point to the Sessions-flow guide even though the Requirements row names Advanced flow; use the explicitly stated requirement rather than treating those links as proof of Sessions support here. (raw lines 19–28, 183–187)
- **Availability and request boundaries:** the page says Drop-in uses `countryCode` and `amount.currency` from the server's `/paymentMethods` request to show available methods; it specifies HK and HKD for this PayMe example. The separate additional-use-case table lists `channel` and `lineItems` fields with blank Required cells, so that table does not itself make them mandatory. The `/payments` snippets illustrate TEST, HK/HKD and a PayMe payment method; they do not establish a general Checkout API minimum or live merchant eligibility. (raw lines 30–78, 80–85, 98–164)
- **Redirect handoff:** Drop-in returns `paymentComponentData.paymentMethod`; the client passes it to the server, which makes `/payments` and passes the returned `action` back to the client so Drop-in can redirect to the PayMe app. The page says to get the return URL from `RedirectComponent.getReturnUrl(context)` and routes outcome handling to the Android Drop-in guide. Its request prose spells `returnURL`, while examples spell `returnUrl`; this page does not reconcile the casing. A redirect action or shopper return does not by itself prove final authorization. (raw lines 87–96, 115–116, 152–153, 166–187)
- **Example inconsistencies:** an early fenced block is labeled `kotlin` but contains JavaScript API-library syntax. Its `channel` value is `Android`, whereas the later curl example uses `Web` and the NodeJS example uses `Web/iOS/Android`; these are conflicting illustrations, not a resolved field prescription. (raw lines 43–78, 98–164)
- **Sandbox outcomes:** the PayMe sandbox needs no PayMe app and maps amount endings 30/81 to simulated `Authorised`, 77/90 to `OfferCancelled` after the stated default ten-minute expiry, and 40/44 to request-creation `Error`. These are sandbox mappings, not evidence that a production payment succeeded. (raw lines 189–199)

## Detail locators

- Drop-in app redirect, 4.0.0 support floor and Advanced-flow setup: raw lines 19–28.
- Additional-use-case fields, example requests and HK/HKD availability filter: raw lines 30–85.
- Payment-method data, return URL, `/payments`, redirect action and outcome route: raw lines 87–187.
- Sandbox outcomes and ten-minute expiry: raw lines 189–199.

## Related

- [[adyen]]
- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/payme/android-drop-in/2026-09-15|Adyen PayMe Android Drop-in guide, 2026-09-15 snapshot]]
