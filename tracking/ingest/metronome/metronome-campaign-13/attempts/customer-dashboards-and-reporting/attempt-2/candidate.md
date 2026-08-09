---
title: "Build API-powered customer dashboards"
type: source
review_level: independent
date_ingested: 2026-08-04
original_format: webpage
canonical_url: "https://docs.metronome.com/guides/customers-billing/optimize-customer-experience/customer-dashboards-and-reporting.md"
raw_files:
  - "metronome/guides/customers-billing/optimize-customer-experience/customer-dashboards-and-reporting-2026-07-13.md"
tags: [metronome, customer-dashboards, usage-reporting, invoice-breakdowns, embeddable-dashboards]
---

## Overview

This guide shows how to build API-powered customer dashboards that expose Metronome usage, spend, and credit or commit balances inside a product. It recommends a backend-service pattern for Metronome API calls, gives usage, balance, and invoice-breakdown examples, and describes embeddable invoice, usage, and commits-and-credits dashboards.

## Key takeaways

- Metronome says its APIs and data export features can provide end-user visibility into usage and associated costs; embeddable dashboards show customer usage and invoices.
- All Metronome API calls used to return data to an end-user frontend should originate in the integrator's backend, using a securely stored token; the guide says never expose API tokens to users or frontend clients.
- The usage example calls the usage endpoint for the `CPU hours` billable metric over October 2024, grouped by region in daily windows, then prepares stacked-bar-chart data.
- `/listBalances` with `include_balance: true` exposes the currently usable balance for each credit or commit and excludes upcoming not-yet-started segments; `/getNetBalance` is offered for a single running balance.
- Invoice breakdowns provide hourly or daily buckets per invoice line item; credit or commit deductions appear as separate line items. Embeddable dashboards cover invoices, current-contract usage (30/60/90 days), and commits/credits.

## Details

### Backend integration

The guide requires Metronome APIs to be called by a backend service that returns data to the frontend. It says to authenticate with a securely stored token available to that backend and not expose tokens to users or frontend clients; its diagram is `Your Frontend App <--> Your Backend Service <--> Metronome APIs`.

### Usage visibility

The guide says Metronome can slice and filter usage using event properties. Its example uses the usage endpoint for the `CPU hours` billable metric from 2024-10-01 through 2024-11-01, with `window_size` set to `day` and `group_by.key` set to `region`. The response example carries `value`, `group_key`, `group_value`, `starting_on`, `ending_before`, and `next_page`. The supplied backend pseudocode organizes entries by date and region and builds stacked-bar-chart ranges; the frontend pseudocode fetches chart data from a merchant backend.

### Commitment and balance tracking

The guide's `/listBalances` example requests `include_ledgers`, `include_balance`, `starting_at`, and `include_contract_balances`. With `include_balance: true`, each credit or commit's `balance` reflects the amount available to use now, and upcoming segments that have not started are not included. The worked scenario says a $100 prepaid commit and a $5 reward credit leave the reward credit at $0, the prepaid commit at $20, and the overall balance at $20 after the stated September and October spend. Its pseudocode derives each grant's `granted` amount from access-schedule items, computes `used = granted - balance`, and totals granted, used, and remaining.

For a high-level balance display, the guide points to `/getNetBalance` and says the call returns a real-time total without parsing individual balance details.

### Spend visibility

The invoice breakdown endpoint is described as returning one record for each line item on a customer's invoice in hourly or daily buckets. The guide's example requests daily October 2024 breakdowns and groups the line items by `presentation_group_values.region`. If credits or commits are consumed, the deductions appear as separate line items. The supplied pseudocode aggregates each line item by breakdown date and region and divides `total` by 100 with a comment to convert cents to dollars before charting.

### Embeddable dashboards

Metronome's embeddable options include:

- Invoice dashboard: current and historical draft, finalized, and voided invoices up to 90 days old; clients using Metronome invoicing can manually attempt payment on outstanding invoices.
- Usage dashboard: usage metrics attached to a customer's current contract for the past 30, 60, or 90 days.
- Commits and credits dashboard: current and historical grants, remaining and historical balances, grant and deduction history, access schedules, and expiration dates.

The guide says to create an API token, call `/dashboards/getEmbeddableUrl` with `customer_id` and the selected dashboard, and render the returned URL in an iframe. `color_overrides` can change the palette; examples name `gray_dark` for standard text and `primary_medium` for selected text. The invoice dashboard's optional `dashboard_options` key `show_zero_usage_line_items` defaults to `false`.

## Related
- Company: [[metronome]]
- Concepts: [[metronome-reporting-and-analytics]], [[metronome-credits-and-commits]], [[metronome-invoicing]], [[metronome-security-principles]], [[metronome-customers-and-contracts]]

## Raw Sources
- [[raw/metronome/guides/customers-billing/optimize-customer-experience/customer-dashboards-and-reporting-2026-07-13|2026-07-13 snapshot — API-powered customer dashboards, usage, balances, spend, and embeddable views]]
