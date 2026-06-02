<!-- Source URL: https://docs.stripe.com/payments/mobile/embedded-filter-card-brands -->
<!-- Fetched: 2026-04-22 -->

# Filter card brands

Choose which card brands to accept

# iOS

> This is a iOS for when platform is ios. View the full page at https://docs.stripe.com/payments/mobile/embedded-filter-card-brands?platform=ios.

Use Stripe [In-app Payments](https://docs.stripe.com/payments/mobile.md) to control which card brands you accept. Card brand filtering lets you specify allowed or disallowed card brands for:

- The credit card form in In-app Payments
- The cards buyers can use with Apple Pay.

When you configure In-app Payments, you can specify one of two options:

- `allowed`: Accept only the card brands you specify.
- `disallowed`: Accept all card brands except those you specify.

For either of these options, pass an array with any of the following card brand values as defined on `EmbeddedPaymentElement.Configuration.CardBrandAcceptance.BrandCategory`:

- `.visa`
- `.mastercard`
- `.amex`
- `.discover`

> The `discover` value encompasses all of the cards that are part of the Discover Global Network, including Discover, Diners Club, JCB, UnionPay, and Elo.

This guide demonstrates how to use card brand filtering to only accept card payments from Visa and Mastercard branded cards.

## Before you begin

1. [Create a Stripe account](https://dashboard.stripe.com/register) or [sign in](https://dashboard.stripe.com/login).
1. Follow the [Payment Element Accept In-app payments](https://docs.stripe.com/payments/mobile/accept-payment-embedded.md) guide to integrate with Mobile Payment Element.

## Filter card brands

When you create a `EmbeddedPaymentElement.Configuration` object, specify the card brands you want to allow or disallow using the `cardBrandAcceptance` property. This example shows how to allow only Visa and Mastercard:

```swift
import StripePaymentSheet

class MyCheckoutVC: UIViewController {
  func createEmbeddedPaymentElement() async throws -> EmbeddedPaymentElement {
      // ...
      var configuration = EmbeddedPaymentElement.Configuration()configuration.cardBrandAcceptance = .allowed(brands: [.visa, .mastercard])
      // ...
  }
}
```

## Test your integration

Stripe provides a set of [test card numbers](https://docs.stripe.com/testing.md#cards) that you can use to test your checkout flow and verify that the Mobile Payment Element accepts or blocks your desired card brands.
![The Mobile Payment Element when a card brand is disallowed](assets/stripe-inapp-custom-payment-methods-test-ui.png)

# Android

> This is a Android for when platform is android. View the full page at https://docs.stripe.com/payments/mobile/embedded-filter-card-brands?platform=android.

Use Stripe [In-app Payments](https://docs.stripe.com/payments/mobile.md) to control which card brands you accept. Card brand filtering lets you specify allowed or disallowed card brands for:

- The credit card form in In-app Payments
- The cards buyers can use with Apple Pay.

When you configure In-app Payments, you can specify one of two options:

- `allowed`: Accept only the card brands you specify.
- `disallowed`: Accept all card brands except those you specify.

Pass an array containing a list of the card brands to allow or disallow. You can include any of the following card brand values, as defined in `PaymentSheet.CardBrandAcceptance.BrandCategory`:

- `Visa`
- `Mastercard`
- `Amex`
- `Discover`

> The `discover` value includes all brands that belong to the Discover Global Network, including Discover, Diners Club, JCB, UnionPay, and Elo.

This guide demonstrates how to use card brand filtering to only accept card payments from Visa and Mastercard branded cards.

## Before you begin

1. [Create a Stripe account](https://dashboard.stripe.com/register) or [sign in](https://dashboard.stripe.com/login).
1. Follow the [Payment Element Accept In-app payments](https://docs.stripe.com/payments/mobile/accept-payment-embedded.md) guide to integrate with the Mobile Payment Element.

## Specify the card brand filters

When you create an `EmbeddedPaymentElement.Configuration` object, specify the card brands you want to allow or disallow using the `cardBrandAcceptance` property. This example shows how to allow only Visa and Mastercard:

```kotlin
import com.stripe.android.paymentelement.EmbeddedPaymentElement

@Composable
fun CheckoutScreen() {
    val embeddedPaymentElementBuilder = remember {
        EmbeddedPaymentElement.Builder(
            createIntentCallback = { paymentMethod, shouldSavePaymentMethod ->
                // Create intent
            },
            resultCallback = {
                // Handle result
            },
        )
    }

    val embeddedPaymentElement = rememberEmbeddedPaymentElement(embeddedPaymentElementBuilder)

    LaunchedEffect(embeddedPaymentElement) {
        embeddedPaymentElement.configure(
            configuration = EmbeddedPaymentElement.Configuration.Builder("Powdur").cardBrandAcceptance(
                    PaymentSheet.CardBrandAcceptance.allowed(
                        listOf(
                            PaymentSheet.CardBrandAcceptance.BrandCategory.Visa,
                            PaymentSheet.CardBrandAcceptance.BrandCategory.Mastercard
                        )
                    )
                )
                .build(),
            intentConfiguration = PaymentSheet.IntentConfiguration.Builder().build(),
        )
    }

    embeddedPaymentElement.Content()
}
```

## Test your integration

Stripe provides a set of [test card numbers](https://docs.stripe.com/testing.md#cards) that you can use to test your checkout flow and verify that the Mobile Payment Element accepts or blocks your desired card brands.
![The Mobile Payment Element when a card brand is disallowed](assets/stripe-inapp-custom-payment-methods-test-ui.png)

# React Native

> This is a React Native for when platform is react-native. View the full page at https://docs.stripe.com/payments/mobile/embedded-filter-card-brands?platform=react-native.

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
1. Follow the [Accept In-app payments](https://docs.stripe.com/payments/mobile/accept-payment-embedded.md) guide to integrate with the Payment Element.

## Filter card brands

When you create Payment Element, specify the card brands you want to allow or disallow using the `cardBrandAcceptance` property. This example shows how to allow only Visa and Mastercard:

```javascript
import {
  useEmbeddedPaymentElement,
  EmbeddedPaymentElementConfiguration,
  PaymentSheet
} from '@stripe/stripe-react-native';

export default function CheckoutScreen() {

  const initialize = async () => {
    const elementConfig: EmbeddedPaymentElementConfiguration = {
      // ... other configuration optionscardBrandAcceptance: {
        filter: PaymentSheet.CardBrandAcceptanceFilter.Allowed,
        brands: [
          PaymentSheet.CardBrandCategory.Visa,
          PaymentSheet.CardBrandCategory.Mastercard
        ],
      },
    };
  };
}
```

## Test your integration

Stripe provides a set of [test card numbers](https://docs.stripe.com/testing.md#cards) that you can use to test your checkout flow and verify that the Mobile Payment Element accepts or blocks your desired card brands.
![The Mobile Payment Element when a card brand is disallowed](assets/stripe-inapp-custom-payment-methods-test-ui.png)
