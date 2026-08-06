---
title: "Metronome In-App Reports and Dashboards"
type: source
date_ingested: 2026-08-01
original_format: webpage
canonical_url: "https://docs.metronome.com/guides/reporting-insights/in-app-reporting"
raw_files:
  - "metronome/guides/reporting-insights/in-app-reporting-2026-07-13.md"
tags: [metronome, reporting, analytics, dashboards, arr]
---

## Overview

This guide documents two reporting surfaces inside the Metronome app: downloadable CSV reports and beta dashboards. It covers enablement, generation timing, the standard-report catalog, the paid custom-report workflow, and the definitions, filters, and caveats of the Committed & Run Rate ARR Dashboard. These in-app surfaces are distinct from Data Export delivery and from API-powered dashboards in a merchant application.

## Key takeaways

- Custom and standard reports require enablement through a Metronome Solutions Architect. They run from the app's Reports tab and produce downloadable CSV files; most finish in one to two hours, larger reports can take up to ten hours, and report data updates once daily.
- Standard reports cover customers, contracts, commits and credits, finalized invoices and line items, expired-commit ledger entries, true-up invoices, and monthly revenue by product and category. The user supplies date filters, triggers generation, and receives an email link after completion.
- Custom reports are paid and use the same data tables available through Data Export. Requirements and sample data are reviewed with a Solutions Architect before approval, after which a report can be triggered in the app or scheduled via cron.
- In-app dashboards are beta and require account-level enablement by a Metronome representative. The documented dashboard set includes Basic Revenue Overview, Committed & Run Rate ARR, and a Filterable Customer List.
- The ARR dashboard defines committed and run-rate revenue, ARR and customer movement, GRR, NRR, and configurable filters. Its calculations use only contract data and finalized invoices, prorate invoices by day, and do not support non-USD fiat currencies.

## Access, generation, and delivery

Metronome directs customers to a Solutions Architect to enable either standard or custom reports. A user then visits the Reports tab, selects a report, supplies filtering dates, and chooses **Generate Report**. When generation completes, Metronome sends an email confirmation whose link returns the user to the app to download the CSV.

The documented processing window is normally one to two hours and can reach ten hours for larger reports. The underlying report data updates once per day, so a generated report can be stale depending on update timing; the guide says the user may need to trigger it again. The page does not define a freshness timestamp, cutoff time, time zone, row limit, file-size limit, retention period, retry policy, failed-job behavior, download-link lifetime, email-delivery guarantee, or an API for report execution or retrieval.

## Standard report catalog

| Report | Documented scope |
| --- | --- |
| Customers by created date | All customers in the account, intended for customer-growth tracking. |
| Contracts by created date | All contracts across customers, intended for contract-volume and sales-activity analysis. |
| Commits and credits by created date | All prepaid commits and credits issued to customers, intended for commitment-sales and credit-grant tracking. |
| Invoices by status and effective date | All finalized invoices and line items plus the effective billing period, intended for accounts receivable and revenue-recognition work. |
| Commit expiration ledger entries by month | Ledger entries for commits that expired in each month, intended for unused-balance and breakage-revenue tracking. |
| True up invoices by effective date | All true-up invoices, intended for end-of-period commitment-reconciliation charge tracking. |
| Monthly revenue by product name and revenue category | Monthly product/category totals, with on-demand, commit drawdown, and overage given as example categories. |

These are predefined reports rather than a schema for every returned CSV. The page does not document columns, row grain, ordering, status or date-filter semantics, currency treatment for the standard revenue report, or whether the list is exhaustive for every account.

## Custom reports

Custom reporting is a paid feature. A customer requests a report from a Solutions Architect, shares detailed requirements such as month-end close or customer cohorting, reviews sample data, approves the result, and chooses whether to trigger it from the app or schedule it via cron. The reporting engine can query the same data tables exposed through [[source-metronome-guides-reporting-insights-data-export-overview|Data Export]].

That table-access statement does not establish that every table is available to every custom report, that custom-report rows have the same delivery cadence or freshness as an export destination, or that Data Export's append-only and at-least-once object-storage semantics apply to a CSV. The source also gives no custom-report price, plan eligibility, requirement format, lead time, revision process, ownership of the cron schedule, scheduling syntax, access-control model, or service-level commitment.

## In-app dashboard availability

In-app dashboards are beta and must be enabled for the account by a Metronome representative. The Basic Revenue Overview summarizes monthly invoiced amounts, usage and subscription revenue, commits and credits, and customer-level consumption. The Committed & Run Rate ARR Dashboard focuses on ARR, NRR, GRR, and logo movement for consumption-based businesses. The Filterable Customer List supports searching and sorting customers by billing provider, spend, and other attributes.

The guide says these dashboards let clients monitor metrics and explore customer detail in real time, but it does not define query endpoints, refresh cadence, event-to-dashboard latency, caching, permissions, export behavior, historical retention, data correction, or availability guarantees. The daily-data warning is stated for generated reports, not explicitly for the dashboards. Likewise, API-powered end-user dashboards documented elsewhere are a separate merchant-built surface and should not be treated as this Metronome-app beta.

