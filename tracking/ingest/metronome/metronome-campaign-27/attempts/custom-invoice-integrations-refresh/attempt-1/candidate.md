---
title: "Invoice with Other Systems Using a Managed Integration"
type: source
date_ingested: 2026-08-29
original_format: webpage
canonical_url: "https://docs.metronome.com/integrations/invoice-integrations/custom-invoice-integrations"
raw_files:
  - "metronome/integrations/invoice-integrations/custom-invoice-integrations-2026-08-28.md"
  - "metronome/integrations/invoice-integrations/custom-invoice-integrations-2026-07-13.md"
tags: [metronome, invoicing, managed-integrations, billing-integrations, quickbooks]
---

## Overview

This guide describes invoicing through systems outside Metronome's native integrations. It offers Data Export or a managed integration built with Data Export or Metronome APIs, then uses QuickBooks Online (QBO) to illustrate external setup, identity mapping, finalized-invoice retrieval, transformation, destination creation, and orchestration. The QBO fields and request are a worked example rather than a complete guarantee for QuickBooks or another billing platform.

## Query-critical facts

- The non-native routes are to collaborate with Metronome on a data export or build a managed integration connecting to the selected billing system. The guide directs managed-integration setup questions to `solutions@metronome.com`.
- The implementer prepares the external application's organization, permissions, and credentials; creates or finds external customer and item objects; and stores their identifiers in Metronome custom fields. The QBO example recommends `qbo_item_id` on Product, `qbo_customer_id` on Customer, and optional `qbo_memo_ref` on Contract.
- QBO item identity can be per Metronome product, preserving product-level reporting at the cost of naming and governance, or one generic item, simplifying setup while collapsing downstream revenue detail. These alternatives are QBO example choices, not universal external-system capabilities.
- The recommended API flow listens for `invoice.finalized` after Metronome's grace period, uses the payload's `customer_id` to list `FINALIZED` invoices for the associated billing period, transforms the returned invoice and line-item data, and upserts the destination invoice and lines. The event is not enabled by default; the refreshed page routes enablement to the Metronome support portal. Although the sample payload also contains `invoice_id`, this guide does not document a direct-fetch flow or how to select among several list matches.
- The orchestration layer can run in the implementer's developer environment or a third-party tool. Metronome recommends Workato to teams investigating an IPaaS and describes its public connector as an SDK-like Metronome API wrapper; the guide routes API and connector questions to the support portal.

## Responsibility and recovery boundaries

Metronome supplies the finalized-invoice event and invoice data, while the implementer maps external identities, transforms fields, and performs the downstream upsert; the selected billing system owns its customer, item, and invoice objects. The page does not assign hosting or operational support, nor define webhook verification, delivery ordering or deduplication, list pagination or consistency, destination idempotency, partial-failure recovery, replay, concurrency, rate limits, ongoing object synchronization, or reconciliation. Dedicated webhook and API references remain authoritative for mechanics they establish.

The QBO mapping tells implementers to verify whether amounts are cents or dollars before conversion. It does not define universal currency, rounding, tax, discount, credit, negative-amount, due-date, duplicate-document, invoice-update, payment-collection, refund, credit-memo, accounting-close, or status-synchronization behavior, and it is not authority for external-platform acceptance, payment, settlement, or reconciliation.

## Raw-detail coverage map

- **External setup and identity:** complete Intuit app, Accounting-scope, OAuth, callback, token, Realm ID, customer and item creation, custom-field key, and QBO object-mapping steps are in the latest raw page.
- **Invoice retrieval:** the exact `invoice.finalized` example payload, enablement note, invoice-list curl example, status and billing-period filters, and returned invoice and line-item field list are in the latest raw page.
- **Transformation and creation:** full header and line mapping tables, amount-unit warning, QBO invoice request example, example identifiers, dates, notes, quantities, and prices are in the latest raw page.
- **Orchestration and contacts:** the developer-environment and Workato options, connector positioning, `solutions@metronome.com` managed-integration route, and support-portal routes are in the latest raw page.

## Related

- Company: [[metronome]]
- Primary concepts: [[metronome-integrations]], [[metronome-invoicing]], [[metronome-custom-fields]]
- Supporting concepts: [[metronome-webhooks]], [[metronome-reporting-and-analytics]], [[metronome-products-and-rate-cards]], [[metronome-customers-and-contracts]]
- Related sources: [[source-metronome-guides-reporting-insights-data-export-overview]], [[source-metronome-guides-platform-configuration-setup-webhooks]], [[source-metronome-integrations-platform-integrations-workato-connector]], [[source-metronome-integrations-invoice-integrations-stripe]], [[source-metronome-guides-invoices-overview]]

## Raw Sources

- [[raw/metronome/integrations/invoice-integrations/custom-invoice-integrations-2026-08-28|2026-08-28 snapshot - current managed custom-invoice routes, QuickBooks mapping and finalized-invoice flow, Workato option, and support contacts]]
- [[raw/metronome/integrations/invoice-integrations/custom-invoice-integrations-2026-07-13|2026-07-13 snapshot - prior managed custom-invoice guide using representative-based contact directions]]
