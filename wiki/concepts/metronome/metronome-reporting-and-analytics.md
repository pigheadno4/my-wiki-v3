---
title: "Metronome Reporting and Analytics"
type: concept
category: technology
tags: [metronome, data-export, warehouse, reporting, analytics]
---

## Definition

Metronome data export exposes billing and operational data as warehouse tables for reporting, reconciliation, and custom analysis. The database reference spans raw events, customers, invoices, contracts and balances, pricing, packages, payments, alerts, and client-specific metadata.

## Audit-log reporting surface

Metronome's `GET /v1/auditLogs` is a cursor-pollable account-activity source intended for compliance reporting, security monitoring, and troubleshooting across API, UI, and automated actions. Time filters are inclusive-start and exclusive-end and cannot be combined with a cursor; paired resource filters and explicit timestamp sort can narrow retrieval. Empty `data` means no new logs yet, not permanent completion, but the page does not define retention, earliest coverage, visibility latency, cursor recovery, cross-page consistency, export, or evidence-integrity guarantees. Because actor, resource, action, and status are optional in the item schema, retrieval alone does not establish a complete attributable compliance population. [[source-metronome-api-reference-security-get-audit-logs]]

## Invoice-list reporting surface

Metronome's customer invoice-list API supports billing-history, current-draft, reconciliation, support, and date-bounded reporting queries. Its date filters use inclusive billing-period start and exclusive billing-period end rather than issue date, and complete retrieval requires following nullable `next_page` cursors. The page does not establish cursor snapshot consistency or reporting freshness, and its conflicting default-order descriptions require callers that depend on order to pass the `sort` parameter explicitly. [[source-metronome-api-reference-invoices-list-invoices]]

## Invoice-breakdown reporting surface

The invoice-breakdown API supplies one customer's hourly or daily invoice time windows for usage and cost dashboards, reports, and dispute investigation. Required timestamp filters select whole breakdown windows, while daily and hourly reads have separate 35-day and 24-hour temporal caps and a nullable envelope cursor for further results. Because backdated usage can update breakdowns after invoice finalization and the page defines no revision, as-of time, freshness SLA, cursor snapshot, or stable ordering among windows of one invoice, a completed traversal is not proof of an immutable reporting population. This API read also remains distinct from daily draft-breakdown warehouse snapshots and finalized export rows. [[source-metronome-api-reference-invoices-list-invoice-breakdowns]]

## Query model

For merchant-facing seat-balance views, `POST /v1/contracts/seatBalances/list` supplies one contract's current and initial combined credit/commit balances by seat and credit type. Optional seat-level sibling credit and commit arrays can include their own ledgers, but the expanded schemas omit `credit_type_id`; a dashboard or reconciliation process cannot map those objects to a particular per-credit-type balance from this response alone. The example's sole seat-1 balance reports current `30000` and starting `50000`, matching the commit detail, while a separate credit reports current `20000` and a `25000` segment-start amount, with no established reconciliation. Complete seat retrieval requires following the body cursor and nested seat-count pagination. With detail expansion, the documented 100-item threshold can be exceeded to return a complete seat, as the 108-commit example shows; no seat ordering or greedy-selection tie-breaker is documented. Missing requested seats can be silently omitted when configured, and the page establishes no retention, freshness, snapshot consistency, duplicate/skip, or broader reconciliation guarantee. [[source-metronome-api-reference-credits-and-commits-list-seat-balances]]

For merchant-facing seat views, Metronome routes aggregate quantity changes to subscription quantity history and identity-bearing changes to per-`seat_id` history. Its seat-balance list can return current balance for all seats or one seat and can include grant and burn-down ledgers over optional date bounds. The guide does not establish response schemas, pagination, ordering, retention, freshness, snapshot consistency, or reconciliation guarantees; use dedicated API references for those details. [[source-metronome-guides-pricing-packaging-subscription-manage-seats]]

