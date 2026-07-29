---
title: "Set prepaid balance thresholds"
type: source
date_ingested: 2026-07-29
canonical_url: "https://docs.metronome.com/guides/customers-billing/optimize-customer-experience/prepaid-balance-thresholds"
original_format: webpage
raw_files:
  - "metronome/guides/customers-billing/optimize-customer-experience/prepaid-balance-thresholds-2026-07-13.md"
tags: [metronome, prepaid-credits, balance-thresholds, auto-recharge, payment-gating]
---

## Overview

This guide documents Metronome's contract-level prepaid balance threshold configuration. It covers automatic recharge, manual commit purchases, optional payment-gated balance release, fiat and custom-pricing-unit balances, balance inclusion and exclusion rules, configuration changes, notifications, and the Stripe and external-gateway payment lifecycles.

Prepaid credits are modeled as commits. Customers fund usage in advance and are expected to maintain a positive balance to retain product access; this page configures the balance and payment workflow, but does not describe how a merchant should enforce product-access gating.

## Key takeaways

- `threshold_amount` is the balance level at which Metronome initiates recharge, and `recharge_to_amount` is the balance to restore. The default threshold calculation totals contract- and customer-level commits and credits while always excluding individual seat-scoped balances.
- Thresholds work with fiat currency and custom pricing units (CPUs). CPU threshold and recharge values are expressed in the custom unit, then converted to fiat for payment using the customer's rate-card conversion rate.
- Payment gating can defer release of balance from an automatic recharge or manual purchase until payment succeeds. Metronome supports Stripe configuration and an `EXTERNAL` flow in which the integrator charges the customer and explicitly releases or cancels the commit.
- Stripe use requires a valid contract billing configuration. `payment_type` chooses a Stripe Billing invoice or a direct Stripe PaymentIntent; `is_enabled: true` requests immediate evaluation when the contract is created.
- Updating the threshold configuration takes effect immediately and forces evaluation against the customer's current balance.
- A failed gated payment disables the configuration, produces a voided invoice in Metronome and Stripe, and is not retried automatically. Re-enabling the configuration forces a new threshold evaluation and payment attempt.

## Configuration and balance semantics

### Threshold and recharge amounts

A contract may include `prepaid_balance_threshold_configuration` with a commit definition, `threshold_amount`, `recharge_to_amount`, `is_enabled`, and an optional `payment_gate_config`. Metronome describes `threshold_amount` as the level at which the customer is recharged and `recharge_to_amount` as the target balance after recharge begins.

By default, evaluation counts all prepaid contract- and customer-level commits and credits. Individual seat-scoped commits and credits are always excluded. A `threshold_balance_specifiers` configuration can narrow the balances considered; the guide's examples use custom fields on `ContractCreditOrCommit` objects to exclude trial balances from the recharge decision.

The auto-recharge note documents a minimum threshold value of $5 and requires the recharge target to be at least $10 above the threshold. It says those minimums apply to fiat and CPU-denominated balances; CPU values are evaluated in the custom pricing unit and converted to fiat through the rate-card conversion rate.

For a CPU example where one AI Token equals $0.10, a balance falling to 50 tokens with a 500-token recharge target creates a 450-token commit and a $45 payment through the configured gateway.

### Balance exclusion logic

When multiple `custom_field_filters` objects appear in an exclusion condition, a balance matching at least one filter is excluded (OR logic). When multiple key-value entries appear in one `custom_field_filters` array, the balance must match every entry to be excluded (AND logic). The same custom-field key cannot be repeated inside one filter.

The guide demonstrates excluding a product-specific trial credit tagged `credit_type: ai_trial`, and then demonstrates exclusions for either `credit_type: ai_trial` or `credit_type: june_product_launch_trial`. A separate example excludes only balances that have both `credit_type: ai_trial` and `is_active: true`.

### Payment gate and billing prerequisites

`payment_gate_config` controls whether balance release waits for payment and which gateway is used. Choose `EXTERNAL` for a gateway Metronome does not support. For Stripe, `PAYMENT_TYPE` selects a Stripe Billing invoice or a direct `paymentIntent`, and the configuration can select an existing tax provider. The contract must have a valid Stripe billing configuration.

