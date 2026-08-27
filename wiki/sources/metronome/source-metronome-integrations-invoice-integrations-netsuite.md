---
title: "Metronome NetSuite Integration"
type: source
date_ingested: 2026-08-27
canonical_url: "https://docs.metronome.com/integrations/invoice-integrations/netsuite.md"
original_format: webpage
raw_files:
  - "metronome/integrations/invoice-integrations/netsuite-2026-07-13.md"
tags: [metronome, netsuite, invoicing, revenue-recognition, payments, erp, integrations]
---

## Overview

This guide documents Metronome's Public Beta NetSuite integration for two contract-routed outcomes: sending finalized invoices to NetSuite for billing, or sending invoices and available payment state to NetSuite as a revenue system when another provider performs billing. It defines the principal configuration layers, product and customer identity mappings, state and recovery surfaces, and the limits that must be checked before production use.

## Query-critical facts

- The integration is Public Beta and may introduce breaking changes before general availability. Custom currencies and account hierarchy are explicitly unsupported; inventory items that require a location are also unsupported, and NetSuite invoice-line `amount`, `quantity`, and `total` fields must be writable. Metronome directs clients to validate the full flow in a NetSuite sandbox. The page states support for up to 25,000 arrears invoices per month and warns that higher volume may sync more slowly; initial object indexing can itself take up to an hour.
- Billing and revenue-system configurations have different responsibility boundaries. With NetSuite as `customer_billing_configuration`, Metronome sends the invoice after finalization and NetSuite handles distribution, tax calculation, and payment collection. With NetSuite as `revenue_system_configuration`, billing occurs elsewhere; Metronome sends the invoice after a payment attempt and creates the NetSuite payment object when payment succeeds. A failed first payment can leave the NetSuite invoice `OPEN`, followed by a later retroactive `PAID` update after a successful reattempt.
- Product identity is mapped from a Metronome product custom field, such as `netsuite_item_internal_id`, to the internal NetSuite invoice-item ID; many Metronome products may map to one NetSuite item. For prepaid consumption represented by a zero-dollar invoice, negative commit-burn lines require a separate NetSuite Commit Application item and mapping so purchase and consumption can receive different revenue treatment. A mismatch in revenue treatment among invoice items causes the invoice to fail to send.
- Customer-level configuration does not route invoices by itself. A customer may have several billing or revenue-system configurations, and the relevant configuration ID must be selected on the contract. The `netsuite_customer_id` identifies the external customer, while `delivery_method_id`, `billing_provider_configuration_id`, and `revenue_system_configuration_id` occupy distinct configuration and selection layers and should not be conflated.
- Billing-mode sync state appears under `external_invoice`, including the created NetSuite invoice ID, `external_status`, and provider error. Revenue-mode sync state appears under `revenue_system_invoices`, including provider, external entity identity, `sync_status`, and error message. The guide names `invoice.invoice_sync_status` for invoice-sync outcomes and `payment.payment_status_sync` for payment-object sync outcomes. A corrected item mapping can be followed by a manual UI **Send to NetSuite** reattempt; the page does not define a general automatic retry contract.
- NetSuite owns tax calculation through the client's chosen NetSuite tax integration. Metronome neither calculates nor sends tax amounts to NetSuite, and tax is not synchronized back to Metronome. Optional case-sensitive NetSuite invoice fields `metronome_invoice_id`, `metronome_contract_id`, and `metronome_customer_id` preserve cross-system identifiers for reconciliation; their presence supports matching, not proof that accounting or reconciliation completed.

## Material boundaries

- Connection setup, an Active Integrations row, returned IDs, `SUCCEEDED`, `FINALIZED`, or `PAID`-like states are Metronome-documented observations, not complete guarantees of NetSuite configuration compatibility, external acceptance, distribution, customer delivery, collection, payment finality, tax correctness, settlement, revenue posting, or reconciliation. Metronome does not adapt the integration for instance-specific NetSuite customizations; the client owns required compatibility changes and sandbox validation.
- The stated one-hour indexing and status-update timing and the 25,000-arrears-invoices monthly throughput figure are planning boundaries, not service-level or completeness guarantees. The guide does not define queue ordering, exactly-once behavior, automatic retries, terminality, partial-failure recovery, concurrency, replay, or a reconciliation procedure after ambiguous outcomes.
- The guide's POST examples remain subject to the separate [[metronome-api-idempotency|API-wide `Idempotency-Key` authority]]. This page adds no endpoint-specific guarantee for retries without a key, an expired key, concurrency, cached errors, or ambiguous failure recovery. The UI invoice-sync reattempt is a downstream recovery action and must not be treated as the API-wide POST idempotency contract.
- Several code blocks are illustrative rather than copy-ready endpoint authority: the customer payload contains malformed JSON, the block described as contract creation calls `/v1/customers`, and invoice-read examples also call `/v1/customers`. Use the dedicated customer, contract, invoice, and configuration API references for current methods and schemas; do not infer that the displayed routes or example field requiredness are normative.

## Raw-detail coverage map

Use the raw page for the full Public Beta and compatibility checklist; sandbox, throughput, customization, and initial-indexing notes; UI connection and credential workflow; product and Commit Application mapping steps; customer billing and revenue-system configuration payloads; the complete PLG and SLG contract examples; tax flow; billing-mode and revenue-mode invoice-state examples; invoice and payment webhook payload examples; failure objects and manual resend walkthrough; reconciliation custom-field IDs; and the zero-dollar-invoice control. Dedicated API and webhook sources remain authoritative for complete schemas, authentication, transport, signing, retry, ordering, idempotency, and recovery behavior.

## Related

- Company: [[metronome]]
- Primary concepts: [[metronome-integrations]], [[metronome-invoicing]], [[metronome-customers-and-contracts]]
- Supporting concepts: [[metronome-products-and-rate-cards]], [[metronome-custom-fields]], [[metronome-credits-and-commits]], [[metronome-webhooks]], [[metronome-reporting-and-analytics]], [[metronome-currencies-and-custom-pricing-units]]
- Related source: [[source-metronome-api-reference-idempotency]]

## Raw Sources

- [[raw/metronome/integrations/invoice-integrations/netsuite-2026-07-13|2026-07-13 snapshot - Public Beta scope, NetSuite mappings, contract routing, invoice and payment state, recovery, tax, and reconciliation boundaries]]
