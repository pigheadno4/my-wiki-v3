<!-- Source URL: https://docs.stripe.com/payments/mobile/upgrade-to-handle-actions -->
<!-- Fetched: 2026-04-23 -->

# Migrate your basic card integration

Migrate your mobile app to an integration that can handle bank requests for card authentication.

# iOS

> This is a iOS for when platform is ios. View the full page at https://docs.stripe.com/payments/mobile/upgrade-to-handle-actions?platform=ios.

If you followed the [Card payments without bank authentication](https://docs.stripe.com/payments/without-card-authentication.md) guide, your integration creates payments that decline when a bank asks the customer to authenticate the purchase.

If you start seeing many failed payments like the one in the Dashboard below or with an error code of `requires_action_not_handled` in the API, upgrade your basic integration to handle, rather than decline, these payments.
![Dashboard showing a failed payment that says that this bank required authentication for this payment](assets/stripe-inapp-failed-payment-dashboard.png)

Use this guide to learn how to upgrade the integration you built in the previous guide to add server and client code that prompts the customer to authenticate the payment by displaying a modal.

> See a [full sample](https://github.com/stripe-samples/accept-a-payment/tree/master/custom-payment-flow) of this integration on GitHub.

## Check if the payment requires authentication [Server-side]

Make three changes to the endpoint on your server that creates the PaymentIntent:

1. **Remove** the [error_on_requires_action](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-error_on_requires_action) parameter to no longer fail payments that require authentication. Instead, the PaymentIntent status changes to `requires_action`.
1. **Add** the `confirmation_method` parameter to indicate that you want to explicitly (manually) _confirm_ (Confirming an intent indicates that the customer intends to use the current or provided payment method. Upon confirmation, the intent attempts to initiate the portions of the flow that have real-world side effects) the payment again on the server after handling authentication requests.
1. **Add** the [use_stripe_sdk](https://docs.stripe.com/api/payment_intents/confirm.md#confirm_payment_intent-use_stripe_sdk) parameter to enable your mobile client to handle additional authentication steps.

#### Node.js

```javascript
let intent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "usd",
  payment_method_types: ["card"],
  confirm: true,
  payment_method: request.body.payment_method_id,
  confirmation_method: "manual",
  use_stripe_sdk: true,
});
```

Then update your “generate response” function to handle the `requires_action` state instead of erroring:

#### Node.js

```javascript
app.post("/pay", async (request, response) => {
  try {
    // Create the PaymentIntent
    let intent = await stripe.paymentIntents.create({
      amount: 1099,
      currency: "usd",
      payment_method_types: ["card"],
      confirm: true,
      payment_method: request.body.payment_method_id,
      confirmation_method: "manual",
      use_stripe_sdk: true,
    });
    return generateResponse(response, intent);
  } catch (e) {
    if (e.type === "StripeCardError") {
      // Display error on client
      return response.send({ error: e.message });
    } else {
      // Something else happened
      return response.status(500).send({ error: e.type });
    }
  }
});

function generateResponse(response, intent) {
  if (intent.status === "succeeded") {
    // Handle post-payment fulfillment
    return response.send({ success: true });
  } else if (intent.status === "requires_action") {
    // Tell the client to handle the action
    return response.send({
      requiresAction: true,
      clientSecret: intent.client_secret,
    });
  } else {
    // Any other status would be unexpected, so error
    return response
      .status(500)
      .send({ error: "Unexpected status " + intent.status });
  }
}
```

## Ask the customer to authenticate [Client-side]

Next, update your iOS code to tell Stripe to show a modal if the customer needs to authenticate.

Use `handleNextActionForPayment` when a PaymentIntent has a status of `requires_action`. If successful, the PaymentIntent will have a status of `requires_confirmation` and you need to confirm the PaymentIntent again on your server to finish the payment.

#### Objective C

```objc
- (void)handleResponse:(NSDictionary *)json {
    if (json[@"error"] != nil) {
        // Display the error to the customer} else if (json[@"requiresAction"]) {
        // Payment requires additional actions
        NSString *clientSecret = json[@"clientSecret"];
        STPPaymentHandler *paymentHandler = [STPPaymentHandler sharedHandler];
        [paymentHandler handleNextActionForPayment:clientSecret
                         withAuthenticationContext:self
                                         returnURL:nil
                                        completion:^(STPPaymentHandlerActionStatus status, STPPaymentIntent *paymentIntent, NSError *handleActionError) {
                switch (status) {
                    case STPPaymentHandlerActionStatusFailed: {
                        // Display handleActionError to the customer
                        break;
                    }
                    case STPPaymentHandlerActionStatusCanceled: {
                        // Canceled
                        break;
                    }
                    case STPPaymentHandlerActionStatusSucceeded: {
                        // The card action has been handled
                        // Send the PaymentIntent ID to your server and confirm it again
                        break;
                    }
                    default:
                        break;
                }
        }];
    } else {
        // Display success message
    }
}

# pragma mark STPAuthenticationContext
- (UIViewController *)authenticationPresentingViewController {
    return self;
}
```

## Confirm the PaymentIntent again [Server-side]

Using the same endpoint you set up earlier, _confirm_ (Confirming an intent indicates that the customer intends to use the current or provided payment method. Upon confirmation, the intent attempts to initiate the portions of the flow that have real-world side effects) the PaymentIntent again to finalize the payment and fulfill the order. The payment attempt fails and transitions back to `requires_payment_method` if it isn’t confirmed again within one hour.

#### Node.js

```javascript
// Using Express
const express = require("express");
const app = express();
app.use(express.json());

app.post("/pay", async (request, response) => {
  try {
    let intent;
    if (request.body.payment_method_id) {
      // Create the PaymentIntent
      intent = await stripe.paymentIntents.create({
        amount: 1099,
        currency: "usd",
        payment_method_types: ["card"],
        confirm: true,
        payment_method: request.body.payment_method_id,
        confirmation_method: "manual",
        use_stripe_sdk: true,
      });
    } else if (request.body.payment_intent_id) {
      intent = await stripe.paymentIntents.confirm(
        request.body.payment_intent_id,
      );
    }
    // Send the response to the client
    return generateResponse(response, intent);
  } catch (e) {
    if (e.type === "StripeCardError") {
      // Display error on client
      return response.send({ error: e.message });
    } else {
      // Something else happened
      return response.status(500).send({ error: e.type });
    }
  }
});
```

## Test the integration

Use our test cards in a sandbox to verify that your integration was properly updated. Stripe displays a fake authentication page inside the modal in a sandbox that lets you simulate a successful or failed authentication attempt. In live mode the bank controls the UI of what’s displayed inside the modal.

| Number           | Description                                                                                                       |
| ---------------- | ----------------------------------------------------------------------------------------------------------------- |
| 4242424242424242 | Succeeds and immediately processes the payment.                                                                   |
| 4000000000009995 | Always fails with a decline code of `insufficient_funds`.                                                         |
| 4000002500003155 | Requires authentication, which in this integration will fail with a decline code of `authentication_not_handled`. |

# Android

> This is a Android for when platform is android. View the full page at https://docs.stripe.com/payments/mobile/upgrade-to-handle-actions?platform=android.

If you followed the [Card payments without bank authentication](https://docs.stripe.com/payments/without-card-authentication.md) guide, your integration creates payments that decline when a bank asks the customer to authenticate the purchase.

If you start seeing many failed payments like the one in the Dashboard below or with an error code of `requires_action_not_handled` in the API, upgrade your basic integration to handle, rather than decline, these payments.
![Dashboard showing a failed payment that says that this bank required authentication for this payment](assets/stripe-inapp-failed-payment-dashboard.png)

Use this guide to learn how to upgrade the integration you built in the previous guide to add server and client code that prompts the customer to authenticate the payment by displaying a modal.

> See a [full sample](https://github.com/stripe-samples/accept-a-payment/tree/master/custom-payment-flow) of this integration on GitHub.

## Check if the payment requires authentication [Server-side]

Make three changes to the endpoint on your server that creates the PaymentIntent:

1. **Remove** the [error_on_requires_action](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-error_on_requires_action) parameter to no longer fail payments that require authentication. Instead, the PaymentIntent status changes to `requires_action`.
1. **Add** the `confirmation_method` parameter to indicate that you want to explicitly (manually) _confirm_ (Confirming an intent indicates that the customer intends to use the current or provided payment method. Upon confirmation, the intent attempts to initiate the portions of the flow that have real-world side effects) the payment again on the server after handling authentication requests.
1. **Add** the [use_stripe_sdk](https://docs.stripe.com/api/payment_intents/confirm.md#confirm_payment_intent-use_stripe_sdk) parameter to enable your mobile client to handle additional authentication steps.

#### Node.js

```javascript
let intent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "usd",
  payment_method_types: ["card"],
  confirm: true,
  payment_method: request.body.payment_method_id,
  confirmation_method: "manual",
  use_stripe_sdk: true,
});
```

Then update your “generate response” function to handle the `requires_action` state instead of erroring:

#### Node.js

```javascript
app.post("/pay", async (request, response) => {
  try {
    // Create the PaymentIntent
    let intent = await stripe.paymentIntents.create({
      amount: 1099,
      currency: "usd",
      payment_method_types: ["card"],
      confirm: true,
      payment_method: request.body.payment_method_id,
      confirmation_method: "manual",
      use_stripe_sdk: true,
    });
    return generateResponse(response, intent);
  } catch (e) {
    if (e.type === "StripeCardError") {
      // Display error on client
      return response.send({ error: e.message });
    } else {
      // Something else happened
      return response.status(500).send({ error: e.type });
    }
  }
});

function generateResponse(response, intent) {
  if (intent.status === "succeeded") {
    // Handle post-payment fulfillment
    return response.send({ success: true });
  } else if (intent.status === "requires_action") {
    // Tell the client to handle the action
    return response.send({
      requiresAction: true,
      clientSecret: intent.client_secret,
    });
  } else {
    // Any other status would be unexpected, so error
    return response
      .status(500)
      .send({ error: "Unexpected status " + intent.status });
  }
}
```

## Ask the customer to authenticate [Client-side]

Next, update your Android code to tell Stripe to show a modal if the customer needs to authenticate.

Use `handleNextActionForPayment` when a PaymentIntent has a status of `requires_action`. If successful, the PaymentIntent will have a status of `requires_confirmation` and you need to confirm the PaymentIntent again on your server to finish the payment.

#### Java

```java
public class CheckoutActivity extends Activity {private Stripe stripe;

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        stripe = new Stripe(this, "<<YOUR_PUBLISHABLE_KEY>>");
    }
    private void handleResponse(@NonNull JSONObject json) throws JSONException {
        if (json.has("error")) {
            // Display the error to the customer
            final String error = json.getString("error");} else if (json.has("requiresAction")) {
            final String clientSecret = json.getString("clientSecret");
            stripe.handleNextActionForPayment(this, clientSecret);
        } else {
            // Display success message
        }
    }@Override
    protected void onActivityResult(int requestCode, int resultCode, @Nullable Intent data) {
        super.onActivityResult(requestCode, resultCode, data);

        stripe.onPaymentResult(requestCode, data,
                new ApiResultCallback<PaymentIntentResult>() {
                    @Override
                    public void onSuccess(@NonNull PaymentIntentResult result) {
                        switch (result.getOutcome()) {
                            case StripeIntentResult.Outcome.SUCCEEDED: {
                                // The card action has been handled
                                // Send the Payment Intent ID to your server and confirm it again
                            }
                            case StripeIntentResult.Outcome.CANCELED: {
                                // Canceled
                            }
                            case StripeIntentResult.Outcome.TIMEDOUT: {
                                // Timed-out
                            }
                            case StripeIntentResult.Outcome.FAILED: {
                                // Failed
                            }
                        }
                    }

                    @Override
                    public void onError(@NonNull Exception e) {
                        // Error encountered
                    }
                }
        );
    }
}
```

## Confirm the PaymentIntent again [Server-side]

Using the same endpoint you set up earlier, _confirm_ (Confirming an intent indicates that the customer intends to use the current or provided payment method. Upon confirmation, the intent attempts to initiate the portions of the flow that have real-world side effects) the PaymentIntent again to finalize the payment and fulfill the order. The payment attempt fails and transitions back to `requires_payment_method` if it isn’t confirmed again within one hour.

#### Node.js

```javascript
// Using Express
const express = require("express");
const app = express();
app.use(express.json());

app.post("/pay", async (request, response) => {
  try {
    let intent;
    if (request.body.payment_method_id) {
      // Create the PaymentIntent
      intent = await stripe.paymentIntents.create({
        amount: 1099,
        currency: "usd",
        payment_method_types: ["card"],
        confirm: true,
        payment_method: request.body.payment_method_id,
        confirmation_method: "manual",
        use_stripe_sdk: true,
      });
    } else if (request.body.payment_intent_id) {
      intent = await stripe.paymentIntents.confirm(
        request.body.payment_intent_id,
      );
    }
    // Send the response to the client
    return generateResponse(response, intent);
  } catch (e) {
    if (e.type === "StripeCardError") {
      // Display error on client
      return response.send({ error: e.message });
    } else {
      // Something else happened
      return response.status(500).send({ error: e.type });
    }
  }
});
```

## Test the integration

Use our test cards in a sandbox to verify that your integration was properly updated. Stripe displays a fake authentication page inside the modal in a sandbox that lets you simulate a successful or failed authentication attempt. In live mode the bank controls the UI of what’s displayed inside the modal.

| Number           | Description                                                                                                       |
| ---------------- | ----------------------------------------------------------------------------------------------------------------- |
| 4242424242424242 | Succeeds and immediately processes the payment.                                                                   |
| 4000000000009995 | Always fails with a decline code of `insufficient_funds`.                                                         |
| 4000002500003155 | Requires authentication, which in this integration will fail with a decline code of `authentication_not_handled`. |

# React Native

> This is a React Native for when platform is react-native. View the full page at https://docs.stripe.com/payments/mobile/upgrade-to-handle-actions?platform=react-native.

If you followed the [Card payments without bank authentication](https://docs.stripe.com/payments/without-card-authentication.md) guide, your integration creates payments that decline when a bank asks the customer to authenticate the purchase.

If you start seeing many failed payments like the one in the Dashboard below or with an error code of `requires_action_not_handled` in the API, upgrade your basic integration to handle, rather than decline, these payments.
![Dashboard showing a failed payment that says that this bank required authentication for this payment](assets/stripe-inapp-failed-payment-dashboard.png)

Use this guide to learn how to upgrade the integration you built in the previous guide to add server and client code that prompts the customer to authenticate the payment by displaying a modal.

## Check if the payment requires authentication [Server-side]

Make three changes to the endpoint on your server that creates the PaymentIntent:

1. **Remove** the [error_on_requires_action](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-error_on_requires_action) parameter to no longer fail payments that require authentication. Instead, the PaymentIntent status changes to `requires_action`.
1. **Add** the `confirmation_method` parameter to indicate that you want to explicitly (manually) _confirm_ (Confirming an intent indicates that the customer intends to use the current or provided payment method. Upon confirmation, the intent attempts to initiate the portions of the flow that have real-world side effects) the payment again on the server after handling authentication requests.
1. **Add** the [use_stripe_sdk](https://docs.stripe.com/api/payment_intents/confirm.md#confirm_payment_intent-use_stripe_sdk) parameter to enable your mobile client to handle additional authentication steps.

#### Node.js

```javascript
let intent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "usd",
  payment_method_types: ["card"],
  confirm: true,
  payment_method: request.body.payment_method_id,
  confirmation_method: "manual",
  use_stripe_sdk: true,
});
```

Then update your “generate response” function to handle the `requires_action` state instead of erroring:

#### Node.js

```javascript
app.post("/pay", async (request, response) => {
  try {
    // Create the PaymentIntent
    let intent = await stripe.paymentIntents.create({
      amount: 1099,
      currency: "usd",
      payment_method_types: ["card"],
      confirm: true,
      payment_method: request.body.payment_method_id,
      confirmation_method: "manual",
      use_stripe_sdk: true,
    });
    return generateResponse(response, intent);
  } catch (e) {
    if (e.type === "StripeCardError") {
      // Display error on client
      return response.send({ error: e.message });
    } else {
      // Something else happened
      return response.status(500).send({ error: e.type });
    }
  }
});

function generateResponse(response, intent) {
  if (intent.status === "succeeded") {
    // Handle post-payment fulfillment
    return response.send({ success: true });
  } else if (intent.status === "requires_action") {
    // Tell the client to handle the action
    return response.send({
      requiresAction: true,
      clientSecret: intent.client_secret,
    });
  } else {
    // Any other status would be unexpected, so error
    return response
      .status(500)
      .send({ error: "Unexpected status " + intent.status });
  }
}
```

## Ask the customer to authenticate [Client-side]

Update your client-side code to show a modal if the customer needs to authenticate. Use `handleCardAction` when a PaymentIntent has a status of `requires_action`. If successful, the PaymentIntent will have a status of `requires_confirmation` and you need to confirm the PaymentIntent again on your server to finish the payment.

```javascript
function CheckoutScreen() {
  const { handleCardAction } = useStripe();

  const handleResponse = async (response) => {
    if (response.error) {
      // handle error} else if (response.requiresAction) {
      const { error, paymentIntent } = await handleCardAction(
        response.clientSecret,
      );

      if (error) {
        Alert.alert(`Error code: ${error.code}`, error.message);
      } else {
        // The card action has been handled
        // The PaymentIntent can be confirmed again on the server
        fetch("/pay", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ payment_intent_id: paymentIntent.id }),
        })
          .then(function (confirmResult) {
            return confirmResult.json();
          })
          .then(handleServerResponse);
      }
    } else {
      // Display success message
    }
  };
}
```

## Confirm the PaymentIntent again [Server-side]

Using the same endpoint you set up earlier, _confirm_ (Confirming an intent indicates that the customer intends to use the current or provided payment method. Upon confirmation, the intent attempts to initiate the portions of the flow that have real-world side effects) the PaymentIntent again to finalize the payment and fulfill the order. The payment attempt fails and transitions back to `requires_payment_method` if it isn’t confirmed again within one hour.

#### Node.js

```javascript
// Using Express
const express = require("express");
const app = express();
app.use(express.json());

app.post("/pay", async (request, response) => {
  try {
    let intent;
    if (request.body.payment_method_id) {
      // Create the PaymentIntent
      intent = await stripe.paymentIntents.create({
        amount: 1099,
        currency: "usd",
        payment_method_types: ["card"],
        confirm: true,
        payment_method: request.body.payment_method_id,
        confirmation_method: "manual",
        use_stripe_sdk: true,
      });
    } else if (request.body.payment_intent_id) {
      intent = await stripe.paymentIntents.confirm(
        request.body.payment_intent_id,
      );
    }
    // Send the response to the client
    return generateResponse(response, intent);
  } catch (e) {
    if (e.type === "StripeCardError") {
      // Display error on client
      return response.send({ error: e.message });
    } else {
      // Something else happened
      return response.status(500).send({ error: e.type });
    }
  }
});
```

## Test the integration

Use our test cards in a sandbox to verify that your integration was properly updated. Stripe displays a fake authentication page inside the modal in a sandbox that lets you simulate a successful or failed authentication attempt. In live mode the bank controls the UI of what’s displayed inside the modal.

| Number           | Description                                                                                                       |
| ---------------- | ----------------------------------------------------------------------------------------------------------------- |
| 4242424242424242 | Succeeds and immediately processes the payment.                                                                   |
| 4000000000009995 | Always fails with a decline code of `insufficient_funds`.                                                         |
| 4000002500003155 | Requires authentication, which in this integration will fail with a decline code of `authentication_not_handled`. |