If `is_enabled` is `true` at contract creation, Metronome immediately evaluates the contract. When payment gating is enabled and payment fails, Metronome changes `is_enabled` to `false`.

### Optional discounts

`discount_config` has a `fraction` and an optional `cap`. The cap is tracked through a spend tracker; after accumulated spend reaches the cap, later recharges are not discounted for the remainder of that tracker's period. With CPUs, the invoice schedule amount is first calculated using the overage rate. The guide's example converts 100 AI credits to $50 at a 2:1 conversion and says a 10% discount makes the charge $45.

## Timing and lifecycle

### Creation and updates

Contracts can be created or edited through the Metronome app or API. Adding or changing `prepaid_balance_threshold_configuration`, including changing `threshold_amount`, takes effect immediately and forces evaluation of the current customer balance on every configuration change.

### Stripe-gated recharge

After configuration, Metronome evaluates the remaining available contract balance. When the threshold is reached and the payment gate is Stripe, Metronome attempts to charge the customer in Stripe. If payment succeeds, Metronome creates the commit needed to bring the customer back to `recharge_to_amount`.

Metronome sends three threshold-billing webhook types:

- `payment_gate.threshold_reached` when the threshold is reached.
- `payment_gate.payment_status` after a payment attempt, with `payment_status` equal to `paid` or `failed`.
- `payment_gate.payment_pending_action_required` when payment processing needs intervention.

The merchant must configure its webhook endpoint to handle these notifications.

### Failed payments

On failure, `payment_gate.payment_status` reports `failed`, the contract's `is_enabled` becomes `false`, and the guide says a voided invoice should appear in both Metronome and Stripe. The merchant must follow up with the customer directly or automate a workflow from the webhook. To try again, set `is_enabled` to `true`; this forces threshold evaluation and a new payment attempt. Metronome explicitly does not retry failed payments automatically.

### External payment gate

For `payment_gate_type: EXTERNAL`, the integrator must:

1. Configure the external payment gate.
2. Listen for `payment_gate.external_initiate`.
3. Save its `workflow_id`, which is required to release the commit.
4. Charge the customer through the chosen gateway.
5. Call `commits/threshold-billing/release` to release the commit after success or cancel it after failure.

## Documentation cautions and boundaries

> [!warning] Threshold boundary wording
> The page says auto recharge occurs when balance "drops to" or "hits" `threshold_amount`, but the balance-specifier section says recharge occurs when matching balances "drop below" it. This source does not reconcile whether equality triggers every evaluation path.

> [!warning] Minimum-field naming
> The minimums note uses `recharge_threshold` and `recharge_to amount`, while the configuration fields elsewhere are `threshold_amount` and `recharge_to_amount`. The examples use the latter field names.

> [!warning] Discount fraction wording
> The page describes `fraction` as "the discount applied" but its JSON uses `fraction: 0.9` and its CPU example describes that configuration as a 10% discount. The source does not explicitly define whether the value is a retained invoice fraction or a discount fraction, so the example and API contract should be checked before implementation.

The page names manual commit purchase as a supported path and says payment gating can govern its balance release, but its detailed lifecycle is specifically the threshold-triggered recharge flow. It does not document the manual-purchase sequence on this page. It also does not specify concurrency, duplicate recharge suppression, or ordering guarantees for threshold evaluations and webhooks.

## Related

- Company: [[metronome]]
- Concepts: [[metronome-credits-and-commits]], [[metronome-customers-and-contracts]], [[metronome-invoicing]], [[metronome-products-and-rate-cards]], [[metronome-webhooks]], [[metronome-integrations]]
- Related sources: [[source-metronome-guides-pricing-packaging-apply-credits-and-commits-create-a-pre-paid-commit]], [[source-metronome-guides-pricing-packaging-billing-model-guides-enterprise-commit]], [[source-metronome-api-reference-contracts-create-a-contract]], [[source-metronome-guides-platform-configuration-setup-webhooks]], [[source-metronome-integrations-invoice-integrations-stripe]], [[source-metronome-guides-customers-billing-manage-customers-schedule-billing-provider-change]]

## Raw Sources

- [[raw/metronome/guides/customers-billing/optimize-customer-experience/prepaid-balance-thresholds-2026-07-13|2026-07-13 snapshot — Set prepaid balance thresholds]]
