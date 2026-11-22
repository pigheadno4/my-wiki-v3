---
title: "Stripe Partial Authorization"
type: concept
category: technology
tags: [stripe, partial-authorization, capture, payment-intents, ic-plus, debit, prepaid]
---

## Overview

Partial authorization lets a supporting issuer approve less than the requested online card payment when the cardholder's available balance is insufficient. Before using partial authorization, decide whether to take another payment for the remainder, cancel the original Intent, or capture up to the partial approval. Explain the choice to the customer. IC+ pricing and Stripe sales or Support enablement apply.

## Availability

- Online card payments only: Visa, Mastercard, Discover, Amex
- Issuer and card type determine actual eligibility at transaction time
- **AmEx (May 2024)**: debit/prepaid only; no recurring or cross-border transactions
- **Visa (May 2024 example)**: the guide says to use the feature across card types
- [[stripe-overcapture]] cannot capture above the approved amount on a partially authorized transaction.

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

**Auto-capture**: This optional flow automatically captures a partial approval without a separate merchant capture decision and can capture less than the order needs. The samples capture only the 70 USD partially authorized on a 100 USD request. The May and November partial-authorization guides describe explicit `automatic` or omission, and the omitted-field examples show `automatic` in the response. The separate November Create PaymentIntent reference lists `automatic_async` as its general default. The examples do not establish which default applies across accounts or versions, or partial-authorization support under `automatic_async`. See [[source-stripe-partial-authorization]].

## Key Restrictions

- Cannot use overcapture on a partially authorized transaction
- Connect `transfer_amount` capped at partially authorized amount
- Stripe enforces minimum charge — declines if partial auth falls below minimum
- Must decide before beginning how to handle the uncovered portion (new PI, cancel, or partial capture)

## Combining with Incremental Authorization

Confirm an uncaptured PaymentIntent with the separate incremental authorization request and check for `available` on the latest Charge. On the increment, send the desired total and `request_partial_authorization=if_available` to allow partial approval. The initial partial opt-in persists unless overridden with `never`. Capture remains separate. See [[stripe-incremental-authorization]].

## Sources

- [[source-stripe-partial-authorization]] — May and November 2026 guides to issuer/card scope, manual and automatic capture, versioned request examples and partial increments.
