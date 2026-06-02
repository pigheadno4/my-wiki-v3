---
title: "Stripe: Set Up a Pay-As-You-Go Pricing Model"
type: source
date_ingested: 2026-05-05
original_format: webpage
raw_files:
  - "stripe-usage-based-billing-payg-2025.md"
tags: [stripe, billing, usage-based, meters, subscriptions, pricing, pay-as-you-go]
---

## Summary

End-to-end implementation guide for pay-as-you-go pricing using Stripe's Meter API (v2). Uses a fictional LLM company (Hypernian: $0.04 per 100 tokens) as a running example. Covers Dashboard and API paths for every step.

## Key Details

### Step 1: Create a meter

- `stripe.billing.meters.create({ display_name, event_name, default_aggregation: { formula }, customer_mapping: { event_payload_key: 'stripe_customer_id', type: 'by_id' }, value_settings: { event_payload_key: 'value' } })`
- Aggregation formulas: **sum** (total value), **count** (number of events), **last** (last value reported)

### Step 2: Create a metered price

- `stripe.prices.create({ currency, unit_amount, billing_scheme: 'per_unit', transform_quantity: { divide_by: 100, round: 'up' }, recurring: { usage_type: 'metered', interval: 'month', meter: METER_ID }, product_data: { name } })`
- Meter ID referenced directly on the price via `recurring.meter`
- Pricing structures: per package (transform_quantity), per unit, per tier (tiered pricing)

### Step 3: Create a customer

- Standard `stripe.customers.create({ name })` — or Accounts v2 equivalent

### Step 4: Create a subscription

- `stripe.subscriptions.create({ customer: CUSTOMER_ID, items: [{ price: PRICE_ID }] })`
- `billing_mode=flexible`: no first invoice for metered items (recommended — no prior usage to bill)
- `billing_mode=classic`: generates zero-value line item for metered items on first invoice

### Step 5: Send meter events

- `stripe.billing.meterEvents.create({ event_name, payload: { stripe_customer_id: CUSTOMER_ID, value: '25' } })`
- `value` is a **string** in the payload
- Meter events process asynchronously — preview invoices may lag

### Step 6: Preview invoice

- `stripe.invoices.createPreview({ subscription: SUBSCRIPTION_ID })`

### Optional: Query event summaries

- `stripe.billing.meters.listEventSummaries(METER_ID, { customer, start_time, end_time })` — Unix timestamps

## Raw Sources

- [[stripe-usage-based-billing-payg-2025]] — verbatim webpage content (276 lines, full end-to-end guide with Dashboard + API for every step)
