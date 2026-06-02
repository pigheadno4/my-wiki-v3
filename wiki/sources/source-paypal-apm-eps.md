---
title: "Accept EPS Payments"
type: source
date_ingested: 2026-04-14
original_format: webpage
raw_files:
  - "paypal-apm-eps.md"
  - "paypal-apm-eps-js-sdk.md"
  - "paypal-apm-eps-orders-api.md"
tags: [paypal, apm, eps, austria, bank-redirect, local-payment-methods]
---

## Overview

EPS is Austria's bank redirect payment method. Same eligibility structure as Bancontact and BLIK.

Source URL: <https://developer.paypal.com/docs/checkout/apm/eps/>

Last updated: 2025-05-12

## Key Details

| Field | Value |
| --- | --- |
| Countries | Austria (AT) only |
| Currency | EUR |
| Minimum | 1 EUR |
| Refunds | Within 180 days |
| Flow | Bank redirect |
| Merchant eligibility | Global (excluding Russia, Japan, Brazil) |

## Eligibility Restrictions (same as Bancontact/BLIK)

- No billing agreements, no multiple seller payments, no shipping callbacks
- **No chargebacks**
- **Capture only** — authorization not supported
- **Online only**

## Integration Methods

- JavaScript SDK
- Orders REST API

## JS SDK Integration

Source URL: <https://developer.paypal.com/docs/checkout/apm/eps/js-sdk/>

Last updated: 2025-03-28

### SDK script

```html
<script src="https://www.paypal.com/sdk/js?client-id=CLIENT_ID&components=buttons,payment-fields,marks,funding-eligibility&enable-funding=eps&currency=EUR"></script>
```

### Payment fields

Collects **first name and last name only** — same as Bancontact (BLIK also collects email).

### Checkout flows

- **Single-page**: fields + button on same page
- **Multi-page**: same pattern as Bancontact/BLIK; German merchants use for regulatory compliance

### Webhooks (same as Bancontact/BLIK JS SDK)

`CHECKOUT.ORDER.APPROVED`, `CHECKOUT.PAYMENT-APPROVAL.REVERSED`, `CHECKOUT.ORDER.DECLINED`, `PAYMENT.CAPTURE.PENDING/COMPLETED/DENIED`

### Notes

- Orders must be created in EUR currency
- GitHub sample: `github.com/paypal-examples/eps-paypal-payment-js-sdk`

## Orders API Integration

Source URL: <https://developer.paypal.com/docs/checkout/apm/eps/orders-api/>

Last updated: 2025-03-19

Same pattern as Bancontact/BLIK Orders API. `payment_source.eps` with `name` + `country_code: AT` only — no `email` field (same as Bancontact; BLIK has optional email).

```json
{
  "payment_source": {
    "eps": { "country_code": "AT", "name": "John Doe" }
  },
  "processing_instruction": "ORDER_COMPLETE_ON_PAYMENT_APPROVAL",
  "application_context": { "locale": "en-AT", "return_url": "...", "cancel_url": "..." }
}
```

Webhooks: `PAYMENT.CAPTURE.COMPLETED`, `PAYMENT.CAPTURE.DENIED`, `CHECKOUT.ORDER.DECLINED` (with `most_recent_errors`).

## Raw Sources

- [[paypal-apm-eps]] — verbatim overview page
- [[paypal-apm-eps-js-sdk]] — JS SDK integration: `enable-funding=eps&currency=EUR`, name-only fields, single/multi-page flows
- [[paypal-apm-eps-orders-api]] — Orders API integration: same auto-capture pattern as Bancontact; `payment_source.eps` with `country_code: AT` + `name` (no email)

## Relevant Wiki Pages

- [[paypal-apm]] — APM overview with all 11 supported methods
- [[source-paypal-apm-bancontact]] — Bancontact (same structure)
