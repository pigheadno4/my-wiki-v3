---
title: "Accept BLIK Payments"
type: source
date_ingested: 2026-04-14
original_format: webpage
raw_files:
  - "paypal-apm-blik.md"
  - "paypal-apm-blik-js-sdk.md"
  - "paypal-apm-blik-orders-api.md"
tags: [paypal, apm, blik, poland, bank-redirect, local-payment-methods]
---

## Overview

BLIK is Poland's bank redirect payment method. Same eligibility structure as Bancontact.

Source URL: <https://developer.paypal.com/docs/checkout/apm/blik/>

Last updated: 2025-05-09

## Key Details

| Field | Value |
| --- | --- |
| Countries | Poland (PL) only |
| Currency | PLN |
| Minimum | 1 PLN |
| Refunds | Within 180 days |
| Flow | Bank redirect |
| Merchant eligibility | Global (excluding Russia, Japan, Brazil) |

## Eligibility Restrictions (same as Bancontact)

- No billing agreements, no multiple seller payments, no shipping callbacks
- **No chargebacks**
- **Capture only** — authorization not supported
- **Online only**

## Integration Methods

- JavaScript SDK
- Orders REST API

## JS SDK Integration

Source URL: <https://developer.paypal.com/docs/checkout/apm/blik/js-sdk/>

Last updated: 2025-04-25

### SDK script

```html
<script src="https://www.paypal.com/sdk/js?client-id=CLIENT_ID&components=buttons,payment-fields,marks,funding-eligibility&enable-funding=blik&currency=PLN"></script>
```

### Payment fields — key difference vs Bancontact

BLIK collects **first name, last name, and email** (Bancontact collects name only).

### Checkout flows

- **Single-page**: fields + button on same page
- **Multi-page**: same pattern as Bancontact; German merchants use for regulatory compliance

### Webhooks (same as Bancontact JS SDK)

`CHECKOUT.ORDER.APPROVED`, `CHECKOUT.PAYMENT-APPROVAL.REVERSED`, `CHECKOUT.ORDER.DECLINED`, `PAYMENT.CAPTURE.PENDING/COMPLETED/DENIED`

### Notes

- Orders must be created in PLN currency
- GitHub sample: `github.com/paypal-examples/blik`

## Orders API Integration

Source URL: <https://developer.paypal.com/docs/checkout/apm/blik/orders-api/>

Last updated: 2025-03-18

Same structure as Bancontact Orders API. Key difference: `payment_source.blik` includes `email` field (optional):

```json
{
  "payment_source": {
    "blik": {
      "country_code": "PL",
      "name": "John Doe",
      "email": "buyer@example.com"
    }
  },
  "processing_instruction": "ORDER_COMPLETE_ON_PAYMENT_APPROVAL",
  "application_context": { "locale": "en-PL", "return_url": "...", "cancel_url": "..." }
}
```

Webhooks: `PAYMENT.CAPTURE.COMPLETED`, `PAYMENT.CAPTURE.DENIED`, `CHECKOUT.ORDER.DECLINED` (with `most_recent_errors`).

## Raw Sources

- [[paypal-apm-blik]] — verbatim overview page
- [[paypal-apm-blik-js-sdk]] — JS SDK integration: `enable-funding=blik&currency=PLN`, name+email fields, single/multi-page flows
- [[paypal-apm-blik-orders-api]] — Orders API integration: same auto-capture pattern as Bancontact; `payment_source.blik` includes optional `email` field

## Relevant Wiki Pages

- [[paypal-apm]] — APM overview
- [[source-paypal-apm-bancontact]] — Bancontact (same structure)
