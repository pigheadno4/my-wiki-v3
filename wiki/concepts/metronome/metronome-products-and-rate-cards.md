---
title: "Metronome Products and Rate Cards"
type: concept
category: technology
tags: [metronome, products, rate-cards, pricing]
---

## Definition

In the SDK guide's pricing flow, a product supplies invoice presentation and connects a billable metric to a chargeable catalog item. A rate card supplies the product's price and can be reused across a product catalog; a customer contract then applies the rate card.

## Products

- The guide lists usage, fixed, composite, and subscription product types.
- Usage products vary with reported usage and each references exactly one previously created billable metric; one metric can support multiple products.
- Composite products apply a percentage charge over applicable products, subscription products charge recurring fees, and fixed products support scheduled charges, commits, and credits.
- Products determine charge mechanics and invoice presentation, but price ownership remains downstream: usage, composite, and subscription prices live on rate cards and can be modified on contracts; fixed-product prices live on contracts.
- `presentation_group_key` can group invoice line items by an event-property value.
- Pricing and presentation group keys on a product must be a subset of the underlying metric's group keys; both can be used together.
- When both presentation and pricing dimensions are required, the metric must define one compound group key containing every property used by either product key.
- `quantity_conversion` can multiply or divide displayed quantities, such as converting individual tokens to millions of tokens.
- A rounding conversion can change display granularity, such as rounding seconds to minutes.
- Product edits are effective-dated and can start in the future or apply retroactively from a past `Starting at` value. Name, tags, metric, conversion, rounding, and API-only group-key fields are editable while billing is active, but product type is immutable; correcting it requires a replacement product and archival of the original.
- Product tags can also store internal catalog identifiers and select products for composites, commits, and discounts.

## Rate cards and rates

- The currency guide enumerates 18 fiat currencies and defines Metronome-specific API scaling: USD uses cents, while every other listed fiat currency uses whole units. One rate card carries one fiat currency; a product rate can use that currency or a custom pricing unit with a conversion from the underlying fiat currency. After a product rate is saved in one pricing unit, that rate's unit cannot be changed. The guide does not define replacement, effective-dating, contract migration, precision, rounding, or invoice-recalculation behavior.

- Card creation accepts a name, optional description and effective-dated aliases, selected products, one fiat currency, and product rates, entitlements, and effective dates. Aliases can stand in for generated IDs during contract provisioning, but uniqueness, overlap, boundary lookup, and reuse are undocumented.
- Metadata edits cover name, description, aliases, and newly rated products. Price changes instead add a future-effective rate; the guide does not define overlap, automatic ending, backdating, deletion, currency changes, grandfathering, or invoice recalculation.
- `entitled` controls whether a rate appears on customer invoices by default; a non-entitled rate requires a contract-level override.
- The guide lists flat and tiered rates.
- USD prices are expressed in cents, while the guide says other currencies use whole units and points to its currency-denomination guide for details.
- `starting_at` and `ending_before` establish effective periods so rates can evolve over time.
- The architecture guide describes rate cards as reusable default pricing that flows into multiple customer commercial models. Contract-specific discounts and per-unit overrides remain a separate layer; the guide does not establish precedence, grandfathering, or rollout timing when shared rates change.
- A rate card uses one fiat currency. The dashboard guide recommends a shared standard rate card, with contract-level overrides for customer-specific prices.
- Rate-card options include dimensional values, volume tiers, custom pricing-unit conversions, commit-specific rates, and date-effective rate changes.
- Dimensional pricing maps one metric and one product to many rates selected by group-key combinations. The guide's 216-combination example is illustrative, not a platform limit; fallback, missing-combination, and multi-match precedence are undocumented.
- Tier minimums are exclusive and maximums inclusive. One tier configuration applies independently per presentation-group value, and each tier appears as its own invoice line. Tier-count, validation, gap, and overlap behavior remain undocumented.
- Prepaid thresholds can be denominated in a custom pricing unit. Metronome evaluates the threshold and recharge target in that unit, then uses the customer's rate-card conversion to calculate the fiat payment.
- `@metronome/sdk@3.10.0` adds `add_credit_type_conversions` to the rate-card update type. It can add custom pricing-unit conversions, while the generated docstring says existing conversions cannot be modified through this field. [[source-github-metronome-node]]

