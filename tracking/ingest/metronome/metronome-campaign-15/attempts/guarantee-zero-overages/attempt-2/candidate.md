---
title: "Guarantee zero overages"
type: source
date_ingested: 2026-08-19
canonical_url: "https://docs.metronome.com/guides/pricing-packaging/apply-credits-and-commits/guarantee-zero-overages.md"
original_format: webpage
raw_files:
  - "metronome/guides/pricing-packaging/apply-credits-and-commits/guarantee-zero-overages-2026-07-13.md"
tags: [metronome, commits, overages, rate-cards, pricing-overrides]
---

## Overview

This guide documents a Metronome pricing pattern for customers who must never be billed beyond a committed balance. It combines a zero-dollar list rate with a real price that applies only during commit drawdown, so usage after exhaustion continues to resolve for billing at zero rather than producing a positive overage charge.

The pattern is intentionally narrower than ordinary prepaid or trial designs. It is a billing guarantee, not a product-access control: merchant applications must still stop or restrict consumption through their own gating workflow.

## Key takeaways

- Set the rate card's list rate to 0 USD, then place the real per-unit price either in a reusable rate-card `commit_rate` or in a commit-specific contract override.
- While an eligible commit has balance, usage draws it down at the real price. When that balance reaches zero, the commit-only pricing ceases and the 0 USD list rate becomes the fallback.
- Rate-card commit pricing suits a shared price inherited by customers on the card. A commit-specific `overwrite` override suits customer-specific pricing; a contract override takes precedence over the card's default commit rate.
- This configuration differs from prepaid balance thresholds, which restore balance through automatic recharge, and spend thresholds, which trigger incremental payment to constrain exposure. Use this pattern only when positive overage billing is unacceptable.
- Zero-overage billing does not reject usage events or stop service consumption. Balance thresholds, webhooks, or another application-owned control remain necessary when access must stop after exhaustion.

## Pricing mechanics

Two layers create the fallback. The usage product's ordinary list rate is 0 USD. A second, balance-dependent price applies only while a commit funds the usage, allowing the commit to burn down at the intended commercial rate without leaving a positive price after exhaustion.

For uniform pricing, the rate-card entry carries both `price: 0` and a `commit_rate`. The commit selects that price with `rate_type: commit_rate`; customers using the rate card inherit the arrangement without a per-contract price override.

For customer-specific pricing, the card keeps only the zero list rate and the contract adds an `overwrite` override with `is_commit_specific: true`. `override_specifiers.commit_ids` limits the override to the named commit, so the override no longer applies after that balance is exhausted. A card-level commit rate can also serve as the default while selected contracts apply a different commit-specific override.

## Use-case and enforcement boundaries

The guide positions the pattern for hard-capped free trials, fraud-sensitive accounts, and strict contractual budgets where even failed application gating must not create an overage bill. Prepaid balance thresholds and spend thresholds address different goals: maintaining funded service through recharge or limiting accrued exposure through incremental payment. They do not replace the zero-list-rate fallback when the requirement is that overages must never be charged.

The fallback changes the billed amount, not whether Metronome accepts usage or whether the underlying product remains available. A merchant that intends exhaustion to stop consumption must evaluate balance state and enforce access in its application, using threshold signals or webhooks as inputs rather than treating the billing configuration itself as an entitlement barrier.

## Documentation cautions

> [!warning] Contradiction
> Both worked payloads set a flat `price` of `100`, while the prose calls that value 100 USD per unit. Existing Metronome source evidence says USD API prices use cents, under which `100` represents 1 USD; see [[source-metronome-guides-get-started-developer-sdks]] and [[source-metronome-guides-pricing-packaging-make-pricing-changes-use-currency-custompricingunits]]. Verify the intended amount against the current API schema before copying either example.

The page demonstrates flat rates only and does not establish whether this zero-overage pattern supports every other rate type, pricing unit, balance combination, or override interaction. It also does not define concurrent exhaustion behavior, invoice recalculation, finalized-invoice correction, alert latency, webhook guarantees, or application-gating implementation.

The existing prepaid-commit and free-trial sources describe uncovered usage returning to ordinary list-price overage or arrears. That is not a platform-wide contradiction: those outcomes depend on a positive list rate, whereas this guide deliberately configures the fallback list rate to zero.

## Related

- Company: [[metronome]]
- Concepts: [[metronome-credits-and-commits]], [[metronome-products-and-rate-cards]], [[metronome-currencies-and-custom-pricing-units]], [[metronome-usage-based-billing]], [[metronome-alerts-and-notifications]]
- Related sources: [[source-metronome-guides-pricing-packaging-apply-credits-and-commits-create-a-pre-paid-commit]], [[source-metronome-guides-pricing-packaging-billing-model-guides-create-a-trial]], [[source-metronome-guides-customers-billing-optimize-customer-experience-prepaid-balance-thresholds]], [[source-metronome-guides-customers-billing-optimize-customer-experience-set-customer-spend-control]], [[source-metronome-guides-get-started-developer-sdks]], [[source-metronome-guides-pricing-packaging-make-pricing-changes-use-currency-custompricingunits]]

## Raw Sources

- [[raw/metronome/guides/pricing-packaging/apply-credits-and-commits/guarantee-zero-overages-2026-07-13|2026-07-13 snapshot — zero-overage rate-card and contract-override patterns]]
