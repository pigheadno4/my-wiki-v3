<!-- Source URL: https://docs.stripe.com/terminal/features/saving-payment-details/save-directly -->
<!-- Fetched: 2026-05-01 -->

# Save directly without charging

Collect details of a present card and save them for online use.

> #### Use the Accounts v2 API to represent customers
>
> The Accounts v2 API is generally available for Connect users, and in public preview for other Stripe users. If you’re part of the Accounts v2 preview, you need to specify a [specify a preview version](https://docs.stripe.com/api-v2-overview.md#sdk-and-api-versioning) in your code.
>
> To request access to the Accounts v2 preview,
>
> For most use cases, we recommend [modeling your customers as customer-configured Account objects](https://docs.stripe.com/connect/use-accounts-as-customers.md) instead of using [Customer](https://docs.stripe.com/api/customers.md) objects.

Use [SetupIntents](https://docs.stripe.com/payments/setup-intents.md) to collect card or mobile wallet details without charging the card. A SetupIntent can’t save a `card_present` _PaymentMethod_ (PaymentMethods represent your customer's payment instruments, used with the Payment Intents or Setup Intents APIs) directly, but in most cases you can create a reusable `generated_card` PaymentMethod that represents the same card. From your customer’s perspective, they’re the same payment method.

> All charges made using the `generated_card` PaymentMethod are card-not-present (CNP) transactions, and features available to card-present transactions (such as _liability shifts_ (With some 3D Secure transactions, the liability for fraudulent chargebacks (stolen or counterfeit cards) shifts from you to the card issuer) and [pricing](https://stripe.com/terminal#pricing))don’t apply to these charges.

You can use [SetupIntents](https://docs.stripe.com/payments/setup-intents.md) to collect card details on Visa, Mastercard, American Express, Discover, and co-branded Interac, eftpos, and girocard cards. However, co-branded Interac cards must be inserted to a reader. This means that they aren’t supported by [Tap to Pay](https://docs.stripe.com/terminal/payments/setup-reader/tap-to-pay.md).

[SetupIntents](https://docs.stripe.com/payments/setup-intents.md) don’t support single-branded Interac, eftpos, and girocard cards.

Saving cards with Stripe Terminal using SetupIntents requires you to:

1. Create or retrieve a _Customer_ (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments) object.
1. Create a [SetupIntent](https://docs.stripe.com/api/setup_intents.md) object to track the process.
1. After you collect the customer’s consent, collect the payment method and submit the details to Stripe.

> We’ve changed the customer consent model of this feature to require the `allow_redisplay` parameter instead of the legacy `customer_consent_collected` parameter. If your integration uses `customer_consent_collected`, you must update your integration to use `allow_redisplay`. This update became mandatory on March 31, 2025 for non-React Native users, and is mandatory for React Native users on September 30, 2025. For guidance, see the [changelog entry](https://docs.stripe.com/changelog/acacia/2024-09-30/terminal-remove-customer-consent-require-allow-redisplay.md).

# Server-driven

> This is a Server-driven for when terminal-sdk-platform is server-driven. View the full page at https://docs.stripe.com/terminal/features/saving-payment-details/save-directly?terminal-sdk-platform=server-driven.

> The server-driven-based SetupIntents API is compatible with BBPOS WisePOS E and Stripe Reader S700/S710.

## Create or retrieve a customer

To charge a card saved with Stripe, you must attach it to a [Customer](https://docs.stripe.com/api/customers.md).

When you include a customer in your [SetupIntent](https://docs.stripe.com/api/setup_intents.md) before confirming, Stripe automatically attaches the generated card payment method to the [Customer](https://docs.stripe.com/api/customers.md) object you provide.

Include the following code on your server to create a new `Customer`.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const customer = await stripe.customers.create();
```

## Create a SetupIntent

> Provide a [Customer ID](https://docs.stripe.com/api/setup_intents/create.md#create_setup_intent-customer) while creating a SetupIntent to attach the card payment method to the `Customer` upon successful setup. If you don’t provide a Customer ID, you must attach the payment method in a separate call.

A [SetupIntent](https://docs.stripe.com/api/setup_intents.md) is an object that represents your intent to set up a customer’s payment method for future payments. The SetupIntent tracks the steps of this setup process. For Terminal, this includes collecting and recording cardholder consent.

- [Create a SetupIntent](https://docs.stripe.com/api/setup_intents/create.md)

You must create the SetupIntent on your server and include `card_present` on the `payment_method_types` parameter. Specify `usage=on_session` if you only intend to reuse the payment method when the customer is in your checkout flow.

#### Node.js

```javascript
const express = require('express');
const app = express();
app.post('/create_setup_intent', async (req, res) => {
  const intent = // ... Fetch or create the SetupIntent
  res.json({id: intent.id});
});
app.listen(3000, () => {
  console.log('Running on port 3000');
});
```

## Collect a payment method for saving

- [process_setup_intent](https://docs.stripe.com/api/terminal/readers/process_setup_intent.md)

After you create a SetupIntent, you need to collect a payment method and collect customer consent. Pass [allow_redisplay](https://docs.stripe.com/api/payment_methods/object.md#payment_method_object-allow_redisplay) as `always` or `limited`, indicating the degree to which a payment method can be shown in a customer checkout flow.

> Collect customer consent verbally or with a checkbox in your application. You must comply with all applicable laws, rules, and regulations in your region.

You must call the [process_setup_intent](https://docs.stripe.com/api/terminal/readers/process_setup_intent.md) endpoint, which handles both collecting and confirming the SetupIntent. If the customer provides consent, set `allow_redisplay` to either `always` or `limited`.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const reader = await stripe.terminal.readers.processSetupIntent(
  '{{READER_ID}}',
  {
    setup_intent: '{{SETUP_INTENT_ID}}',
    allow_redisplay: 'always',
  }
);
```

This method collects encrypted payment method data using the connected card reader, and associates the encrypted data with the SetupIntent.

> Collecting a payment method happens locally and requires no authorization or updates to the SetupIntent object until the next step.

### Cancel collection

#### Programmatic cancellation

- [cancel_action](https://docs.stripe.com/api/terminal/readers/cancel_action.md)

You can cancel collecting a payment method by calling [cancel_action](https://docs.stripe.com/api/terminal/readers/cancel_action.md).

## Submit the payment method details to Stripe

Your previous call to [process_setup_intent](https://docs.stripe.com/api/terminal/readers/process_setup_intent.md) handles the _confirm_ (Confirming an intent indicates that the customer intends to use the current or provided payment method. Upon confirmation, the intent attempts to initiate the portions of the flow that have real-world side effects) for you, so no further action is necessary.

A successful setup returns a `succeeded` value for the SetupIntent’s [status](https://docs.stripe.com/api/setup_intents/object.md#setup_intent_object-status) property, along with a [SetupAttempt.payment_method_details.card_present.generated_card](https://docs.stripe.com/api/setup_attempts/object.md#setup_attempt_object-payment_method_details-card_present-generated_card), which is a reusable `card` payment method you can use for online payments.

> The [SetupIntent.payment_method](https://docs.stripe.com/api/setup_intents/object.md#setup_intent_object-payment_method) is a `card_present` PaymentMethod that represents the tokenization of the physically present card and isn’t chargeable online. Future payments use the generated card instead. From the customer’s perspective, they’re the same payment method.

The `generated_card` payment method automatically attaches to the customer you provided during [SetupIntent creation](https://docs.stripe.com/terminal/features/saving-payment-details/save-directly.md#create-setupintent). You can retrieve the `generated_card` payment method by expanding the SetupIntent’s `latest_attempt` property. Always check for a `generated_card` value, because for payment methods that don’t allow generated cards, the value is empty.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const setupIntent = await stripe.setupIntents.retrieve(
  '{{SETUPINTENT_ID}}',
  {
    expand: ['latest_attempt'],
  }
);
```

Alternatively, you can retrieve the attached payment method by fetching the list of payment methods that gets attached to the customer.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const paymentMethods = await stripe.customers.listPaymentMethods(
  '{{CUSTOMER_ID}}',
  {
    type: 'card',
  }
);
```

If you didn’t provide a customer during SetupIntent creation, you can attach the `generated_card` to a Customer object in a separate call.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const paymentMethod = await stripe.paymentMethods.attach(
  '{{PAYMENTMETHOD_ID}}',
  {
    customer: '{{CUSTOMER_ID}}',
  }
);
```

If the setup isn’t successful, inspect the returned error to determine the cause. For example, failing to collect and notify Stripe of customer consent results in an error.

## Mobile wallets considerations

Saved mobile wallets is only for [off_session](https://docs.stripe.com/api/payment_intents/confirm.md#confirm_payment_intent-off_session) payments such as future subscription or other payments you initiate on behalf of your customer. When you save a digital wallet payment method, the `generated_card` has `allow_redisplay=limited`, to indicate its specific usage considerations.

When you attempt to charge a mobile wallet, make sure to pass `off_session=true` during PaymentIntent confirmation. If the customer is present in your checkout flow, you’ll need to instead use the [Apple Pay](https://docs.stripe.com/apple-pay.md) and [Google Pay](https://docs.stripe.com/google-pay.md) integrations to re-prompt for payment method presentment.

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

> This is a JavaScript for when terminal-sdk-platform is js. View the full page at https://docs.stripe.com/terminal/features/saving-payment-details/save-directly?terminal-sdk-platform=js.

## Create or retrieve a customer

To charge a card saved with Stripe, you must attach it to a [Customer](https://docs.stripe.com/api/customers.md).

When you include a customer in your [SetupIntent](https://docs.stripe.com/api/setup_intents.md) before confirming, Stripe automatically attaches the generated card payment method to the [Customer](https://docs.stripe.com/api/customers.md) object you provide.

Include the following code on your server to create a new `Customer`.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const customer = await stripe.customers.create();
```

## Create a SetupIntent

> Provide a [Customer ID](https://docs.stripe.com/api/setup_intents/create.md#create_setup_intent-customer) while creating a SetupIntent to attach the card payment method to the `Customer` upon successful setup. If you don’t provide a Customer ID, you must attach the payment method in a separate call.

A [SetupIntent](https://docs.stripe.com/api/setup_intents.md) is an object that represents your intent to set up a customer’s payment method for future payments. The SetupIntent tracks the steps of this setup process. For Terminal, this includes collecting and recording cardholder consent.

- [Create a SetupIntent](https://docs.stripe.com/api/setup_intents/create.md)

You must create the SetupIntent on your server and include `card_present` on the `payment_method_types` parameter. Specify `usage=on_session` if you only intend to reuse the payment method when the customer is in your checkout flow.

The SetupIntent contains a [client secret](https://docs.stripe.com/api/setup_intents/object.md#setup_intent_object-client_secret), which is a key that’s unique to the individual SetupIntent. You must obtain the _client secret_ (The client secret is a unique key returned from Stripe as part of a PaymentIntent. This key lets the client access important fields from the PaymentIntent (status, amount, currency) while hiding sensitive ones (metadata, customer)) from the SetupIntent on your server and pass it to the client side.

#### Node.js

```javascript
const express = require('express');
const app = express();
app.post('/create_setup_intent', async (req, res) => {
  const intent = // ... Fetch or create the SetupIntent
  res.json({id: intent.id, client_secret: intent.client_secret});
});
app.listen(3000, () => {
  console.log('Running on port 3000');
});
```

## Collect a payment method for saving

- [collectSetupIntentPaymentMethod (JavaScript)](https://docs.stripe.com/terminal/references/api/js-sdk.md#collect-setup-intent-payment-method)

After you create a SetupIntent, you need to collect a payment method using the SDK and collect customer consent. Pass [allowRedisplay](https://docs.stripe.com/api/payment_methods/object.md#payment_method_object-allow_redisplay) as `always` or `limited`, indicating the degree to which a payment method can be shown in a customer checkout flow.

> Collect customer consent verbally or with a checkbox in your application. You must comply with all applicable laws, rules, and regulations in your region.

To collect a payment method, make sure that you’re connected to a reader. The connected reader waits for a card after your app calls `collectSetupIntentPaymentMethod`.

```javascript
async () => {
  // clientSecret is the client_secret from the SetupIntent you created in Step 1.
  const result = await terminal.collectSetupIntentPaymentMethod(clientSecret, "always");
  if (result.error) {
    // Placeholder for handling result.error
  } else {
    // Placeholder for confirming result.setupIntent
  }
}
```

This method collects encrypted payment method data using the connected card reader, and associates the encrypted data with the SetupIntent.

> Collecting a payment method happens locally and requires no authorization or updates to the SetupIntent object until the next step.

### Cancel collection

#### Programmatic cancellation

You can cancel collecting a payment method by calling [cancelCollectSetupIntentPaymentMethod](https://docs.stripe.com/terminal/references/api/js-sdk.md#cancel-collect-setup-intent-payment-method) in the SDK.

#### Customer-initiated cancellation

When you set [enable_customer_cancellation](https://docs.stripe.com/terminal/references/api/js-sdk.md#collect-setup-intent-payment-method) to true for a transaction, smart reader users see a cancel button. Tapping the cancel button cancels the active transaction.

```javascript
terminal.collectSetupIntentPaymentMethod(
  setupIntent,
  allowRedisplay,{
    enable_customer_cancellation: true
  }
)
```

## Submit the payment method details to Stripe

- [confirmSetupIntent (JavaScript)](https://docs.stripe.com/terminal/references/api/js-sdk.md#confirm-setup-intent)

Use `confirmSetupIntent` to complete the setup.

A successful setup returns a `succeeded` value for the SetupIntent’s [status](https://docs.stripe.com/api/setup_intents/object.md#setup_intent_object-status) property, along with a [SetupAttempt.payment_method_details.card_present.generated_card](https://docs.stripe.com/api/setup_attempts/object.md#setup_attempt_object-payment_method_details-card_present-generated_card), which is a reusable `card` payment method you can use for online payments.

> The [SetupIntent.payment_method](https://docs.stripe.com/api/setup_intents/object.md#setup_intent_object-payment_method) is a `card_present` PaymentMethod that represents the tokenization of the physically present card and isn’t chargeable online. Future payments use the generated card instead. From the customer’s perspective, they’re the same payment method.

The `generated_card` payment method automatically attaches to the customer you provided during [SetupIntent creation](https://docs.stripe.com/terminal/features/saving-payment-details/save-directly.md#create-setupintent). You can retrieve the `generated_card` payment method by expanding the SetupIntent’s `latest_attempt` property. Always check for a `generated_card` value, because for payment methods that don’t allow generated cards, the value is empty.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const setupIntent = await stripe.setupIntents.retrieve(
  '{{SETUPINTENT_ID}}',
  {
    expand: ['latest_attempt'],
  }
);
```

Alternatively, you can retrieve the attached payment method by fetching the list of payment methods that gets attached to the customer.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const paymentMethods = await stripe.customers.listPaymentMethods(
  '{{CUSTOMER_ID}}',
  {
    type: 'card',
  }
);
```

If you didn’t provide a customer during SetupIntent creation, you can attach the `generated_card` to a Customer object in a separate call.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const paymentMethod = await stripe.paymentMethods.attach(
  '{{PAYMENTMETHOD_ID}}',
  {
    customer: '{{CUSTOMER_ID}}',
  }
);
```

If the setup isn’t successful, inspect the returned error to determine the cause. For example, failing to collect and notify Stripe of customer consent results in an error.

## Mobile wallets considerations

Saved mobile wallets is only for [off_session](https://docs.stripe.com/api/payment_intents/confirm.md#confirm_payment_intent-off_session) payments such as future subscription or other payments you initiate on behalf of your customer. When you save a digital wallet payment method, the `generated_card` has `allow_redisplay=limited`, to indicate its specific usage considerations.

When you attempt to charge a mobile wallet, make sure to pass `off_session=true` during PaymentIntent confirmation. If the customer is present in your checkout flow, you’ll need to instead use the [Apple Pay](https://docs.stripe.com/apple-pay.md) and [Google Pay](https://docs.stripe.com/google-pay.md) integrations to re-prompt for payment method presentment.

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

> This is a iOS for when terminal-sdk-platform is ios. View the full page at https://docs.stripe.com/terminal/features/saving-payment-details/save-directly?terminal-sdk-platform=ios.

> In version `5.0.0` of the SDK, the collect and confirm integration steps are now combined into a single `processSetupIntent` step.

## Create or retrieve a customer

To charge a card saved with Stripe, you must attach it to a [Customer](https://docs.stripe.com/api/customers.md).

When you include a customer in your [SetupIntent](https://docs.stripe.com/api/setup_intents.md) before confirming, Stripe automatically attaches the generated card payment method to the [Customer](https://docs.stripe.com/api/customers.md) object you provide.

Include the following code on your server to create a new `Customer`.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const customer = await stripe.customers.create();
```

## Create a SetupIntent

> Provide a [Customer ID](https://docs.stripe.com/api/setup_intents/create.md#create_setup_intent-customer) while creating a SetupIntent to attach the card payment method to the `Customer` upon successful setup. If you don’t provide a Customer ID, you must attach the payment method in a separate call.

A [SetupIntent](https://docs.stripe.com/api/setup_intents.md) is an object that represents your intent to set up a customer’s payment method for future payments. The SetupIntent tracks the steps of this setup process. For Terminal, this includes collecting and recording cardholder consent.

- [SetupIntentParameters (iOS)](https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPSetupIntentParameters.html)

You can create a SetupIntent providing the `customer`, `onBehalfOf` (_Connect_ (Connect is Stripe's solution for multi-party businesses, such as marketplace or software platforms, to route payments between sellers, customers, and other recipients) only), and `usage` parameters.

#### Swift

```swift
import UIKit
import StripeTerminal

class PaymentViewController: UIViewController {

    // Action for a "Save Card" button
    func saveCardAction() throws {
        let params = try SetupIntentParametersBuilder().setCustomer(""{{CUSTOMER_ID}}"")
        Terminal.shared.createSetupIntent(params) { createResult, createError in
            if let error = createError {
                print("createSetupIntent failed: \(error)")
            } else if let setupIntent = createResult {
                print("createSetupIntent succeeded")
                // ...
            }
        }
    }

    // ...
}

```

If the information required to start a payment isn’t readily available in your app, you can [create the SetupIntent](https://docs.stripe.com/api/setup_intents/create.md) on your server. Use the client secret to call `retrieveSetupIntent`, and, then use the retrieved SetupIntent to call `processSetupIntent`.

## Collect a payment method for saving

- [retrieveSetupIntent (iOS)](<https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPTerminal.html#/c:objc(cs)SCPTerminal(im)retrieveSetupIntent:delegate:completion:>)
- [processSetupIntent (iOS)](<https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPTerminal.html#/c:objc(cs)SCPTerminal(im)processSetupIntent:collectConfig:completion:>)

After you create a SetupIntent, you need to collect a payment method using the SDK and collect customer consent. Pass [allowRedisplay](https://docs.stripe.com/api/payment_methods/object.md#payment_method_object-allow_redisplay) as `always` or `limited`, indicating the degree to which a payment method can be shown in a customer checkout flow.

> Collect customer consent verbally or with a checkbox in your application. You must comply with all applicable laws, rules, and regulations in your region.

To process a setup intent, make sure that you’re connected to a reader. The connected reader waits for a card after your app calls `processSetupIntent`.

#### Swift

```swift


import UIKit
import StripeTerminal

class PaymentViewController: UIViewController, ReaderDisplayDelegate {
    // Label for displaying messages from the card reader
    let readerMessageLabel = UILabel(frame: .zero)
    var collectCancelable: Cancelable? = nil

    // ...

    // Action for a "Subscribe" button
    func subscribeAction() throws {
        let params = try SetupIntentParametersBuilder().setCustomer(""{{CUSTOMER_ID}}"").build()
        Terminal.shared.createSetupIntent(params) { createResult, createError in
            if let error = createError {
                print("createSetupIntent failed: \(error)")
            } else if let setupIntent = createResult {
                print("createSetupIntent succeeded")
                let config = try CollectSetupIntentConfigurationBuilder()
                    .setAllowRedisplay(.always)
                    .build()
                self.collectCancelable = Terminal.shared.processSetupIntent(setupIntent, collectConfig: config) { processedSetupIntent, processError in
                    if let error = processError {
                        print("processSetupIntent failed: \(error)")
                    } else if let processedSetupIntent = processedSetupIntent {
                        print("processSetupIntent succeeded")
                    }
                }
            }
        }
    }
}
```

This method collects encrypted payment method data using the connected card reader, and associates the encrypted data with the SetupIntent.

> Collecting a payment method happens locally and requires no authorization or updates to the SetupIntent object until the next step.

### Cancel collection

#### Programmatic cancellation

You can cancel collecting a payment method by using the [Cancelable](https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPCancelable.html) object returned by the SDK.

#### Customer-initiated cancellation

CustomerCancellation is enabled by default, so smart reader users see a cancel button. Tapping the cancel button cancels the active transaction. Use [setCustomerCancellation](<https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPCollectSetupIntentConfigurationBuilder.html#/c:objc(cs)SCPCollectSetupIntentConfigurationBuilder(im)setCustomerCancellation>) to toggle this behavior for a transaction.

#### Swift

```swift
let setupConfig = try CollectSetupIntentConfiguration()
    .build()
Terminal.shared.collectSetupIntentPaymentMethod(intent, allowRedisplay: AllowRedisplay.always, setupConfig: setupConfig) {
    collectedSetupIntent, collectError in
}
```

## Submit the payment method details to Stripe

Your previous call to `processSetupIntent` handles the _confirm_ (Confirming an intent indicates that the customer intends to use the current or provided payment method. Upon confirmation, the intent attempts to initiate the portions of the flow that have real-world side effects) for you, so no further action is necessary.

A successful setup returns a `succeeded` value for the SetupIntent’s [status](https://docs.stripe.com/api/setup_intents/object.md#setup_intent_object-status) property, along with a [SetupAttempt.payment_method_details.card_present.generated_card](https://docs.stripe.com/api/setup_attempts/object.md#setup_attempt_object-payment_method_details-card_present-generated_card), which is a reusable `card` payment method you can use for online payments.

> The [SetupIntent.payment_method](https://docs.stripe.com/api/setup_intents/object.md#setup_intent_object-payment_method) is a `card_present` PaymentMethod that represents the tokenization of the physically present card and isn’t chargeable online. Future payments use the generated card instead. From the customer’s perspective, they’re the same payment method.

The `generated_card` payment method automatically attaches to the customer you provided during [SetupIntent creation](https://docs.stripe.com/terminal/features/saving-payment-details/save-directly.md#create-setupintent). You can retrieve the `generated_card` payment method by expanding the SetupIntent’s `latest_attempt` property. Always check for a `generated_card` value, because for payment methods that don’t allow generated cards, the value is empty.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const setupIntent = await stripe.setupIntents.retrieve(
  '{{SETUPINTENT_ID}}',
  {
    expand: ['latest_attempt'],
  }
);
```

Alternatively, you can retrieve the attached payment method by fetching the list of payment methods that gets attached to the customer.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const paymentMethods = await stripe.customers.listPaymentMethods(
  '{{CUSTOMER_ID}}',
  {
    type: 'card',
  }
);
```

If you didn’t provide a customer during SetupIntent creation, you can attach the `generated_card` to a Customer object in a separate call.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const paymentMethod = await stripe.paymentMethods.attach(
  '{{PAYMENTMETHOD_ID}}',
  {
    customer: '{{CUSTOMER_ID}}',
  }
);
```

If the setup isn’t successful, inspect the returned error to determine the cause. For example, failing to collect and notify Stripe of customer consent results in an error.

#### Swift

```swift


// Action for a "Save Card" button
func saveCardAction() throws {
  let params = try SetupIntentParametersBuilder.setCustomer(""{{CUSTOMER_ID}}"").build()
  Terminal.shared.createSetupIntent(params) { createResult, createError in
      if let error = createError {
          print("createSetupIntent failed: \(error)")
      } else if let setupIntent = createResult {
          print("createSetupIntent succeeded")
          let config = try CollectSetupIntentConfigurationBuilder()
              .setAllowRedisplay(.always)
              .build()
          self.collectCancelable = Terminal.shared.processSetupIntent(setupIntent, collectConfig: config) { processedSetupIntent, processError in
              if let error = processError {
                  print("processSetupIntent failed: \(error)")
              } else if let processedSetupIntent = processedSetupIntent {
                  print("processSetupIntent succeeded")
              }
          }
      }
  }
}
```

## Mobile wallets considerations

Saved mobile wallets is only for [off_session](https://docs.stripe.com/api/payment_intents/confirm.md#confirm_payment_intent-off_session) payments such as future subscription or other payments you initiate on behalf of your customer. When you save a digital wallet payment method, the `generated_card` has `allow_redisplay=limited`, to indicate its specific usage considerations.

When you attempt to charge a mobile wallet, make sure to pass `off_session=true` during PaymentIntent confirmation. If the customer is present in your checkout flow, you’ll need to instead use the [Apple Pay](https://docs.stripe.com/apple-pay.md) and [Google Pay](https://docs.stripe.com/google-pay.md) integrations to re-prompt for payment method presentment.

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

> This is a Android for when terminal-sdk-platform is android. View the full page at https://docs.stripe.com/terminal/features/saving-payment-details/save-directly?terminal-sdk-platform=android.

> In version `5.0.0` of the SDK, the collect and confirm integration steps are now combined into a single `processSetupIntent` step.

## Create or retrieve a customer

To charge a card saved with Stripe, you must attach it to a [Customer](https://docs.stripe.com/api/customers.md).

When you include a customer in your [SetupIntent](https://docs.stripe.com/api/setup_intents.md) before confirming, Stripe automatically attaches the generated card payment method to the [Customer](https://docs.stripe.com/api/customers.md) object you provide.

Include the following code on your server to create a new `Customer`.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const customer = await stripe.customers.create();
```

## Create a SetupIntent

> Provide a [Customer ID](https://docs.stripe.com/api/setup_intents/create.md#create_setup_intent-customer) while creating a SetupIntent to attach the card payment method to the `Customer` upon successful setup. If you don’t provide a Customer ID, you must attach the payment method in a separate call.

A [SetupIntent](https://docs.stripe.com/api/setup_intents.md) is an object that represents your intent to set up a customer’s payment method for future payments. The SetupIntent tracks the steps of this setup process. For Terminal, this includes collecting and recording cardholder consent.

- [SetupIntentParameters (Android)](https://stripe.dev/stripe-terminal-android/external/com.stripe.stripeterminal.external.models/-setup-intent-parameters/index.html)

You can create a SetupIntent providing the `customer`, `onBehalfOf` (_Connect_ (Connect is Stripe's solution for multi-party businesses, such as marketplace or software platforms, to route payments between sellers, customers, and other recipients) only), and `usage` parameters.

#### Kotlin

```kotlin
val params = SetupIntentParameters.Builder()
    .setCustomer(""{{CUSTOMER_ID}}"")
    .build()

Terminal.getInstance().createSetupIntent(
    params, object : SetupIntentCallback {
        override fun onSuccess(setupIntent: SetupIntent) {
            // Placeholder for handling successful operation
        }

        override fun onFailure(e: TerminalException) {
            // Placeholder for handling exception
        }
    }
)
```

If the information required to start a payment isn’t readily available in your app, you can [create the SetupIntent](https://docs.stripe.com/api/setup_intents/create.md) on your server. Use the client secret to call `retrieveSetupIntent`, and, then use the retrieved SetupIntent to call `processSetupIntent`.

## Collect a payment method for saving

- [retrieveSetupIntent (Android)](https://stripe.dev/stripe-terminal-android/core/com.stripe.stripeterminal/-terminal/retrieve-setup-intent.html)
- [processSetupIntent (Android)](https://stripe.dev/stripe-terminal-android/core/com.stripe.stripeterminal/-terminal/process-setup-intent.html)

After you create a SetupIntent, you need to collect a payment method using the SDK and collect customer consent. Pass [allowRedisplay](https://docs.stripe.com/api/payment_methods/object.md#payment_method_object-allow_redisplay) as `always` or `limited`, indicating the degree to which a payment method can be shown in a customer checkout flow.

> Collect customer consent verbally or with a checkbox in your application. You must comply with all applicable laws, rules, and regulations in your region.

To process a setup intent, make sure that you’re connected to a reader. The connected reader waits for a card after your app calls `processSetupIntent`.

#### Kotlin

```kotlin
val config = CollectSetupIntentConfiguration.Builder()
    .build()

val cancelable = Terminal.getInstance().processSetupIntent(
    setupIntent,
    AllowRedisplay.ALWAYS,
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

This method collects encrypted payment method data using the connected card reader, and associates the encrypted data with the SetupIntent.

> Collecting a payment method happens locally and requires no authorization or updates to the SetupIntent object until the next step.

### Cancel collection

#### Programmatic cancellation

You can cancel collecting a payment method by using the [Cancelable](https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPCancelable.html) object returned by the SDK.

#### Customer-initiated cancellation

CustomerCancellation is enabled by default, so smart reader users see a cancel button. Tapping the cancel button cancels the active transaction. Use [setCustomerCancellation](https://stripe.dev/stripe-terminal-android/external/com.stripe.stripeterminal.external.models/-collect-setup-intent-configuration/-builder/set-customer-cancellation.html) to toggle this behavior for a transaction.

#### Kotlin

```kotlin
Terminal.getInstance().collectSetupIntentPaymentMethod(
    setupIntent,
    AllowRedisplay.ALWAYS,SetupIntentConfiguration.Builder()
        .build(),
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

## Submit the payment method details to Stripe

Your previous call to `processSetupIntent` handles the _confirm_ (Confirming an intent indicates that the customer intends to use the current or provided payment method. Upon confirmation, the intent attempts to initiate the portions of the flow that have real-world side effects) for you, so no further action is necessary.

A successful setup returns a `succeeded` value for the SetupIntent’s [status](https://docs.stripe.com/api/setup_intents/object.md#setup_intent_object-status) property, along with a [SetupAttempt.payment_method_details.card_present.generated_card](https://docs.stripe.com/api/setup_attempts/object.md#setup_attempt_object-payment_method_details-card_present-generated_card), which is a reusable `card` payment method you can use for online payments.

> The [SetupIntent.payment_method](https://docs.stripe.com/api/setup_intents/object.md#setup_intent_object-payment_method) is a `card_present` PaymentMethod that represents the tokenization of the physically present card and isn’t chargeable online. Future payments use the generated card instead. From the customer’s perspective, they’re the same payment method.

The `generated_card` payment method automatically attaches to the customer you provided during [SetupIntent creation](https://docs.stripe.com/terminal/features/saving-payment-details/save-directly.md#create-setupintent). You can retrieve the `generated_card` payment method by expanding the SetupIntent’s `latest_attempt` property. Always check for a `generated_card` value, because for payment methods that don’t allow generated cards, the value is empty.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const setupIntent = await stripe.setupIntents.retrieve(
  '{{SETUPINTENT_ID}}',
  {
    expand: ['latest_attempt'],
  }
);
```

Alternatively, you can retrieve the attached payment method by fetching the list of payment methods that gets attached to the customer.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const paymentMethods = await stripe.customers.listPaymentMethods(
  '{{CUSTOMER_ID}}',
  {
    type: 'card',
  }
);
```

If you didn’t provide a customer during SetupIntent creation, you can attach the `generated_card` to a Customer object in a separate call.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const paymentMethod = await stripe.paymentMethods.attach(
  '{{PAYMENTMETHOD_ID}}',
  {
    customer: '{{CUSTOMER_ID}}',
  }
);
```

If the setup isn’t successful, inspect the returned error to determine the cause. For example, failing to collect and notify Stripe of customer consent results in an error.

## Mobile wallets considerations

Saved mobile wallets is only for [off_session](https://docs.stripe.com/api/payment_intents/confirm.md#confirm_payment_intent-off_session) payments such as future subscription or other payments you initiate on behalf of your customer. When you save a digital wallet payment method, the `generated_card` has `allow_redisplay=limited`, to indicate its specific usage considerations.

When you attempt to charge a mobile wallet, make sure to pass `off_session=true` during PaymentIntent confirmation. If the customer is present in your checkout flow, you’ll need to instead use the [Apple Pay](https://docs.stripe.com/apple-pay.md) and [Google Pay](https://docs.stripe.com/google-pay.md) integrations to re-prompt for payment method presentment.

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

> This is a React Native for when terminal-sdk-platform is react-native. View the full page at https://docs.stripe.com/terminal/features/saving-payment-details/save-directly?terminal-sdk-platform=react-native.

> In version `0.0.1-beta.29` of the React Native SDK, you can use the [processSetupIntent](https://stripe.dev/stripe-terminal-react-native/api-reference/interfaces/StripeTerminalSdkType.html#processsetupintent) method to combine the collect and confirm integration steps into a single API call.

## Create or retrieve a customer

To charge a card saved with Stripe, you must attach it to a [Customer](https://docs.stripe.com/api/customers.md).

When you include a customer in your [SetupIntent](https://docs.stripe.com/api/setup_intents.md) before confirming, Stripe automatically attaches the generated card payment method to the [Customer](https://docs.stripe.com/api/customers.md) object you provide.

Include the following code on your server to create a new `Customer`.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const customer = await stripe.customers.create();
```

## Create a SetupIntent

> Provide a [Customer ID](https://docs.stripe.com/api/setup_intents/create.md#create_setup_intent-customer) while creating a SetupIntent to attach the card payment method to the `Customer` upon successful setup. If you don’t provide a Customer ID, you must attach the payment method in a separate call.

A [SetupIntent](https://docs.stripe.com/api/setup_intents.md) is an object that represents your intent to set up a customer’s payment method for future payments. The SetupIntent tracks the steps of this setup process. For Terminal, this includes collecting and recording cardholder consent.

- [CreateSetupIntentParams (React Native)](https://stripe.dev/stripe-terminal-react-native/api-reference/index.html#CreateSetupIntentParams)

You can create a SetupIntent providing the `customer`, `onBehalfOf` (_Connect_ (Connect is Stripe's solution for multi-party businesses, such as marketplace or software platforms, to route payments between sellers, customers, and other recipients) only), and `usage` parameters.

```js
const { createSetupIntent } = useStripeTerminal();

const { paymentIntent, error } = await createSetupIntent({
  customer: "{{CUSTOMER_ID}}",
});

if (error) {
  // Placeholder for handling exception
  return;
}

// Placeholder for collecting a payment method with setupIntent
```

If the information required to start a payment isn’t readily available in your app, you can [create the SetupIntent](https://docs.stripe.com/api/setup_intents/create.md) on your server. Use the client secret to call `retrieveSetupIntent`, and, then use the retrieved SetupIntent to call `collectSetupIntentPaymentMethod`.

## Collect a payment method for saving

- [retrieveSetupIntent (React Native)](https://stripe.dev/stripe-terminal-react-native/api-reference/interfaces/StripeTerminalSdkType.html#retrieveSetupIntent)
- [collectSetupIntentPaymentMethod (React Native)](https://stripe.dev/stripe-terminal-react-native/api-reference/interfaces/StripeTerminalSdkType.html#collectSetupIntentPaymentMethod)

After you create a SetupIntent, you need to collect a payment method using the SDK and collect customer consent. Pass [allowRedisplay](https://docs.stripe.com/api/payment_methods/object.md#payment_method_object-allow_redisplay) as `always` or `limited`, indicating the degree to which a payment method can be shown in a customer checkout flow.

> Collect customer consent verbally or with a checkbox in your application. You must comply with all applicable laws, rules, and regulations in your region.

To collect a payment method, make sure that you’re connected to a reader. The connected reader waits for a card after your app calls `collectSetupIntentPaymentMethod`.

```js
const { setupIntent, error } = await collectSetupIntentPaymentMethod({
  setupIntent: setupIntent,
  allowRedisplay: "always",
});

if (error) {
  // Placeholder for handling exception
  return;
}

// Placeholder for confirming setupIntent
```

This method collects encrypted payment method data using the connected card reader, and associates the encrypted data with the SetupIntent.

> Collecting a payment method happens locally and requires no authorization or updates to the SetupIntent object until the next step.

### Cancel collection

#### Programmatic cancellation

You can cancel collecting a payment method by calling [cancelCollectSetupIntent](https://stripe.dev/stripe-terminal-react-native/api-reference/interfaces/StripeTerminalSdkType.html#cancelCollectSetupIntent) in the SDK.

#### Customer-initiated cancellation

Smart readers show customers a cancel button by default. You can disable this by setting [customerCancellation](https://stripe.dev/stripe-terminal-react-native/api-reference/types/CollectSetupIntentPaymentMethodParams.html) to `'disableIfAvailable'`. Tapping the cancel button cancels the active transaction.

```js
const { setupIntent, error } = await collectSetupIntentPaymentMethod({
  setupIntentId: setupIntentId,
  allowRedisplay: "always",
  customerCancellation: "enableIfAvailable",
});

if (error) {
  // Placeholder for handling exception
}

// Placeholder for processing SetupIntent
```

## Submit the payment method details to Stripe

- [confirmSetupIntent (React Native)](https://stripe.dev/stripe-terminal-react-native/api-reference/interfaces/StripeTerminalSdkType.html#confirmSetupIntent)

Use `confirmSetupIntent` to complete the setup.

A successful setup returns a `succeeded` value for the SetupIntent’s [status](https://docs.stripe.com/api/setup_intents/object.md#setup_intent_object-status) property, along with a [SetupAttempt.payment_method_details.card_present.generated_card](https://docs.stripe.com/api/setup_attempts/object.md#setup_attempt_object-payment_method_details-card_present-generated_card), which is a reusable `card` payment method you can use for online payments.

> The [SetupIntent.payment_method](https://docs.stripe.com/api/setup_intents/object.md#setup_intent_object-payment_method) is a `card_present` PaymentMethod that represents the tokenization of the physically present card and isn’t chargeable online. Future payments use the generated card instead. From the customer’s perspective, they’re the same payment method.

The `generated_card` payment method automatically attaches to the customer you provided during [SetupIntent creation](https://docs.stripe.com/terminal/features/saving-payment-details/save-directly.md#create-setupintent). You can retrieve the `generated_card` payment method by expanding the SetupIntent’s `latest_attempt` property. Always check for a `generated_card` value, because for payment methods that don’t allow generated cards, the value is empty.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const setupIntent = await stripe.setupIntents.retrieve(
  '{{SETUPINTENT_ID}}',
  {
    expand: ['latest_attempt'],
  }
);
```

Alternatively, you can retrieve the attached payment method by fetching the list of payment methods that gets attached to the customer.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const paymentMethods = await stripe.customers.listPaymentMethods(
  '{{CUSTOMER_ID}}',
  {
    type: 'card',
  }
);
```

If you didn’t provide a customer during SetupIntent creation, you can attach the `generated_card` to a Customer object in a separate call.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const paymentMethod = await stripe.paymentMethods.attach(
  '{{PAYMENTMETHOD_ID}}',
  {
    customer: '{{CUSTOMER_ID}}',
  }
);
```

If the setup isn’t successful, inspect the returned error to determine the cause. For example, failing to collect and notify Stripe of customer consent results in an error.

```js
const { setupIntent, error } = await confirmSetupIntent({
  setupIntent: setupIntent,
});

if (error) {
  // Placeholder for handling exception
  return;
}

// The SetupIntent is now ready to be used as a payment method on a future payment
```

## Mobile wallets considerations

Saved mobile wallets is only for [off_session](https://docs.stripe.com/api/payment_intents/confirm.md#confirm_payment_intent-off_session) payments such as future subscription or other payments you initiate on behalf of your customer. When you save a digital wallet payment method, the `generated_card` has `allow_redisplay=limited`, to indicate its specific usage considerations.

When you attempt to charge a mobile wallet, make sure to pass `off_session=true` during PaymentIntent confirmation. If the customer is present in your checkout flow, you’ll need to instead use the [Apple Pay](https://docs.stripe.com/apple-pay.md) and [Google Pay](https://docs.stripe.com/google-pay.md) integrations to re-prompt for payment method presentment.

## Compliance

You’re responsible for your compliance with all applicable laws, regulations, and network rules when saving a customer’s payment details. For example, the European Data Protection Board has issued guidance regarding saving payment details. These requirements generally apply if you want to save your customer’s payment method for future use. This applies in situations such as presenting a customer’s payment method to them in the checkout flow for a future purchase, or charging them when they’re not actively using your website or app, placing a MOTO order, or in your store.

Add terms to your checkout flow that state how you plan to save payment method details and allow customers to opt in. If you plan to charge the customer while they’re not actively checking out, make sure (at a minimum) that your terms also cover the following:

- The customer’s agreement to your initiating a payment or a series of payments on their behalf for specified transactions.
- The anticipated timing and frequency of payments (for instance, whether charges are for scheduled installment or subscription payments, or for unscheduled top-ups).
- How the payment amount is determined.
- Your cancellation policy, if you’re setting up the payment method for a subscription service.

Make sure you keep a record of your customer’s written agreement to these terms.

When you save a payment method, you can only use it for the specific purpose that you included in your terms. If you want to charge customers when they’re not actively checking out and also save the customer’s payment method to present to them as a saved payment method for future purchases, you must explicitly collect consent from the customer. One way to do so is with a “Save my payment method for future use” checkbox.
