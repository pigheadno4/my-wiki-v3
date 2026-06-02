---
title: "Accept iDEAL Payments"
type: source
date_ingested: 2026-04-14
original_format: webpage
raw_files:
  - "paypal-apm-ideal.md"
  - "paypal-apm-ideal-js-sdk.md"
  - "paypal-apm-ideal-orders-api.md"
tags: [paypal, apm, ideal, netherlands, bank-redirect, local-payment-methods, onboarding]
---

## Overview

iDEAL is the Netherlands' dominant bank redirect payment method — buyers select their issuing bank from a list. Buyer experience varies by bank.

Source URL: <https://developer.paypal.com/docs/checkout/apm/ideal/>

Last updated: 2025-05-09

## Key Details

| Field | Value |
| --- | --- |
| Countries | Netherlands (NL) only |
| Currency | EUR |
| Minimum | **0.01 EUR** — lowest of all APMs |
| Refunds | Within 180 days |
| Flow | Bank redirect |
| Merchant eligibility | Global (excluding Russia, Japan, Brazil) |

## Eligibility Restrictions (same as Bancontact/BLIK/EPS)

- No billing agreements, no multiple seller payments, no shipping callbacks
- **No chargebacks**
- **Capture only** — authorization not supported
- **Online only**

## Onboarding (unique detail vs other APMs)

### Listed countries (32, including AT/AU/BE/BG/CA/CY/CZ/DE/DK/EE/ES/FI/FR/GR/HU/IE/IT/LI/LT/LU/LV/MT/NL/NO/PL/PT/RO/SE/SI/SK/UK/US)

Self-serve production onboarding: `paypal.com/bizsignup/add-product?product=iDEAL&capabilities=IDEAL`

**Partners (ISU flow)**:

- Call Partner Referral API
- Pass `iDEAL` in `products` array
- **Skip** the `capabilities` array (important — unlike other APMs)

### Merchants outside listed countries

Offline onboarding required:

1. Merchant completes CIP (Critical Infrastructure Protection) process
2. Partner coordinates with Customer Success Manager or Sales rep to enable iDEAL
3. **Merchant must include website URL in their PayPal account** during this process

## Integration Methods

- JavaScript SDK
- Orders REST API

## JS SDK Integration

Source URL: <https://developer.paypal.com/docs/checkout/apm/ideal/js-sdk/>

Last updated: 2025-03-28

### SDK script

```html
<script src="https://www.paypal.com/sdk/js?client-id=CLIENT_ID&components=buttons,payment-fields,marks,funding-eligibility&enable-funding=ideal&currency=EUR"></script>
```

### Payment fields

Collects **first name and last name only** — same as Bancontact and EPS (BLIK also collects email).

### Checkout flows

Single-page and multi-page (same pattern as other APMs).

### Unique: merchant onboarding error

Explicit error message documented for when merchant isn't onboarded:
> "The 'API caller' and/or 'payee' is not set up to be able to process the selected payment source..."

Not seen in other APM JS SDK guides — reflects iDEAL's more complex onboarding requirement.

### Notes

- Orders must be created in EUR
- GitHub sample: `github.com/paypal-examples/ideal-paypal-payment-js-sdk`

## Orders API Integration

Source URL: <https://developer.paypal.com/docs/checkout/apm/ideal/orders-api/>

Last updated: 2025 (exact date not in source)

Same auto-capture pattern as Bancontact/BLIK/EPS. `payment_source.ideal` with `name` + `country_code: NL` (no email).

### Unique: two onboarding failure scenarios

**1. Unsuccessful confirm-payment-source** — `POST /orders/{id}/confirm-payment-source` with `experience_context` inside `payment_source.ideal`:

```json
{
  "payment_source": {
    "ideal": {
      "country_code": "NL",
      "name": "Firstname Lastname",
      "experience_context": {
        "return_url": "https://example.com/return",
        "cancel_url": "https://example.com/cancel"
      }
    }
  }
}
```

→ 422 `NOT_ENABLED_FOR_PAYMENT_SOURCE` when merchant not onboarded.

**2. Unsuccessful single-shot create order** — same `experience_context` in payment_source + `ORDER_COMPLETE_ON_PAYMENT_APPROVAL` → same 422 error.

> [!info] `experience_context` location
> In the confirm-payment-source variant, `experience_context` is nested inside `payment_source.ideal` — unlike other APMs where it goes in `application_context` at the root level.

## Raw Sources

- [[paypal-apm-ideal]] — verbatim overview page (unique onboarding section)
- [[paypal-apm-ideal-js-sdk]] — JS SDK integration: `enable-funding=ideal&currency=EUR`, name-only fields, merchant onboarding error message
- [[paypal-apm-ideal-orders-api]] — Orders API integration: auto-capture, two onboarding failure scenarios (confirm-payment-source + single-shot), `experience_context` inside `payment_source.ideal`

## Relevant Wiki Pages

- [[paypal-apm]] — APM overview with all 11 supported methods
