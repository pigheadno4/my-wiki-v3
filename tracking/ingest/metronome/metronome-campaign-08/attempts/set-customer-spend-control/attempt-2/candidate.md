---
title: "Metronome Enforce Spend Thresholds"
type: source
date_ingested: 2026-07-31
original_format: webpage
canonical_url: "https://docs.metronome.com/guides/customers-billing/optimize-customer-experience/set-customer-spend-control"
raw_files:
  - "metronome/guides/customers-billing/optimize-customer-experience/set-customer-spend-control-2026-07-13.md"
tags: [metronome, spend-thresholds, payment-gating, contracts, fraud-risk, webhooks]
---

## Overview

This guide documents Metronome spend-threshold billing for a customer contract. A configured threshold determines when accumulated contract spend triggers a payment attempt; optional payment gating controls whether the resulting commit is released, with Stripe and external-gateway paths. The feature limits exposure to uncollected revenue by charging incrementally, but this page does not establish a hard application-access block or a customer-wide spending cap.

## Key takeaways

- `spend_threshold_configuration.threshold_amount` is the contract-spend level that triggers a payment attempt. The source does not define currency, denomination, equality behavior, aggregation, or how spend is allocated across concurrent contracts.
- The configuration identifies a commit product for the customer-facing incremental invoice and can choose whether commit release is payment-gated.
- Stripe collection can use a Stripe Billing invoice or a direct PaymentIntent and requires a valid Stripe billing configuration on the contract. Setting `is_enabled: true` requests immediate evaluation after contract creation.
- A spend-threshold configuration can be added to an existing contract or updated later; the page says changes take effect immediately but does not define whether an edit synchronously evaluates spend or attempts payment.
- With `payment_gate_type: EXTERNAL`, the integrator owns collection, retains the `workflow_id` from `payment_gate.external_initiate`, and calls the threshold-release endpoint to release the commit after success or cancel it after failure.
- Payment success and failure are communicated through webhook workflows, but this page does not name the ordinary success/failure event types or define retry behavior.

## Contract configuration

A contract can optionally carry `spend_threshold_configuration`. The documented fields cover a `threshold_amount`, a commit definition with the product shown on the incremental invoice, enablement, and a `payment_gate_config`. The payment gate selects `EXTERNAL` for an unsupported gateway or, for Stripe, chooses a Stripe Billing invoice versus a direct PaymentIntent and selects an existing tax provider.

The example uses `payment_gate_type: "NONE"`, demonstrating that a threshold can be configured without gating commit release on payment. The page does not explain the resulting commit's access schedule, amount, type, ledger behavior, invoice finalization, or what occurs if an ungated payment attempt later fails. The sample amounts and product IDs are illustrative rather than limits or defaults.

For Stripe, the contract must already have a valid billing configuration. At initial contract creation, `is_enabled: true` asks Metronome to evaluate the contract immediately. The source does not define the evaluation transaction boundary, whether an existing spend balance is included, duplicate-attempt suppression, or concurrency behavior.

## Adding and updating thresholds

The guide says a spend threshold can be added to a previously unlimited contract or changed later, including after a history of successful payments. Its examples use `add_spend_threshold_configuration` and `update_spend_threshold_configuration` in contract-edit payloads, and it states that changes take effect immediately.

> [!warning] Documentation links
> The creation section links its Metronome API text to an edit-contract path, while the editing section links its API text to `/api-reference/authorization`. Neither link establishes the authoritative create or edit endpoint. Use the dedicated current contract references for method, path, schema, and authorization details.

The page does not define whether add and update are mutually exclusive, how a threshold is disabled or removed, whether omitted nested fields are preserved, how edits interact with an in-flight payment gate, or whether threshold changes affect finalized invoices.

## Payment gating and external collection

`payment_gate_config` controls whether commit release waits for collection and which gateway participates. For Stripe, the guide offers invoice or PaymentIntent collection; this page does not specify the Stripe object lifecycle, default-payment-method requirements, tax request shape, failure invoice behavior, automatic retries, or customer-action handling.

For an external gate, Metronome emits `payment_gate.external_initiate` when it is ready for the outcome. The integrator must store its `workflow_id`, charge the customer through the chosen gateway, and call `commits/threshold-billing/release` to release the commit after success or cancel it after failure. The page does not define event ordering, duplicate delivery handling, workflow expiry, idempotency, authentication, retry safety, or the state and visibility of the pending commit before release or cancellation.

## Enforcement, alert, and customer boundaries

The page uses "enforce" and "cap" language to describe incremental collection that limits exposure to unpaid spend. It documents a payment trigger and optional commit-release gate; it does not say Metronome blocks further usage, disables product access, rejects events, or enforces a merchant application's authorization decision.

Spend threshold billing is configured on a contract. The source does not establish customer-wide aggregation across multiple contracts, treatment of credits or commits in the spend calculation, threshold reset timing, which draft or finalized charges count, or whether refunds and adjustments reduce tracked spend.

The guide tells readers to watch webhook notifications for payment success or failure and delegates detailed failure handling to the separate prepaid-balance threshold lifecycle. It does not itself name the ordinary payment-status events, establish that every prepaid-balance failure rule applies identically to spend thresholds, or define alert timing, webhook delivery, payment retry, and re-enablement behavior.

## Related

- Company: [[metronome]]
- Concepts: [[metronome-spend-threshold-billing]], [[metronome-customers-and-contracts]], [[metronome-invoicing]], [[metronome-credits-and-commits]], [[metronome-integrations]], [[metronome-alerts-and-notifications]], [[metronome-webhooks]]
- Related sources: [[source-metronome-api-reference-contracts-create-a-contract]], [[source-metronome-guides-customers-billing-optimize-customer-experience-prepaid-balance-thresholds]], [[source-metronome-guides-platform-configuration-setup-webhooks]], [[source-metronome-integrations-tax-integrations-stripe-tax]]

## Raw Sources

- [[raw/metronome/guides/customers-billing/optimize-customer-experience/set-customer-spend-control-2026-07-13|2026-07-13 snapshot — spend-threshold configuration, updates, payment gates, and external collection]]
