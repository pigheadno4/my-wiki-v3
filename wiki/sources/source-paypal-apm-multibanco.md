---
title: "Accept Multibanco Payments"
type: source
date_ingested: 2026-04-14
original_format: webpage
raw_files:
  - "paypal-apm-multibanco.md"
  - "paypal-apm-multibanco-js-sdk.md"
  - "paypal-apm-multibanco-orders-api.md"
tags: [paypal, apm, multibanco, portugal, voucher, local-payment-methods]
---

## Overview

Multibanco is Portugal's interbank network — a **voucher** payment (not bank redirect). Fundamentally different from Bancontact/BLIK/EPS/iDEAL in flow and restrictions.

Source URL: <https://developer.paypal.com/docs/checkout/apm/multibanco/>

Last updated: 2025-05-14

## Key Details

| Field | Value |
| --- | --- |
| Country | Portugal (PT) only |
| Currency | EUR |
| Minimum | N/A (no minimum) |
| **Maximum** | **99,999.99 EUR** |
| **Refunds** | **N/A — no refunds supported** |
| Payment type | **Voucher** (not bank redirect) |
| Flow | Redirect |

## How it Works (non-instant)

1. Buyer chooses Multibanco and provides first name + last name
2. Payment instruction presented to buyer (reference number)
3. Buyer pays via online banking **or Multibanco ATM**
4. Merchant receives `PAYMENT.CAPTURE.COMPLETED` webhook (asynchronous)
5. Merchant ships goods after webhook confirmation

Uses `unbranded-flow-non-instant.svg` — distinct from the instant bank redirect flow used by Bancontact/BLIK/EPS/iDEAL.

## Differences vs Other Bank Redirect APMs

| Aspect | Multibanco | Bancontact/BLIK/EPS/iDEAL |
| --- | --- | --- |
| Payment type | Voucher | Bank redirect |
| Settlement | Non-instant (ATM/online banking later) | Instant (real-time bank redirect) |
| Minimum | None | 0.01–1 EUR |
| Maximum | 99,999.99 EUR | None listed |
| Refunds | **Not supported** | Within 180 days |
| Eligibility restrictions | Not documented | No chargebacks, capture-only, etc. |

## Integration Methods

- JavaScript SDK
- Orders REST API

## JS SDK Integration

Source URL: <https://developer.paypal.com/docs/checkout/apm/multibanco/js-sdk/>

Last updated: 2025-02-20

### SDK script

```html
<script src="https://www.paypal.com/sdk/js?client-id=CLIENT_ID&components=buttons,payment-fields,marks,funding-eligibility&enable-funding=multibanco&currency=EUR"></script>
```

### Payment fields

Collects **name only** (first + last). Single-page flow only — no multi-page (voucher payment doesn't require multi-page checkout).

### `isEligible()` check

Recommended before rendering: `button.isEligible()` — more prominent than in other APM JS SDK guides.

### Unique webhook behavior (voucher-specific)

| Webhook | Meaning | Action |
| --- | --- | --- |
| `CHECKOUT.ORDER.APPROVED` | Order approved; retrieve `BARCODE_URL` | Send voucher via email or display again; **capture is automatic** |
| `PAYMENT.CAPTURE.PENDING` | Buyer hasn't paid at ATM yet | Wait |
| `PAYMENT.CAPTURE.COMPLETED` | ATM payment received | Ship goods |
| `PAYMENT.CAPTURE.DENIED` | Voucher expired without payment | Notify buyer |

> [!info] Doc typo
> The `createOrder` note says "Create Bancontact orders in EUR" — should say Multibanco. Copy-paste error from Bancontact guide.

## Orders API Integration

Source URL: <https://developer.paypal.com/docs/checkout/apm/multibanco/orders-api/>

Last updated: 2025-05-06

### Two-step flow (different from all other APM Orders API integrations)

**Step 1** — Create order (no `payment_source`):

```json
{ "intent": "CAPTURE", "purchase_units": [{ "amount": { "currency_code": "EUR", "value": "100.00" } }] }
```

Response: `status: CREATED`, HTTP 201.

**Step 2** — Confirm payment source:

```json
{
  "payment_source": { "multibanco": { "name": "John Doe", "country_code": "PT" } },
  "processing_instruction": "ORDER_COMPLETE_ON_PAYMENT_APPROVAL",
  "application_context": { "locale": "en-PT", "return_url": "...", "cancel_url": "..." }
}
```

Response: `payer-action` HATEOAS link → redirect buyer to Multibanco payment instruction page.

> [!info] `application_context` at root
> Unlike iDEAL which puts `experience_context` inside `payment_source.ideal`, Multibanco uses `application_context` at the root level of the confirm-payment-source request.

### `payment_reference` + `payment_entity`

After redirect, call GET `/orders/{id}` to retrieve `payment_source.multibanco.payment_reference` and `.payment_entity` — the voucher reference and bank entity code. Send to buyer via email.

### Webhook sequence (up to 7 days)

1. `PAYMENT.CAPTURE.PENDING` (immediate after confirm) — capture status: `PENDING`
2. Up to 7 days later:
   - `PAYMENT.CAPTURE.COMPLETED` → ship goods
   - `PAYMENT.CAPTURE.DENIED` → voucher expired / buyer didn't complete

## Raw Sources

- [[paypal-apm-multibanco]] — verbatim overview page
- [[paypal-apm-multibanco-js-sdk]] — JS SDK integration: `enable-funding=multibanco`, name-only fields, `BARCODE_URL` in webhook, voucher expiration via `PAYMENT.CAPTURE.DENIED`
- [[paypal-apm-multibanco-orders-api]] — Orders API integration: 2-step flow (create order without payment_source → confirm-payment-source), `payment_reference` + `payment_entity`, 7-day payment window

## Relevant Wiki Pages

- [[paypal-apm]] — APM overview with all 11 supported methods
