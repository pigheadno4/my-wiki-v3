---
title: "Get commit and usage analytics"
type: source
date_ingested: 2026-08-19
original_format: webpage
canonical_url: "https://docs.metronome.com/guides/reporting-insights/gtm-reporting/get-commit-and-usage-analytics.md"
raw_files:
  - "metronome/guides/reporting-insights/gtm-reporting/get-commit-and-usage-analytics-2026-07-13.md"
tags: [metronome, data-export, commit-analytics, usage-analytics, customer-success]
---

## Overview

This guide describes a warehouse-and-BI workflow for customer-level commit burn dashboards used by go-to-market teams. It combines expected pacing derived from commit access schedules with actual consumption from finalized and current-period invoice data, then proposes operational signals for renewal, adoption, and implementation outreach.

The page is a modeling recipe rather than an executable query or warehouse-schema contract. Its generalized SQL mixes identifiers from unresolved export table families, so implementers must reconcile every selected field, join, row grain, snapshot rule, and delivery rule against the current Data Export database reference before production use.

## Key takeaways

- Data Export is a paid prerequisite. The dedicated export documentation—not this guide's broad daily wording—defines each table's transfer cadence, average freshness, snapshot behavior, and destination delivery semantics.
- Expected burn spreads an access-schedule amount over its service-period days; intended actual burn comes from invoice rows attributed to a commit. The published examples do not resolve whether their actual-burn fields belong to base invoice tables or invoice-breakdown tables.
- Finalized `invoice` and `line_item` are incremental, with 2-hour transfer frequency and 4-hour average freshness. `contracts_balances` and the base `draft_invoice` and `draft_line_item` tables are 24-hour/24-hour snapshots.
- Base draft invoices produce one point-in-time invoice snapshot per day with `snapshot_time` aligned to start-of-day UTC; draft breakdown snapshots instead contain month-to-date rows. Selecting and summing more than one relevant snapshot can overstate burn.
- Object-storage duplication is a separate axis: append-only, at-least-once delivery can repeat primary keys after updates or retries, requiring latest-row resolution even after the intended table family and snapshot have been selected.
- A null commit ID means an amount cannot be attributed to a particular commit. This guide calls every null on-demand usage, but the existing revenue-reporting source says null can mean on-demand or overage and requires client-defined metadata to distinguish them.
- The burn-rate bands and suggested outreach actions are merchant playbook examples, not Metronome-enforced thresholds or universal customer-health definitions.

## Export prerequisites and table semantics

The guide calls for at least seven days of usage data, an Admin or Analyst role, contract-and-commit visibility, Data Export configuration access, and a BI tool. It identifies Data Export as paid and asks users to enable customers, contract-related models, finalized invoice data, and draft invoice data.

For this model, the dedicated export sources establish different timing and grains. Finalized `invoice` and `line_item` are incremental exports listed at 2-hour transfer frequency and 4-hour average freshness. `contracts_balances`, base `draft_invoice`, and base `draft_line_item` are snapshots listed at 24-hour transfer frequency and 24-hour average freshness. Base draft invoice data contains one point-in-time snapshot per invoice per day, with `snapshot_time` at start-of-day UTC; draft breakdown snapshots instead carry month-to-date rows through each snapshot.

Those snapshot rules govern which business-state row or period is selected. Separately, object-storage destinations are append-only and at-least-once, so updates or transfer retries can repeat a primary key and require latest-row resolution. A correct burn model must handle both axes: first select the intended table family and snapshot, then resolve delivery duplicates. Summing several daily or month-to-date draft snapshots, or summing repeated object-storage rows, can count the same consumption more than once.

## Expected pacing

The expected curve parses schedule items from `contracts_balances`, converts the sample monetary amounts from cents to currency units, calculates an inclusive schedule duration, and divides each schedule amount by that duration to obtain a daily expected rate.

