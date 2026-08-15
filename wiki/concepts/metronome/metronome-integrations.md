---
title: "Metronome Integrations"
type: concept
category: technology
tags: [metronome, integrations, stripe, invoicing]
---

## Definition

Metronome integrations connect its usage-billing and contract workflows to external systems. The Metronome Stripe App is an embedded management interface inside the Stripe Dashboard; it is distinct from the native Stripe invoicing integration that delivers invoices to Stripe.

## TypeScript SDK boundary

`@metronome/sdk@3.10.0` is a generated server-side TypeScript and JavaScript client with no runtime dependencies. It defaults bearer authentication from `METRONOME_BEARER_TOKEN`, supports configurable fetch, proxy, timeout, retry, logging, raw-response, and pagination behavior, and exposes both typed resources and generic HTTP methods. Its generated types prove an exact package's client surface, not feature enablement or current service behavior. React Native is explicitly unsupported in this release. [[source-github-metronome-node]]

## AI operating-guidance boundary

`Metronome-Industries/ai` packages integration, catalog, customer, contract, PLG, CSM, and Stripe-migration instructions for coding and operational agents. Its preview-before-write controls and reference-first routing are useful workflow evidence, but its examples do not replace dedicated API schemas or prove account enablement. Internal conflicts in event value types, rate representation, endpoint names, and migration consequences must be reconciled against canonical documentation before execution. [[source-github-ai]]

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

For the Indian-card mandate flow, Stripe owns SetupIntent confirmation, mandate creation, status changes, and `invoice.payment_action_required`. Metronome's role is limited to storing and returning a contract custom-field value, mapping it to Stripe's invoice `default_mandate`, attempting attachment on invoices sent to Stripe, and surfacing payment failures through its normal failure path. Metronome does not expose a mandate-management API or manage lifecycle events; the integrator must wait for active status and replace or update the Stripe mandate before retrying when necessary.

## Stripe Tax boundary

Metronome creates and maps the Stripe invoice, while Stripe Tax calculates and applies tax when Stripe finalizes it. Metronome supplies the linked Stripe customer and a line-item product mapping; Stripe uses the customer address for jurisdiction and the Stripe product tax code for classification. Leaving the invoice as a draft defers automatic tax until manual finalization.

## Avalara tax-app boundary

For Stripe-delivered invoices using Avalara, AvaTax integrates through Stripe's Marketplace app and third-party tax-app framework rather than directly with Metronome. The guide creates the case-sensitive `TaxCode` custom field on Metronome `Product`, while its mapping row sends `ContractProduct.TaxCode` to `invoiceitem.metadata.TaxCode`; Stripe hosts the draft invoice and integration settings; Avalara calculates tax from the customer address and line-item code and owns unresolved rate-accuracy questions. The guide requires **Leave invoices as drafts** to remain on so Avalara can calculate and apply tax before finalization, but it does not define finalization ownership, processing time, retries, or safeguards against finalizing without tax.

## Anrok tax-app boundary

For the primary Anrok path, Metronome creates the Stripe invoice and supplies linked-customer and mapped-product context, Stripe hosts the installed Anrok app and automatic-tax provider selection, and Anrok calculates tax and handles compliance instead of Stripe's native tax engine. Stripe customer addresses determine jurisdiction; each Metronome Product carries `stripe_product_id`, mapped from `ContractProduct.stripe_product_id` to `invoiceitem.price.product`. The Product-versus-`ContractProduct` terminology is unresolved in this guide as it is in the native Stripe Tax guide. Arrears tax calculates inline without requiring invoices to remain drafts; prepaid-balance and spend thresholds use `tax_type: "STRIPE"` and `payment_type: "INVOICE"`, where `STRIPE` is the documented `tax_type` value for this Anrok-through-Stripe threshold configuration, while the guide does not define the enum's general semantics. The literal is not reliable evidence of calculator identity because the documented active provider in this mode is Anrok. The guide separately permits Stripe Tax to calculate while Anrok consumes Stripe transaction data for compliance, filing, and reporting; it does not define transfer timing, completeness, reconciliation, correction, filing cadence, or failure handling for that hybrid mode.

## Threshold payment-gate boundary

