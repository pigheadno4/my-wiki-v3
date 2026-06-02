---
title: "Stripe ACS Catalog Feed"
type: concept
category: technology
tags: [stripe, agentic-commerce, product-feed, catalog, inventory, csv, v2-api]
---

## Overview

The ACS catalog feed is how sellers share structured product, inventory, pricing, and promotion data with Stripe for distribution to AI agents. Data is submitted as CSV via the v2 `ProductCatalogImport` API.

## Four Feed Types

| Feed | Modes | Purpose |
| --- | --- | --- |
| `product` | `upsert` / `replace` | Full catalog (all attributes) |
| `inventory` | `upsert` only | Stock availability + quantity |
| `pricing` | `upsert` only | Price + sale price |
| `promotions` | `upsert` only | Discount rules |

**Replace mode** (product feed only): products absent from file are permanently deleted.

## Processing Rules

- **Deletion**: add `delete=true` column → removes product; only `id` + `delete` are read for that row
- **Discovery-only**: `disable_checkout=true` → product indexed/ranked by agents, but checkout redirects to `link` URL (not in-agent checkout)
- Each row = one product or variant

## Required Product Fields

`id`, `title`, `description`, `link`, `brand` (most), `price`, `availability`, inventory (`inventory_quantity` or `inventory_not_tracked=true`)

## Key Format Patterns

**Shipping**: `country:delivery_area:service:speed_range:price`; supports `per_order`/`per_item` cost basis and free shipping threshold.

**Tax**: `stripe_product_tax_code` OR `third_party_tax_code: anrok:code`; `tax_behavior: inclusive/exclusive`

**Variants**: `item_group_id` groups all variants; `color`, `size`, `gender`, `material`; up to 3 custom option name/value pairs

**Product relationships**: `relationship_type:target_id`; types: `upsell`, `cross_sell`, `substitute`, `accessory`; max 10

**Compliance**: `product_warning` (types: `legal_disclaimer`, `safety_warning`, `prop_65`); `age_restriction`

**Review signals**: `product_review_rating` (1-5) + `product_review_count`; `popularity_score` (0-5); `return_rate` (%)

## Agent-Side SFTP Ingestion

Stripe delivers seller catalogs to agent's SFTP server (port 22, Ed25519 auth). Directory: `/[stripe_profile_id]/catalog/` (daily) + `/updates/` (hourly delta, opt-in). `manifest.json` uploaded last — wait for it before ingesting (signals batch complete). Shards for catalogs > 100k rows.

**Deletion**: explicit (`delete=true`) OR implicit (absent from latest full feed) → remove product. Reappearance in later feed = active.

**Ingestion rules**: idempotent, timestamp-validate, log `batch_timestamp` for auditability.

## Sources

- [[source-stripe-agentic-commerce-product-feed]] — full field reference for all four feeds
- [[source-stripe-agentic-commerce-sftp-catalog]] — agent-side SFTP ingestion: directory structure, manifest pattern, deletion rules, idempotency
