---
title: "Metronome Integrations"
type: concept
category: technology
tags: [metronome, integrations, stripe, invoicing]
---

## Definition

Metronome integrations connect its usage-billing and contract workflows to external systems. The Metronome Stripe App is an embedded management interface inside the Stripe Dashboard; it is distinct from the native Stripe invoicing integration that delivers invoices to Stripe.

## NetSuite product-item retrieval surface

The product catalog's `initial` and `current` state schemas and its update schema can expose `netsuite_internal_item_id` and `netsuite_overage_item_id`; both fields state that their availability depends on the client's configuration. This retrieval schema does not define what either identifier maps to, external-item validation, freshness, propagation, synchronization, invoice delivery, or reconciliation. [[source-metronome-api-reference-products-list-products]]


## Native NetSuite integration boundary

Metronome's Public Beta NetSuite integration supports direct billing and revenue-system use cases. A contract selects a customer configuration: billing mode sends finalized invoices to NetSuite for NetSuite-owned distribution, tax, and collection, while revenue mode sends invoices after another system attempts payment and creates payment objects when successful. Product custom fields map Metronome line items to NetSuite item IDs, and zero-dollar prepaid-consumption invoices require a separate Commit Application item. Billing status and errors appear under `external_invoice`; revenue-system status and errors appear under `revenue_system_invoices`; invoice and payment sync webhooks expose outcome signals, and an item-mapping failure can be corrected before a manual UI resend. The guide does not turn those signals into guarantees of delivery, payment finality, tax correctness, revenue posting, settlement, or reconciliation. The beta excludes custom currencies and account hierarchy, assumes compatible standard NetSuite configuration, and assigns client-specific changes and sandbox validation to the client.

## TypeScript SDK boundary

`@metronome/sdk@3.10.0` is a generated server-side TypeScript and JavaScript client with no runtime dependencies. It defaults bearer authentication from `METRONOME_BEARER_TOKEN`, supports configurable fetch, proxy, timeout, retry, logging, raw-response, and pagination behavior, and exposes both typed resources and generic HTTP methods. Its generated types prove an exact package's client surface, not feature enablement or current service behavior. React Native is explicitly unsupported in this release. [[source-github-metronome-node]]

## AI operating-guidance boundary

`Metronome-Industries/ai` packages integration, catalog, customer, contract, PLG, CSM, and Stripe-migration instructions for coding and operational agents. Its preview-before-write controls and reference-first routing are useful workflow evidence, but its examples do not replace dedicated API schemas or prove account enablement. Internal conflicts in event value types, rate representation, endpoint names, and migration consequences must be reconciled against canonical documentation before execution. [[source-github-ai]]

## Terraform provider boundary

`terraform-provider-metronome@0.1.0-alpha.3` is an experimental, Stainless-generated provider that must not be used in production. It accepts base URL, bearer token, and webhook-secret configuration and constructs a Metronome Go client, but its exact implementation registers no Terraform resources and no data sources. Configuration support is therefore not evidence that this release can manage or look up any Metronome entity. Generic release-note entries about resource permissions, data-source IDs, serialization, or validators do not override the empty registration surface. [[source-github-terraform-provider-metronome]]

## Stripe App boundary

- The app requires a Metronome production environment, Stripe Dashboard access, and a configured Metronome Stripe integration.
- It provides revenue and usage summaries, linked-customer views, and a four-step contract-creation workflow inside Stripe.
- Customer and contract management still operates through Metronome's embedded interface.
- Invoice delivery does not originate from the app itself. Contracts use the customer's existing Stripe billing-provider configuration, and invoicing continues through Metronome's native Stripe integration.

## Native Stripe invoicing boundary

The custom-field key creation reference says product custom-field values can be used by the Stripe integration to set invoice metadata. It does not define the metadata key or value mapping, target Stripe object, timing, overwrite precedence, validation, failure handling, retroactivity, delivery, or reconciliation. Creating an allowed key is also separate from assigning a product value and from generating or delivering an invoice, so a successful `addKey` response proves no Stripe-side mutation. [[source-metronome-api-reference-custom-fields-create-a-custom-field-key]]

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

## Account-level provider setup

Bearer-authenticated `POST /v1/setUpBillingProvider` creates an account-level delivery configuration for AWS, Azure, or GCP Marketplace and returns UUID `delivery_method_id`. Its JSON payload schema requires provider, delivery method, and an open provider-specific `configuration`, although the enclosing `requestBody` is not marked required. This operation does not identify or mutate a customer or contract; separate sources use the returned delivery-method layer when constructing customer billing configuration and use a distinct customer configuration ID for contract selection. The endpoint does not document provider readiness, propagation to listing, update or deletion, external validation, or downstream invoice and reconciliation outcomes. [[source-metronome-api-reference-settings-set-up-account-level-billing-provider]]


