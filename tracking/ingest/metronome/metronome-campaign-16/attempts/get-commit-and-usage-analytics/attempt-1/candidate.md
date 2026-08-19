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

This guide describes a warehouse-and-BI workflow for customer-level commit burn dashboards used by go-to-market teams. It combines an expected pacing curve derived from commit access schedules with actual consumption from finalized and current draft invoice line items, then proposes operational signals for renewal, adoption, and implementation outreach.

The page is implementation guidance rather than an executable query contract. Its SQL is explicitly generalized, contains example-level alias and table-name inconsistencies, and must be reconciled with the dedicated Data Export database reference, table grains, delivery cadence, and duplicate-row handling before production use.

## Key takeaways

- Data Export is a paid prerequisite, and the guide asks users to enable customer, contract-related, finalized-invoice, draft-invoice, and corresponding line-item tables. Its broad daily-flow wording does not replace the table-specific cadence and freshness rules in the dedicated export documentation.
- Expected burn is modeled from each balance access schedule by spreading the scheduled amount across its service-period days; actual burn comes from invoice line items whose commit ID identifies the consumed balance.
- Historical consumption uses finalized invoices, while the current billing period uses draft invoices and draft line items. The two result sets must be combined with the access schedule and an appropriate date spine.
- A null commit ID cannot be joined to a particular commit, so this guide excludes the associated usage from the commit burn curve. Its stronger claim that every null value is on-demand usage conflicts with the existing revenue-reporting guide, which says null can mean on-demand or overage and requires client-defined metadata to distinguish them.
- The suggested burn-rate bands, warning thresholds, and outreach actions are examples for merchant-owned GTM operations, not Metronome-enforced limits or universal health definitions.

## Export prerequisites and scope

The guide calls for at least seven days of usage data, an Admin or Analyst role, contract-and-commit visibility, Data Export configuration access, and a BI tool that can query the exported Metronome tables. It identifies Data Export as paid and says initial setup typically takes two to three hours plus ongoing refinement.

The requested table set includes customers, contract-related models, finalized invoices and line items, and draft invoices and line items. The guide describes data flowing daily, but the dedicated Data Export overview remains authoritative for table-specific transfer frequency, average freshness, destination semantics, and latest-row selection. In particular, a production model must account for snapshot grains and, for object-storage destinations, append-only at-least-once delivery rather than assuming one current row per ID.

## Expected and actual burn curves

### Expected pacing

The expected curve parses schedule items from an access-schedule JSON value, converts monetary amounts from cents to currency units, calculates an inclusive schedule duration, and divides each schedule amount by that duration to obtain a daily expected rate. The sample also classifies a prepaid balance with an empty invoice schedule as a free commit.

The query is not directly executable as published. The source says its generalized SQL will most likely require adaptation, and the first sample selects through an undefined `sch` alias after naming the access-schedule relation `acs`; it also alternates between `contracts_balances_table` and `balances_table`. Those examples do not establish exact production table or JSON-field names.

### Historical and current consumption

For historical burn, the guide filters invoices to `FINALIZED`, joins invoice line items, and treats a populated `commit_id` as the balance identifier. The selected data includes customer, product, service-period, invoice, quantity, unit price, line-item total, and audit timestamps.

For the active billing period, a parallel query uses draft invoices and draft line items. The guide says this current-period result supplements the finalized history so the combined model reflects consumption through the current day. The draft example also carries a `commit_segment_id`, but the source does not define how segment changes, repeated snapshots, voids, backfills, or late corrections should be deduplicated in this model.

## Combined model and GTM use

The source instructs readers to join `line_item.commit_id` to the access-schedule balance ID, create a date spine over the relevant schedule service period, and cumulatively sum line-item totals within that period. Usage without a commit ID is omitted because it cannot be attributed to a particular commitment. A forecast curve is deliberately left to merchant-selected heuristics.

Comparing expected and actual curves can flag customers consuming faster, slower, or approximately on pace. The guide gives illustrative bands—80–110% as on track, above 150% before month three as concerning, and below 50% after 60 days as an adoption signal—and proposes account-manager or CSM dashboards, alerts, renewal outreach, and product-activation conversations. These thresholds are playbook examples, not contractual billing behavior.

## Data and documentation cautions

> [!warning] Contradiction
> This guide maps `commit_id IS NULL` to on-demand usage. The existing revenue-reporting source says a null line-item commit ID can mean either on-demand usage or overage and requires client-defined contract or commit metadata to distinguish them. Preserve the narrower conclusion: null means the amount is not attributable to a specific commit; verify classification before labeling it on-demand.

> [!warning] Generalized SQL
> The sample queries are expressly non-executable generalized SQL and contain unresolved identifiers and table-name variants. They also do not implement the dedicated export documentation's snapshot selection or object-storage duplicate-row resolution. Treat the page as a modeling recipe and verify current schemas before deployment.

Backdated usage can temporarily spike the curve, price changes can distort burn calculations, and recent configuration changes should be checked before escalating anomalies. The guide advises allowing 24 hours for backdated-usage effects and says draft invoice exports are daily, so neither the chart nor an alert should be represented as real-time. It does not define alert delivery, calculation ownership, time zones, currency aggregation, correction policy, data-retention requirements, access control for the BI layer, or forecast validation.

## Related

- Company: [[metronome]]
- Concepts: [[metronome-reporting-and-analytics]], [[metronome-credits-and-commits]]
- Related sources: [[source-metronome-guides-reporting-insights-data-export-overview]], [[source-metronome-guides-reporting-insights-data-export-database-reference]], [[source-metronome-guides-reporting-insights-financial-reporting-revenue-recognition]]

## Raw Sources

- [[raw/metronome/guides/reporting-insights/gtm-reporting/get-commit-and-usage-analytics-2026-07-13|2026-07-13 snapshot — commit pacing, finalized and draft consumption queries, and GTM playbook guidance]]
