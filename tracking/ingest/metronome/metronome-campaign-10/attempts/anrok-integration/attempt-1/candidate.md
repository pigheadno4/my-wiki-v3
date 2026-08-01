---
title: "Configure Anrok Tax with Metronome and Stripe"
type: source
date_ingested: 2026-08-01
original_format: webpage
canonical_url: "https://docs.metronome.com/integrations/tax-integrations/anrok"
raw_files:
  - "metronome/integrations/tax-integrations/anrok-2026-07-13.md"
tags: [metronome, anrok, stripe, tax-integration, invoicing]
---

## Overview

This guide configures Anrok for tax calculation and compliance on invoices that Metronome sends through its native Stripe invoice integration. In the primary documented path, Anrok is selected as Stripe's third-party automatic-tax provider through the Anrok Stripe app; it is not Stripe's native tax engine. The guide also describes a separate hybrid mode in which Stripe Tax calculates tax and Anrok consumes Stripe transaction data for compliance, filing, and reporting.

## Key takeaways

- The Anrok app must be installed and connected in Stripe, selected under Stripe's tax integrations, and used with automatic tax enabled. Applicable sales-tax, VAT, and GST registrations remain prerequisites.
- Metronome must already be connected to Stripe, each Metronome customer must be linked to a Stripe customer, and Metronome must enable tax application after setup. Each Stripe customer needs an `address` and Taxable status; the guide says a missing address causes tax application to fail.
- Anrok classifies each invoice line from its Stripe product. Metronome stores the corresponding product ID in a Product custom field named `stripe_product_id` and maps `ContractProduct.stripe_product_id` to `invoiceitem.price.product`.
- Explicit Stripe product tax codes are recommended for accuracy, although this guide says Anrok falls back to a default product classification when one is absent. That fallback is Anrok-specific and does not revise the separate Stripe Tax guide's native-engine requirements.
- Arrears invoices can calculate Anrok tax inline through the Stripe app without requiring the invoice to remain a draft. Threshold billing instead sets `tax_type: "STRIPE"` and `payment_type: "INVOICE"` in `payment_gate_config`.
- A finalized Stripe invoice can be checked for `automatic_tax.enabled: true`, `provider: "anrok"`, and `status: "complete"`; the sample also shows `liability.type: "self"`, but this guide does not define that field's legal or operational semantics.

## Responsibility and provider modes

Metronome owns the upstream Stripe connection, customer linkage, Product custom field, entity mapping, invoice creation path, and account-level enablement coordinated through a Metronome representative. Stripe hosts the Anrok app and integration selection, customer address and Taxable setting, Stripe products and tax codes, default tax behavior, and the invoice object used for verification. In the primary mode, Anrok calculates tax and handles compliance instead of Stripe's native engine.

The FAQ documents a distinct coexistence mode: Stripe Tax performs the calculation while Anrok handles compliance, filing, and reporting by picking up transaction data from Stripe. This should not be collapsed into the primary Anrok-calculation path or treated as evidence that both engines calculate the same invoice simultaneously. The page does not define transaction-transfer timing, completeness, reconciliation, correction, filing cadence, remittance, or failure handling for the compliance-only path.

## Customer and product mapping

Each Stripe customer must have a valid `address`, which determines tax jurisdiction, and must be marked Taxable. Missing customer location or an incomplete Metronome mapping are the guide's most common explanations for an invoice failing or finalizing without tax. If both checks pass and tax is still absent, the documented escalation is to a Metronome representative; no automatic retry, fallback rate, or retroactive repair flow is specified.

Anrok determines line-item tax treatment from the Stripe product. The guide recommends an explicit tax code on every Stripe product, while documenting an Anrok default-classification fallback when no tax code exists. Each Metronome Product receives a `stripe_product_id` value for the corresponding Stripe product, and the Stripe mapping is:

| Stripe vendor entity | Stripe vendor key | Metronome entity | Metronome key |
| --- | --- | --- | --- |
| `invoiceitem.price` | `product` | `ContractProduct` | `stripe_product_id` |

> [!warning] Documentation ambiguity
> The setup step creates `stripe_product_id` on the Metronome **Product** entity, but the mapping table names the source entity `ContractProduct`. This is the same unresolved terminology mismatch recorded by the separate Stripe Tax guide; verify the mapping context rather than assuming the two entity labels are interchangeable.

## Invoice flow and verification

For end-of-period arrears invoices, Anrok calculates tax inline through the Stripe app, and the guide says **Leave invoices as drafts** need not be enabled. For prepaid-balance and spend-threshold billing, `payment_gate_config` uses `tax_type: "STRIPE"` and `payment_type: "INVOICE"`. Here `STRIPE` is the documented Metronome configuration literal for the Stripe invoice path; it must not be read as proof that Stripe's native tax engine, rather than Anrok, performs the calculation.

Testing uses a Metronome sandbox connected to Stripe test mode. Generate and finalize an invoice, confirm that tax line items appear, and inspect `automatic_tax` on the Stripe invoice. The sample's `provider: "anrok"` distinguishes an active Anrok-calculation path; `enabled: false` or `provider: null` indicates that the integration is not active according to this guide. The Stripe dashboard also needs a default tax behavior, but this page does not define its allowed values or whether prices are inclusive or exclusive.

## Contradictions and unknowns

No direct contradiction with the existing native Stripe Tax or Stripe invoice-integration sources was found. The shared customer-address, product-ID mapping, finalization, and threshold configuration reflect the same Stripe invoice transport, while calculation responsibility differs by selected provider. The Anrok fallback classification is provider-specific, and the hybrid FAQ is a separate operating mode, so neither should overwrite native Stripe Tax behavior.

The guide does not specify supported jurisdictions, currencies, product classifications, tax rates, exemptions, inclusive-versus-exclusive defaults, refund or credit-note handling, transaction-sync guarantees, filing or remittance mechanics, retry behavior, or ownership of corrections after finalization. It also does not define `liability.type: "self"`; no merchant-of-record or legal-liability conclusion should be inferred from the sample alone.

## Related

- Companies: [[metronome]], [[stripe]]
- Concepts: [[metronome-integrations]], [[metronome-invoicing]], [[stripe-tax]]
- Related sources: [[source-metronome-integrations-tax-integrations-stripe-tax]], [[source-metronome-integrations-invoice-integrations-stripe]], [[source-stripe-billing-taxes-collect]]

## Raw Sources

- [[raw/metronome/integrations/tax-integrations/anrok-2026-07-13|2026-07-13 snapshot — Anrok tax-provider setup, Stripe product mapping, invoice flow, and hybrid compliance mode]]