### Native AWS Marketplace integration boundary

The AWS path layers an approved seller listing, delegated AWS access, customer identity, and contract routing. **Contract with Consumption** uses fixed terms and contract dimensions corresponding to Metronome pricing models and lifecycle events such as subscription end and renewal; those contract-dimension API identifiers and display names are merchant-chosen, pay-as-you-go is unchecked, and each contract-dimension price is `$0`. **Usage-based pricing** can be started or stopped by the customer and omits the contract-only dimension and purchasing steps. Both routes use a separate single usage dimension whose mandatory API identifier is `usage_fee` and whose price is `$0.01` per unit. A seller-owned cross-account IAM role grants BatchMeterUsage plus entitlement and marketplace entity reads; customer-level AWS customer/product/region configuration and contract-level AWS selection remain separate layers. Completing setup is not documented proof of listing activation, AWS acceptance, invoice delivery, settlement, or reconciliation. [[source-metronome-integrations-marketplace-integrations-aws]]

### Native Azure Marketplace integration boundary

The Azure path layers a merchant-created Azure SaaS offer, Microsoft Entra credentials, an activated marketplace Subscription ID, customer-level Azure configuration, and contract-level Azure delivery selection. Metronome submits calculated USD-cent invoice totals, but the merchant owns SaaS status, contract alignment, lifecycle handling in its app, marketplace-window true-ups, and manual refund escalation. Configuration does not prove Azure activation or acceptance, payment, settlement, tax, refund completion, or reconciliation. [[source-metronome-integrations-marketplace-integrations-azure]]

### Native GCP Marketplace integration boundary

The GCP path layers merchant-owned project and listing configuration, Workload Identity Federation, a GCP service account with procurement and usage-reporting access, Provider ID and federation JSON submission, customer Entitlement/Order ID plus Service Name mapping, and contract-level GCP delivery selection. Metronome calculates and reports USD-cent invoice totals, while the merchant owns Google listing approval, its subscription backend and application status, contract alignment, marketplace-window true-ups, and manual refund escalation. Configuration and access validation do not prove GCP publication or activation, metering acceptance, payment, settlement, tax, refund completion, or reconciliation. [[source-metronome-integrations-marketplace-integrations-gcp]]

## Account-level provider enumeration

`POST /v1/listConfiguredBillingProviders` is a bearer-authenticated Settings operation that enumerates the billing-provider delivery methods configured for an account. Its optional nullable UUID `next_page` cursor paginates a required `data` array; each entry requires a provider, UUID `delivery_method_id`, delivery method, and method-specific configuration object. The provider enum covers AWS Marketplace, Stripe, NetSuite, custom, Azure Marketplace, QuickBooks Online, Workday, GCP Marketplace, and Metronome, while delivery is enumerated as direct provider delivery, AWS SQS, Tackle, or AWS SNS. Configuration permits arbitrary method-specific properties and may omit security-sensitive values.

The returned identifiers and settings are described as inputs for mapping customer contracts to billing integrations, but this operation does not create or update customer configurations, contract selections, or provider schedules. Its item description calls `delivery_method_id` an ID used for a customer; do not equate that account-level delivery-method identifier with a customer billing-provider configuration ID or contract selector without separate schema evidence. The page does not define token scope, ordering, page size, cursor lifecycle, configuration readiness, invoice-delivery outcomes, payment ownership, retry behavior, or errors beyond a generic HTTP 400 message. [[source-metronome-api-reference-settings-list-account-level-billing-providers]]


## Invoice-read integration status surface

The single-invoice response can expose nullable `external_invoice` and `revenue_system_invoices`. An external-invoice object requires a billing-provider type when present and can optionally report an external ID, issued time, provider status, PDF URL, beta tax and invoiced totals, provider error, and external payment ID. Each revenue-system item requires provider, sync status, and external entity type, with optional external entity ID and error. The endpoint does not define observation freshness, status transitions, provider precedence, retry, terminality, or reconciliation; a returned identifier or paid-like status does not independently prove delivery, settlement finality, tax correctness, revenue posting, or reconciliation, and absence of an error is not success proof.

## Billing-provider transitions

> [!warning] Contract-edit provider scope conflict
> The `POST /v2/contracts/edit` schema says `add_billing_provider_configuration_update` currently supports only adding a provider configuration to a contract that has none, and gives the same add-only boundary for the feature-gated revenue-system update. The dedicated provider-transition guide separately documents provider-to-provider changes on existing contracts. The sources do not establish whether the endpoint description is stale, configuration-dependent, or narrower than the guide. Neither source proves downstream provider readiness, invoice delivery, revenue posting, or reconciliation; verify current account enablement and runtime transition support. [[source-metronome-api-reference-contracts-edit-a-contract]] [[source-metronome-guides-customers-billing-manage-customers-schedule-billing-provider-change]]

