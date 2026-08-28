---
title: "Metronome Create Products"
type: source
date_ingested: 2026-08-28
original_format: webpage
canonical_url: "https://docs.metronome.com/guides/implement-metronome/core-concepts/create-products-contracts"
raw_files:
  - "metronome/guides/implement-metronome/core-concepts/create-products-contracts-2026-08-28.md"
  - "metronome/guides/implement-metronome/core-concepts/create-products-contracts-2026-07-13.md"
tags: [metronome, products, rate-cards, contracts, pricing, invoices]
---

## Overview

This guide defines Metronome products as catalog objects analogous to SKUs or ERP items. Products connect offerings to charge mechanics and invoice presentation, while billable metrics, rate cards, and contracts supply the metering and pricing context.

## Query-critical facts

- Metronome documents four product types: usage, composite, subscription, and fixed. Usage products vary with reported usage; subscription products carry scheduled recurring fees; fixed products support scheduled charges, commits, and credits.
- Products determine how a customer is charged and how charges appear on invoices, but do not hold the price itself. Usage, composite, and subscription prices are set on a rate card and may be modified on a contract; fixed-product prices are set on a contract.
- Each usage product attaches to one previously created billable metric, while one metric can support multiple products. Product-side pricing and presentation group keys must already exist on that metric.
- Composite products apply a percentage charge to selected products. Applicable products can be selected by product ID or product tag, and configuration can include spend from nested composite products.
- Products can be edited while active in customer billing. Usage-product edits are effective-dated through `Starting at`: a future timestamp schedules a change and a past timestamp applies it retroactively from that time. Product type cannot be changed; correcting it requires a replacement product and archival of the original.
- Pricing group keys select dimension-specific rate-card prices, while presentation group keys group invoice line items. The guide warns that high-cardinality combinations can increase API latency.

## Actors, relationships, and lifecycle

A merchant defines products in the Metronome app, connects usage products to billable metrics, and assigns prices downstream through rate cards or contracts. Product names and presentation configuration affect generated invoice lines. Tags can carry internal catalog identifiers and select products for composite charges, commits, or discounts.

The current guide adds a dedicated composite-product creation flow: choose whether nested composite spend is included, then select applicable products or tags. It also narrows the documented editable-field list to usage products; the guide does not establish the editable fields or effective-dating behavior for composite, subscription, or fixed products.

## Material boundaries and conflicts

- The guide does not define composite recursion, cycle handling, percentage-calculation order, overlapping ID/tag selection, or historical replay when nested composite spend is enabled.
- Retroactive usage-product edits are documented, but recalculation, draft-versus-finalized invoice effects, and propagation to existing commits, credits, discounts, or scheduled charges remain unspecified.
- The guide says Metronome supports four product types, while existing product read/list API sources expose a fifth `PRO_SERVICE` enum value. The sources do not establish whether that value is creatable, API-only, feature-gated, or legacy; see [[metronome-products-and-rate-cards]].
- The high-cardinality note directs customers to the Metronome support portal for configuration discussion; it is not a documented hard limit or latency guarantee.

## Raw-detail coverage map

| Detail category | Exact evidence route |
| --- | --- |
| Product definitions, type purposes, and price ownership | [[raw/metronome/guides/implement-metronome/core-concepts/create-products-contracts-2026-08-28|latest raw snapshot]] |
| Usage and composite app creation steps, tags, conversions, and rounding | [[raw/metronome/guides/implement-metronome/core-concepts/create-products-contracts-2026-08-28|latest raw snapshot]] |
| Effective-dated usage-product edits and immutable product type | [[raw/metronome/guides/implement-metronome/core-concepts/create-products-contracts-2026-08-28|latest raw snapshot]] |
| Pricing-key rate example, presentation-key invoice example, and cardinality warning | [[raw/metronome/guides/implement-metronome/core-concepts/create-products-contracts-2026-08-28|latest raw snapshot]] |
| Prior wording before composite nesting and creation-flow clarification | [[raw/metronome/guides/implement-metronome/core-concepts/create-products-contracts-2026-07-13|2026-07-13 raw snapshot]] |

## Related

- Company: [[metronome]]
- Primary concepts: [[metronome-products-and-rate-cards]], [[metronome-billable-metrics]], [[metronome-customers-and-contracts]]
- Related source: [[source-metronome-guides-implement-metronome-core-concepts-create-billable-metrics]]

## Raw Sources

- [[raw/metronome/guides/implement-metronome/core-concepts/create-products-contracts-2026-08-28|2026-08-28 snapshot — product roles, composite selection and nesting, creation flows, effective-dated edits, tags, and group keys]]
- [[raw/metronome/guides/implement-metronome/core-concepts/create-products-contracts-2026-07-13|2026-07-13 snapshot — earlier product types, creation, effective-dated edits, tags, and group-key guidance]]
