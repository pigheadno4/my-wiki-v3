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

## Customer retrieval API

Bearer-authenticated `GET /v1/customers/{customer_id}` requires a Metronome UUID path parameter and returns detailed customer identity, timestamps, ingest aliases, customer configuration, and custom fields under `data`. Its schema retains required-but-deprecated `external_id`; the page directs billing-configuration searches to `/getCustomerBillingConfigurations` and does not equate `customer_config` with a billing-provider configuration. Optional `archived_at` is nullable, while optional `current_billable_status` is client-configuration-dependent. The page documents only HTTP `200` and leaves not-found behavior, freshness, archived-customer retrieval, and status derivation undefined. [[source-metronome-api-reference-customers-get-a-customer]]


### Customer list API

Bearer-authenticated `GET /v1/customers` returns active customers by default and can filter by one ingest alias, up to 100 customer IDs, only archived customers, or up to 100 Salesforce account IDs. It uses optional 1-100 `limit` and `next_page` query parameters and requires a customer-detail array plus nullable `next_page` in a successful response. The endpoint does not define filter-intersection semantics, result ordering, default page size, cursor lifetime, snapshot consistency, or freshness. [[source-metronome-api-reference-customers-list-customers]]

The Salesforce integration can synchronize every Metronome customer or only customers linked to Salesforce accounts. The UI link stores a supplied Salesforce account ID on the Metronome customer, and the guide says the association can also be made during programmatic customer creation without supplying the request contract. The Salesforce objects include customer identity and the associated Salesforce-account lookup when present. The distinct customer-ingest-alias object carries the Metronome alias ID, customer lookup, alias value, and environment. Contract records link customer and rate card and expose inclusive UTC start, nullable exclusive UTC end, and usage-statement schedule frequency. The page does not define account-ID validation, uniqueness, reassignment, unlinking, linkage freshness, exact programmatic field, or row deletion and archive behavior. For the alias replica, it likewise does not establish alias uniqueness, current-active status, reassignment, deletion, ordering, event-matching freshness, or synchronization atomicity.



## Customer name update API

Bearer-authenticated `POST /v1/customers/{customer_id}/setName` targets a required UUID path identifier. Its JSON payload schema requires string `name`, while the enclosing `requestBody` is not marked required; names longer than 160 characters are truncated. HTTP `200` requires `data` containing a customer whose required identity fields are UUID `id`, deprecated `external_id`, `ingest_aliases`, and the updated `name`. Metronome says the new name is applied immediately across all billing documents and interfaces, but this page does not define the scope across historical, draft, finalized, exported, rendered, or downstream-provider copies; archived-customer eligibility; errors; concurrency; or partial-failure recovery. [[source-metronome-api-reference-customers-update-a-customer-name]]

## Customer creation API

`POST /v1/customers` creates a customer for product-led or sales-led provisioning. `name` is the only required payload property; values longer than 160 characters are truncated. A customer may receive up to 2,000 ingest aliases of 1–128 characters each, while the older `external_id` field is deprecated.

Billing-provider and revenue-system configurations can be attached during creation or added later. A contract must select the intended customer configuration because one customer can have multiple invoice destinations. The narrative calls the returned identifier `customer_id`, while the response schema exposes it as `data.id`.

The implementation guide states that a customer needs at least one contract before rating begins. A customer can hold several provider configurations, while each contract selects one, separating customer creation from rating and invoice routing.

### NetSuite customer and contract routing layers

A Metronome customer can hold multiple NetSuite billing or revenue-system configurations, but a configuration does not route invoices until the relevant configuration ID is selected on a contract. Billing configuration sends finalized contract invoices to NetSuite for NetSuite-owned distribution, tax, and collection. Revenue-system configuration sends invoices and available payment state after billing occurs elsewhere; a failed first payment can leave the NetSuite invoice `OPEN`, followed by a retroactive `PAID` update after later success. The external `netsuite_customer_id`, account-level `delivery_method_id`, and contract selectors `billing_provider_configuration_id` or `revenue_system_configuration_id` remain distinct identity layers.