Metronome's SQL cookbook supplies starting-point queries across customers, events, finalized and draft invoices, invoice-breakdown snapshots, contracts, rate cards, and alerts. Its patterns include `archived_at IS NULL` for non-archived customers, table-global maximum draft snapshots, ID-plus-snapshot breakdown joins, descending `updated_at` ordering for contract overrides, future `ending_before` filtering for rate-card entries, and active webhook-alert predicates. Apply four authorities before production aggregation: only the two breakdown examples filter `environment_type = 'PRODUCTION'` even though one destination spans Production and Sandbox; append-only at-least-once object-storage delivery requires latest-row resolution per primary key before aggregation; `DRAFT_INCOMPLETE` rows can make `COUNT(0)` include rows whose null `total` is ignored by `SUM(total)`; and the rate-card query omits `starting_at`, nullable-end semantics, and version/snapshot selection. A global maximum snapshot is not per-key deduplication or a per-object completeness guarantee, and descending override order is not a one-row selector.

A consolidated hierarchy invoice can retain origin customer and contract identifiers on line items, allowing consumers to group subsidiary spend and measure contract-level usage. Metronome also keeps standalone usage statements visible through the UI, API, and data export when consolidation occurs; the guide's specific caution is to filter the standalone parent usage statement when showing spend detail to the parent so that parent-facing UI does not count both it and the consolidated invoice. This is not a documented blanket deduplication rule for every standalone child statement, analysis, or export grain. The guide separately says invoice and commit embeddable dashboards do not work for customers whose contract is in a hierarchy; it does not extend that limitation to all reports, API views, or exports.

### Imported-invoice time breakdowns

A historical invoice line item can replace one period-level `quantity` with time-windowed `subtotals_with_quantity` and set invoice `breakdown_granularity` so Metronome can retrieve hourly or daily usage-and-cost breakdowns; the billing-period invoice sums the window subtotals. The source says imported invoices are accessible on the Contracts page or through the API, but does not establish Data Export table coverage, snapshot behavior, freshness, permitted granularity values beyond hourly or daily, or validation for gaps and overlaps.

- Treat table grain explicitly: finalized invoices and line items are distinct from daily draft snapshots and daily invoice-breakdown snapshots.
- Use snapshot, watermark, effective-time, and version columns where documented instead of assuming one current row per object.
- Join through stable object IDs such as customer, contract, invoice, line-item, product, billable-metric, and rate-card IDs.
- Follow table-specific scope notes. For example, `contracts_commits` contains contract-level commits but excludes customer-level commits or credits and contract-level credits.

For non-monotonically increasing `LATEST` metrics, this guide defines an important reconciliation boundary: invoice breakdowns return incremental quantity and associated cost for each time window, including negative values when usage falls, whereas usage endpoints return the absolute latest reported value within each requested window. With no breakdown, the usage example returns the latest value across the full query period. Comparing these surfaces as if they shared one quantity grain can create apparent mismatches; exact endpoint parameters, envelopes, pagination, ordering, freshness, and consistency require the dedicated API references.


## Delivery and freshness

### In-app reports and dashboards

Metronome's app exposes standard and custom reports as generated CSVs from the Reports tab. The current guide routes enablement through the support portal rather than a named Solutions Architect; custom reporting is paid, uses `solutions@metronome.com` for commercial contact, and can query the same tables available through Data Export. A user supplies dates and triggers a report, while a custom report can be arranged for app execution or cron scheduling after requirements, sample review with the Metronome team, and approval. Most reports generate in one to two hours, larger reports can take up to ten hours, and report data updates once per day, so a run can be stale and require retriggering. The page does not define report roles, complete CSV schemas or row grains, file or row limits, cutoff time, retention, link expiry, scheduling ownership, completeness, failure behavior, or service levels. Shared table access does not make report CSV delivery inherit Data Export cadence, destination availability, append-only behavior, at-least-once semantics, or exact row grains.

