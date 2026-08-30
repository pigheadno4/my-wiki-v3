---
title: "Configure Avalara AvaTax with Metronome and Stripe"
type: source
date_ingested: 2026-08-30
original_format: webpage
canonical_url: "https://docs.metronome.com/integrations/tax-integrations/avalara"
raw_files:
  - "metronome/integrations/tax-integrations/avalara-2026-08-28.md"
  - "metronome/integrations/tax-integrations/avalara-2026-07-13.md"
tags: [metronome, stripe, avalara, avatax, tax-integration, invoicing]
---

## Overview

This guide configures Avalara AvaTax for invoices that Metronome generates through Stripe. Avalara does not connect directly to Metronome in this flow: its Stripe Marketplace app uses Stripe's third-party tax-app framework for inline calculation, while Metronome supplies line-item tax metadata and leaves the Stripe invoice in draft for tax processing before finalization.

## Query-critical facts

- Setup spans three systems: install and connect the AvaTax app in Stripe, select Avalara as the tax calculation provider, turn **Use automatic tax** on, complete applicable sales-tax, VAT, and GST registrations, connect Stripe to Metronome, and link each Metronome customer to a Stripe customer ID.
- Each linked Stripe customer must have the Customer `address` object and be marked Taxable. The guide says the address determines tax jurisdiction and that omitting it causes tax application to fail.
- Create a case-sensitive Metronome Product custom field named `TaxCode`, assign each product an Avalara tax code, and map `ContractProduct.TaxCode` to `invoiceitem.metadata.TaxCode`. The refreshed UI path is **Developer > Integrations > Stripe > Edit Mapping**.
- Turn **Leave invoices as drafts** on under **Developer > Integrations > Stripe > Settings**. The guide says Avalara needs the draft interval to calculate and apply tax before finalization.
- The documented test uses a Metronome sandbox connected to a Stripe Sandbox, generates the invoice in Metronome, inspects it as a Stripe draft, and confirms tax line items on the finalized Stripe invoice after Avalara processing. These observations are a test procedure, not a finalization, delivery, payment, filing, or reconciliation guarantee.

## Responsibility, failure, and correction boundaries

Metronome documents the Stripe connection, customer linkage, `TaxCode` field and mapping, draft-invoice setting, and sandbox test. Stripe hosts the AvaTax app, tax-provider selection, customer location and Taxable state, invoice, and default tax behavior. The guide assigns rate determination to Avalara using the customer address and line-item tax code, and directs unresolved rate-accuracy issues to Avalara support; it directs otherwise unresolved setup issues to the Metronome support portal. This Metronome page is not complete authority for Avalara's external service behavior.

For invoices that fail or finalize without tax, the guide's recovery sequence is to check customer address and tax location, the draft setting, and product `TaxCode` mapping, then escalate setup verification. It does not define automatic retry, processing latency, who finalizes the invoice, a safeguard against taxless finalization, correction of an already-finalized invoice, refunds or credit notes, filing or remittance, payment collection, webhook behavior, or reconciliation.

> [!warning] Documentation ambiguities
> The setup prose creates `TaxCode` on the Metronome **Product** entity, while the mapping row names **ContractProduct**; the guide does not reconcile those entity labels. For a missing `TaxCode`, one note says standard state sales tax applies for the customer's jurisdiction, while the FAQ calls the outcome a default tax rate that may cause incorrect classification. Preserve both source-scoped descriptions rather than inferring a universal fallback code or behavior outside state-sales-tax contexts.

A 0% result is not necessarily an error: the page says some products, including SaaS in some states, may be tax-exempt. That example does not establish the product's legal tax treatment in any jurisdiction; the page routes code verification to Avalara's catalog and unresolved rate accuracy to Avalara.

## Raw-detail coverage map

| Raw detail category | Exact raw coverage |
| --- | --- |
| Prerequisites and external setup | AvaTax app installation, two-dashboard connection verification, Stripe provider and automatic-tax settings, registration links, Metronome connection, customer linkage, address, and Taxable state |
| Product classification and mapping | Exact `TaxCode` casing, Avalara code catalog, Product-to-`ContractProduct` terminology, full entity-mapping row, refreshed Developer UI path, and missing-code statements |
| Invoice flow and testing | Refreshed draft-setting path, draft requirement, Metronome and Stripe sandbox pairing, invoice generation, Stripe draft inspection, and finalized-invoice tax-line check |
| Failure and support routing | Missing location, draft setting, mapping and product-code checks, Metronome support portal, 0% exemption example, Avalara rate-accuracy ownership, and Stripe default tax behavior |

## Related

- Companies: [[metronome]], [[stripe]]
- Primary concepts: [[metronome-integrations]], [[metronome-invoicing]], [[metronome-custom-fields]], [[stripe-tax]]
- Related sources: [[source-metronome-integrations-invoice-integrations-stripe]], [[source-metronome-integrations-tax-integrations-stripe-tax]]

## Raw Sources

- [[raw/metronome/integrations/tax-integrations/avalara-2026-08-28|2026-08-28 snapshot — refreshed Developer navigation and Metronome support-portal routing, plus Avalara setup, mapping, draft-invoice flow, and troubleshooting]]
- [[raw/metronome/integrations/tax-integrations/avalara-2026-07-13|2026-07-13 snapshot — prior Avalara setup, tax-code mapping, draft-invoice requirement, and responsibility boundaries]]
