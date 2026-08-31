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
- Composite products apply a percentage charge over applicable products selected by product ID or product tag, and configuration can optionally include spend from nested composite products; subscription products charge recurring fees; and fixed products support scheduled charges, commits, and credits. The guide does not define composite recursion, cycle handling, percentage-calculation order, overlapping-selector behavior, whether nested-composite inclusion or selectors can be edited after creation, or historical replay.
- Products determine charge mechanics and invoice presentation, but price ownership remains downstream: usage, composite, and subscription prices live on rate cards and can be modified on contracts; fixed-product prices live on contracts.
- `presentation_group_key` can group invoice line items by an event-property value.
- Pricing and presentation group keys on a product must be a subset of the underlying metric's group keys; both can be used together.
- When both presentation and pricing dimensions are required, the metric must define one compound group key containing every property used by either product key.
- `quantity_conversion` can multiply or divide displayed quantities, such as converting individual tokens to millions of tokens.
- A rounding conversion can change display granularity, such as rounding seconds to minutes.
- Products remain editable while actively used for customer billing, and product changes generally use a `Starting at` effective time that may be future-scheduled or retroactive. The guide expressly enumerates name, tags, billable metric, quantity conversion, rounding, and API-only group-key edits only for usage products; it does not enumerate editable fields for composite, subscription, or fixed products. Product type is immutable, so correcting it requires a replacement product and archival of the original.
- Product tags can also store internal catalog identifiers and select products for composites, commits, and discounts.


- On usage invoices, pricing group keys produce a separate line item for each priced group-key combination, but the guide says a combination without usage does not produce a line item. Presentation group keys instead organize usage-product lines under a property such as project or organization. The guide does not define missing-key behavior, ordering, cardinality limits, fallback pricing, or label stability after edits. [[source-metronome-guides-implement-metronome-core-concepts-how-invoicing-works]]

Bearer-secured `POST /v1/contract-pricing/products/get` reads one product using a UUID required inside the JSON payload schema, although the enclosing OpenAPI `requestBody` is not marked required. HTTP `200` requires `data`; the product requires UUID `id`, `type`, `initial`, `current`, and an `updates` array. Both state objects require `name`, `created_at`, and `created_by`, while each update requires only `created_at` and `created_by`. State `billable_metric_id` is an unformatted string, whereas the update field is UUID-formatted. The five-value response enum includes `PRO_SERVICE`, whose behavior this endpoint does not define. Optional nullable `archived_at` and optional custom fields sit beside the required history surfaces. The description promises all metadata and historical changes, but the page defines no history ordering, completeness, version identity, archive-event representation, archived-product retrieval rule, freshness, or read-after-write guarantee.

The single-product read can expose optional UUID-array `composite_product_ids` and string-array `composite_tags`. Its state-only, feature-annotated `composite_scope` selects `CUSTOMER` or `CONTRACT` and is described as determining contributing spend. In the 2026-08-28 Get snapshot, `include_composite_spend` appears on state and update without the earlier feature or SDK-skip annotations; it remains explicitly composite-only, defaults false, and permits spend from other composite products when true. This source-scoped annotation change does not prove general tenant availability or create/edit acceptance and must not be generalized to the separately documented List operation. For usage products, nullable quantity conversion requires a numeric factor and an enumerated multiply/divide operation when present; nullable rounding requires an enumerated method and numeric decimal places of at least zero. Pricing- and presentation-group-key string arrays select pricing per key value and group invoice usage lines respectively, and their combined value superset must be configured as one compound billable-metric group key. [[source-metronome-api-reference-products-get-a-product]]

Archiving a billable metric creates an asymmetric Product boundary: the metric can no longer define metering for a new Product, but the archive endpoint says a Product already associated with it continues to function and meter from the archived definition. Separately, the create-products-contracts guide establishes that usage-product billable-metric edits can use `Starting at` effective dating. The archive page does not require the metric to be unused, expose affected Product IDs, define whether a future-effective Product update selecting the metric counts as new use, or specify ordering against concurrent Product creation, update, or metric reassignment. Its HTTP `200` requires top-level `data` referencing a generic `Id` schema whose required UUID `id` example repeats the request UUID, but the schema does not label that value as metric-resource or archive-operation identity. The sparse result does not prove Product-state, rating, invoice, report, export, or downstream propagation. The existing-Product claim also remains unresolved against the dedicated Get-metric source's statement that archived metrics stop processing new usage events. [[source-metronome-api-reference-billable-metrics-archive-a-billable-metric]] [[source-metronome-api-reference-billable-metrics-get-a-billable-metric]] [[source-metronome-guides-implement-metronome-core-concepts-create-products-contracts]]

## Product catalog retrieval API

