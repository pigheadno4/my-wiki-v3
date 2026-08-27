---
title: "Metronome Invoicing"
type: concept
category: technology
tags: [metronome, invoicing, stripe, marketplaces, erp]
---

## Definition

Metronome presents invoicing as a set of distribution-channel options rather than one mandatory delivery path. Its overview identifies native Stripe invoicing, marketplace invoicing for AWS, Azure, and GCP, and ERP-oriented invoicing and revenue workflows.


## Native invoice model

Bearer-authenticated `POST /v1/contracts/updateInvoiceIssueDate` reschedules one invoice only while it remains `DRAFT`; the new RFC 3339 issue date cannot be later than the contract end date. It does not modify future billing cycles or underlying contract terms. The page does not define interaction with grace periods or simultaneous finalization, read/export visibility timing, reversibility, or downstream Stripe, marketplace, ERP, tax, delivery, collection, payment, and accounting effects. [[source-metronome-api-reference-contracts-update-invoice-issue-date]]

Contracts are Metronome's primary invoice generator. Usage invoices (`USAGE`) follow a contract's usage-statement schedule, cover a billing period, update while usage arrives, and enter a configurable grace period that defaults to 24 hours. Scheduled invoices (`SCHEDULED`) cover fixed charges such as commitment prepayments, postpaid true-ups, and recurring fees; they have no grace period or billing-period boundary fields. Their documented finalization is immediate for past or present issue dates, within two hours and 30 minutes when the issue date is within two hours of contract creation, and within 30 minutes of later issue dates.

The guide names draft, grace period, finalized, and void as the four states. `FINALIZED` invoices are immutable within Metronome; a finalized invoice created in error may become `VOID` and be regenerated from updated usage and pricing. Distribution and collection follow contract billing configuration, but the guide does not prove provider delivery, settlement, payment, tax, or accounting outcomes. Its worked JSON also uses `issued_at`, `start_timestamp`, and `end_timestamp` where its schema prose names `issue_date`, `billing_period_start_date`, and `billing_period_end_date`, and its negative commitment adjustment omits quantity and unit price despite the universal line-item list. Use dedicated API schemas for exact fields. [[source-metronome-guides-implement-metronome-core-concepts-how-invoicing-works]]

## Invoicing options

| Option | Documented scope |
| --- | --- |
| Stripe Invoicing | Native Stripe integration that can use Stripe Tax, dunning, and other Stripe product-suite capabilities. |
| Marketplace Invoicing | Out-of-the-box metering and invoice creation for AWS, Azure, and GCP marketplaces, covering all Metronome charge types without a third-party integrator. |
| ERP Invoicing | Out-of-the-box and custom ERP integrations for collection, book-closing, and revenue workflows; the overview highlights NetSuite as a native option. |


### AWS Marketplace metering and delivery limits

For an AWS-selected customer, Metronome meters the accrued total across AWS-billed contract invoices since the last request as a USD-cent quantity. Prepaid commit charges follow scheduled-invoice service dates; unpaid credits suppress metering until overage remains; postpaid shortfall true-ups are not sent and remain merchant-owned. AWS accepts only positive quantities, so an overbill cannot be reduced through later Metronome credits; Metronome pauses until usage catches up or the merchant issues an AWS refund. AWS accepts records for one hour after contract end, while Metronome sends a final request after 15 minutes; later usage and outage backlog can become undeliverable. Only USD invoices are sent. [[source-metronome-integrations-marketplace-integrations-aws]]

> [!warning] AWS-specific coverage qualification
> The invoicing overview's broad statement that marketplace invoicing supports all Metronome charge types is qualified by the dedicated AWS guide's exclusions for postpaid true-up invoices and non-USD invoices.

### Azure Marketplace metering and delivery limits

For Azure Marketplace delivery, Metronome meters accrued totals since the prior request across contract invoices routed to Azure, encoded as USD cents. Scheduled prepaid purchases use the scheduled invoice service-period date; credits send only later overage; and a postpaid shortfall true-up that finalizes after the marketplace window is not sent, leaving the merchant to handle it directly in Azure. Azure's positive-quantity limit means a later credit cannot decrease an already submitted bill. [[source-metronome-integrations-marketplace-integrations-azure]]

### GCP Marketplace metering and delivery limits

For GCP Marketplace delivery, Metronome meters accrued totals since the prior request across contract invoices routed to GCP and encodes the quantity as USD cents. Scheduled prepaid purchases follow the scheduled invoice service-period date; credits send only post-drawdown overage; and a postpaid shortfall true-up that finalizes after the marketplace window is not sent. GCP's positive-only usage quantities mean a later credit cannot reduce an already reported bill; Metronome pauses until usage catches up or the merchant issues a manual GCP refund. [[source-metronome-integrations-marketplace-integrations-gcp]]

## Selection model

The overview emphasizes optionality: organizations can use simpler integrated invoicing, marketplace distribution, or ERP systems according to their contracting and revenue-process needs. It does not define invoice objects, lifecycle states, synchronization details, or integration setup; those require the linked dedicated guides.

## Calculation and timing boundary

