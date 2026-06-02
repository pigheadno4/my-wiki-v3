---
title: "Payment Methods Reference"
type: source
date_ingested: 2026-04-14
original_format: webpage
raw_files:
  - "paypal-payment-methods-reference.md"
tags: [paypal, payment-methods, apm, reference, catalog]
---

## Overview

Comprehensive catalog of all PayPal-supported payment methods — digital wallets, cards, APMs, and loans. Last updated May 2025.

Source URL: <https://developer.paypal.com/docs/checkout/payment-methods/>

Last updated: 2025-05-09

## Complete Payment Method Table (18 entries)

| Method | Type | Buyer countries | Refunds |
| --- | --- | --- | --- |
| PayPal | digital wallet | Global | Yes |
| Pay Later | loan | AU/FR/DE/IT/ES/GB/US | Yes |
| PayPal Credit | revolving credit | US/UK | Yes |
| Venmo | digital wallet | US | Yes |
| Amex/Discover/Mastercard/Visa | credit card | PayPal/Expanded Checkout countries | Yes |
| Apple Pay | push | **US only** (per this page) | ≤180 days |
| Bancontact | bank redirect | Belgium | ≤180 days |
| BLIK | bank redirect | Poland | ≤180 days |
| EPS | bank redirect | Austria | ≤180 days |
| Google Pay | **bank redirect** (per this page) | US | ≤180 days |
| iDEAL¹ | bank redirect | Netherlands | ≤180 days |
| MyBank | bank redirect | Italy | ≤180 days |
| Pay upon Invoice | deferred payment | Germany | ≤180 days |
| Przelewy24 | bank redirect | Poland | ≤180 days |
| Trustly | bank redirect | AT/DE/DK/EE/ES/FI/GB/LT/LV/NL/NO/SE | ≤365 days |

**Multibanco not in this table** — notable absence.

## Doc Errors

> [!warning] Two errors vs other sources
> 1. **Google Pay**: listed as "bank redirect" — should be "push" (consistent in all other docs including the APM overview)
> 2. **Apple Pay**: listed as "US only" — Apple Pay integration guide says 34 countries

## iDEAL Footnote (¹)

For iDEAL payments:
- **Cannot use BIC** to identify the bank when creating an order
- Remove `bic` from request parameters (unless returning buyer)
- Remove any hosted pages used for bank selection

## Raw Sources

- [[paypal-payment-methods-reference]] — verbatim reference page

## Relevant Wiki Pages

- [[paypal-apm]] — APM overview
- [[paypal]] — PayPal company overview
