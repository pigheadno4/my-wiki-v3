---
title: "Stripe Terminal: Save Payment Details After Payment"
type: source
date_ingested: 2026-05-01
original_format: webpage
raw_files:
  - "stripe-terminal-save-after-payment-2025.md"
tags: [stripe, stripe-terminal, saved-payment-methods, generated-card, setup-future-usage, allow-redisplay, compliance]
---

## Summary

Integration guide for saving card-present payment methods as part of an in-person payment (charge and save in one flow). Covers all 5 SDK platforms, the `setup_future_usage` mechanism, `allow_redisplay` consent, `generated_card` retrieval, and fallback when no generated card is produced.

## Key Takeaways

- **One-flow save**: set `setup_future_usage` (`on_session` or `off_session`) on the PaymentIntent at creation to request a `generated_card`; the card is charged and saved in a single transaction
- **Initial payment is card-present; follow-ups are CNP**: subsequent `generated_card` charges have no liability shift and no card-present pricing
- **`allow_redisplay` at collect time**: passed via `processPaymentIntent`/`collectPaymentMethod`, not at PaymentIntent creation
- **`generated_card` access**: expand `latest_charge` on the PaymentIntent → `payment_method_details.card_present.generated_card`; if Customer ID was provided at PaymentIntent creation, generated card auto-attaches to the Customer
- **Not always produced**: digital wallets and single-branded Interac/eftpos/girocard don't produce a `generated_card` — always verify before relying on it

## Supported Card Networks

Visa, Mastercard, Amex, Discover, co-branded eftpos, co-branded Interac, co-branded girocard.

## When generated_card Is Absent (Fallback)

1. Prompt customer to save a different payment method via the [save directly (SetupIntent) flow](https://docs.stripe.com/terminal/features/saving-payment-details/save-directly.md)
2. Refund the in-person payment, indicate failure, and instruct customer to use a different method

## SDK Notes

| SDK | Notes |
| --- | --- |
| Server-driven | Two options: `process_payment_intent` (one-step) or `collect_payment_method` + `confirm_payment_intent` (two-step, gives card brand/funding access before confirming) |
| JavaScript | `collectPaymentMethod` with `config_override: { allow_redisplay }` |
| iOS | `collectPaymentMethod` — requires iOS SDK v4.3.0+ |
| Android | `collectPaymentMethod` — requires Android SDK v4.0.0+ |
| React Native | `collectPaymentMethod` with `allowRedisplay` |

## Customer/Account Creation

Accounts v2 (preferred): `stripe.v2.core.accounts.create()` with `configuration.customer` object. Generally available for Connect users; public preview for others.

Customers v1: `stripe.customers.create()` — returns a `Customer` object with an `id` to store for later.

## See Also

- [[stripe-terminal-save-payment-details]] — concept page
- [[source-stripe-terminal-save-directly]] — companion source: save without charging (SetupIntent flow)

## Raw Sources

- [[stripe-terminal-save-after-payment-2025]] — verbatim webpage content (5 SDK platforms)
