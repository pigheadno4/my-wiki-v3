---
title: "Stripe: Google Pay"
type: source
date_ingested: 2026-11-09
original_format: webpage
canonical_url: https://docs.stripe.com/google-pay
raw_files:
  - "stripe-google-pay-2025.md"
tags: [stripe, wallets, google-pay, android, react-native, web, dpan, fpan, liability-shift, domain-registration, sigma]
---

## Summary

The 2026-11-07 base URL capture is a navigation index linking Android, React Native, and Web variants; those variant bodies were not fetched in this job. The historical 2026-05-07 combined capture contains general Google Pay properties and detailed instructions for all three routes. The integration, eligibility, testing, domain registration, and liability statements below describe that older capture, not verified current variant instructions or a guarantee that Google Pay will render for a particular buyer.

## Integration routes in the 2026-05-07 capture

- **Android**: enable `com.google.android.gms.wallet.api.enabled` in AndroidManifest.xml. `GooglePayLauncher` can confirm a PaymentIntent or SetupIntent after its readiness callback; `GooglePayPaymentMethodLauncher` collects only a PaymentMethod for later server-side confirmation. The older guide calls for production access through the Google Pay & Wallet Console, a signed release build and live keys for production testing. Its test instructions require a physical Android device in a supported country and a real card saved in Google Wallet.
- **React Native**: use `PlatformPayButton` and check `isPlatformPaySupported`; `confirmPlatformPayPayment` confirms a PaymentIntent, `confirmPlatformPaySetupIntent` is the SetupIntent route, and `createPlatformPayPaymentMethod` only collects a PaymentMethod for later confirmation. The older guide says Expo Go does not support this flow and calls for a development build. It likewise describes Google production access and physical-device testing.
- **Web**: the older guide describes Checkout and Elements, with Google Pay enabled in payment method settings. Checkout needed no additional Google Pay code in that route; Elements pointed to the Express Checkout Element or accept-a-payment guide. It required an HTTPS page with a TLS domain-validated certificate.

## Web domains and display conditions

The 2026-05-07 Web instructions say to register every domain that displays the Google Pay button in both test and production, including subdomains such as `www`. For Connect direct charges, register the domain for each connected account; the guide says that extra per-account registration is not required for other charge types. The old Web test section says a real card must first be added to the wallet for Google Pay to display and that Stripe will not render the option when device or integration requirements are unmet. These are dated instructions; the new index does not confirm current domain or browser behavior.

## Token types, disputes, and liability in the 2026-05-07 capture

The old guide distinguishes **DPAN** device cards (liability shift by default), **FPAN** cards saved in Chrome or a Google property (global liability shift with 3D Secure, including Visa), and **e-commerce tokens** (neither liability shift nor 3D Secure supported **at that time**). For Visa transactions outside a Stripe-hosted product, it instructs merchants to enable Fraud Liability Protection for Visa Device Tokens in Google Pay & Wallet Console. Sigma's `charges.card_token_type` distinguishes `fpan` from `dpan_or_ecommerce_token`. These statements are historical, conditional on token and integration path, and do not guarantee a liability outcome for a charge; the newer index contains no updated liability or 3D Secure details. The old guide also says Google Pay payments can still be disputed and successful payments can be fully or partially refunded.

## Other dated scope

The 2026-05-07 general properties describe customer and business locations as worldwide except India and refer to Stripe's supported presentment currencies rather than listing a universal currency set. They mark recurring payments, Connect, disputes, manual capture, and refunds as supported, subject to the route and payment requirements. The older in-app digital-goods statement is scoped to Android apps selling digital products, content, or subscriptions in the US or EEA, and points readers to Google Play developer terms for purchases that must use its billing system. The 2026-11-07 index does not recheck those regional, store-policy, wallet availability, or currency conditions.

## Related Pages

- [[stripe-wallets]] — main Stripe wallets concept and Google Pay token, route, and display context.
- [[stripe]] — Stripe company page.

## Raw Sources

- [[raw/stripe-google-pay-2025|2026-05-07 Google Pay combined guide]] — historical Android, React Native, and Web route instructions, general properties, tests, domain registration, token types, liability, disputes, and refunds.

## Related raw API references

- [[raw/stripe-google-pay-2026-11-07|2026-11-07 Google Pay platform index]] — navigation links to Android, React Native, and Web variants only; linked bodies were not captured.