The separately documented in-app dashboards are beta and require support-portal account enablement. Basic Revenue Overview summarizes invoiced amounts, usage and subscription revenue, commits and credits, and customer consumption; Committed & Run Rate ARR defines ARR, movement, NRR, GRR, and logo classifications; Filterable Customer List supports customer search and sorting. Committed ARR annualizes balance-schedule items and scheduled charges over their durations, while Run Rate ARR annualizes average usage and subscription revenue over a configurable trailing completed-month window. The ARR dashboard uses only contract data and finalized invoices, prorates invoices by day across months, and does not support non-USD fiat. The page calls customer-detail exploration “real time” but defines no dashboard refresh cadence, latency, caching, permissions, availability, export, embedding, correction, retention, or accounting-standard guarantee. The once-daily warning applies explicitly to generated reports, not dashboards; Data Export and merchant-built reporting remain separate surfaces. [[source-metronome-guides-reporting-insights-in-app-reporting]]

The native Salesforce integration is a distinct CRM-facing reporting surface from Data Export and in-app reporting: Census pushes selected Metronome customer, contract, commit or credit, rate-card, invoice, and invoice-line data into Salesforce once per day. The initial sync can take a couple of hours, and the cadence cannot currently be configured more frequently. Completed-sync totals count only rows changed since the prior sync, while the downloadable error CSV samples at most 100 failures for one object type and sync. Those counters and samples do not establish full-population completeness, end-to-end Salesforce visibility, retry or recovery, ordering across object types, or a financial-reconciliation guarantee.

### Embeddable customer dashboards

Bearer-authenticated `POST /v1/dashboards/getEmbeddableUrl` generates an iframe-ready, customer-specific URL for `invoices`, `usage`, or `commits_and_credits`. The prose calls the URL secure and time-limited and says it contains authentication tokens plus configuration parameters, while HTTP `200` requires only outer `data` and does not require nested `url`. Invoice-only dashboard options cover zero-usage lines, contract, invoice type, and invoice status; the schema additionally names deprecated `hide_voided_invoices` and `billable_status_filter` without defining a value contract for the latter. This embedded external-app surface is distinct from app-native beta dashboards and generated CSV reports. The endpoint defines no data-refresh cadence, URL TTL or expiry timestamp, permission inheritance, revocation, regeneration, origin restriction, browser-exposure, or failure-recovery behavior. [[source-metronome-api-reference-customers-get-an-embeddable-customer-dashboard]]

## Commercial export-row accounting

Metronome defines one Row Exported as one row written to a configured Data Export destination across any schema table. Incremental tables count new or updated rows in each sync; snapshot tables re-export the whole table, and every row in every full cycle counts again. This usage measure is separate from transfer cadence, freshness, destination delivery semantics, and table availability. [[source-metronome-guides-platform-configuration-metronome-pricing-model]]

- One export destination is configured across all Metronome environments, so Production and Sandbox cannot use distinct destinations.
- Selected incremental tables transfer every two hours with four-hour average freshness; the listed snapshot tables and some other exports transfer every 24 hours with 24-hour average freshness.
- Object-storage destinations produce append-only Parquet files with at-least-once semantics. Consumers must resolve repeated primary keys from updates or retries by selecting the most recent row.
- Incremental exports include rows changed since the prior export; Metronome directs consumers to use `updated_at` to obtain the latest updates.

## Global cautions

- The 2026-08-28 database reference documents `contracts_commits.cost_basis` directly as amount paid for a commit divided by credit granted. The broader `contracts_balances` table includes postpaid, prepaid, and credit rows but retains that commit-specific `cost_basis` wording; applicability and denominator meaning for credit rows, denominator-zero behavior, and accounting treatment are not documented. The snapshot also adds created-commit duration, rollover, and rate fields to prepaid balance-threshold exports and nullable customer scoping to alert exports. Treat these as versioned schema additions and consult the current raw field catalog before production queries. [[source-metronome-guides-reporting-insights-data-export-database-reference]]
- Because of the export methodology, every column may appear nullable in the destination schema even when its business meaning is normally required.
- Deprecated columns remain present in several tables and are documented as expected to be null.
- Draft invoices can be `DRAFT_INCOMPLETE`, with no total or line items until a later snapshot hydrates them.
- Some histories are versioned or effective-dated; selecting the latest exported row is not always equivalent to selecting the row valid for a requested time.

