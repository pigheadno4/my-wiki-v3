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

`POST /v1/contracts/archive` permanently ends and archives a contract and all its terms when an incorrectly created contract must be removed from a customer. The record is not deleted: it remains available to `ListContracts` with `include_archived=true` and through the UI's "Show archived" option. `ArchiveContractPayload` requires UUID `customer_id`, UUID `contract_id`, and boolean `void_invoices`; the enclosing OpenAPI `requestBody` is not marked required, so omitted-body behavior is undocumented. The page does not define restoration, retention, propagation timing, read-after-write consistency, duplicate-call behavior, concurrency ordering, or partial-failure recovery. [[source-metronome-api-reference-contracts-archive-a-contract]]

### Deprecated Plans listing boundary

`GET /v1/plans` is a deprecated bearer-authenticated Plans endpoint that lists legacy plan records with optional cursor pagination. The response requires a plan array plus a nullable `next_page`; each plan requires a UUID `id`, `name`, and `description`, with an optional string-valued custom-field map. Metronome directs new clients to Contracts, but this source does not name an equivalent Contracts route, define a Plan-to-Contract field or identity mapping, supply a migration procedure, or state a removal date.

### Historical invoice migration

A migration can recreate a contract with its original start and starting credit or commit balances while setting `usage_statement_schedule.invoice_generation_starting_at` to the first period Metronome should generate. In the worked example, a June 1 contract and August 1 generation start produce an August draft but no June or July invoices; those earlier periods are added through `/v1/contracts/createHistoricalInvoices`. The source does not establish whether imports appear in contract edit history, mutate contract terms after creation, or may overlap existing Metronome invoice periods.

- A basic contract can apply predefined list prices from a rate card.
- Contract-level terms can add negotiated discounts or commitments.
- Contracts can modify rate-card prices and hold fixed-product prices, but the product guide does not define price precedence or contract lifecycle behavior.
- The contract `starting_at` time determines the billing periods for which invoices are generated.
- Current-period usage appears on a draft invoice, and the guide says its line items update seconds after Metronome receives usage data.

This introductory source does not define the full contract schema, amendment lifecycle, or invoice-state machine; those require dedicated contract and invoicing references.

The architecture guide frames each contract as answering what the customer buys, how they pay, and where charges are delivered. It lists pay-as-you-go arrears, prepaid credits, subscriptions with overage, enterprise commitments, and hybrids, while leaving request validation, effective-time semantics, amendments, and state transitions to dedicated references.

For a grandfathered customer that opts into new pricing, the pricing-change guide gives two individual routes: end the existing contract and re-provision it with the new package, or edit the contract directly with customer-specific changes such as negotiated overrides. The page does not define termination timing, proration, continuity, amendment history, override precedence, invoice recalculation, or either route's complete request schema.

Metronome account hierarchies link distinct parent and child customers through their contracts. The guide limits a hierarchy to one parent-child level and 10 active nodes, requires every customer to retain its own contract, and configures the relationship during contract creation. A child contract identifies both the parent customer and parent contract, then selects parent-versus-self payment and consolidated-versus-separate usage-statement behavior. Each child's usage remains separately rated under that child's contract; parent tiered pricing applies only to direct parent usage, not aggregated child usage. For shared parent-commit access, both contracts must be active during the same period. The guide does not define reparenting, detachment, deletion, concurrent hierarchy changes, or validation responses.

### Customer balance views

Metronome documents `/getNetBalance` as a customer-scoped single aggregate with filters for balance type, currency, pending charges, and custom fields. `listBalances` provides the detailed per-credit or per-commit alternative. The page does not define whether the aggregate crosses all customer contracts, how customer- and contract-level balances interact, how hierarchy affects the result, or whether reads are snapshot-consistent.

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

A general contract edit can be made in the UI or through `editContract`; the guide's supported surface spans commits, recurring commits, credits, recurring credits, overrides, scheduled charges, spend-threshold configuration, and contract name and end date changes. Draft invoices immediately reflect an edit, while finalized invoices remain unchanged unless voided and regenerated from current contract state.

Keep three related surfaces distinct: `getEditHistory` lists recorded changes, `getContract` with `as_of_date` retrieves full contract state at a historical point, and all edits also enter Metronome audit logs available through the UI and API. The guide names an edit-history contributor `updateEndDate`, while the dedicated history source names `updateContractEndDate`; current runtime naming is unresolved. The guide also says to use the first edit's `created_at` for `as_of_date`, although its edit records expose `timestamp`, the shown contract state's `created_at` predates the first edit, and no request is displayed, so the exact timestamp source remains unresolved.

Contract-level overrides layer customer-specific rate or entitlement changes over rate-card defaults. Applicable overrides do not stack on one usage-invoice line: an overwrite takes precedence over multiplier or tiered overrides, the last-added overwrite wins among overwrites, and multiplier prioritization chooses either the lowest multiplier or the lowest explicit priority value. Despite its title, the override guide shows only contract-create requests and does not document how to add, update, end, or remove an override on an existing contract.

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