A subscription's `invoice_placement` defaults to `ON_USAGE_INVOICE`, placing its charge on the usage invoice with the matching billing date. `ON_SCHEDULED_INVOICE` places the charge on a scheduled invoice: Metronome appends it when a scheduled invoice with that billing date exists and creates a new scheduled invoice when none exists. This placement does not establish finalization, delivery, collection success, or payment timing.

### Legacy Plans one-time invoice charge

Metronome's deprecated Plans API exposes bearer-authenticated `POST /v1/customers/{customer_id}/addCharge`. The required path `customer_id` is UUID-formatted; the `requestBody` is not itself marked required, while its payload schema requires `charge_id`, `price`, `quantity`, `invoice_start_timestamp`, `customer_plan_id`, and `description`. The charge must be on a product outside the current plan, and that product must have only fixed charges. The caller supplies the numeric price, which must match the invoice currency, with USD cents given only as an example. The target invoice is described through the customer, customer plan, and invoice start timestamp rather than an invoice ID, and HTTP 200 has an empty object schema. The page directs new clients to Contracts but does not identify the replacement endpoint, map the payload, define eligible invoice states or duplicate behavior, or document line-item creation, downstream delivery, tax, discounts, credits, commits, payment, accounting, or reconciliation effects.


### Customer-name propagation boundary

`POST /v1/customers/{customer_id}/setName` is documented to apply the new display name immediately across all billing documents and interfaces. The endpoint does not distinguish already-finalized from draft or future documents; define whether PDFs, exports, webhooks, data exports, or downstream Stripe, ERP, and marketplace copies are included; or establish invoice recalculation, delivery, collection, payment, tax, accounting, settlement, or reconciliation effects. Preserve the immediate product claim while treating those surfaces and outcomes as undocumented. [[source-metronome-api-reference-customers-update-a-customer-name]]

## Commercial Billings measure

For Metronome's own consumption pricing, Billings are the total value of invoices generated through Metronome whether invoiced automatically or manually. The stated exclusions are current-period finalized invoices voided before Metronome invoices the platform customer, non-production draft invoices used for testing or demonstration, and zero-dollar invoices used to track free-trial credits. The source does not define currency aggregation, tax, discounts, refunds, or other adjustments. [[source-metronome-guides-platform-configuration-metronome-pricing-model]]

The architecture guide orders invoice generation as usage receipt, billable-metric quantity calculation, contract pricing with base-rate-card overrides, and customer-facing invoice generation. It separately describes event-time alert evaluation, on-demand API-backed views, and cycle-close invoice finalization and delivery. The first two contexts do not establish that an invoice is finalized, and the page gives no latency, delivery, collection, retry, or failure-state guarantees.

The customer-controls guide distinguishes two alert calculations: `spend_threshold_reached` uses usage-based spend before credit and commit drawdown, while `invoice_total_reached` evaluates the amount after drawdown and can be limited to usage invoices. These are threshold-evaluation semantics, not evidence that an invoice is finalized, delivered, collected, paid, or immutable.

## Shared Plan and Contract invoice surface

Metronome also exposes bearer-authenticated `GET /v1/customers/{customer_id}/invoices/{invoice_id}/pdf` with both path identifiers required and UUID-formatted. HTTP 200 uses `application/pdf`; although the prose describes a binary full-invoice PDF, the OpenAPI media schema says only `type: object` and does not define bytes, properties, headers, filename, length, or streaming. HTTP 404 is a generic JSON error requiring string `message` and does not distinguish a missing customer, invoice, or customer-invoice mismatch. The page describes on-demand generation and potential performance impact from frequent requests but provides no rate, latency, caching, retry, lifecycle, retention, rendering-stability, availability, legal-officiality, audit-sufficiency, or compliance guarantee.

Metronome documents shared invoice operations for Plans and Contracts: customer-scoped retrieval of one or all invoices plus regeneration and voiding. Contract-targeted invoices may carry commit, credit, or usage details, while Plan invoices are generally scoped to plan-level billing events. Documented invoice fields include plan identity and generation-time plan custom fields, invoice adjustments, and charge sub-line items; non-tiered nonzero charges may expose a unit `price`, while tiered detail uses `tier_period` and `tiers`. The page does not specify HTTP methods, API version prefixes, pagination, target-selection mechanics, lifecycle preconditions, monetary units or currency, enum values, ordering, downstream-provider effects, or how the plan fields behave for contract invoices.


Bearer-authenticated `GET /v1/customers/{customer_id}/invoices/{invoice_id}` requires both UUID path identifiers and returns a required `data` envelope. The invoice schema requires only ID, customer ID, credit type, line items, status, total, and type; each line item requires only name, total, credit type, and type. Optional boolean `skip_zero_qty_line_items` removes zero-quantity lines from the representation. Prose says drafts update in real time and may change and says voided invoices retain original line details, but it defines no freshness SLA, snapshot guarantee, lifecycle transition contract, or retention period. This read page uses uppercase `VOID`, while the void-operation authority uses lowercase `voided`; preserve both source-scoped claims because enum exhaustiveness, casing normalization, and whether the operation wording is a literal GET response value are unresolved.