Bearer-authenticated `POST /v1/contract-pricing/products/list` returns a cursor-paginated organization-wide catalog and excludes archived products by default unless `archive_filter` selects `ARCHIVED` or `ALL`. Optional query `limit` is `1` to `100`; HTTP `200` requires `data` plus nullable `next_page`. Every product item requires UUID `id`, enum `type`, `initial`, `current`, and `updates`; the state objects require `name`, `created_at`, and `created_by`, while update entries require only `created_at` and `created_by`. The endpoint says the list returns complete version history, but defines no update ordering, retention horizon, future-scheduled-entry semantics, current-state selection, omitted-field inheritance, cursor lifetime, snapshot or cross-page consistency, default page size, non-200 response, or read-after-write guarantee.

In the 2026-08-28 List snapshot, `include_composite_spend` appears on both initial/current state and update entries without the earlier feature and SDK-skip annotations; it remains explicitly composite-only and defaults false. `composite_scope` remains state-only, selects `CUSTOMER` or `CONTRACT`, and retains its feature and SDK-skip annotations. This List-specific schema drift does not establish general tenant availability or create/edit acceptance and must not be generalized to the separate Get or mutation schemas. [[source-metronome-api-reference-products-list-products]]

> [!warning] Product-type contradiction
> The list schema adds `PRO_SERVICE` to `USAGE`, `SUBSCRIPTION`, `COMPOSITE`, and `FIXED`, while the product guide enumerates only four types. The sources do not establish whether `PRO_SERVICE` is newly supported, API-only, feature-gated, legacy, or creatable; preserve the mismatch and verify current creation support. [[source-metronome-api-reference-products-list-products]]




## Rate cards and rates

In private preview, a managed AI rate card for [[metronome-token-billing]] creates selected-model billable metrics, products, and rates from configured markups and automatically adds newly released models at the default markup. Provider-driven repricing for changed underlying rates is only described as coming soon; update timing, effective dating, removal, fallback, rounding, and reconciliation remain undocumented. [[source-metronome-guides-pricing-packaging-billing-model-guides-token-billing]]

The deprecated Plan-detail read can expose minimum and overage-rate configuration. Minimum entries require a value, credit type, and `start_period`; overage entries require `to_fiat_conversion_factor`, fiat and source credit types, and `start_period`. The shared `start_period` description counts billing periods before the charge applies. This read does not establish current Contract pricing, product-rate selection, precedence, denomination, calculation, invoice outcome, or migration behavior. [[source-metronome-api-reference-plans-get-plan-details]]

The contract rate-schedule read combines rate-card scheduled changes with contract overrides at an optional effective timestamp and returns only entitled rates. Each returned segment identifies its rate card and product and requires a list rate; optional fields can expose an override rate or commit rate. The endpoint does not define ordering, cross-page consistency, overlap precedence, freshness, or whether the returned surfaces equal a final invoice amount. [[source-metronome-api-reference-contracts-get-the-rate-schedule-for-a-contract]]

`POST /v1/contract-pricing/rate-cards/archive` permanently disables a rate card for new contracts, removes it from contract-creation workflows, and preserves pricing for existing contracts. The endpoint page does not define whether preservation uses a snapshot or retained reference, how later catalog changes interact with those contracts, visibility outside creation workflows, restoration, propagation timing, in-flight contract creation, idempotency, or concurrency. [[source-metronome-api-reference-rate-cards-archive-a-rate-card]]

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

Metronome frames pricing launches at three scopes: rate-card changes for all customers, packages for selected new-customer cohorts, and contract edits or re-provisioning for individual customers. The all-customer guide uses `POST /v1/contract-pricing/rate-cards/addRates` with an array of effective-dated, entitlement-bearing product rates. Package rates layer on top of rate-card changes, and package customers inherit most rate-card changes; a package overwrite override is the stated exception and follows the separate override rules. The page does not enumerate what `most` excludes beyond overwrite overrides or define precedence for other overlapping package, rate-card, and contract changes.

> [!warning] Pricing-change example contradiction
> The launch guide says its single `addRates` call schedules a price increase after one year, but both rates use the same `starting_at` timestamp and differ by region as well as price. The payload therefore shows simultaneous dimension-specific rates, not the described future increase. Do not infer a missing later date, intended region relationship, or automatic ending of the earlier rate.

For a non-monotonically increasing metric, each rate applies only to the incremental usage in that rate's effective window. A negative increment after a rate change is priced at the current effective rate rather than the original rate; the guide's drop of 10 after a move from $3 to $4 produces a `-$40` charge. It warns that a rate increase can therefore make the per-unit credit for a decrease larger than the original per-unit charge. The page does not define overlap precedence, window boundaries, retroactive changes, late corrections, rounding, or finalized-invoice recalculation.

