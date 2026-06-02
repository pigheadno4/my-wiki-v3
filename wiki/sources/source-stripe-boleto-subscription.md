---
title: "Stripe: Use Boleto with Subscriptions"
type: source
date_ingested: 2026-05-07
original_format: webpage
raw_files:
  - "stripe-boleto-subscription-2025.md"
tags: [stripe, vouchers, boleto, brazil, brl, subscriptions, recurring, send-invoice, charge-automatically, tax-id]
---

## Summary

Guide for using Boleto with subscriptions. Supports both `send_invoice` and `charge_automatically`. Key distinction: `charge_automatically` requires customer's tax ID + Brazilian address set up as default payment method; `send_invoice` has customer re-enter details each cycle.

## Key Details

**Prerequisite**: enable "Send a Stripe-hosted link for customers to confirm payments when required" in Subscriptions & Emails settings.

**Both collection methods supported** (unique among voucher methods):

| | `send_invoice` | `charge_automatically` |
| --- | --- | --- |
| Customer setup | None needed upfront | Requires name, address, tax ID as default PM |
| Per cycle | Customer re-enters details every invoice | Boleto emailed automatically |
| Invoice due date | Required | Not applicable |
| Boleto creation | When customer enters details | When invoice is created |

**`charge_automatically` setup flow**:
1. Create Boleto PaymentMethod with `billing_details` (name, email, Brazilian address) + `boleto.tax_id`
2. Attach PaymentMethod to Customer
3. Set as `invoice_settings.default_payment_method`
4. Create subscription with `collection_method: 'charge_automatically'`, `off_session: true`

**`send_invoice` setup**: subscription with `collection_method: 'send_invoice'`, `payment_method_types: ['card', 'boleto']`, `days_until_due`.

**Checkout Sessions** for subscriptions: `mode: 'subscription'` with `payment_method_options.boleto.expires_after_days`.

## Raw Sources

- [[stripe-boleto-subscription-2025]] — verbatim webpage content (417 lines); fixed `*payment method*` ×1, `*Customers*` ×1, `*subscriptions*` ×2, `*Products*` ×1, `*Prices*` ×1, `*invoices*` ×1, `*sandbox*` ×1
