---
title: "Metronome Credits and Commits"
type: concept
category: technology
tags: [metronome, credits, commits, contracts]
---

## Definition

Metronome commitments represent contractually agreed spend and can be prepaid or postpaid. In the enterprise guide, a prepaid commitment separates when balance becomes available from when the customer is invoiced, allowing access and payment schedules to differ.

## Enterprise commitment structure

- Access schedules determine when commitment balance becomes usable.
- Invoice schedules determine when prepaid commitment charges are billed.
- `rollover_fraction` can preserve a defined portion of unused balance when transition logic is applied at renewal.
- Contract rate overrides can scope negotiated discounts to product tags.
- Scheduled charges model separately timed fixed charges; they are not interchangeable with commitment balance.

The guide's example allocates a $500,000 prepaid commitment across three annual access periods, invoices it in two $250,000 installments, and sets a 25% rollover fraction.

## Lifecycle

A contract edit adds terms without starting a new contract. A contract transition starts a new contract, retains its relationship to the original, and can apply transition logic such as rolling over unused commitments or credits.

Recurring credits and commits create a new grant and ledger each period. `commit_duration` controls how long unused value remains available, the recurrence schedule defaults to the contract usage schedule, and null proration defaults to `FIRST_AND_LAST`. A distinct recurring-grant start date becomes its anchor and does not prorate the first period.

For offset-notification scheduling, Metronome says subsequent recurring-commit child commits are generated at most one future billing period ahead. A before-`commit.segment.start` offset longer than that horizon cannot fire at the requested earlier time because the child does not yet exist; it fires when the next child is created. This page does not establish the exact child-creation instant or a general recurring-commit generation SLA outside the offset scenario.

## Drawdown and invoice attribution

Credits and prepaid commits at contract or customer level can carry access schedules in custom pricing units or selected currencies. Usage priced in a custom unit burns down applicable balances whose access schedules use that same unit; when none remains, invoice conversion to the rate card's fiat currency covers the residual usage. A CHF-paid prepaid commit granting Cloud Compute Tokens illustrates differing payment and access denominations, but the guide does not define arbitrary balance conversion, applicability priority, exchange rates, precision, or rounding.

### Future-credit versus credit-memo boundary

A Metronome credit can grant relief on future billing at customer scope, where it can apply across existing contracts on the account, or at contract scope. This does not alter the past transaction or invoice. When charges and associated revenue must be reversed, the credit-memo guide instead assigns the memo to the external customer-A/R system; the resulting A/R invoice can differ from the Metronome invoice line, with the memo serving as the audit record. The source does not establish that a future credit reverses historical revenue.

- Credits and prepaid commits ordinarily draw down before postpaid commits; lower numeric priorities consume first within the applicable ordering tier.

> [!warning] Contradiction
> The broad prepaid-before-postpaid rule has a rollover exception: the prioritization guide places postpaid rollover commits before prepaid rollover commits and credits. After the rollover tier, prepaid commits and credits still precede ordinary postpaid commits regardless of priority. Commit type outranks priority; same-type rollover ties use priority, narrower product applicability, narrower usage applicability, then earlier `ending_before`. Prepaid ties additionally place zero-dollar cost basis before paid value, then use earlier `starting_on` and fewer applicable contracts. The postpaid section says it follows prepaid logic but its abbreviated list omits usage applicability, so that tie-breaker remains ambiguous for postpaid commits.
- The same usage can apply to only one credit or commit, with any remainder continuing as postpaid fulfillment or overage.
- Application occurs at invoice line-item level. Covered usage, the negative balance-application line, and uncovered overage remain separately attributable.
- Every credit or commit uses a fixed product for invoice and reporting attribution, while product IDs, tags, or specifiers can restrict eligible usage.
- The `@metronome/sdk@3.10.0` commit model adds optional `cost_basis`, defined as the ratio of amount paid to credit granted. Its V2 customer-commit edit accepts `applicable_contract_ids`, where null applies to all customer contracts; the field cannot be edited for postpaid or contract-level commits. [[source-github-metronome-node]]
- Stripe-taxed prepaid-balance thresholds, spend thresholds, and one-off payment-gated commits require `payment_gate_type: "STRIPE"`, `tax_type: "STRIPE"`, and `stripe_config.payment_type: "INVOICE"`; account-level tax enablement does not cover these flows.

