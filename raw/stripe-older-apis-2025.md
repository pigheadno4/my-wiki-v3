<!-- Source URL: https://docs.stripe.com/payments/older-apis -->
<!-- Fetched: 2026-04-20 -->

# Older payment APIs

Information about our older APIs and the newer APIs that replace them.

We’ve replaced some of our older APIs and no longer update their documentation.

## Migrate to current APIs

The older APIs are limited. To get the latest Stripe features, migrate to the [Payment Intents](https://docs.stripe.com/payments/payment-intents.md), [Setup Intents](https://docs.stripe.com/payments/setup-intents.md), and [Payment Methods](https://docs.stripe.com/payments/payment-methods.md) APIs. See each individual API’s docs for specifics on migrating.

## Deprecation of the Sources API

We’ve deprecated support for local payment methods in the [Sources API](https://docs.stripe.com/sources.md) and plan to turn it off. If you currently handle any local payment methods using the Sources API, you must [migrate them to the current APIs](https://docs.stripe.com/payments/payment-methods/transitioning.md). We’ll communicate more information about this end of support through email.

We’ve also deprecated support for card payments in the Sources API, but don’t currently plan to turn it off.

## Older APIs that remain available

Although unsupported, these APIs aren’t going away. Until you upgrade your integration, you can still use these APIs:

- [Charges](https://docs.stripe.com/payments/charges-api.md)
- [ACH](https://docs.stripe.com/ach-deprecated.md)

## Comparing the APIs

| Feature                                                                                                                                                                                                                                                       | Payment Intents, Setup Intents, & Payment Methods                                                                 | Charges, Tokens, & Sources |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | -------------------------- |
| Supported payment methods                                                                                                                                                                                                                                     | [Cards, digital wallets, bank transfers, and so on](https://docs.stripe.com/payments/payment-methods/overview.md) | Cards, ACH                 |
| _SCA-ready_ (Strong Customer Authentication (SCA) is a regulatory requirement in effect as of September 14, 2019, that impacts many European online payments. It requires customers to use two-factor authentication like 3D Secure to verify their purchase) | ✓ Supported                                                                                                       | ✗ Not supported            |
| Works with [Terminal](https://docs.stripe.com/terminal.md) (in-person payments)                                                                                                                                                                               | ✓ Supported                                                                                                       | ✗ Not supported            |
| Future development                                                                                                                                                                                                                                            | ✓ Supported                                                                                                       | ✗ Not supported            |
