---
title: "Stripe — Shared Payment Tokens"
type: source
date_ingested: 2026-11-09
original_format: webpage
canonical_url: "https://docs.stripe.com/agentic-commerce/concepts/shared-payment-tokens"
raw_files:
  - "stripe-shared-payment-tokens-2026.md"
tags: [stripe, spt, shared-payment-token, agentic-commerce, payment-method, agent, seller, machine-payments]
---

## Overview

The full 2026-05-12 Stripe guide describes Shared Payment Tokens (SPTs) from both roles: an agent issues a scoped grant of a customer's payment method to a seller, and the seller receives a granted token for payment processing. That capture says SPTs are available to agents, customers, and sellers in the US; it does not establish present-day geography or account eligibility. The 2026-11-07 capture at the same base URL is a short variant index for Sellers, Agents, and Connect platforms. Its omission of detailed flows does not show that SPT functionality was removed, and the Connect variant body was not captured in this job.

## Seller perspective — May 2026 guide

- **Receive:** The agent grants a `shared_payment.granted_token` to the seller's Stripe profile, with usage and expiration limits. The seller guide says to have a Stripe account and create a Stripe profile before use.
- **Use:** The public-preview Node example calls `stripe.paymentIntents.create({ payment_method_data: { shared_payment_granted_token: 'spt_xxx' }, confirm: true })`. On confirmation, Stripe sets `payment_method` to a new PaymentMethod cloned from the customer's original method; the guide says later refunds and reporting behave as if that method were supplied directly. Token use or creation of this PaymentIntent is not proof of a succeeded or settled payment.
- **Retrieve:** The public-preview example uses `stripe.sharedPayment.grantedTokens.retrieve('spt_xxx')`; the guide says the response can expose usage limits and limited method details such as card brand and last four digits.
- **Test-mode simulation:** The guide's test-helper example, `stripe.testHelpers.sharedPayment.grantedTokens.create({ payment_method, usage_limits })`, simulates a granted SPT with a test payment method and limits.
- **Separate live-mode test:** The guide labels a Link CLI flow as testing a live-mode integration. It requires logging in to a personal Link account, selecting or adding a payment method, and creating a one-time spend request with `--credential-type shared_payment_token`, a business-profile `--network-id`, and `--request-approval`. This is not interchangeable with the test-helper simulation.
- **Webhook:** `shared_payment.granted_token.deactivated` means the granted token was revoked or expired and can no longer be used to create a payment.

## Agent perspective — May 2026 guide

- **Collect and issue:** Collect the seller's Stripe profile during onboarding. The Payment Element example uses `paymentMethodCreation: 'manual'` and `sellerDetails.networkBusinessProfile` to present buyer methods compatible with that seller, then `stripe.preparePaymentMethod({ elements })` and the server-side public-preview `stripe.sharedPayment.issuedTokens.create(...)` example. The issued token carries the seller profile and limits for currency, maximum amount, and expiration; the agent shares its ID with the seller for a transaction. The guide requires HTTPS before accepting live payments.
- **Methods in the May capture:** Its table lists cards, Link, Apple Pay, Google Pay, Klarna, and limited Affirm. The card-network footnote says Stripe might use Mastercard Agent Pay or Visa Intelligent Commerce network tokens on the agent's behalf. For Affirm, the buyer must navigate and confirm the loan-application UI; the agent might not interact with it programmatically or render it on a device browser outside its navigation control. Affirm marketing by an agent carries separate compliance guidance. The November index does not update this support list.
- **Next actions and revocation:** A seller payment can put the issued token into `requires_action` for 3DS or another customer redirect. The agent retrieves the token and presents the action; the guide's client example calls `stripe.handleNextAction(...)`. The `active` event follows completed customer action unless the token was deactivated, meaning the SPT can continue through the payment flow. The agent can revoke it, preventing seller use.
- **Agent events:** `shared_payment.issued_token.requires_action`, `.active`, `.used`, and `.deactivated` distinguish customer action, renewed token usability, seller use, and revocation/expiry. The May table defines `.used` as seller use of the SPT; it does not establish that a PaymentIntent succeeded or settled. Check payment outcome separately.

## Detail locators

- Seller prerequisites, test helper, distinct live-mode Link CLI flow, PaymentIntent example, retrieval, and seller webhook: [[raw/stripe-shared-payment-tokens-2026|May full guide]], lines 8–139.
- Agent profile and payment collection, issued-token example, method table and Affirm footnotes, next actions, revocation, and agent webhooks: same May guide, lines 141–431. The Node snippets identify the public-preview SDK; they are examples, not proof of current SDK or account access.

## Related

- [[stripe]]; [[stripe-shared-payment-tokens]]; [[stripe-agentic-commerce]]; [[stripe-machine-payments]]

## Related raw API references

The [[raw/stripe-agentic-commerce-concepts-shared-payment-tokens-2026-11-07|November 7, 2026 base-URL index]] provides navigation only; these variant bodies were not read for this source update:

- [Sellers](https://docs.stripe.com/agentic-commerce/concepts/shared-payment-tokens.md?agent-seller=seller)
- [Agents](https://docs.stripe.com/agentic-commerce/concepts/shared-payment-tokens.md?agent-seller=agent)
- [Connect platforms](https://docs.stripe.com/agentic-commerce/concepts/shared-payment-tokens.md?agent-seller=connect)

## Raw Sources

- [[raw/stripe-shared-payment-tokens-2026|May 12, 2026 full seller and agent guide]]
