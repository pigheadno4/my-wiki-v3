---
title: "Stripe Terminal: Save Payment Details After Payment"
type: source
date_ingested: 2026-05-01
date_updated: 2026-11-24
original_format: webpage
canonical_url: "https://docs.stripe.com/terminal/features/saving-payment-details/save-after-payment"
raw_files:
  - "stripe-terminal-save-after-payment-2025.md"
tags: [stripe, stripe-terminal, saved-payment-methods, generated-card, setup-future-usage, allow-redisplay, compliance]
---

## Summary

The full 2026-05-01 [[stripe|Stripe]] Terminal guide explains how to request a reusable payment method as part of an in-person payment. It covers Server-driven, JavaScript, iOS, Android and React Native variants, including customer consent, `generated_card` retrieval and conditional fallback. The 2026-11-07 capture is a navigation index for those five variants. The implementation guidance below comes from the May capture.

## Key Takeaways

- **One-flow save** — Create the `card_present` PaymentIntent with `setup_future_usage` to request a `generated_card`. Use `on_session` for reuse only with the customer present and `off_session` otherwise.
- **Initial payment and follow-up charges** — The in-person payment is card-present. Subsequent `generated_card` charges are card-not-present and lack card-present liability-shift and pricing benefits.
- **Consent and `allow_redisplay`** — After the customer consents to saving, pass `always` or `limited` at collection or processing. The guide dates the requirement to March 31, 2025 for non-React Native integrations and September 30, 2025 for React Native.
- **`generated_card` retrieval** — A successful payment with a future-use-capable method returns a PaymentIntent in `requires_capture` or `succeeded`. Expand `latest_charge` and check `payment_method_details.card_present.generated_card` for the distinct reusable `card` PaymentMethod. The method attaches automatically if the customer ID was supplied at creation. Otherwise, attach it separately.
- **Availability** — Verify that `generated_card` is present. Some digital-wallet and single-branded Interac, eftpos or girocard payments might produce none.
- **Saved mobile wallets** — The May guide restricts them to off-session reuse. Their `generated_card` has `allow_redisplay=limited`. Pass `off_session=true` when confirming the later PaymentIntent. When the customer is present, the guide directs you to re-prompt with the Apple Pay or Google Pay integration.

## Supported Card Networks

Visa, Mastercard, Amex, Discover, co-branded eftpos, co-branded Interac, co-branded girocard.

## When generated_card Is Absent (Fallback)

If a reusable payment method is required, the May guide offers two options.

- Ask the customer to save a different method via the [save directly (SetupIntent) flow](https://docs.stripe.com/terminal/features/saving-payment-details/save-directly.md).
- Refund the in-person payment, indicate the transaction failed, and ask the customer to use a different method.

## SDK Notes

| SDK | Notes |
| --- | --- |
| Server-driven | The May guide specifies `Stripe-Version: 2024-09-30.acacia` for this feature. Use `process_payment_intent`, or use Preview `collect_payment_method` to access card brand or funding before separately calling `confirm_payment_intent`. |
| JavaScript | `collectPaymentMethod` with `config_override: { allow_redisplay }` |
| iOS | `collectPaymentMethod` — requires iOS SDK v4.3.0+ |
| Android | `collectPaymentMethod` — requires Android SDK v4.0.0+ |
| React Native | `collectPaymentMethod` with `allowRedisplay` |

## Customer/Account Creation

The May guide recommends `stripe.v2.core.accounts.create()` with `configuration.customer` for most use cases. It describes Accounts v2 as generally available for Connect users and in public preview for other Stripe users, with a preview API version required for preview participants.

Customers v1: `stripe.customers.create()` — returns a `Customer` object with an `id` to store for later.

## See Also

- [[stripe-terminal-save-payment-details]] — concept page
- [[source-stripe-terminal-save-directly]] — companion source: save without charging (SetupIntent flow)

## Raw Sources

- [[raw/stripe-terminal-save-after-payment-2025|2026-05-01 Stripe Terminal save-after-payment guide]] — full implementation guide for five variants

## Related raw API references

- [[raw/stripe-terminal-features-saving-payment-details-save-after-payment-2026-11-07|2026-11-07 save-after-payment variant index]] — navigation to Server-driven, JavaScript, iOS, Android and React Native
