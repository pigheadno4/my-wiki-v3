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

## Stripe Tax boundary

Metronome creates and maps the Stripe invoice, while Stripe Tax calculates and applies tax when Stripe finalizes it. Metronome supplies the linked Stripe customer and a line-item product mapping; Stripe uses the customer address for jurisdiction and the Stripe product tax code for classification. Leaving the invoice as a draft defers automatic tax until manual finalization.

## Threshold payment-gate boundary

For a Stripe-gated prepaid threshold, Metronome initiates the configured Stripe invoice or PaymentIntent and releases the recharge commit only after successful payment. With `payment_gate_type: EXTERNAL`, Metronome emits `payment_gate.external_initiate`, while the integrator owns collection and must call the threshold-release endpoint with the workflow ID to release or cancel the commit. The guide does not document external-gateway readiness, retry, or idempotency behavior.

For a manual Stripe-gated commit, Metronome initiates and monitors payment and requires the product mapping described in [[metronome-products-and-rate-cards]]. Release timing depends on the provider, payment method, and authentication. After failure, the guide requires a new Metronome request and no automatic payment retry; the broader Stripe ownership statement above must not override this source-specific boundary.

## Billing-provider transitions

Metronome can schedule contract invoice delivery among Stripe, NetSuite, and AWS, Azure, or GCP Marketplace. Marketplace-involved transitions must start next period because marketplace billing covers a complete period; Stripe and NetSuite changes can also correct the current period while the invoice remains a draft.

Metronome owns the provider schedule and invoice routing. The guide does not document how destination accounts are provisioned, reconciled, or checked for readiness before a scheduled segment becomes active.

The architecture overview names payment systems and marketplaces as the contract's delivery destination and says finalized invoices are sent to a selected downstream system at cycle close. It does not allocate configuration, payment collection, retry, or failure responsibilities, so the dedicated integration sources remain authoritative.

## Customer-provisioning configuration

The external billing system must be connected before its customer configuration is created. Customer-level AWS configuration alone does not route invoices; a contract must select it. Beta archival makes a configuration reusable elsewhere but immediately removes it from an active contract and stops destination billing, with no replacement allowed on that contract according to this guide.

Customer creation can attach configurations for Stripe, NetSuite, AWS Marketplace, Azure Marketplace, or GCP Marketplace. Each billing configuration requires a provider; delivery can be identified by a delivery-method UUID or a named method such as direct provider delivery, AWS SQS, Tackle, or AWS SNS. Provider-specific configuration is open-ended, and its empty-object default is invalid for most provider/delivery combinations.

The optional tax-provider field lists Anrok, Avalara, and Stripe. The source limits Stripe tax calculation in this customer-creation structure to Stripe configurations using payment-intent collection methods. A separately feature-flagged revenue-system configuration currently enumerates NetSuite and expects a provider-specific customer identifier.

## Sources

- [[source-metronome-guides-get-started-stripe-marketplace-app]] — embedded Stripe Dashboard app, customer management, contract creation, and invoicing boundary
- [[source-metronome-integrations-invoice-integrations-stripe]] — native invoice delivery, account routing, mappings, status synchronization, and Stripe limits
- [[source-metronome-integrations-tax-integrations-stripe-tax]] — tax responsibility, customer/product mapping, finalization, and threshold configuration
- [[source-metronome-guides-customers-billing-optimize-customer-experience-prepaid-balance-thresholds]] — Stripe and external threshold payment-gate responsibilities
- [[source-metronome-guides-customers-billing-manage-customers-schedule-billing-provider-change]] — Stripe, NetSuite, and marketplace transition timing and responsibility
- [[source-metronome-api-reference-customers-create-a-customer]] — provider, delivery, tax, and revenue-system configuration during provisioning
- [[source-metronome-guides-get-started-how-metronome-works]] — high-level downstream-destination boundary
- [[source-metronome-guides-implement-metronome-core-concepts-provision-customer]] — external connection prerequisite, contract selection, and beta archival
- [[source-metronome-guides-pricing-packaging-apply-credits-and-commits-manual-payment-gated-commits]] — Stripe manual-gate responsibility, product mapping, and retry boundary

## Related

- [[metronome-customers-and-contracts]]
- [[metronome-invoicing]]
- [[metronome-products-and-rate-cards]]
- [[metronome-webhooks]]
- [[stripe]]
