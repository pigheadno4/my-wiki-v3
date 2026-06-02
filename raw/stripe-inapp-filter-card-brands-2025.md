<!-- Source URL: https://docs.stripe.com/payments/mobile/filter-card-brands -->
<!-- Fetched: 2026-04-22 -->

# Filter card brands

Choose which card brands to accept

# iOS

> This is a iOS for when platform is ios. View the full page at https://docs.stripe.com/payments/mobile/filter-card-brands?platform=ios.

Use Stripe [In-app Payments](https://docs.stripe.com/payments/mobile.md) to control which card brands you accept. Card brand filtering lets you specify allowed or disallowed card brands for:

- The credit card form in In-app Payments
- The cards buyers can use with Apple Pay.

When you configure In-app Payments, you can specify one of two options:

- `allowed`: Accept only the card brands you specify.
- `disallowed`: Accept all card brands except those you specify.

For either of these options, pass an array with any of the following card brand values as defined on `PaymentSheet.Configuration.CardBrandAcceptance.BrandCategory`:

- `.visa`
- `.mastercard`
- `.amex`
- `.discover`

> The `discover` value encompasses all of the cards that are part of the Discover Global Network, including Discover, Diners Club, JCB, UnionPay, and Elo.

This guide demonstrates how to use card brand filtering to only accept card payments from Visa and Mastercard branded cards.

## Before you begin

1. [Create a Stripe account](https://dashboard.stripe.com/register) or [sign in](https://dashboard.stripe.com/login).
1. Follow the steps in [Accept in-app payments](https://docs.stripe.com/payments/mobile/accept-payment.md) to integrate with the Mobile Payment Element.

## Filter card brands

When you create your `PaymentSheet.Configuration` object, specify the card brands you want to allow or disallow using the `cardBrandAcceptance` property. This example shows how to allow only Visa and Mastercard:

```swift
import StripePaymentSheet

class MyCheckoutVC: UIViewController {
  func setUpPaymentSheet() {
      // ...
      var configuration = PaymentSheet.Configuration()configuration.cardBrandAcceptance = .allowed(brands: [.visa, .mastercard])
      // ...
  }
}
```

## Test your integration

Stripe provides a set of [test card numbers](https://docs.stripe.com/testing.md#cards) that you can use to test your checkout flow and verify that the Mobile Payment Element accepts or blocks your desired card brands.
![The Mobile Payment Element when a card brand is disallowed](assets/stripe-inapp-filter-card-brands-ios.png)

# Android

> This is a Android for when platform is android. View the full page at https://docs.stripe.com/payments/mobile/filter-card-brands?platform=android.

Use Stripe [In-app Payments](https://docs.stripe.com/payments/mobile.md) to control which card brands you accept. Card brand filtering lets you specify allowed or disallowed card brands for:

- The credit card form in the In-app Payments
- The cards buyers can use with Google Pay.

When you configure In-app Payments, you can specify one of two options:

- `allowed`: Accept only the card brands you specify.
- `disallowed`: Accept all card brands except those you specify.

For either of these options, pass an array with any of the following card brand values as defined on `PaymentSheet.CardBrandAcceptance.BrandCategory`:

- `Visa`
- `Mastercard`
- `Amex`
- `Discover`

> The `Discover` value encompasses all of the cards that are part of the Discover Global Network, including Discover, Diners Club, JCB, UnionPay, and Elo.

This guide demonstrates how to use card brand filtering to only accept card payments from Visa and Mastercard branded cards.

## Before you begin

1. [Create a Stripe account](https://dashboard.stripe.com/register) or [sign in](https://dashboard.stripe.com/login).
1. Follow the steps in [Accept in-app payments](https://docs.stripe.com/payments/mobile/accept-payment.md) to integrate with the Mobile Payment Element.

## Filter card brands

When you create your `PaymentSheet.Configuration` object, specify the card brands you want to allow or disallow using the `cardBrandAcceptance` property. This example shows how to allow only Visa and Mastercard:

```kotlin
import com.stripe.android.paymentsheet.PaymentSheet

class CheckoutActivity : AppCompatActivity() {

  private fun onPayClicked(
    paymentSheet: PaymentSheet,
    paymentIntentClientSecret: String,
  ) {
      val configuration = PaymentSheet.Configuration.Builder(merchantDisplayName = "Example, Inc.").cardBrandAcceptance(
          PaymentSheet.CardBrandAcceptance.allowed(
            listOf(
              PaymentSheet.CardBrandAcceptance.BrandCategory.Visa,
              PaymentSheet.CardBrandAcceptance.BrandCategory.Mastercard
            )
          )
        )
        .build()

      // Present Payment Sheet
      paymentSheet.presentWithPaymentIntent(paymentIntentClientSecret, configuration)
    }
}
```

## Test your integration

Stripe provides a set of [test card numbers](https://docs.stripe.com/testing.md#cards) that you can use to test your checkout flow and verify that the Mobile Payment Element accepts or blocks your desired card brands.
![The Mobile Payment Element when a card brand is disallowed](assets/stripe-inapp-filter-card-brands-android.png)

# React Native

> This is a React Native for when platform is react-native. View the full page at https://docs.stripe.com/payments/mobile/filter-card-brands?platform=react-native.

Use Stripe [In-app Payments](https://docs.stripe.com/payments/mobile.md) to control which card brands you accept. Card brand filtering lets you specify allowed or disallowed card brands for:

- The credit card form in the In-app Payments.
- The cards buyers can use with Apple Pay.

When you configure In-app Payments, you can specify one of two options:

- `Allowed`: Accept only the card brands you specify.
- `Disallowed`: Accept all card brands except those you specify.

For either of these options, pass an array with any of the following card brand values as defined on `PaymentSheet.CardBrandCategory`:

- `.Visa`
- `.Mastercard`
- `.Amex`
- `.Discover`

> The `Discover` value encompasses all of the cards in the Discover Global Network, including Discover, Diners Club, JCB, UnionPay, and Elo.

This guide demonstrates how to use card brand filtering to only accept card payments from Visa and Mastercard branded cards.

## Before you begin

1. [Create a Stripe account](https://dashboard.stripe.com/register) or [sign in](https://dashboard.stripe.com/login).
1. Follow the steps in [Accept in-app payments](https://docs.stripe.com/payments/mobile/accept-payment.md) to integrate with the Mobile Payment Element.

## Filter card brands

When you create PaymentSheet, specify the card brands you want to allow or disallow using the `cardBrandAcceptance` property. This example shows how to allow only Visa and Mastercard:

```javascript
import { useStripe } from '@stripe/stripe-react-native';

export default function CheckoutScreen() {
  const { initPaymentSheet } = useStripe();

  const initializePaymentSheet = async () => {
    const { error } = await initPaymentSheet({
      // ... other configuration optionscardBrandAcceptance: {
        filter: PaymentSheet.CardBrandAcceptanceFilter.Allowed,
        brands: [PaymentSheet.CardBrandCategory.Visa, PaymentSheet.CardBrandCategory.Mastercard],
      },
    });
    if (error) {
      // handle error
    }
  };
}
```

## Test your integration

Stripe provides a set of [test card numbers](https://docs.stripe.com/testing.md#cards) that you can use to test your checkout flow and verify that the Mobile Payment Element accepts or blocks your desired card brands.
![The Mobile Payment Element when a card brand is disallowed](assets/stripe-inapp-filter-card-brands-ios.png)
