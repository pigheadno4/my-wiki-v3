---
title: "Stripe — Finalize Payments on the Server"
type: source
date_ingested: 2026-05-11
original_format: webpage
raw_files:
  - "stripe-finalize-payments-server-2026.md"
tags: [stripe, payment-element, confirmation-token, server-side, payment-intent, setup-intent, handle-next-action]
---

## Summary

Server-side confirmation variant of the deferred intent pattern. Key difference: `paymentMethodCreation: 'manual'` + ConfirmationToken sent to server → PI created + confirmed in single server call.

## Key Difference from Deferred Intent Guide

| | Deferred (client confirm) | Finalize on server |
| --- | --- | --- |
| `paymentMethodCreation` | Not set | `'manual'` |
| ConfirmationToken | Optional (two-step) | Required |
| PI confirmation | `stripe.confirmPayment()` on client | `stripe.paymentIntents.create({ confirm: true, confirmation_token })` on server |
| Next actions | Handled by Stripe.js automatically | Manual `stripe.handleNextAction({ clientSecret })` |

## Server Flow

1. Client: `stripe.createConfirmationToken({ elements, params })` — expires in **12 hours**
2. Send `confirmationToken.id` to server
3. Server: `stripe.paymentIntents.create({ confirm: true, amount, currency, confirmation_token: id })`
4. Return `{ client_secret, status }` to client
5. If `status === 'requires_action'`: `stripe.handleNextAction({ clientSecret })`

## Setup Flow

Same but `mode: 'setup'` + `stripe.setupIntents.create({ confirm: true, confirmation_token: id })`.

## SDK Minimum Versions (for ConfirmationToken)

stripe-node v14.22.0, stripe-python v8.8.0, stripe-php v13.15.0, stripe-ruby v10.13.0, stripe-java v24.21.0, stripe-go v76.22.0, stripe-dotnet v43.20.0.

## Related Pages

- [[stripe-payment-intents]] — concept page (updated with server-side confirmation variant)
- [[source-stripe-accept-payment-deferred]] — client-side confirmation variant
- [[source-stripe-two-step-confirmation]] — two-step with review page

## Raw Sources

- [[stripe-finalize-payments-server-2026]] — verbatim server-side finalization guide (2541 lines)