Even this first sample needs repair before execution: it selects through `sch` after naming the relation `acs`, and it alternates between `contracts_balances_table` and `balances_table`. More importantly, the later actual-burn examples cross table-family boundaries, so correcting aliases alone would not establish the intended schema or grain.

## Unresolved actual-burn table families

### Finalized history

The finalized example is introduced as an `invoice` plus `line_item` query and joins those placeholder tables. It then filters `li.line_item_type`, a field the dedicated database reference documents on breakdown line items rather than the base `line_item` family. The guide does not decide whether the intended source is base finalized invoice rows or finalized invoice-breakdown rows. That choice changes available fields and row grain, so an implementer must verify the current reference and choose one coherent family before writing joins or aggregations.

### Current-period draft data

The draft example is introduced as `draft_invoice` plus `draft_line_item`, but it selects `breakdown_start_timestamp`, `breakdown_end_timestamp`, `commit_segment_id`, and joins through `invoice_breakdown_id`. The dedicated reference associates those fields with the `breakdowns_draft_invoices` and `breakdowns_draft_line_items` family. Again, the source does not establish whether base draft snapshots or month-to-date draft breakdown snapshots are intended.

Do not combine the published placeholders as if they formed one documented schema. Reconcile the current field catalog, select either the appropriate base or breakdown grain for each part of the model, and apply that family's snapshot rule before aggregating.

## Combined model and GTM use

At the modeling level, the guide instructs readers to connect commit-attributed consumption to an access-schedule balance, create a date spine over the relevant service period, and cumulatively sum line-item totals. A forecast curve is deliberately left to merchant-selected heuristics. Usage without a commit ID is excluded because it cannot be tied to a particular commitment.

Comparing expected and actual curves can flag customers consuming faster, slower, or approximately on pace. The page gives examples such as 80–110% as on track, above 150% before month three as concerning, 300% in week one prompting an immediate check-in, and below 50% after 60 days prompting adoption outreach. These are illustrative GTM actions, not billing limits or guaranteed predictors.

## Data and documentation cautions

> [!warning] Contradiction
> This guide maps `commit_id IS NULL` to on-demand usage. The existing revenue-reporting source says a null line-item commit ID can mean either on-demand usage or overage and requires client-defined contract or commit metadata to distinguish them. Preserve only the non-attribution conclusion until classification is verified.

> [!warning] Unresolved table family and grain
> The finalized query names base invoice tables while filtering a breakdown-line-item field. The draft query names base draft tables while selecting breakdown timestamps, a commit segment, and an invoice-breakdown join key. The guide does not establish which family is intended. Do not infer the answer or aggregate across both families; reconcile the current database reference before choosing joins and grain.

> [!warning] Two independent overcount risks
> Draft snapshot selection and object-storage delivery deduplication solve different problems. Base draft rows are daily point-in-time invoice snapshots; draft breakdown rows are month-to-date snapshots; object storage can separately repeat primary keys through updates or retries. Summing multiple snapshots or unresolved delivery duplicates can overstate commit burn.

Backdated usage can temporarily spike the curve, price changes can distort burn calculations, and recent configuration changes should be checked before escalating anomalies. The guide advises waiting 24 hours before escalating a backdated-usage spike. It does not define calculation ownership, time zones, currency aggregation, correction policy, retention, BI access control, or forecast validation.

## Related

- Company: [[metronome]]
- Concepts: [[metronome-reporting-and-analytics]], [[metronome-credits-and-commits]]
- Related sources: [[source-metronome-guides-reporting-insights-data-export-overview]], [[source-metronome-guides-reporting-insights-data-export-database-reference]], [[source-metronome-guides-reporting-insights-financial-reporting-revenue-recognition]]

## Raw Sources

- [[raw/metronome/guides/reporting-insights/gtm-reporting/get-commit-and-usage-analytics-2026-07-13|2026-07-13 snapshot — commit pacing, unresolved invoice table families, burn aggregation, and GTM playbook guidance]]
