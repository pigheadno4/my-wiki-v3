---
title: "Stripe — Migrate Basic Card Integration (Handle Auth)"
type: source
date_ingested: 2026-05-11
original_format: webpage
raw_files:
  - "stripe-migrate-basic-card-integration-2026.md"
tags: [stripe, payment-intent, authentication, handle-card-action, confirmation-method, migration, legacy]
---

## Summary

Upgrade guide from the US/CA-only `error_on_requires_action` pattern to a global integration that handles bank authentication via modal.

## Two Server Changes

1. **Remove** `error_on_requires_action` — status becomes `requires_action` instead of failing
2. **Add** `confirmation_method: 'manual'` + `use_stripe_sdk: true`

## Flow After Migration

1. Server creates PI with `confirm: true, confirmation_method: 'manual'`
2. If `requires_action` → return `{ requiresAction: true, clientSecret }`
3. Client: `stripe.handleCardAction(clientSecret)` → shows auth modal → returns PI with `requires_confirmation`
4. Client sends `payment_intent_id` back to server
5. Server: `stripe.paymentIntents.confirm(payment_intent_id)` → must confirm within **1 hour** or fails back to `requires_payment_method`

## Same Endpoint Handles Both

Same `/pay` endpoint branches on `payment_method_id` (initial) vs `payment_intent_id` (re-confirm after auth).

## Related Pages

- [[stripe-payment-intents]] — concept page
- [[source-stripe-payments-without-auth]] — the guide this migrates from

## Raw Sources

- [[stripe-migrate-basic-card-integration-2026]] — verbatim migration guide (171 lines, 1 screenshot)
