---
title: "Metronome Subscription Overview"
type: source
date_ingested: 2026-07-30
original_format: webpage
canonical_url: "https://docs.metronome.com/guides/pricing-packaging/subscription/subscription-overview"
raw_files:
  - "metronome/guides/pricing-packaging/subscription/subscription-overview-2026-07-13.md"
tags: [metronome, subscriptions, recurring-billing, seat-based-billing, rate-cards, contracts, credits]
---

## Overview

This overview introduces Metronome subscriptions as recurring-fee products billed on a schedule. It maps the high-level subscription model across products, rate-card rates, and customer contracts, including quantity, collection timing, proration, and optional credit provisioning; it is not an API or lifecycle specification.

## Key takeaways

- Subscription fees support seat-based billing, platform fees, and other recurring charges.
- A subscription product drives the invoice line item; Metronome recommends one product per subscription type, analogous to a SKU.
- A rate card holds each standard price at quantity `1`; one product can map to distinct rates for different billing frequencies.
- The overview says to set `entitlement` to `true` for the purchased subscription rate, then use the contract for quantity, proration, and in-advance or in-arrears collection. That wording is source evidence, not a confirmed API-field schema.
- Credit balance may optionally be provisioned with a subscription, pooled at the subscription level, or scoped per seat.

## Subscription data model

### Products and rates

Metronome describes the subscription product as the catalog item that ultimately drives a customer invoice line item. It recommends a separate product for each offering, such as Good, Better, and Best, and compares those products to SKUs.

A rate card holds each standard price, with the displayed price representing quantity `1`. One product can have multiple rates: the guide's Good, Better, and Best example across monthly, quarterly, and annual billing frequencies has nine rates, or three rates per product. This overview does not define rate schemas, effective-date behavior, or price precedence.

### Customer contracts and credits

For a purchased plan, the guide directs the reader to create a customer contract and says to set `entitlement` to `true` for its corresponding subscription rate. The contract sets subscription quantity, proration behavior, and collection behavior in advance or in arrears. Metronome does not distinguish recurring platform fees from seat-based subscriptions in this overview; `quantity` counts subscriptions and most commonly models the seats to which a customer is entitled.

The contract can optionally provision credit balance. The guide limits this statement to credit scope: balance may be pooled for the subscription or scoped to individual seats; it does not document provisioning mechanics, drawdown, or hybrid-model accounting.

## Terminology caution

This overview's prose uses `entitlement`, while the existing Metronome product and rate-card context documents an `entitled` field for whether a rate appears on customer invoices by default. Preserve the overview's wording as evidence, but do not treat `entitlement` as an authoritative API field or infer that the two terms have identical schema semantics without a dedicated current schema source.

## Follow-on guide routes

The four cards route readers to other guides; their descriptions identify scope but do not supply those guides' mechanics or schemas here:

- **Define subscription pricing:** create subscription products and add them to a rate card to define standard list prices.
- **Provision your customer:** create contracts based on the selected plan, covering standard recurring fees and hybrid credit models.
- **Manage seats:** change the seat count per subscription, optionally associate a seat with a user ID, view changes over time, and manage seat balance for hybrid models.
- **Subscription lifecycle:** model subscription transitions within Metronome.

## Scope and unknowns

This short overview does not define subscription endpoints; rate, schedule, or contract schemas; proration calculations; in-advance or in-arrears collection mechanics; entitlement semantics; credit provisioning or drawdown; seat-management rules; lifecycle-transition behavior; or invoice-state behavior. The linked pricing, provisioning, seat-management, and lifecycle guides are the appropriate follow-on sources.

## Related

- Company: [[metronome]]
- Concepts: [[metronome-subscriptions]], [[metronome-products-and-rate-cards]], [[metronome-customers-and-contracts]], [[metronome-credits-and-commits]]

## Raw Sources

- [[raw/metronome/guides/pricing-packaging/subscription/subscription-overview-2026-07-13|2026-07-13 snapshot — subscription products, rates, contracts, quantities, credits, and follow-on guide routes]]