### Historical invoice balance effects

Historical invoice import combines supplied line-item quantities with unit prices on the contract to calculate invoice totals and effects on the customer's credit and commit balances. The guide does not define the resulting ledger-entry types or effective timestamps, ordering relative to existing deductions, rollback or reversal behavior, whether preview results persist, or any relationship between those balance effects and correction or credit-and-rebill workflows.

### Balance retrieval and ledger calculation

Archiving a contract also archives all associated commits and credits. For prepaid commits with active segments, Metronome automatically creates expiration ledger entries to close remaining balances and shows them in commit transaction history as `PREPAID_COMMIT_EXPIRATION`. The archive page does not define association behavior for customer-level balances shared across contracts, entry amounts or effective timestamps, ordering against invoice deductions, atomicity, or reconciliation after partial failure. Its uppercase type spelling differs from the lowercase `prepaid_commit_expiration` documented by the remaining-balance guide, so enum casing should be verified per surface. [[source-metronome-api-reference-contracts-archive-a-contract]]

`POST /v1/contracts/customerBalances/list` is the detailed balance read. Its payload schema requires `customer_id`, although the request-body wrapper is not marked required; omitted-body and top-level unknown-field behavior remain undocumented. Optional access-window filters, balance and ledger expansions, contract and archive inclusion, feature-gated zero exclusion, and JSON-body cursor pagination are available. HTTP 200 is an object requiring `data` and nullable `next_page`; `data` is the Commit-or-Credit union. The endpoint's body `limit` is 1-25 and defaults to 25, unlike the separate pagination authority's query-parameter convention and general 100 cap.

`include_archived` says exactly "archived credits and credits from archived contracts." Commit alone exposes `archived_at`; Credit has no corresponding property. The contract-archive authority establishes that associated commits and credits are archived. This list surface still does not establish whether archived commits are returned, how Credit exposes archive status without `archived_at`, how the repeated-credit wording partitions results, or omitted-flag behavior.

The calculated balance excludes expired and upcoming segments, includes future-dated manual entries on active segments, and ordinarily matches ledger sum. If negative manual entries exceed positive remaining value, however, it is floored at zero.

> [!warning] Contradiction
> This non-negative floor qualifies the existing broad signed-ledger-sum statement. The OpenAPI page also serializes uppercase, often expanded tokens such as `PREPAID_COMMIT_EXPIRATION`, `POSTPAID_COMMIT_INITIAL_BALANCE`, and `CREDIT_EXPIRATION`, while the remaining-balance guide uses lowercase and sometimes differently named `prepaid_commit_expiration`, `postpaid_initial_balance`, and `credit_segment_expiration`. Do not infer normalization or one-to-one equivalence; preserve each surface's exact names.

### Revenue-reporting treatment

Metronome's revenue-recognition guide treats prepaid-commit purchase invoices as deferred revenue, prepaid drawdown invoices as recognized as consumption occurs, and unused prepaid expiration as recognized at period end. Postpaid usage is recognized as the balance draws down, with any unmet minimum reported when the true-up invoice is issued. Free credits are never paid for and do not affect deferred revenue, although their drawdown may have a contra-revenue effect. For line-item-based reports, the guide says to ignore `credit_automated_invoice_deduction` and `prepaid_automated_invoice_deduction` on `CONTRACT_USAGE`, plus `postpaid_automated_invoice_deduction` and `postpaid_trueup` where invoice line items already include the amounts; include `prepaid_segment_expiration` because Metronome does not invoice that expiration, and usually ignore `credit_segment_expiration` because free-credit expiration does not affect revenue. These rules are documented report-construction guidance, not a complete merchant accounting policy.

