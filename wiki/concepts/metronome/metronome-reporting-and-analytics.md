---
title: "Metronome Reporting and Analytics"
type: concept
category: technology
tags: [metronome, data-export, warehouse, reporting, analytics]
---

## Definition

Metronome data export exposes billing and operational data as warehouse tables for reporting, reconciliation, and custom analysis. The database reference spans raw events, customers, invoices, contracts and balances, pricing, packages, payments, alerts, and client-specific metadata.

## Query model

### Imported-invoice time breakdowns

A historical invoice line item can replace one period-level `quantity` with time-windowed `subtotals_with_quantity` and set invoice `breakdown_granularity` so Metronome can retrieve hourly or daily usage-and-cost breakdowns; the billing-period invoice sums the window subtotals. The source says imported invoices are accessible on the Contracts page or through the API, but does not establish Data Export table coverage, snapshot behavior, freshness, permitted granularity values beyond hourly or daily, or validation for gaps and overlaps.

- Treat table grain explicitly: finalized invoices and line items are distinct from daily draft snapshots and daily invoice-breakdown snapshots.
- Use snapshot, watermark, effective-time, and version columns where documented instead of assuming one current row per object.
- Join through stable object IDs such as customer, contract, invoice, line-item, product, billable-metric, and rate-card IDs.
- Follow table-specific scope notes. For example, `contracts_commits` contains contract-level commits but excludes customer-level commits or credits and contract-level credits.

## Delivery and freshness

### In-app reports and dashboards

Metronome's app exposes standard and custom reports as generated CSVs from the Reports tab. Both require Solutions Architect enablement; custom reporting is paid and its reporting engine can query the same tables available through Data Export. A user selects date filters and triggers a report, or can arrange a custom report for app execution or cron scheduling after requirements, sample review, and approval. Most reports generate in one to two hours, larger reports can take up to ten hours, and report data updates once per day, so a run can be stale and require retriggering. The page does not define report roles, file or row limits, cutoff time, retention, link expiry, scheduling semantics, failure behavior, or service levels. “Same tables” does not make report CSV delivery inherit Data Export transfer cadence, destination availability, append-only behavior, at-least-once semantics, or exact row grains.

The separately documented in-app dashboards are beta and require account enablement. Basic Revenue Overview summarizes invoiced amounts, usage and subscription revenue, commits and credits, and customer consumption; Committed & Run Rate ARR defines ARR, movement, NRR, GRR, and logo classifications; Filterable Customer List supports customer search and sorting. Committed ARR annualizes balance-schedule items and scheduled charges over their durations, with CPU commitments converted through the associated rate-card conversion. Run Rate ARR annualizes average usage and subscription revenue over a configurable trailing completed-month window, uses available history for newer customers, and continues to calculate a moving average for churned customers whose latest month is zero. Movement compares a configurable current and base period; GRR excludes expansion while NRR includes it.

The ARR dashboard defaults include excluding `credit` commits and commits or charges shorter than 30 days, a 12-month movement lookback, excluding `credit_drawdown` from run-rate revenue, and a three-completed-month run-rate average. Its caveats say only contract data and finalized invoices are used, invoices are prorated by day across months, and non-USD fiat is unsupported. The page calls customer-detail exploration “real time” but gives no dashboard refresh cadence, latency, API, permissions, caching, correction, retention, availability, or accounting-standard guarantee. The once-daily update warning is stated for generated reports, not explicitly for dashboards; Data Export timing and API-powered merchant dashboards remain separate surfaces.

## Commercial export-row accounting

Metronome defines one Row Exported as one row written to a configured Data Export destination across any schema table. Incremental tables count new or updated rows in each sync; snapshot tables re-export the whole table, and every row in every full cycle counts again. This usage measure is separate from transfer cadence, freshness, destination delivery semantics, and table availability. [[source-metronome-guides-platform-configuration-metronome-pricing-model]]

- One export destination is configured across all Metronome environments, so Production and Sandbox cannot use distinct destinations.
- Selected incremental tables transfer every two hours with four-hour average freshness; the listed snapshot tables and some other exports transfer every 24 hours with 24-hour average freshness.
- Object-storage destinations produce append-only Parquet files with at-least-once semantics. Consumers must resolve repeated primary keys from updates or retries by selecting the most recent row.
- Incremental exports include rows changed since the prior export; Metronome directs consumers to use `updated_at` to obtain the latest updates.

