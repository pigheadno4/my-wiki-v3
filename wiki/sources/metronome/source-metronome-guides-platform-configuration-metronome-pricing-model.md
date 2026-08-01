---
title: "Metronome's Pricing Model"
type: source
date_ingested: 2026-08-01
original_format: webpage
canonical_url: "https://docs.metronome.com/guides/platform-configuration/metronome-pricing-model"
raw_files:
  - "metronome/guides/platform-configuration/metronome-pricing-model-2026-07-13.md"
tags: [metronome, platform-pricing, consumption-pricing, usage-metering, data-export]
---

## Overview

This page defines how Metronome meters charges to organizations that use the platform. It separates a fixed annual platform fee from consumption-based charges, defines the commercial meanings of Events and Billings, and explains how exported data rows accumulate. These are terms on the customer's Metronome invoice and order form, not the pricing that the customer configures in Metronome for its own end users.

## Key takeaways

- Metronome pricing combines an annual platform fee with consumption-based charges that begin on the production go-live date; the platform fee is outside the consumption categories.
- An order-form Consumption Commitment is a prepaid, non-refundable minimum against consumption-based platform charges, and unused value expires without refund or credit at the end of the applicable service term.
- For commercial metering, an Event is each discrete JSON object submitted to and accepted by Metronome, while Billings are the total value of invoices generated through Metronome subject to three stated exclusions.
- A Row Exported is any row written to the configured Data Export destination. Incremental tables count new or updated rows per sync, while every row in every full snapshot export counts again.
- Data Export tables are labeled Standard or Premium, but the page warns that not every Premium table may currently be available.

## Commercial pricing boundary

The annual platform fee provides access to the services and does not count toward Percentage of Billings, Events-based, Data Export, or Invoice Row Updates consumption categories. Consumption-based charges accrue only after production go-live. The page does not provide actual fee amounts, unit rates, tiers, included allowances, overage treatment, invoice timing, payment terms, or the consumption categories present in a particular order form. It names Invoice Row Updates as a charge category but does not define how those updates are counted.

The capitalized Consumption Commitment is a commercial term between Metronome and the organization buying its services. This page does not describe the separate credit and commit objects that a Metronome customer can configure for its own customers, nor does it define application priority, ledgers, access schedules, or invoice schedules for those objects.

## Event and Billings boundaries

An Event is counted at the accepted JSON-object boundary of the ingestion API. The examples of an API call, storage measurement, data transfer, or another billable action illustrate what one submitted event may represent; they do not establish that Metronome observes or counts those underlying actions without an accepted event object. The page does not state how rejected, retried, or duplicate submissions affect commercial event counts.

Billings include the total value of invoices generated through Metronome whether they are invoiced automatically or manually. The page excludes three cases: current-period finalized invoices voided before Metronome invoices the customer, non-production drafts used for testing or demonstration, and zero-dollar invoices used for free-trial-credit tracking. It does not define currency conversion or aggregation, tax treatment, discounts, credits, refunds, partial voids, or treatment outside those exclusions.

## Data Export row accounting

Data Export continuously sends Metronome billing and usage data to a configured warehouse or object-storage destination. One Row Exported is one written row across any schema table. Incremental tables count only rows that are new or updated in a sync cycle; snapshot tables re-export the full table, so each row counts in each cycle even if it was exported before.

The Standard category lists contract, contract-modification, contract-pricing, payment, alert, finalized-invoice, customer, event, and core-entity tables. The Premium category lists draft invoices and line items, draft and finalized breakdown tables, and finalized and draft Rated Events. The page explicitly says some Premium tables may not currently be available and directs readers to a Metronome representative for current availability; it does not specify entitlements, prices, table-level rollout status, destinations, cadence, freshness, or delivery guarantees.

## Unknowns

- Exact annual and consumption fees, unit definitions beyond Events and exported rows, included volumes, thresholds, and rate tiers.
- Which consumption categories and commitments apply to a specific customer or order form.
- How Percentage of Billings and Invoice Row Updates are calculated beyond the Billings definition and the category name.
- How duplicate, rejected, retried, corrected, or backfilled activity affects Metronome's commercial usage totals.
- Current availability and commercial eligibility for each Premium Data Export table.

## Related

- Company: [[metronome]]
- Concepts: [[metronome-usage-based-billing]], [[metronome-event-ingestion]], [[metronome-invoicing]], [[metronome-reporting-and-analytics]], [[metronome-credits-and-commits]]
- Related sources: [[source-metronome-api-reference-usage-ingest-events]], [[source-metronome-guides-reporting-insights-data-export-overview]], [[source-metronome-guides-reporting-insights-data-export-database-reference]]

## Raw Sources

- [[raw/metronome/guides/platform-configuration/metronome-pricing-model-2026-07-13|2026-07-13 snapshot — Metronome platform pricing, usage metrics, and export-row accounting]]