For a Stripe-gated prepaid threshold, Metronome initiates the configured Stripe invoice or PaymentIntent and releases the recharge commit only after successful payment. With `payment_gate_type: EXTERNAL`, Metronome emits `payment_gate.external_initiate`, while the integrator owns collection and must call the threshold-release endpoint with the workflow ID to release or cancel the commit. The guide does not document external-gateway readiness, retry, or idempotency behavior.

For a manual Stripe-gated commit, Metronome initiates and monitors payment and requires the product mapping described in [[metronome-products-and-rate-cards]]. Release timing depends on the provider, payment method, and authentication. After failure, the guide requires a new Metronome request and no automatic payment retry; the broader Stripe ownership statement above must not override this source-specific boundary.

Spend-threshold billing uses the same explicit external-ownership pattern as the documented threshold release route: `payment_gate_type: EXTERNAL` causes `payment_gate.external_initiate`; the integrator retains the workflow ID, collects payment independently, and calls the release endpoint to release or cancel the pending commit. For Stripe, the spend-threshold page offers invoice or PaymentIntent collection and requires a valid contract billing configuration. It does not define gateway readiness, event ordering, duplicate outcomes, expiry, retry, or idempotency.

## Billing-provider transitions

Metronome can schedule contract invoice delivery among Stripe, NetSuite, and AWS, Azure, or GCP Marketplace. Marketplace-involved transitions must start next period because marketplace billing covers a complete period; Stripe and NetSuite changes can also correct the current period while the invoice remains a draft.

The invoice-regeneration endpoint says that when the voided invoice is attached to a contract with a billing provider, the regenerated invoice is distributed according to that configuration. The page does not identify the provider, the configuration-resolution time, the regenerated invoice's state, synchronous versus asynchronous timing, delivery identifiers, webhooks, failures, retries, or duplicate-delivery behavior. This distribution statement does not void or cancel the old downstream invoice: the separate credit-and-rebill guide assigns that step to the merchant, while stating specifically that a regenerated invoice using the Metronome Stripe integration is sent to Stripe automatically. Do not extend regeneration to payment collection, refunds, tax, A/R, revenue, or ledger reconciliation without separate evidence.

Metronome owns the provider schedule and invoice routing. The guide does not document how destination accounts are provisioned, reconciled, or checked for readiness before a scheduled segment becomes active.

The architecture overview names payment systems and marketplaces as the contract's delivery destination and says finalized invoices are sent to a selected downstream system at cycle close. It does not allocate configuration, payment collection, retry, or failure responsibilities, so the dedicated integration sources remain authoritative.

## Customer-provisioning configuration

The external billing system must be connected before its customer configuration is created. Customer-level AWS configuration alone does not route invoices; a contract must select it. Beta archival makes a configuration reusable elsewhere but immediately removes it from an active contract and stops destination billing, with no replacement allowed on that contract according to this guide.

Customer creation can attach configurations for Stripe, NetSuite, AWS Marketplace, Azure Marketplace, or GCP Marketplace. Each billing configuration requires a provider; delivery can be identified by a delivery-method UUID or a named method such as direct provider delivery, AWS SQS, Tackle, or AWS SNS. Provider-specific configuration is open-ended, and its empty-object default is invalid for most provider/delivery combinations.

The optional tax-provider field lists Anrok, Avalara, and Stripe. The source limits Stripe tax calculation in this customer-creation structure to Stripe configurations using payment-intent collection methods. A separately feature-flagged revenue-system configuration currently enumerates NetSuite and expects a provider-specific customer identifier.

## Managed custom-invoice integration boundary

For billing systems outside Metronome's native integrations, Metronome documents data exports or a managed integration built on Data Export or Metronome APIs. In the QuickBooks example, the implementer owns external application and OAuth setup, external customer and item creation or lookup, storage of external identifiers in Metronome custom fields, invoice transformation, and the destination upsert. Metronome supplies the finalized-invoice event and invoice data; the selected billing system stores its customer, item, and created invoice objects. The overall pattern may inform other use cases, but the named credentials, object mappings, fields, and request are QBO-specific. The page does not assign hosting, operational support, payment collection, tax, retries, idempotency, reconciliation, or ongoing object-synchronization ownership. Workato is an optional orchestration recommendation, not a documented complete implementation of those responsibilities.