## Customer archival API

On the documented production server `https://api.metronome.com`, top-level bearer-secured `POST /v1/customers/archive` takes a JSON `Id` payload whose required property is UUID `id`, while the enclosing `requestBody` is not marked required. Metronome positions archival for a mistakenly onboarded customer, makes it irreversible, keeps the customer visible through the API and UI for audit, automatically archives all contracts as of the current date, and voids all corresponding invoices. Ingest aliases remain reserved unless removed before archival. The page does not define retention, archive timestamp propagation, read-after-write consistency, contract or invoice state partitioning, atomicity, repeated-call behavior, or partial-failure recovery. [[source-metronome-api-reference-customers-archive-a-customer]]


## Contract and invoice behavior

`POST /v1/contracts/customerCredits/create` creates one customer-level credit that can be limited with `applicable_contract_ids` or used across all of the customer's contracts when that selector is omitted; the prose also calls an empty value cross-contract. Metronome recommends contract create or edit for most credits. The endpoint does not define behavior for invalid, archived, duplicate, foreign-customer, or later-created contract IDs, nor customer-credit lifecycle or read-after-write visibility. [[source-metronome-api-reference-credits-and-commits-create-a-credit]]

Bearer-authenticated `POST /v1/contracts/getContractRateSchedule` reads the entitled rate schedule for one customer contract. Required payload properties identify the customer and contract, optional `at` selects overlapping schedule segments and defaults to the current timestamp, and selectors use OR semantics across selector objects while supplying no selectors returns all rates. The result incorporates the contract's rate card, scheduled changes, and overrides but does not establish invoice, authorization, freshness, or snapshot-consistency behavior. [[source-metronome-api-reference-contracts-get-the-rate-schedule-for-a-contract]]

`POST /v1/contracts/updateInvoiceIssueDate` changes the issue date of one identified draft invoice without changing the contract's terms or later billing cycles. Metronome directs callers to edit-contract or edit-commit operations when the future billing schedule must also change; this page does not establish those operations' request contracts or the rescheduling mutation's concurrency and recovery behavior. [[source-metronome-api-reference-contracts-update-invoice-issue-date]]

`POST /v1/contracts/archive` permanently ends and archives a contract and all its terms when an incorrectly created contract must be removed from a customer. The record is not deleted: it remains available to `ListContracts` with `include_archived=true` and through the UI's "Show archived" option. `ArchiveContractPayload` requires UUID `customer_id`, UUID `contract_id`, and boolean `void_invoices`; the enclosing OpenAPI `requestBody` is not marked required, so omitted-body behavior is undocumented. The page does not define restoration, retention, propagation timing, read-after-write consistency, duplicate-call behavior, concurrency ordering, or partial-failure recovery. [[source-metronome-api-reference-contracts-archive-a-contract]]


A provisioned contract is the primary invoice-generation mechanism and produces invoices on predefined schedules throughout its lifecycle. Usage invoices follow the contract's usage-statement cadence, while commitments and scheduled charges can produce scheduled invoices. Draft usage invoices update as usage arrives; finalized invoices no longer change, and their distribution and collection follow contract billing configuration without establishing provider acceptance or payment success. [[source-metronome-guides-implement-metronome-core-concepts-how-invoicing-works]]

### Deprecated Plans listing boundary

Bearer-authenticated `GET /v1/planDetails/{plan_id}` requires a UUID Plan ID and returns high-level configuration for one legacy Plan. The detail representation requires plan `id`, `name`, and `custom_fields` while leaving `description` optional; the separate Plan-list representation instead requires `description` and leaves `custom_fields` optional. Preserve operation-specific requiredness. Metronome directs new clients to Contracts but supplies no replacement endpoint, Plan-to-Contract identity or field mapping, migration procedure, compatibility period, or removal date. [[source-metronome-api-reference-plans-get-plan-details]]

