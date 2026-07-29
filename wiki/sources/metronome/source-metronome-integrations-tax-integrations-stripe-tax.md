---
title: "Configure Stripe Tax with Metronome"
type: source
date_ingested: 2026-07-29
canonical_url: "https://docs.metronome.com/integrations/tax-integrations/stripe-tax"
original_format: webpage
raw_files:
  - "metronome/integrations/tax-integrations/stripe-tax-2026-07-13.md"
tags: [metronome, stripe, stripe-tax, tax-integration, invoicing]
---

## Overview

This guide configures Stripe Tax as the tax-calculation layer for invoices that Metronome creates through its native Stripe invoice integration. Metronome supplies customer and product mappings and creates the Stripe invoice; Stripe Tax calculates and applies sales tax when that invoice is finalized. The page is specifically about Stripe's own tax product, not Anrok or Avalara connected through Stripe's third-party tax-app framework.

## Key takeaways

- Stripe Tax must first be activated in Stripe, including tax registrations for the applicable sales-tax, VAT, and GST jurisdictions. The Metronome Stripe invoice connection and customer-to-Stripe-customer links must already exist.
- Each linked Stripe customer needs its `address` object populated and must be marked Taxable. The address determines tax jurisdiction, and a missing Customer Address causes tax application to fail.
- Stripe Tax derives the tax code and rate from the Stripe product attached to each invoice line item. Metronome products carry a `stripe_product_id` custom field that is passed to Stripe through entity mapping.
- Multiple Metronome products may reuse one Stripe product only when they share a tax code. The custom field must not enforce uniqueness because this reuse is intentional and that setting cannot later be undone.
- Account-level tax enablement applies to arrears invoices, but not threshold billing. Prepaid-balance thresholds, spend thresholds, and one-off payment-gated commits require explicit Stripe tax configuration in the API.
- Tax is calculated inline when Stripe finalizes the invoice. Leaving invoices as drafts defers that calculation until manual finalization; the collection method controls payment after finalization, not whether tax is applied.
- The guide documents validation and escalation checks but no automatic fallback when tax cannot be applied or when payment fails.

## Responsibility and prerequisites

Stripe Tax is Stripe's native tax engine. In the documented flow, Metronome creates invoices in Stripe and supplies the mapped customer and product information; Stripe calculates and applies the tax. This configuration depends on, and does not replace, Metronome's native Stripe invoice integration. General account routing, status synchronization, and Stripe invoice representation limits belong to the separate invoice-integration guide.

Before enabling this tax path:

1. Activate Stripe Tax under **Settings → Tax** in Stripe.
2. Complete the required tax registrations in applicable jurisdictions for sales tax, VAT, and GST.
3. Connect the Stripe account to Metronome.
4. Link every Metronome customer to its Stripe customer ID.
5. Populate each Stripe customer's `address` object and mark the customer Taxable.
6. Ask the Metronome representative to enable tax application after the initial setup is complete.

The Customer Address determines the tax jurisdiction. The page does not specify currency restrictions, currency conversion, or currency-specific tax behavior, so none should be inferred from the numeric threshold examples.

## Product and tax-code mapping

Create at least one Stripe product and assign its tax code under **Product Settings → Tax code**. Stripe Tax uses the product attached to each invoice line item to determine the applicable tax code and rate. Metronome products with the same tax classification may map to the same Stripe product; distinct classifications require distinct Stripe products and tax codes.

In Metronome, create a custom field on the Product entity with key `stripe_product_id`, then set each Metronome product's value to the corresponding Stripe product ID. Do not enable `enforce_uniqueness`: reuse across Metronome products is intentional, and the guide says uniqueness cannot be undone without archiving and recreating the field.

Configure the Stripe entity mapping as follows:

| Stripe vendor entity | Stripe vendor key | Metronome entity | Metronome key |
| --- | --- | --- | --- |
| `invoiceitem.price` | `product` | `ContractProduct` | `stripe_product_id` |

