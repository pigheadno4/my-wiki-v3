---
title: "Configure Stripe Tax with Metronome"
type: source
date_ingested: 2026-08-28
canonical_url: "https://docs.metronome.com/integrations/tax-integrations/stripe-tax"
original_format: webpage
raw_files:
  - "metronome/integrations/tax-integrations/stripe-tax-2026-08-28.md"
  - "metronome/integrations/tax-integrations/stripe-tax-2026-07-13.md"
tags: [metronome, stripe, stripe-tax, tax-integration, invoicing]
---

## Overview

This guide configures Stripe Tax as the tax-calculation layer for invoices that Metronome creates through its native Stripe invoice integration. Metronome supplies customer and product mappings and creates the Stripe invoice; Stripe Tax calculates and applies sales tax when Stripe finalizes that invoice. The page covers Stripe's own tax product, not Anrok or Avalara connected through Stripe's third-party tax-app framework.

## Query-critical facts

- Activate Stripe Tax and complete applicable sales-tax, VAT, and GST registrations in Stripe before using this path. Metronome's Stripe invoice connection and each customer-to-Stripe-customer link must already exist, and Metronome support must enable tax application on the account after initial setup.
- Each linked Stripe customer needs its `address` object populated and must be marked Taxable. The address determines tax jurisdiction, and a missing Customer Address causes tax application to fail.
- Stripe Tax derives classification from the Stripe product attached to each invoice line. Metronome stores that ID in a Product custom field named `stripe_product_id` and maps `ContractProduct.stripe_product_id` to `invoiceitem.price.product`.
- Multiple Metronome products may reuse one Stripe product when they share a tax code. Do not enable `enforce_uniqueness` on `stripe_product_id`, because that reuse is intentional and uniqueness cannot be undone without archiving and recreating the field. If a Stripe product has no tax code, Stripe Tax falls back to the account's preset product tax code.
- Account-level tax enablement covers arrears invoices but not prepaid-balance thresholds, spend thresholds, or one-off payment-gated commits. Those flows must explicitly set `payment_gate_type: "STRIPE"`, `tax_type: "STRIPE"`, and `stripe_config.payment_type: "INVOICE"`.
- Stripe automatic tax calculates inline when the invoice is finalized. Keeping Stripe invoices as drafts defers calculation until manual finalization; the collection method determines payment behavior after finalization and is independent of whether tax applies.

## Configuration and mapping

Create the `stripe_product_id` custom field on Metronome's **Product** entity, populate it with the matching Stripe product ID, and configure the mapping under **Developer → Integrations → Stripe → Edit Mapping**:

| Stripe vendor entity | Stripe vendor key | Metronome entity | Metronome key |
| --- | --- | --- | --- |
| `invoiceitem.price` | `product` | `ContractProduct` | `stripe_product_id` |

Optional mappings can send Product custom fields to `invoiceitem.metadata.*` and Customer custom fields to `invoice.metadata.*`; they are not prerequisites for native Stripe Tax.

> [!warning] Documentation ambiguity
> The guide creates `stripe_product_id` on Metronome's **Product** entity but names `ContractProduct` in the required mapping row. It does not reconcile those labels, so verify the mapping context rather than assuming they are interchangeable API entities.

## Invoice lifecycle and failure boundaries

For a sandbox check, create a Metronome test customer linked to a valid Stripe customer, generate an invoice, and inspect the corresponding Stripe invoice for calculated tax. This verifies the observed test invoice only; it does not establish external payment, settlement, filing, remittance, or end-to-end reconciliation. Stripe's tax documentation remains authoritative for Stripe's tax-code and default-tax-behavior semantics, while this Metronome guide is configuration guidance rather than legal, accounting, or tax-registration advice.

Both collection methods support tax but produce different post-finalization behavior. `charge_automatically` requires a default Stripe payment method before finalization or payment fails; `send_invoice` emails payment instructions and requires `days_until_due`. Under **Developer → Integrations → Stripe → Settings**, turning **Leave invoices as drafts** off lets Metronome finalize synced invoices so Stripe calculates tax automatically; leaving it on requires manual finalization in Stripe.

If tax is absent, verify Stripe Tax enablement, customer address and Taxable status, saved entity mapping, populated `stripe_product_id` values, valid Stripe product tax codes, and a selected default tax behavior. Missing address explicitly causes tax application failure. The troubleshooting section says incomplete location or mapping can accompany an invoice failure or finalization without tax, but it does not assign one deterministic outcome to each cause. If checks pass, use the Metronome support portal to inspect account configuration. The guide defines no automatic fallback rate, retry schedule, retroactive repair, or reconciliation process.

## Raw-detail coverage map

- **Prerequisites and UI setup:** Stripe activation and registrations, customer address and Taxable status, account enablement through Metronome support, and current Stripe and Metronome menu paths are in the latest raw page.
- **Mapping detail:** the exact required entity-mapping row, optional invoice and line-item metadata mappings, custom-field example value, uniqueness warning, tax-code fallback, and FAQ are in the latest raw page.
- **Threshold payloads:** complete prepaid-balance and spend-threshold JSON examples, numeric example amounts, and the one-off edit-contract statement are in the latest raw page; the examples do not specify currency.
- **Testing and troubleshooting:** the sandbox walkthrough, diagnostic checklist, collection-method email and payment behavior, draft-finalization preference, support escalation, and default-tax-behavior reminder are in the latest raw page.

## Related

- Companies: [[metronome]], [[stripe]]
- Primary concepts: [[stripe-tax]], [[metronome-integrations]], [[metronome-invoicing]]
- Supporting concepts: [[metronome-products-and-rate-cards]], [[metronome-custom-fields]], [[metronome-credits-and-commits]], [[metronome-spend-threshold-billing]]
- Related sources: [[source-metronome-integrations-invoice-integrations-stripe]], [[source-stripe-billing-taxes-collect]]

## Raw Sources

- [[raw/metronome/integrations/tax-integrations/stripe-tax-2026-08-28|2026-08-28 snapshot — current Stripe Tax prerequisites, mappings, threshold configuration, finalization, and troubleshooting]]
- [[raw/metronome/integrations/tax-integrations/stripe-tax-2026-07-13|2026-07-13 snapshot — prior Stripe Tax setup, mapping, threshold billing, and invoice finalization]]