> [!warning] SQL cookbook boundaries
> The `Finalized Invoices` queries have no status predicate even though the database reference says `invoice` includes both `FINALIZED` and `VOID` rows. The alert-history query titled `over the last week` has no date predicate. The detailed draft-breakdown query selects six nonaggregated expressions while grouping only by the first two despite the standard-SQL framing. Beyond those raw-page defects, one destination can contain Production and Sandbox while only the two breakdown examples filter Production; append-only at-least-once object-storage delivery requires latest-row selection per primary key; global maximum snapshots do not guarantee per-object completeness; and `DRAFT_INCOMPLETE` rows can be counted while their null totals are ignored by `SUM`. The rate-card count tests only future `ending_before`, omitting start time, nullable-end semantics, and version/snapshot selection. Reconcile status, environment, delivery deduplication, draft hydration, effective time, exported grain, time scope, and target-warehouse grouping before production use.

> [!warning] Cookbook currency alias
> `total/100 AS total_dollars` cannot establish a universal scale. The direct Metronome authority [[metronome-currencies-and-custom-pricing-units]] documents USD in cents and listed non-USD fiat in whole units; select the row's pricing-unit rule before conversion.

## Architecture requirements

Billing architecture should define the freshness and granularity customers need, how sales teams access billing context through a CRM or custom reporting, and how revenue-recognition data and audit trails are handled. The planning guide does not promise a particular API, CRM integration, reporting latency, accounting treatment, or compliance outcome.

## Go-live export checks

Metronome's go-live checklist recommends enabling Data Export in production, confirming that the destination receives data, sampling invoice, customer, and usage objects, and defining a finance reconciliation process. These checks express an operational objective; they do not establish export completeness, freshness, retention, exactly-once delivery, accounting correctness, or a general audit guarantee, so the dedicated export delivery and table-grain rules still apply. [[source-metronome-guides-implement-metronome-production-checklist]]

## Revenue-recognition reporting model

A separate ASC 606 guide maps the standard's five steps—contract identification, performance-obligation identification, transaction-price determination, allocation, and recognition—to Metronome contracts, products, pricing, usage, invoices, balances, ledgers, exports, and integration identifiers. Metronome describes daily and product-level data, billed-versus-earned views, true-up linkage, and external ERP or revenue-subledger integration as support for merchant-owned workflows. The same guide expressly says Metronome is not a revenue-recognition platform, does not generate journal entries or make accounting determinations, and leaves policy and compliance to the customer. Its broad full-history, immutable-audit-trail, schema-stability, real-time, retention, and audit-ready claims do not replace table-specific export grain, cadence, duplicate-delivery, snapshot, correction, reconciliation, or sign-off authority. [[source-metronome-guides-reporting-insights-financial-reporting-asc-606-revenue-recognition]]

Metronome documents daily-granularity transaction and ledger data, available through APIs or Data Export, for merchant-owned revenue-recognition workflows by product and category. The reporting categories are on-demand usage, prepaid-commit drawdown, postpaid-commit drawdown, overage, and credit drawdown. In the guide's query model, invoice line items and selected balance-ledger entries supply the amounts; `FINALIZED` invoices form the recognized-revenue report and `DRAFT` invoices form the accrued-revenue report. Automated invoice-deduction and postpaid-true-up ledger entries are excluded when the same amount already appears in invoice line items, while `prepaid_segment_expiration` is included because Metronome does not invoice that expiration. Metronome explicitly does not create revenue journal entries. The page does not define a governing accounting standard, performance obligations, allocation, close controls, corrections, or auditor approval, and invoice status plus exported data is not by itself proof of accounting correctness. Existing table-grain and documented-freshness cautions remain table-specific. For object-storage destinations specifically, exports are append-only and at-least-once, so repeated primary keys require selecting the most recent row. Incremental exports separately use `updated_at` as the documented latest-update field.

