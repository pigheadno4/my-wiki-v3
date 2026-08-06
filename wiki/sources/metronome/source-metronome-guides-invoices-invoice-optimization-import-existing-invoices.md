---
title: "Import Existing Invoices into Metronome"
type: source
date_ingested: 2026-08-01
original_format: webpage
canonical_url: "https://docs.metronome.com/guides/invoices/invoice-optimization/import-existing-invoices"
raw_files:
  - "metronome/guides/invoices/invoice-optimization/import-existing-invoices-2026-07-13.md"
tags: [metronome, invoices, historical-invoices, contracts, billing-migration, reporting]
---

## Overview

This guide documents a migration path for bringing an externally provisioned contract and its already-issued invoices into Metronome. The worked flow separates the contract's original start from the date Metronome begins generating invoices, then imports earlier invoice periods through a dedicated historical-invoice endpoint.

## Key takeaways

- Create the contract with its original start and balances, but set `usage_statement_schedule.invoice_generation_starting_at` to the first period Metronome should invoice; in the example, contract creation generates an August draft and does not generate June or July invoices.
- `POST /v1/contracts/createHistoricalInvoices` accepts historical invoice periods and usage-line-item quantities. Metronome applies the contract's unit prices to calculate invoice totals and effects on customer credit and commit balances.
- `preview: true` is a dry run for comparing existing and imported invoices before saving. The page does not document the non-preview request, response schema, validation errors, idempotency, or partial-import behavior.
- Optional `subtotals_with_quantity` windows plus invoice `breakdown_granularity` preserve hourly or daily quantities; Metronome sums those windows for the billing-period invoice.
- Imported invoices are available from the Contracts page or API, but Metronome does not send them to its Stripe integration, preventing duplicate invoice delivery through that route.

## Migration sequence

The example starts with an external monthly contract effective June 1, 2024 whose June and July invoices were already issued outside Metronome. It recreates the contract with the original start and any starting commit or credit balances, while setting `invoice_generation_starting_at` to August 1. That produces an August draft without automatically recreating June and July; the earlier periods are supplied separately to the historical-invoice endpoint.

This page does not establish whether historical invoice import appears in `getEditHistory`, mutates the contract itself after creation, or can overlap periods that already have Metronome invoices. It also does not define ordering, concurrency, atomicity across the `invoices` array, retry safety, or uniqueness controls.

## Historical invoice inputs and calculation

Each worked invoice identifies the customer, contract, credit type, inclusive service-period start, exclusive service-period end, issue date, and usage line items. Each line item supplies a product, its own inclusive and exclusive bounds, and a quantity. Metronome combines those quantities with contract unit prices to calculate the invoice amount and the effects on credit and commit balances; the guide does not document direct amount overrides, taxes, discounts, rounding, currency rules, or reconciliation when the calculated result differs from the externally issued invoice.

The `preview` option performs a dry run so differences can be checked before saving. The source does not state whether preview results are persisted, how a caller commits an accepted preview, or what response fields and invoice states the endpoint returns.

## Optional time breakdowns

For hourly or daily usage-and-cost retrieval, a line item can replace its single `quantity` with time-windowed `subtotals_with_quantity` and set the invoice's `breakdown_granularity`. Metronome sums the window subtotals when generating the invoice for the full billing period. The page does not define permitted granularity values beyond hourly or daily, window coverage and overlap validation, missing-window behavior, time-zone rules, or whether these breakdowns appear in Data Export.

## Operational boundaries

This is an import of invoices already issued outside Metronome, not the credit-memo guide's correction of an incorrect draft or finalized invoice, its credit-and-rebill sequence, a payment refund, or an external A/R credit memo. The source also does not say that importing an invoice changes external A/R, payment, revenue-recognition, tax, or collection state.

Imported invoices can be viewed on the Contracts page or through the API. Metronome explicitly excludes them from the Stripe integration to avoid duplicate customer invoices; that exclusion does not establish behavior for NetSuite, marketplace, custom ERP, or other delivery paths.

## Related

- Company: [[metronome]]
- Concepts: [[metronome-invoicing]], [[metronome-customers-and-contracts]], [[metronome-reporting-and-analytics]], [[metronome-credits-and-commits]]
- Related sources: [[source-metronome-api-reference-contracts-create-a-contract]], [[source-metronome-api-reference-contracts-get-contract-edit-history]], [[source-metronome-guides-invoices-invoice-optimization-issue-credit-memos]], [[source-metronome-guides-invoices-overview]], [[source-metronome-guides-reporting-insights-data-export-database-reference]], [[source-metronome-integrations-invoice-integrations-stripe]]

## Raw Sources

- [[raw/metronome/guides/invoices/invoice-optimization/import-existing-invoices-2026-07-13|2026-07-13 snapshot - historical contract and invoice import, preview, time breakdowns, and Stripe-delivery boundary]]
