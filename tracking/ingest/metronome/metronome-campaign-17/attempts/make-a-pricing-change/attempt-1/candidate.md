---
title: "Metronome Launch New Pricing"
type: source
date_ingested: 2026-08-19
canonical_url: "https://docs.metronome.com/guides/pricing-packaging/make-pricing-changes/make-a-pricing-change.md"
original_format: webpage
raw_files:
  - "metronome/guides/pricing-packaging/make-pricing-changes/make-a-pricing-change-2026-07-13.md"
tags: [metronome, pricing, rate-cards, packages, package-aliases, contracts, grandfathering]
---

## Overview

This guide presents three scopes for launching pricing changes in Metronome: rate-card changes for all customers, packages and package aliases for specific cohorts, and contract changes for individual customers. Its worked examples show entitlement-based grandfathering and time-resolved package aliases, but they are implementation illustrations rather than complete endpoint schemas or lifecycle specifications.

## Key takeaways

- A rate-card `addRates` call can introduce product rates for all customers, including rates selected by pricing-group values.
- To keep existing customers on their contracted pricing while offering a new product to new customers, the guide adds the product to the rate card with `entitled: false`, then creates a package whose override entitles it and provisions new contracts by `package_alias`.
- Package rates layer on top of rate-card changes, so package customers inherit most rate-card changes. An overwrite override is the stated exception and follows the separate standard override rules.
- Reusing a package alias with a later `starting_at` can redirect unchanged provisioning calls to a newly created package while preserving the earlier package's bounded alias schedule for existing customers.
- An individual customer can move by ending and re-provisioning its contract with the new package, or by editing the existing contract with customer-specific overrides.

## All-customer rate-card changes

The page directs callers to `POST /v1/contract-pricing/rate-cards/addRates`, the same endpoint it says creates new rates. The request identifies a rate card and submits a `rates` array containing product ID, effective start, default entitlement, rate type, price, and pricing-group values. The example supplies two flat rates for the same product, one for `us-west-2` on AWS at `100` and one for `us-east-2` on AWS at `120`.

> [!warning] Worked-example scheduling contradiction
> The narrative says the example launches a product and schedules a price increase after one year in a single call, but both submitted rates have the identical `starting_at` value of `2024-01-01T00:00:00.000Z` and differ by region as well as price. The payload therefore demonstrates simultaneous region-specific rates, not a future-effective increase. Do not infer the missing later effective date, the intended region relationship, or automatic termination of an earlier rate.

The page does not define required fields beyond the example, array atomicity, idempotency, overlap resolution, backdating, automatic end dates, failure responses, or effects on draft or finalized invoices. Use the dedicated rate-card API reference for those boundaries.

## Cohort rollout and grandfathering

For a new-customer-only launch, the guide first adds the product to the shared rate card with `entitled: false`. It then creates a package over that rate card with an override scoped by product ID and pricing-group values and sets `entitled: true`. New contracts select the package through `package_alias: "New Customer Pricing"`; the guide says those new customers receive the product while existing customers' contracted pricing remains unchanged.

Package rates are applied on top of rate-card changes, and customers provisioned through a package still inherit most changes made to its rate card. The documented exception is a package overwrite override, for which the separate standard override rules apply. The word "most" is not enumerated here, and the page does not define precedence for other overlapping package, rate-card, or contract changes.

## Package-alias transition

The guide creates a second package with the same `New Customer Pricing` alias and a later `starting_at`. It says Metronome automatically gives the original package an alias schedule ending when the new one begins, and unchanged provisioning calls resolve to the newer package from that date. This supports changing the package selected for future customers without changing provisioning infrastructure while existing customers retain their original package pricing.

The example labels the overwrite change as `$1` to `$1.20` while the payload uses `price: 120`; the request does not identify the rate card's currency on this page. Alias uniqueness, overlapping schedules, exact boundary lookup, timezone handling, reuse after removal, whether already-provisioned contracts retain a resolved package ID, and transition failure behavior remain undocumented.

## Individual-customer changes

For a grandfathered customer that opts into new pricing, the guide gives two routes: end the contract and re-provision it with the new package, or edit the contract directly. It also points to custom contract overrides for negotiated customer-specific pricing. This page does not define termination timing, proration, continuity, amendment history, override precedence, invoice recalculation, or the request schemas for either route.

## Related

- Company: [[metronome]]
- Concepts: [[metronome-products-and-rate-cards]], [[metronome-packages-and-aliases]], [[metronome-customers-and-contracts]]
- Related sources: [[source-metronome-guides-implement-metronome-core-concepts-create-manage-rate-cards]], [[source-metronome-api-reference-contracts-create-a-contract]]

## Raw Sources

- [[raw/metronome/guides/pricing-packaging/make-pricing-changes/make-a-pricing-change-2026-07-13|2026-07-13 snapshot — all-customer, cohort, alias, and individual pricing-change workflows]]