## Enterprise design

- Contracts build on a selected rate card but may also carry fixed products outside it. The provisioning guide's cloud-tag example adds an entitled `0.95` multiplier; dimensional pricing requires an override for each relevant group-key and product combination.

- Product tags can group products that are priced, discounted, or packaged similarly, allowing contract overrides to target a group instead of enumerating product IDs.
- Every invoice charge is associated with a product, including one-time charges and upfront payments for prepaid commitments; the guide models these as fixed products.
- The deprecated Plans `addCharge` endpoint adds a narrower legacy rule: its `charge_id` must be on a product outside the current plan, and that product must have only fixed charges. The caller supplies numeric `price` and `quantity`; the price must match the target invoice's currency, with USD cents given only as an example. The page does not establish non-USD denomination, positivity, precision, rounding, rate-card precedence, catalog-price validation, or how the restriction maps to Contracts, so it must not be generalized into current Contract pricing behavior.
- Every credit or commit is associated with a fixed product for invoice-line and reporting attribution; eligible usage can be restricted separately by product IDs, product tags, or specifiers.
- Product custom fields can retain ERP SKU identifiers for reconciliation and revenue-recognition mapping.
- A commit edit can target usage through direct product IDs or tags, or through pricing and presentation-group specifiers, but the direct selectors and `specifiers` cannot be combined.
- A commit's `rate_type` can switch current and future invoices between list-rate and commit-rate behavior; finalized invoices must be voided and regenerated to reflect the change.
- Legacy contract amendments can add overwrite, multiplier, or tiered rate overrides. Overwrites take precedence; explicit tiered and multiplier priority uses the lowest number first. Product IDs or tags cannot be combined with override specifiers, and a configured percentage minimum prevents commit-specific overrides from applying.
- Stripe Tax mapping stores a Stripe product ID in `stripe_product_id`; Metronome products can share one Stripe product only when they share a tax code, so the field must not enforce uniqueness.

> [!warning] Documentation ambiguity
> The Stripe Tax guide creates `stripe_product_id` on Metronome's `Product` entity but maps it from `ContractProduct`. The page does not reconcile those labels.

> [!warning] Rate-card documentation inconsistencies
> The guide alternates between `/addRates` and `/addRate`, and between `"FLAT"` and `"tiered"` casing. It also says all contracts are built on rate cards while the create-contract schema makes package or rate-card selection optional. Confirm current API behavior rather than inferring endpoint aliases, enum normalization, or an implicit card.

> [!warning] AI worked-example inconsistency
> The `Metronome-Industries/ai` catalog reference calls `SUBSCRIPTION` rate type deprecated and uses `FLAT` with `billing_frequency`, while its PLG worked example uses `rate_type: "SUBSCRIPTION"` with a nested `subscription_rate`. Treat both as agent examples and verify the dedicated rate-card schema. [[source-github-ai]]

> [!info] Retroactive edit boundary
> The product guide permits retroactive effective dates but does not explain recalculation, draft-versus-finalized invoice effects, historical visibility after archival, or how existing commits, credits, discounts, and scheduled charges follow the change.

## Subscription and payment-gate extensions

- Subscription offerings use one product per offering, with quantity-one list pricing on a rate card. Separate billing frequencies can use distinct rates; when several subscription rates exist, the guide recommends defaulting them to `false` and enabling the applicable rate or rates on the contract without defining exclusivity or resolution.
- Subscription-rate changes reach inheriting contracts in the next billing period, while contract overwrites retain their assigned price. The lifecycle source says one subscription rate applies per billing period.
- The PayGo example tags selected-plan products `premium` and uses a tag-scoped `entitled: false` override for its Basic package. This is invoice/package configuration, not proof of application authorization.
- A manual Stripe-gated commit requires the commit product to carry `stripe_product_id` mapped to `invoiceitem.price`; a missing mapping prevents the invoice line and payment. The existing Product-versus-ContractProduct terminology warning still applies.
- Trial packaging can use `entitled: false` for merchant-enforced feature restriction or a time-bounded multiplier `0` for uncapped free usage, after which list pricing resumes. Overlapping-override precedence, missing-rate behavior, and automatic product gating remain unknown.

