---
title: "Stripe Klarna"
type: concept
category: framework
tags: [stripe, klarna, bnpl, subscriptions, payment-methods, checkout, payment-element, mandate, 23-countries]
---

## Overview

Klarna is a Buy Now Pay Later (BNPL) payment method on Stripe. Customers authenticate and select repayment options (Pay Now, Pay Later, Pay in installments) through a Klarna-hosted redirect, subject to their use case and buyer country. The 2026-05-13 subscription guide includes sandbox test data for 23 customer countries; this does not establish current merchant or buyer eligibility. The guide describes subscription integrations.

**Important**: Payment options available to customers vary by use case and buyer country — check Klarna's supported options before integrating.

## May 2026 sandbox country data (23)

The dated subscription guide gives test inputs for AU, AT, BE, CA, CZ, DK, FI, FR, DE, GR, IE, IT, NL, NZ, NO, PL, PT, RO, ES, SE, CH, UK and US. This is a sandbox test list, not a current eligibility matrix; Klarna options vary by use case and buyer country.

## Subscription integration

Stripe recommends **Checkout** for Klarna subscriptions.

### Checkout (recommended)

The May 2026 guide creates a Checkout Session with `mode='subscription'` and at least one recurring Price; its sample omits `payment_method_types`, without establishing a universal override rule. Retrieve the created subscription through `checkout.session.completed`, or retrieve and verify the Session server-side if the buyer returns. A visit to `success_url` alone does not prove payment or justify access.

> [!warning] Contradiction
> The guide's Session-creation request uses `mode='subscription'`, but its illustrative `checkout.session.completed` payload says `mode: "setup"`. Treat the payload as an inconsistent example, not a subscription-mode instruction. See [[source-stripe-subscriptions-klarna]].

Supports trial periods via `subscription_data.trial_period_days` or `trial_end`.

### Payment Element (advanced)

In the May 2026 advanced example, create an incomplete subscription with `payment_behavior=default_incomplete` and `save_default_payment_method='on_subscription'`, then mount the Payment Element. Its `stripe.confirmPayment` call passes `elements` and `confirmParams` with `return_url` and example `mandate_data`; Klarna redirects the buyer. On return, check the PaymentIntent and call payment successful and the subscription active only if its status is `succeeded`. The example does not impose those confirm parameters on hosted Checkout.

## Testing

- **Cookie-based**: log out of Klarna sandbox between different country test sessions
- **Email controls outcome**: `customer@email.{country}` = approve; `customer+denied@email.{country}` = deny
- **Two-step auth**: any 6-digit code passes; `999999` = fail
- **Repayment options in test flow**: Direct Debit, Bank transfer, Credit/Debit cards

Full per-country test data (name, DOB, address, phone for 23 countries) in [[source-stripe-subscriptions-klarna]].

## Sources

- [[source-stripe-subscriptions-klarna]] — 2026-05-13 Klarna subscription guide: hosted Checkout and advanced Payment Element; 2026-11-07 capture is a variant index; country tables are sandbox test data