The Salesforce integration synchronizes invoice and invoice-line custom objects daily. Invoice fields include identity, customer, contract, credit type, invoice type, inclusive and exclusive UTC service-period bounds, total, status, issue time, and environment; lines include invoice, credit-type and commit lookups, quantity, unit price, product ID, total, effective-time bounds, and environment. The prose explicitly says the invoice and line objects include draft and finalized invoices, while the invoice status field enumerates `Draft`, `Finalized`, and `Void`; whether void invoices are synchronized or retained is unresolved. Salesforce copies do not establish invoice finalization freshness, provider delivery, payment, tax, settlement, accounting, or reconciliation.


### Customer invoice-list read

Bearer-authenticated `GET /v1/customers/{customer_id}/invoices` lists a customer's invoices with cursor pagination and filters for status, invoice type, credit type, contract, and inclusive-start/exclusive-end billing-period boundaries. The prose says drafts update as usage arrives and void invoices are included by default, but it gives no freshness or snapshot guarantee. Its ordering authorities conflict: prose says creation-date descending by default, while the `sort` parameter says `issued_at` ordering defaults to `date_asc`; callers needing deterministic order should pass `sort` explicitly. The prose also calls results summaries, while the response schema references an invoice object requiring `line_items`, so neither line-item omission nor single-invoice completeness is established. [[source-metronome-api-reference-invoices-list-invoices]]

## Event-based invoice preview

Metronome exposes `POST /v1/customers/{customer_id}/previewEvents` to calculate draft invoices from supplied usage events and the customer's current contract configuration before those events are processed. The request can replace historical usage or merge with it, and the response returns draft invoice records with totals and line items. Contracts using SQL billable metrics are excluded from this preview capability.

The cost-preview guide clarifies that Preview Events simulates invoice impact without processing or billing the proposed events. Its calculation can include tiered pricing, commit and credit coverage, free allotments, and multiple products. `merge` includes existing billing-period usage; `replace` ignores existing usage. Multiple active contracts return separate draft-invoice-shaped results.

These results are previews, not finalized, delivered, collectible, or documented as persisted invoices. The guide limits the endpoint to 8 RPS per client and returns HTTP 400 when SQL billable metrics are present on the customer invoice being evaluated. Its worked response is structurally illustrative: a request for 100 compute hours produces quantity 10, unit price 4900, line-item total 0, and invoice total 49000 without reconciling the quantity or arithmetic.

## Revenue-reporting invoice classification

Metronome's financial-reporting guide classifies `CONTRACT_SCHEDULED` invoices as scheduled charges including prepaid purchases, `CONTRACT_USAGE` invoices as usage charges, and `CONTRACT_TRUEUP` invoices as postpaid true-up charges. Invoice service-period timestamps select the target ERP accounting period, `line_items.product_id` maps the amount to a product or ERP SKU, and a populated `line_items.commit_id` joins to `balances.id` so `balances.type` classifies the amount as `credit`, `prepaid`, or `postpaid`. A null commit ID leaves on-demand versus overage classification to client-defined contract or commit metadata. The guide maps `FINALIZED` invoices to recognized-revenue reporting and `DRAFT` invoices to accrued-revenue reporting, with finalized and draft invoices transferred in separate export tables. It does not define metadata completeness, void and correction handling, downstream posting state, journal entries, or whether those status filters satisfy a particular accounting standard or close control.

> [!warning] Revenue-example invoice labels and IDs
> The CloudNet postpaid table labels twelve `800` rows `CONTRACT_SCHEDULED` while its conclusion calls them usage invoices; it labels the `400` row `CONTRACT_TRUEUP` while the conclusion calls it scheduled. Invoice ID `30011` is used for three periods, and IDs `30002`–`30012` recur across Customer B contract `20002` and Customer C contract `20003`. Line-item IDs `40005`/`40006` and `40006`–`40008` are likewise reused in different scenarios, while ledger IDs beginning `60001` recur under different balances. The scenarios may be isolated alternatives; do not combine them, assume global uniqueness, silently renumber them, or infer corrected invoice types without current source-data verification.

## Dashboard lifecycle overview

The dashboard quickstart describes a draft invoice accumulating usage during the billing period, followed by a 24-hour grace period before finalization. With a billing provider connected, it says the invoice is pushed within approximately one hour after finalization. Payment collection and paid or failed status remain the billing provider's responsibility.

## Credit and commit application

### Conditional suppression of a postpaid true-up invoice

Postpaid usage is paid in arrears, and a shortfall against the committed amount otherwise produces a final true-up invoice on `invoice_date`. `POST /v1/contracts/commits/disableTrueup` conditionally prevents that invoice from being generated for an identified postpaid commit.

> [!info] Invoice-effect boundary
> The endpoint does not define its cutoff or retroactivity, behavior for an already generated or finalized invoice, balance or ledger effects, forgiveness of the underlying obligation, reversal or re-enablement, reporting or export treatment, webhooks, downstream A/R behavior, or effects on other invoices. Treat it as a qualification to the normal shortfall true-up rule, not as evidence for any of those lifecycle or downstream outcomes.

