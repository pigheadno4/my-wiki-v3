---
title: "Metronome Manage Seats"
type: source
date_ingested: 2026-08-27
original_format: webpage
canonical_url: "https://docs.metronome.com/guides/pricing-packaging/subscription/manage-seats.md"
raw_files:
  - "metronome/guides/pricing-packaging/subscription/manage-seats-2026-07-13.md"
tags: [metronome, subscriptions, seats, credits]
---

## Overview

This guide explains how to change subscription seat counts after contract creation, preserve or change seat identity, monitor credit balances, and expose seat history. It distinguishes aggregate quantity management from identity-bearing `seat_config` management and routes the exact payload examples and operational detail to the complete raw page.

## Durable facts

- Standard subscriptions and shared credit pools use an edit-contract `update_subscription` action. A caller can submit the new total through `quantity` or a change through `quantity_delta`; aggregate quantity updates with the same `starting_at` are applied in submission order.
- Aggregate quantity changes are invoiced according to the subscription's contract proration configuration. When the subscription is linked to recurring credits, the change also releases credit balance according to that recurring credit's proration settings and `access_amount`.
- Seat-based credit subscriptions preserve identity through `seat_ids`: their update surface can add or remove identified seats and add or remove unassigned seats. Invoice billing and credit release remain configuration-dependent.
- Reassignment without changing total subscription quantity is a two-part lifecycle operation: remove the departing `seat_id` and add one unassigned seat, making the capacity available for a later assignee. The worked example gives both changes the same effective timestamp in one request.
- A customer- or contract-level credit-balance threshold excludes seat-scoped credits. Seat-scoped monitoring instead uses `low_remaining_seat_balance_reached` with a required request-body `seat_filter.seat_group_key`; optional `seat_group_value` narrows monitoring or lookup to one seat.
- Customer-facing history can poll aggregate quantity changes or per-`seat_id` history. The seat-balance list route can return current balances for all seats or one `seat_id`, and `include_ledgers: true` adds grant and burn-down history with optional time bounds.

## Material boundaries

- The guide makes invoice and credit effects depend on existing subscription and recurring-credit configuration. It does not define the proration formula, rounding, invoice state or timing, credit-release timing, atomicity, concurrency, errors, or recovery; do not calculate or promise those outcomes from this guide alone. The same-`starting_at` ordering statement appears in the aggregate quantity section and is not documented here as a general ordering guarantee for `seat_updates`.
- General customer- or contract-balance alerts explicitly omit seat-scoped credits. Webhook receipt can be used by the merchant to gate access, but the guide does not make the alert an automatic entitlement change or define webhook latency, delivery, retry, or deduplication.
- The guide states that `seat_filter` is required when creating the seat-balance notification, but it is not the complete API schema authority. Its specific-seat `/customer-alerts/get` shell example also omits a comma between `alert_id` and `seat_filter`, so copy the intent rather than treating that block as executable JSON.

## Coverage map

| Raw detail category | Exact raw coverage |
| --- | --- |
| Aggregate quantity edits | `quantity` versus `quantity_delta`, `starting_at` ordering, proration dependency, recurring-credit release, and a complete `/contracts/edit` payload |
| Identity-bearing seat edits | `add_seat_ids`, `remove_seat_ids`, unassigned-seat operations, effective timestamps, and a complete seat-update payload |
| Seat reassignment | Same-request example that removes one identified seat and adds one unassigned seat while preserving total quantity |
| Balance notifications | Customer/contract exclusion of seat-scoped credits, seat-alert type, `seat_filter` key/value scoping, create examples, and a specific-seat get example |
| History and balance views | Quantity-history and seat-ID-history routes plus current per-seat balance and optional ledger/time-window query behavior |

Use the path-qualified raw page for the complete request bodies, example UUIDs and timestamps, alert payloads, and endpoint walkthroughs.

## Related raw API references

These are navigation targets named by the assigned guide, not separately read evidence for this source:

- `/api-reference/contracts/edit-a-contract`
- `/api-reference/alerts/create-a-threshold-notification`
- `/api-reference/alerts/get-an-alert`
- `/api-reference/contracts/get-subscription-quantity-history`
- `/api-reference/contracts/get-subscription-seats-history`
- `/api-reference/credits-and-commits/list-seat-balances`

## Related

- Company: [[metronome]]
- Primary concepts: [[metronome-subscriptions]], [[metronome-credits-and-commits]], [[metronome-alerts-and-notifications]]
- Additional affected concepts: [[metronome-customers-and-contracts]], [[metronome-invoicing]], [[metronome-reporting-and-analytics]]

## Raw Sources

- [[raw/metronome/guides/pricing-packaging/subscription/manage-seats-2026-07-13|Manage seats — complete raw page]]
