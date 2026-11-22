---
title: "Stripe — Multicapture"
type: source
date_ingested: 2026-05-11
original_format: webpage
raw_files:
  - "stripe-multicapture-2026.md"
tags: [stripe, multicapture, capture, payment-intents, checkout, ic-plus, connect, webhooks]
---

## Summary

IC+ feature allowing multiple partial captures on a single PaymentIntent up to 50 times, up to the full authorized amount. Used for orders with multiple shipments. Covered across three integration paths: Stripe-hosted Checkout, Embedded Checkout, and direct PaymentIntents (Elements).

## Availability

- **IC+ pricing only** — blended pricing users must contact Stripe
- Online card payments only (`capture_method: 'manual'` required)
- Cards: Amex, Visa, Discover, Mastercard, Cartes Bancaires, Diners Club, CUP (US only), JCB (US/CA/AU/NZ only)
- **Max 50 captures** per PaymentIntent
- Separate Charges & Transfers with `source_transaction` NOT supported

## Enabling Multicapture

Set `payment_method_options.card.request_multicapture: 'if_available'` on create/confirm. Check `charge.payment_method_details.card.multicapture.status` in the response → `available` or `unavailable`.

**Checkout**: set on `payment_method_options.card.request_multicapture` at session creation with `payment_intent_data.capture_method: 'manual'` and `mode: 'payment'`.

## Capture Mechanics

- `final_capture: false` — capture partially, keep remaining authorized
- `final_capture: true` (default) — capture and release remaining uncaptured funds → `succeeded`
- Omitting `final_capture` defaults to `true`
- Authorization window expiry also triggers final capture
- **Release without capturing**: `amount_to_capture: 0` + `final_capture: true`

## Webhooks

| Event | When |
| --- | --- |
| `charge.updated` | Every capture |
| `payment_intent.amount_capturable_updated` | Every capture |
| `charge.captured` | Final capture only (or auth window expiry) |
| `refund.created` | Each partial refund |

`charge.refunded` becomes `true` only after final capture + full refund of `amount_received`.

## Refunds

- Can refund multiple times up to `amount_received - amount_refunded`
- **Partial refunds with `refund_application_fee=true` or `reverse_transfer=true` not supported** — use application fee refund and transfer reversal endpoints manually; after doing so, further refunds with those flags aren't supported

## Connect

- All Connect use cases supported except Separate Charges & Transfers with `source_transaction`
- If `application_fee_amount` or `transfer_data[amount]` set on first capture, required on all subsequent captures
- Each capture's values override PI creation/confirmation/update values

## Compliance

Most card networks restrict multicapture to card-not-present transactions for separately shipped goods. Some permit for travel industry; some prohibit for installment/deposit workflows. Merchant is responsible for compliance.

## Test Cards

| Number | Payment Method | Notes |
| --- | --- | --- |
| 4242424242424242 | pm_card_visa | Supports multicapture |
| 4000002500001001 | pm_card_visa_cartesBancaires | Supports multicapture |
| 4000008400000076 | pm_card_credit_disableEnterpriseCardFeatures | Does NOT support multicapture |

## Related Pages

- [[stripe-multicapture]] — concept page
- [[stripe-payment-line-items-flexible]] — multicapture line items behavior

## Raw Sources

- [[stripe-multicapture-2026]] — verbatim multicapture guide, all 3 UI variants (1,033 lines)
