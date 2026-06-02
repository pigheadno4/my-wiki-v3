---
title: "Stripe — Agentic Commerce Suite: Sell Through Agents"
type: source
date_ingested: 2026-05-12
original_format: webpage
raw_files:
  - "stripe-agentic-commerce-for-sellers-2026.md"
tags: [stripe, agentic-commerce, ai-agents, product-catalog, v2-api, webhooks, order-approval-hook, catalog-feed]
---

## Summary

Seller integration guide for Stripe's Agentic Commerce Suite (ACS). Covers catalog feed upload, order fulfillment, optional hooks (order approval, checkout customization), manual capture, and incremental inventory/price updates.

## Catalog Feed Upload (v2 API)

Three feed types: `product` (daily full upload), `inventory` (incremental), `pricing` (incremental). All use `upsert` mode.

```js
stripe.v2.commerce.productCatalog.imports.create({
  feed_type: 'product', // or 'inventory' or 'pricing'
  mode: 'upsert',
})
```

Flow: create import → get presigned URL → `PUT` CSV (max 4 GB) → poll status.

**Import states**: `awaiting_upload` → `processing` → `succeeded` / `succeeded_with_errors` / `failed`

**Error file**: `status_details.succeeded_with_errors.error_file.url` — expires after 5 minutes.

**Feed webhooks** (v2): `v2.commerce.product_catalog.imports.succeeded/succeeded_with_errors/failed` — webhook omits full object; retrieve via `related_object.url`.

## Order Fulfillment

Listen to `checkout.session.completed`. Expand with `Stripe-Version: 2025-12-15.preview` to get line items, taxes, payment details in one call.

SKU available at: `CheckoutSession.LineItems.Data[].price.external_reference`

Batch fulfill via List CheckoutSessions endpoint with `created[gt]` + `status=complete`; use `starting_after` for deduplication.

## Order Approval Hook

Pre-payment webhook to your endpoint; Stripe enforces 4-second timeout. Must be idempotent (agents may retry on 424). Returns `approved` or `declined`. Can optionally set `application_fee_details` for Connect.

## Checkout Customization Hook

Dynamic tax rates and shipping options. Returns `shipping_options[]` and `line_items[]` with tax rates. Same idempotency requirement.

## Manual Capture

Dashboard setting; capture via `POST /v1/payment_intents/:id/capture` with `Stripe-Version: 2025-09-30.preview`.

## Related Pages

- [[stripe-agentic-commerce]] — concept page
- [[agentic-commerce]] — general industry concept

## Raw Sources

- [[stripe-agentic-commerce-for-sellers-2026]] — verbatim ACS seller guide (680 lines)
