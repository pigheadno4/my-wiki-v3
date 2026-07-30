---
title: "Metronome Customers and Contracts"
type: concept
category: technology
tags: [metronome, customers, contracts, invoicing]
---

## Definition

Metronome customers are the billing entities to which usage is attributed. Contracts represent the commercial terms a customer has agreed to pay, generally starting from a rate card with optional negotiated discounts or commitments layered on top.

## Customer matching

An ingest alias associates an application-defined identifier with a Metronome customer. The SDK guide recommends this pattern when usage starts before the customer exists in Metronome: send the application's customer-table ID in events, then register it as an alias when provisioning the customer.

An ingest alias is also a persistent idempotency boundary: it cannot be moved to another customer until it is removed from the original customer, even when the original customer is archived.

Because aliases can match events sent before or after the Metronome customer exists, the event guide recommends keeping Metronome out of the producer's critical customer-creation path: create the application customer first, then create the matching Metronome customer asynchronously.

The provisioning guide additionally treats aliases as an enterprise hierarchy mechanism: one Metronome customer can receive usage from sub-organization aliases, with group keys shaping invoice presentation. It explicitly says adding an alias later retroactively associates earlier usage carrying that alias.

## Customer creation API

`POST /v1/customers` creates a customer for product-led or sales-led provisioning. `name` is the only required payload property; values longer than 160 characters are truncated. A customer may receive up to 2,000 ingest aliases of 1–128 characters each, while the older `external_id` field is deprecated.

Billing-provider and revenue-system configurations can be attached during creation or added later. A contract must select the intended customer configuration because one customer can have multiple invoice destinations. The narrative calls the returned identifier `customer_id`, while the response schema exposes it as `data.id`.

The implementation guide states that a customer needs at least one contract before rating begins. A customer can hold several provider configurations, while each contract selects one, separating customer creation from rating and invoice routing.

## Contract and invoice behavior

- A basic contract can apply predefined list prices from a rate card.
- Contract-level terms can add negotiated discounts or commitments.
- Contracts can modify rate-card prices and hold fixed-product prices, but the product guide does not define price precedence or contract lifecycle behavior.
- The contract `starting_at` time determines the billing periods for which invoices are generated.
- Current-period usage appears on a draft invoice, and the guide says its line items update seconds after Metronome receives usage data.

This introductory source does not define the full contract schema, amendment lifecycle, or invoice-state machine; those require dedicated contract and invoicing references.

The architecture guide frames each contract as answering what the customer buys, how they pay, and where charges are delivered. It lists pay-as-you-go arrears, prepaid credits, subscriptions with overage, enterprise commitments, and hybrids, while leaving request validation, effective-time semantics, amendments, and state transitions to dedicated references.

## Contract creation API

The implementation workflow names six prerequisites: connected usage events, a billable metric, product, rate card, customer, and customer billing-provider configuration. Its worked contract combines an effective start, rate-card alias, provider routing, prepaid commit, scheduled charge, and usage-statement schedule. The page does not reconcile its customer-level configuration prerequisite with the contract-level `billing_provider_configuration` sample.

`POST /v1/contracts/create` requires only `customer_id` and `starting_at` at the top level. Optional structures can apply a rate card or package, commits and credits, overrides, scheduled charges, subscriptions, usage routing, thresholds, provider configuration, and hierarchy behavior.

Important creation constraints include:

- `starting_at` is inclusive and `ending_before` is exclusive.
- `package_id` invokes a restricted package-provisioning mode in which only the documented small field subset is accepted; `package_alias` is mutually exclusive with `package_id`.
- Subscription quantity requirements depend on `quantity_management_mode`: quantity-only needs `initial_quantity`, while seat-based needs `seat_config`.
- `uniqueness_key` can prevent duplicate creation; its schema says reuse fails with HTTP 409.
- The scheduled-charge consolidation setting cannot be changed after the contract is created.

Rate-card aliases can stand in for generated IDs during provisioning, and contract overrides can change tier boundaries or prices for one customer. The rate-card guide says categorically that all contracts are built on cards, while this API surface treats package or rate-card selection as optional; no source explains whether a default or package-resolved card fills that gap.

## Prepaid threshold configuration

`prepaid_balance_threshold_configuration` adds contract-level automatic recharge. It defines the eligible balance threshold, recharge target, commit attribution, enablement, and optional payment gate. Changes take effect immediately and force an evaluation of the customer's current balance.

With payment gating enabled, a failed payment changes `is_enabled` to `false`; Metronome does not retry automatically. Setting it back to `true` causes another balance evaluation and payment attempt. The threshold guide does not define duplicate-evaluation suppression or concurrency ordering.

## Contract edit history

`POST /v2/contracts/getEditHistory` returns the recorded edit history for one customer contract. Metronome describes this as a full history spanning changes made in the UI, through `editContract`, and through other contract-changing endpoints. Each `ContractEdit` can identify when an edit occurred and group the additions, updates, archives, and removals it contained, including changes to pricing overrides, discounts, charges, commits, credits, subscriptions, usage filters, contract dates, and threshold configuration.

The targeted `POST /v2/contracts/commits/edit` operation is narrower than a general contract edit: it identifies one existing customer- or contract-level commit and changes that commit's fields, schedules, applicability, invoicing contract, rate type, priority, or hierarchy access.

## Legacy contract amendments

`POST /v1/contracts/amend` is a legacy mutation endpoint. Metronome directs new clients to `editContract` and says amendment access is removed once Contract editing is enabled.

