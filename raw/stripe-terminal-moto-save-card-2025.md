<!-- Source: Stripe Terminal — Save a card with MOTO for future payments (all SDK platforms) -->
<!-- Fetched: 2026-04-24 -->

# Save a card with MOTO for future payments

Save mail order and telephone order (MOTO) card details for future payment using Stripe Terminal.

> #### Requesting access
>
> To begin processing MOTO payments, contact [Stripe support](https://support.stripe.com/) for access.

# Server-driven

> This is a Server-driven for when terminal-sdk-platform is server-driven. View the full page at https://docs.stripe.com/terminal/features/mail-telephone-orders/save-directly?terminal-sdk-platform=server-driven.

To save payment details from a MOTO for a future payment, you must:

1. [Create or retrieve a Customer](https://docs.stripe.com/terminal/features/mail-telephone-orders/save-directly.md#create-customer).
1. [Create a SetupIntent](https://docs.stripe.com/terminal/features/mail-telephone-orders/save-directly.md#create-setup-intent).
1. [Process the SetupIntent](https://docs.stripe.com/terminal/features/mail-telephone-orders/save-directly.md#process-setupintent).
1. [Verify the reader state](https://docs.stripe.com/terminal/features/mail-telephone-orders/save-directly.md#verify-reader-state).
1. [Charge the saved PaymentMethod](https://docs.stripe.com/terminal/features/mail-telephone-orders/save-directly.md#charge-payment-method).

## Create or retrieve a Customer

To charge a card saved with Stripe, you must attach it to a [Customer](https://docs.stripe.com/api/customers.md).

When you include a customer in your [SetupIntent](https://docs.stripe.com/api/setup_intents.md) before confirming, Stripe automatically attaches the generated card payment method to the provided [Customer](https://docs.stripe.com/api/customers.md) object that you create/retrieve.

Include the following code on your server to create a new `Customer`:

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const customer = await stripe.customers.create();
```

## Create a SetupIntent

- [Create a SetupIntent](https://docs.stripe.com/api/setup_intents/create.md)

A [SetupIntent](https://docs.stripe.com/api/setup_intents.md) is an object that represents your intent to set up a customer’s payment method for future payments. The SetupIntent tracks the steps of this setup process. The [payment_method_types](https://docs.stripe.com/api/setup_intents/create.md#create_setup_intent-payment_method_types) must include `card`.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const setupIntent = await stripe.setupIntents.create({
  customer: "{{CUSTOMER_ID}}",
  payment_method_types: ["card"],
});
```

## Process the SetupIntent

> CVC is mandatory for MOTO transactions. Skipping CVC is in private preview and you can request it for mail orders. Contact [Stripe support](https://support.stripe.com/) for access.

After you create the SetupIntent, use [process_setup_intent](https://docs.stripe.com/api/terminal/readers/process_setup_intent.md) to process the payment, setting [process_config[moto]](https://docs.stripe.com/api/terminal/readers/process_setup_intent.md#process_setup_intent-process_config) to `true`. Pass [allow_redisplay](https://docs.stripe.com/api/payment_methods/object.md#payment_method_object-allow_redisplay) as `always` or `limited`, indicating the degree to which a payment method can be shown in a customer checkout flow.

```curl
curl https://api.stripe.com/v1/terminal/readers/{{TERMINALREADER_ID}}/process_setup_intent \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d "setup_intent={{SETUPINTENT_ID}}" \
  -d "process_config[moto]=true" \
  -d allow_redisplay=always
```

The [process_setup_intent](https://docs.stripe.com/api/terminal/readers/process_setup_intent.md) request is asynchronous. After the request, the reader prompts you for the cardholder’s card number, CVC, expiry date, and postal code.

## Verify the reader state

Your application must follow the instructions for [verifying the reader state](https://docs.stripe.com/terminal/payments/collect-card-payment.md?terminal-sdk-platform=server-driven&reader=wpe#verify-reader) to confirm a successful (approved) SetupIntent.

## Charge the saved PaymentMethod

You can now charge the saved PaymentMethod associated with the `Customer` using a [PaymentIntent](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method).

## Testing

Use the [simulated reader](https://docs.stripe.com/terminal/references/testing.md#simulated-reader) and [simulated test card numbers](https://docs.stripe.com/terminal/references/testing.md#simulated-test-cards) to test your integration.

## Compliance

You’re responsible for your compliance with all applicable laws, regulations, and network rules when saving a customer’s payment details. For example, the European Data Protection Board has issued guidance regarding saving payment details. These requirements generally apply if you want to save your customer’s payment method for future use. This applies in situations such as presenting a customer’s payment method to them in the checkout flow for a future purchase, or charging them when they’re not actively using your website or app, placing a MOTO order, or in your store.

Add terms to your checkout flow that state how you plan to save payment method details and allow customers to opt in. If you plan to charge the customer while they’re not actively checking out, make sure (at a minimum) that your terms also cover the following:

- The customer’s agreement to your initiating a payment or a series of payments on their behalf for specified transactions.
- The anticipated timing and frequency of payments (for instance, whether charges are for scheduled installment or subscription payments, or for unscheduled top-ups).
- How the payment amount is determined.
- Your cancellation policy, if you’re setting up the payment method for a subscription service.

Make sure you keep a record of your customer’s written agreement to these terms.

When you save a payment method, you can only use it for the specific purpose that you included in your terms. If you want to charge customers when they’re not actively checking out and also save the customer’s payment method to present to them as a saved payment method for future purchases, you must explicitly collect consent from the customer. One way to do so is with a “Save my payment method for future use” checkbox.

# iOS

> This is a iOS for when terminal-sdk-platform is ios. View the full page at https://docs.stripe.com/terminal/features/mail-telephone-orders/save-directly?terminal-sdk-platform=ios.

To save payment details from a MOTO for a future payment, you must:

1. [Create or retrieve a Customer](https://docs.stripe.com/terminal/features/mail-telephone-orders/save-directly.md#create-customer).
1. [Create a SetupIntent](https://docs.stripe.com/terminal/features/mail-telephone-orders/save-directly.md#create-setup-intent).
1. [Process the SetupIntent](https://docs.stripe.com/terminal/features/mail-telephone-orders/save-directly.md#process-setup-intent).

## Create or retrieve a Customer

To charge a card saved with Stripe, you must attach it to a [Customer](https://docs.stripe.com/api/customers.md).

When you include a customer in your [SetupIntent](https://docs.stripe.com/api/setup_intents.md) before confirming, Stripe automatically attaches the generated card payment method to the provided `Customer` object that you create/retrieve.

Include the following code on your server to create a new `Customer` object:

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const customer = await stripe.customers.create();
```

## Create a SetupIntent

A [SetupIntent](https://docs.stripe.com/api/setup_intents.md) is an object that represents your intent to set up a customer’s payment method for future payments. The SetupIntent tracks the steps of this setup process. For Terminal, this includes collecting and recording cardholder consent.

The [payment_method_types](https://docs.stripe.com/api/setup_intents/create.md#create_setup_intent-payment_method_types) must include `card`.

#### Swift

```swift
let params = try SetupIntentParametersBuilder()
  .setCustomer("{{CUSTOMER_ID}}")
  .setOnBehalfOf("{{ON_BEHALF_OF}}")
  .setDescription("Customer A's Card")
  .setPaymentMethodTypes([.card])
  .build()
Terminal.shared.createSetupIntent(params) { (createdSetupIntent, createError) in
  if let error = createError {
    print("createSetupIntent failed: \(error)")
  } else if let setupIntent = createdSetupIntent {
    print("createSetupIntent succeeded")
    // ...
  }
}
```

## Process the SetupIntent

> CVC is mandatory for MOTO transactions. Skipping CVC is in private preview and you can request it for mail orders. Contact [Stripe support](https://support.stripe.com/) for access.

After you create a SetupIntent, the next step is to process it with the SDK. Pass [allowRedisplay](https://docs.stripe.com/api/payment_methods/object.md#payment_method_object-allow_redisplay) as `always` or `limited`, indicating the degree to which a payment method can be shown in a customer checkout flow.

To process a SetupIntent, you must connect your app to a reader. In the `CollectSetupIntentConfiguration`, set a `MotoConfiguration` object.

The connected reader prompts you to enter the customer’s card number, CVC, expiration date, and postal code after your app calls `processSetupIntent`.

#### Swift

```swift
let motoConfig = try MotoConfigurationBuilder().build()
let config = try CollectSetupIntentConfigurationBuilder()
    .setMotoConfiguration(motoConfig)
    .setAllowRedisplay(.always)
    .build()

let cancelable = Terminal.shared.processSetupIntent(
    setupIntent,
    collectConfig: config
) { processedSetupIntent, processError in
    if let error = processError {
        print("processSetupIntent failed: \(error)")
        // Placeholder for handling error
    } else if let setupIntent = processedSetupIntent {
        print("processSetupIntent succeeded")
        // Placeholder for handling successful operation
    }
}
```

## Use the PaymentMethod

You can now [charge the saved PaymentMethod](https://docs.stripe.com/payments/save-and-reuse.md#charge-saved-payment-method) associated with the customer using a PaymentIntent.

## Testing

Use the [simulated reader](https://docs.stripe.com/terminal/references/testing.md#simulated-reader) and [simulated test card numbers](https://docs.stripe.com/terminal/references/testing.md#simulated-test-cards) to test your integration.

## Compliance

You’re responsible for your compliance with all applicable laws, regulations, and network rules when saving a customer’s payment details. For example, the European Data Protection Board has issued guidance regarding saving payment details. These requirements generally apply if you want to save your customer’s payment method for future use. This applies in situations such as presenting a customer’s payment method to them in the checkout flow for a future purchase, or charging them when they’re not actively using your website or app, placing a MOTO order, or in your store.

Add terms to your checkout flow that state how you plan to save payment method details and allow customers to opt in. If you plan to charge the customer while they’re not actively checking out, make sure (at a minimum) that your terms also cover the following:

- The customer’s agreement to your initiating a payment or a series of payments on their behalf for specified transactions.
- The anticipated timing and frequency of payments (for instance, whether charges are for scheduled installment or subscription payments, or for unscheduled top-ups).
- How the payment amount is determined.
- Your cancellation policy, if you’re setting up the payment method for a subscription service.

Make sure you keep a record of your customer’s written agreement to these terms.

When you save a payment method, you can only use it for the specific purpose that you included in your terms. If you want to charge customers when they’re not actively checking out and also save the customer’s payment method to present to them as a saved payment method for future purchases, you must explicitly collect consent from the customer. One way to do so is with a “Save my payment method for future use” checkbox.

# Android

> This is a Android for when terminal-sdk-platform is android. View the full page at https://docs.stripe.com/terminal/features/mail-telephone-orders/save-directly?terminal-sdk-platform=android.

To save payment details from a MOTO for a future payment, you must:

1. [Create or retrieve a Customer](https://docs.stripe.com/terminal/features/mail-telephone-orders/save-directly.md#create-customer).
1. [Create a SetupIntent](https://docs.stripe.com/terminal/features/mail-telephone-orders/save-directly.md#create-setup-intent).
1. [Process the SetupIntent](https://docs.stripe.com/terminal/features/mail-telephone-orders/save-directly.md#process-setup-intent).

## Create or retrieve a Customer

To charge a card saved with Stripe, you must attach it to a [Customer](https://docs.stripe.com/api/customers.md).

When you include a customer in your [SetupIntent](https://docs.stripe.com/api/setup_intents.md) before confirming, Stripe automatically attaches the generated card payment method to the provided `Customer` object that you create/retrieve.

Include the following code on your server to create a new `Customer` object:

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const customer = await stripe.customers.create();
```

## Create a SetupIntent

A [SetupIntent](https://docs.stripe.com/api/setup_intents.md) is an object that represents your intent to set up a customer’s payment method for future payments. The SetupIntent tracks the steps of this setup process. For Terminal, this includes collecting and recording cardholder consent.

The [payment_method_types](https://docs.stripe.com/api/setup_intents/create.md#create_setup_intent-payment_method_types) must include `card`.

#### Kotlin

```kotlin
val params = SetupIntentParameters.Builder()
    .setCustomer("{{CUSTOMER_ID}}")
    .setOnBehalfOf("{{ON_BEHALF_OF}}")
    .setDescription("Customer A's Card")
    .setPaymentMethodTypes(listOf(PaymentMethodType.CARD))
    .build()

Terminal.getInstance().createSetupIntent(params, object : SetupIntentCallback {
    override fun onSuccess(setupIntent: SetupIntent) {
        // Placeholder for handling successful operation
    }

    override fun onFailure(e: TerminalException) {
        // Placeholder for handling exception
    }
})
```

## Process the SetupIntent

> CVC is mandatory for MOTO transactions. Skipping CVC is in private preview and you can request it for mail orders. Contact [Stripe support](https://support.stripe.com/) for access.

After you create a SetupIntent, the next step is to process it with the SDK. Pass [allowRedisplay](https://docs.stripe.com/api/payment_methods/object.md#payment_method_object-allow_redisplay) as `always` or `limited`, indicating the degree to which a payment method can be shown in a customer checkout flow.

To process a SetupIntent, you must connect your app to a reader. In the `CollectSetupIntentConfiguration`, set a `MotoConfiguration` object.

The connected reader prompts you to enter the customer’s card number, CVC, expiration date, and postal code after your app calls `processSetupIntent`.

#### Kotlin

```kotlin
val config = CollectSetupIntentConfiguration.Builder()
    .setMotoConfiguration(
        MotoConfiguration.Builder()
            .build()
    )
    .setAllowRedisplay(AllowRedisplay.ALWAYS)
    .build()

val cancelable = Terminal.getInstance().processSetupIntent(
    setupIntent,
    config,
    object : SetupIntentCallback {
        override fun onSuccess(setupIntent: SetupIntent) {
            // Placeholder for handling successful operation
        }

        override fun onFailure(e: TerminalException) {
            // Placeholder for handling exception
        }
    }
)
```

## Use the PaymentMethod

You can now [charge the saved PaymentMethod](https://docs.stripe.com/payments/save-and-reuse.md#charge-saved-payment-method) associated with the customer using a PaymentIntent.

## Testing

Use the [simulated reader](https://docs.stripe.com/terminal/references/testing.md#simulated-reader) and [simulated test card numbers](https://docs.stripe.com/terminal/references/testing.md#simulated-test-cards) to test your integration.

## Compliance

You’re responsible for your compliance with all applicable laws, regulations, and network rules when saving a customer’s payment details. For example, the European Data Protection Board has issued guidance regarding saving payment details. These requirements generally apply if you want to save your customer’s payment method for future use. This applies in situations such as presenting a customer’s payment method to them in the checkout flow for a future purchase, or charging them when they’re not actively using your website or app, placing a MOTO order, or in your store.

Add terms to your checkout flow that state how you plan to save payment method details and allow customers to opt in. If you plan to charge the customer while they’re not actively checking out, make sure (at a minimum) that your terms also cover the following:

- The customer’s agreement to your initiating a payment or a series of payments on their behalf for specified transactions.
- The anticipated timing and frequency of payments (for instance, whether charges are for scheduled installment or subscription payments, or for unscheduled top-ups).
- How the payment amount is determined.
- Your cancellation policy, if you’re setting up the payment method for a subscription service.

Make sure you keep a record of your customer’s written agreement to these terms.

When you save a payment method, you can only use it for the specific purpose that you included in your terms. If you want to charge customers when they’re not actively checking out and also save the customer’s payment method to present to them as a saved payment method for future purchases, you must explicitly collect consent from the customer. One way to do so is with a “Save my payment method for future use” checkbox.

# JavaScript

> This is a JavaScript for when terminal-sdk-platform is js. View the full page at https://docs.stripe.com/terminal/features/mail-telephone-orders/save-directly?terminal-sdk-platform=js.

To save payment details from a MOTO for a future payment, you must:

1. [Create or retrieve a Customer](https://docs.stripe.com/terminal/features/mail-telephone-orders/save-directly.md#create-customer).
1. [Create a SetupIntent](https://docs.stripe.com/terminal/features/mail-telephone-orders/save-directly.md#create-setup-intent).
1. [Collect a PaymentMethod](https://docs.stripe.com/terminal/features/mail-telephone-orders/save-directly.md#collect-payment-method).
1. [Confirm and use the PaymentMethod](https://docs.stripe.com/terminal/features/mail-telephone-orders/save-directly.md#confirm-use-payment-method).

## Create or retrieve a Customer

To charge a card saved with Stripe, you must attach it to a [Customer](https://docs.stripe.com/api/customers.md).

When you include a customer in your [SetupIntent](https://docs.stripe.com/api/setup_intents.md) before confirming, Stripe automatically attaches the generated card payment method to the provided `Customer` object that you create/retrieve.

Include the following code on your server to create a new `Customer` object:

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const customer = await stripe.customers.create();
```

## Create a SetupIntent

A [SetupIntent](https://docs.stripe.com/api/setup_intents.md) is an object that represents your intent to set up a customer’s payment method for future payments. The SetupIntent tracks the steps of this setup process. For Terminal, this includes collecting and recording cardholder consent.

The [payment_method_types](https://docs.stripe.com/api/setup_intents/create.md#create_setup_intent-payment_method_types) must include `card`.

The SetupIntent contains a [client secret](https://docs.stripe.com/api/setup_intents/object.md#setup_intent_object-client_secret), which is a key that’s unique to the individual SetupIntent. You must obtain the _client secret_ (The client secret is a unique key returned from Stripe as part of a PaymentIntent. This key lets the client access important fields from the PaymentIntent (status, amount, currency) while hiding sensitive ones (metadata, customer)) from the SetupIntent on your server and pass it to the client side.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const setupIntent = await stripe.setupIntents.create({
  customer: "{{CUSTOMER_ID}}",
  payment_method_types: ["card"],
});
```

## Collect a PaymentMethod

After you create a SetupIntent, the next step is to collect a PaymentMethod with the SDK and collect customer consent. Pass [allowRedisplay](https://docs.stripe.com/api/payment_methods/object.md#payment_method_object-allow_redisplay) as `always` or `limited`, indicating the degree to which a payment method can be shown in a customer checkout flow.

To collect a PaymentMethod, you must connect your app to a reader. In the `SetupIntentConfiguration`, set `moto` to `true`.

The connected reader prompts you to enter the customer’s card number, CVC, expiration date, and postal code after your app calls `collectSetupIntentPaymentMethod`.

```js
async () => {
  // Pass the client_secret from the SetupIntent you created in the previous step.
  const result = await terminal.collectSetupIntentPaymentMethod(
    client_secret,
    "always",
    {
      config: {
        moto: true,
      },
    },
  );
  if (result.error) {
    // Placeholder for handling result.error
  } else {
    // Placeholder for confirming result.setupIntent
  }
};
```

## Confirm and use the PaymentMethod

You can follow the usual procedure to [confirm the PaymentMethod](https://docs.stripe.com/terminal/features/saving-payment-details/save-directly.md?terminal-card-present-integration=terminal#submit-payment-method). You can now [charge the saved PaymentMethod](https://docs.stripe.com/payments/save-and-reuse.md#charge-saved-payment-method) associated with the customer using a PaymentIntent.

## Testing

Use the [simulated reader](https://docs.stripe.com/terminal/references/testing.md#simulated-reader) and [simulated test card numbers](https://docs.stripe.com/terminal/references/testing.md#simulated-test-cards) to test your integration.

## Compliance

You’re responsible for your compliance with all applicable laws, regulations, and network rules when saving a customer’s payment details. For example, the European Data Protection Board has issued guidance regarding saving payment details. These requirements generally apply if you want to save your customer’s payment method for future use. This applies in situations such as presenting a customer’s payment method to them in the checkout flow for a future purchase, or charging them when they’re not actively using your website or app, placing a MOTO order, or in your store.

Add terms to your checkout flow that state how you plan to save payment method details and allow customers to opt in. If you plan to charge the customer while they’re not actively checking out, make sure (at a minimum) that your terms also cover the following:

- The customer’s agreement to your initiating a payment or a series of payments on their behalf for specified transactions.
- The anticipated timing and frequency of payments (for instance, whether charges are for scheduled installment or subscription payments, or for unscheduled top-ups).
- How the payment amount is determined.
- Your cancellation policy, if you’re setting up the payment method for a subscription service.

Make sure you keep a record of your customer’s written agreement to these terms.

When you save a payment method, you can only use it for the specific purpose that you included in your terms. If you want to charge customers when they’re not actively checking out and also save the customer’s payment method to present to them as a saved payment method for future purchases, you must explicitly collect consent from the customer. One way to do so is with a “Save my payment method for future use” checkbox.

# React Native

> This is a React Native for when terminal-sdk-platform is react-native. View the full page at https://docs.stripe.com/terminal/features/mail-telephone-orders/save-directly?terminal-sdk-platform=react-native.

To save payment details from a MOTO for a future payment, you must:

1. [Create or retrieve a Customer](https://docs.stripe.com/terminal/features/mail-telephone-orders/save-directly.md#create-customer).
1. [Create a SetupIntent](https://docs.stripe.com/terminal/features/mail-telephone-orders/save-directly.md#create-setup-intent).
1. [Collect a PaymentMethod](https://docs.stripe.com/terminal/features/mail-telephone-orders/save-directly.md#collect-payment-method).
1. [Confirm and use the PaymentMethod](https://docs.stripe.com/terminal/features/mail-telephone-orders/save-directly.md#confirm-use-payment-method).

## Create or retrieve a Customer

To charge a card saved with Stripe, you must attach it to a [Customer](https://docs.stripe.com/api/customers.md).

When you include a customer in your [SetupIntent](https://docs.stripe.com/api/setup_intents.md) before confirming, Stripe automatically attaches the generated card payment method to the provided `Customer` object that you create/retrieve.

Include the following code on your server to create a new `Customer` object:

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const customer = await stripe.customers.create();
```

## Create a SetupIntent

A [SetupIntent](https://docs.stripe.com/api/setup_intents.md) is an object that represents your intent to set up a customer’s payment method for future payments. The SetupIntent tracks the steps of this setup process. For Terminal, this includes collecting and recording cardholder consent.

The [payment_method_types](https://docs.stripe.com/api/setup_intents/create.md#create_setup_intent-payment_method_types) must include `card`.

```js
const params = {
  customer: "{{CUSTOMER_ID}}",
  onBehalfOf: "{{ON_BEHALF_OF}}",
  description: "Customer A's Card",
  paymentMethodTypes: ["card"],
};

try {
  const setupIntent = await terminal.createSetupIntent(params);
  // Placeholder for handling successful operation
} catch (error) {
  // Placeholder for handling exception
}
```

## Collect a PaymentMethod

After you create a SetupIntent, the next step is to collect a PaymentMethod with the SDK and collect customer consent. Pass [allowRedisplay](https://docs.stripe.com/api/payment_methods/object.md#payment_method_object-allow_redisplay) as `always` or `limited`, indicating the degree to which a payment method can be shown in a customer checkout flow.

To collect a PaymentMethod, you must connect your app to a reader. Set `motoConfiguration` to `{ skipCvc: true }` when calling `collectSetupIntentPaymentMethod`.

The connected reader prompts you to enter the customer’s card number, CVC, expiration date, and postal code after your app calls `collectSetupIntentPaymentMethod`.

```js
try {
  const result = await collectSetupIntentPaymentMethod({
    setupIntent: setupIntent,
    allowRedisplay: "always",
    motoConfiguration: { skipCvc: true },
  });
  // Placeholder for handling successful operation
} catch (error) {
  // Placeholder for handling exception
}
```

## Confirm and use the PaymentMethod

You can follow the usual procedure to [confirm the PaymentMethod](https://docs.stripe.com/terminal/features/saving-payment-details/save-directly.md?terminal-card-present-integration=terminal#submit-payment-method). You can now [charge the saved PaymentMethod](https://docs.stripe.com/payments/save-and-reuse.md#charge-saved-payment-method) associated with the customer using a PaymentIntent.

## Testing

Use the [simulated reader](https://docs.stripe.com/terminal/references/testing.md#simulated-reader) and [simulated test card numbers](https://docs.stripe.com/terminal/references/testing.md#simulated-test-cards) to test your integration.

## Compliance

You’re responsible for your compliance with all applicable laws, regulations, and network rules when saving a customer’s payment details. For example, the European Data Protection Board has issued guidance regarding saving payment details. These requirements generally apply if you want to save your customer’s payment method for future use. This applies in situations such as presenting a customer’s payment method to them in the checkout flow for a future purchase, or charging them when they’re not actively using your website or app, placing a MOTO order, or in your store.

Add terms to your checkout flow that state how you plan to save payment method details and allow customers to opt in. If you plan to charge the customer while they’re not actively checking out, make sure (at a minimum) that your terms also cover the following:

- The customer’s agreement to your initiating a payment or a series of payments on their behalf for specified transactions.
- The anticipated timing and frequency of payments (for instance, whether charges are for scheduled installment or subscription payments, or for unscheduled top-ups).
- How the payment amount is determined.
- Your cancellation policy, if you’re setting up the payment method for a subscription service.

Make sure you keep a record of your customer’s written agreement to these terms.

When you save a payment method, you can only use it for the specific purpose that you included in your terms. If you want to charge customers when they’re not actively checking out and also save the customer’s payment method to present to them as a saved payment method for future purchases, you must explicitly collect consent from the customer. One way to do so is with a “Save my payment method for future use” checkbox.
