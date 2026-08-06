---
title: "Metronome Create SQL Billable Metrics"
type: source
date_ingested: 2026-08-01
original_format: webpage
canonical_url: "https://docs.metronome.com/guides/implement-metronome/core-concepts/billable-metrics-sql-editor"
raw_files:
  - "metronome/guides/implement-metronome/core-concepts/billable-metrics-sql-editor-2026-07-13.md"
tags: [metronome, billable-metrics, sql, aggregation, usage-based-billing]
---

## Overview

This guide defines the SQL Editor query surface for Metronome billable metrics, including event-field access, result-column selection, supported functions, and a daily-storage example. It also explains product-level `hour` versus `service period` breakdown granularity and illustrates how quantities accrue when one SQL metric is scheduled to replace another during a billing period.

## Key takeaways

- SQL billable metrics query Metronome's `events` table. Queries filter and aggregate usage, while Metronome supplies the individual-customer and billing-period filtering.
- For a multi-column result, Metronome uses a column named `value` as the metric quantity when present and otherwise uses the first returned column. Remaining columns can become downstream group keys; unused extra columns are summed over to produce one quantity.
- The documented SQL surface includes eight aggregation forms, arithmetic and comparison operators, conditional and membership logic, `DATE_TRUNC` to hour or day, and `CAST`. The page does not identify the SQL dialect or define type, null, precision, tie, or error semantics.
- SQL breakdown granularity is selected on the product. The default `hour` mode incurs costs through the period as usage is ingested; `service period` places the full period quantity and cost in the final time window.
- A product's SQL metric can be changed effective during a billing period. The worked two-SQL-metric average example preserves the old metric's value at the swap and then incurs only increases in the documented combined value.

## Query inputs and output selection

Queries read `event_type`, `timestamp`, and event properties through `properties.field_name` from the `events` table. Metronome says the query author does not need to add customer or billing-period filtering, but the page does not expose that injected predicate, its boundary inclusivity, timezone, or behavior for late, corrected, or backdated events.

For a result with more than one column, `value` is preferred as the quantity column; if it is absent, the first returned column is used. Therefore this page does not make a `value` alias mandatory. Other returned columns can serve as presentation or pricing group keys, and extra columns not selected for either purpose are summed over to create a single metric quantity. The page does not define duplicate column names, nonnumeric quantity handling, output-row or group-cardinality limits, or whether column ordering remains stable through validation.

## Supported SQL surface

The documented aggregations are `COUNT`, `SUM`, `MAX`, `MIN`, `AVG`, `EARLIEST`, `LATEST`, and `COUNT DISTINCT`; `EARLIEST` and `LATEST` select by `timestamp`. Arithmetic supports `+`, `-`, `*`, and `/`; the comparison list renders `=`, `!=`, `>`, `<`, `≥`, and `≤`. Scalar math includes `LEAST`, `GREATEST`, `ROUND`, `CEIL`, and `FLOOR`. Logic includes `AND`, `OR`, `NOT`, `CASE WHEN`, `IS NULL`, `IS NOT NULL`, `IN`, and `NOT IN`. `DATE_TRUNC` is documented only for truncating `timestamp` to `hour` or `day`, and `CAST` is listed without supported target types.

The neighboring create-metrics guide shows distinct counting as `count(distinct …)`, while this page labels the supported aggregation `COUNT DISTINCT`. The Basic Filters guide's instruction to use a SQL metric for `UNIQUE` is directionally consistent with distinct-count support here, but these pages do not define `UNIQUE` as a SQL function or reconcile it with the create API's separate `UNIQUE` aggregation enum. The rendered `≥` and `≤` glyphs also should not be assumed to prove that literal Unicode operators, ASCII `>=` and `<=`, or both are accepted.

## Daily-storage example