When several eligible invoice lines can receive a credit or commit, Metronome applies the balance to usage products before subscription products and then composite products. Ties within a product type go to the earlier line-item start date, then the higher unit price, then alphabetical line-item name.

For a product rated in a custom pricing unit, Metronome first burns down applicable credits and prepaid commits with access schedules in that unit. If no applicable matching balance remains, the invoice receives a conversion line item that calculates the residual cost in the rate card's fiat currency; the converted fiat amount becomes the total due in the example. This does not establish conversion formula direction, precision, rounding, tax, finalization, delivery, collection, or payment-success behavior.

### Historical invoice import

For invoices already issued before a customer was provisioned in Metronome, `/v1/contracts/createHistoricalInvoices` accepts service periods and usage-line-item quantities, combines them with contract unit prices, and calculates invoice totals plus credit and commit balance effects. `preview: true` dry-runs the comparison before saving, and imported invoices are available through the Contracts page or API. Metronome does not send these invoices to its Stripe integration. This guide's worked migration is distinct from the credit-memo guide's mechanics for draft or finalized invoice corrections, external A/R credit memos, payment refunds, and credit-and-rebill. A separate `createHistoricalInvoices` API reference describes the endpoint as ideal for both billing migrations and correcting past billing periods, but the sources do not establish the correction workflow, its invoice-state preconditions, or its reconciliation behavior. This page does not define imported invoice state, finalization, collection, tax, downstream delivery beyond Stripe, idempotency, or partial failure.

### Credit, correction, and re-bill state boundaries

Contract archival cancels draft invoices and voids upcoming scheduled invoices. Finalized invoices are optional: the payload schema requires boolean `void_invoices`, while the `requestBody` itself is not marked required, and the schema explicitly says finalized invoices remain when it is `false`. The page does not define the cutoff for upcoming, eligible finalized states, effects on already distributed invoices, downstream Stripe, ERP, or marketplace records, payment or refund handling, tax, webhooks, revenue recognition, error recovery, or whether the contract, invoice, balance, and ledger mutations are atomic. [[source-metronome-api-reference-contracts-archive-a-contract]]

For incorrect usage on a current-period `DRAFT` invoice, the credit-memo guide directs the merchant to send a negative quantity or value matching the affected product's billable metric. For a previous-period `finalized` invoice, Metronome says usage events cannot be corrected or adjusted; the documented alternatives are a future credit or an external A/R credit memo. When the whole invoice is wrong, the guide separately gives a credit-and-rebill sequence of negative usage, corrected usage, voiding, and regeneration. A Metronome void does not void a downstream invoice, and historical usage submission is limited to 34 days; older re-bills remain entirely in the invoicing and A/R system.

Metronome exposes `POST /v1/invoices/void` under the OpenAPI document's global HTTP bearer scheme. The operation does not mark `requestBody` itself as required; within its JSON object schema, `id` is required and UUID-formatted. The HTTP 200 schema defines but does not require top-level `data`, requires `id` only within `data`, and shows an example containing `data.id`; status and other invoice fields are not documented, but the page does not exclude additional actual response fields. The operation description says voiding permanently and immediately sets the invoice status to `voided`, prevents collection, removes it from customer billing, and stops payment processing, and presents correcting billing errors, cancelling incorrect charges, and handling disputed invoices that should not be collected as intended uses rather than a complete eligibility-state contract. The page does not define eligible starting states, repeated-call or idempotency behavior, errors, concurrency handling, webhooks, or downstream reconciliation. Because the separate correction guide says a Metronome void does not void a downstream invoice, do not extend this endpoint's effect to Stripe, ERP, marketplace, payment refund, A/R, tax, revenue, or ledger changes without separate evidence.

> [!warning] Documentation ambiguity
> The finalized-period example prohibits usage-event correction for finalized invoices, while the following re-bill sequence instructs readers to negate and replace usage before voiding without stating the starting invoice state or reconciling that order with finalized-invoice immutability. Verify state preconditions and operation order before implementation.

Metronome exposes globally bearer-secured `POST /v1/invoices/regenerate` to regenerate a voided invoice. The operation recalculates from up-to-date rates, available balances, and other fees regardless of billing period, and says an invoice attached to a contract with a billing provider will be distributed according to that configuration. The JSON object schema requires a UUID-formatted `id` within the object, although `requestBody` itself is not marked required. HTTP 200 defines a non-required top-level `data` property whose object requires UUID-formatted `id` when present, and the example contains `data.id`. The page does not define the new invoice's state or amounts, calculation as-of or atomicity semantics, balance and ledger reconciliation, distribution timing or outcome, downstream voiding, payment or refund effects, error responses, or endpoint-specific repeated-call, concurrency, and timeout-recovery behavior. Apply the separately documented API-wide `Idempotency-Key` contract for POST operations without treating this page's omission as evidence of unsupported idempotency, and do not assume a changed key is safe after uncertain regeneration state. Its billing-period wording does not establish that corrected usage can bypass the separately documented 34-day historical-submission limit.

> [!warning] Documentation contradiction
> The prose says the regenerated invoice ID is distinct from the previously voided invoice, but the request and response examples reuse the same UUID. The schema constrains UUID format only and does not resolve equality. Verify runtime identity behavior before relying on either interpretation.

