---
title: "Adyen endless aisle: order in store, pick up in store"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/unified-commerce/retail-use-cases/endless-aisle/e-a-store-pickup"
raw_files:
  - "adyen/docs/unified-commerce/retail-use-cases/endless-aisle/e-a-store-pickup/2026-09-15.md"
tags: [adyen, unified-commerce, endless-aisle, retail, point-of-sale, capture]
---

## Overview

Adyen's 2026-09-15 snapshot is an implementation guide for one **endless-aisle retail scenario**: a shopper orders online inventory while in a store, chooses a pickup store, and authorizes the ordered items on a payment terminal. The merchant captures payment for those ordered items when they are picked up, possibly through multiple partial captures as items become available. This is a merchant order and fulfillment journey with separate payment authorization, capture and refund operations; an order-ready notification or handoff of goods is not a payment outcome. See [[adyen]], [[adyen-unified-commerce]], [[adyen-payment-capture]] and [[adyen-card-recognition]].

## Key takeaways

- The scenario requires both Adyen ecommerce and POS integrations and consolidated order/inventory or ERP systems, or an orchestration layer across subsystems that consumes webhooks. Store and warehouse returns must update inventory. The guide also requires **manual capture** and says to contact Adyen Support to enable **multiple partial captures**. Ordered items are authorized first and captured upon pickup; a reduced or staggered pickup calls for partial captures.
- At order placement, Terminal API card acquisition obtains card alias and/or PAR to look up or create the merchant's shopper/order record and collect contact details and pickup location. The later pickup uses card acquisition again to find the order, then stops that acquisition with EnableService; card acquisition is an identifier step, not a new payment. This use requires enabling shopper identifying data in API responses and storing alias and/or PAR in the shopper profile. The guide gives no independent consent or identity-proof rule.
- Mixed baskets may put in-store and ordered items in **one transaction with multiple partial captures**, but this requires the same merchant account; in-store items are captured when acquired, and ordered items later. Alternatively, **two separate transactions** authorize online items for later capture and pay for in-store items separately with immediate or delayed automatic capture. Adding in-store items at pickup to a single transaction requires initial pre-authorization and an upward authorization adjustment. These are choices, not a claim that order creation itself captures funds.
- The merchant must decide sale attribution and account/capture structure. Merchant Account Sharing for separate accounts on the same terminal is subject to compliance approval, and terminals require a local legal entity; the guide offers separate terminals, multiple stores under one account, or Pay by Link as alternatives. It does not decide seller, merchant of record, inventory ownership or settlement for a specific retailer.
- Authorization can expire while the shopper waits to collect goods. The guide offers pre-authorization and amount updates (synchronous data blob or asynchronous webhook), Extend on capture for American Express/Mastercard/Visa, or optional tokenization followed by a new Checkout API payment if capture fails because the transaction expired. Adjustments incur costs. A capture request needs its webhook outcome checked; the guide's failed-capture token route does not prove recovery succeeded.
- Store returns use a Terminal API referenced reversal with the original terminal transaction reference and timestamp; warehouse returns use a Checkout API referenced refund with the original PSP reference. Order systems must retain the proper references. Phone/chat discounts may also need partial referenced refunds. These are later payment modifications, separate from product return and inventory updates.

## Detail locators

- `## Requirements`, `## Shopper journey`: integrations, orchestration/inventory and shopper steps.
- `## Considerations` → `### Capture settings`, `### Authorization expiry and late capture`, `### Mixed baskets`: capture configuration, expiry options and account/capture models.
- `## Considerations` → `### Legal entity and location`, `### Card recognition`, `### Sale attribution`, `### Refunds and discounts`: compliance qualification, identifier setup and later returns.
- `## API flow` and `## Instructions` → `#### Contact details`, `#### (Pre-)authorization`, `#### Authorization extension (optional)`, `#### In-store pickup`, `#### Later returns, after pickup`: sequence diagrams, API fields/examples and webhook outcome guidance. In the dated raw, synchronous `/amountUpdates` cURL examples contain an extra `}` after the PSP reference; verify against the linked API reference before copying.

## Related

- [[adyen-unified-commerce]] — primary concept route for this scenario.
- [[adyen-payment-capture]] — manual and multiple partial capture semantics and outcome boundary.
- [[adyen-card-recognition]] — card acquisition and identifier boundary.
- [[adyen-authorization-adjustment]] — pre-authorization and adjustment route.

## Raw Sources

- [[raw/adyen/docs/unified-commerce/retail-use-cases/endless-aisle/e-a-store-pickup/2026-09-15|Adyen Order in store, pick up in store, captured 2026-09-15]]