Metronome's CloudNet examples relate customer and contract metadata, invoice types, invoice-line-item commit/product/service-period fields, and credit or commit balance ledgers across on-demand usage, free credits, prepaid drawdown and expiration, overage, and postpaid true-up. Treat them as illustrative provider reporting examples rather than executable schema: the introduction promises `invoices.type`, `line_items.product_id`, and `balances.type`, while the examples use `invoice_type`, omit `product_id` in favor of `product_name`, and vary the balance-type header among `ledger type`, `ledger_type`, and `commit_type`. Customer B is `10002` but its contract uses Customer A's `10001`; invoice, line-item, and ledger-entry IDs are reused across scenarios and balances, including three periods sharing invoice `30011`. The scenarios may be isolated alternatives, but do not combine or join them by those sample IDs without current source-data and identifier-scope verification. The examples also contain arithmetic and category conflicts, so rebuild control totals from current exports. Under the parent guide's query model, automated credit/prepaid/postpaid invoice-deduction and postpaid-true-up ledger entries are not added again when the same amount is already represented through invoice line items; `prepaid_segment_expiration` is the stated non-invoiced inclusion. These are query-construction rules, not GAAP, IFRS, journal-entry, close-control, or merchant-policy authority.

## Financial reconciliation workflows

Metronome documents Data Export and the API as two reconciliation paths: Data Export is the preferred bulk mechanism, while list endpoints provide lower-latency access for change-oriented dashboards. Its worked warehouse flow uses custom fields as foreign-key mappings to compare contract dates, commits, and overrides against Salesforce and the latest finalized invoice against Stripe. The example SQL selects maximum contract, commit, or override snapshots and one customer's most recent `FINALIZED` invoice, but it does not show the Salesforce-side join, custom-field predicate, Stripe record key, mismatch tolerances, pagination, or accounting sign-off. Treat complete-and-accurate-transmission language as the workflow objective, not as an export completeness or accounting guarantee; the documented cadence still applies, and object-storage exports retain their documented append-only, at-least-once duplication, and consumer-side latest-row resolution boundaries. [[source-metronome-guides-reporting-insights-financial-reporting-reconcile-data]]

Metronome's GTM reporting guide models expected commit pacing from access schedules and intended actual burn from finalized plus current-period invoice data, but its generalized SQL does not resolve the export table family. The finalized example names base invoice tables while filtering `li.line_item_type`, which the database reference documents on breakdown line items. The draft example names `draft_invoice` and `draft_line_item` while selecting breakdown timestamps, `commit_segment_id`, and `invoice_breakdown_id`, which the reference associates with the draft-breakdown family. Do not choose a family by inference: reconcile the current reference, fields, joins, and grain first. Finalized base invoice data is incremental at 2-hour transfer and 4-hour average freshness; `contracts_balances` and base draft invoice data are 24-hour/24-hour snapshots. Base draft invoices emit one point-in-time invoice snapshot per day at start-of-day UTC, while draft breakdown snapshots contain month-to-date rows. Separately, object-storage exports are append-only and at-least-once, so latest-row resolution for repeated primary keys remains necessary after snapshot selection. Summing multiple snapshots or delivery duplicates can overstate burn. The source's burn bands and outreach actions are merchant playbook examples, not platform-enforced thresholds.

## Sources

