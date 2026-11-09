---
title: "Redeem Credits"
type: source
date_ingested: 2026-11-09
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/advanced/credits"
raw_files:
  - "stripe-payments-advanced-credits-2026-11-07.md"
  - "stripe-checkout-redeem-credits-2025.md"
tags: [stripe, checkout-sessions, credits, store-credit, gift-card, gated]
---

## Summary

Access-gated Checkout Session credits overview for applying store credit or prepaid gift card amounts. The 2026-11-07 public capture includes an email registration example for requesting access, not a credit-operation API call or proof that access has been granted. Detailed integration guidance is not exposed here.

## Key Facts

- **Applied after** tax and shipping — reduces the net amount due
- **Stripe doesn't track credit balances** — merchant passes the available credit amount into the session
- **Reconciliation**: after session completion, retrieve session details to determine credit amount actually used
- **Use cases**: store credit, prepaid gift cards
- **Documented scope**: this page describes credits applied to a Checkout Session. The 2026-04-21 capture specifically named Elements with the Checkout Sessions API as a claim-credit route; the newer public capture does not name a UI mode. Neither capture proves that Elements is the exclusive UI or establishes a global prohibition on Payment Intents.
- **Access**: request access via the captured registration flow; submitting the example email request does not establish preview eligibility or an accepted account.

The public captures do not specify a credit-balance ledger, reservation or return behavior for failed or abandoned Sessions, redemption limits, or an account's current access. The merchant remains responsible for tracking available balances and reconciling the actual amount used after Session completion; the overview does not itself prove a credit was applied successfully.

## Related Pages

- [[stripe-checkout]] — Checkout concept page

## Raw Sources

- [[raw/stripe-payments-advanced-credits-2026-11-07|2026-11-07 credits overview and access request]] — Session-level ordering, merchant balance ownership, reconciliation, registration example

- [[raw/stripe-checkout-redeem-credits-2025|2026-04-21 credits overview]] — verbatim overview (gated feature, limited public content)