## Global cautions

- Because of the export methodology, every column may appear nullable in the destination schema even when its business meaning is normally required.
- Deprecated columns remain present in several tables and are documented as expected to be null.
- Draft invoices can be `DRAFT_INCOMPLETE`, with no total or line items until a later snapshot hydrates them.
- Some histories are versioned or effective-dated; selecting the latest exported row is not always equivalent to selecting the row valid for a requested time.

## Architecture requirements

Billing architecture should define the freshness and granularity customers need, how sales teams access billing context through a CRM or custom reporting, and how revenue-recognition data and audit trails are handled. The planning guide does not promise a particular API, CRM integration, reporting latency, accounting treatment, or compliance outcome.

## Go-live export checks

Metronome's go-live checklist recommends enabling Data Export in production, confirming that the destination receives data, sampling invoice, customer, and usage objects, and defining a finance reconciliation process. These checks express an operational objective; they do not establish export completeness, freshness, retention, exactly-once delivery, accounting correctness, or a general audit guarantee, so the dedicated export delivery and table-grain rules still apply. [[source-metronome-guides-implement-metronome-production-checklist]]

## Revenue-recognition reporting model

Metronome documents daily-granularity transaction and ledger data, available through APIs or Data Export, for merchant-owned revenue-recognition workflows by product and category. The reporting categories are on-demand usage, prepaid-commit drawdown, postpaid-commit drawdown, overage, and credit drawdown. In the guide's query model, invoice line items and selected balance-ledger entries supply the amounts; `FINALIZED` invoices form the recognized-revenue report and `DRAFT` invoices form the accrued-revenue report. Automated invoice-deduction and postpaid-true-up ledger entries are excluded when the same amount already appears in invoice line items, while `prepaid_segment_expiration` is included because Metronome does not invoice that expiration. Metronome explicitly does not create revenue journal entries. The page does not define a governing accounting standard, performance obligations, allocation, close controls, corrections, or auditor approval, and invoice status plus exported data is not by itself proof of accounting correctness. Existing table-grain and documented-freshness cautions remain table-specific. For object-storage destinations specifically, exports are append-only and at-least-once, so repeated primary keys require selecting the most recent row. Incremental exports separately use `updated_at` as the documented latest-update field.

## Financial reconciliation workflows

Metronome documents Data Export and the API as two reconciliation paths: Data Export is the preferred bulk mechanism, while list endpoints provide lower-latency access for change-oriented dashboards. Its worked warehouse flow uses custom fields as foreign-key mappings to compare contract dates, commits, and overrides against Salesforce and the latest finalized invoice against Stripe. The example SQL selects maximum contract, commit, or override snapshots and one customer's most recent `FINALIZED` invoice, but it does not show the Salesforce-side join, custom-field predicate, Stripe record key, mismatch tolerances, pagination, or accounting sign-off. Treat complete-and-accurate-transmission language as the workflow objective, not as an export completeness or accounting guarantee; the documented cadence still applies, and object-storage exports retain their documented append-only, at-least-once duplication, and consumer-side latest-row resolution boundaries. [[source-metronome-guides-reporting-insights-financial-reporting-reconcile-data]]

## Sources

- [[source-metronome-guides-reporting-insights-in-app-reporting]] — report enablement and CSV timing, custom-report scope, beta dashboards, ARR definitions and filters, and calculation limits

- [[source-metronome-guides-reporting-insights-financial-reporting-revenue-recognition]] - revenue categories, invoice and ledger query model, finalized-versus-draft reporting, and journal-entry ownership boundary

- [[source-metronome-guides-invoices-invoice-optimization-import-existing-invoices]] - optional hourly or daily historical invoice quantities and API or Contracts-page access boundary

- [[source-metronome-guides-reporting-insights-data-export-database-reference]] — exported table families, grains, fields, snapshot behavior, and global cautions
- [[source-metronome-guides-reporting-insights-data-export-overview]] — destination scope, delivery cadence, freshness, and object-storage semantics
- [[source-metronome-guides-implement-metronome-planning-your-billing-architecture]] — customer, sales, finance, and audit distribution requirements

## Related

- [[metronome-event-ingestion]]
- [[metronome-invoicing]]
- [[metronome-customers-and-contracts]]
- [[metronome-products-and-rate-cards]]