> [!warning] Revenue-example amount and classification conflicts
> The CloudNet free-credit example gives uncovered CloudStorage a line-item total of `75` but concludes `150` of on-demand revenue. Its prepaid-expiration narrative and ledger burn `700` in months 2–12, while the conclusion allocates `700` to compute plus `100` to storage in each of those months and then also recognizes `1,400` expiration. In the overage alternative, month 11 lists `900` overage but an `800` summary invoice, while the detailed invoice is `900`; the conclusion classifies all month-11 and month-12 revenue as prepaid even though only `100` remained entering month 11. Both gross month-11 rows carry `commit_id 50002`, which joins to a `PREPAID` balance, conflicting with the page's overage label under the parent classification model. Do not infer corrected amounts, allocation, or classification; reconcile current line items, balances, and client metadata.

`/getNetBalance` returns one customer-level remaining-balance sum with filters for balance type, currency, pending charges, and custom fields. `listBalances` supports individual credit and commit views: each balance has a ledger, and summing its positive and negative entries produces that ledger's remaining balance. Values can be fractional; for USD the unit is cents, so `0.8` represents $0.008 and must not be silently truncated.

Ledger entries carry a type, signed amount, and effective timestamp. One invoice-deduction entry exists for every invoice that consumes a balance, and its timestamp is the usage invoice's service-period end. Positive and negative manual entries can correct or migrate balances. Credit, prepaid-commit, and postpaid-commit ledgers have distinct start, drawdown, rollover, expiration, true-up, manual, and seat-adjustment types; the guide gives identical descriptions for `prepaid_segment_expiration` and `prepaid_commit_expiration` without distinguishing their trigger boundaries.

## Prepaid balance thresholds

A contract-provisioning example separates a one-year prepaid commit's access schedule from its one-time upfront invoice schedule and scopes the balance to `cloud`-tagged products. A quarterly platform charge has its own schedule. Optional usage-invoice consolidation applies to scheduled charges including commits when the service-period end date aligns and the usage invoice remains unfinalized.

A contract can automatically replenish prepaid value when its eligible balance reaches a configured `threshold_amount`. `recharge_to_amount` is the target balance, so Metronome creates only the commit needed to restore that level. The default calculation includes contract- and customer-level commits and credits but always excludes individual seat-scoped balances. Threshold balance specifiers can additionally exclude balances by `ContractCreditOrCommit` custom fields.

Thresholds support fiat and custom pricing units. Custom-unit amounts are converted to fiat for payment through the customer's rate-card conversion. Payment gating can delay release of an automatic or manually purchased commit until Stripe or an external gateway confirms payment.

A failed gated payment disables the threshold configuration and is not retried automatically. Re-enabling it forces a fresh balance evaluation and payment attempt. An external gateway must retain the `payment_gate.external_initiate` workflow ID and call the threshold-release endpoint to release or cancel the commit.

Active threshold billing must be removed before a contract can transition to an AWS, Azure, or GCP Marketplace billing provider.

> [!warning] Documentation ambiguity
> The threshold guide alternates between recharge at the threshold and recharge only below it. It also describes `discount_config.fraction` as the discount while showing `0.9` for a 10% discount, and its minimums note uses field labels that differ from the request examples. Confirm these boundaries against the current API schema.

A threshold `discount_config.cap` can reference a public-beta spend tracker. The documented tracker currently sums selected commit purchases by manual or threshold-recharge source and optional discounted status. When qualifying spend reaches the cap, new threshold commits remain undiscounted until the tracker resets at the next billing period. A similar cap on manually issued payment-gated commits is not automatic: the merchant must query the tracker and enforce the check before issuing the commit.

Spend-threshold billing is a separate contract control from prepaid-balance auto-recharge. It associates a product with the commit shown on the incremental invoice and can payment-gate that commit's release. Under the external path, the integrator stores `payment_gate.external_initiate.workflow_id`, collects payment, and calls the threshold-release endpoint to release the commit on success or cancel it on failure. The source does not define the pending commit's amount, type, schedules, ledger availability, or visibility before the outcome.

## Customer-level create API

`POST /v1/contracts/customerCommits/create` creates a balance outside an individual contract for enterprise-wide or multi-contract use. Metronome recommends contract-level commits for standard cases.

