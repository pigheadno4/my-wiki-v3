---
title: "Database reference"
type: source
date_ingested: 2026-07-14
canonical_url: "https://docs.metronome.com/guides/reporting-insights/data-export/database-reference"
original_format: webpage
raw_files:
  - "metronome/guides/reporting-insights/data-export/database-reference-2026-07-13.md"
tags: [metronome, data-export, database-schema, invoicing, contracts]
---

## Overview

This page is a schema reference for data exported from Metronome to a data warehouse. It documents core entities, events, customers, invoicing, contracts, packages, payments, alerts, and metadata. The invoicing sections distinguish finalized or voided invoices, daily draft snapshots, and daily invoice-breakdown exports, while the contracts sections describe contract, commit, balance, usage-filter, subscription, and pricing data. The page also notes that exported columns may appear nullable in the destination schema.

## Key takeaways

- The export schema covers foundational entities such as billable metrics, credit types, events, and customers.
- The events table contains deduplicated raw events whether or not they matched a billable metric.
- Draft invoice tables are daily snapshots; incomplete drafts have no line items or total and may be hydrated in later snapshots.
- Invoice breakdowns use four separate tables, with draft data exported as month-to-date snapshots and finalized breakdowns exported incrementally.
- Payment data is documented as currently in Private Beta, and the payment gateway schema includes Stripe payment intent and method details.

## Details

### Core entities and events

- The `billable_metric` and `credit_type` tables define foundational Metronome data types, including environment and timestamp fields.
- The `events` table includes transaction ID, customer ID, timestamp, event type, properties, and Metronome metadata ID.
- Customer metadata includes ingest aliases that can be joined with the `events` table; `archived_at` indicates whether a customer is active.

### Invoicing and breakdowns

- Finalized invoice records include invoices with `FINALIZED` or `VOID` status, and no further changes can be made to those invoices or their corresponding line items.
- Draft invoice tables contain daily snapshots based on customer configuration and usage; `DRAFT_INCOMPLETE` invoices have no line items or total in that snapshot.
- Invoice breakdowns are exported through four tables; draft breakdowns contain month-to-date periods through the snapshot timestamp, while finalized breakdowns export incrementally as invoices finalize.
- Invoice breakdown exports can be filtered to ignore specified zero-value and zero-quantity invoices and line items, with enablement handled by a Metronome Solutions Architect.

### Contracts and balances

- Contract exports include contract records, contract-level commits, balances, recurring commits and credits, usage filters, threshold configurations, subscriptions, scheduled charges, hierarchy configurations, and contract modifications.
- The commits table includes contract-level commits but excludes customer-level commits or credits and contract-level credits.
- Usage-filter tables represent changing versions over time; the documented selection methods use contract IDs and time or version filters.

### Pricing and packages

- Contract pricing exports include rate cards, rate-card entries, and product list item versions.
- Package records include duration, rate card, payment-term, billing-provider, delivery-method, alias, environment, snapshot, and metadata fields.

### Payments, alerts, and metadata

- The Payments section is marked Private Beta, and the `payment` table includes invoice, customer, contract, amount, status, error, gateway, and timestamp fields.
- The payment gateway type shown in the schema is `stripe`, with payment intent ID, payment method ID, and an error field.
- Alert exports include alert definitions and customer alert history, while metadata is stored as a client-specific JSON object in the `metadata` column.

## Change history

- 2026-07-14: Luna pilot draft from the assigned raw snapshot.

## Related

- Company: [[metronome]]
- Concepts: coordinator concept audit required before promotion.

## Raw Sources

- [[raw/metronome/guides/reporting-insights/data-export/database-reference-2026-07-13|collection-date snapshot]]