The Salesforce sync exposes a rate-card custom object containing Metronome rate-card ID, name, description, and environment. Contract replicas reference the rate card. Invoice-line replicas identify the product and can be connected through many-to-many association objects to pricing-dimension key/value records; parallel association objects connect lines to presentation or invoicing-group key/value records. The guide does not define product or rate versioning, archive handling, dimension cardinality, ordering, missing-key behavior, or whether Salesforce receives historical versus current catalog state.



Packages let one rate card support multiple standardized pricing plans by adding reusable, time-relative contract terms and package-level rate overrides. Package creation requires an existing product and rate card, but this guide does not define precedence with later rate-card changes or already-provisioned contract state. [[source-metronome-guides-implement-metronome-core-concepts-packages-overview]]

A zero-overage guide uses a zero product list rate as the post-commit fallback and places the real price either in a rate-card `commit_rate` for inherited pricing or in a contract commit-specific overwrite for per-customer pricing. A contract commit-specific override takes precedence over the default rate-card commit rate. The pattern is illustrative and does not define missing-rate behavior, multiple-balance resolution, concurrency at exhaustion, or complete add-rate and override schemas.

## Enterprise design

Metronome's ASC 606 guide uses product and rate-card structures, tags or custom fields, charge-level reporting, consistent identifiers, historical raw amounts, and pricing or discount detail as inputs for obligation mapping, standalone-selling-price analysis, and downstream allocation. A SKU is not automatically a distinct performance obligation: the customer owns that determination and the mapping. Metronome supplies granular data but does not perform SSP allocation or reallocation and does not establish variable-consideration, foreign-exchange, material-right, or other accounting policy. [[source-metronome-guides-reporting-insights-financial-reporting-asc-606-revenue-recognition]]

Customer-commit creation requires UUID `product_id` for the fixed product used to invoice the commit amount even when eligible usage is unrestricted. Eligible usage can be selected through product IDs, product tags, or `specifiers`; omitting all three applies the commit to all products, and `specifiers` cannot be combined with either direct selector. The page does not define whether both direct selectors may coexist, empty-array behavior, missing-dimension matching, duplicate selectors, or validation of unknown enclosing fields. [[source-metronome-api-reference-credits-and-commits-create-a-commit]]

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

Contract overrides apply to usage, subscription, and composite products. Multipliers continue to track rate-card list-price changes, overwrites remain fixed when the list price changes, and tiered multipliers apply to quantity ranges only under explicit override prioritization. Overrides can also enable a product's entitlement; once enabled, usage for that product appears on customer invoices. This does not establish application authorization or access control.

Simple contract-override targeting uses product IDs or product tags. Compound `override_specifiers` combine fields with AND semantics inside one specifier and OR semantics across the specifier array. Only one override is selected for a usage-invoice line item: overwrites outrank multiplier and tiered overrides, the last-added applicable overwrite wins, and multiplier selection uses either the lowest multiplier or the lowest explicit priority value. The guide does not define concurrent or backdated meaning for last-added, edit atomicity, or ordering among several applicable tiered overrides.

> [!warning] Documentation ambiguity
> The Stripe Tax guide creates `stripe_product_id` on Metronome's `Product` entity but maps it from `ContractProduct`. The page does not reconcile those labels.

> [!warning] Rate-card documentation inconsistencies
> The guide alternates between `/addRates` and `/addRate`, and between `"FLAT"` and `"tiered"` casing. It also says all contracts are built on rate cards while the create-contract schema makes package or rate-card selection optional. Confirm current API behavior rather than inferring endpoint aliases, enum normalization, or an implicit card.

> [!warning] Dimensional override scope ambiguity
> The contract-override guide says dimensional pricing must use a product ID and specify all pricing-group values needed to apply the override, but a later multiplier example permits a subset of the product's pricing-group keys and lets omitted hardware values match. The first statement follows an overwrite-specific tag prohibition and may itself be overwrite-specific, but the page does not explicitly settle that scope.

> [!warning] AI worked-example inconsistency
> The `Metronome-Industries/ai` catalog reference calls `SUBSCRIPTION` rate type deprecated and uses `FLAT` with `billing_frequency`, while its PLG worked example uses `rate_type: "SUBSCRIPTION"` with a nested `subscription_rate`. Treat both as agent examples and verify the dedicated rate-card schema. [[source-github-ai]]

> [!info] Retroactive edit boundary
> The product guide permits retroactive effective dates but does not explain recalculation, draft-versus-finalized invoice effects, historical visibility after archival, or how existing commits, credits, discounts, and scheduled charges follow the change.

