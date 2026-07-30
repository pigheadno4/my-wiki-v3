---
title: "Payment-gated commits"
type: source
date_ingested: 2026-07-30
canonical_url: "https://docs.metronome.com/guides/pricing-packaging/apply-credits-and-commits/manual-payment-gated-commits"
original_format: webpage
raw_files:
  - "metronome/guides/pricing-packaging/apply-credits-and-commits/manual-payment-gated-commits-2026-07-13.md"
tags: [metronome, payment-gating, prepaid-commits, stripe, webhooks]
---

## Overview

This guide describes a manually requested prepaid commit that is added to an existing Metronome contract and released only after a Stripe payment succeeds. Metronome initiates and monitors the payment, reports the result or required intervention through payment-gating webhooks, and creates no commit after a failed payment. The page documents this Stripe path rather than a provider-agnostic payment-gating or application access-control mechanism.

## Key takeaways

- Payment-gated commits can be added only to existing contracts through the contract-edit flow, and the contract needs a valid billing configuration.
- Before requesting one, the customer needs a default payment method in the configured payment provider and a stored valid address; the guide says either missing prerequisite causes payment failure.
- The commit's Metronome product must map to a Stripe Product ID through a `stripe_product_id` custom field and a mapping to `invoiceitem.price`; otherwise Stripe cannot generate the invoice line item and payment fails.
- Metronome attempts payment for the commit's invoice amount. Success releases the commit balance, failure voids the associated Metronome and Stripe invoices and creates no commit, and an authentication challenge produces an action-required notification.
- `payment_gate.payment_status` reports `paid` or `failed`, while `payment_gate.payment_pending_action_required` reports required intervention. A failed payment is not retried automatically; retrying requires a new Metronome API request with the commit information.

## Flow and prerequisites

The documented use case is a prepaid product-led-growth flow in which the organization waits for successful payment before making the purchased balance available. Metronome initiates payment with the configured billing provider and monitors completion. The guide says successful payments and credit release usually complete within seconds, but actual timing depends on the payment provider, payment method, and authentication challenges; this is not a fixed latency guarantee.

The customer must have a default payment method configured with the billing provider, and the checkout flow must capture and retain a valid customer address. For the documented Stripe implementation, the product attached to the commit must have a `stripe_product_id` Metronome Product custom field containing the corresponding Stripe Product ID, plus a Stripe integration mapping from that field to `invoiceitem.price`.

## Request shape

A payment-gated commit is added to an existing contract through the linked contract-edit API. The example supplies `customer_id`, `contract_id`, and one `add_commits` entry with a fixed `product_id`, `type: "prepaid"`, an invoice schedule, an access schedule, `priority: 100`, and `payment_gate_config.payment_gate_type: "STRIPE"`. Its sample also sets `tax_type: "STRIPE"`; this page shows that field but does not separately define when tax configuration is required.

Both sample schedules use an amount of `2000`, and the access item runs from April 1, 2025 through April 1, 2026. The guide does not state the amount's currency or unit, general schedule-validation rules, or whether access and invoice amounts must always match, so the payload should not be generalized into a complete commit schema.

## Payment outcomes and notifications

Metronome immediately starts a payment attempt based on the commit invoice amount. On success, it releases the commit and associated balance. On failure, it voids the associated invoice in Metronome and Stripe and creates no commit. When additional authentication or another intervention is required, Metronome emits `payment_gate.payment_pending_action_required`; after an attempted payment, `payment_gate.payment_status` carries `paid` or `failed` in `payment_status`.

A failed payment has no automatic payment retry. The documented retry is a new Metronome API request containing the relevant commit information. That integration-level instruction does not say whether Stripe reuses or replaces an underlying PaymentIntent, so it must not be conflated with generic Stripe PaymentIntent retry guidance. Separately, the webhook guide documents retries for failed webhook **delivery**; those delivery retries do not mean Metronome retries the failed payment.

## Documentation boundaries

> [!info] Stripe-specific evidence
> The request and required product mapping in this page use `payment_gate_type: "STRIPE"` and a Stripe Product ID. The page does not document an external payment-gate flow or establish equivalent behavior for another billing provider. Its statement that Metronome initiates payment through the configured provider should therefore not be generalized beyond the concrete Stripe flow shown here.

> [!warning] Product-mapping terminology
> This page says to create `stripe_product_id` on the Metronome Product entity and map it to `invoiceitem.price`. The related Stripe Tax source already records that its own mapping table names `ContractProduct` while its setup prose names `Product`; these pages do not reconcile that entity terminology.

The page starts by describing creation of a payment-gated commit but later says a failed payment means no commit is created. It does not expose the identity or state of the temporary resource that is voided before success. It also does not define webhook ordering, duplicate handling, the workflow for completing required authentication, API idempotency or concurrency behavior for manual retries, Stripe object IDs or statuses, payment-method eligibility, regional availability, or failure recovery beyond sending a new request.

## Related

- Companies: [[metronome]], [[stripe]]
- Concepts: [[metronome-credits-and-commits]], [[metronome-customers-and-contracts]], [[metronome-products-and-rate-cards]], [[metronome-invoicing]], [[metronome-integrations]], [[metronome-webhooks]]
- Related sources: [[source-metronome-guides-customers-billing-optimize-customer-experience-prepaid-balance-thresholds]], [[source-metronome-integrations-invoice-integrations-stripe]], [[source-metronome-integrations-tax-integrations-stripe-tax]], [[source-metronome-guides-platform-configuration-setup-webhooks]], [[source-metronome-guides-pricing-packaging-apply-credits-and-commits-create-a-pre-paid-commit]]

## Raw Sources

- [[raw/metronome/guides/pricing-packaging/apply-credits-and-commits/manual-payment-gated-commits-2026-07-13|2026-07-13 snapshot — manual Stripe payment-gated commit flow, outcomes, notifications, and retry boundary]]
