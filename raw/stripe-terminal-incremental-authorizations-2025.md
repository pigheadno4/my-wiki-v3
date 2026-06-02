<!-- Source URL: https://docs.stripe.com/terminal/features/incremental-authorizations -->
<!-- Fetched: 2026-05-01 -->

# Incremental authorizations

Increase the authorized amount before capturing a payment.

Incremental authorizations allow you to increase the authorized [amount](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-amount) on a confirmed [PaymentIntent](https://docs.stripe.com/payments/payment-intents.md) before you capture it. This is helpful if the total price changes or the customer adds goods or services and you need to update the amount on the payment.

Depending on the issuing bank, cardholders might see the amount of the original pending authorization increase in place, or they might see each increment as an additional pending authorization. After capture, the total captured amount appears as one entry.

## Availability

When using incremental authorizations, be aware of the following restrictions:

- They’re only available with Visa, Mastercard, American Express, or Discover.
- Certain card brands have merchant category restrictions (see below).
- You can only increment a transaction made with the POS and reader fully online.
- You have a maximum of 10 attempts per payment.

#### Availability by card network and merchant category

Use incremental authorizations on payments that fulfill the criteria below. You can find your user category in the [Dashboard](https://dashboard.stripe.com/settings/update/company/update).

Attempting to perform an incremental authorization on a payment that doesn’t fulfill the below criteria results in an error.

| Card brand           | Merchant category                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Visa**             | All user categories                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| **Mastercard**       | All user categories                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| **American Express** | All user categories                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| **Discover**         | Car rental, hotels, local/suburban commuter, passenger transportation, including ferries, passenger railways, bus lines-charter, tour, steamship/cruise lines, boat rentals & lease, grocery stores and supermarkets, electric vehicle charging, eating places and restaurants, drinking places (alcoholic beverages), hotels, motels, resorts, trailer parks & campgrounds, equip/tool/furn/appl rental & leasing, automobile rental agency, truck and utility trailer rentals, motor home and rec vehicle rentals, parking lots, parking meters, and garages, amusement parks, circuses, fortune tell, recreation services (not classified) |

## Request incremental authorization support [Server-side] [Client-side]

When you create a `PaymentIntent`, you can request the ability to capture increments of the payment. Set the [request_incremental_authorization_support](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-card_present-request_incremental_authorization_support) field to `true` and the [capture_method](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-capture_method) to `manual`. This updates the text from `Total` to `Pre-authorization` in the payment collection screen.

#### Server-side

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1000,
  currency: 'usd',
  payment_method_types: ['card_present'],
  capture_method: 'manual',
  payment_method_options: {
    card_present: {
      request_incremental_authorization_support: true,
    },
  },
});
```

#### iOS

#### Swift

```swift
let cardPresentParams = try CardPresentParametersBuilder().setRequestIncrementalAuthorization(true).build()
let paymentMethodOptionsParams = try PaymentMethodOptionsParametersBuilder(cardPresentParameters: cardPresentParams).build()
let params = try PaymentIntentParametersBuilder(amount: 1000, currency: "usd")
    .setPaymentMethodOptionsParameters(paymentMethodOptionsParams)
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

#### Android

#### Kotlin

```kotlin
val cardPresentParams = CardPresentParameters.Builder()
    .setRequestIncrementalAuthorizationSupport(true)
    .build()

val paymentMethodOptionsParams = PaymentMethodOptionsParameters.Builder()
    .setCardPresentParameters(cardPresentParams)
    .build()

val params = PaymentIntentParameters.Builder()
    .setAmount(1000)
    .setCurrency("usd")
    .setPaymentMethodOptionsParameters(paymentMethodOptionsParams)
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

#### React Native

```js
const { paymentIntent, error } = await createPaymentIntent({
  amount: 1000,
  currency: 'usd',
  paymentMethodOptions: {
    requestIncrementalAuthorizationSupport: true,
  }
});

if (error) {
  console.log(`createPaymentIntent failed: ${error.message}`);
  return;
}

console.log('createPaymentIntent succeeded');
```

## Confirm the PaymentIntent [Client-side]

Check the [incremental_authorization_supported](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-card_present-incremental_authorization_supported) field in the confirm response to determine if the `PaymentIntent` is eligible for incremental authorization.

You can only perform incremental authorizations on uncaptured payments after confirmation. To adjust the amount of a payment before confirmation, use the [update](https://docs.stripe.com/api/payment_intents/update.md) method instead.

#### JavaScript

```javascript
async () => {
  const result = await terminal.processPayment(paymentIntent);
  if (result.error) {
    // Placeholder for handling result.error
  } else if (result.paymentIntent) {
    // Now you're ready to increment the authorization using your backend
  }
};
```

#### iOS

#### Swift

```swift