The deprecated Plans `POST /v1/credits/listEntries` endpoint lists credit ledgers across customers and directs new clients to Contracts. The page does not name an equivalent Contracts route, map Plan credit-grant or ledger identity to Contract credits or commits, provide migration steps, or state a removal date. Its exclusion of entries associated with voided grants is a Plans-surface visibility rule and does not establish current Contracts archival or ledger-retention behavior. [[source-metronome-api-reference-credit-grants-list-credit-ledger-entries]]

`GET /v1/plans` is a deprecated bearer-authenticated Plans endpoint that lists legacy plan records with optional cursor pagination. The response requires a plan array plus a nullable `next_page`; each plan requires a UUID `id`, `name`, and `description`, with an optional string-valued custom-field map. Metronome directs new clients to Contracts, but this source does not name an equivalent Contracts route, define a Plan-to-Contract field or identity mapping, supply a migration procedure, or state a removal date.

The deprecated Plans `POST /v1/credits/voidGrant` page directs new clients to Contracts but does not identify a replacement Contracts operation, map Plan grant identity to a contract credit or commit, provide migration steps, or state a removal date. [[source-metronome-api-reference-credit-grants-void-a-credit-grant]]

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

The seat-specific alternative is `POST /v1/contracts/seatBalances/list`, whose supplied JSON object requires both customer and contract UUIDs and returns balances from that contract's seat-based subscriptions. It can filter by subscription or seat, request sibling seat-level credit and commit objects plus their nested ledgers, and paginate seats through a body cursor. The expanded object schemas omit `credit_type_id`, so they cannot be mapped from this response alone to the per-credit-type balance entries. Unlike the customer-level `customerBalances/list` envelope, HTTP 200 requires a nested `pagination` object with seat counts and an optional nullable `next_page`; the endpoint does not define hierarchy behavior, seat order, cursor lifetime, snapshot consistency, freshness, cross-contract aggregation, or reconciliation. [[source-metronome-api-reference-credits-and-commits-list-seat-balances]]

Metronome documents `/getNetBalance` as a customer-scoped single aggregate with filters for balance type, currency, pending charges, and custom fields. `listBalances` provides the detailed per-credit or per-commit alternative. The page does not define whether the aggregate crosses all customer contracts, how customer- and contract-level balances interact, how hierarchy affects the result, or whether reads are snapshot-consistent.

The detailed view is `POST /v1/contracts/customerBalances/list`. Its JSON payload requires the customer UUID and can filter by access-window dates, with exclusive `effective_before`; the body wrapper itself is not marked required. HTTP 200 requires an object containing a Commit-or-Credit `data` array and nullable `next_page`. This endpoint puts `next_page` and a 1-25, default-25 `limit` in the JSON body, unlike the general pagination authority's query parameters and 100 cap.

`include_contract_balances` requests contract-level records. `include_archived` says "archived credits and credits from archived contracts," while Commit alone exposes `archived_at` and Credit does not. The contract-archive authority establishes that associated commits and credits are archived. The list surface still does not establish omitted-flag behavior, whether archived commits are returned, how Credit exposes archive status, how the repeated-credit wording partitions results, hierarchy effects, response ordering, cursor lifetime, or snapshot consistency.

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

Package creation is customer agnostic; customer binding occurs later through `/contracts/create`. In package mode, the guide says contract creation accepts only `package_id` or `package_alias` plus `transition`, and additional terms return HTTP 400. The provisioned contract retains an attached package ID visible in the app, data export, and API. [[source-metronome-guides-implement-metronome-core-concepts-packages-overview]]

## Prepaid threshold configuration

`prepaid_balance_threshold_configuration` adds contract-level automatic recharge. It defines the eligible balance threshold, recharge target, commit attribution, enablement, and optional payment gate. Changes take effect immediately and force an evaluation of the customer's current balance.