## Committed and run-rate ARR

### Committed ARR

Committed ARR represents contractually committed revenue from usage commitments and scheduled charges and is derived from `scheduled_charges` and `balances`. For balance schedules, Metronome unnests individual commit or credit periods and annualizes each schedule item as `(amount / duration_days) × 365`; CPU-denominated commits are first converted to dollars through the associated rate-card conversion. Scheduled-charge items are unnested and summed per charge over `starting_at` to `ending_before`, then annualized over that duration.

### Run Rate ARR

Run Rate ARR estimates annualized usage and subscription revenue over a configurable trailing window. The guide's three-month example is `average monthly revenue across the last 3 months × 12`. When a customer has less than the selected number of months, the calculation uses the available months. It continues to compute run-rate ARR for churned customers: if the latest month has `$0` usage, the moving average still includes the prior months in the window.

The Run Rate tab hardcodes a completed-month filter (`month < current month start`), defaults **Average last X months** to `3`, and shares a default 12-month lookback with the Committed ARR tab.

## Movement and retention definitions

All movement metrics compare a current period with a configurable base period X months earlier:

- **New ARR** is current ARR from a customer whose base ARR was zero or whose record did not exist, when current ARR is greater than zero.
- **Expansion ARR** is the positive difference between current and base ARR for an existing customer whose ARR grew.
- **Contraction ARR** is the positive difference between base and current ARR when current ARR remains greater than zero.
- **Churned ARR** is the full base-period ARR for a customer whose current ARR is zero.
- **Net ARR Change** is New ARR plus Expansion ARR minus Contraction ARR minus Churned ARR.

GRR is `retained_arr / starting_arr`, where each customer's retained ARR is `min(current ARR, base ARR)`; it excludes expansion. NRR is `ending_arr_from_base_cohort / starting_arr`, where the numerator is current ARR for customers present in the base period; it includes expansion. The page interprets GRR below 100% as contraction or churn, NRR above 100% as expansion exceeding contraction and churn, and NRR below 100% as the reverse.

Logo movement applies the same current-versus-base framing to customer counts: new, expanding, retained, contracting, churned, and active customers are classified by whether ARR was absent, zero, unchanged, increased, decreased but positive, or fell to zero. Active customers are those with current-period ARR greater than zero regardless of base-period status.

## Filters and calculation caveats

The Committed ARR tab applies filters to combined scheduled-charge and commit data. Defaults exclude commit type `credit`, exclude commits or charges shorter than 30 days, and use a 12-month lookback. Users can also exclude customers or contracts, keep only recurring charges, keep only invoiced commits, and select rate cards. Rows without contracts or commit types remain preserved under the relevant exclusion filters as documented.

The Run Rate tab filters usage-based revenue. It supports customer, product, product-type, revenue-recognition-type, non-credit-commit, and rate-card filters; `credit_drawdown` is excluded by default. Its trailing-average default is three completed months, and its shared movement and retention lookback defaults to twelve months.

For this ARR dashboard, only contract data and finalized invoices are used. Invoices spanning months are prorated by day, and non-USD fiat currencies are unsupported. The page does not define treatment of exchange rates, non-fiat units, taxes, discounts, refunds, credits beyond the named filters, late corrections, voids, time zones, partial days, rounding, or whether its revenue and retention measures conform to GAAP, IFRS, ASC 606, or a customer's own accounting policy.

## Contradictions and unknowns

No direct contradiction was found with the existing reporting concept when the surfaces remain separated. Data Export has destination-specific transfer, freshness, snapshot, and at-least-once rules; this page documents generated CSVs and beta app dashboards. The report section's once-daily data update does not establish dashboard freshness, while the dashboard's “real time” wording supplies no measurable latency or guarantee. Similarly, “same data tables” for custom reports establishes query scope but not identical availability, row grain, delivery semantics, or freshness.

The guide does not document which app roles can view, trigger, schedule, or download reports and dashboards; whether filters are inclusive or exclusive at date boundaries; how report or dashboard definitions are versioned; how corrections or late-arriving data are handled; or whether metric formulas are contractual accounting definitions. Availability is also account-dependent: reports require Solutions Architect enablement, custom reports are paid, and dashboards are beta.

## Related

- Company: [[metronome]]
- Concept: [[metronome-reporting-and-analytics]]
- Related sources: [[source-metronome-guides-reporting-insights-data-export-overview]], [[source-metronome-guides-reporting-insights-data-export-database-reference]], [[source-metronome-guides-get-started-how-metronome-works]]

## Raw Sources

- [[raw/metronome/guides/reporting-insights/in-app-reporting-2026-07-13|2026-07-13 snapshot — report access, CSV generation, beta dashboards, ARR definitions, filters, and caveats]]
