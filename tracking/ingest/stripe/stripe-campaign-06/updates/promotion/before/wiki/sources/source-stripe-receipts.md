---
title: "Stripe — Receipts and Paid Invoices"
type: source
date_ingested: 2026-05-11
original_format: webpage
raw_files:
  - "stripe-receipts-2026.md"
tags: [stripe, receipts, refunds, invoices, connect, payment-links, checkout]
---

## Summary

Stripe receipt mechanics: auto-send, manual send, customization, refund receipts, invoice receipts, test mode behavior, and Connect considerations.

## Key Details

- **Receipt URL**: `Charge.receipt_url` — always reflects latest status; expires in **30 days** (expired links require original email)
- **Not downloadable**: browser-only (except Mexico refund receipts)
- **Auto-send**: Payment Links, Checkout Sessions (hosted/embedded/Elements), advanced integrations
- **Manual send**: Dashboard → Payment details → Receipt history; comma-separated emails; last 10 tracked
- **Refund receipts**: enable in Dashboard → Customer emails settings → Refunds toggle; Mexico: downloadable
- **Invoice/subscription**: itemized (line items, discounts, taxes); Hosted Invoice Page includes download link
- **Test mode**: auto-receipts only for verified account emails; others require manual Dashboard send

## Connect Behavior

| Charge type | Branding source |
| --- | --- |
| Destination + separate charges | Platform account settings |
| Direct charges | Connected account settings |

Pass `receipt_email` to send receipt on behalf of connected account. Standard accounts: configure via Dashboard Branding. Express/Custom: platform sets via `settings.branding` API.

## Related Pages

- [[stripe-payment-intents]] — concept page (receipts accessed via Charge.receipt_url within PaymentIntent flow)
- [[stripe]] — Stripe company page

## Raw Sources

- [[stripe-receipts-2026]] — verbatim receipts guide
