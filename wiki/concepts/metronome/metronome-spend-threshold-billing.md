---
title: "Metronome Spend Threshold Billing"
type: concept
category: technology
tags: [metronome, spend-thresholds, payment-gating, contracts, fraud-risk]
---

## Definition

Metronome spend-threshold billing configures a contract-spend amount that triggers incremental collection. A `spend_threshold_configuration` defines the threshold, the commit product represented on the incremental invoice, enablement, and optional payment-gate behavior. This limits exposure to uncollected revenue; it is not documented as a merchant-application access control or a customer-wide hard spending cap.

## Configuration and lifecycle

Stripe collection can use a Stripe Billing invoice or direct PaymentIntent and requires valid contract billing configuration. `is_enabled: true` requests immediate evaluation after contract creation. A threshold can be added to an existing contract or updated later, and the page says changes take effect immediately without defining synchronous evaluation, payment, concurrency, or invoice effects.

## Payment gates

A payment gate can delay commit release. With `EXTERNAL`, the integrator receives `payment_gate.external_initiate`, stores its `workflow_id`, collects through its own gateway, and calls the threshold-release endpoint to release the commit on success or cancel it on failure. The source does not define ordinary Stripe failure events, retries, pending-commit visibility, event ordering, workflow expiry, or idempotency.

## Documentation boundaries

The source does not define spend aggregation across contracts, currency or amount denomination, equality behavior, reset periods, credit/commit treatment in the spend calculation, access enforcement, notification timing, or complete create/edit schemas. Its creation API link points to edit-contract documentation and its edit API link points to authorization, so dedicated current API references remain authoritative.

## Sources

- [[source-metronome-guides-customers-billing-optimize-customer-experience-set-customer-spend-control]] — contract configuration, updates, payment gates, and external collection

## Related

- [[metronome-customers-and-contracts]]
- [[metronome-invoicing]]
- [[metronome-credits-and-commits]]
- [[metronome-integrations]]
- [[metronome-alerts-and-notifications]]
- [[metronome-webhooks]]
