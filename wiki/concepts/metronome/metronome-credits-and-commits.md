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

## Drawdown and invoice attribution

- Credits and prepaid commits draw down before postpaid commits; lower numeric priorities consume first.
- The same usage can apply to only one credit or commit, with any remainder continuing as postpaid fulfillment or overage.
- Application occurs at invoice line-item level. Covered usage, the negative balance-application line, and uncovered overage remain separately attributable.
- Every credit or commit uses a fixed product for invoice and reporting attribution, while product IDs, tags, or specifiers can restrict eligible usage.
- Stripe-taxed prepaid-balance thresholds, spend thresholds, and one-off payment-gated commits require `payment_gate_type: "STRIPE"`, `tax_type: "STRIPE"`, and `stripe_config.payment_type: "INVOICE"`; account-level tax enablement does not cover these flows.

## Prepaid balance thresholds

A contract can automatically replenish prepaid value when its eligible balance reaches a configured `threshold_amount`. `recharge_to_amount` is the target balance, so Metronome creates only the commit needed to restore that level. The default calculation includes contract- and customer-level commits and credits but always excludes individual seat-scoped balances. Threshold balance specifiers can additionally exclude balances by `ContractCreditOrCommit` custom fields.

Thresholds support fiat and custom pricing units. Custom-unit amounts are converted to fiat for payment through the customer's rate-card conversion. Payment gating can delay release of an automatic or manually purchased commit until Stripe or an external gateway confirms payment.

A failed gated payment disables the threshold configuration and is not retried automatically. Re-enabling it forces a fresh balance evaluation and payment attempt. An external gateway must retain the `payment_gate.external_initiate` workflow ID and call the threshold-release endpoint to release or cancel the commit.

Active threshold billing must be removed before a contract can transition to an AWS, Azure, or GCP Marketplace billing provider.

> [!warning] Documentation ambiguity
> The threshold guide alternates between recharge at the threshold and recharge only below it. It also describes `discount_config.fraction` as the discount while showing `0.9` for a 10% discount, and its minimums note uses field labels that differ from the request examples. Confirm these boundaries against the current API schema.

## Customer-level create API

`POST /v1/contracts/customerCommits/create` creates a balance outside an individual contract for enterprise-wide or multi-contract use. Metronome recommends contract-level commits for standard cases.

- The request requires customer, type, priority, fixed product, and access schedule.
- Postpaid commits require matching access and invoice totals, one item in each schedule, and an invoice contract.
- A prepaid commit can omit invoicing to create a complimentary balance.
- Contract scope can be explicit or cross-contract; product scope can use IDs, tags, or specifiers.
- Lower priority numbers consume first, with contract-level balances winning ties over customer-level balances.
- `uniqueness_key` prevents duplicate creation; its description documents a `409` failure.

## Targeted commit edits

`POST /v2/contracts/commits/edit` changes one contract-level or customer-level commit identified by `customer_id` and `commit_id`. It can update display fields, access or invoice schedule items, invoicing contract, applicability, priority, rate type, fixed product, or hierarchy access.

- Schedule items use separate add, update, and remove arrays; updates and removals address existing items by UUID.
- Direct product ID or tag selectors cannot be combined with `specifiers`.
- Hierarchy child access can allow all children, no children, or a non-empty contract-ID list.
- The schema does not define general omitted-versus-null mutation semantics, the meaning of its success `data.id`, or the interaction between top-level `product_id` and the applicability selectors.

## Documentation cautions

The guides contain example-level inconsistencies that should be checked against the current API schema before implementation:

- Its create-contract sample uses `product` inside a commit, while the dedicated create-contract API reference documents `product_id`.
- Its upsell prose calls the new $300,000 term a commitment, while the accompanying edit request adds a scheduled charge rather than a commit.
- The customer-commit schema exposes a generic recurring invoice schedule, while its postpaid prose requires one schedule item; confirm this combination before use.

> [!warning] Contradiction
> The credits-and-commits guide's prepaid prose describes $10,000 of accessible value, while its sample grants `100000` USD cents ($1,000) and invoices `1000000` cents ($10,000). Its recurring examples also contain invalid JSON, dates that conflict with the described January 1 signup and January 21 upgrade, and `rollover_fraction: 100`; the dedicated create-contract reference constrains this fraction to 0–1.

## Sources

- [[source-metronome-guides-pricing-packaging-billing-model-guides-enterprise-commit]] — enterprise commitment design, schedules, rollover, discounts, and lifecycle examples
- [[source-metronome-api-reference-contracts-create-a-contract]] — current create-contract request schema and conditional constraints
- [[source-metronome-api-reference-credits-and-commits-create-a-commit]] — customer-level create endpoint, conditional invoicing, scope, priority, and response boundary
- [[source-metronome-guides-pricing-packaging-apply-credits-and-commits-create-a-pre-paid-commit]] — free credits, prepaid and postpaid commits, recurring grants, transitions, and line-item drawdown
- [[source-metronome-guides-customers-billing-optimize-customer-experience-prepaid-balance-thresholds]] — automatic recharge, balance inclusion, payment gating, and failure handling
- [[source-metronome-guides-customers-billing-manage-customers-schedule-billing-provider-change]] — threshold removal prerequisite for marketplace transitions
- [[source-metronome-api-reference-credits-and-commits-edit-a-commit]] — targeted commit fields, schedule operations, applicability, and hierarchy access
- [[source-metronome-integrations-tax-integrations-stripe-tax]] — explicit tax configuration for threshold and payment-gated flows

## Related

- [[metronome-customers-and-contracts]]
- [[metronome-products-and-rate-cards]]
- [[metronome-usage-based-billing]]
- [[metronome-invoicing]]