With payment gating enabled, a failed payment changes `is_enabled` to `false`; Metronome does not retry automatically. Setting it back to `true` causes another balance evaluation and payment attempt. The threshold guide does not define duplicate-evaluation suppression or concurrency ordering.

The 2026-08-28 warehouse schema adds created-commit duration value and unit, rollover fraction, and rate type to `contracts_prepaid_balance_threshold_configurations`. This export surface helps inspect configured contract state but does not establish edit-request support, propagation timing, or payment recovery behavior. [[source-metronome-guides-reporting-insights-data-export-database-reference]]

## Contract edit history

The targeted `POST /v2/contracts/commits/edit` operation identifies one existing customer- or contract-level commit with `customer_id` and `commit_id` and changes that commit rather than the whole contract. For a customer-level commit, nullable `applicable_contract_ids` can select contracts and `null` means all of the customer's contracts; that field cannot be edited for `POSTPAID` or contract-level commits. Omission, empty-array, invalid-ID, later-contract, visibility, and conditional-error behavior remain undocumented. [[source-metronome-api-reference-credits-and-commits-edit-a-commit]]

Bearer-authenticated `POST /v2/contracts/edit` mutates one identified customer contract and requires contract-editing enablement. Within a supplied payload, UUID `customer_id` and `contract_id` are required; the enclosing `requestBody` is not marked required and top-level `additionalProperties` is unspecified. `update_contract_end_date` is an exclusive nullable timestamp, while `allow_contract_ending_before_finalized_invoice` defaults to `true`, permits ending before existing finalized-invoice end timestamps, leaves those invoices unchanged, and requires void-and-regenerate to incorporate the new end date. HTTP `200` requires `data.id` but makes `data.edit` optional, while the narrative promises an edit ID and complete details and the example reuses the request contract ID; edit-versus-contract identity and detail completeness are unresolved. Mixed-edit atomicity, validation order, partial success, concurrency, visibility, and recovery are not defined. [[source-metronome-api-reference-contracts-edit-a-contract]]

After contract creation, subscription capacity is edited through `update_subscription`. Aggregate updates accept total `quantity` or `quantity_delta`, while seat-based updates add or remove identified and unassigned seats; replacing an assignee without changing quantity removes the old seat ID and adds unassigned capacity. The source does not define atomicity across seat operations, validation, error mapping, concurrent-edit behavior, or when the new state becomes visible in contract reads and edit history. [[source-metronome-guides-pricing-packaging-subscription-manage-seats]]

`POST /v2/contracts/getEditHistory` returns the recorded edit history for one customer contract. Metronome describes this as a full history spanning changes made in the UI, through `editContract`, and through other contract-changing endpoints. Each `ContractEdit` can identify when an edit occurred and group the additions, updates, archives, and removals it contained, including changes to pricing overrides, discounts, charges, commits, credits, subscriptions, usage filters, contract dates, and threshold configuration.

The targeted `POST /v2/contracts/commits/edit` operation is narrower than a general contract edit: it identifies one existing customer- or contract-level commit and changes that commit's fields, schedules, applicability, invoicing contract, rate type, priority, or hierarchy access.

A general contract edit can be made in the UI or through `editContract`; the guide's supported surface spans commits, recurring commits, credits, recurring credits, overrides, scheduled charges, spend-threshold configuration, and contract name and end date changes. Draft invoices immediately reflect an edit, while finalized invoices remain unchanged unless voided and regenerated from current contract state.

Keep three related surfaces distinct: `getEditHistory` lists recorded changes, `getContract` with `as_of_date` retrieves full contract state at a historical point, and all edits also enter Metronome audit logs available through the UI and API. The guide names an edit-history contributor `updateEndDate`, while the dedicated history source names `updateContractEndDate`; current runtime naming is unresolved. The guide also says to use the first edit's `created_at` for `as_of_date`, although its edit records expose `timestamp`, the shown contract state's `created_at` predates the first edit, and no request is displayed, so the exact timestamp source remains unresolved.

