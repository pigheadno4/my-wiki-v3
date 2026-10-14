---
title: "Adyen Docs: Order, return, or replace terminals"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/managing-terminals/order-terminals"
raw_files:
  - "adyen/docs/point-of-sale/managing-terminals/order-terminals/2026-09-15.md"
tags: [adyen, point-of-sale, customer-area, terminal-management, orders]
---

## Overview

Adyen's POS guide, captured 2026-09-15, explains Customer Area sales orders for terminals, card readers, and accessories, plus return and replacement requests, hardware kits, order cancellation, tracking, and Terminal order update webhooks. API ordering is a separate linked route. The guide covers physical device logistics and TRS billing conditions, not Terminal API payment execution. [[adyen]] · [[adyen-terminal-management]]

## Key takeaways

- Test terminals and Adyen test cards come from the test Customer Area and are limited to test integrations with dummy payments; live terminals are ordered from the live Customer Area. The Customer Area order requires a suitable role, the intended merchant account, use country/region, selected cart items, shipping address, summary review, and placement. The purchase order number is optional for a sales order. Once delivered, the terminal still needs boarding to connect and associate with a store.
- A terminal can only be used in the country or region it was ordered for; a different power cord does not overcome its regional modem constraint. Accessories such as frames and charging bases cannot be returned. The guide says to use a separate sales order for replacement accessories.
- A return order sends back a faulty terminal; replacing it through a separate sales order is different from a TRS replacement request. TRS requires signup and contractual terms and permits return plus a new terminal in one request when the old device's defect is covered. TRS charges continue for devices in terminal inventory; non-return within two weeks of receiving replacement devices triggers their cost. Examination or repair costs can also apply depending on the defect finding. Consult current TRS terms before relying on the snapshot's fee language.
- The ordered cart can be changed until placement. After placement, the order cannot be changed; a Customer Area order with `Placed` status can be cancelled only before Adyen processes it. Shipment tracking and logistical status appear in Customer Area and email, with optional Terminal order update webhooks. For direct-to-store automation, Adyen recommends assigning on `Shipped` instead of waiting for potentially delayed carrier `Delivered` updates; that recommendation is not evidence that a specific terminal is boarded or ready to transact.
- Custom hardware kits require prior Adyen enablement and packaging setup; the snapshot lists annual-volume, region, sleeve-model, and mixed-cart limits. The linked API kit-order route is distinct from this Customer Area procedure.

## Detail locators

- **Environment, roles, and limitations:** opening lines 19–25; raw heading “Requirements” (27–57) has different Customer Area role alternatives for sales, returns, and replacements, the Terminal order update subscription, nonreturnable accessories, and TRS/hardware-kit setup. For sales, `Merchant terminal order` and `Merchant POS standard` are both required when using that role alternative; the other listed roles are alternatives. See “Regional compatibility” (59–63).
- **Sales checkout:** “Submit a sales order” (65–101) covers merchant-account switch, country selection, cart editing, shipping address, optional PO number, pre-placement review, order updates, and post-delivery boarding. Its two-business-day dispatch sentence is snapshot guidance, not a delivery guarantee.
- **Returns, replacements, and TRS:** “Returning or replacing terminals” (103–114), “Terminal Replacement Service (TRS)” and its “How it works”/“What is covered by TRS” subsections (116–150), “Submit a return or replacement order” (152–196), CSV input (197–229), and “Send terminals back to us” (231–255). The return/replacement flow uses device serial number and problem; `New request` replacement is available when signed up for TRS and the terminal is live. Return packaging instructions include checking a replacement for tampering and returning terminals without accessories.
- **Hardware kits and cancellation:** “Hardware kits” and “Order hardware kits” (257–282) list enablement, packaging, volume, region/model, and cart restrictions. “Cancel an order” (284–294) gives the pre-processing `Placed` condition. “Track delivery” (296–306) routes to the carrier.
- **Logistics notifications:** “Terminal order updates” (308–316), “Receive webhooks” (318–327), and “Webhook content” (329–476) define the optional Terminal order update type and sales/return/replacement status fields. Example JSON is illustrative; private-labeling Adyen emails can still leave carrier emails to the recipient.

## Related

- [[adyen-terminal-management]] — device fleet administration and order routes
- [[adyen-pos-store-management]] — separate store account and payment-method administration
- [[adyen-terminal-api]] — separate in-person payment messaging

## Related raw API references

The linked Management API ordering guide, boarding guide, troubleshooting guidance, webhook setup, and current TRS legal terms were not read for this entry; use them as navigation only:

- [[raw/adyen/docs/point-of-sale/automating-terminal-management/order-terminals-api/2026-09-15|Order terminals with the Management API]]
- [[raw/adyen/docs/point-of-sale/managing-terminals/board-terminal/2026-09-15|Board a terminal]]

## Raw Sources

- [[raw/adyen/docs/point-of-sale/managing-terminals/order-terminals/2026-09-15|Adyen order, return, or replace terminals, fetched 2026-09-15]]