## Sources

- [[source-github-ai]] - agent catalog workflow, setup order, pricing examples, and internal rate-representation conflict
- [[source-github-metronome-node]] - exact `3.10.0` rate-card update type and custom-unit conversion addition

- [[source-metronome-api-reference-invoices-add-a-one-time-charge]] — deprecated Plans fixed-product eligibility and invoice-currency price boundary for one-time charges

- [[source-metronome-guides-pricing-packaging-make-pricing-changes-use-currency-custompricingunits]] — fiat support, API denomination, custom-unit conversion setup, and saved-rate unit immutability

- [[source-metronome-guides-get-started-developer-sdks]] — introductory product, quantity-conversion, rate-card, and effective-date workflow
- [[source-metronome-guides-pricing-packaging-billing-model-guides-enterprise-commit]] — product tags, fixed-charge products, and finance mappings
- [[source-metronome-guides-get-started-metronome-dashboard-quickstart]] — group-key constraints, conversions, and dashboard rate-card workflow
- [[source-metronome-guides-pricing-packaging-apply-credits-and-commits-create-a-pre-paid-commit]] — fixed-product attribution and balance applicability
- [[source-metronome-guides-customers-billing-optimize-customer-experience-prepaid-balance-thresholds]] — custom-unit threshold evaluation and rate-card conversion
- [[source-metronome-api-reference-credits-and-commits-edit-a-commit]] — selector exclusivity and commit rate-type updates
- [[source-metronome-integrations-tax-integrations-stripe-tax]] — Stripe product and tax-code mapping
- [[source-metronome-guides-implement-metronome-core-concepts-create-billable-metrics]] — compound group-key design and metric-to-product pricing flow
- [[source-metronome-api-reference-contracts-amend-a-contract]] — legacy override types, selector exclusivity, priority, and minimum behavior
- [[source-metronome-guides-implement-metronome-core-concepts-create-products-contracts]] — product types, price ownership, creation, effective-dated edits, tags, and group keys
- [[source-metronome-guides-get-started-how-metronome-works]] — reusable pricing layer, presentation controls, and automatic-flow claim
- [[source-metronome-guides-implement-metronome-core-concepts-provision-contract]] — contract layering, tag-scoped multiplier, and dimensional override requirement
- [[source-metronome-guides-implement-metronome-core-concepts-create-manage-rate-cards]] — card creation, aliases, effective changes, dimensional rates, and tiers
- [[source-metronome-guides-pricing-packaging-subscription-subscription-overview]] — subscription products, quantity-one prices, and terminology caution
- [[source-metronome-guides-pricing-packaging-subscription-define-subscription-pricing]] — per-offering setup, flat-rate example, and multi-rate recommendation
- [[source-metronome-guides-pricing-packaging-subscription-manage-subscription-lifecycle]] — inherited price changes, overwrites, and lifecycle wording
- [[source-metronome-guides-pricing-packaging-billing-model-guides-pay-as-you-go]] — plan tags and contract-scoped entitlement override
- [[source-metronome-guides-pricing-packaging-apply-credits-and-commits-manual-payment-gated-commits]] — Stripe product mapping for a payment-gated commit
- [[source-metronome-guides-pricing-packaging-billing-model-guides-create-a-trial]] — time-bounded entitlement and zero-multiplier trial overrides

## Related

- [[metronome-billable-metrics]]
- [[metronome-customers-and-contracts]]
- [[metronome-usage-based-billing]]
- [[metronome-credits-and-commits]]
- [[metronome-subscriptions]]
