<!-- Source URL: https://docs.stripe.com/terminal/features/saving-payment-details/save-after-payment -->
<!-- Fetched: 2026-05-01 -->

# Save payment details after payment

Accept an in-person payment and save payment details to use later, when the customer is not present.

> #### Use the Accounts v2 API to represent customers
>
> The Accounts v2 API is generally available for Connect users, and in public preview for other Stripe users. If you’re part of the Accounts v2 preview, you need to specify a [specify a preview version](https://docs.stripe.com/api-v2-overview.md#sdk-and-api-versioning) in your code.
>
> To request access to the Accounts v2 preview,
>
> For most use cases, we recommend [modeling your customers as customer-configured Account objects](https://docs.stripe.com/connect/use-accounts-as-customers.md) instead of using [Customer](https://docs.stripe.com/api/customers.md) objects.

You can use Stripe Terminal to save payment details from an in-store purchase. A successful `card_present` payment returns a reusable `card` PaymentMethod in the `generated_card` attribute. There are several use cases:

- A gym customer pays in person for an initial session and a membership subscription. The transaction sets up a `generated_card` to use for future automatic membership renewals.
- A customer at a clothing store provides their email address when making a purchase at the checkout counter. The transaction creates a customer record and an associated saved `generated_card`. That allows the customer to log into the store’s website later and place an order using the same card.

> The initial, in-person payment is a card-present transaction. All subsequent charges made using the `generated_card` are card-not-present (CNP) transactions, and features available to card-present transactions (such as _liability shifts_ (With some 3D Secure transactions, the liability for fraudulent chargebacks (stolen or counterfeit cards) shifts from you to the card issuer) and [pricing](https://stripe.com/terminal#pricing)) don’t apply to these subsequent charges.

> We’ve changed the customer consent model of this feature to require the `allow_redisplay` parameter. You must update your integration to use `allow_redisplay`. This update became mandatory on March 31, 2025 for non-React Native users, and is mandatory for React Native users on September 30, 2025. For guidance, see the [changelog entry](https://docs.stripe.com/changelog/acacia/2024-09-30/terminal-remove-customer-consent-require-allow-redisplay.md).

# Server-driven

> This is a Server-driven for when terminal-sdk-platform is server-driven. View the full page at https://docs.stripe.com/terminal/features/saving-payment-details/save-after-payment?terminal-sdk-platform=server-driven.

## Create a customer

To set up a payment method for future payments, you must attach it to an object that represents your customer. When your customer creates an account or has their first transaction with your business, create either a customer-configured [Account](https://docs.stripe.com/api/v2/core/accounts/create.md) object with the Accounts v2 API or a [Customer](https://docs.stripe.com/api/customers/create.md) object with the Customers API.

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const account = await stripe.v2.core.accounts.create({
  contact_email: 'jenny.rosen@example.com',
  display_name: 'Jenny Rosen',
  configuration: {
    customer: {

    },
  },
  include: ['configuration.customer'],
});
```

Successful creation returns the customer-configured [Account](https://docs.stripe.com/api/v2/core/accounts/object.md#v2_account_object-configuration-customer) object. Inspect the object for the customer’s `id` and store the value in your database for later retrieval.

#### Customers v1

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const customer = await stripe.customers.create({
  name: 'Jenny Rosen',
  email: 'jennyrosen@example.com',
});
```

Successful creation returns the [Customer](https://docs.stripe.com/api/customers/object.md) object. Inspect the object for the customer’s `id` and store the value in your database for later retrieval.

You can find these customers in the [Customers](https://dashboard.stripe.com/customers) page in the Dashboard.

## Create a PaymentIntent

- [Create a PaymentIntent](https://docs.stripe.com/api/payment_intents/create.md)

Request a `generated_card` when you create a PaymentIntent by specifying a value for [setup_future_usage](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-setup_future_usage). If you intend to only reuse the payment method when the customer is present in the checkout flow, use `on_session`. Otherwise, use `off_session`.

#### Node.js

```javascript

// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const intent = await stripe.paymentIntents.create({
  amount: 1000,
  currency: 'sgd',
  payment_method_types: ['card_present'],
  setup_future_usage: 'off_session',
  customer: '{{CUSTOMER_ID}}'
});
```

> Visa, Mastercard, American Express, Discover, co-branded eftpos, co-branded Interac, and co-branded girocard cards are supported as `card_present` payment methods that can be saved as type `card`.

## Collect and process a payment method

> This feature requires your API requests to include `Stripe-Version: 2024-09-30.acacia`. For guidance, see the [changelog entry](https://docs.stripe.com/changelog/acacia/2024-09-30/terminal-remove-customer-consent-require-allow-redisplay.md).

- [process_payment_intent](https://docs.stripe.com/api/terminal/readers/process_payment_intent.md)

- [collect_payment_method](https://docs.stripe.com/api/terminal/readers/collect_payment_method.md)

When the customer is ready to pay and has [consented to their payment method details being saved](https://docs.stripe.com/terminal/features/saving-payment-details/save-after-payment.md#compliance), pass [allow_redisplay](https://docs.stripe.com/api/payment_methods/object.md#payment_method_object-allow_redisplay) as `always` or `limited` into the `process_payment_intent` or `collect_payment_method`(Preview) call. The value indicates the degree to which a payment method can be shown in a customer checkout flow.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const reader = await stripe.terminal.readers.processPaymentIntent(
  '{{READER_ID}}',
  {
    payment_intent: '{{PAYMENT_INTENT_ID}}',
    process_config: {
      allow_redisplay: 'always',
    },
  }
);
```

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const reader = await stripe.terminal.readers.collectPaymentMethod(
  '{{READER_ID}}',
  {
    payment_intent: '{{PAYMENT_INTENT_ID}}',
    collect_config: {
      allow_redisplay: 'always',
    },
  }
);
```

- [confirm_payment_intent](https://docs.stripe.com/api/terminal/readers/confirm_payment_intent.md)

If you use the `collect_payment_method` flow, which allows access to useful data like card brand and funding from the PaymentMethod before confirming it, you must also separately confirm the PaymentIntent.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const reader = await stripe.terminal.readers.confirmPaymentIntent(
  '{{READER_ID}}',
  {
    payment_intent: '{{PAYMENT_INTENT_ID}}',
  }
);
```

## Access the generated_card

A successful payment with a method that supports future use returns a PaymentIntent in the `requires_capture` or `succeeded` state. You can retrieve the [generated_card](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-card_present-generated_card) payment method by expanding the PaymentIntent’s [latest_charge](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-latest_charge) property and viewing [payment_method_details.card_present](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-card_present). If you passed the customer ID into the PaymentIntent creation call, the reusable PaymentMethod is automatically attached to the [Customer](https://docs.stripe.com/api/customers.md) object. Otherwise, you can [manually attach it](https://docs.stripe.com/api/payment_methods/attach.md) in a separate call.

Always verify that the [PaymentIntent.latest_charge](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-latest_charge) contains a `generated_card` value. Some payments, such as digital wallet payments and single-branded Interac, eftpos, or girocard card payments, might not create a generated card. If that happens, and you require a reusable payment method, you have two options:

- Prompt the customer to save a different payment method using the flow to [save a payment method without taking a payment](https://docs.stripe.com/terminal/features/saving-payment-details/save-directly.md).
- Refund the in-person payment, indicate that the transaction failed, and instruct the customer to use a different payment method.

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

> This is a JavaScript for when terminal-sdk-platform is js. View the full page at https://docs.stripe.com/terminal/features/saving-payment-details/save-after-payment?terminal-sdk-platform=js.

## Create a customer

To set up a payment method for future payments, you must attach it to an object that represents your customer. When your customer creates an account or has their first transaction with your business, create either a customer-configured [Account](https://docs.stripe.com/api/v2/core/accounts/create.md) object with the Accounts v2 API or a [Customer](https://docs.stripe.com/api/customers/create.md) object with the Customers API.

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const account = await stripe.v2.core.accounts.create({
  contact_email: 'jenny.rosen@example.com',
  display_name: 'Jenny Rosen',
  configuration: {
    customer: {

    },
  },
  include: ['configuration.customer'],
});
```

Successful creation returns the customer-configured [Account](https://docs.stripe.com/api/v2/core/accounts/object.md#v2_account_object-configuration-customer) object. Inspect the object for the customer’s `id` and store the value in your database for later retrieval.

#### Customers v1

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const customer = await stripe.customers.create({
  name: 'Jenny Rosen',
  email: 'jennyrosen@example.com',
});
```

Successful creation returns the [Customer](https://docs.stripe.com/api/customers/object.md) object. Inspect the object for the customer’s `id` and store the value in your database for later retrieval.

You can find these customers in the [Customers](https://dashboard.stripe.com/customers) page in the Dashboard.

## Create a PaymentIntent

- [Create a PaymentIntent](https://docs.stripe.com/api/payment_intents/create.md)

Request a `generated_card` when you create a PaymentIntent by specifying a value for [setup_future_usage](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-setup_future_usage). If you intend to only reuse the payment method when the customer is present in the checkout flow, use `on_session`. Otherwise, use `off_session`.

#### Node.js

```javascript

// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const intent = await stripe.paymentIntents.create({
  amount: 1000,
  currency: 'sgd',
  payment_method_types: ['card_present'],
  setup_future_usage: 'off_session',
  customer: '{{CUSTOMER_ID}}'
});
```

> Visa, Mastercard, American Express, Discover, co-branded eftpos, co-branded Interac, and co-branded girocard cards are supported as `card_present` payment methods that can be saved as type `card`.

## Collect and process a payment method

- [collectPaymentMethod (JavaScript)](https://docs.stripe.com/terminal/references/api/js-sdk.md#collect-payment-method)

When the customer is ready to pay and has [consented to their payment method details being saved](https://docs.stripe.com/terminal/features/saving-payment-details/save-after-payment.md#compliance), pass [allow_redisplay](https://docs.stripe.com/api/payment_methods/object.md#payment_method_object-allow_redisplay) as `always` or `limited` into the `collectPaymentMethod` call. The value indicates the degree to which a payment method can be shown in a customer checkout flow.

```javascript
async () => {
  // clientSecret is the client_secret from the PaymentIntent you created in Step 2.
  const result = await terminal.collectPaymentMethod(clientSecret, { config_override: {
      allow_redisplay: "always"
    } });
  if (result.error) {
    // Placeholder for handling result.error
  } else {
    // Placeholder for confirming result.paymentIntent
  }
}
```

## Access the generated_card

A successful payment with a method that supports future use returns a PaymentIntent in the `requires_capture` or `succeeded` state. You can retrieve the [generated_card](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-card_present-generated_card) payment method by expanding the PaymentIntent’s [latest_charge](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-latest_charge) property and viewing [payment_method_details.card_present](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-card_present). If you passed the customer ID into the PaymentIntent creation call, the reusable PaymentMethod is automatically attached to the [Customer](https://docs.stripe.com/api/customers.md) object. Otherwise, you can [manually attach it](https://docs.stripe.com/api/payment_methods/attach.md) in a separate call.

Always verify that the [PaymentIntent.latest_charge](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-latest_charge) contains a `generated_card` value. Some payments, such as digital wallet payments and single-branded Interac, eftpos, or girocard card payments, might not create a generated card. If that happens, and you require a reusable payment method, you have two options:

- Prompt the customer to save a different payment method using the flow to [save a payment method without taking a payment](https://docs.stripe.com/terminal/features/saving-payment-details/save-directly.md).
- Refund the in-person payment, indicate that the transaction failed, and instruct the customer to use a different payment method.

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

> This is a iOS for when terminal-sdk-platform is ios. View the full page at https://docs.stripe.com/terminal/features/saving-payment-details/save-after-payment?terminal-sdk-platform=ios.

## Create a customer

To set up a payment method for future payments, you must attach it to an object that represents your customer. When your customer creates an account or has their first transaction with your business, create either a customer-configured [Account](https://docs.stripe.com/api/v2/core/accounts/create.md) object with the Accounts v2 API or a [Customer](https://docs.stripe.com/api/customers/create.md) object with the Customers API.

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const account = await stripe.v2.core.accounts.create({
  contact_email: 'jenny.rosen@example.com',
  display_name: 'Jenny Rosen',
  configuration: {
    customer: {

    },
  },
  include: ['configuration.customer'],
});
```

Successful creation returns the customer-configured [Account](https://docs.stripe.com/api/v2/core/accounts/object.md#v2_account_object-configuration-customer) object. Inspect the object for the customer’s `id` and store the value in your database for later retrieval.

#### Customers v1

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const customer = await stripe.customers.create({
  name: 'Jenny Rosen',
  email: 'jennyrosen@example.com',
});
```

Successful creation returns the [Customer](https://docs.stripe.com/api/customers/object.md) object. Inspect the object for the customer’s `id` and store the value in your database for later retrieval.

You can find these customers in the [Customers](https://dashboard.stripe.com/customers) page in the Dashboard.

## Create a PaymentIntent

- [Create a PaymentIntent](https://docs.stripe.com/api/payment_intents/create.md)

Request a `generated_card` when you create a PaymentIntent by specifying a value for [setup_future_usage](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-setup_future_usage). If you intend to only reuse the payment method when the customer is present in the checkout flow, use `on_session`. Otherwise, use `off_session`.

#### Node.js

```javascript

// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const intent = await stripe.paymentIntents.create({
  amount: 1000,
  currency: 'sgd',
  payment_method_types: ['card_present'],
  setup_future_usage: 'off_session',
  customer: '{{CUSTOMER_ID}}'
});
```

> Visa, Mastercard, American Express, Discover, co-branded eftpos, co-branded Interac, and co-branded girocard cards are supported as `card_present` payment methods that can be saved as type `card`.

## Collect and process a payment method

> This feature requires iOS SDK v4.3.0 or later.

- [collectPaymentMethod (iOS)](<https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPTerminal.html#/c:objc(cs)SCPTerminal(im)collectPaymentMethod:delegate:completion:>)

When the customer is ready to pay and has [consented to their payment method details being saved](https://docs.stripe.com/terminal/features/saving-payment-details/save-after-payment.md#compliance), pass [allow_redisplay](https://docs.stripe.com/api/payment_methods/object.md#payment_method_object-allow_redisplay) as `always` or `limited` into the `collectPaymentMethod` call. The value indicates the degree to which a payment method can be shown in a customer checkout flow.

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
        let params = try PaymentIntentParametersBuilder().setCustomer(""{{CUSTOMER_ID}}"").build()
        Terminal.shared.createPaymentIntent(params) { createResult, createError in
            if let error = createError {
                print("createPaymentIntent failed: \(error)")
            } else if let paymentIntent = createResult {
                print("createPaymentIntent succeeded")
                let config = try CollectConfigBuilder().setAllowRedisplay(AllowRedisplay.always).build()
                self.collectCancelable = Terminal.shared.collectPaymentMethod(paymentIntent, config) { collectResult, collectError in
                    if let error = collectError {
                        print("collectPaymentMethod failed: \(error)")
                    } else if let collectPaymentMethodPaymentIntent = collectResult {
                        print("collectPaymentMethod succeeded")
                        // ... Confirm the PaymentIntent
                        Terminal.shared.confirmPaymentIntent(collectPaymentMethodPaymentIntent) { confirmResult, confirmError in
                            if let error = confirmError {
                                print("confirmPaymentIntent failed: \(error)")
                            } else if let confirmedPaymentIntent = confirmResult {
                                print("confirmPaymentIntent succeeded")
                            }
                        }
                    }
                }
            }
        }
    }
```

## Access the generated_card

A successful payment with a method that supports future use returns a PaymentIntent in the `requires_capture` or `succeeded` state. You can retrieve the [generated_card](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-card_present-generated_card) payment method by expanding the PaymentIntent’s [latest_charge](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-latest_charge) property and viewing [payment_method_details.card_present](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-card_present). If you passed the customer ID into the PaymentIntent creation call, the reusable PaymentMethod is automatically attached to the [Customer](https://docs.stripe.com/api/customers.md) object. Otherwise, you can [manually attach it](https://docs.stripe.com/api/payment_methods/attach.md) in a separate call.

Always verify that the [PaymentIntent.latest_charge](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-latest_charge) contains a `generated_card` value. Some payments, such as digital wallet payments and single-branded Interac, eftpos, or girocard card payments, might not create a generated card. If that happens, and you require a reusable payment method, you have two options:

- Prompt the customer to save a different payment method using the flow to [save a payment method without taking a payment](https://docs.stripe.com/terminal/features/saving-payment-details/save-directly.md).
- Refund the in-person payment, indicate that the transaction failed, and instruct the customer to use a different payment method.

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

> This is a Android for when terminal-sdk-platform is android. View the full page at https://docs.stripe.com/terminal/features/saving-payment-details/save-after-payment?terminal-sdk-platform=android.

## Create a customer

To set up a payment method for future payments, you must attach it to an object that represents your customer. When your customer creates an account or has their first transaction with your business, create either a customer-configured [Account](https://docs.stripe.com/api/v2/core/accounts/create.md) object with the Accounts v2 API or a [Customer](https://docs.stripe.com/api/customers/create.md) object with the Customers API.

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const account = await stripe.v2.core.accounts.create({
  contact_email: 'jenny.rosen@example.com',
  display_name: 'Jenny Rosen',
  configuration: {
    customer: {

    },
  },
  include: ['configuration.customer'],
});
```

Successful creation returns the customer-configured [Account](https://docs.stripe.com/api/v2/core/accounts/object.md#v2_account_object-configuration-customer) object. Inspect the object for the customer’s `id` and store the value in your database for later retrieval.

#### Customers v1

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const customer = await stripe.customers.create({
  name: 'Jenny Rosen',
  email: 'jennyrosen@example.com',
});
```

Successful creation returns the [Customer](https://docs.stripe.com/api/customers/object.md) object. Inspect the object for the customer’s `id` and store the value in your database for later retrieval.

You can find these customers in the [Customers](https://dashboard.stripe.com/customers) page in the Dashboard.

## Create a PaymentIntent

- [Create a PaymentIntent](https://docs.stripe.com/api/payment_intents/create.md)

Request a `generated_card` when you create a PaymentIntent by specifying a value for [setup_future_usage](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-setup_future_usage). If you intend to only reuse the payment method when the customer is present in the checkout flow, use `on_session`. Otherwise, use `off_session`.

#### Node.js

```javascript

// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const intent = await stripe.paymentIntents.create({
  amount: 1000,
  currency: 'sgd',
  payment_method_types: ['card_present'],
  setup_future_usage: 'off_session',
  customer: '{{CUSTOMER_ID}}'
});
```

> Visa, Mastercard, American Express, Discover, co-branded eftpos, co-branded Interac, and co-branded girocard cards are supported as `card_present` payment methods that can be saved as type `card`.

## Collect and process a payment method

> This feature requires Android SDK v4.0.0 or later.

- [collectPaymentMethod (Android)](https://stripe.dev/stripe-terminal-android/core/com.stripe.stripeterminal/-terminal/collect-payment-method.html)

When the customer is ready to pay and has [consented to their payment method details being saved](https://docs.stripe.com/terminal/features/saving-payment-details/save-after-payment.md#compliance), pass [allow_redisplay](https://docs.stripe.com/api/payment_methods/object.md#payment_method_object-allow_redisplay) as `always` or `limited` into the `collectPaymentMethod` call. The value indicates the degree to which a payment method can be shown in a customer checkout flow.

#### Kotlin

```kotlin
val config = CollectPaymentIntentConfiguration.Builder()
    .setAllowRedisplay(AllowRedisplay.ALWAYS)
    .build()

val cancelable = Terminal.getInstance().collectPaymentMethod(
    paymentIntent,
    config,
    callback = object : PaymentIntentCallback {
        override fun onSuccess(paymentIntent: PaymentIntent) {
            // Placeholder for handling successful operation
        }

        override fun onFailure(e: TerminalException) {
            // Placeholder for handling exception
        }
    }
)
```

## Access the generated_card

A successful payment with a method that supports future use returns a PaymentIntent in the `requires_capture` or `succeeded` state. You can retrieve the [generated_card](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-card_present-generated_card) payment method by expanding the PaymentIntent’s [latest_charge](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-latest_charge) property and viewing [payment_method_details.card_present](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-card_present). If you passed the customer ID into the PaymentIntent creation call, the reusable PaymentMethod is automatically attached to the [Customer](https://docs.stripe.com/api/customers.md) object. Otherwise, you can [manually attach it](https://docs.stripe.com/api/payment_methods/attach.md) in a separate call.

Always verify that the [PaymentIntent.latest_charge](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-latest_charge) contains a `generated_card` value. Some payments, such as digital wallet payments and single-branded Interac, eftpos, or girocard card payments, might not create a generated card. If that happens, and you require a reusable payment method, you have two options:

- Prompt the customer to save a different payment method using the flow to [save a payment method without taking a payment](https://docs.stripe.com/terminal/features/saving-payment-details/save-directly.md).
- Refund the in-person payment, indicate that the transaction failed, and instruct the customer to use a different payment method.

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

> This is a React Native for when terminal-sdk-platform is react-native. View the full page at https://docs.stripe.com/terminal/features/saving-payment-details/save-after-payment?terminal-sdk-platform=react-native.

## Create a customer

To set up a payment method for future payments, you must attach it to an object that represents your customer. When your customer creates an account or has their first transaction with your business, create either a customer-configured [Account](https://docs.stripe.com/api/v2/core/accounts/create.md) object with the Accounts v2 API or a [Customer](https://docs.stripe.com/api/customers/create.md) object with the Customers API.

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const account = await stripe.v2.core.accounts.create({
  contact_email: 'jenny.rosen@example.com',
  display_name: 'Jenny Rosen',
  configuration: {
    customer: {

    },
  },
  include: ['configuration.customer'],
});
```

Successful creation returns the customer-configured [Account](https://docs.stripe.com/api/v2/core/accounts/object.md#v2_account_object-configuration-customer) object. Inspect the object for the customer’s `id` and store the value in your database for later retrieval.

#### Customers v1

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const customer = await stripe.customers.create({
  name: 'Jenny Rosen',
  email: 'jennyrosen@example.com',
});
```

Successful creation returns the [Customer](https://docs.stripe.com/api/customers/object.md) object. Inspect the object for the customer’s `id` and store the value in your database for later retrieval.

You can find these customers in the [Customers](https://dashboard.stripe.com/customers) page in the Dashboard.

## Create a PaymentIntent

- [Create a PaymentIntent](https://docs.stripe.com/api/payment_intents/create.md)

Request a `generated_card` when you create a PaymentIntent by specifying a value for [setup_future_usage](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-setup_future_usage). If you intend to only reuse the payment method when the customer is present in the checkout flow, use `on_session`. Otherwise, use `off_session`.

#### Node.js

```javascript

// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const intent = await stripe.paymentIntents.create({
  amount: 1000,
  currency: 'sgd',
  payment_method_types: ['card_present'],
  setup_future_usage: 'off_session',
  customer: '{{CUSTOMER_ID}}'
});
```

> Visa, Mastercard, American Express, Discover, co-branded eftpos, co-branded Interac, and co-branded girocard cards are supported as `card_present` payment methods that can be saved as type `card`.

## Collect and process a payment method

- [collectPaymentMethod (React Native)](https://stripe.dev/stripe-terminal-react-native/api-reference/interfaces/StripeTerminalSdkType.html#collectpaymentmethod)

When the customer is ready to pay and has [consented to their payment method details being saved](https://docs.stripe.com/terminal/features/saving-payment-details/save-after-payment.md#compliance), pass [allow_redisplay](https://docs.stripe.com/api/payment_methods/object.md#payment_method_object-allow_redisplay) as `always` or `limited` into the `collectPaymentMethod` call. The value indicates the degree to which a payment method can be shown in a customer checkout flow.

```js
const { paymentIntent, error } = await collectPaymentMethod({
  paymentIntent: paymentIntent.id,
  allowRedisplay: "always",
});

if (error) {
  // Placeholder for handling exception
  return;
}

// Placeholder for confirming paymentIntent
```

## Access the generated_card

A successful payment with a method that supports future use returns a PaymentIntent in the `requires_capture` or `succeeded` state. You can retrieve the [generated_card](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-card_present-generated_card) payment method by expanding the PaymentIntent’s [latest_charge](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-latest_charge) property and viewing [payment_method_details.card_present](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-card_present). If you passed the customer ID into the PaymentIntent creation call, the reusable PaymentMethod is automatically attached to the [Customer](https://docs.stripe.com/api/customers.md) object. Otherwise, you can [manually attach it](https://docs.stripe.com/api/payment_methods/attach.md) in a separate call.

Always verify that the [PaymentIntent.latest_charge](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-latest_charge) contains a `generated_card` value. Some payments, such as digital wallet payments and single-branded Interac, eftpos, or girocard card payments, might not create a generated card. If that happens, and you require a reusable payment method, you have two options:

- Prompt the customer to save a different payment method using the flow to [save a payment method without taking a payment](https://docs.stripe.com/terminal/features/saving-payment-details/save-directly.md).
- Refund the in-person payment, indicate that the transaction failed, and instruct the customer to use a different payment method.

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
