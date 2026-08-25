---
title: "Metronome Non-Monotonically Increasing Metrics"
type: source
date_ingested: 2026-08-25
original_format: webpage
canonical_url: "https://docs.metronome.com/guides/implement-metronome/core-concepts/non-monotonically-increasing-metrics.md"
raw_files:
  - "metronome/guides/implement-metronome/core-concepts/non-monotonically-increasing-metrics-2026-07-13.md"
tags: [metronome, billable-metrics, latest-aggregation, usage-based-billing, credits, rate-changes]
---

## Overview

This guide documents how Metronome bills metrics whose reported value can rise or fall, such as connected-device or storage-in-use measurements. These metrics typically use `latest`; for billing, Metronome derives incremental changes between consecutive reporting windows, while its usage-query surface reports absolute latest values. The guide is useful for reasoning about rating, commit and credit coverage, rate changes, invoice breakdowns, and reconciliation, but it does not replace the linked metric-creation or endpoint schemas.

## Metric and billing semantics

A non-monotonically increasing metric can move up or down during a billing period and typically uses `latest`, which captures the most recently reported value at each point in time. For billing, Metronome uses the change between consecutive reporting windows rather than the absolute reported value. In the worked sequence `7 -> 9 -> 10 -> 5`, the billed quantities are `7`, `2`, `1`, and `-5`; a decrease therefore creates a negative billed quantity and a credit for that period.

The page does not define the exact reporting-window boundaries, timezone, missing-window behavior, first-value baseline across billing periods, treatment of late or corrected values, precision, rounding, or invoice-finalization effects. Its examples establish the documented outcomes shown, not a complete event, metric-creation, invoice-lifecycle, or accounting contract.

## Commits, credits, and effective dates

Commits and credits cover only incremental usage within their effective date range, not the absolute latest value. In the guide's example, a commit beginning on day 2 covers the increment from `7` to `9`—quantity `2`—but not day 1's quantity `7`. The same effective-window rule is illustrated for a free credit: only incremental units accrued inside the credit's date range are covered, and the remainder is billed at the standard rate.

## Rate changes and negative quantities

A mid-period rate applies to incremental usage in its own effective window. An increase from `7` to `9` after a move from $3 to $4 per unit bills only the increment of `2` at $4. If the reported value falls after the rate change, the negative increment is priced at the current effective rate: the guide's decrease of `10` at the new $4 rate produces a `-$40` charge line. It warns that a higher current rate can make the per-unit credit larger than the earlier per-unit charge.

## Credit application and negative totals

When credits, a rate change, and a later usage decrease coexist, Metronome evaluates charge lines independently in chronological order and applies credit to positive lines as encountered; it does not look ahead to later negative charges or first cap credit consumption against the net invoice. In the worked example, a $100 full-period credit is consumed against an initial $120 positive charge, after which a `-$40` line yields a final total due of `-$20`. The guide does not explain whether a negative total is carried forward, refunded, offset, exported, delivered to a billing provider, or treated for tax, payment, settlement, reconciliation, or accounting.

> [!warning] Intra-page recommendation conflict
> The worked example explicitly says its $100 credit covers the full billing period and still produces a `-$20` total because credit is consumed before the later negative charge. The later tip nevertheless recommends full-period commit and credit coverage and says that configuration applies credits holistically across all line items and avoids unexpected negative totals. The page does not reconcile these statements. Preserve both as documented and verify operational behavior before relying on the recommendation.

## Invoice-breakdown and usage-query distinction

For this guide's `latest` metrics, the invoice-breakdowns endpoint returns incremental quantity and associated cost for each time window, including negative quantities and negative costs when usage decreases. By contrast, the usage endpoints return the absolute latest reported value within each requested window; with no breakdown, the example returns the latest value across the full queried period. This difference matters when reconciling usage views with billed quantities.

This guide documents the distinction, not the endpoints' exact authentication, parameters, response envelopes, pagination, ordering, freshness, consistency, or error behavior. Those contracts require the dedicated API references.

## Related

- Company: [[metronome]]
- Concepts: [[metronome-billable-metrics]], [[metronome-usage-based-billing]], [[metronome-products-and-rate-cards]], [[metronome-credits-and-commits]], [[metronome-invoicing]], [[metronome-reporting-and-analytics]]
- Metric design authority: [[source-metronome-guides-implement-metronome-core-concepts-create-billable-metrics]]

## Related raw API references

- [[raw/metronome/api-reference/invoices/list-invoice-breakdowns-2026-07-13|Invoice breakdowns API reference]] — navigation-only; not used as factual evidence for this source body
- [[raw/metronome/api-reference/usage/get-usage-data-with-paginated-groupings-2026-07-13|Usage data with paginated groupings API reference]] — navigation-only; not used as factual evidence for this source body

## Raw Sources

- [[raw/metronome/guides/implement-metronome/core-concepts/non-monotonically-increasing-metrics-2026-07-13|2026-07-13 snapshot - non-monotonic metric billing, effective-date, rate-change, credit, and query-surface behavior]]
