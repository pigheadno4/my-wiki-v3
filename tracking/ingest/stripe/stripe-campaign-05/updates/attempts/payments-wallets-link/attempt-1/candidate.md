---
title: "Stripe Docs — Link payment methods"
type: source
date_ingested: 2026-05-08
date_updated: 2026-11-22
original_format: webpage
raw_files:
  - "stripe-link-payment-methods-2025.md"
tags: [stripe, link, link-payment-methods, instant-bank-payments, klarna, pix, upi, stablecoins, bnpl, us-only]
---

## Summary

The May 8, 2026 [[stripe|Stripe]] capture describes alternative funding surfaced by Link on eligible checkouts for US Stripe accounts. It lists Instant Bank Payments, Klarna, Pix, UPI and stablecoins. The May and separate November US funding guides say Link can present eligible funding automatically within an existing Link integration, without separate method-specific configuration. Initial Link enablement and integration follow the broader wallet guide.

## Funding and eligibility

The May 8 funding capture recorded `https://docs.stripe.com/payments/wallets/link`. It describes five criteria Link checks per session: business eligibility, presentment currency, transaction limits, customer location, and recurring or off-session support. The customer sees the subset eligible for the session. Both US guides describe the same criteria.

The separate [[raw/stripe-payments-link-link-payment-methods-2026-11-07|November 7 US funding guide]] at [Link payment methods](https://docs.stripe.com/payments/link/link-payment-methods) describes a card classification plus four alternative funding groups. It says these groups are enabled with Link subject to eligibility.

| Group code | Funding |
| --- | --- |
| `lfsg_000` | Cards |
| `lfsg_001` | Stablecoins |
| `lfsg_002` | Pix and UPI |
| `lfsg_003` | Instant Bank Payments |
| `lfsg_004` | Klarna |

See the May funding capture at lines 6–32 and November US funding capture at lines 7–54.

## Dashboard and API representation

Both US funding guides describe Dashboard payments as either `type=link` or `type=card` with `brand=link`, depending on integration. Both are presented as Link regardless of underlying funding. The general wallet overview's PaymentMethod object fields are separately scoped. Standalone Link yields `type=link` without a wallet hash. Card-specific Link yields `type=card` and `card.wallet.type=link`.

The November US funding guide places `funding_source_group` on the Charge, at `payment_method_details.link.funding_source_group` for standalone Link or `payment_method_details.card.wallet.link.funding_source_group` for a card-specific integration. This identifies the funding group. Pix and UPI share a code. See May lines 14–16, November US funding lines 27–38, and November general overview lines 88–90.

## Customer experience and settings

For new customers, Link uses the supplied email and detected location to show eligible methods. Customers choose their method, sign up and authenticate. The guides describe immediate payment confirmation and saving the method for future use across Link-enabled merchants. Returning customers can be recognized using email, phone or browser cookie. A one-time passcode authenticates the Link session, followed by autofill of saved payment and shipping details. The separate November funding guide also documents the Dashboard **Save customer information** default selection. See May lines 34–50 and November US funding lines 56–77.

The May general disabling prose says turning off Link removes alternative funding and accelerated checkout. May separately describes individual BNPL settings and says enabling a method outside Link disables that method's Link interface and its Link saving path. The November US funding guide specifies that disabling payment methods in groups 1–3 requires turning off Link. See May lines 52–56 and November US funding lines 79–81.

## General Link wallet overview

Use [[source-stripe-link|the general Link overview]] for overall wallet availability, integration and PaymentMethod representation. The [[raw/stripe-link-2025|May 7 broad overview]] and the [[raw/stripe-payments-wallets-link-2026-11-07|November 7 full broad overview]] both record [the Link wallet overview URL](https://docs.stripe.com/payments/wallets/link). The broad guides describe Stripe account and customer reach outside India plus a Thailand and Brazil Payment Element restriction. The May 8 US funding capture records the same URL with a different body. The capture history leaves the reason for those bodies unresolved.

## Related Pages

- [[stripe-link]] — Link integration, funding and reporting
- [[stripe-wallets#Link Details|Link in Stripe Wallets]]
- [[source-stripe-link]] — general Link wallet overview
- [[stripe]] — provider overview

## Raw Sources

- [[raw/stripe-link-payment-methods-2025]] — May 8, 2026 US alternative funding guide
