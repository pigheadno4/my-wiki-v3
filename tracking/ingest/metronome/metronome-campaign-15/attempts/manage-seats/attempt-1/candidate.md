---
title: "Manage Metronome Subscription Seats"
type: source
date_ingested: 2026-08-19
original_format: webpage
canonical_url: "https://docs.metronome.com/guides/pricing-packaging/subscription/manage-seats.md"
raw_files:
  - "metronome/guides/pricing-packaging/subscription/manage-seats-2026-07-13.md"
tags: [metronome, subscriptions, seat-based-billing, credits, alerts, contract-edits]
---

## Overview

This guide explains how to change subscription seat counts after contract creation, monitor pooled or seat-scoped credit balances, and retrieve quantity, seat-assignment, and ledger history. It distinguishes quantity-managed subscriptions from seat-based credit subscriptions whose `seat_config` tracks assigned seat IDs and unassigned seats.

## Key takeaways

- Standard subscriptions and credit pools use the edit-contract `update_subscription` action with either a new total `quantity` or a relative `quantity_delta`. Updates sharing a `starting_at` timestamp are applied in submission order, and invoice treatment follows the subscription's proration configuration.
- Changing the quantity of a subscription linked to recurring credits also releases credit balance; the amount depends on the recurring-credit `access_amount` and applicable proration settings.
- Seat-based credit subscriptions instead edit assigned `seat_ids` and optional unassigned seats. Removing an assigned seat ID while adding one unassigned seat at the same effective time preserves total subscription quantity while freeing capacity for reassignment.
- Contract- or customer-level credit alerts exclude seat-scoped credits. Seat-scoped monitoring uses `low_remaining_seat_balance_reached` and requires a `seat_filter.seat_group_key`; an optional `seat_group_value` narrows the rule to one seat.
- Quantity history and seat-ID history use separate contract endpoints. The seat-balance list can return all current seat balances or one seat, and `include_ledgers: true` adds grant and burn-down history that can be time-filtered.

## Seat-count changes

For quantity-managed subscriptions, schedule an `update_subscription` action through the edit-contract endpoint and provide either the desired total through `quantity` or the change from the prior amount through `quantity_delta`. When multiple updates use the same `starting_at`, Metronome applies them in the order submitted. The guide ties invoicing to the subscription's proration settings but does not define the proration formula, invoice-state interactions, idempotency, concurrency, or failure atomicity.

When a quantity-managed subscription is linked to recurring credits, a quantity change can release new credit balance. The guide says the amount depends on proration and the recurring credit's `access_amount`; it does not document an exact increase or decrease formula, the resulting ledger timing, or whether a decrease removes previously released balance.

For a seat-based credit subscription, `seat_updates` can add or remove assigned `seat_ids` and add unassigned-seat quantity. The examples schedule each operation independently. To free an assigned identity without reducing purchased capacity, remove that seat ID and add one unassigned seat at the same effective time. The page does not define seat-ID uniqueness, reassignment races, removal of unassigned seats, validation, or whether the paired changes are atomic.

## Balance alerts and retrieval

A general credit-balance threshold evaluates customer- or contract-level credits and excludes seat-scoped credits. For seat-scoped credits and commits, create a `low_remaining_seat_balance_reached` notification. Its request requires `seat_filter`, whose `seat_group_key` selects balances associated with seat-based subscriptions configured with that key; `seat_group_value` is optional and narrows the notification to a specific seat. Alert state for a specific seat can be queried through the customer-alert get endpoint.

For product-facing history, quantity-managed subscriptions use the subscription-quantity-history endpoint, while `seat_config` subscriptions use the subscription-seats-history endpoint for seat-ID history. The seat-balance list returns current balance for all seats when given customer and contract IDs and can be scoped by `seat_id`. With `include_ledgers: true`, it also returns credit-grant and burn-down history; `starting_at` and `ending_before` optionally bound the requested period. The guide does not define pagination, ordering, read consistency, precision, or whether the time bounds are inclusive or exclusive.

## Documentation boundaries

The JSON and curl bodies are worked examples rather than complete endpoint schemas. This page does not document authentication requirements, response schemas, error codes, retry or idempotency behavior, concurrent edits, webhook delivery guarantees, automatic access enforcement, or accounting treatment. Access gating after a low-balance webhook is an action the merchant may take, not a documented automatic Metronome entitlement change. No direct contradiction was found with the existing Metronome subscription, credit-and-commit, alert, remaining-balance, or contract-edit-history pages when the customer/contract alert exclusion and seat-scoped alert path remain distinct.

## Related

- Company: [[metronome]]
- Concepts: [[metronome-subscriptions]], [[metronome-credits-and-commits]], [[metronome-alerts-and-notifications]], [[metronome-customers-and-contracts]]
- Related sources: [[source-metronome-guides-pricing-packaging-subscription-subscription-overview]], [[source-metronome-guides-pricing-packaging-subscription-define-subscription-pricing]], [[source-metronome-guides-customers-billing-optimize-customer-experience-get-remaining-balance]], [[source-metronome-api-reference-contracts-get-contract-edit-history]]

## Raw Sources

- [[raw/metronome/guides/pricing-packaging/subscription/manage-seats-2026-07-13|2026-07-13 snapshot - seat changes, seat-scoped alerts, and seat balance and history retrieval]]
