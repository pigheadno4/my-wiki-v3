---
title: "Accept Swish Payments"
type: source
date_ingested: 2026-04-14
original_format: webpage
raw_files:
  - "paypal-apm-swish.md"
  - "paypal-apm-swish-orders-api.md"
tags: [paypal, apm, swish, sweden, push-payment, qr-code, mobile, sek]
---

## Overview

Swish is Sweden's leading mobile payment method — push payment type with instant settlement. **Not in the original 11-APM overview table** — added November 2025.

Source URL: <https://developer.paypal.com/docs/checkout/apm/swish/>

Last updated: 2026-04-07

## Key Details

| Field | Value |
| --- | --- |
| Countries | Sweden (SE) only |
| Currency | SEK |
| Payment type | **Push** (like Apple Pay/Google Pay — not bank redirect) |
| Minimum | 0.01 SEK |
| Maximum | **999,999,999,999.99 SEK** (largest of all APMs) |
| Refunds | Full/partial, **up to 13 months** (longest of all APMs) |
| Settlement | Instant, auto-capture |

## Two Buyer Flows

- **QR code flow**: Buyer scans QR code on desktop; returns to merchant after payment
- **Mobile app switch flow**: Redirects buyer to Swish app on mobile; returns automatically after approval

## Two Integration Patterns (unique to Swish)

| Pattern | How it works |
| --- | --- |
| **PayPal-hosted** | Redirect to `payer-action` link; PayPal handles payment UI |
| **Merchant-hosted** | Display `qr_details.qr_image` on your own checkout page; control the payment UI |

Both patterns support QR code and mobile app switch flows.

## Key Distinctions vs Other APMs

- **Push payment** (not bank redirect) — immediate settlement
- **Longest refund window**: 13 months (vs Trustly's 365 days for bank redirects)
- **Largest max amount**: ~1 trillion SEK
- **Merchant-hosted pattern**: `qr_details.qr_image` field — not seen in any other APM

## Orders API Integration

Source URL: <https://developer.paypal.com/docs/checkout/apm/swish/orders-api/>

Last updated: 2026-03-31

### Create Order payload (unique features)

```json
{
  "intent": "CAPTURE",
  "processing_instruction": "ORDER_COMPLETE_ON_PAYMENT_APPROVAL",
  "payment_source": {
    "swish": {
      "name": "John Doe",
      "country_code": "SE",
      "experience_context": {
        "locale": "sv-SE",
        "return_url": "...",
        "cancel_url": "...",
        "redirect_to_app": true
      }
    }
  },
  "payer": {
    "email_address": "...",
    "first_name": "...",
    "last_name": "...",
    "country_code": "SE",
    "phone": { "phone_type": "MOBILE", "phone_number": { "national_number": "..." } }
  },
  "purchase_units": [{ "amount": { "currency_code": "SEK", "value": "100" } }]
}
```

**Unique aspects vs other APMs:**

- **`payer` object** (email, name, country, phone) — not seen in any other APM Orders API
- **Both auto-capture** (`ORDER_COMPLETE_ON_PAYMENT_APPROVAL`) **and manual capture** (`NO_INSTRUCTION`) supported
- **Mobile app switch**: set `redirect_to_app: true`; `payer-action` URL is `swish://paymentrequest?token=...` (custom scheme)
- **`qr_details.qr_image`** (base64) + `qr_details.qr_payload` in response — for Merchant-hosted pattern
- **Seller protection: ELIGIBLE** in capture response (unusual for APMs)

> [!info] Approval request links empty
> Sandbox and Live approval request links are blank — Swish likely still in limited release. Use self-serve dashboard onboarding (Account Settings > Products & Services > Payment Methods).
> Also: Webhook docs URL references Klarna path (`/klarna/accept-klarna-payments/...`) — copy-paste artifact in source.

## Raw Sources

- [[paypal-apm-swish]] — verbatim overview page with buyer flow image
- [[paypal-apm-swish-orders-api]] — Orders API integration: `payer` object, auto/manual capture, `swish://` URL scheme, `qr_details.qr_image`, seller protection eligible

## Relevant Wiki Pages

- [[paypal-apm]] — APM overview (note: Swish not in original 11-APM table — added Nov 2025)
