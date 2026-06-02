<!-- Source: Stripe Terminal — Process MOTO payments (all SDK platforms) -->
<!-- Fetched: 2026-04-24 -->

# Process MOTO payments

Process mail order and telephone order (MOTO) payments using Stripe Terminal.

> #### Requesting access
>
> To begin processing MOTO payments, contact [Stripe support](https://support.stripe.com/) for access.

# Server-driven

> This is a Server-driven for when terminal-sdk-platform is server-driven. View the full page at https://docs.stripe.com/terminal/features/mail-telephone-orders/payments?terminal-sdk-platform=server-driven.

To process MOTO payments with a server-driven integration, you must:

1. [Create a PaymentIntent](https://docs.stripe.com/terminal/features/mail-telephone-orders/payments.md#create-payment-intent).
1. [Process the payment](https://docs.stripe.com/terminal/features/mail-telephone-orders/payments.md#process-payment).
1. [Verify the reader state](https://docs.stripe.com/terminal/features/mail-telephone-orders/payments.md#verify-reader-state).
1. [Capture the payment](https://docs.stripe.com/terminal/features/mail-telephone-orders/payments.md#capture-payment).

## Create a PaymentIntent

To begin collecting a MOTO payment, you must create a [PaymentIntent](https://docs.stripe.com/payments/payment-intents.md) with [payment_method_types](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_types) that includes `card`.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  currency: "usd",
  payment_method_types: ["card"],
  capture_method: "automatic",
  amount: 1000,
});
```

## Process the payment

> CVC is mandatory for MOTO transactions. Skipping CVC is in private preview and you can request it for mail orders. Contact [Stripe support](https://support.stripe.com/) for access.

After you create a `PaymentIntent`, use [process_payment_intent](https://docs.stripe.com/api/terminal/readers/process_payment_intent.md) to process the payment, setting [process_config[moto]](https://docs.stripe.com/api/terminal/readers/process_payment_intent.md#process_payment_intent-process_config) to `true`.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const reader = await stripe.terminal.readers.processPaymentIntent(
  "{{TERMINALREADER_ID}}",
  {
    payment_intent: "{{PAYMENTINTENT_ID}}",
    process_config: {
      moto: true,
    },
  },
);
```

The [process_payment_intent](https://docs.stripe.com/api/terminal/readers/process_payment_intent.md) request is asynchronous. After the request, the reader prompts you for the cardholder’s card number, CVC, expiration date, and postal code.

> If you’re displaying cart details using the [setReaderDisplay](https://docs.stripe.com/terminal/features/display.md) method, you must reset the reader’s display from a line item interface to the splash screen before collecting a MOTO payment.

## Verify the reader state

Your application must follow the instructions for [verifying the reader state](https://docs.stripe.com/terminal/payments/collect-card-payment.md?terminal-sdk-platform=server-driven&reader=wpe#verify-reader) to confirm a successful (approved) payment.

## Capture the payment

You must call [capture](https://docs.stripe.com/terminal/payments/collect-card-payment.md?terminal-sdk-platform=server-driven#capture-payment) to complete the payment if the `PaymentIntent` has a status of `requires_capture`.

## Testing

Use the [simulated reader](https://docs.stripe.com/terminal/references/testing.md#simulated-card-presentment) and [simulated test card numbers](https://docs.stripe.com/terminal/references/testing.md#simulated-test-cards) to test your integration.

# iOS

> This is a iOS for when terminal-sdk-platform is ios. View the full page at https://docs.stripe.com/terminal/features/mail-telephone-orders/payments?terminal-sdk-platform=ios.

To process MOTO payments, you must:

1. [Create a PaymentIntent](https://docs.stripe.com/terminal/features/mail-telephone-orders/payments.md#create-payment-intent).
1. [Collect a PaymentMethod](https://docs.stripe.com/terminal/features/mail-telephone-orders/payments.md#collect-payment-method).
1. [Confirm and capture the payment](https://docs.stripe.com/terminal/features/mail-telephone-orders/payments.md#confirm-capture-payment).

## Create a PaymentIntent

To begin collecting a MOTO payment, you must create a [PaymentIntent](https://docs.stripe.com/payments/payment-intents.md) with [payment_method_types](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_types) that includes `card`.

#### Swift

```swift
let params = try PaymentIntentParametersBuilder(amount: 1000, currency: "sgd")
  .setPaymentMethodTypes([.card])
  .build()
Terminal.shared.createPaymentIntent(params) { createResult, createError in
  if let error = createError {
    print("createPaymentIntent failed: \(error)")
  } else if let paymentIntent = createResult {
    print("createPaymentIntent succeeded")
    // ...
  }
}
```

## Collect a payment method

> CVC is mandatory for MOTO transactions. Skipping CVC is in private preview and you can request it for mail orders. Contact [Stripe support](https://support.stripe.com/) for access.

After you’ve created a PaymentIntent, you can collect a PaymentMethod with the SDK. To collect a MOTO payment, your app must connect to a reader.

To enable MOTO, set a non-nil `MotoConfiguration` on the `CollectPaymentIntentConfiguration`.

After the request, the connected reader prompts you for the cardholder’s number, CVC, expiration date, and postal code.

> If you’re displaying cart details using the [setReaderDisplay](https://docs.stripe.com/terminal/features/display.md) method, you must reset the reader’s display from a line item interface to the splash screen before collecting a MOTO payment.

#### Swift

```swift
let motoConfig = try MotoConfigurationBuilder().build()
let config = try CollectPaymentIntentConfigurationBuilder().setMotoConfiguration(motoConfig).build()
Terminal.shared.collectPaymentMethod(paymentIntent, config) { intentWithPaymentMethod, attachError in
  if let error = attachError {
    print("collectPaymentMethod failed: \(error)")
  } else if let paymentIntent = intentWithPaymentMethod {
    print("collectPaymentMethod succeeded")
    // ...
  }
}
```

## Confirm and capture payment

You can follow the usual procedure to [confirm](https://docs.stripe.com/terminal/payments/collect-card-payment.md#confirm-payment) and [capture](https://docs.stripe.com/terminal/payments/collect-card-payment.md#capture-payment) the PaymentIntent.

## Testing

Use the [simulated reader](https://docs.stripe.com/terminal/references/testing.md#simulated-reader) and [simulated test card numbers](https://docs.stripe.com/terminal/references/testing.md#simulated-test-cards) to test your integration.

# Android

> This is a Android for when terminal-sdk-platform is android. View the full page at https://docs.stripe.com/terminal/features/mail-telephone-orders/payments?terminal-sdk-platform=android.

To process MOTO payments, you must:

1. [Create a PaymentIntent](https://docs.stripe.com/terminal/features/mail-telephone-orders/payments.md#create-payment-intent).
1. [Collect a PaymentMethod](https://docs.stripe.com/terminal/features/mail-telephone-orders/payments.md#collect-payment-method).
1. [Confirm and capture the payment](https://docs.stripe.com/terminal/features/mail-telephone-orders/payments.md#confirm-capture-payment).

## Create a PaymentIntent

To begin collecting a MOTO payment, you must create a [PaymentIntent](https://docs.stripe.com/payments/payment-intents.md) with [payment_method_types](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_types) that includes `card`.

#### Kotlin

```kotlin
val params = PaymentIntentParameters.Builder(
    listOf(PaymentMethodType.CARD)
  )
  .setAmount(1000)
  .setCurrency("sgd")
  .build()
Terminal.getInstance().createPaymentIntent(
    params,
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

## Collect a payment method

> CVC is mandatory for MOTO transactions. Skipping CVC is in private preview and you can request it for mail orders. Contact [Stripe support](https://support.stripe.com/) for access.

After you’ve created a PaymentIntent, you can collect a PaymentMethod with the SDK. To collect a MOTO payment, your app must connect to a reader.

To enable MOTO, set a non-null `MotoConfiguration` on the `CollectPaymentIntentConfiguration`.

After the request, the connected reader prompts you for the cardholder’s number, CVC, expiration date, and postal code.

> If you’re displaying cart details using the [setReaderDisplay](https://docs.stripe.com/terminal/features/display.md) method, you must reset the reader’s display from a line item interface to the splash screen before collecting a MOTO payment.

#### Kotlin

```kotlin
val config = CollectPaymentIntentConfiguration.Builder()
    .setMotoConfiguration(
        MotoConfiguration.Builder()
            .build()
    )
    .build()

Terminal.getInstance().collectPaymentMethod(
    paymentIntent,
    config,
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

## Confirm and capture payment

You can follow the usual procedure to [confirm](https://docs.stripe.com/terminal/payments/collect-card-payment.md#confirm-payment) and [capture](https://docs.stripe.com/terminal/payments/collect-card-payment.md#capture-payment) the PaymentIntent.

## Testing

Use the [simulated reader](https://docs.stripe.com/terminal/references/testing.md#simulated-reader) and [simulated test card numbers](https://docs.stripe.com/terminal/references/testing.md#simulated-test-cards) to test your integration.

# JavaScript

> This is a JavaScript for when terminal-sdk-platform is js. View the full page at https://docs.stripe.com/terminal/features/mail-telephone-orders/payments?terminal-sdk-platform=js.

To process MOTO payments, you must:

1. [Create a PaymentIntent](https://docs.stripe.com/terminal/features/mail-telephone-orders/payments.md#create-payment-intent).
1. [Collect a PaymentMethod](https://docs.stripe.com/terminal/features/mail-telephone-orders/payments.md#collect-payment-method).
1. [Confirm and capture the payment](https://docs.stripe.com/terminal/features/mail-telephone-orders/payments.md#confirm-capture-payment).

## Create a PaymentIntent

To begin collecting a MOTO payment, you must create a [PaymentIntent](https://docs.stripe.com/payments/payment-intents.md) with [payment_method_types](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_types) that includes `card`.

Create the PaymentIntent on your back end. The PaymentIntent contains a [client secret](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-client_secret), a key that’s unique to the individual PaymentIntent. To use the client secret, you must obtain it from the PaymentIntent on your server and [pass it to the client side](https://docs.stripe.com/payments/payment-intents.md#passing-to-client).

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  currency: "usd",
  payment_method_types: ["card"],
  capture_method: "automatic",
  amount: 1000,
});
```

## Collect a payment method

> CVC is mandatory for MOTO transactions. Skipping CVC is in private preview and you can request it for mail orders. Contact [Stripe support](https://support.stripe.com/) for access.

After you’ve created a PaymentIntent, you can collect a PaymentMethod with the SDK. To collect a MOTO payment, your app must connect to a reader.

Set `moto` to `true` in the `CollectConfiguration` object when calling `collectPaymentMethod`.

After the request, the connected reader prompts you for the cardholder’s number, CVC, expiration date, and postal code.

> If you’re displaying cart details using the [setReaderDisplay](https://docs.stripe.com/terminal/features/display.md) method, you must reset the reader’s display from a line item interface to the splash screen before collecting a MOTO payment.

```js
async () => {
  // Pass the client_secret from the PaymentIntent you created in the previous step.
  const result = await this.terminal.collectPaymentMethod(client_secret, {
    config_override: {
      moto: true,
    },
  });
  if (result.error) {
    // Placeholder for handling result.error
  } else {
    // Placeholder for processing result.paymentIntent
  }
};
```

## Confirm and capture payment

You can follow the usual procedure to [confirm](https://docs.stripe.com/terminal/payments/collect-card-payment.md#confirm-payment) and [capture](https://docs.stripe.com/terminal/payments/collect-card-payment.md#capture-payment) the PaymentIntent.

## Testing

Use the [simulated reader](https://docs.stripe.com/terminal/references/testing.md#simulated-reader) and [simulated test card numbers](https://docs.stripe.com/terminal/references/testing.md#simulated-test-cards) to test your integration.

# React Native

> This is a React Native for when terminal-sdk-platform is react-native. View the full page at https://docs.stripe.com/terminal/features/mail-telephone-orders/payments?terminal-sdk-platform=react-native.

To process MOTO payments, you must:

1. [Create a PaymentIntent](https://docs.stripe.com/terminal/features/mail-telephone-orders/payments.md#create-payment-intent).
1. [Collect a PaymentMethod](https://docs.stripe.com/terminal/features/mail-telephone-orders/payments.md#collect-payment-method).
1. [Confirm and capture the payment](https://docs.stripe.com/terminal/features/mail-telephone-orders/payments.md#confirm-capture-payment).

## Create a PaymentIntent

To begin collecting a MOTO payment, you must create a [PaymentIntent](https://docs.stripe.com/payments/payment-intents.md) with [payment_method_types](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_types) that includes `card`.

```js
const params = {
  amount: 1000,
  currency: "sgd",
  paymentMethodTypes: ["card"],
};

try {
  const paymentIntent = await terminal.createPaymentIntent(params);
  // Placeholder for handling successful operation
} catch (error) {
  // Placeholder for handling exception
}
```

## Collect a payment method

> CVC is mandatory for MOTO transactions. Skipping CVC is in private preview and you can request it for mail orders. Contact [Stripe support](https://support.stripe.com/) for access.

After you’ve created a PaymentIntent, you can collect a PaymentMethod with the SDK. To collect a MOTO payment, your app must connect to a reader.

To enable MOTO, set a non-nil `MotoConfiguration` on the `CollectPaymentIntentConfiguration`.

After the request, the connected reader prompts you for the cardholder’s number, CVC, expiration date, and postal code.

> If you’re displaying cart details using the [setReaderDisplay](https://docs.stripe.com/terminal/features/display.md) method, you must reset the reader’s display from a line item interface to the splash screen before collecting a MOTO payment.

```js
try {
  const result = await collectPaymentMethod({
    paymentIntent: paymentIntent,
    motoConfiguration: { skipCvc: true },
  });
  // Placeholder for handling successful operation
} catch (error) {
  // Placeholder for handling exception
}
```

## Confirm and capture payment

You can follow the usual procedure to [confirm](https://docs.stripe.com/terminal/payments/collect-card-payment.md#confirm-payment) and [capture](https://docs.stripe.com/terminal/payments/collect-card-payment.md#capture-payment) the PaymentIntent.

## Testing

Use the [simulated reader](https://docs.stripe.com/terminal/references/testing.md#simulated-reader) and [simulated test card numbers](https://docs.stripe.com/terminal/references/testing.md#simulated-test-cards) to test your integration.
