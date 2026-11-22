---
title: "Stripe Partial Authorization"
type: concept
category: technology
tags: [stripe, partial-authorization, capture, payment-intents, ic-plus, debit, prepaid]
---

## Overview

Partial authorization lets a card issuer approve a portion of the requested payment amount when the cardholder's available balance is insufficient. The customer can then pay the remaining balance with an alternative payment method. Primarily used with debit and prepaid cards. **IC+ pricing required; must contact sales/support to enable.**

## Availability

- Online card payments only: Visa, Mastercard, Discover, Amex
- Issuer and card type determine actual eligibility at transaction time
- **AmEx (May 2024)**: debit/prepaid only; no recurring or cross-border transactions
- **Visa**: must implement across all card types
- **Incompatible with [[stripe-overcapture]]**

## API

```js
// Enable
payment_method_options: { card: { request_partial_authorization: 'if_available' } }

// Check status on charge
charge.payment_method_details.card.partial_authorization.status
// → 'partially_authorized' | 'fully_authorized' | 'declined' | 'not_requested'

charge.payment_method_details.card.amount_requested    // original amount
charge.payment_method_details.card.amount_authorized   // amount actually approved
```

## Capture Modes

**Manual (recommended)**: review the partial amount before deciding to capture, cancel, or create a new PI for the remainder.

**Auto-capture**: Stripe automatically captures whatever was partially authorized — proceed with caution.

## Key Restrictions

- Cannot use overcapture on a partially authorized transaction
- Connect `transfer_amount` capped at partially authorized amount
- Stripe enforces minimum charge — declines if partial auth falls below minimum
- Must decide before beginning how to handle the uncovered portion (new PI, cancel, or partial capture)

## Combining with Incremental Authorization

Can request partial authorization on increments by passing `request_partial_authorization: 'if_available'` on the `increment_authorization` endpoint. The opt-in persists from initial PI confirmation unless explicitly set to `never`. See [[stripe-incremental-authorization]].

## Sources

- [[source-stripe-partial-authorization]] — full guide with API flow, manual vs auto-capture, partial + incremental combination, test cards
