---
title: "Stripe Multicapture"
type: concept
category: technology
tags: [stripe, multicapture, capture, payment-intents, checkout, ic-plus, connect]
---

## Overview

Multicapture lets you capture a single authorized PaymentIntent up to 50 times, capturing partial amounts as goods ship. Each capture draws down the authorized amount; remaining funds stay reserved until final capture or the auth window expires. **IC+ pricing required.**

## Availability

- Online card payments only (`capture_method: 'manual'` required)
- Cards: Amex, Visa, Discover, Mastercard, Cartes Bancaires, Diners Club, CUP (US only), JCB (US/CA/AU/NZ only)
- Max **50 captures** per PaymentIntent
- Not supported: Separate Charges & Transfers with `source_transaction`

## Enabling

`payment_method_options.card.request_multicapture: 'if_available'` on create/confirm. The response includes `charge.payment_method_details.card.multicapture.status: 'available' | 'unavailable'`.

**Checkout**: set at session creation with `payment_intent_data.capture_method: 'manual'` and `mode: 'payment'`. Works with Stripe-hosted, embedded, and custom Elements integrations.

## Capture Flow

```text
POST /payment_intents/:id/capture
  amount_to_capture: 700       # partial amount
  final_capture: false          # keep remaining authorized
```

- `final_capture: false` — partial capture, remaining stays authorized; **returns 400 error if capturing the full remaining amount**
- `final_capture: true` (default) — releases remaining funds, PI → `succeeded`
- `amount_to_capture: 0` + `final_capture: true` — release all without capturing

## Key Webhooks

| Event | Fires |
| --- | --- |
| `charge.updated` | Every capture |
| `payment_intent.amount_capturable_updated` | Every capture |
| `charge.captured` | Final capture or auth window expiry only |

`charge.refunded` → `true` only after final capture + complete refund of `amount_received`.

## Partial Refunds Limitation

Cannot use `refund_application_fee=true` or `reverse_transfer=true` for partial refunds. Use application fee refund and transfer reversal endpoints manually instead. After using those, further refunds with those flags are blocked.

## Connect

- All Connect flows supported except Separate Charges & Transfers with `source_transaction`
- `application_fee_amount` / `transfer_data[amount]`: if set on first capture, required on all subsequent; each capture overrides PI creation values

## Compliance

Merchant is responsible for network compliance. Most networks restrict to card-not-present + separately shipped goods. Best practice: notify customers of each shipment's delivery date and amount before and at purchase.

## Related IC+ Features

- [[stripe-overcapture]] — capture above authorized amount (single capture); contrast with multicapture (multiple captures up to authorized amount)

## Sources

- [[source-stripe-multicapture]] — full integration guide (Stripe-hosted, embedded, Elements), test cards, Connect/refund details
- [[source-stripe-payment-line-items-flexible]] — multicapture with payment line items (aggregation rules)
