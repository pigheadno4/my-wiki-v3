---
title: "Manage contracts in Stripe"
type: source
date_ingested: 2026-07-28
canonical_url: "https://docs.metronome.com/guides/get-started/stripe-marketplace-app"
original_format: webpage
raw_files:
  - "metronome/guides/get-started/stripe-marketplace-app-2026-07-13.md"
tags: [metronome, stripe, usage-based-billing, contracts, stripe-marketplace]
---

## Overview

This guide describes the Metronome Stripe App, which is installed from the Stripe App Marketplace and runs in the Stripe Dashboard. It covers the app's prerequisites, overview dashboard, customer management, contract-creation wizard, and troubleshooting.

## Key takeaways

- The app provides an embedded Metronome interface in the Stripe Dashboard, while invoicing continues through Metronome's native Stripe integration.
- Its Overview tab reports billed revenue, top products, a 30-day usage-events trend, and new customers.
- The four-step contract-creation wizard configures invoicing, pricing, credits, and confirmation; created contracts use the Stripe customer's existing billing provider configuration.
- A missing customer must be linked through the Stripe billing configuration in the connected Metronome account.

## Details

Installation requires a Metronome account with a production environment, a Stripe account with Dashboard access, and a configured Metronome Stripe integration. The Customers tab shows linked Stripe and Metronome customers with creation date, lifetime billings, and contract provision status; it can open the Stripe profile, open Metronome management, or start contract creation.

The invoicing step selects contract dates, invoice schedule, send date, and net payment terms. Pricing selects a Metronome rate card, can apply tag-scoped price overrides, sets subscription quantities, and can override individual product entitlement. Credits can be one-time, monthly, or custom allocations, with optional applicable product tags plus invoice and credit amounts.

For authentication errors, the guide directs users to clear cached Metronome credentials, log out of Metronome, and sign in again. If the connected Metronome account is not linked to the Stripe account, the guide directs users to configure the Stripe invoicing integration.

## Related

- Coordinator audit: determine the appropriate existing company and platform-concept links before promotion; this candidate introduces no such links.

## Raw Sources

- [[raw/metronome/guides/get-started/stripe-marketplace-app-2026-07-13|stripe-marketplace-app-2026-07-13]] — verbatim Metronome documentation page.
