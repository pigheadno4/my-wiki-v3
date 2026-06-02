---
title: "Stripe: Create and Configure a Meter"
type: source
date_ingested: 2026-05-05
original_format: webpage
raw_files:
  - "stripe-usage-based-billing-meters-configure-2025.md"
tags: [stripe, billing, usage-based, meters, ingestion]
---

## Summary

Deep-dive on meter creation and configuration for usage-based billing. Covers Dashboard and API creation paths, all configuration attributes, ingestion modes (Raw vs Pre-aggregated), and how to fix incorrect usage data via Meter Event Adjustments.

## Key Details

**Meter configuration attributes:**

| Attribute | Description |
| --- | --- |
| Event name | Unique per meter; must match `event_name` in meter events |
| Event ingestion | Raw (default) or Pre-aggregated |
| Aggregation formula | sum, count, last |
| Payload key overrides | `value_settings.event_payload_key` (default: `value`), `customer_mapping.event_payload_key` (default: `stripe_customer_id`) |

**Ingestion modes:**

- **Raw** (default): every event is standalone; multiple events for the same timestamp all count toward aggregation.
- **Pre-aggregated**: if multiple events arrive within the same hourly or daily window, only the most recently received event is kept. UTC boundaries dictate hour/day intervals.

**Immutability**: after meter creation, only `display_name` can be changed. All other configuration is locked.

**Meter Event Adjustment** — cancel incorrectly recorded events:

- Must specify the `identifier` of the event to cancel
- Only events sent within the last 24 hours can be cancelled
- Cancellations do not update finalized invoices
- Negative quantities are also valid for correcting usage (if aggregate goes negative, Stripe reports 0)

API: `stripe.billing.meterEventAdjustments.create({ type: 'cancel', event_name, cancel: { identifier } })`

## Raw Sources

- [[stripe-usage-based-billing-meters-configure-2025]] — verbatim webpage content (93 lines)
