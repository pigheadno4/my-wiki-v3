---
title: "Invoice with Stripe"
type: source
date_ingested: 2026-07-28
canonical_url: "https://docs.metronome.com/integrations/invoice-integrations/stripe"
original_format: webpage
raw_files:
  - "metronome/integrations/invoice-integrations/stripe-2026-07-13.md"
tags: [metronome, stripe, invoicing, billing-integration]
---

## Overview

Metronome documents its native Stripe integration for creating a corresponding Stripe invoice when a Metronome invoice finalizes at the end of a billing period. The guide covers connection and configuration, customer and contract billing settings, status tracking, tax flow, payment timing, errors, and Stripe invoice limits.

## Key takeaways

- Stripe connections are configured per Metronome environment; sandbox connects to Stripe test mode for end-to-end invoice and payment-collection testing.
- Customer billing configuration supplies the Stripe customer ID and collection method; multi-account configurations require `delivery_method_id`, while contract-level configuration can route different contracts through different providers.
- For `charge_automatically`, Stripe can wait up to one hour after the `invoice.created` webhook before attempting payment, with a 72-hour fallback when webhook delivery fails.
- Adding Stripe to an existing contract affects only invoices that finalize afterward; previously finalized invoices are not sent retroactively.
- Payment-gated commits require each participating Metronome product to map a valid `stripe_product_id`, or the payment attempt fails and the commit is voided.

## Details

### Connection and routing

Each Metronome environment has its own Stripe connection; a Metronome sandbox connects to Stripe test mode. One environment can connect to multiple Stripe accounts, but settings and entity mappings are then configured independently for each account. Customer configuration must use `delivery_method_id` to identify the destination account in a multi-account setup; single-account setup can use `delivery_method`.

A customer billing configuration uses `stripe_customer_id` and `stripe_collection_method`. `charge_automatically` requires a default payment method on the Stripe customer before finalization. `send_invoice` emails payment instructions and takes its due-date behavior from the account-level integration setting. Contract-level configuration can route different contracts differently, such as Stripe for pay-as-you-go and a marketplace for enterprise terms.

Adding a billing provider to an existing contract does not replay prior finalized invoices. The first Stripe delivery is the in-arrears invoice for the billing period in which the configuration was attached, determined by attachment time rather than contract start or configuration creation time.

### Account-level settings and mappings

Integration settings are enforced per Stripe account and Metronome environment, not per customer. They can change due dates, leave Stripe invoices as drafts by setting `auto_advance=false`, skip invoices below Stripe's currency minimum, align `effective_at` to the service period's last day, and control zero-quantity or decimal-quantity presentation. The `effective_at` alignment option is incompatible with Stripe Tax according to this guide.

Metronome places its invoice ID in Stripe metadata as `metronome_id` and can map additional Metronome custom fields to Stripe invoice, invoice-item, and price fields. Payment-gated commits have a stricter requirement: every participating Metronome product must map `stripe_product_id` to a valid Stripe Product ID, otherwise Stripe cannot construct the line item, the payment fails, and the commit is voided.

### Status, tax, timing, and errors

Metronome records Stripe invoice status changes from webhooks, and its documented tax flow creates a draft Stripe invoice, passes mapping data, lets a tax provider calculate tax, and then finalizes the invoice with tax included. The guide also describes the webhook type `invoice.billing_provider_error` for errors sending invoices to Stripe.

Stripe events map to Metronome external statuses including `FINALIZED`, `UNCOLLECTIBLE`, `PAID`, `PAYMENT_FAILED`, `VOID`, and `DELETED`; the status is also available through data export. When invoices are deliberately left as drafts, Stripe does not return a status and Metronome does not show one.

For `charge_automatically`, Metronome sends the finalized invoice immediately, but Stripe waits up to one hour after delivering `invoice.created` before attempting payment. A failed webhook delivery can extend the Stripe-side wait to 72 hours. The guide proposes manually confirming the PaymentIntent from a Stripe webhook as a workaround, while noting that auto-recharge and payment-gated-commit invoices use different payment paths.

### Stripe limitations

- If any quantity is decimal, Metronome sends quantity `1` for every Stripe line item and includes the true quantities in descriptions.
- If a Metronome invoice exceeds Stripe's 250-line-item limit, Metronome collapses it into one Stripe line item.
- Metronome reports an error for a charge above the guide's stated Stripe maximum of $999,999.99.
- The integration does not natively issue Stripe credit memos.

## Related

- Companies: [[metronome]], [[stripe]]
- Concepts: [[metronome-invoicing]], [[metronome-integrations]], [[metronome-customers-and-contracts]], [[metronome-credits-and-commits]], [[metronome-webhooks]]

## Raw Sources

- [[raw/metronome/integrations/invoice-integrations/stripe-2026-07-13|2026-07-13 snapshot — Stripe invoice integration, routing, timing, and limits]]