The customer-credit create payload requires a UUID `product_id` even when eligible usage is unrestricted. The `applicable_product_ids` and `applicable_product_tags` descriptions say omitting both direct selectors makes the credit apply to all products. However, the same payload permits `specifiers` only when those direct selectors are absent and says at least one specifier condition must match; it does not reconcile whether `specifiers` override that all-products wording. Within a specifier, all listed product tags must match, and pricing or presentation group-value maps accept arbitrary string-valued keys. The exclusion array makes a specifier inapplicable when usage matches its inclusion criteria and any exclusion entry; within one exclusion entry, all listed product tags must match. The page does not say whether direct IDs and tags may coexist with each other, how empty arrays behave, how missing dimensions are evaluated, or how duplicates and unknown enclosing-object fields are validated.

## Subscription and payment-gate extensions

- Subscription offerings use one product per offering, with quantity-one list pricing on a rate card. Separate billing frequencies can use distinct rates; when several subscription rates exist, the guide recommends defaulting them to `false` and enabling the applicable rate or rates on the contract without defining exclusivity or resolution.
- Subscription-rate changes reach inheriting contracts in the next billing period, while contract overwrites retain their assigned price. The lifecycle source says one subscription rate applies per billing period.
- The PayGo example tags selected-plan products `premium` and uses a tag-scoped `entitled: false` override for its Basic package. This is invoice/package configuration, not proof of application authorization.
- A manual Stripe-gated commit requires the commit product to carry `stripe_product_id` mapped to `invoiceitem.price`; a missing mapping prevents the invoice line and payment. The existing Product-versus-ContractProduct terminology warning still applies.
- Trial packaging can use `entitled: false` for merchant-enforced feature restriction or a time-bounded multiplier `0` for uncapped free usage, after which list pricing resumes. Overlapping-override precedence, missing-rate behavior, and automatic product gating remain unknown.

## Sources

- [[source-metronome-guides-pricing-packaging-apply-credits-and-commits-guarantee-zero-overages]] - zero-list-rate fallback, inherited rate-card commit pricing, per-contract commit-specific overwrite pricing, and override precedence
- [[source-metronome-guides-reporting-insights-financial-reporting-asc-606-revenue-recognition]] - SKU and obligation mapping, pricing and discount inputs, historical SSP evidence, downstream allocation support, and accounting-decision boundary

- [[source-metronome-integrations-invoice-integrations-stripe]] — required `stripe_product_id` mapping for every product used by a payment-gated commit and the documented line-item, payment-failure, and commit-void consequence when it is absent

- [[source-metronome-guides-get-started-api-quickstart]] — product and shared-rate-card roles in first-invoice onboarding, dimensional group-key dependencies, and missing-rate diagnostic

- [[source-metronome-api-reference-rate-cards-archive-a-rate-card]] — permanent new-contract disablement, preserved existing-contract pricing, and archive request/response boundaries

- [[source-metronome-guides-pricing-packaging-make-pricing-changes-make-a-pricing-change]] — all-customer rate additions, package inheritance boundary, and the future-change worked-example contradiction
- [[source-metronome-guides-pricing-packaging-make-pricing-changes-edit-or-override-a-contract]] — contract override models, entitlements, selector logic, dimensional-targeting ambiguity, and precedence

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

- [[source-metronome-api-reference-credits-and-commits-create-a-credit]] - required credit product, direct product applicability, specifier matching, and selector-validation boundaries


- [[source-metronome-guides-implement-metronome-core-concepts-how-invoicing-works]] — pricing-group line creation, presentation grouping, and invoice field boundaries

- [[source-metronome-api-reference-products-get-a-product]] - single-product POST read, required identity and state/history envelope, five-value type enum, state-versus-update schema distinctions, composite selectors, configuration-dependent integration fields, usage conversions, and compound group-key constraint

- [[source-metronome-api-reference-products-list-products]] — product catalog listing that excludes archived products by default, pagination, state and update shapes, optional configuration, and the `PRO_SERVICE` type contradiction

- [[source-metronome-guides-implement-metronome-core-concepts-non-monotonically-increasing-metrics]] - effective-window rating of non-monotonic increments, current-rate pricing of negative quantities, and larger-credit warning

- [[source-metronome-integrations-platform-integrations-sfdc-integration]] - Salesforce rate-card replica, contract lookup, invoice-line product attribution, pricing-dimension and invoicing-group association objects, and catalog-state unknowns





- [[source-metronome-integrations-invoice-integrations-netsuite]] - many-to-one Metronome product to NetSuite item mapping through product custom fields and a separate Commit Application item for zero-dollar consumption invoices

- [[source-metronome-api-reference-sdks]] — SDK product-to-metric presentation, quantity conversion, reusable rate-card pricing, entitlement, flat and tiered rate forms, and effective-date walkthrough

## Related

- [[metronome-billable-metrics]]
- [[metronome-customers-and-contracts]]
- [[metronome-usage-based-billing]]
- [[metronome-credits-and-commits]]
- [[metronome-subscriptions]]
