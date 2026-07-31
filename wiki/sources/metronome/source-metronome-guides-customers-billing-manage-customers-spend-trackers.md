---
title: "Spend trackers"
type: source
date_ingested: 2026-07-31
canonical_url: "https://docs.metronome.com/guides/customers-billing/manage-customers/spend-trackers"
original_format: webpage
raw_files:
  - "metronome/guides/customers-billing/manage-customers/spend-trackers-2026-07-13.md"
tags: [metronome, spend-trackers, contracts, commits, prepaid-balance-thresholds, discounts, public-beta]
---

## Overview

Metronome spend trackers accumulate selected contract spend over a reset period so another contract configuration or a merchant application can make a spend-based decision. In the documented public-beta scope, the only eligible spend type is commit purchases; the tracker can distinguish manual from threshold-recharge commits and optionally select purchases marked as discounted.

## Key takeaways

- Spend trackers are in Public Beta, can change before general availability, and require access through a Metronome representative.
- A tracker can be configured during package creation, contract creation, or contract edit, and returns the sum of matching charges for its reset period.
- `applicable_spend_specifiers` currently support only `COMMIT_PURCHASE`, with source selection for manual and/or threshold-recharge commits and an optional discounted-status filter.
- A prepaid-balance threshold discount can reference a tracker alias and cap. After qualifying spend reaches the cap, new threshold commits receive no discount until the next billing period.
- The contract query returns `accumulated_spend` with an amount and current-period boundaries. For pricing rules that are not wired to a contract configuration, the merchant must query the tracker and enforce the rule itself.

## Public-beta scope

The guide labels spend trackers Public Beta, warns that breaking changes can occur before general availability, and directs customers to a Metronome representative for access. The create-contract API's broader feature-gating caution remains relevant: the presence of spend-tracker fields in documentation does not establish availability for every account.

## Tracker definition and eligible spend

A contract tracker has an alias, credit type, reset frequency, and one or more applicable-spend specifiers. The guide says it can be set during package creation, contract creation, or contract edit. It does not define the corresponding package or edit API requests, mutation semantics, or the complete set of reset-frequency values.

The documented specifier fields are:

- `spend_type`: only commit purchases are currently eligible.
- `sources`: select manual commits, threshold-billing commits, or both.
- `discounted`: optionally select whether purchases marked discounted count. Manual commits use `spend_tracker_attributes.count_as_discounted`; threshold-billing commits use `discount_config`.

This scope is purchase spend, not customer usage-event volume, rated usage, invoice totals, balance consumption, or a general ledger. The page does not define when a commit purchase begins counting or how pending, payment-gated, failed, voided, canceled, refunded, or reversed purchases affect the total.

## Threshold-discount cap

The example creates a `promo-cap` tracker that resets each billing period and includes discounted manual and threshold-recharge commit purchases. A prepaid-balance threshold's `discount_config.cap` points to that tracker alias with an amount. When the cap is reached, subsequent threshold commits are not discounted until the next billing period.

The guide does not define the cap amount's unit or scaling, equality versus crossing behavior, concurrency handling around the cap, or whether previously discounted purchases can later be removed from accumulated spend. Its example uses `fraction: 0.90`; the related threshold guide already records that the documentation does not explicitly resolve whether this is a retained-price fraction or a discount fraction.

## Retrieval and merchant-owned enforcement

The guide says querying the contract returns current-period `accumulated_spend`, including `amount`, `period_starting_at`, and `period_ending_before`, alongside the tracker definition. It does not state calculation freshness, consistency, pagination, historical-period retrieval, or a standalone tracker endpoint. The shown `v2/contracts/get` curl body contains a response-shaped `data` object, so it should not be treated as an authoritative request schema without the dedicated API reference.

A tracker can directly drive a configuration that supports it, such as the threshold-billing discount cap. For a separate internal pricing rule, the guide makes enforcement merchant-owned: its payment-gated-commit example tells the user to check the tracker before issuing the commit. The page does not document a spend-tracker alert, webhook, customer-facing display component, automatic denial of manual commits, or product-access action.

## Documentation boundaries

Spend trackers aggregate selected commit-purchase spend for a defined reset period. This source does not establish a general customer-usage metric, an alert state machine, invoice or payment state, balance availability, revenue recognition, or payment success. It also leaves alias uniqueness, edit and backfill behavior, period reset timing, time zones, late-arriving or backdated purchases, multi-currency conversion, credit-type compatibility, threshold-cap atomicity, and error behavior unspecified.

## Related

- Company: [[metronome]]
- Concepts: [[metronome-spend-trackers]], [[metronome-credits-and-commits]], [[metronome-customers-and-contracts]], [[metronome-alerts-and-notifications]]
- Related sources: [[source-metronome-guides-customers-billing-optimize-customer-experience-prepaid-balance-thresholds]], [[source-metronome-api-reference-contracts-create-a-contract]], [[source-metronome-guides-pricing-packaging-apply-credits-and-commits-manual-payment-gated-commits]]

## Raw Sources

- [[raw/metronome/guides/customers-billing/manage-customers/spend-trackers-2026-07-13|2026-07-13 snapshot — spend-tracker scope, threshold-discount cap, retrieval, and enforcement boundary]]