The example filters `storage_heartbeat` events, groups by truncated day, `user_id`, and `region`, takes the maximum `storage_used` within each observed day and group, and divides the sum of those daily maxima by the sum of one `num_days` marker per group. The output aliases the calculation to `value`, returns `user_id` for invoice presentation, and returns `region` for dimensional pricing. It therefore computes an average of per-observed-day maxima, not a general average of every storage reading. The page does not specify whether days without events enter the denominator, how division precision or rounding is handled, or what happens when values are absent or nonnumeric. It recommends previewing against existing usage before saving.

## Breakdown granularity

A product backed by a SQL metric defaults to `hour` granularity. In the guide's three-event `SUM` example, values 5, 10, and 15 arrive before a January 15 rate change, so each is priced at the earlier $10 rate; a day-2-only credit or commit applies only to the day-2 quantity and spend, and invoice breakdowns show each day's quantity and cost separately.

With `service period` granularity, the example's full quantity of 30 is incurred in the billing period's final time window and uses the final $20 price. A credit or commit must cover the last instant of the period to apply, and invoice breakdowns place the cost in that last window. These are documented example outcomes; the page does not define exact time-window boundaries, final-price selection under overlapping schedules, late-event recalculation, invoice-finalization effects, or how non-additive aggregations behave in every case.

## Scheduled metric transitions

The guide says SQL billable metrics are swappable on products and a swap may take effect at any point in a billing period. Its example changes from SQL Metric A, averaging `value` on `average_metric_v1` events, to SQL Metric B, averaging `value_new` on `average_metric_v2` events, effective March 15.

Before the swap, Metric A's cumulative average produces an incurred quantity of 4 on March 1 and then 1 more on March 2 when the average rises to 5. After the swap, the combined value is defined as B through the current day, plus A through the swap day, minus B through the swap day. In the example, B's pre-swap value is zero; the reported March 15 increment of 10 corresponds to a combined value of 15 after 5 was already incurred, and B's average rising from 10 to 11 on March 16 produces one additional unit.

The worked transition has two SQL metrics and does not define exact effective-time inclusivity, timezones, transitions where only one side is SQL, interactions with `service period` granularity, falling combined values or negative adjustments, late-event corrections, finalized-invoice behavior, or subsequent billing periods. The heading's broader "to or from a SQL billable metric" wording should not be used alone to infer every streaming-to-SQL or SQL-to-streaming transition contract.

## Consistency and documentation boundaries

The Basic Filters and create-metrics sources direct distinct counts to SQL, which is consistent with this page’s `COUNT DISTINCT` support. They also reserve `COUNT`, `SUM`, `MAX`, and `LATEST` as the documented streaming aggregation set; this page’s broader SQL function list does not contradict that editor boundary.

> [!warning] Contradiction
> The existing shared billable-metrics concept currently leaves SQL output rules undefined. The earlier create-metrics raw guide and its source summary call `value` a required SQL output column, while this SQL Editor raw page documents first-column fallback when a multi-column result has no `value` column. For the documented multi-column case, treat `value` as preferred rather than universally mandatory. This page does not state how a one-column result is selected, and it does not define runtime behavior for missing, duplicate, or nonnumeric quantity columns. Add a reciprocal contradiction warning to the earlier create-metrics source summary so both source pages expose the conflict. No other direct contradiction with the two adjacent source summaries was found.

## Related

- Company: [[metronome]]
- Concepts: [[metronome-billable-metrics]], [[metronome-products-and-rate-cards]], [[metronome-credits-and-commits]], [[metronome-invoicing]]
- Related sources: [[source-metronome-guides-implement-metronome-core-concepts-billable-metrics-basic-filters]], [[source-metronome-guides-implement-metronome-core-concepts-create-billable-metrics]]

## Raw Sources

- [[raw/metronome/guides/implement-metronome/core-concepts/billable-metrics-sql-editor-2026-07-13|2026-07-13 snapshot — SQL query surface, output selection, aggregation, product granularity, and scheduled metric transitions]]