Metronome can schedule contract invoice delivery among Stripe, NetSuite, and AWS, Azure, or GCP Marketplace. Marketplace-involved transitions must start next period because marketplace billing covers a complete period; Stripe and NetSuite changes can also correct the current period while the invoice remains a draft.

The invoice-regeneration endpoint says that when the voided invoice is attached to a contract with a billing provider, the regenerated invoice is distributed according to that configuration. The page does not identify the provider, the configuration-resolution time, the regenerated invoice's state, synchronous versus asynchronous timing, delivery identifiers, webhooks, failures, retries, or duplicate-delivery behavior. This distribution statement does not void or cancel the old downstream invoice: the separate credit-and-rebill guide assigns that step to the merchant, while stating specifically that a regenerated invoice using the Metronome Stripe integration is sent to Stripe automatically. Do not extend regeneration to payment collection, refunds, tax, A/R, revenue, or ledger reconciliation without separate evidence.

Metronome owns the provider schedule and invoice routing. The guide does not document how destination accounts are provisioned, reconciled, or checked for readiness before a scheduled segment becomes active.

The architecture overview names payment systems and marketplaces as the contract's delivery destination and says finalized invoices are sent to a selected downstream system at cycle close. It does not allocate configuration, payment collection, retry, or failure responsibilities, so the dedicated integration sources remain authoritative.

## Customer-provisioning configuration

The dedicated customer mutation `POST /v1/setCustomerBillingProviderConfigurations` can add multiple customer configurations across AWS Marketplace, Stripe, NetSuite, custom, Azure Marketplace, QuickBooks Online, Workday, GCP Marketplace, or Metronome. Delivery is named as direct provider API, AWS SQS, Tackle, or AWS SNS, or selected by account-level UUID `delivery_method_id`; that ID is mandatory for multiple connected Stripe accounts. Provider configuration explicitly permits arbitrary properties and the examples are not closed provider schemas. Creation makes a configuration available for later contract association but proves neither contract selection nor provider readiness, external acceptance, delivery, payment, settlement, tax, or reconciliation. [[source-metronome-api-reference-customers-set-billing-provider-configurations-for-a-customer]]

The external billing system must be connected before its customer configuration is created. Customer-level AWS configuration alone does not route invoices; a contract must select it. Beta archival makes a configuration reusable elsewhere but immediately removes it from an active contract and stops destination billing, with no replacement allowed on that contract according to this guide.

Customer creation can attach configurations for Stripe, NetSuite, AWS Marketplace, Azure Marketplace, or GCP Marketplace. Each billing configuration requires a provider; delivery can be identified by a delivery-method UUID or a named method such as direct provider delivery, AWS SQS, Tackle, or AWS SNS. Provider-specific configuration is open-ended, and its empty-object default is invalid for most provider/delivery combinations.

The optional tax-provider field lists Anrok, Avalara, and Stripe. The source limits Stripe tax calculation in this customer-creation structure to Stripe configurations using payment-intent collection methods. A separately feature-flagged revenue-system configuration currently enumerates NetSuite and expects a provider-specific customer identifier.

## Managed custom-invoice integration boundary

For billing systems outside Metronome's native integrations, Metronome documents data exports or a managed integration built on Data Export or Metronome APIs. In the QuickBooks example, the implementer owns external application and OAuth setup, external customer and item creation or lookup, storage of external identifiers in Metronome custom fields, invoice transformation, and the destination upsert. Metronome supplies the finalized-invoice event and invoice data; the selected billing system stores its customer, item, and created invoice objects. The overall pattern may inform other use cases, but the named credentials, object mappings, fields, and request are QBO-specific. The page does not assign hosting, operational support, payment collection, tax, retries, idempotency, reconciliation, or ongoing object-synchronization ownership. Workato is an optional orchestration recommendation, not a documented complete implementation of those responsibilities.

## Workato connector boundary

Metronome documents an SDK-like Workato connector for performing actions on Metronome endpoints. It gives third-party invoicing, customer provisioning, and contract provisioning as example workflows. Setup requires generating a Metronome API token and pasting it into a Workato connection, and a unique connection is required for each Metronome environment. The page does not enumerate the connector's available actions, endpoint coverage, API-token permissions, workflow triggers, data mappings, error handling, retry behavior, or connection-rotation procedure; it therefore does not establish complete endpoint coverage or broader Workato capabilities.

## Segment event-delivery integration