// Action for a "Checkout" button
func checkoutAction() throws {
  let params = PaymentIntentParametersBuilder(amount: 1000, currency: "sgd").build()
  Terminal.shared.createPaymentIntent(params) { createResult, createError in
      if let error = createError {
          print("createPaymentIntent failed: \(error)")
      } else if let paymentIntent = createResult {
          print("createPaymentIntent succeeded")
          self.collectCancelable = Terminal.shared.collectPaymentMethod(paymentIntent) { collectResult, collectError in
              if let error = collectError {
                  print("collectPaymentMethod failed: \(error)")
              } else if let collectPaymentMethodPaymentIntent = collectResult {
                  print("collectPaymentMethod succeeded")
                  // ... Confirm the payment
                  Terminal.shared.confirmPaymentIntent(collectPaymentMethodPaymentIntent) { confirmResult, confirmError in
                      if let error = confirmError {
                          print("confirmPaymentIntent failed: \(error)")
                      } else if let confirmedPaymentIntent = confirmResult {
                          print("confirmPaymentIntent succeeded")
                          // Now you're ready to increment the authorization using your backend
                      }
                  }
              }
          }
      }
  }
}
```

#### Android

#### Kotlin

```kotlin
Terminal.getInstance().confirmPaymentIntent(
    paymentIntent,
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

#### React Native

```js
const { paymentIntent, error } = await createPaymentIntent({
  amount: 1000,
  currency: 'usd',
});

if (error) {
  console.log(`createPaymentIntent failed: ${error.message}`);
  return;
}

console.log('createPaymentIntent succeeded');

const { paymentIntent: collectedPI, error: paymentIntentError } = await collectPaymentMethod({ paymentIntent: paymentIntent.id });

if (paymentIntentError) {
  console.log(`collectPaymentMethod failed: ${paymentIntentError.message}`);
  return;
}

console.log('collectPaymentMethod succeeded');

const { paymentIntent: processedPI, error: processError } = await processPayment(paymentIntent.id);

if (processError) {
  console.log(`processPayment failed: ${processError.message}`);
  return;
}

// Now you're ready to increment the authorization using your backend
console.log('processPayment succeeded');
```

Not all PaymentIntents are eligible for incremental authorizations. To determine whether a PaymentIntent is eligible based on the restrictions listed in the [Availability](https://docs.stripe.com/terminal/features/incremental-authorizations.md#availability) section, check the [incremental_authorization_supported](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-card_present-incremental_authorization_supported) field on the PaymentIntent’s latest charge after a successful confirmation.

## Perform an incremental authorization [Server-side]

To increase the authorized amount on a payment, use the [increment_authorization](https://docs.stripe.com/api/payment_intents/increment_authorization.md) endpoint and provide the updated total [amount](https://docs.stripe.com/api/payment_intents/increment_authorization.md#increment_authorization-amount) to increment to, which must be greater than the original authorized amount. This attempts to authorize for the difference between the previous amount and the incremented amount. Each `PaymentIntent` can have a maximum of 10 incremental authorization attempts, including declines.

A single `PaymentIntent` can call this endpoint multiple times to further increase the authorized amount.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const paymentIntent = await stripe.paymentIntents.incrementAuthorization(
  '{{PAYMENT_INTENT_ID}}',
  {
    amount: 1500,
  }
);
```

An authorization can either:

- Succeed – Returns the `PaymentIntent` with the updated amount.
- Fail – Returns a [card_declined](https://docs.stripe.com/error-codes.md#card-declined) error, and the `PaymentIntent` remains authorized to capture the original amount. Updates to other `PaymentIntent` fields (for example, [application_fee_amount](https://docs.stripe.com/api/payment_intents/increment_authorization.md#increment_authorization-application_fee_amount)) aren’t saved.

## Capture the PaymentIntent [Server-side]

To capture the authorized amount on a `PaymentIntent` that has prior incremental authorizations, use the [capture](https://docs.stripe.com/api/payment_intents/capture.md) endpoint. To increase the authorized amount and simultaneously capture that updated amount, provide an updated [amount_to_capture](https://docs.stripe.com/api/payment_intents/capture.md#capture_payment_intent-amount_to_capture).

Providing an `amount_to_capture` that’s higher than the currently authorized amount results in an automatic incremental authorization attempt.

> If you’re eligible to [collect on-receipt tips](https://docs.stripe.com/terminal/features/collecting-tips/on-receipt.md), using an `amount_to_capture` that’s higher than the currently authorized amount won’t result in an automatic incremental authorization attempt. Capture requests always succeed.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const paymentIntent = await stripe.paymentIntents.capture(
  '{{PAYMENT_INTENT_ID}}',
  {
    amount_to_capture: 2000,
  }
);
```

The possible outcomes of an incremental authorization attempt are:

- Succeed – Returns the `captured` `PaymentIntent` with the updated amount.
- Fail – Returns a [card_declined](https://docs.stripe.com/error-codes.md#card-declined) error, and the `PaymentIntent` remains authorized to capture the original amount. Updates to other `PaymentIntent` fields (for example, [application_fee_amount](https://docs.stripe.com/api/payment_intents/capture.md#capture_payment_intent-application_fee_amount)) aren’t saved.

Regardless, when using `amount_to_capture` we recommend that you always check for potential failures.