- The request requires customer, type, priority, fixed product, and access schedule.
- Postpaid commits require matching access and invoice totals, one item in each schedule, and an invoice contract.
- A prepaid commit can omit invoicing to create a complimentary balance.
- Contract scope can be explicit or cross-contract; product scope can use IDs, tags, or specifiers.
- Lower priority numbers consume first, with contract-level balances winning ties over customer-level balances.
- `uniqueness_key` prevents duplicate creation; its description documents a `409` failure.

### Customer-level credit creation

Bearer-authenticated `POST /v1/contracts/customerCredits/create` creates a customer-level credit, though Metronome recommends contract create or edit for most credits. The payload schema requires UUID customer, numeric priority, UUID fixed product, and access schedule; the request-body wrapper itself is not marked required. Each schedule item requires numeric amount plus inclusive RFC 3339 start and exclusive end, while the optional credit type defaults to USD cents. Contract scope can be selected or cross-contract. For product applicability, the direct-selector descriptions say omitting both IDs and tags means all products, while the same payload permits `specifiers` only when those direct selectors are absent and says at least one specifier condition must match; the page does not reconcile those statements into one selector algorithm. An exclusion array makes a specifier inapplicable when usage matches its inclusion criteria and any exclusion entry, while all tags within one exclusion entry must match. Lower numeric priority applies first, with contract-level balances winning equal-priority ties over customer-level balances; this endpoint summary does not replace the fuller rollover, type, cost-basis, applicability, and schedule ordering rules. HTTP 200 returns required UUID `data.id`; 400 and 404 use generic required string messages, while `uniqueness_key` separately documents a 409 duplicate failure. The page leaves unknown-field behavior, amount constraints, schedule cardinality and overlap, ledger state, balance-read timing, lifecycle mutations, concurrency, and propagation to invoices, alerts, reports, exports, webhooks, external A/R, tax, payment, refunds, and revenue recognition unspecified.

## Targeted commit edits

### Postpaid true-up suppression

Globally bearer-secured `POST /v1/contracts/commits/disableTrueup` prevents generation of the final true-up invoice for one postpaid commit. The operation's `requestBody` wrapper is not marked required; within the referenced JSON payload, customer, contract, and commit UUID properties are required, while an amendment UUID is optional when applicable. This does not establish omitted-body runtime behavior. HTTP 200 requires a `data.id` UUID, while the operation lists generic `400` and `404` responses.

Postpaid usage remains described as paid in arrears, with a shortfall otherwise producing a final true-up invoice on `invoice_date`. Apply the separate API-wide [[metronome-api-idempotency|`Idempotency-Key` contract]] for POST requests: identical parameters with the same key replay the original result, changed parameters return `409`, and retention is at least 24 hours.

> [!info] Operation boundary
> This source establishes invoice suppression only. It does not define a balance or ledger mutation, forgiveness of the unmet commitment, a timing cutoff or retroactive effect, reversal or re-enablement, behavior after invoice generation, already-disabled behavior, replay with another or expired key, concurrent calls, `disableTrueup`-specific recovery after cached errors, detailed error-condition mapping, or propagation to reports, exports, webhooks, external A/R, and other invoices. Existing categorical statements that a postpaid shortfall generates a true-up should be qualified with this endpoint's conditional exception rather than replaced.

`POST /v2/contracts/commits/edit` changes one contract-level or customer-level commit identified by `customer_id` and `commit_id`. It can update display fields, access or invoice schedule items, invoicing contract, applicability, priority, rate type, fixed product, or hierarchy access.

- Schedule items use separate add, update, and remove arrays; updates and removals address existing items by UUID.
- Direct product ID or tag selectors cannot be combined with `specifiers`.
- Hierarchy child access can allow all children, no children, or a non-empty contract-ID list.
- The schema does not define general omitted-versus-null mutation semantics, the meaning of its success `data.id`, or the interaction between top-level `product_id` and the applicability selectors.

