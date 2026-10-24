---
title: "Adyen express checkout overview"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/express-checkout"
raw_files:
  - "adyen/docs/payment-methods/express-checkout/2026-09-15.md"
tags: [adyen, express-checkout, wallets, online-payments]
---

## Overview

Adyen overview of express checkout buttons on product, cart or basket pages, allowing shoppers to choose a supported express payment method without visiting a separate checkout page. It is a 2026-09-15 website snapshot and navigation guide, not a complete integration procedure. It says express methods store shopper payment details and that order-fulfillment details come from the method after payment, but the specific child guides own setup, data availability and payment-result handling.

## Key takeaways

- The page says express methods can reduce checkout steps and describes one-click and abandonment benefits, while explicitly saying implementation needs additional integration steps. Treat these as intended benefits, not measured conversion or transaction guarantees (raw lines 19–37).
- Its Component-version matrix is qualified by method, platform and server-side flow: Apple Pay Web Advanced 5.0.0/Sessions 6.31.0; Apple Pay iOS Advanced 5.0.0/Sessions **not supported**; Google Pay Web Advanced 5.0.0/Sessions 6.31.0; PayPal Web Advanced and Sessions 5.59.0. The table states the Component version from which express checkout is supported, not merchant enablement or a universal SDK/API compatibility claim (raw lines 39–48).
- Buttons may appear on product-details or cart/basket pages. The page separately lists checkout-page instant Apple Pay/Google Pay placement, stored-payment-detail tokenization, and Web-only Click to Pay as alternatives; do not conflate those with this express-button matrix (raw lines 50–84).
- Get-started links point to Apple Pay, Google Pay and PayPal Web Component express guides. They are child navigation, not evidence from this page of wallet credential setup, shopper consent, redirect/return completion, authorization, capture or settlement (raw lines 86–98).

## Detail locators

- Purpose and claimed benefits/additional integration boundary: raw lines 19–37.
- Method/platform/flow/Component-version matrix: raw lines 39–48.
- Product/cart placement and faster-checkout alternatives: raw lines 50–84.
- Child Web Component express guide routes: raw lines 86–98.

## Related

- [[adyen]]
- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/express-checkout/2026-09-15|Adyen express checkout overview snapshot]]