- [[source-metronome-api-reference-invoices-list-invoice-breakdowns]] - hourly or daily invoice time-series read, required window bounds, temporal caps, envelope pagination, late-usage mutation, and reporting-completeness limits
- [[source-metronome-api-reference-customers-get-an-embeddable-customer-dashboard]] - customer-scoped embedded invoice, usage, and commit-and-credit dashboard URLs, request and response placement, customization, and lifecycle, freshness, and exposure boundaries
- [[source-metronome-guides-reporting-insights-financial-reporting-asc-606-revenue-recognition]] - ASC 606 five-step product mapping, reporting and reconciliation inputs, timing tensions, worked-detail route, and accounting-authority boundary

- [[source-metronome-guides-pricing-packaging-subscription-manage-seats]] — aggregate and per-seat history routes plus current seat-balance and ledger-view navigation

- [[source-metronome-guides-reporting-insights-data-export-cookbook]] — cross-domain SQL starting points with corrected environment, at-least-once latest-row, snapshot/completeness, invoice-status, draft-hydration, effective-time/version, aggregation, and currency boundaries
- [[source-metronome-guides-reporting-insights-financial-reporting-revenue-recognition-examples]] — complete CloudNet export examples, reused-key and schema cautions, double-count boundary, and arithmetic/classification conflicts

- [[source-metronome-guides-reporting-insights-gtm-reporting-get-commit-and-usage-analytics]] — expected-versus-actual commit burn model, unresolved base-versus-breakdown SQL fields, snapshot and delivery-overcount cautions, null attribution conflict, and illustrative GTM burn bands
- [[source-metronome-guides-pricing-packaging-billing-model-guides-model-hierarchical-customer-relationships]] — consolidated origin analysis, standalone-statement double-count boundary, and embeddable-dashboard limitation

- [[source-metronome-guides-reporting-insights-in-app-reporting]] — report enablement and CSV timing, custom-report scope, beta dashboards, ARR definitions and filters, and calculation limits

- [[source-metronome-guides-reporting-insights-financial-reporting-revenue-recognition]] - revenue categories, invoice and ledger query model, finalized-versus-draft reporting, and journal-entry ownership boundary

- [[source-metronome-guides-invoices-invoice-optimization-import-existing-invoices]] - optional hourly or daily historical invoice quantities and API or Contracts-page access boundary

- [[source-metronome-guides-reporting-insights-data-export-database-reference]] — exported table families, grains, fields, snapshot behavior, and global cautions
- [[source-metronome-guides-reporting-insights-data-export-overview]] — destination scope, delivery cadence, freshness, and object-storage semantics
- [[source-metronome-guides-implement-metronome-planning-your-billing-architecture]] — customer, sales, finance, and audit distribution requirements

- [[source-metronome-guides-implement-metronome-core-concepts-non-monotonically-increasing-metrics]] - reconciliation boundary between incremental invoice-breakdown quantities and absolute latest usage-query values

- [[source-metronome-integrations-platform-integrations-sfdc-integration]] - daily CRM sync through Census, selected customer and billing-data scope, changed-row outcome monitoring, 100-failure sample boundary, and freshness and completeness unknowns



- [[source-metronome-api-reference-invoices-list-invoices]] - invoice-history and current-draft retrieval, billing-period filters, pagination completeness, and ordering boundaries
- [[source-metronome-api-reference-security-get-audit-logs]] - compliance-reporting audit stream, time and resource filters, cursor polling, attribution gaps, and historical-completeness boundaries

- [[source-metronome-api-reference-credits-and-commits-list-seat-balances]] - dashboard-oriented seat balances, sibling detail expansions without credit-type attribution, example reconciliation ambiguity, endpoint-specific pagination, completeness limits, and reporting consistency unknowns

- [[source-metronome-integrations-invoice-integrations-netsuite]] - revenue-system invoice and payment synchronization, cross-system identifiers for reconciliation, and accounting-outcome boundaries

## Related

- [[metronome-event-ingestion]]
- [[metronome-invoicing]]
- [[metronome-customers-and-contracts]]
- [[metronome-products-and-rate-cards]]