Credits and commits apply at invoice line-item level. Covered usage, its negative application line, and uncovered overage remain separate so product-level precommitted and overage spend stays attributable. A commit can record an invoiced amount without sending a downstream invoice, and scheduled commit charges can be consolidated onto a usage statement when the contract enables that behavior.

Commit edits appear immediately on draft invoices, while finalized invoices remain unchanged unless voided and regenerated. Invoice-schedule items tied to finalized invoices cannot be removed or updated, and a voided invoice's schedule item still cannot be removed. An access-schedule segment applied to a finalized invoice can be removed only after voiding that invoice.

When a contract edit adds an invoice-schedule item at date X, or moves an item to X, and a finalized scheduled invoice already exists there, Metronome leaves that invoice untouched and creates a new finalized scheduled invoice for the edited items. Removing an access-schedule segment also removes its manual ledger entry. The guide does not define delivery, collection, consolidation, idempotency, or downstream-provider effects for the newly created invoice.

A credit or commit ledger has one deduction entry for each invoice that consumes that balance. The deduction's effective timestamp is always the end of the usage invoice's service period, and Metronome says that timestamp can support balance views including or excluding pending charges. This does not make the ledger timestamp an invoice creation, finalization, delivery, collection, or payment timestamp, and the guide does not define how `pending` maps to invoice states.

The customer-credit create schema describes optional nonempty `name` as displayed on invoices and optional `description` as UI/API-only and not exposed to end customers. This endpoint does not define which invoice line or state displays the name, whether already-draft or finalized invoices change, or how either field propagates to PDFs, exports, webhooks, downstream billing providers, external A/R, tax, payment, refunds, or accounting systems.

Customer archival automatically archives all of that customer's contracts as of the current date and voids all corresponding invoices. [[source-metronome-api-reference-customers-archive-a-customer]]

For non-monotonically increasing `LATEST` metrics, invoice quantities are changes between reporting windows and may be negative when usage falls. Metronome evaluates charge lines independently and chronologically, consuming credit against positive lines without looking ahead to a later negative line; the worked full-period-credit example ends at `-$20`. The invoice-breakdowns surface is described as returning each window's incremental quantity and associated cost, including negative quantities and costs. The guide does not define how a negative invoice total proceeds through finalization, delivery, payment, refund, tax, settlement, external A/R, reconciliation, or accounting.

> [!warning] Intra-page recommendation conflict
> The example's credit covers the full billing period and still yields a negative total, but the later tip says full-period coverage avoids unexpected negative totals. The guide does not reconcile that recommendation with its example.



### Legacy credit-grant purchase-invoice boundary

A deprecated Plans credit-grant void can optionally set `void_credit_purchase_invoice: true` to void the purchase invoice associated with the grant. The endpoint does not define omitted or false behavior, invoice-state eligibility, downstream-provider propagation, payment or refund effects, tax or accounting treatment, or atomicity with the grant void. [[source-metronome-api-reference-credit-grants-void-a-credit-grant]]

## Threshold payment flow

Prepaid balance thresholds can gate release of a recharge commit on payment. Stripe gating can use a Stripe Billing invoice or a direct PaymentIntent. On a failed payment, the guide says the threshold configuration is disabled and a voided invoice should appear in both Metronome and Stripe; there is no automatic retry. An external payment gate leaves collection to the integrator, which must explicitly release or cancel the pending commit.

Spend-threshold billing is separate from prepaid-balance recharge: accumulated contract spend reaching `threshold_amount` triggers a payment attempt, and the configured commit product determines what appears on the incremental invoice. Stripe payment can use a Billing invoice or PaymentIntent; an external gate leaves collection to the integrator, which releases or cancels the commit afterward. The page does not define invoice finalization, payment retry, pending-commit invoice state, threshold denomination, or whether an ungated failure changes customer access.

## PayGo and manual commit payment

The PayGo example configures Stripe with `send_invoice`, which emails payment instructions. It must not be interpreted as automatic card collection; the native Stripe integration states that a default payment method is required for `charge_automatically`, not generally for `send_invoice`.

A separate manual payment-gated commit flow attempts payment for a one-off commit invoice. Success releases the commit; failure voids both associated invoices, creates no commit, and is not automatically retried. A new Metronome API request is required, and this payment retry is distinct from webhook-delivery retries.

## Native Stripe invoice delivery

For Avalara AvaTax on Stripe-delivered invoices, Metronome must leave the Stripe invoice in draft so Avalara can calculate and apply tax before finalization. This differs from the Stripe Tax guide's usual recommendation to avoid retaining drafts when tax should calculate on sync, but the settings are provider-specific rather than contradictory. The Avalara page confirms tax line items on the finalized invoice after processing without defining who finalizes it, processing latency, retry behavior, or a guard against taxless finalization.

