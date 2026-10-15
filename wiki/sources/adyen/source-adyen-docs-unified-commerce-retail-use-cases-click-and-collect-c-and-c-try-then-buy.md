---
title: "Adyen click and collect: reserve online, try in store"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/unified-commerce/retail-use-cases/click-and-collect/c-and-c-try-then-buy"
raw_files:
  - "adyen/docs/unified-commerce/retail-use-cases/click-and-collect/c-and-c-try-then-buy/2026-09-15.md"
tags: [adyen, unified-commerce, click-and-collect, retail, authorization, capture]
---

## Overview

Adyen's 2026-09-15 click-and-collect guide describes a **reserve online, try in store, then buy** scenario. The shopper reserves items and selects a pickup store; the ecommerce integration requests Checkout API authorization with **manual capture**, leaving funds uncaptured at reservation. At the store, staff find the reservation, the shopper tries the items, and the merchant captures the amount for the purchase decision. This separates inventory reservation and in-store fulfillment from payment authorization and capture. See [[adyen]], [[adyen-unified-commerce]], [[adyen-payment-capture]] and [[adyen-card-recognition]].

## Key takeaways

- The scenario requires both Adyen ecommerce and POS integrations and a consolidated order/inventory or ERP system, or webhook-consuming orchestration across subsystems. The POS must update online inventory after pickup, sale or return. The guide does not define a universal reservation object or prove that reserving stock completes a payment.
- **Manual capture is required.** The online Checkout API payment request authorizes the reserved amount at reservation; it does not capture it. Pre-authorization with manual capture is recommended when an upward amount adjustment may be needed; regular authorization with manual capture suffices when the amount will stay the same or decrease. The guide warns that not all card schemes support pre-authorization and points to scheme/payment-method availability.
- For all reserved items purchased, the ecommerce side makes a Checkout API full capture. For fewer items, it makes a partial capture and the guide says the unused amount is released. For additional items, one transaction adjusts the original online authorization upward **only if it was pre-authorized**, then captures the total; the alternative captures the original reservation and makes a separate Terminal API in-person payment for extra items. Account structure affects reconciliation and sale attribution. These examples are API requests, not evidence that a particular capture or adjustment succeeded.
- At reservation, the shopper can choose card recognition or profile details for pickup. Card recognition works only where a card or NFC wallet was used for the online reservation; the guide explicitly excludes QR-code wallets, BNPL and other alternative methods, so it directs merchants to implement both identification methods. For card recognition, the merchant enables identifying data in API responses and webhooks; after the `AUTHORISATION` webhook it saves card alias when available, PAR, PSP reference and amount. An alias cannot make payments, and an NFC-wallet transaction may lack one. At pickup a Terminal API card-acquisition response supplies alias/PAR for the merchant record lookup; the merchant then stops the acquisition flow. This lookup is separate from a payment.
- The guide says to ask **explicit permission before saving shopper details** and to store identifiers/profile information securely. It does not say alias/PAR proves a person's civil identity or bypasses permission. The merchant must decide cross-channel sale attribution. The snapshot does not establish seller, merchant of record, settlement, authorization lifetime, current scheme eligibility or a completed purchase.

## Detail locators

- `## Requirements`, `## Shopper journey`: two integrations, order/inventory synchronization, reservation, pickup and purchase decisions.
- `## Considerations` → `### Capture settings`: manual capture, pre-authorization versus regular authorization, card-scheme caveat.
- `## Considerations` → `### Shopper identification`, `### Card acquisition`, `### Mixed basket and account structure`: permission, supported identifier paths, extra-item transaction choices.
- `## API flow`, `## Instructions` → `### Online reservation`: Checkout authorization samples, `AUTHORISATION` webhook identifiers and reference retention.
- `## Instructions` → `### In-store pickup and try-on`, `### Capture based on purchase decision`: card-acquisition and profile lookup, full/partial capture, adjustment and separate Terminal API payment examples.

## Related

- [[adyen-unified-commerce]] — main cross-channel retail concept.
- [[adyen-payment-capture]] — manual/partial capture and asynchronous outcome boundary.
- [[adyen-card-recognition]] — card acquisition and identifier limits.
- [[adyen-authorization-adjustment]] — pre-authorization adjustment route.

## Raw Sources

- [[raw/adyen/docs/unified-commerce/retail-use-cases/click-and-collect/c-and-c-try-then-buy/2026-09-15|Adyen Reserve online, try in store, captured 2026-09-15]]
