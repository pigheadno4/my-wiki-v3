---
title: "Metronome Manage Seats"
type: source
date_ingested: 2026-08-27
original_format: webpage
canonical_url: "https://docs.metronome.com/guides/pricing-packaging/subscription/manage-seats.md"
raw_files:
  - "metronome/guides/pricing-packaging/subscription/manage-seats-2026-07-13.md"
tags: [metronome, subscriptions, seats, credits, idempotency]
---

## Overview

This guide explains how to change subscription seat counts after contract creation, preserve or change seat identity, monitor credit balances, and expose seat history. It distinguishes aggregate quantity management from identity-bearing `seat_config` management and routes exact payload examples and operational detail to the complete raw page.

## Durable facts

- Standard subscriptions and shared credit pools use an edit-contract `update_subscription` action. A caller can submit the new total through `quantity` or a change through `quantity_delta`; aggregate quantity updates with the same `starting_at` are applied in submission order.
- Aggregate quantity changes are invoiced according to the subscription's contract proration configuration. When the subscription is linked to recurring credits, the change also releases credit balance according to that recurring credit's proration settings and `access_amount`.
- Seat-based credit subscriptions preserve identity through `seat_ids`: their update surface can add or remove identified seats and add or remove unassigned seats. Invoice billing and credit release remain configuration-dependent.
- Reassignment without changing total subscription quantity is a two-part lifecycle operation: remove the departing `seat_id` and add one unassigned seat, making the capacity available for a later assignee. The worked example gives both changes the same effective timestamp in one request.
- A customer- or contract-level credit-balance threshold excludes seat-scoped credits. Seat-scoped monitoring instead uses `low_remaining_seat_balance_reached`. The guide explicitly requires the request-body `seat_filter` object when creating this notification and says that object provides `seat_group_key`; it does not independently mark the nested `seat_group_key` property as required. Optional `seat_filter.seat_group_value` narrows monitoring or lookup to one seat.
- Customer-facing history can poll aggregate quantity changes or per-`seat_id` history. The seat-balance list route can return current balances for all seats or one `seat_id`, and `include_ledgers: true` adds grant and burn-down history with optional time bounds.

## Material boundaries

- The guide makes invoice and credit effects depend on existing subscription and recurring-credit configuration. It does not define the proration formula, rounding, invoice state or timing, credit-release timing, atomicity, concurrency, errors, or recovery. The same-`starting_at` ordering statement appears only in the aggregate quantity section and is not a general ordering guarantee for `seat_updates`.
- General customer- or contract-balance alerts explicitly omit seat-scoped credits. Webhook receipt can be used by the merchant to gate access, but the guide does not make the alert an automatic entitlement change or define webhook latency, delivery, retry, or deduplication. The specific-seat `/customer-alerts/get` example omits a comma between `alert_id` and `seat_filter`, so it is malformed JSON and should not be copied as executable code.
- A separate Metronome API-wide authority applies `Idempotency-Key` to all POST requests: identical parameters with the same key replay the original result, changed parameters with the same key return HTTP `409 Conflict`, and keys are retained for at least 24 hours. A cached result can be HTTP `500`; the authority recommends investigating system state and deciding whether to resolve manually or retry rather than automatically switching keys after a potentially partial failure. [[metronome-api-idempotency]]
- Unsafe retries are materially risky here. Reissuing a `quantity_delta` or an unassigned-seat addition with a different or expired key may apply billable capacity twice, with corresponding invoice and credit effects; creating an alert with a new key may likewise duplicate a configured signal. The guide and the API-wide authority do not define edit-, alert-, history-, or balance-endpoint atomicity, read-after-write visibility, concurrent ordering, another-key behavior, or recovery after ambiguous failure. For history and balance reads implemented as POST, same-key result replay also does not prove a fresh view.

## Coverage map

| Raw detail category | Exact raw coverage |
| --- | --- |
| Aggregate quantity edits | `quantity` versus `quantity_delta`, `starting_at` ordering, proration dependency, recurring-credit release, and a complete `/contracts/edit` payload |
| Identity-bearing seat edits | `add_seat_ids`, `remove_seat_ids`, unassigned-seat operations, effective timestamps, and a complete seat-update payload |
| Seat reassignment | Same-request example that removes one identified seat and adds one unassigned seat while preserving total quantity |
| Balance notifications | Customer/contract exclusion of seat-scoped credits; guide-required `seat_filter` object; nested key/value scoping; create examples; malformed specific-seat get example |
| History and balance views | Quantity-history and seat-ID-history routes plus current per-seat balance and optional ledger/time-window query behavior |
| Retry decision | Business consequences of repeating `quantity_delta`, unassigned-seat additions, and alert creation; API-wide POST replay remains a separate authority |

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
- Primary concepts: [[metronome-subscriptions]], [[metronome-credits-and-commits]], [[metronome-alerts-and-notifications]], [[metronome-api-idempotency]]
- Additional affected concepts: [[metronome-customers-and-contracts]], [[metronome-invoicing]], [[metronome-reporting-and-analytics]]

## Raw Sources

- [[raw/metronome/guides/pricing-packaging/subscription/manage-seats-2026-07-13|Manage seats — complete raw page]]
