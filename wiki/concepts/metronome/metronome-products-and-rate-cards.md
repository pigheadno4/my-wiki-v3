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
- `quantity_conversion` can multiply or divide displayed quantities, such as converting individual tokens to millions of tokens.

## Rate cards and rates

- `entitled` controls whether a rate appears on customer invoices by default; a non-entitled rate requires a contract-level override.
- The guide lists flat and tiered rates.
- USD prices are expressed in cents, while the guide says other currencies use whole units and points to its currency-denomination guide for details.
- `starting_at` and `ending_before` establish effective periods so rates can evolve over time.

## Enterprise design

- Product tags can group products that are priced, discounted, or packaged similarly, allowing contract overrides to target a group instead of enumerating product IDs.
- Every invoice charge is associated with a product, including one-time charges and upfront payments for prepaid commitments; the guide models these as fixed products.
- Product custom fields can retain ERP SKU identifiers for reconciliation and revenue-recognition mapping.

## Sources

- [[source-metronome-guides-get-started-developer-sdks]] — introductory product, quantity-conversion, rate-card, and effective-date workflow
- [[source-metronome-guides-pricing-packaging-billing-model-guides-enterprise-commit]] — product tags, fixed-charge products, and finance mappings

## Related

- [[metronome-billable-metrics]]
- [[metronome-customers-and-contracts]]
- [[metronome-usage-based-billing]]
- [[metronome-credits-and-commits]]
