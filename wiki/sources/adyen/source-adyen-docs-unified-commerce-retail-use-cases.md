---
title: "Retail use cases | Adyen Docs"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/unified-commerce/retail-use-cases"
raw_files:
  - "adyen/docs/unified-commerce/retail-use-cases/2026-09-15.md"
tags: [adyen, unified-commerce, retail, click-and-collect, endless-aisle, mixed-baskets]
---

## Overview

This Adyen Docs retail-use-case hub introduces shopper journeys that connect a merchant's ecommerce and point-of-sale operations. It defines **click and collect** as ordering or buying online and picking up at a physical store, and **endless aisle** as placing an ecommerce order in a store or another physical location. The page routes to detailed click-and-collect, endless-aisle and mixed-basket/account-structure guides and calls the collection a work in progress. It is navigation and framing, not an API flow or a deployed merchant outcome. See [[adyen]] and [[adyen-unified-commerce]].

## Key takeaways

- The page says child use cases start with a shopper journey, show an involved API flow and give high-level instructions. This hub itself gives no request schema, transaction sequence, payment response, stock/fulfillment state or financial object. The shopper places or collects an order; the merchant owns its ecommerce/POS operations in the description. No seller, payee or merchant-of-record assignment is provided here.
- Its click-and-collect links label **reserve online, try in a store**, **buy online, pick up in a store**, and **buy online, pick up by an assistant**. These labels are navigation, not proof that a reservation authorizes/captures funds, that an assistant completes payment, or that pickup/returns are supported for a particular account.
- Its endless-aisle links label **order in a store, ship to home** and **order in a store, pick up in a store**. The page does not say how stock, fulfillment, cancellation, capture or refunds are handled. The mixed-baskets link points to account-structure options; this overview neither defines a basket split nor assigns legal entities, merchant accounts or settlement owners.
- A separate industry feature-pack link is a tip, not reviewed evidence of required features in this entry. The overview does not describe a returns flow or current regional/merchant eligibility. Follow the child guides for those operational questions and verify current behavior before implementation.

## Detail locators

- `Retail use cases`, pinned raw lines 15–17: omnichannel retail hub identity.
- `Features per industry`, lines 19–21: link to a separate retail feature pack, navigation only.
- Introduction, lines 23–27: intended child-guide level, click-and-collect and endless-aisle definitions, work-in-progress limit.
- `Next steps`, lines 29–45: click-and-collect scenario labels, endless-aisle scenario labels and mixed-baskets account-structure route.

## Related

- [[adyen-unified-commerce]] — primary provider concept for cross-channel merchant journeys.
- [[source-adyen-docs-unified-commerce-shopper-experiences]] — separate broader journey overview; its examples are not implementation evidence for this hub.

## Raw Sources

- [[raw/adyen/docs/unified-commerce/retail-use-cases/2026-09-15|Adyen retail use-cases hub, fetched 2026-09-15]]
