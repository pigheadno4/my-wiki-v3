---
title: "Stripe — Shared Payment Tokens"
type: source
date_ingested: 2026-05-12
original_format: webpage
raw_files:
  - "stripe-shared-payment-tokens-2026.md"
tags: [stripe, spt, shared-payment-token, agentic-commerce, payment-method, agent, seller, machine-payments]
---

## Summary

Full reference for Shared Payment Tokens (SPTs) covering both perspectives: sellers (receive and use SPTs) and agents (issue SPTs). US only.

## Seller Perspective

**Receive**: Agent grants `shared_payment.granted_token` scoped to seller's Stripe profile with usage limits.

**Use**: `stripe.paymentIntents.create({ payment_method_data: { shared_payment_granted_token: 'spt_xxx' }, confirm: true })` — Stripe clones the customer PM; refunds/reporting behave as if PM was provided directly.

**Retrieve**: `stripe.sharedPayment.grantedTokens.retrieve('spt_xxx')` → usage_limits, card brand, last4.

**Test**: `stripe.testHelpers.sharedPayment.grantedTokens.create({ payment_method, usage_limits })` OR `link-cli spend-request create --credential-type shared_payment_token --network-id profile_xxx`

**Webhook**: `shared_payment.granted_token.deactivated`

## Agent Perspective

**Collect seller profile**: `network_business_profile` from seller's Stripe profile.

**Collect payment method**: Payment Element with `paymentMethodCreation: 'manual'` + `sellerDetails: { networkBusinessProfile }` → shows buyer-compatible payment methods; `stripe.preparePaymentMethod({ elements })`.

**Issue SPT**: `stripe.sharedPayment.issuedTokens.create({ payment_method, seller_details: { network_business_profile }, usage_limits: { currency, max_amount, expires_at }, return_url })`

**Supported payment methods**: Cards (Mastercard Agent Pay / Visa Intelligent Commerce), Link, Apple Pay, Google Pay, Klarna, Affirm (limited).

**Handle next actions**: `shared_payment.issued_token.requires_action` → `stripe.handleNextAction({ hashedValue: next_action.use_stripe_sdk.value })` → `shared_payment.issued_token.active`

**Revoke**: `stripe.sharedPayment.issuedTokens.revoke('spt_xxx')`

**Agent webhooks**: `requires_action`, `active`, `used`, `deactivated`

**Test seller profile**: `profile_test_61TU90nIeGjU7NNVXA6TU90m7ISQWsBxpcx9lASWWXTk`

## Related Pages

- [[stripe-shared-payment-tokens]] — concept page
- [[stripe-agentic-commerce]] — ACS context
- [[stripe-machine-payments]] — machine payments using SPTs

## Raw Sources

- [[stripe-shared-payment-tokens-2026]] — verbatim SPT guide, seller + agent perspectives (431 lines)
