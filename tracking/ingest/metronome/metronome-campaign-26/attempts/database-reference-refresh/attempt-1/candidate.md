---
title: "Metronome Data Export Database Reference"
type: source
date_ingested: 2026-08-28
canonical_url: "https://docs.metronome.com/guides/reporting-insights/data-export/database-reference"
original_format: webpage
raw_files:
  - "metronome/guides/reporting-insights/data-export/database-reference-2026-08-28.md"
  - "metronome/guides/reporting-insights/data-export/database-reference-2026-07-13.md"
tags: [metronome, data-export, warehouse-schema, invoices, contracts]
---

## Overview

This reference routes warehouse consumers across Metronome's exported schema. Use it to choose the table family and row grain, then follow the complete retained raw page for exact columns, nested JSON types, enumerations, and field-level caveats.

## Key takeaways

- Destination columns may all appear nullable because of the export methodology; generated warehouse nullability does not establish business optionality.
- Exported identity and row grain vary by table: object IDs, metadata IDs, snapshot IDs or timestamps, versions, effective-time bounds, and watermarks can all matter to correct selection.
- Finalized invoices, daily draft invoice snapshots, finalized breakdowns, and daily month-to-date draft breakdown snapshots are distinct reporting grains.
- Contract exports span snapshot-style object tables and effective or versioned records; `contracts_commits` is narrower than the broader balance domain.
- The 2026-08-28 snapshot adds material fields and scope signals without changing this page's role as a router: consult the current raw schema before production queries.

## Table-family and row-grain map

| Family | Navigate here for | Grain or selection signal to verify in raw |
| --- | --- | --- |
| Core entities | Billable metrics, credit types, deduplicated raw events, and customers | Stable entity or event identity; customer aliases can join to events |
| Finalized invoicing | `invoice` and `line_item` | `FINALIZED` or `VOID` invoices and their line items; these records are documented as no longer changing |
| Draft invoicing | `draft_invoice` and `draft_line_item` | Daily point-in-time rows keyed by invoice or line-item identity plus snapshot time; `DRAFT_INCOMPLETE` can lack totals and line items until a later snapshot |
| Invoice breakdowns | Finalized and draft invoice/line-item breakdown pairs | Finalized rows export incrementally; draft snapshots contain month-to-date breakdown periods and use breakdown, snapshot, and watermark fields |
| Contract state and balances | Contracts, commits, balances, recurring configurations, filters, thresholds, subscriptions, charges, and hierarchy | Snapshot IDs, object IDs, effective bounds, versions, and nested schedule or ledger identity are table-specific |
| Contract changes and pricing | Overrides, transitions, edits, amendments, rate cards, entries, and product-list-item versions | Transition or amendment identity, effective intervals, versions, and snapshots must be selected deliberately |
| Other domains | Packages, payments, alerts/history, and client-specific metadata | Follow each table's object identity and scope notes; the Payments section's Private Beta statement is scoped to Metronome invoicing |

This map is not a substitute for the complete table list, column catalog, or nested type definitions.

## Selection and completeness boundaries

### Nullability and schema shape

All exported columns may appear nullable in the destination schema. Several fields are also explicitly deprecated and expected to be null, so consumers should use the table documentation rather than generated types to decide whether a value is optional, deprecated, or temporarily absent. The page is a rendered warehouse schema reference rather than an OpenAPI object contract and does not document unknown-column runtime behavior as a closed-schema guarantee.

### Invoice snapshots and completeness

Draft invoice rows are calculated once per day through the billing period: `updated_at` is calculation time while `snapshot_time` aligns to start of day UTC. A `DRAFT_INCOMPLETE` row signals that an invoice exists but has not been fully computed; a later snapshot is expected to hydrate it. Draft breakdown snapshots contain all month-to-date periods through their snapshot so backdated usage and mid-period pricing changes can be reflected in the latest snapshot. Optional zero-value or zero-quantity breakdown filtering is enabled through the Metronome support portal.

### Contract identity, scope, and time selection

Contract tables mix snapshot IDs with object IDs, nested JSON schedules and ledgers, effective ranges, and explicit versions. The two usage-filter exports publish different time-selection recipes, so consumers should follow the exact table-specific instructions rather than apply one generic latest-row rule. `contracts_commits` contains only contract-level commits and excludes customer-level commits or credits and contract-level credits; `contracts_balances` covers the broader credit-or-commit balance domain.

## 2026-08-28 schema-change watch

- `contracts_commits` and `contracts_balances` now document `cost_basis` as the ratio of amount paid for a commit to credit granted. The reference does not define denominator-zero behavior or make an accounting-policy claim.
- `contracts_prepaid_balance_threshold_configurations` now exposes created-commit duration value and unit, rollover fraction, and rate type; exact defaults and allowed values remain in the raw field catalog.
- `alert.customer_id` is now documented: a null value means the configured alert applies to all customers. This is export-row scope, not a delivery, evaluation, or webhook guarantee.
- `contracts_transitions.type` is now described with renewal as an example rather than as an exhaustive two-value list. Do not infer a closed transition enum from the current reference.

## Raw-detail coverage map

Use the 2026-08-28 raw page for the complete table and column catalog; precise ID, environment, snapshot, version, effective-time, watermark, and update fields; nested access, invoice, recurring, subscription, schedule, rate, specifier, ledger, gateway, and metadata types; deprecated-field notes; status and enum literals; invoice-breakdown filter choices; and every table-specific nullability or scope caveat. The 2026-07-13 raw page remains available for schema-delta and historical wording checks.

## Change history

- 2026-08-28: Refreshed from the new collection snapshot; preserved prior raw history, updated the invoice-breakdown filter contact route, added schema-change navigation for commit/balance cost basis, prepaid-threshold commit fields, and alert customer scope, and removed any implication that transition types form a closed two-value set.
- 2026-07-14: Initial ingest from the 2026-07-13 collection snapshot; strengthened schema-navigation, row-grain, nullability, and beta-scope language.

## Related

- Company: [[metronome]]
- Primary concept: [[metronome-reporting-and-analytics]]
- Related domains: [[metronome-event-ingestion]], [[metronome-invoicing]], [[metronome-customers-and-contracts]], [[metronome-credits-and-commits]], [[metronome-products-and-rate-cards]], [[metronome-alerts-and-notifications]]

## Raw Sources

- [[raw/metronome/guides/reporting-insights/data-export/database-reference-2026-08-28|2026-08-28 snapshot - complete current table, column, and nested-type reference]]
- [[raw/metronome/guides/reporting-insights/data-export/database-reference-2026-07-13|2026-07-13 snapshot - prior complete table and column reference]]
