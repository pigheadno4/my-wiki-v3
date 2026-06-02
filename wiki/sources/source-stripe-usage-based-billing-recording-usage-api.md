---
title: "Stripe: Record Usage for Billing with the API"
type: source
date_ingested: 2026-05-05
original_format: webpage
raw_files:
  - "stripe-usage-based-billing-recording-usage-api-2025.md"
tags: [stripe, billing, usage-based, meters, ingestion, api, rate-limits, webhooks]
---

## Summary

Deep-dive on API-based meter event ingestion. Covers standard and high-throughput (API v2) ingestion paths, event timestamp rules, idempotency, rate limits, and async error handling via thin webhook events.

## Key Details

**Create meter events** — `stripe.billing.meterEvents.create({ event_name, payload: { value, stripe_customer_id } })`

- `value` is a string; decimal values accepted
- `identifier` field optional — auto-generated if omitted (used for idempotency and cancellation)
- Timestamp optional — defaults to now

**Event timestamp constraints:**

- Must be within the past **35 calendar days**
- Must not be more than **5 minutes in the future** (clock drift tolerance)

**Rate limits (v1 endpoint):**

- Live mode: **1,000 calls/second**
- Connect platforms (using `Stripe-Account` header): **100 ops/second**
- Sandbox: counts toward basic rate limit
- Mitigation: pre-aggregate before sending, or use v2 high-throughput endpoint

**High-throughput ingestion (API v2 — Meter Event Streams):**

- Up to **10,000 events/second** (live mode only; contact sales for up to 200,000/s)
- Uses stateless auth sessions: create a `MeterEventSession` (15-minute token) → use token to call `MeterEventStream`
- Stream events not logged in Workbench Logs tab

```js
// Session (refresh every 15 min)
meterEventSession = await client.v2.billing.meterEventSession.create();

// High-throughput event
const client = new Stripe(meterEventSession.authentication_token);
await client.v2.billing.meterEventStream.create({ events: [{ event_name, payload }] });
```

**Async error handling — thin events:**

| Event | Trigger |
| --- | --- |
| `v1.billing.meter.error_report_triggered` | Meter has invalid usage events |
| `v1.billing.meter.no_meter_found` | Events reference missing/invalid meter IDs |

Both are thin events — subscribe via Workbench with **Thin** payload style. Fetch full event with `client.v2.core.events.retrieve(thinEvent.id)` then `event.fetchRelatedObject()` for the meter.

**Error codes** (`reason.error_types.code`):
`meter_event_customer_not_found`, `meter_event_no_customer_defined`, `meter_event_dimension_count_too_high`, `archived_meter`, `timestamp_too_far_in_past`, `timestamp_in_future`, `meter_event_value_not_found`, `meter_event_invalid_value`, `no_meter`

## Raw Sources

- [[stripe-usage-based-billing-recording-usage-api-2025]] — verbatim webpage content (290 lines)