General contract editing also supports adding and archiving commits and credits; editing their applicable products, descriptive fields, and documented schedules; adding recurring grants; changing documented recurring-grant amounts and end times; and editing commit rollover fraction. Rollover commits cannot themselves be edited. An originating commit's access schedule is editable only until the destination contract has a finalized invoice, while its invoice schedule is editable only until the original contract ends. Archiving requires voiding the documented finalized usage, payment, or scheduled-charge invoices first. The guide does not define inclusive cutoff semantics, concurrency ordering, or failure codes for those guardrails.

In an account hierarchy, a parent commit can make its balance available to all children, no children, or selected child contract IDs. The shared-pool example lets children draw down the parent commit and then makes self-paying children responsible for their own overages after exhaustion; both parent and child contracts must be active during the same period for access. Selective access can coexist with separate child rate cards and contract overrides. The guide states that hierarchies can share credits as well, but its detailed child-access payloads are commit examples and do not establish credit-specific request mechanics.

## Legacy amendment payloads

The retiring contract-amendment endpoint can add prepaid or postpaid commits and credits as part of one amendment. Its commit schema requires type and product, while prose calls `access_schedule` required without listing it in the OpenAPI `required` array. Postpaid schedules are limited to one matching access and invoice item; omitting a prepaid invoice schedule creates a complimentary commit.

Commit and credit rollover fractions are constrained to 0–1, and lower numeric priorities apply first. Direct product IDs or tags cannot be combined with specifiers. The credit applicability description says absence of IDs and tags means all products even though the same object also accepts specifiers; the page does not reconcile that wording.

## Documentation cautions

The guides contain example-level inconsistencies that should be checked against the current API schema before implementation:

- Its create-contract sample uses `product` inside a commit, while the dedicated create-contract API reference documents `product_id`.
- Its upsell prose calls the new $300,000 term a commitment, while the accompanying edit request adds a scheduled charge rather than a commit.
- The customer-commit schema exposes a generic recurring invoice schedule, while its postpaid prose requires one schedule item; confirm this combination before use.

> [!warning] Contradiction
> The credits-and-commits guide's prepaid prose describes $10,000 of accessible value, while its sample grants `100000` USD cents ($1,000) and invoices `1000000` cents ($10,000). Its recurring examples also contain invalid JSON, dates that conflict with the described January 1 signup and January 21 upgrade, and `rollover_fraction: 100`; the dedicated create-contract reference constrains this fraction to 0–1.

## Subscription, manual-gate, and trial extensions

- A subscription can optionally provision credit pooled at subscription level or scoped per seat. The overview does not define grant schedules, drawdown, thresholds, payment gates, or hybrid mechanics.
- When cancelling a hybrid subscription by moving that subscription's end date, its recurring credit must be ended separately. The lifecycle source does not establish contract-level cancellation behavior for that credit.
- A manual one-off Stripe-gated commit edits an existing contract. Successful payment releases the balance; failure voids the associated Metronome and Stripe invoices, creates no commit, and requires a new API request rather than an automatic payment retry. Pre-success resource state and external-gate equivalence are undocumented.
- A capped trial can use a fixed credit product with a time-bounded access schedule, blank applicability fields for all usage, and a low numeric priority so the trial grant draws down first. Depletion or expiry permits later usage to rate in arrears; monetary encoding and isolation from other balances remain unknown.
- The prepaid-credits business-model guide makes product access merchant-owned: the merchant stores a local boolean entitlement for latency and resilience, sets it true only after successful gated payment, and uses a zero-balance alert as the signal to set it false. The guide implements the purchased "credits" as an `add_commits` contract edit and calls the balance and access-schedule amounts `2000`, but does not define their unit. Its sample access interval is invalid because `ending_before` is 2025-04-01 while `starting_at` is 2026-04-01, and its auto-recharge prose and payload use `threshold_billing_configuration` and `credit_balance_threshold_configuration` rather than the dedicated threshold guide's `prepaid_balance_threshold_configuration`. Do not copy these examples without verifying the current contract schema and corrected dates.

A subscription-linked recurring credit can create a shared pool by referencing the subscription's temporary identifier. Each period supplies `access_amount` of contract balance per seat, and seat additions release additional shared balance according to proration. Individual-seat allocation instead gives each identified seat a periodic balance that only that seat can consume; its usage path depends on the configured metric group key, product presentation group key, stable event seat identifier, and `SEAT_BASED` subscription configuration.

