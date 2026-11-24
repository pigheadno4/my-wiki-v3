---
title: "Stripe: Secure Remote Commerce Program Guide"
type: source
date_ingested: 2026-05-08
date_updated: 2026-11-24
original_format: webpage
canonical_url: "https://docs.stripe.com/secure-remote-commerce"
raw_files:
  - "stripe-secure-remote-commerce-2025.md"
tags: [stripe, src, click-to-pay, masterpass, visa-checkout, card-networks, checkout]
---

## Summary

The 2026-05-08 [[stripe]] program guide covers accepting Secure Remote Commerce (SRC), or Click to Pay, in an existing Stripe integration. It describes US-only Stripe availability and recommends that existing Visa Checkout or Masterpass integrations migrate to SRC. Users can enroll Visa, Mastercard, American Express and Discover cards for Click to Pay. The 2026-11-07 capture corroborates the guide and reformats its examples.

## Key Details

> **Masterpass deprecation and onboarding.** Both dated guides say Mastercard deprecated Masterpass, the Dashboard cannot generate new Masterpass Checkout IDs, and Stripe was working to re-enable SRC onboarding. The same guides retain a legacy instruction to generate a Checkout ID. The documented flow below assumes an existing ID. The guides establish no new-account onboarding path or reopening date.

## Existing Checkout ID Flow

1. Use the existing Masterpass Checkout ID and the configured sandbox and production callback URLs. Load the corresponding Mastercard `merchant.js` script.
2. The browser button invokes `masterpass.checkout` with `checkoutId`, the merchant’s `allowedCardTypes`, the decimal `amount`, `currency`, and a unique `cartId`. The optional `callbackUrl` overrides the configured default. See [Mastercard’s checkout parameters](https://developer.mastercard.com/documentation/masterpass-merchant-integration-v7/7#standard-checkout1).
3. The customer selects or enters a payment method on the Mastercard site. Mastercard redirects to the merchant’s callback and appends the `oauth_verifier` query parameter.
4. In the legacy example, the merchant confirms the PaymentIntent created at the start of checkout. The example sets `payment_method_data.type` to `card` and places `cart_id` and `transaction_id` in `payment_method_data.card.masterpass`, using `oauth_verifier` for `transaction_id`. The callback’s success text is example output.

The parameter tables use `en_US`, while the HTML snippets use `en_us`. Both snippets labeled as black and white button variants use the same `src_mark_hor_blk.svg` asset. The captures leave runtime locale casing and any distinct white-mark asset unresolved.

> **Dated Confirm payload difference.** Both SRC examples also send top-level `amount` and `currency`. The separately captured [[raw/stripe-api-payment-intents-confirm-2026-11-07|November PaymentIntents Confirm reference]] lists optional `amount_to_confirm` and `payment_method_data` (lines 403–410 and 621–625) and omits top-level `amount` and `currency` from its parameter list. The captures leave acceptance of the legacy inputs and any required migration unresolved.

## Testing

The guides describe a Mastercard sandbox checkout with an SRC test user and a [Mastercard test card](https://developer.mastercard.com/masterpass/documentation/migration/masterpass_to_src_migration/#mastercard-test-cards). Serve the page over HTTP or HTTPS. Filesystem serving is unsupported, including during testing.

## Related

- [[stripe-payment-methods]] — payment method families and dated availability
- [[source-stripe-payment-intents]] — PaymentIntent lifecycle and confirmation context

## Raw Sources

- [[raw/stripe-secure-remote-commerce-2025|Stripe Secure Remote Commerce program guide captured 2026-05-08]]

## Related raw API references

- [[raw/stripe-secure-remote-commerce-2026-11-07|Stripe Secure Remote Commerce program guide captured 2026-11-07, corroborating reference]]
