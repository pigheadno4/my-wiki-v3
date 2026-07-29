---
title: "Metronome Dashboard Quickstart: First Invoice"
type: source
date_ingested: 2026-07-29
canonical_url: "https://docs.metronome.com/guides/get-started/metronome-dashboard-quickstart"
original_format: webpage
raw_files:
  - "metronome/guides/get-started/metronome-dashboard-quickstart-2026-07-13.md"
tags: [metronome, usage-based-billing, invoicing, dashboard]
---

## Overview

This dashboard-only quickstart walks a Sandbox user from event-schema design through billable metrics, products, rate cards, a customer contract, test events, and a first invoice. It separates metering from rating: usage events and billable metrics determine measured quantities, while products, rate cards, and contracts determine what appears on an invoice and what it costs.

## Key takeaways

- Usage events require a unique `transaction_id`, `customer_id`, `event_type`, and `timestamp`; `properties` carry quantities, pricing dimensions, and invoice or analytics metadata, with up to 2,000 properties per event.
- A streaming billable metric uses an exact event-type filter, an aggregation key, an aggregation type (`Count`, `Sum`, or `Max`), and creation-time group keys. Group keys cannot be added or changed after the metric is created.
- Products map a billable metric to an invoice line item. Pricing and presentation group keys must be a subset of the underlying billable metric's group keys; quantity and rounding conversions are optional.
- A rate card is a centralized, single-fiat-currency price table. Its rates can use dimensional values, tiers, custom pricing-unit conversions, commit rates, and effective-date changes; contracts reference the rate card and can add customer-specific commits or overrides.
- Dashboard test-event entry is Sandbox-only. Each test event needs a unique transaction ID, a timestamp within the preceding 34 days, and an event type and properties that match the metric filters and group keys. Production event delivery uses the API.

## Dashboard workflow

### Design the event contract

Metronome distinguishes raw usage events from charge calculation. Before creating a metric, define the event fields that will support current and future billing: quantities to aggregate, dimensions to price by, and metadata needed for invoice display or analytics. The page advises retaining useful metadata because pricing or presentation dimensions must be established through metric group keys before downstream product configuration.

### Configure the billable metric

In **Offering → Billable Metrics → + Add**, create either a streaming metric for most real-time aggregation use cases or a SQL metric for calculations such as daily averages, unique counts per period, or weighted formulas. For the streaming path, name the metric, set an event-type filter that exactly matches emitted events, select the property to aggregate, choose `Count`, `Sum`, or `Max`, select group keys, review the example event payload, and save.

Group keys control two downstream uses: a pricing group key permits different rates for values such as `model_name`, while a presentation group key produces invoice breakdowns such as by `user_id`. They must be defined on the billable metric before a product can use them; the guide states that the metric's group keys, property filters, and aggregation settings cannot be modified after creation.

### Create products and price them

In **Offering → Products → + Add new product**, create a named invoice line item. The documented product types are usage, subscription, composite, and fixed; a usage product selects the billable metric. Assign no group key for a flat usage price, a pricing group key for dimension-specific prices, a presentation group key for same-price invoice breakdowns, or both where needed. A quantity conversion can transform sent quantities for display and pricing, and a rounding conversion can transform units such as seconds to minutes.

In **Offering → Rate Cards → + Add new rate card**, add products and their rates. A single standard rate card is recommended as the usual price source of truth because rate updates propagate to contracts that reference it, while contracts can override rates per customer. The guide also documents volume tiers, custom pricing units configured before their rate-card conversion, commit-specific rates, and date-effective edits or additions.

### Provision the customer and contract

Create a customer under **Customers → + Add customer** and optionally add ingest aliases so engineering can send internal customer IDs rather than the Metronome UUID. On the customer's page, add a contract, select the rate card, set contract start and end dates, and optionally connect an invoice integration or add customer-specific credits, commits, or overrides. The page names Stripe and AWS/Azure Marketplace as billing-provider examples.

### Test and verify billing

For Sandbox testing, open the customer contract, select a rate-card product, and use the dashboard's test-event option. After event ingestion, find the current-period draft invoice under **Customers → Contract → Invoices** and verify quantities and charges. If usage appears under Connections but charges do not appear, the page directs the user to check that event values match the rate card's pricing-group-key values.

## Invoice and payment boundary

Metronome automatically generates invoices on the contract billing schedule. A draft accumulates usage during the period; at period end, the guide gives a 24-hour grace period before finalization. When a billing provider is connected, the guide says the invoice is pushed within approximately one hour of finalization. Metronome delegates payment collection and paid/failed status to that provider; webhooks can notify a customer system of payment statuses for payment-gated commits.

## Scope and caveats

- This is a dashboard quickstart, not the programmatic setup path; the page directs engineering-led integration to the API Quickstart.
- Test-event entry is unavailable in production, and production events are sent through the API.
- The source describes streaming metric setup; SQL metrics are only identified as the option for complex calculations and are linked to separate documentation.
- The page's invoice-delivery timing and payment-status handling describe the connected billing-provider path; it does not define provider-specific configuration, retries, or payment-state synchronization details.

## Related

- Company: [[metronome]]
- Concepts: [[metronome-event-ingestion]], [[metronome-billable-metrics]], [[metronome-products-and-rate-cards]], [[metronome-customers-and-contracts]], [[metronome-invoicing]], [[metronome-webhooks]]
- Related sources: [[source-metronome-guides-events-design-usage-events]], [[source-metronome-guides-get-started-home]], [[source-metronome-guides-invoices-overview]]

## Raw Sources

- [[raw/metronome/guides/get-started/metronome-dashboard-quickstart-2026-07-13|2026-07-13 snapshot — dashboard first-invoice quickstart]]