Contract-level overrides layer customer-specific rate or entitlement changes over rate-card defaults. Applicable overrides do not stack on one usage-invoice line: an overwrite takes precedence over multiplier or tiered overrides, the last-added overwrite wins among overwrites, and multiplier prioritization chooses either the lowest multiplier or the lowest explicit priority value. Despite its title, the override guide shows only contract-create requests and does not document how to add, update, end, or remove an override on an existing contract.

`POST /v2/contracts/get` retrieves one customer contract by customer and contract UUID and can return the full contract configuration as of an RFC 3339 `as_of_date`. The endpoint's `has_more` flags mean its embedded commits or credits can be incomplete and require the respective list endpoints for full collections. Its schema does not establish freshness, snapshot consistency, or historical-balance semantics. [[source-metronome-api-reference-contracts-get-a-contract-v2]]

## Legacy contract amendments

`POST /v1/contracts/amend` is a legacy mutation endpoint. Metronome directs new clients to `editContract` and says amendment access is removed once Contract editing is enabled.

The legacy request requires customer ID, contract ID, and an inclusive `starting_at`, and can add commits, credits, overrides, scheduled charges, and client-configured commercial fields. Its schema does not define whether omitted fields preserve state, whether arrays append or replace, how backdating interacts with invoice state, whether nested changes are atomic, or what the response `data.id` identifies.

## Edits and transitions

The enterprise guide distinguishes two lifecycle operations. An edit adds terms without starting a new contract. A transition starts a new contract, preserves its relationship to the original, and can apply renewal logic such as rolling over unused commitments or credits.

For recurring-grant upgrades, a renewal at the next period removes future old-contract charges and creates a finalized scheduled invoice plus a new draft usage invoice. A mid-period renewal prorates the first grant and finalizes old-contract usage through the transition date. A backdated renewal moves open-period usage to the replacement contract and uses a one-time adjustment before forward recurrence begins.

### Account-level provider prerequisite

`POST /v1/setUpBillingProvider` inserts account-level AWS, Azure, or GCP Marketplace configuration and returns `delivery_method_id`, described as enabling later mapping of contracts across customers. The call accepts no customer or contract identifier and does not itself create a customer billing-provider configuration or select one on a contract. Because other sources separately use `delivery_method_id` at customer configuration and `billing_provider_configuration_id` at contract selection, callers must verify each downstream schema rather than treat the identifiers as interchangeable. The page defines no propagation, readiness, attachment, update, archival, or reconciliation behavior. [[source-metronome-api-reference-settings-set-up-account-level-billing-provider]]

## Billing-provider schedule

A beta workflow permits attaching a billing provider to a previously unconfigured contract at the current period start, including marketplace metering for the whole period. This differs from the next-period-only marketplace transition rule below; the documentation does not establish whether initial attachment and provider-to-provider transition intentionally have different timing.

An existing contract can change invoice destinations without being replaced. `add_billing_provider_configuration_update` on `POST v2/contracts/edit` adds a segment at `START_OF_CURRENT_PERIOD` or `START_OF_NEXT_PERIOD`; the full ordered schedule is returned separately from the backward-compatible currently active configuration.

Stripe-to-Stripe and Stripe/NetSuite transitions may start in the current or next period. Any transition to or from AWS, Azure, or GCP Marketplace is next-period only, and threshold billing must be removed before moving to a marketplace. A contract supports at most 10 schedule segments unless the account team grants more capacity.


### AWS Marketplace provisioning layers

The AWS guide configures a customer with AWS customer ID, product code, region, and a usage-based-product flag when applicable, then requires the Metronome contract to mirror the Marketplace agreement and select AWS for delivery. Its examples keep customer provider configuration separate from contract selection. When Metronome detects a Marketplace subscription change it stops metering and updates Metronome customer status, while the merchant owns application status and ending the Metronome contract when relevant. [[source-metronome-integrations-marketplace-integrations-aws]]

