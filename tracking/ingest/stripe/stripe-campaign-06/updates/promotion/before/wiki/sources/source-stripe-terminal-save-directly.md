---
title: "Stripe Terminal: Save Directly Without Charging"
type: source
date_ingested: 2026-05-01
original_format: webpage
raw_files:
  - "stripe-terminal-save-directly-2025.md"
tags: [stripe, stripe-terminal, saved-payment-methods, generated-card, setup-intents, allow-redisplay, compliance]
---

## Summary

Detailed integration guide for saving card-present payment methods without charging, using SetupIntents. Covers the full 5-platform implementation (server-driven, JS, iOS, Android, React Native), card network support, `allow_redisplay` consent model, and mobile wallet caveats.

## Key Takeaways

- **generated_card is CNP**: all charges via `generated_card` are card-not-present — no liability shift, no card-present pricing
- **Card network support**: Visa, Mastercard, Amex, Discover, co-branded Interac/eftpos/girocard (must be inserted, not tapped — so Tap to Pay doesn't support co-branded Interac). Single-branded Interac, eftpos, girocard are NOT supported
- **3-step flow**: Create/retrieve Customer → Create SetupIntent (with `card_present` in `payment_method_types`) → Collect + confirm (combined in newer SDK versions)
- **`allow_redisplay` required** (replacing legacy `customer_consent_collected`): mandatory since March 31, 2025 for non-React Native; Sept 30, 2025 for React Native. Values: `always` (can show in any checkout flow) or `limited`
- **`usage=on_session`**: specify if only reusing when customer is present in checkout flow
- **Accounts v2**: generally available for Connect users, public preview for others; recommend modeling customers as customer-configured Account objects

## SDK Compatibility

| SDK | Compatible readers | Notes |
| --- | --- | --- |
| Server-driven | WisePOS E, S700/S710 | Uses `process_setup_intent` API endpoint |
| JavaScript | All | Uses `collectSetupIntentPaymentMethod` + `confirmSetupIntent` separately |
| iOS 5.0.0+ | All | `processSetupIntent` combines collect + confirm in one step |
| Android 5.0.0+ | All | `processSetupIntent` combines collect + confirm in one step |
| React Native 0.0.1-beta.29+ | All | `processSetupIntent` available; older versions use separate collect + confirm |

## Retrieving the generated_card

After successful setup, retrieve via `SetupAttempt.payment_method_details.card_present.generated_card`. Always check for a value — not all payment methods support generated cards.

Options:
1. Expand `latest_attempt` on the SetupIntent
2. List payment methods on the Customer (`type: 'card'`)
3. If no Customer provided during SetupIntent creation, attach `generated_card` to Customer in a separate call

Note: `SetupIntent.payment_method` is the `card_present` PaymentMethod (not chargeable online) — the `generated_card` is the separate reusable `card` PaymentMethod.

## Mobile Wallets

- Saved mobile wallets → `generated_card` with `allow_redisplay=limited` (off-session only)
- Must pass `off_session=true` when charging a saved mobile wallet
- If customer is present in checkout flow: use Apple Pay or Google Pay integrations directly instead of the saved wallet

## See Also

- [[stripe-terminal-save-payment-details]] — concept page
- [[source-stripe-terminal-save-payment-details]] — overview source

## Raw Sources

- [[stripe-terminal-save-directly-2025]] — verbatim webpage content (5 SDK platforms)
