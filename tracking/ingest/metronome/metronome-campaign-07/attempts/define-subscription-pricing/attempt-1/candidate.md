---
title: "Metronome Define Subscription Pricing"
type: source
date_ingested: 2026-07-30
canonical_url: "https://docs.metronome.com/guides/pricing-packaging/subscription/define-subscription-pricing"
original_format: webpage
raw_files:
  - "metronome/guides/pricing-packaging/subscription/define-subscription-pricing-2026-07-13.md"
tags: [metronome, subscriptions, pricing, rate-cards, entitlements, seat-based-billing]
---

## Overview

This short guide defines Metronome's list-price setup for subscription offerings: create a subscription product for each offering, then place it on a rate card. It also documents the prerequisite for a seat-based credit model and the rate attributes used for the quantity-one list price; it is not a complete subscription-contract or API schema reference.

## Key takeaways

- Create a distinct subscription product for each subscription offering, such as Good, Better, and Best plans.
- For a seat-based credit model, applicable usage products need a `seat_id` presentation group key so usage can be determined per product and seat.
- A rate card supplies the subscription offering's list price at quantity one; subscription quantity and associated credits are configured later when creating the contract.
- The documented API setup adds a subscription product as a `flat` rate and specifies `price`, `billing_frequency`, and an entitlement state.
- When one rate card has more than one subscription rate, Metronome recommends defaulting their entitlement states to `false` and enabling the selected rate while provisioning the contract.

## Subscription catalog and seat-based credits

The guide directs an implementer to create one subscription product for each kind of subscription it sells, either in the Metronome app or through the product-create API. Its seat-based credit guidance applies to applicable **usage** products: configure `seat_id` as a presentation group key, then include that property on usage events so Metronome can determine usage for each product and seat. The example is illustrative and does not define seat identifier format, uniqueness, lifecycle, or how seat usage changes affect a contract.

## Rate-card list pricing

A rate card acts as the list price for a subscription offering at quantity one. The guide explicitly places quantity and associated-credit configuration in the later contract-creation stage. To add the subscription through the API, add the product as a `flat` rate and supply a price, billing frequency, and entitlement state. The displayed request uses `entitled: false`, `rate_type: "flat"`, a `starting_at` timestamp, `price: 500`, and `billing_frequency: "MONTHLY"`.

For a card containing more than one subscription rate, the guide recommends defaulting the rates' entitlement states to `false` and enabling the chosen rate during contract provisioning. This is a recommendation for that multi-rate configuration, not a documented universal entitlement default or a complete subscription-selection lifecycle.

## Documentation boundaries

- The guide links to product creation and rate-card add-rate APIs but does not provide their complete request or response schemas, validation rules, idempotency behavior, or error handling.
- It does not define permitted `billing_frequency` or entitlement values, price denomination or precision, the relationship between `starting_at` and billing cycles, or how multiple applicable subscription rates are resolved.
- It does not document contract fields for subscription quantity or associated credits, seat additions or removals, proration, invoicing, cancellation, or entitlement changes after provisioning.

## Related

- Company: [[metronome]]
- Concepts: [[metronome-products-and-rate-cards]], [[metronome-customers-and-contracts]]
- Related source: [[source-metronome-guides-implement-metronome-core-concepts-create-manage-rate-cards]]

## Raw Sources

- [[raw/metronome/guides/pricing-packaging/subscription/define-subscription-pricing-2026-07-13]] — verbatim subscription-pricing guide
