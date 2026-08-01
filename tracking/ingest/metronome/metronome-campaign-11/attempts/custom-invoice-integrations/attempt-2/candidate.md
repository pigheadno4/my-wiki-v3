---
title: "Invoice with Other Systems Using a Managed Integration"
type: source
date_ingested: 2026-08-01
original_format: webpage
canonical_url: "https://docs.metronome.com/integrations/invoice-integrations/custom-invoice-integrations"
raw_files:
  - "metronome/integrations/invoice-integrations/custom-invoice-integrations-2026-07-13.md"
tags: [metronome, invoicing, managed-integrations, billing-integrations, quickbooks]
---

## Overview

This guide describes options for invoicing through systems outside Metronome's native integrations. It presents data exports or a managed integration built on Metronome APIs, then uses QuickBooks Online (QBO) to illustrate external-system prerequisites, object mapping, a finalized-invoice API flow, field transformation, invoice creation, and orchestration choices.

## Key takeaways

- Metronome presents two routes for non-native invoicing: collaborate with Metronome on data exports or build a managed integration using data export or Metronome APIs.
- The QuickBooks example requires the implementer to prepare the external application and OAuth credentials, map or create external customers and items, and store the resulting external identifiers in Metronome custom fields.
- The recommended API flow listens for `invoice.finalized`, queries finalized invoices for the webhook's customer and associated billing period, transforms the returned invoice and line-item data, and upserts the invoice and line items in the downstream system.
- The `invoice.finalized` event is not enabled by default; the page directs clients to contact their Metronome representative to enable it.
- The source offers per-product and single-item QBO mapping strategies with different reporting-detail and governance trade-offs, but it does not define a universal mapping for other billing providers.

## Managed integration model

Metronome says out-of-the-box invoice-platform integrations can require significant customization when they synchronize data without accounting for the full use case and business model. Its managed-integration approach is intended to start from client invoicing requirements. Such an integration can use Data Export or Metronome APIs, and the page directs readers to a Metronome representative for setup information.

The page also says Metronome continues to assess native integrations as it develops support for different business models, pointing to its existing Stripe, NetSuite, and marketplace solutions. That statement does not commit Metronome to a particular new native integration, schedule, feature set, or service level. Nor does the page define whether Metronome, the client, or another party hosts, operates, monitors, or supports a managed integration.

## External-system prerequisites and object ownership

The worked example is QuickBooks-specific, although Metronome says its overall pattern and design decisions apply to other use cases. Before configuring the Metronome side, the implementer checks the selected billing platform's organizational and invoice-creation requirements. For QBO, the documented setup creates an Intuit Developer app with the Accounting scope, records its client ID and client secret, configures an OAuth callback URI, completes OAuth 2.0 for access and refresh tokens, and records the Realm ID identifying the target QBO company.

Customer and item records live in the selected billing system. The recommended Metronome custom fields retain the external references: `qbo_item_id` on a Product, `qbo_customer_id` on a Customer, and optional `qbo_memo_ref` on a Contract. For each Metronome customer, the integration finds or creates a QBO customer and writes the QBO identifier back to Metronome. The source does not define match keys, conflict resolution, ownership of changes after initial mapping, or synchronization when either system's object is renamed, merged, archived, or deleted.

For items, the page offers two strategies. A per-product mapping creates one QBO item per Metronome product and preserves product-level revenue reporting, at the cost of item governance and naming conventions. A single-item mapping sends every line to one generic QBO item, simplifying setup while collapsing downstream revenue detail into one category. These are documented design options for the example, not a rule that all downstream providers expose equivalent customer, item, or reporting objects.

## Finalized-invoice API flow

The recommended flow begins with a webhook endpoint listening for `invoice.finalized`, which the guide says is created after a Metronome invoice finalizes when the grace period ends. The sample payload supplies `customer_id`, `invoice_id`, and `invoice_finalized_date`. The page then uses `customer_id` to query `/listInvoices` for `FINALIZED` invoices in the associated billing period rather than documenting a direct fetch by the payload's `invoice_id`.

The listed response data includes invoice identifiers, status, total, subtotal, issue and service-period timestamps, contract ID, and line items with names, types, quantities, unit prices, totals, product IDs, and other details. The integration parses and transforms that response into the destination format, then upserts the invoice and its line items. In the QBO example, a customer and at least one item must already exist.

This page defines the business sequence but not the delivery guarantees or mutation contract. It does not specify webhook verification, retry, ordering, or deduplication; `/listInvoices` pagination, consistency, or behavior when several finalized invoices share the queried customer and time range; destination idempotency or the key used for an upsert; partial-failure recovery; replay; concurrency; rate limits; or reconciliation after either system changes. The dedicated webhook and API references remain authoritative for mechanics they document.

## QuickBooks transformation example

The sample mapping uses the stored QBO customer identifier for `CustomerRef.value`, the date portion of `issued_at` for `TxnDate` with `end_timestamp` as a fallback when null, a shortened `MTR-`-prefixed invoice UUID for QBO's length-constrained `DocNumber`, and invoice or contract context in private notes and customer-facing memo text. For line items, it maps the selected QBO item, quantity, unit price, total amount, and a composite description. The page explicitly tells the implementer to check whether amounts are represented in cents or dollars and convert when necessary.

These fields and the displayed QBO request are examples, not a complete Metronome or QuickBooks schema. The page does not define currency and rounding rules, tax mapping, discounts, credits, negative amounts, invoice-state changes, due-date precedence, duplicate document-number handling, line-item limits, QBO validation or error responses, or how updates to an existing downstream invoice should be applied. It also does not assign responsibility for payment collection, tax calculation, collections, refunds, credit memos, accounting close, or status synchronization.

## Orchestration boundary

The orchestration layer can run in an existing developer environment or use a third-party tool. Metronome recommends Workato for teams evaluating an integration platform and describes its public Workato connector as an SDK-like wrapper around distinct Metronome API endpoints. The guide does not enumerate connector actions or endpoint coverage here, and it does not establish that Workato supplies the full mapping, state management, retry, reconciliation, security, or operational behavior needed by this QuickBooks example.

## Related

- Company: [[metronome]]
- Concepts: [[metronome-integrations]], [[metronome-invoicing]], [[metronome-webhooks]], [[metronome-reporting-and-analytics]], [[metronome-products-and-rate-cards]]
- Related sources: [[source-metronome-guides-reporting-insights-data-export-overview]], [[source-metronome-guides-platform-configuration-setup-webhooks]], [[source-metronome-integrations-platform-integrations-workato-connector]], [[source-metronome-integrations-invoice-integrations-stripe]], [[source-metronome-guides-invoices-overview]]

## Raw Sources

- [[raw/metronome/integrations/invoice-integrations/custom-invoice-integrations-2026-07-13|2026-07-13 snapshot - managed custom-invoice integration and QuickBooks example]]
