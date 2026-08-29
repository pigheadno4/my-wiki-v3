---
title: "Configure Anrok Tax with Metronome and Stripe"
type: source
date_ingested: 2026-08-29
original_format: webpage
canonical_url: "https://docs.metronome.com/integrations/tax-integrations/anrok"
raw_files:
  - "metronome/integrations/tax-integrations/anrok-2026-08-28.md"
  - "metronome/integrations/tax-integrations/anrok-2026-07-13.md"
tags: [metronome, anrok, stripe, tax-integration, invoicing]
---

## Overview

This guide configures Anrok as the tax calculator and compliance platform for invoices that Metronome sends through Stripe. Anrok participates through its Stripe app and Stripe's third-party tax-provider setting rather than through a direct Metronome integration or Stripe's native tax engine. A separate documented mode keeps Stripe Tax as calculator while Anrok consumes Stripe transaction data for compliance, filing, and reporting.

## Query-critical facts

- Setup spans all three systems: Stripe hosts the Anrok app, automatic-tax provider selection, customers, addresses, products, tax codes, and invoice object; Metronome holds the Stripe connection, customer linkage, Product custom field, entity mapping, and account-level tax enablement; Anrok calculates tax and handles compliance in the primary path.
- Each Stripe customer needs a Customer `address`, which the guide says determines tax jurisdiction, and must be marked Taxable. The guide explicitly says a missing address causes tax application to fail.
- Anrok determines line-item tax treatment from the Stripe product. Each Metronome Product stores the corresponding Stripe product ID in `stripe_product_id`, mapped from `ContractProduct.stripe_product_id` to `invoiceitem.price.product`; explicit Stripe product tax codes are recommended, while Anrok falls back to a default product classification if one is absent.
- For arrears invoices, Anrok calculates tax inline through the Stripe app and does not require **Leave invoices as drafts**. For prepaid-balance and spend-threshold billing, the guide requires `tax_type: "STRIPE"` and `payment_type: "INVOICE"` in `payment_gate_config` and routes the exact payload to the Stripe Tax threshold documentation.
- Testing is scoped to a Metronome sandbox connected to Stripe test mode. After invoice generation and finalization, the Stripe invoice should show tax line items and an `automatic_tax` object with `enabled: true`, `provider: "anrok"`, and `status: "complete"`; these observations are verification signals, not guarantees of filing, remittance, settlement, or reconciliation.
- The FAQ's coexistence mode is distinct: Stripe Tax performs calculation and Anrok picks up Stripe transaction data for compliance, filing, and reporting. The page does not establish that both engines calculate the same invoice.

## Responsibility, failure, and recovery boundaries

Metronome documents how to connect and map the systems and now routes account enablement and unresolved setup problems through the Metronome support portal. Stripe is the documented location for the installed app, tax-provider selection, customer address and Taxable state, product tax codes, default tax behavior, test mode, and invoice inspection. Anrok is the selected calculator and compliance actor in the primary mode, but this Metronome guide is not complete authority for Anrok's external service behavior.

The guide names a missing Stripe Customer Address and an incomplete Metronome entity mapping as the common causes of failed invoices or invoices finalized without tax. If those checks pass and tax is still absent, the documented recovery is support escalation. It specifies no automatic retry, fallback tax rate, correction of an already-finalized invoice, or reconciliation procedure. `automatic_tax.enabled: false` or `provider: null` indicates an inactive integration according to the guide, but the page does not define propagation timing, transient states, or a taxless-finalization safeguard.

> [!warning] Documentation ambiguity
> The setup prose creates `stripe_product_id` on the Metronome **Product** entity, while the mapping table names `ContractProduct` as the Metronome entity. The guide does not reconcile those labels; do not assume they are interchangeable API entities.

The page does not define supported jurisdictions, currencies, exemptions, inclusive-versus-exclusive behavior, refunds, credit notes, filing cadence, remittance, transaction-transfer completeness, retries, correction ownership, or the legal or operational meaning of the sample's `liability.type: "self"`.

## Raw-detail coverage map

| Raw detail category | Exact raw coverage |
| --- | --- |
| Prerequisites and enablement | Anrok app installation, Stripe tax-provider and automatic-tax settings, registrations, Metronome-to-Stripe connection, customer linkage, address and Taxable requirements, and Metronome support-portal enablement |
| Product identity and classification | Stripe products and tax codes, Anrok default-classification fallback, `stripe_product_id` custom field, exact entity-mapping row, and current **Developer > Integrations > Stripe > Edit Mapping** UI path |
| Invoice variants | Arrears inline calculation and the two threshold-billing configuration values, with the exact payload delegated to the linked Stripe Tax guide |
| Test and troubleshooting | Metronome sandbox plus Stripe test mode, invoice-generation and tax-line checks, missing-address and incomplete-mapping diagnosis, and support escalation |
| Provider-mode verification | Complete sample `automatic_tax` object, inactive-value checks, Stripe Tax plus Anrok compliance-only coexistence, and Stripe default-tax-behavior reminder |

## Related

- Companies: [[metronome]], [[stripe]]
- Primary concepts: [[metronome-integrations]], [[metronome-invoicing]], [[stripe-tax]]
- Related sources: [[source-metronome-integrations-tax-integrations-stripe-tax]], [[source-metronome-integrations-invoice-integrations-stripe]], [[source-stripe-billing-taxes-collect]]

## Raw Sources

- [[raw/metronome/integrations/tax-integrations/anrok-2026-08-28|2026-08-28 snapshot — refreshed support-portal routing and Stripe mapping navigation, plus Anrok tax setup, invoice flow, troubleshooting, and provider verification]]
- [[raw/metronome/integrations/tax-integrations/anrok-2026-07-13|2026-07-13 snapshot — prior Anrok tax-provider setup, product mapping, invoice flow, and hybrid compliance mode]]