The legacy request requires customer ID, contract ID, and an inclusive `starting_at`, and can add commits, credits, overrides, scheduled charges, and client-configured commercial fields. Its schema does not define whether omitted fields preserve state, whether arrays append or replace, how backdating interacts with invoice state, whether nested changes are atomic, or what the response `data.id` identifies.

## Edits and transitions

The enterprise guide distinguishes two lifecycle operations. An edit adds terms without starting a new contract. A transition starts a new contract, preserves its relationship to the original, and can apply renewal logic such as rolling over unused commitments or credits.

For recurring-grant upgrades, a renewal at the next period removes future old-contract charges and creates a finalized scheduled invoice plus a new draft usage invoice. A mid-period renewal prorates the first grant and finalizes old-contract usage through the transition date. A backdated renewal moves open-period usage to the replacement contract and uses a one-time adjustment before forward recurrence begins.

## Billing-provider schedule

A beta workflow permits attaching a billing provider to a previously unconfigured contract at the current period start, including marketplace metering for the whole period. This differs from the next-period-only marketplace transition rule below; the documentation does not establish whether initial attachment and provider-to-provider transition intentionally have different timing.

An existing contract can change invoice destinations without being replaced. `add_billing_provider_configuration_update` on `POST v2/contracts/edit` adds a segment at `START_OF_CURRENT_PERIOD` or `START_OF_NEXT_PERIOD`; the full ordered schedule is returned separately from the backward-compatible currently active configuration.

Stripe-to-Stripe and Stripe/NetSuite transitions may start in the current or next period. Any transition to or from AWS, Azure, or GCP Marketplace is next-period only, and threshold billing must be removed before moving to a marketplace. A contract supports at most 10 schedule segments unless the account team grants more capacity.

## Stripe Dashboard contract management

The Metronome Stripe App embeds customer and contract management in the Stripe Dashboard. It lists Stripe customers linked through Metronome billing-provider configurations and can automatically create a corresponding Metronome customer when contract creation starts. Its four-step wizard configures invoice terms, rate-card pricing and overrides, subscription quantities and product entitlement, credit schedules, and confirmation. The resulting contract uses the Stripe customer's existing billing-provider configuration for invoice delivery.

## Metronome dashboard provisioning

The Metronome dashboard quickstart creates a customer, optionally assigns ingest aliases, and then creates a contract with a rate card and start and end dates. The contract can also select a billing provider and include customer-specific prepaid commits or overrides.

## Sources

- [[source-metronome-guides-get-started-developer-sdks]] — customer aliases, basic contract provisioning, and introductory invoice behavior
- [[source-metronome-api-reference-contracts-create-a-contract]] — create endpoint, request families, conditional requirements, and response boundary
- [[source-metronome-api-reference-contracts-get-contract-edit-history]] — cross-channel contract change history and response structure
- [[source-metronome-guides-get-started-stripe-marketplace-app]] — Stripe Dashboard customer and contract management workflow
- [[source-metronome-guides-pricing-packaging-billing-model-guides-enterprise-commit]] — enterprise provisioning, edits, transitions, and renewal rollover
- [[source-metronome-guides-get-started-metronome-dashboard-quickstart]] — dashboard customer and contract provisioning
- [[source-metronome-guides-pricing-packaging-apply-credits-and-commits-create-a-pre-paid-commit]] — recurring grants, renewal transitions, and upgrade timing
- [[source-metronome-guides-customers-billing-optimize-customer-experience-prepaid-balance-thresholds]] — contract threshold configuration, immediate evaluation, and failed-payment disablement
- [[source-metronome-api-reference-credits-and-commits-edit-a-commit]] — targeted commit edit boundary
- [[source-metronome-guides-customers-billing-manage-customers-schedule-billing-provider-change]] — contract provider schedules, transition matrix, and segment limit
- [[source-metronome-api-reference-idempotency]] — ingest-alias reuse, supported uniqueness keys, and HTTP 409 conflict behavior
- [[source-metronome-api-reference-customers-create-a-customer]] — provisioning flow, alias limits, optional downstream configuration, and response boundary
- [[source-metronome-api-reference-contracts-amend-a-contract]] — legacy amendment lifecycle, mutation surface, and undocumented state semantics
- [[source-metronome-guides-implement-metronome-core-concepts-send-usage-events]] — asynchronous customer provisioning and ingest-alias matching boundary
- [[source-metronome-guides-implement-metronome-core-concepts-create-products-contracts]] — product price-ownership boundary and contract modification context
- [[source-metronome-guides-get-started-how-metronome-works]] — contract what/how/where boundary and commercial-model examples
- [[source-metronome-guides-implement-metronome-core-concepts-provision-contract]] — provisioning prerequisites, charge schedules, provider attachment, and usage-filter routing
- [[source-metronome-guides-implement-metronome-core-concepts-create-manage-rate-cards]] — alias provisioning, reusable standard pricing, customer tier overrides, and card relationship tension
- [[source-metronome-guides-implement-metronome-core-concepts-provision-customer]] — alias hierarchy, retroactive association, contract rating boundary, and provider assignment

## Related

- [[metronome-event-ingestion]]
- [[metronome-products-and-rate-cards]]
- [[metronome-invoicing]]
- [[metronome-integrations]]
- [[metronome-credits-and-commits]]
- [[metronome-api-idempotency]]
