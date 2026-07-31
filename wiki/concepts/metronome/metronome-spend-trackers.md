---
title: "Metronome Spend Trackers"
type: concept
category: technology
tags: [metronome, spend-trackers, contracts, commits, discounts, public-beta]
---

## Definition

A Metronome spend tracker is a public-beta contract configuration that sums selected spend over a reset period. Other contract configurations can reference its alias for spend-based behavior, while merchant applications can query the accumulated total for pricing decisions that Metronome does not enforce directly.

## Eligible spend and configuration

Trackers can be configured during package creation, contract creation, or contract edit. Each has an alias, credit type, reset frequency, and applicable-spend specifiers. The documented eligibility is currently limited to commit purchases: a tracker can select manual commits, threshold-recharge commits, or both, and can optionally filter on whether a purchase is marked discounted. Manual commits use `spend_tracker_attributes.count_as_discounted`; threshold commits derive that classification from `discount_config`.

This is not a generic customer-usage accumulator. The page does not say that usage events, rated usage, invoice totals, payment volume, or balance consumption count toward the tracker.

## Threshold-discount caps

A prepaid-balance threshold's `discount_config.cap` can reference a spend-tracker alias and amount. In the documented billing-period example, once qualifying discounted manual and threshold-recharge commit spend reaches the cap, new threshold commits remain undiscounted until the next billing period. The source does not define amount scaling, exact equality semantics, concurrent cap crossings, or retroactive adjustments.

## Retrieval and enforcement

The contract query returns `accumulated_spend.amount` and current-period start and exclusive-end timestamps with the tracker definition. No freshness, consistency, history, standalone endpoint, or pagination behavior is documented, and the guide's curl body appears response-shaped rather than an authoritative request schema.

Configurations designed to consume a tracker can act on it directly, as the threshold discount does. A separate internal rule is merchant-owned: for a manual payment-gated commit cap, the merchant checks the tracker before issuing the commit. The source does not document tracker alerts, webhooks, customer-facing presentation, automatic rejection of manual commits, or product-access enforcement.

## Billing-state and lifecycle boundaries

The guide does not say when a commit purchase enters accumulated spend or how pending, payment-gated, failed, voided, canceled, refunded, or reversed purchases affect it. It also leaves alias uniqueness, edit and backfill behavior, period reset timing and time zone, backdated purchases, credit-type compatibility, multi-currency conversion, error handling, and tracker deletion unspecified.

## Status

Spend trackers are Public Beta, may introduce breaking changes before general availability, and require access through a Metronome representative.

## Related

- [[metronome-credits-and-commits]]
- [[metronome-customers-and-contracts]]
- [[metronome-alerts-and-notifications]]

## Sources

- [[source-metronome-guides-customers-billing-manage-customers-spend-trackers]] — public-beta scope, eligible commit purchases, reset-period accumulation, threshold-discount integration, and merchant enforcement boundary
