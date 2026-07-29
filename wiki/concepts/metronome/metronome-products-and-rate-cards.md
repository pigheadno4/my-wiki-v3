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
- A usage product can reference a billable metric.
- `presentation_group_key` can group invoice line items by an event-property value.
- Pricing and presentation group keys on a product must be a subset of the underlying metric's group keys; both can be used together.
- `quantity_conversion` can multiply or divide displayed quantities, such as converting individual tokens to millions of tokens.
- A rounding conversion can change display granularity, such as rounding seconds to minutes.

## Rate cards and rates

- `entitled` controls whether a rate appears on customer invoices by default; a non-entitled rate requires a contract-level override.
- The guide lists flat and tiered rates.
- USD prices are expressed in cents, while the guide says other currencies use whole units and points to its currency-denomination guide for details.
- `starting_at` and `ending_before` establish effective periods so rates can evolve over time.
- A rate card uses one fiat currency. The dashboard guide recommends a shared standard rate card, with contract-level overrides for customer-specific prices.
- Rate-card options include dimensional values, volume tiers, custom pricing-unit conversions, commit-specific rates, and date-effective rate changes.

## Enterprise design

- Product tags can group products that are priced, discounted, or packaged similarly, allowing contract overrides to target a group instead of enumerating product IDs.
- Every invoice charge is associated with a product, including one-time charges and upfront payments for prepaid commitments; the guide models these as fixed products.
- Every credit or commit is associated with a fixed product for invoice-line and reporting attribution; eligible usage can be restricted separately by product IDs, product tags, or specifiers.
- Product custom fields can retain ERP SKU identifiers for reconciliation and revenue-recognition mapping.
- A commit edit can target usage through direct product IDs or tags, or through pricing and presentation-group specifiers, but the direct selectors and `specifiers` cannot be combined.
- A commit's `rate_type` can switch current and future invoices between list-rate and commit-rate behavior; finalized invoices must be voided and regenerated to reflect the change.
- Stripe Tax mapping stores a Stripe product ID in `stripe_product_id`; Metronome products can share one Stripe product only when they share a tax code, so the field must not enforce uniqueness.

> [!warning] Documentation ambiguity
> The Stripe Tax guide creates `stripe_product_id` on Metronome's `Product` entity but maps it from `ContractProduct`. The page does not reconcile those labels.

## Sources

- [[source-metronome-guides-get-started-developer-sdks]] — introductory product, quantity-conversion, rate-card, and effective-date workflow
- [[source-metronome-guides-pricing-packaging-billing-model-guides-enterprise-commit]] — product tags, fixed-charge products, and finance mappings
- [[source-metronome-guides-get-started-metronome-dashboard-quickstart]] — group-key constraints, conversions, and dashboard rate-card workflow
- [[source-metronome-guides-pricing-packaging-apply-credits-and-commits-create-a-pre-paid-commit]] — fixed-product attribution and balance applicability
- [[source-metronome-api-reference-credits-and-commits-edit-a-commit]] — selector exclusivity and commit rate-type updates
- [[source-metronome-integrations-tax-integrations-stripe-tax]] — Stripe product and tax-code mapping

## Related

- [[metronome-billable-metrics]]
- [[metronome-customers-and-contracts]]
- [[metronome-usage-based-billing]]
- [[metronome-credits-and-commits]]
