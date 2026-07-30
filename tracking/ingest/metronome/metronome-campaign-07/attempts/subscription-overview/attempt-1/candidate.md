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

This overview introduces Metronome subscriptions as recurring-fee products billed on a schedule. It describes the subscription data model across products, rate-card rates, and customer contracts, including seat quantities, entitlement, collection timing, proration, and optional credit provisioning.

## Key takeaways

- Subscription fees support seat-based billing, platform fees, and other recurring charges.
- A subscription product drives the invoice line item; a distinct product represents each subscription offering, such as a Good, Better, or Best plan.
- A rate card holds each standard price for quantity `1`. One product can have multiple rates, such as separate monthly, quarterly, and annual prices.
- When a customer buys a plan, create a contract and set `entitlement` to `true` for the selected subscription rate. The contract sets quantity, proration behavior, and in-advance or in-arrears collection behavior.
- Credits can optionally be provisioned with a subscription and pooled at the subscription level or scoped per seat.

## Subscription data model

### Products and rates

Metronome treats a subscription product as the catalog item that ultimately drives a customer invoice line item. The guide recommends creating one product for each subscription type and compares these products to SKUs.

Rates are added to a rate card for each standard price, with the listed price representing quantity `1`. A product may map to multiple rates. The guide's illustrative Good, Better, and Best offerings across monthly, quarterly, and annual billing frequencies therefore use nine rates: three per product.

### Customer contracts

A customer purchasing a subscription plan receives a contract with the corresponding subscription rate entitled. The contract controls the subscription quantity, proration behavior, and whether Metronome collects in advance or in arrears. The guide does not distinguish a recurring platform fee from a seat-based subscription; `quantity` represents the number of subscriptions and commonly the number of seats to which the customer is entitled.

The contract can also provision credit balance as part of the subscription. The guide says that balance may be pooled for the subscription or scoped to individual seats.

## Scope and unknowns

This is a short data-model overview, not an API reference or lifecycle specification. It does not define subscription endpoints, rate or schedule schemas, the calculation rules for proration or in-advance versus in-arrears collection, entitlement semantics, credit-provisioning mechanics, or seat-management and transition behavior. The linked pricing, provisioning, seat-management, and lifecycle guides are the appropriate follow-on sources.

No direct contradiction with the current Metronome product/rate-card or contract concepts was found. This source adds subscription-specific framing and does not establish price-precedence, billing-frequency validation, or invoice-state behavior.

## Related

- Company: [[metronome]]
- Concepts: [[metronome-subscriptions]], [[metronome-products-and-rate-cards]], [[metronome-customers-and-contracts]], [[metronome-credits-and-commits]], [[metronome-usage-based-billing]]
- Related sources: [[source-metronome-guides-implement-metronome-core-concepts-create-products-contracts]], [[source-metronome-guides-implement-metronome-core-concepts-provision-contract]], [[source-metronome-guides-get-started-how-metronome-works]]

## Raw Sources

- [[raw/metronome/guides/pricing-packaging/subscription/subscription-overview-2026-07-13|2026-07-13 snapshot — subscription products, rates, contracts, quantities, and credits]]
