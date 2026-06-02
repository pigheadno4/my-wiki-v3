---
title: "Stripe Overcapture"
type: concept
category: technology
tags: [stripe, overcapture, capture, payment-intents, ic-plus, sca]
---

## Overview

Overcapture lets you capture a higher amount than the original card authorization without triggering a new authorization with card networks. The pending authorization settles at the captured amount — customers see no immediate statement change. **IC+ pricing required.**

Contrast with [[stripe-multicapture]] (multiple captures up to authorized amount) and incremental authorization (new network authorization for more funds).

## Availability

- Online card payments only; `capture_method: 'manual'` required
- Cards: Visa (excl. EEA), Mastercard, AmEx, Discover
- Diners Club: beta support (US only, via Discover)

## Percent Limits

Limits are network-, category-, and country-specific:

| Network | Category | Limit |
| --- | --- | --- |
| Visa (US) | Restaurants, fast food, caterers | +30% |
| Visa | Restaurants, fast food; taxicabs; bars; beauty/spas | +20% |
| Visa | Car rentals | Greater of +15% or $75 USD |
| Visa | Lodging, cruise lines; all other (cardholder-initiated) | +15% |
| Mastercard | US restaurants/fast food (US-issued cards only) | +30% |
| AmEx | Restaurants, bars, fast food | +30% (debit/prepaid max +20%) |
| AmEx | Taxicabs, beauty/spas | +20% |
| AmEx | Lodging, car/truck/RV rental, grocery, retail | +15% |
| Discover | Restaurants, taxicabs, bars, beauty/spas | +20% |
| Discover | Lodging, car rentals | +15% |

## SCA Constraint

In SCA-required countries, authenticate for the highest estimated amount upfront. Exceeding the authenticated amount requires canceling and re-creating the payment. MIT (merchant-initiated transactions) may qualify for exemption.

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

If `amount_to_capture` needs to exceed `maximum_amount_capturable`, use incremental authorization instead.

## Sources

- [[source-stripe-overcapture]] — full guide with percent limit tables, SCA rules, test cards, all 3 integration paths
- [[source-stripe-payment-line-items-flexible]] — overcapture with payment line items