- Stripe connections are scoped to a Metronome environment; sandbox connects to Stripe test mode.
- Customer billing configuration selects the Stripe customer and collection method. Multi-account customer setup requires `delivery_method_id`; contract creation selects among the customer's configured providers with `billing_provider_configuration_id`, obtained from `/getCustomerBillingProviderConfigurations`.
- Adding Stripe to an existing contract does not send earlier finalized invoices retroactively.
- `charge_automatically` requires a Stripe default payment method. Stripe can wait up to one hour after `invoice.created` before attempting payment, or 72 hours when that webhook delivery fails.
- Account-level settings can leave invoices as drafts, skip invoices below the currency minimum, adjust presentation, or align `effective_at` to the service period. The guide says that alignment is incompatible with Stripe Tax.

Metronome receives Stripe invoice-status changes through webhooks and exposes mapped external status through its invoice API and data export. No external status appears in Metronome when the integration deliberately leaves the Stripe invoice as a draft.

For Stripe Tax, Metronome supplies the linked customer and product mapping, and Stripe calculates tax when the invoice is finalized. Retaining Stripe invoices as drafts defers calculation until manual finalization. Collection method controls what happens after finalization and is independent of whether tax is applied.

### Anrok-through-Stripe invoice tax behavior

In the primary Anrok provider mode, Anrok calculates arrears tax inline through the Stripe app without requiring **Leave invoices as drafts**. Prepaid-balance and spend-threshold flows use the documented `tax_type: "STRIPE"` and `payment_type: "INVOICE"` values in `payment_gate_config`; the guide does not define the `tax_type` enum's general semantics, and the `STRIPE` literal is not reliable evidence of calculator identity because the documented active provider in this mode is Anrok. A finalized Stripe invoice is verified through `automatic_tax.enabled: true`, `provider: "anrok"`, and `status: "complete"`.

This provider-specific flow is distinct both from native Stripe Tax and from the separate mode in which Stripe Tax calculates while Anrok handles compliance, filing, and reporting. Where product mapping is implemented, the guide creates `stripe_product_id` on Metronome **Product** but maps from `ContractProduct.stripe_product_id`; that terminology remains unresolved. The guide does not define invoice-finalization timing, retries, fallback, correction, filing, remittance, or the legal or operational semantics of `liability.type`.

### India card e-mandates

For Indian-card invoices, the documented flow collects the card on-session and confirms a Stripe SetupIntent, then waits for the mandate to become active. Threshold recharges use a sporadic interval and maximum amount; subscriptions and recurring fees use their recurrence cadence and a fixed amount when known or maximum when variable. A mandate may remain pending for up to 30 minutes; an inactive mandate is unusable and requires new customer authorization.

The contract stores the Stripe mandate ID in a custom field mapped to `invoice.payment_settings.default_mandate`. Invoices sent to Stripe attempt to attach the mandate, but attachment is not a payment-success guarantee. Stripe can issue `invoice.payment_action_required`; no response or an inactive mandate enters the normal failure flow.

Stripe owns mandate creation and lifecycle. Metronome returns the custom-field value and maps it into invoice delivery but exposes no mandate-management API. The page requires SetupIntent setup for this integration because it characterizes all charges, including the first, as off-session. The integrator must update or replace the mandate in Stripe and act before retrying.

## Custom downstream invoice delivery

Metronome's recommended API pattern for a non-native downstream provider listens for `invoice.finalized`, then uses the webhook's `customer_id` to query `/listInvoices` for finalized invoices in the associated billing period, transforms the returned invoice and line-item fields, and upserts them into the destination. The guide says finalization occurs after the grace period and that `invoice.finalized` must be enabled through a Metronome representative. Its QuickBooks example requires a preexisting downstream customer and at least one item. This is a recommended integration sequence, not an exactly-once or complete synchronization contract: the source does not define webhook ordering or duplicate handling, invoice-list pagination or consistency, how several matches are selected, destination idempotency, partial-failure recovery, replay, downstream status synchronization, payment collection, tax, credit-memo behavior, or reconciliation.

## Account-level marketplace delivery setup

`POST /v1/setUpBillingProvider` creates account-level AWS, Azure, or GCP Marketplace delivery configuration and returns a UUID `delivery_method_id` for later mapping. Its setup success response contains only that identifier; it does not establish customer or contract attachment, provider readiness, invoice routing, marketplace metering, payment collection, tax handling, delivery success, or reconciliation. Provider-specific configuration is open-ended, and the page does not define activation timing, read-after-write visibility, update or rollback, or external-provider validation. [[source-metronome-api-reference-settings-set-up-account-level-billing-provider]]

## Scheduled provider routing

Scheduled and commit charges can optionally consolidate onto a usage invoice when the exclusive service-period end day matches the scheduled invoice date and the usage invoice has not finalized. Metronome reevaluates this at contract creation and later changes; this does not make the creation-time consolidation setting editable.

A customer-level provider configuration does not itself route an invoice; a contract must select it. The customer-provisioning guide says archiving an attached configuration immediately stops billing to that destination and prevents provisioning a replacement on the active contract. This archival behavior is beta.

A contract can schedule invoice routing among Stripe, NetSuite, and AWS, Azure, or GCP Marketplace. A current-period Stripe or NetSuite correction can reroute a draft invoice, but it does not reroute an invoice already finalized and sent; Metronome states that each invoice is delivered exactly once. Marketplace transitions begin only with the next billing period.