> [!warning] Provider-change lifecycle contradiction
> The AWS guide says a billing provider cannot be added or changed after contract creation, while [[source-metronome-guides-customers-billing-manage-customers-schedule-billing-provider-change]] documents next-period changes to and from AWS Marketplace. The sources do not resolve whether the AWS statement is stale, UI-specific, or limited to initial provisioning.

### Azure Marketplace provisioning layers

Azure provisioning requires the accepted offer's Subscription ID in customer provider configuration and Azure selection on a matching Metronome contract. On marketplace lifecycle changes, Metronome stops metering and updates its customer status, while the merchant owns application status and ending the Metronome contract when relevant. The Azure guide says the provider cannot be added or changed after contract creation, conflicting with the separate next-period marketplace-transition authority; the scope or staleness of that restriction is unresolved. [[source-metronome-integrations-marketplace-integrations-azure]]

### GCP Marketplace provisioning layers

GCP provisioning maps the marketplace Entitlement ID, also called Order ID, and Service Name onto customer provider configuration, then separately selects GCP delivery on a Metronome contract matching the accepted offer. On marketplace lifecycle changes, Metronome stops metering and updates its customer status, while the merchant owns application status and ending the Metronome contract when relevant. The GCP guide says the provider cannot be added or changed after contract creation, conflicting with the separate next-period marketplace-transition authority; the scope or staleness of that restriction is unresolved. [[source-metronome-integrations-marketplace-integrations-gcp]]

## Stripe Dashboard contract management

The Metronome Stripe App embeds customer and contract management in the Stripe Dashboard. It lists Stripe customers linked through Metronome billing-provider configurations and can automatically create a corresponding Metronome customer when contract creation starts. Its four-step wizard configures invoice terms, rate-card pricing and overrides, subscription quantities and product entitlement, credit schedules, and confirmation. The resulting contract uses the Stripe customer's existing billing-provider configuration for invoice delivery.

## Metronome dashboard provisioning

The Metronome dashboard quickstart creates a customer, optionally assigns ingest aliases, and then creates a contract with a rate card and start and end dates. The contract can also select a billing provider and include customer-specific prepaid commits or overrides.

## Subscription, trial, and metric-discovery extensions

- The product-access overview frames customer access as contract terms across packaging models. It identifies customer provisioning plus contract assignment as the basis for encoding entitlements, and routes renewal, upsell, and upgrade entitlement changes to contract lifecycle management. The page does not define transition semantics, evaluation timing, or application-side enforcement. [[source-metronome-guides-customers-billing-manage-customers-manage-product-access]]
- A purchased subscription plan is represented through a customer contract. The subscription guides assign quantity, proration, collection direction, applicable rate or rates, and associated credits to contract provisioning, but do not define complete request schemas or multi-rate resolution.
- Subscription upgrades and downgrades use renewal transitions in the lifecycle guide. Only upgrades are prorated; downgrades take effect next period. Most cancellations should end the contract, and later restarts should create a new contract so the contract remains the active-plan record.
- A PayGo illustration provisions a Stripe customer, attaches its ID through a Metronome customer billing-provider configuration, and then creates a contract. Its Best payload uses top-level `ending_at`, conflicting with the create-contract API's exclusive `ending_before`; preserve the six-month intent but verify the schema.
- A manual payment-gated commit can be added only to an existing contract with valid billing configuration; the customer needs a configured default payment method and stored address. The source does not define complete edit validation, idempotency, concurrency, or authorization.
- Trial examples place one-week credits or overrides inside a one-year contract. Credit depletion or expiry can expose later usage to arrears pricing, while an expired multiplier-0 override returns selected usage to list pricing; no distinct paid-state transition is documented.
- `GET /v1/customers/{customer_id}/billable-metrics` lists metrics available to one customer. `on_current_plan=true` narrows the list, but the source does not explain how “current plan” maps to contracts, rate cards, multiple or scheduled contracts, or metric-association provenance.
- Commercial-design planning should make prepaid-versus-arrears terms, seat and usage interaction, commitments and overages, ramp and multi-year structures, exceeded-limit policy, and segment-specific payment terms explicit. The planning guide does not itself establish supported contract fields, lifecycle behavior, or enforcement.

