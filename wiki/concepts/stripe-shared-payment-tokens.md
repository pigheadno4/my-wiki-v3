---
title: "Stripe Shared Payment Tokens (SPT)"
type: concept
category: technology
tags: [stripe, spt, shared-payment-token, agentic-commerce, agent, seller, machine-payments]
---

## Overview

A **Shared Payment Token (SPT)** is a scoped, time-limited grant of a customer's payment method from an agent to a seller. The agent controls the scope (max amount, expiration, currency); the seller uses the SPT to create a PaymentIntent without ever seeing the raw payment method. US only.

Two API objects:
- `shared_payment.issued_token` — the agent's view (they issue it)
- `shared_payment.granted_token` — the seller's view (they receive it)

## Seller Flow

```js
// Use the SPT to charge
stripe.paymentIntents.create({
  payment_method_data: { shared_payment_granted_token: 'spt_xxx' },
  confirm: true
})
// Stripe clones the PM → refunds/reporting work normally
```

Test with: `stripe.testHelpers.sharedPayment.grantedTokens.create({ payment_method, usage_limits })`

Seller webhook: `shared_payment.granted_token.deactivated`

## Agent Flow

```js
// 1. Collect PM via Payment Element (sellerDetails filters compatible methods)
stripe.preparePaymentMethod({ elements })

// 2. Issue SPT to seller
stripe.sharedPayment.issuedTokens.create({
  payment_method: 'pm_xxx',
  seller_details: { network_business_profile: 'profile_xxx' },
  usage_limits: { currency: 'usd', max_amount: 1000, expires_at: timestamp },
  return_url: 'https://...'
})

// 3. Handle next actions (3DS, redirects)
stripe.handleNextAction({ hashedValue: next_action.use_stripe_sdk.value })

// 4. Revoke if needed
stripe.sharedPayment.issuedTokens.revoke('spt_xxx')
```

At the retained `@stripe/link-cli@0.13.0` baseline, a consumer-side agent can also obtain an SPT from a Link wallet for a Stripe MPP `402` challenge. `link-cli mpp pay` extracts the challenge's network ID and amount, creates a user-approved spend request, retrieves the SPT, and retries with the payment credential. The SPT is one-time use; a failed payment requires a new spend request.

## Supported Payment Methods

Cards (Mastercard Agent Pay / Visa Intelligent Commerce), Link, Apple Pay, Google Pay, Klarna, Affirm (limited — no programmatic UI interaction).

## Agent Webhooks

| Event | Meaning |
| --- | --- |
| `requires_action` | Customer must complete 3DS/redirect |
| `active` | Required action completed |
| `used` | Seller charged the SPT |
| `deactivated` | Revoked or expired |

## Usage Limits

Agent sets `max_amount`, `currency`, `expires_at`. Usage limits enforce the transaction scope — seller can't exceed them.

## Sources

- [[source-stripe-shared-payment-tokens]] — full seller + agent integration guide with code
- [[source-github-link-cli]] — package-qualified Link CLI implementation of approval-gated SPT issuance and MPP payment
