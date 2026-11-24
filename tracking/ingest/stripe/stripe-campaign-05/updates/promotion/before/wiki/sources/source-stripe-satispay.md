---
title: "Stripe: Satispay Payments"
type: source
date_ingested: 2026-05-08
original_format: webpage
raw_files:
  - "stripe-satispay-2025.md"
tags: [stripe, wallets, satispay, italy, eur, disputes, refunds, connect]
---

## Summary

Overview of Satispay, an Italy-focused stored-value digital wallet available through Stripe. Covers payment flow, disputes, refunds, Connect support, prohibited categories, and supported currencies.

## Key Details

**Italy customers only**, EUR only. Redirect to Satispay website for authentication. Immediate confirmation (customer-initiated).

**20 eurozone business countries**: AT, BE, CY, DE, EE, ES, FI, FR, GR, HR, IE, IT, LT, LU, LV, MT, NL, PT, SI, SK.

**Product support**: Connect, Payment Links, Checkout, Elements (Express Checkout Element not supported), Subscriptions.

**No recurring payments.**

**Manual capture**: Yes.

## Disputes

12-day evidence submission window. Customers can dispute for suspected fraud, double payments, or order/amount mismatch. Evidence types: tracking ID, shipping date, purchase records (IP/email for digital, phone/receipt for physical), refund records. Respond via Dashboard or API.

## Refunds

Full and partial. 180-day window. Async, up to 5 minutes. Failed refunds return to Stripe balance — merchant must arrange alternative refund.

Webhooks: `refund.updated` (success) or `refund.failed`.

## Connect

Capability: `satispay_payments`. Statement descriptor rules by charge type:

| Charge type | Descriptor from |
| --- | --- |
| Direct | Connected account |
| Destination | Platform |
| Separate charge and transfer | Platform |
| Destination (with `on_behalf_of`) | Connected account |
| Separate charge and transfer (with `on_behalf_of`) | Connected account |

## Prohibited Categories

14 categories: automobile associations, betting/casino gambling, counseling services, credit reporting agencies, detective agencies, direct marketing (catalog + outbound telemarketing), door-to-door sales, employment/temp agencies, financial institutions, cryptocurrency exchanges and wallets, pawn shops, security brokers/dealers, plus additional at Satispay's discretion.

## Raw Sources

- [[stripe-satispay-2025]] — verbatim overview page (185 lines); 1 CDN video downloaded
