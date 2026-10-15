---
title: "Order in store, ship to home | Adyen Docs"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/unified-commerce/retail-use-cases/endless-aisle/e-a-ship-home"
raw_files:
  - "adyen/docs/unified-commerce/retail-use-cases/endless-aisle/e-a-ship-home/2026-09-15.md"
tags: [adyen, unified-commerce, endless-aisle, point-of-sale, ecommerce, capture, refunds]
---

## Overview

This Adyen Endless Aisle guide describes an order placed with store staff and authorized on a payment terminal, then shipped to the shopper. Ordered items are manually captured at shipment, including corresponding partial captures for partial shipments. A mixed basket can also include items taken from the store, with their payment captured at the point of sale.

## Key takeaways

- The merchant needs both Adyen ecommerce and point-of-sale integrations and a consolidated order/inventory or orchestration system that can consume webhooks and update inventory for returns to either store or warehouse.
- Manual capture is required for the ordered items; the guide says to contact Adyen Support to enable multiple partial captures. A mixed basket can use one transaction with multiple partial captures under the same merchant account, or two separate transactions with the in-store items captured immediately or after a delay.
- Terminal authorization of the online order raises merchant-account and legal-entity choices. Merchant Account Sharing for different online and in-person merchant accounts is subject to compliance approval, and terminals require a local legal entity. The page lists separate terminals, multiple stores under one account, and Pay by Link as alternative arrangements.
- Delivery-address lookup uses a card-acquisition response's card alias or PAR, if present. This requires enabling shopper-identifying data in API responses and storing the alias and/or PAR in the shopper profile; staff verifies or enters the address, and a new CRM record is possible when no match exists.
- Preserve the authorization's PSP reference for later Checkout API capture and warehouse returns. Preserve the full terminal transaction ID and timestamp for in-store returns. Referenced refunds use Terminal API for store returns and Checkout API for warehouse returns; the page also calls for partial referenced refunds by customer service when discounts are offered remotely.

## Detail locators

- `Requirements` and `Considerations` > `Capture settings` / `Mixed baskets` — prerequisite systems, capture enablement, and one-versus-two-transaction choices.
- `Considerations` > `Legal entity and location` / `Delivery address` / `Sale attribution` — merchant account approval, local entity, card identifiers, CRM handling, and attribution decision.
- `Instructions` > `Delivery address` / `Authorization` — card-acquisition reference, PAR/alias when present, amount and manual-capture request, plus payment response identifiers.
- `Instructions` > `Captures and refunds` — Checkout capture and warehouse refund routes, Terminal API in-store referenced refund fields, and example payloads. A response shown in an example is a request/response step, not evidence of the final financial outcome.

## Related

- Company: [[adyen]]
- Concept: [[adyen-unified-commerce]]
- Related concepts: [[adyen-payment-capture]], [[adyen-refunds]], [[adyen-terminal-api]]

## Raw Sources

- [[raw/adyen/docs/unified-commerce/retail-use-cases/endless-aisle/e-a-ship-home/2026-09-15|2026-09-15 snapshot — Order in store, ship to home]]
