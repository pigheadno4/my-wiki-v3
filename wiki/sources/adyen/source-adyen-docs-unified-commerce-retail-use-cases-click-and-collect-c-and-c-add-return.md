---
title: "Adyen click and collect: change items at pickup"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/unified-commerce/retail-use-cases/click-and-collect/c-and-c-add-return"
raw_files:
  - "adyen/docs/unified-commerce/retail-use-cases/click-and-collect/c-and-c-add-return/2026-09-15.md"
tags: [adyen, unified-commerce, click-and-collect, retail, refunds, point-of-sale]
---

## Overview

Adyen's click-and-collect use case starts with a shopper paying online, then identifying themselves when collecting the order in a physical store. At pickup, unwanted purchased items can be refunded and additional store items can be bought with a separate Terminal API payment. It is a merchant-orchestrated online/POS journey, requiring both ecommerce and point-of-sale integrations plus a consolidated order/inventory or ERP system, or an orchestration layer that connects the systems and consumes webhooks. [[adyen-unified-commerce]] [[adyen]]

## Key takeaways

- The online purchase uses Checkout API authorization. The guide recommends immediate capture: a delayed capture can leave the authorization expired before pickup, with validity varying by card scheme. After an authorized result, the shopper chooses pickup identification by payment card or profile details. Ask explicit permission before saving identifying details for the first time.
- The guide calls for both identification methods. Card recognition depends on a card or NFC wallet used for the online purchase; it does not cover QR-code wallets, BNPL, or other alternative payment methods. A card alias identifies the PAN but cannot be used to make payments and is unavailable for NFC wallet transactions; PAR can identify the payment account linked to a card or NFC wallet. The merchant must enable identifying data in responses/webhooks for card recognition and use its own system to look up the shopper and purchased items. The online `AUTHORISATION` webhook supplies the payment PSP reference and amount for later order lookup and referenced refunds.
- If the shopper drops an item, issue a partial referenced refund against the ecommerce payment PSP reference, choosing either Terminal API `ReversalRequest` or Checkout API `/payments/{paymentPspReference}/refunds`. The Terminal route prints a receipt and can refund from another terminal or merchant account; the Checkout route does not print a terminal receipt.
- For the Terminal reversal of an ecommerce payment, put a **leading dot** before the PSP reference in `OriginalPOITransaction.POITransactionID.TransactionID`; the guide says omission yields `unreachable host`. A partial Terminal `ReversedAmount` is **not in minor units**; without it the whole purchase is refunded. The original ecommerce payment timestamp and refund currency are also specified in the Terminal route. By contrast, the Checkout refund sends an `amount` object: its `value` cannot exceed the captured amount and its `currency` must match the authorization; the guide's USD 12.50 example uses `value: 1250`. Keep the two amount conventions separate.

## Detail locators

- `Requirements`, `Shopper journey`, and `Considerations` — integration/system prerequisites, identity options, explicit permission, capture-expiry warning, and sale attribution decision.
- `Instructions > Online purchase` — Sessions and Advanced Checkout examples, authorized-result branch, `AUTHORISATION` webhook identifiers, PSP reference, and amount. Examples show test values, not production outcomes.
- `Instructions > In-store pickup`, steps 1–3 — Terminal API `CardAcquisitionRequest`, PAR/alias `AdditionalResponse`, `EnableServiceRequest` to stop card acquisition, and staff lookup through merchant systems.
- `Instructions > In-store pickup`, step 4 — Terminal reversal versus Checkout refund, route-specific required fields and USD 12.50 examples.
- `Instructions > In-store pickup`, step 5 — additional item purchase via Terminal API `PaymentRequest`.

## Related

- [[adyen-unified-commerce]] — provider cross-channel concept.
- [[adyen]] — provider overview.

## Raw Sources

- [[raw/adyen/docs/unified-commerce/retail-use-cases/click-and-collect/c-and-c-add-return/2026-09-15|Adyen buy online, pick up in store with item changes, fetched 2026-09-15]]