> [!warning] Documentation ambiguity
> The provider-change guide first selects a schedule segment relative to service-period end or `issued~at`, then says each invoice maps by service-period start. It does not reconcile those timing formulations.

Hierarchy consolidation uses parent `invoice_consolidation_type: "CONCATENATE"` with child `payer: "PARENT"` and `usage_statement_behavior: "CONSOLIDATE"`; a self-paying child must use a separate statement. Inclusion also requires the child usage service period to be bounded by the parent's period and parent and child issue dates to align on the same day. Metronome still generates standalone parent and child usage statements for UI, API, and data export visibility, but does not send them downstream when consolidation occurs; the guide specifically suggests filtering the standalone parent statement in a parent-facing spend UI to avoid double-counting it with the consolidated invoice. Consolidated line items retain origin customer and contract information. Hierarchy billing currently supports only Stripe; marketplace billing is merely described as coming soon, without a date or provider contract. The source does not define the disposition of a child invoice that fails the consolidation checks.

## Stripe representation limits

Decimal quantities are moved into descriptions while Stripe line-item quantities become `1`; invoices over 250 line items collapse into one Stripe item. The guide also documents a maximum-charge error and no native Stripe credit-memo support. These transformations mean the Metronome invoice remains the detailed billing record when Stripe representation is compressed.

## Go-live verification boundary

Metronome's go-live checklist asks teams to understand the draft-to-grace-period-to-finalized lifecycle, enable and test `invoice.finalized`, confirm the chosen integration's delivery path, and exercise an event-to-invoice-to-webhook-to-payment cycle with a production test customer. It also asks teams to confirm sandbox-to-production migration and document rollback procedures. This is a verification exercise, not evidence of provider-specific collection ownership, payment finality, delivery timing, test isolation, future invoice accuracy, or rollback success. [[source-metronome-guides-implement-metronome-production-checklist]]

## Related

- Company: [[metronome]]
- Usage-billing context: [[metronome-usage-based-billing]]
- Related platform: [[stripe]]

## Sources

- [[source-metronome-api-reference-credits-and-commits-disable-trueup-for-commit]] — conditional suppression of a postpaid shortfall true-up invoice and unresolved invoice-lifecycle and downstream effects
- [[source-metronome-api-reference-contracts-archive-a-contract]] — draft cancellation, scheduled-invoice voiding, finalized-invoice flag behavior, and downstream boundary

- [[source-metronome-api-reference-invoices-get-an-invoice-pdf]] — bearer-authenticated PDF retrieval, required customer and invoice identifiers, binary media boundary, and generic not-found contract

- [[source-metronome-guides-pricing-packaging-make-pricing-changes-edit-contract]] — draft recalculation, finalized-invoice regeneration, schedule restrictions, and same-date scheduled-invoice creation
- [[source-metronome-guides-reporting-insights-financial-reporting-revenue-recognition-examples]] — scheduled, usage, and true-up examples with table-versus-conclusion labels and reused sample identifiers

- [[source-metronome-guides-pricing-packaging-apply-credits-and-commits-prioritization-rules]] - eligible invoice-line ordering by product type, start date, unit price, and name
- [[source-metronome-guides-pricing-packaging-subscription-provision-your-customer]] - subscription usage-invoice versus scheduled-invoice placement and same-billing-date append-or-create behavior
- [[source-metronome-guides-pricing-packaging-billing-model-guides-model-hierarchical-customer-relationships]] — parent-paid consolidation conditions, standalone-statement boundary, origin attribution, and Stripe-only hierarchy limit

- [[source-metronome-api-reference-invoices-regenerate-an-invoice]] - invoice regeneration contract, recalculation and distribution side effects, identity contradiction, and retry boundaries

- [[source-metronome-api-reference-invoices-add-a-one-time-charge]] — deprecated Plans one-time-charge request contract, invoice-selection context, caller-supplied price, and empty response boundary

- [[source-metronome-plans-shared-endpoints-invoices]] - shared Plan and Contract invoice operations, plan context, adjustments, sub-line items, and tier-schema boundaries

- [[source-metronome-api-reference-invoices-void-an-invoice]] — invoice void endpoint contract, immediate status-transition wording, success-response limit, and downstream boundary

- [[source-metronome-guides-reporting-insights-financial-reporting-revenue-recognition]] - invoice-type and line-item classification, finalized-versus-draft revenue reporting, and downstream journal-entry boundary

- [[source-metronome-integrations-invoice-integrations-custom-invoice-integrations]] — finalized-invoice API export and downstream transformation flow with QuickBooks-specific prerequisites and unresolved delivery semantics

- [[source-metronome-integrations-tax-integrations-avalara]] — third-party Avalara calculation on draft Stripe invoices and finalization responsibility boundary

- [[source-metronome-integrations-tax-integrations-anrok]] — provider-specific inline arrears tax, threshold configuration values, finalized-invoice verification, and separation from native Stripe Tax and compliance-only coexistence

- [[source-metronome-guides-invoices-invoice-optimization-import-existing-invoices]] - historical invoice calculation, preview, contract-balance effects, and Stripe-delivery exclusion

