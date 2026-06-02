<!-- Source URL: https://docs.stripe.com/terminal/features/refunds -->
<!-- Fetched: 2026-05-01 -->

# Refund transactions

Cancel or refund Stripe Terminal payments.

Stripe Terminal supports both _automatic_ (Automatically capture funds when a charge is authorized) and _manual_ (Manually capture funds separately from an authorization) capture.

When the SDK returns a confirmed PaymentIntent to your app, the payment is authorized but not [captured](https://docs.stripe.com/terminal/payments/collect-card-payment.md#capture-payment). You can [cancel](https://docs.stripe.com/terminal/features/refunds.md#canceling-payments) payments that are authorized and not captured. If the PaymentIntent has already been captured, you must [refund](https://docs.stripe.com/terminal/features/refunds.md#refunds) the underlying charge created by the PaymentIntent, using the [refunds API](https://docs.stripe.com/api.md#create_refund) or [Dashboard](https://docs.stripe.com/refunds.md?dashboard-or-api=dashboard).

We recommend [reconciling payments](https://docs.stripe.com/terminal/payments/collect-card-payment.md#reconciling) on your backend after a day’s activity to prevent unintended authorizations and uncollected funds.

## Availability

**Canceling payments** is available on Visa, Mastercard, American Express, Discover, and girocard. For single-message payment methods like [Interac](https://docs.stripe.com/terminal/payments/regional.md?integration-country=CA#interac-payments) and [eftpos](https://docs.stripe.com/terminal/payments/regional.md?integration-country=AU#eftpos-payments), PaymentIntents are automatically captured. In lieu of canceling PaymentIntents, make sure your application can allow initiating a refund at the end of the checkout flow.

**Online refunds** are available on all card networks except for Interac.

[In-person refunds](https://docs.stripe.com/terminal/payments/regional.md?integration-country=CA#refund-an-interac-payment) are only available on Interac.

## Cancel payments (Client-side)(Server-side)

- [cancelPaymentIntent (iOS)](<https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPTerminal.html#/c:objc(cs)SCPTerminal(im)cancelPaymentIntent:completion:>)
- [cancelPaymentIntent (Android)](https://stripe.dev/stripe-terminal-android/core/com.stripe.stripeterminal/-terminal/cancel-payment-intent.html)
- [cancelPaymentIntent (React Native)](https://stripe.dev/stripe-terminal-react-native/api-reference/interfaces/StripeTerminalSdkType.html#cancelPaymentIntent)
- [cancelPaymentIntent (Java)](https://stripe.dev/stripe-terminal-java/core/com.stripe.stripeterminal/-terminal/cancel-payment-intent.html)

You can [cancel](https://docs.stripe.com/api.md#cancel_payment_intent) a `card_present` PaymentIntent at any time before it has been captured. Canceling a PaymentIntent releases all uncaptured funds, and a canceled PaymentIntent can no longer be used to perform charges.

Use this when, for example, your customer decides to use a different payment method or pay with cash after the payment has been processed. In your application’s UI, consider allowing the user to cancel after they [confirm the payment](https://docs.stripe.com/terminal/payments/collect-card-payment.md#confirm-payment), and before you finalize it and notify your backend to [capture](https://docs.stripe.com/terminal/payments/collect-card-payment.md#capture-payment).

#### Client-side

Cancel a `PaymentIntent` from your client using the iOS, Android, or React Native SDK:

# Server-driven

> This is a Server-driven for when terminal-sdk-platform is server-driven. View the full page at https://docs.stripe.com/terminal/features/refunds?terminal-sdk-platform=server-driven.

> Client-side `PaymentIntent` cancellation is possible with the iOS, Android, and React Native SDKs. If you’re using a server-driven integration, cancel the `PaymentIntent` server-side.

# JavaScript

> This is a JavaScript for when terminal-sdk-platform is js. View the full page at https://docs.stripe.com/terminal/features/refunds?terminal-sdk-platform=js.

> Client-side `PaymentIntent` cancellation is possible with the other client SDKs. If you’re using the JavaScript SDK for Stripe Terminal, cancel the `PaymentIntent` server-side.

# iOS

> This is a iOS for when terminal-sdk-platform is ios. View the full page at https://docs.stripe.com/terminal/features/refunds?terminal-sdk-platform=ios.

#### Swift

```swift
// Action for a "Cancel" button
func cancelAction() {
    if let paymentIntent = self.paymentIntent {
        Terminal.shared.cancelPaymentIntent(paymentIntent) { cancelResult, cancelError in
            if let error = cancelError {
                print("cancelPaymentIntent failed: \(error)")
            }
            else {
                print("cancelPaymentIntent succeeded")
            }
        }
    }
}
```

# Android

> This is a Android for when terminal-sdk-platform is android. View the full page at https://docs.stripe.com/terminal/features/refunds?terminal-sdk-platform=android.

#### Kotlin

```kotlin
Terminal.getInstance().cancelPaymentIntent(paymentIntent,
    object : PaymentIntentCallback {
        override fun onSuccess(paymentIntent: PaymentIntent) {
            // Placeholder for handling successful operation
        }

        override fun onFailure(e: TerminalException) {
            // Placeholder for handling exception
        }
    }
)
```

# React Native

> This is a React Native for when terminal-sdk-platform is react-native. View the full page at https://docs.stripe.com/terminal/features/refunds?terminal-sdk-platform=react-native.

```js
const { cancelPaymentIntent } = useStripeTerminal();

const { paymentIntent, error } = await cancelPaymentIntent(paymentIntent);

if (error) {
  // Placeholder for handling exception
  return;
}

// Placeholder for handling successful operation
```

#### Server-side

- [Cancel a PaymentIntent](https://docs.stripe.com/api/payment_intents/cancel.md)

The JavaScript SDK and server-driven integration require you to cancel the `PaymentIntent` on your server. For the other client SDKs, you can cancel the `PaymentIntent` on your server if the information required to start a payment isn’t readily available in your app.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const paymentIntent = await stripe.paymentIntents.cancel('pi_ANipwO3zNfjeWODtRPIg');
```

## Perform refunds (Server-side)

When you use a PaymentIntent to collect payment from a customer, Stripe creates a [charge](https://docs.stripe.com/api/charges/object.md) behind the scenes. To refund the customer’s payment after the PaymentIntent has succeeded, [create a refund](https://docs.stripe.com/api.md#create_refund) by passing in the PaymentIntent ID or the charge ID. You can also optionally refund part of a payment by specifying an amount.

You can perform refunds [with the API](https://docs.stripe.com/refunds.md?dashboard-or-api=api) or [through the Dashboard](https://docs.stripe.com/refunds.md?dashboard-or-api=dashboard). For Interac transactions in Canada, you can provide [in-person refunds](https://docs.stripe.com/terminal/payments/regional.md?integration-country=CA#refund-an-interac-payment) on the BBPOS WisePad 3, BBPOS WisePOS E, Stripe Reader S700/S710, Tap to Pay on iPhone, or Tap to Pay on Android.

Online refunds don’t require a cardholder to present their card again at the point of sale. The following example shows how to create a full refund by passing in the PaymentIntent ID.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const refund = await stripe.refunds.create({
  payment_intent: 'pi_Aabcxyz01aDfoo',
});
```

To refund part of a PaymentIntent, provide an `amount` parameter, as an integer in cents (or the charge currency’s smallest currency unit):

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const refund = await stripe.refunds.create({
  payment_intent: 'pi_Aabcxyz01aDfoo',
  amount: 1000,
});
```

## See also

- [Cart display](https://docs.stripe.com/terminal/features/display.md)
- [Receipts](https://docs.stripe.com/terminal/features/receipts.md)
