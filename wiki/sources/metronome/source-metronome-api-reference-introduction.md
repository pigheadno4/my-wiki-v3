---
title: "Metronome API Reference Introduction"
type: source
date_ingested: 2026-07-30
canonical_url: "https://docs.metronome.com/api-reference/introduction"
original_format: webpage
raw_files:
  - "metronome/api-reference/introduction-2026-07-13.md"
tags: [metronome, api-reference, usage-based-billing, developer-tools]
---

## Overview

This Metronome API Reference introduction is a navigation page for the platform's billing API. It states that Metronome supports accurate invoices and pricing changes, identifies API-wide support for idempotency, pagination, and customer fields, and routes developers to a quickstart, conceptual guide, and four language SDK repositories.

## Key takeaways

- Metronome says its billing platform is intended to support accurate invoices and pricing changes as a business grows.
- The API introduction explicitly names idempotency, pagination, and customer fields as supported API capabilities.
- The page links to SDK repositories for Python, Go, Ruby, and Node.js.
- Its endpoint directory groups the API into Usage, Billable Metrics, Products, Rate cards, Customers, Contracts, Packages, Commits and Credits, Invoices, and Notifications.

## Details

The directory describes **Usage** as sending usage events from an application and **Billable Metrics** as converting raw usage events into invoice quantities. **Products** define invoice line items, while **Rate cards** set base prices.

For customer and commercial configuration, **Customers** represent customer relationships, **Contracts** define invoice behavior for a customer, and **Packages** are reusable, time-relative sets of contract terms. **Commits and Credits** modify invoice amounts.

The remaining directory entries describe **Invoices** as a set of charges for one billing cycle and **Notifications** as powering workflows from Metronome state. The page also points readers to the API Quickstart and How Metronome Works, but does not reproduce either guide's content.

> [!info] Source boundary
> This is an API directory, not an endpoint specification. It does not provide HTTP methods, request or response schemas, authentication requirements, rate limits, pagination parameter semantics, idempotency retention, customer-field definitions, SDK version support, or notification-delivery behavior. No numeric limits, field-level requirements, warnings, or contradictions are stated on this page; implementation details remain in the linked endpoint and guide pages.

## Related

- Company: [[metronome]]
- Concepts: [[metronome-usage-based-billing]], [[metronome-event-ingestion]], [[metronome-billable-metrics]], [[metronome-products-and-rate-cards]], [[metronome-customers-and-contracts]], [[metronome-credits-and-commits]], [[metronome-invoicing]]
- Related sources: [[source-metronome-api-reference-idempotency]], [[source-metronome-api-reference-pagination]], [[source-metronome-api-reference-customers-create-a-customer]], [[source-metronome-api-reference-usage-ingest-events]], [[source-metronome-api-reference-contracts-create-a-contract]], [[source-metronome-guides-get-started-developer-sdks]]

## Raw Sources

- [[raw/metronome/api-reference/introduction-2026-07-13|2026-07-13 snapshot — Metronome API Reference introduction]]
