---
title: "Metronome Create and Manage Rate Cards"
type: source
date_ingested: 2026-07-30
original_format: webpage
canonical_url: "https://docs.metronome.com/guides/implement-metronome/core-concepts/create-manage-rate-cards"
raw_files:
  - "metronome/guides/implement-metronome/core-concepts/create-manage-rate-cards-2026-07-13.md"
tags: [metronome, rate-cards, pricing, dimensional-pricing, tiered-pricing, contracts]
---

## Overview

Rate cards centralize standard product pricing and future price changes. This guide covers product prerequisites, UI and API creation, aliases, one-currency cards, flat rates, metadata edits, scheduled changes, dimensional pricing, and tiered pricing. It is not a complete API schema or lifecycle specification.

## Card creation and identifiers

Products must exist before they are added to a card. App creation collects an internal name, optional description and aliases, selected products, one fiat currency, and rates, default entitlements, and effective dates. USD is the documented default; currency mutation and non-USD denomination are not defined.

Aliases can replace generated card IDs in contract-provisioning calls. The API example gives aliases `starting_at` and `ending_before`, demonstrating a time-bounded handoff. It does not define uniqueness, overlap resolution, boundary lookup, reuse after removal, or whether a contract retains the resolved ID.

The page uses `POST /v1/contract-pricing/rate-cards/create`, then adds rates through `/addRates`. Flat examples apply entitled `FLAT` rates to one product for different `region` and `cloud` combinations. Price denomination, precision, validation, `entitled: false`, and complete request requiredness are outside this page.

## Metadata and rate changes

Metadata edits can change name and description, add or remove aliases, and rate new products. Existing price changes instead use the add-rates endpoint with a later `starting_at`. This demonstrates future scheduling but not whether later rates end earlier ones, overlap handling, backdating, invoice recalculation, or atomicity across a rates array.

Removal or archival, editing a rate in place, currency changes, contract grandfathering, audit history, concurrency, idempotency, and effects on draft, finalized, or voided invoices are undocumented.

## Dimensional pricing

Dimensional pricing changes the object relationship from one metric → one product → one rate to one metric → one product → many rates. Prices are assigned to pricing-group-key combinations rather than duplicating products.

The example combines three products, three clouds, four zones, three classifications, and two availability-zone counts for 216 possible combinations. This is an illustration, not a minimum, maximum, or requirement to populate every combination.

Product pricing keys originate from group keys on the underlying metric. The page does not define wildcard/default rates, unmatched combinations, unknown group values, maximum dimensions or combinations, or precedence if several rates match.

## Tiered pricing

Tiered rates depend on quantity used in the billing period. Tiers can be placed on a card or applied as customer-specific contract overrides that change boundaries or prices.

Minimum boundaries are exclusive and maximum boundaries inclusive. The example makes uses 1–5 free, 6–10 cost $1 each, and 11+ cost $1.50. A single tier configuration applies independently to each presentation-group value, and invoices show each tier as a separate line item.

The page provides no tier request body, tier-count limit, boundary validation, empty-tier behavior, or gap/overlap allocation rules.

## Documentation tensions

> [!warning] Endpoint and enum inconsistency
> Initial and scheduled rates use `/addRates`, while the final tier instruction names `/addRate`. Examples use uppercase `"FLAT"` and lowercase `"tiered"`. The page does not establish whether these are valid aliases or documentation defects.

> [!warning] Contract relationship tension
> This guide says all contracts are built on rate cards, while the create-contract API requires only customer and start time at the top level and treats package or rate-card selection as optional. The sources do not explain whether a default, package-resolved, or implicit card satisfies the categorical statement.

The word “overrides” is used both for custom-dimension pricing and customer contract changes without establishing whether these are the same stored object.

## Related

- Company: [[metronome]]
- Concepts: [[metronome-products-and-rate-cards]], [[metronome-billable-metrics]], [[metronome-customers-and-contracts]], [[metronome-usage-based-billing]]
- Related sources: [[source-metronome-guides-implement-metronome-core-concepts-create-products-contracts]], [[source-metronome-guides-implement-metronome-core-concepts-create-billable-metrics]], [[source-metronome-api-reference-contracts-create-a-contract]]

## Raw Sources

- [[raw/metronome/guides/implement-metronome/core-concepts/create-manage-rate-cards-2026-07-13|2026-07-13 snapshot — card creation, effective changes, dimensional pricing, and tiers]]
