---
title: "Stripe Overcapture"
type: concept
category: technology
tags: [stripe, overcapture, capture, payment-intents, ic-plus, sca]
---

## Overview

Overcapture lets you capture a higher amount than the original card authorization without triggering a new network authorization. The customer's pending statement entry updates once the captured amount settles.

The May 11, 2026 dedicated guide offers overcapture on IC+ and directs users on standard pricing to Stripe Support to ask about access. The November 7, 2026 [[source-stripe-elements-advanced-payments|Advanced Elements matrix]] lists Overcapture for Checkout Sessions and Payment Intents under flexible scenarios marked IC+ only. The Support referral leaves exceptions, plan changes and actual access unverified. See [[source-stripe-overcapture]].

Contrast with [[stripe-multicapture]] (multiple captures up to authorized amount) and incremental authorization (new network authorization for more funds).

## Availability

- Online card payments only; `capture_method: 'manual'` required
- Cards in the May 2026 guide: Visa (excluding EEA businesses), Mastercard, AmEx, Discover
- Diners Club: beta support (US only, via Discover)
- [[stripe-partial-authorization|Partial authorization]] caps capture at the approved amount. The May and November [[source-stripe-partial-authorization|partial-authorization guides]] prohibit overcapture above that amount.

## Percent Limits

Limits are network-, category-, and country-specific:

| Network | Category | Limit |
| --- | --- | --- |
| Visa (US) | Restaurants, fast food, caterers | +30% |
| Visa | Restaurants, fast food; taxicabs; bars; beauty/spas | +20% |
| Visa | Car rentals | Greater of +15% or USD 75 (or local currency equivalent) |
| Visa | Lodging, cruise lines; all other (cardholder-initiated) | +15% |
| Mastercard | US restaurants/fast food (US-issued cards only) | +30% |
| AmEx | Restaurants, bars, fast food | +30% (debit/prepaid max +20%) |
| AmEx | Taxicabs, beauty/spas | +20% |
| AmEx | Lodging, car/truck/RV rental, grocery, retail | +15% |
| Discover | Restaurants, taxicabs, bars, beauty/spas | +20% |
| Discover | Lodging, car rentals | +15% |

## SCA Constraint

When the merchant and cardholder are in a country with SCA requirements, the May 2026 guide generally calls for authenticating and authorizing at least the expected capture amount. Capture above the original authenticated and authorized amount calls for canceling and recreating the payment unless an applicable exemption applies. A merchant-initiated transaction with the customer absent is potentially exempt.

## API

```js
// Enable at confirm
payment_method_options: { card: { request_overcapture: 'if_available' } }

// Check availability on charge
charge.payment_method_details.card.overcapture.status           // 'available' | 'unavailable'
charge.payment_method_details.card.overcapture.maximum_amount_capturable

// Capture
stripe.paymentIntents.capture(id, { amount_to_capture: 1200 })

// Original auth preserved
charge.payment_method_details.card.amount_authorized
// PI amount updates to captured amount
paymentIntent.amount  // → 1200 after overcapture
```

If overcapture is unavailable, `maximum_amount_capturable` is the authorized amount. If a higher amount is needed, incremental authorization is an option where available.

The May 11, 2026 [[source-stripe-overcapture|Overcapture guide]] requires `payment_intent_data.capture_method=manual` for hosted and embedded Checkout, although both Session examples omit it. Embedded Session `complete` can precede PaymentIntent capture. Check the PaymentIntent and latest Charge server-side.

## Sources

- [[source-stripe-overcapture]] — May 2026 full guide to overcapture eligibility, request paths and capture state. November 2026 web variant index provides navigation.
- [[source-stripe-payment-line-items-flexible]] — overcapture with payment line items
- [[source-stripe-flexible-features-migration]] — 2026-05-11 full beta-to-GA migration guide for pre-confirmation request and conditional charge maximum; November capture is variant navigation only
