<!-- Source URL: https://docs.stripe.com/apple-pay/cartes-bancaires -->
<!-- Fetched: 2026-05-07 -->

# Cartes Bancaires with Apple Pay

Learn how to integrate Cartes Bancaires with Apple Pay.

> Stripe only supports EUR payments for Cartes Bancaires with Apple Pay.

Use this guide to enable the [Cartes Bancaires](https://docs.stripe.com/payments/cartes-bancaires.md) payment method in your Apple Pay integration.

# iOS

> This is a iOS for when platform is ios. View the full page at https://docs.stripe.com/apple-pay/cartes-bancaires?platform=ios.

## Before you begin

To avoid issues with failed payments, take the following steps:

- Add Cartes Bancaires to your list of enabled networks only if the transaction is in Euros.
- Only enable Cartes Bancaires with Apple Pay if you support charges through Cartes Bancaires.
- If you’re a platform using the [on_behalf_of](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-on_behalf_of) parameter, make sure that the `on_behalf_of` account supports Cartes Bancaires charges. Check an account’s eligibility using the [Capabilities API](https://docs.stripe.com/api/capabilities.md).

## Set up Stripe

First, you need a Stripe account. [Register now](https://dashboard.stripe.com/register).

## Accept Apple Pay

Follow the [Apple Pay guide](https://docs.stripe.com/apple-pay.md?platform=ios) to start accepting Apple Pay.

## Add Cartes Bancaires as an enabled network

When your app starts, configure the SDK with Cartes Bancaires as an enabled Apple Pay network.

#### Swift

```swift
StripeAPI.additionalEnabledApplePayNetworks = [.cartesBancaires]
```

## Test Apple Pay

Apple Pay Wallet can’t save Stripe test card information. Instead, Stripe recognizes when you’re using your test API keys and provides a successful test card token for you to use. This allows you to make test payments using a live card without any charges being applied.

Make sure you test using a Cartes Bancaires card obtained from one of the [Apple Pay participating banks](https://support.apple.com/en-us/109516).

# Web

> This is a Web for when platform is web. View the full page at https://docs.stripe.com/apple-pay/cartes-bancaires?platform=web.

## Set up Stripe

First, you need a Stripe account. [Register now](https://dashboard.stripe.com/register).

## Accept Apple Pay

Follow the [Apple Pay guide](https://docs.stripe.com/apple-pay.md?platform=web) to start accepting Apple Pay.

## Use a supported web Element

Stripe automatically supports Cartes Bancaires on Apple Pay using the following Elements:

- [Payment Element](https://docs.stripe.com/payments/payment-element.md)
- [Express Checkout Element](https://docs.stripe.com/elements/express-checkout-element.md)
- [Checkout](https://docs.stripe.com/payments/checkout.md)
- [Payment Request Button](https://docs.stripe.com/stripe-js/elements/payment-request-button.md)

## Test Apple Pay

Apple Pay Wallet can’t save Stripe test card information. Instead, Stripe recognizes when you’re using your test API keys and provides a successful test card token for you to use. This allows you to make test payments using a live card without any charges being applied.

Make sure you test using a Cartes Bancaires card obtained from one of the [Apple Pay participating banks](https://support.apple.com/en-us/109516).

## If you’re a Connect Platform

If you’re creating an Elements object without an Intent, make sure to set the [OnBehalfOf](https://docs.stripe.com/js/elements_object/create_without_intent#stripe_elements_no_intent-options-onBehalfOf) parameter to the same account on `on_behalf_of` of the Intent used when confirming payment.
