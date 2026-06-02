---
title: "Accept Trustly Payments"
type: source
date_ingested: 2026-04-14
original_format: webpage
raw_files:
  - "paypal-apm-trustly.md"
  - "paypal-apm-trustly-js-sdk.md"
  - "paypal-apm-trustly-orders-api.md"
tags: [paypal, apm, trustly, europe, bank-redirect, local-payment-methods, multi-currency]
---

## Overview

Trustly is a bank redirect payment method covering 12 European countries and 5 currencies — the broadest European coverage of any bank redirect APM. Non-instant settlement (up to 7 days).

Source URL: <https://developer.paypal.com/docs/checkout/apm/trustly/>

Last updated: 2025-05-09

## Key Details

| Field | Value |
| --- | --- |
| Countries | AT, DE, DK, EE, ES, FI, GB, LT, LV, NL, NO, SE (12 countries) |
| Currencies | **EUR, DKK, SEK, GBP, NOK** (5 currencies — most of any bank redirect APM) |
| Minimum | 0.01 EUR (or equivalent) |
| Refunds | **Up to 365 days** (longest of all APMs) |
| Settlement | **Non-instant** — up to 7 days after authorization |
| Payment type | Bank redirect |

## Key Differences vs Other Bank Redirect APMs

| Aspect | Trustly | Bancontact/BLIK/EPS/iDEAL/MyBank |
| --- | --- | --- |
| Countries | 12 European | 1 each |
| Currencies | EUR, DKK, SEK, GBP, NOK | 1 each |
| Settlement | Up to 7 days (non-instant) | Instant |
| Refunds | 365 days | 180 days |
| Merchant exclusions | RU, BR, BE, CZ, PL, SK, SI | RU, JP, BR |

## Non-Instant Settlement Flow

1. Buyer authorizes payment at bank
2. Merchant receives **payment initiation webhook** (PENDING state)
3. Payment completes within **7 days** (bank-dependent)
4. Merchant receives **payment completion webhook** → ship goods

## Eligibility Restrictions

- No billing agreements, no multiple seller payments, no shipping callbacks
- **No chargebacks**
- **Capture only** — authorization not supported
- **Online only**
- Merchant exclusions: Russia, Brazil, **Belgium, Czechia, Poland, Slovakia, Slovenia** (different from other APMs which exclude Japan instead)

## Integration Methods

- JavaScript SDK
- Orders REST API

## Orders API Integration

Source URL: <https://developer.paypal.com/docs/checkout/apm/trustly/orders-api/>

Last updated: 2025-05-06

`payment_source.trustly` with `country_code` + `name` (name-only in sample). Email is **optional** — listed in Modify the code section but absent from sample request.

Same auto-capture pattern and currency/country mismatch error as JS SDK. Full PENDING webhook payload included.

> [!info] Doc errors
> (1) `PAYMENT.CAPTURE.DENIED` webhook description says "Multibanco payment instruction has expired" — should say Trustly (copy-paste error).
> (2) `cancel_url` noted as "a placeholder for future reference for now" — unusual for an APM guide.

## JS SDK Integration

Source URL: <https://developer.paypal.com/docs/checkout/apm/trustly/js-sdk/>

Last updated: 2025-08-17

### SDK script

```html
<script src="https://www.paypal.com/sdk/js?client-id=CLIENT_ID&components=buttons,payment-fields,marks,funding-eligibility&enable-funding=trustly&currency=EUR"></script>
```

Supports EUR, DKK, SEK, GBP, NOK — must match the country's currency.

### Payment fields

Name only (first + last) — same as Bancontact/EPS. No multipage flow images. `isEligible()` check recommended.

### Unique `onApprove` behavior

Unlike other APMs where `onApprove` captures the order:

```javascript
onApprove(data) {
    // You do NOT need to capture — already auto-captured
    // Show thank-you message and listen for webhooks
}
```

### Webhook pattern (same as Multibanco/Trustly non-instant)

- `CHECKOUT.ORDER.APPROVED` → auto-capture, no code needed
- `PAYMENT.CAPTURE.PENDING` → payment in progress (up to 7 days)
- `PAYMENT.CAPTURE.COMPLETED` → ship goods
- `PAYMENT.CAPTURE.DENIED` → cancel order

**Note**: "Payment completion happens within 7 days, depending on the bank."

### Error: `CURRENCY_NOT_SUPPORTED_BY_PAYMENT_SOURCE`

Currency must match the country. Example: SEK cannot be used with `country_code: NL`. Each country supports specific currencies from the EUR/DKK/SEK/GBP/NOK set.

## Raw Sources

- [[paypal-apm-trustly]] — verbatim overview page
- [[paypal-apm-trustly-js-sdk]] — JS SDK integration: `enable-funding=trustly`, name-only, unique `onApprove`, non-instant webhook pattern, currency/country mismatch error
- [[paypal-apm-trustly-orders-api]] — Orders API integration: `payment_source.trustly` (name + optional email); full PENDING webhook payload; `cancel_url` placeholder note; two doc errors

## Relevant Wiki Pages

- [[paypal-apm]] — APM overview with all 11 supported methods
