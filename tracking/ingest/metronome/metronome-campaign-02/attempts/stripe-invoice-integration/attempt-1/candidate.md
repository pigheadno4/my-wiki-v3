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
- Customer billing configuration supplies the Stripe customer ID and collection method; multi-account configurations require `delivery_method_id`.
- For `charge_automatically`, Stripe can wait up to one hour after the `invoice.created` webhook before attempting payment, with a 72-hour fallback when webhook delivery fails.
- Metronome maps Stripe webhook events to external invoice statuses and documents invoice-limit handling, including decimal quantities and more than 250 line items.

## Details
Metronome can connect one environment to multiple Stripe accounts. In that case, accounts have independent integration settings and mapping rules, and customer configuration must identify the destination account with `delivery_method_id`. The guide says Metronome sets a `metronome_id` on created Stripe invoices and supports additional mapping from Metronome custom fields to Stripe entities.

A Stripe customer billing configuration uses `stripe_customer_id` and `stripe_collection_method`. `charge_automatically` uses the customer’s default payment method; `send_invoice` emails payment instructions and uses the configured due-date setting. Contract-level configuration can route different contracts differently, and adding a provider configuration does not retroactively send earlier finalized invoices.

Metronome records Stripe invoice status changes from webhooks, and its documented tax flow creates a draft Stripe invoice, passes mapping data, lets a tax provider calculate tax, and then finalizes the invoice with tax included. The guide also describes a webhook-based error notification type, `invoice.billing_provider_error`.

For Stripe limitations, Metronome puts true decimal quantities in line-item descriptions when needed, collapses invoices above 250 line items into one item, reports an error above the documented charge maximum, and does not natively issue Stripe credit memos.

## Related
- Coordinator audit: determine whether existing Metronome and Stripe company pages or platform-specific concept pages should be linked before promotion.

## Raw Sources
- [[raw/metronome/integrations/invoice-integrations/stripe-2026-07-13|stripe-2026-07-13]] — verbatim Metronome Stripe invoice-integration documentation.
