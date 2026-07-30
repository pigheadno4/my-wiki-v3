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

This guide provisions and evolves a customer contract. Contracts build on a rate card and can add product access, commits, discounts, fixed products outside the card, scheduled charges, invoice scheduling, billing-provider routing, and usage filters.

## Prerequisites and worked contract

The documented workflow assumes connected usage events plus an existing billable metric, product, rate card, customer, and `customer_billing_provider_configuration`. These are operational prerequisites for this workflow, not proof that each is an unconditional request field in every create-contract call.

The example selects `rate_card_alias: base_usage_products`, starts on 2024-11-01, and routes directly to AWS Marketplace. It combines a one-year prepaid commit for products tagged `cloud`, a quarterly platform charge, and monthly usage statements anchored to contract start. `amount: 1000000` and the upfront `unit_price: 1000000` match the narrative's $10,000 commit; `unit_price: 100000` matches the $1,000 platform charge.

The page does not state the currency or numeric denomination, complete nested validation rules, or date inclusivity beyond field names. The create-contract API reference remains the schema authority.

## Provider configuration after creation

> [!warning] Beta behavior and prerequisite tension
> The page first lists customer billing-provider configuration as a prerequisite, then says a contract created without `billing_provider_configuration` can receive one later through editing. It does not reconcile the customer-level prerequisite with the contract-level sample field.

The beta edit takes effect at the start of the current billing period. The current Stripe invoice is then sent at month end; for marketplaces, the whole billing period is metered to the marketplace. A free-trial conversion must credit free usage to prevent billing it.

> [!warning] Marketplace timing boundary
> A separate provider-change guide limits marketplace-involved transitions to the next period. This page describes initial attachment to an unconfigured contract at the current period start. The sources do not establish whether attachment and provider-to-provider transition intentionally differ.

## Scheduled-charge consolidation

`scheduled_charges_on_usage_invoices: ALL` can consolidate scheduled and commit charges onto a usage invoice only when the exclusive last day of the usage service period is the same day as the scheduled invoice date and the corresponding usage invoice has not finalized.

Metronome evaluates consolidation at creation and after later contract changes. This does not establish that the setting is editable; the create-contract reference separately says it cannot change after creation.

In the example, a $75 monthly scheduled charge and $100 monthly commit begin January 1. The first invoice finalizes that day with the $75 charge. The February draft contains the next $75 charge plus January usage, and later invoices follow that pattern absent contract changes.

## Discounts and overrides

Discounts can be supplied at creation or later through credits, rate overrides, tiers, and other terms. Dimensional pricing requires an override for every relevant group-key and product combination.

The edit example adds an entitled multiplier override of `0.95`, effective 2024-11-01, to products tagged `cloud`, representing a five-percent discount. The guide does not define precedence among overlapping overrides.

## Multiple contracts and usage filters

A customer can hold concurrent contracts with different rate cards, dates, and discounts while those contracts share customer-level commits and credits. A contract usage filter routes selected usage to one contract.

The creation example selects events with `region: US`. A later `/v1/contracts/setUsageFilter` call adds `EU`, effective 2025-01-01, so EU usage is billed through the US contract at US prices.

- For a streaming metric, the filter key must already be a group key. With dimensional-pricing or presentation keys, all keys must be in one compound metric group key.
- For a SQL metric, the filter key must exist as a property on the underlying events.

The page does not define overlapping-filter precedence, behavior when usage matches zero or multiple contracts, backdating limits, validation errors, or retry and idempotency behavior.

## Custom fields

Contract or commit custom fields can support downstream workflows. The example proposes `salesforce_opportunity_id` to associate Metronome revenue with an SFDC opportunity, but does not define schema, limits, synchronization, or enforcement.

## Related

- Company: [[metronome]]
- Concepts: [[metronome-customers-and-contracts]], [[metronome-products-and-rate-cards]], [[metronome-credits-and-commits]], [[metronome-invoicing]], [[metronome-billable-metrics]]
- Related sources: [[source-metronome-api-reference-contracts-create-a-contract]], [[source-metronome-guides-customers-billing-manage-customers-schedule-billing-provider-change]], [[source-metronome-guides-pricing-packaging-apply-credits-and-commits-create-a-pre-paid-commit]]

## Raw Sources

- [[raw/metronome/guides/implement-metronome/core-concepts/provision-contract-2026-07-13|2026-07-13 snapshot — prerequisites, provisioning, consolidation, overrides, filters, and custom fields]]
