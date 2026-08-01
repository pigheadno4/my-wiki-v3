---
title: "Configure Avalara AvaTax with Metronome and Stripe"
type: source
date_ingested: 2026-08-01
original_format: webpage
canonical_url: "https://docs.metronome.com/integrations/tax-integrations/avalara"
raw_files:
  - "metronome/integrations/tax-integrations/avalara-2026-07-13.md"
tags: [metronome, stripe, avalara, avatax, tax-integration, invoicing]
---

## Overview

This guide configures Avalara AvaTax for invoices that Metronome delivers through Stripe. Avalara is not connected directly to Metronome: its Stripe Marketplace app uses Stripe's third-party tax-app framework, while Metronome supplies line-item tax-code metadata and keeps the Stripe invoice in draft for tax calculation before finalization.

## Key takeaways

- Install and connect the Avalara AvaTax app in Stripe, select Avalara as the tax provider, enable automatic tax, complete applicable tax registrations, and connect the Stripe account to Metronome.
- Every Metronome customer must be linked to a Stripe customer that has an `address` and is marked Taxable; the address determines jurisdiction, and a missing address causes tax application to fail.
- Create a case-sensitive Metronome Product custom field named `TaxCode`, populate it with Avalara codes, and map `ContractProduct.TaxCode` to `invoiceitem.metadata.TaxCode`.
- Turn **Leave invoices as drafts** on. Avalara requires the Stripe invoice to remain a draft while it calculates and applies tax before finalization.
- Avalara determines the rate from the customer address and line-item tax code. Missing codes receive a default rate and can be misclassified; Avalara support owns unresolved rate-accuracy questions.

## Responsibility and prerequisites

Metronome remains the usage-billing and invoice-origin system and passes configured `TaxCode` metadata into the Stripe invoice. Stripe is the invoice provider and hosts the Avalara app and third-party tax-app framework. Avalara calculates tax from the Stripe customer location and line-item classification; the source directs unresolved rate-accuracy issues to Avalara support.

The setup requires an installed AvaTax app connected to an Avalara account, Avalara selected under **Settings > Tax > Integrations**, **Use automatic tax** enabled, and registrations completed in applicable sales-tax, VAT, and GST jurisdictions. The Stripe account must be connected to Metronome, each Metronome customer must be linked to a Stripe customer ID, and each Stripe customer must have an `address` and Taxable status.

The phrase **Use automatic tax** is a Stripe setting used by the third-party app framework here; it does not make Avalara Stripe's native Stripe Tax calculation engine or product. The existing Stripe Tax guide documents Stripe's own tax engine and a different product mapping.

## Tax-code metadata mapping

Create a Product custom field named exactly `TaxCode` and assign each product its Avalara tax code. The documented entity mapping is:

| Stripe vendor entity | Stripe vendor key | Metronome entity | Metronome key |
| --- | --- | --- | --- |
| `invoiceitem.metadata` | `TaxCode` | `ContractProduct` | `TaxCode` |

The setup prose names the custom-field entity **Product**, while the mapping row names **ContractProduct**. This matches the same terminology split documented by the Stripe Tax source but is not reconciled here; verify the mapping context rather than assuming those are interchangeable API entities.

If metadata lacks `TaxCode`, the guide first says standard state sales tax applies for the customer's jurisdiction and later describes Avalara applying a default rate that may misclassify the item. These statements support explicit codes as the safe configuration, but do not define the default code, rate, or behavior outside state-sales-tax contexts.

## Draft invoice flow

Set **Leave invoices as drafts** to on in the Metronome Stripe integration settings. The documented test generates an invoice in Metronome, inspects the draft in Stripe, and checks that tax line items appear on the finalized Stripe invoice after Avalara processes it.

This is provider-specific behavior: the existing Stripe Tax guide generally recommends not retaining drafts when tax should calculate on sync, whereas Avalara requires the draft interval to calculate before finalization. The sources do not conflict because they describe different tax engines. This Avalara page does not identify who or what finalizes the invoice, how long processing takes, how failures are retried, or how a draft without tax is prevented from finalizing.

## Testing and troubleshooting

Test with a Metronome sandbox connected to a Stripe sandbox, a linked Stripe customer with a valid address, and an invoice generated from Metronome. If tax is missing or the invoice fails, check customer location data, Taxable status, the draft-invoice setting, the saved entity mapping, product `TaxCode` values, and Stripe's default tax behavior. Escalate setup issues to the Metronome representative and rate-accuracy issues to Avalara support.

A 0% rate is not necessarily an error: the guide notes that some products, including SaaS in some states, can be exempt. The source does not document exemption-certificate handling, tax-registration lifecycle, address-validation rules, rounding, inclusive versus exclusive default behavior, invoice-finalization ownership, payment collection, refunds, credit notes, filing, remittance, reconciliation, webhook behavior, retry semantics, or historical correction.

## Related

- Companies: [[metronome]], [[stripe]]
- Concepts: [[metronome-invoicing]], [[metronome-integrations]], [[stripe-tax]]
- Related sources: [[source-metronome-integrations-invoice-integrations-stripe]], [[source-metronome-integrations-tax-integrations-stripe-tax]]

## Raw Sources

- [[raw/metronome/integrations/tax-integrations/avalara-2026-07-13|2026-07-13 snapshot — Avalara AvaTax setup, metadata mapping, draft-invoice requirement, and responsibility boundaries]]
