---
title: "Manage Contracts in Stripe"
type: source
date_ingested: 2026-07-28
canonical_url: "https://docs.metronome.com/guides/get-started/stripe-marketplace-app"
original_format: webpage
raw_files:
  - "metronome/guides/get-started/stripe-marketplace-app-2026-07-13.md"
tags: [metronome, stripe, usage-based-billing, contracts, stripe-marketplace]
---

## Overview

This guide describes the Metronome Stripe App, which is installed from the Stripe App Marketplace and runs in the Stripe Dashboard. It covers prerequisites, revenue and usage summaries, customer management, a contract-creation wizard, and troubleshooting.

## Key takeaways

- The app embeds Metronome customer and contract management in the Stripe Dashboard, while invoicing continues through Metronome's separate native Stripe integration.
- Its Overview tab reports billed revenue, top products, a 30-day usage-events trend, and new customers.
- The four-step contract wizard configures invoicing, pricing, credits, and confirmation; the completed contract uses the Stripe customer's existing billing-provider configuration.
- The Customers tab displays only Stripe customers linked to Metronome customers through the connected account's Stripe billing configuration.

## Details

### Setup and dashboard

Installation requires a Metronome account with a production environment, a Stripe account with Dashboard access, and a configured Metronome Stripe integration. The Overview tab shows total and recent revenue, top products, total and duplicate usage-event trends, and recently added customers.

### Customer management

The Customers tab shows linked Stripe and Metronome customers with Stripe creation date, lifetime billings, and contract provision status. Actions can open the Stripe profile, open advanced management in Metronome, or start contract creation. When a Stripe customer lacks a corresponding Metronome customer, starting contract creation automatically creates one using the Stripe customer name.

### Contract wizard

The four steps configure:

1. Contract dates, invoice frequency and send date, and net payment terms.
2. A Metronome rate card, tag-scoped price overrides, subscription quantities, effective prices, and product entitlement.
3. One-time, monthly, or custom credit allocations, optional product-tag scope, invoice amount, and credit amount.
4. Confirmation and contract creation using the customer's existing billing-provider configuration.

If multiple product tags are selected for a price override, the product must have all selected tags. Missing customers or account-link errors should be checked against the connected Metronome account and its `stripe_customer_id` billing configuration.

## Related

- Companies: [[metronome]], [[stripe]]
- Concepts: [[metronome-integrations]], [[metronome-customers-and-contracts]], [[metronome-invoicing]], [[metronome-products-and-rate-cards]]

## Raw Sources

- [[raw/metronome/guides/get-started/stripe-marketplace-app-2026-07-13|2026-07-13 snapshot — Stripe Dashboard app and contract workflow]]