### Commit-usage analytics boundary

A GTM analytics guide derives expected commit pacing from an access schedule and proposes actual burn from finalized plus current-period invoice data. At the model level it joins a populated `line_item.commit_id` to the access-schedule balance ID and sums attributed amounts within that schedule's service period; however, its base-versus-breakdown table family and grain remain unresolved and must be verified before aggregation. A null commit ID cannot be attributed to a particular commit and is excluded from the curve.

> [!warning] Contradiction
> The GTM guide labels every null commit ID as on-demand usage, while the revenue-reporting guide says null can mean on-demand or overage and requires client-defined metadata to distinguish them. Preserve only the non-attribution conclusion until classification is verified.

## Commit-balance notifications

Threshold notifications can monitor credit and commit remaining balance, percent remaining, or days remaining. A custom field can narrow the evaluated objects; the example filters credit entities to `credit_type: free_trial` and creates a `$0` **Contract credit balance** notification for selected customers. The page does not define balance aggregation, percent denomination or rounding, day-count boundaries, missing-field behavior, or whether these dimensions have identical semantics for credits and commits.

A merchant can create `low_remaining_commit_balance_reached` for a customer, credit type, and threshold. The resulting signal can support customer communication, sales outreach, or a merchant-owned service cutoff when the balance reaches zero. The page does not define which contract- or customer-level commits contribute, applicability or priority effects, expired-balance treatment, inclusion of credits, or automatic access enforcement.

## Sources

- [[source-metronome-api-reference-credits-and-commits-disable-trueup-for-commit]] — bearer-secured postpaid true-up invoice suppression, payload requiredness distinction, success and error envelopes, API-wide idempotency context, and lifecycle unknowns
- [[source-metronome-api-reference-contracts-archive-a-contract]] — associated commit and credit archival, active prepaid-balance expiration entries, and ledger casing ambiguity
- [[source-metronome-api-reference-credits-and-commits-release-external-payment-gate-threshold-commit]] — pending-commit release or cancellation, required external workflow ID, accepted outcome values, and recovery unknowns

- [[source-metronome-guides-pricing-packaging-make-pricing-changes-edit-contract]] — commit and credit edit capabilities, rollover cutoffs, schedule-ledger behavior, and archival prerequisites
- [[source-metronome-guides-reporting-insights-financial-reporting-revenue-recognition-examples]] — prepaid purchase, drawdown, expiration, overage, and postpaid true-up examples with amount, key, and classification conflicts

- [[source-metronome-guides-pricing-packaging-apply-credits-and-commits-prioritization-rules]] - rollover, prepaid, and postpaid burn-down ordering; type precedence; applicability and schedule tie-breakers; and the postpaid-list ambiguity
- [[source-metronome-guides-pricing-packaging-billing-model-guides-prepaid-credits]] — end-to-end prepaid-credit model, merchant-owned entitlement, Stripe-gated purchase, auto-recharge lifecycle, and example contradictions
- [[source-metronome-guides-pricing-packaging-subscription-provision-your-customer]] - subscription-linked shared recurring credits, per-seat grants, and individual-seat credit attribution prerequisites
- [[source-metronome-guides-reporting-insights-gtm-reporting-get-commit-and-usage-analytics]] — access-schedule pacing, unresolved invoice-data grain, commit-attributed burn, and the null-commit on-demand-versus-overage contradiction
- [[source-metronome-guides-pricing-packaging-billing-model-guides-model-hierarchical-customer-relationships]] — parent commit access for all, no, or selected children and self-paid overage boundary

- [[source-github-metronome-node]] - exact `3.10.0` commit cost-basis and contract-applicability types

- [[source-metronome-guides-reporting-insights-financial-reporting-revenue-recognition]] - prepaid and postpaid reporting treatment, free-credit contra-revenue boundary, and ledger double-counting exclusions

- [[source-metronome-guides-invoices-invoice-optimization-import-existing-invoices]] — contract-priced historical-invoice totals and bounded effects on customer credit and commit balances

