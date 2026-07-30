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

This guide describes Metronome rate cards as the centralized store for standard product pricing and future price changes. It covers product prerequisites, UI and API creation, aliases, one-currency cards, flat-rate examples, metadata edits, scheduled changes, dimensional pricing, and tiered pricing. It is a configuration guide rather than a complete rate-card API schema or lifecycle specification.

## Key takeaways

- Rate cards hold reusable standard prices for products, while customer contracts reference that pricing and can apply customer-specific overrides.
- Products must exist before they can be added to a rate card. Each rate card has one fiat currency, with USD as the documented default.
- A rate card can have effective-dated aliases that replace Metronome-generated IDs in contract-provisioning API calls and allow an integration to switch the underlying card without changing its identifier.
- The API examples add entitled `FLAT` rates to the same product for different pricing-group values and schedule future price changes by adding rates with a later `starting_at`.
- After creation, the documented metadata-edit surface covers name, description, aliases, and adding newly rated products; existing price changes use the same add-rates endpoint as initial rate creation.
- Dimensional pricing changes the relationship from one product/one rate to one product/many rates by assigning prices to pricing-group-key combinations rather than creating duplicate products.
- Tiered pricing varies the applicable rate with billing-period usage. Minimum boundaries are exclusive, maximum boundaries are inclusive, presentation-group values receive tiers independently, and invoices show each tier as a separate line item.

## Pricing role and prerequisites

Metronome describes a rate card as the pricing source of truth on which contracts are built. The card represents standard rates; customer-specific terms can be modeled through contract overrides. The guide's AI example says separate PayGo and enterprise offerings can use distinct rate cards, or one standard card can be retained while enterprise contracts receive overrides.

A rate card depends on products that already exist in Metronome. In the app, creation collects an internal name, optional description, optional aliases, selected products, one fiat currency, and each product's rates, default entitlement, and effective dates. The source says the default currency is USD but does not state whether currency can be changed after creation or how rates in other currency denominations are encoded.

## Creation and identifiers

The app workflow is **Offering → Rate cards → Add new rate card**. An alias can be used instead of a generated rate-card ID when provisioning a contract through the API. The API create example gives each alias a `starting_at` and `ending_before`, demonstrating time-bounded names and a handoff from one alias interval to the next.

The page does not define alias uniqueness, whether alias intervals may overlap, how lookup is resolved at an interval boundary, whether aliases are reusable after removal, or whether a contract retains the resolved card ID after provisioning.

API creation uses `POST /v1/contract-pricing/rate-cards/create`. Rates are added separately with the documented `POST /v1/contract-pricing/rate-cards/addRates` path. The flat-rate example adds two entitled rates for one product, both starting at the same time, with prices selected by the `region` and `cloud` entries in `pricing_group_values`.

## Rate forms documented here

### Flat rates

The API examples use `rate_type: "FLAT"`, a numeric `price`, an `entitled` Boolean, a product ID, an effective start, and optional pricing-group values. The source does not define price denomination, numeric precision, negative or zero-price validation, the behavior of `entitled: false`, or whether the shown fields are the full request schema.

### Tiered rates

Tiered pricing is a usage-based model in which the rate depends on quantity used so far in the billing period. Tiers can be defined on the rate card or introduced as a contract override; a contract override can change boundaries or prices for one customer.

The minimum of each tier is exclusive and its maximum is inclusive. In the example, usage 1–5 is free, usage 6–10 costs $1 per use, and usage 11 and above costs $1.50 per use. For a product with presentation group keys, Metronome says one tier configuration is automatically applied separately to each presentation-group value. Invoice charges are grouped by tier, and each tier appears as a separate invoice line item.

The final API instruction uses `"rate_type": "tiered"` but does not provide the tier request body, supported tier count, boundary validation, empty-tier behavior, or how usage is allocated when tiers have gaps or overlaps.

## Effective timing and edit lifecycle

After creation, the guide distinguishes metadata edits from rate changes. Metadata edits can change the card's name or description, add or remove aliases, and rate new products. They are available through the card's app page or `POST /v1/contract-pricing/rate-cards/update`.

Rate changes are scheduled with the same add-rates endpoint used for initial rates. The example adds new rates for the same product and pricing-group combinations with a `starting_at` one year after the initial rates. This demonstrates future scheduling but does not define whether a later rate automatically ends an earlier one, what occurs when effective intervals overlap, whether backdated changes are allowed, which invoice states can be recalculated, or whether changes are atomic across the submitted `rates` array.

The guide does not document removing or archiving a card, product, or rate; editing an existing rate in place; changing card currency; contract grandfathering; audit history; concurrency; idempotency; or the effect of a card change on draft, finalized, or voided invoices.

## Dimensional pricing

Dimensional pricing lets one product carry rates that vary by cost-driving properties such as cloud provider, region, service type, or model type. The guide describes the object relationship as:

- Traditional: one billable metric → one product → one rate.
- Dimensional: one billable metric → one product → many rates.

The infrastructure example retains three products—reads, writes, and data storage—while varying price over three cloud providers, four zones, three classifications, and two availability-zone counts. Multiplying those values yields 216 possible product-and-dimension combinations. This is an example of possible distinct rates, not a stated minimum, maximum, or requirement to populate every combination.

The app workflow requires pricing group keys on the products, defines possible values for each dimension, and assigns rates to key combinations. The dedicated product and billable-metric guides establish that these product keys originate from group keys on the underlying metric; this rate-card page does not restate that upstream creation constraint. It also does not define wildcard or default rates, missing-combination behavior, validation of unknown group values, maximum dimensions or combinations, or precedence when several rates could match.

## Documentation tensions and unknowns

> [!warning] Endpoint and enum inconsistency
> Initial rates, scheduled changes, and dimensional prices point to `/contract-pricing/rate-cards/addRates`, while the final tiered-pricing instruction names `/contract-pricing/rate-cards/addRate`. The examples also use uppercase `"FLAT"` and lowercase `"tiered"`. The page does not explain whether the singular path or casing differences are valid aliases or documentation defects; confirm the current API reference before implementation.

> [!warning] Contract relationship tension
> This guide says all Metronome contracts are built on rate cards. The separately ingested create-contract API says only `customer_id` and `starting_at` are unconditionally required and presents package or rate-card selection as optional. The documentation does not reconcile whether a default, package-resolved, or implicit card satisfies the categorical statement, so do not infer that every create-contract request must contain a rate-card identifier.

The page uses “overrides” for flexible pricing by custom dimensions near its opening and later for customer-specific tier changes on contracts. It does not establish whether those are the same stored object or separate rate-card and contract mechanisms. No numeric limits, permissions, error responses, retry rules, deletion behavior, alias constraints, rate-overlap rules, dimensional fallback rules, or invoice-recalculation guarantees are supplied.

## Related

- Company: [[metronome]]
- Concepts: [[metronome-products-and-rate-cards]], [[metronome-billable-metrics]], [[metronome-customers-and-contracts]], [[metronome-usage-based-billing]]
- Related sources: [[source-metronome-guides-get-started-developer-sdks]], [[source-metronome-guides-get-started-metronome-dashboard-quickstart]], [[source-metronome-guides-implement-metronome-core-concepts-create-billable-metrics]], [[source-metronome-api-reference-contracts-create-a-contract]]

## Raw Sources

- [[raw/metronome/guides/implement-metronome/core-concepts/create-manage-rate-cards-2026-07-13|2026-07-13 snapshot — rate-card creation, lifecycle, dimensional pricing, and tiered pricing]]
