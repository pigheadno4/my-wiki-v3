---
title: "Metronome Data Export Database Reference"
type: source
date_ingested: 2026-07-14
canonical_url: "https://docs.metronome.com/guides/reporting-insights/data-export/database-reference"
original_format: webpage
raw_files:
  - "metronome/guides/reporting-insights/data-export/database-reference-2026-07-13.md"
tags: [metronome, data-export, warehouse-schema, invoices, contracts]
---

## Overview

This reference describes the tables Metronome exports to a customer's data warehouse. It is best used as a schema-navigation map: identify the relevant table family and row grain here, then use the retained raw page for exact columns, nested JSON types, enumerations, and field-level caveats.

## Key takeaways

- All destination columns may appear nullable because of Metronome's export methodology; downstream models should not infer business optionality from warehouse nullability alone.
- The `events` export contains deduplicated raw events whether or not they matched a billable metric.
- Finalized/void invoices, daily draft snapshots, and daily invoice-breakdown snapshots have different grains and update behavior.
- Contract exports are broad and include object snapshots, commits and balances, recurring configurations, filters, thresholds, subscriptions, scheduled charges, hierarchy, modifications, and pricing.
- Time, snapshot, version, and watermark fields are part of correct record selection; consumers should not assume every table contains one timeless current row per ID.

## Table-family map

| Family | Representative tables and use |
| --- | --- |
| Core entities | `billable_metric`, `credit_type`, deduplicated `events`, and `customer` metadata/aliases |
| Finalized invoicing | `invoice` and `line_item` for invoices that are finalized or voided |
| Draft invoicing | `draft_invoice` and `draft_line_item`, emitted as daily point-in-time snapshots |
| Invoice breakdowns | Finalized and draft invoice/line-item breakdown pairs, with daily draft month-to-date snapshots |
| Contract state | Contracts, commits, balances, recurring commits/credits, usage filters, thresholds, subscriptions, charges, and hierarchy |
| Contract changes | Overrides, transitions, edits, and amendments |
| Contract pricing | Rate cards, rate-card entries, and product-list-item versions |
| Other domains | Packages, payments, alerts/history, and client-specific JSON metadata |

The families above are a navigation aid, not a replacement for the complete table list or column reference.

## Query and lifecycle cautions

### Nullable and deprecated fields

Every exported column may appear nullable in the destination schema. Several invoice fields are also explicitly deprecated and expected to be null, so null handling should be driven by table documentation rather than generated warehouse types alone.

### Invoice grains

Finalized invoice tables include `FINALIZED` and `VOID` records that no longer change. Draft tables emit one snapshot per invoice per day during a billing period; `updated_at` is calculation time and `snapshot_time` aligns to start of day UTC. A `DRAFT_INCOMPLETE` row has no total or line items and may be hydrated later.

Invoice breakdowns use four tables. Draft breakdowns contain month-to-date periods through each snapshot so backdated usage and mid-period pricing changes appear in the latest snapshot; finalized breakdowns export incrementally as invoices finalize. Optional export filters for zero-value/zero-quantity data require a Metronome Solutions Architect.

### Contract scope and time selection

The contract family contains both snapshot-style object tables and effective/versioned data. The reference gives separate selection instructions for usage-filter schedule rows and versioned usage-filter rows. The `contracts_commits` table is narrower than the broader balance domain: it includes contract-level commits but excludes customer-level commits or credits and contract-level credits.

### Payments note

The Payments section documents payment and Stripe gateway fields. Its accompanying Private Beta note says that Metronome invoicing is currently in Private Beta; this source does not generalize that statement to every exported table.

## Change history

- 2026-07-14: Initial ingest from the 2026-07-13 collection snapshot; Sol strengthened schema-navigation, row-grain, nullability, and beta-scope language after reviewing the Luna draft.

## Related

- Company: [[metronome]]
- Concept: [[metronome-reporting-and-analytics]]
- Related domains: [[metronome-event-ingestion]], [[metronome-invoicing]], [[metronome-customers-and-contracts]], [[metronome-products-and-rate-cards]]

## Raw Sources

- [[raw/metronome/guides/reporting-insights/data-export/database-reference-2026-07-13|2026-07-13 snapshot - complete table and column reference]]
