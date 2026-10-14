---
title: "Shopper experiences | Adyen Docs"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/unified-commerce/shopper-experiences"
raw_files:
  - "adyen/docs/unified-commerce/shopper-experiences/2026-09-15.md"
tags: [adyen, unified-commerce, shopper-experiences, omnichannel, purchase-journeys]
---

## Overview

This Adyen Docs **Shopper Experiences** overview frames an omnichannel purchase journey as three separable parts: the order, the product or service, and the payment. It gives merchant-facing examples in which a shopper can order, receive or collect goods, and pay through different online or physical touchpoints. It is a use-case map, not an API schema, implementation checklist or proof that any merchant has fulfilled an order or completed a payment. See [[adyen]] and [[adyen-unified-commerce]].

## Key takeaways

- **Endless aisle:** a shopper can place an ecommerce order and pay in a store for an item out of stock or not sold there, with home delivery. A kiosk/tablet/payment-terminal setup is one possible configuration, not a required UI or evidence of inventory synchronization, stock reservation, fulfillment or capture.
- **Pay by Link:** the page describes sending a link to complete payment alongside an existing online-payments integration, including orders taken by email, call center or social media. It does not specify link creation, authentication, expiration, payment result handling or merchant-of-record/payee arrangements. The linked Pay by Link guide is a next-step route.
- **Referenced refunds:** Adyen says a unique payment reference helps track payments and refunds and supports in-store returns for items bought at POS or online. This overview does not define the original-reference field, refund request, eligibility, capture/cancellation interaction or asynchronous outcome. Consult the separate referenced-refunds guide before implementing.
- **Mobile and in-store examples:** click and collect has online purchase followed by in-store pickup; reserve and collect places a reservation online and pays at collection; table self-order/close bill and self-scan use the shopper's own mobile device for ordering or online payment. Pay anywhere in store names mobile Verifone/Android terminals, Pay by Link or kiosks as alternatives to a fixed till. These are example paths, not equivalent transaction flows, guaranteed availability or actual payment/fulfillment results.
- The shopper is the buyer in these examples; the page addresses merchants planning journeys. It does not assign seller, payee or merchant-of-record roles, define inventory ownership or settle funds across parties. The 2026-09-15 capture carries a 2021 last-modified date; current product and regional support need checking in the linked guides.

## Detail locators

- `Shopper experiences`, pinned raw lines 15–19: order, product/service and payment as distinct journey parts.
- `Endless aisle`, lines 21–22: in-store ecommerce order/payment, out-of-stock example, home delivery and optional kiosk setup.
- `Pay by Link`, lines 24–25: link-payment proposition and email/call-center/social order channels.
- `Referenced refunds`, lines 27–28: unique reference and omnichannel return framing.
- `In-app and mobile omnichannel journeys`, lines 30–39: click/collect, reserve/collect, table/mobile pay and self-scan examples.
- `Pay anywhere in store`, lines 41–42: terminal, link and kiosk checkout examples.
- `Next steps`, lines 44–56: child pages for endless aisle, Pay by Link and referenced refunds; their procedures are not evidence from this overview.

## Related

- [[adyen-unified-commerce]] — primary provider concept for cross-channel journeys.
- [[adyen-online-payments]] — online payment context, separately evidenced.
- [[adyen-terminal-api]] — in-person terminal message context, separately evidenced.

## Raw Sources

- [[raw/adyen/docs/unified-commerce/shopper-experiences/2026-09-15|Adyen Shopper Experiences overview, fetched 2026-09-15]]
