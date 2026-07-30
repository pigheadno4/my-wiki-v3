---
title: "Metronome Provision a Customer Contract"
type: source
date_ingested: 2026-07-30
original_format: webpage
canonical_url: "https://docs.metronome.com/guides/implement-metronome/core-concepts/provision-contract"
raw_files:
  - "metronome/guides/implement-metronome/core-concepts/provision-contract-2026-07-13.md"
tags: [metronome, contracts, rate-cards, commits, scheduled-charges, usage-filters, invoicing]
---

## Overview

This implementation guide explains how to provision and evolve a Metronome customer contract. A contract encodes product access, product rates, and access duration by combining a specific rate card with terms such as commits, discounts, fixed products outside the rate card, scheduled charges, usage-invoice scheduling, billing-provider routing, and usage filters.

## Key takeaways

- The documented provisioning workflow assumes connected usage events plus an existing billable metric, product, rate card, customer, and customer billing-provider configuration.
- The worked contract starts on 2024-11-01 and combines a one-year, $10,000 prepaid commit for products tagged `cloud`, a $1,000 quarterly platform charge, monthly usage statements anchored to contract start, and direct AWS Marketplace delivery.
- The page labels adding a billing-provider configuration to a contract that previously lacked one as beta. The configuration begins at the start of the current billing period; free-trial conversions must credit trial usage so the newly routed period is not billed.
- `scheduled_charges_on_usage_invoices: ALL` can place scheduled and commit charges on a usage invoice only when the scheduled date aligns with the exclusive end day of the usage service period and that usage invoice has not finalized. Metronome evaluates consolidation at creation and again after later contract changes.
- Discounts can be created with the contract or added by editing it. The example adds an entitled `multiplier` override of `0.95` to products tagged `cloud`; dimensional pricing requires overrides for each relevant group-key and product combination.
- A customer can hold multiple simultaneous contracts with different rate cards, dates, and discounts while sharing customer-level commits and credits. Contract usage filters route event groups among those contracts and can be changed on a future-effective schedule.

## Prerequisites and contract model

Before this workflow, the guide requires usage events connected to Metronome, a billable metric, a product, a rate card, a customer, and `customer_billing_provider_configuration`. These are operational prerequisites for the documented provisioning flow; the page is not the complete create-contract schema and does not say that each item is an unconditionally required field in every API request.

Contracts are built on rate cards, which are themselves built on products. A contract selects a rate card and can layer on commits, discounts, fixed products not present on that card, and other commercial terms. Operators can create the contract in the Metronome app or through `/v1/contracts/create`.

## Worked contract, pricing, and dates

The API example identifies the customer, selects `rate_card_alias: base_usage_products`, and sets `starting_at` to `2024-11-01T00:00:00.000Z`. Its `billing_provider_configuration` selects `aws_marketplace` with `delivery_method: direct_to_billing_provider`.

The prepaid commit has its own fixed `product_id`, an access-schedule item from 2024-11-01 through `ending_before` 2025-11-01, and an invoice-schedule item dated 2024-11-01. The payload represents the narrative's $10,000 upfront charge with `amount: 1000000` and `unit_price: 1000000`, applies the balance to products tagged `cloud`, and labels it "Usage Commit".

The platform charge has a separate `product_id` and a recurring schedule over the same dates. It uses quarterly frequency, `unit_price: 100000`, quantity `1`, and `amount_distribution: each`, corresponding to the narrative's $1,000 quarterly fee. Usage statements are monthly with `day: contract_start`.

The guide does not state the currency or numeric denomination of `amount` and `unit_price`, define date inclusivity beyond the field names, or provide the complete conditional validation rules for these nested objects. The dedicated create-contract API reference remains the implementation authority for those schemas and constraints.

## Billing-provider configuration after creation

> [!warning] Beta behavior and prerequisite tension
> The page first lists `customer_billing_provider_configuration` as a prerequisite, then says a contract created without `billing_provider_configuration` can receive one later through contract editing. It does not explain whether the prerequisite is limited to the primary workflow or how the customer-level prerequisite relates to the contract-level object in the sample.

