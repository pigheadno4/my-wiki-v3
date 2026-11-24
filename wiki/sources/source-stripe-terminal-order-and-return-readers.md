---
title: "Stripe Terminal: Place Hardware Orders"
type: source
date_ingested: 2026-05-01
date_updated: 2026-11-24
original_format: webpage
canonical_url: "https://docs.stripe.com/terminal/fleet/order-and-return-readers"
raw_files:
  - "stripe-terminal-fleet-order-and-return-readers-2026-11-07.md"
  - "stripe-terminal-order-and-return-readers-2025.md"
tags: [stripe, stripe-terminal, hardware, fleet, orders, returns, api, shipping]
---

## Summary

The May and November 2026 [[stripe|Stripe]] Terminal guide covers Dashboard ordering, tracking and eligible returns, plus order creation, retrieval and listing through the Hardware Orders API preview. The 2026-11-07 capture adds preregistration for eligible smart readers and device-level webhook outcomes. See [[stripe-terminal-hardware-orders]] for the fleet workflow.

## Key Details

**Ordering** — Buy pre-certified readers and accessories in Dashboard → Terminal → Shop or through the Hardware Orders API preview. Both guides state a limit of 10,000 of each item in a single order. Contact Stripe sales for volume discounts.

**Order statuses** — Pending lasts at least 30 minutes and allows Dashboard cancellation. Ready to ship ends cancellation. The order becomes Shipped when tracking is available. The November capture includes the v4 state diagram with branches from Pending to Canceled and from Shipped to Delivered or Undeliverable.

**Shipping** — Stripe lists eligible destinations, excluded territories, cutoff times and signature thresholds. Hardware ships to physical addresses. Destination determines available standard, express or priority options. Stripe selects freight for large orders. Terminal Connect platforms can specify a connected account's eligible physical destination address. The chart lists 40 destinations in both captures, with example signature thresholds above 500 USD in the US and 400 EUR at many European destinations.

**Permissions** — Support Specialist and View Only cannot place or cancel Dashboard orders. View Only cannot initiate self-service returns.

## Preregister Smart Readers

The 2026-11-07 guide describes selecting one Terminal location per order when ordering eligible smart readers. Edit that location on the hardware order details page until serial numbers are available. Stripe then automatically registers eligible readers to the selected location. For an order spanning multiple locations, wait for serial numbers and register each reader individually by serial number. Other registration methods are covered by [[source-stripe-terminal-register-readers]].

## Returns

Eligible Dashboard users can start self-service returns from **Return items** for Dashboard orders placed and shipped within the guide's listed countries when the order is Shipped or Delivered. The 30-day window starts at purchase and requires original packaging and accessories. The first initiated return refunds shipping fees. Stripe issues a refund when the distribution facility receives the package. Credit card funds can take up to 10 days to return.

> [!warning] Dated self-service scope
> The 2026-05-01 guide lists 33 self-service countries, including Gibraltar (`GI`). The 2026-11-07 guide lists 32 and omits `GI`, which remains in both shipping tables. The captures leave the effective date and account-specific eligibility unresolved. When self-service is unavailable, use **Contact support** on the Dashboard order and keep the original packaging and accessories within the 30-day window. The guide directs returns past 30 days to Stripe Support.

## Hardware Orders API Preview

Sales assesses preview eligibility. The guide requires a Stripe Account manager, agreement to monthly invoice billing and acknowledgment that timely integration updates may be needed. Retrieve available SKUs and shipping methods with the `country` filter. The shipping method must be available for the shipping address's country, and all SKUs and shipping methods must share a provider. Query availability dynamically. The optional order preview validates and estimates taxes without creating an order. The guide then shows order creation, retrieval and listing.

- **2026-11-07** — `Stripe-Version: 2026-10-28.endive;terminal_hardware_orders_beta=v5`.
- **2026-05-01** — `Stripe-Version: 2026-04-22.dahlia;terminal_hardware_orders_beta=v5`.

The guide also requires version configuration for webhook endpoints and gives the matching dated header as its example. Both captures list six `terminal.hardware_order.*` events for order states. November adds `terminal.hardware_order_device.registered` and `terminal.hardware_order_device.registration_failed` for automatic registration attempts on eligible devices when the account has API preview access. Each event's `data.object` is the Hardware Order Device. Use its device ID, serial number and hardware order relationship to correlate the result.

Status update helpers are sandbox-only. The changelog documents a historical duplicate `terminal.hardware_order.shipped` event when v3 and v4 webhooks are enabled in the same mode, and maps v4 `ready_to_ship` to v3 `shipped`. Both captures pair their API version with beta v5 and mark v1–v3 deprecated.

## Related

- [[stripe-terminal-hardware-orders]] — ordering, shipping, returns and the Hardware Orders API preview
- [[stripe-terminal]] — Terminal fleet management

## Raw Sources

- [[raw/stripe-terminal-fleet-order-and-return-readers-2026-11-07|2026-11-07 Stripe Terminal hardware orders guide]] — full guide with preregistration, device webhooks and updated return list
- [[raw/stripe-terminal-order-and-return-readers-2025|2026-05-01 Stripe Terminal hardware orders guide]] — full earlier guide with shipping table, prior preview header and historical return list
