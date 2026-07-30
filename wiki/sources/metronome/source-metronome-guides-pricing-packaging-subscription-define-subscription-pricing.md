---
title: "Metronome Define Subscription Pricing"
type: source
date_ingested: 2026-07-30
original_format: webpage
canonical_url: "https://docs.metronome.com/guides/pricing-packaging/subscription/define-subscription-pricing"
raw_files:
  - "metronome/guides/pricing-packaging/subscription/define-subscription-pricing-2026-07-13.md"
tags: [metronome, subscriptions, pricing, rate-cards, entitlements, seat-based-billing]
---

## Overview

This guide defines Metronome's list-price setup for subscription offerings: create a subscription product for each offering, then add it to a rate card. It also documents the conditional seat-based-credit prerequisite for applicable usage products and a narrow rate-setup example; it is not a complete subscription-contract or API-schema reference.

## Key takeaways

- Create one subscription product for each subscription offering, such as Good, Better, and Best plans.
- For a seat-based credit model, all applicable usage products need a `seat_id` presentation group key so Metronome can determine usage per product and seat.
- A rate card supplies a subscription offering's list price at quantity `1`; quantity amount and associated credits are configured later during contract creation.
- The illustrated API request sets `rate_type` to `flat`, specifies `price`, `billing_frequency`, and an entitlement state, and uses `entitled: false`.
- When a rate card has more than one subscription rate, Metronome recommends defaulting those rates to `false` and enabling the applicable rate or rates when provisioning a contract.

## Subscription products and seat-based credits

The guide directs an implementer to create a subscription product for each kind of subscription it sells, either in the Metronome app or through the product-create API. Its seat-based-credit guidance is conditional and applies to applicable **usage** products: configure `seat_id` as a presentation group key. The example usage event includes that property, and the guide says it lets Metronome determine usage on a per-product, per-seat basis. It does not define the seat identifier's format, uniqueness, lifecycle, or how seat usage changes affect a contract.

## Rate-card list pricing and entitlement setup

A rate card acts as the list price for a subscription offering at quantity `1`; subscription quantity amount and associated credits are configured later during contract creation. For the API rate setup, the guide says to add the subscription as a `flat` rate, then specify a `price`, `billing_frequency`, and entitlement state. In the displayed request, `rate_type` has the value `flat`, while the request includes `price: 500`, `billing_frequency: "MONTHLY"`, `starting_at`, and `entitled: false`.

If a rate card has more than one subscription rate, Metronome recommends defaulting those rates to `false` and enabling the applicable rate or rates when provisioning a contract. The guide does not define a singular selection rule, exclusivity, or how multiple applicable rates are resolved.

## Documentation boundaries

- The guide links to product creation and rate-card add-rate APIs but does not provide complete request or response schemas, validation rules, idempotency behavior, or error handling.
- It does not define permitted `billing_frequency` or entitlement values, price denomination or precision, `starting_at` billing-cycle behavior, or non-`flat` rate behavior.
- It does not document contract request fields for quantity or associated credits, seat additions or removals, proration, invoicing, cancellation, or entitlement changes after provisioning.

## Related

- Company: [[metronome]]
- Concepts: [[metronome-subscriptions]], [[metronome-products-and-rate-cards]], [[metronome-customers-and-contracts]]
- Related sources: [[source-metronome-guides-pricing-packaging-subscription-subscription-overview]], [[source-metronome-guides-implement-metronome-core-concepts-create-manage-rate-cards]]

## Raw Sources

- [[raw/metronome/guides/pricing-packaging/subscription/define-subscription-pricing-2026-07-13|2026-07-13 snapshot — verbatim subscription-pricing guide]]