The Metronome (Actions) destination connects one selected Segment source using a Metronome API token and maps Segment event fields into Metronome's usage-event format. Additional Destination Actions can pair mappings with triggers containing any number of conditions, such as excluding company-domain user emails. The page calls these action configurations `subscriptions`; in this context they are Segment conditional-delivery rules, not Metronome billing subscriptions or customer contracts. It does not define token scope or rotation, trigger overlap or evaluation order, duplicate delivery, retries, batching, response handling, replay, or observability.

The single-product read can expose string `netsuite_internal_item_id` and `netsuite_overage_item_id` on initial/current state and update entries. Both schemas describe those fields as dependent on the client's configuration. Their presence is a product response surface, not evidence of mapping correctness, NetSuite integration readiness, synchronization, invoice delivery, accounting, revenue posting, or reconciliation.

## Salesforce outbound data sync

The dedicated customer mutation `POST /v1/customers/{customer_id}/updateConfig` exposes nullable `salesforce_account_id` as its only concrete configuration field and expressly leaves name and ingest aliases outside its scope. Its sparse HTTP `200` response contains no body, and the page does not define Salesforce-account validation, uniqueness, reassignment, null-as-unlink behavior, read-after-write visibility, Census pickup timing, Salesforce acceptance, or synchronization recovery. A successful Metronome mutation is therefore configuration-result evidence, not proof that the daily outbound integration has propagated or committed the linkage in Salesforce. [[source-metronome-api-reference-customers-update-a-customer-configuration]]

Metronome's native Salesforce integration uses Census as an ETL layer to push Metronome data into Salesforce daily. Setup installs the Metronome-Salesforce package, creates a Census workspace, links Census to a Salesforce Production or Sandbox destination, and selects either all Metronome customers or only those associated with Salesforce accounts; the process is repeated for every Metronome environment that should sync. After setup, the first syncs start automatically and can take a couple of hours; later syncs run once per day and cannot currently be configured more frequently. Completed-run monitoring reports attempted, successful, and failed changed rows by object type, and its downloadable error CSV is only a sample of up to 100 failures. The guide does not define credential rotation, package lifecycle, retries, recovery, object-ordering or atomicity, deletion handling, or proof of Salesforce visibility for rows reported successful.



## Sources

- [[source-metronome-api-reference-customers-set-billing-provider-configurations-for-a-customer]] - customer-level provider configuration creation, delivery routes, identifier layers, open provider schema, and downstream authority boundaries

- [[source-metronome-api-reference-settings-list-account-level-billing-providers]] — account-level billing-provider delivery-method enumeration, configuration exposure, pagination, and identifier boundaries

- [[source-github-ai]] - Metronome-authored AI skills, operational controls, migration workflow, and evidence limitations
- [[source-github-metronome-node]] - exact `@metronome/sdk@3.10.0` package, runtime, transport, generated API, and evidence boundaries
- [[source-github-terraform-provider-metronome]] - experimental Terraform provider configuration and empty resource/data-source boundary at `0.1.0-alpha.3`

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

- [[source-metronome-api-reference-settings-set-up-account-level-billing-provider]] — account-level marketplace provider setup, open configuration payload, returned delivery-method identifier, credential examples, and lifecycle boundaries


- [[source-metronome-api-reference-invoices-get-an-invoice]] - nullable external billing and revenue-system records, provider and sync diagnostics, beta totals and tax fields, and downstream-outcome boundaries


- [[source-metronome-integrations-marketplace-integrations-aws]] — AWS Marketplace listing, IAM delegation, customer and contract configuration layers, metering behavior, and downstream limits

- [[source-metronome-api-reference-products-get-a-product]] - configuration-dependent NetSuite item identifiers in product state and updates, with readiness, synchronization, delivery, accounting, and reconciliation boundaries

- [[source-metronome-api-reference-products-list-products]] — configuration-dependent NetSuite item-ID fields in product initial, current, and update schemas, with mapping and synchronization boundaries

- [[source-metronome-integrations-platform-integrations-sfdc-integration]] - outbound Census-powered Salesforce sync, per-environment setup, customer selection, daily cadence, changed-row monitoring, failure sampling, and downstream boundaries




- [[source-metronome-integrations-invoice-integrations-netsuite]] - Public Beta NetSuite billing and revenue-system modes, product and customer mappings, contract routing, sync-state recovery, and downstream authority boundaries

- [[source-metronome-api-reference-sdks]] — first-party Python, Go, Ruby, and Node.js SDK overview, generic typed/pagination/retry features, bearer-token setup, and end-to-end application integration walkthrough

## Related

- [[metronome-customers-and-contracts]]
- [[metronome-invoicing]]
- [[metronome-products-and-rate-cards]]
- [[metronome-webhooks]]
- [[stripe]]
