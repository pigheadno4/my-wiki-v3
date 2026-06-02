---
title: "Accept Bancontact Payments"
type: source
date_ingested: 2026-04-14
original_format: webpage
raw_files:
  - "paypal-apm-bancontact.md"
  - "paypal-apm-bancontact-js-sdk.md"
  - "paypal-apm-bancontact-orders-api.md"
tags: [paypal, apm, bancontact, belgium, bank-redirect, local-payment-methods]
---

## Overview

Bancontact integration overview — Belgium's dominant payment method (15M+ cards, 150K+ daily online transactions, 20+ issuing banks). Belgium only.

Source URL: <https://developer.paypal.com/docs/checkout/apm/bancontact/>

Last updated: 2025-05-09

## Key Details

| Field | Value |
| --- | --- |
| Countries | Belgium (BE) only |
| Currency | EUR |
| Minimum | 1 EUR |
| Refunds | Within 180 days |
| Flow | Bank redirect |
| Merchant eligibility | Global (excluding Russia, Japan, Brazil) |

## Eligibility Restrictions

- No billing agreements
- No multiple seller payments
- No shipping callbacks
- **No chargebacks**
- **Capture only** — authorization not supported
- **Online only** — buy online, pay in-store not supported

## Integration Methods

- JavaScript SDK (PayPal-hosted payment fields)
- Orders REST API (full customization)

## JS SDK Integration

Source URL: <https://developer.paypal.com/docs/checkout/apm/bancontact/js-sdk/>

Last updated: 2025-03-18

### SDK script

```html
<script src="https://www.paypal.com/sdk/js?client-id=CLIENT_ID&components=buttons,payment-fields,marks,funding-eligibility&enable-funding=bancontact&currency=EUR"></script>
```

Required components: `buttons`, `payment-fields`, `marks`, `funding-eligibility`.

### Payment fields

Collects first name + last name only (minimal for bank redirect). Two flows:

- **Single-page**: fields + button on same page
- **Multi-page**: page 1 renders mark + fields with `onInit`/`actions.validate()` to gate navigation; page 2 renders button. **German merchants** use multi-page for local regulatory compliance.

### Webhooks

| Event | Action |
| --- | --- |
| `CHECKOUT.ORDER.APPROVED` | Capture the payment |
| `CHECKOUT.PAYMENT-APPROVAL.REVERSED` | Capture window missed — notify buyer, order cancelled |
| `CHECKOUT.ORDER.DECLINED` | Handle failure with reason code |
| `PAYMENT.CAPTURE.PENDING/COMPLETED/DENIED` | Monitor capture status |

### Onboarding

Self-serve approval required (sandbox + live links). **Progressive Onboarding not supported** for APMs — onboard merchants before they accept payments.

### Notes

- Orders must be created in EUR
- Multipage flow images (`Multipage_1_temp.png`, `Multipage_2_temp.png`) are shared across APM JS SDK guides

## Orders API Integration

Source URL: <https://developer.paypal.com/docs/checkout/apm/bancontact/orders-api/>

Last updated: 2025-03-18

### Create Order payload

```json
{
  "intent": "CAPTURE",
  "payment_source": {
    "bancontact": {
      "country_code": "BE",
      "name": "John Doe"
    }
  },
  "processing_instruction": "ORDER_COMPLETE_ON_PAYMENT_APPROVAL",
  "application_context": {
    "locale": "en-BE",
    "return_url": "https://example.com/returnUrl",
    "cancel_url": "https://example.com/cancelUrl"
  }
}
```

**Key distinction**: `processing_instruction: ORDER_COMPLETE_ON_PAYMENT_APPROVAL` — payment is **auto-captured** when buyer approves at bank; no explicit capture call needed.

Uses `application_context` (not `experience_context`).

### Flow

1. Create order → response: `PAYER_ACTION_REQUIRED` + `payer-action` HATEOAS link
2. Redirect buyer to `payer-action` URL (bank approval)
3. Auto-capture on approval → buyer returned to `return_url`
4. `PAYMENT.CAPTURE.COMPLETED` webhook confirms success

### Webhooks (Orders API — different from JS SDK)

| Event | Trigger |
| --- | --- |
| `PAYMENT.CAPTURE.COMPLETED` | Successful capture |
| `PAYMENT.CAPTURE.DENIED` | Failed capture |
| `CHECKOUT.ORDER.DECLINED` | Declined — `most_recent_errors[].issue` + `.description` in `purchase_units` |

**Polling fallback**: `GET /v2/checkout/orders/{id}` if webhook missed — rate limits enforced by PayPal.

## Raw Sources

- [[paypal-apm-bancontact]] — verbatim overview page
- [[paypal-apm-bancontact-js-sdk]] — JS SDK integration: script tag, payment fields, single/multi-page flows, webhooks, onboarding
- [[paypal-apm-bancontact-orders-api]] — Orders API integration: auto-capture via `ORDER_COMPLETE_ON_PAYMENT_APPROVAL`, `application_context`, webhook payloads with `most_recent_errors`

## Relevant Wiki Pages

- [[paypal-apm]] — APM overview with all 11 supported methods
