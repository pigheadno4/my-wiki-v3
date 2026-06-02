---
title: "Payment Sheet"
type: source
date_ingested: 2026-04-22
original_format: webpage
raw_files:
  - "stripe-inapp-payment-sheet-2025.md"
tags: [stripe, mobile, ios, android, react-native, payment-sheet, appearance-api, saved-payment-methods, wallets, card-brand-filtering]
---

## Summary

Detailed reference for the Payment Sheet UI — Stripe's recommended prebuilt mobile payment UI. Covers layout options, Appearance API, payment methods, wallets, saved PMs, address collection, and additional features. Supplementary to [[source-stripe-inapp-payments-overview]].

## Layout Options

`.automatic` — Stripe picks the best layout
`.vertical` — vertical list
`.horizontal` — horizontal scroll

![Layout options](../raw/assets/stripe-inapp-ps-layout.png)

## Appearance API

Colors, fonts, borders, shadows all configurable. 50+ aspects.

![Appearance examples](../raw/assets/stripe-inapp-ps-appearance.png)

## Payment Methods

100+ payment methods. Payment Sheet handles all collection forms (localized, kept up-to-date by Stripe). Enable via Dashboard or [Custom Payment Methods](https://docs.stripe.com/payments/payment-methods/custom-payment-methods.md).

![Payment methods examples](../raw/assets/stripe-inapp-ps-payment-methods.png)

## Wallets

Apple Pay, Link (Stripe wallet), and others via express buttons.

![Wallets example](../raw/assets/stripe-inapp-ps-wallets.png)

## Saved Payment Methods

Supports: **cards**, **US bank accounts**, **SEPA debit**. Consent collection automatic. CustomerSessions API controls visibility/removal behavior.

![Saved payment methods](../raw/assets/stripe-inapp-saved-payment-methods.png)

## Address Collection

Configurable: name, email, phone, billing address — regardless of payment method chosen.

![Address collection example](../raw/assets/stripe-inapp-ps-address-collection.png)

## Additional Features

- **CVC recollection**: Configure whether CVC re-collection is required when paying with a saved card
- **Card brand filtering**: Configure which card brands you accept

## Related Pages

- [[stripe-inapp-payments]] — concept page
- [[source-stripe-inapp-payments-overview]] — overview source

## Raw Sources

- [[stripe-inapp-payment-sheet-2025]] — verbatim Payment Sheet reference (92 lines, 8 images)