The beta edit takes effect at the start of the current billing period. For Stripe, the guide says the current invoice is sent to Stripe at month end. For a marketplace, the entire billing period is metered to that marketplace. A free-trial conversion therefore needs a credit for the free usage to prevent it from being billed.

> [!warning] Marketplace timing boundary
> The separate provider-change guide says transitions to or from a marketplace are next-period only, while this page describes adding a provider to an unconfigured contract at the start of the current period and metering the whole period to a marketplace. The sources do not establish whether initial provider attachment and provider-to-provider transition follow different rules; confirm the intended operation before implementation.

## Scheduled-charge consolidation

The contract can opt to consolidate scheduled invoices, including commit charges, onto usage invoices. Consolidation requires both of the following:

1. The exclusive last day of the usage service period falls on the same day as the scheduled invoice date.
2. The corresponding usage invoice has not finalized.

Metronome evaluates this at contract creation and after later contract changes. This reevaluation does not establish that the consolidation setting itself is editable; the create-contract API reference separately documents that the setting cannot be changed after creation.

In the guide's no-end-date example, a package carries a $75 monthly scheduled charge and a $100 monthly commit from January 1. With `scheduled_charges_on_usage_invoices: ALL`, the January 1 invoice is issued and finalized with the $75 charge. The February draft contains the next $75 scheduled charge plus January usage, and later invoices follow that second pattern if the contract remains unchanged.

## Discounts and rate overrides

Discounts can be supplied during creation or through a later contract edit using credits, rate overrides, tiers, and other terms. For dimensional pricing, the guide requires a price override for every relevant group-key and product combination.

The edit example calls `/v2/contracts/edit` with the customer and contract IDs and adds an override effective 2024-11-01. `entitled: true`, `type: multiplier`, `multiplier: 0.95`, and `applicable_product_tags: ["cloud"]` apply a five-percent discount to the tagged cloud products. The guide does not define precedence when this override overlaps another override; the dedicated editing/API references must resolve that behavior.

## Multiple contracts and usage filters

A customer can have several concurrent contracts with distinct rate cards, start and end dates, discounts, and other terms. Those contracts can draw down shared customer-level credits and commits. A per-contract usage filter determines which usage is assigned to which contract.

The creation example routes events whose `region` property equals `US` through a contract by setting `usage_filter.group_key: region` and `group_values: ["US"]`. The page then changes that filter through `/v1/contracts/setUsageFilter`, adding `EU` with `starting_at: 2025-01-01T00:00:00.000Z`; this makes EU usage bill through the US contract at US prices from that date.

For a streaming billable metric, the usage-filter key must already be a group key on the underlying metric. If dimensional-pricing and presentation keys are also used, all of those properties and the usage-filter key must be present in a compound metric group key. For a SQL billable metric, the usage-filter group key must exist as a property value on the underlying events, such as `properties.region`.

The guide does not define precedence for overlapping filters, behavior when usage matches no contract or multiple contracts, backdating limits, validation errors, or retry and idempotency behavior for `setUsageFilter`.

## Custom fields

Custom fields can attach metadata to a contract or commit for downstream workflows such as revenue recognition. The example proposes `salesforce_opportunity_id` to connect a Metronome contract and its revenue to an SFDC opportunity. This page does not define the custom-field schema, value limits, synchronization mechanism, or whether the mapping is enforced.

## Related

- Company: [[metronome]]
- Concepts: [[metronome-customers-and-contracts]], [[metronome-products-and-rate-cards]], [[metronome-credits-and-commits]], [[metronome-invoicing]], [[metronome-billable-metrics]]
- Related sources: [[source-metronome-api-reference-contracts-create-a-contract]], [[source-metronome-api-reference-contracts-amend-a-contract]], [[source-metronome-guides-customers-billing-manage-customers-schedule-billing-provider-change]], [[source-metronome-guides-pricing-packaging-apply-credits-and-commits-create-a-pre-paid-commit]]

## Raw Sources

- [[raw/metronome/guides/implement-metronome/core-concepts/provision-contract-2026-07-13|2026-07-13 snapshot — contract prerequisites, provisioning, consolidation, overrides, usage filters, and custom fields]]
