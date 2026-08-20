---
title: "Metronome Contract Edits and Overrides"
type: source
date_ingested: 2026-08-19
original_format: webpage
canonical_url: "https://docs.metronome.com/guides/pricing-packaging/make-pricing-changes/edit-or-override-a-contract.md"
raw_files:
  - "metronome/guides/pricing-packaging/make-pricing-changes/edit-or-override-a-contract-2026-07-13.md"
tags: [metronome, contracts, rate-overrides, entitlements, dimensional-pricing]
---

## Overview

This guide explains how contract-level overrides change rate-card defaults for an individual customer or cohort. It covers three rate-override models, entitlement overrides, simple and compound targeting, effective-dated discounts, dimensional and presentation-group examples, quantity tiers, and override priority. Despite the page title, it does not document a contract-edit operation or compare edits with overrides; every request example shown uses the contract-create endpoint.

## Override models and propagation

Metronome applies overrides to usage, subscription, and composite products. A multiplier scales the rate-card rate and therefore changes its effective price when the list rate changes. An overwrite assigns a flat or tiered product rate that remains fixed when the rate-card list price changes. A tiered override applies multipliers to specified quantity ranges and is available only when the contract uses explicit override prioritization.

Contract overrides can also enable a product whose rate-card entitlement is disabled. Once enabled, usage for that product appears on the customer's invoices. This establishes billing and invoice behavior, not application-level access control or authorization.

## Targeting rules

For simple selection, an override can target a `product_id` or products carrying any tag in `applicable_product_tags`. For compound selection, `override_specifiers` accepts an array of specifiers combining product IDs, product tags, pricing-group values, and presentation-group values. Fields inside one specifier are ANDed; satisfying any specifier in the array targets the line item, giving OR behavior across specifiers. The guide's examples use this distinction to express either-tag versus both-tags targeting.

A time-bounded promotion supplies `starting_at` and `ending_before`. Tag targeting also creates propagation behavior: adding a relevant tag to a newly created product causes the matching discount to apply automatically. The guide does not define whether either timestamp is inclusive, how tag changes to existing products propagate, or how retroactive windows affect already generated invoices.

## Dimensional and presentation-group examples

Pricing-group targeting can discount selected dimensional rates without discounting every rate for the product. One multiplier example supplies only `resource.region`, and the guide says those supplied values can be a subset of the product's pricing-group keys, so the discount applies regardless of the omitted `resource.hardware` value. Presentation-group values can also target resource combinations that are used for invoice presentation rather than customer-wide rate differentiation; the example combines `cluster_id` and `resource_id`.

> [!warning] Dimensional targeting scope ambiguity
> An earlier info box says that dimensional pricing must use the product ID, optionally with pricing-group values, and must specify all pricing-group values needed to apply the override. A later multiplier example expressly permits a subset of the product's pricing-group keys. Because the earlier statement immediately follows a prohibition on using product tags for overwrite overrides, it may be overwrite-specific, but the page does not explicitly settle that scope. Verify the applicable override type and rate dimensions before relying on partial dimensional selectors.

The page separately states that product tags cannot target overwrite overrides. Its dimensional example uses product IDs in `override_specifiers`, while its presentation-group example combines a product ID with both presentation values. It does not provide request-schema requiredness, selector-exclusivity rules, unmatched-dimension behavior, or validation errors.

## Quantity tiers and prioritization

A tiered example applies a 20% list-rate discount to the first ten uses in a billing period and a 30% discount to the next ten. The guide does not define behavior above the listed tiers, tier gaps or overlaps, boundary inclusivity, validation, or whether a missing terminal tier falls back to list price.

Only one applicable override is selected for a usage-invoice line item; overrides do not stack. An overwrite always takes precedence over multiplier or tiered overrides, and the last-added overwrite wins when several overwrites apply. Multiplier selection can use either the lowest multiplier, which grants the largest discount, or explicit numeric priority, where the lowest priority value wins. Although tiered overrides require explicit prioritization, this page's final priority list describes multiplier selection and does not separately explain how several applicable tiered overrides are ordered.

## Contract-edit and operational boundaries

All worked requests call `POST /v1/contracts/create`. The page does not identify an endpoint or action for adding, changing, ending, or removing an override on an existing contract, and it does not establish whether the same payload shapes are accepted by `editContract`. It also leaves undocumented edit-history recording, idempotency, concurrency, atomicity, permissions, error responses, retry behavior, backdating, and effects on draft, finalized, or voided invoices.

The guide defines precedence for applicable overrides but not the timing semantics of "last-added" when requests are concurrent or backdated. It also does not explain whether an overwrite remains fixed across currency or pricing-unit changes, what happens when a targeted product or tag is archived or edited, or whether entitlement changes affect anything beyond rated usage appearing on invoices.

## Related

- Company: [[metronome]]
- Concepts: [[metronome-products-and-rate-cards]], [[metronome-customers-and-contracts]]
- Related sources: [[source-metronome-guides-implement-metronome-core-concepts-create-manage-rate-cards]], [[source-metronome-guides-implement-metronome-core-concepts-create-products-contracts]], [[source-metronome-api-reference-contracts-create-a-contract]], [[source-metronome-api-reference-contracts-amend-a-contract]], [[source-metronome-api-reference-contracts-get-contract-edit-history]]

## Raw Sources

- [[raw/metronome/guides/pricing-packaging/make-pricing-changes/edit-or-override-a-contract-2026-07-13|2026-07-13 snapshot - override types, targeting, examples, and priority rules]]
