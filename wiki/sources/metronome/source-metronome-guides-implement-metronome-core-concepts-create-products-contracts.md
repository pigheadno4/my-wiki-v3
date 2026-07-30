---
title: "Metronome Create Products"
type: source
date_ingested: 2026-07-30
original_format: webpage
canonical_url: "https://docs.metronome.com/guides/implement-metronome/core-concepts/create-products-contracts"
raw_files:
  - "metronome/guides/implement-metronome/core-concepts/create-products-contracts-2026-07-13.md"
tags: [metronome, products, rate-cards, contracts, pricing, invoices]
---

## Overview

This guide defines Metronome products as catalog objects analogous to SKUs or ERP items and explains how they connect billable metrics, invoice presentation, rate cards, and contracts. It covers four product types, the app-based creation sequence, effective-dated edits, tags, dimensional pricing, invoice grouping, and a high-cardinality API-latency caution.

## Key takeaways

- Products determine how a customer is charged and how charges appear as invoice line items, but they do not themselves hold prices.
- Usage, composite, and subscription product prices are defined on rate cards and can be modified on contracts; fixed-product prices are set on contracts.
- Usage products require a previously configured billable metric. One usage product is associated with one metric, while the same metric can support multiple products.
- Product edits use a `Starting at` effective time and can be scheduled for the future or applied retroactively from a past time, even while the product is active in customer billing.
- Product type cannot be changed. Correcting the type requires a replacement product and archival of the original.
- Pricing group keys select dimension-specific rate-card prices, while presentation group keys group invoice line items; both must originate on the underlying billable metric.

## Products in the commercial model

A product represents one service or offering, such as Reads, Writes, Storage, or an individual AI model. It controls the charging shape and invoice presentation: a product or product grouping becomes an invoice line item. Price ownership remains downstream. Usage, composite, and subscription prices live on a rate card and can be modified on a customer contract; fixed-product prices are set on a contract.

This page therefore establishes a product-to-rate-card-to-contract boundary but does not document how to create or edit either rate cards or contracts. It also does not define how a contract resolves a missing rate, how contract changes interact with product effective dates, or which object takes precedence when several applicable prices exist.

## Product types

- **Usage:** varies with reported customer usage for the billing period. The billable metric must be created first. Each product uses one billable metric, but one metric can be reused by multiple products.
- **Composite:** applies a percentage charge to a group of applicable products.
- **Subscription:** charges a recurring fee on a schedule, including seat, platform, and other recurring-fee models.
- **Fixed:** supports scheduled charges, commits, and credits.

The source names these purposes but does not define composite applicability, percentage calculation order, subscription schedule rules, or the contract fields and lifecycle needed to price fixed products.

## Creation sequence

In the Metronome app, product creation proceeds through Offering → Products → **+ Add new product**:

1. Name the product; the name appears on customer invoices.
2. Optionally add product tags and select the product type.
3. For a usage product, select its previously configured billable metric.
4. Optionally add pricing and presentation group keys. These are usage-product fields and can use only group keys already defined on the underlying metric.
5. Optionally multiply or divide usage-product quantity by a conversion factor.
6. Optionally round usage-product quantity up, down, or half up to a chosen number of decimal places.
7. Save the product, then configure price downstream on a rate card or contract as appropriate for its type.

The guide documents the app workflow but does not provide the product API request schema, validation errors, required-name limits, tag limits, conversion-factor constraints, rounding precision limits, or creation idempotency.

## Product edit lifecycle

Products remain editable while actively used for customer billing. Every change is scheduled at a `Starting at` time: a future value schedules the change, while a past value applies it retroactively from that time. Editable fields are name, tags, billable metric, quantity conversion, rounding, and pricing or presentation group keys; the group-key fields are editable only through the API.

Product type is immutable. A product created with the wrong type must be replaced with a correctly typed product and the original archived. The page does not define whether archival is immediate or effective-dated, how replacement references are migrated, whether archived products remain visible on historical invoices, or how retroactive edits affect draft versus finalized invoices, previously calculated usage, commits, credits, discounts, or scheduled charges.

## Tags and selection

One product can carry multiple tags. Consistent tags make products easier to select when constructing a composite product or adding products to a commit or discount. Tags can also store an internal product code or similar company identifier to keep Metronome aligned with internal systems.

The source does not state that tags are unique, immutable, indexed, or validated against an external catalog, and it does not define selection behavior when tags change retroactively.

## Pricing and presentation group keys

Both group-key types depend on group keys defined on the usage product's billable metric. Pricing group keys encode variables such as `region` and `cloud_provider`; the rate card then holds a distinct rate for each applicable key-value permutation. The guide's example keeps two products while encoding eight rates across two regions and two cloud providers. It states that Metronome does not restrict the number of pricing group keys used to define pricing.

Presentation group keys organize invoice line items by a property without making that property the pricing dimension. In the example, `region` selects price while `org` groups the displayed usage, allowing regional quantities for each product to be shown per organization. A property can be both a pricing and presentation group key.

> [!warning] High-cardinality configuration
> Multiple pricing and presentation group keys with many possible values for one customer can increase Metronome API latency. When the possible-value cardinality may reach one thousand, the guide directs users to contact a Metronome representative. This is a consultation threshold, not a documented hard limit; the page supplies no latency target, enforcement behavior, or maximum cardinality.

## Documentation boundaries

- “Products don't have prices” means price values are stored on rate cards or contracts; it does not mean products are unrelated to pricing, because product configuration determines charge mechanics and dimensional rate selection.
- The guide does not describe product identifiers, API endpoints, permissions, audit history, deletion behavior, concurrency, or retry semantics.
- Retroactive product edits are documented, but their recalculation and invoice-state effects are not.
- Unlimited pricing-group-key count does not remove the separate value-cardinality latency warning.
- The page does not document contract creation, rate-card management, or the full lifecycle of composite, subscription, and fixed charges.

## Related

- Company: [[metronome]]
- Concepts: [[metronome-products-and-rate-cards]], [[metronome-billable-metrics]], [[metronome-customers-and-contracts]]
- Related source: [[source-metronome-guides-implement-metronome-core-concepts-create-billable-metrics]]

## Raw Sources

- [[raw/metronome/guides/implement-metronome/core-concepts/create-products-contracts-2026-07-13|2026-07-13 snapshot — product types, creation, effective-dated edits, tags, and group keys]]
