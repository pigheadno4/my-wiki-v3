---
title: "Adyen Unified Commerce endless aisle"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/unified-commerce/endless-aisle"
raw_files:
  - "adyen/docs/unified-commerce/endless-aisle/2026-09-15.md"
tags: [adyen, unified-commerce, endless-aisle, point-of-sale, pay-by-link]
---

## Overview

Adyen's dated endless-aisle page describes letting shoppers place **ecommerce orders while physically in a store or another location**—for example, ordering an out-of-stock item or online exclusive for delivery. The merchant supplies an app or web interface for online inventory and chooses a payment channel; the guide gives four possible device/payment arrangements without selecting one for a particular merchant. See [[adyen]], [[adyen-unified-commerce]] and [[adyen-terminal-api]].

## Key takeaways

- Three tabled options use **Terminal API** card-present payments: a tablet with a dedicated terminal; a tablet sending transactions to terminals shared with ordinary POS sales; or an existing POS system and terminals using local or cloud Terminal API communications. The POS-system option must combine POS and ecommerce flows and collect delivery details. The page labels these low, medium and high integration effort, respectively; these are the guide's comparative descriptions, not delivery estimates or an architecture decision.
- A fourth option is a tablet making a **Pay by Link API** call, with no payment terminal. The page says this option may require fraud rules and 3D Secure. It does not describe this option as a card-present terminal payment, and gives no checkout-result or capture semantics for it.
- A merchant must build an app or web interface that accesses its online inventory; Adyen recommends including a way to identify the **store or sales associate**. The page presents product-range, delivery-address and stock-allocation benefits as potential uses. It does not define inventory synchronization, seller/order identifiers, shipping execution, refunds, split settlement or a common order API across the four payment options.
- **For an endless-aisle transaction using a payment terminal**, the guide classifies the transaction as card-present POS and requires the terminal to be assigned to a merchant account under a legal entity registered in the country/region of the physical store. Its British-entity/Dutch-store example says the Dutch store and terminal cannot be assigned to the British ecommerce entity because that obscures the store's true location. This is a terminal-assignment constraint; the page does not establish who is seller or merchant of record for the ecommerce order, or state that the same rule applies unchanged to Pay by Link.
- The source was captured 2026-09-15 but its metadata says last modified 2021-11-04. Its illustrative device options and example do not prove current terminal, region, payment-method or merchant-account eligibility, a completed order, payment authorization, capture, refund or delivery.

## Detail locators

- Opening and benefits list: in-store ecommerce order purpose, out-of-stock/online-exclusive and delivery examples, potential use of order data for stock allocation.
- `## Technical setup`: four tabled device/payment-channel options and their stated integration effort; Terminal API versus Pay by Link distinction.
- `### App or web interface`: merchant-built online inventory interface and recommended store/associate identification.
- `## Compliance requirements`: card-present classification and in-country legal-entity assignment for **terminal transactions**, plus the illustrative UK/Netherlands example.

## Related

- [[adyen-unified-commerce]] — primary cross-channel merchant proposition.
- [[adyen-terminal-api]] — terminal payment-message route for three listed setups.

## Raw Sources

- [[raw/adyen/docs/unified-commerce/endless-aisle/2026-09-15|Adyen Endless aisle, captured 2026-09-15]]
