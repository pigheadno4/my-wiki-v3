---
title: "Reconcile Metronome data across finance systems"
type: source
date_ingested: 2026-08-01
original_format: webpage
canonical_url: "https://docs.metronome.com/guides/reporting-insights/financial-reporting/reconcile-data"
raw_files:
  - "metronome/guides/reporting-insights/financial-reporting/reconcile-data-2026-07-13.md"
tags: [metronome, data-reconciliation, data-export, financial-reporting, salesforce, stripe]
---

## Overview

This guide presents financial data reconciliation as a pre-revenue-recognition check that records agree across systems for an accounting period. It documents two Metronome retrieval paths—Data Export for bulk warehouse comparisons and list-oriented API access for lower-latency views—and illustrates contract reconciliation against Salesforce plus finalized-invoice reconciliation against Stripe.

## Key takeaways

- Metronome positions reconciliation as a finance control for checking complete and accurate transmission, customer invoicing, and revenue recognition; these are workflow goals rather than a guarantee that any one query proves accounting correctness.
- Data Export is the recommended bulk path, while the API is the lower-latency alternative for dashboards and other near-real-time views.
- The export workflow uses foreign-key mapping, commonly through custom fields, to associate Metronome objects with records in another system.
- The Salesforce example compares contract dates, commit terms, and negotiated overrides; the Stripe example compares a customer's most recent finalized Metronome invoice with the downstream invoice record.
- The SQL snippets retrieve Metronome records and snapshots, but do not show a complete Salesforce join, a custom-field predicate, a Stripe record key, mismatch handling, or an accounting sign-off procedure.

## Reconciliation model

The worked architecture uses Salesforce CPQ for customer and deal information, Metronome for usage-based billing, Stripe as the invoice provider, and a warehouse for recurring snapshots. A Salesforce integration creates the corresponding customer and contract in Metronome; after metering, Metronome sends finalized invoices to Stripe and exports data snapshots to the warehouse for comparison. The page names Salesforce, Stripe, internal systems, and third-party warehouses as possible comparison counterparts, but does not define connector delivery guarantees or synchronization timing.

Data Export is described as more efficient than repeated API calls for larger volumes. Exported rows can be queried beside internal or external records, with custom fields serving as the common foreign-key mechanism. The guide's example stores an SFDC opportunity ID on a Metronome contract so finance can compare start and end dates, commit amount, discounts, and other negotiated terms.

## Contract and invoice checks

The contract, commit, and override examples select the maximum `snapshot_id` from `contracts_contracts`, `contracts_commits`, or `contracts_overrides`, then retrieve a named Metronome object from that snapshot. The surrounding prose says to match through the SFDC opportunity ID, but the sample SQL filters only on Metronome object IDs and does not include the Salesforce-side table or custom-field join. Treat the snippets as Metronome-side retrieval patterns, not complete cross-system reconciliation controls.

For invoices, the example selects the latest row by `end_timestamp` from `invoice` for one customer where `status = 'FINALIZED'`, then directs the reader to compare relevant details with Stripe. It does not identify the Stripe invoice key, enumerate the fields or tolerances to compare, address currencies or tax, or define what happens when records disagree.

## API alternative and evidence boundaries

The API alternative uses list endpoints for common reconciliation objects such as contracts, customers, and invoices. Metronome characterizes this path as lower latency and suitable for dashboards that highlight changes, but the page gives no latency, freshness, snapshot-consistency, pagination, ordering, completeness, or failure-handling guarantee. The separate pagination reference remains necessary for complete traversal of list results.

No direct contradiction was found with the existing reporting-and-export summaries. This guide's claims about complete and accurate transmission and a reliable mechanism to receive all data describe the intended reconciliation outcome; they do not supersede the documented export cadence, average freshness, nullable destination schema, append-only delivery, at-least-once duplicates, or consumer-side latest-row resolution.

## Related

- Companies: [[metronome]], [[stripe]]
- External system in the worked example: Salesforce
- Concepts: [[metronome-reporting-and-analytics]], [[metronome-customers-and-contracts]], [[metronome-invoicing]]
- Related sources: [[source-metronome-guides-reporting-insights-data-export-overview]], [[source-metronome-guides-implement-metronome-core-concepts-provision-contract]], [[source-metronome-api-reference-pagination]]

## Raw Sources

- [[raw/metronome/guides/reporting-insights/financial-reporting/reconcile-data-2026-07-13|2026-07-13 snapshot — reconciliation methods, system roles, and example SQL]]