- [[source-metronome-guides-pricing-packaging-make-pricing-changes-use-currency-custompricingunits]] — custom-unit balance drawdown, conversion-line-item fallback, and fiat total-due boundary
- [[source-metronome-guides-invoices-invoice-optimization-issue-credit-memos]] — future credits, external A/R credit memos, draft versus finalized correction, void-and-regenerate re-billing, and refund ownership

- [[source-metronome-guides-invoices-overview]] — Stripe, marketplace, and ERP invoicing options
- [[source-metronome-api-reference-invoices-preview-events]] — draft-invoice previews calculated from proposed usage events
- [[source-metronome-integrations-invoice-integrations-stripe]] — Stripe routing, settings, status synchronization, payment timing, and representation limits
- [[source-metronome-guides-get-started-metronome-dashboard-quickstart]] — draft, finalization, provider-delivery, and collection boundary
- [[source-metronome-guides-pricing-packaging-apply-credits-and-commits-create-a-pre-paid-commit]] — balance application, downstream-invoice suppression, and consolidation
- [[source-metronome-api-reference-credits-and-commits-edit-a-commit]] — draft reflection and finalized or voided schedule constraints
- [[source-metronome-guides-customers-billing-optimize-customer-experience-prepaid-balance-thresholds]] — gated recharge, failed-payment invoices, and external release flow
- [[source-metronome-guides-customers-billing-manage-customers-schedule-billing-provider-change]] — scheduled invoice destinations, draft rerouting, and exactly-once boundary
- [[source-metronome-integrations-tax-integrations-stripe-tax]] — finalization-time tax calculation and collection-method boundary
- [[source-metronome-guides-get-started-how-metronome-works]] — calculation order and separation of evaluation, visibility, and finalization
- [[source-metronome-guides-implement-metronome-core-concepts-provision-contract]] — consolidation conditions and beta provider-attachment timing
- [[source-metronome-guides-implement-metronome-core-concepts-provision-customer]] — customer/contract routing boundary and beta archival
- [[source-metronome-guides-pricing-packaging-billing-model-guides-pay-as-you-go]] — illustrative Stripe `send_invoice` boundary
- [[source-metronome-guides-pricing-packaging-apply-credits-and-commits-manual-payment-gated-commits]] — manual commit payment, invoice voiding, and retry boundary
- [[source-metronome-guides-customers-billing-optimize-customer-experience-india-e-mandates]] — Indian-card Stripe mandate creation, activation, invoice mapping, customer action, and ownership boundaries
- [[source-metronome-guides-customers-billing-optimize-customer-experience-set-customer-spend-control]] — incremental spend-threshold invoicing, Stripe payment choices, and external outcome flow
- [[source-metronome-guides-customers-billing-optimize-customer-experience-preview-event-cost]] — contract-aware cost simulation, merge/replace semantics, multi-contract draft results, performance limit, and SQL-metric exclusion
- [[source-metronome-guides-customers-billing-optimize-customer-experience-customer-controls]] — pre-drawdown spend versus post-drawdown usage-invoice alert calculation
- [[source-metronome-guides-customers-billing-optimize-customer-experience-get-remaining-balance]] — per-invoice balance deductions, service-period effective timestamps, and pending-charge display boundary

- [[source-metronome-api-reference-settings-set-up-account-level-billing-provider]] — account-level marketplace delivery setup, returned routing identifier, and downstream outcome boundaries

- [[source-metronome-api-reference-credits-and-commits-create-a-credit]] - credit name and description invoice-visibility boundary plus unspecified downstream propagation

- [[source-metronome-api-reference-customers-update-a-customer-name]] — immediate customer-name propagation claim across billing documents and interfaces, with finalized-artifact and downstream scope unresolved

- [[source-metronome-api-reference-invoices-get-an-invoice]] - customer-scoped invoice retrieval, required invoice and line-item fields, mutable draft and void representation, uppercase-VOID versus lowercase-voided uncertainty, downstream-record boundaries, and schema gaps

- [[source-metronome-guides-implement-metronome-core-concepts-how-invoicing-works]] — contract-driven usage and scheduled invoice types, lifecycle and finalization timing, line-item presentation, and schema-example boundaries

- [[source-metronome-integrations-marketplace-integrations-aws]] — AWS listing and routing prerequisites, USD-cent metering semantics, credit and commit treatment, positive-quantity correction, cutoff, outage, and currency limits

- [[source-metronome-api-reference-customers-archive-a-customer]] - automatic current-date contract archival and corresponding-invoice voiding

- [[source-metronome-guides-implement-metronome-core-concepts-non-monotonically-increasing-metrics]] - incremental and negative invoice quantities, no-look-ahead credit consumption, negative-total boundary, and invoice-breakdown behavior

- [[source-metronome-integrations-platform-integrations-sfdc-integration]] - daily Salesforce invoice and line-item replicas, service-period and attribution fields, draft and finalized scope, Void-status ambiguity, and downstream-outcome boundaries

- [[source-metronome-api-reference-invoices-list-invoices]] - customer-scoped invoice listing, billing-period filters, cursor pagination, live-draft boundary, and conflicting default-order descriptions
