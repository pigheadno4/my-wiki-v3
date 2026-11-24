---
title: "Stripe Terminal: Save Directly Without Charging"
type: source
date_ingested: 2026-05-01
date_updated: 2026-11-24
original_format: webpage
canonical_url: "https://docs.stripe.com/terminal/features/saving-payment-details/save-directly"
raw_files:
  - "stripe-terminal-save-directly-2025.md"
tags: [stripe, stripe-terminal, saved-payment-methods, generated-card, setup-intents, allow-redisplay, compliance]
---

## Summary

The 2026-05-01 [[stripe]] Terminal guide describes saving details from a present card or mobile wallet for online reuse without charging, using a SetupIntent. The 2026-11-07 capture retains that purpose and indexes the Server-driven, JavaScript, iOS, Android, and React Native variants. The variant bodies are outside that capture. The integration details below come from the 2026-05-01 guide.

## Key Takeaways

- **CNP reuse**. Charges using a reusable `generated_card` are card-not-present (CNP). Card-present liability shift and pricing do not apply.
- **Card networks**. The guide lists Visa, Mastercard, Amex, Discover, and co-branded Interac, eftpos, and girocard. Co-branded Interac must be inserted into a reader and is unsupported by Tap to Pay. The guide excludes single-branded Interac, eftpos, and girocard.
- **Setup flow**. Create or retrieve the customer. Server-driven and JavaScript integrations create the SetupIntent on the server with `card_present` in `payment_method_types`. JavaScript passes its client secret to the client. iOS, Android, and React Native can create through the SDK or create on the server and retrieve through the SDK using the client secret. Obtain the customer’s explicit consent before collecting encrypted payment details through the reader and confirming the SetupIntent.
- **Consent and `allow_redisplay`**. The historical deadlines for replacing `customer_consent_collected` were March 31, 2025 for non-React Native integrations and September 30, 2025 for React Native. Use the consent-appropriate value, `always` for display in any checkout flow or `limited` for restricted display. The guide calls for opt-in terms, written agreement records, and use only for the agreed purpose. See the Compliance section of the 2026-05-01 guide for off-session terms.
- **`usage=on_session`**. The guide specifies this setting for checkout-only reuse.
- **Accounts v2**. At the 2026-05-01 capture, Stripe recommended customer-configured Account objects for most use cases. Accounts v2 was generally available for Connect users and in public preview for other Stripe users, with a preview version required for preview users.

## SDK Compatibility

| Integration | Reader models named for this variant | Collection and confirmation in the 2026-05-01 guide |
| --- | --- | --- |
| Server-driven | BBPOS WisePOS E, Stripe Reader S700/S710 | The `process_setup_intent` endpoint handles both steps |
| JavaScript | Unspecified | Separate `collectSetupIntentPaymentMethod` and `confirmSetupIntent` calls |
| iOS | Unspecified | SDK 5.0.0 combines both steps in `processSetupIntent` |
| Android | Unspecified | SDK 5.0.0 combines both steps in `processSetupIntent` |
| React Native | Unspecified | SDK 0.0.1-beta.29 offers combined `processSetupIntent`. The guide also documents separate collection and confirmation |

The platform sections of the 2026-05-01 guide contain their respective cancellation examples. For separately documented iOS and Android SDK 6.0.0 consent and model migrations, see [[stripe-terminal-save-payment-details]].

## Retrieving the generated_card

After successful setup, the SetupIntent status is `succeeded`. Check `SetupAttempt.payment_method_details.card_present.generated_card` for the reusable `card` PaymentMethod. The value can be empty for unsupported methods. The `card_present` PaymentMethod in `SetupIntent.payment_method` represents the physically presented instrument and cannot be charged online.

Attach an available `generated_card` to the Customer before reuse. It attaches automatically after successful setup when the Customer was supplied at SetupIntent creation. Otherwise, attach it in a separate call. Expand `latest_attempt` on the SetupIntent or list the Customer’s attached PaymentMethods with `type: 'card'`.

## Mobile Wallets

- Saved mobile wallets are off-session only and their `generated_card` has `allow_redisplay=limited`.
- Pass `off_session=true` at PaymentIntent confirmation for a saved mobile wallet charge.
- If the customer is present in the checkout flow, use Apple Pay or Google Pay to prompt for payment method presentment.

## See Also

- [[stripe-terminal-save-payment-details]] — concept page
- [[source-stripe-terminal-save-payment-details]] — overview source

## Raw Sources

- [[raw/stripe-terminal-save-directly-2025|Stripe Terminal integration guide captured 2026-05-01]] — five platform bodies

## Related raw API references

- [[raw/stripe-terminal-features-saving-payment-details-save-directly-2026-11-07|Stripe Terminal save-directly platform variant index captured 2026-11-07]]