## Subscription, trial, and metric-discovery extensions

- A purchased subscription plan is represented through a customer contract. The subscription guides assign quantity, proration, collection direction, applicable rate or rates, and associated credits to contract provisioning, but do not define complete request schemas or multi-rate resolution.
- Subscription upgrades and downgrades use renewal transitions in the lifecycle guide. Only upgrades are prorated; downgrades take effect next period. Most cancellations should end the contract, and later restarts should create a new contract so the contract remains the active-plan record.
- A PayGo illustration provisions a Stripe customer, attaches its ID through a Metronome customer billing-provider configuration, and then creates a contract. Its Best payload uses top-level `ending_at`, conflicting with the create-contract API's exclusive `ending_before`; preserve the six-month intent but verify the schema.
- A manual payment-gated commit can be added only to an existing contract with valid billing configuration; the customer needs a configured default payment method and stored address. The source does not define complete edit validation, idempotency, concurrency, or authorization.
- Trial examples place one-week credits or overrides inside a one-year contract. Credit depletion or expiry can expose later usage to arrears pricing, while an expired multiplier-0 override returns selected usage to list pricing; no distinct paid-state transition is documented.
- `GET /v1/customers/{customer_id}/billable-metrics` lists metrics available to one customer. `on_current_plan=true` narrows the list, but the source does not explain how “current plan” maps to contracts, rate cards, multiple or scheduled contracts, or metric-association provenance.
- Commercial-design planning should make prepaid-versus-arrears terms, seat and usage interaction, commitments and overages, ramp and multi-year structures, exceeded-limit policy, and segment-specific payment terms explicit. The planning guide does not itself establish supported contract fields, lifecycle behavior, or enforcement.

## Sources

- [[source-metronome-api-reference-contracts-archive-a-contract]] — permanent contract archival, historical visibility, required request flags, and lifecycle unknowns

- [[source-metronome-api-reference-plans-list-plans]] — deprecated `GET /v1/plans` route, bearer authentication, cursor pagination, legacy Plan response schema, and Contracts migration boundary

- [[source-metronome-guides-pricing-packaging-make-pricing-changes-make-a-pricing-change]] — cohort grandfathering and individual re-provision-versus-edit pricing routes
- [[source-metronome-guides-pricing-packaging-make-pricing-changes-edit-or-override-a-contract]] — customer-specific contract override types, targeting, precedence, and undocumented edit lifecycle
- [[source-metronome-guides-pricing-packaging-make-pricing-changes-edit-contract]] — general contract-edit channels, historical edit records, `as_of_date` full-state retrieval, UI/API audit logs, and documented endpoint/timestamp ambiguities

- [[source-metronome-guides-pricing-packaging-billing-model-guides-model-hierarchical-customer-relationships]] — one-level parent-child contract model, payer and statement behavior, separate rating, and hierarchy limits

- [[source-metronome-guides-invoices-invoice-optimization-import-existing-invoices]] - original contract-state recreation, invoice-generation cutoff, and dedicated historical-invoice import boundary

- [[source-metronome-guides-events-send-usage-events]] — customer-ID and ingest-alias attribution for usage events

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
- [[source-metronome-guides-pricing-packaging-subscription-subscription-overview]] — contract-level subscription quantity, proration, collection, and credits
- [[source-metronome-guides-pricing-packaging-subscription-define-subscription-pricing]] — quantity, credits, and applicable-rate provisioning
- [[source-metronome-guides-pricing-packaging-subscription-manage-subscription-lifecycle]] — transitions, proration, cancellation, and finalized-period boundary
- [[source-metronome-guides-pricing-packaging-billing-model-guides-pay-as-you-go]] — illustrative PayGo provisioning and ending-field conflict
- [[source-metronome-guides-pricing-packaging-apply-credits-and-commits-manual-payment-gated-commits]] — existing-contract and customer prerequisites
- [[source-metronome-guides-pricing-packaging-billing-model-guides-create-a-trial]] — contract-layered capped and uncapped trial periods
- [[source-metronome-api-reference-billable-metrics-get-billable-metrics-for-a-customer]] — customer-scoped metric discovery and current-plan filter
- [[source-metronome-guides-implement-metronome-planning-your-billing-architecture]] — commercial-design axes and implementation unknowns
- [[source-metronome-guides-customers-billing-optimize-customer-experience-get-remaining-balance]] — customer aggregate and individual credit-or-commit balance views

## Related

- [[metronome-event-ingestion]]
- [[metronome-products-and-rate-cards]]
- [[metronome-invoicing]]
- [[metronome-integrations]]
- [[metronome-credits-and-commits]]
- [[metronome-api-idempotency]]
- [[metronome-subscriptions]]
