---
title: "Stripe Incremental Authorization (Online)"
type: concept
category: technology
tags: [stripe, incremental-authorization, capture, payment-intents, ic-plus, sca, visa, mastercard]
---

## Overview

Incremental authorization lets you increase the authorized amount on a confirmed PaymentIntent before capture. Used for travel/hospitality where the final amount isn't known at authorization time (car rentals, hotel stays). **IC+ pricing required.**

Each increment creates a **separate pending entry** on the customer's card statement. After capture, all pending entries are replaced by one final captured amount.

For in-person incremental authorization, see [[stripe-terminal-incremental-authorizations]].

## Availability

- Visa and Mastercard: all categories, global (MC excl. MX users, JPY for JP)
- AmEx: all categories, global — **some issuers don't support** (check `incremental_authorization.status`)
- Discover: specific T&E categories only (car rental, hotels, restaurants, transit, parking, amusement parks, etc.)
- Discover CNP: also taxicabs
- Beta (Diners Club, UnionPay, JCB): same T&E categories via Discover, CNP only

Attempting incremental auth on ineligible payments returns an error.

## API

```js
// Enable at confirm
payment_method_options: { card: { request_incremental_authorization: 'if_available' } }

// Check availability on charge
charge.payment_method_details.card.incremental_authorization.status  // 'available' | 'unavailable'

// Increment (pass new total, not delta)
POST /payment_intents/:id/increment_authorization  { amount: 1500 }
```

**Limits**:

- Max 10 increments per PaymentIntent
- Per-increment cap: greater of +$500 or +500% over the previous authorized amount

**On failure**: `card_declined` error; PI remains capturable at previous amount; no field updates saved.

## Key Constraint

Does **NOT extend the authorization validity window** — must still capture before the initial auth expires. Use [[stripe-extended-authorization]] to extend the window.

## SCA Countries

When incremental auth is requested under SCA: Stripe auto-configures PM for future off-session usage; initial auth requires 3DS; subsequent increments treated as MIT (potentially SCA-exempt). No liability shift applies to MIT transactions. Disclose off-session usage to customer at checkout.

## Combining with Partial Authorization

Can combine incremental auth with [[stripe-partial-authorization]] — pass `request_partial_authorization: 'if_available'` on the increment endpoint to allow the issuer to partially approve the requested increment amount.

## Related IC+ Features

- [[stripe-extended-authorization]] — extends auth window (complementary to incremental auth)
- [[stripe-multicapture]] — multiple partial captures within the authorized amount
- [[stripe-overcapture]] — capture above authorized amount
- [[stripe-terminal-incremental-authorizations]] — in-person Terminal variant

## Sources

- [[source-stripe-incremental-authorization]] — full guide with availability tables, SCA rules, API limits, test cards
