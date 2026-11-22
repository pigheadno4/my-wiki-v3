---
title: "Stripe Multicapture"
type: concept
category: technology
tags: [stripe, multicapture, capture, payment-intents, checkout, ic-plus, connect]
---

## Overview

Multicapture lets you capture a single authorized PaymentIntent in parts, for example as goods ship. In the May 11, 2026 guide Stripe offers up to 50 captures per PaymentIntent and describes multicapture as an IC+ feature. It directs blended-pricing users seeking access to Stripe support. See [[source-stripe-multicapture]].

## Availability

- Online card payments only (`capture_method: 'manual'` required)
- Cards: Amex, Visa, Discover, Mastercard, Cartes Bancaires, Diners Club, CUP (US only), JCB (US/CA/AU/NZ only)
- Max **50 captures** per PaymentIntent
- Not supported: Separate Charges & Transfers with `source_transaction`

## Enabling

The May 11, 2026 [[source-stripe-multicapture|multicapture guide]] requests `payment_method_options.card.request_multicapture: 'if_available'` and checks `latest_charge.payment_method_details.card.multicapture.status` for `available` or `unavailable` after confirmation. Stripe-hosted and embedded Checkout use `mode: 'payment'` and `payment_intent_data.capture_method: 'manual'` at Session creation. The Advanced route works directly with a manual PaymentIntent.

The May embedded Node sample omits the documented manual setting. May also warns that `automatic` and `automatic_async` can report `available` even though the Intent automatically captures in full.

## Capture Flow

```text
POST /payment_intents/:id/capture
  amount_to_capture: 700       # partial amount
  final_capture: false          # keep remaining authorized
```

- In the May 11, 2026 [[source-stripe-multicapture|dedicated guide]], a non-final partial capture with `final_capture: false` keeps the remainder authorized. A final capture uses `final_capture: true` by default, releases any remaining authorization and finalizes the captured Intent as `succeeded`.
- On expiry Stripe releases the uncaptured authorization. A wholly uncaptured Intent becomes `canceled`. An already partially captured Intent becomes `succeeded` on finalization at expiry.
- To finalize an already partially captured Intent without taking more funds, use `amount_to_capture: 0` and `final_capture: true`.
- The separate May [[source-stripe-flexible-features-migration#Multicapture|beta-to-GA migration guide]] documents HTTP 400 for a non-final capture of the entire remaining amount in its GA flow.

## Key Webhooks

| Event | Fires |
| --- | --- |
| `charge.updated` | Every capture |
| `payment_intent.amount_capturable_updated` | Every capture |
| `charge.captured` | Final capture or auth window expiry only |

The May guide describes `refund.created` for each partial refund separately from the Charge Boolean `refunded`, which becomes true only after final capture and refund of the entire `amount_received`. While the Intent is still in `requires_capture`, already captured amounts can be refunded repeatedly up to `amount_received - amount_refunded`. See [[source-stripe-multicapture#Refunds|multicapture refund scope]].

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

- [[source-stripe-multicapture]] — May 2026 full web guide for hosted Checkout, embedded Checkout and direct PaymentIntents. November 2026 adds a variant index.
- [[source-stripe-payment-line-items-flexible]] — multicapture with payment line items (aggregation rules)
- [[source-stripe-flexible-features-migration]] — 2026-05-11 full beta-to-GA migration guide for the dated version header, full-remaining-amount error, event switch and uncaptured-funds representation; November capture is variant navigation only
