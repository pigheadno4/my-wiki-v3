<!-- Source URL: https://docs.stripe.com/payments/mobile/migration-confirmation-tokens -->
<!-- Fetched: 2026-04-23 -->

# Migrate to Confirmation Tokens

Use a ConfirmationToken instead of a PaymentMethod to handle payments

This guide demonstrates how to migrate from the legacy [PaymentMethod](https://docs.stripe.com/api/payment_methods.md) to the [ConfirmationToken](https://docs.stripe.com/api/confirmation_tokens.md) in your mobile integration.

You can use the ConfirmationToken object instead of the PaymentMethod to:

- **Simplify server-side code**: You won’t need to manually construct `mandate_data` or pass `return_url` and `shipping` when you confirm intents.
- **Handle data**: It automatically includes shipping information and other payment context for you.

| Feature                      | PaymentMethod (Legacy) | ConfirmationToken |
| ---------------------------- | ---------------------- | ----------------- |
| Payment confirmation         | ✓                      | ✓                 |
| Setup future usage           | Manual                 | Automatic         |
| Shipping information         | Manual                 | Automatic         |
| Mandate data                 | Manual                 | Automatic         |
| Return URL                   | Manual                 | Automatic         |
| Server-side CVC recollection | ❌                     | ✓                 |

## Before you begin

This guide assumes you have an existing mobile integration using the legacy PaymentMethod. If you’re building a new integration, follow the [Accept a payment](https://docs.stripe.com/payments/mobile/accept-payment.md) guide, which uses ConfirmationTokens by default.

# iOS

> This is a iOS for when platform is ios. View the full page at https://docs.stripe.com/payments/mobile/migration-confirmation-tokens?platform=ios.

## Update your client code [Client-side]

To access and use payment details, pass a callback that receives a `confirmationToken`:

```swift
let intentConfig = PaymentSheet.IntentConfiguration(
  mode: .payment(amount: 1099, currency: "USD")) { confirmationToken in
  try await withCheckedThrowingContinuation() { continuation in
    // If you send paymentMethod.stripeId to your server, send confirmationToken.stripeId instead.
    let myServerResponse: Result<String, Error> = ... // Make a request to your server
    switch myServerResponse {
    case .success(let clientSecret):
      intentCreationCallback(.success(clientSecret))
    case .failure(let error):
      intentCreationCallback(.failure(error))
    }}
}
```

## Update your server code [Server-side]

When you accept payments, you can choose where to confirm the PaymentIntent or SetupIntent:

- **Client-side confirmation**: Your server creates an unconfirmed Intent and returns its `client_secret` to your app. The mobile SDK then confirms the Intent directly to Stripe.

- **Server-side confirmation**: Your app sends the ConfirmationToken to your server, which both creates and confirms the Intent in a single API call by setting `confirm: true`. The confirmation happens entirely on your server when you call the Stripe API, and provides you with more control over the payment flow.

#### Client-side confirmation

Create the PaymentIntent or SetupIntent by excluding `payment_method`, `return_url`, `mandate_data`, and `shipping`. The mobile SDK handles confirmation on the client-side using the ConfirmationToken:

```javascript
app.post("/create-intent", async (req, res) => {
  try {
    const args = {
      amount: 1099,
      currency: "usd",
      automatic_payment_methods: { enabled: true },
    };

    const intent = await stripe.paymentIntents.create(args);
    res.json({ client_secret: intent.client_secret });
  } catch (err) {
    res.status(err.statusCode).json({ error: err.message });
  }
});
```

#### Server-side confirmation

Use the `confirmation_token` parameter when you create and confirm the PaymentIntent or SetupIntent. The ConfirmationToken automatically provides the payment method, mandate data, and return URL.

```javascript
app.post("/create-intent", async (req, res) => {
  try {
    const args = {
      amount: 1099,
      currency: "usd",
      automatic_payment_methods: { enabled: true },
      confirm: true,
      confirmation_token: req.body.confirmationTokenId,
    };

    const intent = await stripe.paymentIntents.create(args);
    res.json({ client_secret: intent.client_secret });
  } catch (err) {
    res.status(err.statusCode).json({ error: err.message });
  }
});
```

Any parameters that you provide directly to the PaymentIntent or SetupIntent at confirmation time, such as `shipping`, override the corresponding properties on the ConfirmationToken.

# Android

> This is a Android for when platform is android. View the full page at https://docs.stripe.com/payments/mobile/migration-confirmation-tokens?platform=android.

## Update your client code [Client-side]

To update the `createIntentCallback`, modify it to receive a `confirmationToken`:

```kotlin
paymentSheet = PaymentSheet.Builder(::onPaymentSheetResult).createIntentCallback { confirmationToken ->
    val networkResult = myNetworkClient.createIntent(// Make a request to your server to create a PaymentIntent and return its client secret.
      // Optionally pass confirmationToken.id if doing server-side confirmation.
      confirmationTokenId = confirmationToken.id,
    )
    if (networkResult.isSuccess) {
      CreateIntentResult.Success(networkResult.clientSecret)
    } else {
      CreateIntentResult.Failure(networkResult.exception)
    }
  }
  .build(this)
```

## Update your server code [Server-side]

When you accept payments, you can choose where to confirm the PaymentIntent or SetupIntent:

- **Client-side confirmation**: Your server creates an unconfirmed Intent and returns its `client_secret` to your app. The mobile SDK then confirms the Intent directly to Stripe.

- **Server-side confirmation**: Your app sends the ConfirmationToken to your server, which both creates and confirms the Intent in a single API call by setting `confirm: true`. The confirmation happens entirely on your server when you call the Stripe API, and provides you with more control over the payment flow.

#### Client-side confirmation

Create the PaymentIntent or SetupIntent by excluding `payment_method`, `return_url`, `mandate_data`, and `shipping`. The mobile SDK handles confirmation on the client-side using the ConfirmationToken:

```javascript
app.post("/create-intent", async (req, res) => {
  try {
    const args = {
      amount: 1099,
      currency: "usd",
      automatic_payment_methods: { enabled: true },
    };

    const intent = await stripe.paymentIntents.create(args);
    res.json({ client_secret: intent.client_secret });
  } catch (err) {
    res.status(err.statusCode).json({ error: err.message });
  }
});
```

#### Server-side confirmation

Use the `confirmation_token` parameter when you create and confirm the PaymentIntent or SetupIntent. The ConfirmationToken automatically provides the payment method, mandate data, and return URL.

```javascript
app.post("/create-intent", async (req, res) => {
  try {
    const args = {
      amount: 1099,
      currency: "usd",
      automatic_payment_methods: { enabled: true },
      confirm: true,
      confirmation_token: req.body.confirmationTokenId,
    };

    const intent = await stripe.paymentIntents.create(args);
    res.json({ client_secret: intent.client_secret });
  } catch (err) {
    res.status(err.statusCode).json({ error: err.message });
  }
});
```

Any parameters that you provide directly to the PaymentIntent or SetupIntent at confirmation time, such as `shipping`, override the corresponding properties on the ConfirmationToken.

# React Native

> This is a React Native for when platform is react-native. View the full page at https://docs.stripe.com/payments/mobile/migration-confirmation-tokens?platform=react-native.

## Update your client code [Client-side]

To change `confirmHandler` to `confirmationTokenConfirmHandler`, update the callback signature to receive `confirmationToken`:

```jsx
intentConfiguration: {confirmationTokenConfirmHandler: async (
    confirmationToken,
    intentCreationCallback
  ) => {
    const response = await fetch('/create-intent', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({// Make a request to your server to create a PaymentIntent and return its client secret.
        // Optionally pass confirmationToken.id if doing server-side confirmation.
        confirmationTokenId: confirmationToken.id,
      }),
    });

    const { clientSecret, error } = await response.json();

    if (clientSecret) {
      intentCreationCallback({ clientSecret });
    } else {
      intentCreationCallback({ error });
    }
  },
  mode: {
    amount: 6099,
    currencyCode: 'USD',
  },
}
```

## Update your server code [Server-side]

When you accept payments, you can choose where to confirm the PaymentIntent or SetupIntent:

- **Client-side confirmation**: Your server creates an unconfirmed Intent and returns its `client_secret` to your app. The mobile SDK then confirms the Intent directly to Stripe.

- **Server-side confirmation**: Your app sends the ConfirmationToken to your server, which both creates and confirms the Intent in a single API call by setting `confirm: true`. The confirmation happens entirely on your server when you call the Stripe API, and provides you with more control over the payment flow.

#### Client-side confirmation

Create the PaymentIntent or SetupIntent by excluding `payment_method`, `return_url`, `mandate_data`, and `shipping`. The mobile SDK handles confirmation on the client-side using the ConfirmationToken:

```javascript
app.post("/create-intent", async (req, res) => {
  try {
    const args = {
      amount: 1099,
      currency: "usd",
      automatic_payment_methods: { enabled: true },
    };

    const intent = await stripe.paymentIntents.create(args);
    res.json({ client_secret: intent.client_secret });
  } catch (err) {
    res.status(err.statusCode).json({ error: err.message });
  }
});
```

#### Server-side confirmation

Use the `confirmation_token` parameter when you create and confirm the PaymentIntent or SetupIntent. The ConfirmationToken automatically provides the payment method, mandate data, and return URL.

```javascript
app.post("/create-intent", async (req, res) => {
  try {
    const args = {
      amount: 1099,
      currency: "usd",
      automatic_payment_methods: { enabled: true },
      confirm: true,
      confirmation_token: req.body.confirmationTokenId,
    };

    const intent = await stripe.paymentIntents.create(args);
    res.json({ client_secret: intent.client_secret });
  } catch (err) {
    res.status(err.statusCode).json({ error: err.message });
  }
});
```

Any parameters that you provide directly to the PaymentIntent or SetupIntent at confirmation time, such as `shipping`, override the corresponding properties on the ConfirmationToken.

> If you previously inspected the PaymentMethod object, you can now access payment method details through the `paymentMethodPreview` property on the ConfirmationToken.

## See also

- [Accept a payment](https://docs.stripe.com/payments/mobile/accept-payment.md)
- [Finalize payments on the server](https://docs.stripe.com/payments/mobile/finalize-payments-on-the-server.md)
- [ConfirmationToken API reference](https://docs.stripe.com/api/confirmation_tokens.md)
