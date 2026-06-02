---
title: "Accept Przelewy24 Payments"
type: source
date_ingested: 2026-04-14
original_format: webpage
raw_files:
  - "paypal-apm-przelewy24.md"
  - "paypal-apm-przelewy24-js-sdk.md"
  - "paypal-apm-przelewy24-orders-api.md"
tags: [paypal, apm, przelewy24, poland, bank-redirect, local-payment-methods]
---

## Overview

Przelewy24 is Poland's bank redirect payment method — supports both PLN and EUR (unlike BLIK which is PLN only).

Source URL: <https://developer.paypal.com/docs/checkout/apm/przelewy24/>

Last updated: 2025-05-12

## Key Details

| Field | Value |
| --- | --- |
| Countries | Poland (PL) only |
| Currencies | **PLN and EUR** (BLIK supports PLN only) |
| Minimum | 1 PLN |
| Refunds | Within 180 days |
| Flow | Bank redirect |
| Merchant eligibility | Global (excluding Russia, Japan, Brazil) |

## Eligibility Restrictions (same as Bancontact/BLIK/EPS/iDEAL/MyBank)

- No billing agreements, no multiple seller payments, no shipping callbacks
- **No chargebacks**
- **Capture only** — authorization not supported
- **Online only**

## Integration Methods

- JavaScript SDK
- Orders REST API

## JS SDK Integration

Source URL: <https://developer.paypal.com/docs/checkout/apm/przelewy24/js-sdk/>

Last updated: 2025-03-18

### SDK script

```html
<script src="https://www.paypal.com/sdk/js?client-id=CLIENT_ID&components=buttons,payment-fields,marks,funding-eligibility&enable-funding=p24&currency=EUR"></script>
```

**Funding key**: `p24` (not `przelewy24`). Default currency EUR (supports PLN and EUR).

### Payment fields

Collects **first name, last name, and email** — same as BLIK (not name-only like Bancontact/EPS). No dedicated mark image (renders via `paypal.FUNDING.P24` only, same as MyBank).

### Notes

- GitHub sample: `github.com/paypal-examples/p24-paypal-payment-js-sdk`
- createOrder note explicitly mentions PLN/EUR (correctly reflects both supported currencies)

## Orders API Integration

Source URL: <https://developer.paypal.com/docs/checkout/apm/przelewy24/orders-api/>

Last updated: 2025-05-06

Same auto-capture pattern as other APM Orders API guides. `payment_source.p24` with `name` + `email` (email required — unlike Bancontact/EPS which are name-only). `country_code: PL`. `application_context` at root.

## Raw Sources

- [[paypal-apm-przelewy24]] — verbatim overview page
- [[paypal-apm-przelewy24-js-sdk]] — JS SDK integration: `enable-funding=p24&currency=EUR`, name+email fields, no mark image
- [[paypal-apm-przelewy24-orders-api]] — Orders API integration: `payment_source.p24` with name + email (email required); auto-capture, PLN sample

## Relevant Wiki Pages

- [[paypal-apm]] — APM overview with all 11 supported methods
- [[source-paypal-apm-blik]] — BLIK (Poland/PLN only — compare: Przelewy24 also supports EUR)
