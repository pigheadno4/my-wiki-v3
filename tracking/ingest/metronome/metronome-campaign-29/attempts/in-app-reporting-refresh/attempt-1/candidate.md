---
title: "Metronome In-App Reports and Dashboards"
type: source
date_ingested: 2026-08-30
canonical_url: "https://docs.metronome.com/guides/reporting-insights/in-app-reporting"
original_format: webpage
raw_files:
  - "metronome/guides/reporting-insights/in-app-reporting-2026-08-28.md"
  - "metronome/guides/reporting-insights/in-app-reporting-2026-07-13.md"
tags: [metronome, reporting, analytics, dashboards, arr]
---

## Overview

This guide documents two reporting surfaces inside the Metronome app: generated CSV reports and beta dashboards. It identifies who must enable them, how users trigger and receive reports, the data and freshness boundaries, and the definitions and limits of the Committed & Run Rate ARR Dashboard.

## Query-critical facts

- Metronome can run standard and custom reports against a customer's Metronome data for CSV download from the app's Reports tab. The current page routes report enablement through the Metronome support portal; custom reporting is a paid feature whose commercial contact is `solutions@metronome.com`.
- A user triggers a standard report in the Reports tab by selecting a predefined report and filtering dates. Completion produces an email confirmation with a link back to the UI for CSV download. The catalog covers customers, contracts, prepaid commits and credits, finalized invoices and line items, expired-commit ledger entries, true-up invoices, and monthly revenue by product and category. These descriptions state reporting purposes, not complete CSV schemas or accounting guarantees.
- Most reports generate within one to two hours, while larger reports can take up to ten hours. Report data updates once per day, so a run can be stale and may need to be triggered again; the page gives no freshness timestamp, cutoff, completeness, retention, failed-job, retry, email-delivery, or download-link guarantee.
- Custom reports can query the same data tables available through Data Export. The customer requests a report through support, shares requirements, reviews sample data with the Metronome team, approves the result, and chooses app triggering or cron scheduling. “Same data tables” establishes query scope only; it does not make a report CSV inherit Data Export delivery cadence, row grain, append-only behavior, at-least-once semantics, or completeness.
- In-app dashboards are beta and require account enablement through the support portal. The documented set is Basic Revenue Overview, Committed & Run Rate ARR, and Filterable Customer List. The page describes access directly within the Metronome app and calls customer-detail exploration “real time,” but it defines no refresh cadence, latency, caching, permission, availability, export, embedding, or external-app contract.
- Committed ARR annualizes balance schedule items and scheduled charges over their durations; CPU commits use the associated rate-card conversion. Run Rate ARR annualizes average usage and subscription revenue over a configurable trailing window, uses available history for newer customers, and continues a moving average for churned customers whose latest month is zero. Movement compares the current period with a configurable base period; GRR excludes expansion and NRR includes it. The Run Rate tab uses completed months only.
- The ARR dashboard uses only contract data and finalized invoices, prorates invoices by day across months, and does not support non-USD fiat currencies. Its formulas and labels are product reporting definitions, not stated GAAP, IFRS, ASC 606, audit, or merchant accounting-policy authority.

## Material boundaries

- Standard reports, custom reports, beta in-app dashboards, Data Export, and merchant-built or embedded reporting surfaces are distinct. Navigation to Data Export and shared table access do not establish shared delivery, freshness, access, or reliability semantics.
- The standard-report catalog's “all” wording is scoped to the named account objects or invoice classes; the page does not document columns, row grain, ordering, filter-boundary semantics, correction handling, late-arriving data, or whether every account receives an identical catalog.
- The page does not say which app roles may view, trigger, schedule, or download reports or dashboards, how definitions are versioned, how report or dashboard failures recover, or whether dashboard “real time” has a measurable service level. The daily-update warning is stated for generated reports, not explicitly for dashboards.

## Raw-detail coverage map

Use the raw page for the complete standard-report catalog and stated use cases; the report-generation UI path and email-download flow; processing-time and once-daily freshness note; the paid custom-report request, sample-review, approval, and cron choices; the three beta dashboard descriptions; full Committed ARR and Run Rate ARR formulas and methodology; ARR movement, GRR, NRR, and customer/logo definitions; every Committed and Run Rate filter, type, default, and preservation rule; and the finalized-invoice, daily-proration, and currency caveats. The guide does not supply complete CSV schemas, dashboard APIs, role permissions, failure behavior, embedding contracts, or accounting-standard authority.

## Related

- Company: [[metronome]]
- Primary concept: [[metronome-reporting-and-analytics]]
- Related sources: [[source-metronome-guides-reporting-insights-data-export-overview]], [[source-metronome-guides-reporting-insights-data-export-database-reference]], [[source-metronome-guides-get-started-how-metronome-works]]

## Raw Sources

- [[raw/metronome/guides/reporting-insights/in-app-reporting-2026-08-28|2026-08-28 snapshot - support-routed report and dashboard access, CSV generation, beta dashboards, ARR definitions, filters, and caveats]]
- [[raw/metronome/guides/reporting-insights/in-app-reporting-2026-07-13|2026-07-13 snapshot - prior Solutions Architect and representative access wording with the same reporting and ARR surfaces]]
