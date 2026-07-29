---
title: "Metronome Integrations"
type: concept
category: technology
tags: [metronome, integrations, stripe, invoicing]
---

## Definition

Metronome integrations connect its usage-billing and contract workflows to external systems. The Metronome Stripe App is an embedded management interface inside the Stripe Dashboard; it is distinct from the native Stripe invoicing integration that delivers invoices to Stripe.

## Stripe App boundary

- The app requires a Metronome production environment, Stripe Dashboard access, and a configured Metronome Stripe integration.
- It provides revenue and usage summaries, linked-customer views, and a four-step contract-creation workflow inside Stripe.
- Customer and contract management still operates through Metronome's embedded interface.
- Invoice delivery does not originate from the app itself. Contracts use the customer's existing Stripe billing-provider configuration, and invoicing continues through Metronome's native Stripe integration.

## Native Stripe invoicing boundary

- Metronome owns usage rating and its invoice record, then creates the corresponding Stripe invoice for payment collection.
- Connections and mapping rules are configured per Metronome environment and Stripe account.
- Customer configuration uses `delivery_method_id` to select a Stripe account in a multi-account setup. Contract creation instead selects one of the customer's configured providers with `billing_provider_configuration_id`, obtained from `/getCustomerBillingProviderConfigurations`.
- Stripe owns downstream payment timing, retries, and invoice payment status; Metronome imports status changes from Stripe webhooks.
- Tax providers operate on the draft Stripe invoice before Stripe finalization.
- `invoice.billing_provider_error` reports failures sending an invoice to Stripe, but the webhook guide warns that it does not cover failures that exist entirely inside Stripe.

## Sources

- [[source-metronome-guides-get-started-stripe-marketplace-app]] — embedded Stripe Dashboard app, customer management, contract creation, and invoicing boundary
- [[source-metronome-integrations-invoice-integrations-stripe]] — native invoice delivery, account routing, mappings, status synchronization, and Stripe limits

## Related

- [[metronome-customers-and-contracts]]
- [[metronome-invoicing]]
- [[metronome-products-and-rate-cards]]
- [[metronome-webhooks]]
- [[stripe]]