Optional mappings can send Product custom fields to `invoiceitem.metadata.*` and Customer custom fields to `invoice.metadata.*`. The examples describe line-item metadata such as `TaxCode` and invoice-level metadata such as a customer tax classification; they do not make these optional metadata mappings prerequisites for Stripe Tax.

> [!warning] Documentation ambiguity
> The setup step says to create `stripe_product_id` on the Metronome **Product** entity, while the required mapping row names the Metronome entity as `ContractProduct`. The page does not reconcile those labels; verify the expected mapping context with Metronome rather than assuming they are interchangeable API entities.

## Calculation and invoice flow

For a sandbox test, create a Metronome test customer linked to a valid Stripe customer, generate an invoice in Metronome, and inspect the corresponding Stripe invoice for calculated tax. At invoice-line level, Metronome passes the mapped Stripe product ID; Stripe Tax uses the product tax code plus the customer's address-derived jurisdiction to calculate and apply tax.

Stripe automatic tax calculates inline when the Stripe invoice is finalized. The **Leave invoices as drafts** setting under **Connections → Integrations → Stripe → Settings** determines whether Metronome immediately finalizes a synced invoice or leaves it for review. The guide generally recommends switching that preference off for automatic calculation on sync. If drafts are retained, tax waits for manual finalization in Stripe.

The Stripe dashboard also needs a default tax behavior selected. This page requires that setting but does not define its allowed values or their effect, so those semantics should be taken from Stripe's own tax documentation rather than inferred here.

## Threshold and payment-gated billing

Account-level tax enablement covers arrears invoices but does not apply to prepaid-balance or spend-threshold billing. For either threshold form, `payment_gate_config` must explicitly include:

- `payment_gate_type: "STRIPE"`
- `tax_type: "STRIPE"`
- `stripe_config.payment_type: "INVOICE"`

The same explicit configuration applies to one-off payment-gated commits added through the edit-contract endpoint. The examples include numeric threshold and recharge amounts, but the page does not attach a currency or describe regional availability for these threshold flows.

## Collection and finalization behavior

Both documented Stripe invoice collection methods apply tax; the method controls what occurs after an invoice is finalized:

- `charge_automatically` charges the customer's default Stripe payment method. A default payment method must be present before finalization or payment fails. Stripe does not email the invoice by default, although Stripe receipt emails can be enabled separately.
- `send_invoice` emails the customer an invoice with payment instructions and requires `days_until_due`.

Tax configuration is independent of that collection-method choice. The page says both methods work with all tax providers, but it supplies setup instructions only for Stripe Tax and should not be treated as documentation of another provider's configuration.

## Failure checks and documented limits

If tax is absent, verify that Stripe Tax is enabled, the Stripe customer has a Customer Address and is Taxable, the entity mapping is saved, every relevant Metronome product has `stripe_product_id`, and each Stripe product has a valid tax code. A missing address explicitly causes tax application to fail. The troubleshooting section also describes invoices that either fail or finalize without tax when location information or mapping is incomplete, without assigning one deterministic outcome to each cause.

If those checks pass and automatic tax still does not apply, contact the Metronome representative to inspect account configuration. The guide does not document an automatic fallback tax rate, a retry schedule, a retroactive repair flow, or behavior for currencies and regions beyond applicable registration and address-based jurisdiction. Anrok and Avalara use separate setup guides even when connected through Stripe's third-party tax-app integration.

## Related

- Companies: [[metronome]], [[stripe]]
- Concepts: [[stripe-tax]], [[metronome-invoicing]], [[metronome-integrations]], [[metronome-products-and-rate-cards]], [[metronome-credits-and-commits]]
- Related sources: [[source-metronome-integrations-invoice-integrations-stripe]], [[source-stripe-billing-taxes-collect]]

## Raw Sources

- [[raw/metronome/integrations/tax-integrations/stripe-tax-2026-07-13|2026-07-13 snapshot — Stripe Tax setup, mapping, threshold billing, and invoice finalization]]