## Sources

- [[source-metronome-guides-customers-billing-manage-customers-manage-product-access]] - contract terms as the product-access frame, provisioning and assignment as the entitlement basis, and lifecycle navigation for renewal, upsell, and upgrade changes
- [[source-metronome-guides-pricing-packaging-subscription-manage-seats]] — post-creation aggregate and identity-bearing subscription edits, unassigned-seat reassignment, and contract-state visibility unknowns

- [[source-metronome-guides-get-started-api-quickstart]] — customer alias identity, ordered customer and contract provisioning, rate-card linkage, provider-optional invoice generation, and in-window event prerequisite

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

- [[source-metronome-api-reference-customers-get-a-customer]] — UUID-scoped customer retrieval, returned identity and alias fields, configuration-dependent status, and documented read boundaries

- [[source-metronome-api-reference-settings-set-up-account-level-billing-provider]] — account-level provider creation prerequisite, returned delivery-method identifier, and customer/contract mapping boundary

- [[source-metronome-api-reference-credits-and-commits-list-balances]] - customer-scoped detailed balance envelope, access filters, endpoint-specific pagination, contract inclusion, archive-response asymmetry, and consistency unknowns


- [[source-metronome-api-reference-customers-list-customers]] — account-wide customer filters, cursor envelope, customer-detail item shape, archived visibility, and list-consistency unknowns


- [[source-metronome-api-reference-customers-update-a-customer-name]] — UUID-scoped display-name mutation, 160-character truncation, returned customer identity, immediate billing-document/interface claim, and recovery boundaries


- [[source-metronome-guides-implement-metronome-core-concepts-how-invoicing-works]] — contract-driven invoice generation, usage-statement cadence, scheduled charges, and lifecycle boundaries


- [[source-metronome-integrations-marketplace-integrations-aws]] — AWS customer identifiers, contract routing, lifecycle ownership, and the provider-change contradiction

- [[source-metronome-api-reference-customers-archive-a-customer]] - production bearer-authenticated customer archival, irreversible lifecycle, audit visibility, contract and invoice effects, alias reservation, request schema, and lifecycle unknowns

- [[source-metronome-integrations-platform-integrations-sfdc-integration]] - Salesforce account linkage and selected-customer sync, customer and ingest-alias replicas, contract lookup and effective-time fields, and linkage and lifecycle unknowns
- [[source-metronome-guides-customers-billing-set-up-notifications-system-notifications]] - contract create, start, edit, end, and archive event policies; customer and contract payload context; and prospective account-wide enablement
- [[source-metronome-api-reference-credit-grants-list-credit-ledger-entries]] - deprecated Plans customer-ledger listing and the undocumented Contracts replacement, identity-mapping, migration, and removal-date boundaries



- [[source-metronome-api-reference-credits-and-commits-list-seat-balances]] - contract-scoped seat-balance listing, customer and contract identity, subscription and seat filters, sibling expansion attribution boundary, endpoint-specific pagination, and consistency unknowns

- [[source-metronome-integrations-invoice-integrations-netsuite]] - customer billing and revenue-system configurations, external customer identity, contract-level selection, and per-contract NetSuite routing

- [[source-metronome-api-reference-sdks]] — application-owned ingest aliases, customer and contract provisioning, rate-card linkage, and contract-start invoice behavior, with stale worked usage and a Go start date that falls after every shown event

## Related

- [[metronome-event-ingestion]]
- [[metronome-products-and-rate-cards]]
- [[metronome-invoicing]]
- [[metronome-integrations]]
- [[metronome-credits-and-commits]]
- [[metronome-api-idempotency]]
- [[metronome-subscriptions]]
