---
title: "Metronome Provision Your Customer Subscription"
type: source
date_ingested: 2026-08-19
original_format: webpage
canonical_url: "https://docs.metronome.com/guides/pricing-packaging/subscription/provision-your-customer.md"
raw_files:
  - "metronome/guides/pricing-packaging/subscription/provision-your-customer-2026-07-13.md"
tags: [metronome, subscriptions, seat-based-billing, credits, contracts, invoicing]
---

## Overview

This guide explains how to provision standard, pooled-credit, and individual-seat-credit subscriptions on a Metronome customer contract. It covers subscription-rate selection, quantity and proration configuration, billing-cycle and invoice placement, recurring-credit linkage, and the metric, product, event, and contract prerequisites for seat-scoped credits.

## Key takeaways

- Metronome documents three contract subscription configurations: a standard recurring fee, a seat-based shared credit pool, and credits allocated to individual seats; overages in both credit models are billed at contract level.
- Each standard subscription config selects a rate by `billing_frequency` and `product_id`, sets collection in advance or arrears, supplies initial quantity, and defines proration and invoice timing for mid-period quantity changes.
- A subscription is not charged unless its config exists and its associated rate is enabled on the contract. An override must identify both billing frequency and product because one product can have several rates.
- Advance subscriptions can use a custom billing anchor and can place charges on matching usage invoices or scheduled invoices. Invoice routing and payment collection on Metronome's behalf additionally require a contract billing-provider configuration.
- Individual-seat credits require a metric group key, a product presentation group key, a stable seat identifier on every usage event, and `SEAT_BASED` contract configuration; the guide and dedicated create-contract schema disagree on the unassigned-seat field name.

## Standard subscription provisioning

A subscription is configured inside the create-contract request. Its `subscription_rate` identifies the rate-card entry using both `billing_frequency` and `product_id`; `collection_schedule` selects `advance` or `arrears`; and `initial_quantity` supplies the current quantity, such as the seat count or `1` for a platform license. The `proration` object controls whether mid-period quantity changes are prorated and whether they invoice immediately or on the next billing cycle, with optional rounding for prorated charges. A subscription may also have dates that differ from the contract and a name or description shown on its invoice line item.

A contract override can discount the list rate and enable it. Because one product may map to multiple subscription rates, the override must also specify both billing frequency and product ID. The guide explicitly says Metronome will not charge the subscription unless a subscription config is present and the associated rate is enabled; it does not establish `enabled` as a literal request-field name, and its examples use an `entitled` override.

## Billing cycle, invoice placement, and routing

The optional `billing_cycle_config` decouples a subscription from the contract's default cycle. Its `anchor_date` must be on or before the subscription start and is supported only for advance subscriptions. Without a custom anchor, the subscription follows the contract's usage-invoice anchor, typically the first of the month.

`invoice_placement` defaults to `ON_USAGE_INVOICE`, placing the subscription charge on the usage invoice with the matching billing date. `ON_SCHEDULED_INVOICE` instead appends the charge to an existing scheduled invoice with that billing date or creates a new scheduled invoice when none exists. These placement rules do not establish invoice finalization, delivery, collection, payment timing, or provider success.

To route invoices and collect payment through Metronome, the guide requires the contract to include `billing_provider_configuration`. This is a conditional requirement for that routing and collection path, not evidence that every create-contract request requires the field or that its presence guarantees a downstream outcome.

## Shared subscription credit pool

A pooled-credit subscription follows the standard subscription setup and also links to a recurring credit. During contract creation, the subscription receives a `temporary_id`, and the recurring-credit config references that identifier through its subscription configuration. Each billing period, the contract receives shared balance equal to `access_amount` per seat. Adding seats makes additional shared balance available according to the configured proration. An existing standard subscription can later be linked to a recurring credit through `add_recurring_credits` on contract edit, although this guide does not supply that endpoint's complete schema or lifecycle behavior.

## Individual seat credits

Individual-seat allocation gives each identified seat a balance that only that seat can consume. The guide states a default support boundary of up to 1,000 seats and directs larger implementations to contact Metronome; it is not presented as an immutable API maximum.

The model requires a stable unique seat identifier, such as an email address or internal user ID. The underlying streaming billable metric must define the seat property as a group key before metric creation because that group key cannot later be edited. Applicable usage products then use the same property as a presentation group key, and every usage event must include the seat property so consumption maps to the correct seat.

On the contract, the guide says to set `quantity_management_mode` to `SEAT_BASED` and populate `seat_config` rather than a simple quantity. It names three labels: `initial_seat_ids`, `initial_unassigned_seats_quantity`, and `seat_group_key`. It says the unassigned-seat value contributes to total subscription quantity but does not generate credits until a seat ID is specified. The illustrated recurring commit references the subscription and sets `allocation: "INDIVIDUAL"`.

> [!warning] Documentation contradiction
> This provisioning guide names the unassigned-seat field `initial_unassigned_seats_quantity`, while the dedicated create-contract schema from the same collection snapshot names it `initial_unassigned_seats`. The evidence does not establish which spelling is current runtime truth; verify the live schema before implementation.

## Documentation boundaries

The payloads are worked examples, not complete request or response schemas. The page does not define seat-ID collision handling, reassignment or removal mechanics, concurrent edits, exact proration formulas, failure atomicity, idempotency, error responses, or how individual-seat balances behave after a seat is removed. The field-name contradiction above is separate from those lifecycle unknowns. Dedicated current contract and edit-contract API references remain the implementation authority.

No other contradiction was found with the reviewed canonical Metronome subscription, contract, rate-card, billable-metric, event-ingestion, credit-and-commit, or invoicing material.

## Related

- Company: [[metronome]]
- Concepts: [[metronome-subscriptions]], [[metronome-credits-and-commits]], [[metronome-invoicing]]
- Related sources: [[source-metronome-guides-pricing-packaging-subscription-subscription-overview]], [[source-metronome-guides-pricing-packaging-subscription-define-subscription-pricing]], [[source-metronome-api-reference-contracts-create-a-contract]], [[source-metronome-guides-pricing-packaging-apply-credits-and-commits-create-a-pre-paid-commit]]

## Raw Sources

- [[raw/metronome/guides/pricing-packaging/subscription/provision-your-customer-2026-07-13|2026-07-13 snapshot - subscription provisioning, billing-cycle configuration, and pooled and individual seat credits]]