- [[source-metronome-guides-pricing-packaging-apply-credits-and-commits-alerts]] — credit and commit threshold dimensions, free-trial custom-field filtering, and access-action boundary
- [[source-metronome-guides-pricing-packaging-make-pricing-changes-use-currency-custompricingunits]] — custom-unit access schedules, matching-unit balance drawdown, and residual fiat conversion boundary
- [[source-metronome-guides-invoices-invoice-optimization-issue-credit-memos]] — future customer- or contract-level credit boundary versus external A/R credit memos

- [[source-metronome-guides-pricing-packaging-billing-model-guides-enterprise-commit]] — enterprise commitment design, schedules, rollover, discounts, and lifecycle examples
- [[source-metronome-api-reference-contracts-create-a-contract]] — current create-contract request schema and conditional constraints
- [[source-metronome-api-reference-credits-and-commits-create-a-commit]] — customer-level create endpoint, conditional invoicing, scope, priority, and response boundary
- [[source-metronome-guides-pricing-packaging-apply-credits-and-commits-create-a-pre-paid-commit]] — free credits, prepaid and postpaid commits, recurring grants, transitions, and line-item drawdown
- [[source-metronome-guides-customers-billing-optimize-customer-experience-prepaid-balance-thresholds]] — automatic recharge, balance inclusion, payment gating, and failure handling
- [[source-metronome-guides-customers-billing-manage-customers-schedule-billing-provider-change]] — threshold removal prerequisite for marketplace transitions
- [[source-metronome-api-reference-credits-and-commits-edit-a-commit]] — targeted commit fields, schedule operations, applicability, and hierarchy access
- [[source-metronome-integrations-tax-integrations-stripe-tax]] — explicit tax configuration for threshold and payment-gated flows
- [[source-metronome-api-reference-contracts-amend-a-contract]] — legacy amendment commit/credit schedules, targeting, priority, and validation gaps
- [[source-metronome-guides-implement-metronome-core-concepts-provision-contract]] — worked commit schedules, tag scope, platform charge, and consolidation
- [[source-metronome-guides-pricing-packaging-subscription-subscription-overview]] — pooled or per-seat subscription-credit scope
- [[source-metronome-guides-pricing-packaging-subscription-manage-subscription-lifecycle]] — bounded hybrid-subscription cancellation rule
- [[source-metronome-guides-pricing-packaging-apply-credits-and-commits-manual-payment-gated-commits]] — manual Stripe gate, invoice voiding, and explicit retry
- [[source-metronome-guides-pricing-packaging-billing-model-guides-create-a-trial]] — capped trial grant, priority, and expiry boundary
- [[source-metronome-guides-customers-billing-set-up-notifications-offset-notifications]] — recurring-child generation horizon and before-segment offset timing limitation
- [[source-metronome-guides-customers-billing-manage-customers-spend-trackers]] — commit-purchase tracking, threshold-discount caps, reset behavior, and manual enforcement boundary
- [[source-metronome-guides-customers-billing-optimize-customer-experience-set-customer-spend-control]] — spend-triggered commit representation, optional payment gate, and external release/cancel flow
- [[source-metronome-guides-customers-billing-optimize-customer-experience-customer-controls]] — low-remaining-commit alert and merchant-owned outreach or access action
- [[source-metronome-guides-customers-billing-optimize-customer-experience-get-remaining-balance]] — aggregate and detailed balance APIs, signed-ledger arithmetic, precision, effective time, entry types, and manual adjustments

- [[source-metronome-api-reference-credits-and-commits-create-a-credit]] - customer-level credit creation, payload and schedule requiredness, applicability, priority, uniqueness, response, and lifecycle boundaries

- [[source-metronome-api-reference-credits-and-commits-list-balances]] - detailed balance request and response schemas, endpoint-specific pagination, archive asymmetry, schedule-unit boundary, calculated-balance floor, custom fields, and ledger-enum contradictions

## Related

- [[metronome-customers-and-contracts]]
- [[metronome-products-and-rate-cards]]
- [[metronome-usage-based-billing]]
- [[metronome-invoicing]]
- [[metronome-subscriptions]]
