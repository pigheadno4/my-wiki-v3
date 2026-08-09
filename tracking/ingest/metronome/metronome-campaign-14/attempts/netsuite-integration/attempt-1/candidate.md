---
title: "Metronome NetSuite Integration"
type: source
date_ingested: 2026-08-05
original_format: webpage
canonical_url: "https://docs.metronome.com/integrations/invoice-integrations/netsuite.md"
raw_files:
  - "metronome/integrations/invoice-integrations/netsuite-2026-07-13.md"
tags: [metronome, netsuite, invoicing, revenue-recognition, erp-integration]
---

## Overview

This guide documents Metronome's Public Beta NetSuite integration for two distinct routes: sending finalized invoices to NetSuite for billing, or sending invoices and available payment information to NetSuite while another provider handles billing. It covers compatibility prerequisites, connection and product mapping, customer and contract routing, tax ownership, synchronization state, failures, payments, and optional reconciliation metadata.

## Key takeaways

- The integration is in Public Beta, may introduce breaking changes before general availability, and does not support custom currencies or account hierarchy.
- It targets standard NetSuite configurations: invoice-line `amount`, `quantity`, and `total` must be writable, inventory items requiring a location are unsupported, and clients own instance-specific compatibility changes.
- A customer-level NetSuite billing or revenue-system configuration does not route invoices by itself; the relevant configuration must also be selected on the contract.
- Billing-provider and revenue-system routes use different invoice fields and failure states. Billing-provider failures use `external_invoice.external_status = INVALID_REQUEST_ERROR` and `billing_provider_error`; revenue-system failures use `revenue_system_invoices[].sync_status = FAILED` and `error_message`.
- NetSuite owns tax calculation through a separately configured tax provider. Metronome neither sends tax amounts to NetSuite nor imports the resulting tax back into Metronome.

## Availability and compatibility prerequisites

The guide says the integration is available to all Metronome customers while also labeling it Public Beta and warning that unsupported features and breaking changes remain possible. Custom currencies and account hierarchy are explicitly unsupported. An existing customer-creation source describes revenue-system configuration as feature-flagged, so account-level availability of that particular route should be verified rather than inferred solely from this guide's broader availability statement.

The target NetSuite instance must permit writes to invoice-line `amount`, `quantity`, and `total`. Inventory items that require a location are unsupported. Metronome does not customize the integration for instance-specific configurations; required compatibility changes remain the client's responsibility. The guide recommends validating the complete invoice-sync flow in a NetSuite sandbox before production.

The documented throughput is up to 25,000 arrears invoices per month. Exceeding that volume is described as increasing synchronization delay, not as a rejection threshold or hard maximum. Connection setup requires the NetSuite account ID, installation of Metronome's permissions bundle, and generated NetSuite credentials. Initial object indexing can take up to one hour and can delay the first invoice sync.

## Product and zero-dollar-invoice mapping

Each Metronome product line maps to a NetSuite item ID through a product custom field and the integration's entity-mapping interface. Several Metronome products may map to one NetSuite item. The documented mapping shape is `Invoice.Items: internal_id -> ContractProduct: your key`.

For prepaid-credit consumption represented by zero-dollar invoices, the guide requires a separate NetSuite Commit Application item. A second Metronome product custom field maps negative commit-burn-down lines to that item, allowing purchase and application lines to receive different revenue treatments. However, every item on one NetSuite invoice must share the same revenue treatment; mixing a deferred Commit Application item with usage items that point directly to revenue causes the invoice send to fail.

Metronome sends zero-USD invoices to NetSuite by default, although the connection settings can disable them. Optional case-sensitive NetSuite invoice fields named `metronome_invoice_id`, `metronome_contract_id`, and `metronome_customer_id` receive Metronome identifiers for reconciliation. If those fields are absent, the invoice may still sync, but that associated metadata cannot be synchronized.

## Billing and revenue-system routing

With NetSuite as `customer_billing_configuration`, Metronome sends a finalized invoice to NetSuite, after which NetSuite handles distribution, tax calculation, and payment collection. With NetSuite as `revenue_system_configuration`, another system such as Stripe handles billing, and Metronome sends the invoice and available payment information to NetSuite for revenue operations after payment has been attempted.

Both configurations are created on the customer and then selected on the relevant contract. Because a customer can hold multiple billing and revenue-system configurations, creating a customer-level configuration without assigning its ID to a contract is insufficient to route that contract's invoices or payments.

For the revenue-system route, a failed first payment attempt does not prevent invoice synchronization: the invoice is sent to NetSuite as `OPEN`. If a later payment attempt succeeds, Metronome retroactively updates the NetSuite invoice to `PAID` and creates the payment object. The guide illustrates Stripe billing plus NetSuite revenue recognition for PLG customers and NetSuite billing for SLG customers, but its displayed API examples contain apparent endpoint, JSON-syntax, and identifier irregularities. Verify current customer, configuration-fetch, and contract-create API references before implementing those payloads.

## Tax, invoice state, and failures

NetSuite must be integrated with the client's chosen tax provider for both billing and revenue-recognition routes. Metronome creates the NetSuite invoice, the NetSuite-side integration adds tax, and the calculated tax is not synchronized back to Metronome.

For NetSuite billing, synchronization details appear in `external_invoice`, including the NetSuite invoice ID and `external_status`. NetSuite status changes are reflected back in Metronome with approximately one-hour latency. For the revenue-system route, details instead appear in `revenue_system_invoices`, including the external entity ID, entity type, and `sync_status`. Initial invoice synchronization emits `invoice.invoice_sync_status`, with `sync_type` distinguishing `billing_provider` from `revenue_system`.

A billing-route failure sets `external_status` to `INVALID_REQUEST_ERROR` and records `billing_provider_error`. A revenue-system failure sets `sync_status` to `FAILED` and records `error_message`. The guide's missing-item example is remediated by correcting the product's NetSuite item-ID custom field and manually selecting **Send to NetSuite** in the invoice UI. It does not document automatic invoice-sync retries, retry limits, idempotency, duplicate-invoice prevention, partial-success recovery, or reconciliation after uncertain outcomes.

When Stripe billing succeeds, Metronome stores the Stripe payment-intent ID and invoiced amount, sends the invoice to NetSuite as paid, and creates a linked payment object. Payment-object synchronization emits `payment.payment_status_sync`. When NetSuite performs billing, a payment recorded in NetSuite updates the Metronome invoice to `PAID` after synchronization. This page identifies the event types and object fields but does not define webhook delivery, verification, retry, ordering, or deduplication semantics; the dedicated webhook documentation remains authoritative for those mechanics.

## Public Beta and operational boundaries

The guide does not define a general-availability timeline, compatibility for custom currencies or hierarchy accounts, behavior above the documented monthly volume, synchronization ordering, configuration-change propagation, automatic recovery, deletion handling, conflict resolution, or end-to-end accounting reconciliation. Sandbox validation, monitoring through the UI, API, data export, and webhooks, and verification of the current API schemas remain necessary before production use.

## Related

- Companies: [[metronome]], [[stripe]]
- Concepts: [[metronome-integrations]], [[metronome-invoicing]], [[metronome-customers-and-contracts]], [[metronome-products-and-rate-cards]], [[metronome-webhooks]]
- Related sources: [[source-metronome-integrations-invoice-integrations-stripe]], [[source-metronome-guides-reporting-insights-financial-reporting-revenue-recognition]]

## Raw Sources

- [[raw/metronome/integrations/invoice-integrations/netsuite-2026-07-13|2026-07-13 snapshot — NetSuite prerequisites, routing, mappings, state, and failure boundaries]]