## Workato connector boundary

Metronome documents an SDK-like Workato connector for performing actions on Metronome endpoints. It gives third-party invoicing, customer provisioning, and contract provisioning as example workflows. Setup requires generating a Metronome API token and pasting it into a Workato connection, and a unique connection is required for each Metronome environment. The page does not enumerate the connector's available actions, endpoint coverage, API-token permissions, workflow triggers, data mappings, error handling, retry behavior, or connection-rotation procedure; it therefore does not establish complete endpoint coverage or broader Workato capabilities.

## Segment event-delivery integration

The Metronome (Actions) destination connects one selected Segment source using a Metronome API token and maps Segment event fields into Metronome's usage-event format. Additional Destination Actions can pair mappings with triggers containing any number of conditions, such as excluding company-domain user emails. The page calls these action configurations `subscriptions`; in this context they are Segment conditional-delivery rules, not Metronome billing subscriptions or customer contracts. It does not define token scope or rotation, trigger overlap or evaluation order, duplicate delivery, retries, batching, response handling, replay, or observability.

## Sources

- [[source-github-ai]] - Metronome-authored AI skills, operational controls, migration workflow, and evidence limitations
- [[source-github-metronome-node]] - exact `@metronome/sdk@3.10.0` package, runtime, transport, generated API, and evidence boundaries

- [[source-metronome-api-reference-invoices-regenerate-an-invoice]] - configured billing-provider distribution for regenerated invoices and bounded downstream side effects

- [[source-metronome-integrations-invoice-integrations-custom-invoice-integrations]] — managed non-native invoice integration routes, QuickBooks object mapping, finalized-invoice export flow, and system-ownership boundaries

- [[source-metronome-integrations-platform-integrations-workato-connector]] — SDK-like Workato connector setup with a Metronome API token and the unique-connection requirement for each Metronome environment

- [[source-metronome-integrations-platform-integrations-segment]] - Segment source and token setup, usage-event field mappings, transaction-ID default, and conditional Destination Actions

- [[source-metronome-integrations-tax-integrations-avalara]] — Stripe-hosted Avalara path, TaxCode metadata mapping, draft-invoice requirement, and rate-accuracy ownership

- [[source-metronome-integrations-tax-integrations-anrok]] — Anrok-through-Stripe responsibility, customer and product mapping, invoice modes, and compliance-only coexistence with Stripe Tax

- [[source-metronome-guides-get-started-stripe-marketplace-app]] — embedded Stripe Dashboard app, customer management, contract creation, and invoicing boundary
- [[source-metronome-integrations-invoice-integrations-stripe]] — native invoice delivery, account routing, mappings, status synchronization, and Stripe limits
- [[source-metronome-integrations-tax-integrations-stripe-tax]] — tax responsibility, customer/product mapping, finalization, and threshold configuration
- [[source-metronome-guides-customers-billing-optimize-customer-experience-prepaid-balance-thresholds]] — Stripe and external threshold payment-gate responsibilities
- [[source-metronome-guides-customers-billing-manage-customers-schedule-billing-provider-change]] — Stripe, NetSuite, and marketplace transition timing and responsibility
- [[source-metronome-api-reference-customers-create-a-customer]] — provider, delivery, tax, and revenue-system configuration during provisioning
- [[source-metronome-guides-get-started-how-metronome-works]] — high-level downstream-destination boundary
- [[source-metronome-guides-implement-metronome-core-concepts-provision-customer]] — external connection prerequisite, contract selection, and beta archival
- [[source-metronome-guides-pricing-packaging-apply-credits-and-commits-manual-payment-gated-commits]] — Stripe manual-gate responsibility, product mapping, and retry boundary
- [[source-metronome-guides-customers-billing-optimize-customer-experience-india-e-mandates]] — Stripe mandate ownership, Metronome contract-field mapping, action-required handling, and retry boundary
- [[source-metronome-guides-customers-billing-optimize-customer-experience-set-customer-spend-control]] — Stripe and external spend-threshold payment-gate responsibility

## Related

- [[metronome-customers-and-contracts]]
- [[metronome-invoicing]]
- [[metronome-products-and-rate-cards]]
- [[metronome-webhooks]]
- [[stripe]]
