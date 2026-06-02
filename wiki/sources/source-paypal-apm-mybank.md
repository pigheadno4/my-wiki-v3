---
title: "Accept MyBank Payments"
type: source
date_ingested: 2026-04-14
original_format: webpage
raw_files:
  - "paypal-apm-mybank.md"
  - "paypal-apm-mybank-js-sdk.md"
  - "paypal-apm-mybank-orders-api.md"
tags: [paypal, apm, mybank, italy, bank-redirect, local-payment-methods]
---

## Overview

MyBank is Italy's bank redirect payment method. Same eligibility structure as Bancontact/BLIK/EPS.

Source URL: <https://developer.paypal.com/docs/checkout/apm/mybank/>

Last updated: 2025-05-13

## Key Details

| Field | Value |
| --- | --- |
| Countries | Italy (IT) only |
| Currency | EUR |
| Minimum | N/A (no minimum) |
| Refunds | Within 180 days |
| Flow | Bank redirect |
| Merchant eligibility | Global (excluding Russia, Japan, Brazil) |

## Eligibility Restrictions (same as Bancontact/BLIK/EPS/iDEAL)

- No billing agreements, no multiple seller payments, no shipping callbacks
- **No chargebacks**
- **Capture only** — authorization not supported
- **Online only**

## Integration Methods

- JavaScript SDK
- Orders REST API

## JS SDK Integration

Source URL: <https://developer.paypal.com/docs/checkout/apm/mybank/js-sdk/>

Last updated: 2025-03-18

### SDK script

```html
<script src="https://www.paypal.com/sdk/js?client-id=CLIENT_ID&components=buttons,payment-fields,marks,funding-eligibility&enable-funding=mybank&currency=EUR"></script>
```

### Payment fields

Collects **first name and last name only** — same as Bancontact, EPS, iDEAL.

### Notable differences vs other APM JS SDK guides

- **No separate mark image** — no dedicated mark PNG; renders via `paypal.FUNDING.MYBANK` only
- **No self-serve onboarding links** in Know before you code section
- **Different APM agreement URL**: `paypal.com/us/legalhub/paypal/apm-tnc` (vs `webapps/mpp/ua/apm-tnc` in other APMs)
- GitHub sample: `github.com/paypal-examples/mybank-paypal-payment-js-sdk`

## Orders API Integration

Source URL: <https://developer.paypal.com/docs/checkout/apm/mybank/orders-api/>

Last updated: 2025-05-06

Same auto-capture pattern as Bancontact/EPS. `payment_source.mybank` with `country_code: IT` + `name` only. No self-serve onboarding links (unlike Bancontact/EPS/BLIK).

> [!info] Doc error
> The second webhook sample heading reads "Sample CHECKOUT.ORDER.DENIED webhook" but the actual `event_type` in the payload is `PAYMENT.CAPTURE.DENIED`. The heading is mislabeled in the original docs.

## Raw Sources

- [[paypal-apm-mybank]] — verbatim overview page
- [[paypal-apm-mybank-js-sdk]] — JS SDK integration: `enable-funding=mybank&currency=EUR`, name-only fields, no mark image, no self-serve onboarding links
- [[paypal-apm-mybank-orders-api]] — Orders API integration: same auto-capture as Bancontact/EPS; no onboarding links; doc error: second webhook heading says "CHECKOUT.ORDER.DENIED" but event_type is PAYMENT.CAPTURE.DENIED

## Relevant Wiki Pages

- [[paypal-apm]] — APM overview with all 11 supported methods
- [[source-paypal-apm-bancontact]] — Bancontact (same structure)
